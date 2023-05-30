##camera test

import cv2

def test_camera():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (change if using multiple cameras)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error opening the camera.")
        return

    # Read and display frames from the camera
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if frame reading was successful
        if not ret:
            print("Error reading the frame.")
            break

        # Display the frame in a window named "Camera Feed"
        cv2.imshow("Camera Feed", frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to test the camera
test_camera()
