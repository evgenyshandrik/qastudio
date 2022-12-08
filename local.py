from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def create_driver():
    cap = {
        "appium:platformName": "Android",
        "appium:udid": "emulator-5554",
        "appium:app": "(path to apk file)",
        "appium:appActivity": "com.chess.splash.SplashActivity",
        "appium:appPackage": "com.chess"
    }

    return webdriver.Remote("http://0.0.0.0:4723/wd/hub", cap)


def test_login():
    driver = create_driver()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button'))).click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (AppiumBy.ID, 'com.chess:id/log_in'))).click()

    assert WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((AppiumBy.ID, 'com.chess:id/text'))).text == 'Log In'
