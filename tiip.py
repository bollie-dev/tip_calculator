# -*- coding: utf-8 -*-
"""
Challenge: Tip Calculator

Created on Fri May 17 15:53:12 2024

@author: EJ Bollie

"""

# Welcome message
print("Welcome to the tip Calculator!")
print()
print()

# What is the total bill?
bill = float(input("What was the total bill? $"))

# What percentage tip would you like to give? 10, 12, or 15
tip = int(input(
    "How much tip would you like to give? Tip in percentage: 10, 12, or 15:  "))

# How many people to split the bill?
people = int(input("How many people splitting the bill? "))


# Calculating the user inputs for {bill} and {tip}
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount

# Calculation for spliting the bill between user input for {people}

bill_per_person = total_bill / people
print()
print()
print(f"Your bill + tip = ${total_bill}")
print()
print("Bill per person: $", round(bill_per_person))


