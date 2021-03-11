from flats import Bill, Flatmate
from reports import PdfReport

amount = float(input('Hey user, enter the bill amount: '))
period = input('Enter the period. e.g. December 2021 ')
the_bill = Bill(amount, period)

your_name = input('Enter your name: ')
days = int(input(f'Enter how many days {your_name} was home in the bill period: '))
flatmate1 = Flatmate(your_name, days)

flatmate_name = input('Enter flatmate\'s name: ')
days2 = int(input(f'Enter how many days {flatmate_name} was home in the bill period: '))
flatmate2 = Flatmate(flatmate_name, days2)

print(f'{flatmate1.name} pays: ',flatmate1.pays(the_bill, flatmate2))
print(f'{flatmate2.name} pays: ',flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, the_bill)
