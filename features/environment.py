from utils.webdriver import WebDriver


def before_all(context):
    context.webdriver = WebDriver()


def after_all(context):
    context.webdriver.quit()