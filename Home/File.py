from flet import * #type: ignore


class FetchFiles(UserControl):
    def __init__(self, value_text, remove_task):
        super().__init__()
        self.value = value_text
        self.remove_task = remove_task
        # declaring checkboxes and creating edit text field
    def build(self):
        self.task_tf = TextField(hint_text=self.value, expand=True)
        self.edit_tf = TextField(value=self.value, expand=True)

        # main structure of the app
        self.task_view = Row(
            visible=True,
            controls=[
                self.task_tf,
                # creating buttons to do stuff
                IconButton(icon=icons.CREATE_OUTLINED, on_click=self.edit_clicked),
                IconButton(icon=icons.DELETE_OUTLINE, on_click=self.delete_clicked)
            ]

        )
        # making edit mode
        self.edit_view = Row(
            visible=False,
            controls=[
                self.edit_tf,
                IconButton(icon=icons.CHECK, on_click=self.save_clicked)
            ]
        )
        # returning all the stuff mentioned above
        return Column(controls=[self.task_view, self.edit_view])
    # defining edit buttons

    def edit_clicked(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()
    # defining delete button

    def delete_clicked(self, e):
        self.remove_task(self)
    # defining the save button

    def save_clicked(self, e):
        self.task_tf.label = self.edit_tf.value
        self.task_view.visible = True
        self.edit_view.visible = False
        self.update()
    