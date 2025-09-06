#!/usr/bin/env python3
"""
Script para ejecutar todos los tests de DuocPoint
"""

import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

def setup_django():
    """Configurar Django para testing"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.test')
    django.setup()

def run_tests():
    """Ejecutar todos los tests"""
    setup_django()
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # Ejecutar tests
    failures = test_runner.run_tests([
        'tests.test_authentication',
        'tests.test_forum',
        'duocpoint.apps.accounts.tests',
        'duocpoint.apps.forum.tests',
        'duocpoint.apps.market.tests',
        'duocpoint.apps.portfolio.tests',
        'duocpoint.apps.polls.tests',
        'duocpoint.apps.campuses.tests',
    ])
    
    if failures:
        print(f"\n❌ {failures} test(s) failed!")
        sys.exit(1)
    else:
        print("\n✅ All tests passed!")

if __name__ == '__main__':
    run_tests()
