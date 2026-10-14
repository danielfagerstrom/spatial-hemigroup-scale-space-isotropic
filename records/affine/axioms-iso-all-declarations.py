#!/usr/bin/env python3
r"""The axiom guard of the isotropic paper, and Lean's `#print axioms` report for EVERY declaration
that Appendix B of the paper lists, with its comparison with the paper's table of the cited facts
per statement (`tab:trust-base`; Table 1 of section 1.1 until Q-0428 moved it to Appendix B, where
it is printed as Table 3; "Table 1" below and in the generated file's messages is that table).

The module's guard (`Formalization/CIAxiomGuard.lean`, `blueprint/trust-boundary.txt`) admits
twelve axioms, three of them the companion paper's. The isotropic paper claims nine: its seven
cited facts, C3 being three. This script makes that claim a check (Q-0427; the plan's D7, batch
R2; the finding is records/affine/reviews/VERIFY-round1-claims-and-trust-base.md, item 6(b)).

Three sources, none of them typed twice:

* the nine names: `blueprint/trust-boundary-iso.txt`, one per line with the paper's label;
* the declarations: `ROWS` and `PENDING` of records/affine/gen-verification-table.py, that is,
  the \lean tags of the blueprint nodes that Appendix B lists (`gen-verification-table.py check`
  compares `ROWS` with the appendix) and of the nodes that have Lean and are not printed yet;
* the cited facts each statement rests on: `TABLE1` below, typed from the paper's table
  `tab:trust-base`, and `PENDING_FACTS` for the statements not printed yet, from their status
  lines (none since Q-0428 printed the six statements of Q-0427 and Q-0429).

    python records/affine/axioms-iso-all-declarations.py gen
        writes two files from those sources:
        (1) Formalization/AffineHemigroup/IsoAxiomGuard.lean, COMMITTED and part of the library:
            for each statement one command `#iso_axioms <declarations> expects <cited facts>`,
            which fails the build if a declaration depends on an axiom outside Lean's three and
            the nine, or if the union over the statement's declarations is not the listed set.
            The Lean CI job builds the library, so CI runs this check (guard 1, the build);
        (2) Formalization/scratch/axioms_iso_all_declarations.lean (git-ignored): one
            `#print axioms` line per distinct declaration, in the order of Appendix B, from
            which the report is printed.
    python records/affine/axioms-iso-all-declarations.py check
        the committed IsoAxiomGuard.lean equals what `gen` writes now. No Lean is started. Exit 1
        if a \lean tag, the list of nine or Table 1 changed and the file was not regenerated.
    (run from Formalization/, one Lean process at a time, after `lake build`:)
        lake env lean scratch/axioms_iso_all_declarations.lean \
          > ../records/affine/axioms-iso-all-declarations-output.txt 2>&1
    python records/affine/axioms-iso-all-declarations.py table
        reads that report; prints the table statement -> axioms (Markdown), and checks
        (a) every declaration was reported, (b) no declaration names an axiom outside Lean's three
        and the nine, in particular none of the companion paper's three, (c) for each statement
        the union of the axioms of its declarations is the set that Table 1 gives. Exit 1 if a
        check fails.
    python records/affine/axioms-iso-all-declarations.py verify
        for the freeze gates: `check`, then one Lean process on the requests, whose output must
        equal the committed report, then the checks of `table` on it. Writes no tracked file.

After a change to a Lean file, to a \lean tag of a statement of the list, to the nine names or to
Table 1: `gen`, `lake build`, the Lean command above, `table`, and commit the two files.

History. Made for the verification of the external review of iso-review-1 (round 1) as
records/affine/reviews/verify-round1-scripts/axioms_all_144.py, copied here by Q-0424 (141
distinct declarations, Lean 4.31.0, the sources of d3ddc15), and made a guard by Q-0427, which
added the three statements whose Lean it wrote. Q-0429 added its three as pending rows. Q-0428
(at the merge of that Lean) made the six rows of the paper, in its printed order, with their
entries in `TABLE1`: 32 statements, every one printed.
"""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LEAN_DIR = ROOT / "Formalization"
SCRATCH = LEAN_DIR / "scratch" / "axioms_iso_all_declarations.lean"
GUARD = LEAN_DIR / "AffineHemigroup" / "IsoAxiomGuard.lean"
NINE = ROOT / "blueprint" / "trust-boundary-iso.txt"
OUTPUT = HERE / "axioms-iso-all-declarations-output.txt"

