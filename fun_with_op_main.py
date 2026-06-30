#day 10
# def format_name(f_name, l_name):
# docstring   """take a first and last name and fprmat it to
#                return the title case version of the name"""
#     # print(f_name.capitalize())
#     # print(l_name.capitalize())   #can also use .title()
#
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs. "
#
#     formated_f = f_name.capitalize()
#     formated_l = l_name.capitalize()
#     return f"{formated_f} {formated_l}"
#
# print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
#------------------------------------------------------------------

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


















