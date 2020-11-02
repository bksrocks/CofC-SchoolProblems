# Name: Barbara Szwabowski
# working_time.py

# Purpose:

# Certification of Authenticity: I certify that this lab is entirely my
# own work.

# Input:

# Output:


def working_time():
    print("This program calculates the total amount of hours worked by "
          "employees of a company.")

    final_team_hours = []
    final_minutes, final_hours, final_days = 0, 0, 0
    number_teams = eval(input("Enter the number of teams in the "
                              "company: "))

    for k in range(number_teams):
        print("=========================================")
        print("                 Team", k+1)
        print("=========================================")

        team_minutes, team_hours, team_days = 0, 0, 0
        partial_hours_worked = []
        number_employees = eval(input("Enter the number of employees in"
                                      " the team: "))

        for i in range(number_employees):
            print("Employee", i+1)
            input_hours = int(input("Enter the amount of hours worked:"
                                    " "))
            input_minutes = int(input("Enter the amount of minutes"
                                      " worked: "))
            employee_minutes = input_minutes % 60
            employee_hours = input_hours + (input_minutes // 60)
            partial_hours_worked.append(i+1)
            partial_hours_worked.append(employee_hours)
            partial_hours_worked.append(employee_minutes)
            team_minutes = team_minutes + employee_minutes
            team_hours = team_hours + employee_hours

        team_hours = team_hours + (team_minutes // 60)
        team_minutes = team_minutes % 60
        final_team_hours.append(k+1)
        final_team_hours.append(team_hours)
        final_team_hours.append(team_minutes)

        final_minutes = final_minutes + team_minutes
        print(team_hours)
        print(final_hours)
        print(final_minutes)
        final_hours = (final_hours + team_hours) % 24
        print(final_hours)
        final_days = final_days + ((final_hours + team_hours) // 24)

        print("-----------------------------------------")
        for j in range(0, len(partial_hours_worked), 3):
            print("Employee ", partial_hours_worked[j], ": ",
                  partial_hours_worked[j+1], " hours, and ",
                  partial_hours_worked[j+2], " minutes.", sep="")
        print()

    print("===========================================================")

    for m in range(0, len(final_team_hours), 3):
        print("Total time team ", final_team_hours[m], ": ",
              final_team_hours[m+1], " hours, and ",
              final_team_hours[m+2], " minutes.", sep="")

    print("===========================================================")
    print("Total time of all teams: ", final_days, " days, ",
          final_hours, " hours, and ", final_minutes,
          " minutes.", sep="")
    print("===========================================================")

def main():
    working_time()

main()
