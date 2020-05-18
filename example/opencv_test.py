import cv2

use_mask = False
img = None
templ = None
mask = None
image_window = "Idle Heroes"
result_window = "Close Button"

match_method = 0
max_Trackbar = 5


def matching_method(param):
    global match_method
    global image_window
    match_method = param

    img_display = img.copy()

    method_accepts_mask = (
        cv2.TM_SQDIFF == match_method or match_method == cv2.TM_CCORR_NORMED
    )
    if use_mask and method_accepts_mask:
        result = cv2.matchTemplate(img, templ, match_method, None, mask)
    else:
        result = cv2.matchTemplate(img, templ, match_method)

    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)

    if match_method == cv2.TM_SQDIFF or match_method == cv2.TM_SQDIFF_NORMED:
        matchLoc = minLoc
    else:
        matchLoc = maxLoc

    cv2.rectangle(
        img_display,
        matchLoc,
        (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]),
        (0, 0, 0),
        2,
        8,
        0,
    )
    cv2.rectangle(
        result,
        matchLoc,
        (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]),
        (0, 0, 0),
        2,
        8,
        0,
    )
    cv2.imshow(image_window, img_display)
    cv2.imshow(result_window, result)

    pass


def main():
    # test locally

    global img
    global templ
    global image_window
    img = cv2.imread("../games/idle_heroes/images/home/idle.png", cv2.IMREAD_COLOR)
    templ = cv2.imread(
        "../games/idle_heroes/images/home/idle_close.png", cv2.IMREAD_COLOR
    )
    if False:
        global use_mask
        use_mask = True
        global mask
        mask = cv2.imread(sys.argv[3], cv2.IMREAD_COLOR)

    cv2.namedWindow(image_window, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(result_window, cv2.WINDOW_AUTOSIZE)

    trackbar_label = "Method: \n 0: SQDIFF \n 1: SQDIFF NORMED \n 2: TM CCORR \n 3: TM CCORR NORMED \n 4: TM COEFF \n 5: TM COEFF NORMED"
    cv2.createTrackbar(
        trackbar_label, image_window, match_method, max_Trackbar, matching_method
    )

    matching_method(match_method)

    cv2.waitKey(0)
    return 0
