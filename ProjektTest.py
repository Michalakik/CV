from tkinter import *

class Test(object):
    def __init__(self):
        self.auser = [False] * 10
        self.buser = [False] * 10
        self.cuser = [False] * 10
        self.duser = [False] * 10
        self.page_number = 0
        self.overview = False
        self.initialnt = False

        self.aoption = ["None"] * 10
        self.boption = ["None"] * 10
        self.coption = ["None"] * 10
        self.doption = ["None"] * 10
        self.question = ["None"] * 10
        self.aanswer = [False] * 10
        self.banswer = [False] * 10
        self.canswer = [False] * 10
        self.danswer = [False] * 10
    def pytanie(self,questionnumber,questiontext,atext,btext,ctext,dtext):
        if (type(questionnumber) is int) and (1 <= questionnumber <= 10) and all(isinstance(sub, str) for sub in (atext, btext, ctext, dtext,questiontext)):
            self.question[questionnumber-1] = questiontext
            self.aoption[questionnumber-1] = atext
            self.boption[questionnumber-1] = btext
            self.coption[questionnumber-1] = ctext
            self.doption[questionnumber-1] = dtext
    def odpowiedz(self,questionnumber,aanswer,banswer,canswer,danswer):
        if (type(questionnumber) is int) and (1 <= questionnumber <= 10) and all(isinstance(sub, bool) for sub in (atext, btext, ctext, dtext,questiontext)):
            self.aanswer[questionnumber-1] = aanswer
            self.banswer[questionnumber-1] = banswer
            self.canswer[questionnumber-1] = canswer
            self.danswer[questionnumber-1] = danswer
    def indivQA(self,questionnumber,abcd,text,answer):
        if (type(questionnumber) is int) and (1 <= questionnumber <= 10) and all(isinstance(sub, str) for sub in (atext, btext, ctext, dtext,questiontext)):
            if abcd == "a":
                self.aoption[questionnumber-1] = text
                self.aanswer[questionnumber-1] = answer
            if abcd == "b":
                self.boption[questionnumber-1] = text
                self.banswer[questionnumber-1] = answer
            if abcd == "c":
                self.coption[questionnumber-1] = text
                self.canswer[questionnumber-1] = answer
            if abcd == "d":
                self.doption[questionnumber-1] = text
                self.danswer[questionnumber-1] = answer
    def odpowiedzi(self,aanswer,banswer,canswer,danswer):
        if (aanswer,banswer,canswer,danswer is list):
            self.aanswer = aanswer
            self.banswer = banswer
            self.canswer = canswer
            self.danswer = danswer





def typ():
    possible_corrects = 0
    if nazwa_testu.aanswer[nazwa_testu.page_number]:
        possible_corrects += 1
    if nazwa_testu.banswer[nazwa_testu.page_number]:
        possible_corrects += 1
    if nazwa_testu.canswer[nazwa_testu.page_number]:
        possible_corrects += 1
    if nazwa_testu.danswer[nazwa_testu.page_number]:
        possible_corrects += 1
    if possible_corrects == 1:
        return True
    else:
        return False



