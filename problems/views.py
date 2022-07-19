from django.shortcuts import render, get_object_or_404, get_list_or_404

from problems.models import Problem, Tag


def details(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    tags = Tag.objects.all().filter(problem=problem)
    return render(request, 'problems/details.html', {'problem': problem, 'tags':tags})