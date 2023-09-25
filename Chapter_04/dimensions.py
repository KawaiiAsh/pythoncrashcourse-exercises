dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 # Tuple object does not support item assignment

for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("Modified dimensions")
for dimension in dimensions:
    print(dimension)