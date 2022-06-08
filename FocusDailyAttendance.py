from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#location of chromedriver (replace '...' with file location
chromedriver = 'C:/Users/...chromedriver.exe'

#tells selenium where to find the driver to open Chrome
driver = webdriver.Chrome(chromedriver)

def log_in():
    #goes to Focus website
    driver.get('https://focus.oneclay.net/focus/')
    #login with username (replace ****** with real username)
    driver.find_element_by_xpath('//*[@id="username-input"]').send_keys('******')
    #Replace ****** with password
    driver.find_element_by_xpath('//*[@id="main-login-form"]/input[2]').send_keys('******')
    driver.find_element_by_xpath('//*[@id="main-login-form"]/div[1]/div[2]/button').click()
    time.sleep(3)
    if driver.find_element_by_xpath('//*[@id="computer-name-form"]/input'):
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="computer-name-form"]/input').send_keys('Attendance Bot')
        driver.find_element_by_xpath('//*[@id="computer-name-form"]/div/button').click()
        time.sleep(3)
    else:
        time.sleep(3)

    #Clicks attendance
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div[4]/button').click()

    #Clicks take attendance
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div[4]/div/div/div/div/a[1]').click()
    time.sleep(3)

    #clicks 'save'
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button').click()

    #change course dropdown
    driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #change classes, save, then select next class
    #class 1
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[1]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[1]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()
        time.sleep(3)


    #class 2
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[2]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[2]').click()
        time.sleep(3)
        if driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button'):
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button').click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 3
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[3]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[3]').click()
        time.sleep(3)
        #looks for 'save' button using find_elements_by_xpath. Notice the 's' in elements.
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 4
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[4]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[4]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 5
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[5]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[5]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 6
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[6]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[6]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 7
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[7]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[7]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 8
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[8]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[8]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 9
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[9]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[9]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 10
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[10]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[10]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 11
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[11]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[11]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 12
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[12]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[12]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 13
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[13]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[13]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 14
    if driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[14]'):
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[1]/option[14]').click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 15
    other_class1 = driver.find_elements_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[2]/option')
    if len(other_class1) > 0:
        other_class1[0].click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 16
    other_class2 = driver.find_elements_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[2]/option[1]')
    if len(other_class2) > 0:
        other_class2[0].click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
    else:
        driver.find_element_by_xpath('//*[@id="Top_Right"]/li[4]/select').click()

    #class 17
    other_class3 = driver.find_elements_by_xpath('//*[@id="Top_Right"]/li[4]/select/optgroup[2]/option[2]')
    if len(other_class3) > 0:
        other_class3[0].click()
        time.sleep(3)
        save = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/main/form/table/tbody/tr/td/font/b/div/button')
        if len(save) > 0:
            save[0].click()
            time.sleep(3)
        else:
            driver.find_element_by_id('red_button_form').click()
            time.sleep(3)
        time.sleep(3)
    else:
        driver.quit()
        
log_in()

#closes browser and ends sesson.
driver.quit()

#Sends email confirmation attendence was taken
fromaddr = "**inpute email address sending report from here **"
toaddr = "**place email address reciptient here**"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject
time_now = datetime.datetime.now().isoformat()
msg['Subject'] = "Daily Attendance" + time_now[0:10]
  
# string to store the body of the mail 
body = r"Today's attendance has been taken."
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# encode into base64 
#encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment;None") 
  
# creates SMTP session  (example uses gmail)
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication.  Replace ****** with FROM email address password
s.login(fromaddr, "******") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit()

#for best use, create a .exe file from the .py file and run using windows task scheduler




