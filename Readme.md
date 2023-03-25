# Wekart

This is a Django-based web application that allows shopkeepers to manage their orders. It includes CRUD functionality, secure login with Google OAuth, and additional features such as tags and favorites.

## Features

* Create, Read, Update, and Delete orders
* Secure login with Google OAuth
* Add tags to items to make searching easier
* Search for items by tag or name
* Mark orders as favorites for quick access and view on a seperate page

## Technology Used

* Django
* Tailwind Css
* Google OAuth

## Setup

First clone the repository

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