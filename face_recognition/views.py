import base64

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.base import ContentFile
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
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            class_name = request.POST.get('class')
            speciality = request.POST.get('speciality')
            image_data = request.POST.get('image')

            # Process the base64 image
            if image_data:
                # Remove the data:image/jpeg;base64, prefix if present
                if 'base64,' in image_data:
                    image_data = image_data.split('base64,')[1]

                # Convert base64 to image file
                image_content = ContentFile(base64.b64decode(image_data))

                # Create student instance
                student = Student(
                    name=name,
                    email=email,
                    phone=phone,
                    class_name=class_name,
                    speciality=speciality,
                )

                # Save the image
                student.photo.save(f"{email}_photo.jpg", image_content, save=False)
                student.save()

                return redirect('face_recognition:index')
            else:
                error_message = "Photo is required"
                return render(request, 'face_recognition/student_registration.html',
                              {'error_message': error_message})

        except Exception as e:
            error_message = str(e)
            return render(request, 'face_recognition/student_registration.html',
                          {'error_message': error_message})

    return render(request, 'face_recognition/student_registration.html')

def student_list(request):
    # Get unauthorized students only
    students = Student.objects.filter(authorized=False)
    return render(request, 'face_recognition/student_list.html', {'students': students})


def authorize_student(request, student_id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=student_id)
            # Toggle the authorized status
            student.authorized = not student.authorized
            student.save()

            action = "authorized" if student.authorized else "revoked authorization for"
            messages.success(request, f'Successfully {action} {student.name}')
        except Student.DoesNotExist:
            messages.error(request, 'Student not found.')

    return redirect('face_recognition:student_list')

def mark_attendance(request):
    return render(request, 'face_recognition/mark_attendance.html')

def attendance_details(request):
    return render(request, 'face_recognition/attendance_details.html')
