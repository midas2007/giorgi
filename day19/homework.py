my_list = [1,2,3]
result = 1
for element in my_list:
    result *= element
print("სიაში ყველა ელემენტის ნამრავლია", result)

numbers = [-1,-2,-3,-4,-5,-6,-7,-8,-9]

negative_numbers = []
for num in numbers:
     if num < 0:
          negative_numbers.append(num)
print("negative numbers", negative_numbers)

numbers = [10,20,30,40,50]
total = sum(numbers)
avarge = total / len(numbers)
print("სიაში ჩაწერილი რიცხვების საშუალო არითმეტიკული არის:", avarge)
list1 = [1,2,3]
list2 = [4,5,6]
combined_list = list1 + list2
print("ორ რიცხვთა სიები ერთ სიაში", combined_list)
numbers = [1,2,3,4,5,6,7]
unique_numbers = list(set(numbers))
print(unique_numbers)




