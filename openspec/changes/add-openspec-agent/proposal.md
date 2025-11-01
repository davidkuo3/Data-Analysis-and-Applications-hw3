## Why

The project can benefit from a repeatable, auditable scaffolding for automations (agents) that perform routine OpenSpec tasks: creating change scaffolds, running validations, and optionally opening skeleton PRs. This reduces manual errors and improves consistency for proposals.

## What Changes

- Add a new capability: OpenSpec Agent Scaffolding.
- Provide a standardized scaffold that creates `proposal.md`, `tasks.md`, and minimal `specs/` delta files for a given change id.
- Provide an acceptance-check that runs `openspec validate <change-id> --strict` and reports parsing issues.

**Change id:** `add-openspec-agent`

## Impact

- Affected specs: `agent` capability (new)
- Affected files: new directory `openspec/changes/add-openspec-agent/` with `proposal.md`, `tasks.md`, `specs/agent/spec.md`
- Implementation deliverables: CLI helper script or makefile target (optional), tests for skeleton generation, CI step to run `openspec validate` for new changes

## Migration

- No migration required for existing capabilities. This is additive tooling to help authors create proposals correctly.

## Non-goals

- Full automation of code changes or merging PRs is out of scope for the initial proposal. The initial scoped feature provides scaffolding, validation, and minimal guidance only.
