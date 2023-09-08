# message = "Hello Python Crash Course reader!"
# print(message)
# messageTwo="Message two" 
# print(messageTwo)
# messageTwo="message two changed"
# print(messageTwo.title())
# ##########################################
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name.title())
# print(f"Merhaba, {full_name.title()}")

# favorite_language = 'python '
# print(favorite_language)
# print(favorite_language.rstrip())

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-2])

# cars = ['bmw', 'badi', 'toyota', 'subaru'] 
# cars.sort()
# print(cars)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#   print(f"{magician.title()}, that was a great trick!")
#   print(f"I can't wait to see your next trick, {magician.title()}.\n")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#   print(f"{magician.title()}, that was a great trick!") 
# print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print(magician)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you everyone, that was a great magic show!")

# numbers = set(range(1, 6))
# print(numbers)


# numbers = list(range(1, 6))
# print(numbers)

# squares = []
# for value in range(1,11):
#   squares.append(value**2) 
# print(squares)

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])
# my_t = (3,)
# print(my_t[1])

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0 
# alien_0['y_position'] = 25
# print(alien_0)  
# del alien_0['points']


# user_0 = {
# 'username': 'efermi',
# 'first': 'enrico',
# 'last': 'fermi',
# }
# print(user_0.items())

# user_0 = {
# 'username': 'efermi',
#               'first': 'enrico',
#               'last': 'fermi',
#               }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())
    
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()): 
#   print(language.title())
  
# print(favorite_languages.values())
# print(set(favorite_languages.values()))

# print(list(range(1, 10)))
# print(set(range(1, 10)))
# print(tuple(range(1, 10)))

# def build_person(first_name, last_name, age=None):
#        """Return a dictionary of information about a person."""
#        person = {'first': first_name, 'last': last_name}
#        if age:
#            person['age'] = age
#        return person
# musician = build_person('jimi', 'hendrix',27)
# print(musician)

# def get_formatted_name(first_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = f"{first_name} {last_name}"
#        return full_name.title()
#    # This is an infinite loop!
# while True:
#       print("\nPlease tell me your name:")
#       f_name = input("First name: ")
#       l_name = input("Last name: ")
#       formatted_name = get_formatted_name(f_name, l_name)
#       print(f"\nHello, {formatted_name}!")