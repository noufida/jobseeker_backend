# REST API- job portal
 This is sample rest api for web app which helps in streamlining the flow of job application process.  There are two end users (applicant,recruiter). Login session are persistent and REST APIs are securely protected by JWT token verification.
 After logging in, a recruiter can create/read/delete/update jobs, shortlist/accept/reject applications, view resume and edit profile. And, an applicant can view jobs, perform search and apply various filters, apply for jobs,save jobs, view status of job applications, add qualificaitons, experiences, skills, upload resume and edit profile.
 Admin can analyse the sales and analyse the jobs, restrict users, check and approve/reject applied companies, create/read/upadate/delete subsciption plans,job locations, categories.


## Live Demonstration

Base url for api: https://seeker.savebox.ae


## Getting started
To get started you can simply clone this jobseeker_backend repository and install the dependencies.

Clone the ecommerce-demo repository using git:
```python
git clone https://github.com/noufida/jobseeker_backend.git
cd jobseeker_backend
```
Create a virtual environment to install dependencies in and activate it:
```python
python3 -m venv env
source env/bin/activate
```

Then install the dependencies:
```python
(env)$ pip install -r requirement.txt
```
Note the ```(env)``` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once ```pip``` has finished downloading the dependencies:
```python
(env)$ cd jobseeker_backend
(env)$ python3 manage.py runserver
```
And navigate to ```http://127.0.0.1:8000/```


## Tech Stack

  Python
  
  Django 
  
  Django Rest Framework
  
  PostgreSQL
  
 
