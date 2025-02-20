action = "yes"
list = []

while action != "no":
    salary = float(input("Enter your salary: "))
    month = str(input("Enter the month: "))
    savings_percent = float(input("Enter the percentage of salary you want to save: "))
    rent_percent = float(input("Enter the percentage of salary you want to spend on rent: "))
    electricity_percent = float(input("Enter the percentage of salary you want to spend on electricity: "))
        
    savings = (savings_percent / 100) * salary
    rent = (rent_percent / 100) * salary
    electricity = (electricity_percent / 100) * salary
    total = savings + rent + electricity
        
    list.append([month, salary, savings, rent, electricity, total])
    action = input("Do you want to add another month? (yes/no): ")
print(list)