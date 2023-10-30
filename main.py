
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.toast import toast
from kivy.lang import Builder

from gtts import gTTS
from playsound import playsound


kv="""
<TextoSpk>:
	BoxLayout:
		orientation: "vertical"
		ActionBar:
			canvas:
				Color:
					rgba: 1/10,1/10,1/4,1
				Rectangle:
					pos: self.pos
					size: self.size
			ActionView:
				ActionPrevious:
					with_previous: False
					app_icon: "img/iconsf.png"
					title: "Texto para Audio"
					
				ActionButton:
					text: "about"
				ActionButton:
					text: "help"
		BoxLayout:
			size_hint_y: None
			spacing: 250
			padding: 70
			height: "200px"
			MDLabel:
				id: lg1
				text: "Portugues"
				color: 0,0,1,1
			MDIconButton:
				id: btnLg
				icon: "img/rev3.png"
				on_release: root.change_lang()
				
				pos_hint: {"center_x":.5,"center_y": .5}
			MDLabel:
				id: lg2
				text: "Ingles"
				color: 1,0,0,1
		BoxLayout:
			pos_hint: {"center_x": .5,"y": 0}
			size_hint_x: .8
			size_hint_y: 2
			TextInput:
				id: inText
				text: "ola mundo!"
				
		BoxLayout:
			pos_hint: {"center_x": .5,"center_y": .6}
			size_hint_x: .6
			MDRectangleFlatButton:
				text: "DOWNLOAD AUDIO"
				pos_hint: {"center_x": .5,"center_y": .5}
				on_release: root.save1()
				
			MDIconButton:
				icon: "play"
				pos_hint: {"center_x":.5,"center_y": .5}
				on_release: root.play1()
"""
Builder.load_string(kv)
class TextoSpk(Screen):
	def play1(self):
		path = "/storage/emulated/0/.CovertText/"
		texto = self.ids.inText.text
		ply = 1
		lang1 = self.ids.lg1.text
		lg = "pt"
		if lang1 == "Portugues":
			lg = "pt"
		elif lang1 == "Ingles":
			lg = "en"
		else:
			toast("Problema na linguagem do audio...")
		try:
			
			voz = gTTS(text= texto,lang=lg,slow=False)
			
			voz.save(path+"audio_convert.mp3")
		except:
			toast("Nao tem Conecao a a internet...")
			ply = 0
		if ply == 1:
			try:
				playsound(path+"audio_convert.mp3")
			except:
				toast("Falha no player...")
				
			
	def save1(self):
		iniPath = "/storage/emulated/0/.CovertText/"
		argv = "audio_convert.mp3"
		
		savePath = "/storage/emulated/0/ConvertText/"
		try:
			os.rename(initPath+argv,savePath+argv)
		except:
			toast("Erro. Reproduza o audio Primeiro..")
		
		
	def change_lang(self):
		lang1 = self.ids.lg1.text
		lang2 = self.ids.lg2.text
		
		if lang1 == "Portugues":
			lang1 = "Ingles"
			lang2 = "Portugues"
		elif lang1 == "Ingles":
			lang1 = "Portugues"
			lang2 = "Ingles"
		
		self.ids.lg1.text = lang1
		self.ids.lg2.text = lang2

class Construtor(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "DeepPurple"
		return TextoSpk()

Construtor().run()
