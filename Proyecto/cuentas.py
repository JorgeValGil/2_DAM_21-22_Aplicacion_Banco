import validators

import conexion
import var


class Cuentas:
    """Clase en la que se controla el funcionamiento de la pestaña Cuentas"""

    def validar_iban(self):
        """Valida el campo de texto Nº de Cuenta en la pestaña Cuentas.
        Muestra en una etiqueta una V en verde o una X en rojo, según el valor sea válido o no"""
        cuenta = var.ui.lineEdit_ncuenta.text()
        cuenta = cuenta.strip().upper()
        cuenta = cuenta.replace(" ", "").replace("-", "")
        valid = validators.iban(cuenta)
        if valid:
            var.ui.label_cuenta_valid.setStyleSheet('QLabel {color: green;}')
            var.ui.label_cuenta_valid.setText('V')
        else:
            var.ui.label_cuenta_valid.setStyleSheet('QLabel {color: red;}')
            var.ui.label_cuenta_valid.setText('X')

    def validar_iban_boolean(self):
        """Valida el campo de texto Nº de Cuenta en la pestaña Cuentas.
        Devuelve True o False, según el valor sea válido o no"""
        cuenta = var.ui.lineEdit_ncuenta.text()
        cuenta = cuenta.strip().upper()
        cuenta = cuenta.replace(" ", "").replace("-", "")
        valid = validators.iban(cuenta)
        if valid:
            return True
        else:
            return False

    def limpiar_cuenta(self):
        """Limpia el texto de todos los campos de texto, etiquetas modificadas y ComboBox de la pestaña Cuentas"""
        try:
            var.ui.lineEdit_ncuenta.setText('')
            var.ui.lineEdit_cuenta_saldo.setText('')
            var.ui.cmbClienteTitular.setCurrentIndex(0)
            var.ui.label_cuenta_valid.setText('')
            var.ui.label_status_cuenta.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def limpiar_cuenta_no_estado(self):
        """Limpia el texto de todos los campos de texto, etiquetas modificadas y ComboBox de la pestaña Cuentas.
        No limpia la etiqueta de status."""
        try:
            var.ui.lineEdit_ncuenta.setText('')
            var.ui.lineEdit_cuenta_saldo.setText('')
            var.ui.cmbClienteTitular.setCurrentIndex(0)
            var.ui.label_cuenta_valid.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def baja_cuenta(self):
        """En la pestaña Cuentas, comprueba que el campo de texto Nº de Cuenta tenga contenido.
        Muestra un mensaje si el campo está vacío o llama a la función de borrar cuenta.
        Por último, actualiza las tablas y contenidos."""
        try:
            if var.ui.lineEdit_ncuenta.text().strip() != '':
                numerocuenta = var.ui.lineEdit_ncuenta.text()
                conexion.Conexion.baja_cuenta(self, numerocuenta)
                conexion.Conexion.mostrar_en_tablas(self)
                conexion.Conexion.obtener_datos_en_var(self)
                Cuentas.limpiar_cuenta_no_estado(self)
            else:
                var.ui.label_status_cuenta.setText('Error al Eliminar! El campo de texto "Nº de Cuenta" '
                                                   'no puede estar vacío.')
        except Exception as error:
            print('Error al eliminar la cuenta: %s' % str(error))

    def modif_cuenta(self):
        """En la pestaña Cuentas, recoge los datos de los campos de texto, ComboBox y
        llama a la función de modificar cuenta.
        Comprueba que esté seleccionado un cliente o informa mediante un mensaje.
        Por último, actualiza las tablas."""
        try:
            newdata = []
            cliente = var.ui.cmbClienteTitular.currentText()
            saldo = int(var.ui.lineEdit_cuenta_saldo.text())
            numerocuenta = var.ui.lineEdit_ncuenta.text()
            if cliente != '':
                var.ui.label_status_cuenta.setText('')
                newdata.append(cliente)
                newdata.append(saldo)
                conexion.Conexion.modif_cuenta(self, numerocuenta, newdata)
                conexion.Conexion.mostrar_en_tablas(self)
            else:
                var.ui.label_status_cuenta.setText('Se debe seleccionar un cliente válido')
        except Exception as error:
            print('Error modificar cuentas: %s ' % str(error))

    def buscar_cuenta(self):
        """En la pestaña Cuentas, comprueba que el campo de texto Nº de Cuenta tenga contenido.
        Muestra un mensaje si el campo está vacío o llama a la función de buscar cuenta."""
        try:
            if var.ui.lineEdit_ncuenta.text().strip() != '':
                numerocuenta = var.ui.lineEdit_ncuenta.text()
                conexion.Conexion.buscar_cuenta(self, numerocuenta)
            else:
                var.ui.label_status_cuenta.setText('Error al Buscar! El campo de texto "Nº de cuenta" '
                                                   'no puede estar vacío.')
        except Exception as error:
            print('Error buscando cuentas: %s' % str(error))

    def alta_cuenta(self):
        """En la pestaña Cuentas, comprueba que el campo de texto Nº de Cuenta sea un IBAN válido, que los demás campos
        de texto tengan contenido y los ComboBox tengan seleccionada una opción válida.
        Muestra mensajes si el Nº de Cuenta no es válido, si algún campo de texto está vacío o si algún ComboBox tiene
        seleccionada una opción no válida.
        LLama a la función de crear una cuenta."""
        try:
            if Cuentas.validar_iban_boolean(self):
                datos = [var.ui.lineEdit_ncuenta.text()]
                if str(var.ui.cmbClienteTitular.currentText()) != "":
                    datos.append(str(var.ui.cmbClienteTitular.currentText()))
                    if var.ui.lineEdit_cuenta_saldo.text() != "":
                        datos.append(var.ui.lineEdit_cuenta_saldo.text())
                        conexion.Conexion.cargar_cuenta(self, datos)
                    else:
                        var.ui.label_status_cuenta.setText('Error al Crear! Saldo no es válido.')
                else:
                    var.ui.label_status_cuenta.setText('Error al Crear! Se debe seleccionar un cliente.')
            else:
                var.ui.label_status_cuenta.setText('Error al Crear! El campo de texto "Nº de Cuenta" no es válido.')
        except Exception as error:
            print('Error: %s' % str(error))
