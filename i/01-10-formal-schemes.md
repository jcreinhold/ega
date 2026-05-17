# Chapter I — The Language of Schemes

## §10. Formal Schemes

<!-- label: I.10 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference .

> **Note.** The results of §10 are not used before §3 of Chapter III. Readers are encouraged to skip this section on
> first reading.

### 10.1. Formal affine schemes

<!-- label: I.10.1 -->

**(10.1.1)** Let `A` be an admissible topological ring (0.7.1). The _formal spectrum_ `Spf(A)` is the topological space
of _open_ prime ideals of `A`, with topology induced from `Spec(A)` (the discrete-topology spectrum). For each ideal of
definition `𝔍`, `Spf(A)` is identified with `Spec(A/𝔍)` (with topology, but with structure sheaf inheriting the adic
completion).

**Definition (10.1.2).** A _formal affine scheme_ is a topologically ringed space `(X, 𝒪_X)` isomorphic to
`(Spf(A), 𝒪_{Spf(A)})` for some admissible ring `A`. Here `𝒪_{Spf(A)}` is the sheaf of topological rings whose sections
over `D(f)` are the completed rings of fractions `A_{\{f\}}` (0.7.6.15).

**Proposition (10.1.3).** `Γ(Spf(A), 𝒪_{Spf(A)}) = A` topologically.

**Proposition (10.1.4).** For `A` adic Noetherian, `Spf(A)` is canonically `lim⃗_n Spec(A/𝔍^{n+1})` (filtered inductive
limit in the category of ringed spaces).

**Proposition (10.1.6).** `Spf` is a functor from admissible rings to topologically ringed spaces, contravariant in the
ring.

### 10.2. Morphisms of formal affine schemes

<!-- label: I.10.2 -->

**(10.2.1)** A _morphism of formal affine schemes_ `(X, 𝒪_X) → (Y, 𝒪_Y)` is a morphism of topologically ringed spaces
with continuous stalk homomorphisms; equivalently (for `X = Spf(A)`, `Y = Spf(B)`), a continuous ring homomorphism
`B → A`.

**Proposition (10.2.2).** Hom-sets are bijective with continuous ring homomorphisms:

```
Hom(Spf(A), Spf(B)) ≅ Hom_{cont}(B, A).
```

### 10.3. Ideals of definition for a formal affine scheme

<!-- label: I.10.3 -->

**Definition (10.3.3).** A _sheaf of ideals of definition_ for a formal prescheme `X` is a quasi-coherent sheaf of
ideals `ℐ ⊂ 𝒪_X` such that locally `ℐ` corresponds to an ideal of definition.

**Proposition (10.3.4)–(10.3.6).** Existence and uniqueness of sheaves of ideals of definition for formal affine
schemes; the _fundamental system of ideals of definition_ corresponds to a fundamental system of neighborhoods of `0` in
`A`.

### 10.4. Formal preschemes and morphisms

<!-- label: I.10.4 -->

**Definition (10.4.2).** A _formal prescheme_ is a topologically ringed space `(X, 𝒪_X)` covered by open subsets each
isomorphic to a formal affine scheme.

**Proposition (10.4.3).** Formal preschemes form a category, with morphisms locally those of formal affine schemes.

**Corollary (10.4.4).** The functor `Spf` extends to admissible topological algebras over a fixed admissible base.

**Definition (10.4.5).** _Adic morphism_: a morphism of formal preschemes `f : X → Y` is _adic_ if for every affine open
`Spf(B) ⊂ Y` with ideal of definition `𝔍 ⊂ B`, the preimage `f⁻¹(Spf(B))` admits an open cover by formal affine opens
`Spf(A_α)` whose topologies are `𝔍 A_α`-adic.

**Proposition (10.4.6).** Adic morphisms are stable under composition and base change (when fiber products exist; see
(10.7)).

**(10.4.7)** _Formal `S`-preschemes:_ for a formal prescheme `S`, a _formal `S`-prescheme_ is a formal prescheme `X`
together with a morphism `X → S`.

### 10.5. Sheaves of ideals of definition for formal preschemes

<!-- label: I.10.5 -->

**(10.5.1)** A formal prescheme `X` carries a _largest sheaf of ideals of definition_ `ℐ ⊂ 𝒪_X` such that locally `ℐ`
corresponds to an ideal of definition. Quotient `𝒪_X / ℐⁿ` defines a sheaf of rings making `(X, 𝒪_X / ℐⁿ)` a prescheme
for each `n`.

**Proposition (10.5.3).** Existence of the largest sheaf of ideals of definition.

**Proposition (10.5.4)–(10.5.6).** Comparison with sheaves of nilpotents, with adic completion, and with quotient-sheaf
constructions.

### 10.6. Formal preschemes as inductive limits

<!-- label: I.10.6 -->

**Proposition (10.6.2)–(10.6.3).** For an adic Noetherian formal prescheme `X` with sheaf of ideals of definition `ℐ`,
the system `X_n = (X, 𝒪_X / ℐⁿ⁺¹)` (`n ≥ 0`) is an _adic inductive system_ of preschemes, and `X = lim⃗_n X_n` (in a
suitable sense).

**Corollaries (10.6.4)–(10.6.5).** Properties carried from the `X_n` to `X` (and conversely).

