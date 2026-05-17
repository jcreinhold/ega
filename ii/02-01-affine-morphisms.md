# §1. Affine morphisms

Most of the results in this section are the "global" counterparts of those in Chapter I, §1; they are therefore not
essentially new and merely provide a convenient language for the sequel.

## 1.1. `S`-preschemes and `𝒪_S`-algebras

**(1.1.1)**

<!-- label: II.1.1.1 -->

Let `S` be a prescheme, `X` an `S`-prescheme, and `f : X → S` its structure morphism. We know `(0, 4.2.4)` that the
direct image `f_*(𝒪_X)` is an `𝒪_S`-algebra, which we

<!-- original page 6 -->

denote by `𝒜(X)` when no confusion is likely. If `U` is an open subset of `S`, then

```text
  𝒜(f⁻¹(U)) = 𝒜(X)|U.
```

Likewise, for every `𝒪_X`-module `ℱ` (resp. every `𝒪_X`-algebra `ℬ`), we write `𝒜(ℱ)` (resp. `𝒜(ℬ)`) for the direct
image `f_*(ℱ)` (resp. `f_*(ℬ)`), which is an `𝒜(X)`-module (resp. `𝒜(X)`-algebra), and not just an `𝒪_S`-module (resp.
`𝒪_S`-algebra).

**(1.1.2)**

<!-- label: II.1.1.2 -->

Let `Y` be a second `S`-prescheme, `g : Y → S` its structure morphism, and `h : X → Y` an `S`-morphism, giving the
commutative diagram

```text
        h
   X ─────→ Y                                                            (1.1.2.1)
    \      /
   f \    / g
      ↘  ↙
       S
```

By definition `h = (ψ, θ)`, where `θ : 𝒪_Y → h_*(𝒪_X) = ψ_*(𝒪_X)` is a homomorphism of sheaves of rings; we therefore
obtain `(0, 4.2.2)` a homomorphism of `𝒪_S`-algebras `g_*(θ) : g_*(𝒪_Y) → g_*(h_*(𝒪_X)) = f_*(𝒪_X)`, in other words a
homomorphism of `𝒪_S`-algebras `𝒜(Y) → 𝒜(X)`, which we also denote by `𝒜(h)`. If `h' : Y → Z` is a second `S`-morphism,
it is immediate that `𝒜(h' ∘ h) = 𝒜(h) ∘ 𝒜(h')`. We have thus defined a _contravariant functor_ `𝒜(X)` on the category
of `S`-preschemes, with values in the category of `𝒪_S`-algebras.

Now let `ℱ` be an `𝒪_X`-module, `𝒢` an `𝒪_Y`-module, and `u : 𝒢 → ℱ` an `h`-morphism — that is `(0, 4.4.1)`, a
homomorphism of `𝒪_Y`-modules `𝒢 → h_*(ℱ)`. Then `g_*(u) : g_*(𝒢) → g_*(h_*(ℱ)) = f_*(ℱ)` is a homomorphism
`𝒜(𝒢) → 𝒜(ℱ)` of `𝒪_S`-modules, which we denote by `𝒜(u)`; furthermore, the pair `(𝒜(h), 𝒜(u))` is a _di-homomorphism_
from the `𝒜(Y)`-module `𝒜(𝒢)` to the `𝒜(X)`-module `𝒜(ℱ)`.

**(1.1.3)**

<!-- label: II.1.1.3 -->

If we fix the prescheme `S`, the pairs `(X, ℱ)` with `X` an `S`-prescheme and `ℱ` an `𝒪_X`-module form a _category_: a
_morphism_ `(X, ℱ) → (Y, 𝒢)` is by definition a pair `(h, u)` with `h : X → Y` an `S`-morphism and `u : 𝒢 → ℱ` an
`h`-morphism. We may then say that `(𝒜(X), 𝒜(ℱ))` is a _contravariant functor_ with values in the category whose objects
are pairs consisting of an `𝒪_S`-algebra and a module over that algebra, and whose morphisms are di-homomorphisms.

## 1.2. Affine preschemes over a prescheme

**Definition.**

<!-- label: II.1.2.1 -->

Let `X` be an `S`-prescheme and `f : X → S` its structure morphism. We say that `X` is _affine over_ `S` if there exists
a covering `(S_α)` of `S` by affine opens such that for every `α`, the prescheme induced by `X` on `f⁻¹(S_α)` is affine.

**Example.**

<!-- label: II.1.2.2 -->

Every closed subprescheme of `S` is an `S`-prescheme affine over `S` (`I, 4.2.3` and `4.2.4`).

**Remark.**

<!-- label: II.1.2.3 -->

A prescheme `X` affine over `S` need not itself be an affine scheme, as the example `X = S` from (1.2.2) shows. On the
other hand, if an affine scheme `X` is an `S`-prescheme, `X` is not necessarily affine over `S` (see (1.3.3) below).
Recall

<!-- original page 7 -->

however that if `S` is a _scheme_, then every `S`-prescheme that is an affine scheme is affine over `S` (`I, 5.5.10`).

**Proposition.**

<!-- label: II.1.2.4 -->

Every `S`-prescheme affine over `S` is separated over `S` (in other words, it is an `S`-scheme).

**Proof.** This follows immediately from `(I, 5.5.5)` and `(I, 5.5.8)`.

**Proposition.**

<!-- label: II.1.2.5 -->

Let `X` be an `S`-scheme affine over `S` and `f : X → S` its structure morphism. For every open `U ⊂ S`, `f⁻¹(U)` is
affine over `U`.

**Proof.** By Definition (1.2.1), we reduce to the case where `S = Spec(A)` and `X = Spec(B)` are affine, with
`f = (ᵃφ, φ̃)` and `φ : A → B` a homomorphism. Since the `D(g)` for `g ∈ A` form a basis of `S`, we reduce to
`U = D(g)`; but `f⁻¹(U) = D(φ(g))` `(I, 1.2.2.2)`, which gives the proposition.

**Proposition.**

<!-- label: II.1.2.6 -->

Let `X` be an `S`-scheme affine over `S` and `f : X → S` its structure morphism. For every quasi-coherent `𝒪_X`-module
`ℱ`, `f_*(ℱ)` is a quasi-coherent `𝒪_S`-module.

**Proof.** Given (1.2.4), this follows from `(I, 9.2.2 a)`.

In particular, the `𝒪_S`-algebra `𝒜(X) = f_*(𝒪_X)` is _quasi-coherent_.

**Proposition.**

<!-- label: II.1.2.7 -->

Let `X` be an `S`-scheme affine over `S`. For every `S`-prescheme `Y`, the map `h ↦ 𝒜(h)` from `Hom_S(Y, X)` to
`Hom(𝒜(X), 𝒜(Y))` (1.1.2) is bijective.

**Proof.** Let `f : X → S` and `g : Y → S` be the structure morphisms.

First, suppose `S = Spec(A)` and `X = Spec(B)` are affine. We must show that every homomorphism
`ω : f_*(𝒪_X) → g_*(𝒪_Y)` of `𝒪_S`-algebras arises from a unique `S`-morphism `h : Y → X` via `𝒜(h) = ω`. By definition,
for every open `U ⊂ S`, `ω` defines a homomorphism

