from lyra_core.permissions import (
    PermissionLevel,
    PermissionManager,
    create_default_policy,
)


def test_unknown_actions_are_blocked():
    manager = PermissionManager()

    assert manager.evaluate("unknown_action") is PermissionLevel.BLOCKED
    assert manager.may_execute("unknown_action") is False


def test_safe_observation_is_allowed():
    manager = create_default_policy()

    assert manager.may_execute("observe_screen") is True


def test_sensitive_action_requires_confirmation():
    manager = create_default_policy()

    assert manager.may_execute("open_application") is False
    assert manager.may_execute(
        "open_application",
        user_confirmed=True,
    ) is True


def test_blocked_actions_cannot_be_confirmed():
    manager = create_default_policy()

    assert manager.may_execute(
        "unrestricted_terminal",
        user_confirmed=True,
    ) is False

    assert manager.may_execute(
        "self_modify",
        user_confirmed=True,
    ) is False

    assert manager.may_execute(
        "create_tools",
        user_confirmed=True,
    ) is False
