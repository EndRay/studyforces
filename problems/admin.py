from django.contrib import admin

# Register your models here.
from problems.models import Problem, Tag


class TagsInline(admin.StackedInline):
    model = Tag
    extra = 3


class ProblemAdmin(admin.ModelAdmin):
    fields = ['name', 'statement']
    inlines = [TagsInline]


admin.site.register(Problem, ProblemAdmin)
