from lib2to3.pgen2 import driver
from mechanize import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

def getSearchData():
    input_data = input("Enter product name / description: ").replace(" ", "+")
    return input_data

def control():
    print("Q to quit")
    input_data = ""
    while (input_data.lower() != "q"):
        input_data = getSearchData()
        browser = webdriver.Chrome()
        browser.get("https://patents.google.com/")
        elem = browser.find_element(By.NAME, 'q')
        elem.send_keys(input_data, Keys.ARROW_DOWN)


        print("Here is a selection of products to your description: \n")
    exit()

control()

