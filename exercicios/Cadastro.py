from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
         break
    if eventos == 'Entrar':
         if valores['usuario'] == 'Jhonatan' and valores ['Senha'] =='123456':
              print('Bem-vindo a Dev aprender!')
