# Chapter 2: How AI Actually Works (No PhD Required)

You can drive a car without building an engine — but you can't drive *well* without knowing what the pedals actually do. This chapter is the pedals: what a large language model really is, what tokens and context windows mean for your daily work, why models make things up, and how to choose your tools. No math. No code. Just the mental models that make everything after this chapter click.

Engineers: don't skip this one on principle. The lessons connect model mechanics directly to agentic practice — context budgets, verification design, model selection — and Chapter 5 assumes them.

!!! abstract "What you will learn"
    - Explain what an LLM is and how it produces answers, in your own words.
    - Use tokens and context windows as practical planning tools, not trivia.
    - Move from prompting to delegating — the shift that unlocks agents.
    - Predict where models are strong, where they're weak, and why they hallucinate.
    - Choose a model and a tool for a given job with a straight face.

!!! success "Builder principle"
    Practical model knowledge helps you predict failure and choose proportionate checks.

!!! example "Watch with this chapter"
    - [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) — 3Blue1Brown (8 min). Watch before Lesson 2.1.
    - [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — Andrej Karpathy (3.5 hr). The complete picture, for when you want it all.
    - [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) — Andrej Karpathy (2 hr). Practical daily usage from one of the field's founders; pairs with Lesson 2.5.

## Real talk

Similar requests can produce different-quality results because context, model behavior, tools, and verification differ. This chapter gives you a vocabulary for investigating those differences rather than treating them as luck.

<!-- lesson-index:start -->

## Lessons in this chapter

- [2.1 LLMs in Plain Language](2.1_llms_in_plain_language.md)
- [2.2 Tokens, Context Windows, and Memory](2.2_tokens_context_windows_and_memory.md)
- [2.3 From Prompting to Delegating](2.3_from_prompting_to_delegating.md)
- [2.4 Strengths, Limits, and Hallucination](2.4_strengths_limits_and_hallucination.md)
- [2.5 Choosing Your Tools](2.5_choosing_your_tools.md)

<!-- lesson-index:end -->

## Chapter checkpoint

Complete [Chapter 2: Predict the failure](../../course/assessment/chapter-checkpoints.md#chapter-2-predict-the-failure), save the evidence, then score your first attempt with the shared rubric.
