## 1. Implementation

- [ ] 1.1 Create scaffolding script: `scripts/openspec-agent-scaffold.(ps1|js|py)` (choose language)
- [ ] 1.2 Create template files for `proposal.md`, `tasks.md`, and `specs/<capability>/spec.md`
- [ ] 1.3 Wire a CI job to run `openspec validate <change-id> --strict` on generated changes
- [ ] 1.4 Add unit tests for template generation and validation

## 2. Documentation

- [ ] 2.1 Document usage in `openspec/project.md` and `README.md`

## 3. Acceptance

- [ ] 3.1 CLI or script can create a new `openspec/changes/<change-id>` with the expected files
- [ ] 3.2 `openspec validate <change-id> --strict` runs with no parsing errors for the scaffolded change
- [ ] 3.3 Templates follow scenario formatting (use `#### Scenario:` headers)
