from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.test_page_object_pattern.click_page import Click_Page
from selenium_automation.test_page_object_pattern.form_page import Form_Page
from selenium_automation.test_page_object_pattern.login_page import Login_Page


class Test_Random:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://admin-demo.nopcommerce.com")
        login_page = Login_Page(driver)
        from_page = Form_Page(driver)
        click_page = Click_Page(driver)

    def teardown_class(self):
        driver.quit()

    def test_verify_login(self):
        self.login_page.signup()
