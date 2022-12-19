#I didnt wanna put these functions in other files :)

def colorcode(color):
    if ("Red" in color) or ("red" in color) or ("Ruby" in color) or ("Sangria" in color):
        color = "Red"
    elif ("Blue" in color) or ("blue" in color):
        color = "Blue"
    elif ("Green" in color) or ("green" in color):
        color = "Green"
    elif ("Black" in color) or ("black" in color):
        color = "Black"
    elif ("Yellow" in color) or ("yellow" in color):
        color = "Yellow"
    elif ("Gray" in color) or ("gray" in color) or ("Grey" in color) or ("grey" in color) or ("Steel" in color) or ("steel" in color) or ("Silver" in color) or ("Granite" in color):
        color = "Gray"
    elif "Orange" in color:
        color = "Orange"
    elif "White" in color:
        color = "White"
    else:
        return color
    return color

def modelcode(name):
    carmodels = ['3000ME', 'Cobra', 'Frua', 'Romeo 75', 'Romeo 33', 'Romeo 33 Stradale', 'Romeo 155', 'Romeo 156', 'Romeo Alfasud', 'Romeo Arna', 'Romeo Brera', 'Romeo GT', 'Romeo Montreal', 'Romeo Spider', 'Romeo SZ and RZ', 'A106', 'A108/Willys Interlagos', 'A110', 'A310', 'Alpine GTA/A610', 'Gremlin', 'Hornet', '80 and 90', 'Coupé/*Quattro', 'A3', 'A4', 'R8', 'A1', 'A2', 'Sprite', 'Allegro', 'Maestro', 'Metro', 'Montego', 'A111', 'A112','ILX', 'Y10', 'II', 'ADO16', 'ADO17', '326', '328', '327', '507', '503', '3200 CS', 'New Class', '2000C and 2000CS', 'CS', 'i3', 'i8', 'M1', 'Z1', 'Z8', '3 Series', '5 Series', '8 Series', 'X5', 'Type 18', 'Type 30', 'Type 35', 'Type 37', 'Type 38', 'Type 39', 'Type 40', 'Type 41', 'Type 50', 'Type 51', 'Type 55', 'Type 57', 'Type 101', 'EB110', 'Veyron', 'Apollo', 'Centurion', 'Electra', 'Invicta', 'LeSabre', 'Riviera', 'Special', 'Wildcat', 'e6', 'F3DM', 'Qin', 'Tang', 'Cimarron', 'Allanté', 'De Ville',\
'ELR', 'Marathon', 'Camaro', 'Caprice', 'Cavalier', 'Citation', 'Corvair', 'Corvette', 'Cruze', 'Impala', 'Malibu', 'Monza', 'Opala', 'Suburban', 'Vega', 'Volt', 'Aspen Hybrid', 'Newport', 'TC by Maserati', 'minivans', 'Town & Country', '2CV', 'DS', 'Mark II', 'Copen', 'DeLorean', 'Tomaso Deauville', 'Tomaso Guarà', 'Tomaso Longchamp', 'Tomaso Mangusta', 'Tomaso Pantera', 'Tomaso Vallelunga', 'Custom', 'Aries/Plymouth Reliant', 'Coronet', 'Stealth', 'Viper', 'Talon', 'Bermuda', 'Corsair', 'Citation', 'Pacer', 'Ranger', 'Roundup', 'Villager', 'Series II', 'Vega FV/FVS/HK500', 'Vega Excellence', 'II', 'III',\
'Vega 6', '166 MM', '212 Inter', '250 MM', '250 GT Coupé', '250 GT Berlinetta', '250 GT Berlinetta SWB', '250 GT', '250 GTO', '250 GT Lusso', '275', '330 GT 2+2', '250 LM', '330 GTC and GTS', 'Dino', '365 GT 2+2', '365 GTC and GTS', '365 GTB/4 and GTS/4', '512S', '365 GTC/4', '365 GT4 2+2, 400 and 412', 'BB', '308 GTB and GTS', 'Mondial', 'Testarossa', '288 GTO', '328', 'F40', '348', '456', '333 SP', 'F355', 'F50', '550 Maranello', '575M Maranello', '360', 'Ferrari', 'F430', '458', 'FF', '124', '126', '127', '500', 'Panda', 'Punto', 'Uno', 'X1/9', '131', 'Karma', 'Aerostar','Charger', 'CE14 platform', 'Cortina', 'Crown Victoria', 'D186 platform', 'E-Series', 'Escort/(North America)', 'Explorer', 'F-Series', 'Falcon', 'Fiesta', 'Fiesta', 'Focus', 'Granada (North America)', 'GT', 'LTD', 'Model A', 'Model T', 'Mustang', 'Puma', 'Ranchero', 'Ranger', 'Ranger (T6)', 'RS200', 'Sierra', 'Taurus', 'Tempo', 'Thunderbird', 'Transit', 'Standard', 'Polonez', 'A platform', 'A platform', 'A platform', 'B platform', 'B platform', 'B platform', 'B platform', 'B platform', 'D platform', 'J platform', 'W platform', 'J Deluxe', 'Ambassador', 'Commodore', 'Accord', 'Beat', 'Civic', 'CR-V', 'Fit', 'NSX', 'Prelude', 'S600', 'S500', 'S800', 'S2000', 'Super', 'Elantra', 'Accent', 'Sonata', 'Crown', 'Isetta', 'XK120', 'C-Type', 'D-Type', 'Mark 1', 'XK150', 'Mark 2', 'E-Type', 'XJ', 'XJS', 'XJR-15', 'XJ220', 'XK', 'X-Type', 'XF', 'Cherokee (XJ)', 'CJ', 'Wrangler', 'Cherokee (KL)', 'Renegade', 'Compass', 'Interceptor', 'Deluxe', 'Riva', 'Marquise', '11, 11.9, 12 and 12/24', '14/60 and 2-litre Speed', '16/65', '3-litre', '16/80', 'Rapier', 'M45', '3.5-litre', 'LG45', 'LG6', 'V12', '2.6-Litre', '3-Litre', 'Rapide', 'Taraf', '350GT', '400GT', 'Aventador', 'Countach', 'Diablo', 'Espada', 'Gallardo', 'Huracán', 'Islero', 'Jalpa', 'Jarama', 'LM002', 'Miura', 'Murciélago', 'Reventón', 'Silhouette', 'Urraco', 'Urus', 'Stratos', 'Montecarlo', 'Dedra', 'Ypsilon', 'Rover Series/Defender', 'Rover Discovery', 'Rover Freelander', 'Rover Discovery Sport', 'Range Rover', 'Rover Evoque', 'Rover Sport', 'CT', 'LFA', 'Car Company Rocket', 'Continental', 'Town Car', 'Versailles', 'T70', 'Elise', 'F1', 'P1', '12C', '800', 'Biturbo', '3200 GT', 'Coupé and Spyder', 'MC12', 'GranTurismo', '57 and 62', 'Rancho', 'Familia', 'MPV', 'MX-5', 'R360', 'RX-7', 'RX-8', 'Type 300', '600', 'C-Class', 'CLK GTR', 'G-Class', 'SLR McLaren', 'S-Class', 'SL-Class', 'W123', 'W201', 'GT', 'Bobcat',\
'Colony Park', 'RDX','HR-V','Pacifica','Terrain','CX-5','A7', 'Romeo Stelvio', 'Q50','Escalade', 'NX','Insight', 'RX', 'Patriot','X1', 'Challenger', 'MDX','MKZ', 'TLX', 'ILX', 'Cougar', 'Altima','GLA-Class', 'Cyclone', 'Grand Marquis', 'Marauder', 'Mariner', 'Milan', 'Monarch', 'Montego', 'Monterey', 'Monterey (minivan)', 'Mountaineer', 'Sable', 'Turnpike Cruiser', 'Villager', 'KR175', 'KR200', 'F and TF', 'MGB', 'Midget', 'XPower SV', 'Carisma', 'Galant', 'GTO', 'Lancer', 'L200', 'Rogue', 'CLA-Class',\
'Outlander', 'Outback', 'Pajero', 'Ital', 'Marina', 'Minor', 'Statesman', 'Be-1', 'S-Cargo', 'Figaro', 'Leaf', 'Maxima', 'Micra', 'Qashqai/Rogue Sport', 'Tiida/Versa', 'Sunny/Sentra/Pulsar/Almera', 'Z-cars', 'Aurora', 'Cutlass', '88', 'Ascona', 'Astra', 'Corsa', 'Vectra', '07', 'Eight', 'Huayra', 'Esperante', 'Roadster', 'P50', 'Trident', '204', '205', '206', '504', '406 coupé', 'Fury', 'Prowler', 'Aries/Plymouth Reliant', 'Voyager', 'Astre', 'Aztek', 'Bonneville', 'Firebird', 'Grand Am', '356', '550', '911', '904', '906', '908', '914', '917', '924', '928', '944', '956', '962', '959', '968', 'Boxster', 'Cayenne', 'Carrera GT', 'Panamera', '918', 'Macan', 'Classic', '4CV', 'Dauphine', 'Clio', 'Sport Spider', 'Twingo', 'Twizy', 'Zoe', '25', '45', '75', '800', '900', 'S7', 'S-Series', 'Ibiza', '1000', '1100', 'Octavia', 'Champion', 'Fortwo', 'Roadster', '360', 'Alcyone', 'Legacy', 'Cappuccino', 'Jimny', 'Wagon R', 'Swift', 'FR2000', 'F4-T014', 'MSV F4-016', 'USF-17', 'PM-18', 'FT-50', 'F.3 T318', 'Model 3', 'Model S', 'Model X', 'Roadster', '2000GT', '86/Scion FR-S/Subaru BRZ', 'Camry', 'Celica', 'Corolla', 'Curren', 'Hilux', 'Ipsum', 'Land Cruiser', 'Mirai', 'Prius', 'RAV4', 'Soarer/Lexus SC', 'Sports 800', 'Stout/Toyopet RK', 'Supra', 'Viva', 'W8', 'M12', 'Beetle', 'Gol', 'Golf', 'Jetta', 'Passat', 'Polo', 'PV444/544', 'Duett', 'Amazon', 'P1800', '140', '164', '200 series', '300', '700 series', '850', 'S40/V40', 'V70/XC70', '77', '965 Zaporozhets', 'Skala']
    for model in carmodels:
        if model in name:
            return model
    return "Failed"

