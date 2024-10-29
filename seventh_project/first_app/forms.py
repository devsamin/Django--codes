from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels  = {
            'name' : 'Student name',
            'roll' : 'Student roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-danger'})
        }
        help_texts = {
            'name' : 'Enter your full name'
        }
        error_messages = {
            'name' : {'required': 'Enter your name'}
        }