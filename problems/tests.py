import string
import random

from django.test import TestCase
from django.urls import reverse

from problems.models import Problem, Tag


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    print(result_str)


def create_mock_problem():
    return Problem.objects.create(name='get_random_string(10)', statement='get_random_string(100)')


# class ProblemModelTests(TestCase):
#     def test_simple_problem_test(self):
#         pass


class DetailView(TestCase):
    def test_no_problem(self):
        url = reverse('problems:details', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_simple_problem_no_tags(self):
        problem = create_mock_problem()
        url = reverse('problems:details', args=(problem.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_simple_problem(self):
        problem = create_mock_problem()
        tag = Tag.objects.create(problem=problem)
        url = reverse('problems:details', args=(problem.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
