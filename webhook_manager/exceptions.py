"""Define the exceptions for the webhook manager package."""
from __future__ import annotations


class CircleCIWebhookManagerError(Exception):
    """Define the base exception for the webhook manager package."""

    def __init__(self: CircleCIWebhookManagerError, message: str) -> None:
        """Initialize the base exception."""
        super().__init__(message)
