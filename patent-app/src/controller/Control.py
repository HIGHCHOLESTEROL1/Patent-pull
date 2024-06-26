from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json
import sys

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
        if input_data.lower() == "q":
            exit()

        elem = browser.find_element(By.NAME, 'q')
        try:
            elem.clear()
            elem.send_keys(input_data)
        except:
            elem = browser.find_element(By.NAME, 'q')
            elem.clear()
            elem.send_keys(input_data)

        search = browser.find_element(By.ID, 'searchButton')
        try:
            ## click search button
            search.click()
        except:
            search = browser.find_element(By.ID, 'searchButton')
            search.click()

        links = browser.find_elements(By.ID, 'link')
        try:
            for link in links:
                if link.get_attribute('href')!= None:
                    print(link.get_attribute('href'))
        except:
            links = browser.find_elements(By.ID, 'link')
            for link in links:
                if link.get_attribute('href')!= None:
                    print(link.get_attribute('href'))
                    
    ## exit once quit is input
    exit()
control()

