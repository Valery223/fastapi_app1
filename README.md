--> poetry
export PYTHONPATH=$PWD/src:$PATHONPATH

poetry new app-name
poetry init
poetry add packege
poetry install
poetry env info --path  # intepritator python, path for vscode


--> uvicorn  
uvicorn hello:app --reload
or in .py

--> requests
>>> import requests
>>> r = requests.get("http://localhost:8000/hi")
>>> r
>>> r.json()
'Hello? World?'

http localhost:8000/hi      