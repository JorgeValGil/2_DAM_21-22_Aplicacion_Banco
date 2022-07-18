import sys
import var


class Eventos:
    """Clase de los eventos del programa"""

    def salir(self):
        """Función para salir del programa. Muestra una ventana de aviso y captura la respuesta.
        Oculta la ventana de aviso o sale del programa"""
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print('Error en módulo salir ', error)
