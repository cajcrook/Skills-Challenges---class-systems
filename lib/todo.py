# File: lib/todo_list.py

from binascii import Incomplete


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
        incomplete_list = []
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        for i in range(len(self.full_todo_list)):
            # print(f"Line 23, {i}")
            # print(f"Line 24, {self.full_todo_list[i]}")
            # print(f"Line 25, {self.full_todo_list[i].task}")
            # print(f"Line 26, {self.full_todo_list[i].status}")
            if self.full_todo_list[i].status == False:
                incomplete_list.append(self.full_todo_list[i].task)
        return incomplete_list

        
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = []
        for i in range(len(self.full_todo_list)):
            # print(f"i =, {i}")
            # print(f"Line 45, {self.full_todo_list[i]}")
            # print(f"Line 46, {self.full_todo_list[i].task}")
            # print(f"Line 46, {self.full_todo_list[i].status}")
            if self.full_todo_list[i].status == True:
                complete_list.append(self.full_todo_list[i].task)
        return complete_list


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        give_up_list = []
        for i in range(len(self.full_todo_list)):
            if self.full_todo_list[i] == False:
                self.full_todo_list[i] = True
            

# File: lib/todo.py

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
        self.task_list = [task]
        self.status_list = [status]

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        for i in range(len(self.task_list)):
            if self.task_list[i] == False:
                self.task_list[i] = True