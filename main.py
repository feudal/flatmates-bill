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


the_bill = Bill(amount=120, period='March 2021')
john = Flatmate(name="John", day_in_house=17)
marry = Flatmate(name="Marry", day_in_house=24)

print(john.pays(bill=the_bill, flatmate2=marry))
print(marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(john, marry, the_bill)
