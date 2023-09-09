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

# def get_formatted_name(first_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = f"{first_name} {last_name}"
#        return full_name.title()
# while True:
#        print("\nPlease tell me your name:")
#        print("(enter 'q' at any time to quit)")
#        f_name = input("First name: ")
#        if f_name == 'q':
#            l_name = None;
#            break
#        l_name = input("Last name: ")
#        if l_name == 'q':
#                 break
              
# formatted_name = get_formatted_name(f_name, l_name)
# print(f"\nHello, {formatted_name}!")

# list = [1, 2, 3, 4, 5]
# listTwo = []
# while list:
#     listTwo = list.pop()
#     print(f"Printing model: {listTwo}")
#     listTwo = list


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:    
#   current_design = unprinted_designs.pop()
#   print(f"Printing model: {current_design}")    
#   completed_models.append(current_design)
  
# print("\nThe following models have been printed:")
# for completed_model in completed_models:    
#   print(completed_model)


# def print_models(unprinted_designs, completed_models):    
#   while unprinted_designs:
#         current_design = unprinted_designs.pop()        
#         print(f"Printing model: {current_design}")        
#         completed_models.append(current_design)
  
# def show_completed_models(completed_models):    
#         print("\nThe following models have been printed:")    
#         for completed_model in completed_models:        
#           print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def mergeAlternately(word1, word2):
#    result = ""
#    if(len(word1) == len(word2)):
#     for i in range(len(word1)):
#      result += word1[i]
#      result += word2[i]
#     return result
#    if(len(word1) < len(word2)):
#      for i in range(len(word1)):
#        result += word1[i]
#        result += word2[i]
#      result += word2[len(word1):]
#      return result
#    if(len(word1) > len(word2)):
#      for i in range(len(word2)):
#        result += word1[i]
#        result += word2[i]
#      result += word1[len(word2):]
#      return result
          
  

# print(mergeAlternately("abcanan", "pqr"))


# class Dog:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
        
# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# print(my_dog)
# my_dog.sit()
# my_dog.roll_over()

# class Car:
# # A simple attempt to represent a car.
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
                 
# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size
#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} miles on a full charge.")
            
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank!")
                
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# car = Car('audi', 'a4', 2019)
# car.fill_gas_tank()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()