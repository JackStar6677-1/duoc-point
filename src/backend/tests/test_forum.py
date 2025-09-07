"""
Tests para el sistema de foros de DuocPoint
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from duocpoint.apps.forum.models import Foro, Post, Comentario, PostReporte
from duocpoint.apps.campuses.models import Sede

User = get_user_model()


class ForumTestCase(APITestCase):
    """Tests para el sistema de foros"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.sede = Sede.objects.create(
            nombre='Sede Maipú',
            direccion='Av. Américo Vespucio 1501, Maipú',
            lat=-33.5115,
            lng=-70.7525
        )
        
        self.user = User.objects.create_user(
            email='test@duocuc.cl',
            password='testpass123',
            name='Test User',
            role='student',
            campus=self.sede,
            career='Ingeniería en Informática'
        )
        
        self.moderator = User.objects.create_user(
            email='moderator@duocuc.cl',
            password='testpass123',
            name='Moderator User',
            role='moderator',
            campus=self.sede,
            career='Ingeniería en Informática'
        )
        
        self.foro = Foro.objects.create(
            titulo='Foro General',
            carrera='Ingeniería en Informática',
            slug='foro-general',
            sede=self.sede
        )
    
    def test_create_post_success(self):
        """Test: Usuario puede crear post exitosamente"""
        self.client.force_authenticate(user=self.user)
        post_data = {
            'foro': self.foro.id,
            'titulo': 'Test Post',
            'cuerpo': 'Este es un post de prueba',
            'anonimo': False
        }
        response = self.client.post('/api/posts', post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Post.objects.filter(titulo='Test Post').exists())
    
    def test_create_post_anonymous(self):
        """Test: Usuario puede crear post anónimo"""
        self.client.force_authenticate(user=self.user)
        post_data = {
            'foro': self.foro.id,
            'titulo': 'Test Post Anónimo',
            'cuerpo': 'Este es un post anónimo',
            'anonimo': True
        }
        response = self.client.post('/api/posts', post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(titulo='Test Post Anónimo')
        self.assertTrue(post.anonimo)
    
    def test_create_post_with_banned_words(self):
        """Test: Post con palabras prohibidas es enviado a revisión"""
        self.client.force_authenticate(user=self.user)
        post_data = {
            'foro': self.foro.id,
            'titulo': 'Test Post con palabra prohibida',
            'cuerpo': 'Este post contiene una palabra prohibida: spam',
            'anonimo': False
        }
        response = self.client.post('/api/posts', post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(titulo='Test Post con palabra prohibida')
        self.assertEqual(post.estado, Post.Estado.REVISION)
    
    def test_create_comment_success(self):
        """Test: Usuario puede crear comentario exitosamente"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        
        self.client.force_authenticate(user=self.user)
        comment_data = {
            'post': post.id,
            'cuerpo': 'Este es un comentario de prueba'
        }
        response = self.client.post('/api/posts/{}/comentarios'.format(post.id), comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Comentario.objects.filter(cuerpo='Este es un comentario de prueba').exists())
    
    def test_vote_post_success(self):
        """Test: Usuario puede votar en post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        
        self.client.force_authenticate(user=self.user)
        vote_data = {
            'valor': 1
        }
        response = self.client.post('/api/posts/{}/votar'.format(post.id), vote_data)
        if response.status_code != status.HTTP_200_OK:
            print(f"Vote error response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.score, 1)
    
    def test_report_post_success(self):
        """Test: Usuario puede reportar post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        
        self.client.force_authenticate(user=self.user)
        report_data = {
            'post': post.id,
            'tipo': 'contenido_inapropiado',
            'descripcion': 'Este post contiene contenido inapropiado'
        }
        response = self.client.post('/api/posts/{}/reportar'.format(post.id), report_data)
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Report error response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PostReporte.objects.filter(post=post).exists())
    
    def test_moderate_post_approve(self):
        """Test: Moderador puede aprobar post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='REVISION'
        )
        
        self.client.force_authenticate(user=self.moderator)
        moderation_data = {
            'accion': 'aprobar',
            'razon': 'Post aprobado por moderador'
        }
        response = self.client.post('/api/posts/{}/moderar'.format(post.id), moderation_data)
        if response.status_code != status.HTTP_200_OK:
            print(f"Moderation error response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.estado, Post.Estado.PUBLICADO)
        self.assertEqual(post.moderado_por, self.moderator)
    
    def test_moderate_post_reject(self):
        """Test: Moderador puede rechazar post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='REVISION'
        )
        
        self.client.force_authenticate(user=self.moderator)
        moderation_data = {
            'accion': 'rechazar',
            'razon': 'Post rechazado por contenido inapropiado'
        }
        response = self.client.post('/api/posts/{}/moderar'.format(post.id), moderation_data)
        if response.status_code != status.HTTP_200_OK:
            print(f"Moderation error response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.estado, Post.Estado.RECHAZADO)
        self.assertEqual(post.moderado_por, self.moderator)
    
    def test_list_posts_by_forum(self):
        """Test: Usuario puede listar posts por foro"""
        Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post 1',
            cuerpo='Este es un post de prueba 1',
            estado='PUBLICADO'
        )
        Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post 2',
            cuerpo='Este es un post de prueba 2',
            estado='PUBLICADO'
        )
        
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/posts?foro={}'.format(self.foro.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_list_posts_requires_authentication(self):
        """Test: Listar posts requiere autenticación"""
        response = self.client.get('/api/posts')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ForumModelTestCase(TestCase):
    """Tests para los modelos del sistema de foros"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.sede = Sede.objects.create(
            nombre='Sede Maipú',
            direccion='Av. Américo Vespucio 1501, Maipú',
            lat=-33.5115,
            lng=-70.7525
        )
        
        self.user = User.objects.create_user(
            email='test@duocuc.cl',
            password='testpass123',
            name='Test User',
            role='student',
            campus=self.sede,
            career='Ingeniería en Informática'
        )
        
        self.foro = Foro.objects.create(
            titulo='Foro General',
            carrera='Ingeniería en Informática',
            slug='foro-general',
            sede=self.sede
        )
    
    def test_foro_creation(self):
        """Test: Foro puede ser creado correctamente"""
        self.assertEqual(self.foro.titulo, 'Foro General')
        self.assertEqual(self.foro.sede, self.sede)
        self.assertEqual(str(self.foro), 'Foro General')
    
    def test_post_creation(self):
        """Test: Post puede ser creado correctamente"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        self.assertEqual(post.titulo, 'Test Post')
        self.assertEqual(post.usuario, self.user)
        self.assertEqual(post.foro, self.foro)
        self.assertEqual(post.estado, 'PUBLICADO')
    
    def test_post_verificar_contenido(self):
        """Test: Verificación automática de contenido"""
        # Post con contenido limpio
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post con contenido limpio',
            estado='REVISION'
        )
        post.estado = post.verificar_contenido()
        self.assertEqual(post.estado, Post.Estado.PUBLICADO)
        
        # Post con palabras prohibidas
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este post contiene spam',
            estado='REVISION'
        )
        post.estado = post.verificar_contenido()
        self.assertEqual(post.estado, Post.Estado.REVISION)
    
    def test_post_moderar(self):
        """Test: Moderación de post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='REVISION'
        )
        
        # Aprobar post
        post.moderar(self.user, 'aprobar', 'Post aprobado')
        self.assertEqual(post.estado, Post.Estado.PUBLICADO)
        self.assertEqual(post.moderado_por, self.user)
        
        # Rechazar post
        post.estado = 'REVISION'
        post.moderar(self.user, 'rechazar', 'Post rechazado')
        self.assertEqual(post.estado, Post.Estado.RECHAZADO)
    
    def test_post_reportar(self):
        """Test: Reporte de post"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        
        post.reportar(self.user, 'CONTENIDO_INAPROPIADO', 'Contenido inapropiado')
        self.assertEqual(post.total_reportes, 1)
        self.assertTrue(PostReporte.objects.filter(post=post).exists())
    
    def test_comentario_creation(self):
        """Test: Comentario puede ser creado correctamente"""
        post = Post.objects.create(
            foro=self.foro,
            usuario=self.user,
            titulo='Test Post',
            cuerpo='Este es un post de prueba',
            estado='PUBLICADO'
        )
        
        comentario = Comentario.objects.create(
            post=post,
            usuario=self.user,
            cuerpo='Este es un comentario de prueba'
        )
        self.assertEqual(comentario.cuerpo, 'Este es un comentario de prueba')
        self.assertEqual(comentario.post, post)
        self.assertEqual(comentario.usuario, self.user)
