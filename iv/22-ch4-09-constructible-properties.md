<!-- original page 54 -->

## §9. Constructible properties

Let `S` be a prescheme, `f : X → S` a morphism *of finite presentation* `(1.6.1)`, `ℱ` a quasi-coherent `𝒪_X`-Module of
finite presentation. We propose, in this section, to give criteria ensuring, for example, that the set of `s ∈ S` such
that the `k(s)`-prescheme `X_s = f⁻¹(s) = X ×_S Spec(k(s))` has a certain property, or such that the `𝒪_{X_s}`-Module
`ℱ_s = ℱ ⊗_{𝒪_S} k(s)` has a certain property, is locally constructible, or at least *ind-constructible* `(1.9.4)`; we
shall see that this is the case for most of the properties that arise in algebraic geometry. Assuming only `f` locally
of finite presentation, we shall also give `(9.9)` criteria for the set of points `x ∈ X` where the fibre `X_{f(x)}` (or
the `𝒪_{X_{f(x)}}`-Module `ℱ_{f(x)}`) has a certain property to be locally constructible. We shall see in §12 that these
results, combined with the additional hypothesis that `f` is flat (resp. proper and flat), allow one to prove that the
sets considered in `X` (resp. in `S`) are even *open* in many cases.

### 9.1. The principle of finite extension

**Proposition (9.1.1) (Principle of finite extension).**

<!-- label: IV.9.1.1 -->

*Let `k` be a field, `𝒞` a set of extensions of `k`. Assume the following conditions are satisfied:*

*(i) If `K ∈ 𝒞` and there exists a `k`-homomorphism `K → K'` (where `K'` belongs to the universe in which one places
oneself), then `K' ∈ 𝒞`.*

*(ii) If `K ∈ 𝒞`, there exists a sub-extension `K'` of `K`, of finite type over `k`, such that `K' ∈ 𝒞`.*

*(iii) If `K ∈ 𝒞` is the field of fractions of an integral `k`-algebra `A` of finite type, there exists `f ∈ A − {0}`
such that for every maximal ideal `𝔪` of `A_f` one has `A_f/𝔪 ∈ 𝒞`.*

<!-- original page 55 -->

*Let `Ω` be an algebraically closed extension of `k` (in the universe under consideration). The following conditions are
equivalent:*

*a) `𝒞` is non-empty.*

*b) There exists `K' ∈ 𝒞` which is a finite extension of `k`.*

*c) One has `Ω ∈ 𝒞`.*

Condition (i) evidently implies that b) entails c), and c) entails trivially a); let us prove that a) entails b). By
virtue of (ii) and (iii) there exists an extension `K' ∈ 𝒞` of the form `A/𝔪`, where `A` is a `k`-algebra of finite type
over `k` and `𝔪` is a maximal ideal of `A`. One knows, by Hilbert's Nullstellensatz
`(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 2 of th. 1)`, that `K'` is a finite extension of `k`.

**Corollary (9.1.2).**

<!-- label: IV.9.1.2 -->

*Under the hypotheses (i), (ii), (iii) of `(9.1.1)`, if `k` is algebraically closed and if `𝒞` is non-empty, then `𝒞`
contains all extensions of `k` in the universe considered.*

Indeed, since a) entails c), one has `k ∈ 𝒞`, and the conclusion results from hypothesis (i).

**Remark (9.1.3).**

<!-- label: IV.9.1.3 -->

In practice, one will verify condition (ii) of `(9.1.1)` by noting that `K` is the inductive limit of its sub-extensions
`K_α` of finite type, and by applying the results of §8, taking into account if necessary that for `K_α ⊂ K_β`, `K_β` is
faithfully flat over `K_α`. Frequently the set `𝒞` is formed of the fields belonging to a set `𝒞'` of `k`-algebras that
satisfies the following condition:

*(i bis) If `A ∈ 𝒞'` and there exists a `k`-algebra homomorphism `A → A'` (where `A'` belongs to the universe in which
one places oneself), then `A' ∈ 𝒞'`.*

When this is the case, condition (i) is trivially satisfied, and one will generally verify condition (iii) of `(9.1.1)`
by noting that the field of fractions `K` of `A` is the inductive limit of the algebras `A_f` (for the relation
`D(f) ⊃ D(g)`), and by applying the results of §8, taking into account if necessary that the morphisms `D(g) → D(f)` are
open immersions.

By contrast, when (i bis) is not satisfied, the proof of (iii) is often more delicate, and is tied to constructibility
criteria that will be developed below.

Here are some typical examples of application of the principle of finite extension.

**Proposition (9.1.4).**

<!-- label: IV.9.1.4 -->

*Let `k` be a field, `Ω` an algebraically closed extension of `k`, `X` and `Y` two preschemes of finite type over `k`.
The following conditions are equivalent:*

*a) There exists an `Ω`-morphism `X_{(Ω)} → Y_{(Ω)}` (resp. an `Ω`-morphism possessing one (specified) of the properties
(i) to (xiv) of `(8.10.5)`).*

*b) There exists a finite extension `k'` of `k` and a `k'`-morphism `X_{(k')} → Y_{(k')}` (resp. a `k'`-morphism
possessing the property considered).*

*c) There exists an extension `K` of `k` and a `K`-morphism `X_{(K)} → Y_{(K)}` (resp. a `K`-morphism possessing the
property considered).*

One applies remark `(9.1.3)`, taking for `𝒞'` the set of all `k`-algebras `A` (of the universe in which one is placed)
such that there exists an `A`-morphism `X ⊗_k A → Y ⊗_k A` (resp. a morphism having that one of the properties of
`(8.10.5)` that one considers). Condition (i bis) of `(9.1.3)` is then verified thanks to the fact that the

<!-- original page 56 -->

properties envisaged in `(8.10.5)` are all stable under base change. Condition (iii) of `(9.1.1)` is therefore satisfied
by virtue of `(8.8.2, (i))` (resp. `(8.10.5)`), since `Spec(k)` is quasi-compact and quasi-separated. It remains to
verify condition (ii) of `(9.1.1)`, which follows again from `(8.8.2, (i))` and `(8.10.5)`, by viewing `K` as the
inductive limit of its sub-extensions of finite type. One concludes therefore by `(9.1.1)`.

In particular, if there exists an extension `K` of `k` and a `K`-isomorphism `X_{(K)} ⥲ Y_{(K)}`, one says that `X` and
`Y` are *geometrically isomorphic*.

The following corollary generalizes `(II, 6.6.5)`.

**Corollary (9.1.5).**

<!-- label: IV.9.1.5 -->

*Let `k` be a field, `X` a `k`-prescheme. If there exists an extension `K` of `k` such that `X_{(K)}` is projective
(resp. quasi-projective) over `K`, then `X` is projective (resp. quasi-projective) over `k`.*

The morphism `Spec(K) → Spec(k)` being faithfully flat and quasi-compact, it follows already from `(2.7.1, (v))` that
`X` is of finite type over `k`. The hypothesis means that there exists a closed immersion (resp. an immersion)
`X_{(K)} → 𝐏^r_K = 𝐏^r_k ⊗_k K` `(II, 5.5.4, (ii) and 5.5.3)`; applying `(9.1.4)` for property (iv) (resp. (ii)) of
`(8.10.5)`, one deduces that there is a finite extension `k'` of `k` and a closed immersion (resp. an immersion)
`X_{(k')} → 𝐏^r_{k'}`, that is, `X_{(k')}` is projective (resp. quasi-projective) over `k'`. One concludes by
`(II, 6.6.5)`.

**Proposition (9.1.6).**

<!-- label: IV.9.1.6 -->

*Let `k` be a field, `Ω` an algebraically closed extension of `k`, `X` a prescheme of finite type over `k`, `ℱ`, `𝒢` two
coherent `𝒪_X`-Modules. Suppose there exists an isomorphism `ℱ ⊗_k Ω ⥲ 𝒢 ⊗_k Ω`. Then there exist a finite extension
`k'` of `k` and an isomorphism `ℱ ⊗_k k' ⥲ 𝒢 ⊗_k k'`.*

The reasoning is the same as in `(9.1.4)`, applying `(8.5.2, (i))` (one uses here, in the proof of property (iii) of
`(9.1.1)`, the fact that the morphisms `D(g) → D(f)` (with the notation of `(9.1.3)`) are open immersions, and *a
fortiori* flat morphisms).

### 9.2. Constructible and ind-constructible properties

**Definition (9.2.1).**

<!-- label: IV.9.2.1 -->

*Let `P(X, ℱ, k)` be a relation. We say that `P` is a **constructible** (resp. **ind-constructible**) **property of
algebraic preschemes** if the following two conditions are satisfied:*

*(i) If `k` is a field, `X` an algebraic prescheme over `k`, `ℱ` a coherent `𝒪_X`-Module, `k'` an extension of `k`,
then, for `P(X, ℱ, k)` to be true, it is necessary and sufficient that `P(X_{(k')}, ℱ ⊗_k k', k')` be true.*

*(ii) Let `S` be an integral Noetherian prescheme, of generic point `η`, `u : X → S` a morphism of finite type, `ℱ` a
coherent `𝒪_X`-Module. For every `s ∈ S`, set `X_s = u⁻¹(s) = X ×_S Spec(k(s))`, `ℱ_s = ℱ ⊗_{𝒪_S} k(s)`. Let `E` be the
set of `s ∈ S` such that `P(X_s, ℱ_s, k(s))` is true. Then one of the sets `E`, `S − E` (resp. the set `E`) contains a
non-empty open set (and consequently is a neighbourhood of `η`) (resp. contains a non-empty open set if it contains
`η`).*

<!-- original page 57 -->

**Remarks (9.2.2).**

<!-- label: IV.9.2.2 -->

(i) This is of course a convention of language of metamathematical nature and not a mathematical definition properly
speaking. One has analogous "definitions" for relations between `k`, one or several algebraic `k`-preschemes,
`k`-morphisms between these preschemes, coherent Modules on these preschemes, or homomorphisms between these Modules.

(ii) We shall also have to consider relations in which constructible parts of preschemes figure. For example, let
`P(X, Z, k)` be a relation; we shall say (by abuse of language) that `P` is a **constructible** (resp.
**ind-constructible**) **property of the constructible part `Z` of `X`** if the following two conditions are satisfied:

1° If `k` is a field, `X` an algebraic prescheme over `k`, `Z` a constructible part of `X`, `k'` an extension of `k`,
then, for `P(X, Z, k)` to be true, it is necessary and sufficient that `P(X_{(k')}, p⁻¹(Z), k')` be true
(`p : X_{(k')} → X` being the canonical projection).

2° Let `S` be an integral Noetherian prescheme, of generic point `η`, `u : X → S` a morphism of finite type, `Z` a
constructible part of `X`. For every `s ∈ S`, set `X_s = u⁻¹(s)`, `Z_s = Z ∩ X_s`. Let `E` be the set of `s ∈ S` such
that `P(X_s, Z_s, k(s))` is true. Then one of the sets `E`, `S − E` (resp. the set `E`) contains a non-empty open set
(resp. contains a non-empty open set if it contains `η`).

One should note that in condition 2° one must assume that `Z` is a constructible part *of `X`*, and not only that `Z_s`
is a constructible part of `X_s` for every `s`; the former of these two properties entails the latter `(1.8.2)`, but not
conversely.

(iii) If `P` is a constructible property, it is clear that the same is true of "not `P`". If `P`, `Q` are two
constructible (resp. ind-constructible) properties, the same is true of the properties "`P` or `Q`" and "`P` and `Q`";
indeed, if, under the hypotheses of `(9.2.1, (ii))`, `E`, `E'` are two parts of `S` and if `E` contains a non-empty open
set, the same is true of `E ∪ E'`, and if `S − E` and `S − E'` each contain a non-empty open set, the same is true of
`S − (E ∪ E') = (S − E) ∩ (S − E')`.

(iv) Let `P(X, ℱ, k)` be a relation satisfying condition `(9.2.1, (i))`; let `S` be a prescheme, `u : X → S` a morphism
of finite type; with the notation of `(9.2.1, (ii))`, let `E` be the set of `s ∈ S` such that `P(X_s, ℱ_s, k(s))` is
true. Let on the other hand `g : S' → S` be an arbitrary morphism, and set `X' = X_{(S')}`, `ℱ' = ℱ ⊗_{𝒪_S} 𝒪_{S'}`;
then it follows from the transitivity of fibres `(I, 3.6.4)` and from condition `(9.2.1, (i))` that *the set of
`s' ∈ S'` such that `P(X'_{s'}, ℱ'_{s'}, k(s'))` is true is equal to `g⁻¹(E)`*. This extends at once to the case where
several preschemes, Modules, morphisms of preschemes, or homomorphisms of Modules figure in `P`, and to properties of
the type considered in (ii).

(v) As we shall see in the remainder of this section and in the course of the rest of Chap. IV, most properties `P`
satisfying condition `(9.2.1, (i))` also satisfy `(9.2.1, (ii))`. As possible exceptions, let us note the property of
being *projective*, or *quasi-projective*, or *affine*, or *quasi-affine* over the base field (for an algebraic
prescheme); we shall see `(9.6.2)` that these properties are ind-constructible, but we shall later give an example where
`S` is a non-empty open part of `Spec(ℤ)` (or an open part of an elliptic curve over a finite field) and where all the
fibres `X_s`

<!-- original page 58 -->

*except* the generic fibre `X_η` are projective over `k(s)` (all the preschemes `X_s` being of dimension 2).

**Proposition (9.2.3).**

<!-- label: IV.9.2.3 -->

*Let `P` be a constructible (resp. ind-constructible) property of algebraic preschemes, `S` a prescheme, `X` a prescheme
of finite presentation over `S`, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. Then the set `E` of `s ∈ S`
such that `P(X_s, ℱ_s, k(s))` is true is locally constructible (resp. ind-constructible). Moreover, if `S` is
irreducible of generic point `η`, then one of the two sets `E`, `S − E` is a neighbourhood of `η` in `S` (resp. `E` is a
neighbourhood of `η` if it contains this point).*

To prove these assertions, one may restrict to the case where `S = Spec(A)` is affine. One then knows that there exists
a sub-ring `A_0` of `A` which is a `ℤ`-algebra of finite type, an `A_0`-prescheme of finite type `X_0`, and a coherent
`𝒪_{X_0}`-Module `ℱ_0` such that `X` is isomorphic to `X_0 ⊗_{A_0} A` and `ℱ` to `ℱ_0 ⊗_{A_0} A` `(8.9.1)`. Let
`p : S → S_0 = Spec(A_0)` be the morphism corresponding to the injection `A_0 → A`, and let `E_0` be the set of
`s_0 ∈ S_0` such that `P((X_0)_{s_0}, (ℱ_0)_{s_0}, k(s_0))` is true; then, by virtue of `(9.2.2, (iv))`, one has
`E = p⁻¹(E_0)`; one may therefore `(1.8.2)` restrict to the case where `S` is the spectrum of a `ℤ`-algebra of finite
type, hence a Noetherian scheme. Let us use the constructibility criterion `(0_III, 9.2.3)` (resp. the
ind-constructibility criterion `(1.9.10)`); one is then reduced, using as above `(9.2.2, (iv))` and replacing `S` by an
integral closed sub-scheme of `S`, to the case where `S` is Noetherian and integral, and one must prove that `E` is rare
in `S` or contains a non-empty open set of `S` (resp. that `E` contains a non-empty open set of `S` if it contains the
generic point); but this is guaranteed by virtue of condition `(9.2.1, (ii))`.

One should note that one has used `(9.2.1, (ii))` only when `S` is the spectrum of an integral ring of finite type over
`ℤ`. It is clear on the other hand that the statement of `(9.2.3)` also applies when several preschemes, Modules on
these preschemes, morphisms of preschemes, or homomorphisms of Modules figure in `P`. It still applies when (finitely
many) parts of the preschemes considered figure in it, provided that one imposes on these parts the condition of being
*locally constructible*. Indeed, the restriction to the case where `S` is affine shows that one may restrict to the case
where these parts are constructible: one then applies `(8.3.11)`, which shows (with the notation above) that a
constructible part of `X` is the inverse image of a constructible part of `X_0` for a suitable choice of `A_0`.

**Corollary (9.2.4).**

<!-- label: IV.9.2.4 -->

*Let `P` be a constructible (resp. ind-constructible) property of algebraic preschemes, `X`, `Y` two `S`-preschemes of
finite presentation, `f : X → Y` an `S`-morphism. For every `s ∈ S`, set `X_s = X ×_S Spec(k(s))`,
`Y_s = Y ×_S Spec(k(s))`, `f_s = f × 1 : X_s → Y_s`. Then the set `E` of `s ∈ S` such that, for every `y ∈ Y_s`, the
property `P(f_s⁻¹(y), k(y))` is true, is locally constructible (resp. ind-constructible).*

Indeed, let `Z` be the set of `y ∈ Y` such that `P(f⁻¹(y), k(y))` is true. As the fibres `f⁻¹(y)` and `f_s⁻¹(y)` are
isomorphic, one sees that `E` is the set of `s ∈ S` such that `Y_s ⊂ Z`; if `g : Y → S` is the structure morphism, one
therefore has `E = S − g(Y − Z)`.

<!-- original page 59 -->

Now `f` is of finite presentation `(1.6.2, (v))`, so it follows from `(9.2.3)` that `Z` is locally constructible (resp.
ind-constructible) in `Y`, hence `Y − Z` is locally constructible (resp. pro-constructible) in `Y`. Since `g` is of
finite presentation, `g(Y − Z)` is locally constructible (resp. pro-constructible) in `S`, by virtue of Chevalley's
theorem `(1.8.4)` (resp. of `(1.9.5, (vii))`); hence `E` is locally constructible (resp. ind-constructible) in `S`.

**Remark (9.2.5).**

<!-- label: IV.9.2.5 -->

One should note that if `P` is a property of algebraic preschemes for which prop. `(9.2.3)` is true, then `P` also
satisfies condition `(9.2.1, (ii))`: this follows from the fact that in an irreducible Noetherian space, a constructible
set is rare or contains a non-empty open set `(0_III, 9.2.3)`.

**Proposition (9.2.6).**

<!-- label: IV.9.2.6 -->

*Let `P` denote one of the following properties of a `k`-prescheme `X`:*

*(i) `X` is empty.*

*(ii) `X` is finite over `k`.*

*(iii) `X` is radicial over `k`.*

*(iv) `dim(X)` belongs to a given part `Φ` of the set `‾ℤ = ℤ ∪ {−∞}`.*

*Then `P` is constructible.*

It is clear that (i) and (ii) are special cases of (iv), taking respectively for `Φ` the set `{−∞}` and the set
`{−∞, 0}`. One has therefore only to prove (iii) and (iv). In each of these two cases condition (i) of `(9.2.1)` is
fulfilled by virtue of `(2.7.1, (xv))` and `(4.1.4)`. On the other hand, in case (iii), the property `P` satisfies the
conclusion of `(9.2.3)` by virtue of `(1.8.7)`; it remains therefore to see that the same is true in case (iv). This
will result from the more precise proposition that follows.

**Proposition (9.2.6.1).**

<!-- label: IV.9.2.6.1 -->

*If `f : X → S` is a morphism of finite presentation, the function `s ↦ dim(f⁻¹(s))` is locally constructible.*

The question is local on `S`, so one may suppose that `S = Spec(A)` is affine and prove that for every `n`, the set `E`
of `s ∈ S` such that `dim(X_s) = n` is constructible. The same reasoning as in `(9.2.3)` reduces to the case where `A`
is Noetherian and integral, and it then suffices to prove:

**Corollary (9.2.6.2).**

<!-- label: IV.9.2.6.2 -->

*Let `S` be an integral Noetherian prescheme of generic point `η`, `f : X → S` a morphism of finite type. Then there
exists a neighbourhood of `η` in `S` such that the function `s ↦ dim(X_s)` is constant in this neighbourhood.*

The images by `f` of the irreducible components (finitely many) of `X` which do not meet `X_η` are contained in closed
parts of `S` not containing `η` (since `S` is integral `(0_I, 2.1.5)`), so (replacing `S` by an open neighbourhood of
`η`) one may restrict to the case where all the irreducible components `X_i` of `X` meet `X_η`; denote again by `X_i`
the reduced closed sub-prescheme of `X` having `X_i` as underlying space; since `dim(X_s) = sup_i dim((X_i)_s)`
`(4.1.1)`, one may restrict

<!-- original page 60 -->

to the case where `X` is irreducible. There then exists a finite cover `(U_j)` of `X` by everywhere-dense affine open
sets, and the numbers `dim((U_j)_η)` are all equal to `n = dim(X_η)` `(4.1.1.3)`; one may therefore restrict to the case
where `X` is affine, hence also `X_η`. There then exists, by virtue of `(4.1.2)`, a non-empty open set `W` of `X` such
that `W ⊂ X_η`, and a finite surjective `k(η)`-morphism `h : W_η → 𝐕^n_{k(η)} (= Spec(k(η)[T_1, …, T_n]))`; applying
`(8.8.2, (i))` and the method of `(8.1.2, a))`, one deduces (replacing `S` if necessary by a neighbourhood of `η`) that
`h = g_η`, where `g : W → 𝐕^n_A (= Spec(A[T_1, …, T_n]))` is an `S`-morphism, and one may suppose this morphism finite
and surjective by virtue of `(8.10.5, (vi) and (x))`. One concludes that for every `s ∈ S`, the morphism
`g_s : W_s → 𝐕^n_{k(s)}` is finite and surjective, hence `dim(W_s) = n` `(4.1.2)`.

