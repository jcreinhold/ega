# §10. Complements on flat modules

<!-- original page 361 -->

For the proofs of the properties stated without proof in nos. `(10.1)` and `(10.2)`, we refer the reader to Bourbaki,
_Alg. comm._, chap. II and III.

## 10.1. Relations between flat modules and free modules

**10.1.1.**

<!-- label: 0_III.10.1.1 -->

Let `A` be a ring, `𝔍` an ideal of `A`, `M` an `A`-module; for every integer `p ≥ 0`, one has a canonical homomorphism
of `(A/𝔍)`-modules

```text
  φ_p : (M/𝔍 M) ⊗_{A/𝔍} (𝔍^p/𝔍^{p+1}) → 𝔍^p M/𝔍^{p+1} M               (10.1.1.1)
```

which is obviously surjective. We shall denote by `gr(A) = ⊕_{p≥0} 𝔍^p/𝔍^{p+1}` the graded ring associated to `A`
filtered by the `𝔍^p`, and by `gr(M) = ⊕_{p≥0} 𝔍^p M/𝔍^{p+1} M` the graded `gr(A)`-module associated to `M` filtered by
the `𝔍^p M`; we therefore have `gr_p(A) = 𝔍^p/𝔍^{p+1}`, `gr_p(M) = 𝔍^p M/𝔍^{p+1} M`; the `φ_p` define a surjective
homomorphism of graded `gr(A)`-modules

```text
  φ : gr_0(M) ⊗_{gr_0(A)} gr(A) → gr(M).                                 (10.1.1.2)
```

<!-- original page 362 -->

**10.1.2.**

<!-- label: 0_III.10.1.2 -->

*Suppose that one of the following hypotheses holds:*

*(i) `𝔍` is nilpotent;*

*(ii) `A` is Noetherian, `𝔍` is contained in the radical of `A`, and `M` is of finite type.*

*Then the following properties are equivalent:*

*a) `M` is a free `A`-module.*

*b) `M/𝔍 M = M ⊗_A (A/𝔍)` is a free `(A/𝔍)`-module, and `Tor_1^A(M, A/𝔍) = 0`.*

*c) `M/𝔍 M` is a free `(A/𝔍)`-module and the canonical homomorphism `(10.1.1.2)` is injective (hence bijective).*

**10.1.3.**

<!-- label: 0_III.10.1.3 -->

*Suppose that `A/𝔍` is a field (in other words, that `𝔍` is maximal), and that one of the hypotheses (i), (ii) of
`(10.1.2)` holds. Then the following properties are equivalent:*

*a) `M` is a free `A`-module.*

*b) `M` is a projective `A`-module.*

*c) `M` is a flat `A`-module.*

*d) `Tor_1^A(M, A/𝔍) = 0`.*

*e) The canonical homomorphism `(10.1.1.2)` is bijective.*

This result will apply in particular in the following two cases:

(i) `M` is an arbitrary module over a local ring `A` whose maximal ideal `𝔍` is nilpotent (for example an Artinian local
ring).

(ii) `M` is a module of finite type over a Noetherian local ring.

## 10.2. Local criteria of flatness

**10.2.1.**

<!-- label: 0_III.10.2.1 -->

*The hypotheses and notation being those of `(10.1.1)`, consider the following conditions:*

*a) `M` is a flat `A`-module.*

*b) `M/𝔍 M` is a flat `(A/𝔍)`-module and `Tor_1^A(M, A/𝔍) = 0`.*

*c) `M/𝔍 M` is a flat `(A/𝔍)`-module and the canonical homomorphism `(10.1.1.2)` is bijective.*

*d) For every `n ≥ 1`, `M/𝔍^n M` is a flat `(A/𝔍^n)`-module.*

*One then has the implications*

```text
  a) ⟹ b) ⟹ c) ⟹ d)
```

*and if `𝔍` is nilpotent, the four conditions a), b), c), d) are equivalent. The same holds if `A` is Noetherian and if
moreover `M` is **ideally separated**, that is, if for every ideal `𝔞` of `A`, the `A`-module `𝔞 ⊗_A M` is separated for
the `𝔍`-preadic topology.*

