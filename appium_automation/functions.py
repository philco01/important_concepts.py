from selenium.webdriver.common.by import By

username = "company"
password = "company"
class Form_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(By.XPATH, "//*[@id='usernameTextField']").send_keys(username)

    def get_password(self):
        return self.driver.find_element(By.XPATH, "//*[@id='passwordTextField']").send_keys(password)

    def click_button(self):
        self.driver.find_element_by_xpath("//*[@text='Login']").click()

    def action(self, ocupation, age, location):
        self.get_occupation().send_keys(ocupation)
        self.get_age()
        self.get_location().send_keys("Israel")
        self.click_button()