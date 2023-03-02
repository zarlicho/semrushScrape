from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from statistics import mean 
import xlsxwriter
import time 
import pandas as pd
import pickle

outWorkbook = xlsxwriter.Workbook("adata.xlsx")
outSheet = outWorkbook.add_worksheet()
innerSheet = outWorkbook.add_worksheet()
newSheet = outWorkbook.add_worksheet()
outSheet.write("A1","Title")
outSheet.write("B1","content")
outSheet.write("C1","Image")
innerSheet.write("A1","Title")
innerSheet.write("B1","content")
newSheet.write("A1","Image")
class Main:
    ur=""
    usn = ""
    cap = ""
    def __init__(self):
        # self.ur = urx
        self.options = Options()
        # self.options.add_argument("--auto-open-devtools-for-tabs")
        self.options.add_experimental_option("debuggerAddress","localhost:8989")
        self.options.add_argument("--start-maximized")  
        # self.options.add_argument("user-data-dir=C:\chromeprofile2")
        # self.options.add_argument('--headless')
        # self.options.add_argument('--disable-gpu')
        # self.driver = uc.Chrome(options=self.options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options) 
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
    def LoadArticle(self):
        nilai = 0
        # ur = input("masukan link: ")
        ur = self.driver.current_url
        self.driver.get(ur)
        time.sleep(5)
        with open("link.txt", "r") as f:
            for i,x in enumerate(f.readlines()):
                if "is editing...To make your changes, please come back later." in self.driver.page_source:
                    time.sleep(30)
                    print("please come back later. wait 30 seccond!")
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]"))).click()
                edit=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]")))
                self.actions.click(on_element=edit).perform()
                edit.clear()
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/span/abbr/span"))).click()
                print(x)
                lnk=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[15]/div[3]/form/div[1]/div/div/input")))
                lnk.send_keys(x)
                lnk.send_keys(Keys.ENTER)
                article = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div")))
                print("running!")
                Head = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/h1")))
                print(Head.text)
                print(enumerate(x))
                outSheet.write(i+1,0,Head.text)
                outSheet.write(i+1,1,article.text)
                innerSheet.write(i+1,0,Head.text)
                innerSheet.write(i+1,1,article.get_attribute('innerHTML'))
                time.sleep(2)
                img=self.driver.find_elements(By.XPATH, "//div[contains(@class,'ql-editor')]//img")
                for imgs in img:
                    nilai+=1
                    print(imgs.get_attribute('src'))
                    newSheet.write(nilai+1 ,2,imgs.get_attribute('src'))
                    print(f)
                print(nilai)
                newSheet.write(nilai+1 ,1,Head.text)
                time.sleep(3)
            outWorkbook.close()


    def GetWeb(self):
        # self.driver.get("https://www.youtube.com/watch?v=H2-5ecFwHHQ&t=316s")
        print(self.driver.current_url)
        if "https://www.semrush.com/swa/checker" in self.driver.current_url:
            self.LoadArticle()

ms = Main()
ms.GetWeb()
