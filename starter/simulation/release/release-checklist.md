# Synthetic Release Checklist

## Review surface

- [ ] Private repository or authenticated preview
- [ ] Recorded walkthrough with synthetic data
- [ ] Public URL after an explicit publication decision
- [ ] Simulation journal when no execution access exists

Select one. A public URL is not universally required.

## Evidence

- [ ] Brief and observable acceptance criteria
- [ ] Data authorization and classification
- [ ] Named diff with no unexplained paths
- [ ] Machine evidence labeled live, delegated, or simulated
- [ ] Human acceptance evidence, or an explicit unproven item
- [ ] Accessibility and privacy review
- [ ] Mechanisms marked used, simulated, or declined with reason

## Recovery boundaries

- Repository content: restore or revert only reviewed tracked paths/commits.
- Untracked or ignored files: preserve separately before cleanup.
- Service configuration: use the service's preview, version, and rollback
  controls.
- Data writes: use tested backup/restore or compensating operations.
- Credentials: revoke and rotate through the provider.
- Messages or publications: use correction, retraction, or follow-up; Git
  cannot unsend them.

## Disclosure

```text
This submission uses synthetic task data. Evidence labeled simulated came from
the course fixture and was reviewed, not executed, by the learner. No live
agent, MCP server, hook, agent team, or deployment was operated. The remaining
unproven items are listed with the submission.
```

Before a real launch, recheck current product behavior, provider terms, prices,
data handling, authentication, and rollback documentation at decision time.
