# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'coursesapp/index.html', {'all_courses': courses})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        if len(name) > 5 and len(desc) >15:
            new_course = Course.objects.create(name = name)
            Description.objects.create(desc = desc, course = new_course)
            return redirect("/courses")
            
    return redirect("/courses")

def destroy(request, course_id):
    if request.method == 'GET':
        the_course = Course.objects.get(id = course_id)
        return render(request, 'coursesapp/destroy.html', {'the_course':the_course})

    elif request.method == 'POST':
        the_course = Course.objects.get(id = course_id)
        the_course.description.delete()
        the_course.delete()
        return redirect('/courses')

def comment(request, course_id):
    if request.method == 'GET':
        the_course = Course.objects.get(id = course_id)
        comments = the_course.comments.all()
        return render(request, 'coursesapp/comment.html', {'the_course':the_course, 'comments':comments})

    elif request.method == 'POST':
        comment = request.POST['comment']
        Comment.objects.create(comment = comment, course = Course.objects.get(id = course_id))        
        return redirect('/courses/comment/{}'.format(course_id))