```text
  ω_U = Γ(U, ω) : Γ(f⁻¹(U), 𝒪_X) → Γ(g⁻¹(U), 𝒪_Y)
```

of `Γ(U, 𝒪_S)`-algebras. In particular, taking `U = S`, we obtain a homomorphism `φ : Γ(X, 𝒪_X) → Γ(Y, 𝒪_Y)` of
`Γ(S, 𝒪_S)`-algebras, to which corresponds a well-defined `S`-morphism `h : Y → X` since `X` is affine `(I, 2.2.4)`. It
remains to prove `𝒜(h) = ω`, that is: for every open `U` in a basis of `S`, `ω_U` coincides with the algebra
homomorphism `φ_U` corresponding to the restriction `g⁻¹(U) → f⁻¹(U)` of `h`. We may take `U = D(λ)` with `λ ∈ S`; then
if `f = (ᵃρ, ρ̃)` with `ρ : A → B` a ring homomorphism, `f⁻¹(U) = D(μ)` for `μ = ρ(λ)`, and `Γ(f⁻¹(U), 𝒪_X)` is the ring
of fractions `B_μ`. The diagram

```text
   B ──────φ─────→ Γ(Y, 𝒪_Y)
   │                  │
   ↓                  ↓
   B_μ ────φ_U───→ Γ(g⁻¹(U), 𝒪_Y)
```

commutes, and so does the analogous diagram with `φ_U` replaced by `ω_U`; the equality `φ_U = ω_U` then follows from the
universal property of rings of fractions `(0, 1.2.4)`.

For the general case, let `(S_α)` be a covering of `S` by affine opens

<!-- original page 8 -->

such that the `f⁻¹(S_α)` are affine. Every homomorphism `ω : 𝒜(X) → 𝒜(Y)` of `𝒪_S`-algebras restricts to a family of
homomorphisms

```text
  ω_α : 𝒜(f⁻¹(S_α)) → 𝒜(g⁻¹(S_α))
```

of `𝒪_{S_α}`-algebras, hence to a family of `S_α`-morphisms `h_α : g⁻¹(S_α) → f⁻¹(S_α)` by the affine case above. We
need only check that on every affine open `U` in a basis of `S_α ∩ S_β`, the restrictions of `h_α` and `h_β` to `g⁻¹(U)`
agree, which is evident since both correspond to the restriction `𝒜(X)|U → 𝒜(Y)|U` of `ω`.

**Corollary.**

<!-- label: II.1.2.8 -->

Let `X`, `Y` be two `S`-schemes affine over `S`. An `S`-morphism `h : Y → X` is an isomorphism if and only if
`𝒜(h) : 𝒜(X) → 𝒜(Y)` is one.

**Proof.** Immediate from (1.2.7) and the functoriality of `𝒜(X)`.

## 1.3. Affine prescheme over `S` associated to an `𝒪_S`-algebra

**Proposition.**

<!-- label: II.1.3.1 -->

Let `S` be a prescheme. For every quasi-coherent `𝒪_S`-algebra `ℬ`, there exists a prescheme `X` affine over `S`,
defined up to unique `S`-isomorphism, such that `𝒜(X) = ℬ`.

**Proof.** Uniqueness follows from (1.2.8); we prove existence. For every affine open `U ⊂ S`, set
`X_U = Spec(Γ(U, ℬ))`; since `Γ(U, ℬ)` is a `Γ(U, 𝒪_S)`-algebra, `X_U` is an `S`-prescheme `(I, 1.6.1)`. As `ℬ` is
quasi-coherent, the `𝒪_S`-algebra `𝒜(X_U)` is canonically identified with `ℬ|U` (`I, 1.3.7`, `1.3.13`, `1.6.3`). For a
second affine open `V ⊂ S`, let `X_{U,V}` be the prescheme induced by `X_U` on `f_U⁻¹(U ∩ V)`, where `f_U : X_U → S` is
the structure morphism; then `X_{U,V}` and `X_{V,U}` are affine over `U ∩ V` (1.2.5), and by definition `𝒜(X_{U,V})` and
`𝒜(X_{V,U})` both identify canonically with `ℬ|(U ∩ V)`. Hence (1.2.8) there is a canonical `S`-isomorphism
`θ_{U,V} : X_{V,U} → X_{U,V}`; furthermore, if `W` is a third affine open of `S` and `θ'_{U,V}`, `θ'_{V,W}`, `θ'_{U,W}`
are the restrictions to the inverse images of `U ∩ V ∩ W`, then `θ'_{U,V} ∘ θ'_{V,W} = θ'_{U,W}`. Consequently there
exists a prescheme `X`, a covering `(T_U)` of `X` by affine opens, and for each `U` an isomorphism `φ_U : X_U → T_U`
such that `φ_U` carries `f_U⁻¹(U ∩ V)` onto `T_U ∩ T_V` with `θ_{U,V} = φ_U⁻¹ ∘ φ_V` `(I, 2.3.1)`. The morphism
`g_U = f_U ∘ φ_U⁻¹` makes `T_U` an `S`-prescheme, and `g_U`, `g_V` coincide on `T_U ∩ T_V`, so `X` is an `S`-prescheme.
It is then clear by construction that `X` is affine over `S` and that `𝒜(T_U) = ℬ|U`, whence `𝒜(X) = ℬ`.

We say that the `S`-scheme `X` so defined is _associated to the `𝒪_S`-algebra_ `ℬ`, or is the _spectrum of `ℬ`_, and we
denote it by `Spec(ℬ)`.

**Corollary.**

<!-- label: II.1.3.2 -->

Let `X` be a prescheme affine over `S` and `f : X → S` the structure morphism. For every affine open `U ⊂ S`, the
prescheme induced on `f⁻¹(U)` is the affine scheme with ring `Γ(U, 𝒜(X))`.

<!-- original page 9 -->

**Proof.** Since by (1.2.6) and (1.3.1) we may take `X` to be associated to an `𝒪_S`-algebra, the corollary follows from
the construction of `X` in (1.3.1).

**Example.**

<!-- label: II.1.3.3 -->

Let `S` be the affine plane over a field `K` with the origin doubled `(I, 5.5.11)`; with the notation of `(I, 5.5.11)`,
`S` is the union of two affine opens `Y_1`, `Y_2`. If `f` is the open immersion `Y_1 → S`, then `f⁻¹(Y_2) = Y_1 ∩ Y_2`
is not an affine open in `Y_1` (_loc. cit._), giving an example of an affine scheme that is not affine over `S`.

**Corollary.**

<!-- label: II.1.3.4 -->

Let `S` be an affine scheme. An `S`-prescheme `X` is affine over `S` if and only if `X` is an affine scheme.

**Corollary.**

<!-- label: II.1.3.5 -->

Let `X` be a prescheme affine over a prescheme `S`, and let `Y` be an `X`-prescheme. Then `Y` is affine over `S` if and
only if `Y` is affine over `X`.

**Proof.** We reduce immediately to the case where `S` is an affine scheme, and then, by (1.3.4), so is `X`; the two
conditions both say that `Y` is an affine scheme (1.3.4).

