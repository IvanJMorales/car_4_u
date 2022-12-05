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

def edmundsmodel(name):
    if "Sport" in name:
        model = name.split(" ")


name = "2020 Mitsubishi Outlander Sport"

if "Sport" in name:
    model = name.split(" ")
    model = model[:-1]
    model = model[-1]
    print(model)