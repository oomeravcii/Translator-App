
#! pip install googletrans==3.1.0a0
#! to install googletrans module.

#? Automatically detecting a language

import googletrans
translator = googletrans.Translator()

text = "Bu bir test. Bir iki üç"

translated_text = translator.detect(text)
print(translated_text.lang) # Shows the detected language
print(translated_text.confidence) # Shows the confidence between 0.0 to 1.0

#? Simple translation: from [Any detected language] --- to --> [Default language(english)]

import googletrans
translator = googletrans.Translator()

text = "Merhaba, bu bir test!"

translated_text = translator.translate(text)
print(translated_text)

#? Advanced translation: from [Any language we want] --- to ---> [Any language we want(data,source,destination)]

import googletrans
translator = googletrans.Translator()

text = "Bu bir test. Bir iki üç"

translated_text = translator.translate(text, src="tr", dest="en")
print(translated_text) # Shows all info
print(translated_text.origin) # Shows original text
print(translated_text.text) # Shows translated text

#? Translating as list

import googletrans
translator = googletrans.Translator()

text = ["Bu bir yazı", "Bu iki yazı", "Bu üç yazı"] # Creating a list

translated_list = translator.translate(text, src="tr", dest="de")

for elements in translated_list: # Printing translated version of every elements inside of the list using for loop
    print(f"{elements.origin}: {elements.text}")