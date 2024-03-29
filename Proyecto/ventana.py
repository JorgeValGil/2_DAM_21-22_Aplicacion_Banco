# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("banco.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_cuentas = QtWidgets.QWidget()
        self.tab_cuentas.setObjectName("tab_cuentas")
        self.lineEdit_ncuenta = QtWidgets.QLineEdit(self.tab_cuentas)
        self.lineEdit_ncuenta.setGeometry(QtCore.QRect(130, 30, 250, 20))
        self.lineEdit_ncuenta.setObjectName("lineEdit_ncuenta")
        self.Recargar_Cuenta = QtWidgets.QPushButton(self.tab_cuentas)
        self.Recargar_Cuenta.setGeometry(QtCore.QRect(750, 0, 32, 32))
        self.Recargar_Cuenta.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/reload/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Recargar_Cuenta.setIcon(icon1)
        self.Recargar_Cuenta.setObjectName("Recargar_Cuenta")
        self.Buscar_Cuenta = QtWidgets.QPushButton(self.tab_cuentas)
        self.Buscar_Cuenta.setGeometry(QtCore.QRect(445, 20, 32, 32))
        self.Buscar_Cuenta.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/lupa/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Buscar_Cuenta.setIcon(icon2)
        self.Buscar_Cuenta.setObjectName("Buscar_Cuenta")
        self.label_ncuenta = QtWidgets.QLabel(self.tab_cuentas)
        self.label_ncuenta.setGeometry(QtCore.QRect(50, 35, 72, 13))
        self.label_ncuenta.setObjectName("label_ncuenta")
        self.tableCuentas = QtWidgets.QTableWidget(self.tab_cuentas)
        self.tableCuentas.setGeometry(QtCore.QRect(40, 120, 701, 311))
        self.tableCuentas.setColumnCount(3)
        self.tableCuentas.setObjectName("tableCuentas")
        self.tableCuentas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCuentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCuentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCuentas.setHorizontalHeaderItem(2, item)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_cuentas)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 440, 761, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_botones_inferiores_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_botones_inferiores_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_botones_inferiores_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_botones_inferiores_2.setSpacing(10)
        self.horizontalLayout_botones_inferiores_2.setObjectName("horizontalLayout_botones_inferiores_2")
        self.Alta_Cuenta = QtWidgets.QPushButton(self.layoutWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/alta_cuenta/alta_cuenta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alta_Cuenta.setIcon(icon3)
        self.Alta_Cuenta.setObjectName("Alta_Cuenta")
        self.horizontalLayout_botones_inferiores_2.addWidget(self.Alta_Cuenta)
        self.Modificar_Cuenta = QtWidgets.QPushButton(self.layoutWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/modificar/modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Modificar_Cuenta.setIcon(icon4)
        self.Modificar_Cuenta.setObjectName("Modificar_Cuenta")
        self.horizontalLayout_botones_inferiores_2.addWidget(self.Modificar_Cuenta)
        self.Eliminar_Cuenta = QtWidgets.QPushButton(self.layoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/eliminar/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Eliminar_Cuenta.setIcon(icon5)
        self.Eliminar_Cuenta.setObjectName("Eliminar_Cuenta")
        self.horizontalLayout_botones_inferiores_2.addWidget(self.Eliminar_Cuenta)
        self.Limpiar_Cuenta = QtWidgets.QPushButton(self.layoutWidget_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/limpiar/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Limpiar_Cuenta.setIcon(icon6)
        self.Limpiar_Cuenta.setObjectName("Limpiar_Cuenta")
        self.horizontalLayout_botones_inferiores_2.addWidget(self.Limpiar_Cuenta)
        self.pushButton_Salir_Cuenta = QtWidgets.QPushButton(self.layoutWidget_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/salir/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Salir_Cuenta.setIcon(icon7)
        self.pushButton_Salir_Cuenta.setObjectName("pushButton_Salir_Cuenta")
        self.horizontalLayout_botones_inferiores_2.addWidget(self.pushButton_Salir_Cuenta)
        self.label_cuenta_cliente = QtWidgets.QLabel(self.tab_cuentas)
        self.label_cuenta_cliente.setGeometry(QtCore.QRect(50, 95, 91, 16))
        self.label_cuenta_cliente.setObjectName("label_cuenta_cliente")
        self.cmbClienteTitular = QtWidgets.QComboBox(self.tab_cuentas)
        self.cmbClienteTitular.setGeometry(QtCore.QRect(130, 90, 113, 22))
        self.cmbClienteTitular.setObjectName("cmbClienteTitular")
        self.label_status_cuenta = QtWidgets.QLabel(self.tab_cuentas)
        self.label_status_cuenta.setGeometry(QtCore.QRect(10, 500, 761, 20))
        self.label_status_cuenta.setText("")
        self.label_status_cuenta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_cuenta.setObjectName("label_status_cuenta")
        self.label_cuenta_saldo = QtWidgets.QLabel(self.tab_cuentas)
        self.label_cuenta_saldo.setGeometry(QtCore.QRect(507, 95, 47, 13))
        self.label_cuenta_saldo.setObjectName("label_cuenta_saldo")
        self.lineEdit_cuenta_saldo = QtWidgets.QLineEdit(self.tab_cuentas)
        self.lineEdit_cuenta_saldo.setGeometry(QtCore.QRect(557, 90, 125, 20))
        self.lineEdit_cuenta_saldo.setObjectName("lineEdit_cuenta_saldo")
        self.label_cuenta_valid = QtWidgets.QLabel(self.tab_cuentas)
        self.label_cuenta_valid.setGeometry(QtCore.QRect(390, 20, 47, 30))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(14)
        self.label_cuenta_valid.setFont(font)
        self.label_cuenta_valid.setText("")
        self.label_cuenta_valid.setObjectName("label_cuenta_valid")
        self.tabWidget.addTab(self.tab_cuentas, "")
        self.tab_Clientes = QtWidgets.QWidget()
        self.tab_Clientes.setObjectName("tab_Clientes")
        self.layoutWidget = QtWidgets.QWidget(self.tab_Clientes)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 761, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_botones_inferiores = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_botones_inferiores.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_botones_inferiores.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_botones_inferiores.setSpacing(10)
        self.horizontalLayout_botones_inferiores.setObjectName("horizontalLayout_botones_inferiores")
        self.Alta_Cliente = QtWidgets.QPushButton(self.layoutWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/alta/alta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alta_Cliente.setIcon(icon8)
        self.Alta_Cliente.setObjectName("Alta_Cliente")
        self.horizontalLayout_botones_inferiores.addWidget(self.Alta_Cliente)
        self.Modificar_Cliente = QtWidgets.QPushButton(self.layoutWidget)
        self.Modificar_Cliente.setIcon(icon4)
        self.Modificar_Cliente.setObjectName("Modificar_Cliente")
        self.horizontalLayout_botones_inferiores.addWidget(self.Modificar_Cliente)
        self.Eliminar_Cliente = QtWidgets.QPushButton(self.layoutWidget)
        self.Eliminar_Cliente.setIcon(icon5)
        self.Eliminar_Cliente.setObjectName("Eliminar_Cliente")
        self.horizontalLayout_botones_inferiores.addWidget(self.Eliminar_Cliente)
        self.Limpiar_Cliente = QtWidgets.QPushButton(self.layoutWidget)
        self.Limpiar_Cliente.setIcon(icon6)
        self.Limpiar_Cliente.setObjectName("Limpiar_Cliente")
        self.horizontalLayout_botones_inferiores.addWidget(self.Limpiar_Cliente)
        self.pushButton_Salir_Cliente = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Salir_Cliente.setIcon(icon7)
        self.pushButton_Salir_Cliente.setObjectName("pushButton_Salir_Cliente")
        self.horizontalLayout_botones_inferiores.addWidget(self.pushButton_Salir_Cliente)
        self.Recargar = QtWidgets.QPushButton(self.tab_Clientes)
        self.Recargar.setGeometry(QtCore.QRect(750, 0, 32, 32))
        self.Recargar.setText("")
        self.Recargar.setIcon(icon1)
        self.Recargar.setObjectName("Recargar")
        self.label_dni = QtWidgets.QLabel(self.tab_Clientes)
        self.label_dni.setGeometry(QtCore.QRect(50, 35, 47, 13))
        self.label_dni.setObjectName("label_dni")
        self.lineEdit_dni = QtWidgets.QLineEdit(self.tab_Clientes)
        self.lineEdit_dni.setGeometry(QtCore.QRect(100, 30, 115, 20))
        self.lineEdit_dni.setObjectName("lineEdit_dni")
        self.Buscar = QtWidgets.QPushButton(self.tab_Clientes)
        self.Buscar.setGeometry(QtCore.QRect(275, 20, 32, 32))
        self.Buscar.setText("")
        self.Buscar.setIcon(icon2)
        self.Buscar.setObjectName("Buscar")
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.tab_Clientes)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(100, 80, 115, 20))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.label_apellido = QtWidgets.QLabel(self.tab_Clientes)
        self.label_apellido.setGeometry(QtCore.QRect(50, 85, 47, 13))
        self.label_apellido.setObjectName("label_apellido")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.tab_Clientes)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(480, 80, 115, 20))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.label_nombre = QtWidgets.QLabel(self.tab_Clientes)
        self.label_nombre.setGeometry(QtCore.QRect(420, 85, 47, 13))
        self.label_nombre.setObjectName("label_nombre")
        self.tableClientes = QtWidgets.QTableWidget(self.tab_Clientes)
        self.tableClientes.setGeometry(QtCore.QRect(40, 120, 701, 311))
        self.tableClientes.setColumnCount(3)
        self.tableClientes.setObjectName("tableClientes")
        self.tableClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(2, item)
        self.label_status_cliente = QtWidgets.QLabel(self.tab_Clientes)
        self.label_status_cliente.setGeometry(QtCore.QRect(10, 500, 761, 20))
        self.label_status_cliente.setText("")
        self.label_status_cliente.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_cliente.setObjectName("label_status_cliente")
        self.label_dni_valid = QtWidgets.QLabel(self.tab_Clientes)
        self.label_dni_valid.setGeometry(QtCore.QRect(220, 20, 47, 30))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(14)
        self.label_dni_valid.setFont(font)
        self.label_dni_valid.setText("")
        self.label_dni_valid.setObjectName("label_dni_valid")
        self.tabWidget.addTab(self.tab_Clientes, "")
        self.tab_movimientos = QtWidgets.QWidget()
        self.tab_movimientos.setObjectName("tab_movimientos")
        self.label_movimiento_cuenta = QtWidgets.QLabel(self.tab_movimientos)
        self.label_movimiento_cuenta.setGeometry(QtCore.QRect(50, 35, 75, 16))
        self.label_movimiento_cuenta.setObjectName("label_movimiento_cuenta")
        self.cmbMovimiento_cuenta = QtWidgets.QComboBox(self.tab_movimientos)
        self.cmbMovimiento_cuenta.setGeometry(QtCore.QRect(130, 30, 231, 22))
        self.cmbMovimiento_cuenta.setObjectName("cmbMovimiento_cuenta")
        self.cmbMovimiento_tipo = QtWidgets.QComboBox(self.tab_movimientos)
        self.cmbMovimiento_tipo.setGeometry(QtCore.QRect(500, 30, 150, 22))
        self.cmbMovimiento_tipo.setObjectName("cmbMovimiento_tipo")
        self.label_movimiento_tipo = QtWidgets.QLabel(self.tab_movimientos)
        self.label_movimiento_tipo.setGeometry(QtCore.QRect(450, 35, 60, 16))
        self.label_movimiento_tipo.setObjectName("label_movimiento_tipo")
        self.label_movimiento_importe = QtWidgets.QLabel(self.tab_movimientos)
        self.label_movimiento_importe.setGeometry(QtCore.QRect(50, 85, 59, 16))
        self.label_movimiento_importe.setObjectName("label_movimiento_importe")
        self.label_status_movimiento = QtWidgets.QLabel(self.tab_movimientos)
        self.label_status_movimiento.setGeometry(QtCore.QRect(10, 500, 761, 20))
        self.label_status_movimiento.setText("")
        self.label_status_movimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_movimiento.setObjectName("label_status_movimiento")
        self.lineEdit_movimiento_importe = QtWidgets.QLineEdit(self.tab_movimientos)
        self.lineEdit_movimiento_importe.setGeometry(QtCore.QRect(130, 80, 120, 20))
        self.lineEdit_movimiento_importe.setObjectName("lineEdit_movimiento_importe")
        self.tableMovimientos = QtWidgets.QTableWidget(self.tab_movimientos)
        self.tableMovimientos.setGeometry(QtCore.QRect(40, 120, 701, 311))
        self.tableMovimientos.setObjectName("tableMovimientos")
        self.tableMovimientos.setColumnCount(4)
        self.tableMovimientos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableMovimientos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMovimientos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMovimientos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMovimientos.setHorizontalHeaderItem(3, item)
        self.Recargar_movimiento = QtWidgets.QPushButton(self.tab_movimientos)
        self.Recargar_movimiento.setGeometry(QtCore.QRect(750, 0, 32, 32))
        self.Recargar_movimiento.setText("")
        self.Recargar_movimiento.setIcon(icon1)
        self.Recargar_movimiento.setObjectName("Recargar_movimiento")
        self.Alta_Movimiento = QtWidgets.QPushButton(self.tab_movimientos)
        self.Alta_Movimiento.setGeometry(QtCore.QRect(100, 452, 144, 24))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/alta_movimiento/alta_movimiento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alta_Movimiento.setIcon(icon9)
        self.Alta_Movimiento.setObjectName("Alta_Movimiento")
        self.pushButton_Salir_Movimiento = QtWidgets.QPushButton(self.tab_movimientos)
        self.pushButton_Salir_Movimiento.setGeometry(QtCore.QRect(524, 450, 144, 24))
        self.pushButton_Salir_Movimiento.setIcon(icon7)
        self.pushButton_Salir_Movimiento.setObjectName("pushButton_Salir_Movimiento")
        self.Limpiar_Movimiento = QtWidgets.QPushButton(self.tab_movimientos)
        self.Limpiar_Movimiento.setGeometry(QtCore.QRect(309, 450, 144, 24))
        self.Limpiar_Movimiento.setIcon(icon6)
        self.Limpiar_Movimiento.setObjectName("Limpiar_Movimiento")
        self.tabWidget.addTab(self.tab_movimientos, "")
        self.tab_Datos = QtWidgets.QWidget()
        self.tab_Datos.setObjectName("tab_Datos")
        self.tableDatos = QtWidgets.QTableWidget(self.tab_Datos)
        self.tableDatos.setGeometry(QtCore.QRect(40, 80, 701, 341))
        self.tableDatos.setObjectName("tableDatos")
        self.tableDatos.setColumnCount(3)
        self.tableDatos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDatos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDatos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDatos.setHorizontalHeaderItem(2, item)
        self.label_status_datos = QtWidgets.QLabel(self.tab_Datos)
        self.label_status_datos.setGeometry(QtCore.QRect(10, 500, 761, 20))
        self.label_status_datos.setText("")
        self.label_status_datos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_datos.setObjectName("label_status_datos")
        self.label_datos = QtWidgets.QLabel(self.tab_Datos)
        self.label_datos.setGeometry(QtCore.QRect(50, 35, 165, 16))
        self.label_datos.setObjectName("label_datos")
        self.comboBox_datos_cuenta = QtWidgets.QComboBox(self.tab_Datos)
        self.comboBox_datos_cuenta.setGeometry(QtCore.QRect(220, 30, 360, 20))
        self.comboBox_datos_cuenta.setObjectName("comboBox_datos_cuenta")
        self.Limpiar_Dato = QtWidgets.QPushButton(self.tab_Datos)
        self.Limpiar_Dato.setGeometry(QtCore.QRect(230, 452, 144, 24))
        self.Limpiar_Dato.setIcon(icon6)
        self.Limpiar_Dato.setObjectName("Limpiar_Dato")
        self.pushButton_Salir_Dato = QtWidgets.QPushButton(self.tab_Datos)
        self.pushButton_Salir_Dato.setGeometry(QtCore.QRect(450, 452, 144, 24))
        self.pushButton_Salir_Dato.setIcon(icon7)
        self.pushButton_Salir_Dato.setObjectName("pushButton_Salir_Dato")
        self.Buscar_Dato = QtWidgets.QPushButton(self.tab_Datos)
        self.Buscar_Dato.setGeometry(QtCore.QRect(610, 20, 32, 32))
        self.Buscar_Dato.setText("")
        self.Buscar_Dato.setIcon(icon2)
        self.Buscar_Dato.setObjectName("Buscar_Dato")
        self.tabWidget.addTab(self.tab_Datos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actioninformepdf = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/informepdf/informe-pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioninformepdf.setIcon(icon10)
        self.actioninformepdf.setObjectName("actioninformepdf")
        self.toolBar.addAction(self.actioninformepdf)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco DI"))
        self.lineEdit_ncuenta.setToolTip(_translate("MainWindow", "Formato: ES3200789398504222542001"))
        self.Recargar_Cuenta.setToolTip(_translate("MainWindow", "Recargar Tabla"))
        self.Buscar_Cuenta.setToolTip(_translate("MainWindow", "Buscar Cuenta"))
        self.label_ncuenta.setText(_translate("MainWindow", "Nº de Cuenta:"))
        self.tableCuentas.setToolTip(_translate("MainWindow", "Tabla Cuenta"))
        item = self.tableCuentas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de Cuenta"))
        item = self.tableCuentas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cliente Titular"))
        item = self.tableCuentas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Saldo"))
        self.Alta_Cuenta.setToolTip(_translate("MainWindow", "Dar de Alta una Cuenta"))
        self.Alta_Cuenta.setText(_translate("MainWindow", "Alta"))
        self.Modificar_Cuenta.setToolTip(_translate("MainWindow", "Modificar Cuenta"))
        self.Modificar_Cuenta.setText(_translate("MainWindow", "Modificar"))
        self.Eliminar_Cuenta.setToolTip(_translate("MainWindow", "Eliminar Cuenta"))
        self.Eliminar_Cuenta.setText(_translate("MainWindow", "Eliminar"))
        self.Limpiar_Cuenta.setToolTip(_translate("MainWindow", "Limpiar Campos Cuentas"))
        self.Limpiar_Cuenta.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton_Salir_Cuenta.setToolTip(_translate("MainWindow", "Salir"))
        self.pushButton_Salir_Cuenta.setText(_translate("MainWindow", "Salir"))
        self.label_cuenta_cliente.setText(_translate("MainWindow", "Cliente Titular"))
        self.cmbClienteTitular.setToolTip(_translate("MainWindow", "Seleccionar Cliente"))
        self.label_cuenta_saldo.setText(_translate("MainWindow", "Saldo:"))
        self.lineEdit_cuenta_saldo.setToolTip(_translate("MainWindow", "Formato: 100"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cuentas), _translate("MainWindow", "Cuentas"))
        self.Alta_Cliente.setToolTip(_translate("MainWindow", "Dar de Alta un Cleinte"))
        self.Alta_Cliente.setText(_translate("MainWindow", "Alta"))
        self.Modificar_Cliente.setToolTip(_translate("MainWindow", "Modificar Cliente"))
        self.Modificar_Cliente.setText(_translate("MainWindow", "Modificar"))
        self.Eliminar_Cliente.setToolTip(_translate("MainWindow", "Eliminar Cliente"))
        self.Eliminar_Cliente.setText(_translate("MainWindow", "Eliminar"))
        self.Limpiar_Cliente.setToolTip(_translate("MainWindow", "Limpiar Campos Clientes"))
        self.Limpiar_Cliente.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton_Salir_Cliente.setToolTip(_translate("MainWindow", "Salir"))
        self.pushButton_Salir_Cliente.setText(_translate("MainWindow", "Salir"))
        self.Recargar.setToolTip(_translate("MainWindow", "Recargar Tabla"))
        self.label_dni.setText(_translate("MainWindow", "DNI:"))
        self.lineEdit_dni.setToolTip(_translate("MainWindow", "Formato: 11111111H"))
        self.Buscar.setToolTip(_translate("MainWindow", "Buscar Cliente"))
        self.lineEdit_apellido.setToolTip(_translate("MainWindow", "Introducir Apellidos"))
        self.label_apellido.setText(_translate("MainWindow", "Apellidos:"))
        self.lineEdit_nombre.setToolTip(_translate("MainWindow", "Introducir Nombre"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre:"))
        self.tableClientes.setToolTip(_translate("MainWindow", "Tabla Clientes"))
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Clientes), _translate("MainWindow", "Clientes"))
        self.label_movimiento_cuenta.setText(_translate("MainWindow", "Nº de Cuenta:"))
        self.cmbMovimiento_cuenta.setToolTip(_translate("MainWindow", "Seleccionar Numero de Cuenta"))
        self.cmbMovimiento_tipo.setToolTip(_translate("MainWindow", "Seleccionar Tipo de Movimiento"))
        self.label_movimiento_tipo.setText(_translate("MainWindow", "Tipo:"))
        self.label_movimiento_importe.setText(_translate("MainWindow", "Importe:"))
        self.lineEdit_movimiento_importe.setToolTip(_translate("MainWindow", "Formato: 100"))
        self.tableMovimientos.setToolTip(_translate("MainWindow", "Tabla Movimientos"))
        item = self.tableMovimientos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableMovimientos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Número de Cuenta"))
        item = self.tableMovimientos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de Movimeinto"))
        item = self.tableMovimientos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Importe"))
        self.Recargar_movimiento.setToolTip(_translate("MainWindow", "Recargar Tabla"))
        self.Alta_Movimiento.setToolTip(_translate("MainWindow", "Dar de Alta un Movimiento"))
        self.Alta_Movimiento.setText(_translate("MainWindow", "Alta"))
        self.pushButton_Salir_Movimiento.setToolTip(_translate("MainWindow", "Salir"))
        self.pushButton_Salir_Movimiento.setText(_translate("MainWindow", "Salir"))
        self.Limpiar_Movimiento.setToolTip(_translate("MainWindow", "Limpiar Campos Movimientos"))
        self.Limpiar_Movimiento.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_movimientos), _translate("MainWindow", "Movimientos"))
        self.tableDatos.setToolTip(_translate("MainWindow", "Tabla Movimientos Cuenta"))
        item = self.tableDatos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de Cuenta"))
        item = self.tableDatos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo de Movimiento"))
        item = self.tableDatos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Importe"))
        self.label_datos.setText(_translate("MainWindow", "Selecciona una cuenta bancaria:"))
        self.comboBox_datos_cuenta.setToolTip(_translate("MainWindow", "Seleccionar Cuenta Bancaria"))
        self.Limpiar_Dato.setToolTip(_translate("MainWindow", "Limpiar Campos Datos"))
        self.Limpiar_Dato.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton_Salir_Dato.setToolTip(_translate("MainWindow", "Salir"))
        self.pushButton_Salir_Dato.setText(_translate("MainWindow", "Salir"))
        self.Buscar_Dato.setToolTip(_translate("MainWindow", "Buscar Movimientos Cuenta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Datos), _translate("MainWindow", "Datos"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actioninformepdf.setText(_translate("MainWindow", "informepdf"))
        self.actioninformepdf.setToolTip(_translate("MainWindow", "Generar Informe PDF"))
import alta_cuenta_rc
import alta_movimiento_rc
import alta_rc
import eliminar_rc
import informepdf_rc
import limpiar_rc
import lupa_rc
import modificar_rc
import reload_rc
import salir_rc
