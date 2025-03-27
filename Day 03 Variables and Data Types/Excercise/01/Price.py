# Create a variable to store the price of an item. Calculate the total cost after adding 10% sales tax.
Item_Price=float(input("Enter the price of the item:"))
Sales_Tax=Item_Price*0.1
Total_Price=Item_Price+Sales_Tax
print(f"Item price:{Item_Price},Sales Tax:{Sales_Tax},Total Price:{Total_Price}")