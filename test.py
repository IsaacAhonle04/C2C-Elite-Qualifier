import unittest
from main import generate_response_1
#from main import generate_response_2
#from main import generate_response_3
#from main import generate_response_4
#from main import generate_response_good
#from main import generate_response_bad
class TestResponseGeneration(unittest.TestCase):
  def test_set1_1(self):
    self.assertEqual (generate_response_1(user_input="Hello!"),"Interesting!")
  #def test_set1_2(self):
   # self.assertEqual (generate_response_1(user_input="Hello!"),"Nice one!")    
  #def test_set1_3(self):
   # self.assertEqual (generate_response_1(user_input="Hello!"),"Me too!")

if __name__ == '__main__':
    unittest.main()