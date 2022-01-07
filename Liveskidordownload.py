from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import csv


success = 0
while success == 0:
    url = input("Write correct URL. Must link to Live.skidor.com: ") #Ask user for URL
    if 'live.skidor.com' in url and len(url) >= 27: #Check URL validity
        print("success")
        success = 1
    else:
        print("Plese enter a correct url")
        success = 0
#Sets the preferred webdriver. Can be changed for chromium if desired. See:
#https://www.selenium.dev/documentation/webdriver/getting_started/
driver = webdriver.Firefox()
driver.get(url) #navigate to url in browser

#Sets folder name based on current time and the name of the competition
foldername = time.strftime("%d%m%y-%H%M%S ") + driver.find_element(By.XPATH, "//*[@id='compName']").text
print(foldername)
os.mkdir("./%s" % foldername)

time.sleep(1)

liclass = driver.find_elements(By.CLASS_NAME, "li-class") #find all elements in the dropdown for classes
for classes in liclass: #goes through every class and opens it
    classbutton = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/button")
    classbutton.click()
    classes.click()
    os.mkdir("./%s/%s" % (foldername, classbutton.text)) #creates a folder with the class name
    lipos = driver.find_elements(By.CLASS_NAME, "li-pos") #find all elements in the dropdown for positions (e.g. startlist, finish)
    print(classbutton.text)
    for positions in lipos: #goes through every position and opens it
        posbutton = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/button")
        posbutton.click()
        positions.click()
        time.sleep(0.5) #required delay. Code breaks otherwise since the new elements don't have time to load
        columnelements = driver.find_elements(By.XPATH, "//tr[@data-tab='head']/th")
        columns = len(columnelements) #number of columns in current tab
        rowelements = driver.find_elements(By.XPATH, "//tr[@data-id]")
        rows = len(rowelements) #number of rows in current tab
        f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "x") #create file for current list
        headerlist = []
        print(posbutton.text)
        for x in range(columns): #go through all collumns and create a list of the header info
            columnelementpos = columnelements[x]
            headerlist.append(columnelementpos.text)
        rowlist = []
        print(headerlist)
        f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "a", newline='')
        writer = csv.writer(f)
        writer.writerow(headerlist) #write headers to file
        f.close()
        for i in range(rows): #go through all rows
            rowlist = []
            rowelementpos = rowelements[i]
            for j in range(columns): #go through every item in a row and create a list
                rowelementitems = rowelementpos.find_elements(By.TAG_NAME, "td")
                rowelementtest = rowelementitems[j]
                rowlist.append(rowelementtest.text)
            print(rowlist)
            f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "a", newline='')
            writer = csv.writer(f)
            writer.writerow(rowlist) #write row to file
            f.close()

print("Done!")