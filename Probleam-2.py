#With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
# function base serise 
def generate_serise(num):
    serise_pattern = []
    for n in range(1, num+1):
        serise_pattern.append(2 * n -1)
    return serise_pattern

result = generate_serise(3)
# it printing list 
print(result)

# second approch 
a = int(input("Enter a number: "))

for n in range(1, a + 1):
    print(2 * n - 1, end=", " if n < a else "")
