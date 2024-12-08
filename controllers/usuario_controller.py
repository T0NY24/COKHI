# controllers/usuario_controller.py
from models.usuario_model import UsuarioModel
from datetime import datetime
import uuid

def generate_unique_id():
    """Genera un ID único para los usuarios."""
    return str(uuid.uuid4())

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def crear_usuario(self, correoElectronico, nombre, telefono, ciudad, codigoPostal, estado="activo",
                      idioma="es", modoOscuro=False, altoContraste=False,
                      tarjetaCredito=False, paypal=False, pagoContraEntrega=False,
                      email=True, push=False, sms=False):
        """Crea un nuevo usuario."""
        usuario = {
            'id': generate_unique_id(),
            'correoElectronico': correoElectronico,
            'nombre': nombre,
            'telefono': telefono,
            'fechaRegistro': datetime.now(),
            'estado': estado,
            'configuracion': {
                'idioma': idioma,
                'modoOscuro': modoOscuro,
                'altoContraste': altoContraste
            },
            'metodosPago': {
                'tarjetaCredito': tarjetaCredito,
                'paypal': paypal,
                'pagoContraEntrega': pagoContraEntrega
            },
            'ubicacion': {
                'ciudad': ciudad,
                'codigoPostal': codigoPostal
            },
            'preferenciasNotificacion': {
                'email': email,
                'push': push,
                'sms': sms
            }
        }
        self.model.crear_usuario(usuario)

    def obtener_usuario(self, user_id):
        """Obtiene un usuario por su ID."""
        return self.model.obtener_usuario(user_id)

    def actualizar_usuario(self, user_id, data):
        """Actualiza datos específicos de un usuario."""
        self.model.actualizar_usuario(user_id, data)

    def eliminar_usuario(self, user_id):
        """Elimina un usuario por su ID."""
        self.model.eliminar_usuario(user_id)

    def obtener_todos_usuarios(self):
        """Obtiene todos los usuarios."""
        return self.model.obtener_todos_usuarios()
