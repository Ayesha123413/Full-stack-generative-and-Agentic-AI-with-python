users=[
    {"id":1 ,"total": 100 ,"coupon":"P10"},
    {"id":2 ,"total": 200 ,"coupon":"F10"},
    {"id":3 ,"total": 300 ,"coupon":"P30"},
]

discounts={
    "P10":(0.1,0) ,
     "F10":(0.2,0) ,
     "P30":(0,30)
     }


for user in users:
    percentage, fixed=discounts.get(user["coupon"],(0,0))
    discount= user["total"]*percentage + fixed
    print(f" User {user['id']} has a discount of {discount} with coupon {user['coupon']}")