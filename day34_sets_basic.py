# Day 34 - Sets Basics

# Create a set
cities = {"Patna", "Delhi", "Mumbai", "Tokyo", "New York"}
print(cities)

# Empty set + add()
a = set()
a.add(10)
a.add(20)
a.add(30)
print(a)

# Remove item
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)

# Membership check
languages = {"Java", "Python", "C++"}
print("Python" in languages)

# Convert list into set
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))

# Set with tuple values
pairs = {(1, 2), (3, 4)}
print(pairs)

# Set from string
word = set("school")
print(word)

# Length of set
data = {100, 200, 200, 300, 400}
print(len(data))

# Add and remove together
colors = {"red", "blue", "green"}
colors.add("yellow")
colors.remove("blue")
print(colors)

# Check value exists or not
values = {10, 20, 30, 40, 50}
print(50 in values)