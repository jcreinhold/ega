# Chapter I — The Language of Schemes

## §2. Preschemes and Morphisms of Preschemes

<!-- label: I.2 -->

### 2.1. Definition of preschemes

<!-- label: I.2.1 -->

**(2.1.1)** Given a ringed space `(X, 𝒪_X)`, an open subset `V ⊂ X` is called an _affine open_ if the ringed space
`(V, 𝒪_X | V)` is an affine scheme (1.7.1).

**Definition (2.1.2).** A _prescheme_ [modern: scheme] is a ringed space `(X, 𝒪_X)` such that every point of `X` admits
an affine open neighborhood.

**Proposition (2.1.3).** If `(X, 𝒪_X)` is a prescheme, the affine open subsets form a basis of the topology of `X`.

**Proof.** Let `V` be an open neighborhood of `x`, and `W` an affine open neighborhood with ring `A`. Then `V ∩ W` is
open in `W`, so some `D(f) ⊂ V ∩ W` (`f ∈ A`) is an affine open neighborhood of `x`, by (1.1.10) and (1.3.6).

**Proposition (2.1.4).** The underlying space of a prescheme is a Kolmogorov space.

**Proposition (2.1.5).** In a prescheme `(X, 𝒪_X)`, every closed irreducible subset of `X` admits a unique generic
point; thus `x ↦ {x}̄` is a bijection of `X` onto the set of closed irreducible subsets.

**Proof.** If `Y` is closed irreducible and `y ∈ Y`, let `U` be an affine open neighborhood of `y`. Then `U ∩ Y` is
dense in `Y`, irreducible, and closed in `U`; by (1.1.14), `U ∩ Y = {x}̄ ∩ U` for some `x ∈ U`, so `Y = {x}̄`.
Uniqueness follows from (2.1.4) and (0.2.1.3).

**(2.1.6)** If `Y ⊂ X` is closed irreducible with generic point `y`, the local ring `𝒪_y` (also written `𝒪_{X/Y}`) is
called the _local ring of `X` along `Y`_ (or the _local ring of `Y` in `X`_).

If `X` is irreducible with generic point `x`, `𝒪_x` is the _ring of rational functions on_ `X` (cf. §7).

**Proposition (2.1.7).** For every open `U ⊂ X`, the ringed space `(U, 𝒪_X | U)` is a prescheme — the _induced_
prescheme (or _restriction_) on `U`.

**(2.1.8)** A prescheme `(X, 𝒪_X)` is _irreducible_ (resp. _connected_) if `X` is. It is _integral_ if it is irreducible
and reduced (cf. (5.1.4)). It is _locally integral_ if every `x ∈ X` admits an open neighborhood `U` such that the
induced prescheme on `U` is integral.

### 2.2. Morphisms of preschemes

<!-- label: I.2.2 -->

**Definition (2.2.1).** Given two preschemes `(X, 𝒪_X)` and `(Y, 𝒪_Y)`, a _morphism of preschemes_ `(X, 𝒪_X) → (Y, 𝒪_Y)`
is a morphism `(ψ, θ)` of ringed spaces such that for every `x ∈ X`, `θ_x^♯ : 𝒪_{ψ(x)} → 𝒪_x` is a _local_ homomorphism.

Passing to quotients, the stalk map gives a monomorphism `θ^x : κ(ψ(x)) → κ(x)`, making `κ(x)` an extension of
`κ(ψ(x))`.

**(2.2.2)** Composition of two morphisms of preschemes is a morphism of preschemes (by `θ″^♯ = θ^♯ ∘ ψ*(θ′^♯)`,
(0.3.5.5)). Thus preschemes form a _category_; we write `Hom(X, Y)` for the set of morphisms.

**Example (2.2.3).** For an open `U ⊂ X`, the canonical injection `(U, 𝒪_X | U) → (X, 𝒪_X)` is a _monomorphism_ of
preschemes.

**Proposition (2.2.4).** Let `(X, 𝒪_X)` be a prescheme and `(S, 𝒪_S)` an affine scheme of ring `A`. There is a canonical
bijection between morphisms of preschemes `(X, 𝒪_X) → (S, 𝒪_S)` and ring homomorphisms `A → Γ(X, 𝒪_X)`.

**Proof sketch.** Any morphism `(ψ, θ)` gives `Γ(θ) : A → Γ(X, 𝒪_X)`. Conversely, given `φ : A → Γ(X, 𝒪_X)`, cover `X`
by affine opens `(V_α)`; composing with restriction `Γ(X, 𝒪_X) → Γ(V_α, 𝒪_X | V_α)` gives `φ_α`, which corresponds by
(1.7.3) to a morphism `(ψ_α, θ_α) : V_α → S`. These agree on overlaps (by (2.1.3) and stalkwise compatibility), so they
glue to a morphism `(ψ, θ) : X → S` of preschemes with `Γ(θ) = φ`.

