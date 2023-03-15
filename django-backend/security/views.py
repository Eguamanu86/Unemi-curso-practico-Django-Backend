from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views import View
import json

class LoginPageView(TemplateView):
    template_name = 'security/login.html'

    def post(self, request, *args, **kwargs):
        status_code = None
        data = {'resp': False, 'error': None}
        try:

            if 'username' in request.POST:
                json_data = request.POST
            else:
                json_data = json.loads(request.body)

            username = json_data['username']
            password = json_data['password']
            # autenticar si el usuario y password es correcto. retorna un objeto usuario
            user = authenticate(username=username,password=password)

            # valida que el usuario no sea nulo
            if user is not None:
                # valida que el usuario este activo
                if user.is_active:
                    # crea la session del usuario entre el navegado y el servidor
                    login(request, user)
                    status_code = 200
                    data['resp'] = True
                    data['`user`'] = {
                        "username": user.username,
                        "email" : user.email,
                        "names": f"{user.first_name} {user.last_name}",
                        "status": user.is_active
                    }
                    # retornamos la respuesta, con status 200: OK
                    return JsonResponse(data, status=status_code)
                else:
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
            else:
                data['error'] = 'Login Fallido!, credenciales incorrectas.'

            status_code = 400

        except Exception as e:
            data['error'] = 'Error internal Server'
            status_code = 500

        return JsonResponse(data, status=status_code)

# Create your views here.
class InicioTemplate(LoginRequiredMixin, TemplateView):
    login_url = '/security/login'
    redirect_field_name = 'redirect_to'
    template_name = 'security/index.html'
