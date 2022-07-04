# SquadMakersTest

A Rest API created with Flask, getting ramdom jokes and some math aperations.

## Initial Configuration

Clone this repository:  
`git clone https://github.com/GaboChirico/SquadMakersTest.git`

Create a virtual environment:  
`python3 venv <venv_name>`

Activate the virtual environment.  

Install dependencies.  
`pip install -r requirements.txt`

Set Flask Enviroment variables at `config.py` file

Run command:   
`flask run`

Running Tests  
`python -m unittest -v`

---
## API

The app will run on `localhost:5000/`

#### URLS:


`joke/` 
- GET: Returns a ramdon joke.
- POST: Creates a new Joke (Form param: `text`: str )
- PUT: Updates an existing Joke (Form params: `number`: int, `text`: str)
- DELETE: Deletes an existing Joke (Form params: `number`: int)

`joke/<str:joke_type>` 
- GET: Chuck or Dad Jokes (Path params: `Chuck`: str, `Dad`: str)

`math/`
- GET: Least common multiple of a list of numbers (Query params: `numbers`: int)
- GET: Returns the parametes `number` + 1 (Query params: `number`: int)
     

---

## Database

The default database for the project is MongoDB a very popular NoSQL database, due to the great performance it has, lightness and it's easy to use.

For SQL database there is a basic setup at `database.py` with PostgresSQL conections and query functions.

---
 
## API Documentation at `/docs/api.yaml` file.


Gabriel Chirico - gacn40@gmail.com