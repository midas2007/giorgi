def numbers_product(start, end, step):
    multiples_of_3 = []
    
    product = 1
    
    current_number = start
    
    while current_number <= end:
        if current_number % 3 == 0:
            multiples_of_3.append(current_number)
        current_number += step
    
    for num in multiples_of_3:
        product *= num
    
    return product

start = 1
end = 20
step = 1
print(numbers_product(start, end, step))  # Output will be the product of multiples of 3 within the range