def aktualizuj():
    global overview
    global page_number
    global pola
    global polew1
    global polew2
    global polew3
    global polew4
    global initialnt
    global ramka_new
    etykieta["text"] = "pytanie " + str(nazwa_testu.page_number + 1) + ": " + Test1.question[nazwa_testu.page_number]
    if nazwa_testu.initialnt:
        ramka_new.destroy()
    ramka_new = Frame(ramka)
    ramka_new.grid(row=1, column=0, sticky=W)


    if typ():
        polew1 = Radiobutton(ramka_new)
        polew1["text"] = " A: " + nazwa_testu.aoption[nazwa_testu.page_number]
        polew1["variable"] = pola
        polew1["value"] = "TFFF."
        #polew1["command"] = aktualizuj
        polew1.grid(row=1, column=0, sticky=W)

        polew2 = Radiobutton(ramka_new)
        polew2["text"] = " B: " + nazwa_testu.boption[nazwa_testu.page_number]
        polew2["variable"] = pola
        polew2["value"] = "FTFF"
        #polew2["command"] = aktualizuj
        polew2.grid(row=2, column=0, sticky=W)

        polew3 = Radiobutton(ramka_new)
        polew3["text"] = " C: " + nazwa_testu.coption[nazwa_testu.page_number]
        polew3["variable"] = pola
        polew3["value"] = "FFTF"
        #polew3["command"] = aktualizuj
        polew3.grid(row=3, column=0, sticky=W)

        polew4 = Radiobutton(ramka_new)
        polew4["text"] = " D: " + nazwa_testu.doption[nazwa_testu.page_number]
        polew4["variable"] = pola
        polew4["value"] = "FFFT"
        #polew4["command"] = aktualizuj
        polew4.grid(row=4, column=0, sticky=W)


    else:

        polew1 = Checkbutton(ramka_new)
        polew1["text"] = " A: " + nazwa_testu.aoption[nazwa_testu.page_number]
        polew1["variable"] = a[nazwa_testu.page_number]
        polew1.grid(row=1, column=0, sticky=W)
        #polew1["command"] = aktualizuj

        polew2 = Checkbutton(ramka_new)
        polew2["text"] = " B: " + nazwa_testu.boption[nazwa_testu.page_number]
        polew2["variable"] = b[nazwa_testu.page_number]
        polew2.grid(row=2, column=0, sticky=W)
        #polew2["command"] = aktualizuj

        polew3 = Checkbutton(ramka_new)
        polew3["text"] = " C: " + nazwa_testu.coption[nazwa_testu.page_number]
        polew3["variable"] = c[nazwa_testu.page_number]
        polew3.grid(row=3, column=0, sticky=W)
        #polew3["command"] = aktualizuj

        polew4 = Checkbutton(ramka_new)
        polew4["text"] = " D: " + nazwa_testu.doption[nazwa_testu.page_number]
        polew4["variable"] = d[nazwa_testu.page_number]
        polew4.grid(row=4, column=0, sticky=W)
        #polew4["command"] = aktualizuj
    nazwa_testu.initialnt = True
    if nazwa_testu.overview:
        answer_desc()



def answer_desc():
    text = ""
    polew1.configure(state=DISABLED)
    polew2.configure(state=DISABLED)
    polew3.configure(state=DISABLED)
    polew4.configure(state=DISABLED)
    text += "Klucz:\n"
    if nazwa_testu.aanswer[nazwa_testu.page_number]:
        text += "Dobrze " + polew1["text"] + "\n"
    else:
        text += "Źle " + polew1["text"] + "\n"
    if nazwa_testu.banswer[nazwa_testu.page_number]:
        text += "Dobrze " + polew2["text"] + "\n"
    else:
        text += "Źle " + polew2["text"] + "\n"
    if nazwa_testu.canswer[nazwa_testu.page_number]:
        text += "Dobrze " + polew3["text"] + "\n"
    else:
        text += "Źle " + polew3["text"] + "\n"
    if nazwa_testu.danswer[nazwa_testu.page_number]:
        text += "Dobrze " + polew4["text"] + "\n"
    else:
        text += "Źle " + polew4["text"] + "\n"
    poletext.delete(0.0, END)
    poletext.insert(0.0, text)



def next():

    if nazwa_testu.page_number < 9:
        if nazwa_testu.overview:
            nazwa_testu.page_number += 1

            aktualizuj()
            recall()

        else:
            remember()
            nazwa_testu.page_number += 1

            aktualizuj()
            recall()


def previous():

    if nazwa_testu.page_number > 0:
        if nazwa_testu.overview:
            nazwa_testu.page_number -= 1

            aktualizuj()
            recall()

        else:
            remember()
            nazwa_testu.page_number -= 1

            aktualizuj()
            recall()


def finish():

    if nazwa_testu.overview:
        nazwa_testu.overview = False
        fullreset()
        przycisk3.config(text="Zakończ test")
        poletext.delete(0.0, END)
    else:
        remember()
        nazwa_testu.overview = True
        result()
        polew1.configure(state=DISABLED)
        polew2.configure(state=DISABLED)
        polew3.configure(state=DISABLED)
        polew4.configure(state=DISABLED)
        przycisk3.config(text="Nowy test")



def reset():

    if typ():
        polew1.select()

    else:
        polew1.deselect()
        polew2.deselect()
        polew3.deselect()
        polew4.deselect()



