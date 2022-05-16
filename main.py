from selenium import webdriver
import time , os
import web.app as wa
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
one = "https://thehimalayantimes.com/kathmandu"
two = "https://thehimalayantimes.com/morearticles/Kathmandu"
thre = 'https://thehimalayantimes.com/nepal'
four = 'https://thehimalayantimes.com/morearticles/Nepal'
five = 'https://epaper.thehimalayantimes.com/'
pwd = os.getcwd()
driver_path = os.path.join(pwd , "firefoxDriver", "geckodriver")
#################################################################
def getwebsite():
    chec_link = ""
    linkslist=[]
    url = "https://thehimalayantimes.com/home"
    first_row = '/html/body/div/main/div[3]/div/div[1]'
    se_row = "/html/body/div/main/div[3]/div/div[1]/div[2]/div/div[1]"
    
    drive = webdriver.Firefox(executable_path=driver_path, options= firefox_options)
    drive.get(url)
    
    ele = drive.find_element(By.XPATH,first_row)
    f = ele.find_elements(By.TAG_NAME,"a")
    
    for x in f:
        newlink = x.get_attribute('href').lower()
        if (chec_link != newlink and (chec_link != one and chec_link != two and chec_link !=thre and chec_link != four)):
            print(chec_link)
            linkslist.append(newlink)
        chec_link = newlink
    linkslist = list(dict.fromkeys(linkslist))
    
    try:
        
        linkslist.remove(one) 
        linkslist.remove(two)
        linkslist.remove(thre)
        linkslist.remove(four)
        linkslist.remove(five)
    except:
        try:
            linkslist.remove(two)
            linkslist.remove(thre)
            linkslist.remove(four)
            linkslist.remove(five)
        except:
            try:
                linkslist.remove(thre)
                linkslist.remove(four)
                linkslist.remove(five)
            except:
                try:
                    linkslist.remove(four)
                    linkslist.remove(five)
                except:
                    try:
                        linkslist.remove(five)
                    except:
                        print("no errors")
                        
                
    
    print("######################################")
    print(linkslist)
        
    drive.close()
    return linkslist



def goto(linkslist):
     drive = webdriver.Firefox(executable_path=driver_path, options=firefox_options)
     title_new = ""
     mybody = ""
     for x in range(len(linkslist)):
        url = linkslist[x]
        drive.get(url)
        try:
            title = drive.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div/div[1]/div[1]/article/h1")
        except:
            print("error")
        body = drive.find_elements(By.XPATH,"/html/body/div[1]/main/div[2]/div/div[1]/div[1]/article/div[6]/div/div")
        print(title.text)
        title_new = title.text
        print(title_new)
        
        try:
            c =""
            for x in body:
                if c != x.text:
                 mybody= mybody + x.text
                 print(mybody)
                c = x.text
            
            wa.add_news(title_new, mybody)
               
        except Exception as e:
            print('\n')
            print(e)
        
        
                
     drive.close()
links = getwebsite()
goto(links)
