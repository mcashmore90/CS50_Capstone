Capstone project for HarvardX CS50’s Web Programming with Python and JavaScript course using https://pokeapi.co/ API to recreate the Pokedex from Pokemon generation 1.

Postman APIs to be used:
https://www.postman.com/navigation-observer-99340780/pokemon-api/collection/miirbob/apis?action=share&creator=38650772


## Clone repository 
git clone https://github.com/mcashmore90/CS50_Capstone.git


## Project setup
This can be done in two ways:

# 1
# CD into the frontend project
[file_path]/CS50_Capstone/frontend

# Run these NPM commands
npm run build
npm run makemigrations
npm run migrate
npm run runserver

# Go to the generated localhost URL 

# 2
# CD into the front end project
[file_path]/CS50_Capstone/frontend

# Run these NPM commands
npm run build

# CD into the back end project
[file_path]/CS50_Capstone/Pokedex

# Run these Python commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Go to the generated localhost URL 