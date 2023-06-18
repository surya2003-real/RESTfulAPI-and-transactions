# RESTfulAPI and transactions
## I have built a fully functional RESTful API using Django.

### First activate the django environment using `django_env/Scripts/activate` and then 'cd restapi'.
### When you launch the website using `py manage.py runsever` you can have a GUI to interact with the backend functionalities.

### This site enables you to faciltate transaction between the users.


|Endpoint|What it Does|
|---|---|
|https://localhost:8000/admin/|Opens admin page|
|https://localhost:8000/|POST request to create new users|
|https://localhost:8000/showusers/|GET request to view all registered users|
|https://localhost:8000/profile/|GET, PUT the profile of active user|
|https://localhost:8000/profile/pk|GET request to view a registered user using a primary key (pk is primary key, it is the user id)
|https://localhost:8000/dElEtE/| DELETE all users|
|https://localhost:8000/dElEtE/pk|DELETE user with given primary key (pk is primary key, it is the user id)|
|https://localhost:8000/login/| GET request to login|
|https://localhost:8000/logout/| GET request to logout|
|https://localhost:8000/transactions/|GET request to view all transactions|
|https://localhost:8000/transactions/pk/|GET request to view a particular transaction using transaction id(pk is primary key, it is the transaction id)|
|https://localhost:8000/transactions/new/|POST request to create transactions|

>1. Only user who is logged in can make transactions.  
>2. Also only logged in user can update his profile.  
>3. Beware of delete commands once used it will not even ask for confirmation and permanently delete data.(therefore it has been kept difficult to write)
