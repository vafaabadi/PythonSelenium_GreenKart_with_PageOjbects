from selenium.webdriver.common.by import By


class checkoutPage():

    def __init__(self, driver):

        self.driver = driver


    productsTitle = (By.XPATH, "//div[@class='card h-100']")
    productFooter = (By.XPATH, "div/button")
    threeLines = (By.CLASS_NAME, "navbar-toggler-icon")
    COButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    correctProduct = (By.XPATH, "//a[contains(text(),'Blackberry')]")
    continueShopping = (By.CSS_SELECTOR, "button[class*='btn-default']")
    removefirstItem = (By.XPATH, "//tr[1]//td[5]//button[1]")
    quantity = (By.ID, "exampleInputEmail1")
    total = (By.XPATH, "//td[@class='text-right']//strong[contains(text(),'. 600000')]")
    continueButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getcardtitles(self):
        return self.driver.find_elements(*checkoutPage.productsTitle)

    def getcardfooter(self):
        return self.driver.find_element(*checkoutPage.productFooter)

    def getthreeLines(self):
        return self.driver.find_element(*checkoutPage.threeLines)

    def getCOButton(self):
        return self.driver.find_element(*checkoutPage.COButton)

    def getcorrectproduct(self):
        return self.driver.find_element(*checkoutPage.correctProduct)

    def getcontinueShopping(self):
        return self.driver.find_element(*checkoutPage.continueShopping)

    def getremovefirstitem(self):
        return self.driver.find_element(*checkoutPage.removefirstItem)

    def getQuantity(self):
        return self.driver.find_element(*checkoutPage.quantity)

    def getTotal(self):
        return self.driver.find_element(*checkoutPage.total)

    def getcontinueButton(self):
        return self.driver.find_element(*checkoutPage.continueButton)