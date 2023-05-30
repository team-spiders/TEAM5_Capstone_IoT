
import RPi.GPIO as GPIO #to control the GPIO pins of raspberry pi
import time
import telebot
import cv2

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the PIR sensor output
pir_pin = 4

# Set the pin as input
GPIO.setup(pir_pin, GPIO.IN)

# Initialize the Telegram bot
bot_token = '5799122232:AAECPj_9B4EsLx5s3MTuWoQfbd49HgAZttA'
chat_id = '2036970866'
bot = telebot.TeleBot(bot_token)

# Initialize the camera
camera = cv2.VideoCapture(0)

# Set initial state and timestamps
motion_detected = False
motion_start_time = 0
motion_count = 0
image_count = 0

# Thresholds for motion detection
motion_threshold = 3  # Number of consecutive detections to trigger motion
motion_duration = 5   # Minimum duration of motion (in seconds)
image_interval = 10    # Interval between sending images (in seconds)

def send_photo(photo_path, caption):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=caption)

try:
    while motion_count < 3:
        if GPIO.input(pir_pin):
            if not motion_detected:
                motion_detected = True
                motion_start_time = time.time()
        else:
            if motion_detected:
                motion_detected = False
                motion_start_time = 0
                motion_count += 1

        # Check if motion has been detected for the required duration
        if motion_detected and (time.time() - motion_start_time >= motion_duration):
            print("Motion detected!")
            # Capture a photo
            ret, frame = camera.read()
            if ret:
                photo_path = '/home/pi/photo.jpg'
                cv2.imwrite(photo_path, frame)
                # Send the photo via Telegram with a caption
                caption = 'Motion detected!'
                send_photo(photo_path, caption)
                image_count += 1
                if image_count == 3:
                    break
                time.sleep(image_interval)  # Wait for the specified interval before capturing another photo
        else:
            print("No motion detected.")
            time.sleep(2)  # Pause between readings

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
    camera.release()
