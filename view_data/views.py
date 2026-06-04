from django.shortcuts import render
from add_student.models import Student 

def view_data(request):
    students = Student.objects.all()

    return render(
        request,
        "view_data.html",
        {"students": students}
    )

