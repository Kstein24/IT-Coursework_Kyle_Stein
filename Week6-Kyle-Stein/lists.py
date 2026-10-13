# creating a list of courses I've taken at Walsh 
courses = ["it 407", "it 462", "it 463", "com 405", "acc 201"]

# sort the list and print each course in uppercase with message
courses.sort()
for course in courses:
    print("I have taken", course.upper(), "at Walsh College.")

# add new courses I plan to take next term
print("\nThis is my course of study with upcoming courses added:")
courses.extend(["it 480", "cyb 490"])
courses.sort()
for course in courses:
    print(course)

# remove the courses already taken and print them
taken_courses = ["it 407", "it 462", "it 463", "com 405", "acc 201"]
print("\nI do not have to take these courses:")
for course in taken_courses:
    if course in courses:
        print(course)
        courses.remove(course)

# print courses I still plan to take next term
print("\nI plan to take the following courses next term:")
for course in courses:
    print(course)

# create list of numbers 1 to 1000 divisible by 6
divisible_by_6 = []
for num in range(1, 1001):
    if num % 6 == 0:
        divisible_by_6.append(num)

# print first 20 numbers divisible by 6
print("\nHere are twenty numbers divisible by 6:")
for i in range(20):
    print(divisible_by_6[i])

# find and store the maximum number
max_num = max(divisible_by_6)
print("\nThe maximum value in the list is:", max_num)

# find and store the sum of values from 10th to 50th in the list
sum_values = sum(divisible_by_6[9:50])
print("\nHere is the sum of several values in the list:", sum_values)

# overwrite the courses variable with the large list
courses = divisible_by_6
