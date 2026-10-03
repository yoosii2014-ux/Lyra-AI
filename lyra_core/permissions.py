from enum import Enum
from dataclasses import dataclass


class PermissionLevel(Enum):
    ALLOWED = "allowed"
    CONFIRMATION_REQUIRED = "confirmation_required"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class ActionPolicy:
    name: str
    permission: PermissionLevel
    description: str = ""


class PermissionManager:
    """
    Minimal permission layer for Lyra AI.

    Reasoning and tool selection do not automatically authorize execution.
    Every exposed action is evaluated against an explicit policy.
    """

    def __init__(self):
        self._policies: dict[str, ActionPolicy] = {}

    def register(
        self,
        action: str,
        permission: PermissionLevel,
        description: str = "",
    ) -> None:
        if not action:
            raise ValueError("Action name cannot be empty.")

        self._policies[action] = ActionPolicy(
            name=action,
            permission=permission,
            description=description,
        )

    def get_policy(self, action: str) -> ActionPolicy | None:
        return self._policies.get(action)

    def evaluate(self, action: str) -> PermissionLevel:
        """
        Unknown actions are blocked by default.
        """
        policy = self.get_policy(action)

        if policy is None:
            return PermissionLevel.BLOCKED

        return policy.permission

    def may_execute(
        self,
        action: str,
        *,
        user_confirmed: bool = False,
    ) -> bool:
        permission = self.evaluate(action)

        if permission is PermissionLevel.ALLOWED:
            return True

        if permission is PermissionLevel.CONFIRMATION_REQUIRED:
            return user_confirmed

        return False


def create_default_policy() -> PermissionManager:
    manager = PermissionManager()

    # Observation can operate without granting control.
    manager.register(
        "observe_screen",
        PermissionLevel.ALLOWED,
        "Read-only screen observation.",
    )

    # Consequential desktop actions require explicit approval.
    manager.register(
        "open_application",
        PermissionLevel.CONFIRMATION_REQUIRED,
        "Open an application on the user's computer.",
    )

    manager.register(
        "control_volume",
        PermissionLevel.CONFIRMATION_REQUIRED,
        "Change system audio volume.",
    )

    # High-risk capabilities remain unavailable.
    manager.register(
        "unrestricted_terminal",
        PermissionLevel.BLOCKED,
        "Unrestricted shell access is disabled.",
    )

    manager.register(
        "self_modify",
        PermissionLevel.BLOCKED,
        "The assistant may not modify its own code.",
    )

    manager.register(
        "create_tools",
        PermissionLevel.BLOCKED,
        "Autonomous creation of executable tools is disabled.",
    )

    return manager
