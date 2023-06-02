from selenium.webdriver.common.by import By


class Form_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_occupation(self):
        return self.driver.find_element(By.ID, "occupation")

    def get_age(self):
        return self.driver.find_element(By.ID, "age")

    def get_location(self):
        self.driver.find_element(By.ID, "location")

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

    def action(self, ocupation, age, location):
        self.get_occupation().send_keys(ocupation)
        self.get_age()
        self.get_location().send_keys("Israel")
        self.click_button()
