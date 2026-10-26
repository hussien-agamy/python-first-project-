name = input("Enter your name: ")
amount = float(input("Enter purchase amount: "))
member = str(input("Are you a member? (yes/no): ").lower())
if amount >= 2000 and member == "yes":
    discount_rate = 0.25
elif amount >= 1000 or member == "yes":
    discount_rate = 0.10
else:
    discount_rate = 0
discount = amount * discount_rate
final_amount = amount - discount
print("Customer:" + str(name))
print("Original Price:" + str(amount))
print("Discount:" + str(discount))
print("Final Price:" + str(final_amount))

