# Chapter 0 — Preliminaries

## §3. Complements on Sheaves

<!-- label: 0.3 -->

### 3.1. Sheaves with values in a category

<!-- label: 0.3.1 -->

**(3.1.1)** Let `𝑲` be a category, let `(A_α)_{α ∈ I}` and `(A_{αβ})_{(α,β) ∈ I × I}` be two families of objects of `𝑲`
with `A_{βα} = A_{αβ}`, and let `(ρ_{αβ})_{(α,β) ∈ I × I}` be a family of morphisms `ρ_{αβ} : A_α → A_{αβ}`. We say that
a pair consisting of an object `A` of `𝑲` and a family of morphisms `ρ_α : A → A_α` is a _solution of the universal
problem_ defined by the data `(A_α)`, `(A_{αβ})`, `(ρ_{αβ})` if, for every object `B` of `𝑲`, the map sending
`f ∈ Hom(B, A)` to `(ρ_α ∘ f) ∈ ∏_α Hom(B, A_α)` is a _bijection_ of `Hom(B, A)` onto the set of `(f_α)` such that
`ρ_{αβ} ∘ f_α = ρ_{βα} ∘ f_β` for every pair of indices `(α, β)`. One sees at once that if such a solution exists, it is
unique up to isomorphism.

**(3.1.2)** We shall not recall the definition of a _presheaf_ `U ↦ ℱ(U)` on a topological space `X` with values in a
category `𝑲` (G, I, 1.9); we say that such a presheaf is a _sheaf with values in_ `𝑲` if it satisfies the following
axiom:

> (F) _For every cover_ `(U_α)` _of an open set_ `U ⊂ X` _by open sets_ `U_α ⊂ U`, _if_ `ρ_α` (resp. `ρ_{αβ}`) _denotes
> the restriction morphism_
>
> ```
> ℱ(U) → ℱ(U_α)    (resp. ℱ(U_α) → ℱ(U_α ∩ U_β)),
> ```
>
> _then the pair_ `(ℱ(U), (ρ_α))` _is a solution of the universal problem for_ `(ℱ(U_α))`, `(ℱ(U_α ∩ U_β))`, _and_
> `(ρ_{αβ})` _(3.1.1)._[^3-1]

Equivalently, for every object `T` of `𝑲`, the family `U ↦ Hom(T, ℱ(U))` is a _sheaf of sets_.

**(3.1.3)** Suppose `𝑲` is the category defined by a "species of structure with morphisms" `Σ` — the objects of `𝑲`
being the sets endowed with structures of species `Σ`, and the morphisms those of `Σ`. Suppose moreover that `𝑲`
satisfies:

> (E) If `(A, (ρ_α))` is a solution of a universal mapping problem _in the category_ `𝑲` for families `(A_α)`,
> `(A_{αβ})`, `(ρ_{αβ})`, then it is also a solution of the universal mapping problem for the same families _in the
> category of sets_ — that is, when one regards `A`, the `A_α`, and the `A_{αβ}` as sets and `ρ_α`, `ρ_{αβ}` as
> maps.[^3-2]

Under these conditions, axiom (F) implies that, viewed as a presheaf of sets, `U ↦ ℱ(U)` is a _sheaf_. Moreover, for a
map `u : T → ℱ(U)` to be a morphism of `𝑲`, it is necessary and sufficient, by (F), that each `ρ_α ∘ u` be a morphism
`T → ℱ(U_α)` — that is, that the structure of species `Σ` on `ℱ(U)` be the _initial structure_ for the morphisms `ρ_α`.
Conversely, suppose that a presheaf `U ↦ ℱ(U)` on `X` with values in `𝑲` is a _sheaf of sets_ and satisfies the
preceding condition; then it satisfies (F), hence is a _sheaf with values in_ `𝑲`.

**(3.1.4)** When `Σ` is the species of group or ring structures, the fact that the presheaf `U ↦ ℱ(U)` with values in
`𝑲` is a sheaf of _sets_ implies _ipso facto_ that it is a sheaf _with values in_ `𝑲` — that is, a sheaf of groups or
rings in the sense of (G).[^3-3] This is no longer the case when, for example, `𝑲` is the category of _topological
rings_ (with continuous representations as morphisms): a sheaf with values in `𝑲` is then a sheaf of sets `U ↦ ℱ(U)`
such that for every open `U` and every cover of `U` by open `U_α ⊂ U`, the topology of `ℱ(U)` is _the coarsest_ making
the representations `ℱ(U) → ℱ(U_α)` continuous. In this case we say that `ℱ(U)`, viewed as a sheaf of rings (without
topology), is _underlying_ the sheaf of topological rings `U ↦ ℱ(U)`. The morphisms `u_V : ℱ(V) → 𝒢(V)` (for arbitrary
open `V ⊂ X`) of sheaves of topological rings are thus homomorphisms of the underlying sheaves of rings such that `u_V`
is _continuous_ for every open `V`; to distinguish them from arbitrary homomorphisms of the underlying sheaves of rings,
we call them _continuous homomorphisms_ of sheaves of topological rings. Analogous definitions and conventions hold for
sheaves of topological spaces or topological groups.

**(3.1.5)** It is clear that for any category `𝑲`, if `ℱ` is a presheaf (resp. sheaf) on `X` with values in `𝑲` and `U`
is an open subset of `X`, then the `ℱ(V)` for `V ⊂ U` form a presheaf (resp. sheaf) with values in `𝑲`, called the
presheaf (resp. sheaf) _induced_ by `ℱ` on `U` and written `ℱ|U`.

For every morphism `u : ℱ → 𝒢` of presheaves on `X` with values in `𝑲`, we shall write `u|U` for the morphism
`ℱ|U → 𝒢|U` given by the `u_V` for `V ⊂ U`.

