# Chapter 0 — Preliminaries

## §6. Flatness

<!-- label: 0.6 -->

**(6.0)** The notion of flatness is due to J.-P. Serre [16]; in what follows, we omit proofs that are given in N.
Bourbaki's _Algèbre commutative_, to which we refer the reader. All rings are assumed commutative.[^6-1]

If `M`, `N` are `A`-modules and `M′` (resp. `N′`) is a submodule of `M` (resp. `N`), we write `Im(M′ ⊗_A N′)` for the
submodule of `M ⊗_A N` that is the image of the canonical map `M′ ⊗_A N′ → M ⊗_A N`.

### 6.1. Flat modules

<!-- label: 0.6.1 -->

**(6.1.1)** Let `M` be an `A`-module. The following are equivalent:

> a) The functor `M ⊗_A N` in `N` is exact on `A`-modules; b) `Tor_i^A(M, N) = 0` for every `i > 0` and every `A`-module
> `N`; c) `Tor_1^A(M, N) = 0` for every `A`-module `N`.

When `M` satisfies these conditions, `M` is called a _flat_ `A`-module. Every free `A`-module is plainly flat.

For `M` to be flat, it suffices that for every _finite-type_ ideal `𝔍` of `A`, the canonical map `M ⊗_A 𝔍 → M ⊗_A A = M`
be _injective_.

**(6.1.2)** Every inductive limit of flat `A`-modules is flat. A direct sum `⊕_{λ ∈ L} M_λ` is flat if and only if each
`M_λ` is flat. In particular, every projective `A`-module is flat.

Let `0 → M′ → M → M″ → 0` be an exact sequence with `M″` _flat_. Then for every `A`-module `N`,

```
0 → M′ ⊗ N → M ⊗ N → M″ ⊗ N → 0
```

is exact. Moreover, for `M` to be flat, it is necessary and sufficient that `M′` be flat (but `M` and `M′` may both be
flat without `M″ = M/M′` being flat).

**(6.1.3)** Let `M` be a flat `A`-module and `N` an arbitrary `A`-module. For two submodules `N′, N″` of `N`,

```
Im(M ⊗ (N′ + N″)) = Im(M ⊗ N′) + Im(M ⊗ N″)
Im(M ⊗ (N′ ∩ N″)) = Im(M ⊗ N′) ∩ Im(M ⊗ N″)
```

(images taken in `M ⊗ N`).

**(6.1.4)** Let `M`, `N` be `A`-modules, `M′` (resp. `N′`) a submodule of `M` (resp. `N`), and suppose one of
`M/M′, N/N′` is flat. Then `Im(M′ ⊗ N′) = Im(M′ ⊗ N) ∩ Im(M ⊗ N′)` (images in `M ⊗ N`). In particular, if `𝔍` is an
ideal of `A` and `M/M′` is flat, then `𝔍 M′ = M′ ∩ 𝔍 M`.

### 6.2. Change of ring

<!-- label: 0.6.2 -->

When an abelian group `M` is endowed with several module structures over rings `A`, `B`, …, instead of saying that `M`
is flat as an `A`-module, `B`-module, etc., we shall sometimes say `M` is `A`-_flat_, `B`-_flat_, etc.

**(6.2.1)** Let `A, B` be rings, `M` an `A`-module, and `N` an `(A, B)`-bimodule. If `M` is flat and `N` is `B`-flat,
then `M ⊗_A N` is `B`-flat. In particular, if `M, N` are two flat `A`-modules, `M ⊗_A N` is a flat `A`-module. If `B` is
an `A`-algebra and `M` is a flat `A`-module, the `B`-module `M_{(B)} = M ⊗_A B` is flat. Finally, if `B` is an
`A`-algebra which is flat as an `A`-module, and `N` is a flat `B`-module, then `N` is also `A`-flat.

**(6.2.2)** Let `A` be a ring and `B` an `A`-algebra which is flat as an `A`-module. Let `M, N` be `A`-modules with `M`
admitting a finite presentation. The canonical homomorphism

```
(6.2.2.1)    Hom_A(M, N) ⊗_A B → Hom_B(M ⊗_A B, N ⊗_A B)
```

sending `u ⊗ b` to the homomorphism `m ⊗ b′ ↦ u(m) ⊗ b′b` is an isomorphism.

