
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],

 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
	n=0
	print "\n %s" %(key.title())
	#print data

	for value in data:
		n += 1
		name = value["first_name"].upper() +" "+ value["last_name"].upper()
		count = len(value["first_name"]) + len(value["last_name"])

		print "%d - %s - %d" %(n, name, count)
