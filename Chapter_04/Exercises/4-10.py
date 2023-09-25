my_foods = ['pizza','falafel','carrot','cake','cannoli','ice cream','apple']
print('The first three items in the list are')
print(my_foods[:3])
print('The iteams from the middle of the list are')
start_index  = len(my_foods) // 2 - 1
end_index = start_index + 3
print(my_foods[start_index:end_index])
print('Thelast threeitems in thelistare:')
print(my_foods[-3:])
