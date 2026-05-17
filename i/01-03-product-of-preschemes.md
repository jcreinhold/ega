# Chapter I — The Language of Schemes

## §3. Product of Preschemes

<!-- label: I.3 -->

> **Translation status.** This section is a translation skeleton: subsection headings and the principal definitions and
> statements are translated; longer proofs are summarized or referenced. Proofs in full follow the structure of
>  and the source PDF.

### 3.1. Sums of preschemes

<!-- label: I.3.1 -->

**(3.1.1)** Let `(X_λ)_{λ ∈ L}` be a family of preschemes. The topological sum `X = ⨆_λ X_λ` carries a sheaf of rings
`𝒪_X` whose restriction to each `X_λ` is `𝒪_{X_λ}`. The ringed space `(X, 𝒪_X)` is a prescheme, called the _sum_ of the
`(X_λ)`. The canonical injections `X_λ → X` are open immersions. For an `S`-prescheme structure, the sum is the
coproduct in the category of `S`-preschemes.

### 3.2. Products of preschemes

<!-- label: I.3.2 -->

**Definition (3.2.1).** Let `X`, `Y` be `S`-preschemes with structure morphisms `f : X → S` and `g : Y → S`. A _product
of `X` and `Y` over `S`_ is an `S`-prescheme `Z` together with `S`-morphisms `p : Z → X` and `q : Z → Y` (the _canonical
projections_) such that, for every `S`-prescheme `T`, the map

```
Hom_S(T, Z) → Hom_S(T, X) × Hom_S(T, Y),   u ↦ (p ∘ u, q ∘ u)
```

is a _bijection_. By the universal property, when it exists, `Z` is unique up to unique `S`-isomorphism. Write
`Z = X ×_S Y`.

**Proposition (3.2.2).** The product `X ×_S Y` exists when `X`, `Y`, and `S` are affine. Specifically, if `X = Spec(A)`,
`Y = Spec(B)`, `S = Spec(C)`, then `X ×_S Y = Spec(A ⊗_C B)`, with projections corresponding to `a ↦ a ⊗ 1` and
`b ↦ 1 ⊗ b`.

**Corollary (3.2.3).** For affine `S`, `X ×_S Y` exists if `X` is affine over `S`, etc.

**Proposition (3.2.4).** Existence of products is _local_: if it holds when `X`, `Y`, `S` are replaced by affine opens
forming covers, then it holds in general.

**Theorem (3.2.6).** For any `S`-preschemes `X`, `Y`, the product `X ×_S Y` exists.

The proof glues affine local products using a cocycle argument and (3.2.4); see Lemmas (3.2.6.1)–(3.2.6.4).

**Corollary (3.2.7).** Products are functorial: for `S`-morphisms `u : X → X′`, `v : Y → Y′`, there is a unique
`S`-morphism `u × v : X ×_S Y → X′ ×_S Y′` compatible with projections.

### 3.3. Formal properties of the product; change of base prescheme

<!-- label: I.3.3 -->

**(3.3.1)** _Commutativity:_ there is a canonical isomorphism `X ×_S Y ≅ Y ×_S X`.

**(3.3.2)** _Associativity:_ for three `S`-preschemes, `(X ×_S Y) ×_S Z ≅ X ×_S (Y ×_S Z) ≅ X ×_S Y ×_S Z`.

**Proposition (3.3.3).** Identity: `X ×_S S ≅ X` canonically.

**Corollary (3.3.4).** For `S′ → S` a morphism, the base change `X_{(S′)} = X ×_S S′` is an `S′`-prescheme, with
structure morphism the second projection. This `X ↦ X_{(S′)}` is a functor
`(S\text{-preschemes}) → (S′\text{-preschemes})`.

**Proposition (3.3.9).** _Transitivity of base change:_ for `S″ → S′ → S`, `(X ×_S S′) ×_{S′} S″ ≅ X ×_S S″`.

**Corollary (3.3.10).** Base change commutes with finite products: `(X ×_S Y)_{(S′)} = X_{(S′)} ×_{S′} Y_{(S′)}`.

