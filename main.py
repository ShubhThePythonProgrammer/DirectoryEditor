from flet import * # type: ignore
from Home.gui import AppGui


def main(pg: Page):
    pg.title = "Directroy Editor"
    pg.horizontal_alignment = CrossAxisAlignment.CENTER
    pg.add(
        AppGui()
    )
    pg.update()

if __name__ == '__main__':
    app(target=main)