**(6.2.3)** Let `(A_λ, φ_{μλ})` be a filtered inductive system of rings with `A = lim⃗ A_λ`. For each `λ`, let `M_λ` be
an `A_λ`-module, and for `λ ≤ μ` let `θ_{μλ} : M_λ → M_μ` be a `φ_{μλ}`-homomorphism, with `(M_λ, θ_{μλ})` an inductive
system; set `M = lim⃗ M_λ`, an `A`-module. If each `M_λ` is `A_λ`-_flat_, then `M` is `A`-_flat_. Indeed, let `𝔍` be a
finite-type ideal of `A`; by the definition of the inductive limit, there is an index `λ` and an ideal `𝔍_λ ⊂ A_λ` with
`𝔍 = 𝔍_λ A`. Setting `𝔍′_μ = 𝔍_λ A_μ` for `μ ≥ λ`, also `𝔍 = lim⃗ 𝔍′_μ` (over `μ ≥ λ`). Since `lim⃗` is exact and
commutes with tensor products,

```
M ⊗_A 𝔍 = lim⃗ (M_μ ⊗_{A_μ} 𝔍′_μ) = lim⃗ 𝔍′_μ M_μ = 𝔍 M.
```

### 6.3. Localization of flatness

<!-- label: 0.6.3 -->

**(6.3.1)** Let `A` be a ring and `S` a multiplicative subset. Then `S⁻¹A` is a flat `A`-module: for every `A`-module
`N`, `N ⊗_A S⁻¹A` is identified with `S⁻¹N` (1.2.5), and `S⁻¹N` is exact in `N` (1.3.2).

If `M` is a flat `A`-module, then `S⁻¹M = M ⊗_A S⁻¹A` is `S⁻¹A`-flat (6.2.1) — hence also `A`-flat by (6.2.1). In
particular, if `P` is an `S⁻¹A`-module viewed as an `A`-module (isomorphic to `S⁻¹P`), then `P` is `A`-flat if and only
if it is `S⁻¹A`-flat.

**(6.3.2)** Let `A` be a ring, `B` an `A`-algebra, and `T` a multiplicative subset of `B`. If `P` is a `B`-module which
is `A`-_flat_, then `T⁻¹P` is `A`-flat. Indeed, for every `A`-module `N`,

```
(T⁻¹P) ⊗_A N = (T⁻¹B ⊗_B P) ⊗_A N = T⁻¹B ⊗_B (P ⊗_A N) = T⁻¹(P ⊗_A N);
```

`T⁻¹(P ⊗_A N)` is exact in `N` as the composite of two exact functors `P ⊗_A N` (in `N`) and `T⁻¹Q` (in `Q`). If `S ⊂ A`
is multiplicative with its image in `B` _contained_ in `T`, then `T⁻¹P = S⁻¹(T⁻¹P)`, so also `S⁻¹A`-flat by (6.3.1).

**(6.3.3)** Let `φ : A → B` be a ring homomorphism and `M` a `B`-module. The following are equivalent:

> a) `M` is `A`-flat; b) For every maximal ideal `𝔫` of `B`, `M_𝔫` is `A`-flat; c) For every maximal ideal `𝔫` of `B`,
> with `𝔪 = φ⁻¹(𝔫)`, `M_𝔫` is `A_𝔪`-flat.

Indeed, since `M_𝔫 = (M_𝔫)_𝔪`, the equivalence of _b)_ and _c)_ follows from (6.3.1), and _a)_ ⟹ _b)_ is (6.3.2). For
_b)_ ⟹ _a)_: given an injective `u : N′ → N` of `A`-modules, we must show `v = 1 ⊗ u : M ⊗_A N′ → M ⊗_A N` is injective.
Since `v` is also a `B`-module homomorphism, it suffices that `v_𝔫` be injective for every maximal `𝔫`. But

```
(M ⊗_A N)_𝔫 = B_𝔫 ⊗_B (M ⊗_A N) = M_𝔫 ⊗_A N,
```

so `v_𝔫` is `1 ⊗ u : M_𝔫 ⊗_A N′ → M_𝔫 ⊗_A N`, injective since `M_𝔫` is `A`-flat.

In particular (taking `B = A`), an `A`-module `M` is flat iff `M_𝔪` is `A_𝔪`-flat for every maximal ideal `𝔪` of `A`.