**10.2.2.**

<!-- label: 0_III.10.2.2 -->

*Let `A` be a Noetherian ring, `B` a commutative Noetherian `A`-algebra, `𝔍` an ideal of `A` such that `𝔍 B` is
contained in the radical of `B`, `M` a `B`-module of finite type. Then, when `M` is considered as an `A`-module, the
conditions a), b), c), d) of `(10.2.1)` are equivalent.*

<!-- original page 363 -->

This result applies above all when `A` and `B` are Noetherian local rings, the homomorphism `A → B` a local
homomorphism. More particularly, if `𝔍` is then the maximal ideal of `A`, one may, in conditions b) and c), drop the
hypothesis that `M/𝔍 M` is flat, which is automatically satisfied, and condition d) means that the modules `M/𝔍^n M` are
free over the `A/𝔍^n`.

**10.2.3.**

<!-- label: 0_III.10.2.3 -->

*The hypotheses on `A`, `B`, `𝔍`, `M` being those formulated at the beginning of `(10.2.2)`, let `Â` be the Hausdorff
completion of `A` for the `𝔍`-preadic topology, `M̂` the Hausdorff completion of `M` for the `𝔍 B`-preadic topology.
Then, for `M` to be a flat `A`-module, it is necessary and sufficient that `M̂` be a flat `Â`-module.*

**10.2.4.**

<!-- label: 0_III.10.2.4 -->

*Let `ρ : A → B` be a local homomorphism of Noetherian local rings, `k` the residue field of `A`, `M`, `N` two
`B`-modules of finite type, `N` being assumed to be `A`-flat. Let `u : M → N` be a `B`-homomorphism. Then the following
conditions are equivalent:*

*a) `u` is injective and `Coker(u)` is a flat `A`-module.*

*b) `u ⊗ 1 : M ⊗_A k → N ⊗_A k` is injective.*

**10.2.5.**

<!-- label: 0_III.10.2.5 -->

*Let `ρ : A → B`, `σ : B → C` be local homomorphisms of Noetherian local rings, `k` the residue field of `A`, `M` a
`C`-module of finite type. Suppose that `B` is a flat `A`-module. Then the following conditions are equivalent:*

*a) `M` is a flat `B`-module.*

*b) `M` is a flat `A`-module, and `M ⊗_A k` is a flat `(B ⊗_A k)`-module.*

**Proposition (10.2.6).**

<!-- label: 0_III.10.2.6 -->

*Let `A`, `B` be two Noetherian local rings, `ρ : A → B` a local homomorphism, `𝔍` an ideal of `B` contained in the
maximal ideal, `M` a `B`-module of finite type. Suppose that for every `n ≥ 0`, `M_n = M/𝔍^{n+1} M` is a flat
`A`-module. Then `M` is a flat `A`-module.*

**Proof.** We must prove that for every injective homomorphism `u : N' → N` of `A`-modules of finite type,
`v = 1 ⊗ u : M ⊗_A N' → M ⊗_A N` is injective. Now, `M ⊗_A N'` and `M ⊗_A N` are `B`-modules of finite type, hence
separated for the `𝔍`-preadic topology `(0_I, 7.3.5)`; it therefore suffices to prove that the homomorphism
`v̂ : (M ⊗_A N')^∧ → (M ⊗_A N)^∧` between Hausdorff completions is injective. Now, one has `v̂ = lim v_n`, where `v_n`
is the homomorphism `1 ⊗ u : M_n ⊗_A N' → M_n ⊗_A N`; since by hypothesis `M_n` is `A`-flat, `v_n` is injective for
every `n`, and so the same holds for `v̂`, the functor `lim` being left exact.

**Corollary (10.2.7).**

<!-- label: 0_III.10.2.7 -->

*Let `A` be a Noetherian ring, `B` a Noetherian local ring, `ρ : A → B` a homomorphism, `f` an element of the maximal
ideal of `B`, `M` a `B`-module of finite type. Suppose that the homothety `f_M : x ↦ fx` of `M` is injective and that
`M/fM` is a flat `A`-module. Then `M` is a flat `A`-module.*

