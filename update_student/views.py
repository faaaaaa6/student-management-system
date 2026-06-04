from django.shortcuts import render,get_object_or_404,redirect
from add_student.models import Student

def update_student(request,pk):
    student = get_object_or_404(Student,pk=pk)

    if request.method =='POST':
        name = request.POST['name']
        age = request.POST["age"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        course= request.POST["course"]

        student.name = name
        student.age = age
        student.email = email
        student.phone = phone
        student.course = course

        student.save()

        return redirect('view_data')
    else:
        return render(request, "update_student.html",{"student":student})

  

