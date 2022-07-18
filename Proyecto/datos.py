import conexion
import var


class Datos:
    """Clase en la que se controla el funcionamiento de la pestaña Datos"""

    def limpiar_dato(self):
        """Limpia el texto dl campo de texto, etiquetas modificadas, ComboBox y tabla de la pestaña Datos"""
        try:
            var.ui.tableDatos.clearContents()
            var.ui.tableDatos.setRowCount(0)
            var.ui.comboBox_datos_cuenta.setCurrentIndex(0)
            var.ui.label_status_datos.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def buscar_datos(self):
        """En la pestaña Datos, comprueba que el texto del ComboBox Nº de Cuenta tenga contenido.
        Muestra un mensaje si el campo está vacío o llama a la función de buscar Dato."""
        try:
            if str(var.ui.comboBox_datos_cuenta.currentText()) != "":
                numerocuenta = str(var.ui.comboBox_datos_cuenta.currentText())
                conexion.Conexion.buscar_dato(self, numerocuenta)
            else:
                var.ui.label_status_datos.setText('Error al Buscar! Se debe seleccionar una cuenta.')
        except Exception as error:
            print('Error buscando datos: %s' % str(error))
