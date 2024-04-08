def lb2kg(pounds):
    kilos = pounds * 0.45
    return kilos

def in2m(inches):
    meters = round(inches * 0.025, 3)
    return meters

def calcBMI(height, weight):
    bmi = round(weight/(height**2), 1)
    return bmi

def bmiCategory(bmi):
    category = ""
    # T = "threshold"
    normalT = 18.5
    overweightT = 25
    obeseT = 30

    if bmi < normalT:
        category = "Underweight"
    elif normalT <= bmi < overweightT:
        category = "Normal Weight"
    elif overweightT <= bmi < obeseT:
        category = "Overweight"
    elif bmi >= obeseT:
        category = "Obese"
    return category


def main():
    feet = float(input("Enter height:\n\tfeet: "))
    inches = float(input("\tinches: "))
    pounds = float(input("Enter weight\n\tpounds: "))

    inches = (feet * 12) + inches

    meters = in2m(inches)
    kilos = lb2kg(pounds)

    bmi = calcBMI(meters, kilos)
    category = bmiCategory(bmi)

    return bmi, category
