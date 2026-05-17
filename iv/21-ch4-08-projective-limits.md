<!-- original page 5 -->

## §8. Projective limits of preschemes

### 8.1. Introduction

**(8.1.1)** In this section we shall systematically study the following situation. Let `I` be a filtered (increasing)
preordered set, `(A_α, φ_{βα})` an inductive system of rings indexed by `I`, and `A = lim A_α` its inductive limit. For
every `α ∈ I` and every `A_α`-prescheme `X_α`, consider the `A_λ`-preschemes `X_λ = X_α ⊗_{A_α} A_λ` for `λ ≥ α`, and
the `A`-prescheme `X = X_α ⊗_{A_α} A`; it is clear that the preschemes `X_λ` (for `λ ≥ α`) form a projective system, and
one will see `(8.2.5)` that `X` is a projective limit of this system in the category of preschemes. We propose to find
conditions on `X_α` or on the `A_λ` allowing us to prove properties of the following type: in order that `X` possess a
property `P` (for example, the property of being proper over `S = Spec(A)`, or irreducible, or connected, etc.), it is
necessary and sufficient that there exist an index `μ ≥ α` such that, for every `λ ≥ μ`, `X_λ` has (with respect to
`S_λ = Spec(A_λ)`, if applicable) the same property `P`. We shall obtain analogous statements for properties of
`𝒪`-Modules, of `A`-morphisms of `A`-preschemes, etc. We shall also show `(8.9.1)` that giving an `A`-prescheme of
finite presentation `(1.6.1)` is essentially equivalent to giving an `A_λ`-prescheme of finite presentation `X_λ` for
`λ` large enough, `X` being then isomorphic to `X_λ ⊗_{A_λ} A`. One has analogous statements for `𝒪_X`-Modules of finite
presentation, their homomorphisms, the `A`-morphisms of `A`-preschemes of finite presentation, etc.

**(8.1.2)** The utility of such results will appear, for example, in the following questions:

a) Let `Y` be a prescheme, `y` a point of `Y`, `(U_α)` the filtered (decreasing) projective system of affine open
neighbourhoods of `y` in `Y`; if `A_α` is the ring of `U_α`, the `A_α` form a filtered (increasing) inductive system
whose inductive limit `A` is the local ring `𝒪_y`. Moreover, if one denotes by `𝔭_α` the prime ideal of `y` in the ring
`A_α`, the inductive system `(A_α)` is cofinal with every inductive system `(A_{α,f})`, where `f` runs through
`A_α − 𝔭_α` (for a fixed `α`), since the `D(f)` form a fundamental system of neighbourhoods of `y` in `U_α`, hence in
`Y`. The results of the present section will imply that the algebraic geometry of `𝒪_y`-preschemes of finite
presentation (and the theory of Modules of finite presentation on these preschemes) is essentially equivalent to the
algebraic geometry of preschemes of finite presentation on "sufficiently small" open neighbourhoods of `y`. Thus, the
statement `(8.10.5, (xiii))` implies that if a morphism `f : X → Y` is of finite presentation, then, in order that
`X ×_Y Spec(𝒪_y)` be proper over `Spec(𝒪_y)`, it is necessary and sufficient that there exist an open neighbourhood `U`
of `y` in `Y` such that `f⁻¹(U)` be proper over `U`.

<!-- original page 6 -->

A particularly important case, and to a certain extent classical, is that in which `Y` is integral and `y` is its
generic point, so that `𝒪_y` is none other than the field `R(Y) = K` of rational functions on `Y`. The results of the
present section then amount to interpreting the algebraic geometry over `K` in terms of the algebraic geometry above
non-empty "sufficiently small" open sets of `Y`, that is to say, intuitively, in terms of "families" of geometric
objects indexed by the points of such an open set. This point of view has moreover been commonly used for a long time,
not only in algebraic geometry over algebraically closed fields, but also in the arithmetic study of varieties defined
over a number field `K` (finite extension of `ℚ`), by considering this latter as the field of fractions of its ring of
integers `A` ("theory of reduction modulo `𝔭`", `𝔭` a prime ideal of `A`; cf. `(I, 3.7)`). The results of §§8 and 9 thus
furnish among other things foundations of the language of "reduction modulo `𝔭`" in arithmetic.

One will note that in the example envisaged here, the morphisms `S_μ → S_λ` (for `λ ≤ μ`) are the canonical open
immersions `U_μ → U_λ`, and *a fortiori* are flat morphisms (but not faithfully flat in general), which explains the
interest of statements that appeal to such a restriction.

b) Suppose that the `A_λ` are *fields*, so that `A = lim A_λ` is also a field. This case generally arises when one
starts from geometric data above an arbitrary field `K`, which one considers as an extension of a field `k` (for example
the prime subfield of `K`). It is then advantageous to consider `K` as the inductive limit of its sub-extensions that
are *of finite type over `k`*, which permits in many questions to reduce to the case where `K` is an extension of finite
type of `k`. Using also the method sketched in a), one can then generally reduce to the case of a base ring `A` that is
*an integral algebra of finite type over `k`*.

One will note that in this example, the morphisms `S_μ → S_λ` are faithfully flat.

c) Suppose one is interested in the properties, local on `Y`, of preschemes of finite presentation above an arbitrary
prescheme `Y`, which one may therefore assume affine with ring `A`. It is then advantageous to consider `A` as the
inductive limit of its sub-rings that are `ℤ`-algebras of finite type, which permits to reduce many questions to the
case where `Y` is the spectrum of such an algebra. This is the explicit form of the "Kroneckerian point of view",
according to which algebraic geometry reduces to the algebraic geometry of preschemes of finite type over `ℤ` (which is
sometimes called "absolute algebraic geometry"). This example shows us in particular that in most "relative" questions
over a base prescheme `Y`, one can reduce to the case where `Y` is Noetherian.

One will note that in this example, contrary to the preceding ones, the morphisms `S_μ → S_λ` have in general no
particular regularity property.

In what follows, when we apply the results that follow to any one of the three particular situations just described, we
shall dispense with redescribing in detail the procedure that permits these applications, contenting ourselves with
referring back to the foregoing.

**(8.1.3)** In example a) of `(8.1.2)`, we saw that if `Y` is an integral prescheme with generic point `y`, and
`f : X → Y` a morphism of finite presentation, then, if the generic fibre `f⁻¹(y)` is proper over `k(y)`, there is an
open neighbourhood `U` of `y` such that `f⁻¹(U)` is proper over `U`; *a fortiori*, for every `s ∈ U`, `f⁻¹(s)` is proper
over `k(s)`. There are occasions when one needs a converse, asserting that if `f⁻¹(s)` is proper over `k(s)` for
"sufficiently many" points `s ∈ U`, then `f⁻¹(y)` is proper over `k(y)`. For example, suppose that `X` and `Y` are
algebraic preschemes over an algebraically closed field `k` (one can take for `k` the field `ℂ` of complex numbers, to
fix the ideas); one sometimes needs to know that if, for every `s ∈ Y` rational over `k`, the fibre `f⁻¹(s)` is proper
over `k(s)`, then `f⁻¹(y)` is proper over `k(y)`, and consequently `f⁻¹(U)` is proper over `U` for some neighbourhood
`U` of `y` (¹). Now this statement will follow easily from the following: the set `E` of points `s ∈ Y` such that
`f⁻¹(s)` is proper over `k(s)` is *constructible* (and consequently identical to all of `Y` if it contains the closed
points of `Y`, thanks to Hilbert's Nullstellensatz `(10.4.8)`); this also amounts to saying that if `f⁻¹(y)` is not
proper over `k(y)`, then there exists an open neighbourhood `U` of `y` such that `f⁻¹(s)` is not proper over `k(s)` for
every `s ∈ U` (cf. `(9.6.1, (iv))`). This example illustrates the interest of systematically developing
*constructibility criteria* for the most important notions: this is what will be done in §9.

> (¹) One will note that such a statement is in the end purely geometric, in the sense that it only appeals to points
> rational over `k`, and not to generic points; for example, when `k = ℂ`, this statement has an obvious topological
> meaning for the analyst, when one interprets "proper" in the topological sense of the term, for the spaces underlying
> the analytic spaces formed by the points of `X` and `Y` rational over `ℂ`.

<!-- original page 7 -->

### 8.2. Projective limits of preschemes

**(8.2.1)** Let `S_0` be a ringed space, `L` a filtered (increasing) preordered set, `(𝒜_λ, φ_{μλ})` an inductive system
of `𝒪_{S_0}`-Algebras (not necessarily commutative) indexed by `L`. One knows that, considered as an inductive system of
`𝒪_{S_0}`-Modules, `(𝒜_λ, φ_{μλ})` admits an inductive limit `𝒜`; let us denote by `φ_λ : 𝒜_λ → 𝒜` the canonical
homomorphism (of `𝒪_{S_0}`-Modules). Let `m_λ : 𝒜_λ ⊗ 𝒜_λ → 𝒜_λ` be the homomorphism of `𝒪_{S_0}`-Modules that defines
the multiplication in the `𝒪_{S_0}`-Algebra `𝒜_λ`; the hypothesis on the `φ_{μλ}` entails that the `m_λ` form an
inductive system of homomorphisms, and since the functor `lim` commutes with tensor product, `m = lim m_λ` is a
homomorphism `𝒜 ⊗ 𝒜 → 𝒜` of `𝒪_{S_0}`-Modules; by passage to the limit on the commutative diagrams expressing the
associativity of `m_λ` and the existence of a unit section in `𝒜_λ`, one sees that `m` defines on `𝒜` a structure of
`𝒪_{S_0}`-Algebra and that `φ_λ` is a homomorphism of `𝒪_{S_0}`-Algebras for every `λ ∈ L`. Moreover `𝒜` is the
inductive limit of the system `(𝒜_λ, φ_{μλ})` in the category of `𝒪_{S_0}`-Algebras; in other words, for every
`𝒪_{S_0}`-Algebra `ℬ`, the canonical map

```text
  (8.2.1.1)    Hom_{S_0-Alg.}(𝒜, ℬ) → lim Hom_{S_0-Alg.}(𝒜_λ, ℬ)
```

which to every homomorphism `f : 𝒜 → ℬ` of `𝒪_{S_0}`-Algebras associates the family `(f ∘ φ_λ)`, is bijective. Indeed,
one already knows that it is injective and identifies `Hom_{S_0-Alg.}(𝒜, ℬ)` with a part of
`lim Hom_{S_0-Mod.}(𝒜_λ, ℬ)`; everything comes down to seeing that if `(f_λ)` is an inductive system of homomorphisms of
`𝒪_{S_0}`-Algebras, `f_λ : 𝒜_λ → ℬ`, its inductive limit `f : 𝒜 → ℬ`, which by definition is a homomorphism of
`𝒪_{S_0}`-Modules, is also a homomorphism of `𝒪_{S_0}`-Algebras; but this results from passage to the inductive limit in
the commutative diagram of homomorphisms of `𝒪_{S_0}`-Modules expressing that the `f_λ` are Algebra homomorphisms, and
from the fact that the functor `lim` commutes with tensor products.

One will note finally that if the `𝒜_λ` are commutative `𝒪_{S_0}`-Algebras, the same is true of `𝒜`.

**(8.2.2)** Suppose now that `S_0` is a prescheme and that the `𝒜_λ` are *quasi-coherent* (commutative)
`𝒪_{S_0}`-Algebras; one knows then that `𝒜 = lim 𝒜_λ` is a quasi-coherent `𝒪_{S_0}`-Algebra `(I, 4.1.1)`. Let us denote
by `S_λ` (resp. `S`) the spectrum of the `𝒪_{S_0}`-Algebra `𝒜_λ` (resp. `𝒜`) `(II, 1.3.1)`, and let `u_{μλ} : S_μ → S_λ`
(for `λ ≤ μ`) and `u_λ : S → S_λ` be the `S_0`-morphisms corresponding to the homomorphisms `φ_{μλ}` and `φ_λ`
respectively `(II, 1.2.7)`; it is clear that `(S_λ, u_{μλ})` is a projective system in the category of `S_0`-preschemes.
One will note that the `u_{μλ}` and `u_λ` are *affine* morphisms `(II, 1.6.2)`, hence *quasi-compact* and *separated*.

**Proposition (8.2.3).**

<!-- label: IV.8.2.3 -->

*With the notations of `(8.2.2)`, the morphisms `u_λ : S → S_λ` make `S` a projective limit of the projective system
`(S_λ, u_{μλ})` in the category of preschemes. Moreover, if `h : S_0 → T` is a morphism, making every `S_0`-prescheme a
`T`-prescheme, `S` is also a projective limit of the system `(S_λ, u_{μλ})` in the category of `T`-preschemes.*

Let us first prove the second assertion of the statement in the case `T = S_0`.

<!-- original page 8 -->

Everything comes down to showing that if `X` is an arbitrary `S_0`-prescheme, the canonical map

```text
  (8.2.3.1)    Hom_{S_0}(X, S) → lim Hom_{S_0}(X, S_λ)
```

which to every `S_0`-morphism `v : X → S` associates the family `(u_λ ∘ v)`, is bijective. Now, if `g : X → S_0` is the
structure morphism and if one sets `ℬ = g_*(𝒪_X)`, which is an `𝒪_{S_0}`-Algebra, the map `(8.2.3.1)` is canonically
identified with `(8.2.1.1)` `(II, 1.2.7)`, and the conclusion therefore results from what was seen in `(8.2.1)`.

The other assertions of `(8.2.3)` are consequences of the following general lemma:

**Lemma (8.2.4).**

<!-- label: IV.8.2.4 -->

*Let `𝒞` be a category, `T` an object of `𝒞`, `𝒞_T` the subcategory of objects of `𝒞` above `T`. Let `(S_λ, u_{μλ})` be
a projective system in `𝒞_T`; then every projective limit of this system in `𝒞_T` is also a projective limit in `𝒞`, and
conversely.*

Let `f_λ : S_λ → T` be the structure morphism. Suppose that `S` is a projective limit of `(S_λ, u_{μλ})` in `𝒞`, and
denote by `u_λ : S → S_λ` the corresponding canonical morphisms. Consider then a projective system of `T`-morphisms
`w_λ : Y → S_λ`, where `Y ∈ 𝒞_T`. There exists by hypothesis a unique morphism `w : Y → S` (in `𝒞`) such that
`w_λ = u_λ ∘ w` for every `λ`. The hypothesis that the `u_λ` are `T`-morphisms entails that the morphisms
`f_λ ∘ u_λ : S → T` are all equal, and this morphism `f` therefore makes `S` a `T`-object. If `g : Y → T` is the
structure morphism of `Y`, one has then `f ∘ w = f_λ ∘ u_λ ∘ w = f_λ ∘ w_λ = g` for every `λ`, which proves that `w` is
a `T`-morphism. Conversely, suppose (with the same notations) that `S` is a projective limit of `(S_λ, u_{μλ})` in
`𝒞_T`, and consider now a projective system of morphisms (of `𝒞`) `w_λ : Y → S_λ`. The composite morphisms
`f_λ ∘ w_λ : Y → T` are then all equal: indeed, for any two indices `λ`, `μ`, there is an index `ν` such that `λ ≤ ν`
and `μ ≤ ν`, whence `f_ν = f_λ ∘ u_{λν} = f_μ ∘ u_{μν}`; since `w_λ = u_{λν} ∘ w_ν` and `w_μ = u_{μν} ∘ w_ν`, one has
`f_λ ∘ w_λ = f_λ ∘ u_{λν} ∘ w_ν = f_ν ∘ w_ν` and one sees in the same way that `f_μ ∘ w_μ = f_ν ∘ w_ν`. If `g : Y → T`
is the unique morphism thus defined, `g` makes `Y` a `T`-object, and the `w_λ` are then `T`-morphisms; they consequently
have a projective limit `w : Y → S` which is a `T`-morphism, and *a fortiori* a morphism of `𝒞`; moreover the first part
of the reasoning shows that every projective limit `w'` (in `𝒞`) of the projective system `(w_λ)` is necessarily also a
`T`-morphism, hence equal to `w`, which completes the proof of the lemma.

**Proposition (8.2.5).**

<!-- label: IV.8.2.5 -->

*Under the conditions of `(8.2.2)`, let `α` be an element of `L`, `X_α` an `S_α`-prescheme. For every `λ ≥ α`, set
`X_λ = X_α ×_{S_α} S_λ`, and for `α ≤ λ ≤ μ`, set `v_{μλ} = 1_{X_α} × u_{μλ}`, so that `(X_λ, v_{μλ})` is a projective
system of `X_α`-preschemes, whose index set is formed of the `λ ≥ α` in `L`. Set likewise `X = X_α ×_{S_α} S` and
`v_λ = 1_{X_α} × u_λ`. Then the `X_α`-morphisms `v_λ : X → X_λ` make `X` a projective limit of the projective system
`(X_λ, v_{μλ})` in the category of `X_α`-preschemes, or in the category of all preschemes.*

This will again result from the following general lemma:

**Lemma (8.2.6).**

<!-- label: IV.8.2.6 -->

*Let `𝒞` be a category in which fibre products exist, `q : T' → T` a morphism of `𝒞`, `𝒞_T` (resp. `𝒞_{T'}`) the
category of objects of `𝒞` above `T` (resp. `T'`).*

<!-- original page 9 -->

*Let `(S_λ, u_{μλ})` be a projective system (not necessarily filtered) in `𝒞_T`, and set `S'_λ = S_λ ×_T T'`,
`u'_{μλ} = u_{μλ} × 1_{T'}`, so that `(S'_λ, u'_{μλ})` is a projective system in `𝒞_{T'}`. Then, if `(S, u_λ)` is a
projective limit of `(S_λ, u_{μλ})` in `𝒞_T`, `(S ×_T T', u_λ × 1_{T'})` is a projective limit of `(S'_λ, u'_{μλ})` in
`𝒞_{T'}`.*

One has by hypothesis, for every `λ`, a commutative diagram

```text
  S'  ──u'_λ──→  S'_λ  ──h'_λ──→  T'
   │              │                │
   p│            p_λ│               q
   ↓              ↓                ↓
   S   ──u_λ───→  S_λ  ───f_λ───→  T
```

where one has set `S' = S ×_T T'`, `u'_λ = u_λ × 1_{T'}`, `h'_λ = f_λ × 1_{T'}`. Let `Y` be a `T'`-object, `g' : Y → T'`
the corresponding morphism, and consider a projective system of `T'`-morphisms `w'_λ : Y → S'_λ`. Then `Y` is a
`T`-object via the morphism `g = q ∘ g'`, and the `w_λ = p_λ ∘ w'_λ` are `T`-morphisms, since
`h_λ ∘ w_λ = h_λ ∘ p_λ ∘ w'_λ = q ∘ h'_λ ∘ w'_λ = q ∘ g'` by hypothesis. Moreover, one verifies at once that `(w_λ)` is
a projective system. There exists therefore by hypothesis a unique `T`-morphism `w : Y → S` such that `u_λ ∘ w = w_λ`
for every `λ`. By definition of the fibre product, there is a unique `T'`-morphism `w' : Y → S'` such that `p ∘ w' = w`.
One has then `u_λ ∘ p ∘ w' = u_λ ∘ w = w_λ = p_λ ∘ w'_λ`, which can also be written `p_λ ∘ u'_λ ∘ w' = p_λ ∘ w'_λ`; on
the other hand, by writing that `w'` is a `T'`-morphism, one gets `h'_λ ∘ u'_λ ∘ w' = g' = h'_λ ∘ w'_λ`. The definition
of `S'_λ` as fibre product `S_λ ×_T T'` thus gives `u'_λ ∘ w' = w'_λ`, and it is immediate that `w'` is the unique
`T'`-morphism verifying these relations, whence the lemma.

**Remark (8.2.7).**

<!-- label: IV.8.2.7 -->

Given an arbitrary ringed space `S`, the inductive limits with respect to an arbitrary preordered set `L` (not
necessarily filtered) exist in the category of commutative `𝒪_S`-Algebras, since the filtered inductive limit exists by
`(8.2.1)` and on the other hand, for two homomorphisms of `𝒪_S`-Algebras `𝒜 → ℬ`, `𝒜 → 𝒞`, the tensor product `ℬ ⊗_𝒜 𝒞`
is the corresponding "amalgamated sum" in this category. When `S` is a prescheme, one knows that the tensor product
`ℬ ⊗_𝒜 𝒞` is a quasi-coherent `𝒪_S`-Algebra when this is so of `𝒜`, `ℬ` and `𝒞` `(I, 1.3.13)`; one concludes that, in
the category of *quasi-coherent* `𝒪_S`-Algebras, the inductive limits for an arbitrary preordered index set always
exist. This permits one to generalize the definition of a projective limit of preschemes and Propositions `(8.2.3)` and
`(8.2.5)` to the case where the preordered set `L` is not necessarily filtered.

**(8.2.8)** With the notations of `(8.2.2)`, set `u_{μλ} = (ψ_{μλ}, θ_{μλ})` and `u_λ = (ψ_λ, θ_λ)`; thus
`(S_λ, ψ_{μλ})` is a projective system of topological spaces and `(ψ_λ)` an inductive system of continuous maps
`S → S_λ` of the spaces underlying the preschemes `S` and `S_λ` respectively.

**Proposition (8.2.9).**

<!-- label: IV.8.2.9 -->

*With the notations of `(8.2.8)`, the projective limit of the projective system `(ψ_λ)` of continuous maps is a
homeomorphism of the space underlying `S` onto the projective limit of the projective system `(S_λ, ψ_{μλ})` of
topological spaces.*

Let `T` be the topological space limit of the system `(S_λ, ψ_{μλ})` and set `ψ = lim ψ_λ : S → T`. One may restrict to
the case where `S_0 = S_α` for some `α ∈ L`, and `λ ≥ α`.

<!-- original page 10 -->

(i) Let us show first that the topology of `S` is the inverse image under `ψ` of the topology of `T`; in other words, if
`π_λ : T → S_λ` is the canonical map, one must show that every open set of `S` is a union of open sets of the form
`ψ⁻¹(π_λ⁻¹(U_λ))`, where `U_λ` is open in `S_λ`. Now every open set of `S` is by definition a union of open sets
obtained as follows: one considers an affine open set `U_0` of `S_0`, with ring `A_0`, so that `u_0⁻¹(U_0)` is the
affine open set of `S` with ring `A = Γ(U_0, 𝒜)`, then one takes an element `f ∈ A` and one considers in `Spec(A)`,
identified with `u_0⁻¹(U_0)`, the open set `D(f)`. It is these open sets `D(f)` that form a base of the topology of `S`
`(II, 1.3.1)`. Now, if one sets `A_λ = Γ(U_0, 𝒜_λ)`, one has `A = lim A_λ` `(I, 1.3.9)`, so there exists an index `λ`
such that `f` is the canonical image of an element `f_λ ∈ A_λ`; one has then `D(f) = ψ_λ⁻¹(D(f_λ))` `(I, 1.2.2)`, and
since `ψ_λ = π_λ ∘ ψ`, our assertion is proved.

(ii) Let us now prove that `ψ` is bijective, which will complete the proof. Since `S` is a Kolmogorov space, it already
follows from (i) that `ψ` is injective, and it therefore remains to show that `ψ` is surjective. One can evidently
replace `T` for this purpose by an open set `π_0⁻¹(U_0)`, where `U_0` is an affine open set in `S_α = S_0`, so one can
limit oneself to the case where the `S_λ` and `S` are affine, in other words `𝒜_λ` is the sheaf associated with an
`A_0`-algebra `A_λ`, and `𝒜` the sheaf of algebras associated with `A = lim A_λ`; we shall again denote by
`φ_{μλ} : A_λ → A_μ` and `φ_λ : A_λ → A` the canonical homomorphisms. By definition, an element of `T` is a family
`(𝔭_λ)_{λ ∈ L}`, where `𝔭_λ` is a prime ideal of `A_λ` and where one has `𝔭_λ = φ_{μλ}⁻¹(𝔭_μ)` for `λ ≤ μ`. One knows
then `((5.13.3) and (5.13.1))` that there is a prime ideal `𝔭` of `A` such that `𝔭_λ = φ_λ⁻¹(𝔭)` for every `λ ∈ L`,
which completes the proof.

In particular, we have thus proved the

**Corollary (8.2.10).**

<!-- label: IV.8.2.10 -->

*Let `(A_λ)_{λ ∈ L}` be a filtered inductive system of rings, and let `A = lim A_λ`, `φ_λ : A_λ → A` the canonical
homomorphisms. The canonical map `𝔭 ↦ (φ_λ⁻¹(𝔭))` is a homeomorphism of `Spec(A)` onto the topological space
`lim Spec(A_λ)`.*

**Corollary (8.2.11).**

<!-- label: IV.8.2.11 -->

*With the notations of `(8.2.8)`, for every quasi-compact open set `U` of `S`, there exist an index `λ` and a
quasi-compact open set `U_λ` of `S_λ` such that `U = ψ_λ⁻¹(U_λ)`.*

This results from the fact that, by definition of the projective limit topology, the `ψ_λ⁻¹(U_λ)` (`U_λ` quasi-compact
open in `S_λ`) form a base of the topology of `S`, and from the fact that the index set `L` is filtered.

**Corollary (8.2.12).**

<!-- label: IV.8.2.12 -->

*With the notations of `(8.2.8)`, the inductive limit of the inductive system of homomorphisms
`θ_λ^{#} : ψ_λ^*(𝒪_{S_λ}) → 𝒪_S` of sheaves of rings on `S` is an isomorphism*

```text
  (8.2.12.1)    lim ψ_λ^*(𝒪_{S_λ}) ⥲ 𝒪_S.
```

One can evidently suppose the `S_λ` affine; with the notations of the proof of `(8.2.9)`, everything comes down to
seeing that the inductive limit of the system of canonical maps `(A_λ)_{𝔭_λ} → A_𝔭` is an isomorphism, which is none
other than `(5.13.3, (ii))`.

<!-- original page 11 -->

**Proposition (8.2.13).**

<!-- label: IV.8.2.13 -->

*Suppose that the morphisms `u_{μλ} : S_μ → S_λ` are open immersions, so that `S_μ` is identified with the sub-prescheme
induced on an open set of `S_λ` for `λ ≤ μ`. Then, for every `α ∈ L`, the space underlying the prescheme `S` is
identified with the subspace of `S_α` intersection of the `S_λ` for `λ ≥ α`, and the structure sheaf `𝒪_S` with the
sheaf induced `(G, II, 1.5)` by `𝒪_{S_α}` on this intersection; more generally, for every `𝒪_{S_α}`-Module `ℱ_α`,
`u_α^*(ℱ_α)` is identified with the `𝒪_S`-Module induced by `ℱ_α` on `S`.*

The first assertion results from `(8.2.9)`, in view of the definition of a projective limit of topological spaces; in
addition all the `ψ_λ^*(𝒪_{S_λ})` are equal to the sheaf induced by `𝒪_{S_α}` on `S` by definition `(0_I, 3.7.1)` and,
with the notations of the proof of `(8.2.9)`, the homomorphisms `(A_λ)_{𝔭_λ} → (A_α)_𝔭` are bijective for a system
`(𝔭_λ)` of prime ideals corresponding to a single point of `S`; the assertion relative to `𝒪_S` therefore follows from
`(8.2.12)`. The last assertion results then from the definition of `u_α^*(ℱ_α)` `(0_I, 4.3.1)`.

**Remark (8.2.14).**

<!-- label: IV.8.2.14 -->

The results of `(8.2.9)` and `(8.2.12)` show that `S` is the projective limit of the projective system `(S_λ, u_{μλ})`
in the category of all ringed spaces (or of all ringed spaces in local rings). Indeed, let `Y` be a ringed space, and
consider a projective system of morphisms of ringed spaces `w_λ : Y → S_λ`. If one sets `w_λ = (p_λ, ω_λ)`, the `p_λ`
form a projective system of continuous maps and, by virtue of `(8.2.9)`, their projective limit `p` is identified with a
continuous map `Y → S` such that `p_λ = ψ_λ ∘ p`. On the other hand, the `ω_λ^{#} : p_λ^*(𝒪_{S_λ}) → 𝒪_Y` form an
inductive system of homomorphisms of sheaves of rings; since one may write `p_λ^*(𝒪_{S_λ}) = p^*(ψ_λ^*(𝒪_{S_λ}))` and
the functor `p^*` is exact, the inductive limit of the `p_λ^*(𝒪_{S_λ})` is `p^*(𝒪_S)` by virtue of `(8.2.12)`, and there
is therefore a unique homomorphism `ω^{#} : p^*(𝒪_S) → 𝒪_Y` such that `ω_λ^{#} = ω^{#} ∘ p^*(θ_λ^{#})`, which proves our
assertion.

### 8.3. Constructible parts in a projective limit of preschemes

**(8.3.1)** In all that follows in this section, we suppose the conditions of `(8.2.2)` to be satisfied, and we preserve
its notations.

**Theorem (8.3.2).**

<!-- label: IV.8.3.2 -->

*For every `λ`, let `E_λ`, `F_λ` be two parts of `S_λ`. Set*

```text
  (8.3.2.1)    E = ⋂_λ u_λ⁻¹(E_λ),    F = ⋃_λ u_λ⁻¹(F_λ).
```

*Assume the following conditions:*

*(i) For every `λ`, `E_λ` is pro-constructible and `F_λ` is ind-constructible `(1.9.4)`.*

*(ii) For `λ ≤ μ`, one has `u_{μλ}⁻¹(E_λ) ⊃ E_μ` and `u_{μλ}⁻¹(F_λ) ⊂ F_μ`.*

*(iii) There exists `α ∈ L` such that `S_α` is quasi-compact (which entails that `S_λ` is quasi-compact for `λ ≥ α`).*

*Then the following properties are equivalent:*

*a) `E ⊂ F`.*

