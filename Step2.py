import requests
import csv

# request data
url = "http://localhost:8000/api/worker-list/"
data = requests.get(url).json()
print(data)

# open file
csvfile = open('step2.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=',')

# write keys
k = list(data[0].keys())
writer.writerow(k)

# write data
for d in data:
    writer.writerow(list(d.values()))

csvfile.close()


