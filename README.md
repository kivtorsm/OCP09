# OCP09 : LITReview

Projet OpenClassrooms - Programme développeur d'applications Python

**Objectif** : Commercialise product allowing a community to ask for reviews of books on demand

## Functions
- Sign-up
- Log-in, log-out
- Feed
- Read, update, delete own posts (Tickets or reviews)
- Create ticket
- Create review
- Follow or unfollow users
- Read followers or users followed

## Installing and running

### 1. Install Software requirements
- Install Python 3.11+

### 2. Create Python project environment
1. In your terminal/IDLE, position yourself in the directory where you want
to create your project folder
    > $ cd *//path//*
2. Create your project folder
    > $ mkdir *Project_Name*
3. Create your project environment
    > $ python -m venv env

### 3. Activate virtual environment
- From your project folder (this commande may change depending on your OS):
    > $ ./env/Scripts/activate

### 4. Install Pyhton packages
- From your terminal or IDLE, install all packages listed in requirements.txt
    > $ pip install -r requirements.txt

### 5. Create database
- From your terminal or IDLE, from the manage.py location folder, migrate DB:
    > $ python manage.py migrate

### 6. Run Server
- From your terminal or IDLE, from the manage.py location folder, migrate DB:
    > $ python manage.py runserver

### 7. Launch app
- Go to your web browser and launch the ip address provided by your terminal or IDLe:
    > https//:127.0.0.1:8000/home

## Test Data
### URLs
| Page  | URL                          |
|-------|------------------------------|
| Home  | http://127.0.0.1:8000/home/  |
| Admin | http://127.0.0.1:8000/admin/ |

### Users
| Log-in   | Password       | Role      |
|----------|----------------|-----------|
| admin-oc | ocp09litreview | Superuser |
| toto     | ocp09litreview | user      |
| coco     | ocp09litreview | user      |
| momo     | ocp09litreview | user      |

### Database
Initialised data in `db.sqlite3`

### Media
All attached images are saved to the `/media/` folder 

