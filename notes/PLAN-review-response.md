# PLAN — response to the external reviews of the isotropic paper, round 1 (2026-10-12)

Article-kit `PROCESS.md` § 9. The build reviewed is the tag `iso-review-1` (61 pages). Both reviews
are by GPT-6.1 Sol at its Ultra setting, run by the author, and are archived as returned in
`records/affine/reviews/`:

- **the content review** (`review-content-iso-review-1-GPT-6.1-Sol-Ultra.md`): *major revision*.
  It finds no fatal error in the classification, the threshold, the rate, the bounds, the strict
  filtration or the Cin theorem, and reproduces the worked constants and both figures. It finds
  the novelty comparison incomplete (classical Hankel theorems, Bessel potentials), six
  statements of the surrounding prose wrong, one printed derivation incomplete, two "open
  problems" that the paper's own material settles, and the imaging reading overstated. Thirteen
  required changes, eight suggestions.
- **the presentation review** (`review-presentation-iso-review-1-GPT-6.1-Sol-Ultra.md`): twenty
  ranked changes.

Every finding was verified against the text, the blueprint, the Lean and the sources, by agents
that did not write the paper; the records are `records/affine/reviews/VERIFY-round1-*.md`, with
their scripts and outputs in `verify-round1-scripts/` and five new reading notes
(`READING-bingham1997abel.md`, `-bingham1999ratio.md`, `-aronszajn1961theory.md`,
`-cygan2017asymptotic.md`, `-leonenko2013tauberian.md`). **Nothing in the paper, the blueprint or
the Lean has changed.** A change is a new freeze (`iso-review-2`) and a second round.

## 0. Decided (2026-10-12)

**D1, the author, on reading this plan** (verbatim): "Some variant around D1 (a). My main interest is that we derive a scale spae from basic axioms and that we describe and classify the result and the consequences. Whether the results are new or not in probabillity research is not that important for me. My interest is to see what the hemigroup approach gives to scale space theory."

What follows from it, for every batch below:

- **The paper is a paper in scale-space theory.** Its subject is what the hemigroup axioms give:
  which kernels a rotation-invariant cascade in dimension d can have (the classification), what
  they look like (the centre: bounded or not, the shape, the rate through the profile), and how the
  dimension restricts them (the dictionary with the radial characteristic functions, the strict
  filtration, the critical values). The contributions are stated in those terms, for a reader who
  designs or uses a scale space.
- **The apparatus of novelty goes.** No list of what is "new as far as the author has found", no
  second tier of "not found stated", no sentence on what a search did or did not find. The three
  claims of § 1.1 are not replaced by other claims of novelty.
- **Attribution stays, and is exact.** Every statement that is known in probability, in the theory
  of Hankel transforms or of random fields is given to its source where it is stated, once, with
  the anchor read at the page (`RELEASE.md` rule 4). Table 3 becomes a table of where each
  statement comes from. A statement for which no source was found is simply proved; the paper does
  not say that it was not found.
- **The new statements are adopted because they describe the result** (D2, D3, D4), not because
  they may be new. The prior-art search for them is a search for the right attribution, bounded,
  and it does not gate the work.

**D2 to D7 and D9, by the author's standing delegation** (the recommendation is followed unless he
says otherwise; `REVIEW-author-paper-iso.md`): D2 the dictionary as a proposition with its printed
proof, Theorems 3.19 and 3.20 kept, a Lean proof of its self-contained part estimated before it is
decided; D3 option (2); D4 option (1); D5 route (A); D6 option (i); D7 as recommended; D9 the
30-page limit is held as the target, the tier paragraphs and the search sentences that D1 removes
being the first cuts. **Still the author's**: D8 (the AI statement is his declaration; it stays as
it is until he says) and D10 (the acquisitions).

**Order of work.** Wave 1, in parallel: R1 (the wrong statements and the two proofs); the new
statements as blueprint nodes with their proofs of record, refereed blind before any Lean (R3,
first half); the attributions of the new statements. Wave 2: the Lean of R3 and the guard of R2 in
the worktree with the build; then R4 and R5 as one rewrite of the abstract, § 1, the openings of
§ 3.3 and § 3.4, Table 3 and § 4 on the footing above, written once, after the statements are in
the paper; then passes 2, 3 and 7 on what changed, the second freeze and round 2.

## 1. The result of the verification

**The referee was right on every point of substance, and the verification found more.** No
theorem is false and no proof of record fails. What changes is what the paper may call its own.

### 1.1 The three claims of novelty (`VERIFY-round1-prior-art.md`, `-filtration-map-blind-check.md`)

