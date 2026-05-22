<!-- original page 255 -->

## §21. Divisors

On the content of the present section, see the comments of the introduction to §20. For the global properties of
divisors, the reader is referred to the section devoted to them in chap. V.

### 21.1. Divisors on a ringed space

**(21.1.1).** Let $(X, \mathcal{O}_{X})$ be a ringed space, $\mathcal{M}_{X}$ the sheaf of germs of meromorphic
functions on $X$ `(20.1.3)`, $\mathcal{M}^{\times}_{X}$ the sheaf (of multiplicative groups) of germs of regular
meromorphic functions on $X$ `(20.1.8)`. It is clear that the sheaf (of multiplicative groups)
$\mathcal{O}^{\times}_{X}$ of germs of invertible sections of $\mathcal{O}_{X}$ is canonically identified with a
subsheaf (of multiplicative groups) of $\mathcal{M}^{\times}_{X}$.

**Definition (21.1.2).**

<!-- label: IV.21.1.2 -->

*One calls **sheaf of divisors on $X$** and denotes by $\mathcal{D}iv_{X}$ the quotient sheaf (of commutative groups)
$\mathcal{M}^{\times}_{X} / \mathcal{O}^{\times}_{X}$; the sections of this sheaf over $X$ are called **divisors on
$X$**; they form a commutative group denoted $\operatorname{Div}(X)$. For every section $f$ of
$\mathcal{M}^{\times}_{X}$ over $X$ (in other words, every regular meromorphic function on $X$ `(20.1.8)`), one calls
**divisor of $f$** and denotes by $div(f)$ (or $div_{X}(f)$) the divisor on $X$ image of $f$ by the canonical
homomorphism $\Gamma(X, \mathcal{M}^{\times}_{X}) \to \Gamma(X, \mathcal{D}iv_{X})$.*

The **support** of a divisor $D$ is the closed set of $x \in X$ such that $D_{x} \neq 0$. One denotes it $Supp(D)$.

For every open $U$ of $X$, one obviously has $\mathcal{M}^{\times}_{X} | U = \mathcal{M}^{\times}_{U}$,
$\mathcal{O}^{\times}_{X} | U = \mathcal{O}^{\times}_{U}$, hence $\mathcal{D}iv_{X} | U = \mathcal{D}iv_{U}$, and
consequently the sheaf $\mathcal{D}iv_{X}$ is equal to the presheaf $U \mapsto \operatorname{Div}(U)$.

When $X = \operatorname{Spec}(A)$ is affine, one writes $\operatorname{Div}(A)$ instead of
$\operatorname{Div}(\operatorname{Spec}(A))$.

**(21.1.3).** We shall always denote the group $\operatorname{Div}(X)$ of divisors on $X$ *additively*. For two regular
meromorphic functions $f$, $g$ on $X$, one therefore has

```text
  (21.1.3.1)             div(fg) = div(f) + div(g),

  (21.1.3.2)             div(f⁻¹) = −div(f).
```

By definition, for every regular meromorphic function $f$ on $X$, one has the equivalence

```text
  (21.1.3.3)             div(f) = 0  ⟺  f ∈ Γ(X, 𝒪_X^×),
```

whence, for two regular meromorphic functions $f$, $g$ on $X$,

```text
  (21.1.3.4)             div(f) = div(g)  ⟺  f = ug, u ∈ Γ(X, 𝒪_X^×).
```

**(21.1.4).** Let now $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module, and let $s$ be a regular meromorphic
section `(20.1.8)` of $\mathcal{L}$ over $X$. Every $x \in X$ possesses an open neighbourhood $U$ such that $\mathcal{L}
| U$ is isomorphic to $\mathcal{O}_{U}$, hence $\mathcal{M}_{X}(\mathcal{L}) | U$ isomorphic to $\mathcal{M}_{U}$; by
one of these isomorphisms, $s | U$ corresponds to a section $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, and since two
isomorphisms of $\mathcal{L} | U$ onto $\mathcal{O}_{U}$ differ only by multiplication by an element of $\Gamma(U,
\mathcal{O}^{\times}_{X})$ $(0_{I}, 5.4.3)$, the element $div_{U}(f)$ of $\Gamma(U, \mathcal{D}iv_{X})$ is independent
of the chosen isomorphism; it is clear that these elements (for variable $U$) are the restrictions of a section of
$\mathcal{D}iv_{X}$ over $X$, which one calls the **divisor of $s$** and denotes $div(s)$ (such a divisor is not
necessarily of the form $div(g)$ for a regular meromorphic function $g$ on $X$; see `(21.2.9)`). For $\mathcal{L} =
\mathcal{O}_{X}$ the definition of $div(s)$ coincides with that of `(21.1.2)`. If $\mathcal{L}$, $\mathcal{L}'$ are two
invertible $\mathcal{O}_{X}$-Modules, $s$ (resp. $s'$) a regular meromorphic section of $\mathcal{L}$ (resp.
$\mathcal{L}'$) over $X$, it is immediate that one has

```text
  (21.1.4.1)             div(s ⊗ s') = div(s) + div(s')

  (21.1.4.2)             div(s^⊗ n) = n · div(s)        for every n ∈ ℤ
```

($s^{-1}$ being the regular meromorphic section of $\mathcal{L}^{-1}$ over $X$ defined in `(20.1.10)`), and, for two
regular meromorphic sections $s$, $s'$ of $\mathcal{L}$ over $X$, one has the relation

```text
  (21.1.4.3)             div(s) = div(s')  ⟺  s' = ts, with t ∈ Γ(X, 𝒪_X^×).
```

<!-- original page 256 -->

**(21.1.5).** The sheaf $\mathcal{S}(\mathcal{O}_{X})$ `(20.1.3)` whose sections over an open $U$ of $X$ are the regular
elements of $\Gamma(U, \mathcal{O}_{X})$ is a subsheaf of monoids of $\mathcal{M}^{\times}_{X}$; one can write

$$ (21.1.5.1) \mathcal{S}(\mathcal{O}_{X}) = \mathcal{O}_{X} \cap \mathcal{M}^{\times}_{X}. $$

If one denotes by $\mathcal{S}(\mathcal{O}_{X})^{-1}$ the sheaf whose sections over $U$ are the inverses in $\Gamma(U,
\mathcal{M}^{\times}_{X})$ of the elements of $\Gamma(U, \mathcal{S}(\mathcal{O}_{X}))$, it is clear that one has
$\Gamma(U, \mathcal{S}(\mathcal{O}_{X})) \cap \Gamma(U, \mathcal{S}(\mathcal{O}_{X})^{-1}) = \Gamma(U,
\mathcal{O}^{\times}_{X})$, hence

$$ (21.1.5.2) \mathcal{S}(\mathcal{O}_{X}) \cap \mathcal{S}(\mathcal{O}_{X})^{-1} = \mathcal{O}^{\times}_{X}. $$

**Definition (21.1.6).**

<!-- label: IV.21.1.6 -->

*The subsheaf of sets of $\mathcal{D}iv_{X}$ that is the canonical image of the subsheaf $\mathcal{S}(\mathcal{O}_{X})$
of $\mathcal{M}^{\times}_{X}$ is denoted $\mathcal{D}iv^{+}_{X}$; its sections over $X$ are called **positive divisors
on $X$**, and their set is denoted $\operatorname{Div}^{+}(X)$.*

Since $\mathcal{S}(\mathcal{O}_{X})$ is a sheaf of (multiplicative) monoids, one has

```text
  (21.1.6.1)             Div^+(X) + Div^+(X) ⊂ Div^+(X)
```

and on the other hand, by virtue of `(21.1.5.2)` and `(21.1.3.3)`,

$$ (21.1.6.2) \operatorname{Div}^{+}(X) \cap (-\operatorname{Div}^{+}(X)) = {0}. $$

These two relations show that $\operatorname{Div}^{+}(X)$ is the set of positive elements for an order structure on the
group $\operatorname{Div}(X)$, compatible with this group structure; one denotes this order relation $D \geq D'$; in
other words, one has

$$ (21.1.6.3) D \geq 0 \Longleftrightarrow D \in \operatorname{Div}^{+}(X). $$

We shall always assume in what follows that $\operatorname{Div}(X)$ is endowed with this order structure; it is clear
that $\mathcal{D}iv^{+}_{X} | U = \mathcal{D}iv^{+}_{U}$, hence $\Gamma(U, \mathcal{D}iv^{+}_{X}) =
\operatorname{Div}^{+}(U)$, and one can therefore say that $\mathcal{D}iv^{+}_{X}$ defines on $\mathcal{D}iv_{X}$ a
structure of sheaf of ordered groups. The stalk $(\mathcal{D}iv_{X})_{x}$ at a point $x$ of the sheaf
$\mathcal{D}iv_{X}$ is a submonoid of the group $(\mathcal{D}iv_{X})_{x}$, the set of elements $\geq 0$ for an order
structure compatible with the group structure; for a divisor $D$ on $X$, it amounts to the same to say that $D \geq 0$
or that $D_{x} \geq 0$ for every $x \in X$.

By definition, for every regular meromorphic function $f$ on $X$, one has the relation

```text
  (21.1.6.4)             div(f) ≥ 0  ⟺  f ∈ Γ(X, 𝒮(𝒪_X));
```

in other words, $div(f) \geq 0$ signifies that $f$ is a regular section of $\mathcal{O}_{X}$, or also a section of
$\mathcal{O}_{X}$ invertible in $M(X)$.

More generally, given a divisor $D$ on $X$, the relation $div(f) \geq D$ is equivalent to the following: for every open
$U$ of $X$ such that $D | U = div_{U}(g)$, where $g \in \Gamma(U, \mathcal{M}^{\times}_{X})$, there exists a regular
element $t$ of $\Gamma(U, \mathcal{O}_{X})$ such that $f | U = tg$.

**(21.1.7).** Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module, $s$ a regular meromorphic section of
$\mathcal{L}$ over $X$; one has the relation

```text
  (21.1.7.1)             div(s) ≥ 0  ⟺  s ∈ Γ(X, ℒ) ∩ Γ(X, (𝓜_X(ℒ))^×)
```

as follows at once from the definitions `(21.1.4)` and `(21.1.6)`.

**Proposition (21.1.8).**

<!-- label: IV.21.1.8 -->

*Let $X$ be a locally Noetherian prescheme, $D$ a divisor on $X$. Suppose that for every $x \in X$ such that
$prof(\mathcal{O}_{X,x}) = 1$ one has $D_{x} \geq 0$ (resp. $D_{x} = 0$). Then one has $D \geq 0$ (resp. $D = 0$).*

The question being local on $X$, one may assume that $D = div(f)$, $f$ being a

<!-- original page 257 -->

regular meromorphic function on $X$; the relation $D_{x} \geq 0$ is equivalent to $x \in dom(f)$, hence the hypothesis
means that if $T = X - dom(f)$, one has $prof(\mathcal{O}_{X,x}) \geq 2$ for every $x \in T$ (since $dom(f)$ contains
the maximal points of $X$). Consequently `(5.10.5)` the restriction homomorphism $\Gamma(X, \mathcal{O}_{X}) \to
\Gamma(X - T, \mathcal{O}_{X})$ is bijective, which shows that there exists a section $s$ of $\mathcal{O}_{X}$ over $X$
such that $f = s | (X - T)$. But by definition of $T$, this implies $T = \emptyset$, hence $f = s$ and $D \geq 0$. The
assertion relative to the relation $D_{x} = 0$ follows at once by applying what precedes to $-D$, by virtue of
`(21.1.6.2)`.

**Corollary (21.1.9).**

<!-- label: IV.21.1.9 -->

*Let $X$ be a locally Noetherian prescheme, $D$ a divisor on $X$. Let $S$ be the support of $D$. Then, for every maximal
point $x$ of $S$, one has $prof(\mathcal{O}_{X,x}) \leq 1$.*

Indeed set $X_{1} = \operatorname{Spec}(\mathcal{O}_{X,x})$; in view of `(20.2.11)` and `(20.3.6)`, the sheaf
$\mathcal{O}_{X}$ is induced on `X_1` by $\mathcal{O}_{X}$, hence one may restrict to the case where $X = X_{1}$, in
which case, since $x \in S$ and $x$ is a maximal point of $S$, one necessarily has $S = {x}$. If one had
$prof(\mathcal{O}_{X,x}) \neq 1$, one would conclude, by virtue of `(21.1.8)`, that $D = 0$, which contradicts the
definition of $S$.

**Proposition (21.1.10).**

<!-- label: IV.21.1.10 -->

*Let $A$ be a Noetherian local ring; for $\operatorname{Div}(A) = 0$, it is necessary and sufficient that $prof(A) = 0$
(in other words, that the maximal ideal $\mathfrak{m}$ of $A$ be associated to $A$ `(0, 16.4.6)`).*

Indeed, to say that $\operatorname{Div}(A) = 0$ means that in $A$ every regular element is invertible, or also that all
the elements of $\mathfrak{m}$ are zero-divisors, which means that $\mathfrak{m} \in Ass(A)$ (Bourbaki, _Alg. comm._,
chap. IV, §1, n° 1, cor. 3 of prop. 2).

### 21.2. Divisors and invertible fractional Ideals

**(21.2.1).** Let $(X, \mathcal{O}_{X})$ be a ringed space. One calls **fractional Ideal on $X$** a
sub-$\mathcal{O}_{X}$-Module of the $\mathcal{O}_{X}$-Module $\mathcal{M}_{X}$ of germs of meromorphic functions on $X$.
A fractional Ideal $\mathcal{I}$ on $X$ which is an invertible $\mathcal{O}_{X}$-Module is called an **invertible
fractional Ideal**.

**Proposition (21.2.2).**

<!-- label: IV.21.2.2 -->

*For a fractional Ideal $\mathcal{I}$ on $X$ to be invertible, it is necessary and sufficient that for every $x \in X$,
there exist an open neighbourhood $U$ of $x$ and a section $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$ such that
$\mathcal{I} | U = \mathcal{O}_{U} \cdot f$.*

The condition is obviously sufficient, the map $s \mapsto s \cdot (f | V)$ from $\Gamma(V, \mathcal{O}_{X})$ to
$\Gamma(V, \mathcal{I})$ being obviously bijective for every open $V \subset U$. To see that it is necessary, note that
by hypothesis there exist an open neighbourhood $U$ of $x$ and an isomorphism of $\mathcal{O}_{X}$-Modules
$\mathcal{O}_{U} \xrightarrow{\sim} \mathcal{I} | U$. If $f$ is the image of the section $1 \in \Gamma(U,
\mathcal{O}_{X})$ by this isomorphism, one may assume, restricting $U$, that $f = u^{-1}s$, where $u \in \Gamma(U,
\mathcal{O}_{X})$ and $s \in \Gamma(U, \mathcal{S}(\mathcal{O}_{X}))$, and the considered isomorphism then makes
correspond, to every section $v \in \Gamma(V, \mathcal{O}_{X})$ (where $V$ is an open contained in $U$) the section $v(u
| V)^{-1} f(s | V)^{-1}$; to say that the map thus defined is bijective means that $u | V$ is a regular element of
$\Gamma(V, \mathcal{O}_{X})$, hence $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$.

One will note that for every open $U$ of $X$ such that $\mathcal{I} | U = \mathcal{O}_{U} \cdot f$ with $f \in \Gamma(U,
\mathcal{M}^{\times}_{X})$, the section $f$ is determined up to multiplication by an element of $\Gamma(U,
\mathcal{O}^{\times}_{X})$, since the

<!-- original page 258 -->

multiplication by these elements provides all the automorphisms of the $\mathcal{O}_{U}$-Module $\mathcal{O}_{U}$
$(0_{I}, 5.4.3)$.

**Corollary (21.2.3).**

<!-- label: IV.21.2.3 -->

*(i) Let $\mathcal{I}$ be an invertible fractional Ideal; then the invertible $\mathcal{O}_{X}$-Module
$\mathcal{I}^{-1}$ is canonically identified with the fractional Ideal $\mathcal{I}'$ (transporter of $\mathcal{I}$ into
$\mathcal{O}_{X}$) defined in the following way: for every open $U$ of $X$ such that $\mathcal{I} | U = \mathcal{O}_{U}
\cdot f$, where $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, one has $\mathcal{I}' | U = \mathcal{O}_{U} \cdot f^{-1}$.*

*(ii) If $\mathcal{I}_{1}$ and $\mathcal{I}_{2}$ are two invertible fractional Ideals, the canonical map
$\mathcal{I}_{1} \otimes \mathcal{I}_{2} \to \mathcal{I}_{1} \mathcal{I}_{2}$ is an isomorphism of
$\mathcal{O}_{X}$-Modules.*

Assertion (ii) follows at once from `(21.2.2)`. On the other hand, the remark made at the end of `(21.2.2)` shows that
there exists indeed one and only one fractional Ideal $\mathcal{I}'$ defined by the condition of the statement; the
canonical isomorphism of $\mathcal{I}'$ onto $\mathcal{I}^{-1} = \mathcal{H}\mathit{om}_{\mathcal{O}_{X}}(\mathcal{I},
\mathcal{O}_{X})$ is obtained by making correspond to every section $s \in \Gamma(V, \mathcal{I}^{-1})$ (where $V$ is an
open contained in $U$ and $f \in \Gamma(V, \mathcal{M}^{\times}_{X})$) the homomorphism $t(f | V)^{-1} \mapsto st$ from
$\Gamma(V, \mathcal{I})$ to $\Gamma(V, \mathcal{O}_{X})$.

By virtue of `(21.2.3, (i))`, one will generally identify the $\mathcal{O}_{X}$-Modules $\mathcal{I}'$ and
$\mathcal{I}^{-1}$, considering therefore $\mathcal{I}^{-1}$ as a sub-$\mathcal{O}_{X}$-Module of $\mathcal{M}_{X}$.

**(21.2.4).** It follows from `(21.2.3)` that the set `Id.inv(X)` of *invertible fractional Ideals on $X$* is endowed
with a structure of commutative group for the composition law $(\mathcal{I}_{1}, \mathcal{I}_{2}) \mapsto
\mathcal{I}_{1} \mathcal{I}_{2}$, the neutral element of this group being $\mathcal{O}_{X}$. It is clear that for every
open $U$ of $X$, one has $(\mathcal{I}_{1} \mathcal{I}_{2}) | U = (\mathcal{I}_{1} | U)(\mathcal{I}_{2} | U)$, hence the
restriction map $\mathcal{I} \mapsto \mathcal{I} | U$ is a homomorphism of groups $Id.inv(X) \to Id.inv(U)$; one thus
defines a *presheaf of commutative groups* $U \mapsto Id.inv(U)$; it is immediate that in fact this presheaf is a *sheaf
of commutative groups*, which one denotes $\mathit{Id}.\mathit{inv}_{X}$.

**(21.2.5).** For every regular meromorphic function $f \in \Gamma(X, \mathcal{M}^{\times}_{X})$, it follows from
`(21.2.2)` that $\mathcal{J}(f) = \mathcal{O}_{X} \cdot f$ is an invertible fractional Ideal, and one obviously has
$\mathcal{J}(f_{1} f_{2}) = \mathcal{J}(f_{1}) \mathcal{J}(f_{2})$; in other words the map $f \mapsto \mathcal{J}(f)$ is
a homomorphism from the commutative group $\Gamma(X, \mathcal{M}^{\times}_{X})$ into the commutative group `Id.inv(X)`.
Replacing $X$ by any open $U$ of $X$ and noting that the homomorphisms obtained are compatible with the operations of
restriction, one obtains a canonical homomorphism of sheaves of commutative groups:

$$ (21.2.5.1) \mathcal{J} : \mathcal{M}^{\times}_{X} \to \mathit{Id}.\mathit{inv}_{X}. $$

Note that if $f \in \Gamma(X, \mathcal{O}^{\times}_{X})$, one has $\mathcal{J}(f) = \mathcal{O}_{X}$; one deduces at
once that the homomorphism $\mathcal{J}$ factors as

```text
  (21.2.5.2)             𝓜_X^× → 𝓜_X^× / 𝒪_X^× = 𝒟iv_X → 𝐼𝑑.𝑖𝑛𝑣_X
```

<!-- original page 259 -->

where $\mathit{I}$ is a homomorphism from the sheaf of additive groups $\mathcal{D}iv_{X}$ into the sheaf of
multiplicative groups $\mathit{Id}.\mathit{inv}_{X}$; one therefore has for every open $U$ of $X$ a homomorphism
$\mathit{I}_{U} : \operatorname{Div}(U) \to Id.inv(U)$ of commutative groups, such that, for every section $f \in
\Gamma(U, \mathcal{M}^{\times}_{X})$, one has

$$ (21.2.5.3) \mathit{I}_{U}(div_{U}(f)) = \mathcal{O}_{U} \cdot f. $$

One concludes that $\mathit{I}(D)$, for every divisor $D \in \operatorname{Div}(X)$, is the invertible fractional Ideal
defined in the following way: for every open $U$ of $X$ such that $D | U = div_{U}(f)$, where $f \in \Gamma(U,
\mathcal{M}^{\times}_{X})$, $\mathit{I}(D) | U$ is the invertible fractional Ideal $\mathcal{O}_{U} \cdot f$. One
therefore has, by virtue of `(21.1.6)`, for every regular meromorphic function $f \in \Gamma(X,
\mathcal{M}^{\times}_{X})$, the relation

```text
  (21.2.5.4)             f ∈ Γ(X, 𝐼(D))  ⟺  div(f) ≥ D.
```

**Proposition (21.2.6).**

<!-- label: IV.21.2.6 -->

*The homomorphism $\mathit{I} : \mathcal{D}iv_{X} \to \mathit{Id}.\mathit{inv}_{X}$ is bijective.*

One defines a homomorphism $\mathit{I}_{X}'$ from `Id.inv(X)` into $\operatorname{Div}(X)$ by making correspond to every
invertible fractional Ideal $\mathcal{I}$ on $X$ the divisor $\mathit{I}_{X}'(\mathcal{I})$ defined in the following
way: for every open $U$ of $X$ such that $\mathcal{I} | U = \mathcal{O}_{U} \cdot f$, where $f \in \Gamma(U,
\mathcal{M}^{\times}_{X})$ `(21.2.2)`, one takes $\mathit{I}_{X}'(\mathcal{I}) | U = div_{U}(f)$; by virtue of the
remark following `(21.2.2)`, this definition is independent of the generator $f$ chosen in $\mathcal{I} | U$, and
determines indeed a divisor on $X$. Moreover, this definition shows at once that the homomorphisms $\mathit{I}_{X}$ and
$\mathit{I}_{X}'$ are reciprocal to one another. Replacing $X$ by any open $U$, one deduces the definition of the
isomorphism $\mathit{I}' : \mathit{Id}.\mathit{inv}_{X} \to \mathcal{D}iv_{X}$ reciprocal to $\mathit{I}$, whence the
proposition. One will set $\mathit{I}_{X}'(\mathcal{I}) = div(\mathcal{I})$, so that one has, for every regular
meromorphic function $f$ on $X$,

$$ (21.2.6.1) div(\mathcal{O}_{X} \cdot f) = div(f). $$

**(21.2.7).** One will often *identify* the sheaves $\mathcal{D}iv_{X}$ and $\mathit{Id}.\mathit{inv}_{X}$ (resp. the
groups $\operatorname{Div}(X)$ and `Id.inv(X)`) by means of the preceding isomorphisms $\mathit{I}$ and $\mathit{I}'$
(resp. $\mathit{I}_{X}$ and $\mathit{I}_{X}'$). One will note that one has the relation

```text
  (21.2.7.1)             D ≥ 0  ⟺  𝐼_X(D) ⊂ 𝒪_X       for D ∈ Div(X)
```

as follows at once from the definitions `(21.1.6)` and `(21.1.5.1)`; in other words, the image
$\mathit{I}_{X}(\operatorname{Div}^{+}(X))$ is the set of Ideals of $\mathcal{O}_{X}$ (also sometimes called *integral
Ideals*) that are invertible $\mathcal{O}_{X}$-Modules: such an Ideal $\mathcal{I}$ is again characterized by the fact
that for every $x \in X$, there is an open neighbourhood $U$ of $x$ in $X$ such that $\mathcal{I} | U = \mathcal{O}_{U}
\cdot f$, where $f$ is a regular element of $\Gamma(U, \mathcal{O}_{X})$. The set
$\mathit{I}_{X}(\operatorname{Div}^{+}(X))$ of these Ideals is therefore a submonoid of `Id.inv(X)`, equal to the set of
positive elements for an order relation compatible with the group structure of `Id.inv(X)`, and it is immediate that
this relation is none other than the relation opposite to inclusion; in other words, one has

```text
  (21.2.7.2)             ℐ_1 ⊂ ℐ_2  ⟺  div(ℐ_1) ≥ div(ℐ_2)
```

for $\mathcal{I}_{1}$, $\mathcal{I}_{2}$ in `Id.inv(X)`.

**(21.2.8).** For every divisor $D$ on $X$, one sets

$$ (21.2.8.1) \mathcal{O}_{X}(D) = (\mathit{I}_{X}(D))^{-1}; $$

$\mathcal{O}_{X}(D)$ is therefore an invertible fractional Ideal, defined in the following way: for every open $U$ of
$X$

<!-- original page 260 -->

such that $D | U = div_{U}(f)$, where $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, $\mathcal{O}_{X}(D) | U$ is the
invertible fractional Ideal $\mathcal{O}_{U} \cdot f^{-1}$; by virtue of `(21.1.6)`, for every regular meromorphic
function $f$, one has the relation

```text
  (21.2.8.2)             f ∈ Γ(X, 𝒪_X(D))  ⟺  div(f) ≥ −D.
```

Moreover, it is clear that one has canonical isomorphisms `(21.2.3)`

```text
  (21.2.8.3)             𝒪_X(0) = 𝒪_X,   𝒪_X(D + D') = 𝒪_X(D) ⊗ 𝒪_X(D'),
                         𝒪_X(nD) = (𝒪_X(D))^⊗ n,   𝒪_X(−D) = (𝒪_X(D))⁻¹
```

for every integer $n \in \mathbb{Z}$, and for any two divisors $D$, $D'$ on $X$.

**(21.2.9).** Let $\mathcal{I}$ be an invertible fractional Ideal on $X$. The canonical injection $\mathcal{I} \to
\mathcal{M}_{X}$ defines by tensorization a homomorphism of $\mathcal{O}_{X}$-Modules

```text
  (21.2.9.1)             𝓜_X(ℐ) = ℐ ⊗_{𝒪_X} 𝓜_X → 𝓜_X ⊗_{𝒪_X} 𝓜_X = 𝓜_X
```

which is an isomorphism: indeed, if $U$ is an open of $X$ such that $\mathcal{I} | U = \mathcal{O}_{U} \cdot f$, where
$f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, the homomorphism `(21.2.9.1)` restricted to $U$ is none other than the
isomorphism that to every section $t$ of $\mathcal{M}_{X}(\mathcal{I}) | U = \mathcal{M}_{U}$ over $V \subset U$ makes
correspond the section $t (f | V)^{-1}$ of the same sheaf. In the isomorphism `(21.2.9.1)`, to the regular meromorphic
sections of $\mathcal{I}$ over $X$ correspond the regular meromorphic functions on $X$.

Consider in particular the case where $\mathcal{I} = \mathcal{O}_{X}(D)$, where $D$ is a divisor on $X$; one then has a
canonical isomorphism

$$ (21.2.9.2) \mathcal{M}_{X}(\mathcal{O}_{X}(D)) \xrightarrow{\sim} \mathcal{M}_{X} $$

and one denotes by $s_{D}$ the regular meromorphic section of $\mathcal{O}_{X}(D)$ over $X$ which corresponds by this
isomorphism to the section `1` of $\mathcal{M}_{X}$. If $U$ is an open of $X$ such that $\mathcal{O}_{X}(D) | U =
\mathcal{O}_{U} \cdot f^{-1}$, where $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, one has $s_{D} | U = f$ in $\Gamma(U,
\mathcal{M}_{X})$; since one then has $D | U = div_{U}(f)$, one deduces `(21.1.4)` that one has

$$ (21.2.9.3) div(s_{D}) = D. $$

On the other hand, one deduces at once from the canonical isomorphisms `(21.2.8.3)` the formulas

```text
  (21.2.9.4)             s_0 = 1,   s_{D + D'} = s_D ⊗ s_{D'},   s_{nD} = s_D^{⊗ n}   (n ∈ ℤ).
```

**(21.2.10).** Let us consider, between two pairs $(\mathcal{L}, s)$, $(\mathcal{L}', s')$, where $\mathcal{L}$ and
$\mathcal{L}'$ are two invertible $\mathcal{O}_{X}$-Modules, $s$ (resp. $s'$) a regular meromorphic section of
$\mathcal{L}$ (resp. $\mathcal{L}'$) over $X$, the relation: "there exists an isomorphism $u : \mathcal{L}
\xrightarrow{\sim} \mathcal{L}'$ such that $\bar{u}(s) = s'$", where $\bar{u} : \Gamma(X, \mathcal{M}_{X}(\mathcal{L}))
\xrightarrow{\sim} \Gamma(X, \mathcal{M}_{X}(\mathcal{L}'))$ is the isomorphism deduced from $u$ (one will note that the
isomorphism $u$ verifying this condition is then uniquely determined). It is clear that this is an equivalence relation,
and since there exists a set of invertible $\mathcal{O}_{X}$-Modules such that every invertible $\mathcal{O}_{X}$-Module
is isomorphic to an element of this set $(0_{I}, 5.4.7)$, one can speak of the *set $D(X)$ of equivalence classes of
pairs $(\mathcal{L}, s)$* for the preceding relation. For every invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ and
every

<!-- original page 261 -->

regular meromorphic section $s$ of $\mathcal{L}$ over $X$, one will denote by $cl(\mathcal{L}, s)$ the element of $D(X)$
corresponding to the pair $(\mathcal{L}, s)$. It follows from $(0_{I}, 5.4.3)$ that if $s$, $s'$ are two regular
meromorphic sections of $\mathcal{L}$ over $X$, the relation $cl(\mathcal{L}, s) = cl(\mathcal{L}, s')$ is equivalent to
the existence of a section $t \in \Gamma(X, \mathcal{O}^{\times}_{X})$ such that $s' = ts$.

It is immediate that if $(\mathcal{L}, s)$ is equivalent to $(\mathcal{L}_{1}, s_{1})$ and $(\mathcal{L}', s')$ to
$(\mathcal{L}_{1}', s_{1}')$, the pairs $(\mathcal{L} \otimes \mathcal{L}', s \otimes s')$ and $(\mathcal{L}_{1} \otimes
\mathcal{L}_{1}', s_{1} \otimes s_{1}')$ are equivalent; one therefore defines in $D(X)$ a composition law by setting

```text
  (21.2.10.1)            cl(ℒ, s) · cl(ℒ', s') = cl(ℒ ⊗ ℒ', s ⊗ s');
```

it is immediate that this is a commutative group law, whose neutral element is $cl(\mathcal{O}_{X}, 1)$ and where the
inverse of $cl(\mathcal{L}, s)$ is $cl(\mathcal{L}^{-1}, s^{\otimes(-1)})$.

**Proposition (21.2.11).**

<!-- label: IV.21.2.11 -->

*The maps*

```text
  (21.2.11.1)            D ↦ cl(𝒪_X(D), s_D),       cl(ℒ, s) ↦ div(s)
```

*are reciprocal isomorphisms of $\operatorname{Div}(X)$ onto $D(X)$ and of $D(X)$ onto $\operatorname{Div}(X)$
respectively.*

In view of `(21.2.8.3)`, `(21.2.9.4)` and `(21.2.10.1)`, it suffices to see that the composites of these two maps are
the identity in $\operatorname{Div}(X)$ and $D(X)$ respectively. The first assertion is none other than `(21.2.9.3)`. On
the other hand, let $D = div(s)$, where $s$ is a regular meromorphic section of $\mathcal{L}$ over $X$, and let $U$ be
an open of $X$ such that there exists an isomorphism of $\mathcal{L} | U$ onto $\mathcal{O}_{U}$ transforming $s | U$
into $f \in \Gamma(U, \mathcal{M}^{\times}_{X})$, so that $D | U = div_{U}(f)$, $\mathcal{O}_{X}(D) | U =
\mathcal{O}_{U} \cdot f^{-1}$, and $s_{D} | U$ is the unit element of $\Gamma(U, \mathcal{O}^{\times}_{X})$. There is
therefore an isomorphism $v_{U} : \mathcal{L} | U \to \mathcal{O}_{U} \cdot f^{-1} = \mathcal{O}_{X}(D) | U$ such that
$\bar{v}_{U}$ (notation of `(21.2.10)`) transforms $s | U$ into $f \cdot f^{-1} = 1$; one sees at once that these
isomorphisms are compatible with the operations of restriction, hence define an isomorphism $v : \mathcal{L} \to
\mathcal{O}_{X}(D)$ such that $\bar{v}(s) = s_{D}$. Q.E.D.

One can transport, by the first of the isomorphisms `(21.2.11.1)`, the ordered group structure of
$\operatorname{Div}(X)$ to $D(X)$; the elements $\geq 0$ of $D(X)$ are therefore the classes $cl(\mathcal{L}, s)$ such
that $div(s) \geq 0$, that is to say `(21.1.7.1)` such that

```text
                         s ∈ Γ(X, ℒ) ∩ Γ(X, (𝓜_X(ℒ))^×).
```

**(21.2.12).** Let $D$ be a positive divisor on a prescheme $X$; the fractional Ideal $\mathcal{O}_{X}(D)$ is therefore
an Ideal of $\mathcal{O}_{X}$ which is an invertible $\mathcal{O}_{X}$-Module; let $Y(D)$ be the closed sub-prescheme of
$X$ it defines. For every $x \in Y(D)$, there is by hypothesis an open neighbourhood $U$ of $x$ in $X$ and a regular
section $t \in \Gamma(U, \mathcal{O}_{X})$ such that $\mathcal{O}_{X}(D) | U = \mathcal{O}_{U} \cdot t \cdot
(\mathcal{O}_{X} | U)$; in other words, the canonical immersion $Y(D) \to X$ is *regular and of codimension `1`*
`(19.1.4)` at every point of $Y(D)$. Conversely, if $Y$ is a closed sub-prescheme of $X$, regularly immersed in $X$ and
of codimension `1` at every point of $Y$, there exists *one and only one positive divisor* $D$ such that $Y(D) = Y$, for
every $x \in Y$, there is a neighbourhood $U$ of $x$ in $X$ such that $Y \cap U$ is defined by an Ideal of
$\mathcal{O}_{X}$ of the form $\mathcal{O}_{U} \cdot t$, where $t$ is regular in $\Gamma(U, \mathcal{O}_{X})$.

One will note that one then has $Supp(D) = Y(D)$, for to say that $D_{x} \neq 0$ means that $t$ (with the notations
above) is not invertible, that is to say that $x \in Y(D)$.

<!-- original page 262 -->

### 21.3. Linear equivalence of divisors

**(21.3.1).** One says that a divisor $D$ on $X$ is *principal* if it is of the form $div(f)$, where $f$ is a regular
meromorphic function on $X$; the regular meromorphic functions $f'$ such that $div(f') = D$ are then all those of the
form `tf`, where $t \in \Gamma(X, \mathcal{O}^{\times}_{X})$ `(21.1.3.4)`. The set of principal divisors is a subgroup
of $\operatorname{Div}(X)$, denoted $\operatorname{Div}.princ(X)$, isomorphic to $\Gamma(X, \mathcal{M}^{\times}_{X}) /
\Gamma(X, \mathcal{O}^{\times}_{X})$. Two divisors $D$, $D'$ are said to be *linearly equivalent* if $D - D'$ is a
principal divisor; the principal divisors are therefore the divisors *linearly equivalent to `0`*.

**(21.3.2).** Recall $(0_{I}, 5.4.7)$ that one can speak of the set of equivalence classes of invertible
$\mathcal{O}_{X}$-Modules for the relation of isomorphy; one denotes this set by $\operatorname{Pic}(X)$, and for every
invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$, one denotes by $cl(\mathcal{L})$ the equivalence class of
$\mathcal{O}_{X}$-Modules isomorphic to $\mathcal{L}$; moreover, $\operatorname{Pic}(X)$ is a commutative group for the
multiplication defined by $cl(\mathcal{L}) cl(\mathcal{L}') = cl(\mathcal{L} \otimes \mathcal{L}')$. It is clear that
the map

```text
  (21.3.2.1)             𝓁' : cl(ℒ, s) ↦ cl(ℒ)
```

is a homomorphism from the group $D(X)$ `(21.2.10)` into the group $\operatorname{Pic}(X)$. By composition, one
therefore deduces a homomorphism

```text
  (21.3.2.2)             𝓁 : Div(X) ⥲ D(X) → Pic(X)
```

(also denoted $\mathcal{l}_{X}$) such that, for every divisor $D$, one has

$$ (21.3.2.3) \mathcal{l}(D) = cl(\mathcal{O}_{X}(D)). $$

Note finally that, if $u : X' \to X$ is a morphism of ringed spaces, $\mathcal{L}_{1}$, $\mathcal{L}_{2}$ two isomorphic
invertible $\mathcal{O}_{X}$-Modules, the invertible $\mathcal{O}_{X'}$-Modules $u^{*}(\mathcal{L}_{1})$ and
$u^{*}(\mathcal{L}_{2})$ $(0_{I}, 5.4.5)$ are isomorphic; since moreover, for any two invertible
$\mathcal{O}_{X}$-Modules $\mathcal{L}_{1}$, $\mathcal{L}_{2}$, one has $u^{*}(\mathcal{L}_{1} \otimes \mathcal{L}_{2})
= u^{*}(\mathcal{L}_{1}) \otimes u^{*}(\mathcal{L}_{2})$ up to canonical isomorphism $(0_{I}, 4.3.3)$, one sees that the
morphism $u$ canonically defines a homomorphism of commutative groups

```text
  (21.3.2.4)             Pic(u) : Pic(X) → Pic(X').
```

**Proposition (21.3.3).**

<!-- label: IV.21.3.3 -->

*(i) The kernel of the canonical homomorphism $\mathcal{l} : \operatorname{Div}(X) \to \operatorname{Pic}(X)$ is the
subgroup $\operatorname{Div}.princ(X)$; in other words, for $\mathcal{O}_{X}(D)$ and $\mathcal{O}_{X}(D')$ to be
isomorphic, it is necessary and sufficient that $D$ and $D'$ be linearly equivalent. One therefore has a canonical
injective homomorphism*

```text
  (21.3.3.1)             Div(X) / Div.princ(X) → Pic(X)
```

*deduced from $\mathcal{l}$.*

*(ii) For an invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ to be such that $cl(\mathcal{L})$ is of the form
$\mathcal{l}(D)$, or also for $\mathcal{L}$ to be isomorphic to an $\mathcal{O}_{X}$-Module of the form
$\mathcal{O}_{X}(D)$, it is necessary and sufficient that there exist a regular meromorphic section of $\mathcal{L}$.*

<!-- original page 263 -->

The proposition follows at once from the definitions and from `(21.2.10)`.

**Proposition (21.3.4).**

<!-- label: IV.21.3.4 -->

*Let $X$ be a prescheme satisfying one of the two following hypotheses:*

*a) $X$ is locally Noetherian and $Ass(\mathcal{O}_{X})$ is contained in an affine open of $X$.*

*b) $X$ is reduced and the set of its irreducible components is locally finite.*

*Then the canonical homomorphism $\mathcal{l} : \operatorname{Div}(X) \to \operatorname{Pic}(X)$ is surjective, and
gives, by passage to the quotient, an isomorphism*

```text
                         Div(X) / Div.princ(X) ⥲ Pic(X).
```

It suffices to show that every invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ admits a regular meromorphic section
over $X$ `(21.3.3)`. In the two cases, it suffices, thanks to `(20.2.11, (ii))`, to define a section $s$ of
$(\mathcal{M}_{X}(\mathcal{L}))^{\times}$ over a schematically dense open $U$ of $X$, or also in case a), over an open
$U$ containing $Ass(\mathcal{O}_{X})$ `(20.2.13, (iv))`. Indeed, let $V$ be any open of $X$ such that $\mathcal{L} | V$
is isomorphic to $\mathcal{O}_{V}$, so that there exists an isomorphism of $\mathcal{M}_{X}(\mathcal{L}) | V$ onto
$\mathcal{M}_{X} | V$, transforming $s | (U \cap V)$ into a section $f_{V}$ of $\mathcal{M}_{X}$ over $U \cap V$. Since
$U \cap V$ is schematically dense in $V$, it follows from `(20.2.11)` that there exists one and only one regular
meromorphic function $g_{V}$ on $V$ such that $g_{V} | (U \cap V) = f_{V}$, and this section therefore corresponds, by
the isomorphism considered, to a regular meromorphic section $u_{V}$ of $\mathcal{L}$ over $V$ such that $u_{V} | (U
\cap V) = s | (U \cap V)$. Moreover, if $V'$ is a second open of $X$ such that $\mathcal{L} | V'$ is isomorphic to
$\mathcal{O}_{V'}$, the restrictions of $u_{V}$ and $u_{V'}$ to $V \cap V'$ are equal, for they correspond by
isomorphism to two meromorphic functions which coincide in a schematically dense open $U \cap V \cap V'$, and one
concludes again by `(20.2.11)`; the $u_{V}$ are therefore the restrictions of a section of
$(\mathcal{M}_{X}(\mathcal{L}))^{\times}$ over $X$.

This being so, in case b), one takes for each of the maximal points $x_{\lambda}$ of $X$ an open $U_{\lambda}$
containing $x_{\lambda}$, not meeting any irreducible component of $X$ distinct from ${x_{\lambda}}$ and such that
$\mathcal{L} | U_{\lambda}$ is isomorphic to $\mathcal{O}_{U_{\lambda}}$; one will take for $s$ the section such that $s
| U_{\lambda}$ is the section of $\mathcal{L} | U_{\lambda}$ corresponding by the preceding isomorphism to the unit
section of $\mathcal{O}_{U_{\lambda}}$.

In case a), one can take by hypothesis for $U$ an affine open (hence Noetherian); in other words, one may assume that $X
= \operatorname{Spec}(A)$, where $A$ is Noetherian, and $\mathcal{L} = \tilde{P}$, where $P$ is a projective $A$-module
of rank `1`. If $S$ is the set of regular elements of $A$, one has $\Gamma(X, \mathcal{M}_{X}) = S^{-1} A$ `(20.2.12)`
and $\Gamma(X, \mathcal{M}_{X}(\mathcal{L})) = S^{-1} P$. But $S$ is the set of elements not belonging to any of the
ideals associated to $A$, hence $S^{-1} A$ is a semi-local ring whose maximal ideals come from the maximal elements of
$Ass(A)$, and $S^{-1} P$ is a projective $S^{-1} A$-module of rank `1`, hence here free of rank `1` (Bourbaki, _Alg.
comm._, chap. II, §5, n° 3, prop. 5); an element forming a basis of this $S^{-1} A$-module is therefore `(20.1.8)` a
regular meromorphic section of $\mathcal{L}$ over $X$.

**Corollary (21.3.5).**

<!-- label: IV.21.3.5 -->

*If $X$ is a Noetherian prescheme such that there exists an ample invertible $\mathcal{O}_{X}$-Module `(II, 4.5.3)` (for
example a quasi-projective prescheme over the spectrum of a Noetherian ring `(II, 5.3.1` and `4.6.6)`), the canonical
homomorphism $\mathcal{l} : \operatorname{Div}(X) \to \operatorname{Pic}(X)$ is surjective.*

<!-- original page 264 -->

Indeed `(II, 4.5.4)`, there then exists an affine open neighbourhood of the finite set $Ass(\mathcal{O}_{X})$.

**Remark (21.3.6).**

<!-- label: IV.21.3.6 -->

*Recall $(0_{I}, 5.4.7)$ that one has a canonical isomorphism $\pi : H^{1}(X, \mathcal{O}^{\times}_{X})
\xrightarrow{\sim} \operatorname{Pic}(X)$ defined in the following way. One starts from a `1`-cocycle $(c_{\alpha
\beta})$ with values in $\mathcal{O}^{\times}_{X}$ corresponding to an open cover $(U_{\alpha})$ of $X$, $c_{\alpha
\beta}$ being an element of $\Gamma(U_{\alpha} \cap U_{\beta}, \mathcal{O}^{\times}_{X})$, and one associates with it
the class of the invertible $\mathcal{O}_{X}$-Module obtained by gluing the $\mathcal{O}_{U_{\alpha}}$ along the
isomorphisms $\mathcal{O}_{X} | (U_{\alpha} \cap U_{\beta}) \xrightarrow{\sim} \mathcal{O}_{X} | (U_{\alpha} \cap
U_{\beta})$ defined by multiplication by $c_{\alpha \beta}$. On the other hand, one deduces from the exact sequence of
sheaves of commutative groups*

$$ 1 \to \mathcal{O}^{\times}_{X} \to \mathcal{M}^{\times}_{X} \to \mathcal{D}iv_{X} \to 0 $$

*the connecting homomorphism of the exact cohomology sequence*

$$ (21.3.6.1) \partial : \operatorname{Div}(X) \to H^{1}(X, \mathcal{O}^{\times}_{X}). $$

*Let us show that the composite homomorphism*

```text
                                                ∂              π
                         Div(X) → H^1(X, 𝒪_X^×) ⥲ Pic(X)
```

*is none other than the homomorphism $\mathcal{l}$ defined in `(21.3.2.2)`. Indeed, one must start from a divisor $D$
and an open cover $(U_{\alpha})$ of $X$ such that $D | U_{\alpha} = div_{U_{\alpha}}(g_{\alpha})$, where $g_{\alpha}$ is
a regular meromorphic function over $U_{\alpha}$; $\partial(D)$ is the cohomology class of the cocycle $(c_{\alpha
\beta})$, where $c_{\alpha \beta} = g_{\alpha|\alpha \beta} g^{-1}_{\beta|\alpha \beta}$, $g_{\alpha|\alpha \beta}$
denoting the restriction of $g_{\alpha}$ to $U_{\alpha} \cap U_{\beta}$. It is clear that the image by $\pi$ of this
cohomology class is the class of the invertible fractional Ideal $\mathcal{L}$ such that for every $\alpha$,
$\mathcal{L} | U_{\alpha} = \mathcal{O}_{U_{\alpha}} \cdot g^{-1}_{\alpha}$, which is none other by definition than
$\mathcal{O}_{X}(D)$ `(21.2.8)`.*

### 21.4. Inverse images of divisors

**(21.4.1).** Let $f : X' \to X$ be a morphism of ringed spaces; we propose to give conditions allowing us to associate
with a divisor $D$ on $X$ a divisor $D'$ on $X'$, *inverse image* of $D$ by $f$. Note first for this that for every
section $t \in \Gamma(X, \mathcal{O}^{\times}_{X})$, the image of $t$ by the canonical homomorphism $\Gamma(X,
\mathcal{O}_{X}) \to \Gamma(X', \mathcal{O}_{X'})$ is again invertible, in other words belongs to $\Gamma(X',
\mathcal{O}^{\times}_{X'})$. Consider then $D$ as given by the equivalence class of a pair $(\mathcal{L}, s)$, where
$\mathcal{L}$ is an invertible $\mathcal{O}_{X}$-Module and $s$ a regular meromorphic section of $\mathcal{L}$ over $X$
`(21.2.11)`. Form the invertible $\mathcal{O}_{X'}$-Module $f^{*}(\mathcal{L}) = \mathcal{L}'$; to say that the inverse
image $s \circ f$ of $s$ by $f$ exists `(20.1.11)` and is a regular meromorphic section of $\mathcal{L}'$ over $X'$
amounts to saying that the inverse images by $f$ of $s$ and of $s^{\otimes(-1)}$ exist, in other words that $s \in
\Gamma(X, \mathcal{M}_{f}(\mathcal{L}))$ and $s^{\otimes(-1)} \in \Gamma(X, \mathcal{M}_{f}(\mathcal{L}^{-1}))$; the
remark made above then shows that if $(\mathcal{L}_{1}, s_{1})$ is a pair equivalent to $(\mathcal{L}, s)$ in the sense
of `(21.2.10)`, the inverse image $s_{1} \circ f$ exists and is a regular meromorphic section of $\mathcal{L}_{1}' =
f^{*}(\mathcal{L}_{1})$ over $X'$, and the pairs $(\mathcal{L}', s \circ f)$ and $(\mathcal{L}_{1}', s_{1} \circ f)$ are
equivalent. One can therefore lay down the following definition:

**Definition (21.4.2).**

<!-- label: IV.21.4.2 -->

*Given a morphism $f : X' \to X$ of ringed spaces, one says that the **inverse image** by $f$ of a divisor $D$ on $X$
**exists** if one has $s_{D} \in \Gamma(X, \mathcal{M}_{f}(\mathcal{O}_{X}(D)))$ and $s_{-D} \in \Gamma(X,
\mathcal{M}_{f}(\mathcal{O}_{X}(-D)))$ (cf. `(20.1.11)`). One then calls **inverse image** of $D$ by $f$, and denotes by
$f^{*}(D)$, the divisor on $X'$ which corresponds canonically `(21.2.11)` to the class of the pair
$(f^{*}(\mathcal{O}_{X}(D)), s_{D} \circ f)$.*

It follows at once from this definition that if $D$ and $D'$ have inverse images under $f$, so do $-D$ and $D + D'$
(taking account of `(21.2.9.4)`) and that one has

<!-- original page 265 -->

$f^{*}(D + D') = f^{*}(D) + f^{*}(D')$. In other words, the set $\operatorname{Div}_{f}(X)$ of divisors on $X$ whose
inverse image by $f$ exists is a subgroup of $\operatorname{Div}(X)$, and the map $D \mapsto f^{*}(D)$ is an increasing
homomorphism from the ordered subgroup $\operatorname{Div}_{f}(X)$ into the ordered group $\operatorname{Div}(X')$,
making commutative the diagram

```text
                         Div_f(X) ─𝓁_X─→ Pic(X)
                            │              │
  (21.4.2.1)              f^*│              │ Pic(f)
                            ↓              ↓
                         Div(X') ─𝓁_{X'}→ Pic(X')
```

**(21.4.3).** Definition `(21.4.2)` shows at once that, for $f^{*}(D)$ to exist, it is necessary and sufficient that for
every open $U$ of $X$, the inverse image by $f_{U} : f^{-1}(U) \to U$ (restriction of $f$) of $D | U$ exist. Now, if $D
= div(g)$, where $g$ is a regular meromorphic function on $X$, to say that the inverse image of $s_{D}$ by $f$ exists
and is a regular meromorphic section of $f^{*}(\mathcal{O}_{X}(D))$ signifies `(21.2.9)` that the inverse image of $g$
by $f$ exists and is a regular meromorphic function on $X'$. One deduces at once a second description of
$\operatorname{Div}_{f}(X)$ and of $f^{*}(D)$: consider the subsheaf of groups of $\mathcal{M}^{\times}_{X}$, denoted
$\mathcal{M}^{f\times}_{X}$, formed of the germs of regular meromorphic functions on an open of $X$ whose inverse image
by $f$ exists and is regular on the inverse image open `(20.1.11)`. Then if $f = (\psi, \theta)$, the canonical
homomorphism `(20.1.11)` $\psi^{*}(\mathcal{M}_{X}) \to \mathcal{M}_{X'}$ gives by restriction a homomorphism of sheaves
of groups $\psi^{*}(\mathcal{M}^{f\times}_{X}) \to \mathcal{M}^{\times}_{X'}$. Setting $\mathcal{D}iv^{f}_{X} =
\mathcal{M}^{f\times}_{X} / \mathcal{O}^{\times}_{X}$, one has $\operatorname{Div}_{f}(X) = \Gamma(X,
\mathcal{D}iv^{f}_{X})$, and the map $D \mapsto f^{*}(D)$ corresponds to the homomorphism of sheaves of groups
$\psi^{*}(\mathcal{M}^{f\times}_{X}) / \psi^{*}(\mathcal{O}^{\times}_{X}) \to \mathcal{M}^{\times}_{X'} /
\mathcal{O}^{\times}_{X'} = \mathcal{D}iv_{X'}$ deduced from the preceding one by passage to the quotients.

**(21.4.4).** It follows at once from the preceding definitions that if $f' : X'' \to X'$ is a second morphism of ringed
spaces, $D$ a divisor on $X$ such that the inverse images $f^{*}(D)$ and $f'^{*}(f^{*}(D))$ exist, then $(f \circ
f')^{*}(D)$ exists and is equal to $f'^{*}(f^{*}(D))$.

**Proposition (21.4.5).**

<!-- label: IV.21.4.5 -->

*Let $f : X' \to X$ be a morphism of ringed spaces. In each of the three following cases, the inverse image by $f$ of
every divisor on $X$ is defined:*

*(i) $f$ is flat.*

*(ii) $X$ and $X'$ are locally Noetherian preschemes and one has $f(Ass(\mathcal{O}_{X'})) \subset
Ass(\mathcal{O}_{X})$.*

*(iii) $X$ and $X'$ are preschemes, the set of irreducible components of $X$ is locally finite, $X'$ is reduced, and
every irreducible component of $X'$ dominates an irreducible component of $X$.*

It suffices to show that in the three cases one has $\mathcal{M}^{f\times}_{X} = \mathcal{M}^{\times}_{X}$. In case (i),
this follows from `(20.1.12)`. In case (iii), one may restrict to the case where $X = \operatorname{Spec}(A)$ and $X' =
\operatorname{Spec}(A')$ are affine; if $s \in A$ is regular, it does not belong to any minimal prime ideal of $A$
`(20.1.3.1)`, hence the hypothesis implies that its image in $A'$ does not belong to any minimal prime ideal of $A'$,
and is consequently a regular element of $A'$ `(20.1.3.1)`. In case (ii) the meromorphic functions on $X'$ are
identified with the pseudo-functions on $X'$ `(20.2.11)`, and the hypothesis, joined to `(20.2.13, (iv))`, ensures that
the inverse image

<!-- original page 266 -->

by $f$ of every schematically dense open of $X$ is a schematically dense open of $X'$; one therefore concludes by
`(20.3.12)`.

**Corollary (21.4.6).**

<!-- label: IV.21.4.6 -->

*Let $X$ be a prescheme having one of the following properties:*

*(i) $X$ is locally Noetherian.*

*(ii) $X$ is reduced and the set of its irreducible components is locally finite.*

*Then, for every $x \in X$, one has a canonical isomorphism*

$$ (21.4.6.1) (\mathcal{D}iv_{X})_{x} \xrightarrow{\sim} \operatorname{Div}(\mathcal{O}_{X,x}). $$

This follows from `(20.2.11)`, `(20.3.7)` and from the fact that $\mathcal{O}^{\times}_{X}$ identifies with the group of
invertible elements of the ring $\mathcal{O}_{X,x}$.

**(21.4.7).** Let $X$, $X'$ be two preschemes, $f : X' \to X$ a morphism. If $D$ is a positive divisor on $X$ such that
the inverse image $f^{*}(D)$ is defined `(21.4.2)`, then the closed sub-prescheme $Y(f^{*}(D))$ of $X'$ is none other
than the inverse image $f^{-1}(Y(D))$; this follows at once from the definitions `(21.4.2)` and `(21.2.12)`.

**Proposition (21.4.8).**

<!-- label: IV.21.4.8 -->

*Let $X$, $Y$ be two preschemes; $f : X \to Y$ a faithfully flat morphism. Then, if a divisor $D$ on $Y$ is such that
$f^{*}(D) \geq 0$ (the existence of $f^{*}(D)$ following from `(21.4.5)`), one has $D \geq 0$. In particular, the map $D
\mapsto f^{*}(D)$ from $\operatorname{Div}(Y)$ to $\operatorname{Div}(X)$ is injective.*

The question being local on $Y$, one may restrict to the case where $D = div(w)$, with $w = uv^{-1}$, $u$ and $v$ being
two regular sections of $\mathcal{O}_{Y}$ over $Y$. By hypothesis one has $u\mathcal{O}_{X} \subset v\mathcal{O}_{X}$,
hence, for every $x \in X$, if one sets $y = f(x)$, one has $u_{y} \mathcal{O}_{x} \subset v_{y} \mathcal{O}_{x}$; one
concludes that $u_{y} \mathcal{O}_{y} \subset v_{y} \mathcal{O}_{y}$ by virtue of the hypothesis that $\mathcal{O}_{x}$
is a faithfully flat $\mathcal{O}_{y}$-module and of Bourbaki, _Alg. comm._, chap. I, §3, n° 5, prop. 10, (ii); whence
$u \mathcal{O}_{Y} \subset v \mathcal{O}_{Y}$ since $f$ is surjective, and consequently $D \geq 0$.

### 21.5. Direct images of divisors

**(21.5.1).** Let $X$, $X'$ be two preschemes, $f : X' \to X$ a morphism. We shall, in this n°, give sufficient
conditions to be able to associate with every divisor $D'$ on $X'$ a divisor $D$ on $X$, *direct image* of $D'$ by $f$.
We shall restrict to the case where $f$ is a *finite* morphism (for more general conditions, see the chapter of this
Treatise devoted to intersection theory).

**Lemma (21.5.2).**

<!-- label: IV.21.5.2 -->

*Let $A$ be a ring, $E$ a free $A$-module of finite rank. For an endomorphism $u$ of $E$ to be injective, it is
necessary and sufficient that $det(u)$ be a regular element of $A$.*

This is proved in Bourbaki, _Alg._, chap. III, 3rd ed., §8, n° 2, prop. 3.

**(21.5.3).** Suppose now that the morphism $f : X' \to X$ is finite, and moreover that $f$ verifies one of the two
following properties:

I) $f$ is a *finite locally free* morphism, in other words `(18.2.7)` the quasi-coherent $\mathcal{O}_{X}$-Module of
finite type $f_{*}(\mathcal{O}_{X'})$ is locally free.

II) $X$ is a reduced locally Noetherian prescheme, the $\mathcal{O}(X)$-Module $f_{*}(\mathcal{O}_{X'})
\otimes_{\mathcal{O}} \mathcal{K}(X)$ is locally free, and for every section $s' \in \Gamma(f^{-1}(U),
\mathcal{O}_{X'})$ ($U$ open

<!-- original page 267 -->

in $X$), $N_{X'/X}(s')$ is a section of $\mathcal{O}_{X}$ over $U$ (cf. `(II, 6.5.1)`). (One recalls that condition (II)
is verified for every finite morphism $f$ when $X$ is a locally Noetherian normal prescheme (_loc. cit._).)

One then knows `(II, 6.5.5)` that for every invertible $\mathcal{O}_{X'}$-Module $\mathcal{L}'$ one defines the norm
$\mathcal{L} = N_{X'/X}(\mathcal{L}')$ (which we shall also write $N(\mathcal{L}')$), which is an invertible
$\mathcal{O}_{X}$-Module. Moreover, for every open $U$ of $X$ and every regular section $s' \in \Gamma(f^{-1}(U),
\mathcal{O}_{X'})$, the norm $N_{X'/X}(s') = N_{f^{-1}(U)/U}(s')$ (which we shall also write $N(s')$) is a regular
element of $\Gamma(U, \mathcal{O}_{X})$; one is indeed at once reduced to the case where $U = X$ is affine, and then the
conclusion follows from `(21.5.2)` under hypothesis (I); on the other hand, under hypothesis (II), the fact that
$\mathcal{K}(X)$ is a flat $\mathcal{O}_{X}$-Module entails that the section $s' \otimes 1$ of $\Gamma(U,
f_{*}(\mathcal{O}_{X'}) \otimes_{\mathcal{O}} \mathcal{K}(X))$ is also regular $(0_{I}, 6.1.2)$, and the conclusion
follows again from `(21.5.2)` applied to the ring $\Gamma(U, \mathcal{K}(X))$, taking into account the definition of the
norm of a section `(II, 6.5.3)`. This being so, let $u'$ be a meromorphic section of $\mathcal{L}'$ over $X'$; the
morphism $f$ being affine, every point $x \in X$ admits an open neighbourhood $U$ such that $u' | f^{-1}(U)$ is of the
form $t' / s'$, where $t' \in \Gamma(f^{-1}(U), \mathcal{L}')$ and $s'$ is a regular section in $\Gamma(f^{-1}(U),
\mathcal{O}_{X'})$; the element $N(t') / N(s')$ (where $N(t')$ is the section of $\mathcal{L}$ defined in `(II, 6.5.3)`)
is then a meromorphic section of $\mathcal{L}$ over $U$ by virtue of what precedes, and it follows from the
multiplicative properties of the norm `(II, 6.5.3.1)` that this section depends only on $u' | f^{-1}(U)$ and not on its
expression in the form $t' / s'$; for the same reason, when $U$ varies, the meromorphic sections of $\mathcal{L}$ over
$U$ thus defined are the restrictions of one and the same meromorphic section of $\mathcal{L}$ over $X$, which one calls
the **norm** of $u'$ and denotes $N_{X'/X}(u')$ (or simply $N(u')$). The map thus defined

```text
  (21.5.3.1)             N_{X'/X} : Γ(X', 𝓜_{X'}(ℒ')) → Γ(X, 𝓜_X(N_{X'/X}(ℒ')))
```

extends the norm defined in `(II, 6.5.3)`; if $u'$ is a regular meromorphic section of $\mathcal{L}'$ over $X'$, it
follows at once from what precedes that $N(u')$ is a regular meromorphic section of $\mathcal{L}$ over $X$, for (with
the same notations) $N(t')$ is regular if $t'$ is. Finally, if $\mathcal{L}_{1}'$, $\mathcal{L}_{2}'$ are two invertible
$\mathcal{O}_{X'}$-Modules, $s_{1}'$ (resp. $s_{2}'$) a meromorphic section of $\mathcal{L}_{1}'$ (resp.
$\mathcal{L}_{2}'$) over $X'$, one has, by virtue of what precedes and of `(II, 6.5.3.1)`,

```text
  (21.5.3.2)             N(s_1' ⊗ s_2') = N(s_1') ⊗ N(s_2').
```

**(21.5.4).** Suppose still that $f$ verifies one of the hypotheses I), II) of `(21.5.3)`. If $(\mathcal{L}_{1}',
s_{1}')$, $(\mathcal{L}_{2}', s_{2}')$ are two pairs each formed of an invertible $\mathcal{O}_{X'}$-Module and a
regular meromorphic section of that Module over $X'$, which are moreover equivalent in the sense of `(21.2.10)`, then
the pairs $(N(\mathcal{L}_{1}'), N(s_{1}'))$ and $(N(\mathcal{L}_{2}'), N(s_{2}'))$ are also equivalent, for an
isomorphism of invertible $\mathcal{O}_{X'}$-Modules has for norm an isomorphism of their norms `(II, 6.5.3)`, and one
has seen above that $N_{X'/X}$ transforms sections of $\Gamma(X', \mathcal{O}^{\times}_{X'})$ into those of $\Gamma(X,
\mathcal{O}^{\times}_{X})$. One can therefore lay down the following definition:

<!-- original page 268 -->

**Definition (21.5.5).**

<!-- label: IV.21.5.5 -->

*Given a finite morphism $f : X' \to X$ of preschemes, verifying one of the conditions I), II) of `(21.5.3)`, one calls
**direct image** (or **norm**) of a divisor $D'$ on $X'$ by $f$, and denotes $f_{*}(D')$ (or $N_{X'/X}(D')$), the
divisor on $X$ which corresponds canonically `(21.2.11)` to the class of the pair $(N_{X'/X}(\mathcal{O}_{X'}(D')),
N_{X'/X}(s_{D'}))$.*

It follows at once from this definition, taking into account `(21.2.9.4)` and `(21.5.3.2)`, that if $D_{1}'$, $D_{2}'$,
$D'$ are divisors on $X'$, one has

```text
  (21.5.5.1)             f_*(D_1' + D_2') = f_*(D_1') + f_*(D_2')
```

and $D' \geq 0$ implies $f_{*}(D') \geq 0$; in other words, $D' \mapsto f_{*}(D')$ is an increasing homomorphism from
the ordered group $\operatorname{Div}(X')$ into the ordered group $\operatorname{Div}(X)$. Definition `(21.5.5)`
moreover shows at once that for every open $U$ of $X$, one has $f_{U,*}(D' | f^{-1}(U)) = f_{*}(D') | U$ ($f_{U}$ being
the restriction $f^{-1}(U) \to U$ of $f$), and the homomorphisms $f_{U,*}$, for variable $U$, therefore define a
homomorphism of sheaves of ordered groups

$$ (21.5.5.2) N_{X'/X} : f_{*}(\mathcal{D}iv_{X'}) \to \mathcal{D}iv_{X}. $$

Moreover, for every open $U$ of $X$, every invertible $\mathcal{O}_{X'}$-Module $\mathcal{L}'$ and every regular
meromorphic section $s'$ of $\mathcal{L}'$ over $f^{-1}(U)$, one has, according to the preceding definitions and
`(21.1.4)`,

$$ (21.5.5.3) div_{X}(N_{X'/X}(s')) = f_{*}(div_{X'}(s')). $$

**Proposition (21.5.6).**

<!-- label: IV.21.5.6 -->

*Let $f : X' \to X$ be a finite locally free morphism and suppose that $f_{*}(\mathcal{O}_{X'})$ is of constant rank
$n$. Then, for every divisor $D$ on $X$, $f_{*}(f^{*}(D))$ is defined and one has*

$$ (21.5.6.1) f_{*}(f^{*}(D)) = nD. $$

The first assertion follows from the fact that $f$ is flat `(21.4.5)`, and the second is an immediate consequence of the
definitions and of `(II, 6.5.3.2)`.

**Proposition (21.5.7).**

<!-- label: IV.21.5.7 -->

*Let $f : X' \to X$ be a finite morphism verifying one of the hypotheses I), II) of `(21.5.3)`, $f' : X'' \to X'$ a
finite locally free morphism of constant rank $n$. Then $f'' = f \circ f' : X'' \to X$ verifies the same hypothesis as
$f$, and for every divisor `D''` on `X''`, one has*

$$ (21.5.7.1) f''_{*}(D'') = f_{*}(f'_{*}(D'')). $$

In view of definition `(21.5.5)`, it suffices to prove the following result:

**Lemma (21.5.7.2).**

<!-- label: IV.21.5.7.2 -->

*Under the hypotheses of `(21.5.7)`, one has a functorial isomorphism*

$$ (21.5.7.3) N_{X''/X}(\mathcal{L}'') \xrightarrow{\sim} N_{X'/X}(N_{X''/X'}(\mathcal{L}'')) $$

*in the category of invertible $\mathcal{O}_{X}$-Modules.*

Indeed, taking into account the definition of the norm of a section of $\mathcal{L}''$ `(II, 6.5.3)` and definition
`(21.5.5)`, one will at once obtain `(21.5.7.1)`. To prove `(21.5.7.2)`, it suffices, in view of the definitions of
`(II, 6.5.2 and 6.5.3)`, to prove that for every section $s$ of $f''_{*}(\mathcal{O}_{X''}) =
f_{*}(f'_{*}(\mathcal{O}_{X''}))$ over an open $U$ of $X$, one has

$$ (21.5.7.4) N_{X''/X}(s) = N_{X'/X}(N_{X''/X'}(s)). $$

<!-- original page 269 -->

The question is obviously local on $X$, and one may therefore restrict to the case where $X = \operatorname{Spec}(A)$ is
affine; one then has $X' = \operatorname{Spec}(A')$ and $X'' = \operatorname{Spec}(A'')$, and one may suppose that `A''`
is a projective $A'$-module of rank $n$. When $f$ is locally free, one may suppose that $A'$ is a free $A$-module of
rank $m$, and then `A''` is a projective $A$-module of rank `mn`, and by restricting $X$ to a suitable open, one may
suppose that `A''` is a free $A$-module of rank `mn`; formula `(21.5.7.4)` then follows from the transitivity of the
norm (Bourbaki, _Alg._, chap. VIII, §12, n° 2, prop. 7). When $f$ verifies hypothesis II), $A$ is Noetherian reduced,
and if $R$ is its total ring of fractions, $A' \otimes_{A} R$ is a free $R$-module of rank $m$, hence $A'' \otimes_{A} R
= A'' \otimes_{A'} (A' \otimes_{A} R)$ is a projective $R$-module of rank `mn`, and since $R$ is then a semi-local ring,
this $R$-module is free; the proposition follows again from the transitivity of norms.

**Proposition (21.5.8).**

<!-- label: IV.21.5.8 -->

*Let $f : X' \to X$ be a finite morphism, $g : Y \to X$ a morphism; set $Y' = X' \times_{X} Y$, $f' = f_{(Y)} : Y' \to
Y$, $g' = g_{(X')} : Y' \to X'$. Suppose verified one of the following conditions:*

*(i) $f$ is locally free and $g$ is flat.*

*(ii) $f$ is locally free, $X$ and $Y$ are locally Noetherian, $g(Ass(\mathcal{O}_{Y})) \subset Ass(\mathcal{O}_{X})$
and $g'(Ass(\mathcal{O}_{Y'})) \subset Ass(\mathcal{O}_{X'})$.*

*(iii) $f$ verifies hypothesis II) of `(21.5.3)`, $Y$ is locally Noetherian, $Y$ and $Y'$ are reduced, and every
irreducible component of $Y$ (resp. $Y'$) dominates an irreducible component of $X$ (resp. $X'$).*

*Then, for every divisor $D'$ on $X'$, $g'^{*}(D')$ is defined, $g^{*}(f_{*}(D'))$ is defined, and one has*

$$ (21.5.8.1) g^{*}(f_{*}(D')) = f'_{*}(g'^{*}(D')). $$

Indeed, in all the cases, it follows from `(II, 6.5.8)` that one has a functorial isomorphism

$$ g^{*}(N_{X'/X}(\mathcal{L}')) \xrightarrow{\sim} N_{Y'/Y}(g'^{*}(\mathcal{L}')) $$

in the category of invertible $\mathcal{O}_{Y}$-Modules; moreover `(II, 6.5.4)`, if $s'$ is a section of
$\mathcal{O}_{X'}$ over $f^{-1}(U)$, `s''` the corresponding section of $\mathcal{O}_{Y'}$ over $g'^{-1}(f^{-1}(U))$
($U$ open of $X$), $N_{Y'/Y}(s'')$ is the section of $\mathcal{O}_{Y}$ over $g^{-1}(U)$ which corresponds to the section
$N_{X'/X}(s')$ of $\mathcal{O}_{X}$ over $U$. Formula `(21.5.8.1)` will therefore follow from the definitions if one
proves that $g'^{*}(D')$ and $g^{*}(D)$ are defined, whatever the divisors $D'$ on $X'$ and $D$ on $X$. As regards $D$,
this follows from the hypotheses made and from `(21.4.5)`. As regards $D'$, in case (i) $g'$ is flat, hence in all the
cases $g'^{*}(D')$ is defined by virtue of `(21.4.5)`.

### 21.6. `1`-codimensional cycle associated with a divisor

**(21.6.1).** Let $X$ be a locally Noetherian prescheme, and let $\mathfrak{J}(X)$ denote the set of irreducible closed
parts of $X$ (which is in bijective correspondence with $X$ by the map $x \mapsto \overline{x}$). In the product group
$\mathbb{Z}^{X}$, consider the subgroup $\mathfrak{z}(X)$ of elements $(n_{x})_{x \in X}$ such that the set of
$\overline{x} \in \mathfrak{J}(X)$ such that $n_{x} \neq 0$ (or, what amounts to the same,

<!-- original page 270 -->

the set of $x \in X$ such that $n_{x} \neq 0$) is locally finite. It is clear that $\mathfrak{z}(X)$ is a subgroup of
$\mathbb{Z}^{X}$ which contains the direct sum group $\mathbb{Z}^{(X)}$ (free group having $\mathfrak{J}(X)$ for basis),
and is equal to it when $X$ is Noetherian. The elements of $\mathfrak{z}(X)$ are called **cycles on $X$** and those of
$\mathfrak{J}(X)$ **prime cycles** (they do not in general form a basis of $\mathfrak{z}(X)$ when $X$ is not
Noetherian). One always considers $\mathfrak{z}(X)$ as *ordered* by the order induced on this subgroup by the product
order of $\mathbb{Z}^{X}$, and one denotes $\mathfrak{z}^{+}(X)$ the set of cycles $\geq 0$.

For every cycle $Z \in \mathfrak{z}(X)$, equal to $(n_{x})_{x \in X}$, one writes by abuse of language,

```text
                         Z = ∑_{x ∈ X} n_x · ‾{x};
```

one calls **multiplicity** of $Z$ at the point $x$ and one denotes by $mult_{x}(Z)$ the integer $n_{x}$ (positive or
negative). To say that $Z \geq 0$ means that $mult_{x}(Z) \geq 0$ for every $x \in X$. One calls **support** of $Z$ and
denotes by $Supp(Z)$ the union of the $\overline{x}$ such that $mult_{x}(Z) \neq 0$; by definition of $\mathfrak{z}(X)$,
this is a closed part of $X$, as union of a locally finite family of closed parts. One calls **dimension** (resp.
**codimension**) of $Z$ and denotes by $\dim(Z)$ (resp. $codim(Z)$) the dimension (resp. codimension in $X$) of
$Supp(Z)$.

**(21.6.2).** One says that a closed part $Y$ of $X$ is *purely of codimension $p$ (in $X$)* if each of its irreducible
components is of codimension $p$ in $X$. One says that a cycle is *purely of codimension $p$*, or (by abuse of language)
is a **$p$-codimensional cycle**, if its support is purely of codimension $p$. One denotes by $X^{(p)}$ the set of $x
\in X$ such that $codim(\overline{x}, X) = p$, or, what amounts to the same `(5.1.2.1)`, $\dim(\mathcal{O}_{X,x}) = p$:
the cycles purely of codimension $p$ form a subgroup $\mathfrak{z}^{p}(X)$ of $\mathfrak{z}(X)$, isomorphic to the
subgroup of $\mathbb{Z}^{X^{(p)}}$ formed of the $(n_{x})_{x \in X^{(p)}}$ such that the set of $\overline{x}$ (or the
set of $x$) for which $n_{x} \neq 0$ is locally finite; this subgroup contains the free group $\mathbb{Z}^{(X^{(p)})}$
and is identical to it when $X$ is Noetherian. One denotes by $\mathfrak{z}^{p+}(X)$ the set of elements $\geq 0$ of
$\mathfrak{z}^{p}(X)$. It is clear that the ordered group $\mathfrak{z}(X)$ contains the direct sum of the ordered
subgroups $\mathfrak{z}^{p}(X)$, and is identical to this direct sum when $X$ is Noetherian; in this last case, one
considers $\mathfrak{z}(X)$ as *graded* by the $\mathfrak{z}^{p}(X)$ for $p \in \mathbb{N}$.

**(21.6.3).** Let $Z = \sum_{x \in X} n_{x} \cdot \overline{x}$ be a cycle on $X$, $U$ an open of $X$; one calls
**restriction of $Z$ to $U$** and one denotes by $Z | U$ the cycle $\sum_{x \in U} n_{x} \cdot (U \cap \overline{x})$ on
$U$; one has $Supp(Z | U) = Supp(Z) \cap U$. It is clear that $Z \mapsto Z | U$ is a homomorphism of ordered groups from
$\mathfrak{z}(X)$ into $\mathfrak{z}(U)$ (resp. from $\mathfrak{z}^{p}(X)$ into $\mathfrak{z}^{p}(U)$), and that if $V$
is an open contained in $U$, one has $Z | V = (Z | U) | V$; the map $U \mapsto \mathfrak{z}(U)$ (resp. $U \mapsto
\mathfrak{z}^{p}(U)$) is therefore a presheaf on $X$ of ordered commutative groups. In fact this presheaf is a *sheaf*,
direct sum of the sheaves $(j_{x})_{*}(\mathbb{Z}_{\overline{x}})$, where $x$ runs through $X$ (resp. $X^{(p)}$) and for
each $x \in X$, $j_{x}$ is the canonical injection $\overline{x} \to X$ and $\mathbb{Z}_{\overline{x}}$ is the simple
sheaf associated with the constant sheaf $\mathbb{Z}$ on the space $\overline{x}$: this follows at once from the
description of the sections of a direct sum of sheaves of commutative groups (G, II, 2.7). One denotes this sheaf
$\mathfrak{z}_{X}$ (resp. $\mathfrak{z}^{p}_{X}$). One denotes by $\mathfrak{z}^{+}_{X}$ (resp. $\mathfrak{z}^{p+}_{X}$)
the subsheaf

<!-- original page 271 -->

of monoids $U \mapsto \mathfrak{z}^{+}(U)$ (resp. $U \mapsto \mathfrak{z}^{p+}(U)$) of $\mathfrak{z}_{X}$ (resp.
$\mathfrak{z}^{p}_{X}$). The sheaf $\mathfrak{z}_{X}$ is evidently the direct sum of the sheaves $\mathfrak{z}^{p}_{X}$.

Note finally that the sheaves $\mathfrak{z}^{p}_{X}$ (hence also $\mathfrak{z}_{X}$) are *flasque*. Suppose indeed given
a section $Z$ of $\mathfrak{z}^{p}_{X}$ over an open $U$, so that the set $S$ of $x \in U$ such that $mult_{x}(Z) \neq
0$ is locally finite in $U$; this set is also locally finite in $X$, for, for every $\xi \in X$ and every Noetherian
open neighbourhood $V$ of $\xi$, $U \cap V$ is Noetherian, hence contains only a finite number of points of $S$. One
therefore defines a section $Z'$ of $\mathfrak{z}^{p}_{X}$ over $X$ by setting $Z' = \sum_{x \in U} mult_{x}(Z) \cdot
\overline{x}$; and since the closure of $x$ in $U$ is $\overline{x} \cap U$, one has indeed $Z' | U = Z$, whence our
assertion.

**(21.6.4).** We propose to define a canonical homomorphism

$$ (21.6.4.1) c : \mathcal{D}iv_{X} \to \mathfrak{z}^{1}_{X} $$

of sheaves of commutative groups. It evidently suffices to define a homomorphism from $\mathcal{M}^{\times}_{X}$ into
$\mathfrak{z}^{1}_{X}$, which vanishes on $\mathcal{O}^{\times}_{X}$ `(21.1.2)`; now, by definition,
$\mathcal{M}^{\times}_{X}$ is the symmetrization of the sheaf of monoids $\mathcal{S}(\mathcal{O}_{X}) = \mathcal{O}_{X}
\cap \mathcal{M}^{\times}_{X}$, and a homomorphism $\mathcal{M}^{\times}_{X} \to \mathfrak{z}^{1}_{X}$ is uniquely
determined by the data of its restriction $\mathcal{S}(\mathcal{O}_{X}) \to \mathfrak{z}^{1}_{X}$, which is a
homomorphism of sheaf of monoids subject to the sole condition of being zero on $\mathcal{O}^{\times}_{X}$; it amounts
to the same to say that to define $c$, it suffices to define a homomorphism of sheaf of monoids

$$ (21.6.4.2) c : \mathcal{D}iv^{+}_{X} \to \mathfrak{z}^{1+}_{X}. $$

**(21.6.5).** Now, one has seen that to every positive divisor $D$ on $X$ corresponds the closed sub-prescheme $Y(D)$ of
$X$, defined by the Ideal $\mathcal{O}_{X}(D) \subset \mathcal{O}_{X}$, and which is regularly immersed and of
codimension `1`. At each of the maximal points $x$ of $Y(D)$, one therefore has `((19.1.4)` and `(5.1.2))`
$codim(\overline{x}, X) = \dim(\mathcal{O}_{X,x}) = 1$, in other words $x \in X^{(1)}$; moreover the set of these
maximal points is locally finite in $X$ `(3.1.6)`, and $\mathcal{O}_{Y(D),x}$ is an Artinian ring. At every point $x \in
X^{(1)}$ which is not a maximal point of $Y(D)$, one necessarily has $x \notin Y(D)$, hence $\mathcal{O}_{Y(D),x} = 0$.
Set

```text
  (21.6.5.1)             cyc(D) = ∑_{x ∈ X^{(1)}} long(𝒪_{Y(D),x}) · ‾{x}
```

which is therefore an element of $\mathfrak{z}^{1}(X)$.

**Proposition (21.6.6).**

<!-- label: IV.21.6.6 -->

*The map $D \mapsto cyc(D)$ is a homomorphism from the monoid $\operatorname{Div}^{+}(X)$ into $\mathfrak{z}^{1}(X)$.*

Everything reduces to seeing that for two positive divisors $D$, $D'$, one has

```text
                         cyc(D + D') = cyc(D) + cyc(D').
```

Now, one has `(21.2.5)` $\mathcal{O}_{X}(D + D') = \mathcal{O}_{X}(D) \mathcal{O}_{X}(D')$; everything reduces to seeing
that if $x \in X^{(1)}$, if one sets $A = \mathcal{O}_{X,x}$, and if $t$ and $t'$ are two regular elements of $A$, one
has `long(A / tt'A) = long(A / tA) + long(A / t'A)`; but since $t$ is regular, $tA / tt'A$ is isomorphic to $A / t'A$,
whence the proposition at once.

<!-- original page 272 -->

It follows at once from the definitions that for every open $U \subset X$, one has

```text
                         Y(D | U) = Y(D) ∩ U,
```

hence $cyc(D | U) = cyc(D) | U$, and the homomorphisms $cyc : \operatorname{Div}^{+}(U) \to \mathfrak{z}^{1}(U)$
therefore define a homomorphism of sheaves of monoids `(21.6.4.2)`, whence the sought homomorphism `(21.6.4.1)` of
sheaves of groups.

One has `Supp(cyc(D)) ⊂ Supp(D)` for every divisor $D$ and

```text
  (21.6.6.2)             Supp(cyc(D)) = Supp(D)     when D ≥ 0;
```

one has indeed already seen the second relation `(21.2.12)`; when $D$ is arbitrary, the relation $D_{x} = 0$ entails the
existence of an open neighbourhood $U$ of $x$ such that $D | U = 0$, whence $cyc(D) | U = 0$, which proves our
assertion.

**(21.6.7).** The homomorphism `(21.6.4.1)` gives, by passage to the groups of sections over $X$, an increasing
homomorphism of ordered groups $\operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$, which we shall again denote $D \mapsto
cyc(D)$; the number $mult_{x}(cyc(D))$ for $x \in X^{(1)}$ is also denoted $mult_{x}(D)$ or $mult_{\overline{x}}(D)$ and
is called **multiplicity of the divisor $D$ at the point $x$**, or **multiplicity of the prime cycle $\overline{x}$ in
$D$**; this is a positive or negative integer, equal as one has seen to $long(\mathcal{O}_{Y(D),x})$ when $D$ is a
positive divisor; one therefore has by definition

```text
  (21.6.7.1)             cyc(D) = ∑_{x ∈ X^{(1)}} mult_x(D) · ‾{x},
```

and by virtue of the fact that $D \mapsto cyc(D)$ is a homomorphism, one has

```text
  (21.6.7.2)             mult_x(−D) = −mult_x(D),    mult_x(D + D') = mult_x(D) + mult_x(D')
```

for any two divisors $D$, $D'$.

For every regular meromorphic function $f$ on $X$, one sets in particular, for $x \in X^{(1)}$,

$$ (21.6.7.3) \omega_{x}(f) = mult_{x}(div(f)) $$

and one says that $\omega_{x}(f)$ (positive or negative integer) is the **order of $f$ at the point $x \in X^{(1)}$**.
If $f \in \mathcal{O}_{X,x}$ (a regular element of this local ring by hypothesis), one therefore has

```text
  (21.6.7.4)             ω_x(f) = long(𝒪_{X,x} / f 𝒪_{X,x});
```

for two regular meromorphic functions $f$, $f'$ on $X$, one has

```text
  (21.6.7.5)             ω_x(ff') = ω_x(f) + ω_x(f'),    ω_x(f⁻¹) = −ω_x(f)
```

for every $x \in X^{(1)}$. The `1`-codimensional cycles

```text
                         Z^+(f) = ∑_{x ∈ X^{(1)}, ω_x(f) > 0} ω_x(f) · ‾{x},
                         Z^−(f) = ∑_{x ∈ X^{(1)}, ω_x(f) < 0} (−ω_x(f)) · ‾{x}
```

are called respectively the **cycle of zeros** and the **cycle of poles** (or **polar cycle**) of $f$, and one has
obviously $cyc(div(f)) = Z^{+}(f) - Z^{-}(f)$. The `1`-codimensional cycles of the form $cyc(div(f))$ are called
**principal** (or *linearly equivalent to `0`*) and form a subgroup $\mathfrak{z}^{1}_{princ}(X)$ of
$\mathfrak{z}^{1}(X)$. The sections over $X$ of the image $c(\mathcal{D}iv_{X}) \subset \mathfrak{z}^{1}_{X}$ are

<!-- original page 273 -->

called **locally principal cycles**; such a cycle $Z$ is therefore characterized by the fact that, for every $y \in X$,
there is an open neighbourhood $U$ of $y$ in $X$ and a regular meromorphic function $f$ on $U$ such that $Z | U =
\sum_{x \in U \cap X^{(1)}} \omega_{x}(f) \cdot (\overline{x} \cap U)$. If $Z = \sum_{x \in X^{(1)}} n_{x} \cdot
\overline{x}$, it amounts to the same to say that, for every $y \in X$, if one sets $T_{y} =
\operatorname{Spec}(\mathcal{O}_{X,y})$ and $Z_{y} = \sum_{x \in X^{(1)} \cap T_{y}} n_{x} \cdot (\overline{x} \cap
T_{y})$, $Z_{y}$ is principal; in other words there exists a regular meromorphic function $g$ on $T_{y}$ such that
$Z_{y} = cyc(div(g))$. This follows at once indeed from the preceding definition and from `(20.3.7)`, which establishes
a bijective correspondence between the regular meromorphic functions on $T_{y}$ and the germs of regular meromorphic
functions on the open neighbourhoods of $y$ in $X$ when $X$ is locally Noetherian. One again expresses the fact that
$Z_{y}$ is principal by saying that *$Z$ is principal at the point $y$*. The set of points where $Z$ is principal is
evidently open, by virtue of what precedes.

One deduces from the canonical homomorphism $cyc : \operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$ a canonical
homomorphism `Div(X) / Div.princ(X) → 𝔷^1(X) / 𝔷_{princ}^1(X)`, by virtue of the definition of
$\mathfrak{z}^{1}_{princ}(X)$. One says that the group $\mathfrak{z}^{1}(X) / \mathfrak{z}^{1}_{princ}(X)$ is the
**group of classes of `1`-codimensional cycles on $X$** and one denotes it $Cl(X)$. Two elements of
$\mathfrak{z}^{1}(X)$ having the same image in $Cl(X)$ are called **linearly equivalent**.

**(21.6.8).** Consider in particular the case where $X = \operatorname{Spec}(A)$, where $A$ is an integrally closed
Noetherian integral domain. Then $X^{(1)}$ is the set of prime ideals of height `1` of $A$, and $\mathfrak{z}^{1}(X)$ is
therefore identified with the group of divisors (in the sense of N. Bourbaki) of the Krull ring $A$ (Bourbaki, _Alg.
comm._, chap. VII, §1, n° 3, cor. of th. 2 and n° 6, th. 3).

Since on the other hand, the regular meromorphic functions on $X$ are then identified with the elements $\neq 0$ of the
fraction field $K$ of $A$, the map $f \mapsto cyc(div(f))$ from $M(X)^{\times}$ into $\mathfrak{z}^{1}(X)$ is identified
with the map denoted $f \mapsto div(f)$ in Bourbaki (_loc. cit._, §1, n° 1); $\mathfrak{z}^{1}_{princ}(X)$ is therefore
identified with the group of principal divisors of $A$ in the sense of Bourbaki, and $Cl(X)$ with the group of divisor
classes of $A$ in the sense of Bourbaki (_loc. cit._, §1, n° 2 and n° 10).

**Theorem (21.6.9).**

<!-- label: IV.21.6.9 -->

*Let $X$ be a locally Noetherian normal prescheme.*

*(i) The canonical homomorphism $cyc : \operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$ is injective and its image is
formed of the locally principal cycles.*

*(ii) The following conditions are equivalent:*

*a) The homomorphism $cyc : \operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$ is bijective.*

*b) Every `1`-codimensional cycle is locally principal.*

*c) For every $x \in X$, the local ring $\mathcal{O}_{X,x}$ is factorial.*

*(One then says that $X$ is a **locally factorial prescheme**.)*

(i) It suffices to prove that

$$ (21.6.9.1) cyc^{-1}(\mathfrak{z}^{1+}(X)) = \operatorname{Div}^{+}(X), $$

since one has $\operatorname{Div}^{+}(X) \cap (-\operatorname{Div}^{+}(X)) = 0$ and $\mathfrak{z}^{1+}(X) \cap
(-\mathfrak{z}^{1+}(X)) = 0$. One is therefore reduced to proving that if $D$ is a divisor on $X$ such that $mult_{x}(D)
\geq 0$ for every $x \in X^{(1)}$, one has $D \geq 0$. Now, for every $x \notin X^{(1)}$, the local ring
$\mathcal{O}_{X,x}$ is integral and integrally closed, and

<!-- original page 274 -->

of dimension `0` or $\geq 2$, hence one has $prof(\mathcal{O}_{X,x}) = 0$ or $prof(\mathcal{O}_{X,x}) \geq 2$
`(0, 16.5.1)`. On the other hand, at the points $x \in X^{(1)}$, the ring $\mathcal{O}_{X,x}$ is a discrete valuation
ring `(II, 7.1.6)`, hence $prof(\mathcal{O}_{X,x}) = 1$ `(0, 16.5.1)`; the only points of $X$ such that
$prof(\mathcal{O}_{X,x}) \leq 1$ are therefore the points of $X^{(1)}$, and the conclusion follows from `(21.1.8)`.

(ii) The equivalence of a) and b) is clear by virtue of (i). According to the characterization of locally principal
cycles given in `(21.6.7)`, and the relation between `1`-codimensional cycles on $\operatorname{Spec}(A)$ and divisors
(in the sense of Bourbaki) of the ring $A$ when $A$ is an integrally closed Noetherian ring `(21.6.8)`, condition b) is
equivalent to saying that for every $x \in X$, every divisor of the ring $\mathcal{O}_{X,x}$ is principal, in other
words that the ring $\mathcal{O}_{X,x}$ is factorial (Bourbaki, _Alg. comm._, chap. VII, §3, n° 1), whence the
equivalence of b) and c).

**(21.6.9.2).** When $A$ is a factorial Noetherian ring, it is clear that $X = \operatorname{Spec}(A)$ is locally
factorial (Bourbaki, _Alg. comm._, chap. VII, §3, n° 4, prop. 3). If, in this case, one writes an element $f \neq 0$ of
the fraction field $K$ of $A$ in the form $r/s$, where $r$ and $s$ are two coprime elements of $A$, whose divisors are
well determined (_loc. cit._, §3, n° 3), these divisors are identified respectively with the *cycle of zeros* and the
*cycle of poles* of $f$ `(21.6.7)`.

**Corollary (21.6.10).**

<!-- label: IV.21.6.10 -->

*Let $X$ be a locally Noetherian normal prescheme.*

*(i) There exists a canonical injective homomorphism*

$$ (21.6.10.1) \operatorname{Pic}(X) \to Cl(X). $$

*(ii) If $X$ is locally factorial, the homomorphism `(21.6.10.1)` is bijective, and conversely.*

One has seen `(21.6.7)` that the image of $\operatorname{Div}.princ(X)$ by the homomorphism $cyc : \operatorname{Div}(X)
\to \mathfrak{z}^{1}(X)$ is $\mathfrak{z}^{1}_{princ}(X)$; one therefore deduces from `(21.6.9)` that the homomorphism
`Div(X) / Div.princ(X) → 𝔷^1(X) / 𝔷_{princ}^1(X) = Cl(X)` deduced from `cyc` is injective, and that it is bijective if
and only if $X$ is locally factorial. The conclusion therefore follows from the fact that, when $X$ is locally
Noetherian and reduced, the canonical homomorphism `Div(X) / Div.princ(X) → Pic(X)` `(21.3.3.1)` is bijective
`(21.3.4, (ii))`.

**Corollary (21.6.11).**

<!-- label: IV.21.6.11 -->

*Let $X$ be a locally Noetherian and locally factorial prescheme. Then the sheaf $\mathcal{D}iv_{X}$ is flasque, and for
every open $U$ of $X$, the canonical homomorphism $\operatorname{Pic}(X) \to \operatorname{Pic}(U)$ is surjective.*

Taking into account `(21.6.9, (ii))`, the first assertion is equivalent to saying that the sheaf $\mathfrak{z}^{1}_{X}$
is flasque, which has been seen above `(21.6.3)`. For every open $U$ of $X$, the canonical homomorphism
$\mathfrak{z}^{1}(X) \to \mathfrak{z}^{1}(U)$ is therefore surjective; since by virtue of `(21.6.10)`, the homomorphism
$\operatorname{Pic}(X) \to \operatorname{Pic}(U)$ is canonically identified with $\mathfrak{z}^{1}(X) /
\mathfrak{z}^{1}_{princ}(X) \to \mathfrak{z}^{1}(U) / \mathfrak{z}^{1}_{princ}(U)$, it is also surjective.

**Proposition (21.6.12).**

<!-- label: IV.21.6.12 -->

*Let $X$ be a Noetherian reduced prescheme. Let $(U_{\lambda})_{\lambda \in L}$ be a decreasing filtered family of opens
of $X$ verifying the following conditions:*

*1° If $Y_{\lambda} = X - U_{\lambda}$, one has $codim(Y_{\lambda}, X) \geq 2$ for every $\lambda \in L$.*

*2° For every $x \in \bigcap_{\lambda \in L} U_{\lambda}$, the ring $\mathcal{O}_{X,x}$ is factorial.*

<!-- original page 275 -->

*Then there exist canonical isomorphisms*

```text
  (21.6.12.1)            lim Div(U_λ) ⥲ 𝔷^1(X),    lim Pic(U_λ) ⥲ Cl(X)
```

*such that, for every open $V$ of $X$, the diagrams*

```text
                         lim Div(U_λ) ─⥲─ 𝔷^1(X)
                              │             │
  (21.6.12.2)
                              ↓             ↓
                         lim Div(U_λ ∩ V) ─⥲ 𝔷^1(V)

                         lim Pic(U_λ) ─⥲─ Cl(X)
                              │             │
                              ↓             ↓
                         lim Pic(U_λ ∩ V) ─⥲ Cl(V)
```

*are commutative.*

Hypothesis 1° on $U_{\lambda}$ implies that for every $\lambda \in L$, one has $X^{(1)} \subset U_{\lambda}$
`(5.1.3.1)`; hence the restriction homomorphism $\mathfrak{z}^{1}(X) \to \mathfrak{z}^{1}(U_{\lambda})$ is bijective and
consequently one has a canonical isomorphism $\lim \mathfrak{z}^{1}(U_{\lambda}) \xrightarrow{\sim}
\mathfrak{z}^{1}(X)$. The canonical homomorphisms $cyc : \operatorname{Div}(U_{\lambda}) \to
\mathfrak{z}^{1}(U_{\lambda})$ define therefore, by passage to the inductive limit, the first of the canonical
homomorphisms `(21.6.12.1)`, and the second one is deduced from it by passage to the quotients. Moreover, it follows
from condition 1° that the $U_{\lambda}$ are dense in $X$, hence schematically dense since $X$ is reduced `(11.10.4)`,
and consequently every meromorphic function on $X$ is entirely determined by its restriction to each $U_{\lambda}$; one
deduces at once from this that in the isomorphism $\mathfrak{z}^{1}(X) \xrightarrow{\sim}
\mathfrak{z}^{1}(U_{\lambda})$, the image of $\mathfrak{z}^{1}_{princ}(X)$ is $\mathfrak{z}^{1}_{princ}(U_{\lambda})$,
hence one also has a canonical isomorphism $\lim Cl(U_{\lambda}) \xrightarrow{\sim} Cl(X)$. The second of the canonical
homomorphisms `(21.6.12.1)` will therefore be an isomorphism if the first is, and it remains to prove this latter point,
the commutativity of the diagrams `(21.6.12.2)` being trivial.

Let us show first that the homomorphism $\lim \operatorname{Div}(U_{\lambda}) \to \mathfrak{z}^{1}(X)$ is injective. Set
$T = \bigcap_{\lambda} U_{\lambda}$, and note that the $U_{\lambda}$ form a fundamental system of neighbourhoods of $T$.
Indeed, for every open $V \supset T$, $X - V$ is a closed subspace of $X$, hence a Noetherian space every closed
irreducible part of which admits a generic point; since the sets $(X - V) \cap (X - U_{\lambda})$ are closed in $X - V$,
form an increasing filtered family and have for union $X - V$, our assertion follows from $(0_{III}, 9.2.4)$. This being
so, it is a matter of seeing that if $D \in \operatorname{Div}(U_{\lambda})$ is such that $cyc(D) = 0$ in
$\mathfrak{z}^{1}(U_{\lambda})$, then there exists $\mu \geq \lambda$ such that $D | U_{\mu} = 0$. By virtue of what
precedes, it will suffice to see that for every $x \in T$, one has $D_{x} = 0$; indeed, there will then be a
neighbourhood $W(x)$ of $x$ in $X$ such that $D | W(x) = 0$, and the union of the $W(x)$ for $x \in T$ contains some
$U_{\mu}$. Taking into account `(21.4.6)`, one is therefore reduced to the case where $X =
\operatorname{Spec}(\mathcal{O}_{X,x})$; but by hypothesis $\mathcal{O}_{X,x}$ is factorial, hence integral and
integrally closed, and $\operatorname{Spec}(\mathcal{O}_{X,x})$ is then normal; hence the conclusion follows from
`(21.6.9, (i))`.

To prove that the homomorphism $\lim \operatorname{Div}(U_{\lambda}) \to \mathfrak{z}^{1}(X)$ is bijective, it suffices
to prove similarly that for every $Z \in \mathfrak{z}^{1}(X)$ and every $x \in T$, there is a neighbourhood $W(x)$

<!-- original page 276 -->

of $x$ in $X$ and a divisor $D_{x}$ on $W(x)$ such that $cyc(D_{x}) = Z | W(x)$. Indeed, one will then be able to cover
the quasi-compact set $T$ by a finite number of $W(x_{i})$, and by virtue of the first part of the demonstration, since
the pairs $(i, j)$ are finite in number, there will exist an index $\lambda$ such that in each of the $W(x_{i}) \cap
W(x_{j}) \cap U_{\lambda}$, the restrictions of $D_{x_{i}}$ and $D_{x_{j}}$ coincide; since one may suppose moreover
that $U_{\lambda}$ is contained in the union of the $W(x_{i})$, one sees that the restrictions $D_{x_{i}} | (W(x_{i})
\cap U_{\lambda})$ are the restrictions of one and the same divisor $D \in \operatorname{Div}(U_{\lambda})$ which will
be such that $cyc(D) = Z | U_{\lambda}$. One is therefore reduced again to the case where $X =
\operatorname{Spec}(\mathcal{O}_{X,x})$ with $x \in T$; but since $\mathcal{O}_{X,x}$ is factorial, so are its
localizations (Bourbaki, _Alg. comm._, chap. VII, §3, n° 4, prop. 3), and it suffices to apply `(21.6.9, (ii))`.

**Corollary (21.6.13).**

<!-- label: IV.21.6.13 -->

*Let $A$ be an integrally closed Noetherian integral local ring of dimension $\geq 2$. Set $X = \operatorname{Spec}(A)$,
and let $a$ be the closed point of $X$, $U = X - {a}$. For $A$ to be factorial, it is necessary and sufficient that $U$
be locally factorial and that $\operatorname{Pic}(U) = 0$.*

Indeed, to say that $A$ is factorial is equivalent to saying that $Cl(X) = 0$ (Bourbaki, _Alg. comm._, chap. VII, §1, n°
4, cor. of th. 2 and §3, n° 2, th. 1); it therefore suffices to use the existence of the second isomorphism
`(21.6.12.1)`, taking the family $(U_{\lambda})$ restricted to the single open $U$.

**Corollary (21.6.14).**

<!-- label: IV.21.6.14 -->

*Let $A$ be a Noetherian local ring of dimension $\geq 2$, $X = \operatorname{Spec}(A)$, $a$ the closed point of $X$, $U
= X - {a}$. The following conditions are equivalent:*

*a) $A$ is factorial.*

*b) $\operatorname{Pic}(U) = 0$ and $prof(A) \geq 2$ (conditions which we shall later (21.13) express by saying that the
ring $A$ is **parafactorial**), and $U$ is locally factorial.*

It is clear that if $A$ is factorial, it is normal, hence $prof(A) \geq 2$ since $\dim(A) \geq 2$ `(0, 16.5.1)`, and
`(21.6.13)` shows that a) implies b). Conversely, if b) is verified, it suffices to see that $A$ is integrally closed to
conclude by `(21.6.13)` that b) entails a). By virtue of Serre's criterion `(5.8.6)`, it suffices to verify for $X$ the
conditions `(R_1)` and `(S_2)`. Now, $U$ being locally factorial verifies these conditions, and the hypothesis $prof(A)
\geq 2$ entails that $X$ verifies them also.

### 21.7. Interpretation of positive `1`-codimensional cycles in terms of subpreschemes

**(21.7.1).** Let $X$ be a locally Noetherian prescheme, $C = \sum_{x \in X^{(1)}} n_{x} \cdot \overline{x}$ a positive
`1`-codimensional cycle (so that one has $n_{x} \geq 0$ for every $x \in X^{(1)}$, and $n_{x} = 0$ except on a locally
finite set of points). Denote by $Y(C)$ the closed sub-prescheme of $X$, **closed image** `(I, 9.5.3` and `9.5.1)` of
the sum prescheme $Y'(C) = \coprod_{x \in X^{(1)}} \operatorname{Spec}(\mathcal{O}_{X,x} / \mathfrak{m}^{n_{x}}_{x})$
under the canonical morphism, and by $\mathcal{J}_{X}(C)$ (or $\mathcal{J}(C)$) the Ideal of $\mathcal{O}_{X}$ defining
$Y(C)$.

**Proposition (21.7.2).**

<!-- label: IV.21.7.2 -->

*Let $X$ be a locally Noetherian prescheme verifying condition `(R_1)` `(5.8.2)`. For a closed sub-prescheme $Y$ of $X$
to be of the form $Y(C)$, where $C$ is a positive `1`-codimensional cycle, it is necessary and sufficient that it verify
the two following conditions:*

*(i) $Y$ is purely of codimension `1`.*

<!-- original page 277 -->

*(ii) $Y$ verifies condition `(S_1)`, in other words `(5.7.5)` has no immersed associated prime cycle.*

*One then has*

$$ (21.7.2.1) mult_{x}(C) = long(\mathcal{O}_{Y,x}). $$

*The map $C \mapsto Y(C)$ is a bijection of $\mathfrak{z}^{1+}(X)$ onto the set of closed sub-preschemes of $X$
verifying conditions (i) and (ii).*

The conditions are necessary (without assuming that $X$ verifies `(R_1)`). Indeed, the question being local on $X$, one
may suppose that $X = \operatorname{Spec}(A)$, where $A$ is a Noetherian ring; one then has $Y(C) =
\operatorname{Spec}(A / \mathfrak{J})$, where $\mathfrak{J}$ is by definition `(I, 9.5.1)` the kernel of the canonical
homomorphism $A \to \oplus A_{\mathfrak{p}_{i}} / \mathfrak{p}^{n_{i}}_{i} A_{\mathfrak{p}_{i}}$, where the
$\mathfrak{p}_{i}$ are the prime ideals corresponding to the points $x_{i} \in X^{(1)}$ for which $n_{x_{i}} \neq 0$,
and where one has set $n_{i} = n_{x_{i}}$. The inverse image $\mathfrak{q}_{i}$ of $\mathfrak{p}^{n_{i}}_{i}
A_{\mathfrak{p}_{i}}$ in $A$ is a $\mathfrak{p}_{i}$-primary ideal, and one has $\mathfrak{J} = \bigcap
\mathfrak{q}_{i}$. Moreover, since the $x \in X^{(1)}$ are such that $\overline{x}$ is of codimension `1`, no point of
$X^{(1)}$ can be adherent to another point of $X^{(1)}$. Hence the $\mathfrak{p}_{i}$ are the minimal prime ideals of $A
/ \mathfrak{J}$ and the set of $\mathfrak{p}_{i}$ is equal to $Ass(A / \mathfrak{J})$, which proves conditions (i) and
(ii).

The conditions are sufficient. Denoting by $\mathcal{J}$ the Ideal of $\mathcal{O}_{X}$ defining $Y$, hypothesis (ii)
implies that $Ass(\mathcal{O}_{X} / \mathcal{J})$ is identical to the set $F$ of maximal points of $Y$, and hypothesis
(i) implies that $F$ is contained in $X^{(1)}$; hence `(3.2.6)` $\mathcal{O}_{X} / \mathcal{J}$ is identified with a
sub-$\mathcal{O}_{X}$-Module of $\oplus_{x \in F} \mathcal{E}(x)$, where for each $x \in F$, $\mathcal{E}(x)$ is an
irredundant $\mathcal{O}_{X}$-Module such that $Ass(\mathcal{E}(x)) = {x}$. Now, since $X$ verifies `(R_1)`, for each $x
\in F$, $\mathcal{O}_{X,x}$ is a discrete valuation ring, and consequently the primary ideals $\neq 0$ of this ring are
the powers $\mathfrak{m}^{k}_{x}$ of the maximal ideal; supposing still that $X = \operatorname{Spec}(A)$, one concludes
that $\mathcal{J} = \mathfrak{J}$, where $\mathfrak{J} = \bigcap \mathfrak{q}_{i}$, the $\mathfrak{q}_{i}$ being the
inverse images in $A$ of ideals $\mathfrak{p}^{n_{i}}_{i} A_{\mathfrak{p}_{i}}$, where the $\mathfrak{p}_{i}$ correspond
to the points of $F$. One sees therefore well that $Y$ is of the form $Y(C)$.

**Corollary (21.7.3).**

<!-- label: IV.21.7.3 -->

*Let $X$ be a locally Noetherian prescheme. For every positive divisor $D$ on $X$ such that $X$ verifies `(R_1)` at the
maximal points of the closed sub-prescheme $Y(D)$ `(21.2.12)`, $Y(D)$ majorizes the closed sub-prescheme $Y(cyc(D))$
`(21.7.1)`, and has the same underlying space; for these two sub-preschemes to be equal, it is necessary and sufficient
that $Y(D)$ verify condition `(S_1)`, or also that, for every $x \in Y(D)$ distinct from a maximal point of $Y(D)$, one
have $prof(\mathcal{O}_{X,x}) \geq 2$ (condition always verified when $X$ is normal).*

Indeed, the question being local, one may always suppose that $\mathcal{O}_{X}(D) = \mathcal{O}_{X} \cdot t$, $t$ being
a regular section of $\mathcal{O}_{X}$ over $X$; at every maximal point $x$ of $Y(D)$, necessarily belonging to
$X^{(1)}$, $\mathcal{O}_{X,x}$ is by hypothesis a discrete valuation ring, hence $\mathcal{O}_{X,x} t =
\mathfrak{m}^{n_{x}}_{x}$ for $n_{x} = mult_{x}(D)$. One may suppose $X = \operatorname{Spec}(A)$, and then, if
$\mathcal{J}_{X}(cyc(D)) = \mathfrak{J}$, $\mathcal{O}_{X}(D) = \mathfrak{J}'$, it follows from what precedes and from
`(21.7.1)` that $\mathfrak{J}$ and $\mathfrak{J}'$ have the same non-immersed primary ideals; hence $\mathfrak{J}'
\subset \mathfrak{J}$, since $\mathfrak{J}$ is the intersection

<!-- original page 278 -->

of these primary ideals `(21.7.2)`. This proves that $Y(D)$ majorizes $Y(cyc(D))$ and that these two sub-preschemes are
equal if and only if $Y(D)$ has no immersed associated prime cycle (in other words verifies `(S_1)`). Since for every $x
\in Y(D)$, there is by hypothesis an open neighbourhood $U$ of $x$ in $X$ and a regular element $t \in \Gamma(U,
\mathcal{O}_{X})$ such that $\mathcal{O}_{Y(D)} | (U \cap Y(D))$ is the restriction to $Y(D) \cap U$ of $\mathcal{O}_{U}
/ t \mathcal{O}_{U}$, to say that $Y(D)$ verifies `(S_1)` also means that at every non-maximal point $x \in Y(D)$, one
has $prof(\mathcal{O}_{X,x} / t \mathcal{O}_{X,x}) \geq 1$, that is to say `(0, 16.4.6)` $prof(\mathcal{O}_{X,x}) \geq
2$. The assertion concerning the case where $X$ is normal is then immediate since $X$ verifies `(S_2)` and at the
non-maximal points $x$ of $Y(D)$ one has $\dim(\mathcal{O}_{X,x}) \geq 2$ `(0, 16.3.4)`.

**(21.7.3.1).** One therefore sees that when $X$ is normal, $\operatorname{Div}^{+}(X)$ is canonically identified with
the set of closed sub-preschemes $Y$ of $X$ verifying conditions (i) and (ii) of `(21.7.2)` and regularly immersed in
$X$.

**Proposition (21.7.4).**

<!-- label: IV.21.7.4 -->

*Let $X$ be a locally Noetherian prescheme, reduced at each of its isolated points. The following conditions are
equivalent:*

*a) The canonical homomorphism $c : \mathcal{D}iv_{X} \to \mathfrak{z}^{1}_{X}$ `(21.6.4)` is an isomorphism of sheaves
of ordered groups.*

*a') Every prime `1`-codimensional cycle on $X$ is the image by `cyc` of a positive divisor, and the canonical
homomorphism $c : \mathcal{D}iv_{X} \to \mathfrak{z}^{1}_{X}$ is injective.*

*a") For every integral closed sub-prescheme $Y$ of $X$, of codimension `1`, the canonical immersion $Y \to X$ is
regular.*

*b) $X$ is normal and the homomorphism $cyc : \operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$ is bijective.*

*c) $X$ is locally factorial.*

The equivalence of b) and c) has been proved in `(21.6.9)`, as well as the fact that c) entails a). Moreover b) entails
a") by virtue of `(21.7.3.1)`, and a) trivially implies a'). It remains to see that a') or a") entails c).

Suppose then that condition a') is verified, and let us first show that $X$ is normal. Note first that if $X$ verifies
a'), so does every local scheme $\operatorname{Spec}(\mathcal{O}_{X,x})$. Consider then $x \in X^{(1)}$, so that $A =
\mathcal{O}_{X,x}$ is a Noetherian local ring of dimension `1`. Applying condition a') to $\operatorname{Spec}(A)$ and
to the prime `1`-codimensional cycle formed of the closed point of $\operatorname{Spec}(A)$, one sees that in $A$ the
maximal ideal is generated by a single regular element of $A$; hence `(0, 17.1.1)` $A$ is a regular ring. Since the
localized rings $A_{\mathfrak{p}}$ are also regular `(0, 17.3.2)`, one sees that $X$ is regular at all its non-isolated
maximal points; since it is also reduced (hence regular) at its isolated points by hypothesis, one concludes that $X$
verifies condition `(R_1)`. Let us show moreover that $X$ also verifies `(S_1)`, in other words that for every $x \in X$
such that $\dim(\mathcal{O}_{X,x}) \geq 1$, one has $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X,x})$ `(0, 16.4.6)`.
Indeed, hypothesis a') applied to $X_{1} = \operatorname{Spec}(\mathcal{O}_{X,x})$ shows that there exists on this
prescheme at least one divisor $\neq 0$, in other words that one has $\mathcal{M}_{X_{1}} \neq
\mathcal{O}^{\times}_{X_{1}}$, and it suffices to apply `(21.1.10)`. One already deduces from these results that $X$ is
reduced `(5.8.5)`. Let us next prove that it verifies condition `(S_2)` (which will establish that $X$ is normal, by
virtue of Serre's criterion `(5.8.6)`). Argue by contradiction by supposing that the set $E$ of points $x \in X$ where
$X$ does not verify `(S_2)` is non-empty, and let $x \in E$ be a point for which $\dim(\mathcal{O}_{X,x})$ is the
smallest possible; since $X$ verifies `(S_1)`, one has $\dim(\mathcal{O}_{X,x}) \geq 2$. In $X_{1} =
\operatorname{Spec}(\mathcal{O}_{X,x})$, the open $U = X_{1} - {x}$ verifies `(S_2)`; let us show that `X_1` verifies
`(S_2)`, so that one will have reached a contradiction. It suffices, by virtue of `(5.10.5)`, to show that every section
$f$ of $\mathcal{O}_{U}$ over $U$ extends to a section of $\mathcal{O}_{X_{1}}$ over `X_1`. Since `X_1` is reduced and
$U$ dense in `X_1`, $U$ is schematically dense in `X_1`, and consequently $f$ is the restriction to $U$ of a regular
meromorphic section $g \in M(X_{1})$. Moreover, since $\dim(\mathcal{O}_{X,x}) \geq 2$, one has $cyc(div(g)) \geq 0$
since $g | U = f$; since the homomorphism `cyc` is injective, one necessarily has $div(g) \geq 0$, hence `(21.6.4)` $g$
is a section of $\mathcal{O}_{X_{1}}$ over `X_1`, which establishes our assertion.

To show that a') implies c), remark then that condition a') implies that the canonical homomorphism $cyc :
\operatorname{Div}(X) \to \mathfrak{z}^{1}(X)$ is surjective; since $X$ is normal, it suffices to apply `(21.6.9)`.

Let us now prove that a") entails c). It follows from `(21.6.5)` that a") entails that every prime `1`-codimensional
cycle on $X$ is the image by `cyc` of a positive divisor; the first part of the reasoning made above therefore proves
again that $X$ verifies `(R_1)` and `(S_1)`. It remains to see that $X$ is normal (the end of the reasoning being then
the same), that is to say that if $x \in X$ is such that $\dim(\mathcal{O}_{X,x}) \geq 2$, one has
$prof(\mathcal{O}_{X,x}) \geq 2$. Now, if $y$ is a generization of $x$ such that $\overline{y}$ is of codimension `1` in
$X$, the reduced sub-prescheme $Y$ of $X$ having $\overline{y}$ for underlying

<!-- original page 279 -->

space is integral, hence regularly immersed in $X$ by hypothesis. This entails that there exists a regular element $t$
of $\mathcal{O}_{X,x}$ such that the ideal $t \mathcal{O}_{X,x}$ is the prime ideal defining the prescheme `Y_1`,
inverse image of $Y$ in $X_{1} = \operatorname{Spec}(\mathcal{O}_{X,x})$. Since $\mathcal{O}_{X,x} / t
\mathcal{O}_{X,x}$ is integral, this proves that $prof(\mathcal{O}_{X,x}) \geq 2$ and finishes the proof of `(21.7.4)`.

**Remark (21.7.5).**

<!-- label: IV.21.7.5 -->

*One cannot in `(21.7.4)` replace condition a') by the weaker condition that every prime `1`-codimensional cycle of $X$
be the image by `cyc` of a positive divisor. This is shown by the example where $X$ is the affine scheme defined in
`(14.1.5)` ("union of a plane and a line meeting it"), which is not normal; with the notations introduced in `(14.1.5)`,
the prime `1`-codimensional cycles of $X$ are those of the plane `X_1` and the closed points of the line `X_2` distinct
from the common point of `X_1` and `X_2`; if $t_{1}$, $t_{2}$, $t_{3}$ are the images of `T_1`, `T_2`, `T_3` in $A /
\mathfrak{a}$, one sees therefore that the prime `1`-codimensional cycles of $X$ are defined by the principal prime
ideals of generators $P(t_{1}, t_{2})$ ($P$ irreducible in $K[T_{1}, T_{2}]$) or $t_{3} - a$, with $a \neq 0$ in $K$;
these elements being regular in $A / \mathfrak{a}$, every `1`-codimensional cycle is indeed the canonical image of a
positive divisor.*

**Corollary (21.7.6).**

<!-- label: IV.21.7.6 -->

*Let $X$ be a locally Noetherian prescheme, reduced at each of its isolated points. The following conditions are
equivalent:*

*a) The canonical homomorphism $c : \mathcal{D}iv_{X} \to \mathfrak{z}^{1}_{X}$ is an isomorphism of sheaves of ordered
groups, and one has `Div(X) = Div.princ(X)`.*

*a') The canonical homomorphism $c : \mathcal{D}iv_{X} \to \mathfrak{z}^{1}_{X}$ is injective, and every prime
`1`-codimensional cycle is the image by `cyc` of a positive principal divisor, in other words is of the form
$cyc(div(f))$, where $f$ is a regular section of $\mathcal{O}_{X}$ over $X$.*

*a") For every integral closed sub-prescheme $Y$ of $X$, of codimension `1`, there exists a regular section $f$ of
$\mathcal{O}_{X}$ over $X$ such that $Y$ is defined by the Ideal $f \mathcal{O}_{X}$.*

*b) $X$ is normal and every prime `1`-codimensional cycle on $X$ is principal.*

*c) $X$ is locally factorial and $\operatorname{Pic}(X) = 0$.*

*d) $X$ is normal, and for every open $U$ of $X$, one has $\operatorname{Pic}(U) = 0$.*

The equivalence of a), a'), a"), b) and c) follows at once from `(21.7.4)` and from `(21.6.11)`. Moreover, it follows at
once from a") that every non-empty open $U$ of $X$ again verifies the same conditions; in other words these conditions
imply d). It remains to see that d) entails b). Now, denote by $U_{\lambda}$ the opens that are complements of finite
unions of sets of the form $\overline{x}$, where $\dim(\mathcal{O}_{X,x}) \geq 2$; it is clear that the $U_{\lambda}$
form a decreasing filtered family, and that for every $x \in \bigcap_{\lambda} U_{\lambda}$, one has
$\dim(\mathcal{O}_{X,x}) \leq 1$, hence $\mathcal{O}_{X,x}$ is a principal ring by virtue of the hypothesis. One can
therefore apply to the family $(U_{\lambda})$ proposition `(21.6.12)`, which shows that $Cl(X)$ is isomorphic to $\lim
\operatorname{Pic}(U_{\lambda})$, hence $Cl(X) = 0$ by virtue of the hypothesis, which proves b) by definition.

**Remark (21.7.7).**

<!-- label: IV.21.7.7 -->

*When $X = \operatorname{Spec}(A)$, where $A$ is a Noetherian integral ring, the equivalent conditions of `(21.7.6)` are
equivalent to saying that $A$ is a factorial ring.*

<!-- original page 280 -->

### 21.8. Divisors and normalization

**Lemma (21.8.1).**

<!-- label: IV.21.8.1 -->

*Let $f : X' \to X$ be an integral morphism of preschemes. For every $\mathcal{O}_{X'}$-Module locally free
$\mathcal{E}'$ of constant rank $n$ and every $x \in X$, there exists an open neighbourhood $U$ of $x$ in $X$ such that,
setting $U' = f^{-1}(U)$, $\mathcal{E}' | U'$ is isomorphic to $\mathcal{O}^{n}_{U'}$.*

Since the question is local on $X$, one may restrict to the case where $X = \operatorname{Spec}(A)$ is affine; one then
has $X' = \operatorname{Spec}(A')$, where $A'$ is an integral $A$-algebra. Then $A'$ is the inductive limit of its
finite sub-$A$-algebras $A'_{\lambda}$. Setting $X'_{\lambda} = \operatorname{Spec}(A'_{\lambda})$ and denoting by
$p_{\lambda} : X' \to X'_{\lambda}$ the structure morphism, it follows from `(8.5.2)` and `(8.5.5)` that there exist an
index $\lambda$ and an $\mathcal{O}_{X'_{\lambda}}$-Module $\mathcal{E}'_{\lambda}$ locally free of rank $n$ such that
$\mathcal{E}' = p^{*}_{\lambda}(\mathcal{E}'_{\lambda})$; it will evidently suffice to prove the lemma for
$X'_{\lambda}$ and $\mathcal{E}'_{\lambda}$, in other words, one may restrict to the case where the morphism $f$ is
finite. Set $B = \mathcal{O}_{X,x}$ and let $B'$ be the ring of the affine scheme $X'_{0} = X' \times_{X}
\operatorname{Spec}(\mathcal{O}_{X,x})$; since $B$ is a local ring and $B'$ is a finite $B$-algebra, $B'$ is a
semi-local ring (Bourbaki, _Alg. comm._, chap. V, §2, n° 1, prop. 3); one concludes that the locally free
$\mathcal{O}_{X'_{0}}$-Module $\mathcal{E}'_{0} = \mathcal{E}' \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X,x}$ is
isomorphic to $\mathcal{O}^{n}_{X'_{0}}$ (Bourbaki, _Alg. comm._, chap. II, §5, n° 3, prop. 5). Considering $X'_{0}$ as
the projective limit

<!-- original page 281 -->

of the preschemes induced by $X'$ on the opens $f^{-1}(U)$, where $U$ ranges over the filtered set of affine open
neighbourhoods of $x$ in $X$, following the method of `(8.1.2, a)`, and applying `(8.5.2.5)`, one obtains the desired
conclusion.

**Corollary (21.8.2).**

<!-- label: IV.21.8.2 -->

*Let $f : X' \to X$ be an integral morphism of preschemes. Then:*

*(i) $R^{1} f_{*}(\mathcal{O}^{\times}_{X'}) = 0$ $(0_{III}, 12.2.1)$.*

*(ii) The group $\operatorname{Pic}(X')$ is canonically isomorphic to $H^{1}(X, f_{*}(\mathcal{O}^{\times}_{X'}))$.*

(i) $R^{1} f_{*}(\mathcal{O}^{\times}_{X'})$ is the sheaf associated to the presheaf of commutative groups $U \mapsto
H^{1}(f^{-1}(U), \mathcal{O}^{\times}_{X'})$ on $X$ (_loc. cit._); the stalk of this sheaf at a point $x$ may therefore
$(0_{I}, 5.4.7)$ be identified with the commutative group $\lim \operatorname{Pic}(f^{-1}(U))$, where $U$ ranges over
the open neighbourhoods of $x$, the transition homomorphisms $\operatorname{Pic}(f^{-1}(U')) \to
\operatorname{Pic}(f^{-1}(U))$ for two opens $U \subset U'$ being defined by `(21.3.2.4)`. Now, for every $x \in X$,
every open neighbourhood $U'$ of $x$ in $X$, and every element $\zeta' \in \operatorname{Pic}(f^{-1}(U'))$, it follows
from `(21.8.1)` that there is an open neighbourhood $U \subset U'$ of $x$ such that the image of $\zeta'$ in
$\operatorname{Pic}(f^{-1}(U))$ is zero. Hence the stalk of $R^{1} f_{*}(\mathcal{O}^{\times}_{X'})$ at $x$ is zero.

(ii) The Leray spectral sequence for the composite functor $\mathcal{F} \mapsto \Gamma(X, f_{*}(\mathcal{F}))$ on
sheaves of commutative groups on $X'$ `(T, 2.4)` gives the exact sequence of low-degree terms `(M, XV, 6)`

```text
                         0 → H¹(X, f_*(𝒪_{X'}^×)) → H¹(X', 𝒪_{X'}^×) → H⁰(X, R¹ f_*(𝒪_{X'}^×))
```

and the conclusion follows from (i) and from the isomorphism between $\operatorname{Pic}(X')$ and $H^{1}(X',
\mathcal{O}^{\times}_{X'})$ $(0_{I}, 5.4.7)$.

**Proposition (21.8.3).**

<!-- label: IV.21.8.3 -->

*Let $f = (\psi, \theta) : X' \to X$ be an integral morphism of preschemes; suppose that, for every open $U$ of $X$, the
homomorphism $\Gamma(\theta) : \Gamma(U, \mathcal{O}_{X}) \to \Gamma(f^{-1}(U), \mathcal{O}_{X'})$ sends regular
elements to regular elements, which permits one canonically to extend the homomorphism $\theta : \mathcal{O}_{X} \to
f_{*}(\mathcal{O}_{X'})$ to a homomorphism of sheaves of rings $\theta' : \mathcal{M}_{X} \to f_{*}(\mathcal{M}_{X'})$,
whence homomorphisms of sheaves of multiplicative groups $\theta^{*} : \mathcal{O}^{\times}_{X} \to
f_{*}(\mathcal{O}^{\times}_{X'})$ and $\theta'^{*} : \mathcal{M}^{\times}_{X} \to f_{*}(\mathcal{M}^{\times}_{X'})$,
yielding by passage to quotients a homomorphism $\theta''^{*} : \mathcal{D}iv_{X} \to f_{*}(\mathcal{D}iv_{X'})$. One
then has a commutative diagram*

```text
                         1 ——→ 𝒪_X^×  ——→  𝓜_X^×  ——→  𝒟iv_X  ——→  0
                                  │           │           │
  (21.8.3.1)                    θ^*│        θ'^*│        θ''^*│
                                  ↓           ↓           ↓
                         1 ——→ f_*(𝒪_{X'}^×) → f_*(𝓜_{X'}^×) → f_*(𝒟iv_{X'}) → 0
```

*in which both rows are exact.*

The only point to verify is the exactness of the second row of the diagram, which follows from applying the exact
cohomology sequence for the functor $f_{*}$ to the exact sequence of sheaves of commutative groups on $X'$

$$ 1 \to \mathcal{O}^{\times}_{X'} \to \mathcal{M}^{\times}_{X'} \to \mathcal{D}iv_{X'} \to 0 $$

and from `(21.8.2)`.

<!-- original page 282 -->

**Corollary (21.8.4).**

<!-- label: IV.21.8.4 -->

*If, in addition to the hypotheses of `(21.8.3)`, the homomorphism $\theta'$ is an isomorphism of sheaves of rings, then
$\theta^{*} : \mathcal{O}^{\times}_{X} \to f_{*}(\mathcal{O}^{\times}_{X'})$ is injective, $\theta''^{*} :
\mathcal{D}iv_{X} \to f_{*}(\mathcal{D}iv_{X'})$ is surjective and $Ker(\theta''^{*})$ is isomorphic to
$Coker(\theta^{*})$.*

This is an immediate consequence of the snake-diagram lemma (Bourbaki, _Alg. comm._, chap. I, §2, n° 4, prop. 2) applied
to the diagram `(21.8.3.1)`.

**Proposition (21.8.5).**

<!-- label: IV.21.8.5 -->

*Let $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ an integral morphism; assume that there exists a
schematically dense open $U$ in $X$ such that $f^{-1}(U)$ is schematically dense in $X'$ `(cf. (20.3.5))`, and that the
morphism $f^{-1}(U) \to U$, the restriction of $f$, is an isomorphism. Then:*

*(i) The homomorphism $\theta' : \mathcal{M}_{X} \to f_{*}(\mathcal{M}_{X'})$ is defined and bijective, the homomorphism
$\theta^{*} : \mathcal{O}^{\times}_{X} \to f_{*}(\mathcal{O}^{\times}_{X'})$ is injective, the homomorphism
$\theta''^{*} : \mathcal{D}iv_{X} \to f_{*}(\mathcal{D}iv_{X'})$ is surjective, $Ker(\theta''^{*})$ is isomorphic to
$\mathcal{N} = Coker(\theta^{*})$, and the support of the sheaf of multiplicative groups $\mathcal{N}$ is contained in
$S = X - U$.*

*(ii) Assume in addition that the set $S$ is discrete and, to abbreviate, set $\mathcal{O}'_{X} =
f_{*}(\mathcal{O}_{X'})$. Then one has a commutative diagram*

```text
                                  j                            i_X    i_{X'}
  1 → ∏_{s ∈ S} 𝒪'^×_{X,s}/𝒪^×_{X,s} ─→ Div(X) ──→ Div(X') ─→ 0
                                  │           │
  (21.8.5.1)                      │           │
                                  ↓           ↓
  1 → (∏_{s ∈ S} 𝒪'^×_{X,s}/𝒪^×_{X,s}) / Im Γ(X', 𝒪_{X'}^×) ─→ Pic(X) ─→ Pic(X') ─→ 0
                                  j'
```

*where the rows are exact and where the left vertical arrow is the canonical homomorphism.*

(i) The hypothesis entails that one has a canonical isomorphism $\mathcal{M}_{X} \xrightarrow{\sim}
f_{*}(\mathcal{M}_{X'})$ for the sheaves of germs of pseudo-functions `(20.2.2)`, whence the assertion concerning
$\theta'$, in view of the existence of the canonical isomorphisms $\mathcal{M}_{X} \xrightarrow{\sim} \mathcal{M}'_{X}$
and $\mathcal{M}_{X'} \xrightarrow{\sim} \mathcal{M}'_{X'}$ `(20.2.11)`. The rest of assertion (i) follows from
`(21.8.4)`, except for what concerns the support of $\mathcal{N}$, which follows directly from the hypothesis on $U$.

(ii) Applying the exact cohomology sequence to the two exact sequences of sheaves of commutative groups

```text
                         1 → 𝒩 → 𝒟iv_X → f_*(𝒟iv_{X'}) → 0
  (21.8.5.2)
                         1 → 𝒪_X^× → f_*(𝒪_{X'}^×) → 𝒩 → 1
```

one obtains respectively the exact sequences

```text
                         1 → Γ(X, 𝒩) ─→ Div(X) → Div(X') → H¹(X, 𝒩)
                                       j
  (21.8.5.3)
                         Γ(X', 𝒪_{X'}^×) → Γ(X, 𝒩) ─→ Pic(X) → Pic(X') → H¹(X, 𝒩)
                                                    ∂
```

taking account of the canonical isomorphism $\operatorname{Pic}(X') \xrightarrow{\sim} H^{1}(X,
f_{*}(\mathcal{O}^{\times}_{X'}))$ `(21.8.2)`. Now, since the support of $\mathcal{N}$ is contained in the discrete set
$S$, closed in $X$, one has

<!-- original page 283 -->

$H^{1}(X, \mathcal{N}) = H^{1}(S, \mathcal{N} | S)$ `(G, II, 4.9.2)` and $H^{1}(S, \mathcal{N} | S) = \prod_{s \in S}
H^{1}({s}, \mathcal{N}_{s}) = 0$ by definition of cohomology `(G, II, 4.4)`. Similarly one has $\Gamma(X, \mathcal{N}) =
\prod_{s \in S} \mathcal{N}_{s}$ and $\mathcal{N}_{s} = \mathcal{O}'^{\times}_{X,s} / \mathcal{O}^{\times}_{X,s}$, by
virtue of the second exact sequence `(21.8.5.2)`. It remains to make precise the injections $j$ and $j'$. One can
describe a section $t$ of $\mathcal{N}$ over $X$ by taking a covering of $X$ formed by $U$ and by opens $U_{i}$ such
that $U_{i} \cap S$ is reduced to a single point $s_{i}$ and that $U_{i} \cap U_{j} \subset U$ for $i \neq j$, then
considering for each $i$ a section $t_{i}$ of $\mathcal{N}$ over $U_{i}$, necessarily such that $(t_{i})_{s_{i}} \in
\mathcal{O}'^{\times}_{X,s_{i}} / \mathcal{O}^{\times}_{X,s_{i}}$ and $(t_{i})_{x} = 0$ at the points $x \in U_{i} -
{s_{i}}$. The germ $(t_{i})_{s_{i}}$ comes from a section $u_{i}$ of $\mathcal{O}^{\times}_{X'}$ over $f^{-1}(U_{i})$,
which one may also consider as a section of $\mathcal{M}^{\times}_{X'}$ over $f^{-1}(U_{i})$, hence a section of
$\mathcal{M}^{\times}_{X}$ over $U_{i}$ (in virtue of the hypothesis); there corresponds canonically to this section a
section $d_{i} \in \Gamma(U_{i}, \mathcal{D}iv_{X})$, and since in $f^{-1}(U \cap U_{j})$ the restriction of $u_{i}$ is
identified with a section of $\mathcal{O}^{\times}_{X'}$ over $U \cap U_{j}$ by virtue of the hypothesis, the
restrictions of the $d_{i}$ to $U \cap U_{j}$ are all zero, so the $d_{i}$ are the restrictions of one and the same
divisor $d \in \operatorname{Div}(X)$, which is the image of the section $t$ under $j$. Similarly, the image of $t$
under $\partial : \Gamma(X, \mathcal{N}) \to H^{1}(X, \mathcal{O}^{\times}_{X})$ comes from the cocycle equal to the
restriction of $\mathcal{N}$ in $U \cap U_{j}$ for each $i$, to $(u_{i} | (U_{i} \cap U_{j}))(u_{j} | (U_{i} \cap
U_{j}))^{-1}$ in $U_{i} \cap U_{j}$, whence the expression of `j'(t)` and the commutativity of the diagram `(21.8.5.1)`.

**Remarks (21.8.6).**

<!-- label: IV.21.8.6 -->

(i) The conditions of application of `(21.8.5, (i))` are in particular satisfied when $X$ is a reduced locally
Noetherian prescheme having only finitely many irreducible components, $X'$ its normalization, and $X'$ is also locally
Noetherian `(II, 6.3.8)`; the $\mathcal{O}_{X}$-Module $\mathcal{D}iv_{X}$ is then an extension of
$f_{*}(\mathcal{D}iv_{X'})$ by the cokernel $\mathcal{N}$ of $\mathcal{O}^{\times}_{X} \to
f_{*}(\mathcal{O}^{\times}_{X'})$, which one may regard as known. If moreover $X$ is a (reduced) algebraic curve over a
field $k$, one is in the conditions of application of `(21.8.5, (ii))`.

(ii) When the conditions of application of `(21.8.5, (ii))` are satisfied and moreover the global canonical homomorphism
$\Gamma(X, \mathcal{O}_{X}) \to \Gamma(X', \mathcal{O}_{X'})$ is bijective, one sees that the kernels of the surjective
homomorphisms $\operatorname{Div}(X) \to \operatorname{Div}(X')$ and $\operatorname{Pic}(X) \to \operatorname{Pic}(X')$
are isomorphic.

(iii) When the conditions of application of `(21.8.5, (ii))` are satisfied, one sees that the homomorphism
$\operatorname{Div}(X) \to \operatorname{Div}(X')$ can be injective (in which case it is bijective) only if
$\mathcal{O}'^{\times}_{X,s} = \mathcal{O}^{\times}_{X,s}$ for every $s \in S$. For an $s \in S$ such that the ring
$\mathcal{O}'_{X,s}$ is local (which, taking into account that $X' = \operatorname{Spec}(\mathcal{O}'_{X})$ `(II, 1.3)`,
means that there exists *only one* point $s' \in X'$ above $s$), this implies necessarily that the residue fields $k(s)$
and $k(s')$ are equal and that $1 + \mathfrak{m}_{s} = 1 + \mathfrak{m}_{s'}$, hence finally is equivalent to the
relation $\mathcal{O}'_{X,s} = \mathcal{O}_{X,s}$, or also (taking the hypothesis into account) to the fact that there
is an open neighbourhood $V$ of $s$ in $X$ such that the morphism $f^{-1}(V) \to V$ is an isomorphism. In the general
case, the ring $\mathcal{O}'_{X,s}$ is semi-local (this is evident when the morphism $f$ is finite, and in the general
case it follows from $(0_{IV}, 23.2.6)$); the canonical homomorphism $\mathcal{O}^{\times}_{X,s} \to
\mathcal{O}'^{\times}_{X,s}$ defines, by passage to quotients, a homomorphism from the multiplicative group
$(k(s))^{\times}$ to the product of the multiplicative groups $(k(s'_{j}))^{\times}$, the $s'_{j}$ being the points (in

<!-- original page 284 -->

number `> 1`) of $X'$ above $s$. It is immediate that this homomorphism can be bijective only if $k(s)$ and all the
$k(s'_{j})$ are equal to the field $\mathbb{F}_{2}$ with `2` elements; moreover, if this condition is verified, it is
necessary in addition that the multiplicative group $1 + \mathfrak{m}_{s}$ have image $1 + \mathfrak{r}$, where
$\mathfrak{r}$ is the radical of $\mathcal{O}'_{X,s}$, or also that $\mathfrak{m}_{s} = \mathfrak{r}$, which entails
that $\mathcal{O}'_{X,s} \otimes_{\mathcal{O}_{X,s}} k(s)$ is a direct sum of fields isomorphic to $k(s)$ (which, when
the morphism $f$ is finite, entails that it is unramified at the points $s'_{j}$ `(17.4.1)`). If, for example, no
residue field of $X$ is isomorphic to $\mathbb{F}_{2}$, the canonical homomorphism $\operatorname{Div}(X) \to
\operatorname{Div}(X')$ can be bijective only if $f$ is an isomorphism. In the case where the canonical homomorphism
$\Gamma(X, \mathcal{O}_{X}) \to \Gamma(X', \mathcal{O}_{X'})$ is bijective, one concludes from the preceding and from
(ii) that in the previous considerations one may replace the homomorphism $\operatorname{Div}(X) \to
\operatorname{Div}(X')$ by the homomorphism $\operatorname{Pic}(X) \to \operatorname{Pic}(X')$.

### 21.9. Divisors on preschemes of dimension 1

**(21.9.1).** Let $X$ be a topological space, $x$ a point of $X$, $i_{x} : {x} \to X$ the canonical injection. If $A(x)$
is a commutative group, one may regard it as a sheaf of commutative groups on the space ${x}$ reduced to a single point,
and take its direct image $(i_{x})_{*}(A(x))$, which is a sheaf of commutative groups on $X$ $(0_{I}, 3.4.1)$; it
follows at once from the definitions that for every open $U$ of $X$, $\Gamma(U, (i_{x})_{*}(A(x))) = A(x)$ if $x \in U$,
and reduces to `0` in the contrary case; hence, for $y \in {x}$ one has $((i_{x})_{*}(A(x)))_{y} = A(x)$, and for $y
\notin {x}$, $((i_{x})_{*}(A(x)))_{y} = 0$.

If now $\mathcal{F}$ is a sheaf of commutative groups on $X$ and $Y$ a part of $X$, for every open $U$ of $X$ one has a
canonical homomorphism

```text
  (21.9.1.1)             Γ(U, ℱ) → ∏_{x ∈ U ∩ Y} ℱ_x = ∏_{x ∈ Y} Γ(U, (i_x)_*(ℱ_x))
```

and since these homomorphisms commute with the restriction operators, they define a canonical homomorphism of sheaves

```text
  (21.9.1.2)             j_Y : ℱ → ∏_{x ∈ Y} (i_x)_*(ℱ_x).
```

**Lemma (21.9.2).**

<!-- label: IV.21.9.2 -->

*Let $X$ be a locally Noetherian topological space, `X_0` the set of its closed points, $\mathcal{F}$ a sheaf of
commutative groups on $X$. The following conditions are equivalent:*

*a) The canonical homomorphism $j_{X_{0}} : \mathcal{F} \to \prod_{x \in X_{0}} (i_{x})_{*}(\mathcal{F}_{x})$ is
injective and has as image $\bigoplus_{x \in X_{0}} (i_{x})_{*}(\mathcal{F}_{x})$.*

*a') There exists a family of commutative groups $(A(x))_{x \in X_{0}}$ such that $\mathcal{F}$ is isomorphic to
$\bigoplus_{x \in X_{0}} (i_{x})_{*}(A(x))$.*

*b) Every section of $\mathcal{F}$ over an open $U$ of $X$ has a discrete support contained in `X_0`.*

*When this is so, for every $x \in X_{0}$, the group $A(x)$ is determined up to unique isomorphism and is isomorphic to
$\mathcal{F}_{x}$. Moreover, the sheaf $\mathcal{F}$ is then flasque.*

Since the points of `X_0` are closed in $X$, one has $((i_{x})_{*}(A(x)))_{y} = 0$ for every

<!-- original page 285 -->

$y \neq x \in X_{0}$; this remark proves the uniqueness assertion relative to the groups $A(x)$, and it is clear besides
that a) implies a'). To see that a') implies b), one may restrict to the case where $U$ is Noetherian; then
`(G, II, 3.10)` one has

```text
                         Γ(U, ⨁_{x ∈ X_0} (i_x)_*(A(x))) = ⨁_{x ∈ X_0} Γ(U, (i_x)_*(A(x)))
```

so every section $s$ of $\mathcal{F}$ over $U$ is a direct sum of finitely many sections $s_{k} \in \Gamma(U,
(i_{x_{k}})_{*}(A(x_{k})))$ ($1 \leq k \leq n$) with $x_{k} \in X_{0}$. But since $x_{k}$ is closed in $X$, the support
of $s_{k}$ is reduced to $x_{k}$, so the support of $s$ is contained in the finite set of the $x_{k}$, which is
evidently discrete since the points $x_{k}$ are closed. Let us finally show that b) entails a); for every Noetherian
open $U$, any support of a section of $\mathcal{F}$ over $U$, being discrete and quasi-compact, is finite. One thus
deduces from hypothesis b) that for every Noetherian open $U$, the image of the homomorphism `(21.9.1.1)` (for $Y =
X_{0}$) is contained in $\bigoplus_{x \in X_{0}} \Gamma(U, (i_{x})_{*}(\mathcal{F}_{x}))$ and that this homomorphism is
injective, which establishes a).

Finally, to show that $\mathcal{F}$ is flasque, consider a section $s$ of $\mathcal{F}$ over an open $U$ of $X$; since
the support of $s$ is a discrete and closed subspace of $X$, one extends $s$ to a section $s'$ of $\mathcal{F}$ over $X$
by setting $s'_{z} = 0$ in $X - U$.

**Remarks (21.9.3).**

<!-- label: IV.21.9.3 -->

(i) In condition b) of `(21.9.2)`, it does not suffice to suppose that the support of every section of $\mathcal{F}$
over an arbitrary open of $X$ is discrete; this is shown by the example where one takes for $X$ the spectrum of a
discrete valuation ring, with a closed point $b$ and a generic point $a$, and for $\mathcal{F}$ the sheaf of commutative
groups such that $\mathcal{F}_{b} = 0$ and $\mathcal{F}_{a} = \mathbb{Z}$.

(ii) Assume that the conditions of `(21.9.2)` are verified; let $E$ be a discrete part of `X_0`, and for every $x \in
E$, let $a(x)$ be an element of $A(x)$. Then there exists one and only one section $t$ of $\bigoplus_{x \in X_{0}}
(i_{x})_{*}(A(x))$ over $X$ such that $t_{x} = a(x)$ for every $x \in E$ and that the support of $t$ is contained in
$E$. Indeed, for every Noetherian open $U$, $E \cap U$ is finite, and it suffices to take for $t$ the section of
$\bigoplus_{x \in X_{0}} (i_{x})_{*}(A(x))$ whose restriction to each Noetherian open $U$ is the sum of the $a(x)$ for
$x \in E \cap U$.

**Proposition (21.9.4).**

<!-- label: IV.21.9.4 -->

*Let $X$ be a locally Noetherian prescheme of dimension $\leq 1$, $X^{(1)}$ the set of points $x \in X$ such that
$\dim(\mathcal{O}_{X,x}) = 1$. One then has a canonical isomorphism*

```text
  (21.9.4.1)             𝒟iv_X ⥲ ⨁_{x ∈ X^{(1)}} (i_x)_*(Div(𝒪_{X,x}))
```

*and $\mathcal{D}iv_{X}$ is flasque.*

Taking the isomorphism `(21.4.6.1)` into account, the homomorphism `(21.9.4.1)` is defined by `(21.9.1.2)`: let us prove
that it is a bijection. Since $\dim(X) \leq 1$, the points of $X^{(1)}$ are the non-isolated closed points of $X$. One
is reduced to proving that: 1° $\mathcal{D}iv_{X}$ verifies condition b) of `(21.9.2)`; 2° for every isolated point $x
\in X$, one has $(\mathcal{D}iv_{X})_{x} = 0$. The second point follows from the fact that $\mathcal{O}_{X,x}$ is then
an Artinian ring and so every regular element of $\mathcal{O}_{X,x}$ is invertible. For the first, it suffices to note
that for every open $U$ of $X$ and every divisor $D \in \operatorname{Div}(U)$, the maximal points of the support $S$ of
$D$ are such that

<!-- original page 286 -->

$prof(\mathcal{O}_{X,x}) = 1$ `(21.1.9)`, so a fortiori belong to $X^{(1)} \cap U$; since $\dim(X) \leq 1$, the set of
these points equals $S$, and $S$ is therefore discrete, the set of irreducible components of $S$ being locally finite.

**Corollary (21.9.5).**

<!-- label: IV.21.9.5 -->

*Let $X$ be a locally Noetherian prescheme of dimension $\leq 1$. For every discrete part $E \subset X^{(1)}$ and every
family $(D(x))_{x \in E}$ with $D(x) \in \operatorname{Div}(\mathcal{O}_{X,x})$, there exists one and only one divisor
$D$ on $X$ such that the support of $D$ is contained in $E$ and $D_{x} = D(x)$ for every $x \in E$.*

This follows from `(21.9.4)` and `(21.9.3, (ii))`.

**Corollary (21.9.6).**

<!-- label: IV.21.9.6 -->

*Let $X$ be a locally Noetherian prescheme of dimension $\leq 1$; every divisor $D$ on $X$ is of the form $D' - D''$,
where $D'$, `D''` are two divisors $\geq 0$ with supports contained in that of $D$.*

In virtue of `(21.9.5)`, one is at once reduced to the case where $X = \operatorname{Spec}(A)$, $A$ a Noetherian local
ring; it then suffices to observe that $M(X)$ is the total ring of fractions of $A$, and that a section of
$\mathcal{M}^{\times}_{X}$ over $X$ is by definition expressible as a quotient $b/a$ of two regular elements of $A$.

**Corollary (21.9.7).**

<!-- label: IV.21.9.7 -->

*Let $X$ be a locally Noetherian prescheme of dimension $\leq 1$, having no isolated point, and $U$ a dense open in $X$.
Then there exists a divisor $D \geq 0$ on $X$, with support contained in $U$ and meeting each of the irreducible
components of $X$.*

One may assume that $U$ is the union of disjoint non-empty open sets $U_{\alpha}$, each contained in a single
irreducible component of $X$; it then suffices to take in each $U_{\alpha}$ a point $x_{\alpha}$ closed in $X$ (such a
point exists since the unique generic point of $U_{\alpha}$ cannot be isolated by hypothesis), and to apply `(21.9.5)`
to the discrete set of the $x_{\alpha}$.

The interest of this corollary is that it will allow one to prove that a separated algebraic curve $X$ over a field $k$
is quasi-projective, the divisor $D \geq 0$ defined in `(21.9.7)` being then necessarily ample in virtue of the Riemann-
Roch theorem for curves (chap. V).

**(21.9.8).** For locally Noetherian preschemes $X$ of dimension $\leq 1$, proposition `(21.9.4)` reduces the
determination of $\mathcal{D}iv_{X}$ to the case where $X = \operatorname{Spec}(A)$, $A$ a Noetherian local ring of
dimension `1`.

When $A$ is a regular local ring of dimension `1` (in other words, a discrete valuation ring), the group
$\operatorname{Div}(A)$ is canonically identified with $\mathbb{Z}$ `(21.6.8)`; consequently, in virtue of `(21.9.2)`:

**Proposition (21.9.9).**

<!-- label: IV.21.9.9 -->

*Let $X$ be a regular locally Noetherian prescheme of dimension $\leq 1$. Then the sheaf $\mathcal{D}iv_{X}$ is
canonically isomorphic to $\bigoplus_{x \in X^{(1)}} (i_{x})_{*}(\mathbb{Z}(x))$, where $\mathbb{Z}(x)$ is the additive
group $\mathbb{Z}$ considered as a sheaf of groups on the space ${x}$.*

**(21.9.10).** Assume only that the Noetherian local ring $A$ of dimension `1` is reduced; then, if $A'$ is the
normalization of $A$ (integral closure of $A$ in its total ring of fractions), $A'$ is Noetherian in virtue of the
Krull-Akizuki theorem (Bourbaki, _Alg. comm._, chap. VII, §2, n° 5, prop. 5), and one saw in `(21.8.6)` how

<!-- original page 287 -->

$\operatorname{Div}(A)$ may be obtained as an *extension* of $\operatorname{Div}(A')$, the latter group being of the
form $\mathbb{Z}^{r}$.

**Proposition (21.9.11).**

<!-- label: IV.21.9.11 -->

*Let $X$ be a Noetherian prescheme, `X_0` a closed subprescheme of $X$ having the following properties:*

*1° $\dim(X_{0}) \leq 1$.*

*2° For every locally closed part $Y$ of $X$ such that $Y \cap X_{0}$ is discrete, there exists a part $Y'$ of $Y$,
closed in $X$ and open in $Y$, containing $Y \cap X_{0}$.*

*Under these conditions:*

*(i) Let `Z_0` be the union of the sets ${x} \cap X_{0}$ as $x$ ranges over the part of $Ass(\mathcal{O}_{X})$ formed by
points such that ${x} \cap X_{0}$ is finite. Then, for every divisor `D_0` on `X_0` whose support does not meet `Z_0`,
there exists a divisor $D$ on $X$ whose inverse image under the canonical injection $X_{0} \to X$ exists `(21.4)` and
equals `D_0`; if moreover $D_{0} \geq 0$, one may suppose $D \geq 0$.*

*(ii) Assume in addition that there exists in `X_0` an affine open `U_0` containing $Ass(\mathcal{O}_{X_{0}}) \cup
Z_{0}$ (a condition automatically satisfied when there exists an ample $\mathcal{O}_{X_{0}}$-Module `(II, 4.5.4)`). Then
the canonical homomorphism `(21.3.2.4)` $\operatorname{Pic}(X) \to \operatorname{Pic}(X_{0})$ is surjective.*

(i) Taking `(21.9.6)` into account, one may restrict to proving the assertion concerning divisors $D_{0} \geq 0$; in
virtue of `(21.9.4)`, the support $T$ of `D_0` is a finite discrete and closed set in `X_0`. One may suppose $D_{0} \neq
0$, that is, $T \neq \emptyset$, otherwise there is nothing to prove. For every $x \in T$, there exists an element
$s_{x} \in \mathcal{O}_{X_{0},x}$ which is not a zero-divisor in this ring, belongs to its maximal ideal, and whose
image in $(\mathcal{D}iv_{X_{0}})_{x}$ is $(D_{0})_{x}$. There exists an affine open neighbourhood $U^{(x)}$ of $x$ in
$X$ and a section $g^{(x)}$ of $\mathcal{O}_{X}$ over $U^{(x)}$ such that $s_{x}$ is the image in
$\mathcal{O}_{X_{0},x}$ of the germ $(g^{(x)})_{x} \in \mathcal{O}_{X,x}$; we shall see that by taking $U^{(x)}$ small
enough, one can arrange for $g^{(x)}$ not to be a zero-divisor in $\Gamma(U^{(x)}, \mathcal{O}_{X})$, in other words
`(3.1.9)`, denoting by $V^{(x)}$ the closed part of $U^{(x)}$ formed by $y$ such that $g^{(x)}(y) = 0$, one has $V^{(x)}
\cap Ass(\mathcal{O}_{X}) = \emptyset$. Now, if $z \in Ass(\mathcal{O}_{X})$, the hypothesis $x \notin Z_{0}$ entails
that one has either $x \notin {z}$, or $x$ is not isolated in ${z} \cap X_{0}$. By replacing $U^{(x)}$ by a smaller
open, one may suppose that the second case occurs for a $z \in V^{(x)} \cap Ass(\mathcal{O}_{X})$; $V^{(x)}$ would
therefore contain an irreducible component of dimension `1` of $X_{0} \cap U^{(x)}$ containing $x$; but this would mean
that the image $\bar{g}^{(x)}$ of $g^{(x)}$ in $\Gamma(U^{(x)} \cap X_{0}, \mathcal{O}_{X_{0}})$ would be in the
nilradical of this ring, and consequently $s_{x}$ would belong to the nilradical of $\mathcal{O}_{X_{0},x}$, which is
absurd. One has therefore $x \notin {z}$ for every point $z \in V^{(x)} \cap Ass(\mathcal{O}_{X})$, and since this set
is finite, one may, by replacing $U^{(x)}$ by a smaller open neighbourhood of $x$, suppose that $V^{(x)} \cap
Ass(\mathcal{O}_{X}) = \emptyset$.

By virtue of the choice of $U^{(x)}$, one may define a divisor $D'^{(x)}$ on $U^{(x)}$ by $D'^{(x)} = div(g^{(x)})$;
moreover, one saw above that $x$ is necessarily isolated in $V^{(x)} \cap X_{0}$, so by replacing $U^{(x)}$ again by a
smaller open neighbourhood of $x$, one may suppose that $V^{(x)} \cap X_{0}$ is reduced to the point $x$. But there
exists then, in virtue of condition 2°, a part $W^{(x)}$ of $V^{(x)}$, closed in $X$ and open in $V^{(x)}$, such that
$W^{(x)} \cap X_{0} = {x}$. Replacing $U^{(x)}$ again by a smaller open neighbourhood of $x$, one may therefore suppose

<!-- original page 288 -->

that $W^{(x)} = V^{(x)}$, in other words that $V^{(x)}$ is closed in $X$. One may then define a divisor $D^{(x)}$ on $X$
by the condition that $D^{(x)} | U^{(x)} = D'^{(x)}$ and $D^{(x)} | (X - V^{(x)}) = 0$, which makes sense because in
$U^{(x)} \cap (X - V^{(x)})$ the restriction of $g^{(x)}$ is an invertible section, so the restrictions to this open of
the two divisors considered on $U^{(x)}$ and $X - V^{(x)}$ are equal. It then suffices, to answer the question, to take
$D = \sum_{x \in T} D^{(x)}$, which makes sense since $T$ is finite.

(ii) Taking the commutative diagram `(21.4.2.1)` into account, the conclusion will follow from (i) if one proves that
every invertible $\mathcal{O}_{X_{0}}$-Module $\mathcal{L}_{0}$ is isomorphic to an $\mathcal{O}_{X_{0}}$-Module of the
form $\mathcal{O}_{X_{0}}(D_{0})$ `(21.2.8)`, where `D_0` is a divisor on `X_0` whose support does not meet `Z_0`. Now,
since `U_0` is schematically dense in `X_0` `(20.2.13, (iv))`, it suffices for this to prove that there exists a section
$t \in \Gamma(U_{0}, \mathcal{L}_{0})$ such that $t(z_{0}) \neq 0$ at the points of $Ass(\mathcal{O}_{X_{0}}) \cup
Z_{0}$ `(3.1.9)`. One may therefore restrict to the case where $X_{0} = \operatorname{Spec}(A_{0})$ is affine; but then
$\mathcal{L}_{0}$ is ample `(II, 5.1.4)` and since the set $Ass(\mathcal{O}_{X_{0}}) \cup Z_{0}$ is finite, the
conclusion follows from `(II, 4.5.4)`.

**Corollary (21.9.12).**

<!-- label: IV.21.9.12 -->

*Let $A$ be a Henselian local ring `(18.5.8)`, $S = \operatorname{Spec}(A)$, $s_{0}$ the closed point of $S$, $f : X \to
S$ a separated morphism of finite presentation, and suppose that the set $X_{0} = f^{-1}(s_{0})$ is of dimension $\leq
1$. Then, for every closed subscheme $X'_{0}$ of $X$ having `X_0` as underlying set and of finite presentation over $S$,
the canonical homomorphism `(21.3.2.4)` $\operatorname{Pic}(X) \to \operatorname{Pic}(X'_{0})$ is surjective.*

Let us first show that it suffices to prove the corollary when the Henselian local ring $A$ is moreover Noetherian. One
knows in fact `(18.6.15)` that one can write $A = \lim A_{\lambda}$, where the $A_{\lambda}$ are Noetherian Henselian
local rings, the homomorphisms $A_{\lambda} \to A$ being local; there exists in addition an index $\alpha$ and a
separated morphism of finite presentation $f_{\alpha} : X_{\alpha} \to S_{\alpha} = \operatorname{Spec}(A_{\alpha})$
such that $X$ and $f$ are deduced from $X_{\alpha}$ and $f_{\alpha}$ by the base change $S \to S_{\alpha}$
`(8.10.5, (v))`; with the usual notation `(8.8.1)`, the morphisms $f_{\lambda} : X_{\lambda} \to S_{\lambda}$ will be
separated for $\lambda \geq \alpha$ and one will have $X = X_{\lambda} \times_{S_{\lambda}} S$. Moreover, one may assume
that, if $s_{0\lambda}$ is the unique closed point of $S_{\lambda}$, there is a closed subscheme $X'_{0\lambda}$ of
$X_{\lambda}$, having the same underlying set as $f^{-1}_{\lambda}(s_{0\lambda})$, such that $X'_{0} = X'_{0\lambda}
\times_{S_{\lambda}} S$ `(8.6.3)`; one has, for $\lambda \geq \alpha$, $\dim(X'_{0\lambda}) = \dim(X'_{0}) \leq 1$ by
transitivity of fibres and `(4.1.4)`. It is a matter of seeing that if one has proved that the homomorphism
$\operatorname{Pic}(X_{\lambda}) \to \operatorname{Pic}(X'_{0\lambda})$ is surjective for every $\lambda \geq \alpha$,
then it is the same for $\operatorname{Pic}(X) \to \operatorname{Pic}(X'_{0})$. One evidently has the commutative
diagram of canonical homomorphisms

```text
                         Pic(X_λ) ──→ Pic(X)
                              │           │
                              ↓           ↓
                         Pic(X'_{0λ}) ─→ Pic(X'_0)
```

For every invertible $\mathcal{O}_{X'_{0}}$-Module $\mathcal{L}'_{0}$, there exist a $\lambda \geq \alpha$ and an
invertible $\mathcal{O}_{X'_{0\lambda}}$-Module $\mathcal{L}'_{0\lambda}$ such that $\mathcal{L}'_{0}$ is deduced from
it by the base change $S \to S_{\lambda}$ `(8.5.2` and `8.5.5)`; it suffices to

<!-- original page 289 -->

consider an invertible $\mathcal{O}_{X_{\lambda}}$-Module $\mathcal{L}_{\lambda}$ such that
$cl(\mathcal{L}'_{0\lambda})$ is the image of $cl(\mathcal{L}_{\lambda})$ in $\operatorname{Pic}(X'_{0\lambda})$, then
to take the invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ deduced from $\mathcal{L}_{\lambda}$ by the base change;
in virtue of the commutativity of the preceding diagram, $cl(\mathcal{L}'_{0})$ will be the image of $cl(\mathcal{L})$.

Therefore assume $A$ Noetherian, hence so is $X$, and verify that $X$ and $X'_{0}$ satisfy the conditions of
`(21.9.11, (ii))`. One has by hypothesis $\dim(X'_{0}) \leq 1$; on the other hand, to verify condition 2° of
`(21.9.11)`, consider a subprescheme $Y$ of $X$ having $Y$ as underlying set; the morphism $g : Y \to S$, restriction of
$f$, being quasi-finite at each of the points $x_{i}$ of $Y \cap X_{0}$ ($1 \leq i \leq n$), one may apply
`(18.5.11, c)` and one sees that $Y$ is the sum of the open subpreschemes $Y_{i} =
\operatorname{Spec}(\mathcal{O}_{Y,x_{i}})$ ($1 \leq i \leq n$) and of a prescheme `Y''` such that $Y'' \cap X_{0} =
\emptyset$, and moreover the canonical injections $j_{i} : Y_{i} \to X$ are such that $f \circ j_{i}$ is a finite
morphism. Since $f$ is separated, $j_{i}$ is also a finite morphism, so $Y_{i}$ is closed in $X$; one therefore answers
the question by taking $Y' = \bigcup_{1 \leq i \leq n} Y_{i}$.

It remains to verify the supplementary hypothesis of `(21.9.11, (ii))`. Now, $X'_{0}$ being a separated curve over the
field $k(s_{0})$, is a quasi-projective $k(s_{0})$-scheme (chap. V) [^1], so there exists an ample
$\mathcal{O}_{X'_{0}}$-Module `(II, 5.3.1)`, and this completes the proof.

**Remark (21.9.13).**

<!-- label: IV.21.9.13 -->

Under the conditions of `(21.9.12)`, assuming moreover $f$ proper, the morphism $f$ is even projective: indeed, if
$\mathcal{L}'_{0}$ is an ample $\mathcal{O}_{X'_{0}}$-Module, there exists, in virtue of `(21.9.12)`, an invertible
$\mathcal{O}_{X}$-Module $\mathcal{L}$ whose inverse image in $X'_{0}$ is isomorphic to $\mathcal{L}'_{0}$, hence is
ample. Since every neighbourhood of $s_{0}$ in $S$ is necessarily all of $S$, one then deduces from `(9.6.4)` that
$\mathcal{L}$ is an ample $\mathcal{O}_{X}$-Module, whence the conclusion `(II, 5.3.1` and `II, 5.5.3)`.

### 21.10. Inverse images and direct images of 1-codimensional cycles

In a later chapter, devoted to intersection theory, the notions of inverse image and direct image of cycles will be
developed systematically. In the present number, we content ourselves with defining these notions in certain useful
particular cases, and for *1-codimensional* cycles, these definitions being chosen so that they are compatible with the
corresponding definitions for divisors `(21.4` and `21.5)`, taking account of the homomorphism `cyc` defined in
`(21.6)`.

**(21.10.1).** Let $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ a morphism, $T$ a part of $X$; assume
that the image under $f$ of every maximal point of $X'$ is a maximal point of $X$, and that, for every $x' \in X'^{(1)}$
(i.e. such that $\dim(\mathcal{O}_{X',x'}) = 1$), one has *one* of the three following conditions for the point $x =
f(x')$:

(i) $x \notin T$;

(ii) $x \in X^{(1)}$ and $\mathcal{O}_{X',x'}$ is a flat $\mathcal{O}_{X,x}$-module;

(iii) the ring $\mathcal{O}_{X,x}$ is factorial and $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X',x'})$.

Under these conditions, we propose, for every 1-codimensional cycle $Z$ on $X$ with support contained in $T$, to define
a 1-codimensional cycle $Z' = f^{*}(Z)$, so

<!-- original page 290 -->

that $Z \mapsto f^{*}(Z)$ is a homomorphism of ordered groups from the subgroup of $\mathfrak{J}^{1}(X)$ formed by
cycles with support contained in $T$ to the ordered group $\mathfrak{J}^{1}(X')$. For this, let

```text
  (21.10.1.1)            Z = ∑_{x ∈ T ∩ X^{(1)}} n_x · {x}
```

where the family of $x \in T \cap X^{(1)}$ such that $n_{x} \neq 0$ is locally finite. For every $x' \in X'^{(1)}$, let
us define an integer $n_{x'}$ in the following way, setting $x = f(x')$:

1° if $x \notin T$, take $n_{x'} = 0$;

2° if $x \in X^{(1)}$ and $\mathcal{O}_{X',x'}$ is a flat $\mathcal{O}_{X,x}$-module, one knows `(6.1.1)` that
$\dim(\mathcal{O}_{X',x'} / \mathfrak{m}_{x} \mathcal{O}_{X',x'}) = 0$; in other words $\mathcal{O}_{X',x'} /
\mathfrak{m}_{x} \mathcal{O}_{X',x'}$ is an $\mathcal{O}_{X',x'}$-module of finite length $\lambda_{x'}$, and one takes
$n_{x'} = \lambda_{x'} n_{x}$;

3° if $\mathcal{O}_{X,x}$ is factorial and $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X',x'})$, one knows `(21.6.9)` that
the canonical homomorphism `cyc : Div(𝒪_{X,x}) → 𝔍^1(Spec(𝒪_{X,x}))` is bijective, and on the other hand since
$\dim(\mathcal{O}_{X',x'}) = 1$ and $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X',x'})$, $Ass(\mathcal{O}_{X',x'})$
consists solely of the maximal points of $\operatorname{Spec}(\mathcal{O}_{X',x'})$, so the hypothesis on $f$ implies
that $f(Ass(\mathcal{O}_{X',x'})) \subset Ass(\mathcal{O}_{X,x})$, and it follows from `(21.4.5, (ii))` that the
homomorphism $f^{*} : \operatorname{Div}(\mathcal{O}_{X,x}) \to \operatorname{Div}(\mathcal{O}_{X',x'})$ is defined;
finally, $x'$ being the unique closed point of $\operatorname{Spec}(\mathcal{O}_{X',x'})$,
$\mathfrak{J}^{1}(\operatorname{Spec}(\mathcal{O}_{X',x'}))$ is canonically isomorphic to $\mathbb{Z}$. One has
therefore a composite canonical homomorphism

```text
                                    cyc⁻¹              f^*                cyc
  (21.10.1.2)            𝔍^1(Spec(𝒪_{X,x})) ─→ Div(𝒪_{X,x}) ─→ Div(𝒪_{X',x'}) ─→ 𝔍^1(Spec(𝒪_{X',x'})) ⥲ ℤ.
```

If $Z_{x}$ is the cycle $\sum_{y \in \operatorname{Spec}(\mathcal{O}_{X,x}) \cap X^{(1)}} n_{y} \cdot ({y} \cap
\operatorname{Spec}(\mathcal{O}_{X,x}))$ on $\operatorname{Spec}(\mathcal{O}_{X,x})$, one takes for $n_{x'}$ the image
of $Z_{x}$ under the homomorphism `(21.10.1.2)`.

**(21.10.2).** We propose to show that:

A) When two of the conditions 1°, 2°, 3° of `(21.10.1)` are simultaneously satisfied, the corresponding values of
$n_{x'}$ coincide.

B) The set of $x' \in X'^{(1)}$ such that $n_{x'} \neq 0$ is locally finite in $X'$.

To prove A), assume first that $x \notin T$ and that $x$ verifies one of conditions 2° or 3° of `(21.10.1)`; then $n_{x}
= 0$ and if one is in case 2°, one has $n_{x'} = 0$; if one is in case 3°, one has $Z_{x} = 0$ since $Supp(Z) \subset
T$, so again $n_{x'} = 0$. It remains to consider the case where one is at once in case 2° and in case 3°; then, since
$\dim(\mathcal{O}_{X,x}) = 1$, $\mathcal{O}_{X,x}$ is a discrete valuation ring; if $t$ is a uniformizer of this ring,
the divisor corresponding to $Z_{x}$ is $div(t^{n_{x}})$ in $\operatorname{Div}(\mathcal{O}_{X,x})$, and its image in
$\operatorname{Div}(\mathcal{O}_{X',x'})$ is the divisor of $t'^{n_{x}}$, where $t'$ is the (regular) element of
$\mathcal{O}_{X',x'}$ image of $t$. One may evidently restrict to the case where $n_{x} = 1$, and then the definition
`(21.6.5.1)` shows that the image of $Z_{x}$ under `(21.10.1.1)` is the number $\lambda_{x'}$, which completes the proof
of A).

Let us now prove B). Set $T_{0} = Supp(Z) \subset T$, $T'_{0} = f^{-1}(T_{0})$; it suffices to prove that the relation
$n_{x'} \neq 0$ implies that $x'$ belongs to the set of maximal points of $T'_{0}$, the latter being locally finite in
$X'$. It is immediate that one necessarily has $x' \in T'_{0}$; if $x'$ were not maximal in the closed set $T'_{0}$,
there would exist a generization $y'$ of $x'$ in $T'_{0}$, distinct from $x'$, and since $x' \in X'^{(1)}$, $y'$ would
necessarily

<!-- original page 291 -->

be a maximal point of $X'$; consequently $y = f(y')$ would be a maximal point of $X$ by hypothesis; but this is absurd
since $y \in T_{0}$ and `T_0` is purely of codimension `1` in $X$.

**(21.10.3).** One can now set

```text
                         f^*(Z) = ∑_{x' ∈ X'^{(1)}} n_{x'} · {x'},
```

the sum on the right-hand side making sense in virtue of what was proved in `(21.10.2)`; one says that the
1-codimensional cycle $f^{*}(Z)$ is the *inverse image* of $Z$ under $f$. It is immediate that the map $f^{*}$ thus
defined is a homomorphism of ordered groups. Moreover, if $U$ is an open of $X$, $V$ an open of $X'$ such that $f(V)
\subset U$, and $f' : V \to U$ the restriction of $f$, it follows at once from the definitions that one has

```text
  (21.10.3.1)            f'^*(Z | U) = f^*(Z) | V.
```

Denote by $\Gamma_{T}(\mathfrak{J}^{1}_{X})$ the largest subsheaf of commutative groups of $\mathfrak{J}^{1}_{X}$ with
support contained in $T$; it follows from relation `(21.10.3.1)` that the maps $\Gamma(U,
\Gamma_{T}(\mathfrak{J}^{1}_{X})) \to \Gamma(V, \mathfrak{J}^{1}_{X'})$ just defined determine a homomorphism of sheaves
of ordered commutative groups on $X'$

$$ \psi^{*}(\Gamma_{T}(\mathfrak{J}^{1}_{X})) \to \mathfrak{J}^{1}_{X'} $$

where $\psi$ is the continuous map underlying the morphism $f$.

**Proposition (21.10.4).**

<!-- label: IV.21.10.4 -->

*Assume the conditions of `(21.10.1)` are verified. Then, for every divisor $D$ on $X$ such that $Supp(D) \subset T$ and
that $f^{*}(D)$ is defined `(21.4.2)`, one has*

$$ (21.10.4.1) cyc(f^{*}(D)) = f^{*}(cyc(D)). $$

The question being local on $X$, one may restrict to the case where $X = \operatorname{Spec}(A)$ is affine, $D =
div(t)$, $t$ a regular non-invertible element of $A$, and where the subprescheme $Y(D)$ `(21.2.12)` has a single maximal
point $y$, so that $cyc(D) = n_{y} \cdot {y}$, where $n_{y}$ is the length of $\mathcal{O}_{X,y} / t \mathcal{O}_{X,y}$
`(21.6.5.1)`. One saw in the proof of `(21.10.2, B)` that the points $x' \in X'$ such that $mult_{x'}(f^{*}(cyc(D)))
\neq 0$ are maximal points of $f^{-1}({y})$. If the point $x'$ is in case 3° of `(21.10.1)`, the equality of the
multiplicities at $x'$ of the two members of `(21.10.4.1)` follows from the definition of $n_{x'}$ by means of the
homomorphism `(21.10.1.1)`. Suppose on the contrary that $x'$ is in case 2° of `(21.10.1)`, and let $x = f(x')$; since
$x \in X^{(1)} \cap {y}$, one necessarily has $x = y$. Let us remark now that $f^{*}(D) = div(t')$, where $t'$ is the
image of $t$ in $\Gamma(X', \mathcal{O}_{X'})$, and $Y(f^{*}(D)) = f^{-1}(Y(D))$; the multiplicity of $f^{*}(D)$ at the
point $x'$ is therefore the length $n_{x'}$ of the $\mathcal{O}_{X',x'}$-module $\mathcal{O}_{X',x'} / t'
\mathcal{O}_{X',x'}$; since $\mathcal{O}_{X',x'} / t' \mathcal{O}_{X',x'} = (\mathcal{O}_{X,y} / t \mathcal{O}_{X,y})
\otimes_{\mathcal{O}_{X,y}} \mathcal{O}_{X',x'}$, it follows from `(4.7.1)` that one has $n_{x'} = \lambda_{x'} n_{y}$,
so the multiplicities at $x'$ of the two members of `(21.10.4.1)` are again equal, which completes the proof.

**(21.10.5).** Suppose now that $f : X' \to X$ is a morphism of locally Noetherian preschemes, sending every maximal
point of $X'$ to a maximal point of $X$, and suppose in addition that for every rare closed part $T$ of $X$, $f$
verifies the conditions

<!-- original page 292 -->

of `(21.10.1)`; this means again that for every $x' \in X'^{(1)}$, either $x = f(x')$ is a maximal point of $X$, or $x'$
verifies one of conditions (ii), (iii) of `(21.10.1)`. If one takes into account that every 1-codimensional cycle has
rare support in $X$, one sees that $f^{*}(Z)$ is defined for every 1-codimensional cycle $Z$ on $X$; in virtue of
`(21.10.3.1)`, one has thus defined a homomorphism of sheaves of ordered commutative groups

$$ \psi^{*}(\mathfrak{J}^{1}_{X}) \to \mathfrak{J}^{1}_{X'}. $$

If, moreover, for every divisor $D$ on $X$, $f^{*}(D)$ is defined `(21.4.5)`, the fact that the support of $D$ is rare
in $X$ `(21.6.6)` entails that `(21.10.4)` is applicable, and one therefore has the formula `(21.10.4.1)` for every
divisor $D$ on $X$. In particular:

**Proposition (21.10.6).**

<!-- label: IV.21.10.6 -->

*Let $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ a flat morphism. Then $f^{*}(Z)$ is defined for
every 1-codimensional cycle $Z$ on $X$, $f^{*}(D)$ is defined for every divisor $D$ on $X$, and one has relation
`(21.10.4.1)`.*

Indeed, if $x' \in X'^{(1)}$ is such that $x = f(x')$ is not maximal, it follows from `(6.1.1)` that one necessarily has
$x \in X^{(1)}$, so one is in case (ii) of `(21.10.1)`. One may therefore apply `(21.10.5)`, taking account of
`(21.4.5)` and `(2.3.4)`.

**Remark (21.10.7).**

<!-- label: IV.21.10.7 -->

The existence of $f^{*}(Z)$ for every 1-codimensional cycle $Z$ on $X$ already follows from the hypothesis that $f$ is
flat at the points $x'$ of $X'$ of codimension $\leq 1$ in $X'$ (i.e. such that $\dim(\mathcal{O}_{X',x'}) \leq 1$);
indeed, for every maximal point $x' \in X'$, it follows from `(6.1.1)` that $x = f(x')$ is a maximal point of $X$ since
$\dim(\mathcal{O}_{X,x}) \leq \dim(\mathcal{O}_{X',x'}) = 0$. Similarly, if $x' \in X'^{(1)}$, $x = f(x')$ is maximal or
belongs to $X^{(1)}$ by `(6.1.1)`; one can therefore again apply `(21.10.5)`.

**Proposition (21.10.8).**

<!-- label: IV.21.10.8 -->

*Let $X$, $X'$, `X''` be three locally Noetherian preschemes, $f : X' \to X$, $g : X'' \to X'$ two morphisms; assume
that $f$ (resp. $g$) is flat at every point of codimension $\leq 1$ in $X'$ (resp. `X''`). Then $f \circ g$ is flat at
every point of codimension $\leq 1$ in `X''` and for every 1-codimensional cycle $Z$ on $X$, one has $(f \circ g)^{*}(Z)
= g^{*}(f^{*}(Z))$.*

The first assertion follows from `(6.1.1)` and `(2.1.6)`. The second results from the fact that $f$ (resp. $g$, resp. $f
\circ g$) sends maximal points of $X'$ (resp. `X''`, resp. `X''`) to maximal points of $X$ (resp. $X'$, resp. $X$), and
that, if $x'' \in X''^{(1)}$ is such that $x' = g(x'') \in X'^{(1)}$ and $x = f(x') \in X^{(1)}$, one has

```text
                  long(𝒪_{X'',x''} / 𝔪_x 𝒪_{X'',x''}) = long(𝒪_{X'',x''} / 𝔪_{x'} 𝒪_{X'',x''}) · long(𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}).
```

Indeed, setting $A = \mathcal{O}_{X,x}$, $A' = \mathcal{O}_{X',x'}$, $A'' = \mathcal{O}_{X'',x''}$, $\mathfrak{m} =
\mathfrak{m}_{x}$, $\mathfrak{m}' = \mathfrak{m}_{x'}$, one has $A'' / \mathfrak{m} A'' = (A' / \mathfrak{m} A')
\otimes_{A'} A''$, and the formula

```text
                         long_{A''}(A'' / 𝔪 A'') = long_{A'}(A' / 𝔪 A') · long_{A''}(A'' / 𝔪' A'')
```

follows from `(4.7.1)` and from the flatness hypothesis of `A''` over $A'$.

**(21.10.9).** Let $X$ be a locally Noetherian prescheme, $\Lambda$ a commutative group, written additively and
therefore considered as a $\mathbb{Z}$-module; one will denote again by $\mathbb{Z}$ and $\Lambda$ the simple sheaves on
$X$ associated to the constant presheaves equal respectively to $\mathbb{Z}$ and $\Lambda$ $(0_{I}, 3.6)$. The sheaf of
commutative groups $\mathfrak{J}^{1}_{X} \otimes_{\mathbb{Z}} \Lambda$ is called the *sheaf of germs of 1-codimensional
cycles with coefficients in $\Lambda$*. If $\Lambda = \mathbb{Q}$, one says that the sections of

<!-- original page 293 -->

$\mathfrak{J}^{1}_{X} \otimes_{\mathbb{Z}} \mathbb{Q}$ over $X$ are the *1-codimensional cycles with rational
coefficients*. Since the stalks of $\mathfrak{J}^{1}_{X}$ are torsion-free $\mathbb{Z}$-modules `(21.6.3)`, the
canonical homomorphism $\mathfrak{J}^{1}_{X} \to \mathfrak{J}^{1}_{X} \otimes_{\mathbb{Z}} \mathbb{Q}$ is injective, so
1-codimensional cycles are identified with 1-codimensional cycles with rational coefficients.

**(21.10.10).** We are going to see that under certain conditions, one may broaden the definition of $f^{*}(Z)$ given in
`(21.10.3)` for a 1-codimensional cycle $Z$ on $X$, but on condition of taking for $f^{*}(Z)$ a 1-codimensional cycle
with rational coefficients on $X'$. The more general case in which we place ourselves is that where $f$ sends every
maximal point of $X'$ to a maximal point of $X$, and where, at every point $x' \in X'^{(1)}$, one has one of conditions
(i), (ii), (iii) of `(21.10.1)` or a fourth condition (setting $x = f(x')$):

(iv) $x \in X^{(1)}$, $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X,x})$, and moreover, if one sets $A =
\hat{\mathcal{O}}_{X,x}$, $A' = \hat{\mathcal{O}}_{X',x'}$, and if $K$ denotes the total ring of fractions of $A$, then
$A'$ is a finite $A$-algebra and $K' = A' \otimes_{A} K$ is a free $K$-module.

Let us denote then by $r_{x'}$ the rank of the free $K$-module $K'$, by $q_{x'}$ the degree of $k(x') = k(A')$ over
$k(x) = k(A)$, and set $\mu_{x'} = r_{x'} / q_{x'}$. For a 1-codimensional cycle with support contained in $T$, given by
`(21.10.1.1)`, and every $x' \in X'^{(1)}$, one defines $c_{x'} \in \mathbb{Q}$ as equal to the number $n_{x'} \in
\mathbb{Z}$ when one is in one of cases 1°, 2°, 3° of `(21.10.1)`; but there remains here a fourth possibility:

4° if $x'$ verifies condition (iv) above, take $c_{x'} = \mu_{x'} n_{x} \in \mathbb{Q}$.

**(21.10.11).** It remains to prove that when condition 4° of `(21.10.10)` is verified simultaneously with one of
conditions 1°, 2°, 3° of `(21.10.1)`, one has $n_{x'} = c_{x'}$. This is evident if $x \notin T$ since then $n_{x} = 0$.
To study the two other cases, note that $\mathfrak{m}_{x} \mathcal{O}_{X',x'}$ is closed for the
$\mathfrak{m}_{x'}$-preadic topology, so the completion of $\mathcal{O}_{X',x'} / \mathfrak{m}_{x} \mathcal{O}_{X',x'}$
for the latter topology is $A' / \mathfrak{m}_{x} A'$. If one is at once in case 2° and case 4°, $\mathcal{O}_{X',x'} /
\mathfrak{m}_{x} \mathcal{O}_{X',x'}$ is discrete for the $\mathfrak{m}_{x'}$-preadic topology, so isomorphic to $A' /
\mathfrak{m}_{x} A'$. Since $A'$ is a finite and flat $A$-algebra $(0_{III}, 10.2.3)$, it is a free $A$-module
$(0_{III}, 10.1.3)$, and the rank of $A' / \mathfrak{m}_{x} A'$ over $A / \mathfrak{m}_{x} A = k(x)$ is equal to the
rank of $A'$ over $A$, hence also to that of $K'$ over $K$. On the other hand, this rank is also equal to the product of
the length $\lambda_{x'}$ of $\mathcal{O}_{X',x'} / \mathfrak{m}_{x} \mathcal{O}_{X',x'}$ (as
$\mathcal{O}_{X',x'}$-module, or as $k(x')$-module) by the rank $[k(x') : k(x)] = q_{x'}$, which proves the relation
$\mu_{x'} = r_{x'} / q_{x'} = \lambda_{x'}$ in this case.

Assume finally that one is at once in case 3° and case 4°. Then, since $\dim(\mathcal{O}_{X,x}) = 1$,
$\mathcal{O}_{X,x}$ is a discrete valuation ring, hence regular. On the other hand, $\mathcal{O}_{X',x'}$ is of
dimension `1`, and since $\mathfrak{m}_{x} \notin Ass(\mathcal{O}_{X',x'})$, $\mathcal{O}_{X',x'}$ is a Cohen-Macaulay
ring `(0, 16.4.6)`; finally, since $A'$ is an $A$-module of finite type, $A' / \mathfrak{m}_{x} A'$ is a $k(x)$-vector
space of finite rank; since $\mathcal{O}_{X',x'} / \mathfrak{m}_{x} \mathcal{O}_{X',x'}$ is contained in $A' /
\mathfrak{m}_{x} A'$, it is also a $k(x)$-vector space of finite rank, hence an Artinian ring. Applying `(6.1.5)` then
shows that $\mathcal{O}_{X',x'}$ is a flat $\mathcal{O}_{X,x}$-module, so one is also in case 2°, and one concludes by
what was seen above.

This being so, in the case under consideration, one will set

```text
                         f^*(Z) = ∑_{x' ∈ X'^{(1)}} c_{x'} · {x'}
```

<!-- original page 294 -->

which is therefore a 1-codimensional cycle on $X'$ with rational coefficients. One has again defined in this way a
homomorphism $f^{*}$ of ordered groups, satisfying `(21.10.3.1)`, and consequently a homomorphism of sheaves of
commutative groups

```text
                         ψ^*(Γ_T(𝔍^1_X)) → 𝔍^1_{X'} ⊗_ℤ ℚ.
```

When $f$ verifies the preceding conditions for every closed part $T$ rare in $X$, that is, when for every $x' \in
X'^{(1)}$, either $x = f(x')$ is a maximal point of $X$, or $x'$ verifies one of conditions (ii), (iii) or (iv),
$f^{*}(Z)$ is then defined for every 1-codimensional cycle $Z$ on $X$, and one has defined a homomorphism of sheaves of
ordered commutative groups

```text
                         ψ^*(𝔍^1_X) → 𝔍^1_{X'} ⊗_ℤ ℚ
```

whence, by tensorization, a homomorphism of sheaves of ordered $\mathbb{Q}$-vector spaces

```text
  (21.10.11.1)           ψ^*(𝔍^1_X ⊗_ℤ ℚ) → 𝔍^1_{X'} ⊗_ℤ ℚ.
```

**Remark (21.10.12).**

<!-- label: IV.21.10.12 -->

When one is in the situation of `(21.10.10)`, one may effectively, for 1-codimensional cycles $Z$ on $X$, have for
$f^{*}(Z)$ 1-codimensional cycles with *non-integral* coefficients; in other words, the numbers $\mu_{x'}$ may be non-
integers. One has an example by taking the complete integral ring $A$ of `(6.15.11, (ii))` and its integral closure
$A'$: the closed point $x'$ of $\operatorname{Spec}(A')$ verifies condition (iv) of `(21.10.10)` and one has $\mu_{x'} =
1/2$.

**Lemma (21.10.13).**

<!-- label: IV.21.10.13 -->

*Let $A$ be a Noetherian local ring of dimension `1`, $t$ a regular element of $A$ belonging to the maximal ideal
$\mathfrak{m}$ (which implies that $\mathfrak{m} \notin Ass(A)$).*

*(i) For every $A$-module $M$ of finite type, the kernel $N_{t}(M)$ and cokernel $P_{t}(M)$ of the homothety $t_{M} : M
\to M$ of ratio $t$ are of finite length. One sets $d_{t}(M) = long P_{t}(M) - long N_{t}(M)$.*

*(ii) If $0 \to M' \to M \to M'' \to 0$ is an exact sequence of $A$-modules of finite type, one has $d_{t}(M) =
d_{t}(M') + d_{t}(M'')$.*

*(iii) One has $d_{t}(M) \geq 0$ for every $A$-module $M$ of finite type; for $d_{t}(M) = 0$ to hold, it is necessary
and sufficient that $M$ be of finite length.*

*(iv) If $K$ is the total ring of fractions of $A$ and if $M \otimes_{A} K$ is a free $K$-module of rank $n$, one has
$d_{t}(M) = n \cdot d_{t}(A) = n \cdot long(A / tA)$.*

*(v) If $M$ verifies the hypotheses of (iv) and moreover $t$ is $M$-regular, one has $long(M / tM) = n \cdot long(A /
tA)$.*

(i) $\operatorname{Spec}(A)$ consists of the point $\mathfrak{m}$ and the minimal prime ideals $\mathfrak{p}_{i}$; since
by hypothesis $t \notin \mathfrak{p}_{i}$ for every $i$ (Bourbaki, _Alg. comm._, chap. IV, §1, n° 1, cor. 3 of prop. 2),
the image of $t$ in each of the $A_{\mathfrak{p}_{i}}$ is invertible, and the supports of the $A$-modules of finite type
$N_{t}(M)$ and $P_{t}(M)$ are therefore empty or reduced to $\mathfrak{m}$; one concludes `(0, 16.1.10)` that these
modules are of finite length.

(ii) Since $t$ is regular, one has an exact sequence

```text
                              t_A
                         0 → A ─→ A → A / tA → 0
```

<!-- original page 295 -->

and since $Tor^{A}_{i}(M, A) = 0$ for $i \geq 1$, the exact sequence of `Tor` gives on the one hand the exact sequence

```text
                                                          t_M
                         0 → Tor_1^A(M, A / tA) → M ─→ M → M / tM → 0
```

and on the other, for $i \geq 2$,

```text
                         0 = Tor_i^A(M, A) → Tor_i^A(M, A / tA) → Tor_{i-1}^A(M, A) = 0
```

so one has $N_{t}(M) = Tor^{A}_{1}(M, A / tA)$ and $Tor^{A}_{i}(M, A / tA) = 0$ for $i \geq 2$; the exact sequence of
`Tor` gives an exact sequence

```text
  0 → Tor_1^A(M', A / tA) → Tor_1^A(M, A / tA) → Tor_1^A(M'', A / tA) →
                              M' ⊗_A (A / tA) → M ⊗_A (A / tA) → M'' ⊗_A (A / tA) → 0
```

and this sequence is written, by the foregoing,

```text
  0 → N_t(M') → N_t(M) → N_t(M'') → P_t(M') → P_t(M) → P_t(M'') → 0
```

which proves (ii).

To prove (iii), note that there is a composition series $(M_{k})$ of $M$ whose quotients $M_{k} / M_{k+1}$ are
isomorphic to $A / \mathfrak{m}$ or to one of the $A / \mathfrak{p}_{i}$ (Bourbaki, _Alg. comm._, chap. IV, §1, n° 4,
th. 1), and for $M$ to be of finite length, it is necessary and sufficient that all these quotients be isomorphic to $A
/ \mathfrak{m}$. Everything therefore reduces (in virtue of (ii)) to proving that $d_{t}(A / \mathfrak{m}) = 0$ and
$d_{t}(A / \mathfrak{p}_{i}) > 0$. Now, the image of $t$ in $A / \mathfrak{m}$ being `0`, one has $N_{t}(A /
\mathfrak{m}) = A / \mathfrak{m}$ and $P_{t}(A / \mathfrak{m}) = A / \mathfrak{m}$, whence the first assertion; on the
other hand, the image of $t$ in $A / \mathfrak{p}_{i}$ is regular, so $N_{t}(A / \mathfrak{p}_{i}) = 0$ and $P_{t}(A /
\mathfrak{p}_{i}) = A / (tA + \mathfrak{p}_{i})$, which is not reduced to `0`, whence the second assertion.

(iv) There is a basis of $M \otimes_{A} K$ of the form $(x_{j} / s)_{1 \leq j \leq n}$, where $s$ is a regular element
of $A$ and $x_{j} \in M$. Consider the homomorphism $u : A^{n} \to M$ which sends the element $e_{j}$ ($1 \leq j \leq
n$) of the canonical basis of $A^{n}$ to $x_{j}$, and let us show that $Ker(u)$ and $Coker(u)$ are of finite length;
indeed, for every $i$, the image of $s$ in $A_{\mathfrak{p}_{i}}$ is invertible, and since $K_{\mathfrak{p}_{i}} =
A_{\mathfrak{p}_{i}}$, the images of the $x_{j} / s$ in $M_{\mathfrak{p}_{i}}$ form a basis of this
$A_{\mathfrak{p}_{i}}$-module; so $u_{\mathfrak{p}_{i}} : A^{n}_{\mathfrak{p}_{i}} \to M_{\mathfrak{p}_{i}}$ is
bijective. As in (i), one concludes that the supports of $Ker(u)$ and $Coker(u)$ are contained in ${\mathfrak{m}}$, so
that these modules are of finite length. This being so, it follows from (ii) and (iii) that one has $d_{t}(M) =
d_{t}(A^{n}) = n \cdot d_{t}(A) = n \cdot long(A / tA)$ since $t$ is regular.

Finally, it is clear that (v) is at once deduced from (iv), since then $N_{t}(M) = 0$.

This lemma allows one to generalize `(21.10.4)`:

**Proposition (21.10.13).**

<!-- label: IV.21.10.13bis -->

*Assume that $f$ verifies the conditions of `(21.10.10)`. Then, for every divisor $D$ on $X$ such that $Supp(D) \subset
T$ and that $f^{*}(D)$ is defined, one has*

$$ (21.10.13.1) cyc(f^{*}(D)) = f^{*}(cyc(D)). $$

Reasoning as in `(21.10.4)`, everything reduces to seeing (with the same notation) that if $x'$ is in case 4° of
`(21.10.10)` and if $n_{y}$ is the length of $\mathcal{O}_{X,y} / t \mathcal{O}_{X,y}$, then the

<!-- original page 296 -->

length $n_{x'}$ of $\mathcal{O}_{X',x'} / t' \mathcal{O}_{X',x'}$ is equal to $\mu_{x'} n_{y}$, $\mu_{x'}$ being the
rational number defined in `(21.10.10)`. Since $\mathcal{O}_{X',x'} / t' \mathcal{O}_{X',x'}$ is of finite length, it
has the same length as its $\mathfrak{m}_{x'}$-preadic completion $A' / t' A'$, which one may also write $A' / t_{y}
A'$; moreover, since $t'$ is regular by hypothesis in $\mathcal{O}_{X',x'}$, $t_{y}$ is also regular in $A'$ by flatness
$(0_{I}, 6.3.4)$, and when $A'$ is considered as $A$-module, one may also say that $t$ is $A'$-regular. Since $A$ is of
dimension `1` and $A'$ is an $A$-module of finite type such that $A' \otimes_{A} K$ is a free $K$-module of rank
$r_{x'}$, one may apply `(21.10.13, (v))` to $M = A'$ and to $t$, and the length of $A' / t_{y} A'$ as $K$-module is
therefore $r_{x'} n_{y}$. Since $k(x')$ is a $k(x)$-vector space of rank $q_{x'}$, the length of $A' / t' A'$ as
$A'$-module is therefore $r_{x'} n_{y} / q_{x'} = \mu_{x'} n_{y}$, which completes the proof.

**(21.10.14).** Let now $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ a morphism having the *two*
following properties:

a) $f$ is finite;

b) the image under $f$ of every maximal point of $X'$ is a maximal point of $X$.

For every $x \in X^{(1)}$, the points $x' \in f^{-1}(x)$ all belong to $X'^{(1)}$, as follows from hypothesis b) and the
inequality `(0, 16.3.9.1)`, the fibre $f^{-1}(x)$ being discrete. Let then

```text
                         Z' = ∑_{x' ∈ X'^{(1)}} n_{x'} · {x'}
```

be a 1-codimensional cycle on $X'$. For every $x \in X^{(1)}$, let us define an integer $n_{x}$ by the formula

```text
                         n_x = ∑_{x' ∈ f⁻¹(x)} n_{x'} · [k(x') : k(x)]
```

which makes sense, the points of $f^{-1}(x)$ being finite in number and $k(x')$ being a field of finite degree over
$k(x)$ `(I, 6.4.4)`. Moreover, the set of $x \in X^{(1)}$ such that $n_{x} \neq 0$ is locally finite in $X$, since it is
contained in the image under $f$ of the set of $x' \in X'^{(1)}$ such that $n_{x'} \neq 0$, and the conclusion follows
from the fact that the morphism $f$ is quasi-compact. One may thus define a 1-codimensional cycle on $X$ by setting

```text
  (21.10.14.1)           f_*(Z') = ∑_{x ∈ X^{(1)}} n_x · {x}
```

and one says that $f_{*}(Z')$ is the *direct image* of $Z'$ under $f$. It is clear that the map $f_{*} :
\mathfrak{J}^{1}(X') \to \mathfrak{J}^{1}(X)$ thus defined is a homomorphism of ordered groups. Moreover, if $U$ is an
open of $X$, $f_{U} : f^{-1}(U) \to U$ the restriction of $f$, it follows at once from the definitions that one has

```text
  (21.10.14.2)           (f_U)_*(Z' | f⁻¹(U)) = f_*(Z') | U
```

so, denoting by $\psi$ the continuous map underlying the morphism $f$, the maps $\Gamma(f^{-1}(U),
\mathfrak{J}^{1}_{X'}) \to \Gamma(U, \mathfrak{J}^{1}_{X})$ just defined determine a homomorphism of sheaves of ordered
commutative groups on $X$

$$ \psi_{*}(\mathfrak{J}^{1}_{X'}) \to \mathfrak{J}^{1}_{X}. $$

<!-- original page 297 -->

**Proposition (21.10.15).**

<!-- label: IV.21.10.15 -->

*Let $X$, $X'$, `X''` be three locally Noetherian preschemes, $f : X' \to X$, $g : X'' \to X'$ two morphisms verifying
conditions a) and b) of `(21.10.14)`. Then $f \circ g$ verifies the same conditions, and for every 1-codimensional cycle
`Z''` on `X''`, one has $(f \circ g)_{*}(Z'') = f_{*}(g_{*}(Z''))$.*

This follows at once from the definitions.

**Proposition (21.10.16).**

<!-- label: IV.21.10.16 -->

*Let $X$, $X'$, `X_1` be three locally Noetherian preschemes, $f : X' \to X$ a morphism verifying conditions a) and b)
of `(21.10.14)`, $g : X_{1} \to X$ a flat morphism. Set $X'_{1} = X' \times_{X} X_{1}$ (so that $X'_{1}$ is locally
Noetherian) and note $f_{1} : X'_{1} \to X_{1}$ and $g_{1} : X'_{1} \to X'$ the canonical projections. Then $f_{1}$
verifies conditions a) and b) of `(21.10.14)`, and for every 1-codimensional cycle $Z'$ on $X'$, one has*

$$ (21.10.16.1) g^{*}(f_{*}(Z')) = (f_{1})_{*}(g^{*}_{1}(Z')). $$

It is clear that $f_{1}$ is finite, and it verifies condition b) of `(21.10.14)` by virtue of `(2.3.7)`. To prove
`(21.10.16.1)`, one is at once reduced to the case where $X$, $X'$ and `X_1` are spectra of Noetherian local rings of
dimension `1`, $A$, $A'$ and `A_1`, with $A'$ a finite $A$-module and `A_1` a flat $A$-module. Denoting by $x$, $x'$ and
$x_{1}$ the closed points of $X$, $X'$ and `X_1` respectively, it is a matter of seeing that one has

```text
  (21.10.16.2)           ∑_{x'_1} λ_{x'_1}[k(x'_1) : k(x_1)] = λ_{x'}[k(x') : k(x)]
```

where $x'_{1}$ ranges over the set of closed points of $X'_{1}$ (i.e. the set of points lying above both $x'$ and
$x_{1}$) and where $\lambda_{x'} = long(\mathcal{O}_{X',x'} / \mathfrak{m}_{x} \mathcal{O}_{X',x'})$ and
$\lambda_{x_{1}} = long(A_{1} / \mathfrak{m}_{x} A_{1})$. Since one has

```text
                         [k(x'_1) : k(x_1)] · [k(x_1) : k(x)] = [k(x'_1) : k(x')] · [k(x') : k(x)]
```

the left-hand side of `(21.10.16.2)` is also written

```text
                         ([k(x') : k(x)] / [k(x_1) : k(x)]) · long_{A'}(A'_1 / 𝔪_{x'} A'_1) = long_{A_1}(A'_1 / 𝔪_x A'_1)
```

where one has set $A'_{1} = A' \otimes_{A} A_{1}$. One therefore has $A'_{1} / \mathfrak{m}_{x} A'_{1} = (A' /
\mathfrak{m}_{x} A') \otimes_{A} A_{1}$, and since `A_1` is a flat $A$-module, one has by `(4.7.1)`

```text
                         long_{A_1}(A'_1 / 𝔪_x A'_1) = long_A(A' / 𝔪_x A') · long_{A_1}(A_1 / 𝔪 A_1)
                                                    = [k(x') : k(x)] · λ_{x_1}
```

which completes the proof.

**Proposition (21.10.17).**

<!-- label: IV.21.10.17 -->

*Let $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ a finite locally free morphism. Then $f$ verifies
condition b) of `(21.10.14)`, and for every divisor $D'$ on $X'$, one has*

$$ (21.10.17.1) f_{*}(cyc(D')) = cyc(f_{*}(D')). $$

Since $f$ is flat and finite, condition b) of `(21.10.14)` and the relation $f(X'^{(1)}) \subset X^{(1)}$ follow from
`(6.1.1)`. The definition `(21.10.14.1)` shows that one may reduce to the case where $X = \operatorname{Spec}(A) =
\operatorname{Spec}(\mathcal{O}_{X,x})$ for an $x \in X^{(1)}$; then $X' = \operatorname{Spec}(A')$, where $A'$ is an

<!-- original page 298 -->

$A$-algebra which is a *free* $A$-module of finite rank; moreover, one may assume that $D' = div(t')$, where $t'$ is a
regular element of $A'$; one then has $f_{*}(D') = div(t)$, where $t = N_{A'/A}(t')$ is a regular element of $A$
`(21.5.2)`. One may restrict to the case where $t'$ is not invertible in $A'$, which is equivalent to $t$ not being
invertible in $A$; the ring $A / tA$ is then of finite length and $\neq 0$, and $A' / t' A'$ is a direct sum of Artinian
local rings $A'_{i}$ ($1 \leq i \leq r$), the residue field of $A'_{i}$ being $k(x'_{i})$, where $x'_{i}$ ($1 \leq i
\leq r$) are the points of $X'$ above $x$. If $t'_{i}$ ($1 \leq i \leq r$) is the image of $t'$ in $A'_{i}$, $A' / t'
A'$ is the direct sum of the $A'_{i} / t'_{i} A'_{i}$; since the product $long_{A'_{i}}(A'_{i} / t'_{i} A'_{i}) \cdot
[k(x'_{i}) : k(x)]$ equals $long_{A}(A'_{i} / t'_{i} A'_{i})$, one sees that the multiplicity at the point $x$ of the
left-hand side of `(21.10.17.1)` is $long_{A}(A' / t' A')$, so that the formula to prove reduces to

```text
  (21.10.17.2)           long_A(A' / t' A') = long_A(A / tA).
```

This relation follows from the more general following lemma:

**Lemma (21.10.17.3).**

<!-- label: IV.21.10.17.3 -->

*Let $A$ be a Noetherian local ring of dimension `1`, $M$ a free $A$-module of finite rank, $u$ an injective
endomorphism of $M$. Then one has*

```text
  (21.10.17.4)           long_A(Coker u) = long_A(A / (det u) A).
```

Let us distinguish several cases.

I) $A$ is a discrete valuation ring. Indeed, let $\pi$ be a uniformizer of $A$, and remark that $long_{A}(A / \pi^{k} A)
= k$; if $n$ is the rank of $M$ and $\pi^{m_{i}}$ ($1 \leq i \leq n$) are the invariant factors of $u$, $Coker(u)$ is
the direct sum of the $A$-modules $A / \pi^{m_{i}} A$, so has length $m = \sum^{n}_{i=1} m_{i}$, and $det(u)$ is the
product of an invertible element and $\pi^{m}$, whence the conclusion in this case (Bourbaki, _Alg._, chap. VII, §4, n°
5, cor. 1 of prop. 4).

II) $A$ is a complete integral ring (of dimension `1`). One knows then `(0, 19.8.8, (ii))` that there is a subring $B$
of $A$ which is a discrete valuation ring, such that $B \to A$ is a local homomorphism making $A$ a $B$-module of finite
type; since this $B$-module is evidently torsion-free, it is free (Bourbaki, _Alg. comm._, chap. VI, §3, n° 6, lemma 1).
Denote by $M'$ the set $M$ endowed with its (free) $B$-module structure, by $u'$ the endomorphism $u$ regarded as a
$B$-endomorphism. It follows from I) that one has

```text
  (21.10.17.5)           long_B(Coker u') = long_B(B / (det u') B).
```

But one has (Bourbaki, _Alg._, chap. VIII, §12, n° 2, prop. 7)

```text
                         det u' = N_{A/B}(det u),
```

hence, applying `(21.10.17.4)` to the homothety $x \mapsto (det u) x$ of the free $B$-module $A$, it comes

```text
                         long_B(B / (det u') B) = long_B(A / (det u) A),
```

whence, substituting in `(21.10.17.5)` and dividing by $[k(A) : k(B)]$, the length of the $B$-module $k(A)$, one obtains
`(21.10.17.4)` in the case envisaged.

<!-- original page 299 -->

III) $A$ is a complete ring. Note that one may suppose in addition that $\mathfrak{m} \notin Ass(A)$; indeed, since
$det(u)$ is a regular element of $A$, if one had $\mathfrak{m} \in Ass(A)$, one would deduce $det(u) \notin
\mathfrak{m}$, so $det(u)$ would be invertible, $u$ an automorphism of $M$, and the formula `(21.10.17.4)` becomes then
trivial, both members being zero.

In what follows, for an endomorphism $v$ of a module $N$ over a ring $R$, such that `Ker v` and `Coker v` be of finite
length, one will set

```text
                         χ(N, v) = long_R(Ker(v)) − long_R(Coker(v)).
```

One will note that the hypothesis on $v$ amounts to saying that the complex

```text
                                            v
                         K^0 : 0 → N ──→ N → 0
```

has its cohomology modules of finite length and that $\chi(N, v) = \chi(H^{0}(K^{0}))$ $(0_{III}, 11.10)$. One deduces
that if $N'$, $N$, `N''` are three $R$-modules, if one has a commutative diagram

```text
                                 r        s
                         0 → N' ─→ N ─→ N'' → 0
                              │     │     │
                              │v'   │v    │v''
                              ↓     ↓     ↓
                         0 → N' ─→ N ─→ N'' → 0
                                 r        s
```

whose rows are exact, and if two of the three numbers $\chi(N, v)$, $\chi(N', v')$ and $\chi(N'', v'')$ are defined,
then it is the same of the third and one has

```text
  (21.10.17.6)           χ(N, v) = χ(N', v') + χ(N'', v'').
```

This follows at once from the exact cohomology sequence.

Finally, if $N$ is an $R$-module of finite length, one has $\chi(N, v) = 0$.

With these notations, one has the following lemma:

**Lemma (21.10.17.7).**

<!-- label: IV.21.10.17.7 -->

*Let $A$ be a Noetherian local ring of dimension `1` whose maximal ideal $\mathfrak{m}$ is such that $\mathfrak{m}
\notin Ass(A)$; let $\mathfrak{p}_{i}$ ($1 \leq i \leq n$) be the minimal prime ideals of $A$. Let $M$ be a free
$A$-module of finite type, $u$ an endomorphism of $M$ such that $\chi(M, u)$ is defined; for each $i$, set $M_{i} = M
\otimes_{A} (A / \mathfrak{p}_{i})$ and let $u_{i}$ be the endomorphism $u \otimes 1_{A/\mathfrak{p}_{i}}$ of $M_{i}$;
then, if $\chi(M_{i}, u_{i})$ is defined for each $i$, one has*

```text
  (21.10.17.8)           χ(M, u) = ∑_{i=1}^n long(A_{𝔭_i}) · χ(M_i, u_i).
```

Since $\mathfrak{m} \notin Ass(A)$, one has a unique reduced primary decomposition $(0) = \bigcap_{1 \leq i \leq n}
\mathfrak{q}_{i}$, where the ideal $\mathfrak{q}_{i}$ is $\mathfrak{p}_{i}$-primary for $1 \leq i \leq n$. If one sets
$M'_{i} = M \otimes_{A} (A / \mathfrak{q}_{i})$, one then has an exact sequence

```text
                         0 → M → ⨁_i M'_i → M'' → 0
```

of $A$-modules, where `M''` is of finite length: indeed, localizing the preceding exact sequence at each of the
$\mathfrak{p}_{i}$, one obtains $M''_{\mathfrak{p}_{i}} = 0$, since $(\mathfrak{q}_{i})_{\mathfrak{p}_{i}} = 0$ and
$(\mathfrak{q}_{j})_{\mathfrak{p}_{i}} = A_{\mathfrak{p}_{i}}$ for $j \neq i$ (Bourbaki, _Alg. comm._, chap. IV, §2, n°
4, prop. 6), so $(M'_{i})_{\mathfrak{p}_{i}} = M_{\mathfrak{p}_{i}}$ and $(M'_{j})_{\mathfrak{p}_{i}} = 0$;

<!-- original page 300 -->

the support of `M''` being therefore reduced to $\mathfrak{m}$, `M''` is of finite length `(0, 16.1.10)`. If one sets
$u'_{i} = u \otimes 1_{A/\mathfrak{q}_{i}}$, and if `u''` is the endomorphism of `M''` deduced from $\bigoplus_{i}
u'_{i}$ by passage to quotients, one deduces from `(21.10.17.6)` that $\chi(M, u) + \chi(M'', u'') = \sum_{i}
\chi(M'_{i}, u'_{i})$, and since `M''` is of finite length, $\chi(M'', u'') = 0$. To prove `(21.10.17.8)`, one may
therefore reduce to the case where $n = 1$. One will then denote by $\mathfrak{p}$ the unique minimal prime ideal, which
is the nilradical of $A$; if $A_{0} = A / \mathfrak{p}$, $M_{0} = M \otimes_{A} A_{0}$, $u_{0} = u \otimes 1_{A_{0}}$,
it is a matter of proving that if $\chi(M_{0}, u_{0})$ is defined, one has

```text
  (21.10.17.9)           χ(M, u) = long A_𝔭 · χ(M_0, u_0).
```

Let $\mathfrak{n}_{j}$ ($0 \leq j \leq r$) be the "$j$-th symbolic power" of $\mathfrak{p}$, inverse image in $A$ of the
ideal $(\mathfrak{p} A_{\mathfrak{p}})^{j}$ of $A_{\mathfrak{p}}$ ($1 \leq j \leq r$), with $\mathfrak{n}_{0} = A$ and
$\mathfrak{n}_{r} = 0$; set

```text
                         M_j = 𝔫_j M / 𝔫_{j+1} M       (0 ≤ j ≤ r − 1),
```

and denote by $v_{j}$ the endomorphism of $M_{j}$ deduced from $u$ by restriction to $\mathfrak{n}_{j} M$ and passage to
quotients. We shall first show that each of the numbers $\chi(M_{j}, v_{j})$ is defined and that one has

```text
  (21.10.17.10)          χ(M, u) = ∑_j χ(M_j, v_j).
```

The first assertion will entail the second, by applying `(21.10.17.6)` to each of the exact sequences

```text
                         0 → 𝔫_j M / 𝔫_{j+1} M → M / 𝔫_{j+1} M → M / 𝔫_j M → 0.
```

To prove the first assertion, one notes that if $m$ is the rank of the free $A$-module $M$, $M_{j}$ is isomorphic to
$(\mathfrak{n}_{j} / \mathfrak{n}_{j+1})^{m}$, or also (since $\mathfrak{p}$ annihilates each of the quotients
$\mathfrak{n}_{j} / \mathfrak{n}_{j+1}$), $M_{j}$ is an `A_0`-module isomorphic to $M_{0} \otimes_{A_{0}}
(\mathfrak{n}_{j} / \mathfrak{n}_{j+1})$. Denote by $l_{j}$ the rank of the `A_0`-module $\mathfrak{n}_{j} /
\mathfrak{n}_{j+1}$; since the field of fractions `K_0` of `A_0` is the residue field of $A_{\mathfrak{p}}$, $l_{j}$ is
also the length of the $A_{\mathfrak{p}}$-module $(\mathfrak{p} A_{\mathfrak{p}})^{j} / (\mathfrak{p}
A_{\mathfrak{p}})^{j+1}$. There is a system of generators of the `A_0`-module $M_{j}$ which contains a basis of $M_{j}
\otimes_{A_{0}} K_{0}$; so there is an `A_0`-homomorphism

$$ w_{j} : M^{l_{j}}_{0} \to M_{j} $$

whose localization at the ideal `(0)` of `A_0` is an isomorphism, so that the supports of $Ker(w_{j})$ and of
$Coker(w_{j})$ are reduced to the maximal ideal $\mathfrak{m} / \mathfrak{p}$ of `A_0`; $Ker(w_{j})$ and $Coker(w_{j})$
are therefore `A_0`-modules of finite length `(0, 16.1.10)`. Since by hypothesis $\chi(M_{0}, u_{0})$ is defined, the
same holds for $\chi(M^{l_{j}}_{0}, u^{l_{j}}_{0}) = l_{j} \chi(M_{0}, u_{0})$, and in virtue of `(21.10.17.6)` and of
the fact that $Ker(w_{j})$ and $Coker(w_{j})$ are of finite length, one sees that $\chi(M_{j}, v_{j})$ is defined and
equal to $l_{j} \chi(M_{0}, u_{0})$; relation `(21.10.17.10)` then gives

```text
                         χ(M, u) = (∑_j l_j) χ(M_0, u_0),
```

and in virtue of a previous remark, $\sum_{j} l_{j}$ is none other than the length of $A_{\mathfrak{p}}$, which
completes the proof of the lemma `(21.10.17.7)`.

<!-- original page 301 -->

To apply this lemma when $A$ is a complete ring and $\mathfrak{m} \notin Ass(A)$, one observes that if $u$ is injective,
the same holds for the $u_{i}$ (with the notation of the lemma): indeed, `det u` is then a regular element of $A$, so
does not belong to any of the $\mathfrak{p}_{i}$, and its image $det u_{i}$ in $A / \mathfrak{p}_{i}$ is consequently an
element $\neq 0$ of this integral ring, which proves that $u_{i}$ is injective. Since $Coker(u_{i})$ is image of
$Coker(u)$, it is also of finite length and $\chi(M_{i}, u_{i})$ is therefore defined for every $i$; one has accordingly
the formula `(21.10.17.8)`. On the other hand, since $det(u)$ is a regular element of $A$, it is contained in none of
the $\mathfrak{p}_{i}$; the ideal `(det u) A` is therefore $\mathfrak{m}$-primary and the quotient $A / (det u) A$ of
finite length. Applying the same reasoning as above to the injective homothety $t : \xi \mapsto (det u) \xi$ of $A$ and
its images $t_{i} = det u_{i}$ in the $A / \mathfrak{p}_{i}$, it comes

```text
                         χ(A, t) = ∑_i long(A_{𝔭_i}) · χ(A / 𝔭_i, t_i).
```

But the rings $A / \mathfrak{p}_{i}$ are integral and complete, and applying the result of II) to each of them, one
again obtains relation `(21.10.17.4)` for $M$ and $u$.

IV) General case. Set $A' = \hat{A}$, $M' = M \otimes_{A} A'$, $u' = u \otimes 1_{A'}$; one has $det(u') = det(u)$, and
by flatness, $Coker(u') = (Coker(u))_{(A')}$ and $A' / (det u') A' = (A / (det u) A)_{(A')}$; since the formula
`(21.10.17.4)` is true for $A'$ and $u'$ in virtue of III), it is also true for $A$ and $u$ in virtue of `(4.7.1)`.

This completes the proof of `(21.10.17)`.

**Proposition (21.10.18).**

<!-- label: IV.21.10.18 -->

*Let $X$, $X'$ be two locally Noetherian preschemes, $f : X' \to X$ a finite morphism, sending every maximal point of
$X'$ to a maximal point of $X$, and verifying for every $x' \in X'$ one of conditions (ii), (iii), (iv) of `(21.10.10)`.
Assume in addition that there exists an integer $n$ such that, for every maximal point $x$ of $X$,
$(f_{*}(\mathcal{O}_{X'}))_{x}$ is a free $\mathcal{O}_{X,x}$-module of rank $n$. Then, for every 1-codimensional cycle
$Z$ on $X$, one has*

$$ (21.10.18.1) f_{*}(f^{*}(Z)) = n \cdot Z $$

*("projection formula").*

By virtue of the definitions, one is at once reduced to the case where $X$ is the spectrum of a Noetherian local ring
$A$ of dimension `1`, with closed point $x$, and where $Z = {x}$; set $X' = \operatorname{Spec}(A')$, where $A'$ is a
finite $A$-algebra, and, for every minimal prime ideal $\mathfrak{p}_{i}$ of $A$, $A'_{\mathfrak{p}_{i}}$ is a free
$A_{\mathfrak{p}_{i}}$-module of rank $n$. Let us show that one may further restrict to the case where $A$ is complete.
Make in effect the base change $h : Y \to X$, where $Y = \operatorname{Spec}(B)$, with $B = \hat{A}$, and set $Y' = X'
\times_{X} Y = \operatorname{Spec}(B \otimes_{A} A')$ and $g = f_{(Y)} : Y' \to Y$; the morphism $g$ is then finite, and
since $h$ is flat, the maximal points of $Y$ lie above those of $X$; above each of the $\mathfrak{p}_{i}$, there is only
a finite number of minimal ideals $\mathfrak{p}_{ij}$ of $B$, and $(B \otimes_{A} A')_{\mathfrak{p}_{ij}}$ is a free
$B_{\mathfrak{p}_{ij}}$-module of rank $n$. Finally, if $f$ verifies one of conditions (ii), (iii) or (iv) of
`(21.10.10)` at each of the points $x'$ of $f^{-1}(x)$, $g$ verifies the corresponding condition at the unique point
$y'$ of $g^{-1}(x')$ above $x'$ (denoting by $y$ the closed point of $Y$); this is immediate for conditions (ii) and
(iv); for condition (iii), it implies that $A$

<!-- original page 302 -->

is a discrete valuation ring, so the same holds for $B$, and the condition $\mathfrak{m}_{y'} \notin
Ass(\mathcal{O}_{Y',y'})$ follows, by flatness, from the condition $\mathfrak{m}_{x'} \notin Ass(\mathcal{O}_{X',x'})$
`(3.3.1)`. The morphism $g$ therefore verifies the same conditions as $f$; if one proves the formula `(21.10.18.1)` for
$g$ and ${y}$, the same formula will be valid for $f$ and ${x}$, in virtue of `(21.10.16.1)`.

One may therefore assume that $A$ is complete; then so is $A'$, which is thus the direct sum of complete local rings;
one may consequently restrict to the case where $A'$ is a local ring, and it remains to verify `(21.10.18.1)` in each of
the cases (ii), (iii), (iv) for the closed point $x'$ of $X'$. In case (ii), $A'$ being a flat $A$-module of finite
type, is a free $A$-module $(0_{III}, 10.1.3)$, of rank $n$ in virtue of the hypothesis. Now, one has by definition
`(21.10.1` and `21.10.3)` $f^{*}(Z) = \lambda_{x'} \cdot {x'}$, where $\lambda_{x'}$ is the length of the $A'$-module
$A' / \mathfrak{m}_{x} A'$, then $f_{*}(f^{*}(Z)) = (\lambda_{x'} [k(x') : k(x)]) \cdot {x}$; but $\lambda_{x'} [k(x') :
k(x)]$ is the length of $A' / \mathfrak{m}_{x} A' = A' \otimes_{A} k(x)$ as $A$-module, or also its rank as
$k(x)$-vector space, hence equals $n$.

In case (iii), $A$ is a discrete valuation ring, hence regular, and the hypothesis $\mathfrak{m}_{x'} \notin
Ass(\mathcal{O}_{X',x'})$ entails that $A'$ is a Cohen-Macaulay ring `(0, 16.4.6)`; since $\dim(A') = \dim(A) = 1$ and
$A' / \mathfrak{m}_{x} A'$ is an Artinian ring, it follows from `(6.1.5)` that $A'$ is a flat $A$-module, and one is
reduced to case (ii).

In case (iv), if $K$ is the total ring of fractions of $A$, $K' = A' \otimes_{A} K$ is by hypothesis a free $K$-module
of rank $n$ and by definition `(21.10.10)`, one has $f^{*}(Z) = (n / [k(x') : k(x)]) \cdot {x'}$, whence
$f_{*}(f^{*}(Z)) = n \cdot {x}$. Q.E.D.

One will note that the formula `(21.10.18.1)` is applicable in particular when the morphism $f$ is finite and flat and
such that for every maximal point $x$ of $X$, $(f_{*}(\mathcal{O}_{X'}))_{x}$ is a free $\mathcal{O}_{X,x}$-module of
rank $n$.

**Corollary (21.10.19).**

<!-- label: IV.21.10.19 -->

*Under the hypotheses of `(21.10.18)`, let $D$ be a divisor on $X$ such that $f^{*}(D)$ is defined `(21.4.5)`; then one
has*

$$ (21.10.19.1) f_{*}(cyc(f^{*}(D))) = n \cdot cyc(D). $$

This follows from `(21.10.18)` and `(21.10.13)`.

### 21.11. Factoriality of regular local rings

**Theorem (21.11.1) (Auslander-Buchsbaum).**

<!-- label: IV.21.11.1 -->

*A regular Noetherian local ring is factorial.*

The proof that follows is due to I. Kaplansky.

Let $A$ be a regular Noetherian local ring of dimension $n$; we shall reason by induction on $n$. For $n = 0$, $A$ is a
field, and for $n = 1$, a discrete valuation ring, hence principal (and a fortiori factorial). Suppose then $n \geq 2$
and the theorem proved for regular rings of dimension $< n$. Set $X = \operatorname{Spec}(A)$, denote by $a$ the closed
point of $X$, and set $U = X - {a}$. At every point $y \in U$, one has $\dim(\mathcal{O}_{X,y}) \leq n - 1$, and since
$A$ is regular, the rings $\mathcal{O}_{X,y}$ are also regular `(0, 17.3.2)`, so the induction hypothesis entails that
they are factorial. Moreover one has $prof(A) = \dim(A) \geq 2$ since $A$ is regular, hence Cohen-Macaulay
`(0, 17.1.3)`.

<!-- original page 303 -->

Using `(21.6.14)`, one is reduced to proving that $\operatorname{Pic}(U) = 0$. Therefore consider an invertible
$\mathcal{O}_{U}$-Module $\mathcal{L}$, and prove that it is isomorphic to $\mathcal{O}_{U}$. It follows from
`(I, 9.4.5)` that there exists a coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ such that $\mathcal{F} | U =
\mathcal{L}$. Since $A$ is regular, hence of finite cohomological dimension `(0, 17.3.1)`, there exists a finite left
resolution of $\mathcal{F}$:

```text
                         0 ← ℱ ← 𝒪_X^{n_1} ← 𝒪_X^{n_2} ← … ← 𝒪_X^{n_h} ← 0
```

`(0, 17.2.8` and `0, 17.2.2, (iii))`. By restriction to $U$, one therefore has a finite resolution

```text
  (21.11.1.1)            0 ← ℒ ← 𝒪_U^{n_1} ← 𝒪_U^{n_2} ← … ← 𝒪_U^{n_h} ← 0.
```

The theorem will then follow from the general considerations that follow. On a ringed space $X$, let $\mathcal{E}$ be a
locally free $\mathcal{O}_{X}$-Module of finite rank; one will denote by $\Lambda^{\max} \mathcal{E}$ the invertible
$\mathcal{O}_{X}$-Module which, in a neighbourhood of each point of $X$, equals $\Lambda^{p} \mathcal{E}$, denoting by
$p$ the rank of $\mathcal{E}$ in this neighbourhood (which may vary with the connected component of $X$). With this
notation, one has the

**Lemma (21.11.1.2).**

<!-- label: IV.21.11.1.2 -->

*Let $X$ be a ringed space in local rings, and*

$$ 0 \leftarrow \mathcal{E}_{0} \leftarrow \mathcal{E}_{1} \leftarrow \cdots \leftarrow \mathcal{E}_{h} \leftarrow 0 $$

*an exact sequence of $\mathcal{O}_{X}$-Modules locally free of finite rank; then the invertible
$\mathcal{O}_{X}$-Module $\bigotimes_{0 \leq i \leq h} (\Lambda^{\max} \mathcal{E}_{i})^{\otimes (-1)^{i}}$ is
isomorphic to $\mathcal{O}_{X}$.*

Let us show how this lemma will allow one to conclude the proof of `(21.11.1)`. It suffices to note for this that, for
every integer $n$, $\Lambda^{\max}(\mathcal{O}^{n}_{X}) = \Lambda^{n} \mathcal{O}_{X}$ is isomorphic to
$\mathcal{O}_{X}$, as is $\mathcal{O}^{\otimes (-1)}_{X}$. Since on the other hand $\Lambda^{\max} \mathcal{L} =
\mathcal{L}$ for every invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$, the lemma `(21.11.1.2)`, applied to the exact
sequence `(21.11.1.1)`, shows that $\mathcal{L}$ is isomorphic to $\mathcal{O}_{U}$.

It remains to prove `(21.11.1.2)`; one proceeds by induction on $h$, the lemma being trivial for $h = 1$. For $h > 1$,
$\mathcal{N} = Ker(u_{0})$ is an $\mathcal{O}_{X}$-Module locally free of finite rank $(0_{I}, 5.5.5)$, and one has the
two exact sequences

$$ 0 \leftarrow \mathcal{E}_{0} \leftarrow \mathcal{E}_{1} \leftarrow \mathcal{N} \leftarrow 0 0 \leftarrow \mathcal{N}
\leftarrow \mathcal{E}_{2} \leftarrow \cdots \leftarrow \mathcal{E}_{h} \leftarrow 0 $$

In virtue of the induction hypothesis, $(\Lambda^{\max} \mathcal{N}) \otimes (\bigotimes_{2 \leq i \leq h}
(\Lambda^{\max} \mathcal{E}_{i})^{\otimes (-1)^{i-1}})$ is isomorphic to $\mathcal{O}_{X}$; it will therefore suffice to
define a canonical isomorphism `(Λ^{max} 𝒩) ⊗ (Λ^{max} ℰ_0) ⥲ Λ^{max} ℰ_1` to complete the proof. Now, there exists an
open covering $(U_{\alpha})$ of $X$ such that in every $U_{\alpha}$, $\mathcal{E}_{1} | U_{\alpha}$ is the direct sum of
$\mathcal{N} | U_{\alpha}$ and of an $\mathcal{O}_{U_{\alpha}}$-Module locally free $\mathcal{M}_{\alpha}$ $(0_{I},
5.5.5)$, whence a canonical isomorphism $v_{\alpha} : \mathcal{M}_{\alpha} \xrightarrow{\sim} \mathcal{E}_{0} |
U_{\alpha}$. Since one has a canonical isomorphism

```text
                         r_α : (Λ^{max} 𝒩 | U_α) ⊗ (Λ^{max} ℳ_α) ⥲ (Λ^{max} ℰ_1) | U_α
```

one deduces from this, by means of $v_{\alpha}$, an isomorphism

```text
                         u_α : (Λ^{max} 𝒩 | U_α) ⊗ (Λ^{max} ℰ_0 | U_α) ⥲ Λ^{max} ℰ_1 | U_α
```

<!-- original page 304 -->

and it is a matter of showing that $u_{\alpha}$ and $u_{\beta}$ coincide in $U_{\alpha} \cap U_{\beta}$ for any two
indices $\alpha$, $\beta$. Now, if $v'_{\alpha}$ and $v'_{\beta}$ are the restrictions to $U_{\alpha} \cap U_{\beta}$ of
$v_{\alpha}$ and $v_{\beta}$ respectively, one has $v'_{\alpha} = v'_{\beta} \circ w_{\beta \alpha}$, where $w_{\beta
\alpha} : \mathcal{M}_{\alpha} | (U_{\alpha} \cap U_{\beta}) \xrightarrow{\sim} \mathcal{M}_{\beta} | (U_{\alpha} \cap
U_{\beta})$ is the "projection parallel to $\mathcal{N}$" such that for every section $s \in \Gamma(U_{\alpha} \cap
U_{\beta}, \mathcal{M}_{\alpha})$, $w_{\beta \alpha}(s) = s + t$ with $t \in \Gamma(U_{\alpha} \cap U_{\beta},
\mathcal{N})$; the identity of $u_{\alpha}$ and $u_{\beta}$ follows at once from this fact and from the definition of
the canonical isomorphism $r_{\alpha}$ (Bourbaki, _Alg._, chap. III, 3rd ed.).

<!-- original page 304 -->

### 21.12. Van der Waerden's purity theorem for the ramification locus of a birational morphism

**(21.12.1).** Let $X$ and $U$ be two preschemes, $f : U \to X$ a quasi-compact and quasi-separated morphism, so that
$f_{*}(\mathcal{O}_{U})$ is a quasi-coherent $\mathcal{O}_{X}$-Algebra `(1.7.4)`. We call **affine envelope** of the
$X$-prescheme $U$ the $X$-prescheme affine over $X$

```text
                       U^∘ = Aff(U/X) = Spec(f_*(𝒪_U)) = Spec(𝒜(U))                  (II, 1.1.1).
```

If $f^{\circ} : U^{\circ} \to X$ is the structural morphism, one has therefore by definition

```text
                       𝒜(U^∘) = f^∘_*(𝒪_{U^∘}) = f_*(𝒪_U) = 𝒜(U),
```

and to the identity isomorphism of $f_{*}(\mathcal{O}_{U})$ there corresponds by `(II, 1.2.7)` a canonical $X$-morphism

<!-- label: IV.21.12.1 -->

$$ (21.12.1.1) i_{U} : U \to U^{\circ}. $$

For $i_{U}$ to be an isomorphism, it is evidently necessary and sufficient that the morphism $f : U \to X$ be affine.

For every $X$-prescheme $V$ affine over $X$, the map $u \mapsto u \circ i_{U}$ is a bijection

```text
                       Hom_X(U^∘, V) ⥲ Hom_X(U, V)
```

functorial in $V$: this results from the existence of the canonical bijections $\operatorname{Hom}_{X}(U, V)
\xrightarrow{\sim} \operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{A}(V), \mathcal{A}(U))$ and
$\operatorname{Hom}_{X}(U^{\circ}, V) \xrightarrow{\sim} \operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{A}(V),
\mathcal{A}(U^{\circ}))$ `(II, 1.2.7)`.

One can therefore say that $U^{\circ}$ represents the covariant functor $V \mapsto \operatorname{Hom}_{X}(U, V)$ in the
category of $X$-preschemes affine over $X$ $(0_{III}, 8.1.11)$. One deduces $(0_{III}, 8.1.7)$ that, for $X$ fixed, $U
\mapsto Aff(U/X)$ is a covariant functor from the category of quasi-compact and quasi-separated $X$-preschemes into the
category of $X$-preschemes affine over $X$; more precisely, if `U_1`, `U_2` are two quasi-compact and quasi-separated
$X$-preschemes, to every $X$-morphism $g : U_{1} \to U_{2}$ there corresponds the unique $X$-morphism $g^{\circ} :
U^{\circ}_{1} \to U^{\circ}_{2}$ rendering the diagram

```text
                       U_1 ────────→ U_2
                        │             │
                  i_{U_1}│             │i_{U_2}
                        ↓             ↓
                       U_1^∘ ──g^∘──→ U_2^∘
```

commutative.

<!-- original page 305 -->

More generally, consider a commutative diagram

```text
                       U ──u──→ U'
                       │        │
                      f│        │f'
                       ↓        ↓
                       X ──v──→ X'
```

where the morphisms $f$, $f'$ are quasi-compact and quasi-separated and the morphism $u$ affine. Setting $h = u \circ
f$, one has $h_{*}(\mathcal{O}_{U}) = u_{*}(f_{*}(\mathcal{O}_{U})) = u_{*}(f^{\circ}_{*}(\mathcal{O}_{U^{\circ}}))$ and
$u \circ f^{\circ}$ is an affine morphism; one has consequently $U^{\circ} = Aff(U/X')$ (relative to the morphism $h$),
whence a unique $X'$-morphism $v^{\circ} : U^{\circ} \to U'^{\circ}$ rendering the diagram

```text
                       U ──u──→ U'
                       │        │
                  i_U  │        │i_{U'}
                       ↓        ↓
                       U^∘ ─v^∘→ U'^∘
```

commutative.

**Proposition (21.12.2).**

<!-- label: IV.21.12.2 -->

*Let $f : U \to X$ be a quasi-compact and quasi-separated morphism, $h : X' \to X$ a flat morphism; set $U' = U
\times_{X} X'$, $f' = f_{(X')} : U' \to X'$. Then one has a canonical $X'$-isomorphism*

```text
  (21.12.2.1)                          Aff(U'/X') ⥲ Aff(U/X) ×_X X'.
```

Indeed, one has $Aff(U'/X') = \operatorname{Spec}(f'_{*}(\mathcal{O}_{U'}))$, and $Aff(U/X) \times_{X} X' =
\operatorname{Spec}(h^{*}(f_{*}(\mathcal{O}_{U})))$ `(II, 1.5.1)`; the isomorphism of the statement comes from the
canonical isomorphism $h^{*}(f_{*}(\mathcal{O}_{U})) \xrightarrow{\sim} f'_{*}(\mathcal{O}_{U'})$ `(2.3.1)`.

**Corollary (21.12.3).**

<!-- label: IV.21.12.3 -->

*For every quasi-compact and quasi-separated morphism $f : U \to X$ and every $x \in X$, one has, up to a canonical
isomorphism*

```text
  (21.12.3.1)                          U^∘ ×_X Spec(𝒪_{X,x}) = (U ×_X Spec(𝒪_{X,x}))^∘.
```

It also follows from `(21.12.2)` that one has, up to a canonical isomorphism, for every open $V$ of $X$

<!-- label: IV.21.12.4 -->

$$ (21.12.4) (f^{-1}(V))^{\circ} \simeq (f^{\circ})^{-1}(V). $$

**(21.12.5).** We shall consider in particular the case where $f : U \to X$ is an *open immersion*, so that $U$ is
identified with a prescheme induced on an open of $X$. Since the morphism $f_{*}(\mathcal{O}_{U}) \to \mathcal{O}_{U}$
is the identity, it follows from `(21.12.4)` that the morphism $(f^{\circ})^{-1}(U) \to U$ restriction of $f^{\circ}$ is
an isomorphism, $i_{U} : U \to U^{\circ}$ being therefore an *open immersion* permitting $U$ to be identified with a
prescheme induced on an open of $U^{\circ}$.

More generally, for an open $V$ of $X$, the restriction $(f^{\circ})^{-1}(V) \to V$ of $f^{\circ}$ is an isomorphism of
$(f^{\circ})^{-1}(V)$ onto the prescheme induced on the open $V \cap U$ if and only if the open immersion $U \cap V \to
V$ is an affine morphism. It is clear `(II, 1.2.1)`

<!-- original page 306 -->

that the union of these opens $V$ is the largest of them, `U_1`, which contains $U$; by virtue of the foregoing, `U_1`
is also the largest open not meeting the set

$$ Daf(U/X) = f^{\circ}(U^{\circ}) - U $$

("affineness defect" of the open $U$ relative to $X$, which is empty if and only if $U$ is affine over $X$); in other
words, the closed set $Z = X - U_{1}$ is the *closure* of the set $Daf(U/X)$.

Note that for every flat morphism $h : X' \to X$, if one sets $U' = h^{-1}(U)$, one has

<!-- label: IV.21.12.5.1 -->

$$ (21.12.5.1) Daf(U'/X') = h^{-1}(Daf(U/X)) $$

as follows at once from `(21.12.2.1)` and `(I, 3.4.8)`. In particular, for every open $V$ of $X$, one has

<!-- label: IV.21.12.5.2 -->

```text
  (21.12.5.2)                          Daf((U ∩ V)/V) = Daf(U/X) ∩ V
```

and for every $x \in X$,

<!-- label: IV.21.12.5.3 -->

```text
  (21.12.5.3)                          Daf((U ∩ Spec(𝒪_{X,x}))/Spec(𝒪_{X,x})) = Daf(U/X) ∩ Spec(𝒪_{X,x}).
```

We shall, when $X$ is locally Noetherian, give precise information on the nature of the set $Daf(U/X)$, showing for
example that when $U$ is everywhere dense in $X$, $Daf(U/X)$ is not an arbitrary rare closed set:

**Theorem (21.12.6).**

<!-- label: IV.21.12.6 -->

*Let $X$ be a locally Noetherian prescheme, $U$ a non-empty open of $X$, $f : U \to X$ the canonical injection. Then:*

*(i) The closure $Z = X - U_{1}$ of $Daf(U/X)$ is of codimension $\geqslant 2$ in $X$.*

*(ii) If $T = X - U \supset Z$ is of codimension $\geqslant 2$, the morphism $f^{\circ} : U^{\circ} \to X$ is
surjective.*

(i) Let us first show that for every point $x \in Daf(U/X)$ one necessarily has $\dim(\mathcal{O}_{X,x}) \geqslant 1$.
Indeed, $x$ cannot evidently be a maximal point of $X$, being contained in $\bar{U} - U$; we have therefore to see that
one cannot have $\dim(\mathcal{O}_{X,x}) = 1$. But this relation would entail, by `(21.12.5.3)`, that $x \in
Daf(U_{x}/\operatorname{Spec}(\mathcal{O}_{X,x}))$, where $U_{x} = U \cap \operatorname{Spec}(\mathcal{O}_{X,x})$. But
the only opens of $\operatorname{Spec}(\mathcal{O}_{X,x})$ are $\operatorname{Spec}(\mathcal{O}_{X,x})$ itself and the
subsets of the (finite) set of maximal points of $\operatorname{Spec}(\mathcal{O}_{X,x})$. Now the open set reduced to a
maximal point of $\operatorname{Spec}(\mathcal{O}_{X,x})$ is affine, by definition of preschemes; one concludes that all
open sets in $\operatorname{Spec}(\mathcal{O}_{X,x})$ are affine, hence
$Daf(U_{x}/\operatorname{Spec}(\mathcal{O}_{X,x})) = \emptyset$, contrary to the hypothesis made.

To prove (i) one must show more, namely that if $x \in X$ is such that $\dim(\mathcal{O}_{X,x}) = 1$, there exists an
open neighbourhood $W$ of $x$ in $X$ such that $W$ does not meet $Daf(U/X)$, that is to say such that the canonical
injection $f_{W} : U \cap W \to W$ is affine. But, with the same notations as above, one has just seen that the
canonical injection $f^{(x)} : U^{(x)} \to \operatorname{Spec}(\mathcal{O}_{X,x})$ is affine. One can evidently restrict
to the case where $X$ is Noetherian; since the morphism $f$ is of finite presentation, the conclusion results from
`(8.10.5, (viii))` applied following the method of `(8.1.2, a))`.

<!-- original page 307 -->

(ii) We must prove that for every point $x \in T$, one has $x \in f^{\circ}(U^{\circ})$; we shall first show that one
may reduce to the case where $X = \operatorname{Spec}(A)$, where $A$ is a complete Noetherian local ring, and $x$ the
closed point of $X$. For this, it suffices to make the base change $h : X' = \operatorname{Spec}(\hat{A}) \to X$, where
$\hat{A} = \hat{\mathcal{O}}_{X,x}$; if one sets $U' = h^{-1}(U)$, $f' = f_{(X')}$ is the canonical injection $U' \to
X'$, and since the morphism $h$ is flat, it follows from `(21.12.2)` that if one proves that $x$ belongs to
$f'^{\circ}(U'^{\circ})$, one deduces that $x \in f^{\circ}(U^{\circ})$. By virtue of `(6.1.1)`, the reduction sought
has indeed been effected.

Let then `X_1` be a closed reduced sub-prescheme of $X$ whose underlying space is an irreducible component of $X$, of
maximal dimension among those which contain an irreducible component of $T$, and set $U_{1} = U \cap X_{1}$, $T_{1} = T
\cap X_{1} = X_{1} - U_{1}$; one has therefore $codim(T_{1}, X_{1}) \geqslant 2$ `(0, 14.2.1)`, and the pair $(U_{1},
X_{1})$ therefore verifies the same hypotheses as the pair $(U, X)$ (`X_1` being the spectrum of a quotient ring of $A$,
hence local Noetherian and complete). One has moreover a commutative diagram

```text
                       U_1 ──→ U
                        │      │
                       f_1│     │f
                        ↓      ↓
                       X_1 ──j→ X
```

where $i$ and $j$ are the canonical injections, $i$ being therefore an affine morphism; one deduces `(21.12.1)` the
existence of a morphism $j^{\circ} : U^{\circ}_{1} \to U^{\circ}$ rendering the diagram

```text
                       U_1^∘ ──→ U^∘
                        │        │
                       f_1^∘│     │f^∘
                        ↓        ↓
                       X_1 ────→ X
```

commutative, and consequently, to prove that $x \in f^{\circ}(U^{\circ})$, it suffices to prove that $x \in
f^{\circ}_{1}(U^{\circ}_{1})$. One can therefore replace $X$ by `X_1`, and one can consequently suppose that the ring
$A$ is moreover *integral*. But $A$ is the quotient of a regular Noetherian ring by virtue of Cohen's theorem
`(0, 19.8.8, (i))`, and since it is integral, one can apply `(5.11.1)` with the family $(x_{\alpha})$ reduced to the
unique maximal point of $X$; since $codim(T, X) \geqslant 2$ by hypothesis, one sees that $f_{*}(\mathcal{O}_{U})$ is a
coherent $\mathcal{O}_{X}$-Module, hence the morphism $f^{\circ} : U^{\circ} \to X$ is *finite*; since this morphism is
dominant ($U$ being everywhere dense), it is surjective `(II, 6.1.10)`, and consequently $x \in f^{\circ}(U^{\circ})$.
**Q.E.D.**

**Corollary (21.12.7).**

<!-- label: IV.21.12.7 -->

*Let $X$ be a locally Noetherian prescheme, $U$ a sub-prescheme induced on an open of $X$, $j : U \to X$ the canonical
immersion; suppose that $j$ is an affine morphism. Then every irreducible component of $T = X - U$ is of codimension
$\leqslant 1$ (and consequently of codimension `1` if $U$ is everywhere dense).*

Suppose indeed that one of the irreducible components `T_1` of $T$ is of codimension $\geqslant 2$ in $X$. Replacing if
needed $X$ by an open neighbourhood of the generic point of `T_1`, one can suppose $T$ irreducible and of codimension
$\geqslant 2$. But then the hypothesis

<!-- original page 308 -->

that $j : U \to X$ is affine implies that $U^{\circ}$ is identified with $U$ and $j^{\circ}$ with $j$, in other words
that $j^{\circ}(U^{\circ}) = U$; but this contradicts the conclusion of `(21.12.6)` which, under the dimension
hypothesis made, implies that $j^{\circ}$ must be surjective.

**(21.12.8).** Let $A$ be a Noetherian local ring, $Y = \operatorname{Spec}(A)$, $y$ the unique closed point of $Y$, $Y'
= Y - {y}$. Consider the following condition:

**(W)** *For every open $U$ of $Y$ contained in $Y'$, containing no irreducible component of $Y'$ and such that the
canonical immersion $U \to Y'$ is affine, $U$ is itself an affine open.*

This condition is entailed by the following:

**(W̃)** *For every closed part $T$ of $Y$ every irreducible component of which is of codimension `1` in $Y$, and such
that for every irreducible component $Y_{i}$ of $Y$, one has $Y_{i} \cap T \neq {y}$, the open $U = Y - T$ is affine.*

Indeed, if **(W̃)** is verified and if the open $U$ of $Y$ verifies the hypothesis of **(W)**, it follows from
`(21.12.7)` that no irreducible component of $T = Y - U$ can be of codimension $\geqslant 2$; since moreover $U$
contains none of the irreducible components $Y_{i} - {y}$ of $Y'$, condition **(W̃)** shows that $U$ is affine.

Note that condition **(W̃)** simplifies when $Y$ is irreducible and is then equivalent to the following:

**(W̃')** *For every irreducible closed part $T$ of $Y$, of codimension `1` in $Y$, $Y - T$ is an affine open.*

Indeed, it is clear that **(W̃)** entails **(W̃')** when $Y$ is irreducible, and the converse is true by considering the
irreducible components of $T$ and noting that the intersection of a finite number of affine opens is an affine open
`(I, 5.5.6)`.

**Examples (21.12.9).** If $A$ is a factorial Noetherian local ring, it verifies **(W̃)** (and a fortiori **(W)**), since
every prime ideal of height `1` is principal `(I, 1.3.6)`. But there are non-factorial Noetherian local rings verifying
**(W)**, for example those of dimension $\leqslant 1$: indeed, one noted in the proof of `(21.12.6, (i))` that all opens
of $Y$ are then affine. One can moreover prove by using local duality theory (chap. III, 3rd part) that every Noetherian
local ring of dimension `2` verifies **(W)**.

The interest of condition **(W)** lies in the following result:

**Proposition (21.12.10).**

<!-- label: IV.21.12.10 -->

*Let $X$, $Y$ be two locally Noetherian preschemes; $g : X \to Y$ a morphism, $y$ a closed point of $Y$, $Y' = Y - {y}$,
$X' = g^{-1}(Y')$; suppose that the morphism $g' : X' \to Y'$ restriction of $g$ is an open immersion, and that the
local ring $\mathcal{O}_{Y,y}$ verifies condition **(W)** `(21.12.8)`. Then, for every irreducible component $Z$ of
$X_{y} = g^{-1}(y)$, either $Z$ is of codimension $\leqslant 1$ in $X$, or its generic point is isolated in $Z$. If $Z$
is locally of finite type over $k(y)$, the second alternative implies that $Z$ is reduced to a single point.*

The last assertion of the statement results from the fact that $Z$ is then a Jacobson prescheme `(10.4.7)`, and since
the set of closed points of $Z$ is then dense in $Z$, the generic point of $Z$ can be isolated in $Z$ only if $Z$ is
reduced to a single point.

Suppose that there exists in $X_{y}$ an irreducible component $Z$ whose generic point $\xi$ is not isolated in $Z$, and
such that $codim(Z, X) \geqslant 2$. The question being local

<!-- original page 309 -->

on $X$ and $Y$ since $\xi$ is non-isolated in $Z$, one can, by replacing $X$ by an open neighbourhood of $\xi$ in $X$,
suppose $X$ and $Y$ affine, $X_{y} = Z$ irreducible, not reduced to a point and such that $codim(X_{y}, X) \geqslant 2$.
The image $g(X - X_{y}) = U$ is an open of $Y'$ isomorphic to $X - X_{y}$ by hypothesis; let us show that on replacing
if needed $X$ by an open neighbourhood of $\xi$ in $X$, one can suppose that $U$ contains none of the irreducible
components of $Y'$ whose closure contains $y$. Indeed, one can first suppose that all maximal points of $X$ are
generizations of $\xi$, the set of these points being finite; hence the set of maximal points of $U$ is the set of
images $y_{i}$, by $g$ of the maximal points $x_{i}$ of $X$ (no maximal point of $X$ being able by hypothesis to be
contained in $X_{y}$, since $\dim(\mathcal{O}_{X,\xi}) \geqslant 2$). Set $X_{i} = {\bar{x}_{i}}$. By hypothesis, one
has $\xi \in X_{i}$ and since $\xi$ is not isolated in $X_{y}$, there exists in $X_{y}$ a point $x_{i} \neq \xi$. Since
$X_{i} \neq Z$, there exists in $X_{i}$ a point $t_{i}$ such that, if one sets $T_{i} = {\bar{t}_{i}}$, one has
$\dim(\mathcal{O}_{T_{i}, \xi}) = 1$ `(10.5.9)`; this entails by hypothesis $t_{i} \notin Z$, hence $t_{i}$ is not a
generization of $\xi$. Replacing $X$ by $X' = X - \bigcup T_{i}$, one sees that the image by $g$ of $X' - X_{y}$ does
not contain the images $g(t_{i})$, hence contains none of the irreducible components of $Y'$ whose closure contains $y$.
That being the case, since $X$ and $Y$ are affine, the morphism $g : X \to Y$ is affine, hence so is the restriction
$g' : X' \to Y'$; since $g'$ is an open immersion, the canonical immersion $U \to Y'$ is affine. Set
$Y_{1} = \operatorname{Spec}(\mathcal{O}_{Y,y})$, $Y_{1}' = Y_{1} - {y} = Y' \cap Y_{1}$, $U_{1} = U \cap Y_{1}$. The
foregoing proves that the canonical immersion $U_{1} \to Y_{1}'$ is affine, hence `U_1` is an affine open in `Y_1` by
virtue of **(W)**, in other words the canonical immersion $U_{1} \to Y_{1}$ is affine. But since this immersion is of
finite presentation `(1.6.2)`, it follows from `(8.10.5, (viii))` applied following the method of `(8.1.2, a))` that on
restricting if needed $Y$ to an affine open neighbourhood of $y$, one can suppose that the immersion $U \to Y$ is
affine. One would conclude that the open $X - X_{y}$ of $X$, isomorphic to $U$, would be affine, which would contradict
`(21.12.7)`; the proposition is thus proved.

**Corollary (21.12.11).**

<!-- label: IV.21.12.11 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $X$ being supposed irreducible; let $g : X \to Y$ be a morphism
locally of finite type, and let $V$ be the largest open of $X$ such that the restriction $g | V : V \to Y$ is a local
isomorphism. Suppose that for every point $y \in Y$, the local ring $\mathcal{O}_{Y,y}$ verifies condition **(W)**
`(21.12.8)`. Then every irreducible component of $T = X - V$ is either of codimension $\leqslant 1$, or such that its
generic point $\xi$ is isolated in $g^{-1}(g(\xi))$.*

Set $g(\xi) = y$. The question depending only on the fibre $g^{-1}(y)$ and the local ring $\mathcal{O}_{Y,y}$, one can
by base change restrict to the case where $Y = \operatorname{Spec}(\mathcal{O}_{Y,y})$ and where $X$ is affine
(`(I, 3.6.5)` and `(I, 4.5.5)`); replacing if needed $X$ by an open neighbourhood of $\xi$ in $X$, one can suppose that
$T$ is irreducible; moreover one can restrict to the case where $V$ is non-empty. The morphism $g$ can therefore be
supposed separated and $y$ closed in $Y$; since the restriction $g | V : V \to Y$ is a local isomorphism and the
non-empty open $V$ of $X$

<!-- original page 310 -->

is irreducible, it follows from `(I, 8.2.8)` that $g | V : V \to Y$ is an open immersion. The restriction $g | (V \cap
X_{y}) : V \cap X_{y} \to {y} = \operatorname{Spec}(k(y))$ is therefore also an open immersion, which shows that $V \cap
X_{y}$ is either empty or reduced to a point $x$ rational over $k(y)$, hence closed in $X_{y}$ `(I, 6.4.2)`. Replacing
once again if needed $X$ by a smaller open neighbourhood of $\xi$ in $X$, one can therefore restrict to the case where
$V \cap X_{y} = \emptyset$, in other words $T \supset X_{y}$; since moreover $\xi \in X_{y}$ is the generic point of
$T$, one has $g(T) \subset {y} = {y}$, in other words $T = X_{y}$. One is then exactly in the conditions of application
of `(21.12.10)`, whence the conclusion.

**Theorem (21.12.12)** (van der Waerden).

<!-- label: IV.21.12.12 -->

*Let $X$, $Y$ be two locally Noetherian integral preschemes, $g : X \to Y$ a birational morphism locally of finite type.
Suppose moreover that $Y$ is normal and that for every $y \in Y$, the ring $\mathcal{O}_{Y,y}$ verifies condition
**(W)** of `(21.12.8)` (conditions fulfilled in particular when $Y$ is locally factorial `(21.12.9)`). If $V$ is the
largest open of $X$ such that the restriction $g | V : V \to Y$ is a local isomorphism, all irreducible components of $T
= X - V$ are of codimension `1` in $X$.*

Note that since $g$ is birational, the open set $V$ is non-empty; it therefore suffices to prove that a maximal point
$\xi$ of $T$ cannot be isolated in $X_{y}$, where $y = g(\xi)$. But, by restricting to an open neighbourhood of $\xi$,
one can restrict to the case where $T = X_{y}$; then all the fibres $g^{-1}(y')$ ($y' \in Y$) would be empty or reduced
to a point, and it would follow from the *Main theorem* `(8.12.10)` that $g$ would be a local isomorphism, contrary to
the hypothesis $\xi \in T$.

**Corollary (21.12.13).**

<!-- label: IV.21.12.13 -->

*Suppose the hypotheses of `(21.12.12)` are verified and in addition suppose that $g$ is quasi-finite at each of the
points of $X_{y}$ (recall that these are the points where $\dim(\mathcal{O}_{X,x}) = 1$); then $g$ is a local
isomorphism, and if moreover $g$ is separated, $g$ is an open immersion.*

It suffices to prove the first assertion, the second being a consequence of the first and of `(I, 8.2.8)`. Everything
reduces to proving, with the notation of `(21.12.12)`, that $T = \emptyset$; in the contrary case, a generic point $\xi$
of an irreducible component of $T$ would belong to $X_{y}$ by virtue of `(21.12.12)`, and by hypothesis it would be
isolated in $X_{y}$ with $y = g(\xi)$; but we saw in the proof of `(21.12.12)` that this is not possible.

**Remarks (21.12.14).**

<!-- label: IV.21.12.14 -->

(i) The conclusion of `(21.12.12)` applies when $Y$ is regular and integral and $X$ integral, since by virtue of the
Auslander-Buchsbaum theorem `(21.11.1)`, $Y$ is then locally factorial. On the other hand, examples are known where $X$
and $Y$ are normal algebraic schemes of dimension `3`, over an algebraically closed field of arbitrary characteristic,
and where the conclusion of `(21.12.12)` is no longer valid.

(ii) The set $T$ of `(21.12.12)` is also the set of points where $g$ is ramified. Indeed, if $g$ is unramified at a
point $x \in X$, it is also unramified in an affine open neighbourhood $U$ of $x$ `(17.3.7)`, hence $g | U$ is a
separated, quasi-finite and birational morphism `(17.4.3)`. Since $Y$ is normal, one concludes from the *Main theorem*
`(III, 4.4.9)` that $g$ is a local isomorphism at the point $x$, hence $x \in X - T$. Conversely, $g$ is evidently
unramified at every point where it is a local isomorphism. This justifies the title given to this section.

(iii) Without supposing that $Y$ is locally factorial, but supposing on the other hand that $X$ is a complete
intersection relative to $Y$ (chap. V), we shall see in chap. V

<!-- original page 311 -->

that one has a more precise result than `(21.12.12)`, by expressing $T$ as a `1`-codimensional cycle of a section of an
invertible $\mathcal{O}_{X}$-Module, canonically associated to $g$. This will apply notably when $X$ and $Y$ are both
regular, or when $g$ is an $S$-morphism, $X$ and $Y$ being smooth preschemes over $S$.

(iv) One may ask whether `(21.12.10)` admits a converse; in other words, for a given Noetherian local ring $A$, if one
sets $Y = \operatorname{Spec}(A)$, $y$ denoting the closed point of $Y$, and if, for every locally Noetherian prescheme
$X$ and every morphism $g : X \to Y$ such that $g' : X' \to Y'$ is an open immersion, every irreducible component of
$X_{y}$ is of codimension $\leqslant 1$ in $X$ or is reduced to a point, is it then true that $A$ verifies condition
**(W)** of `(21.12.8)`?

(v) Let $Y$ be an integral regular prescheme, $X$ a locally Noetherian normal prescheme, $g : X \to Y$ a morphism
locally of finite type; suppose moreover that, if $\eta$ is the generic point of $Y$, the fibre $X_{\eta}$ is étale over
$k(\eta)$, and let $T'$ be the complement of the largest open $V$ of $X$ such that $g | V : V \to Y$ is étale; is it
then true that all irreducible components of $T'$ are of codimension `1`? This is indeed so when one supposes in
addition that $g$ is locally quasi-finite (Zariski-Nagata "purity theorem"). One can show that the foregoing conjecture
would be a consequence of the following one (and would even be equivalent to it if the conjecture of (iv) were
verified): for a regular local ring $A$ contained in an integral and integrally closed local ring $B$, such that $B$ is
a finite $A$-module, the open $U$ of points of $\operatorname{Spec}(B)$ at which $\operatorname{Spec}(B)$ is unramified
over $\operatorname{Spec}(A)$ (or, what amounts to the same by `(18.10.1)`, étale over $\operatorname{Spec}(A)$) is
affine.

**Proposition (21.12.15).**

<!-- label: IV.21.12.15 -->

*Let $S$ be a prescheme, $g : X \to S$ a flat morphism locally of finite presentation, whose fibres $X_{s} = g^{-1}(s)$
are geometrically irreducible `(4.5.2)`; $h : Y \to S$ a smooth morphism; one denotes $Y_{s} = h^{-1}(s)$ the fibres of
this morphism. Let $f : X \to Y$ be a proper $S$-morphism such that, for every maximal point $\eta$ of $S$, the morphism
$f_{\eta} : X_{\eta} \to Y_{\eta}$ is an isomorphism. Then $f$ is an isomorphism.*

Since $h$ is flat, every maximal point of $Y$ is above a maximal point of $S$ `(2.3.4)`, hence the union of the
$Y_{\eta}$, when $\eta$ runs through the set of maximal points of $S$, is dense in $Y$; since the $f_{\eta}$ are
isomorphisms, $f$ is dominant and hence surjective since it is proper. It therefore suffices to show that $f$ is an open
immersion. Taking `(17.9.5)` into account, it suffices to prove that for every $s \in S$, $f_{s} : X_{s} \to Y_{s}$ is
an open immersion. Since every $s \in S$ is a generization of a maximal point $\eta$, one can already, by making the
base change $\operatorname{Spec}(\mathcal{O}_{S',s}) \to S$, where $S'$ is the reduced sub-prescheme of $S$ having
${\bar{\eta}}$ as underlying space, reduce to the case where $S$ is a local and integral scheme of closed point $s$: the
fibres at the points $\eta$ and $s$ are indeed not changed and the properties of the morphisms $g$, $h$ and $f$ are
preserved by base change. Moreover, the question is local on $Y$; replacing $Y$ by an affine open neighbourhood $U$ in
$Y$ of a point of $Y_{s}$, and $X$ by $f^{-1}(U)$, which is quasi-compact since $f$ is proper, one sees that one can
suppose in addition that $X$ and $Y$ are of finite presentation over $S$. There then exists a Noetherian local sub-ring
`A_0` of $A = \mathcal{O}_{S,s}$ such that $A_{0} \to A$ is a local homomorphism, two morphisms of finite type $g_{0} :
X_{0} \to S_{0} = \operatorname{Spec}(A_{0})$, $h_{0} : Y_{0} \to S_{0}$ and an `S_0`-morphism

<!-- original page 312 -->

$f_{0} : X_{0} \to Y_{0}$ such that $g$, $h$ and $f$ are deduced from $g_{0}$, $h_{0}$, $f_{0}$ by the base change $S
\to S_{0}$ (`(8.9.1)` and `(5.13.3)`); one can in addition suppose $g_{0}$ flat `(11.2.7)`, $h_{0}$ smooth `(17.7.9)`
and $f_{0}$ proper `(8.10.5, (xii))`. On the other hand, the projection on `S_0` of the generic point $\eta$ of $S$ is
the generic point $\eta_{0}$ of `S_0` and it follows from `(2.7.1, (viii))` that the morphism $(f_{0})_{\eta_{0}} :
(X_{0})_{\eta_{0}} \to (Y_{0})_{\eta_{0}}$ is an isomorphism; finally the closed point $s$ of $S$ is above the closed
point $s_{0}$ of `S_0`, hence the fibre $(X_{0})_{s_{0}}$ of $g_{0}$ is geometrically irreducible `(4.5.6)`. One sees
therefore that one can restrict to the case where $S$ is the spectrum of an integral Noetherian local ring, of closed
point $s$, weaken the hypothesis on the fibres by supposing only that $X_{s}$ and $X_{\eta}$ are geometrically
irreducible, and prove that under these hypotheses $f_{s}$ is an open immersion. There is then a discrete valuation ring
$A'$ and a morphism $S' = \operatorname{Spec}(A') \to S$ which transforms the closed point $a$ of $S'$ into $s$ and the
generic point $b$ of $S'$ into $\eta$ `(II, 7.1.9)`; let $g' : X' \to S'$, $h' : Y' \to S'$, $f' : X' \to Y'$ be the
morphisms deduced from $g$, $h$, $f$ by the base change $S' \to S$, which again verify the hypotheses verified by $g$,
$h$, and $f$ in the statement of `(21.12.15)`; if one proves that $f'_{a} : X'_{a} \to Y'_{a}$ is an open immersion, it
will follow from `(2.7.1, (x))` that the same will be true for $f_{s} : X_{s} \to Y_{s}$. One can therefore finally
restrict to the case where $S$ is the spectrum of a *discrete valuation ring*. Then, since $h : Y \to S$ is smooth, $Y$
is regular `(17.5.8)`, and since the question is local on $Y$, one can restrict to the case where $Y$ is integral. Since
$g : X \to S$ is flat, the maximal points of $X$ are contained in $X_{\eta}$ `(2.3.4)` and since $f_{\eta}$ is an
isomorphism, $X$ is irreducible and the local ring at its generic point is a field; moreover, by flatness `(3.3.2)`, one
sees that $X$ has no immersed prime cycles, hence $X$ is reduced `(3.2.1)` and consequently integral and $f$ is a
birational and separated morphism. To prove that $f$ is an open immersion, one can therefore apply the criterion
`(21.12.13)`; to see that $f$ is quasi-finite at the points of $X_{s}$, one remarks that the assertion is evident at
those of these points which belong to $X_{\eta}$; the only point of $X_{s}$ belonging to $X_{\eta}$ is the generic point
$x$ of $X_{s}$, by virtue of `(6.1.1)`. Now, it follows from `(2.4.6)` and `(14.2.2)` that the morphisms $g$ and $h$ are
equidimensional; since $X_{\eta}$ and $Y_{\eta}$ are isomorphic, the irreducible components of $X_{s}$ and of $Y_{s}$
have all the same dimension. But by hypothesis $X_{s}$ is irreducible and one has seen that $f$ is surjective, hence so
is $f_{s} : X_{s} \to Y_{s}$, which entails that $Y_{s}$ is also irreducible; if $y$ is the generic point of $Y_{s}$,
one has therefore $f(x) = y$, and the relation $\dim(X_{s}) = \dim(Y_{s})$ then entails, by virtue of `(5.6.6)`, that
$\dim(f^{-1}_{s}(y)) = 0$, in other words $f_{s}$ (and consequently also $f$) is indeed quasi-finite at the point $x$,
which completes the proof.

**Corollary (21.12.16).**

<!-- label: IV.21.12.16 -->

*Let $g : X \to S$ be a proper, flat morphism of finite presentation, $h : Y \to S$ a smooth, proper morphism of finite
presentation, $f : X \to Y$ an $S$-morphism. Suppose that the fibres $X_{s} = g^{-1}(s)$ of $g$ are geometrically
irreducible. Let $U$ be the set of $s \in S$ such that $f_{s} : X_{s} \to Y_{s}$ is an isomorphism. Then $U$ is open and
closed in $S$, and the morphism $g^{-1}(U) \to h^{-1}(U)$, restriction of $f$, is an isomorphism.*

The last assertion will result from the first and from `(17.9.5)`. One already knows `(9.6.1, (xi))` that $U$ is locally
constructible in $S$. By virtue of `(1.10.1)`, it suffices to prove that $U$ is stable by specialization and by
generization. To demonstrate these assertions one

<!-- original page 313 -->

can, by a base change $\operatorname{Spec}(\mathcal{O}_{S,s}) \to S$, reduce to the case where $S$ is a local scheme of
closed point $s$ and generic point $\eta$, and one must show that, in order for $f_{s}$ to be an isomorphism, it is
necessary and sufficient that $f_{\eta}$ be one. Now, the sufficiency of this condition results from `(21.12.15)`. To
show that it is necessary, one argues as in the proof of `(21.12.15)` (remarking, with the same notations, that the
projection of the closed point of $S$ is the closed point of `S_0`) to reduce to the case where in addition $S$ is
Noetherian; but then the conclusion results from `(III, 4.6.7, (ii))`.

**Remarks (21.12.17).**

<!-- label: IV.21.12.17 -->

(i) The conclusion of proposition `(21.12.15)` is no longer valid if one eliminates the hypothesis that the fibres
$X_{s}$ are irreducible. Take indeed $S = \operatorname{Spec}(A)$, where $A$ is a discrete valuation ring, $Y =
\mathbb{P}^{1}_{S}$, which is proper and smooth over $S$ `(17.3.9)`. Denote again $s$ and $\eta$ the closed point and
the generic point of $S$; let $z$ be a closed point of $Y_{s}$, for example a point rational over $k = k(s)$, and let
$X$ be the $Y$-prescheme obtained by blowing up the point $z$. Since the polynomial ring `A[T]` is regular `(0, 17.3.7)`
and of dimension `2`, one sees as in the proof of `(15.1.1.6)` that, if $f : X \to Y$ is the structure morphism,
$f^{-1}(z)$ is isomorphic to $\mathbb{P}^{1}$, and on the other hand, the complement of $f^{-1}(z)$ in $X_{s}$ is
isomorphic to $Y_{s} - {z}$, hence $Z_{1} = f^{-1}(z)$ and `Z_2`, the closure in $X_{s}$ of the complement of `Z_1`, are
the two irreducible components of $X_{s}$. Moreover, $f$ is evidently proper and $g = h \circ f$ is flat, since $X$ is
integral `(II, 8.1.4)` and for every affine open $U$ of $X$, the homomorphism $A \to \Gamma(U, \mathcal{O}_{X})$ is
injective `(I, 1.2.7)`, hence $\Gamma(U, \mathcal{O}_{X})$ is a torsion-free $A$-module, and consequently flat since $A$
is a discrete valuation ring $(0_{I}, 6.3.4)$. It is clear that $f_{\eta} : X_{\eta} \to Y_{\eta}$ is an isomorphism,
although $f_{s} : X_{s} \to Y_{s}$ is not.

(ii) The conclusion of `(21.12.15)` also fails if, in the hypotheses, one suppresses the hypothesis that $f$ is proper.
It suffices, to see this, to define $S$ and $Y$ as in (i), but to replace $X$ by the complement $X'$ of `Z_2` in the
prescheme $X$ defined in (i), and $f$ by the restriction $f' : X' \to Y$ of $f$; the morphism $g' : X' \to S$,
restriction of $g$, is still flat, and this time $X'_{s}$ is geometrically irreducible; $X'_{s}$ is moreover isomorphic
to the complement of a closed point in $\mathbb{P}^{1}_{k}$, hence is an affine scheme isomorphic to
$\mathbb{V}^{1}_{k}$; since its image in $Y_{s}$ is reduced to the closed point $z$, $f'$ is not proper `(III, 4.4.2)`
and $f'_{s}$ is not an isomorphism, although $f'_{\eta}$ is one.

(iii) It is possible that the statement of proposition `(21.12.15)` remains valid when one replaces the word
"isomorphism" by "étale morphism" (cf. `(21.12.14, (v))`). The same will then still hold for `(21.12.16)`.

### 21.13. Parafactorial couples. Parafactorial local rings

**Definition (21.13.1).**

<!-- label: IV.21.13.1 -->

*Let $X$ be a ringed space, $Y$ a closed part of $X$, $U = X - Y$. One says that the couple $(X, Y)$ is
**parafactorial** if, for every open $V$ of $X$, the restriction functor $\mathcal{L} \mapsto \mathcal{L} | (U \cap V)$,
from the category of $\mathcal{O}_{V}$-Modules invertible to that of $\mathcal{O}_{U \cap V}$-Modules invertible, is an
equivalence of categories.*

To say that the couple $(X, Y)$ is parafactorial means therefore that, for every open $V$ of $X$, the following
conditions are verified:

1° the functor $\mathcal{L} \mapsto \mathcal{L} | (U \cap V)$ is fully faithful, in other words, for two invertible
$\mathcal{O}_{V}$-Modules $\mathcal{L}$, $\mathcal{L}'$, the restriction map

```text
                       Hom_{𝒪_V}(ℒ, ℒ') → Hom_{𝒪_{U ∩ V}}(ℒ | (U ∩ V), ℒ' | (U ∩ V))
```

is bijective;

2° the functor $\mathcal{L} \mapsto \mathcal{L} | (U \cap V)$ is essentially surjective, in other words, for every

<!-- original page 314 -->

invertible $\mathcal{O}_{U \cap V}$-Module $\mathcal{L}_{0}$, there exists an invertible $\mathcal{O}_{V}$-Module
$\mathcal{L}$ such that $\mathcal{L}_{0}$ is isomorphic to $\mathcal{L} | (U \cap V)$; this is also expressed by saying
that the canonical homomorphism `(21.3.2.4)`

$$ \operatorname{Pic}(V) \to \operatorname{Pic}(U \cap V) $$

is surjective.

**Lemma (21.13.2).**

<!-- label: IV.21.13.2 -->

*Let $f : X' \to X$ be a morphism of ringed spaces; for every open $V$ of $X$, one denotes $f_{V} : f^{-1}(V) \to V$ the
restriction of $f$. The following conditions are equivalent:*

*a) For every open $V$ of $X$, the functor $\mathcal{E} \mapsto f^{*}_{V}(\mathcal{E})$ from the category of
$\mathcal{O}_{V}$-Modules locally free of finite rank into the category of $\mathcal{O}_{f^{-1}(V)}$-Modules locally
free of finite rank is faithful (resp. fully faithful).*

*a') For every open $V$ of $X$, the functor $\mathcal{L} \mapsto f^{*}_{V}(\mathcal{L})$ from the category of
$\mathcal{O}_{V}$-Modules locally free of rank `1` into the category of $\mathcal{O}_{f^{-1}(V)}$-Modules locally free
of rank `1` is faithful (resp. fully faithful).*

*b) For every open $V$ of $X$, the canonical homomorphism $(0_{I}, 4.4.3.2)$ $\mathcal{E} \to
(f_{V})_{*}(f^{*}_{V}(\mathcal{E}))$ is a monomorphism (resp. an isomorphism) for every $\mathcal{O}_{V}$-Module
$\mathcal{E}$ locally free of finite rank.*

*b') The canonical homomorphism $\mathcal{O}_{X} \to f_{*}(\mathcal{O}_{X'})$ is a monomorphism (resp. an isomorphism).*

*Suppose that the canonical homomorphism $\mathcal{O}_{X} \to f_{*}(\mathcal{O}_{X'})$ is bijective; then, for an
$\mathcal{O}_{X'}$-Module $\mathcal{E}'$ locally free of finite rank to be isomorphic to an $\mathcal{O}_{X'}$-Module of
the form $f^{*}(\mathcal{E})$, where $\mathcal{E}$ is an $\mathcal{O}_{X}$-Module locally free of finite rank, it is
necessary and sufficient that the two following conditions be fulfilled:*

*(i) $f_{*}(\mathcal{E}')$ is an $\mathcal{O}_{X}$-Module locally free;*

*(ii) The canonical homomorphism $(0_{I}, 4.4.3.3)$ $f^{*}(f_{*}(\mathcal{E}')) \to \mathcal{E}'$ is an isomorphism.*

*When these two conditions are fulfilled, $\mathcal{E}$ is isomorphic to $f_{*}(\mathcal{E}')$.*

To say that the functor $\mathcal{E} \mapsto f^{*}_{V}(\mathcal{E})$ is faithful (resp. fully faithful) means that for
two $\mathcal{O}_{V}$-Modules $\mathcal{E}_{1}$, $\mathcal{E}_{2}$ locally free of finite rank, the map
$\operatorname{Hom}_{\mathcal{O}_{V}}(\mathcal{E}_{1}, \mathcal{E}_{2}) \to
\operatorname{Hom}_{\mathcal{O}_{f^{-1}(V)}}(f^{*}_{V}(\mathcal{E}_{1}), f^{*}_{V}(\mathcal{E}_{2}))$ is injective
(resp. bijective); since this must hold on replacing $V$ by an open $W \subset V$ and $\mathcal{E}_{1}$,
$\mathcal{E}_{2}$ by $\mathcal{E}_{1} | W$, $\mathcal{E}_{2} | W$, and since
$\operatorname{Hom}_{\mathcal{O}_{W}}(\mathcal{E}_{1} | W, \mathcal{E}_{2} | W) = \Gamma(W,
\mathcal{H}om_{\mathcal{O}_{V}}(\mathcal{E}_{1}, \mathcal{E}_{2}))$, the condition means again that the canonical
homomorphism of sheaves

<!-- label: IV.21.13.2.1 -->

```text
  (21.13.2.1)             ℋom_{𝒪_V}(ℰ_1, ℰ_2) → (f_V)_*(f_V^*(ℋom_{𝒪_V}(ℰ_1, ℰ_2)))
```

is injective (resp. bijective). But since $\mathcal{E}_{1}$ and $\mathcal{E}_{2}$ are locally free of finite rank,
$\mathcal{H}om_{\mathcal{O}_{V}}(\mathcal{E}_{1}, \mathcal{E}_{2})$, isomorphic to $\mathcal{E}^{\vee}_{1}
\otimes_{\mathcal{O}_{V}} \mathcal{E}_{2}$ $(0_{I}, 5.4.2)$, is also locally free of finite rank; this already shows
that b) entails a), and conversely b) is a particular case of a), taking into account the isomorphism $\mathcal{E}
\simeq \mathcal{H}om_{\mathcal{O}_{V}}(\mathcal{O}_{V}, \mathcal{E})$. It is clear that a') is a particular case of a)
and b') a particular case of b). Conversely, since b) is a local property, one can, to verify it, restrict to the case
where $\mathcal{E} = \mathcal{O}_{V}$, and this shows that b') entails b).

If the canonical homomorphism $\mathcal{O}_{X} \to f_{*}(\mathcal{O}_{X'})$ is bijective, and if conditions (i) and (ii)
are fulfilled, it is clear that $\mathcal{E}' = f^{*}(\mathcal{E})$ with $\mathcal{E} = f_{*}(\mathcal{E}')$, up to
isomorphism.

<!-- original page 315 -->

Conversely, suppose that $\mathcal{E}' = f^{*}(\mathcal{E})$, with $\mathcal{E}$ locally free; the question being local
on $X$, one can suppose that $\mathcal{E} = \mathcal{O}_{X}$, whence $\mathcal{E}' = \mathcal{O}_{X'}$, and conditions
(i) and (ii) result from the hypothesis that $\mathcal{O}_{X} \to f_{*}(\mathcal{O}_{X'})$ is an isomorphism.

In this number, we shall apply the preceding lemma to a canonical injection $j : U \to X$, where $U$ is the ringed space
induced by $X$ on an open of $X$. With these notations, `(21.13.2)` translates into:

**Corollary (21.13.3).**

<!-- label: IV.21.13.3 -->

*Let $X$ be a ringed space, $Y$ a closed part of $X$, $U = X - Y$, $j : U \to X$ the canonical injection. The following
conditions are equivalent:*

*a) For every open $V$ of $X$, the restriction functor $\mathcal{E} \mapsto \mathcal{E} | (U \cap V)$ from the category
of $\mathcal{O}_{V}$-Modules locally free of finite rank into the category of $\mathcal{O}_{U \cap V}$-Modules locally
free of finite rank is faithful (resp. fully faithful).*

*a') For every open $V$ of $X$, the restriction functor $\mathcal{L} \mapsto \mathcal{L} | (U \cap V)$ from the category
of $\mathcal{O}_{V}$-Modules locally free of rank `1` into the category of $\mathcal{O}_{U \cap V}$-Modules locally free
of rank `1` is faithful (resp. fully faithful).*

*b) For every open $V$ of $X$, the canonical homomorphism $\mathcal{E} \to (j_{*})(\mathcal{E} | (U \cap V))$ is
injective (resp. bijective) for every $\mathcal{O}_{V}$-Module $\mathcal{E}$ locally free of finite rank.*

*b') The canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is injective (resp. bijective).*

*Suppose that the canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is bijective. Then, for an
$\mathcal{O}_{U}$-Module $\mathcal{E}'$ locally free of finite rank to be of the form $\mathcal{E} | U$, where
$\mathcal{E}$ is an $\mathcal{O}_{X}$-Module locally free of finite rank, it is necessary and sufficient that
$j_{*}(\mathcal{E}')$ be an $\mathcal{O}_{X}$-Module locally free, and in this case, one may take $\mathcal{E} =
j_{*}(\mathcal{E}')$.*

**Lemma (21.13.4).**

<!-- label: IV.21.13.4 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed part of $X$, $U = X - Y$, $j : U \to X$ the canonical
injection. For the canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ to be injective (resp.
bijective), it is necessary and sufficient that $prof_{Y}(\mathcal{O}_{X}) \geqslant 1$ (resp.
$prof_{Y}(\mathcal{O}_{X}) \geqslant 2$) (in other words, that $prof(\mathcal{O}_{X,x}) \geqslant 1$ (resp.
$prof(\mathcal{O}_{X,x}) \geqslant 2$) for every $x \in Y$).*

These assertions are particular cases of `(5.10.2)` and `(5.10.5)`.

**Proposition (21.13.5).**

<!-- label: IV.21.13.5 -->

*Let $X$ be a ringed space, $Y$ a closed part of $X$, $U = X - Y$, $j : U \to X$ the canonical injection. For the couple
$(X, Y)$ to be parafactorial, it is necessary and sufficient that the canonical homomorphism $\mathcal{O}_{X} \to
j_{*}(\mathcal{O}_{U})$ be bijective, and that for every open $V$ of $X$ and every invertible $\mathcal{O}_{U \cap
V}$-Module $\mathcal{L}$, $(j_{V})_{*}(\mathcal{L})$ be an invertible $\mathcal{O}_{V}$-Module (notation of
`(21.13.3)`).*

This is an immediate consequence of definition `(21.13.1)` and of `(21.13.3)`.

**Corollary (21.13.6).**

<!-- label: IV.21.13.6 -->

*Let $X$ be a ringed space, $Y$ a closed part of $X$.*

*(i) If the couple $(X, Y)$ is parafactorial, the same is true of $(W, Y \cap W)$ for every open $W$ of $X$. Conversely,
if $(W_{\alpha})$ is an open covering of $X$ such that each of the couples $(W_{\alpha}, Y \cap W_{\alpha})$ is
parafactorial, then the couple $(X, Y)$ is parafactorial.*

*(ii) If the couple $(X, Y)$ is parafactorial, the same is true of `(X, Y')` for every closed part $Y'$ of $Y$.*

*(iii) Suppose that $X$ is a prescheme, and let $X'$ be a prescheme, $f : X' \to X$ a faithfully flat and quasi-compact
morphism; set $Y' = f^{-1}(Y)$. Suppose that the couple `(X', Y')` is parafactorial and that the open $U = X - Y$ is
retrocompact in $X$ $(0_{III}, 9.1.1)$. Then the couple $(X, Y)$ is parafactorial.*

<!-- original page 316 -->

(i) Since the fact that the canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is bijective is a local
property on $X$, everything reduces (by virtue of `(21.13.5)`) to seeing, denoting by $j_{\alpha}$ the canonical
injection $U \cap W_{\alpha} \to W_{\alpha}$, that one has the following property: if, for every $\alpha$ and for every
invertible $\mathcal{O}_{U \cap W_{\alpha}}$-Module $\mathcal{L}$, $(j_{\alpha})_{*}(\mathcal{L} | (U \cap W_{\alpha}))$
is an invertible $\mathcal{O}_{W_{\alpha}}$-Module, then $j_{*}(\mathcal{L})$ is an invertible $\mathcal{O}_{X}$-Module.
But the property of being an invertible $\mathcal{O}_{X}$-Module is local on $X$, and $(W_{\alpha})$ is an open covering
of $X$; since one has $j_{*}(\mathcal{L}) | W_{\alpha} = (j_{\alpha})_{*}(\mathcal{L} | (U \cap W_{\alpha}))$, this
proves our assertion.

(ii) Set $U' = X - Y'$ and let $j' : U' \to X$ be the canonical injection. To say that the homomorphism $\mathcal{O}_{X}
\to j'_{*}(\mathcal{O}_{U'})$ is bijective amounts to saying that for every open $V$ of $X$, the homomorphism $\Gamma(V,
\mathcal{O}_{X}) \to \Gamma(V \cap U', \mathcal{O}_{X})$ is bijective; but the composite homomorphism

```text
                       Γ(V, 𝒪_X) → Γ(V ∩ U', 𝒪_X) → Γ(V ∩ U, 𝒪_X)
```

is bijective by hypothesis `(21.13.5)`, and on replacing $V$ by $V \cap U'$, one sees that $\Gamma(V \cap U',
\mathcal{O}_{X}) \to \Gamma(V \cap U, \mathcal{O}_{X})$ is bijective, hence $\Gamma(V, \mathcal{O}_{X}) \to \Gamma(V
\cap U', \mathcal{O}_{X})$ is bijective. Note next that if $j'' : U \to U'$ is the canonical injection and if
$\mathcal{L}'$ is an invertible $\mathcal{O}_{U'}$-Module, $\mathcal{L}' | U$ is an invertible $\mathcal{O}_{U}$-Module,
hence $j_{*}(\mathcal{L}' | U) = j'_{*}(j''_{*}(\mathcal{L}' | U))$ is by hypothesis an invertible
$\mathcal{O}_{X}$-Module. Since the couple $(U', U' \cap Y)$ is parafactorial by virtue of (i), one has
$j''_{*}(\mathcal{L}' | U) \simeq \mathcal{L}'$, hence $j'_{*}(\mathcal{L}')$ is an invertible $\mathcal{O}_{X}$-Module.
It then suffices, to conclude, to replace in the preceding argument $X$, $U$ and $U'$ by $V$, $V \cap U$ and $V \cap
U'$, where $V$ is an open of $X$.

(iii) Set $U' = X' - Y' = f^{-1}(U)$ and note that since one is dealing with preschemes, one can write $U' = U
\times_{X} X'$; let $f_{U} : f^{-1}(U) \to U$ be the restriction of $f$ and let $j' : U' \to X'$ be the canonical
injection, which one also writes $j_{(X')}$. Let us first show that the canonical homomorphism $\rho : \mathcal{O}_{X}
\to j_{*}(\mathcal{O}_{U})$ is bijective; for this, note that by hypothesis the canonical homomorphism $\mathcal{O}_{X'}
\to j'_{*}(\mathcal{O}_{U'})$ is bijective; but since the morphism $j$ is quasi-compact and separated by hypothesis, and
the morphism $f$ flat, $j'_{*}(\mathcal{O}_{U'}) = j'_{*}(f^{*}_{U}(\mathcal{O}_{U}))$ is canonically identified with
$f^{*}(j_{*}(\mathcal{O}_{U}))$ by virtue of `(2.3.1)`; since $\mathcal{O}_{X'} = f^{*}(\mathcal{O}_{X})$, one sees that
the homomorphism $f^{*}(\rho) : f^{*}(\mathcal{O}_{X}) \to f^{*}(j_{*}(\mathcal{O}_{U}))$ is bijective; one concludes
that $\rho$ is bijective since $f$ is faithfully flat `(2.2.7)`. Consider next an invertible $\mathcal{O}_{U}$-Module
$\mathcal{L}$, and let $\mathcal{L}' = f^{*}_{U}(\mathcal{L})$, which is an invertible $\mathcal{O}_{U'}$-Module. By
hypothesis $j'_{*}(f^{*}_{U}(\mathcal{L}))$ is an invertible $\mathcal{O}_{X'}$-Module, which is isomorphic to
$f^{*}(j_{*}(\mathcal{L}))$ by `(2.3.1)` as above. But since $f$ is faithfully flat and quasi-compact, this entails that
$j_{*}(\mathcal{L})$ is an $\mathcal{O}_{X}$-Module locally free `(2.5.2)`. To complete the proof, it suffices to
replace $X$ by an open $V$ and $X'$ by $f^{-1}(V)$ in the foregoing.

**Definition (21.13.7).**

<!-- label: IV.21.13.7 -->

*One says that a local ring $A$ is **parafactorial** if, setting $X = \operatorname{Spec}(A)$ and denoting by $a$ the
closed point of $X$, the couple `(X, {a})` is parafactorial.*

**Proposition (21.13.8).**

<!-- label: IV.21.13.8 -->

*The notations being those of `(21.13.7)`, set $U = X - {a}$. For $A$ to be parafactorial, it is necessary and
sufficient that it verify the following conditions:*

*(i) The canonical homomorphism $A = \Gamma(X, \mathcal{O}_{X}) \to \Gamma(U, \mathcal{O}_{X})$ is bijective,*

*(ii) $\operatorname{Pic}(U) = 0$.*

<!-- original page 317 -->

*If moreover $A$ is Noetherian, condition (i) is equivalent to*

*(i bis) $prof(A) \geqslant 2$.*

Indeed, the only open of $X$ containing $a$ is $X$ itself, and consequently every invertible $\mathcal{O}_{X}$-Module is
isomorphic to $\mathcal{O}_{X}$, in other words $\operatorname{Pic}(X) = 0$; the first assertion therefore results from
definition `(21.13.1)` and from `(21.13.3)`. The second assertion is a particular case of `(21.13.4)`.

**Examples (21.13.9).**

<!-- label: IV.21.13.9 -->

(i) A parafactorial Noetherian local ring is necessarily of dimension $\geqslant 2$ by virtue of `(21.13.8)`; in other
words a Noetherian local ring of dimension $\leqslant 1$ is not parafactorial.

(ii) A factorial Noetherian local ring $A$ of dimension $\geqslant 2$ is parafactorial, as follows from `(21.13.8)` and
`(21.6.14)`.

(iii) If $A$ is a Noetherian local ring of dimension $\geqslant 3$ and parafactorial, it is not necessarily normal nor
even reduced. Consider a regular local ring $B$ of dimension $\geqslant 3$, and let $A = D_{B}(B)$ `(0, 18.2.3)`,
isomorphic to $B[T]/(T^{2})$; one sees at once that one has `prof(A) = prof(B) = dim(B) ⩾ 3`. To show that $A$ is
parafactorial, it suffices, with the notations of `(21.13.8)`, to prove that $\operatorname{Pic}(U) = 0$. Let
$\mathcal{J}$ be the kernel of the augmentation $A \to B$, which is such that $\mathcal{J}^{2} = 0$ and which, as a
$B$-module, is isomorphic to $B$. Since $B = A/\mathcal{J}$, $X = \operatorname{Spec}(A)$ and $X_{0} =
\operatorname{Spec}(B)$ have the same underlying space; if $\mathcal{I} = \tilde{\mathcal{J}}$, `X_0` is the sub-scheme
defined by $\mathcal{I}$, we shall denote `U_0` the sub-prescheme induced by `X_0` on the open $U$. For every $z \in
\mathcal{J}$, set $\phi(z) = 1 + z$; since $(1 + z)(1 - z) = 1$, $1 + z$ is invertible in $A$ and $\phi(\mathcal{J})$ is
the kernel of the canonical surjective homomorphism of multiplicative groups $A^{\times} \to B^{\times}$; in other
words, one has an exact sequence of commutative groups

```text
                       0 → 𝒥 →^φ A^× → B^× → 1
```

(the last three groups being multiplicative, the first two additive). For the same reason, for every $t \in A$, one has
the exact sequence

$$ 0 \to \mathcal{J}_{t} \to (A_{t})^{\times} \to (B_{t_{0}})^{\times} \to 1 $$

denoting by $t_{0}$ the image of $t$ in $B$, since $B_{t_{0}} = A_{t} / \mathcal{J}_{t}$; in other words, one has an
exact sequence of sheaves of commutative groups on the topological space $X$

$$ 0 \to \mathcal{I} \to \mathcal{O}^{\times}_{X} \to \mathcal{O}^{\times}_{X_{0}} \to 1 $$

whence by restriction to the open $U$, an exact sequence

```text
                       0 → ℐ | U → 𝒪_U^× → 𝒪_{U_0}^× → 1.
```

By the cohomology exact sequence, one deduces an exact sequence

<!-- label: IV.21.13.9.1 -->

```text
  (21.13.9.1)             H^1(U, ℐ) → H^1(U, 𝒪_U^×) → H^1(U, 𝒪_{U_0}^×).
```

But since $\mathcal{J}$ is a $B$-module isomorphic to $B$, one has $H^{1}(U, \mathcal{I}) \simeq H^{1}(U_{0},
\mathcal{O}_{U_{0}})$, and it follows from chap. III, 3rd part (see also `[41, III, Example III-1]`) that one has

<!-- original page 318 -->

$H^{1}(U_{0}, \mathcal{O}_{U_{0}}) = 0$ by reason of the relation $prof(B) \geqslant 3$. Moreover, since $B$ is
factorial, one has $H^{1}(U, \mathcal{O}^{\times}_{U_{0}}) = \operatorname{Pic}(U_{0}) = 0$; one therefore draws indeed
from the preceding exact sequence that $\operatorname{Pic}(U) = H^{1}(U, \mathcal{O}^{\times}_{U}) = 0$.

(iv) There also exist Noetherian local rings of dimension `3` which are integral, integrally closed and parafactorial,
but not factorial. Let indeed $B$ be a Noetherian local ring, complete, integral and integrally closed, of dimension
$\geqslant 2$ and non-factorial (for example the completion of the localized ring of the integral algebra $k[U, V,
W]/(W^{2} - UV)$ at the maximal ideal image of $(U) + (V) + (W)$). Then it will follow from what we shall see below
`(21.14.2)` that the local ring $A = B[[T]]$ of formal series in $T$ over $B$ is parafactorial, but it is not factorial,
otherwise $B$ would be by virtue of `(21.13.12)` below.

(v) One can show that an absolute complete intersection local ring `(19.3.1)` of dimension $\geqslant 4$ is
parafactorial (cf. `[41, XI, 3.13 (i))]`).

(vi) One has seen (Remark (ii)) that every factorial Noetherian local ring $A$ of dimension `2` is parafactorial. But
there are Noetherian local rings of dimension `2` which are parafactorial and non-factorial. One can show that, for a
Noetherian local ring $A$ of dimension `2` to be parafactorial and non-factorial, it is necessary and sufficient that it
satisfy the three following conditions:

1° $A$ is a Cohen-Macaulay ring (in other words $prof(A) = 2$).

2° $A$ is integral and if $A'$ is its integral closure, $A'$ is factorial and is a finite $A$-algebra.

3° Let $\mathcal{J}$ be the conductor of $A$ in $A'$ (annihilator of the $A$-module $A'/A$, or also the largest ideal of
$A'$ contained in $A$); set $B = A/\mathcal{J}$, $B' = A'/\mathcal{J}$; then $\dim(B) = 1$ (which implies $A' \neq A$,
in other words $A$ is not integrally closed), and the canonical map $D(B) \to D(B')$ `(21.4.5)` is surjective.

One can show moreover that these conditions entail the following property:

4° The ring $B'$ (and a fortiori $B \subset B'$) is reduced, and the morphism $\operatorname{Spec}(B') \to
\operatorname{Spec}(B)$ is bijective.

If one sets $X = \operatorname{Spec}(A)$, $X' = \operatorname{Spec}(A')$, $Y = \operatorname{Spec}(B)$, $Y' =
\operatorname{Spec}(B')$, so that $Y$ (resp. $Y'$) is defined by the ideal $\mathcal{J}$ of $A$ (resp. $A'$), the
structural morphism $f : X' \to X$ is an isomorphism of $X' - Y'$ onto $X - Y$ (Bourbaki, _Alg. comm._, chap. V, §1, n°
5, cor. 5 of prop. 16). One sees therefore by virtue of 4° that $f$ is a bijective morphism; in other words, $X$ is a
unibranch prescheme `(6.15.1)` (and in particular $A'$ is a Noetherian local ring); in general $X$ is not geometrically
unibranch. The space $Y$, of dimension `1`, is constituted by the closed point $x$ of $X$ and the maximal points $y_{i}$
($1 \leqslant i \leqslant r$) of $Y$, and the unique point $y'_{i}$ of $Y'$ above $y_{i}$ is also a maximal point of
$Y'$; since $B$ and $B'$ are reduced, one deduces that one has $\mathfrak{m}_{X', z'} = \mathfrak{m}_{X, z}$ for $z =
y_{i}$ and $z' = y'_{i}$; this relation is also evidently verified for $z \in Y$ and $z'$ the unique point of
$f^{-1}(z)$, hence for every $z \in U = X - {x}$ and $z'$ the unique point of $f^{-1}(z)$. In particular, if the ring
$A$ is of characteristic `0` `(0, 21.1.1)` one sees that $U'$ is unramified over $U$ (but not étale in general).

We shall restrict ourselves here to demonstrating that conditions 1°, 2°, 3° above are sufficient for $A$ to be

<!-- original page 319 -->

parafactorial. Now, by virtue of condition 1° and of `(21.13.8)`, it suffices to show that $\operatorname{Pic}(U) = 0$.

Since $A'$ is factorial by virtue of 2°, one has $\operatorname{Pic}(U') = 0$, and one deduces from `(21.8.5, (ii))` an
exact sequence

```text
                       1 → (⨁_{s ∈ S} (A'_{p'_s})^× / (A_{p_s})^×) / Im(Γ(U', 𝒪_{U'}^×)) → Pic(U) → Pic(U') → 0
```

and one must therefore show that the second term of this sequence is reduced to the neutral element, taking for $S$ the
set of the $y_{i}$ ($1 \leqslant i \leqslant r$) and noting that here $f_{*}(\mathcal{O}_{X'}) = A'$ is the
$\mathcal{O}_{X}$-Algebra `Ã'`. Let $p_{i}$, $p'_{i}$ be the prime ideals of $A$ and $A'$ corresponding to the points
$y_{i}$, $y'_{i}$, and remark that $p'_{i} \cap A = p_{i}$; let us give for each $i$ an invertible element
$a'_{i}/s_{i}$ of $A'_{p'_{i}}$ with $a'_{i} \in A'$, $s_{i} \notin p'_{i}$; since we have only to examine the quotient
groups $A'^{\times}_{p'_{i}} / A^{\times}_{p_{i}}$, one can suppose $s_{i} = 1$ for all $i$; let $b'_{i} \in B' =
A'/\mathcal{J}$ be the canonical image of $a'_{i}$, so that $b'_{i}$ is a non-zero element of $k(y'_{i}) = B'_{p'_{i}}$.
The set $U \cap Y$ formed by the $y_{i}$ is an affine open of the form $D(t)$ in $Y$, with $t \notin \mathfrak{m}$, the
maximal ideal of $A$; there exists therefore an invertible element $b \in B'_{t}$ whose $b'_{i}$ are the canonical
images, and since $t$ is regular in the integral ring $A'$, one can suppose $b$ of the form $b''/t^{n}$, where $b'' \in
B'$ is invertible. Let `a''` be an element of $A'$ in the class `b''`, which is therefore necessarily invertible; $a' =
a''/t^{n}$ is invertible in $A'_{t}$ and for every $i$, one has $u_{i} = a' - a'_{i} \in \mathcal{J}$, whence $t^{n}
a'_{i} = a'' - t^{n} u_{i} = a''(1 - a''^{-1} t^{n} u_{i})$; but $a''^{-1} t^{n} u_{i} \in \mathcal{J} \subset
\mathfrak{m}$, hence $1 - a''^{-1} t^{n} u_{i}$ is an invertible element of $A$, and the classes of $a'$ and $a'_{i}$ in
$A'^{\times}_{p'_{i}} / A^{\times}_{p_{i}}$ are the same, which completes the proof.

To have an explicit example of a parafactorial ring of dimension `2` obtained in this manner and *non-factorial*,
consider the ring $E = \mathbb{R}[[U, V]]/(U^{2} + V^{2})$, whose integral closure $E'$ identifies with
$\mathbb{C}[[U]]$ `(6.15.11)`. If one sets $A = E[[T]]$, the integral closure of $A$ is the ring $A' = E'[[T]]$
(Bourbaki, _Alg. comm._, chap. V, §1, n° 4, prop. 14); one verifies at once that the conductor of $E$ in $E'$ is the
maximal ideal $\mathfrak{n}$ of $E$, hence the conductor $\mathcal{J}$ of $A$ in $A'$ is $\mathfrak{n}[[T]]$, and one
has $B = A/\mathcal{J} \simeq \mathbb{R}[[T]]$, $B' = A'/\mathcal{J} \simeq \mathbb{C}[[T]]$. It is then immediate that
conditions 1°, 2° and 3° stated above are indeed verified, but $A$ is not even integrally closed.

One can vary this example, and the reader will see without difficulty that if $k$ is an algebraically closed field, the
ring $A$, localization of the ring $k[U, V, W]/(U^{2} - WV^{2})$ at the maximal ideal generated by the images of $U$,
$V$ and $W$, verifies also conditions 1°, 2° and 3° above.

It could be that these three conditions imply even that each of the rings $B'/p'_{i}$ is a discrete valuation ring,
which would entail that $A'$ is even a regular ring.

**Proposition (21.13.10).**

<!-- label: IV.21.13.10 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed part of $X$. For the couple $(X, Y)$ to be parafactorial it is
necessary and sufficient that, for every $y \in Y$, the local ring $\mathcal{O}_{X,y}$ be parafactorial.*

Set $U = X - Y$ and let $j : U \to X$ be the canonical injection.

By virtue of `(21.13.4)`, to say that the canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is
injective is equivalent to saying that each of the local rings $\mathcal{O}_{X,y}$ for $y \in Y$ satisfies condition (i
bis) of `(21.13.8)`.

Let us first show that if the couple $(X, Y)$ is parafactorial, each of the rings $\mathcal{O}_{X,y}$ ($y \in Y$) is
parafactorial. Taking the preceding remark into account, everything reduces to seeing that, if one sets $T_{y} =
\operatorname{Spec}(\mathcal{O}_{X,y})$ and $U_{y} = T_{y} - {y}$, every invertible $\mathcal{O}_{U_{y}}$-Module
$\mathcal{L}_{0}$ is isomorphic to $\mathcal{O}_{U_{y}}$. Now, when $V$ runs through the set of affine open
neighbourhoods of $y$ in $X$, it follows from `(8.2.13)` and `(I, 2.4.2)` that the prescheme $U_{y}$ is projective limit
of the preschemes induced by $X$ on the opens $V - (V \cap {y})$ which are quasi-compact since $X$ is locally
Noetherian. Since the $U_{V} = V - (V \cap {y})$ are separated, it follows from `(8.5.2, (ii))` and `(8.5.5)` that there
is an affine open neighbourhood $V$ of $y$ in $X$ and an invertible $\mathcal{O}_{U_{V}}$-Module $\mathcal{L}_{V}$ such
that $\mathcal{L}_{0}$ is the sheaf induced by $\mathcal{L}_{V}$ on $U_{y}$. But the hypothesis entails, by virtue of
`(21.13.6, (i) and (ii))`, that the couple $(V, V \cap {y})$ is parafactorial; one concludes by definition `(21.13.1)`
that there exists a $\mathcal{O}_{V}$-Module invertible $\mathcal{L}_{V}'$ inducing $\mathcal{L}_{V}$ on `U_V`.
Replacing if needed $V$ by a smaller open neighbourhood of $y$, one can suppose that $\mathcal{L}_{V}'$ is isomorphic to
$\mathcal{O}_{V}$, whence one concludes that $\mathcal{L}_{0}$ is isomorphic to $\mathcal{O}_{U_{y}}$.

Conversely, let us prove that if all the $\mathcal{O}_{X,y}$ ($y \in Y$) are parafactorial the couple $(X, Y)$ is
parafactorial. One is evidently reduced, taking the remark at the beginning into account, to showing that for every
invertible $\mathcal{O}_{U}$-Module $\mathcal{L}$, $j_{*}(\mathcal{L})$ is an invertible $\mathcal{O}_{X}$-Module
`(21.13.5)`. The question being local on $X$, one can suppose $X$ Noetherian. The set of $x \in X$ such that the
restriction of $j_{*}(\mathcal{L})$ to an open neighbourhood of $x$ in $X$ is invertible is evidently open in $X$; one
must show that $V = X$. For this, suppose the contrary and set $Z = X - V \neq \emptyset$. Let $y$ be a maximal point of
$Z$; since $Z \subset Y$ by definition, $\mathcal{O}_{X,y}$ is by hypothesis a parafactorial ring. Replacing if needed
$X$ by an open neighbourhood of $y$ in $X$, one can suppose that the restriction of $j_{*}(\mathcal{L})$

<!-- original page 320 -->

to $V - (V \cap {y})$ is invertible; hence, with the notations introduced above, the $\mathcal{O}_{U_{y}}$-Module
$\mathcal{L}_{0}$ induced by $j_{*}(\mathcal{L})$ on $U_{y}$ is invertible. Since $\mathcal{O}_{X,y}$ is parafactorial,
$\mathcal{L}_{0}$ is induced by an invertible $\mathcal{O}_{T_{y}}$-Module $\mathcal{L}'$; but since $T_{y}$ is the
projective limit of the open neighbourhoods $W$ of $y$ in $X$, one can again apply `(8.5.2, (ii))` and `(8.5.5)`,
proving the existence of such a neighbourhood $W$ and of an invertible $\mathcal{O}_{W}$-Module $\mathcal{L}''$ inducing
$\mathcal{L}'$ on $T_{y}$, hence inducing $\mathcal{L}_{0}$ on $U_{y}$; applying this time `(8.5.2.5)` and
`(8.5.2, (i))`, one deduces that on replacing if needed $W$ by a smaller open neighbourhood of $y$, one can suppose that
the restrictions of $j_{*}(\mathcal{L})$ and of $\mathcal{L}''$ to $W - (W \cap {y})$ are equal. If one then sets $V_{1}
= V \cup W$ and if one denotes by $\mathcal{L}_{1}$ the invertible $\mathcal{O}_{V_{1}}$-Module equal to $\mathcal{L}''$
in $W$, to $j_{*}(\mathcal{L}) | V$ in $V$, one has $U \subset V_{1}$ and $\mathcal{L}_{1} | U = \mathcal{L}$. One then
concludes from the fact that the homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is bijective and from
`(21.13.2, b))` that $j_{*}(\mathcal{L}) | V_{1}$ is isomorphic to $\mathcal{L}_{1}$, hence invertible. But this
contradicts the definition of $V$, and therefore concludes the proof of `(21.13.10)`.

**Corollary (21.13.11).**

<!-- label: IV.21.13.11 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed part of $X$, $U = X - Y$. Suppose that the couple $(X, Y)$ is
parafactorial and that $U$ is locally factorial; in other words `(21.13.10)`, for every $x \in X$, the ring
$\mathcal{O}_{X,x}$ is: 1° parafactorial if $x \in Y$; 2° factorial if $x \notin Y$. Then $X$ is locally factorial (in
other words, $\mathcal{O}_{X,x}$ is in fact factorial for every $x \in X$).*

Suppose indeed the contrary, and let $y$ be a point of $Y$ such that $\mathcal{O}_{X,y}$ is not factorial and has
minimal dimension among all points of $Y$ having this property. Then, if one sets $T_{y} =
\operatorname{Spec}(\mathcal{O}_{X,y})$, $U_{y} = T_{y} - {y}$, the hypothesis that $\mathcal{O}_{X,y}$ is parafactorial
entails $\operatorname{Pic}(U_{y}) = 0$ and $prof(\mathcal{O}_{X,y}) \geqslant 2$ `(21.13.8)`; moreover the choice of
$y$ entails that $U_{y}$ is locally factorial. But then `(21.6.14)` proves that $\mathcal{O}_{X,y}$ is factorial,
contrary to hypothesis.

**Proposition (21.13.12).**

<!-- label: IV.21.13.12 -->

*Let $A$, $B$ be two Noetherian local rings, $\rho : A \to B$ a local homomorphism making $B$ a flat $A$-module. Then,
if $B$ is factorial, so is $A$.*

One already knows that $A$ is integral and integrally closed `(6.5.4)`, hence one can restrict to the case where
$\dim(A) \geqslant 2$, and reason by recurrence on $n = \dim(A)$. Let $X = \operatorname{Spec}(A)$, $a$ the closed point
of $X$, $X' = \operatorname{Spec}(B)$, $f : X' \to X$ the structural morphism, $U = X - {a}$, $U' = f^{-1}(U)$.

The local rings $\mathcal{O}_{X', x'}$ at points $x' \in f^{-1}(a)$ are factorial and of dimension $\geqslant 2$
`(6.1.2)`, hence parafactorial `(21.13.9, (ii))`; one concludes `(21.13.10)` that the couple $(X', f^{-1}(a))$ is
parafactorial. By virtue of `(21.13.6, (iii))`, this shows that the ring $A$ is parafactorial, hence $prof(A) \geqslant
2$ and $\operatorname{Pic}(U) = 0$ `(21.13.8)`. Finally, the local rings of $U$ being of dimension $< n$, the recurrence
hypothesis proves that $U$ is locally factorial; the conclusion then results from `(21.6.14)`.

**(21.13.12.1).** Note that the statement `(21.13.12)` where one replaces "factorial" by "parafactorial" is no longer
exact, as shows the example where $A = k$ is a field and $B$ the factorial local ring $k[[T_{1}, T_{2}]]$. However, it
follows from `(21.13.6, (iii))` that, under the conditions of `(21.13.12)`, if $\mathfrak{m}$ denotes the maximal ideal
of $A$ and if $\mathfrak{m}B$ is an ideal

<!-- original page 321 -->

of definition of $B$ (in other words, if $\dim(B/\mathfrak{m}B) = 0$), then, when $B$ is parafactorial, so is $A$. In
particular, if the completion `Â` of a Noetherian local ring is parafactorial, so is $A$.

**Remark (21.13.13).**

<!-- label: IV.21.13.13 -->

A part of the foregoing definitions and results is attached to more general considerations on the cohomology of sheaves
of commutative groups on a topological space, developed in chap. III, 3rd part, and we have given here an independent
exposition only for the convenience of the reader. Indeed, if $X$ is a ringed space, one has a canonical equivalence
between the category of invertible $\mathcal{O}_{X}$-Modules and that of principal homogeneous sheaves under the sheaf
of groups $\mathcal{O}^{\times}_{X}$ `(16.5.15)`. This equivalence is defined by associating to every invertible
$\mathcal{O}_{X}$-Module $\mathcal{L}$ the sheaf $\mathcal{L}^{*} = \mathcal{Is}om_{\mathcal{O}_{X}}(\mathcal{O}_{X},
\mathcal{L})$ of germs of isomorphisms of $\mathcal{O}_{X}$ onto $\mathcal{L}$; it is immediate that $\mathcal{L}^{*}$
is canonically equipped with a structure of principal homogeneous sheaf under $\mathcal{O}^{\times}_{X} =
\mathcal{Is}om_{\mathcal{O}_{X}}(\mathcal{O}_{X}, \mathcal{O}_{X})$. The verification of the fact that the functor
$\mathcal{L} \mapsto \mathcal{L}^{*}$ is an equivalence of categories is immediate. That being the case, consider in a
general way a topological space $X$ and a sheaf of groups $\mathcal{G}$ on $X$; let $Y$ be a closed part of $X$, set $U
= X - Y$, and let $i$ be an integer such that $0 \leqslant i \leqslant 2$; one will say that the couple $(X, Y)$ is
**$i$-pure for $\mathcal{G}$** if, for every open $V$ of $X$, the restriction functor $\mathcal{S} \mapsto \mathcal{S} |
(U \cap V)$, from the category of principal homogeneous sheaves under the sheaf of groups $\mathcal{G} | V$, into the
analogous category under the sheaf of groups $\mathcal{G} | (U \cap V)$, is faithful ($i = 0$), resp. fully faithful ($i
= 1$), resp. an equivalence of categories ($i = 2$). In the case where $X$ is a ringed space and $\mathcal{G} =
\mathcal{O}^{\times}_{X}$, to say that $(X, Y)$ is $i$-pure means therefore for $i = 0$, that the homomorphism
$\mathcal{O}^{\times}_{X} \to j_{*}(\mathcal{O}^{\times}_{U})$ is *injective*; for $i = 1$, that this homomorphism is
*bijective*; and finally, for $i = 2$, that the couple $(X, Y)$ is *parafactorial* `(21.13.3)`.

Returning to the general case, recall that the morphisms in the category of principal sheaves under $\mathcal{G}$ are by
definition the *isomorphisms*. To say that the couple $(X, Y)$ is `0`-pure means therefore that for every open $V$ of
$X$, the canonical homomorphism $H^{0}(V, \mathcal{G}) \to H^{0}(U \cap V, \mathcal{G})$ is injective; to say that the
couple $(X, Y)$ is `1`-pure means that the canonical homomorphism $H^{0}(V, \mathcal{G}) \to H^{0}(U \cap V,
\mathcal{G})$ is bijective (and then the canonical homomorphism $H^{1}(V, \mathcal{G}) \to H^{1}(U \cap V, \mathcal{G})$
is injective); finally, one can show that for the couple $(X, Y)$ to be `2`-pure, it is necessary and sufficient that
the homomorphisms $H^{i}(V, \mathcal{G}) \to H^{i}(U \cap V, \mathcal{G})$ be bijective for $i = 0$ and $i = 1$. When
$\mathcal{G}$ is a sheaf of commutative groups, introducing the cohomology sheaves $\mathcal{H}^{p}_{Y}(\mathcal{G})$
defined in chap. III, 3rd part, to say that $(X, Y)$ is $i$-pure for $i \leqslant 2$ means that
$\mathcal{H}^{p}_{Y}(\mathcal{G}) = 0$ for $p \leqslant i$; in this form, the notion generalizes immediately for every
integer $i$.

**Proposition (21.13.14).**

<!-- label: IV.21.13.14 -->

*Let $X$ be a locally Noetherian normal prescheme, $(U_{\lambda})_{\lambda \in L}$ a filtering decreasing family of
opens of $X$. The following conditions are equivalent:*

*a) Every `1`-codimensional cycle $Z$ on $X$ such that there exists an index $\lambda$ for which $Z | U_{\lambda}$ is
locally principal `(21.6.7)`, is locally principal.*

*b) For every $x \in X$ such that $\dim(\mathcal{O}_{X,x}) \geqslant 2$ and such that $x$ does not belong to $\bigcap
U_{\lambda}$, the ring $\mathcal{O}_{X,x}$ is parafactorial.*

<!-- original page 322 -->

*b') For every closed part $Y$ of $X$ such that $codim(Y, X) \geqslant 2$ and such that there exists $\lambda$ for which
$Y \subset X - U_{\lambda}$, the couple $(X, Y)$ is parafactorial.*

Property a) can again be expressed in the following manner: if the closed set $N$ of points $x \in X$ where $Z$ is not
principal is contained in one of the $X - U_{\lambda}$, then $Z$ is locally principal. Since $X$ is normal, the
condition $\dim(\mathcal{O}_{X,x}) \leqslant 1$ entails that $\mathcal{O}_{X,x}$ is a field or a discrete valuation
ring, hence $Z_{x}$ is principal; in other words, one has necessarily $codim(N, X) \geqslant 2$ `(5.1.3)`. Property a)
is therefore equivalent to the following:

a') *If there exists a closed set $Y$ contained in one of the $X - U_{\lambda}$, such that $codim(Y, X) \geqslant 2$ and
such that $Z | X - Y$ is locally principal, then $Z$ is locally principal.*

Note on the other hand that b) implies b') by virtue of `(21.13.10)`; conversely, if b') is verified and if $x \notin
U_{\lambda}$, then $Y = {\bar{x}}$ is contained in $X - U_{\lambda}$ and one has $codim(Y, X) \geqslant 2$, hence it
follows again from `(21.13.10)` that $\mathcal{O}_{X,x}$ is parafactorial, which proves the equivalence of b) and b').
One is thus reduced to proving the equivalence of a') and b'). Note that since $X$ is normal, one has, for every closed
part $Y$ of $X$ such that $codim(Y, X) \geqslant 2$, $prof_{Y}(\mathcal{O}_{X}) \geqslant 2$ `(5.8.6)`; if one sets $U =
X - Y$, the homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is therefore bijective `(21.13.4)`; since the
conditions a') and b') are local, one sees that it suffices to show the equivalence of the following conditions, when
$X$ is Noetherian and normal and $Y$ is closed in $X$ and such that $codim(Y, X) \geqslant 2$:

a'') *For every `1`-codimensional cycle $Z$ on $X$, the hypothesis that $Z | U$ (where $U = X - Y$) is locally principal
entails that $Z$ itself is locally principal.*

b'') *The canonical homomorphism $\operatorname{Pic}(X) \to \operatorname{Pic}(U)$ is surjective.*

Let us first prove that a'') entails b''); an element $\zeta_{0} \in \operatorname{Pic}(U)$ has for image in $Cl(U)$
`(21.6.11)` the class of a `1`-codimensional cycle `Z_0` on $U$, which is locally principal. The hypothesis $codim(Y, X)
\geqslant 2$ entails that the restriction homomorphism $\mathcal{Z}^{1}(X) \to \mathcal{Z}^{1}(U)$ is bijective, hence
$Z_{0} = Z | U$, where $Z$ is a `1`-codimensional cycle on $X$; since `Z_0` is locally principal, so is $Z$ by virtue of
a''); it follows from `(21.6.11)` that the image of $Z$ in $Cl(X)$ is the image of a unique element $\zeta \in
\operatorname{Pic}(X)$, and it is clear then that $\zeta_{0}$ is the image of $\zeta$.

Conversely, let us prove that b'') entails a''). Let then $Z$ be a `1`-codimensional cycle on $X$ such that $Z | U$ is
locally principal; the image of $Z | U$ in $Cl(U)$ is therefore the image of a unique element $\zeta_{0} \in
\operatorname{Pic}(U)$ `(21.6.11)`. By hypothesis there exists $\zeta \in \operatorname{Pic}(X)$ whose image in
$\operatorname{Pic}(U)$ is $\zeta_{0}$; the image of $\zeta$ in $Cl(X)$ is therefore the class of a `1`-codimensional
cycle $Z'$ on $X$ such that $Z | U$ and $Z' | U$ are linearly equivalent. But since $U$ is schematically dense in $X$,
the image of $\mathcal{Z}^{1}_{princ}(X)$ by the isomorphism $\mathcal{Z}^{1}(X) \to \mathcal{Z}^{1}(U)$ is
$\mathcal{Z}^{1}_{princ}(U)$, hence $Z$ and $Z'$ are linearly equivalent, and since $Z'$ is locally principal, so is
$Z$.

**Corollary (21.13.15).**

<!-- label: IV.21.13.15 -->

*Let $X$ be a locally Noetherian and normal prescheme, $S$ a part of $X$. The following conditions are equivalent:*

*a) Every `1`-codimensional cycle on $X$ which is principal at the points of $S$ is locally principal.*

<!-- original page 323 -->

*b) For every $x \in X$ which is not a generization of a point of $S$ (in other words, such that ${\bar{x}} \cap S =
\emptyset$) and which is such that $\dim(\mathcal{O}_{X,x}) \geqslant 2$, the ring $\mathcal{O}_{X,x}$ is
parafactorial.*

It is clear that the set $S'$ of points of $X$ generizations of points of $S$ is the intersection of the open
neighbourhoods of $S$. One can restrict to the case where $X$ is Noetherian (properties a) and b) being local on $X$);
since every `1`-codimensional cycle on $X$ which is principal at the points of $S$ is also so at the points of an open
neighbourhood of $S$, one sees that condition a) of `(21.13.15)` is equivalent to condition a) of `(21.13.14)` applied
to the family $(U_{\lambda})$ of open neighbourhoods of $S$. The corollary then results from the equivalence of a) and
b) in `(21.13.14)`.

**Remark (21.13.16).**

<!-- label: IV.21.13.16 -->

Under the general conditions of `(21.13.14)`, suppose moreover that one has $\lim \operatorname{Pic}(U_{\lambda}) = 0$.
Then condition a) of `(21.13.14)` is also equivalent to the following:

c) *Every `1`-codimensional cycle on $X$ whose support is contained in one of the sets $X - U_{\lambda}$ is locally
principal.*

One can restrict to the case where $X$ is irreducible and all $U_{\lambda}$ are non-empty. It is clear that a) entails
c), for if the `1`-codimensional cycle $Z$ on $X$ has its support in $X - U_{\lambda}$, $Z | U_{\lambda} = 0$, hence $Z
| U_{\lambda}$ is locally principal. Conversely c) entails a): let indeed $Z$ be a `1`-codimensional cycle on $X$ such
that $Z | U_{\lambda}$ is locally principal; since $X$ is normal, $Z | U_{\lambda} = cyc(D_{\lambda})$, where
$D_{\lambda}$ is a divisor on $U_{\lambda}$ `(21.6.10, (i))`, and the hypothesis implies (by virtue of `(21.3.4)`) that
there is a set $U_{\mu} \subset U_{\lambda}$ such that $D_{\mu} = D_{\lambda} | U_{\mu}$ is equivalent to `0`. If
$D_{\mu} = div(f_{\mu})$, where $f_{\mu}$ is a regular rational function on $U_{\mu}$, $f_{\mu}$ can be considered as a
regular rational function on $X$. If $Z' = cyc(div(f_{\mu}))$, one sees therefore that $Z'' = Z - Z'$ has its support in
$X - U_{\mu}$; by virtue of the hypothesis, `Z''` is locally principal, whence the conclusion.

The condition $\lim \operatorname{Pic}(U_{\lambda}) = 0$ will in particular be fulfilled if $(U_{\lambda})$ is the
family of open neighbourhoods of a point $z \in X$, for every invertible $\mathcal{O}_{U_{\lambda}}$-Module
$\mathcal{L}_{\lambda}$, there exists by definition a $U_{\mu} \subset U_{\lambda}$ such that $\mathcal{L}_{\lambda} |
U_{\mu}$ is isomorphic to $\mathcal{O}_{U_{\mu}}$. One sees therefore that, in the statement of `(21.13.15)`, if $S =
{z}$, conditions a) and b) are also equivalent to the following:

c) *Every `1`-codimensional cycle on $X$ whose support does not contain $z$ is locally principal.*

If moreover $\operatorname{Pic}(X) = 0$, one will conclude that this condition entails that every `1`-codimensional
cycle whose support does not contain $z$ is *principal*.

### 21.14. The Ramanujam-Samuel theorem

**Theorem (21.14.1)** (Ramanujam-Samuel).

<!-- label: IV.21.14.1 -->

*Let $A$ be a Noetherian local ring of maximal ideal $\mathfrak{m}$, such that its completion `Â` is integral and
integrally closed. Let $B$ be a Noetherian local ring such that $\dim(B) > \dim(A)$, $\rho : A \to B$ a local
homomorphism making $B$ a formally smooth $A$-algebra (for the preadic topologies `(0, 19.3.1)`) and such that the
residue field of $B$ is finite over that of $A$. Then every `1`-codimensional cycle on $\operatorname{Spec}(B)$ which is
principal at the point $p = \mathfrak{m}B$ is a principal `1`-codimensional cycle.*

If $k = A/\mathfrak{m}$ is the residue field of $A$, $B/\mathfrak{m}B$ is a formally smooth $k$-algebra (for

<!-- original page 324 -->

its preadic topology) `(0, 19.3.5)`, hence regular, and in particular integral; in other words $p = \mathfrak{m}B$ is
indeed a prime ideal of $B$, which justifies the statement. Everything evidently reduces to proving that every prime
ideal $q$ of $B$ not contained in $p$ is principal.

Let `Â`, $\hat{B}$ be the completions of $A$ and $B$ respectively, so that the maximal ideal of `Â` is
$\mathfrak{m}\hat{A}$; one knows `(0, 19.3.6)` that $\hat{B}$ is a formally smooth `Â`-algebra for the adic topologies.
Let $k'$ be the residue field of $B$, a finite extension of $k$; there exists a local homomorphism $\hat{A} \to C$,
where $C$ is a Noetherian local ring which is a finite and flat (hence free) `Â`-module and is such that
$C/\mathfrak{m}C$ is isomorphic to $k'$ $(0_{III}, 10.3.1)$; one deduces that $C$ is complete, and it then follows from
`(7.5.1)`, `(7.5.3)` and `(6.5.4, (ii))` that $C$ is integral and integrally closed. Moreover, $D = \hat{B}
\otimes_{\hat{A}} C$ is a complete semi-local ring, direct composite of complete local rings one of which, `D_0`, has
residue field $k'$ (since $k' \otimes_{k} k'$ is direct composite of local rings one of which is isomorphic to $k'$).
Since $D$ is formally smooth over $C$, the same is true of `D_0`; consequently $D_{0}/\mathfrak{m}D_{0}$ is a formally
smooth $k'$-algebra, of residue field $k'$, which entails that it is $k'$-isomorphic to a formal series algebra
$k'[[T_{1}, \cdots, T_{n}]]$ `(0, 19.6.4)`; one concludes, by `(0, 19.7.1.5)`, that `D_0` is $C$-isomorphic to
$C[[T_{1}, \cdots, T_{n}]]$, and consequently integral and integrally closed (Bourbaki, _Alg. comm._, chap. V, §1, n° 4,
prop. 14). Since the morphisms $\operatorname{Spec}(D_{0}) \to \operatorname{Spec}(\hat{B})$ and
$\operatorname{Spec}(D_{0}) \to \operatorname{Spec}(B)$ are faithfully flat, one deduces that $\hat{B}$ and $B$ are also
integral and integrally closed `(2.1.13)`. This proves that the ideal $qD_{0}$ is divisorial (Bourbaki, _Alg. comm._,
chap. VII, §1, n° 10, prop. 15) and not contained in $\mathfrak{m}D_{0}$, otherwise one would have $q = (qD_{0}) \cap B
\subset (\mathfrak{m}D_{0}) \cap B = \mathfrak{m}B = p$ by faithful flatness $(0_{I}, 6.5.1)$. One concludes that none
of the prime ideals $r_{i}$ of height `1` in `D_0` which contain $qD_{0}$ can be contained in $\mathfrak{m}D_{0}$; if
one proves that these ideals are principal, it will follow that $qD_{0}$ is principal, the divisors (in Bourbaki's
sense) of $qD_{0}$ and of a product of powers of the $r_{i}$ being equal (Bourbaki, _Alg. comm._, chap. VII, §1, n° 4,
prop. 5). Since $qD_{0} \cap B = q$, one deduces by faithful flatness that $q$ is principal `(2.5.2)`, using the fact
that $B$ is a local ring.

One is thus reduced to proving the theorem in the particular case where $A$ is complete and $B = A[[T_{1}, \cdots,
T_{n}]]$. Let us first show that one can reduce to the case where $n = 1$. Indeed, proceed by recurrence on $n$, and let
$f \in q$ be an element not belonging to $p = \mathfrak{m}B$; it will suffice to show that there exists an
$A$-automorphism $\sigma$ of $B$ such that $\sigma(f)$ does not belong to the ideal $p' = p + BT_{1} + \cdots +
BT_{n-1}$: indeed, if $B' = A[[T_{1}, \cdots, T_{n-1}]]$, $B'$ is complete and has maximal ideal $\mathfrak{m}B' +
B'T_{1} + \cdots + B'T_{n-1} = \mathfrak{m}'$. Since one has $B = B'[[T_{n}]]$ and $p' = \mathfrak{m}'B$, it will follow
from the recurrence hypothesis (taking into account that $B'$ is integral and integrally closed) that the ideal
$\sigma(q)$ is principal in $B$, hence so is $q$. Now, if $\bar{f} \in k[[T_{1}, \cdots, T_{n}]]$ is the image of $f$
("reduced series" of $f$), one knows (Bourbaki, _Alg. comm._, chap. VII, §3, n° 7, lemma 3) that there is an
$A$-automorphism $\sigma$ of $B$ such that $(\sigma(\bar{f}))(0, \cdots, 0, T_{n}) \neq 0$, which evidently implies
$\sigma(f) \notin p'$.

Suppose then $n = 1$ and write $T$ in place of `T_1`, so that $B = A[[T]]$. It suffices to show that in the polynomial
ring `A[T]`, the ideal $q \cap A[T]$ is principal;

<!-- original page 325 -->

in fact, let $f$ be an element of $q$ not belonging to $\mathfrak{m}B$; it is a formal series whose reduced series
$\bar{f}_{0}$ is not zero; hence, by virtue of the preparation theorem (Bourbaki, _Alg. comm._, chap. VII, §3, n° 8,
prop. 5), for every $f \in q$, there exist $g \in B$ and a polynomial $r \in A[T]$ such that $f = gf + r$, and one has
therefore $r \in q \cap A[T]$; on the other hand (loc. cit., prop. 6) there exist a non-constant distinguished
polynomial $F_{0} \in A[T]$ and an invertible element $u \in B$ such that $f_{0} = uF_{0}$, hence one also has $F_{0}
\in q \cap A[T]$, which proves that $q$ is generated by $q \cap A[T] = q_{1}$. Since $B$ is flat over `A[T]` $(0_{I},
7.3.3)$, it follows from Bourbaki, _Alg. comm._, chap. VII, §1, n° 10, prop. 15, that $q_{1}$ is a prime ideal of height
`1` in `A[T]`. Moreover, one has necessarily $q_{1} \cap A = 0$; otherwise, $q_{1} \cap A$ would necessarily be of
height `> 1`, and it would follow from `(5.5.3)` that one would have $q_{1} = (q_{1} \cap A)A[T]$. But then, since
$q_{1} \cap A \subset \mathfrak{m}$, one would have $q_{1} \subset \mathfrak{m}A[T]$ contrary to the hypothesis on $q$.
If $K$ is the field of fractions of $A$, $q_{1}K[T]$ is therefore a prime ideal distinct from `0` and from `K[T]` in
`K[T]`, hence of the form $h\cdot K[T]$, where $h(T) = T^{m} + a_{1} T^{m-1} + \cdots + a_{m}$ with $m \geqslant 1$ and
the $a_{i} \in K$, $h$ being irreducible in `K[T]`. But one has seen above that there exists in $q_{1}$ a non-constant
distinguished polynomial $F_{0} \in A[T]$. If $t$ is the class of $T$ in $K[T]/q_{1}K[T]$, $t$ is therefore a root of
the polynomial `F_0` in an extension of $K$ and consequently $h$ divides `F_0` in `K[T]`; but since $h$ and `F_0` are
monic, this entails that the coefficients $a_{i}$ of $h$ are integral over $A$ (Bourbaki, _Alg. comm._, chap. V, §1, n°
3, prop. 11), hence belong to $A$ since $A$ is integrally closed. In other words, one has $h \in A[T] \cap q_{1} K[T] =
q_{1}$ (Bourbaki, _Alg. comm._, chap. II, §1, n° 5, prop. 11); since every polynomial $g \in q_{1}$ is divisible by $h$
in `K[T]` and $h$ is monic, the coefficients of $g/h$ belong to $A$, hence $q_{1} = h\cdot A[T]$. **Q.E.D.**

The statement `(21.14.1)` is equivalent to the following:

**Corollary (21.14.2).**

<!-- label: IV.21.14.2 -->

*Under the hypotheses of `(21.14.1)` on $A$, $B$ and $p$, for every prime ideal $q$ of $B$ not contained in $p =
\mathfrak{m}B$ and such that $\dim(B_{q}) \geqslant 2$, the ring $B_{q}$ is parafactorial. In particular, if $\dim(B
\otimes_{A} k) > 0$ (i.e. $\dim B > \dim A$ (`(0, 19.7.1)` and `(6.1.1)`)), the ring $B$ is parafactorial.*

Indeed, one has seen in the proof of `(21.14.1)` that the conditions of the statement entail that $B$ is integral and
integrally closed; the equivalence of the statements `(21.14.1)` and `(21.14.2)` then results from `(21.13.15)` applied
to $X = \operatorname{Spec}(B)$ and $S = {p}$.

**Proposition (21.14.3).**

<!-- label: IV.21.14.3 -->

*Let $S$ be a normal prescheme, $f : X \to S$ a smooth morphism.*

*(i) If $S$ is locally Noetherian (hence also $X$), then, for every $x \in X$ such that $\dim(\mathcal{O}_{X,x})
\geqslant 2$ and such that $x$ is not a maximal point of its fibre $f^{-1}(f(x))$, the ring $\mathcal{O}_{X,x}$ is
parafactorial. Every `1`-codimensional cycle $Z$ on $X$ such that $Supp(Z)$ contains no irreducible component of a fibre
$f^{-1}(s) = X_{s}$, is locally principal.*

*(ii) Let $Y$ be a closed part of $X$ containing no irreducible component of a fibre $X_{s}$, and such that for every
maximal point $\eta$ of $S$, $Y_{\eta} = Y \cap X_{\eta}$ is of codimension $\geqslant 2$ in $X_{\eta}$. Then the couple
$(X, Y)$ is parafactorial.*

Note that the conditions of (ii) are fulfilled if $Y$ is a closed part of $X$ such that, for every $s \in S$, $Y_{s} = Y
\cap X_{s}$ is of codimension $\geqslant 2$ in $X_{s}$.

To prove `(21.14.3)`, note first that under the hypotheses of (i), if one

<!-- original page 326 -->

sets $Y = {\bar{x}}$, there exists an open neighbourhood $V$ of $x$ in $X$ such that $Y \cap V$ and $V$ verify the
conditions of (ii): indeed, it follows from the hypothesis and from `(9.5.3)` that one can take $V$ such that $V \cap Y$
contains no irreducible component of an $X_{s}$; on the other hand, for every maximal point $\eta$ of $S$ such that $Y
\cap X_{\eta} \neq \emptyset$, the points of $Y \cap X_{\eta}$ are specializations of $x$, hence at such a point $z$ one
has $\dim(\mathcal{O}_{X,z}) \geqslant 2$ and since $\mathcal{O}_{X_{\eta}, z} = \mathcal{O}_{X, z}$ ($S$ being reduced
to the point $\eta$ by virtue of `(2.1.13)`), $Y \cap X_{\eta}$ is indeed of codimension $\geqslant 2$ in $X_{\eta}$.
Since the couple $(V, Y \cap V)$ is then parafactorial by virtue of (ii), one concludes from `(21.13.10)` that the ring
$\mathcal{O}_{X,x}$ is parafactorial, that is to say the first assertion of (i). To prove the second, one can restrict
to the case where $Z = {\bar{\xi}}$, where $\xi \in X_{\eta}$; since $\mathcal{O}_{X,\xi}$ is an integrally closed local
ring of dimension `1`, it is a discrete valuation ring and $Z$ is therefore principal at the point $\xi$; for every
other point $x$ of $Supp(Z)$, one therefore has $\dim(\mathcal{O}_{X,x}) \geqslant 2$ and $x$ is not a maximal point of
its fibre by hypothesis, hence $\mathcal{O}_{X,x}$ is parafactorial. Apply then `(21.13.15)` taking for $S$ the set
formed by $\xi$ and the maximal points of the fibres of $f$; it is clear that $Z$ is principal at the points of $S$
since $\xi$ is the only point of $S$ belonging to $Supp(Z)$; since on the other hand condition b) of `(21.13.15)` is
evidently fulfilled, one concludes that $Z$ is locally principal.

One is therefore reduced to proving (ii). Set $U = X - Y$ and let $j : U \to X$ be the canonical injection.

Since the hypotheses and the conclusion are local on $S$ and on $X$ by virtue of `(21.13.6, (i))`, one can restrict to
the case where $S$ and $X$ are affine, $f$ being therefore of finite presentation. Since the fibres of $f$ are regular,
the hypothesis on $Y$ entails that, for every

<!-- original page 327 -->

point $x \in Y$, one has $prof(\mathcal{O}_{X_{f(x)}, x}) = \dim(\mathcal{O}_{X_{f(x)}, x}) \geqslant 1$; it follows
from `(19.9.8)` that the canonical homomorphism $\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is *injective*. Moreover,
replacing $Y$ by a larger closed part following the method of the proof of `(19.9.8)`, and using `(21.13.6, (ii))`, one
can suppose that $Y$ is defined by an ideal of finite type of the ring of $X$, hence the open $U = X - Y$ is
quasi-compact and quasi-separated and the closed set $Y$ is constructible.

To prove (ii), it suffices, for every invertible $\mathcal{O}_{U}$-Module $\mathcal{L}$ and every point $x \in Y$ given,
to establish the existence of an open neighbourhood $V$ of $x$ in $X$ such that: 1° the canonical homomorphism
$\mathcal{O}_{V} \to (j_{V})_{*}(\mathcal{L} | (U \cap V))$ is surjective; 2° there exists an invertible
$\mathcal{O}_{V}$-Module $\mathcal{L}_{V}$ such that $\mathcal{L}_{V} | (U \cap V) = \mathcal{L} | (U \cap V)$
(`(21.13.5)` and `(21.13.3)`).

Set $s = f(x)$; we shall see that one can restrict to the case where $S = S_{0} =
\operatorname{Spec}(\mathcal{O}_{S,s})$. Let $(S_{\nu})$ be a fundamental system of affine open neighbourhoods of $s$ in
$S$, and set $X_{\nu} = f^{-1}(S_{\nu})$, $Y_{\nu} = Y \cap X_{\nu}$, $U_{\nu} = X_{\nu} - Y_{\nu}$, $j_{\nu} : U_{\nu}
\to X_{\nu}$ being the canonical injection; $X_{0} = X \times_{S} S_{0}$ is then projective limit of the $X_{\nu}$,
`(8.1.2, a))`; suppose the proposition true for the morphism $f_{0} : X_{0} \to S_{0}$ and for $Y_{0} = Y \cap X_{0}$,
and set $U_{0} = X_{0} - Y_{0}$, $j_{0} : U_{0} \to X_{0}$ being the canonical injection. The projection $p_{\nu} :
X_{0} \to X_{\nu}$ being an affine morphism, one has $(j_{0})_{*}(\mathcal{L} | U_{0}) =
p^{*}_{\nu}((j_{\nu})_{*}(\mathcal{L} | U_{\nu}))$ `(II, 1.5.2)` and the canonical homomorphism $\rho_{0} :
\mathcal{O}_{X_{0}} \to (j_{0})_{*}(\mathcal{L} | U_{0})$ is none other than $p^{*}_{\nu}(\rho_{\nu})$, where
$\rho_{\nu} : \mathcal{O}_{X_{\nu}} \to (j_{\nu})_{*}(\mathcal{L} | U_{\nu})$ is the canonical homomorphism; since by
hypothesis $\rho_{0}$ is surjective, the same is true of $\rho_{\nu}$ for $\nu$ large enough `(8.5.7)`. Let on the other
hand $\mathcal{L}_{0}$ be the invertible $\mathcal{O}_{U_{0}}$-Module restriction of $\mathcal{L}$, and note that the
$X_{\nu}$ are affine, hence quasi-compact and quasi-separated; since by hypothesis there exists an invertible
$\mathcal{O}_{X_{0}}$-Module $\mathcal{L}'_{0}$ such that $\mathcal{L}_{0} | U_{0} = \mathcal{L}'_{0}$, there exists a
$\nu$ large enough and a quasi-coherent $\mathcal{O}_{X_{\nu}}$-Module $\mathcal{L}'_{\nu}$ of finite presentation such
that $\mathcal{L}'_{0}$ is isomorphic to $p^{*}_{\nu}(\mathcal{L}'_{\nu})$ `(8.5.2, (ii))`; moreover `(8.5.5)` one can
suppose that $\mathcal{L}'_{\nu}$ is invertible. Finally, since the $U_{\nu}$ are quasi-compact and quasi-separated and
$\mathcal{L}_{0} | U_{0} = \mathcal{L}'_{0}$, there exists $\nu$ large enough such that $\mathcal{L} | U_{\nu}$ and
$\mathcal{L}''_{\nu} = \mathcal{L}'_{\nu} | U_{\nu}$ are isomorphic `(8.5.2.5)`.

One is thus reduced to the case where $S = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, where $A$ is a *local*
ring; since $X$ is normal and $f$ smooth, $S$ is normal `(17.5.7)`, hence $A$ is integral and integrally closed.
Consider then $A$ as inductive limit of its sub-$\mathbb{Z}$-algebras of finite type; since the integral closure of such
a sub-$\mathbb{Z}$-algebra is a subring of $A$ and is also a $\mathbb{Z}$-algebra of finite type
`(7.8.3, (ii), (iii) and (vi))`, $A$ is filtered inductive limit of the sub-$\mathbb{Z}$-algebras of finite type
$A_{\lambda}$ of $A$ which are integrally closed rings. By virtue of `(1.8.4.2)`, there exists an index $\lambda$ and an
$A_{\lambda}$-algebra of finite type $B_{\lambda}$ such that $B = B_{\lambda} \otimes_{A_{\lambda}} A$ up to an
$A$-isomorphism. Set $S_{\lambda} = \operatorname{Spec}(A_{\lambda})$, $X_{\lambda} = \operatorname{Spec}(B_{\lambda})$;
if $p_{\lambda} : X \to X_{\lambda}$ is the canonical projection, one can moreover suppose (since $Y$ is constructible)
that $Y = p^{-1}_{\lambda}(Y_{\lambda})$, where $Y_{\lambda}$ is a closed part of $X_{\lambda}$ `(8.3.11)`. Let
$f_{\lambda}$ be the morphism $X_{\lambda} \to S_{\lambda}$; by virtue of the transitivity of fibres and of `(4.2.6)`,
$Y_{\lambda}$ contains no irreducible component of the fibres $f^{-1}_{\lambda}(s_{\lambda})$ for any $s_{\lambda} \in
S_{\lambda}$. Since $f$ is smooth, one can also suppose that $f_{\lambda}$ is smooth `(17.7.8)`; finally, the image of
the generic point $\eta$ of $S$ in $S_{\lambda}$ is the generic point $\eta_{\lambda}$ of $S_{\lambda}$, and one has
$codim((Y_{\lambda})_{\eta_{\lambda}}, (X_{\lambda})_{\eta_{\lambda}}) = codim(Y_{\eta}, X_{\eta}) \geqslant 2$ by
virtue of `(6.1.4)`. One sees therefore that $S_{\lambda}$, $X_{\lambda}$ and $Y_{\lambda}$ verify all the hypotheses of
(ii), and on setting $X_{\mu} = X_{\lambda} \times_{S_{\lambda}} S_{\mu}$ for $\lambda \leqslant \mu$, the same is true
for $S_{\mu}$, $X_{\mu}$ and $Y_{\mu}$. Let us show that if one proves that the couple $(X_{\mu}, Y_{\mu})$ is
parafactorial for every $\mu \geqslant \lambda$, the same is true for $(X, Y)$. Indeed, let $U = X - Y$, $U_{\mu} =
X_{\mu} - Y_{\mu}$, $j : U \to X$, $j_{\mu} : U_{\mu} \to X_{\mu}$ the canonical injections; the projection $p_{\mu} : X
\to X_{\mu}$ being an affine morphism, one has $j_{*}(\mathcal{O}_{U}) =
p^{*}_{\mu}((j_{\mu})_{*}(\mathcal{O}_{U_{\mu}}))$ `(II, 1.5.2)`, and consequently the canonical homomorphism $\rho :
\mathcal{O}_{X} \to j_{*}(\mathcal{O}_{U})$ is none other than $p^{*}_{\mu}(\rho_{\mu})$, where $\rho_{\mu} :
\mathcal{O}_{X_{\mu}} \to (j_{\mu})_{*}(\mathcal{O}_{U_{\mu}})$ is the canonical homomorphism; the latter being
bijective by hypothesis, the same is true of $\rho$. On the other hand, for every invertible $\mathcal{O}_{U}$-Module
$\mathcal{L}$, there exists $\mu \geqslant \lambda$ and an invertible $\mathcal{O}_{U_{\mu}}$-Module
$\tilde{\mathcal{L}}$ such that $\mathcal{L} \simeq p^{*}_{\mu}(\tilde{\mathcal{L}})$ (denoting by $p_{\mu} : U \to
U_{\mu}$ the restriction of $p_{\mu}$) `(8.5.2 and 8.5.5)`, $U_{\mu}$ being quasi-compact since $X_{\mu}$ is Noetherian.
By hypothesis, there exists an invertible $\mathcal{O}_{X_{\mu}}$-Module $\mathcal{L}'_{\mu}$ such that
$\mathcal{L}'_{\mu} | U_{\mu}$ is isomorphic to $\tilde{\mathcal{L}}$; $\mathcal{L}' = p^{*}_{\mu}(\mathcal{L}'_{\mu})$
is then an invertible $\mathcal{O}_{X}$-Module such that $\mathcal{L}' | U$ is isomorphic to $\mathcal{L}$, which proves
our assertion.

One is thus reduced to proving (ii) when the ring $A$ is a $\mathbb{Z}$-algebra of finite type integrally closed; since
the local rings $\mathcal{O}_{S, y}$ of $S$ are then excellent integrally closed rings, their completions are also
integrally closed `(7.8.3, (ii), (iii) and (vii))`. To prove that the couple $(X, Y)$ is parafactorial, it suffices to
show that for every $x \in Y$, the ring $\mathcal{O}_{X,x}$ is parafactorial `(21.13.10)`. Let $y$ be a closed point of
$Y_{f(x)}$, which is a specialization of $x$ `(5.1.11)`; if one sets $s = f(x) = f(y)$, $\mathcal{O}_{S,s}$ has a

<!-- original page 328 -->

integrally closed completion, and $\mathcal{O}_{X,y}$ is a formally smooth $\mathcal{O}_{S,s}$-algebra for the preadic
topologies `(17.5.3)`; since $Y_{s}$ contains no irreducible component of $X_{s}$, one has $\dim(\mathcal{O}_{X,y}) >
\dim(\mathcal{O}_{S,s})$ `(17.5.8)`. If $x \neq \eta$, one has $\dim(\mathcal{O}_{X,x}) \geqslant 1$; if on the contrary
$y = \eta$, one has by hypothesis $\dim(\mathcal{O}_{X,\eta}) \geqslant 2$; hence in all cases $\dim(\mathcal{O}_{X,x})
\geqslant 2$. Moreover, the prime ideal of $\mathcal{O}_{X,y}$ corresponding to the point $x$ is not contained in
$\mathfrak{m}_{y} \mathcal{O}_{X,y}$ since $Y$ contains no irreducible component of $X_{s}$. Finally, since $y$ is
closed in $X_{s}$, $k(y)$ is a finite extension of $k(s)$ `(I, 6.4.2)`. In all cases, one can apply to $A =
\mathcal{O}_{S,s}$, $B = \mathcal{O}_{X,y}$ and $q = \mathfrak{m}_{x} \mathcal{O}_{X,y}$ the result of `(21.14.2)`,
which completes the proof.

**Remarks (21.14.4).**

<!-- label: IV.21.14.4 -->

(i) It may be that the statements `(21.14.1)` and `(21.14.2)` remain valid without hypothesis on the residue field of
$B$. Stated with this generality, the result would be equivalent, by virtue of `(21.13.15)` and `(21.13.12.1)`, to the
following: *Let $A$ be a Noetherian local ring complete, integral and integrally closed, $B$ a Noetherian local ring
which is a formally smooth $A$-algebra, such that $\dim(B) > \dim(A)$; then $B$ is parafactorial.*

(ii) We shall see in chap. VI, by using a "finite descent" technique applied to the morphism $Y' \to Y =
\operatorname{Spec}(A)$, where $Y'$ is the normalization of $Y$, that the conclusion of `(21.14.1)` (or of `(21.14.2)`)
remains valid on replacing the hypothesis that `Â` is integrally closed by the hypothesis that `Â` is reduced provided
that $\dim B \geqslant \dim A + 2$. If one replaces this last condition by $\dim B \geqslant \dim A + 3$, one can even
suppress the hypothesis that `Â` is reduced. Similarly, the conclusion of `(21.14.3)` remains valid on replacing the
hypothesis that $X$ is normal by the hypothesis that $X$ is reduced, provided that $\dim(\mathcal{O}_{X,x}) \geqslant
\dim(\mathcal{O}_{S,s}) + 2$.

(iii) In chap. III, 3rd part, one proves that if $f : X \to S$ is a smooth morphism, $Y$ a locally constructible closed
part of $X$ such that, for every $s \in S$, one has (with the notations of `(21.14.3)`) $codim(Y_{s}, X_{s}) \geqslant
3$, then the couple $(X, Y)$ is parafactorial (`[41]`, XII, 4.8). This conclusion is no longer valid when one supposes
only that $codim(Y_{s}, X_{s}) \geqslant 2$ for every $s \in S$ and when one no longer supposes $X$ reduced. For
example, let $k$ be a field, $A = k[T]/(T^{2})$, algebra of dual numbers over $k$, $S = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(A[T_{1}, T_{2}])$ ($T_{1}, T_{2}$ indeterminates), so that $X = \mathbb{V}^{2}_{S}$, $Y$ being the
"zero section" of this bundle; if $s$ is the unique closed point of $S$, one has $X_{s} = \mathbb{V}^{2}_{k}$ and
$Y_{s}$ is the "zero section" of $X_{s}$. To see that the couple $(X, Y)$ is not parafactorial, it suffices to show that
the ring $B = A[T_{1}, T_{2}]_{\mathfrak{m}}$, where $\mathfrak{m}$ is the ideal $(T_{1}) + (T_{2})$ which defines $Y$,
is not parafactorial `(21.13.10)`. Let $B_{0} = B_{red}$, and denote $U$ and `U_0` the complements of the closed point
in $\operatorname{Spec}(B)$ and $\operatorname{Spec}(B_{0})$; arguing as in `(21.13.9)`, one has the exact sequence,
extension of `(21.13.9.1)`

```text
                       Γ(U, 𝒪_U^×) → Γ(U_0, 𝒪_{U_0}^×) → H^1(U_0, 𝒪_{U_0}) → Pic(U) → Pic(U_0).
```

Now, one has $\Gamma(U, \mathcal{O}_{U}) = B$, $\Gamma(U_{0}, \mathcal{O}_{U_{0}}) = B_{0}$ since $prof(B) = prof(B_{0})
= 2$ `(5.10.5)`. Moreover $\operatorname{Pic}(U_{0}) = 0$ since `B_0` is factorial, and $H^{1}(U_{0},
\mathcal{O}_{U_{0}}) \neq 0$ `[41, 3, Example III-1]`; since the homomorphism $B^{\times} \to B^{\times}_{0}$ is
surjective, one concludes that $\operatorname{Pic}(U) \neq 0$, hence that $B$ is not parafactorial.

<!-- original page 329 -->

(iv) The result `(21.14.3)` was first proved by C. Seshadri `[44]` in the particular case where $S$ is a normal
algebraic scheme over an algebraically closed field $k$ and $X = S \times_{k} T$, where $T$ is a $k$-prescheme algebraic
and smooth over $k$. Seshadri's proof `[44, p. 188-189]` is global in nature and uses the theory of Picard schemes. It
gives moreover (loc. cit.) results such as the following (for which one does not at present possess a proof by local
means). Let $S$, $T$ be two preschemes locally of finite type over a field $k$, $X = S \times_{k} T$, $Z$ a
`1`-codimensional cycle on $X$ (considered as $S$-prescheme); suppose the following conditions are verified:

1° $S$ and $T$ are geometrically normal over $k$ `(6.7.6)`;

2° For every maximal point $\eta$ of $S$, the `1`-codimensional cycle $Z_{\eta}$ on the fibre $X_{\eta}$, having the
same multiplicity as $Z$ at every point of $X_{\eta} \cap X_{(s_{\eta})}$, is locally principal (in other words, is the
image of a divisor of $X_{\eta}$, since $X_{\eta}$ is normal);

3° For every $s \in S$, $Z$ is principal at the maximal points of the fibre $X_{s}$.

Then $Z$ is locally principal. In other words, $X$ being normal `(6.14.1)`, for every $x \in X$ which is not maximal in
its fibre $X_{s}$ and which belongs to none of the "generic fibres" $X_{\eta}$ (which implies $\dim(\mathcal{O}_{X,x})
\geqslant 2$ by virtue of `(6.1.1)`), the local ring $\mathcal{O}_{X,x}$ is parafactorial, by virtue of
`(21.12.15)`.[^21.14.4-seshadri]

### 21.15. Relative divisors

**(21.15.1).** Let $S$ be a prescheme, $f : X \to S$ a flat morphism locally of finite presentation. One has defined in
`(20.6.1)` the sheaf of rings $\mathcal{M}_{X/S}$ of germs of meromorphic functions on $X$ relative to $S$, a subsheaf
of $\mathcal{M}_{X}$; it is clear that the canonical injection $\mathcal{O}_{X} \to \mathcal{M}_{X}$ `(20.1.4.1)` sends
$\mathcal{O}_{X}$ onto a subsheaf of $\mathcal{M}_{X/S}$, with which one identifies it. Let $\mathcal{M}^{\times}_{X/S}$
be the sheaf (in multiplicative groups) of germs of invertible sections of $\mathcal{M}_{X/S}$; it is therefore a
subsheaf of $\mathcal{M}^{\times}_{X}$ and contains $\mathcal{O}^{\times}_{X}$ as a subsheaf.

**Definition (21.15.2).**

<!-- label: IV.21.15.2 -->

*One calls **sheaf of divisors on $X$ relative to $S$**, or **sheaf of divisors on $X$ transversal to $f$**, and one
denotes $\mathcal{D}iv_{X/S}$ the quotient sheaf (of commutative groups) $\mathcal{M}^{\times}_{X/S} /
\mathcal{O}^{\times}_{X}$; the sections of this sheaf over $X$ are called **divisors on $X$ relative to $S$**, or
**divisors on $X$ transversal to $f$**; they form a commutative group denoted $\operatorname{Div}(X/S)$.*

It is clear that $\mathcal{D}iv_{X/S}$ identifies canonically with a subsheaf of $\mathcal{D}iv_{X}$, and consequently
$\operatorname{Div}(X/S)$ with a subgroup of $\operatorname{Div}(X)$, which one again denotes additively.

<!-- original page 330 -->

For every open $U$ of $X$, one has $\mathcal{M}_{X/S} | U = \mathcal{M}_{U/S}$, hence $\mathcal{D}iv_{X/S} | U =
\mathcal{D}iv_{U/S}$, and the sheaf $\mathcal{D}iv_{X/S}$ is therefore equal to the presheaf $U \mapsto
\operatorname{Div}(U/S)$.

Since $\mathcal{M}^{\times}_{X/S}$ is a subsheaf of $\mathcal{M}^{\times}_{X}$, the definitions, notations and formulas
relating to the divisors of sections of $\mathcal{M}_{X}$ over $X$ `(21.1.3)` apply without change to the sections of
$\mathcal{M}_{X/S}$ over $X$.

**(21.15.3).** The structure of sheaf of ordered groups on $\mathcal{D}iv_{X}$ `(21.1.6)` induces on the subsheaf
$\mathcal{D}iv_{X/S}$ a structure of sheaf of ordered groups, for which the sheaf of monoids of germs of positive
sections is $\mathcal{D}iv^{+}_{X} \cap \mathcal{D}iv_{X/S}$, which one denotes $\mathcal{D}iv^{+}_{X/S}$. One has
$\Gamma(X, \mathcal{D}iv^{+}_{X/S}) = \operatorname{Div}^{+}(X) \cap \operatorname{Div}(X/S)$; one denotes this
submonoid of $\operatorname{Div}(X/S)$ by $\operatorname{Div}^{+}(X/S)$, and it is formed of elements $\geqslant 0$ for
a structure of ordered group on $\operatorname{Div}(X/S)$. It follows from `(21.1.5.1)` that $\mathcal{D}iv^{+}_{X/S}$
is the image in $\mathcal{M}^{\times}_{X/S}$ of the subsheaf of monoids

<!-- label: IV.21.15.3.1 -->

$$ (21.15.3.1) \mathcal{O}^{+,\star}_{X} = \mathcal{O}^{\star}_{X} \cap \mathcal{M}^{\times}_{X/S}. $$

For every open $U$ of $X$, $\Gamma(U, \mathcal{O}^{+,\star}_{X})$ is the set of sections $t$ of $\mathcal{O}_{X}$ over
$U$ such that $t$ be regular and that $1/t$ belong to $\Gamma(U, \mathcal{M}_{X/S})$, which means, with the notations of
`(20.6.1)`, that $t \in \mathcal{S}_{X/S}(U)$, so that the sheaf $\mathcal{O}^{+,\star}_{X}$ is none other than the
sheaf denoted $\mathcal{S}_{X/S}$ in `(20.6.1)`. One can therefore write

<!-- label: IV.21.15.3.2 -->

$$ (21.15.3.2) \mathcal{D}iv^{+}_{X/S} = \mathcal{S}_{X/S} \ \mathcal{O}^{\times}_{X} $$

up to a canonical isomorphism.

**(21.15.3.3).** Let $D \in \operatorname{Div}^{+}(X/S)$ and consider the closed sub-prescheme $Y(D)$ of $X$ defined by
the Ideal $\mathcal{J}_{X}(D)$ of $\mathcal{O}_{X}$ `(21.2.12)`; by virtue of what precedes, for every $x \in Y(D)$,
there is an open neighbourhood $U$ of $x$ in $X$ and a section $t \in \Gamma(\mathcal{S}_{X/S}(U))$ such that
$\mathcal{J}_{X}(D) | U = (\mathcal{O}_{X} | U) \cdot t$; since $x \in Y(D)$, the image $t_{x}$ of $t$ in $\Gamma(U \cap
X_{f(x)}, \mathcal{O}_{X_{f(x)}})$ belongs to the maximal ideal of $\mathcal{O}_{X_{f(x)}, x}$, and moreover, by
definition, for every $s \in S$, the image $t_{s}$ of $t$ in $\Gamma(U \cap X_{s}, \mathcal{O}_{X_{s}})$ is a regular
section. One deduces therefore from `(11.3.8)` and `(19.2.4)` that the canonical immersion $Y(D) \to X$ is
*transversally regular* relative to $S$ and of codimension `1` at the point $x$. The converse being immediate, one sees
that one can identify canonically the positive divisors on $X$ relative to $S$ with the closed sub-preschemes $Y$ of $X$
such that the canonical injection $Y \to X$ be a transversally regular immersion relative to $S$ and of codimension `1`.
We shall ordinarily make this identification.

**Proposition (21.15.4).**

<!-- label: IV.21.15.4 -->

*Let $D$ be a divisor on $X$, $\mathcal{O}_{X}(D)$ the corresponding invertible fractional Ideal `(21.2.5)`. For $D \in
\operatorname{Div}(X/S)$, it is necessary and sufficient that, for every $x \in X$, one have $(\mathcal{O}_{X}(D)
\otimes_{\mathcal{O}_{X}} \mathcal{M}_{X/S})_{x} = \mathcal{M}_{X/S, x}$ (or what amounts to the same, that one have
$\mathcal{O}_{X}(D) \otimes_{\mathcal{O}_{X}} \mathcal{M}_{X/S} = \mathcal{M}_{X/S}(\mathcal{O}_{X}(D))$).*

Indeed, to say that $D \in \operatorname{Div}(X/S)$ means that for every $x \in X$, there exists an open neighbourhood
$U$ of $x$ and a section $f \in \Gamma(U, \mathcal{M}_{X/S})$ such that $D | U = div_{U}(f)$; since $\mathcal{O}_{X}(D)
| U$ is the invertible fractional Ideal $\mathcal{O}_{U} f$, the proposition follows at once.

<!-- original page 331 -->

**Proposition (21.15.5).**

<!-- label: IV.21.15.5 -->

*Let $D$ be a divisor on $X$, $\mathcal{O}_{X}(D)$ the invertible fractional Ideal and $s_{D}$ the regular meromorphic
section of $\mathcal{O}_{X}(D)$ defined canonically by $D$ `(21.2.8 and 21.2.9)`. For $D \in \operatorname{Div}(X/S)$,
it is necessary and sufficient that $s_{D} \in \Gamma(X, \mathcal{M}_{X/S}(\mathcal{O}_{X}(D)))$.*

Indeed, if $U$ is an open of $X$ such that $D | U = div_{U}(f)$, where $f \in \Gamma(U, \mathcal{M}_{X})$, to say that
$s_{D} \in \Gamma(U, \mathcal{M}_{X/S}(\mathcal{O}_{X}(D)))$ means, by virtue of definitions `(20.6.2)`, that $f^{-1}
\in \Gamma(U, \mathcal{M}_{X/S})$, whence the proposition.

The interpretation of divisors on $X$ by means of the classes $cl(\mathcal{L}, s)$ `(21.2.11)` therefore permits the
interpretation of the elements of $\operatorname{Div}(X/S)$ as the couples (up to isomorphism) $(\mathcal{L}, s)$ such
that $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module and that $s$ be a meromorphic section of $\mathcal{L}$ over
$X$, regular relative to $S$ `(20.6.5, (iii))`.

**Proposition (21.15.6).**

<!-- label: IV.21.15.6 -->

*Let $D$ be a divisor on $X$ relative to $S$, and suppose that for every $x \in X$ such that
$prof(\mathcal{O}_{X_{f(x)}, x}) = 1$, one has $D_{x} \geqslant 0$ (resp. $D_{x} = 0$). Then one has $D \geqslant 0$
(resp. $D = 0$).*

As in `(21.1.8)`, one can restrict to the case where $D = div(\phi)$, where $\phi$ is a regular meromorphic function
relative to $S$, and everything reduces to seeing that if $D_{x} \geqslant 0$ at every point $x \in X$ such that
$prof(\mathcal{O}_{X_{f(x)}, x}) = 1$, $\phi$ is everywhere defined in $X$. But this hypothesis means that, if $T = X -
dom(\phi)$, one has $prof(\mathcal{O}_{X_{f(x)}, x}) \geqslant 2$ for every $x \in T$, and it suffices, to conclude, to
apply `(20.6.6)`.

**(21.15.7).** Let $X'$ be a second $S$-prescheme flat and locally of finite presentation over $S$, and let $g : X' \to
X$ be an $S$-morphism. If the $S$-morphism $g$ is flat, one knows `(21.4.5)` that the inverse image by $g$ of every
divisor on $X$ is defined; if moreover $D \in \operatorname{Div}(X/S)$, it follows from definition `(21.15.2)` and from
`(20.6.8)` that one has then $g^{*}(D) \in \operatorname{Div}(X'/S)$.

**(21.15.8).** Let $X'$ be a second $S$-prescheme flat and locally of finite presentation over $S$, and let $g : X' \to
X$ be a finite and flat $S$-morphism. Note that $g$ is then necessarily of finite presentation
`(1.4.3, 1.4.6 and 1.6.3)`, hence $g_{*}(\mathcal{O}_{X'})$ is a flat and finite-presentation $\mathcal{O}_{X}$-Module,
and consequently locally free `(2.1.12)`; in other words $g$ is a *locally free morphism* `(18.2.7)`; for every $s \in
S$, the corresponding morphism $g_{s} : X'_{s} \to X_{s}$ is therefore also finite and locally free. One deduces then
from `(21.5.2)` and `(20.6.1)` that for every open $U$ of $X$ and every section $f \in \Gamma(g^{-1}(U),
\mathcal{M}_{X'/S})$, the norm $N_{X'/X}(f)$ belongs to $\Gamma(U, \mathcal{M}_{X/S})$; the reasoning of `(21.5.3)` then
proves that for every invertible $\mathcal{O}_{X'}$-Module $\mathcal{L}'$ and every meromorphic section $u'$ of
$\mathcal{L}'$ over $X'$, regular relative to $S$, the norm $N_{X'/X}(u')$ is a meromorphic section of
$\mathcal{O}^{N_{X'/X}(\mathcal{L}')}_{X}$ over $X$, regular relative to $S$. The interpretation of divisors relative to
$S$ given in `(21.15.5)` and the definition of the direct image of a divisor `(21.5.5)` then prove that for every
divisor $D' \in \operatorname{Div}(X'/S)$, one has $g_{*}(D') \in \operatorname{Div}(X/S)$.

**(21.15.9).** Consider finally any morphism $S' \to S$, and (under the hypotheses of `(21.15.1)`) set $X' = X
\times_{S} S'$, which is flat and locally of finite presentation over $S'$; if $p : X' \to X$ is the canonical
projection, one has seen `(20.6.9)` that one has a canonical homomorphism $p^{*}(\mathcal{M}_{X/S}) \to
\mathcal{M}_{X'/S'}$, which evidently transforms every section of $\mathcal{M}_{X/S}$ over an open $U$, regular relative
to $S$, into a section of $\mathcal{M}_{X'/S'}$ over $p^{-1}(U)$, regular relative to $S'$ `(20.6.5, (iii))`; one then
concludes from the definition

<!-- original page 332 -->

`(21.15.2)` and from the right-exactness of the functor $p^{*}$, that the foregoing homomorphism defines by passage to
quotients a canonical homomorphism

<!-- label: IV.21.15.9.1 -->

$$ (21.15.9.1) \operatorname{Div}(X/S) \to \operatorname{Div}(X'/S') $$

which evidently transforms the elements of $\operatorname{Div}^{+}(X/S)$ into elements of
$\operatorname{Div}^{+}(X'/S')$. One sets again $\operatorname{Div}(X'/S') = \operatorname{Div}_{X/S}(S')$ (resp.
$\operatorname{Div}^{+}(X'/S') = \operatorname{Div}^{+}_{X/S}(S')$), and one sees at once that one has thus defined two
contravariant functors

```text
                       𝒟iv_{X/S} : Sch_{/S}^∘ → Ab,        𝒟iv_{X/S}^+ : Sch_{/S}^∘ → Set
```

from the category of $S$-preschemes into that of commutative groups (resp. of sets). One will see later (chap. VI)
important cases where the functor $\mathcal{D}iv_{X/S}$ is representable $(0_{III}, 8.1.8)$.

For every divisor $D \in \operatorname{Div}(X/S)$, the image of $D$ by the homomorphism `(21.15.9.1)` is none other than
the inverse image $p^{*}(D)$ (in the sense of `(21.4.2)`): the existence of this inverse image and the preceding
assertion are indeed immediate consequences of `(20.6.5, (iii))` and `(20.6.9)`.

The elements of $\operatorname{Div}(X'/S')$ are often called, by abuse of language, *"families of divisors on $X$
relative to $S$, parametrized by the $S$-prescheme $S'$"*; this terminology is used especially when one is dealing with
positive divisors.

[^1]: The reader will verify that `(21.9.12)` is not used to prove this property in chap. V.

[^21.14.4-seshadri]: In fact, in the article cited above, Seshadri supposes that $k$ is algebraically closed, $T$
    separated and "semi-complete" (i.e. such that $\Gamma(T, \mathcal{O}_{T})$ is $k$-isomorphic to $k$) and replaces
    hypothesis 3° by the stronger hypothesis that $Supp(Z)$ contains none of the fibres $X_{s}$ for $s \in S$. But since
    the statement is local on $S$, one concludes at once that it suffices to make hypothesis 3°, and this proves that
    the conclusion (interpreted as above in terms of the parafactoriality property of the rings $\mathcal{O}_{X,x}$) is
    local on $S$ and on $T$, which allows one to eliminate completely the hypothesis that $T$ is "semi-complete" and
    that $k$ is algebraically closed, since (by passing first to the algebraic closure of $k$) one can suppose first $T$
    affine, which allows one to embed it as an open of a projective normal scheme over $k$, to which Seshadri's result
    applies. Note also that, thanks to this reduction, it suffices to do Seshadri's proof in the case where $T$ is
    projective (and not only "semi-complete"), a case in which the Picard scheme theory used by Seshadri is contained in
    the theory which will be developed in chap. VI of our Treatise.
