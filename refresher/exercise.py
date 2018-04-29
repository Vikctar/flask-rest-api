def who_do_you_know():
    """Ask the user for a set of people
    they know. Split the string into a list.
    Return that list"""
    who_you_know = input("Tell me the names of people you know, my g, separated by commas:")
    people = who_you_know.split(',')

    people_without_spaces = [person.strip() for person in people]

    return people_without_spaces


watu = who_do_you_know()
print(watu)


def ask_user():
    """Ask user for a name
    See if their name is in the list of people they know
    Print out that they know the person"""
    known_person = input("Tell me the name of someone you know:")

    if known_person in watu:
        print("you know {} my g".format(known_person))
    else:
        print("You don't know {}, blood".format(known_person))


ask_user()
