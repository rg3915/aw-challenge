from django.test import TestCase
from myproject.core.models import Repo


class ContractTest(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'name',
            'full_name',
            'htm_url',
            'stargazers_count',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Repo, field))
