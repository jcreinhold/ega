# Chapter 0_III (suite)

# Preliminaries

## §8. Representable functors

<!-- original page 5 -->

### 8.1. Representable functors.

**8.1.1.**

<!-- label: 0_III.8.1.1 -->

We denote by `Set` the category of sets. Let `𝒞` be a category; for two objects `X`, `Y` of `𝒞`, we set
`h_X(Y) = Hom(Y, X)`; for every morphism `u : Y → Y'` in `𝒞`, we denote by `h_X(u)` the map `v ↦ v ∘ u` from
`Hom(Y', X)` into `Hom(Y, X)`. It is immediate that with these definitions `h_X : 𝒞 → Set` is a *contravariant functor*,
that is, an object of the category, denoted `Hom(𝒞°, Set)`, of covariant functors from the category `𝒞°` dual to `𝒞`
into the category `Set` `(T, 1.7, d)` and `[29]`.

> _Translator's note._ We render EGA's `Ens` as `Set` throughout, the standard modern English form. The 1961 original
> capitalizes the category as **Ens**; the typographical species ("category in bold") is rendered here by the upright
> ASCII string `Set` inside backticks.

**8.1.2.**

<!-- label: 0_III.8.1.2 -->

Now let `w : X → X'` be a morphism in `𝒞`; for every `Y ∈ 𝒞` and every `v ∈ Hom(Y, X) = h_X(Y)`, we have
`w ∘ v ∈ Hom(Y, X') = h_{X'}(Y)`; we denote by `h_w(Y)` the map `v ↦ w ∘ v` from `h_X(Y)` into `h_{X'}(Y)`. It is
immediate that for every morphism `u : Y → Y'` in `𝒞`, the diagram

```text
              h_X(u)
   h_X(Y') ────────→ h_X(Y)

   h_w(Y')│           │h_w(Y)
          ↓           ↓

   h_{X'}(Y') ───────→ h_{X'}(Y)
                h_{X'}(u)
```

is commutative; in other words, `h_w` is a *functorial morphism* `h_X → h_{X'}` `(T, 1.2)`, or again a morphism in the
category `Hom(𝒞°, Set)` `(T, 1.7, d)`. The definitions of `h_X` and `h_w` therefore constitute the definition of a
*canonical covariant functor*

```text
  h : 𝒞 → Hom(𝒞°, Set).                                                    (8.1.2.1)
```

**8.1.3.**

<!-- label: 0_III.8.1.3 -->

Let `X` be an object of `𝒞`, `F` a contravariant functor from `𝒞` into `Set` (an object of `Hom(𝒞°, Set)`). Let
`g : h_X → F` be a functorial morphism: for every `Y ∈ 𝒞`,

<!-- original page 6 -->

`g(Y)` is a map `h_X(Y) → F(Y)` such that for every morphism `u : Y → Y'` in `𝒞`, the diagram

```text
              h_X(u)
   h_X(Y') ────────→ h_X(Y)

   g(Y')  │           │ g(Y)                                              (8.1.3.1)
          ↓           ↓

   F(Y') ────────────→ F(Y)
                F(u)
```

is commutative. In particular, we have a map `g(X) : h_X(X) = Hom(X, X) → F(X)`, whence an element

```text
  α(g) = (g(X))(1_X) ∈ F(X)                                                (8.1.3.2)
```

and consequently a canonical map

```text
  α : Hom(h_X, F) → F(X).                                                  (8.1.3.3)
```

Conversely, consider an element `ξ ∈ F(X)`; for every morphism `v : Y → X` in `𝒞`, `F(v)` is a map `F(X) → F(Y)`;
consider the map

```text
  v ↦ (F(v))(ξ)                                                            (8.1.3.4)
```

from `h_X(Y)` into `F(Y)`; if we denote this map by `(β(ξ))(Y)`,

```text
  β(ξ) : h_X → F                                                           (8.1.3.5)
```

is a functorial morphism, for we have, for every morphism `u : Y → Y'` in `𝒞`, `(F(v ∘ u))(ξ) = (F(u) ∘ F(v))(ξ)`, which
verifies the commutativity of `(8.1.3.1)` for `g = β(ξ)`. We have thus defined a canonical map

