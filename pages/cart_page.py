import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def cart_page():
    driver = webdriver.Chrome()
    driver.get('http://automationexercise.com')

    assert "Automation Exercise" in driver.title

    cart_button = driver.find_element(By.XPATH, "//a[text()='Cart']")
    cart_button.click()

    footer = driver.find_element(By.XPATH, "//footer")
    driver.execute_script("arguments[0].scrollIntoView(true);", footer)

    subscription_text = "SUBSCRIPTION"
    assert subscription_text in driver.page_source

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")

    arrow_button = driver.find_element(By.XPATH, "//button[contains(@class, 'arrow')]")
    arrow_button.click()

    success_message_locator = (By.XPATH, "//div[@class='success' and contains(text(), 'You have been successfully subscribed!')]")
    success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(success_message_locator))
    assert success_message.is_displayed()

    driver.quit()




