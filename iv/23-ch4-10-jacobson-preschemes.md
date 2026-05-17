<!-- original page 95 -->

## §10. Jacobson preschemes

We have already had occasion to observe `(5.2.5)` that even excellent preschemes `(7.8.5)` do not always behave like the
"varieties" of classical algebraic geometry, particularly as regards questions of dimension; thus if `X` is the spectrum
of a complete discrete valuation ring, the set of closed points of `X` (reduced to a single element) is not everywhere
dense in `X`, and its complement (also reduced to a single element) is an open set everywhere dense in `X` but of
dimension zero, hence `< dim(X)`. In this section we examine general conditions under which such phenomena do not occur;
the result is a more satisfactory behaviour, in certain respects, for the relations between dimension, codimension,
depth and codepth in such preschemes `(10.6 and 10.8)`. Moreover, in the preschemes considered, the fact that the set of
closed points is everywhere dense (and even "very dense" `(10.1.3)`) makes it possible to consider only these points in
many proofs; one thus rejoins the classical viewpoint of "algebraic varieties" which, from our standpoint, are the sets
of closed points of algebraic preschemes over a field, and one connects the language of schemes with that of Serre's
"varieties" or "algebraic spaces" `(10.9 and 10.10)`.

### 10.1. Very dense subsets of a topological space

**(10.1.1)**

<!-- label: IV.10.1.1 -->

We say that a subset of a topological space `X` is *quasi-constructible* if it is a finite union of locally closed
subsets of `X`. We say that a subset `T` of `X` is *locally quasi-constructible* if for every `x ∈ X`, there exists an
open neighbourhood `V` of `x` such that `T ∩ V` is quasi-constructible in `V`. It is clear that every
quasi-constructible subset of `X` is locally quasi-constructible; the converse holds if `X` is quasi-compact. The
argument of `(0_III, 9.1.3)`, dropping the word "retrocompact", shows that the set of quasi-constructible (resp. locally
quasi-constructible) subsets of `X`, which we shall denote by `𝒬c(X)` (resp. `ℒ𝒬c(X)`), is stable under finite union,
finite intersection, and complementation. If `f : X → Y` is a continuous map, it follows immediately from these
definitions that for every quasi-constructible (resp. locally quasi-constructible) subset `Z` of `Y`, `f⁻¹(Z)` is
quasi-constructible (resp. locally quasi-constructible) in `X`.

The constructible (resp. locally constructible) subsets of `X` are obviously quasi-constructible (resp. locally
quasi-constructible); the converse holds when `X` is Noetherian (resp. locally Noetherian).

In what follows, we denote respectively by `𝒪(X)`, `𝔉(X)`, `ℒℱ(X)`, `ℭ(X)`, `ℒℭ(X)` the set of subsets of `X` which are
respectively open, closed, locally closed, constructible, locally constructible.

<!-- original page 96 -->

**Proposition (10.1.2).**

<!-- label: IV.10.1.2 -->

*Let `X` be a topological space, `X₀` a subset of `X`. The following conditions are equivalent:*

*a) For every locally closed subset `Z ≠ ∅` of `X`, one has `Z ∩ X₀ ≠ ∅`.*

*a') For every closed subset `Z` of `X`, one has `Z = ‾{Z ∩ X₀}`.*

*b) For every subset `Z ≠ ∅` of `X` that is locally quasi-constructible, one has `Z ∩ X₀ ≠ ∅`.*

*b') For every locally quasi-constructible subset `Z` of `X`, one has `Z ⊂ ‾{Z ∩ X₀}` (in other words, `Z ∩ X₀` is dense
in `Z`).*

*c) The map `U ↦ U ∩ X₀` from `𝒪(X)` to `𝒪(X₀)` is injective (hence bijective).*

*c') The map `F ↦ F ∩ X₀` from `𝔉(X)` to `𝔉(X₀)` is injective (hence bijective).*

*c'') The map `Z ↦ Z ∩ X₀` from `ℒℱ(X)` to `ℒℱ(X₀)` is injective (hence bijective).*

*c''') The map `Z ↦ Z ∩ X₀` from `ℒ𝒬c(X)` to `ℒ𝒬c(X₀)` is injective.*

*Moreover, when these conditions are satisfied, the map `Z ↦ Z ∩ X₀` from `ℒ𝒬c(X)` to `ℒ𝒬c(X₀)` is bijective.*

Note that the surjectivity assertions in c) and c') are trivial; they imply that every locally closed subset of `X₀` is
the trace on `X₀` of a locally closed subset of `X`, so the map `ℒℱ(X) → ℒℱ(X₀)` defined in c'') is also surjective.

We shall prove the implications

```text
  c''') ⟹ c'') ⟹ c') ⟹ c) ⟹ b) ⟹ b') ⟹ a') ⟹ a) ⟹ c''').
```

The first three are trivial. To see that c) implies b), note first that c) entails that `X₀` is dense in `X`. Replacing
`X` and `X₀` by a suitable open set `U` of `X` and by `U ∩ X₀` respectively, we may then assume `Z` is locally closed in
`X`, hence `Z = V ∩ ∁W`, where `V` and `W` are open in `X`; the hypothesis `Z ≠ ∅` means `V ⊄ W`, or equivalently
`V ∪ W ≠ W`. By c), one then has `(V ∪ W) ∩ X₀ ≠ W ∩ X₀`, hence `V ∩ X₀ ⊄ W`, and consequently `(V ∩ ∁W) ∩ X₀ ≠ ∅`.

To see that b) entails b'), it suffices to apply b) to `Z ∩ U`, where `U` is an arbitrary open neighbourhood of a point
of `Z`. Since `Z ∩ X₀ ⊂ Z`, it is trivial that b') implies a'). To show that a') entails a), note that if `Z` is locally
closed in `X`, we may write `Z = F − F'` where `F` and `F'` are closed in `X` and `F' ⊂ F`; hence
`Z ∩ X₀ = (F ∩ X₀) − (F' ∩ X₀)`. If one had `Z ∩ X₀ = ∅`, one would deduce `F ∩ X₀ ⊂ F' ∩ X₀`, hence `F = F'` by a'),
that is, `Z = ∅`.

