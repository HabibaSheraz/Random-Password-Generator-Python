import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols=['!', '@', '#', '$', '%', '&', '*', '_', '+']
print("Welcome to Pypassword Generator!")

nr_letters=int(input("How many letters would you like in your password\n"))
nr_symbols=int(input("How many symbols would you like in your password\n"))
nr_numbers=int(input("How many numbers would you like in your password\n"))
password=[]

for i in range(1,nr_letters+1):
    selected_letters=random.choice(letters)
    password+=selected_letters 
for i in range(1, nr_symbols+1):
    selected_symbols=random.choice(symbols) 
    password+=selected_symbols  
for i in range(1,nr_numbers+1):
    selected_numbers=random.choice(numbers)
    password+=str(selected_numbers)
    random.shuffle(password)
    pass_string=''.join(password)
print(f"\nPassword generated for you is {pass_string}")    
#random1=[selected_letters,selected_numbers,selected_symbols]
#for i in range(0,3):
   # password=random.choice(random1)
   # print(password)

