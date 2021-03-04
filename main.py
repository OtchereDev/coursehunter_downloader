from copy import Error
from mode import all_video_download, get_video, range_download, single_video_download
import time
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests.exceptions
from colorama import Fore
from colorama import Style

from module.create import create_folder, create_logger
# from module.extractor import extract_video, extract_video_url
# from module.extractor import extract_material_url_and_download , download_mode





print(f'{Fore.GREEN}+++++++++++++++++++++++++++++++++++++++++++++++++++{Style.RESET_ALL}')
print()
print(f'{Fore.BLUE}         COURSEHUNTER DOWNLOADER v2.0{Style.RESET_ALL}')
print()
print(f'{Fore.GREEN}+++++++++++++++++++++++++++++++++++++++++++++++++++{Style.RESET_ALL}\n')

# request for user details
user_email = input('Email : \n\t')
print()
password = input('Password : \n\t')
print()
course_link = input('Course_link : \n\t')
print()


moz_driver_path=os.path.join(os.path.abspath('.'),'geckodriver')
chrome_driver_path=os.path.join(os.path.abspath('.'),'chromedriver')
driver_path_check=os.path.exists(chrome_driver_path) or os.path.exists(moz_driver_path)

if not driver_path_check:
    raise Error('Selenium Driver is needed','Please ensure you have a chromedrive or mozilla firefox gecko driver in the root of the folder....Try again')
# start browser in mute mode for the whole download section
# ----chrome
if os.path.exists(chrome_driver_path) :
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")

    driver=webdriver.Chrome(chrome_driver_path,
                            options=chrome_options)

# ---mozilla
else:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(executable_path=moz_driver_path,
                                firefox_profile=profile)

# creating folder to hold download course video
download_path=os.path.join(os.path.abspath('.'),course_link.split("/")[-1])
create_folder.createFolder(download_path)

# signing in user to coursehunter
driver.get('https://coursehunter.net/sign-in')
user_input=driver.find_element_by_css_selector('input[type="email"]')
user_input.send_keys(user_email)

password_input=driver.find_element_by_css_selector('input[type="password"]')
password_input.send_keys(password)

login_btn=driver.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

# redirecting to the desire course to download
driver.get(course_link)

# start to play course video
play=driver.find_element_by_css_selector('.player-play')
play.click()
time.sleep(6)

# getting hold of all video in the course
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#oframeplayer > pjsdiv:nth-child(15) > pjsdiv:nth-child(1) > pjsdiv')))
button.click()
episodeList=driver.find_elements_by_css_selector('#player_playlist > pjsdiv > pjsdiv')


# minimize browser window
driver.minimize_window()

# initiate download
print(f'\n{Fore.RED}There are {len(episodeList)} lessons in this course !!!{Style.RESET_ALL}\n')
download_type = input('Which type of download '
            + 'would you like to make: \n\t [S]ingle lesson, '
            + '[R]ange of lessons, [A]ll lessons:\n\t')

if download_type.upper() == 'A':
        all_video_download(episodeList,driver,button,download_path)
    

elif download_type.upper() =='R':
    
    user_range = input('Provide range of lesson to download:\n\t '
        + 'Use ":" to seperate the range. eg. 1:20  :\n\t')
    
    start,end=user_range.split(":")
    range_download(episodeList,driver,button,download_path,start,end)

elif download_type.upper() == 'S':
    
    user_esp = input('What a lesson number do you want eg. 10  :\n\t')

    single_video_download(episodeList,driver,button,download_path,user_esp)




            






