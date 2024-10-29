from django.shortcuts import render
import datetime 
# Create your views here.
def home(request):
    d = {'name' : 'samin', 'age' : 10, 'list' : [1,2,3,4,5,7,8,9,16], 'birthday': datetime.datetime.now() ,'courses': [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 9000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'c',
            'fee' : 3000
        }
    ]}
    return render(request, 'home.html', d)