### 9.3. Constructible properties of morphisms of algebraic preschemes

**Proposition (9.3.1).**

<!-- label: IV.9.3.1 -->

*Let `P(X, k)` be a constructible (resp. ind-constructible) property of algebraic preschemes. Denote by `P'(f, X, Y, k)`
the following relation: `f : X → Y` is a `k`-morphism of algebraic `k`-preschemes such that for every `y ∈ Y`, one has
the property `P(f⁻¹(y), k(y))`. Then `P'` is a constructible (resp. ind-constructible) property.*

Indeed, since `P` satisfies condition `(9.2.1, (i))`, the same is true of `P'` by virtue of the transitivity of fibres
`(I, 3.6.4)`; on the other hand, the fact that `P'` satisfies condition `(9.2.1, (ii))` results from `(9.2.4)`, in view
of remark `(9.2.5)`.

**Proposition (9.3.2).**

<!-- label: IV.9.3.2 -->

*Let `P` denote one of the following properties of a `k`-morphism `f : X → Y` of algebraic `k`-preschemes:*

*(i) `f` is surjective.*

*(ii) `f` is quasi-finite.*

*(iii) `f` is radicial.*

*(iv) For every `y ∈ Y`, `dim(f⁻¹(y))` belongs to `Φ` (notation of `(9.2.6)`).*

*Then `P` is constructible.*

This follows at once from `(9.3.1)` and `(9.2.6)` if one takes into account that `f` is of finite type `(1.5.4, (v))`,
the characterization of radicial morphisms `(I, 3.5.8)`, and that of quasi-finite morphisms `(II, 6.2.2)`.

**Proposition (9.3.3).**

<!-- label: IV.9.3.3 -->

*Suppose the hypotheses of `(8.8.1)` are satisfied, the notation of which we retain; suppose in addition that `S_α` is
quasi-compact, `X_α` and `Y_α` of finite presentation over `S_α`, and let `f_α : X_α → Y_α` be an `S_α`-morphism. Let
`P` be an ind-constructible property of morphisms of algebraic preschemes. For every `s ∈ S` (resp. `s_λ ∈ S_λ`) set
`X_s = X ×_S Spec(k(s))`, `Y_s = Y ×_S Spec(k(s))`, `f_s = f × 1 : X_s → Y_s` (resp.
`X_{λ, s_λ} = X_λ ×_{S_λ} Spec(k(s_λ))`, `Y_{λ, s_λ} = Y_λ ×_{S_λ} Spec(k(s_λ))`,
`f_{λ, s_λ} = f_λ × 1 : X_{λ, s_λ} → Y_{λ, s_λ}`). Then, in order that for every `s ∈ S` one has the property `P(f_s)`,
it is necessary and sufficient that there exist `λ ⩾ α` such that for every `s_λ ∈ S_λ`, one has `P(f_{λ, s_λ})`.*

Indeed, let `E` (resp. `E_λ`) be the set of `s ∈ S` (resp. `s_λ ∈ S_λ`) such that the property `P(f_s)` (resp.
`P(f_{λ, s_λ})`) is true; it follows from `(9.2.2, (iv))` that one has `E_μ = u_{λμ}⁻¹(E_λ)` for `λ ⩽ μ`, and
`E = u_λ⁻¹(E_λ)`; moreover, by virtue of `(9.2.3)`, `E` (resp. `E_λ`) is ind-constructible in `S` (resp. `S_λ`); the
proposition therefore results from `(8.3.4)` applied to the ind-constructible part `E` of `S`.

<!-- original page 61 -->

This result generalizes without difficulty to properties `P` of the type considered in `(9.2.3, (i) and (ii))`.

**Remark (9.3.4).**

<!-- label: IV.9.3.4 -->

The conjunction of `(9.3.3)` and `(9.3.2, (ii))` proves the assertion `(8.10.5, (xi))`.

**Proposition (9.3.5).**

<!-- label: IV.9.3.5 -->

*Let `P(X, Y, k)` be the property: "`X` and `Y` are two preschemes of finite type over the field `k`, and there exists
an extension `k'` of `k` and a `k'`-morphism `g : X_{(k')} → Y_{(k')}` satisfying `Q(g)`", where `Q` is one of the
properties (i) to (xiv) of `(8.10.5)`. Then `P` is an ind-constructible property.*

The definition of `P` shows indeed that condition `(9.2.1, (i))` is satisfied, taking account of the fact that the
property `Q(g)` is stable under change of base field, and that two extensions of `k` can always be considered as
sub-extensions of a third extension of `k`. To verify `(9.2.1, (ii))`, one may restrict to the case where `S = Spec(A)`
is affine; if `K = k(η)`, the field of fractions of `A`, there exists by hypothesis and by virtue of `(9.1.4)` a finite
extension `K'` of `K` and a `K'`-morphism `g' : (X_η)_{(K')} → (Y_η)_{(K')}` satisfying `Q(g')`, and `K'` is evidently
the field of fractions of an integral `A`-algebra `A'` finite over `A`. If one sets `S' = Spec(A')`, it then follows
from `(8.10.5)` that there is a neighbourhood `U'` of the generic point `η'` of `S'` such that, if one sets
`X' = X ⊗_A A'`, `Y' = Y ⊗_A A'`, there exists, for every `s' ∈ U'`, a morphism `X'_{s'} → Y'_{s'}` having the property
`Q`. But the morphism `h : S' → S` is finite, hence closed, and since `h⁻¹(η) = {η'}`, `h(U')` contains an open
neighbourhood `U` of `η` in `S`; for every `s ∈ U`, there is therefore `s' ∈ U'` such that `h(s') = s`, and since
`X'_{s'} = X_s ⊗_{k(s)} k(s')`, `Y'_{s'} = Y_s ⊗_{k(s)} k(s')`, the property `P(X_s, Y_s, k(s))` is true for every
`s ∈ U`.

**Example (9.3.6).**

<!-- label: IV.9.3.6 -->

Take for example for `Q` the property of being an isomorphism. Then, by combining `(9.3.5)` and `(9.3.3)`, one has the
following property: the notations and hypotheses being those of `(8.8.1)`, `S_α` being quasi-compact, `X_α` and `Y_α` of
finite presentation over `S_α`, in order that, for every `s ∈ S`, `X_s` and `Y_s` be geometrically isomorphic `(9.1.4)`,
it is necessary and sufficient that there exist `λ ⩾ α` such that, for every `s_λ ∈ S_λ`, `X_{λ, s_λ}` and `Y_{λ, s_λ}`
be geometrically isomorphic.

One has an analogous result when the preschemes one considers are equipped with "composition laws" of a certain kind
`(0_III, 8.2.1)`, for example "preschemes in groups", "preschemes in rings", etc. `(0_III, 8.2.3)`. Then the preceding
statement is still valid when by "isomorphism" one means isomorphisms of preschemes that are *homomorphisms* for the
composition laws considered `(0_III, 8.2.2)`; it suffices here to use not only `(8.10.5)` but also `(8.8.2, (i))`,
remarking that the notion of homomorphism for a composition law is expressed by writing that diagrams of morphisms of
preschemes are commutative (it is of course necessary that the transition morphisms `X_μ → X_λ` and `Y_μ → Y_λ` for
`λ ⩽ μ` be homomorphisms for the composition laws envisaged).

One may also, instead of considering morphisms of preschemes as in `(9.3.5)`, consider homomorphisms of Modules, using
`(9.1.6)` in place of `(9.1.5)`.

<!-- original page 62 -->

### 9.4. Constructibility of certain properties of modules

**Notation (9.4.1).**

<!-- label: IV.9.4.1 -->

*In this number and the following ones up to the end of §9, we shall systematically use the following notation: given a
morphism `f : X → S`, we shall set, for every `s ∈ S`, `X_s = f⁻¹(s) = X ×_S Spec(k(s))`; for every quasi-coherent
`𝒪_X`-Module `ℱ`, `ℱ_s` will denote the `𝒪_{X_s}`-Module `ℱ ⊗_{𝒪_S} k(s)`, and for every homomorphism `u : ℱ → 𝒢` of `ℱ`
into a quasi-coherent `𝒪_X`-Module `𝒢`, `u_s : ℱ_s → 𝒢_s` will be the morphism `p*(u)`, where `p` is the canonical
projection `X_s → X`. For every section `g` of `ℱ` above `X`, one shall denote by `g_s` the image of `g` under the
canonical homomorphism `Γ(X, ℱ) → Γ(X_s, ℱ_s)`. For every part `Z` of `X`, one will denote by `Z_s` the inverse image
`p⁻¹(Z) = Z ∩ X_s` `(I, 3.6.1)`. Finally, if `Y` is a second `S`-prescheme and `h : X → Y` an `S`-morphism, one will
denote by `h_s` the morphism `h × 1 : X_s → Y_s`.*

**Proposition (9.4.2).**

<!-- label: IV.9.4.2 -->

*Let `S` be an integral prescheme of generic point `η`, `f : X → S` a morphism of finite presentation, `ℱ`, `𝒢`, `ℋ`
three quasi-coherent `𝒪_X`-Modules of finite presentation. Let `u : ℱ → 𝒢`, `v : 𝒢 → ℋ` be two homomorphisms of
`𝒪_X`-Modules, and suppose that the sequence `ℱ_η ─u_η→ 𝒢_η ─v_η→ ℋ_η` is exact. Then there exists an open neighbourhood
`U` of `η` in `S` such that, for every `s ∈ U`, the sequence `ℱ_s ─u_s→ 𝒢_s ─v_s→ ℋ_s` is exact.*

With the general notation of `(9.2.1)`, this concerns the relation `P(X, ℱ, 𝒢, ℋ, u, v, k)`: "`X` is an algebraic
prescheme over the field `k`, `ℱ → 𝒢 → ℋ` an exact sequence of quasi-coherent `𝒪_X`-Modules". Since, for every extension
`k'` of `k`, the canonical projection `X_{(k')} → X` is a faithfully flat morphism `(2.2.13)`, condition `(9.2.1, (i))`
is satisfied `(2.2.7)`. By virtue of `(9.2.3)`, one may restrict to the case where `S` is integral and Noetherian, in
which case `X` is Noetherian, and `ℱ`, `𝒢`, `ℋ` are coherent `𝒪_X`-Modules. The hypothesis implies that there exists an
open neighbourhood `U` of `η` in `S` such that the sequence `ℱ|f⁻¹(U) → 𝒢|f⁻¹(U) → ℋ|f⁻¹(U)` is exact, by virtue of
`(8.5.8, (i))` applied following the general method of `(8.1.2, a))`, and one may therefore already suppose that the
sequence `ℱ → 𝒢 → ℋ` is exact; it evidently suffices to prove that one has `Ker(v_s) = (Ker v)_s` and
`Im(u_s) = (Im u)_s` for every `s` close to `η` in `S`; consequently (taking account of the fact that the `𝒪_X`-Modules
`ℱ`, `𝒢`, `ℋ` are coherent and of `(0_I, 5.3.4)`) one is reduced to proving the proposition in the particular case where
the sequence `0 → ℱ → 𝒢 → ℋ → 0` is exact. But then there is an open set `U` in `S` containing `η` and such that
`ℋ|f⁻¹(U)` is flat over `U` `(6.9.1)`; it then follows from `(2.1.8)` that for every `s ∈ U`, the sequence
`0 → ℱ_s → 𝒢_s → ℋ_s → 0` is exact, which completes the proof.

**Corollary (9.4.3).**

<!-- label: IV.9.4.3 -->

*Let `S` be an integral prescheme, of generic point `η`, `f : X → S` a morphism of finite presentation. Let
`ℒ• = (ℒ^i)_{i ∈ ℤ}` be a complex of quasi-coherent `𝒪_X`-Modules of finite presentation. For every `i`, there exists an
open neighbourhood `U` of `η` in `S` such that the canonical homomorphisms*

```text
  (9.4.3.1)        (ℋ^i(ℒ•))_s → ℋ^i(ℒ•_s)
```

*are bijective for every `s ∈ U`.*

<!-- original page 63 -->

One may evidently restrict to a complex with three terms of degrees `−1, 0, +1`: `ℳ ─u→ 𝒩 ─v→ 𝒫` with `v ∘ u = 0`; and
to `i = 0`; the homomorphism to consider is then the canonical homomorphism `(Ker v / Im u)_s → Ker(v_s)/Im(u_s)`. Using
`(8.9.1)` and `(8.5.2, (i))`, one sees that one may reduce to the case where `S` (hence also `X`) is Noetherian, and
consequently `ℳ`, `𝒩`, `𝒫` are coherent `𝒪_X`-Modules; then `Im(u)` and `Ker(v)` are also coherent `(0_I, 5.3.4)` and
moreover there exists a neighbourhood `U` of `η` such that for `s ∈ U`, one has `Ker(v_s) = (Ker(v))_s` and
`Im(u_s) = (Im(u))_s` `(9.4.2)`; the conclusion then results from `(9.4.2)` applied to the exact sequence
`0 → Im(u) → Ker(v) → Ker(v)/Im(u) → 0`, taking account of the fact that `𝒪_η = k(η)` (since `S` is integral) and
consequently the sequence

```text
  0 → (Im u)_η → (Ker v)_η → (Ker v / Im u)_η → 0
```

is exact.

**Proposition (9.4.4).**

<!-- label: IV.9.4.4 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ`, `𝒢`, `ℋ` three quasi-coherent `𝒪_X`-Modules of finite
presentation. Let `u : ℱ → 𝒢`, `v : 𝒢 → ℋ` be two homomorphisms of `𝒪_X`-Modules. Then the set `E` of `s ∈ S` such that
the sequence `ℱ_s ─u_s→ 𝒢_s ─v_s→ ℋ_s` is exact is locally constructible.*

Taking account of `(9.2.3)`, one must establish that the property `P` considered in `(9.4.2)` is constructible. One has
already remarked in the proof of `(9.4.2)` that condition `(9.2.1, (i))` is satisfied for this property, and it remains
to verify condition `(9.2.1, (ii))`. Suppose then that `S` is integral Noetherian, of generic point `η`, and let us
prove that `E` or `S − E` is a neighbourhood of `η`. If `η ∈ E`, our assertion follows from `(9.4.2)`, and one may
therefore restrict to the case where `η ∉ E`, that is, the sequence `ℱ_η ─u_η→ 𝒢_η ─v_η→ ℋ_η` is not exact. Let us
distinguish two cases.

1° Set `w = v ∘ u`, and suppose first that `w_η = v_η ∘ u_η ≠ 0`. Since `ℱ`, `𝒢`, `ℋ` are coherent, the same is true of
`𝒩 = Ker(w)` `(0_I, 5.3.4)`; it then follows from `(9.4.2)` applied to the exact sequence `0 → 𝒩 → ℱ → ℱ` that there is
a neighbourhood `U` of `η` in `S` such that, for `s ∈ S`, `Ker(w_s) = 𝒩_s`; by restricting `S`, one may therefore
suppose this relation verified for every `s ∈ S`. Let `j` be the canonical injection `𝒩 → ℱ`, and set `ℳ = Coker(j)`;
the right-exactness of the functor `ℱ ↦ ℱ_s` entails that `ℳ_s = Coker(j_s)` for every `s ∈ S`. The hypothesis `w_η ≠ 0`
means that `ℳ_η ≠ 0`; since `ℳ` is coherent `(0_I, 5.3.4)`, it follows from `(1.8.6)` that there is an open
neighbourhood `U` of `η` in `S` such that `ℳ_s ≠ 0` for `s ∈ U`, hence `w_s ≠ 0` for `s ∈ U`, and *a fortiori* `S − E`
is a neighbourhood of `η`.

2° Suppose that `w_η = 0`; by virtue of `(8.5.2, (i))`, applied following the general method of `(8.1.2, a))`, there
exists an open neighbourhood `U` of `η` such that `w|f⁻¹(U) = 0`; replacing `S` by `U`, one may already suppose `w = 0`
in `X`. Then `ℱ ─u→ 𝒢 ─v→ ℋ` is a complex with three terms `ℒ•`, to which one may apply `(9.4.3)`; by hypothesis one has
`(ℋ^0(ℒ•))_η = ℋ^0(ℒ•_η) ≠ 0`, and `ℋ^0(ℒ•)` is coherent `(0_I, 5.3.4 and 5.3.3)`, hence it follows from `(1.8.6)` that
there is an open neighbourhood `U` of `η` such that `(ℋ^0(ℒ•))_s ≠ 0` for every `s ∈ U`; but as one may suppose that
`ℋ^0(ℒ•)_s = (ℋ^0(ℒ•))_s` for `s ∈ U` by `(9.4.3)`, one sees again that `S − E` is a neighbourhood of `η` in `S`.

<!-- original page 64 -->

**Corollary (9.4.5).**

<!-- label: IV.9.4.5 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ`, `𝒢` two quasi-coherent `𝒪_X`-Modules of finite presentation,
`u : ℱ → 𝒢` a homomorphism of `𝒪_X`-Modules. Then the set of `s ∈ S` such that `u_s` is injective (resp. surjective,
bijective, zero) is locally constructible.*

It suffices to apply `(9.4.4)` to the sequences `0 → ℱ ─u→ 𝒢`, `ℱ ─u→ 𝒢 → 0`, `0 → ℱ ─u→ 𝒢 → 0`, `ℱ ─u→ 𝒢 ─1_𝒢→ 𝒢`.

**Corollary (9.4.6).**

<!-- label: IV.9.4.6 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. Let `h`
be a section of `ℱ` above `X`; for every `s ∈ S`, let `h_s` be the corresponding section of `ℱ_s` above `X_s` (for the
projection morphism `X_s → X`). Then the set of `s ∈ S` such that `h_s = 0` is locally constructible.*

It suffices to note that `h` corresponds to a homomorphism `u : 𝒪_X → ℱ` `(0_I, 5.1.1)` and `h_s` to the homomorphism
`u_s`.

**Proposition (9.4.7).**

<!-- label: IV.9.4.7 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. The set
`E` (resp. `E'`) of `s ∈ S` such that `ℱ_s` is a locally free `𝒪_{X_s}`-Module (resp. locally free of rank `n`) is
locally constructible.*

If `X` is an algebraic prescheme over a field `k`, `ℱ` a coherent `𝒪_X`-Module, `k'` an extension of `k`, then, for `ℱ`
to be locally free (resp. locally free of rank `n`), it is necessary and sufficient that the same be true of `ℱ ⊗_k k'`,
since the projection `X_{(k')} → X` is a faithfully flat morphism `(2.2.7)`. In other words, condition `(9.2.1, (i))` is
verified for the properties whose constructibility one wishes to prove, and it remains to verify `(9.2.1, (ii))`; one
may therefore again suppose that `S` is affine, Noetherian, and integral. There are once more four cases to envisage.

1° `η ∈ E`. It follows from `(8.5.5)`, applied following the general method of `(8.1.2, a))`, that there exists an open
neighbourhood `U` of `η` in `S` such that `ℱ|f⁻¹(U)` is locally free; *a fortiori* `ℱ_s` is locally free for every
`s ∈ U`.

2° `η ∈ E'`. Same reasoning as in 1°.

3° `η ∈ S − E`. Since `ℱ_η` is a coherent `𝒪_{X_η}`-Module, to say that it is not locally free is equivalent to saying
that it is *not flat* over `𝒪_{X_η}` `(Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of th. 1)`. The fact that
`S − E` is a neighbourhood of `η` will therefore result from the more general lemma below (applied to the case where `g`
is the identity).

**Lemma (9.4.7.1).**

<!-- label: IV.9.4.7.1 -->

*Let `S` be an integral Noetherian prescheme, of generic point `η`, `X`, `Y` two `S`-preschemes of finite type over `S`,
`g : X → Y` an `S`-morphism, `ℱ` a coherent `𝒪_X`-Module. If `ℱ_η` is not `g_η`-flat, then there exists an open
neighbourhood `U` of `η` in `S` such that for every `s ∈ U`, `ℱ_s` is not `g_s`-flat.*

Taking account of `(2.1.2)` and of `Bourbaki, Alg. comm., chap. I, §2, n° 3, Remark 1`, the hypothesis means that there
exists a non-empty open set `V` of `Y_η` and an injective homomorphism `v : ℳ → 𝒩` of coherent `𝒪_V`-Modules, such that
the homomorphism `1 ⊗ v : ℱ_η ⊗_{𝒪_V} ℳ → ℱ_η ⊗_{𝒪_V} 𝒩` is not injective. One has `V = Y_η ∩ W`, where `W` is open in
`Y` `(I, 3.6.1)`, and it follows from `(8.5.2, (i) and (ii))`, applied following the method of `(8.1.2, a))`, that there
exists an open neighbourhood `U_0` of `η` in `S`, two coherent `𝒪_Z`-Modules

