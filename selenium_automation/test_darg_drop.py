from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Test_Asserts:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")

    # def teardown_class(self):
    #     driver.quit()

    def test_drag_drop(self):
        draggable = driver.find_element_by_id("draggable")
        droppable = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.drag_and_drop(draggable, droppable).perform()
        assert driver.find_element_by_id("droppable").text == "Dropped!"

    def test_click_2(self):
        items = driver.find_elements_by_xpath("//ol/li")
        action = ActionChains(driver)
        action.click_and_hold(items[2]).click_and_hold(items[3]).perform()

    def test_double_click(self):
        double_click = driver.find_elements_by_id("dbl_click")
        action = ActionChains(driver)
        action.double_click(double_click).perform()
        some_text = driver.find_element_by_id("demo").text
        assert some_text == "Hello World"
