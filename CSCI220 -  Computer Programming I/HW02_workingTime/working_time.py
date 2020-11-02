# Name: Barbara Szwabowski
# working_time.py

# Purpose: Calculate the total time worked in a company, in minutes,
# hours and days and output the numbers in the correct formats
# (60 minutes/24 hours)

# Certification of Authenticity: I certify that this lab is entirely my
# own work but I discussed it with Dr. Kebin Xu.

# Input: Number of teams in a company, number of employees in each team
# and the hours and minutes worked by each employee.

# Output: 1 - Total minutes and hours worked by the employees in a team
# 2 - Total minutes and hours worked by each team in a company
# 3 - Total minutes, hours, and days worked in a company

def working_time():
    print("This program calculates the total amount of hours worked by "
          "employees of a company.")

    # Initiates variables and list that will contain accumulated values
    total_company = []
    partial_minutes, partial_hours = 0, 0

    # Asks user for input on number of teams in the company
    number_teams = eval(input("Enter the number of teams in the "
                              "company: "))
    print()

    for team in range(number_teams):
        print("========================================================"
              "===")
        print("                          Team", team+1)
        print("========================================================"
              "===")

        # Initiates lists and variables that will store temporary values
        partial_employees =[]
        partial_team = []
        team_minutes, team_hours, team_days = 0, 0, 0

        # Asks user for input on number of employees in each team
        number_employees = eval(input("Enter the number of employees in"
                                      " the team: "))

        for employee in range(number_employees):
            print("Employee", employee+1)

            # Asks user for the number of hours and minutes worked by
            # the employees in the team
            input_hours = int(input("Enter the amount of hours worked:"
                                    " "))
            input_minutes = int(input("Enter the amount of minutes"
                                      " worked: "))

            # Calculates the employee's total of minutes and hours
            employee_minutes = input_minutes % 60
            employee_hours = input_hours + (input_minutes // 60)

            # Add values to a temporary list
            partial_employees.append(employee+1)
            partial_employees.append(employee_hours)
            partial_employees.append(employee_minutes)

            # Assign employee's hours and minutes to a temporary
            # variable
            team_hours += employee_hours
            team_minutes += employee_minutes

        # Calculates the total of minutes and hours in the team
        team_hours += (team_minutes // 60)
        team_minutes = team_minutes % 60

        # Add values to a temporary list
        partial_team.append(team+1)
        partial_team.append(team_hours)
        partial_team.append(team_minutes)

        # Transfer values from temporary lists to accumulated list
        total_company.append(partial_employees)
        total_company.append(partial_team)

        # Assign team's hours and minutes to temporary variables
        partial_minutes += team_minutes
        partial_hours += team_hours

        print("--------------------------------------------------------"
              "---")
        print()

    # Computes total values for company minutes, hours and days
    company_minutes = partial_minutes % 60
    company_hours = ((partial_minutes // 60) + partial_hours) % 24
    company_days = ((partial_minutes // 60) + partial_hours) // 24

    print("===========================================================")

    for i in range(0, len(total_company), 2):
        # Assign values in accumulated list to variables
        output_employees = total_company[i]
        output_team = total_company[i+1]
        print("Team", output_team[0])

        for j in range(0, len(output_employees), 3):
            # Outputs hours for each employee in a team
            print("Employee ", output_employees[j], ": ",
                  output_employees[j+1], " hours, and ",
                  output_employees[j+2], " minutes.", sep="")
        # Outputs hours for each team in the company
        print("Total hours time team ", output_team[0], ": ",
              output_team[1], " hours, and ",
              output_team[2], " minutes.", sep="")
        print("--------------------------------------------------------"
              "---")
    # Outputs total hours for the company
    print("Total time of all teams: ", company_days, " days, ",
          company_hours, " hours, and ", company_minutes,
          " minutes.", sep="")
    print("===========================================================")


def main():
    working_time()


main()
