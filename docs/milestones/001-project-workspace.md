# Milestone 1 — Project Workspace CLI

This milestone adds a minimal installable `pulse` CLI focused on the first BA onboarding workflow.

## Install

```bash
python -m pip install -e .
```

## Create a project

```bash
pulse project create "FPTPlay" --description "Streaming and sports platform"
```

The command creates two linked areas:

- `projects/fptplay/`: BA workspace, source documents, research, requirements, diagrams, deliverables, and working memory.
- `knowledge/projects/fptplay/`: normalized Markdown pages and RAG indexes used by the existing researcher/ITBA flow.

## Commands

```bash
pulse project create "FPTPlay"
pulse project list
pulse project info fptplay
pulse doctor
pulse validate
```

## Why two folders?

The project workspace stores work products and project memory. The knowledge folder stores normalized information intended for retrieval. This prevents raw files and temporary BA artifacts from being indexed accidentally while preserving compatibility with the existing `knowledge/projects` convention.
