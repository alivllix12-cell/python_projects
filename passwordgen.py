print("##############Password generator##############")
import secrets 
import string
string.ascii_letters
string.digits
string.punctuation
how_long=int(input("how long u want the password be :  "))
include=input("what do u want the password include : letters/numbers/symboles/all = ")
if include == "letters":
    characters=string.ascii_letters
if include== "nummbers":
    characters=string.digits
if include =="symboles":
    characters=string.punctuation
if include == "all":
    characters= string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(how_long):
 password+=secrets.choice(characters)
print(password)