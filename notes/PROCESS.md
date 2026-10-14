# How this article was made — the process account

This is the account that the "Author contribution and use of AI" section of both papers points to
(`paper/ai-statement.tex`, `paper-iso/ai-statement.tex`), on Paper V's convention of pointing rather
than restating (`spatial-hemigroup-scale-space/records/selection/PROCESS.md`, `records/line/PROCESS.md`,
`records/cone/PROCESS.md`). It holds the chronology, the division of labour in numbers, the reviews,
and the caveats the numbers travel with. Written in the first person, from the session archive and the
repository's own record (git log, `CHANGELOG.md`, the ADRs, `notes/HANDOFF.md`); it does not repeat the
trust base, which each paper's §1.1 owns.

The two papers are one history until 2026-10-04. The module was created on 2026-09-07 from the single
spatial draft in `spatial-hemigroup-scale-space` (that earlier work is counted in Paper V's own
process notes, not here). Everything from the first item dispatched in this repository, Q-0043 on
2026-09-25, through the whole-paper review of 2026-10-04 built one article; the split into the
isotropic paper (`paper-iso/`) and the affine paper (`paper/`) is itself a decision taken that day
(`adr/0001-two-papers-split-at-section-3-4.md`), and both papers' statements of record are blueprint
chapters written before it. So this note is shared, as the isotropic paper's introduction restates
nothing of the affine paper's and vice versa, but their production is one campaign up to the seam and
two short ones after it.

*Status: drafted 2026-10-05 (Q-0315, pass 5). The by-the-numbers figures below were re-derived by
the archivist on 2026-10-13 (Q-0451), for the release `iso-v0.1`, to the archive's sync of that day (last archived turn 16:03
UTC). They are lower bounds and stop at that sync: re-derive once more at a release.*

## How the work went

The research programme and the question are the author's, as for the earlier modules of the hemigroup
programme: what the theory of the line and the cone becomes on $\mathbb{R}^d$, and what affine
covariance forces along the Loewner order. The question was asked, and the hub decided this module's
place in the programme's order, before this repository's first commit.

**25 September** opened the module's own work. An agent read Sato (1999) at the page for the
boundedness threshold in dimension $d$ (Q-0043); the postdoctoral research office had proposed, in
P-0013, that the threshold is the dimension itself, and the day's work proved it as a theorem rather
than leaving it a conjecture. The same day, a second item (Q-0044) proved the dimension filtration
strict at every step and that no $\mathrm{Cin}$ ray of the line reaches the plane, closing P-0014's two
questions.

**27 September to 1 October** built the blueprint's classical and axiomatic layers: the $d^{-1/2}$
rate of the thresholds (Q-0150); the passage from operator axioms to kernels in $\mathbb{R}^d$
(Q-0207); the reduction of the classification theorem to the line paper's (Q-0208); the affine-orbit
step cone and the single-step rigidity theorem, reduced to the line's Darmois–Skitovich form
(Q-0206, Q-0241, Q-0246); and, across several items, conjecture A$'$ for similarity-covariant
families with an elliptical part — stated, then refuted as stated, then proved under a comparable
rank-one limit (Q-0246, Q-0264). Each batch of new nodes was checked by an independent blind referee
before the author saw it, the project's standing rule; every one of these rounds found the mathematics
correct and narrowed an annotation or two. The author's own decisions in this window — recorded in
`CHANGELOG.md` and `notes/HANDOFF.md`'s "Decided" — include accepting the postdoc office's proposals
P-0017 through P-0020, answering the weakened-axiom and hypothesis-(H) questions, admitting ledger
entry A5, and ordering every batch's blind check before the next was begun.

**3 October** fixed the article's structure: a review of what the line and cone papers supply, then
three sections organized by one $(G, W)$ axiom scheme (`notes/PLAN-article-structure.md`), with
Khintchine's null-array theorem admitted as ledger entry A6 and the implementation chapter moved out to
Paper VI. The parameter space, the invariant wedges on $\mathrm{PD}(d)$, and the smaller-groups table
were all proved and blind-checked that day (Q-0265 through Q-0268), closing the mathematics the article
would need.

