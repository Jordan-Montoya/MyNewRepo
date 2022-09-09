#Variables

name = input("Name? ")
wage = input("hourly? ")
hours = input("hours per day worked? ")
days = input("days per week worked? ")
weekly = float(days) * float(hours) * float(wage)
biweekly = float(weekly) * 2
gross = float(biweekly) * 24

if (gross >= 0) and (gross <= 9950):
    tax_owed = gross * 0.1
    tax_rate = "10%"
elif (gross >= 9951) and (gross <= 40525):
    tax_owed = 995 + (0.12 * (gross - 9950))
    tax_rate = "12%"
elif (gross >= 40526) and (gross <= 86375):
    tax_owed = 4664 + (0.22 * (gross - 40525))
    tax_rate = "22%"
elif (gross >= 86376) and (gross <= 164925):
    tax_owed = 14751 + (0.24 * (gross - 86375))
    tax_rate = "24%"
elif (gross >= 164926) and (gross <= 209425):
    tax_owed = 33603 + (0.32 * (gross - 164925))
    tax_rate = "32%"
elif (gross >= 209426) and (gross <= 523600):
    tax_owed = 47843 + (0.35 * (gross - 209425))
    tax_rate = "35%"
elif gross >= 523601:
    tax_owed = 33603 + (0.32 * (gross - 164925))
    tax_rate = "37%"


formatted_tax = f'${tax_owed:,.2f}'


print("Dear", name, "you have an annual income of", f'${gross:,.2f}', ", your total taxes owed based off your income is", formatted_tax,". Your Tax bracket is", tax_rate)
input("press enter to quit")
print("1")
