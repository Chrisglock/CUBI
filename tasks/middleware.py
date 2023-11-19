from .models import PerfilUsuario  # Ajusta el import según la ubicación de tu modelo

class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_profile = None
        if request.user.is_authenticated:
            user_profile = PerfilUsuario.objects.get(user=request.user)
        request.user_profile = user_profile
        response = self.get_response(request)
        return response