<!-- original page 12 -->

*b) There exists `λ ≥ α` such that `u_λ⁻¹(E_λ) ⊂ u_λ⁻¹(F_λ)` (and one then has `u_μ⁻¹(E_μ) ⊂ u_μ⁻¹(F_μ)` for `μ ≥ λ`).*

*c) There exists `λ ≥ α` such that `E_λ ⊂ F_λ` (and one then has `E_μ ⊂ F_μ` for `μ ≥ λ`).*

The remarks in parentheses in b) and c) result from (ii). Set

```text
  G_λ = E_λ ∩ (S_λ − F_λ),    G = E ∩ (S − F).
```

Then `G_λ` is a pro-constructible part of `S_λ` `(1.9.5, (i))`, and by virtue of `(8.3.2.1)` and (ii), one has
`G = ⋂_λ u_λ⁻¹(G_λ)`.

One is thus reduced to proving the particular case of `(8.3.2)` corresponding to `F_λ = ∅` for every `λ`:

**Corollary (8.3.3).**

<!-- label: IV.8.3.3 -->

*For every `λ`, let `E_λ` be a pro-constructible part of `S_λ` such that, for `λ ≤ μ`, one has `E_μ ⊂ u_{μλ}⁻¹(E_λ)`.
Suppose there exists `α ∈ L` such that `S_α` is quasi-compact. Then the following conditions are equivalent:*

*a) `E = ⋂_λ u_λ⁻¹(E_λ) = ∅`.*

*b) There exists `λ` such that `u_λ⁻¹(E_λ) = ∅` (and then `u_μ⁻¹(E_μ) = ∅` for `μ ≥ λ`).*

*c) There exists `λ` such that `E_λ = ∅` (and then `E_μ = ∅` for `μ ≥ λ`).*

It is clear that c) implies a). Let us prove that a) entails b): since `S_α` is quasi-compact, so is `S` `(8.2.2)`;
`E_λ` being pro-constructible, so is `u_λ⁻¹(E_λ)` `(1.9.5, (vi))`; the filtered decreasing family of pro-constructible
sets `u_λ⁻¹(E_λ)` then has empty intersection, hence `(1.9.9)` one of them is empty.

Finally, let us show that b) entails c). Since `S_α` is quasi-compact and `L` filtered, one can replace `S_α` by an
affine open set, so one can suppose `(8.2.2)` that `S` and the `S_λ` for `λ ≥ α` are affine; one has then `(1.9.2.1)`,
for `μ ≥ λ`,

```text
  u_λ⁻¹(E_λ) = ⋂_{μ ≥ λ} (E_λ ∩ u_{μλ}(S_μ)),
```

whence `E_λ ∩ u_λ(S) = ⋂_{μ ≥ λ} (E_λ ∩ u_{μλ}(S_μ))`.

Now, since `u_λ` and the `u_{μλ}` are quasi-compact, `u_λ(S)` and `u_{μλ}(S_μ)` are pro-constructible in `S_λ`
`(1.9.5, (vii))`, so the sets `E_λ ∩ u_{μλ}(S_μ)` for `μ ≥ λ` form a filtered decreasing family of pro-constructible
parts of `S_λ`. Since `S_λ` is quasi-compact, hypothesis b) entails that the intersection of this family is empty, hence
`(1.9.9)` one of the sets `E_λ ∩ u_{μλ}(S_μ)` is empty, hence `E_μ ⊂ u_{μλ}⁻¹(E_λ)` is empty. Q.E.D.

**Corollary (8.3.4).**

<!-- label: IV.8.3.4 -->

*For every `λ`, let `F_λ` be an ind-constructible part of `S_λ` such that for `λ ≤ μ` one has `u_{μλ}⁻¹(F_λ) ⊂ F_μ`.
Suppose there exists `α ∈ L` such that `S_α` is quasi-compact. Then the following conditions are equivalent:*

*a) The set `F = ⋃_λ u_λ⁻¹(F_λ)` is equal to `S`.*

*b) There exists `λ` such that `u_λ⁻¹(F_λ) = S` (and then `u_μ⁻¹(F_μ) = S` for `μ ≥ λ`).*

<!-- original page 13 -->

*c) There exists `λ` such that `F_λ = S_λ` (and then `F_μ = S_μ` for `μ ≥ λ`).*

This follows at once from `(8.3.3)` by passage to complements.

**Corollary (8.3.5).**

<!-- label: IV.8.3.5 -->

*For every `λ`, let `E_λ`, `F_λ` be two constructible parts of `S_λ` such that, for `λ ≤ μ`, one has
`E_μ ⊂ u_{μλ}⁻¹(E_λ)` and `F_μ ⊃ u_{μλ}⁻¹(F_λ)`. Suppose there exists an index `α` such that `S_α` is quasi-compact.
Then, in order that `E ⊂ F` (resp. `E = F`), it is necessary and sufficient that there exist `λ` such that `E_λ ⊂ F_λ`
(resp. `E_λ = F_λ`), in which case one also has `E_μ ⊂ F_μ` (resp. `E_μ = F_μ`) for `μ ≥ λ`.*

This is a particular case of `(8.3.2)`.

In particular:

**Corollary (8.3.6).**

<!-- label: IV.8.3.6 -->

*Suppose there exists an `α` such that `S_α` is quasi-compact. In order that `S = ∅`, it is necessary and sufficient
that there exist `λ` such that `S_λ = ∅`.*

**Corollary (8.3.7).**

<!-- label: IV.8.3.7 -->

*One has, for every `λ`,*

```text
  (8.3.7.1)    u_λ(S) = ⋂_{μ ≥ λ} u_{μλ}(S_μ).
```

It is clear that the first member of `(8.3.7.1)` is contained in the second. Let `s` be a point of `S_λ` and set
`X_λ = Spec(k(s))`; consider the projective system `(X_μ, z_{νμ})` where `X_μ = X_λ ×_{S_λ} S_μ` and
`z_{νμ} = 1 × u_{νμ}` for `λ ≤ μ ≤ ν`; its projective limit is `X = X_λ ×_{S_λ} S` and `p_λ = 1 × u_λ` is the canonical
map `X → X_λ` `(8.2.5)`. If `s ∈ ⋂_{μ ≥ λ} u_{μλ}(S_μ)`, this entails that `X_μ ≠ ∅` for every `μ ≥ λ` `(I, 3.4.8)`; it
follows then from `(8.3.6)` that `X ≠ ∅`, hence `s ∈ u_λ(S)` by `(I, 3.4.8)`.

**Proposition (8.3.8).**

<!-- label: IV.8.3.8 -->

*(i) In order that the morphism `u_λ : S → S_λ` be dominant (resp. surjective), it is necessary and sufficient that for
`μ ≥ λ` the morphism `u_{μλ} : S_μ → S_λ` be dominant (resp. surjective).*

*(ii) If, for some index `λ`, the morphisms `u_{μλ} : S_μ → S_λ` are flat (resp. faithfully flat) for all `μ ≥ λ`, then
the morphism `u_λ : S → S_λ` is flat (resp. faithfully flat).*

*(iii) Suppose that the morphisms `u_{μλ} : S_μ → S_λ` are surjective for `μ ≥ λ`. In order that `u_λ` be an open
morphism (resp. universally open), it is necessary and sufficient that, for every `μ ≥ λ`, `u_{μλ}` be an open morphism
(resp. universally open).*

(i) Since `u_λ(S) ⊂ u_{μλ}(S_μ)` for `μ ≥ λ`, the necessity of the conditions is trivial, and it follows at once from
`(8.3.7.1)` that if the `u_{μλ}` are surjective, so is `u_λ`. Suppose now the `u_{μλ}` dominant for `μ ≥ λ`, and
consider in `S_λ` a non-empty quasi-compact open set `U_λ`; then the `U_μ = u_{μλ}⁻¹(U_λ)` for `μ ≥ λ` form a projective
system whose projective limit is `U = u_λ⁻¹(U_λ)` `(8.2.5)`. By hypothesis the `U_μ` are all non-empty, so the same is
true of `U` by `(8.3.6)`, which proves that `u_λ` is dominant.

(ii) By virtue of (i), it suffices to consider the case where the `u_{μλ}` are flat; one can then restrict to the case
where `S_λ` is affine, so also the `S_μ` for `μ ≥ λ` and `S`, and the assertion follows then from `(2.1.2)` and
`(0_I, 6.2.3)`.

(iii) By virtue of `(8.2.5)` and `(I, 3.5.2)`, it suffices to treat the case of open morphisms. Since
`u_λ = u_{μλ} ∘ u_μ` and `u_μ` is surjective, one knows that if `u_λ` is open so is `u_{μλ}` for `μ ≥ λ`
`(Bourbaki, Top. gén., chap. I, 3rd ed., §5, n° 1, prop. 1)`.

<!-- original page 14 -->

Conversely, to show that `u_λ` is open when all the `u_{μλ}` are open for `μ ≥ λ`, it suffices to see that for every
quasi-compact open set `V` of `S`, `u_λ(V)` is open in `S_λ`; but there exists then `μ ≥ λ` such that `V = u_μ⁻¹(V_μ)`,
where `V_μ` is open in `S_μ` `(8.2.11)`; since `u_μ` is surjective, one has `V_μ = u_μ(V)` and `u_λ(V) = u_{μλ}(u_μ(V))`
is therefore open by hypothesis.

One will note that it may happen that all the `u_{μλ}` are open without `u_λ` being so when the `u_{μλ}` are not
surjective. One has an example by considering an integral ring `A` which is not a field, and its field of fractions `K`,
which is the inductive limit of the `A_f`, where `f` runs through `A − {0}`; if one sets `S_1 = Spec(A)`,
`S_f = Spec(A_f)`, one has `S = lim S_f = Spec(K)`, and the morphism `S → S_1` is not open, although the morphisms
`S_f → S_1` are.

**(8.3.9)** For every prescheme `X`, we shall denote as usual by `𝔓(X)` the set of parts of the underlying set of `X`,
by `𝔈(X)` (resp. `𝔒𝔠(X)`, `𝔉𝔠(X)`, `𝔏𝔉𝔠(X)`) the set of constructible (resp. constructible and open, resp. constructible
and closed, resp. constructible and locally closed) parts of `X`. It is clear that `(𝔓(S_λ), u_{μλ}⁻¹)` is an inductive
system of sets and that the maps `u_λ⁻¹ : 𝔓(S_λ) → 𝔓(S)` form an inductive system of maps, whence, by passage to the
inductive limit, a canonical map

```text
  (8.3.9.1)    lim 𝔓(S_λ) → 𝔓(S).
```

Moreover, it follows from `(1.8.2)` that `u_{μλ}⁻¹` carries `𝔈(S_λ)` (resp. `𝔒𝔠(S_λ)`, `𝔉𝔠(S_λ)`, `𝔏𝔉𝔠(S_λ)`) into
`𝔈(S_μ)` (resp. `𝔒𝔠(S_μ)`, `𝔉𝔠(S_μ)`, `𝔏𝔉𝔠(S_μ)`) and that `u_λ⁻¹` carries `𝔈(S_λ)` (resp. `𝔒𝔠(S_λ)`, `𝔉𝔠(S_λ)`,
`𝔏𝔉𝔠(S_λ)`) into `𝔈(S)` (resp. `𝔒𝔠(S)`, `𝔉𝔠(S)`, `𝔏𝔉𝔠(S)`). One therefore has by restriction of `(8.3.9.1)` canonical
maps

```text
  (8.3.9.2)    lim 𝔈(S_λ) → 𝔈(S)
  (8.3.9.3)    lim 𝔒𝔠(S_λ) → 𝔒𝔠(S)
  (8.3.9.4)    lim 𝔉𝔠(S_λ) → 𝔉𝔠(S)
  (8.3.9.5)    lim 𝔏𝔉𝔠(S_λ) → 𝔏𝔉𝔠(S).
```

**(8.3.10)** Let `g_α : X_α → S_α` be a morphism; with the notations of `(8.2.5)` one has as above a canonical map
`v_α⁻¹ : lim 𝔓(X_λ) → 𝔓(X)`; on the other hand, one has projection morphisms `g_λ : X_λ → S_λ` for every `λ ≥ α` and a
projection morphism `g : X → S`. It is clear that the `g_λ⁻¹ : 𝔓(S_λ) → 𝔓(X_λ)` form an inductive system of maps, and
that the diagrams

```text
  𝔓(S_λ)  ──g_λ⁻¹──→  𝔓(X_λ)
    │                    │
    u_{μλ}⁻¹            v_{μλ}⁻¹
    ↓                    ↓
  𝔓(S_μ)  ──g_μ⁻¹──→  𝔓(X_μ)
```

are commutative; one therefore deduces by passage to the inductive limit a commutative diagram

```text
  (8.3.10.1)    lim 𝔓(S_λ)  ───→  lim 𝔓(X_λ)
                    │                  │
                    ↓                  ↓
                  𝔓(S)    ──g⁻¹──→  𝔓(X)
```

<!-- original page 15 -->

and it follows from `(1.8.2)` that one has analogous diagrams on replacing `𝔓` by `𝔈`, `𝔒𝔠`, `𝔉𝔠` or `𝔏𝔉𝔠`.

It results from `(8.3.5)` that under the hypothesis that for some `α ∈ L`, `S_α` is quasi-compact, the canonical map
`(8.3.9.2)` is injective. Moreover:

**Theorem (8.3.11).**

<!-- label: IV.8.3.11 -->

*Suppose there exists `α ∈ L` such that `S_α` is quasi-compact and quasi-separated. Then the canonical maps `(8.3.9.2)`,
`(8.3.9.3)`, `(8.3.9.4)` and `(8.3.9.5)` are bijective.*

By virtue of the preceding remark, it remains to prove that these maps are surjective; since every constructible part of
`S` is a finite union of sets of the form `U ∩ ∁V`, where `U` and `V` are open and constructible, it will suffice to
prove that `(8.3.9.3)` is surjective for the same to hold of `(8.3.9.2)` (and also of `(8.3.9.4)`, by passage to
complements). Now, since the morphisms `S_λ → S_α` and `S → S_α` are affine, hence separated, the `S_λ` for `λ ≥ α` and
`S` are quasi-compact and quasi-separated `(1.2.2)`, and one knows that the constructible open parts in such a prescheme
are none other than the quasi-compact open parts `(1.8.1)`. The conclusion therefore follows from `(8.2.11)` except for
the map `(8.3.9.5)`. To prove that this last map is surjective, consider a part `Z` locally closed and constructible in
`S`; `Z` is therefore quasi-compact `(0_III, 9.1.4)`. Since every point `x ∈ Z` admits by hypothesis a quasi-compact
open neighbourhood `V_x` in `S` such that `Z ∩ V_x` is closed in `V_x`, one can cover `Z` by a finite number of the
`V_x`; in other words, there is a quasi-compact open set `U` containing `Z` and such that `Z` is closed in `U`; since
`Z` is constructible in `S`, it is so also in `U` `(0_III, 9.1.8)`. One knows `(8.2.11)` that there is an index `λ` and
a quasi-compact open set `U_λ` in `S_λ` such that `U = u_λ⁻¹(U_λ)`. Applying to `U` (which is the projective limit of
the `U_μ = u_{μλ}⁻¹(U_λ)` for `μ ≥ λ`) the fact that the map `(8.3.9.4)` is surjective, one sees that there exists
`μ ≥ λ` and a constructible closed set `Z_μ` in `U_μ` such that `Z = u_μ⁻¹(Z_μ)`. But since the canonical immersion
`U_μ → S_μ` is quasi-compact by hypothesis `(1.2.7)`, it is of finite presentation `(1.6.2, (i))`, and `Z_μ` is also a
constructible part of `S_μ` by virtue of `(1.8.4)` and `(1.8.1)`; since `Z_μ` is evidently locally closed in `S_μ`, this
completes the proof.

**Corollary (8.3.12).**

<!-- label: IV.8.3.12 -->

*Suppose there exists `α` such that `S_α` is quasi-compact, and let, for every `λ`, `Z_λ` be a constructible part of
`S_λ` such that `Z_μ = u_{μλ}⁻¹(Z_λ)` for `μ ≥ λ`. If `Z = u_λ⁻¹(Z_λ)`,*

<!-- original page 16 -->

*then, in order that `Z` be open (resp. closed, resp. locally closed) in `S`, it is necessary and sufficient that there
exist `λ ≥ α` such that `Z_λ` be so in `S_λ`.*

Cover `S_α` by a finite number of affine open sets `U_α^{(i)}`; then the `U^{(i)} = u_α⁻¹(U_α^{(i)})` form an open
affine cover of `S`, and for `Z` to be open (resp. closed, resp. locally closed) in `S`, it is necessary and sufficient
that each of the `Z ∩ U^{(i)}` be so in `U^{(i)}`. Since `L` is filtered and each of the `Z ∩ U^{(i)}` is constructible
in `U^{(i)}` `(0_III, 9.1.8)`, one can restrict to proving the corollary when `S_α` is affine, hence quasi-compact and
quasi-separated; but in that case it follows from `(8.3.11)`.

**Proposition (8.3.13).**

<!-- label: IV.8.3.13 -->

*Suppose that the morphisms `u_{μλ} : S_μ → S_λ` are flat for `λ ≤ μ`, and that there exists `α` such that `S_α` is
quasi-compact. For every `λ`, let `Z_λ`, `Z'_λ` be two pro-constructible parts of `S_λ`, such that `Z_μ = u_{μλ}⁻¹(Z_λ)`
and `Z'_μ = u_{μλ}⁻¹(Z'_λ)` for `μ ≥ λ`; suppose moreover that `Z_α` is constructible in `S_α`. Let `Z' = u_λ⁻¹(Z_λ)`,
`Z'' = u_λ⁻¹(Z'_λ)`; in order that `‾Z'' ⊂ ‾Z'`, it is necessary and sufficient that there exist `λ ≥ α` such that
`‾Z'_λ ⊂ ‾Z_λ`.*

Indeed, one knows that `u_λ : S → S_λ` is also a flat morphism for every `λ` `(8.3.8)`; since `Z_λ` is
pro-constructible, the closure of `Z_μ` for `μ ≥ λ` (resp. of `Z'`) in `S_μ` (resp. `S`) is equal to `u_{μλ}⁻¹(‾Z_λ)`
(resp. `u_λ⁻¹(‾Z_λ)`) `(2.3.10)`. Since the `u_{μλ}⁻¹(‾Z_λ)` and `u_λ⁻¹(‾Z_λ)` are constructible `(1.8.2)`, the
conclusion follows from `(8.3.2)`.

### 8.4. Irreducibility and connectedness criteria for projective limits of preschemes

**Proposition (8.4.1).**

<!-- label: IV.8.4.1 -->

*Suppose there exists an index `α` such that `S_α` is quasi-compact.*

*(i) If `S` is not irreducible and if in addition the space underlying `S` is Noetherian and `S_α` quasi-separated,
there exists `λ ≥ α` such that, for `μ ≥ λ`, `S_μ` is not irreducible.*

*(ii) If `S` is not connected, there exists `λ ≥ α` such that, for `μ ≥ λ`, `S_μ` is not connected.*

Suppose that `S` is the union of two closed sets `S'`, `S''` distinct from `S` (resp. disjoint non-empty closed sets).
In case (i), `S'` and `S''` are constructible since the space `S` is Noetherian. By virtue of `(8.3.11)`, there exist
therefore `λ ≥ α` and two constructible closed sets `S'_λ`, `S''_λ` of `S_λ` such that `S' = u_λ⁻¹(S'_λ)`,
`S'' = u_λ⁻¹(S''_λ)`; since `S = S' ∪ S''`, it follows also from `(8.3.11)` that one can suppose that
`S_λ = S'_λ ∪ S''_λ`; since `S'_λ` and `S''_λ` are distinct from `S_λ`, this proves that `S_λ` is not irreducible.

In case (ii), `S'` and `S''` are quasi-compact open sets, hence, by virtue of `(8.2.11)`, there exist `λ ≥ α` and two
quasi-compact open sets `S'_λ`, `S''_λ` of `S_λ` such that `S' = u_λ⁻¹(S'_λ)`, `S'' = u_λ⁻¹(S''_λ)`. Moreover, since
`S'` and `S''` are open and closed in `S`, they are at once pro-constructible and ind-constructible `(1.9.6)`, hence
constructible `(1.9.11)`, and it follows therefore from `(8.3.5)` that one can suppose `λ` taken such that
`S_λ = S'_λ ∪ S''_λ` and `S'_λ ∩ S''_λ = ∅`, which shows that `S_λ` is not connected.

**Proposition (8.4.2).**

<!-- label: IV.8.4.2 -->

*Suppose that the space underlying `S` is Noetherian and that one of the following two conditions is satisfied:*

*a) For `λ ≤ μ`, `u_{μλ} : S_μ → S_λ` is dominant, and there exists `α` such that `S_α` is quasi-compact.*

<!-- original page 18 -->

*b) There exists `α` such that the space underlying `S_α` is Noetherian, and for `μ ≥ λ`, `u_{μλ}` is a homeomorphism of
`S_μ` onto a subspace of `S_λ`.*

*Under these conditions, there exists `λ` such that, for every `μ ≥ λ`:*

*(i) For every irreducible component `Y_i` of `S` (`1 ≤ i ≤ m`), `‾{u_μ(Y_i)}` is an irreducible component of `S_μ`, and
the map `Y_i ↦ ‾{u_μ(Y_i)}` is a bijection of the set of irreducible components of `S` onto the set of irreducible
components of `S_μ`.*

