from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WorkerSerializer
from .models import Worker
import datetime
import time
import random
import csv
import os

data = [
	{
		"worker_id": 0,
		"worker_name": "p2_pc",
		"cpu_usage": 0,
		"ram": 0.01,
		"vmem": 0.0,
		"gpu": "GeForce RTX 2070, not used"
	},
	{
		"worker_id": 1,
		"worker_name": "p1_01",
		"cpu_usage": 3,
		"ram": 0.17,
		"vmem": 0.13,
		"gpu": "GeForce RTX 2070, not used"
	},
	{
		"worker_id": 2,
		"worker_name": "p2_00",
		"cpu_usage": 32,
		"ram": 0.03,
		"vmem": 0.1,
		"gpu": "GeForce RTX 2080 Ti, not used"
	},
	{
		"worker_id": 5,
		"worker_name": "filecoin",
		"cpu_usage": 48,
		"ram": 0.13,
		"vmem": 0.43,
		"gpu": "GeForce RTX 1080 Ti, not used"
	}
]

def SAVE2CSV():
	
	f = os.path.isfile('record.csv')

	# If file does not exist, write the title into the file at first time
	if not f:
		csvfile = open('record.csv', 'a', newline='')
		writer = csv.writer(csvfile, delimiter=',')
		k = ['time'] + list(data[0].keys())
		writer.writerow(k)
		for d in data:
			writer.writerow([datetime.datetime.now()] + list(d.values()))
	else:
		csvfile = open('record.csv', 'a', newline='')
		writer = csv.writer(csvfile, delimiter=',')
		for d in data:
			writer.writerow([datetime.datetime.now()] + list(d.values()))

	csvfile.close()
	return

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/worker-list/',
		}

	return Response(api_urls)
    
@api_view(['GET'])
def workerList(request):
	SAVE2CSV()
	
	d={}
	d['admin_id'] = round(random.random()*10)
	d['call_date'] = datetime.date.today()
	d['call_time'] = time.strftime("%H:%M:%S")
	d['result'] = True

	serializer = WorkerSerializer(data=d)

	if serializer.is_valid():
		serializer.save()
	return Response(data)

