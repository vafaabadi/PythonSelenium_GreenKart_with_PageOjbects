from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.LINK_TEXT,"Shop")

    def shopitems(self):
        return self.driver.find_element(*homePage.shop)