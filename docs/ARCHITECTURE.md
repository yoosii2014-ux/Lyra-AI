# Lyra AI — Architecture

## Overview

Lyra is a local desktop AI assistant designed around a simple principle:

**Conversation can remain flexible, while consequential computer actions remain controlled.**

The project separates reasoning and conversation from the execution of desktop actions.

## High-level architecture

```text
User
  |
  v
Lyra Interface
  |
  v
AI / Reasoning Layer
  |
  v
Permission & Safety Layer
  |
  +---- Screen Observation / Guardian
  |
  +---- Routine System
  |
  +---- Safe Tool Registry
  |
  v
Approved Desktop Actions
