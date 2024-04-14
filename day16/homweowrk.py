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





#cars = ["Mercedes","BMW","Nissan","porsche"
#,"lamborghini","pagani zonda","Tesla","jiguli"]

#print(len(cars))

# Initialize an empty list to store the numbers



numbers = []


for i in range(10):
    number = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(number)

first_index_sum = numbers[0]
last_index_sum = numbers[-1]

print("Sum of the element at the first index:", first_index_sum)
print("Sum of the element at the last index:", last_index_sum)
