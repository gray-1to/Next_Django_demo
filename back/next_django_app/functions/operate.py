import csv
from http.client import HTTPResponse
from urllib import response
import csv
from django.http import HttpResponse  

def operate_file():
    csv_data = []
    for i in range(1,100,2):
        row = [i, i*100]
        csv_data.append(row)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="foo.csv"'
    writer = csv.writer(response)
    for row in csv_data:
        writer.writerow(row)

    return response

def operate_uploaded_file(uploaded_file):
    # csv_data = uploaded_file.tolist()
    csv_data = []
    for line in uploaded_file:
        try:
            line_list = str(line.decode()).split(",")
        except UnicodeDecodeError:
            line_list = str(line.decode('cp932')).split(",")
        
        csv_data.append(line_list)

    for i in range(1,100,2):
        row = [-i, -i*100]
        csv_data.append(row)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="foo.csv"'
    writer = csv.writer(response)
    for row in csv_data:
        writer.writerow(row)

    return response