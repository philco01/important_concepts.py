from selenium.webdriver.common.by import By


class Click_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[type='button']")

    def verify_button(self):
        assert self.get_button().is_displayed()
