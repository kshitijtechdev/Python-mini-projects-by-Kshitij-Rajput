# inventory
d = {
    "apple": 40.00,   
    "banana": 60.00, 
    "orange": 75.00, 
    "grapes": 30.00,  
}

print("Items Available")
for i, j in d.items():
    print("{}: Rs {:.2f} per kg".format(i.capitalize(), j))

c = {}
t = 0

while True:
    i = input("Enter the item you want to purchase (or type 'done' to finish shopping): ").lower()
    if (i == "done"):
        break
    if (i in d):
        q = float(input("Enter quantity of {} (in kg): ".format(i.capitalize())))
        t += d[i] * q
        c[i] = q
    else:
        print("Item not available in the inventory. Please choose another item.")

print("Total bill: Rs {:.2f}".format(t))

payment_method = input("Enter payment method (card/cash): ").lower()

if (payment_method == "card"):
    card_number = input("Enter card number: ")
    expiry_date = input("Enter expiry date (MM/YY): ")
    name = input("Enter cardholder's name: ")
    card_balance = float(input("Enter card balance (in rupees): Rs "))

    if (card_balance >= t):
        card_balance -= t
        print("Payment successful!")
        print("Remaining balance: Rs {:.2f}".format(card_balance))
    else:
        print("Not enough funds in the card. Please choose another payment method.")
elif (payment_method == "cash"):
    print("Payment successful!")
else:
    print("Invalid payment method. Please choose between card or cash.")

if (payment_method in ["card", "cash"]):
    print("Generating bill")
    print("Your Bill")
    for i, q in c.items():
        print("{}: {} kg x Rs {} = Rs {:.2f}".format(i.capitalize(), q, d[i], q * d[i]))

    print("Total: Rs {:.2f}".format(t))
    print("Thank you for shopping ")
