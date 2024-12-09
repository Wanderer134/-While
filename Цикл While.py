numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
index = 0
while index < len(numbers):
    if numbers[index] > 0:
        positive_numbers.append(numbers[index])
    elif numbers[index] < 0:
        break
    index += 1
print(positive_numbers)