```text
  β : F(X) → Hom(h_X, F).                                                  (8.1.3.6)
```

**Proposition (8.1.4).**

<!-- label: 0_III.8.1.4 -->

*The maps `α` and `β` are mutually inverse bijections.*

**Proof.** Let us compute `α(β(ξ))` for `ξ ∈ F(X)`; for every `Y ∈ 𝒞`, `(β(ξ))(Y)` is the map `g_1(Y) : v ↦ (F(v))(ξ)`
from `h_X(Y)` into `F(Y)`. We therefore have

```text
  α(β(ξ)) = (g_1(X))(1_X) = (F(1_X))(ξ) = 1_{F(X)}(ξ) = ξ.
```

Let us now compute `β(α(g))` for `g ∈ Hom(h_X, F)`; for every `Y ∈ 𝒞`, `(β(α(g)))(Y)` is the map
`v ↦ (F(v))((g(X))(1_X))`; by the commutativity of `(8.1.3.1)`, this map is none other than
`v ↦ (g(Y))((h_X(v))(1_X)) = (g(Y))(v)` by the definition of `h_X(v)`; in other words, it is equal to `g(Y)`, which
proves the proposition.

**8.1.5.**

<!-- label: 0_III.8.1.5 -->

Recall that a *subcategory* `𝒞'` of a category `𝒞` is defined by the condition that its objects be objects of `𝒞`, and
that if `X'`, `Y'` are two objects of `𝒞'`, the set `Hom_{𝒞'}(X', Y')` of morphisms `X' → Y'` in `𝒞'` is a subset of the
set `Hom_𝒞(X', Y')` of morphisms `X' → Y'` in `𝒞`, the canonical map of "composition of morphisms"

```text
  Hom_{𝒞'}(X', Y') × Hom_{𝒞'}(Y', Z') → Hom_{𝒞'}(X', Z')
```

<!-- original page 7 -->

being the restriction of the canonical map

```text
  Hom_𝒞(X', Y') × Hom_𝒞(Y', Z') → Hom_𝒞(X', Z').
```

We say that `𝒞'` is a *full* subcategory of `𝒞` if `Hom_{𝒞'}(X', Y') = Hom_𝒞(X', Y')` for every pair of objects of `𝒞'`.
The subcategory `𝒞''` of `𝒞` formed by the objects of `𝒞` isomorphic to objects of `𝒞'` is then also a full subcategory
of `𝒞`, *equivalent* `(T, 1.2)` to `𝒞'`, as one verifies without difficulty.

A covariant functor `F : 𝒞_1 → 𝒞_2` is said to be *fully faithful* if, for every pair of objects `X_1`, `Y_1` of `𝒞_1`,
the map `u ↦ F(u)` from `Hom(X_1, Y_1)` into `Hom(F(X_1), F(Y_1))` is bijective; this entails that the subcategory
`F(𝒞_1)` of `𝒞_2` is full. Moreover, if two objects `X_1`, `X'_1` have the same image `X_2`, there exists a unique
isomorphism `u : X_1 → X'_1` such that `F(u) = 1_{X_2}`. For each object `X_2` of `F(𝒞_1)`, let `G(X_2)` be one of the
objects `X_1` of `𝒞_1` such that `F(X_1) = X_2` (`G` being defined by means of the axiom of choice); for every morphism
`v : X_2 → Y_2` in `F(𝒞_1)`, `G(v)` will be the unique morphism `u : G(X_2) → G(Y_2)` such that `F(u) = v`; `G` is then
a functor from `F(𝒞_1)` into `𝒞_1`; `F ∘ G` is the identity functor on `F(𝒞_1)`, and what precedes shows that there
exists an isomorphism of functors `φ : 1_{𝒞_1} → G ∘ F` such that `F`, `G`, `φ` and the identity `1_{F(𝒞_1)} → F ∘ G`
define an *equivalence* of the category `𝒞_1` with the full subcategory `F(𝒞_1)` of `𝒞_2` `(T, 1.2)`.

**8.1.6.**

<!-- label: 0_III.8.1.6 -->

