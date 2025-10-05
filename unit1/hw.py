# printing bakery name to console
print("\t\t\t✧･ﾟ: *✧･ﾟ✧Dream Bakery:･ﾟ✧*:･ﾟ✧")
print("\t\t\t\t┗━•❃°•°❀°•°❃•━┛")
# list of items and prices
my_list = ["Chocolate Chip Cookie $2.00", "Cheesecake $40.00", "Muffin+Cupcake $5.00", "Bread $5.00", "Custom Order Cake $100.00", "Pie $30.00", "Chocolate Brownie $2.00", "Glazed Donut $4.00", "Coffee $3.00", "Eclair and Cream Puff $18.00"]
# storing items to a list
item_list = ["1. Chocolate Chip Cookie", "2. Cheesecake", "3. Muffin+Cupcake", "4. Bread", "5. Custom Order Cake", "6. Pie", "7. Chocolate Brownie", "8. Glazed Donut", "9. Coffee", "10. Eclair and Cream Puff"]
# storing prices to a list
price_list = [2, 40, 5, 5, 100, 30, 2, 4, 3, 18]
# printing menu to console
print("\n\t1. Chocolate Chip Cookie $2.00  \t6. Pie $30.00  \n\t2. Cheesecake $40.00  \t\t\t7. Chocolate Brownie $2.00  \n\t3. Muffin+Cupcake $5.00  \t\t8. Glazed Donut $4.00  \n\t4. Bread $5.00  \t\t\t9. Coffee $3.00  \n\t5. Custom Order Cake $100.00  \t\t10. Eclair and Cream Puff $18.00")
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●")
# asking customer what they would like to buy, how many, and how much it is using variables and the input function
buy_again = "yes"
total = 0
final_order_items = []  # List to store the names of ordered items
final_order_quantities = []  # List to store the quantities of ordered items
while buy_again == "yes":
    input("Hi what can I get for you today?")
    sequence_num = int(input("Please enter the number of the item:"))
    amount = int(input("How many would you like?"))
    item = item_list[sequence_num-1].split('. ', 1)[1] # Get just the item name
    price = price_list[sequence_num-1]

    final_order_items.append(item)
    final_order_quantities.append(amount)

    item_total = amount * price
    # calculating and printing total price
    total = total + item_total
    buy_again = input("Would you like to buy again?")

print("Your total before deductions is $", total)
# asking for amount spent to get credit points
credit_point = input("Have you spent $50 in our shop?")
if credit_point == "yes":
    credit_point == 5
    # asking how many credit points they would like to use
    deductions = int(input("How many credit points would you like to spent?"))
else:
    credit_point == 0
    deductions = 0
# printing customer final order
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●")
print("Order:")
for i in range(len(final_order_items)):
    item = final_order_items[i]
    quantity = final_order_quantities[i]
    price = price_list[item_list.index([it for it in item_list if it.split('. ', 1)[1] == item][0])]
    print(f"- {item} (x{quantity}) - ${price * quantity:.2f}")

print(f"You have {deductions} credit points")
# calculating total price after deductions
final_total = total - deductions
if deductions > 0:
    print("Your total after using points is $", final_total)
else:
    pass
# printing thank yous
print("Thank you for ordering with us, have a nice day!")
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・●・○・●")
