import requests

payload =  {"email":"mail_sinh_vien"}
r = requests.get("http://localhost:5000/get", params=payload)