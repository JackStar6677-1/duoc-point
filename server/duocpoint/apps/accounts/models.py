"""Modelos para la aplicación de cuentas.

Contiene el modelo de usuario personalizado utilizado por todo el
proyecto. El objetivo principal es extender el modelo por defecto de
`django.contrib.auth` para utilizar el correo electrónico como
identificador principal y agregar metadatos adicionales como la sede,
la carrera y el rol del usuario.

Para validar que sólo se utilicen correos institucionales se define el
validador :func:`validate_duoc_email`. Si en el futuro el dominio
cambia, basta con modificar la constante ``DUOC_DOMAIN``.
"""

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


DUOC_DOMAIN = "@duocuc.cl"


def validate_duoc_email(value: str) -> None:
    """Ensure that the email belongs to the institutional domain.

    Parameters
    ----------
    value:
        Correo electrónico ingresado por el usuario.

    Raises
    ------
    ValidationError
        Si el correo no termina en ``@duocuc.cl``.
    """

    if not value.lower().endswith(DUOC_DOMAIN):
        raise ValidationError("Solo se permiten correos @duocuc.cl")


class UserManager(BaseUserManager):
    """Administrador para el modelo :class:`User`.

    Maneja la creación de usuarios asegurando que siempre exista un
    correo válido. Las contraseñas se almacenan usando el método de
    hashing de Django.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        validate_duoc_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Usuario principal del sistema.

    Campos principales
    ------------------
    email:
        Identificador único del usuario. Debe pertenecer al dominio
        institucional ``@duocuc.cl``.
    name:
        Nombre visible del usuario.
    campus:
        Sede a la que pertenece el usuario. Es opcional para permitir
        registros tempranos.
    career:
        Carrera o programa del estudiante.
    role:
        Define los permisos generales del usuario dentro de la
        plataforma. Para añadir nuevos roles basta con extender
        :class:`User.Roles`.
    """

    class Roles(models.TextChoices):
        STUDENT = "student", "Student"
        MODERATOR = "moderator", "Moderator"
        DIRECTOR_CARRERA = "director_carrera", "Director de Carrera"
        ADMIN_GLOBAL = "admin_global", "Administrador Global"

    email = models.EmailField("email address", unique=True, validators=[validate_duoc_email])
    name = models.CharField(max_length=150)
    campus = models.ForeignKey(
        "campuses.Campus", on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    career = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.STUDENT)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = UserManager()

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.email

