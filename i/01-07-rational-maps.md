# Chapter I — The Language of Schemes

## §7. Rational Maps

<!-- label: I.7 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference
> .

### 7.1. Rational maps and rational functions

<!-- label: I.7.1 -->

**(7.1.1)** Two `S`-morphisms `f_1 : U_1 → Y`, `f_2 : U_2 → Y` from dense open subsets `U_1, U_2 ⊂ X` are _equivalent_
if they agree on a dense open of `U_1 ∩ U_2`. This is an equivalence relation among morphisms from dense opens; an
equivalence class is a _rational `S`-map_ `X ⇢ Y`.

**Definition (7.1.2).** A _rational `S`-map_ from `X` to `Y` (or _`S`-rational map_) is an equivalence class as above. A
_rational function_ on `X` is a rational map `X ⇢ Spec(ℤ[T])` — equivalently, an element of the _ring of rational
functions_ of `X` (defined below).

**Proposition (7.1.5).** When `X` is irreducible with generic point `η`, every rational map `X ⇢ Y` is determined by a
morphism `Spec(κ(η)) → Y` of `S`-preschemes (i.e., by a `κ(η)`-rational point of `Y`).

**Proposition (7.1.7).** For `X` irreducible, rational `S`-maps `X ⇢ Y` correspond bijectively to morphisms
`Spec(𝒪_{X,η}) → Y` of `S`-preschemes.

**Corollary (7.1.8).** For `X` integral, the _ring of rational functions on `X`_ `R(X)` is the field of fractions of
`𝒪_{X,η}` (the local ring at the generic point).

**Corollary (7.1.9).** For `X` integral with function field `R(X) = K`, rational maps `X ⇢ Y` correspond bijectively to
`K`-rational points of `Y` (when `Y → S` is appropriate).

**Proposition (7.1.11).** For `X` having finitely many irreducible components `X_i` with generic points `η_i`, the _ring
of rational functions_ is `R(X) = ∏_i 𝒪_{X,η_i}` (product of local rings at generic points).

**Corollaries (7.1.12)–(7.1.16).** Functoriality and base-change properties of `R(X)`; rational maps compose when
defined; the field/ring `R(X)` is the ring of rational sections of `𝒪_X` along the generic-fiber subprescheme.

### 7.2. Domain of definition of a rational map

<!-- label: I.7.2 -->

**Definition (7.2.1).** The _domain of definition_ of a rational map `f : X ⇢ Y` is the union of all open `U ⊂ X` on
which `f` is represented by an honest morphism `U → Y`. A rational map is _defined at_ `x ∈ X` if `x` is in its domain.

**Proposition (7.2.2).** The domain of definition is open.

**Corollaries (7.2.3)–(7.2.7).** Properties of domains of definition: stability under composition; restriction; behavior
under base change.

**(7.2.8)** A rational map `f : X ⇢ Spec(B)` to an affine target is defined at `x` iff each generator `b ∈ B` "extends"
to a section of `𝒪_X` in a neighborhood of `x`.

**Proposition (7.2.9).** For `X` integral and `Y` separated, a rational map `f : X ⇢ Y` is determined by its restriction
to any nonempty open of the domain of definition.

### 7.3. Sheaf of rational functions

<!-- label: I.7.3 -->

**(7.3.1)** Define the _sheaf of rational functions_ `𝒦_X` on `X` as the sheaf associated with the presheaf
`U ↦ R(U) = (ring of rational functions on U)`.

**Definition (7.3.2).** A _meromorphic function_ on `X` is a section of `𝒦_X`. The sheaf `𝒦_X` is an `𝒪_X`-module
containing `𝒪_X` as a subsheaf.

**Proposition (7.3.3).** When `X` is integral, `𝒦_X` is the constant sheaf with stalks `R(X)`.

**Corollaries (7.3.4)–(7.3.6).** Behavior of `𝒦_X` under open immersions, sums, and reduction.

**Proposition (7.3.7).** For `X` locally Noetherian, the _total ring of fractions_ sheaf `𝒦_X` is the sheafification of
`U ↦ S_U⁻¹ Γ(U, 𝒪_X)` where `S_U` is the set of non-zero-divisors in `Γ(U, 𝒪_X)`.

### 7.4. Torsion and torsion-free sheaves

<!-- label: I.7.4 -->

**(7.4.1)** For an `𝒪_X`-module `ℱ`, the _torsion subsheaf_ `t(ℱ) ⊂ ℱ` is the kernel of `ℱ → ℱ ⊗_{𝒪_X} 𝒦_X`. `ℱ` is
_torsion-free_ if `t(ℱ) = 0`, _torsion_ if `t(ℱ) = ℱ`.

**Proposition (7.4.2).** Torsion is functorial; `t(ℱ)` is the largest torsion subsheaf.

**(7.4.2)** For `ℱ` torsion-free of finite rank, the _rank_ is the rank of `ℱ ⊗_{𝒪_X} 𝒦_X` as an `𝒦_X`-module.

**Corollary (7.4.3).** On an integral prescheme, the rank of a torsion-free coherent sheaf is well-defined (constant).

**Proposition (7.4.5)–(7.4.6).** Torsion behavior under direct sums, tensor products, and pullback.

