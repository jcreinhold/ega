<!-- original page 135 -->

## §17. Regular rings

### 17.1. Definition of regular rings

**Proposition (17.1.1).**

<!-- label: 0_IV.17.1.1 -->

*Let `A` be a Noetherian local ring of dimension `n`, `𝔪` its maximal ideal, `k = A/𝔪` its residue field. The following
conditions are equivalent:*

*a) The canonical surjective homomorphism of graded `k`-modules `(15.1.1.1)`*

```text
                                φ : S_•(𝔪/𝔪²) → gr_𝔪(A)
```

*(where the right-hand side is the graded `k`-module associated with `A` equipped with the `𝔪`-preadic filtration) is
bijective.*

*b) One has `rg_k(𝔪/𝔪²) = n`.*

*c) The ideal `𝔪` admits a system of generators with `n` elements.*

*d) The ideal `𝔪` admits a system of generators which is an `A`-regular sequence.*

By Nakayama's lemma, `rg_k(𝔪/𝔪²)` is the smallest number of elements in a system of generators of `𝔪`, so b) and c) are
equivalent. On the other hand, if `(x_i)_{1 ≤ i ≤ n}` is a system of generators of `𝔪` whose classes `x̄_i mod 𝔪²` form
a basis of the `k`-vector space `𝔪/𝔪²`, then `S_•(𝔪/𝔪²)` is isomorphic to the polynomial ring

<!-- original page 136 -->

`k[T_1, …, T_n]`; taking into account that every `A`-module of finite type is separated for the `𝔪`-preadic filtration
`(0_I, 7.3.5)`, it follows from `(15.1.9)` that conditions a) and d) are equivalent; furthermore, since every
`A`-regular sequence of elements of `𝔪` has at most `n` elements `(16.4.1)`, one sees that d) implies c). It remains to
prove that c) implies a). For brevity put `S = S_•(𝔪/𝔪²) = k[T_1, …, T_n]`, `G = gr_𝔪(A)`, and consider the exact
sequence `0 → 𝔍 → S →^φ G → 0`, where the kernel `𝔍` of `φ` is a graded ideal of `S`. For every integer `s ≥ 0` one has
therefore

```text
(17.1.1.1)               C(s+n-1, n-1) = long(S_s) = long(G_s) + long(𝔍_s).
```

Suppose `𝔍 ≠ 0`, so that there exists a homogeneous element `u ∈ 𝔍` of degree `h ≥ 0`; `𝔍_s` contains `u S_{s-h}` for
`s ≥ h`, and since `u ≠ 0` and `S` is an integral domain, `u S_{s-h}` is isomorphic to `S_{s-h}` as a `k`-vector space;
one would therefore have `long(𝔍_s) ≥ long(S_{s-h}) = C(s-h+n-1, n-1)`, whence for `s ≥ h`,

```text
(17.1.1.2)              long(G_s) ≤ C(s+n-1, n-1) − C(s-h+n-1, n-1).
```

Now, the right-hand side of `(17.1.1.2)` is a polynomial in `s` of degree `≤ n-2`; but one has `G_s = 𝔪^s/𝔪^{s+1}`, and
for `s` large enough, `long(G_s)` is a polynomial in `s` of degree exactly equal to `n-1` whose leading coefficient is
`> 0` `(16.2.1)`, which contradicts the inequality `(17.1.1.2)`. Q.E.D.

**Definition (17.1.2).**

<!-- label: 0_IV.17.1.2 -->

*One says that a Noetherian local ring which satisfies the equivalent conditions of `(17.1.1)` is **regular**.*

**Corollary (17.1.3).**

<!-- label: 0_IV.17.1.3 -->

*A regular local ring is an integral domain, integrally closed, and a Cohen-Macaulay ring.*

The last assertion follows from `(17.1.1, d))`; on the other hand, if `A` is regular, `gr_𝔪(A)` is an integral domain
and completely integrally closed, being isomorphic to `k[T_1, …, T_n]`; one concludes that `A` also possesses these two
properties `(Bourbaki, Alg. comm., chap. III, §2, n° 3, cor. of prop. 1 and chap. V, §1, n° 5, prop. 15)`.

**Examples (17.1.4).** — (i) A regular local ring of dimension `0`, being an integral domain by `(17.1.3)`, is
necessarily a field, and conversely.

(ii) For a Noetherian local ring of dimension `1` to be regular, it is necessary and sufficient that it be a *discrete
valuation ring*: indeed, to say that a Noetherian local ring of dimension `1` is regular means that its maximal ideal is
principal, and the conclusion follows from `Bourbaki, Alg. comm., chap. VI, §3, n° 6, prop. 9`.

(iii) Let `k` be a field; the ring of formal power series `A = k[[T_1, …, T_n]]` is a *regular ring of dimension `n`*;
indeed, it is clear that the `T_i` `(1 ≤ i ≤ n)` generate the maximal ideal `𝔪` of `A` and form an `A`-regular sequence,
since `A/(T_1 A + ⋯ + T_i A)` is isomorphic to `k[[T_{i+1}, …, T_n]]`.

**Proposition (17.1.5).**

<!-- label: 0_IV.17.1.5 -->

*For a Noetherian local ring `A` to be regular, it is necessary and sufficient that its completion `Â` be so.*

<!-- original page 137 -->

Indeed, the maximal ideal of `Â` is `𝔪Â`, and one knows that `𝔪^h/𝔪^{h+1}` and `(𝔪Â)^h/(𝔪Â)^{h+1}` are isomorphic
`k`-vector spaces; condition a) of `(17.1.1)` is therefore the same for `A` and `Â`.

**Definition (17.1.6).**

<!-- label: 0_IV.17.1.6 -->

*Given a Noetherian local ring `A` with maximal ideal `𝔪`, one calls a **regular system of parameters** of `A` a system
of parameters for `A` `(16.3.5)` that generates `𝔪`.*

