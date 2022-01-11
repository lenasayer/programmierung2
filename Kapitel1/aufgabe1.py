##1
#Klassendef?
#beschriebt Struktur eines Objekts, welches aus Attributen+Methoden besteht, Beschreibung eines Objekttyps - nicht Objekt selbst
# theoretischer Bauplan einer Klasse mit Attributen + Methoden
# Instanz?
# Methode der Klassen wird aufgerufen, Realisierung einer Klassendef mit eigenen Werten der Klassenattribute


class Fenster:
    def __init__(self,laenge,breite):
        self.laenge = laenge
        self.breite = breite 

    def __str__(self):
        return f"{self.laenge},{self.breite}" #bis hierhr Klassendef

a = Fenster(2.5,3) #Instanz
print(a)

##2
#magische Methoden?
# Methoden, welche Klasse spezielle Fähigkeiten gibt, mit zwei unterstrichen, implizit: werden automatische abgerufen bei best. Def in den Instanzen, sehr einfach!! (Bsp.str in Zeichenkette)

##3
class Stadt:
    def __init__(self, name, einwohner, land, koordinate):
        self.name = name
        self.einwohnerzahl = einwohner
        self.land = land
        self.koordinate = koordinate

    def __str__(self):
        return f"Stadt: {self.name},Einwohnerzahl:{self.einwohnerzahl},Land:{self.land},Koordinate:{self.koordinate}"

# wieso eigene Klasse für Datentyp "tuple" und "Str"?
# für Koordinate: einfacher um Bedingungen festzulegen und Form (7Stellen für Schweiz)
# für Land: 1 zu n Beziehung, Land muss bei jedem Attribut neu beschrieben werden, als Klasse nur einmal

##4
#'Was wird direkt aufgerufen bei neuer Instanz? Konstruktor'
#Ausgabe dieses Programms? print(k.id) ->200 
# Was ist wahr? int(3).__add__(2) ginbt 5; Es können mehrere Instanzen für eine Klasse erzeugt werden; Wird Klasse vererbt, muss Konstruktor durch super().__init__() manuell aufgerufen werden um Attribute korrekt initilisiert werden
# Ausgabe dieses Programms? print(Test(5)) -> 5
##5
class Roman:
    def __init__(self, roman):
        self.roman = roman
    
    def __add__(self,other):
        return self.int_to_Roman(self.roman_to_int(self.roman),self.roman_to_int(other.roman))

    def __int__(self):
        return self.roman_to_int(self.roman)

    def __str__(self):
        return f"{self.roman}"

    def int_to_Roman(num):
        pass

    def roman_to_int(s):
        pass

##6
class Student:
    def __init__(self,name,vorname,gender,imm_nr,age=0):
        self.name = name
        self.vorname = vorname
        self.gender=gender
        self.imm_nr = imm_nr
        self.setAge(age)
        self.mark = {}

    def setAge(self,age):
        self.age= age

    def setMark(self,topic,mark):
        self.mark[topic] = mark

    def display(self):
        print(self.name,self.vorname,self.gender,self.imm_nr,self.age,self.mark)
    
b = Student("Sayer","Lena","weiblich","1234")
Student.display(b)

###Neu
##4
class Dreieck:
    def __init__(self,A,B,C):
        self.A,self.B,self.C = A,B,C
    
    def Strecken(self):
        self.a = Strecke(B,C)
        self.b = Strecke(A,C)
        self.c= Strecke(A,B)

    def Flaeche(self):
        self.Strecken()
        s = (self.a.laenge()+self.b.laenge()+self.c.laenge())/2
        F = (s*(s-self.a.lange())*(s-self.b.lange())*(s-self.c.laenge()))*0.5
        return F

    def Umfang(self):
        self.Strecken()
        return self.a.laenge()+ self.b.laenge()+self.c.laenge()

    def Inkreisradius(self):
        self.Strecken()
        return 2*self.Flaeche()/(self.a.laenge()+self.b.laenge()+self.c.laenge())


class Punkt:
    pass
class Strecke:
    pass

A = Punkt()
B = Punkt()
C = Punkt()

##5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#layout = QFormLayout()
#event = QLineEdit()
#calendar = QCalendarWidget()
#button = QPushButton("Ok")

#layout.addRow("Event-Name",event)
#layout.addRow("Datum", calendar)
#layout.addRow(button)

##6
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Währungsumrechner")
        self.show()

        layout = QFormLayout()

        self.chf = QLineEdit()
        self.euro = QLineEdit()
        self.button = QPushButton("Umrechnen")
        layout.addRow("Schweizer Franken", self.chf)
        layout.addRow("Euro", self.euro)
        layout.addRow(self.button)

        self.button.clicked.connect(self.umrechnen)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    def umrechnen(self):
        try:
            chf = self.chf.text()
            euro = float(chf)*0.876
            self.euro.setText(str(euro))
        except:
            self.chf.setText("ungültiger Wert")

app=QApplication([])
f = MyWindow()
app.exec()


