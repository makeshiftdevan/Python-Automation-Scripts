from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#location of chromedriver and geckodriver.  Replace ... with directory
geckodriver = 'C:\\Users\\....\\geckodriver.exe'
options = webdriver.FirefoxOptions()
#options.add_argument('-headless')

#tells selenium where to find the driver to open Firefox
driver = webdriver.Firefox(executable_path=geckodriver, options =options)


def log_in():
    #goes to *****.com log in screen 
    driver.get('https://insert login address here')
    time.sleep(3)
    #Replace ***** with username
    driver.find_element_by_css_selector('#emailAddress').send_keys('*****')
    #Replace ****** with password for website
    driver.find_element_by_css_selector('#pwd').send_keys('******')
    driver.find_element_by_css_selector('#loginForm > button').click()
    time.sleep(5)
log_in()

#ap Physics 1 scripts
def course():
    i = 0
    #Search for specific course
    selected_course = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/input')
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/input').click()
    #Search for specific course
    ActionChains(driver).move_to_element(selected_course).send_keys('AP Physics 1: Homeschool Curriculum').send_keys(Keys.ENTER).perform()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div[1]/div/h4/a').click()
    #Go to Lesson 1
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[3]/div[1]/div[5]/div/div[3]/div[3]/table/tbody/tr[1]/td[2]/a').click()
    while i <= 110:
        WebDriverWait(driver, 200)
        
        def print_transcripts():
            #Firefox hamburger
            pyautogui.moveTo(1265, 55)
            pyautogui.click()
            #Print
            pyautogui.moveTo(1078,505)
            time.sleep(2)
            pyautogui.click()
            time.sleep(5)
            pyautogui.hotkey('alt', 'p')
            pyautogui.moveTo(688, 480)
            pyautogui.click()
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.moveTo(605, 758)
            pyautogui.click()
            pyautogui.hotkey(print(str(i)))
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('alt', 'c')
            time.sleep(5)
        print_transcripts()
        
        def print_quiz():
            driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/div[1]/ul/li[2]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/a').click
            time.sleep(2)
            WebDriverWait(driver, 100)
            pyautogui.hotkey('ctrl', 'p')
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.hotkey('q', 'u', 'i', 'z')
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.hotkey('alt', 'c')
        print_quiz()
        ++i
        #next lesson
        driver.find_element_by_css_selector('#nextLessonBreadcrumb > span:nth-child(2)').click()
        time.sleep(5)
course()

print("AP Physics 1 download complete")