**(3.1.6)** Suppose now that `𝑲` admits _inductive limits [modern: direct limits]_ (T, 1.8); then, for every presheaf
(and in particular every sheaf) `ℱ` on `X` with values in `𝑲` and every `x ∈ X`, one can define the _stalk_ `ℱ_x` as the
object of `𝑲` given by the inductive limit of the filtered (by `⊃`) family of open neighborhoods `U` of `x` in `X`, with
the restriction morphisms `ρ^V_U : ℱ(V) → ℱ(U)`. If `u : ℱ → 𝒢` is a morphism of presheaves with values in `𝑲`, one
defines for each `x ∈ X` the morphism `u_x : ℱ_x → 𝒢_x` as the inductive limit of the `u_U : ℱ(U) → 𝒢(U)` over the
system of open neighborhoods of `x`; this makes `ℱ_x` a covariant functor in `ℱ`, with values in `𝑲`, for each `x ∈ X`.

When in addition `𝑲` is defined by a species of structure with morphisms `Σ`, the elements of `ℱ(U)` are still called
_sections over_ `U` of the _sheaf_ `ℱ` with values in `𝑲`, and we then write `Γ(U, ℱ)` in place of `ℱ(U)`; for
`s ∈ Γ(U, ℱ)` and `V` an open subset of `U`, we write `s|V` in place of `ρ^U_V(s)`; for `x ∈ U`, the canonical image of
`s` in `ℱ_x` is the _germ_ of `s` at `x`, written `s_x`. (We shall never use the notation `s(x)` in this sense, since it
is reserved for another notion concerning the particular sheaves considered in this treatise (5.5.1).)

If `u : ℱ → 𝒢` is a morphism of sheaves with values in `𝑲`, we shall write `u(s)` in place of `u_V(s)` for
`s ∈ Γ(V, ℱ)`.

If `ℱ` is a sheaf of abelian groups, rings, or modules, the set of `x ∈ X` such that `ℱ_x ≠ {0}` is called the _support_
of `ℱ`, written `Supp(ℱ)`; this set is not necessarily closed in `X`.

When `𝑲` is defined by a species of structure with morphisms, _we systematically refrain from introducing the
"étalé-space" viewpoint_ for sheaves with values in `𝑲`. In other words, we never view a sheaf as a topological space
(nor even as the disjoint union of its stalks), and we shall not view a morphism `u : ℱ → 𝒢` of such sheaves on `X` as a
continuous map of topological spaces.

### 3.2. Presheaves on a basis of open sets

<!-- label: 0.3.2 -->

**(3.2.1)** We restrict ourselves in what follows to categories `𝑲` admitting _projective limits \[modern: inverse
limits\]_ (in the generalized sense — corresponding to preordered sets that are not necessarily filtered; cf. (T, 1.8)).
Let `X` be a topological space and `𝔅` a basis of open sets for the topology of `X`. We call a _presheaf on_ `𝔅` _with
values in_ `𝑲` a family of objects `ℱ(U) ∈ 𝑲` attached to each `U ∈ 𝔅`, together with morphisms `ρ^V_U : ℱ(V) → ℱ(U)`
defined for every pair `(U, V)` of elements of `𝔅` with `U ⊂ V`, satisfying `ρ^U_U = identity` and
`ρ^W_U = ρ^V_U ∘ ρ^W_V` whenever `U ⊂ V ⊂ W` in `𝔅`. To such a family we associate a _presheaf with values in_ `𝑲`,
`U ↦ ℱ′(U)` in the usual sense, by setting

```
ℱ′(U) = lim⃖_{V ∈ 𝔅, V ⊂ U} ℱ(V),
```

where `V` ranges over the (in general non-filtered) ordered set of `V ∈ 𝔅` with `V ⊂ U`; the `ℱ(V)` form a projective
system for the `ρ^W_V` (`V ⊂ W ⊂ U`, `V, W ∈ 𝔅`). Indeed, if `U, U′` are open with `U ⊂ U′`, define `ρ′^{U′}_U` as the
projective limit (over `V ⊂ U`) of the canonical morphisms `ℱ′(U′) → ℱ(V)` — that is, the unique morphism
`ℱ′(U′) → ℱ′(U)` whose composition with each canonical `ℱ′(U) → ℱ(V)` gives the canonical `ℱ′(U′) → ℱ(V)`. The
transitivity of the `ρ′^{U′}_U` follows immediately. Moreover, for `U ∈ 𝔅` the canonical morphism `ℱ′(U) → ℱ(U)` is an
_isomorphism_, allowing one to identify these two objects.[^3-4]

**(3.2.2)** For the presheaf `ℱ′` defined above to be a _sheaf_, it is necessary and sufficient that the presheaf `ℱ` on
`𝔅` satisfy:

> (F₀) _For every cover_ `(U_α)` _of_ `U ∈ 𝔅` _by sets_ `U_α ∈ 𝔅` _contained in_ `U`, _and for every object_ `T ∈ 𝑲`,
> _the map sending_ `f ∈ Hom(T, ℱ(U))` _to_ `(ρ^U_{U_α} ∘ f) ∈ ∏_α Hom(T, ℱ(U_α))` _is a bijection of_ `Hom(T, ℱ(U))`
> _onto the set of_ `(f_α)` _such that_ `ρ^{U_α}_V ∘ f_α = ρ^{U_β}_V ∘ f_β` _for every pair_ `(α, β)` _and every_
> `V ∈ 𝔅` _with_ `V ⊂ U_α ∩ U_β`.[^3-5]

The condition is plainly necessary. For sufficiency, consider a second basis `𝔅′` for the topology of `X` with `𝔅′ ⊂ 𝔅`,
and let `ℱ″` denote the presheaf obtained from the subfamily `(ℱ(V))_{V ∈ 𝔅′}`. Then `ℱ″` is _canonically isomorphic_ to
`ℱ′`: for any open `U`, the projective limit (over `V ∈ 𝔅′`, `V ⊂ U`) of the canonical `ℱ′(U) → ℱ(V)` is a morphism
`ℱ′(U) → ℱ″(U)`. For `U ∈ 𝔅` this morphism is an isomorphism, since by hypothesis each canonical `ℱ′(U) → ℱ(V)` for
`V ∈ 𝔅′`, `V ⊂ U`, factors as `ℱ′(U) → ℱ″(U) → ℱ(V)`, and one checks at once that the composites `ℱ′(U) → ℱ″(U) → ℱ′(U)`
and `ℱ″(U) → ℱ′(U) → ℱ″(U)` are identities. This being so, for every open `U` the morphisms `ℱ′(U) → ℱ″(W) = ℱ(W)` for
`W ∈ 𝔅`, `W ⊂ U`, satisfy the conditions characterizing the projective limit of the `ℱ(W)` (`W ∈ 𝔅`, `W ⊂ U`), which
proves our assertion by uniqueness of projective limits up to isomorphism.

