# Environment Ecommerce
“Environment Ecommerce” as the name suggests is about providing various kinds of environmental services. It will automate the task of finding providers (or workers who will perform those services) as well as of collecting funds through a web-application.
People facing a certain environmental issue in their locality just need to login to the application and raise a service.<br>

## Requirement
Django is the basic requirement for the project
All the requirements can be found in `requirements.txt` in the project root folder and can be installed with `pip3 install -r requirements.txt`. `pip` in required for the same.<br>
**To Run the project:** Use `python manage.py runserver`

## Functionality
Refer [ppt here](https://docs.google.com/presentation/d/1KZTJOCgC-inyOFpb1xzQI-1aHEAy9aiKQjQ78_tvess/edit?usp=sharing) for this.

## Project Structure
The project strictly follows Django Architecture. Use [this tutorial](https://medium.com/@timmykko/a-quick-glance-of-django-for-beginners-688bc6630fab#:~:text=robust%20and%20scalable.-,Django%20Architecture,such%20as%20MySql%2C%20Postgres) to get a basic idea of Django.

There are 2 Django Apps in the project:
  * **users** - Handles the profile of users in the application and other login features. This uses Django [users](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/) model.
  * **feed** - Handles the user feed in the application for all services. The code for database can be found out in [models.py](https://github.com/Mohit17067/environment_ecommerce/blob/master/feed/models.py) of feed application.<br>
    HTML files can be found in [templates](https://github.com/Mohit17067/environment_ecommerce/tree/master/feed/templates/feed) folder of feed application which handles all the user interface for the application.<br>
    [urls.py](https://github.com/Mohit17067/environment_ecommerce/blob/master/feed/urls.py) contains all the urls in the web-application and the corresponding controller methods.<br>
    [views.py](https://github.com/Mohit17067/environment_ecommerce/blob/master/feed/views.py) contains all the class view controller methods for the feed application.<br>
    [forms.py](https://github.com/Mohit17067/environment_ecommerce/blob/master/feed/forms.py) contains all the customised forms which are used at various places(login/registeration, service creation etc) in the application.<br>
    
