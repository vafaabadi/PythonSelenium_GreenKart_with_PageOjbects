import time
from pageObjects.checkoutPage import checkoutPage
from pageObjects.confirmationPage import confirmationPage
from pageObjects.homePage import homePage
from utilities.baseClass import baseClass


class TestOne(baseClass):

    def test_e2e(self):
        homepage = homePage(self.driver)
        homepage.shopitems().click()
        time.sleep(2)
        checkoutpage = checkoutPage(self.driver)
        products = checkoutpage.getcardtitles()  # parent
        for product in products:  # //div[@class='card h-100']/div/h4/a
            productName = product.find_element_by_xpath("div/h4/a").text  # child
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        checkoutpage.getthreeLines().click()
        checkoutpage.getCOButton().click()
        selected_product = checkoutpage.getcorrectproduct()
        assert selected_product.text == "Blackberry"
        checkoutpage.getcontinueShopping().click()

        products = checkoutpage.getcardtitles()  # parent
        for product in products:  # div[class='card h-100']
            productName = product.find_element_by_xpath("div/h4/a").text  # child
            if productName == "Nokia Edge" or productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        time.sleep(2)
        checkoutpage.getCOButton().click()

        time.sleep(2)
        checkoutpage.getremovefirstitem().click()
        checkoutpage.getQuantity().send_keys("2")
        total = checkoutpage.getTotal().text
        assert "600000" in total
        checkoutpage.getcontinueButton().click()
        confirmationpage = confirmationPage(self.driver)
        confirmationpage.getautosuggestiveMenu().send_keys("ir")
        time.sleep(5)
        confirmationpage.getsuggestedCountry().click()
        time.sleep(2)
        confirmationpage.getcheckBox().click()
        time.sleep(2)
        confirmationpage.getapplyButton().click()
        success = confirmationpage.getsubmissionText().text
        assert "Success!" in success
