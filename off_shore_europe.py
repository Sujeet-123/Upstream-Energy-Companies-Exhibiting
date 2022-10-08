from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.offshore-europe.co.uk/en-gb/exhibitor-directory.html")

time.sleep(6)

driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
time.sleep(5)

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
time.sleep(10)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
time.sleep(10)

links = []
names = []
locations = []
descriptions = []
linkedin = []
websites = []
emails = []
phoneNumbers = []
address = []

divs = driver.find_elements(By.CLASS_NAME,'flexible-content')

for i in divs:
    a = i.find_element(By.TAG_NAME,'a')
    link = a.get_attribute('href')
    links.append(link)
    print(link)
    print(len(links))
# time.sleep(1)
    name = i.find_element(By.XPATH,'.//div[@class="description-container col-md-8 col-xs-12"]/div/div/a/h3').text
    names.append(name)
    print(name)
    try:
        description = i.find_element(By.CLASS_NAME,'wrap-word.line-clamp').text
        descriptions.append(description)
        print(description)
    except:
        descriptions.append("No Data")  
        print("No data")

    try:
        location = i.find_elements(By.CLASS_NAME,'directory-stand')
        locations.append(location[1].text)
        print(location[1].text)

    except:
        locations.append("No data")
        print("No data")

    # if(len(links)==5):
    #     break
    time.sleep(1)
print(len(links))

for i in links:
    driver.get(i)
    time.sleep(6)
    print("=================123==================")

    try:
        hrf = driver.find_element(By.CLASS_NAME,'linkedin-logo-color.social-media-logo.text-center.without-opacity')
        linked = hrf.get_attribute('href')
        linkedin.append(linked)
        print(linked)
    except:
        linkedin.append("No Data")

    try:
        webs = driver.find_element(By.ID,'exhibitor_details_website')
        aweb  = webs.find_element(By.TAG_NAME,'a')
        web = aweb.get_attribute('href')
        websites.append(web)
        print(web)
    except:
        websites.append("No Data")
        print("nodata")


    try:
        mails = driver.find_element(By.ID,'exhibitor_details_email')
        amails = mails.find_element(By.TAG_NAME,'a')
        mail = amails.get_attribute('href')
        emails.append(mail)
        print(mail)
    except:
        emails.append("No Data")
        print("nodata")


    try:
        phones = driver.find_element(By.ID,'exhibitor_details_phone')
        aphone = phones.find_element(By.TAG_NAME,'a').text
        phoneNumbers.append(aphone)
        print(aphone)

    except:
        phoneNumbers.append("No data")
        print("NODATA")


    try:
        addid = driver.find_element(By.ID,'exhibitor_details_address')
        addp = addid.find_element(By.TAG_NAME,'p')
        addsp = addp.find_element(By.CSS_SELECTOR,'span')
        address.append(addsp.text)
        print(addsp.text)
    except:
        address.append("No Data")
        print("No data")





    # time.sleep(2)
    # name = driver.find_element(By.CLASS_NAME,'wrap-word').text
    # names.append(name)
    # time.sleep(1)

  


dic = {
    'Company Name' : names,
    'Company Description' : descriptions,
    'Company Address' : locations,
    'Company Website' : websites,
    'Company tel Number' : phoneNumbers,
    'Company Emails' : emails,
    'Company linkedIn' : linkedin,
    'Comapany Address': address
}

df = pd.DataFrame.from_dict(dic, orient='index')
df = df.transpose()

df.to_csv("offshore-europe.csv")

driver.close()