Apply Proposition `(8.1.4)` to the case where the functor `F` is `h_{X'}`, `X'` being an arbitrary object of `𝒞`; the
map `β : Hom(X, X') → Hom(h_X, h_{X'})` is here none other than the map `w ↦ h_w` defined in `(8.1.2)`; this map being
bijective, we see, with the terminology of `(8.1.5)`, that:

**Proposition (8.1.7).**

<!-- label: 0_III.8.1.7 -->

*The canonical functor `h : 𝒞 → Hom(𝒞°, Set)` is fully faithful.*

**8.1.8.**

<!-- label: 0_III.8.1.8 -->

Let `F` be a contravariant functor from `𝒞` into `Set`; we say that `F` is *representable* if there exists an object
`X ∈ 𝒞` such that `F` is isomorphic to `h_X`; it follows from `(8.1.7)` that the data of an `X ∈ 𝒞` and an isomorphism
of functors `g : h_X → F` determines `X` up to unique isomorphism. Proposition `(8.1.7)` also means that `h` defines an
*equivalence* of `𝒞` with the full subcategory of `Hom(𝒞°, Set)` formed by the representable contravariant functors. It
moreover follows from `(8.1.4)` that the data of a functorial morphism `g : h_X → F` is equivalent to that of an element
`ξ ∈ F(X)`; to say that `g` is an isomorphism is equivalent, for `ξ`, to the following condition: *for every object `Y`
of `𝒞` the map `v ↦ (F(v))(ξ)` from `Hom(Y, X)` into `F(Y)` is bijective*. When `ξ` satisfies this condition, we shall
say that the pair `(X, ξ)` *represents* the representable functor `F`. By abuse of language, we shall also say that the
object `X ∈ 𝒞` represents `F` if there exists `ξ ∈ F(X)` such that `(X, ξ)` represents `F`, in other words if `h_X` is
isomorphic to `F`.

Let `F`, `F'` be two representable contravariant functors from `𝒞` into `Set`, `h_X → F` and `h_{X'} → F'` two
isomorphisms of functors. Then it follows from `(8.1.6)` that there is a canonical one-to-one correspondence between
`Hom(X, X')` and the set `Hom(F, F')` of functorial morphisms `F → F'`.

**8.1.9.** *Examples. I: projective limits.*

<!-- label: 0_III.8.1.9 -->

The notion of representable contravariant functor covers in particular the "dual" notion of the usual notion of
"solution of a

<!-- original page 8 -->

universal problem". More generally, we shall see that the notion of *projective limit* is a particular case of that of
representable functor. Recall that in a category `𝒞`, one defines a *projective system* by the data of a preordered set
`I`, a family `(A_α)_{α ∈ I}` of objects of `𝒞`, and, for every pair of indices `(α, β)` such that `α ≤ β`, a morphism
`u_{αβ} : A_β → A_α`. A *projective limit* of this system in `𝒞` consists of an object `B` of `𝒞` (denoted `lim A_α`),
and, for each `α ∈ I`, a morphism `u_α : B → A_α`, such that: 1° `u_α = u_{αβ} ∘ u_β` for `α ≤ β`; 2° For every object
`X` of `𝒞` and every family `(v_α)_{α ∈ I}` of morphisms `v_α : X → A_α` such that `v_α = u_{αβ} ∘ v_β` for `α ≤ β`,
there exists a unique morphism `v : X → B` (denoted `lim v_α`) such that `v_α = u_α ∘ v` for every `α ∈ I` `(T, 1.8)`.
This is interpreted as follows: the `u_{αβ}` canonically define maps

```text
  ū_{αβ} : Hom(X, A_β) → Hom(X, A_α)
```

which define a projective system of sets `(Hom(X, A_α), ū_{αβ})`, and `(v_α)` is by definition an element of the set
`lim Hom(X, A_α)`; it is clear that `X ↦ lim Hom(X, A_α)` is a contravariant functor from `𝒞` into `Set`, and the
existence of the projective limit `B` is equivalent to saying that `(v_α) ↦ lim v_α` is an isomorphism of functors in
`X`

```text
  lim Hom(X, A_α) ⥲ Hom(X, B)                                              (8.1.9.1)
```

in other words that the functor `X ↦ lim Hom(X, A_α)` is *representable*.

