?Install required packages - pip install -r requirements.txt
?Edit database configuration details for postgreSQL database in settings.py
?Admin user cerdentials - username : admin, password : admin@123
?Run the server

ENDPOINTS
?http://127.0.0.1:8000/api/token/ - POST request
		
		Payload - {
????              "username":"admin",
???              ?"password":"admin@123"
　　　　　　　　　　　}
?http://127.0.0.1:8000/account/add_user/ - POST request
	
		 Payload - {
????					"username":"teacher6",
???					?"is_staff":true,
????					"is_superuser":false,
????					"email":"teacher6@gmail.com"
　　　}
?http://127.0.0.1:8000/account/forgot_password/ - POST request

		Payload - {
???					?"username":"teacher2"
　　　}
?http://127.0.0.1:8000/account/reset_password/ - POST request

		Payload - {
????					"code":"666787",
????					"username":"admin",
????					"new_password":"pass1",
????					"confirm_password":"pass1"
　　　}



?http://127.0.0.1:8000/account/add_student/ - POST request

		Payload - {
????					"username":"student6",
????					"email":"student1@gmail.com"
　　　}
?http://127.0.0.1:8000/account/profile/ - GET request

?http://127.0.0.1:8000/account/list_students/ - GET request

?http://127.0.0.1:8000/account/list_users/ - GET request