| claim in the frozen text | verdict | what is in print |
|---|---|---|
| the rate at the centre, Prop. 3.15(1), "new for d ≥ 2" | **known, in every dimension and for every 0 < c < d**, with the paper's constants, for the ball and for the density | Leonenko–Olenko 2013, Theorems 3 and 4 (credited to Olenko 1991, Leonenko 1999, Olenko 2005; stated without proof in the survey); for c > (d−3)/2 also the Abel–Tauber theorem for Hankel transforms (Bingham 1972, Ridenhour–Soni 1974, as Bingham–Inoue 1997 restate it); the Matérn example is the Bessel kernel of Aronszajn–Smith 1961, (4,2), with the same three regimes and constants, and is Leonenko–Olenko's Example 3; the same constants by the paper's own method for the potential measure in Cygan–Grzywny–Trojan, Theorems 8–9 |
| the rate at the threshold, Prop. 3.15(2) | a corollary of Bingham–Inoue's Theorem 1.1; **not found stated**; the explicit logarithmic lower bound is the paper's | Inoue–Kikuchi 1999 is where a statement might be; not held |
| strictness of the filtration "from 𝒜_3 on", Thm. 3.19 | **follows from classical results at every step** | the map φ ↦ F(r) = c∫_0^r (1 − φ(u)) du/u between radial characteristic functions on ℝ^d and the exponents of 𝒜_d with finite c (the radial form of Sato's Thm. 17.5; in general form Jurek–Mason Prop. 3.6.10, statement read, proof not) carries Gneiting's strict chain (1999, p. 94) to 𝒜_d ⊋ 𝒜_{d+1}; an elementary step-profile argument does it too, and the paper's own proof of Thm. 3.20 already contains it |
| no Cin ray in the plane, Thm. 3.20 | **the same map at d = 1 with φ = cos**; no clause is left over | cos is not a radial characteristic function on the plane (J_0 > −1) |

The map was derived during the verification and then checked blind by a second agent, from the
definition of self-decomposability and numerically: it holds at every step. The paper's sentence
that Gneiting's functions "cannot serve here" is wrong: they serve as φ, not as e^{−F}. "The
literature on ℝ^d does not study one law" is false on the paper's own Table 3.

**What stays the paper's own**, as far as the sources now read show:
1. the classification from the measurement axioms on operators, in dimension d (not new as a
   statement about laws, and never counted);
2. the threshold with its boundary case, the two-sided bounds with their constants and the rate at
   the threshold with its lower bound, as statements for the class by one proof ("known
   ingredients, not found stated");
3. the quantitative filtration: the cone paper's family separates every pair of consecutive
   classes, at critical values that decrease strictly and are of exact order d^{−1/2};
4. the machine-checked development.

**What the verification adds that the paper does not yet state** (each derived in full in the
records, checked numerically, not machine-checked, and not yet searched for in print beyond the
notes on the line theory):
- **the slowly varying factor of the rate through the polar profile, with its constant in every
  dimension**: q(s) ~ Q s^{c−d} K(s), K(x) = exp∫_x^1 (c − k_d) du/u,
  Q = Γ((d−c)/2)/(π^{d/2}Γ(c/2)) · exp(−C_k − (c/2)(γ_E − ψ(d/2))), and its form at c = d. At d = 1
  it is Sato–Yamazato's (1.12) and (1.14) to the constant. This answers § 4.1's first question;
  the referee's formula is correct as stated (`VERIFY-round1-open-problems.md`, B);
- **√d·w_d → √π** (the same record, A): six printed lines from the proof's own bounds and
  Stirling's formula. § 4.1's fourth question is settled;
- **a member of 𝒜_{d+1} has a continuous polar profile in dimension d**, so any datum with a jump
  is a witness (`VERIFY-round1-mathematics.md`, item 9);
- **the separating family consists of Gaussian variance mixtures**: infinitely divisible in every
  dimension and self-decomposable exactly up to dimension d, which the classical witnesses are not
  (`-filtration-map-blind-check.md`, item 7);
- **the Student-t hypothesis is discharged in print**: Halgreen 1979, p. 14, covers the
  inverse-gamma law (held; read at the page);
- **the Gaussian caveat on C5 can be withdrawn**: Kanter's Lemma 3.1 (p. 70) and Theorem 3.2
  (p. 74) put a Gaussian in his class and close it under convolution.

### 1.2 Statements of the prose that are wrong (`VERIFY-round1-mathematics.md`, `-claims-and-trust-base.md`)

All confirmed; each has replacement wording in its record; none touches a statement.

| where | what | fix |
|---|---|---|
| p. 26, after Prop. 3.16 | "The power cannot be improved" (false for c > d) | restrict to c ≤ d; for c < d the profile form says exactly when a pure power holds |
| pp. 21, 25 | the slopes of Figure 1 (the bounded curve has slope 0) | one sentence, one caption |
| p. 30 | "the stable kernels have c = ∞" (the Gaussian endpoint has c = 0) | index below 2 |
| pp. 6, 13 | C6 "assumes more than its source" (it does not) | § 1.1, § 2.6 |
| p. 10 | Prop. 2.7, k(x) = ϖ((x,∞)) | "for almost every x" |
| pp. 22, 30 | a derivative filter "needs" N continuous derivatives (wrong as a necessity: the Matérn kernel of index 1 on the line) | "is enough for" |
| pp. 2, 30 | "no finite value to sample" | the invariant statement, with ‖μ∗f‖_∞ ≤ ‖f‖_∞ and finite cell masses |
| abstract, Table 3, § 3.3, § 4 | "rate … with its constant" folds c = d into c < d | two forms |
| p. 22 and four more | "explicit constants" for Prop. 3.17 | display A_β (explicit formula in the record) or reword |
| p. 7 | "readable on its own" | Theorem 2.3 is restated without proof |
| pp. 55–56 | Appendix B's pass criterion is the twelve-axiom guard, and the printed command shows 68 of 141 declarations and none of the printed block | corrected sentences; see D7 |
| p. 30 | the Student-t item as an open problem | cite Halgreen |

Proof-level, in the paper's printed proofs only (the Lean is complete in each case):
- **p. 54**, the alternative derivation of 𝒜_∞ = 𝒮 omits three steps, all proved lemmas of the
  blueprint and the Lean (`lem:lk-negative-definite`, `lem:bernstein-triplet-unique`,
  `lem:dilation-decreasing-profile`); the paper's copy dropped the pointer.
- **pp. 44–45**, the Borel measurability of K ↦ u_K is asserted. A proof by σ-compactness is in the
  record; it needs Blaschke's selection theorem and no descriptive set theory, so the open
  question of a reference for analytic sets goes away. This is a shared proof of record.

**The trust base holds.** Lean's report for all 141 distinct declarations
(`verify-round1-scripts/axioms-all-144-output.txt`): each depends on Lean's three axioms and a
subset of the nine; none names an axiom of the affine paper; every statement's set equals Table 1.

### 1.3 The presentation review (`VERIFY-round1-presentation.md`)

Three items accepted, sixteen in part, one the author's (the AI statement). Seven of its
descriptions of the text were wrong or already met. Most worth doing: the gloss of "from scale
zero" on p. 1; the Cin rays as "elementary exponents" with the sentence on superpositions brought
forward from p. 29; the slowly varying factor explained at the opening of § 3.3; the figures
redrawn at their printed size (the lettering prints at about 4.4 pt); the abstract, once, after
the content response.

## 2. Decisions for the author

**D1. What the paper is, after § 1.1.** None of the three headline results is new as a qualitative
statement.
- (a) *Reposition and strengthen* (recommended). The paper becomes the isotropic theory in
  dimension d with its literature placed correctly: the classification from the axioms; the
  dictionary between 𝒜_d and the radial characteristic functions, which explains the dimension
  filtration and connects it to Schoenberg and Gneiting; the kernel at its centre in terms of the
  polar profile, with constants in every dimension; the quantitative critical values with their
  limit; all machine-checked or marked. The three claims of novelty are withdrawn and replaced by
  what § 1.1 lists, each after its own search of the literature.
- (b) *Reposition only*: withdraw the claims, correct the prose, add nothing. The paper is then a
  synthesis with a formal development; quicker, and thinner than (a).
- (c) *Do not publish the isotropic paper separately*: fold it back into the affine paper as its
  first part (reversing the repository's ADR-0001).

**D2. The dictionary as a statement** (if D1(a)): a proposition for the map and its two
consequences (strictness at every step; no Cin ray), with Theorems 3.19 and 3.20 kept for the
family and for the self-contained proof. A blueprint node; a Lean proof is a separate decision
(the classical side, Gneiting's chain, would be a new cited fact). Recommended: the proposition
printed with its proof, the theorems kept, no new cited fact, the Lean in a later item.

**D3. The profile form of the rate** (`VERIFY-round1-open-problems.md`, B, options 1–3): (1) a
proposition with full Lean, about 1650 lines; (2) the asymptotic of the exponent in Lean and the
two closed forms of the constant as computations of the prose, about 950 lines; (3) a remark with
a one-page printed proof. Recommended: (2), after a prior-art search for the constant in ℝ^d (it
is now the paper's most specific result, so it gets the search the rate did not).

**D4. √d·w_d → √π**: (1) a clause of Lemma A.5 with its Lean proof, 300–400 lines, Stirling for the
real Gamma function proved, no new cited fact; (2) a remark. Recommended: (1).

**D5. C5 and the Gaussian part**: (A) withdraw the caveat in § 1.1, § 2.6, the node's annotation
and ledger A8, citing Kanter's Lemma 3.1 and Theorem 3.2; (B) also narrow the cited fact and prove
the Gaussian case directly, several hundred lines of Lean. Recommended: (A).

**D6. The Student-t clause** (also the hub's Q-0418, point 3): (i) keep clause (4) conditional in
form and say in the text that Halgreen proves the hypothesis; (ii) admit Halgreen's theorem as a
cited fact and make the clause unconditional. Recommended: (i) now.

**D7. Review access and the guard.** The referee asks for a frozen, accessible export.
Recommended: as the cone paper did, the public export at the release; for round 2 the complete
axiom report attached with the PDF; a paper-specific guard (nine names) added to CI and to the
export. A review export before the release needs a `[[modules]]` entry for `iso` and about three
hours of build.

**D8. The AI statement.** Both reviews ask to drop the word ratio and the sentence on spare time.
`WRITING.md` § 6 does not require a ratio. Options in `VERIFY-round1-claims-and-trust-base.md`,
item 7. In every case "the module's" becomes "the paper's".

**D9. Length.** About five of the thirty main-text pages restate results (each headline result
seven to twelve times). The fixes of § 1.2 and § 1.3 add about 25 lines; D2–D4 add more. The cuts
proposed (the second paragraph of § 4, the tier paragraph of § 3.3, two passages of the opening of
§ 3.4, Table 3's anchors to an appendix table, Definition 3.18 as a pointer) recover about 35.
Decide: hold the 30-page limit, or let the main text grow by what D2–D4 add.

**D10. Sources to acquire** before the wording is final: Leonenko, *Limit Theorems for Random
Fields with Singular Spectrum* (1999), or Olenko's papers of 2005–2006 (queued, need a browser),
for the primary statement of the rate; Bingham 1972 and Ridenhour–Soni 1974; the published
Bingham–Inoue; Inoue–Kikuchi 1999 (the threshold case); a reference for Blaschke's selection
theorem (Schneider, *Convex Bodies*); Jurek–Mason's proof of Prop. 3.6.10 is held and unread.

Declined, with the reason for the response: reordering Theorem 3.12's clauses and moving 3.12(3)
(three shared statements renumbered, no page gained); renaming "origin datum" (a shared
definition, the affine paper, 29 Lean files; a gloss is added instead); the 6 + 4√2 bound to a
remark (a statement and its Lean, no page); adding uniqueness to C6 (the three lemmas are cited
instead).

## 3. Batches of work, after the decisions

Each batch is one item on its own branch, through the gates of `run-freeze-gates.py`.

- **R1, the wrong statements and the two proofs** (§ 1.2; needs D5 and D6 only): prose, the
  blueprint proof of `prop:isotropic-radial-monotone` with its mirror, ledger A8 and A10,
  `READING-kanter1977unimodality.md` extended, `READING-halgreen1979self.md` written, Appendix B's
  sentences, the Table 1 caption.
- **R2, the trust base** (D7): the full axiom report as a record of the paper, the nine-name guard
  in CI.
- **R3, the new statements** (D2, D3, D4): blueprint nodes with proofs of record from the
  verification records, each refereed blind before the Lean; the prior-art search for D3 first.
- **R4, the repositioning** (D1; after R3, so that it is written once): the abstract, § 1's answers,
  prior work and contributions, Table 3 (with Aronszajn–Smith, Leonenko–Olenko, Bingham–Inoue,
  Cygan–Grzywny–Trojan and the dictionary), the attributions of § 3.3, the opening of § 3.4, § 4
  and § 4.1 (two questions left: the derivatives, and what D6 leaves). Drafted cells and sentences
  are in `VERIFY-round1-prior-art.md` §§ 5–6. Then passes 2, 3 and 7 of `PROCESS.md` § 8 on what
  changed.
- **R5, the presentation items** (§ 1.3, D8, D9), with the figures redrawn.
- **R6, the second freeze** and round 2, in another system, with the axiom report attached and the
  line and cone papers' PDFs beside the manuscript (the referee could not retrieve them).

## 4. What is not settled

- The primary sources of the rate (D10) were not read: the citation is "as stated in
  Leonenko–Olenko's survey" until one is.
- Whether the profile form of the rate with its ψ(d/2) constant, the continuity criterion and the
  dictionary's radial specialisation are in print was not searched.
- The verification's own derivations (the map, the profile form, the limit, the Borel argument,
  the direct proof of the Gaussian case) are checked by a second agent or numerically, and not
  machine-checked.
- One agent stopped a slow script with `taskkill /IM python.exe`, which may have ended another
  agent's run in the same worktree at about 10:05; every agent reported its scripts complete with
  saved output, so nothing is known to be missing.
