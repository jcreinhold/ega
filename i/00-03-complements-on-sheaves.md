# Chapter 0 — Preliminaries

## §3. Complements on Sheaves

<!-- label: 0.3 -->

### 3.1. Sheaves with values in a category

<!-- label: 0.3.1 -->

**(3.1.1)** Let $\mathit{K}$ be a category, let $(A_{\alpha})_{\alpha \in I}$ and $(A_{\alpha \beta})_{(\alpha,\beta)
\in I \times I}$ be two families of objects of $\mathit{K}$ with $A_{\beta \alpha} = A_{\alpha \beta}$, and let
$(\rho_{\alpha \beta})_{(\alpha,\beta) \in I \times I}$ be a family of morphisms $\rho_{\alpha \beta} : A_{\alpha} \to
A_{\alpha \beta}$. We say that a pair consisting of an object $A$ of $\mathit{K}$ and a family of morphisms
$\rho_{\alpha} : A \to A_{\alpha}$ is a _solution of the universal problem_ defined by the data $(A_{\alpha})$,
$(A_{\alpha \beta})$, $(\rho_{\alpha \beta})$ if, for every object $B$ of $\mathit{K}$, the map sending $f \in
\operatorname{Hom}(B, A)$ to $(\rho_{\alpha} \circ f) \in \prod_{\alpha} \operatorname{Hom}(B, A_{\alpha})$ is a
_bijection_ of $\operatorname{Hom}(B, A)$ onto the set of $(f_{\alpha})$ such that $\rho_{\alpha \beta} \circ f_{\alpha}
= \rho_{\beta \alpha} \circ f_{\beta}$ for every pair of indices $(\alpha, \beta)$. One sees at once that if such a
solution exists, it is unique up to isomorphism.

**(3.1.2)** We shall not recall the definition of a _presheaf_ $U \mapsto \mathcal{F}(U)$ on a topological space $X$
with values in a category $\mathit{K}$ (G, I, 1.9); we say that such a presheaf is a _sheaf with values in_ $\mathit{K}$
if it satisfies the following axiom:

> (F) _For every cover_ $(U_{\alpha})$ _of an open set_ $U \subset X$ _by open sets_ $U_{\alpha} \subset U$, _if_
> $\rho_{\alpha}$ (resp. $\rho_{\alpha \beta}$) _denotes the restriction morphism_
>
> ```
> ℱ(U) → ℱ(U_α)    (resp. ℱ(U_α) → ℱ(U_α ∩ U_β)),
> ```
>
> _then the pair_ $(\mathcal{F}(U), (\rho_{\alpha}))$ _is a solution of the universal problem for_
> $(\mathcal{F}(U_{\alpha}))$, $(\mathcal{F}(U_{\alpha} \cap U_{\beta}))$, _and_ $(\rho_{\alpha \beta})$
> _(3.1.1)._[^3-1]

Equivalently, for every object $T$ of $\mathit{K}$, the family $U \mapsto \operatorname{Hom}(T, \mathcal{F}(U))$ is a
_sheaf of sets_.

**(3.1.3)** Suppose $\mathit{K}$ is the category defined by a "species of structure with morphisms" $\Sigma$ — the
objects of $\mathit{K}$ being the sets endowed with structures of species $\Sigma$, and the morphisms those of $\Sigma$.
Suppose moreover that $\mathit{K}$ satisfies:

> (E) If $(A, (\rho_{\alpha}))$ is a solution of a universal mapping problem _in the category_ $\mathit{K}$ for families
> $(A_{\alpha})$, $(A_{\alpha \beta})$, $(\rho_{\alpha \beta})$, then it is also a solution of the universal mapping
> problem for the same families _in the category of sets_ — that is, when one regards $A$, the $A_{\alpha}$, and the
> $A_{\alpha \beta}$ as sets and $\rho_{\alpha}$, $\rho_{\alpha \beta}$ as maps.[^3-2]

Under these conditions, axiom (F) implies that, viewed as a presheaf of sets, $U \mapsto \mathcal{F}(U)$ is a _sheaf_.
Moreover, for a map $u : T \to \mathcal{F}(U)$ to be a morphism of $\mathit{K}$, it is necessary and sufficient, by (F),
that each $\rho_{\alpha} \circ u$ be a morphism $T \to \mathcal{F}(U_{\alpha})$ — that is, that the structure of species
$\Sigma$ on $\mathcal{F}(U)$ be the _initial structure_ for the morphisms $\rho_{\alpha}$. Conversely, suppose that a
presheaf $U \mapsto \mathcal{F}(U)$ on $X$ with values in $\mathit{K}$ is a _sheaf of sets_ and satisfies the preceding
condition; then it satisfies (F), hence is a _sheaf with values in_ $\mathit{K}$.

**(3.1.4)** When $\Sigma$ is the species of group or ring structures, the fact that the presheaf $U \mapsto
\mathcal{F}(U)$ with values in $\mathit{K}$ is a sheaf of _sets_ implies _ipso facto_ that it is a sheaf _with values
in_ $\mathit{K}$ — that is, a sheaf of groups or rings in the sense of (G).[^3-3] This is no longer the case when, for
example, $\mathit{K}$ is the category of _topological rings_ (with continuous representations as morphisms): a sheaf
with values in $\mathit{K}$ is then a sheaf of sets $U \mapsto \mathcal{F}(U)$ such that for every open $U$ and every
cover of $U$ by open $U_{\alpha} \subset U$, the topology of $\mathcal{F}(U)$ is _the coarsest_ making the
representations $\mathcal{F}(U) \to \mathcal{F}(U_{\alpha})$ continuous. In this case we say that $\mathcal{F}(U)$,
viewed as a sheaf of rings (without topology), is _underlying_ the sheaf of topological rings $U \mapsto
\mathcal{F}(U)$. The morphisms $u_{V} : \mathcal{F}(V) \to \mathcal{G}(V)$ (for arbitrary open $V \subset X$) of sheaves
of topological rings are thus homomorphisms of the underlying sheaves of rings such that $u_{V}$ is _continuous_ for
every open $V$; to distinguish them from arbitrary homomorphisms of the underlying sheaves of rings, we call them
_continuous homomorphisms_ of sheaves of topological rings. Analogous definitions and conventions hold for sheaves of
topological spaces or topological groups.

**(3.1.5)** It is clear that for any category $\mathit{K}$, if $\mathcal{F}$ is a presheaf (resp. sheaf) on $X$ with
values in $\mathit{K}$ and $U$ is an open subset of $X$, then the $\mathcal{F}(V)$ for $V \subset U$ form a presheaf
(resp. sheaf) with values in $\mathit{K}$, called the presheaf (resp. sheaf) _induced_ by $\mathcal{F}$ on $U$ and
written $\mathcal{F}|U$.

For every morphism $u : \mathcal{F} \to \mathcal{G}$ of presheaves on $X$ with values in $\mathit{K}$, we shall write
$u|U$ for the morphism $\mathcal{F}|U \to \mathcal{G}|U$ given by the $u_{V}$ for $V \subset U$.

