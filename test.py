from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import smtplib
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.chrome.options import Options as cOP

chrome_options = cOP()
chrome_options.add_argument('--headless')
chrome_options.headless = True


def trigger_mail(Recipients, User, Pass, Message):
    mail_content = '''Hello,
    ''' + Message + '''
    '''
    # The mail addresses and password
    sender_address = User
    sender_pass = Pass
    receiver_address = [Recipients]

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ", ".join(receiver_address)
    message['Subject'] = 'A test mail sent by Python.'  # The subject line
    # The body and the attachments for the mail

    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


# driver = webdriver.Chrome()
# driver.get("https://apartmentlove.com/")
# driver.find_element(By.XPATH, "//button[@id='consent-popup-accept']").click()
# driver.find_element(By.XPATH, "(//div[@class='cityList-title'])[1]").click()
# c = driver.current_url
c = "https://apartmentlove.com/apartments-for-rent/austin/texas/united-states"
req = requests.get(c)
t = req.status_code
if t == 200:
    print("Site is working, Status code :" + str(t))
else:
    # print("Site is not working")
    trigger_mail('avneet@netzoptimize.com', 'avneet.ratiocinativesolutions@gmail.com', 'zfjsxcghnhvmewco','Site is not working Status code :' + str(t))
    assert False
# t = requests.get("https://apartmentlove.com/")
# s = t.status_code
# print(p)
# ts = time.time()
# date_time = datetime.fromtimestamp(ts)
# str_date_time = date_time.strftime("%H:%M")
# print(str_date_time)
# print(int(str_date_time))
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# now_plus_10 = now + timedelta(minutes = 10)
# print(now_plus_10)
# if s == 200:
#     print("Site is working")
#
# else:
#     print("Send a mail to user site is not working")
#
#     while True:
#         time.sleep(30)
#         c = 404
#         if c == 200:
#             print("Site is working now")
#             break
#         else:
#             print("site is not working")


# driver = webdriver.Chrome()
#
# driver.get("https://apartmentlove.com/")
#
# driver.set_window_size(1920,1024)
# t = driver.find_element(By.XPATH,"//div[@class='cityList-title']//h4[contains(text(),'Philadelphia Apartments')]")
# if t :
#     print("Avneet")
# else:
#     print("Not available")
# driver.quit()
#
# driver = webdriver.Firefox()
# driver.get("https://apartmentlove.com/")
# t = driver.find_element(By.XPATH,"//div[@class='cityList-title']//h4[contains(text(),'Philadelphia Apartments')]")
# if t :
#     print("Thakur")
# else:
#     print("Not available")
# driver.quit()
