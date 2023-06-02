import time

from appium import webdriver
from selenium.webdriver.common.by import By

username = "company"
password = "company"


class Test_EriBank:

    def setup_class(self):
        dc = {}
        global driver
        dc['udid'] = 'eicicqssdahmca85'
        dc['appPackage'] = 'com.experitest.ExperiBank'
        dc['appActivity'] = '.LoginActivity'
        dc['platformName'] = 'android'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    def test_eri_login(self):
        driver.find_element(By.XPATH, "//*[@id='usernameTextField']").send_keys(username)
        driver.find_element(By.XPATH, "//*[@id='passwordTextField']").send_keys(password)
        driver.find_element_by_xpath("//*[@text='Login']").click()
        driver.find_element(By.XPATH, "//*[@text='Logout']").click()

    def teardown_class(self):
        driver.quit()