**Proof.** Set `M_i = f^i M` for `i ≥ 0`; since `f_M` is injective, `M_i/M_{i+1}` is isomorphic to `M/fM`, hence
`A`-flat for every `i ≥ 0`; from the exact sequence

```text
  0 → M_i/M_{i+1} → M/M_{i+1} → M/M_i → 0
```

one deduces by induction on `i` that `M/M_i` is `A`-flat for every `i ≥ 0` `(0_I, 6.1.2)`; one can therefore apply
`(10.2.6)`. One may also argue directly as follows: for every `A`-module `N` of finite type, `M ⊗_A N` is a `B`-module
of finite type; since `f` belongs to the radical `𝔫` of `B`, the `(f)`-adic topology on `M ⊗_A N` is finer than the
`𝔫`-adic topology, and the latter is known to be separated `(0_I, 7.3.5)`.

<!-- original page 364 -->

Moreover, since `M/M_i` is `A`-flat, one has `f^i(M ⊗_A N) = Im(M_i ⊗_A N → M ⊗_A N) = Ker(M ⊗_A N → (M/M_i) ⊗_A N)`
`(0_I, 6.1.2)`. Let then `N` be an `A`-module of finite type, `N'` a submodule of `N`, `j : N' → N` the canonical
injection; in the commutative diagram

```text
  M ⊗_A N'    →    (M/M_i) ⊗_A N'
     │                  │
     │ 1_M ⊗ j           │ 1_{M/M_i} ⊗ j
     ↓                  ↓
  M ⊗_A N     →    (M/M_i) ⊗_A N
```

`1_{M/M_i} ⊗ j` is injective since `M/M_i` is `A`-flat; one concludes that

```text
  Ker(M ⊗_A N' → M ⊗_A N) ⊂ Ker(M ⊗_A N' → (M/M_i) ⊗_A N')
```

whatever the value of `i`; since the intersection of the right-hand sides is reduced to `0` as seen above, the same
holds for the left-hand side, and consequently `M` is `A`-flat.

**Proposition (10.2.8).**

<!-- label: 0_III.10.2.8 -->

*Let `A` be a reduced Noetherian ring, `M` an `A`-module of finite type. Suppose that for every `A`-algebra `B` which is
a discrete valuation ring, `M ⊗_A B` is a flat `B`-module (hence free `(10.1.3)`). Then `M` is a flat `A`-module.*

**Proof.** It is known that for `M` to be flat, it is necessary and sufficient that for every maximal ideal `𝔪` of `A`,
`M_𝔪` be a flat `A_𝔪`-module `(0_I, 6.3.3)`; one may therefore restrict to the case where `A` is local `(0_I, 1.2.8)`.
Let then `𝔪` be the maximal ideal of `A`, `𝔭_i` `(1 ≤ i ≤ r)` its minimal prime ideals, `k = A/𝔪` the residue field. It
is known `(II, 7.1.7)` that for each `i` there exists a discrete valuation ring `B_i` having the same field of fractions
`K_i` as the integral ring `A/𝔭_i`, and dominating the latter. Set `M_i = M ⊗_A B_i`. By hypothesis, `M_i` is free over
`B_i`, so one has, denoting by `k_i` the residue field of `B_i`,

```text
  rg_{k_i}(M_i ⊗_{B_i} k_i) = rg_{K_i}(M_i ⊗_{B_i} K_i).                 (10.2.8.1)
```

But it is clear that the composite homomorphism `A → A/𝔭_i → B_i` is local, so `k_i` is an extension of `k`, and one has
`M_i ⊗_{B_i} k_i = M ⊗_A k_i = (M ⊗_A k) ⊗_k k_i`, and on the other hand `M_i ⊗_{B_i} K_i = M ⊗_A K_i`. The equality
`(10.2.8.1)` therefore yields

```text
  rg_k(M ⊗_A k) = rg_{K_i}(M ⊗_A K_i)                  for 1 ≤ i ≤ r
```

