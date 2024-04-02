from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import UploadFileForm
from .models import Table
from django.db import connection
import random
import math


def index(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            with open('file.txt', 'r') as f:
                lines = [i.strip() for i in f.readlines() if isinstance(i, str)]
                if len(lines) < 50:
                    while len(lines) < 50:
                        slovo = random.choice(lines)
                        lines.append(slovo)


                
            wordDict = dict.fromkeys(set(lines), 0)
            for word in set(lines):
                wordDict[word] = lines.count(word)

            tfDict = {}
            
            idfDict = {}
            N = len(lines)
            for word, count in wordDict.items():
                tfDict[word] = count/float(len(lines))   

                doc_count = sum(1 for line in lines if word in line)
                idfDict[word] = math.log10(N / (float(doc_count) + 1))
                
                tf = tfDict[word]
                idf = idfDict[word]
                num = count
                Table.objects.create(word=word, tf=tf, idf=idf, count=num)

            print(lines)    
            return render(request, 'tb/table.html', {'form': form})
            
    else:
        truncate(Table)
        form = UploadFileForm()
        

    return render(request, 'tb/index.html', {'form': form})



def handle_uploaded_file(f):
    with open('file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
              
def truncate(model):
    model.objects.all().delete()       