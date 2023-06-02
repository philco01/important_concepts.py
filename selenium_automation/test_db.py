import mysql
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_DB:
    def setup_class(self):
        global driver
        global mydb
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")

        mydb = mysql.connector.connect(
            host=" sql8.freemysqlhosting.net",
            database = 'random_shit',
            user="sql8619418",
            password="usLdALJItR"
        )

        def test_01