The existence of such a system is equivalent to the fact that `A` is regular `(17.1.1)`; if `(x_i)_{1 ≤ i ≤ n}` is a
regular system of parameters, it is a minimal system of generators of `𝔪`, whose classes mod `𝔪²` form a basis of `𝔪/𝔪²`
over `k`; by virtue of `(17.1.1, a))` and `(15.1.9)`, `(x_i)` is a maximal `A`-regular sequence (whence the
terminology).

One should beware, however, that in a regular ring, a system of parameters for `A` which is also an `A`-regular sequence
is not necessarily a regular system of parameters, as the example of the `k`-th powers of a regular system of parameters
shows `(15.1.20)`.

**Proposition (17.1.7).**

<!-- label: 0_IV.17.1.7 -->

*Let `A` be a Noetherian local ring, `𝔪` its maximal ideal, `k = A/𝔪` its residue field, `(x_i)_{1 ≤ i ≤ r}` a sequence
of elements of `𝔪`, `𝔍 = x_1 A + ⋯ + x_r A`. The following conditions are equivalent:*

*a) `A` is regular and the `x_i` are part of a regular system of parameters of `A`.*

*a′) `A` is regular and the classes `x̄_i` of the `x_i` mod `𝔪²` are linearly independent over `k`.*

*b) The `x_i` are part of a system of parameters for `A` and `A/𝔍` is a regular ring.*

*Moreover, when these conditions are satisfied, `𝔍` is a prime ideal.*

The last assertion follows trivially from the fact that `A/𝔍`, being regular, is an integral domain `(17.1.3)`. Put
`n = dim(A)`. The equivalence of a) and a′) is immediate; indeed, the classes mod `𝔪²` of the elements of a regular
system of parameters form a basis of `𝔪/𝔪²` over `k`, and conversely, if the `x̄_i` `(1 ≤ i ≤ r)` are linearly
independent over `k`, one can find `n - r` elements `x_i ∈ 𝔪` `(r + 1 ≤ i ≤ n)` such that the `x̄_i` `(1 ≤ i ≤ n)` form
a basis of `𝔪/𝔪²`, hence `(x_i)_{1 ≤ i ≤ n}` is a regular system of parameters. To see that a) implies b), let us remark
that since the `x_i` are part of a system of parameters of `A`, one has `dim(A/𝔍) = n - r` `(16.3.6)`; let `𝔫 = 𝔪/𝔍` be
the maximal ideal of `A/𝔍`. One has an exact sequence

```text
(17.1.7.1)              0 → (𝔪² + 𝔍)/𝔪² → 𝔪/𝔪² → 𝔫/𝔫² → 0
```

since `𝔫² = (𝔪² + 𝔍)/𝔍`; hypothesis a) implies that `rg_k((𝔪² + 𝔍)/𝔪²) = r`, hence `rg_k(𝔫/𝔫²) = n - r = dim(A/𝔍)`,
which proves b) by virtue of `(17.1.1, b))`.

Conversely, to prove that b) implies a), note that the fact that the `x_i` are part of a system of parameters implies
that `dim(A/𝔍) = n - r` `(16.3.6)`; on the other hand, the hypothesis that `A/𝔍` is regular implies `rg_k(𝔫/𝔫²) = n - r`
`(17.1.1)`; moreover one obviously has `rg_k((𝔪² + 𝔍)/𝔪²) ≤ r`, so one deduces from `(17.1.7.1)` that
`rg_k(𝔪/𝔪²) ≤ r + (n - r) = n`; hence `A` is regular by virtue of `(16.2.6)` and `(17.1.1)`. Furthermore, the relation
`rg_k(𝔪/𝔪²) = n` then implies `rg_k((𝔪² + 𝔍)/𝔪²) = r`, and consequently the `x̄_i` are linearly independent over `k`.
Q.E.D.

<!-- original page 138 -->

**Corollary (17.1.8).**

<!-- label: 0_IV.17.1.8 -->

*Let `A` be a Noetherian local ring, `𝔪` its maximal ideal, `t` an element of `𝔪`. The following conditions are
equivalent:*

*a) `A/tA` is regular and `t` is not a zero-divisor in `A`.*

*b) `A` is regular and `t ∉ 𝔪²`.*

This is the special case `r = 1` of `(17.1.7)` (taking into account that an element of `𝔪` which is not a zero-divisor
is part of a system of parameters `(16.4.1)`).

**Corollary (17.1.9).**

<!-- label: 0_IV.17.1.9 -->

*Let `A` be a regular local ring, `𝔪` its maximal ideal, `𝔍` an ideal of `A` contained in `𝔪`. The following conditions
are equivalent:*

*a) The ring `A/𝔍` is regular.*

*b) `𝔍` is generated by a sequence `(x_i)_{1 ≤ i ≤ r}` which is part of a regular system of parameters of `A`.*

We have already seen `(17.1.7)` that b) implies a). Conversely, suppose `A/𝔍` is regular (which implies that `𝔍` is
prime) and let `n = dim(A)`, `n - r = dim(A/𝔍)`; with the notations of `(17.1.7)`, the exact sequence `(17.1.7.1)` gives
`rg_k((𝔪² + 𝔍)/𝔪²) = r`, hence there exists a sequence `(x_i)_{1 ≤ i ≤ r}` of elements of `𝔍` that is part of a regular
system of parameters of `A`. Put `𝔍′ = x_1 A + ⋯ + x_r A`; it follows from `(17.1.7)` that `𝔍′` is a prime ideal of `A`
and that `A/𝔍′` is regular and of dimension `n - r`; but since `A/𝔍 = (A/𝔍′)/(𝔍/𝔍′)` and `𝔍/𝔍′` is prime in the integral
domain `A/𝔍′`, the dimensions of `A/𝔍` and `A/𝔍′` can be equal only if `𝔍 = 𝔍′` `(16.1.2.2)`.

### 17.2. Recollections on the projective dimension and the injective dimension of modules

