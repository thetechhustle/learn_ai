# Simulated Formative Pilot Report

## Disclosure and disposition

This is a **simulated pilot**, not human-subject research and not a claim that
seven real learners completed the course. One evaluator traced seven distinct
learner personas through the course at commit
`2bfc7531b2b5574a67447304bc1ed4ad4fecfd5f` on branch
`agent/full-curriculum` on 2026-07-23.

The evaluator ran offline commands and manipulated only disposable copies under
`/private/tmp`. No real credentials, paid accounts, live external systems, or
confidential data were used. The repository was not changed during testing.

**Pilot disposition: revise before a real beginner/accessibility pilot.** The
course has a strong deterministic starter, coherent safety material in its
later chapters, and a complete assessment skeleton. Two missing on-ramps,
however, prevent intended learners from completing the journey as written.

Severity totals:

| Blocker | High | Medium | Low | Total |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 4 | 7 | 2 | 15 |

Evidence labels used below:

- **M — mechanical evidence:** observed in files, rendered output, or command
  execution.
- **I — persona inference:** a predicted learner outcome based on the stated
  persona. It should be tested with real learners before being generalized.

## Scope and method

The simulated journey covered:

1. Course home, overview, entry diagnostic, and competency interpretation.
2. Setup, platform commands, and access requirements.
3. Starter acquisition, clean baseline, no-code edit, expected failure, fix,
   and human/machine verification expectations.
4. At least two chapter checkpoints per persona.
5. Answer-key use, rubric scoring, recovery, exit diagnostic, and capstone
   handoff.
6. Build/navigation, local links and fragments, accessibility alternatives,
   workload, product claims, privacy boundaries, and the current-course audit.

Offline executions:

| Task | Observed result |
| --- | --- |
| `make build` | Strict MkDocs build passed; 81 HTML pages were produced. |
| `make audit-test` | `Course audit self-test: PASS`. |
| `make audit` | Passed static rules and date/anchor checks for five external-fact records; 84 files scanned. |
| `node starter/verify.js` | Clean repository starter passed all 8 checks. |
| Disposable no-code edit | Assigning `T-104` to `You` failed exactly the summary check: expected `unassignedOpen: 1`, received `0`; exit 1. |
| Disposable expected-output fix | Changing `unassignedOpen` to `0` restored all 8 passes. |
| Disposable broken starter | Removing one JSON quote produced the useful parse error first, then three dependent cascade failures; exit 1. |
| Disposable file recovery | Restoring the known-good `index.html` restored all 8 passes. |
| Disposable Git recovery | A fresh repository exposed one seeded `styles.css` diff; documented path-specific `git restore --worktree starter/styles.css` returned the tree to clean and all 8 checks passed. |
| Built-site local-link check | 4,669 local links/fragments checked across 81 pages; 0 missing targets or fragments. |
| Static accessibility inventory | 0 images missing `alt`; 54 lesson pages had a rendered H1-to-H3 heading jump and duplicate lesson title. |
| Assessment count check | 8 competency anchors, 8 entry situations, 8 exit situations, 11 checkpoint chapters, 11 answer-pattern sections, and 7 capstone rubric dimensions were present. |
| Workload inventory | 54 lesson files, approximately 47,244 words, 49 `Try it now` sections, and 11 chapter checkpoints. |

## Findings

Findings are ordered by severity. Each row records the attempted task, evidence,
confusion or blocker, assistance not supplied by the course, affected personas,
and a precise correction.