**(3.1.6)** Suppose now that $\mathit{K}$ admits _inductive limits [modern: direct limits]_ (T, 1.8); then, for every
presheaf (and in particular every sheaf) $\mathcal{F}$ on $X$ with values in $\mathit{K}$ and every $x \in X$, one can
define the _stalk_ $\mathcal{F}_{x}$ as the object of $\mathit{K}$ given by the inductive limit of the filtered (by
$\supset$) family of open neighborhoods $U$ of $x$ in $X$, with the restriction morphisms $\rho^{V}_{U} : \mathcal{F}(V)
\to \mathcal{F}(U)$. If $u : \mathcal{F} \to \mathcal{G}$ is a morphism of presheaves with values in $\mathit{K}$, one
defines for each $x \in X$ the morphism $u_{x} : \mathcal{F}_{x} \to \mathcal{G}_{x}$ as the inductive limit of the
$u_{U} : \mathcal{F}(U) \to \mathcal{G}(U)$ over the system of open neighborhoods of $x$; this makes $\mathcal{F}_{x}$ a
covariant functor in $\mathcal{F}$, with values in $\mathit{K}$, for each $x \in X$.

When in addition $\mathit{K}$ is defined by a species of structure with morphisms $\Sigma$, the elements of
$\mathcal{F}(U)$ are still called _sections over_ $U$ of the _sheaf_ $\mathcal{F}$ with values in $\mathit{K}$, and we
then write $\Gamma(U, \mathcal{F})$ in place of $\mathcal{F}(U)$; for $s \in \Gamma(U, \mathcal{F})$ and $V$ an open
subset of $U$, we write $s|V$ in place of $\rho^{U}_{V}(s)$; for $x \in U$, the canonical image of $s$ in
$\mathcal{F}_{x}$ is the _germ_ of $s$ at $x$, written $s_{x}$. (We shall never use the notation $s(x)$ in this sense,
since it is reserved for another notion concerning the particular sheaves considered in this treatise (5.5.1).)

If $u : \mathcal{F} \to \mathcal{G}$ is a morphism of sheaves with values in $\mathit{K}$, we shall write $u(s)$ in
place of $u_{V}(s)$ for $s \in \Gamma(V, \mathcal{F})$.

If $\mathcal{F}$ is a sheaf of abelian groups, rings, or modules, the set of $x \in X$ such that $\mathcal{F}_{x} \neq
{0}$ is called the _support_ of $\mathcal{F}$, written $Supp(\mathcal{F})$; this set is not necessarily closed in $X$.

When $\mathit{K}$ is defined by a species of structure with morphisms, _we systematically refrain from introducing the
"étalé-space" viewpoint_ for sheaves with values in $\mathit{K}$. In other words, we never view a sheaf as a topological
space (nor even as the disjoint union of its stalks), and we shall not view a morphism $u : \mathcal{F} \to \mathcal{G}$
of such sheaves on $X$ as a continuous map of topological spaces.

### 3.2. Presheaves on a basis of open sets

<!-- label: 0.3.2 -->

**(3.2.1)** We restrict ourselves in what follows to categories $\mathit{K}$ admitting _projective limits \[modern: inverse
limits\]_ (in the generalized sense — corresponding to preordered sets that are not necessarily filtered; cf. (T, 1.8)).
Let $X$ be a topological space and $\mathfrak{B}$ a basis of open sets for the topology of $X$. We call a _presheaf on_ $\mathfrak{B}$ _with
values in_ $\mathit{K}$ a family of objects $\mathcal{F}(U) \in \mathit{K}$ attached to each $U \in \mathfrak{B}$, together with morphisms $\rho^{V}_{U} : \mathcal{F}(V) \to \mathcal{F}(U)$
defined for every pair $(U, V)$ of elements of $\mathfrak{B}$ with $U \subset V$, satisfying $\rho^{U}_{U} = identity$ and
$\rho^{W}_{U} = \rho^{V}_{U} \circ \rho^{W}_{V}$ whenever $U \subset V \subset W$ in $\mathfrak{B}$. To such a family we associate a _presheaf with values in_ $\mathit{K}$,
$U \mapsto \mathcal{F}'(U)$ in the usual sense, by setting

```
ℱ′(U) = lim⃖_{V ∈ 𝔅, V ⊂ U} ℱ(V),
```

where $V$ ranges over the (in general non-filtered) ordered set of $V \in \mathfrak{B}$ with $V \subset U$; the
$\mathcal{F}(V)$ form a projective system for the $\rho^{W}_{V}$ ($V \subset W \subset U$, $V, W \in \mathfrak{B}$).
Indeed, if $U, U'$ are open with $U \subset U'$, define $\rho'^{U'}_{U}$ as the projective limit (over $V \subset U$) of
the canonical morphisms $\mathcal{F}'(U') \to \mathcal{F}(V)$ — that is, the unique morphism $\mathcal{F}'(U') \to
\mathcal{F}'(U)$ whose composition with each canonical $\mathcal{F}'(U) \to \mathcal{F}(V)$ gives the canonical
$\mathcal{F}'(U') \to \mathcal{F}(V)$. The transitivity of the $\rho'^{U'}_{U}$ follows immediately. Moreover, for $U
\in \mathfrak{B}$ the canonical morphism $\mathcal{F}'(U) \to \mathcal{F}(U)$ is an _isomorphism_, allowing one to
identify these two objects.[^3-4]

**(3.2.2)** For the presheaf $\mathcal{F}'$ defined above to be a _sheaf_, it is necessary and sufficient that the
presheaf $\mathcal{F}$ on $\mathfrak{B}$ satisfy:

> (F₀) _For every cover_ $(U_{\alpha})$ _of_ $U \in \mathfrak{B}$ _by sets_ $U_{\alpha} \in \mathfrak{B}$ _contained in_
> $U$, _and for every object_ $T \in \mathit{K}$, _the map sending_ $f \in \operatorname{Hom}(T, \mathcal{F}(U))$ _to_
> $(\rho^{U}_{U_{\alpha}} \circ f) \in \prod_{\alpha} \operatorname{Hom}(T, \mathcal{F}(U_{\alpha}))$ _is a bijection
> of_ $\operatorname{Hom}(T, \mathcal{F}(U))$ _onto the set of_ $(f_{\alpha})$ _such that_ $\rho^{U_{\alpha}}_{V} \circ
> f_{\alpha} = \rho^{U_{\beta}}_{V} \circ f_{\beta}$ _for every pair_ $(\alpha, \beta)$ _and every_ $V \in \mathfrak{B}$
> _with_ $V \subset U_{\alpha} \cap U_{\beta}$.[^3-5]

