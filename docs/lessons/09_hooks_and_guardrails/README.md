# Chapter 9: Hooks and Guardrails

Everything you've built so far has one dependency you haven't addressed: *you remembering things*. Verify before committing. Run the wrap routine. Keep the agent off the no-touch files. You've been the enforcement mechanism — and humans are wonderful, inconsistent enforcement mechanisms.

This chapter removes the dependency. **Hooks** run your checks automatically at the seams of every session; **validation harnesses** give the agent a truth-teller to test itself against; **permission policy** turns your judgment into configuration. The result is the thing the premium cohorts call "agentic validation" and what it really is: quality that doesn't require anyone to remember.

!!! abstract "What you will learn"
    - Explain why guardrails-as-mechanism beat guardrails-as-discipline.
    - Configure hooks that fire at session events: after edits, before commands, at session end.
    - Build a validation harness — tests, checks, formatters — that lets the agent self-correct.
    - Codify permissions: allowlists, deny rules, and the policies from Chapter 8 as settings.

!!! success "Builder principle"
    Discipline is what you do when you remember. Mechanism is what happens either way. Ship on mechanism.

!!! example "Read with this chapter"
    - [Claude Code docs — hooks and settings](https://code.claude.com/docs/en/overview) — the current syntax reference; hooks are config, and config docs age fast, so always check the source.

## Real talk

Ask anyone who ships software for a living where quality actually comes from. It's never "we're careful." It's the boring machinery: the test that blocks the merge, the check that runs every time, the permission nobody can fat-finger past. Careful is a mood. Machinery is a decision — made once, paying forever. This chapter is you making it.

<!-- lesson-index:start -->

## Lessons in this chapter

- [9.1 Quality by Mechanism](9.1_quality_by_mechanism.md)
- [9.2 Hooks: Automation at the Seams](9.2_hooks_automation_at_the_seams.md)
- [9.3 The Validation Harness](9.3_the_validation_harness.md)
- [9.4 Permission Policy](9.4_permission_policy.md)

<!-- lesson-index:end -->

## Chapter checkpoint

Complete [Chapter 9: Guardrail that proves itself](../../course/assessment/chapter-checkpoints.md#chapter-9-guardrail-that-proves-itself), save the evidence, then score your first attempt with the shared rubric.
