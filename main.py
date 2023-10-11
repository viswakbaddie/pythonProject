import random
import math
import mysql.connector as mysql
from geopy import distance
con = mysql.connect(host='localhost', password='password', database = 'flight_game', user='root')
cursor = con.cursor()

def random_dice():
    x = random.randint(1, 6)
    return x
def user_dice(x):
    y = random.randint(1,x)
    return y
def convert(gallon):
    litre = gallon * 3.785
    return litre
def sum_list(l):
    sum = 0
    for i in l:
        sum = sum+i
    return sum
def odd(l):
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
    return even
def unit_price(diameter,price):
    area = math.pi*(diameter/2)*(diameter/2)
    unit_price=price/area
    return unit_price


while True:
    choice = float(input('enter question number'))
    if choice == 6.1:
        while True:
            dice = random_dice()
            if dice == 6:
                break
            else:
                print(dice)

    if choice == 6.2:
        side = int(input('enter max number on dice'))
        while True:
            roll = user_dice(side)
            if roll == side:
                break
            else:
                print(roll)
    if choice == 6.3:
        while True:
            gallon = float(input('enter gallon'))
            if gallon>0:
                print(convert(gallon))
            else:
                break
    if choice == 6.4:
        list = eval(input('enter list of integrers'))
        print(sum_list(list))
    if choice == 6.5:
        list1 = eval(input('enter list of integers'))
        print(list1)
        print(odd(list1))
    if choice == 6.6:
        diameter1=int(input('enter diameter of first pizza'))
        diameter2=int(input('enter diameter of second pizza'))
        price1=int(input('enter price of first pizza'))
        price2=int(input('enter price of second pizza'))
        print(unit_price(diameter1,price1),unit_price(diameter2,price2))
        if unit_price(diameter1,price1)>unit_price(diameter2,price2):
            print('pizza 2 is cheaper')
        else:
            print('pizza one is cheaper')
    if choice == 7.1:
        tuple1 = ('spring', 'summer', 'autumn', 'winter')
        no = int(input('enter number of the month'))
        if no<4:
            print(tuple1[3])
        elif 3 < no < 7:
            print(tuple1[0])
        elif 6 < no < 10:
            print(tuple1[1])
        elif 9 < no < 13:
            print(tuple1[2])
        else:
            print('invalid input')
    if choice==7.2:
        s = set()
        while True:

            name=input('enter name')
            if name=='':
                break
            elif name in s:
                print('Already exist')
            else:
                print('new user')
                s.add(name)
        for i in s:
            print(i)

    if choice == 7.3:
        d={}
        while True:
            opt = int(input('1.enter new airport \n2.fetch info about airport \n3.quit'))
            if opt==1:
                ICAO = input('enter ICAO code')
                airport = input('enter name of airport')
                d[ICAO]=airport
            elif opt==2:
                ICAO = input('enter ICAO code')
                print('airport name:',d[ICAO])
            elif opt == 3:
                break
            else:
                print('invalid output')
    if choice == 8.1:
        ICAO = input('enter icao code of airport')
        querry = "select name,latitude_deg,longitude_deg from airport where ident='{}'".format(ICAO)
        cursor.execute(querry)
        d = cursor.fetchone()
        print('airport name:', d[0], 'location:', d[1], d[2])
    if choice == 8.2:
        a,b,c,x,e,g,j = 0,0,0,0,0,0,0
        code = input('enter area code')
        querry = "select name,type from airport where iso_country = '{}' order by type;".format(code)

        cursor.execute(querry)
        d=cursor.fetchall()
        for i in d:

            if i[1]=='heliport':
                a=a+1
            if i[1]=='small_airport':
                b=b+1
            if i[1]=='closed':
                c=c+1
            if i[1]=='seaplane_base':
                x=x+1
            if i[1]=='balloonport':
                e=e+1
            if i[1]=='medium_airport':
                g=g+1
            if i[1]=='large_airport':
                j=j+1

        print('heliport:',a)
        print('small_airport:',b)
        print('closed',c)
        print('seaplane_base',x)
        print('ballonprt:',e)
        print('medium_airport:',g)
        print('large_airport',j)

    if choice == 8.3:
        ICAO1 = input('enter 1st ICAO code')
        ICAO2 = input('enter 2nd ICAO code')
        querry = "select latitude_deg,longitude_deg from airport where ident='{}'".format(ICAO1)
        cursor.execute(querry)
        a=cursor.fetchone()
        querry1="select latitude_deg,longitude_deg from airport where ident='{}'".format(ICAO2)
        cursor.execute(querry1)
        b=cursor.fetchone()
        loc1 = (a[0],a[1])
        loc2 = (b[0],b[1])
        print(distance.distance(loc1, loc2).miles)








































