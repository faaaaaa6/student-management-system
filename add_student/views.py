from django.shortcuts import render
from .models import Student

def add_student(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        phone = request.POST['phone']
        
        

        Student.object.create(
            
            name=name,
            age=age,
            email=email,
            phone=phone
          

        )
    
    return render(request,"add_student.html")