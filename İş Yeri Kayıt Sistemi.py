import sys,os
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout,QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
from PyQt5 import QtWidgets,QtGui

class KayıtSistemi(QWidget):

    def __init__(self):
        super(KayıtSistemi, self).__init__()


        self.init_ui()

    def init_ui(self):
        
        layout1 = QtWidgets.QVBoxLayout()
        layout2= QtWidgets.QVBoxLayout()
        layout3=QtWidgets.QHBoxLayout()

        layout3.addLayout(layout1)
        layout3.addLayout(layout2)
        self.setLayout(layout3)
  
        self.setFixedSize(450,300) 
        self.setWindowTitle('Kayıt Sistemi')

        self.show()

        self.yazi_alani =QtWidgets.QTextEdit()
        self.Sirket_Adı =  QtWidgets.QTextEdit("Şirket Adı")
        self.Sirket_Temsilcisi = QtWidgets.QTextEdit("Şirket Temsilcisi")
        self.Adres=QtWidgets.QTextEdit("Adres")
        self.Vergi_No=QtWidgets.QTextEdit("VERGİ No")
        self.Telefon_No=QtWidgets.QTextEdit("Tel No")   
        self.Cep_Tel=QtWidgets.QTextEdit("Cep Tel")   
        self.Vergi_D=QtWidgets.QTextEdit("Vergi D")
        self.durumbildirici=QtWidgets.QLabel()
        self.yazi_alani.setText("Notlarınızı Buraya Yazınız..")  
        
        self.Kayıt = QtWidgets.QPushButton("Kaydet")   
        self.Temizle=QtWidgets.QPushButton("Temizle")    
 
        layout1.addWidget(self.durumbildirici)
        layout1.addWidget(self.Sirket_Adı)
        layout1.addWidget(self.Sirket_Temsilcisi)
        layout2.addWidget(self.Adres)
        layout1.addWidget(self.Vergi_D)
        layout1.addWidget(self.Vergi_No)
        layout2.addWidget(self.Telefon_No)
        layout2.addWidget(self.Cep_Tel)
        layout2.addWidget(self.yazi_alani)
        layout2.addWidget(self.Kayıt)
        layout2.addWidget(self.Temizle)
    
        self.Kayıt.clicked.connect(self.yazici)       
        self.Temizle.clicked.connect(self.temizleyici)
    
    def temizleyici(Self):   #Ekranda yazılan tüm bilgilerin silinmesini sağlarız.
        Self.Sirket_Adı.setText("")
        Self.Sirket_Temsilcisi.setPlainText("")
        Self.Adres.setText("")
        Self.Vergi_D.setText("")
        Self.Vergi_No.setText("")
        Self.Telefon_No.setPlainText("")
        Self.Cep_Tel.setPlainText("")
        Self.yazi_alani.setPlainText("")
    
    def yazici(self):
        self.setStyleSheet("background-color :green")               #Ekranın rengini değiştiririz.
        self.durumbildirici.setText("Kayıt Başarılı")
        dosya_ismi = QFileDialog.getSaveFileName(self, "dosya kaydet", os.getenv("Desktop"))  # dosyayı kaydet modunda açarız

        with open(dosya_ismi[0], "a")as file:
            
            file.write("Sirket Adı: "+self.Sirket_Adı.toPlainText()+"\n")
            file.write("Sirket Temsilcisi:  "+self.Sirket_Temsilcisi.toPlainText()+"\n")
            file.write("Adres:  "+self.Adres.toPlainText()+"\n")
            file.write("Vergi Dairesi:  "+self.Vergi_D.toPlainText()+"\n")
            file.write("Vergi Numarası:  "+self.Vergi_No.toPlainText()+"\n")
            file.write("Telefon Numarası:  "+self.Telefon_No.toPlainText()+"\n")
            file.write("Cep Telefonu:  "+self.Cep_Tel.toPlainText()+"\n")
            file.write("Notlar: "+self.yazi_alani.toPlainText()+"\n")
            file.write("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        

            
app = QApplication(sys.argv)

Kayıt = KayıtSistemi()
sys.exit(app.exec_())