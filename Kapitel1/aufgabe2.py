
##2021
#1) Erstellen Sie Klasse "Kreis" mit Methoden Umfang, Flaeche, Mittelpunkt

import math

class Kreis():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    
    def umfang(self):
        return self.r*2*math.pi

    def flaeche(self):
        return self.r**2*math.pi
    
    def mittelpunkt(self):
        return str(self.x), str(self.y)

k = Kreis(10,-1,5)
print(k.umfang()) #etc.

#2) Vorteile der Versionsverwaltung von Python Code mit git resp. GitHub?
# schnell, leistungsfähig, revolutionär
# super für Teamarbeit und guter Datenschutz

#3) Welche Methoden für Zugriff auf entsprechende Wig´dgets?
# QLineEdit - text()
#QCheckBox - isChecked()
# QTimeEdit - time()
# QDateEdit - date()
# QComboBox - currentIndex()
# QSlider - value()

#4) Wahr Falsch?
# um GUI- Elemente anzuordnen gibt es Layouts (GridLayout etc.) -wahr
# mit MessageBox warning kann dialog geöffnet werden mit warnsymbol und text - wahr
# QProgressBar ist Statusanzeige, welche Forschritt einer Operation anzeigt - wahr

#5) Klasse Point ist gegeben
#a) erstelle Instanz
p = Point(10,20)
#b) für was kann _str_ verwendet werden?
# Resultat eines Objektes in String umwandeln
#c) Klasse in anderem Projekt wieder verwenden. Wie?
# import der py-Datei mit (z.B. from point.py import *)
# bei neuer Klasse (Vererbung) z.b. class Kreis(Point):

#6) wahr falsch?
# GitHub unterstützt Entwickler bei Verfolgung von Codeänderung in Projekten - wahr
# Python nutzt Ausnahmebehandlung als Mittel, um Fehlerbed. zu testen. Innerhalb Klasse nicht verwendbar - falsch
# Magische Methoden werden für Spezialeffekte in Filmindustrie verwendet - falsch
# Klasse dient als Bauplan für reale Objekte in Softwareobjekte und beschreibt Attribute - wahr

#7) erstellen von 100 Zahlen im Bereich -10,10
import numpy as np
a = np.linspace(-10,10,100)
print(a)

##2018

#1 a) Nennen Sie ein Bsp eines Signals für QCheckBox und QRadioButton
# und erstelle kleines Beispiel
# b) Wie kann auf Text von QLabel zugegriffen werden? wie verändern?
from PyQt5.QtWidgets import *
#  Rest siehe Prüfung1 Aufgabe 5

#2) Terminplaner implementieren

# siehe Prüfung 1 Aufgabe 6

#3) GUI ist erstellt mit Meilen/Kilometer und Button
# Code für Umwandlung wird gefragt

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
# siehe Prüfung1 Aufgabe 7

#4) Wahr oder falsch?

# In numpy können einzelne Arrays nur einen einzigen Datentypen enthalten - wahr
#Die Bibliothek Pandas wird heute vor allem in Filmindustrie eingesetzt. Kung Fu Panda wurde erstellt. daher kommt der Name - falsch
# Das Modul "matplotlib" muss installiert werden, gehört nicht zum Standardumfang von Python - wahr
# Mit QtDesigner können GUI erstellt werden. Diese werden in XML basierten ui-Files gespeichert. - wahr
# Dieses Programm stürzt nach Installation von numpy ab: import numpy as np       s = np.array([1,2,3])   - falsch
# In numpy wird mit np.arange(1,5) folgendes array erstellt: array([1,2,3,4,5])   - falsch

#5) Gegeben ist Liste data bestehend aus Tupeln mit Kantonsnamen und Wahlbeteiligung
# mit Pandas wird daraus Dataframe erstellt, und Spalten bekommen Namen "kanton" und "wahlbeteiligung"
import pandas as pd
from pandas.core.indexes.base import InvalidIndexError
data = [("Zürich", 47.2),("Bern", 59.1)]  #usw
df = pd.DataFrame(data)
df.columns = ["kanton","wahlbeteiligung"]
# Wie kann ein neues Dataframe erstellt werden für alle Kantone mit Wahlbeteiligung >50%?
df[df['wahlbeteiligung']>50]

#6) Schreiben sie Python-Programm, welches überprüft, dass "numpy" installiert ist.

try:
    import numpy
except ImportError:
    print("numpy ist nicht installiert")

#7) a) Was passiert, wenn diese Zeile im Jupyter Notebook ausgeführt wird?
from matplotlib.pyplot import *

axis("equal")
plot([1,2,3,4,5],[3,3,3,2,2], "bo-")
show()

# Es wird ein Plot-Fenster erstellt, in dem die Punkt als blaue Kreise erscheinen
# & verbunden sind mit einer durchgezogenen Linie
# erste Liste = x-Werte, zweite Liste = y- Werte
# mit axis('equal') sind Ko-Achsen gleich skaliert

#b)
import numpy as np

a = np.array([1,2,3], dtype=np.float)
b = np.array([2,3,4], dtype=np.float)
a*b

# Die beiden Arrays werden elementweise multipliziert
# Das Resultat ist ein Array[2,6,12]
# Der Datentyp des Elements ist float.

