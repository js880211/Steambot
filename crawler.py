import requests,time,json
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium and BS4 setup
webdriver_path = 'C:/Users/User/Desktop/chromedriver.exe'
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get("https://store.steampowered.com/search/?specials=1&category1=998") #前往這個網址
r=driver.page_source
soup = BeautifulSoup(r, 'html.parser')
num=soup.find(id="search_results_filtered_warning_persistent").div.text

#get number
temp=''
for n in num:
    if n!=' ':
        temp+=n
    else:
        break
temp=temp.replace(',','')
counter=int(temp)//50+1

#get discount game
game=[]
while(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    counter-=1
    if(counter==0):
        r=driver.page_source
        soup = BeautifulSoup(r, 'html.parser')
        for i in soup.find_all(class_='search_result_row ds_collapse_flag'):
            print(i.span.string)
            game.append(i.span.string+'<br>')
        f = open('data.json','w')
        f.write(json.dumps(game))
        f.close()
        break
    else:
        continue
driver.close()