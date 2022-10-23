from ast import keyword
import pickle
from re import T
import time
from tkinter import SE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlsxwriter

outWorkbook = xlsxwriter.Workbook("adata.xlsx")
outSheet = outWorkbook.add_worksheet()
innerSheet = outWorkbook.add_worksheet()
outSheet.write("A1","Title")
outSheet.write("B1","content")
outSheet.write("C1","Image")
innerSheet.write("A1","Title")
innerSheet.write("B1","content")
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\chromeprofile") #Path to your chrome profile
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
# https://www.semrush.com/seo-content-template/
dt = 1
def saveContent(title, contents, num):
    outSheet.write(num,0,title)
    outSheet.write(num,1,contents)

def LoadArticle():
    ur = input("masukan link: ")
    driver.get(ur)
    WebDriverWait(driver, 220).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[3]/section[1]/div[2]/div[2]/div[2]/div[2]/a[2]/button"))).click()
    WebDriverWait(driver, 220).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[5]/div[2]/button[2]"))).click()
    time.sleep(5)
    # /html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]
    # try:
    #     keywords = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]")))
    #     keywords.send_keys(Keys.CONTROL, 'a')
    #     keywords.send_keys(Keys.BACKSPACE)
    # except:
    #     print("error!")
    #     pass
    # time.sleep(3)
    with open("link.txt", "r") as f:
        for i,x in enumerate(f.readlines()):
            print(x)
            warning = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]")))
            if "nygigi@kellychibale-researchgroup-uct.com is editing...To make your changes, please come back later." in warning.text:
                time.sleep(30)
                print("please come back later. wait 30 seccond!")
            time.sleep(5)
            keywords = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]")))
            keywords.send_keys(Keys.CONTROL, 'a')
            keywords.send_keys(Keys.DELETE)
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/span/abbr"))).click()
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[14]/div[3]/form/div[1]/div/div/input"))).send_keys(x)
            # WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[14]/div[3]/form/div[2]/button[1]"))).click()
            try:
                driver.find_element(By.XPATH, "/html/body/div[14]/div[3]/form/div[2]/button[1]").click()
            except:
                pass
            time.sleep(5)
            article = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]")))
            print("running!")
            Head = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/h1")))
            print(Head.text)
            print(enumerate(x))
            outSheet.write(i+1,0,Head.text)
            outSheet.write(i+1,1,article.text)
            innerSheet.write(i+1,0,Head.text)
            innerSheet.write(i+1,1,article.get_attribute('innerHTML'))
            print(i)
            print(article.get_attribute('innerHTML'))
            # print(article.text)
            time.sleep(5)
            img=driver.find_elements(By.XPATH, "//div[contains(@class,'ql-editor')]//img")
            for imgs in img:
                print(imgs.get_attribute('src'))
                outSheet.write(i+1 ,2,imgs.get_attribute('src'))
            time.sleep(30)
        outWorkbook.close()
            # keywords2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]")))
            # keywords2.send_keys(Keys.CONTROL, 'a')
            # keywords2.send_keys(Keys.DELETE)

LoadArticle()