## 2016:

#1) a) Nennen sie je 2 Signale für QPushButton und QlineEdit und erstellen Sie ein Bsp
#button.pressed.connect('Funktion')
#button.clicked.connect('Funktion')

#lineedit.textChanged('txt')
#lineedit.editingFinished()

#b) Wie kann auf den Text QLineEdit zugegriffen werden?
#QLineEdit.text()

#2) Folgender Code wird ausgeführt- was passiert?

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline 
x = np.linspace(1,2,10)
y = x*x
plt.axis("equal")
plt.plot(x,y, 'ko-')
#(show())
#was ist Resultat?

# 3) Welche Klassen und Instanzen sind in Pacman denkbar?

##2016
#1) Vorteile von Jupyter Notebook gegenüber herkömmlichen Entwicklungsumgebungen?
# die Resultate werden gleich visualisiert
# Ablauf eines Programms mit alles Zwischenresultaten leichter nachvollziehbar

#2) wahr oder falsch?
# Jupyter N. wurde programmiert für gutes Tool zur Jupiter Mission der NASA - falsch
#für QGIS können Plugins mittels Python programmiert werden - wahr
# mit QGIS können Shapefiles & GeoTIFFS geöffnet und dargestellt werden - wahr
# QGIS unterstützt nur Python Version 3.4 plus höher - falsch
# Jupiter N. ist Web-Applikation. Python-Code wird in Browser angezeigt - wahr
# numpy muss zusätzlich installiert werden - wahr
# matplotlib.patches ermöglicht zeichnen von Figuren - wahr
#QGIS ist Open Source, dh. Qelltext frei verfügbar - wahr

#3) Aufgabe mit data mit Kantonsnamen und Wahlbeteiligung
#a) 5 Kantonsnamen mit höchster Wahlbeteiligung ermitteln

import operator
data.sort(key = operator.itemgetter(1))
#for i in range(0,5):
    #print(data[i])

#b) 5 Kantonsnamen mit kleinster W
#for i in range (1,6):
    #print(data[len(data)-i])

#4) Funktion y = 1/2 x^2 - 1 plotten
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,20)
y = 0.5*x*x -1
plt.plot(x,y,"ro-")
plt.show()

##2014
#1) Terminplaner
#2) Converter Celsius/Fahrenheit
#3) Es soll ein GUI aufgebaut werden, bei dem eine Datei zum Speichern ausgewählt wird.
# Beim Klicken auf "Select File" erscheint ein Filedialog, welcher eine Text-Datei zum 
# Speichern auswählt. Wird eine Datei slektiert, so erscheint der Dateiname in einem Label darunter.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()
    
    def createLayout(self):
        self.setWindowTitle("Speicherung...")

        layout = QHBoxLayout()
        layoutV= QVBoxLayout()

        self.but = QPushButton("Select File...")
        self.url = QLineEdit()
        self.lab = QLabel("File:")
        self.label = QLabel("")

        layout.addWidget(self.lab)
        layout.addWidget(self.url)
        layout.addWidget(self.but)

        layoutV.addLayout(layout)
        layoutV.addWidget(self.label)

        center = QWidget()
        center.setLayout(layoutV)

        self.setCentralWidget(center)

        self.show()
        self.raise_()

    def createConnects(self):
        self.but.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern","C:data", "Text (.txt)")
        if (filename != ""):
            self.url.setText(filename)
            self.label.setText(filename)
        

app = QApplication([])
f = MyWindow()
app.exec()

#4) GUI mit Button beenden.. sobald button gedrückt wird, wird er inaktiv und nach 10sec schliest programm

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("blablabla")

        layout= QVBoxLayout()

        self.button = QPushButton("Beenden")

        layout.addWidget(self.button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
        self.raise_()
    
    def createConnects(self):
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.button.setDisabled(True)
        self.id= self.startTimer(10000)

    def timerEvent(self,event):
        self.close()

app = QApplication([])
f = MyWindow()
app.exec()

#5) Programm, was zufällige Linien zeichnet (1000 Linien, KO zufällig(breite-1, höhe-1), dicke zufällig 1-10, farbe zufällig)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import random

class GraphicsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.breiteF= 640
        self.hoeheF = 480

        self.createLayout()

    def createLayout(self):
        self.setWindowTitle("Zufallslinien")

        self.setGeometry(200,200, self.breiteF, self.hoeheF)
        self.show()
        self.raise_()

    def mousePressEvent(self,event):
        self.repaint()

    def paintEvent(self,event):

        self.breiteF= self.width()
        self.hoeheF = self.height()

        qp = QPainter()
        qp.begin(self)

        for i in range(0,1000,1):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)

            breite = random.randint(1,10)

            pinsel = QPen(QColor(r,g,b), breite)
            qp.setPen(pinsel)

            x1 = random.randint(0,self.breiteF-1)
            y1 = random.randint(0,self.hoeheF-1)

            x2 = random.randint(0,self.breiteF-1)
            y2 = random.randint(0,self.hoeheF-1)

            qp.drawLine(QPoint(x1,y1), QPoint(x2,y2))

        qp.end()

app= QApplication([])
f = GraphicsWindow()
app.exec()