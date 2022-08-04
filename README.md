<h1 align="center">
📄<br>VetClinic Database Challenge
</h1>

## Data Engineering Challenge #1: SQL and Python

[![Repositório](https://img.shields.io/badge/repositório%20-%23323330.svg?&style=for-the-badge&logo=repositório&logoColor=black&color=8000FF)](https://github.com/lucca-miorelli/vetclinic-database)

---

## 👩‍💻 What to do?
### PART 1: DATABASE NORMALIZATION
* Get *vetclinic_procedures.parquet* in *data* folder
* Normalize the dataset into how many tables you feel right.
* Create a database (and store the credentials in a .env file).
* Create tables with all constraints necessary.
* Upload tables into database.

### PART 2: CREATING AND USING VIEWS
A view is a "virtual table" that ease the search in the database and avoid super-long queries. Also, it can help protects sensitive data from others users in the database. See [*how to create a view in PostgreSQL*](https://www.postgresql.org/docs/9.2/sql-createview.html).<br>
Postgres also has *materialized views*, which differ in quite a few concepts from standard *views*, as can be seen in this [article](https://medium.com/analytics-vidhya/materialized-view-vs-view-in-postgresql-1ddb4fe86cb7).<br>

* Create a view named *send_giftcard* that shows:
  * Full procedures history.
  * The price of the procedure.
  * The name and kind of the pet.
  * The full name and the zipcode of the owner.
* Query the view with these requirements:
  * petname, petkind, owner_fullname, zipcode
  * Only with procedures realized in december.