LOGIC = ["propext", "Classical.choice", "Quot.sound"]
NS = "AffineHemigroup."
COMPANION = {NS + "operatorSelfDecomposable_infinitelyDivisible", NS + "khintchine_null_array",
             NS + "gelfand_naimark_logMajorized"}

# The paper's table of the cited facts per statement (tab:trust-base, in
# paper-iso/appendix-verification.tex since Q-0428), row by row: the cited facts that the formal
# proof of each statement rests on. "every other statement: none". The table's rows for the
# statements with no formal counterpart (prop:radial-dictionary, cor:dictionary-filtration,
# prop:separating-family-mixtures) are not entries: there is no declaration to compare.
TABLE1 = {
    "thm:isotropic-classification": ["C3(ii)", "C3(iii)"],
    "cor:isotropic-classification-operators": ["C3(ii)", "C3(iii)"],
    # Q-0434, printed since Q-0448 (the corollary after Lemma 3.8): A2, A3, A4, through
    # `prop:isotropic-polar-classification`(2) (the exponent of a rotation-invariant
    # self-decomposable law is admissible) and the necessity direction of
    # `thm:isotropic-classification`
    "cor:isotropic-scale-zero-kernels": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4"],
    "prop:isotropic-polar-reading": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4"],
    "thm:origin-boundedness-d": ["C1"],
    "prop:isotropic-radial-monotone": ["C5", "C3(ii)", "C3(iii)", "C2"],
    "prop:origin-lower-bound-d": ["C3(iii)"],
    "prop:origin-upper-bound-d": ["C3(iii)", "C2", "C5"],
    "prop:origin-rate-d": ["C7", "C2", "C3(iii)", "C5"],
    # Q-0427, printed since Q-0428 (Proposition 3.17): the row "the rate through the profile"
    "prop:origin-rate-profile-d": ["C7", "C2", "C3(iii)", "C5"],
    # Q-0447, a row of the paper since the joining step of Q-0448: the stages, one proposition
    # for three nodes. The declarations of clauses (1) and (2) (the nodes
    # lem:isotropic-stage-levy-measure and prop:isotropic-stage-atom) rest on no cited fact;
    # those of clause (3) (prop:isotropic-stage-density) on A3(iii) in items (a) and (b) and on
    # A1 in item (c), and the closing sentence on both
    "prop:isotropic-stages": ["C1", "C3(iii)"],
    # Q-0429, printed since Q-0428 (Proposition 3.19, in the row of the dictionary, and Theorem
    # 3.21): A2, A3, A4 through the polar form of the classes and the uniqueness of a datum, as
    # `prop:isotropic-polar-reading`
    "prop:profile-one-dimension-down": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4"],
    "thm:separating-family-critical-values": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4"],
    # Q-0448: the row "the bottom of the chain". The node is printed in the place of
    # thm:filtration-strict. Its three declarations: classS_of_classAInf on A10 and A2,
    # A3(i)-(ii), A4; classAInf_of_classS on A2 and A3(iii); filtration_top on the union
    # (the comment above their lines in Formalization/CIAxiomGuard.lean)
    "lem:filtration-top": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4", "C6"],
}
# prop:isotropic-exponent-profile, lem:threshold-asymptotic (Q-0427) and lem:shadow-polar-profile
# (Q-0429), printed since Q-0428 as A.6, A.12 and A.8, rest on no cited fact: they are under the
# table's last row, "every other statement: none", and have no entry, like every such statement.
#
# The statements of `PENDING` (Lean written, not printed by the paper yet, so not in its table):
# the cited facts of their blueprint status lines. A statement not named here rests on none. When
# the paper prints a statement, its row moves to `ROWS` and its entry to `TABLE1`, with the table.
PENDING_FACTS = {
    # Q-0448: not printed by the paper any more, and kept under the guard with the sets that
    # the paper's table gave them while it printed them
    "thm:filtration-strict": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4", "C6"],
    "thm:no-cin-ray-in-the-plane": ["C2", "C3(i)", "C3(ii)", "C3(iii)", "C4"],
}
ORDER = ["C1", "C2", "C3(i)", "C3(ii)", "C3(iii)", "C4", "C5", "C6", "C7"]


