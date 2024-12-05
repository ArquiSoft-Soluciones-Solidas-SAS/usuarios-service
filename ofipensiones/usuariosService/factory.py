#script para crear 3 usuarios en la base de datos

from .models import Usuario
# Lista de usuarios válidos y su institución asociada
USER_INSTITUTION_MAPPING = {
    "padre-familia-ernesto-1": "Harloe_Elementary",
    "aux-jose-1": "Harloe_Elementary",
    "padre-familia-valentina-1": "Quincy_Middle_School",
    "aux-camila-1": "Quincy_Middle_School",
}

ROLES = ["Auxiliar contable", "Padre de familia"]


# Función para crear usuarios
def create_users():
    for username, institution in USER_INSTITUTION_MAPPING.items():
        # Determinar el tipo de usuario basado en el prefijo del nombre de usuario
        tipo_usuario = "Padre de familia" if "padre-familia" in username else "Auxiliar contable"

        # Crear el usuario en la base de datos
        user = Usuario(
            nombreUsuario=username,
            tipoUsuario=tipo_usuario,
            nombreInstitucion=institution,
        )
        user.save()
        print(f"Usuario '{username}' creado con éxito.")