**(1.3.6)**

<!-- label: II.1.3.6 -->

Let `X` be a prescheme affine over `S`. To give a prescheme `Y` affine _over_ `X` is, by Corollary (1.3.5), the same as
to give a prescheme `Y` affine _over_ `S` together with an `S`-morphism `g : Y → X`; in other words ((1.3.1) and
(1.2.7)), it is the same as to give a quasi-coherent `𝒪_S`-algebra `ℬ` together with a homomorphism `𝒜(X) → ℬ` of
`𝒪_S`-algebras (which may be viewed as defining on `ℬ` an `𝒜(X)`-algebra structure). If `f : X → S` is the structure
morphism, then `ℬ = f_*(g_*(𝒪_Y))`.

**Corollary.**

<!-- label: II.1.3.7 -->

Let `X` be a prescheme affine over `S`. Then `X` is of finite type over `S` if and only if the quasi-coherent
`𝒪_S`-algebra `𝒜(X)` is of finite type `(I, 9.6.2)`.

**Proof.** By definition `(I, 9.6.2)` we reduce to the case where `S` is affine; then `X` is affine `(1.3.4)`, and if
`S = Spec(A)`, `X = Spec(B)`, then `𝒜(X)` is the `𝒪_S`-algebra `B̃`. Since `Γ(S, B̃) = B`, the corollary follows from
`(I, 9.6.2)` and `(I, 6.3.3)`.

**Corollary.**

<!-- label: II.1.3.8 -->

Let `X` be a prescheme affine over `S`. Then `X` is reduced if and only if the quasi-coherent `𝒪_S`-algebra `𝒜(X)` is
reduced `(0, 4.1.4)`.

**Proof.** The question is local on `S`; by Corollary (1.3.2), the assertion follows from `(I, 5.1.1)` and `(I, 5.1.4)`.

## 1.4. Quasi-coherent sheaves on an affine prescheme over `S`

**Proposition.**

<!-- label: II.1.4.1 -->

Let `X` be a prescheme affine over `S`, `Y` an `S`-prescheme, and `ℱ` (resp. `𝒢`) a quasi-coherent `𝒪_X`-module (resp.
`𝒪_Y`-module). Then the map `(h, u) ↦ (𝒜(h), 𝒜(u))` from the set of morphisms `(Y, 𝒢) → (X, ℱ)` to the set of
di-homomorphisms `(𝒜(X), 𝒜(ℱ)) → (𝒜(Y), 𝒜(𝒢))` ((1.1.2) and (1.1.3)) is bijective.

**Proof.** The proof follows exactly the same lines as that of (1.2.7), using `(I, 2.2.5)` and `(I, 2.2.4)`; details are
left to the reader.

**Corollary.**

<!-- label: II.1.4.2 -->

If, in addition to the hypotheses of (1.4.1), `Y` is also affine over `S`, then `(h, u)` is an isomorphism if and only
if `(𝒜(h), 𝒜(u))` is a di-isomorphism.

**Proposition.**

<!-- label: II.1.4.3 -->

<!-- original page 10 -->

For every pair `(ℬ, ℳ)` consisting of a quasi-coherent `𝒪_S`-algebra `ℬ` and a quasi-coherent `ℬ`-module `ℳ` (viewed as
an `𝒪_S`-module or as a `ℬ`-module — these are equivalent `(I, 9.6.1)`), there exists a pair `(X, ℱ)` consisting of a
prescheme `X` affine over `S` and a quasi-coherent `𝒪_X`-module `ℱ` such that `𝒜(X) = ℬ` and `𝒜(ℱ) = ℳ`; this pair is
determined up to unique isomorphism.

**Proof.** Uniqueness follows from (1.4.1) and (1.4.2); existence is proved as in (1.3.1), and we again leave details to
the reader.

We denote by `ℳ̃` the `𝒪_X`-module `ℱ` so obtained, and call it _associated_ to the quasi-coherent `ℬ`-module `ℳ`. For
every affine open `U ⊂ S`, `ℱ|p⁻¹(U)` (where `p` is the structure morphism `X → S`) is canonically isomorphic to
`(Γ(U, ℳ))̃`.

**Corollary.**

<!-- label: II.1.4.4 -->

On the category of quasi-coherent `ℬ`-modules, `ℳ̃` is a covariant additive exact functor in `ℳ` that commutes with
direct limits and direct sums.

**Proof.** We reduce immediately to the case where `S` is affine; the corollary then follows from `(I, 1.3.5)`,
`(I, 1.3.9)`, and `(I, 1.3.11)`.

**Corollary.**

<!-- label: II.1.4.5 -->

Under the hypotheses of (1.4.3), `ℳ̃` is an `𝒪_X`-module of finite type if and only if `ℳ` is a `ℬ`-module of finite
type.

**Proof.** We reduce to `S = Spec(A)` affine. Then `ℬ = B̃`, where `B` is an `A`-algebra of finite type `(I, 9.6.2)`,
and `ℳ = M̃`, where `M` is a `B`-module `(I, 1.3.13)`. On the prescheme `X`, `𝒪_X` is associated to `B` and `ℳ̃` to the
`B`-module `M`; so `ℳ̃` is of finite type iff `M` is of finite type `(I, 1.3.13)`, whence the claim.

**Proposition.**

<!-- label: II.1.4.6 -->

Let `Y` be a prescheme affine over `S`, and let `X`, `X'` be two preschemes affine over `Y` (hence also over `S` by
(1.3.5)). Set `ℬ = 𝒜(Y)`, `𝒜 = 𝒜(X)`, `𝒜' = 𝒜(X')`. Then `X ×_Y X'` is affine over `Y` (and hence also over `S`), and
`𝒜(X ×_Y X')` is canonically identified with `𝒜 ⊗_ℬ 𝒜'`.

**Proof.** By `(I, 9.6.1)`, `𝒜 ⊗_ℬ 𝒜'` is a quasi-coherent `ℬ`-algebra, and thus also a quasi-coherent `𝒪_S`-algebra
`(I, 9.6.1)`. Let `Z` be the spectrum of `𝒜 ⊗_ℬ 𝒜'` (1.3.1). The canonical `ℬ`-homomorphisms `𝒜 → 𝒜 ⊗_ℬ 𝒜'` and
`𝒜' → 𝒜 ⊗_ℬ 𝒜'` correspond by (1.2.7) to `Y`-morphisms `p : Z → X` and `p' : Z → X'`. To see that `(Z, p, p')` is a
product `X ×_Y X'`, we may reduce to the case where `S` is an affine scheme with ring `C` `(I, 3.2.6.4)`. Then `Y`, `X`,
`X'` are affine schemes (1.3.4) with rings `B`, `A`, `A'` which are `C`-algebras such that `ℬ = B̃`, `𝒜 = Ã`, `𝒜' = Ã'`.
Then `(I, 1.3.13)` gives `𝒜 ⊗_ℬ 𝒜' = (A ⊗_B A')̃`, so the ring of `Z` is `A ⊗_B A'` and the morphisms `p`, `p'`
correspond to the canonical homomorphisms `A → A ⊗_B A'` and `A' → A ⊗_B A'`. The proposition follows from `(I, 3.2.2)`.