<!-- original page 65 -->

`ℳ'`, `𝒩'` (where `Z = W ∩ h⁻¹(U_0)`, `h : Y → S` being the structure morphism) and an `𝒪_Z`-homomorphism `u : ℳ' → 𝒩'`
such that `ℳ'_η = ℳ`, `𝒩'_η = 𝒩` and `v = u_η`; one may therefore suppose `U_0` taken such that for `s ∈ U_0`,
`u_s : ℳ'_s → 𝒩'_s` is injective `(9.4.5)`. But for every `s ∈ U_0`, the homomorphism
`1 ⊗ u_s : ℱ_s ⊗_{𝒪_{Y_s}} ℳ'_s → ℱ_s ⊗_{𝒪_{Y_s}} 𝒩'_s` is none other than `(1 ⊗ u)_s`; the hypothesis that `(1 ⊗ u)_η`
is non-injective therefore entails `(9.4.5)` the existence of a non-empty open set `U ⊂ U_0` such that for every
`s ∈ U`, `(1 ⊗ u)_s` is non-injective, and consequently `ℱ_s` is not `g_s`-flat for every `s ∈ U`.

4° `η ∈ S − E'`. It is clear that `S − E ⊂ S − E'`, and if `η ∈ S − E`, `S − E'` is *a fortiori* a neighbourhood of `η`
by 3°. Suppose therefore that `η ∈ E`, hence `ℱ_η` locally free; these hypotheses entail that `X_η` is disconnected, and
that the ranks of the locally free `𝒪_{X_η}`-Module `ℱ_η` are not the same on the various connected components of `X_η`.
Now it follows from `(8.4.2)`, applied following the method of `(8.1.2, a))`, that one may suppose (replacing `S` by an
open neighbourhood of `η`) that `X` and `X_η` have the same number of connected components, the connected components of
`X_η` being the intersections of `X_η` with the connected components of `X`. The conclusion then results from the
reasoning made in 2°, applied to each of the connected components of `X` (which are finite in number).

**Remark (9.4.7.2).**

<!-- label: IV.9.4.7.2 -->

The lemma `(9.4.7.1)` will be generalized later and freed of Noetherian hypotheses `(11.2.8)`.

**Proposition (9.4.8).**

<!-- label: IV.9.4.8 -->

*Let `S` be a locally Noetherian prescheme, `f : X → S` a morphism of finite type, `ℱ` a coherent `𝒪_X`-Module. Suppose
that for every `s ∈ S`, `X_s` is a locally integral prescheme. Then the set `E` (resp. `E'`) of `s ∈ S` such that `ℱ_s`
is a torsion `𝒪_{X_s}`-Module (resp. a torsion-free `𝒪_{X_s}`-Module) is locally constructible.*

One may evidently suppose `S = Spec(A)` affine and Noetherian and prove that `E` (resp. `E'`) is then constructible by
using the criterion `(0_III, 9.2.3)`; replacing `S` by the reduced closed sub-prescheme of `S` having an irreducible
closed part `Y` of `S` as underlying space, and noting `(I, 3.6.4)` that for `s ∈ Y`, the fibre `(X_{(Y)})_s` identifies
canonically with `X_s` and the sheaf `(ℱ ⊗_{𝒪_S} 𝒪_Y)_s` with `ℱ_s`, one sees that one is reduced to the case where `S`
is integral of generic point `η`, and to proving that `E` or `S − E` (resp. `E'` or `S − E'`) is a neighbourhood of `η`
in `S`. Note moreover that `X` is a finite union of affine open sets `U_i` of finite type over `S`, and each of
`(U_i)_s` is induced on an open set of `X_s`, hence locally integral; in addition, if `(U_i)_η` is empty (resp.
non-empty), one knows that `(U_i)_s` is also empty (resp. non-empty) in a neighbourhood of `η` `(9.2.6)`. One may
therefore suppose all the `(U_i)_η` non-empty and integral, and to say that `ℱ_s` is torsion (resp. torsion-free) is
equivalent to saying that each of the `ℱ_s|(U_i)_s` is torsion (resp. torsion-free). One is therefore reduced to the
case where `X = Spec(B)` is affine, and `ℱ = M̃`, where `M` is a `B`-module of finite type; one sets `B_s = B ⊗_A k(s)`,
`M_s = M ⊗_A k(s)`, and one may suppose `B_η` integral. We have four cases to envisage.

1° `η ∈ E`; `M_η` is then a torsion `B_η`-module of finite type, and there is consequently `h ≠ 0` in `B_η` such that
`hM_η = 0`; by virtue of `(8.5.2, (i))`, applied following the method

<!-- original page 66 -->

of `(8.1.2, a))`, one may (replacing `S` if necessary by a neighbourhood of `η`) suppose that `h ∈ Γ(X_η, 𝒪_{X_η})` is
of the form `g_η`, where `g ∈ Γ(X, 𝒪_X)`; let `u : ℱ → ℱ` be the endomorphism of `ℱ` defined by multiplication by `g`;
by hypothesis, one has `u_η = 0`, hence `(9.4.5)` the endomorphism `u_s : ℱ_s → ℱ_s`, defined by multiplication by
`g_s`, is zero in a neighbourhood of `η`. On the other hand, let `v : 𝒪_X → 𝒪_X` be the endomorphism defined by
multiplication by `g`; since `B_η` is integral and `h = g_η ≠ 0`, `v_η` is injective, and it therefore follows from
`(9.4.5)` that `v_s` is an injective endomorphism of `𝒪_{X_s}` for `s` close to `η`, in other words, `g_s` is an
`𝒪_{X_s}`-regular element for these values of `s`; hence `ℱ_s` is torsion in a neighbourhood of `η`.

2° `η ∈ S − E`. To say that a `B_η`-module `M_η` of finite type is not a torsion module means that its quotient `M_η/T`
by its torsion sub-module is `≠ 0`, and since it is a torsion-free `B_η`-module of finite type, it is isomorphic to a
sub-module of a `B_η`-module `B_η^n`; there is consequently a homomorphism `w : M_η → B_η^n` which is `≠ 0`. Applying
`(8.5.2, (i))` following the method of `(8.1.2, a))`, one deduces (replacing `S` if necessary by a neighbourhood of `η`)
that there exists a homomorphism `v : ℱ → 𝒪_X^n` such that `v_η = w`. The hypothesis `v_η ≠ 0` therefore entails
`(9.4.5)` that `v_s ≠ 0` in a neighbourhood of `η`, and since `X_s` is locally integral, `ℱ_s` is not torsion for these
values of `s`.

3° `η ∈ E'`. Since `M_η` is a torsion-free `B_η`-module of finite type, there exists an injective homomorphism
`w : M_η → B_η^n`. Using `(8.5.2, (i))` and `(9.4.5)` as in 2° (restricting `S` if necessary), one deduces that there
exists a homomorphism `v : ℱ → 𝒪_X^n` such that `v_η = w` and that for `s` close to `η`, `v_s : ℱ_s → 𝒪_{X_s}^n` is
injective; for these values of `s`, `ℱ_s` is therefore torsion-free.

4° `η ∈ S − E'`. Let `T` be the torsion sub-module of `M_η`; by hypothesis `T ≠ 0`, and `T` is of finite type since
`M_η` is Noetherian. Using this time `(8.5.2, (i) and (ii))` one sees (restricting `S` if necessary) that there exists a
coherent `𝒪_X`-Module `𝒢` and an injective homomorphism `u : 𝒢 → ℱ` such that `𝒢_η = T̃` and `u_η` is the canonical
injection `T̃ → ℱ_η`. It then follows from 1° and from `(1.8.6)` that in a neighbourhood of `η`, `𝒢_s` is a torsion
`𝒪_{X_s}`-Module `≠ 0`, and on the other hand it follows from `(9.4.5)` that in a neighbourhood of `η`, `u_s` is
injective. One concludes that in a neighbourhood of `η`, the torsion sub-Module of `ℱ_s` is non-zero. C.Q.F.D.

**Remark (9.4.9).**

<!-- label: IV.9.4.9 -->

The property "`X` is a locally integral algebraic `k`-prescheme" does not verify condition `(9.2.1, (i))`, and it is
therefore not certain that the statement `(9.4.8)` remains valid when one makes no hypothesis on `S` and one supposes
only that `f` is a morphism of finite presentation and `ℱ` an `𝒪_X`-Module of finite presentation. Let us nevertheless
consider the following particular case: `S_0` being a locally Noetherian prescheme, let `f_0 : X_0 → S_0` be a morphism
of finite type, such that the fibres `(X_0)_{s_0}` are locally integral (for every `s_0 ∈ S_0`), and `ℱ_0` a coherent
`𝒪_{X_0}`-Module; let `g : S → S_0` be an arbitrary morphism, set `X = X_0 ×_{S_0} S`, `ℱ = ℱ_0 ⊗_{𝒪_{S_0}} 𝒪_S`,
`f = f_0 × 1_S : X → S`, and suppose that for every `s ∈ S`, the fibre `X_s` is still locally integral. Then the set `E`
(resp. `E'`) of `s ∈ S` such that `ℱ_s` is torsion (resp. torsion-free)

<!-- original page 67 -->

is still locally constructible. Indeed, let `s ∈ S` and let `s_0 = g(s)`; it will suffice (taking into account
`(1.8.2)`) to prove that, for `ℱ_s` to be torsion (resp. torsion-free), it is necessary and sufficient that
`(ℱ_0)_{s_0}` be so. Now, `Supp(ℱ_s)` is the inverse image of `Supp((ℱ_0)_{s_0})` by the projection
`p : X_s → (X_0)_{s_0}` `(I, 9.1.13)`; since `p` is faithfully flat and quasi-compact, to say that `Supp(ℱ_s)` contains
a maximal point of `X_s` is equivalent to saying that `Supp((ℱ_0)_{s_0})` contains a maximal point of `(X_0)_{s_0}`
`(1.1.5 and 2.3.4)`; whence our assertion concerning the set `E` `(I, 7.4.6)`. If the torsion sub-Module `𝒯` of
`(ℱ_0)_{s_0}` is non-zero, `𝒯 ⊗_{k(s_0)} k(s)` (which is torsion by what precedes) is non-zero and identifies with a
sub-Module of `ℱ_s` `(2.2.7)`, hence the torsion sub-Module of `ℱ_s` is non-zero. Finally, if `(ℱ_0)_{s_0}` is
torsion-free, one may suppose (by considering an affine open set of `(X_0)_{s_0}`) that `(ℱ_0)_{s_0}` is isomorphic to a
sub-Module of a `𝒪_{(X_0)_{s_0}}^n`, hence `ℱ_s` is isomorphic to a sub-Module of an `𝒪_{X_s}^n` `(2.2.7)`, and this
establishes our assertion concerning `E'`.

### 9.5. Constructibility of topological properties

**Proposition (9.5.1).**

<!-- label: IV.9.5.1 -->

*Let `f : X → S` be a morphism of finite presentation, `Z` a locally constructible part of `X`. Then the set `E` of
`s ∈ S` such that `Z_s ≠ ∅` is locally constructible.*

Indeed, one has `E = f(Z)`, and it suffices to apply Chevalley's theorem `(1.8.4)`.

**Corollary (9.5.2).**

<!-- label: IV.9.5.2 -->

*If `Z'`, `Z''` are two locally constructible parts of `X`, the set of `s ∈ S` such that `Z'_s ⊂ Z''_s` (resp.
`Z'_s = Z''_s`) is locally constructible.*

Indeed, the relation `Z'_s ⊂ Z''_s` is equivalent to `(Z' ∩ (∁ Z''))_s = ∅`, and `Z' ∩ ∁ Z''` is locally constructible.

**Proposition (9.5.3).**

<!-- label: IV.9.5.3 -->

*Let `f : X → S` be a morphism of finite presentation, `Z`, `Z'` two locally constructible parts of `X` such that
`Z ⊂ Z'`. Then the set `E` of `s ∈ S` such that `Z_s` is dense in `Z'_s` is locally constructible in `S`.*

One must verify the two conditions of `(9.2.2, (ii))`. As for the first, consider an algebraic prescheme `X` over a
field `k`, two constructible parts `Z`, `Z'` of `X` such that `Z ⊂ Z'`, and an extension `k'` of `k`. Then the canonical
projection `p : X_{(k')} → X` is a faithfully flat and quasi-compact morphism, and one therefore has
`p⁻¹(‾Z) = ‾{p⁻¹(Z)}` and `p⁻¹(‾Z') = ‾{p⁻¹(Z')}` by virtue of `(2.3.10)`; since `p` is surjective, the relation
`‾Z = ‾Z'` is equivalent to `‾{p⁻¹(Z)} = ‾{p⁻¹(Z')}`.

Let us now verify the second condition, and suppose therefore `S` affine, Noetherian, and integral, of generic point
`η`. Let us distinguish two cases.

1° `η ∈ S − E`, in other words, `Z_η` is not dense in `Z'_η`; there exists therefore in `X` an open set `V` such that
`V ∩ Z_η = ∅` and `V ∩ Z'_η ≠ ∅`. As `X` is Noetherian, `V` is locally constructible, hence so is `V ∩ Z`, and by virtue
of `(9.5.1)`, there is a neighbourhood `U` of `η` in `S` such that for every `s ∈ U`, one has `(V ∩ Z)_s = ∅` and
`(V ∩ Z')_s ≠ ∅`; this entails that `Z_s` is not dense in `Z'_s` for `s ∈ U`, in other words `U ⊂ S − E`.

<!-- original page 68 -->

2° `η ∈ E`, hence `Z_η` is dense in `Z'_η`. Let us first show that one may suppose `Z'` closed. Indeed, `Z_η` is dense
in `‾{Z'_η}` (closure taken in `X_η`); set `V_η = X_η − ‾{Z'_η}`, which is open in `X_η` and does not meet `Z_η`; one
may suppose `V_η` of the form `V ∩ X_η`, where `V` is open (hence constructible) in `X`, and the hypothesis
`V_η ∩ Z'_η = ∅` then entails `V_s ∩ Z'_s = ∅` for every `s` close to `η` by virtue of `(9.5.1)`. Replacing `S` by an
open neighbourhood of `η`, one may therefore suppose that `V ∩ Z' = ∅`, hence `V ∩ ‾Z' = ∅` (closure taken in `X`), and
consequently `(‾Z')_η = ‾{Z'_η}`, whence our assertion. The set `‾Z'` is then the union of its irreducible components in
finite number, and by restricting `S` again to a neighbourhood of `η`, one may suppose that all the irreducible
components `Z'_i` of `‾Z'` meet `X_η`, whence it follows that `X_η` contains the generic points of the `Z'_i`
`(0_I, 2.1.8)`. To say that `Z_s` is dense in `Z'_s` is then equivalent to saying that each of the `(Z ∩ Z'_i)_s` is
dense in `(Z'_i)_s`, and one is thus reduced to the case where `‾Z'` is irreducible. Replacing then if necessary `X` by
the reduced sub-prescheme having `‾Z'` as underlying space, one sees that one may suppose that `Z' = X` and that `X` is
integral and dominates `S`. Finally, by covering `X` by a finite number of affine open sets `W_j` and replacing `Z` by
`Z ∩ W_j`, one may suppose that `X = Spec(A)`, where `A` is an integral Noetherian ring. Since `X_η` is integral
Noetherian and `Z_η` is constructible in `X_η` and dense in `X_η`, `Z_η` contains a non-empty open set of `X_η`
`(0_III, 9.2.2)`, which one may suppose of the form `(D(t))_η`, where `t` is an element `≠ 0` of `A`. Replacing `S` if
necessary by a neighbourhood of `η`, one may moreover, by virtue of the relation `(D(t))_η ⊂ Z_η`, suppose that
`D(t) ⊂ Z` `(9.5.2)`. Finally, since the homothety of ratio `t` in `𝒪_X` is injective, it follows from `(9.4.5)` that
for `s` close to `η`, `t_s` is `𝒪_{X_s}`-regular, hence `(X_s)_{t_s}` is dense in `X_s`, and *a fortiori* the same is
true of `Z_s`, which contains `(X_s)_{t_s}`.

**Corollary (9.5.4).**

<!-- label: IV.9.5.4 -->

*Let `f : X → S` be a morphism of finite presentation, `Z` a locally constructible part of `X`. The set `E` of `s ∈ S`
such that `Z_s` is closed (resp. open, resp. locally closed) in `X_s` is locally constructible in `S`.*

To say that `Z_s` is open in `X_s` means that `(X − Z)_s = X_s − Z_s` is closed in `X_s`, and since `X − Z` is locally
constructible, one may restrict to considering the set of `s ∈ S` such that `Z_s` is closed and the set of `s ∈ S` such
that `Z_s` is locally closed.

Let us verify in each case the two conditions of `(9.2.2, (ii))`. The first results from the fact that
`p : X_{(k')} → X` is faithfully flat and quasi-compact, and from `(2.3.12)` and `(2.3.14)`. Let us therefore verify the
second condition, `S` being supposed affine, Noetherian, and integral, of generic point `η`. Set `Z' = ‾Z`; the same
reasoning as in `(9.5.3)` shows that `Z'_η` is equal to the closure of `Z_η` in `X_η`; by virtue of `(9.5.3)`, there is
therefore a neighbourhood `U` of `η` such that for `s ∈ U`, `Z_s` is dense in `Z'_s`, the latter being closed in `X_s`.
To say that `Z_s` is closed in `X_s` then means that `Z''_s = ∅`, where `Z'' = Z' − Z`; it therefore follows from
`(9.5.1)` that the set `E` of `s ∈ S` where `Z''_s = ∅` is such that `E` or `S − E` contains a neighbourhood of `η`. To
say that `Z_s` is locally closed in `X_s` means that `Z''_s` is closed in `X_s`; it therefore suffices to apply the
preceding result, replacing `Z` by `Z''`, which is locally constructible in `X`.

<!-- original page 69 -->

**Proposition (9.5.5).**

<!-- label: IV.9.5.5 -->

*Let `f : X → S` be a morphism of finite presentation, `Z` a locally constructible part of `X` such that, for every
`s ∈ S`, `Z_s` is locally closed in `X_s`. For every `s ∈ S`, let `D(s) ⊂ ℤ ∪ {−∞}` be the set of dimensions of the
irreducible components of `Z_s`. Then the function `s ↦ D(s)` is locally constructible in `S`.*

Let `Φ` be a finite part of `ℤ ∪ {−∞}`; one must show that the set of `s ∈ S` such that `D(s) = Φ` is locally
constructible; taking account of `(9.2.3)`, we still have to verify the two conditions of `(9.2.2, (ii))`.

As for the first, one must see that if `X` is an algebraic prescheme over a field `k`, `Z` a locally closed part of `X`,
`k'` an extension of `k`, `p : X_{(k')} → X` the canonical projection, then the set of dimensions of the irreducible
components of `Z` is the same as that of the dimensions of the irreducible components of `p⁻¹(Z)`; taking account of the
existence of a sub-prescheme of `X` having `Z` as underlying space `(I, 5.2.1)`, this results from `(4.2.8)`.

For the second condition of `(9.2.2, (ii))`, one is in the case where `S` is Noetherian and integral of generic point
`η`, and `f : X → S` is a morphism of finite type, so that `X` is Noetherian. The sub-space `Z_η` of the Noetherian
space `X_η` is by hypothesis locally closed, hence has a finite number of irreducible components `Z_{iη}`, which are
locally closed in `X_η`. There exists consequently for each index `i` a locally closed part `Z_i` of `X` such that
`(Z_i)_η = Z_{iη}`, hence if `Z' = ⋃_i Z_i`, one has `Z'_η = Z_η`. But since `Z` and `Z'` are locally constructible, one
may, by replacing `S` by a neighbourhood of `η`, suppose that `Z' = Z` `(9.5.1)`. Moreover, for `i ≠ j`,
`Z_{iη} ∩ Z_{jη}` is rare and closed in `Z_{iη}`; hence `(9.5.3 and 9.5.4)`, one may suppose again, by restricting `S`,
that for `j ≠ i`, `(Z_i)_s ∩ (Z_j)_s` is rare and closed in `(Z_i)_s`. Since `Z_i` is locally closed in `X`, there is a
sub-prescheme of `X` having `Z_i` as underlying space (still denoted `Z_i`), which is of finite type over `S`
`(I, 6.3.5)`. Set `U_i = Z_i − ⋃_{j ≠ i}(Z_i ∩ Z_j)`, which is open in `Z` and such that, for every `s ∈ S`, `(U_i)_s`
is open everywhere-dense in `(Z_i)_s`; moreover, by construction, the `U_i` are pairwise disjoint. Since `(Z_i)_s` is an
algebraic `k(s)`-prescheme, the set of dimensions of the irreducible components of `Z_s = ⋃_i (Z_i)_s` is the same as
the set of dimensions of the irreducible components of the union of the `(U_i)_s` `(4.1.1.3)`, each of these components
being already an irreducible component of one of the `(U_i)_s`. One may therefore restrict to the case where `Z = U_i`;
moreover, since `Z_η` is then irreducible, there is only one irreducible component of `‾Z` meeting `X_η` `(0_I, 2.1.8)`,
and one may evidently, by restricting `Z`, suppose `Z` irreducible. One is finally reduced to proving the following
particular case of `(9.5.5)`.