That said, let `U` be an arbitrary open set of `X`, `(U_α)` a cover of `U` by open sets contained in `U`, and `𝔅′` the
subfamily of `𝔅` consisting of those elements of `𝔅` contained in some `U_α`. Plainly `𝔅′` is still a basis for the
topology of `X`, so `ℱ′(U)` (resp. `ℱ′(U_α)`) is the projective limit of the `ℱ(V)` for `V ∈ 𝔅′`, `V ⊂ U` (resp.
`V ⊂ U_α`); axiom (F) is then verified at once, by the definition of projective limit.

When (F₀) holds, we shall say by abuse of language that the presheaf `ℱ` on the basis `𝔅` _is a sheaf_.

**(3.2.3)** Let `ℱ`, `𝒢` be two presheaves on the basis `𝔅` with values in `𝑲`. A _morphism_ `u : ℱ → 𝒢` is a family
`(u_V)_{V ∈ 𝔅}` of morphisms `u_V : ℱ(V) → 𝒢(V)` satisfying the usual compatibility with the restriction morphisms
`ρ^W_V`. With the notation of (3.2.1), one obtains a morphism `u′ : ℱ′ → 𝒢′` of the corresponding ordinary presheaves by
taking for `u′_U` the projective limit of the `u_V` for `V ∈ 𝔅`, `V ⊂ U`; the compatibility with the `ρ′^{U′}_U` follows
from the functoriality of projective limits.

**(3.2.4)** If `𝑲` admits inductive limits and `ℱ` is a presheaf on `𝔅` with values in `𝑲`, then for every `x ∈ X` the
neighborhoods of `x` belonging to `𝔅` form a cofinal subset (for `⊃`) of the neighborhoods of `x`; hence if `ℱ′` is the
ordinary presheaf associated with `ℱ`, the stalk `ℱ′_x` equals `lim⃗ ℱ(V)` over `V ∈ 𝔅`, `x ∈ V`. If `u : ℱ → 𝒢` is a
morphism of presheaves on `𝔅` and `u′ : ℱ′ → 𝒢′` the corresponding morphism of ordinary presheaves, then `u′_x` is the
inductive limit of the `u_V : ℱ(V) → 𝒢(V)` for `V ∈ 𝔅`, `x ∈ V`.

**(3.2.5)** Returning to the general setting of (3.2.1): if `ℱ` is an ordinary _sheaf_ with values in `𝑲` and `ℱ_1` is
the sheaf on `𝔅` obtained by restriction of `ℱ` to `𝔅`, then the ordinary sheaf `ℱ′_1` obtained from `ℱ_1` by the
construction of (3.2.1) is canonically isomorphic to `ℱ`, by (F) and the uniqueness of projective limits. We shall
ordinarily identify `ℱ` and `ℱ′_1`.

If `𝒢` is a second ordinary sheaf on `X` with values in `𝑲` and `u : ℱ → 𝒢` a morphism, the preceding remark shows that
giving the `u_V : ℱ(V) → 𝒢(V)` _for_ `V ∈ 𝔅` _alone_ determines `u` completely. Conversely, given `u_V` for `V ∈ 𝔅`
satisfying the commutativity diagrams with the restriction morphisms `ρ^W_V` for `V, W ∈ 𝔅` and `V ⊂ W`, there is a
unique morphism `u′ : ℱ → 𝒢` with `u′_V = u_V` for every `V ∈ 𝔅` (3.2.3).

**(3.2.6)** Continue to assume that `𝑲` admits projective limits. Then the category of _sheaves on_ `X` _with values in_
`𝑲` also admits _projective limits_: if `(ℱ_λ)` is a projective system of sheaves on `X` with values in `𝑲`, then the
`ℱ(U) = lim⃖_λ ℱ_λ(U)` define a presheaf with values in `𝑲`, and axiom (F) holds by the transitivity of projective
limits; that `ℱ` is then the projective limit of the `ℱ_λ` is immediate.

When `𝑲` is the category of sets, then for every projective system `(ℋ_λ)` with `ℋ_λ` a _subsheaf_ of `ℱ_λ` for each
`λ`, `lim⃖_λ ℋ_λ` is canonically identified with a subsheaf of `lim⃖_λ ℱ_λ`. If `𝑲` is the category of abelian groups,
the covariant functor `lim⃖_λ ℱ_λ` is _additive_ and _left exact_.

### 3.3. Gluing of sheaves

<!-- label: 0.3.3 -->

