import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_Asserts:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/bmi/")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test_exercise1(self):
        expected_result = "43"
        driver.find_element_by_id("weight").send_keys("123")
        driver.find_element_by_id("hight").send_keys("167")
        driver.find_element_by_id("calculate_data").click()
        actual_result = driver.find_element_by_id("bmi_result").get_attribute("value")
        assert expected_result == actual_result, "results are not equal"

    def test_calculate_BMI(self):
        button_size = driver.find_element_by_id("calculate_data").size
        button_pos = driver.find_element_by_id("calculate_data").location
        button_enabled = driver.find_element_by_id("calculate_data").is_enabled()
        button_displayed = driver.find_element_by_id("calculate_data").is_displayed()
        button_not_selected = driver.find_element_by_id("calculate_data").is_selected()
        button_tag = driver.find_element_by_id("calculate_data").tag_name
        button_text = driver.find_element_by_id("calculate_data").get_attribute("value")
        expected_result = "43"
        # driver.find_element_by_id("weight").send_keys("123")
        driver.find_element_by_id("hight").send_keys("167")

        print("size of button is", button_size)
        print("location of button is", button_pos)
        print("enabled=", button_enabled)
        print("displayed", button_displayed)
        print("not selected", button_not_selected)
        print("tag name of the button", button_tag)
        print("button text is", button_text)
        driver.find_element_by_id("calculate_data").click()
        if driver.find_element_by_id("validation").is_displayed():
            if driver.find_element_by_id("weight").get_attribute("value") is None or driver.find_element_by_id(
            "hight").get_attribute("value") is None:
                driver.find_element_by_id("validation").is_enabled()
        else:
            print("everything fine mr philip")