| ID | Severity | Task attempted and observed evidence | Blocker or confusion | Undocumented assistance needed | Affected personas | Precise recommended correction |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | **Blocker** | **M:** The overview sends learners from Setup directly to the Starter Project (`course/overview.md:61-63`). Setup creates `~/builds` but never clones or downloads the course (`course/setup.md:116-140`). Starter then assumes `starter/` exists and that the learner is at the repository root (`course/starter-project.md:3-8,29-31`). A search of learner-facing `docs/` found no `git clone` or Download ZIP step. | A web-first learner cannot locate or run the bundled starter. The first common practice surface is unreachable as written. | A helper must explain how to clone/download the repository, where it landed, how to enter its root, and how to open the starter. | 1, 2, 3, 4, 6, 7 | Add a required “Get the course files” setup step with both Git and no-Git downloads, Mac/PowerShell commands, a repository-root check, and exact browser/editor open steps. Link it immediately before the starter baseline. |
| F02 | **Blocker** | **M:** Overview requires a computer the learner controls and an eligible paid/API-backed Claude account (`course/overview.md:28-32`). Setup tells a learner with blocked installs to use a personal machine (`course/setup.md:142-146`). Assessment policy says to use “the documented simulation option” when an install, account, payment method, or service is unavailable (`assessment/README.md:30-38`), but only checkpoint-level simulations are documented (`chapter-checkpoints.md:14,65,184`); core lessons 3.4 and 5-10 still require a running agent/product. | The locked-down/no-paid learner can submit some checkpoint simulations but cannot follow the instructional path that is supposed to teach the skills. “Use a personal machine” is not an available recovery for the defined persona. | A facilitator would need to invent transcripts, screenshots, permission prompts, diffs, tool manifests, and mock agent sessions. | 6; also learners in 1, 2, 3, 4 without paid access | Publish a complete no-install/no-paid simulation lane: downloadable starter and fixtures, narrated agent transcripts, permission and failure decisions, before/after files, mock MCP/hook/team artifacts, and scoring instructions. Otherwise narrow the audience claim and remove the promise of a documented alternative. |
| F03 | **High** | **M:** Setup calls native PowerShell the simpler supported Windows start (`course/setup.md:19,31,145`), but later learner commands assume Unix: `mkdir -p` (`setup.md:121`; `3.2_files_folders_and_paths.md:92`), `cd ... && cat ...` (`3.2...:99`), and a chained Git exercise with `&&` (`3.3_git_your_safety_net.md:137`). The file-opening examples cover Mac and WSL, not native PowerShell (`3.4_your_first_claude_code_session.md:56-61`). No `pwsh` runtime was available in this pilot, so the incompatibility review is static. | A Windows-native PowerShell learner is told the lane is supported and then receives commands written for Bash. Windows PowerShell 5.1 in particular does not support `&&`, and `mkdir -p` is not the documented PowerShell form. | A helper must translate commands or redirect the learner to Git Bash/WSL, changing the promised platform path. | 2, 6 | Add OS-tabbed command blocks throughout Setup and Chapter 3. Use PowerShell-native `New-Item -ItemType Directory -Force`, `Get-Content`, `Set-Location`, `;` or separate commands, and `Invoke-Item .\index.html`. If Bash is required after setup, state that requirement instead of claiming a native path. |
| F04 | **High** | **M:** Chapter 3 says the project folder becomes the agent’s “whole world” and that one project per folder gives a “defined sandbox, nowhere near your tax documents” (`3.2_files_folders_and_paths.md:61-78`). The glossary says Git tracks “every change” and learners can “always roll back” (`course/glossary.md:35`). These absolutes contradict the more accurate boundaries in Setup (`setup.md:125`), Chapter 3.3 (`3.3_git_your_safety_net.md:20-27`), and the answer key (`assessment/answer-key.md:38-47`). | Beginners may infer that current directory and Git alone prevent out-of-workspace access or recover all changes. That is unsafe when agents can run commands, access untracked files, or affect remote systems. | A reviewer must correct the mental model before the learner approves consequential actions. | 1, 2, 3, 4, 6, 7 | Replace “sandbox/whole world/always” with a single consistent model: the folder is the intended workspace, not an OS boundary; Git records committed tracked content; permissions, sandboxing, backups, scoped credentials, and service recovery cover other effects. Correct the glossary and Chapter 3 before the first live agent session. |
| F05 | **High** | **M:** The capstone permits justified declines, private/authenticated delivery, synthetic demonstrations, and recorded walkthroughs (`course/capstone.md:34-44,81-85`). The immediate Chapter 11 handoff instead requires “Vision brief to live URL, full harness engaged,” a ready `project-init` Skill, a 30-day revenue goal, and sharing a capstone URL (`11.5_staying_current_finishing_strong.md:31-40,50-52`). | Learners reach the exit with two incompatible definitions of required work. The stricter lesson path disadvantages no-code, locked-down, noncommercial, and confidential projects and can pressure unsafe public sharing. | A facilitator must tell the learner which document governs and waive lesson-only requirements. | 1, 3, 4, 6, 7 | Make Chapter 11.5 quote the capstone contract: reviewable public **or private** surface; context/tool/guardrail/team mechanisms used or explicitly declined; optional commercial goal; sanitized sharing only. Remove `project-init`, revenue, live URL, and public sharing as universal preflight gates. |
| F06 | **High** | **M:** The course requires learners to distinguish observed, sourced, assumed, and unknown claims (`chapter-checkpoints.md:29-37`) and prohibits guaranteed economic/career claims (`chapter-checkpoints.md:259-265`). Its own instructional prose includes uncited named success anecdotes (`01_the_shift/README.md:21-25`), unsupported market claims (`1.3_the_rise_of_agentic_engineering.md:40-49`), “most people” saving 2-4 hours weekly (`6.5_your_first_true_automation.md:69`), and claims that local freelance work is the “fastest money,” every listed business needs it, and engineer advancement “writes itself” (`11.4_getting_paid_freelance_products_career.md:13-16,30-36,57-59`). | The modeled standard contradicts the assessed standard. Learners may treat persuasive anecdotes as evidence when making time, career, or pricing decisions. | A learner or reviewer must independently source or discount claims the course presents as fact. | All, especially 1, 4, 6 | Give every material market, price, productivity, and career claim a source and date, or recast it explicitly as an illustration/hypothesis to validate locally. Apply the course’s claim-ledger labels to its own opening stories and Chapter 11 advice. |
| F07 | **Medium** | **M:** All 54 lesson source files begin with `###`. MkDocs generated a filename-derived H1, followed by a duplicate H3 lesson title and then H2 sections; the static rendered check found 54 H1-to-H3 jumps. Example: `3.1_meet_the_terminal.md:1` renders H1 “3.1 meet the terminal,” H3 “3.1 Meet the Terminal,” then H2. | Screen-reader heading navigation receives a duplicate, out-of-order structure on every lesson page. Visual users also get a title whose hierarchy does not match the following sections. | A screen-reader learner must infer the page structure and ignore one duplicate title. | 3; secondarily all | Change each lesson’s first heading to one H1 and keep subsections at H2/H3. Add a build-time heading-order check so duplicate auto-titles and skipped levels fail CI. |
| F08 | **Medium** | **M:** Assessment and starter accommodations are strong (`assessment/README.md:30-38`; `starter-project.md:96-116`), but the main lesson path repeatedly frames verification as “with your own eyes,” watching scrolling operations, clicking every link, narrowing a window, and judging visual similarity (`overview.md:5-11`; `3.4_your_first_claude_code_session.md:65-93`; `4.4_verification_never_trust_always_check.md:45-57`; `5.1_context_is_the_product.md:42`). | The course supplies an accessible starter alternative but no equivalent nonvisual human-acceptance recipe for the recurring Builder Loop. “Text readable without zooming” is also not a sufficient low-vision acceptance criterion. | A low-vision learner must design their own screen-reader, keyboard, zoom/reflow, and nonvisual evidence pass. | 3 | Add a reusable human-acceptance matrix beside Chapter 4’s five-step pass: keyboard-only main/failure paths, screen-reader names/state/order, 200% zoom and reflow, contrast/non-color cues, and delegated visual review recorded as such. Refer back to it everywhere “own eyes” appears. |
| F09 | **Medium** | **M:** The entry diagnostic intentionally precedes instruction but uses terms such as MCP server, broad token, data minimization, provenance, recourse, monitoring, and provider handling (`diagnostic.md:51-67`). Exit adds regression, schema, prompt injection, revocation, and roll-forward (`diagnostic.md:113-147`). The glossary does not define `artifact`, `rubric`, `provenance`, `recourse`, `revocation`, `least privilege`, `prompt injection`, `fixture`, `regression`, `schema`, `sandbox`, or `roll-forward`. Language support is allowed (`assessment/README.md:32-35`), but no neutral term sheet is supplied. | The diagnostic can measure English technical vocabulary and prior industry exposure in addition to the intended judgment. A low score may not identify the competency gap accurately. | Translation or facilitator explanation is needed before the learner can demonstrate independent judgment. | 1, 3, 4, 6, 7 | Add a plain-language, non-answer-bearing diagnostic term sheet and define all recurring assessment terms in the glossary. Permit translated prompts and require scorers to ignore language polish. Pilot the wording with additional-language learners before norming any score interpretation. |
| F10 | **Medium** | **M:** The course contains about 47,244 lesson words, 49 hands-on sections, 11 checkpoints, two 45-90 minute diagnostics, and an 8-20+ hour capstone. Overview separately estimates 35-55 hours for reading, labs as additional, and 8-20+ hours for capstone (`course/overview.md:34-44`). The no-code learner is told to read every lesson, do every exercise, and watch linked videos, while the schedule says 3-4 hours/week finishes in about 12 weeks (`1.5_how_to_run_this_course.md:29-51`). Even the stated lower bounds for reading, checkpoints, diagnostics, setup, and capstone exceed 50 hours before lesson labs and videos. | “Finish the course” has no consistent workload definition. The beginner plan understates the required full-practice path and makes normal pacing look like learner failure. | A learner must invent an essential/optional scope or extend the schedule without guidance. | 1, 2, 3, 4, 6, 7 | Publish three totals: reading-only, assessed practice path, and assessed path plus capstone. Mark videos and repeated builds essential or optional, add pause points, and provide a minimum viable route for time-constrained learners. Recalculate the 5/6/12-week schedules from those totals. |
| F11 | **Medium** | **M:** The overview correctly says to attempt the diagnostic/checkpoint before opening the key (`overview.md:61-65`), but the answer key is permanently visible in the main Assessment navigation and entry instructions link directly to its diagnostic patterns (`diagnostic.md:11-17`). No separation, printable first-attempt form, or completion interstitial exists. | A learner can accidentally preview the answer patterns while navigating or deliberately optimize the entry baseline against them. The paired measure then reflects answer exposure, not only growth. | A facilitator must distribute or bookmark an answer-key-free form and control the reveal. | All; greatest validity effect for 1, 4, 6 | Create answer-key-free entry/checkpoint pages or printables and route first attempts there. Put reference patterns behind a clear “finish and save first” interstitial or separate reviewer section. Ask the learner to record whether the key was viewed before the attempt. |
| F12 | **Medium** | **M:** Later trust-boundary and capstone guidance is appropriately strict (`8.5_trust_boundaries.md:39-47`; `course/capstone.md:9-16`). Earlier context/workflow lessons tell learners to store meeting notes and research in an agent-readable second brain (`5.4_building_a_second_brain.md:1-17`) and to use three real writing samples, pasted notes, job-search or community-organizing material because “almost everything is files” (`6.4_beyond_code_words_research_and_plans.md:1-35,82-96`) without an adjacent authorization/provider/data-minimization gate. | A privacy-sensitive learner can follow the local exercise literally before reaching Chapter 8 and expose confidential member, client, employee, or unpublished material to the agent/provider. | A privacy-aware facilitator must insert a data-classification and sanitization check at the point of use. | 5, 6, 7; possible for all | Add a mandatory data gate before Chapters 5 and 6 real-project exercises: classify data, confirm authorization and provider controls, minimize/redact, prefer synthetic style samples, and keep confidential/regulated work out unless organizational controls are approved. Repeat the gate next to every “paste notes/use real examples” prompt. |
| F13 | **Medium** | **M:** Counts and score maxima are present and arithmetically coherent: diagnostics use 8 x 0-3 = 24; chapter tasks use 4 x 0-3 = 12; capstone explicitly uses 7 x 0-2. However, the competency framework labels only one or two competencies “Primary” for many chapters, while checkpoint headings relabel reinforced competencies as primary. For example, Chapter 3 maps C3 primary/C4 reinforced (`competency-framework.md:66-80`) but its checkpoint says C3 and C4 are primary (`chapter-checkpoints.md:62-65`); similar drift occurs in Chapters 4, 6, 7, 9, 10, and 11. Overview also says “Retake the same diagnostic” although entry and exit use different paired situations (`overview.md:65`; `diagnostic.md:1-4`). | Learners and reviewers cannot tell whether checkpoint evidence should update only mapped primary competencies or every competency named by the task. “Retake” can also imply re-answering the entry form. | A scorer must choose a mapping convention not stated in the course. | All | Use one term set across the map and checkpoints (`primary`, `reinforced`, or `assessed`) and state how chapter evidence updates a competency profile. Replace “retake the same diagnostic” with “complete the paired exit diagnostic.” Keep the three score scales in a one-page scoring legend. |
| F14 | **Low** | **M:** `make audit` prints external facts as `PASS ... current` when the stored review date is in range and a text anchor exists. The script does no network request and cannot confirm that a maintainer actually opened the sources; maintenance documentation explains this limitation (`course/maintenance.md:22-29`). At this commit the review dates and commit date are the same, but no audit report artifact is tracked. | A learner or maintainer reading only terminal output can mistake date freshness for external factual verification. | Someone must inspect history/maintenance prose to interpret `PASS current` correctly. | 5; maintainers | Rename the state to `REVIEW RECORDED / NOT REVERIFIED OFFLINE`, include the limitation in terminal output, and link to durable review evidence (for example, a PR or issue ID) in each fact record. |
| F15 | **Low** | **M:** A one-character JSON defect in a disposable starter produced the actionable parse error first, followed by schema, summary, and filter failures caused only by undefined task data. Restoring the file returned all 8 passes. Recovery correctly says to read the first useful error (`recovery-guide.md:7-19`). | Beginners, screen-reader users, and additional-language learners may interpret four failures as four independent repairs. | A helper may need to explain cascade failures, although the recovery guide points in the right direction. | 1, 3, 4, 6 | Make dependent checks skip after parse failure and print `SKIP: task data unavailable`; keep the first parse error and a line/column hint. This preserves deterministic evidence while reducing noise. |

