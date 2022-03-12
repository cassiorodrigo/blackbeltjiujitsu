from kivymd.toast.kivytoast.kivytoast import toast
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
import json
from kivymd.uix.list import OneLineListItem, MDList, ThreeLineListItem, ThreeLineAvatarListItem, ImageLeftWidget
from mysqlhelper import getData, insertData, updateData, removeData


class MainScreen(Screen):

    def filtrar(self, texto):
        #resposta = getData()
        resposta = [["cassio", "roxa", "ga","ga","digo","20022002"]]
        self.ids.container.clear_widgets()
        for e in resposta:
            if str(texto).capitalize() in str(e[0]).capitalize():
                self.ids.container.add_widget(ThreeLineAvatarListItem(text=e[0], secondary_text=e[1],
                                                                      tertiary_text=e[2],id=e[0]))
        criancas = self.ids.container.children
        for each in criancas:
            faixa = each.secondary_text
            if faixa == "Branca":
                each.add_widget(ImageLeftWidget(source="imgbelts/white.jpeg"))
            if faixa == "Azul":
                each.add_widget(ImageLeftWidget(source="imgbelts/blue.jpeg"))
            if faixa == "Roxa":
                each.add_widget(ImageLeftWidget(source="imgbelts/purple.jpeg"))
            if faixa == "Marrom":
                each.add_widget(ImageLeftWidget(source="imgbelts/brown.jpeg"))
            if faixa == "Preta":
                each.add_widget(ImageLeftWidget(source="imgbelts/black.jpeg"))

        for e in self.ids.container.children:
            e.bind(on_release=lambda e: self.mostrarlutador(e.text))
        for i in self.ids.container.children:
            i.bind(on_release=lambda i: self.trocarTela("Second", i.text))

    def trocarTela(self, text2, nome):

        self.manager.current = text2
        self.manager.get_screen("Second").ids.deletarbtn.bind(on_release = lambda r:self.manager.get_screen(
            "Second").deletar(nome))

        return

    def mostrarlutador(self, nome):
        resposta = getData()
        for e in resposta:
            if e[0] == nome:
                nome = e[0]
                faixa = e[1]
                equipe = e[2]
                academia = e[3]
                datagraduacao = e[4]
                apelido = e[5]
                strlutador = f'''[size=16][b]Nome:[/b] {nome} \n\n[b]Faixa:[/b] {faixa} \n\n[b]Time:[/b] {equipe} 
\n[b]Academia:[/b] {academia} \n\n[b]Data de graduacao:[/b]{datagraduacao} \n\n[b]Apelido:[/b] {apelido}[/size]'''

        return self.manager.get_screen("Second").mostrarlutador(strlutador)

    # def pegardados(self):
    #     resposta = getData()
    #     for e in resposta:
    #         self.ids.container.add_widget(ThreeLineListItem(text=e[1], secondary_text=e[2], tertiary_text=e[3]))
    #     for i in self.ids.container.children:
    #         i.bind(on_release=lambda i: self.trocarTela("Second"))



class Second (Screen):

    def on_enter(self, *args):
        pass
        #self.manager.get_screen("Mainscreen").mostrarlutador("Lucas Henrique")
        return

    def deletar(self,nome):
        BlackbeltsApp().confirmarDeletar(nome)
        self.manager.current = "Mainscreen"
        return

    def mostrarvalor(self,nome, faixa, equipe, academia, datagraduacao, apelido):
        strlutador = f"Nome: {nome} \nFaixa: {faixa} \nTime: {equipe} \nAcademia: {academia} \nData de graduacao:" \
                     f" {datagraduacao} \nApelido: {apelido}"
        self.ids.mostrarlutador.text = strlutador
        return strlutador

    def mostrarlutador(self, strlutador):
        self.ids.mostrarlutador.text = strlutador
        return

class Adicionar (Screen):

    def adicionar(self, nome, faixa, equipe, academia, datagraduacao, apelido):
        print(nome)
        print(faixa)
        print(equipe)
        print(academia)
        print(datagraduacao)
        print(apelido)
        if insertData(nome, faixa, equipe, academia, datagraduacao, apelido) == True:
            toast(f"O Lutador {nome} foi adicionado com sucesso")
            self.manager.get_screen("Mainscreen").filtrar("")
            self.manager.current = "Mainscreen"
        else:
            toast(f"Um erro aconteceu. Contacte o desenvolvedor")
        return


class AlterarEntrada(Screen):

    def alterarEntrada(self):
        updateData()
        return

class BlackbeltsApp(MDApp):
    dialog = None

    def Build(self):
        #KV = Builder.load_file("blackbelts.kv")
        return MDApp

    def confirmarDeletar(self,nome):
        dialog = MDDialog(
            title=f'Remover Lutador {nome}', size_hint=(.8, .3), text_button_ok='Remover',
            text=f"Deseja excluir permanentemente o lutador \n{nome} \nda base de dados?", text_button_cancel='Cancel')
        dialog.auto_dismiss = False
        dialog.open()
        dialog.children[0].children[0].children[1].children[0].bind(on_press=lambda x:self.deletarconfirmado(nome))

    def deletarconfirmado(self, nome):
        toast(f"Lutador {nome} foi deletado com sucesso")
        removeData(nome)
        return

if __name__ == "__main__":
    BlackbeltsApp().run()