import flet as ft


def main(page: ft.Page):
    page.title = "Browse Restaurants!"
   

   

    page.add(

        ft.Row(
            [
                ft.NavigationRail(
                    min_width=100,
                    min_extended_width=400,
                    selected_index=0,
                    destinations=[
                        ft.NavigationRailDestination(
                            icon=ft.Icons.RESTAURANT_OUTLINED,
                            selected_icon=ft.Icons.RESTAURANT,
                            label="Restaurants"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.Icons.HISTORY_OUTLINED,
                            selected_icon=ft.Icons.HISTORY,
                            label="Order History"
                        )
                    ]
                ),
                ft.VerticalDivider(width=1),
                ft.Column(
                    [ft.Text("Hello World!", color=ft.Colors.WHITE_30)], alignment=ft.MainAxisAlignment.START, expand=True
                )
            ],
            expand=True
        )
    )


ft.run(main)
