# create a single list that has all the data in the order given
data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# separate the mixed data into three clean lists for IDs, names, and pay rates
employee_numbers = []
employee_names = []
employee_salaries = []

for item in data:
    if type(item) == int:
        if item not in employee_numbers:
            employee_numbers.append(item)
    elif type(item) == str:
        if item not in employee_names:
            employee_names.append(item)
    elif type(item) == float:
        if item not in employee_salaries:
            employee_salaries.append(item)

# now multiply each salary by 1.3 to account for benefits and make a list called total_hourly_rate
total_hourly_rate = []
for rate in employee_salaries:
    total_hourly_rate.append(round(rate * 1.3, 2))

# check for any total hourly rate that goes over 37.30 and print a warning
for rate in total_hourly_rate:
    if rate > 37.30:
        print("Warning:", rate, "may be a budget concern due to high total hourly rate.")

# find the highest total hourly rate for reference
max_total_rate = max(total_hourly_rate)
print("\nHighest total hourly rate:", max_total_rate)

# make a list of employees whose total hourly rate is between 28.15 and 30.65
underpaid_salaries = []
for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid salaries (between 28.15 and 30.65):", underpaid_salaries)

# calculate pay raises based on original unmodified hourly rate list
company_raises = []
for rate in employee_salaries:
    if 22 <= rate < 24:
        raise_amt = round(rate * 1.05, 2)
    elif 24 <= rate < 26:
        raise_amt = round(rate * 1.04, 2)
    elif 26 <= rate < 28:
        raise_amt = round(rate * 1.03, 2)
    else:
        raise_amt = round(rate * 1.02, 2)
    company_raises.append(raise_amt)

print("\nCalculated company raises based on salary ranges:", company_raises)

# design a custom complex condition with at least four truth tests
# this checks if the employee is highly paid, their ID is above 1130, they’re not underpaid, and they got less than a 4% raise
for i in range(len(employee_salaries)):
    salary = employee_salaries[i]
    emp_id = employee_numbers[i % len(employee_numbers)]
    total = total_hourly_rate[i]
    raise_val = company_raises[i]
    
    # checking all conditions at once
    if (salary > 25 and emp_id > 1130 and total > 30 and raise_val < salary * 1.04):
        print("\nComplex Condition: Employee", emp_id, "(", employee_names[i % len(employee_names)], ") meets all criteria.")
    else:
        pass

# final check printout of lists for verification
print("\nEmployee Numbers:", employee_numbers)
print("Employee Names:", employee_names)
print("Employee Salaries:", employee_salaries)
