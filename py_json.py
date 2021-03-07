#json is commonly used with data APIS . here we can parse json into  python dictionary

import json 

#sample json
userJSON = '{"first_name": "John", "last_name": "Doe", "Age": 30}'

#parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)