The condition is plainly necessary. For sufficiency, consider a second basis $\mathfrak{B}'$ for the topology of $X$
with $\mathfrak{B}' \subset \mathfrak{B}$, and let $\mathcal{F}''$ denote the presheaf obtained from the subfamily
$(\mathcal{F}(V))_{V \in \mathfrak{B}'}$. Then $\mathcal{F}''$ is _canonically isomorphic_ to $\mathcal{F}'$: for any
open $U$, the projective limit (over $V \in \mathfrak{B}'$, $V \subset U$) of the canonical $\mathcal{F}'(U) \to
\mathcal{F}(V)$ is a morphism $\mathcal{F}'(U) \to \mathcal{F}''(U)$. For $U \in \mathfrak{B}$ this morphism is an
isomorphism, since by hypothesis each canonical $\mathcal{F}'(U) \to \mathcal{F}(V)$ for $V \in \mathfrak{B}'$, $V
\subset U$, factors as $\mathcal{F}'(U) \to \mathcal{F}''(U) \to \mathcal{F}(V)$, and one checks at once that the
composites $\mathcal{F}'(U) \to \mathcal{F}''(U) \to \mathcal{F}'(U)$ and $\mathcal{F}''(U) \to \mathcal{F}'(U) \to
\mathcal{F}''(U)$ are identities. This being so, for every open $U$ the morphisms $\mathcal{F}'(U) \to \mathcal{F}''(W)
= \mathcal{F}(W)$ for $W \in \mathfrak{B}$, $W \subset U$, satisfy the conditions characterizing the projective limit of
the $\mathcal{F}(W)$ ($W \in \mathfrak{B}$, $W \subset U$), which proves our assertion by uniqueness of projective
limits up to isomorphism.

That said, let $U$ be an arbitrary open set of $X$, $(U_{\alpha})$ a cover of $U$ by open sets contained in $U$, and
$\mathfrak{B}'$ the subfamily of $\mathfrak{B}$ consisting of those elements of $\mathfrak{B}$ contained in some
$U_{\alpha}$. Plainly $\mathfrak{B}'$ is still a basis for the topology of $X$, so $\mathcal{F}'(U)$ (resp.
$\mathcal{F}'(U_{\alpha})$) is the projective limit of the $\mathcal{F}(V)$ for $V \in \mathfrak{B}'$, $V \subset U$
(resp. $V \subset U_{\alpha}$); axiom (F) is then verified at once, by the definition of projective limit.

When (F₀) holds, we shall say by abuse of language that the presheaf $\mathcal{F}$ on the basis $\mathfrak{B}$ _is a
sheaf_.

**(3.2.3)** Let $\mathcal{F}$, $\mathcal{G}$ be two presheaves on the basis $\mathfrak{B}$ with values in $\mathit{K}$.
A _morphism_ $u : \mathcal{F} \to \mathcal{G}$ is a family $(u_{V})_{V \in \mathfrak{B}}$ of morphisms $u_{V} :
\mathcal{F}(V) \to \mathcal{G}(V)$ satisfying the usual compatibility with the restriction morphisms $\rho^{W}_{V}$.
With the notation of (3.2.1), one obtains a morphism $u' : \mathcal{F}' \to \mathcal{G}'$ of the corresponding ordinary
presheaves by taking for $u'_{U}$ the projective limit of the $u_{V}$ for $V \in \mathfrak{B}$, $V \subset U$; the
compatibility with the $\rho'^{U'}_{U}$ follows from the functoriality of projective limits.

**(3.2.4)** If $\mathit{K}$ admits inductive limits and $\mathcal{F}$ is a presheaf on $\mathfrak{B}$ with values in
$\mathit{K}$, then for every $x \in X$ the neighborhoods of $x$ belonging to $\mathfrak{B}$ form a cofinal subset (for
$\supset$) of the neighborhoods of $x$; hence if $\mathcal{F}'$ is the ordinary presheaf associated with $\mathcal{F}$,
the stalk $\mathcal{F}'_{x}$ equals $\varinjlim \mathcal{F}(V)$ over $V \in \mathfrak{B}$, $x \in V$. If $u :
\mathcal{F} \to \mathcal{G}$ is a morphism of presheaves on $\mathfrak{B}$ and $u' : \mathcal{F}' \to \mathcal{G}'$ the
corresponding morphism of ordinary presheaves, then $u'_{x}$ is the inductive limit of the $u_{V} : \mathcal{F}(V) \to
\mathcal{G}(V)$ for $V \in \mathfrak{B}$, $x \in V$.

**(3.2.5)** Returning to the general setting of (3.2.1): if $\mathcal{F}$ is an ordinary _sheaf_ with values in
$\mathit{K}$ and $\mathcal{F}_{1}$ is the sheaf on $\mathfrak{B}$ obtained by restriction of $\mathcal{F}$ to
$\mathfrak{B}$, then the ordinary sheaf $\mathcal{F}'_{1}$ obtained from $\mathcal{F}_{1}$ by the construction of
(3.2.1) is canonically isomorphic to $\mathcal{F}$, by (F) and the uniqueness of projective limits. We shall ordinarily
identify $\mathcal{F}$ and $\mathcal{F}'_{1}$.

If $\mathcal{G}$ is a second ordinary sheaf on $X$ with values in $\mathit{K}$ and $u : \mathcal{F} \to \mathcal{G}$ a
morphism, the preceding remark shows that giving the $u_{V} : \mathcal{F}(V) \to \mathcal{G}(V)$ _for_ $V \in
\mathfrak{B}$ _alone_ determines $u$ completely. Conversely, given $u_{V}$ for $V \in \mathfrak{B}$ satisfying the
commutativity diagrams with the restriction morphisms $\rho^{W}_{V}$ for $V, W \in \mathfrak{B}$ and $V \subset W$,
there is a unique morphism $u' : \mathcal{F} \to \mathcal{G}$ with $u'_{V} = u_{V}$ for every $V \in \mathfrak{B}$
(3.2.3).

**(3.2.6)** Continue to assume that $\mathit{K}$ admits projective limits. Then the category of _sheaves on_ $X$ _with
values in_ $\mathit{K}$ also admits _projective limits_: if $(\mathcal{F}_{\lambda})$ is a projective system of sheaves
on $X$ with values in $\mathit{K}$, then the $\mathcal{F}(U) = \varprojlim_{\lambda} \mathcal{F}_{\lambda}(U)$ define a
presheaf with values in $\mathit{K}$, and axiom (F) holds by the transitivity of projective limits; that $\mathcal{F}$
is then the projective limit of the $\mathcal{F}_{\lambda}$ is immediate.

When $\mathit{K}$ is the category of sets, then for every projective system $(\mathcal{H}_{\lambda})$ with
$\mathcal{H}_{\lambda}$ a _subsheaf_ of $\mathcal{F}_{\lambda}$ for each $\lambda$, $\varprojlim_{\lambda}
\mathcal{H}_{\lambda}$ is canonically identified with a subsheaf of $\varprojlim_{\lambda} \mathcal{F}_{\lambda}$. If
$\mathit{K}$ is the category of abelian groups, the covariant functor $\varprojlim_{\lambda} \mathcal{F}_{\lambda}$ is
_additive_ and _left exact_.

### 3.3. Gluing of sheaves

<!-- label: 0.3.3 -->

**(3.3.1)** Continue to assume that $\mathit{K}$ admits (generalized) projective limits. Let $X$ be a topological space,
$\mathfrak{U} = (U_{\lambda})_{\lambda \in L}$ an open cover of $X$, and for each $\lambda \in L$ let
$\mathcal{F}_{\lambda}$ be a sheaf on $U_{\lambda}$ with values in $\mathit{K}$. Suppose that for every pair $(\lambda,
\mu)$ we are given an _isomorphism_ $\theta_{\lambda \mu} : \mathcal{F}_{\mu}|(U_{\lambda} \cap U_{\mu})
\xrightarrow{\sim} \mathcal{F}_{\lambda}|(U_{\lambda} \cap U_{\mu})$, and that for every triple $(\lambda, \mu, \nu)$,
writing $\theta'_{\lambda \mu}, \theta'_{\mu \nu}, \theta'_{\lambda \nu}$ for the restrictions of $\theta_{\lambda \mu},
\theta_{\mu \nu}, \theta_{\lambda \nu}$ to $U_{\lambda} \cap U_{\mu} \cap U_{\nu}$, one has $\theta'_{\lambda \nu} =
\theta'_{\lambda \mu} \circ \theta'_{\mu \nu}$ (_the gluing condition for the_ $\theta_{\lambda \mu}$). Then there is a
sheaf $\mathcal{F}$ on $X$ with values in $\mathit{K}$, and for each $\lambda$ an isomorphism $\eta_{\lambda} :
\mathcal{F}|U_{\lambda} \xrightarrow{\sim} \mathcal{F}_{\lambda}$, such that for every $(\lambda, \mu)$, writing
$\eta'_{\lambda}$ and $\eta'_{\mu}$ for the restrictions of $\eta_{\lambda}$ and $\eta_{\mu}$ to $U_{\lambda} \cap
U_{\mu}$, one has $\theta_{\lambda \mu} = \eta'_{\lambda} \circ \eta'^{-1}_{\mu}$. Moreover, $\mathcal{F}$ and the
$\eta_{\lambda}$ are determined up to unique isomorphism by these conditions. Uniqueness follows at once from (3.2.5).
For existence, let $\mathfrak{B}$ be the basis of open sets contained in some $U_{\lambda}$; choose (via Hilbert's
$\tau$-function) one of the $\mathcal{F}_{\lambda}(U)$ for some $\lambda$ with $U \subset U_{\lambda}$; call this object
$\mathcal{F}(U)$. The $\rho^{V}_{U}$ for $U \subset V$, $U, V \in \mathfrak{B}$, are defined in the obvious way (using
the $\theta_{\lambda \mu}$), and transitivity follows from the gluing condition. Axiom (F₀) is then immediate, so the
presheaf on $\mathfrak{B}$ so defined is a sheaf; from it the general construction (3.2.1) yields an ordinary sheaf,
again written $\mathcal{F}$, with the required property. We say that $\mathcal{F}$ is obtained by _gluing the_
$\mathcal{F}_{\lambda}$ _via the_ $\theta_{\lambda \mu}$, and we ordinarily identify $\mathcal{F}_{\lambda}$ and
$\mathcal{F}|U_{\lambda}$ via $\eta_{\lambda}$.

It is clear that every sheaf $\mathcal{F}$ on $X$ with values in $\mathit{K}$ may be viewed as obtained by gluing the
sheaves $\mathcal{F}_{\lambda} = \mathcal{F}|U_{\lambda}$ (where $(U_{\lambda})$ is any open cover of $X$) via the
identity isomorphisms $\theta_{\lambda \mu}$.

**(3.3.2)** With the same notation, let $\mathcal{G}_{\lambda}$ be a second sheaf on $U_{\lambda}$ (for each $\lambda
\in L$) with values in $\mathit{K}$, and suppose given for each $(\lambda, \mu)$ an isomorphism $\omega_{\lambda \mu} :
\mathcal{G}_{\mu}|(U_{\lambda} \cap U_{\mu}) \xrightarrow{\sim} \mathcal{G}_{\lambda}|(U_{\lambda} \cap U_{\mu})$
satisfying the gluing condition. Suppose finally given for each $\lambda$ a morphism $u_{\lambda} :
\mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$ such that the diagrams

```
(3.3.2.1)    ℱ_μ|(U_λ ∩ U_μ) ──u_μ──→ 𝒢_μ|(U_λ ∩ U_μ)
                   │                          │
                   ↓                          ↓
             ℱ_λ|(U_λ ∩ U_μ) ──u_λ──→ 𝒢_λ|(U_λ ∩ U_μ)
```

commute. Then if $\mathcal{G}$ is obtained by gluing the $\mathcal{G}_{\lambda}$ via the $\omega_{\lambda \mu}$, there
is a unique morphism $u : \mathcal{F} \to \mathcal{G}$ such that the diagrams

```
ℱ|U_λ ──u|U_λ──→ 𝒢|U_λ
  │                 │
  ↓                 ↓
 ℱ_λ ────u_λ───→  𝒢_λ
```

commute; this follows at once from (3.2.3). The correspondence between the family $(u_{\lambda})$ and $u$ is a
functorial bijection of the subset of $\prod_{\lambda} \operatorname{Hom}(\mathcal{F}_{\lambda}, \mathcal{G}_{\lambda})$
satisfying (3.3.2.1) onto $\operatorname{Hom}(\mathcal{F}, \mathcal{G})$.

**(3.3.3)** With the notation of (3.3.1), let $V$ be an open subset of $X$. The restrictions of the $\theta_{\lambda
\mu}$ to $V \cap U_{\lambda} \cap U_{\mu}$ plainly satisfy the gluing condition for the induced sheaves
$\mathcal{F}_{\lambda}|(V \cap U_{\lambda})$, and the sheaf on $V$ obtained by gluing these is canonically identified
with $\mathcal{F}|V$.

### 3.4. Direct images of presheaves

<!-- label: 0.3.4 -->

**(3.4.1)** Let $X$, $Y$ be topological spaces and $\psi : X \to Y$ a continuous map. Let $\mathcal{F}$ be a presheaf on
$X$ with values in $\mathit{K}$; for every open $U \subset Y$, set $\mathcal{G}(U) = \mathcal{F}(\psi^{-1}(U))$, and for
$U \subset V$ open in $Y$ let $\rho'^{V}_{U}$ be the morphism $\mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}(\psi^{-1}(U))$.
The $\mathcal{G}(U)$ and $\rho'^{V}_{U}$ define a _presheaf_ on $Y$ with values in $\mathit{K}$, called the _direct
image of_ $\mathcal{F}$ _by_ $\psi$ and written $\psi_{*}(\mathcal{F})$. If $\mathcal{F}$ is a sheaf, axiom (F) for
$\mathcal{G}$ is immediate, so $\psi_{*}(\mathcal{F})$ is a sheaf.

**(3.4.2)** Let $\mathcal{F}_{1}$, $\mathcal{F}_{2}$ be presheaves on $X$ with values in $\mathit{K}$ and let $u :
\mathcal{F}_{1} \to \mathcal{F}_{2}$ be a morphism. As $U$ ranges over the open subsets of $Y$, the family
$u_{\psi^{-1}(U)} : \mathcal{F}_{1}(\psi^{-1}(U)) \to \mathcal{F}_{2}(\psi^{-1}(U))$ satisfies the compatibility with
restriction morphisms, defining $\psi_{*}(u) : \psi_{*}(\mathcal{F}_{1}) \to \psi_{*}(\mathcal{F}_{2})$. If $v :
\mathcal{F}_{2} \to \mathcal{F}_{3}$ is a further morphism, $\psi_{*}(v \circ u) = \psi_{*}(v) \circ \psi_{*}(u)$; that
is, $\psi_{*}$ is a _covariant functor_ from presheaves (resp. sheaves) on $X$ with values in $\mathit{K}$ to presheaves
(resp. sheaves) on $Y$ with values in $\mathit{K}$.

**(3.4.3)** Let $Z$ be a third topological space, $\psi' : Y \to Z$ continuous, and set $\psi'' = \psi' \circ \psi$. One
has $\psi''_{*}(\mathcal{F}) = \psi'_{*}(\psi_{*}(\mathcal{F}))$ for every presheaf $\mathcal{F}$ on $X$ with values in
$\mathit{K}$; for every morphism $u : \mathcal{F} \to \mathcal{G}$, $\psi''_{*}(u) = \psi'_{*}(\psi_{*}(u))$. In other
words, $\psi''_{*}$ is the _composite_ of $\psi'_{*}$ and $\psi_{*}$:

```
(ψ′ ∘ ψ)_* = ψ′_* ∘ ψ_*.
```

Moreover, for every open $U \subset Y$, the direct image by the restriction $\psi|\psi^{-1}(U)$ of the induced presheaf
$\mathcal{F}|\psi^{-1}(U)$ is none other than the induced presheaf $\psi_{*}(\mathcal{F})|U$.

**(3.4.4)** Suppose $\mathit{K}$ admits inductive limits and let $\mathcal{F}$ be a presheaf on $X$ with values in
$\mathit{K}$. For each $x \in X$, the morphisms $\Gamma(\psi^{-1}(U), \mathcal{F}) \to \mathcal{F}_{x}$ ($U$ an open
neighborhood of $\psi(x)$ in $Y$) form an inductive system; passage to the limit gives a stalk morphism

$$ \psi_{x} : (\psi_{*}(\mathcal{F}))_{\psi(x)} \to \mathcal{F}_{x}. $$

In general, $\psi_{x}$ is _neither injective nor surjective_. It is functorial: for $u : \mathcal{F}_{1} \to
\mathcal{F}_{2}$, the diagram

```
(ψ_*(ℱ_1))_{ψ(x)} ──ψ_x──→ (ℱ_1)_x
        │                       │
(ψ_*(u))_{ψ(x)}                u_x
        │                       │
        ↓                       ↓
(ψ_*(ℱ_2))_{ψ(x)} ──ψ_x──→ (ℱ_2)_x
```

commutes. If $Z$ is a third topological space, $\psi' : Y \to Z$ continuous, and $\psi'' = \psi' \circ \psi$, then
$\psi''_{x} = \psi_{x} \circ \psi'_{\psi(x)}$ for $x \in X$.

**(3.4.5)** Under the hypotheses of (3.4.4), suppose further that $\psi$ is a _homeomorphism_ of $X$ onto the subspace
$\psi(X)$ of $Y$. Then for every $x \in X$, $\psi_{x}$ is an _isomorphism_. This applies in particular to the canonical
injection $j$ of a subspace $X \subset Y$ into $Y$.

**(3.4.6)** Suppose $\mathit{K}$ is the category of groups, of rings, etc. If $\mathcal{F}$ is a sheaf on $X$ with
support $S$, and $y \notin \psi\bar{S}$, then by the definition of $\psi_{*}(\mathcal{F})$ one has
$(\psi_{*}(\mathcal{F}))_{y} = {0}$; that is, $Supp(\psi_{*}(\mathcal{F})) \subset \psi\bar{S}$. The support is not,
however, necessarily contained in $\psi(S)$. Under the same hypotheses, if $j$ is the canonical injection of a subspace
$X \subset Y$, the sheaf $j_{*}(\mathcal{F})$ induces $\mathcal{F}$ on $X$; if moreover $X$ is _closed_ in $Y$, then
$j_{*}(\mathcal{F})$ is the sheaf on $Y$ inducing $\mathcal{F}$ on $X$ and `0` on $Y - X$ (G, II, 2.9.2); but the two
sheaves are in general distinct when $X$ is locally closed but not closed.

### 3.5. Inverse images of presheaves

<!-- label: 0.3.5 -->

**(3.5.1)** Under the hypotheses of (3.4.1), if $\mathcal{F}$ (resp. $\mathcal{G}$) is a presheaf on $X$ (resp. $Y$)
with values in $\mathit{K}$, every morphism $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$ of presheaves on $Y$ is called a
_ψ-morphism_ of $\mathcal{G}$ into $\mathcal{F}$, also written $\mathcal{G} \to \mathcal{F}$. We write
$\operatorname{Hom}_{\psi}(\mathcal{G}, \mathcal{F})$ for $\operatorname{Hom}_{Y}(\mathcal{G}, \psi_{*}(\mathcal{F}))$.
For every pair $(U, V)$ with $U$ open in $X$, $V$ open in $Y$, and $\psi(U) \subset V$, one has a morphism $u_{U,V} :
\mathcal{G}(V) \to \mathcal{F}(U)$ obtained by composing the restriction $\mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}(U)$
with $u_{V} : \mathcal{G}(V) \to \psi_{*}(\mathcal{F})(V) = \mathcal{F}(\psi^{-1}(V))$. These morphisms make the
diagrams

```
(3.5.1.1)    𝒢(V) ──u_{U,V}──→ ℱ(U)
               │                  │
               ↓                  ↓
             𝒢(V′) ──u_{U′,V′}──→ ℱ(U′)
```

(for $U' \subset U$, $V' \subset V$, $\psi(U') \subset V'$) commute. Conversely, a family $(u_{U,V})$ making (3.5.1.1)
commute defines a $\psi$-morphism $u$: take $u_{V} = u_{\psi^{-1}(V), V}$.

If $\mathit{K}$ admits (generalized) projective limits and $\mathfrak{B}$, $\mathfrak{B}'$ are bases for the topologies
of $X$ and $Y$, then to define a $\psi$-morphism of _sheaves_ it suffices to give $u_{U,V}$ for $U \in \mathfrak{B}$, $V
\in \mathfrak{B}'$, $\psi(U) \subset V$, satisfying (3.5.1.1) for $U, U' \in \mathfrak{B}$ and $V, V' \in
\mathfrak{B}'$; for an arbitrary open $W \subset Y$, define $u_{W}$ as the projective limit of the $u_{U,V}$ for $V \in
\mathfrak{B}'$, $V \subset W$, $U \in \mathfrak{B}$, $\psi(U) \subset V$.

When $\mathit{K}$ admits inductive limits, one obtains for each $x \in X$ a morphism $\mathcal{G}(V) \to
\mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}_{x}$ for every open neighborhood $V$ of $\psi(x)$ in $Y$; these form an
inductive system whose limit is a stalk morphism $\mathcal{G}_{\psi(x)} \to \mathcal{F}_{x}$.

**(3.5.2)** Under the hypotheses of (3.4.3), let $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ be presheaves on $X$, $Y$,
$Z$ with values in $\mathit{K}$, and let $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$, $v : \mathcal{H} \to
\psi'_{*}(\mathcal{G})$ be a $\psi$-morphism and a $\psi'$-morphism. One obtains a $\psi''$-morphism

```
w : ℋ ──v──→ ψ′_*(𝒢) ──ψ′_*(u)──→ ψ′_*(ψ_*(ℱ)) = ψ″_*(ℱ),
```

called by definition the _composite_ of $u$ and $v$. One may therefore regard pairs $(X, \mathcal{F})$ of a topological
space $X$ and a presheaf $\mathcal{F}$ on $X$ (with values in $\mathit{K}$) as forming a _category_, with morphisms the
pairs $(\psi, \theta) : (X, \mathcal{F}) \to (Y, \mathcal{G})$ consisting of a continuous map $\psi : X \to Y$ and a
$\psi$-morphism $\theta : \mathcal{G} \to \mathcal{F}$.

**(3.5.3)** Let $\psi : X \to Y$ be a continuous map and $\mathcal{G}$ a presheaf on $Y$ with values in $\mathit{K}$. We
call an _inverse image of_ $\mathcal{G}$ _by_ $\psi$ a pair $(\mathcal{G}', \rho)$ consisting of a _sheaf_
$\mathcal{G}'$ on $X$ with values in $\mathit{K}$ and a $\psi$-morphism $\rho : \mathcal{G} \to \mathcal{G}'$
(equivalently, a homomorphism $\mathcal{G} \to \psi_{*}(\mathcal{G}')$) such that, for every _sheaf_ $\mathcal{F}$ on
$X$ with values in $\mathit{K}$, the map

```
(3.5.3.1)    Hom_X(𝒢′, ℱ) → Hom_ψ(𝒢, ℱ) = Hom_Y(𝒢, ψ_*(ℱ))
```

sending $v$ to $\psi_{*}(v) \circ \rho$ is a _bijection_; this map being functorial in $\mathcal{F}$, it then defines an
isomorphism of functors in $\mathcal{F}$. As a solution of a universal problem, the pair $(\mathcal{G}', \rho)$, when it
exists, is _determined up to unique isomorphism_. We then write $\mathcal{G}' = \psi*(\mathcal{G})$, $\rho =
\rho_{\mathcal{G}}$, and by abuse of language we call $\psi*(\mathcal{G})$ the _inverse image sheaf of_ $\mathcal{G}$
_by_ $\psi$, with the understanding that $\psi*(\mathcal{G})$ is taken together with the canonical $\psi$-morphism
$\rho_{\mathcal{G}} : \mathcal{G} \to \psi_{*}(\psi*(\mathcal{G}))$, i.e. with the canonical homomorphism of presheaves
on $Y$

$$ (3.5.3.2) \rho_{\mathcal{G}} : \mathcal{G} \to \psi_{*}(\psi*(\mathcal{G})). $$

For any homomorphism $v : \psi*(\mathcal{G}) \to \mathcal{F}$ (where $\mathcal{F}$ is a sheaf on $X$ with values in
$\mathit{K}$), set $v^{\flat} = \psi_{*}(v) \circ \rho_{\mathcal{G}} : \mathcal{G} \to \psi_{*}(\mathcal{F})$. By
definition, _every_ morphism $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$ of presheaves is of the form $v^{\flat}$ for a
unique $v$, which we write $u^{\sharp}$. In other words, every such $u$ factors uniquely as

```
(3.5.3.3)    u : 𝒢 ──ρ_𝒢──→ ψ_*(ψ*(𝒢)) ──ψ_*(u^♯)──→ ψ_*(ℱ).
```

**(3.5.4)** Suppose now that the category $\mathit{K}$ is such[^3-6] that _every_ presheaf $\mathcal{G}$ on $Y$ with
values in $\mathit{K}$ admits an inverse image by $\psi$, denoted $\psi*(\mathcal{G})$.

We shall see that $\psi*(\mathcal{G})$ may be defined as a _covariant functor in_ $\mathcal{G}$, from presheaves on $Y$
to sheaves on $X$, in such a way that the isomorphism $v \mapsto v^{\flat}$ is an _isomorphism of bifunctors_

```
(3.5.4.1)    Hom_X(ψ*(𝒢), ℱ) ⥲ Hom_Y(𝒢, ψ_*(ℱ))
```

in $\mathcal{G}$ and $\mathcal{F}$.

Indeed, for every morphism $w : \mathcal{G}_{1} \to \mathcal{G}_{2}$ of presheaves on $Y$, consider the composite
$\mathcal{G}_{1} \xrightarrow{w} \mathcal{G}_{2} \xrightarrow{\rho_{\mathcal{G}_{2}}} \psi_{*}(\psi*(\mathcal{G}_{2}))$;
to it corresponds a morphism $(\rho_{\mathcal{G}_{2}} \circ w)^{\sharp} : \psi*(\mathcal{G}_{1}) \to
\psi*(\mathcal{G}_{2})$, which we write $\psi*(w)$. By (3.5.3.3),

```
(3.5.4.2)    ψ_*(ψ*(w)) ∘ ρ_{𝒢_1} = ρ_{𝒢_2} ∘ w.
```

For every morphism $u : \mathcal{G}_{2} \to \psi_{*}(\mathcal{F})$ (with $\mathcal{F}$ a sheaf on $X$ with values in
$\mathit{K}$), by (3.5.3.3), (3.5.4.2), and the definition of $u^{\flat}$,

```
(u^♯ ∘ ψ*(w))^♭ = ψ_*(u^♯) ∘ ψ_*(ψ*(w)) ∘ ρ_{𝒢_1} = ψ_*(u^♯) ∘ ρ_{𝒢_2} ∘ w = u ∘ w,
```

that is,

```
(3.5.4.3)    (u ∘ w)^♯ = u^♯ ∘ ψ*(w).
```

Taking in particular $u = \rho_{\mathcal{G}_{3}} \circ w'$ for a morphism $w' : \mathcal{G}_{2} \to \mathcal{G}_{3}$,
one gets $\psi*(w' \circ w) = (\rho_{\mathcal{G}_{3}} \circ w' \circ w)^{\sharp} = (\rho_{\mathcal{G}_{3}} \circ
w')^{\sharp} \circ \psi*(w) = \psi*(w') \circ \psi*(w)$, proving functoriality.

Finally, for a sheaf $\mathcal{F}$ on $X$ with values in $\mathit{K}$, let $i_{\mathcal{F}}$ be the identity of
$\psi_{*}(\mathcal{F})$ and set

```
σ_ℱ = (i_ℱ)^♯ : ψ*(ψ_*(ℱ)) → ℱ;
```

(3.5.4.3) then gives the factorization

```
(3.5.4.4)    u^♯ : ψ*(𝒢) ──ψ*(u)──→ ψ*(ψ_*(ℱ)) ──σ_ℱ──→ ℱ
```

for every morphism $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$. We call $\sigma_{\mathcal{F}}$ the _canonical morphism_.

**(3.5.5)** Let $\psi' : Y \to Z$ be continuous and suppose every presheaf $\mathcal{H}$ on $Z$ with values in
$\mathit{K}$ admits an inverse image $\psi'*(\mathcal{H})$. Then (under the hypotheses of (3.5.4)) every presheaf
$\mathcal{H}$ on $Z$ admits an inverse image by $\psi'' = \psi' \circ \psi$, and there is a canonical functorial
isomorphism

$$ (3.5.5.1) \psi''*(\mathcal{H}) \xrightarrow{\sim} \psi*(\psi'*(\mathcal{H})). $$

This follows at once from the definitions, given that $\psi''_{*} = \psi'_{*} \circ \psi_{*}$. Moreover, if $u :
\mathcal{G} \to \psi_{*}(\mathcal{F})$ is a $\psi$-morphism, $v : \mathcal{H} \to \psi'_{*}(\mathcal{G})$ a
$\psi'$-morphism, and $w = \psi'_{*}(u) \circ v$ their composite (3.5.2), one checks at once that $w^{\sharp}$ is the
composite

```
w^♯ : ψ*(ψ′*(ℋ)) ──ψ*(v^♯)──→ ψ*(𝒢) ──u^♯──→ ℱ.
```

**(3.5.6)** Take in particular $\psi = 1_{X} : X \to X$. If an inverse image by $\psi$ of a presheaf $\mathcal{F}$ on
$X$ exists, this inverse image is called the _sheaf associated with the presheaf_ $\mathcal{F}$. Every morphism $u :
\mathcal{F} \to \mathcal{F}'$ from $\mathcal{F}$ to a sheaf $\mathcal{F}'$ with values in $\mathit{K}$ factors uniquely
as

```
ℱ ──ρ_ℱ──→ 1_X*(ℱ) ──u^♯──→ ℱ′.
```

### 3.6. Simple and locally simple sheaves

<!-- label: 0.3.6 -->

**(3.6.1)** A presheaf $\mathcal{F}$ on $X$ with values in $\mathit{K}$ is called _constant_ if the canonical morphisms
$\mathcal{F}(X) \to \mathcal{F}(U)$ are _isomorphisms_ for every nonempty open $U \subset X$; note that $\mathcal{F}$ is
not necessarily a sheaf. A _sheaf_ $\mathcal{F}$ is called _simple_ if it is associated (3.5.6) with a constant
presheaf. A sheaf $\mathcal{F}$ is called _locally simple_ if every $x \in X$ admits an open neighborhood $U$ such that
$\mathcal{F}|U$ is simple.

**(3.6.2)** Suppose $X$ is _irreducible_ (2.1.1). The following are equivalent:

> a) $\mathcal{F}$ is a constant presheaf on $X$; b) $\mathcal{F}$ is a simple sheaf on $X$; c) $\mathcal{F}$ is a
> locally simple sheaf on $X$.

Indeed, let $\mathcal{F}$ be a constant presheaf on $X$. If `U, V` are nonempty open subsets, then $U \cap V$ is
nonempty; so $\mathcal{F}(X) \to \mathcal{F}(U) \to \mathcal{F}(U \cap V)$ and $\mathcal{F}(X) \to \mathcal{F}(V) \to
\mathcal{F}(U \cap V)$ are isomorphisms, whence so are $\mathcal{F}(U) \to \mathcal{F}(U \cap V)$ and $\mathcal{F}(V)
\to \mathcal{F}(U \cap V)$. One concludes at once that axiom (F) of (3.1.2) holds, so $\mathcal{F}$ is isomorphic to its
associated sheaf, proving _a) ⇒ b)_.

Now let $(U_{\alpha})$ be an open cover of $X$ by nonempty open sets and $\mathcal{F}$ a sheaf on $X$ with
$\mathcal{F}|U_{\alpha}$ simple for every $\alpha$. Since $U_{\alpha}$ is irreducible, $\mathcal{F}|U_{\alpha}$ is a
constant presheaf by the above. Since $U_{\alpha} \cap U_{\beta} \neq \emptyset$, both $\mathcal{F}(U_{\alpha}) \to
\mathcal{F}(U_{\alpha} \cap U_{\beta})$ and $\mathcal{F}(U_{\beta}) \to \mathcal{F}(U_{\alpha} \cap U_{\beta})$ are
isomorphisms, giving a canonical isomorphism $\theta_{\alpha \beta} : \mathcal{F}(U_{\alpha}) \to
\mathcal{F}(U_{\beta})$ for every pair. Applying (F) with $U = X$, one sees that for every index $\alpha_{0}$, the pair
$(\mathcal{F}(U_{\alpha_{0}}), (\theta_{\alpha \alpha_{0}}))$ is a solution of the universal problem; by uniqueness,
$\mathcal{F}(X) \to \mathcal{F}(U_{\alpha})$ is an isomorphism, proving _c) ⇒ a)_.

