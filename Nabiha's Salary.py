action = "yes"
list = []

while action.lower() != "no": #Making sure that the user can add as many months as they want all sorted in a list
    salary = float(input("Enter your salary: "))
    month = str(input("Enter the month: "))
    savings_percent = float(input("Enter the percentage of salary you want to save: "))
    rent_percent = float(input("Enter the percentage of salary you want to spend on rent: "))
    electricity_percent = float(input("Enter the percentage of salary you want to spend on electricity: "))
    add_savings = input("Do you have any additional savings? (yes/no): ")

    savings = (savings_percent / 100) * salary #Calculating the amount saved
    rent = (rent_percent / 100) * salary #Calculating the amount spent on rent
    electricity = (electricity_percent / 100) * salary #Calculating the amount spent on electricity
    total = savings + rent + electricity #Calculating the total amount spent on rent, electricity, and savings
    remaining = salary - total #Calculating the remaining amount after spending on rent, electricity, and savings
    yearly_cost = (rent + electricity) * 12 #What the user spends in a year for electricity and rent
    doubled_salary = salary * 2 #the fun part
    
    if add_savings.lower() == "yes":
        additional_savings = float(input("Enter the amount of additional savings: "))
        savings += additional_savings

    list.append([month, salary, savings, rent, electricity, total])#Adding the month, salary, savings, rent, electricity, and total to the list
    action = input("Do you want to add another month? (yes/no): ")
print(f"You have {savings} in savings.")
print(f"You have spent {rent} on rent.")
print(f"You have spent {electricity} on electricity.")
print(f"You have spent {total} in total.")
print(f"You have {remaining} remaining.")
print(f"You have spent {yearly_cost} in total for rent and electricity.")
print(f"Your salary doubled is {doubled_salary}.")
print(f"You added {additional_savings} to your savings.")