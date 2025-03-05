### Distinctiveness and Complexity

This is my Capstone project for the CS50 Web Programming with Python and JavaScript course. This project is the recreation of the Pokedex from Pokemon Generation 1, the user can navigate through a list of 151 Pokemon and can view the detail of the Pokemon such as stats, moves, and types. This project has three components to it; React frontend, Django backend, and a custom made API service to retrieve the data. This leveraged both frameworks to create a unique, complex and responsive application.

The API Service file is used to retrieve data from [Poke API](https://pokeapi.co/) on the initial startup of the application. On startup it will call various APIs, seen here in [Postman](https://www.postman.com/navigation-observer-99340780/pokemon-api/collection/miirbob/apis?action=share&creator=38650772), and will convert the data into Django ORM and will be saved to the database. After the data has been seeded into the database and other startups, it will check the data and relationships to ensure the integrity of the database. With a large amount of data to go through, I implemented aiohttp and asyncio to make the process asynchronous to speed up the data migration. 


The Django backend is used for data processing, business logic, and database management. The Python views manage the business logic of calling the API Service and calling the index view from the static file while also serving as the database for the data to be saved to and data retrieval. The views are used to create API endpoints that the React frontend can interact with to handle data retrieval that are returned as JSON objects for the React fronent to interact with to display the information retrieved from the database.


I chose to use React as my frontend for this project for its component based architecture and its UseState for updating the UI. With the UI broken into separate components, I was able to organize the various and complex designed parts of the UI into their own entities. This helped for easier UI management, organizing the files and allowed for passing the required data and method callbacks to their respective components. Being able to use React's UseState I was able to update the detail section based on which Pokemon detail was being viewed, to update the UI to improve the UX of the application, show/hide the 'loading screen' when the data retrieval was complete and to send requests to the backend.



### File Descriptions

- **manage.py**: The command-line utility for managing the Django project.
- **CS50_Capstone/**: The main Django project directory.
  - **__init__.py**: An empty file that tells Python that this directory should be considered a package.
  - **settings.py**: Contains all the settings and configuration for the Django project.
  - **urls.py**: The URL declarations for the Django project.
  - **wsgi.py**: The WSGI configuration for the Django project.
- **Pokedex/**: The Django app directory.
  - **__init__.py**: An empty file that tells Python that this directory should be considered a package.
  - **views.py**: Contains the view functions for the Django app.
  - **urls.py**: The URL declarations for the Django app.
- **frontend/**: The React frontend directory.
  - **package.json**: Contains the dependencies and scripts for the React project.
  - **public/**: Contains the static files for the React project.
    - **index.html**: The main HTML file for the React project.
    - **script.js**: Contains JavaScript functions used in the HTML file.
  - **src/**: Contains the source code for the React project.
    - **App.js**: The main React component.
    - **index.js**: The entry point for the React application.
  - **build/**: Contains the production build of the React project.


### Project Setup

**Clone Repository**
```git clone https://github.com/mcashmore90/CS50_Capstone.git```

**Build and Run**
This can be done in two ways:

1. **NPM**
  - CD into the frontend project [file_path]/CS50_Capstone/frontend
  - run these NPM commands 
    - ``` npm run build ```
    - ``` npm run makemigrations```
    - ``` npm run migrate```
    - ``` npm run runserver```
  - Go to the generated localhost URL 

2. **Python**
  - CD into the frontend project [file_path]/CS50_Capstone/frontend
  - run these NPM commands 
    - ```npm run build```
  - CD into the back end project [file_path]/CS50_Capstone
  - Run these Python commands
    - ``` python manage.py makemigrations ```
    - ``` python manage.py migrate```
    - ``` python manage.py runserver```
  - Go to the generated localhost URL 


### Framework Versions
- Python 3.11.9
- Django 5.1.6
- Node.js 21.6.1
- npm 10.2.4