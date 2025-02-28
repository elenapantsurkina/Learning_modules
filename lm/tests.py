from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lm.models import Learning
from lm.serializers import LearningSerializer
from users.models import User


class LearningTestCase(APITestCase):

    def setUp(self):
        """Данные для теста(фикстура для теста)."""
        self.user = User.objects.create(email="test@test.com")
        self.learning = Learning.objects.create(
            name="Рисование", description="Курс позволит нарисовать Вам первую картину", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_learning_retrieve(self):
        url = reverse("lm:learning-detail", args=(self.learning.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.learning.name)

    def test_learning_create(self):
        url = reverse("lm:learning-list")
        data = {
            "name": "Математика",
            "description": "После прохождения курса Вы будете разбираться в логарифмах",
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_learning_update(self):
        """Тест на обновление образовательного модуля."""
        url = reverse("lm:learning-detail", args=(self.learning.pk,))
        data = {"name": "Логарифмы"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Логарифмы")

    def test_learning_delete(self):
        """Тест на удаление образовательного модуля."""
        url = reverse("lm:learning-detail", args=(self.learning.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_learning_list(self):
        """Тест на получение списка образовательных модулей."""
        url = reverse("lm:learning-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.learning.pk,
                    "name": "Рисование",
                    "description": "Курс позволит нарисовать Вам первую картину",
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class LearningSerializerTest(TestCase):
    def setUp(self):
        """Данные для теста (фикстура для теста)."""
        self.user = User.objects.create(email="test@test.com")
        self.valid_data = {
            "name": "Рисование",
            "description": "Курс позволит нарисовать Вам первую картину",
            "owner": self.user.id,
        }
        self.invalid_data = {
            "name": "",  # Пустое имя должно вызвать ошибку валидации
            "description": "Курс позволит нарисовать Вам первую картину",
            "owner": self.user.id,
        }

    def test_learning_serializer_with_valid_data(self):
        """Тест на сериализацию с валидными данными."""
        serializer = LearningSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], "Рисование")
        self.assertEqual(serializer.validated_data["description"], "Курс позволит нарисовать Вам первую картину")

    def test_learning_serializer_with_invalid_data(self):
        """Тест на сериализацию с невалидными данными."""
        serializer = LearningSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)  # Проверяем, что ошибка валидации для поля 'name'
