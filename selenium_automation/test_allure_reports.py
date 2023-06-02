import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test_Allure_Reports:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://admin-demo.nopcommerce.com")

    def teardown_class(self):
        driver.quit()

    @allure.title("Login")
    @allure.description("make login with given password and male")
    def test_make_report(self):
        try:
            self.insert_mail("admin@yourstore.com")
            self.insert_password("admin")
            self.click_login()
            self.verify_login()
        except:
            self.attach_file()
            pytest.fail("test is failed")
        finally:
            print("test done!! report created")


    @allure.step("insert email")
    def insert_mail(self, mail):
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys(mail)

    @allure.step("insert given pas")
    def insert_password(self, password):
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys(password)

    @allure.step("click on button")
    def click_login(self):
        driver.find_element_by_css_selector("button[type='submit']").click()

    @allure.step("verify if current url is wright")
    def verify_login(self):
        title = "https://admin-demo.nopcommerce.com/admi/"
        assert driver.current_url == title

    @allure.step("attach sreenshot of fail")
    def attach_file(self):
        image = "C:/Users/philip itkin/PycharmProjects/pythonProject/selenium_automation/screen.png"
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)




