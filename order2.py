import random
from datetime import datetime
from datetime import timedelta
from randomtimestamp import randomtimestamp

def order_list(menu,cust,nor):

    # customerid,name,gender,age,phone,email,addrs
    # DishId DishName Category PriceSmall FoodCostSmall LabourCostSmall OverheadCostSmall       ---cont
    # PriceMedium FoodCostMedium LabourCostMedium OverheadCostMedium                            ---cont
    # PriceLarge FoodCostLarge LabourCostLarge OverheadCostLarge
    #REQUIRED
    # orderid,customerid,DishId,DishName,ordertype,Category,servicetype,subtotal,deliverycharge,gst,total,ets,sts,ots

    services = [['Home Delivery', 0.05], ['Self Pickup', 0]]

    tax = 0.05
    order_all = []
    for i in range(nor):
        order_ind = []
        menu_picker = random.randrange(0, len(menu))
        cust_picker = random.randrange(0, len(cust))
        services_picker = random.randrange(0, len(services))
        ordertype_picker = random.randrange(0,3)

        orderid = i+1
        customerid = cust[cust_picker][0]
        dishid = menu[menu_picker][0]
        dishname = menu[menu_picker][1]
        ordertype = [['Small',menu[menu_picker][3]],['Medium',menu[menu_picker][7]],['Large',menu[menu_picker][11]]]
        otype = ordertype[ordertype_picker][0]
        category = menu[menu_picker][2]
        servicetype = services[services_picker][0]
        subtotal = float(ordertype[ordertype_picker][1])
        delivery_charge = subtotal*services[services_picker][1]
        gst = subtotal * tax
        total = subtotal + delivery_charge + gst
        #ots = datetime.now()
        ots = randomtimestamp()
        ots = datetime.strptime(ots, '%d-%m-%Y %H:%M:%S')
        ets = ots + timedelta(minutes=random.randrange(15,30))
        sts = ets + timedelta(minutes=random.randrange(10,20))
        order_ind.append(str(orderid))
        order_ind.append(str(customerid))
        order_ind.append(str(dishid))
        order_ind.append(str(dishname))
        order_ind.append(str(otype))
        order_ind.append(str(category))
        order_ind.append(str(servicetype))
        order_ind.append(str(subtotal))
        order_ind.append(str(round(delivery_charge)))
        order_ind.append(str(round(gst,2)))
        order_ind.append(str(total))
        order_ind.append(str(ots))
        order_ind.append(str(ets))
        order_ind.append(str(sts))

        order_all.append(order_ind)

    return order_all

'''SAYANTAN CHATTERJEE'''