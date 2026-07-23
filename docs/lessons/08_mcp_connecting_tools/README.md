# Chapter 8: MCP — Give Your Agent Hands

Until now, your agent's world has ended at the edge of the project folder. MCP — the Model Context Protocol — is how that changes: an open standard that connects agents to *everything else*. Databases. Browsers. Design tools. Calendars. Your company's internal systems. Think USB-C for AI: one port, any device.

This chapter demystifies the protocol, gets your first servers connected, teaches the CLI alternative that pros often prefer, and — most importantly — builds your security judgment, because giving an agent hands means deciding what those hands may touch.

!!! abstract "What you will learn"
    - Explain why tools transform what agents can do, and what MCP standardizes.
    - Understand MCP's moving parts in plain language: servers, tools, resources.
    - Connect and use real MCP servers in Claude Code.
    - Use CLIs as agent tools — the underrated alternative that's often better.
    - Draw trust boundaries: which connections are safe, which need guardrails, which to refuse.

!!! success "Builder principle"
    Every connection you give an agent is capability *and* attack surface. The pros aren't the ones with the most connections — they're the ones who can defend the ones they chose.

!!! example "Watch and read with this chapter"
    - [MCP, Clearly Explained](https://www.youtube.com/watch?v=e3MX7HoGXug) — the quick conceptual version.
    - [Claude's Model Context Protocol — let's test it](https://www.youtube.com/watch?v=HyzlYwjoXOQ) — Fireship's hands-on take, fast and irreverent.
    - [Anthropic Academy: Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) — free official course, the thorough companion.
    - [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro) — the standard itself; bookmark.

## Real talk

Connecting an agent to an actual system changes both its evidence and its risk. This chapter practices that decision with explicit capability, data, credential, and approval boundaries.

<!-- lesson-index:start -->

## Lessons in this chapter

- [8.1 Why Agents Need Hands](8.1_why_agents_need_hands.md)
- [8.2 MCP in Plain Language](8.2_mcp_in_plain_language.md)
- [8.3 Connecting Your First Server](8.3_connecting_your_first_server.md)
- [8.4 CLIs: The Other Kind of Hands](8.4_clis_the_other_kind_of_hands.md)
- [8.5 Trust Boundaries](8.5_trust_boundaries.md)

<!-- lesson-index:end -->

## Chapter checkpoint

Complete [Chapter 8: Least-privilege connection decision](../../course/assessment/chapter-checkpoints.md#chapter-8-least-privilege-connection-decision), save the evidence, then score your first attempt with the shared rubric.
