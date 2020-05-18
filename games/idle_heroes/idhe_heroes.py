from appium.webdriver.common.touch_action import TouchAction

from android import AndroidDevice
from games.idle_heroes.pages.welcome_page import WelcomePage
from image_recognizer import ImageRecognizer


class IdleHeroes:
    appium = None
    device = None
    driver = None

    def __init__(self) -> None:
        self.device = AndroidDevice("games/idle_heroes/game.apk")

    def start(self):
        self.driver = self.device.connect("http://localhost:4723/wd/hub")
        self.appium = ImageRecognizer(self.device)
        return WelcomePage(self.driver, self.device, self.appium)
