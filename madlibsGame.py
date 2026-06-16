#Mad libs is a word game where you create a story by filling in the blanks with random words

adj = input("Please enter an adjective: ")
noun1 = input("Please enter a noun (person, animal, etc.): ")
verb1 = input("Please enter a verb (action for the noun): ")
noun2 = input("Please enter another noun (something to eat): ")
verb2 = input("Please enter a final verb: ")

# story part
print(f"\nToday I saw a/an {adj} {noun1} in the middle of the zoo, ")
print(f"and it suddenly started to {verb1} while eating a giant {noun2}, ")
print(f"which made all the visitors {verb2} in complete shock!")
