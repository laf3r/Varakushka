from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

#author I. A. Gerasimov (@innokentiyG7)

def copy(event):
    print('copy')

def paste(event):
    print('paste')

def change_theme(theme):
    textfield['bg'] = themes[theme]['text_bg']
    textfield['fg'] = themes[theme]['text_fg']
    textfield['insertbackground'] = themes[theme]['cursor']
    textfield['selectbackground'] = themes[theme]['select_bg']

def change_font(change_font):
    textfield['font'] = fonts[change_font]['font']


def closeprogram():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if(answer):
        win.destroy()

def open_help():
   top= Toplevel(win)
   top.geometry("580x140")
   top.title("Справка")
   Label(top, text= "Разработчик: И. А. Герасимов \nСделано в образовательных целях в качестве учебного проекта", font=('Consolas 13 bold')).place(x=20,y=80)

def openfile():
    filepath = filedialog.askopenfilename(title='Открыть файл...', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if filepath:
        textfield.delete('1.0', END)
        textfield.insert('1.0', open(filepath, encoding='utf-8').read())
    
    
def extractPath(iowrapper):
    #Обрезание iowrapper в str
    stringtext = str(iowrapper)

    start ="<_io.TextIOWrapper name='"
    end ="' mode='w' encoding='cp1251'>"

    stringtext = stringtext.replace(start, "")
    stringtext = stringtext.replace(end, "")
    return stringtext
def savefile():
   filepath = filedialog.asksaveasfile(initialfile = 'Текстовый_файл.txt', defaultextension=".txt", filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
   filestring = extractPath(filepath)

   f = open(filestring, 'w', encoding='utf-8')
   text = textfield.get('1.0', END)
   f.write(text)
   f.close()
win = Tk()


win.title('Текстовый редактор Варакушка')
win.geometry('650x450')


textframe = Frame(win)
textframe.pack(fill=BOTH, expand=1)


#Меню
mainmenu = Menu(win)




#Файл
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть', command=openfile)
filemenu.add_command(label='Сохранить', command=savefile)
filemenu.add_separator()
filemenu.add_command(label='Закрыть', command= closeprogram)

#Вид
viewmenu = Menu(mainmenu, tearoff=0)
viewmenu_sub = Menu(viewmenu, tearoff=0)
fontmenu_sub = Menu(viewmenu, tearoff=0)

viewmenu_sub.add_command(label='Сепия', command=lambda: change_theme('sepia'))
viewmenu_sub.add_command(label='Белая', command=lambda: change_theme('white'))

viewmenu.add_cascade(label='Тема', menu=viewmenu_sub)

#Шрифты
fontmenu_sub.add_command(label='Consolas', command=lambda: change_font('Consolas'))
fontmenu_sub.add_command(label='Arial', command=lambda: change_font('Arial'))
fontmenu_sub.add_command(label='Times New Roman', command=lambda: change_font('TimesNewRoman'))
fontmenu_sub.add_command(label='Calibri', command=lambda: change_font('Calibri'))

viewmenu.add_cascade(label='Шрифт', menu=fontmenu_sub)
win.config(menu=viewmenu)

#Справка
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label='Об авторе', command=open_help)

#Добавление каскадов меню
mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Вид', menu=viewmenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)


win.config(menu=mainmenu)





themes = {
    'sepia': {
        'text_bg': '#F6EDDB', 'text_fg': 'black', 'cursor': 'black', 'select_bg' : '#b3b3b3'},
    'white': {'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg' : '#0078D7'}
    }

fonts = {
    'Consolas': {
        'font':'Consolas 12'
        },
    'Arial': {
        'font':('Arial', 12)
        },
    'Calibri': {
        'font':('Calibri', 12)
        },
    'TimesNewRoman': {
        'font':('Times New Roman', 12)
        },
    
    }

textfield = Text(textframe, bg='white', fg='black', padx=2.5, pady=2.5, wrap=WORD, insertbackground='black', spacing3=8, width=30, font = 'Consolas 12')
textfield.pack(expand=1, fill=BOTH, side=LEFT)


scroll = Scrollbar(textframe, command=textfield.yview)
scroll.pack(side=LEFT, fill=Y)
textfield.config(yscrollcommand=scroll.set)


win.bind('<Control-c>', copy)
win.bind('<Control-v>', paste)
win.bind('<Control-Cyrillic_em>', paste)
win.mainloop()