### 3.7. Inverse images of presheaves of groups or rings

<!-- label: 0.3.7 -->

**(3.7.1)** We show that when $\mathit{K}$ is the category of sets, the inverse image by $\psi$ of every presheaf
$\mathcal{G}$ always exists (notation and hypotheses on $X$, $Y$, $\psi$ as in (3.5.3)). For each open $U \subset X$,
define $\mathcal{G}'(U)$ as follows: an element $s'$ of $\mathcal{G}'(U)$ is a family $(s'_{z})_{z \in U}$ with $s'_{z}
\in \mathcal{G}_{\psi(z)}$ such that for every $x \in U$, the following holds: there is an open neighborhood $V$ of
$\psi(x)$ in $Y$, a neighborhood $W \subset \psi^{-1}(V) \cap U$ of $x$, and an element $s \in \mathcal{G}(V)$ with
$s'_{z} = s_{\psi(z)}$ for $z \in W$. One checks at once that $U \mapsto \mathcal{G}'(U)$ is a _sheaf_.

Now let $\mathcal{F}$ be a sheaf of sets on $X$, and let $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$, $v : \mathcal{G}'
\to \mathcal{F}$ be morphisms. Define $u^{\sharp}$ and $v^{\flat}$ as follows: if $s'$ is a section of $\mathcal{G}'$
over a neighborhood $U$ of $x \in X$ and $V$ is an open neighborhood of $\psi(x)$ with $s'_{z} = s_{\psi(z)}$ for $z$ in
a neighborhood of $x$ contained in $\psi^{-1}(V) \cap U$, set $u^{\sharp}_{x}(s'_{x}) = u_{\psi(x)}(s_{\psi(x)})$. If $s
\in \mathcal{G}(V)$ for $V$ open in $Y$, let $v^{\flat}(s)$ be the section of $\mathcal{F}$ over $\psi^{-1}(V)$, image
under $v$ of the section $s'$ of $\mathcal{G}'$ with $s'_{z} = s_{\psi(z)}$ for $z \in \psi^{-1}(V)$. The canonical
homomorphism (3.5.3) $\rho : \mathcal{G} \to \psi_{*}(\psi*(\mathcal{G}))$ is defined by: for $V \subset Y$ open and $s
\in \Gamma(V, \mathcal{G})$, $\rho(s)$ is the section $(s_{\psi(z)})_{z \in \psi^{-1}(V)}$ of $\psi*(\mathcal{G})$ over
$\psi^{-1}(V)$. The relations $(u^{\flat})^{\sharp} = u$, $(v^{\sharp})^{\flat} = v$, and $v^{\flat} = \psi_{*}(v) \circ
\rho$ are immediate.

One checks that if $w : \mathcal{G}_{1} \to \mathcal{G}_{2}$ is a morphism of presheaves of sets on $Y$, then $\psi*(w)$
is given explicitly by: if $s' = (s'_{z})_{z \in U}$ is a section of $\psi*(\mathcal{G}_{1})$ over an open $U \subset
X$, then $(\psi*(w))(s') = (w_{\psi(z)}(s'_{z}))_{z \in U}$. For every open $V \subset Y$, the inverse image of
$\mathcal{G}|V$ by $\psi|\psi^{-1}(V)$ is identical with $\psi*(\mathcal{G})|\psi^{-1}(V)$.

