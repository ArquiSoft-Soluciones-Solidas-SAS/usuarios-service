from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mongoengine import DoesNotExist

from usuariosService.models import Usuario


@csrf_exempt
def get_institution_from_user(request, user_id):
    # Verificar si el usuario está en la lista de usuarios válidos
    try:
        user = Usuario.objects.get(pk=user_id)
        institution = user.nombreInstitucion
        return JsonResponse({"institution": institution})
    except DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
