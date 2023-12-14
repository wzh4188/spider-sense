import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading


# Function to control robot movement via keyboard
def on_key_press(event):
    key = event.keysym.lower()
    if key == 'w':
        move_forward()
    elif key == 's':
        move_backward()
    elif key == 'a':
        move_left()
    elif key == 'd':
        move_right()
    elif key == 'left':
        turn_left()
    elif key == 'right':
        turn_right()


# Function to move the robot forward
def move_forward():
    print("Moving robot forward")


# Function to move the robot backward
def move_backward():
    print("Moving robot backward")


# Function to move the robot left
def move_left():
    print("Moving robot left")


# Function to move the robot right
def move_right():
    print("Moving robot right")


# Function to turn the robot left
def turn_left():
    print("Turning robot left")


# Function to turn the robot right
def turn_right():
    print("Turning robot right")


# Function to continuously update the video feed
def update_video_feed():
    cap = cv2.VideoCapture(0)  # Use the appropriate camera index if multiple cameras are available

    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            video_label.config(image=img)
            video_label.image = img
        else:
            print("Error: Unable to capture frame")
            break

    cap.release()


# Create main window
root = tk.Tk()
root.title("Robot Control")

# Create a label to display the video feed
video_label = tk.Label(root, width=640, height=480)
video_label.pack()

# Bind keyboard events to the function
root.bind("<KeyPress>", on_key_press)

# Create buttons for robot control
forward_btn = tk.Button(root, text="Forward (w)", width=15, command=move_forward)
forward_btn.pack()

backward_btn = tk.Button(root, text="Backward (s)", width=15, command=move_backward)wwwww
backward_btn.pack()

left_btn = tk.Button(root, text="Left (a)", width=15, command=move_left)
left_btn.pack()

right_btn = tk.Button(root, text="Right (d)", width=15, command=move_right)
right_btn.pack()

turn_left_btn = tk.Button(root, text="Turn Left (Left)", width=15, command=turn_left)
turn_left_btn.pack()

turn_right_btn = tk.Button(root, text="Turn Right (Right)", width=15, command=turn_right)
turn_right_btn.pack()


# Start a thread for updating the video feed
video_thread = threading.Thread(target=update_video_feed)
video_thread.daemon = True
video_thread.start()

# Run the main event loop
root.mainloop()