and since `A` is reduced, this condition is known to imply that `M` is a free `A`-module (Bourbaki, _Alg. comm._, chap.
II, § 3, no. 2, prop. 7).

## 10.3. Existence of flat extensions of local rings

**Proposition (10.3.1).**

<!-- label: 0_III.10.3.1 -->

*Let `A` be a Noetherian local ring, `𝔍` its maximal ideal, `k = A/𝔍` its residue field. Let `K` be an extension of the
field `k`. There exists a local homomorphism from `A` into a Noetherian local ring `B`, such that `B/𝔍 B` is
`k`-isomorphic to `K`, and such that `B` is a flat `A`-module.*

**Proof.** We shall prove this proposition in several steps.

**10.3.1.1.**

<!-- label: 0_III.10.3.1.1 -->

Suppose first that `K = k(T)`, where `T` is an indeterminate. In the polynomial ring `A' = A[T]`, consider the prime
ideal `𝔍' = 𝔍 A'` formed by the

<!-- original page 365 -->

polynomials with coefficients in the ideal `𝔍`; it is clear that `A'/𝔍'` is canonically isomorphic to `k[T]`. Let us
show that the ring of fractions `B = A'_{𝔍'}` answers the question; it is evidently a Noetherian local ring whose
maximal ideal is `𝔏 = 𝔍 B`. Furthermore, `B/𝔏 = (A'/𝔍')_{𝔍'} = (k[T])_{(0)}` is nothing other than the field of
fractions `K` of `k[T]`. Finally, `B` is a flat `A'`-module and `A'` a free `A`-module, hence `B` is a flat `A`-module
`(0_I, 6.2.1)`.

**10.3.1.2.**

<!-- label: 0_III.10.3.1.2 -->

Suppose next that `K = k(t) = k[t]`, where `t` is algebraic over `k`; let `f ∈ k[T]` be the minimal polynomial of `t`;
there exists a unitary polynomial `F ∈ A[T]` whose canonical image in `k[T]` is `f`. Set again `A' = A[T]`, and let `𝔍'`
be the ideal `𝔍 A' + (F)` in `A'`. We are going to see that the quotient ring `B = A'/(F)` answers the question this
time. First of all, it is clear that `B` is a free `A`-module, hence flat. The ring `A'/𝔍'` is isomorphic to
`(A'/𝔍 A')/((𝔍 A' + (F))/𝔍 A') = k[T]/(f) = K`; the image `𝔏` of `𝔍'` in `B` is therefore maximal and one obviously has
`𝔏 = 𝔍 B`. Finally, `B` is a semi-local ring, since it is an `A`-module of finite type (Bourbaki, _Alg. comm._, chap.
IV, § 2, no. 5, cor. 3 of prop. 9), and its maximal ideals are in bijective correspondence with those of `B/𝔍 B`
(`[13]`, vol. I, p. 259); what precedes therefore proves that `B` is a local ring.

**Lemma (10.3.1.3).**

<!-- label: 0_III.10.3.1.3 -->

*Let `(A_λ, f_{μλ})` be a filtered inductive system of local rings, such that the `f_{μλ}` are local homomorphisms; let
`𝔪_λ` be the maximal ideal of `A_λ`, and let `K_λ = A_λ/𝔪_λ`. Then `A' = lim A_λ` is a local ring whose maximal ideal is
`𝔪' = lim 𝔪_λ`, and whose residue field is `K = lim K_λ`. Furthermore, if `𝔪_μ = 𝔪_λ A_μ` for `λ < μ`, then
`𝔪' = 𝔪_λ A'` for every `λ`. If, in addition, `A_μ` is a flat `A_λ`-module for `λ < μ`, and if all the `A_λ` are
Noetherian, then `A'` is Noetherian and is a flat `A_λ`-module for every `λ`.*

