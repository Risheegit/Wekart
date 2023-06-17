# Wekart

This is a Django-based web application [https://wekart-production.up.railway.app/] that allows users to buy and sell items. It includes CRUD functionality, secure login with Google OAuth, analytics with Google Analytics 4, hosted with Raleway and additional features such as wishlist, tags and search functionality.

## Features

* Create, Read, Update, and Delete orders
* Secure login with Google OAuth
* Analytics with Google Analytics 4
* Add tags to items to make searching easier
* Search for items by tag or name
* Wishlist to view and buy items at a later date

## Technology Used

* Django
* Tailwind CSS
* Postgres SQL
* Google OAuth
* Google Analytics
* Raleway

## Setup

The website can be viewed at https://wekart-production.up.railway.app/[https://wekart-production.up.railway.app/]. 
To set the website locally, first clone the repository

    git clone https://github.com/Risheegit/Wekart.git
    cd wekart

Create a virtual environment to install dependencies in and activate it:

    virtualenv env
    source env/bin/activate

Then install the dependencies:

    pip install -r requirements.txt

Configure the Google OAuth credentials in settings.py
Once the dependencies are downloaded
Run the migrations using the command 

    python manage.py migrate

Start the development server using the command python manage.py runserver


    python manage.py runserver

And navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)