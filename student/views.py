from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student


def student_show(request):
    # x = []
    # for i in range(10):
    #     x.append(i)
    # return HttpResponse("<h1>Range Of 0 to 10</h1>The Digits are {0}".format(x))
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})

