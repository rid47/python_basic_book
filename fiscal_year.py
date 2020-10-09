from datetime import datetime
date = input("Enter Date: ")


def find_fiscal_year(date):
    """Convert date string format %Y-%m-%d to Fiscal Year"""
    # Converting date str to date obj for comparision
    print("Inside find_fiscal_year")
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    print(date_obj)
    # 1st July of current year
    threshold_date = datetime(date_obj.year, 7, 1, 0, 0)
    if date_obj < threshold_date:
        fiscal_year_part_1 = date_obj.year - 1
        fiscal_year_part_2 = date_obj.year - 2000
        fiscal_year = str(fiscal_year_part_1)+"-"+str(fiscal_year_part_2)
    else:
        fiscal_year_part_1 = date_obj.year
        fiscal_year_part_2 = (date_obj.year + 1) - 2000
        fiscal_year = str(fiscal_year_part_1)+"-"+str(fiscal_year_part_2)

    return fiscal_year


result = find_fiscal_year(date)
print(f"result: {result} and typeof result: {type(result)}")
