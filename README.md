<h1 align="center">:rocket: Holberton BnB (HBnB) :rocket:</h1>

<img src="/assets/hbnb.png" style="width:100;height:50px;">

This is the console or command interpreter for the Holberton Airbnb clone project. Its uses are to store objects in and retrieve objects from a JSON.

### :zap: Classes :zap:

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### :zap: Commands :zap:

* create - creates an object or instance
* show - show an object in a specific format
* destroy - destroy an object or deletes it
* all - show all objects of a certain type (if specified), or all types
* quit/EOF - quit or exit the console
* help - see descriptions of commands

### So, where do we begin? :eyes:

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

- The console can also do method calls `<class name>.<command>(<parameters>)` syntax.
   Ex:
    `User.show()`

- The console can receive commands from non-interactive mode, it means that you can create files with some commands and make a kind of automation tasks.
    Ex: <br />
   `$ echo "create User \n show User" >> t_file` <br />
   `$ cat t_file | ./console.py`

### Authors
:copyright: Andrew Kalil - [Twitter](https://www.twitter.com/AndrewKalil1) - [GitHub](www.github.com/AndrewKalil) <br />
:copyright: Elkin Mejia - [Twitter](https://www.twitter.com/ElkinAMG) - [GitHub](www.github.com/ElkinAMG)