**Corollary.**

<!-- label: II.1.4.7 -->

Let `ℱ` (resp. `ℱ'`) be a quasi-coherent `𝒪_X`-module (resp. `𝒪_{X'}`-module). Then `𝒜(ℱ ⊗_Y ℱ')` is canonically
identified with `𝒜(ℱ) ⊗_{𝒜(Y)} 𝒜(ℱ')`.

**Proof.** We know `(I, 9.1.2)` that `ℱ ⊗_Y ℱ'` is quasi-coherent on `X ×_Y X'`. Let `g : Y → S`, `f : X → Y`,
`f' : X' → Y` be the structure morphisms, so that the structure morphism

<!-- original page 11 -->

`h : Z → S` equals `g ∘ f ∘ p = g ∘ f' ∘ p'`. We define a canonical homomorphism

```text
  𝒜(ℱ) ⊗_{𝒜(Y)} 𝒜(ℱ') → 𝒜(ℱ ⊗_Y ℱ')
```

as follows: for every open `U ⊂ S`, the canonical homomorphisms `Γ(f⁻¹(g⁻¹(U)), ℱ) → Γ(h⁻¹(U), p*(ℱ))` and
`Γ(f'⁻¹(g⁻¹(U)), ℱ') → Γ(h⁻¹(U), p'*(ℱ'))` `(0, 4.4.3)` give a canonical homomorphism

```text
  Γ(f⁻¹(g⁻¹(U)), ℱ) ⊗_{Γ(g⁻¹(U), 𝒪_Y)} Γ(f'⁻¹(g⁻¹(U)), ℱ')
    → Γ(h⁻¹(U), p*(ℱ)) ⊗_{Γ(h⁻¹(U), 𝒪_Z)} Γ(h⁻¹(U), p'*(ℱ')).
```

To see this is an isomorphism of `𝒜(Z)`-modules, we reduce to the affine case: `S` (and hence `X`, `X'`, `Y`,
`X ×_Y X'`) affine, and (with the notation of (1.4.6)) `ℱ = M̃`, `ℱ' = M̃'` with `M` an `A`-module and `M'` an
`A'`-module. Then `ℱ ⊗_Y ℱ'` identifies with the sheaf on `X ×_Y X'` associated to the `(A ⊗_B A')`-module `M ⊗_B M'`
`(I, 9.1.3)`, and the corollary follows from the canonical identification of `𝒪_S`-modules `(M ⊗_B M')̃` and
`M̃ ⊗_{B̃} M̃'` (where `M`, `M'`, `B` are viewed as `C`-modules) (`I, 1.3.13` and `1.6.3`).

Applying (1.4.7) in the special case `X = Y`, `ℱ' = 𝒪_{X'}`, we see that the `𝒜'`-module `𝒜(f'*(ℱ))` identifies with
`𝒜(ℱ) ⊗_ℬ 𝒜'`.

**(1.4.8)**

<!-- label: II.1.4.8 -->

In particular, when `X = X' = Y` (with `X` affine over `S`), for any two quasi-coherent `𝒪_X`-modules `ℱ`, `𝒢`,

```text
  𝒜(ℱ ⊗_{𝒪_X} 𝒢) = 𝒜(ℱ) ⊗_{𝒜(X)} 𝒜(𝒢)                                    (1.4.8.1)
```

up to canonical functorial isomorphism. If furthermore `ℱ` admits a finite presentation, then `(I, 1.6.3)` and
`(I, 1.3.12)` give

```text
  𝒜(𝓗𝓸𝓶_X(ℱ, 𝒢)) = 𝓗𝓸𝓶_{𝒜(X)}(𝒜(ℱ), 𝒜(𝒢))                                  (1.4.8.2)
```

up to canonical isomorphism.

**Remark.**

<!-- label: II.1.4.9 -->

If `X`, `X'` are two preschemes affine over `S`, then the disjoint sum `X ⊔ X'` is also affine over `S`, since the sum
of two affine schemes is affine.

**Proposition.**

<!-- label: II.1.4.10 -->

Let `S` be a prescheme, `ℬ` a quasi-coherent `𝒪_S`-algebra, and `X = Spec(ℬ)`. For every quasi-coherent sheaf of ideals
`𝒥` of `ℬ`, `𝒥̃` is a quasi-coherent sheaf of ideals of `𝒪_X`, and the closed subprescheme `Y` of `X` it defines is
canonically isomorphic to `Spec(ℬ/𝒥)`.

**Proof.** By `(I, 4.2.3)`, `Y` is affine over `S`; by (1.3.1) we reduce to `S` affine, and the assertion is then
`(I, 4.1.2)`.

The conclusion of (1.4.10) can be restated: if `h : ℬ → ℬ'` is a _surjective_ homomorphism of quasi-coherent
`𝒪_S`-algebras, then `Spec(h) : Spec(ℬ') → Spec(ℬ)` is a _closed immersion_.

**Proposition.**

<!-- label: II.1.4.11 -->

<!-- original page 12 -->

Let `S` be a prescheme, `ℬ` a quasi-coherent `𝒪_S`-algebra, and `X = Spec(ℬ)`. For every quasi-coherent sheaf of ideals
`𝒦` of `𝒪_S` (denoting by `f : X → S` the structure morphism), `f*(𝒦)𝒪_X = (𝒦ℬ)̃` up to canonical isomorphism.

**Proof.** The question is local on `S`, so we reduce to `S = Spec(A)` affine, where the assertion is just `(I, 1.6.9)`.

## 1.5. Change of base prescheme

**Proposition.**

<!-- label: II.1.5.1 -->

Let `X` be a prescheme affine over `S`. For every base change `g : S' → S`, `X' = X_{(S')} = X ×_S S'` is affine over
`S'`.

**Proof.** If `f' : X' → S'` is the projection, it suffices to prove that `f'⁻¹(U')` is an affine open for every affine
open `U' ⊂ S'` such that `g(U')` is contained in an affine open `U ⊂ S` (1.2.1). We may thus assume `S` and `S'` are
affine; it then suffices to show `X'` is affine (1.3.4). But then `X` is affine, and if `A`, `A'`, `B` are the rings of
`S`, `S'`, `X`, then `X'` is the affine scheme with ring `A' ⊗_A B` `(I, 3.2.2)`.

**Corollary.**

<!-- label: II.1.5.2 -->

Under the hypotheses of (1.5.1), let `f : X → S` be the structure morphism and `f' : X' → S'`, `g' : X' → X` the
projections, so that the diagram

```text
   X ←─g'── X'
   │        │
 f │        │ f'
   ↓        ↓
   S ←──g── S'
```

is commutative. For every quasi-coherent `𝒪_X`-module `ℱ`, there is a canonical isomorphism of `𝒪_{S'}`-modules

```text
  u : g*(f_*(ℱ)) ⥲ f'_*(g'*(ℱ)).                                          (1.5.2.1)
```

In particular, there is a canonical isomorphism from `𝒜(X')` to `g*(𝒜(X))`.

**Proof.** To define `u`, it suffices to define a homomorphism

