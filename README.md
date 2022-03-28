# Glam Dolls


# About
Glam Dolls is a business website that advertises the Glam Dolls beauty salon. On this website, you can view all the different treatments offered by the salon, list through the different categories of these treatments, and even buy gift cards!
You also have the ability to subscribe for the newest news on offers or discounts.


[Live Website](https://glam-dolls.herokuapp.com/)

![Responsice Mockup](media/mockup.png)

## Table of Contents
  - [Business Goals](#business-goals)
  - [User goals](#User-goals)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Framewoks](#frameworks)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Acknowledgement](#acknowledgement)


## Business Goals
  - To target the customers who are looking for a beauty salon.
  - To target the customers who are looking for nails treatments.
  - To target the customers who are looking for facial treatments.
  - To target the customers who are looking for eye treatments.
  - To sell online how many gift cards is possible.

## User goals

As a customer,  I would like
  - To know what treatments this beauty salon offer.
  - To be able to select a specific category of treatments.
  - To be able to see the description and price of treatment.
  - To be able to buy a gift card online for someone special.
  - To be able to see the total in my shopping bag before checkout.


## Features

### Existing Features
 ### Home

  - ### About
  ![About]()



  - ### History
  ![History]()



 ### Book library
 ![Library]()



 ### Blog
 ![Blog]()


 ### Post Detailes
 ![Comments]()









## Technologies Used

 ### Libraries

  - For the account registration used [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) library
  - For the feature images and CSS support used the [Whitenoise](https://whitenoise.evans.io/en/stable/django.html)
  - For the comments used [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) library
  - For the login/logout templates used default account templates from [Allauth](https://django-allauth.readthedocs.io/en/latest/) library
  - For Awesome icons used [Font Awesome](https://fontawesome.com/)

 ### Programming languages

  - HTML
  - CSS
  - Java Script
  - Python

 ### Framewoks
   - [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean design.
   - [Boostrap](https://getbootstrap.com/) - Bootstrap is a web framework that focused on simplifying the development of an informative web page.

## Testing

 ### Validator Testing

## Deployment

  - ### Create the Heroku app
    On the Heroku, dashboard click on the "Create new app" button then give the app a name, choose a region and click on the "Create app" button.

  - ### Attach the PostgreSQL database
    On the Heroku, menu clicks on the "Resources" tab then in "Add-ons" search for "Postgres" to add Heroku Postgres to the project.

  - ### Prepare our environment and [settings.py](https://github.com/SerjMartin/glam_dolls/blob/main/glamdolls/settings.py) files
    In the project's [settings.py](https://github.com/SerjMartin/glam_dolls/blob/main/glamdolls/settings.py) add the app name in "INSTALET_APP".
    Create the [env.py](https://github.com/SerjMartin/glam_dolls/blob/main/env_sample.py) file to store the URL from DATABASE, SECRET_KEYS then add them in the Heroku "Config Vars".

  - ### Get our static and media files stored on Whitenoise
    - In the project's [settings.py](https://github.com/SerjMartin/glam_dolls/blob/main/glamdolls/settings.py) by adding followings line in MIDDLEWARE ["whitenoise.middleware.WhiteNoiseMiddleware"]
    - In Gitpod workspace's terminal install Whitenoise by typing ("pip3 install whitenoise")


 - ### Deployment to Heroku
    Add Heroku's app name followed by herokuapp.com to ALLOWED_HOST from [setings.py](https://github.com/SerjMartin/glam_dolls/blob/main/glamdolls/settings.py).
    Add a file named "Procfile" for Heroku to know how to run my project.
    In the Heroku, dashboard click on the "Deploy" tab then click on GitHub to connect GitHub account after that searching for a repo to connect it to the Heroku.


### Cloning

## Acknowledgement