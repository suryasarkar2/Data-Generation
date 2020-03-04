import pandas as pd
from flask import request, jsonify

def func_C():
    df = pd.read_csv('customer_details.csv')

    age = df.age
    gender = df.gender
    data = []
    print(type(age[0]))
    male_c = 0
    female_c = 0
    other_c = 0
    for i in range(len(age)):
        if gender[i] == 'Male':
            male_c += 1
        if gender[i] == 'Female':
            female_c += 1
        if gender[i] == 'Others':
            other_c += 1

    data.append({'Name':'Male', 'y': male_c, 'sliced': True, 'selected': True})
    data.append({'Name':'Female', 'y': female_c})
    data.append({'Name':'Others', 'y': other_c})

    print(data)
    return data

def func_O():
    df = pd.read_csv('order_details.csv')

    order_id = df.orderid
    order_date = df.ots
    dishtype = df.DishName
    year = []
    year2 = []

    for i in range(len(order_date)):
        y = int(str(order_date[i])[:4])
        year2.append(y)
        if y not in year:
            year.append(y)
    year.sort(reverse=True)
    data = []
    i = 0
    for each in year:
        oc = 0
        for each2 in year2:
            if each == each2:
                oc += 1
        if i == 0:
            data.append({'Name': each, 'y': oc, 'sliced': True, 'selected': True})
        else:
            data.append({'Name': each, 'y': oc})
        i=i+1
    return data

def func_O2():
    df = pd.read_csv('order_details.csv')

    dishtype = df.DishName
    dish = []
    dish2 = []

    for i in range(len(dishtype)):
        d = dishtype[i]
        dish.append(d)
        if d not in dish2:
            dish2.append(d)
    data = []
    i = 0
    for each in dish2:
        oc = 0
        for each2 in dish:
            if each == each2:
                oc += 1
        if i == 0:
            data.append({'Name': each, 'y': oc, 'sliced': True, 'selected': True})
        else:
            data.append({'Name': each, 'y': oc})
        i = i + 1
    return data

def func_O3():
    l1=[]
    l2=[]
    l4=[]
    l5=[]
    l6=[]
    total=[]
    df=pd.read_csv('food_details.csv')
    cat= df['Category']   
    for i in range(len(cat)):
        l1.append(str(cat[i]))
    for i in l1:
        if i not in l2:
            l2.append(i)
    #total.append(l2)
    for i in l2:
        l3=[]
        df2=df.loc[df['Category'] == str(i)]
        for i in df2['PriceSmall']:
            l3.append(int(i))
        avgsmall=sum(l3)/len(l3)
        #print(l3)
        l4.append(int(avgsmall))
    for i in l2:
        l3=[]
        df2=df.loc[df['Category'] == str(i)]
        for i in df2['PriceMedium']:
            l3.append(int(i))
        avgsmall=sum(l3)/len(l3)
        #print(l3)
        l5.append(int(avgsmall))
    for i in l2:
        l3=[]
        df2=df.loc[df['Category'] == str(i)]
        for i in df2['PriceLarge']:
            l3.append(int(i))
        avgsmall=sum(l3)/len(l3)
        #print(l3)
        l6.append(int(avgsmall))
    
    d1={
    "name": 'Price Small',
    "data": l4
    }
    d2={
    "name": 'Price Medium',
    "data": l5
    }
    d3={
    "name": 'Price Large',
    "data": l6
    }
    l7=[]
    l7.append(d1)
    l7.append(d2)
    l7.append(d3)
    #print(l7)
    return l7
    
def func_M():
    df = pd.read_csv('food_details.csv')

    # Sl No.,dishId,dishname,category,pricesmall,foodcostsmall,labourcostsmall,overheadcostsmall,priceMedium,foodcostmedium,labourcostmedium,overheadcostmedium,priceLarge,foodcostlarge,labourcostlarge,overheadcostlarge

    category = df.Category
    pricesmall = df.PriceSmall
    foodcostsmall = df.FoodCostSmall
    labourcostsmall = df.LabourCostSmall
    overheadcostsmall = df.OverheadCostSmall

    pricemedium = df.PriceMedium
    foodcostmedium = df.FoodCostMedium
    labourcostmedium = df.LabourCostMedium
    overheadcostmedium = df.OverheadCostMedium

    pricelarge = df.PriceLarge
    foodcostlarge = df.FoodCostLarge
    labourcostlarge = df.LabourCostLarge
    overheadcostlarge = df.OverheadCostLarge

    nor = len(pricesmall)

    tot_ps = 0
    tot_fcs = 0
    tot_lcs = 0
    tot_ohcs = 0

    categories = ['Mexican', 'Indian', 'Italian', 'Cajun', 'Soul', 'Thai', 'Greek', 'Chinese', 'Lebanese',
                  'Japanese', 'American', 'Moroccan', 'Mediterranean', 'French', 'Spanish', 'German', 'Korean',
                  'Turkish', 'Caribbean', 'Vietnamese']

    profit_small = []
    profit_medium = []
    profit_large = []

    data = []

    for i in range(len(categories) - 1, -1, -1):
        c = categories[i]
        tot_ps = 0
        tot_fcs = 0
        tot_lcs = 0
        tot_ohcs = 0

        tot_pm = 0
        tot_fcm = 0
        tot_lcm = 0
        tot_ohcm = 0

        tot_pl = 0
        tot_fcl = 0
        tot_lcl = 0
        tot_ohcl = 0

        avg_profit_small = 0
        avg_profit_medium = 0
        avg_profit_large = 0

        for i in range(len(category)):
            if c == category[i]:
                tot_ps = tot_ps + pricesmall[i]
                tot_fcs = tot_fcs + foodcostsmall[i]
                tot_lcs = tot_lcs + labourcostsmall[i]
                tot_ohcs = tot_ohcs + overheadcostsmall[i]
                avg_profit_small = (tot_ps / nor) - ((tot_fcs / nor) + (tot_lcs / nor) + (tot_ohcs / nor))

                tot_pm = tot_pm + pricemedium[i]
                tot_fcm = tot_fcm + foodcostmedium[i]
                tot_lcm = tot_lcm + labourcostmedium[i]
                tot_ohcm = tot_ohcm + overheadcostmedium[i]
                avg_profit_medium = (tot_pm / nor) - ((tot_fcm / nor) + (tot_lcm / nor) + (tot_ohcm / nor))

                tot_pl = tot_pl + pricelarge[i]
                tot_fcl = tot_fcl + foodcostlarge[i]
                tot_lcl = tot_lcl + labourcostlarge[i]
                tot_ohcl = tot_ohcl + overheadcostlarge[i]
                avg_profit_large = (tot_pl / nor) - ((tot_fcl / nor) + (tot_lcl / nor) + (tot_ohcl / nor))
        profit_small.append(int(avg_profit_small))
        profit_medium.append(int(avg_profit_medium))
        profit_large.append(int(avg_profit_large))

        print('Category {}  Average Profit {}'.format(c, avg_profit_small))

    data.append({'name': 'Profit Small', 'data': profit_small})
    data.append({'name': 'Profit Medium', 'data': profit_medium})
    data.append({'name': 'Profit Large', 'data': profit_large})


    return data
    #print(l4)
    #print(df['pricesmall'])

