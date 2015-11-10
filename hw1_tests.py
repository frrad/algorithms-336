import unittest
import hw1


class TestStringMethods(unittest.TestCase):

    def test_example(self):
        hospital_rankings = [[0, 1, 2], [2, 1, 0]]
        student_rankings = [[0, 1], [0, 1], [0, 1]]

        expected_output = [0, 2]

        self.assertEqual(
            hw1.stable_matching(hospital_rankings, student_rankings), expected_output)

    def test_trickier(self):
        hospital_rankings = [[0, 1, 2], [0, 1, 2]]
        student_rankings = [[0, 1], [0, 1], [0, 1]]

        expected_output = [0, 1]

        self.assertEqual(
            hw1.stable_matching(hospital_rankings, student_rankings), expected_output)


if __name__ == '__main__':
    unittest.main()
