from googletrans import Translator
import requests as re

tr = Translator()

def translate(text, lang):
	transl = tr.translate(text, dest=lang)
	trans = transl.text
	return trans, lang

text = input("Tarjima qilmoqchi bo'lgan matningizni kiriting: ")
lang = input("Tarjima qilmoqchi bo'lgan til kodini kiriting: ")
if True:
	try:
		if True:
			trmatn = translate(text, lang)[0]
			trlang = translate(text, lang)[1]
			print("Siz kiritgan so'z:", text)
			print("Tarjima qilingan matn:", trmatn)
			print("Tarjima tili:", trlang)
	except Exception as e:
		print("Xato, qayta urining!")
		
