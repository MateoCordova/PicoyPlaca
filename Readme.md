## Pico y Placa Predictor
# About
This web application aims to be able to predict, given a vehicle license plate, a date and a time, if a private vehicle can travel in the city of Quito following the current restriction rules:

![alt text](https://github.com/MateoCordova/PicoyPlaca/blob/master/App/Content/reglas.jpg?raw=true)

# Instalation

This proyect was made with Python 3.10.4, using Flask minimal framework. After you have installed Python, open a terminal in the root of the repository and run the following commands:

```bash
pip install -r requirements.txt
cd ./App
flask init-db
flask run
```

# Use and testing
Open browser at http://localhost:5000 for a web user experience. You could also test the app as an API using as endpoint  http://localhost:5000/plate/canDrive which uses the following parameters:

```json
{
    "plate" : "PAA1234",  
    "date" : "13-05-2022", 
    "hour" : "10:20" 
}
```

For testing, pytest is used. Open Terminal at root of the repo and run 

```bash
pytest
```

# Design explication

An MVC architecture was used using the Flask framework.
By defining the data layer in the Model module, converting it from an SQLite base defined in the Database module. The Badge and Restriction class is defined for usability and code maintenance. This design allows you to determine what restrictions a board is subject to using regular expressions, so that if rules are added or changed, a change in the code is not necessary, but only in the data.