def namecode(name):
    carmanu = ['Audi','Acura','MAZDA', 'BMW', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Honda', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia', 'Land Rover', 'Lexus', 'Lincoln', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Porsche', 'RAM', 'Subaru', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'AC', 'Alfa Romeo', 'Am General', 'American Motors', 'Aston Martin', 'Austin-Healey','Avanti Motors', 'Bentley', 'Bugatti', 'Citroen', 'Datsun', 'Delorean', 'Desoto', 'DeTomaso', 'Edsel', 'Ferrari', 'FIAT', 'Fisker', 'Genesis', 'Geo', 'Hudson', 'Hummer', 'International', 'Isuzu', 'Jensen', 'Kaiser', 'Karma', 'Lamborghini', 'LaSalle', 'Lotus', 'Lucid', 'Maserati', 'Maybach', 'McLaren','Mercury', 'MG', 'MINI', 'Morgan', 'Nash', 'Oldsmobile', 'Opel','Packard', 'Pagani', 'Plymouth', 'Polestar', 'Pontiac', 'Qvale', 'Rivian', 'Rolls-Royce', 'Saab', 'Saleen', 'Saturn', 'Scion', 'smart', 'Studebaker', 'Sunbeam', 'Suzuki', 'Triumph', 'Willys']
    for manu in carmanu:
        if manu in name:
            return manu
    return "Failed"

test = "2022 Acura TLX Type S"

print(namecode(test))