from appium.webdriver.common.touch_action import TouchAction


class WelcomePage:
    appium = None
    device = None
    driver = None

    def __init__(self, driver, device, appium) -> None:
        self.driver = driver
        self.device = device
        self.appium = appium

    def guess_login(self):
        self.__close_popup()
        actions = TouchAction(self.driver)
        size = self.device.get_device_size()
        center_x = size[0] / 2
        center_y = size[1] / 2
        actions.tap(None, center_x, center_y, 1).perform()

    def member_login(self, username, password):
        if username is None:
            raise ValueError
        if password is None:
            raise ValueError

        self.__close_popup()
        match_location = self.appium.find_by(
            "games/idle_heroes/images/home/login_profile.png"
        )
        print("Location to tap: ", match_location)
        actions = TouchAction(self.driver)
        actions.tap(None, match_location[0], match_location[1], 1).perform()

    def __close_popup(self):
        match_location = self.appium.find_by(
            "games/idle_heroes/images/home/idle_close.png"
        )
        print("Location to tap: ", match_location)
        actions = TouchAction(self.driver)
        actions.tap(None, match_location[0], match_location[1], 1).perform()
