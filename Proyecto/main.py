import clients
import conexion
import cuentas
import datos
import events
import movimientos
import printer
import sys
import var
from ventana import *
from windowaviso import *


class Main(QtWidgets.QMainWindow):
    """Clase principal del programa"""

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        """Función que crear la conexión con la base de datos"""
        conexion.Conexion.db_connect(self, var.filebd)

        """Evento para validar DNI"""
        var.ui.lineEdit_dni.editingFinished.connect(clients.Clientes.validar_dni)

        """Evento para validar IBAN"""
        var.ui.lineEdit_ncuenta.editingFinished.connect(cuentas.Cuentas.validar_iban)

        """Función que carga los tipos de movimientos en una variable y en un ComboBox"""
        movimientos.Movimientos.cargar_tipo_movimiento(self)

        """Función que carga y muestra las Cuentas, los Clientes y en los Movimientos en las respectivas tablas"""
        conexion.Conexion.mostrar_en_tablas(self)

        """Función que carga las Cuentas y los Clientes en variables y en ComboBoxes"""
        conexion.Conexion.obtener_datos_en_var(self)

        """Eventos boton Crear Informe PDF"""
        var.ui.actioninformepdf.triggered.connect(printer.Printer.informe_pdf)

        """Eventos botones Limpiar"""
        var.ui.Limpiar_Cliente.clicked.connect(clients.Clientes.limpiar_cliente)
        var.ui.Limpiar_Cuenta.clicked.connect(cuentas.Cuentas.limpiar_cuenta)
        var.ui.Limpiar_Movimiento.clicked.connect(movimientos.Movimientos.limpiar_movimiento)
        var.ui.Limpiar_Dato.clicked.connect(datos.Datos.limpiar_dato)

        """Eventos botones Alta"""
        var.ui.Alta_Cuenta.clicked.connect(cuentas.Cuentas.alta_cuenta)
        var.ui.Alta_Cliente.clicked.connect(clients.Clientes.alta_cliente)
        var.ui.Alta_Movimiento.clicked.connect(movimientos.Movimientos.alta_movimiento)

        """Eventos botones Eliminar"""
        var.ui.Eliminar_Cliente.clicked.connect(clients.Clientes.baja_cliente)
        var.ui.Eliminar_Cuenta.clicked.connect(cuentas.Cuentas.baja_cuenta)

        """Eventos botones Modificar"""
        var.ui.Modificar_Cuenta.clicked.connect(cuentas.Cuentas.modif_cuenta)
        var.ui.Modificar_Cliente.clicked.connect(clients.Clientes.modif_cliente)

        """Eventos botones Buscar"""
        var.ui.Buscar.clicked.connect(clients.Clientes.buscar_cliente)
        var.ui.Buscar_Cuenta.clicked.connect(cuentas.Cuentas.buscar_cuenta)
        var.ui.Buscar_Dato.clicked.connect(datos.Datos.buscar_datos)

        """Eventos botones Recargar"""
        var.ui.Recargar_movimiento.clicked.connect(conexion.Conexion.mostrar_en_tablas)
        var.ui.Recargar_Cuenta.clicked.connect(conexion.Conexion.mostrar_en_tablas)
        var.ui.Recargar.clicked.connect(conexion.Conexion.mostrar_en_tablas)

        """Eventos botones Salir"""
        var.ui.pushButton_Salir_Cuenta.clicked.connect(events.Eventos.salir)
        var.ui.pushButton_Salir_Cliente.clicked.connect(events.Eventos.salir)
        var.ui.pushButton_Salir_Movimiento.clicked.connect(events.Eventos.salir)
        var.ui.pushButton_Salir_Dato.clicked.connect(events.Eventos.salir)

        """Bucles para que las columnas de las tablas ocupen el mismo ancho"""
        for i in range(var.ui.tableClientes.horizontalHeader().count()):
            var.ui.tableClientes.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        for i in range(var.ui.tableCuentas.horizontalHeader().count()):
            var.ui.tableCuentas.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        for i in range(var.ui.tableDatos.horizontalHeader().count()):
            var.ui.tableDatos.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        for i in range(var.ui.tableMovimientos.horizontalHeader().count()):
            var.ui.tableMovimientos.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


class DialogSalir(QtWidgets.QDialog):
    """Clase ventana de aviso para Salir"""

    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_windowaviso()
        var.dlgsalir.setupUi(self)


if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())