*(ii) For every connected component `C_j` of `S` (`1 ≤ j ≤ n`), `u_μ(C_j)` is a connected component of `S_μ`, and the
map `C_j ↦ u_μ(C_j)` is a bijection of the set of connected components of `S` onto the set of connected components of
`S_μ`.*

We shall first establish the

**Lemma (8.4.2.1).**

<!-- label: IV.8.4.2.1 -->

*Under condition a) or b) of `(8.4.2)`, there exists `λ` such that, for `μ ≥ λ`, `u_μ : S → S_μ` is dominant.*

In case a), this has already been proved without supposing the space `S` Noetherian `(8.3.8, (i))`. In case b), set
`Z_α = ‾{u_α(S)}`; as a closed part of the Noetherian space `S_α`, `Z_α` is constructible, and since `u_α⁻¹(Z_α) = S`,
it follows from `(8.3.5)` that there exists `λ ≥ α` such that, for `μ ≥ λ`, one has `Z_μ = u_{μα}⁻¹(Z_α) = S_μ`. But
since `u_{αμ}` is a homeomorphism of `S_μ` onto a subspace of `S_α`, and since the composite map `S → Z_μ → Z_α` is
dominant, the same is true of `S → Z_μ = S_μ`.

This lemma being proved, one may suppose that for every `λ`, `u_λ` is a dominant morphism.

(i) Each of the `S_λ` is the union of the `u_λ(Y_i)`, which are irreducible. On the other hand, if `U_i` is the open set
of `S` complementary to the union of the `Y_j` of index `j ≠ i` (`1 ≤ i ≤ m`), the `U_i` are pairwise disjoint and
`Y_i = ‾{U_i}` `(0_I, 2.1.6)`. Since the space underlying `S` is Noetherian, the `U_i` are quasi-compact, hence there
exists an index `λ` and open sets `U_{iλ}` of `S_λ` such that `U_i = u_λ⁻¹(U_{iλ})` for `1 ≤ i ≤ m` `(8.2.11)`. One
concludes that if one sets `U_{iμ} = u_{μλ}⁻¹(U_{iλ})` for `λ ≤ μ`, the `U_{iμ}` are pairwise disjoint, for the
`U_i = u_μ⁻¹(U_{iμ})` are, and `u_μ` is dominant. Consequently, none of the closures `‾{U_{iμ}}` is contained in
another, and `u_μ(Y_i)` is dense in `U_{iμ}` since `u_μ` is dominant; one has therefore `‾{U_{iμ}} = ‾{u_μ(Y_i)}`, which
proves that the `‾{U_{iμ}}` are the irreducible components of `S_μ` `(0_I, 2.1.7)` and completes the proof.

(ii) Since the space `S` is Noetherian, the `C_j` are open and closed in `S` and quasi-compact; the same reasoning as in
(i) therefore shows that there exists `λ` and open sets `V_{jλ}` of `S_λ` such that `C_j = u_λ⁻¹(V_{jλ})` for
`1 ≤ j ≤ n`. One sees also, as in (i), that if one sets `V_{jμ} = u_{μλ}⁻¹(V_{jλ})` for `μ ≥ λ`, the `V_{jμ}` are
pairwise disjoint, and `u_μ(C_j)` is dense in `V_{jμ}`; this entails that `V_{jμ}` is connected. Moreover, it follows
from `(8.3.4)` that for `μ` large enough, the union of the `V_{jμ}` is `S_μ`, since every open set in a prescheme is
ind-constructible `(1.9.6)`. The `V_{jμ}` are therefore the connected components of `S_μ`, which completes the proof.

One will note that if the morphisms `u_{μλ}` are immersions, they will satisfy in particular condition b) of `(8.4.2)`.

<!-- original page 19 -->

**Corollary (8.4.3).**

<!-- label: IV.8.4.3 -->

*Suppose one of the conditions a), b) of `(8.4.2)` is satisfied, the space underlying `S` being Noetherian; then, in
order that `S` be irreducible, it is necessary and sufficient that there exist `λ` such that `S_μ` be so for every
`μ ≥ λ`.*

**Proposition (8.4.4).**

<!-- label: IV.8.4.4 -->

*Suppose there exists `α` such that `S_α` is quasi-compact and that, for `λ ≤ μ`, `u_{μλ} : S_μ → S_λ` is dominant.
Then, in order that `S` be connected, it is necessary and sufficient that there exist `λ` such that `S_μ` be so for
every `μ ≥ λ`.*

The condition is sufficient by virtue of `(8.4.1)`; on the other hand, one has seen `(8.3.8, (i))` that `u_λ : S → S_λ`
is dominant for `λ` large enough, hence, if `S` is connected, so is `S_λ`, since `u_λ(S)` is dense in `S_λ` and
connected.

**Corollary (8.4.5).**

<!-- label: IV.8.4.5 -->

*Let `k` be a field, `X` a quasi-compact `k`-prescheme. In order that `X` be geometrically connected `(4.5.2)`, it is
necessary and sufficient that, for every finite separable extension `K` of `k`, `X ⊗_k K` be connected.*

The condition is trivially necessary. To see that it is sufficient, we must prove that if `Ω` is an algebraic closure of
`k`, `X ⊗_k Ω` is connected `(4.5.1)`. Now, `Ω` is the filtered inductive limit of the finite sub-extensions `k'` of
`k`, and for `k ⊂ k' ⊂ k'' ⊂ Ω`, the morphism `X ⊗_k k'' → X ⊗_k k'` is surjective. One is therefore reduced, by virtue
of `(8.4.4)`, to proving that `X ⊗_k k'` is connected for every finite extension `k'` of `k`. But if `K` is the largest
separable extension contained in `k'`, the morphism `X ⊗_k k' → X ⊗_k K` is finite, surjective and radicial, hence
`(2.4.5)` a homeomorphism, and since `X ⊗_k K` is connected by hypothesis, the same is true of `X ⊗_k k'`.

**Remarks (8.4.6).**

<!-- label: IV.8.4.6 -->

(i) The proof of `(8.4.2)` shows that the conclusion of this proposition is valid if one supposes that the space
underlying `S` is Noetherian, that there exists `α` such that `S_α` is quasi-compact, and finally that the
`u_λ : S → S_λ` are dominant.

(ii) By contrast, the conclusion of `(8.4.2)` can fail when the `u_λ` are not dominant for `λ` large enough, even when
the `S_λ` and `S` are Noetherian, as the following example shows. Take for index set `ℕ`, all the `S_n` equal to
`Spec(A × K) = Spec(A) ⨿ Spec(K)`, where `K` is a field, `A` an arbitrary `K`-algebra, and all the morphisms
`u_{n, n+1}` equal to the same morphism corresponding to the homomorphism `(x, y) ↦ (j(y), y)` of `A × K` into itself,
where `j : K → A` is the canonical homomorphism. One verifies easily that the inductive limit of this system of rings is
`K`, the canonical homomorphism `u_n` corresponding to the second projection `A × K → K`. One sees therefore that
`S = Spec(K)` is irreducible although none of the `S_n` is connected.

### 8.5. Modules of finite presentation over a projective limit of preschemes

**(8.5.1)** We continue to use the notations of `(8.2.2)`; we shall in addition restrict to the case where `S_0` is one
of the `S_λ`, to which one may always reduce.

When, in this section, we consider a family `(ℱ_λ)`, where, for every `λ ∈ L`, `ℱ_λ` is an `𝒪_{S_λ}`-Module, it shall be
understood that this family satisfies the condition

```text
  (8.5.1.1)    ℱ_μ = u_{μλ}^*(ℱ_λ)    for λ ≤ μ.
```

We shall then set

```text
  (8.5.1.2)    ℱ = u_λ^*(ℱ_λ),
```

which is an `𝒪_S`-Module not depending on the index `λ ∈ L`, by virtue of hypothesis `(8.5.1.1)`.

Let now `(ℱ_λ)`, `(𝒢_λ)` be two such families of `𝒪_{S_λ}`-Modules. It is clear that the maps `f_λ ↦ u_{μλ}^*(f_λ)` from
`Hom_{S_λ}(ℱ_λ, 𝒢_λ)` to `Hom_{S_μ}(ℱ_μ, 𝒢_μ)` define an inductive system of abelian groups
`(Hom_{S_λ}(ℱ_λ, 𝒢_λ), u_{μλ}^*)`, and that the maps `f_λ ↦ u_λ^*(f_λ)` form an inductive system of homomorphisms of
abelian groups, whence, by passing to the inductive limit, a canonical homomorphism of abelian groups

```text
  (8.5.1.3)    u_λ^* : lim Hom_{S_λ}(ℱ_λ, 𝒢_λ) → Hom_S(ℱ, 𝒢).
```

Let us note that when `ℱ_λ = 𝒪_{S_λ}` condition `(8.5.1.1)` is satisfied, and one has `ℱ = 𝒪_S`; homomorphism
`(8.5.1.3)` thus gives `(0_I, 5.1.1)` a canonical homomorphism of abelian groups

```text
  (8.5.1.4)    lim Γ(S_λ, 𝒢_λ) → Γ(S, 𝒢).
```

**Theorem (8.5.2).**

<!-- label: IV.8.5.2 -->

*(i) Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated) and that, for some `λ ∈ L`, `ℱ_λ` is
quasi-coherent and of finite type (resp. of finite presentation) and `𝒢_λ` quasi-coherent. Then the homomorphism `u_λ^*`
is injective (resp. bijective).*

*(ii) Suppose `S_0` quasi-compact and quasi-separated. For every quasi-coherent `𝒪_S`-Module `ℱ` of finite presentation,
there exist `λ ∈ L` and a quasi-coherent `𝒪_{S_λ}`-Module `ℱ_λ` of finite presentation such that `ℱ` is isomorphic to
`u_λ^*(ℱ_λ)`.*

(i) One can evidently restrict to the case where `S_0 = S_λ` since the morphisms `u_{0λ} : S_λ → S_0` are affine, hence
quasi-compact and separated. Consider first the case where `S_0 = Spec(A_0)` is affine. Then assertion (i) is equivalent
to the

**Lemma (8.5.2.1).**

<!-- label: IV.8.5.2.1 -->

*Let `A_0` be a ring, `(A_λ)_{λ ∈ L}` an inductive system of `A_0`-algebras, `A = lim A_λ`; let `M_0`, `N_0` be two
`A_0`-modules, and set `M_λ = M_0 ⊗_{A_0} A_λ`, `N_λ = N_0 ⊗_{A_0} A_λ`, `M = M_0 ⊗_{A_0} A = lim M_λ`,
`N = N_0 ⊗_{A_0} A = lim N_λ`. If `M_0` is of finite type (resp. of finite presentation), the canonical homomorphism*

<!-- original page 20 -->

```text
  (8.5.2.2)    lim Hom_{A_λ}(M_λ, N_λ) → Hom_A(M, N)
```

*is injective (resp. bijective).*

One knows indeed `(Bourbaki, Alg., chap. II, 3rd ed., §5, n° 1)` that one has canonical functorial isomorphisms

```text
  Hom_{A_λ}(M_λ, N_λ) ⥲ Hom_{A_0}(M_0, N_λ),    Hom_A(M, N) ⥲ Hom_{A_0}(M_0, N)
```

<!-- original page 21 -->

so that the homomorphism `(8.5.2.2)` is none other, up to canonical isomorphisms, than the canonical homomorphism

```text
  (8.5.2.3)    lim Hom_{A_0}(M_0, N_λ) → Hom_{A_0}(M_0, lim N_λ),
```

which, to every inductive system of homomorphisms of `A_0`-modules `θ_λ : M_0 → N_λ`, associates its inductive limit.

Now, if `M_0` is of finite type (resp. of finite presentation), one has an exact sequence `A_0^m → M_0 → 0` (resp.
`A_0^n → A_0^m → M_0 → 0`); since it is clear that `(8.5.2.3)` is bijective when `M_0` is of the form `A_0^m`, it
suffices to use the left-exactness of the functor `M_0 ↦ Hom_{A_0}(M_0, P)` and the exactness of the functor `lim` (in
the category of abelian groups) to conclude.

Let us pass to the case where `S_0` is quasi-compact, and let `(U_i)` be a finite cover of `S_0` by affine open sets;
for every `λ`, the `U_{iλ} = u_{0λ}⁻¹(U_i)` form an affine open cover of `S_λ`, and the `V_i = u_0⁻¹(U_i)` an affine
open cover of `S`. To see that `u_λ^*` is injective, one must prove that if `f_λ : ℱ_λ → 𝒢_λ` is such that
`f = u_λ^*(f_λ) = 0`, then there exists `μ ≥ λ` such that `f_μ = u_{μλ}^*(f_λ) = 0`. By virtue of Lemma `(8.5.2.1)`, for
each `i` there exists `μ_i` such that `f_{μ_i} | U_{iμ_i} = 0` for `μ ≥ μ_i`. It therefore suffices to take `μ` greater
than all the `μ_i`.

Suppose in addition `S_0` quasi-separated and `ℱ_λ` of finite presentation, and let `f : ℱ → 𝒢` be a homomorphism of
`𝒪_S`-Modules. By virtue of Lemma `(8.5.2.1)`, for every `i`, there exists an index `μ_i` and a homomorphism
`f^{(i)}_{μ_i} : ℱ_{μ_i} | U_{iμ_i} → 𝒢_{μ_i} | U_{iμ_i}` such that `u_{μ_i}^*(f^{(i)}_{μ_i}) = f | V_i`. Since `L` is
filtered, one can in addition suppose all the `μ_i` equal to a single `λ`. Note now that `S_λ` is quasi-separated
`(1.2.3)` and `ℱ_λ` is a quasi-coherent `𝒪_{S_λ}`-Module of finite presentation `(0_I, 5.2.5)`; since, for every pair of
indices `i`, `j`, `U_{ijλ} = U_{iλ} ∩ U_{jλ}` is quasi-compact and one has
`u_λ^*(f^{(i)}_λ | U_{ijλ}) = u_λ^*(f^{(j)}_λ | U_{ijλ}) = f | (V_i ∩ V_j)` by definition, it results from what was seen
above that there exists an index `λ_{ij}` such that
`u_{λ_{ij}λ}^*(f^{(i)}_λ) | U_{ijλ_{ij}} = u_{λ_{ij}λ}^*(f^{(j)}_λ) | U_{ijλ_{ij}}` for `μ ≥ λ_{ij}`; taking `μ` greater
than all the `λ_{ij}`, one sees therefore that `u_{μλ}^*(f^{(i)}_λ)` and `u_{μλ}^*(f^{(j)}_λ)` coincide in
`U_{iμ} ∩ U_{jμ}` for every pair `(i, j)`, and consequently define a homomorphism `f_μ : ℱ_μ → 𝒢_μ` such that
`f = u_μ^*(f_μ)`.

Before passing to the proof of (ii), let us note the following corollaries of (i):

**Corollary (8.5.2.4).**

<!-- label: IV.8.5.2.4 -->

*Suppose `S_0` quasi-compact, `ℱ_λ` quasi-coherent of finite type, `𝒢_λ` quasi-coherent of finite presentation. Let
`f_λ : ℱ_λ → 𝒢_λ` be a homomorphism. In order that `f = u_λ^*(f_λ) : ℱ → 𝒢` be an isomorphism, it is necessary and
sufficient that there exist `μ ≥ λ` such that `f_μ = u_{μλ}^*(f_λ) : ℱ_μ → 𝒢_μ` be an isomorphism.*

One may always suppose `S_λ = S_0`; the question being local on `S_0`, one can in addition (`S_0` being quasi-compact
and `L` filtered) reduce to the case where `S_0` is affine, hence quasi-separated. The condition being trivially
sufficient, it remains to show it is necessary: now, by hypothesis there is an `𝒪_S`-homomorphism `g : 𝒢 → ℱ` such that
`g ∘ f = 1_ℱ` and `f ∘ g = 1_𝒢`. Since `𝒢` is of finite presentation, there exist `ν ≥ λ` and a homomorphism
`g_ν : 𝒢_ν → ℱ_ν` such that `g = u_ν^*(g_ν)` by virtue of `(8.5.2, (i))`; one has consequently `u_ν^*(g_ν ∘ f_ν) = 1_ℱ`

<!-- original page 22 -->

and `u_ν^*(f_ν ∘ g_ν) = 1_𝒢`; taking into account that `ℱ_ν` and `𝒢_ν` are of finite type, one concludes by
`(8.5.2, (i))` that there exists `μ ≥ ν` such that `g_μ ∘ f_μ = 1_{ℱ_μ}` and `f_μ ∘ g_μ = 1_{𝒢_μ}`, whence the
corollary.

**Corollary (8.5.2.5).**

<!-- label: IV.8.5.2.5 -->

*Suppose `S_0` quasi-compact and quasi-separated. Suppose that `ℱ_λ`, `𝒢_λ` are quasi-coherent `𝒪_{S_λ}`-Modules of
finite presentation. In order that `ℱ` and `𝒢` be isomorphic, it is necessary and sufficient that there exist `μ ≥ λ`
such that `ℱ_μ` and `𝒢_μ` be isomorphic. Moreover, for every isomorphism `f : ℱ ⥲ 𝒢`, there exist `ν ≥ μ` and an
isomorphism `f_ν : ℱ_ν ⥲ 𝒢_ν` such that `f = u_ν^*(f_ν)`.*

This follows from `(8.5.2.4)` and `(8.5.2, (i))` since every homomorphism `f : ℱ → 𝒢` is of the form `u_μ^*(f_μ)` for
some `μ ≥ λ` and a homomorphism `f_μ : ℱ_μ → 𝒢_μ`.

(ii) Consider again first the case where `S_0 = Spec(A_0)` is affine. Then the assertion is equivalent to Lemma
`(5.13.7.1)`.

In the general case, starting from a finite affine open cover `(U_i)` of `S_0`, one deduces from `(5.13.7.1)` that for
every `i`, there exists an index `λ(i)` and a quasi-coherent `𝒪_{U_{iλ(i)}}`-Module of finite presentation `ℱ^{(i)}`
such that `u_{λ(i)}^*(ℱ^{(i)}) = ℱ | V_i` (with the notations of (i)). Moreover, since `L` is filtered, one can suppose
that all the `λ(i)` are equal to a single `λ`. Since `U_{ijλ} = U_{iλ} ∩ U_{jλ}` is quasi-compact and quasi-separated
`(1.2.7)`, it follows from `(8.5.2.5)` that for every pair `(i, j)`, there exists an index `λ_{ij} ≥ λ` and an
isomorphism `θ^{(λ)}_{ij} : u_{λ_{ij}λ}^*(ℱ^{(i)} | U_{ijλ}) ⥲ u_{λ_{ij}λ}^*(ℱ^{(j)} | U_{ijλ})` such that
`u_{λ_{ij}}^*(θ^{(λ)}_{ij})` is the identity automorphism of `ℱ | (V_i ∩ V_j)`; one can again suppose all the `λ_{ij}`
equal to `λ`. Changing notations, one can therefore suppose that there exists for every pair `(i, j)` an isomorphism
`θ_{ij} : ℱ^{(i)} | U_{ijλ} ⥲ ℱ^{(j)} | U_{ijλ}`, such that `u_λ^*(θ_{ij})` is the identity automorphism of
`ℱ | (V_i ∩ V_j)`. Finally, for any three indices `i`, `j`, `k`, if one sets `U_{ijkλ} = U_{iλ} ∩ U_{jλ} ∩ U_{kλ}`,
`U_{ijkλ}` is quasi-compact, and if `θ'_{ij}`, `θ'_{jk}` and `θ'_{ik}` denote the restrictions of `θ_{ij}`, `θ_{jk}` and
`θ_{ik}` to `U_{ijkλ}`, one has `u_λ^*(θ'_{ij} ∘ θ'_{jk}) = u_λ^*(θ'_{ik})`. There exists therefore, by virtue of (i),
an index `μ ≥ λ` such that one has `u_{μλ}^*(θ'_{ik}) = u_{μλ}^*(θ'_{ij} ∘ θ'_{jk})`; thus the isomorphisms
`u_{μλ}^*(θ_{ij}) : u_{μλ}^*(ℱ^{(i)}) | U_{ijμ} ⥲ u_{μλ}^*(ℱ^{(j)}) | U_{ijμ}` verify the gluing condition, and
consequently define on `S_μ` a quasi-coherent `𝒪_{S_μ}`-Module `ℱ_μ` of finite presentation `(0_I, 3.3.1)` such that `ℱ`
is isomorphic to `u_μ^*(ℱ_μ)`.

**Scholium (8.5.3).**

<!-- label: IV.8.5.3 -->

The result of `(8.5.2)` may again be expressed by saying that if `S_0` is quasi-compact and quasi-separated, the
category of quasi-coherent `𝒪_S`-Modules of finite presentation is determined up to equivalence by the data of the
categories of quasi-coherent `𝒪_{S_λ}`-Modules of finite presentation, the functors `u_{μλ}^*` between these categories,
and the transition isomorphisms `u_{νμ}^* ∘ u_{μλ}^* ⥲ u_{νλ}^*`. Pictorially, one can say that giving a quasi-coherent
`𝒪_S`-Module of finite presentation `ℱ` amounts "functorially" to giving an `𝒪_{S_λ}`-Module of finite presentation
`ℱ_λ` for `λ` large; and if a quasi-coherent `𝒪_{S_μ}`-Module of finite presentation `ℱ'_μ` also has `ℱ` as inverse
image, then `ℱ_λ` and `ℱ'_μ` have the same inverse image in a suitable `S_ν` (`ν ≥ λ`, `ν ≥ μ`).

We are going to interpret various notions related to quasi-coherent `𝒪_S`-Modules from this point of view.

<!-- original page 23 -->

**Corollary (8.5.4).**

<!-- label: IV.8.5.4 -->

*Suppose `S_0` quasi-compact and quasi-separated; then, for every quasi-coherent `𝒪_{S_λ}`-Module `𝒢_λ`, the canonical
homomorphism `(8.5.1.4)` is bijective.*

Indeed, it suffices to apply `(8.5.2, (i))` to the case where `ℱ_λ = 𝒪_{S_λ}`, which is of finite presentation.

**Proposition (8.5.5).**

<!-- label: IV.8.5.5 -->

*Suppose `S_0` quasi-compact, and suppose that `ℱ_λ` is a quasi-coherent `𝒪_{S_λ}`-Module of finite presentation. In
order that `ℱ` be locally free (resp. locally free of rank `n`), it is necessary and sufficient that there exist `μ ≥ λ`
such that `ℱ_μ` be so.*

The condition being trivially sufficient, let us prove that it is necessary. If `ℱ` is locally free (resp. locally free
of rank `n`), there exists a finite affine open cover `(V_i)` of `S` such that `ℱ | V_i` is isomorphic to
`𝒪_S^{n_i} | V_i` (resp. `𝒪_S^n | V_i`) for every `i`. By virtue of `(8.2.11)`, there exists `ν ≥ λ` and for each `i` a
quasi-compact open set `U_{iν}` of `S_ν` such that `V_i = u_ν⁻¹(U_{iν})`. Since `S_ν` is quasi-compact, each `U_{iν}` is
a finite union of affine open sets; one is therefore reduced to the case where `S_0` is affine and `ℱ = 𝒪_S^n`; one then
knows that there exists `μ ≥ λ` such that `ℱ_μ` is isomorphic to `𝒪_{S_μ}^n` `(8.5.2.5)`.

**Proposition (8.5.6).**

<!-- label: IV.8.5.6 -->

*Suppose `S_0` quasi-compact, and consider a sequence*

```text
  ℱ_λ → 𝒢_λ → ℋ_λ → 0
```

*of homomorphisms of quasi-coherent `𝒪_{S_λ}`-Modules, where `ℱ_λ` and `𝒢_λ` are of finite type and `ℋ_λ` of finite
presentation. In order that the corresponding sequence `ℱ → 𝒢 → ℋ → 0` be exact, it is necessary and sufficient that
there exist `μ ≥ λ` such that the sequence `ℱ_μ → 𝒢_μ → ℋ_μ → 0` be so (in which case the same is true of the sequence
`ℱ_ν → 𝒢_ν → ℋ_ν → 0` for `ν ≥ μ`).*

The fact that the condition is sufficient and the last assertion result from the fact that the functor `u_λ^*` (resp.
`u_{μλ}^*`) is right exact. To prove that the condition is necessary, note that it follows from the hypothesis and from
`(8.5.2, (i))` that there exists `ν ≥ λ` such that the composite `ℱ_ν → 𝒢_ν → ℋ_ν` is zero. If one sets
`ℋ'_ν = Coker(ℱ_ν → 𝒢_ν)`, one has therefore a homomorphism `f_ν : ℋ'_ν → ℋ_ν`; by hypothesis, `u_ν^*(f_ν)` is an
isomorphism, and it follows therefore from `(8.5.2.4)` that there exists `μ ≥ ν` such that `u_{μν}^*(f_ν)` is an
isomorphism, which completes the proof.

**Corollary (8.5.7).**

<!-- label: IV.8.5.7 -->

*Suppose `S_0` quasi-compact, `ℱ_λ` quasi-coherent, `𝒢_λ` quasi-coherent of finite type, and let `f_λ : ℱ_λ → 𝒢_λ` be a
homomorphism. In order that `f = u_λ^*(f_λ) : ℱ → 𝒢` be surjective, it is necessary and sufficient that there exist
`μ ≥ λ` such that `f_μ = u_{μλ}^*(f_λ) : ℱ_μ → 𝒢_μ` be so.*

This is the particular case of `(8.5.6)` applied to the sequence `ℱ_λ → 𝒢_λ → ℋ_λ → 0`, where `ℋ_λ = Coker(f_λ)`, which
is quasi-coherent and of finite type (taking into account that one has `ℋ = Coker(f)` and `ℋ_μ = Coker(f_μ)`, by virtue
of the right exactness of the functors `u_λ^*` and `u_{μλ}^*`).

