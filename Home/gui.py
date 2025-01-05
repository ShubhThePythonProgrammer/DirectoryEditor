from flet import * #type: ignore
import os
from Home.File import FetchFiles


class AppGui(UserControl):
    def __init__(self):
        super().__init__()
        self.counter = 0
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
            on_click=self.retrieveFiles,
            width=100,
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
        self.counter += 1
        if self.counter > 1:
            pass
        else:    
            self.content =  list(os.listdir())
            for i in self.content:
                itemPath = os.path.join(os.getcwd(), i)
                if os.path.isdir(itemPath):
                    file = FetchFiles(i, self.RemoveFiles, is_directory=True)
                else:
                    file = FetchFiles(i, self.RemoveFiles)
                self.appLayout.controls.append(file)
                self.update()
        
    def RemoveFiles(self, task):
        self.appLayout.controls.remove(task)
        self.update()