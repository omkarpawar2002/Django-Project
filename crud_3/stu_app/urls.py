from django.urls import path
from .views import ( add_student,show_student,update_student,delete_student )

urlpatterns = [
    path('add_student/',add_student,name='Add_Student'),
    path('show_student/',show_student,name='Show_Student'),
    path('update_student/<int:pk>/',update_student,name='Update_Student'),
    path('delete_student/<int:pk>/',delete_student,name='Delete_Student')
]