**8.1.10.** *Examples. II: final object.*

<!-- label: 0_III.8.1.10 -->

Let `𝒞` be a category, `{a}` a set reduced to a single element. Consider the contravariant functor `F : 𝒞 → Set` which
assigns to every object `X` of `𝒞` the set `{a}`, and to every morphism `X → X'` in `𝒞` the unique map `{a} → {a}`. To
say that this functor is representable means that there exists an object `e ∈ 𝒞` such that for every `Y ∈ 𝒞`,
`Hom(Y, e) = h_e(Y)` is reduced to one element; we say that `e` is a *final object* of `𝒞`, and it is clear that two
final objects of `𝒞` are isomorphic (which allows us to define, in general by means of the axiom of choice, a final
object of `𝒞`, then denoted `e_𝒞`). For example, in the category `Set`, the final objects are the sets reduced to one
element; in the category of augmented algebras over a field `K` (where the morphisms are the algebra homomorphisms
compatible with the augmentations), `K` is a final object; in the category of `S`-preschemes `(I, 2.5.1)`, `S` is a
final object.

**8.1.11.**

<!-- label: 0_III.8.1.11 -->

For two objects `X`, `Y` of a category `𝒞`, set `h'_X(Y) = Hom(X, Y)`, and for every morphism `u : Y → Y'`, let
`h'_X(u)` be the map `v ↦ u ∘ v` from `Hom(X, Y)` into `Hom(X, Y')`; `h'_X` is then a *covariant functor* `𝒞 → Set`,
from which one deduces, as in `(8.1.2)`, the definition of a canonical covariant functor `h' : 𝒞° → Hom(𝒞, Set)`; a
covariant functor `F` from `𝒞` into `Set`, that is, an object of `Hom(𝒞, Set)`, is then said to be *representable* if
there exists an object `X ∈ 𝒞` (necessarily unique up to unique isomorphism) such that `F` is isomorphic to `h'_X`; we
leave to the reader the task of developing the "dual" considerations of the preceding ones for this notion, which this
time covers that of *inductive limit*, and in particular the usual notion of "solution of a universal problem".

<!-- original page 9 -->

### 8.2. Algebraic structures in categories.

**8.2.1.**

<!-- label: 0_III.8.2.1 -->

Given two contravariant functors `F`, `F'` from `𝒞` into `Set`, recall that for every object `Y ∈ 𝒞`, we set
`(F × F')(Y) = F(Y) × F'(Y)`, and for every morphism `u : Y → Y'` in `𝒞`, we set `(F × F')(u) = F(u) × F'(u)`, which is
the map `(t, t') ↦ ((F(u))(t), (F'(u))(t'))` from `F(Y') × F'(Y')` into `F(Y) × F'(Y)`; `F × F' : 𝒞 → Set` is therefore
a contravariant functor (which is moreover none other than the *product* of the objects `F`, `F'` in the category
`Hom(𝒞°, Set)`). Given an object `X ∈ 𝒞`, we shall call an *internal composition law* on `X` a functorial morphism

```text
  γ_X : h_X × h_X → h_X.                                                   (8.2.1.1)
```

In other words `(T, 1.2)`, for every object `Y ∈ 𝒞`, `γ_X(Y)` is a map `h_X(Y) × h_X(Y) → h_X(Y)` (so by definition an
internal composition law on the set `h_X(Y)`) subject to the condition that, for every morphism `u : Y → Y'` in `𝒞`, the
diagram

```text
                    h_X(u) × h_X(u)
   h_X(Y') × h_X(Y') ──────────────→ h_X(Y) × h_X(Y)

   γ_X(Y')         │                          │ γ_X(Y)
                   ↓                          ↓

       h_X(Y') ───────────────────────→ h_X(Y)
                          h_X(u)
```

is commutative; this means that for the composition laws `γ_X(Y)` and `γ_X(Y')`, `h_X(u)` is a homomorphism from
`h_X(Y')` into `h_X(Y)`.

In the same way, given two objects `Z`, `X` of `𝒞`, one calls an *external composition law* on `X`, *having `Z` as
domain of operators*, a functorial morphism

