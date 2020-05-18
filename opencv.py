import cv2
import numpy as np


class OpenCV:
    def find_in_image(
        self, image, template, match_method=cv2.TM_CCOEFF_NORMED, mask_path=None
    ):
        method_accepts_mask = (
            cv2.TM_SQDIFF == match_method or match_method == cv2.TM_CCORR_NORMED
        )

        if mask_path and method_accepts_mask:
            mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)
            result = cv2.matchTemplate(image, template, match_method, None, mask)
        else:
            result = cv2.matchTemplate(image, template, match_method)

        print("Points are: ", result)
        # optionally normalize here
        return result

    def match_images(
        self,
        search_in_path,
        search_for_path,
        match_method=cv2.TM_CCOEFF_NORMED,
        mask_with_path=None,
        threshold=0.8,
    ):
        image_url = None
        image = cv2.imread(search_in_path, cv2.IMREAD_COLOR)
        template = cv2.imread(search_for_path, cv2.IMREAD_COLOR)
        result = self.find_in_image(image, template, match_method, mask_with_path)
        match_locations = np.where(result >= threshold)
        print("Matching points:", match_locations)

        any_match = any(map(lambda x: x.size > 0, match_locations))
        print("Have at least one match:", any_match)

        if any_match:
            print("Match found. Writing image")
            img_display = image.copy()
            self.print_all_match(img_display, template, match_locations)
            image_url = "games/idle_heroes/images/result.png"
            cv2.imwrite(image_url, img_display)

        return match_locations

    def match_image(
        self,
        search_in_path,
        search_for_path,
        match_method=cv2.TM_CCOEFF_NORMED,
        mask_with_path=None,
        threshold=0.8,
    ):
        image_url = None
        center = None
        image = cv2.imread(search_in_path, cv2.IMREAD_COLOR)
        template = cv2.imread(search_for_path, cv2.IMREAD_COLOR)
        found_image = self.find_in_image(image, template, match_method, mask_with_path)
        top_left = self.best_match(found_image, match_method)
        top_left_y = top_left[1]
        top_left_x = top_left[0]

        print("Result point: ", found_image[top_left_y][top_left_x])
        print("Threshold: ", threshold)

        print("Image shape: ", template.shape)
        template_height, template_width, template_channel = template.shape

        if top_left and found_image[top_left_y][top_left_x] >= threshold:
            print("Match found (X,Y):", top_left_x, top_left_y)
            img_display = image.copy()
            self.print_single_match(img_display, template, top_left)
            image_url = "games/idle_heroes/images/result.png"
            cv2.imwrite(image_url, img_display)
            center = (top_left_x + template_width / 2, top_left_y + template_height / 2)
            print("Returning center:", center)
        else:
            print(
                "Match not found ",
                top_left,
                "or value is under threshold: ",
                found_image[top_left_y][top_left_x],
            )
            image_url = "games/idle_heroes/images/result.png"
            cv2.imwrite(image_url, image)

        return center

    def best_match(self, result, match_method):
        _minVal, _maxVal, min_loc, max_loc = cv2.minMaxLoc(result, None)
        if match_method == cv2.TM_SQDIFF or match_method == cv2.TM_SQDIFF_NORMED:
            match_loc = min_loc
        else:
            match_loc = max_loc
        return match_loc

    def print_single_match(self, printed_image, template, match_location):
        rows = template.shape[0]
        columns = template.shape[1]
        cv2.rectangle(
            printed_image,
            match_location,
            # shape returns first ROW then COLUMNS, which means add COLUMNS to X axis
            (match_location[0] + columns, match_location[1] + rows),
            (0, 0, 255),
            2,
        )

    def print_all_match(self, printed_image, template, match_locations):
        for location in zip(*match_locations[::-1]):
            self.print_single_match(printed_image, template, location)

    def normalize(self, image, method=cv2.NORM_MINMAX):
        normalized_result = cv2.normalize(image, None, 0, 1, method, dtype=cv2.CV_32F)
        print("Normalized points are: ", normalized_result)
        return normalized_result
