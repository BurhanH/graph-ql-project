# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['APITestCase::test_api_1 1'] = {
    'data': {
        'hello': 'Hello stranger'
    }
}

snapshots['APITestCase::test_api_2 1'] = {
    'data': {
        'hello': 'Hello graph'
    }
}

snapshots['APITestCase::test_api_3 1'] = {
    'data': {
        'hello': 'Hello world'
    }
}
