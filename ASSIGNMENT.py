# NAME: ADENIYI OLUWADEMILADEAYO SAMUEL
# MATRIC NUMBER: BU24CSC1016
# DEPARTMENT : COMPUTER SCIENCE

def tax():
    details = (
        "0 = Single Fillers",
        "1 = Married Filling jointly or qualified window(er)",
        "2 = Married Filling Separately",
        "3 = Head of Household",
    )
    print(details)

    status_tax = int(input("Enter Tax status: "))
    taxable_income = int(input("Enter the income: "))

    # SINGLE FILLERS
    if status_tax == 0:
        print("Single Fillers")

        if 0 <= taxable_income <= 8350:
            tax0 = 0.10 * taxable_income

        elif 8351 <= taxable_income <= 33950:
            tax0 = (0.10 * 8350) + ((taxable_income - 8350) * 0.15)

        elif 33951 <= taxable_income <= 82250:
            tax0 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((taxable_income - 33950) * 0.25)

        elif 82251 <= taxable_income <= 171550:
            tax0 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((82250 - 33950) * 0.25) + ((taxable_income - 82250) * 0.28)

        elif 171551 <= taxable_income <= 372950:
            tax0 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((82250 - 33950) * 0.25) + ((171550 - 82250) * 0.28) + ((taxable_income - 171550) * 0.33)

        else:
            tax0 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((82250 - 33950) * 0.25) + ((171550 - 82250) * 0.28) + ((372950 - 171550) * 0.33) + ((taxable_income - 372950) * 0.35)

        print("Total Tax is", tax0)

    # MARRIED FILING JOINTLY
    elif status_tax == 1:
        print("Married Filling jointly or qualified window(er)")

        if 0 <= taxable_income <= 16700:
            tax1 = 0.10 * taxable_income

        elif 16701 <= taxable_income <= 67900:
            tax1 = (0.10 * 16700) + ((taxable_income - 16700) * 0.15)

        elif 67901 <= taxable_income <= 137050:
            tax1 = (0.10 * 16700) + ((67900 - 16700) * 0.15) + ((taxable_income - 67900) * 0.25)

        elif 137051 <= taxable_income <= 208850:
            tax1 = (0.10 * 16700) + ((67900 - 16700) * 0.15) + ((137050 - 67900) * 0.25) + ((taxable_income - 137050) * 0.28)

        elif 208851 <= taxable_income <= 372950:
            tax1 = (0.10 * 16700) + ((67900 - 16700) * 0.15) + ((137050 - 67900) * 0.25) + ((208850 - 137050) * 0.28) + ((taxable_income - 208850) * 0.33)

        else:
            tax1 = (0.10 * 16700) + ((67900 - 16700) * 0.15) + ((137050 - 67900) * 0.25) + ((208850 - 137050) * 0.28) + ((372950 - 208850) * 0.33) + ((taxable_income - 372950) * 0.35)

        print("Total Tax is", tax1)

    # MARRIED FILING SEPARATELY
    elif status_tax == 2:
        print("Married Filling Separately")

        if 0 <= taxable_income <= 8350:
            tax2 = 0.10 * taxable_income

        elif 8351 <= taxable_income <= 33950:
            tax2 = (0.10 * 8350) + ((taxable_income - 8350) * 0.15)

        elif 33951 <= taxable_income <= 68525:
            tax2 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((taxable_income - 33950) * 0.25)

        elif 68526 <= taxable_income <= 104425:
            tax2 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((68525 - 33950) * 0.25) + ((taxable_income - 68525) * 0.28)

        elif 104426 <= taxable_income <= 186475:
            tax2 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((68525 - 33950) * 0.25) + ((104425 - 68525) * 0.28) + ((taxable_income - 104425) * 0.33)

        else:
            tax2 = (0.10 * 8350) + ((33950 - 8350) * 0.15) + ((68525 - 33950) * 0.25) + ((104425 - 68525) * 0.28) + ((186475 - 104425) * 0.33)

        print("Total Tax is", tax2)

    # HEAD OF HOUSEHOLD
    elif status_tax == 3:
        print("Head of Household")

        if 0 <= taxable_income <= 11950:
            tax3 = 0.10 * taxable_income

        elif 11951 <= taxable_income <= 45500:
            tax3 = (0.10 * 11950) + ((taxable_income - 11950) * 0.15)

        elif 45501 <= taxable_income <= 117450:
            tax3 = (0.10 * 11950) + ((45500 - 11950) * 0.15) + ((taxable_income - 45500) * 0.25)

        elif 117451 <= taxable_income <= 190200:
            tax3 = (0.10 * 11950) + ((45500 - 11950) * 0.15) + ((117450 - 45500) * 0.25) + ((taxable_income - 117450) * 0.28)

        elif 190201 <= taxable_income <= 372950:
            tax3 = (0.10 * 11950) + ((45500 - 11950) * 0.15) + ((117450 - 45500) * 0.25) + ((190200 - 117450) * 0.28) + ((taxable_income - 190200) * 0.33)

        else:
            tax3 = (0.10 * 11950) + ((45500 - 11950) * 0.15) + ((117450 - 45500) * 0.25) + ((190200 - 117450) * 0.28) + ((372950 - 190200) * 0.33)

        print("Total Tax is", tax3)

    else:
        print("Invalid tax status")

tax()
