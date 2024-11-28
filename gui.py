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

        self.appLayout = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(value="Hello World")
            ]
        )
    
    def build(self):
        return self.appLayout

        