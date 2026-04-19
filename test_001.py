
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_file_upload():

    driver = webdriver.Chrome()

    driver.maximize_window()
    # driver.get("https://the-internet.herokuapp.com/upload")
    # time.sleep(10)

    # upload = driver.find_element(By.ID, "file-upload")

    # upload.send_keys(os.path.abspath(r"C:\Users\Acer SwiftGo 14\Downloads\Test Metrics.xlsx"))

    # time.sleep(5)

    # upload_btn = driver.find_element(By.XPATH, "//input[@id='file-submit']")

    # upload_btn.click()

    # time.sleep(5)

    # driver.get("https://the-internet.herokuapp.com/download")

    # download = driver.find_element(By.XPATH, "//a[text()='panda.png']")

    # download.click()
    # time.sleep(5)


    # driver.get("https://selectorshub.com/iframe-in-shadow-dom/")

    # script = "return document.querySelector('#userName').shadowRoot.querySelector('#kils')"

    # target = driver.execute_script(script)
    # target.send_keys("Amrit")

    # time.sleep(5)

    # script_iframe = "return document.querySelector('#userName').shadowRoot.querySelector('#pact1')"


    # iframe = driver.execute_script(script_iframe)

    # driver.switch_to.frame(iframe)
    # input = driver.find_element(By.CSS_SELECTOR, "#jex")
    # input.send_keys("Hello")
    
    # driver.switch_to.default_content()

    # time.sleep(5)

    # driver.find_element(By.XPATH, "//a[@href='/courses-recordings/']").click()

    # time.sleep(5)


    # driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")

    # original = driver.current_window_handle

    # new_tab = driver.find_element(By.XPATH, "//button[@id='newWindowBtn']")

    # new_tab.click()

    # for handle in driver.window_handles:
    #     if handle != original:
    #         driver.switch_to.window(handle)
    #         break

    
    # # driver.find_element(By.XPATH, "//button[@id='alertBox']").click()

    # # time.sleep(3)

    # # WebDriverWait(driver = driver, timeout=5).until(EC.alert_is_present())

    # # # alert = Alert(driver=driver)
    # # alert = driver.switch_to.alert
    # # alert.accept()

    # time.sleep(3)

    # # driver.close()

    # driver.maximize_window()
    # time.sleep(4)

    # driver.switch_to.window(original)


    # time.sleep(5)

    driver.get("https://vinothqaacademy.com/iframe/")

    iframe = driver.find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe[1])

    btn = driver.find_element(By.XPATH, "//button[text()='Confirm Alert Box']")
    btn.click()

    wait = WebDriverWait(driver=driver, timeout=5)
    
    wait.until(EC.alert_is_present())

    alert = Alert(driver=driver)

    alert.accept()

    time.sleep(5)








