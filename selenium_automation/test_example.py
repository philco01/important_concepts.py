from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_Example:

    def setup_class(self):
        global webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il")


    def test_01(self):
        my_title = webdriver

    def test_02(self):
        my_url = webdriver.current_url
        print(my_url)
