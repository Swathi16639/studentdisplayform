from django import forms
from App1.models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		#fields='__all__'
		fields=[
		       'name',
		       'course',
		       'email',
		       'age',
		       'profile_picture',
		]