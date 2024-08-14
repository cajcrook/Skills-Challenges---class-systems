# File: lib/todo_list.py
from ast import Pass


class TodoList:
    def __init__(self):
        self.full_todo_list = []


    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo = todo
        self.full_todo_list.append(todo)
        print(self.full_todo_list)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass
        # for i in range(len(self.full_todo_list)):
        #     if self.full_todo_list[i] == False:
        #         return [i-1]

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
        self.task = task
        self.status = status
        self.list = []

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        for i in range(len(self.list)):
            if self.list[i] == False:
                self.list[i] = True