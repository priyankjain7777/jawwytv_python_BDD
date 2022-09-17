from behave import*
from selenium import webdriver

@given('open chrome browser')
def OpenBrowser(context):
   # context.driver=webdriver.Chrome(executable_path="C:\Users\hp\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    context.driver=webdriver.Chrome()


@when('open jawwaytv homepage')
def OpenHomepage (context):
    context.driver.get("https://subscribe.stctv.com")


@then('change language to english')
def changelang(context):
    status=context.driver.find_element("xpath","//a[@id='changeLanguageButton']").click


@then('check the lite pack')
def litepack(context):
    status=context.driver.find_element("xpath","//div[@class='packages packages Light']").is_displayed()
    assert status is True


@then('check the lite pack price')
def litepackprice(context):
    status=context.driver.find_element("xpath","//span[contains(text(),'5.4')]").is_displayed()
    assert status is True


@then('check the classic pack')
def classicpack(context):
    status=context.driver.find_element("xpath","//div[@class='packages packages Classic']").is_displayed()
    assert status is True


@then('check the classic pack price')
def classicpackprice(context):
    status=context.driver.find_element("xpath","//span[contains(text(),'10.9')]").is_displayed()
    assert status is True


@then('check the premium pack')
def premiumpack(context):
    status = context.driver.find_element("xpath", "//div[@class='packages packages Premium']").is_displayed()
    assert status is True


@then('check the premium pack price')
def premiumpackprice(context):
    status=context.driver.find_element("xpath","//span[contains(text(),'16.3')]").is_displayed()
    assert status is True


@then('close browser')
def Closebrowser(context):
   context.driver.close()