def fullreset():

    reset()
    aktualizuj()
    nazwa_testu.auser = [None] * 10
    nazwa_testu.buser = [None] * 10
    nazwa_testu.cuser = [None] * 10
    nazwa_testu.duser = [None] * 10


def recall():

    reset()
    if nazwa_testu.auser[nazwa_testu.page_number]:
        polew1.select()
    if nazwa_testu.buser[nazwa_testu.page_number]:
        polew2.select()
    if nazwa_testu.cuser[nazwa_testu.page_number]:
        polew3.select()
    if nazwa_testu.duser[nazwa_testu.page_number]:
        polew4.select()


def remember():

    if typ():

        if pola.get()[0] == "T":
            nazwa_testu.auser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.auser[nazwa_testu.page_number] = False

        if pola.get()[1] == "T":
            nazwa_testu.buser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.buser[nazwa_testu.page_number] = False

        if pola.get()[2] == "T":
            nazwa_testu.cuser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.cuser[nazwa_testu.page_number] = False

        if pola.get()[3] == "T":
            nazwa_testu.duser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.duser[nazwa_testu.page_number] = False

    else:
        if a[nazwa_testu.page_number].get():
            nazwa_testu.auser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.auser[nazwa_testu.page_number] = False
        if b[nazwa_testu.page_number].get():
            nazwa_testu.buser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.buser[nazwa_testu.page_number] = False
        if c[nazwa_testu.page_number].get():
            nazwa_testu.cuser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.cuser[nazwa_testu.page_number] = False
        if d[nazwa_testu.page_number].get():
            nazwa_testu.duser[nazwa_testu.page_number] = True
        else:
            nazwa_testu.duser[nazwa_testu.page_number] = False


def result():
    points = 0.0
    for i in range(10):
        corrects = 0
        if nazwa_testu.aanswer[i] == nazwa_testu.auser[i] and nazwa_testu.auser[i]:
            corrects += 1
        if nazwa_testu.banswer[i] == nazwa_testu.buser[i] and nazwa_testu.buser[i]:
            corrects += 1
        if nazwa_testu.canswer[i] == nazwa_testu.cuser[i] and nazwa_testu.cuser[i]:
            corrects += 1
        if nazwa_testu.danswer[i] == nazwa_testu.duser[i] and nazwa_testu.duser[i]:
            corrects += 1

        wrongs = 0
        if nazwa_testu.aanswer[i] != nazwa_testu.auser[i] and nazwa_testu.auser[i]:
            wrongs += 1
        if nazwa_testu.banswer[i] != nazwa_testu.buser[i] and nazwa_testu.buser[i]:
            wrongs += 1
        if nazwa_testu.canswer[i] != nazwa_testu.cuser[i] and nazwa_testu.cuser[i]:
            wrongs += 1
        if nazwa_testu.danswer[i] != nazwa_testu.duser[i] and nazwa_testu.duser[i]:
            wrongs += 1

        if (corrects - wrongs) > 0:
            possible_corrects = 0
            if nazwa_testu.aanswer[i]:
                possible_corrects += 1
            if nazwa_testu.banswer[i]:
                possible_corrects += 1
            if nazwa_testu.canswer[i]:
                possible_corrects += 1
            if nazwa_testu.danswer[i]:
                possible_corrects += 1

            if possible_corrects == 0:
                points += 0
            if possible_corrects == 1:
                points += (corrects-wrongs) / possible_corrects
            if possible_corrects == 2:
                points += (corrects-wrongs) / possible_corrects
            if possible_corrects == 3:
                points += (corrects-wrongs) / possible_corrects
            if possible_corrects == 4:
                points += (corrects-wrongs) / possible_corrects

    text = "Otrzymano: " + str(points) + " punktów\nSposób liczenia: \n(poprawne-niepoprawne)/(możliwe_poprawne)\nkiedy za pytanie wychodzi mniej niż 0 punktów przyznawane jest za nie 0 punktów"
    poletext.delete(0.0, END)
    poletext.insert(0.0, text)

