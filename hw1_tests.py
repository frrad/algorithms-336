import unittest
import hw1


class TestStringMethods(unittest.TestCase):

    def test_example(self):
        hospital_rankings = [[0, 1, 2], [2, 1, 0]]
        hospital_capacities = [1, 1]
        student_rankings = [[0, 1], [0, 1], [1, 0]]

        expected_output = [[0], [2]]
        output = hw1.stable_matching(
            hospital_rankings, hospital_capacities, student_rankings)

        self.assertTrue(
            consistent(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            first_kind(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            second_kind(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertEqual(output, expected_output)

    def test_trickier(self):
        hospital_rankings = [[0, 1, 2], [0, 1, 2]]
        hospital_capacities = [1, 1]
        student_rankings = [[0, 1], [0, 1], [0, 1]]

        expected_output = [[0], [1]]
        output = hw1.stable_matching(
            hospital_rankings, hospital_capacities, student_rankings)

        self.assertTrue(
            consistent(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            first_kind(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            second_kind(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertEqual(output, expected_output)


def consistent(hospital_rankings, hospital_capacities, student_rankings, output):
    assigned_students = set()

    for i,  choice in enumerate(output):
        if len(choice) != hospital_capacities[i]:
            return False
        x, y = len(assigned_students), len(choice)
        assigned_students |= set(choice)
        if len(assigned_students) != x + y:
            return False

    return True


def first_kind(hospital_rankings, hospital_capacities, student_rankings, output):
    assigned_students = set()

    for choice in output:
        assigned_students |= set(choice)

    unassigned_students = set(range(len(student_rankings))) - assigned_students

    for i, preference in enumerate(hospital_rankings):

        choice = output[i]  # which students were chosen by hospital i
        capacity = hospital_capacities[i]

        for student in preference:
            if student in choice:
                capacity -= 1
            if student in unassigned_students and capacity > 0:
                return False

    return True


def second_kind(hospital_rankings, hospital_capacities, student_rankings, output):
    assigned_students = set()

    for choice in output:
        assigned_students |= set(choice)

    student_assignments = dict()
    for i, choice in enumerate(output):
        for student in choice:
            if student in student_assignments:
                return False
            student_assignments[student] = i

    for i, preference in enumerate(hospital_rankings):
        choice = output[i]  # which students were chosen by hospital i
        capacity = hospital_capacities[i]

        for student in preference:
            if student in choice:
                capacity -= 1
            if student in assigned_students and capacity > 0:
                student_ranking = student_rankings[student]
                if student_ranking.index(i) < student_ranking.index(student_assignments[student]):
                    return False

    return True


if __name__ == '__main__':
    unittest.main()
