from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv
import json


driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')


driver.get("http://43.245.130.98:8082/ekioskv2/(S(cbttez3uegg3vqrx5ssgk51d))/SearchResult.aspx?p=p5&1=V&t=1&from=XCYtcfND0sE=")


def loadJquery():
    driver.execute_script("""var jq = document.createElement('script');
    jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
    document.getElementsByTagName('head')[0].appendChild(jq);""")
    time.sleep(1)


page_counter = 0
cases_list = []

def fetch_data():

    global page_counter
    global cases_list

    print("fetching data outside")

    try:

        print("fetching data")

        cases_info = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.ID, "GRSearchResult")))

        current_cases_list = driver.find_elements_by_css_selector('tbody tr')

        if f'page {page_counter}' not in current_cases_list[-1].text.lower():
            page_counter += 1
            
            for case in current_cases_list:
                print(case.text)
            
            driver.find_element_by_id("GRSearchResult_btn_next").click()
            fetch_data()

        time.sleep(10)
        fetch_data()

        

       

    except Exception as e:
        print("except running", str(e))

    finally:
        driver.quit()


fetch_data()
