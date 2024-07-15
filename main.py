from typing import Union
from fastapi import FastAPI
from models import Todo
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

todos = []

# Get all todos 
@app.get("/todos")
def get_todos():
    return {"todos": todos}


# Get Single Todo 
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos: 
        if todo.id == todo_id:
            return { "todo": todo }
        
    return {"message": "No todos found"}

# Create a todo 
@app.post("/todos")
def create_todos(todo: Todo):
    todos.append(todo)
    return {"mesasge": "Todo has been added"}

# Update a todo 
@app.put("/todos/{todo_id}")
def get_todo(todo_id: int, todo_object: Todo):
    for todo in todos: 
        if todo.id == todo_id:
            todo.id = todo_object.id
            todo.item = todo_object.item
            return { "todo": todo }
        
    return {"message": "No todos found to update"}

# Delete a todo 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos: 
        if todo.id == todo_id:
            todos.remove(todo)
            return { "message": "Todo has been deleted" }
        
    return {"message": "No todos found"}
