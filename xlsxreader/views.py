import os
from django.shortcuts import render, HttpResponseRedirect
from .forms import ExcelUpload
from .models import ExcelFileUpload
import pandas as pd

# def read_file(filename, **kwargs):
#     """Read file with **kwargs; files supported: xls, xlsx, csv, csv.gz, pkl"""
#     read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
#                 'gz': pd.read_csv, 'pkl': pd.read_pickle}
#     ext = os.path.splitext(filename)[1].lower()[1:]
#     assert ext in read_map, "Input file not in correct format, must be xls, xlsx, csv, csv.gz, pkl; current format '{0}'".format(ext)
#     assert os.path.isfile(filename), "File Not Found Exception '{0}'.".format(filename)
#     return read_map[ext](filename, **kwargs)

def home(request):
    template = 'home.html'
    form = ExcelUpload(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            excelfile = ExcelFileUpload(uploaded_file = request.FILES['uploaded_file'])
            excelfile.save()

            print(excelfile.uploaded_file.url)
            print(excelfile.uploaded_file.path)
            data = pd.read_excel(excelfile.uploaded_file.path)
            data_to_html = data.to_html
            return render(request, template, {'form':form, 'data_to_html':data_to_html})
    else:
        form = ExcelUpload()
    return render(request, template, {'form': form})

