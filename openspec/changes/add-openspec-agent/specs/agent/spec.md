## ADDED Requirements

### Requirement: OpenSpec Agent Scaffolding
The project SHALL provide a scaffolding capability (an "agent") that, given a valid change-id, generates a directory under `openspec/changes/<change-id>/` containing at minimum a `proposal.md`, `tasks.md`, and a `specs/<capability>/spec.md` file following OpenSpec formatting rules.

#### Scenario: Successful scaffold creation
- **WHEN** a developer runs the scaffolding tool with a valid, unused `change-id` (e.g., `add-openspec-agent`)
- **THEN** the tool creates `openspec/changes/<change-id>/proposal.md` with an initial Why/What/Impact section
- **AND** the tool creates `tasks.md` with the implementation checklist
- **AND** the tool creates `specs/<capability>/spec.md` with an `## ADDED Requirements` block and at least one `#### Scenario:`

#### Scenario: Validation passes for scaffold
- **WHEN** the scaffold is generated
- **THEN** running `openspec validate <change-id> --strict` produces no parsing errors