When $\psi = 1_{X}$ is the identity, the construction of $\mathcal{G}'$ recovers the usual sheaf of sets associated with
a presheaf (G, II, 1.2). The above goes through unchanged when $\mathit{K}$ is the category of groups or rings (not
necessarily commutative).

When $X$ is an arbitrary subspace of a topological space $Y$ and $j : X \to Y$ is the canonical injection, the _inverse
image_ $j*(\mathcal{G})$, when it exists, is called the sheaf _induced on_ $X$ _by_ $\mathcal{G}$; for sheaves of sets
(or groups, or rings) this recovers the usual definition (G, II, 1.5).

**(3.7.2)** Keeping the notation and hypotheses of (3.5.3), suppose $\mathcal{G}$ is a _sheaf_ of groups (resp. rings)
on $Y$. The construction of sections of $\psi*(\mathcal{G})$ (3.7.1) shows, in view of (3.4.4), that the stalk
homomorphism $\psi_{x} \circ \rho_{\psi(x)} : \mathcal{G}_{\psi(x)} \to (\psi*(\mathcal{G}))_{x}$ is a _functorial
isomorphism in_ $\mathcal{G}$, which allows one to identify these two stalks. Under this identification,
$u^{\sharp}_{x}$ is identical with the homomorphism defined in (3.5.1), and in particular

