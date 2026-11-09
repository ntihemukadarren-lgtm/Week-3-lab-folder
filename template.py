"""
RECORD CHECK  -  my version
===========================

Name  : Ntihemuka Migambi Darren
Lane  :  AI     (delete two)
Date  : 10/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """If user input is <90 then "OK"
       If user input is >=90 then "Warning"
       If user input is >=100 then "Over limit" 
    """
    if percent >= 100:
        return "over limit"
    elif percent >= 90:
        return "Warning"
    else:
        return "OK"


def check(value, limit):
    """
    Calculates difference between value and limit and percentage of the value to the limit
    """
    difference = value-limit
    percentage = (value/limit)*100
    return difference, percentage


def print_report(label, value, limit, difference, percent, status):
    """
    Prints label, value, limit, difference, percent, status
    """
    print(f"value = {value}")
    print(f"limit = {limit}")
    print(f"Difference = {difference:+.2f}")
    print(f"Percentage = {percentage:.2f}%")
    print(f"status = {status}")
    return label, value, limit, difference, percent, status


#
while True:
    next = input("Continue? (y/n) : ")
    if next == "n":
        print("quit")
        break
    elif next == "y":
        label = input("Choose a label: ")
        value = float(input("Your value: "))
        limit = float(input("Your limit: "))

        difference, percentage = check(value, limit)
        status = status_of(percentage)

        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {label}")
        print("=" * 34)
        print(f"value = {value}")
        print(f"limit = {limit}")
        print(f"Difference = {difference:+.2f}")
        print(f"Percentage = {percentage:.2f}%")
        print(f"status = {status}")
        print("=" * 34)
        print(print_report(label, value, limit, difference, percentage, status))
        print("=" * 34)
