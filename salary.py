salary = 3800000
hourlyOvertimeRate = 110000

numberOfOvertime = (input("Enter the number of overtime: "))
while (numberOfOvertime.isalpha()) or not (float(numberOfOvertime) <= 20 and float(numberOfOvertime) >= 0):
        print(f"Please enter a number in range of 0 and 20")
        numberOfOvertime = (input("Enter the number of overtime: "))
numberOfOvertime = float(numberOfOvertime)

levelOfAllowance = (input("Enter level of allowance: "))
while levelOfAllowance not in ["1","2","3"]:
        print(f"Enter level of allowance (1 to 3)")
        levelOfAllowance = (input("Enter level of allowance: "))
levelOfAllowance = int(levelOfAllowance)

if levelOfAllowance == 1:
        salary += numberOfOvertime * hourlyOvertimeRate
        salary += 3800000 * 0.05
        print("-----------------------------------------")
        print(f"The Total Salary is: {int(salary)}")

elif levelOfAllowance == 2:
        salary += numberOfOvertime * hourlyOvertimeRate
        salary += 3800000 * 0.1
        print("-----------------------------------------")
        print(f"The Total Salary is: {int(salary)}")

elif levelOfAllowance == 3:
        salary += numberOfOvertime * hourlyOvertimeRate
        salary += 3800000 * 0.15
        print("-----------------------------------------")
        print(f"The Total Salary is: {int(salary)}")



