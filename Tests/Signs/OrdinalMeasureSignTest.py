import unittest
from Core.MeasureSigns.OrdinalMeasureSign import OrdinalMeasureSign


class MyTestCase(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.correct_ordinal_data = [{"name": "Test ordinal Data",
                                      "data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["No", "Maybe", "Yes"]
                                      }, {"name": "Тест Ранговой шкалі",
                                          "data": {
                                              89: 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Yes", 89]
                                          },
                                     {"name": "Test ordinal Data",
                                      "data": {
                                          "Maybe": 87,
                                          "Yes": 5,
                                          'Iess': 1
                                      },
                                      "ranks": ["Maybe", "Yes", f'Iess']
                                      },
                                     {"name": "Test ordinal Data",
                                      "data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["Yes", "No", "Maybe"]
                                      }, {"name": "Test ordinal Data",
                                          "data": {
                                              "Yes": 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Maybe", "Yes"]
                                          }
                                     ]

    def test_ordinal(self):
        OrdinalMeasureSign()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
