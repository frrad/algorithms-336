import unittest
import hw1
import random
from copy import deepcopy


class TestStringMethods(unittest.TestCase):

    def test_example(self):
        hospital_rankings = [[0, 1, 2], [2, 1, 0]]
        hospital_capacities = [1, 1]
        student_rankings = [[0, 1], [0, 1], [1, 0]]

        self.execute_test(
            hospital_rankings, hospital_capacities, student_rankings)

    def test_trickier(self):
        hospital_rankings = [[0, 1, 2], [0, 1, 2]]
        hospital_capacities = [1, 1]
        student_rankings = [[0, 1], [0, 1], [0, 1]]

        self.execute_test(
            hospital_rankings, hospital_capacities, student_rankings)

    def test_big(self):
        hospital_rankings = [[5, 7, 2, 0, 6, 1, 4, 3], [5, 1, 3, 4, 0, 6, 2, 7], [
            7, 1, 5, 3, 2, 4, 0, 6], [2, 3, 7, 5, 1, 4, 0, 6], [1, 6, 3, 2, 7, 4, 0, 5]]
        hospital_capacities = [1, 2, 3, 1, 1]
        student_rankings = [[1, 0, 3, 2, 4], [1, 4, 3, 2, 0], [3, 0, 1, 4, 2], [
            0, 4, 1, 2, 3], [1, 2, 0, 3, 4], [4, 1, 0, 3, 2], [3, 0, 2, 1, 4], [1, 4, 0, 2, 3]]

        self.execute_test(
            hospital_rankings, hospital_capacities, student_rankings)

    def test_random(self):
        for i in xrange(100):
            hospital_rankings, hospital_capacities, student_rankings = random_instance()
            self.execute_test(
                hospital_rankings, hospital_capacities, student_rankings)

    def execute_test(self, hospital_rankings, hospital_capacities, student_rankings):
        output = hw1.stable_matching(deepcopy(hospital_rankings), deepcopy(
            hospital_capacities), deepcopy(student_rankings))

        self.assertTrue(
            consistent(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            first_kind(hospital_rankings, hospital_capacities, student_rankings, output))
        self.assertTrue(
            second_kind(hospital_rankings, hospital_capacities, student_rankings, output))


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


def random_instance():
    x, num_hospitals = 3, 5
    capacities = [random.randint(1, x) for i in xrange(num_hospitals)]
    slots = sum(capacities)
    num_students = random.randint(slots, 2 * slots)

    hospital_rankings = []
    for i in xrange(num_hospitals):
        rank = range(num_students)
        random.shuffle(rank)
        hospital_rankings.append(rank)

    student_rankings = []
    for i in xrange(num_students):
        rank = range(num_hospitals)
        random.shuffle(rank)
        student_rankings.append(rank)

    return hospital_rankings, capacities, student_rankings


if __name__ == '__main__':
    unittest.main()
