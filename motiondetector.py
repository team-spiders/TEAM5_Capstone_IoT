import RPi.GPIO as GPIO
import time
import picamera
import datetime
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'sudip@gmail.com'
SMTP_PASSWORD = 'password'
TO_EMAIL = 'recipient_email@example.com'
FROM_EMAIL = 'sudip@gmail.com'

# GPIO pin for motion sensor
pir_sensor = 11

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

# initialize camera
camera = picamera.PiCamera()

# initialize variables
first_frame = None
motion_detected = False

# capture first frame
def capture_first_frame():
    global first_frame
    camera.start_preview()
    time.sleep(2)
    camera.capture('first_frame.jpg')
    camera.stop_preview()
    first_frame = cv2.imread('first_frame.jpg')

# capture video and detect motion
def detect_motion():
    global first_frame, motion_detected
    camera.start_preview()
    time.sleep(2)
    while True:
        current_frame = capture_frame()
        if first_frame is None:
            first_frame = current_frame
            continue
        delta_frame = cv2.absdiff(first_frame, current_frame)
        gray_frame = cv2.cvtColor(delta_frame, cv2.COLOR_BGR2GRAY)
        blur_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
        _, threshold_frame = cv2.threshold(blur_frame, 20, 255, cv2.THRESH_BINARY)
        dilated_frame = cv2.dilate(threshold_frame, None, iterations=2)
        contours, _ = cv2.findContours(dilated_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 10000:
                continue
            motion_detected = True
            send_alert()
        first_frame = current_frame
    camera.stop_preview()

# capture frame
def capture_frame():
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
    frame = cv2.imdecode(data, 1)
    return frame

# send alert via email
def send_alert():
    global motion_detected
    msg = MIMEMultipart()
    msg['Subject'] = 'Motion detected in baby monitoring system'
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    with open('frame.jpg', 'wb') as file:
        camera.capture(file)
    with open('frame.jpg', 'rb') as file:
        img = MIMEImage(file.read())
        msg.attach(img)
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    server.quit()
    motion_detected = False
    print('Alert sent')

# main function
def main():
    capture_first_frame()
    detect_motion()

# execute main function
if __name__ == '__main__':
    main()

# cleanup GPIO
GPIO.cleanup()
