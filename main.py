from flet import *
from Home.gui import AppGui


def main(pg: Page):
    pg.title = "Directory Editor"
    pg.horizontal_alignment = CrossAxisAlignment.CENTER
    pg.scroll = True
    pg.add(
        AppGui()
    )
    pg.update()

if __name__ == '__main__':
    app(target=main)