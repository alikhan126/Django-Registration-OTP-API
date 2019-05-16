Features:
---------
* User registration

* View user profile

* Send OTP 

* Verify OTP


API Documentation
-----------------

i. User - Registration
Create/ Register a new user.

	Endpoint 	: /api/accounts/register/
	Request Type 	: POST
	Request Params 	: username, email, password, password_2, first_name, last_name, invite_code
	Non-mandatory params : invite_code

	Response Http status codes : HTTP_200_OK or HTTP_400_BAD_REQUEST


ii. User - Login
Obtain authentication token given the user credentials.

	Endpoint 	: /api/accounts/login/
	Request Type 	: POST
	Request Params 	: email (or username) and password
	
	Response 	: { "token": <token> }
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
vi. User - Retrieve Profile
Retrieve logged in users profile.

	Endpoint 	: /api/accounts/user-profile/
	Request Type 	: GET
	Request Headers : 
		Authorization : Token <token>
	
	HTTP status code: HTTP_200_OK or HTTP_401_UNAUTHORISED
	
vi. Verificaton - Send OTP
Send OTP to given Phone Number.

	Endpoint 	: /api/verification/send_otp/
	Request Type 	: POST
	Request Headers : 
		Authorization : Token <token>
	
	HTTP status code: HTTP_200_OK or HTTP_401_UNAUTHORISED
	Response Sample : "OTP Sent"

vi. Verificaton - Verify OTP
Verify OTP from given input.

	Endpoint 	: /api/verification/send_otp/
	Request Type 	: POST
	Request Headers : 
		Authorization : Token <token>
	
	HTTP status code: HTTP_200_OK or HTTP_401_UNAUTHORISED
	Response Sample : "Congrats your phone number has been verified"
	

## Run the project Locally ##

i. Clone the repository.

ii. Go to directory of manage.py and install the requirements.

	pip install -r requirements.txt
	
**Note:**
You may configure the virtual environment if required.

For instructions, click here : https://virtualenv.pypa.io/en/latest/installation/
    
**Note:**
By default, Sqlite3 database is used. You may also use different database in local_settings file if required.

iv. Run migrations

	python manage.py migrate

v. Ready to run the server.

	python manage.py runserver
	

#### PASSWORD_MIN_LENGTH #### 

A constraint that defines minimum length of password. Defaulted to 6

#### INVITATION_VALIDITY_DAYS #### 

Validity (in days) of user team invitation email. Defaulted to 7


## Try it online: ##
https://dry-stream-50652.herokuapp.com/
	
	
