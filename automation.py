import time                                     
import os 
import textwrap                           
import wikipedia                                
import webbrowser                               
import playsound                                
import speech_recognition as speech             
from gtts import gTTS                           
from googlesearch import search                 
from datetime import datetime                 
import tkinter as tk                            


today = datetime.now().strftime("%d/%m/%Y and time is %H:%M")

wlcmsg = "Hello hope you are doing fine,\nThe today's date is {}.\n ".format(today)

def gsearch(content):                                                        #google search function
    links= []
    for i in search(content,  tld='com', num=5, start=0,stop=5, pause=2.0):
        links.append(i)
    return links

def urlsearch(url):                                                          #link search function
    return webbrowser.open(url)

def voice(text):                                                             #Text to Speech function
    audio = gTTS(text= text,lang= 'en', slow=False )
    filename = "voice.mp3"
    audio.save("audiofiles/{}".format(filename))
    playsound.playsound("audiofiles/{}".format(filename))
    
def wiki_search(content):                                                    #wiki search function and return a summary
    return textwrap.wrap(wikipedia.summary(content),width= 130)

def open_file(app):                                                          #open file function
    from platform import system
    system = system()

    if system == 'Windows':
        def find(path):
            os.chdir(path)
            dirs=tuple(os.listdir(path))
            for name in dirs:
                if name==app:
                    os.startfile(path+'\\'+name)
                    break
                else:
                    try:
                        find(path+'\\'+name)
                        
                    except:
                        pass 
        find('C:\\')
        find('D:\\')
        find('E:\\')

    else:
        print("Not supported")
        return
    
def web_gui():                                                               #gui for google search, link opening and wiki search
    
    def close_window():
        root1.destroy()
       
    root1 = tk.Tk()
    root1.title('Web')
    #root1.resizable(0, 0)
    
    canvas = tk.Canvas(root1, bg = "black")
    canvas.pack()

    hello = tk.Label(canvas,text = wlcmsg+'\n Dont know something just google it! : ) \n or search the web or \n do some wiki search ; )',  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("agency fb","20"))
    hello.pack()

    entry = tk.Entry(root1, width = 50)
    entry.pack()

    def gclick():
        result = gsearch(entry.get())
        for i in result:
            label = tk.Label(root1, text = i ,fg = "black" ,font=("berlin sans fb","15"))
            label.pack()

    def wikiclick():       
        result = wiki_search(entry.get())
        for i in result:
            label = tk.Label(root1, text = i,fg = "black",font=("berlin sans fb","15"))
            label.pack()

    def urlclick():
        urlsearch('http:'+entry.get())

    gglsrc = tk.Button(canvas,text = "Search the amazing world of Google", fg = "white", bg = "black",font = ("berlin sans fb","15"), command = gclick)#google search
    gglsrc.pack()

    websearch = tk.Button(canvas,text = "Open a Website", fg = "white", bg = "black",font=("berlin sans fb","15"), command = urlclick)#google search
    websearch.pack()

    wiki = tk.Button(canvas,text = "Do a wiki search", fg = "white", bg = "black",font=("berlin sans fb","15"), command = wikiclick)#google search
    wiki.pack()

    exit = tk.Button(canvas,text = "back",padx = 50, pady = 20,  fg = "white", bg = "black",font = ("berlin sans fb","15"),command = lambda: [close_window(),gui()])
    exit.pack()

def openfile_gui():                                             #gui for file opener
    
    def close_window():
        root2.destroy()
        
    root2 = tk.Tk()
    root2.title('Open File or App')
    root2.resizable(0, 0)

    canvas = tk.Canvas(root2, bg = "black")
    canvas.pack()

    hello = tk.Label(canvas,text = wlcmsg+"\n Dont know where a file is, I'll find it for you, Just type the name and click to open  ; )",  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("agency fb","20"))
    hello.pack()

    entry = tk.Entry(root2, width = 50)
    entry.pack()
    
    def openfile_click():
        open_file(entry.get())
        
    opnfl = tk.Button(canvas,text = "Click to Open", fg = "white", bg = "black",font = ("berlin sans fb","15"), command = openfile_click)#google search
    opnfl.pack()
    
    exit = tk.Button(canvas,text = "back",padx = 50, pady = 20,  fg = "white", bg = "black",font = ("berlin sans fb","15"),command = lambda: [close_window(),gui()])
    exit.pack()
    
    NB = tk.Label(canvas,text = "NB: If the file is not opening even after 2 minute,the file do not exist",  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("berlin sans fb","15"))
    NB.pack()
    
def tts_gui():                                                         #gui for tts
    def close_window():
        root3.destroy()

    root3 = tk.Tk()
    root3.title('Text To Speech')
    root3.resizable(0, 0)

    canvas = tk.Canvas(root3, bg = "black")
    canvas.pack()

    hello = tk.Label(canvas,text = wlcmsg+"\n Type anything and I'll say it back :)",  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("agency fb","20"))
    hello.pack()

    entry = tk.Entry(root3, width = 50)
    entry.pack()
    def say_click():
        voice(entry.get())
    ttss = tk.Button(canvas,text = "Click to Say", fg = "white", bg = "black",font = ("berlin sans fb","15"), command = say_click)#google search
    ttss.pack()
    
    exit = tk.Button(canvas,text = "back",padx = 50, pady = 20,  fg = "white", bg = "black",font = ("berlin sans fb","15"),command =lambda:[close_window(),gui()])
    exit.pack()
   
def gui():                                                              #main window gui
    def close_window():
        root.destroy()

    root = tk.Tk()
    root.title('Automation')
    root.resizable(0, 0)
    
    canvas = tk.Canvas(root, bg = "black")
    canvas.pack()

    hello = tk.Label(canvas,text = wlcmsg,  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("agency fb","20"))
    hello.pack()

    openfile = tk.Button(canvas,text = "Open a File",  fg = "white", bg = "black",font = ("berlin sans fb","15"),command = lambda: [openfile_gui(),close_window()] )#open a file
    openfile.pack()

    gglsrc = tk.Button(canvas,text = "Open a Website or\nSearch the amazing world of Google", fg = "white", bg = "black",font = ("berlin sans fb","15"),command  = lambda: [web_gui(),close_window()])#google search
    gglsrc.pack()

    tts = tk.Button(canvas,text = "Want to know how a sentence sounds, Go ahead I'll tell you",padx = 50, pady = 20,  fg = "white", bg = "black",font = ("berlin sans fb","15"),command = lambda: [tts_gui(), close_window()])#text to voice
    tts.pack()
    
    NB = tk.Label(canvas,text = "NB: During the services requiring input, Input first(When a text box comes below) and then click the required Button NOT THE OTHER WAY!!!",  padx = 50, pady = 20,fg = "white", bg = "black" ,font = ("berlin sans fb","15"))
    NB.pack()

    exit = tk.Button(canvas,text = "exit",padx = 50, pady = 20,  fg = "white", bg = "black",font = ("berlin sans fb","15"),command = close_window)
    exit.pack()

    root.mainloop()
gui()
