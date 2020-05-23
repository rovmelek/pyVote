#!/usr/bin/env python3
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('some URL')
    print(driver.page_source)

    nameDiv = driver.find_element_by_css_selector("div[fs-field-validation-name*=Name]")
    first_name = nameDiv.find_element_by_css_selector("input[type=text][aria-label='First Name']")
    last_name = nameDiv.find_element_by_css_selector("input[type=text][aria-label='Last Name']")

    emailDiv = driver.find_element_by_css_selector("div[fs-field-validation-name*=Email]")
    email = emailDiv.find_element_by_css_selector("input[type=email]")

    addressDiv = driver.find_element_by_css_selector("div[fs-field-validation-name*=Address]")
    address = addressDiv.find_element_by_css_selector("input[type=text][aria-label*=Address][name$=address]")
    city = addressDiv.find_element_by_css_selector("input[type=text][aria-label*=City]")
    state = Select(driver.find_element_by_css_selector("select[aria-label*=State]"))
    zip = addressDiv.find_element_by_css_selector("input[type=text][aria-label*=ZIP]")

    phoneDiv = driver.find_element_by_css_selector("div[fs-field-validation-name*=Phone]")
    phone = phoneDiv.find_element_by_css_selector("input[type=tel]")

    first_name.send_keys("John")
    last_name.send_keys("Doe")
    email.send_keys("john.doe@unknown")
    address.send_keys("4141 POSTMARK DR")
    city.send_keys("ANCHORAGE")
    state.select_by_value("AK")
    zip.send_keys("99530")
    phone.send_keys("9512623062")

    # option1RadioBtn = driver.find_element_by_id("field93011629_1")
    # option1RadioBtn.click()
    # driver.find_element_by_css_selector("input[type='radio'][name='field93011629'][value='Option1']").click()
    # driver.find_element_by_css_selector("input[type='radio'][name='field93011957'][value='Option3']").click()
    options = driver.find_elements_by_css_selector('input[type=radio][name*=field][value=No]')
    for option in options:
        option.click()

    # agree = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='field93014946_1']")))
    # if not agree.is_selected():
    #     driver.execute_script("arguments[0].click();", agree)

    # agreeDiv = driver.find_element_by_css_selector("div[fs-field-type=checkbox][fs-field-validation-name=Checkbox]")
    # agree = agreeDiv.find_element_by_css_selector("input[type=checkbox]")
    agree = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@fs-field-validation-name='Checkbox']//input[@type='checkbox']")))
    if not agree.is_selected():
        driver.execute_script("arguments[0].click();", agree)

    # agree = driver.find_element_by_xpath("//input[@type='checkbox']")
    # agree.click()
    # state = Select(driver.find_element_by_id("field93011956"))
    # state = Select(driver.find_element_by_xpath("//select/parent[fs-field-validation-name='State']"))
    # stateDiv = driver.find_element_by_css_selector("div[fs-field-validation-name*=State]")
    # state = Select(stateDiv.find_element_by_tag_name('select'))
    # state.select_by_value("Oregon")

    # submitBtn = driver.find_element_by_css_selector('input[id*=fsSubmitButton]')
    submitBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@id,'fsSubmit')]//input[@class='fsSubmitButton' and @type='submit']")))
    submitBtn.submit()
    # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Submit')]"))).click()

    # driver.quit()