To see that a) entails c'''), it suffices to show that if `Z ≠ ∅` is locally quasi-constructible, then `Z ∩ X₀ ≠ ∅`:
indeed, the relation `Z' ∩ X₀ = Z'' ∩ X₀` is equivalent to `((Z' ∪ Z'') − (Z' ∩ Z'')) ∩ X₀ = ∅`. In other words, it
suffices to prove that a) entails b); moreover, replacing `X` and `X₀` by an open set `U` of `X` and by `U ∩ X₀`
respectively, we are reduced to the case where `Z` is locally closed in `X`, whence the conclusion.

It remains to show that the map `ℒ𝒬c(X) → ℒ𝒬c(X₀)` is surjective. Let `Z₀` be a locally quasi-constructible subset of
`X₀`: there is a cover `(V_α)` of `X₀` by open sets of `X₀` such that `Z₀ ∩ V_α` is quasi-constructible in `V_α` (and

<!-- original page 97 -->

hence also in `X₀`). By c), there exists for each `α` a unique open set `U_α` of `X` such that `X₀ ∩ U_α = V_α`, and by
c'') a unique quasi-constructible set `Z_α` in `X` such that `Z₀ ∩ V_α = X₀ ∩ Z_α`. If `α` and `β` are any two indices,
one has `Z_β ∩ U_α ∩ X₀ = U_α ∩ Z₀ ∩ V_β = V_α ∩ Z₀ ∩ V_β = Z_α ∩ X₀ ∩ V_β ⊂ Z_α ∩ X₀`; since `Z_β ∩ U_α` and `Z_α` are
quasi-constructible in `X`, it follows from c'') that `Z_β ∩ U_α ⊂ Z_α`. Setting `Z = ⋃ Z_α`, one therefore has
`Z ∩ U_α = Z_α` for every `α`; moreover, since the `V_α` cover `X₀`, it follows from c) that the `U_α` cover `X`, and
one sees that `Z` is locally quasi-constructible in `X` and `Z₀ = Z ∩ X₀`.

**Definition (10.1.3).**

<!-- label: IV.10.1.3 -->

*When a subset `X₀` of a topological space `X` satisfies the equivalent conditions of `(10.1.2)`, one says that `X₀` is
**very dense** in `X`.*

It has already been seen in the course of the proof of `(10.1.2)` that `X₀` is then dense in `X`.

**Corollary (10.1.4).**

<!-- label: IV.10.1.4 -->

*If `X₀` is very dense in `X` and `U` is an open subset of `X`, then `U ∩ X₀` is very dense in `U`. Conversely, if
`(U_α)` is an open cover of `X` such that `U_α ∩ X₀` is very dense in `U_α` for every `α`, then `X₀` is very dense in
`X`.*

Since every locally closed subset of `U` is locally closed in `X`, the first assertion follows from criterion a) of
`(10.1.2)`; the same is true of the second, for if `Z ≠ ∅` is locally closed in `X`, then `Z ∩ U_α` is locally closed in
`U_α` for every `α`, and `Z ∩ U_α ≠ ∅` for at least one `α`.

### 10.2. Quasi-homeomorphisms

**Proposition (10.2.1).**

<!-- label: IV.10.2.1 -->

*Let `X₀`, `X` be two topological spaces, `f : X₀ → X` a continuous map. The following conditions are equivalent:*

*a) The map `U ↦ f⁻¹(U)` from `𝒪(X)` to `𝒪(X₀)` is bijective.*

*a') The map `F ↦ f⁻¹(F)` from `𝔉(X)` to `𝔉(X₀)` is bijective.*

*b) The topology of `X₀` is the inverse image under `f` of that of `X`, and `f(X₀)` is very dense `(10.1.3)` in `X`.*

*c) The functor `ℱ ↦ f*(ℱ)` from the category of sheaves of sets (resp. sheaves of abelian groups) on `X` to the
category of sheaves of sets (resp. sheaves of abelian groups) on `X₀` is an equivalence of categories.*

It is clear that a) and a') are equivalent, and a) implies that the topology of `X₀` is the inverse image under `f` of
that of `X`. On the other hand, if `f(X₀)` is not very dense in `X`, there exist two distinct open sets `U₁, U₂` of `X`
such that `U₁ ∩ f(X₀) = U₂ ∩ f(X₀)`, and consequently `f⁻¹(U₁) = f⁻¹(U₂)`, which shows that a) entails b). Conversely,
condition b) implies that the maps `U ↦ U ∩ f(X₀)` from `𝒪(X)` to `𝒪(f(X₀))` and `V ↦ f⁻¹(V)` from `𝒪(f(X₀))` to `𝒪(X₀)`
are bijective, hence so is their composite `U ↦ f⁻¹(U)`.

To see that a) entails c), it suffices to apply the definition of `f*(ℱ)` `(0_I, 3.7.1)` and the sheaf axioms: a)
entails that for every open `U` of `X`, the canonical map `Γ(U, ℱ) → Γ(f⁻¹(U), f*(ℱ))` is a bijection functorial in `ℱ`,
whence c). It remains to show that c) entails b).

<!-- original page 98 -->

Suppose first that `f(X₀)` is not very dense in `X`; there then exist two distinct closed subsets `Y ⊋ Y'` of `X` such
that `Y ∩ f(X₀) = Y' ∩ f(X₀)`. Let `ℱ` (resp. `ℱ'`) be the sheaf of abelian groups on `X` direct image under the
canonical injection `Y → X` (resp. `Y' → X`) of the simple sheaf associated with the constant presheaf `ℤ` on `Y` (resp.
`Y'`); the definition of `f*` `(0_I, 3.7.1)` shows that `f*(ℱ)` is isomorphic to `f*(ℱ')`, but `ℱ` is not isomorphic to
`ℱ'`, so condition c) is not satisfied. (Note that the functor `f*` is then not even faithful, for if `u` and `v` are
the identity automorphism and the zero endomorphism of `ℱ → ℱ'`, then `f*(u)` and `f*(v)` are equal.)

Let us now show that c) entails that the topology of `X₀` is the inverse image of that of `X` under `f`. Note that if
condition c) is satisfied for the category of sheaves of sets, it is also satisfied for the category of sheaves of
abelian groups, since it follows immediately from the definitions `(0_III, 8.2.5)` that the latter is none other than
the category of group objects in the category of sheaves of sets. It therefore suffices to prove our assertion assuming
c) is satisfied for the categories of sheaves of abelian groups on `X` and `X₀`. Now, if `ℤ_X` denotes the simple sheaf
on `X` associated with the constant presheaf equal to `ℤ`, one has a canonical isomorphism `Γ(X, ℱ) ≃ Hom(ℤ_X, ℱ)`
functorial in `ℱ` (same argument as in `(0_I, 5.1.1)`); since it is clear from the definition `(0_I, 3.7.1)` that
`f*(ℤ_X) = ℤ_{X₀}`, the hypothesis that `f*` is an equivalence entails that the canonical homomorphism
`Γ(X, ℱ) → Γ(X₀, f*(ℱ))` is bijective for every sheaf of abelian groups `ℱ` on `X`. Now let `Y₀` be a closed subset of
`X₀`; let `ℱ₀` be the sheaf on `X₀` direct image under the canonical injection `Y₀ → X₀` of the simple sheaf associated
with the constant presheaf `ℤ` on `Y₀`. Since `f*` is an equivalence, `ℱ₀` is isomorphic to a sheaf of the form `f*(ℱ)`,
where `ℱ` is a sheaf of abelian groups on `X`. Consider the section `s₀` of `ℱ₀` over `X₀` such that
`(s₀)_{x₀} = 1_{(ℱ₀)_{x₀}}` if `x₀ ∈ Y₀`, `(s₀)_{x₀} = 0_{(ℱ₀)_{x₀}}` if `x₀ ∉ Y₀`. The preceding remarks show that
there exists a section `s` of `ℱ` over `X` such that `(s₀)_{x₀} = s_{f(x₀)}` for every `x₀ ∈ X₀` (the fibres `(ℱ₀)_{x₀}`
and `ℱ_{f(x₀)}` being canonically identified `(0_I, 3.7.1)`); this entails that `Y₀` is the inverse image under `f` of
the set `Y` of `x ∈ X` such that `s_x ≠ 0_x`, and `Y` is closed in `X`. Q.E.D.

**Definition (10.2.2).**

<!-- label: IV.10.2.2 -->

*When a continuous map `f : X₀ → X` satisfies the equivalent conditions of `(10.2.1)`, one says that `f` is a
**quasi-homeomorphism** of `X₀` into `X`.*

By virtue of `(10.2.1, b))`, to say that a subset `X₀` of a topological space `X` is very dense in `X` means that the
canonical injection `X₀ → X` is a quasi-homeomorphism.

**Corollary (10.2.3).**

<!-- label: IV.10.2.3 -->

*The composite of two quasi-homeomorphisms is a quasi-homeomorphism.*

This follows immediately from `(10.2.1, a))`.

**Corollary (10.2.4).**

<!-- label: IV.10.2.4 -->

*Let `f : X → Y` be a quasi-homeomorphism, `Y'` a locally quasi-constructible subset of `Y`, `X' = f⁻¹(Y')`; then the
restriction `f' = f|X' : X' → Y'` is a quasi-homeomorphism.*

It is clear by `(10.2.1, b))` that the topology induced on `X'` by that of `X` is the inverse image under `f'` of the
topology induced on `Y'` by that of `Y`. On the other hand,

<!-- original page 99 -->

let `Z ≠ ∅` be a closed subset of `Y'`, and `ξ ∈ Z`; there is an open neighbourhood `U` of `ξ` in `Y` such that `U ∩ Y'`
is a finite union of subsets `Y_j'` closed in `U`; if `j` is an index such that `ξ ∈ Y_j'`, then `Z ∩ Y_j'` is closed in
`U`. Since `f(X) ∩ U` is very dense in `U` `(10.1.4)`, `Z ∩ Y_j' ∩ f(X)` is non-empty `(10.1.2, a))`, and a fortiori
`Z ∩ f(X)`; but since `Z ⊂ Y'`, one has `Z ∩ f(X) = Z ∩ f'(X')`. Criterion `(10.1.2, a))` thus shows that `f'(X')` is
very dense in `Y'`, and one concludes using `(10.2.1, b))`.

**Corollary (10.2.5).**

<!-- label: IV.10.2.5 -->

*Let `f : X → Y` be a continuous map, `(V_α)` an open cover of `Y`. If, for every `α`, the restriction `f⁻¹(V_α) → V_α`
of `f` is a quasi-homeomorphism, then `f` is a quasi-homeomorphism.*

This follows immediately from criterion `(10.2.1, b))` and from `(10.1.4)`.

**Corollary (10.2.6).**

<!-- label: IV.10.2.6 -->

*Let `f : X → Y` be a quasi-homeomorphism, `Y'` a locally quasi-constructible subset of `Y`, `X' = f⁻¹(Y')`. For `Y'` to
be quasi-compact (resp. Noetherian, resp. retrocompact in `Y`), it is necessary and sufficient that `X'` be
quasi-compact (resp. Noetherian, resp. retrocompact in `X`).*

Let us first prove the first two assertions; by virtue of `(10.2.4)`, we may assume `Y' = Y`. To say that `X` is
quasi-compact (resp. Noetherian) means that for every filtered increasing family `(U_α)` in `𝒪(X)` having `X` as largest
element (resp. for every filtered increasing family `(U_α)` in `𝒪(X)`), there exists `γ` such that `U_α = U_γ` for
`α ⩾ γ`. Since `U ↦ f⁻¹(U)` is a bijection of `𝒪(Y)` onto `𝒪(X)`, our assertion follows immediately from the preceding
remark.

The quasi-compact open sets of `X` are thus the sets of the form `f⁻¹(U)` where `U` is a quasi-compact open set in `Y`,
by `(10.2.1, a))` and what precedes. For `X'` to be retrocompact in `X`, it is necessary and sufficient that for every
quasi-compact open `U` in `Y`, `f⁻¹(U) ∩ X' = f⁻¹(U ∩ Y')` be quasi-compact `(0_III, 9.1.1)`; the first part of the
proof shows that this is equivalent to saying that `U ∩ Y'` is quasi-compact for every quasi-compact open `U`, that is,
that `Y'` is retrocompact in `Y`.

**Proposition (10.2.7).**

<!-- label: IV.10.2.7 -->

*Let `f : X → Y` be a quasi-homeomorphism. Then the map `Z ↦ f⁻¹(Z)` from `𝔓(Y)` to `𝔓(X)` defines by restriction the
following bijections (cf. `(10.1.1)` for the notation):*

```text
  𝒪(Y) ≃ 𝒪(X)
  𝔉(Y) ≃ 𝔉(X)
  ℒℱ(Y) ≃ ℒℱ(X)
  ℒ𝒬c(Y) ≃ ℒ𝒬c(X)
  ℭ(Y) ≃ ℭ(X)
  ℒℭ(Y) ≃ ℒℭ(X).
```

For the first two, this is none other than the definition `(10.2.2)`; since the topology of `X` is the inverse image
under `f` of that of `f(X)`, the last five maps,

<!-- original page 100 -->

where one replaces `Y` by `f(X)`, are bijective. One may therefore (by `(10.2.1, b))`) restrict to the case where `X` is
a very dense subspace of `Y`, and the fact that the maps `𝔉(Y) → 𝔉(X)`, `ℒℱ(Y) → ℒℱ(X)`, `ℒ𝒬c(Y) → ℒ𝒬c(X)` are bijective
has already been proved `(10.1.2)`. Every locally constructible subset being locally quasi-constructible, the maps
`ℭ(Y) → ℭ(X)` and `ℒℭ(Y) → ℒℭ(X)` are injective; in addition, for every open `U ⊂ Y`, the restriction `f⁻¹(U) → U` of
`f` is a quasi-homeomorphism `(10.2.4)`, so if one shows that `ℭ(Y) → ℭ(X)` is surjective, the same will be true of
`ℒℭ(Y) → ℒℭ(X)`. But by `(10.2.6)`, every open retrocompact subset `Z` in `X` is of the form `f⁻¹(T)`, where `T` is open
retrocompact in `Y`; this evidently proves the surjectivity of `ℭ(Y) → ℭ(X)`.

**Remarks (10.2.8).**

<!-- label: IV.10.2.8 -->

*(i)* It was seen in the proof of `(10.2.1)` that if `f` is a quasi-homeomorphism, the canonical map

```text
(10.2.8.1)        Γ(Y, ℱ) → Γ(X, f*(ℱ))
```

is an isomorphism of abelian groups functorial in `ℱ` in the category of sheaves of abelian groups on `Y`. Since `f*` is
exact in this category `(0_I, 3.7.2)`, this implies that the canonical homomorphisms `(T, 3.2.2)`

```text
  H^i(Y, ℱ) → H^i(X, f*(ℱ))
```

are bijective for every `i`.

*(ii)* If `f : X → Y` is a continuous map and `ℱ, 𝒢` are two sheaves of abelian groups on `Y`, one has
`f*(ℱ ⊗_{ℤ_Y} 𝒢) = f*(ℱ) ⊗_{ℤ_X} f*(𝒢)` up to canonical isomorphism `(0_I, 4.3.3)`. One concludes that if `f` is a
quasi-homeomorphism, `f*` is also an equivalence of the category of sheaves of rings on `Y` and the category of sheaves
of rings on `X`; the datum of a ringed-space structure on `Y` is thus equivalent to that of a ringed-space structure on
`X`.

Given two ringed spaces `(X, 𝒪_X)`, `(Y, 𝒪_Y)`, we shall say that a morphism of ringed spaces
`f = (ψ, θ) : (X, 𝒪_X) → (Y, 𝒪_Y)` is a *quasi-isomorphism* if `ψ` is a quasi-homeomorphism of `X` into `Y` and
`θ♯ : ψ*(𝒪_Y) → 𝒪_X` is an isomorphism of sheaves of rings; when this is so, the ringed space `(X, 𝒪_X)` is entirely
determined, up to isomorphism, by `(Y, 𝒪_Y)`, the space `X`, and the quasi-homeomorphism `ψ` (which one may take
arbitrary). When `f` is a quasi-isomorphism of ringed spaces, the functor

```text
  ℱ ↦ f*(ℱ)
```

is an equivalence of the category of `𝒪_Y`-Modules with that of `𝒪_X`-Modules, since `f*(ℱ)` is here canonically
identified with `ψ*(ℱ)`. One concludes, for example, isomorphisms of bi-`∂`-functors

```text
  Ext^p_{𝒪_Y}(ℱ, 𝒢) ≃ Ext^p_{𝒪_X}(f*(ℱ), f*(𝒢)).
```

In general, one may say that the usual constructions of sheaf theory and homological algebra, performed on the ringed
space `Y` or on the ringed space `X`, are equivalent.

<!-- original page 101 -->

### 10.3. Jacobson spaces

**Definition (10.3.1).**

<!-- label: IV.10.3.1 -->

*One says that a topological space `X` is a **Jacobson space** if the set `X₀` of closed points of `X` is very dense in
`X` (in other words, if the canonical injection `X₀ → X` is a quasi-homeomorphism).*

This means therefore `(10.1.2)` that every locally closed (or only locally quasi-constructible) subset `Z ≠ ∅` of `X`
contains a closed point of `X`, or also that *every closed subset of `X` is the closure of the set of its closed
points*.

**Proposition (10.3.2).**

<!-- label: IV.10.3.2 -->

*Let `X` be a Jacobson space, `Z` a locally quasi-constructible subset of `X`; then the subspace `Z` of `X` is a
Jacobson space, and for a point of `Z` to be closed in `Z`, it is necessary and sufficient that it be closed in `X`.*

If `X₀` is the set of closed points of `X`, then `Z ∩ X₀` is very dense in `Z` by virtue of `(10.2.4)` applied to the
injection `i : X₀ → X`; since the set `Z₀` of closed points of `Z` obviously contains `Z ∩ X₀`, it is a fortiori very
dense in `Z`, so `Z` is a Jacobson space. Let us now show that one has in fact `Z₀ = Z ∩ X₀`; let `x ∈ Z` be a point
closed in `Z`; let `‾{x}` be its closure in `X`; then `‾{x} ∩ Z = {x}` is therefore a locally quasi-constructible subset
of `X`, and since its intersection with `X₀` is non-empty `(10.1.2)`, one has `x ∈ X₀`.

**Proposition (10.3.3).**

<!-- label: IV.10.3.3 -->

*Let `X` be a topological space, `(U_α)` an open cover of `X`. For `X` to be a Jacobson space, it is necessary and
sufficient that each of the subspaces `U_α` be one.*

The condition is necessary by virtue of `(10.3.2)`. Conversely, let us first show that the hypothesis that the `U_α` are
Jacobson spaces entails that for a point `x ∈ U_α` to be closed in `X`, it suffices that it be closed in `U_α`. It
suffices in fact to see that this condition entails that `x` is also closed in each of the `U_β` that contain it; but
`U_α ∩ U_β` is open in `U_α`, so `x` is closed in `U_α ∩ U_β`, and by `(10.3.2)`, `x` is also closed in `U_β`, which
completes the proof.

### 10.4. Jacobson preschemes and Jacobson rings

**Definition (10.4.1).**

<!-- label: IV.10.4.1 -->

*One says that a prescheme `X` is a **Jacobson prescheme** if the underlying topological space `X` is a Jacobson space.
One says that a ring `A` is a **Jacobson ring** if `Spec(A)` is a Jacobson prescheme.*

Every closed subset of `X = Spec(A)` is of the form `Z = V(𝔞)`, where `𝔞` is an ideal equal to its radical, and the set
`X₀` of closed points of `X` is the set of maximal ideals of `A`; to say that `Z ∩ X₀` is dense in `Z` means therefore
that `𝔞` is an intersection of maximal ideals `(I, 1.1.4)`; since `𝔞` is an intersection of prime ideals, this amounts
to saying that every prime ideal of `A` is an intersection of maximal ideals; by virtue of `(10.3.1)` and `(10.1.2)`,
the usual definition of Jacobson rings `(Bourbaki, Alg. comm., chap. V, §3, n° 4, déf. 1)` therefore coincides with
definition `(10.4.1)`.

<!-- original page 102 -->

**Proposition (10.4.2).**

<!-- label: IV.10.4.2 -->

*Let `X` be a prescheme, `(U_α)` a cover of `X` by affine open sets. For `X` to be a Jacobson prescheme, it is necessary
and sufficient that the rings `Γ(U_α, 𝒪_X)` of the `U_α` be Jacobson rings.*

This follows from `(10.3.3)` and from definition `(10.4.1)`.

**(10.4.3)**

<!-- label: IV.10.4.3 -->

A discrete prescheme is a Jacobson prescheme; an Artinian ring is therefore a Jacobson ring. Every principal ring having
infinitely many maximal ideals (for example `ℤ`) is a Jacobson ring; a local Noetherian ring `A` is a Jacobson ring if
and only if its maximal ideal is its only prime ideal, that is, if `A` is Artinian. Every subprescheme of a Jacobson
prescheme is a Jacobson prescheme by virtue of `(10.3.2)`.

**Proposition (10.4.4).**

<!-- label: IV.10.4.4 -->

*Let `B` be an integral ring. The following conditions are equivalent:*

*a) There exists `f ≠ 0` in `B` such that `B_f` is a field.*

*b) The field of fractions of `B` is a `B`-algebra of finite type.*

*c) There exists a field `K` containing `B` which is a `B`-algebra of finite type.*

*d) The generic point of `Spec(B)` is isolated in `Spec(B)`.*

It is clear that d) is equivalent to a), since d) means that there exists `f ≠ 0` in `B` such that `D(f)` is reduced to
the generic point of `Spec(B)`. It is trivial that a) entails b) and that b) entails c). Finally, c) entails a), by
virtue of `(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 2 of th. 1)`.

**Proposition (10.4.5).**

<!-- label: IV.10.4.5 -->

*Let `A` be a ring. The following conditions are equivalent:*

*a) `A` is a Jacobson ring.*

*b) For every non-maximal prime ideal `𝔭` of `A` and every `f ≠ 0` in `B = A/𝔭`, `B_f` is not a field.*

*b') Every `A`-algebra of finite type `K` which is a field is a finite `A`-algebra.*

It is known that a) entails b') `(Bourbaki, Alg. comm., chap. V, §3, n° 4, cor. 3 of th. 3)`. Moreover, the kernel of
the homomorphism `A → K` is then a maximal ideal `𝔪` of `A`, and `K` is a finite extension of `A/𝔪` (loc. cit.). It is
trivial that b') entails b), since `A/𝔭 = B` is not a field, every `B`-algebra of finite type is an `A`-algebra of
finite type, and `B_f` is a `B`-algebra of finite type. It remains to see that b) implies a). We shall use the following
lemma:

**Lemma (10.4.5.1).**

<!-- label: IV.10.4.5.1 -->

*Let `X` be a topological space having the following property: for every locally closed subset `Z ≠ ∅` of `X`, there
exists a subset `Z'` of `Z`, locally closed in `X` (or in `Z`, which amounts to the same thing), and a point `x ∈ Z'`,
closed in `Z'`. Then, for `X` to be a Jacobson space, it is necessary and sufficient that no non-closed point `x` of `X`
be isolated in `‾{x}`.*

If `X` is a Jacobson space, a non-closed point `x` of `X` cannot be isolated in `‾{x}`, for this would mean that there
exists an open set `U` of `X` such that `U ∩ ‾{x} = {x}`; but `U ∩ ‾{x}` is locally closed in `X` and would contain no
point closed in `X`, which is contrary to the hypothesis that `X` is a Jacobson space. Conversely, suppose the condition
of the statement is satisfied; then the set of closed points of `X` is identical with the set `X₀` of `x ∈ X` that are
isolated in `‾{x}`; but it follows from `(5.1.10.1)` that

<!-- original page 103 -->

this set is very dense in `X`, so `X` is a Jacobson space by definition.

Recall `(5.1.10)` that the hypothesis made on `X` in `(10.4.5.1)` is always satisfied when `X` is the space underlying a
prescheme.

Returning then to the proof of `(10.4.5)`, condition b) entails that for every non-closed point `x` of `Spec(A)`, the
generic point `x` of `Spec(A/𝔭) = V(𝔭) = ‾{x}` is not isolated in `‾{x}`, so b) entails a) by virtue of the lemma
`(10.4.5.1)` and `(10.4.4)`.

**Corollary (10.4.6).**

<!-- label: IV.10.4.6 -->

*Every algebra of finite type `B` over a Jacobson ring `A` is a Jacobson ring, and the inverse image in `A` of every
maximal ideal of `B` is a maximal ideal of `A`. In particular, every algebra of finite type over a field or over `ℤ` is
a Jacobson ring.*

A `B`-algebra of finite type `K` that is a field is also an `A`-algebra of finite type, hence an `A`-module of finite
type and a fortiori a `B`-module of finite type, whence the first assertion; the second was proved in the course of the
proof of `(10.4.5)`, applied to `K = B/𝔪`.

**Corollary (10.4.7).**

<!-- label: IV.10.4.7 -->

*If `X` is a Jacobson prescheme, `f : Y → X` a morphism locally of finite type, then `Y` is a Jacobson prescheme and the
image under `f` of every closed point in `Y` is a closed point in `X`.*

The question being local on `X` and on `Y`, one is reduced to the case where `X` and `Y` are affine, and the corollary
then follows from `(10.4.6)`.

**Corollary (10.4.8).**

<!-- label: IV.10.4.8 -->

*If `k` is an algebraically closed field, `X` a `k`-prescheme locally of finite type, the set of points of `X` rational
over `k` is very dense in `X`.*

Indeed, `X` is a Jacobson prescheme `(10.4.7)` and the closed points of `X` are exactly the points rational over `k`
`(I, 6.4.2)`.

**(10.4.9)**

<!-- label: IV.10.4.9 -->

The fact that preschemes locally of finite type over a field or over `ℤ` are Jacobson preschemes is particularly
important, in view of the possibility of reducing many questions of algebraic geometry to this case `(8.1.2, c))`. We
shall give two examples.

**Applications (10.4.10). I. Proof of `(6.15.9)`.**

<!-- label: IV.10.4.10 -->

Let `k` be a separably closed field, `X` a `k`-prescheme locally of finite type over `k` and unibranch. It is known that
the integral closure of an integral `k`-algebra of finite type `A` in a finite extension of its field of fractions is a
finite `A`-algebra `(Bourbaki, Alg. comm., chap. V, §3, n° 2, th. 2)`, so every `A`-algebra of finite type is a
universally Japanese ring; one concludes that the set of points `x ∈ X` where `X` is geometrically unibranch is locally
constructible `(9.7.10)`. But the hypothesis and the lemma `(6.15.8)` entail that this set contains all closed points of
`X`. The conclusion therefore results from `(10.4.6)`, `(10.3.1)`, and the bijectivity of the canonical map
`ℒℭ(X) → ℒℭ(X₀)` (where `X₀` is the set of closed points of `X`) `(10.2.7)`.

**Applications. II. Proposition (10.4.11).**

<!-- label: IV.10.4.11 -->

*Let `S` be a prescheme, `X` an `S`-prescheme of finite type. Every `S`-endomorphism of `X` that is radicial is
surjective (hence bijective).*

<!-- original page 104 -->

Let `f : X → S` be the structure morphism, `g : X → X` the `S`-endomorphism under consideration, and, for every `s ∈ S`,
let `g_s` be the morphism deduced from `g` by the base change `Spec(k(s)) → S`, which is a `k(s)`-endomorphism of the
fibre `f⁻¹(s) = X ×_S Spec(k(s))`.

To prove that `g` is surjective, it suffices to prove that `g_s` is surjective for every `s ∈ S`, so one may (by virtue
of `(I, 3.5.7)`) assume `S = Spec(k)` is the spectrum of a field `k`, in which case `f` is a morphism of finite
presentation, since `S` is Noetherian. Applying `(8.9.1)` and `(8.10.5, (vii))`, one is reduced to the case where
`S = Spec(A)`, where `A` is a `ℤ`-subalgebra of finite type of `k`. Now `X` is then a Jacobson prescheme `(10.4.7)`, and
`g(X)` is constructible in `X` `(1.8.5)`, so to prove that `g(X) = X`, it suffices to show that `g(X)` contains all
closed points of `X` `(10.3.1)`.

**Lemma (10.4.11.1).**

<!-- label: IV.10.4.11.1 -->

*Let `Y` be a `ℤ`-prescheme of finite type.*

*(i) For a point `y ∈ Y` to be closed in `Y`, it is necessary and sufficient that `k(y)` be a finite field.*

*(ii) For every prime number `p` and every integer `d ⩾ 1`, the set of points `y ∈ Y` such that `k(y)` is an extension
of `𝔽_p` whose degree divides `d` is finite.*

Assertion (i) follows from the fact that the image of a closed point `y ∈ Y` in `Spec(ℤ)` is a closed point `(10.4.7)`,
in other words a prime number, and from `(I, 6.4.2)`. On the other hand, since `Y` is a finite union of affine open sets
of finite type over `ℤ`, one may restrict, to prove (ii), to the case where `Y = Spec(C)`, where `C` is a `ℤ`-algebra of
finite type. Now the points `y ∈ Y` such that the degree of `k(y)` over `𝔽_p` divides `d` correspond bijectively to the
homomorphisms `C → 𝔽_{p^d}`; but if `(t_i)` is a system of generators of the `ℤ`-algebra `C`, every homomorphism of `C`
is determined by its values on the elements `t_i`, and consequently there are only finitely many homomorphisms of `C`
into a finite field.

This being so, `X` is a `ℤ`-prescheme of finite type; let `T_{p,d}` be the set of closed points `z ∈ X` such that `k(z)`
is an extension of `𝔽_p` of degree dividing `d`; it follows from `(10.4.11.1)` that the set `T_{p,d}` is finite and that
the set of closed points of `X` is the union of the `T_{p,d}`. Moreover, if `z ∈ T_{p,d}` and if `h` is any endomorphism
of `X`, `k(h(z))` is isomorphic to a subfield of `k(z)`, so `h(z) ∈ T_{p,d}`, in other words `T_{p,d}` is stable under
every endomorphism of `X`. Since `g` is by hypothesis injective, its restriction to `T_{p,d}` is bijective since
`T_{p,d}` is finite, which completes the proof of the proposition.

We shall see later `(17.9.7)` that when one further assumes, on the one hand, that `X` is an `S`-prescheme of finite
presentation, and on the other hand, that `g` is a monomorphism, then one can affirm that `g` is an automorphism of `X`.

### 10.5. Noetherian Jacobson preschemes

**Proposition (10.5.1).**

<!-- label: IV.10.5.1 -->

*Let `B` be a Noetherian integral ring. The equivalent conditions a) to d) of `(10.4.4)` are then also equivalent to the
following:*

*e) `Spec(B)` is finite.*

*f) `B` is a semi-local ring of dimension `⩽ 1`.*

It follows in fact from the Artin-Tate theorem `(0, 16.3.3)` that the conditions a) and f) are equivalent. The condition
f) implies that `Spec(B)` is the union of the finite set

<!-- original page 105 -->

of its closed points and its generic point, so f) implies e) without supposing `A` Noetherian. Finally e) implies d)
without supposing `A` Noetherian, for the generic point `x` of `X` is the complement of the union of the closures
`‾{y}`, where `y` ranges over the set of points `y ≠ x`, and since these points are finite in number, `{x}` is the
complement of a closed set in `X`.

**Corollary (10.5.2).**

<!-- label: IV.10.5.2 -->

*Let `A` be a Noetherian ring. For `A` to be a Jacobson ring, it is necessary and sufficient that there exist no prime
ideal `𝔭` of `A` such that `A/𝔭` be a semi-local ring of dimension `1`.*

This follows immediately from `(10.5.1)` and from condition b) of `(10.4.5)`, the prime ideals `𝔭` of `A` such that
`A/𝔭` is semi-local of dimension `0` being the maximal ideals of `A`.

**Corollary (10.5.3).**

<!-- label: IV.10.5.3 -->

*Let `X` be a Noetherian irreducible prescheme. The following conditions are equivalent:*

*a) The generic point of `X` is isolated.*

*b) `X` is finite.*

*c) `X` is of dimension `⩽ 1` and its set of closed points is finite.*

There exist by hypothesis a finite number of irreducible affine open sets `U_i` (`1 ⩽ i ⩽ n`) covering `X`, each of
which therefore contains the generic point of `X`; it suffices to prove the equivalence of a), b), and c) for each of
the `(U_i)_red` (taking `(0, 14.1.7)` into account). But this equivalence then follows from `(10.5.1)`.

**Remark (10.5.4).**

<!-- label: IV.10.5.4 -->

A Noetherian prescheme `X` satisfying the equivalent conditions of `(10.5.3)` is not necessarily an affine scheme; in
fact, it may even fail to be separated. One has an example by replacing, in example `(I, 5.5.11)` of the "affine line
with doubled point", `X_1` and `X_2` by the spectrum of the discrete valuation ring `(K[t])_{(t)}`, and `U_{12}` and
`U_{21}` by the open set reduced to the generic point in `X_1` and `X_2` respectively; the non-separated prescheme `X`
that one obtains has exactly 3 points.

**Proposition (10.5.5).**

<!-- label: IV.10.5.5 -->

*Let `X` be a Noetherian prescheme.*

*(i) The set `X₀` of points `x ∈ X` such that `‾{x}` is finite is very dense in `X`.*

*(ii) For `X` to be a Jacobson prescheme, it is necessary and sufficient that there exist no subprescheme of `X`
isomorphic to the spectrum of an integral semi-local ring of dimension `1`.*

The condition that `‾{x}` be finite is equivalent here `(10.5.3)` to the fact that `x` be isolated in `‾{x}`, `‾{x}`
being the space underlying a (Noetherian) subprescheme of `X`; assertion (i) therefore follows from `(5.1.10.1)`.
Similarly, taking `(10.4.5.1)` into account, to prove assertion (ii), note that for a non-closed point `x` of `X` to
belong to `X₀`, it is necessary and sufficient that the closed integral subprescheme `Y` of `X` having `‾{x}` as
underlying space be of dimension `1` and finite, hence a finite union of (open in `Y`) affine subpreschemes `U_i` that
are spectra of integral semi-local rings of dimension `1`. Conversely, if there is a subprescheme `Z` of `X` that is the
spectrum of an integral semi-local ring of dimension `1`, then `Z` is not a Jacobson prescheme `(10.5.2)`, so neither is
`X` `(10.3.2)`.

<!-- original page 106 -->

**Remark (10.5.6).**

<!-- label: IV.10.5.6 -->

Assertion (ii) of `(10.5.5)` remains valid when `X` is locally Noetherian: indeed, if `(V_α)` is a cover of `X` by
(Noetherian) affine open sets, every subprescheme of a `V_α` is a subprescheme of `X`; conversely, if a subprescheme `Z`
of `X` is isomorphic to the spectrum of an integral semi-local ring of dimension `1`, there is some `α` such that
`V_α ∩ Z` contains an affine open `U` of `Z` not reduced to the generic point of `Z`, which is therefore also the
spectrum of an integral semi-local ring of dimension `1`. One concludes by means of `(10.3.3)`.

**Proposition (10.5.7).**

<!-- label: IV.10.5.7 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed subset of `X` such that every non-empty closed subset of `X`
meets `Y`. Then the prescheme induced on the open set `X − Y` is a Jacobson prescheme.*

Apply criterion `(10.5.5, (ii))`, and suppose there is a subprescheme `Z` of `X − Y` that is the spectrum of an integral
semi-local ring of dimension `1`, the generic point `z` of `Z` being isolated in `Z` (or in the closure `‾Z` of `Z` in
`X`), and `Z` being distinct from `{z}`. Let `y ≠ z` be a point of `Z`; since it does not belong to `Y`, it is not
closed in `X`, and its closure `‾{y}` in `X` meets `Y` at a point `x ≠ y` which is therefore a specialization of `y`.
The existence of the chain `{x} ⊂ ‾{y} ⊂ ‾{z}` shows then that the dimension of `‾{z}` would be `⩾ 2`, and the same
would be true of the dimension of `U ∩ ‾{z}`, where `U` is an affine (hence Noetherian) open neighbourhood of `x` in
`X`. But this contradicts the fact that the generic point `z` of `U ∩ ‾{z}` is isolated in `U ∩ ‾{z}` `(10.5.3)`.

**Corollary (10.5.8).**

<!-- label: IV.10.5.8 -->

*Let `A` be a Noetherian ring; for every element `f` of the radical `𝔑` of `A`, the ring `A_f` is a Jacobson ring, and
the open set `Spec(A) − V(𝔑)` is a Jacobson scheme.*

If `X = Spec(A)`, `Y = V(𝔍)`, where `𝔍` is an ideal of `A`, to say that every non-empty closed subset of `X` meets `Y`
is equivalent `(0_I, 2.1.3)` to saying that `Y` contains all closed points of `X`, or again that `𝔍` is contained in the
radical `𝔑` of `A`. If `f ∈ 𝔑`, the open set `D(f)` therefore does not meet `V(𝔑)`, and is a Jacobson space by virtue of
`(10.5.7)`.

**Corollary (10.5.9).**

<!-- label: IV.10.5.9 -->

*Let `A` be a local Noetherian ring, `𝔪` its maximal ideal, `X = Spec(A)`, `Y = X − {𝔪}`; then `Y` is a Jacobson scheme,
whose closed points are the prime ideals `𝔭 ∈ Spec(A)` such that `dim(A/𝔭) = 1`.*

The first assertion is a particular case of `(10.5.8)`; on the other hand the closed points of `Y` are the prime ideals
`𝔭` of `A` which are maximal elements in the set of prime ideals `≠ 𝔪`, which, by definition of dimension, means that
`dim(A/𝔭) = 1`.

**Proposition (10.5.10).**

<!-- label: IV.10.5.10 -->

*Let `A` be a reduced complete local Noetherian ring which is not a field. Then the finite intersections of the kernels
of the local homomorphisms of `A` into discrete valuation rings `V` making `V` a finite `A`-algebra form a filter base
tending to `0` for the adic topology of `A`.*

It suffices `(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8)` to prove that the intersection of the kernels
considered in the statement is reduced to `0`. Suppose first that `A` is integral and of dimension `1`; by virtue of
Nagata's theorem `(0, 23.1.5 and 23.1.6)`, the integral closure `A'` of `A` is an integral complete local ring,

<!-- original page 107 -->

integrally closed, of dimension `1`, and a finite `A`-algebra; it is therefore a discrete valuation ring, and the
proposition follows immediately in this case.

Let us pass to the general case; let `x` be the closed point of `X = Spec(A)`, and set `Y = X − {x}`; one knows
`(10.5.9)` that `Y` is a Jacobson prescheme. Let us show that this entails that the intersection of the prime ideals `𝔭`
of `A` such that `dim(A/𝔭) = 1` is reduced to `0`; the proposition will follow since, for each of these ideals `𝔭`, the
intersection of the kernels of the local homomorphisms of `A/𝔭` into discrete valuation rings `V`, making `V` a finite
`(A/𝔭)`-algebra, is reduced to `0`. But to say that the intersection of these prime ideals is reduced to `0` means that
the set of these ideals is dense in `X`, or also in `Y` (since `Y` is dense in `X`), and this follows immediately from
`(10.5.9)`.

### 10.6. Dimension in Jacobson preschemes

The results of this number sharpen, in certain cases, and generalize results of §5.

**Proposition (10.6.1).**

<!-- label: IV.10.6.1 -->

*Let `S` be a locally Noetherian prescheme satisfying in addition the following conditions: 1° `S` is a Jacobson
prescheme; 2° for every `s ∈ S`, `𝒪_{S,s}` is universally catenary `(5.6.2)`; 3° every irreducible component `S'` of `S`
is equicodimensional (in other words, for every closed point `s` of `S'` and every subprescheme of `S` having `S'` as
underlying space, one has `dim(S') = dim(𝒪_{S',s})`). One then has the following properties:*

*(i) For every morphism `g : X → S` locally of finite type, `X` satisfies the preceding conditions 1°, 2°, and 3°. In
particular, if `X` is equidimensional (for example if `X` is irreducible), then `X` is biequidimensional (in other
words, `X` is catenary and for every closed point `x` of `X`, one has `dim(𝒪_{X,x}) = dim(X)` `(0, 14.3.3)`).*

*(ii) Let `X`, `Y` be two `S`-preschemes locally of finite type over `S`, `f : X → Y` an `S`-morphism; suppose `X`
irreducible and `f` dominant. If `ξ` (resp. `η`) is the generic point of `X` (resp. `Y`) and
`e = dim(f⁻¹(η)) = deg.tr_{k(η)} k(ξ)`, one has*

```text
(10.6.1.1)        dim(X) = dim(Y) + e.
```

*(iii) Let `X`, `Y` be two `S`-preschemes locally of finite type over `S`, `f : X → Y` an `S`-morphism, `n` an integer
`⩾ 0` such that one has `dim(f⁻¹(y)) ⩽ n` (resp. `dim(f⁻¹(y)) ⩾ n`) for every `y ∈ Y`. Then one has*

```text
(10.6.1.2)        dim(X) ⩽ dim(Y) + n
```

*(resp.*

```text
(10.6.1.3)        dim(X) ⩾ dim(Y) + n).
```

(i) Property 1° for `X` follows from `(10.4.7)`. For every `x ∈ X`, `𝒪_{X,x}` is the local ring at a prime ideal of an
`𝒪_{S,g(x)}`-algebra of finite type, and the homomorphism `𝒪_{S,g(x)} → 𝒪_{X,x}`

<!-- original page 108 -->

is local; so `(5.6.3, (iv))` `𝒪_{X,x}` is universally catenary. To prove that `X` satisfies condition 3°, consider
several cases:

(a) `X` is a closed irreducible subprescheme of `S`; let `S'` be an irreducible component of `S` containing `X`, `ξ` the
generic point of `X`, `x` a closed point of `X`; for every `s ∈ S'`, `𝒪_{S',s}`, a quotient of `𝒪_{S,s}`, is catenary
`(5.6.1)`, so conditions 2° and 3° entail that `S'` is biequidimensional `(0, 14.3.3)`. By virtue of `(5.1.2)` and
`(0, 14.3.3.2)`, one therefore has

```text
  dim(𝒪_{X,x}) = dim(𝒪_{S,x}) − dim(𝒪_{S,ξ}) = dim(S') − dim(𝒪_{S,ξ})
```

which shows that `dim(𝒪_{X,x})` does not depend on the closed point `x` considered, whence the assertion in this case
`(5.1.4)`.

(b) `X` is irreducible and `g` dominant. Then, for every closed point `x` of `X`, `g(x)` is closed in `S` by `(10.4.7)`;
since `𝒪_{S,g(x)}` is universally catenary, it follows from `(5.6.5.3)` that one has

```text
  dim(𝒪_{X,x}) = dim(𝒪_{S,g(x)}) + e
```

where `e = dim(g⁻¹(ζ))`, `ζ` being the generic point of `S`. Since `dim(S) = dim(𝒪_{S,s})` by virtue of condition 3° for
`S`, one has `dim(𝒪_{X,x}) = dim(S) + e` for every closed point `x ∈ X`; this proves condition 3° for `X` `(5.1.4)`, and
at the same time the formula

```text
(10.6.1.4)        dim(X) = dim(S) + e.
```

(c) General case. Considering a reduced subprescheme `X'` of `X` having an irreducible component of `X` as underlying
space, one is reduced to the case where `X` is integral; using `(I, 5.2.2)` and case (a) proved above, one may then
replace `S` by the reduced subprescheme having `g(X)` as underlying space; one is then reduced to case (b), and this
completes the proof of (i).

(ii) The morphism `f` being locally of finite type `(1.3.4)`, one may apply the results of (i) replacing `S` by `Y`;
moreover, since `X` is irreducible and `f` dominant, one may also replace `S` by `Y` in `(10.6.1.4)`, which gives
`(10.6.1.1)`.

(iii) The assertion concerning the case where `dim(f⁻¹(y)) ⩽ n` for every `y ∈ Y` has already been proved under more
general hypotheses in `(5.6.7)`. Suppose that `dim(f⁻¹(y)) ⩾ n` for every `y ∈ Y`, and consider a generic point `η` of
an irreducible component `Y'` of `Y`; there exists at least one irreducible component `Z` of `f⁻¹(η)` of dimension
`⩾ n`; if `ξ` is the generic point of `Z`, then `ξ` is also the generic point of an irreducible component `X'` of `X`
such that `f(X')` is dense in `Y'` `(0_I, 2.1.8)`. Consider the reduced subpreschemes of `X`, `Y` having respectively
`X'`, `Y'` as underlying spaces, and the restriction `X' → Y'` of `f` `(I, 5.2.2)`; it then follows from (ii) that
`dim(X') ⩾ dim(Y') + n`, and a fortiori `dim(X) ⩾ dim(Y') + n`; this being true for every irreducible component `Y'` of
`Y`, one concludes the inequality `(10.6.1.2)`.

**Corollary (10.6.2).**

<!-- label: IV.10.6.2 -->

*Suppose that `X` satisfies conditions 1°, 2°, and 3° of `(10.6.1)`. Then, for every open `U` dense in `X`, one has
`dim(U) = dim(X)`.*

<!-- original page 109 -->

One knows in fact that `dim(U) ⩽ dim(X)` `(0, 14.1.4)`; moreover, since `X` is a Jacobson prescheme, `U` contains a
closed point of every irreducible component of `X`, so `dim(U) = dim(X)` by virtue of `(10.6.1)` and `(0, 14.1.2.1)`.

**Proposition (10.6.3).**

<!-- label: IV.10.6.3 -->

*Suppose that `X` satisfies conditions 1°, 2°, and 3° of `(10.6.1)`, and let `Y` be a closed subset of `X`. Then, for
every `x ∈ Y`, and every open neighbourhood `U` of `x` in `X` not meeting the irreducible components of `Y` which do not
contain `x`, one has*

```text
(10.6.3.1)        dim(U) = sup_i dim(U ∩ Y_i) = sup_i dim(Y_i) = dim_x(X)
```

*where `Y_i` (`1 ⩽ i ⩽ m`) are the irreducible components of `Y` containing `x`.*

By considering a closed subprescheme of `X` having `Y` as underlying space, we may restrict, by virtue of
`(10.6.1, (i))`, to the case where `Y = X`. By the choice of `U`, `U` is the union of the `U ∩ X_i`, so
`dim(U) = sup_i dim(U ∩ X_i)`; but by `(10.6.2)` applied to a closed subprescheme of `X` having `X_i` as underlying
space, one has (taking `(10.6.1, (i))` into account) `dim(U ∩ X_i) = dim(X_i)`; this proves that the second and fourth
terms of `(10.6.3.1)` are equal. Since `U ∩ X_i` is biequidimensional `(10.6.1, (i))` (since the immersion
`U ∩ X_i → X_i` is of finite type `(I, 6.3.5)`), one has

```text
(10.6.3.2)        dim(U ∩ X_i) = dim(U ∩ ‾{x}) + codim(‾{x}, X_i)
```

`(0, 14.3.5)`. By `(10.6.2)` applied to a closed subprescheme of `X` having `‾{x}` as underlying space,
`dim(U ∩ ‾{x}) = dim(‾{x})`; since one also has, for the same reasons,

```text
(10.6.3.3)        dim(X_i) = dim(‾{x}) + codim(‾{x}, X_i)
```

one obtains

```text
  dim(U) = dim(‾{x}) + sup_i codim(‾{x}, X_i) = dim(‾{x}) + codim(‾{x}, X)
```

by definition of codimension `(0, 14.2.1)`. This shows that `dim(U)` is independent of the open neighbourhood `U` of `x`
satisfying the conditions of the statement, hence is equal to `dim_x(X)`, by `(0, 14.1.4.1)`.

**Corollary (10.6.4).**

<!-- label: IV.10.6.4 -->

*Under the hypotheses of `(10.6.3)`, let `ℱ` be a coherent `𝒪_X`-Module, `Y` its support. For every `x ∈ Y`, one has*

```text
(10.6.4.1)        dim(‾{x}) + dim(ℱ_x) = dim_x(Y).
```

Indeed, this follows from `(10.6.3.1)` and from the formula `dim(ℱ_x) = codim(‾{x}, Y)` `(5.1.12.2)`.

### 10.7. Examples and counterexamples

**(10.7.1)**

<!-- label: IV.10.7.1 -->

Let `S` be a locally Noetherian prescheme of dimension `⩾ 1` and suppose that `S` is a Jacobson prescheme; when `S` is
Noetherian, this amounts to saying that the irreducible components of `S` of dimension `1` are infinite, for every
`x ∈ S` that is not closed is the generic point of such a component `(10.4.5 and 10.5.4)`. Then `S` also satisfies
conditions 2° and 3° of `(10.6.1)`: indeed, every local ring `𝒪_{S,s}` is of dimension `0` or `1`, and consequently is
universally catenary `(7.2.9)`; on the other hand, an irreducible component `S'` of `S` is either reduced

<!-- original page 110 -->

to a point or of dimension `1`, and for every closed point `s ∈ S'`, `𝒪_{S',s}` is necessarily of dimension `1`.

One deduces from these remarks and from `(10.6.1)` that every prescheme locally of finite type over `S` also satisfies
properties 1°, 2°, and 3° of `(10.6.1)`: this is so in particular for preschemes locally of finite type over a field or
over `ℤ`.

**(10.7.2)**

<!-- label: IV.10.7.2 -->

Let `A` be a local Noetherian universally catenary ring and let `S` be the complement in `X = Spec(A)` of the closed
point `a`. Then `S` satisfies conditions 1°, 2°, and 3° of `(10.6.1)`: indeed, it was already seen that `S` is a
Jacobson prescheme `(10.5.9)`; since `A` is universally catenary, so are the local rings `A_𝔭` at the prime ideals of
`A` `(5.6.3)`. On the other hand, an irreducible component `S'` of `S` is the complement of `a` in an irreducible
component `X'` of `X`; for every closed point `x` of `S`, the closure of `x` in `X` is therefore `{x, a}`, in other
words `dim(‾{x}) = 1` and consequently, since `X'` is by hypothesis biequidimensional `(0, 14.3.3)`, one has
`dim(𝒪_{X',x}) = dim(X') − 1` `(0, 14.3.2)`, which proves that `S'` is equicodimensional `(5.1.4)`.

**(10.7.3)**

<!-- label: IV.10.7.3 -->

Let `A` be a discrete valuation ring; let us show that in the ring `B = A[T_1, …, T_n]` of polynomials in `n`
indeterminates, there exist two maximal ideals `𝔪`, `𝔫` of heights `n` and `n + 1` respectively. This was seen in
`(5.2.5, (i))` for `n = 1`; let us prove it by induction on `n`. Since `A[T_1, …, T_{n+1}]` is a free
`A[T_1, …, T_n]`-module, hence faithfully flat, there are in `A[T_1, …, T_{n+1}]` two maximal ideals `𝔪'`, `𝔫'` lying
respectively over `𝔪` and `𝔫` `(0_I, 6.5.1)`; moreover, according to `(5.5.3)`, these ideals are necessarily of heights
`n + 1` and `n + 2` respectively, whence our assertion. Assume `n ⩾ 2` in what follows. Let `𝔍` be the ideal
`𝔪 ∩ 𝔫 = 𝔪𝔫`, and `R = 1 + 𝔍`, which is a multiplicative subset of `B`; if one sets `B' = R⁻¹B`, the ideal `𝔍' = R⁻¹𝔍`
is contained in the radical of `B'` `(Bourbaki, Alg. comm., chap. III, §3, n° 5, prop. 12)`; one knows that
`X' = Spec(B')` is identified as a topological space with a subspace of `X = Spec(B)`, and that at the points `x` of
`X'`, the local rings `𝒪_{X,x}` and `𝒪_{X',x}` are the same `(I, 1.6.2)`. Consider then in `X'` the closed set
`Y' = V(𝔍')`, and set `S = X' − Y'`; one knows `(10.5.7)` that `S` is a Jacobson prescheme, obviously irreducible and
Noetherian; moreover the local rings `𝒪_{S,s} = 𝒪_{X,s}` are universally catenary for every `s ∈ S` by virtue of
`(5.6.3)`, since `A` is universally catenary `(5.6.4)`. Yet there are two closed points `a`, `b` of `S` such that
`𝒪_{S,a}` and `𝒪_{S,b}` do not have the same dimension, in other words `S` does not satisfy condition 3° of `(10.6.1)`.
To see this, consider the two maximal ideals `𝔪' = R⁻¹𝔪`, `𝔫' = R⁻¹𝔫` of `B'`, which are of heights `n` and `n + 1`
respectively; one has `𝔍' = 𝔪' ∩ 𝔫'`, and `𝔍'` is therefore contained in no prime ideal of `B'` distinct from `𝔪'` and
`𝔫'`, which are consequently the only maximal ideals of `B'`. Let `a'`, `b'` be the only closed points of `X'`,
corresponding to `𝔪'` and `𝔫'`. There exists in `B'` a non-maximal prime ideal `𝔭' ⊂ 𝔪'` which is not contained in `𝔫'`:
it suffices to show that there is in `B` a non-maximal prime ideal contained in `𝔪` and not in `𝔫`; for this, one may
for example consider the fibre of `𝔪` for the morphism corresponding to the injection `A[T_1] → B = A[T_1, …, T_n]`, and
apply `(6.1.2)`. By considering a maximal chain of prime ideals between `𝔭'` and `𝔪'` and replacing `𝔭'` by the
next-to-last ideal of this chain, one may therefore suppose that the point `a` of `X'` corresponding to `𝔭'` is such
that its closure in `X'` is `{a, a'}`; since `B'_{𝔪'}` is biequidimensional, `𝔭'` is then of height `n − 1`. One
constructs in the same way a non-maximal prime ideal `𝔮'` of `B'` of height `n`, such that if `b` is the corresponding
point of `X'`, the closure of `b` in `X'` is `{b, b'}`. This being so, `a` and `b` are in `S`, hence closed in `S`, and
consequently answer the question.

### 10.8. Rectified depth

**Definition (10.8.1).**

<!-- label: IV.10.8.1 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. For every `x ∈ X`, one calls **rectified
depth** of `ℱ` at the point `x`, and one denotes by `prof*_x(ℱ)`, the number (integer `⩾ 0` or `+∞`) equal to*

```text
(10.8.1.1)        prof*_x(ℱ) = prof(ℱ_x) + dim(‾{x})
```

*where `‾{x}` is the closure of the point `x` in `X`. For every subset `Z` of `X`, one calls **rectified depth** of `ℱ`
along `Z`, and one denotes by `prof*_Z(ℱ)`, the number*

```text
(10.8.1.2)        prof*_Z(ℱ) = inf_{x ∈ Z} prof*_x(ℱ).
```

In other words, for every integer `n`, the relation `prof*_Z(ℱ) ⩾ n` is equivalent to `prof*_x(ℱ) ⩾ n` for every
`x ∈ Z`. If `Z = X`, one writes `prof*(ℱ)` instead of `prof*_X(ℱ)`.

<!-- original page 111 -->

**Remarks (10.8.2).**

<!-- label: IV.10.8.2 -->

(i) At every closed point `x ∈ X`, the rectified depth is equal to the depth.

(ii) Let `Y` be a closed subprescheme of `X`, `j : Y → X` the canonical injection, `𝒢` a coherent `𝒪_Y`-Module. One
knows `(5.7.3, (vi))` that `prof(𝒢_x) = prof((j_*(𝒢))_x)` for every `x ∈ Y`; one deduces that one also has
`prof*_x(𝒢) = prof*_x(j_*(𝒢))` for every `x ∈ Y`.

(iii) The notion of rectified depth is of interest only when it is of local character, that is, when it does not change
on replacing `X` by an arbitrary open neighbourhood `U` of `x`. This evidently requires that `x` not be isolated in
`‾{x}` when `x` is not closed, and consequently that `X` be a Jacobson prescheme `(10.4.5.1)`; most often, it will also
be necessary to know that `dim(U) = dim(X)` for every open `U` dense in `X`, and one will therefore have to suppose that
`X` also satisfies conditions 2° and 3° of `(10.6.1)`.

**Lemma (10.8.3).**

<!-- label: IV.10.8.3 -->

*Let `X` be a regular and biequidimensional prescheme, `ℱ` a coherent `𝒪_X`-Module. Then one has, for every `x ∈ X`,*

```text
(10.8.3.1)        prof*_x(ℱ) = dim(X) − dim. proj(ℱ_x).
```

Indeed, since `X` is biequidimensional, one has `(0, 14.3.5.1)`

```text
  dim(‾{x}) = dim(X) − codim(‾{x}, X) = dim(X) − dim(𝒪_{X,x})
```

by virtue of `(5.1.2)`. On the other hand, since `X` is regular, one has by `(0, 17.3.4)`

```text
  prof(ℱ_x) = dim(𝒪_{X,x}) − dim. proj(ℱ_x)
```

whence the lemma.

**Corollary (10.8.4).**

<!-- label: IV.10.8.4 -->

*Under the hypotheses of `(10.8.3)`, the function `x ↦ prof*_x(ℱ)` is lower semi-continuous.*

This follows from `(10.8.3.1)`, since `x ↦ dim. proj(ℱ_x)` is upper semi-continuous `(6.11.1)`.

**Proposition (10.8.5).**

<!-- label: IV.10.8.5 -->

*Let `S` be a locally Noetherian prescheme, `X` a prescheme locally of finite type over `S`, `ℱ` a coherent
`𝒪_X`-Module. Suppose that `S` satisfies the following conditions: 1° `S` is a Jacobson prescheme; 2° `S` is regular; 3°
the irreducible components of `S` are equicodimensional. Then the function `x ↦ prof*_x(ℱ)` is lower semi-continuous in
`X`; in other words, for every integer `n`, the set `U_n` of `x ∈ X` such that `prof*_x(ℱ) ⩾ n` is open.*

Since the local rings `𝒪_{S,s}` of `S` are regular, they are universally catenary `(5.6.4)`; in other words, `S`
satisfies conditions 1°, 2°, and 3° of `(10.6.1)`, so the same holds for `X` `(10.6.1, (i))`. The notion of rectified
depth then being of local character `(10.8.2, (iii))`, one may restrict to the case where `S = Spec(A)` and
`X = Spec(B)` are affine, `A` being a regular ring and `B` an `A`-algebra of finite type, hence a quotient of a
polynomial ring `C = A[T_1, …, T_n]`, and the latter is regular `(0, 17.3.7)`. One may therefore suppose that `X` is a
closed subprescheme of a regular prescheme `Y` also satisfying conditions 1°, 2°, and 3° of `(10.6.1)`; taking remark
`(10.8.2, (ii))` into account, one is thus reduced to the case where `X` is in addition regular and Noetherian. But
since the local rings of `X` are then integral, the irreducible components of `X` are

<!-- original page 112 -->

open `(I, 6.1.10)`, and one may consequently also suppose `X` irreducible. Then, since the local rings of `X` are
catenary `(0, 16.5.12)`, hypothesis 3° of `(10.6.1)` entails that `X` is biequidimensional (`(5.1.5)` and
`(0, 14.3.3)`); it therefore suffices to apply `(10.8.4)`.

One notes that if `S` is the spectrum of a field or of `ℤ`, it satisfies the conditions of `(10.8.5)`.

**Corollary (10.8.6).**

<!-- label: IV.10.8.6 -->

*Under the hypotheses of `(10.8.5)`, for every `x ∈ X`, the number `prof*_x(ℱ)` is the unique integer `n` having the
following property: there exists an open neighbourhood `U` of `x` in `X` such that for every point `x' ∈ U ∩ ‾{x}`,
closed in `U`, one has `prof(ℱ_{x'}) = n`. In particular, for `prof*_x(ℱ) ⩾ m` (resp. `prof*_x(ℱ) ⩽ m`), it is necessary
and sufficient that there exist an open neighbourhood `V` of `x` in `X` such that, for every `x' ∈ V ∩ ‾{x}`, closed in
`V`, one has `prof(ℱ_{x'}) ⩾ m` (resp. `prof(ℱ_{x'}) ⩽ m`).*

Indeed, one may restrict to the case where `x` is not closed; if `prof*_x(ℱ) = n`, the set of `y ∈ X` such that
`prof*_y(ℱ) < n` is closed by virtue of `(10.8.5)`, so contains `‾{x}`; and by virtue of the lower semi-continuity of
`y ↦ prof*_y(ℱ)`, there exists an open neighbourhood `U` of `x` such that `prof*_y(ℱ) = n` for every `y ∈ U ∩ ‾{x}`,
hence `prof(ℱ_{x'}) = n` if `x' ∈ U ∩ ‾{x}` is closed in `U` (since the notion of rectified depth is local).

For preschemes satisfying the hypotheses of `(10.8.5)`, the notion of rectified depth can therefore be defined by means
of the values of the depth at the closed points of `X` (the latter forming a very dense set in every closed part of
`X`).

**Proposition (10.8.7).**

<!-- label: IV.10.8.7 -->

*Let `S` be a locally Noetherian prescheme satisfying conditions 1°, 2°, and 3° of `(10.6.1)`. Let `X` be a prescheme
locally of finite type over `S`, `ℱ` a coherent `𝒪_X`-Module, `Y = Supp(ℱ)`. Then, for every `x ∈ Y`, one has*

```text
(10.8.7.1)        prof*_x(ℱ) = dim_x(Y) − coprof(ℱ_x).
```

Indeed, by definition, one has `coprof(ℱ_x) = dim(ℱ_x) − prof(ℱ_x)`, and it follows from `(10.6.4)` that one has
`dim_x(Y) = dim(‾{x}) + dim(ℱ_x)`; whence `(10.8.7.1)` by definition of `prof*_x(ℱ)`.

**Corollary (10.8.8).**

<!-- label: IV.10.8.8 -->

*The hypotheses on `f` and `ℱ` being those of `(9.9.1)`, the function `x ↦ prof*_x(ℱ_{f(x)})` is constructible.*

Note that for every `s ∈ S`, the fibre `X_s` being a prescheme locally of finite type over `k(s)`, is a Jacobson
prescheme `(10.4.7)`; since in addition `Spec(k(s))` satisfies the conditions of `(10.6.1)`, one has
`prof*_x(ℱ_{f(x)}) = dim_x(Supp(ℱ_{f(x)})) − coprof((ℱ_{f(x)})_x)` `(10.8.7)`. Now, if `Z = Supp(ℱ)`, one has
`Z_{f(x)} = Supp(ℱ_{f(x)})` `(I, 9.1.13)` and `Z` is locally constructible `(8.9.1)`; so the functions
`x ↦ dim_x(Supp(ℱ_{f(x)}))` and `x ↦ coprof((ℱ_{f(x)})_x)` are locally constructible (`(9.9.1)` and `(9.9.3)`), which
proves the proposition.

### 10.9. Maximal spectra and ultra-preschemes

*The results of this number will not be used in what follows.*

**(10.9.1)**

<!-- label: IV.10.9.1 -->

Let `X` be a Jacobson prescheme, and let `S(X)` be the ringed space whose underlying space is the subspace of closed
points of `X`, and whose sheaf of rings is the sheaf induced on this subspace by `𝒪_X`, in other words the sheaf of
rings `ψ*(𝒪_X)`, where `ψ : S(X) → X` denotes the canonical injection. Since `ψ` is a quasi-

<!-- original page 113 -->

homeomorphism, it was seen `(10.2.8, (ii))` that if `θ : 𝒪_X → ψ_*(𝒪_{S(X)})` is the homomorphism of sheaves of rings
such that `θ♯ : ψ*(𝒪_X) → 𝒪_{S(X)}` is the identity, then `j_X = (ψ, θ)` is a quasi-isomorphism of ringed spaces, and
`ℱ ↦ ψ*(ℱ)` an equivalence of the category of `𝒪_X`-Modules and that of `𝒪_{S(X)}`-Modules. It is clear that in this
equivalence, locally free (resp. coherent) `𝒪_X`-Modules correspond to locally free (resp. coherent) `𝒪_{S(X)}`-Modules;
in addition, if `ℱ` is a locally free `𝒪_X`-Module and `U` is an open of `X` such that `ℱ|U` is isomorphic to
`(𝒪_X|U)^n`, `ψ*(ℱ)` is such that `ψ*(ℱ)|(U ∩ S(X))` is isomorphic to `(𝒪_{S(X)}|(U ∩ S(X)))^n`.

**(10.9.2)**

<!-- label: IV.10.9.2 -->

Let `X`, `Y` be two Jacobson preschemes and `f = (φ, λ) : X → Y` a morphism locally of finite type. It was seen
`(10.4.7)` that `φ(S(X)) ⊂ S(Y)`, and by restriction of `φ` to `S(X)`, one therefore defines a continuous map
`S(φ) : S(X) → S(Y)`. On the other hand, for every open `V` of `Y`, one defines by composition a ring homomorphism

```text
  Γ(V ∩ S(Y), 𝒪_{S(Y)}) → Γ(V, 𝒪_Y) → Γ(f⁻¹(V), 𝒪_X) → Γ(f⁻¹(V) ∩ S(X), 𝒪_{S(X)})
```

where the two extreme isomorphisms have been defined in `(10.9.1)`; it is clear that this defines a homomorphism of
sheaves of rings `S(λ) : 𝒪_{S(Y)} → S(φ)_*(𝒪_{S(X)})` (recalling that the open sets of `S(X)` (resp. `S(Y)`) correspond
bijectively to those of `X` (resp. `Y`) `(10.2.1)`); one thus obtains a morphism of ringed spaces
`S(f) = (S(φ), S(λ)) : (S(X), 𝒪_{S(X)}) → (S(Y), 𝒪_{S(Y)})` such that the diagram

```text
              S(f)
       S(X) ———→ S(Y)
        │           │
    j_X │           │ j_Y
        ↓           ↓
        X  ———→   Y
              f
```

is commutative; in addition, if `Z` is a third Jacobson prescheme and `g : Y → Z` a morphism locally of finite type, it
is clear that `S(g ∘ f) = S(g) ∘ S(f)`. One has thus defined a covariant functor `S : 𝒞 → 𝒞'`, where `𝒞'` is the
category of ringed spaces in local rings, and `𝒞` the category whose objects are the Jacobson preschemes and whose
morphisms are the morphisms locally of finite type between Jacobson preschemes.

**(10.9.3)**

<!-- label: IV.10.9.3 -->

Let us propose to determine the subcategory `𝒞''` of `𝒞'` formed by the ringed spaces isomorphic to the `S(X)` and whose
morphisms come from the `S(f)`. Suppose first that `X = Spec(A)`, where `A` is a Jacobson ring; then `S(X)` is the set
of maximal ideals of `A`, equipped with: 1° the topology induced by that of `X`, so that a base of this topology is
formed by the `D_𝔪(h) = D(h) ∩ S(X)`, the set of maximal ideals `𝔪` of `A` such that `h ∉ 𝔪`, where `h` runs through
`A`; 2° the sheaf of rings `𝒪_{S(X)}` such that `Γ(D_𝔪(h), 𝒪_{S(X)}) = A_h`. We shall say that this ringed space is the
**maximal spectrum** of the Jacobson ring `A` and we shall denote it by `Spm(A)`.

Note that if `j : D(h) → X` is the canonical injection, the ringed space induced on `D_𝔪(h)` by `S(X)` is `S(D(h))` and
the canonical injection `D_𝔪(h) → S(X)` of ringed spaces is equal to `S(j)`.

Let `B` be a second Jacobson ring, `Y = Spec(B)`, `φ : B → A` a ring homomorphism making `A` a `B`-algebra of finite
type, `f = (ᵃφ, ᵃφ̃) : X → Y` the corresponding morphism of preschemes, and

```text
  S(f) : Spm(A) → Spm(B)
```

the morphism of ringed spaces corresponding to `f`. It is clear that `S(f) = (ψ, θ)` is a morphism of ringed spaces in
local rings, that is `(Err_III, 1.8.2)` that for every `x ∈ Spm(A)`, `θ^♯_x` is a local homomorphism. Conversely:

**Proposition (10.9.4).**

<!-- label: IV.10.9.4 -->

*Let `A`, `B` be two Jacobson rings. If `u = (ψ, θ) : Spm(A) → Spm(B)` is a morphism of ringed spaces in local rings
such that `Γ(θ) : B → A` makes `A` a `B`-algebra of finite type, there exists a morphism of preschemes
`f : Spec(A) → Spec(B)` and only one such that `u = S(f)`.*

The uniqueness of `f` is evident, since if `f = (ᵃφ, ᵃφ̃)`, one must have `φ = Γ(θ)`; it remains to see that `S(f)` is
defined and that one has `u = S(f)`. Now, the first assertion follows from the fact that `φ` is assumed to make `A` a
`B`-algebra of finite type, and consequently `f(Spm(A)) ⊂ Spm(B)`; the fact that `θ^♯_x` is a local homomorphism for
every `x ∈ Spm(A)` then allows one to repeat the argument of `(I, 1.7.3)` while restricting to the points `x` of
`Spm(A)`: one thus shows successively that `ψ(x) = ᵃφ(x)` for every `x ∈ Spm(A)`, then that
`θ^♯_x = φ_x : B_{ψ(x)} → A_x`, which completes the proof that `u = S(f)`.

<!-- original page 114 -->

**(10.9.5)**

<!-- label: IV.10.9.5 -->

Let us now consider a ringed space `(X, 𝒪_X)`; we shall say that an open subset `U` of `X` is **ultra-affine** if the
induced ringed space `(U, 𝒪_X|U)` is isomorphic to a maximal spectrum `Spm(A)`, where `A` is a Jacobson ring. We shall
say that `X` is an **ultra-prescheme** if every point of `X` admits an ultra-affine open neighbourhood. One shows, as in
`(I, 2.1.3 and 2.1.4)`, that the ultra-affine open sets form a base of the topology of `X` and that `X` is a Kolmogorov
space. If `Y` is a second ultra-prescheme, we shall say that a morphism of ringed spaces `f : X → Y` is a *morphism of
ultra-preschemes* if it satisfies the following conditions: 1° `f` is a morphism of ringed spaces in local rings; 2° for
every `x ∈ X`, there is an ultra-affine open neighbourhood `V` of `f(x)` in `Y` and an ultra-affine open neighbourhood
`U` of `x` in `X` such that `f(U) ⊂ V` and such that the homomorphism `Γ(V, 𝒪_Y) → Γ(U, 𝒪_X)` corresponding to `f` makes
`Γ(U, 𝒪_X)` a `Γ(V, 𝒪_Y)`-algebra of finite type.

It is immediate that one thus defines morphisms, the composite of two morphisms being a third thanks to the final remark
of `(10.9.3)`. It is clear that the category `𝒞''_0` thus defined is a subcategory of `𝒞'` which contains `𝒞''`; we
propose to show that `𝒞'' = 𝒞''_0`, in other words:

**Proposition (10.9.6).**

<!-- label: IV.10.9.6 -->

*The functor `X ↦ S(X)` from `𝒞` to `𝒞''_0` is an equivalence of categories.*

1° Let us first show that the functor `X ↦ S(X)` is fully faithful, in other words that for `X`, `Y` in `𝒞`, the
canonical map

```text
  Hom_𝒞(X, Y) → Hom_{𝒞''_0}(S(X), S(Y))
```

is bijective. First, it is injective: let `f`, `g` be two morphisms locally of finite type from `X` to `Y` and suppose
that `S(f) = S(g)`. This entails first that for every open `V` of `Y`, one has `f⁻¹(V) ∩ S(X) = g⁻¹(V) ∩ S(X)`, hence
(`(10.3.1)` and `(10.2.7)`) `f⁻¹(V) = g⁻¹(V)`; it therefore suffices to prove that for every affine open `V` of `Y`, `f`
and `g` coincide in `f⁻¹(V) = g⁻¹(V)`, in other words one is reduced to the case where `Y = Spec(B)` is the spectrum of
a Jacobson ring `B`. It suffices `(I, 2.2.4)` to show that the ring homomorphisms `B → Γ(X, 𝒪_X)` corresponding to `f`
and `g` are then the same. Now, for every `s ∈ B`, the images of `s` under these homomorphisms are two sections of `𝒪_X`
over `X` which, by hypothesis, induce the same section over `S(X)`; one knows therefore `(10.2.8)` that these sections
are identical, whence our assertion. Let us prove secondly that every morphism `h : S(X) → S(Y)` (for the category
`𝒞''_0`) is of the form `S(f)`, where `f : X → Y` is a morphism locally of finite type. By hypothesis, there exists an
ultra-affine open cover `(U'_λ)` (resp. `(V'_λ)`) of `S(X)` (resp. `S(Y)`) such that for every `λ`, `h(U'_λ)` is
contained in some `V'_λ` and there corresponds to the morphism `h_λ : U'_λ → V'_λ`, restriction of `h`, a ring
homomorphism `Γ(V'_λ, 𝒪_{S(Y)}) → Γ(U'_λ, 𝒪_{S(X)})` making the second ring an algebra of finite type over the first.
One may suppose that `U'_λ = U_λ ∩ S(X)` and `V'_λ = V_λ ∩ S(Y)`, where `U_λ` and `V_λ` are affine open sets uniquely
determined in `X` and `Y` respectively; if one shows that, for every `λ`, `h_λ = S(f_λ)` where `f_λ : U_λ → V_λ` is a
morphism of finite type, then it follows from the first part of the argument, applied to the restrictions of `f_α` and
`f_β` to `U_α ∩ U_β`, that the `f_λ` are the restrictions of a single morphism `f : X → Y`, and one will evidently have
`h = S(f)`. One is thus reduced to the case where `X` and `Y` are affine, and the conclusion then follows from
`(10.9.4)`.

2° It remains to prove that every ultra-prescheme `X'` is of the form `S(X)` for a Jacobson prescheme `X` (which will
necessarily be unique up to isomorphism, by virtue of 1°). There is a cover `(U'_α)` of `X'` by ultra-affine open sets,
each of which is of the form `S(U_α)`, `U_α` being the spectrum of a Jacobson ring. For every pair of indices `α`, `β`,
consider the unique open `U_{αβ}` of `U_α` whose trace on `U'_α` is `U'_α ∩ U'_β`; by virtue of 1°, the identity
automorphism of `U'_α ∩ U'_β` is of the form `S(θ_{αβ})`, where `θ_{αβ} : U_{αβ} → U_{βα}` is an isomorphism of
preschemes. One verifies immediately (by virtue of 1°) that the family `(θ_{αβ})` satisfies the gluing condition
`(0_I, 4.1.7)`, and that this family therefore defines a prescheme `X`, in which the `U_α` are identified with affine
open sets; it is then clear that one has `X' = S(X)`, which completes the proof.

### 10.10. Serre algebraic spaces

**(10.10.1)**

<!-- label: IV.10.10.1 -->

The language introduced by Serre in `(FAC)` is sometimes convenient, in particular in questions where the main interest
attaches to the points rational over the base field `k` (algebraically closed by hypothesis) of the "algebraic
varieties" over `k` that one considers. We shall sketch this language here while connecting it to the foregoing
considerations, to enable the reader to translate Serre's statements into the language of schemes. It is in fact
possible to develop Serre's language also for preschemes over a non-algebraically-closed field (and even over an
Artinian ring); but this introduces considerable technical complications, and besides,

<!-- original page 115 -->

over an arbitrary base field, the (mainly psychological) advantages of Serre's viewpoint disappear; we shall therefore
confine ourselves to the framework fixed by Serre. The present number, like the preceding one, will not be used in the
remainder of this Treatise, and we shall therefore confine ourselves to brief indications.

**(10.10.2)**

<!-- label: IV.10.10.2 -->

Given a fixed ultra-prescheme `R`, one may naturally (as in any category) define the notion of *`R`-ultra-prescheme*.
Consider in particular an algebraically closed field `k`; `Spm(k)` is then identical with `Spec(k)`; we shall say that a
`Spm(k)`-ultra-prescheme `X'` is a **pre-algebraic space** over `k`: it is therefore a `k`-ringed space in local rings
each point of which has an open neighbourhood isomorphic to the maximal spectrum of a `k`-algebra of finite type; this
amounts to saying (by `(10.9.6)`) that `X' = S(X)`, where `X` is a prescheme locally of finite type over `k`. If `X`,
`Y`, `Z` are three `k`-preschemes locally of finite type, so is `X ×_Z Y` `(1.3.4)`, so by virtue of `(10.9.6)`, the
notion of product exists in the category of pre-algebraic spaces over `k` (both the product "over `k`" `X' ×_k Y'` and
the "fibre product" `X' ×_{Z'} Y'`, where `X'`, `Y'`, `Z'` are three pre-algebraic spaces over `k`). One may therefore
define the diagonal morphism `Δ_{X'} : X' → X' ×_k X'` (which is moreover none other than `S(Δ_X)`); one says that `X'`
is an **algebraic space** over `k` if `X` is a scheme, and this amounts to saying that the image of `Δ_{X'}` is a closed
subset of `X' ×_k X'`.

**(10.10.3)**

<!-- label: IV.10.10.3 -->

The simplifications coming from the hypothesis that `k` is algebraically closed are first that, for a `k`-prescheme `X`
locally of finite type, there is a bijective correspondence between closed points of `X`, points of `X` with values in
`k` `(I, 3.4.4)`, and points of `X` rational over `k` `(I, 3.4.5)`, by virtue of `(I, 6.4.2)`. This shows in particular
(by virtue of `(I, 3.4.3.1)`) that for two `k`-pre-algebraic spaces `X'`, `Y'`, the underlying set of the product
`X' ×_k Y'` is identical with the *product set* `X' × Y'` of the underlying sets (but of course the topology of the
space underlying `X' ×_k Y'` is not the product topology of the topologies of the spaces underlying `X'` and `Y'`; it is
in general strictly finer than the latter).

On the other hand, the local rings `𝒪_x` at the points of a pre-algebraic space `X'` over `k` are `k`-algebras whose
residue field has just been seen to be isomorphic to `k`; if `A` and `B` are two such local `k`-algebras, every
`k`-homomorphism `φ : A → B` is necessarily local: indeed, if an element `x` of the maximal ideal of `A` were such that
`φ(x)` is invertible, there would exist `λ ∈ k` non-zero such that `φ(x − λ · 1)` belongs to the maximal ideal of `B`,
which is absurd since `x − λ · 1` is invertible in `A`. One concludes immediately that if `X' = S(X)`, `Y' = S(Y)` are
two pre-algebraic spaces over `k`, every morphism `X' → Y'` of `k`-ringed spaces is also a morphism of `k`-ringed spaces
in local rings `(I, 1.8.2; cf. Err_III)`. Moreover, with the preceding notation, if `A` and `B` are `k`-algebras of
finite type, `φ` makes `B` an `A`-algebra of finite type; so every morphism `X' → Y'` of `k`-ringed spaces is, by virtue
of `(10.9.6)`, of the form `S(f)`, where `f : X → Y` is a morphism of `k`-preschemes.

Finally, for every open `U` of `X'`, every section `s ∈ Γ(U, 𝒪_{X'})`, and every `x ∈ U`, `s(x)` `(0_I, 5.5.1)` is
identified with an element of `k`, and one has thus associated to `s` a map `s̃ : x ↦ s(x)` from `U` to `k`, in other
words a section over `U` of the sheaf `𝒜(X')` of germs of maps from `X'` to `k`; since the map `h_U : s ↦ s̃` is
evidently a ring homomorphism `Γ(U, 𝒪_{X'}) → Γ(U, 𝒜(X'))` and commutes with restrictions to an open `V ⊂ U`, the `h_U`
define a homomorphism of sheaves of rings `h : 𝒪_{X'} → 𝒜(X')`. If one takes for `U` an ultra-affine open `Spm(A)`,
where `A` is a Jacobson ring, to say that `s̃ = 0` means that for every maximal ideal `𝔪` of `A`, `s` belongs to `𝔪`, or
equivalently that `s` is in the radical of `A`; but since `A` is a Jacobson ring, its radical is equal to its
nilradical; for `h_U` to be injective, it is therefore necessary and sufficient that `A` be reduced.

**(10.10.4)**

<!-- label: IV.10.10.4 -->

One says that the `k`-pre-algebraic space `X' = S(X)` is **reduced** if `X` is so; since the set of points `x ∈ X` where
`X` is reduced is open `(0_I, 5.2.2)`, its complement contains at least one closed point if it is non-empty `(5.1.11)`,
and it therefore amounts to the same to say that `X'` is reduced or that each of its local rings `𝒪_x` (for `x ∈ X'`) is
reduced. It was just seen in `(10.10.3)` that for the homomorphism `h : 𝒪_{X'} → 𝒜(X')` to be injective, it is necessary
and sufficient that `X'` be reduced. In `(FAC)`, Serre in fact restricts to reduced pre-algebraic spaces, which allows
him to define `𝒪_{X'}` as a subsheaf of `𝒜(X')`. Note that if `X'` and `Y'` are reduced `k`-pre-algebraic spaces, so is
`X' ×_k Y'`: indeed, everything reduces to seeing that if `A` and `B` are two reduced `k`-algebras of finite type, so is
`A ⊗_k B`; but we have seen that the radicals of `A` and `B` are then reduced to `0`, and since `k` is algebraically
closed, `A` and `B` are "separable" algebras over `k` in the sense of Bourbaki
`(Bourbaki, Alg., chap. VIII, §7, n° 5, prop. 5)`; so `A ⊗_k B` has no radical (loc. cit., n° 6, cor. 3 of th. 3), and
since it is a Jacobson ring, it is reduced. However, if `Z'` is a third pre-algebraic space over `k`, the "fibre
product" `X' ×_{Z'} Y'` of two reduced pre-algebraic spaces over `Z'` is in general not reduced, which implies that the
category of these spaces is insufficient in many questions (in particular in the theory of algebraic groups). But as was
seen above, one may keep Serre's language without restricting oneself, as he does (and he in addition only considers
quasi-compact pre-algebraic spaces), to the case of reduced pre-algebraic spaces.

<!-- original page 116 -->

**(10.10.5)**

<!-- label: IV.10.10.5 -->

Finally, one may also consider ultra-preschemes over an arbitrary field `k` while keeping a language that remains close
to that of Serre, and introducing, as with Weil, a fixed algebraically closed extension `K` of `k` (chosen large enough,
for example of infinite transcendence degree over `k`, to have enough "generic points" in Weil's sense). To every
prescheme `X` locally of finite type over `k`, one then associates the set `S_K(X) = S(X ⊗_k K)` of points of `X` with
values in `K`; one has a canonical map `j : S_K(X) → X` which one shows to be a quasi-homeomorphism when one equips
`S_K(X)` with the inverse image of the topology of `X` under `j`; one equips `S_K(X)` with the sheaf of `k`-algebras
`j*(𝒪_X)`, and one thus obtains a subcategory of the category of `k`-ringed spaces in local rings, which one might call
the *category of `(k, K)`-pre-algebraic spaces*. One can show that one may still define products there and generalize
the results of `(10.10.3)` and `(10.10.4)` (`𝒜(X')` being here replaced by the sheaf `𝒜_K(X')` of germs of maps from
`X'` to `K`). However, this viewpoint gives an artificial role to an arbitrarily chosen overfield of `k`, and we signal
it only to reject it.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/23-c4-s10-preschemas-jacobson.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-3.pdf, pp. 95-116 -->