**(3.3.1)** Continue to assume that `𝑲` admits (generalized) projective limits. Let `X` be a topological space,
`𝔘 = (U_λ)_{λ ∈ L}` an open cover of `X`, and for each `λ ∈ L` let `ℱ_λ` be a sheaf on `U_λ` with values in `𝑲`. Suppose
that for every pair `(λ, μ)` we are given an _isomorphism_ `θ_{λμ} : ℱ_μ|(U_λ ∩ U_μ) ⥲ ℱ_λ|(U_λ ∩ U_μ)`, and that for
every triple `(λ, μ, ν)`, writing `θ′_{λμ}, θ′_{μν}, θ′_{λν}` for the restrictions of `θ_{λμ}, θ_{μν}, θ_{λν}` to
`U_λ ∩ U_μ ∩ U_ν`, one has `θ′_{λν} = θ′_{λμ} ∘ θ′_{μν}` (_the gluing condition for the_ `θ_{λμ}`). Then there is a
sheaf `ℱ` on `X` with values in `𝑲`, and for each `λ` an isomorphism `η_λ : ℱ|U_λ ⥲ ℱ_λ`, such that for every `(λ, μ)`,
writing `η′_λ` and `η′_μ` for the restrictions of `η_λ` and `η_μ` to `U_λ ∩ U_μ`, one has `θ_{λμ} = η′_λ ∘ η′_μ⁻¹`.
Moreover, `ℱ` and the `η_λ` are determined up to unique isomorphism by these conditions. Uniqueness follows at once from
(3.2.5). For existence, let `𝔅` be the basis of open sets contained in some `U_λ`; choose (via Hilbert's `τ`-function)
one of the `ℱ_λ(U)` for some `λ` with `U ⊂ U_λ`; call this object `ℱ(U)`. The `ρ^V_U` for `U ⊂ V`, `U, V ∈ 𝔅`, are
defined in the obvious way (using the `θ_{λμ}`), and transitivity follows from the gluing condition. Axiom (F₀) is then
immediate, so the presheaf on `𝔅` so defined is a sheaf; from it the general construction (3.2.1) yields an ordinary
sheaf, again written `ℱ`, with the required property. We say that `ℱ` is obtained by _gluing the_ `ℱ_λ` _via the_
`θ_{λμ}`, and we ordinarily identify `ℱ_λ` and `ℱ|U_λ` via `η_λ`.

It is clear that every sheaf `ℱ` on `X` with values in `𝑲` may be viewed as obtained by gluing the sheaves `ℱ_λ = ℱ|U_λ`
(where `(U_λ)` is any open cover of `X`) via the identity isomorphisms `θ_{λμ}`.

**(3.3.2)** With the same notation, let `𝒢_λ` be a second sheaf on `U_λ` (for each `λ ∈ L`) with values in `𝑲`, and
suppose given for each `(λ, μ)` an isomorphism `ω_{λμ} : 𝒢_μ|(U_λ ∩ U_μ) ⥲ 𝒢_λ|(U_λ ∩ U_μ)` satisfying the gluing
condition. Suppose finally given for each `λ` a morphism `u_λ : ℱ_λ → 𝒢_λ` such that the diagrams

```
(3.3.2.1)    ℱ_μ|(U_λ ∩ U_μ) ──u_μ──→ 𝒢_μ|(U_λ ∩ U_μ)
                   │                          │
                   ↓                          ↓
             ℱ_λ|(U_λ ∩ U_μ) ──u_λ──→ 𝒢_λ|(U_λ ∩ U_μ)
```

commute. Then if `𝒢` is obtained by gluing the `𝒢_λ` via the `ω_{λμ}`, there is a unique morphism `u : ℱ → 𝒢` such that
the diagrams

```
ℱ|U_λ ──u|U_λ──→ 𝒢|U_λ
  │                 │
  ↓                 ↓
 ℱ_λ ────u_λ───→  𝒢_λ
```

commute; this follows at once from (3.2.3). The correspondence between the family `(u_λ)` and `u` is a functorial
bijection of the subset of `∏_λ Hom(ℱ_λ, 𝒢_λ)` satisfying (3.3.2.1) onto `Hom(ℱ, 𝒢)`.

**(3.3.3)** With the notation of (3.3.1), let `V` be an open subset of `X`. The restrictions of the `θ_{λμ}` to
`V ∩ U_λ ∩ U_μ` plainly satisfy the gluing condition for the induced sheaves `ℱ_λ|(V ∩ U_λ)`, and the sheaf on `V`
obtained by gluing these is canonically identified with `ℱ|V`.

### 3.4. Direct images of presheaves

<!-- label: 0.3.4 -->

**(3.4.1)** Let `X`, `Y` be topological spaces and `ψ : X → Y` a continuous map. Let `ℱ` be a presheaf on `X` with
values in `𝑲`; for every open `U ⊂ Y`, set `𝒢(U) = ℱ(ψ⁻¹(U))`, and for `U ⊂ V` open in `Y` let `ρ′^V_U` be the morphism
`ℱ(ψ⁻¹(V)) → ℱ(ψ⁻¹(U))`. The `𝒢(U)` and `ρ′^V_U` define a _presheaf_ on `Y` with values in `𝑲`, called the _direct image
of_ `ℱ` _by_ `ψ` and written `ψ_*(ℱ)`. If `ℱ` is a sheaf, axiom (F) for `𝒢` is immediate, so `ψ_*(ℱ)` is a sheaf.

**(3.4.2)** Let `ℱ_1`, `ℱ_2` be presheaves on `X` with values in `𝑲` and let `u : ℱ_1 → ℱ_2` be a morphism. As `U`
ranges over the open subsets of `Y`, the family `u_{ψ⁻¹(U)} : ℱ_1(ψ⁻¹(U)) → ℱ_2(ψ⁻¹(U))` satisfies the compatibility
with restriction morphisms, defining `ψ_*(u) : ψ_*(ℱ_1) → ψ_*(ℱ_2)`. If `v : ℱ_2 → ℱ_3` is a further morphism,
`ψ_*(v ∘ u) = ψ_*(v) ∘ ψ_*(u)`; that is, `ψ_*` is a _covariant functor_ from presheaves (resp. sheaves) on `X` with
values in `𝑲` to presheaves (resp. sheaves) on `Y` with values in `𝑲`.

**(3.4.3)** Let `Z` be a third topological space, `ψ′ : Y → Z` continuous, and set `ψ″ = ψ′ ∘ ψ`. One has
`ψ″_*(ℱ) = ψ′_*(ψ_*(ℱ))` for every presheaf `ℱ` on `X` with values in `𝑲`; for every morphism `u : ℱ → 𝒢`,
`ψ″_*(u) = ψ′_*(ψ_*(u))`. In other words, `ψ″_*` is the _composite_ of `ψ′_*` and `ψ_*`:

```
(ψ′ ∘ ψ)_* = ψ′_* ∘ ψ_*.
```

Moreover, for every open `U ⊂ Y`, the direct image by the restriction `ψ|ψ⁻¹(U)` of the induced presheaf `ℱ|ψ⁻¹(U)` is
none other than the induced presheaf `ψ_*(ℱ)|U`.

**(3.4.4)** Suppose `𝑲` admits inductive limits and let `ℱ` be a presheaf on `X` with values in `𝑲`. For each `x ∈ X`,
the morphisms `Γ(ψ⁻¹(U), ℱ) → ℱ_x` (`U` an open neighborhood of `ψ(x)` in `Y`) form an inductive system; passage to the
limit gives a stalk morphism

```
ψ_x : (ψ_*(ℱ))_{ψ(x)} → ℱ_x.
```

In general, `ψ_x` is _neither injective nor surjective_. It is functorial: for `u : ℱ_1 → ℱ_2`, the diagram

```
(ψ_*(ℱ_1))_{ψ(x)} ──ψ_x──→ (ℱ_1)_x
        │                       │
(ψ_*(u))_{ψ(x)}                u_x
        │                       │
        ↓                       ↓
(ψ_*(ℱ_2))_{ψ(x)} ──ψ_x──→ (ℱ_2)_x
```

commutes. If `Z` is a third topological space, `ψ′ : Y → Z` continuous, and `ψ″ = ψ′ ∘ ψ`, then `ψ″_x = ψ_x ∘ ψ′_{ψ(x)}`
for `x ∈ X`.

**(3.4.5)** Under the hypotheses of (3.4.4), suppose further that `ψ` is a _homeomorphism_ of `X` onto the subspace
`ψ(X)` of `Y`. Then for every `x ∈ X`, `ψ_x` is an _isomorphism_. This applies in particular to the canonical injection
`j` of a subspace `X ⊂ Y` into `Y`.

**(3.4.6)** Suppose `𝑲` is the category of groups, of rings, etc. If `ℱ` is a sheaf on `X` with support `S`, and
`y ∉ ψ(S)̅`, then by the definition of `ψ_*(ℱ)` one has `(ψ_*(ℱ))_y = {0}`; that is, `Supp(ψ_*(ℱ)) ⊂ ψ(S)̅`. The support
is not, however, necessarily contained in `ψ(S)`. Under the same hypotheses, if `j` is the canonical injection of a
subspace `X ⊂ Y`, the sheaf `j_*(ℱ)` induces `ℱ` on `X`; if moreover `X` is _closed_ in `Y`, then `j_*(ℱ)` is the sheaf
on `Y` inducing `ℱ` on `X` and `0` on `Y − X` (G, II, 2.9.2); but the two sheaves are in general distinct when `X` is
locally closed but not closed.

### 3.5. Inverse images of presheaves

<!-- label: 0.3.5 -->

**(3.5.1)** Under the hypotheses of (3.4.1), if `ℱ` (resp. `𝒢`) is a presheaf on `X` (resp. `Y`) with values in `𝑲`,
every morphism `u : 𝒢 → ψ_*(ℱ)` of presheaves on `Y` is called a _ψ-morphism_ of `𝒢` into `ℱ`, also written `𝒢 → ℱ`. We
write `Hom_ψ(𝒢, ℱ)` for `Hom_Y(𝒢, ψ_*(ℱ))`. For every pair `(U, V)` with `U` open in `X`, `V` open in `Y`, and
`ψ(U) ⊂ V`, one has a morphism `u_{U,V} : 𝒢(V) → ℱ(U)` obtained by composing the restriction `ℱ(ψ⁻¹(V)) → ℱ(U)` with
`u_V : 𝒢(V) → ψ_*(ℱ)(V) = ℱ(ψ⁻¹(V))`. These morphisms make the diagrams

```
(3.5.1.1)    𝒢(V) ──u_{U,V}──→ ℱ(U)
               │                  │
               ↓                  ↓
             𝒢(V′) ──u_{U′,V′}──→ ℱ(U′)
```

(for `U′ ⊂ U`, `V′ ⊂ V`, `ψ(U′) ⊂ V′`) commute. Conversely, a family `(u_{U,V})` making (3.5.1.1) commute defines a
`ψ`-morphism `u`: take `u_V = u_{ψ⁻¹(V), V}`.

If `𝑲` admits (generalized) projective limits and `𝔅`, `𝔅′` are bases for the topologies of `X` and `Y`, then to define
a `ψ`-morphism of _sheaves_ it suffices to give `u_{U,V}` for `U ∈ 𝔅`, `V ∈ 𝔅′`, `ψ(U) ⊂ V`, satisfying (3.5.1.1) for
`U, U′ ∈ 𝔅` and `V, V′ ∈ 𝔅′`; for an arbitrary open `W ⊂ Y`, define `u_W` as the projective limit of the `u_{U,V}` for
`V ∈ 𝔅′`, `V ⊂ W`, `U ∈ 𝔅`, `ψ(U) ⊂ V`.

When `𝑲` admits inductive limits, one obtains for each `x ∈ X` a morphism `𝒢(V) → ℱ(ψ⁻¹(V)) → ℱ_x` for every open
neighborhood `V` of `ψ(x)` in `Y`; these form an inductive system whose limit is a stalk morphism `𝒢_{ψ(x)} → ℱ_x`.

**(3.5.2)** Under the hypotheses of (3.4.3), let `ℱ`, `𝒢`, `ℋ` be presheaves on `X`, `Y`, `Z` with values in `𝑲`, and
let `u : 𝒢 → ψ_*(ℱ)`, `v : ℋ → ψ′_*(𝒢)` be a `ψ`-morphism and a `ψ′`-morphism. One obtains a `ψ″`-morphism

```
w : ℋ ──v──→ ψ′_*(𝒢) ──ψ′_*(u)──→ ψ′_*(ψ_*(ℱ)) = ψ″_*(ℱ),
```

called by definition the _composite_ of `u` and `v`. One may therefore regard pairs `(X, ℱ)` of a topological space `X`
and a presheaf `ℱ` on `X` (with values in `𝑲`) as forming a _category_, with morphisms the pairs
`(ψ, θ) : (X, ℱ) → (Y, 𝒢)` consisting of a continuous map `ψ : X → Y` and a `ψ`-morphism `θ : 𝒢 → ℱ`.

**(3.5.3)** Let `ψ : X → Y` be a continuous map and `𝒢` a presheaf on `Y` with values in `𝑲`. We call an _inverse image
of_ `𝒢` _by_ `ψ` a pair `(𝒢′, ρ)` consisting of a _sheaf_ `𝒢′` on `X` with values in `𝑲` and a `ψ`-morphism `ρ : 𝒢 → 𝒢′`
(equivalently, a homomorphism `𝒢 → ψ_*(𝒢′)`) such that, for every _sheaf_ `ℱ` on `X` with values in `𝑲`, the map

```
(3.5.3.1)    Hom_X(𝒢′, ℱ) → Hom_ψ(𝒢, ℱ) = Hom_Y(𝒢, ψ_*(ℱ))
```

sending `v` to `ψ_*(v) ∘ ρ` is a _bijection_; this map being functorial in `ℱ`, it then defines an isomorphism of
functors in `ℱ`. As a solution of a universal problem, the pair `(𝒢′, ρ)`, when it exists, is _determined up to unique
isomorphism_. We then write `𝒢′ = ψ*(𝒢)`, `ρ = ρ_𝒢`, and by abuse of language we call `ψ*(𝒢)` the _inverse image sheaf
of_ `𝒢` _by_ `ψ`, with the understanding that `ψ*(𝒢)` is taken together with the canonical `ψ`-morphism
`ρ_𝒢 : 𝒢 → ψ_*(ψ*(𝒢))`, i.e. with the canonical homomorphism of presheaves on `Y`

```
(3.5.3.2)    ρ_𝒢 : 𝒢 → ψ_*(ψ*(𝒢)).
```

For any homomorphism `v : ψ*(𝒢) → ℱ` (where `ℱ` is a sheaf on `X` with values in `𝑲`), set
`v^♭ = ψ_*(v) ∘ ρ_𝒢 : 𝒢 → ψ_*(ℱ)`. By definition, _every_ morphism `u : 𝒢 → ψ_*(ℱ)` of presheaves is of the form `v^♭`
for a unique `v`, which we write `u^♯`. In other words, every such `u` factors uniquely as

```
(3.5.3.3)    u : 𝒢 ──ρ_𝒢──→ ψ_*(ψ*(𝒢)) ──ψ_*(u^♯)──→ ψ_*(ℱ).
```

**(3.5.4)** Suppose now that the category `𝑲` is such[^3-6] that _every_ presheaf `𝒢` on `Y` with values in `𝑲` admits
an inverse image by `ψ`, denoted `ψ*(𝒢)`.

We shall see that `ψ*(𝒢)` may be defined as a _covariant functor in_ `𝒢`, from presheaves on `Y` to sheaves on `X`, in
such a way that the isomorphism `v ↦ v^♭` is an _isomorphism of bifunctors_

```
(3.5.4.1)    Hom_X(ψ*(𝒢), ℱ) ⥲ Hom_Y(𝒢, ψ_*(ℱ))
```

in `𝒢` and `ℱ`.

Indeed, for every morphism `w : 𝒢_1 → 𝒢_2` of presheaves on `Y`, consider the composite
`𝒢_1 ──w──→ 𝒢_2 ──ρ_{𝒢_2}──→ ψ_*(ψ*(𝒢_2))`; to it corresponds a morphism `(ρ_{𝒢_2} ∘ w)^♯ : ψ*(𝒢_1) → ψ*(𝒢_2)`, which we
write `ψ*(w)`. By (3.5.3.3),

```
(3.5.4.2)    ψ_*(ψ*(w)) ∘ ρ_{𝒢_1} = ρ_{𝒢_2} ∘ w.
```

For every morphism `u : 𝒢_2 → ψ_*(ℱ)` (with `ℱ` a sheaf on `X` with values in `𝑲`), by (3.5.3.3), (3.5.4.2), and the
definition of `u^♭`,

```
(u^♯ ∘ ψ*(w))^♭ = ψ_*(u^♯) ∘ ψ_*(ψ*(w)) ∘ ρ_{𝒢_1} = ψ_*(u^♯) ∘ ρ_{𝒢_2} ∘ w = u ∘ w,
```

that is,

```
(3.5.4.3)    (u ∘ w)^♯ = u^♯ ∘ ψ*(w).
```

Taking in particular `u = ρ_{𝒢_3} ∘ w′` for a morphism `w′ : 𝒢_2 → 𝒢_3`, one gets
`ψ*(w′ ∘ w) = (ρ_{𝒢_3} ∘ w′ ∘ w)^♯ = (ρ_{𝒢_3} ∘ w′)^♯ ∘ ψ*(w) = ψ*(w′) ∘ ψ*(w)`, proving functoriality.

Finally, for a sheaf `ℱ` on `X` with values in `𝑲`, let `i_ℱ` be the identity of `ψ_*(ℱ)` and set

```
σ_ℱ = (i_ℱ)^♯ : ψ*(ψ_*(ℱ)) → ℱ;
```

(3.5.4.3) then gives the factorization

```
(3.5.4.4)    u^♯ : ψ*(𝒢) ──ψ*(u)──→ ψ*(ψ_*(ℱ)) ──σ_ℱ──→ ℱ
```

for every morphism `u : 𝒢 → ψ_*(ℱ)`. We call `σ_ℱ` the _canonical morphism_.

**(3.5.5)** Let `ψ′ : Y → Z` be continuous and suppose every presheaf `ℋ` on `Z` with values in `𝑲` admits an inverse
image `ψ′*(ℋ)`. Then (under the hypotheses of (3.5.4)) every presheaf `ℋ` on `Z` admits an inverse image by
`ψ″ = ψ′ ∘ ψ`, and there is a canonical functorial isomorphism

```
(3.5.5.1)    ψ″*(ℋ) ⥲ ψ*(ψ′*(ℋ)).
```

This follows at once from the definitions, given that `ψ″_* = ψ′_* ∘ ψ_*`. Moreover, if `u : 𝒢 → ψ_*(ℱ)` is a
`ψ`-morphism, `v : ℋ → ψ′_*(𝒢)` a `ψ′`-morphism, and `w = ψ′_*(u) ∘ v` their composite (3.5.2), one checks at once that
`w^♯` is the composite

```
w^♯ : ψ*(ψ′*(ℋ)) ──ψ*(v^♯)──→ ψ*(𝒢) ──u^♯──→ ℱ.
```

**(3.5.6)** Take in particular `ψ = 1_X : X → X`. If an inverse image by `ψ` of a presheaf `ℱ` on `X` exists, this
inverse image is called the _sheaf associated with the presheaf_ `ℱ`. Every morphism `u : ℱ → ℱ′` from `ℱ` to a sheaf
`ℱ′` with values in `𝑲` factors uniquely as

```
ℱ ──ρ_ℱ──→ 1_X*(ℱ) ──u^♯──→ ℱ′.
```

### 3.6. Simple and locally simple sheaves

<!-- label: 0.3.6 -->

**(3.6.1)** A presheaf `ℱ` on `X` with values in `𝑲` is called _constant_ if the canonical morphisms `ℱ(X) → ℱ(U)` are
_isomorphisms_ for every nonempty open `U ⊂ X`; note that `ℱ` is not necessarily a sheaf. A _sheaf_ `ℱ` is called
_simple_ if it is associated (3.5.6) with a constant presheaf. A sheaf `ℱ` is called _locally simple_ if every `x ∈ X`
admits an open neighborhood `U` such that `ℱ|U` is simple.

**(3.6.2)** Suppose `X` is _irreducible_ (2.1.1). The following are equivalent:

> a) `ℱ` is a constant presheaf on `X`; b) `ℱ` is a simple sheaf on `X`; c) `ℱ` is a locally simple sheaf on `X`.

