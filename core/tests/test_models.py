import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        file = get_file_path(None, 'image.png')
        self.assertTrue(len(file), len(self.filename))


class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service)


class JobTestCase(TestCase):
    def setUp(self):
        self.job = mommy.make('Job')

    def test_str(self):
        self.assertEqual(str(self.job), self.job.job)


class TeamTestCase(TestCase):
    def setUp(self):
        self.team = mommy.make('Team')

    def test_str(self):
        self.assertEqual(str(self.team), self.team.name)


class FeatureTestCase(TestCase):
    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.name)
