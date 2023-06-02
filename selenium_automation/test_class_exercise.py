from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_Store:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/bmi/")

    def test_find_store(self):
        desired_result = "45"
        driver.find_element_by_id("weight").send_keys("200")
        driver.find_element_by_name("height").send_keys("178")
        driver.find_element_by_id("calculate_data").click()
        result = driver.find_element_by_id("bmi_result").get_attribute("value")
        assert result == desired_result