**Corollary (8.5.8).**

<!-- label: IV.8.5.8 -->

*Suppose `S_0` quasi-compact and the morphisms `u_{μλ} : S_μ → S_λ` flat. Then:*

<!-- original page 24 -->

*(i) Let `ℱ_λ ─f_λ→ 𝒢_λ ─g_λ→ ℋ_λ` be a sequence of homomorphisms of quasi-coherent `𝒪_{S_λ}`-Modules, such that
`Im f_λ` and `Ker g_λ` are of finite type. In order that the corresponding sequence `ℱ → 𝒢 → ℋ` be exact, it is
necessary and sufficient that there exist `μ ≥ λ` such that the sequence `ℱ_μ ─f_μ→ 𝒢_μ ─g_μ→ ℋ_μ` be exact.*

*(ii) Let `f_λ : ℱ_λ → 𝒢_λ` be a homomorphism of quasi-coherent `𝒪_{S_λ}`-Modules such that `Ker f_λ` is of finite type.
In order that `f = u_λ^*(f_λ) : ℱ → 𝒢` be injective, it is necessary and sufficient that there exist `μ ≥ λ` such that
`f_μ = u_{μλ}^*(f_λ) : ℱ_μ → 𝒢_μ` be so.*

(i) Taking into account `(8.3.8, (ii))`, note that, by flatness, `Im f` and `Ker g` (resp. `Im f_μ` and `Ker g_μ` for
`μ ≥ λ`) are the inverse images of `Im f_λ` and `Ker g_λ` `(0_I, 6.7.2)`. Suppose that the sequence `ℱ → 𝒢 → ℋ` is
exact. Since `Im f_λ` is of finite type, there exists `μ ≥ λ` such that the composite `ℱ_μ → 𝒢_μ → ℋ_μ` is zero, by
virtue of `(8.5.2, (i))`. Changing notations, one can therefore already suppose that `g_λ ∘ f_λ = 0`. Then since the
homomorphism `ℱ → Ker g` is surjective and `Ker g_λ` is of finite type, it follows from `(8.5.7)` that there exists
`μ ≥ λ` such that the homomorphism `ℱ_μ → Ker g_μ` is surjective, which completes the proof of (i).

(ii) The assertion is the particular case of (i) applied to the sequence `0 → ℱ_λ → 𝒢_λ`.

**Lemma (8.5.9).**

<!-- label: IV.8.5.9 -->

*Suppose `S_0` quasi-compact, `ℱ_λ` quasi-coherent of finite type; let `𝒢'_λ` and `𝒢''_λ` be two quasi-coherent
quotients of `ℱ_λ`, `𝒢'_λ` being moreover supposed of finite presentation. In order that `𝒢''` be a quotient of `𝒢'`, it
is necessary and sufficient that there exist `μ ≥ λ` such that `𝒢''_μ` be a quotient of `𝒢'_μ`.*

By hypothesis, there are two surjective homomorphisms `p'_λ : ℱ_λ → 𝒢'_λ`, `p''_λ : ℱ_λ → 𝒢''_λ`; by virtue of the right
exactness of `u_λ^*` and `u_{μλ}^*`, `p' = u_λ^*(p'_λ)`, `p'' = u_λ^*(p''_λ)`, `p'_μ = u_{μλ}^*(p'_λ)`,
`p''_μ = u_{μλ}^*(p''_λ)` are also surjective; moreover, if there exists a homomorphism `f : 𝒢' → 𝒢''` (resp.
`f_μ : 𝒢'_μ → 𝒢''_μ`) such that `p'' = f ∘ p'` (resp. `p''_μ = f_μ ∘ p'_μ`), this homomorphism is necessarily unique,
which shows that the question is local on `S_λ`, and that one can therefore (`S_0` being quasi-compact and `L` filtered)
suppose `S_λ` affine, hence quasi-separated. It is clear that the condition of the statement is sufficient. Conversely,
since `𝒢'_λ` is of finite presentation, `S_λ` quasi-compact and quasi-separated, it follows from `(8.5.2, (i))` that if
there exists a homomorphism `f : 𝒢' → 𝒢''` such that `p'' = f ∘ p'`, there exist `μ ≥ λ` and a homomorphism
`f_μ : 𝒢'_μ → 𝒢''_μ` such that `f = u_μ^*(f_μ)` and `p''_μ = f_μ ∘ p'_μ`, whence the lemma.

**(8.5.10)** In what follows in this number, for every quasi-coherent Module `ℱ` on a prescheme, let us denote by `𝒬(ℱ)`
the set of quotient Modules of `ℱ` that are of finite presentation. If `ℱ_λ` is quasi-coherent and `𝒢_λ ∈ 𝒬(ℱ_λ)`, it
follows from the fact that `u_{μλ}^*` and `u_λ^*` are right exact, that one has `𝒢_μ ∈ 𝒬(ℱ_μ)` for `μ ≥ λ` and
`𝒢 ∈ 𝒬(ℱ)`; it is clear that `(𝒬(ℱ_λ), u_{μλ}^*)` is an inductive system of sets, and that the `u_λ^* : 𝒬(ℱ_λ) → 𝒬(ℱ)`
form an inductive system of maps, whence, by passage to the inductive limit, a canonical map

```text
  (8.5.10.1)    u_𝒬 : lim 𝒬(ℱ_λ) → 𝒬(ℱ).
```

Moreover, if `(ℱ'_λ)` is a second family of quasi-coherent `𝒪_{S_λ}`-Modules and if, for every `λ`, `ℱ'_λ` is a quotient
of `ℱ_λ`, then `ℱ'` is a quotient of `ℱ` and one has a commutative diagram

<!-- original page 25 -->

```text
  (8.5.10.2)    lim 𝒬(ℱ_λ)  ──→  𝒬(ℱ)
                    │              │
                    ↓              ↓
                lim 𝒬(ℱ'_λ)  ──→  𝒬(ℱ').
```

**Proposition (8.5.11).**

<!-- label: IV.8.5.11 -->

*Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated). Suppose `ℱ_λ` quasi-coherent of finite type
(resp. of finite presentation) for every `λ`; then the canonical map `(8.5.10.1)` is injective (resp. bijective).*

The first assertion results from the more precise lemma `(8.5.9)`. To prove the second, consider a quotient `𝒪_S`-Module
`𝒢` of `ℱ` that is of finite presentation. It follows from `(8.5.2, (ii))` that there exist `λ' ∈ L` and a
quasi-coherent `𝒪_{S_{λ'}}`-Module `𝒢_{λ'}` of finite presentation such that `𝒢 = u_{λ'}^*(𝒢_{λ'})`; since `L` is
filtered, one can suppose `λ' = λ` (replacing `λ` and `λ'` by an index majoring them). Consider then the canonical
homomorphism `p : ℱ → 𝒢`; it follows from `(8.5.2, (i))` that there exist `μ ≥ λ` and a homomorphism `p_μ : ℱ_μ → 𝒢_μ`
such that `p = u_μ^*(p_μ)`. Moreover, by virtue of `(8.5.7)`, one can suppose `μ` chosen large enough so that `p_μ` is
surjective, which finishes the proof.

### 8.6. Sub-preschemes of finite presentation of a projective limit of preschemes

**(8.6.1)** Given a prescheme `Y`, let us denote in this number by `𝔖𝔭𝔯(Y)` the ordered set `(I, 4.1.10)` of
sub-preschemes of `Y` that are of finite presentation over `Y` `(1.6.1)`, by `𝔖𝔭𝔯_o(Y)` (resp. `𝔖𝔭𝔯_f(Y)`) the part of
`𝔖𝔭𝔯(Y)` formed of sub-preschemes induced on open sets (resp. closed sub-preschemes) of `Y`, of finite presentation over
`Y`; this amounts to saying that a sub-prescheme `Z` of `Y` belongs to `𝔖𝔭𝔯_o(Y)` (resp. `𝔖𝔭𝔯_f(Y)`) precisely when it
is induced on an open set and the underlying space `Z` is retrocompact in `Y` (resp. when it is closed and the Ideal `𝒥`
of `𝒪_Y` that defines it is of finite type, which also means that `j_*(𝒪_Z) ∈ 𝒬(𝒪_Y)` if `j : Z → Y` is the canonical
injection) `(1.6.1 and 1.4.5)`.

**(8.6.2)** We continue to use the notations of `(8.2.2)` and suppose that `S_0` is one of the `S_λ`. Let `Y_λ` be a
sub-prescheme of `S_λ`; then `Y_μ = u_{μλ}⁻¹(Y_λ)` (resp. `Y = u_λ⁻¹(Y_λ)`) is a sub-prescheme of `S_μ` for `μ ≥ λ`
(resp. of `S`); it is induced on an open set (resp. it is closed) if `Y_λ` is `(I, 4.3.2)` and of finite presentation
over `S_μ` (resp. `S`) if `Y_λ` is of finite presentation over `S_λ` `(1.6.2, (iii))`. Consequently
`(𝔖𝔭𝔯(S_λ), u_{μλ}⁻¹)` (resp. `(𝔖𝔭𝔯_o(S_λ), u_{μλ}⁻¹)`, `(𝔖𝔭𝔯_f(S_λ), u_{μλ}⁻¹)`) is an inductive system, and the maps
`u_λ⁻¹ : 𝔖𝔭𝔯(S_λ) → 𝔖𝔭𝔯(S)` (resp. `𝔖𝔭𝔯_o(S_λ) → 𝔖𝔭𝔯_o(S)`, `𝔖𝔭𝔯_f(S_λ) → 𝔖𝔭𝔯_f(S)`) form an inductive system of maps;
whence, by passage to the inductive limit, canonical maps

```text
  (8.6.2.1)    lim 𝔖𝔭𝔯(S_λ) → 𝔖𝔭𝔯(S)
  (8.6.2.2)    lim 𝔖𝔭𝔯_o(S_λ) → 𝔖𝔭𝔯_o(S)
  (8.6.2.3)    lim 𝔖𝔭𝔯_f(S_λ) → 𝔖𝔭𝔯_f(S).
```

<!-- original page 26 -->

Let us recall `(I, 4.1.10)` that `𝔖𝔭𝔯(X)`, for every prescheme `X`, is a set ordered by the relation "`Z` is a
sub-prescheme of the sub-prescheme `Y`", which is written `Z ≤ Y`. The maps `u_{μλ}⁻¹` and `u_λ⁻¹` are increasing for
the corresponding order relations in `𝔖𝔭𝔯(S_λ)`, `𝔖𝔭𝔯(S_μ)`, `𝔖𝔭𝔯(S)`. Moreover, one defines an order relation in the
set `lim 𝔖𝔭𝔯(S_λ)` by writing that `η ≤ η'` for two elements of this set when there exist a `λ` and two elements `Y_λ`,
`Y'_λ` of `𝔖𝔭𝔯(S_λ)`, of which `η` and `η'` are the canonical images, and which are such that `Y_λ ≤ Y'_λ`; one verifies
easily that this does not depend on the representatives `Y_λ`, `Y'_λ` considered, and that one thus has indeed an order
relation. That being so, the fact that the `u_{μλ}⁻¹` are increasing entails at once that the canonical map `(8.6.2.1)`
is increasing; the same is evidently true of `(8.6.2.2)` and `(8.6.2.3)`.

**Proposition (8.6.3).**

<!-- label: IV.8.6.3 -->

*Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated). Then the maps `(8.6.2.1)`, `(8.6.2.2)`,
`(8.6.2.3)` are injective (resp. bijective).*

Taking into account the remarks of `(8.6.1)`, the assertions relative to `(8.6.2.3)` follow from `(8.5.11)` applied to
`ℱ_λ = 𝒪_{S_λ}`; similarly, the assertions relative to `(8.6.2.2)` are particular cases of `(8.3.5)` and `(8.3.11)`,
taking into account that the `S_λ` and `S` are quasi-compact. It remains to consider the map `(8.6.2.1)`. Let us first
prove that it is surjective when `S_0` is quasi-compact and quasi-separated. Let `Z` be a sub-prescheme of `S`, of
finite presentation over `S`; since `S` is quasi-compact, so is `Z`, hence there exists a quasi-compact open set `U` of
`S` such that `Z` is a closed sub-prescheme of `U`, of finite presentation over `U`. There exist then an index `λ` and a
quasi-compact open set `U_λ` of `S_λ` such that `U = u_λ⁻¹(U_λ)` `(8.2.11)`; since `S_λ` is quasi-separated, so is `U_λ`
`(1.2.7)`, and consequently one can restrict to the case where `U = S`; but in this case, one is reduced to the fact
that `(8.6.2.3)` is surjective.

Finally, to see that `(8.6.2.1)` is injective when `S_0` is quasi-compact, it will suffice to prove the following more
precise result:

**Corollary (8.6.3.1).**

<!-- label: IV.8.6.3.1 -->

*Suppose `S_0` quasi-compact and let `Z_λ`, `Z'_λ` be two sub-preschemes of `S_λ`, of finite presentation over `S_λ`. In
order that `Z' = u_λ⁻¹(Z_λ)` be majorized by `Z'' = u_λ⁻¹(Z'_λ)` `(I, 4.1.10)`, it is necessary and sufficient that
there exist `μ ≥ λ` such that `Z_μ = u_{μλ}⁻¹(Z_λ)` be majorized by `Z'_μ = u_{μλ}⁻¹(Z'_λ)`.*

It is trivial that the condition is sufficient. To see that it is necessary, note first that the underlying sets `Z_λ`
and `Z'_λ` are locally constructible in `S_λ` by hypothesis `(1.8.4)`, hence the hypothesis entails the existence of
`ν ≥ λ` such that `Z_ν ⊂ Z'_ν` `(8.3.5)`; replacing `λ` by `ν`, one can therefore already suppose that one has
`Z_λ ⊂ Z'_λ`. Moreover, by hypothesis `(1.6.1)`, the subspaces `Z_λ` and `Z'_λ` of `S_λ` are quasi-compact; for every
point `x ∈ Z_λ`, there is a quasi-compact open neighbourhood `V(x)` in `S_λ` such that `V(x) ∩ Z_λ` and `V(x) ∩ Z'_λ`
are closed in `V(x)`. By covering `S_λ` by a finite number of neighbourhoods `V(x_i)` one sees therefore that there is a
quasi-compact open set `U_λ` of `S_λ` containing `Z_λ` and such that `Z_λ` and `Z'_λ ∩ U_λ` are closed in `U_λ`. If one
denotes by `Y_λ` the sub-prescheme induced by `Z'_λ` on `U_λ ∩ Z'_λ`, it is clear that with the usual notations, `Y_μ`
(resp. `Y`) is induced by `Z'_μ` on `U_μ ∩ Z'_μ` for `μ ≥ λ` (resp. by `Z''` on `U ∩ Z''`); moreover `Z'` is majorized
by `Y` `(I, 4.4.1)`, and since it suffices to prove that `Z_μ` is majorized by `Y_μ` for `μ`

<!-- original page 27 -->

large enough, one sees finally that one is reduced (replacing `S_λ` by `U_λ`) to the case where `Z_λ` and `Z'_λ` are
closed sub-preschemes of `S_λ`. But then this has already been proved since `(8.6.2.3)` is increasing and injective.

**Corollary (8.6.4).**

<!-- label: IV.8.6.4 -->

*Suppose `S_0` quasi-compact, and let `Z_λ` be a sub-prescheme of `S_λ`, of finite presentation over `S_λ`. In order
that `Z = u_λ⁻¹(Z_λ)` be a sub-prescheme induced on an open set (resp. a closed sub-prescheme) of `S`, it is necessary
and sufficient that there exist `μ ≥ λ` such that `Z_μ = u_{μλ}⁻¹(Z_λ)` be induced on an open set (resp. a closed
sub-prescheme) of `S_μ`.*

Let `(U^{(i)}_λ)` be a finite affine open cover of `S_λ`, and set `U^{(i)}_μ = u_{μλ}⁻¹(U^{(i)}_λ)` for `μ ≥ λ` and
`U^{(i)} = u_λ⁻¹(U^{(i)}_λ)`. If `Z` is open (resp. closed) in `S`, `Z ∩ U^{(i)}` is so in `U^{(i)}`, and conversely if
each of the `Z_μ ∩ U^{(i)}_μ` is open (resp. closed) in `U^{(i)}_μ`, `Z_μ` is so in `S_μ`. Since `L` is filtered, it
suffices to prove the corollary when `S_λ` is affine, hence quasi-separated. But then the result follows from the fact
that the maps `(8.6.2.1)`, `(8.6.2.2)` and `(8.6.2.3)` are bijective.

### 8.7. Criteria for a projective limit of preschemes to be a reduced (resp. integral) prescheme

We continue to use the hypotheses and notations of `(8.2.2)` and suppose always that `S_0` is one of the `S_λ`.

**Proposition (8.7.1).**

<!-- label: IV.8.7.1 -->

*Suppose that `S` is non-reduced. Then there exists `λ_0` such that for `λ ≥ λ_0`, `S_λ` is non-reduced.*

The question being local on `S_0`, one can suppose `S_0 = Spec(A_0)` affine, whence `S = Spec(A)`, where `A = lim A_λ`
is the inductive limit of an inductive system of `A_0`-algebras `(A_λ)`. One knows then `(5.13.2)` that the nilradical
of `A` is the inductive limit of those of the `A_λ`; if it is not zero, one of the `A_λ` thus contains a nilpotent
element `a_λ ≠ 0` whose image in `A` is a nilpotent and non-zero element, and the image of `a_λ` in the `A_μ` for
`μ ≥ λ` is consequently a nilpotent and non-zero element.

**Proposition (8.7.2).**

<!-- label: IV.8.7.2 -->

*Suppose one of the following hypotheses is satisfied:*

*a) `S_0` is quasi-compact, the nilradical `𝒩_0` of `𝒪_{S_0}` is an Ideal of finite type (which will be the case for
example when `S_0` is Noetherian), and the morphisms `u_{μλ} : S_μ → S_λ` are open immersions.*

*b) The morphisms `u_{μλ} : S_μ → S_λ` are faithfully flat.*

*Under these conditions, in order that `S` be reduced, it is necessary and sufficient that there exist `λ_0` such that
`S_λ` be reduced for `λ ≥ λ_0`.*

*Moreover, in case b), if `S` is reduced, all the `S_λ` are.*

The last assertion follows from the fact that the morphism `S → S_λ` is then faithfully flat for every `λ` `(8.3.8)` and
from `(2.1.13)`. On the other hand, `(8.7.1)` proves that the condition of the statement is sufficient (without
hypothesis on `S_0` nor on the `u_{μλ}`). It remains therefore to see that the condition is necessary in hypothesis a);
then `(8.2.13)`, the space underlying `S` is identified with the intersection of the spaces underlying the `S_λ` (the
`S_λ` being identified with sub-preschemes induced on open sets of `S_0`), and the structure sheaf `𝒪_S` is identified
with the

<!-- original page 28 -->

sheaf induced on `S` by all the `𝒪_{S_λ}`; in particular for every `s ∈ S`, the local ring `𝒪_s` is the same for `S` and
for all the `S_λ`. If `𝒩_λ` is the Nilradical of `𝒪_{S_λ}`, the Nilradical `𝒩` of `𝒪_S` has therefore at each point of
`S` the same fibre `𝒩_s` (nilradical of `𝒪_s`) as `u_λ^*(𝒩_λ)` (induced on `S` by `𝒩_λ`). The hypothesis that `S` is
reduced thus entails `u_λ^*(𝒩_λ) = 0`; since `𝒩_0` is supposed of finite type, the same is true of `𝒩_λ`, and the
conclusion therefore follows from `(8.5.7)`.

**Corollary (8.7.3).**

<!-- label: IV.8.7.3 -->

*Suppose one of the following hypotheses is satisfied:*

*a) `S_0` is a Noetherian prescheme and the morphisms `u_{μλ} : S_μ → S_λ` are open immersions.*

*b) The morphisms `u_{μλ} : S_μ → S_λ` are faithfully flat.*

*Then, in order that `S` be integral, it is necessary and sufficient that there exist `λ_0` such that `S_λ` be integral
for `λ ≥ λ_0`.*

To say that a prescheme is integral means that it is at once reduced and irreducible; the corollary therefore follows
from `(8.7.2)` and `(8.4.3)`.

**Remark (8.7.4).**

<!-- label: IV.8.7.4 -->

If one makes no hypothesis on the `u_{μλ}`, it may happen that `S` is integral although all the `S_λ` are non-reduced
and non-connected, as the example `(8.4.6)` shows, where one takes the ring `A` non-reduced.

### 8.8. Preschemes of finite presentation over a projective limit of preschemes

**(8.8.1)** Continuing to use the notations and hypotheses of `(8.2.2)`, we shall assume given in this section two
`S_α`-preschemes `X_α`, `Y_α`, which defines `(8.2.5)` two projective systems of preschemes `(X_λ, v_{μλ})` and
`(Y_λ, w_{μλ})` by setting `X_λ = X_α ×_{S_α} S_λ`, `Y_λ = Y_α ×_{S_α} S_λ`, `v_{μλ} = 1_{X_α} × u_{μλ}`,
`w_{μλ} = 1_{Y_α} × u_{μλ}` (for `α ≤ λ ≤ μ`), whose projective limits are respectively `X = X_α ×_{S_α} S`,
`Y = Y_α ×_{S_α} S`, the canonical morphisms `v_λ : X → X_λ` and `w_λ : Y → Y_λ` being respectively equal to
`1_{X_α} × u_λ` and `1_{Y_α} × u_λ`. For `α ≤ λ ≤ μ`, one has a canonical map
`e_{μλ} : Hom_{S_λ}(X_λ, Y_λ) → Hom_{S_μ}(X_μ, Y_μ)`, which to every `S_λ`-morphism `f_λ : X_λ → Y_λ` associates
`f_μ = f_λ × 1_{S_μ} : X_λ ×_{S_λ} S_μ → Y_λ ×_{S_λ} S_μ`, and it is clear that `(Hom_{S_λ}(X_λ, Y_λ), e_{μλ})` is an
inductive system of sets. Similarly, one has a canonical map `e_λ : Hom_{S_λ}(X_λ, Y_λ) → Hom_S(X, Y)` which to `f_λ`
associates `f = f_λ × 1_S : X_λ ×_{S_λ} S → Y_λ ×_{S_λ} S` and `(e_λ)` is an inductive system of maps; whence, by
passage to the inductive limit, a canonical map, functorial in `S_α`, `X_α` and `Y_α`:

```text
  (8.8.1.1)    e : lim Hom_{S_λ}(X_λ, Y_λ) → Hom_S(X, Y).
```

**Theorem (8.8.2).**

<!-- label: IV.8.8.2 -->

*(i) Suppose `X_α` quasi-compact (resp. quasi-compact and quasi-separated), and `Y_α` locally of finite type (resp.
locally of finite presentation) over `S_α`. Then the map `(8.8.1.1)` is injective (resp. bijective).*

*(ii) Suppose `S_0` quasi-compact and quasi-separated. For every prescheme `X` of finite presentation over `S`, there
exist `λ ∈ L`, a prescheme `X_λ` of finite presentation over `S_λ`, and an `S`-isomorphism `X_λ ×_{S_λ} S ⥲ X`.*

<!-- original page 29 -->

(i) Consider first the case where `S_0 = Spec(A_0)`, `X_α = Spec(B_α)` and `Y_α = Spec(C_α)` are affine; then the
`S_λ = Spec(A_λ)` and `S = Spec(A)` are also affine, with `A = lim A_λ`, and the assertions of (i) are equivalent to the

**Lemma (8.8.2.1).**

<!-- label: IV.8.8.2.1 -->

*Let `A_0` be a ring, `(A_λ)_{λ ∈ L}` an inductive system of `A_0`-algebras, `A = lim A_λ`; let `B_α` be an
`A_α`-algebra, `C_α` an `A_α`-algebra of finite type (resp. of finite presentation). Then the canonical homomorphism*

```text
  (8.8.2.2)    lim Hom_{A_λ-alg.}(C_α ⊗_{A_α} A_λ, B_α ⊗_{A_α} A_λ) → Hom_{A-alg.}(C_α ⊗_{A_α} A, B_α ⊗_{A_α} A)
```

*is injective (resp. bijective).*

One knows that one has canonical functorial isomorphisms

```text
  Hom_{A_λ-alg.}(C_α ⊗_{A_α} A_λ, B_α ⊗_{A_α} A_λ) ⥲ Hom_{A_α-alg.}(C_α, B_α ⊗_{A_α} A_λ)
  Hom_{A-alg.}(C_α ⊗_{A_α} A, B_α ⊗_{A_α} A) ⥲ Hom_{A_α-alg.}(C_α, B_α ⊗_{A_α} A)
```

by virtue of the universal property of the tensor product of two algebras. It therefore suffices to prove the

**Lemma (8.8.2.3).**

<!-- label: IV.8.8.2.3 -->

*Let `E` be a ring, `G` an `E`-algebra of finite type (resp. of finite presentation), `(F_λ)` an inductive system of
`E`-algebras. Then the canonical homomorphism*

```text
  lim Hom_{E-alg.}(G, F_λ) → Hom_{E-alg.}(G, lim F_λ)
```

*which, to every inductive system of homomorphisms `θ_λ : G → F_λ` of `E`-algebras, associates its inductive limit, is
injective (resp. bijective).*

