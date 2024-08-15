
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

```python
# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass
        # self.full_todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
        # self.todo = todo
        # self.full_todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        # todo = Todo
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
from xmlrpc.client import boolean

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task, status):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
class Todo
def __init__()
Tests that Todo instantiates task with correct attribute
"""
def test_todo_instantiated_correctly():
    todo_1 = Todo("Task_1", False)
    assert todo_1.task == "Task_1"
    assert todo_1.status == False

"""
class Todo
def mark_complete()
Test to change all Todos status to True (complete)
"""
def test_upate_all_status_to_true():
    todo_1 = Todo("Task_1", True)
    assert todo_1.task == "Task_1"
    assert todo_1.status == True

"""
class TodoList
def add()
Test that Todo is added to TodoList
"""
def test_todo_is_added_to_todolist():
    todolist = TodoList()
    todo_1 = Todo("Taske_1", False)
    todolist.add(todo_1)
    assert todolist.full_todo_list

"""
class TodoList
def incomplete()
Test show all Todos that are incomplete (false)
"""
def test_to_return_all_incomplete():
    todolist = TodoList()
    todo_1 = Todo("Task_1", False)
    todo_2 = Todo("Task_2", False)
    todo_3 = Todo("Task_3", True)
    todolist.add(todo_1)
    todolist.add(todo_2)
    todolist.add(todo_3)
    assert todolist.incomplete() == ["Task_1", "Task_2"]

"""
class TodoList
def complete()
Test show all Todos that are complete (true)
"""
def test_to_return_all_complete():
    todolist = TodoList()
    todo_1 = Todo("Task_1", False)
    todo_2 = Todo("Task_2", True)
    todo_3 = Todo("Task_3", True)
    todolist.add(todo_1)
    todolist.add(todo_2)
    todolist.add(todo_3)
    assert todolist.complete() == ["Task_2", "Task_3"]

"""
class TodoList
def give_up()
Give up and mark all todos as complete (true)
"""
def test_mark_all_as_complete():
    todolist = TodoList()
    todo_1 = Todo("Task_1", False)
    todo_2 = Todo("Task_2", False)
    todo_3 = Todo("Task_3", True)
    todolist.add(todo_1)
    todolist.add(todo_2)
    todolist.add(todo_3)
    assert todolist.give_up


## test multiples


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
