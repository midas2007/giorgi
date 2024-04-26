#favourite_films = ["home alone","super natural","creed","the mist","kung fu panda"]
#print(favourite_films[1])



#footballer = ["footballer: " "Messi","iniesta","suarez","neymar","yamal"]
#basketballer =["basketballer: " " michael jordan",
#"jason williams","step curry",
#"shaqquile o'neal","kobe bryant"]

#print(footballer, ",",basketballer)




#name = "giorgi"


#first_character = name[0]
#last_character = name[5]

#print("First character:", first_character)
#print("Last character:", last_character)















































#მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ 
#სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.

# num = []
# for i in range(5):
#     num1 = int(input("enter number:"))
#     num.append(num1)

# num2 = 0
# for num3 in num:
#     num2 += num3
# print(num2)

#სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ
# სიაში არსებული ყველაზე დიდი რიცხვი, მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.

# num = []
# for i in range(10):
#     num2 = int(input("enter number:"))
#     num.append(num2)

# num3 = num[0]
# for num4 in num:
#     if num4 > num3:
#         num3=num4
# print(num3)


#სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი.
# შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.



# numbers = list(range(30,51))
# odd = 0
# for num in numbers:
#     if num % 2 !=0:
#         odd += 1
# print(odd)



#სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები.
# შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

#list1 =list(range(10,51,4))
#print(list1)


#თქვენი დავალებაა, რომ სიაში შეიტანოთ 50-იდან 100-მდე არსებული ყველა რიცხვი.
# შემდეგ გამოიყენეთ for ციკლი და დაბეჭდეთ ყველა ლუწი რიცხვი  მათი ინდექსებით.
# test case: ["50 - 0", "52 - 3", "54 - 5", "56 - 7"]


#for num in range(50,101,2):
    #print(f"{num} - {(num - 50) // 2}", end=", ")








#cars = ["Mercedes","BMW","Nissan","porsche"
#,"lamborghini","pagani zonda","Tesla","jiguli"]

#print(len(cars))

# Initialize an empty list to store the numbers



# numbers = []


# for i in range(10):
#     number = float(input("Enter number {}: ".format(i + 1)))
#     numbers.append(number)

# first_index_sum = numbers[0]
# last_index_sum = numbers[-1]

print("Sum of the element at the first index:", first_index_sum)
print("Sum of the element at the last index:", last_index_sum)










































#მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ 
#სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.

# num = []
# for i in range(5):
#     num1 = int(input("enter number:"))
#     num.append(num1)

# num2 = 0
# for num3 in num:
#     num2 += num3
# print(num2)

#სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ
# სიაში არსებული ყველაზე დიდი რიცხვი, მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.

# num = []
# for i in range(10):
#     num2 = int(input("enter number:"))
#     num.append(num2)

# num3 = num[0]
# for num4 in num:
#     if num4 > num3:
#         num3=num4
# print(num3)


#სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი.
# შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.



# numbers = list(range(30,51))
# odd = 0
# for num in numbers:
#     if num % 2 !=0:
#         odd += 1
# print(odd)



#სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები.
# შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

#list1 =list(range(10,51,4))
#print(list1)


#თქვენი დავალებაა, რომ სიაში შეიტანოთ 50-იდან 100-მდე არსებული ყველა რიცხვი.
# შემდეგ გამოიყენეთ for ციკლი და დაბეჭდეთ ყველა ლუწი რიცხვი  მათი ინდექსებით.
# test case: ["50 - 0", "52 - 3", "54 - 5", "56 - 7"]


for num in range(50,101,2):
    print(f"{num} - {(num - 50) // 2}", end=", ")
