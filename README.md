# Build a Site

## Resources

- Tutorial: [YouTube ePayMinds](https://www.youtube.com/watch?v=5bTvseLFkAo&list=PLV2_Iivd4jxYVDWCcxmccusNaUx2kWCg1)
- Source Codes: [GitHub](https://github.com/codingforentrepreneurs/eCommerce)

## Packages

### Global Level

- Python 3.7.2
- virturalenv 6.3.0

### Project Level

- Django 2.1.5
- mysqlclient: download `mysqlclient‑1.4.1‑cp37‑cp37m‑win_amd64.whl` from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
- pillow

## File System Structure

### Project Name:

- config

### Apps

- core
- common
- authentication
- users
- products

## Commands

### Create a Project

```shell
django-admin startproject config .
```

### Create the apps

```shell
python manage.py startapp core
python manage.py startapp common
python manage.py startapp authentication
python manage.py startapp users
python manage.py startapp products
```

### Make Migrations

```shell
python manage.py makemigrations
```

### Migrate

```shell
python manage.py migrate
```

### Dump Database Tables

```shell
python manage.py dumpdata auth.User --format json --indent 4 > texture/users.json
python manage.py dumpdata products.Product --format json --indent 4 > texture/products.json
```

### Seed Database Tables

```shell
python manage.py loaddata texture/users.json
python manage.py loaddata texture/products.json
```

## Templates

- Home Page: Bootstrap 4.2 jumbotron
- About Page: Bootstrap 4.2 album
- Contact Page: Bootstrap 4.2 checkout form
- Product List Page: Bootstrap 4.2 album
