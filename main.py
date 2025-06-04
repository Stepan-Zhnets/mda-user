import flet as ft

from UI_Components import update_table

enter_user = ft.TextField(
    label="Имя",
    hint_text="Иванов Иван Иванович"
    )



def main(page: ft.Page):
    page.title="ПУД-Пользователя"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding=20
    page.window.height=300
    page.window.width=600
    
    
    page.add(
        ft.Container(content=enter_user, width=400),
    )

    update_table(page)
    

if __name__ == "__main__":
    ft.app(main)
