from selenium import webdriver

class WebDriver:

    driver = webdriver.Chrome()
    driver.maximize_window()

    def quit(self):
        self.driver.quit()