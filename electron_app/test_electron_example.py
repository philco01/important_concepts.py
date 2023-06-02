import time

from selenium import webdriver

electron_app = r'C:\electron\ElectronApiDemos\ElectronApiDemos.exe'
edriver = r'C:\electron\ElectronDriver\electrondriver.exe'

class Test_Example3:

    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.binary_location = electron_app

        global driver
        driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
        driver.implicitly_wait(5)

    def test_01_electron(self):
        driver.find_element_by_id("button-windows").click()
        driver.find_element_by_id("button-crash-hang").click()
        driver.find_element_by_id("button-menus").click()
        time.sleep(1)

    def teardown_class(self):
        driver.quit()