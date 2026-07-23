# Synthetic Dashboard Context

## Purpose

This dependency-free dashboard is a safe practice surface for reviewing agent
work with synthetic task data.

## Durable constraints

- Keep runtime assets local and preserve direct `index.html` opening.
- Add no packages, network requests, credentials, analytics, or real-person
  data.
- Preserve semantic table markup, keyboard operation, visible focus, and
  narrow-screen reflow.
- Inspect named paths and make the smallest change that satisfies an observable
  criterion.
- Stop when a requested action needs another production file or external
  system.

## Verification

- Machine evidence: `node starter/verify.js` when Node is available.
- Human evidence: content, combined filters, keyboard path, screen-reader
  labels/state/order, and 200 percent zoom/reflow.
- A prerecorded transcript must be labeled simulated.

## Data boundary

All practice records are public-classification synthetic data. Do not replace
them with customer, employee, health, financial, membership, credential, or
private account data.

## Unknowns

The static verifier does not prove browser compatibility, security of a future
deployment, or fitness for a real team's workflow.