**(6.3.4)** Let `M` be an `A`-module. If `M` is flat and `f ∈ A` is not a zero divisor of `A`, then `f` annihilates no
nonzero element of `M`: the homomorphism `m ↦ f · m` is `1 ⊗ u`, where `u : a ↦ f · a` on `A` and `M ≅ M ⊗_A A`; `u` is
injective, so `1 ⊗ u` is injective since `M` is flat. In particular, if `A` is an integral ring, `M` is _torsion-free_.

Conversely, suppose `A` is integral and `M` is torsion-free, and that for every maximal `𝔪` of `A`, `A_𝔪` is a _discrete
valuation ring_. Then `M` is `A`-_flat_. By (6.3.3), it suffices to show `M_𝔪` is `A_𝔪`-flat, so assume `A` is already a
DVR. Since `M = lim⃗ M_i` over its finite-type submodules (each torsion-free), one may assume `M` is of finite type
(6.1.2); then `M` is a free `A`-module, whence the assertion.

In particular, if `A` is integral and `φ : A → B` is a homomorphism making `B` a flat `A`-module with `B ≠ {0}`, then
`φ` is _injective_. Conversely, if `B` is integral, `A` is a subring of `B`, and `A_𝔪` is a DVR for every maximal `𝔪`,
then `B` is `A`-flat.

### 6.4. Faithfully flat modules

<!-- label: 0.6.4 -->

**(6.4.1)** For an `A`-module `M`, the following are equivalent:

> a) A sequence `N′ → N → N″` of `A`-modules is exact iff `M ⊗ N′ → M ⊗ N → M ⊗ N″` is exact; b) `M` is flat, and for
> every `A`-module `N`, `M ⊗ N = 0` implies `N = 0`; c) `M` is flat, and for every homomorphism `v : N → N′` of
> `A`-modules, `1_M ⊗ v = 0` implies `v = 0`; d) `M` is flat, and `𝔪 M ≠ M` for every maximal ideal `𝔪` of `A`.

When `M` satisfies these conditions, `M` is _faithfully flat_; `M` is then necessarily a _faithful_ module. Moreover,
for `u : N → N′`, `u` is injective (resp. surjective, bijective) iff `1 ⊗ u : M ⊗ N → M ⊗ N′` is.

**(6.4.2)** A nonzero free module is faithfully flat. So is the direct sum of a flat module and a faithfully flat one.
If `S ⊂ A` is multiplicative, `S⁻¹A` is faithfully flat as an `A`-module only if `S` consists of invertible elements (so
`S⁻¹A = A`).

**(6.4.3)** Let `0 → M′ → M → M″ → 0` be exact with `M′` and `M″` flat. If either is faithfully flat, then `M` is
faithfully flat.

**(6.4.4)** Let `A, B` be rings, `M` an `A`-module, and `N` an `(A, B)`-bimodule. If `M` is faithfully flat and `N` is a
faithfully flat `B`-module, then `M ⊗_A N` is a faithfully flat `B`-module. In particular, if `M, N` are two faithfully
flat `A`-modules, so is `M ⊗_A N`. If `B` is an `A`-algebra and `M` is a faithfully flat `A`-module, then `M_{(B)}` is a
faithfully flat `B`-module.

**(6.4.5)** If `M` is a faithfully flat `A`-module and `S ⊂ A` is multiplicative, then `S⁻¹M` is a faithfully flat
`S⁻¹A`-module (since `S⁻¹M = M ⊗_A S⁻¹A`, by (6.4.4)). Conversely, if `M_𝔪` is faithfully flat over `A_𝔪` for every
maximal `𝔪`, then `M` is faithfully flat over `A`: it is `A`-flat by (6.3.3), and

```
M_𝔪 / 𝔪 M_𝔪 = (M ⊗_A A_𝔪) ⊗_{A_𝔪} (A_𝔪 / 𝔪 A_𝔪) = M ⊗_A (A/𝔪) = M / 𝔪 M,
```

so the hypothesis gives `M / 𝔪 M ≠ 0` for every maximal `𝔪`, whence (6.4.1).

### 6.5. Restriction of scalars

<!-- label: 0.6.5 -->

