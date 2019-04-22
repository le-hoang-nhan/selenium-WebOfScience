import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import numpy as np

#Create intervals of records to download articiles:
arrayStart = np.array(range(0, 4002, 500))
arrayEnd = np.array(range(1, 4002, 500))
array = np.concatenate((arrayStart, arrayEnd))
array.sort()
array = np.delete(array, 0)
array = np.delete(array, -1)

#Set browswer path
browswerPath = "G:\OneDrive - studenti.unitn.it\Projects\WebOfScience/chromedriver"

#Open up a Chrome browser and navigate to web page
driver = webdriver.Chrome(browswerPath)
driver.get("https://apps.webofknowledge.com/Search.do?product=WOS&SID=E4vgzdX8syup9Pbsfnb&search_mode=GeneralSearch&prID=25ff6a8f-1fb5-452f-bce0-05a1529cf88d")

for start, end in zip(array[0::2], array[1::2]):

    # Choose radio button in Number of Records:
    element = driver.find_element_by_id("saveToMenu")
    dropbox = Select(element)
    dropbox.select_by_value("other")

    # Choose Record Content is Full Record
    recordContent = driver.find_element_by_id("bib_fields")
    dropbox = Select(recordContent)
    dropbox.select_by_index(2)

    # driver.implicitly_wait(5)

    # Choose File Format is Tab-delimited (Win, UTF-8):
    fileFormat = driver.find_element_by_id("saveOptions")
    dropbox = Select(fileFormat)
    dropbox.select_by_value("tabWinUTF8")

    # Fill range of record from ... to ....
    markFrom = driver.find_element_by_id("markFrom")
    markFrom.send_keys(int(start))
    markFrom.send_keys(Keys.RETURN)

    markTo = driver.find_element_by_id("markTo")
    markTo.send_keys(int(end))
    markTo.send_keys(Keys.RETURN)

    # Refresh the page
    driver.refresh()










#Click Send button to get the file.txt
#sendButton = driver.find_element_by_class_name("standard-button primary-button")
#sendButton.click()

#Work in Email Close Button.
#CloseButton = driver.find_element_by_class_name("quickoutput-cancel-action").click()

#CloseButton = driver.find_element_by_xpath("//*[@id='ui-id-9']/form/div[2]/a").click()

#CloseButton = driver.find_element_by_id("ui-id-9").click()
#CloseButton = driver.find_elements_by_class_name("quickoutput-cancel-action").click()
#CloseButton = driver.find_element_by_xpath("//a[contains(text(),'Cancel')])[5]").click()
#CloseButton = driver.find_element_by_xpath("//a[contains(@href, '#')])[5]").click()
#CloseButton = driver.find_element_by_xpath("//*[@id='ui-id-9'']/form/div[2]/a/@href").click()





#cancel = driver.find_element_by_link_text("#").click()
#driver.get("https://apps.webofknowledge.com/Search.do?product=WOS&SID=C28IMnMUcwh3MxDMk4y&search_mode=GeneralSearch&prID=0a24045c-44b2-49f4-828f-117d4e958fab#")
#cancel = driver.find_element_by_class_name("quickoutput-cancel-action").click()

#driver.find_element_by_xpath('//div[contains(@class,"ui-dialog") and @aria-describedby="dialogContent2"]//button[@title="Close"]').click()
#cancel = driver.find_element_by_class_name("ui-button ui-widget ui-state-default ui-corner-all ui-dialog-titlebar-close ui-button-icon-only ui-state-hover").click()
#cancel = driver.find_element_by_link_text("Close").click()
#cancel = driver.find_element_by_class_name("ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close").click()
