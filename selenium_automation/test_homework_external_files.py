import xml.etree.ElementTree as ET
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# def get_data(node_name):
#     root = ET.parse("./confighomework.xml").getroot()
#     return root.find(".//" + node_name).text


# url = get_data("URL")
# browser_type = get_data("BROWSER_TYPE")
# height = get_data("HEIGHT")
# weight = get_data("WEIGHT")
# expected_result = get_data("EXPECTED_BMI")
def get_data(node_name):
    root = ET.parse("./confighomework.xml").getroot()
    return root.find(".//" + node_name).text

class Test_External_files:


    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(get_data("URL"))

    def teardown_class(self):
        driver.quit()

    def test_external_files(self):
        driver.find_element_by_id("weight").send_keys(get_data("WEIGHT"))
        driver.find_element_by_id("hight").send_keys(get_data("HEIGHT"))
        driver.find_element_by_id("calculate_data").click()
        bmi_result = driver.find_element_by_id("bmi_result").get_attribute("value")
        assert bmi_result == get_data("EXPECTED_BMI")