```text
  ω_{X,Z} : h_Z × h_X → h_X.                                               (8.2.1.2)
```

One sees as above that for every `Y ∈ 𝒞`, `ω_{X,Z}(Y)` is an external composition law on `h_X(Y)`, having `h_Z(Y)` as
domain of operators, and such that for every morphism `u : Y → Y'`, `h_Z(u)` and `h_X(u)` form a *di-homomorphism* from
`(h_Z(Y'), h_X(Y'))` into `(h_Z(Y), h_X(Y))`.

**8.2.2.**

<!-- label: 0_III.8.2.2 -->

Let `X'` be a second object of `𝒞`, and suppose given on `X'` an internal composition law `γ_{X'}`; we shall say that a
morphism `w : X → X'` in `𝒞` is a *homomorphism* for these composition laws, if for every `Y ∈ 𝒞`,
`h_w(Y) : h_X(Y) → h_{X'}(Y)` is a homomorphism for the composition laws `γ_X(Y)` and `γ_{X'}(Y)`. If `X''` is a third

<!-- original page 10 -->

object of `𝒞` equipped with an internal composition law `γ_{X''}` and `w' : X' → X''` a morphism in `𝒞` which is a
homomorphism for `γ_{X'}` and `γ_{X''}`, it is clear that the morphism `w' ∘ w : X → X''` is a homomorphism for the
composition laws `γ_X` and `γ_{X''}`. An isomorphism `w : X ⥲ X'` in `𝒞` is called an *isomorphism for the composition
laws `γ_X` and `γ_{X'}`* if `w` is a homomorphism for these composition laws, and if its inverse morphism `w^{−1}` is a
homomorphism for the composition laws `γ_{X'}` and `γ_X`.

One defines in the same way the *di-homomorphisms* for the pairs of objects of `𝒞` equipped with external composition
laws.

**8.2.3.**

<!-- label: 0_III.8.2.3 -->

When an internal composition law `γ_X` on an object `X ∈ 𝒞` is such that `γ_X(Y)` is a *group law* on `h_X(Y)` for every
`Y ∈ 𝒞`, we say that `X`, equipped with this law, is a *`𝒞`-group* or a *`𝒞`-object in groups*. One defines in the same
way *`𝒞`-rings*, *`𝒞`-modules*, etc.

**8.2.4.**

<!-- label: 0_III.8.2.4 -->

Suppose that the product `X × X` of an object `X ∈ 𝒞` by itself exists in `𝒞`; by definition, we then have
`h_{X × X} = h_X × h_X` up to canonical isomorphism, since this is a particular case of projective limit `(8.1.9)`; an
internal composition law on `X` may therefore be considered as a functorial morphism `γ_X : h_{X × X} → h_X`, and so
canonically determines `(8.1.6)` an element `c_X ∈ Hom(X × X, X)` such that `h_{c_X} = γ_X`; in this case, the data of
an internal composition law on `X` is therefore equivalent to that of a morphism `X × X → X`; when `𝒞` is the category
`Set`, one recovers the classical notion of internal composition law on a set. One has an analogous result for an
external composition law when the product `Z × X` exists in `𝒞`.

**8.2.5.**

<!-- label: 0_III.8.2.5 -->

With the preceding notations, suppose in addition that `X × X × X` exists in `𝒞`; the characterization of the product as
an object representing a functor `(8.1.9)` entails the existence of canonical isomorphisms

```text
  (X × X) × X ⥲ X × X × X ⥲ X × (X × X);
```

if one canonically identifies `X × X × X` with `(X × X) × X`, the map `γ_X(Y) × 1_{h_X(Y)}` identifies with
`h_{c_X × 1_X}(Y)` for every `Y ∈ 𝒞`. It is therefore equivalent to say that for every `Y ∈ 𝒞`, the internal law
`γ_X(Y)` is *associative*, or that the diagram of maps

```text
                         γ_X(Y) × 1
   h_X(Y) × h_X(Y) × h_X(Y) ────────→ h_X(Y) × h_X(Y)

   1 × γ_X(Y) │                              │ γ_X(Y)
              ↓                              ↓

   h_X(Y) × h_X(Y) ──────────────────────→ h_X(Y)
                          γ_X(Y)
```

