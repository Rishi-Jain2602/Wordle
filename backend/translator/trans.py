from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com'
    ])

def translate_lang(text,lang):
  translation = translator.translate(text, dest=lang)
  return translation.text
