"""Test the models module."""
from __future__ import annotations

from typing import Any

from webhook_manager.models import CircleCIOrganization, CircleCIProject, CircleCIUser, CircleCIWebhook


def test_organization(org_data: dict[str, str]) -> None:
    """Test the organization model."""
    circleci_organization = CircleCIOrganization(**org_data)
    circleci_org_dict: dict[str, Any] = circleci_organization.to_dict()
    assert circleci_org_dict
    assert isinstance(circleci_org_dict, dict)
    assert circleci_organization.name == circleci_organization.slug
    assert str(circleci_organization) == "CircleCIOrganization"
    assert circleci_organization.id == circleci_org_dict["id"]


def test_project(project_data: dict[str, str]) -> None:
    """Test the project model."""
    circleci_project = CircleCIProject(**project_data)
    circleci_project_dict: dict[str, Any] = circleci_project.to_dict()
    assert circleci_project_dict
    assert isinstance(circleci_project_dict, dict)
    assert circleci_project.id == circleci_project_dict["id"]


def test_user(user_data: dict[str, str]) -> None:
    """Test the user model."""
    circleci_user = CircleCIUser(**user_data)
    circleci_user_dict: dict[str, Any] = circleci_user.to_dict()
    assert circleci_user_dict
    assert isinstance(circleci_user_dict, dict)


def test_webhook(webhook_data: dict[str, str]) -> None:
    """Test the webhook model."""
    circleci_webhook = CircleCIWebhook(**webhook_data)
    circleci_webhook_dict: dict[str, Any] = circleci_webhook.to_dict()
    assert circleci_webhook_dict
    assert isinstance(circleci_webhook_dict, dict)
