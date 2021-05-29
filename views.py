from django.shortcuts import render
from App1.form import StudentForm
IMAGE_FILE_TYPES=['png','jpeg','jpg','jfif']


# Create your views here.
def create(request):
	obj=StudentForm()

	if request.method=='POST':
		obj=StudentForm(request.POST,request.FILES)

		if obj.is_valid():
			obj=obj.save(commit=False)

			obj.profile_picture=request.FILES['profile_picture']

			#myphoto.png,myphoto.pdf
			file_type=obj.profile_picture.url.split('.')[-1]
			file_type=file_type.lower()

			if file_type in IMAGE_FILE_TYPES:
				obj.save()

				return render(request,'details.html',{'student':obj})
			else:
				return render(request,'error.html')
	context={'form':obj}
	return render(request,'create.html',context)

def index(request):
	return render(request,'index.html')
	
#def login(request):
	#return render(request,'login.html')

def details(request):
	return render(request,'details.html')



# Create your views here.
