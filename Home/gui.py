from flet import * #type: ignore
import os
from os import (
    remove,
    rename,
    rmdir
)


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
        self.appLayout = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.title,
                self.path,

            ]
        )
    
    def build(self):
        return self.appLayout

        