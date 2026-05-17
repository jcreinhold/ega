# Chapter I — The Language of Schemes

## §9. Complements on Quasi-coherent Sheaves

<!-- label: I.9 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference
> `~/Code/ega/ega1/ega1-9.tex`.

### 9.1. Tensor product of quasi-coherent sheaves

<!-- label: I.9.1 -->

**Proposition (9.1.1).** For quasi-coherent `𝒪_X`-modules `ℱ`, `𝒢` on a prescheme `X`, `ℱ ⊗_{𝒪_X} 𝒢` is quasi-coherent.

**Definition (9.1.2).** For preschemes `X_1, X_2` and quasi-coherent `𝒪_{X_i}`-modules `ℱ_i` (`i = 1, 2`), the _tensor
product on distinct preschemes_ `ℱ_1 ⊠ ℱ_2 = p_1^*(ℱ_1) ⊗_{𝒪_{X_1 ×_S X_2}} p_2^*(ℱ_2)` on `X_1 ×_S X_2` (where `p_i` is
the projection).

**Proposition (9.1.3).** External tensor product is quasi-coherent; bifunctorial in `ℱ_1, ℱ_2`.

**Proposition (9.1.4).** _Restriction of scalars and base change preserve quasi-coherence:_ for `f : X → Y` and `ℱ`
quasi-coherent on `Y`, `f*(ℱ)` is quasi-coherent on `X`.

**Corollaries (9.1.5)–(9.1.7).** Behavior under sub- and quotient-modules, kernels, cokernels, inductive limits.

**Proposition (9.1.9)–(9.1.12).** Exactness properties: `f*` is right exact; if `f` is flat, `f*` is exact.

**Corollary (9.1.13).** Stalks of pullback: `(f*(ℱ))_x = ℱ_{f(x)} ⊗_{𝒪_{f(x)}} 𝒪_x`.

### 9.2. Direct image of a quasi-coherent sheaf

<!-- label: I.9.2 -->

**Proposition (9.2.1).** For `f : X → Y` a _quasi-compact, separated_ morphism, and `ℱ` quasi-coherent on `X`, the
direct image `f_*(ℱ)` is quasi-coherent on `Y`.

**Corollary (9.2.2).** For an affine morphism `f : X → Y` (i.e., the preimage of every affine open is affine), `f_*`
preserves quasi-coherence.

### 9.3. Extension of sections

<!-- label: I.9.3 -->

**Theorem (9.3.1).** Let `X` be a Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-module, `U ⊂ X` open. Every section
`s ∈ Γ(U, ℱ)` extends to a section of `ℱ ⊗ 𝒪_X(D)` for some divisor `D` supported on `X ∖ U` (after multiplying by
powers of local equations).

**Corollary (9.3.2)–(9.3.3).** Sections over `U = X_f` extend to global sections after multiplying by a power of `f`.

**Proposition (9.3.4).** Behavior of section extension under flat base change.

**Corollary (9.3.5).** For Noetherian `X` and quasi-compact `U`, `Γ(U, ℱ)` is a localization of `Γ(X, ℱ)` in a precise
functorial sense.

### 9.4. Extension of quasi-coherent sheaves

<!-- label: I.9.4 -->

**(9.4.1)** For `X` a Noetherian prescheme, `U ⊂ X` open, and `ℱ` quasi-coherent on `U`, an _extension_ of `ℱ` to `X` is
a quasi-coherent `𝒪_X`-module `ℱ̃` with `ℱ̃ | U ≅ ℱ`.

**Proposition (9.4.2).** _Existence of extension:_ every quasi-coherent sheaf on `U` extends to a quasi-coherent sheaf
on `X`.

**Corollary (9.4.3).** Coherent extensions: a coherent sheaf on `U` extends to a coherent sheaf on `X` whose restriction
to `U` is the given one.

**Corollary (9.4.5).** Quasi-coherent sub-Modules of a coherent sheaf extend to quasi-coherent sub-Modules.

**Lemma (9.4.6).** Bounded-from-below `𝒥`-adic filtrations: for a quasi-coherent ideal `𝒥` and coherent `ℱ`, the
canonical filtration `𝒥ⁿ ℱ` decreases to a quasi-coherent submodule.

**Theorem (9.4.7).** _Theorem of extension of subsheaves:_ every quasi-coherent subsheaf of `ℱ | U` extends to a
quasi-coherent subsheaf of `ℱ` on `X`.

**Corollaries (9.4.8)–(9.4.10).** Consequences for closed subpreschemes, base change, and morphisms.

### 9.5. Closed image of a prescheme; closure of a subprescheme

<!-- label: I.9.5 -->

**Proposition (9.5.1).** For `f : X → Y` with `X` Noetherian (or `f` quasi-compact), the kernel
`𝒥 = Ker(𝒪_Y → f_*(𝒪_X))` is a quasi-coherent ideal sheaf, defining the _closed image_ `f(X)̄` (with reduced
subprescheme structure) — the smallest closed subprescheme of `Y` through which `f` factors.

**Corollary (9.5.2).** The closed image is the closure of the set-theoretic image in `Y` with its reduced subprescheme
structure when `Y` is reduced.

**Definition (9.5.3).** The _closure_ of a subprescheme `Y′ ↪ Y` (or _adherence_ of a subprescheme) is the closed image
of `Y′ → Y`.

**Propositions (9.5.4)–(9.5.6).** Functoriality of the closure under base change and composition.

**Propositions (9.5.8)–(9.5.10).** Closures and irreducible components: the closure of `Y′` decomposes by the
irreducible components of `Y′̄`.

**Corollary (9.5.11).** _Closure of a subprescheme_: `Y′ ↪ Y` extends uniquely (up to isomorphism) to a closed
subprescheme of `Y` containing `Y′` as a dense open subprescheme.

### 9.6. Quasi-coherent sheaves of algebras; change of structure sheaf

<!-- label: I.9.6 -->

**Proposition (9.6.1).** For a quasi-coherent `𝒪_X`-algebra `𝒜`, the ringed space `(X, 𝒜)` is not in general a
prescheme, but its "Spec" is — see (9.6.5).

**Proposition (9.6.3).** Quasi-coherence is preserved under change of structure sheaf for affine morphisms.

**Corollary (9.6.4).** Tensor products of quasi-coherent algebras are quasi-coherent.

**Proposition (9.6.5) (Spec of a quasi-coherent algebra).** For `(X, 𝒪_X)` a prescheme and `𝒜` a quasi-coherent
`𝒪_X`-algebra, there is an affine morphism `f : Spec(𝒜) → X` such that `f_*(𝒪_{Spec(𝒜)}) = 𝒜` and `Spec(𝒜)` is universal
among `X`-preschemes whose direct image yields `𝒜`.

**Proposition (9.6.6).** Properties of `Spec(𝒜)`: it is separated; coherent if `𝒜` is locally finitely presented;
functorial in `𝒜`.

<!-- source: ~/Code/papers/books/ega/i/01-09-complements-faisceaux-quasi-coherents.md and ~/Code/ega/ega1/ega1-9.tex -->
