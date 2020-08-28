import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    #yield
    #driver.close()
