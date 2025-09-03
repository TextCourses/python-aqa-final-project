## Running the Application

Install PostgreSQL 16:
- Windows: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- Linux: 
```
sudo apt update 
sudo apt install -y postgresql-16
sudo pg_ctlcluster 16 main start
```

Alter user postgres in postgres command line:
```
ALTER USER postgres WITH PASSWORD 'postgres';
```

Create database for application:
```
CREATE DATABASE django_rest;
```

Create .env file in project root dir and add row:
```
POSTGRES_PASSWORD = "postgres"
```

Install python requirements:
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