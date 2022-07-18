import conexion
import var


class Movimientos:
    """Clase en la que se controla el funcionamiento de la pestaña Movimientos"""

    def cargar_tipo_movimiento(self):
        """Carga los tipos de movimientos en una variable y en un ComboBox"""
        try:
            tipos = ['', 'RETIRADA', 'INGRESO']
            var.tiposmovimiento = tipos
            for i in tipos:
                var.ui.cmbMovimiento_tipo.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))

    def limpiar_movimiento(self):
        """Limpia el texto de todos los campos de texto, etiquetas modificadas y ComboBox de la pestaña Movimientos"""
        try:
            var.ui.cmbMovimiento_cuenta.setCurrentIndex(0)
            var.ui.cmbMovimiento_tipo.setCurrentIndex(0)
            var.ui.lineEdit_movimiento_importe.setText('')
            var.ui.label_status_movimiento.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def limpiar_movimiento_no_estado(self):
        """Limpia el texto de todos los campos de texto y ComboBox de la pestaña Movimientos.
        No limpia la etiqueta de status."""
        try:
            var.ui.cmbMovimiento_cuenta.setCurrentIndex(0)
            var.ui.cmbMovimiento_tipo.setCurrentIndex(0)
            var.ui.lineEdit_movimiento_importe.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def alta_movimiento(self):
        """En la pestaña Movimientos, comprueba que el campo de texto ID tenga contenido, que los demás campos de texto
        tengan contenido y los ComboBox tengan seleccionada una opción válida.
        Muestra mensajes si el ID está vacío, si algún campo de texto está vacío o si algún ComboBox tiene seleccionada
        una opción no válida. LLama a la función de crear una movimiento."""
        try:
            datos = []
            if str(var.ui.cmbMovimiento_cuenta.currentText()) != "":
                datos.append(str(var.ui.cmbMovimiento_cuenta.currentText()))
                if str(var.ui.cmbMovimiento_tipo.currentText()) == "RETIRADA" or str(
                        var.ui.cmbMovimiento_tipo.currentText()) == "INGRESO":
                    tipo = str(var.ui.cmbMovimiento_tipo.currentText())
                    datos.append(tipo)
                    if var.ui.lineEdit_movimiento_importe.text() != "":
                        datos.append(var.ui.lineEdit_movimiento_importe.text())
                        conexion.Conexion.cargar_movimiento(self, datos)
                        Movimientos.limpiar_movimiento_no_estado(self)
                    else:
                        var.ui.label_status_movimiento.setText('Error al Crear! Importe no es válido.')
                else:
                    var.ui.label_status_movimiento.setText('Error al Crear! Se debe seleccionar un tipo válido.')
            else:
                var.ui.label_status_movimiento.setText('Error al Crear! Se debe seleccionar una cuenta.')
        except Exception as error:
            print('Error: %s' % str(error))