Indeed, let `ℱ` be a constant presheaf on `X`. If `U, V` are nonempty open subsets, then `U ∩ V` is nonempty; so
`ℱ(X) → ℱ(U) → ℱ(U ∩ V)` and `ℱ(X) → ℱ(V) → ℱ(U ∩ V)` are isomorphisms, whence so are `ℱ(U) → ℱ(U ∩ V)` and
`ℱ(V) → ℱ(U ∩ V)`. One concludes at once that axiom (F) of (3.1.2) holds, so `ℱ` is isomorphic to its associated sheaf,
proving _a) ⇒ b)_.

Now let `(U_α)` be an open cover of `X` by nonempty open sets and `ℱ` a sheaf on `X` with `ℱ|U_α` simple for every `α`.
Since `U_α` is irreducible, `ℱ|U_α` is a constant presheaf by the above. Since `U_α ∩ U_β ≠ ∅`, both
`ℱ(U_α) → ℱ(U_α ∩ U_β)` and `ℱ(U_β) → ℱ(U_α ∩ U_β)` are isomorphisms, giving a canonical isomorphism
`θ_{αβ} : ℱ(U_α) → ℱ(U_β)` for every pair. Applying (F) with `U = X`, one sees that for every index `α_0`, the pair
`(ℱ(U_{α_0}), (θ_{α α_0}))` is a solution of the universal problem; by uniqueness, `ℱ(X) → ℱ(U_α)` is an isomorphism,
proving _c) ⇒ a)_.