**Proposition (10.6.9).** Sheafification of inductive systems.

### 10.7. Products of formal preschemes

<!-- label: I.10.7 -->

**Proposition (10.7.2)–(10.7.3).** For `S` a formal prescheme and `X, Y` formal `S`-preschemes, the _fiber product_
`X ×̂_S Y` exists in the category of formal preschemes, computed via completed tensor products of admissible algebras
(0.7.7).

### 10.8. Formal completion of a prescheme along a closed subset

<!-- label: I.10.8 -->

**Lemma (10.8.2).** For a prescheme `Y` and a closed subset `Y′ ⊂ Y`, the _formal completion_ `Ŷ_{/Y′}` exists as a
formal prescheme.

**Definition (10.8.4).** For a quasi-coherent ideal `𝒥 ⊂ 𝒪_Y` defining `Y′`, the _formal completion_ of `Y` along `Y′`
is the topologically ringed space `(Y′, lim⃖_n 𝒪_Y / 𝒥ⁿ)`. As a formal prescheme, this is the inductive limit of
`(Y′, 𝒪_Y / 𝒥ⁿ)`.

**Proposition (10.8.5).** The formal completion is a formal prescheme; functorial in the pair `(Y, Y′)`.

**Corollary (10.8.6).** Coherent sheaves on `Y` give rise canonically to coherent sheaves on `Ŷ_{/Y′}` by base change.

**Proposition (10.8.8)–(10.8.11).** Behavior of formal completion under products, fiber products, and morphisms;
commutation with operations on coherent sheaves.

**Corollaries (10.8.12)–(10.8.14).** Affineness, Noetherianness, and topological completeness of formal completions.

### 10.9. Extension of morphisms to completions

<!-- label: I.10.9 -->

**Proposition (10.9.4)–(10.9.5).** Morphisms `Y → Z` of preschemes extend functorially to morphisms `Ŷ_{/Y′} → Ẑ_{/Z′}`
of formal completions, provided closed subsets are compatible.

**Proposition (10.9.7).** Existence and uniqueness of extension under standard hypotheses.

### 10.10. Coherent sheaves on formal affine schemes

<!-- label: I.10.10 -->

**Proposition (10.10.2)–(10.10.8).** For an adic Noetherian formal affine scheme `Spf(A)`: every coherent sheaf is the
formal completion of a coherent sheaf on `Spec(A_n)` for some `n`; the category of coherent sheaves is equivalent to the
category of `A`-modules of finite type.

### 10.11. Coherent sheaves on formal preschemes

<!-- label: I.10.11 -->

**Proposition (10.11.1).** Coherent sheaves on locally Noetherian formal preschemes admit local descriptions in terms of
coherent sheaves on associated preschemes.

**Theorem (10.11.3).** _Comparison of coherent sheaves with formal completion:_ the formal completion of a coherent
sheaf on an algebraic prescheme along a closed subset is again coherent.

**Corollaries (10.11.4)–(10.11.5).** Specialization, restriction, and stalk computations for coherent sheaves on formal
preschemes.

**Proposition (10.11.7)–(10.11.9).** Functoriality of coherence and projective limits of coherent sheaves.

### 10.12. Adic morphisms of formal preschemes

<!-- label: I.10.12 -->

**Definition (10.12.1).** An _adic morphism_ (from (10.4.5)) preserves ideals of definition: `f^♯(ℐ_Y) · 𝒪_X = ℐ_X`
locally.

**Theorem (10.12.3).** Adic morphisms of locally Noetherian formal preschemes are stable under composition and base
change.

**Proposition (10.12.3.1).** Characterization of adic morphisms via inductive systems.

### 10.13. Morphisms of finite type

<!-- label: I.10.13 -->

**Proposition (10.13.1).** A morphism of locally Noetherian formal preschemes `f : X → Y` is _of finite type_ iff
locally on `Y = Spf(B)`, `X` is `Spf(C)` with `C` a topologically finitely generated `B`-algebra (quotient of
`B{T_1, …, T_r}`).

**Definition (10.13.3).** A formal prescheme `X` _of finite type_ over a formal prescheme `S` is one whose structure
morphism is of finite type.

**Corollaries (10.13.2), (10.13.4)–(10.13.6).** Composition, base change, and base change to ordinary preschemes
preserve finite-type morphisms.

### 10.14. Closed subpreschemes of formal preschemes

<!-- label: I.10.14 -->

**Proposition (10.14.1).** _Closed formal subpreschemes_ of a formal prescheme correspond bijectively to quasi-coherent
sheaves of ideals.

**Definition (10.14.2).** A _closed immersion of formal preschemes_ `Y → X` is a morphism realizing `Y` as a closed
formal subprescheme of `X`.

**Proposition (10.14.3)–(10.14.4).** Stability properties of closed immersions: composition, base change, fiber
products.

### 10.15. Separated formal preschemes

<!-- label: I.10.15 -->

**Definition (10.15.1).** A morphism of formal preschemes `f : X → S` is _separated_ if the diagonal `Δ : X → X ×̂_S X`
is a closed immersion of formal preschemes. _Formal `S`-schemes_ are separated formal `S`-preschemes.

Composition, base change, and standard valuative criteria carry over from the prescheme setting.
