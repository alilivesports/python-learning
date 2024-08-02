print("Hello World")
first_name = "Ali"
last_name = "Raza"
full_name = f"{first_name} {last_name}"
print(full_name)

# bikes = ['trek', 'redline', 'giant']

# first_bike = bikes[0]
# last_bike = bikes[-1]

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

for bike in bikes:
    print(bike)

squares = []
for x in range(1, 11):
    squares.append(x**2)    

print(squares)    

squares = [x**2 for x in range(1, 11)]
print(squares)    

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[-2:]
copy_finishers = finishers[:]
print(copy_finishers)