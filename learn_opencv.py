from android import AndroidDevice
from opencv import OpenCV

device = AndroidDevice("games/idle_heroes/game.apk")
device.take_screen_shot()
OpenCV().match_image(
    "games/idle_heroes/images/screenshot.png",
    "games/idle_heroes/images/home/idle_close.png",
)
