"""Define the models for the webhook manager package."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class BaseModel:
    """Define the base model for the webhook manager package."""

    id: str  # noqa: A003

    def __str__(self: BaseModel) -> str:
        """Return the string representation of the base model."""
        return f"{self.__class__.__name__}"

    def to_dict(self: BaseModel) -> dict[str, Any]:
        """Return the dictionary representation of this object."""
        return self.__dict__


@dataclass
class CircleCIProject(BaseModel):
    """Define the CircleCI Project model.

    Sample:
        {
            "slug": "gh/CircleCI-Public/api-preview-docs",
            "name": "api-preview-docs",
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "organization_name": "CircleCI-Public",
            "organization_slug": "CircleCI-Public",
            "organization_id": "CircleCI-Public",
            "vcs_info": {
                "vcs_url": "https://github.com/CircleCI-Public/api-preview-docs",
                "provider": "Bitbucket",
                "default_branch": "master"
            }
        }

    """

    slug: str
    name: str
    organization_name: str
    organization_slug: str
    organization_id: str
    vcs_info: dict[str, str]


@dataclass
class CircleCIWebhook(BaseModel):
    """Define the CircleCI Webhook model.

    Sample:
        {
            "url": "string",
            "verify-tls": true,
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "signing-secret": "string",
            "updated-at": "2015-09-21T17:29:21.042Z",
            "name": "string",
            "created-at": "2015-09-21T17:29:21.042Z",
            "scope": {
                "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                "type": "string",
            },
            "events": [
                "workflow-completed",
            ],
        }

    """

    url: str
    verify_tls: bool
    signing_secret: str
    updated_at: str
    name: str
    created_at: str
    scope: dict[str, str]
    events: list[str]


@dataclass
class CircleCIUser(BaseModel):
    """Define the CircleCI User model.

    Sample:
        {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "login": "string",
            "name": "string"
        }

    """

    login: str
    name: str


@dataclass
class CircleCIOrganization(BaseModel):
    """Define the CircleCI Organization model.

    Sample:
        {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "vcs-type": "string",
            "name": "string",
            "avatar_url": "string",
            "slug": "string",
        }

    """

    vcs_type: str
    name: str
    avatar_url: str
    slug: str
