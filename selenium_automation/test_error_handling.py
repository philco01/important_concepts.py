import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium_automation.event_listener import EventListener


class Test_Error_Handling:
    def setup_class(self):
        global driver
        edriver = webdriver.Chrome(ChromeDriverManager().install())
        driver = EventFiringWebDriver(edriver, EventListener())
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def teardown_class(self):
        driver.quit()

    def test_check_errors(self):
        try:
            driver.find_element_by_id("btn").click()
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='checkbox']").is_displayed()
        except Exception as s:
            print("test failed")
        finally:
            print("test is done")

    def test_optimized_check(self):



