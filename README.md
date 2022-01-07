# LiveSkidorDownload
Simple tool to scrape and download cross country ski timings and results from live.skidor.com

Important note:
Do not tamper with the newly open tab, it risks breaking the script.

Usage:
1. Put the python file in a dedicated folder. 
2. If using Firefox, Download this https://github.com/mozilla/geckodriver/releases. 
If using chrome, download this instead https://chromedriver.chromium.org/downloads for your current version. 
(to check chrome version, click the three dots in the top right corner, then "help" and lastly "about chrome") 

 for windows: 
 extract the .ZIP file with a tool like winrar or 7-zip, and put the EXE file in the same folder as the python file. Same for both firfox and chrome.
 
 For linux/unix based systems:
 If using firefox: download Geckodriver from your preferred package manager.
 If using Chrome: download Chromedriver from your preferred package manager.

3. Run the python file with python 3.10 and above, preferably from the terminal.
4. Go to http://live.skidor.com and choose the wanted race and then copy the url of that page, it should look something like this "http://live.skidor.com/XXXX" where the X's are numbers.
5. Input the url to the terminal and let it work!

After this it should start scraping the web for the information. When its done, check the folder where you launched the python file and there should be a folder named after the time it was created and inside is all starting and finish lists in .csv format so it can be directly imported to software like excel.
Good luck!
