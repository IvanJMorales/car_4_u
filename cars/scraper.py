from bs4 import BeautifulSoup
import requests
import pandas as pd
#from models import Car
import sqlite3


def databasecreate():
    
    con = sqlite3.connect("cars.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
    name TEXT,
    year INTEGER,
    price INTEGER,
    miles INTEGER,
    engine TEXT,
    link TEXT,
    image TEXT)
    """)

    con.close()


def cars_com_scrape():

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
    
    for makes in car_make_info:
        
        url = f"https://www.cars.com/shopping/results/?list_price_max=&makes[]={makes.text.strip().lower()}&maximum_distance=20&models[]=&page=1&page_size=100&stock_type=all"
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
            
                carmake.append(makes.text.strip())
                
                name = car.find('a', class_="vehicle-card-link js-gallery-click-link")
                carname.append(name.text.strip()[5:])
        
                caryear.append(name.text.strip()[:4])
        
                price = car.find('span', class_="primary-price")
                carprice.append(price.text.strip()[1:].replace(',',''))
            
                link = 'https://www.cars.com' + name['href']
                carlink.append(link)
                
                print(link)
                #Goes into car page
                carpage = requests.get(link)
                soup2 = BeautifulSoup(carpage.content, "html.parser")
                
                #IF EV
                if soup2.find_all("dd")[3].text.strip() == "Electric":
                    
                    mileage = soup2.find_all("dd")[8]
                    
                    if mileage == "" or mileage == None:
                        carmiles.append("-")
                        
                    carmiles.append(mileage.text.strip()[:-4].replace(',',''))
                    
                    carengine.append(soup2.find_all("dd")[3].text.strip())
                #IF NOT EV
                else:
            
                    mileage = soup2.find_all("dd")[9]
                
                    if mileage == "" or mileage == None:
                        carmiles.append("-")
                        
                    carmiles.append(mileage.text.strip()[:-4].replace(',',''))
        
                    carengine.append(soup2.find_all("dd")[6].text.strip())
        
                pic = soup2.find('img', class_="swipe-main-image image-index-0")
                
                if pic == None:
                    carpic.append('N/A')
                else:
                    carpic.append(pic['src'])
        
        
                print(name.text.strip()[5:])
                print(name.text.strip()[:4])
                print(price.text.strip()[1:].replace(',',''))
                print(mileage.text.strip()[:-4].replace(',',''))
                print(soup2.find_all("dd")[6].text.strip())
                #print(link)
                #print(pic['src'])
                #print(pic)

        
            website = requests.get(url)
            soup = BeautifulSoup(website.content, "html.parser")
            car_info = soup.find_all('div', class_="vehicle-card-main js-gallery-click-card")

            
        

    dfzip = list(zip(carmake,carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    cardata = pd.DataFrame(dfzip, columns = ['carmake','name','year','price','engine','miles','link','image'])

    cardata.to_csv('testcardata.csv', index=False)
    cardata.to_json('testcardata.json', indent=4, orient="split")
    return cardata


def autotrader_scrape():
    carname = []
    caryear = []
    carprice = []
    carlink = []
    carmiles = []
    carpic = []
    carengine = []
    carmake = []
    
    pagenum = 10
    
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
            #name = name[5:]
            carname.append(name)

            year = name[0:4]
            caryear.append(year)

            carmanu = name.split(' ')
            carmanu = carmanu[1]

            #for land rovers
            if 'Land' in name:
                carmanu = 'Land Rover'

            carmake.append(carmanu)
                
            #go into car details
            link = 'https://www.autotrader.com' + car.find('a', rel="nofollow")['href']
            carlink.append(link)
        
            page = requests.get(link, headers=headers)
            soup2 = BeautifulSoup(page.content, "html.parser")
            pic = soup2.find('img',class_='carousel-image css-1tknha6-StyledImage e1nnhggb0')

            image = pic['src']
            carpic.append(image)

            price = soup2.find('span',class_='first-price first-price-lg text-size-700').text.strip()
            price = price.replace(',','').replace('$','')
            carprice.append(price)
        
            engine = soup2.find('div',class_='col-xs-10 margin-bottom-0').text.strip()
            carengine.append(engine)
        
            miles = soup2.find('div',class_='col-xs-10 margin-bottom-0').text.strip()
            miles = miles[:-6].replace(',','')
            carmiles.append(miles)
        
            print(name)
            print(carmanu)
            print(year)
            print(price)
            print(link)
            print(miles)
            print(pic['src'])
            print(engine)

            #importing data in database
            cur.execute(f"""
            INSERT INTO CARS(NAME, MANUFACTURER, YEAR, PRICE, MILES, ENGINE, LINK, IMAGE) VALUES (?,?,?,?,?,?,?,?)""",
                (f'{name}',
                 f'{carmanu}',
                 f'{year}',
                 f'{price}',
                 f'{miles}',
                 f'{engine}',
                 f'{link}',
                 f'{image}'
                 )
            )
            con.commit()

            


    dfzip = list(zip(carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    cardata = pd.DataFrame(dfzip, columns = ['name','year','price','engine','miles','link','image'])
    cardata.to_csv('testcardata.csv', index=False)

    


    return cardata


#databasecreate()

con = sqlite3.connect("cars.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
    name TEXT,
    manufacturer TEXT,
    year INTEGER,
    price INTEGER,
    miles INTEGER,
    engine TEXT,
    link TEXT,
    image TEXT)
    """)

autotrader_scrape()
con.close()