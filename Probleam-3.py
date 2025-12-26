# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
a = int(input("Enter a number: "))

if a % 2 == 0:
    a = a - 1
    
result = []
for n in range(1, a + 1):
    result.append(2 * n - 1)

print(", ".join(map(str, result)))
