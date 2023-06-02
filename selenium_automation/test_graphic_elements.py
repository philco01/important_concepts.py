from applitools.selenium import Eyes
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

eyes = Eyes()


class Test_Automatic_Graphic_Elements:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://applitools.com/helloworld/")
        eyes.api_key = "1HluwvaV555Z109qh977WEu5THSLQzbc4PZdV46suaD8pk110"

    def teardown_class(self):
        driver.quit()
        eyes.abort()

    def test_click_elements(self):
        eyes.open(driver, "Test for buttons", "we check for mooving text with button")
        eyes.check_window("before everyhing")
        driver.find_element_by_partial_link_text("?diff1").click()
        eyes.check_window("diff1 is clicked")
        driver.find_element_by_partial_link_text("?diff2").click()
        eyes.check_window("diff2 is clicked")
        driver.find_elements_by_xpath("//Button")
        eyes.check_window("button is clicked")


