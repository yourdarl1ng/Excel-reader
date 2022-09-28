from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import *
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import pandas as pd
#C:\Users\andre\Desktop\siemens\zadanie_data.xlsx
class MWSIEMENS(MDApp):
    #reset search funkcie, zobrazi cely excel subor
    def show_raw(self, *args):
        self.search_var = False
        screen.remove_widget(self.collumn_name)
        screen.remove_widget(self.value_name)
        screen.remove_widget(self.main_card)
        self.value_name = MDTextField(text=self.value_name.text, halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.value_name.size_hint = 0.3, 0.1
        self.value_name.pos_hint = {"center_x": 0.6, "center_y": 0.8}

        self.collumn_name = MDTextField(text=self.collumn_name.text, halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.collumn_name.size_hint = 0.3, 0.1
        self.collumn_name.pos_hint = {"center_x": 0.3, "center_y": 0.8}
        #karta v strede obrazovky
        self.main_card = MDCard()
        self.main_card.size_hint = 0.5, 0.5
        self.main_card.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #text karty v strede obrazovky
        self.card_text = MDTextFieldRect(text=f"{self.data}", halign="center")
        self.card_text.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.main_card.add_widget(self.card_text)

        '''self.apply_search = MDRectangleFlatButton(text="search", on_press=self.search_for_coll)
        self.apply_search.pos_hint = {"center_x": 0.3, "center_y": 0.2}
        self.show_all = MDRectangleFlatButton(text="reset search", on_press=self.show_raw)
        self.show_all.pos_hint = {"center_x": 0.3, "center_y": 0.1}
        self.export_name = MDTextField(halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.export_name.size_hint = 0.3, 0.1
        self.export_name.pos_hint = {"center_x": 0.8, "center_y": 0.2}

        self.export_button = MDRectangleFlatButton(text="export", on_press=self.export)
        self.export_button.pos_hint = {"center_x": 0.8, "center_y": 0.1}'''


        screen.add_widget(self.main_card)
        screen.add_widget(self.collumn_name)
        screen.add_widget(self.value_name)
    #search funkcia, na obrazovke budu cisla riadkov a True/False hodnota zalezi ci sa v riadku nachadza ziadany vyrok
    def search_for_coll(self, *args):
        self.search_var = True
        self.search = self.data[str(self.collumn_name.text)]
        #premenna s vysledkom hladania
        self.search2 = self.data[f"{self.collumn_name.text}"] == f"{self.value_name.text}"
        #self.search_final = self.data_final[f"{self.collumn_name.text}"] == f"{self.value_name.text}"
        screen.remove_widget(self.collumn_name)
        screen.remove_widget(self.value_name)
        screen.remove_widget(self.main_card)
        #search bar widget
        self.value_name = MDTextField(text=self.value_name.text, halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.value_name.size_hint = 0.3, 0.1
        self.value_name.pos_hint = {"center_x": 0.6, "center_y": 0.8}

        self.collumn_name = MDTextField(text=self.collumn_name.text, halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.collumn_name.size_hint = 0.3, 0.1
        self.collumn_name.pos_hint = {"center_x": 0.3, "center_y": 0.8}
        #karta v strede
        self.main_card = MDCard()
        self.main_card.size_hint = 0.5, 0.5
        self.main_card.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #text karty
        self.card_text = MDTextFieldRect(text=f"{self.search2}", halign="center")
        self.card_text.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.main_card.add_widget(self.card_text)

        '''self.apply_search = MDRectangleFlatButton(text="search", on_press=self.search_for_coll)
        self.apply_search.pos_hint = {"center_x": 0.3, "center_y": 0.2}
        self.show_all = MDRectangleFlatButton(text="reset search", on_press=self.show_raw)
        self.show_all.pos_hint = {"center_x": 0.3, "center_y": 0.1}
        self.export_name = MDTextField(halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.export_name.size_hint = 0.3, 0.1
        self.export_name.pos_hint = {"center_x": 0.8, "center_y": 0.2}

        self.export_button = MDRectangleFlatButton(text="export", on_press=self.export)
        self.export_button.pos_hint = {"center_x": 0.8, "center_y": 0.1}'''


        screen.add_widget(self.main_card)
        screen.add_widget(self.collumn_name)
        screen.add_widget(self.value_name)
    #otvori a zobrazi cely excel subor
    def open_xlsx(self, *args):
        self.search_var = False
        #self.data_head = pd.read_excel(str(self.file_input.text)).split("\n")[0]

        self.data = pd.read_excel(str(self.file_input.text))
        #self.data_final = pd.DataFrame(str(self.file_input.text)).to_json()
        #zmaze povodnu obrazovku
        try:
            screen.remove_widget(self.file_input)
            screen.remove_widget(self.file_input_button)
            #screen.remove_widget(self.custom_sheet)
            #screen.remove_widget(self.custom_sheet_name)
        except:
            pass
        #tu sa nachadzaju search bars
        self.value_name = MDTextField(text="Value", halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.value_name.size_hint = 0.3, 0.1
        self.value_name.pos_hint = {"center_x": 0.6, "center_y": 0.8}

        self.collumn_name = MDTextField(text="Elements ", halign="center")
        #self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.collumn_name.size_hint=0.3,0.1
        self.collumn_name.pos_hint = {"center_x":0.3, "center_y":0.8}
        #karta v strede obrazovky
        self.main_card = MDCard()
        self.main_card.size_hint = 0.5, 0.5
        self.main_card.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #text karty
        self.card_text = MDTextFieldRect(text=f"{self.data}", halign="center")
        self.card_text.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.main_card.add_widget(self.card_text)
        #tlacitko search
        self.apply_search = MDRectangleFlatButton(text="search", on_press=self.search_for_coll)
        self.apply_search.pos_hint = {"center_x": 0.3, "center_y": 0.2}
        self.show_all = MDRectangleFlatButton(text="reset search", on_press=self.show_raw)
        self.show_all.pos_hint = {"center_x": 0.3, "center_y": 0.1}
        self.export_name = MDTextField(halign="center")
        # self.value_names = MDTextField(text="Value1;Value2;Value3", halign="center")
        self.export_name.size_hint = 0.3, 0.1
        self.export_name.pos_hint = {"center_x": 0.8, "center_y": 0.2}
        #tlacitko export
        self.export_button = MDRectangleFlatButton(text="export", on_press=self.export)
        self.export_button.pos_hint = {"center_x": 0.8, "center_y": 0.1}
        #pridanie vsetkeho na obrazovku
        screen.add_widget(self.export_button)
        screen.add_widget(self.export_name)
        screen.add_widget(self.show_all)
        screen.add_widget(self.value_name)
        screen.add_widget(self.main_card)
        screen.add_widget(self.collumn_name)
        screen.add_widget(self.apply_search)
    #funkcia exportuje to co je na karte
    def export(self, *args):
        #self.export_data = self.data[f"{self.collumn_name.text}"] == f"{self.value_name.text}"
        self.export_data = self.card_text.text
        #vytvori subor so zadanym menom a zapise donho text karty
        with open(f"{str(self.export_name.text)}.mwexport", "w+") as exp:
            exp.write(str(self.export_data))
            exp.close()
    #zakladna obrazovka, pyta si .xlsx subor
    def build(self):
        #nastavenia farieb
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        
        global screen
        screen = MDScreen()
        #hlavny toolbar
        self.main_toolbar = MDTopAppBar(title="Excel reader")
        self.main_toolbar.pos_hint = {'top':True}

        screen.add_widget(self.main_toolbar)
        #vyber suboru
        self.file_input = MDTextField(text="Full Path to xlsx file", halign="center")
        self.file_input.pos_hint = {"center_x":0.5, "center_y":0.6}
        self.file_input.size_hint = 0.3,0.1

        #self.custom_sheet = MDSwitch()
        #self.custom_sheet.pos_hint = {"center_x":0.3, "center_y":0.5}
        #self.custom_sheet_name = MDTextField(text="name or sheet number(starts at 0)", halign="center")
        #self.custom_sheet_name.size_hint=0.3,0.1
       # self.custom_sheet_name.pos_hint = {"center_x":0.5, "center_y":0.5}
#       #tlacitko na otvorenie suboru
        self.file_input_button = MDRectangleFlatButton(text="Open File", on_press=self.open_xlsx)
        self.file_input_button.pos_hint = {"center_x":0.5, "center_y":0.4}

        #pridanie vsetkeho na obrazovku
        screen.add_widget(self.file_input)
       # screen.add_widget(self.custom_sheet_name)
        #screen.add_widget(self.custom_sheet)
        screen.add_widget(self.file_input_button)

        return screen

MWSIEMENS().run()
