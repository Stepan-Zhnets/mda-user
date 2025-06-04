import flet as ft

from Python_AD.AD import groups

def get_options():
    options=[]
    for group in groups:
        options.append(
            ft.DropdownOption(
                key=group,
                content=ft.Text(
                    value=group
                )
            )
        )
    return options

def edit_user(
        User_All_Name:str,
        User_Login_Name:str,
        User_Group:str,
        )->str:
    data_user = ft.AlertDialog(
        # width=500,
        actions=[
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(User_All_Name),
                            ft.Text(User_Login_Name),
                            ft.Text(User_Group),
                            ft.Divider(thickness=3, color="white"),
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.SAVE,
                                        icon_color="green300",
                                        icon_size=30,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color="red300",
                                        icon_size=30,
                                    ),
                                ]
                            ),
                        ]
                    ),
                    ft.VerticalDivider(),
                    ft.Column(
                        controls=[
                            ft.Dropdown(
                                editable=True,
                                label="Наборы",
                                options=get_options()
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
    return data_user

