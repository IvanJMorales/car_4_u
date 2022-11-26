from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import string
#import sqlite3
import dbcreate

"""
def databasecreate():
    
    con = sqlite3.connect("cars.db")
    cur = con.cursor()
    cur.execute(\"""
    CREATE TABLE IF NOT EXISTS cars(
    name TEXT,
    year INTEGER,
    price INTEGER,
    miles INTEGER,
    engine TEXT,
    link TEXT,
    image TEXT)
    \""")

    con.close()
"""


def cars_com_scrape():

    db = dbcreate.dbcreate()
    carname = []
    caryear = []
    carprice = []
    carlink = []
    carmiles = []
    carpic = []
    carengine = []
    carmake = []
    
    page = requests.get("https://www.cars.com")
    soup = BeautifulSoup(page.content, "html.parser")
    car_make_info = soup.find_all('option')
    car_make_info = car_make_info[6:36]

    for manufac in car_make_info:
        
        url = f"https://www.cars.com/shopping/results/?list_price_max=&makes[]={manufac.text.strip().lower()}&maximum_distance=20&models[]=&page=1&page_size=100&stock_type=all"
        #url = f"https://www.cars.com/shopping/results/?list_price_max=&makes[]=tesla&maximum_distance=20&models[]=&page=1&page_size=100&stock_type=all"
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        car_info = soup.find_all('div', class_="vehicle-card-main js-gallery-click-card")
        #print(car_info)
        #print(url)

        pagenum = 1
    
    
        for page in range(pagenum):
            website = requests.get(url)
            soup = BeautifulSoup(website.content, "html.parser")
            nextpage = soup.find('a',id=f'pagination-direct-link-{page + 2}')
            url = 'https://www.cars.com' + nextpage['href']
        
            #print(url)
            #print(page)
        
            
            
            for car in car_info:
            
                carmake.append(manufac.text.strip())
                
                name = car.find('a', class_="vehicle-card-link js-gallery-click-link")
                vehiclename = name.text.strip()[5:]
                carname.append(name.text.strip()[5:])

                vehicleyear = name.text.strip()[:4]
                caryear.append(name.text.strip()[:4])
        
                price = car.find('span', class_="primary-price")
                carprice.append(price.text.strip()[1:].replace(',',''))
                price = price.text.strip()[1:].replace(',','')
            
                link = 'https://www.cars.com' + name['href']
                carlink.append(link)
                
                #print(link)
                #Goes into car page
                carpage = requests.get(link)
                soup2 = BeautifulSoup(carpage.content, "html.parser")

                manu = manufac.text.strip()
                condition = soup2.find('p',class_='new-used').text.strip()

                model = soup2.find('h1', class_="listing-title").text.strip().split(" ")[2]


                
                #IF EV
                if soup2.find_all("dd")[3].text.strip() == "Electric":
                    
                    mileage = soup2.find_all("dd")[8]
                    
                    if mileage == "" or mileage == None:
                        carmiles.append("-")
                        
                    carmiles.append(mileage.text.strip()[:-4].replace(',',''))
                    mileage = mileage.text.strip()[:-4].replace(',','')
                    
                    carengine.append(soup2.find_all("dd")[3].text.strip())
                    engine = soup2.find_all("dd")[3].text.strip()
                #IF NOT EV
                else:
            
                    mileage = soup2.find_all("dd")[9]
                
                    if mileage == "" or mileage == None:
                        carmiles.append("-")
                        
                    carmiles.append(mileage.text.strip()[:-4].replace(',',''))
                    mileage = mileage.text.strip()[:-4].replace(',','')
        
                    carengine.append(soup2.find_all("dd")[6].text.strip())
                    engine = soup2.find_all("dd")[6].text.strip()
                
                color = soup2.find_all("dd")[0].text.strip()
        
                pic = soup2.find('img', class_="swipe-main-image image-index-0")
                
                if pic == None:
                    carpic.append('N/A')
                    pic = 'N/A'
                else:
                    carpic.append(pic['src'])
                    pic = pic['src']
                print("link :", link)
                print("name: ", vehiclename)
                print("year: ", vehicleyear)
                print("price: ", price)
                print("mileage: ", mileage)
                print("engine: ", engine)
                print("condition: ", condition)
                print("color: ", color)
                print("picture: ", pic)
                print("manufacturer: ", manu)
                print("model: ", model)

                data = {
                u"Condition": condition,
                u"Name": vehiclename,
                u"Manufacturer": manu,
                u"Model": model,
                u"Year": vehicleyear,
                u"Price": price,
                u"Miles": mileage,
                u"Link": link,
                u"Image": pic,
                u"Engine": engine, 
                u"Color": color#,
                #u"Miles Per Gallon City": mpg_city,
                #u"Miles Per Gallon Highway": mpg_highway
            }

                carid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32)) #creates a 32 character key for the database

                dbcreate.dbinsert(db,carid,data)

        
            website = requests.get(url)
            soup = BeautifulSoup(website.content, "html.parser")
            car_info = soup.find_all('div', class_="vehicle-card-main js-gallery-click-card")

            
        

    dfzip = list(zip(carmake,carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    cardata = pd.DataFrame(dfzip, columns = ['carmake','name','year','price','engine','miles','link','image'])

    cardata.to_csv('testcardata.csv', index=False)
    cardata.to_json('testcardata.json', indent=4, orient="split")
    return cardata





def autotrader_scrape():

    db = dbcreate.dbcreate()
    carname = []
    caryear = []
    carprice = []
    carlink = []
    carmiles = []
    carpic = []
    carengine = []
    carmake = []
    
    pagenum = 4
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection':'keep-alive'
    }
    
    for page in range(pagenum):
        page += 1
        print(page)
        
        url = 'https://www.autotrader.com/cars-for-sale/all-cars/brooklyn-ny-11201?dma=&searchRadius=25&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=100'

        if page != 1:
            url = 'https://www.autotrader.com/cars-for-sale/all-cars/brooklyn-ny-11201?dma=&searchRadius=25&isNewSearch=false&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=100' + f'&firstRecord={(page - 1)*100}'
    
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, "html.parser")
        car_info = soup.find_all('div', class_="item-card row display-flex align-items-stretch")
    
        for car in car_info:
            

            name = car.find('h2').text.strip().split(" ")[1:]
            name = " ".join(name)
            carname.append(name)

            condition = car.find('h2').text.strip().split(" ")[0]


            year = name[0:4]
            caryear.append(year)

            carmanu = name.split(' ')
            carmanu = carmanu[1]

            #for land rovers
            if 'Land' in name:
                carmanu = 'Land Rover'

            model = name.split(' ')[2]

            if carmanu == 'Land Rover':
                model = name.split(' ')[3:4]
                model = " ".join(model)
                model = "Range Rover"

            carmake.append(carmanu)
                
            #go into car details
            link = 'https://www.autotrader.com' + car.find('a', rel="nofollow")['href']
            carlink.append(link)
        
            page = requests.get(link, headers=headers)
            soup2 = BeautifulSoup(page.content, "html.parser")
            pic = soup2.find('img',class_='carousel-image css-1tknha6-StyledImage e1nnhggb0')

            image = pic['src']
            carpic.append(image)
            
            print(link)

            if soup2.find('span',class_='first-price first-price-lg text-size-700') != None:
                price = soup2.find('span',class_='first-price first-price-lg text-size-700').text.strip()
                price = price.replace(',','').replace('$','')
                carprice.append(price)
            else:
                price = "N/A"
        
            engine = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[3].text.strip()
            engine = engine.split(" ")[:-1]
            engine = " ".join(engine)
            #carengine.append(engine)

            color = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[1].text.strip()
            color = color.split(" ")[0]
        
            miles = soup2.find('div',class_='col-xs-10 margin-bottom-0').text.strip()
            miles = miles[:-6].replace(',','')
            carmiles.append(miles)

            """
            mpg = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[6].text.strip()
            mpg = mpg.split(" ")
            mpg_city = mpg[0]
            mpg_highway = mpg[3]
            """
            print(name)
            print(carmanu)
            print(year)
            print(price)
            print(link)
            print(miles)
            print(pic['src'])
            print(engine)
            print(condition)

            #importing data in database

            """
            cur.execute(f\"""
            INSERT INTO CARS(NAME, MANUFACTURER, YEAR, PRICE, MILES, ENGINE, LINK, IMAGE) VALUES (?,?,?,?,?,?,?,?)\""",
                (f'{name}',
                 f'{carmanu}',
                 f'{year}',
                 f'{price}',
                 f'{miles}',
                 'N/A',
                 f'{link}',
                 f'{image}'
                 )
            )
            con.commit()
            """

            data = {
                u"Condition": condition,
                u"Name": name,
                u"Manufacturer": carmanu,
                u"Model": model,
                u"Year": year,
                u"Price": price,
                u"Miles": miles,
                u"Link": link,
                u"Image": image,
                u"Engine": engine, 
                u"Color": color#,
                #u"Miles Per Gallon City": mpg_city,
                #u"Miles Per Gallon Highway": mpg_highway
            }

            carid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32)) #creates a 32 character key for the database
            dbcreate.dbinsert(db,carid,data)
            


    #dfzip = list(zip(carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    #cardata = pd.DataFrame(dfzip, columns = ['name','year','price','engine','miles','link','image'])
    #cardata.to_csv('testcardata.csv', index=False)

    


    #return cardata


autotrader_scrape()
