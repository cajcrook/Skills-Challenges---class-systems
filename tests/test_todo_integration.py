from lib.todo import *

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
def add()
Test that multiple Todo is added to TodoList
"""
def test_multiple_todo_is_added_to_todolist():
    todolist = TodoList()
    todo_1 = Todo("Taske_1", False)
    todo_2 = Todo("Taske_2", False)
    todo_3 = Todo("Taske_3", False)
    todolist.add(todo_1)
    todolist.add(todo_2)
    todolist.add(todo_3)
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