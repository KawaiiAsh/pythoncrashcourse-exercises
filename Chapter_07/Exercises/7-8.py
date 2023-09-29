sandwich_orders = ['Beef sandwich','Tuna sandwich','Lamb sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("All sandwich are done........")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)