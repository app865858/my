from django.shortcuts import render
import datetime

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'這裡是在MAIN.VIEW context like 顯示的字串', 'now':datetime.datetime.now()}
    return render(request, 'main/main.html', context)



def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')