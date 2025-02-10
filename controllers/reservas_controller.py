from models.firebase_model import FirebaseModel


class ReservasController:
    def __init__(self):
        self.firebase = FirebaseModel()

    def crear_reserva(self, usuario_id, cuidador_id, fecha_inicio, fecha_fin, mascota):
        """Crea una nueva reserva en Firestore."""
        return self.firebase.create_reservation(
            usuario_id, cuidador_id, fecha_inicio, fecha_fin, mascota
        )

    def obtener_reserva(self, reserva_id):
        """Obtiene la información de una reserva."""
        return self.firebase.get_reservation(reserva_id)

    def actualizar_estado_reserva(self, reserva_id, nuevo_estado):
        """Actualiza el estado de una reserva."""
        return self.firebase.update_reservation_status(reserva_id, nuevo_estado)

    def eliminar_reserva(self, reserva_id):
        """Elimina una reserva de Firestore."""
        return self.firebase.delete_reservation(reserva_id)
