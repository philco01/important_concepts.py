import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")

    def teardown_class(self):
        time.sleep(2)
        driver.quit()

    def test_drag_and_drop(self):
        draggable = driver.find_element_by_id("draggable")
        droppable = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.drag_and_drop(draggable, droppable).perform()
        assert driver.find_element_by_id("droppable").text == "Dropped!"

    def test_multiple_select(self):
        list1 = driver.find_elements_by_css_selector("ol>li[class='ui-widget-content ui-selectee']")
        action = ActionChains(driver)
        action.click_and_hold(list1[1]).click_and_hold(list1[2]).click().perform()

    def test_double_click(self):
        d_click = driver.find_element_by_id("dbl_click")
        action = ActionChains(driver)
        action.double_click(d_click).perform()
        assert driver.find_element_by_id("demo").is_enabled()

    def test_hover_over(self):
        yellow = "background-color: rgb(255, 255, 0);"
        action = ActionChains(driver)
        elem1 = driver.find_element_by_id("mouse_hover")
        action.move_to_element(elem1).perform()
        assert driver.find_element_by_id("mouse_hover").get_attribute("style") == yellow

    def test_scroll_down(self):
        driver.execute_script("scrollTo(0, 600);")
        time.sleep(1)
        expected_result = "This Element is Shown When Scrolled"
        assert driver.find_element_by_id("scrolled_element").text == expected_result


