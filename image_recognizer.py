import time

from opencv import OpenCV


class ImageRecognizer:
    device = None

    def __init__(self, device) -> None:
        self.device = device

    def find_by(self, search_for_path, match_all=False, retry_count=10, delay_ms=5.0):
        count = 0
        match_location = None
        open_cv = OpenCV()
        while count < retry_count and not match_location:
            if count != 0:
                time.sleep(delay_ms)
            count = count + 1
            print("Trying time:", count)
            screen_shot_path = self.device.take_screen_shot()
            if match_all:
                match_location = open_cv.match_images(screen_shot_path, search_for_path)
            else:
                match_location = open_cv.match_image(screen_shot_path, search_for_path)
        return match_location
