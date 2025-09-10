#!/usr/bin/env python3
"""
Crear superusuario por defecto si no existe.
"""

import os
import django


def main() -> None:
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
	django.setup()

	from django.contrib.auth import get_user_model

	User = get_user_model()
	email = 'admin@duocuc.cl'
	password = 'admin123'
	username = 'admin'

	if User.objects.filter(email=email).exists():
		print('Superusuario ya existe')
		return

	User.objects.create_superuser(username, email, password)
	print('Superusuario creado: admin@duocuc.cl / admin123')


if __name__ == '__main__':
	main()


