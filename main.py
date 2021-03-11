import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, day_in_house):
        self.name = name
        self.day_in_house = day_in_house

    def pays(self, bill, flatmate2):
        return bill.amount / (self.day_in_house + flatmate2.day_in_house) * self.day_in_house


class PdfReport:
    """
    Create pdf report that contain period and how
    much will pay each flatmate
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A5')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=30)
        #Add icon
        pdf.image('house.png', w=30, h=30)
        #Add title to the bill
        pdf.cell(w=540, h=100, txt='Flatmates Bill', border=0, align='L', ln=1)
        #Insert the period of the bill
        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=100, h=50, txt='Period:', border=0, align='L')
        pdf.cell(w=440, h=50, txt=bill.period, border=0, align='L', ln=1)
        #Insert name of the flatmates and amount that they need to pay
        pdf.set_font(family='Times', style='I', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='L')
        pdf.cell(w=440, h=25, txt=flatmate1_pay + ' $', border=0, align='L', ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='L')
        pdf.cell(w=440, h=25, txt=flatmate2_pay + ' $', border=0, align='L', ln=1)
        #Toal amount of the bill
        pdf.cell(w=100, h=25, txt='Total', border=0, align='L')
        pdf.cell(w=440, h=25, txt=str(bill.amount) + ' $', border=0, align='L', ln=1)

        # pdf.cell(w=540, h=500, txt='', border=1, align='L', ln=1)
        # pdf.cell(w=540, h=50, txt='', border=1, align='L', ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)

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
