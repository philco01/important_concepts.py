import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class Test_Demo:

    def setup_class(self):
        print("do first")

    def teardown_class(self):
        print("do after all")

    def setup_method(self):
        print("check method")

    def teardown_method(self):
        print("check end")

    def test_01(self):
        print("test-01")

    def test_02(self):
        print("test-02")
# WebDriver Object methods - homework
# exercise 1
class Test_Homework:

    # @pytest.fixture(autouse=True)
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://imdb.com")

    def teardown_class(self):
        driver.quit()

    def test_01(self):
        print("test done")
        driver.refresh()
        web_title = driver.title
        web_url = driver.current_url
        expected_result = "Page"
        expected_url = "https://imdb.com"
        if web_title == expected_result:
            print("equal result")
        else:
            print("there is no match overthrew")
        if web_url == expected_url:
            print("equal result")
        else:
            print("no match")


# exercise 2
class Test_Goofle_Bing_Switcher:

    @pytest.fixture(autouse=True)
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://google.com")

    def test_go_to_bing(self):
        driver.get("https://bing.com")
        driver.back()
        print(driver.title)
        page_source = driver.page_source
        if page_source.find("bubble") is not None:
            print("Exists")
        else:
            print("not exists")
        # or another simplier case is
        # if "bubble in source:
        #   print(...)
        #else:
        #   print(...)

class Test_Open_Browsers:

    def test_open_browsers(self):
        global driver

        # Open Chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(2)
        driver.quit()

        # Open Edge
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        time.sleep(2)
        driver.quit()

        # Open Firefox
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        time.sleep(2)
        driver.quit()
        #
        # # Open Opera
        # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        # time.sleep(2)
        # driver.quit()


# Homework Locators - Basic
# Exercise 1
class Test_Locators:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://selenium.dev")

    def teardown_class(self):
        driver.quit()

    def test_select_logo(self):
        print(driver.find_element_by_class_name("navbar-brand"))
        print(driver.find_element_by_class_name("navbar-logo"))
        print(driver.find_element_by_id("Layer_1"))
        print(driver.find_elements_by_tag_name("svg"))
        links = driver.find_elements_by_tag_name("a")
        Selenium_links = driver.find_elements_by_partial_link_text("Selenium")
        selenium_links = driver.find_elements_by_partial_link_text("selenium")
        print("Number of total links in page: " + str(len(links)))
        print("Number of links in page with word: Selenium is: " + str(len(Selenium_links)))
        print("Number of links in page with word: selenium is: " + str(len(selenium_links)))



class Test_Wikipedia:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://wikipedia.org/")
        driver.maximize_window()

    def test_wikipedia(self):
        main_logo = driver.find_element_by_class_name("central-featured-logo")
        search_field = driver.find_element_by_id("searchInput")
        select_language = driver.find_element_by_id("searchLanguage")
        footer_sidebar = driver.find_element_by_class_name("footer-sidebar-content")
        web_elements=[main_logo, search_field, select_language, footer_sidebar]
        




