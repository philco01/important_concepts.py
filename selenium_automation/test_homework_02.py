from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as EC, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_advanced:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")

    # def teardown_class(self):
    #     # driver.quit()

    def test_locators(self):
        print("locator 1", driver.find_element_by_id("locator_id"))
        print("locator 2", driver.find_element_by_name("locator_name"))
        print("locator 3", driver.find_element_by_tag_name("p"))
        print("locator 4", driver.find_element_by_class_name("locator_class"))
        print("locator 5", driver.find_elements_by_link_text("myLocator"))
        print("locator 6", driver.find_element_by_partial_link_text("Find my locator"))
        print("locator 7", driver.find_element_by_xpath("//input[@class='btn btn-2']"))
        print("locator 8", driver.find_element_by_css_selector("button[class='btn btn-2"))

    def test_print_text(self):
        locator_1 = driver.find_element_by_id("locator_id")
        locator_2 = driver.find_element_by_name("locator_name")
        locator_3 = driver.find_element_by_tag_name("p")
        locator_4 = driver.find_element_by_class_name("locator_class")
        locator_5 = driver.find_elements_by_link_text("myLocator")
        locator_6 = driver.find_element_by_partial_link_text("Find my locator")
        locator_7 = driver.find_element_by_xpath("//input[@class='btn btn-2']")
        locator_8 = driver.find_element_by_css_selector("button[class='btn btn-2")
        print(locator_1.text)
        print(locator_2.text)
        print(locator_3.text)
        print(locator_4.text)
       # print(locator_5.text)
        print(locator_6.text)
        print(locator_7.text)
        print(locator_8.text)

class Test_sync:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def teardown_class(self):
        driver.quit()

    def test_sync(self):
        driver.find_element_by_id("btn").click()
        WebDriverWait(driver, 10).until

