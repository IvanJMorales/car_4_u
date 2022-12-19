from bs4 import BeautifulSoup
import requests
import pandas as pd
import dbcreate_test
import random
import string
import extra



def cars_com_scrape():

    db = dbcreate_test.dbcreate()
    carname = []
    caryear = []
    carprice = []
    carlink = []
    carmiles = []
    carpic = []
    carengine = []
    carmake = []
    carid = 1
    
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
                vehiclename = name.text.strip()
                carname.append(name.text.strip())

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

                manu = extra.namecode(vehiclename)

                condition = soup2.find('p',class_='new-used').text.strip()

                model = extra.modelcode(vehiclename)


                
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
                color = extra.colorcode(color)
        
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
                dbcreate_test.dbinsert(db,carid,data)

        
            website = requests.get(url)
            soup = BeautifulSoup(website.content, "html.parser")
            car_info = soup.find_all('div', class_="vehicle-card-main js-gallery-click-card")

            
        

    dfzip = list(zip(carmake,carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    cardata = pd.DataFrame(dfzip, columns = ['carmake','name','year','price','engine','miles','link','image'])

    cardata.to_csv('testcardata.csv', index=False)
    cardata.to_json('testcardata.json', indent=4, orient="split")
    return cardata


def autotrader_scrape():

    db = dbcreate_test.dbcreate()
    
    pagenum = 4
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection':'keep-alive'
    }
    
    for page in range(pagenum):
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

            condition = car.find('h2').text.strip().split(" ")[0]

            year = name[0:4]

            carmanu = name.split(' ')
            carmanu = carmanu[1]
            carmanu = extra.namecode(name)

            #for land rovers
            if 'Land' in name:
                carmanu = 'Land Rover'

            model = extra.modelcode(name)
                
            #go into car details
            link = 'https://www.autotrader.com' + car.find('a', rel="nofollow")['href']
        
            page = requests.get(link, headers=headers)
            soup2 = BeautifulSoup(page.content, "html.parser")
            pic = soup2.find_all('img')[0]


            if pic != None:
                image = pic['src']
            else:
                image = "N/A"
            
            print(link)

            if soup2.find('span',class_='first-price first-price-lg text-size-700') != None:
                price = soup2.find('span',class_='first-price first-price-lg text-size-700').text.strip()
                price = price.replace(',','').replace('$','')
            else:
                price = "N/A"
        
            engine = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[3].text.strip()
            engine = engine.split(" ")[:-1]
            engine = " ".join(engine)
            #carengine.append(engine)

            color = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[1].text.strip()
            color = color.split(" ")[:-1]
            color = " ".join(color)
            color = extra.colorcode(color)
        
            miles = soup2.find('div',class_='col-xs-10 margin-bottom-0').text.strip()
            miles = miles[:-6].replace(',','')

            #mpg = soup2.find_all('div',class_='col-xs-10 margin-bottom-0')[6].text.strip()
            #mpg = mpg.split(" ")
            #mpg_city = mpg[0]
            #mpg_highway = mpg[3]

            img = str(soup2.find_all('meta')[-1])
            img = img.split(" ")[1].replace('content=\"',"")
            img = img.replace('\"','')
        
            print(name)
            print(carmanu)
            print(year)
            print(price)
            #print(link)
            print(miles)
            print(pic)
            print(engine)
            print(condition)

            #importing data in database


            data = {
                u"Condition": condition,
                u"Name": name,
                u"Manufacturer": carmanu,
                u"Model": model,
                u"Year": year,
                u"Price": price,
                u"Miles": miles,
                u"Link": link,
                u"Image": img,
                u"Engine": engine, 
                u"Color": color#,
                #u"Miles Per Gallon City": mpg_city,
                #u"Miles Per Gallon Highway": mpg_highway
            }

            carid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32)) #creates a 32 character key for the database
            dbcreate_test.dbinsert(db,carid,data)
            


    #dfzip = list(zip(carname,caryear,carprice,carengine,carmiles,carlink,carpic))
    #cardata = pd.DataFrame(dfzip, columns = ['name','year','price','engine','miles','link','image'])
    #cardata.to_csv('testcardata.csv', index=False)


def edmunds_scrape():

    db = dbcreate_test.dbcreate()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection':'keep-alive'
        }

    url = "https://www.edmunds.com/used-cars-new-york-ny"
    x = 2

    while True:

        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, "html.parser")

        cars = soup.find_all('div', class_='d-flex flex-column usurp-inventory-card w-100 srp-expanded')

        url = f"https://www.edmunds.com/used-cars-new-york-ny/?pagenumber={x}"
        x += 1
        print("--------------------------------------------------------------------------------------------------------", url)
        for car in cars:
            #print(car)

            name = car.find('div',class_='size-16 font-weight-bold mb-0_5 text-primary-darker').text.strip()
            price = car.find('span',class_='size-24 font-weight-bold text-gray-darker').text.strip().replace(',','')[1:]
            someinfo = car.find_all('span',class_='')
            mileage = someinfo[0].text.strip().replace(',','').split(' ')[0]
            engine = someinfo[2].text.strip()
            link = f"https://www.edmunds.com{car.find('a',class_='usurp-inventory-card-vdp-link')['href']}"
            img = car.find('img')['src']
            model = extra.modelcode(name)
        
            print(name)
            print(price)
            print(mileage)
            print(engine)
            print(link)
            print(img)

            page = requests.get(link, headers = headers)
            soup2 = BeautifulSoup(page.content, "html.parser")

            manu = soup2.find('h1',class_='not-opaque text-black d-inline-block mb-0 size-24').text.strip().split(' ')[1]
            manu = extra.namecode(name)

            condition = soup2.find('div',class_='text-gray-darker mt-1 mt-md-1_25 medium').text.strip()
            year = soup2.find('h1',class_='not-opaque text-black d-inline-block mb-0 size-24').text.strip().split(' ')[0]

            print(manu)
            print(condition)
            print(year)

            moredetails = soup2.find_all('li',class_='d-flex justify-content-between m-0 pb-0_75 mb-0_75 row')
            color = moredetails[1].text.strip().split('Exterior color')[1][1:]
            color = extra.colorcode(color)


            print(color)

            data = {
                u"Condition": condition,
                u"Name": name,
                u"Manufacturer": manu,
                u"Model": model,
                u"Year": year,
                u"Price": price,
                u"Miles": mileage,
                u"Link": link,
                u"Image": img,
                u"Engine": engine, 
                u"Color": color#,
                #u"Miles Per Gallon City": mpg_city,
                #u"Miles Per Gallon Highway": mpg_highway
            }

            carid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32)) #creates a 32 character key for the database
            dbcreate_test.dbinsert(db,carid,data)