def nine():
    """label -> Lean name, from blueprint/trust-boundary-iso.txt."""
    out = {}
    for ln in NINE.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        name, _, label = ln.partition("#")
        out[label.strip()] = name.strip()
    if sorted(out) != sorted(ORDER):
        sys.exit(f"{NINE.name}: the labels are {sorted(out)}, expected {ORDER}")
    return out


C = nine()


def generator():
    path = ROOT / "records" / "affine" / "gen-verification-table.py"
    spec = importlib.util.spec_from_file_location("gen_verification_table", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def statements():
    """[(kind, label, [full Lean names], printed)] in the order of Appendix B, then the pending."""
    g = generator()
    src = g.blueprint()
    out = []
    for printed, rows in ((True, g.ROWS), (False, g.PENDING)):
        for kind, label, nodes in rows:
            names = []
            for node in nodes or [label]:
                for n in g.lean_names(src, node):
                    if n not in names:
                        names.append(n)
            out.append((kind, label, names, printed))
    return out


def expected(label):
    return TABLE1.get(label, PENDING_FACTS.get(label, []))


def distinct(rows):
    seen = []
    for _, _, names, _ in rows:
        for n in names:
            if n not in seen:
                seen.append(n)
    return seen


# Q-0452: the guard and the file of requests import the library of the isotropic paper
# (Formalization/AffineHemigroup/IsotropicLibrary.lean, imports only), where they imported the
# whole library `AffineHemigroup`, so that the closure of the guard holds no file of the affine
# paper and the report is made from the files that the paper's public repository has.
LIBRARY = "AffineHemigroup.IsotropicLibrary"


def requests(rows):
    return f"import {LIBRARY}\n" + "".join(f"#print axioms {n}\n" for n in distinct(rows))


GUARD_HEAD = r'''/-
Copyright (c) 2026 Daniel Fagerström. All rights reserved.
Released under the Apache 2.0 license as described in the file LICENSES/Apache-2.0.txt.
Authors: Daniel Fagerström
-/
import AffineHemigroup.IsotropicLibrary

/-!
# The axiom guard of the isotropic paper

**Generated** by `records/affine/axioms-iso-all-declarations.py gen`; do not edit by hand. The
script's `check` step fails when this file differs from what it generates.

`Formalization/CIAxiomGuard.lean` checks the whole module against `blueprint/trust-boundary.txt`,
twelve axioms, three of which are cited facts of the affine paper. The isotropic paper claims
nine: its seven cited facts, C3 being three (`blueprint/trust-boundary-iso.txt`). This file makes
that claim a build error when it fails. For each statement that Appendix B of the paper lists
(and for a statement whose Lean exists and which the paper does not print yet, when there is
one), one command

  `#iso_axioms <the declarations of the statement> expects <cited facts>`

fails unless (a) every declaration depends only on Lean's three logical axioms and on the nine,
and (b) the cited facts that the declarations reach, taken together, are exactly the listed ones,
which are those of the statement's row in the paper's table of the cited facts per statement, in
its Appendix B (none, when the statement has no row). The declarations are the `\lean` tags of
the blueprint nodes, read by `records/affine/gen-verification-table.py`, which also writes the
appendix's list.

The file is part of the library (nothing imports it), so `lake build`, and with it the Lean CI
job, runs the check. It prints nothing; the report of Lean's `#print axioms` for the same
declarations is `records/affine/axioms-iso-all-declarations-output.txt`. It imports the library
of the isotropic paper, `AffineHemigroup.IsotropicLibrary`, and no other file.
-/

open Lean Elab Command

namespace AffineHemigroup.IsoAxiomGuard

/-- Lean's three logical axioms. -/
def logicalAxioms : List Name := [``propext, ``Classical.choice, ``Quot.sound]

/-- The nine axioms of the isotropic paper: its cited facts C1 to C7, C3 being three. -/
def citedFacts : List Name := [
@@NINE@@]

/-- `#iso_axioms d₁ d₂ … expects a₁ a₂ …`: every declaration `dᵢ` depends only on the logical
axioms and on `citedFacts`, and the cited facts reached by the `dᵢ` together are exactly the
`aⱼ`. -/
syntax (name := isoAxioms) "#iso_axioms " ident* " expects " ident* : command

@[command_elab isoAxioms] def elabIsoAxioms : CommandElab := fun stx => do
  let want := stx[3].getArgs.toList.map (·.getId)
  let mut reached : List Name := []
  for d in stx[1].getArgs do
    let n ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo d
    let axs ← liftCoreM <| collectAxioms n
    for a in axs do
      unless logicalAxioms.contains a do
        unless citedFacts.contains a do
          throwErrorAt d "{n} depends on the axiom {a}, not one of the isotropic paper's nine"
        unless reached.contains a do
          reached := a :: reached
  for a in reached do
    unless want.contains a do
      throwError "the declarations of this statement reach {a}, which its row does not list"
  for a in want do
    unless reached.contains a do
      throwError "the row lists {a}, which no declaration of this statement reaches"

-- the commands below are the content of this file, not leftovers of a proof session
set_option linter.hashCommand false

'''

GUARD_TAIL = "end AffineHemigroup.IsoAxiomGuard\n"


def guard_text(rows):
    head = GUARD_HEAD.replace("@@NINE@@", ",\n".join(f"  ``{C[k]}" for k in ORDER))
    body = []
    pending_said = False
    for kind, label, names, printed in rows:
        if not printed and not pending_said:
            body.append("/-! ## Statements with Lean that the paper does not print -/\n\n")
            pending_said = True
        facts_ = [C[k] for k in ORDER if k in expected(label)]
        body.append(f"-- {kind} `{label}`: " + (", ".join(k for k in ORDER if k in expected(label))
                                                or "no cited fact") + "\n")
        body.append("#iso_axioms\n" + "".join(f"  {n}\n" for n in names)
                    + "  expects" + "".join(f"\n  {a}" for a in facts_) + "\n\n")
    return head + "".join(body) + GUARD_TAIL


def write(path, text):
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def gen():
    rows = statements()
    total = sum(len(n) for _, _, n, _ in rows)
    write(SCRATCH, requests(rows))
    write(GUARD, guard_text(rows))
    print(f"{len(rows)} rows, {total} names, {len(distinct(rows))} distinct")
    print(f"wrote {GUARD.relative_to(ROOT)} (committed) and {SCRATCH.relative_to(ROOT)}")
    print("run from Formalization/:  lake build, then  "
          "lake env lean scratch/axioms_iso_all_declarations.lean")


def check():
    want = guard_text(statements())
    have = GUARD.read_text(encoding="utf-8").replace("\r\n", "\n") if GUARD.exists() else ""
    if have != want:
        print(f"{GUARD.relative_to(ROOT)} differs from what the blueprint's lean tags, "
              f"{NINE.name} and Table 1 generate: run `axioms-iso-all-declarations.py gen`")
        return False
    print(f"{GUARD.relative_to(ROOT)}: equal to what `gen` writes "
          f"({want.count('#iso_axioms' + chr(10))} statements)")
    return True


def parse(text):
    """name -> set of axioms, from Lean's output."""
    text = text.replace("\r\n", "\n")
    got = {}
    for m in re.finditer(r"^'([^']+)' depends on axioms: \[([^\]]*)\]", text, re.M):
        got[m.group(1)] = {a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()}
    for m in re.finditer(r"^'([^']+)' does not depend on any axioms", text, re.M):
        got[m.group(1)] = set()
    return got


def facts(axioms):
    cited = [k for k in ORDER if C[k] in axioms]
    return ", ".join(cited) if cited else "none"


def table(text):
    """The report as Markdown and whether every check passes."""
    rows = statements()
    got = parse(text)
    logic = set(LOGIC)
    ok = True
    lines = []
    problems = []
    lines.append("| statement | declarations | cited facts printed (union) | Table 1 | agrees |")
    lines.append("|---|---:|---|---|---|")
    detail = []
    seen = set()
    for kind, label, names, printed in rows:
        union = set()
        for n in names:
            if n not in got:
                problems.append(f"NOT REPORTED: {n} ({label})")
                ok = False
                continue
            ax = got[n]
            seen.add(n)
            extra = ax - logic - set(C.values())
            if extra:
                problems.append(f"OUTSIDE THE NINE: {n} ({label}): {sorted(extra)}")
                ok = False
            if ax & COMPANION:
                problems.append(f"COMPANION AXIOM: {n} ({label}): {sorted(ax & COMPANION)}")
                ok = False
            union |= ax
            detail.append((label, n, ax))
        want = {C[k] for k in expected(label)}
        have = union - logic
        agrees = have == want
        if not agrees:
            ok = False
            problems.append(f"TABLE 1 DIFFERS: {label}: Lean {facts(have)}; Table 1 {facts(want)}")
        where = "" if printed else " (not printed yet; from its status line)"
        lines.append(f"| {kind} `{label}` | {len(names)} | {facts(have)} | {facts(want)}{where} | "
                     f"{'yes' if agrees else 'NO'} |")
    lines.append("")
    lines.append("| statement | declaration | logical axioms | cited facts |")
    lines.append("|---|---|---|---|")
    for label, n, ax in detail:
        lg = ", ".join(a for a in LOGIC if a in ax) or "none"
        lines.append(f"| `{label}` | `{n}` | {lg} | {facts(ax)} |")
    used = set().union(*[ax for _, _, ax in detail]) - logic
    summary = [
        f"rows: {len(rows)} ({sum(1 for r in rows if r[3])} printed by the paper, "
        f"{sum(1 for r in rows if not r[3])} not yet); "
        f"names: {sum(len(n) for _, _, n, _ in rows)}; distinct: {len(seen)}; "
        f"reported by Lean: {len(got)}",
        "cited facts named by at least one declaration: " + facts(used),
        "cited facts named by none: " + (", ".join(k for k in ORDER if C[k] not in used) or "none"),
        "companion axioms named: " + (", ".join(sorted(used & COMPANION)) or "none"),
        "declarations on no axiom at all: "
        + str(sum(1 for n in seen if not got[n])),
        "declarations on Lean's logical axioms only: "
        + str(sum(1 for n in seen if got[n] and not (got[n] - logic))),
        "declarations naming a cited fact: " + str(sum(1 for n in seen if got[n] - logic)),
    ]
    out = "\n".join(summary) + "\n\n" + "\n".join(lines) + "\n"
    if problems:
        out += "\nPROBLEMS\n" + "\n".join(problems) + "\n"
    return out, ok


def verify():
    ok = check()
    rows = statements()
    write(SCRATCH, requests(rows))
    p = subprocess.run(["lake", "env", "lean", "scratch/axioms_iso_all_declarations.lean"],
                       cwd=LEAN_DIR, capture_output=True, text=True, encoding="utf-8")
    fresh = (p.stdout + p.stderr).replace("\r\n", "\n")
    print(f"lake env lean scratch/axioms_iso_all_declarations.lean: exit {p.returncode}")
    if p.returncode != 0:
        sys.stderr.write(fresh[-3000:])
        return False
    saved = OUTPUT.read_text(encoding="utf-8").replace("\r\n", "\n")
    if fresh != saved:
        print(f"Lean's output differs from the committed report {OUTPUT.name}: "
              "save the new output and commit it")
        ok = False
    else:
        print(f"Lean's output equals the committed report ({len(parse(fresh))} declarations)")
    text, table_ok = table(fresh)
    print("\n".join(text.splitlines()[:7]))
    if not table_ok:
        print(text[text.find("PROBLEMS"):] if "PROBLEMS" in text else "")
    return ok and table_ok


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "gen":
        gen()
    elif mode == "check":
        sys.exit(0 if check() else 1)
    elif mode == "table":
        text_, ok_ = table(open(OUTPUT, encoding="utf-8").read())
        print(text_)
        print("ALL CHECKS PASS" if ok_ else "A CHECK FAILED")
        sys.exit(0 if ok_ else 1)
    elif mode == "verify":
        good = verify()
        print("ALL CHECKS PASS" if good else "A CHECK FAILED")
        sys.exit(0 if good else 1)
    else:
        sys.exit(__doc__)
