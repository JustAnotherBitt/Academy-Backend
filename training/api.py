from datetime import date
from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError
from .schemas import StudentProgressSchema, StudentsSchema, CompletedLessonSchema
from .graduation import *
from .models import Students, CompletedLessons

training_router = Router()

@training_router.post('/', response={200: StudentsSchema})
def create_student(request, student_schema: StudentsSchema):
    name = student_schema.dict()['name']
    email = student_schema.dict()['email']
    belt = student_schema.dict()['belt']
    birth_date = student_schema.dict()['birth_date']

    # Checks if there is a student registered with the same email
    if Students.objects.filter(email=email).exists():
        raise HttpError(400, "Email already registered.")

    student = Students(name=name, email=email, belt=belt, birth_date=birth_date)
    student.save()
    
    return student

@training_router.get('/students/', response=List[StudentsSchema])
def list_students(request):
    students = Students.objects.all()
    return students

@training_router.get('/student_progress/', response={200: StudentProgressSchema})
def student_progress(request, student_email: str):
    student = Students.objects.get(email=student_email)
    
    total_completed_lessons = CompletedLessons.objects.filter(student=student).count()

    current_belt = student.get_belt_display()
    
    n = order_belt.get(current_belt, 0)
  
    total_lessons_next_belt = calculate_lessons_to_upgrade(n)

    total_completed_lessons_current_belt = CompletedLessons.objects.filter(student=student, current_belt=student.belt).count()

    remaining_lessons = max(total_lessons_next_belt - total_completed_lessons_current_belt, 0)

    return {
        "email": student.email,
        "name": student.name,
        "belt": current_belt,
        "total_lessons": total_completed_lessons_current_belt,
        "required_classes_for_next_belt": remaining_lessons
    }
    
@training_router.post('/completed_lesson/', response={200: str})
def completed_lesson(request, completed_lesson: CompletedLessonSchema):
    qtd = completed_lesson.qtd 
    email_student = completed_lesson.email_student 
    
    if qtd <= 0:
        raise HttpError(400, "Lessons quantity must be greater than zero")

    student = Students.objects.get(email=email_student)
    
    for _ in range(0, qtd):
        cl = CompletedLessons(
            student=student,
            current_belt=student.belt
        )
        cl.save()
    
    return 200, f"Class marked as completed for the student {student.name}"

@training_router.put("/students/{student_id}", response=StudentsSchema)
def update_student(request, student_id: int, student_data: StudentsSchema):
    student = get_object_or_404(Students, id=student_id)
    
    # Checks whether the student is the appropriate age for the belt
    age = date.today() - student.birth_date

    if int(age.days/365) < 18 and student_data.dict()['belt'] in ('B', 'P', 'Br', 'Bl'):
        raise HttpError(400, "The student is underage and cannot be promoted to this belt.")

    # It can be also exclude_unset=True
    for attr, value in student_data.dict().items():
        if value:
            setattr(student, attr, value)
    
    student.save()
    return student
