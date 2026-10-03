# Lyra AI

Lyra is an open-source local AI assistant focused on safe desktop automation, explicit user control, screen awareness, and modular tools.

The project explores how a capable desktop AI agent can remain useful and autonomous in conversation while keeping consequential computer actions under explicit user control.

## Core principles

- Free and natural conversation
- Permission-based desktop actions
- Explicit confirmation for sensitive operations
- Screen observation and contextual awareness
- Modular tools and components
- Local-first architecture
- Clear separation between reasoning and execution

## Safety model

Lyra distinguishes between what the assistant can discuss and what it is allowed to execute.

Sensitive actions can require explicit user confirmation before execution. High-risk capabilities such as unrestricted terminal access, self-modification, autonomous tool creation, and system-level configuration can be disabled entirely.

This approach is intended to make desktop AI agents more transparent, predictable, and controllable.

## Planned public components

- Core assistant architecture
- Permission and confirmation system
- Screen observation / Guardian
- Routine recording and playback
- Safe desktop tools
- Configuration system
- Documentation and tests

## Technology

Lyra is primarily developed in Python and designed for Windows desktop environments.

Technologies used or evaluated include:

- Python
- PyQt
- Local and remote language models
- Windows APIs
- Screen and application context
- Modular tool execution

## Project status

Lyra is under active development.

This public repository is being prepared as a clean open-source edition of the project, with a focus on security, reproducibility, documentation, and safe desktop-agent architecture.

## Maintainer

Maintained by Vladimir Alberto Fain.

Contributions, testing, documentation improvements, and technical discussion are welcome.