For `f ∈ A`, `ψ⁻¹(D(f)) = X_{φ(f)}` (the open set where the section `φ(f)` does not vanish; see (0.5.5.2)). (2.2.4.1)

**Proposition (2.2.5).** Under the hypotheses of (2.2.4), let `φ : A → Γ(X, 𝒪_X)`, `f : X → S` the corresponding
morphism, `𝒢` an `𝒪_X`-module, `ℱ` an `𝒪_S`-module, and `M = Γ(S, ℱ)`. There is a canonical bijection between
`f`-morphisms `ℱ → 𝒢` (0.4.4.1) and `A`-homomorphisms `M → (Γ(X, 𝒢))_{[φ]}`.

**(2.2.6)** A morphism `(ψ, θ) : X → Y` of preschemes is _open_ (resp. _closed_) if for every open `U ⊂ X` (resp. closed
`F ⊂ X`), `ψ(U)` is open (resp. `ψ(F)` is closed) in `Y`. It is _dominant_ if `ψ(X)` is dense in `Y`, and _surjective_
if `ψ` is. These conditions depend only on `ψ`.

**Proposition (2.2.7).** Let `f : X → Y` and `g : Y → Z` be morphisms of preschemes.

> (i) If `f`, `g` are both open (resp. closed, dominant, surjective), so is `g ∘ f`. (ii) If `f` is surjective and
> `g ∘ f` closed, then `g` is closed. (iii) If `g ∘ f` is surjective, so is `g`.

**Proposition (2.2.8).** Let `f : X → Y` and `(U_α)` an open cover of `Y`. `f` is open (resp. closed, surjective,
dominant) iff each restriction `ψ⁻¹(U_α) → U_α` is.

**(2.2.9)** Let `X, Y` have finitely many irreducible components `X_i, Y_i` (`1 ≤ i ≤ n`) with generic points `ξ_i, η_i`
(2.1.5). A morphism `f = (ψ, θ) : X → Y` is _birational_ if for every `i`, `ψ⁻¹(η_i) = {ξ_i}` and
`θ_{ξ_i}^♯ : 𝒪_{η_i} → 𝒪_{ξ_i}` is an _isomorphism_. A birational morphism is dominant (0.2.1.8), and surjective if it
is closed.

**Notation (2.2.10).** When no confusion threatens, we suppress the structure sheaf (resp. the morphism of structure
sheaves) from notation. For an open `U ⊂ X` of a prescheme, "the prescheme `U`" means the induced prescheme on `U`.

### 2.3. Gluing of preschemes

<!-- label: I.2.3 -->

**(2.3.1)** By (2.1.2), every ringed space obtained by gluing preschemes (0.4.1.7) is a prescheme. In particular, every
prescheme can be obtained by _gluing affine schemes_.

**Example (2.3.2).** Let `K` be a field, `B = K[s]`, `C = K[t]` polynomial rings; set `X_1 = Spec(B)`, `X_2 = Spec(C)`.
In `X_1` (resp. `X_2`), let `U_{12} = D(s)` (resp. `U_{21} = D(t)`), with ring `B_s` (resp. `C_t`). Let
`u_{12} : U_{21} → U_{12}` be the isomorphism corresponding to `B_s → C_t` sending `f(s)/sᵐ` to `f(1/t)/(1/tᵐ)`. Glue
`X_1, X_2` along `U_{12}, U_{21}` via `u_{12}` (no cocycle condition). The resulting prescheme `X` is _not_ affine:
`Γ(X, 𝒪_X) = K`, since a global section is a polynomial `f(s) = g(t) = f(1/t)` on the overlap, forcing `f = g ∈ K`.
(This is the projective line `ℙ¹_K`; see (II.2.4.3).)

### 2.4. Local schemes

<!-- label: I.2.4 -->

**(2.4.1)** An affine scheme `X = Spec(A)` is a _local scheme_ if `A` is a local ring; `X` then has a unique closed
point `a`, and `a ∈ {b}̄` for every `b ∈ X` (1.1.7).

For a prescheme `Y` and `y ∈ Y`, the local scheme `Spec(𝒪_y)` is the _local scheme of `Y` at_ `y`. For an affine open
`V ⊂ Y` with ring `B` containing `y`, `𝒪_y ≅ B_y`, and the canonical `B → B_y` gives a morphism `Spec(𝒪_y) → V → Y`,
independent of `V` — the _canonical morphism_ `Spec(𝒪_y) → Y`.

