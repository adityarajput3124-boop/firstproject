name = input("Enter customer's name: ")
amount = float(input("Enter total shopping amount: ₹"))

if amount >= 50000:
    discount_rate = 20
elif amount >= 30000:
    discount_rate = 15
elif amount >= 10000:
    discount_rate = 10
else:
    discount_rate = 0

discount_amount = amount * discount_rate / 100
final_amount = amount - discount_amount

print("----- BILL DETAILS -----")
print("Customer Name:", name)
print("Original Amount: ₹", amount)
print("Discount Amount: ₹", discount_amount)
print("Final Amount to be Paid: ₹", final_amount)






even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for i in range(10):
    num = int(input("Enter a number: "))

    if num == 0:
        break

    if num < 0:
        continue

    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)



class BankAccount:

    bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if self.balance - amount >= 150:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Minimum balance should be 150")

    @staticmethod
    def bank_rules():
        print("Minimum balance should be 150")


customer = BankAccount("Aditya", 5000)

customer.deposit(1000)
customer.withdraw(2000)

customer.bank_rules()

print("Account Details")
print("Bank Name:", customer.bank_name)
print("Account Holder:", customer.account_holder)
print("Balance:", customer.balance)


