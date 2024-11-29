from flet import * #type: ignore
import os
from os import (
    remove,
    rename,
    rmdir
)
from Home.File import FetchFiles


class AppGui(UserControl):
    def __init__(self):
        super().__init__()
        self.title = Text(
            value="Directory Editor",
            size=36
        )
        self.NoUseText = Text(value="Current Directory: ")
        self.pathOfDir = TextField(
            value=os.getcwd(),
            expand=True
            )
        self.path = Row(
            controls=[
                self.NoUseText,
                self.pathOfDir
            ]            
        )
        self.retrieve = FloatingActionButton(
            text="Retrieve",
            on_click=self.retrieveFiles
        )
        self.appLayout = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.title,
                self.path,
                self.retrieve
            ]
        )
        
    def build(self):
        return self.appLayout

    def retrieveFiles(self, e):
        file = FetchFiles("ChalloE", self.RemoveFiles)
        self.appLayout.controls.append(file)
        self.update()
    def RemoveFiles(self, task):
        self.appLayout.controls.remove(task)
        self.update()