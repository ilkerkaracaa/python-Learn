from name_function import get_formatted_name
def test_first_last_name():
  """Do names like 'Janis Joplin' work?"""
  formatted_name = get_formatted_name('janis', 'joplin')
  assert formatted_name == 'Janis Joplin'
def test_first_last_middle_name():
  """Do names like 'Wolfgang Amadeus Mozart' work?"""
  formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
  assert formatted_name == 'Wolfgang Amadeus Mozart'
  
  
  # import unittest
# print(__name__)
# from name_function import get_formatted_name
# class NamesTestCase(unittest.TestCase): 
#   """Tests for 'name_function.py'."""
#   def test_first_last_name(self):
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     self.assertEqual(formatted_name, 'Janis Joplin')
# if __name__ == '__main__': 
#   unittest.main()