from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/api')
    assert resp.status_code == 200