## Per-persona journey outcomes

These are **I — persona inferences** grounded in the mechanical/file evidence
above. They are hypotheses for a real pilot, not observed human behavior.

| Persona | Overview and diagnostic | Setup and starter | Representative checkpoints and scoring | Recovery, exit, and capstone | Simulated outcome |
| --- | --- | --- | --- | --- | --- |
| 1. No-code Mac creator, never used Git | Audience language is welcoming, but the 45-75 minute entry diagnostic introduces advanced assessment vocabulary before instruction. The answer key is easy to reveal early. | Mac installer and basic terminal sequence are plausible. The journey stops because the web course never explains how `starter/` arrives. After an evaluator-supplied clone/download detour, baseline, owner edit, expected failure, and fix all behave exactly as described. | **Chapter 3** no-code checkpoint supports file comparisons or graphical Git. **Chapter 4** requires a visible caught failure and maps well to the starter. Universal rubric is usable after terms are explained. | Scoped Git and no-Git recovery are good. Exit wording is ambiguous, and Chapter 11.5 adds live URL/full harness/revenue requirements not present in the capstone. | **Blocked at starter acquisition; conditionally viable after assistance.** |
| 2. Windows-native PowerShell office worker | Diagnostic can be completed in writing or recording. Platform confidence established in Setup is important for this persona. | PowerShell installer is shown, then Bash syntax appears in Setup/Chapter 3. Missing acquisition and native browser-open steps require a shell switch or translation. | **Chapter 3** is the critical failure point because evidence commands are Unix-shaped. **Chapter 8** can be completed as a paper threat model/mock approval and is a good alternative. Scoring is otherwise platform-neutral. | Recovery commands are Git-compatible, but file/path examples remain Unix-shaped. Exit/capstone can use a private demo but Chapter 11.5 implies otherwise. | **Blocked on the promised native path without command translation.** |
| 3. Low-vision keyboard/screen-reader learner | Diagnostics explicitly allow audio/video and assistive technology. Main site images have alt text, but every lesson has a duplicate out-of-order title structure. | Starter has labels, native selects, row/column headers, written risk, live counts, a skip link, and explicit keyboard/screen-reader alternatives. No live screen-reader test was performed. | **Chapter 3** permits equivalent interface actions. **Chapter 4** relies on a visual “fresh eyes/click/resize” acceptance pass without a nonvisual equivalent. Rubric permits timestamped recordings. | Recovery text and deterministic output are strong, though JSON cascades add noise. Capstone requires accessibility checks and accepts recordings/private delivery. | **Conditional pass with recurring accessibility friction; real AT testing required.** |
| 4. English-additional-language learner with low technical vocabulary | Plain-language teaching intent is strong, but the entry diagnostic and rubric use many undefined professional terms. Language support is allowed without a neutral term sheet. | Starter data edit is concrete; JSON punctuation and error prose may require translation/partner help, which is explicitly allowed. Acquisition remains missing. | **Chapter 1** claim-ledger task is conceptually accessible after terms are defined. **Chapter 8** introduces dense security vocabulary and needs a glossary bridge. The 0-3 rubric is consistent but linguistically demanding. | The recovery guide is ordered and symptom-based. “Retake the same diagnostic” and the changing 0-3/0-2 scales can cause avoidable interpretation load. | **Conditional pass with language assistance; diagnostic validity is at risk.** |
| 5. Experienced engineer new to agents | Entry diagnostic appropriately exposes judgment gaps without requiring product trivia. Engineer route is easy to locate. | Existing Git/terminal skills reduce setup friction; starter baseline and verifier are credible. Acquisition is still absent for a web-first user. | **Chapter 9** pass/fail/corrected-pass checkpoint is mechanically rigorous. **Chapter 10** permits either isolated parallel work or a justified sequential plan and correctly inventories shared resources. Answer patterns are useful after first attempt. | Recovery guidance is appropriately scoped. External product “current” claims cannot be reverified offline. Chapter 11.5 over-prescribes the capstone despite the capstone’s judgment-based declines. | **Pass with content-governance and claim-rigor corrections.** |
| 6. Locked-down corporate computer; no admin, installs, or paid access | Entry diagnostic and written simulations are available. Overview prerequisites immediately exclude the actual environment. | Setup’s only recovery is “use a personal machine.” HTML starter might open, but Node verification is delegated; no full product simulation path exists. | **Chapter 3** says run or simulate and can be done from supplied before/after artifacts, but none are supplied. **Chapter 8** explicitly allows a paper threat model/mock approval, which passes. Many Chapters 5-10 still assume live Claude Code. | No-Git recovery is documented. Exit diagnostic is writable, but capstone and Chapter 11.5 still assume tool access/full harness unless a facilitator invents substitutes. | **Blocked from the core instructional path, despite assessment accommodations.** |
| 7. Privacy-sensitive community organizer with confidential member data | Entry C8 uses a highly relevant volunteer-membership scenario and promotes private/synthetic delivery. | Synthetic starter is a strong safe practice surface once acquired. General secret/data warnings are accurate. | **Chapter 6** invites real notes, writing samples, and community-organizing files before repeating a data gate. **Chapter 8** least-privilege/manual-export checkpoint is strong and permits declining all live connections. | Recovery distinguishes Git from external state. Capstone’s private delivery and responsible-build gate are strong, but Chapter 11.5’s live/share language creates conflicting pressure. | **Conditionally viable if the learner follows the stricter privacy guidance and ignores the public handoff pressure.** |

