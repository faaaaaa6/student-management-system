from django.shortcuts import redirect,get_object_or_404
from add_student.models import Student

def delete_student(request,pk):
    student = get_object_or_404(Student,pk=pk)  
    student.delete()
    return redirect("view_data")


