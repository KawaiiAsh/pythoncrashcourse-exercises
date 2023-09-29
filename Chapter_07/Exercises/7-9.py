sandwich_orders = ['Beef sandwich','Pastrami sandwich','Tuna sandwich'
                   ,'Pastrami sandwich','Lamb sandwich','Pastrami sandwich']
finished_orders = []
print("All Pastrami sandwich are out of stock.......")

while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_orders.append(current_sandwich)
    
print("Sandwich_orders list:", sandwich_orders)
print("Finished_orders list:", finished_orders)
