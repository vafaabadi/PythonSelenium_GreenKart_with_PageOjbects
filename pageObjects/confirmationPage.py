from selenium.webdriver.common.by import By


class confirmationPage():

    def __init__(self, driver):

        self.driver = driver


    autosuggestiveMenu = (By.ID, "country")
    suggestedCountry = (By.XPATH,"//a[contains(text(),'Iran')]")
    checkBox = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    applyButton = (By.CSS_SELECTOR, "input[type='submit']")
    submissionText = (By.XPATH, "//strong[contains(text(),'Success!')]")


    def getautosuggestiveMenu(self):
        return self.driver.find_element(*confirmationPage.autosuggestiveMenu)

    def getsuggestedCountry(self):
        return self.driver.find_element(*confirmationPage.suggestedCountry)

    def getcheckBox(self):
        return self.driver.find_element(*confirmationPage.checkBox)

    def getapplyButton(self):
        return self.driver.find_element(*confirmationPage.applyButton)

    def getsubmissionText(self):
        return self.driver.find_element(*confirmationPage.submissionText)