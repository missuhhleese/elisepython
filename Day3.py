# IMPORTANT: To run this file
# 1. Open your terminal
# 2. cd into the learn_python directory
# 3. paste the command: python3 Day3.py

# TODO: Complete the following tasks.
#  * Save the name Matthew as a variable called brother.
#  * Save the name Liz as a variable called mother.
#  * Save the name Kia as a variable called best_sister_ever.
#  * Save the name Kayla as a variable called okayest_sister.
#  * Save the name Penny as a variable called dog.
#  * Create an empty list called family_members.
#  * Create an empty list called family_rankings.
#  * Add your family members (the variables you created) to the list family_members using the `.append` method.
#  * Rank those family members on a scale of 1-5 by using the `.append` method to add a ranking to the list
#  family_rankings. Here is how they should be ranked: Liz -> 1, Kayla -> 2, Matthew -> 3, Penny -> 4, Kia -> 5.
#  For example, if Matthew is first in you family_members list, then you would need to append his ranking FIRST bu using
#  family_rankings.append(3).

# TODO: When you run this file, *ALL* of the following should happen:
#  * "Who are your top five favorite family members?" should appear in the terminal.
#  * Your family_members list (the answer) should appear in the terminal.
#  * "How would you rank those family members on a scale of 1-5, 5 being the most awesome?" should appear in the terminal.
#  * Your family_rankings list (the answer) should appear in the terminal.
#  * "Wow! I need to meet this Kia person, she must be awesome!!!" should appear in the terminal next.
#  * The answer to the above question should appear in the terminal. You MUST use the variable you created.
#  * "Who is your other sister, the just-okay one?" should appear in the terminal.
#  CHALLENGE: The answer (Meagan of course) should appear in the terminal. You MUST refer to Megan using her index in
#  the family_members list. For example: family_members[1].

brother = "Matthew"
mother = "Liz"
best_sister_ever = "Kia"
okayest_sister_ever = "Kayla"
dog = "Penny"

family_members = []

family_members.append(brother)
family_members.append(mother)
family_members.append(best_sister_ever)
family_members.append(okayest_sister_ever)
family_members.append(dog)


family_rankings = []

family_rankings.append(3)
family_rankings.append(1)
family_rankings.append(5)
family_rankings.append(2)
family_rankings.append(4)

print("Who are your top five favorite family members?")
print(family_members)

print("How would you rank those family members on a scale of 1-5, 5 being the most awesome?")
print(family_rankings)

print("Wow! I need to meet this Kia person, she must be awesome!!!")

print("Who is your other sister, the just-okay one?")
print(family_members[3])