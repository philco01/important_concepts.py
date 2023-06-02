import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_DDT:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")

    def teardown_class(self):
        time.sleep(2)
        driver.quit()

    @pytest.mark.parametrize(
        "search_value, expected_heading",
        [
            ("Israel", "Israel"),
            ("Automation", "Automation"),
            ("BlahBlah", "Search results")
        ]
    )
    def test_wikipedia_ddt(self, search_value, expected_heading):
        driver.find_element_by_id("searchInput").send_keys(search_value)
        driver.find_element_by_css_selector("button[type='submit']").click()
        assert driver.find_element_by_id("firstHeading").text == expected_heading
        driver.get("http://wikipedia.org/")