**Corollary (3.3.11).** Open immersions are preserved by base change: if `j : U → X` is an open immersion, so is
`j ×_S 1_{S′} : U_{(S′)} → X_{(S′)}`.

### 3.4. Points of a prescheme with values in a prescheme; geometric points

<!-- label: I.3.4 -->

**Definition (3.4.1).** Let `X` be an `S`-prescheme, `T` an `S`-prescheme. A _`T`-valued point_ of `X` (or _`T`-point_)
is an `S`-morphism `T → X`; the set of such is `X(T) = Hom_S(T, X)`.

**(3.4.2)** A _fiber product of sets_: for sets `A → C ← B`, `A ×_C B = {(a, b) ∈ A × B : f(a) = g(b)}`.

**Proposition (3.4.3).** `(X ×_S Y)(T) = X(T) ×_{S(T)} Y(T)` for every `S`-prescheme `T`.

**(3.4.4)** _Points with values in a ring `A`_: if `T = Spec(A)`, write `X(A) = X(T)`. For `S = Spec(C)`,
`X(A) = Hom_{C\text{-alg}}(\text{some algebra}, A)` when `X` is affine.

**(3.4.5) Geometric points.** A _geometric point_ of `X` is a morphism `Spec(K) → X` for `K` a field. The _value field_
of the geometric point is `K`. A _geometric point above `s ∈ S`_ is a geometric point `Spec(K) → X` whose composition
with `X → S` factors through `Spec(K) → Spec(κ(s)) → S`. A geometric point _localized at_ `x ∈ X` is one whose
underlying map sends the unique point to `x`.

**Lemma (3.4.6).** Geometric points of `X` above `s ∈ S` correspond to pairs `(x, K_x)` with `x ∈ X` over `s` and `K_x`
an extension of `κ(x)`.

**Proposition (3.4.7).** For `f : X → Y` an `S`-morphism, every geometric point of `X` maps via `f` to a geometric point
of `Y` with the same value field.

### 3.5. Surjections and injections

<!-- label: I.3.5 -->

**Proposition (3.5.2).** A morphism `f : X → Y` is surjective iff every geometric point of `Y` lifts to a geometric
point of `X`.

**Proposition (3.5.3).** Surjectivity is preserved by base change: if `f : X → Y` is surjective and `g : Y′ → Y` is a
morphism, then `f_{(Y′)} : X ×_Y Y′ → Y′` is surjective.

**Definition (3.5.4).** A morphism `f : X → Y` is _radicial_ (or _universally injective_) if for every base change
`Y′ → Y`, `f_{(Y′)}` is injective; equivalently, for every field `K`, `X(K) → Y(K)` is injective. A radicial morphism is
injective.

**Proposition (3.5.6).** `f` is radicial iff it is injective and induces purely inseparable residue-field extensions at
every point.

**Proposition (3.5.7).** Composition and base change preserve radicial morphisms.

**Proposition (3.5.8).** _Geometric injection_: `f : X → Y` is radicial iff the diagonal `X → X ×_Y X` is surjective.

### 3.6. Fibers

<!-- label: I.3.6 -->

**Proposition (3.6.1).** For an `S`-prescheme `X` with structure morphism `f`, and a geometric point `s : Spec(K) → S`,
the _fiber_ `X_s = X ×_S Spec(K)` is a `K`-prescheme. Set-theoretically, the underlying space of `X_s` (where
`K = κ(s)`) is `f⁻¹(s)`.

**Proposition (3.6.4).** Fibers commute with base change: `(X ×_S Y)_s = X_s ×_K Y_s` (`K = κ(s)`).

**Proposition (3.6.5).** Surjectivity and radiciality of a morphism are detected fiber-by-fiber.

### 3.7. Reduction mod 𝔍

<!-- label: I.3.7 -->

For an ideal `𝔍 ⊂ A` and an `A`-prescheme `X`, the _reduction_ `X mod 𝔍` is `X ×_{Spec(A)} Spec(A/𝔍)`. This is a functor
from `A`-preschemes to `(A/𝔍)`-preschemes.