**(17.2.1)** Let `A` be a ring, `M` an `A`-module. Recall `(M, VI, 2)` that one calls the *projective dimension* (resp.
*injective dimension*) of `M`, and denotes by `dim. proj(M)` or `dim. proj_A(M)` (resp. `dim. inj(M)` or
`dim. inj_A(M)`), the smallest `n` (an integer or equal to `+∞`) such that there exists a left projective resolution
(resp. a right injective resolution) of `M` of length `n`. It comes to the same thing *(loc. cit.)* to say that `n` is
the smallest number such that for every `A`-module `N`, one has `Ext^i_A(M, N) = 0` (resp. `Ext^i_A(N, M) = 0`) for
every `i > n`, or only for `i = n + 1`. For every direct factor `M'` of `M`, one therefore has
`dim. proj(M') ≤ dim. proj(M)` since `Ext^i_A(M', N)` is a direct factor of `Ext^i_A(M, N)`; similarly
`dim. inj(M') ≤ dim. inj(M)`. An equivalent condition to `dim. proj(M) = n` (resp. `dim. inj(M) = n`) is that `n` is the
smallest number such that, for every exact sequence

```text
                        0 → R → P_{n-1} → ⋯ → P_0 → M → 0
```

(resp. `0 → M → Q_0 → ⋯ → Q_{n-1} → C → 0`), where all the `P_i` for `0 ≤ i < n` are projective (resp. all the `Q_i` for
`0 ≤ i < n` are injective), `R` is projective (resp. `C` is injective).

**Remarks (17.2.2).** — (i) To say that `M` is a projective (resp. injective) `A`-module is therefore equivalent to
saying that `dim. proj(M) = 0` (resp. `dim. inj(M) = 0`).

(ii) Let `T` be an additive covariant functor from the category of `A`-modules to an abelian category. It follows at
once from the definitions of `(17.2.1)` and from that of

<!-- original page 139 -->

derived functors that if `dim. proj(M) ≤ n` (resp. `dim. inj(M) ≤ n`), one has `L_i T(M) = 0` (resp. `R^i T(M) = 0`) for
every `i > n`.

(iii) If one assumes `A` Noetherian and `M` of finite type, the last interpretation of the projective dimension given in
`(17.2.1)` shows that if `dim. proj(M) = n`, then `M` admits a left resolution of length `n` formed of projective
modules *of finite type*. If moreover `A` is a Noetherian local ring, `M` admits a resolution of length `n` by *free
modules of finite type*, a projective `A`-module of finite type being then free
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`.

**Lemma (17.2.3).**

<!-- label: 0_IV.17.2.3 -->

*Let `A` be a ring, `M` an `A`-module. For `dim. inj(M) ≤ n`, it is necessary and sufficient that for every monogenic
`A`-module `N`, one have `Ext^{n+1}_A(N, M) = 0`.*

With the notations of `(17.2.1)`, it suffices to prove that `C` is injective; for every `A`-module `N`,
`Ext^{n+1}_A(N, M)` is isomorphic to `Ext^1_A(N, C)` `(M, V, 7)`, so one has `Ext^1_A(N, C) = 0` for every `A`-module
`N` of the form `A/𝔍`, where `𝔍` is an arbitrary ideal of `A`. The exact sequence of Ext then shows that the canonical
homomorphism `Hom(A, C) → Hom(𝔍, C)` is surjective for every ideal `𝔍` of `A`, which implies that `C` is an injective
`A`-module `(M, I, 3.2)`.

**Lemma (17.2.4).**

<!-- label: 0_IV.17.2.4 -->

*Let `A` be a Noetherian ring, `M` an `A`-module of finite type. For `dim. proj(M) ≤ n`, it is necessary and sufficient
that for every monogenic `A`-module `N`, one have `Ext^{n+1}_A(M, N) = 0`.*

One knows indeed `(M, VI, 2.5)` that the condition `dim. proj(M) ≤ n` is equivalent to `Ext^{n+1}_A(M, N) = 0` for every
`A`-module `N` of finite type. To see that the condition of the statement is also sufficient, one argues by induction on
the number of generators `m` of `N`: there is a submodule `N_1` of `N` generated by `m - 1` elements and such that
`N_2 = N/N_1` is monogenic; from the exact sequence `0 → N_1 → N → N_2 → 0`, one then deduces the exact sequence
`Ext^{n+1}_A(M, N_1) → Ext^{n+1}_A(M, N) → Ext^{n+1}_A(M, N_2)`, and the induction hypothesis shows that the condition
of the statement does indeed imply `Ext^{n+1}_A(M, N) = 0`.

**Corollary (17.2.5).**

<!-- label: 0_IV.17.2.5 -->

*Let `A` be a Noetherian ring, `M` an `A`-module. One has*

```text
(17.2.5.1)              dim. inj_A(M) = sup_𝔪(dim. inj_{A_𝔪}(M_𝔪))
```

*and if `M` is of finite type*

```text
(17.2.5.2)              dim. proj_A(M) = sup_𝔪(dim. proj_{A_𝔪}(M_𝔪))
```

*where `𝔪` runs through the set of prime ideals (or the set of maximal ideals) of `A`.*

Indeed, if `N` is an `A`-module of finite type (hence of finite presentation), one has, for every multiplicative subset
`S` of `A` and every `i ≥ 0`,

```text
                        S^{-1} Ext^i_A(N, M) ≅ Ext^i_{S^{-1} A}(S^{-1} N, S^{-1} M)