**Proof.** Since `f_{μλ}(𝔪_λ) ⊂ 𝔪_μ` for `λ < μ` by hypothesis, the `𝔪_λ` form an inductive system, and its limit `𝔪'`
is obviously an ideal of `A'`. Furthermore, if `x' ∉ 𝔪'`, there exists `λ` such that `x' = f_λ(x_λ)` for some
`x_λ ∈ A_λ` (`f_λ : A_λ → A'` denoting the canonical homomorphism); since `x' ∉ 𝔪'`, we necessarily have `x_λ ∉ 𝔪_λ`, so
`x_λ` admits an inverse `y_λ` in `A_λ`, and `y' = f_λ(y_λ)` is the inverse of `x'` in `A'`, which proves that `A'` is a
local ring with maximal ideal `𝔪'`; the assertion concerning `K` follows immediately from the fact that `lim` is an
exact functor. The hypothesis `𝔪_μ = 𝔪_λ A_μ` means that the canonical map `𝔪_λ ⊗_{A_λ} A_μ → 𝔪_μ` is surjective; the
relation `𝔪' = 𝔪_λ A'` thus follows again from the exactness of the functor `lim` and the fact that it commutes with the
tensor product.

Suppose now that for `λ < μ` one has `𝔪_μ = 𝔪_λ A_μ` and that `A_μ` is a flat `A_λ`-module. Then `A'` is a flat
`A_λ`-module for every `λ`, by virtue of `(0_I, 6.2.3)`; since `A'` and `A_λ` are local rings and `𝔪' = 𝔪_λ A'`, `A'` is
even a faithfully flat `A_λ`-module `(0_I, 6.6.2)`. Suppose finally, in addition, that the `A_λ` are Noetherian; the
`𝔪_λ`-preadic topologies are then separated `(0_I, 7.3.5)`; let us show that it follows first that on `A'` the `𝔪'`-adic
topology is separated. Indeed, if `x' ∈ A'` belongs to every `𝔪'^n` `(n > 0)`, it is the image of some `x_μ ∈ A_μ` for a
certain index `μ`, and since the inverse image in `A_μ` of `𝔪'^n = 𝔪_μ^n A'` is `𝔪_μ^n` `(0_I, 6.6.1)`, `x_μ` belongs to
every `𝔪_μ^n`, hence `x_μ = 0` by hypothesis, and consequently `x' = 0`. Denote by `Â'` the completion of `A'` for the
`𝔪'`-adic topology; what precedes shows that `A' ⊂ Â'`. We shall show that `Â'` is Noetherian and `A_λ`-flat for every
`λ`; it will

<!-- original page 366 -->

follow that `Â'` is `A'`-flat `(0_I, 6.2.3)`, and since `𝔪' Â' ≠ Â'`, `Â'` is a faithfully flat `A'`-module
`(0_I, 6.6.2)`, whence one will finally conclude that `A'` is Noetherian `(0_I, 6.5.2)`, which will complete the proof
of the lemma.

One has `Â' = lim_n A'/𝔪'^n`; on account of the fact that `A'` is `A_λ`-flat, one has

```text
  𝔪'^n/𝔪'^{n+1} = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{A_λ} A'
                = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{K_λ} (K_λ ⊗_{A_λ} A')
                = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{K_λ} K;
```

since `𝔪_λ^n/𝔪_λ^{n+1}` is a `K_λ`-vector space of finite dimension, `𝔪'^n/𝔪'^{n+1}` is a `K`-vector space of finite
dimension for every `n ≥ 0`. It therefore follows from `(0_I, 7.2.12)` and `(0_I, 7.2.8)` that `Â'` is Noetherian. We
further know that the maximal ideal of `Â'` is `𝔪' Â'` and that `Â'/𝔪'^n Â'` is isomorphic to `A'/𝔪'^n`; since
`A'/𝔪'^n = (A_λ/𝔪_λ^n) ⊗_{A_λ} A'`, `A'/𝔪'^n` is a flat `(A_λ/𝔪_λ^n)`-module `(0_I, 6.2.1)`; criterion `(10.2.2)` is
therefore applicable to the Noetherian `A_λ`-algebra `Â'`, and shows that `Â'` is `A_λ`-flat.

**10.3.1.4.**

<!-- label: 0_III.10.3.1.4 -->

