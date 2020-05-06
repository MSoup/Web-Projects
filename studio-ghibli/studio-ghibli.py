import argparse
import requests

#Set up -d as possible argument
parser = argparse.ArgumentParser(description='Get Ghibli Films')

parser.add_argument('-d', dest='d',action='store_true',help='Enable -d to show directors with films')

args = parser.parse_args()

#Requests to access API
response = requests.get('https://ghibliapi.herokuapp.com/films')

x = response.json()

if args.d:
  for i in range(len(x)):
    print(f'{x[i]["title"]} - {x[i]["director"]}')
else:
  for i in range(len(x)):
    print(x[i]['title'])
