from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm
from .models import Student, Attendance


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'students/register_student.html', {'form': form})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    attendance = Attendance.objects.filter(student=student).order_by('date')
    return render(request, 'students/student_detail.html', {'student': student, 'attendance': attendance})


def student_attendance(request, pk):
    student = get_object_or_404(Student, pk)
    if request.method == 'POST':
        date = request.POST.get('date')
        is_present = request.POST.get('is_present') == 'on'
        attendance = Attendance.objects.filter(student=student, date=date, is_present=is_present)
        attendance.save()
        return redirect('student_detail', pk=pk)
    else:
        return render(request, 'students/student_attendance.html', {'student': student})
