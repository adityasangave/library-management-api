# library-management-api
An api which lets you manage library transaction built with fastapi

### How to Use
1. Clone the repository
2. Activate virtual environment
3. 
```
poetry shell
```

4. Install Dependencies using

```
poetry install
```
5. Run the server

```
poetry run uvicorn main:app --reload
```
6. Access API at http://127.0.0.1:800/docs#/

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

### URL Routes
1. /issue/book/ : To see all the books which are issues
2. /issue/book/{rollNo}/{bookName} : To issue book to a student
3. /issue/book/{rollNo}/{bookName} :
4. /add/student/: Add new student
5. /all/student/ : Get all student information
6. /get/inventory/{bookName} : Get details of specific book
7. /get/inventory : Get all the books in inventory
8. /add/inventory/ : Add new book to inventory
9. /update/inventory/{bookname} : Update quantity of book in database
10. /get/popular-books/ : Get most popular book
