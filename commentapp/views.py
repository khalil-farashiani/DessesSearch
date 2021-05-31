from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as loginn, authenticate
from django.contrib.auth.forms import UserCreationForm
import json
import xlsxwriter
import mimetypes
import os

from .forms import CommentForm

def CommentFormPost(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_comment = form.save()
            new_comment.save()
            return HttpResponse('thanks for your comment')

    else:
        form = CommentForm()

    return render(request, 'commentapp/proj/home.html', {'form': form})


def tools(request):
    
    return render(request, 'commentapp/proj/tools.html')

def login(request):
    
    return render(request, 'commentapp/proj/login.html')

def signupp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            loginn(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'commentapp/proj/sing up.html', {'form': form})

def Edu(request):
    
    return render(request, 'commentapp/proj/Educational concepts.html')

def forget(request):
    
    return render(request, 'commentapp/proj/forget pass.html')



def search(request):
    q = request.GET.get('q')
    print(q)
    f = open('database.json', 'r')

    for i in f:
        if q in i:
            i = i.strip("""\n\t""")
            i = i.strip()
            j = i.split(sep='"')
            x = j[3]
            y = x.split(' ')
            z = y[0]
            y.pop(0)
            y.pop(0)
            y = ' '.join(y)
            print(z)
            print(y)
            workbook = xlsxwriter.Workbook(f'{z}.xlsx')
            worksheet = workbook.add_worksheet()
            row = 0
            col = 0
            worksheet.write(row, col, 'name')
            worksheet.write(row, col+1, 'code')
            worksheet.write(row, col+2, 'more enformation')
            worksheet.write(row+1, col, y)
            worksheet.write(row+1, col+1, z)
            worksheet.write(row+1, col+2, 'https://www.kegg.jp/entry'+y)
            workbook.close()
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # BASE_DIR2 = os.path.join(BASE_DIR, 'commentapp')
            fl_path = BASE_DIR+f'/{z}.xlsx'
            filename = z+'.xlsx'
            fl = open(fl_path, 'rb').read()
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
    return HttpResponse('this isnt a valid value for search try again')



def download_file(request):
    # fill these variables with real values
    fl_path = ''
    filename = 'downloaded_file_name.extension'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response