from appium import webdriver

user = 'user'
key = 'key'

desired_cap = {
    "app": "bs://<hash app>",
    "platformName": "Android",
    "appPackage": "com.chess",
    "deviceName": "Google Pixel 5",
    "appActivity": "com.chess.splash.SplashActivity"
}

driver = webdriver.Remote(
    command_executor=f"http://{user}:{key}@hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

driver.quit()
