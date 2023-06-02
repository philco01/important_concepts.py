from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Support:
    def __init__(self, _driver):
        self.driver = _driver

    def verify_elements(self):
        driver.find_element_by_id()




class Test_Loudev:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://loudev.com")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test_01(self):
        support = Support()
        support.verify_elements(driver)