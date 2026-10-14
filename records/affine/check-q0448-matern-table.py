"""Q-0448: the numbers of the table of Example ex:matern of the isotropic paper (the Matern kernel
of index gamma = 3/4, the kernel of Figure 1, in dimensions 1, 2 and 3), computed from the
statements the example quotes and checked against the closed form of the density.

    uv run --no-project --with mpmath python records/affine/check-q0448-matern-table.py

For each d: the polar profile k_d(r) = (4 gamma / Gamma(d/2)) (r / sqrt 2)^(d/2) K_(d/2)(sqrt 2 r)
(checked against the integral eq:polar-profile-d with the delay profile gamma e^(-u)); the
constants C_k = int_1^inf k_d dr/r and K(0+) = exp int_0^1 (c - k_d) du/u of Proposition
prop:isotropic-exponent-profile; varkappa_d of Lemma lem:exponent-profile-constant(3);
A = exp(-C_k - c varkappa_d), with the identity A K(0+) = 2^gamma; for c < d the constant
Q = R(d, c) A of Proposition prop:origin-rate-profile-d(1) and the coefficient Q K(0+) of the
pure power (its clause (2)), against Gamma(d/2 - gamma) / (2^gamma pi^(d/2) Gamma(gamma)) and
against the closed form eq:matern-density at a small radius; for c > d the value at the centre
(2 pi)^(-d/2) Gamma(gamma - d/2) / Gamma(gamma), against the closed form at a small radius.
Exits 1 if an identity fails.
"""
import sys

from mpmath import besselk, digamma, euler, exp, gamma, inf, log, mp, mpf, pi, quad, sqrt

mp.dps = 30
G = mpf(3) / 4
C = 2 * G
ok = True


def profile(d, r):
    return 4 * G / gamma(mpf(d) / 2) * (r / sqrt(2)) ** (mpf(d) / 2) * besselk(mpf(d) / 2, sqrt(2) * r)


def profile_integral(d, r):
    f = lambda v: v ** (mpf(d) / 2 - 1) * exp(-v) * G * exp(-r * r / (2 * v))
    return 2 / gamma(mpf(d) / 2) * quad(f, [0, 1, inf])


def density(d, x):
    nu = G - mpf(d) / 2
    return 2 / ((2 * pi) ** (mpf(d) / 2) * gamma(G)) * (x / sqrt(2)) ** nu * besselk(nu, sqrt(2) * x)


def close(a, b, tol, what):
    global ok
    good = abs(a - b) <= tol * max(abs(a), abs(b))
    ok = ok and good
    print(f"    {'ok ' if good else 'FAIL'} {what}: {mp.nstr(a, 8)} against {mp.nstr(b, 8)}")


print(f"the Matern kernel of index gamma = {G}, c = 2 gamma = {C}")
for d in (1, 2, 3):
    print(f"\nd = {d}")
    close(profile(d, mpf("0.7")), profile_integral(d, mpf("0.7")), mpf("1e-12"),
          "polar profile, closed form against eq:polar-profile-d at r = 0.7")
    ck = quad(lambda r: profile(d, r) / r, [1, 4, inf])
    k0 = exp(quad(lambda u: (C - profile(d, u)) / u, [0, mpf("1e-6"), mpf("1e-3"), mpf("0.1"), 1]))
    kappa = (euler - digamma(mpf(d) / 2)) / 2 - log(2)
    a = exp(-ck - C * kappa)
    print(f"    C_k = {mp.nstr(ck, 5)}   K(0+) = {mp.nstr(k0, 5)}   varkappa_d = {mp.nstr(kappa, 5)}"
          f"   A = {mp.nstr(a, 5)}")
    close(a * k0, 2 ** G, mpf("1e-8"), "A K(0+) against 2^gamma")
    if C < d:
        r_dc = gamma((d - C) / 2) / (2 ** C * pi ** (mpf(d) / 2) * gamma(C / 2))
        q = r_dc * a
        coeff = gamma(mpf(d) / 2 - G) / (2 ** G * pi ** (mpf(d) / 2) * gamma(G))
        print(f"    R(d,c) = {mp.nstr(r_dc, 5)}   Q = {mp.nstr(q, 5)}   Q K(0+) = {mp.nstr(q * k0, 5)}")
        close(q * k0, coeff, mpf("1e-8"), "Q K(0+) against the coefficient in closed form")
        # the next term of the density at the centre is of relative order |x|^(d-c), which is
        # 1e-4 at d = 2 and |x| = 1e-8: the tolerance is ten times that
        x = mpf("1e-8")
        close(density(d, x) * x ** (d - C), coeff, 10 * x ** (d - C),
              "p(x) |x|^(d-c) at |x| = 1e-8 against the coefficient")
    else:
        centre = (2 * pi) ** (-mpf(d) / 2) * gamma(G - mpf(d) / 2) / gamma(G)
        print(f"    bounded: the value at the centre is {mp.nstr(centre, 5)}")
        close(density(d, mpf("1e-12")), centre, mpf("1e-5"), "p at |x| = 1e-12 against that value")

print("\nALL IDENTITIES HOLD" if ok else "\nAN IDENTITY FAILS")
sys.exit(0 if ok else 1)