**4 October** was the heaviest day by a wide margin: the draft was rewritten to the plan's structure
first (Q-0279), then the paper was drafted section by section against the blueprint (Q-0285 through
Q-0288: the trust base and the cited facts, chapter 3 transcribed verbatim, chapter 4's axiom scheme,
chapter 5's landscape, orbits, smaller groups, the overview table and shape adaptation), each section
immediately blind-reviewed and its flags fixed at the blueprint or the paper as the finding required
(Q-0286, Q-0290, Q-0291). The whole paper, now 89 pages, was then read blind as a unit
(`records/affine/REVIEW-paper-whole.md`), and its flag 41 is what produced the split: the isotropic
theory of the former §3 depends on nothing in §§4–5 and reads as a complete 20-page paper for a
probability audience, while §§4–5 use only four of its statements. The author took the split
(`adr/0001`) the same day, and two short, independent drafting-and-review cycles followed before the
day was out: the isotropic paper opened, was reviewed whole, revised, and reviewed again
(Q-0307, Q-0310, Q-0311); the affine paper's remaining fixes were applied and it too was reviewed whole
and revised (Q-0309, Q-0312). In parallel all day, a second unattended line of work scaffolded and then
typed the Lean statement skeleton for every one of the blueprint's 103 nodes (Q-0281, dispatches 1–5),
priced at some 55,700 lines, itself blind-reviewed before the author saw it and immediately followed by
a first wave of proof (wave 1, groups A–D) that closed several nodes on Lean core alone. Late the same
evening (commit timestamps 21:47–23:13 local), three further passes landed on both papers: the
isotropic paper's readability and scope-audit passes with a last prior-art reading (Q-0313); the
affine paper's own scope audit and the Lean session's report that two new nodes exist and that a
listed ledger entry (A7) does not (Q-0314); and the content fixes the blind register review of both
papers found (Q-0317, 204 flags on the affine paper's register alone, with the two new nodes blind-
checked as well).

## What the agents did, in detail

The prose, the statements, the proofs, the figures, the numerical checks, and the Lean development
begun in this window were all written by AI agents, in dialogue with the author and increasingly
through the unattended work queue: of the items named above, all but the plan and the split decision
itself were dispatched runs that worked without anyone to answer a question. Mathematical content
originated with the agents more than once: the central boundedness threshold began as the postdoctoral
office's conjecture (P-0013) before it was proved; the step cone of a general affine orbit and
conjecture A$'$'s refutation and repair were an agent's arguments on the author's question; the Lean
skeleton's own blind review found a statement that was false as typed and fixed it before any proof
was attempted. Corrections that narrow a claim to what its proof gives are delegated to the agents by
the project's standing rule (the author's decision of 2026-10-04): a session may accept such a finding
without waiting, each one reported and reversible at the author's word. The technical decisions of the
Lean skeleton and of the proof waves were, for the most part, the agents' prices and routes, approved
by the author through the standing delegation rather than drafted by him.

## The reviews

Review by agents with no part in the writing was the working method throughout, not a final gate: every
batch of new blueprint nodes was refereed blind before the author saw it; each paper's sections were
read blind against the writing standard, section by section and then as a whole; the Lean statement
skeleton was itself reviewed blind before any proof was attempted; and the blind register review of
2026-10-04 (Q-0317) read both papers' full statement registers a further time, finding 204 flags on
the affine paper's alone. Every finding was checked against the text, the blueprint, or the Lean before
it was acted on, and the disposition of each is recorded beside its review
(`records/affine/REVIEW-*.md`, `records/formalization/REVIEW-*.md`). The cited results were read at
their page anchors from held copies by an agent acting as librarian, and a reading note
(`records/affine/READING-*.md`) was written before the statement resting on it. **Beyond the author, no
human reader has reviewed either paper.**

## By the numbers

The archivist's re-derivation of 2026-10-13, from the canonical tier of the session archive
(`ai-archive/canonical/sessions.jsonl`, synced through 2026-10-13 16:03 UTC) by the script
`records/affine/ai-figures-2026-10-11/rec.py` (the output saved beside it is that of 2026-10-11; the script was run again unchanged on 2026-10-12 and on 2026-10-13, and the figures of the last run are `records/affine/ai-figures-2026-10-13.md`). It is scoped to this module the way Paper V's notes
scope theirs. The **core** is every unattended queue run tagged to this repository (31 sessions), the
Paper VII session run from the hub, counted whole, and the Lean formalization session of 2026-10-04 to
2026-10-08. The **ceiling** adds the four hub shift sessions that touched this module among others.

