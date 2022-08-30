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