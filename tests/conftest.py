import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("detach", True)
    chromeOptions.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.media_stream_mic" : 1,
            "profile.default_content_setting_values.media_stream_camera" : 1,
            "profile.default_content_setting_values.geolocation" : 1,
            "profile.default_content_setting_values.notification" : 1,
        }
    )

    driver = webdriver.Chrome(options = chromeOptions)
    driver.implicitly_wait(10)
    driver.maximize_window()

    url = "https://saucedemo.com/"
    driver.get(url)

    yield driver
    
    driver.quit()