import graphene

from snapshottest import TestCase
from graphene.test import Client

from queries import Query


class APITestCase(TestCase):
    def _test(self, schema_name, argument=''):
        client = Client(graphene.Schema(query=Query))
        if argument is not '':
            line = schema_name + ' (argument: "{0}")'.format(argument)
        else:
            line = schema_name
        self.assert_match_snapshot(client.execute('''{ ''' + line + ''' }'''))

    def test_api_1(self):
        self._test('hello')

    def test_api_2(self):
        self._test('hello', 'graph')

    def test_api_3(self):
        self._test('hello', 'world')