$$ Supp(\psi*(\mathcal{G})) = \psi^{-1}(Supp(\mathcal{G})). $$

An immediate consequence is that _the functor_ $\psi*(\mathcal{G})$ _is exact in_ $\mathcal{G}$ in the abelian category
of sheaves of abelian groups.

### 3.8. Sheaves of pseudo-discrete spaces

<!-- label: 0.3.8 -->

**(3.8.1)** Let $X$ be a topological space whose topology admits a basis $\mathfrak{B}$ of _quasi-compact_ open sets.
Let $\mathcal{F}$ be a sheaf of sets on $X$. Endowing each $\mathcal{F}(U)$ with the _discrete_ topology makes $U
\mapsto \mathcal{F}(U)$ a _presheaf of topological spaces_. We shall see that there exists a _sheaf of topological
spaces_ $\mathcal{F}'$ associated with $\mathcal{F}$ (3.5.6) such that $\Gamma(U, \mathcal{F}')$ is the discrete space
$\mathcal{F}(U)$ for every _quasi-compact_ open $U$. For this, it suffices to show that the presheaf $U \mapsto
\mathcal{F}(U)$ of topological spaces _on_ $\mathfrak{B}$ satisfies (F₀) of (3.2.2), and more generally that if $U$ is a
quasi-compact open set and $(U_{\alpha})$ is a cover of $U$ by elements of $\mathfrak{B}$, then the coarsest topology
$\mathcal{T}$ on $\Gamma(U, \mathcal{F})$ making the maps $\Gamma(U, \mathcal{F}) \to \Gamma(U_{\alpha}, \mathcal{F})$
continuous is the _discrete_ topology. There is a finite set of indices $\alpha_{i}$ with $U = \bigcup_{i}
U_{\alpha_{i}}$. Let $s \in \Gamma(U, \mathcal{F})$ and let $s_{i}$ be its image in $\Gamma(U_{\alpha_{i}},
\mathcal{F})$; the intersection of the inverse images of ${s_{i}}$ is by definition a $\mathcal{T}$-neighborhood of $s$.
But since $\mathcal{F}$ is a sheaf of sets and the $U_{\alpha_{i}}$ cover $U$, this intersection reduces to ${s}$,
whence the assertion.