**Proposition (2.4.2).** Let `Y` be a prescheme. For `y ∈ Y`, let `(ψ, θ) : Spec(𝒪_y) → Y` be the canonical morphism.
Then `ψ` is a homeomorphism of `Spec(𝒪_y)` onto the subspace `S_y = {z ∈ Y : y ∈ {z}̄}` (the _generizations_ of `y`);
for `z = ψ(𝔭)`, `θ_z^♯ : 𝒪_z → (𝒪_y)_𝔭` is an isomorphism. So `(ψ, θ)` is a monomorphism of ringed spaces.

There is thus a bijection between `Spec(𝒪_y)` and the set of closed irreducible subsets of `Y` containing `y`.

**Corollary (2.4.3).** `y ∈ Y` is the generic point of an irreducible component of `Y` iff `𝒪_y` has only its maximal
ideal as prime — i.e., `𝒪_y` has dimension zero.

**Proposition (2.4.4).** Let `X = Spec(A)` be a local scheme with closed point `a`, and `Y` a prescheme. Every morphism
`u = (ψ, θ) : X → Y` factors uniquely as `X → Spec(𝒪_{ψ(a)}) → Y`, where the second arrow is the canonical morphism and
the first corresponds to a local homomorphism `𝒪_{ψ(a)} → A`. This gives a canonical bijection between `Hom(X, Y)` and
the set of local homomorphisms `𝒪_y → A` (for `y ∈ Y`).

**(2.4.5)** The spectrum of a field `K` is a single point. For `A` a local ring with maximal ideal `𝔪`, a local
homomorphism `A → K` has kernel `𝔪`, factoring as `A → A/𝔪 → K` with the second map a field monomorphism. Thus morphisms
`Spec(K) → Spec(A)` correspond bijectively to field monomorphisms `A/𝔪 → K`.

For `y ∈ Y` and an ideal `𝔞_y ⊂ 𝒪_y`, the canonical `𝒪_y → 𝒪_y / 𝔞_y` gives a morphism `Spec(𝒪_y/𝔞_y) → Spec(𝒪_y) → Y`,
the _canonical morphism_. When `𝔞_y = 𝔪_y`, this gives the morphism `Spec(κ(y)) → Y`.

**Corollary (2.4.6).** Let `X = Spec(K)` for `K` a field with unique point `ξ`, and `Y` a prescheme. Every morphism
`u : X → Y` factors uniquely as `X → Spec(κ(ψ(ξ))) → Y`, with the first arrow given by a field monomorphism
`κ(ψ(ξ)) → K`. Hence `Hom(X, Y) ↔ ⨆_{y ∈ Y} Hom_{field}(κ(y), K)`.

**Corollary (2.4.7).** For every `y ∈ Y`, the canonical morphism `Spec(𝒪_y / 𝔞_y) → Y` is a monomorphism of ringed
spaces.

**Remark (2.4.8).** On a local scheme, every invertible `𝒪_X`-module is _trivial_ (isomorphic to `𝒪_X`), since every
affine open containing the closed point equals `X`. This fails for general affine schemes; for `A` normal, invertibility
implies triviality iff `A` is a UFD.

### 2.5. Preschemes over a prescheme

<!-- label: I.2.5 -->

**Definition (2.5.1).** Given a prescheme `S`, a _prescheme over_ `S` (or _`S`-prescheme_) is a prescheme `X` together
with a morphism `φ : X → S`, the _structure morphism_. `S` is the _base prescheme_. When `S = Spec(A)`, `X` is an
_`A`-prescheme_; this is equivalent to making `𝒪_X` a sheaf of `A`-algebras.

Every prescheme is canonically a `ℤ`-prescheme.

For `φ : X → S` and `x ∈ X`, `s ∈ S`, `x` is _over_ `s` if `φ(x) = s`. `X` _dominates_ `S` if `φ` is dominant.

**(2.5.2)** For `S`-preschemes `X, Y`, a morphism `u : X → Y` is an _`S`-morphism_ (or _morphism over `S`_) if
`φ_Y ∘ u = φ_X`. `S`-preschemes form a category, with morphism set `Hom_S(X, Y)`; the identity is `1_X`. When
`S = Spec(A)`, we say _`A`-morphism_.

**(2.5.3)** A morphism `v : X′ → X` makes any `S`-prescheme `X` into an `S`-prescheme `X′`; restrictions of
`S`-morphisms to open subsets are `S`-morphisms; `S`-morphisms glue from compatible restrictions on an open cover.

**(2.5.4)** A morphism `S′ → S` makes every `S′`-prescheme into an `S`-prescheme. If `S′ ⊂ S` is open and an
`S`-prescheme `X` has `φ(X) ⊂ S′`, then `X` is naturally an `S′`-prescheme.

**(2.5.5)** An _`S`-section_ of an `S`-prescheme `X` is an `S`-morphism `S → X` — i.e., `ψ : S → X` with `φ ∘ ψ = 1_S`.
Write `Γ(X/S)` for the set of `S`-sections.