**Corollary (9.5.6).**

<!-- label: IV.9.5.6 -->

*Let `S` be a Noetherian and irreducible prescheme of generic point `η`, `X` an irreducible prescheme, `f : X → S` a
dominant morphism of finite type. Then there exists a neighbourhood `U` of `η` in `S` such that, for every `s ∈ U`, all
the irreducible components of `X_s` are of dimension `n = dim(X_η)`.*

One may evidently restrict to the case where `S = Spec(A)` is affine, `A` being therefore Noetherian; replacing `f` by
`f_red`, which is of finite type `(1.5.4, (vi))`, one may

<!-- original page 70 -->

suppose `A` integral and `X` reduced, hence integral since it is irreducible. One knows `(4.1.2)` that there exists a
dense open set `W` in `X_η` and a finite surjective `k(η)`-morphism `h : W → 𝐕((k(η))^n) = Spec(B')`, where
`B' = k(η)[T_1, …, T_n]` (`T_i` indeterminates). If `V` is an open set of `X` such that `V ∩ X_η = W`, one knows
`(9.5.3)` that for `s` close to `η` in `S`, `V_s` is a dense open set in `X_s`, and one may consequently `(4.1.1.3)`
restrict to the case where `V = X`, `W = X_η`. Set `B = A[T_1, …, T_n]` and `Y = Spec(B) = 𝐕^n_A`, so that
`Spec(B') = Y_η`; it follows from `(8.8.2, (i))` and `(8.10.5, (vi) and (x))`, applied following the method of
`(8.1.2, a))`, that by replacing `S` if necessary by a neighbourhood of `η`, one may suppose that `h = g_η`, where
`g : X → Y` is a finite surjective morphism; in other words, one has `X = Spec(C)`, where `C` is a finite `B`-algebra
and the homomorphism `B → C` corresponding to `g` is *injective*; since `C` is an integral ring, `C` is therefore a
torsion-free `B`-module of finite type, and `C_η = C ⊗_A k(η)` is therefore a torsion-free module of finite type over
`B_η = B ⊗_A k(η) = k(η)[T_1, …, T_n]` (being a module of fractions whose denominators are in `A − {0} ⊂ B − {0}`). It
therefore follows from `(9.4.8)` that there is a neighbourhood `U` of `η` in `S` such that for `s ∈ U`,
`C_s = C ⊗_A k(s)` is a torsion-free module of finite type over `B_s = B ⊗_A k(s) = k(s)[T_1, …, T_n]`, and in
particular the homomorphism `g_s : B_s → C_s` is injective. Since no element of `B_s` is a zero-divisor in `C_s`, for
every minimal prime ideal `𝔭_i` of `C_s` (whose elements are zero-divisors in `C_s`), one has necessarily
`𝔭_i ∩ B_s = 0`, hence the canonical homomorphism `B_s → C_s/𝔭_i` is injective. One deduces that for each irreducible
component `Z_i = Spec(C_s/𝔭_i)` of `X_s`, the restriction to `Z_i` of `g_s` is a finite and dominant morphism
`Z_i → Y_s`, hence surjective `(II, 6.1.10)`. One concludes by `(4.1.2)` that `dim(Z_i) = n`, which completes the proof.

**Remark (9.5.7).**

<!-- label: IV.9.5.7 -->

One will take care to note that under the hypotheses of `(9.5.6)` it may happen that `X_s` is irreducible for no `s ≠ η`
in a neighbourhood of `η`; in other words, the property "`X` is an irreducible algebraic `k`-prescheme" is not
constructible. Take for example `S = Spec(k[T])`, where `k` is an algebraically closed field, `T` an indeterminate; one
therefore has `k(η) = K = k(T)`. Let `L` be a finite separable extension of `K` of degree `> 1`, and let `X` be the
integral closure of `S` in `L` `(II, 6.3.4)`; one has therefore `X = Spec(B)`, where `B` is the integral closure of
`k[T]` in `L`. One knows that `B` is a Dedekind ring, and that all the maximal ideals of `k[T]`, except a finite number,
are unramified in `B`; since in addition the residue field of every maximal ideal of `B` is necessarily `k` (since it is
a finite extension of `k`), one sees that for almost all the maximal ideals `𝔧_s` of `k[T]`, `B_s = B/𝔧_s B` is a direct
sum of `[L : K]` fields isomorphic to `k`, in other words `X_s` is not irreducible, although `X_η = Spec(L)` is.

The same example shows that the property "`X` is an integral algebraic `k`-prescheme" is not constructible. Finally, the
same is true of the property "`X` is a reduced algebraic `k`-prescheme". To see this it suffices to take again
`S = Spec(k[T])`, where this time `k` is an algebraically closed field of characteristic `p > 0`, and for `X` the
integral closure of `S` in `L = K^{1/p}` (where `K = k(T)`), so that `X = Spec(B)` with `B = k[T^{1/p}]` (`k` being
perfect); every maximal ideal of `k[T]` is of the form `(T − α)` with `α ∈ k`; the unique ideal of `B` above the ideal
`(T − α)` is the principal ideal `(T^{1/p} − α^{1/p})` and it is immediate

<!-- original page 71 -->

that the quotient ring `B/(T − α)B` consequently admits nilpotent elements; in other words, `X_s` is reduced for no
`s ≠ η`, while `X_η = Spec(L)` is integral.

We shall see a little further on `(9.7)` that one obtains by contrast constructible properties when one considers the
"geometric" notions corresponding to the notions of irreducible, reduced, or integral prescheme `(4.5 and 4.6)`.

### 9.6. Constructibility of certain properties of morphisms

**Proposition (9.6.1).**

<!-- label: IV.9.6.1 -->

*Let `X`, `Y` be two `S`-preschemes of finite presentation, `f : X → Y` an `S`-morphism. Let `E` be the set of `s ∈ S`
for which `f_s` has one of the following properties: to be:*

*(i) surjective;*

*(ii) dominant;*

*(iii) separated;*

*(iv) proper;*

*(v) radicial;*

*(vi) finite;*

*(vii) quasi-finite;*

*(viii) an immersion;*

*(ix) a closed immersion;*

*(x) an open immersion;*

*(xi) an isomorphism;*

*(xii) a monomorphism.*

*Then `E` is locally constructible in `S`.*

The assertions of (i), (v) and (vii) are inserted only for the record, having already been established in `(9.3.2)`.

(ii): Note first that `f` is of finite presentation `(1.6.2, (v))`, hence, by virtue of Chevalley's theorem `(1.8.4)`,
`f(X)` is locally constructible in `Y`. On the other hand, one has `f_s(X_s) = (f(X))_s` `(I, 3.6.1)`; the set of `s`
such that `f_s` is dominant is the set of `s` such that `(f(X))_s` is dense in `Y_s`; the conclusion therefore results
in this case from `(9.5.3)`.

(iii): Since `f : X → Y` is of finite presentation, the diagonal immersion `Δ_f : X → X ×_Y X` is of finite presentation
`(1.6.2, (iv) and (v))`; it follows from `(1.8.4.1)` that `Δ_f(X) = Δ_X` is a locally constructible part of `X ×_Y X`.
To say that `f_s` is separated means (taking into account `(I, 5.3.4)`) that `(Δ_X)_s` is closed in
`X_s ×_{Y_s} X_s = (X ×_Y X)_s`; the conclusion therefore results here from `(9.5.4)`.

(iv): Let us show that the property "`X` and `Y` are algebraic preschemes over a field `k`, and `f : X → Y` is a proper
`k`-morphism" is constructible. Condition `(9.2.1, (i))` is verified by virtue of `(2.7.1, (vii))`. One may therefore
restrict to the case where `S` is affine, Noetherian, and integral, of generic point `η`, and one must prove that `E` or
`S − E` is a neighbourhood of `η`. Suppose first that `η ∈ E`; it follows from `(8.10.5, (xii))` applied following the
method of `(8.1.2, a))` that, by replacing `S` by a neighbourhood of `η`, one may

<!-- original page 72 -->

suppose that `f` is itself a proper morphism; one then knows that the same is true of `f_s` for every `s ∈ S`
`(II, 5.4.2, (iii))`. Suppose on the contrary that `η ∈ S − E`, and let us distinguish two cases.

1° Suppose that `f_η` is not separated; then it follows from (iii) that `f_s` is non-separated (and *a fortiori* not
proper) in a neighbourhood of `η`.

2° Suppose `f_η` separated; `Y` is a finite union of affine open sets `V_i`, and for `f_s` to be proper, it is necessary
and sufficient that each of its restrictions `f_s⁻¹((V_i)_s) → (V_i)_s` be so `(II, 5.4.1)`; one may therefore restrict
to the case where `Y` is affine, hence a scheme. To say that `f_η` is not proper means `(II, 5.6.3)` that there exists a
morphism of finite type `h : Z → Y_η` such that the morphism `(f_η)_{(Z)} : X_η ×_{Y_η} Z → Z` is not closed. As `Y` is
a scheme, one deduces from `(8.8.2, (i) and (ii))` (by restricting `S` if necessary to a neighbourhood of `η`) that
there exists a morphism of finite type `g : Y' → Y` such that `Z` is isomorphic to `Y'_η` and `g_η = h`; if one sets
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`, one has `(f_η)_{(Z)} = f'_η`, and by hypothesis there exists therefore a
closed part `M'` of `X'_η` such that `f'_η(M')` is not closed in `Y'_η`. Now `M'` is the trace on `X'_η` of a closed
part `N'` of `X'`; since `X'` is Noetherian and `f'` of finite type, `f'(N')` is constructible in `Y'` `(1.8.4)`, and by
hypothesis `(f'(N'))_η = f'_η(N'_η) = f'_η(M')` is not closed in `Y'_η`. One then concludes from `(9.5.4)` that there
exists a neighbourhood `U` of `η` in `S` such that for `s ∈ U`, `(f'(N'))_s = f'_s(N'_s)` is not closed in `Y'_s`; in
other words, the morphism `f'_s` is not closed, and *a fortiori* the morphism `f_s` is not proper.

(vi): The property is the conjunction of properties (iv) and (vii) `(8.11.1)`, hence the proposition results in this
case from what has already been proved.

(ix): The verification of condition `(9.2.1, (i))` results from `(2.7.1, (xi))`. One may therefore restrict to the case
where `S` is affine, Noetherian, and integral of generic point `η`, and to proving that `E` or `S − E` is a
neighbourhood of `η`. If `η ∈ E`, one may (by replacing `S` by a neighbourhood of `η`) suppose that `f` is a closed
immersion by virtue of `(8.10.5, (iv))`, and then it is clear that `f_s` is a closed immersion for every `s ∈ S`
`(I, 4.3.2)`. Suppose therefore that `η ∈ S − E` and let us distinguish two cases.

1° `f_η` is not a finite morphism. Then it follows from (vi) that in a neighbourhood of `η`, `f_s` is not finite, nor *a
fortiori* a closed immersion.

2° `f_η` is finite; then, by virtue of `(8.10.5, (x))`, one may suppose (by restricting `S` if necessary) that `f`
itself is a finite morphism. In this case `𝒜 = 𝒜(X) = f_*(𝒪_X)` is a coherent `𝒪_Y`-Module `(II, 6.1.3)` and `f = 𝒜(u)`,
where `u : 𝒪_Y → 𝒜` is a homomorphism of `𝒪_Y`-Algebras `(II, 1.1.2)`; since `f_η` is not a closed immersion by
hypothesis, `u_η` is not surjective `(II, 1.4.10)`, hence `(9.4.5)` there is a neighbourhood of `η` in which `u_s` is
not surjective, and consequently `(I, 4.2.3)` `f_s` is not a closed immersion.

(viii): The verification of condition `(9.2.1, (i))` is done as in (ix), this time using `(2.7.1, (x))` and the fact
that every immersion of a Noetherian prescheme into another is quasi-compact. One is therefore reduced to the case where
`S` is affine, Noetherian, and integral of generic point `η`, and to proving that `E` or `S − E` is a neighbourhood of
`η`. If `η ∈ E`, one concludes as in (ix) by means of `(8.10.5, (ii))`. If `η ∈ S − E`, one distinguishes once again two
cases.

<!-- original page 73 -->

1° `f_η(X_η)` is not a locally closed part of `Y_η`. As `f(X)` is constructible in `Y` `(1.8.4)` and
`f_s(X_s) = (f(X))_s`, one deduces from `(9.5.4)` that for `s` close to `η`, `f_s(X_s)` is not locally closed in `Y_s`,
and *a fortiori* `f_s` is not an immersion.

2° `f_η(X_η)` is locally closed in `Y_η`. As `f(X)` is constructible in `Y` `(1.8.4)`, and the same is true of `‾{f(X)}`
since `Y` is Noetherian, it follows from `(8.3.11)` that by restricting `S` if necessary, one may suppose that `f(X)` is
locally closed in `Y`. There is then an open set `V` of `Y` containing `f(X)` and in which `f(X)` is closed. Since `Y`
is Noetherian, `V` is of finite type over `S`, and by replacing `Y` by `V`, one may therefore reduce to the case where
`f(X)` is closed in `Y`. But then `f_s(X_s) = (f(X))_s` is closed in `Y_s` for every `s ∈ S`, and to say that `f_s` is
an immersion is equivalent to saying that `f_s` is a closed immersion; one is therefore reduced to what was proved in
(ix).

(x): Using this time `(2.7.1, (ix))` and `(8.10.5, (iii))`, one is reduced to the case where `S` is affine, Noetherian,
integral of generic point `η`, and where `η ∈ S − E`. Let us distinguish three cases.

1° `f_η(X_η)` is not open in `Y_η`. As `f(X)` is constructible in `Y` `(1.8.4)`, one deduces from `(9.5.4)` that
`f_s(X_s)` is not open in `Y_s` for `s` close to `η`, and *a fortiori* `f_s` is not an open immersion.

2° `f_η(X_η)` is open in `Y_η` but `f_η` is not an immersion. It then follows from (viii) that for `s` close to `η` in
`S`, `f_s` is not an immersion, nor *a fortiori* an open immersion.

3° `f_η(X_η)` is open in `Y_η` and `f_η` is an immersion. As `f(X)` is constructible in `Y`, it follows from `(8.3.11)`
that by restricting `S` if necessary, one may already suppose that `f(X)` is open in `Y`. Since `Y` is Noetherian, the
sub-prescheme induced on `f(X)` is of finite type over `S`, so one may reduce to the case where `f` is *surjective* by
replacing `Y` by `f(X)`. By hypothesis, `f_η` is a closed immersion, hence one may, as in (ix), suppose that `f` is a
closed immersion, and consequently that `X` is a closed sub-prescheme of `Y` defined by a coherent Ideal `𝒥` of `𝒪_Y`.
By hypothesis `f_η` is not an isomorphism, hence `𝒥_η ≠ 0`; one concludes `(9.4.5)` that in a neighbourhood of `η`, one
has `𝒥_s ≠ 0`, and consequently the surjective closed immersion `f_s` is not open.

(xi): The property is the conjunction of properties (i) and (x) and therefore results from what has been proved.

(xii): By virtue of `(I, 5.3.8)`, to say that `f_s` is a monomorphism means that
`Δ_{f_s} = (Δ_f)_s : X_s → X_s ×_{Y_s} X_s = (X ×_Y X)_s` is an isomorphism, and since `X ×_Y X` is an `S`-prescheme of
finite presentation `(1.6.2, (iv))`, the conclusion results from (xi).

**Proposition (9.6.2).**

<!-- label: IV.9.6.2 -->

*Let `X`, `Y` be two `S`-preschemes of finite presentation, `f : X → Y` an `S`-morphism.*

*I) Let `E` be the set of `s ∈ S` for which `f_s` has one of the following properties: to be:*

*(i) affine;*

*(ii) quasi-affine;*

*(iii) projective;*

*(iv) quasi-projective.*

*Then `E` is ind-constructible in `S`.*

<!-- original page 74 -->

*II) Let `ℒ` be an invertible `𝒪_X`-Module. Then the set `E'` of `s ∈ S` such that `ℒ_s` is an ample (resp. very ample)
`𝒪_{X_s}`-Module relative to `f_s` is ind-constructible in `S`.*

I) Let us verify conditions (i) and (ii) of `(9.2.1)`. As regards condition `(9.2.1, (i))`, it results, for properties
(i) and (ii), from `(2.7.1, (xiii) and (xiv))`; for properties (iii) and (iv), it results from `(9.1.5)`. Let us then
verify condition `(9.2.1, (ii))`, supposing therefore `S` Noetherian, integral and of generic point `η`, and that
`f_η : X_η → Y_η` has one of the properties (i) to (iv) of the statement. Applying
`(8.10.5, (viii), (ix), (xiii) and (xiv))` following the method of `(8.1.2, a))`, one sees first that there exists an
open neighbourhood `U` of `η` such that, if `V` and `W` are the inverse images of `U` in `X` and `Y` respectively by the
structure morphisms, the restriction `V → W` of `f` has that one of the properties (i) to (iv) that one considers. The
conclusion then results from the fact that these properties are all stable under base change.

II) One proceeds in the same way. Condition `(9.2.1, (i))` results this time from `(2.7.2)`. For condition
`(9.2.1, (ii))`, with the same notation as in I), it follows from `(8.10.5.2)` that for a neighbourhood `U` of `η` in
`S`, the restriction `ℒ|V` is ample (resp. very ample) relative to the restriction `V → W` of `f`. The conclusion
results again from the stability of the properties considered under base change `(II, 4.6.13 and 4.4.10)`.

One may improve `(9.6.2, II))` under certain conditions.

**Proposition (9.6.3).**

<!-- label: IV.9.6.3 -->

*Let `X`, `Y` be two `S`-preschemes of finite presentation, `f : X → Y` a *proper* `S`-morphism, `ℒ` an invertible
`𝒪_X`-Module. Then the set `E` (resp. `E'`) of `s ∈ S` such that `ℒ_s` is an ample (resp. very ample) `𝒪_{X_s}`-Module
relative to `f_s : X_s → Y_s` is locally constructible in `S`.*

Let `k` be a field, `Z`, `T` two algebraic preschemes over `k`, `ℳ` an invertible `𝒪_Z`-Module, `g : Z → T` a
`k`-morphism of finite type; then, if `P(Z, T, ℳ, g, k)` denotes the relation "`ℳ` is ample (resp. very ample) relative
to `g`", one has already remarked in `(9.6.2)` that `P(Z, T, ℳ, g, k)` satisfies condition `(9.2.1, (i))` by virtue of
`(2.7.2)`. One already knows on the other hand that `E` and `E'` are ind-constructible. It remains therefore to see that
if `S` is Noetherian, integral, of generic point `η` and if `η ∈ S − E` (resp. `η ∈ S − E'`), then `S − E` (resp.
`S − E'`) contains a neighbourhood of `η`. We shall consider separately the case of `E'` and that of `E`.

I) **Case of `E'`.** Note that since `f` is separated and `Y` quasi-compact, there exists an integer `h` such that for
`q > h`, one has `R^q f_*(ℒ) = 0` `(III, 1.4.12)`; on the other hand, since `f` is proper and `Y` Noetherian, the
`R^q f_*(ℒ)` are all coherent `𝒪_Y`-Modules `(III, 3.2.1)`; since they are zero except for a finite number of values of
`q`, the generic flatness theorem `(6.9.1)` shows that by restricting `S` to a neighbourhood of `η`, one may suppose
that `ℒ` and the `R^q f_*(ℒ)` are all `S`-flat. One then concludes from `(III, 6.9.9)` that the canonical homomorphism

```text
  (9.6.3.1)        f_*(ℒ) ⊗_{𝒪_S} k(s) → (f_s)_*(ℒ_s)
```

*is an isomorphism*.

<!-- original page 75 -->

This being so, it follows from `(II, 4.4.4)` that to say `ℒ_s` is not very ample relative to `f_s` means: either the
canonical homomorphism `(f_s)*((f_s)_*(ℒ_s)) → ℒ_s` is not surjective; or the preceding homomorphism is surjective and
the canonical morphism `r : X_s → 𝐏((f_s)_*(ℒ_s))` is not an immersion. Taking into account the isomorphism `(9.6.3.1)`,
these conditions are written respectively in the form: 1° the canonical homomorphism `(f*(f_*(ℒ)))_s → ℒ_s` is not
surjective; 2° the preceding homomorphism is surjective and the canonical morphism `X_s → 𝐏((f_*(ℒ))_s)` is not an
immersion.

Suppose first that the canonical homomorphism `(f*(f_*(ℒ)))_η → ℒ_η` is not surjective. Since `f_*(ℒ)` is coherent, the
same is true of `f*(f_*(ℒ))`, and then it follows from `(9.4.5)` that for every `s` in a neighbourhood of `η`, the
homomorphism `(f*(f_*(ℒ)))_s → ℒ_s` is not surjective, which proves in this case that `S − E'` is a neighbourhood of
`η`.

