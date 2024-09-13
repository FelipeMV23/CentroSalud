def nav_items(request):
    return {
        'nav_items': [
            {'name': 'Inicio', 'url_name': 'home'},
            {'name': 'Especialidades', 'url_name': 'especialistas'},
            {'name': 'Toma de hora', 'url_name': 'especialistas'},
            {'name': 'Iniciar sesión', 'url_name': 'login'},
            {'name': 'Registrarse', 'url_name': 'register'},
        ]
    }