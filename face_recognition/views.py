from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages

from face_recognition.models import Student


def index(request):
    return render(request, 'face_recognition/index.html')


def student_registration(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            class_name = request.POST['class']
            speciality = request.POST['speciality']
            image = request.FILES.get('image')

            # Create new student
            student = Student.objects.create(
                name=name,
                email=email,
                phone_number=phone,
                class_name=class_name,
                speciality=speciality,
                image=image
            )
            messages.success(request, 'Student registered successfully!')
            return redirect('face_recognition:index')
        except Exception as e:
            messages.error(request, f'Error registering student: {str(e)}')

    return render(request, 'face_recognition/student_registration.html')
