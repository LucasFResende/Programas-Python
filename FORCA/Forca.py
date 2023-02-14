import sys
from Forca_dsn import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Forca(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        img6 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_6.jpg'
        self.img6 = QPixmap(img6)
        self.forca.setPixmap(self.img6)
        self.verifica()
        self.letras_certas = []
        self.letras_digitadas = ""
        self.palavra_temporaria = ""
        self.vidas = 6
        img5 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_5.jpg'
        self.img5 = QPixmap(img5)
        img4 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_4.jpg'
        self.img4 = QPixmap(img4)
        img3 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_3.jpg'
        self.img3 = QPixmap(img3)
        img2 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_2.jpg'
        self.img2 = QPixmap(img2)
        img1 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_1.jpg'
        self.img1 = QPixmap(img1)
        img0 = r'C:\Users\lucas\OneDrive\PROGRAMAS\Programas Python\FORCA\img\forca_vida_0.jpg'
        self.img0 = QPixmap(img0)
        if '-' in self.palavra_secreta:
            l = self.palavra_secreta.index('-')
            self.palavra_sec.setText(
                '_ '*l + '- ' + '_ '*(len(self.palavra_secreta)-l))
            self.letras_certas.append('-')
        else:
            self.palavra_sec.setText('_ '*len(self.palavra_secreta))
        self.btnA.clicked.connect(self.btn_A)
        self.btnB.clicked.connect(self.btn_B)
        self.btnC.clicked.connect(self.btn_C)
        self.btnD.clicked.connect(self.btn_D)
        self.btnE.clicked.connect(self.btn_E)
        self.btnF.clicked.connect(self.btn_F)
        self.btnG.clicked.connect(self.btn_G)
        self.btnH.clicked.connect(self.btn_H)
        self.btnI.clicked.connect(self.btn_I)
        self.btnJ.clicked.connect(self.btn_J)
        self.btnK.clicked.connect(self.btn_K)
        self.btnL.clicked.connect(self.btn_L)
        self.btnM.clicked.connect(self.btn_M)
        self.btnN.clicked.connect(self.btn_N)
        self.btnO.clicked.connect(self.btn_O)
        self.btnP.clicked.connect(self.btn_P)
        self.btnQ.clicked.connect(self.btn_Q)
        self.btnR.clicked.connect(self.btn_R)
        self.btnS.clicked.connect(self.btn_S)
        self.btnT.clicked.connect(self.btn_T)
        self.btnU.clicked.connect(self.btn_U)
        self.btnV.clicked.connect(self.btn_V)
        self.btnW.clicked.connect(self.btn_W)
        self.btnX.clicked.connect(self.btn_X)
        self.btnY.clicked.connect(self.btn_Y)
        self.btnZ.clicked.connect(self.btn_Z)
        self.btnCd.clicked.connect(self.btn_Cd)

    def verifica(self):
        numeros = list(str(x) for x in range(0, 10))
        self.palavra_secreta = QtWidgets.QInputDialog.getText(
            self, 'Forca', 'Dige a palavra secreta:')
        self.palavra_secreta = self.palavra_secreta[0]
        for c in numeros:
            while c in self.palavra_secreta:
                self.palavra_secreta = QtWidgets.QInputDialog.getText(
                    self, 'Forca', 'Dige a palavra válida:')
                self.palavra_secreta = self.palavra_secreta[0]

        self.palavra_secreta = self.palavra_secreta.upper()
        self.tam_palavra = len(self.palavra_secreta)

    def btn_A(self):
        self.palavra_temporaria = ""
        if 'A' in self.palavra_secreta or 'Á' in self.palavra_secreta or 'Â' in self.palavra_secreta or 'À' in self.palavra_secreta or 'Ã' in self.palavra_secreta:
            self.letras_certas.append('A')
            self.letras_certas.append('Á')
            self.letras_certas.append('Â')
            self.letras_certas.append('À')
            self.letras_certas.append('Ã')
            self.letras_digitadas += 'A - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnA.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'A - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnA.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'
            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_B(self):
        self.palavra_temporaria = ""
        if 'B' in self.palavra_secreta:
            self.letras_certas.append('B')
            self.letras_digitadas += 'B - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnB.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'B - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnB.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)
        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_C(self):
        self.palavra_temporaria = ""
        if 'C' in self.palavra_secreta:
            self.letras_certas.append('C')
            self.letras_digitadas += 'C - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnC.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'C - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnC.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_D(self):
        self.palavra_temporaria = ""
        if 'D' in self.palavra_secreta:
            self.letras_certas.append('D')
            self.letras_digitadas += 'D - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnD.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'D - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnD.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_E(self):
        self.palavra_temporaria = ""
        if 'E' in self.palavra_secreta or 'É' in self.palavra_secreta or 'Ê' in self.palavra_secreta or 'È' in self.palavra_secreta:
            self.letras_certas.append('E')
            self.letras_certas.append('È')
            self.letras_certas.append('É')
            self.letras_certas.append('Ê')
            self.letras_digitadas += 'E - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnE.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'E - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnE.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_F(self):
        self.palavra_temporaria = ""
        if 'F' in self.palavra_secreta:
            self.letras_certas.append('F')
            self.letras_digitadas += 'F - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnF.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'F - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnF.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_G(self):
        self.palavra_temporaria = ""
        if 'G' in self.palavra_secreta:
            self.letras_certas.append('G')
            self.letras_digitadas += 'G - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnG.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'G - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnG.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_H(self):
        self.palavra_temporaria = ""
        if 'H' in self.palavra_secreta:
            self.letras_certas.append('H')
            self.letras_digitadas += 'H - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnH.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'H - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnH.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_I(self):
        self.palavra_temporaria = ""
        if 'I' in self.palavra_secreta or 'Í' in self.palavra_secreta or 'Î' in self.palavra_secreta or 'Ì' in self.palavra_secreta:
            self.letras_certas.append('I')
            self.letras_certas.append('Ì')
            self.letras_certas.append('Í')
            self.letras_certas.append('Î')
            self.letras_digitadas += 'I - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnI.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'I - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnI.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_J(self):
        self.palavra_temporaria = ""
        if 'J' in self.palavra_secreta:
            self.letras_certas.append('J')
            self.letras_digitadas += 'J - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnJ.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'J - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnJ.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_K(self):
        self.palavra_temporaria = ""
        if 'K' in self.palavra_secreta:
            self.letras_certas.append('K')
            self.letras_digitadas += 'K - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnK.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'K - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnK.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_L(self):
        self.palavra_temporaria = ""
        if 'L' in self.palavra_secreta:
            self.letras_certas.append('L')
            self.letras_digitadas += 'L - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnL.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'L - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnL.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_M(self):
        self.palavra_temporaria = ""
        if 'M' in self.palavra_secreta:
            self.letras_certas.append('M')
            self.letras_digitadas += 'M - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnM.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'M - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnM.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_N(self):
        self.palavra_temporaria = ""
        if 'N' in self.palavra_secreta:
            self.letras_certas.append('N')
            self.letras_digitadas += 'N - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnN.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'N - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnN.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_O(self):
        self.palavra_temporaria = ""
        if 'O' in self.palavra_secreta or 'Ó' in self.palavra_secreta or 'Ô' in self.palavra_secreta or 'Ò' in self.palavra_secreta or 'Õ' in self.palavra_secreta:
            self.letras_certas.append('O')
            self.letras_certas.append('Ó')
            self.letras_certas.append('Ô')
            self.letras_certas.append('Ò')
            self.letras_certas.append('Õ')
            self.letras_digitadas += 'O - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnO.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'O - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnO.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_P(self):
        self.palavra_temporaria = ""
        if 'P' in self.palavra_secreta:
            self.letras_certas.append('P')
            self.letras_digitadas += 'P - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnP.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'P - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnP.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_Q(self):
        self.palavra_temporaria = ""
        if 'Q' in self.palavra_secreta:
            self.letras_certas.append('Q')
            self.letras_digitadas += 'Q - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnQ.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'Q - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnQ.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_R(self):
        self.palavra_temporaria = ""
        if 'R' in self.palavra_secreta:
            self.letras_certas.append('R')
            self.letras_digitadas += 'R - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnR.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'R - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnR.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_S(self):
        self.palavra_temporaria = ""
        if 'S' in self.palavra_secreta:
            self.letras_certas.append('S')
            self.letras_digitadas += 'S - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnS.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'S - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnS.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_T(self):
        self.palavra_temporaria = ""
        if 'T' in self.palavra_secreta:
            self.letras_certas.append('T')
            self.letras_digitadas += 'T - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnT.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'T - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnT.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_U(self):
        self.palavra_temporaria = ""
        if 'U' in self.palavra_secreta or 'Ú' in self.palavra_secreta or 'Ù' in self.palavra_secreta or 'Û' in self.palavra_secreta:
            self.letras_certas.append('U')
            self.letras_certas.append('Ú')
            self.letras_certas.append('Ù')
            self.letras_certas.append('Û')
            self.letras_digitadas += 'U - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnU.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'U - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnU.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_V(self):
        self.palavra_temporaria = ""
        if 'V' in self.palavra_secreta:
            self.letras_certas.append('V')
            self.letras_digitadas += 'V - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnV.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'V - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnV.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_W(self):
        self.palavra_temporaria = ""
        if 'W' in self.palavra_secreta:
            self.letras_certas.append('W')
            self.letras_digitadas += 'W - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnW.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'W - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnW.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_X(self):
        self.palavra_temporaria = ""
        if 'X' in self.palavra_secreta:
            self.letras_certas.append('X')
            self.letras_digitadas += 'X - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnX.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'X - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnX.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_Y(self):
        self.palavra_temporaria = ""
        if 'Y' in self.palavra_secreta:
            self.letras_certas.append('Y')
            self.letras_digitadas += 'Y - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnY.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'Y - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnY.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_Z(self):
        self.palavra_temporaria = ""
        if 'Z' in self.palavra_secreta:
            self.letras_certas.append('Z')
            self.letras_digitadas += 'Z - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnZ.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'Z - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnZ.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'

            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')

    def btn_Cd(self):
        self.palavra_temporaria = ""
        if 'Ç' in self.palavra_secreta:
            self.letras_certas.append('Ç')
            self.letras_digitadas += 'Ç - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnCd.setDisabled(True)
        else:
            self.vidas -= 1
            self.letras_digitadas += 'Ç - '
            if len(self.letras_digitadas) <= 72:
                self.letras_dig.setText(
                    self.letras_digitadas[0:len(self.letras_digitadas)-2])
            else:
                self.letras_dig_2.setText(
                    self.letras_digitadas[71:len(self.letras_digitadas)-2])
            self.btnCd.setDisabled(True)

        if self.vidas == 5:
            self.forca.setPixmap(self.img5)
        elif self.vidas == 4:
            self.forca.setPixmap(self.img4)
        elif self.vidas == 3:
            self.forca.setPixmap(self.img3)
        elif self.vidas == 2:
            self.forca.setPixmap(self.img2)
        elif self.vidas == 1:
            self.forca.setPixmap(self.img1)
        elif self.vidas == 0:
            self.forca.setPixmap(self.img0)
            self.palavra_sec.setText(
                f'VOCÊ PERDEU! A PALAVRA ERA: {self.palavra_secreta}')

        if self.vidas != 0:
            for c in self.palavra_secreta:
                if c in self.letras_certas:
                    self.palavra_temporaria += f'{c}'
                else:
                    self.palavra_temporaria += f'{"_ "}'
            self.palavra_sec.setText(self.palavra_temporaria)

        if self.palavra_temporaria == self.palavra_secreta:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.palavra_sec.setFont(font)
            self.palavra_sec.setText(
                f'PARABÉNS! VOCÊ ACERTOU A PALAVRA! A PALAVRA ERA: {self.palavra_secreta}')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    forca = Forca()
    forca.show()
    qt.exec()
