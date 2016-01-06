from django import forms
from kerimealbayrak.models import teacher
from kerimealbayrak.models import student
from kerimealbayrak.models import course



class student_teacher_ChoiceField(forms.ModelChoiceField): #http://stackoverflow.com/questions/3167824/change-django-modelchoicefield-to-show-users-full-names-rather-than-usernames
     def label_from_instance(self, obj):
         return "%s %s" % (obj.firstname, obj.lastname)


class CourseMultiChoice(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.code, obj.name)


class StudentForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()


class TeacherForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    office = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()


class CourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=100)
    classroom = forms.CharField(max_length=100)
    time = forms.CharField(max_length=100)
    teacher = student_teacher_ChoiceField(queryset=teacher.objects.all())


class EnrollStudents(forms.Form):
    student = student_teacher_ChoiceField(queryset=student.objects.all())
    course = CourseMultiChoice(queryset=course.objects.all())
