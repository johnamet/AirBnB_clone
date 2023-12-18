# AirBnB Clone Console

This is a command-line interface (CLI) for managing objects in an AirBnB clone project. The console allows you to
interact with different classes such as BaseModel, User, City, Amenity, Place, Review, and State. You can perform
operations like creating instances, showing details, updating attributes, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Command Examples](#command-examples)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Installation

1. Clone the repository:

   ```bash
   git clone 
   ```

Change directory to the project folder:

```
cd AirBnB_clone
```

Run the console

```
./console.py
```

# Usage

The console supports various commands to interact with the AirBnB objects. Use the `help`` command to see the list of
available commands and their usage.

```
./console.py
```

## Features

- Create new instances of different classes.
- Show details of instances based on class and ID.
- Update attributes of instances.
- Destroy instances.
- List all instances or instances of a specific class.
- Count instances of a specific class.

## Command Examples

- Create a new User instance

```
create User
```

- Show details of a User instance

```
show User <user_id>
```

- Update the email attribute of a User instance

```
update User <user_id> email "new_email@example.com"
```

or

```
User.update("<id>", {"email": "new_email@example.com"})
```

- Destroy an Instance

```
destroy City <city_id>
```

- List all instances

```
all
```

-- Count instances of a specific class

```
<class_name>.count()
```

# Authors

Johnny <johnametepeagboku@live.com>



