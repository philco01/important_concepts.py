import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('./configuration.xml').getroot()
    return root.find(".//" + node_name).text


class Test_Lesson10:
    def setup_class(self):
        global driver
        driver = get(get_data("Chrome"))
        driver.maximize_window()
        driver.get(get_data("Url"))

    def test_external(self):
        driver.find_element_by_id("weight").send_keys(get_data("Weight"))
        driver.find_element_by_name("height").send_keys(get_data("Height"))
        driver.find_element_by_id("calculate_data").click()
        expected_result = get_data("ExpectedBMI")
        actual_result = driver.find_element_by_id("bmi_result").get_attribute("value")
        assert expected_result == actual_result



class Test_Exceptions:

    def setup_class(self):
        global driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def test_exceptions(self):
        driver.find_element_by_id("btn").click()
        time.sleep(5)
             try:
                driver.find_element_by_id("checkbox").is_displayed()
             except Exception:
                print("hjkhjhjk")




