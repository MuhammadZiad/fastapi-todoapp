# make necessary imports from the resources
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, HTTPException


# create the FastAPI class
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# classes
class Todo (BaseModel):
    id: UUID # the optional one
    name: str
    status: Optional [str] = "pending"


todo_lst=[Todo(id=uuid4(),name='Do homework'),
Todo(id=uuid4(),name='Shopping'),
Todo(id=uuid4(),name='Reading',status='Done')]

@app.get("/")
def read_root():
    return {"Good luck": "team 2 and 3"}

# create a todo list and add 3 Todo items to serve as examples

Todo(id=uuid4(),name='Reading')]


# create a get req. listener for the landing page "/"
# return hello world or sth random as a response object

@app.get("/")
def read_root():
    return {"Hello": "Everybody"}

# create a get req. listener for the endpoint "/todos"
# return all todos as a response object

@app.get("/todos")
def read_todos():
    return todo_lst

# create a get req. listener for the a single todo item, customize the path using item id
# return the particular item as a response object
@app.get("/get-item")

def get_todo_item(id: str):
    for item in todo_lst:
        if str(item.id) == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found, do it again.")


# create a post req. listener for creating a new todo item
# return the newly created item as a response object
def create_todo_item(item: Todo):
    todo = Todo(name = item.name)
    todo_lst.append(todo)
    return todo


# create a put req. listener for updating an existing todo item
# return the updated item as a response object



# create a delete req. listener for deleting a todo item
# return the final list of todos as a response object



# create a delete req. listener for deleting all todo items
# return the  final list of todos, which would be an empty list, as a response object

@app.delete("/todos")

def delete_all_items():
    global todo_lst
    todo_lst = []
    return todo_lst




# THINGS TO KEEP IN MIND:

# work in specific branches (git checkout -b feature/<feature_name_of_your_branch>)

# make sure to specify each function by creating docstrings, here's an example:
    # """Search for a single user
    # Args:
    #     user_id (UUID): id of the user
    # Returns:
    #    JSON: JSON representation of user details
    # """


# use proper error handling - check FastAPI docs.

# install the following VsCode extensions:
# autoDocstring - Python Docstring Generator
# Live Server

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