```text
  v : f_*(ℱ) → g_*(f'_*(g'*(ℱ))) = f_*(g'_*(g'*(ℱ)))
```

and set `u = v♯` `(0, 4.4.3)`. Take `v = f_*(ρ)` with `ρ : ℱ → g'_*(g'*(ℱ))` the canonical homomorphism `(0, 4.4.3)`. To
prove that `u` is an isomorphism, we may assume `S`, `S'` (hence `X`, `X'`) are affine. With the notation of (1.5.1),
`ℱ = M̃` for a `B`-module `M`, and one checks that both `g*(f_*(ℱ))` and `f'_*(g'*(ℱ))` equal the `𝒪_{S'}`-module
associated to the `A'`-module `A' ⊗_A M` (with `M` viewed as an `A`-module), and that `u` corresponds to the identity
(`I, 1.6.3`, `1.6.5`, `1.6.7`).

**Remark.**

<!-- label: II.1.5.3 -->

One should _not_ expect (1.5.2) to remain valid when `X` is no longer affine over `S` — not even when `S' = Spec(κ(s))`
for `s ∈ S` with `S' → S` the canonical morphism `(I, 2.4.5)`, in which case `X'` is just the _fibre_ `f⁻¹(s)`
`(I, 3.6.2)`. In other words, when `X` is not affine over `S`, the operation

<!-- original page 13 -->

"direct image of quasi-coherent sheaves" does not commute with the operation "passage to fibres". We will see however in
Chapter III `(III, 4.2.4)` a result in this direction, of an "asymptotic" character, valid for _coherent_ sheaves on `X`
when `f` is proper (5.4) and `S` is Noetherian.

**Corollary.**

<!-- label: II.1.5.4 -->

For every prescheme `X` affine over `S` and every `s ∈ S`, the fibre `f⁻¹(s)` (where `f : X → S` is the structure
morphism) is an affine scheme.

**Proof.** Apply (1.5.1) with `S' = Spec(κ(s))` and use (1.3.4).

**Corollary.**

<!-- label: II.1.5.5 -->

Let `X` be an `S`-prescheme and `S'` a prescheme affine over `S`. Then `X' = X_{(S')}` is a prescheme affine over `X`.
Furthermore, if `f : X → S` is the structure morphism, there is a canonical isomorphism of `𝒪_X`-algebras
`𝒜(X') ⥲ f*(𝒜(S'))`, and for every quasi-coherent `𝒜(S')`-module `ℳ` a canonical di-isomorphism `f*(ℳ) ⥲ 𝒜(f'*(ℳ̃))`,
where `f' = f_{(S')} : X' → S'` is the structure morphism.

**Proof.** Swap the roles of `X` and `S'` in (1.5.1) and (1.5.2).

**(1.5.6)**

<!-- label: II.1.5.6 -->

Now let `S`, `S'` be two preschemes, `q : S' → S` a morphism, `ℬ` (resp. `ℬ'`) a quasi-coherent `𝒪_S`-algebra (resp.
`𝒪_{S'}`-algebra), and `u : ℬ → ℬ'` a `q`-morphism — that is, a homomorphism `ℬ → q_*(ℬ')` of `𝒪_S`-algebras. If
`X = Spec(ℬ)` and `X' = Spec(ℬ')`, we obtain canonically a morphism

```text
  v = Spec(u) : X' → X
```

such that the diagram

```text
   X' ──v──→ X
   │         │                                                            (1.5.6.1)
   ↓         ↓
   S' ──q──→ S
```

commutes (the vertical arrows being the structure morphisms). Indeed, the datum of `u` is equivalent to that of a
homomorphism `u♯ : q*(ℬ) → ℬ'` of quasi-coherent `𝒪_{S'}`-algebras `(0, 4.4.3)`, which canonically defines an
`S'`-morphism

```text
  w : Spec(ℬ') → Spec(q*(ℬ))
```

with `𝒜(w) = u♯` (1.2.7). On the other hand, (1.5.2) gives a canonical identification `Spec(q*(ℬ)) ≅ X ×_S S'`, and `v`
is the composition `X' ─w→ X ×_S S' ─pr₁→ X`; the commutativity of (1.5.6.1) follows from the definitions. Let `U`
(resp. `U'`) be an affine open of `S` (resp. `S'`) with `q(U') ⊂ U`, with rings `A = Γ(U, 𝒪_S)`, `A' = Γ(U', 𝒪_{S'})`,
and `B = Γ(U, ℬ)`, `B' = Γ(U', ℬ')`. The restriction of `u` to a `(q|U')`-morphism `ℬ|U → ℬ'|U'` corresponds to a
di-homomorphism of algebras `B → B'`; if `V`, `V'` are the inverse images of `U`, `U'` in `X`, `X'` under the structure
morphisms, the morphism `V' → V` (the restriction of `v`) corresponds `(I, 1.7.3)` to this di-homomorphism.

**(1.5.7)**

<!-- label: II.1.5.7 -->

Under the same hypotheses as (1.5.6), let `ℳ` be a quasi-coherent `ℬ`-module. There is then a canonical isomorphism of
`𝒪_{X'}`-modules

```text
  v*(ℳ̃) ⥲ (q*(ℳ) ⊗_{q*(ℬ)} ℬ')̃.                                          (1.5.7.1)
```

<!-- original page 14 -->

Indeed, the canonical isomorphism (1.5.2.1) gives a canonical identification of `pr₁*(ℳ̃)` with the sheaf on
`Spec(q*(ℬ))` associated to the `q*(ℬ)`-module `q*(ℳ)`, and one applies (1.4.7).

## 1.6. Affine morphisms

**(1.6.1)**

<!-- label: II.1.6.1 -->

We say that a morphism `f : X → Y` of preschemes is _affine_ if it makes `X` an affine prescheme over `Y`. The
properties of preschemes affine over another translate as follows in this language:

**Proposition.**

<!-- label: II.1.6.2 -->

1. A closed immersion is affine.
1. The composition of two affine morphisms is affine.
1. If `f : X → Y` is an affine `S`-morphism, then `f_{(S')} : X_{(S')} → Y_{(S')}` is affine for every base change
    `S' → S`.
1. If `f : X → Y` and `f' : X' → Y'` are two affine `S`-morphisms, then `f ×_S f' : X ×_S X' → Y ×_S Y'` is affine.
1. If `f : X → Y` and `g : Y → Z` are two morphisms such that `g ∘ f` is affine and `g` is separated, then `f` is
    affine.
1. If `f` is affine, so is `f_red`.

**Proof.** By `(I, 5.5.12)`, it suffices to prove (i), (ii), (iii). But (i) is just Example (1.2.2), (ii) is just
Corollary (1.3.5), and (iii) follows from (1.5.1) since `X_{(S')}` identifies with `X ×_Y Y_{(S')}` `(I, 3.3.11)`.

**Corollary.**

<!-- label: II.1.6.3 -->

If `X` is an affine scheme and `Y` is a scheme, then every morphism `f : X → Y` is affine.

**Proposition.**

<!-- label: II.1.6.4 -->

Let `Y` be a locally Noetherian prescheme and `f : X → Y` a morphism of finite type. Then `f` is affine if and only if
`f_red` is.