```

by flatness, considering a free resolution of `M` and using the fact that the preceding relation is true for `i = 0`
`(Bourbaki, Alg. comm., chap. II, §2, n° 7, prop. 19)`. In particular
`Ext^i_{A_𝔪}(A_𝔪/𝔍 A_𝔪, M_𝔪) = (Ext^i_A(A/𝔍, M))_𝔪` for every prime ideal `𝔪` and every ideal `𝔍` of `A`; taking
`(17.2.3)` into account, and the fact that every

<!-- original page 140 -->

ideal of `A_𝔪` is of the form `𝔍 A_𝔪` for a suitable ideal `𝔍` of `A`, one deduces formula `(17.2.5.1)` from what
precedes and from `Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1`. One proceeds similarly for `(17.2.5.2)`, this time
using `(17.2.4)` and exchanging the roles of `M` and `N`.

For Noetherian rings and modules of finite type, the study of projective dimension or injective dimension is therefore
reduced by `(17.2.5)` to the case of *local* rings. One then has the following:

**Lemma (17.2.6).**

<!-- label: 0_IV.17.2.6 -->

*Let `A` be a Noetherian local ring, `k` its residue field, `M` an `A`-module of finite type. For `dim. proj(M) ≤ n`, it
is necessary that `Tor^A_i(M, k) = 0` for `i > n`, and sufficient that `Tor^A_{n+1}(M, k) = 0`.*

Necessity is a special case of remark `(17.2.2, (ii))`, applied to the covariant functor `M ↦ k ⊗_A M`. To prove that
the condition is sufficient, one must, with the notations of `(17.2.1)`, establish that `R` is projective when the `P_i`
are assumed of finite type; now `Tor^A_{n+1}(M, k)` is isomorphic to `Tor^A_1(R, k)` `(M, V, 7)`; and one knows that,
since `R` is of finite type, the condition `Tor^A_1(R, k) = 0` implies that `R` is free
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`.

**Corollary (17.2.7).**

<!-- label: 0_IV.17.2.7 -->

*Under the hypotheses of `(17.2.6)`, let `x` be an `M`-regular element of `A` belonging to the maximal ideal of `A`;
then one has*

```text
(17.2.7.1)              dim. proj(M/xM) = dim. proj(M) + 1.
```

Indeed, from the exact sequence `0 → M →^x M → M/xM → 0` defined by multiplication by `x` in `M`, one deduces the exact
sequence of Tor:

```text
        Tor^A_i(M, k) →^x Tor^A_i(M, k) → Tor^A_i(M/xM, k) → Tor^A_{i-1}(M, k) →^x Tor^A_{i-1}(M, k)
```

for every `i ≥ 1`. Now, for every `A`-module `N`, the homothety of ratio `x` in `M ⊗_A N` comes both from the homothety
of ratio `x` in `M` and from the homothety of ratio `x` in `N`; one concludes at once, since the homothety of ratio `x`
in `k` is zero by definition, that for every `i`, the homomorphism `Tor^A_i(M, k) →^x Tor^A_i(M, k)` is zero; in other
words, one has the exact sequence

```text
                        0 → Tor^A_i(M, k) → Tor^A_i(M/xM, k) → Tor^A_{i-1}(M, k) → 0.
```

If `dim. proj(M) = n`, then `Tor^A_n(M, k) ≠ 0` and `Tor^A_{n+1}(M, k) = Tor^A_{n+2}(M, k) = 0` by virtue of `(17.2.6)`.
It follows from what precedes that one has `Tor^A_{n+1}(M/xM, k) ≠ 0` and `Tor^A_{n+2}(M/xM, k) = 0`, hence
`dim. proj(M/xM) = n + 1` by `(17.2.6)`.

**Proposition (17.2.8) (M. Auslander).**

<!-- label: 0_IV.17.2.8 -->

*Let `A` be a ring. The following conditions are equivalent:*

*a) Every `A`-module is of projective dimension `≤ n`.*

*a′) Every `A`-module of finite type is of projective dimension `≤ n`.*

*b) Every `A`-module is of injective dimension `≤ n`.*

*c) For every pair of `A`-modules `M, N` one has `Ext^{n+1}_A(M, N) = 0`.*

*c′) For every pair of `A`-modules `M, N` such that `M` is of finite type (or only monogenic), one has
`Ext^{n+1}_A(M, N) = 0`.*

<!-- original page 141 -->

This follows at once from `(17.2.1)` and `(17.2.3)`.

The smallest number `n` (an integer or `+∞`) for which the equivalent conditions of `(17.2.8)` are satisfied is called
the *global cohomological dimension* (or simply *cohomological dimension*) of `A` and denoted `dim. coh(A)`.

**Proposition (17.2.9).**

<!-- label: 0_IV.17.2.9 -->

*Let `A` be a Noetherian ring. The following conditions are equivalent:*

*a) `dim. coh(A) ≤ n`.*

*b) Every `A`-module of finite type is of injective dimension `≤ n`.*

*c) For every pair of `A`-modules of finite type `M, N`, one has `Ext^{n+1}_A(M, N) = 0`.*

This follows at once from the definition and from `(17.2.4)`.

**Corollary (17.2.10).**

<!-- label: 0_IV.17.2.10 -->

*If `A` is a Noetherian ring, one has*

```text
(17.2.10.1)             dim. coh(A) = sup_𝔪(dim. coh(A_𝔪))
```

*where `𝔪` runs through the spectrum of `A` (or the set of maximal ideals of `A`).*

This follows from `(17.2.9)` and `(17.2.5)`.

**Proposition (17.2.11).**

<!-- label: 0_IV.17.2.11 -->

*Let `A` be a Noetherian local ring, `k` its residue field. For `dim. coh(A) ≤ n`, it is necessary that
`Tor^A_i(k, k) = 0` for `i > n`, and sufficient that `Tor^A_{n+1}(k, k) = 0`.*

Taking `(17.2.6)` into account, it suffices to prove that the relations `dim. coh(A) ≤ n` and `dim. proj_A(k) ≤ n` are
equivalent. It is clear that the first implies the second by definition. Conversely, if `dim. proj_A(k) ≤ n`, one has
`Tor^A_i(M, k) = 0` for `i > n` and every `A`-module `M` by virtue of `(17.2.2, (ii))`; hence `dim. proj(M) ≤ n`, which
proves the proposition by virtue of `(17.2.8)`.

**Corollary (17.2.12).**

<!-- label: 0_IV.17.2.12 -->

*Let `A` be a Noetherian ring. For `dim. coh(A) ≤ n`, it is necessary that, for every maximal ideal `𝔪` of `A`, one have
`Tor^{A_𝔪}_i(A/𝔪, A/𝔪) = 0` for `i > n`, and sufficient that these relations be satisfied for `i = n + 1`.*

