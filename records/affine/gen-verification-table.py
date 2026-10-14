r"""Q-0414, round 3: the table of Appendix B of the isotropic paper, statement by statement with the
Lean declarations behind it, from the blueprint's \lean tags.

The appendix listed the machine-checked statements by number only (the register review of
2026-10-11b, flag 36: "make it the table a reproducer needs, statement and name of its Lean
declaration"). The rows are generated, never typed: for each statement of section 3 and of
Appendix A that has a formal counterpart, in printed order, the declarations of the \lean tag of
its blueprint node (the paper's Lemma lem:operators-to-kernels renders two nodes, and gets both
tags). The namespace AffineHemigroup is dropped from the names, and the table says so; a name of
the shared library keeps its namespace ScaleSpace.

Q-0428 (2026-10-12, at the merge of the Lean of Q-0429): the list has an item for every statement
of the paper that is machine-checked, 32, in the order of the paper as rewritten in that item.
The six statements formalized in Q-0427 and Q-0429 are rows (they were `PENDING` until the paper
printed them), and the rows that the rewrite moved to Appendix A stand at their new places: the
two bounds (A.4, A.5), the strict filtration (A.15) and the Cin rays (A.16). The four statements
that the paper prints and that have no \lean tag are not rows: prop:radial-dictionary (3.18),
lem:exponent-profile-constant (A.7), cor:dictionary-filtration (A.9) and
prop:separating-family-mixtures (A.14); section 1.1 of the paper lists them.

The rows are the items of a list, not of a table: the names do not fit one page, and a list
breaks across pages. Each item carries its status in words, "machine-checked" or, for a
definition, "formalised in Lean": `linkage check` reads the region of the appendix in rows (an
\item is one) and compares the status that a row gives a \ref'd statement with the blueprint's
\leanok (LINKAGE.md rule 13).

    python records/affine/gen-verification-table.py write    # replace the rows in the appendix
    python records/affine/gen-verification-table.py check    # exit 1 if the appendix differs

Q-0448 (the split of the paper into a paper and a supplement): the list is in the supplement,
paper-iso/supp-verification.tex (section S4; Appendix F of the full document), and its rows are
in the order of the paper: section 3, Appendix A, then the statements of the supplement.

The rows stand in paper-iso/supp-verification.tex between the comment lines
"% verification table: begin" and "% verification table: end". Run from the repository root.
"""
import glob
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "paper-iso" / "supp-verification.tex"
BS = chr(92)
BEGIN = "% verification table: begin\n"
END = "% verification table: end\n"

# (kind as printed, paper label, blueprint nodes), in the order in which the paper prints them.
# The numbers in the comments are those of the build of Q-0428 (paper-iso/main.aux); they are not
# read, and say only where a row stands.
ROWS = [
    ("Def.", "def:isotropic-operator-family", None),            # 3.1
    ("Def.", "def:isotropic-kernel-family", None),              # 3.2
    ("Lemma", "lem:operators-to-kernels", ["lem:operators-to-kernels", "lem:kernels-to-operators"]),
    ("Lemma", "lem:radial-marginal", None),                     # 3.4
    ("Lemma", "lem:isotropic-marginal-family", None),           # 3.5
    ("Thm.", "thm:isotropic-classification", None),             # 3.6
    ("Cor.", "cor:isotropic-classification-operators", None),   # 3.7
    ("Lemma", "lem:isotropic-realisation", None),               # 3.8
    ("Cor.", "cor:isotropic-scale-zero-kernels", None),         # 3.9 (Q-0434; printed since Q-0448)
    ("Def.", "def:isotropic-origin-datum", None),               # 3.9
    ("Prop.", "prop:isotropic-polar-reading", None),            # 3.10
    ("Prop.", "prop:isotropic-bridge", None),                   # 3.11
    ("Thm.", "thm:origin-boundedness-d", None),                 # 3.12
    ("Cor.", "cor:origin-profile-exponent", None),              # 3.13
    ("Prop.", "prop:isotropic-radial-monotone", None),          # 3.14
    ("Prop.", "prop:isotropic-exponent-profile", None),         # 3.15 (Q-0427; in 3.3 since Q-0448)
    ("Prop.", "prop:origin-rate-profile-d", None),              # 3.17 (Q-0427)
    # the stages of a cascade, 3.20: one proposition of the paper for three blueprint nodes
    # (Q-0434; machine-checked since Q-0447; a row since the joining step of Q-0448)
    ("Prop.", "prop:isotropic-stages", ["lem:isotropic-stage-levy-measure",
                                         "prop:isotropic-stage-atom",
                                         "prop:isotropic-stage-density"]),
    ("Prop.", "prop:profile-one-dimension-down", None),         # 3.19 (Q-0429)
    ("Def.", "def:filtration-thresholds", None),                # 3.20
    ("Thm.", "thm:separating-family-critical-values", None),    # 3.21 (Q-0429)
    # Appendix A of the paper
    ("Lemma", "lem:polar-decomposition", None),
    ("Lemma", "lem:isotropic-exponent-log", None),
    ("Prop.", "prop:origin-lower-bound-d", None),
    ("Prop.", "prop:origin-upper-bound-d", None),
    ("Lemma", "lem:shadow-polar-profile", None),                # (Q-0429)
    ("Lemma", "lem:delay-polar-profile", None),
    # the supplement (supp-proofs.tex)
    ("Lemma", "lem:positive-transform-origin", None),
    ("Lemma", "prop:origin-rate-d", None),                      # the rate through the transform,
                                                                # a lemma of the supplement (Q-0448)
    ("Lemma", "lem:threshold-monotone", None),
    ("Lemma", "lem:threshold-limit", None),
    ("Lemma", "lem:threshold-asymptotic", None),                # (Q-0427)
    ("Lemma", "lem:filtration-top", None),                      # printed since Q-0448, in the
                                                                # place of thm:filtration-strict
]

