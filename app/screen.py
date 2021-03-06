from PyQt5 import QtWidgets
import sys

def window(control,now,gold_value,dolar_value,euro_value,sterlin_value):
    app = QtWidgets.QApplication(sys.argv)

    myWindow = QtWidgets.QWidget()
    myWindow.setWindowTitle("to TRY:")

    buton = QtWidgets.QPushButton(myWindow)
    buton.setText("Calculate")

    buton2 = QtWidgets.QPushButton(myWindow)
    buton2.setText("Close")

    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()

    label = QtWidgets.QLabel(myWindow)
    label.setText("to TRY converter")
    label.move(160,50)

    if(control):
        #labels
        label2=QtWidgets.QLabel(myWindow)
        label3=QtWidgets.QLabel(myWindow)

        #Radio Buttons
        goldBtn = QtWidgets.QRadioButton(myWindow)
        dolarBtn = QtWidgets.QRadioButton(myWindow)
        euroBtn = QtWidgets.QRadioButton(myWindow)
        sterBtn = QtWidgets.QRadioButton(myWindow)
        
        #Set Text
        label2.setText(f"\n{now.day}/{now.month}/{now.year}\t{now.hour} : {now.minute} : {now.second}\n")
        goldBtn.setText(f"\tGOLD : {gold_value}\t")       
        dolarBtn.setText(f"\tDOLAR : {dolar_value}\t")     
        euroBtn.setText(f"\tEURO : {euro_value}\t")
        sterBtn.setText(f"\tSTERLIN : {sterlin_value}\t")
        
        label2.move(80,120)
    else:
        label2 = QtWidgets.QLabel(myWindow)
        label2.setText("NO CONNECTION!")
        label2.move(200,150)

    amount = QtWidgets.QLabel(myWindow)
    amount.setText("Amount :")

    textArea = QtWidgets.QLineEdit()

    v_box.addStretch()
    v_box.addWidget(label)
    v_box.addWidget(label2)
    try:
        v_box.addWidget(goldBtn)
        v_box.addWidget(dolarBtn)
        v_box.addWidget(euroBtn)
        v_box.addWidget(sterBtn)
        v_box.addWidget(label3)
    except:
        pass

    v_box.addWidget(amount)
    v_box.addWidget(textArea)
    v_box.addWidget(buton)
    v_box.addWidget(buton2)
    v_box.addStretch()

    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()

    #functions
    etp = QtWidgets.QLabel(myWindow)
    def Calculate(gold,dolar,euro,ster):
        try:
            local_amount = float(textArea.text())
            if dolar:
                etp.setText("{} TL".format(local_amount*float(dolar_value.replace(",",".")))) 
                v_box.addWidget(etp)
            elif gold:
                etp.setText("{} TL".format(local_amount*float(gold_value.replace(",","."))))
                v_box.addWidget(etp)

            elif euro:
                etp.setText("{} TL".format(local_amount*float(euro_value.replace(",","."))))
                v_box.addWidget(etp)

            elif ster:
                etp.setText("{} TL".format(local_amount*float(sterlin_value.replace(",","."))))
                v_box.addWidget(etp)

        except:
            etp.setText("Something Went Wrong")
            v_box.addWidget(etp)

    def Close():
        QtWidgets.qApp.quit()

    
    buton.clicked.connect(lambda : Calculate(goldBtn.isChecked(),dolarBtn.isChecked,euroBtn.isChecked(),sterBtn.isChecked()))
    buton2.clicked.connect(Close)
    myWindow.setLayout(v_box)
    myWindow.setLayout(h_box)
    myWindow.setGeometry(430,150,320,250)
    myWindow.show()
    sys.exit(app.exec_())