## What passed

- Strict documentation build and navigation generation passed.
- No broken local page links, file paths, or anchors were found in 4,669
  rendered local-link checks.
- No built-site image lacked an `alt` attribute.
- The starter clean baseline is deterministic and matches the documented 6
  total, 4 open, 2 high-risk-open, and 1 unassigned-open summary.
- The no-code change produces the promised expected-summary failure, and the
  documented one-value correction restores all checks.
- The starter uses synthetic local data, references only local runtime assets,
  and the verifier found no network or credential markers.
- A deliberately broken starter can be diagnosed and restored using the
  Recovery Guide’s smallest-surface approach.
- Path-specific Git recovery works as documented in a disposable repository.
- The Recovery Guide explicitly protects untracked/ignored and external state
  and avoids blanket reset/clean instructions.
- Entry and exit each cover C1-C8, use the same 0-3 scale, and have the correct
  maximum of 24.
- All 11 chapter checkpoints and all 11 answer-pattern sections exist. The
  universal chapter rubric has a clear maximum of 12 and a safety stop rule.
- The assessment permits audio/video/live demonstration, translation,
  assistive technology, synthetic data, justified refusal, manual work, and
  simulations.
- Chapter 8’s least-privilege/manual-export path and the capstone’s
  private/synthetic delivery options are particularly strong.
