import pytest
import requests
import data
from selenium import webdriver
from helpers import *


@pytest.fixture(params=[data.browser_chrome, data.browser_firefox])
def driver(request):
    if request.param == data.browser_chrome:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == data.browser_firefox:
        data.DRIVER_NAME = data.browser_firefox
        driver = webdriver.Firefox()

    driver.set_window_size(1440, 1100)
    driver.get(data.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def create_user_and_delete():
    email = generate_random_email(5)
    password = generate_random_string(7)
    name = generate_random_string(7)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(data.REGISTER_URL, json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')
    yield email, password, token
    headers = {'Authorization': token[1]}
    requests.delete(data.USER_DELETE, headers=headers)
