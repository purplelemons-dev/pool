# Pool
pool is a database manager that hosts a database for scripts to either temporarily store or cache data. It is a simple database manager that is easy to use and is very fast. It is also very lightweight and is easy to install.

## Installation
this is in beta currently, so you can only run it from source.

## Usage
pool should run in the background and scripts can connect to it using the Pool module.
### Running pool
execute inside the pool directory, the one with the `__main__.py` file in it.
```bash
python -m pool
```
### Using Pool
Read/write to the database using the Pool module:
```py
from Pool import Pool
# Pool objects can be created with a name. The pool manager will check if the name exists and if it does, it will connect to it. If it doesn't, it will create a new pool with that name.
pool = Pool(name="example")
# We can create an empty list. Empty dicts and tuples can also be created.
pool["table1"] = []
# Empty sets cannot be created as seen above, so the .set("path","to","table") method can be used to create an empty set. This method can also be used to create lists, dicts, and tuples.
pool.set("table2")
while True:
    user_in = input(">>> ")
    if user_in == "exit":
        break
    elif len(user_in) > 1:
        pool["table1"].append(user_in[0])
        pool["table2"].add(user_in[1:])
    else:
        pool["table1"].append(user_in)
        pool["table2"].add(user_in)
```
Listen to pool:
```py
from Pool import Pool
# If you plan on listening to pool, make a subclass with a modified on_change method.
class Pool(Pool):
    def on_change(self, path, before, after):
        print(f"Path: {path}\nBefore: {before}\nAfter: {after}\n")
MyPool(name="example").listen()
```
