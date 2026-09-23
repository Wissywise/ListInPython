# Step 1: Creating the Purchase History using a list of lists
purchase_history = [
    ["Laptop", 500],
    ["Mouse", 5],
    ["Keyboard", 10],
    ["Headphones", 15],
    ["Monitor", 50],
    ["Phone", 300],
    ["USB Drive", 10]
]

# Step 2: Function to display the recent purchases
def show_recent_purchases(history, n=5):
    recent_purchases = history[-n:]  # Get the last 'n' purchases
    print("\nRecent Purchases:")
    for purchase in recent_purchases:
        item = purchase[0]  # Extract item name
        price = purchase[1]  # Extract price
        print(f"{item}: ${price}")

# Step 3: Function to add a new purchase
def add_purchase(history, item, price):
    history.append([item, price])  # Append as a list instead of a tuple
    print(f"\nAdded: {item} - ${price}")

# Step 4: Function to check if an item is expensive or affordable
is_expensive = lambda price: "Expensive" if price > 500 else "Affordable"

# Step 5: Function to calculate total spent amount
def total_spent(history):
    return sum(purchase[1] for purchase in history)  # Extract prices from lists

# Step 6: Show initial recent purchases
show_recent_purchases(purchase_history)

# Step 7: Taking user input for new purchases
while True:
    item_name = input("\nEnter item name (or 'exit' to stop): ").strip()
    if item_name.lower() == "exit":
        break  # Stop taking input

    item_price = float(input("Enter item price: "))
    add_purchase(purchase_history, item_name, item_price)

    print(f"Last purchase '{item_name}' is {is_expensive(item_price)}.")

# Step 8: Show final recent purchases and total spent amount
show_recent_purchases(purchase_history)
print(f"\nTotal Amount Spent: ${total_spent(purchase_history)}")

