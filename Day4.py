# IMPORTANT: To run this file
# 1. Open your terminal
# 2. cd into the learn_python directory
# 3. paste the command: python3 Day4.py

# TODO: Complete the following tasks.
#  * Create a list called my_favorite_numbers and use `.append` to add three numbers to the list.
#  * Create a list called my_favorite_people and use `.append` to add three names to the list.
#  * Create a new list called my_favorite_numbers_again. This list should be equal to the numbers from the first list repeated five times. Use the multiplication operator and your old list to do this.
#  * Create a new list called more_people and `.append` three more names.
#  * Create a new list called all_my_favorite_people. This list should be equal to both of your previous people lists. Use the addition operation to do this.
#  * Create a new list called my_favorite_people_and_numbers. It should be equal to your favorite people and favorite numbers in the same list.

my_favorite_numbers = []
my_favorite_numbers.append(8)
my_favorite_numbers.append(2)
my_favorite_numbers.append(82)

my_favorite_people = []
my_favorite_people.append("Kia")
my_favorite_people.append("Auri")
my_favorite_people.append("Alara")

my_favorite_numbers_again = [x * 5 for x in [my_favorite_numbers]]

more_people = []
more_people.append("Matt")
more_people.append("Kai")
more_people.append("Papa Chris")

all_my_favorite_people = my_favorite_people + more_people

my_favorite_people_and_numbers = all_my_favorite_people + my_favorite_numbers


# TODO: When you run this file, *ALL* of the following should happen:
#  * The third number from your my_favorite_numbers list should appear in the terminal. You MUST use the index property (ie my_favorite_numbers[8]) to do this.
#  * The first name from your my_favorite_people list should appear. Use the same method as for the above task.
#  * "This is a list of my favorite numbers:" should appear in the terminal.
#  * The list of your favorite numbers should appear.
#  * "This is a list of my favorite numbers, but bigger:" should appear in the terminal.
#  * The list of your bigger favorites numbers should appear.
#  * "This is a list of my favorite people:" should appear in the termianl.
#  * The list of all your favorite people should appear.
#  * Find the remainder when 1178 is divided by 9. The answer appear in the terminal.
#  * Find the answer to 89 times 725 plus 19029. It should appear in the terminal.
#  CHALLENGE: Create two new lists, one of numbers and one of names. Add them together to form a new list. The new list appear in the terminal.

print(my_favorite_numbers[1])
print(my_favorite_people[0])

print("This is a list of my favorite numbers:")
print(my_favorite_numbers)

print("This is a list of my favorite numbers, but bigger:")
print(my_favorite_numbers_again)

print("This is a list of my favorite people:")
print(my_favorite_people)

print(1178 % 9)
print(89 * 725 + 19029)

new_numbers = [100, 200, 300]
new_names = ["Brayden", "Brent", "Evs"]
new_numbers_and_names = new_numbers + new_names
print(new_numbers_and_names)