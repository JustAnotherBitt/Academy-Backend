from typing import Optional
from ninja import ModelSchema, Schema
from .models import Students

class StudentsSchema(ModelSchema):
    class Meta:
        model = Students
        fields = ['name', 'email', 'belt', 'birth_date']
        
class UpdateStudentSchema(Schema):
    name: Optional[str] = None
    email: Optional[str] = None
    belt: Optional[str] = None
    birth_date: Optional[str] = None

class DeleteStudentSchema(Schema):
    message: str

class StudentProgressSchema(Schema):
    email: str
    name: str
    belt: str
    total_lessons: int
    required_classes_for_next_belt: int
    
class CompletedLessonSchema(Schema):
    qtd: Optional[int] = 1
    email_student: str