Suppose secondly that the canonical homomorphism `(f*(f_*(ℒ)))_η → ℒ_η` is surjective but that the morphism
`X_η → 𝐏((f_*(ℒ))_η)` is not an immersion. Then the same reasoning as above shows first that for every `s` sufficiently
close to `η`, the homomorphism `(f*(f_*(ℒ)))_s → ℒ_s` is surjective; on the other hand, by virtue of `(9.6.1, (viii))`,
for `s` sufficiently close to `η`, the morphism `X_s → 𝐏((f_*(ℒ))_s)` is not an immersion. This completes the proof in
the case of `E'`.

II) **Case of `E`.** Let us first consider the particular case where `Y = S`.

**Corollary (9.6.4).**

<!-- label: IV.9.6.4 -->

*Let `f : X → S` be a proper morphism of finite presentation, `ℒ` an invertible `𝒪_X`-Module. Then the set `E` of
`s ∈ S` such that `ℒ_s` is ample (relative to `f_s`) is open in `S`, and `ℒ|f⁻¹(E)` is ample relative to the restriction
`f⁻¹(E) → E` of `f`.*

Since condition `(9.2.1, (i))` is verified by the property `P` defined above, the result of `(9.2.2, (iv))` and the
reasoning of `(9.2.3)` show that one may restrict to the case where `S` is Noetherian; but then the result follows from
`(III, 4.7.1)` and from the stability of ampleness under base change `(II, 4.6.13)`.

**Corollary (9.6.5).**

<!-- label: IV.9.6.5 -->

*Under the hypotheses of `(9.6.4)`, in order that `ℒ` be ample relative to `f`, it is necessary and sufficient that, for
every `s ∈ S`, `ℒ_s` be ample relative to `f_s`.*

**(9.6.6) End of the proof of `(9.6.3)`.**

<!-- label: IV.9.6.6 -->

Let us return to the general case, `S` being Noetherian, integral and of generic point `η ∈ S − E`. Since `f` is proper,
it follows from `(9.6.4)` that the set `V` of `y ∈ Y` such that `ℒ_y` is an ample `𝒪_{X_y}`-Module, relative to the
morphism `f_y : X_y → Spec(k(y))`, is open, hence `F = Y − V` is closed in `Y`. This being so, since `f_s` is proper and
that, for every `y ∈ Y` above `s ∈ S`, one has `ℒ_y = (ℒ_s)_y`, it follows from `(9.6.5)` that for `s` to belong to
`S − E`, it is necessary and sufficient that one have `F_s ≠ ∅`. But since `F` is closed in `Y` and `F_η ≠ ∅`, it
follows from `(9.5.1)` that the set of `s ∈ S` such that `F_s ≠ ∅` is a neighbourhood of `η` in `S`. C.Q.F.D.

**Remarks (9.6.7).**

<!-- label: IV.9.6.7 -->

(i) For each of the properties `P` considered in `(9.6.1)`, proposition `(9.3.3)` is applicable, and these properties
(for the morphisms `f_s`) are therefore "stable" under passage from an essentially affine projective limit `(8.13.4)` of
preschemes `X_λ` to a suitable one of them.

(ii) Let `Z` be a locally constructible part of `X` such that, for every `s ∈ S`, `Z ∩ X_s` is open in `X_s`, and denote
by `Z_s` the sub-prescheme of `X_s` induced on the open set `Z ∩ X_s`.

<!-- original page 76 -->

Then, in propositions `(9.6.1)` and `(9.6.2, (I))`, one may everywhere replace `f_s` by its restriction
`f_s|Z_s : Z_s → Y_s` without changing the conclusions. Indeed, the verification of `(9.2.1, (i))` is done as in
`(9.6.1)` and `(9.6.2)`. On the other hand, in the reduction to the case where `S` is Noetherian, done in `(9.2.3)`, if
`Z = q⁻¹(Z_0)`, where `q : X → X_0` is the canonical projection and `Z_0` a constructible part of `X_0` `(8.3.11)`, the
fact that `(Z_0)_{s_0}` is open in `(X_0)_{s_0}`, for `s_0 = p(s)`, follows from `(2.4.10)` and from the fact that the
projection `X_s → (X_0)_{s_0}` is surjective. One is therefore reduced to verifying `(9.2.1, (ii))` under the new
hypotheses. Now, since `Z_η` is open in `X_η`, there exists an open set `Z' ⊂ X` such that `Z_η = Z' ∩ X_η`; as `X` is
then Noetherian, `Z'` is constructible, and the same is true of `Z` by hypothesis; one therefore concludes from
`(9.5.2)` and `(0_III, 9.2.2)` that there is a neighbourhood `U` of `η` in `S` such that `Z_s = Z'_s` for `s ∈ U`.
Replacing `S` by `U`, one may therefore restrict to the case where `Z` is open in `X`, and then one is reduced to what
was proved in `(9.6.1)` and `(9.6.2)`.

<!-- original page 76 -->

### 9.7. Constructibility of separability, geometric irreducibility, and geometric connectedness

**Lemma (9.7.1).**

<!-- label: IV.9.7.1 -->

*Let `S` be an irreducible prescheme with generic point `η`, and `f : X → S` a morphism of finite presentation. If `X_η`
has `n` irreducible components (resp. `n'` connected components), there exists an open neighbourhood `U` of `η` in `S`
such that for every `s ∈ U`, `X_s` has at least `n` irreducible components (resp. `n'` connected components).*

One may restrict to the case where `S` is affine, so that `X` is quasi-compact and quasi-separated.

Let `V_i` (`1 ≤ i ≤ n`) be the interiors of the irreducible components of `X_η`; they are pairwise disjoint, quasi-
compact, and their union is dense in `X_η`. By virtue of `(8.2.11)`, applied via the method of `(8.1.2, a))`, there
exists for each `i` a quasi-compact open `W_i` in `X` such that `W_i ∩ X_η = V_i`; since `X` is quasi-separated, the
intersections `W_i ∩ W_j` are quasi-compact `(1.2.7)`, hence, replacing `S` by a neighbourhood of `η`, we may suppose
`W_i ∩ W_j = ∅` for `i ≠ j` by `(8.3.3)`. Moreover, since the `W_i` are constructible, there is a neighbourhood `U` of
`η` in `S` such that for every `s ∈ U` the `(W_i)_s` are non-empty `((9.5.1)` and `(9.2.3))` and such that the union of
the `(W_i)_s` is dense in `X_s` `((9.5.3)` and `(9.2.3))`. This being so, the (finitely many) irreducible components of
the `(W_i)_s` are also the irreducible components of the union of the `(W_i)_s` `(0_I, 2.1.7)`, so the closures in `X_s`
of these components are the irreducible components of `X_s` `(0_I, 2.1.6)` and their number is evidently `≥ n`.

Now let `C_j` (`1 ≤ j ≤ n'`) be the connected components of `X_η`; these are pairwise disjoint quasi-compact open
subsets of `X_η`. If one replaces the `V_i` by the `C_j` in the preceding reasoning, one sees (using `(8.3.3)` twice)
that one may suppose `X` is the union of `n'` pairwise disjoint quasi-compact opens `M_j` (`1 ≤ j ≤ n'`) and that, in a
neighbourhood of `η`, the `(M_j)_s` are non-empty. Since the union of the `(M_j)_s` is `X_s`, the connected components
of the `(M_j)_s` are the connected components of `X_s`, so their number is `≥ n'`.

<!-- original page 77 -->

**Lemma (9.7.2).**

<!-- label: IV.9.7.2 -->

*Let `S` be an irreducible prescheme with generic point `η`, and `f : X → S` a morphism of finite presentation. If `X_η`
is not reduced, there exists an open neighbourhood `U` of `η` in `S` such that, for every `s ∈ U`, `X_s` is not
reduced.*

Indeed, let `𝒩` be the Nilradical of `𝒪_X`; it follows from `(8.2.13)`, applied via the method of `(8.1.2, a))`, that
`𝒩_η` is the nilradical of `𝒪_{X_η}`, and the hypothesis is that `𝒩_η ≠ 0`. One concludes from `(9.4.5)` and `(9.2.3)`
that there is a neighbourhood `U` of `η` such that, for every `s ∈ U`, `𝒩_s` is identified with an Ideal of `𝒪_{X_s}`
and `𝒩_s ≠ 0`; since `𝒩_s` is evidently contained in the Nilradical of `𝒪_{X_s}`, one sees that `X_s` is not reduced for
`s ∈ U`.

**(9.7.3)**

<!-- label: IV.9.7.3 -->

Given a polynomial `F ∈ A[T_1, …, T_n]`, where `A` is a ring and the `T_i` are indeterminates, for every ring
homomorphism `ρ : A → B`, we denote by `F^(ρ)` or `F^(B)` the polynomial of `B[T_1, …, T_n]` obtained by replacing each
coefficient of `F` by its image under `ρ`. If `k` is a field, `F ∈ k[T_1, …, T_n]` a non-constant polynomial, and
`X = Spec(k[T_1, …, T_n]/(F))`, to say that `X` is integral (or that the ideal `(F)` is prime) means that `F` is
irreducible (that is, in every factorization `F = F_1 F_2` into polynomials of `k[T_1, …, T_n]`, `F_1` or `F_2` is of
degree `0`); this follows from the fact that the ring `k[T_1, …, T_n]` is factorial. From this one deduces immediately
(`(4.6.2)` and `(4.5.2)`):

**Lemma (9.7.4).**

<!-- label: IV.9.7.4 -->

*Let `k` be a field, `Ω` an algebraically closed extension of `k`, `F` a non-constant polynomial of `k[T_1, …, T_n]`.
The following conditions are equivalent:*

*a) `X = Spec(k[T_1, …, T_n]/(F))` is geometrically integral.*

*b) `F^(K)` is irreducible for every extension `K` of `k`.*

*c) `F^(Ω)` is irreducible.*

In this case we shall say that `F` is **geometrically irreducible**.

**Lemma (9.7.5).**

<!-- label: IV.9.7.5 -->

*Let `A` be an integral ring, `K` its field of fractions, `F` a non-constant polynomial of `A[T_1, …, T_n]` of degree
`d` such that `F^(K)` is geometrically irreducible. Then there exists `f ≠ 0` in `A` such that for every `x ∈ D(f)`,
`F^(k(x))` is geometrically irreducible.*

Write `F = ∑_α c_α T^α` as usual, with `α = (α_1, …, α_n)`, `T^α = T_1^{α_1} T_2^{α_2} ⋯ T_n^{α_n}`,
`|α| = α_1 + α_2 + ⋯ + α_n ≤ d` (at least one of the `c_α` with `|α| = d` being non-zero). Since the non-zero `c_α` are
invertible in `K`, we may suppose, by replacing `A` if necessary with a ring `A_g` (`g ≠ 0` in `A`), that the non-zero
`c_α` are invertible in `A`. It follows that for every `x ∈ Spec(A)`, `F^(k(x))` is of degree `d`.

We first prove a preliminary lemma.

**Lemma (9.7.5.1).**

<!-- label: IV.9.7.5.1 -->

*Let `A` be an integral ring, `S = Spec(A)`, `η` the generic point of `S`, `B` the polynomial ring `A[T_1, …, T_m]`,
`(P_i)_{i ∈ I}` a finite family of elements of `B`, and `𝔞` the ideal of `B` generated by the `P_i`. For every `s ∈ S`,
let `𝔞_s` be the ideal of `k(s)[T_1, …, T_m]` generated by the polynomials `(P_i)^(k(s))` (`i ∈ I`). Then, if
`V(𝔞_η) = ∅`, there exists a neighbourhood `U` of `η` in `S` such that `V(𝔞_s) = ∅` for every `s ∈ U`.*

Indeed, let `Y = Spec(B)`, and let `Z` be the closed part `V(𝔞)` of `Y`; since `𝔞` is a finitely generated ideal, `Z` is
constructible in `Y` `(0_III, 9.1.5)`, and with the notations introduced in `(9.4.1)`, one has `V(𝔞_s) = Z_s` for every
`s ∈ S`; since the structure morphism `Y → S` is of finite presentation, the conclusion of the lemma follows from
`(9.5.1)` and `(9.2.3)`.

<!-- original page 78 -->

Let `(p, q)` be a pair of integers `> 0` with `p + q = d`; introduce indeterminates `T'_β`, `T''_γ` for all systems of
integers `β`, `γ` with `|β| ≤ p` and `|γ| ≤ q`; for every system of integers `α` with `|α| ≤ d`, consider the polynomial
of `B = A[T'_β, T''_γ]_{|β| ≤ p, |γ| ≤ q}`:

```text
                P_α(T'_β, T''_γ) = ∑_{β + γ = α} T'_β T''_γ − c_α.
```

Let `Ω` be an algebraic closure of `K`; to say that there exist two polynomials `F_1`, `F_2` of `Ω[T_1, …, T_n]`, of
respective degrees `p` and `q`, such that `F_1 F_2 = F^(Ω)`, is to say that the system of equations `P_α(ξ, ζ) = 0`
(`|α| ≤ d`) admits a solution `(ξ, ζ)` (`|β| ≤ p`, `|γ| ≤ q`) formed of elements of `Ω`. Let `𝔞` be the ideal of `B`
generated by the `P_α`; the preceding interpretation, and Hilbert's Nullstellensatz, show that the hypothesis on `F^(K)`
implies that `V(𝔞_η) = ∅`, where `η` denotes the generic point of `Spec(A)`; lemma `(9.7.5.1)` therefore proves that in
a neighbourhood of `η`, one has `V(𝔞_s) = ∅`, and consequently, for these values of `x`, `F^(k(x))` admits no
factorization `F^(k(x)) = G_1 G_2` where `G_1`, `G_2` are polynomials of respective degrees `p` and `q` whose
coefficients lie in an algebraic closure of `k(x)`. It suffices to apply this result to all pairs of integers `(p, q)`
with `p > 0`, `q > 0`, and `p + q = d` to obtain the conclusion of lemma `(9.7.5)`.

**Proposition (9.7.6).**

<!-- label: IV.9.7.6 -->

*Let `S` be an integral Noetherian prescheme with generic point `η`, `f : X → S` a morphism of finite type, `ℱ` a
coherent `𝒪_X`-Module. If `ℱ_η` has no embedded associated prime cycle, there exists a neighbourhood `U` of `η` in `S`
such that, for every `s ∈ U`, `ℱ_s` has no embedded associated prime cycle.*

Since `X_η` is Noetherian, there exists an injective homomorphism `v : ℱ_η → ⊕_{i=1}^m 𝒢_i`, where each `𝒢_i` is
irredundant and `Ass(𝒢_i)` is the set of `x_i`, where `{x_i} = Ass(ℱ_η)` `(3.2.6)`; if `Z_i` is the closure of `{x_i}`
in `X_η`, one has `Z_i = Supp(𝒢_i)` `(3.1.4)`, and by hypothesis the `Z_i` are the irreducible components of
`Z = Supp(ℱ_η)`. It follows from `(8.5.2, (i)` and `(ii))` (by restricting `S` if necessary to a neighbourhood of `η`)
and `(8.5.8)` that there exist coherent `𝒪_X`-Modules `ℋ_i` and an injective homomorphism `u : ℱ → ⊕_{i=1}^m ℋ_i` such
that `(ℋ_i)_η = 𝒢_i` for every `i` and `v = u_η`. If `Y_i = Supp(ℋ_i)`, one has `(Y_i)_s = Supp((ℋ_i)_s)` for every
`s ∈ S` `(I, 9.1.13)`, and in particular `(Y_i)_η = Z_i` for every `i`. The hypothesis implies that for `i ≠ j`,
`Z_i − (Z_i ∩ Z_j)` is dense open in `Z_i`; one therefore deduces from `(9.5.3)` and `(9.5.4)` that in a neighbourhood
of `η`, `(Y_i)_s − ((Y_i)_s ∩ (Y_j)_s)` is open and dense in `(Y_i)_s`. Suppose that we have proved that each `(ℋ_i)_s`
has no embedded associated prime cycle for `s ∈ U`. Then the elements of `Ass((ℋ_i)_s)` are the maximal points of
`(Y_i)_s`; none of them can therefore belong to a `(Y_j)_s` for `i ≠ j`, and the proposition will be proved. We may
therefore suppose that `ℱ` is irredundant; moreover, we may restrict to the case where `S = Spec(A)` is affine; `X` is
then a union of finitely many affine opens `V_j`, and if `V_j ∩ Supp(ℱ_η) = ∅`, one will also have `V_j ∩ Supp(ℱ_s) = ∅`
for `s` near `η` `(9.5.1)`, so we may restrict to the case where `X = Spec(B)` is also affine and where the morphism
`f : X → S` is dominant; `A` is therefore an integral Noetherian ring, a subring of a finitely generated `A`-algebra
`B`, and `ℱ = M̃`, where `M` is a finitely generated `B`-module; by hypothesis, if `K` is the field of fractions of `A`,
the `B^(K)`-module `M^(K)` is irredundant. Let `𝔮` be the unique

<!-- original page 79 -->

element of `Ass(M^(K))`, and let `𝔭` be the prime ideal of `B` inverse image of `𝔮` under the canonical map `B → B^(K)`.
We know `(5.11.1.1)` that there exists a finite filtration `(N_h)_{0 ≤ h ≤ m}` of `M^(K)` such that `N_0 = M^(K)`,
`N_m = 0`, and `N_h/N_{h+1}` is isomorphic to a non-zero sub-`B^(K)`-module of `B^(K)/𝔮`. Let `M_h` be the inverse image
of `N_h` under the canonical map `M → M^(K)`. It follows from `(9.4.4)` that for `s` sufficiently close to `η`,
`(M_h)^(k(s))` is identified with a sub-`B^(k(s))`-module of `M^(k(s))`, and the quotient
`(M_h)^(k(s))/(M_{h+1})^(k(s))` with a non-zero sub-`B^(k(s))`-module of `B^(k(s))/𝔭^(k(s)) = (B/𝔭)^(k(s))`. Taking
`(3.1.7)` into account, one sees that one is reduced to proving, with the same notations, that if `B` is integral, then
`B^(k(s))` has no embedded associated prime ideals for `s` near `η`. Now, replacing `A` if necessary by `A_g` and `B` by
`B_g` (where `g` is an element `≠ 0` of `A`), one may suppose that `B` contains a polynomial `A`-algebra
`C = A[T_1, …, T_n]` such that `B` is a finitely generated `C`-module (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, cor. 1
of th. 1). Since `B^(K)` is a torsion-free `C^(K)`-module, one may apply again the reasoning made above by replacing
`B`, `M`, and `𝔮` by `C`, `B`, and `(0)` respectively, and it therefore suffices to see that for `s` near `η`,
`C^(k(s))` has no embedded associated prime ideals. But this is evident since `C^(k(s)) = k(s)[T_1, …, T_n]` is an
integral ring. Q.E.D.

**Theorem (9.7.7).**

<!-- label: IV.9.7.7 -->

*Let `f : X → S` be a morphism of finite presentation, and let `E` be the set of `s ∈ S` for which `X_s` has one of the
following properties:*

*(i) being geometrically irreducible;*

*(ii) being geometrically connected;*

*(iii) being geometrically reduced;*

*(iv) being geometrically integral.*

*Then `E` is locally constructible in `S`.*

To see that the properties considered are constructible, we first remark that they trivially satisfy condition
`(9.2.1, (i))`, by virtue of `(4.5.6, (i))` and `(4.6.5, (i))`. It therefore remains to verify `(9.2.1, (ii))`, so we
may suppose `S = Spec(A)` is affine, Noetherian, and integral, with generic point `η`. By virtue of `(4.6.8)`, there
exists a finite extension `K'` of `K = k(η)` such that `(X_η)_{(K')}` is such that its irreducible (resp. connected)
components are geometrically irreducible (resp. geometrically connected) and such that `((X_η)_{(K')})_{red}` is
geometrically reduced. Since there exists a basis of `K'` over `K` formed of elements integral over `A`, the integral
ring `A'` generated by these elements is finite over `A` and has `K'` as its field of fractions. Set `S' = Spec(A')`;
the morphism `g : S' → S` is finite and dominant, hence surjective `(II, 6.1.10)`. Set `X' = X_{(S')}`, so that if `η'`
is the generic point of `S'`, one has `X'_{η'} = (X_η)_{(K')}`; the set `E'` of `s' ∈ S'` such that `X'_{s'}` has one of
properties (i), (ii), (iii), or (iv) is equal to `g^{-1}(E)` `(9.2.2, (iv))` (`E` corresponding of course to the same
property); since `g` is surjective, one has `E = g(E')` and `S − E = g(S' − E')`; moreover, `g` is closed and
`g^{-1}(η) = {η'}` since `A'` is integral and finite over `A` (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, cor. 1 of
prop. 1), so the image under `g` of every neighbourhood of `η'` is a neighbourhood of `η`. The theorem will therefore be
proved if we show that `E'` or `S' − E'` is a neighbourhood of `η'`. Otherwise put, we may henceforth suppose that the
irreducible (resp. connected) components of `X_η` are geometrically irreducible (resp. geometrically connected) and that
`(X_η)_{red}` is geometrically reduced.

<!-- original page 80 -->