### 3.7. Inverse images of presheaves of groups or rings

<!-- label: 0.3.7 -->

**(3.7.1)** We show that when `𝑲` is the category of sets, the inverse image by `ψ` of every presheaf `𝒢` always exists
(notation and hypotheses on `X`, `Y`, `ψ` as in (3.5.3)). For each open `U ⊂ X`, define `𝒢′(U)` as follows: an element
`s′` of `𝒢′(U)` is a family `(s′_z)_{z ∈ U}` with `s′_z ∈ 𝒢_{ψ(z)}` such that for every `x ∈ U`, the following holds:
there is an open neighborhood `V` of `ψ(x)` in `Y`, a neighborhood `W ⊂ ψ⁻¹(V) ∩ U` of `x`, and an element `s ∈ 𝒢(V)`
with `s′_z = s_{ψ(z)}` for `z ∈ W`. One checks at once that `U ↦ 𝒢′(U)` is a _sheaf_.

Now let `ℱ` be a sheaf of sets on `X`, and let `u : 𝒢 → ψ_*(ℱ)`, `v : 𝒢′ → ℱ` be morphisms. Define `u^♯` and `v^♭` as
follows: if `s′` is a section of `𝒢′` over a neighborhood `U` of `x ∈ X` and `V` is an open neighborhood of `ψ(x)` with
`s′_z = s_{ψ(z)}` for `z` in a neighborhood of `x` contained in `ψ⁻¹(V) ∩ U`, set `u^♯_x(s′_x) = u_{ψ(x)}(s_{ψ(x)})`. If
`s ∈ 𝒢(V)` for `V` open in `Y`, let `v^♭(s)` be the section of `ℱ` over `ψ⁻¹(V)`, image under `v` of the section `s′` of
`𝒢′` with `s′_z = s_{ψ(z)}` for `z ∈ ψ⁻¹(V)`. The canonical homomorphism (3.5.3) `ρ : 𝒢 → ψ_*(ψ*(𝒢))` is defined by: for
`V ⊂ Y` open and `s ∈ Γ(V, 𝒢)`, `ρ(s)` is the section `(s_{ψ(z)})_{z ∈ ψ⁻¹(V)}` of `ψ*(𝒢)` over `ψ⁻¹(V)`. The relations
`(u^♭)^♯ = u`, `(v^♯)^♭ = v`, and `v^♭ = ψ_*(v) ∘ ρ` are immediate.