We now take up the general case. There exist an ordinal `γ` and, for every ordinal `λ ≤ γ`, a subfield `k_λ` of `K`
containing `k`, such that: 1° For every `λ < γ`, `k_{λ+1}` is an extension of `k_λ` generated by a single element; 2°
For every ordinal `μ` without predecessor, `k_μ = ⋃_{λ<μ} k_λ`; 3° `K = k_γ`. Indeed, it suffices to consider a
bijection `ξ ↦ t_ξ` of the set of ordinals `ξ ≤ β` (for a suitable `β`) onto `K`, to define `k_λ` by transfinite
induction (for `λ ≤ β`) as the union of the `k_μ` for `μ < λ` if `λ` has no predecessor, and, if `λ = ν + 1`, as
`k_ν(t_ξ)`, where `ξ` is the smallest ordinal such that `t_ξ ∉ k_ν`; `γ` is then by definition the smallest ordinal
`≤ β` such that `k_γ = K`.

This being so, we shall define, by transfinite recursion, a family of Noetherian local rings `A_λ` for `λ ≤ γ`, and
local homomorphisms `f_{μλ} : A_λ → A_μ` for `λ ≤ μ`, satisfying the following conditions:

(i) `(A_λ, f_{μλ})` is an inductive system and `A_0 = A`.

(ii) For every `λ`, one has a `k`-isomorphism `A_λ/𝔍 A_λ ⥲ k_λ`.

(iii) For `λ ≤ μ`, `A_μ` is a flat `A_λ`-module.

Suppose then that the `A_λ` and the `f_{μλ}` are defined for `λ < μ < ξ`, and suppose first that `ξ = ζ + 1`, so that
`k_ξ = k_ζ(t)`. If `t` is transcendental over `k_ζ`, one defines `A_ξ` following the procedure of `(10.3.1.1)` as equal
to `(A_ζ[T])_{𝔍 A_ζ[T]}`; `f_{ξζ}` is the canonical map, and for `λ < ζ` one takes `f_{ξλ} = f_{ξζ} ∘ f_{ζλ}`; the
verification of conditions (i) to (iii) is then immediate, in view of what was proved in `(10.3.1.1)`. Suppose next that
`t` is algebraic, and let `h` be its minimal polynomial in `k_ζ[T]`, `H` a unitary polynomial of `A_ζ[T]` whose image in
`k_ζ[T]` is `h`; one then takes `A_ξ` equal to `A_ζ[T]/(H)`, the `f_{ξλ}` being defined as before; the verification of
conditions (i) to (iii) then follows from what was seen in `(10.3.1.2)`.

Suppose now that `ξ` has no predecessor; one then takes for `A_ξ` the inductive limit of the inductive system of local
rings `(A_λ, f_{μλ})` for `λ < ξ`; `f_{ξλ}` is defined as the canonical map for `λ < ξ`. The fact that `A_ξ` is local
Noetherian, that the `f_{ξλ}` are local homomorphisms, and conditions (i) to (iii) for `λ ≤ ξ`

<!-- original page 367 -->

then follow from the inductive hypothesis and from Lemma `(10.3.1.3)`. This construction being done, it is clear that
the ring `B = A_γ` satisfies the statement of `(10.3.1)`.

One should note that by virtue of `(10.2.1, c))`, one has a canonical isomorphism

```text
  gr(A) ⊗_k K ⥲ gr(B).                                                  (10.3.1.5)
```

On the other hand, one may replace `B` by its `𝔍 B`-adic completion `B̂` without changing the conclusions of `(10.3.1)`,
since `B̂` is a flat `B`-module `(0_I, 7.3.3)`, hence a flat `A`-module `(0_I, 6.2.1)`.

We have moreover proved the

**Corollary (10.3.2).**

<!-- label: 0_III.10.3.2 -->

*If `K` is an extension of finite degree, one may suppose that `B` is a finite `A`-algebra.*

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iii/03-c0-s10-complements-modules-plats.md;
     PDF: ~/Code/pdfs/ega/EGA-III-1.pdf, pp. 361–367 (IHÉS print) / pp. 17–23 (PDF) -->
