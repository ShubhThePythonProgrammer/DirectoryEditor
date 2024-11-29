from flet import * #type: ignore


class FetchFiles(UserControl):
    def __init__(self):
        super().__init__()
        self.appLayout = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text("Hello Everybody")
            ]
        )
    
    def build(self):
        return self.appLayout
    