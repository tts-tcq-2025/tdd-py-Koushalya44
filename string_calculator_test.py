import unittest
from monitor import check_vitals_with_warning

class Test_string_calculator(unittest.Testcase):
  def test_empty_string_return_zero(self):
    # arrange
    input = ""
    expected_value =0
    # action
    actual_value = add(input)
    # assert
    self.assertEqual(actual_value, expected_value)

if__name__=="main__",