**Proof.** By (1.6.2)(vi), it suffices to prove sufficiency. We may suppose `Y` affine and Noetherian, and must show `X`
is affine; then `Y_red` is affine, so by hypothesis `X_red` is affine. Since `X` is Noetherian, the conclusion follows
from `(I, 6.1.7)`.

## 1.7. Vector bundle associated to a sheaf of modules

**(1.7.1)**

<!-- label: II.1.7.1 -->

Let `A` be a ring and `E` an `A`-module. Recall that the _symmetric algebra_ on `E`, denoted `𝕊(E)` (or `𝕊_A(E)`), is
the quotient of the tensor algebra `𝕋(E)` by the two-sided ideal generated by `x ⊗ y − y ⊗ x` for `x, y ∈ E`. The
algebra `𝕊(E)` is characterized by the following universal property: if `σ : E → 𝕊(E)` is the canonical map (obtained by
composing `E → 𝕋(E)` with `𝕋(E) → 𝕊(E)`), then every `A`-linear map `E → B` with `B` a _commutative_ `A`-algebra factors
uniquely as `E ─σ→ 𝕊(E) ─g→ B`, where `g` is an `A`-homomorphism _of algebras_. From this characterization, for two
`A`-modules `E`, `F`,

```text
  𝕊(E ⊕ F) = 𝕊(E) ⊗ 𝕊(F)
```

<!-- original page 15 -->

up to canonical isomorphism. Furthermore, `𝕊(E)` is a covariant functor in `E` from `A`-modules to commutative
`A`-algebras, and if `E = lim_→ E_λ`, then `𝕊(E) = lim_→ 𝕊(E_λ)` up to canonical isomorphism. By abuse of notation, a
product `σ(x_1)σ(x_2) ⋯ σ(x_n)` with `x_i ∈ E` is often written `x_1 x_2 ⋯ x_n` when no confusion can arise. The algebra
`𝕊(E)` is _graded_, with `𝕊_n(E)` the set of linear combinations of products of `n` elements of `E` (`n ≥ 0`); `𝕊(A)` is
canonically isomorphic to the polynomial algebra `A[T]` in one indeterminate, and `𝕊(Aⁿ)` to `A[T_1, …, T_n]`.

**(1.7.2)**

<!-- label: II.1.7.2 -->

Let `φ : A → B` be a ring homomorphism. If `F` is a `B`-module, the canonical map `F → 𝕊(F)` gives a canonical map
`F_{[φ]} → 𝕊(F)_{[φ]}`, which factors as `F_{[φ]} → 𝕊(F_{[φ]}) → 𝕊(F)_{[φ]}`; the canonical homomorphism
`𝕊(F_{[φ]}) → 𝕊(F)_{[φ]}` is surjective but not in general bijective. If `E` is an `A`-module, every di-homomorphism
`E → F` (that is, every `A`-homomorphism `E → F_{[φ]}`) yields canonically an `A`-homomorphism of algebras
`𝕊(E) → 𝕊(F_{[φ]}) → 𝕊(F)_{[φ]}`, i.e. a di-homomorphism of algebras `𝕊(E) → 𝕊(F)`.

With the same notation, for every `A`-module `E`, `𝕊(E ⊗_A B)` is canonically isomorphic to `𝕊(E) ⊗_A B`; this follows
immediately from the universal property of `𝕊(E)` (1.7.1).

**(1.7.3)**

<!-- label: II.1.7.3 -->

Let `R` be a multiplicative subset of `A`. Applying (1.7.2) with `B = R⁻¹A` and recalling that `R⁻¹E = E ⊗_A R⁻¹A`, we
get `𝕊(R⁻¹E) = R⁻¹𝕊(E)` up to canonical isomorphism. If `R' ⊃ R` is a second multiplicative subset, the diagram

```text
   R⁻¹E ─────→ R'⁻¹E
     │           │
     ↓           ↓
   𝕊(R⁻¹E) → 𝕊(R'⁻¹E)
```

commutes.

**(1.7.4)**

<!-- label: II.1.7.4 -->

Now let `(S, 𝒜)` be a ringed space and `ℰ` an `𝒜`-module on `S`. Associating to every open `U ⊂ S` the `Γ(U, 𝒜)`-module
`𝕊(Γ(U, ℰ))` defines (by the functoriality of `𝕊(E)` (1.7.2)) a presheaf of algebras; we call the associated sheaf,
denoted `𝕊(ℰ)` or `𝕊_𝒜(ℰ)`, the _symmetric `𝒜`-algebra on the `𝒜`-module `ℰ`_. By (1.7.1) `𝕊(ℰ)` is the solution of a
universal problem: every homomorphism of `𝒜`-modules `ℰ → ℬ` with `ℬ` an `𝒜`-algebra factors uniquely as `ℰ → 𝕊(ℰ) → ℬ`,
the second arrow being a homomorphism of `𝒜`-algebras. There is thus a bijective correspondence between homomorphisms
`ℰ → ℬ` of `𝒜`-modules and homomorphisms `𝕊(ℰ) → ℬ` of `𝒜`-algebras. In particular, every homomorphism `u : ℰ → ℱ` of
`𝒜`-modules defines a homomorphism `𝕊(u) : 𝕊(ℰ) → 𝕊(ℱ)` of `𝒜`-algebras, and `𝕊(ℰ)` is a covariant functor in `ℰ`.

<!-- original page 16 -->

By (1.7.2) and the commutation of `𝕊` with direct limits, `(𝕊(ℰ))_s = 𝕊(ℰ_s)` for every `s ∈ S`. For two `𝒜`-modules
`ℰ`, `ℱ`, `𝕊(ℰ ⊕ ℱ)` identifies canonically with `𝕊(ℰ) ⊗_𝒜 𝕊(ℱ)`, as one sees on presheaves.

We also note that `𝕊(ℰ)` is a graded `𝒜`-algebra — the infinite direct sum of the `𝕊_n(ℰ)`, where `𝕊_n(ℰ)` is the sheaf
associated to the presheaf `U ↦ 𝕊_n(Γ(U, ℰ))`. In particular `𝕊_𝒜(𝒜)` identifies with `𝒜[T] = 𝒜 ⊗_ℤ ℤ[T]` (`T` an
indeterminate, `ℤ` viewed as a constant sheaf).

**(1.7.5)**

<!-- label: II.1.7.5 -->

Let `(T, ℬ)` be a second ringed space and `f : (S, 𝒜) → (T, ℬ)` a morphism. For `ℱ` a `ℬ`-module, `𝕊(f*(ℱ))` identifies
canonically with `f*(𝕊(ℱ))`: with `f = (ψ, θ)` and by definition `(0, 4.3.1)`,

```text
  𝕊(f*(ℱ)) = 𝕊(ψ*(ℱ) ⊗_{ψ*(ℬ)} 𝒜) = 𝕊(ψ*(ℱ)) ⊗_{ψ*(ℬ)} 𝒜
```

by (1.7.2). For every open `U ⊂ S` and every section `h` of `𝕊(ψ*(ℱ))` over `U`, `h` agrees in a neighbourhood `V` of
every `s ∈ U` with an element of `𝕊(Γ(V, ψ*(ℱ)))`; unfolding the definition of `ψ*(ℱ)` `(0, 3.7.1)` and using that every
element of `𝕊(E)` is a linear combination of finitely many products of elements of `E`, one finds a neighbourhood `W` of
`ψ(s)` in `T`, a section `h'` of `𝕊(ℱ)` over `W`, and a neighbourhood `V' ⊂ V ∩ ψ⁻¹(W)` of `s` such that `h` agrees with
`t ↦ h'(ψ(t))` on `V'`; whence the assertion.

**Proposition.**

<!-- label: II.1.7.6 -->

Let `A` be a ring, `S = Spec(A)` its prime spectrum, and `ℰ = M̃` the `𝒪_S`-module associated to an `A`-module `M`. Then
the `𝒪_S`-algebra `𝕊(ℰ)` is associated to the `A`-algebra `𝕊(M)`.

**Proof.** For every `f ∈ A`, `𝕊(M_f) = (𝕊(M))_f` (1.7.3), so the proposition follows from `(I, 1.3.4)`.

**Corollary.**

<!-- label: II.1.7.7 -->

If `S` is a prescheme and `ℰ` a quasi-coherent `𝒪_S`-module, then the `𝒪_S`-algebra `𝕊(ℰ)` is quasi-coherent. If
furthermore `ℰ` is of finite type, then each `𝕊_n(ℰ)` is an `𝒪_S`-module of finite type.

**Proof.** The first assertion is immediate from (1.7.6) and `(I, 1.4.1)`. The second follows because for an `A`-module
`E` of finite type, `𝕊_n(E)` is also of finite type; apply `(I, 1.3.13)`.

**Definition.**

<!-- label: II.1.7.8 -->

Let `ℰ` be a quasi-coherent `𝒪_S`-module. We call the _vector bundle over `S` defined by `ℰ`_, denoted `𝕍(ℰ)`, the
spectrum (1.3.1) of the quasi-coherent `𝒪_S`-algebra `𝕊(ℰ)`.

By (1.2.7), for every `S`-prescheme `X` there is a canonical bijective correspondence between the `S`-morphisms
`X → 𝕍(ℰ)` and the homomorphisms `𝕊(ℰ) → 𝒜(X)` of `𝒪_S`-algebras, hence also between these `S`-morphisms and the
homomorphisms `ℰ → 𝒜(X) = f_*(𝒪_X)` of `𝒪_S`-modules (where `f` is the structure morphism `X → S`). In particular:

**(1.7.9)**

<!-- label: II.1.7.9 -->

Take `X` to be the subprescheme induced by `S` on an _open_ `U ⊂ S`. Then the `S`-morphisms `U → 𝕍(ℰ)` are just the
`U`-sections `(I, 2.5.5)` of the `U`-prescheme induced by `𝕍(ℰ)` on `p⁻¹(U)` (with `p : 𝕍(ℰ) → S` the structure
morphism). By the above, these `U`-sections correspond bijectively to homomorphisms of `𝒪_S`-modules `ℰ → j_*(𝒪_S|U)`
(with `j : U → S` the canonical injection), or

<!-- original page 17 -->

equivalently `(0, 4.4.3)` to `(𝒪_S|U)`-homomorphisms `j*(ℰ) = ℰ|U → 𝒪_S|U`. It is immediate that restriction to an open
`U' ⊂ U` of an `S`-morphism `U → 𝕍(ℰ)` corresponds to the restriction to `U'` of the corresponding homomorphism
`ℰ|U → 𝒪_S|U`. We conclude that _the sheaf of germs of `S`-sections_ of `𝕍(ℰ)` is canonically identified with the _dual_
`ℰ̌` of `ℰ`.

In particular, taking `X = U = S`, the _zero_ homomorphism `ℰ → 𝒪_S` corresponds to a canonical `S`-section of `𝕍(ℰ)`,
called the _zero `S`-section_ (cf. (8.3.3)).

**(1.7.10)**

<!-- label: II.1.7.10 -->

Now take `X` to be the spectrum `{ξ}` of a field `K`; the structure morphism `f : X → S` corresponds to a monomorphism
`κ(s) → K` with `s = f(ξ)` `(I, 2.4.6)`. The `S`-morphisms `{ξ} → 𝕍(ℰ)` are then just the _geometric points of `𝕍(ℰ)`
with values in the extension `K` of `κ(s)`_ `(I, 3.4.5)`, points localized over `p⁻¹(s)`. The set of these points —
which we call the _rational geometric fibre over `K`_ of `𝕍(ℰ)` over `s` — identifies, by (1.7.8), with
`Hom_{𝒪_S}(ℰ, f_*(𝒪_X))`, or equivalently `(0, 4.4.3)` with `Hom_{𝒪_X}(f*(ℰ), 𝒪_X = K)`. By definition `(0, 4.3.1)`
`f*(ℰ) = ℰ_s ⊗_{𝒪_s} K = ℰ^s ⊗_{κ(s)} K` with `ℰ^s = ℰ_s/𝔪_s ℰ_s`; so the rational geometric fibre of `𝕍(ℰ)` over `s`
with values in `K` identifies with the _dual_ of the `K`-vector space `ℰ^s ⊗_{κ(s)} K`. If `ℰ^s` or `K` is
finite-dimensional over `κ(s)`, this dual identifies further with `(ℰ^s)̌ ⊗_{κ(s)} K`, where `(ℰ^s)̌` denotes the dual
of the `κ(s)`-vector space `ℰ^s`.

**Proposition.**

<!-- label: II.1.7.11 -->

1. `𝕍(ℰ)` is a contravariant functor in `ℰ` from quasi-coherent `𝒪_S`-modules to affine `S`-schemes.
1. If `ℰ` is an `𝒪_S`-module of finite type, then `𝕍(ℰ)` is of finite type over `S`.
1. If `ℰ` and `ℱ` are two quasi-coherent `𝒪_S`-modules, then `𝕍(ℰ ⊕ ℱ)` identifies canonically with `𝕍(ℰ) ×_S 𝕍(ℱ)`.
1. For a morphism `g : S' → S` and any quasi-coherent `𝒪_S`-module `ℰ`, `𝕍(g*(ℰ))` identifies canonically with
    `𝕍(ℰ)_{(S')} = 𝕍(ℰ) ×_S S'`.
1. A surjective homomorphism `ℰ → ℱ` of quasi-coherent `𝒪_S`-modules corresponds to a closed immersion `𝕍(ℱ) → 𝕍(ℰ)`.

**Proof.** (i) is immediate from (1.2.7), given that every homomorphism `ℰ → ℱ` of `𝒪_S`-modules canonically defines a
homomorphism `𝕊(ℰ) → 𝕊(ℱ)` of `𝒪_S`-algebras. (ii) follows immediately from `(I, 6.3.1)` and the fact that for an
`A`-module `E` of finite type, `𝕊(E)` is an `A`-algebra of finite type. For (iii), start from the canonical isomorphism
`𝕊(ℰ ⊕ ℱ) ⥲ 𝕊(ℰ) ⊗_{𝒪_S} 𝕊(ℱ)` (1.7.4) and apply (1.4.6). Similarly, for (iv), start from `𝕊(g*(ℰ)) ⥲ g*(𝕊(ℰ))` (1.7.5)
and apply (1.5.2). Finally, for (v), surjectivity of `ℰ → ℱ` implies surjectivity of the corresponding homomorphism
`𝕊(ℰ) → 𝕊(ℱ)` of `𝒪_S`-algebras, and the conclusion follows from (1.4.10).

