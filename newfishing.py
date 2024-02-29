import pyautogui
import time
import random

# Function to find the position of a specific color on the screen
def find_color_on_screen(expected_color):
    # Capture the screen
    screenshot = pyautogui.screenshot()
    # Check for the specific color on the entire screen
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            actual_color = screenshot.getpixel((x, y))
            if actual_color == expected_color:
                return x, y
    return None, None

# Function to perform a click
def click(x, y):
    pyautogui.click(x, y)

# Main function
def main():
    # Expected color (put your RGB value here)
    expected_color = (0, 230, 250)  # Example: (0, 230, 250)
    
    # Set the click distance from the detected color position (in pixels)
    click_distance_x = 190  # Example: 20 pixels from x axis
    click_distance_y = 120  # Example: 20 pixels from y axis
    
    # Set the range of random clicks around the detected color position (in pixels)
    random_click_range = 30  # Example: 10 pixels
    
    while True:
        # If the specific color is found on the screen
        target_x, target_y = find_color_on_screen(expected_color)
        if target_x is not None and target_y is not None:
            # Calculate random click position within the specified range
            random_x = random.randint(target_x - random_click_range, target_x + random_click_range)
            random_y = random.randint(target_y - random_click_range, target_y + random_click_range)
            
            # Calculate the click position within the specified distance from the detected color position
            click_x = min(max(random_x, target_x - click_distance_x), target_x + click_distance_x)
            click_y = min(max(random_y, target_y - click_distance_y), target_y + click_distance_y)
            
            # Perform the click
            click(click_x, click_y)
            
            # Add randomness to the click time (Example: random time between 0.5 seconds and 1.5 seconds)
            random_sleep_time = random.uniform(0.5, 1.5)
            time.sleep(random_sleep_time)

