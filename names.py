students = {
	'names': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
	]
}

for key, data in students.items():
     #print data
     for value in data:
		 print value["first_name"], value["last_name"]
