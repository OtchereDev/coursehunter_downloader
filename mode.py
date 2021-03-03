from module.extractor.extract_video import extract_video

import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_video(driver,single,button,download_path):
    driver.execute_script("arguments[0].click();", single)
    time.sleep(5)
    video=driver.find_element_by_css_selector('#oframeplayer > pjsdiv:nth-child(3) > video')
    src=video.get_attribute("src")
    videoCont=driver.find_element_by_css_selector('#player')
    driver.execute_script("arguments[0].click();", videoCont)
    title=(single.get_attribute("textContent")).split('|')[0]
    driver.execute_script("document.getElementsByTagName('video')[0].pause()")
    hover=ActionChains(driver).move_to_element(videoCont).move_to_element(button)
    hover.perform()
    button.click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#oframeplayer > pjsdiv:nth-child(26)')))
    extract_video(src,title,download_path)

def all_video_download(episodeList,driver,button,download_path):
    for single in episodeList:
        get_video(driver,single,button,download_path)

def range_download(episodeList,driver,button,download_path,start,end):
    start=int(start)-1
    end=int(end)
    for single in episodeList[start:end]:
        get_video(driver,single,button,download_path)

def single_video_download(episodeList,driver,button,download_path,esp_num: int):
    esp_num=int(esp_num)-1
    single=episodeList[esp_num]
    get_video(driver,single,button,download_path)