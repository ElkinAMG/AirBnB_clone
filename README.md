# :rocket: Holberton BnB (HBnB) :rocket:

This is the console or command interpreter for the Holberton Airbnb clone project. Its uses are to store objects in and retrieve objects from a JSON.

### Classes:

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:

* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

### So, where do we begin?

Go to the root of the project folder and enter `./console.py` in the shell.

#### Create

`create <class name>`
Ex:
`create BaseModel`

#### Show

`show <class name> <object id>`
Ex:
`show User user.id`

#### Destroy

`destroy <class name> <object id>`
Ex:
`destroy Place place.id`

#### All

`all` or `all <class name>`
Ex:
`all` or `all User`

#### Quit

`quit` or `EOF`

#### Help

`help` or `help <command>`
Ex:
`help` or `help all`

### Extras

The console can also do method calls `<class name>.<command>(<parameters>)` syntax.
Ex:
`User.show()`