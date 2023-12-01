import customtkinter as ctk
from tkinter import messagebox
from googletrans import Translator


# function to auto translate (detects the written language)
def auto_translate(data, var_dest):
    translator = Translator()
    
    detect_text_lang = translator.detect(data)
    detected_text_lang = detect_text_lang.lang # getting the language of the text
    translated_text = translator.translate(data, src=detected_text_lang, dest=var_dest)
    return translated_text.text

# function to manual translate
def manual_translate(data, var_src, var_dest):
    translator = Translator()
    
    translated_text = translator.translate(data, src=var_src, dest=var_dest)
    return translated_text.text

# function for the button
def button_clicked():
    
    # getting the variables
    text = from_textbox.get("1.0",'end-1c')
    source = from_combobox.get()
    destination = to_combobox.get()
    
    if text == "":
        messagebox.showerror(title="Error",message="Input field can't be empty!")
    
    else:
        
        if source == "detect":
            translated_text = auto_translate(text, destination)
            to_textbox.configure(state="normal") # make textbox editable
            to_textbox.delete("1.0", ctk.END) # clear textbox
            to_textbox.insert("1.0", translated_text) # write inside textbox
            to_textbox.configure(state="disabled") #make textbox uneditable

        else:
            translated_text = manual_translate(text, source, destination)
            to_textbox.configure(state="normal") # make textbox editable
            to_textbox.delete("1.0", ctk.END) # clear textbox
            to_textbox.insert("1.0", translated_text) # write inside textbox
            to_textbox.configure(state="disabled") #make textbox uneditable


# creating tkinter window
window = ctk.CTk()
ctk.set_default_color_theme("green")
window.title("Translator")

# window size settings
window.geometry("950x610+450+180")
window.minsize(950, 600)

# responsive frame
main_frame = ctk.CTkFrame(window, fg_color=("white","#2c2c2c"))
main_frame.pack(fill=ctk.BOTH, expand=True, pady="5p", padx="5p")

# translator text
translator_label = ctk.CTkLabel(main_frame, text="Translator", text_color="#4285F4",font=("Roboto",50,"bold"), fg_color=("#FAF9F6","#042e29"), corner_radius=10)
translator_label.pack(pady=(10,0))

# more frames for window management
from_frame = ctk.CTkFrame(main_frame, fg_color=("#e7f5ee","#0f9d58"), corner_radius=20)
from_frame.pack(side="left", fill=ctk.BOTH, expand=True, padx="5p", pady=(10,50))

to_frame = ctk.CTkFrame(main_frame, fg_color=("#fbeceb","#db4437"), corner_radius=20)
to_frame.pack(side="right", fill=ctk.BOTH, expand=True, padx="5p", pady=(10,50))

# translate button
translate_button = ctk.CTkButton(main_frame, text="Translate", fg_color="#4285F4", height=40, width=200, command=button_clicked)
translate_button.place(relx=0.5, rely=1.0, anchor="s")

# "from" frame widgets
from_label = ctk.CTkLabel(from_frame, text="From: ", font=("Roboto",15,"bold"))
from_label.grid(row=0, column=0, padx=(30,0), pady=10)

from_languages = [
    'detect',
    'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 
    'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 
    'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 
    'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 
    'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 
    'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 
    'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 
    'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 
    'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 
    'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 
    'yiddish', 'yoruba', 'zulu'
]

from_combobox = ctk.CTkComboBox(from_frame, values=from_languages)
from_combobox.grid(row=0, column=1, pady=(1,0))
from_combobox.set("detect") # Default value

from_textbox = ctk.CTkTextbox(from_frame, width=300, height=390)
from_textbox.place(relx=0.5, rely=0.55, anchor="center")

# "to" frame widgets
to_label = ctk.CTkLabel(to_frame, text="To: ", font=("Roboto",15,"bold"))
to_label.grid(row=0, column=0, padx=(50,0), pady=10)

to_languages = [
    'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 
    'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 
    'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 
    'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 
    'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 
    'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 
    'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 
    'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 
    'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 
    'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 
    'yiddish', 'yoruba', 'zulu'
]

to_combobox = ctk.CTkComboBox(to_frame, values=to_languages)
to_combobox.grid(row=0, column=1, pady=(1,0))
to_combobox.set("english") # Default value

to_textbox = ctk.CTkTextbox(to_frame, width=300, height=390, state="disabled")
to_textbox.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()
