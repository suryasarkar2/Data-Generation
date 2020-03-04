from flask import request, Response, jsonify, send_file, render_template
import flask
import requests
import csv
from mimesis import Food
from faker import Faker
import random
import urllib
import json
import pandas as pd
import customer1
import menulist
import order2
import csvTOjson



cust_al=[]
menu_list_all = []

columns=['DishId', 'DishName', 'Category', 'PriceSmall', 'FoodCostSmall', 'LabourCostSmall', 'OverheadCostSmall', 'PriceMedium', 'FoodCostMedium', 'LabourCostMedium', 'OverheadCostMedium', 'PriceLarge', 'FoodCostLarge', 'LabourCostLarge', 'OverheadCostLarge']
categories  = ['Mexican','Indian','Italian','Cajun','Soul','Thai','Greek','Chinese','Lebanese','Japanese','American','Moroccan','Mediterranean','French','Spanish','German','Korean','Turkish','Caribbean','Vietnamese']
gender = ['Male','Female','Others']


column=['customer_id','customer_name','gender','age','phone_no','email','address']

# Create the application.
app = flask.Flask(__name__)
food = Food()
fake = Faker(['en-US'])

#generate/customer-details
@app.route('/')
def my_form():
    return render_template('web.html')

@app.route('/generate/customer-details',methods =['GET','POST'])
def generateCustomerDetails():
    try:
        if request.method =='POST':
            text = request.form['text1']
            print(text)
            #body = request.get_json()
            #rows=int(body['rows'])
            for i in range(1,int(text)+1):
                gender_picker = random.randrange(len(gender))
                cust_ind = []
                # print('EMAIL {} - ADDRESS {} - NAME {} - GENDER {} - AGE {} - PHONE_NUMBER {}'.format(fake.email(),fake.address(),fake.name_female(), "Female",random.randrange(18,90),fake.phone_number()))
                #customerid,name,gender,age,phone,email,addrs
                cust_ind.append(str(i))
                cust_ind.append(fake.name())
                cust_ind.append(gender[gender_picker])
                cust_ind.append(random.randrange(18, 90))
                cust_ind.append(fake.phone_number().replace('x', '0'))
                cust_ind.append(fake.email())
                cust_ind.append(fake.address().replace('\\n', ''))
            
                cust_al.append(cust_ind)
            #print('a')
            #print(cust_al)
            with open('customer_details.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(column)
                for i in range(int(text)):
                    writer.writerow(cust_al[i])
                file.close()
            print('b')
            filepath='customer_details.csv'
            print('c')
            return send_file(filepath,
                mimetype='text/csv',
                attachment_filename='customer_details.csv',
                as_attachment=True)
            print('Successful')
    except Exception as e:
        return {"Error:":e}

@app.route('/generate/food-details',methods =['GET','POST'])
def generateFoodDetails():
    try:
        if request.method =='POST':
            rows=int(request.form['text2'])
            for i in range(rows):
                menu_list_ind = []

                item = food.dish()
                item_category = categories[random.randrange(0,len(categories)-1)]

                #Pricing Determining
                p_sm = random.randrange(190, 900)
                p_md = p_sm + (0.10 * p_sm)
                p_lg = p_sm + (0.25 * p_sm)
                #PERCENTAGES FOR SMALL
                fcs_percent = random.randrange(25, 35)
                lcs_percent = random.randrange(10, 25)
                ocs_percent = 5
                #PERCENTAGES FOR MEDIUM
                fcm_percent = fcs_percent + random.randrange(1,3)
                lcm_percent = lcs_percent + random.randrange(1,3)
                ocm_percent = 5
                #PERCENTAGES FOR LARGE
                fcl_percent = fcs_percent + random.randrange(3,6)
                lcl_percent = lcs_percent + random.randrange(3,6)
                ocl_percent = 5
                #COSTING FOR SMALL
                fcs = (fcs_percent / 100) * p_sm
                lcs = (lcs_percent / 100) * p_sm
                ocs = (ocs_percent / 100) * p_sm
                profit_small = p_sm - (fcs+lcs+ocs)
                #COSTING FOR MEDIUM
                fcm = (fcm_percent / 100) * p_md
                lcm = (lcm_percent / 100) * p_md
                ocm = (ocm_percent / 100) * p_md
                profit_medium = p_md - (fcm + lcm + ocm)
                #COSTING FOR LARGE
                fcl = (fcl_percent / 100) * p_lg
                lcl = (lcl_percent / 100) * p_lg
                ocl = (ocl_percent / 100) * p_lg
                profit_large = p_lg - (fcl + lcl + ocl)

                #DishId DishName Category PriceSmall FoodCostSmall LabourCostSmall OverheadCostSmall       ---cont
                #PriceMedium FoodCostMedium LabourCostMedium OverheadCostMedium                            ---cont
                #PriceLarge FoodCostLarge LabourCostLarge OverheadCostLarge

                menu_list_ind.append(str(i+1))
                menu_list_ind.append(item)
                menu_list_ind.append(item_category)
                menu_list_ind.append(str(round(p_sm,2)))
                menu_list_ind.append(str(round(fcs,2)))
                menu_list_ind.append(str(round(lcs,2)))
                menu_list_ind.append(str(round(ocs,2)))
                menu_list_ind.append(str(round(p_md, 2)))
                menu_list_ind.append(str(round(fcm, 2)))
                menu_list_ind.append(str(round(lcm, 2)))
                menu_list_ind.append(str(round(ocm, 2)))
                menu_list_ind.append(str(round(p_lg, 2)))
                menu_list_ind.append(str(round(fcl, 2)))
                menu_list_ind.append(str(round(lcl, 2)))
                menu_list_ind.append(str(round(ocl, 2)))

                menu_list_all.append(menu_list_ind)

            with open('food_details.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
                for i in range(rows):
                    writer.writerow(menu_list_all[i])
                file.close()
            filepath='food_details.csv'
            return send_file(filepath,
                mimetype='text/csv',
                attachment_filename='food-details.csv',
                as_attachment=True)
            print('Successful!')
            #return jsonify('Successful')
    except Exception as e:
        return {"Error:":str(e)}

@app.route('/generate/order-details',methods =['GET','POST'])
def generateCusNFoodDetails():
    try:
        if request.method =='POST':
            rows=int(request.form['text3'])
            menu = menulist.food_list(int(rows))
            cust = customer1.customer_list(int(rows))
            ord = order2.order_list(menu, cust, int(rows))
            print(len(ord[0]))
            columns=['orderid','customerid','DishId','DishName','ordertype','Category','servicetype','subtotal','deliverycharge','gst','total','ets','sts','ots']
            with open('order_details.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
                for i in range(rows):
                    writer.writerow(ord[i])
                file.close()
            filepath='order_details.csv'
            return send_file(filepath,
                mimetype='text/csv',
                attachment_filename='order-details.csv',
                as_attachment=True)
            print('Successful!')
            #return send_file('order.csv',  as_attachment=True)
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

@app.route('/customerchart', methods=['GET'])
def vizualizeC():
    try:
        if request.method == 'GET':
            return send_file('vlz1.html')
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

@app.route('/highcharts', methods=['GET'])
def vizualizeC_Highcharts():
    try:
        if request.method == 'GET':
            d = {
                'name': 'Brands',
                'colorByPoint': True,
                'data': csvTOjson.func_C()
            }
            print(d)
            return jsonify(d)
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

@app.route('/orderchart', methods=['GET'])
def vizualizeO():
    try:
        if request.method == 'GET':
            return send_file('vlz2.html')
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)
#'YEARLY ORDERS'
@app.route('/highcharts2', methods=['GET'])
def vizualizeO_Highcharts():
    try:
        if request.method == 'GET':
            d = {
                'name': 'ORDER NUMBER',
                'colorByPoint': True,
                'data': csvTOjson.func_O()
            }

            return d
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)
#'DISH TYPE FREQUENCY'
@app.route('/highcharts3', methods=['GET'])
def vizualizeO2_Highcharts():
    try:
        if request.method == 'GET':
            d = {
                'name': 'DISH TYPE',
                'colorByPoint': True,
                'data': csvTOjson.func_O2()
            }

            return d
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

@app.route('/highcharts4', methods=['GET'])
def vizualize_Highcharts4():
    try:
        if request.method == 'GET':
            d = csvTOjson.func_O3()
            print(d)
            return jsonify(d)
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

@app.route('/menuchart', methods=['GET'])
def vizualize4():
    try:
        if request.method == 'GET':
            return send_file('vlz3.html')
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)


@app.route('/highcharts5', methods=['GET'])
def vizualizeM_Highcharts():
    try:
        if request.method == 'GET':
            d ={'data':csvTOjson.func_M()}
            print(d)
            return d
    except Exception as e:
        msg = {"message": str(e)}
        return jsonify(msg)

if __name__ == '__main__':
    app.debug=True
    app.run()
