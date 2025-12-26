# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {}

for k in range(1, 10): #given_list = [1,2,3,4,5,6,7,8,9]
    count = 0
    for num in numbers:
        if num % k == 0:
            count += 1
    result[k] = count

print(result)

