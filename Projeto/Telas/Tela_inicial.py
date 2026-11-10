import flet as ft

textinicial = ft.Text("Bem-vindo", size=15, weight=ft.FontWeight.BOLD)
textsecundario = ft.Text("alçalal", size=15, weight=ft.FontWeight.BOLD)
text_terciario = ft.Text("Bem", size=15, weight=ft.FontWeight.BOLD)

mensagemInicial = ft.Row(controls=[textinicial],alignment = ft.MainAxisAlignment.CENTER)
mensagemsecundaria = ft.Row(controls=[textsecundario],alignment = ft.MainAxisAlignment.CENTER)
mensagemterciaria = ft.Row(controls=[text_terciario],alignment = ft.MainAxisAlignment.CENTER)

tela1 = ft.Container(content=mensagemInicial, 
              width=200, height= 300,
              border=ft.border.all(2,ft.Colors.GREY_100))

tela2 = ft.Container(content=mensagemsecundaria, 
                     width=200, height= 300,
                     border=ft.border.all(2,ft.Colors.GREY_100))

tela3 = ft.Container(content=mensagemterciaria, 
                            width=200, height= 300,
                            border=ft.border.all(2,ft.Colors.GREY_100))

telas = {
       0: tela1,
       1: tela2,
       2: tela3
}

conteudo_principal = ft.Container(content=telas[0], alignment= ft.MainAxisAlignment.CENTER)

def mudar_tela(e):
       conteudo_principal.content = telas[e.control.selected_index]
       conteudo_principal.update

menu1 = ft.NavigationRailDestination(icon=ft.Icons.HOME_OUTLINED,selected_icon=ft.Icons.HOME,label="Inicio")
menu2 = ft.NavigationRailDestination(icon=ft.Icons.PERSON_OUTLINED,selected_icon=ft.Icons.PERSON,label="Inicio")
menu3 = ft.NavigationRailDestination(icon=ft.Icons.AIRPLANEMODE_ON,selected_icon=ft.Icons.AIRPLANEMODE_OFF,label="Inicio")

navegacao = ft.NavigationRail(destinations=[menu1,menu2,menu3],selected_index=0,on_change=mudar_tela,group_alignment=-1.0)
linha = ft.Row(controls=[navegacao,conteudo_principal],expand=True)
