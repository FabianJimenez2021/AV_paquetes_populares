import requests

#get
# url = ("https://jsonplaceholder.typicode.com/users")

# r = requests.get(url, timeout=10)

# r = r.json()

# for user in r:
#     print(user["name"])

# url = ("https://jsonplaceholder.typicode.com/users/1")
# r = requests.get(url, timeout=10)
# print(r.json())

#post 
#Para crear no se necesita indicar en la url
# url = ("https://jsonplaceholder.typicode.com/users")
# user = {
#     "id":11,
#     "name":"Guarumo el perro marihuano"
# }
# r = requests.post(url, timeout=10, data=user)
# print(r)

#put y patch 
#se necesita indicar dentro de la url lo que se va a actualizar

# url = ("https://jsonplaceholder.typicode.com/users/11")
# user = {
#     "name":"el perro marihuano"
# }
# r = requests.put(url, timeout=10, data=user)
# print(r)

#delete

url = ("https://jsonplaceholder.typicode.com/users/11")
user = {
    "name":"el perro marihuano"
}
r = requests.delete(url, timeout=10, data=user)
print(r)