This follows at once from `(17.2.11)` and `(17.2.10)`.

**Proposition (17.2.13).**

<!-- label: 0_IV.17.2.13 -->

*Let `A`, `B` be two Noetherian local rings, `φ : A → B` a local homomorphism making `B` a flat `A`-module. Then one
has*

```text
(17.2.13.1)             dim. coh(A) ≤ dim. coh(B).
```

Suppose that `dim. coh(B) = n` is finite; it suffices to prove that for every pair `(M, N)` of `A`-modules of finite
type, one has `Tor^A_i(M, N) = 0` for `i > n` `(17.2.11)`. Since `B` is a faithfully flat `A`-module `(0_I, 6.6.2)`, it
comes to the same thing `(0_I, 6.4.1)` to show that one has

```text
(17.2.13.2)             Tor^A_i(M, N) ⊗_A B = 0.
```

Now, if `L_• = (L_j)` is a right resolution of `M` by free `A`-modules, it follows from the fact that `B` is a flat
`A`-module that `L_• ⊗_A B = (L_j ⊗_A B)` is a right resolution of the `B`-module `M ⊗_A B` by free `B`-modules;
moreover, one has `(L_j ⊗_A B) ⊗_B (N ⊗_A B) = (L_j ⊗_A N) ⊗_A B`, whence one concludes at once that the left-hand side

<!-- original page 142 -->

of `(17.2.13.2)` equals `Tor^B_i(M ⊗_A B, N ⊗_A B)`; the hypothesis on `B` implies that this `B`-module is zero for
`i > n` `(17.2.2, (ii))`, whence the conclusion.

**(17.2.14)** Let `(X, 𝒪_X)` be a ringed space, `ℱ` an `𝒪_X`-Module; one calls the *pointwise projective* (resp.
*injective*) *dimension* of `ℱ` and denotes by `dim. proj(ℱ)` (resp. `dim. inj(ℱ)`) the number
`sup_{x ∈ X}(dim. proj(ℱ_x))` (resp. `sup_{x ∈ X}(dim. inj(ℱ_x))`). One calls the *pointwise cohomological dimension* of
`X` and denotes by `dim. coh(X)` the number `sup_{x ∈ X}(dim. coh(𝒪_x))`. It follows from `(17.2.5)` and `(17.2.10)`
that when `A` is a Noetherian ring, `M` an `A`-module of finite type and `X = Spec(A)`, one has
`dim. proj(M̃) = dim. proj(M)`, `dim. inj(M̃) = dim. inj(M)` and `dim. coh(X) = dim. coh(A)`. One calls the *projective*
(resp. *injective*) *dimension* of `ℱ` *at a point* `x ∈ X` the projective (resp. injective) dimension of `ℱ_x`, the
*cohomological dimension* of `X` *at a point* `x` the cohomological dimension of `𝒪_x`.

**Proposition (17.2.15).**

<!-- label: 0_IV.17.2.15 -->

*Let `X`, `Y` be two ringed spaces with Noetherian local rings, `f : X → Y` a flat morphism. If `dim. coh(X) ≤ n`, then
`Y` is of cohomological dimension `≤ n` at every point of `f(X)`.*

This follows at once from `(17.2.13)`.

### 17.3. Cohomological theory of regular rings

**Theorem (17.3.1) (Hilbert-Serre).**

<!-- label: 0_IV.17.3.1 -->

*Let `A` be a Noetherian local ring. For `A` to be of finite cohomological dimension, it is necessary and sufficient
that `A` be regular; one has then*

```text
(17.3.1.1)              dim. coh(A) = dim(A).
```

