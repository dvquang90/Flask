import requests as requests
import json as json

r=requests.post

data = {"name": "ten_sv",
        "age":30,
        "gender":"gioi_tinh",
        "email":"email_sv",
        "school":"truong_sv"}
with open("sv_infor.json", "w") as data:
    json.dump(data)
print (data)