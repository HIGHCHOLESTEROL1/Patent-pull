from lib2to3.pgen2 import driver
from mechanize import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

def getSearchData():
    ## gather user input information
    input_data = input("Enter product name / description: ")
    return input_data

def control():
    ## ask user for product name / idea first
    print("Q to quit")
    input_data = ""
    ## set chrome browser
    browser = webdriver.Chrome()
    browser.get("https://patents.google.com/")
    ## repeatdely ask user for producst and displaying on browser until quit
    while (input_data.lower() != "q"):
        ## search user input data
        input_data = getSearchData()
        elem = browser.find_element(By.NAME, 'q')
        elem.clear()
        elem.send_keys(input_data)
        ## click search button
        search = browser.find_element(By.ID, 'searchButton')
        search.click()
    ## exit once quit is input
    exit()

control()



