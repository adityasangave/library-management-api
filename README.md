# library-management-api
An api which lets you manage library transaction built with fastapi

### How to Use
1. Clone the repository
2. Activate virtual environment
3. Install Dependencies using

```
poetry install
```
4. Run the server

```
poetry run uvicorn main:app --reload
```

### Tables Structure

![alt text](https://github.com/adii21-Ux/library-management-api/blob/master/schema.png)

### Directory Structure

```
.
|
|___database.py
|___main.py
|___models.py
|___schemas.py
```

1. Database.py : Contains functions to create database connection.
2. main.py : Contains routes and controllers for API
3. models.py : Contains database tables
4. schemas.py : Database tables structure and fields type to verify data
