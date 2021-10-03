# Wep App
It using Flutter platform with Dart language, and drag_and_drop_lists library. It have include desktop view and mobile view

# How to run it
Open it on visual studio code, re-save again the pubspec.yaml for install others library,click on main.dart inside lib folder, click the run on the top menu and debugging it


--------------------------------------------------------------------------------------

# API Project
It using python with FastAPI as framework and some library

# How to run it
Command prompt and "cd" to api folder, run "pip install -r requirements.txt" to install all library or can create one virtual enviroment to install it. 
After that same location run "uvicorn app.main:app --port 9900" then can be use already

## Get endpoint
http://localhost:9900/assessment/<name>    (GET method)

## Update endpoint
http://localhost:9900/assessment	   (PUT method)
json
{
  "name": "string",
  "monthly_salary": 0
}
