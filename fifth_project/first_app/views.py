from django.shortcuts import render
from .forms import ContactForm , StudentData, PasswordValidationProject
# Create your views here.
def home(request):
    return render(request, './first_app/home.html')
def about(request):
    print(request.POST)
    if request.method == 'POST':

        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name' : name,'email' : email, 'select' : select})
    else:
         return render(request, './first_app/about.html')
def form(request):
    
        return render(request, './first_app/form.html')
def djangoform(request):
     if request.method == 'POST':
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            print(Form.cleaned_data)
            # file = Form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as distination:
            #      for chunk in file.chunks():
            #           distination.write(chunk)
            
        else:
             print("Form is not valid")
     else:
          Form = ContactForm()
     return render(request, "./first_app/djangoform.html" ,{'Form' : Form})

def student_form(request):
     if request.method == 'POST':
          form = StudentData(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
            
          else:
                print('Form is not valid')
     else:
        form = StudentData()
     return render(request, "./first_app/djangoform.html" ,{'Form': form})
def PasswordValidation(request):
     if request.method == 'POST':
          form = PasswordValidationProject(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
            
          else:
                print('Form is not valid')
     else:
        form = PasswordValidationProject()
     return render(request, "./first_app/djangoform.html" ,{'Form': form})