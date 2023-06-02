from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test_Controllers:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_controllers.html")

    def test_control(self):
        driver.find_element_by_name("firstname").send_keys("Philip")
        driver.find_element_by_name("lastname").send_keys("Itkin")
        my_continent = Select(driver.find_element_by_id("continents"))
        my_continent.select_by_visible_text("Asia")
        driver.find_element_by_id("submit").click()
        url = driver.current_url
        if url.__contains__("Philip") & url.__contains__("Itkin"):
            print("Test passed")
        else:
            print("Test failed")

    def test_control_bonus(self):
        driver.find_element_by_id("sex-0").click()
        driver.find_element_by_id("exp-3").click()
        driver.find_element_by_id("datepicker").click()
        date_widget = driver.find_element_by_id("ui-datepicker-div")
        cells = date_widget.find_elements_by_tag_name("td")
        for cell in cells:
            if cell == 18:
                cell.click()
                break
        driver.find_element_by_id("profession-0").click()
        driver.find_element_by_id("profession-1").click()
        driver.find_element_by_id("tool-1").click()
        selenium_commands = Select(driver.find_element_by_id("selenium-commands"))
        commands = selenium_commands.options
        for command in commands:
            print(command.text)
        driver.find_element_by_id("submit").click()
