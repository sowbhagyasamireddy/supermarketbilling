from datetime import datetime
name=input("enter your name")

list = '''''
rice    Rs  20/kg
dal     Rs  30/kg
salt    Rs  20/kg
maggie  Rs  50/kg
boost   Rs  90/each
oil     Rs  80/liter
cashew  Rs  110/kg
colgate Rs  85/each

'''''
price = 0
pricelist = []
totalprice=0
finalprice=0
item_list=[]
quantity_list=[]
price_list=[]
items={'rice':20,'dal':30,'salt':20,'maggie':50,'boost':90,'oil':80,'cashew':110,'colgate':85}
option = int(input("list of items enter 1:-"))
if option ==1:
    print(list)
for i in range(len(items)):
    input1=int(input("if you want to buy enter 1 or 2 for exit:-"))
    if input1==2:
        print("thank you")
        break
    if input1==1:
        item=input("enter your items:-")
        quantity=int(input("enter quantity:-"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            item_list.append(item)
            price_list.append(price)
            quantity_list.append(quantity)
            gst=((totalprice*5)/100)
            finalamount=gst+totalprice
        else:
            print("entered item is not there")
    else:
        print("you entered wrong number")
    inp=(input("can i bill the items yes or no:"))
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","mayabazar",25*"=")
            print(28*" ","vizag")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',item_list[i],3*',',quantity_list[i],8*" ",price_list[i])
                print(75*"-")
                print(50*"-",'TotalAmount:','Rs',totalprice)
                print("gstAmount:",40*" ",'Rs',gst)
                print(75*"-")
                print(50*"-",'finallAmount:','Rs',finalamount)
                print(75*"-")
                print(20*"-","Thanks for visiting")
                print(75*"-")
        