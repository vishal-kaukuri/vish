import pandas as pd
import numpy as np
seats_booked=[]
rows=int(input('Enter the number of rows : '))
cols=int(input('Enter the number of columns : '))
name_l = []
sex_l = []
age_l = []
Phone = []
dict={'row':[],'col':[]}
def buy(): 
    dict['row'] = int(input("enter row number :"))
    dict['col'] = int(input("enter column number :"))
    if rows*cols <60:
        print("Ticket price is $10")
    elif r <= rows//2:
        print("Ticket price is $10")
    elif r >= rows//2:
        print("Ticket price is $8")
    print("want to Book...?")
    l = {
        "1": "yes", 
        "2": "no"}
    print(l)
    choice = int(input("choose your option: ")) 
    
    if choice == 1:
        name = str(input("\nName : "))
        name_l.append(name)
        age  = int(input("\nAge  : "))
        age_l.append(age)
        sex  = str(input("\nGender : "))
        sex_l.append(sex)
        ph  = int(input("\nPhone No : "))
        Phone.append(ph)
        print("Booked Successfully")
        main()
    elif choice == 2:
        main()
      

def stats():
    a=len(seats_booked)
    print("Number of Purchased Tickets:",a)
    print("Percentage of Tickets Booked:",round(a/(rows*cols)*100,2),"%") 
     
    print("Current Income","$",a*10)
    
    print("Total Income : $",(rows//2*10)+((rows-(rows//2))*8))
    main()

def seats(): 
    print("Cinema:")
    df=pd.DataFrame(data='S', index=range(1,rows+1), columns=range(1,cols+1))
    data1=df.at[dict['row'],dict['col']]
    seats_booked.append(data1)
    if data1 in seats_booked:
        df.at[dict['row'],dict['col']]='B'
        print(df)
    else:
        print(pd.DataFrame(data='S', index=range(1,rows+1), columns=range(1,cols+1)))
        print("All Seats Vacant")

def booked_details():
    list(map(lambda seats_booked,name_1 : seats_booked[i] == name_1[i] for i in range(len(seats_booked))))
    list(map(lambda name_1,sex_1 : name_1[i] == sex_1[i] for i in range(len(name_1))))
    list(map(lambda sex_1,age_1 : sex_1[i] == age_1[i] for i in range(len(sex_1))))
    list(map(lambda age_1,Phone : age_1[i] == Phone_1[i] for i in range(len(name_1))))
    for j in range(len(seats_booked)):
        print(name_1[j])
        print(sex_1[j])
        print(age_1[j])
        print(Phone[j])


def main():
    print("1.Show the seats") 
    print("2.Buy a Ticket ") 
    print("3.Statistics") 
    print("4.Show booked Tickets User info") 
    print("0 Exit \n")
    query = int(input("choose your option: ")) 
    if query == 1:
            seats() 
    elif query == 2: 
            buy() 
    elif query == 3: 
            stats() 
    elif query == 4: 
            booked_details()
    else:
            exit()
    

main() 