- The current audit’s offline static rules, self-tests, exception handling, and
  quarterly cadence are transparent about their intended boundary in the
  maintenance document.

Areas with no observed issue:

- **Broken links/anchors:** none found in the built local site.
- **Starter baseline arithmetic:** no mismatch found.
- **Diagnostic maximum and chapter-rubric arithmetic:** no mismatch found.
- **Mac/Linux execution of tested offline Node/Git commands:** no failure found
  in this environment.
- **Real credential handling in pilot:** no credentials were requested or used.

## Study limitations

1. This was one evaluator simulating personas. It did not measure comprehension,
   confidence, completion time, retention, or actual learner behavior.
2. No Windows or PowerShell runtime was available. Windows findings are static
   command/platform review and need reproduction on Windows PowerShell 5.1 and
   current PowerShell 7.
3. No GUI browser, screen reader, keyboard session, automated accessibility
   engine, or mobile device was used. Accessibility evidence is static HTML/CSS
   inspection plus course-path review, not WCAG conformance testing.
4. External URLs, videos, captions, product documentation, package registries,
   plan terms, prices, and hosted course behavior were not checked. The local
   build and local links were checked only.
5. No Claude Code, GitHub authentication, MCP server, hosting provider, API, or
   paid service was exercised. No statement here validates current external
   product behavior.
