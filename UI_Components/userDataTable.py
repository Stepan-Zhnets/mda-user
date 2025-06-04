import flet as ft
from UI_Components.edit_userAlertDialog import edit_user

data_users = [
    {
        "User_All_Name": "Иванов Иван Иванович",
        "User_Login_Name": "ivanov.ivan",
        "User_Group": "Набор_01",
    },
    {
        "User_All_Name": "Иванов Иван Иванович",
        "User_Login_Name": "ivanov.ivan",
        "User_Group": "Набор_01",
    },
    {
        "User_All_Name": "Иванов Иван Иванович",
        "User_Login_Name": "ivanov.ivan",
        "User_Group": "Набор_01",
    },
]

def update_table(page):
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    list_users = data_users

    columns = [
        ft.DataColumn(ft.Text("Выводимое имя")),
        ft.DataColumn(ft.Text("Логин")),
        ft.DataColumn(ft.Text("Набор")),
        ft.DataColumn(ft.Text("actions"))
    ]

    rows = []
    for user in list_users:
        rows.append(lv.controls.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(user["User_All_Name"])),
                ft.DataCell(ft.Text(user["User_Login_Name"])),
                ft.DataCell(ft.Text(user["User_Group"])),
                ft.DataCell(ft.IconButton(
                    icon=ft.Icons.ACCOUNT_CIRCLE,
                    icon_color="blue300",
                    icon_size=30,
                    tooltip="Выбрать пользователя",
                    on_click=lambda e: page.open(edit_user(
                        user["User_All_Name"],
                        user["User_Login_Name"],
                        user["User_Group"]
                    )),
                ))
            ]
        )))
        # lv.controls.append()

    data_table = ft.DataTable(
        columns=columns, rows=rows,
        border=ft.border.all(1, "black"),
        border_radius=10,)

    page.clean
    page.add(
        ft.Container(content=data_table),
    )