# AirBnB_clone

## Descriptions:

- This is the first step towards building AirBnB full web application clone.

* This command interpreter (console) is to manage the objects of the AirBnB web application:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Whats in the command interpreter:

- BaseModel to take care of the initialization, serialization and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine

## What’s a command interpreter:

we want to be able to manage the objects of our project:
