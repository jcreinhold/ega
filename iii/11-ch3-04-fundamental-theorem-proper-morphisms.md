# §4. The fundamental theorem of proper morphisms; applications

<!-- original page 122 -->

## 4.1. The fundamental theorem

**(4.1.1)**

<!-- label: III.4.1.1 -->

Let `X`, `Y` be two usual Noetherian preschemes, `f : X → Y` a proper morphism, `Y'` a closed subset of `Y`, and `X'`
its inverse image `f^{-1}(Y')`. We denote by `𝔛` and `𝔜` the formal preschemes `X_{/X'}` and `Y_{/Y'}`, the completions
of `X` and `Y` along `X'` and `Y'` respectively `(I, 10.8.5)`; we write `𝑓̂` for the extension of `f` to these
completions `(I, 10.9.1)`, which is a morphism `𝔛 → 𝔜` of formal preschemes. For every coherent `𝒪_X`-module `ℱ`, we
denote by `ℱ̂` its completion along `X'` `(I, 10.8.4)`, which is a coherent `𝒪_𝔛`-module `(I, 10.8.8)`.

<!-- original page 123 -->

**(4.1.2)**

<!-- label: III.4.1.2 -->

Let `𝒥` be a coherent ideal of `𝒪_Y` such that `Supp(𝒪_Y/𝒥) = Y'` `(I, 5.2.1)`; we know `(I, 4.4.5)` that
`𝒦 = f^*(𝒥) 𝒪_X` is a coherent ideal of `𝒪_X` such that

```text
  Supp(𝒪_X / 𝒦) = X'.
```

We consider, for every `k ≥ 0`, the coherent `𝒪_X`-modules

```text
  ℱ_k = ℱ / 𝒦^{k+1} ℱ.
```

The `𝒪_Y`-modules `R^n f_*(ℱ)` and `R^n f_*(ℱ_k)` are coherent for every `n` (3.2.1). For every `k' ≥ k` and every `n`,
the canonical homomorphism `ℱ_{k'} → ℱ_k` defines by functoriality a homomorphism

```text
  R^n f_*(ℱ_{k'}) → R^n f_*(ℱ_k).                                            (4.1.2.1)
```

Moreover, since `ℱ_k` is an `𝒪_X / 𝒦^{k+1}`-module, `R^n f_*(ℱ_k)` is an `𝒪_Y / 𝒥^{k+1}`-module `(0_III, 12.2.1)`, and
one deduces from (4.1.2.1) a homomorphism

```text
  R^n f_*(ℱ_{k'}) ⊗_{𝒪_Y} (𝒪_Y / 𝒥^{k+1}) → R^n f_*(ℱ_k).                    (4.1.2.2)
```

The two sides of (4.1.2.2) form two projective systems, and the projective limit of the first side is none other than
the completion `(R^n f_*(ℱ))_{/Y'}` which we shall denote `(R^n f_*(ℱ))^∧`. Furthermore, it is immediate that the
homomorphisms (4.1.2.2) form a projective system, whence by passage to the limit a canonical homomorphism

```text
  φ_n : (R^n f_*(ℱ))^∧ → lim_← R^n f_*(ℱ_k).                                 (4.1.2.3)
                          k
```

Moreover, (4.1.2.2) is a homomorphism of `(𝒪_Y / 𝒥^{k+1})`-modules, and therefore `(I, 10.8.3)` may be considered as a
continuous homomorphism of pseudo-discrete topological `𝒪_𝔜`-modules `(0_I, 3.8.1)`. The homomorphism `φ_n` is
consequently a continuous homomorphism of topological `𝒪_𝔜`-modules.

**(4.1.3)**

<!-- label: III.4.1.3 -->

Let `i : 𝔛 → X` be the canonical morphism of ringed spaces defined in `(I, 10.8.7)`, so that we have the commutative
diagram

```text
  X_k →^{h_k} X
   ↓ f_k       ↓ f                                                            (4.1.3.1)
  Y_k →        Y
```

where `X_k` is the closed subprescheme of `X` defined by the ideal `𝒦^{k+1}`, `i_k` the canonical injection, `h_k` the
morphism of ringed spaces corresponding to the identity on the underlying spaces and to the canonical homomorphism
`𝒪_X → 𝒪_X / 𝒦^{k+1}` `(I, 10.5.2)`. Moreover, we have `ℱ̂ = i^*(ℱ)` `(I, 10.8.8)` up to canonical isomorphism. We know
that

```text
  H^n(X_k, ℱ_k) = H^n(X, ℱ_k)                                                (4.1.3.2)
```

up to canonical isomorphism, since `ℱ_k = (h_k)_*((i_k)^*(ℱ_k))` `(0_I, 4.9.1)`; the canonical homomorphism
`H^n(X, ℱ) → H^n(X_k, ℱ_k)` `(0_III, 12.1.3.5)` thus also reads

```text
  H^n(X, ℱ) → H^n(X, ℱ_k),                                                   (4.1.3.3)
```

and these homomorphisms obviously form a projective system, whence by passage to the limit a canonical homomorphism

```text
  ψ_X : H^n(X, ℱ) → lim_← H^n(X, ℱ_k).                                       (4.1.3.4)
                      k
```

<!-- original page 124 -->

Replacing `X` by an open set of the form `f^{-1}(V)`, where `V` is an affine open set of `Y`, and taking (1.4.11) into
account, we have homomorphisms

```text
  ψ_V : H^n(X ∩ f^{-1}(V), ℱ) → lim_← Γ(V, R^n f_*(ℱ_k));                    (4.1.3.5)
                                  k
```

these homomorphisms obviously commute with restriction from `V` to a smaller affine open set, and therefore finally
define a canonical homomorphism of sheaves

```text
  ψ : R^n f_*(ℱ) → lim_← R^n f_*(ℱ_k).                                       (4.1.3.6)
                     k
```

**(4.1.4)**

<!-- label: III.4.1.4 -->

Let finally `j : 𝔜 → Y` be the canonical morphism of ringed spaces `(I, 10.8.7)`; since `R^n f_*(ℱ)` is a coherent
`𝒪_Y`-module (3.2.1), we have `j^*(R^n f_*(ℱ)) = (R^n f_*(ℱ))^∧` up to canonical isomorphism `(I, 10.8.8)`, and we
therefore have a canonical homomorphism

```text
  ρ_n : (R^n f_*(ℱ))^∧ = j^*(R^n f_*(ℱ)) → R^n 𝑓̂_*(j^*(ℱ)) = R^n 𝑓̂_*(ℱ̂),     (4.1.4.1)
```

defined in general for ringed spaces (see the proof of `(1.4.15)`). We show that the diagram

```text
  (R^n f_*(ℱ))^∧ ────→ R^n 𝑓̂_*(ℱ̂)
        ↓ φ_n             ↑ ψ_n                                              (4.1.4.2)
        lim_← R^n f_*(ℱ_k)
          k
```

is commutative. It clearly suffices to prove the commutativity of the corresponding diagram of homomorphisms of
presheaves, so we may restrict to the case where `Y` is affine, and everything reduces to proving that the diagram

```text
  (H^n(X, ℱ))^∧ ────→ H^n(𝔛, ℱ̂)
        ↓ φ_n           ↑ ψ_{n,𝔛}                                            (4.1.4.3)
        lim_← H^n(X, ℱ_k)
          k
```

is commutative. But the commutativity of (4.1.3.1) and the relations seen in (4.1.3) between the cohomology groups give
at once the commutative diagram

```text
  H^n(X, ℱ) ────→ H^n(𝔛, ℱ̂) = H^n(𝔛, i^*(ℱ))
         ╲         ╱
          H^n(X_k, ℱ_k) = H^n(X, ℱ_k)
```

whence we deduce immediately the commutativity of (4.1.4.3).

**Theorem (4.1.5).**

<!-- label: III.4.1.5 -->

*Let `f : X → Y` be a proper morphism of Noetherian preschemes, `Y'` a closed subset of `Y`, `X' = f^{-1}(Y')`. Then,
for every coherent `𝒪_X`-module `ℱ`, `R^n 𝑓̂_*(ℱ̂)` is a coherent `𝒪_𝔜`-module, and the homomorphisms `φ_n`, `ψ_n`, and
`ρ_n` of the diagram (4.1.4.2) are topological isomorphisms.*

**Proof.** It clearly suffices to prove that `φ_n` and `ψ_n` are isomorphisms; since `R^n f_*(ℱ)` is coherent (3.2.1),
it will follow that `(R^n f_*(ℱ))^∧` is coherent `(I, 10.8.8)`, and the bicontinuity of `φ_n`, `ψ_n`, and `ρ_n` is then
automatic `(I, 10.11.6)`.

**Remarks (4.1.6).**

<!-- label: III.4.1.6 -->

(i) If we set `ℱ̂_k = ℱ̂ / 𝒦̂^{k+1} ℱ̂`, it is immediate that `ℱ̂_k = i^*(ℱ_k)`, and the canonical homomorphism
(4.1.3.6) is none other than the homomorphism already defined in (3.4.2.2)

```text
  R^n 𝑓̂_*(ℱ̂) → lim_← R^n 𝑓̂_*(ℱ̂_k);                                          (4.1.6.1)
                 k
```

<!-- original page 125 -->

consequently, the fact that `ψ_n` is an isomorphism is a particular case of (3.4.3). But we shall give below a direct
proof, avoiding the delicate considerations on projective limits of spectral sequences `(0_III, 13.7)` on which the
general theorem (3.4.3) rests.

(ii) Taking account of the fact that the `ψ_n` are isomorphisms, it is equivalent to say that the `φ_n` or the
`ρ_n = ψ_n ∘ φ_n^{-1}` are isomorphisms. Theorem (4.1.5) expresses, among other things, that *the formation of
`R^n f_*(ℱ)` commutes with completion*, and may be called the *first comparison theorem between the "algebraic" and
"formal" theories*.

We shall begin by establishing the affine form of (4.1.5):

**Corollary (4.1.7).**

<!-- label: III.4.1.7 -->

*The hypotheses being those of (4.1.5), suppose in addition that `Y = Spec(A)`, where `A` is Noetherian, and `𝒥 = 𝔍̃`,
where `𝔍` is an ideal of `A`, so that `ℱ_k = ℱ / 𝔍^{k+1} ℱ`. The canonical homomorphism*

```text
  φ_n : (H^n(X, ℱ))^∧ → lim_← H^n(X, ℱ_k)                                    (4.1.7.1)
                          k
```

*(where the first member is the Hausdorff completion of `H^n(X, ℱ)` for the `𝔍`-preadic topology) is an isomorphism. The
projective system `(H^n(X, ℱ_k))_{k ≥ 0}` satisfies condition (ML) for every `n`, and the canonical homomorphism*

```text
  ψ_n : H^n(X, ℱ) → lim_← H^n(X, ℱ_k)                                        (4.1.7.2)
                       k
```

*is an isomorphism. Finally, the filtration on `H^n(X, ℱ)` defined by the kernels of the canonical homomorphisms*

<!-- original page 126 -->

*`H^n(X, ℱ) → H^n(X, ℱ_k)` is `𝔍`-good `(0_III, 13.7.7)`, and `ψ_n` is a topological isomorphism* (1).

> (1) The following proof, simpler than the original proof, and the complement on the filtration of `H^n(X, ℱ)`, were
> communicated to us by J.-P. Serre.

**Proof.** The integer `n ≥ 0` being fixed in this proof, we shall set for simplicity

```text
  H = H^n(X, ℱ),    H_k = H^n(X, ℱ_k),                                       (4.1.7.3)
  R_k = Ker(H → H_k),     a sub-`A`-module of `H`.                           (4.1.7.4)
```

The exact sequence of cohomology

```text
  H^n(X, 𝔍^{k+1} ℱ) → H^n(X, ℱ) → H^n(X, ℱ_k) → H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, ℱ)
```

shows that we also have `R_k = Im(H^n(X, 𝔍^{k+1} ℱ) → H^n(X, ℱ))`; we shall set

```text
  Q_k = Ker(H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, ℱ))
      = Im(H^n(X, ℱ_k) → H^{n+1}(X, 𝔍^{k+1} ℱ)).                             (4.1.7.5)
```

We thus have the exact sequence

```text
  0 → R_k → H → H_k → Q_k → 0.                                               (4.1.7.6)
```

**(4.1.7.7).** Let `x` be an element of `𝔍^r` (`r ≥ 0`); multiplication by `x` in `𝔍^k ℱ` is a homomorphism
`𝔍^k ℱ → 𝔍^{k+r} ℱ` and consequently gives rise to a homomorphism

```text
  μ_x : H^n(X, 𝔍^k ℱ) → H^n(X, 𝔍^{k+r} ℱ).                                   (4.1.7.8)
```

If we denote by `S` the graded `A`-algebra `⊕ 𝔍^k`, we know that the multiplications `μ_x` endow `E = ⊕ H^n(X, 𝔍^k ℱ)`
with a structure of graded module of finite type over the graded ring `S` (3.3.2), which is Noetherian `(II, 2.1.5)`.

**Lemma (4.1.7.9).** *The submodules `R_k` of `H` define on `H` a `𝔍`-good filtration.*

**Proof.** First, we show that we have

```text
  𝔍 R_k ⊂ R_{k+1},                                                           (4.1.7.10)
```

multiplication in `H = H^n(X, ℱ)` by an element `x ∈ 𝔍` being therefore the map `μ_x` for `r = 1`. For every `x ∈ 𝔍`,
the diagram

```text
  𝔍^{k+1} ℱ ────→ 𝔍^{k+2} ℱ
       ↓             ↓
       ℱ   ────→     ℱ
```

<!-- original page 127 -->

(where the horizontal arrows are multiplication by `x`, and the vertical arrows the canonical injections) is
commutative; hence the corresponding diagram

```text
  H^n(X, 𝔍^{k+1} ℱ) ──^{μ_{x,n}}──→ H^n(X, 𝔍^{k+2} ℱ)
           ↓                                ↓                                (4.1.7.11)
         H^n(X, ℱ)  ──^{μ_{x,0}}──→  H^n(X, ℱ)
```

is commutative, which, taking into account the interpretation of `R_k` as the image of `H^n(X, 𝔍^{k+1} ℱ) → H^n(X, ℱ)`,
proves (4.1.7.10) and shows in addition that the graded `S`-module `R = ⊕ R_k` is a quotient of the sub-`S`-module
`M = ⊕ H^n(X, 𝔍^{k+1} ℱ)` of `E`; the remark made above thus shows that `R` is an `S`-module of finite type, which is
equivalent to the assertion of (4.1.7.9) (Bourbaki, *Alg. comm.*, chap. III, § 3, n° 1, th. 1).

**(4.1.7.12).** Consider now the graded `S`-module `N = ⊕ H^{n+1}(X, 𝔍^{k+1} ℱ)` defined as in (4.1.7.8); it is again an
`S`-module of finite type by virtue of (3.3.2); we have `Q_k ⊂ N_k` for every `k` by (4.1.7.5), and the diagram
(4.1.7.11) where we replace `n` by `n+1` shows that `𝔍^r Q_k ⊂ Q_{k+r}`. In other words, `Q = ⊕ Q_k` is a graded
sub-`S`-module of `N`, and is therefore of finite type.

**(4.1.7.13).** Denote by `a_k` the canonical injection `𝔍^k → A`, which we may write `a_k : S_k → S_0`. Since
`𝔍^{k+1} ℱ` is annihilated by `S_{k+1}`, the `A`-module `H^n(X, 𝔍^{k+1} ℱ)` is annihilated by `S_{k+1}`; since `Q_k` is
the image of the `A`-homomorphism `H^n(X, ℱ_k) → H^{n+1}(X, 𝔍^{k+1} ℱ)`, `Q_k`, as an `A`-module, is also annihilated by
`S_{k+1}`. This still means that, in the `S`-module `Q`, we have

```text
  a_{k+1}(S_{k+1}) Q_k = 0.                                                  (4.1.7.14)
```

Since `Q` is an `S`-module of finite type, there exist an integer `k_0` and an integer `h` such that `Q_{k+h} = S_h Q_k`
for `k ≥ k_0` `(II, 2.1.6, (ii))`; from this relation and (4.1.7.14), one deduces that there exists an integer `r > 0`
such that

```text
  a_r(S_r) Q = 0.                                                            (4.1.7.15)
```

**(4.1.7.16).** Note now that the canonical injection `𝔍^{k+1} ℱ → 𝔍^k ℱ` gives, on passage to cohomology, an
`A`-homomorphism

```text
  v_k : H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, 𝔍^k ℱ),                           (4.1.7.17)
```

and, for every `x ∈ 𝔍`, we have the obvious factorization

```text
  μ_{x,0} : H^{n+1}(X, ℱ) → H^{n+1}(X, 𝔍^{k+1} ℱ) →^{v_k} H^{n+1}(X, 𝔍^k ℱ), (4.1.7.18)
```

<!-- original page 128 -->

from which we conclude that, for every sub-`A`-module `P` of `H^{n+1}(X, 𝔍^{k+1} ℱ)`, we have, in the `S`-module `N`,

```text
  v_k(S_1 P) = a_1(S_1) P.                                                   (4.1.7.19)
```

**Lemma (4.1.7.20).** *There exists an integer `m > 0` such that `v_k(Q_{k+m}) = 0` for every `k ≥ k_0`.*

**Proof.** Take for `m` a multiple of `h` that is `≥ r`; since `Q_{k+m} = S_m Q_k` for `k ≥ k_0`, we have by virtue of
(4.1.7.19) and (4.1.7.15) `v_k(Q_{k+m}) = a_m(S_m) Q ⊂ a_r(S_r) Q = 0`.

**(4.1.7.21).** Note that from the commutative diagram

```text
  H^n(X, ℱ) ──→ H^n(X, ℱ_k) ──→ H^{n+1}(X, 𝔍^{k+1} ℱ) ──→ H^{n+1}(X, ℱ)
      ║              ↓                       ↓                  ║
  H^n(X, ℱ) ──→ H^n(X, ℱ_{k+m}) → H^{n+1}(X, 𝔍^{k+m+1} ℱ) → H^{n+1}(X, ℱ)
```

itself coming from the commutative diagram

```text
  0 → 𝔍^{k+1} ℱ ──→ ℱ ──→ ℱ_k ──→ 0
        ↑          ║      ↑
  0 → 𝔍^{k+m+1} ℱ → ℱ → ℱ_{k+m} → 0
```

where the vertical arrows are the canonical maps, one deduces a commutative diagram

```text
  0 → R_k    ──→ H ──→ H_k    ──→ Q_k    → 0
       ↓        id      ↓           ↓
  0 → R_{k+m} → H → H_{k+m} ──→ Q_{k+m} → 0
```

where the rows are exact. Since the last vertical arrow is zero for `k ≥ k_0` (4.1.7.20), the image of `H_{k+m}` in
`H_k` is contained in `Ker(H_k → Q_k) = Im(H → H_k)`, but moreover it contains `Im(H → H_k)` by the commutativity of the
diagram, so it is equal to it; the same therefore holds for the images in `H_k` of the `H_{k'}` for `k' ≥ k + m`, which
proves condition (ML) for the projective system `(H_k)_{k ≥ 0}`. Moreover, for every affine open set `U` of `X`, we have
`H^i(U, ℱ) = 0` for `i > 0` (1.3.1), and for `m > 0`, the map `H^0(U, ℱ_{k+m}) → H^0(U, ℱ_k)` is surjective
`(I, 1.3.9)`. We may therefore apply `(0_III, 13.3.1)`, and the canonical homomorphism `H^n(X, ℱ) → lim_← H^n(X, ℱ_k)`
is bijective for every `n ≥ 0`.

<!-- original page 129 -->

Since the projective system `(H/R_k)_{k ≥ 0}` is strict, we may pass to the projective limit in the exact sequences

```text
  0 → H/R_k → H_k → Q_k → 0                                                  (4.1.7.22)
```

`(0_III, 13.2.2)`; since `v_k(Q_{k+m}) = 0`, we have `lim_← Q_k = 0`, whence a topological isomorphism
`lim_← (H/R_k) ⥲ lim_← H_k`. But since the filtration `(R_k)` of `H` is `𝔍`-good, it defines on `H` the `𝔍`-preadic
topology; therefore `lim_← (H/R_k)` is the Hausdorff completion of `H` for the `𝔍`-preadic topology, which completes the
proof of (4.1.7).

**(4.1.8)**

<!-- label: III.4.1.8 -->

We now pass to the proof of (4.1.5). For every affine open set `V` of `Y`, `Γ(V, (R^n f_*(ℱ))^∧)` is the Hausdorff
completion of `Γ(V, R^n f_*(ℱ))` for the `𝔍`-preadic topology (if `𝒥 ∣ V = 𝔍̃`) since `R^n f_*(ℱ)` is a coherent
`𝒪_Y`-module `(I, 10.8.4)`, and `Γ(V, lim_← R^n f_*(ℱ_k)) = lim_← Γ(V, R^n f_*(ℱ_k))` `(0_I, 3.2.6)`; the fact that
`φ_n` is a topological isomorphism then results from (4.1.7) and (1.4.11). On the other hand (again by virtue of
(1.4.11)), it follows from (4.1.7) that the homomorphism `ψ_n` of (4.1.3.3) is an isomorphism, hence `ψ_n` is an
isomorphism by definition of `R^n 𝑓̂_*(ℱ̂)`.

**Corollary (4.1.9).**

<!-- label: III.4.1.9 -->

*Under the hypotheses of (4.1.4), for every affine open set `V` of `Y`, the canonical homomorphism*

```text
  H^n(𝔛 ∩ 𝑓̂^{-1}(V), ℱ̂) → Γ(𝔜 ∩ V, R^n 𝑓̂_*(ℱ̂))
```

*is bijective.*

**Remark (4.1.10).**

<!-- label: III.4.1.10 -->

Let `f : X → Y` be a morphism of finite type of (usual) Noetherian preschemes, and let `ℱ` be a coherent `𝒪_X`-module
whose support is proper over `Y` `(II, 5.4.10)`. We then know (3.2.4) that `R^n f_*(ℱ)` is a coherent `𝒪_Y`-module for
every `n ≥ 0`. Moreover, we may always assume that `ℱ = u_*(𝒢)`, where `𝒢 = u^*(ℱ)` is a coherent `𝒪_Z`-module, `Z`
denoting a suitable closed subprescheme of `X` whose underlying space is `Supp(ℱ)`, and `u : Z → X` the canonical
injection `(I, 9.3.5)`. If we set `𝒢_k = 𝒢 / 𝔍^{k+1} 𝒢` (with `𝔍 = u^*(𝒥) 𝒪_Z`), we have `ℱ_k = u_*(𝒢_k)`,
`R^n f_*(ℱ) = R^n (f ∘ u)_*(𝒢)`, and `R^n f_*(ℱ_k) = R^n (f ∘ u)_*(𝒢_k)` (1.3.4), and finally, taking `(I, 10.9.5)` into
account,

```text
  R^n 𝑓̂_*(ℱ̂) = R^n (f ∘ u)^∧_*(𝒢̂).
```

We may then apply (4.1.5) to `𝒢` and to the proper morphism `f ∘ u`, and we conclude that under these hypotheses, the
results of (4.1.5) are valid for `ℱ` and `f`.

## 4.2. Particular cases and variants

The most useful form of the comparison theorem (4.1.5) is the following:

**Proposition (4.2.1).**

<!-- label: III.4.2.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism, `ℱ` a coherent `𝒪_X`-module. Then, for every
`y ∈ Y` and every `p`, `(R^p f_*(ℱ))_y` is*

<!-- original page 130 -->

*an `𝒪_y`-module of finite type, hence separated for the `𝔪_y`-preadic topology, and we have a canonical topological
isomorphism*

```text
  ((R^p f_*(ℱ))_y)^∧ ⥲ lim_← H^p(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{k+1}))      (4.2.1.1)
                         k
```

*where the first member is the completion of `(R^p f_*(ℱ))_y` for the `𝔪_y`-preadic topology, and at the second member
`f^{-1}(y)` is considered, for every `k ≥ 0`, as the underlying space of the prescheme* *`X ×_Y Spec(𝒪_y / 𝔪_y^{k+1})`
`(I, 3.6.1)`.*

**Proof.** Since `𝒪_y` is a Noetherian local ring and `(R^p f_*(ℱ))_y` is a finitely generated `𝒪_y`-module (3.2.1), the
`𝔪_y`-preadic topology on `(R^p f_*(ℱ))_y` is separated `(0_I, 7.3.5)`. The other assertions are consequences of (4.1.7)
when `Y` is Noetherian and the point `y` is closed, on replacing `Y` by an affine neighbourhood of `y` and taking
`Y' = {y}`, in view of `(G, II, 4.9.1)`. In the general case, set `Y_1 = Spec(𝒪_y)`, `X_1 = X ×_Y Y_1`,
`ℱ_1 = ℱ ⊗_{𝒪_Y} 𝒪_y`, and let `f_1 = f ×_Y 1_{Y_1} : X_1 → Y_1`; `Y_1` is Noetherian and `f_1` is proper
`(II, 5.4.2, (iii))`, and `ℱ_1` is coherent `(0_I, 5.3.11)`. Let `y_1` be the unique closed point of `Y_1`; the
proposition is valid for `f_1`, `y_1`, and `ℱ_1`; we have `𝒪_{y_1} = 𝒪_y`, `f_1^{-1}(y_1) = f^{-1}(y)` `(I, 3.6.5)`, the
preschemes `X ×_Y Spec(𝒪_y / 𝔪_y^{k+1})` and `X_1 ×_{Y_1} Spec(𝒪_{y_1} / 𝔪_{y_1}^{k+1})` being canonically identified
`(I, 3.3.9)`; moreover, `ℱ_1 ⊗_{𝒪_{y_1}} (𝒪_{y_1} / 𝔪_{y_1}^{k+1})` is identified with `ℱ ⊗_{𝒪_y} (𝒪_y / 𝔪_y^{k+1})`
`(I, 9.1.6)`. It remains to see that `R^p f_{1*}(ℱ_1)` is canonically isomorphic to `R^p f_*(ℱ) ⊗_{𝒪_Y} 𝒪_y`, which
results from `(1.4.15)`, the local morphism `Spec(𝒪_y) → Y` being flat `(0_I, 6.7.1 and I, 2.4.2)`.

The following corollary uses the terminology of dimension theory (chap. IV) and will not be applied before chap. IV.

**Corollary (4.2.2).**

<!-- label: III.4.2.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism, `y` a point of `Y`, `r` the dimension of
`f^{-1}(y)`. Then, for every coherent `𝒪_X`-module `ℱ`, the sheaves `R^p f_*(ℱ)` are zero in a neighbourhood of `y` for
every `p > r`.*

**Proof.** Indeed, we then have `H^p(f^{-1}(y), ℱ ⊗ (𝒪_y / 𝔪_y^{k+1})) = 0` `(G, II, 4.15.2)` for every `k`, hence
(4.2.1) the Hausdorff completion of `(R^p f_*(ℱ))_y` for the `𝔪_y`-preadic topology is zero, and as this topology is
separated, we also have `(R^p f_*(ℱ))_y = 0`; whence the conclusion, since `R^p f_*(ℱ)` is coherent `(0_I, 5.2.2)`.

**(4.2.3).** The result (4.2.1) is principally used for `p = 0`; we thus obtain the following corollary:

**Corollary (4.2.4).**

<!-- label: III.4.2.4 -->

*Under the hypotheses of (4.2.1), we have a canonical topological isomorphism*

```text
  ((f_*(ℱ))_y)^∧ ⥲ lim_← Γ(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{k+1})).           (4.2.4.1)
                     k
```

## 4.3. Zariski's connection theorem

The results of this section and of the next generalize well-known theorems of Zariski, and may all be deduced from
(4.2.4). They are consequences of the following theorem:

**Theorem (4.3.1) (Connection theorem).**

<!-- label: III.4.3.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism. Then `ℬ(X) = f_*(𝒪_X)` is a coherent
`𝒪_Y`-algebra.*

<!-- original page 131 -->

*Let `Y'` be the finite `Y`-scheme over `Y` such that `𝒜(Y') = f_*(𝒪_X)`, determined up to `Y`-isomorphism
`(II, 1.3.1 and 6.1.3)`; if `f' = ν(e)` is the `Y`-morphism `X → Y'` deduced from the identity isomorphism
`e : 𝒜(Y') ⥲ f_*(𝒪_X)` `(II, 1.2.7)`, then `f'` is proper, `f'_*(𝒪_X)` is isomorphic to `𝒪_{Y'}`, and the fibres
`f'^{-1}(y')` of the morphism `f'` are connected and non-empty for every `y' ∈ Y'`.*

**Proof.** Let `g : Y' → Y` be the structure morphism. To prove that the homomorphism `θ : 𝒪_{Y'} → f'_*(𝒪_X)` entering
the definition of the morphism `f'` is bijective, it suffices, since `Y'` is affine over `Y`, to prove that
`g_*(θ) : g_*(𝒪_{Y'}) → g_*(f'_*(𝒪_X)) = f_*(𝒪_X)` is the identity `(II, 1.4.2)`; but this results from the definitions
since `g_*(𝒪_{Y'}) = 𝒜(Y')` and `f_*(𝒪_X) = ℬ(X)`. The fact that `ℬ(X)` is coherent is a particular case of the
finiteness theorem (3.2.1). Since `f` is proper and `g` separated, `f'` is proper `(II, 5.4.3, (i))`; to complete the
proof of (4.3.1), it suffices therefore to prove the

**Corollary (4.3.2).**

<!-- label: III.4.3.2 -->

*Under the hypotheses of (4.3.1), suppose in addition that `f_*(𝒪_X)` is isomorphic to `𝒪_Y`. Then the fibres
`f^{-1}(y)` of `f` are connected and non-empty for every `y ∈ Y`.*

**Proof.** The hypothesis that `f_*(𝒪_X)` is isomorphic to `𝒪_Y` already implies that `f` is dominant, hence surjective
since `f` is a closed map. We may reduce, as in (4.2.1), to the case where `y` is closed in `Y`; `f^{-1}(y)`, being a
Noetherian space, has a finite number of connected components, and it is the underlying space of the completion `𝔛`
along `f^{-1}(y)`. If `Z_i` (`1 ≤ i ≤ n`) are these connected components, it is clear that `Γ(𝔛, 𝒪_𝔛)` is the direct sum
of the rings `Γ(Z_i, 𝒪_𝔛)`, and each of these is not reduced to `0`, since the unit section is distinct from `0` at each
point of `X`. Now, if we apply (4.1.5) to `ℱ = 𝒪_X`, whose completion along `f^{-1}(y)` is `𝒪_𝔛`, we see that
`Γ(𝔛, 𝒪_𝔛)` is isomorphic to the Hausdorff `𝔪_y`-adic completion `𝒪̂_y` of the local ring `𝒪_y`; it is therefore a local
ring which cannot be a direct sum of several rings not reduced to `0` (otherwise it would have several distinct maximal
ideals). We thus have `n = 1`, which proves the corollary.

**Corollary (4.3.3).**

<!-- label: III.4.3.3 -->

*Under the hypotheses of (4.3.1), for every `y ∈ Y`, the set of connected components of the fibre `f^{-1}(y)` is in
one-to-one correspondence with the finite set of points of the fibre `g^{-1}(y)`, where `g : Y' → Y` is the structure
morphism (in other words, the set of maximal ideals of `(f_*(𝒪_X))_y`).*

**Proof.** Since `Y'` is finite over `Y`, we know indeed that `g^{-1}(y)` is a finite discrete space `(II, 6.1.7)`.
Since `f^{-1}(y) = f'^{-1}(g^{-1}(y))`, the corollary follows from this remark and from (4.3.1).

We thus have a remarkable interpretation of the `Y`-prescheme `Y'` defined in (4.3.1). The factorization `f = g ∘ f'` of
the proper morphism `f` is analogous to the factorization obtained by K. Stein for holomorphic maps of analytic spaces,
and we shall call it henceforth the *Stein factorization* of `f`.

**Remark (4.3.4).**

<!-- label: III.4.3.4 -->

Let `k` be an extension of the field `κ(y)`: if the prescheme `f^{-1}(y) ⊗_{κ(y)} k = f^{-1}(y) ×_Y Spec(k)` is
connected, then so is `f^{-1}(y)`, which is its image under a projection morphism `(I, 3.4.7)`. We shall say that, for a
morphism `f : X → Y` of preschemes and a point `y ∈ Y`, the fibre `f^{-1}(y)` is *geometrically connected* if, for every
extension `k` of `κ(y)`, the prescheme `f^{-1}(y) ⊗_{κ(y)} k = f^{-1}(y) ×_Y Spec(k)` is connected.

<!-- original page 132 -->

Under the hypotheses of (4.3.2), one may then strengthen its conclusion: the fibres `f^{-1}(y)` are in fact
*geometrically connected*. To see this, observe that for every extension `k` of `κ(y)`, there exists a Noetherian local
ring `A` and a local homomorphism `φ : 𝒪_y → A` which makes `A` a flat `𝒪_y`-module and such that the residue field of
`A` is `κ(y)`-isomorphic to `k` `(0_III, 10.3.1)`. Let then `Y_1 = Spec(A)` and let `h : Y_1 → Y` be the local morphism
corresponding to `φ`, transforming the unique closed point of `Y_1` into `y` `(I, 2.4.1)`; set `X_1 = X ×_Y Y_1` and
`f_1 = f ×_Y 1_{Y_1}`; `f_1` is proper `(II, 5.4.2, (iii))` and `f_1^{-1}(y_1)` is a `κ(y_1)`-prescheme isomorphic to
`X ×_Y Spec(k)`. It thus suffices to show that `f_{1*}(𝒪_{X_1}) = 𝒪_{Y_1}` in order to apply (4.3.2) to `f_1`. Now, `h`
is a flat morphism, as follows from `(I, 2.4.2)` and `(1.4.15.5)`; we therefore have
`f_{1*}(𝒪_{X_1}) = h^*(f_*(𝒪_X)) = h^*(𝒪_Y) = 𝒪_{Y_1}` by virtue of `(1.4.15)` applied for `q = 0`.

In the general case (4.3.1), the same reasoning shows that we have (with the notation of (4.3.1))
`f_{1*}(𝒪_{X_1}) = h^*(f_*(𝒪_X))`, and the Stein factorization `f_1 = g_1 ∘ f'_1` of `f_1` is such that
`g_1 = g ×_Y 1_{Y_1}` `(II, 1.5.2)`, the corresponding finite `Y_1`-scheme being `Y'_1 = Y' ×_Y Y_1`. Taking the
transitivity of fibres `(I, 3.6.4)` into account, we therefore see that the number of connected components of
`f_1^{-1}(y_1)` is, by virtue of (4.3.3), equal to the number of elements of `g_1^{-1}(y_1) = g^{-1}(y) ⊗_{κ(y)} k`. If
we take for `k` an algebraically closed extension of `κ(y)`, this number is independent of the algebraically closed
extension considered and equal to the *geometric number of points* of `g^{-1}(y)` `(I, 6.4.7)`, or again to the sum of
the separable ranks `[κ(y'_i) : κ(y)]_s` where `y'_i` runs over the finite set `g^{-1}(y)`. We also say that this number
is the *geometric number of connected components* of `f^{-1}(y)`. Note that the `κ(y'_i)` are none other than the
residue fields of the semi-local ring `(f_*(𝒪_X))_y`.

**Proposition (4.3.5).**

<!-- label: III.4.3.5 -->

*Let `X` and `Y` be two locally Noetherian integral preschemes and `f : X → Y` a proper dominant morphism. For every
`y ∈ Y`, the number of connected components of `f^{-1}(y)` is at most equal to the number of maximal ideals of the
integral closure `𝒪'_y` of `𝒪_y` in the field of rational functions `R(X)`.*

**Proof.** Indeed, for every open set `U` of `Y`, `Γ(U, f_*(𝒪_X)) = Γ(f^{-1}(U), 𝒪_X)` is the intersection of the local
rings `𝒪_x` such that `x ∈ f^{-1}(U)` `(I, 8.2.1.1)`. We thus conclude immediately that the stalk `(f_*(𝒪_X))_y` is a
subring of `R(X)` containing `𝒪_y`. Moreover, since `f_*(𝒪_X)` is a coherent `𝒪_Y`-module, `(f_*(𝒪_X))_y` is a finitely
generated `𝒪_y`-module, and is therefore contained in `𝒪'_y`; we know ([13], vol. I, p. 257 and 259) that every maximal
ideal of such a ring `A` is the intersection of `A` and a maximal ideal of `𝒪'_y`, whence the proposition.

**Definition (4.3.6).**

<!-- label: III.4.3.6 -->

*We say that an integral local ring is *unibranch* if its integral closure is a local ring. We say that a point `y` of
an integral prescheme `Y` is *unibranch* if the local ring `𝒪_y` is unibranch (which is in particular the case when `Y`
is normal at the point `y`).*

Let `A` be an integral local ring, and let `K` be its field of fractions; for `A` to be unibranch, it is necessary and
sufficient that every subring `A_1` of `K` containing `A` and which is a finite `A`-algebra be a local ring. Indeed, let
`A'` be the integral closure of `A`; it follows from the first Cohen–Seidenberg theorem (Bourbaki, *Alg. comm.*, chap.
V, § 2, n° 1, th. 1) that every maximal ideal of `A_1` is the trace of a maximal ideal of `A'`, so if `A'` is local,
then so is `A_1`. Conversely, `A'` is the inductive limit

<!-- original page 133 -->

of the increasing filtered family of finite sub-`A`-algebras `A_1` of `A'`, and if each of the `A_1` is a local ring,
the maximal ideal of `A_1` is the trace on `A_1` of that of `A_2`, for `A_1 ⊂ A_2`, by the same reasoning as above, so
`A'` is a local ring `(0_I, 10.3.1.3)`.

Note that if the completion of a Noetherian local ring `A` is integral (which we express by saying that `A` is
*analytically integral*), then `A` is unibranch. Indeed, let `𝔪` be the maximal ideal of `A`, `K` its field of
fractions, `K'` the field of fractions of `Â`; we then have `K' = K ⊗_A Â`. Let `A_1` be a finite sub-`A`-algebra of
`K`. The subring `B_1` of `K'` generated by `Â` and `A_1` is isomorphic to `A_1 ⊗_A Â`; it is an `Â`-module of finite
type, the completion of `A_1` for the `𝔪`-adic topology `(0_I, 7.3.3 and 7.3.6)`. Since `A_1` is a semi-local ring
(Bourbaki, *Alg. comm.*, chap. IV, § 2, n° 5, cor. 3 of prop. 9) and its completion is integral, `A_1` can have only one
maximal ideal `𝔪_1`, and we have `𝔪̂_1 ∩ A = 𝔪`; whence our assertion.

**Corollary (4.3.7).**

<!-- label: III.4.3.7 -->

*Under the hypotheses of (4.3.5), suppose that the algebraic closure of `R(Y)` in `R(X)` is of separable degree `n`, and
that `y ∈ Y` is unibranch. Then the fibre `f^{-1}(y)` has at most `n` connected components. In particular, if the
algebraic closure of `R(Y)` in `R(X)` is radicial over `R(Y)`, then `f^{-1}(y)` is connected.*

**Proof.** Indeed, let `𝒪'_y` be the integral closure of `𝒪_y`; the integral closure `𝒪̃_y` of `𝒪_y` in `R(X)` is also
that of `𝒪'_y`; but we know that if `𝒪'_y` is a local ring, then `𝒪̃_y` is a semi-local ring whose number of maximal
ideals is at most equal to `n` ([13], vol. I, p. 289, th. 22).

This corollary is essentially the form in which Zariski states his "connection theorem" for algebraic schemes.

**Remark (4.3.8).**

<!-- label: III.4.3.8 -->

If one adds to the hypotheses of (4.3.7) the hypothesis that `Y` is normal at `y`, the fibre `f^{-1}(y)` is
*geometrically connected*, since (with the notation of (4.3.4)) `g^{-1}(y)` is reduced to a point `y'` and `κ(y')` is
radicial over `κ(y)`.

**Definition (4.3.9).**

<!-- label: III.4.3.9 -->

*Given a locally Noetherian prescheme `Y`, we say that a morphism of finite type `f : X → Y` is *universally open* if,
for every irreducible locally Noetherian prescheme `Y'` and every dominant morphism `g : Y' → Y`, every irreducible
component of `X' = X ×_Y Y'` dominates `Y'`.*

If `Y` is irreducible, this comes to saying that if `η`, `η'` are the generic points of `Y` and `Y'` respectively (so
that `g(η') = η`), and if we set `f' = f_{(Y')}`, every irreducible component of `X'` meets `f'^{-1}(η')`
`(0_I, 2.1.8)`; this implies that for every open set `U` of `Y`, the morphism `f^{-1}(U) → U`, restriction of `f`, is
universally open.

**Corollary (4.3.10).**

<!-- label: III.4.3.10 -->

*Let `X`, `Y` be two locally Noetherian integral preschemes, `f : X → Y` a proper dominant universally open morphism. If
the algebraic closure of `R(Y)` in `R(X)` is radicial over `R(Y)`, every fibre `f^{-1}(y)` (`y ∈ Y`) is geometrically
connected.*

**Proof.** We may restrict to the case where `Y = Spec(B)`, `B` being an integral Noetherian ring. It then follows from
`(II, 7.1.7)` that there exists an integrally closed Noetherian local ring `A` which dominates `𝒪_y` and has `R(Y)` for
field of fractions. Let `Y' = Spec(A)`, and let `h : Y' → Y` be the morphism corresponding to the canonical injection
`B → A`, which is birational (hence dominant); moreover, if `y'` is the unique closed point of `Y'`, we have
`h(y') = y`. Let

<!-- original page 134 -->

`X' = X ×_Y Y'`, `f' = f ×_Y 1_{Y'}`; denote by `η`, `η'`, `ξ` the generic points of `Y`, `Y'`, and `X` respectively, so
that `f(ξ) = η` and `h^{-1}(η) = {η'}`; moreover, `κ(η') = κ(η) = R(Y)`, so `f'^{-1}(η')` is isomorphic to `f^{-1}(η)`
`(I, 3.6.4)`, and in particular, since `ξ` is the generic point of `f^{-1}(η)` `(0_I, 2.1.8)`, `f'^{-1}(η')` has a
single generic point. But by hypothesis, every irreducible component of `X'` has its generic point in `f'^{-1}(η')`, so
`X'` is necessarily irreducible, its generic point `ξ'` is the generic point of `f'^{-1}(η')`, and we have
`κ(ξ') = κ(ξ)`. Set `X'' = X'_{red}`; `X''` is then integral and Noetherian, `f''` is proper `(II, 5.4.6)` and the
underlying spaces of the fibres `f''^{-1}(y')` and `f'^{-1}(y')` are the same; moreover, `R(X'') = κ(ξ') = R(X)`, so
`f''` satisfies the hypotheses of (4.3.8), and `f''^{-1}(y')` is geometrically connected. Now let `k` be an arbitrary
extension of `κ(y)`; there exists an extension `k_1` of `κ(y')` such that `κ(y)` and `k` can be considered as
subextensions of `k_1` (Bourbaki, *Alg.*, chap. V, § 4, prop. 2). By hypothesis, `f''^{-1}(y') ×_{Y'} Spec(k_1)` is
connected, and it has the same reduced prescheme as `f'^{-1}(y') ×_{Y'} Spec(k_1)` `(I, 5.1.8)`, so the latter is
connected, and since it is isomorphic to `f^{-1}(y) ×_Y Spec(k_1)` `(I, 3.6.4)`, we conclude that the latter is
connected; *a fortiori*, the same holds for `f^{-1}(y) ×_Y Spec(k)` by the remark at the beginning of (4.3.4), which
completes the proof.

**Remarks (4.3.11).**

<!-- label: III.4.3.11 -->

(i) The preceding reasoning is due in substance to Zariski [20], except that he can take for `A` the integral closure of
`𝒪_y`, the latter being a Noetherian ring for the local rings of classical algebraic geometry. On the other hand,
Zariski proves that if `Y` is the Chow variety of a projective space `P^r_k` over a field `k`, and if `X` is the closed
part of `P^r_k × Y` which defines the Chow correspondence between `P^r_k` and `Y`, then the projection `X → Y` is a
universally open morphism (loc. cit., lemma on p. 82). It appears indeed to be the only formal property of "Chow
coordinates" that has been used in certain applications; consequently, in such a situation, it is of interest to
substitute the language of *fibres of a proper morphism* (possibly assumed universally open or subject to other
analogous restrictions of local regularity) for the language of *specialization of cycles in projective space*.

(ii) In chap. IV, we shall see that a universally open morphism `f : X → Y` may also be defined in the following way
(which justifies the terminology): for every morphism `Z → Y`, the morphism `f_{(Z)} : X_{(Z)} → Z` is open. One may
moreover show that if `f` satisfies the hypotheses of (4.3.10), then if `y`, `y'` are two points of `Y` such that `y'`
is a specialization of `y`, the *geometric number of connected components* of `f^{-1}(y')` is at most equal to that of
the connected components of `f^{-1}(y)`.

**Corollary (4.3.12).**

<!-- label: III.4.3.12 -->

*Under the hypotheses of (4.3.5), suppose in addition that `R(Y)` is algebraically closed in `R(X)`, and let `y` be a
normal point of `Y`. Then `f^{-1}(y)` is geometrically connected, and there exists an open neighbourhood `U` of `y` in
`Y` such that `f_*(𝒪_X)(f^{-1}(U))` is isomorphic to `𝒪_Y ∣ U`. More particularly, if we assume `Y` normal (and `R(Y)`
algebraically closed in `R(X)`), then `f_*(𝒪_X)` is isomorphic to `𝒪_Y`.*

**Proof.** The first assertion relative to `f^{-1}(y)` is a particular case of (4.3.8). We

<!-- original page 135 -->

deduce that if `f : X → Y' → Y` is the Stein factorization of `f` (4.3.3), `g^{-1}(y)` is reduced to a single point
`y'`; moreover, we have `𝒪_y ⊂ 𝒪_{y'} = (f_*(𝒪_X))_y ⊂ R(X)`, and since `𝒪_{y'}` is finite over `𝒪_y` (and *a fortiori*
over `R(Y)`), it is contained in `R(Y)` by virtue of the hypothesis; since `y` is normal, we necessarily have
`𝒪_{y'} = 𝒪_y`, from which we conclude that `g` is a local isomorphism at the point `y'` `(I, 6.5.4)`, which completes
the proof of the first part of the corollary. The second results from the first, for the additional hypothesis implies
that `g` is bijective and a local isomorphism in the neighbourhood of every point of `Y'`, hence an isomorphism.

The fact that (4.3.7) is established in the framework of schemes permits applications such as the following:

**Proposition (4.3.13).**

<!-- label: III.4.3.13 -->

*Let `A` be a Noetherian unibranch local ring, `𝔞` an ideal of definition of `A`, `A_0 = A/𝔞`, `S = gr_𝔞(A)` the graded
ring associated to `A` for the `𝔞`-preadic filtration; `S` is a graded `A_0`-algebra generated by `S_1`, `S_1` being a
finitely generated `A_0`-module. Then `Proj(S)` is a connected `A_0`-scheme.*

**Proof.** Let `𝔪` be the maximal ideal of `A`; `Y = Spec(A)` is an integral scheme whose point corresponding to `𝔪` is
the unique closed point. By hypothesis, we have `𝔪^p ⊂ 𝔞 ⊂ 𝔪` for an integer `p`, so `V(𝔞) = {𝔪}`. Let
`S' = ⊕_{n ≥ 0} 𝔞^n`, and let `X = Proj(S')`, which is the `Y`-scheme obtained by blowing up the ideal `𝔞`; `X` is
integral and the structure morphism `f : X → Y` is birational `(II, 8.1.4)` and obviously projective. Consequently,
(4.3.7) is applicable and shows that `f^{-1}(𝔪)` is connected; but the space `f^{-1}(𝔪)` is the underlying space of
`Proj(S' ⊗_A A_0)` `(I, 3.6.1 and II, 2.8.10)`; since `S' ⊗_A A_0 = S` by definition, the proposition is proved.

## 4.4. Zariski's "main theorem"

**Proposition (4.4.1).**

<!-- label: III.4.4.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism. Let `X'` be the set of points `x ∈ X` which
are isolated in their fibre `f^{-1}(f(x))`. Then the set `X'` is open in `X`, and if `f = g ∘ f'` is the Stein
factorization of `f` (4.3.3), the restriction of `f'` to `X'` is an isomorphism of `X'` onto a subprescheme induced on
an open set `U` of `Y'`, and we have `X' = f'^{-1}(U)`.*

**Proof.** Since `g^{-1}(f(x))` is finite and discrete (4.3.3 and `II, 6.1.7`), for `x` to be isolated in
`f^{-1}(f(x))`, it is necessary and sufficient that it be isolated in `f'^{-1}(f'(x))`; we may thus restrict to the case
where `f' = f`, hence `f_*(𝒪_X) = 𝒪_Y`. Then, if `x ∈ X'`, `f^{-1}(f(x))`, which is connected (4.3.2), is necessarily
reduced to the point `x`. Since `f` is closed, for every open neighbourhood `V` of `x` in `X`, `f(X − V)` is closed in
`Y` and does not contain `y = f(x)`, since `f^{-1}(y) = {x}`; if `U` is the complement of `f(X − V)` in `Y`, we have
`f^{-1}(U) ⊂ V`, and we conclude that the inverse images by `f` of a fundamental system of open neighbourhoods of `y`
form a fundamental system of open neighbourhoods of `x`. The hypothesis `f_*(𝒪_X) = 𝒪_Y` and the definition of the
direct image of a sheaf `(0_I, 3.4.1 and 4.2.1)` then imply that, if `f = (ψ, θ)`, the homomorphism `θ_x^♯ : 𝒪_y → 𝒪_x`
is an isomorphism. We conclude that there exists an open neighbourhood `V` of `x` and an open neighbourhood `U` of `y`
such that the restriction of `f` to `V` is an isomorphism of `V` onto `U` `(I, 6.5.4)`; furthermore, by what we have
just seen,

<!-- original page 136 -->

we may suppose `f^{-1}(U) = V`, whence we conclude immediately, by definition, that `V ⊂ X'`, which completes the proof.

The following proposition was proved by Chevalley in the case of algebraic schemes:

**Proposition (4.4.2).**

<!-- label: III.4.4.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism. The following conditions are equivalent:*

*a) `f` is finite.*

*b) `f` is affine and proper.*

*c) `f` is proper and, for every `y ∈ Y`, `f^{-1}(y)` is a finite set.*

**Proof.** We know that a) implies b) `(II, 6.1.2 and 6.1.11)`. If `f` is proper and affine, the same holds for the
morphism `f^{-1}(y) → Spec(κ(y))` `(II, 1.6.2, (iii) and 5.4.2, (iii))`, and the finiteness theorem (3.2.1) applied to
the structure sheaf of `f^{-1}(y)` shows that `f^{-1}(y) = Spec(A)`, where `A` is a finite `κ(y)`-algebra; hence
`f^{-1}(y)` is a finite set `(II, 6.1.7)`, and we see that b) implies c). Finally, since `f^{-1}(y)` is an algebraic
prescheme over `κ(y)`, the hypothesis that the set `f^{-1}(y)` is finite implies that the space `f^{-1}(y)` is discrete
`(I, 6.4.4)`. With the notation of (4.4.1), we therefore have `X' = X`, and `f' : X → Y'` is an isomorphism; since `g`
is a finite morphism, we see that c) implies a).

**Theorem (4.4.3) ("Main theorem" of Zariski).**

<!-- label: III.4.4.3 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a quasi-projective morphism, `X'` the set of points `x ∈ X` which are
isolated in their fibre `f^{-1}(f(x))`. Then `X'` is an open part of `X`, and the subprescheme induced `X'` is
isomorphic to a prescheme induced on an open part of a `Y`-prescheme `Y'` finite over `Y`.*

**Proof.** The hypothesis implies that there exists a projective `Y`-prescheme `Z` such that `X` is `Y`-isomorphic to a
subprescheme induced on an open set of `Z` `(II, 5.3.2 and 5.5.1)`. We are thus reduced to proving the theorem when `f`
is a projective morphism, hence proper `(II, 5.5.3)`, and it then follows at once from (4.4.1).

**Remark (4.4.4).**

<!-- label: III.4.4.4 -->

If `X` is reduced (resp. irreducible, and `X'` non-empty), one may suppose, in the statement of (4.4.3), that `Y'` is
reduced (resp. irreducible). Indeed, one may always replace `Y'` by the subprescheme closure `X̄'` of `X'` in `Y'`
`(I, 9.5.11 and II, 6.1.5, (i) and (ii))`, and one knows that if `X'` is reduced, the same holds for `X̄'`
`(I, 9.5.9, (i))`; on the other hand, if `X'` is non-empty, it is irreducible if `X` is, and `X̄'` is then also
irreducible.

**Corollary (4.4.5).**

<!-- label: III.4.4.5 -->

*Let `Y` be a locally Noetherian scheme, `f : X → Y` a morphism of finite type, `x` a point of `X` isolated in its fibre
`f^{-1}(f(x))`. Then there exists an open neighbourhood of `x` in `X` which is isomorphic to an open part of a
`Y`-prescheme finite over `Y`.*

**Proof.** Let `y = f(x)`, `U` an affine open neighbourhood of `y` in `Y`, `V` an affine open neighbourhood of `x` in
`X`, contained in `f^{-1}(U)`. Since `Y` is separated, the injection `U → Y` is affine `(II, 1.6.3)`, and since `V` is
affine over `U` (*ibid.*), the restriction of `f` to `V` is an affine morphism `V → Y` `(II, 1.6.2, (ii))`; *a
fortiori*, this restriction is a quasi-projective morphism since it is of finite type `(I, 6.3.5 and II, 5.3.4, (i))`.
It then suffices to apply (4.4.3) to this restriction.

Corollary (4.4.5) may be stated in the language of commutative algebra:

<!-- original page 137 -->

**Corollary (4.4.6).**

<!-- label: III.4.4.6 -->

*Let `A` be a Noetherian ring, `B` an `A`-algebra of finite type, `𝔮` a prime ideal of `B`, `𝔭` its inverse image in
`A`. Suppose that `𝔮` is both maximal and minimal in the set of prime ideals of `B` whose inverse image is `𝔭`. Then
there exist `g ∈ B − 𝔮`, a finite `A`-algebra `A'`, and an element `f' ∈ A'` such that the `A`-algebras `B_g` and
`A'_{f'}` are isomorphic.*

**Proof.** It suffices to apply (4.4.5) to `Y = Spec(A)` and `X = Spec(B)`, the hypothesis on `𝔮` meaning exactly that
`𝔮` is isolated in its fibre `(I, 1.1.7)`.

We deduce the following less general-looking result:

**Corollary (4.4.7).**

<!-- label: III.4.4.7 -->

*Let `A` be a Noetherian local ring, `B` an `A`-algebra of finite type, `𝔫` a prime ideal of `B` whose inverse image in
`A` is the maximal ideal `𝔪`. Suppose that `𝔫` is maximal in `B` and is minimal in the set of prime ideals of `B` whose
inverse image is `𝔪` (which also means that `B_𝔫` is primary for `𝔫`). Then there exists a finite `A`-algebra `A'` and a
maximal ideal `𝔪'` of `A'` (of which `𝔪` is the inverse image in `A`) such that `B_𝔫` is isomorphic to the `A`-algebra
`A'_{𝔪'}`.*

The following particular case of (4.4.7) is also sometimes called the "Main Theorem":

**Corollary (4.4.8).**

<!-- label: III.4.4.8 -->

*Under the conditions of (4.4.7), suppose in addition that `A` and `B` are integral and have the same field of fractions
`K`. Then, if `A` is integrally closed, we have `B_𝔫 = A`.*

**Proof.** Indeed, Remark (4.4.4) shows that we may suppose, in the application of (4.4.7), that `A'` is integral and
has `K` for field of fractions; the hypothesis on `A` then implies `A' = A`, hence `B_𝔫 = A`; since we have
`A ⊂ B ⊂ B_𝔫`, we indeed conclude `A = B`.

The statement (4.4.8) is the form given by Zariski to his "Main theorem" (extended to arbitrary Noetherian integral
local rings).

The preceding corollaries were local-type variants of (4.4.3), which is a global result. Here is another consequence of
global nature:

**Corollary (4.4.9).**

<!-- label: III.4.4.9 -->

*Let `Y` be a locally Noetherian integral prescheme, `f : X → Y` a separated morphism, of finite type and birational.
Suppose in addition `Y` normal and all the fibres `f^{-1}(y)` finite for `y ∈ Y`. Then `f` is an open immersion; if in
addition `f` is closed (in particular if `f` is proper), `f` is an isomorphism.*

**Proof.** Indeed, let `x ∈ X`, and set `y = f(x)`. Since `f^{-1}(y)` is an algebraic scheme over `κ(y)`, the hypothesis
that it is finite implies that it is discrete `(I, 6.4.4)`; in addition, `𝒪_y` is integrally closed and `𝒪_x` and `𝒪_y`
have the same field of fractions `(I, 7.1.5)`. We may thus apply (4.4.8), and if `f = (ψ, θ)`, the homomorphism
`θ_x^♯ : 𝒪_y → 𝒪_x` is bijective; we conclude `(I, 6.5.4)` that `f` is a local isomorphism. But since `f` is separated
and `X` integral, `f` is an open immersion `(I, 8.2.8)`. The last assertion follows from the fact that `f` is dominant.

**Proposition (4.4.10).**

<!-- label: III.4.4.10 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type. The set `X'` of `x ∈ X`
isolated in their fibre `f^{-1}(f(x))` is open in `X`.*

**Proof.** The question being local on `X` and `Y`, we may suppose `X` and `Y` affine Noetherian and `f` of finite type;
`f` is then an affine morphism of finite type, hence quasi-projective `(II, 5.3.4, (i))`, and it suffices to apply
(4.4.3).

<!-- original page 138 -->

**Corollary (4.4.11).**

<!-- label: III.4.4.11 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism. The set `U` of points `y ∈ Y` such that
`f^{-1}(y)` is discrete is open in `Y`, and the morphism `f^{-1}(U) → U` restriction of `f` is finite. In particular, a
proper and quasi-finite morphism `X → Y` is finite.*

**Proof.** Indeed, the complement of `U` in `Y` is the image by `f` of `X − X'` which is closed in `X` by virtue of
(4.4.10); since `f` is a closed map, `U` is open. Moreover, it follows from `(II, 6.2.2)` that `f^{-1}(y)` is finite for
every `y ∈ U`; since the morphism `f^{-1}(U) → U` restriction of `f` is proper `(II, 5.4.1)`, it is finite by virtue of
(4.4.2).

**Remarks (4.4.12).**

<!-- label: III.4.4.12 -->

(i) As announced in `(II, 6.2.7)`, we shall show in chap. V that if `Y` is locally Noetherian, every quasi-finite and
separated morphism `f : X → Y` is quasi-affine, hence quasi-projective. It will then follow that, in the Main Theorem
(4.4.3), the conclusion remains valid when one supposes only `f` separated and of finite type. Indeed, it follows from
(4.4.10) that `X'` is open in `X`, and since `X` is locally Noetherian, the restriction of `f` to `X'` is again of
finite type `(I, 6.3.5)`, hence quasi-finite by definition of `X'`, and obviously separated; one may therefore apply
(4.4.3) to this restriction, whence the conclusion.

(ii) We shall give in chap. IV a more elementary proof of (4.4.10), using dimension theory.

## 4.5. Completions of modules of homomorphisms

**Proposition (4.5.1).**

<!-- label: III.4.5.1 -->

*Let `A` be a Noetherian ring, `𝔍` an ideal of `A`, `X` an `A`-prescheme of finite type, `ℱ`, `𝒢` two coherent
`𝒪_X`-modules whose supports have a proper intersection over `Y = Spec(A)` `(II, 5.4.10)`. Then, for every integer
`n ≥ 0`, `Ext_{𝒪_X}^n(X; ℱ, 𝒢)` is an `A`-module of finite type, and its Hausdorff completion for the `𝔍`-preadic
topology is canonically identified (with the notation of (4.1.7)) with `Ext_{𝒪_𝔛}^n(𝔛; ℱ̂, 𝒢̂)`.*

**Proof.** We know `(T, 4.2)` that there exists a biregular spectral sequence `E(ℱ, 𝒢)` whose abutment is
`Ext_{𝒪_X}^•(X; ℱ, 𝒢)` and whose `E_2` terms are given by `E_2^{p,q} = H^p(X, 𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢))`. We know that
`𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢)` is a coherent `𝒪_X`-module `(0_III, 12.3.3)` whose support is contained in the intersection of those
of `ℱ` and `𝒢` `(T, 4.2.2)`, and is consequently proper over `Y` `(II, 5.4.10)`. We conclude from (3.2.4) that the
`E_2^{p,q}` are `A`-modules of finite type, and consequently `(0_III, 11.1.8)` so are all the terms `E_r^{p,q}` of the
spectral sequence and its abutment. On the other hand, if `i : 𝔛 → X` is the canonical morphism, `ℱ̂` and `𝒢̂` are
canonically identified with `i^*(ℱ)` and `i^*(𝒢)`, and `i` is flat `(I, 10.8.8 and 10.8.9)`. We then know
`(0_III, 12.3.4)` that for every `q ≥ 0`, there exists a canonical `i`-morphism
`ω_q : 𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢) → 𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂)`, and that the corresponding `𝒪_𝔛`-homomorphism
`ω_q^♯ : i^*(𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢)) → 𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂)` is an isomorphism `(0_III, 12.3.5)`; in other words
`(I, 10.8.8)`, `𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂)` is canonically identified with the completion `(𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢))^∧` (with the
notation of (4.1.7)). We then conclude from the comparison theorem (4.1.10) that for every `p ≥ 0`,
`H^p(𝔛, 𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂))` is canonically identified with the Hausdorff completion

<!-- original page 139 -->

of `H^p(X, 𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢))` for the `𝔍`-preadic topology. If we denote by `E(ℱ̂, 𝒢̂)` the biregular spectral sequence
defined in `(T, 4.2)` relative to `ℱ̂` and `𝒢̂`, we therefore see that if `Â` denotes the Hausdorff completion of `A`
for the `𝔍`-preadic topology, we have, up to canonical isomorphism, `E_2^{p,q}(ℱ̂, 𝒢̂) = E_2^{p,q}(ℱ, 𝒢) ⊗_A Â`
`(0_I, 7.3.3)`.

This being so, we know that the data of the flat morphism `i` defines a canonical homomorphism of spectral sequences

```text
  φ : E(ℱ, 𝒢) → E(ℱ̂, 𝒢̂) = E(i^*(ℱ), i^*(𝒢))
```

which, for the `E_2`-terms (resp. the abutment), reduces to the homomorphism

```text
  ω_q^♯♯ : H^p(X, 𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢)) → H^p(𝔛, 𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂))
```

(resp. `u_n : Ext_{𝒪_X}^n(X; ℱ, 𝒢) → Ext_{𝒪_𝔛}^n(𝔛; ℱ̂, 𝒢̂)`) deduced from `ω_q` (resp. `u_0`) by functoriality
`(0_III, 12.3.4)`. By tensoring with `Â`, the `ω_q^♯♯` and `u_n` give homomorphisms of `A`-modules

```text
  ω̃_q^♯♯ : E_2^{p,q}(ℱ, 𝒢) ⊗_A Â → E_2^{p,q}(ℱ̂, 𝒢̂),
  ũ_n   : Ext_{𝒪_X}^n(X; ℱ, 𝒢) ⊗_A Â → Ext_{𝒪_𝔛}^n(𝔛; ℱ̂, 𝒢̂).
```

Since `Â` is a flat `A`-module `(0_I, 7.3.3)`, the `A`-modules `E_r^{p,q}(ℱ, 𝒢) ⊗_A Â` form a biregular spectral
sequence with abutment the `Ext_{𝒪_X}^n(X; ℱ, 𝒢) ⊗_A Â`, and the `ω̃_q^♯♯` and `ũ_n` a morphism of spectral sequences.
Since the `ω̃_q^♯♯` are isomorphisms, so are the `ũ_n` `(0_III, 11.1.5)`.

**Corollary (4.5.2).**

<!-- label: III.4.5.2 -->

*Under the hypotheses of (4.5.1), suppose in addition that `A` is a Noetherian `𝔍`-adic ring. Then, for every integer
`n ≥ 0`, `Ext_{𝒪_X}^n(X; ℱ, 𝒢)` is canonically identified with `Ext_{𝒪_𝔛}^n(𝔛; ℱ̂, 𝒢̂)`.*

**Proof.** It suffices to remark that `Ext_{𝒪_X}^n(X; ℱ, 𝒢)`, being an `A`-module of finite type, is separated and
complete for the `𝔍`-preadic topology `(0_I, 7.3.6)`.

The particular case `n = 0` of (4.5.1) is stated as follows:

**Corollary (4.5.3).**

<!-- label: III.4.5.3 -->

*Under the hypotheses of (4.5.1), for every homomorphism `u : ℱ → 𝒢`, denote by `û` the completed homomorphism `ℱ̂ → 𝒢̂`
`(I, 10.8.4)`. Then we have a canonical isomorphism*

```text
  (Hom_{𝒪_X}(ℱ, 𝒢))^∧ ⥲ Hom_{𝒪_𝔛}(ℱ̂, 𝒢̂)                                     (4.5.3.1)
```

*where the first member is the Hausdorff completion for the `𝔍`-preadic topology of the `A`-module `Hom_{𝒪_X}(ℱ, 𝒢)`,
this isomorphism being obtained by passage to Hausdorff completions from the homomorphism `u ↦ û`.*

## 4.6. Relations between formal morphisms and usual morphisms

**Proposition (4.6.1).**

<!-- label: III.4.6.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism, `ℱ` a coherent `𝒪_X`-module and `f`-flat, `y`
a point of `Y`. Suppose that for some*

<!-- original page 140 -->

*integer `n`, we have `H^n(f^{-1}(y), ℱ ⊗_{𝒪_X} κ(y)) = 0`. Then there exists a neighbourhood `U` of `y` in `Y` such
that `R^n f_*(ℱ) ∣ U = 0`, and for every integer `p ≥ 0`, the canonical homomorphism*

```text
  (R^{n-1} f_*(ℱ))_y → H^{n-1}(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{p+1}))
```

*of (4.2.1.1) is surjective.*

**Proof.** Since `R^n f_*(ℱ)` is a coherent `𝒪_Y`-module (3.2.1), the first assertion of the proposition will be
established if we prove that `(R^n f_*(ℱ))_y = 0` `(0_I, 5.2.2)`; by virtue of (4.2.1), it suffices to prove that
`H^n(f^{-1}(y), ℱ ⊗ (𝒪_y / 𝔪_y^{p+1})) = 0` for every `p`. This is true by hypothesis for `p = 0`; we shall prove it by
induction on `p`. Set `X_p = X ×_Y Spec(𝒪_y / 𝔪_y^{p+1})`, so that `X_{p-1}` is a closed subprescheme of `X_p`, having
the same underlying space `(I, 3.6.1)`; the induction hypothesis `H^n(X_{p-1}, ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^p)) = 0` therefore
entails `H^n(X_p, ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^p)) = 0`; on the other hand, the exact sequence in cohomology gives, from the
exact sequence

```text
  0 → 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ → ℱ / 𝔪_y^{p+1} ℱ → ℱ / 𝔪_y^p ℱ → 0
```

of `𝒪_X`-modules, the exact sequence

```text
  H^n(X_p, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) → H^n(X_p, ℱ / 𝔪_y^{p+1} ℱ) → H^n(X_p, ℱ / 𝔪_y^p ℱ)
```

and it will suffice to show that we have

```text
  H^n(X_p, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) = 0                                        (4.6.1.1)
```

for then `H^n(X_p, ℱ / 𝔪_y^{p+1} ℱ)` will be a submodule of `H^n(X_p, ℱ / 𝔪_y^p ℱ)`, hence `0` by virtue of the
induction hypothesis.

Note now that the fibre `Z = f^{-1}(y) = X ×_Y Spec(κ(y))` is a closed subprescheme of `X_p`, and that
`𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ` is annihilated by `𝔪_y`, hence may be considered as an `𝒪_Z`-module, so that
`H^n(Z, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) = H^n(X_p, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ)`. This being so, we shall show that the canonical
`𝒪_Z`-homomorphism

```text
  (ℱ / 𝔪_y ℱ) ⊗_{κ(y)} (𝔪_y^p / 𝔪_y^{p+1}) → 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ           (4.6.1.2)
```

is bijective; this established, it will follow, since `𝔪_y^p / 𝔪_y^{p+1}` is a free `κ(y)`-module, that we have

```text
  H^n(Z, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) = H^n(Z, ℱ / 𝔪_y ℱ) ⊗_{κ(y)} (𝔪_y^p / 𝔪_y^{p+1}) = 0
```

`(0_III, 12.2.3)`, since `H^n(Z, ℱ / 𝔪_y ℱ) = 0` by hypothesis, whence (4.6.1.1). To establish the first assertion, it
remains therefore to prove that (4.6.1.2) is bijective; since the question is pointwise on `X` and `ℱ_x` is an
`𝒪_y`-flat module by hypothesis for every `x ∈ f^{-1}(y)`, it suffices to apply `(0_III, 10.2.1, c))`, since
`ℱ_x / 𝔪_y ℱ_x` is a flat module over the field `κ(y) = 𝒪_y / 𝔪_y`.

To prove the second assertion of (4.6.1), we reduce at once, as in (4.2.1), to the case where `Y` is affine and `y`
closed. Note that (4.6.1.1) gives, by an analogous reasoning, for every `k > 0`, the relation

```text
  H^n(X_{p+k}, 𝔪_y^p ℱ / 𝔪_y^{p+k+1} ℱ) = 0                                  (4.6.1.3)
```

<!-- original page 141 -->

whence one deduces, by (4.2.1), that we also have

```text
  (R^n f_*(𝔪_y^p ℱ))_y = 0.                                                  (4.6.1.4)
```

This being so, one draws from the exact sequence in cohomology the exactness of the sequence

```text
  (R^{n-1} f_*(ℱ))_y → (R^{n-1} f_*(ℱ / 𝔪_y^p ℱ))_y → (R^n f_*(𝔪_y^p ℱ))_y = 0
```

and since `y` is closed and `Y` affine, we have (1.4.11)

```text
  R^{n-1} f_*(ℱ / 𝔪_y^p ℱ) = (H^{n-1}(X, ℱ / 𝔪_y^p ℱ))^∼ = (H^{n-1}(f^{-1}(y), ℱ / 𝔪_y^p ℱ))^∼
```

`(G, II, 4.9.1)`; now `H^{n-1}(f^{-1}(y), ℱ / 𝔪_y^p ℱ)` is an `(𝒪_y / 𝔪_y^p)`-module, whence

```text
  (R^{n-1} f_*(ℱ / 𝔪_y^p ℱ))_y = H^{n-1}(f^{-1}(y), ℱ / 𝔪_y^p ℱ)
```

and this completes the proof of (4.6.1).

**Corollary (4.6.2).**

<!-- label: III.4.6.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper and flat morphism, `ℱ`, `𝒢` two locally free
`𝒪_X`-modules, `y` a point of `Y`. Set `X_y = f^{-1}(y) = X ⊗_{𝒪_Y} κ(y)`, `ℱ_y = ℱ ⊗_{𝒪_Y} κ(y)`,
`𝒢_y = 𝒢 ⊗_{𝒪_Y} κ(y)`, and suppose that*

```text
  H^1(X_y, 𝓗𝓸𝓶_{𝒪_{X_y}}(ℱ_y, 𝒢_y)) = 0.                                     (4.6.2.1)
```

*Then, for every homomorphism `u_0 : ℱ_y → 𝒢_y`, there exists an open neighbourhood `U` of `y` and a homomorphism
`u : ℱ ∣ f^{-1}(U) → 𝒢 ∣ f^{-1}(U)` such that `u_y` is equal to the homomorphism `u_0 ⊗ 1`.*

**Proof.** Indeed, the hypothesis permits applying (4.6.1) to the coherent `𝒪_X`-module `ℋ = 𝓗𝓸𝓶_{𝒪_X}(ℱ, 𝒢)` for
`n = 1` and `p = 0`, for `ℱ` is locally free and *a fortiori* `f`-flat, and the `𝒪_{X_y}`-module `ℋ ⊗_{𝒪_Y} κ(y)` is
then identified with `𝓗𝓸𝓶_{𝒪_{X_y}}(ℱ_y, 𝒢_y)` `(0_I, 6.2.2)`. We may suppose `Y = Spec(A)` affine, and then (1.4.11)
`R^0 f_*(ℋ) = (Hom_{𝒪_X}(ℱ, 𝒢))^∼`, hence `(R^0 f_*(ℋ))_y = Hom_{𝒪_X}(ℱ, 𝒢) ⊗_A 𝒪_y`; the canonical homomorphism

```text
  Hom_{𝒪_X}(ℱ, 𝒢) ⊗_A 𝒪_y → Hom_{𝒪_{X_y}}(ℱ_y, 𝒢_y)
```

being surjective by (4.6.1), this establishes the corollary, since every element of `Hom_{𝒪_X}(ℱ, 𝒢) ⊗_A 𝒪_y` may always
be put under the form `u_0 ⊗ (1/s)`, where `s ∉ 𝔪_y` is an element of `A`.

This corollary can be supplemented by the following:

**Corollary (4.6.3).**

<!-- label: III.4.6.3 -->

*Under the hypotheses of (4.6.2), if `u_0` is injective (resp. surjective, bijective), one may suppose that the same
holds for `u`.*

**Proof.** We may restrict to the case where `U = Y`. It suffices to prove that if `u_0` is injective (resp.
surjective), `Ker u_x = 0` (resp. `Coker u_x = 0`) for every `x ∈ f^{-1}(y)`: indeed, `Ker u` and `Coker u` are coherent
`𝒪_X`-modules `(0_I, 5.3.4)`, so there will exist a neighbourhood `V` of `f^{-1}(y)` in `X` such that the restriction of
`Ker u` (resp. `Coker u`) to `V` is `0` `(0_I, 5.2.2)`; since `f` is closed, there will exist a neighbourhood `U' ⊂ U`
of `y` such that `f^{-1}(U') ⊂ V`, and (4.6.3) will be proved. By hypothesis,
`u_0 ⊗ 1 : ℱ_x ⊗_{𝒪_x} κ(y) → 𝒢_x ⊗_{𝒪_x} κ(y)` is injective (resp. surjective),

<!-- original page 142 -->

`ℱ_x` and `𝒢_x` are free `𝒪_x`-modules of finite type and `𝒪_x` is a flat `𝒪_y`-module. When we suppose `u_0 ⊗ 1`
injective, the fact that `u_x` is injective results from `(0_III, 10.2.4)`. When we suppose `u_0 ⊗ 1` surjective, *a
fortiori* the homomorphism `ℱ_x / 𝔪_y ℱ_x → 𝒢_x / 𝔪_y 𝒢_x` which is deduced from it by passage to quotients, is
surjective; since `𝒢_x` is an `𝒪_x`-module of finite type and `𝒪_x` is a local ring of maximal ideal `𝔪_x`, the
conclusion follows from Nakayama's lemma (Bourbaki, *Alg.*, chap. VIII, § 6, n° 3, cor. 4 of prop. 6).

One deduces in particular from (4.6.3):

**Corollary (4.6.4).**

<!-- label: III.4.6.4 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper and flat morphism, `y` a point of `Y`,
`X_y = X ⊗_Y κ(y)`. Let `ℰ_y` be a locally free `𝒪_{X_y}`-module such that*

```text
  H^1(X_y, 𝓗𝓸𝓶_{𝒪_{X_y}}(ℰ_y, ℰ_y)) = 0.                                     (4.6.4.1)
```

*Let `ℱ`, `𝒢` be two locally free `𝒪_X`-modules such that `ℱ_y` and `𝒢_y` (with the notation of (4.6.2)) are isomorphic
to `ℰ_y`. Then there exists an open neighbourhood `U` of `y` such that `ℱ ∣ f^{-1}(U)` and `𝒢 ∣ f^{-1}(U)` are
isomorphic.*

More particularly:

**Corollary (4.6.5).**

<!-- label: III.4.6.5 -->

*Under the hypotheses of (4.6.4) on `f`, `X`, `Y`, suppose that `H^1(X_y, 𝒪_{X_y}) = 0`. If `ℒ` and `𝒮` are two
invertible `𝒪_X`-modules such that `ℒ_y` and `𝒮_y` are isomorphic, there exists an open neighbourhood `U` of `y` such
that `ℒ ∣ f^{-1}(U)` and `𝒮 ∣ f^{-1}(U)` are isomorphic.*

**Proof.** It suffices to apply (4.6.4) to the modules `ℒ^{-1} ⊗ 𝒮` and `𝒪_X`.

**Remarks (4.6.6).**

<!-- label: III.4.6.6 -->

(i) Using (4.6.5), we shall establish in chap. V the classification of invertible sheaves on a projective fibre,
announced in `(II, 4.2.7)`.

(ii) The result of (4.6.1) will appear in § 7 as a consequence of more general propositions.

**Proposition (4.6.7).**

<!-- label: III.4.6.7 -->

*Let `Z` be a locally Noetherian prescheme, `X`, `Y` two `Z`-preschemes such that the structure morphisms `g : X → Z`,
`h : Y → Z` are proper. Let `f : X → Y` be a `Z`-morphism, `z` a point of `Z`, and let
`f_z = f ⊗_Z 1 : X ⊗_Z κ(z) → Y ⊗_Z κ(z)`.*

*(i) If `f_z` is a finite morphism (resp. a closed immersion), there exists an open neighbourhood `U` of `z` such that
the morphism `g^{-1}(U) → h^{-1}(U)`, restriction of `f`, is a finite morphism (resp. a closed immersion).*

*(ii) Suppose in addition that `g` is a flat morphism. Then, if `f_z` is an isomorphism, there exists an open
neighbourhood `U` of `z` such that the morphism `g^{-1}(U) → h^{-1}(U)`, restriction of `f`, is an isomorphism.*

**Proof.** In both cases, it will suffice to prove that for every `y ∈ h^{-1}(z)`, there exists a neighbourhood `V_y` of
`y` such that the restriction `f^{-1}(V_y) → V_y` of `f` is a finite morphism (resp. a closed immersion, an
isomorphism); it will then follow that if `V` is the union of the `V_y`, the restriction `f^{-1}(V) → V` of `f` is a
finite morphism (resp. a closed immersion, an isomorphism) `(II, 6.1.1 and I, 4.2.4)`. Since `h` is a closed morphism,
there will exist an open neighbourhood `U` of `z` such that `h^{-1}(U) ⊂ V`, and the proposition will be proved.

(i) Note first that `f` is a proper morphism `(II, 5.4.3)`; if we

<!-- original page 143 -->

suppose `f_z` finite, the existence for every `y ∈ h^{-1}(z)` of a neighbourhood `V_y` such that `f^{-1}(V_y) → V_y` is
finite results from (4.4.11). To treat the case where `f_z` is a closed immersion, we may therefore already suppose that
the morphism `f` is finite, hence `X = Spec(ℬ)`, where `ℬ` is a coherent `𝒪_Y`-algebra, the morphism `f` corresponding
`(II, 1.2.7)` to the canonical homomorphism `u : 𝒪_Y → ℬ`. If we prove that for every `y ∈ h^{-1}(z)`, the homomorphism
`u_y : 𝒪_y → ℬ_y` is surjective, it will follow that for a neighbourhood `V_y` of `y`, `u ∣ V_y` is surjective, the
sheaf `Coker u` being coherent `(0_I, 5.3.4 and 5.2.2)`. This being so, the finite morphism `f_z` corresponds to the
homomorphism `v = u ⊗ 1 : 𝒪_Y ⊗_{𝒪_Z} κ(z) → ℬ ⊗_{𝒪_Z} κ(z)`, and the hypothesis that `f_z` is a closed immersion
implies that the homomorphism `u ⊗ 1 : 𝒪_y ⊗_{𝒪_z} κ(z) → ℬ_y ⊗_{𝒪_z} κ(z)` is surjective. Since `ℬ_y` is an
`𝒪_y`-module of finite type and `𝒪_y` is a Noetherian local ring, the conclusion results as in (4.6.3) from Nakayama's
lemma.

(ii) The same reasoning as above shows that it suffices this time to prove that `u_y` is bijective, knowing that
`u_y ⊗ 1` is bijective.

This will result from the following lemma:

**Lemma (4.6.7.1).**

<!-- label: III.4.6.7.1 -->

*Let `A`, `B` be two Noetherian local rings, `ρ : A → B` a local homomorphism, `u : N → M` a homomorphism of
`B`-modules. Suppose that `M` is a flat `A`-module, `N` a `B`-module of finite type and that `u ⊗ 1 : N ⊗_A k → M ⊗_A k`
(where `k` is the residue field of `A`) is injective. Then `N` is a flat `A`-module and `u` is injective.*

**Proof.** To establish the first assertion, we must show that for every pair of `A`-modules of finite type `P`, `Q` and
every injective `A`-homomorphism `v : P → Q`, `1_N ⊗ v : N ⊗_A P → N ⊗_A Q` is injective. Now, we have the commutative
diagram

```text
  N ⊗_A P ───^{1_N ⊗ v}───→ N ⊗_A Q
      ↓ u ⊗ 1_P                  ↓ u ⊗ 1_Q
  M ⊗_A P ───^{1_M ⊗ v}───→ M ⊗_A Q
```

and since `1_M ⊗ v` is injective by hypothesis, it suffices to prove the same for `u ⊗ 1_P`. Let `𝔪` be the maximal
ideal of `A`; the `𝔪`-adic filtration on the `A`-module `N ⊗_A P` is also its `𝔪B`-adic filtration as a `B`-module; the
topology defined by this filtration is therefore separated, since `B` is Noetherian, `𝔪B` is contained in the radical of
`B`, and `N ⊗_A P` is a `B`-module of finite type, `N` being a `B`-module of finite type and `P` an `A`-module of finite
type `(0_I, 7.3.5)`. It therefore suffices to prove that the homomorphism `gr(u ⊗ 1_P) : gr_•(N ⊗_A P) → gr_•(M ⊗_A P)`
(where the graded modules are relative to the `𝔪`-adic filtrations) is injective (Bourbaki, *Alg. comm.*, chap. III, §
2, n° 8, cor. 1 of th. 1). Note now that since `M` is a flat `A`-module, the homomorphisms
`M ⊗_A (𝔪^n P) → 𝔪^n(M ⊗_A P)` are bijective; the same therefore holds for the canonical homomorphism

```text
  φ_M : gr_0(M) ⊗_A gr_•(P) → gr_•(M ⊗_A P).
```

<!-- original page 144 -->

Now we have a commutative diagram

```text
  gr_0(N) ⊗_A gr_•(P) ──^{gr(u) ⊗ 1}──→ gr_0(M) ⊗_A gr_•(P)
        ↓ φ_N                                      ↓ φ_M
  gr_•(N ⊗_A P)       ──^{gr(u ⊗ 1_P)}──→ gr_•(M ⊗_A P)
```

in which `φ_M` is bijective, `φ_N` surjective; moreover, `gr(u)` is injective by hypothesis, and since
`gr_0(N) ⊗_A gr_•(P) = gr_0(N) ⊗_k gr_•(P)`, `gr_0(M) ⊗_A gr_•(P) = gr_0(M) ⊗_k gr_•(P)`, `gr(u) ⊗ 1` is also injective.
We conclude that `gr(u ⊗ 1)` is injective, which completes the proof of the first assertion. The second is deduced from
the preceding reasoning on taking `P = A`.

**Proposition (4.6.8).**

<!-- label: III.4.6.8 -->

*Let `Z` be a locally Noetherian prescheme, `X`, `Y` two `Z`-preschemes such that the structure morphisms `g : X → Z`,
`h : Y → Z` are proper, `Z'` a closed part of `Z`, `X' = g^{-1}(Z')`, `Y' = h^{-1}(Z')` its inverse images,
`𝔛 = X_{/X'}`, `𝔜 = Y_{/Y'}`, `𝔷 = Z_{/Z'}` the formal completions of `X`, `Y`, `Z` along these closed parts,
`f : X → Y` a `Z`-morphism, `𝑓̂ : 𝔛 → 𝔜` its extension to the completions. For `𝑓̂` to be an isomorphism (resp. a closed
immersion), it is necessary and sufficient that there exists an open neighbourhood `U` of `Z'` such that the morphism
`g^{-1}(U) → h^{-1}(U)`, restriction of `f`, is an isomorphism (resp. a closed immersion).*

**Proof.** The sufficiency of the condition is immediate `(I, 10.14.7)`. To show its necessity, it suffices again to
prove that for every `y ∈ Y'`, there exists an open neighbourhood `V_y` of `y` such that the restriction
`f^{-1}(V_y) → V_y` of `f` is an isomorphism (resp. a closed immersion), by the same reasoning as in (4.6.7). We are
thus reduced to the case where `Y = Z`, `Y = Spec(A)` being affine Noetherian. By hypothesis `(I, 10.9.1 and 10.14.2)`
the fibre `f^{-1}(y)` is reduced to a point for `y ∈ Y'`, hence since `f` is proper `(II, 5.4.3)`, there exists an open
neighbourhood `U` of `y` such that the restriction `f^{-1}(U) → U` of `f` is a finite morphism (4.4.11). We may
therefore already suppose that `f` is a finite morphism, hence `X = Spec(B)`, where `B` is an `A`-algebra finite over
`A`. If `Y' = V(𝔍)`, we then have `𝔜 = Spf(Â)`, `𝔛 = Spf(B̂)`, `Â` being the Hausdorff completion of `A` for the
`𝔍`-preadic topology, `B̂` the Hausdorff completion of `B` for the `𝔍B`-preadic topology, or (which amounts to the same
thing), the Hausdorff completion of the `A`-module `B` for the `𝔍`-preadic topology; moreover, `𝑓̂` is the morphism of
affine formal schemes corresponding to the continuous extension `φ̂ : Â → B̂` of the canonical homomorphism of rings
`φ : A → B`, and the hypothesis is that `φ̂` is surjective (resp. bijective) `(I, 10.14.2)`. Now, `φ̂` is also the
continuous extension of `φ` considered as a homomorphism of `A`-modules; we know then `(I, 10.8.14)` that there exists
an open neighbourhood `U` of `Y'` such that the restriction to `U` of the homomorphism `φ̃ : Ã → B̃` of `𝒪_Y`-modules is
surjective (resp. bijective), which completes the proof.

<!-- original page 145 -->

## 4.7. An ampleness criterion

**Theorem (4.7.1).**

<!-- label: III.4.7.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism, `ℒ` an invertible `𝒪_X`-module, `y` a point
of `Y`, `X_y = X ⊗_Y κ(y) = f^{-1}(y)`, `q` the projection of `X_y` into `X`. If `ℒ_y = q^*(ℒ) = ℒ ⊗_{𝒪_Y} κ(y)` is
ample on `X_y`, there exists an open neighbourhood `U` of `y` in `Y` such that `ℒ ∣ f^{-1}(U)` is ample for the
restriction of `f` to `f^{-1}(U)`.*

**Proof.**

I) Set `Y' = Spec(𝒪_y)`, `X' = X ×_Y Y'`, and let `ℒ' = 𝒪_{X'} ⊗_{𝒪_X} ℒ`; we shall first prove that `ℒ'` is ample for
`f' = f_{(Y')}`. We have the commutative diagram

```text
  X ←──── X' ←──── X_y
  ↓ f      ↓ f'      ↓
  Y ←──── Y' ←──── Spec(κ(y))
```

Since `f'` is proper `(II, 5.4.2, (iii))` and `𝒪_y` Noetherian, we see that we may restrict to the case where
`Y = Y' = Spec(𝒪_y)`, hence `X = X'`, suppose `ℒ_y` ample for `f_y`, and prove that `ℒ` is ample for `f` `(II, 4.6.6)`.
We shall apply the criterion `(2.6.1, b))` and shall in fact show that for every coherent `𝒪_X`-module `ℱ`, there exists
an integer `N` such that `H^q(X, ℱ(n)) = 0` for every `n ≥ N`, with `ℱ(n) = ℱ ⊗_{𝒪_X} ℒ^{⊗n}`. Note that `y` is a closed
point of `Y` corresponding to the maximal ideal `𝔪` of `𝒪_y`; `X_y` is therefore a closed subprescheme of `X` defined by
the coherent ideal `𝒥 = f^*(𝔪̃) 𝒪_X = 𝔪 𝒪_X` of `𝒪_X` `(I, 4.4.5)`, and `q` the canonical injection. Consider then the
graded `κ(y)`-algebra `S = gr(𝒪_y) = ⊕_{k ≥ 0} 𝔪^k / 𝔪^{k+1}`, which is of finite type since `𝒪_y` is Noetherian; the
`𝒪_X`-algebra `𝒮 = f^*(S̃)` is therefore quasi-coherent and of finite type, and it is obviously annihilated by `𝒥`, so
if we set `𝒮_y = q^*(𝒮)`, `𝒮_y` is a quasi-coherent `𝒪_{X_y}`-algebra of finite type, and `𝒮_y = q̃^*(S̃)`. Set, on the
other hand, `ℳ_k = 𝔪^k ℱ / 𝔪^{k+1} ℱ` and `ℳ = ⊕_{k ≥ 0} ℳ_k = gr(ℱ)`; since `ℱ` is coherent, `ℳ` is a quasi-coherent
`𝒪_X`-module of finite type `(0_III, 10.1.1)` which is also annihilated by `𝒥`, so if we set `ℳ_y = q^*(ℳ)`,
`ℳ_y = q^*(ℳ) = ⊕_j ℳ'_j` is a quasi-coherent graded `𝒮_y`-module of finite type such that `ℳ = q_*(ℳ_y)`. Moreover, if
we set `ℳ_y(n) = ℳ_y ⊗_{𝒪_{X_y}} ℒ_y^{⊗n}`, we have `ℳ_y(n) = q^*(ℳ(n))`. This being so, `f_y` is proper
`(II, 5.4.2, (iii))` and `ℒ_y` ample, so `f_y` is projective `(II, 5.5.4 and 4.6.11)`, and we may apply to `Spec(κ(y))`,
`f_y`, `𝒮_y`, `ℒ_y` and `ℳ_y` the theorem `(2.4.1, (ii))`: there exists an integer `N` such that for `n ≥ N`, we have
`H^q(X_y, ℳ_y(n)) = 0` for every `q > 0` and every `j`; consequently, we also have `H^q(X, ℳ_j(n)) = 0` for every
`q > 0` and every `j` `(G, II, 4.9.1)`. Set then `ℱ(n)_j = ℱ(n) / 𝔪^{j+1} ℱ(n)`, so that `ℳ_j(n) = ℱ(n)_j / ℱ(n)_{j-1}`
for `j ≥ 1` and `ℳ_0(n) = ℱ(n)_0`. We have `H^q(X, ℱ(n)_0) = 0`, and, by the exact sequence of cohomology,
`H^q(X, ℱ(n)_j) = H^q(X, ℱ(n)_{j-1})` for every `j ≥ 1`, hence `H^q(X, ℱ(n)_j) = 0` for every `j ≥ 0`. We conclude from
(4.2.1) that `H^q(X, ℱ(n)) = 0`, which completes the proof of our assertion.

II) Returning to the notation of the beginning of the proof, note that we

<!-- original page 146 -->