6. Workload findings compare stated quantities and file counts; no learner was
   timed.
7. Persona outcomes intentionally identify likely friction. They do not estimate
   how common any persona or outcome is.

## Disposition-ready checklist

The checklists below preserve the recommendations at the time of the initial
simulation. The later [Remediation Verification](#remediation-verification)
records their current disposition; unchecked boxes here do not override that
evidence.

### Required before a real formative pilot

- [ ] Add course-file/starter acquisition for Git and no-Git learners (F01).
- [ ] Supply the promised end-to-end no-install/no-paid simulation lane or
      narrow eligibility claims (F02).
- [ ] Add and test a genuinely native PowerShell path through Setup and Chapter
      3 (F03).
- [ ] Correct workspace, sandbox, and Git recovery absolutes before the first
      live-agent lesson (F04).
- [ ] Align Chapter 11.5 with the capstone’s private delivery and justified
      decline rules (F05).
- [ ] Source/date or qualify economic, productivity, career, and anecdotal
      claims (F06).

### Recommended before broad public release

- [ ] Correct lesson heading hierarchy and add a CI heading check (F07).
- [ ] Add a reusable nonvisual/keyboard/zoom human-acceptance path (F08).
- [ ] Add a diagnostic term sheet and complete assessment glossary (F09).
- [ ] Recalculate full-practice workload and publish essential/optional routes
      (F10).
- [ ] Separate first-attempt assessments from answer patterns (F11).
- [ ] Put data-classification gates next to Chapters 5-6 real-data prompts
      (F12).
- [ ] Align competency labels, explain profile updates, and clarify the paired
      exit diagnostic (F13).

### Maintenance improvements

- [ ] Relabel offline external-fact status so “review date current” cannot be
      mistaken for verification (F14).
- [ ] Skip dependent starter checks after a JSON parse failure (F15).

### Real-pilot acceptance evidence to collect

- [ ] One learner from each of the seven personas completes the journey with
      assistance events logged.
- [ ] Windows PowerShell 5.1 and PowerShell 7 command transcripts pass.
- [ ] VoiceOver and NVDA learners complete navigation, starter filters,
      verifier interpretation, recovery, and one chapter checkpoint.
- [ ] Additional-language learners explain diagnostic prompts without answer
      coaching; scorers compare construct-relevant evidence.
- [ ] Locked-down learners complete the simulation lane without installs,
      credentials, paid access, or facilitator-created artifacts.
- [ ] Privacy-sensitive learners correctly choose synthetic/private delivery
      without being prompted by the facilitator.
- [ ] Median and range of actual time are reported separately for reading,
      exercises/checkpoints, diagnostics, and capstone.
- [ ] Pilot feedback is dispositioned as accept, modify, or decline with owner,
      target release, and verification evidence.

## Remediation Verification

Rechecked against the candidate remediation tree on July 23, 2026. Status means
the specific documented defect is resolved, not that a real learner pilot or
external product verification has occurred.

**Disposition:** 12 resolved, 3 partially resolved, 0 not resolved. No new
blocker or high-severity finding was introduced. The remaining original
high-severity residual is F03 (Windows execution not performed). F08 and F09
retain medium-severity human-pilot residuals.

| ID | Status | Exact changed evidence | Validation performed | Residual limitation |
| --- | --- | --- | --- | --- |
| F01 | **Resolved** | Setup now provides Git-clone and Download-ZIP acquisition, repository-root checks, and OS-specific open steps (`course/setup.md:154-287`); Starter Project now begins with exact find/enter/open instructions and links back to acquisition (`course/starter-project.md:10-55`). | Strict build passed; 5,636 rendered local links/fragments across 86 pages had 0 issues; required local path references exist. | The GitHub download/clone and OS browser/editor commands were not exercised against the live external service on Mac or Windows. |
| F02 | **Resolved** | The new no-install/no-paid lane states its evidence boundary and covers Chapters 1-11 (`course/simulation-path.md:1-242`); `starter/simulation/README.md` indexes the supplied brief, transcript, permissions, patch, before/after data, Skill, MCP, hook, team, release, and verifier artifacts. | Applied `changes.patch` with `git apply --check` and `git apply`; patched starter passed all 8 checks; before/after task data and summary matched the patch; only T-104's owner changed; all 7 JSON artifacts parsed. | No locked-down learner completed the lane in a browser, so usability and sufficiency without facilitator help remain unobserved. |
| F03 | **Partially resolved** | Setup separates PowerShell and CMD installer commands (`course/setup.md:58-68`), adds native acquisition/root/open commands (`course/setup.md:170-282`), and explicitly claims PowerShell 5.1 support (`course/setup.md:325-328`). Chapter 3 supplies PowerShell equivalents for navigation, files, Git, preflight, and opening HTML. | Static inspection found 15 PowerShell blocks and 0 runnable `&&`, `mkdir -p`, or Bash `cat` forms inside them. | Neither Windows PowerShell 5.1 nor PowerShell 7 was available; commands and path behavior were not executed on Windows. |
| F04 | **Resolved** | Setup and Chapter 3 now call the folder an intended workspace rather than an OS boundary (`course/setup.md:149-152`; `3.2_files_folders_and_paths.md:83-104`). Glossary definitions now bound commits and Git to tracked snapshots (`course/glossary.md:29,47,95`), and the Chapter 3 overview describes checkpoint/compare/selective restore (`03_command_center/README.md:12-14`). | Targeted scans found no remaining `whole world`, `defined sandbox`, `always roll back`, `tracks every change`, or `undo button` language; the course audit passed. | No beginner comprehension session tested whether learners can apply the distinction to untracked files, external effects, and backups. |
| F05 | **Resolved** | Chapter 11.5 now says the capstone contract governs and accepts public, private/authenticated, recorded, local, or synthetic review; live URL, every mechanism, revenue, and public sharing are not universal requirements (`11.5_staying_current_finishing_strong.md:46-82`). | Strict build and rendered-link checks passed; wording was compared with the capstone delivery contract. | No confidential-project learner tested whether the revised handoff removes perceived pressure to publish. |
| F06 | **Resolved** | The named opening stories are labeled illustrative rather than case studies (`01_the_shift/README.md:25-32`); market statements are framed as dated local hypotheses (`1.3_the_rise_of_agentic_engineering.md:49-63`); Chapter 6 requires measured local results (`6.5_your_first_true_automation.md:75-80`); Chapter 11 rejects guaranteed buyer, product, career, and timeline outcomes (`11.4_getting_paid_freelance_products_career.md:10-56`). Broader claims about context, planning, Skills, harness reuse, team speed, debugging, and automation were also converted to bounded hypotheses or instructions to measure local results. | Repeated repository searches checked the original examples and broader quantified/economic rhetoric after the final remediation; the previously identified `double this afternoon`, two-minutes-versus-an-afternoon, permanent Skill training, setup-market-rate, percentage, and universal ROI language is absent. | This was a targeted repository review, not an exhaustive independent fact-check. No external market, price, productivity, or career claim was independently verified with current sources or learner outcomes. |
| F07 | **Resolved** | All 54 lesson files now begin with one source H1, and the audit adds a `LESSON_FIRST_HEADING` rule plus self-test coverage (`course/maintenance.md:100-110`; `scripts/audit_course.py:255-272,510-519`). | Source check found 0 bad first headings; rendered inspection found 0 heading-level jumps across 86 HTML pages; audit self-test and full audit passed. | Heading structure was not navigated with a live screen reader. |
| F08 | **Partially resolved** | Chapter 4 now provides keyboard-only, screen-reader, 200% zoom/reflow, contrast/non-color, and delegated-visual-review rows with required evidence (`4.4_verification_never_trust_always_check.md:55-67`) and incorporates the matrix into practice (`:88-95`). | Strict rendering passed with 0 heading jumps and 0 images missing `alt`; references to the matrix were inspected statically. | No VoiceOver, NVDA, keyboard-only, zoom/reflow, contrast, or affected-user acceptance session was run. |
| F09 | **Partially resolved** | The new answer-free term sheet defines 20 assessment terms (`course/assessment/term-sheet.md:1-28`); the glossary includes the same terms; diagnostics route to the sheet before the questions (`assessment/diagnostic.md:9-11`); assessment policy permits translation and ignores polished English (`assessment/README.md:35-43`). | A term-presence check found 0 missing entries in either the term sheet or glossary; strict build and link checks passed. | No additional-language learner reviewed the wording, and no scorer comparison tested whether vocabulary effects were reduced. |
| F10 | **Resolved** | Overview now publishes reading, assessed-practice, and assessed-plus-capstone totals, inventory assumptions, optional extensions, and pause points (`course/overview.md:34-61`). Lesson 1.5 recalculates schedules for 3-4 and 8-10 hours/week and defines valid stopping points (`1.5_how_to_run_this_course.md:47-63`). | Inventory found 54 lesson files, 48,039 lesson words, 49 `Try it now` sections, and 11 checkpoint chapters; schedule arithmetic and cross-links were checked. | The ranges remain planning estimates, explicitly not completion data; no timed learner pilot validated them. |
| F11 | **Resolved** | The assessment path now uses an answer-free scoring guide and a deliberate save/disclosure interstitial (`assessment/README.md:5-16`; `assessment/review-after-attempt.md:1-27`). Diagnostics and checkpoints route through that page, and the answer key is absent from primary navigation. | Static route check found 0 direct `answer-key.md` references in Overview, Assessment Guide, Diagnostics, or Checkpoints; built links passed. | The interstitial is not access control and cannot prevent deliberate URL, repository, or search access; the course now states that limitation. |
| F12 | **Resolved** | Chapter 5 adds a mandatory classify/authorize/provider/minimize/substitute gate before creating agent-readable files (`5.4_building_a_second_brain.md:19-26`). Chapter 6 repeats the gate before writing samples, notes, job-search, community, client, incident, or workplace material (`6.4_beyond_code_words_research_and_plans.md:13-24`). | Targeted privacy-term inspection confirmed adjacent gates; strict build and local links passed. | No privacy-sensitive learner or real provider was used; actual authorization, retention settings, and learner decisions remain untested. |
| F13 | **Resolved** | The framework defines primary versus reinforced evidence and profile-update rules (`assessment/competency-framework.md:82-91`); the one-page scoring guide separates 24-, 12-, and 14-point scales (`assessment/scoring-guide.md:1-17,59-72`); Overview names a different paired exit diagnostic (`course/overview.md:78-84`). | Count check found 8 competency anchors, 8 entry situations, 8 exit situations, 11 checkpoints, 11 answer-pattern sections, and 7 capstone dimensions. Programmatic comparison found 0 primary/reinforced mapping mismatches across Chapters 1-11. | The instruments remain course feedback tools, not validated psychometric measures; scorer agreement was not piloted. |
| F14 | **Resolved** | Audit output now says `REVIEW RECORDED / NOT REVERIFIED OFFLINE`, prints the offline limitation, due date, primary sources, and a durable review URL (`scripts/audit_course.py:450-469`); maintenance documentation explains the distinction (`course/maintenance.md:24-37`). | `make audit-test` passed; `make audit` scanned 90 files, reported 0 static findings, labeled all five facts as not reverified offline, and passed. | This run made no network request and did not open the primary sources or durable GitHub records; current external-product accuracy is not established. |
| F15 | **Resolved** | The starter verifier computes line/column context for JSON parse errors and skips dependent task-data checks (`starter/verify.js:53-79,96-124,164-171`). | Clean baseline passed 8/8. Removing one quote in a disposable copy produced one JSON failure at line 76/column 15, exactly 3 `SKIP: task data unavailable` results, `3 dependent checks skipped`, and exit 1. | The malformed case was terminal-driven, not interpreted by a beginner or screen-reader learner. |

### Verification rerun

- `make build`: strict MkDocs build passed, 86 HTML pages.
- `make audit-test`: passed.
- `make audit`: passed; 90 files scanned, 0 static findings, 5 external
  records explicitly not reverified offline.
- `node starter/verify.js`: 8 checks passed.
- Disposable malformed starter: actionable parse location, 3 dependent skips,
  exit 1.
- Disposable simulation: patch check/apply passed, verifier 8/8, 5 artifact
  consistency assertions true, 7 JSON files parsed, and only
  `starter/index.html` plus `starter/expected/summary.json` changed.
- Rendered structural check: 5,636 local links/fragments, 0 issues; 0 heading
  jumps; 0 images missing `alt`.
- Assessment check: 8 + 8 diagnostic situations, 11 checkpoints, 11 answer
  patterns, 7 capstone dimensions, and 0 mapping mismatches.
- Static platform/path check: 15 PowerShell blocks, 0 runnable Bash-syntax
  violations inside them, and 0 missing declared simulation references.
