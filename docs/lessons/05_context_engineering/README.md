# Chapter 5: Context Engineering

The same model can behave differently when its instructions, evidence, examples, and constraints change. Context engineering deliberately designs that task packet, while model capability, tools, and verification remain separate factors.

You'll build a CLAUDE.md that turns your agent from tourist to teammate, layer memory so nothing gets re-explained twice, grow a second brain your agent can read, and manage sessions so quality doesn't sag as work gets long. The reference points here are the same ones the top engineering teams use — translated for both lanes.

!!! abstract "What you will learn"
    - Explain why context quality dominates model quality in real-world results.
    - Write and iterate a CLAUDE.md that measurably changes agent behavior.
    - Use the memory layers: session context, project memory, user memory.
    - Build a second brain — decisions, style, research — that agents consult.
    - Keep long sessions sharp with scoping, `/clear`, and compaction awareness.
    - Scale all of it to large, messy, real codebases.

!!! success "Builder principle"
    Your agent is exactly as good as what it can see. Feed it like a teammate, not like a search box.

!!! example "Watch with this chapter"
    - [Mastering Claude Code in 30 Minutes](https://www.youtube.com/watch?v=B_KAEqiC-0Q) — the CLAUDE.md and memory segments especially.
    - [Claude Code docs: memory & CLAUDE.md](https://code.claude.com/docs/en/overview) — the living reference; bookmark it.

## Real talk

In Lesson 4.5's retro you wrote down what your agent needed but did not have. Repeated missing context creates repeated clarification and rework. This chapter shows how to reduce that cost and measure whether the change helps.

<!-- lesson-index:start -->

## Lessons in this chapter

- [5.1 Context Is the Product](5.1_context_is_the_product.md)
- [5.2 CLAUDE.md: Your Project's Brain](5.2_claude_md_your_projects_brain.md)
- [5.3 The Memory Layers](5.3_the_memory_layers.md)
- [5.4 Building a Second Brain](5.4_building_a_second_brain.md)
- [5.5 Managing Long Sessions](5.5_managing_long_sessions.md)
- [5.6 Context at Scale: Big Codebases](5.6_context_at_scale_big_codebases.md)

<!-- lesson-index:end -->

## Chapter checkpoint

Complete [Chapter 5: Context experiment](../../course/assessment/chapter-checkpoints.md#chapter-5-context-experiment), save the evidence, then score your first attempt with the shared rubric.
