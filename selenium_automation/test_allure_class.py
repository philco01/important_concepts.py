import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_Asserts:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://admin-demo.nopcommerce.com/login")

    def teardown_class(self):
        driver.quit()

    @allure.title("Report")
    @allure.description("test for login")
    def test_allure(self):
        try:
            driver.find_element_by_class_name("email valid").send_keys("email valid")
            driver.find_element_by_id("Password").send_keys("admin")
            driver.find_element_by_css_selector("button[type='submit']").click()
            assert driver.find_element_by_css_selector("div[class='content-header'] > h1").is_displayed()
        except Exception as e:
            screen_shot = "./screenshot/screen.png"
            driver.get_screenshot_as_file(screen_shot)
            allure.attach.file(screen_shot, attachment_type=allure.attachment_type.PNG)
            pytest.fail("fail")


            # fluent pattern allow to concatinate methods


