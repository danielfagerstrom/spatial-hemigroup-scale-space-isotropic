# Changelog

All releases of this module are recorded here, newest first, with what changed and why, and in
particular which statements were renumbered, strengthened, weakened or withdrawn (hub `RELEASES.md`,
rule 2).

## iso-v0.1 — 2026-10-14 — first release of the isotropic paper: rotation-invariant self-decomposable kernels in dimension d

The article *Spatial scale space from hemigroup axioms: rotation-invariant self-decomposable
kernels in dimension d*: a paper of 55 pages (sections 1 to 4, Appendices A and B) and a
supplement of 42 pages (sections S1 to S4), from one set of sources. It follows the
characterization on the line and the admissible cone, and restates in its section 2 what it
uses of the two. This is its
first release: no statement is renumbered, strengthened, weakened or withdrawn against an
earlier version, and the statement numbers below are the ones to cite.

What it states. The axioms ask that the stages of the cascade compose, a hemigroup indexed by
two scales, and that rescaling the signal relabels the scales; they do not ask for a semigroup.
In dimension d the rotation-invariant families they allow are classified by reduction to the
line (Theorem 3.6, on operators Corollary 3.7): the kernels that take the signal from scale
zero to each scale are the dilations of one rotation-invariant self-decomposable law, and every
such law but the point mass occurs (the main result as one statement, Corollary 3.9). The
kernel at its centre: with c the power at which the transform falls off, the density is bounded
near the centre exactly when c > d (Theorem 3.13), c is read from the exponent alone and is the
same in every dimension (Corollary 3.14), and for c at most d the growth of the spike and its
constant are given (Proposition 3.18, with the Matérn kernels as Example 3.19 and Table 1). A stage between positive scales passes a fixed fraction of the record unchanged
when c is finite (Proposition 3.20). The dimension filtration: each higher dimension admits
strictly fewer exponents, with a dictionary between the dimensions (Proposition 3.21), a test
on the profile one dimension down (Proposition 3.22), the step exponents (Proposition 3.23) and
a separating family whose critical values decrease strictly, like the square root of π/d
(Theorem 3.25).

What is machine-checked. Thirty-three statements have formal counterparts in Lean 4 (219
declarations, listed statement by statement in section S4 of the supplement), on Lean's three
logical axioms and seven cited facts of the literature, C1 to C7 in the paper (ledger entries
A1 to A4, A8, A10 and A11; nine axioms, C3 being three); Table 4 says which statement rests on
which. Five statements are proved in print only, and section 1.1 lists them: Lemma 3.17,
Propositions 3.21 and 3.23, Corollary A.7 and Proposition A.8. The statements restated from the
two earlier papers are cited, and the formal proofs assume none of them. No human other than
the author has reviewed the paper, and the formal statements were compared with the printed
ones by AI agents only; the statement on the use of AI says so.

What is stated as open in section 4.1 and promised nowhere: how the first derivative of the
density that the threshold theorem does not reach behaves at the centre, and whether the
absolutely continuous part of a stage between positive scales is bounded near the centre.

Reviews. Two external rounds, archived verbatim with the plans that record what was done for
every finding: GPT-6.1 Sol at its Ultra setting on the first review build (content and
presentation), and five blind Claude Fable referees on the second. The response to the second round split the
article into the paper and the supplement. A blind draft review, the author's reading, and a
scope audit and a citation audit on the final text preceded the release.

The release form. This repository is private, so the release is a public verification export,
https://github.com/danielfagerstrom/spatial-hemigroup-scale-space-isotropic, tagged `v0.1`
there: the two PDFs, their LaTeX sources, the Lean development with its guard and its ledger of
the cited facts, blueprint chapters 2 and 3, the scripts of the two figures and of Table 1, the
process account and the reviews. The export is built from scratch, and its guard prints, for
the eight declarations of the block in section S4, what the supplement prints. The Lean
development of the export is the Lean of this paper, 79 files: those that hold a declaration
of one of its statements, what they import, and the paper's formal examples, its probes and
its axiom guard. The formal development of the companion paper on affine covariance is in this
repository and not in the export, and neither are that paper's text and blueprint chapters. Of
it the export has three things, since the two papers share them: the companion paper's three
cited facts, stated beside this paper's seven, on which no declaration of the export depends;
the correspondence between operators and kernels in the general form of which Lemma 3.3 is a
case, with the definitions it is stated in; and general lemmas that both papers use.

The version DOI and the concept DOI are recorded here at the deposit.
