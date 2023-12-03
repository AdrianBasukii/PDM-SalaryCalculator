userData = {}
salary = 3800000
hourlyOvertimeRate = 110000

while True: 
    numberOfOvertime = int(input("Enter the number of overtime (max: 20): "))
    if numberOfOvertime <= 20 and numberOfOvertime >= 0:
        levelOfAllowance = int(input("Enter level of allowance (1 to 3): "))
        if levelOfAllowance == 1:
            salary += numberOfOvertime * hourlyOvertimeRate
            salary += 3800000 * 0.05
            print(f"The Total Salary is: {int(salary)}")
            break


        elif levelOfAllowance == 2:
            salary += numberOfOvertime * hourlyOvertimeRate
            salary += 3800000 * 0.1
            print(f"The Total Salary is: {int(salary)}")
            break


        elif levelOfAllowance == 3:
            salary += numberOfOvertime * hourlyOvertimeRate
            salary += 3800000 * 0.15
            print(f"The Total Salary is: {int(salary)}")
            break


        else:
            print("Invalid level of allowance")

    else:
        print("Invalid overtime number")