One checks that if `w : 𝒢_1 → 𝒢_2` is a morphism of presheaves of sets on `Y`, then `ψ*(w)` is given explicitly by: if
`s′ = (s′_z)_{z ∈ U}` is a section of `ψ*(𝒢_1)` over an open `U ⊂ X`, then `(ψ*(w))(s′) = (w_{ψ(z)}(s′_z))_{z ∈ U}`. For
every open `V ⊂ Y`, the inverse image of `𝒢|V` by `ψ|ψ⁻¹(V)` is identical with `ψ*(𝒢)|ψ⁻¹(V)`.

When `ψ = 1_X` is the identity, the construction of `𝒢′` recovers the usual sheaf of sets associated with a presheaf (G,
II, 1.2). The above goes through unchanged when `𝑲` is the category of groups or rings (not necessarily commutative).

When `X` is an arbitrary subspace of a topological space `Y` and `j : X → Y` is the canonical injection, the _inverse
image_ `j*(𝒢)`, when it exists, is called the sheaf _induced on_ `X` _by_ `𝒢`; for sheaves of sets (or groups, or rings)
this recovers the usual definition (G, II, 1.5).

**(3.7.2)** Keeping the notation and hypotheses of (3.5.3), suppose `𝒢` is a _sheaf_ of groups (resp. rings) on `Y`. The
construction of sections of `ψ*(𝒢)` (3.7.1) shows, in view of (3.4.4), that the stalk homomorphism
`ψ_x ∘ ρ_{ψ(x)} : 𝒢_{ψ(x)} → (ψ*(𝒢))_x` is a _functorial isomorphism in_ `𝒢`, which allows one to identify these two
stalks. Under this identification, `u^♯_x` is identical with the homomorphism defined in (3.5.1), and in particular

