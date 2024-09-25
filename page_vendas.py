import flet as ft 
def main(page:ft.Page):
    page.bgcolor=ft.colors.BLACK
    page.scroll=True
    def change_main_image(e):
        for elm in options.controls:
            if elm == e.control:
                elm.opacity=1
                img_principal.src = elm.image_src
            else:
                elm.opacity=0.5
        img_principal.update()
        options.update()
    imgs=ft.Container(
        col={'xs':12,'md':6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                img_principal:=ft.Image(src='https://th.bing.com/th/id/OIP.TzTNPI9oMJTIHrXFMXp_ngHaIY?rs=1&pid=ImgDetMain'),
                options:= ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                            ft.Container(
                            image_src='https://th.bing.com/th/id/OIP.TzTNPI9oMJTIHrXFMXp_ngHaIY?rs=1&pid=ImgDetMain',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                            ft.Container(
                            image_src='https://images.tcdn.com.br/img/img_prod/858375/poltrona_macau_1321_1_864d702c6f453c0fcb80d91e26a93c33.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                            ft.Container(
                            image_src='https://th.bing.com/th/id/OIP.UVKzNiDrwiLcZsgHcgf-tAHaIR?rs=1&pid=ImgDetMain',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        )
                    ]
                )
            ]
        )
        )
    details=ft.Container(
        col={'xs':12,'md':6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='POLTRONAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    value='poltrona marrom moderna',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30
                ),
                ft.Text(
                    value='sala de estar',
                    color=ft.colors.GREY,
                    italic=True
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='R$ 399',
                            color=ft.colors.WHITE,
                            size=30,
                            col={'xs':12,'sm':6}
                            ),
                        ft.Row(
                            col={'xs':12,'sm':6},
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _<4 else ft.colors.WHITE,
                                    offset=ft.Offset(x=0,y=0.3),
                                    
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=120,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='compre esta bela poltrona de algodão e veludo',
                                    color=ft.colors.GREY
                                )
                            )
                        ),
                        ft.Tab(
                            text='detalhes',
                             content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='preço de 399 reais e mais outras coisas top de linha',
                                    color=ft.colors.GREY
                                    )
                                )
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE,size=15),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='amarelo',text_style=ft.TextStyle(color=ft.colors.WHITE)),
                                ft.dropdown.Option(text='vermelho',text_style=ft.TextStyle(color=ft.colors.WHITE)),
                                ft.dropdown.Option(text='azul',text_style=ft.TextStyle(color=ft.colors.WHITE)),
                            ],bgcolor=ft.colors.BLACK87
                        ),
                         ft.Dropdown(
                            col=6,
                            label='quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE,size=15),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} und',text_style=ft.TextStyle(color=ft.colors.WHITE)) for num in range(1,11)
                            ],bgcolor=ft.colors.BLACK87
                        )
                    ]
                ),
                ft.Container(expand=True),
                ft.ElevatedButton(
                    width=800,
                    text='adicionar na lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={ft.MaterialState.DEFAULT:ft.BorderSide(width=2,color=ft.colors.WHITE)},
                        bgcolor={ft.MaterialState.HOVERED:ft.colors.WHITE,ft.MaterialState.DEFAULT:ft.colors.BLACK87},
                        color={ft.MaterialState.DEFAULT:ft.colors.WHITE,ft.MaterialState.HOVERED:ft.colors.BLACK}
                    )
                ),
                ft.ElevatedButton(
                    width=800,
                    text='adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={ft.MaterialState.DEFAULT:ft.BorderSide(width=2,color=ft.colors.WHITE)},
                        bgcolor={ft.MaterialState.HOVERED:ft.colors.WHITE,ft.MaterialState.DEFAULT:ft.colors.AMBER},
                        color={ft.MaterialState.DEFAULT:ft.colors.WHITE,ft.MaterialState.HOVERED:ft.colors.BLACK}
                    )
                )
            ]
        )
    )
    layout=ft.Container(
        shadow=ft.BoxShadow(blur_radius=50,color=ft.colors.BLUE_ACCENT),
        margin=ft.margin.all(30),
        width=800,
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                imgs,
                details
            ]
        )
    )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main)