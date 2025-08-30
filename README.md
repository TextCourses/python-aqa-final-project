## Running the Application

Install requirements:
```
pip install -r requirements.txt
```
Create the DB tables first:
```
python app/manage.py migrate
```
Run the development web server:
```
python app/manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.