Suppose first the `E`-algebra `G` of finite type, and let `(t_i)_{1 ≤ i ≤ n}` be a system of generators of this
`E`-algebra; let us show that if `(θ_λ)`, `(θ'_λ)` are two inductive systems of homomorphisms `G → F_λ` such that
`lim θ_λ = lim θ'_λ`, there exists `μ ≥ λ` such that `θ_μ = θ'_μ`. Indeed, if `φ_{μλ} : F_λ → F_μ` and
`φ_λ : F_λ → F = lim F_λ` are the canonical homomorphisms of the inductive system `(F_λ)`, by hypothesis, for each index
`i`, there exists an index `λ_i` such that `φ_{λ_i}(θ_λ(t_i)) = φ_{λ_i}(θ'_λ(t_i))`, and one can suppose all the `λ_i`
equal to a single `λ`; it follows likewise the existence of `μ ≥ λ` such that `φ_{μλ}(θ_λ(t_i)) = φ_{μλ}(θ'_λ(t_i))` for
`1 ≤ i ≤ n`, that is, `θ_μ(t_i) = θ'_μ(t_i)` for `1 ≤ i ≤ n`, whence `θ_μ = θ'_μ`.

Suppose secondly `G` of finite presentation, so that one has `G = E[T_1, …, T_n]/𝔍`, where `𝔍` is an ideal of finite
type, `t_i` being the class of `T_i` mod. `𝔍`. Let `(P_j)_{1 ≤ j ≤ m}` be a system of generators of `𝔍`. Suppose given a
homomorphism of `E`-algebras `θ : G → F`; set `b_i = θ(t_i)`; by definition, one has therefore
`P_j(b_1, b_2, …, b_n) = θ(P_j(t_1, …, t_n)) = 0` for `1 ≤ j ≤ m`. Now, there exist `λ` and elements `a_1, …, a_n` in
`F_λ` such that `b_i = φ_λ(a_i)` for `1 ≤ i ≤ n`; one has therefore `φ_λ(P_j(a_1, …, a_n)) = P_j(b_1, …, b_n) = 0`, and
consequently there exists `μ ≥ λ` such that `φ_{μλ}(P_j(a_1, …, a_n)) = P_j(φ_{μλ}(a_1), …, φ_{μλ}(a_n)) = 0` for
`1 ≤ j ≤ m`; one concludes that there exists a homomorphism of `E`-algebras `θ_μ : G → F_μ` such that
`θ_μ(t_i) = φ_{μλ}(a_i)`

<!-- original page 30 -->

for `1 ≤ i ≤ n`; one deduces for every `ν ≥ μ` a homomorphism of `E`-algebras `θ_ν = φ_{νμ} ∘ θ_μ` from `G` to `F_ν`,
and it is clear that `θ` is the inductive limit of this inductive system of homomorphisms, which finishes proving the
lemma.

Let us now pass to the case where `X_α` is quasi-compact and `Y_α` locally of finite type over `S_α`. Set
`Z_α = X_α ×_{S_α} Y_α` and introduce the corresponding projective system of `Z_λ = Z_α ×_{S_α} S_λ = X_λ ×_{S_λ} Y_λ`
and its limit `Z = Z_α ×_{S_α} S = X ×_S Y`; the canonical bijections `(I, 3.3.14)` give commutative diagrams

```text
  Hom_{S_λ}(X_λ, Y_λ)  ─────→  Hom_S(X, Y)
        │                          │
        ↓                          ↓
  Hom_{X_λ}(X_λ, Z_λ)  ─────→  Hom_X(X, Z)
```

and consequently one is reduced to proving that `(8.8.1.1)` is injective in the particular case where `S_α = X_α`
(taking into account `(1.3.4)`). Moreover, since `X_α` is quasi-compact, hence a finite union of affine open sets, one
can suppose `X_α` affine (`L` being filtered). Suppose then given two `X_α`-morphisms `f'_α : X_α → Y_α`,
`f''_α : X_α → Y_α` such that `f'` and `f''` are equal `X`-morphisms from `X` to `Y`; one must prove that `f'_μ = f''_μ`
for `μ ≥ α` large enough. Since `X_α` is quasi-compact, so is `f'_α(X_α) ∪ f''_α(X_α)`, and since `Y_α` is locally of
finite type over `X_α`, `f'_α(X_α) ∪ f''_α(X_α)` is contained in a finite union of affine open sets `V_{iα}` of `Y_α`,
of finite type over `X_α`. Set `U'_{iα} = f'_α⁻¹(V_{iα})`, `U''_{iα} = f''_α⁻¹(V_{iα})`, `U_{iα} = U'_{iα} ∩ U''_{iα}`,
`U_α = ⋃ U_{iα}`. The hypothesis `f' = f''` entails `v_α⁻¹(U'_{iα}) = v_α⁻¹(U''_{iα})`, these two sets being
respectively equal to `f'⁻¹(w_α⁻¹(V_{iα}))` and `f''⁻¹(w_α⁻¹(V_{iα}))`. Since the `V_{iα}` cover `Y_α`, one has
`v_α⁻¹(U_α) = f'⁻¹(Y) = X`. Since `X_α` is quasi-compact and every open part of `X_α` is ind-constructible, it follows
from `(8.3.4)` that there is an index `λ ≥ α` such that the `U_{iλ} = v_{λα}⁻¹(U_{iα})` form a cover of `X_λ`. Replacing
`α` by `λ`, one can therefore suppose that the `U_{iα}` cover `X_α`; this entails that for every `x ∈ X_α`, there is an
affine open neighbourhood `W(x)` contained in one of the `U_{iα}`, in other words such that the restrictions of `f'_α`
and `f''_α` to `W(x)` send `W(x)` into a single affine open set `V_{iα}`. Since `X_α` is quasi-compact, it is covered by
a finite number of affine open sets `W(x_k)`; by virtue of Lemma `(8.8.2.1)` and the fact that `L` is filtered, there
exists `λ ≥ α` such that the restrictions of `f'_λ` and `f''_λ` to each of the open sets `v_{λα}⁻¹(W(x_k))` are equal,
whence `f'_λ = f''_λ`.

Suppose now `X_α` quasi-compact and quasi-separated and `Y_α` locally of finite presentation over `S_α`, and let us
prove that `(8.8.1.1)` is surjective. Suppose therefore given an `S`-morphism `f : X → Y`. Since `X` is quasi-compact,
so is `f(X)`, and consequently there is a quasi-compact open set `Y'` in `Y` that contains `f(X)`; there exists
consequently `λ ≥ α` and a quasi-compact open set `Y'_λ` in `Y_λ` such that `Y' = w_λ⁻¹(Y'_λ)` `(8.2.11)`.

<!-- original page 31 -->

Replacing if need be `α` by `λ` and `Y_α` by `Y'_λ`, one can therefore restrict to the case where `Y_α` is
quasi-compact, so also `Y` and the `Y_λ`. Since `Y` is quasi-compact, it is a finite union of affine open sets `V_i`,
and consequently `X` is the union of the open sets `f⁻¹(V_i)`. Since every point of `X` has a quasi-compact open
neighbourhood contained in one of the `f⁻¹(V_i)` and `X` is quasi-compact, one can, taking into account `(8.2.11)` and
replacing if need be `α` by an index `λ ≥ α`, suppose that `Y` is a finite union of open sets `V_i = w_α⁻¹(V_{iα})`,
where the `V_{iα}` are affine open sets of `Y_α`; consequently `X` is the union of the open sets `f⁻¹(V_i)`. Since every
point of `X` has a quasi-compact open neighbourhood contained in one of the `f⁻¹(V_i)` and `X` is quasi-compact, one can
cover `X` by a finite number of such neighbourhoods, and (repeating if need be some of the `V_i`) suppose that one has a
cover `(U_i)` of `X` by quasi-compact open sets having the same index set as `(V_i)` and such that `f(U_i) ⊂ V_i` for
every `i`. Moreover, with the help of `(8.2.11)` (and replacing if need be `α` by an index `λ ≥ α`), one can suppose
that one has `U_i = v_α⁻¹(U_{iα})` where the `U_{iα}` are quasi-compact open sets in `X_α`; furthermore, using `(8.3.4)`
as above, one can suppose that `(U_{iα})` is a cover of `X_α`.

That being so, it will suffice to show that there exist `λ ≥ α` and, for each `i`, a morphism
`f^{(i)}_λ : U_{iλ} → V_{iλ}` (with `U_{iλ} = v_{λα}⁻¹(U_{iα})` and `V_{iλ} = w_{λα}⁻¹(V_{iα})`) such that the
corresponding morphism `f^{(i)} = e_λ(f^{(i)}_λ) : U_i → V_i` is equal to the restriction of `f` to `U_i`. Indeed, if
so, since `X_λ` is quasi-separated `(1.2.3)`, the `U_{iλ} ∩ U_{jλ}` are quasi-compact and the uniqueness result proved
above (which applies since `Y_λ` is locally of finite type over `S_λ`) proves that there exists `μ ≥ λ` such that
`f^{(i)}_μ` and `f^{(j)}_μ` coincide in `U_{iμ} ∩ U_{jμ}` for every pair `(i, j)`, and consequently define an
`S_μ`-morphism `f_μ : X_μ → Y_μ` such that `e_μ(f_μ) = f`.

One is thus reduced to the case where `Y_α` is affine, and since moreover one can suppose that the `V_{iα}` have images
in `S_α` contained in affine open sets, one can also suppose that `S_α` is affine; let then `S_α = Spec(A_α)`,
`Y_α = Spec(C_α)`, `C_α` being an `A_α`-algebra of finite presentation, `S = Spec(A)`, `Y = Spec(C)`, with
`A = lim A_λ`, `C = C_α ⊗_{A_α} A`. One has then

```text
  Hom_S(X, Y) = Hom_{A-alg.}(C, Γ(X, 𝒪_X)) = Hom_{A_α-alg.}(C_α, Γ(X, 𝒪_X))
```

`(I, 2.2.4)` and likewise

```text
  Hom_{S_λ}(X_λ, Y_λ) = Hom_{A_λ-alg.}(C_α ⊗_{A_α} A_λ, Γ(X_λ, 𝒪_{X_λ})) = Hom_{A_α-alg.}(C_α, Γ(X_λ, 𝒪_{X_λ})).
```

But since `X_α` is quasi-compact and quasi-separated, one knows `(8.5.4)` that one has
`lim Γ(X_λ, 𝒪_{X_λ}) = Γ(X, 𝒪_X)`; since `C_α` is an `A_α`-algebra of finite presentation, the fact that `(8.8.1.1)` is
bijective then follows from `(8.8.2.3)`.

Before passing to the proof of (ii), let us note the following corollaries of (i):

**Corollary (8.8.2.4).**

<!-- label: IV.8.8.2.4 -->

*Suppose `S_0` quasi-compact, `X_α` of finite presentation over `S_α`, `Y_α` of finite type over `S_α` and
quasi-separated over `S_α` (which will be the case for example if `Y_α` is also*

<!-- original page 32 -->

*of finite presentation over `S_α`). Let `f_α : X_α → Y_α` be an `S_α`-morphism. In order that `f : X → Y` be an
isomorphism, it is necessary and sufficient that there exist `λ ≥ α` such that `f_λ : X_λ → Y_λ` be an isomorphism.*

The condition is evidently sufficient. To prove that it is necessary, note first that the question being local on `S_0`
(since `L` is filtered), one can always suppose `S_0` affine, hence quasi-separated. There is by hypothesis an
`S`-morphism `g : Y → X` such that `g ∘ f = 1_X` and `f ∘ g = 1_Y`. Since `X_α` is of finite presentation over `S_α`,
and `Y_α` quasi-compact and quasi-separated (since `S_α` is quasi-compact and quasi-separated), there exist `μ ≥ α` and
an `S_μ`-morphism `g_μ : Y_μ → X_μ` such that `g = g_μ × 1_S` by virtue of `(8.8.2, (i))`. On the other hand, it also
follows from `(8.8.2, (i))` and from the relations `g ∘ f = 1_X` and `f ∘ g = 1_Y` that there exists `ν ≥ μ` such that
one has `g_ν ∘ f_ν = 1_{X_ν}` and `f_ν ∘ g_ν = 1_{Y_ν}`, since `X_α` and `Y_α` are of finite type over `S_α` and
quasi-compact. This means that `f_ν : X_ν → Y_ν` is an isomorphism, whence the corollary.

**Corollary (8.8.2.5).**

<!-- label: IV.8.8.2.5 -->

*Suppose `S_0` quasi-compact and quasi-separated, `X_α` and `Y_α` of finite presentation over `S_α`. In order that `X`
and `Y` be `S`-isomorphic, it is necessary and sufficient that there exist `λ ≥ α` such that `X_λ` and `Y_λ` be
`S_λ`-isomorphic. Moreover, for every `S`-isomorphism `f : X → Y`, there exist `μ ≥ λ` and an `S_μ`-isomorphism
`f_μ : X_μ → Y_μ` such that `f = f_μ × 1_S`.*

The condition is evidently sufficient; conversely, if there exists an `S`-isomorphism `f : X → Y`, it follows from
`(8.8.2, (i))` that `f` is of the form `f_μ × 1_S` for some `μ ≥ α` and a homomorphism `f_μ : X_μ → Y_μ`; but since `f`
is an isomorphism, it follows from `(8.8.2.4)` that there exists `ν ≥ μ` such that `f_ν : X_ν → Y_ν` is an isomorphism.

(ii) Consider again first the case where `S_0 = Spec(A_0)` and `X = Spec(B)` are affine; then the assertion of (ii) is
equivalent to Lemma `(1.8.4.2)`.

To prove (ii) in the general case, note that `S` is quasi-compact and quasi-separated; since `X` is of finite
presentation over `S` and `S` affine over `S_0`, there exists therefore a finite cover `(U_i)` of `S_0` and, if `(W_i)`
is the affine open cover of `S` formed by the inverse images of the `U_i` under the morphism `S → S_0`, a finite cover
`(X_r)` of `X` by affine open sets such that the image under `X → S` of each `X_r` is contained in some `W_{i(r)}`; the
ring `A(X_r)` is then an algebra of finite presentation over the ring `A(W_{i(r)})` `(1.4.6)`. By virtue of Lemma
`(1.8.4.2)` and the fact that `L` is filtered, there exist an index `λ ∈ L` and, for each index `r`, an affine scheme
`Z_{rλ}` of finite presentation over the inverse image `W_{i(r), λ}` of `U_{i(r)}` in `S_λ`, and an `S`-isomorphism
`g_r : Z_{rλ} ×_{S_λ} S ⥲ X_r`. Let `Z_{rs}` be the inverse image under `g_r` of the sub-prescheme induced on the open
set `X_r ∩ X_s` of `X_r`, which is quasi-compact since `X` is quasi-separated, and denote by `g'_{rs}` the restriction
`Z_{rs} → X_r ∩ X_s` of the isomorphism `g_r`. By virtue of `(8.8.2.5)`, there exist `ν ≥ λ` and, for every pair
`(r, s)`, a quasi-compact open set `Z_{rsμ}` of `Z_{rμ} = v_{μλ}⁻¹(Z_{rλ})` such that `Z_{rs}` is the inverse image of
`Z_{rsμ}`; moreover, since `S_μ` is quasi-separated, and `W_{i(r), μ}` an open quasi-compact set in `S_μ`, each of the
`Z_{rsμ}` is of finite presentation over `S_μ` `(1.6.2)`. Consider then, for every pair `(r, s)`, the isomorphism
`h_{sr} = g'_{sr}⁻¹ ∘ g'_{rs}` from `Z_{rs}` onto `Z_{sr}`; it follows from `(8.8.2.4)` that there exist `ν ≥ μ` and,
for every pair `(r, s)`, an isomorphism `h_{srν} : Z_{rsν} → Z_{srν}` such that `h_{sr} = h_{srν} × 1_S`. Finally, for
every triple `(r, s, t)` let us denote by `h'_{sr}` the restriction of `h_{sr}` to

<!-- original page 33 -->

`Z_{rs} ∩ Z_{rt}`; it follows at once from the definitions that `h'_{sr}` is an isomorphism of `Z_{rs} ∩ Z_{rt}` onto
`Z_{sr} ∩ Z_{st}`, and that one has the relation `h'_{ts} ∘ h'_{sr} = h'_{tr}`. By virtue of `(8.8.2, (i))`, there
exists therefore `ρ ≥ ν` such that, for every triple `(r, s, t)`, one has `h'_{tsρ} ∘ h'_{srρ} = h'_{trρ}`. One
concludes that the isomorphisms `h_{srρ}` verify the gluing condition `(0_I, 4.1.7)` and therefore define a prescheme
`X_ρ` such that `X` is isomorphic to `X_ρ ×_{S_ρ} S`. Moreover, the `Z_{rρ}` are of finite presentation over `S_ρ` and,
if one identifies them with open sets of `X_ρ`, the intersections `Z_{rρ} ∩ Z_{sρ}`, isomorphic to the `Z_{rsρ}`, are
quasi-compact, hence `(1.6.3)` `X_ρ` is of finite presentation over `S_ρ`. Q.E.D.

**Scholium (8.8.3).**

<!-- label: IV.8.8.3 -->

The essential content of `(8.8.2)` may again be expressed by saying that if `S_0` is quasi-compact and quasi-separated,
the category of `S`-preschemes of finite presentation is determined up to equivalence by the data of the categories of
`S_λ`-preschemes of finite presentation, the functors `p_{μλ} : X_λ ↦ X_λ ×_{S_λ} S_μ` (for `λ ≤ μ`) between these
categories, and the transitivity isomorphisms `p_{νμ} ∘ p_{μλ} ⥲ p_{νλ}`. Pictorially, one can say that giving an
`S`-prescheme of finite presentation `X` amounts "functorially" to giving an `S_λ`-prescheme of finite presentation
`X_λ`; if an `S_μ`-prescheme of finite presentation `X'_μ` is such that `X` is `S`-isomorphic to `X'_μ ×_{S_μ} S`, there
exists `ν` such that `λ ≤ ν`, `μ ≤ ν` and such that `X_λ ×_{S_λ} S_ν` and `X'_μ ×_{S_μ} S_ν` are `S_ν`-isomorphic. The
fact that `L` is filtered moreover entails that if one gives a finite family `(X^{(i)})_{i ∈ I}` of `S`-preschemes of
finite presentation, and a finite family `(f^{(j)})_{j ∈ J}` of `S`-morphisms between these preschemes (`f^{(j)}` being
therefore of the form `X^{(σ(j))} → X^{(τ(j))}` where `σ` and `τ` are two maps from `J` to `I`), then there is an index
`λ ∈ L`, a family `(X^{(i)}_λ)_{i ∈ I}` of `S_λ`-preschemes of finite presentation and a family `(f^{(j)}_λ)_{j ∈ J}` of
`S_λ`-morphisms such that `X^{(i)}` is identified with `X^{(i)}_λ ×_{S_λ} S` and `f^{(j)}` with `f^{(j)}_λ × 1_S` for
every `i` and `j`; moreover, if one has a relation `f^{(j)} = f^{(k)}`, one can suppose `λ` chosen so that
`f^{(j)}_λ = f^{(k)}_λ`.

Consider in particular three `S`-preschemes of finite presentation `X`, `Y`, `Z` and two `S`-morphisms `f : X → Z`,
`g : Y → Z`, so that the product `X ×_Z Y` relative to these morphisms is again an `S`-prescheme of finite presentation
`(1.6.2)`. Then it follows from what precedes and from `(I, 3.3.11)` that one can write
`X ×_Z Y = (X_λ ×_{Z_λ} Y_λ) ×_{S_λ} S` for a suitable `λ`, `X_λ`, `Y_λ`, `Z_λ` being `S_λ`-preschemes of finite
presentation; one can therefore say that the determination of `S`-preschemes of finite presentation by giving the
`S_λ`-preschemes of finite presentation is "compatible with fibre products". One has seen on the other hand `(8.6.3)`
that if `g` is an immersion, one can suppose the same of `g_λ : Y_λ → Z_λ`; identifying `Y` (resp. `Y_λ`) with a
sub-prescheme of `Z` (resp. `Z_λ`), one sees therefore that one can write, for a suitable `λ`,
`f⁻¹(Y) = f_λ⁻¹(Y_λ) ×_{S_λ} S` `(I, 4.4.1)`; there is therefore also "compatibility with the formation of inverse
images of sub-preschemes". More particularly, if `f_1`, `f_2` are two `S`-morphisms from `X` to `Y`, one calls *kernel*
of this pair of morphisms the inverse image `N` of the diagonal sub-prescheme of `Y ×_S Y` under the `S`-morphism
`(f_1, f_2)_S`; one deduces from what precedes that one will have, for a suitable `λ`, `N = N_λ ×_{S_λ} S`, where `N_λ`
is the kernel of the pair of `S_λ`-morphisms `(f_{1λ}, f_{2λ})` from `X_λ` to `Y_λ`. These remarks extend to arbitrary
finite products and to the "kernels" of arbitrary finite systems of `S`-morphisms from one `S`-prescheme of finite
presentation

<!-- original page 34 -->

into another; one concludes that in a general way the formation of `S`-preschemes of finite presentation by giving the
`S_λ`-preschemes of finite presentation is "compatible with finite projective limits", such a limit being by definition
the kernel of a finite system of morphisms from a single `S`-prescheme into a product of `S`-preschemes `(T, 1.8)`.

We shall permit ourselves currently in what follows to make the translations implied by the preceding properties (as
well as by `(8.3.11)`, `(8.5.2)` and `(8.6.3)`) without always constraining ourselves to justify them step by step as
above. For example, giving a "prescheme in groups" `G` of finite presentation over `S` is equivalent to giving a
prescheme in groups `G_λ` of finite presentation over an `S_λ` for `λ` sufficiently large; for indeed to write the
associativity condition for the `S`-morphism "composition law" `G ×_S G → G` of the prescheme in groups amounts to
writing that the kernel of two `S`-morphisms of the form `G ×_S G ×_S G → G` is equal to `G ×_S G ×_S G` `(II, 8.3.9)`,
and the other conditions intervening in the definition of a prescheme in groups are interpreted likewise.

<!-- original page 34 -->

### 8.9. First applications to the elimination of Noetherian hypotheses.

**Proposition (8.9.1).**

<!-- label: IV.8.9.1 -->

*Let `A` be a ring and `X` an `A`-prescheme.*

*(i) The following conditions are equivalent:*

*a) `X` is of finite presentation over `A`.*

*b) There exists a Noetherian ring `A_0`, a prescheme `X_0` of finite type over `A_0`, a ring homomorphism `A_0 → A`,
and an `A`-isomorphism `X_0 ⊗_{A_0} A ⥲ X`.*

*c) There exists a sub-ring `A_0` of `A`, which is a `Z`-algebra of finite type, a prescheme `X_0` of finite type over
`A_0`, and an `A`-isomorphism `X_0 ⊗_{A_0} A ⥲ X`.*

*(ii) If `ℱ` is a quasi-coherent `𝒪_X`-Module of finite presentation, one may suppose the sub-ring `A_0` chosen so that
there exists a coherent `𝒪_{X_0}`-Module `ℱ_0` such that `ℱ` is isomorphic to `ℱ_0 ⊗_{A_0} A`; `Supp(ℱ)` is
constructible and closed in `X`, and there is a closed sub-prescheme `Z` of `X`, having `Supp(ℱ)` as underlying space,
such that the canonical immersion `Z → X` is of finite presentation.*

*(iii) If `Y` is a second `A`-prescheme of finite presentation, and `f : X → Y` an `A`-morphism, one may suppose the
sub-ring `A_0` of `A` chosen so that there exist a prescheme `Y_0` of finite type over `A_0`, an `A`-isomorphism
`Y_0 ⊗_{A_0} A ⥲ Y` and an `A_0`-morphism `f_0 : X_0 → Y_0` (necessarily of finite type) such that `f` is identified
with `f_0 ⊗ 1_A`.*

(i) Since `A` is the inductive limit of its sub-rings of finite type over `Z`, a) implies c) by virtue of
`(8.8.2, (ii))`; c) implies b) since a `Z`-algebra of finite type is a Noetherian ring; finally, if `A_0` is Noetherian,
an `A_0`-prescheme of finite type is of finite presentation `(1.6.1)`, hence b) implies a) by virtue of
`(1.6.2, (iii))`.

Assertion (ii) is deduced immediately from `(8.5.2, (ii))`, `(8.3.11)` and `(1.8.2)`, and assertion (iii) from
`(8.8.2, (i))`.

**(8.9.2)**

<!-- label: IV.8.9.2 -->

Proposition `(8.9.1)` and the results of `(8.5.2)` and `(8.8.2)` make it possible to extend, in many cases, to morphisms
of finite presentation `X → Y` results proved by Noetherian techniques under the assumption that `Y` is locally
Noetherian.

<!-- original page 35 -->

We shall see numerous examples of this in what follows; here we restrict ourselves to giving a few results of this type.

**Proposition (8.9.3).**

<!-- label: IV.8.9.3 -->

*Let `A` be a ring and `M` an `A`-module of finite presentation. Then every surjective `A`-endomorphism of `M` is
bijective.*

Indeed, view `A` as the inductive limit of its sub-`Z`-algebras of finite type. It follows from `(8.5.2.6)` that there
exists one of these sub-algebras `A_0` and an `A_0`-module `M_0` of finite presentation such that `M` is `A`-isomorphic
to `M_0 ⊗_{A_0} A`; moreover, if `f : M → M` is a surjective `A`-endomorphism, one may suppose `(8.5.2, (i))` that there
exists an `A_0`-endomorphism `f_0 : M_0 → M_0` such that `f = f_0 ⊗ 1_A`; finally `(8.5.7)` one may suppose `f_0` to be
surjective. But since `A_0` is Noetherian and `M_0` is an `A_0`-module of finite type, `M_0` is a Noetherian
`A_0`-module, hence (Bourbaki, *Alg.*, chap. VIII, §2, n° 2, lemma 3) `f_0` is bijective, and consequently so is `f`.