Suppose first that `η ∈ S − E` for one of properties (i) to (iv). If `X_η` is not geometrically irreducible (resp.
geometrically connected), it is not irreducible (resp. connected) by the preceding hypothesis, so the same is true of
`X_s` for `s` in a neighbourhood of `η` `(9.7.1)`, and *a fortiori* in this neighbourhood `X_s` is not geometrically
irreducible (resp. geometrically connected). On the other hand, if `X_η` is not geometrically reduced, it is not reduced
(otherwise it would be equal to `(X_η)_{red}`, which is geometrically reduced by hypothesis); hence, in a neighbourhood
of `η`, `X_s` is not reduced `(9.7.2)`, and *a fortiori* not geometrically reduced. Finally, if `X_η` is not
geometrically integral, either it is not reduced, in which case we have just seen that `X_s` is not reduced (nor *a
fortiori* integral) in a neighbourhood of `η`; or `X_η` is reduced (hence geometrically reduced by hypothesis), and then
it is not geometrically irreducible, and we saw above that the same is then true of `X_s` for `s` near `η`; *a fortiori*
`X_s` is not geometrically integral for these values of `s`.

We shall therefore henceforth suppose that `η ∈ E` and examine separately each of the properties considered.

**1°** Suppose `X_η` is geometrically integral. Let `L` be the field of rational functions on `X_η`; the hypothesis on
`X_η` implies that `L` is a separable extension of `K` `(4.6.3)`, hence a finite separable extension of a pure extension
`K(T_1, …, T_n)` (`T_i` indeterminates); there is therefore an element `z ∈ L`, integral over the ring `K[T_1, …, T_n]`,
such that `L = K(T_1, …, T_n)(z)`; let `G ∈ K[T_1, …, T_n, T_{n+1}]` be its minimal polynomial. There exists an element
`g ≠ 0` of `A` such that all the non-zero coefficients of `G` (which belong to `K`) lie in the ring `A_g`; replacing `A`
by `A_g` (which amounts to replacing `S` by a neighbourhood of `η`), we may therefore suppose that `G` has its
coefficients in `A`; denoting by `F` the polynomial `G` considered as an element of `A[T_1, …, T_n, T_{n+1}]`, we then
have `G = F^(k(η))`. Set `Y = Spec(A[T_1, …, T_{n+1}]/(F))`, so that `Y_η = Spec(k(η)[T_1, …, T_{n+1}]/(G))`; `Y_η` is
an integral scheme having `L` as its field of rational functions. Since `X_η` and `Y_η` are Noetherian, there exists a
non-empty open `V ⊂ Y_η` and an open immersion `v : V → X_η` (necessarily dominant) `((I, 6.5.1, (ii))` and
`(6.5.4, (ii)))`. Let `W` be an open of `Y` such that `W ∩ Y_η = V`; applying `(8.8.2, (i))` and `(8.10.5, (iii))` via
the method of `(8.1.2, a))`, one sees that, by replacing `S` if necessary by a neighbourhood of `η`, one may suppose
that `v = w_η`, where `w : W → X` is an open immersion.

This being so, we saw `(4.6.3)` that the criterion for an integral algebraic prescheme to be geometrically integral
depends only on its field of rational functions; since `X_η` is geometrically integral by hypothesis, the same is true
of `Y_η`, and the definition of `G` therefore implies that this polynomial is geometrically irreducible `(9.7.4)`.
Applying `(9.7.5)`, one sees that there is a neighbourhood `U` of `η` in `S` such that `F^(k(s))` is geometrically
irreducible for every `s ∈ U`, hence `Y_s` is geometrically integral for `s ∈ U` `(9.7.4)`; moreover, we may suppose
that for `s ∈ U`, `W_s` is non-empty `(9.5.1)`, and consequently is geometrically integral `(4.6.3)`; finally, we may
also suppose that

<!-- original page 81 -->

for `s ∈ U`, `w_s : W_s → X_s` is an open immersion `(9.6.1, (x))`, and that its image in `X_s` is everywhere dense
`(9.5.3)`. Otherwise put, for `s ∈ U` there is in `X_s` an everywhere dense open `W_s` which is geometrically integral;
criterion `(4.5.9, c))` therefore already shows that `X_s` is geometrically irreducible for `s ∈ U`. Finally, since
`X_η` is reduced and consequently has no embedded associated prime cycle `(3.2.1)`, one may also suppose that for
`s ∈ U`, `X_s` has no embedded associated prime cycle `(9.7.6)`; let then (for a fixed `s ∈ U`) `Ω` be an algebraically
closed extension of `k(s)`, and let `p : (X_s)_{(Ω)} → X_s` be the canonical projection; `p^{-1}(W_s)` is a dense open
in `(X_s)_{(Ω)}` `(2.3.10)` and is integral by hypothesis; moreover `(X_s)_{(Ω)}` has no embedded associated prime cycle
`(4.2.7)`, so one concludes from `(3.2.1)` that `(X_s)_{(Ω)}` is reduced; this completes the proof that `X_s` is
geometrically integral `(4.6.1)`.

**2°** Suppose `X_η` is geometrically irreducible; since `X_{red}` is also of finite type over `S` `(1.5.4, (vi))` one
may, taking `(I, 5.1.8)` into account, replace `X` by `X_{red}`; then `X_η` is also integral, and since by hypothesis
`X_η` is geometrically reduced, it is geometrically integral. One is then in the conditions of 1°, and one concludes
(returning to the initial hypotheses) that `X_s` is geometrically irreducible for `s` near `η`.

**3°** Suppose `X_η` is geometrically connected, and let `Z_i` (`1 ≤ i ≤ n`) be the irreducible components of `X_η`;
there exists (by virtue of `(5.10.8.1)` applied to `Σ = {∅}`) a surjective map `j ↦ ν(j)` from an interval `[1, m]` of
`ℕ` onto `[1, n]` such that `Z_{ν(j)} ∩ Z_{ν(j+1)} ≠ ∅` for `1 ≤ j ≤ m`. For each `i`, let `X_i` be the closure of `Z_i`
in `X`, and let `Y` be the union of the `X_i`; since `Y_η = X_η` by definition, we may suppose, by virtue of `(9.5.1)`,
that `Y_s = X_s` for every `s ∈ S`, hence that `X_s` is the union of the `(X_i)_s`. But, considering the reduced closed
sub-preschemes of `X` having the `X_i` as underlying spaces, one sees by 2° that there exists a neighbourhood `U` of `η`
in `S` such that for `s ∈ U` the `(X_i)_s` are geometrically irreducible (since the `(X_i)_η` may be supposed
geometrically irreducible, as we saw at the start). Moreover, we may also suppose that for `s ∈ U`, one has
`(X_{ν(j)})_s ∩ (X_{ν(j+1)})_s ≠ ∅` `(9.5.1)` for `1 ≤ j ≤ m`; one concludes at once that `X_s` is connected, hence
`(4.5.13.1)` geometrically connected for `s ∈ U`.

**4°** Suppose `X_η` is geometrically reduced; let `Z_i` be the irreducible components of `X_η`, `W_i` the interior of
`Z_i` in `X_η`; there is for each `i` an open `V_i` of `X` such that `W_i = V_i ∩ X_η` for every `i`; since the `W_i`
are open and pairwise disjoint and their union is dense in `X_η`, we may (`(9.5.1)`, `(9.5.3)`, and `(9.5.4)`) suppose
that for `s` near `η`, the `(V_i)_s` are pairwise disjoint opens in `X_s` and that their union is dense in `X_s`.
Moreover, since the `W_i` are geometrically reduced and were supposed at the start geometrically irreducible, it follows
from 1° that for `s` near `η`, the `(V_i)_s` are geometrically integral, and *a fortiori* reduced. On the other hand,
one draws from `(9.7.6)` that for `s` near `η`, `X_s` has no embedded associated prime cycle, since this is so for
`X_η`, which is reduced `(3.2.1)`; one concludes from `(3.2.1)` that `X_s` is reduced, and from `(4.6.1)` that it is
geometrically reduced.

<!-- original page 82 -->

The parts of statement `(9.7.7)` concerning properties (i) and (ii) generalize as follows:

**Proposition (9.7.8).**

<!-- label: IV.9.7.8 -->

*Let `S` be an irreducible prescheme with generic point `η`, and `f : X → S` a morphism of finite presentation. Let `n`
(resp. `n'`) be the geometric number of irreducible (resp. connected) components of `X_η` `(4.5.2)`. Then there exists a
neighbourhood `U` of `η` in `S` such that for every `s ∈ U` the geometric number of irreducible (resp. connected)
components of `X_s` is equal to `n` (resp. `n'`).*

Taking into account that the geometric number of irreducible (resp. connected) components of an algebraic prescheme is
invariant under extension of the base field `(4.5.6)`, one sees by the method of `(9.2.3)` that one may reduce to the
case where `S` is affine, Noetherian, and integral. Moreover, reasoning as at the start of the proof of `(9.7.7)`, one
sees that one may suppose that the irreducible (resp. connected) components of `X_η` are geometrically irreducible
(resp. geometrically connected). We already know `(9.7.1)` that for every `s` near `η`, `X_s` has at least `n`
irreducible components and `n'` connected components. On the other hand, if `Z_i` (resp. `Z'_j`) are the irreducible
(resp. connected) components of `X_η`, and `X_i` (resp. `X'_j`) the reduced closed sub-prescheme of `X` having as
underlying space the closure of `Z_i` (resp. `Z'_j`) in `X`, it follows from `(9.5.1)` that in a neighbourhood of `η`,
the `(X_i)_s` (resp. `(X'_j)_s`) form a covering of `X_s` and that the `(X'_j)_s` are pairwise disjoint; since the
`(X_i)_s` (resp. `(X'_j)_s`) are geometrically irreducible (resp. geometrically connected) by virtue of `(9.7.7)` for
`s` near `η`, one sees that `X_s` has at most `n` irreducible components and at most `n'` connected components, whence
the proposition.

**Corollary (9.7.9).**

<!-- label: IV.9.7.9 -->

*Let `f : X → S` be a morphism of finite presentation. For every `s ∈ S`, let `n(s)` (resp. `n'(s)`) be the geometric
number of irreducible (resp. connected) components of `f^{-1}(s)` `(4.5.2)`. Then the function `s ↦ n(s)` (resp.
`s ↦ n'(s)`) is locally constructible in `S`.*

It is a matter of showing that the property "`X` is an algebraic prescheme over a field `k` and the geometric number of
irreducible (resp. connected) components of `X` is equal to `n` (resp. `n'`)" is constructible. It follows from
`(4.5.6)` that this property satisfies condition `(9.2.1, (i))`, and one is therefore reduced to the case where `S` is
affine, Noetherian, and integral with generic point `η`; the conclusion then follows from `(9.7.8)`.

**Corollary (9.7.10).**

<!-- label: IV.9.7.10 -->

*Let `X` be a locally Noetherian prescheme such that, if `X'` is the normalization of `X_{red}`, the canonical morphism
`f : X' → X` is finite. Then the set of points `x ∈ X` such that `X` is geometrically unibranch at the point `x` is
locally constructible in `X`.*

Indeed, this set is by definition the set of points `x ∈ X` such that the number of geometric points of `f^{-1}(x)` is
equal to `1`. But since `f` is finite, this number is also the geometric number of irreducible components of the
discrete space `f^{-1}(x)` (taking into account the definition of the normalization `(II, 6.3.8)` and `(4.5.11)`); the
conclusion therefore follows from `(9.7.9)`.

**Remark (9.7.11).**

<!-- label: IV.9.7.11 -->

\*Let `Z` be a locally constructible part of `X` such that, for every `s ∈ S`, `Z ∩ X_s` is open in `X_s`, and denote by
`Z_s` the sub-prescheme of `X_s` induced

<!-- original page 83 -->

on the open `Z ∩ X_s`. Then, in theorem `(9.7.7)`, one may replace `X_s` by `Z_s` without changing the conclusion: one
sees this by repeating the reasoning made in `(9.6.7, (ii))`.\*

**Proposition (9.7.12).**

<!-- label: IV.9.7.12 -->

*Let `f : X → S` be a morphism of finite presentation, and `g : S → X` an `S`-section of `X` `(I, 2.5.5)`. For every
`s ∈ S`, let `X°_s` be the connected component of `f^{-1}(s)` containing `g(s)`; then, the union `X°` of the `X°_s` for
`s ∈ S` is a locally constructible part of `X`.*

Let us first show that one may reduce to the case where `S` is affine and Noetherian. One may always suppose
`S = Spec(A)` affine; with the notations of `(9.2.3)`, one has `f = (f_0)_{(S)}`, where `f_0 : X_0 → S_0` is a morphism
of finite type, and one may moreover suppose that there exists an `S_0`-section `g_0 : S_0 → X_0` such that
`g = (g_0)_{(S)}` `(8.9.1)`. Note now that if `p` is the morphism `S → S_0`, then, for every `s_0 ∈ S_0`, the connected
component `(X_0)°_{s_0}` of `f_0^{-1}(s_0)` containing `g_0(s_0)` is geometrically connected `(4.5.13)`, and
consequently, if `s_0 = p(s)`, one has `X°_s = q^{-1}((X_0)°_{s_0})` where `q : X_s → (X_0)_{s_0}` is the canonical
projection (`(4.5.8)` and `(4.4.1)`); our assertion therefore follows from `(1.8.2)`.

Let us then use the constructibility criterion `(0_III, 9.2.3)`: let `x` be a point of `X`, `Z` the reduced sub-
prescheme of `X` having `‾{x}` as underlying space, `Y` the reduced sub-prescheme of `S` having `f(Z)` as underlying
space; since the restriction of `f` to `Z` factors as `Z → Y → S` `(I, 5.2.2)`, we may replace `S` by `Y`, otherwise put
suppose that `f(x) = η`, the generic point of the integral prescheme `S`. By hypothesis, `X_η` is the sum of two sub-
preschemes `X^0_η`, `X^1_η` induced on complementary opens of `X_η`. By virtue of `(9.5.4)` and `(9.5.1)`, we may
therefore, by replacing `S` if necessary by a neighbourhood of `η`, suppose that `X` is the union of two disjoint opens
`X^0`, `X^1` such that `(X^0)_η = X^0_η` and `(X^1)_η = X^1_η`. Since `g : S → X` is continuous and injective, `S` is
the union of the two disjoint opens `g^{-1}(X^0)` and `g^{-1}(X^1)`; but since `S` is irreducible, and *a fortiori*
connected, one of these two opens is empty, and since `g(η) ∈ X^0_η` by definition, one has `g^{-1}(X^1) = ∅`. In other
words, `g` is an `S`-section of `X^0`; on the other hand, since `(X^0)_η` is geometrically connected `(4.5.13)`, the
same is true of `(X^0)_s` for every `s` near `η` `(9.7.7)`; since `g(s) ∈ (X^0)_s`, one has indeed `(X^0)_s = X°_s`.
Q.E.D.

### 9.8. Primary decomposition near a generic fibre

**Proposition (9.8.1).**

<!-- label: IV.9.8.1 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. Then
the set `E` of `s ∈ S` such that `ℱ_s` is an `𝒪_{X_s}`-Module with no embedded associated prime cycle is locally
constructible.*

We know that for quasi-coherent Modules on algebraic preschemes, the property of having no embedded associated prime
cycle is invariant under change of base field `(4.2.7)`; we may therefore restrict to the case where `S` is affine,
Noetherian, and integral with generic point `η`, and prove that in this case `E` or `S − E` is a neighbourhood of `η`.
We saw in `(9.7.6)` that if `η ∈ E`, then `E` is a neighbourhood of `η`; there remains to consider the case where `ℱ_η`
has embedded associated prime cycles. We may restrict to the case where `X` is affine, and where there is a sub-
`𝒪_{X_η}`-Module coherent `ℱ'_η` of `ℱ_η` whose support `Z'` is non-empty and rare with respect to the support `Z` of
`ℱ_η` `(3.1.3)`; then, by virtue of `(8.5.2, (i)` and `(ii))`

<!-- original page 84 -->

and `(8.5.8)`, applied via the method of `(8.1.2, a))`, there exists a coherent sub-`𝒪_X`-Module `ℱ'` of `ℱ` such that
`ℱ' = ℱ'_η`; if `Y = Supp(ℱ)`, `Y' = Supp(ℱ')`, one consequently has `Y_s = Supp(ℱ_s)`, `Y'_s = Supp(ℱ'_s)` for every
`s ∈ S` `(I, 9.1.13)`, and in particular `Z = Y_η`, `Z' = Y'_η`; since `Z − Z'` is dense in `Z` and `Z' ≠ ∅`, there is a
neighbourhood `U` of `η` such that for `s ∈ U`, `Y_s − Y'_s` is dense in `Y_s`, and `Y'_s ≠ ∅` (`(9.5.1)` and
`(9.5.3)`); considering a generic point of an irreducible component of `Y'_s` and a sufficiently small neighbourhood of
this point in `X_s`, one deduces at once from `(3.1.3)` that `ℱ_s` has embedded associated prime cycles.

**(9.8.2)**

<!-- label: IV.9.8.2 -->

Let `S` be an integral Noetherian prescheme with generic point `η`, `f : X → S` a morphism of finite type, `ℱ` a
coherent `𝒪_X`-Module. Consider a reduced irredundant decomposition `(𝒢_i)_{i ∈ I}` of `ℱ_η` `(3.2.6)`; the `𝒢_i` are
thus quotients of `ℱ_η`, and there is an injective homomorphism `h : ℱ_η → ⊕ 𝒢_i`; moreover `Ass(𝒢_i)` is reduced to a
single point `x_i`. Let `Z_i` be the closure of `{x_i}` in `X`, so that `(Z_i)_η = Supp(𝒢_i)`. Denote by `𝒥_i` the
coherent Ideal of `𝒪_X` defining the reduced closed sub-prescheme of `X` with underlying space `Z_i` (sub-prescheme also
denoted `Z_i`). By virtue of `(8.5.2)` and `(8.5.8)`, applied via the method of `(8.1.2, a))`, we may (by restricting
`S` if necessary to a neighbourhood of `η`) suppose that there exist quotients `ℋ_i` of `ℱ` (`i ∈ I`) such that
`𝒢_i = (ℋ_i)_η` for every `i`, and a homomorphism `g : ℱ → ⊕ ℋ_i` such that `h = g_η`. Moreover `(I, 9.3.5)`, there
exists an integer `m` such that `((𝒥_i)_η)^m 𝒢_i = (𝒥_i)^m_η 𝒢_i = 0`, and by restricting `S` again, we may therefore
also suppose that `𝒥_i^m ℋ_i = 0` `(8.5.2.5)`, so that the support of `ℋ_i` is contained in `Z_i`; but since it is
closed and contains `x_i`, it is necessarily equal to `Z_i`.

**Proposition (9.8.3).**

<!-- label: IV.9.8.3 -->

*Under the conditions of `(9.8.2)`, for every `s ∈ S` and every `i ∈ I`, denote by `x_{is α}` (`α ∈ 𝒥_{s,i}`) the
maximal points of `(Z_i)_s`. There exists a neighbourhood `U` of `η` in `S` such that, for every `s ∈ U`, the `x_{is α}`
(for `i ∈ I` and, for each `i`, `α ∈ 𝒥_{s,i}`) are pairwise distinct and `Ass(ℱ_s)` is the set of the `x_{is α}` (in
other words, the prime cycles associated to `ℱ_s` are the irreducible components of the `(Z_i)_s`). Moreover, one may
take `U` such that, for the closure of `{x_{is α}}` in `X_s` to be a maximal associated prime cycle of `ℱ_s`, it is
necessary and sufficient that `(Z_i)_η` (closure of `{x_i}` in `X_η`) be a maximal associated prime cycle of `ℱ_η`.*

It follows from `(3.1.3, c'))` that for each `i`, there exists an open `W_i` in `X_η` such that `W_i ∩ (Z_i)_η` is non-
empty, and a coherent `𝒪_{X_η}`-Module `ℋ'_i`, of support `W_i ∩ (Z_i)_η`, such that there is an injective homomorphism
`v_i : ℋ'_i → ℱ_η | W_i`. Let `V_i` be an open of `X` such that `V_i ∩ X_η = W_i`; applying, as in `(9.8.2)`, the
results of `(8.5.2)` and `(8.5.8)`, we may (by restricting `S`) suppose that there exist a coherent Module `ℋ̃_i` of
support `V_i ∩ Z_i` and a homomorphism `u_i : ℋ̃_i → ℱ | V_i` such that `ℋ'_i = (ℋ̃_i)_η` and `v_i = (u_i)_η`. We shall
prove that there is a neighbourhood `U` of `η` such that for `s ∈ U`, the following properties hold:

*(i) The `(ℋ_i)_s` have no embedded associated prime cycle.*

*(ii) The homomorphism `g_s : ℱ_s → ⊕ (ℋ_i)_s` is injective.*

*(iii) `(Z_i)_s ∩ (V_i)_s` is dense in `(Z_i)_s`, `(ℋ̃_i)_s` has support `(Z_i)_s ∩ (V_i)_s`, and
`(u_i)_s : (ℋ̃_i)_s → ℱ_s | (V_i)_s` is injective.*

<!-- original page 85 -->

*(iv) For `i ≠ j`, every irreducible component of `(Z_i)_s` is distinct from every irreducible component of `(Z_j)_s`.*

