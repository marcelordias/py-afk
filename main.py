import pyautogui
import math

def move_cursor_in_circle(delay):
    radius = max(5, delay * 5)
    steps = max(10, int(delay * 30))
    center_x, center_y = pyautogui.position()

    print(f"🌀 Moving cursor in circular motion with radius {radius}... Press Ctrl+C to stop.")
    try:
        while True:
            for i in range(steps):
                angle = 2 * math.pi * (i / steps)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                pyautogui.moveTo(x, y, duration=delay / steps)
    except KeyboardInterrupt:
        print("🔴 Stopped by user.")

def main():
    try:
        delay = float(input("Enter delay in seconds (e.g., 10): "))
        if delay <= 0:
            raise ValueError("Delay must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    move_cursor_in_circle(delay)

if __name__ == "__main__":
    main()