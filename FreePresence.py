from pypresence import Presence
import os
import time
from time import sleep
import ipaddress
import PySimpleGUI as sg

class TelaInicial():
    def __init__(self):
        sg.change_look_and_feel('DarkGrey5')
        layout = [[sg.Text('Discord RPC Editor',font='Ebrima 14',text_color='RoyalBlue1'),sg.Text('v: 0.0.2        by Rahony',font='Couries 8',text_color='RoyalBlue3')],
                [sg.Text('Digite o ID do client: ',size=(25,0)), sg.InputText(size=(20,1),key='clientid')],
                [sg.Text('Digite o status do RPC: ',size=(25,0)), sg.InputText(size=(20,1),key='estatos')],
                [sg.Text('Digite os detalhes do RPC: ',size=(25,0)), sg.InputText(size=(20,1),key='detalhes')],
                [sg.Text('Digite o nome da imagem grande: ',size=(25,0)), sg.InputText(size=(20,1),key='imagemGrande')],
                [sg.Text('Digite o texto da imagem grande: ',size=(25,0)), sg.InputText(size=(20,1),key='textoimagemGrande')],
                [sg.Button('Iniciar',disabled=False), sg.Button('Cancelar')]
                ]
        
        self.janela = sg.Window("DiscordRPC Editor").layout(layout)
        
        
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            clienteid = self.values['clientid']
            estatos =  self.values['estatos']
            detalhes = self.values['detalhes']
            imagemGrande = self.values['imagemGrande']
            textoimagemGrande = self.values['textoimagemGrande']
            rpc = Presence(clienteid)
            rpc.connect()
            if self.event == sg.WIN_CLOSED or self.event == 'Cancelar':
                break
            if self.event == 'Iniciar':
                sg.popup('Aviso! não aperte no botão novamente, isso pode travar o programa')
                rpc.update(state=estatos, details=detalhes, large_image=imagemGrande, large_text=textoimagemGrande, start=time.time())
                print("RPC Iniciado")
                
tela = TelaInicial()
tela.Iniciar()