```
Supp(ψ*(𝒢)) = ψ⁻¹(Supp(𝒢)).
```

An immediate consequence is that _the functor_ `ψ*(𝒢)` _is exact in_ `𝒢` in the abelian category of sheaves of abelian
groups.

### 3.8. Sheaves of pseudo-discrete spaces

<!-- label: 0.3.8 -->

**(3.8.1)** Let `X` be a topological space whose topology admits a basis `𝔅` of _quasi-compact_ open sets. Let `ℱ` be a
sheaf of sets on `X`. Endowing each `ℱ(U)` with the _discrete_ topology makes `U ↦ ℱ(U)` a _presheaf of topological
spaces_. We shall see that there exists a _sheaf of topological spaces_ `ℱ′` associated with `ℱ` (3.5.6) such that
`Γ(U, ℱ′)` is the discrete space `ℱ(U)` for every _quasi-compact_ open `U`. For this, it suffices to show that the
presheaf `U ↦ ℱ(U)` of topological spaces _on_ `𝔅` satisfies (F₀) of (3.2.2), and more generally that if `U` is a
quasi-compact open set and `(U_α)` is a cover of `U` by elements of `𝔅`, then the coarsest topology `𝒯` on `Γ(U, ℱ)`
making the maps `Γ(U, ℱ) → Γ(U_α, ℱ)` continuous is the _discrete_ topology. There is a finite set of indices `α_i` with
`U = ⋃_i U_{α_i}`. Let `s ∈ Γ(U, ℱ)` and let `s_i` be its image in `Γ(U_{α_i}, ℱ)`; the intersection of the inverse
images of `{s_i}` is by definition a `𝒯`-neighborhood of `s`. But since `ℱ` is a sheaf of sets and the `U_{α_i}` cover
`U`, this intersection reduces to `{s}`, whence the assertion.

Note that if `U` is a non-quasi-compact open subset of `X`, the topological space `Γ(U, ℱ′)` still has `Γ(U, ℱ)` as
underlying set, but its topology is in general not discrete: it is the coarsest making the maps `Γ(U, ℱ) → Γ(V, ℱ)`
continuous, for `V ∈ 𝔅`, `V ⊂ U` (the `Γ(V, ℱ)` being discrete).

The above applies without change to sheaves of groups or rings (not necessarily commutative), associating with them
sheaves of _topological groups_ or _topological rings_ respectively. For brevity, we say that `ℱ′` is the _sheaf of
pseudo-discrete spaces_ (resp. groups, rings) _associated_ with the sheaf of sets (resp. groups, rings) `ℱ`.

**(3.8.2)** Let `ℱ`, `𝒢` be sheaves of sets (resp. groups, rings) on `X` and `u : ℱ → 𝒢` a homomorphism. Then `u` is
also a _continuous_ homomorphism `ℱ′ → 𝒢′`, where `ℱ′`, `𝒢′` are the associated pseudo-discrete sheaves; this follows
from (3.2.5).

**(3.8.3)** Let `ℱ` be a sheaf of sets, `ℋ` a subsheaf of `ℱ`, and `ℱ′`, `ℋ′` the associated pseudo-discrete sheaves.
For every open `U ⊂ X`, `Γ(U, ℋ′)` is _closed_ in `Γ(U, ℱ′)`: indeed, it is the intersection of the inverse images of
`Γ(V, ℋ)` (for `V ∈ 𝔅`, `V ⊂ U`) under the continuous maps `Γ(U, ℱ) → Γ(V, ℱ)`, and `Γ(V, ℋ)` is closed in the discrete
space `Γ(V, ℱ)`.

[^3-1]: This is a special case of the general notion of (non-filtered) _projective limit_; see (T, I, 1.8) and the book
    in preparation announced in the Introduction.

[^3-2]: One can prove that this also means that the canonical functor `𝑲 → (Ens)` commutes with projective limits (not
    necessarily filtered).

[^3-3]: This is because in the category `𝑲`, every morphism that is a _bijection_ (as a map of sets) is an
    _isomorphism_. This is no longer true when `𝑲` is, for example, the category of topological spaces.

[^3-4]: If `X` is a _Noetherian_ space, one can still define `ℱ′(U)` and show that it is a presheaf in the ordinary
    sense, assuming only that `𝑲` admits projective limits for _finite_ projective systems. Indeed, for any open
    `U`, there is a finite cover `(V_i)` of `U` by elements of `𝔅`; for each pair `(i, j)`, choose a finite cover
    `(V_{ijk})` of `V_i ∩ V_j` by elements of `𝔅`. Let `I` be the set of indices `i` and triples `(i, j, k)`,
    ordered by the relations `i > (i, j, k)` and `j > (i, j, k)`; take `ℱ′(U)` to be the projective limit of the
    system of the `ℱ(V_i)` and `ℱ(V_{ijk})`. One checks easily that this is independent of the covers and that
    `U ↦ ℱ′(U)` is a presheaf.

[^3-5]: This also means that the pair `(ℱ(U), (ρ_α))` with `ρ_α = ρ^U_{U_α}` is a solution of the universal problem
    (3.1.1) defined by `A_α = ℱ(U_α)`, `A_{αβ} = ∏ ℱ(V)` (for `V ∈ 𝔅` with `V ⊂ U_α ∩ U_β`), and
    `ρ_{αβ} = (ρ^V_{U_α}) : ℱ(U_α) → ∏ ℱ(V)` defined by: for `V, V′, W ∈ 𝔅` with `V ∪ V′ ⊂ U_α ∩ U_β`, `W ⊂ V ∩ V′`,
    `ρ^V_W ∘ ρ^{U_α}_V = ρ^{V′}_W ∘ ρ^{U_α}_{V′}`.

[^3-6]: In the book cited in the Introduction, we shall give very general conditions on `𝑲` ensuring the existence of
    inverse images of presheaves with values in `𝑲`.
