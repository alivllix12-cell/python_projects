print("=======contact book=======")
from pathlib import Path
file_contact=Path("contact.json")
import json

while True:
     choice=input("1=Add contact: |2=view all contacts : | 3=search a contact : |4=delete a contact: |5=exit: ")
     if choice=="1":
      name_nickname=input("Enter your full name: ")
      company=input("Enter your company: ")
      adress=input("Enter your adress: ")
      phone=int(input("Enter yout phone numbers: "))
      with open("contact.json","r") as json_file:
         json_wr=json.load(json_file)
         json_wr.append({"name": name_nickname, "company": company, "address": adress, "phone": phone})
      with open("contact.json" , "w") as json_file:
        json.dump(json_wr,json_file)
     if choice=="2":
        with open("contact.json","r") as json_file:
          contacts= json.load(json_file)
          print(contacts)
     if choice =="3":
        with open("contact.json","r") as file:
          search_input=input("what name are u searching for: ")
          contacts=json.load(file)
          for contact in contacts:
             if contact["name"] == search_input:
                print(contact)
                
     if choice == "4":
        with open("contact.json","r") as file:
          delete_input=input("what name u want to remove? ")
          delete=json.load(file)
          for contact in delete:
             if contact["name"]== delete_input:
                delete.remove(contact)
                with open ("contact.json", "w") as file:
                   json.dump(delete, file)
                   print(f"your {delete_input} is deleted")
     if choice=="5":
        break
               