Note that if $U$ is a non-quasi-compact open subset of $X$, the topological space $\Gamma(U, \mathcal{F}')$ still has
$\Gamma(U, \mathcal{F})$ as underlying set, but its topology is in general not discrete: it is the coarsest making the
maps $\Gamma(U, \mathcal{F}) \to \Gamma(V, \mathcal{F})$ continuous, for $V \in \mathfrak{B}$, $V \subset U$ (the
$\Gamma(V, \mathcal{F})$ being discrete).

The above applies without change to sheaves of groups or rings (not necessarily commutative), associating with them
sheaves of _topological groups_ or _topological rings_ respectively. For brevity, we say that $\mathcal{F}'$ is the
_sheaf of pseudo-discrete spaces_ (resp. groups, rings) _associated_ with the sheaf of sets (resp. groups, rings)
$\mathcal{F}$.

**(3.8.2)** Let $\mathcal{F}$, $\mathcal{G}$ be sheaves of sets (resp. groups, rings) on $X$ and $u : \mathcal{F} \to
\mathcal{G}$ a homomorphism. Then $u$ is also a _continuous_ homomorphism $\mathcal{F}' \to \mathcal{G}'$, where
$\mathcal{F}'$, $\mathcal{G}'$ are the associated pseudo-discrete sheaves; this follows from (3.2.5).

**(3.8.3)** Let $\mathcal{F}$ be a sheaf of sets, $\mathcal{H}$ a subsheaf of $\mathcal{F}$, and $\mathcal{F}'$,
$\mathcal{H}'$ the associated pseudo-discrete sheaves. For every open $U \subset X$, $\Gamma(U, \mathcal{H}')$ is
_closed_ in $\Gamma(U, \mathcal{F}')$: indeed, it is the intersection of the inverse images of $\Gamma(V, \mathcal{H})$
(for $V \in \mathfrak{B}$, $V \subset U$) under the continuous maps $\Gamma(U, \mathcal{F}) \to \Gamma(V, \mathcal{F})$,
and $\Gamma(V, \mathcal{H})$ is closed in the discrete space $\Gamma(V, \mathcal{F})$.

[^3-1]: This is a special case of the general notion of (non-filtered) _projective limit_; see (T, I, 1.8) and the book
    in preparation announced in the Introduction.

[^3-2]: One can prove that this also means that the canonical functor $\mathit{K} \to (Ens)$ commutes with projective
    limits (not necessarily filtered).

[^3-3]: This is because in the category $\mathit{K}$, every morphism that is a _bijection_ (as a map of sets) is an
    _isomorphism_. This is no longer true when $\mathit{K}$ is, for example, the category of topological spaces.

[^3-4]: If $X$ is a _Noetherian_ space, one can still define $\mathcal{F}'(U)$ and show that it is a presheaf in the
    ordinary sense, assuming only that $\mathit{K}$ admits projective limits for _finite_ projective systems. Indeed,
    for any open $U$, there is a finite cover $(V_{i})$ of $U$ by elements of $\mathfrak{B}$; for each pair $(i, j)$,
    choose a finite cover $(V_{ijk})$ of $V_{i} \cap V_{j}$ by elements of $\mathfrak{B}$. Let $I$ be the set of indices
    $i$ and triples $(i, j, k)$, ordered by the relations $i > (i, j, k)$ and $j > (i, j, k)$; take $\mathcal{F}'(U)$ to
    be the projective limit of the system of the $\mathcal{F}(V_{i})$ and $\mathcal{F}(V_{ijk})$. One checks easily that
    this is independent of the covers and that $U \mapsto \mathcal{F}'(U)$ is a presheaf.

[^3-5]: This also means that the pair $(\mathcal{F}(U), (\rho_{\alpha}))$ with $\rho_{\alpha} = \rho^{U}_{U_{\alpha}}$
    is a solution of the universal problem (3.1.1) defined by $A_{\alpha} = \mathcal{F}(U_{\alpha})$, $A_{\alpha \beta}
    = \prod \mathcal{F}(V)$ (for $V \in \mathfrak{B}$ with $V \subset U_{\alpha} \cap U_{\beta}$), and $\rho_{\alpha
    \beta} = (\rho^{V}_{U_{\alpha}}) : \mathcal{F}(U_{\alpha}) \to \prod \mathcal{F}(V)$ defined by: for $V, V', W \in
    \mathfrak{B}$ with $V \cup V' \subset U_{\alpha} \cap U_{\beta}$, $W \subset V \cap V'$, $\rho^{V}_{W} \circ
    \rho^{U_{\alpha}}_{V} = \rho^{V'}_{W} \circ \rho^{U_{\alpha}}_{V'}$.

[^3-6]: In the book cited in the Introduction, we shall give very general conditions on $\mathit{K}$ ensuring the
    existence of inverse images of presheaves with values in $\mathit{K}$.
