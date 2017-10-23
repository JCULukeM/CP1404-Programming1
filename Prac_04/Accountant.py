"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_income_report(num_months,list_incomes):

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = list_incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def main():
    """Display income report for incomes over a given number of months."""
    list_incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        list_incomes.append(income)

    print_income_report(num_months,list_incomes)



main()