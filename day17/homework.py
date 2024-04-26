
# num = []
# for i in range(5):
#     num1 = int(input("enter number:"))
#     num.append(num1)

# num2 = 0
# for num3 in num:
#     num2 += num3
# print(num2)


# num = []
# for i in range(10):
#     num2 = int(input("enter number:"))
#     num.append(num2)

# num3 = num[0]
# for num4 in num:
#     if num4 > num3:
#         num3=num4
# print(num3)





# numbers = list(range(30,51))
# odd = 0
# for num in numbers:
#     if num % 2 !=0:
#         odd += 1
# print(odd)




#list1 =list(range(10,51,4))
#print(list1)




# for num in range(50,101,2):
#     print(f"{num} - {(num - 50) // 2}", end=", ")




num_odd = []
num_even = []

num_in_middle = "please enter number"
num_in_middle = num_odd , num_even
for num in range(1,10+1):
    if num %2 == 0:
        num_odd.append(num_even)
    else:
        num_even.append(num_odd)
print(num_odd , num_even)
