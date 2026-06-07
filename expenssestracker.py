print("=====expensses CSV tracker=====")
from pathlib import Path 
file_track=Path("track.csv")
import csv

while True :
     user_choices=[1,2,3,4]
     choice=input("Enter 1 : for add expenses| 2 : for view All Expenses | 3 : for Total Spending | 4 : Exit = ")
     if choice=="1":
      date=input("What date was this expense? ")
      category=input("what category? ")
      amount=float(input("How much did it cost?"))
      with open("track.csv","a") as csv_file :   
        csv_writer=csv.writer(csv_file)
        csv_writer.writerow([date, category, amount])
        csv_file.close()
      
     elif choice=="2": 
         with open("track.csv","r") as csv_file:
           csv_reader=csv.reader(csv_file)
           for row in csv_reader:
              print(row)
     elif choice =="3":
        total=0
        with open ("track.csv","r") as csv_file:
           total_csv=csv.reader(csv_file)
           for row in total_csv:
             if row:
              row[2] =float(row[2])
              total+= row[2]
        print(f"total spending is {total}\n")
     elif choice =="4":
       break