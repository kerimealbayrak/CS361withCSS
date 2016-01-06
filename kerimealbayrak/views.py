from kerimealbayrak.forms import *
from kerimealbayrak.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = student(firstname=form.cleaned_data["firstname"],
                        lastname=form.cleaned_data["lastname"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentForm()
        return render_to_response('addstudent.html', {'form': form}, RequestContext(request))


def students(request):
    return render_to_response('students.html',{'students': student.objects.all()})


def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = teacher(firstname=form.cleaned_data["firstname"],
                        lastname=form.cleaned_data["lastname"],
                        officedetails=form.cleaned_data["office"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeacherForm()
        return render_to_response('addteacher.html', {'form': form}, RequestContext(request))


def teachers(request):
    return render_to_response('teachers.html',{'teachers': teacher.objects.all()})

def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = course(name=form.cleaned_data["name"],
                        code=form.cleaned_data["code"],
                        classroom=form.cleaned_data["classroom"],
                        times=form.cleaned_data["time"],
                        teacher=form.cleaned_data["teacher"])
            a.save()
            return HttpResponseRedirect('/courses/')
    else:
        form = CourseForm()
        return render_to_response('addcourse.html', {'form': form}, RequestContext(request))


def courses(request):
    return render_to_response('courses.html',{'courses': course.objects.all()})


def studenttoclass(request):
    if request.method == 'POST':
        form = EnrollStudents(request.POST)
        if form.is_valid():
            form.cleaned_data["course"].student.add(form.cleaned_data["student"])

            return HttpResponseRedirect('/studentsatclass/'+str(form.cleaned_data["course"].id))
    else:
        form = EnrollStudents()
        return render_to_response('studenttoclass.html', {'form': form}, RequestContext(request))


def studentsatclass(request,id):
    return render_to_response('studentsatclass.html',{'course': course.objects.all().filter(id=id)[0], "students": student.objects.all()})