**(6.5.1)** Let `A` be a ring and `φ : A → B` a homomorphism making `B` an `A`-algebra. Suppose there is a `B`-module
`N` that is a _faithfully flat_ `A`-module. Then for every `A`-module `M`, the map `x ↦ 1 ⊗ x` from `M` to
`B ⊗_A M = M_{(B)}` is _injective_. In particular, `φ` is injective; for every ideal `𝔞 ⊂ A`, `φ⁻¹(𝔞 B) = 𝔞`; for every
maximal (resp. prime) ideal `𝔪 ⊂ A`, there is a maximal (resp. prime) ideal `𝔫 ⊂ B` with `φ⁻¹(𝔫) = 𝔪`.

**(6.5.2)** Under the conditions of (6.5.1), one identifies `A` with a subring of `B` via `φ`; more generally, `M` is
identified with an `A`-submodule of `M_{(B)}`. Note that if `B` is _Noetherian_, so is `A`: the map `𝔞 ↦ 𝔞 B` is an
increasing injection from ideals of `A` into ideals of `B`, so a strictly increasing infinite chain of ideals of `A`
would give one of `B`.

### 6.6. Faithfully flat rings

<!-- label: 0.6.6 -->

**(6.6.1)** Let `φ : A → B` be a ring homomorphism. The following are equivalent:

> a) `B` is a faithfully flat `A`-module (equivalently, `M_{(B)}` is _exact and faithful_ in `M`); b) `φ` is injective
> and `B / φ(A)` is `A`-flat; c) `B` is `A`-flat (so `M_{(B)}` is exact) and `x ↦ 1 ⊗ x` from `M` to `M_{(B)}` is
> injective for every `M`; d) `B` is `A`-flat and `φ⁻¹(𝔞 B) = 𝔞` for every ideal `𝔞 ⊂ A`; e) `B` is `A`-flat and for
> every maximal `𝔪 ⊂ A` there is a maximal `𝔫 ⊂ B` with `φ⁻¹(𝔫) = 𝔪`.

Under these conditions, `A` is identified with a subring of `B`.

**(6.6.2)** Let `A` be a _local_ ring with maximal ideal `𝔪` and `B` an `A`-algebra with `𝔪 B ≠ B` (this holds, for
example, when `B` is local and `A → B` is _local_). If `B` is `A`-_flat_, then `B` is `A`-_faithfully flat_. Indeed,
`𝔪 B ≠ B` gives a maximal ideal `𝔫 ⊂ B` containing `𝔪 B`; `φ⁻¹(𝔫) ∩ A` contains `𝔪` and not `1`, so `φ⁻¹(𝔫) = 𝔪`, and
criterion _e)_ of (6.6.1) applies. Consequently, if `B` is Noetherian, so is `A` (6.5.2).

**(6.6.3)** Let `B` be an `A`-algebra which is faithfully flat as an `A`-module. For every `A`-module `M` and submodule
`M′ ⊂ M`, identifying `M` with a submodule of `M_{(B)}`, one has `M′ = M ∩ M′_{(B)}`. For `M` to be `A`-flat (resp.
faithfully flat), it is necessary and sufficient that `M_{(B)}` be `B`-flat (resp. faithfully flat).

**(6.6.4)** Let `B` be an `A`-algebra and `N` a faithfully flat `B`-module. For `B` to be `A`-flat (resp. faithfully
flat), it is necessary and sufficient that `N` be.

In particular, let `C` be a `B`-algebra. If `C` is faithfully flat over `B` and `B` is faithfully flat over `A`, then
`C` is faithfully flat over `A`. If `C` is faithfully flat over `B` and over `A`, then `B` is faithfully flat over `A`.

### 6.7. Flat morphisms of ringed spaces

<!-- label: 0.6.7 -->

**(6.7.1)** Let `f : X → Y` be a morphism of ringed spaces and `ℱ` an `𝒪_X`-Module. `ℱ` is `f`-_flat_ (or `Y`-_flat_
when no confusion about `f` can arise) _at a point_ `x ∈ X` if `ℱ_x` is a flat `𝒪_{f(x)}`-module; `ℱ` is `f`-flat _over_
`y ∈ Y` if it is `f`-flat at every `x ∈ f⁻¹(y)`; `ℱ` is `f`-_flat_ if it is `f`-flat at every point of `X`. The morphism
`f` is _flat at_ `x ∈ X` (resp. _flat over_ `y ∈ Y`, resp. _flat_) if `𝒪_X` is `f`-flat at `x` (resp. over `y`, resp.
`f`-flat).

