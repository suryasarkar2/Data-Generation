from faker import Faker
import random

def customer_list(nor):
    fake = Faker(['en-US'])

    cust_al = []

    gender = ['Male','Female','Others']

    for i in range(nor):
        gender_picker = random.randrange(len(gender))
        cust_ind = []
        # print('EMAIL {} - ADDRESS {} - NAME {} - GENDER {} - AGE {} - PHONE_NUMBER {}'.format(fake.email(),fake.address(),fake.name_female(), "Female",random.randrange(18,90),fake.phone_number()))
        #customerid,name,gender,age,phone,email,addrs
        cust_ind.append(str(i+1))
        cust_ind.append(fake.name())
        cust_ind.append(gender[gender_picker])
        cust_ind.append(random.randrange(18, 90))
        cust_ind.append(fake.phone_number().replace('x', '0'))
        cust_ind.append(fake.email())
        cust_ind.append(fake.address().replace('\\n', ''))

        cust_al.append(cust_ind)

    return cust_al


'''SAYANTAN CHATTERJEE'''