**(1.7.12)**

<!-- label: II.1.7.12 -->

Taking `ℰ = 𝒪_S` in particular, the prescheme `𝕍(𝒪_S)` is the affine `S`-scheme which is the spectrum of the
`𝒪_S`-algebra `𝕊(𝒪_S)`, and the latter identifies with the `𝒪_S`-algebra `𝒪_S[T] = 𝒪_S ⊗_ℤ ℤ[T]`

<!-- original page 18 -->

(`T` an indeterminate). This is evident when `S = Spec(ℤ)`, by (1.7.6), and the general case follows by considering the
structure morphism `S → Spec(ℤ)` and using (1.7.11)(iv). We therefore write `𝕍(𝒪_S) = S[T]`, and we have

```text
  S[T] = S ⊗_ℤ ℤ[T].                                                      (1.7.12.1)
```

The identification of the sheaf of germs of `S`-sections of `S[T]` with `𝒪_S`, already seen in `(I, 3.3.15)`, reappears
here in a more general context, as a special case of (1.7.9).

**(1.7.13)**

<!-- label: II.1.7.13 -->

For every `S`-prescheme `X`, we have seen (1.7.8) that `Hom_S(X, S[T])` is canonically identified with
`Hom_{𝒪_S}(𝒪_S, 𝒜(X))`, which is canonically isomorphic to `Γ(S, 𝒜(X))` and so carries a ring structure. To every
`S`-morphism `h : X → Y` corresponds a morphism `Γ(𝒜(h)) : Γ(S, 𝒜(Y)) → Γ(S, 𝒜(X))` for these ring structures (1.1.2).
Equipped with this ring structure, `Hom_S(X, S[T])` becomes a _contravariant functor_ in `X` from the category of
`S`-preschemes to rings. On the other hand, `Hom_S(X, 𝕍(ℰ))` identifies likewise with `Hom_{𝒪_S}(ℰ, 𝒜(X))` (with `𝒜(X)`
viewed as an _`𝒪_S`-module_); it is therefore canonically endowed with a module structure over the ring
`Hom_S(X, S[T])`, and the pair

```text
  (Hom_S(X, S[T]), Hom_S(X, 𝕍(ℰ)))
```

is a contravariant functor in `X` with values in the category whose objects are pairs `(A, M)` with `A` a ring and `M`
an `A`-module, the morphisms being di-homomorphisms.

We interpret this by saying that `S[T]` is an _`S`-scheme of rings_ and that `𝕍(ℰ)` is an _`S`-scheme of modules_ over
the `S`-scheme of rings `S[T]` (cf. Chapter 0, §8).

**(1.7.14)**

<!-- label: II.1.7.14 -->

We shall see that the `S`-scheme-of-modules structure on `𝕍(ℰ)` reconstructs `ℰ` up to unique isomorphism: we show that
`ℰ` is canonically isomorphic to an `𝒪_S`-submodule of `𝕊(ℰ) = 𝒜(𝕍(ℰ))` defined by means of that structure. Indeed
(1.7.4), the set `Hom_{𝒪_S}(𝕊(ℰ), 𝒜(X))` of homomorphisms of _`𝒪_S`-algebras_ identifies canonically with
`Hom_{𝒪_S}(ℰ, 𝒜(X))`, the set of homomorphisms of _`𝒪_S`-modules_: if `h`, `h'` are two elements of the latter set,
`s_i` (`1 ≤ i ≤ n`) sections of `ℰ` over an open `U ⊂ S`, and `t` a section of `𝒜(X)` over `U`, then by definition

```text
  (h + h')(s_1 s_2 ⋯ s_n) = ∏_{i=1}^n (h(s_i) + h'(s_i))
```

and

```text
  (t · h)(s_1 s_2 ⋯ s_n) = tⁿ ∏_{i=1}^n h(s_i).
```

Given this, if `z` is a section of `𝕊(ℰ)` over `U`, then `h ↦ h(z)` is a map from
`Hom_S(X, 𝕍(ℰ)) = Hom_{𝒪_S}(𝕊(ℰ), 𝒜(X))` to `Γ(U, 𝒜(X))`. We will

<!-- original page 19 -->

show that `ℰ` is identified with the `𝒪_S`-submodule of `𝕊(ℰ)` such that, _for every open `U ⊂ S`, every section `z` of
this submodule over `U`, and every `S`-prescheme `X`, the map `h ↦ h(z)` from `Hom_{𝒪_S|U}(𝕊(ℰ)|U, 𝒜(X)|U)` to
`Γ(U, 𝒜(X))` is a homomorphism of `Γ(U, 𝒜(X))`-modules_.

It is immediate that `ℰ` has this property; for the converse, we reduce to proving that when `S = Spec(A)` and `ℰ = M̃`,
a section `z` of `𝕊(ℰ)` over `S` (for `U = S`) satisfying the stated property must be a section of `ℰ`. Write
`z = ∑_{n=0}^∞ z_n` with `z_n ∈ 𝕊_n(M)`; we must show `z_n = 0` for `n ≠ 1`. Set `B = 𝕊(M)` and take `X = Spec(B[T])`
for an indeterminate `T`. Then `Hom_{𝒪_S}(𝕊(ℰ), 𝒜(X))` identifies with the set of ring homomorphisms `h : B → B[T]`
`(I, 1.3.13)`, and by the calculation above `(T · h)(z) = ∑_{n=0}^∞ Tⁿ h(z_n)`; the hypothesis on `z` gives
`∑_{n=0}^∞ Tⁿ h(z_n) = T · ∑_{n=0}^∞ h(z_n)` for every `h`. Taking `h` to be the canonical injection yields
`∑_{n=0}^∞ Tⁿ z_n = T · ∑_{n=0}^∞ z_n`, which forces `z_n = 0` for `n ≠ 1`.

**Proposition.**

<!-- label: II.1.7.15 -->

Let `Y` be a prescheme whose underlying space is Noetherian, or a quasi-compact scheme. Every affine `Y`-scheme `X` of
finite type over `Y` is `Y`-isomorphic to a closed `Y`-subscheme of a `Y`-scheme of the form `𝕍(ℰ)`, where `ℰ` is a
quasi-coherent `𝒪_Y`-module of finite type.

**Proof.** The quasi-coherent `𝒪_Y`-algebra `𝒜(X)` is of finite type (1.3.7). The hypotheses imply `𝒜(X)` is generated
by a quasi-coherent `𝒪_Y`-submodule `ℰ` of finite type `(I, 9.6.5)`; by definition, the canonical homomorphism
`𝕊(ℰ) → 𝒜(X)` extending the injection `ℰ → 𝒜(X)` is _surjective_. The conclusion follows from (1.4.10).

