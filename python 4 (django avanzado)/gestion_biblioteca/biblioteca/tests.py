from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Biblioteca, Autor, Libro

class BibliotecaTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Datos iniciales para todas las pruebas
        cls.biblioteca = Biblioteca.objects.create(nombre="Biblioteca Central")
        cls.autor = Autor.objects.create(nombre="Gabriel García Márquez")
        cls.libro = Libro.objects.create(
            titulo="Cien Años de Soledad",
            autor=cls.autor,
            biblioteca=cls.biblioteca,
            fecha_publicacion="1967-05-30",
            estado="disponible"
        )

    def test_datos_iniciales(self):
        """Verificar que los datos iniciales creados coincidan con los definidos en setUpTestData"""
        biblioteca = Biblioteca.objects.get(nombre="Biblioteca Central")
        autor = Autor.objects.get(nombre="Gabriel García Márquez")
        libro = Libro.objects.get(titulo="Cien Años de Soledad")

        self.assertEqual(biblioteca.nombre, "Biblioteca Central")
        self.assertEqual(autor.nombre, "Gabriel García Márquez")
        self.assertEqual(libro.titulo, "Cien Años de Soledad")
        self.assertEqual(libro.autor, autor)
        self.assertEqual(libro.biblioteca, biblioteca)
        self.assertEqual(libro.fecha_publicacion.strftime("%Y-%m-%d"), "1967-05-30")
        self.assertEqual(libro.estado, "disponible")

    def test_urls_http_200(self):
        """Verificar que las URLs de las vistas devuelvan HTTP 200"""
        # Asegúrate de tener las vistas correspondientes configuradas en urls.py
        response_libro = self.client.get(reverse('ver_libros'))

        self.assertEqual(response_libro.status_code, 200)

    def test_plantillas_correctas(self):
        """Verificar que las vistas usan las plantillas correctas"""
        # Vistas deben estar configuradas con plantillas específicas
        response_libro = self.client.get(reverse('ver_libros'))

        self.assertTemplateUsed(response_libro, 'ver_libros.html')
