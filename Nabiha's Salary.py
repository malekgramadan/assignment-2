action = "yes"
list = []
total_savings = 0

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
        savings += additional_savings # Add additional savings to total savings
        remaining -= additional_savings # Deduct additional savings from remaining salary
        total_savings += additional_savings  # Add to the total additional savings

    list.append([month, salary, savings, rent, electricity, total, remaining, yearly_cost, doubled_salary, additional_savings])
    action = input("Do you want to add another month? (yes/no): ")

for i in list: #Printing the user's data in a table
    print(f"{i[0]}'s salary is {i[1]}, you have {i[2]} savings.")
    print(f"You have spent {i[3]} on rent, and {i[4]} on electricity, for the total of {i[5]} with the savings.")
    print(f"You have {i[6]} remaining.")
    print(f"You would spend {i[7]} in total for rent and electricity.")
    print(f"If your salary was doubled it would be {i[8]}.")
    print(f"You have {i[9]} additional savings.")
    print(" ")
print(f"The total of saving from all months is {total_savings}") #Printing the total of all additional savings