may always suppose `Y = Spec(A)` affine; since `f'` is of finite type and `ℒ'` ample for `f'`, there exists an integer
`m > 0` such that `ℒ'^{⊗m}` is very ample for `f'` `(II, 4.6.11)`; replacing `ℒ` by `ℒ^{⊗m}` if necessary, we may
restrict to considering the case where `ℒ'` is very ample for `f'`, and prove that `ℒ ∣ f^{-1}(U)` is then very ample
for `f`. Since `f'` is proper, there then exists a `Y'`-closed immersion `j : X' → P = P^r_{Y'}` for a suitable integer
`r > 0`, such that `ℒ'` is isomorphic to `j^*(𝒪_P(1))` `(II, 5.5.4, (ii))`; this immersion corresponds canonically to a
surjective `𝒪_{X'}`-homomorphism `u : 𝒪_{X'}^{r+1} → ℒ'` `(II, 4.2.3)`. The latter corresponds `(0_I, 5.1.1)` to the
data of `r + 1` sections `s'_i` (`0 ≤ i ≤ r`) of `ℒ'` over `X'` which generate this `𝒪_{X'}`-module. These sections are
also by definition sections of `f'_*(ℒ')` over `Y'`; we have `f'_*(ℒ') = f_*(ℒ) ⊗_A 𝒪_y` `(0_I, 5.4.10)`, `Y` is affine
and `𝒪_y` is the local ring at the prime ideal `𝔭_y` of `A`, so we have `s'_i = s''_i / t_i`, where the `s''_i` are
sections of `f_*(ℒ)` over `Y` and the `t_i` elements of `A` not belonging to `𝔭_y`; we conclude that there exists an
affine open neighbourhood `V` of `y` in `Y` and sections `s_i` of `f_*(ℒ) ∣ V` such that `s'_i = s_i / 1` (recall that
the space `Y'` is contained in `V`, cf. `I, 2.4.2`). The `s_i` are then sections of `ℒ` over `f^{-1}(V)`, defining
therefore a homomorphism `v : (𝒪_X ∣ f^{-1}(V))^{r+1} → ℒ ∣ f^{-1}(V)` which, by hypothesis, is surjective at every
point of `f^{-1}(y)`; since `Coker(v)` is coherent `(0_I, 5.3.4)`, its support is closed `(0_I, 5.2.2)` and consequently
there exists an open neighbourhood `W ⊂ f^{-1}(V)` of `f^{-1}(y)` such that the restriction of `v` to `W` is a
surjective homomorphism. Since the morphism `f` is closed, we may suppose that `W` is of the form `f^{-1}(U)`, where `U`
is an open neighbourhood of `y`, and the conclusion then follows from `(II, 4.2.3)`.

## 4.8. Finite morphisms of formal preschemes

**Proposition (4.8.1).**

<!-- label: III.4.8.1 -->

*Let `𝔜` be a locally Noetherian formal prescheme, `𝒦` an ideal of definition of `𝔜`, `f : 𝔛 → 𝔜` a morphism of formal
preschemes. The following conditions are equivalent:*

*a) `𝔛` is locally Noetherian, `f` is an adic morphism `(I, 10.12.1)` and if we set `𝒥 = f^*(𝒦) 𝒪_𝔛`, the morphism
`f_0 : (𝔛, 𝒪_𝔛 / 𝒥) → (𝔜, 𝒪_𝔜 / 𝒦)` deduced from `f` is finite.*

*b) `𝔛` is locally Noetherian and is the inductive limit of a `(Y_n)`-inductive adic system `(X_n)` such that the
morphism `X_0 → Y_0` is finite.*

*c) Every point of `𝔜` possesses a Noetherian affine formal open neighbourhood `V` such that `f^{-1}(V)` is an affine
formal open set and that `Γ(f^{-1}(V), 𝒪_𝔛)` is a `Γ(V, 𝒪_𝔜)`-module of finite type.*

**Proof.** It is immediate that a) implies b) by virtue of `(I, 10.12.3)`. To see that b) implies c), we may suppose
that `𝔜 = Spf(B)`, where `B` is adic Noetherian and `𝒦 = 𝔍̃`, where `𝔍` is an ideal of definition of `B`. By hypothesis,
`X_0` is an affine scheme whose ring `A_0` is a `B/𝔍`-module of finite type `(II, 6.1.3)`. By virtue of `(I, 5.1.9)`,
each of the `X_n` is an affine scheme, and if `A_n` is its ring, hypothesis b) implies that for `m ≤ n`, `A_m` is
isomorphic to `A_n / 𝔍^{m+1} A_n`. We deduce that `𝔛` is isomorphic to `Spf(A)`, where `A = lim_← A_n`; one concludes by
virtue of `(0_I, 7.2.9)`. Finally, to prove that c)

<!-- original page 147 -->

implies a), we may again restrict to the case where `𝔜 = Spf(B)`, `𝔛 = Spf(A)`, `A` being a finite `B`-algebra; since
`A / 𝔍A` is then a finite `B/𝔍`-algebra, it follows from `(I, 10.10.9)` that the conditions of a) are satisfied.

**Definition (4.8.2).**

<!-- label: III.4.8.2 -->

*When the equivalent properties a), b), c) of (4.8.1) are satisfied, we say that the morphism `f` is *finite*, or that
`𝔛` is a finite `𝔜`-formal prescheme, or a finite formal prescheme over `𝔜`.*

**Proposition (4.8.3).**

<!-- label: III.4.8.3 -->

*(i) A closed immersion of locally Noetherian formal preschemes is a finite morphism.*

*(ii) The composition of two finite morphisms of locally Noetherian formal preschemes is a finite morphism.*

*(iii) Let `𝔛`, `𝔜`, `𝔖` be three locally Noetherian formal preschemes, `f : 𝔛 → 𝔖` a finite morphism, `g : 𝔜 → 𝔖` a
morphism; then the morphism `𝔛 ×_𝔖 𝔜 → 𝔜` is finite.*

*(iv) Let `𝔖` be a locally Noetherian formal prescheme, `𝔛'`, `𝔜'` two locally Noetherian formal preschemes such that
`𝔛' ×_𝔖 𝔜'` is locally Noetherian. If `𝔛`, `𝔜` are locally Noetherian `𝔖`-formal preschemes, `f : 𝔛 → 𝔛'`, `g : 𝔜 → 𝔜'`
two finite `𝔖`-morphisms, then `f ×_𝔖 g` is a finite morphism.*

*(v) Let `f : 𝔛 → 𝔜`, `g : 𝔜 → 𝔖` be two morphisms of locally Noetherian formal preschemes such that `g` is of finite
type and separated; then, if `g ∘ f` is a finite morphism, `f` is a finite morphism.*

**Proof.** (i) is trivial, and the other assertions reduce immediately to the corresponding propositions for morphisms
of usual preschemes `(II, 6.1.5)` by means of the criterion a) of (4.8.1); we leave the details to the reader, modelled
on `(I, 10.13.5)`.

**Corollary (4.8.4).**

<!-- label: III.4.8.4 -->

*Under the hypotheses of `(I, 10.9.9)`, if `f` is a finite morphism, the same holds for its extension `𝑓̂` to the
completions.*

**Corollary (4.8.5).**

<!-- label: III.4.8.5 -->

*If `𝔛` is a finite formal prescheme over `𝔜`, `f : 𝔛 → 𝔜` the structure morphism, then, for every open set `U ⊂ 𝔜`,
`f^{-1}(U)` is finite over `U`.*

**Proposition (4.8.6).**

<!-- label: III.4.8.6 -->

*If `f : 𝔛 → 𝔜` is a finite morphism of locally Noetherian formal preschemes, `f_*(𝒪_𝔛)` is a coherent `𝒪_𝔜`-algebra.*

**Proof.** One may consider `f` as the inductive limit of an inductive system `(f_n)` of morphisms `f_n : X_n → Y_n`; we
shall show that the `f_n` are finite morphisms and that `f_*(𝒪_𝔛)` is isomorphic to the projective limit of the
`(f_n)_*(𝒪_{X_n})`, which will establish our assertion `(I, 10.10.5)`. It suffices to restrict to the case where
`𝔜 = Spf(B)`, `𝔛 = Spf(A)`, and to remark that if `𝔍` is an ideal of definition of `B` and `A` a `B`-module of finite
type, `A / 𝔍^{n+1} A` is a module of finite type over `B / 𝔍^{n+1} B`, and that `A` is the projective limit of the
`A / 𝔍^{n+1} A`.

Conversely:

**Proposition (4.8.7).**

<!-- label: III.4.8.7 -->

*Let `𝔜` be a locally Noetherian formal prescheme, `𝒜` a coherent `𝒪_𝔜`-algebra. There exists a formal prescheme `𝔛`
finite over `𝔜`, defined up to `𝔜`-isomorphism unique, and such that `f_*(𝒪_𝔛) = 𝒜`, `f : 𝔛 → 𝔜` being the structure
morphism.*

**Proof.** Let `𝒦` be an ideal of definition of `𝔜`, and set `Y_n = (𝔜, 𝒪_𝔜 / 𝒦^{n+1})` and `𝒜_n = 𝒜 / 𝒦^{n+1} 𝒜`; it is
clear that `𝒜_n` is a finite `𝒪_{Y_n}`-algebra and defines therefore a

<!-- original page 148 -->

`Y_n`-prescheme finite `X_n = Spec(𝒜_n)` `(II, 6.1.3)`; for `m ≤ n`, the canonical surjective homomorphism
`h_{nm} : 𝒜_n → 𝒜_m` defines a morphism `u_{nm} : X_m → X_n` such that the diagram

```text
  X_m ──^{u_{nm}}──→ X_n
   ↓ f_m              ↓ f_n
  Y_m ──────────────→ Y_n
```

(`f_n` being the structure morphism) is commutative and identifies `X_m` with the product `X_n ×_{Y_n} Y_m`, as one sees
immediately `(II, 1.4.6)`. The formal prescheme `𝔛`, inductive limit of the inductive system `(X_n)`, is then locally
Noetherian and such that the structure morphism `f : 𝔛 → 𝔜`, inductive limit of the system `(f_n)`, is finite (4.8.1 and
`II, 10.12.3.1`); we saw in addition in the proof of (4.8.6) that `f_*(𝒪_𝔛)` is the projective limit of the `𝒜_n`, hence
equal to `𝒜` `(I, 10.10.6)`. As for the uniqueness assertion, it is a consequence of the following more general result:

**Proposition (4.8.8).**

<!-- label: III.4.8.8 -->

*Let `𝔜` be a locally Noetherian formal prescheme, `𝔛`, `𝔛'` two `𝔜`-formal preschemes finite over `𝔜`, `f : 𝔛 → 𝔜`,
`f' : 𝔛' → 𝔜` the structure morphisms. There exists a canonical bijection of `Hom_𝔜(𝔛, 𝔛')` onto
`Hom_{𝒪_𝔜}(f'_*(𝒪_{𝔛'}), f_*(𝒪_𝔛))` (1).*

> (1) The last expression denotes the set of homomorphisms of `𝒪_𝔜`-algebras `f'_*(𝒪_{𝔛'}) → f_*(𝒪_𝔛)`.

**Proof.** The definition of this map `h ↦ 𝒜(h)` is the same as in `(II, 1.1.2)`, and to see that it is bijective, we
are immediately reduced to the case where `𝔜 = Spf(B)` is a Noetherian affine formal scheme. But then `𝔛 = Spf(A)`,
`𝔛' = Spf(A')`, where `A` and `A'` are two finite `B`-algebras and `f_*(𝒪_𝔛) = A^Δ`, `f'_*(𝒪_{𝔛'}) = A'^Δ`. The
conclusion then results from the one-to-one correspondence, on the one hand between the `𝔜`-morphisms `𝔛 → 𝔛'` and the
`B`-homomorphisms (necessarily continuous) `A' → A` which are homomorphisms of algebras `(I, 10.2.2)`, and on the other
hand between the homomorphisms of `B`-modules `A' → A` and the homomorphisms of `𝒪_𝔜`-modules `A'^Δ → A^Δ`
`(I, 10.10.2.3)`.

**Corollary (4.8.9).**

<!-- label: III.4.8.9 -->

*In the canonical one-to-one correspondence defined in (4.8.8), the closed immersions `𝔛 → 𝔛'` correspond to the
surjective homomorphisms of `𝒪_𝔜`-algebras `f'_*(𝒪_{𝔛'}) → f_*(𝒪_𝔛)`.*

**Proof.** The question being still local on `𝔜`, we are reduced to the definition of closed immersions of locally
Noetherian formal preschemes `(I, 10.14.2)`.

**Corollary (4.8.10).**

<!-- label: III.4.8.10 -->

*The notations and hypotheses being those of (4.8.1), for an adic morphism `f` to be a closed immersion, it is necessary
and sufficient that `f_0` be a closed immersion (of usual preschemes).*

**Proof.** This results immediately from (4.8.9) and from the condition of surjectivity for a homomorphism of coherent
`𝒪_𝔜`-modules `(I, 10.11.5)`.

**Proposition (4.8.11).**

<!-- label: III.4.8.11 -->

*For a morphism `f : 𝔛 → 𝔜` of locally Noetherian formal preschemes*

<!-- original page 149 -->

*to be finite, it is necessary and sufficient that it be proper and have its fibres `f^{-1}(y)` finite (for every
`y ∈ 𝔜`).*

**Proof.** Thanks to the definitions (3.4.1 and 4.8.2), we are at once reduced to the same proposition for `f_0`
(notation of (4.8.1)), which is none other than (4.4.2).
