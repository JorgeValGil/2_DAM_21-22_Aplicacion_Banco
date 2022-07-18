import conexion
import var


class Clientes:
    """Clase en la que se controla el funcionamiento de la pestaña Clientes"""

    def validar_dni(self):
        """Valida el campo de texto DNI en la pestaña Clientes.
        Muestra en una etiqueta una V en verde o una X en rojo, según el valor sea válido o no"""
        try:
            dni = var.ui.lineEdit_dni.text()
            var.ui.lineEdit_dni.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # dígito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayúscula
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.label_dni_valid.setStyleSheet('QLabel {color: green;}')
                    var.ui.label_dni_valid.setText('V')
                else:
                    var.ui.label_dni_valid.setStyleSheet('QLabel {color: red;}')
                    var.ui.label_dni_valid.setText('X')
            else:
                var.ui.label_dni_valid.setStyleSheet('QLabel {color: red;}')
                var.ui.label_dni_valid.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def validar_dni_boolean(self):
        """Valida el campo de texto DNI en la pestaña Clientes.
        Devuelve True o False, según el valor sea válido o no"""
        try:
            dni = var.ui.lineEdit_dni.text()
            var.ui.lineEdit_dni.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # dígito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayúscula
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def limpiar_cliente(self):
        """Limpia el texto de todos los campos de texto y etiquetas modificadas de la pestaña Clientes"""
        try:
            var.ui.lineEdit_dni.setText('')
            var.ui.lineEdit_apellido.setText('')
            var.ui.lineEdit_nombre.setText('')
            var.ui.label_dni_valid.setText('')
            var.ui.label_status_cliente.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def limpiar_cliente_no_estado(self):
        """Limpia el texto de todos los campos de texto y etiquetas modificadas de la pestaña Clientes.
        No limpia la etiqueta de status."""
        try:
            var.ui.lineEdit_dni.setText('')
            var.ui.lineEdit_nombre.setText('')
            var.ui.lineEdit_apellido.setText('')
            var.ui.label_dni_valid.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    def baja_cliente(self):
        """En la pestaña Clientes, comprueba que el campo de texto DNI tenga contenido.
         Muestra un mensaje si el campo está vacío o llama a la función de borrar cliente.
         Por último, actualiza las tablas y contenidos."""
        try:
            if var.ui.lineEdit_dni.text().strip() != '':
                dni = var.ui.lineEdit_dni.text()
                conexion.Conexion.baja_cli(self, dni)
                conexion.Conexion.mostrar_en_tablas(self)
                conexion.Conexion.obtener_datos_en_var(self)
                Clientes.limpiar_cliente_no_estado(self)
            else:
                var.ui.label_status_cliente.setText('Error al Eliminar! El campo de texto "DNI" no puede estar vacío.')
        except Exception as error:
            print('Error al eliminar el cliente: %s' % str(error))

    def modif_cliente(self):
        """En la pestaña Clientes, recoge los datos de los campos de texto y llama a la función de modificar cliente.
        Comprueba que los campos apellidos y nombre tengan contenido o informa mediante un mensaje.
        Por último, actualiza las tablas."""
        try:
            apellido = var.ui.lineEdit_apellido.text()
            nombre = var.ui.lineEdit_nombre.text()
            if apellido != '' and nombre != '':
                var.ui.label_status_cliente.setText('')
                newdata = [apellido, nombre]
                dni = var.ui.lineEdit_dni.text()
                conexion.Conexion.modif_cli(self, dni, newdata)
                conexion.Conexion.mostrar_en_tablas(self)
            else:
                var.ui.label_status_cliente.setText('No pueden haber campos de texto vacíos')
        except Exception as error:
            print('Error modificar clientes: %s ' % str(error))

    def buscar_cliente(self):
        """En la pestaña Clientes, comprueba que el campo de texto DNI tenga contenido.
         Muestra un mensaje si el campo está vacío o llama a la función de buscar cliente."""
        try:
            if var.ui.lineEdit_dni.text().strip() != '':
                dni = var.ui.lineEdit_dni.text()
                conexion.Conexion.buscar_cli(self, dni)
            else:
                var.ui.label_status_cliente.setText('Error al Buscar! El campo de texto "DNI" no puede estar vacío.')
        except Exception as error:
            print('Error buscando clientes: %s' % str(error))

    def alta_cliente(self):
        """En la pestaña Clientes, comprueba que el campo de texto DNI sea un DNI válido y que los demás
        campos de texto tengan contenido. Muestra mensajes si el DNI no es válido o si algún campo de texto está vacío.
         LLama a la función de crear un cliente."""
        try:
            if Clientes.validar_dni_boolean(self):
                datos = [var.ui.lineEdit_dni.text()]
                if var.ui.lineEdit_apellido.text() != "":
                    datos.append(var.ui.lineEdit_apellido.text())
                    if var.ui.lineEdit_nombre.text() != "":
                        datos.append(var.ui.lineEdit_nombre.text())
                        conexion.Conexion.cargar_cli(self, datos)
                    else:
                        var.ui.label_status_cliente.setText('Error al Crear! El campo nombre está vacío.')
                else:
                    var.ui.label_status_cliente.setText('Error al Crear! El campo apellido está vacío.')
            else:
                var.ui.label_status_cliente.setText('Error al Crear! El campo de texto "DNI" no es válido.')
        except Exception as error:
            print('Error: %s' % str(error))
