from django.shortcuts import render
from maheshapp.forms import FeedBackForm

# Create your views here.
def feedback_view(request):
    form=FeedBackForm()
    submitted=False
    name=''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print("From validation success and printing feedback information")
            print("*"*50)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('MailID:',form.cleaned_data['email'])
            print('password:',form.cleaned_data['password'])
            print('rpassword:',form.cleaned_data['Rpassword'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']
    return render(request,'mahiapp/feedback.html',{'form':form,'submitted':submitted,'name':name})