Now, (i) has already been seen `(9.7.6)`; (ii) is a special case of `(9.4.5)`; (iii) follows similarly from `(9.5.3)`
and `(9.4.5)`. Finally, if `i ≠ j`, `(Z_i)_η ∩ (Z_j)_η = (Z_i ∩ Z_j)_η` is rare in `(Z_i)_η` or in `(Z_j)_η`; suppose
for example that `(Z_i ∩ Z_j)_η` is rare in `(Z_j)_η`; then it follows from `(9.5.3)` and `(9.5.4)` that for `s` near
`η`, `(Z_i ∩ Z_j)_s = (Z_i)_s ∩ (Z_j)_s` is rare in `(Z_j)_s`, which shows that no irreducible component of `(Z_j)_s`
can be contained in an irreducible component of `(Z_i)_s`, nor *a fortiori* equal to it.

This being so, it follows from (ii) and from `(3.1.7)` that for `s ∈ U`, one has `Ass(ℱ_s) ⊂ ⋃_i Ass((ℋ_i)_s)`, and it
follows from (i) that `Ass((ℋ_i)_s)` is the set of `x_{is α}` (`α ∈ 𝒥_{s,i}`). On the other hand, by virtue of (iii) and
the criterion `(3.1.3, c'))`, each of the `x_{is α}` (`α ∈ 𝒥_{s,i}`, `i ∈ I`) belongs to `Ass(ℱ_s)`. Finally, (iv) means
that the `x_{is α}` are pairwise distinct.

It remains to prove the final assertion of the statement. It follows from (iv) that for given `s` and `i`, none of the
sets `{x_{is α}}` can be contained in another for `α ∈ 𝒥_{s,i}`. On the other hand, if `(Z_j)_η ⊂ (Z_i)_η`, we may take
`U` so that `(Z_j)_s ⊂ (Z_i)_s` for `s ∈ U` `(9.5.1)`, hence each `x_{js β}` belongs to the closure of some `x_{is α}`;
on the contrary, if `(Z_j)_η ∩ (Z_i)_η` is rare in `(Z_j)_η`, we saw in proving (iv) that `(Z_j)_s ∩ (Z_i)_s` is rare in
`(Z_j)_s`, so none of the `x_{js β}` is adherent to a `x_{is α}`. In particular, if `(Z_j)_η` is maximal, which amounts
to saying that `(Z_j)_η ∩ (Z_i)_η` is rare in `(Z_j)_η` for every `i ≠ j`, one concludes that `(Z_j)_s ∩ (Z_i)_s` is
rare in `(Z_j)_s` for every `i ≠ j`, hence that every `x_{js β}` (`β ∈ 𝒥_{s,j}`) is maximal. Q.E.D.

**Corollary (9.8.4).**

<!-- label: IV.9.8.4 -->

*The notations and hypotheses being those of `(9.8.2)`, there exists a neighbourhood `U` of `η` in `S` such that, for
every `s ∈ U`, each `(ℋ_i)_s` has no embedded associated prime cycle; moreover, if `(ℋ̌_{s i α})_{α ∈ 𝒥_{s,i}}` is the
unique reduced irredundant decomposition of `((ℋ_i)_η)_s`, then, for every `s ∈ U`, the family
`(ℋ̌_{s i α})_{i ∈ I, α ∈ 𝒥_{s,i}}` is a reduced irredundant decomposition of `ℱ_s`.*

The first assertion follows from `(9.8.1)` and the definition of the `ℋ_i`. On the other hand, we saw in `(9.8.3)` that
the homomorphism `ℱ_s → ⊕ (ℋ_i)_s` is injective, and by definition the same is true of each of the homomorphisms
`(ℋ_i)_s → ⊕_α ℋ̌_{s i α}`, hence the homomorphism `ℱ_s → ⊕ ℋ̌_{s i α}` is injective. Since one may suppose `(9.4.5)`
that each of the `(ℋ_i)_s` is a quotient of `ℱ_s`, the `ℋ̌_{s i α}` are quotients of `ℱ_s`, and there remains to verify
`(3.2.5)` that the `x_{is α}` are pairwise distinct and belong to `Ass(ℱ_s)`, which was proved in `(9.8.3)`.

**Proposition (9.8.5).**

<!-- label: IV.9.8.5 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. For
every `s ∈ S`, let `E(s)` (resp. `E'(s)`) be the finite set (subset of `ℤ ∪ {−∞}`) of dimensions of the prime cycles
associated to `ℱ_s` (resp. of the maximal prime cycles associated to `ℱ_s`, that is, of the irreducible components of
`Supp(ℱ_s)`). Then the functions `s ↦ E(s)` and `s ↦ E'(s)` are locally constructible in `S`.*

<!-- original page 86 -->

It follows from `(4.2.7)` and `(4.2.8)` that condition `(9.2.1, (i))` is satisfied for the properties we wish to show
are constructible. One is therefore reduced to the case where `S` is affine, Noetherian, and integral, and to proving
that `E` and `E'` are constant in a neighbourhood of the generic point `η` of `S`; but this follows from `(9.8.3)` and
`(9.5.5)`.

**Proposition (9.8.6).**

<!-- label: IV.9.8.6 -->

*With the hypotheses and notations of `(9.8.2)`, let `i ∈ I` be such that `(Z_i)_η` is maximal (in other words, is an
irreducible component of `Supp(ℱ_η)`). Then, there exists a neighbourhood `U` of `η` in `S` such that for every `s ∈ U`
and every `α ∈ 𝒥_{s,i}`, the geometric length of `ℱ_s` at `x_{is α}` (relative to `k(s)`) `(4.7.5)` is equal to the
geometric length of `ℱ_η` at `x_i` (relative to `k(η)`).*

One may evidently restrict to the case where `S = Spec(A)` is affine; let us first show that one may reduce to the case
where the sub-prescheme `(Z_i)_η` of `X_η`, which is reduced, is geometrically integral. There is indeed a finite
extension `K'` of `K = k(η)` such that `(((Z_i)_η)_{(K')})_{red}` is geometrically reduced and the irreducible
components of `((Z_i)_η)_{(K')}` are geometrically irreducible `(4.6.8)`. Proceeding as in the proof of `(9.7.7)` by
considering a sub-`A`-algebra `A'` of `K'` having `K'` as field of fractions and finite over `A`. Set `S' = Spec(A')`
and consider the finite surjective morphism `g : S' → S`; let then `X' = X_{(S')}` and `ℱ' = ℱ ⊗_{𝒪_S} 𝒪_{S'}`, and let
`η'` be the generic point of `S'`. For every `s' ∈ S'`, let `s = g(s')`; if `T` is an irreducible component of
`Supp(ℱ_s)`, the irreducible components `T'_j` of `T_{(k(s'))}` are irreducible components of `Supp(ℱ'_{s'})` and
dominate `T` `(4.2.7)`, and the radicial multiplicities of `T` with respect to `ℱ_s` and of each `T'_j` with respect to
`ℱ'_{s'}` are the same `(4.7.9)`. The reasoning of the first part of `(9.7.7)` therefore shows that one may restrict to
proving the proposition for `X'` and `ℱ'`; and by virtue of the choice of `K'`, the reduced sub-preschemes with
underlying spaces the irreducible components of `((Z_i)_η)_{(K')}` are geometrically integral `(4.6.1)`.

Suppose then henceforth that `(Z_i)_η` is geometrically integral; then `(9.7.7)` the same is true of `(Z_i)_s` for `s`
near `η`; the definition `(4.7.5)` shows that it will therefore suffice to prove that the length of the
`𝒪_{X_η, x_i}`-module `(ℱ_η)_{x_i}` is equal to that of the `𝒪_{X_s, x_{is}}`-module `(ℱ_s)_{x_{is}}` (here we have
suppressed the index `α`, unnecessary by hypothesis). The question being evidently local on `X`, we may suppose (by
restricting to a neighbourhood of `x_i`) that `ℱ = ℋ_i`, so that `ℱ_η` is irredundant on `X = Spec(B)` affine, and we
shall write `Z` instead of `Z_i`, and `x` for the generic point of `Z` (and of `Z_η`). The Noetherian ring `B` therefore
contains `A` as a subring, and `ℱ = M̃`, where `M` is a finitely generated `B`-module; moreover, if `K` is the field of
fractions of `A`, the `B^(K)`-module `M^(K)` is `≠ 0` and irredundant. Let `𝔮` be the unique element of `Ass(M^(K))` and
let `𝔭` be the prime ideal of `B`, inverse image of `𝔮`. Using `(5.11.1.1)` as in the proof of `(9.7.6)`, one reduces to
the case where `B` is integral and `M` a non-zero sub-module of `B`; then `ℱ` is a non-zero sub-`𝒪_X`-Module of `𝒪_Z`,
and by virtue of `(9.4.5)`, for `s` near `η`, `ℱ_s` is isomorphic to a non-zero sub- `𝒪_{X_s}`-Module of `𝒪_{Z_s}`;
since `Z_s` is geometrically integral, the lengths of `(ℱ_η)_x` and of `(ℱ_s)_{x_s}` are both equal to `1`, which
completes the proof.

<!-- original page 87 -->

**Corollary (9.8.7).**

<!-- label: IV.9.8.7 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. For
every `s ∈ S`, let `M(s)` be the set of pairs `(d, m)` such that there exists an irreducible component of `Supp(ℱ_s)` of
dimension `d` and of radicial multiplicity `m` for `ℱ_s` `(4.7.8)`. Then the function `s ↦ M(s)` is locally
constructible in `S`.*

It follows from `(4.2.7)` and `(4.7.9)` that condition `(9.2.1, (i))` is satisfied for the property we wish to show is
constructible. One is therefore reduced to the case where `S` is affine, Noetherian, and integral, and to proving that
`M` is constant in a neighbourhood of the generic point of `S`; but then the proposition follows from `(9.8.3)` and
`(9.8.6)`.

**Proposition (9.8.8).**

<!-- label: IV.9.8.8 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. For
every `s ∈ S`, let `ℓ(s)` be the sum of the total multiplicities for `ℱ_s` (relative to `k(s)`) of the generic points of
the irreducible components of `Supp(ℱ_s)` `(4.7.12)`. Then the function `s ↦ ℓ(s)` is locally constructible in `S`.*

Taking `(4.7.12)` into account, condition `(9.2.1, (i))` is satisfied for the property we wish to show is constructible,
and one is therefore reduced to the case where `S` is affine, Noetherian, and integral with generic point `η`, and to
showing that `ℓ` is constant in a neighbourhood of `η`. Using the notations of `(9.8.2)`, this follows from the
definition `(4.7.12)`, from the fact that the geometric number of irreducible components of each `(Z_i)_s` is constant
in a neighbourhood of `η` `(9.7.8)`, that the geometric length of `ℱ_s` at `x_{is α}` is equal to that of `ℱ_η` at `x_i`
for each `i` such that `(Z_i)_η` is maximal `(9.8.6)`, and finally from the fact that the closure of `{x_{is α}}` is a
maximal associated prime cycle of `ℱ_s` if and only if `(Z_i)_η` is a maximal associated prime cycle of `ℱ_η` `(9.8.3)`.

**Remark (9.8.9).**

<!-- label: IV.9.8.9 -->

*One can refine the preceding propositions in various ways; let us limit ourselves to one statement as an example. We
say that a finite part `P` of an algebraic `k`-prescheme `X` is **saturated** if, for every pair of points `x`, `y` of
`P`, the generic points of the irreducible components of `‾{x} ∩ ‾{y}` also belong to `P`; for every finite part `Q` of
`X`, there exists a smallest finite part `P` of `X` containing `Q` and saturated; we shall say that `P` is the
**saturation** of `Q`. For every coherent `𝒪_X`-Module `ℱ`, we shall call **primary skeleton** of `ℱ` the system
`(P, Q, ω, d, m)` where `Q = Ass(ℱ)`, `P` is the saturation of `Q`, `ω` the order relation `‾{x} ⊂ ‾{y}` on `P`, `d` the
function `x ↦ dim ‾{x}` on `P`, `m` the function `x ↦ long_{𝒪_{X,x}} ℱ_x` defined on the set of elements of `Q` maximal
for the relation `ω`. We shall on the other hand call **virtual skeleton** any system `(P, Q, ω, d, m)` where `P` is a
set, `Q` a part of `P`, `ω` an order relation on `P`, `d` a map of `P` into `ℕ`, `m` a map into `ℕ` of the set of
maximal elements of `Q`; one defines in an obvious way the notion of isomorphism of two virtual skeletons. Finally, with
the preceding notations, we shall call **primary type** of `ℱ` the class (for the isomorphism relation of virtual
skeletons) of the primary skeleton of `ℱ`. It follows from `(4.2.6)`, `(4.2.7)`, `(4.2.8)`, `(4.5.1)`, and `(4.7.9)`
that if, for an algebraically closed extension `k'`*

<!-- original page 88 -->

*of `k`, one sets `X' = X ⊗_k k'` and `ℱ' = ℱ ⊗_k k'`, the primary type of `ℱ'` is independent of the algebraically
closed extension `k'` of `k` considered; we shall say that it is the **geometric primary type** of `ℱ`. With these
definitions, the statement we have in view is the following:*

**(9.8.9.1)**

<!-- label: IV.9.8.9.1 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. For
every `s ∈ S`, let `T(s)` be the geometric primary type of `ℱ_s`. Then the function `s ↦ T(s)` is locally constructible
in `S`.*

Taking into account the preceding remarks, one is reduced as usual to proving that if `S` is affine, Noetherian, and
integral with generic point `η`, `T(s)` is constant in a neighbourhood of `η`. Reasoning as at the start of `(9.7.7)`,
one may suppose that all the irreducible parts of `X_η` which intervene are geometrically irreducible, and then the
proposition follows from `(9.5.1)`, `(9.5.5)`, `(9.8.3)`, and `(9.8.6)`; we leave the details to the reader. One could
generalize by considering several coherent Modules and defining their "*simultaneous primary skeleton*", etc. The
general conclusion of what has been seen since the start of this section is that for all properties of the type
considered (and for an irreducible `S`) the properties valid on the "*generic fibre*" remain so on all neighbouring
fibres.

### 9.9. Constructibility of local properties of the fibres

**Proposition (9.9.1).**

<!-- label: IV.9.9.1 -->

*Let `f : X → S` be a morphism locally of finite presentation, `Z` a locally constructible part of `X` such that for
every `s ∈ S`, `Z_s` is closed in `X_s`, `Φ` a finite part of `ℤ ∪ {±∞}`. Then the following parts of `X` are locally
constructible:*

*(i) The set of `x ∈ X` such that `dim_x(Z_{f(x)})` belongs to `Φ`.*

*(ii) The set of `x ∈ X` such that `codim_x(Z_{f(x)}, X_{f(x)})` belongs to `Φ`.*

*(iii) The set of `x ∈ X` such that the local ring `𝒪_{Z_{f(x)}, x}` is equidimensional.*

One will note that properties (i) and (ii) may also be expressed by saying that the functions `x ↦ dim_x(Z_{f(x)})` and
`x ↦ codim_x(Z_{f(x)}, X_{f(x)})` are locally constructible in `X` `(0_III, 9.3.1)`.

The questions being local on `X`, we may restrict to the case where `S = Spec(A)` and `X = Spec(B)` are affine and where
`f` is a morphism of finite presentation; there then exists a subring `A_0` of `A` which is a finitely generated
`ℤ`-algebra, an `A_0`-prescheme of finite type `X_0`, and a constructible part `Z_0` of `X_0` such that
`X = X_0 ⊗_{A_0} A` and `Z = h^{-1}(Z_0)`, where `h : X → X_0` is the canonical projection (`(8.9.1)` and `(8.3.11)`).
Moreover, for every `s ∈ S`, if `s_0` is the projection of `s` in `S_0 = Spec(A_0)`, one has
`X_s = (X_0)_{s_0} ⊗_{k(s_0)} k(s)`, and if `h_s` is the projection `X_s → (X_0)_{s_0}`, one has
`Z_s = h_s^{-1}((Z_0)_{s_0})`. Since the morphism `h_s` is faithfully flat and quasi-compact, the hypothesis that `Z_s`
is closed in `X_s` entails that `(Z_0)_{s_0}` is closed in `(X_0)_{s_0}` `(2.3.12)`.

This being so, the transitivity of fibres `(I, 3.6.4)` and proposition `(4.2.7)` entail that the set of dimensions of
the irreducible components of `Z_s` containing `x` is the same as the set of dimensions of the irreducible components of
`(Z_0)_{s_0}` containing `x_0 = h_s(x)`. In particular, one has `dim_x(Z_s) = dim_{x_0}((Z_0)_{s_0})`. On the other
hand, if `Z_s^{(β)}` are the irreducible components of `Z_s` containing `x` and `X_s^{(α)}` the irreducible components
of `X_s`

<!-- original page 89 -->

containing `x`, one has `codim_x(Z_s, X_s) = inf_β(sup_α(codim(Z_s^{(β)}, X_s^{(α)})))`, `(α, β)` varying over the set
of pairs such that `x ∈ Z_s^{(β)} ⊂ X_s^{(α)}` `(0, 14.2.6)`. Since irreducible algebraic preschemes are
biequidimensional `(5.2.1)`, one may write, by virtue of `(0, 14.3.3.1)`:

```text
(9.9.1.1)        codim_x(Z_s, X_s) = inf_β(sup_α(dim(X_s^{(α)}) − dim(Z_s^{(β)})))
```

with the same choice of pairs `(α, β)`. Since `h_s` is faithfully flat and quasi-compact, for every pair formed of an
irreducible component `(X_0)_{s_0}^{(α)}` of `(X_0)_{s_0}` containing `x_0` and of an irreducible component
`(Z_0)_{s_0}^{(β)}` of `(Z_0)_{s_0}` containing `x_0` and contained in `(X_0)_{s_0}^{(α)}`, there exists a pair
`(X_s^{(α)}, Z_s^{(β)})` of the type described above and such that `Z_s^{(β)}` dominates `(Z_0)_{s_0}^{(β)}` and
`X_s^{(α)}` dominates `(X_0)_{s_0}^{(α)}` `(2.3.5)`. Formula `(9.9.1.1)` (and the analogous formula applied to
`(X_0)_{s_0}`) then show, by virtue of `(4.2.7)`, that one has

```text
                  codim_x(Z_s, X_s) = codim_{x_0}((Z_0)_{s_0}, (X_0)_{s_0}).
```

One sees thus that if `E` (resp. `E_0`) is the set of `x ∈ X` (resp. of `x_0 ∈ X_0`) verifying one of the conditions
(i), (ii), (iii) of the statement (resp. the same condition), one has `E = h^{-1}(E_0)`, and by virtue of `(1.8.2)`, one
sees that one may restrict to the case where `A` is Noetherian, and hence so is `B`. Taking `(0_III, 9.2.3)` into
account, as well as `(9.9.1.1)`, one is reduced to seeing that for every `x ∈ X`, there is a neighbourhood `V` of `x` in
`‾{x}` such that, for every `x' ∈ V`, the set of dimensions of the irreducible components of `X_{f(x')}` (resp.
`Z_{f(x')}`) containing `x'` is the same, and moreover that the same is true of the set of pairs
`(dim(Z_{f(x')}^{(β)}), dim(X_{f(x')}^{(α)}))` for pairs formed of an irreducible component `X_{f(x')}^{(α)}` of
`X_{f(x')}` and an irreducible component `Z_{f(x')}^{(β)}` of `Z_{f(x')}` contained in `X_{f(x')}^{(α)}` and containing
`x'`. We may evidently for this replace `S` by the reduced sub-prescheme `S'` of `S` having `‾{f(x)}` as underlying
space, and `X` by `X' = f^{-1}(S')`, the fibres of `X` and `X'` at points of `S'` being the same. Otherwise put, we may
restrict to the case where `S` is integral and where `η = f(x)` is its generic point.

By hypothesis `Z_η` is closed in `X_η`; since `Z` is constructible, it follows from `(8.3.11)`, applied via the method
of `(8.1.2, a))`, that one may, by replacing `S` if necessary by an open neighbourhood of `η`, suppose that `Z` is
closed in `X`. Let `X_i` (resp. `Z_j`) be the irreducible components of `X` (resp. `Z`) containing `x`; by virtue of
`(0_I, 2.1.8)`, the `X_i ∩ X_η` (resp. `Z_j ∩ X_η`) are the irreducible components of `X_η` (resp. `Z_η`) containing
`x`; by virtue of `(9.5.1)`, we may further suppose, by restricting `S` if necessary to a neighbourhood of `η`, that the
`X_i` (resp. `Z_j`) are exactly the irreducible components of `X` (resp. `Z`) meeting `‾{x}` and that the
`(X_i)_s ∩ ‾{x}` and `(Z_j)_s ∩ ‾{x}` are non-empty for every `s ∈ S`. This being so, it follows again from `(9.7.1)`
that we may suppose, by restricting `S`, that the pairs `(i, j)` such that `(Z_j)_s ⊂ (X_i)_s` are the same for every
`s ∈ S`. The conclusion then follows from `(9.5.6)`: for every `s` sufficiently near `η`, all the irreducible components
of `(X_i)_s` (resp. `(Z_j)_s`) have the same dimension, equal to that of `(X_i)_η` (resp. `(Z_j)_η`). Moreover, if
`(i, j)` is a pair such that `Z_j ⊄ X_i`, `(X_i)_η` does not contain the

