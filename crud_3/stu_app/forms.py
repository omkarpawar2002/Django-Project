from django import forms
from .models import Student

gender_choice = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER'),
]

subject_choices = [
    ('PHYSICS','PHYSICS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('MATHS','MATHS'),
    ('ZOOLOGY','ZOOLOGY'),
    ('IT','IT'),
    ('CS','CS')
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'stu_id':'STUDENT ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'gender':'GENDER',
            'mobile':'MOBILE NO',
            'subject':'SUBJECTS',
            'city':'CITY',
            'address':'ADDRESS',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'stu_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101',
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'gender':forms.RadioSelect(choices=gender_choice),
            'mobile':forms.TextInput(attrs={
                'placeholder':'+91 ***** *****'
            }),
            'subjects':forms.Select(choices=subject_choices),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g.,Pune',
            }),
            'address':forms.Textarea(attrs={
                'rows':'3',
                'placeholder':'E.g.,Mumbai, Maharashtra',
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com',
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })

        }