def main():
    global Test1
    global etykieta
    global ramka
    global nazwa_testu
    global pola
    global a
    global b
    global c
    global d
    global poletext
    global przycisk1
    global przycisk2
    global przycisk3
    Test1 = Test()
    #C
    Test1.pytanie(1,"CAPTCHA to technika zabezpieczeń na stronach WWW pozwalająca","przyspieszyć proces logowania do aplikacji internetowej. ","pominąć proces uwierzytelniania do aplikacji internetowej. ","potwierdzić, że dane z formularza są wysyłane przez człowieka. ","automatycznie wypełnić formularz logowania danymi użytkownika. ")
    #C
    Test1.pytanie(2,"Wskaż komentarz wieloliniowy w języku PHP","#"," / / ","/* */ ","<!-- --> ")
    #C
    Test1.pytanie(3,"Którego polecenia nalezy użyć, aby wyraz TEKST został wyświetleny w kolorze czarnym w oknie przeglądarki internetowej?","< body color=\"black\" > TEKST < /font > ","< font color=\"czarny\" > TEKST < /font > "," < font color=\"#000000\" > TEKST < /font > ","< body bgcolor=\"black\" > TEKST < /body > ")
    #D
    Test1.pytanie(4,"W poleceniach, których celem jest odtwarzanie na stronie internetowej dźwięku jako podkładu muzycznego NIE wykorzystuje się atrybutu","loop=\"10\" ","balance=\"-10\" ","volume=\"-100\" ","href=\"C:/100.wav\" ")
    #C
    Test1.pytanie(5,"Jakiego znacznika należy użyć, aby przejść do kolejnej linii tekstu, nie tworząc akapitu na stronie interenetowej ?","< p > ","< /b > ","< br > ","< /br > ")
    #A
    Test1.pytanie(6,"Kaskadowe arkusze stylów tworzy się w celu","ułatwienia formatowania strony ","nadpisywania wartości znaczników już ustawionych na stronie","połączenia struktury dokumentu strony z właściwą formą jego prezentacji","blokowania jakichkolwiek zmian w wartościach znaczników już przypisanych w pliku CSS ")
    #C
    Test1.pytanie(7,"W podanej regule CSS: h1 {color: blue} h1 oznacza","klasę ","wartość ","selektor ","deklarację ")
    #D
    Test1.pytanie(8,"Edytor spełniający założenia WYSIWYG musi umożliwiać","tworzenie podstawowej grafiki wektorowej ","publikację strony na serwerze poprzez wbudowanego klienta FTP ","obróbkę plików dźwiękowych przed umieszczeniem ich na stronie internetowej ","uzyskanie zbliżonego wyniku tworzenej strony do jej obrazu w przegladarce interenetowej ")
    #A,C
    Test1.pytanie(9,"Do graficznego tworzenia stron internetowych należy wykorzystać.","Google Web Designer ","przeglądarkę internetową ","program typu WYSIWYG ","program MS Office Picture Manager ")
    #A,B,C
    Test1.pytanie(10,"Które z tych programów mogą służyć do programowania w języku python ?","PyCharm","nano","Notepad++","Microsoft Paint")
    Test1.odpowiedzi([False, False, False, False, False, True, False, False, True, True],[False, False, False, False, False, False, False, False, False, True],[True, True, True, False, True, False, True, False, True, True],[False, False, False, True, False, False, False, True, False, False])


    nazwa_testu = Test1

    okno = Tk()
    okno.geometry("800x300")
    okno.title("Test")
    ramka = Frame(okno)
    ramka.grid()
    etykieta = Label(ramka)
    etykieta["text"] = "pytanie " + str(nazwa_testu.page_number + 1) + ": " + Test1.question[nazwa_testu.page_number]
    etykieta.grid(row=0, column=0, sticky=W)

    a = [BooleanVar()] * 10
    b = [BooleanVar()] * 10
    c = [BooleanVar()] * 10
    d = [BooleanVar()] * 10

    pola = StringVar()
    pola.set(None)

    aktualizuj()
    reset()

    poletext = Text(ramka, width=100, height=6)
    poletext.grid(row=5, column=0, sticky=W)

    przycisk1 = Button(text="Następne pytanie", width=18)
    przycisk1.grid(row=6, column=0, sticky=W)
    przycisk1["command"] = next
    przycisk2 = Button(text="Poprzednie pytanie", width=18)
    przycisk2.grid(row=7, column=0, sticky=W)
    przycisk2["command"] = previous

    przycisk3 = Button(text="Zakończ test", width=18)
    przycisk3.grid(row=8, column=0, sticky=W)
    przycisk3["command"] = finish

    okno.mainloop()
main()