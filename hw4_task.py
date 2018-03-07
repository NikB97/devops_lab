import argparse
import requests
import json
import getpass


parser = argparse.ArgumentParser() 
parser.add_argument("-p","--parsing", help="Includes parsing by  \"user_login\"  \"user_id\"  \"user_url\"  \"date_creation\"   \"date_pull\" ")
args = parser.parse_args()


#requested data for the user
print("Enter GitHub login:")
username = input()
password = getpass.getpass(prompt="Enter GitHub password:")
print("hint:    https://api.github.com/repos/__user__/__repositorie__/pulls")
print("Enter name of needed user:")
reponame = input()
print("Enter name of needed repositorie:")
repo = input()

#request to GitHub 
req_url= "https://api.github.com/repos/" + reponame + "/" + repo + "/pulls"
req = requests.get(req_url, auth=(username , password))

#receiving data
json_data=req.json()


#functions for parsing
if args.parsing == "user_login": 
	print("USER LOGIN:")
	max_count = len(json_data) 
	i = 0; 
	while i < max_count: 
		print("login" + ": " + str(json_data[i].get("head").get("user").get("login"))) 
		i += 1;


if args.parsing == "user_url":
	print("USER URL:")
	max_count = len(json_data)
	i = 0;
	while i < max_count:
		print("login   " + ": " + str(json_data[i].get("head").get("user").get("login")))
		print("user url" + ": " + str(json_data[i].get("head").get("user").get("url")))
		i += 1;


if args.parsing == "user_id":
	print("USER ID:")
	max_count = len(json_data)	
	i = 0;
	while i < max_count:
		print("login  " + ": " + str(json_data[i].get("head").get("user").get("login")))
		print("user id" + ": " + str(json_data[i].get("head").get("user").get("id")))
		i += 1;


if args.parsing == "date_creation":
	print("DATE OF CREATION:")
	max_count = len(json_data)
	i = 0;
	while i < max_count:
		print("date creation" + ": " + str(json_data[i].get("head").get("repo").get("created_at")))
		i += 1;


if args.parsing == "date_push":
	print("DATE OF PUSHING:")
	max_count = len(json_data)
	i = 0;
	while i < max_count:
		print("date of pushing" + ": " + str(json_data[i].get("head").get("repo").get("pushed_at")))
		i += 1;





