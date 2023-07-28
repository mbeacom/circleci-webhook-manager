"""Test the client module."""
from __future__ import annotations

import httpx
import respx

from webhook_manager.client import CircleCIWebhookManager


@respx.mock(assert_all_called=True, assert_all_mocked=True, base_url="https://circleci.com/api/v2")
def test_client_default(
    respx_mock: respx.router.MockRouter,
    org_data: dict[str, str],
    user_data: dict[str, str],
    project_data: dict[str, str],
    webhook_data: dict[str, str],
) -> None:
    """Test the core client functionality."""
    respx_mock.get("/me").mock(return_value=httpx.Response(200, json=user_data))
    respx_mock.get("/me/collaborations").mock(return_value=httpx.Response(200, json=[org_data, org_data]))
    _client = CircleCIWebhookManager()

    assert _client
    assert _client.user_response.status_code == 200
    assert _client.collaborations_response.status_code == 200
    assert "***" in repr(_client)
    assert _client.__class__.__name__ in repr(_client)

    respx_mock.get(f"/project/{project_data['slug']}").mock(return_value=httpx.Response(200, json=project_data))
    assert _client.get_project(project_slug=project_data["slug"]).to_dict() == project_data

    respx_mock.get("/webhook", params={"scope-id": project_data["id"], "scope-type": "project"}).mock(
        return_value=httpx.Response(200, json={"items": [webhook_data]}),
    )
    webhooks = _client.list_webhooks(scope_id=project_data["id"], scope_type="project")
    assert len(webhooks) == 1
    assert webhooks[0].to_dict() == webhook_data

    respx_mock.get(f"/webhook/{webhook_data['id']}").mock(return_value=httpx.Response(200, json=webhook_data))
    assert _client.get_webhook(webhook_id=webhook_data["id"]).to_dict() == webhook_data


@respx.mock(assert_all_called=True, assert_all_mocked=True, base_url="https://noop.circleci.com/v9")
def test_client_kwargs(
    respx_mock: respx.router.MockRouter,
    org_data: dict[str, str],
    user_data: dict[str, str],
) -> None:
    """Test the core client functionality."""
    respx_mock.get("/me").mock(return_value=httpx.Response(200, json=user_data))
    respx_mock.get("/me/collaborations").mock(return_value=httpx.Response(200, json=[org_data, org_data]))
    _client = CircleCIWebhookManager(
        token="12345abcde",  # noqa: S106
        base_url="https://noop.circleci.com/v9",
        headers={"Custom-Header": "some-value"},
    )

    assert _client.user_response.status_code == 200
    assert _client.collaborations_response.status_code == 200

    assert _client
    assert _client.base_url == "https://noop.circleci.com/v9"
    assert _client.headers["Custom-Header"] == "some-value"
    assert _client.headers["Circle-Token"] == "12345abcde"  # noqa: S105