**Proposition (8.9.4) ("generic flatness theorem").**

<!-- label: IV.8.9.4 -->

*Let `Y` be an integral prescheme, `u : X → Y` a morphism of finite type and locally of finite presentation, `ℱ` a
quasi-coherent `𝒪_X`-Module of finite presentation. Then there exists a non-empty open `U` of `Y` such that `ℱ|u⁻¹(U)`
is flat over `U`.*

The reasoning of the beginning of `(6.9.1)` reduces matters to proving the

**Lemma (8.9.4.1).**

<!-- label: IV.8.9.4.1 -->

*Let `A` be an integral ring, `B` an `A`-algebra of finite presentation, `M` a `B`-module of finite presentation. Then
there exists an `f ≠ 0` in `A` such that `M_f` is a free `A_f`-module.*

Indeed, by `(8.9.1)` there is a sub-`Z`-algebra of finite type `A_0` of `A`, an `A_0`-algebra of finite type `B_0` and a
`B_0`-module of finite type `M_0` such that `B` is `A`-isomorphic to `B_0 ⊗_{A_0} A` and `M` is `B`-isomorphic to
`M_0 ⊗_{A_0} A`; by `(6.9.2)`, there exists `f_0 ≠ 0` in `A_0` such that `(M_0)_{f_0}` is a free `(A_0)_{f_0}`-module.
Since `M_{f_0} = (M_0)_{f_0} ⊗_{A_0} A` and `A_{f_0} = (A_0)_{f_0} ⊗_{A_0} A`, `M_{f_0}` is a free `A_{f_0}`-module.

**Corollary (8.9.5).**

<!-- label: IV.8.9.5 -->

*Let `S` be a quasi-compact and quasi-separated prescheme, `u : X → S` a morphism of finite presentation, `ℱ` a
quasi-coherent `𝒪_X`-Module of finite presentation. Then there exists a partition `(S_i)_{1 ≤ i ≤ n}` of `S` into a
finite number of locally closed sets in `S` such that, for `1 ≤ i ≤ n`, there exists a sub-prescheme `S_i'` of `S`,
having `S_i` as underlying space, of finite presentation over `S`, such that if one sets `X_i = X ×_S S_i'`, the
`𝒪_{X_i}`-Module `ℱ_i = ℱ ⊗_{𝒪_X} 𝒪_{X_i}` is flat over `S_i'`.*

Consider a finite cover `(U_j)_{1 ≤ j ≤ n}` of `S` by affine opens, and define by induction `T_1 = U_1`,
`T_j = U_j − ⋃_{k < j} (U_j ∩ U_k)` for `j ≥ 2`; each `T_j` is closed in the affine open `U_j`, and the `T_j` are
pairwise disjoint; moreover the `U_j ∩ U_k` are quasi-compact since `S` is quasi-separated, and consequently (`S` being
also quasi-compact) are constructible in `S` `(1.8.1)`, hence so are the `T_j`. It will obviously suffice to prove the
corollary for a suitable sub-prescheme `T_j'` of `S` having `T_j` as underlying space, of finite presentation over `S`,
and for the morphism and the Module deduced respectively from `u` and `ℱ` by the base change `T_j' → S`. Note for this
that if one takes on `U_j` the prescheme structure induced by that of `S`, the open immersion `U_j → S` is quasi-compact
since `S` is quasi-separated `(1.2.7)`, hence is of finite presentation `(1.6.2, (i))`.

<!-- original page 36 -->

It therefore suffices that `T_j'` be of finite presentation over `U_j`; in other words, one may already restrict to the
case where `U = S` and `T_j = T` is closed constructible in `S`. Let `S = Spec(A)`, and view `A` as inductive limit of
its sub-`Z`-algebras of finite type, so that `S = lim S_λ`, where the `S_λ` are affine and Noetherian. By virtue of
`(8.3.11)`, there exist a `λ` and a closed part (necessarily constructible) `T_λ` of `S_λ` such that `T = u_λ⁻¹(T_λ)`
(`u_λ : S → S_λ` being the canonical morphism). One equips `T_λ` with a structure of sub-prescheme of `S_λ` and takes
`T' = T_λ ×_{S_λ} S`; since the canonical immersion `T_λ → S_λ` is of finite presentation `(1.6.1)`, so is the immersion
`T' → S`. Since `T'` is affine, one sees finally that one can restrict to the case where `T' = S` is affine. Then
`(8.9.1)`, with the same notation, there exist a `λ`, a morphism of finite type `u_λ : X_λ → S_λ` and a coherent
`𝒪_{X_λ}`-Module `ℱ_λ` such that `X` is isomorphic to `X_λ ×_{S_λ} S` and `ℱ` to `ℱ_λ ⊗_{𝒪_{X_λ}} 𝒪_X`. One may then
apply to `S_λ`, `X_λ` and `ℱ_λ` the result of `(6.9.3)`, and there are sub-preschemes `S_{λ,i}` of `S_λ` whose
underlying sets form a partition of `S_λ` and which are such that, setting `X_{λ,i} = X_λ ×_{S_λ} S_{λ,i}` and
`ℱ_{λ,i} = ℱ_λ ⊗_{𝒪_{X_λ}} 𝒪_{X_{λ,i}}`, the Module `ℱ_{λ,i}` is flat over `S_{λ,i}`. The `S_i' = S_{λ,i} ×_{S_λ} S` are
then sub-preschemes of `S` answering the question, by virtue of `(2.1.4)`.

### 8.10. Permanence properties of morphisms under projective passage to the limit.

In this section we keep the general hypotheses and notation of `(8.8.1)`.

**Proposition (8.10.1).**

<!-- label: IV.8.10.1 -->

*If there exists `λ` such that, for `μ ≥ λ`, `f_μ` is an open morphism (resp. universally open), then `f` is an open
morphism (resp. universally open).*

Since `X = X_λ ×_{Y_λ} Y`, the assertion relative to universally open morphisms is a special case of `(2.4.3, (vi))`.
Suppose then `f_μ` open for `μ ≥ λ`; it suffices to see that for every quasi-compact open `U` of `X`, `f(U)` is open in
`Y`. Now there exists `μ ≥ λ` such that `U = v_μ⁻¹(U_μ)`, where `U_μ` is a quasi-compact open in `X_μ` `(2.3.11)`; one
then has `f(v_μ⁻¹(U_μ)) = w_μ⁻¹(f_μ(U_μ))` `(I, 3.4.8)`, hence `f(U)` is open in `Y`.

**Corollary (8.10.2).**

<!-- label: IV.8.10.2 -->

*Let `f : X → Y` be a morphism. In order that `f` be universally open, it suffices that, for every integer `n > 0`, if
one sets `Y_n = Y ⊗_Z Z[T_1, …, T_n] (= 𝕍_Y^n)` and `X_n = X ×_Y Y_n`, the canonical projection
`f_n = f × 1_{Y_n} : X_n → Y_n` be an open morphism.*

To prove that `f` is universally open, it suffices to prove that this is so for the restriction `f⁻¹(U) → U` of `f` for
every affine open `U` of `Y`; since, by hypothesis, if `U_n = U ⊗_Z Z[T_1, …, T_n]` is the inverse image of `U` in
`Y_n`, the morphism `f_n⁻¹(U_n) → U_n`, restriction of `f_n`, is open, one sees that one may restrict to the case where
`Y = Spec(A)` is affine. Moreover, it obviously suffices to show that for every morphism `Y' → Y`, where `Y' = Spec(A')`
is itself also affine, `f' = f_{(Y')}` is open. Suppose first that `A'` is an `A`-algebra of finite type, hence quotient
of a polynomial algebra `A[T_1, …, T_n]`; then `Y'` is a closed sub-prescheme of `Y_n` and `f'` the

<!-- original page 37 -->

restriction of `f_n` to `f_n⁻¹(Y')`; but for every open `V` of `X_n` one has `f'(V ∩ f_n⁻¹(Y')) = f_n(V) ∩ Y'`, and
since by hypothesis `f_n(V)` is open in `Y_n`, this shows that `f'` is also an open morphism. When `A'` is arbitrary, it
may be viewed as inductive limit of its sub-`A`-algebras of finite type `A_λ'`, and the fact that `f'` is an open
morphism results from what precedes and from `(8.10.1)`.

**Proposition (8.10.3).**

<!-- label: IV.8.10.3 -->

*Suppose there exists `α` such that: 1° `S_α` is quasi-compact; 2° the morphisms `X_α → S_α`, `Y_α → S_α` are
quasi-compact and the morphism `Y_α → S_α` is quasi-separated; 3° for `α ≤ λ ≤ μ`, the morphisms `u_{λμ} : S_μ → S_λ`
are flat; 4° `f_α(X_α)` is constructible in `Y_α`. Then, in order that `f` be dominant, it is necessary and sufficient
that there exist `λ ≥ α` such that `f_λ` be dominant.*

The hypotheses entail that `Y_α` is quasi-compact and that the morphism `f_α` is quasi-compact `(1.2.4)`; consequently
`f_α(X_α) = Z_α` is pro-constructible `(1.9.5, (v"))` in `Y_α`. If one sets `Z_λ = w_{αλ}⁻¹(Z_α)` for `λ ≥ α` and
`Z = w_α⁻¹(Z_α)`, one then has `Z_λ = f_λ(X_λ)` and `Z = f(X)` `(I, 3.4.8)`, and `Z_λ` is pro-constructible in `Y_λ`
`(1.9.5, (vi))`. It then suffices to apply `(8.3.13)` after replacing `S_λ`, `Z_λ` and `Z_λ'` by `Y_λ`, `Y_λ` and `Z_λ`
respectively.

**Proposition (8.10.4).**

<!-- label: IV.8.10.4 -->

*Suppose there exists `α` such that `Y_α` is quasi-compact and `f_α` of finite type and quasi-separated. In order that
the morphism `f` be separated, it is necessary and sufficient that there exist `λ ≥ α` such that `f_λ` be separated.*

The question being local on `Y_α` (since `Y_α` is quasi-compact and `L` filtered), one may restrict to the case where
`Y_α` is affine, hence quasi-separated, and the hypothesis entails that `X_α` (hence the `X_λ` and `X`) are
quasi-compact and quasi-separated. Set `X_λ' = X_λ ×_{Y_λ} X_λ` for `λ ≥ α` and `X' = X ×_Y X`; one has
`X_λ' = X_α' ×_{Y_α} Y_λ` and `X' = X_α' ×_{Y_α} Y`; the first-projection morphism `X_λ' → X_α'` is quasi-compact and
quasi-separated by hypothesis `(1.2.3, (iii))`, hence `X_λ'` is quasi-compact and quasi-separated. Note now that if one
denotes by `Δ_λ` (resp. `Δ`) the diagonal of `X_λ ×_{Y_λ} X_λ` (resp. of `X ×_Y X`), it follows from
`(I, 5.3.4 and 3.4.8)` that `Δ_μ` (resp. `Δ`) is the inverse image of `Δ_λ` under the morphism `v_{λμ}' : X_μ' → X_λ'`
(resp. `v_λ' : X' → X_λ'`). On the other hand, `Δ_α` is constructible in `X_α'`: indeed, since `f_α` is quasi-separated,
the diagonal immersion `X_α → X_α'` is quasi-compact, and locally of finite presentation since `f_α` is of finite type
`(1.4.3` and `I, 5.4, (iii))`; it then follows from `(1.8.4.1)` that `Δ_α` is locally constructible, hence constructible
since `X_α'` is quasi-compact. One may now apply `(8.3.12)` after replacing `S_λ` and `Z_λ` by `X_λ'` and `Δ_λ`
respectively.

**Theorem (8.10.5).**

<!-- label: IV.8.10.5 -->

*Suppose `S_0` quasi-compact, `X_α` and `Y_α` of finite presentation over `S_α`, and let `f_α : X_α → Y_α` be an
`S_α`-morphism. Consider, for a morphism, the property of being:*

*(i) an isomorphism;*

*(i bis) a monomorphism;*

*(ii) an immersion;*

*(iii) an open immersion;*

*(iv) a closed immersion;*

*(v) separated;*

*(vi) surjective;*

<!-- original page 38 -->

*(vii) radicial;*

*(viii) affine;*

*(ix) quasi-affine;*

*(x) finite;*

*(xi) quasi-finite;*

*(xii) proper.*

*Then, if `P` denotes one of the preceding properties, in order that `f` have property `P`, it is necessary and
sufficient that there exist `λ ≥ α` such that `f_λ` have property `P` (in which case `f_μ` also has it for `μ ≥ λ`).*

*If `S_0` is moreover supposed quasi-separated, the same conclusion is valid when `P` is the property of being:*

*(xiii) projective;*

*(xiv) quasi-projective.*

The case where `P` is one of the properties (i) or (v) is inserted in the statement only for the record; in these cases,
the theorem follows from what has been proved respectively in `(8.8.2.4)` and `(8.10.4)`. Moreover, taking into account
`(I, 5.4.1` and `5.3.4)`, (v) also results from (iv). The case (i bis) is deduced at once from (i), using `(I, 5.3.8)`
and noting (as was already used in `(8.10.4)`) that the diagonal `Δ` is deduced from `Δ_λ` by the base change `S → S_λ`.

One notes on the other hand that (vi), (vii) and (xi) are in fact conditions on the fibres `f⁻¹(y)` of the morphisms
considered, taking into account the transitivity of fibres under base change `(I, 3.6.4)`: condition (vi) signifies in
effect that all the fibres must be non-empty, condition (vii) that they must be radicial `(I, 3.5.8)`, and condition
(xi) that they must be finite `(II, 6.2.2` and `6.2.3` and `II, 6.4.4`, taking into account that `f` and the `f_λ` are
morphisms of finite type by `(1.5.4, (v))`. The theorem in these three cases will therefore again be consequence of a
general result on this type of properties concerning only the fibres, which will be established in `(9.3.3)`; we
therefore postpone until that moment the demonstration of the theorem in case (xi) (of course, the reader can verify
that, except in nos. `8.11` and `8.12`, we shall not make use of the theorem in this case until `(9.3.3)`, and that
`(8.11)` and `(8.12)` will not be used before `(9.3.3)`).

For the cases that remain to be proved, one may restrict to showing that the condition of the statement is necessary,
all the properties `P` considered being invariant under base change (see chap. I and II in the numbers concerning each
of these properties). One may moreover suppose that `S_α = S_0` and that `Y_α = S_α`, hence `Y_λ = S_λ` for all `λ ≥ α`.
Finally, properties (i) to (xii) are local on `S_0`, hence, since `S_0` is a finite union of affine opens and `L` is
filtered, one may restrict for proving them to the case where `S_0 = Spec(A_0)` is affine (hence quasi-separated). One
denotes by `A_λ` (resp. `A`) the ring of `S_λ` (resp. `S`).

*Cases (ii), (iii), (iv):* Suppose that `f` is an immersion (resp. an open immersion, resp. a closed immersion), and let
`X'` be the sub-prescheme (resp. induced on an open, resp. closed) of `S` associated with `f`, which is therefore an
`S`-prescheme of finite presentation.

<!-- original page 39 -->

By virtue of `(8.6.3)`, there exist therefore a `λ ≥ α` and a sub-prescheme (resp. induced on an open, resp. closed)
`X_λ'` of `S_λ`, of finite presentation over `S_λ`, such that `X'` is isomorphic to `X_λ' ×_{S_λ} S`. For every `μ ≥ λ`,
`X_μ' = X_λ' ×_{S_λ} S_μ` is therefore a sub-prescheme (resp. induced on an open, resp. closed) of `S_μ`, of finite
presentation over `S_μ`, and it therefore follows from `(8.8.2.4)` and `(8.8.2.5)` that there exist a `μ ≥ λ` and an
isomorphism `g_μ : X_μ → X_μ'` such that `g = g_μ × 1_S` is the isomorphism `X → X'` associated with `f`; whence the
conclusion.

*Cases (vi) and (vii):* One knows `(1.8.4.1)` that `Z_α = f_α(X_α)` is constructible in `S_α`; if one sets
`Z_λ = u_{αλ}⁻¹(Z_α)` for `λ ≥ α` and `Z = u_α⁻¹(Z_α)`, one has `Z_λ = f_λ(X_λ)` and `Z = f(X)` `(I, 3.4.8)`. Since, by
virtue of `(8.3.11)`, the canonical application `lim 𝓒(S_λ) → 𝓒(S)` is injective, the relation `f(X) = S` implies the
existence of a `λ ≥ α` such that `f_λ(X_λ) = S_λ`, which proves the theorem in case (vi). To prove it in case (vii), it
suffices to note that the structure morphism `X_α ×_{S_α} X_α → S_α` is of finite presentation since this is so of the
first projection `X_α ×_{S_α} X_α → X_α` `(1.6.2)`; it therefore suffices, by virtue of `(1.8.7.1)`, to apply case (vi)
of the theorem to the diagonal morphism `Δ_{f_α} : X_α → X_α ×_{S_α} X_α`, noting that one has
`Δ_{f_λ} = Δ_{f_α} × 1_{S_λ}` and `Δ_f = Δ_{f_α} × 1_S` `(I, 5.3.4` and `3.3.11)`.

*Cases (viii) and (ix):* Since `S = Spec(A)` is affine, to say that `f : X → S` is affine (resp. quasi-affine) signifies
that there exists an integer `r` and a closed immersion (resp. an immersion) `j : X → 𝕍_S^r = Spec(A[T_1, …, T_r])` of
`S`-preschemes, since `f` is of finite type and `S` quasi-compact `(II, 5.1.9)`. Since `𝕍_S^r = 𝕍_{S_0}^r ×_{S_0} S`,
and `𝕍_{S_0}^r` is an `S_0`-prescheme of finite presentation, it follows from `(8.8.2, (i))` applied to the `S`-morphism
`j` that there exists a `λ` and an `S_λ`-morphism `j_λ : X_λ → 𝕍_{S_λ}^r` such that `j = j_λ × 1_S`; applying then (iv)
(resp. (ii)) to `j`, one deduces that there exists `μ ≥ λ` such that `j_μ` is a closed immersion (resp. an immersion);
consequently `f_μ` is affine (resp. quasi-affine).

*Case (x):* By hypothesis, one has `X = Spec(B)`, where `B` is an `A`-algebra which is an `A`-module of finite
presentation `(1.4.7)`; it follows therefore from `(8.5.2, (ii))` that there is a `λ` and an `A_λ`-module of finite
presentation `B_λ` such that the `A`-module `B` is isomorphic to `B_λ ⊗_{A_λ} A`. The `A`-algebra structure of `B` is
defined by an `A`-homomorphism `m : B ⊗_A B → B`; since one has `B ⊗_A B = (B_λ ⊗_{A_λ} B_λ) ⊗_{A_λ} A`, there exists
according to `(8.5.2, (i))` a `μ ≥ λ` and an `A_μ`-homomorphism `m_μ : B_μ ⊗_{A_μ} B_μ → B_μ` such that `m = m_μ ⊗ 1`.
Considering the usual diagrams expressing the associativity and commutativity of `m`, one sees by applying again
`(8.5.2, (i))` that there exists `ν ≥ μ` such that `m_ν` defines on `B_ν` an associative and commutative multiplication;
in the same way one sees that one can suppose `ν` taken large enough so that the ring `B_ν` thus defined admits a unit
element. If `X_ν = Spec(B_ν)`, it is then clear that `X` is `S`-isomorphic to `X_ν ×_{S_ν} S`, hence, by virtue of (i),
there exists `ρ ≥ ν` such that `X_ρ` and `X_ν ×_{S_ν} S_ρ` are `S_ρ`-isomorphic, which finishes the demonstration in
this case.

To prove the theorem in case (xii), we first prove the following proposition:

**Proposition (8.10.5.1) (Chow's lemma for morphisms of finite presentation).**

<!-- label: IV.8.10.5.1 -->

*Let `A` be a ring, `X`, `Y` two `A`-preschemes of finite presentation, `f : X → Y`*

<!-- original page 40 -->

*an `A`-morphism, separated. Then there exist two `A`-preschemes `X'`, `P` of finite presentation, and `A`-morphisms
`p : P → Y`, `j : X' → P`, `g : X' → X`, such that the diagram*

```text
                          X' ───j──→ P
                          │           │
                          g           p
                          ↓           ↓
                          X ────f──→ Y
```

*is commutative, and: 1° `p` is projective; 2° `g` is projective and surjective; 3° `j` is an open immersion.*

Indeed, let `A_0 ⊂ A`, `X_0`, `Y_0` and `f_0` be determined as in `(8.9.1)` so that `Y_0` is Noetherian and `f_0` is of
finite type; one may moreover suppose `f_0` separated by `(8.10.4)`. Chow's lemma `(II, 5.6.1)` then shows the existence
of three morphisms `p_0 : P_0 → Y_0`, `g_0 : X_0' → X_0` and `j_0 : X_0' → P_0`, of finite type, such that the diagram

```text
                          X_0' ──j_0──→ P_0
                          │              │
                          g_0            p_0
                          ↓              ↓
                          X_0 ───f_0──→ Y_0
```

is commutative, and `p_0` is projective, `g_0` projective and surjective, and `j_0` an open immersion. The properties of
the statement then result from the invariance of the preceding properties under base change `(II, 5.5.5, (iii)` and
`I, 3.5.2` and `4.3.2)`.

*Case (xii):* Apply to the morphism `f_0 : X_0 → S_0` proposition `(8.10.5.1)`: one then has a commutative diagram

```text
                          X_0' ──j_0──→ P_0
                          │              │
                          g_0            p_0
                          ↓              ↓
                          X_0 ───f_0──→ S_0
```

where `p_0` is projective, `g_0` projective and surjective, and `j_0` an open immersion; one deduces for each `λ` an
analogous diagram where the morphisms `p_λ = p_0 × 1_{S_λ}`, `g_λ = g_0 × 1_{S_λ}` and `j_λ = j_0 × 1_{S_λ}` have
respectively the same properties, and likewise for the projective-limit morphisms `p = p_0 × 1_S`, `g = g_0 × 1_S`,
`j = j_0 × 1_S`. Since `g` is proper `(II, 5.5.3)`, so is `p ∘ j = f ∘ g` `(II, 5.4.2)`, and since `p` is separated, `j`
is proper, hence a closed immersion; applying case (iv) to the morphism `j` (noting that `X_0'` and `P_0` are
`S_0`-preschemes of finite presentation `(8.10.5.1` and `1.6.2)`), one sees that there exists `λ` such that `j_λ` is a
closed immersion, hence is proper `(II, 5.4.2)`. But then `f_λ ∘ g_λ = p_λ ∘ j_λ` is proper `(II, 5.5.3` and `5.4.2)`,
and since `g_λ` is surjective, and one can suppose `f_λ` separated by virtue of the hypothesis on `f` and of (v), it
follows from `(II, 5.4.3)` that `f_λ` is proper.

*Cases (xiii) and (xiv):* By virtue of (xii) and of `(II, 5.5.3)` (which is applicable since the `S_λ` are quasi-compact
and quasi-separated, taking into account `(1.7.19)`), it suffices to

<!-- original page 41 -->

consider the case where `f` is quasi-projective. Suppose then that there exists an invertible `𝒪_X`-Module `ℒ` which is
`f`-ample; since `S_0` is quasi-compact and quasi-separated, so is `X_0` `(1.2.3)`, and there is therefore a `λ` and a
quasi-coherent `𝒪_{X_λ}`-Module `ℒ_λ` of finite presentation such that `ℒ = v_λ^*(ℒ_λ)` `(8.5.2, (ii))`; moreover, by
virtue of `(8.5.5)`, one may suppose `ℒ_λ` invertible. The theorem in this case is then consequence of the more precise
lemma:

**Lemma (8.10.5.2).**

<!-- label: IV.8.10.5.2 -->

*Suppose `S_0` quasi-compact, and let `ℒ_λ` be an invertible `𝒪_{X_λ}`-Module. In order that `ℒ` be an `𝒪_X`-Module
ample for `f` (resp. very ample for `f`), it is necessary and sufficient that there exist `μ ≥ λ` such that `ℒ_μ` be
ample for `f_μ` (resp. very ample for `f_μ`).*

The condition being obviously sufficient `(II, 4.4.10` and `4.6.13)`, let us show that it is necessary; the `S_λ` being
quasi-compact and the `f_λ` of finite type, one may, by replacing `ℒ` by a suitable tensor power, restrict to the case
where `ℒ` is very ample `(II, 4.6.11)`. Moreover, the question being here local on `S_0` (in view of `(II, 4.4.5)` and
the fact that `L` is filtered), one may restrict to the case where `S_0` (and consequently `S`) is affine. Then, by
virtue of `(II, 4.4.1, (ii)` and `II, 4.1.2)`, there exists an `S`-immersion `j : X → ℙ_S^r = P` such that `ℒ` is
isomorphic to `j^*(𝒪_P(1))`. Taking into account `(8.8.2, (i))`, of (ii) and of `(II, 4.1.3)`, there exists therefore a
`μ ≥ λ` and an immersion `j_μ : X_μ → ℙ_{S_μ}^r = P_μ` such that `j = j_μ × 1_S`; using next `(II, 4.1.3.2)` and
`(8.5.2.5)`, one sees that there exists `ν ≥ μ` such that `ℒ_ν` is isomorphic to `j_ν^*(𝒪_{P_ν}(1))`, which shows that
`ℒ_ν` is very ample for `f_ν` `(II, 4.4.2)`.

### 8.11. Application to quasi-finite morphisms.

We propose in this section to prove the two following theorems:

**Theorem (8.11.1).**

<!-- label: IV.8.11.1 -->

*Let `f : X → Y` be a proper morphism, locally of finite presentation, and quasi-finite. Then the morphism `f` is
finite.*

**Theorem (8.11.2).**

<!-- label: IV.8.11.2 -->

*Let `f : X → Y` be a morphism locally of finite presentation, quasi-finite and separated. Then the morphism `f` is
quasi-affine, and a fortiori quasi-projective.*

**Remark (8.11.3).**

<!-- label: IV.8.11.3 -->

We shall see below that, for the proof of `(8.11.1)` and `(8.11.2)`, one may reduce to the case where `Y` is locally
Noetherian; one notes that in this case one obtains thereby another demonstration of Chevalley's theorem `(III, 4.4.2)`.

**(8.11.4)**

<!-- label: IV.8.11.4 -->

The hypotheses and conclusions of `(8.11.1)` and `(8.11.2)` are all local on `Y`
`(1.6.1, 1.2.6, (II, 5.1.1), (II, 5.4.1)` and `(II, 6.2.2))`, hence one may suppose `Y = Spec(A)` affine. One knows that
there then exists a sub-ring `A_0` of `A`, which is a `Z`-algebra of finite type, and a morphism of finite type
`f_0 : X_0 → Spec(A_0)` such that `X` identifies with `X_0 ⊗_{A_0} A` and `f` with `f_0 × 1` `(8.9.1)`. Moreover, `A`
may be viewed as inductive limit of its sub-rings containing `A_0` and which are `Z`-algebras of finite type; using the
method of `(8.1.2, c))` as well as `(8.10.5, (v), (xi)` and `(xii))`, one sees that it suffices to prove the theorems
`(8.11.1)` and `(8.11.2)` for `f_0`. Suppose then henceforth `Y` Noetherian; using now the method of `(8.1.2, a))` as
well as `(8.10.5, (v), (ix), (x), (xi)` and `(xii))`, one may replace `Y` by `Spec(𝒪_y)`, where `y` is a

<!-- original page 42 -->

point of `Y`, hence one sees finally that one may suppose `Y = Spec(A)`, where `A` is a Noetherian local ring. Let `𝔪`
be the maximal ideal of `A`, `Â` the completion of `A` for the `𝔪`-preadic topology; one knows that `Â` is a Noetherian
local ring and that the morphism `Spec(Â) → Spec(A)` is faithfully flat and quasi-compact `(0_I, 7.3.5)`; applying
`(2.7.1, (i), (vii), (xiv), (xv)` and `(xvi))`, one sees moreover that one may restrict to the case where `A` is
complete. It then follows from `(II, 6.2.6)` that `X = X' ⊔ X''`, where `X'` is a `Y`-scheme finite and `X''` a
`Y`-scheme quasi-finite such that `X'' ∩ f⁻¹(y) = ∅`.

Place ourselves first in the hypotheses of `(8.11.1)`; since `f` is proper, `X''`, which is closed in `X`, is proper
over `Y` `(II, 5.4.10)`, hence `f(X'')` is closed in `Y`; but `y` is not contained in `f(X'')`, and moreover is in the
closure of every point of `Y`, hence `f(X'') = ∅`, and consequently `X''` is empty and `f` is finite.

Place ourselves now in the hypotheses of `(8.11.2)` and, restricting (as one may do by what precedes) to the case where
`Y = Spec(A)` is affine and Noetherian of finite dimension, reason moreover by induction on the dimension of `Y`.
Reducing as above to the case where `A` is in addition local and complete, one has `dim(𝒪_y) = dim(A) = dim(Y)` and for
every `ξ ≠ y`, `dim(𝒪_ξ) < dim(𝒪_y)`, hence `dim(Y − {y}) < dim(Y)`. Now, by hypothesis one has `f(X'') ⊂ Y − {y}` and
the restriction of `f` to `X''` is obviously a quasi-finite and separated morphism; applying to `Y − {y}` and `X''` the
inductive hypothesis, one sees that `X''` is quasi-affine over `Y − {y}`; but the open `Y − {y}` being quasi-affine over
`Y` since `Y` is Noetherian, `X''` is also quasi-affine over `Y` `(II, 5.1.10, (ii))`; since moreover `X'` is finite
(and a fortiori affine) over `Y`, `X` is quasi-affine over `Y` `(II, 4.6.17` and `5.1.2, c'))`.

**Proposition (8.11.5).**

<!-- label: IV.8.11.5 -->

*Let `f : X → Y` be a morphism of finite presentation. The following properties are equivalent:*

*a) `f` is a closed immersion.*

