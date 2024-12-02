from django.db.models.expressions import result
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from usuariosService.models import Usuario


@csrf_exempt
def get(request):
    usuarios = Usuario.objects.all()
    resultado = []
    for usuario in usuarios:
        resultado.append({
            "id": str(usuario.id),
            "nombreUsuario": usuario.nombreUsuario,
            "correo": usuario.correo,
            "tipoUsuario": usuario.tipoUsuario,
            "institucionId": usuario.institucionId,
            "nombreInstitucion": usuario.nombreInstitucion,
        })
