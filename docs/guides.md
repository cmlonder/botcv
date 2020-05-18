# Guides
You can find used libraries in this project here.

## OpenCV
We are using [OpenCV](https://docs.opencv.org/4.3.0/) to image recognation.
### Template Matching
We are using Template Matching method to recognize objects in the screen. 
Read tutorial [here](https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html)
Most important point is do NOT take screenshot within an image to match the object. For instance;
if you want to get a car within an image then try to match that car with the image, don't take screenshot.
Instead CROP car from original image and save it. Then try to match that cropped car with the original image.

## Appium
We are using [Appium](https://github.com/appium/appiu) to automate Mobile/Web operations. It is a library extend from Selenium.
### Python Client
Read more [here](https://pypi.org/project/Appium-Python-Client/)

## ADB
We are using [Android Debug Bridge](https://developer.android.com/studio/command-line/adb) to take snapshots
etc. from connected phone. Although it has python library, currently we are running it as a sub process to not slow down
automation.