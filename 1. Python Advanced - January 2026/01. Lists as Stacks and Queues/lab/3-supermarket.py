customer_name = input()

customers = []

while True:
    if customer_name == "End":
        break

    if customer_name == "Paid":
        print("\n".join(customers))
 
        customers.clear()
        customer_name = input()
        continue

    customers.append(customer_name)
    customer_name = input()

print(f"{len(customers)} people remaining.")