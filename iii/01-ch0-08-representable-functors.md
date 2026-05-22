# Chapter 0_III (suite)

# Preliminaries

## §8. Representable functors

<!-- original page 5 -->

### 8.1. Representable functors.

**8.1.1.**

<!-- label: 0_III.8.1.1 -->

We denote by `Set` the category of sets. Let $\mathcal{C}$ be a category; for two objects $X$, $Y$ of $\mathcal{C}$, we
set $h_{X}(Y) = \operatorname{Hom}(Y, X)$; for every morphism $u : Y \to Y'$ in $\mathcal{C}$, we denote by $h_{X}(u)$
the map $v \mapsto v \circ u$ from $\operatorname{Hom}(Y', X)$ into $\operatorname{Hom}(Y, X)$. It is immediate that
with these definitions $h_{X} : \mathcal{C} \to Set$ is a *contravariant functor*, that is, an object of the category,
denoted $\operatorname{Hom}(\mathcal{C}^{\circ}, Set)$, of covariant functors from the category $\mathcal{C}^{\circ}$
dual to $\mathcal{C}$ into the category `Set` `(T, 1.7, d)` and `[29]`.

> _Translator's note._ We render EGA's `Ens` as `Set` throughout, the standard modern English form. The 1961 original
> capitalizes the category as **Ens**; the typographical species ("category in bold") is rendered here by the upright
> ASCII string `Set` inside backticks.

**8.1.2.**

<!-- label: 0_III.8.1.2 -->

Now let $w : X \to X'$ be a morphism in $\mathcal{C}$; for every $Y \in \mathcal{C}$ and every $v \in
\operatorname{Hom}(Y, X) = h_{X}(Y)$, we have $w \circ v \in \operatorname{Hom}(Y, X') = h_{X'}(Y)$; we denote by
$h_{w}(Y)$ the map $v \mapsto w \circ v$ from $h_{X}(Y)$ into $h_{X'}(Y)$. It is immediate that for every morphism $u :
Y \to Y'$ in $\mathcal{C}$, the diagram

```text
              h_X(u)
   h_X(Y') ────────→ h_X(Y)

   h_w(Y')│           │h_w(Y)
          ↓           ↓

   h_{X'}(Y') ───────→ h_{X'}(Y)
                h_{X'}(u)
```

is commutative; in other words, $h_{w}$ is a *functorial morphism* $h_{X} \to h_{X'}$ `(T, 1.2)`, or again a morphism in
the category $\operatorname{Hom}(\mathcal{C}^{\circ}, Set)$ `(T, 1.7, d)`. The definitions of $h_{X}$ and $h_{w}$
therefore constitute the definition of a *canonical covariant functor*

```text
  h : 𝒞 → Hom(𝒞°, Set).                                                    (8.1.2.1)
```

**8.1.3.**

<!-- label: 0_III.8.1.3 -->

Let $X$ be an object of $\mathcal{C}$, $F$ a contravariant functor from $\mathcal{C}$ into `Set` (an object of
$\operatorname{Hom}(\mathcal{C}^{\circ}, Set)$). Let $g : h_{X} \to F$ be a functorial morphism: for every $Y \in
\mathcal{C}$,

<!-- original page 6 -->

$g(Y)$ is a map $h_{X}(Y) \to F(Y)$ such that for every morphism $u : Y \to Y'$ in $\mathcal{C}$, the diagram

```text
              h_X(u)
   h_X(Y') ────────→ h_X(Y)

   g(Y')  │           │ g(Y)                                              (8.1.3.1)
          ↓           ↓

   F(Y') ────────────→ F(Y)
                F(u)
```

is commutative. In particular, we have a map $g(X) : h_{X}(X) = \operatorname{Hom}(X, X) \to F(X)$, whence an element

$$ \alpha(g) = (g(X))(1_{X}) \in F(X) (8.1.3.2) $$

and consequently a canonical map

```text
  α : Hom(h_X, F) → F(X).                                                  (8.1.3.3)
```

Conversely, consider an element $\xi \in F(X)$; for every morphism $v : Y \to X$ in $\mathcal{C}$, $F(v)$ is a map $F(X)
\to F(Y)$; consider the map

$$ v \mapsto (F(v))(\xi) (8.1.3.4) $$

from $h_{X}(Y)$ into $F(Y)$; if we denote this map by $(\beta(\xi))(Y)$,

$$ \beta(\xi) : h_{X} \to F (8.1.3.5) $$

is a functorial morphism, for we have, for every morphism $u : Y \to Y'$ in $\mathcal{C}$, $(F(v \circ u))(\xi) = (F(u)
\circ F(v))(\xi)$, which verifies the commutativity of `(8.1.3.1)` for $g = \beta(\xi)$. We have thus defined a
canonical map

```text
  β : F(X) → Hom(h_X, F).                                                  (8.1.3.6)
```

**Proposition (8.1.4).**

<!-- label: 0_III.8.1.4 -->

*The maps $\alpha$ and $\beta$ are mutually inverse bijections.*

**Proof.** Let us compute $\alpha(\beta(\xi))$ for $\xi \in F(X)$; for every $Y \in \mathcal{C}$, $(\beta(\xi))(Y)$ is
the map $g_{1}(Y) : v \mapsto (F(v))(\xi)$ from $h_{X}(Y)$ into $F(Y)$. We therefore have

```text
  α(β(ξ)) = (g_1(X))(1_X) = (F(1_X))(ξ) = 1_{F(X)}(ξ) = ξ.
```

Let us now compute $\beta(\alpha(g))$ for $g \in \operatorname{Hom}(h_{X}, F)$; for every $Y \in \mathcal{C}$,
$(\beta(\alpha(g)))(Y)$ is the map $v \mapsto (F(v))((g(X))(1_{X}))$; by the commutativity of `(8.1.3.1)`, this map is
none other than $v \mapsto (g(Y))((h_{X}(v))(1_{X})) = (g(Y))(v)$ by the definition of $h_{X}(v)$; in other words, it is
equal to $g(Y)$, which proves the proposition.

**8.1.5.**

<!-- label: 0_III.8.1.5 -->

Recall that a *subcategory* $\mathcal{C}'$ of a category $\mathcal{C}$ is defined by the condition that its objects be
objects of $\mathcal{C}$, and that if $X'$, $Y'$ are two objects of $\mathcal{C}'$, the set
$\operatorname{Hom}_{\mathcal{C}'}(X', Y')$ of morphisms $X' \to Y'$ in $\mathcal{C}'$ is a subset of the set
$\operatorname{Hom}_{\mathcal{C}}(X', Y')$ of morphisms $X' \to Y'$ in $\mathcal{C}$, the canonical map of "composition
of morphisms"

```text
  Hom_{𝒞'}(X', Y') × Hom_{𝒞'}(Y', Z') → Hom_{𝒞'}(X', Z')
```

<!-- original page 7 -->

being the restriction of the canonical map

```text
  Hom_𝒞(X', Y') × Hom_𝒞(Y', Z') → Hom_𝒞(X', Z').
```

We say that $\mathcal{C}'$ is a *full* subcategory of $\mathcal{C}$ if $\operatorname{Hom}_{\mathcal{C}'}(X', Y') =
\operatorname{Hom}_{\mathcal{C}}(X', Y')$ for every pair of objects of $\mathcal{C}'$. The subcategory $\mathcal{C}''$
of $\mathcal{C}$ formed by the objects of $\mathcal{C}$ isomorphic to objects of $\mathcal{C}'$ is then also a full
subcategory of $\mathcal{C}$, *equivalent* `(T, 1.2)` to $\mathcal{C}'$, as one verifies without difficulty.

A covariant functor $F : \mathcal{C}_{1} \to \mathcal{C}_{2}$ is said to be *fully faithful* if, for every pair of
objects `X_1`, `Y_1` of $\mathcal{C}_{1}$, the map $u \mapsto F(u)$ from $\operatorname{Hom}(X_{1}, Y_{1})$ into
$\operatorname{Hom}(F(X_{1}), F(Y_{1}))$ is bijective; this entails that the subcategory $F(\mathcal{C}_{1})$ of
$\mathcal{C}_{2}$ is full. Moreover, if two objects `X_1`, $X'_{1}$ have the same image `X_2`, there exists a unique
isomorphism $u : X_{1} \to X'_{1}$ such that $F(u) = 1_{X_{2}}$. For each object `X_2` of $F(\mathcal{C}_{1})$, let
$G(X_{2})$ be one of the objects `X_1` of $\mathcal{C}_{1}$ such that $F(X_{1}) = X_{2}$ ($G$ being defined by means of
the axiom of choice); for every morphism $v : X_{2} \to Y_{2}$ in $F(\mathcal{C}_{1})$, $G(v)$ will be the unique
morphism $u : G(X_{2}) \to G(Y_{2})$ such that $F(u) = v$; $G$ is then a functor from $F(\mathcal{C}_{1})$ into
$\mathcal{C}_{1}$; $F \circ G$ is the identity functor on $F(\mathcal{C}_{1})$, and what precedes shows that there
exists an isomorphism of functors $\phi : 1_{\mathcal{C}_{1}} \to G \circ F$ such that $F$, $G$, $\phi$ and the identity
$1_{F(\mathcal{C}_{1})} \to F \circ G$ define an *equivalence* of the category $\mathcal{C}_{1}$ with the full
subcategory $F(\mathcal{C}_{1})$ of $\mathcal{C}_{2}$ `(T, 1.2)`.

**8.1.6.**

<!-- label: 0_III.8.1.6 -->

Apply Proposition `(8.1.4)` to the case where the functor $F$ is $h_{X'}$, $X'$ being an arbitrary object of
$\mathcal{C}$; the map $\beta : \operatorname{Hom}(X, X') \to \operatorname{Hom}(h_{X}, h_{X'})$ is here none other than
the map $w \mapsto h_{w}$ defined in `(8.1.2)`; this map being bijective, we see, with the terminology of `(8.1.5)`,
that:

**Proposition (8.1.7).**

<!-- label: 0_III.8.1.7 -->

*The canonical functor $h : \mathcal{C} \to \operatorname{Hom}(\mathcal{C}^{\circ}, Set)$ is fully faithful.*

**8.1.8.**

<!-- label: 0_III.8.1.8 -->

Let $F$ be a contravariant functor from $\mathcal{C}$ into `Set`; we say that $F$ is *representable* if there exists an
object $X \in \mathcal{C}$ such that $F$ is isomorphic to $h_{X}$; it follows from `(8.1.7)` that the data of an $X \in
\mathcal{C}$ and an isomorphism of functors $g : h_{X} \to F$ determines $X$ up to unique isomorphism. Proposition
`(8.1.7)` also means that $h$ defines an *equivalence* of $\mathcal{C}$ with the full subcategory of
$\operatorname{Hom}(\mathcal{C}^{\circ}, Set)$ formed by the representable contravariant functors. It moreover follows
from `(8.1.4)` that the data of a functorial morphism $g : h_{X} \to F$ is equivalent to that of an element $\xi \in
F(X)$; to say that $g$ is an isomorphism is equivalent, for $\xi$, to the following condition: *for every object $Y$ of
$\mathcal{C}$ the map $v \mapsto (F(v))(\xi)$ from $\operatorname{Hom}(Y, X)$ into $F(Y)$ is bijective*. When $\xi$
satisfies this condition, we shall say that the pair $(X, \xi)$ *represents* the representable functor $F$. By abuse of
language, we shall also say that the object $X \in \mathcal{C}$ represents $F$ if there exists $\xi \in F(X)$ such that
$(X, \xi)$ represents $F$, in other words if $h_{X}$ is isomorphic to $F$.

Let $F$, $F'$ be two representable contravariant functors from $\mathcal{C}$ into `Set`, $h_{X} \to F$ and $h_{X'} \to
F'$ two isomorphisms of functors. Then it follows from `(8.1.6)` that there is a canonical one-to-one correspondence
between $\operatorname{Hom}(X, X')$ and the set $\operatorname{Hom}(F, F')$ of functorial morphisms $F \to F'$.

**8.1.9.** *Examples. I: projective limits.*

<!-- label: 0_III.8.1.9 -->

The notion of representable contravariant functor covers in particular the "dual" notion of the usual notion of
"solution of a

<!-- original page 8 -->

universal problem". More generally, we shall see that the notion of *projective limit* is a particular case of that of
representable functor. Recall that in a category $\mathcal{C}$, one defines a *projective system* by the data of a
preordered set $I$, a family $(A_{\alpha})_{\alpha \in I}$ of objects of $\mathcal{C}$, and, for every pair of indices
$(\alpha, \beta)$ such that $\alpha \leq \beta$, a morphism $u_{\alpha \beta} : A_{\beta} \to A_{\alpha}$. A *projective
limit* of this system in $\mathcal{C}$ consists of an object $B$ of $\mathcal{C}$ (denoted $\lim A_{\alpha}$), and, for
each $\alpha \in I$, a morphism $u_{\alpha} : B \to A_{\alpha}$, such that: 1° $u_{\alpha} = u_{\alpha \beta} \circ
u_{\beta}$ for $\alpha \leq \beta$; 2° For every object $X$ of $\mathcal{C}$ and every family $(v_{\alpha})_{\alpha \in
I}$ of morphisms $v_{\alpha} : X \to A_{\alpha}$ such that $v_{\alpha} = u_{\alpha \beta} \circ v_{\beta}$ for $\alpha
\leq \beta$, there exists a unique morphism $v : X \to B$ (denoted $\lim v_{\alpha}$) such that $v_{\alpha} = u_{\alpha}
\circ v$ for every $\alpha \in I$ `(T, 1.8)`. This is interpreted as follows: the $u_{\alpha \beta}$ canonically define
maps

```text
  ū_{αβ} : Hom(X, A_β) → Hom(X, A_α)
```

which define a projective system of sets $(\operatorname{Hom}(X, A_{\alpha}), \bar{u}_{\alpha \beta})$, and
$(v_{\alpha})$ is by definition an element of the set $\lim \operatorname{Hom}(X, A_{\alpha})$; it is clear that $X
\mapsto \lim \operatorname{Hom}(X, A_{\alpha})$ is a contravariant functor from $\mathcal{C}$ into `Set`, and the
existence of the projective limit $B$ is equivalent to saying that $(v_{\alpha}) \mapsto \lim v_{\alpha}$ is an
isomorphism of functors in $X$

```text
  lim Hom(X, A_α) ⥲ Hom(X, B)                                              (8.1.9.1)
```

in other words that the functor $X \mapsto \lim \operatorname{Hom}(X, A_{\alpha})$ is *representable*.

**8.1.10.** *Examples. II: final object.*

<!-- label: 0_III.8.1.10 -->

Let $\mathcal{C}$ be a category, ${a}$ a set reduced to a single element. Consider the contravariant functor $F :
\mathcal{C} \to Set$ which assigns to every object $X$ of $\mathcal{C}$ the set ${a}$, and to every morphism $X \to X'$
in $\mathcal{C}$ the unique map ${a} \to {a}$. To say that this functor is representable means that there exists an
object $e \in \mathcal{C}$ such that for every $Y \in \mathcal{C}$, $\operatorname{Hom}(Y, e) = h_{e}(Y)$ is reduced to
one element; we say that $e$ is a *final object* of $\mathcal{C}$, and it is clear that two final objects of
$\mathcal{C}$ are isomorphic (which allows us to define, in general by means of the axiom of choice, a final object of
$\mathcal{C}$, then denoted $e_{\mathcal{C}}$). For example, in the category `Set`, the final objects are the sets
reduced to one element; in the category of augmented algebras over a field $K$ (where the morphisms are the algebra
homomorphisms compatible with the augmentations), $K$ is a final object; in the category of $S$-preschemes `(I, 2.5.1)`,
$S$ is a final object.

**8.1.11.**

<!-- label: 0_III.8.1.11 -->

For two objects $X$, $Y$ of a category $\mathcal{C}$, set $h'_{X}(Y) = \operatorname{Hom}(X, Y)$, and for every morphism
$u : Y \to Y'$, let $h'_{X}(u)$ be the map $v \mapsto u \circ v$ from $\operatorname{Hom}(X, Y)$ into
$\operatorname{Hom}(X, Y')$; $h'_{X}$ is then a *covariant functor* $\mathcal{C} \to Set$, from which one deduces, as in
`(8.1.2)`, the definition of a canonical covariant functor $h' : \mathcal{C}^{\circ} \to \operatorname{Hom}(\mathcal{C},
Set)$; a covariant functor $F$ from $\mathcal{C}$ into `Set`, that is, an object of $\operatorname{Hom}(\mathcal{C},
Set)$, is then said to be *representable* if there exists an object $X \in \mathcal{C}$ (necessarily unique up to unique
isomorphism) such that $F$ is isomorphic to $h'_{X}$; we leave to the reader the task of developing the "dual"
considerations of the preceding ones for this notion, which this time covers that of *inductive limit*, and in
particular the usual notion of "solution of a universal problem".

<!-- original page 9 -->

### 8.2. Algebraic structures in categories.

**8.2.1.**

<!-- label: 0_III.8.2.1 -->

Given two contravariant functors $F$, $F'$ from $\mathcal{C}$ into `Set`, recall that for every object $Y \in
\mathcal{C}$, we set $(F \times F')(Y) = F(Y) \times F'(Y)$, and for every morphism $u : Y \to Y'$ in $\mathcal{C}$, we
set $(F \times F')(u) = F(u) \times F'(u)$, which is the map $(t, t') \mapsto ((F(u))(t), (F'(u))(t'))$ from $F(Y')
\times F'(Y')$ into $F(Y) \times F'(Y)$; $F \times F' : \mathcal{C} \to Set$ is therefore a contravariant functor (which
is moreover none other than the *product* of the objects $F$, $F'$ in the category
$\operatorname{Hom}(\mathcal{C}^{\circ}, Set)$). Given an object $X \in \mathcal{C}$, we shall call an *internal
composition law* on $X$ a functorial morphism

```text
  γ_X : h_X × h_X → h_X.                                                   (8.2.1.1)
```

In other words `(T, 1.2)`, for every object $Y \in \mathcal{C}$, $\gamma_{X}(Y)$ is a map $h_{X}(Y) \times h_{X}(Y) \to
h_{X}(Y)$ (so by definition an internal composition law on the set $h_{X}(Y)$) subject to the condition that, for every
morphism $u : Y \to Y'$ in $\mathcal{C}$, the diagram

```text
                    h_X(u) × h_X(u)
   h_X(Y') × h_X(Y') ──────────────→ h_X(Y) × h_X(Y)

   γ_X(Y')         │                          │ γ_X(Y)
                   ↓                          ↓

       h_X(Y') ───────────────────────→ h_X(Y)
                          h_X(u)
```

is commutative; this means that for the composition laws $\gamma_{X}(Y)$ and $\gamma_{X}(Y')$, $h_{X}(u)$ is a
homomorphism from $h_{X}(Y')$ into $h_{X}(Y)$.

In the same way, given two objects $Z$, $X$ of $\mathcal{C}$, one calls an *external composition law* on $X$, *having
$Z$ as domain of operators*, a functorial morphism

```text
  ω_{X,Z} : h_Z × h_X → h_X.                                               (8.2.1.2)
```

One sees as above that for every $Y \in \mathcal{C}$, $\omega_{X,Z}(Y)$ is an external composition law on $h_{X}(Y)$,
having $h_{Z}(Y)$ as domain of operators, and such that for every morphism $u : Y \to Y'$, $h_{Z}(u)$ and $h_{X}(u)$
form a *di-homomorphism* from $(h_{Z}(Y'), h_{X}(Y'))$ into $(h_{Z}(Y), h_{X}(Y))$.

**8.2.2.**

<!-- label: 0_III.8.2.2 -->

Let $X'$ be a second object of $\mathcal{C}$, and suppose given on $X'$ an internal composition law $\gamma_{X'}$; we
shall say that a morphism $w : X \to X'$ in $\mathcal{C}$ is a *homomorphism* for these composition laws, if for every
$Y \in \mathcal{C}$, $h_{w}(Y) : h_{X}(Y) \to h_{X'}(Y)$ is a homomorphism for the composition laws $\gamma_{X}(Y)$ and
$\gamma_{X'}(Y)$. If `X''` is a third

<!-- original page 10 -->

object of $\mathcal{C}$ equipped with an internal composition law $\gamma_{X''}$ and $w' : X' \to X''$ a morphism in
$\mathcal{C}$ which is a homomorphism for $\gamma_{X'}$ and $\gamma_{X''}$, it is clear that the morphism $w' \circ w :
X \to X''$ is a homomorphism for the composition laws $\gamma_{X}$ and $\gamma_{X''}$. An isomorphism $w : X
\xrightarrow{\sim} X'$ in $\mathcal{C}$ is called an *isomorphism for the composition laws $\gamma_{X}$ and
$\gamma_{X'}$* if $w$ is a homomorphism for these composition laws, and if its inverse morphism $w^{-1}$ is a
homomorphism for the composition laws $\gamma_{X'}$ and $\gamma_{X}$.

One defines in the same way the *di-homomorphisms* for the pairs of objects of $\mathcal{C}$ equipped with external
composition laws.

**8.2.3.**

<!-- label: 0_III.8.2.3 -->

When an internal composition law $\gamma_{X}$ on an object $X \in \mathcal{C}$ is such that $\gamma_{X}(Y)$ is a *group
law* on $h_{X}(Y)$ for every $Y \in \mathcal{C}$, we say that $X$, equipped with this law, is a *$\mathcal{C}$-group* or
a *$\mathcal{C}$-object in groups*. One defines in the same way *$\mathcal{C}$-rings*, *$\mathcal{C}$-modules*, etc.

**8.2.4.**

<!-- label: 0_III.8.2.4 -->

Suppose that the product $X \times X$ of an object $X \in \mathcal{C}$ by itself exists in $\mathcal{C}$; by definition,
we then have $h_{X \times X} = h_{X} \times h_{X}$ up to canonical isomorphism, since this is a particular case of
projective limit `(8.1.9)`; an internal composition law on $X$ may therefore be considered as a functorial morphism
$\gamma_{X} : h_{X \times X} \to h_{X}$, and so canonically determines `(8.1.6)` an element $c_{X} \in
\operatorname{Hom}(X \times X, X)$ such that $h_{c_{X}} = \gamma_{X}$; in this case, the data of an internal composition
law on $X$ is therefore equivalent to that of a morphism $X \times X \to X$; when $\mathcal{C}$ is the category `Set`,
one recovers the classical notion of internal composition law on a set. One has an analogous result for an external
composition law when the product $Z \times X$ exists in $\mathcal{C}$.

**8.2.5.**

<!-- label: 0_III.8.2.5 -->

With the preceding notations, suppose in addition that $X \times X \times X$ exists in $\mathcal{C}$; the
characterization of the product as an object representing a functor `(8.1.9)` entails the existence of canonical
isomorphisms

```text
  (X × X) × X ⥲ X × X × X ⥲ X × (X × X);
```

if one canonically identifies $X \times X \times X$ with $(X \times X) \times X$, the map $\gamma_{X}(Y) \times
1_{h_{X}(Y)}$ identifies with $h_{c_{X} \times 1_{X}}(Y)$ for every $Y \in \mathcal{C}$. It is therefore equivalent to
say that for every $Y \in \mathcal{C}$, the internal law $\gamma_{X}(Y)$ is *associative*, or that the diagram of maps

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

Under the hypotheses of `(8.2.5)`, if one wants to express that for every $Y \in \mathcal{C}$, the internal law
$\gamma_{X}(Y)$ is a *group law*, it is necessary, on the one hand, to express that it is associative, and on the other
that there exists a map $\alpha_{X}(Y) : h_{X}(Y) \to h_{X}(Y)$ having the properties of the *inverse* in a group; since
for every morphism $u : Y \to Y'$ in $\mathcal{C}$, we have seen that $h_{X}(u)$ must be a group homomorphism $h_{X}(Y')
\to h_{X}(Y)$, one sees first that $\alpha_{X} : h_{X} \to h_{X}$ *must be a functorial morphism*. One can on the other
hand express the characteristic properties of the inverse $s \mapsto s^{-1}$ in a group $G$ without making the neutral
element intervene: it suffices to write that the two composed maps

```text
  (s, t) ↦ (s, s^{−1}, t) ↦ (s, s^{−1} t) ↦ s(s^{−1} t)
  (s, t) ↦ (s, s^{−1}, t) ↦ (s, t s^{−1}) ↦ (t s^{−1}) s
```

are equal to the second projection $(s, t) \mapsto t$ from $G \times G$ into $G$. By virtue of `(8.1.3)`, we have
$\alpha_{X} = h_{a_{X}}$, where $a_{X} \in \operatorname{Hom}(X, X)$; the first preceding condition then expresses that
the composed morphism

```text
                  (1_X, a_X) × 1_X         1_X × c_X            c_X
   X × X ──────────────────────→ X × X × X ────────→ X × X ────────→ X
```

is the second projection $X \times X \to X$ in $\mathcal{C}$, and the second condition is translated similarly.

**8.2.7.**

<!-- label: 0_III.8.2.7 -->

Suppose now that there exists in $\mathcal{C}$ a final object $e$ `(8.1.10)`. Suppose still that $\gamma_{X}(Y)$ is a
group law on $h_{X}(Y)$ for every $Y \in \mathcal{C}$, and denote by $\eta_{X}(Y)$ the neutral element of
$\gamma_{X}(Y)$. Since, for every morphism $u : Y \to Y'$ in $\mathcal{C}$, $h_{X}(u)$ is a group homomorphism, we have
$\eta_{X}(Y) = (h_{X}(u))(\eta_{X}(Y'))$; taking in particular $Y' = e$, in which case $u$ is the unique element
$\epsilon$ of $\operatorname{Hom}(Y, e)$, we see that the element $\eta_{X}(e)$ completely determines $\eta_{X}(Y)$ for
every $Y \in \mathcal{C}$. Set $e_{X} = \eta_{X}(X)$, the neutral element of the group $h_{X}(X) = \operatorname{Hom}(X,
X)$; the commutativity of the diagram

```text
              h_ε(X)
   h_X(e) ───────────→ h_X(Y)

   h_{e_X}(e) │           │ h_{e_X}(Y)
              ↓           ↓

   h_X(e) ───────────→ h_X(Y)
              h_ε(X)
```

(cf. `8.1.2`) shows that, in the set $h_{X}(Y)$, the map $h_{e_{X}}(Y)$ is none other than

<!-- original page 12 -->

$s \mapsto \eta_{X}(Y)$, transforming every element into the neutral element. One then verifies that the fact that
$\eta_{X}(Y)$ is the neutral element of $\gamma_{X}(Y)$ for every $Y \in \mathcal{C}$ is equivalent to saying that the
composed morphism

```text
              (1_X, 1_X)         1_X × e_X            c_X
   X ──────────────────→ X × X ──────────→ X × X ──────→ X,
```

and the analogous one where one permutes `1_X` and $e_{X}$, are both equal to `1_X`.

**8.2.8.**

<!-- label: 0_III.8.2.8 -->

One could of course multiply without difficulty the examples of algebraic structures in categories. The example of
groups has been treated with sufficient detail, but in what follows we shall generally leave to the reader the task of
developing analogous considerations in the examples of algebraic structures that we shall encounter.

______________________________________________________________________

> _Translator's footnote (from p. 5)._ To facilitate reference lookup, we shall henceforth refer to the paragraphs of
> Chapter 0 published with Chapter I by the sign `0_I`.
