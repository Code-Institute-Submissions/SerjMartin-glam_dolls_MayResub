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

### Database
Used SQL database by default.

 - Treatments app


| Name | Key | Type | Extra Info |
| :--------------: | :----------------: | :--------------: | :----------------: |
| Category | category | ForeignKey | null=True, blank=True, on_delete=models.SET_NULL |
| Name | name | CharField | max_length=254 |
| Description | description | TextField | null=True, blank=True |
| Price | price | DecimalField | max_digits=6, decimal_places=2 |
| Deals | deals | CharField | max_length=254, null=True, blank=True |


 - Product app

| Name | Key | Type | Extra Info |
| :--------------: | :----------------: | :--------------: | :----------------: |
| Name | name | CharField | max_length=254 |
| Description | description | TextField |  |
| Price | price | DecimalField | max_digits=6, decimal_places=2 |
| Image url | image_url | URLField | max_length=1024, null=True, blank=True |
| Image | image | ImageField | null=True, blank=True |


 - Checkout app (Order)

| Name | Key | Type | Extra Info |
| :--------------: | :----------------: | :--------------: | :----------------: |
| Order Number | order_number | CharField | max_length=32, null=False, editable=False)
| User Profile | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'|
| Full Name | full_name | CharField | max_length=50, null=False, blank=False |
| Email | email | EmailField | max_length=254, null=False, blank=False |
| Phone Number | phone_number | CharField | max_length=20, null=False, blank=False |
| Country | country | CharField | max_length=40, null=False, blank=False |
| Postcode | postcode | CharField | max_length=20, null=True, blank=True |
| Town Or City | town_or_city | CharField | max_length=40, null=False, blank=False |
| Street Address1 | street_address1 | CharField | max_length=80, null=False, blank=False |
| Street Address2 | street_address2 | CharField | max_length=80, null=True, blank=True |
| County | county | CharField | max_length=80, null=True, blank=True |
| Date | date | DateTimeField | auto_now_add=True |
| Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |


 - Checkout app (OrderLineItem)

| Name | Key | Type | Extra Info |
| :--------------: | :----------------: | :--------------: | :----------------: |
| Order | order | ForeignKey | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product | product | ForeignKey | null=False, blank=False, on_delete=models.CASCADE |
| Quantity | quantity | IntegerField | null=False, blank=False, default=0 |
| Lineitem Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


 - Profile app

| Name | Key | Type | Extra Info |
| :--------------: | :----------------: | :--------------: | :----------------: |
| User | user | OneToOneField | on_delete=models.CASCADE |
| Default Phonenumber | default_phone_number | CharField | max_length=20, null=True, blank=True |
| Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True |
| Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True) |
| Default Town Or City | default_town_or_city | CharField | max_length=40, null=True, blank=True |
| Default County | default_county | CharField | max_length=80, null=True, blank=True |
| Default Ppostcode | default_postcode | CharField | max_length=40, null=True, blank=True |



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