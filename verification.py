import cv2
import numpy as np
import time

def task_example(robot, image, dataTest):
    if dataTest.end_time is None:
        dataTest.end_time = time.time() + 10

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    led_count = len([c for c in contours if cv2.contourArea(c) > 10])

    success = led_count > 0
    desc = f"{led_count} LED(s) detected."
    text = desc

    return dataTest, text, Result(success, desc)