*b) `f` is a proper monomorphism.*

*c) `f` is proper and for every `y ∈ Y`, `f⁻¹(y)` is radicial and geometrically reduced over `k(y)` (that is to say,
empty or `k(y)`-isomorphic to `Spec(k(y))`).*

It is clear that a) implies b). To see that b) implies c), note `(I, 3.3.12)` that for every `y ∈ Y`, the morphism
`f⁻¹(y) → Spec(k(y))` deduced from `f` by base change is a monomorphism, hence is injective, and consequently `f⁻¹(y)`
is empty or reduced to a point, and in any case affine. Moreover, if `A` is the ring of `f⁻¹(y)`, the canonical
homomorphism `A ⊗_{k(y)} A → A` is bijective `(I, 5.3.8)`. This entails obviously that `A = k(y)`, otherwise there would
be an element `a ∈ A` not in `k(y)` and the images of `a ⊗ 1` and `1 ⊗ a` in `A` would both be equal to `a`, whereas
`a ⊗ 1 ≠ 1 ⊗ a` since `1` and `a` form a linearly independent system over `k(y)`.

It remains to prove that c) implies a). It follows first of all from `(8.11.1)` that `f` is a finite morphism, hence
`X = Spec(𝒜)`, where `𝒜` is a finite `𝒪_Y`-Algebra. It therefore suffices to prove that the canonical homomorphism
`𝒪_Y → 𝒜` is surjective `(II, 1.4.10)`, or equivalently that for every `y ∈ Y`, the homomorphism `𝒪_y → 𝒜_y` is
surjective. But by hypothesis

<!-- original page 43 -->

`f⁻¹(y) = Spec(𝒜_y / 𝔪_y 𝒜_y)` `(II, 1.5.5)` is such that the corresponding homomorphism
`k(y) = 𝒪_y / 𝔪_y → 𝒜_y / 𝔪_y 𝒜_y` is bijective; since `𝒜_y` is an `𝒪_y`-module of finite type, Nakayama's lemma shows
that `𝒪_y → 𝒜_y` is surjective, which finishes the demonstration.

**Remark (8.11.5.1).**

<!-- label: IV.8.11.5.1 -->

One notes that the preceding reasoning proves that if `f` is a monomorphism, then, for every `y ∈ Y`, `f⁻¹(y)` is empty
or `k(y)`-isomorphic to `Spec(k(y))`.

**Proposition (8.11.6).**

<!-- label: IV.8.11.6 -->

*If a morphism `f : X → Y` of finite presentation is a universal homeomorphism, it is finite, surjective and radicial
(the converse being true by `(2.4.5, (iv))`).*

Indeed, `f` being of finite type, universally closed, and separated by virtue of `(2.4.4)`, is proper by definition
`(II, 5.4.1)`. Since it is obviously quasi-finite `(II, 6.2.3)`, it is finite by `(8.11.1)`. One knows moreover that it
is radicial `(2.4.4)`, and obviously surjective.

### 8.12. New demonstration and generalization of Zariski's *Main Theorem*.

**Lemma (8.12.1).**

<!-- label: IV.8.12.1 -->

*Let `f : X → Y` be a quasi-compact and quasi-separated morphism, `𝒞` a quasi-coherent `𝒪_Y`-Algebra, `Z = Spec(𝒞)`,
which is a `Y`-prescheme affine over `Y`. Let `g : X → Z` be a `Y`-morphism, `φ = 𝒜(g) : 𝒞 → f_*(𝒪_X)` the corresponding
`𝒪_Y`-homomorphism of `𝒪_Y`-Algebras `(II, 1.2.7)`. Suppose that `g` is an immersion. Then, in order that the closed
image of `X` under `g` `(I, 9.5.3)` be equal to `Z`, it is necessary and sufficient that `φ` be injective; `g` is then
an open immersion.*

The hypothesis entails that `f_*(𝒪_X)` is a quasi-coherent `𝒪_Y`-Algebra `(1.7.5)`; moreover, since the canonical
morphism `h : Z → Y` is affine, hence quasi-compact and separated, `g` is a quasi-compact and quasi-separated morphism
`(1.2.2` and `1.1.2)`, hence `g_*(𝒪_X)` is a quasi-coherent `𝒪_Z`-Algebra `(1.7.5)`. This being so, to say that the
closed image of `X` under `g` is equal to `Z` signifies `(I, 9.5.2)` that the canonical homomorphism
`θ : 𝒪_Z → g_*(𝒪_X)` is injective. But one has `h_*(𝒪_Z) = 𝒞` by definition of `Z` `(II, 1.3.1)`, and
`h_*(g_*(𝒪_X)) = f_*(𝒪_X)`. Since `Z` is affine over `Y`, it comes to the same thing to say that the homomorphism
`θ : 𝒪_Z → g_*(𝒪_X)` is injective or that the corresponding homomorphism `φ = h_*(θ) : 𝒞 → f_*(𝒪_X)` is injective
`(I, 1.3.9)`. The fact that `g` is then an open immersion results from `(I, 9.5.10)` and the hypothesis that `g` is an
immersion.

**Lemma (8.12.2).**

<!-- label: IV.8.12.2 -->

*Let `Y` be a quasi-compact and quasi-separated prescheme, `f : X → Y` a quasi-separated morphism of finite type, `𝒞` a
quasi-coherent `𝒪_Y`-Algebra, `Z = Spec(𝒞)`. Let `g : X → Z` be a `Y`-morphism, `φ : 𝒞 → f_*(𝒪_X)` the corresponding
`𝒪_Y`-homomorphism of `𝒪_Y`-Algebras. Let `(𝒞_λ)` be the increasing filtered family of quasi-coherent sub-`𝒪_Y`-Algebras
of finite type of `𝒞` (of which `𝒞` is the union `((I, 9.6.6)` and `(1.7.9))`); set `Z_λ = Spec(𝒞_λ)` and let `g_λ` be
the composite morphism `X → Z → Z_λ`. Then the following conditions are equivalent:*

*a) `g` is an immersion.*

*b) There exists `λ` such that `g_λ` is an immersion.*

<!-- original page 44 -->

*Moreover, when `g_λ` is an immersion, so is `g_μ` for `μ ≥ λ`.*

It suffices to apply `(II, 3.8.4)` after replacing `ℒ` by `𝒪_X` and `𝒜` by `𝒞[T]`, and taking into account
`(II, 3.1.7)`.

**Proposition (8.12.3).**

<!-- label: IV.8.12.3 -->

*Let `Y` be a quasi-compact and quasi-separated prescheme, `f : X → Y` a separated morphism of finite type. Let
`ℬ = f_*(𝒪_X)`, which is a quasi-coherent `𝒪_Y`-Algebra `(I, 9.2.2)`; let `𝒞` be the integral closure of `𝒪_Y` in `ℬ`,
which is a quasi-coherent `𝒪_Y`-Algebra `(II, 6.3.4)`; set `Z = Spec(𝒞)`, and let `g : X → Z` be the `Y`-morphism
corresponding to the canonical injection `φ : 𝒞 → ℬ = f_*(𝒪_X)` `(II, 1.2.7)`. Let `(𝒞_λ)` be the increasing filtered
family of quasi-coherent sub-`𝒪_Y`-Algebras of finite type of `𝒞` (of which `𝒞` is the union `((I, 9.6.6)` and
`(1.7.9))`), and, for every `λ`, let `g_λ : X → Z_λ = Spec(𝒞_λ)` be the `Y`-morphism corresponding to the injection
`𝒞_λ → ℬ = f_*(𝒪_X)`. Then the following conditions are equivalent:*

*a) There exists a factorization of `f` as*

```text
                                    f'        u
                                X ───→ Y' ───→ Y
```

*where `f'` is an immersion and `u` a finite morphism.*

*a') There exists a factorization `X →^{f'} Y' →^u Y` of `f`, where `f'` is an open immersion and `u` a finite
morphism.*

*b) The morphism `g : X → Z` is an immersion.*

*c) There exists `λ` such that `g_λ : X → Z_λ` is an immersion.*

*Moreover, when this is so, `g` is an open immersion, `g(X)` is dense in `Z`, and there exists `λ` such that, for
`μ ≥ λ`, `g_μ` is an open immersion.*

Since the homomorphism `φ : 𝒞 → f_*(𝒪_X)` is injective, it follows from `(8.12.1)` that if `g` is an immersion, it is an
open immersion and `g(X)` is dense in `Z`, and likewise for `g_λ`. The fact that a) implies a') also follows from
`(8.12.1)`, applied with `Z` replaced by `Y'` and `g` by `f'` (`Y'` being finite, hence affine over `Y`): indeed, if
`Y''` is the closed image of `X` under `f'`, `Y''` is finite over `Y` and `f'` factors as `X →^{f''} Y'' →^j Y'`, where
`j` is the canonical injection, and `f''` is an immersion `(I, 4.1.10)`; it then follows from `(8.12.1)` that `f''` is
an open immersion.

The equivalence of b) and c) follows from `(8.12.2)`, as does the fact that `g_λ` is then an immersion for `λ` large
enough. It is clear that c) implies a), since `Z_λ` is finite over `Y` `(II, 6.3.4` and `6.1.2)`. Finally let us show
that a) implies c). One saw above that one can suppose that `Y'` is the closed image of `X` under `f'`, and it then
follows from `(8.12.1)` that, setting `ℬ' = u_*(𝒪_{Y'})`, so that `Y'` identifies with `Spec(ℬ')`, the homomorphism
`φ' : ℬ' → ℬ = f_*(𝒪_X)` is injective. But since by hypothesis `ℬ'` is a finite `𝒪_Y`-Algebra, it identifies by
definition of `ℬ` with one of the sub-`𝒪_Y`-Algebras `𝒞_λ`, which proves c).

We say that a morphism `f : X → Y`, where `Y` is quasi-compact and quasi-separated, is *pseudo-finite* if it is of
finite type and satisfies condition a) of `(8.12.3)` (in which case it is necessarily separated).

**Corollary (8.12.4).**

<!-- label: IV.8.12.4 -->

*Let `Y` be a quasi-compact and quasi-separated prescheme, `f : X → Y` a morphism.*

<!-- original page 45 -->

*(i) Suppose `f` pseudo-finite. Then, for every morphism `Y' → Y`, where `Y'` is quasi-compact and quasi-separated,
`f_{(Y')} : X' = X_{(Y')} → Y'` is pseudo-finite.*

*(ii) Let `(U_λ)` be a cover of `Y` formed of quasi-compact opens. In order that `f` be pseudo-finite, it is necessary
and sufficient that for every `λ`, the restriction `f_λ : f⁻¹(U_λ) → U_λ` of `f` be a pseudo-finite morphism.*

*(iii) Suppose moreover `Y` Noetherian, and `f` of finite type. Then, in order that `f` be pseudo-finite, it is
necessary and sufficient that, for every `y ∈ Y`, the morphism `f_y = f × 1 : X_y = X ×_Y Spec(𝒪_y) → Spec(𝒪_y)` be so.*

(i) It is clear that `f_{(Y')}` is of finite type `(1.5.4)`; moreover, a factorization `X →^{f'} Z →^u Y` where `g` is
an immersion and `u` is finite, gives a factorization `X' → Z' → Y'` of `f_{(Y')}`, where `Z' = Z_{(Y')}`,
`g' = g_{(Y')}` and `u' = u_{(Y')}`; `g'` is an immersion `(I, 4.3.2)` and `u'` is finite `(II, 6.1.5)`; hence
`f_{(Y')}` is pseudo-finite.

(ii) The condition is necessary by virtue of (i), the `U_λ` being quasi-separated since `Y` is. To see that it is
sufficient, observe (with the notation of `(8.12.3)`) that if one sets `X_λ = f⁻¹(U_λ)`, one has
`ℬ|U_λ = (f_λ)_*(𝒪_{X_λ})`, `𝒞|U_λ` is the integral closure of `𝒪_{U_λ}` in `ℬ|U_λ`, and consequently, if `h : Z → Y` is
the canonical morphism, `Z_λ' = Spec(𝒞|U_λ)` identifies with `h⁻¹(U_λ)`. Now, in order that `g : X → Z` be an immersion,
it is necessary and sufficient that for every `λ`, the restriction `g_λ : f⁻¹(U_λ) → h⁻¹(U_λ)` of `g` be so
`(I, 4.2.4)`. This entails the conclusion by virtue of `(8.12.3)`.

(iii) It suffices, by virtue of (ii), to prove that `y` admits a neighbourhood `U` such that the restriction
`f⁻¹(U) → U` of `f` is a pseudo-finite morphism. Denote by `(U_λ)` the decreasing filtered projective system of affine
open neighbourhoods of `y`, and apply the method of `(8.1.2, a))`. Since `Y` is Noetherian, the restrictions
`f_λ : f⁻¹(U_λ) → U_λ` of `f` are of finite presentation, and so is `f_y`. By hypothesis `f_y` factors as
`X_y →^{g_y} Z_y →^{u_y} Spec(𝒪_y)`, where `u_y` is finite and `g_y` is an immersion. Since `𝒪_y` is Noetherian, so is
`Z_y`, and since `Z_y` is of finite presentation over `Spec(𝒪_y)`, there exist a `λ` and a morphism of finite
presentation `u_λ : Z_λ → U_λ` such that `Z_y` identifies with `Z_λ ×_{U_λ} Spec(𝒪_y)` and `u_y` with `u_λ × 1`
`(8.8.2, (ii))`; moreover, there exists a morphism `g_λ : X_λ → Z_λ` such that `g_y = g_λ × 1` and `f_λ = u_λ ∘ g_λ`
`(8.8.2, (i))`. Moreover, one can suppose `λ` chosen so that `g_λ` is an immersion and `u_λ` a finite morphism
`(8.10.5, (ii)` and `(x))`, which proves that `f_λ` is pseudo-finite.

**(8.12.5)**

<!-- label: IV.8.12.5 -->

We can now give of Zariski's *Main Theorem* `(III, 4.4.3)` a demonstration not using the cohomological results of
"global" nature of chap. III, but appealing on the other hand to the finer properties of Noetherian local rings; we
shall moreover generalize the statement of the theorem by ridding it of Noetherian hypotheses:

