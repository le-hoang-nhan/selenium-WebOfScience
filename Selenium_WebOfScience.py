from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import numpy as np

linkDownload = input('''After filling your keywords and pushing search button. 
Please copy and enter here the URL of the current window showing the searching result:
''')
toRecord = int(input('''We download from record 1. 
Please enter the number in which we will end to download: (example: 1000, 4500)
'''))


#Create intervals of records to download articiles:
arrayStart = np.array(range(0, toRecord +2, 500))
arrayEnd = np.array(range(1, toRecord +2, 500))
array = np.concatenate((arrayStart, arrayEnd))
array.sort()
array = np.delete(array, 0)
array = np.delete(array, -1)

#Set browswer path
browswerPath = "G:\OneDrive - studenti.unitn.it\Projects\WebOfScience/chromedriver"

#Open up a Chrome browser and navigate to web page
driver = webdriver.Chrome(browswerPath)
driver.get(linkDownload)

for start, end in zip(array[0::2], array[1::2]):
    # Choose export button
    driver.find_element_by_xpath("//*[@id='exportTypeName']").click()
    # Choose Other File Formats button
    #driver.find_element_by_xpath("//*[@id='saveToMenu']/li[3]/a").click()

    # Choose Record Content is Full Record
    recordContent = driver.find_element_by_id("bib_fields")
    dropbox = Select(recordContent)
    dropbox.select_by_index(2)

    # Choose File Format is Tab-delimited (Win, UTF-8):
    fileFormat = driver.find_element_by_id("saveOptions")
    dropbox = Select(fileFormat)
    dropbox.select_by_value("tabWinUTF8")

    # Choose radio button
    driver.find_element_by_xpath("//*[@id='numberOfRecordsRange']").click()

    # Fill range of record from ... to ....
    driver.find_element_by_id("markFrom").clear()
    markFrom = driver.find_element_by_id("markFrom")
    markFrom.send_keys(int(start))

    driver.find_element_by_xpath("//*[@id='markTo']").clear()
    markTo = driver.find_element_by_id("markTo")
    markTo.send_keys(int(end))
    markTo.send_keys(Keys.RETURN)

    driver.refresh()
