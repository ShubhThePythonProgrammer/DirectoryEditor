from flet import *
from os import (rename, remove, rmdir)


class FetchFiles(Column):
    def __init__(self, value_text, remove_task, is_directory=False):
        super().__init__()
        self.value = value_text
        self.remove_task = remove_task
        self.is_directory = is_directory
        self.color = Colors.BLUE if self.is_directory else Colors.WHITE
        self.task_tf = TextField(hint_text=self.value, expand=True, bgcolor=self.color)
        self.edit_tf = TextField(value=self.value, expand=True)

        # main structure of the app
        self.task_view = Row(
            visible=True,
            controls=[
                self.task_tf,
                # creating buttons to do stuff
                IconButton(icon=Icons.CREATE_OUTLINED, on_click=self.edit_clicked),
                IconButton(icon=Icons.DELETE_OUTLINE, on_click=self.delete_clicked)
            ]

        )
        # making edit mode
        self.edit_view = Row(
            visible=False,
            controls=[
                self.edit_tf,
                IconButton(icon=Icons.CHECK, on_click=self.save_clicked)
            ]
        )
        
        self.controls=[self.task_view, self.edit_view]
        
        # declaring checkboxes and creating edit text field
    
    # defining edit buttons

    def edit_clicked(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()
    # defining delete button

    def delete_clicked(self, e):
        self.remove_task(self)
        remove(self.value)
        self.update()

    # defining the save button

    def save_clicked(self, e):
        self.task_tf.label = self.edit_tf.value
        rename(self.value, self.edit_tf.value)
        self.value = self.edit_tf.value
        print(f"LOGS:\n{self.value}")
        self.task_view.visible = True
        self.edit_view.visible = False
        self.update()
    
