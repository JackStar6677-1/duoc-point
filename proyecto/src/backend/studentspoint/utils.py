"""
Utilidades para StudentsPoint
"""

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from functools import wraps

def csrf_exempt_api(view_func):
    """
    Decorador para deshabilitar CSRF en APIs REST
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        return csrf_exempt(view_func)(*args, **kwargs)
    return wrapper

def csrf_exempt_class(cls):
    """
    Decorador de clase para deshabilitar CSRF
    """
    cls.dispatch = method_decorator(csrf_exempt)(cls.dispatch)
    return cls
