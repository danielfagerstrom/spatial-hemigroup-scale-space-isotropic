# PLAN — response to the second external round of the isotropic paper (2026-10-13)

Article-kit `PROCESS.md` § 9. The build reviewed is the tag `iso-review-2` (86 pages). The round was
run with Claude Fable, at the author's choice, as five fresh reviewers, each given only the manuscript,
the three earlier papers of the series and Lean's axiom report. The reviews are in
`records/affine/reviews/review-round2-iso-review-2-*.md`, as returned, with the prompt. Every finding
was then verified against the text, the blueprint and the sources:
`reviews/VERIFY-round2-scale-space-literature.md`, `VERIFY-round2-mathematics.md`,
`VERIFY-round2-length-and-exposition.md`. Nothing in the paper has changed.

## What the round found

| part | recommendation | in a line |
|---|---|---|
| A, the front and the trust base | minor revision | each claim is carried by a statement; Appendix B agrees with Lean's report |
| B, the axioms and the classification | minor revision | every proof checks; the main result is what the statements prove |
| C, the kernel at its centre | minor revision | no error or gap; every constant and worked number reproduces |
| D, the dimension, and the conclusion | minor revision | no error or gap; two questions the paper calls open are answered by its own means |
| E, the literature and the exposition | major revision | the scale-space work closest to the paper is missing; 86 pages is too long |

**The mathematics holds.** The four statements proved in print only were read line by line and are
correct. Two "errors in a proof" that reviewers reported are misreadings of the PDF (the factor and
the word they miss are printed).

**The main result is new to scale-space theory as far as the reviewer of the literature found**: no
earlier use of self-decomposability or of hemigroups in scale space.

**The scale-space literature has to come back in** (three reviewers; confirmed at the page; the
author's line and cone papers cite most of it):
- the Bessel scale space of Burgeth, Didas and Weickert (2005) is the paper's Matérn family as a
  semigroup along the index; they also dilate the kernels at a fixed index and state no composition
  law for the dilations, which is what the hemigroup supplies;
- the two-scale composition law is the causality axiom of Alvarez, Guichard, Lions and Morel (1993),
  with a free relabelling of scales; what this paper drops is their locality and regularity;
- two sentences say "semigroup" where "semigroup with scale invariance" is meant;
- the time-causal literature and Felsberg and Sommer's Poisson scale space are to be cited.
A corrected "Relation to scale-space theory" is drafted in the literature record, with every anchor
read at the page.

**Reviewer claims that did not hold**: Iijima's priority "on the Pauwels family" (his family yields
the Gaussian); the shadow as Matheron's descente (it is Daley and Porcu's formula, already cited);
Schoenberg as the source for Ω_d (he prints the inclusion only); the rate at a fixed kernel as new
(it is in Leonenko's book); a residual of the Matérn law "not infinitely divisible" (every stage is).

**Two descriptions the paper can add** (derived in full and checked numerically in the mathematics
record):
- *The stages.* A stage from scale s to scale t of a family with no Gaussian part and finite c is a
  point mass of weight (χ(s)/χ(t))^c at the centre plus a smoothing part: the stage passes that
  fraction of the finer record through unchanged. For the Matérn kernels with χ(t) = t the fraction
  is (s/t)^{2γ}. With c = ∞ or a Gaussian part the stage has a density.
- *The step exponents one and two dimensions up.* The exponent of a step profile of dimension d is
  the exponent of an infinitely divisible law exactly in dimensions up to d + 2, and of a
  self-decomposable one exactly up to d: in two more dimensions it is still a kernel, and no longer
  a cascade.

## Decisions for the author

**1. The format.** The paper is 86 pages: 30 of main text, 46 of proofs, of which 31 are of statements
that Lean has checked. Options, with measured pages (`VERIFY-round2-length-and-exposition.md`):
(a) as it is, 86; (b) a paper of about 48 pages with a supplement of about 40: in print the main text,
the proofs of the classification, the statements Lean did not check with their proofs, the sources
and notation tables; in the supplement the proofs Lean checked, the cited facts in full, the list of
declarations; (c) the cuts the reviews agree on, 79. **Recommended: (b).** Its dividing line is the
paper's own, it touches no statement, the full document still builds from the same sources, and the
journal accepts supplements.

**2. The stages.** Add the description of the stages as a proposition of § 3. **Recommended: yes,
machine-checked** (about 800 lines of Lean by the estimate). It answers the question of § 4.1 that
matters most to a user of the scale space.

## Taken under the standing delegation

- The scale-space literature goes in as drafted; the Matérn family is presented as the Bessel
  kernels of scale-space theory, a known member of the class.
- The main result is stated once, as a corollary after Lemma 3.8 (two reviewers), with its Lean.
- The step exponents: a short proposition proved in print, and the question leaves § 4.1.
- Theorem A.15 is replaced in print by the existing node that carries what is not duplicated; the
  w = 4 example says its plane half is proved in the cone paper; the confirmed slips are corrected
  (a cross-reference, two citation points after Proposition 3.11, "from scale zero" in § 4,
  "admitted" in the abstract, the renumbered clause of Proposition 2.6, the smooth density of a
  kernel with a Gaussian part listed in § 1.1, the witnesses and probes added to the axiom report).
- Ten exposition items (the length record, § 4): one Matérn example with a small table; the clauses
  of the threshold theorem that carry the result said beforehand; terms glossed at first use;
  colliding letters renamed where it is cheap.
- Declined, with the reason: a sharper constant in one lower bound (a machine-checked statement
  would change for no gain to a reader); crediting Schoenberg, Matheron or Iijima as the reviewers
  proposed (refuted above); a review-accessible export before release (as in round 1).

## Order of work

1. The new statements at the blueprint (the corollary, the stages, the step exponents), refereed
   blind, then their Lean.
2. The paper: the literature, the corrections, the new statements, the exposition items, and the
   split into paper and supplement if decision 1 is (b).
3. The gates, the author's final reading, the release (`PROCESS.md` § 10). A third external round is
   not planned: the second found no error, and what changes is literature, format and two
   descriptions that will have been refereed and machine-checked.
