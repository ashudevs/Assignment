# Assignment

1 : Clone this repository : git clone https://github.com/ashudevs/Assignment.git
2 : Make virtual environment in root directory : py -m venv "your env name"
3 : Activate your virtual env
4 : Install required modules : pip install -r requirements.txt
5 : Run the server : py manage.py runserver
6 : Login into admin pannel : 
     User : admin
     Password : admin
7 : Now you can run all the APIs

# SQL Queries
1 : Insert sample data into the "users" table. 
     INSERT INTO users (name, email, role)
     VALUES ('John Doe', 'john.doe@example.com', 'admin');

2 : Retrieve all users from the "users" table.
      select * from users;

3 : Retrieve a specific user by their ID.
      SELECT * FROM users WHERE id = 1;
