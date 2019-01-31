import graphene

from snapshottest import TestCase
from graphene.test import Client

from queries import Query


class APITestCase(TestCase):
    def test_api_1(self):
        client = Client(graphene.Schema(query=Query))
        self.assert_match_snapshot(client.execute('''{ hello }'''))

    def test_api_2(self):
        client = Client(graphene.Schema(query=Query))
        self.assert_match_snapshot(client.execute('''{ hello (argument: "graph") }'''))

    def test_api_3(self):
        client = Client(graphene.Schema(query=Query))
        self.assert_match_snapshot(client.execute('''{ hello (argument: "world") }'''))
