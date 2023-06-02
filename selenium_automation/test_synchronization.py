import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Test_Synchronization:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def teardown_class(self):
        driver.quit()

    def test_synch(self):
        random_text = "My Rendered Element After Fact!"
        driver.find_element_by_id("rendered").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish2")))
        text = driver.find_element_by_id("finish2").text
        assert random_text == text

    def test_sleep(self):
        driver.find_element_by_id("hidden").click()
        time.sleep(1)
        loading = driver.find_element_by_id("loading1")
        assert loading.is_displayed()

    def test_remove(self):
        driver.find_element_by_id("btn").click()
        driver.implicitly_wait(10)
        remove_text = driver.find_element_by_id("message").text
        assert remove_text == "It's gone!"