**(6.7.2)** With the notation of (6.7.1), if `ℱ` is `f`-flat at `x`, then for every open neighborhood `U` of `y = f(x)`,
the functor `(f*(𝒢) ⊗_{𝒪_X} ℱ)_x` in `𝒢` is _exact_ on `(𝒪_Y|U)`-Modules: this stalk is canonically `𝒢_y ⊗_{𝒪_y} ℱ_x`,
whence the assertion. In particular, if `f` is a flat morphism, `f*` is exact on `𝒪_Y`-Modules.

**(6.7.3)** Conversely, suppose `𝒪_Y` is _coherent_, and that for _every_ open neighborhood `U` of `y`, the functor
`(f*(𝒢) ⊗_{𝒪_X} ℱ)_x` is exact in `𝒢` on _coherent_ `(𝒪_Y|U)`-Modules. Then `ℱ` is `f`-_flat at_ `x`. It suffices to
show that for every finite-type ideal `𝔍 ⊂ 𝒪_y`, the canonical map `𝔍 ⊗_{𝒪_y} ℱ_x → ℱ_x` is injective (6.1.1). By
(5.3.8) there is an open `U ∋ y` and a coherent ideal sheaf `𝒥 ⊂ 𝒪_Y|U` with `𝒥_y = 𝔍`, whence the conclusion.

**(6.7.4)** The results of (6.1) on flat modules carry over at once to propositions on `f`-flat sheaves at a point:

If `0 → ℱ′ → ℱ → ℱ″ → 0` is exact and `ℱ″` is `f`-flat at `x`, then for every open `U ∋ y = f(x)` and every
`(𝒪_Y|U)`-Module `𝒢`, the sequence

```
0 → (f*(𝒢) ⊗_{𝒪_X} ℱ′)_x → (f*(𝒢) ⊗_{𝒪_X} ℱ)_x → (f*(𝒢) ⊗_{𝒪_X} ℱ″)_x → 0
```

is exact. For `ℱ` to be `f`-flat at `x`, it is necessary and sufficient that `ℱ′` be. Analogous statements hold for
`f`-flatness over `y ∈ Y` and `f`-flatness on `X`.

**(6.7.5)** Let `f : X → Y` and `g : Y → Z` be morphisms of ringed spaces, `x ∈ X`, `y = f(x)`, and `ℱ` an `𝒪_X`-Module.
If `ℱ` is `f`-flat at `x` and `g` is flat at `y`, then `ℱ` is `(g ∘ f)`-flat at `x` (6.2.1). In particular, if `f` and
`g` are flat, so is `g ∘ f`.

**(6.7.6)** Let `X, Y` be ringed spaces and `f : X → Y` a _flat_ morphism. The canonical homomorphism of bifunctors
(4.4.6)

```
(6.7.6.1)    f*(ℋom_{𝒪_Y}(ℱ, 𝒢)) → ℋom_{𝒪_X}(f*(ℱ), f*(𝒢))
```

is an _isomorphism_ when `ℱ` admits a finite presentation (5.2.5).

Indeed, the question being local, one may assume an exact sequence `𝒪_Y^m → 𝒪_Y^n → ℱ → 0`. Both sides of (6.7.6.1) are
left exact in `ℱ` (using flatness of `f`), so one reduces to `ℱ = 𝒪_Y`, where the assertion is trivial.

**(6.7.8)** A morphism `f : X → Y` of ringed spaces is _faithfully flat_ if `f` is _surjective_ and, for every `x ∈ X`,
`𝒪_x` is a faithfully flat `𝒪_{f(x)}`-module. When `X, Y` are spaces ringed in local rings (5.5.1), this amounts to `f`
being surjective and flat (6.6.2). When `f` is faithfully flat, `f*` is exact and faithful on `𝒪_Y`-Modules (6.6.1,
_a)_), and an `𝒪_Y`-Module `𝒢` is `Y`-flat iff `f*(𝒢)` is (6.6.3).

[^6-1]: See the cited exposé of N. Bourbaki for the generalization of most results to the noncommutative case.
