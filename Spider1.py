from adafruit_servokit import ServoKit
import time

# Initialize the servo kit with 16 channels
kit = ServoKit(channels=16)

# Define servo angles for each leg (adjust angles as needed)
leg1_angles = [90, 90, 90]
leg2_angles = [90, 90, 90]
leg3_angles = [90, 90, 90]
leg4_angles = [90, 90, 90]
leg5_angles = [90, 90, 90]
leg6_angles = [90, 90, 90]

def set_leg_positions(leg_angles):
    # Set the position for each servo in the leg
    for i in range(3):
        kit.servo[i].angle = leg_angles[i]

# Set initial leg positions
set_leg_positions(leg1_angles)
set_leg_positions(leg2_angles)
set_leg_positions(leg3_angles)
set_leg_positions(leg4_angles)
set_leg_positions(leg5_angles)
set_leg_positions(leg6_angles)

# Delay for a moment
time.sleep(1)

# Move the hexapod (you can implement various gaits and movements here)
# Example: Move one leg forward
leg1_angles = [45, 90, 135]
set_leg_positions(leg1_angles)

# Delay for a moment
time.sleep(1)

# Return all legs to the initial position
set_leg_positions(leg1_angles)
set_leg_positions(leg2_angles)
set_leg_positions(leg3_angles)
set_leg_positions(leg4_angles)
set_leg_positions(leg5_angles)
set_leg_positions(leg6_angles)

# Cleanup
kit.deinit()
