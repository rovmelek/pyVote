from selenium import webdriver
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
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.nba.com/blazers/assist')

    first_name = driver.find_element_by_id("FirstName")
    last_name = driver.find_element_by_id("LastName")
    email = driver.find_element_by_id("Email")
    postal_code = driver.find_element_by_id("PostalCode")

    first_name.send_keys("First02")
    last_name.send_keys("Last02")
    email.send_keys("first02.last02@myemail.com")
    postal_code.send_keys("97814")

    select = Select(driver.find_element_by_id("college"))
    select.select_by_value("Baker City")

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Submit')]"))).click()

    print(driver.page_source)

    # driver.quit()