- **Period**: first archived session 2026-09-25 (Q-0043), last archived turn 2026-10-13; sixteen
  archived days (days with a turn).
- **Words, typed only** (the author's own keystrokes, not a dispatched session's machine-written task
  brief: `typed_words`, not `human_words`; see "Reading the numbers honestly" in
  `ai-archive/README.md`): core 3,964 words in 135 turns against the agents' 166,452, subagents
  included, about 42 to 1; ceiling 12,768 against 278,684, about 22 to 1. **Quote the range**: 22 to
  42 to 1. The upper end was 46 on 2026-10-12: since then the author's typed words in the core grew
  by 549 and the agents' by 10,434, so the ratio of the core fell. Without the Lean session, which the report of 2026-10-04 could not contain, the range is
  20 to 38 to 1 (3,581 against 137,625; 12,385 against 249,857). The statements quote the range with
  it, since they say that Lean machine-checks the statements.
- **Active time and span**: core 138.9 h active over 413.5 h of summed session spans; ceiling 199.6 h
  over 716.8 h. Active time is the time of the turns, the agents' and subagents' included, each gap
  capped at fifteen minutes. It is not the author's hours: 63.8 h of it is the Lean session, mostly
  87 subagents at work. The spans are summed over sessions that overlap; from the first archived turn
  to the last the wall clock is about 446 h.
- **Counts**: 33 archived sessions in the core (31 unattended runs, two interactive), 294 subagent
  traces; commit subjects in `git log` name 99 queue items.
- **Against the first report**: the figures of 2026-10-04 (to the sync of 2026-10-03: 15 to 34 to 1
  over seven archived days, core 1,268 typed words against 43,071) recompute unchanged from today's
  archive when it is cut at that sync. Every change is new material, and the ratio moved upward.
- These figures are **lower bounds**. Active time is capped per gap; a professional obligation whose
  records cannot be exported leaves no trace, so the archive is of spare time only; the words count
  visible prose only, so code, LaTeX and proofs written through tool calls are not in the agents'
  words; the scoping is by repository tag and named session, which misses hub time spent on this
  module inside a session named for something else, and counts the hub session whole though it also
  managed other work; what follows the sync is not in them. The typed words leave out two referee
  reports written by another AI system, 7,599 words, which the author pasted into the hub session
  on 2026-10-12 and which the archive counts as typed: they are not his words, and with them the
  ratio would read about 14 to 1.
- **One figure for both papers.** The hub session and the Lean session serve both papers, and the
  author's words and the active time cannot be divided between them, so the figures are the
  module's, as the statements say.

## Sources for this account, and where the record qualifies it

The chronology ("How the work went") and the division-of-labour narrative are from `git log`,
`CHANGELOG.md`, `notes/HANDOFF.md`'s "Decided" entries, and `adr/0001`. The by-the-numbers figures are
the archivist's, re-derived on 2026-10-11 as said above; the scripts of the re-derivation, with the
check that reproduces the first report's figures at its own cut, are in
`records/affine/ai-figures-2026-10-11/`.

Two earlier attempts to extend the first report (Q-0315 on 2026-10-05, Q-0324 on 2026-10-06) did not
succeed, and the second concluded that the sessions of Q-0313, Q-0314 and Q-0317 were missing from
this machine and would have to be exported. That was a misreading. The three items were never
separate sessions: they were subagents dispatched by the hub's Paper VII session, and their turns are
in that session's record as agent turns, where a search by repository tag, branch or title does not
find them. Nothing had to be exported.

The figures were first computed to the sync of 2026-10-10 and moved to that of 2026-10-11 when the
archive's daily run landed the same evening; that run took in three queue runs (Q-0379, Q-0382,
Q-0398) and the hub session's work of the day, this re-derivation included. What the figures still do
not hold: the turns after 2026-10-13 16:03 UTC; subagent traces lost when a session's context was
compacted; and commit attribution, since the archive's list of repositories does not include this
one, so the count of queue items is `git log`'s.
