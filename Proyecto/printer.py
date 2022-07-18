import os
from datetime import datetime

from PyQt5 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var


class Printer:
    """Clase de la funcionalidad de exportar los datos a un informe PDF"""

    def informe_pdf(self):
        """Crear un informe en pdf con los datos de los movimientos bancarios.
        Obteniene mediante una consulta los datos de los movimientos y los muestra en un documento pdf.
        Hace uso de los métodos cabecera, listadomovimientos y pie con los cuales irá formando el documento."""
        try:
            var.rep = canvas.Canvas('informes/listadomovimientos.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.listado_movimientos(self)
            query = QtSql.QSqlQuery()
            query.prepare('select id, numerocuenta, tipomovimiento, importe from movimientos order by numerocuenta')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50
                j = 690
                while query.next():
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 40, j, str(query.value(1)))
                    var.rep.drawString(i + 250, j, str(query.value(2)))
                    var.rep.drawString(i + 380, j, str(query.value(3)))
                    if j - 30 < 50:
                        j = 690
                        Printer.pie(self)
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.listado_movimientos(self)
                    else:
                        j = j - 30
            Printer.pie(self)
            var.rep.save()
            root_path = ".\\informes"
            print(root_path)
            cont = 0
            for file in os.listdir(root_path):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (root_path, file))
                cont = cont + 1

        except Exception as error:
            print('Error informepdf %s' % str(error))

    def cabecera(self):
        """Crea la cabecera del documento pdf"""
        try:
            logo = '.\\img/informe-movimientos.jpg'
            var.rep.setTitle('INFORME MOVIMIENTOS')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            var.rep.drawString(50, 805, 'INFORME MOVIMIENTOS')
            var.rep.drawImage(logo, 450, 752)
        except Exception as error:
            print('Error cabecera %s' % str(error))

    def pie(self):
        """Crea el pie del documento pdf"""
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
        except Exception as error:
            print('Error pie %s' % str(error))

    def listado_movimientos(self):
        """Crea la fila superior de la tabla donde irá el informe con los datos de los movimientos"""
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE MOVIMIENTOS'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itemcli = ['ID', 'Numero de Cuenta', 'Tipo de Movimiento', 'Importe']
            var.rep.drawString(50, 710, itemcli[0])
            var.rep.drawString(90, 710, itemcli[1])
            var.rep.drawString(290, 710, itemcli[2])
            var.rep.drawString(430, 710, itemcli[3])
            var.rep.line(45, 703, 525, 703)

        except Exception as error:
            print('Error lista de movimientos %s' % str(error))
