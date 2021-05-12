import json
sv_infor = {
    "name":"aaaaaa",
    "email":"aaaa@aaa.com",
    "age": None,
    "gender":"Nam",
    "school":"Phan Chau Trinh"
}

data = json.dumps(sv_infor)
print (data)