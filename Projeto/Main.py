import flet as ft
from Telas import Tela_inicial as TI



def main (page: ft.Page):

    page.window.width = 700
    page.window.height = 500

    page.theme_mode = ft.ThemeMode.DARK

    





    page.add(TI.linha)

ft.run (main=main)