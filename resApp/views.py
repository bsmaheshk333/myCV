from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = UserForm()
        if request.method == 'POST':  # handling post data
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Registration Successful.' + user)
                return redirect('/login/')
        return render(request, 'registration.html', {'form': form})  # handling get method


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid login credential. Please Try Again!!')

        context = {}
        return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')  # in order to get to the home page you must validate your identity
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def export_pdf(request):
    from django.http import HttpResponse
    return HttpResponse("<h2>Downloading it is currently unavailable.</h2>")


"""
def export_pdf(request):
    # create a pdf buffer to receive a pdf data
    buffer = io.BytesIO()
    # now create an object for pdf using buffer as its file
    pdf = canvas.Canvas(buffer)

    # now put things in your pdf file
    pdf.drawString(10, 10, text="Hare krishna hare rama")

    # now close the pdf file with clean data
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='resume.pdf')
"""


