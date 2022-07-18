from PyQt5 import QtWidgets, QtSql

import var


class Conexion:
    """Clase encargada de las realizar las acciones con la base de datos"""

    def db_connect(self, filename):
        """Conexión a la base de datos."""
        var.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        var.db.setDatabaseName(filename)
        if not var.db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer la conexion.\n' 'Haz Click para Cancelar',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión Establecida')
            return True

    def obtener_datos_en_var(self):
        """Carga los DNI de los clientes en una variable y en un Combobox.
        Carga los Nº de Cuenta de las Cuentas en una variable y en Comboboxes"""
        Conexion.obtener_clientes(self)
        Conexion.obtener_cuentas(self)

    def obtener_clientes(self):
        """Carga los DNI de los clientes en una variable y en un Combobox"""
        clientes = ['']
        query = QtSql.QSqlQuery()
        query.prepare('select dni from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                clientes.append(dni)
        else:
            print("Error obteniendo clientes: ", query.lastError().text())

        var.datosbdclientes = clientes
        var.ui.cmbClienteTitular.clear()
        for i in clientes:
            var.ui.cmbClienteTitular.addItem(i)

    def obtener_cuentas(self):
        """Carga los Nº de Cuenta de las Cuentas en una variable y en Comboboxes"""
        cuentas = ['']
        query = QtSql.QSqlQuery()
        query.prepare('select numerocuenta from cuentas')
        if query.exec_():
            while query.next():
                numerocuenta = query.value(0)
                cuentas.append(numerocuenta)
        else:
            print("Error obteniendo cuentas: ", query.lastError().text())

        var.datosbdcuentas = cuentas
        var.ui.cmbMovimiento_cuenta.clear()
        var.ui.comboBox_datos_cuenta.clear()
        for i in cuentas:
            var.ui.cmbMovimiento_cuenta.addItem(i)
            var.ui.comboBox_datos_cuenta.addItem(i)

    def mostrar_en_tablas(self):
        """Carga los datos de la tabla de base de datos clientes, en la tabla de la pestaña Clientes.
        Carga los datos de la tabla de base de datos cuentas, en la tabla de la pestaña Cuentas.
        Carga los datos de la tabla de base de datos movimientos, en la tabla de la pestaña Movimientos"""
        Conexion.mostrar_clientes(self)
        Conexion.mostrar_cuentas(self)
        Conexion.mostrar_movimientos(self)

    def mostrar_clientes(self):
        """Carga los datos de la tabla de base de datos clientes, en la tabla de la pestaña Clientes"""
        var.ui.tableClientes.clearContents()
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tableClientes.setRowCount(index + 1)
                var.ui.tableClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def mostrar_cuentas(self):
        """Carga los datos de la tabla de base de datos cuentas, en la tabla de la pestaña Cuentas"""
        var.ui.tableCuentas.clearContents()
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select numerocuenta, cliente, saldo from cuentas')
        if query.exec_():
            while query.next():
                numerocuenta = query.value(0)
                cliente = query.value(1)
                saldo = str(query.value(2))
                var.ui.tableCuentas.setRowCount(index + 1)
                var.ui.tableCuentas.setItem(index, 0, QtWidgets.QTableWidgetItem(numerocuenta))
                var.ui.tableCuentas.setItem(index, 1, QtWidgets.QTableWidgetItem(cliente))
                var.ui.tableCuentas.setItem(index, 2, QtWidgets.QTableWidgetItem(saldo))
                index += 1
        else:
            print("Error mostrar cuentas: ", query.lastError().text())

    def mostrar_movimientos(self):
        """Carga los datos de la tabla de base de datos movimientos, en la tabla de la pestaña Movimientos"""
        var.ui.tableMovimientos.clearContents()
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select id, numerocuenta, tipomovimiento, importe from movimientos')
        if query.exec_():
            while query.next():
                movimiento_id = str(query.value(0))
                numerocuenta = query.value(1)
                tipomovimiento = query.value(2)
                importe = str(query.value(3))
                var.ui.tableMovimientos.setRowCount(index + 1)
                var.ui.tableMovimientos.setItem(index, 0, QtWidgets.QTableWidgetItem(movimiento_id))
                var.ui.tableMovimientos.setItem(index, 1, QtWidgets.QTableWidgetItem(numerocuenta))
                var.ui.tableMovimientos.setItem(index, 2, QtWidgets.QTableWidgetItem(tipomovimiento))
                var.ui.tableMovimientos.setItem(index, 3, QtWidgets.QTableWidgetItem(importe))
                index += 1
        else:
            print("Error mostrar movimientos: ", query.lastError().text())

    def buscar_cli(self, dni):
        """Busca un cliente mediante su DNI y lo carga en los campos de texto de la pestaña Clientes.
        Muestra mensaje en etiqueta status Cliente"""
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos, nombre from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                apellidos = query.value(0)
                nombre = query.value(1)

                var.ui.lineEdit_apellido.setText(apellidos)
                var.ui.lineEdit_nombre.setText(nombre)

                var.ui.label_status_cliente.setText('Cliente con dni ' + dni + ' cargado')
        else:
            print('Error buscando clientes: ', query.lastError().text())

    def buscar_cuenta(self, numerocuenta):
        """Busca una cuenta mediante su Nº de cuenta y lo carga en el campo de texto y ComboBox de la pestaña Cuenta.
        Muestra mensaje en etiqueta status Cuenta"""
        query = QtSql.QSqlQuery()
        query.prepare('select cliente, saldo from cuentas where numerocuenta = :numerocuenta')
        query.bindValue(':numerocuenta', numerocuenta)
        if query.exec_():
            while query.next():
                cliente = query.value(0)
                saldo = int(query.value(1))

                indice_cliente = var.datosbdclientes.index(cliente)
                var.ui.cmbClienteTitular.setCurrentIndex(indice_cliente)
                var.ui.lineEdit_cuenta_saldo.setText(str(saldo))

                var.ui.label_status_cuenta.setText('Cuenta con Nº ' + numerocuenta + ' cargado')
        else:
            print('Error buscando cuentas: ', query.lastError().text())

    def buscar_dato(self, numerocuenta):
        """Busca los movimientos de una cuenta mediante un Nº de cuenta.
        Muestra los datos en la tabla de la pestaña Datos.
        Muestra mensaje en etiqueta status Datos
        """
        var.ui.tableDatos.clearContents()
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare(
            'select id, tipomovimiento, importe from movimientos where numerocuenta = :numerocuenta order by id ASC')
        query.bindValue(':numerocuenta', numerocuenta)
        if query.exec_():
            while query.next():
                tipomovimiento = query.value(1)
                importe = str(query.value(2))
                var.ui.tableDatos.setRowCount(index + 1)
                var.ui.tableDatos.setItem(index, 0, QtWidgets.QTableWidgetItem(numerocuenta))
                var.ui.tableDatos.setItem(index, 1, QtWidgets.QTableWidgetItem(tipomovimiento))
                var.ui.tableDatos.setItem(index, 2, QtWidgets.QTableWidgetItem(importe))
                index += 1
            var.ui.label_status_datos.setText('Movimientos cuenta con Nº ' + numerocuenta + ' cargados')
        else:
            print("Error mostrar datos: ", query.lastError().text())

    def baja_cli(self, dni):
        """Borra un cliente mediante un DNI.
        Llama a la función bajaCuentasCliente la cual borra las cuentas del cliente y los movimientos de dichas cuentas.
        Muestra mensaje en etiqueta status Clientes"""
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            if query.numRowsAffected() > 0:
                var.ui.label_status_cliente.setText('Cliente con dni ' + dni + ' dado de baja')
                Conexion.baja_cuentas_cliente(self, dni)
            else:
                var.ui.label_status_cliente.setText('No se ha borrado ningún cliente con el dni ' + dni)
        else:
            print('Error borrando clientes: ', query.lastError().text())

    def baja_cuentas_cliente(self, dni):
        """Borra las cuentas mediante un DNI de un cliente. Borra los movimientos de dichas cuentas."""
        query = QtSql.QSqlQuery()
        query.prepare('select numerocuenta from cuentas where cliente = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                numerocuenta = query.value(0)
                querycuenta = QtSql.QSqlQuery()
                querycuenta.prepare('delete from cuentas where numerocuenta = :numerocuenta')
                querycuenta.bindValue(':numerocuenta', numerocuenta)
                if querycuenta.exec_():
                    if querycuenta.numRowsAffected() > 0:
                        print('Cuentas del cliente ' + dni + ' eliminadas')
                    else:
                        print('El cliente ' + dni + ' no tenía cuentas')

                querymovimiento = QtSql.QSqlQuery()
                querymovimiento.prepare('delete from movimientos where numerocuenta = :numerocuenta')
                querymovimiento.bindValue(':numerocuenta', numerocuenta)
                if querymovimiento.exec_():
                    if querymovimiento.numRowsAffected() > 0:
                        print('Movimientos de la cuenta ' + numerocuenta + ' eliminados')
                    else:
                        print('La cuenta ' + numerocuenta + ' no tenía movimientos')
        else:
            print('Error borrando cuentas: ', query.lastError().text())

    def baja_cuenta(self, numerocuenta):
        """Borra una cuenta mediante un numero de cuenta. Borra los movimientos de dicha cuenta.
        Muestra mensaje en etiqueta status Cuentas"""
        query = QtSql.QSqlQuery()
        query.prepare('delete from cuentas where numerocuenta = :numerocuenta')
        query.bindValue(':numerocuenta', numerocuenta)
        if query.exec_():
            if query.numRowsAffected() > 0:
                var.ui.label_status_cuenta.setText('Cuenta con Nº ' + numerocuenta + ' dada de baja')

                querymovimiento = QtSql.QSqlQuery()
                querymovimiento.prepare('delete from movimientos where numerocuenta = :numerocuenta')
                querymovimiento.bindValue(':numerocuenta', numerocuenta)
                if querymovimiento.exec_():
                    if querymovimiento.numRowsAffected() > 0:
                        print('Movimientos de la cuenta ' + numerocuenta + ' eliminados')
                    else:
                        print('La cuenta ' + numerocuenta + ' no tenía movimientos')
            else:
                var.ui.label_status_cuenta.setText(
                    'No se ha borrado ninguna cuenta con el numerocuenta ' + numerocuenta)
        else:
            print('Error borrando cuentas: ', query.lastError().text())

    def cargar_cli(self, cliente):
        """Crea un cliente. Recibe los datos a insertar y ejecuta un insert.
        Muestra mensaje en la etiqueta status Clientes.
        Por último, actualiza las tablas y contenidos."""
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre) VALUES (:dni, :apellidos, :nombre)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        if query.exec_():
            print('Inserción correcta')
            var.ui.label_status_cliente.setText('Cliente con dni ' + str(cliente[0]) + ' creado')
            Conexion.mostrar_en_tablas(self)
            Conexion.obtener_datos_en_var(self)
        else:
            print('Error: ', query.lastError().text())
            if query.lastError().text() == "UNIQUE constraint failed: clientes.DNI Unable to fetch row":
                var.ui.label_status_cliente.setText('Ya existe un cliente con DNI ' + str(cliente[0]))

    def cargar_cuenta(self, cuenta):
        """Crea una cuenta. Recibe los datos a insertar y ejecuta un insert.
        Llama a la funcion cargarMovimientoCreacion para crear el movimiento de creación de la cuenta.
        Muestra mensaje en la etiqueta status Cuenta.
        Por último, actualiza las tablas y contenidos."""
        print('cargar cuenta')
        query = QtSql.QSqlQuery()
        query.prepare('insert into cuentas (numerocuenta, cliente, saldo) VALUES (:numerocuenta, :cliente, :saldo)')
        query.bindValue(':numerocuenta', str(cuenta[0]))
        query.bindValue(':cliente', str(cuenta[1]))
        query.bindValue(':saldo', str(cuenta[2]))
        if query.exec_():
            print('Inserción correcta')
            var.ui.label_status_cuenta.setText('Cuenta con Nº ' + str(cuenta[0]) + ' creada')
            Conexion.cargar_movimiento_creacion(self, str(cuenta[0]), str(cuenta[2]))
            Conexion.mostrar_en_tablas(self)
            Conexion.obtener_datos_en_var(self)
        else:
            print('Error: ', query.lastError().text())
            if query.lastError().text() == "UNIQUE constraint failed: cuentas.NUMEROCUENTA Unable to fetch row":
                var.ui.label_status_cuenta.setText('Ya existe una cuenta con Nº ' + str(cuenta[0]))

    def cargar_movimiento_creacion(self, numerocuenta, importe):
        """Crea el Movimiento de tipo CREACIÓN de una Cuenta.
        Recibe el numero de cuenta y el importe ejecuta un insert, usando como tipo de movimiento CREACIÓN."""
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into movimientos (numerocuenta, tipomovimiento, importe) '
            'VALUES (:numerocuenta, :tipomovimiento, :importe)')
        query.bindValue(':numerocuenta', numerocuenta)
        query.bindValue(':tipomovimiento', "CREACIÓN")
        query.bindValue(':importe', importe)
        if query.exec_():
            print('Inserción movimiento creación')
        else:
            print('Error: ', query.lastError().text())

    def cargar_movimiento(self, movimiento):
        """Crea un Movimiento. Recibe los datos a insertar y ejecuta un insert.
        Muestra mensaje en la etiqueta status Movimiento.
        Llama a la función modificarSaldoMovimiento, la cual modifica el saldo de la cuenta.
        Por último, actualiza las tablas y contenidos."""
        print('cargar movimiento')
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into movimientos (numerocuenta, tipomovimiento, importe) '
            'VALUES (:numerocuenta, :tipomovimiento, :importe)')
        query.bindValue(':numerocuenta', str(movimiento[0]))
        query.bindValue(':tipomovimiento', str(movimiento[1]))
        query.bindValue(':importe', str(movimiento[2]))
        if query.exec_():
            print('Inserción correcta')
            var.ui.label_status_movimiento.setText('Movimiento creado')
            Conexion.modificar_saldo_movimiento(self, movimiento)
            Conexion.mostrar_en_tablas(self)
            Conexion.obtener_datos_en_var(self)
        else:
            print('Error: ', query.lastError().text())

    def modificar_saldo_movimiento(self, movimiento):
        """Modifica el saldo de una cuenta al hacer un movimiento.
        Obtiene el saldo anterior de la cuenta, suma o resta el importe del movimiento en base al tipo,
        actualiza el saldo de la cuenta."""
        tipo = str(movimiento[1])
        get_saldo = False
        saldo = 0

        queryget = QtSql.QSqlQuery()
        queryget.prepare('select saldo from cuentas where numerocuenta=:numerocuenta')
        queryget.bindValue(':numerocuenta', str(movimiento[0]))
        if queryget.exec_():
            while queryget.next():
                saldo = int(queryget.value(0))
                get_saldo = True
        else:
            print("Error obteniendo saldo para modificar: ", queryget.lastError().text())

        if get_saldo:
            if tipo == "INGRESO":
                saldo = saldo + int(movimiento[2])
            if tipo == "RETIRADA":
                saldo = saldo - int(movimiento[2])

        query = QtSql.QSqlQuery()
        query.prepare('update cuentas set saldo=:nuevosaldo where numerocuenta=:numerocuenta')
        query.bindValue(':numerocuenta', str(movimiento[0]))
        query.bindValue(':nuevosaldo', saldo)
        if query.exec_():
            print('Saldo cuenta modificado')
        else:
            print("Error modificar saldo cuenta: ", query.lastError().text())

    def modif_cli(self, dni, newdata):
        """Modifica un cliente.
        Actualiza los datos de un cliente.
        Muestra mensaje en la etiqueta status Cliente."""
        query = QtSql.QSqlQuery()
        query.prepare('update clientes set apellidos=:apellidos, nombre=:nombre where dni=:dni')
        query.bindValue(':dni', dni)
        query.bindValue(':apellidos', str(newdata[0]))
        query.bindValue(':nombre', str(newdata[1]))
        if query.exec_():
            print('Cliente modificado')
            var.ui.label_status_cliente.setText('Cliente con dni ' + dni + ' modificado')
        else:
            print("Error modificar cliente: ", query.lastError().text())

    def modif_cuenta(self, numerocuenta, newdata):
        """Modifica una cuenta.
        Actualiza los datos de una cuenta.
        Muestra mensaje en la etiqueta status Cuenta.
        Llama a la funcion cargar_movimiento_modificacion para crear el movimiento de modificación de la cuenta.
        Por último, actualiza las tablas."""
        query = QtSql.QSqlQuery()
        query.prepare('update cuentas set cliente=:cliente, saldo=:saldo where numerocuenta=:numerocuenta')
        query.bindValue(':numerocuenta', numerocuenta)
        query.bindValue(':cliente', str(newdata[0]))
        query.bindValue(':saldo', str(newdata[1]))
        if query.exec_():
            print('Cuenta modificada')
            var.ui.label_status_cuenta.setText('Cuenta con Nº ' + numerocuenta + ' modificada')
            Conexion.cargar_movimiento_modificacion(self, numerocuenta, str(newdata[1]))
            Conexion.mostrar_en_tablas(self)
        else:
            print("Error modificar cuenta: ", query.lastError().text())

    def cargar_movimiento_modificacion(self, numerocuenta, importe):
        """Crea un Movimiento de tipo MODIFICACIÓN para una Cuenta.
        Recibe el numero de cuenta y el importe ejecuta un insert, usando como tipo de movimiento MODIFICACIÓN."""
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into movimientos (numerocuenta, tipomovimiento, importe) '
            'VALUES (:numerocuenta, :tipomovimiento, :importe)')
        query.bindValue(':numerocuenta', numerocuenta)
        query.bindValue(':tipomovimiento', "MODIFICACIÓN")
        query.bindValue(':importe', importe)
        if query.exec_():
            print('Inserción movimiento creación')
        else:
            print('Error: ', query.lastError().text())
