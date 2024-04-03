import requests
from bs4 import BeautifulSoup
import pyttsx3
import pyautogui
import time

def say(text) :
    # engine = ''
    engine.say(text)
    print(text)
    engine.runAndWait()


# Make a Get request to the web page you want to scrape
url = "https://etty-k-first.herokuapp.com/"
response = requests.get(url)

# Parse the Html content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements you want to scrape and extract their content
title = soup.find("title").text
paragraphs = [p.text for p in soup.find_all("p")]

# Print the scraped data
# print("Title:", title)
# print("paragraphs:",paragraphs)

time.sleep(2)
# pyautogui.typewrite(title)
# pyautogui.typewrite(paragraphs)
# pyautogui.press("enter")

# pyautogui.moveTo(100,100)
# pyautogui.click()

engine = pyttsx3.init()
say(title)
say(paragraphs)