# Statements of the isotropic paper whose blueprint node has a \lean tag and which the paper does
# not print yet. They are not rows of the appendix, so `write` and `check` do not read them; the
# paper's axiom guard and report (records/affine/axioms-iso-all-declarations.py) do. When the
# paper prints one, its row moves to `ROWS`, at its place in the printed order, with the kind the
# paper gives it. Empty from Q-0428, which printed the six of Q-0427 and Q-0429, until Q-0434
# (the main result as one statement, a corollary after Lemma 3.8 when the paper prints it).
# Q-0448: two statements of the blueprint with Lean that the paper does not print and will not
# (the author's decision of 2026-10-13, on the second external round): thm:filtration-strict,
# whose content the paper has as Theorem thm:separating-family-critical-values(4), Proposition
# prop:profile-one-dimension-down(2) and Lemma lem:filtration-top, and
# thm:no-cin-ray-in-the-plane, which is clause (3) of that proposition and whose proof the
# paper keeps as a second proof of the clause. They stay under the axiom guard.
# The three nodes on the stages of a cascade (Q-0434) are \leanok since queue item Q-0447. They
# are one row of `ROWS`, after prop:origin-rate-profile-d, which is its place in the paper, with
# the entry of the paper's table in `TABLE1` of axioms-iso-all-declarations.py.
PENDING = [
    ("Thm.", "thm:filtration-strict", None),                    # not printed (Q-0448)
    ("Thm.", "thm:no-cin-ray-in-the-plane", None),              # not printed (Q-0448)
]


def blueprint() -> str:
    files = sorted(glob.glob(str(ROOT / "blueprint" / "src" / "**" / "*.tex"), recursive=True))
    return "\n".join(io.open(f, encoding="utf-8").read() for f in files)


def lean_names(src: str, node: str) -> list[str]:
    at = src.find(BS + "label{" + node + "}")
    if at < 0:
        sys.exit(f"no blueprint node {node}")
    m = re.search(re.escape(BS) + r"lean\{([^}]*)\}", src[at:at + 6000])
    if m is None:
        sys.exit(f"no {BS}lean tag after {node}")
    return [n.strip() for n in m.group(1).replace("\n", " ").split(",") if n.strip()]


def tex_name(name: str) -> str:
    if name.startswith("AffineHemigroup."):
        name = name[len("AffineHemigroup."):]
    return BS + "texttt{" + name.replace("_", BS + "_") + "}"


def rows() -> str:
    src = blueprint()
    out = []
    for kind, label, nodes in ROWS:
        names: list[str] = []
        for node in nodes or [label]:
            for n in lean_names(src, node):
                if n not in names:
                    names.append(n)
        status = "formalised in Lean" if kind == "Def." else "machine-checked"
        out.append(f"{BS}item {kind}~{BS}ref{{{label}}}, {status}:\n  "
                   + ", ".join(tex_name(n) for n in names) + ".\n")
    return "".join(out)


def split(text: str) -> tuple[str, str, str]:
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        sys.exit("the appendix does not have the two marker lines once each")
    i = text.index(BEGIN) + len(BEGIN)
    j = text.index(END)
    return text[:i], text[i:j], text[j:]


def main() -> None:
    raw = io.open(APP, encoding="utf-8", newline="").read()
    eol = "\r\n" if "\r\n" in raw else "\n"
    head, body, tail = split(raw.replace("\r\n", "\n"))
    want = rows()
    if sys.argv[1:] == ["write"]:
        io.open(APP, "w", encoding="utf-8", newline="").write(
            (head + want + tail).replace("\n", eol))
        print(f"{len(ROWS)} rows written, {want.count(BS + 'texttt{')} declarations")
    elif sys.argv[1:] == ["check"]:
        if body != want:
            sys.exit("the list of the supplement differs from the blueprint's lean tags: "
                     "run `gen-verification-table.py write`")
        print(f"{len(ROWS)} rows, {want.count(BS + 'texttt{')} declarations: "
              "equal to the blueprint's lean tags")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