**Theorem (8.12.6) (Zariski's *Main Theorem*).**

<!-- label: IV.8.12.6 -->

*Let `Y` be a quasi-compact and quasi-separated prescheme. If a morphism `f : X → Y` is quasi-finite, separated and of
finite presentation, there exists a factorization of `f`*

```text
(8.12.6.1)                          X ──f'──→ Y' ──u──→ Y
```

*where `f'` is an open immersion and `u` a finite morphism.*

<!-- original page 46 -->

By virtue of `(8.12.4, (ii))` and of the local character (on `Y`) of the notions of quasi-finite, separated and finite
presentation morphisms, one may restrict to the case where `Y = Spec(A)` is affine. Applying `(8.9.1)`, one may suppose
that there is a sub-ring `A_0` of `A`, which is a `Z`-algebra of finite type, and an `A`-isomorphism
`X_0 ⊗_{A_0} A ⥲ X`, `f` being identified by this isomorphism with `f_0 × 1`, where `f_0 : X_0 → Spec(A_0)` is a
morphism of finite type; moreover `(8.10.5, (v)` and `(xi))` one may suppose that `f_0` is separated and quasi-finite;
if one proves that `f_0` is pseudo-finite, so will `f` be by `(8.12.4, (i))`. Since `A_0` is then Noetherian and the
notions of morphism of finite type, separated and quasi-finite are preserved by base change, it follows from
`(8.12.4, (iii))` that one may even suppose that `A` is a local ring, essentially of finite type over `Z` `(1.3.8)`. Set
`n = dim(A)`, and proceed by induction on `n`; for `n = 0`, the theorem is evident, `A` being a field and the morphism
`f` being already finite `(II, 6.2.2)`. Set `B = Γ(X, 𝒪_X)`; denote by `C` the integral closure of `A` in `B`, set
`Z = Spec(C)` and let `g : X → Z` be the `Y`-morphism corresponding to the canonical injective `A`-homomorphism `C → B`;
by virtue of `(8.12.3)`, it remains to show that `g` is an open immersion. Let `a` be the closed point of `Y`, and let
`U = Y − {a}`; `U` is Noetherian and all its local rings are essentially of finite type over `Z` and of dimension `< n`;
taking into account the induction hypothesis, and `(8.12.4, (iii))`, one sees that the restriction `f⁻¹(U) → U` of `f`
is a pseudo-finite morphism. One concludes `(8.12.3)` that, if `h : Z → Y` is the structure morphism, the restriction
`f⁻¹(U) → h⁻¹(U)` of `g` is an open immersion. Set `A' = Â`, `Y' = Spec(A')`, `X' = X_{(Y')}`,
`f' = f_{(Y')} : X' → Y'`. Since the canonical morphism `u : Y' → Y` is flat, it follows from `(2.3.1)` that
`B' = Γ(X', 𝒪_{X'})` identifies with the `A'`-algebra `B ⊗_A A'`. On the other hand, since `A` is an excellent local
ring `(7.8.3)`, the morphism `u : Y' → Y` is regular, and a fortiori normal, and consequently `(6.14.4)` the integral
closure of `A'` in `B'` is equal to `C' = C ⊗_A A'`. One sees therefore that `Z' = Spec(C')` is equal to `Z_{(Y')}` and
the morphism `g' : X' → Z'` coming from the injection `C' → B'` is equal to `g_{(Y')}`. Since `u : Y' → Y` is faithfully
flat and quasi-compact, to prove that `g` is an open immersion, it suffices to prove that `g'` is an open immersion
`(2.7.1, (x))`. Note now that `u⁻¹(a)` is reduced to the closed point `a'` of `Y'` and consequently
`U' = Y' − {a'} = u⁻¹(U)`. If `h' : Z' → Y'` is the canonical morphism, the fact that the restriction `f⁻¹(U) → h⁻¹(U)`
of `g` is an open immersion entails that this is also so of the restriction `f'⁻¹(U') → h'⁻¹(U')` of `g'`. Note now that
`f'` is a separated and quasi-finite morphism `(II, 6.2.4)`; since `A'` is complete, one deduces from `(II, 6.2.6)` that
`X'` is `Y'`-isomorphic to a sum `X_1' ⊔ X_2'`, where the restriction `f'|X_1' = f_1' : X_1' → Y'` is a finite morphism,
and `X_2' ⊂ f'⁻¹(U')`. It follows that `B'` is direct composition of the two `A'`-algebras `Γ(X_1', 𝒪_{X_1'}) = B_1'`
and `Γ(X_2', 𝒪_{X_2'}) = B_2'`; one concludes at once that the integral closure `C'` of `A'` in `B'` is direct
composition of the integral closures `C_1'`, `C_2'` of `A'` in `B_1'`, `B_2'` respectively, whence `Z' = Z_1' ⊔ Z_2'`,
where `Z_i' = Spec(C_i')` `(i = 1, 2)`; and the canonical morphism `g' : X' → Z'` is such that `g'|X_i'` is the
canonical morphism `g_i' : X_i' → Z_i'` `(i = 1, 2)`. But since `B_1'` is already a finite `A'`-algebra, one has
`C_1' = B_1'`, and `g_1'` is therefore an isomorphism. On the other hand, since `X_2' ⊂ f'⁻¹(U')` and is open in
`f'⁻¹(U')`, one knows

<!-- original page 47 -->

already that `g_2'` is an open immersion. One concludes indeed that `g'` is an open immersion, Q.E.D.

**Remark (8.12.7).**

<!-- label: IV.8.12.7 -->

When, in `(8.12.6)`, one supposes that `Y` is an affine scheme, the demonstration by reduction to the Noetherian case
shows that, in the factorization `(8.12.6.1)`, the morphisms `f'` and `u` are also morphisms of finite presentation
`(1.6.2)`.

**Corollary (8.12.8).**

<!-- label: IV.8.12.8 -->

*Let `Y` be a quasi-compact scheme such that there exists an ample `𝒪_Y`-Module `(II, 4.5.3)`, `f : X → Y` a
quasi-finite and quasi-projective morphism. Then there exists a factorization of `f` as*

```text
                                X ──f'──→ Y' ──u──→ Y
```

*where `f'` is an open immersion and `u` a finite morphism.*

The hypothesis entails that `X` identifies with a quasi-compact sub-`Y`-scheme of a `Y`-scheme of the form `Z = ℙ_Y^r`
`(II, 5.3.3)`. There is consequently a quasi-compact open neighbourhood `U` of `X` in `Z` such that `X` is closed in
`U`; since `Z` is a scheme, the canonical injection `U → Z` is a morphism of finite presentation `((1.2.7)` and
`(1.6.2))`, hence the composite morphism `g : U → Z → Y` is also a morphism of finite presentation (the fact that
`ℙ_Y^r` is of finite presentation over `Y` resulting at once from the definition `(II, 4.1.1)`). Let `ℐ` be the
quasi-coherent Ideal of `𝒪_U` defining the closed sub-prescheme `X`; since `U` is a quasi-compact scheme, `ℐ` is the
filtered inductive limit of its quasi-coherent sub-Ideals of finite type `ℐ_λ` `(I, 9.4.9)`. If `X_λ` is the closed
sub-prescheme of `U` defined by `ℐ_λ`, one has consequently `X = ⋂ X_λ`. For every `y ∈ Y`, one therefore has
`f⁻¹(y) = ⋂ (X_λ ∩ g⁻¹(y))`, and since the sets `X_λ ∩ g⁻¹(y)` are closed in the Noetherian space `g⁻¹(y)`, there exists
for every `y` an index `λ(y)` such that `f⁻¹(y) = X_{λ(y)} ∩ g⁻¹(y)`. Denote by `E_λ` the set of `y ∈ Y` such that the
fibre `X_λ ∩ g⁻¹(y)` of the restriction of `g` to `X_λ` is a finite `k(y)`-prescheme. The hypothesis that `f` is
quasi-finite entails, by virtue of what precedes, that `Y = ⋃ E_λ`. Now, each of the `X_λ` is, by definition, of finite
presentation over `Y`; it therefore follows from `(9.2.3)` and `(9.2.6)` (\*) that the `E_λ` are constructible sets in
the scheme `Y`; since they form an increasing filtered family, there exists an index `λ` such that `E_λ = Y` `(1.9.9)`,
and for this index `λ`, the morphism `f_λ : X_λ → Y`, restriction of `g` to `X_λ`, is therefore quasi-finite. Since it
is of finite presentation and separated, one may apply `(8.12.6)` to it, and `f_λ` factors therefore as

```text
                                X_λ ──j_λ──→ Y_λ ──u_λ──→ Y
```

where `j_λ` is an immersion and `u_λ` a finite morphism. Since `X` is a closed sub-prescheme of `X_λ`, one has thus
proved that `f` has property `(8.12.3, a))`, whence the corollary by virtue of the equivalence of `(8.12.3, a))` and
`(8.12.3, a'))`.

The reader will verify that the corollaries `(8.12.8)` to `(8.12.11)` are not used in §9.

<!-- original page 48 -->

**Corollary (8.12.9).**

<!-- label: IV.8.12.9 -->

*Let `f : X → Y` be a locally quasi-finite morphism (Errm, 20). For every `x ∈ X` there exists an open neighbourhood `U`
of `x` in `X`, an open neighbourhood `V` of `y = f(x)` in `Y`, such that `f(U) ⊂ V` and a factorization*

```text
                                U ──f'──→ V' ──u──→ V
```

*of the restriction of `f` to `U`, where `f'` is an open immersion and `u` a finite morphism.*

It obviously suffices to take for `V` an affine neighbourhood of `y` in `Y`, for `U` an affine neighbourhood of `x` in
`X` contained in `f⁻¹(V)` and such that `f|U` is quasi-finite. The morphism `U → V` restriction of `f` being then affine
(hence quasi-projective), one may apply `(8.12.8)` to it.

**Corollary (8.12.10).**

<!-- label: IV.8.12.10 -->

*Let `Y` be an integral and normal prescheme, `X` an integral prescheme, `f : X → Y` a birational and locally
quasi-finite morphism (Errm, 20). Then `f` is a local isomorphism; in order that `f` be an open immersion, it is
necessary and sufficient that `f` be moreover separated.*

The second assertion results at once from the first and from `(I, 8.2.8)`. To prove the first assertion, one may suppose
`X` and `Y` affine and `f` quasi-finite; consider the factorization `f = u ∘ f'` of `(8.12.8)`, which permits to
identify `X` by `f'` with a sub-prescheme induced on an open of `Y'`. Since `X` is integral, one may, by virtue of
`(I, 5.2.3)`, replace `Y'` by the reduced sub-prescheme of `Y'` having `X` as underlying space, hence one may also
suppose that `Y'` is integral. Moreover, since `f` is birational, so is `u`. The conclusion results then from the
following lemma:

**Lemma (8.12.10.1).**

<!-- label: IV.8.12.10.1 -->

*Let `Y'` be an integral prescheme, `Y` an integral and normal prescheme; then a finite and birational morphism
`u : Y' → Y` is an isomorphism.*

Set indeed `𝒜 = u_*(𝒪_{Y'})`, so that `𝒜` is a finite `𝒪_Y`-Algebra, `Y'` identifying with `Spec(𝒜)` `(II, 1.3.6)`. If
`R(Y)` is the field of rational functions of `Y`, one has therefore, for every `y ∈ Y`, `𝒪_y ⊂ 𝒜_y ⊂ R(Y)`; but since
the ring `𝒪_y` is by hypothesis integrally closed and has `R(Y)` as field of fractions, one necessarily has `𝒜_y = 𝒪_y`,
whence the lemma.

**Corollary (8.12.11).**

<!-- label: IV.8.12.11 -->

*Let `Y` be an integral prescheme, `X` an integral and normal prescheme, `f : X → Y` a dominant and locally quasi-finite
morphism. Let `K` and `L` (extension of `K`) be the fields of rational functions of `Y` and `X` respectively, and let
`Y'` be the integral closure of `Y` relative to `L` `(II, 6.3.4)`; then `f` factors in a unique way as
`f : X →^{f'} Y' →^u Y`, where `f'` is birational, and corresponds to the identity automorphism of `L`; `f'` is then a
local isomorphism, and in order that `f'` be an open immersion, it is necessary and sufficient that `f` be separated.*

The existence and uniqueness of the factorization of `f` result from `(II, 6.3.9)`. It follows from `(II, 6.2.4, (v))`,
by reducing to the affine case, that `f'` is locally quasi-finite; moreover, it follows from `(I, 5.5.1)` that, in order
that `f'` be separated, it is necessary and sufficient that `f` be so, since `u` is affine, hence separated; the last
two assertions are therefore consequences of `(8.12.10)` applied to `f'`.

<!-- original page 49 -->

### 8.13. Translation in terms of pro-objects.

The following proposition is essentially equivalent to `(8.8.2, (i))`:

**Proposition (8.13.1).**

<!-- label: IV.8.13.1 -->

*Let `S` be a prescheme, `(X_λ, v_{λμ})` a filtered projective system of `S`-preschemes; suppose there exists `α` such
that `v_{αλ}` is an affine morphism for every `λ ≥ α` (which entails `(II, 1.6.2)` that `v_{λμ}` is affine for
`α ≤ λ ≤ μ`), so that the projective limit `X = lim X_λ` exists in the category of `S`-preschemes `(8.2.3)`. Let `Y` be
an `S`-prescheme, and, for every `λ ≥ α`, let `θ_λ : Hom_S(X_λ, Y) → Hom_S(X, Y)` be the application which, to every
`S`-morphism `f_λ : X_λ → Y`, makes correspond `f = f_λ ∘ v_λ`, where `v_λ : X → X_λ` is the canonical morphism. The
family `(θ_λ)` is an inductive system of applications, which therefore defines a canonical application*

```text
(8.13.1.1)                lim Hom_S(X_λ, Y) → Hom_S(X, Y).
```

*Suppose `X_α` quasi-compact (resp. quasi-compact and quasi-separated), and the structure morphism `Y → S` locally of
finite type (resp. locally of finite presentation). Then the application `(8.13.1.1)` is injective (resp. bijective).*

Set indeed, for `λ ≥ α`, `Z_λ = Y ×_S X_λ`, so that one has `Z_λ = Z_α ×_{X_α} X_λ`. Set likewise
`Z = Y ×_S X = Z_α ×_{X_α} X`; one then knows `(8.2.5)` that, if one also sets `w_{λμ} = 1 × v_{λμ} : Z_μ → Z_λ` for
`α ≤ λ ≤ μ` and `w_λ = 1 × v_λ : Z → Z_λ` for `α ≤ λ`, `Z` is projective limit of the projective system `(Z_λ, w_{λμ})`
and the `w_λ` are the corresponding canonical morphisms. Note on the other hand that the morphism `Z_α → X_α` is locally
of finite type (resp. locally of finite presentation) `(1.3.4` and `1.4.3)`. Finally, one knows that one has

```text
            Hom_S(X_λ, Y) = Hom_{X_λ}(X_λ, Z_λ)    and    Hom_S(X, Y) = Hom_X(X, Z)
```

`(I, 3.3.14)`. It now suffices to apply `(8.8.2, (i))` taking `X_λ = S_λ` and replacing `Y_λ` by `Z_λ`.

**Corollary (8.13.2).**

<!-- label: IV.8.13.2 -->

*With the notation of `(8.13.1)`, suppose `X_α` quasi-compact and quasi-separated, and the `v_{αλ}` affine for `α ≤ λ`;
suppose moreover that `Y = lim Y_ρ`, where `(Y_ρ, t_{ρσ})` is a filtered projective system of `S`-preschemes such that,
for each `ρ`, the structure morphism `Y_ρ → S` is locally of finite presentation. One then has a canonical bijection*

```text
(8.13.2.1)              Hom_S(X, Y) ⥲ lim_ρ (lim_λ Hom_S(X_λ, Y_ρ)).
```

Indeed, the fact that `Y` is projective limit of the `Y_ρ` entails in particular that the canonical application
`Hom_S(X, Y) → lim_ρ Hom_S(X, Y_ρ)` is bijective; and on the other hand, the hypotheses entail, for each `ρ`, the
existence of a canonical bijection `Hom_S(X, Y_ρ) ⥲ lim_λ Hom_S(X_λ, Y_ρ)` by virtue of `(8.13.1)`; whence the
conclusion.

**(8.13.3)**

<!-- label: IV.8.13.3 -->

The preceding results allow one to interpret in the theory of preschemes the notions of "pro-variety" or "pro-scheme"
that intervene in certain applications (for example in the theory of the local class field according to the ideas of
Serre [39] or in Néron's theory of the reduction of abelian

<!-- original page 50 -->

varieties [32]). Let us recall rapidly here the notion of pro-object of a category, referring to chap. V for fuller
developments (we shall moreover not use before chap. V the interpretation that follows, and the reader may therefore
omit until then the reading of the end of this number). Given a category `𝓒`, the category `Pro(𝓒)` of pro-objects of
`𝓒` has as objects the projective systems (in the universe in which one places oneself) `X = (X_μ)_{μ ∈ M}` of objects
of `𝓒` whose index sets (depending on the projective system considered) are assumed pre-ordered filtered. Given two such
pro-objects `X = (X_μ)_{μ ∈ M}`, `X' = (X_{μ'}')_{μ' ∈ M'}`, the morphisms from `X` to `X'` are by definition the
elements of the set `lim_{μ'}(lim_μ Hom(X_μ, X_{μ'}'))`; the verification of the fact that one may take these sets for
sets of morphisms is immediate, the composition of systems of morphisms `u_{μ'}^μ : X_μ → X_{μ'}'`,
`u_{μ''}^{μ'} : X_{μ'}' → X_{μ''}''`, which are inductive in the upper index and projective in the lower index, being
done "argument by argument", in other words by considering the system of the `u_{μ''}^μ = u_{μ''}^{μ'} ∘ u_{μ'}^μ`.

**(8.13.4)**

<!-- label: IV.8.13.4 -->

Consider then a quasi-compact and quasi-separated prescheme `S`, and denote by `𝓒` the full sub-category of the category
`(Sch)_{/S}` of `S`-preschemes formed by the `S`-preschemes `X` having the following property: the structure morphism
`X → S` factors as `X →^g X_0 →^f S`, where `g : X → X_0` is affine and `f : X_0 → S` of finite presentation; we say for
brevity that the preschemes of `𝓒` are *essentially affine* over `S`.

Consider on the other hand the full sub-category `𝓒_0'` of `(Sch)_{/S}` formed by the `S`-preschemes of finite
presentation, and the category `Pro(𝓒_0')` of pro-objects of `𝓒_0'`. We say that an object `X = (X_μ)_{μ ∈ M}` of
`Pro(𝓒_0')` is *essentially affine* if there exists `γ ∈ M` such that for every `μ ≥ γ`, the transition morphism
`v_{γμ} : X_μ → X_γ` is affine (which entails that for `γ ≤ μ ≤ ν`, `v_{μν} : X_ν → X_μ` is affine). One notes that an
object of `Pro(𝓒_0')` isomorphic to an essentially affine object is not necessarily essentially affine itself. We shall
denote by `𝓒'` the full sub-category of `Pro(𝓒_0')` formed by the essentially affine pro-objects of `𝓒_0'`.

This being so, it follows from `(8.2.2)` and `(8.2.3)` that for every object `X = (X_μ)_{μ ∈ M}` of `𝓒'`, the
`S`-prescheme `X = lim X_μ` exists; moreover, since, for `μ` large enough, the morphism `X → X_μ` is affine `(8.2.2)`,
`X` is essentially affine over `S` by definition. Set `X = L(X)`; let us show that one has thus defined a *canonical
functor*

```text
(8.13.4.1)                                  L : 𝓒' → 𝓒.
```

One has in effect, for two objects `X = (X_μ)`, `X' = (X_{μ'}')` of `𝓒'`, a canonical application for each `μ'`

```text
                       lim_μ Hom_S(X_μ, X_{μ'}') → Hom_S(lim X_μ, X_{μ'}')
```

defined in `(8.13.1.1)`, and on the other hand, by definition of the projective limit, a canonical bijection

```text
                lim_{μ'} Hom_S(lim X_μ, X_{μ'}') ⥲ Hom_S(lim X_μ, lim X_{μ'}')
```

<!-- original page 51 -->

whence a canonical application

```text
(8.13.4.2)        lim_{μ'}(lim_μ Hom_S(X_μ, X_{μ'}')) → Hom(lim X_μ, lim X_{μ'}')
```

obviously functorial in `X` and `X'`, and which completes the definition of the functor `L`.

**Proposition (8.13.5).**

<!-- label: IV.8.13.5 -->

*The hypotheses and notation being those of `(8.13.4)`, the functor `L` is fully faithful. If moreover `S` is a
Noetherian prescheme (which already implies that `S` is quasi-compact and quasi-separated `(1.2.8)`), `L` is an
equivalence of categories.*

To say that `L` is fully faithful means that the application `(8.13.4.2)` is bijective for every `X`, `X'` in `𝓒'`,
which is a particular case of `(8.13.2)`: indeed, the structure morphisms `X_μ → S` being of finite presentation, are in
particular quasi-compact and quasi-separated, hence the `X_μ` are quasi-compact and quasi-separated.

To show that when `S` is Noetherian `L` is an equivalence of categories, it suffices, since one already knows that `L`
is fully faithful, to prove that every essentially affine `S`-prescheme `X` is `S`-isomorphic to an object of the form
`L(X)` where `X ∈ 𝓒'` `(0_III, 8.1.5)`. Now, by hypothesis there is a factorization `X →^g X_0 →^f S` of the structure
morphism, `f` being of finite presentation and `g` affine. One may therefore write `X = Spec(𝒜)`, where `𝒜` is a
quasi-coherent `𝒪_{X_0}`-Algebra `(II, 1.3.1)`. Now, since `X_0` is Noetherian (since this is so for `S` and `f` is of
finite type), `𝒜` is the filtered inductive limit of the family `(𝒜_λ)` of its quasi-coherent sub-`𝒪_{X_0}`- Algebras of
finite type `(I, 9.6.6)`. Set `X_λ = Spec(𝒜_λ)`; the morphisms `X_λ → X_0` are of finite type, hence of finite
presentation since `X_0` is Noetherian, and consequently so are the composite morphisms `X_λ → X_0 → S` `(1.6.2)`; in
other words, the `X_λ` belong to `𝓒_0'`, and since the morphisms `X_λ → X_0` are affine, `X = (X_λ)` is an object of
`𝓒'` whose projective limit exists and is `S`-isomorphic to `X` by virtue of `(8.2.2)`. This finishes the demonstration.

**Remark (8.13.6).**

<!-- label: IV.8.13.6 -->

It follows from `(1.6.2)` and from `(II, 1.6.2)` that if `X` and `Y` are essentially affine over `S`, then so is
`X ×_S Y`. One concludes for example `(0_III, 8.2.5)` that a `𝓒`-group is nothing other than a `(Sch)_{/S}`-group which
is an essentially affine prescheme over `S`. On the other hand, finite products exist in the category `𝓒'`: indeed, if
`X = (X_μ)_{μ ∈ M}`, `Y = (Y_ρ)_{ρ ∈ R}` are two objects of `𝓒'`, the products `X_μ ×_S Y_ρ` are `S`-preschemes of
finite presentation, and taking for transition morphisms `X_ν ×_S Y_σ → X_μ ×_S Y_ρ` the products of the transition
morphisms `X_ν → X_μ` and `Y_σ → Y_ρ`, one sees at once that `(X_μ ×_S Y_ρ)` is the product of `X` and `Y` in
`Pro(𝓒_0')`; moreover `(II, 1.6.2)` the transition morphisms thus defined are affine for `μ` and `ρ` large enough, hence
the product `X × Y` thus defined belongs indeed to `𝓒'`. One concludes then as above that a `𝓒'`-group is a
`Pro(𝓒_0')`-group which is essentially affine. One deduces therefore from `(8.13.5)` that the categories of `𝓒'`-groups
and of `𝓒`-groups are equivalent when `S` is Noetherian. It seems plausible that when `S` is the spectrum of a field
`k`, the category of `𝓒`-groups is equivalent to that of `𝓚`-groups, where `𝓚` is the category of quasi-compact
`S`-preschemes; in other words, every group prescheme over `k` that is quasi-compact would be essentially affine. On the
other hand, if one denotes

<!-- original page 52 -->

by `𝓒_0'-gr` the category of `𝓒_0'`-groups, it is plausible that the category of `𝓒'`-groups is equivalent to the full
sub-category of `Pro(𝓒_0'-gr)` formed by the "essentially affine pro-algebraic groups", that is to say the projective
systems `G = (G_μ)_{μ ∈ M}`, where the `G_μ` are algebraic groups over `k` and the transition morphisms `G_ν → G_μ` are
affine for `μ` large enough (which one may also express by saying that `G` is an extension of an algebraic group by an
affine pro-algebraic group). The conjunction of these two conjectures is moreover equivalent to the following: every
group prescheme quasi-compact over `k` is an "extension" of an "algebraic group" (i.e. a group prescheme of finite type
over `k`) by an affine group prescheme over `k`.

The only pro-algebraic groups encountered in practice up to the present being in fact essentially affine, there will
therefore no doubt be advantage in substituting for the study of general pro-algebraic groups (introduced and studied by
Serre [40]) that of quasi-compact group schemes over `k`, whose definition is conceptually simpler.

### 8.14. Characterization of a prescheme locally of finite presentation over another, in terms of the functor it represents.

**(8.14.1)**

<!-- label: IV.8.14.1 -->

Given a prescheme `S`, we say again, as in `(8.13.4)`, that a filtered projective system `(X_λ, v_{λμ})` of
`S`-preschemes is *essentially affine* if there exists `α` such that `v_{αλ}` is an affine morphism for `λ ≥ α`.

The following statement, which will above all be useful in chap. V, makes `(8.8.2, (i))` more precise by furnishing a
converse:

**Proposition (8.14.2).**

<!-- label: IV.8.14.2 -->

*Let `S` be a prescheme, `f : X → S` a morphism. For every `S`-prescheme `T`, set*

```text
                                  h_X(T) = Hom_S(T, X)
```

*so that `h_X` is a contravariant functor from the category `(Sch)_{/S}` of `S`-preschemes to the category Ens of sets
`(0_III, 8.1.1)`, and `X` an object representing this functor `(0_III, 8.1.8)`. The following conditions are
equivalent:*

*a) `f` is locally of finite presentation.*

*b) For every filtered projective system `(Z_λ)` of `S`-preschemes, essentially affine `(8.13.4)` and formed of
quasi-compact and quasi-separated preschemes, the canonical application `(8.13.1.1)`*

```text
(8.14.2.1)                          lim h_X(Z_λ) → h_X(lim Z_λ)
```

*is bijective.*

*c) For every filtered projective system `(Z_λ)` of `S`-preschemes such that the `Z_λ` are affine schemes, the
application `(8.14.2.1)` is bijective.*

*c') For every affine open `U` of `S` and every filtered projective system `(Z_λ)` of `U`-preschemes such that the `Z_λ`
are affine schemes, the application `(8.14.2.1)` is bijective.*

The fact that a) implies b) is none other than `(8.13.1)`; it is trivial that b) implies c) and that c) implies c'). It
remains to see that c') entails a), and since property a) is local on `S`, one may restrict to the case where `S` is
affine.

<!-- original page 53 -->

Suppose first that `X` is also affine; the assertion to be proved is then equivalent to the

**Corollary (8.14.2.2).**

<!-- label: IV.8.14.2.2 -->

*Let `A` be a ring, `B` an `A`-algebra. In order that, for every filtered inductive system `(C_λ)` of `A`-algebras, the
canonical application*

```text
(8.14.2.3)             lim Hom_{A-alg.}(B, C_λ) → Hom_{A-alg.}(B, lim C_λ)
```

*be bijective, it is necessary and sufficient that `B` be an `A`-algebra of finite presentation.*

It remains only to show that the condition is necessary. Take first for `(C_λ)` the filtered inductive system of
sub-`A`-algebras of finite type of `B`, so that `lim C_λ = B`. The fact that `(8.14.2.3)` is bijective entails in
particular that the identity application `1_B` factors as `B → C_λ → B` for a suitable `λ`, which entails `C_λ = B`,
hence `B` is an `A`-algebra of finite type. Set then `B = C/𝔍`, where `C = A[T_1, …, T_n]` and `𝔍` is an ideal of `C`.
Then `𝔍` is the filtered inductive limit of the ideals of finite type `𝔍_λ ⊂ 𝔍` of `C`; setting `C_λ = C/𝔍_λ`, and using
the exactness of the functor `lim`, one sees that `B` is again isomorphic to the inductive limit of the filtered
inductive system `(C_λ)`. There exists therefore a `λ` and an `A`-homomorphism `u : B → C_λ` such that the composite
`B →^u C_λ →^{p_λ} B` (where `p_λ` is the canonical homomorphism) is the identity. Let `q_λ : C → C_λ` be the canonical
homomorphism, and set `t_i = p_λ(q_λ(T_i))`; one has therefore `p_λ(u(t_i)) = p_λ(q_λ(T_i))`, in other words
`u(t_i) − q_λ(T_i) ∈ 𝔍/𝔍_λ`. There exists therefore `μ ≥ λ` such that the `n` elements `u(t_i) − q_λ(T_i)` belong to
`𝔍_μ/𝔍_λ` `(1 ≤ i ≤ n)`; if `p_{λμ} : C_λ → C_μ` is the canonical homomorphism, one has consequently
`p_{λμ}(u(t_i)) = p_{λμ}(q_λ(T_i)) = q_μ(T_i)`. Replacing `λ` by `μ` and `u` by `p_{λμ} ∘ u`, one may therefore suppose
that `u(t_i) = q_λ(T_i)` for every `i`, and if `r = p_λ ∘ q_λ` is the canonical homomorphism `C → C/𝔍 = B`, one may
therefore write `u(r(T_i)) = q_λ(T_i)` for every `i`, whence `q_λ = u ∘ r`. But this entails necessarily that `𝔍 = 𝔍_λ`,
since if `z ∈ 𝔍`, one has `r(z) = 0`; hence one has `B = C_λ`.

Let us pass now to the case where `S` is affine and `X` arbitrary; everything comes down to proving that an affine open
`V` of `X` is of finite presentation over `S`, and by virtue of what has just been demonstrated, it suffices to prove
that for every filtered projective system `(Z_λ)` of affine `S`-preschemes, the application

```text
(8.14.2.4)                Hom_S(Z_λ, V) → Hom_S(lim Z_λ, V)
```

is bijective. It is immediate that this application is injective, for if `(v_λ)`, `(v_λ')` are two inductive systems of
`S`-homomorphisms `v_λ : Z_λ → V`, `v_λ' : Z_λ → V` such that the corresponding morphisms

```text
                 Z ──u_λ──→ Z_λ ──v_λ──→ V,        Z ──u_λ──→ Z_λ ──v_λ'──→ V
```

are equal (`u_λ` being the canonical morphism), then the morphisms

```text
              Z ──u_λ──→ Z_λ ──v_λ──→ V ──j──→ X,      Z ──u_λ──→ Z_λ ──v_λ'──→ V ──j──→ X
```

(where `j` is the canonical injection) are equal, which entails `j ∘ v_λ = j ∘ v_λ'` by hypothesis for a suitable `λ`,
hence `v_λ = v_λ'`.

<!-- original page 54 -->

It remains to prove that `(8.14.2.4)` is surjective. Let then `v : Z → V` be an `S`-morphism; by hypothesis there exist
a `λ` and an `S`-morphism `w_λ : Z_λ → X` such that `j ∘ v` factors as `Z →^{u_λ} Z_λ →^{w_λ} X`, and everything comes
down to proving that there exists `μ ≥ λ` such that the morphism

```text
                            Z_μ ──w_λ ∘ u_{λμ}──→ X
```

(where `u_{λμ}` is the transition morphism) factors as `Z_μ →^{v_μ} V →^j X`. Set, for every `λ`, `U_λ = w_λ⁻¹(V)`. One
has `u_λ⁻¹(U_λ) = u_λ⁻¹(U_λ) = w_λ⁻¹(j⁻¹(V)) = v⁻¹(V) = Z`. Since the `Z_λ` are quasi-compact and the `U_λ`, being open,
are ind-constructible `(1.9.6)`, one deduces from `(8.3.4)` that there exists `μ ≥ λ` such that `U_μ = Z_μ`. Q.E.D.

**Remark (8.14.3).**

<!-- label: IV.8.14.3 -->

The fact that the application `(8.14.2.1)` is injective when `f` is locally of finite type `(8.8.2, (i))` naturally
leads one to ask whether this result also admits a converse. There is nothing of the sort, even when `S` and `X` are
affine, since there exist monomorphisms `X → S` which are not of finite type `(I, 2.4.2)`, and which therefore put this
conjecture in default.
