import tkinter as tk

# Function to perform actions based on keyboard input
def on_key_press(event):
    key = event.keysym
    if key == 'Up':
        # Code to move the robot forward
        print("Moving robot forward")
    elif key == 'Down':
        # Code to move the robot backward
        print("Moving robot backward")
    elif key == 'Left':
        # Code to move the robot to the left
        print("Moving robot left")
    elif key == 'Right':
        # Code to move the robot to the right
        print("Moving robot right")
    elif key == 'a':
        # Code to turn the robot left
        print("Turning robot left")
    elif key == 'd':
        # Code to turn the robot right
        print("Turning robot right")

# Function to control robot movement via buttons
def move_forward():
    # Code to move the robot forward
    print("Moving robot forward")

def move_backward():
    # Code to move the robot backward
    print("Moving robot backward")

def move_left():
    # Code to move the robot to the left
    print("Moving robot left")

def move_right():
    # Code to move the robot to the right
    print("Moving robot right")

def turn_left():
    # Code to turn the robot left
    print("Turning robot left")

def turn_right():
    # Code to turn the robot right
    print("Turning robot right")

# Create main window
root = tk.Tk()
root.title("Robot Control")

# Bind keyboard events to the function
root.bind('<KeyPress>', on_key_press)

# Configure button styles
button_style = {
    'padx': 20,
    'pady': 10,
    'font': ('Arial', 12),
    'bg': '#4CAF50',  # Background color
    'fg': 'blue',    # Text color
    'relief': 'raised'
}

# Create buttons for different movements with updated style
forward_btn = tk.Button(root, text="Forward", command=move_forward, **button_style)
forward_btn.grid(row=0, column=1)

backward_btn = tk.Button(root, text="Backward", command=move_backward, **button_style)
backward_btn.grid(row=2, column=1)

left_btn = tk.Button(root, text="Left", command=move_left, **button_style)
left_btn.grid(row=1, column=0)

right_btn = tk.Button(root, text="Right", command=move_right, **button_style)
right_btn.grid(row=1, column=2)

turn_left_btn = tk.Button(root, text="Turn Left", command=turn_left, **button_style)
turn_left_btn.grid(row=3, column=0)

turn_right_btn = tk.Button(root, text="Turn Right", command=turn_right, **button_style)
turn_right_btn.grid(row=3, column=2)

# Run the main event loop
root.mainloop()
