from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(By.ID, "text")

    def get_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")

    def click_button(self):
        self.driver.find_element(By.ID, "submit")

    def signup(self):
        self.get_username().send_keys("selenium")
        self.get_password().send_keys("webdriver")
        self.click_button()