<!-- original page 90 -->

generic point of `(Z_j)_η`, so `dim((X_i ∩ Z_j)_η) < dim((Z_j)_η)`; consequently, the common dimension of the
irreducible components of `(X_i)_s ∩ (Z_j)_s` is, for every `s ∈ S`, strictly less than the common dimension of the
irreducible components of `(Z_j)_s`, which proves that none of the irreducible components of `(Z_j)_s` is contained in
an irreducible component of `(X_i)_s` for `s ∈ S`. Q.E.D.

**Proposition (9.9.2).**

<!-- label: IV.9.9.2 -->

*Let `f : X → S` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation,
`Φ` a finite part of `ℤ ∪ {±∞}`. The following parts of `X` are locally constructible:*

*(i) The set of points `x ∈ X` such that `ℱ_{f(x)}` is equidimensional at the point `x` `(5.1.12)`.*

*(ii) The set of `x ∈ X` such that the geometric lengths of `ℱ_{f(x)}` relative to `k(f(x))`, at the generic points of
the irreducible components of `Supp(ℱ_{f(x)})` containing `x` `(4.7.5)`, belong to `Φ`.*

*(iii) The set of `x ∈ X` such that the dimensions of the prime cycles associated to `ℱ_{f(x)}` and containing `x`
belong to `Φ`.*

*(iv) The set of `x ∈ X` such that `ℱ_{f(x)}` is geometrically reduced at the point `x` `(4.6.17)`.*

*(v) The set of `x ∈ X` such that `ℱ_{f(x)}` is geometrically integral at the point `x` `(4.6.22)`.*

*(vi) The set of `x ∈ X` such that `dim. proj((ℱ_{f(x)})_x) ∈ Φ`.*

*(vii) The set of `x ∈ X` such that `coprof((ℱ_{f(x)})_x) ∈ Φ`.*

*(viii) The set of `x ∈ X` such that `ℱ_{f(x)}` possesses property `(S_k)` at the point `x` `(5.7.2)`.*

*(ix) The set of `x ∈ X` such that `ℱ_{f(x)}` is a Cohen-Macaulay `𝒪_{X_{f(x)}}`-Module at the point `x` `(5.7.1)`.*

**(i)** The support `Z` of `ℱ` is locally constructible and closed in `X` `(8.9.1)`, and considering a sub-prescheme of
`X` having `Z` as underlying space and which is of finite presentation over `S` `(8.9.1)`, one sees that assertion (i)
is a special case of `(9.9.1, (iii))`.

**(ii)** All the properties considered are local on `X`, and we shall therefore restrict to the case where `X = Spec(B)`
and `S = Spec(A)` are affine and `f` a morphism of finite presentation. We keep the notations of the start of the proof
of `(9.9.1)`, and moreover suppose `A_0` chosen so that there exists a coherent `𝒪_{X_0}`-Module `ℱ_0` such that `ℱ` is
isomorphic to `ℱ_0 ⊗_{A_0} A`. Then (`(4.2.7)` and `(4.7.9)`) the set of geometric lengths of `(ℱ_0)_{f(x_0)}` at the
generic points of the irreducible components of `Supp((ℱ_0)_{f(x_0)})` which contain `x_0` is the same as the analogous
set for `x` and `ℱ_{f(x)}`; otherwise put, if `E` (resp. `E_0`) is the set of `x ∈ X` (resp. of `x_0 ∈ X_0`) verifying
condition (ii) of the statement, one has `E = h^{-1}(E_0)`, and by virtue of `(1.8.2)`, one sees that one may restrict
to considering the case where `A` is Noetherian. As in the proof of `(9.9.1)`, one sees that one is reduced to showing
that, for every `x ∈ X`, there exists a neighbourhood `V` of `x` in `‾{x}` such that, for every `x' ∈ V`, the set of
geometric lengths of `ℱ_{f(x')}` at the generic points of the irreducible components of its support containing `x'` is
the same. Moreover, if `S'` is the reduced sub-prescheme of `S` having `‾{f(x)}` as underlying space, and if
`X' = f^{-1}(S')`, the fibres of `X` and of `X'` at points of `S'` are the same,

<!-- original page 91 -->

so we may replace `S` by `S'` and `X` by `X'`, otherwise put suppose that `S` is integral and that `η = f(x)` is its
generic point.

Now, if one sets `Z = Supp(ℱ)`, the same reasoning as in the proof of `(9.9.1)` shows that, if `Z_i` are the irreducible
components of `Z` containing `x`, one may suppose that these are exactly the irreducible components of `Z` meeting
`‾{x}` and that `(Z_i)_s ∩ ‾{x} ≠ ∅` for every `s ∈ S`. The conclusion then follows from `(9.8.3)` and `(9.8.6)`.

**(iii)** One reduces as in (ii) to the case where `S` is Noetherian and integral and `η = f(x)` its generic point,
using `(4.2.7)`. As in the proof of `(9.9.1)`, one is reduced to showing that there exists a neighbourhood `V` of `x` in
`‾{x}` such that, for every `x' ∈ V`, the set of dimensions of the prime cycles associated to `ℱ_{f(x')}` which contain
`x'` is the same. Now, if `Z'_i` are the closures in `X` of the prime cycles associated to `ℱ_η` which contain `x` (cf.
`(9.8.2)`), it follows from `(9.8.3)` and `(9.5.1)` that for every `s` sufficiently near `η`, the prime cycles
associated to `ℱ_s` which meet `‾{x}` are irreducible components of the `(Z'_i)_s` and, by virtue of `(9.5.6)`, all
these irreducible components have the same dimension equal to `dim((Z'_i)_η)`, whence the conclusion.

**(iv)** One reasons as in (iii), using this time `(4.7.11)`. With the same notations as in (iii), the prime cycles
associated to `ℱ_s` which are irreducible components of `(Z'_i)_s` are embedded if and only if `(Z'_i)_η` is an embedded
associated prime cycle of `ℱ_η`. One concludes already that if `x` belongs to (resp. does not belong to any) embedded
associated prime cycle of `ℱ_η`, the set of `x' ∈ ‾{x}` such that `x'` belongs to (resp. does not belong to any)
embedded associated prime cycle of `ℱ_{f(x')}` is a neighbourhood of `x` in `‾{x}`. The conclusion follows from this
remark, from the characterization of points where a Module is geometrically reduced `(4.7.10)`, and from (ii).

**(v)** Taking `(4.7.11)` into account, we reduce again to the case where `S` is Noetherian and integral and where
`η = f(x)` is its generic point. Let `Y` be a closed sub-prescheme of `X` having `Supp(ℱ_η)` as underlying space.
Reasoning as at the start of the proof of `(9.7.7)`, one sees that there exists an integral finite `A`-algebra `A'` (so
that if `S' = Spec(A')`, the morphism `S' → S` is finite and surjective) such that if `Y' = Y_{(S')}` and if `η'` is the
generic point of `S'`, the irreducible components of `Y'_{η'}` are geometrically irreducible. On the other hand, if
`X' = X_{(S')}`, the projection morphism `h : X' → X` is finite and surjective, hence closed; consequently, if `x'` is a
point of `X'` above `x`, one has `h(‾{x'}) = ‾{x}` and the image under `h` of a neighbourhood of `x'` in `‾{x'}` is a
neighbourhood of `x` in `‾{x}`. Taking `(4.7.11)` into account and setting `ℱ' = ℱ_{(S')}`, we are therefore reduced to
proving that if `ℱ'` is (resp. is not) geometrically integral at the point `x'`, the set of `y' ∈ ‾{x'}` such that
`ℱ'_{f'(y')}` (where `f' = f_{(S')} : X' → S'`) is (resp. is not) geometrically integral at the point `y'` is a
neighbourhood of `x'` in `‾{x'}`. We may therefore restrict to the case where `X' = X` and where the irreducible
components of `Y_η` are geometrically irreducible; if one denotes by `Z_i` closed parts of `X` such that the `Z_i ∩ X_η`
are the

<!-- original page 92 -->

irreducible components of `Y_η`, it follows from `(9.7.7)`, `(9.7.8)`, and `(9.5.3)` that for every `s` near `η`, the
`(Z_i)_s` are the irreducible components of `Y_s` and that they are geometrically irreducible. To say that at a point
`y ∈ X_s`, `ℱ_s` is geometrically integral means then that `ℱ_s` is geometrically reduced at this point and moreover
that `y` belongs to only one of the `(Z_i)_s` `(4.6.22)`. The conclusion therefore follows on the one hand from (iv) and
on the other from `(9.5.1)` applied to the intersection of `‾{x}` and each `Z_i`.

**(vi)** Keeping the same notations as in (ii), it follows from `(6.2.1)` that one has
`dim. proj((ℱ_s)_x) = dim. proj(((ℱ_0)_{s_0})_{x_0})`; one may therefore again restrict to the case where `A` is
Noetherian. Moreover, one reduces again to showing that, for every `x ∈ X`, there exists a neighbourhood `V` of `x` in
`‾{x}` such that, for every `x' ∈ V`, one has `dim. proj((ℱ_{f(x')})_{x'}) = dim. proj((ℱ_{f(x)})_x)`; and as above, we
may suppose that `S` is integral and that `η = f(x)` is its generic point, so that one has `(ℱ_η)_x = ℱ_x`. By virtue of
the generic flatness theorem `(6.9.1)`, we may, by replacing `S` if necessary by an open neighbourhood of `η`, suppose
that the morphism `f` is flat and that `ℱ` is `f`-flat; one then has `dim. proj((ℱ_{f(x')})_{x'}) = dim. proj(ℱ_{x'})`
for every `x' ∈ X` by virtue of `(6.2.3)`. This being so, by virtue of `(6.11.1)`, we may (by replacing `X` if necessary
by an open neighbourhood of `x`) suppose that `dim. proj(ℱ_{x'}) ≤ dim. proj(ℱ_x)` for every `x' ∈ X`. On the other
hand, if `dim. proj(ℱ_x) = n`, there is by hypothesis a finitely generated `𝒪_x`-module `M` such that
`Ext^n_{𝒪_x}(ℱ_x, M) ≠ 0` `(0, 17.2.4)`. Now, there exists a coherent `𝒪_X`-Module `𝒢` such that `M = 𝒢_x` (by replacing
`X` if necessary by an open neighbourhood of `x` `(0_I, 5.3.8)`); by virtue of `(T, 4.2.2)`, one therefore has
`(𝓔𝓍𝓉^n_{𝒪_X}(ℱ, 𝒢))_x ≠ 0`. But `𝓔𝓍𝓉^n_{𝒪_X}(ℱ, 𝒢)` is a coherent `𝒪_X`-Module `(0_III, 12.3.3)`, so its support `Y` is
closed `(0_I, 5.2.2)`; since it contains `x`, it also contains `‾{x}`, from which one concludes (by applying
`(T, 4.2.2)` again) that one has `dim. proj(ℱ_{x'}) ≥ n` for every `x' ∈ ‾{x}`, which completes the proof of the
assertion in case (vi).

**(vii)** Since `B` is a finitely generated `A`-algebra, `X` is `S`-isomorphic to a closed sub-scheme of an `S`-scheme
of the form `Y = Spec(A[T_1, …, T_r])`; if `j : X → Y` is the canonical injection, and `𝒢 = j_*(ℱ)`, one has
`𝒢_s = (j_s)_*(ℱ_s)` for every `s ∈ S`, and, by virtue of `(0, 16.4.11)`, we may restrict to proving the assertion for
`Y` and `𝒢`. Otherwise put, we may suppose that `B = A[T_1, …, T_r]`, so that each of the schemes
`X_s = Spec(k(s)[T_1, …, T_r])` is regular `(0, 17.3.7)`. Let then `W = Supp(ℱ)`, so that `W_s = Supp(ℱ_s)`
`(I, 9.1.13)`; one has, by `(6.11.2.1)`:

```text
(9.9.2.1)     coprof((ℱ_{f(x)})_x) = dim. proj((ℱ_{f(x)})_x) − codim_x(W_{f(x)}, X_{f(x)}).
```

But since `W` is constructible `(8.9.1)` and each `W_s` is closed, it follows from (vi) and from `(9.9.1, (ii))` that
the two functions in the right-hand side of `(9.9.2.1)` are constructible; the same is therefore true of their
difference, which completes the proof of the proposition in case (vii).

**(viii)** Let `U_n` be the set of `x ∈ X` such that `coprof((ℱ_{f(x)})_x) ≤ n`, and set `Z_n = X − U_n`; it follows
from (vii) that the `Z_n` are constructible; moreover, since the function

<!-- original page 93 -->

`x ↦ dim_x(W_{f(x)})` is constructible by virtue of `(9.9.1, (i))`, it takes only finitely many values, hence the
numbers `dim(W_{f(x)})` have a finite upper bound `m` as `x` ranges over `X`; since
`coprof((ℱ_{f(x)})_x) ≤ dim((ℱ_{f(x)})_x) ≤ dim(W_{f(x)})`, one sees that `Z_n = ∅` for `n ≥ m`. Finally, it follows
from `(6.11.2, (i))` that for every `n` and every `s ∈ S`, `(Z_n)_s` is closed in `X_s`. According to `(5.7.4)`, the set
of `x ∈ X` where `(ℱ_{f(x)})_x` possesses property `(S_k)` is the set of `x ∈ X` verifying all the relations

```text
(9.9.2.2)               codim_x((Z_n)_{f(x)}, W_{f(x)}) ≥ n + k
```

for every `n ≥ 0`; since this relation is automatically verified for `n ≥ m`, one only has to consider relations
`(9.9.2.2)` for `0 ≤ n < m`. But by virtue of `(9.9.1, (ii))`, the set `V_{n,k}` of `x` verifying `(9.9.2.2)` is
constructible, and the same is true of the intersection of these sets for `0 ≤ n < m`.

**(ix)** The assertion here follows at once from (vii), the set of `x ∈ X` where `(ℱ_{f(x)})_x` is a Cohen-Macaulay
module being defined by the relation `coprof((ℱ_{f(x)})_x) = 0`.

**Corollary (9.9.3).**

<!-- label: IV.9.9.3 -->

*Let `f : X → S` be a morphism of finite presentation, `ℱ` an `𝒪_X`-Module of finite presentation, `P` one of the
properties (i) to (ix) of `(9.9.2)`. Then the set of `s ∈ S` such that property `P` is true at every point `x ∈ X_s` is
locally constructible in `S`.*

Indeed, its complement is the image under `f` of the complement of the set `E` of points where `P` is true. Since `E` is
locally constructible in `X`, the same is true of `X − E`, hence `f(X − E)` is locally constructible in `S` by virtue of
Chevalley's theorem `(1.8.4)`.

**Proposition (9.9.4).**

<!-- label: IV.9.9.4 -->

*Let `f : X → S` be a morphism locally of finite presentation.*

*The set of `x ∈ X` such that `X_{f(x)}` has at the point `x` one (a fixed one) of the following properties:*

*(i) being geometrically regular;*

*(ii) possessing the geometric property `(R_k)`;*

*(iii) being geometrically normal;*

*(iv) being geometrically reduced (i.e. separable);*

*(v) being geometrically pointwise integral;*

*is a locally constructible part of `X`.*

For properties (iv) and (v), this follows from `(9.9.2, (iv)` and `(v))` applied to `ℱ = 𝒪_X`. For the other properties,
taking `(6.7.8)` into account, one reduces, as at the start of `(9.9.2)`, to the case where `S` is Noetherian and
integral with generic point `η = f(x)`. Moreover, by virtue of the generic flatness theorem `(6.9.1)`, we may, by
replacing `S` by an open neighbourhood of `η`, suppose that `f` is a flat morphism. To say that `X_{f(y)}` is
geometrically regular at the point `y` means then that `f` is regular at the point `y` `(6.8.1)`, and we know that the
set `L` of these points is open in `X` `(6.8.7)`, which proves the proposition in case (i).

To prove case (ii), set `F = X − L`, which is closed in `X`. To say that `X_s`

<!-- original page 94 -->

verifies the geometric property `(R_k)` at the point `y ∈ f^{-1}(s)` means either that `y ∈ L`, or that the generic
points `z_i` of the irreducible components of the closed set `F_s` which contain `y` verify the relation
`dim(𝒪_{X_s, z_i}) ≥ k + 1` (taking `(4.2.7)` and `(5.2.3)` into account); otherwise put, the points `y ∈ F_s` where
`X_s` verifies the geometric property `(R_k)` are those such that `codim_y(F_s, X_s) ≥ k + 1` `(5.1.2)`. The conclusion
therefore follows from (i) and from `(9.9.1, (ii))`.

Finally, in case (iii), the conclusion follows from (ii), from `(9.9.2, (viii))`, from the fact that property `(S_k)` is
stable under extension of the base field `(6.7.1)`, and finally from Serre's criterion `(5.8.6)`.

**Corollary (9.9.5).**

<!-- label: IV.9.9.5 -->

*Let `f : X → S` be a morphism of finite presentation, and denote by `P` one of the properties (i) to (v) of `(9.9.4)`.
Then the set of `s ∈ S` such that property `P` is true at every point `x ∈ X_s` is locally constructible in `S`.*

The proof from `(9.9.4)` is the same as that of `(9.9.3)` from `(9.9.2)`.

**Proposition (9.9.6).**

<!-- label: IV.9.9.6 -->

*Let `f : X → S` be a morphism locally of finite presentation, `ℒ_•` a complex formed of quasi-coherent `𝒪_X`-Modules of
finite presentation; for every `s ∈ S`, let `(ℒ_•)_s` be the complex `ℒ_• ⊗ k(s)` of `𝒪_{X_s}`-Modules of finite type.
Then, for a given integer `n`, the set of `x ∈ X` such that `(ℋ_n((ℒ_•)_{f(x)}))_x = 0` is locally constructible in
`X`.*

We may restrict to the case where `ℒ_i = 0` except for `i = 0`, `1`, or `2`, and where `n = 1`. Moreover, the question
being local on `X`, we may restrict to the case where `S = Spec(A)` and `X = Spec(B)` are affine, `B` being an
`A`-algebra of finite presentation. There then exists a Noetherian subring `A_0` of `A`, an `A_0`-prescheme of finite
type `X_0`, and a complex `ℒ^{(0)}_•` of coherent `𝒪_{X_0}`-Modules, zero except in dimensions `0`, `1`, and `2`, such
that `X = X_0 ⊗_{A_0} A` and `ℒ_• = ℒ^{(0)}_• ⊗_{A_0} A`. For every `s ∈ S`, if `s_0` is the projection of `s` in
`S_0 = Spec(A_0)`, one has `X_s = (X_0)_{s_0} ⊗_{k(s_0)} k(s)`, and the projection morphism `X_s → (X_0)_{s_0}` is
faithfully flat; one concludes that one has `ℋ_n((ℒ_•)_s) = ℋ_n((ℒ^{(0)}_•)_{s_0}) ⊗_{k(s_0)} k(s)`, and consequently,
if `E` (resp. `E_0`) is the set of `x ∈ X` (resp. `x_0 ∈ X_0`) such that `(ℋ_n((ℒ_•)_{f(x)}))_x = 0` (resp.
`(ℋ_n((ℒ^{(0)}_•)_{f(x_0)}))_{x_0} = 0`), one has `E = h^{-1}(E_0)`, where `h : X → X_0` is the canonical projection. By
virtue of `(1.8.2)`, we may therefore restrict to the case where `A` is Noetherian; the question is to see
`(0_III, 9.2.3)` that if `x ∈ X` is such that `(ℋ_n((ℒ_•)_{f(x)}))_x = 0` (resp. `≠ 0`), there exists an open
neighbourhood `V` of `x` in `‾{x}` such that, for every `x' ∈ V`, one has `(ℋ_n((ℒ_•)_{f(x')}))_{x'} = 0` (resp. `≠ 0`).
Replacing `S` by the reduced sub-prescheme of `S` having `‾{f(x)}` as underlying space, we may suppose that `S` is
integral and that `f(x) = η` is its generic point. Then, by restricting `S` to an open neighbourhood of `η`, we may
suppose that for every `s ∈ S`, one has `(ℋ_n(ℒ_•))_s = ℋ_n((ℒ_•)_s)` `(9.4.3)`, and consequently, if `Z` is the support
of `ℋ_n(ℒ_•)`, the support of `ℋ_n((ℒ_•)_s)` is `Z_s = Z ∩ X_s` `(I, 9.1.13.1)`. The hypothesis is that `Z_η ∩ ‾{x} = ∅`
(resp. `≠ ∅`). Since `Z ∩ ‾{x}` is closed in the Noetherian space `X`, one concludes from `(9.5.1)` that there is a
neighbourhood `U` of `η` in `S` such that, for every `s ∈ U`, one has `Z_s ∩ ‾{x} = ∅` (resp. `≠ ∅`). The set
`V = f^{-1}(U) ∩ ‾{x}` therefore answers the question.