Suppose `A` regular; let `𝔪` be its maximal ideal, `𝐱 = (x_i)_{1 ≤ i ≤ n}` a regular system of parameters of `A`
`(17.1.6)`; consider the complex of the exterior algebra `K_•(𝐱)` `(III, 1.1.1)`, which is formed of free `A`-modules,
with `K_i(𝐱) = 0` for `i > n`; since `(x_i)` is a regular sequence, one has `H_i(K_•(𝐱)) = 0` for `i > 0`
`(III, 1.1.4 and 1.1.3.3)` and `H_0(K_•(𝐱)) = A/(x_1 A + ⋯ + x_n A) = A/𝔪 = k`; the `K_i(𝐱)` therefore form a *free
resolution* of `k` of length `n`. Now, the fact that the `x_i` belong to `𝔪` implies at once that in the complex
`K_•(𝐱, k) = K_•(𝐱) ⊗_A k`, the boundary operator is zero in all dimensions, so that one has, by definition,
`Tor^A_i(k, k) = Λ^i(k^n)`; equality `(17.3.1.1)` therefore follows at once from `(17.2.11)` (this result is essentially
Hilbert's "syzygy theorem").

Let us now show that if `A` is a Noetherian local ring, `𝔪` its maximal ideal, and if `dim. proj_A(𝔪)` is finite, then
`A` is regular, which will complete the proof of `(17.3.1)`. We proceed by induction on `n = rg_k(𝔪/𝔪²)`. For `n = 0`,
one has `𝔪 = 0` and the assertion is trivial.

**Lemma (17.3.1.2) (Nagata).**

<!-- label: 0_IV.17.3.1.2 -->

*If every element of `𝔪 - 𝔪²` is a zero-divisor in `A`, there exists `c ≠ 0` in `A` such that `c𝔪 = 0` (in other words,
one has `𝔪 ∈ Ass(A)`).*

One can restrict to the case where `𝔪 ≠ 0`, hence `𝔪 ≠ 𝔪²`. The hypothesis implies that `𝔪 - 𝔪²` is contained in the
union of the ideals `𝔭_i` of `Ass(A)` `(Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 3 of prop. 2)`; hence `𝔪` is
contained in the union of `𝔪²`

<!-- original page 143 -->

and the `𝔭_i`, hence in one of the `𝔭_i` since `𝔪 ≠ 𝔪²` `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`; `𝔪` being
maximal, this proves the lemma.

**Lemma (17.3.1.3).**

<!-- label: 0_IV.17.3.1.3 -->

*If `a ∈ 𝔪 - 𝔪²`, `𝔪/Aa` is isomorphic to a direct factor of `𝔪/a𝔪`.*

There exists a minimal system of generators of `𝔪` containing `a` (whose images in `𝔪/𝔪²` form a basis of this
`k`-vector space); let `𝔟` be the ideal generated by the elements of this system other than `a`. Since the relation
`xa ∈ 𝔟` implies `x ∈ 𝔪` (by considering the image of `xa` in `𝔪/𝔪²`), one has `𝔟 ∩ Aa ⊂ a𝔪`, whence a homomorphism
`𝔟/(𝔟 ∩ Aa) → 𝔪/a𝔪` deduced from the injection `𝔟 → 𝔪` by passage to the quotients, and which is *injective*.
Furthermore, `𝔟 + Aa = 𝔪`, and the composite homomorphism

```text
                𝔪/Aa = (𝔟 + Aa)/Aa ≅ 𝔟/(𝔟 ∩ Aa) → 𝔪/a𝔪 → 𝔪/Aa
```

is the identity; whence the lemma.

**Lemma (17.3.1.4).**

<!-- label: 0_IV.17.3.1.4 -->

*Let `A` be a Noetherian local ring, `𝔪` its maximal ideal, `E` an `A`-module of finite type and of finite projective
dimension. If `a ∈ 𝔪` is `A`-regular and `E`-regular, then `E/aE` is an `(A/aA)`-module of finite projective dimension,
at most equal to `dim. proj_A(E)`.*

We argue by induction on `h = dim. proj_A(E)`, the case `h = 0` being trivial since `E` is then a projective `A`-module,
hence `E/aE` is a projective `(A/aA)`-module. There exists an exact sequence

```text
                                0 → N → L → E → 0
```

where `L` is free and `dim. proj_A(N) = h - 1` `(17.2.2, (iii))`, with `N` of finite type. Moreover, the sequence

```text
                                0 → N/aN → L/aL → E/aE → 0
```

is exact `(15.1.18)`. Since `a` is `A`-regular, it is also `N`-regular since `L` is free; the induction hypothesis
implies that `N/aN` is an `(A/aA)`-module of projective dimension `≤ h - 1`, and since `L/aL` is a free `(A/aA)`-module,
`E/aE` is an `(A/aA)`-module of projective dimension `≤ h`.

Let us now examine two cases:

I. — Suppose first that every element of `𝔪 - 𝔪²` is a zero-divisor in `A`, in which case `(17.3.1.2)` there exists
`c ≠ 0` in `A` such that `c𝔪 = 0`. Let us show that then `𝔪 = 0`. Were this not so, let us first note that `𝔪` could not
be a projective `A`-module, for it would be free `(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, which
contradicts the relation `c𝔪 = 0`. One would therefore have `n = dim. coh(A) ≥ 1`. Since `𝔪 ∈ Ass(A)`, there would exist
an exact sequence of `A`-homomorphisms

```text
                                0 → k → A → E → 0.
```

But this is absurd, for by virtue of the relation `n ≥ 1`, the exact sequence of Tor would give the exact sequence
`0 → Tor^A_{n+1}(E, k) → Tor^A_n(k, k) → 0`; now one has `Tor^A_{n+1}(E, k) = 0` `(17.2.2, (ii))` and
`Tor^A_n(k, k) ≠ 0` `(17.2.11)`, and we have reached a contradiction.

II. — One can therefore restrict to the case where there exists `a ∈ 𝔪 - 𝔪²` which is an `A`-regular element, and
consequently also `𝔪`-regular. Consider the ring `A′ = A/aA` and its

<!-- original page 144 -->

maximal ideal `𝔪′ = 𝔪/aA`; it is clear that `rg_k(𝔪′/𝔪′²) = n - 1`. By virtue of `(17.3.1.4)`, `𝔪/a𝔪` is an `A′`-module
of finite projective dimension, hence so is `𝔪′ = 𝔪/aA`, which is a direct factor of it `(17.3.1.3 and 17.2.1)`. The
induction hypothesis therefore implies that `A′ = A/aA` is regular, which proves by `(17.1.8)` that `A` is regular.

**Corollary (17.3.2).**

<!-- label: 0_IV.17.3.2 -->

*If `A` is a regular local ring, `A_𝔭` is regular for every prime ideal `𝔭` of `A`.*

Indeed, one has seen `(17.2.10)` that `dim. coh(A_𝔭) ≤ dim. coh(A)`, hence the conclusion follows at once from
`(17.3.1)`.

**Proposition (17.3.3).**

<!-- label: 0_IV.17.3.3 -->

*Let `A`, `B` be two Noetherian local rings, `ρ : A → B` a local homomorphism, `𝔪` (resp. `𝔫`) the maximal ideal of `A`
(resp. `B`), `k = A/𝔪` (resp. `k′ = B/𝔫`) the residue field of `A` (resp. `B`). One has therefore a canonical
homomorphism of `k′`-vector spaces*

```text
(17.3.3.1)              ψ : (𝔪/𝔪²) ⊗_k k′ → 𝔫/𝔫².
```

*(i) If `B` is regular and if `B` is a flat `A`-module, `A` is regular.*

*(ii) The following conditions are equivalent:*

*a) `B` is regular and the homomorphism `ψ` `(17.3.3.1)` is injective.*

*b) `A` and `B` are regular, and for a regular system of parameters `(x_i)_{1 ≤ i ≤ m}` of `A`, the `φ(x_i)` are part of
a regular system of parameters of `B` (in which case this property holds for every regular system of parameters of
`A`).*

*c) `B` and `B ⊗_A k` are regular, and `B` is a flat `A`-module.*

*d) `A` and `B ⊗_A k` are regular, and `B` is a flat `A`-module.*

*e) `A` and `B ⊗_A k` are regular, and one has*

```text
(17.3.3.2)              dim(B) = dim(A) + dim(B ⊗_A k).
```

(i) One has `dim. coh(A) ≤ dim. coh(B)` by `(17.2.13)`, so it suffices to apply `(17.3.1)`.

(ii) When `A` is assumed regular and `(x_i)` is a regular system of parameters of `A`, to say that `B` is a flat
`A`-module is equivalent, by virtue of `(15.1.21)`, to saying that the sequence of `y_i = φ(x_i)` is `B`-regular (since
`B ⊗_A k` is a `k`-flat module). On the other hand, since `dim(A) = m`, and the sequence `(y_i)` generates the ideal
`𝔪B`, the relation `(17.3.3.2)`, which is also written `dim(B/𝔪B) = dim(B) - m`, is equivalent to saying that the
sequence `(y_i)_{1 ≤ i ≤ m}` is part of a system of parameters of `B` `(16.3.7)`. One therefore sees that conditions b),
d) and e) are equivalent respectively to the following:

b′) `A` and `B` are regular and `(y_i)_{1 ≤ i ≤ m}` is part of a regular system of parameters of `B`.

d′) `A` is regular, `B/(∑_{i=1}^{m} y_i B)` is regular and the sequence `(y_i)` is `B`-regular.

e′) `A` is regular, `B/(∑_{i=1}^{m} y_i B)` is regular and the sequence `(y_i)` is part of a system of parameters of
`B`.

Now, b′) and e′) are equivalent by virtue of `(17.1.7)`, and since d′) implies e′) `(16.4.1)` and is implied by b′)
`(17.1.7)`, it is equivalent to them. The conjunction

<!-- original page 145 -->

of b) and d) trivially implies c), and by virtue of (i), c) implies d); we have therefore proved the equivalence of b),
c), d) and e). Furthermore, it is clear that b) implies a), the classes of the `x_i` in `𝔪/𝔪²` forming then a basis of
this `k`-vector space and the classes of the `y_i` in `𝔫/𝔫²` a linearly independent system of this `k′`-vector space. It
remains therefore to prove that a) implies e). Put `V = 𝔪/𝔪²`, `W = 𝔫/𝔫²`; it is immediate that one has
`ψ(V ⊗_k k′) = (𝔪² + 𝔪B)/𝔫²`. One has on the one hand, by virtue of `(16.3.9)`,

```text
(17.3.3.3)              dim(B) ≤ dim(A) + dim(B ⊗_A k);
```

in the second place, by `(16.2.6)`, one has

```text
(17.3.3.4)              dim(A) ≤ rg_k(V) ⊗_k k′.
```

Finally, in the local ring `B ⊗_A k = B/𝔪B`, `𝔫′ = 𝔫/𝔪B` is the maximal ideal, `k′` the residue field and `𝔫′/𝔫′²` is
isomorphic to `𝔫/(𝔫² + 𝔪B) = W/ψ(V ⊗_k k′)`; one has therefore, by `(16.2.6)`,

```text
(17.3.3.5)              dim(B ⊗_A k) ≤ rg_{k′} W - rg_{k′} ψ(V ⊗_k k′).
```

Finally, since `B` is assumed regular, one has `dim(B) = rg_{k′} W` `(17.1.1)`; one therefore concludes from
`(17.3.3.3)`, `(17.3.3.4)` and `(17.3.3.5)` that one has

```text
        rg_{k′} W ≤ dim(A) + dim(B ⊗_A k) ≤ rg_{k′} W + rg_{k′}(V ⊗_k k′) - rg_{k′} ψ(V ⊗_k k′)
```

and to say that the two extreme terms of this inequality are equal means that `ψ` is injective. Condition a) therefore
necessarily implies that in each of the relations `(17.3.3.3)`, `(17.3.3.4)` and `(17.3.3.5)`, the two sides are equal;
now, equality in `(17.3.3.4)` (resp. `(17.3.3.5)`) means that `A` (resp. `B ⊗_A k`) is regular `(17.1.1)`; one has
therefore indeed proved that a) implies e).

**Proposition (17.3.4).**

<!-- label: 0_IV.17.3.4 -->

*Let `A` be a regular local ring of dimension `n`, `𝔪` its maximal ideal. For every non-zero `A`-module of finite type
`M`, one has*

```text
(17.3.4.1)              prof(M) + dim. proj(M) = n.
```

We argue by induction on `m = prof(M)`. If `m = 0`, one knows `(16.4.6, (i))` that there exists a submodule `N` of `M`
isomorphic to `k = A/𝔪`; applying the exact sequence of Tor to the exact sequence `0 → N → M → M/N → 0`, one obtains an
exact sequence

```text
                        Tor^A_{n+1}(M/N, k) → Tor^A_n(N, k) → Tor^A_n(M, k),
```

and the hypothesis that `A` is regular implies `Tor^A_{n+1}(M/N, k) = 0` `((17.3.1.1)` and `(17.2.6))`, hence
`Tor^A_n(k, k)` is isomorphic to a sub-`A`-module of `Tor^A_n(M, k)`; applying again `(17.3.1.1)` and `(17.2.6)`, one
sees that `Tor^A_n(M, k) ≠ 0`, hence `dim. proj(M) ≥ n` `(17.2.6)`; but since `dim. proj(M) ≤ n` by `(17.3.1.1)`, one
has indeed `dim. proj(M) = n`. Suppose now `m > 0`, and let `x` be an `M`-regular element belonging to `𝔪`; one knows
then `(16.4.6, (i))` that one has `prof(M/xM) = m - 1`, and on the other hand `(17.2.7)`
`dim. proj(M/xM) = dim. proj(M) + 1`; the induction hypothesis at once proves the relation `(17.3.4.1)`.

<!-- original page 146 -->

**Corollary (17.3.5).**

<!-- label: 0_IV.17.3.5 -->

*(i) Let `A` be a regular local ring of dimension `n`; for an `A`-module `M ≠ 0` of finite type to be free, it is
necessary and sufficient that `M` be a Cohen-Macaulay `A`-module of dimension `n`.*

*(ii) Let `A` be a regular local ring, `B` a local ring, `ρ : A → B` a local homomorphism making `B` an `A`-module of
finite type. For `B` to be a free `A`-module, it is necessary and sufficient that `B` be a Cohen-Macaulay ring and that
`ρ` be injective (or, what comes to the same thing `(16.1.5)`, that `dim(B) = dim(A)`).*

(i) This follows from `(17.3.4.1)` and from the fact that for an `A`-module of finite type, it comes to the same to say
that this module is projective or free `(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`; the free
`A`-modules of finite type `M` are therefore characterized by the relation `dim. proj(M) = 0` `(17.2.2, (i))`.

(ii) To say that `B` is a Cohen-Macaulay ring is equivalent to saying that `B` is a Cohen-Macaulay `A`-module
`(16.5.3)`, hence it suffices to apply (i), since `dim B = dim A` `(16.1.5)`.

**(17.3.6)** One says that a Noetherian ring `A` is *regular* if for every prime ideal `𝔭` of `A`, the local ring `A_𝔭`
is regular; when `A` itself is a local ring, it follows from `(17.3.2)` that this definition is equivalent to that of
`(17.1.2)`. For `A` to be regular it suffices, by virtue of `(17.3.2)`, that `A_𝔪` be regular for every maximal ideal
`𝔪` of `A`. Moreover, it follows at once from this definition that for every multiplicative subset `S` of `A`,
`S^{-1} A` is regular.

**Proposition (17.3.7).**

<!-- label: 0_IV.17.3.7 -->

*If `A` is a regular Noetherian ring, every polynomial ring `A[T_1, …, T_n]` is regular.*

It is evidently enough to prove that the polynomial ring `B = A[T]` is regular; since `B` is a free `A`-module, for
every prime ideal `𝔮` of `B`, `B_𝔮` is a flat `A_𝔭`-module, where `𝔭 = 𝔮 ∩ A` `(0_I, 6.3.1)`; it therefore suffices, by
virtue of `(17.1.10)` [^1], to prove that `B_𝔮 / 𝔭 B_𝔮` is regular, and since this ring is a local ring at a prime ideal
of `A_𝔭[T] / 𝔭 A_𝔭[T] = k[T]` (where `k` is the residue field `A_𝔭/𝔭 A_𝔭`), it suffices to prove that `C = k[T]` is
regular; now, `C` being principal, the local rings at the prime ideals of `C` are discrete valuation rings or a field
(for the ideal `(0)`), hence regular `(17.1.4)`, which completes the proof.

**Corollary (17.3.8).**

<!-- label: 0_IV.17.3.8 -->

*If `A` is a regular ring, every formal power series ring `A[[T_1, …, T_n]]` is regular.*

Let `𝔍` be the ideal generated by the `T_i` in the polynomial ring `A[T_1, …, T_n]`; since the latter is regular by
`(17.3.7)`, and `A[[T_1, …, T_n]]` is the completion of `A[T_1, …, T_n]` for the `𝔍`-preadic topology
`(Bourbaki, Alg. comm., chap. III, §2, n° 12, Example 1)`, the conclusion follows from the:

**Lemma (17.3.8.1).**

<!-- label: 0_IV.17.3.8.1 -->

*Let `A` be a regular ring, `𝔍` an ideal of `A`, `Â` the separated completion of `A` for the `𝔍`-preadic topology. Then
`Â` is regular.*

It suffices indeed `(17.3.6)` to see that for every maximal ideal `𝔫` of `Â`, the local ring `Â_𝔫` is regular; one knows
`(Bourbaki, Alg. comm., chap. III, §3, n° 4, prop. 8)` that `𝔫`

<!-- original page 147 -->

is of the form `𝔪Â`, where `𝔪` is a maximal ideal of `A` containing `𝔍`, and that the canonical homomorphism `A → Â`
gives an *injective* homomorphism `A_𝔪 → Â_𝔫`, such that the `𝔫Â_𝔫`-preadic topology of `Â_𝔫` induces on `A_𝔪` the
`𝔪A_𝔪`-preadic topology, and such that `A_𝔪` is dense in `Â_𝔫` for the `𝔫Â_𝔫`-preadic topology; consequently the
completions of the Noetherian local rings `A_𝔪` and `Â_𝔫` are canonically isomorphic. Now, by hypothesis `A_𝔪` is
regular, hence so is its completion `(17.1.5)`, and since the completion of `Â_𝔫` is regular, so is `Â_𝔫` by `(17.1.5)`.

**Corollary (17.3.9).**

<!-- label: 0_IV.17.3.9 -->

*Let `A` be a Noetherian ring, quotient of a regular Noetherian ring `B`. If `C` is an `A`-algebra of finite type, every
ring of fractions `S^{-1} C` of `C` is a quotient of a regular ring.*

Indeed, `C` is a quotient of a polynomial ring `A[T_1, …, T_n]`; since `A = B/𝔍`, where `𝔍` is an ideal of `B`, one has
`A[T_1, …, T_n] = B[T_1, …, T_n] / 𝔍 B[T_1, …, T_n]`; by virtue of `(17.3.7)`, one can therefore restrict to the case
where `C` is a quotient of a regular ring `B′`; but if `S′` is the inverse image of `S` in `B′`, `S′` is a
multiplicative subset of `B′` and `C` is a quotient ring of `S′^{-1} B′`, so that ultimately everything reduces to
showing that when `C` is regular, so is `S^{-1} C`, which was seen in `(17.3.6)`.

The importance of quotients of regular rings lies among others in the preceding property and in the fact that they are
catenary rings `(16.5.12)`.

All the rings of importance in applications to algebraic geometry are quotients of regular rings.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/04-c0-s17-anneaux-reguliers.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-1.pdf, pp. 135-147 -->

[^1]: Translator's note. EGA's citation reads `(17.1.10)` but no such item exists in §17.1; the intended reference is to
    `(17.3.3, (i))` — flatness plus regularity of the special fibre implies regularity of the base.
