# Sorting by key:
import random

# -----> 1. Using the next list: ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
# Use sort and lambda to sort by:

cities_list: list = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(f'1. Original List: {cities_list}')

# a. By the length of the city name:

print(f'a. The list by the length of the city name: {sorted(cities_list, key=lambda c: len(c))}')

# b. By the number of words in the city name
#.split counts the number of units of an item in the list.

print(f'b. The list by the number of words in the city name: {sorted(cities_list, key=lambda c: len(c.split()))}')

# c. By the last letter of the city name

print(f'c. The list by the last letter of the city name: {sorted(cities_list, key=lambda c: c[-1])}')

# d. The city name in reverse letter order

print(f'd. List by the city name in reverse order: {sorted(cities_list, key=lambda c: len(c), reverse=True)}')

# e. Bonus: The number of times the letter "a" appears in the city name

# f. Add the distance in miles from Israel and the continent name. For example:
# #[["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, ["Europe"], ["London", 2240, "Europe"],
# ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]

dist_list: list = [["Israel", 3766, "Asia"], ["Israel", 6062, "North America"], ["Israel", 1887, "Europe"],\
                   ["Israel", 7589, "Australia / Oceania"], ["Israel", 4216, "Africa"],\
                   ["Israel", 7459, "Central America"], ["Israel", 6546, "South America"], ["Israel", 8427, "Antarctica"]]

print(f'f. Distances from Israel to each continent: {dist_list}')
print()

# f.a. Sort by the distance from Israel

print(f'f.a. List sort by the distance from Israel: {sorted(dist_list, key=lambda d: d[1])}')
print()

# f.b. Sort by the distance from Israel, from largest to smallest

print(f'f.b. List sort by the distance, from largest to smallest: {sorted(dist_list, key=lambda d: d[1], reverse=True)}')
print()

# f.c. Sort by the continent name

print(f'f.c. List sort by by the continent name: {sorted(dist_list, key=lambda d: d[2])}')
print()

# f.d. Sort by the continent name, and then by the distance. (Hint: sort, 2nd sort, 1st sort)

print(f'f.d. List sort by by the continent name, and distance: {sorted(dist_list, key=lambda d: d[2] [1])}')
print()

#1.1Create a list of 50 random numbers between 1-100

num_ran = []

ran_num_list = []
for n in range(50):
    ran_num_list.append(random.randint(1, 101))
print(f'1.1. List of random numbers from 1-100: {ran_num_list}')
print()
#print(f'1.1. List of random numbers from 1-100: {sorted([random.randint(1, 101) for n in range(50)], key=lambda n: n)}')

#1.1a. Sort and print the list in ascending order

print(f'1.1a. List in ascending order: {sorted([random.randint(1, 101) for n in range(50)], key=lambda n: n)}')
print()

#1.1b. Sort and print the numbers by their distance from the average

# -----> 2. Lexical Dictionary
# Below is the following passage:
#
# "This chocolate cake is rich, moist, and full of delicious chocolate flavor.
# To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
# After baking the chocolate cake, let the cake cool before adding the chocolate frosting."
#
# a. Count how many times each word repeats itself, and then print all the words that appeared and how many times each
# word appeared... What word appeared the most times?
#
# b. Count how many times each letter repeats itself, and then print all the letters that appeared and how many times each
# letter appeared... What letter appeared the least number of times?



# -----> 3. Numerical Dictionary
#
# Create a dictionary where the key is a number (base) and the value is that number raised to the power of 3, for
# numbers from 1 to 20.
# For example: {1: 1, 2: 8, 3: 27, ...}
# Explanation: 1 raised to the power of 3 = 1, 2 raised to the power of 3 = 8, 3 raised to the power of 3 = 27, etc.
#
# Now, accept a number from the user and print the result of the number raised to the power of 3.
# For example, if the user inputs the number 2, the answer printed will be 8.
# If the number doesn't exist in the dictionary, print "n does not exist."