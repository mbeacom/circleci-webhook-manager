"""Define the client related functions and classes."""
from __future__ import annotations

import os
from typing import Any

import httpx

from .models import CircleCIOrganization, CircleCIProject, CircleCIUser, CircleCIWebhook


class CircleCIWebhookManager:
    """Define the CircleCI webhook manager."""

    def __init__(
        self: CircleCIWebhookManager,
        token: str = "",  # nosec: B107
        **kwargs: dict[str, str],
    ) -> None:
        """Initialize the CircleCI webhook manager."""
        self.base_url: str = kwargs.get("base_url", "") or os.environ.get(  # type: ignore
            "CIRCLECI_BASE_URL",
            "https://circleci.com/api/v2",
        )
        self._token: str = token or os.environ.get("CIRCLECI_TOKEN", "")
        self._headers: dict[str, str] = {
            "Content-Type": "application/json",
            "User-Agent": "circleci-webhook-manager",
            "Circle-Token": self._token,
        }
        provided_headers: dict[str, str] = kwargs.get("headers", {})
        self.headers: dict[str, str] = {**self._headers, **provided_headers}
        self.session: httpx.Client = httpx.Client(headers=self.headers)
        self._user: CircleCIUser = self.get_user()
        self._collaborations: list[CircleCIOrganization] = self.get_collaborations()

    def __repr__(self: CircleCIWebhookManager) -> str:
        """Return the string representation of the CircleCI webhook manager."""
        _dict = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        _dict["headers"]["Circle-Token"] = f"***{_dict['headers']['Circle-Token'][-4:]}"
        return f"{self.__class__.__name__} - {_dict}"

    def get_project(self: CircleCIWebhookManager, project_slug: str) -> CircleCIProject:
        """Get the project for the given project slug."""
        response: httpx.Response = self.session.get(
            f"{self.base_url}/project/{project_slug}",
        )
        return CircleCIProject(**response.json())

    def list_webhooks(
        self: CircleCIWebhookManager,
        scope_id: str,
        scope_type: str = "project",
    ) -> list[CircleCIWebhook]:
        """List the webhooks for the given project."""
        response: httpx.Response = self.session.get(
            f"{self.base_url}/webhook",
            params={
                "scope-id": scope_id,
                "scope-type": scope_type,
            },
        )
        data: dict[str, Any] = response.json()
        return [CircleCIWebhook(**webhook) for webhook in data.get("items", [])]

    def get_webhook(self: CircleCIWebhookManager, webhook_id: str) -> CircleCIWebhook:
        """Get the webhook for the given project."""
        response: httpx.Response = self.session.get(
            f"{self.base_url}/webhook/{webhook_id}",
        )
        return CircleCIWebhook(**response.json())

    def get_collaborations(self: CircleCIWebhookManager) -> list[CircleCIOrganization]:
        """Get the collaborations for the current identity."""
        self.collaborations_response: httpx.Response = self.session.get(
            f"{self.base_url}/me/collaborations",
        )
        data: list[dict[str, str]] = self.collaborations_response.json()
        return [CircleCIOrganization(**organization) for organization in data]

    def get_user(self: CircleCIWebhookManager) -> CircleCIUser:
        """Get the user for the given token."""
        self.user_response: httpx.Response = self.session.get(
            f"{self.base_url}/me",
        )
        return CircleCIUser(**self.user_response.json())
