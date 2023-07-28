"""Define the pytest configuration for fixture reuse."""
from __future__ import annotations

import pytest
import typer


@pytest.fixture()
def app() -> typer.Typer:
    """Define the Typer CLI fixture."""
    return typer.Typer()


@pytest.fixture()
def org_data() -> dict[str, str]:
    """Define the organization data fixture."""
    return {
        "id": "12345abc-1234-5678-abcd-123abcdef123",
        "vcs_type": "github",
        "name": "mbeacom",
        "avatar_url": "https://avatars.githubusercontent.com/u/7315957?v=4",
        "slug": "mbeacom",
    }


@pytest.fixture()
def project_data() -> dict[str, str]:
    """Define the project data fixture."""
    return {
        "slug": "gh/CircleCI-Public/api-preview-docs",
        "name": "api-preview-docs",
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "organization_name": "CircleCI-Public",
        "organization_slug": "CircleCI-Public",
        "organization_id": "CircleCI-Public",
        "vcs_info": {
            "vcs_url": "https://github.com/CircleCI-Public/api-preview-docs",
            "provider": "Bitbucket",
            "default_branch": "master",
        },
    }


@pytest.fixture()
def user_data() -> dict[str, str]:
    """Define the user data fixture."""
    return {
        "id": "123abcde-1234-5678-abcd-123abcde1234",
        "login": "mbeacom",
        "name": "mbeacom",
    }


@pytest.fixture()
def webhook_data() -> dict[str, str]:
    """Define the webhook data fixture."""
    return {
        "url": "string",
        "verify_tls": True,
        "id": "123abcde-1234-5678-abcd-123abcde1234",
        "signing_secret": "super-secret-signing-key",
        "updated_at": "2023-07-27T17:29:27.042Z",
        "name": "string",
        "created_at": "2023-07-27T17:29:27.042Z",
        "scope": {
            "id": "123abcde-1234-5678-abcd-123abcde1234",
            "type": "project",
        },
        "events": [
            "workflow-completed",
        ],
    }
