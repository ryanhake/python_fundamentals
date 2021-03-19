'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

principal = int(input("Amount of money borrowed: "))
rate = float(input("Interest rate percentage: "))
time = int(input("Time in years: "))
print("future interest owed:",principal*rate/100*time)