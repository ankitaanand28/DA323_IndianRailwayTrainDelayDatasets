from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from time import sleep
import pandas as pd
import math
from random import randint

from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')
s = Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=s,  options=options)
driver.maximize_window()

def webpagecompleteloaded(driver):
    return driver.execute_script("return document.readyState") == "complete"


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True
csv_name_list=["15960.csv","12346.csv","05639.csv","13182.csv","02502.csv","02518.csv","12509.csv","12515.csv","12507.csv","22501.csv","12503.csv","22512.csv"]
link_list=["https://etrain.info/train/Kamrup-Express-15960/history?d=1y","https://etrain.info/train/Saraighat-Exp-12346/history?d=1y",
           "https://etrain.info/train/Scl-Koaa-Special-05639/history?d=1y","https://etrain.info/train/Kaziranga-Exp-13182/history?d=1y",
           "https://etrain.info/train/Agtl-Koaa-Spl-02502/history?d=1y","https://etrain.info/train/Ghy-Koaa-Special-02518/history?d=1y",
           "https://etrain.info/train/Guwahati-Exp-12509/history?d=1y","https://etrain.info/train/Cbe-Scl-Exp-12515/history?d=1y",
           "https://etrain.info/train/Aronai-Express-12507/history?d=1y","https://etrain.info/train/New-Tinsukia-Exp-22501/history?d=1y",
           "https://etrain.info/train/Agtl-Humsafar-12503/history?d=1y","https://etrain.info/train/Karmabhoomi-Exp-22512/history?d=1y"]


for i in range(len(csv_name_list)):
    driver.get(link_list[i]) 

    # Wait until the page is completely loaded
    while not webpagecompleteloaded(driver):
        time.sleep(4)
        print("Waiting for page to load")

    # Wait for the element to be present on the page
    element_np = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/a[2]/div[1]'))
    )

    # Initialize empty lists to store data
    Station = []
    Station_Name = []
    Average_Delay = []
    Right_Time = []
    Slight_Delay=[]
    Significant_Delay = []
    Cancelled = []





    # Function to check if an element is visible
    def is_element_visible(element):
        return element.is_displayed()

    # Function to scroll to the bottom of the page
    def scroll_to_bottom():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find the first element to expand
    element_index = 1

    


    # Loop until there are no more elements to expand
    while True:
        try:
            # Expand the current element
            element_xpath = f'/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/a[{element_index}]/div[1]'
            element_to_expand = driver.find_element(By.XPATH, element_xpath)
            # Create an instance of ActionChains
            actions = ActionChains(driver)
            time.sleep(1)
            # actions on the expanded element 
            text=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/a["+str(element_index)+"]/div[1]")
            print("------------------")
            lis=text.text.split("(")

            Station.append(lis[-1].split(")")[0])
            Station_Name.append(lis[0])

            print("station - " + str(lis[-1].split(")")[0]))
            print("station name - " +str(lis[0]))

            # Expanding the element
            time.sleep(1)
            element_to_expand.click()
            time.sleep(2)

            # Extracting useful data

            delay=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]")

            avg_delay=delay.text.split()[3].split(":")[-1]

            Average_Delay.append(avg_delay)

            print("avg delay - "+str(avg_delay))

            percent1=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[1]/td[2]")
            percent2=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[2]/td[2]")
            percent3=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[3]/td[2]")
            percent4=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/table/tbody/tr[4]/td[2]")

            Right_Time.append(percent1.text.split("%")[0])
            Slight_Delay.append(percent2.text.split("%")[0])
            Significant_Delay.append(percent3.text.split("%")[0])
            Cancelled.append(percent4.text.split("%")[0])

            print("percent 1 - "+str(percent1.text.split("%")[0]))
            print("percent 2 - "+str(percent2.text.split("%")[0]))
            print("percent 3 - "+str(percent3.text.split("%")[0]))
            print("percent 4  - "+str(percent4.text.split("%")[0]))

            print("----------------------------------------done---------------------------------------------------------")

            # Scroll down to load more elements if necessary
            scroll_to_bottom()
            
            # Increment the index to find the next element
            element_index += 1
            element_xpath = f'/html/body/div[3]/div/a/i'
            element_to_expand = driver.find_element(By.XPATH, element_xpath)

            # Collapse the expanded element
            actions.move_to_element(element_to_expand).click().perform()
        except NoSuchElementException:
            # If NoSuchElementException occurs, it means there are no more elements to expand
            break
        
    # loading the extracted data into csv through pandas dataframe. 
    train_df = pd.DataFrame(list(zip(Station,Station_Name,Average_Delay,Right_Time,Slight_Delay,Significant_Delay,Cancelled)),columns=["Station","Station_Name","Average_Delay(min)","Right Time (0-15 min's)","Slight Delay (15-60 min's)","Significant Delay (>1 Hour)","Cancelled/Unknown"])
    train_df.to_csv(csv_name_list[i], index=False)
