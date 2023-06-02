import json

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://api.openweathermap.org/data/2.5/weather"
my_units = "metric"
my_api_key = "ad48510a9aed1ff96b51557d94bc5964"
city_name = "Jerusalem"


class Test_Open_Weather:
    def test_lolo(self):
        print("kuku")

    def test_01(self):
        params = dict(q=city_name, units=my_units, appid=my_api_key)
        response = requests.get(url, params)
        print(response)
        print(json.dumps(response.json(), indent=2))

    def test_02(self):
        params = dict(q=city_name, units=my_units, appid=my_api_key)
        response = requests.get(url, params)
        result = response.json()
        print(json.dumps(result, indent=2))
        print(response.status_code)
        print("Content-Type: ", response.headers['Content-Type'])
        print("Date: ", response.headers['Date'])
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert response.status_code == 200

    def test_03(self):
        params = dict(q=city_name, units=my_units, appid=my_api_key)
        response = requests.get(url, params)
        print(json.dumps(response.json(), indent=2))
        res = response.json()
        assert res['sys']['country'] == 'IL'
        humidity = res['main']['humidity']
        print(humidity)

    def test_04(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://openweathermap.org')
        driver.find_element_by_css_selector("input[placeholder='Weather in your city']").send_keys("Jerusalem,IL")

