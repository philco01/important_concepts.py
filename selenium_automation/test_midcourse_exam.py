import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test_Pizza:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/pizza/")
        driver.maximize_window()

    def teardown_class(self):
        time.sleep(3)
        driver.quit()

    def test_pizza(self):
        minimal_cost = driver.find_element_by_xpath("//span[@class='ginput_total ginput_total_5']").text
        assert minimal_cost == "$7.50"
        driver.find_element_by_css_selector("input[name='input_22.3']").send_keys("Philip")
        driver.find_element_by_css_selector("input[name='input_22.6']").send_keys("Itkin")
        delivery = Select(driver.find_element_by_name("input_21"))
        delivery.select_by_index(1)
        minimal_cost = driver.find_element_by_xpath("//span[@class='ginput_total ginput_total_5']").text
        assert minimal_cost == "$10.50"
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(iframe)
        coupon_number = driver.find_element_by_id("coupon_Number").text
        driver.switch_to.parent_frame()
        driver.find_element_by_name("input_20").send_keys(coupon_number)
        driver.find_element_by_id("gform_submit_button_5").click()
        popup = driver.switch_to.alert
        alert_text = popup.text
        popup.accept()
        assert alert_text == "Philip"+" " + "Itkin"+" " + coupon_number
