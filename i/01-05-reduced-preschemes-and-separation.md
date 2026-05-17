# Chapter I — The Language of Schemes

## §5. Reduced Preschemes; Separation Condition

<!-- label: I.5 -->

> **Translation status.** Skeleton: principal definitions and statements translated; full proofs reference
> .

### 5.1. Reduced preschemes

<!-- label: I.5.1 -->

**Proposition (5.1.1).** Let `X` be a prescheme. The set `𝒩 ⊂ 𝒪_X` of nilpotent germs is a _quasi-coherent sheaf of
ideals_ of `𝒪_X`, called the _nilradical_ of `𝒪_X`. Locally on an affine open `Spec(A)`, `𝒩` corresponds to the
nilradical of `A`.

**Corollary (5.1.2).** `𝒩` defines a closed subprescheme `X_{red}` of `X` whose underlying space coincides with that of
`X`.

**Definition (5.1.3).** A prescheme `X` is _reduced at_ `x ∈ X` if `𝒪_x` is a reduced ring (no nonzero nilpotents). `X`
is _reduced_ if it is reduced at every point — equivalently, `𝒩 = 0`. `X_{red}` is called the _reduced prescheme
associated with_ `X`.

**Proposition (5.1.4).** `X_{red}` is reduced. The canonical immersion `X_{red} → X` is a homeomorphism, and every
morphism `Y → X` with `Y` reduced factors uniquely through `X_{red}`.

**Proposition (5.1.6).** _Integral_ preschemes (2.1.8) are exactly the reduced and irreducible ones.

**Proposition (5.1.7).** For an affine scheme `Spec(A)`: `Spec(A)` is integral iff `A` is an integral domain.

**Corollary (5.1.8).** A prescheme `X` is integral iff `𝒪_x` is an integral domain for some/every `x` (equivalently, the
residue field `κ(η)` at the generic point `η` is the field of fractions of `𝒪_{X,η}`).

**Proposition (5.1.9).** For a prescheme `X` of finite type over a Noetherian base, `X_{red}` is again of finite type.

**Corollary (5.1.10).** Reducedness is preserved by open immersions, fiber products over reduced base, and base change
to reduced bases.

### 5.2. Subprescheme with a given underlying space

<!-- label: I.5.2 -->

**Proposition (5.2.1).** For every locally closed subset `Y ⊂ X`, there is a _unique reduced_ subprescheme of `X` whose
underlying space is `Y`. Call it the _reduced subprescheme structure on `Y`_.

**Proposition (5.2.2).** For closed `Y ⊂ X`, the reduced structure on `Y` corresponds to the largest radical ideal sheaf
`𝒥 ⊂ 𝒪_X` with `Supp(𝒪_X/𝒥) = Y`.

**Corollary (5.2.3).** Every immersion `Y ↪ X` factors uniquely as a closed immersion into the reduced subprescheme
structure on its image.

**Corollary (5.2.4).** Two subpreschemes with the same underlying space and the same ideal radical agree.

### 5.3. Diagonal; graph of a morphism

<!-- label: I.5.3 -->

**(5.3.1)** For an `S`-prescheme `X`, the _diagonal morphism_ is `Δ_{X/S} : X → X ×_S X`, the unique `S`-morphism with
both projections equal to `1_X`.

**Proposition (5.3.2).** `Δ_{X/S}` is an immersion. It is a closed immersion iff `X → S` is separated (see (5.4.1)).

**Corollary (5.3.4).** The diagonal is functorial in `X`.

**Proposition (5.3.5).** For a morphism `f : X → Y` of `S`-preschemes, the _graph_ `Γ_f : X → X ×_S Y` defined by
`(1_X, f)` is an immersion.

**Corollary (5.3.6).** If `Y → S` is separated, every graph `Γ_f` is a closed immersion.

**Proposition (5.3.8).** Diagonal and graph commute with base change.

**Corollary (5.3.13).** For composable morphisms `X → Y → S`, the diagonal of `X → S` factors through the diagonal of
`X → Y` followed by the inclusion `X ×_Y X → X ×_S X`.

### 5.4. Separated morphisms and separated preschemes

<!-- label: I.5.4 -->

**Definition (5.4.1).** A morphism `f : X → S` is _separated_ (or `X` is _separated over_ `S`) if
`Δ_{X/S} : X → X ×_S X` is a _closed_ immersion. An _`S`-scheme_ is a separated `S`-prescheme. A _scheme_ (without base)
is a `ℤ`-scheme — i.e., a separated prescheme.

> Bracketed gloss: _scheme [in EGA: separated prescheme]_.

**Proposition (5.4.2).** Affine schemes are separated. Closed immersions are separated.

**Corollary (5.4.3).** Composition of separated morphisms is separated.

**Corollary (5.4.4).** Separatedness is preserved under base change.

**Corollary (5.4.5).** A subprescheme of a separated prescheme is separated.

**Corollary (5.4.6).** If `g ∘ f` is separated, so is `f`.

**Corollary (5.4.7).** A morphism is separated iff its base change to every affine open of the target is separated.

### 5.5. Separation criteria

<!-- label: I.5.5 -->

**Proposition (5.5.1) (valuative criterion).** `f : X → Y` is separated iff for every valuation ring `V` with field of
fractions `K`, every commutative square

```
Spec(K) ──→ X
   │        │
   ↓        ↓
Spec(V) ──→ Y
```

admits _at most one_ lift `Spec(V) → X`.

**Corollary (5.5.2).** Equivalently: any two `S`-sections of `X → S` that agree on a dense open subset agree everywhere.

**Corollary (5.5.3).** For `X`, `Y` separated `S`-schemes and `f, g : X → Y` two `S`-morphisms agreeing on a dense open:
`f = g`.

**Proposition (5.5.4).** Sums of separated `S`-preschemes are separated.

**Proposition (5.5.5).** A subprescheme of `Spec(A)` (any `A`) is separated.

**Proposition (5.5.6).** A monomorphism is separated.

**Corollaries (5.5.7)–(5.5.9).** Immersions are separated; locally closed subpreschemes of separated preschemes are
separated; if `f : X → Y` is separated and `g ∘ f` is separated, then `g` is separated.

