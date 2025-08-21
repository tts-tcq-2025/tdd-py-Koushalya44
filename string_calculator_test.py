import unittest
from string_calculator import add
class Test_string_calculator(unittest.Testcase):
  def test_empty_string_return_zero(self):
    # arrange
    input = ""
    expected_value =0
    # action
    actual_value = add(input)
    # assert
    self.assertEqual(actual_value, expected_value)

if __name__=="main__":
  unittest.main()