<!-- original page 11 -->

is commutative, or that the diagram of morphisms

```text
                         c_X × 1_X
       X × X × X ────────────────→ X × X

   1_X × c_X │                       │ c_X
             ↓                       ↓

         X × X ──────────────────→ X
                          c_X
```

is commutative.

**8.2.6.**

<!-- label: 0_III.8.2.6 -->

Under the hypotheses of `(8.2.5)`, if one wants to express that for every `Y ∈ 𝒞`, the internal law `γ_X(Y)` is a *group
law*, it is necessary, on the one hand, to express that it is associative, and on the other that there exists a map
`α_X(Y) : h_X(Y) → h_X(Y)` having the properties of the *inverse* in a group; since for every morphism `u : Y → Y'` in
`𝒞`, we have seen that `h_X(u)` must be a group homomorphism `h_X(Y') → h_X(Y)`, one sees first that `α_X : h_X → h_X`
*must be a functorial morphism*. One can on the other hand express the characteristic properties of the inverse
`s ↦ s^{−1}` in a group `G` without making the neutral element intervene: it suffices to write that the two composed
maps

```text
  (s, t) ↦ (s, s^{−1}, t) ↦ (s, s^{−1} t) ↦ s(s^{−1} t)
  (s, t) ↦ (s, s^{−1}, t) ↦ (s, t s^{−1}) ↦ (t s^{−1}) s
```

are equal to the second projection `(s, t) ↦ t` from `G × G` into `G`. By virtue of `(8.1.3)`, we have `α_X = h_{a_X}`,
where `a_X ∈ Hom(X, X)`; the first preceding condition then expresses that the composed morphism

```text
                  (1_X, a_X) × 1_X         1_X × c_X            c_X
   X × X ──────────────────────→ X × X × X ────────→ X × X ────────→ X
```

is the second projection `X × X → X` in `𝒞`, and the second condition is translated similarly.

**8.2.7.**

<!-- label: 0_III.8.2.7 -->

Suppose now that there exists in `𝒞` a final object `e` `(8.1.10)`. Suppose still that `γ_X(Y)` is a group law on
`h_X(Y)` for every `Y ∈ 𝒞`, and denote by `η_X(Y)` the neutral element of `γ_X(Y)`. Since, for every morphism
`u : Y → Y'` in `𝒞`, `h_X(u)` is a group homomorphism, we have `η_X(Y) = (h_X(u))(η_X(Y'))`; taking in particular
`Y' = e`, in which case `u` is the unique element `ε` of `Hom(Y, e)`, we see that the element `η_X(e)` completely
determines `η_X(Y)` for every `Y ∈ 𝒞`. Set `e_X = η_X(X)`, the neutral element of the group `h_X(X) = Hom(X, X)`; the
commutativity of the diagram

```text
              h_ε(X)
   h_X(e) ───────────→ h_X(Y)

   h_{e_X}(e) │           │ h_{e_X}(Y)
              ↓           ↓

   h_X(e) ───────────→ h_X(Y)
              h_ε(X)
```

(cf. `8.1.2`) shows that, in the set `h_X(Y)`, the map `h_{e_X}(Y)` is none other than

<!-- original page 12 -->

`s ↦ η_X(Y)`, transforming every element into the neutral element. One then verifies that the fact that `η_X(Y)` is the
neutral element of `γ_X(Y)` for every `Y ∈ 𝒞` is equivalent to saying that the composed morphism

```text
              (1_X, 1_X)         1_X × e_X            c_X
   X ──────────────────→ X × X ──────────→ X × X ──────→ X,
```

and the analogous one where one permutes `1_X` and `e_X`, are both equal to `1_X`.

**8.2.8.**

<!-- label: 0_III.8.2.8 -->

One could of course multiply without difficulty the examples of algebraic structures in categories. The example of
groups has been treated with sufficient detail, but in what follows we shall generally leave to the reader the task of
developing analogous considerations in the examples of algebraic structures that we shall encounter.

______________________________________________________________________

> _Translator's footnote (from p. 5)._ To facilitate reference lookup, we shall henceforth refer to the paragraphs of
> Chapter 0 published with Chapter I by the sign `0_I`.
