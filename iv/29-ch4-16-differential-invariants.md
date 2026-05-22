<!-- original page 5 -->

## §16. Differential invariants. Differentially smooth morphisms

In this section we present, in global form, certain notions of differential calculus particularly useful in algebraic
geometry. We pass over many developments that are classical in differential geometry (connections, infinitesimal
transformations associated with a vector field, jets, etc.), although these notions are written in a particularly
natural way in the framework of schemes. We likewise pass over here the phenomena special to characteristic $p > 0$
(some of which are studied, in the affine setting, in `(0, 21)`). For certain complements to the differential formalism
in preschemes the reader may consult Exposés II and VII of `[42]`, as well as later chapters of this Treatise.

### 16.1. Normal invariants of an immersion

**(16.1.1).**

<!-- label: IV.16.1.1 -->

Let $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ be two ringed spaces, $f = (\psi, \theta) : Y \to X$ a morphism of
ringed spaces $(0_{I}, 4.1.1)$ such that the homomorphism

$$ \theta^{#} : \psi*(\mathcal{O}_{X}) \to \mathcal{O}_{Y} $$

is surjective, so that $\mathcal{O}_{Y}$ is identified with a quotient sheaf of rings
$\psi*(\mathcal{O}_{X})/\mathcal{I}_{f}$. One can then endow $\psi*(\mathcal{O}_{X})$ with the $\mathcal{I}_{f}$-preadic
filtration.

**Definition (16.1.2).**

<!-- label: IV.16.1.2 -->

*The $\mathcal{O}_{Y}$-augmented sheaf of rings $\psi*(\mathcal{O}_{X})/\mathcal{I}^{n+1}_{f}$ is called the **$n$-th
normal invariant of $f$**; the ringed space $(Y, \psi*(\mathcal{O}_{X})/\mathcal{I}^{n+1}_{f})$ is called the **$n$-th
infinitesimal neighbourhood of $Y$ for the morphism $f$**, and denoted $Y^{(n)}_{f}$ or simply $Y^{(n)}$. The sheaf of
graded rings associated with the sheaf of filtered rings $\psi*(\mathcal{O}_{X})$*

```text
  (16.1.2.1)    𝒢ℛ_•(f) = ⨁_{n ⩾ 0} (𝓘_f^n / 𝓘_f^{n+1})
```

*is called the **sheaf of graded rings associated with $f$**. The sheaf $\mathcal{GR}_{1}(f) = \mathcal{I}_{f} /
\mathcal{I}^{2}_{f}$ is called the **conormal sheaf** of $f$ (and is also denoted $\mathcal{N}_{Y/X}$ when no confusion
results).*

It is clear that the $\mathcal{O}_{Y^{(n)}} = \psi*(\mathcal{O}_{X})/\mathcal{I}^{n+1}_{f}$ (also denoted
$\mathcal{O}_{Y^{(n)}_{f}}$) form a

<!-- original page 6 -->

projective system of sheaves of rings on $Y$, the transition homomorphism $\phi_{nm} : \mathcal{O}_{Y^{(m)}} \to
\mathcal{O}_{Y^{(n)}}$ for $n \leqslant m$ identifying $\mathcal{O}_{Y^{(n)}}$ with the quotient of
$\mathcal{O}_{Y^{(m)}}$ by the power $(\mathcal{I}_{f} / \mathcal{I}^{m+1}_{f})^{n+1}$ of the augmentation ideal of
$\mathcal{O}_{Y^{(m)}}$, kernel of $\phi_{0n} : \mathcal{O}_{Y^{(n)}} \to \mathcal{O}_{Y}$. The $Y^{(n)}$ therefore form
an inductive system of ringed spaces, all having the space $Y$ as underlying space, and one has canonical morphisms of
ringed spaces $h_{n} : Y^{(n)} \to X$ equal to $(\psi, \theta_{n})$, where $\theta^{#}_{n}$ is the canonical morphism
$\psi*(\mathcal{O}_{X}) \to \psi*(\mathcal{O}_{X})/\mathcal{I}^{n+1}_{f}$. It is clear that the sheaf
$\mathcal{GR}_{\bullet}(f)$ is a sheaf of graded algebras over the sheaf of rings $\mathcal{O}_{Y} =
\mathcal{GR}_{0}(f)$, and the $\mathcal{GR}_{k}(f)$ are $\mathcal{O}_{Y}$-Modules.

As for any sheaf of filtered rings, one has a canonical surjective homomorphism of graded $\mathcal{O}_{Y}$-algebras

$$ (16.1.2.2) \mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{GR}_{1}(f)) \to \mathcal{GR}_{\bullet}(f) $$

coinciding in degrees `0` and `1` with the identity homomorphisms.

**Examples (16.1.3).**

<!-- label: IV.16.1.3 -->

*(i) Suppose that $X$ is a space ringed in local rings, that $Y$ is reduced to a single point $y$ (endowed with a ring
$\mathcal{O}_{y}$), and that, if $x = \psi(y)$, $\theta^{#} : \mathcal{O}_{x} \to \mathcal{O}_{y}$ is a surjective
homomorphism of rings having as kernel the maximal ideal $\mathfrak{m}_{x}$ of $\mathcal{O}_{x}$. Then the
$\mathcal{O}_{Y^{(n)}}$ are identified with the rings $\mathcal{O}_{x}/\mathfrak{m}^{n+1}_{x}$, and
$\mathcal{GR}_{\bullet}(f)$ with the graded ring associated with the local ring $\mathcal{O}_{x}$ endowed with its
$\mathfrak{m}_{x}$-preadic filtration.*

*(ii) Suppose that $Y$ is a closed subset of an open subspace $U$ of $X$ and that $\mathcal{O}_{Y}$ is induced on $Y$ by
a quotient sheaf $\mathcal{O}_{U}/\mathcal{I}$, where $\mathcal{I}$ is an Ideal of $\mathcal{O}_{U}$ such that
$\mathcal{I}_{x} = \mathcal{O}_{x}$ for every $x \notin Y$; if $X$ is a space ringed in local rings, we suppose in
addition that $\mathcal{I}_{x} \neq \mathcal{O}_{x}$ for $x \in Y$, so that $(Y, \mathcal{O}_{Y})$ is again a space
ringed in local rings. Let $\psi_{0} : Y \to U$ be the canonical injection, and denote by $\theta_{0} : \mathcal{O}_{U}
\to (\psi_{0})_{*}(\mathcal{O}_{Y})$ the homomorphism such that $\theta^{#}_{0}$ is the canonical homomorphism
$\psi_{0}*(\mathcal{O}_{U}) = \mathcal{O}_{U}|Y \to (\mathcal{O}_{U}/\mathcal{I})|Y$, so that $j_{0} = (\psi_{0},
\theta_{0}) : Y \to U$ is a morphism of ringed spaces (and of spaces ringed in local rings if $X$ is a space ringed in
local rings); if $i : U \to X$ is the canonical injection (morphism of ringed spaces), $j = i \circ j_{0}$ is the
morphism $(\psi, \theta)$ of $Y$ into $X$, where $\psi : Y \to X$ is the canonical injection and $\theta :
\mathcal{O}_{X} \to \psi_{*}(\mathcal{O}_{Y})$ is the homomorphism such that $\theta^{#} = \theta^{#}_{0}$. Since
$\theta^{#}$ is surjective, one can apply the preceding definitions; $\mathcal{O}_{Y^{(n)}}$ is equal to
$\psi_{0}*(\mathcal{O}_{U}/\mathcal{I}^{n+1})$, and one has $(\psi_{0})_{*}(\mathcal{O}_{Y^{(n)}}) =
\mathcal{O}_{U}/\mathcal{I}^{n+1}$ and $\mathcal{GR}_{n}(j) = \mathcal{GR}_{n}(j_{0}) =
\psi_{0}*(\mathcal{I}^{n}/\mathcal{I}^{n+1}) = j_{0}*(\mathcal{I}^{n}/\mathcal{I}^{n+1})$.*

**(16.1.4).**

<!-- label: IV.16.1.4 -->

The example `(16.1.3, (ii))` shows that in general the $\mathcal{O}_{Y^{(n)}}$ are not canonically endowed with a
structure of $\mathcal{O}_{Y}$-Module, still less *a fortiori* with a structure of $\mathcal{O}_{Y}$-Algebra. To give
such a structure amounts to giving a homomorphism of sheaves of rings $\lambda_{n} : \mathcal{O}_{Y} \to
\mathcal{O}_{Y^{(n)}}$, right inverse of the augmentation homomorphism $\phi_{0n}$; equivalently, to giving a morphism
of ringed spaces $(1_{Y}, \lambda_{n}) : Y^{(n)} \to Y$, left inverse of the canonical morphism $(1_{Y}, \phi_{0n}) : Y
\to Y^{(n)}$.

**Proposition (16.1.5).**

<!-- label: IV.16.1.5 -->

*Let $f = (\psi, \theta) : Y \to X$ be an immersion of preschemes. Then:*

*(i) $\mathcal{GR}_{\bullet}(f)$ is a quasi-coherent graded $\mathcal{O}_{Y}$-Algebra.*

<!-- original page 7 -->

*(ii) The $Y^{(n)}$ are preschemes, canonically isomorphic to sub-preschemes of $X$.*

*(iii) Every homomorphism of sheaves of rings $\lambda_{n} : \mathcal{O}_{Y} \to \mathcal{O}_{Y^{(n)}}$, right inverse
of the augmentation homomorphism $\phi_{0n}$, makes the $\mathcal{O}_{Y^{(n)}}$ and the $\mathcal{O}_{Y^{(k)}}$ for $k
\leqslant n$ into quasi-coherent $\mathcal{O}_{Y}$-Algebras; the $\mathcal{O}_{Y}$-Module structures deduced from the
preceding structures on the $\mathcal{GR}_{k}(f)$ for $k \leqslant n$ coincide with those defined in `(16.1.2)`.*

(i) The question being local on $X$ and on $Y$, one can restrict oneself to the case where $Y$ is a closed sub-prescheme
of $X$ defined by a quasi-coherent Ideal $\mathcal{I}$ of $\mathcal{O}_{X}$; since $\mathcal{O}_{Y}$ is the restriction
to $Y$ of $\mathcal{O}_{X}/\mathcal{I}$, assertion (i) is evident, and $Y^{(n)}$ is the closed sub-prescheme of $X$
defined by the quasi-coherent Ideal $\mathcal{I}^{n+1}$ of $\mathcal{O}_{X}$. Finally, to prove (iii), note that the
datum of $\lambda_{n}$ makes the Ideal $\mathcal{I}/\mathcal{I}^{n+1}$ of the augmentation $\phi_{0n}$ and its quotients
$\mathcal{I}^{k}/\mathcal{I}^{n+1}$ ($1 \leqslant k \leqslant n$) into $\mathcal{O}_{Y}$-Modules, and it suffices to
prove by induction on $k$ that the $\mathcal{I}^{k}/\mathcal{I}^{n+1}$ are quasi-coherent $\mathcal{O}_{Y}$-Modules and
that the quotient $\mathcal{O}_{Y}$-Module structure deduced on $\mathcal{I}^{k}/\mathcal{I}^{k+1}$ is the same as that
defined in `(16.1.2)`. The second assertion is immediate, $\mathcal{I}^{k}/\mathcal{I}^{k+1}$ being annihilated by
$\mathcal{I}/\mathcal{I}^{n+1}$; the first follows by induction on $k$: it is trivial for $k = 1$, and
$\mathcal{I}^{k}/\mathcal{I}^{n+1}$ is an extension of $\mathcal{I}^{k}/\mathcal{I}^{k+1}$ by
$\mathcal{I}^{k+1}/\mathcal{I}^{n+1}$ `(III, 1.4.17)`.

**Corollary (16.1.6).**

<!-- label: IV.16.1.6 -->

*Under the general hypotheses of `(16.1.5)`, if the immersion $f$ is locally of finite presentation, the
$\mathcal{GR}_{n}(f)$ are quasi-coherent $\mathcal{O}_{Y}$-Modules of finite type.*

Indeed, with the notation of the proof of `(16.1.5)`, $\mathcal{I}$ is an Ideal of finite type of $\mathcal{O}_{X}$
`(1.4.7)`, so the $\mathcal{I}^{n}/\mathcal{I}^{n+1}$ are $\mathcal{O}_{Y}$-Modules of finite type, whence the
conclusion.

**Corollary (16.1.7).**

<!-- label: IV.16.1.7 -->

*Under the general hypotheses of `(16.1.5)`, let $g : X \to Y$ be a morphism of preschemes left inverse to $f$. Then,
for every $n$, the composite morphism $(1_{Y}, \lambda_{n}) : Y^{(n)} \to X \to Y$ defines a homomorphism of sheaves of
rings $\lambda_{n} : \mathcal{O}_{Y} \to \mathcal{O}_{Y^{(n)}}$ right inverse of the augmentation $\phi_{0n}$, making
$\mathcal{O}_{Y^{(n)}}$ into a quasi-coherent $\mathcal{O}_{Y}$-Algebra; for these homomorphisms, the transition
homomorphisms $\phi_{nm} : \mathcal{O}_{Y^{(m)}} \to \mathcal{O}_{Y^{(n)}}$ ($n \leqslant m$) are homomorphisms of
$\mathcal{O}_{Y}$-Algebras. In addition, if $g$ is locally of finite type, the $\mathcal{O}_{Y^{(n)}}$ are
quasi-coherent $\mathcal{O}_{Y}$-Modules of finite type.*

The first assertion follows at once from the definitions and from `(16.1.5)`. On the other hand, if $g$ is locally of
finite type, then $f$ is locally of finite presentation `(1.4.3, (v))`; the $\mathcal{GR}_{n}(f)$ are then
quasi-coherent $\mathcal{O}_{Y}$-Modules of finite type by `(16.1.6)`, so the same holds for the
$\mathcal{O}_{Y}$-Modules $\mathcal{I}/\mathcal{I}^{n+1}$, which are extensions of finitely many of the
$\mathcal{GR}_{k}(f)$ `(III, 1.4.17)`.

**Proposition (16.1.8).**

<!-- label: IV.16.1.8 -->

*Let $X$ be a locally Noetherian prescheme, $j : Y \to X$ an immersion. Then the $Y^{(n)}$ are locally Noetherian
preschemes, the $\mathcal{GR}_{n}(j)$ are coherent $\mathcal{O}_{Y}$-Modules, and $\mathcal{GR}_{\bullet}(j)$ is a
coherent sheaf of rings on the space $Y$.*

Everything being local on $X$ and $Y$, one is reduced to the case where $X$ is affine and $j$ is a closed immersion;
then all the assertions are evident except the last, which follows from the fact that if $A$ is a Noetherian ring and
$\mathfrak{J}$ is an ideal of $A$, then $gr^{\bullet}_{\mathfrak{J}}(A)$ is a Noetherian ring, taking into account the
exactness of the functor $\psi*$ and $(0_{I}, 5.3.7)$.

<!-- original page 8 -->

**Proposition (16.1.9).**

<!-- label: IV.16.1.9 -->

*Let $X$ be a prescheme, $j : Y \to X$ an immersion locally of finite presentation, $y$ a point of $Y$. The following
conditions are equivalent:*

*a) There exists an open neighbourhood $U$ of $y$ in $Y$ such that $j|U$ is a homeomorphism of $U$ onto an open subset
of $X$.*

*b) There exists an integer $n > 0$ such that the canonical homomorphism*

```text
  (φ_{n-1, n})_y : 𝒪_{Y^{(n)}, y} → 𝒪_{Y^{(n-1)}, y}
```

*is bijective.*

*c) There exists an integer $n > 0$ such that $(\mathcal{GR}_{n}(j))_{y} = 0$.*

*Furthermore, if the integer $n$ satisfies b) or c), then there exists a neighbourhood $V$ of $y$ in $Y$ such that
$\mathcal{GR}_{m}(j)|V = 0$ for $m \geqslant n$ and $\phi_{nm}|V : \mathcal{O}_{Y^{(m)}}|V \to \mathcal{O}_{Y^{(n)}}|V$
is bijective for $m \geqslant n$.*

The question being local on $Y$, one can restrict to the case where $j$ is a closed immersion, $Y$ being defined by a
quasi-coherent Ideal of finite type $\mathcal{I}$ of $\mathcal{O}_{X}$. The equivalence of b) and c), for a given $n$,
is then immediate; furthermore, since $\mathcal{I}^{n}/\mathcal{I}^{n+1}$ is an $\mathcal{O}_{X}$-Module of finite type,
there exists an open neighbourhood $U$ of $y$ in $X$ such that $\mathcal{I}^{n}|U = \mathcal{I}^{n+1}|U$ $(0_{I},
5.2.2)$, hence also $\mathcal{I}^{n}|U = \mathcal{I}^{m}|U$ for $m \geqslant n$, which proves the last assertions. To
prove that a) implies b), one can restrict to the case where the space underlying $Y$ is equal to the space underlying
$X$, and where $\mathcal{I}$ is generated by a finite number of its sections over $X$: as $\mathcal{I}$ is then
contained in the nilradical $\mathcal{N}$ of $\mathcal{O}_{X}$ `(I, 5.1.2)`, it is nilpotent, which proves b). Finally,
to prove that b) implies a), one can also restrict to the case where $\mathcal{I}^{n} = \mathcal{I}^{n+1}$; then, for
every $y \in Y$, since $\mathcal{I}_{y} \subset \mathfrak{m}_{y}$, the maximal ideal of $\mathcal{O}_{X, y}$, one
necessarily has $\mathcal{I}^{n}_{y} = 0$ by Nakayama's lemma, since $\mathcal{I}_{y}$ is an ideal of finite type. The
set of $x \in X$ such that $\mathcal{I}^{n}_{x} = 0$ is therefore an open subset $U$ of $X$ containing $Y$ $(0_{I},
5.2.2)$; since on the other hand $\mathcal{I}_{x} \neq 0$ for $x \notin Y$, one necessarily has $U = Y$.

**Corollary (16.1.10).**

<!-- label: IV.16.1.10 -->

*For the restriction of the immersion $j$ to a neighbourhood of $y$ in $Y$ to be an open immersion (in other words, for
$j$ to be a local isomorphism at the point $y$), it is necessary and sufficient that $(\mathcal{GR}_{1}(j))_{y} =
(\mathcal{N}_{Y/X})_{y} = 0$.*

The condition is obviously necessary, and the preceding reasoning, applied for $n = 1$, proves that it is sufficient.

**Remarks (16.1.11).**

<!-- label: IV.16.1.11 -->

(i) Under the conditions of Definition `(16.1.1)`, the projective limit of the projective system
$(\mathcal{O}_{Y^{(n)}}, \phi_{nm})$ of sheaves of rings on $Y$ is called the **normal invariant of infinite order** of
$f$, and sometimes denoted $\mathcal{O}_{Y^{(\infty)}}$. When $X$ is a locally Noetherian prescheme and $j : Y \to X$ is
a closed immersion, so that $Y$ is a closed sub-prescheme of $X$ defined by a coherent Ideal $\mathcal{I}$,
$\mathcal{O}_{Y^{(\infty)}}$ is none other than the formal completion of $\mathcal{O}_{X}$ along $Y$ `(I, 10.8.4)`, and
$Y^{(\infty)} = (Y, \mathcal{O}_{Y^{(\infty)}})$ is the formal prescheme that is the completion of $X$ along $Y$
`(I, 10.8.5)`. In all cases, one may say that $Y^{(\infty)}$ is the **formal neighbourhood** of $Y$ in $X$ (for the
morphism $f$). In the particular case just considered, it is therefore the formal prescheme that is the inductive limit
of the infinitesimal neighbourhoods of order $n$.

(ii) Note that for a morphism of preschemes $f = (\psi, \theta) : Y \to X$, it can happen that the homomorphism
$\theta^{#} : \psi*(\mathcal{O}_{X}) \to \mathcal{O}_{Y}$ is surjective without $f$ being a local

<!-- original page 9 -->

immersion, and without $\psi$ being injective. One has an example by taking for $Y$ a sum of preschemes $Y_{\lambda}$
all isomorphic to $\operatorname{Spec}(\mathcal{O}_{x})$, where $x \in X$, and for $f$ the morphism equal to the
canonical morphism on each of the $Y_{\lambda}$.

### 16.2. Functorial properties of normal invariants of an immersion

**(16.2.1).**

<!-- label: IV.16.2.1 -->

Let $f = (\psi, \theta) : Y \to X$ and $f' = (\psi', \theta') : Y' \to X'$ be two morphisms of ringed spaces such that
the homomorphisms $\theta^{#}$ and $\theta'^{#}$ are surjective; consider a commutative diagram of morphisms of ringed
spaces

```text
  (16.2.1.1)
                  Y  ──f──>  X
                  ↑          ↑
                  u          v
                  │          │
                  Y' ──f'─>  X'
```

Set $u = (\rho, \lambda)$, $v = (\sigma, \mu)$. One has $\rho*(\psi*(\mathcal{O}_{X})) =
\psi'*(\sigma*(\mathcal{O}_{X}))$, and consequently a commutative diagram of homomorphisms of sheaves of rings on $Y'$

```text
  ρ*(ψ*(𝒪_X)) = ψ'*(σ*(𝒪_X)) ──ψ'*(μ^#)──> ψ'*(𝒪_{X'})
              │                                │
              ρ*(θ^#)                          θ'^#
              ↓                                ↓
            ρ*(𝒪_Y) ────────λ^#──────────> 𝒪_{Y'}
```

from which one concludes, if $\mathcal{I}$ and $\mathcal{I}'$ are the kernels of $\theta^{#}$ and $\theta'^{#}$, that
one has $\psi'*(\mu^{#})(\rho*(\mathcal{I})) \subset \mathcal{I}'$, by exactness of the functor $\rho*$. One deduces at
once that for every integer $n$, $\psi'*(\mu^{#})(\rho*(\mathcal{I}^{n})) \subset \mathcal{I}'^{n}$, which shows that
$\psi'*(\mu^{#})$ defines, by passage to the quotients, a homomorphism of sheaves of rings

$$ (16.2.1.2) \nu_{n} : \rho*(\psi*(\mathcal{O}_{X})/\mathcal{I}^{n+1}) \to \psi'*(\mathcal{O}_{X'})/\mathcal{I}'^{n+1}
$$

and consequently a morphism of ringed spaces $w_{n} = (\rho, \nu_{n}) : Y'^{(n)} \to Y^{(n)}$ (which, for $n = 0$, is
none other than $u$). It follows at once from this definition that the diagrams

```text
  Y^{(n)}  ──h_{mn}──>  Y^{(m)}  ──h_m──>  X
     ↑                    ↑                ↑
     w_n                  w_m              v        (n ⩽ m)
     │                    │                │
  Y'^{(n)} ──h'_{mn}──> Y'^{(m)} ──h'_m──> X'
```

(where the horizontal arrows are the canonical morphisms `(16.1.2)`) are commutative.

By passage to the quotients from the homomorphisms `(16.2.1.2)`, and taking into

<!-- original page 10 -->

account the exactness of the functor $\rho*$, one obtains a di-homomorphism of graded Algebras (relative to the
homomorphism $\lambda^{#} : \rho*(\mathcal{O}_{Y}) \to \mathcal{O}_{Y'}$)

$$ (16.2.1.3) gr(u) : \rho*(\mathcal{GR}_{\bullet}(f)) \to \mathcal{GR}_{\bullet}(f') $$

(or, if one prefers, a $\rho$-morphism $(0_{I}, 3.5.1)$ $\mathcal{GR}_{\bullet}(f) \to \mathcal{GR}_{\bullet}(f')$), and
in particular a di-homomorphism of conormal sheaves

$$ gr_{1}(u) : \rho*(\mathcal{GR}_{1}(f)) \to \mathcal{GR}_{1}(f'). $$

It is immediate, moreover, that these homomorphisms give rise to a commutative diagram

```text
  (16.2.1.4)
       ρ*(𝐒_{𝒪_Y}^•(𝒢ℛ_1(f))) ────────> ρ*(𝒢ℛ_•(f))
              │                              │
              𝐒(gr_1(u))                     gr(u)
              ↓                              ↓
       𝐒_{𝒪_{Y'}}^•(𝒢ℛ_1(f'))  ────────>  𝒢ℛ_•(f')
```

where the horizontal arrows are the canonical homomorphisms `(16.1.2.2)`.

Finally, if one has a commutative diagram of morphisms of ringed spaces

```text
       Y   ──f──>  X
       ↑           ↑
       u           v
       │           │
       Y'  ──f'─>  X'
       ↑           ↑
       u'          v'
       │           │
       Y'' ──f''─> X''
```

where $f'' = (\psi'', \theta'')$ is such that $\theta''^{#}$ is surjective, and if $w_{n}$ and $w_{n}'$ are defined from
$u$, $v$ on the one hand, and from $u'' = u \circ u'$, $v'' = v \circ v'$ on the other, then one has $w_{n}'' = w_{n}
\circ w_{n}'$, as follows at once from the definitions and from $(0_{I}, 3.5.5)$; likewise $gr(u'') = gr(u') \circ
\rho'*(gr(u))$ if $u' = (\rho', \lambda')$. One can therefore say that the $Y^{(n)}$ and the $\mathcal{GR}_{\bullet}(f)$
*depend functorially* on $f$.

**Proposition (16.2.2).**

<!-- label: IV.16.2.2 -->

*With the notation and hypotheses of `(16.2.1)`, suppose moreover that $f$, $f'$, $u$ and $v$ are morphisms of
preschemes. Then:*

*(i) The morphisms $w_{n} : Y'^{(n)} \to Y^{(n)}$ are morphisms of preschemes.*

*(ii) If $Y' = Y \times_{X} X'$, with $u$ and $f'$ the canonical projections, and if $f$ is an immersion or $v$ is flat,
one has $Y'^{(n)} = Y^{(n)} \times_{X} X'$.*

*(iii) If $Y' = Y \times_{X} X'$ and if $v$ is flat (resp. if $f$ is an immersion), the homomorphism*

```text
  Gr(u) = gr(u) ⊗ 1 : 𝒢ℛ_•(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_•(f')
```

*is bijective (resp. surjective).*

(i) The hypotheses at once imply that for every $y' \in Y'$, $\rho_{y'}*(\theta^{#}_{\psi'(y')})$ is a local
homomorphism `(I, 1.6.2)`, so $w_{n}$ is a morphism of preschemes `(I, 2.2.1)`.

<!-- original page 11 -->

(ii) and (iii). If $f$ is an immersion, one can restrict to the case where $f$ is a closed immersion, $Y$ being defined
by the quasi-coherent Ideal $\mathcal{I}$ of $\mathcal{O}_{X}$, and $Y^{(n)}$ by the Ideal $\mathcal{I}^{n+1}$; the
assertions then follow from `(I, 4.4.5)`.

Suppose next that $v$ is flat; one can restrict to the case where $X = \operatorname{Spec}(A)$, $Y =
\operatorname{Spec}(B)$, $X' = \operatorname{Spec}(A')$ are affine, $A'$ being a flat $A$-module; then $Y' =
\operatorname{Spec}(B')$ with $B' = B \otimes_{A} A'$. Moreover, if $\mathfrak{J}$ is the kernel of the homomorphism $A
\to B$, the kernel $\mathfrak{J}'$ of $A' \to B'$ is identified with $\mathfrak{J} \otimes_{A} A'$ by flatness, and
$\mathfrak{J}'^{n}/\mathfrak{J}'^{n+1} = (\mathfrak{J}^{n}/\mathfrak{J}^{n+1}) \otimes_{A} A'$. One deduces at once,
taking $(0_{I}, 4.3.3)$ into account, that the $\mathcal{O}_{Y'}$-Module $\mathcal{I}'^{n}/\mathcal{I}'^{n+1}$ is equal
to $(\mathcal{I}^{n}/\mathcal{I}^{n+1}) \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$, and in particular for $n = 0$ one
has

```text
  𝒪_{Y'} = ρ*(𝒪_Y) ⊗_{ρ*(ψ*(𝒪_X))} ψ'*(𝒪_{X'}),
```

which proves (iii). Set now $C_{n} = \Gamma(Y, \mathcal{O}_{Y^{(n)}})$, $C'_{n} = \Gamma(Y', \mathcal{O}_{Y'^{(n)}})$.
Since $Y^{(n)}$ and $Y'^{(n)}$ are affine schemes `(16.1.5)`, the kernel $\mathfrak{K}_{n}$ (resp. $\mathfrak{K}'_{n}$)
of the homomorphism $C_{n} \to C_{n-1}$ (resp. $C'_{n} \to C'_{n-1}$) is $\Gamma(Y, \mathcal{I}^{n}/\mathcal{I}^{n+1})$
(resp. $\Gamma(Y', \mathcal{I}'^{n}/\mathcal{I}'^{n+1})$), so one deduces from the foregoing that $\mathfrak{K}'_{n} =
\mathfrak{K}_{n} \otimes_{A} A'$. One has a commutative diagram

```text
  0 ──> 𝔎_n ⊗_A A' ──> C_n ⊗_A A' ──> C_{n-1} ⊗_A A' ──> 0
         │                │                │
         r                s_n              s_{n-1}
         ↓                ↓                ↓
  0 ──>  𝔎'_n   ──────> C'_n  ─────────> C'_{n-1}  ─────> 0
```

where the left vertical arrow is bijective and the two rows are exact ($A'$ being a flat $A$-module). One deduces by
induction that $s_{n}$ is bijective for all $n$, since it is so by hypothesis for $n = 0$, and the induction step
follows from the five lemma. This proves the second assertion of (ii).

**Corollary (16.2.3).**

<!-- label: IV.16.2.3 -->

*Let $g : X \to Y$, $u : Y' \to Y$ be two morphisms of preschemes, $X' = X \times_{Y} Y'$, and let $g' : X' \to Y'$ and
$v : X' \to X$ be the canonical projections. Let $f : Y \to X$ be a $Y$-section of $X$ (hence an immersion), $f' =
f_{(Y')} : Y' \to X'$ the $Y'$-section of $X'$ deduced from $f$ by the base change $u$. Then:*

*(i) The morphism $w_{n} : Y'^{(n)}_{f'} \to Y^{(n)}_{f}$ corresponding to $f$, $f'$, $u$, $v$ `(16.2.1)` and the
canonical morphism $h'_{n} : Y'^{(n)}_{f'} \to X'$ identify $Y'^{(n)}_{f'}$ with the product $Y^{(n)}_{f} \times_{X}
X'$.*

*(ii) If one endows $\mathcal{O}_{Y^{(n)}_{f}}$ (resp. $\mathcal{O}_{Y'^{(n)}_{f'}}$) with the structure of
$\mathcal{O}_{Y}$-Algebra defined by $g$ (resp. with the structure of $\mathcal{O}_{Y'}$-Algebra defined by $g'$)
`(16.1.7)`, the homomorphism of $\mathcal{O}_{Y'}$-Algebras*

```text
  (16.2.3.1)    ρ*(𝒪_{Y_f^{(n)}}) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒪_{Y'_{f'}^{(n)}}
```

<!-- original page 12 -->

*deduced from the homomorphism $\nu_{n}$ `(16.2.1.2)` is bijective. Furthermore, the homomorphism of
$\mathcal{O}_{Y'}$-Modules*

```text
  (16.2.3.2)    Gr_1(u) : 𝒢ℛ_1(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_1(f')
```

*is bijective.*

(i) Note first that the morphisms $f' : Y' \to X'$ and $u : Y' \to Y$ identify $Y'$ with the product $Y \times_{X} X'$
(for the structure morphisms $f : Y \to X$ and $v : X' \to X$) `(14.5.12.1)`. The conclusion of (i) then follows from
`(16.2.2, (ii))`, the morphism $g$ being an immersion.

(ii) The commutative diagram

```text
                w_n
  Y_f^{(n)} <─────── Y'_{f'}^{(n)}
     │ h_n               │ h'_n
     ↓                   ↓
     X      <─── v ───   X'
     │ g                 │ g'
     ↓                   ↓
     Y      <─── u ───   Y'
```

identifies $Y'^{(n)}_{f'}$ with the product $Y^{(n)}_{f} \times_{X} X'$, so `(I, 3.3.9)` identifies (for the morphisms
$g' \circ h'_{n}$ and $w_{n}$) $Y'^{(n)}_{f'}$ with the product $Y^{(n)}_{f} \times_{Y} Y'$. Since $Y^{(n)}_{f}$ (resp.
$Y'^{(n)}_{f'}$) is the affine prescheme over $Y$ (resp. $Y'$) associated with the $\mathcal{O}_{Y}$-Algebra
$\mathcal{O}_{Y^{(n)}_{f}}$ (resp. with the $\mathcal{O}_{Y'}$-Algebra $\mathcal{O}_{Y'^{(n)}_{f'}}$), the fact that the
canonical homomorphism `(16.2.3.1)` is bijective follows from `(II, 1.5.2)`. Finally, the canonical homomorphism
`(16.2.3.1)` is compatible with the augmentations $\mathcal{O}_{Y^{(n)}_{f}} \to \mathcal{O}_{Y}$ and
$\mathcal{O}_{Y'^{(n)}_{f'}} \to \mathcal{O}_{Y'}$; as $\mathcal{O}_{Y^{(n)}_{f}}$ is the direct sum (as an
$\mathcal{O}_{Y}$-Module) of $\mathcal{O}_{Y}$ and of the augmentation ideal $\mathcal{I}/\mathcal{I}^{n+1}$, one sees
that the canonical homomorphism `(16.2.3.1)`, restricted to $(\mathcal{I}/\mathcal{I}^{n+1}) \otimes_{\mathcal{O}_{Y}}
\mathcal{O}_{Y'}$, is a bijection of the latter onto $\mathcal{I}'/\mathcal{I}'^{n+1}$. For $n = 1$, this shows that
$Gr_{1}(u)$ is bijective.

One will note that, under the hypotheses of `(16.2.3)`, the homomorphisms $Gr_{n}(u)$ are surjective by virtue of the
foregoing, but are not bijective in general for $n \geqslant 2$. However:

**Corollary (16.2.4).**

<!-- label: IV.16.2.4 -->

*Under the hypotheses of `(16.2.3)`, suppose that $u : Y' \to Y$ is a flat morphism (resp. that the
$\mathcal{GR}_{n}(f)$ are flat $\mathcal{O}_{Y}$-Modules for $n \leqslant m$). Then the homomorphism*

```text
  Gr_n(u) : 𝒢ℛ_n(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_n(f')
```

*is bijective for every $n$ (resp. for $n \leqslant m$).*

If $u$ is flat, then so is $v : X' \to X$, which is deduced from it by base change, and one knows already in this case
that $Gr(u)$ is bijective `(16.2.2, (iii))`. If the $\mathcal{GR}_{n}(f)$ are flat for $n \leqslant m$, one sees first
by induction on $n$ that the same holds for the $\mathcal{I}/\mathcal{I}^{n+1}$ for $n \leqslant m$, by virtue of the
exact sequences

$$ 0 \to \mathcal{I}^{n}/\mathcal{I}^{n+1} \to \mathcal{I}/\mathcal{I}^{n+1} \to \mathcal{I}/\mathcal{I}^{n} \to 0 $$

<!-- original page 13 -->

$(0_{I}, 6.1.2)$; furthermore one then has commutative diagrams

```text
  0 → (𝓘^n/𝓘^{n+1}) ⊗ 𝒪_{Y'} → (𝓘/𝓘^{n+1}) ⊗ 𝒪_{Y'} → (𝓘/𝓘^n) ⊗ 𝒪_{Y'} → 0
           │                            │                       │
           ↓                            ↓                       ↓
  0 ──>  𝓘'^n/𝓘'^{n+1}    ─────>    𝓘'/𝓘'^{n+1}    ─────>   𝓘'/𝓘'^n   ────> 0
```

in which the rows are exact (the first by flatness $(0_{I}, 6.1.2)$) and the last two vertical arrows are bijective by
virtue of `(16.2.3, (ii))`; whence the conclusion.

**Remarks (16.2.5).**

<!-- label: IV.16.2.5 -->

(i) The reasoning of `(16.2.2, (i))` still applies when in `(16.2.1.1)` one is dealing with morphisms of spaces ringed
in local rings $(Err_{III}, (1.8.2))$.

(ii) In `(16.2.2, (ii))`, the conclusion is no longer necessarily valid when one only supposes that $v$ and $f$ are
morphisms of preschemes ($f$ satisfying the condition of `(16.1.1)`). For example (with the notation of the proof of
`(16.2.2, (ii))`), it may happen that $\mathfrak{J} = 0$ while the kernel $\mathfrak{J}'$ of $A' \to B' = B \otimes_{A}
A'$ is not zero and $B' \neq 0$, in which case one has $Y^{(n)} = Y$ for all $n$, but $Y'^{(n)} \neq Y'$. One has an
example of this by taking $A = \mathbb{Z}$, $B = \mathbb{Q}$, $A' = \prod^{\infty}_{h=1} (\mathbb{Z}/m^{h} \mathbb{Z})$
where $m > 1$.

**(16.2.6).**

<!-- label: IV.16.2.6 -->

Consider the particular case of the diagram `(16.2.1.1)` where $X' = X$, $v$ is the identity, $X$ is a prescheme, $Y$ a
sub-prescheme of $X$, $Y'$ a sub-prescheme of $Y$, and $f$, $u$, $f' = f \circ u$ are the canonical injections; the
di-homomorphism `(16.2.1.3)` gives, by tensoring with $\mathcal{O}_{Y'}$ over $\rho*(\mathcal{O}_{Y})$, a homomorphism
of graded $\mathcal{O}_{Y'}$-Algebras

$$ (16.2.6.1) u*(\mathcal{GR}_{\bullet}(f)) \to \mathcal{GR}_{\bullet}(f'). $$

On the other hand, one identifies $\mathcal{O}_{Y}$ with $\psi*(\mathcal{O}_{X})/\mathcal{I}_{f}$ and $\mathcal{O}_{Y'}$
with $\rho*(\mathcal{O}_{Y})/\mathcal{I}_{u}$; since $\rho*$ is an exact functor, one has $\rho*(\mathcal{O}_{Y}) =
\rho*(\psi*(\mathcal{O}_{X}))/\rho*(\mathcal{I}_{f}) = \psi'*(\mathcal{O}_{X})/\rho*(\mathcal{I}_{f})$, and since
$\mathcal{O}_{Y'}$ is on the other hand identified with $\psi'*(\mathcal{O}_{X})/\mathcal{I}_{f'}$, one sees that
$\mathcal{I}_{u} = \mathcal{I}_{f'}/\rho*(\mathcal{I}_{f})$. One deduces from this, for every integer $n$, a canonical
homomorphism $\mathcal{I}^{n}_{f'}/\mathcal{I}^{n+1}_{f'} \to \mathcal{I}^{n}_{u}/\mathcal{I}^{n+1}_{u}$, whence a
canonical homomorphism of graded $\mathcal{O}_{Y'}$-Algebras

$$ (16.2.6.2) \mathcal{GR}_{\bullet}(f') \to \mathcal{GR}_{\bullet}(u). $$

**Proposition (16.2.7).**

<!-- label: IV.16.2.7 -->

*Let $X$ be a prescheme, $Y$ a sub-prescheme of $X$, $Y'$ a sub-prescheme of $Y$, $j : Y' \to Y$ the canonical
injection. Then one has an exact sequence of conormal sheaves ($\mathcal{O}_{Y'}$-Modules)*

$$ (16.2.7.1) j*(\mathcal{N}_{Y/X}) \to \mathcal{N}_{Y'/X} \to \mathcal{N}_{Y'/Y} \to 0 $$

*where the arrows are the degree-`1` components of the canonical homomorphisms `(16.2.6.1)` and `(16.2.6.2)`.*

The question being local, one can restrict to the case where $X = \operatorname{Spec}(A)$, $Y =
\operatorname{Spec}(A/\mathfrak{J})$, $Y' = \operatorname{Spec}(A/\mathfrak{K})$, with $\mathfrak{J}$ and $\mathfrak{K}$
ideals of $A$ such that $\mathfrak{J} \subset \mathfrak{K}$; everything reduces to showing

<!-- original page 14 -->

that the sequence of canonical homomorphisms $\mathfrak{J}/\mathfrak{KJ} \to \mathfrak{K}/\mathfrak{K}^{2} \to
(\mathfrak{K}/\mathfrak{J})/(\mathfrak{K}/\mathfrak{J})^{2} \to 0$ is exact, which is immediate, since the image of
$\mathfrak{J}/\mathfrak{KJ}$ in $\mathfrak{K}/\mathfrak{K}^{2}$ is $(\mathfrak{J} + \mathfrak{K}^{2})/\mathfrak{K}^{2}$
and $(\mathfrak{K}/\mathfrak{J})/(\mathfrak{K}/\mathfrak{J})^{2}$ is identified with $\mathfrak{K}/(\mathfrak{J} +
\mathfrak{K}^{2})$.

It is easy to give examples where the sequence `(16.2.7.1)` extended on the left by a `0` is no longer exact; with the
preceding notation, it suffices to take $A = k[T]$, $\mathfrak{J} = AT^{2}$, $\mathfrak{K} = AT$, because then one has
$(\mathfrak{J} + \mathfrak{K}^{2})/\mathfrak{K}^{2} = 0$ and $\mathfrak{J}/\mathfrak{KJ} \neq 0$. See, however,
`(16.9.13)` and `(19.1.5)` for useful cases where the extended sequence remains exact.

### 16.3. Fundamental differential invariants of a morphism of preschemes

**Definition (16.3.1).**

<!-- label: IV.16.3.1 -->

*Let $f : X \to S$ be a morphism of preschemes, $\Delta_{f} : X \to X \times_{S} X$ the corresponding diagonal morphism,
which is an immersion `(I, 5.3.9` and `Err_III, 10)`. One denotes by $\mathcal{P}^{n}_{f}$ or $\mathcal{P}^{n}_{X/S}$,
and calls the **sheaf of principal parts of order $n$ of the $S$-prescheme $X$**, the $\mathcal{O}_{X}$-augmented sheaf
of rings $n$-th normal invariant of $\Delta_{f}$ `(16.1.2)`. One sets $\mathcal{P}^{\infty}_{f} =
\mathcal{P}^{\infty}_{X/S} = \lim\leftarrow_{n} \mathcal{P}^{n}_{X/S}$, $\mathcal{GR}_{n}(\mathcal{P}_{f}) =
\mathcal{GR}_{n}(\mathcal{P}_{X/S}) = \mathcal{GR}_{n}(\Delta_{f})$ `(16.1.2)`; the $\mathcal{O}_{X}$-Module
$\mathcal{GR}_{1}(\Delta_{f})$, augmentation ideal of $\mathcal{P}^{1}_{X/S}$, is also denoted $\Omega^{1}_{f}$ or
$\Omega^{1}_{X/S}$, and is called the **$\mathcal{O}_{X}$-Module of `1`-differentials** of $f$, or of $X$ with respect
to $S$, or of the $S$-prescheme $X$.*

It follows from this definition that $\mathcal{P}^{0}_{X/S}$ is canonically identified with $\mathcal{O}_{X}$
`(16.1.2)`.

One has `(16.1.2.2)` a canonical surjective homomorphism of graded $\mathcal{O}_{X}$-Algebras

$$ (16.3.1.1) \mathbf{S}^{\bullet}_{\mathcal{O}_{X}}(\Omega^{1}_{X/S}) \to \mathcal{GR}_{\bullet}(\mathcal{P}_{X/S}). $$

It also follows from Definition `(16.3.1)` that for every open $U$ of $X$, one has $\mathcal{P}^{n}_{f|U} =
\mathcal{P}^{n}_{f}|U$, $\mathcal{P}^{\infty}_{f|U} = \mathcal{P}^{\infty}_{f}|U$, $\mathcal{GR}_{n}(\mathcal{P}_{f|U})
= \mathcal{GR}_{n}(\mathcal{P}_{f})|U$, $\Omega^{1}_{f|U} = \Omega^{1}_{f}|U$ (in other words, the notions introduced
are local on $X$).

**(16.3.2).**

<!-- label: IV.16.3.2 -->

Denote by $p_{1}$, $p_{2}$ the two canonical projections of the product $X \times_{S} X$; since $\Delta_{f}$ is an
$X$-section of $X \times_{S} X$ for both morphisms $p_{1}$ and $p_{2}$, *each* of these morphisms defines, for every
$n$, a homomorphism of sheaves of rings $\mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}$, right inverse to the augmentation
$\mathcal{P}^{n}_{X/S} \to \mathcal{O}_{X}$ `(16.1.7)`; one can also say that one thus defines on
$\mathcal{P}^{n}_{X/S}$ *two* quasi-coherent augmented $\mathcal{O}_{X}$-Algebra structures; the corresponding
$\mathcal{O}_{X}$-Module structures on $\mathcal{GR}_{n}(\mathcal{P}_{X/S})$ are the same. One similarly has, by passage
to the limit, two $\mathcal{O}_{X}$-Algebra structures on $\mathcal{P}^{\infty}_{X/S}$.

**(16.3.3).**

<!-- label: IV.16.3.3 -->

The morphism $s = (p_{2}, p_{1})_{S} : X \times_{S} X \to X \times_{S} X$ is an involutive automorphism of $X \times_{S}
X$, called the **canonical symmetry**, such that

```text
  (16.3.3.1)    p_1 ∘ s = p_2,   p_2 ∘ s = p_1,   s ∘ Δ_f = Δ_f.
```

If one sets $s = (\rho, \lambda)$, $p_{i} = (\pi_{i}, \mu_{i})$ ($i = 1, 2$), $\Delta_{f} = (\delta, \nu)$, then
$\lambda^{#}$ is an isomorphism of $\rho*(\pi_{1}*(\mathcal{O}_{X}))$ onto $\pi_{2}*(\mathcal{O}_{X})$, and
$\delta*(\lambda^{#})$ leaves invariant $\delta*(\mathcal{O}_{X \times_{S} X})$ and the kernel $\mathcal{I}$ of the
homomorphism $\nu^{#} : \delta*(\mathcal{O}_{X \times_{S} X}) \to \mathcal{O}_{X}$. Therefore:

**Proposition (16.3.4).**

<!-- label: IV.16.3.4 -->

*The homomorphism $\sigma = \delta*(\lambda^{#})$ deduced from $s$ (and also called the canonical symmetry) is an
involutive automorphism of the projective system $(\mathcal{P}^{n}_{X/S})$ of $\mathcal{O}_{X}$-augmented*

<!-- original page 15 -->

*sheaves of rings, and consequently also of their projective limit $\mathcal{P}^{\infty}_{X/S}$. This automorphism
permutes the two $\mathcal{O}_{X}$-Algebra structures on the $\mathcal{P}^{n}_{X/S}$ and on
$\mathcal{P}^{\infty}_{X/S}$.*

**(16.3.5).**

<!-- label: IV.16.3.5 -->

In what follows, the two $\mathcal{O}_{X}$-Algebra structures defined on the $\mathcal{P}^{n}_{X/S}$ and on
$\mathcal{P}^{\infty}_{X/S}$ will play very different roles: *we shall agree from now on, unless expressly stated
otherwise, that when $\mathcal{P}^{n}_{X/S}$ or $\mathcal{P}^{\infty}_{X/S}$ is considered as an
$\mathcal{O}_{X}$-Algebra, it is the algebra structure defined by $p_{1}$ that is meant.*

For every open $U$ of $X$ and every section $t \in \Gamma(U, \mathcal{O}_{X})$, one will denote simply by $t \cdot 1$ or
even $t$ the image of $t$ under the structural homomorphism $\Gamma(U, \mathcal{O}_{X}) \to \Gamma(U,
\mathcal{P}^{n}_{X/S})$ (resp. $\Gamma(U, \mathcal{O}_{X}) \to \Gamma(U, \mathcal{P}^{\infty}_{X/S})$) (that is to say,
the homomorphism corresponding to $p_{1}$).

**Definition (16.3.6).**

<!-- label: IV.16.3.6 -->

*One denotes by $d^{n}_{f}$, or $d^{n}_{X/S}$ (resp. $d^{\infty}_{f}$, or $d^{\infty}_{X/S}$), or simply $d^{n}$ (resp.
$d^{\infty}$), the homomorphism of sheaves of rings $\mathcal{O}_{X} \to \mathcal{P}^{n}_{f} = \mathcal{P}^{n}_{X/S}$
(resp. $\mathcal{O}_{X} \to \mathcal{P}^{\infty}_{f} = \mathcal{P}^{\infty}_{X/S}$) deduced from $p_{2}$. For every open
$U$ of $X$ and every $t \in \Gamma(U, \mathcal{O}_{X})$, $d^{n} t$ (resp. $d^{\infty} t$) is called the **principal part
of order $n$** (resp. **principal part of infinite order**) of $t$. One sets $dt = d^{1} t - t \cdot 1$, and `dt` is
called the **differential of $t$** (an element of $\Gamma(U, \Omega^{1}_{X/S})$, also denoted $d_{X/S}(t)$).*

It follows at once from this definition that one has

```text
  (16.3.6.1)    d(t_1 t_2) = t_1 dt_2 + t_2 dt_1
```

for any $t_{1}$, $t_{2}$ in $\Gamma(U, \mathcal{O}_{X})$, that is to say, *$d$ is a derivation* of the ring $\Gamma(U,
\mathcal{O}_{X})$ into the $\Gamma(U, \mathcal{O}_{X})$-module $\Gamma(U, \Omega^{1}_{X/S})$.

In all the notation introduced in `(16.3.1)` and `(16.3.6)`, one will sometimes replace $S$ by $A$ when $S =
\operatorname{Spec}(A)$.

**(16.3.7).**

<!-- label: IV.16.3.7 -->

Suppose in particular that $S = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$ are affine schemes, $B$ being
therefore an $A$-algebra. Then $\Delta_{f}$ corresponds to the canonical surjective homomorphism $\pi : B \otimes_{A} B
\to B$ such that $\pi(b \otimes b') = b b'$, with kernel $\mathfrak{J} = \mathfrak{J}_{B/A}$ `(0, 20.4.1)`;
$\mathcal{P}^{n}_{f}$ is the structure sheaf of the prescheme $\operatorname{Spec}(P^{n}_{B/A})$, where

```text
  P_{B/A}^n = (B ⊗_A B) / 𝔍^{n+1};
```

$\mathcal{GR}_{\bullet}(\mathcal{P}_{f})$ is the quasi-coherent $\mathcal{O}_{X}$-Module corresponding to the graded
$B$-module

```text
  gr_𝔍^•(B ⊗_A B) = ⨁_{n ⩾ 0} (𝔍^n / 𝔍^{n+1});
```

in particular $\Omega^{1}_{f} = \Omega^{1}_{X/S}$ is the quasi-coherent $\mathcal{O}_{X}$-Module corresponding to the
$B$-module of `1`-differentials of $B$ with respect to $A$, namely $\Omega^{1}_{B/A}$ `(0, 20.4.3)`. The projection
morphisms $p_{1} : X \times_{S} X \to X$, $p_{2} : X \times_{S} X \to X$ correspond to the two ring homomorphisms
$j_{1} : B \to B \otimes_{A} B$, $j_{2} : B \to B \otimes_{A} B$ such that $j_{1}(b) = b \otimes 1$,
$j_{2}(b) = 1 \otimes b$, so that (by the convention of `(16.3.5)`) $P^{n}_{B/A}$ is always considered as a $B$-algebra
via the composite homomorphism $B \to B \otimes_{A} B \to P^{n}_{B/A}$; the ring homomorphism
$B \to B \otimes_{A} B \to P^{n}_{B/A}$ deduced from $j_{2}$ is denoted $d^{n}_{B/A}$ and corresponds to $d^{n}_{X/S}$
acting on $\Gamma(X, \mathcal{O}_{X})$; for every $t \in B$, `dt` is equal to $d_{B/A} t$, defined in `(0, 20.4.6)` (cf.
$Err_{IV}, 11$).

If $\pi_{n} : B \otimes_{A} B \to P^{n}_{B/A}$ is the canonical homomorphism, one therefore has, by virtue of the
preceding definitions,

```text
  (16.3.7.1)    π_n(b ⊗ b') = b · π_n(1 ⊗ b') = b · d_{B/A}^n(b')   for b ∈ B, b' ∈ B.
```

<!-- original page 16 -->

**Proposition (16.3.8).**

<!-- label: IV.16.3.8 -->

*The image of the homomorphism $d^{n}_{X/S} : \mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}$ generates the
$\mathcal{O}_{X}$-Module $\mathcal{P}^{n}_{X/S}$.*

One reduces at once to the case where $X = \operatorname{Spec}(B)$ and $S = \operatorname{Spec}(A)$ are affine, and the
proposition follows from `(16.3.7.1)` since $\pi_{n}$ is surjective. Note that in general $d^{n}_{X/S}$ is not
surjective (even already for $n = 1$).

**Proposition (16.3.9).**

<!-- label: IV.16.3.9 -->

*Suppose that $f : X \to S$ is a morphism locally of finite type. Then the $\mathcal{P}^{n}_{X/S}$ and the
$\mathcal{GR}_{n}(\mathcal{P}_{X/S})$ are quasi-coherent $\mathcal{O}_{X}$-Modules of finite type.*

This follows from `(16.1.6)` and from the fact that $\Delta_{f}$ is locally of finite presentation `(1.4.3.1)`.

### 16.4. Functorial properties of differential invariants

**(16.4.1).**

<!-- label: IV.16.4.1 -->

Consider a commutative diagram of morphisms of preschemes

```text
  (16.4.1.1)
                  X   <──u──   X'
                  │            │
                  f            f'
                  ↓            ↓
                  S   <──w──   S'
```

One deduces a commutative diagram

```text
                   X        <──u──    X'
                   │                  │
                   Δ_f                Δ_{f'}
                   ↓                  ↓
                X ×_S X   <──v──   X' ×_{S'} X'
```

where $v$ is the composite morphism `(I, 5.3.5` and `5.3.15)`

```text
  (16.4.1.2)    X' ×_{S'} X' ──(p'_1, p'_2)_S──> X' ×_S X' ──u ×_S u──> X ×_S X.
```

One therefore deduces from $u$ and $v$, as was explained in `(16.2.1)`, homomorphisms of augmented sheaves of rings

$$ (16.4.1.3) \nu_{n} : \rho*(\mathcal{P}^{n}_{X/S}) \to \mathcal{P}^{n}_{X'/S'} $$

(where one has set $u = (\rho, \lambda)$); these homomorphisms form a projective system, and consequently give at the
limit a homomorphism of augmented sheaves of rings

$$ (16.4.1.4) \nu_{\infty} : \rho*(\mathcal{P}^{\infty}_{X/S}) \to \mathcal{P}^{\infty}_{X'/S'}; $$

on the other hand, by passage to the quotients, the homomorphisms $\nu_{n}$ give a di-homomorphism of graded Algebras
(relative to $\lambda^{#}$):

$$ (16.4.1.5) gr(u) : \rho*(\mathcal{GR}_{\bullet}(\mathcal{P}_{X/S})) \to \mathcal{GR}_{\bullet}(\mathcal{P}_{X'/S'}).
$$

<!-- original page 17 -->

**(16.4.2).**

<!-- label: IV.16.4.2 -->

If one has a commutative diagram

```text
        X   <──u──   X'  <──u'──  X''
        │            │            │
        f            f'           f''
        ↓            ↓            ↓
        S   <──w──   S'  <──w'──  S''
```

one deduces a commutative diagram

```text
              X       <──u──     X'     <──u'──     X''
              │                  │                  │
              Δ_f                Δ_{f'}             Δ_{f''}
              ↓                  ↓                  ↓
           X ×_S X   <──v──   X' ×_{S'} X'  <─v'─  X'' ×_{S''} X''
```

where $v'$ is defined from $u'$, $w'$, $f'$, `f''` as $v$ was from $u$, $w$, $f$, $f'$. One verifies at once that if
$u'' = u \circ u'$, $w'' = w \circ w'$, then the composite morphism $v \circ v'$ is equal to the morphism `v''` defined
from `u''`, `w''`, $f$, `f''` as $v$ was from $u$, $w$, $f$, $f'$. If one sets $u' = (\rho', \lambda')$, $u'' = (\rho'',
\lambda'')$, it then follows from `(16.2.1)` that the homomorphism $\nu''_{n} : \rho''*(\mathcal{P}^{n}_{X/S}) \to
\mathcal{P}^{n}_{X''/S''}$ is equal to the composite

```text
  ρ'*(ρ*(𝒫_{X/S}^n)) ──ρ'*(ν_n)──> ρ'*(𝒫_{X'/S'}^n) ──ν'_n──> 𝒫_{X''/S''}^n,
```

and one has analogous transitivity properties for the homomorphisms `(16.4.1.4)` and `(16.4.1.5)`, which allows one to
say that the $\mathcal{P}^{n}_{X/S}$, $\mathcal{P}^{\infty}_{X/S}$ and $\mathcal{GR}_{\bullet}(\mathcal{P}_{X/S})$
*depend functorially on $f$*.

**(16.4.3).**

<!-- label: IV.16.4.3 -->

One verifies at once (for example by reducing to the affine case using `(16.3.7)`) that with the notation of `(16.4.1)`,
the diagram

```text
  (16.4.3.1)
              ρ*(𝒪_X)  ──λ^#──>  𝒪_{X'}
                │                  │
                ↓                  ↓
            ρ*(𝒫_{X/S}^n) ──ν_n──> 𝒫_{X'/S'}^n
```

where the vertical arrows are those defining the algebra structures chosen in `(16.3.5)` (that is to say, those coming
from the first projections), is commutative; the same holds for the diagram

```text
  (16.4.3.2)
              ρ*(𝒪_X)         ──λ^#──>      𝒪_{X'}
                │                              │
                ρ*(d_{X/S}^n)                  d_{X'/S'}^n
                ↓                              ↓
            ρ*(𝒫_{X/S}^n)   ──ν_n──>      𝒫_{X'/S'}^n
```

<!-- original page 18 -->

the vertical arrows here defining the algebra structures coming from the second projections; moreover, if $\sigma$ and
$\sigma'$ are the canonical symmetries corresponding to $f$ and $f'$ `(16.3.4)`, one has

```text
  ν_n ∘ ρ*(σ) = σ' ∘ ν_n
```

which lets one pass from one of the preceding diagrams to the other. One therefore deduces from `(16.4.3.1)` a canonical
homomorphism of augmented $\mathcal{O}_{X'}$-Algebras

```text
  (16.4.3.3)    P^n(u) : u*(𝒫_{X/S}^n) = 𝒫_{X/S}^n ⊗_{𝒪_X} 𝒪_{X'} → 𝒫_{X'/S'}^n
```

and it follows from `(16.4.3.2)` that the diagram

```text
  (16.4.3.4)
              𝒪_{X'}             ──id──>          𝒪_{X'}
                │                                  │
                u*(d_{X/S}^n)                      d_{X'/S'}^n
                ↓                                  ↓
            u*(𝒫_{X/S}^n)     ──P^n(u)──>      𝒫_{X'/S'}^n
```

is commutative. One deduces from it a homomorphism of graded $\mathcal{O}_{X'}$-Algebras

$$ (16.4.3.5) Gr_{\bullet}(u) : u*(\mathcal{GR}_{\bullet}(\mathcal{P}_{X/S})) \to
\mathcal{GR}_{\bullet}(\mathcal{P}_{X'/S'}) $$

and in particular a homomorphism of $\mathcal{O}_{X'}$-Modules

```text
  (16.4.3.6)    Gr_1(u) : Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_{X'} → Ω_{X'/S'}^1
```

giving rise to a commutative diagram

```text
  (16.4.3.7)
              𝒪_{X'}                ──id──>               𝒪_{X'}
                │                                            │
                d_{X/S} ⊗ 1                                  d_{X'/S'}
                ↓                                            ↓
            Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_{X'}    ────────────>    Ω_{X'/S'}^1
```

**(16.4.4).**

<!-- label: IV.16.4.4 -->

When $S = \operatorname{Spec}(A)$, $S' = \operatorname{Spec}(A')$, $X = \operatorname{Spec}(B)$, $X' =
\operatorname{Spec}(B')$ are affine, so that one has a commutative diagram of ring homomorphisms

```text
              B  ──>  B'
              ↑       ↑
              A  ──>  A'
```

the image of $\mathfrak{J}_{B/A}$ in $B' \otimes_{A'} B'$ is contained in $\mathfrak{J}_{B'/A'}$, and the homomorphism
$\nu_{n}$ corresponds to the ring homomorphism $P^{n}_{B/A} \to P^{n}_{B'/A'}$ deduced from the homomorphism $B
\otimes_{A} B \to B' \otimes_{A'} B'$ by passage to the quotients. The homomorphism `(16.4.3.6)` corresponds to the
homomorphism defined in `(0, 20.5.4.1)`, and the commutative diagram `(16.4.3.7)` to the diagram `(0, 20.5.4.2)`.

**Proposition (16.4.5).**

<!-- label: IV.16.4.5 -->

*Suppose that $X' = X \times_{S} S'$, with $f'$ and $u$ the canonical projections.*

<!-- original page 19 -->

*Then the canonical homomorphisms $P^{n}(u)$ `(16.4.3.3)` and $Gr_{1}(u)$ `(16.4.3.6)` are bijective.*

One indeed has $X' \times_{S'} X' = (X \times_{S} X) \times_{S} S'$, and it suffices to apply `(16.2.3, (ii))` replacing
$g$ by the first projection $p_{1} : X \times_{S} X \to X$ and $f$ by the diagonal $\Delta_{f}$.

One will note also that under the hypotheses of `(16.4.5)`, the homomorphism $Gr_{\bullet}(u)$ `(16.4.3.5)` is
surjective, but not bijective in general. However `(16.2.4)`:

**Corollary (16.4.6).**

<!-- label: IV.16.4.6 -->

*With the hypotheses of `(16.4.5)`, suppose in addition that $w : S' \to S$ is flat (resp. that the
$\mathcal{GR}_{n}(\mathcal{P}_{X/S})$ are flat $\mathcal{O}_{X}$-Modules for $n \leqslant m$); then the homomorphism*

$$ Gr_{n}(u) : u*(\mathcal{GR}_{n}(\mathcal{P}_{X/S})) \to \mathcal{GR}_{n}(\mathcal{P}_{X'/S'}) $$

*is bijective for every $n$ (resp. for $n \leqslant m$).*

Indeed, if $w$ is flat, so is $v : X' \times_{S'} X' \to X \times_{S} X$, deduced from it by base change, and the
conclusion follows from `(16.2.4)`.

**(16.4.7).**

<!-- label: IV.16.4.7 -->

Let $S$ be a prescheme, $\mathcal{E}$ a quasi-coherent $\mathcal{O}_{S}$-Module, and set $X = \mathbf{V}(\mathcal{E})$
`(II, 1.7.8)`, the **vector bundle** associated with $\mathcal{E}$, equal to
$\operatorname{Spec}(\mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E}))$. Let $f : X \to S$ be the structure morphism. For every
open $U$ of $S$ and every section $t \in \Gamma(U, \mathcal{E})$, $t$ is identified with a section of
$\mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E})$ over $U$; let $t'$ be its image in $\Gamma(f^{-1}(U), \mathcal{O}_{X}) =
\Gamma(U, f_{*}(\mathcal{O}_{X})) = \Gamma(U, \mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E}))$, and set

```text
  (16.4.7.1)    δ(t) = d_{X/S}^n(t') - t' ∈ Γ(f^{-1}(U), 𝒫_{X/S}^n);
```

it is clear that $\delta$ is a di-homomorphism of modules (corresponding to the ring homomorphism $\Gamma(U,
\mathcal{O}_{S}) \to \Gamma(f^{-1}(U), \mathcal{O}_{X})$) of $\Gamma(U, \mathcal{E})$ into $\Gamma(f^{-1}(U),
\mathcal{P}^{n}_{X/S})$, whose image moreover belongs to the augmentation ideal of $\Gamma(f^{-1}(U),
\mathcal{P}^{n}_{X/S})$. One deduces (by varying $U$) a canonical homomorphism of $\mathcal{O}_{X}$-Algebras

$$ (16.4.7.2) f*(\mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E})) \to \mathcal{P}^{n}_{X/S} $$

and by the preceding remark, if $\mathcal{K}$ is the Ideal kernel of the augmentation
$\mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E}) \to \mathcal{O}_{S}$, the image of $\mathcal{K}^{n+1}$ under `(16.4.7.2)` is
zero, so that by factoring through $\mathcal{K}^{n+1}$ one finally has a canonical homomorphism

$$ (16.4.7.3) \delta_{n} : f*(\mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E})/\mathcal{K}^{n+1}) \to \mathcal{P}^{n}_{X/S}. $$

**Proposition (16.4.8).**

<!-- label: IV.16.4.8 -->

*Under the conditions of `(16.4.7)`, the homomorphisms $\delta_{n}$ are bijective and form a projective system of
isomorphisms; one deduces an isomorphism of graded $\mathcal{O}_{X}$-Algebras*

$$ (16.4.8.1) f*(\mathbf{S}^{\bullet}_{\mathcal{O}_{S}}(\mathcal{E})) \xrightarrow{\sim}
\mathcal{GR}_{\bullet}(\mathcal{P}_{X/S}). $$

The fact that the homomorphisms `(16.4.7.3)` form a projective system follows at once from their definition. To prove
that they are isomorphisms, it suffices to

<!-- original page 20 -->

show that `(16.4.8.1)` is an isomorphism, the filtrations of the two sides of `(16.4.7.3)` being finite (Bourbaki, *Alg.
comm.*, chap. III, §2, n° 8, cor. 3 of th. 1). For this, consider the split exact sequence of $\mathcal{O}_{S}$-Modules

```text
  (16.4.8.2)    0 → ℰ ──u──> ℰ ⊕ ℰ ──v──> ℰ → 0
```

where, for every pair of sections $s$, $t$ of $\mathcal{E}$ over an open $U$ of $S$, one takes $u(s) = (-s, s)$ and
$v(s, t) = s + t$. One has

```text
  X ×_S X = Spec(𝐒_{𝒪_S}(ℰ) ⊗_{𝒪_S} 𝐒_{𝒪_S}(ℰ)) = Spec(𝐒_{𝒪_S}(ℰ ⊕ ℰ))
```

`(II, 1.4.6` and `1.7.11)`, and the diagonal morphism $X \to X \times_{S} X$ corresponds `(II, 1.2.7)` to the
homomorphism of $\mathcal{O}_{S}$-Algebras $\mathbf{S}(v) : \mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E} \oplus \mathcal{E})
\to \mathbf{S}_{\mathcal{O}_{S}}(\mathcal{E})$ `(II, 1.7.4)`, so that if $\mathcal{I}$ is the kernel of this
homomorphism, one has

```text
  𝒫_{X/S}^n = f*(𝐒_{𝒪_S}(ℰ ⊕ ℰ) / 𝓘^{n+1}).
```

The proposition will be a consequence of the following lemma:

**Lemma (16.4.8.3).**

<!-- label: IV.16.4.8.3 -->

*Let $Y$ be a ringed space, `0 → ℱ' ──u──> ℱ ──v──> ℱ'' → 0` an exact sequence of $\mathcal{O}_{Y}$-Modules such that
every point $y \in Y$ has an open neighbourhood $V$ such that the sequence $0 \to \mathcal{F}'|V \to \mathcal{F}|V \to
\mathcal{F}''|V \to 0$ is split. Let $\mathcal{I}$ be the Ideal kernel of $\mathbf{S}(v) :
\mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F}) \to \mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F}'')$, and let
$gr^{\bullet}_{\mathcal{I}}(\mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F}))$ be the graded $\mathcal{O}_{Y}$-Algebra
associated with the $\mathcal{O}_{Y}$-Algebra $\mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F})$ endowed with the
$\mathcal{I}$-preadic filtration. Then the homomorphism of graded $\mathcal{O}_{Y}$-Algebras*

```text
  (16.4.8.4)    𝐒_{𝒪_Y}^•(ℱ') ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'') → gr_𝓘^•(𝐒_{𝒪_Y}(ℱ))
```

*(where the first member is the graded tensor product of symmetric $\mathcal{O}_{Y}$-Algebras endowed with their
canonical gradation `(II, 1.7.4` and `2.1.2)`), arising from the canonical injection*

$$ \mathcal{F}' \to \mathcal{I} = gr^{1}_{\mathcal{I}}(\mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F})), $$

*is bijective.*

The injection $\mathcal{F}' \to \mathcal{I}$ indeed canonically gives a homomorphism of graded
$\mathcal{O}_{Y}$-Algebras $\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}') \to
gr^{\bullet}_{\mathcal{I}}(\mathbf{S}_{\mathcal{O}_{Y}}(\mathcal{F}))$, and since the second member is by definition a
graded $\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$-Algebra, one deduces the canonical homomorphism
`(16.4.8.4)` by tensoring the previous one with $\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$. To prove the
lemma, since the question is local, one can restrict to the case where $\mathcal{F} = \mathcal{F}' \oplus
\mathcal{F}''$, with $u$ and $v$ the canonical homomorphisms. Then the graded Algebra
$\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F})$ is canonically identified with the graded tensor product
$\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}') \otimes_{\mathcal{O}_{Y}}
\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$ `(II, 1.7.4)`, and it is immediate that $\mathcal{I}$ is then the
Ideal $\mathcal{I}' \otimes_{\mathcal{O}_{Y}} \mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$, where
$\mathcal{I}'$ is the augmentation ideal of $\mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}')$, that is to say the
(direct) sum of the $\mathbf{S}^{m}_{\mathcal{O}_{Y}}(\mathcal{F}')$ for $m \geqslant 1$. One concludes that
$\mathcal{I}^{n} = \mathcal{I}'^{n} \otimes_{\mathcal{O}_{Y}} \mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$,
where this time $\mathcal{I}'^{n}$ is the (direct) sum of the $\mathbf{S}^{m}_{\mathcal{O}_{Y}}(\mathcal{F}')$ for $m
\geqslant n$; one therefore has $\mathcal{I}^{n}/\mathcal{I}^{n+1} = \mathbf{S}^{n}_{\mathcal{O}_{Y}}(\mathcal{F}')
\otimes_{\mathcal{O}_{Y}} \mathbf{S}^{\bullet}_{\mathcal{O}_{Y}}(\mathcal{F}'')$, which proves that `(16.4.8.4)` is
bijective.

<!-- original page 21 -->

The lemma being established, it remains to check that the homomorphism `(16.4.8.1)` is the image under $f*$ of the
homomorphism `(16.4.8.4)` corresponding to the exact sequence `(16.4.8.2)`; one verifies easily that this follows from
the definition of $u$ `(16.4.8.2)` and of $\delta$ `(16.4.7.1)`, taking into account the definition of the
$\mathcal{O}_{X}$-Algebra structure on $\mathcal{P}^{n}_{X/S}$ and that of $d^{n}_{X/S}$ `(16.3.5` and `16.3.6)`.

In particular:

**Corollary (16.4.9).**

<!-- label: IV.16.4.9 -->

*Under the conditions of `(16.4.7)`, one has a canonical isomorphism*

$$ (16.4.9.1) gr_{1}(\delta) : f*(\mathcal{E}) \xrightarrow{\sim} \Omega^{1}_{X/S}. $$

**Corollary (16.4.10).**

<!-- label: IV.16.4.10 -->

*If $S = \operatorname{Spec}(A)$, $\mathcal{E} = \mathcal{O}^{m}_{S}$, so that*

$$ X = \operatorname{Spec}(A[T_{1}, \cdots, T_{m}]), $$

*then $\mathcal{P}^{n}_{X/S}$ is canonically identified with the $\mathcal{O}_{X}$-Algebra corresponding to the quotient
$A[T_{1}, \cdots, T_{m}]$-algebra $A[T_{1}, \cdots, T_{m}, U_{1}, \cdots, U_{m}]/\mathfrak{K}^{n+1}$, where the $U_{i}$
($1 \leqslant i \leqslant m$) are $m$ new indeterminates and $\mathfrak{K}$ is the ideal generated by $U_{1}, \cdots,
U_{m}$.*

One thus recovers in particular the structure of $\Omega^{1}_{X/S}$ in this case `(0, 20.5.13)`.

Note moreover that $d^{n}_{X/S}$ then assigns to a polynomial $F(T_{1}, \cdots, T_{m})$ the class modulo
$\mathfrak{K}^{n+1}$ of $F(T_{1} + U_{1}, \cdots, T_{m} + U_{m})$, as follows from the definition `(16.4.7.1)`.

**Proposition (16.4.11).**

<!-- label: IV.16.4.11 -->

*Let $f : X \to S$ be a morphism, $g : S \to X$ an $S$-section of $X$, $S^{(n)}_{g}$ the $n$-th infinitesimal
neighbourhood of $S$ for the immersion $g$ `(16.1.2)`. Then there exists one and only one isomorphism of
$\mathcal{O}_{S}$-Algebras*

$$ (16.4.11.1) \varpi_{n} : g*(\mathcal{P}^{n}_{X/S}) \xrightarrow{\sim} \mathcal{O}_{S^{(n)}_{g}} $$

*(for the $\mathcal{O}_{S}$-Algebra structure on $\mathcal{O}_{S^{(n)}_{g}}$ defined by $f$ `(16.1.7)`) making the
diagram*

```text
  (16.4.11.2)
              𝒪_S = g*(𝒪_X)  ────λ_n────>  𝒪_{S_g^{(n)}}
                     ╲                     ╱
            g*(d_{X/S}^n) ╲               ╱ ϖ_n
                          ↘             ↗
                          g*(𝒫_{X/S}^n)
```

*commutative (where $\lambda_{n}$ is the structural homomorphism).*

By virtue of `(I, 5.3.7)`, where one replaces $X$, $Y$, $S$ by $S$, $X$, $S$ respectively and $f$ by $g$, the diagrams

```text
  (16.4.11.3)
       S  ──g──>  X                  S  ──g──>  X
       │          │                  │          │
       g          Δ_f                g          Δ_f
       ↓          ↓                  ↓          ↓
       X ──(g∘f, 1_X)_S──> X ×_S X   X ──(1_X, g∘f)_S──> X ×_S X
```

<!-- original page 22 -->

identify $S$ with the product of the $(X \times_{S} X)$-preschemes $X$ and $X$ for the morphisms $\Delta_{f}$ and $(g
\circ f, 1_{X})_{S}$ (resp. $(1_{X}, g \circ f)_{S}$). On the other hand, the diagrams

```text
  (16.4.11.4)
       X ──(g∘f, 1_X)_S──> X ×_S X    X ──(1_X, g∘f)_S──> X ×_S X
       │                   │          │                   │
       f                   p_1        f                   p_2
       ↓                   ↓          ↓                   ↓
       S ─────g─────>      X          S ─────g─────>      X
```

identify $X$ with the product of the $X$-preschemes $S$ and $X \times_{S} X$ for the morphisms $g$ and $p_{1}$ (resp.
$p_{2}$) (a particular case of the associativity formula `(I, 3.3.9.1)`). One can say that $\Delta_{f}$, considered as
an $X$-section of $X \times_{S} X$ (relative to $p_{1}$ or $p_{2}$), plays the role of a *universal section* for the
$S$-sections of $X$: each such section $g$ is in fact deduced from it by the base change $(g \circ f, 1_{X})_{S} : X \to
X \times_{S} X$. The definition of the homomorphism $\varpi_{n}$ and the fact that it is bijective therefore follow from
these remarks and from `(16.2.3, (ii))` applied to the first diagram `(16.4.11.4)`. The commutativity of the diagram
`(16.4.11.2)` likewise follows from `(16.2.3, (ii))` applied this time to the second diagram `(16.4.11.4)`. To make
$\varpi_{n}$ explicit, one can restrict to the case where $g$ is a closed immersion: indeed, for every $s \in S$, there
is an open neighbourhood $W$ of $s$ in $S$ such that $g(W)$ is closed in an open set $U$ of $X$, and it is clear that
$g|W$ is a $W$-section of the morphism $U \cap f^{-1}(W) \to W$, restriction of $f$, and $g(W)$ is *a fortiori* closed
in $U \cap f^{-1}(W)$. One can therefore suppose that $S$ is a closed sub-prescheme of $X$ defined by a quasi-coherent
Ideal $\mathcal{K}$. The preceding definitions show that if $W$ is an open of $S$ and $t$ is a section of
$\mathcal{O}_{X}$ over $f^{-1}(W)$, $\varpi_{n}(d^{n}_{X/S} t|W)$ is equal to the canonical image of $t$ in $\Gamma(W,
(\mathcal{O}_{X}/\mathcal{K}^{n+1})|W)$. The uniqueness of $\varpi_{n}$ then follows since the image of
$\mathcal{O}_{X}$ under $d^{n}_{X/S}$ generates the $\mathcal{O}_{X}$-Module $\mathcal{P}^{n}_{X/S}$ `(16.3.8)`.

**Corollary (16.4.12).**

<!-- label: IV.16.4.12 -->

*Let $k$ be a field, $X$ a $k$-prescheme, $x$ a point of $X$ rational over $k$. Then $(\mathcal{P}^{n}_{X/k})_{x}
\otimes_{\mathcal{O}_{x}} k(x)$ is canonically isomorphic (as an augmented $k(x)$-algebra) to
$\mathcal{O}_{x}/\mathfrak{m}^{n+1}_{x}$.*

It suffices to consider the unique $k$-section $g$ of $X$ such that $g(\operatorname{Spec}(k)) = {x}$.

**Corollary (16.4.13).**

<!-- label: IV.16.4.13 -->

*Let $f : X \to S$ be a morphism, $s$ a point of $S$, $X_{s} = X \times_{S} \operatorname{Spec}(k(s))$ the fibre of $f$
at $s$. If $x \in X_{s}$ is rational over $k(s)$, $(\mathcal{P}^{n}_{X/S})_{x} \otimes_{\mathcal{O}_{s}} k(s)$ is
canonically isomorphic to $\mathcal{O}_{X_{s}, x}/\mathfrak{m}'^{n+1}_{x}$, where $\mathfrak{m}'_{x}$ is the maximal
ideal of $\mathcal{O}_{X_{s}, x}$; more precisely, this isomorphism sends $(d^{n} t)_{x} \otimes 1$ (where $t$ is a
section of $\mathcal{O}_{X}$ over an open neighbourhood of $x$ in $X$) to the class of $t_{x} \otimes 1$ modulo
$\mathfrak{m}'^{n+1}_{x}$.*

This follows from `(16.4.5)` and `(16.4.12)`.

The preceding corollaries justify the terminology "sheaf of principal parts of order $n$".

**Proposition (16.4.14).**

<!-- label: IV.16.4.14 -->

*Let $\rho : A \to B$ be a ring homomorphism, $S$ a multiplicatively stable subset of $B$. Then the canonical
homomorphisms*

$$ (16.4.14.1) S^{-1} P^{n}_{B/A} \to P^{n}_{S^{-1}B/A} $$

<!-- original page 23 -->

*deduced from the canonical homomorphisms $P^{n}_{B/A} \to P^{n}_{S^{-1}B/A}$ `(16.4.4)` form a projective system and
are bijective.*

It suffices to remark that $S^{-1}((B \otimes_{A} B)/\mathfrak{J}^{n+1}) = S^{-1}(B \otimes_{A}
B)/(S^{-1}\mathfrak{J})^{n+1}$ by flatness, and that $S^{-1}(B \otimes_{A} B) = (S^{-1}B) \otimes_{A} (S^{-1}B)$
`(I, 1.3.4)`.

**Corollary (16.4.15).**

<!-- label: IV.16.4.15 -->

*With the notation of `(16.4.14)`, let $R$ be a multiplicative subset of $A$ such that $\rho(R) \subset S$. Then one has
canonical isomorphisms*

$$ (16.4.15.1) S^{-1} P^{n}_{B/A} \xrightarrow{\sim} P^{n}_{S^{-1}B/R^{-1}A} $$

*forming a projective system.*

It evidently suffices to define canonical isomorphisms

$$ (16.4.15.2) P^{n}_{S^{-1}B/A} \xrightarrow{\sim} P^{n}_{S^{-1}B/R^{-1}A} $$

that is to say, one is reduced to the case where $\rho(R)$ is made up of invertible elements of $B$. But then the
isomorphism `(16.4.15.2)` is simply deduced from the canonical isomorphism $B \otimes_{A} B \to B \otimes_{R^{-1}A} B$
by passage to the quotients $(0_{I}, 1.5.3)$.

**Corollary (16.4.16).**

<!-- label: IV.16.4.16 -->

*Let $f : X \to S$ be a morphism of preschemes, $x$ a point of $X$, $s = f(x)$. Then one has canonical isomorphisms*

$$ (16.4.16.1) (\mathcal{P}^{n}_{X/S})_{x} \xrightarrow{\sim} P^{n}_{\mathcal{O}_{x}/\mathcal{O}_{s}} $$

*forming a projective system.*

One deduces isomorphisms for the associated graded rings, and in particular a canonical isomorphism

$$ (16.4.16.2) (\Omega^{1}_{X/S})_{x} \xrightarrow{\sim} \Omega^{1}_{\mathcal{O}_{x}/\mathcal{O}_{s}}. $$

**Corollary (16.4.17).**

<!-- label: IV.16.4.17 -->

*Let $k$ be a field, $K$ the field of rational functions $k(T_{1}, \cdots, T_{r})$. Then, for every integer $n$, the
homomorphism of $K[U_{1}, \cdots, U_{r}]$ ($U_{i}$ indeterminates) into $P^{n}_{K/k}$ which sends every $U_{i}$ to
$d^{n} T_{i} - T_{i} \cdot 1$ is surjective and defines an isomorphism of the quotient $K[U_{1}, \cdots,
U_{r}]/\mathfrak{m}^{n+1}$ (where $\mathfrak{m}$ is the ideal generated by the $U_{i}$) onto $P^{n}_{K/k}$.*

This follows from `(16.4.8)`, `(16.4.10)` and `(16.4.14)`, where one takes $A = k$, $B = k[T_{1}, \cdots, T_{r}]$ and $S
= B - {0}$.

One thus recovers the fact that the $dT_{i}$ form a basis of the $K$-vector space $\Omega^{1}_{K/k}$ `(0, 20.5.10)`.

**Proposition (16.4.18).**

<!-- label: IV.16.4.18 -->

*Let $f : X \to Y$, $g : Y \to Z$ be two morphisms of preschemes, and consider the canonical homomorphisms of augmented
$\mathcal{O}_{X}$-Algebras `(16.4.3.3)`*

$$ (16.4.18.1) g_{X/Y/Z} : \mathcal{P}^{n}_{X/Z} \to \mathcal{P}^{n}_{X/Y} $$

$$ (16.4.18.2) f_{X/Y/Z} : f*(\mathcal{P}^{n}_{Y/Z}) \to \mathcal{P}^{n}_{X/Z}. $$

*Then $g_{X/Y/Z}$ is surjective, and its kernel is the Ideal generated by the image under $f_{X/Y/Z}$ of the
augmentation ideal of $f*(\mathcal{P}^{n}_{Y/Z})$.*

<!-- original page 24 -->

Note first that $g_{X/Y/Z}$ corresponds to the case in `(16.4.3.3)` where $X' = X$, $S' = Y$, $S = Z$, $u = 1_{X}$, and
$f_{X/Y/Z}$ to the case where one replaces $X'$, $X$, $S$, $S'$ by $X$, $Y$, $Z$, $Z$ respectively and $u$, $f$ by $f$,
$g$ respectively.

One has a commutative diagram `(I, 5.3.5)`

```text
  (16.4.18.3)
              X   ──Δ_f──> X ×_Y X  ──j──> X ×_Z X
                ╲             │              │
                f ╲           p              f ×_Z f
                  ↘           ↓              ↓
                              Y  ──Δ_g──>  Y ×_Z Y
```

where $j = (1_{X}, 1_{X})_{Z}$ is an immersion, $j \circ \Delta_{f} = \Delta_{g \circ f}$, and $p$ is the structure
morphism. Since one can restrict to the case where $X$, $Y$, $Z$ are affine, one can suppose the immersions
$\Delta_{f}$, $\Delta_{g}$ and $j$ to be closed, so that $\mathcal{O}_{X}$ and $\mathcal{O}_{X \times_{Y} X}$ are
identified respectively with $\mathcal{O}_{X \times_{Z} X}/\mathcal{I}$ and $\mathcal{O}_{X \times_{Z} X}/\mathcal{L}$,
where $\mathcal{L} \supset \mathcal{I}$ are two quasi-coherent Ideals corresponding respectively to the immersions
$\Delta_{g \circ f}$ and $j$. The $\mathcal{O}_{X}$-Algebra $\mathcal{P}^{n}_{X/Z}$ is therefore identified with
$\mathcal{O}_{X \times_{Z} X}/\mathcal{I}^{n+1}$, and $\mathcal{P}^{n}_{X/Y}$ is identified with $\mathcal{O}_{X
\times_{Y} X}/(\mathcal{I}/\mathcal{L})^{n+1}$, that is to say with $\mathcal{O}_{X \times_{Z} X}/(\mathcal{I}^{n+1} +
\mathcal{L})$, and consequently with the quotient of $\mathcal{P}^{n}_{X/Z}$ by $(\mathcal{I}^{n+1} +
\mathcal{L})/\mathcal{I}^{n+1}$. But one knows (*loc. cit.*) that $p$ and $j$ make $X \times_{Y} X$ the product of the
$(Y \times_{Z} Y)$-preschemes $Y$ and $X \times_{Z} X$, so if $\mathcal{O}_{Y}$ is identified with $\mathcal{O}_{Y
\times_{Z} Y}/\mathcal{K}$, where $\mathcal{K}$ is the Ideal corresponding to $\Delta_{g}$, then $\mathcal{L}$ is equal
to $(f \times_{Z} f)*(\mathcal{K}) \cdot \mathcal{O}_{X \times_{Z} X}$ `(I, 4.4.5)`. Since $(\mathcal{I}^{n+1} +
\mathcal{L})/\mathcal{I}^{n+1}$ is the Ideal of $\mathcal{P}^{n}_{X/Z}$ generated by the image of $\mathcal{L}$, the
proposition follows.

**Corollary (16.4.19).**

<!-- label: IV.16.4.19 -->

*With the notation of `(16.4.18)`, one has an exact sequence of quasi-coherent $\mathcal{O}_{X}$-Modules*

```text
  (16.4.19.1)    f*(Ω_{Y/Z}^1) ──f_{X/Y/Z}──> Ω_{X/Z}^1 ──g_{X/Y/Z}──> Ω_{X/Y}^1 → 0.
```

When $X$, $Y$, $Z$ are affine, one thus recovers the exact sequence `(0, 20.5.7.1)`.

**Proposition (16.4.20).**

<!-- label: IV.16.4.20 -->

*Let $f : Y \to Z$ be a morphism, $j : X \to Y$ a closed immersion, $\mathcal{K}$ the quasi-coherent Ideal of
$\mathcal{O}_{Y}$ corresponding to $j$. Then one has $\mathcal{P}^{n}_{X/Y} = \mathcal{O}_{X} =
\mathcal{O}_{Y}/\mathcal{K}$, the canonical homomorphism $j_{X/Y/Z} : j*(\mathcal{P}^{n}_{Y/Z}) \to
\mathcal{P}^{n}_{X/Z}$ is surjective, and its kernel is the Ideal of $j*(\mathcal{P}^{n}_{Y/Z})$ generated by
$j*(\mathcal{O}_{Y} \cdot d^{n}_{Y/Z}(\mathcal{K}))$ (note that $d^{n}_{Y/Z}(\mathcal{K})$ is a subsheaf of abelian
groups of $\mathcal{P}^{n}_{Y/Z}$, but is not an $\mathcal{O}_{Y}$-Module in general).*

One knows `(I, 5.3.8)` that the diagonal $\Delta_{j} : X \to X \times_{Y} X$ is an isomorphism, whence the first
assertion. If $\varpi_{1}$ and $\varpi_{2}$ are the two homomorphisms of Algebras $\mathcal{O}_{Y} \to
\mathcal{P}^{n}_{Y/Z}$ corresponding respectively to the two canonical projections $p_{1}$, $p_{2}$ of $Y \times_{Z} Y$
onto $Y$, recall that by definition `(16.3.5` and `16.3.6)` $\varpi_{1}$ is the structural homomorphism of the
$\mathcal{O}_{Y}$-Algebra $\mathcal{P}^{n}_{Y/Z}$ and $\varpi_{2} = d^{n}_{Y/Z}$. The $\mathcal{O}_{X}$-Algebra
$j*(\mathcal{P}^{n}_{Y/Z})$ is therefore identified with $\mathcal{P}^{n}_{Y/Z}/\varpi_{1}(\mathcal{K})
\mathcal{P}^{n}_{Y/Z}$, and its quotient by the Ideal generated by $j*(d^{n}_{Y/Z}(\mathcal{K}))$ with
$\mathcal{P}^{n}_{Y/Z}/(\varpi_{1}(\mathcal{K}) + \varpi_{2}(\mathcal{K})) \mathcal{P}^{n}_{Y/Z}$. Now note that one has
a commutative diagram

<!-- original page 25 -->

```text
              Y  <──j──   X
              │           │
              Δ_f         Δ_{f ∘ j}
              ↓           ↓
           Y ×_Z Y <─j ×_Z j── X ×_Z X
```

identifying $X$ with the product of the $(Y \times_{Z} Y)$-preschemes $Y$ and $X \times_{Z} X$ `(I, 5.3.7)`. Since $j
\times_{Z} j$ is an immersion, one deduces from this remark and from `(16.2.2)` that if $\Delta^{n}_{Y/Z}$ and
$\Delta^{n}_{X/Z}$ denote the infinitesimal neighbourhoods of order $n$ of $Y$ and $X$ for the canonical immersions
$\Delta_{f}$ and $\Delta_{f \circ j}$ respectively, one has a diagram

```text
              Δ_{Y/Z}^n   <───   Δ_{X/Z}^n
                  │                  │
                  ↓                  ↓
               Y ×_Z Y <─j ×_Z j── X ×_Z X
```

making $\Delta^{n}_{X/Z}$ the product of the $(Y \times_{Z} Y)$-preschemes $\Delta^{n}_{Y/Z}$ and $X \times_{Z} X$. One
can also say that $\mathcal{P}^{n}_{X/Z}$ is identified with the sheaf of rings $\mathcal{P}^{n}_{Y/Z}
\otimes_{\mathcal{O}_{Y \times_{Z} Y}} \mathcal{O}_{X \times_{Z} X}$. But one sees at once (for example by reducing to
the affine case) that $\mathcal{O}_{X \times_{Z} X} = \mathcal{O}_{Y \times_{Z} Y}/(p_{1}*(\mathcal{K}) +
p_{2}*(\mathcal{K})) \mathcal{O}_{Y \times_{Z} Y}$. Therefore $\mathcal{P}^{n}_{X/Z}$ is identified with the quotient of
$\mathcal{P}^{n}_{Y/Z}$ by the Ideal generated by the image in $\mathcal{P}^{n}_{Y/Z}$ of $p_{1}*(\mathcal{K}) +
p_{2}*(\mathcal{K})$. But by definition this Ideal is also generated by $\varpi_{1}(\mathcal{K}) +
\varpi_{2}(\mathcal{K})$. Q.E.D.

**Corollary (16.4.21).**

<!-- label: IV.16.4.21 -->

*Let $f : Y \to Z$ be a morphism, $j : X \to Y$ an immersion. One has an exact sequence of quasi-coherent
$\mathcal{O}_{X}$-Modules*

$$ (16.4.21.1) \mathcal{N}_{X/Y} \to j*(\Omega^{1}_{Y/Z}) \to \Omega^{1}_{X/Z} \to 0. $$

When $X$, $Y$, $Z$ are affine, one thus recovers the exact sequence `(0, 20.5.12.1)`.

**Corollary (16.4.22).**

<!-- label: IV.16.4.22 -->

*If $f : X \to S$ is a morphism locally of finite presentation, $\mathcal{P}^{n}_{X/S}$ and $\Omega^{1}_{X/S}$ are
quasi-coherent $\mathcal{O}_{X}$-Modules of finite presentation.*

One is at once reduced to the case where $S = \operatorname{Spec}(A)$ is affine, $X = \operatorname{Spec}(B)$, where $B
= A[T_{1}, \cdots, T_{r}]/\mathfrak{K}$, with $\mathfrak{K}$ an ideal of finite type of $C = A[T_{1}, \cdots, T_{r}]$.
One then applies `(16.4.20)` with $Z = S$, $Y = \operatorname{Spec}(C)$ and $\mathcal{K} = \tilde{\mathfrak{K}}$. Then
$j*(\mathcal{P}^{n}_{Y/Z})$ is a free $\mathcal{O}_{X}$-Module of finite rank `(16.4.10)`, and the hypothesis on
$\mathfrak{K}$ implies that $j*(\mathcal{O}_{Y} \cdot d^{n}_{Y/Z}(\mathcal{K}))$ generates a quasi-coherent
$\mathcal{O}_{X}$-Module of finite type; whence the conclusion.

**Proposition (16.4.23).**

<!-- label: IV.16.4.23 -->

*Let $X$, $Y$ be two $S$-preschemes, $Z = X \times_{S} Y$ their product, $p : X \times_{S} Y \to X$ and $q : X
\times_{S} Y \to Y$ the canonical projections. Then the canonical homomorphism*

```text
  (16.4.23.1)    p_{Z/X/S} ⊕ q_{Z/Y/S} : p*(Ω_{X/S}^1) ⊕ q*(Ω_{Y/S}^1) → Ω_{(X ×_S Y)/S}^1
```

*is bijective.*

<!-- original page 26 -->

The commutative diagram

```text
              Y  <──q──  X ×_S Y  <──id──  X ×_S Y
              │            │                  │
              g            h                  p
              ↓            ↓                  ↓
              S  <──id──    S    <───f───    X
```

gives a factorisation of the canonical isomorphism $P^{n}(p)$ `(16.4.5)`

$$ p*(\mathcal{P}^{n}_{X/S}) \to \mathcal{P}^{n}_{Z/S} \to \mathcal{P}^{n}_{Z/Y} $$

and similarly, by interchanging the roles of $X$ and $Y$, one has a factorisation of the isomorphism $P^{n}(q)$

$$ q*(\mathcal{P}^{n}_{Y/S}) \to \mathcal{P}^{n}_{Z/S} \to \mathcal{P}^{n}_{Z/X}. $$

This proves that the canonical homomorphism `(16.4.18.1)`

```text
  p_{Z/X/S} : p*(𝒫_{X/S}^n) → 𝒫_{Z/S}^n   (resp. q_{Z/Y/S} : q*(𝒫_{Y/S}^n) → 𝒫_{Z/S}^n)
```

is injective, and that the kernel of the canonical surjective homomorphism `(16.4.18.2)`

```text
  𝒫_{Z/S}^n → 𝒫_{Z/Y}^n   (resp. 𝒫_{Z/S}^n → 𝒫_{Z/X}^n)
```

is a complement of the image of $p_{Z/X/S}$ (resp. $q_{Z/Y/S}$). On the other hand, this kernel is, by virtue of
`(16.4.18)`, generated by the image under $q_{Z/Y/S}$ (resp. $p_{Z/X/S}$) of the augmentation ideal of
$q*(\mathcal{P}^{n}_{Y/S})$ (resp. $p*(\mathcal{P}^{n}_{X/S})$). One concludes the proposition by considering the case
$n = 1$.

One generalizes `(16.4.23)` at once to the case of a product of an arbitrary finite number of $S$-preschemes.

**Remarks (16.4.24).**

<!-- label: IV.16.4.24 -->

(i) We shall see `(17.2.3)` that when the morphism $f : X \to Y$ in `(16.4.18)` is smooth, the homomorphism $f_{X/Y/Z}$
in `(16.4.19.1)` is locally left invertible and in particular injective. Likewise, when the morphism $f \circ j : X \to
Z$ of `(16.4.20)` is smooth, the homomorphism on the left in `(16.4.21.1)` is locally left invertible and *a fortiori*
injective `(17.2.5)`. In Chapter V, we shall also give a variant, in the case of Modules over preschemes, of the
"imperfection modules" studied in `(0, 20.6)`, and of the exact sequences in which they appear.

(ii) Let $X$ be a topological space, $\mathcal{A}$ a sheaf of rings on $X$, and $\mathcal{B}$ an $\mathcal{A}$-Algebra
on $X$. Then it is clear that

```text
  U ↦ P_{Γ(U, ℬ)/Γ(U, 𝒜)}^n   (U open in X)
```

is a presheaf of augmented $\Gamma(U, \mathcal{B})$-algebras, so the associated sheaf
$\mathcal{P}^{n}_{\mathcal{B}/\mathcal{A}}$ is an augmented $\mathcal{B}$-Algebra. In the particular case where $X$ is a
prescheme and $f = (\psi, \theta) : X \to S$ is a morphism of preschemes, it follows easily from `(16.4.16)` and from
the exactness of the functor $\lim\to$ that $\mathcal{P}^{n}_{X/S}$ is canonically isomorphic to
$\mathcal{P}^{n}_{\mathcal{O}_{X}/\psi*(\mathcal{O}_{S})}$. It follows that the formalism developed in the present
section could be regarded as a

<!-- original page 27 -->

particular case of a differential formalism for ringed spaces endowed with a sheaf of algebras over the structure sheaf.
We did not, however, wish to start from this point of view, which is less intuitive and less convenient for
applications. It seems, moreover, that, for the various species of "varieties", the "global" construction of the
$\mathcal{P}^{n}$ analogous to the one we use here is also better suited to applications.

### 16.5. Relative tangent sheaves and bundles; derivations

**(16.5.1).**

<!-- label: IV.16.5.1 -->

Let $f = (\psi, \theta) : X \to S$ be a morphism of ringed spaces. For every $\mathcal{O}_{X}$-Module $\mathcal{F}$, an
**$S$-derivation** (or **$(X/S)$-derivation**, or **$f$-derivation**) **of $\mathcal{O}_{X}$ into $\mathcal{F}$** is by
definition any homomorphism of sheaves of additive groups $D : \mathcal{O}_{X} \to \mathcal{F}$ satisfying the following
conditions:

a) for every open $V$ of $X$ and every pair of sections $(t_{1}, t_{2})$ of $\mathcal{O}_{X}$ over $V$, one has

```text
  (16.5.1.1)    D(t_1 t_2) = t_1 D(t_2) + D(t_1) t_2;
```

b) for every open $V$ of $X$, every section $t$ of $\mathcal{O}_{X}$ over $V$, and every section $s$ of
$\mathcal{O}_{S}$ over an open $U$ of $S$ such that $V \subset f^{-1}(U)$, one has

```text
  (16.5.1.2)    D((s|V) t) = (s|V) D(t).
```

It is clear that this amounts to saying that for every $x \in X$, the homomorphism of additive groups $D_{x} :
\mathcal{O}_{x} \to \mathcal{F}_{x}$ is an $\mathcal{O}_{f(x)}$-derivation.

Another interpretation consists in considering the $\mathcal{O}_{X}$-Algebra
$\mathcal{D}_{\mathcal{O}_{X}}(\mathcal{F})$ equal to $\mathcal{O}_{X} \oplus \mathcal{F}$, the algebra structure being
defined by the requirement that for every open $V$ of $X$, the product of two sections of $\mathcal{O}_{X}$ (resp. of a
section of $\mathcal{O}_{X}$ and a section of $\mathcal{F}$) over $V$ is defined by the ring structure of $\Gamma(V,
\mathcal{O}_{X})$ (resp. the $\Gamma(V, \mathcal{O}_{X})$-module structure on $\Gamma(V, \mathcal{F})$), and the product
of two sections of $\mathcal{F}$ over $V$ is taken to be zero. Then $\mathcal{F}$ is an Ideal of
$\mathcal{D}_{\mathcal{O}_{X}}(\mathcal{F})$, kernel of the canonical augmentation
$\mathcal{D}_{\mathcal{O}_{X}}(\mathcal{F}) \to \mathcal{O}_{X}$, and to say that $D$ is an $S$-derivation of
$\mathcal{O}_{X}$ into $\mathcal{F}$ means that $1_{\mathcal{O}_{X}} + D$ is an $\mathcal{O}_{S}$-homomorphism of
Algebras from $\mathcal{O}_{X}$ into $\mathcal{D}_{\mathcal{O}_{X}}(\mathcal{F})$ which, composed with the augmentation,
gives $1_{\mathcal{O}_{X}}$.

The $S$-derivations of $\mathcal{O}_{X}$ into $\mathcal{F}$ obviously form a $\Gamma(X, \mathcal{O}_{X})$-module
$\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{F})$.

When $\mathcal{F} = \mathcal{O}_{X}$, an $S$-derivation of $\mathcal{O}_{X}$ into itself is simply called an
**$S$-derivation of $\mathcal{O}_{X}$**.

**Proposition (16.5.2).**

<!-- label: IV.16.5.2 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $L$ a $B$-module; set $S = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$, $\mathcal{F} = \tilde{L}$. Then the map $D \mapsto \Gamma(D)$ which, to every $S$-derivation
$D$ of $\mathcal{O}_{X}$ into $\mathcal{F}$, assigns the map $\Gamma(D) : t \mapsto D(t)$ of $B$ into $L$, is an
isomorphism of $B$-modules from $\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{F})$ onto $\operatorname{Der}_{A}(B,
L)$ (cf. `(0, 20.1.2)`).*

This follows at once from the interpretation given above of $S$-derivations in terms

<!-- original page 28 -->

of homomorphisms of Algebras, from the analogous interpretation given in `(0, 20.1.6)`, and from the canonical
correspondence between homomorphisms of $\mathcal{O}_{X}$-Algebras and homomorphisms of $B$-algebras `(I, 1.3.13` and
`1.3.8)`.

**Proposition (16.5.3).**

<!-- label: IV.16.5.3 -->

*Let $f = (\psi, \theta) : X \to S$ be a morphism of preschemes.*

*(i) The differential $d_{X/S} : \mathcal{O}_{X} \to \Omega^{1}_{X/S}$ `(16.3.6)` is an $S$-derivation.*

*(ii) For every $\mathcal{O}_{X}$-Module $\mathcal{F}$, the map $u \mapsto u \circ d_{X/S}$ is an isomorphism of
$\Gamma(X, \mathcal{O}_{X})$-modules*

```text
  (16.5.3.1)    Hom_{𝒪_X}(Ω_{X/S}^1, ℱ) ⥲ Der_S(𝒪_X, ℱ).
```

Assertion (i) has already been noted `(16.3.6)`. On the other hand, it is immediate (by virtue of `(0, 20.4.8)`) that $u
\mapsto u \circ d_{X/S}$ is injective, by considering the restrictions to a fibre $\mathcal{O}_{x}$ of both sides and
using `(16.4.16.2)`. To see that the homomorphism `(16.5.3.1)` is surjective, consider an $S$-derivation $D :
\mathcal{O}_{X} \to \mathcal{F}$; for every affine open $V = \operatorname{Spec}(B)$ of $X$ such that $f(V)$ is
contained in an affine open $U = \operatorname{Spec}(A)$ of $S$, $D_{V} : B \to \Gamma(V, \mathcal{F})$ is an
$A$-derivation, so there exists a unique $B$-homomorphism $u_{V} : \Omega^{1}_{B/A} \to \Gamma(V, \mathcal{F})$ such
that $D_{V} = u_{V} \circ d_{B/A}$ `(0, 20.4.8)`; furthermore, the uniqueness of $u_{V}$ shows at once that for every
affine open $W \subset V$, one has $u_{W} = u_{V}|W$, so the $u_{V}$ define a homomorphism of $\mathcal{O}_{X}$-Modules
$u : \Omega^{1}_{X/S} \to \mathcal{F}$ answering the question.

**(16.5.4).**

<!-- label: IV.16.5.4 -->

With the notation of `(16.5.1)`, for every open $U$ of $X$, $\operatorname{Der}_{S}(\mathcal{O}_{U}, \mathcal{F}|U)$ is
a $\Gamma(U, \mathcal{O}_{X})$-module, and it is clear that the map $U \mapsto \operatorname{Der}_{S}(\mathcal{O}_{U},
\mathcal{F}|U)$ is a presheaf; in fact, it is even a sheaf (hence an $\mathcal{O}_{X}$-Module), by virtue of the
pointwise characterization of $S$-derivations seen in `(16.5.1)`. This $\mathcal{O}_{X}$-Module is denoted by
$\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{F})$ and is called the **sheaf of $S$-derivations of $\mathcal{O}_{X}$
into $\mathcal{F}$**, and what one has just seen is also expressed by the following corollary:

**Corollary (16.5.5).**

<!-- label: IV.16.5.5 -->

*For every $\mathcal{O}_{X}$-Module $\mathcal{F}$, the homomorphism of $\mathcal{O}_{X}$-Modules deduced from $u \mapsto
u \circ d_{X/S}$*

```text
  (16.5.5.1)    ℋℴ𝓂_{𝒪_X}(Ω_{X/S}^1, ℱ) → 𝒟ℯ𝓇_S(𝒪_X, ℱ)
```

*is bijective.*

**Corollary (16.5.6).**

<!-- label: IV.16.5.6 -->

*(i) If the morphism $f : X \to S$ is locally of finite presentation and $\mathcal{F}$ is a quasi-coherent
$\mathcal{O}_{X}$-Module, then $\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{F})$ is a quasi-coherent
$\mathcal{O}_{X}$-Module.*

*(ii) If, in addition, $S$ is locally Noetherian and $\mathcal{F}$ is coherent, then
$\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{F})$ is a coherent $\mathcal{O}_{X}$-Module.*

Assertion (i) follows from the isomorphism `(16.5.5.1)`, from `(16.4.22)`, and from `(I, 1.3.12)`; assertion (ii)
follows from $(0_{I}, 5.3.5)$.

**(16.5.7).**

<!-- label: IV.16.5.7 -->

One sets

```text
  (16.5.7.1)    𝒯_{X/S} = ℋℴ𝓂_{𝒪_X}(Ω_{X/S}^1, 𝒪_X) = 𝒟ℯ𝓇_S(𝒪_X, 𝒪_X)
```

and one says that this is the **sheaf of $S$-derivations of $\mathcal{O}_{X}$**, or also the **tangent sheaf of $X$
relative to $S$**: it is therefore the dual of the $\mathcal{O}_{X}$-Module $\Omega^{1}_{X/S}$. If $f$ is locally of
finite presentation,

<!-- original page 29 -->

$\mathcal{T}_{X/S}$ is a quasi-coherent $\mathcal{O}_{X}$-Module; if in addition $S$ is locally Noetherian,
$\mathcal{T}_{X/S}$ is coherent `(16.5.6)`.

**(16.5.8).**

<!-- label: IV.16.5.8 -->

Suppose more particularly that $\Omega^{1}_{X/S}$ is a locally free $\mathcal{O}_{X}$-Module (of finite rank) (which
will be the case when $f$ is smooth `(17.2.3)`); then $\mathcal{T}_{X/S}$ is a locally free $\mathcal{O}_{X}$-Module, of
the same rank as $\Omega^{1}_{X/S}$ at each point. More precisely, suppose that $\Omega^{1}_{X/S}$ is of rank $n$ at a
point $x$; then there are $n$ sections $s_{i}$ ($1 \leqslant i \leqslant n$) of $\mathcal{O}_{X}$ over an affine
neighbourhood $U$ of $x$ such that the canonical images of the $ds_{i}$ in $\Omega^{1}_{X/S} \otimes_{\mathcal{O}_{x}}
k(x)$ form a basis of this $k(x)$-vector space; by virtue of Nakayama's lemma, the germs $(ds_{i})_{x} = d(s_{i})_{x}$
of the $ds_{i}$ at the point $x$ form a basis of the $\mathcal{O}_{x}$-module $(\Omega^{1}_{X/S})_{x}$, so by
restricting $U$ one can suppose that the $ds_{i}$ form a basis of the $\Gamma(U, \mathcal{O}_{X})$-module $\Gamma(U,
\Omega^{1}_{X/S})$. Then the $\Gamma(U, \mathcal{O}_{X})$-module $\Gamma(U, \mathcal{T}_{X/S})$ is dual to the preceding
one; one denotes by $(D_{i})_{1 \leqslant i \leqslant n}$ or $(\partial/\partial s_{i})_{1 \leqslant i \leqslant n}$ the
dual basis of $(ds_{i})_{1 \leqslant i \leqslant n}$, so that, by `(16.5.3)`, one has

```text
  (16.5.8.1)    D_i s_j = ⟨D_i, ds_j⟩ = ⟨∂/∂s_i, ds_j⟩ = δ_{ij}   (Kronecker symbol).
```

Every $\Gamma(S, \mathcal{O}_{S})$-derivation of the $\Gamma(S, \mathcal{O}_{S})$-algebra $\Gamma(U, \mathcal{O}_{X})$
is therefore written in one and only one way as

```text
  D = ∑_{i=1}^n a_i D_i = ∑_{i=1}^n a_i (∂/∂s_i),
```

where the $a_{i}$ ($1 \leqslant i \leqslant n$) are sections of $\mathcal{O}_{X}$ over $U$. For every section $g \in
\Gamma(U, \mathcal{O}_{X})$, if one sets $dg = \sum^{n}_{i=1} c_{i} ds_{i}$, one has $c_{i} = \langle D_{i}, dg\rangle =
D_{i} g$ by virtue of `(16.5.8.1)`, in other words

```text
  (16.5.8.2)    dg = ∑_{i=1}^n (D_i g) ds_i = ∑_{i=1}^n (∂g/∂s_i) ds_i.
```

**(16.5.9).**

<!-- label: IV.16.5.9 -->

Let `D_1`, `D_2` be two $S$-derivations of $\mathcal{O}_{X}$. For every open $U$ of $X$, if $D^{U}_{1}$, $D^{U}_{2}$ are
the corresponding derivations of the ring $\Gamma(U, \mathcal{O}_{X})$, the **bracket**

```text
  [D_1^U, D_2^U] = D_1^U ∘ D_2^U - D_2^U ∘ D_1^U
```

is also a derivation of this ring, so the $\psi*(\mathcal{O}_{S})$-endomorphism of $\mathcal{O}_{X}$

```text
  (16.5.9.1)    [D_1, D_2] = D_1 ∘ D_2 - D_2 ∘ D_1
```

is again an $S$-derivation; as one checks at once that this bracket satisfies the Jacobi identity, one sees that one has
thus defined on $\operatorname{Der}_{S}(\mathcal{O}_{X}, \mathcal{O}_{X})$ a $\Gamma(S, \mathcal{O}_{S})$-Lie-algebra
structure. Since the definition of this structure commutes with restriction to an open subset of $X$, one sees that
$\mathcal{T}_{X/S}$ is canonically endowed with a $\psi*(\mathcal{O}_{S})$-Lie-algebra structure. Note that the map
$(D_{1}, D_{2}) \mapsto [D_{1}, D_{2}]$ is *not* $\Gamma(X, \mathcal{O}_{X})$-bilinear.

**(16.5.10).**

<!-- label: IV.16.5.10 -->

For every base change $g : S' \to S$, if one sets $X' = X \times_{S} S'$, one has seen `(16.4.5)` that one has a
canonical isomorphism

```text
  (16.5.10.1)    Ω_{X/S}^1 ⊗_{𝒪_S} 𝒪_{S'} ⥲ Ω_{X'/S'}^1
```

<!-- original page 30 -->

from which one deduces, by virtue of `(16.5.10.1)`, a canonical homomorphism (Bourbaki, *Alg.*, chap. II, 3rd ed., §5,
n° 3)

```text
  (16.5.10.2)    𝒯_{X/S} ⊗_{𝒪_S} 𝒪_{S'} → 𝒯_{X'/S'}
```

which is in general neither injective nor surjective. However:

**Proposition (16.5.11).**

<!-- label: IV.16.5.11 -->

*(i) If $g : S' \to S$ is a flat morphism and $f$ is locally of finite type (resp. locally of finite presentation), the
homomorphism `(16.5.10.2)` is injective (resp. bijective).*

*(ii) If $\Omega^{1}_{X/S}$ is a locally free $\mathcal{O}_{X}$-Module of finite type, the homomorphism `(16.5.10.2)` is
bijective.*

Indeed, assertion (ii) follows from Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 3, prop. 7. Assertion (i) follows
similarly from Bourbaki, *Alg. comm.*, chap. I, §2, n° 10, prop. 11 and from the fact that if $f$ is locally of finite
type (resp. locally of finite presentation), $\Omega^{1}_{X/S}$ is an $\mathcal{O}_{X}$-Module of finite type (resp. of
finite presentation) (`(16.3.9)` and `(16.4.22)`).

**(16.5.12).**

<!-- label: IV.16.5.12 -->

Since $\Omega^{1}_{X/S}$ is a quasi-coherent $\mathcal{O}_{X}$-Module, one can consider the vector bundle over $X$
defined by $\Omega^{1}_{X/S}$ `(II, 1.7.8)`

$$ (16.5.12.1) T_{X/S} = \mathbf{V}(\Omega^{1}_{X/S}) $$

which is called the **tangent bundle of $X$ relative to $S$**. One has therefore a canonical bijection `(II, 1.7.9)`

```text
  Γ(T_{X/S}/S) ⥲ Hom_{𝒪_X}(Ω_{X/S}^1, 𝒪_X) = Γ(X, 𝒯_{X/S})
```

by definition of $\mathcal{T}_{X/S}$, and in this isomorphism one can replace $X$ by an arbitrary open $U$ of $X$; one
can therefore say that the tangent sheaf of $X$ relative to $S$ is isomorphic to the sheaf of germs of $S$-sections of
the tangent bundle of $X$ relative to $S$. If $f : X \to Y$ is an $S$-morphism, one has seen `(16.4.19)` that one has a
canonical homomorphism $f_{X/Y/S} : f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}$; this gives, taking into account that

```text
  𝐕(f*(Ω_{Y/S}^1)) = 𝐕(Ω_{Y/S}^1) ×_Y X   (II, 1.7.11),
```

an $X$-morphism $T_{X/S}(f) : T_{X/S} \to T_{Y/S} \times_{Y} X$. If $g : Y \to Z$ is a second $S$-morphism, one has
$T_{X/S}(g \circ f) = (T_{Y/S}(g) \times 1_{X}) \circ T_{X/S}(f)$ `(0, 20.5.4.1)`.

It follows from `(16.5.10.1)` and from `(II, 1.7.11)` that for every base change $g : S' \to S$, one has a canonical
isomorphism

```text
  (16.5.12.2)    T_{X'/S'} ⥲ T_{X/S} ×_S S' = T_{X/S} ×_X X'.
```

**(16.5.13).**

<!-- label: IV.16.5.13 -->

For every point $x \in X$, one calls the **tangent space to $X$ at the point $x$** (relative to $S$) the set of points
of the fibre $T_{X/S} \times_{X} \operatorname{Spec}(k(x))$ rational over $k(x)$, that is to say the set

```text
  (16.5.13.1)    T_{X/S}(x) = Hom_{k(x)}(Ω_{X/S}^1 ⊗_{𝒪_x} k(x), k(x))
```

which is the dual of the $k(x)$-vector space $\Omega^{1}_{\mathcal{O}_{x}/\mathcal{O}_{s}}/\mathfrak{m}_{x} \cdot
\Omega^{1}_{\mathcal{O}_{x}/\mathcal{O}_{s}}$. When $\Omega^{1}_{X/S}$ is an $\mathcal{O}_{X}$-Module of finite type,
$T_{X/S}(x)$ is therefore a vector space of finite rank over $k(x)$, and for every base

<!-- original page 31 -->

change $g : S' \to S$ and every point $x' \in X' = X \times_{S} S'$ over $x$, one has a canonical isomorphism

```text
  (16.5.13.2)    T_{X'/S'}(x') ⥲ T_{X/S}(x) ⊗_{k(x)} k(x').
```

If $x$ is rational over $k(s)$, where $s = f(x)$ (so that $k(s) \to k(x)$ is an isomorphism), it follows from
`(16.4.13)` that one has a canonical isomorphism

```text
  (16.5.13.3)    T_{X/S}(x) = T_{X_s/k(s)}(x) = Hom_{k(s)}(𝔪'_x/𝔪'^2_x, k(x))
```

where $\mathfrak{m}'_{x}$ is the maximal ideal of $\mathcal{O}_{X_{s}, x} = \mathcal{O}_{X, x}/\mathfrak{m}_{s}
\mathcal{O}_{X, x}$. In the case where $S$ is the spectrum of a field $k$, one thus recovers the Zariski definition of
the tangent space at a point $x \in X$ rational over $k$, as the dual of $\mathfrak{m}_{x}/\mathfrak{m}^{2}_{x}$.

Let $Y$ be a second $S$-prescheme and let $g : Y \to X$ be an $S$-morphism; one has then a canonical homomorphism of
$\mathcal{O}_{Y}$-Modules `(16.4.19)`

$$ (16.5.13.4) g_{Y/X/S} : g*(\Omega^{1}_{X/S}) \to \Omega^{1}_{Y/S}. $$

Now note that if $y \in Y$ and $x = g(y)$, one has

```text
  g*(Ω_{X/S}^1) ⊗_{𝒪_Y} k(y) = (Ω_{X/S}^1 ⊗_{𝒪_X} k(x)) ⊗_{k(x)} k(y),
```

and consequently, if $\Omega^{1}_{X/S}$ is an $\mathcal{O}_{X}$-Module of finite type, one can identify

```text
  Hom_{k(y)}(g*(Ω_{X/S}^1) ⊗_{𝒪_Y} k(y), k(y))
```

with $T_{X/S}(x) \otimes_{k(x)} k(y)$. One therefore deduces from the homomorphism `(16.5.13.4)` a homomorphism of
$k(y)$-vector spaces

```text
  (16.5.13.5)    T_y(g) : T_{Y/S}(y) → T_{X/S}(x) ⊗_{k(x)} k(y)
```

called the **linear map tangent to $g$ at the point $y$**. When $y$ is rational over $k(s)$, one can identify $k(s)$,
$k(y)$ and $k(x)$, and $T_{y}(g)$ is then a homomorphism of $k(s)$-vector spaces $T_{Y/S}(y) \to T_{X/S}(x)$; note
moreover that in this case $g*(\Omega^{1}_{X/S}) \otimes_{\mathcal{O}_{Y}} k(y)$ is identified with $\Omega^{1}_{X/S}
\otimes_{\mathcal{O}_{X}} k(x)$, and the preceding homomorphism is therefore defined without any finiteness condition on
$\Omega^{1}_{X/S}$, and is none other than the homomorphism $T_{Y/S}(g)$ `(16.5.12)` restricted to the fibre at the
point $y$ of $T_{Y/S}$.

**(16.5.14).**

<!-- label: IV.16.5.14 -->

The interpretation of derivations of an $A$-algebra $B$ into a $B$-module $L$, given in `(0, 20.1.1)`, translates into
the language of preschemes in the following way.

Consider two morphisms of preschemes $f : X \to S$, $g : Y \to S$, and a closed sub-prescheme `Y_0` of $Y$ defined by a
square-zero Ideal $\mathcal{I}$ of $\mathcal{O}_{Y}$ (so that $Y$ and `Y_0` have the same underlying topological space).
Suppose given an $S$-morphism $u_{0} : Y_{0} \to X$, so that one has a commutative diagram

```text
  (16.5.14.1)
              X   <──u_0──   Y_0
              │              │
              f              j
              ↓              ↓
              S   <──g──     Y
```

<!-- original page 32 -->

and we propose to look for $S$-morphisms $u : Y \to X$ such that $u_{0} = u \circ j$ (in other words, whether it is
possible to complete the preceding diagram by the dotted arrow $u$ so as to leave it commutative).

For this, consider an affine open $U = \operatorname{Spec}(C)$ of $Y$; its inverse image $j^{-1}(U)$ is the affine open
$U_{0} = \operatorname{Spec}(C/\mathfrak{L})$, where $\mathfrak{L} = \Gamma(U, \mathcal{I})$, an ideal of square zero in
$C$; we shall suppose $U$ small enough that $u_{0}(U_{0})$ is contained in an affine open $V = \operatorname{Spec}(B)$
of $X$, and $g(U) = f(u_{0}(U_{0}))$ contained in an affine open $W = \operatorname{Spec}(A)$ of $S$, so that $B$ and
$C$ are $A$-algebras and $u_{0}|U_{0}$ corresponds to an $A$-homomorphism $\psi$ of $B$ into $C/\mathfrak{L}$; let
$P(U_{0})$ be the set of restrictions $u|U$ of the sought-for homomorphisms, which correspond canonically to the
$A$-homomorphisms of algebras $\phi : B \to C$ such that the composite `B ──φ──> C → C/𝔏` is equal to $\psi$. One knows
therefore `(0, 20.1.1)` that the set of these homomorphisms is empty or of the form $\phi_{1} +
\operatorname{Der}_{A}(B, \mathfrak{L})$; when $P(U_{0})$ is not empty, the additive group $\operatorname{Der}_{A}(B,
\mathfrak{L})$ acts by addition on $P(U_{0})$, which is then an **affine space** for the additive group
$\operatorname{Der}_{A}(B, \mathfrak{L})$ (or also a **principal homogeneous space** (or **torsor**) under
$\operatorname{Der}_{A}(B, \mathfrak{L})$).

Now remark that, since $\mathfrak{L}$ is endowed with a $B$-module structure via $\psi$, one has an isomorphism $v
\mapsto v \circ d_{B/A}$ from $\operatorname{Hom}_{B}(\Omega^{1}_{B/A}, \mathfrak{L})$ onto $\operatorname{Der}_{A}(B,
\mathfrak{L})$ `(0, 20.4.8)`. Moreover, as $\mathfrak{L}$ is of square zero, hence a $(C/\mathfrak{L})$-module, every
$B$-homomorphism $v : \Omega^{1}_{B/A} \to \mathfrak{L}$ can be considered as a $(C/\mathfrak{L})$-homomorphism
$\Omega^{1}_{B/A} \otimes_{B} (C/\mathfrak{L}) \to \mathfrak{L}$. Since $\mathcal{I}$ is of square zero, it can be
considered as a quasi-coherent $\mathcal{O}_{Y_{0}}$-Module; introduce the $\mathcal{O}_{Y_{0}}$-Module

$$ (16.5.14.2) \mathcal{G} = \mathcal{H}o\mathcal{m}(u_{0}*(\Omega^{1}_{X/S}), \mathcal{I}); $$

it follows then from the fact that $\Omega^{1}_{B/A} = \Gamma(V, \Omega^{1}_{X/S})$ `(16.3.7)` that one can write
$\operatorname{Der}_{A}(B, \mathfrak{L}) = \Gamma(U_{0}, \mathcal{G})$.

As $P(U_{0})$ is defined as the set of $S$-morphisms $U \to X$, it is clear that $U_{0} \mapsto P(U_{0})$ is a *sheaf of
sets* $\mathcal{P}$ on `Y_0`. We use this fact to prove that the map $h : \Gamma(U_{0}, \mathcal{G}) \times P(U_{0}) \to
P(U_{0})$ defining the torsor structure on $P(U_{0})$ is independent of the choice of $V$ and $W$, and in addition that,
if $U' \subset U$ is a second affine open of $Y$ and $U'_{0}$ is its inverse image in `Y_0`, the diagram

```text
  (16.5.14.3)
              Γ(U_0, 𝒢) × P(U_0)   ──h──>   P(U_0)
                   │                          │
                   ↓                          ↓
              Γ(U'_0, 𝒢) × P(U'_0) ──h'──>   P(U'_0)
```

is commutative (the vertical arrows being the restriction operators). By virtue of the preceding remark, one is reduced
to proving the commutativity of the preceding diagram when $h$ is defined as above from the affine opens $V$, $W$ and
$h'$ from affine

<!-- original page 33 -->

opens $V' \subset V$ and $W' \subset W$. But by virtue of the preceding description of $h$, this follows from the
commutativity of the diagram `(0, 20.5.4.2)`.

The maps $\Gamma(U_{0}, \mathcal{G}) \times P(U_{0}) \to P(U_{0})$ therefore define a homomorphism of sheaves of sets
$m : \mathcal{G} \times \mathcal{P} \to \mathcal{P}$ such that, for every open `U_0` for which
$\Gamma(U_{0}, \mathcal{P}) \neq \emptyset$,
$m_{U_{0}} : \Gamma(U_{0}, \mathcal{G}) \times \Gamma(U_{0}, \mathcal{P}) \to \Gamma(U_{0}, \mathcal{P})$ is an external
law defining on $\Gamma(U_{0}, \mathcal{P})$ a torsor structure under the group $\Gamma(U_{0}, \mathcal{G})$.

**(16.5.15).**

<!-- label: IV.16.5.15 -->

In general, when one is given on a topological space $Z$ a sheaf of sets $\mathcal{P}$, a sheaf of groups $\mathcal{G}$
(not necessarily commutative), and a homomorphism of sheaves of sets $m : \mathcal{G} \times \mathcal{P} \to
\mathcal{P}$ such that, for every open $U \subset Z$ with $\Gamma(U, \mathcal{P}) \neq \emptyset$, $m_{U} : \Gamma(U,
\mathcal{G}) \times \Gamma(U, \mathcal{P}) \to \Gamma(U, \mathcal{P})$ makes $\Gamma(U, \mathcal{P})$ a torsor under the
group $\Gamma(U, \mathcal{G})$, one says that $\mathcal{P}$ is a **pseudo-torsor** (or **formally principal homogeneous
sheaf**) under the sheaf of groups $\mathcal{G}$. One says that $\mathcal{P}$ is a **torsor** (or **principal
homogeneous sheaf**) under $\mathcal{G}$ if, in addition, $\Gamma(U, \mathcal{P}) \neq \emptyset$ for every non-empty
open $U$ in a suitable base of the topology of $Z$.

For the general theory of torsors, we refer to `[42]`; we shall limit ourselves here to recalling the canonical
correspondence between isomorphism classes of these torsors (for a given $\mathcal{G}$) and the elements of the
cohomology set $H^{1}(Z, \mathcal{G})$. Consider indeed a torsor $\mathcal{P}$ under $\mathcal{G}$ and an open cover
$(U_{\lambda})$ of $Z$ such that $\Gamma(U_{\lambda}, \mathcal{P}) \neq \emptyset$ for every $\lambda$; denote by
$p_{\lambda}$ an element of $\Gamma(U_{\lambda}, \mathcal{P})$. For every pair of indices $\lambda$, $\mu$ such that
$U_{\lambda} \cap U_{\mu} \neq \emptyset$, there exists then one and only one element $\gamma_{\lambda \mu}$ of
$\Gamma(U_{\lambda} \cap U_{\mu}, \mathcal{G})$ such that $\gamma_{\lambda \mu} \cdot (p_{\mu}|U_{\lambda} \cap U_{\mu})
= p_{\lambda}|U_{\lambda} \cap U_{\mu}$; furthermore, if $\lambda$, $\mu$, $\nu$ are three indices such that
$U_{\lambda} \cap U_{\mu} \cap U_{\nu} \neq \emptyset$, the restrictions $\gamma'_{\lambda \mu}$, $\gamma'_{\mu \nu}$,
$\gamma'_{\lambda \nu}$ of $\gamma_{\lambda \mu}$, $\gamma_{\mu \nu}$, $\gamma_{\lambda \nu}$ to $U_{\lambda} \cap
U_{\mu} \cap U_{\nu}$ satisfy the condition $\gamma'_{\lambda \nu} = \gamma'_{\lambda \mu} \gamma'_{\mu \nu}$; in other
words, $(\lambda, \mu) \mapsto \gamma_{\lambda \mu}$ is a **`1`-cocycle** of the cover $(U_{\lambda})$ with values in
$\mathcal{G}$. If, for every $\lambda$, $p'_{\lambda}$ is a second element of $\Gamma(U_{\lambda}, \mathcal{P})$, there
exists one and only one element $\beta_{\lambda} \in \Gamma(U_{\lambda}, \mathcal{G})$ such that $p'_{\lambda} =
\beta_{\lambda} \cdot p_{\lambda}$, and the `1`-cocycle $(\gamma'_{\lambda \mu})$ corresponding to the family
$(p'_{\lambda})$ is given by $\gamma'_{\lambda \mu} = \beta_{\lambda} \gamma_{\lambda \mu} \beta^{-1}_{\mu}$, that is to
say, is **cohomologous** to $(\gamma_{\lambda \mu})$. Conversely, the datum of a `1`-cocycle $(\gamma_{\lambda \mu})$
defines, for every pair $(\lambda, \mu)$, an automorphism $\theta_{\lambda \mu}$ of the sheaf of sets
$\mathcal{G}|U_{\lambda} \cap U_{\mu}$, namely the right translation by $\gamma_{\lambda \mu}$, and the fact that it is
a cocycle shows that one can glue the sheaves of sets $\mathcal{G}|U_{\lambda}$ by means of the automorphisms
$\theta_{\lambda \mu}$ $(0_{I}, 3.3.1)$; one thus obtains in the obvious way a torsor under $\mathcal{G}$, say
$\mathcal{P}$, and if one takes for $p_{\lambda}$ the unit section over $U_{\lambda}$, the corresponding `1`-cocycle is
none other than the given `1`-cocycle $(\gamma_{\lambda \mu})$; furthermore, if one replaces $(\gamma_{\lambda \mu})$ by
a `1`-cocycle $\gamma'_{\lambda \mu} = \beta_{\lambda} \gamma_{\lambda \mu} \beta^{-1}_{\mu}$ cohomologous to it, one
verifies at once that the torsor obtained is isomorphic to $\mathcal{P}$.

In particular, if $(\gamma_{\lambda \mu})$ is a **`1`-coboundary**, in other words of the form $\gamma_{\lambda \mu} =
\beta_{\lambda} \beta^{-1}_{\mu}$, the torsor $\mathcal{P}$ obtained is isomorphic to $\mathcal{G}$ (considered as a
torsor under itself for left translations); one says in this case that $\mathcal{P}$ is **trivial**, and the converse is
evident.

More particularly, it follows from `(III, 1.3.1)` that one has:

**Proposition (16.5.16).**

<!-- label: IV.16.5.16 -->

*Let $Z$ be an affine scheme, $\mathcal{G}$ a quasi-coherent $\mathcal{O}_{Z}$-Module; then every torsor under
$\mathcal{G}$ is trivial.*

<!-- original page 34 -->

Returning to the problem considered in `(16.5.14)`, one therefore obtains:

**Proposition (16.5.17).**

<!-- label: IV.16.5.17 -->

*Let $X$, $Y$ be two $S$-preschemes, `Y_0` a closed sub-prescheme of $Y$ defined by a quasi-coherent Ideal $\mathcal{I}$
of $\mathcal{O}_{Y}$ such that $\mathcal{I}^{2} = 0$, $j : Y_{0} \to Y$ the canonical injection. Let $u_{0} : Y_{0} \to
X$ be an $S$-morphism, and $\mathcal{P}$ the sheaf of sets on $Y$ such that, for every open $U$ of $Y$, $\Gamma(U,
\mathcal{P})$ is the set of $S$-morphisms $u : U \to X$ such that $u_{0}|U_{0} = u \circ (j|U_{0})$, where $U_{0} =
j^{-1}(U)$. Then there exists on $\mathcal{P}$ a structure of pseudo-torsor under the $\mathcal{O}_{Y_{0}}$-Module
$\mathcal{G} = \mathcal{H}o\mathcal{m}_{\mathcal{O}_{Y_{0}}}(u_{0}*(\Omega^{1}_{X/S}), \mathcal{I})$.*

In particular:

**Corollary (16.5.18).**

<!-- label: IV.16.5.18 -->

*With the notation of `(16.5.17)`, suppose that $Y$ is affine and $\Omega^{1}_{X/S}$ is of finite presentation; if there
exists an open cover $(U_{\alpha})$ of $Y$ and, for each index $\alpha$, an $S$-morphism $v_{\alpha} : U_{\alpha} \to X$
such that, putting $U^{0}_{\alpha} = j^{-1}(U_{\alpha})$, one has $v_{\alpha} \circ (j|U^{0}_{\alpha}) =
u_{0}|U^{0}_{\alpha}$, then there exists an $S$-morphism $u : Y \to X$ such that $u \circ j = u_{0}$.*

Indeed, $\mathcal{G}$ is then a quasi-coherent $\mathcal{O}_{Y_{0}}$-Module `(I, 1.3.12)`; by virtue of `(16.5.16)` and
of the fact that `Y_0` is then affine, the sheaf $\mathcal{P}$, which is by hypothesis a torsor under $\mathcal{G}$, and
not only a pseudo-torsor, is trivial; but if $w$ is an isomorphism from $\mathcal{G}$ onto $\mathcal{P}$ (as torsors
under $\mathcal{G}$), the image under $w$ of the zero section of $\mathcal{G}$ is the sought-for $S$-morphism $u$.

<!-- original page 34 -->

### 16.6. Sheaves of $\Omega$-differentials and exterior differential

**(16.6.1).**

<!-- label: IV.16.6.1 -->

Let $f : X \to S$ be a morphism of preschemes. We call the *sheaf of $p$-differentials of $X$ relative to $S$* ($p$ an
integer) the *$p$-th exterior power* $(0_{I}, 4.1.5)$ of the $\mathcal{O}_{X}$-Module $\Omega^{1}_{X/S}$, denoted

$$ (16.6.1.1) \Omega^{p}_{X/S} = \Lambda^{p}(\Omega^{1}_{X/S}). $$

One thus has $\Omega^{0}_{X/S} = \mathcal{O}_{X}$ and $\Omega^{p}_{X/S} = 0$ for $p < 0$; the $\Omega^{p}_{X/S}$ are the
homogeneous components of the exterior algebra of $\Omega^{1}_{X/S}$

```text
  (16.6.1.2)    Ω^•_{X/S} = Λ(Ω^1_{X/S}) = ⊕_{p ∈ ℤ} Λ^p(Ω^1_{X/S}),
```

which is therefore a quasi-coherent graded $\mathcal{O}_{X}$-Algebra, anti-commutative, and whose elements of degree `1`
are of square zero. For every affine open set $U$ of $X$, one has $\Gamma(U, \Omega^{\bullet}_{X/S}) = \Lambda(\Gamma(U,
\Omega^{1}_{X/S}))$, where $\Gamma(U, \Omega^{1}_{X/S})$ is considered as a $\Gamma(U, \mathcal{O}_{X})$-module.

When $S = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$ are affine, $B$ being then an $A$-algebra, one has
$(0_{I}, 4.1.5)$ $\Omega^{p}_{X/S} = (\Omega^{p}_{B/A})^{\sim}$, on setting $\Omega^{p}_{B/A} = \Lambda^{p}
\Omega^{1}_{B/A}$.

**Theorem (16.6.2).**

<!-- label: IV.16.6.2 -->

*There exists one and only one endomorphism $d$ of the sheaf of additive groups $\Omega^{\bullet}_{X/S}$ having the
following properties:*

*(i) $d \circ d = 0$.*

*(ii) For every open set $U$ of $X$ and every section $f \in \Gamma(U, \mathcal{O}_{X})$, one has $df = d_{X/S} f$.*

<!-- original page 35 -->

*(iii) For every open set $U$ of $X$, every pair of integers `p, q` and every pair of sections $\omega'_{p} \in
\Gamma(U, \Omega^{p}_{X/S})$, $\omega''_{q} \in \Gamma(U, \Omega^{q}_{X/S})$, one has*

```text
  (16.6.2.1)    d(ω'_p ∧ ω''_q) = (dω'_p) ∧ ω''_q + (−1)^p ω'_p ∧ (dω''_q).
```

*Moreover, $d$ is an endomorphism of graded $\psi*(\mathcal{O}_{S})$-Modules of degree `+1`.*

Suppose the existence of the endomorphism $d$ is established. For every affine open set $U$ of $X$, every section of
$\Omega^{p}_{X/S}$ over $U$ is, by virtue of (ii), a linear combination of finitely many elements of the form $g(df_{1}
\wedge df_{2} \wedge \cdots \wedge df_{p})$, where $g$ and the $f_{i}$ are sections of $\mathcal{O}_{X}$ over $U$
`(0, 20.4.7)`. The conditions (i) and (iii) then show, by induction on $p$, that one necessarily has

```text
  (16.6.2.2)    d(g(df_1 ∧ df_2 ∧ ⋯ ∧ df_p)) = dg ∧ df_1 ∧ df_2 ∧ ⋯ ∧ df_p.
```

This proves the *uniqueness* of $d$ and the last assertion of the theorem. By virtue of this uniqueness property, to
establish the existence of $d$ one may restrict to the case where $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine. Now (Bourbaki, *Alg.*, chap. III, 3rd ed., §10), to define an $A$-antiderivation $D$
of degree `+1` of an exterior algebra $\Lambda(M)$ (where $M$ is a $B$-module and $B$ an $A$-algebra), this
antiderivation taking its values in a graded anti-commutative $A$-algebra $C = \oplus^{\infty}_{n=0} C_{n}$ whose
elements of degree `1` are of square zero, it suffices to arbitrarily prescribe an $A$-derivation `D_0` of $B$ into
`C_1` and an $A$-homomorphism `D_1` of $M$ into `C_2`; there then exists one and only one $A$-antiderivation $D$ of
$\Lambda(M)$ into $C$ coinciding with `D_0` on $B$ and with `D_1` on $M$.

In the present case, `D_0` is necessarily equal to $d_{B/A}$ by virtue of (ii); everything comes down to showing, taking
`(16.6.2.2)` into account, that there is an $A$-homomorphism $u$ of $\Omega^{1}_{B/A}$ into $\Omega^{2}_{B/A}$ such that

```text
  (16.6.2.3)    u(g · df) = dg ∧ df
```

for arbitrary `f, g` in $B$; for this it will suffice to show that there exists an $A$-homomorphism $v : B \otimes_{A}
\Omega^{1}_{B/A} \to \Omega^{2}_{B/A}$ such that

```text
  (16.6.2.4)    v(g · ω) = dg ∧ ω
```

for $g \in B$ and $\omega \in \Omega^{1}_{B/A}$. Finally, since $\Omega^{1}_{B/A} = \mathfrak{J}/\mathfrak{J}^{2}$
(where $\mathfrak{J} = \mathfrak{J}_{B/A}$ is the kernel of the canonical homomorphism $B \otimes_{A} B \to B$) and
since $\Omega^{1}_{B/A}$ is generated by elements of the form $g \cdot df$, it suffices to define an $A$-homomorphism
$w : B \otimes_{A} (B \otimes_{A} B) \to \Omega^{2}_{B/A}$ such that

```text
  (16.6.2.5)    w(g' ⊗ g ⊗ f) = dg' ∧ (g · df)
```

and such that $w$ vanishes on the image of $B \otimes_{A} \mathfrak{J}^{2}$. Now, since the right-hand side of
`(16.6.2.5)` is $A$-trilinear in `g', g, f`, the existence of $w$ satisfying `(16.6.2.5)` is immediate. On the other
hand, since $\mathfrak{J}$ is generated by the elements $1 \otimes x - x \otimes 1$ ($x \in B$), one is reduced to
verifying that when $z = (1 \otimes x - x \otimes 1)(1 \otimes y - y \otimes 1)$, one has $w(g' \otimes z) = 0$. Now,
since $z = 1 \otimes (xy) + (xy) \otimes 1 - x \otimes y - y \otimes x$, the formula `(16.6.2.4)` shows that it

<!-- original page 36 -->

suffices to see that one has $d(xy) - x \cdot dy - y \cdot dx = 0$, which expresses that $d$ is a derivation.

It remains to prove that $d$ satisfies condition (i). Now, the square of an antiderivation is a derivation (Bourbaki,
*loc. cit.*), and since $\Omega^{\bullet}_{B/A}$ is generated by $\Omega^{1}_{B/A}$ as a $B$-algebra, it suffices to
verify that $d(dz) = 0$ for $z \in B$ and for $z \in \Omega^{1}_{B/A}$. In the first case, this follows from formula
`(16.6.2.3)` with $g = 1$; in the second, one may restrict to the case where $z = g \cdot df$ with `f, g` in $B$, and
then, by virtue of `(16.6.2.1)` and `(16.6.2.3)`, one has

```text
  d(d(g · df)) = d(dg ∧ df) = (d(dg)) ∧ (df) − (dg) ∧ (d(df)) = 0.
```

Q.E.D.

**Definition (16.6.3).**

<!-- label: IV.16.6.3 -->

*The antiderivation $d$ defined in `(16.6.2)` (also denoted $d_{X/S}$) is called the **exterior differential** on $X$
(relative to $S$).*

**Proposition (16.6.4).**

<!-- label: IV.16.6.4 -->

*For every base change $g : S' \to S$, on setting $X' = X \times_{S} S'$, the canonical homomorphism*

```text
  (16.6.4.1)    Ω^•_{X/S} ⊗_S S' → Ω^•_{X'/S'}
```

*deduced from the isomorphism `(16.5.9.1)` is bijective. Moreover, if $s$ is a section of $\Omega^{\bullet}_{X/S}$ over
an open set $U$ of $X$, and $s \otimes 1$ its inverse image, a section of $\Omega^{\bullet}_{X'/S'}$ over the inverse
image $U'$ of $U$ in $X'$, one has $d_{X'/S'}(s \otimes 1) = d_{X/S}(s) \otimes 1$.*

The first assertion is immediate, since the formation of the exterior algebra of a module commutes with every extension
of the ring of scalars. To prove the second, by virtue of `(16.6.2.2)` one may restrict to the case $s \in \Gamma(U,
\mathcal{O}_{X})$, and in that case the assertion has already been proved `(16.4.3.7)`.

**(16.6.5).**

<!-- label: IV.16.6.5 -->

Suppose that $\Omega^{1}_{X/S}$ is a locally free $\mathcal{O}_{X}$-Module of rank $n$ at a point $x$, so that there
exist $n$ sections $s_{i} \in \Gamma(U, \mathcal{O}_{X})$ such that the $ds_{i}$ form a basis of the $\Gamma(U,
\mathcal{O}_{X})$-module $\Gamma(U, \Omega^{1}_{X/S})$ `(16.5.8)`. Then, for every integer $p \geq 1$, the
$p$-differentials $ds_{i_{1}} \wedge ds_{i_{2}} \wedge \cdots \wedge ds_{i_{p}}$ (for $i_{1} < i_{2} < \cdots < i_{p}$,
elements of `[1, n]`) form a basis of $binom(n, p)$ elements of $\Gamma(U, \Omega^{p}_{X/S})$ over $\Gamma(U,
\mathcal{O}_{X})$. Moreover, formula `(16.6.2.2)` shows that for every section $g \in \Gamma(U, \mathcal{O}_{X})$, one
has

```text
  (16.6.5.1)    d(g · ds_{i_1} ∧ ds_{i_2} ∧ ⋯ ∧ ds_{i_p})
                  = ∑_k (−1)^r (∂g/∂s_k) ds_{i_1} ∧ ⋯ ∧ ds_{i_r} ∧ ds_k ∧ ds_{i_{r+1}} ∧ ⋯ ∧ ds_{i_p}
```

where, on the right-hand side, $k$ ranges over the set of $n - p$ indices distinct from the $i_{h}$, $i_{r}$ being the
largest index $< k$.

One notes that the relation $d(dg) = 0$ for every section $g \in \Gamma(U, \mathcal{O}_{X})$ is expressed in the form

```text
  D_i(D_j g) = D_j(D_i g)    for i ≠ j;
```

in other words, the derivations $D_{i}$ defined in `(16.5.7)` commute pairwise.

### 16.7. The $\mathcal{P}^{n}_{X/S}(\mathcal{F})$

**(16.7.1).**

<!-- label: IV.16.7.1 -->

Let $f : X \to S$ be a morphism of preschemes and $\mathcal{F}$ an $\mathcal{O}_{X}$-Module. Let $X^{(n)}_{\Delta_{f}}$
denote the *$n$-th infinitesimal neighbourhood* of $X$ for the diagonal morphism

<!-- original page 36 -->

$\Delta_{f} : X \to X \times_{S} X$, let $h_{n} : X^{(n)}_{\Delta_{f}} \to X \times_{S} X$ be the canonical morphism
`(16.1.2)`, and consider the two composite morphisms

```text
  p_1^{(n)} : X^{(n)}_{Δ_f} ──h_n──▶ X ×_S X ──p_1──▶ X,
  p_2^{(n)} : X^{(n)}_{Δ_f} ──h_n──▶ X ×_S X ──p_2──▶ X
```

so that, by definition, $p^{(n)}_{1}$ corresponds to the homomorphism of sheaves of rings $\mathcal{O}_{X} \to
\mathcal{P}^{n}_{X/S}$ that we have chosen in order to define the $\mathcal{O}_{X}$-Algebra structure on
$\mathcal{P}^{n}_{X/S}$ `(16.3.5)`, and $p^{(n)}_{2}$ to the homomorphism of sheaves of rings $d^{n}_{X/S} :
\mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}$ `(16.3.6)`. Since $X^{(n)}_{\Delta_{f}}$ and $X$ have the same underlying
space, one can write

$$ (16.7.1.1) \mathcal{P}^{n}_{X/S} = (p^{(n)}_{1})_{*} ((p^{(n)}_{2})*(\mathcal{O}_{X})). $$

More generally, we shall set

$$ (16.7.1.2) \mathcal{P}^{n}_{X/S}(\mathcal{F}) = (p^{(n)}_{1})_{*} ((p^{(n)}_{2})*(\mathcal{F})) $$

so that $\mathcal{P}^{n}_{X/S} = \mathcal{P}^{n}_{X/S}(\mathcal{O}_{X})$; by definition,
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is then an $\mathcal{O}_{X}$-Module.

**(16.7.2).**

<!-- label: IV.16.7.2 -->

Returning to the definitions of inverse images of Modules on ringed spaces $(0_{I}, 4.3.1)$ and taking into account that
$X^{(n)}_{\Delta_{f}}$ and $X$ have the same underlying space, one sees that one may also write the definition
`(16.7.1.2)` in the form

```text
  (16.7.2.1)    𝒫^n_{X/S}(ℱ) = 𝒫^n_{X/S} ⊗_{𝒪_X} ℱ,
```

but where one must take care that, in the interpretation of the symbol $\otimes$, $\mathcal{P}^{n}_{X/S}$ is endowed
with its $\mathcal{O}_{X}$-Module structure defined by *the homomorphism of sheaves of rings $d^{n}_{X/S} :
\mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}$*. It follows immediately from this formula (or directly from `(16.7.1.2)`)
that $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is canonically endowed with a $\mathcal{P}^{n}_{X/S}$-Module structure.

**Proposition (16.7.3).**

<!-- label: IV.16.7.3 -->

*(i) The functor $\mathcal{F} \mapsto \mathcal{P}^{n}_{X/S}(\mathcal{F})$ from the category of $\mathcal{O}_{X}$-Modules
to the category of $\mathcal{P}^{n}_{X/S}$-Modules is right exact and commutes with arbitrary inductive limits; it is
exact when $\mathcal{P}^{n}_{X/S}$ is a flat $\mathcal{O}_{X}$-Module.*

*(ii) If $\mathcal{F}$ is a quasi-coherent (resp. finite type, resp. finitely presented) $\mathcal{O}_{X}$-Module, then
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is a quasi-coherent (resp. finite type, resp. finitely presented)
$\mathcal{P}^{n}_{X/S}$-Module.*

The assertions of (i) follow immediately from formula `(16.7.2.1)` together with the symmetry of $\mathcal{P}^{n}_{X/S}$
`(16.3.4)`. The assertions of (ii) follow from the right exactness of the functor $\mathcal{F} \mapsto
\mathcal{P}^{n}_{X/S}(\mathcal{F})$.

**(16.7.4).**

<!-- label: IV.16.7.4 -->

The two $\mathcal{O}_{X}$-Module structures on $\mathcal{P}^{n}_{X/S}$ define on $\mathcal{P}^{n}_{X/S}(\mathcal{F})$
two $\mathcal{O}_{X}$-Module structures, which are moreover permutable, hence an $\mathcal{O}_{X}$-Bimodule structure.
It is convenient to denote on the *left* the structure coming from the structure homomorphism $\mathcal{O}_{X} \to
\mathcal{P}^{n}_{X/S}$ (chosen in `(16.3.5)`) and on the *right* the one coming from the homomorphism $d^{n}_{X/S} :
\mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S}$. In other words, for every open set $U$ of $X$ and every triple of elements
$a \in \Gamma(U, \mathcal{O}_{X})$, $b \in \Gamma(U, \mathcal{P}^{n}_{X/S})$, $t \in \Gamma(U, \mathcal{F})$, one has by
definition

```text
  (16.7.4.1)    a(b ⊗ t) = (ab) ⊗ t,    (b ⊗ t) a = (b · d^n a) ⊗ t = b ⊗ (at) = (d^n a) · (b ⊗ t).
```

The $\mathcal{O}_{X}$-Module structure coming from the definition `(16.7.1.2)` is, with these conventions, the *left*
$\mathcal{O}_{X}$-Module structure.

<!-- original page 38 -->

If $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module, the same holds of $\mathcal{P}^{n}_{X/S}(\mathcal{F})$
for either of its $\mathcal{O}_{X}$-Module structures. If, moreover, $\mathcal{F}$ is of finite type (resp. finitely
presented) and $f : X \to S$ is locally of finite type (resp. locally of finite presentation), then
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is (for either of its $\mathcal{O}_{X}$-Module structures) of finite type (resp.
finitely presented), as follows from `(16.3.9)` and `(16.4.22)`.

**(16.7.5).**

<!-- label: IV.16.7.5 -->

The definition `(16.7.2.1)` entails the existence of a homomorphism of sheaves of commutative groups

```text
  (16.7.5.1)    d^n_{X/S, ℱ} : ℱ → 𝒫^n_{X/S}(ℱ)    (also written d^n_{X/S})
```

such that, in the notations of `(16.7.4)`, one has

$$ (16.7.5.2) d^{n}_{X/S, \mathcal{F}}(t) = 1 \otimes t $$

and consequently, by virtue of `(16.7.4.1)`,

```text
  (16.7.5.3)    d^n_{X/S, ℱ}(at) = (1 ⊗ t) a = (d^n_{X/S, ℱ}(t)) · a,
```

```text
  (16.7.5.4)    d^n_{X/S, ℱ}(at) = (d^n_{X/S}(a)) · (1 ⊗ t) = (d^n_{X/S}(a)) · (d^n_{X/S, ℱ}(t)).
```

It is therefore $\mathcal{O}_{X}$-linear for the right $\mathcal{O}_{X}$-Module structure on
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$, and *semilinear* (relative to the automorphism $\sigma$ `(16.3.4)`) for the left
$\mathcal{O}_{X}$-Module structure.

**Proposition (16.7.6).**

<!-- label: IV.16.7.6 -->

*The right $\mathcal{O}_{X}$-Module $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is generated by the image of $\mathcal{F}$
under the canonical homomorphism $d^{n}_{X/S, \mathcal{F}}$.*

This follows immediately from `(16.7.5.3)` and the particular case $\mathcal{F} = \mathcal{O}_{X}$ `(16.3.8)`.

**(16.7.7).**

<!-- label: IV.16.7.7 -->

The canonical homomorphisms of sheaves of rings

$$ \phi_{nm} : \mathcal{P}^{m}_{X/S} \to \mathcal{P}^{n}_{X/S} $$

for $n \leq m$ `(16.1.2)` define, by virtue of `(16.7.2.1)`, canonical homomorphisms

```text
  𝒫^m_{X/S}(ℱ) → 𝒫^n_{X/S}(ℱ)    (n ≤ m)
```

which are homomorphisms of $\mathcal{O}_{X}$-Bimodules by virtue of `(16.1.6)` and `(16.7.4.1)`; moreover, one has
commutative diagrams

```text
            𝒫^m_{X/S}(ℱ) ────▶ 𝒫^n_{X/S}(ℱ)
                ▲                  ▲
       d^m_{X/S, ℱ}       d^n_{X/S, ℱ}
                  ╲              ╱
                       ℱ
```

One thus has a projective system of $\mathcal{O}_{X}$-Bimodules $(\mathcal{P}^{n}_{X/S}(\mathcal{F}))$, and one sets

$$ (16.7.7.1) \mathcal{P}^{\infty}_{X/S}(\mathcal{F}) = \varprojlim \mathcal{P}^{n}_{X/S}(\mathcal{F}). $$

Moreover, the preceding shows that the homomorphisms `(16.7.5.1)` form a projective system of homomorphisms, and
therefore define a canonical homomorphism

```text
  (16.7.7.2)    d^∞_{X/S, ℱ} : ℱ → 𝒫^∞_{X/S}(ℱ).
```

<!-- original page 39 -->

**(16.7.8).**

<!-- label: IV.16.7.8 -->

Let $\mathcal{F}, \mathcal{G}$ be two $\mathcal{O}_{X}$-Modules; it follows immediately from the definition `(16.7.2.1)`
that there is a canonical isomorphism of $\mathcal{P}^{n}_{X/S}$-Modules

```text
  (16.7.8.1)    𝒫^n_{X/S}(ℱ ⊗_{𝒪_X} 𝒢) ⥲ 𝒫^n_{X/S}(ℱ) ⊗_{𝒫^n_{X/S}} 𝒫^n_{X/S}(𝒢)
```

(Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 1, prop. 3).

One concludes in particular (or one sees directly from the definition `(16.7.2.1)`) that if $\mathcal{F}$ is endowed
with an $\mathcal{O}_{X}$-Algebra structure (not necessarily associative), then $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is
canonically endowed with a $\mathcal{P}^{n}_{X/S}$-Algebra structure; this Algebra is associative (resp. commutative,
resp. unital, resp. a Lie Algebra) whenever $\mathcal{F}$ is. Furthermore, the canonical homomorphisms
$\mathcal{P}^{m}_{X/S}(\mathcal{F}) \to \mathcal{P}^{n}_{X/S}(\mathcal{F})$ for $n \leq m$ `(16.7.7)` are then
di-homomorphisms of Algebras; similarly, `(16.7.5.1)` is then a homomorphism of $\mathcal{O}_{X}$-Algebras when
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is endowed with its $\mathcal{O}_{X}$-Algebra structure coming from its right
$\mathcal{O}_{X}$-Module structure.

With the same notations, one also has a canonical homomorphism of $\mathcal{P}^{n}_{X/S}$-Modules

```text
  (16.7.8.2)    𝒫^n_{X/S}(ℋom_{𝒪_X}(ℱ, 𝒢)) → ℋom_{𝒫^n_{X/S}}(𝒫^n_{X/S}(ℱ), 𝒫^n_{X/S}(𝒢))
```

(Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 3), which is bijective when $\mathcal{F}$ is a locally free
$\mathcal{O}_{X}$-Module of finite type (*loc. cit.*, prop. 7).

**(16.7.9).**

<!-- label: IV.16.7.9 -->

Suppose one is in the situation described in `(16.4.1)`; then, from the canonical homomorphism $P^{n}(u)$ `(16.4.3.3)`,
one deduces immediately a canonical homomorphism of $\mathcal{O}_{X'}$-Bimodules

$$ (16.7.9.1) u*(\mathcal{P}^{n}_{X/S}(\mathcal{F})) \to \mathcal{P}^{n}_{X'/S'}(u*(\mathcal{F})). $$

We leave to the reader the task of extending to this homomorphism the properties seen in `(16.4)` for the case
$\mathcal{F} = \mathcal{O}_{X}$.

**Remark (16.7.10).**

<!-- label: IV.16.7.10 -->

The definition of $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ in the form `(16.7.1.2)` still makes sense when $\mathcal{F}$ is
an arbitrary sheaf of sets (the inverse image of a sheaf of sets under $p^{(n)}_{2}$ being defined in $(0_{I}, 3.7.1)$);
a variant of this definition allows one to define the *"scheme of jets"* (relative to $S$) of an arbitrary
$X$-prescheme.

### 16.8. Differential operators[^16.8-gabriel]

**Definition (16.8.1).**

<!-- label: IV.16.8.1 -->

*Let $f = (\psi, \theta) : X \to S$ be a morphism of preschemes, $\mathcal{F}$, $\mathcal{G}$ two
$\mathcal{O}_{X}$-Modules, $n$ an integer $\geq 0$. We say that a homomorphism of sheaves of additive groups $D :
\mathcal{F} \to \mathcal{G}$ is a **differential operator of order $\leq n$** (relative to $S$) if there exists a
homomorphism of $\mathcal{O}_{X}$-Modules $u : \mathcal{P}^{n}_{X/S}(\mathcal{F}) \to \mathcal{G}$ (where
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is endowed with its left $\mathcal{O}_{X}$-Module structure `(16.7.4)`) such that
$D = u \circ d^{n}_{X/S, \mathcal{F}}$.*

It is clear, by virtue of the existence of canonical homomorphisms

$$ \mathcal{P}^{m}_{X/S}(\mathcal{F}) \to \mathcal{P}^{n}_{X/S}(\mathcal{F}) $$

<!-- original page 40 -->

for $n \leq m$ `(16.7.7)`, that a differential operator of order $\leq n$ is also a differential operator of order $\leq
m$ for every $m \geq n$. If $D : \mathcal{F} \to \mathcal{G}$ is a differential operator of order $\leq n$, then, for
every open set $U$ of $X$, $D | U : \mathcal{F} | U \to \mathcal{G} | U$ is also a differential operator of order $\leq
n$.

We say that a homomorphism $D : \mathcal{F} \to \mathcal{G}$ of the sheaves of additive groups underlying $\mathcal{F}$
and $\mathcal{G}$ is a *differential operator* (relative to $S$) if, for every $x \in X$, there exist an open
neighbourhood $U$ of $x$ and an integer $n \geq 0$ such that $D | U : \mathcal{F} | U \to \mathcal{G} | U$ is a
differential operator of order $\leq n$. The *order* of a differential operator $D : \mathcal{F} \to \mathcal{G}$ is the
infimum of integers $n$ such that $D$ is a differential operator of order $\leq n$ (and is therefore $+\infty$ if no
such integer exists); this order is always finite when $X$ is quasi-compact. The differential operators of order `0` are
precisely the homomorphisms of $\mathcal{O}_{X}$-Modules $\mathcal{F} \to \mathcal{G}$; by convention, every
differential operator of order `< 0` is zero. For $n \geq 0$, a differential operator is not in general a homomorphism
of $\mathcal{O}_{X}$-Modules but is always a homomorphism of $\psi*(\mathcal{O}_{S})$-Modules.

When $\mathcal{F} = \mathcal{O}_{X}$, a differential operator of order $\leq 1$ from $\mathcal{O}_{X}$ to $\mathcal{G}$
can be written in one and only one way in the form $v + D$, where $v : \mathcal{O}_{X} \to \mathcal{G}$ is an
$\mathcal{O}_{X}$-homomorphism and $D$ an *$S$-derivation* `(16.5.1)` of $\mathcal{O}_{X}$ into $\mathcal{G}$: this
follows from the structure of $\mathcal{P}^{1}_{B/A}$ `(0, 20.4.8)`.

**(16.8.2).**

<!-- label: IV.16.8.2 -->

In order to describe more explicitly a differential operator of order $\leq n$, $D : \mathcal{F} \to \mathcal{G}$, it
suffices, for every affine open set $U$ of $X$ whose image in $S$ is contained in an affine open set $V$, to
characterize the homomorphism $D = D_{U} : \Gamma(U, \mathcal{F}) \to \Gamma(U, \mathcal{G})$. On setting $\Gamma(V,
\mathcal{O}_{S}) = A$, $\Gamma(U, \mathcal{O}_{X}) = B$, so that $B$ is an $A$-algebra, one has $\Gamma(U,
\mathcal{P}^{n}_{X/S}(\mathcal{F})) = (B \otimes_{A} B)/\mathfrak{J}^{n+1}$, where for brevity one writes $\mathfrak{J}
= \mathfrak{J}_{B/A}$. Set moreover $M = \Gamma(U, \mathcal{F})$, $N = \Gamma(U, \mathcal{G})$; then the definition of
$D$ means that, for each pair $(U, V)$ satisfying the above conditions, the $A$-homomorphism $D : M \to N$ factors as

```text
  M → ((B ⊗_A B)/𝔍^{n+1}) ⊗_B M ──v──▶ N
```

where the first arrow is the canonical homomorphism $t \mapsto 1 \otimes t$, and $v$ is a $B$-homomorphism; the
$B$-module structure on $((B \otimes_{A} B)/\mathfrak{J}^{n+1}) \otimes_{B} M$ comes from the first factor $B$ (whereas
we recall that, in the formation of the tensor product over $B$, the $B$-module structure of $(B \otimes_{A}
B)/\mathfrak{J}^{n+1}$ is given by the second factor $B$). Note now that the $B$-module $((B \otimes_{A}
B)/\mathfrak{J}^{n+1}) \otimes_{B} M$ is isomorphic to $(B \otimes_{A} M)/\mathfrak{J}^{n+1}(B \otimes_{A} M)$, where $B
\otimes_{A} M$ is considered as a $(B \otimes_{A} B)$-module and its $B$-module structure comes from the homomorphism $b
\mapsto b \otimes 1$ of $B$ into $B \otimes_{A} B$. Let then $D'$ be the $B$-homomorphism of $B \otimes_{A} M$ into $N$
such that $D'(b \otimes t) = b \cdot D(t)$; the factorization condition on $D$ is again expressed by saying that $D'$
must vanish on the $B$-module $\mathfrak{J}^{n+1}(B \otimes_{A} M)$.

**(16.8.3).**

<!-- label: IV.16.8.3 -->

It is clear that the set of differential operators of order $\leq n$ from $\mathcal{F}$ to $\mathcal{G}$ is an additive
group, denoted $Diff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$; when $\mathcal{F} = \mathcal{G} = \mathcal{O}_{X}$, one also
writes $Diff^{n}_{X/S}$ instead of $Diff^{n}_{X/S}(\mathcal{O}_{X}, \mathcal{O}_{X})$.

It has been seen `(16.8.1)` that, for two open sets $U \supset V$ of $X$, one has a canonical restriction homomorphism

```text
  Diff^n_{U/S}(ℱ | U, 𝒢 | U) → Diff^n_{V/S}(ℱ | V, 𝒢 | V),
```

<!-- original page 41 -->

so that $U \mapsto Diff^{n}_{U/S}(\mathcal{F} | U, \mathcal{G} | U)$ is a presheaf of additive groups; in fact it is
even a sheaf, since for $U$ ranging over the open sets of $X$, the homomorphisms $u \mapsto u \circ d^{n}_{X/S,
\mathcal{F}}$ are *isomorphisms* of additive groups

```text
  (16.8.3.1)    Hom_{𝒪_U}(𝒫^n_{U/S}(ℱ | U), 𝒢 | U) ⥲ Diff^n_{U/S}(ℱ | U, 𝒢 | U),
```

by virtue of the fact that the image of $\mathcal{F}$ under $d^{n}_{X/S, \mathcal{F}}$ generates
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ `(16.7.6)`. This sheaf is denoted $\mathcal{D}iff^{n}_{X/S}(\mathcal{F},
\mathcal{G})$, and one therefore has:

**Proposition (16.8.4).**

<!-- label: IV.16.8.4 -->

*The isomorphisms `(16.8.3.1)` define an isomorphism of sheaves of additive groups*

```text
  (16.8.4.1)    ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) ⥲ 𝒟iff^n_{X/S}(ℱ, 𝒢).
```

When $\mathcal{F} = \mathcal{G} = \mathcal{O}_{X}$, one also writes $\mathcal{D}iff^{n}_{X/S}$ instead of
$\mathcal{D}iff^{n}_{X/S}(\mathcal{O}_{X}, \mathcal{O}_{X})$; it follows from `(16.8.4)` that $\mathcal{D}iff^{n}_{X/S}$
is canonically identified with the *dual* of the $\mathcal{O}_{X}$-Module $\mathcal{P}^{n}_{X/S}$; one also writes
$\langle t, D\rangle$ instead of $u(t)$ if $t$ is a section of $\mathcal{P}^{n}_{X/S}$ over an open set and $u$ is the
homomorphism from $\mathcal{P}^{n}_{X/S}$ to $\mathcal{O}_{X}$ corresponding to $D$.

**(16.8.5).**

<!-- label: IV.16.8.5 -->

Since $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is endowed with an $\mathcal{O}_{X}$-Bimodule structure `(16.7.4)`, one
canonically deduces an $\mathcal{O}_{X}$-Bimodule structure on
$\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{P}^{n}_{X/S}(\mathcal{F}), \mathcal{G})$, and hence also on
$\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$ by virtue of `(16.8.4.1)`. More precisely, to the left
$\mathcal{O}_{X}$-Module structure on $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ corresponds, by virtue of the definition
`(16.8.1)`, the left $\mathcal{O}_{X}$-Module structure on $\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$
explicitly described as follows: for every open set $U$ of $X$, every section $a \in \Gamma(U, \mathcal{O}_{X})$ and
every differential operator $D : \mathcal{F} | U \to \mathcal{G} | U$, `aD` is the differential operator which, to every
section $t \in \Gamma(U, \mathcal{F})$, associates the section

$$ (16.8.5.1) (aD)(t) = a \cdot D(t) $$

of $\Gamma(U, \mathcal{G})$. Similarly, to the right $\mathcal{O}_{X}$-Module structure on
$\mathcal{P}^{n}_{X/S}(\mathcal{F})$ corresponds the right $\mathcal{O}_{X}$-Module structure on
$\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$ explicitly described as follows: with the same notations, `Da` is
the differential operator which, to $t \in \Gamma(U, \mathcal{F})$, associates the section

```text
  (16.8.5.2)    (Da)(t) = D(at).
```

**Proposition (16.8.6).**

<!-- label: IV.16.8.6 -->

*If $f : X \to S$ is a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation, and $\mathcal{G}$ a quasi-coherent $\mathcal{O}_{X}$-Module, then
$\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$ is a quasi-coherent $\mathcal{O}_{X}$-Module for either of the
structures defined in `(16.8.5)`.*

The proposition follows from the fact that, under the hypotheses made, $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ is a
quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation `(16.7.4)`, and from `(I, 1.3.12)`.

**(16.8.7).**

<!-- label: IV.16.8.7 -->

The set of differential operators from $\mathcal{F}$ to $\mathcal{G}$ (of unspecified order, `(16.8.1)`) is denoted
$Diff_{X/S}(\mathcal{F}, \mathcal{G})$; one sees as in `(16.8.3)` that $U \mapsto Diff_{U/S}(\mathcal{F} | U,
\mathcal{G} | U)$ is a sheaf of additive groups, which we shall denote $\mathcal{D}iff_{X/S}(\mathcal{F}, \mathcal{G})$.
It is immediate that $\mathcal{D}iff_{X/S}(\mathcal{F}, \mathcal{G})$ is the union of the increasing filtered family of
its subsheaves $\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$; if $X$ is quasi-compact, $Diff_{X/S}(\mathcal{F},
\mathcal{G})$

<!-- original page 42 -->

is likewise the union of its subgroups $Diff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$ `(16.8.1)`. The
$\mathcal{O}_{X}$-Bimodule structures on the $\mathcal{D}iff^{n}_{X/S}(\mathcal{F}, \mathcal{G})$ therefore define an
$\mathcal{O}_{X}$-Bimodule structure on $\mathcal{D}iff_{X/S}(\mathcal{F}, \mathcal{G})$, again made explicit by
`(16.8.5.1)` and `(16.8.5.2)`.

Note that, for $n \leq m$, one has a commutative diagram

```text
  (16.8.7.1)
              ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) ──~──▶ 𝒟iff^n_{X/S}(ℱ, 𝒢)
                       │                              │
                       ▼                              ▼
              ℋom_{𝒪_X}(𝒫^m_{X/S}(ℱ), 𝒢) ──~──▶ 𝒟iff^m_{X/S}(ℱ, 𝒢)
```

where the horizontal arrows are the isomorphisms `(16.8.4.1)` and the left vertical arrow comes from the canonical
homomorphism $\mathcal{P}^{m}_{X/S}(\mathcal{F}) \to \mathcal{P}^{n}_{X/S}(\mathcal{F})$ `(16.7.7)`. For every open set
$U$ of $X$, let us endow $\Gamma(U, \mathcal{P}^{\infty}_{X/S}(\mathcal{F})) = \varprojlim \Gamma(U,
\mathcal{P}^{n}_{X/S}(\mathcal{F}))$ with the projective limit topology of the discrete topologies on the $\Gamma(U,
\mathcal{P}^{n}_{X/S}(\mathcal{F}))$; this defines on $\Gamma(U, \mathcal{P}^{\infty}_{X/S}(\mathcal{F}))$ a topological
$\Gamma(U, \mathcal{O}_{X})$-bimodule structure, so that $\mathcal{P}^{\infty}_{X/S}(\mathcal{F})$ appears as a sheaf
with values in the category of topological commutative groups $(0_{I}, 3.2.6)$. Then `(G, II, 1.11)` the limit of the
inductive system of sheaves of commutative groups $(\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{P}^{n}_{X/S}(\mathcal{F}),
\mathcal{G}))$ is none other than the sheaf of germs of continuous homomorphisms from
$\mathcal{P}^{\infty}_{X/S}(\mathcal{F})$ to $\mathcal{G}$ (the latter being equipped with the discrete topology): the
continuous homomorphisms from $\Gamma(U, \mathcal{P}^{\infty}_{X/S}(\mathcal{F}))$ into the discrete group $\Gamma(U,
\mathcal{G})$ correspond bijectively to the inductive systems of group homomorphisms $\Gamma(U,
\mathcal{P}^{n}_{X/S}(\mathcal{F})) \to \Gamma(U, \mathcal{G})$. One may therefore restate `(16.8.4)` by saying that
there is a canonical isomorphism

```text
  ℋom^{cont}_{𝒪_X}(𝒫^∞_{X/S}(ℱ), 𝒢) ⥲ 𝒟iff_{X/S}(ℱ, 𝒢)
```

where the left-hand member denotes the sheaf of germs of continuous homomorphisms from
$\mathcal{P}^{\infty}_{X/S}(\mathcal{F})$ to $\mathcal{G}$.

**Proposition (16.8.8).**

<!-- label: IV.16.8.8 -->

*Let $\mathcal{F}$, $\mathcal{G}$ be two $\mathcal{O}_{X}$-Modules, $D : \mathcal{F} \to \mathcal{G}$ a homomorphism of
$\psi*(\mathcal{O}_{S})$-Modules, $n$ an integer $\geq 0$. The following conditions are equivalent:*

*a) $D$ is a differential operator of order $\leq n$.*

*b) For every section $a$ of $\mathcal{O}_{X}$ over an open set $U$, the homomorphism $D_{a} : \mathcal{F} | U \to
\mathcal{G} | U$ such that, for every section $t$ of $\mathcal{F}$ over an open set $V \subset U$, one has*

```text
  (16.8.8.1)    D_a(t) = D(at) − a · D(t),
```

*is a differential operator of order $\leq n - 1$.*

*c) For every open set $U$ of $X$, every family $(a_{i})_{1 \leq i \leq n+1}$ of $n + 1$ sections of $\mathcal{O}_{X}$
over $U$, and every section $t$ of $\mathcal{F}$ over $U$, one has the identity*

```text
  (16.8.8.2)    ∑_{H ⊂ I_{n+1}} (−1)^{Card(H)} (∏_{i ∈ H} a_i) · D((∏_{i ∉ H} a_i) t) = 0
```

*(where $I_{n+1}$ denotes the interval $1 \leq i \leq n + 1$ of $\mathbb{N}$).*

<!-- original page 43 -->

Let us first prove the equivalence of a) and c). By definition, in order to prove that $D$ is a differential operator of
order $\leq n$ it suffices to show that this is so for the restriction $D | U : \mathcal{F} | U \to \mathcal{G} | U$ to
every affine open set $U$ of $X$; on the other hand, property c) holds for every open set $U$ of $X$ if it holds for
every affine open set. One may therefore restrict to the case where $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine. By virtue of `(16.8.2)` (whose notations we retain), condition a) means that the
$A$-homomorphism $D' : B \otimes_{A} M \to N$ such that $D'(b \otimes t) = b \cdot D(t)$ vanishes on
$\mathfrak{J}^{n+1}(B \otimes_{A} M)$, which, by virtue of `(0, 20.4.4)`, is equivalent to saying that $D'$ vanishes on
all elements of the form

```text
  (∏_{i=1}^{n+1} (a_i ⊗ 1 − 1 ⊗ a_i)) · (1 ⊗ t)
```

where $a_{i} \in B$ and $t \in M$. Now this element can be written $\sum_{H \subset I_{n+1}} (\prod_{i \in H} a_{i})
\otimes ((\prod_{i \notin H} a_{i}) t)$, and the value of $D'$ on this element is exactly the left-hand side of
`(16.8.8.2)`, which proves the equivalence of a) and c).

Let us now prove the equivalence of b) and c). We argue by induction on $n$, the assertion being trivial for $n = 0$.
Writing $a_{n+1}$ instead of $a$ in condition b), one sees, by the induction hypothesis, that condition b) means that
for every family $(a_{i})_{1 \leq i \leq n}$ of $n$ sections of $\mathcal{O}_{X}$ over $U$ and every section $t$ of
$\mathcal{F}$ over $U$,

```text
  ∑_{H' ⊂ I_n} (−1)^{Card(H')} (∏_{i ∈ H'} a_i) · D_{a_{n+1}}((∏_{i ∉ H'} a_i) t) = 0.
```

But if in this relation one replaces $D_{a_{n+1}}$ by its definition `(16.8.8.1)`, one immediately sees that one
obtains, up to sign, the left-hand side of `(16.8.8.2)`; whence the conclusion.

**Proposition (16.8.9).**

<!-- label: IV.16.8.9 -->

*If $D : \mathcal{F} \to \mathcal{G}$ is a differential operator of order $\leq n$, and $D' : \mathcal{G} \to
\mathcal{H}$ a differential operator of order $\leq n'$, then $D' \circ D : \mathcal{F} \to \mathcal{H}$ is a
differential operator of order $\leq n + n'$.*

By hypothesis, one may write $D = u \circ d^{n}_{X/S, \mathcal{F}}$ and $D' = v \circ d^{n'}_{X/S, \mathcal{G}}$, where
$u : \mathcal{P}^{n}_{X/S} \otimes_{\mathcal{O}_{X}} \mathcal{F} \to \mathcal{G}$ and $v : \mathcal{P}^{n'}_{X/S}
\otimes_{\mathcal{O}_{X}} \mathcal{G} \to \mathcal{H}$ are $\mathcal{O}_{X}$-homomorphisms. Everything comes down to
showing that the composite homomorphism of sheaves of additive groups

```text
  ℱ ──d^n_{X/S, ℱ}──▶ 𝒫^n_{X/S} ⊗_{𝒪_X} ℱ ──u──▶ 𝒢 ──d^{n'}_{X/S, 𝒢}──▶ 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒢
```

factors as

```text
  ℱ ──d^{n+n'}_{X/S, ℱ}──▶ 𝒫^{n+n'}_{X/S} ⊗_{𝒪_X} ℱ ──w──▶ 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒢
```

where $w$ is an $\mathcal{O}_{X}$-homomorphism. It will suffice to prove the

**Lemma (16.8.9.1).**

<!-- label: IV.16.8.9.1 -->

*There exists one and only one $\mathcal{O}_{X}$-homomorphism*

```text
  (16.8.9.2)    δ : 𝒫^{n+n'}_{X/S} → 𝒫^{n'}_{X/S}(𝒫^n_{X/S}) = 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒫^n_{X/S}
```

<!-- original page 44 -->

*making the diagram*

```text
  (16.8.9.3)
                          d^{n+n'}_{X/S}
                𝒪_X ──────────────▶ 𝒫^{n+n'}_{X/S}
                  │                     │
            d^n_{X/S}                   δ
                  ▼                     ▼
              𝒫^n_{X/S} ────────▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S})
                       d^{n'}_{X/S, 𝒫^n_{X/S}}
```

*commute.*

One will then indeed have a commutative diagram deduced from `(16.8.9.3)` by tensoring with $\mathcal{F}$

```text
                            d^{n+n'}_{X/S, ℱ}
                  ℱ ──────────────────▶ 𝒫^{n+n'}_{X/S}(ℱ)
                    │                          │
              d^n_{X/S, ℱ}                 δ ⊗ 1
                    ▼                          ▼
                𝒫^n_{X/S}(ℱ) ─────────▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ))
                              d^{n'}_{X/S, 𝒫^n_{X/S}(ℱ)}
```

and, on the other hand, one verifies immediately from the definition `(16.7.5)` that the diagram

```text
                                   u
                𝒫^n_{X/S}(ℱ) ──────▶ 𝒢
                    │                │
        d^{n'}_{X/S, 𝒫^n_{X/S}(ℱ)}   d^{n'}_{X/S, 𝒢}
                    ▼                ▼
        𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ)) ─1 ⊗ u─▶ 𝒫^{n'}_{X/S}(𝒢)
```

is commutative. One will therefore answer the question by taking $w$ to be the composite $\mathcal{O}_{X}$-homomorphism

```text
  𝒫^{n+n'}_{X/S}(ℱ) ──δ ⊗ 1──▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ)) ──1 ⊗ u──▶ 𝒫^{n'}_{X/S}(𝒢).
```

It remains to prove Lemma `(16.8.9.1)`. Taking `(16.7.6)` into account, which proves the uniqueness of $\delta$, one is
reduced to the case where $S = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$ are affine; on setting
$\mathfrak{J} = \mathfrak{J}_{B/A}$, it is a matter of defining a canonical homomorphism of $B$-modules

```text
  φ : (B ⊗_A B)/𝔍^{n+n'+1} → ((B ⊗_A B)/𝔍^{n'+1}) ⊗_B ((B ⊗_A B)/𝔍^{n+1}),
```

the $B$-module structures on both sides coming from the first factor $B$; let us recall that, in the tensor product of
the right-hand side, $(B \otimes_{A} B)/\mathfrak{J}^{n'+1}$ is to be considered

<!-- original page 45 -->

as a right $B$-module via its second factor $B$, and $(B \otimes_{A} B)/\mathfrak{J}^{n+1}$ as a left $B$-module via its
first factor $B$ `(16.7.2)`. It amounts to the same to define a homomorphism of $B$-modules

```text
  φ_0 : B ⊗_A B → ((B ⊗_A B)/𝔍^{n'+1}) ⊗_B ((B ⊗_A B)/𝔍^{n+1})
```

and to prove that it vanishes on $\mathfrak{J}^{n+n'+1}$. Now, such a homomorphism is immediately defined by the
condition

```text
  φ_0(b ⊗ b') = π_{n'}(b ⊗ 1) ⊗ π_n(1 ⊗ b')    for b, b' in B
```

with the notations of `(16.3.7)`. Moreover, it is immediate that $\phi_{0}$ is a homomorphism of *rings*. Now, one can
write

```text
  φ_0(b ⊗ 1 − 1 ⊗ b)
        = π_{n'}(b ⊗ 1 − 1 ⊗ b) ⊗ π_n(1 ⊗ 1)
          + π_{n'}(1 ⊗ b) ⊗ π_n(1 ⊗ 1) − π_{n'}(1 ⊗ 1) ⊗ π_n(1 ⊗ b)
```

and one has

```text
  π_{n'}(1 ⊗ b) ⊗ π_n(1 ⊗ 1) = π_{n'}(1 ⊗ 1) · b ⊗ π_n(1 ⊗ 1)
        = π_{n'}(1 ⊗ 1) ⊗ b · π_n(1 ⊗ 1) = π_{n'}(1 ⊗ 1) ⊗ π_n(b ⊗ 1)
```

whence finally

```text
  (16.8.9.4)    φ_0(b ⊗ 1 − 1 ⊗ b)
                  = π_{n'}(b ⊗ 1 − 1 ⊗ b) ⊗ π_n(1 ⊗ 1) + π_{n'}(1 ⊗ 1) ⊗ π_n(b ⊗ 1 − 1 ⊗ b).
```

A product of $n + n' + 1$ terms of the form `(16.8.9.4)` is therefore necessarily zero, since the same is true for a
product of $n + 1$ terms of the form $\pi_{n}(b \otimes 1 - 1 \otimes b)$ and a product of $n' + 1$ terms of the form
$\pi_{n'}(b \otimes 1 - 1 \otimes b)$. The conclusion thus follows from `(0, 20.4.4)`.

**Corollary (16.8.10).**

<!-- label: IV.16.8.10 -->

*The sheaf $\mathcal{D}iff_{X/S}(\mathcal{O}_{X}, \mathcal{O}_{X})$ (also denoted $\mathcal{D}iff_{X/S}$) is canonically
endowed with a structure of sheaf of rings, the $\mathcal{D}iff^{n}_{X/S}$ forming an increasing filtration compatible
with this structure.*

In particular, $\mathcal{D}iff^{0}_{X/S}$ is a sheaf of subrings of $\mathcal{D}iff_{X/S}$, canonically identified with
$\mathcal{O}_{X}$ `(16.8.1)`. Formulas `(16.8.5.1)` and `(16.8.5.2)` show that the $\mathcal{O}_{X}$-Bimodule structure
on $\mathcal{D}iff_{X/S}$ comes from left and right multiplication by sections of $\mathcal{O}_{X}$ considered as a
sheaf of subrings of $\mathcal{D}iff_{X/S}$.

**Remarks (16.8.11).**

<!-- label: IV.16.8.11 -->

(i) Suppose that $\mathcal{F} = \oplus_{\lambda \in L} \mathcal{F}_{\lambda}$; then it is clear `(16.7.2.1)` that
$\mathcal{P}^{n}_{X/S}(\mathcal{F}) = \oplus_{\lambda \in L} \mathcal{P}^{n}_{X/S}(\mathcal{F}_{\lambda})$; as the
functor $\mathcal{F} \mapsto \Gamma(U, \mathcal{F})$ commutes with the formation of arbitrary direct sums, $d^{n}_{X/S,
\mathcal{F}}$ is the homomorphism whose restriction to each $\mathcal{F}_{\lambda}$ is $d^{n}_{X/S,
\mathcal{F}_{\lambda}} : \mathcal{F}_{\lambda} \to \mathcal{P}^{n}_{X/S}(\mathcal{F}_{\lambda})$; one concludes
immediately that one has

```text
  Diff^n_{X/S}(ℱ, 𝒢) = ∏_{λ ∈ L} Diff^n_{X/S}(ℱ_λ, 𝒢),
```

and consequently also $(0_{I}, 3.2.6)$

```text
  𝒟iff^n_{X/S}(ℱ, 𝒢) = ∏_{λ ∈ L} 𝒟iff^n_{X/S}(ℱ_λ, 𝒢).
```

On the other hand, if $\mathcal{G} = \prod_{\mu \in M} \mathcal{G}_{\mu}$ $(0_{I}, 3.2.6)$, one has

```text
  Hom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) = ∏_{μ ∈ M} Hom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢_μ),
```

<!-- original page 46 -->

every homomorphism $u$ from $\mathcal{P}^{n}_{X/S}(\mathcal{F})$ to $\mathcal{G}$ corresponding bijectively to the
family of its composites $u_{\mu} : \mathcal{P}^{n}_{X/S}(\mathcal{F}) \to \mathcal{G} \to \mathcal{G}_{\mu}$. One
therefore has

```text
  Diff^n_{X/S}(ℱ, 𝒢) = ∏_{μ ∈ M} Diff^n_{X/S}(ℱ, 𝒢_μ),
```

and consequently also

```text
  𝒟iff^n_{X/S}(ℱ, 𝒢) = ∏_{μ ∈ M} 𝒟iff^n_{X/S}(ℱ, 𝒢_μ).
```

(ii) Up to now, one has hardly encountered differential operators $\mathcal{F} \to \mathcal{G}$ other than when
$\mathcal{F}$ and $\mathcal{G}$ are locally free $\mathcal{O}_{X}$-Modules of finite rank, in which case their structure
reduces locally, by virtue of (i), to that of the sheaf $\mathcal{D}iff_{X/S}$; the latter will be studied below
`(16.11)` in a particular case.

### 16.9. Regular and quasi-regular immersions

**Definition (16.9.1).**

<!-- label: IV.16.9.1 -->

*Let $X$ be a ringed space. We say that an Ideal $\mathcal{J}$ of $\mathcal{O}_{X}$ is **regular** (resp.
**quasi-regular**) if, for every point $x \in Supp(\mathcal{O}_{X}/\mathcal{J})$, there exist an open neighbourhood $U$
of $x$ in $X$ and a regular sequence `(0, 15.2.2)` (resp. quasi-regular sequence `(0, 15.2.2)`) of elements of
$\Gamma(U, \mathcal{O}_{X})$ generating $\mathcal{J} | U$.*

We say that a regular (resp. quasi-regular) sequence of sections of $\mathcal{O}_{X}$ over $U$ generating $\mathcal{J} |
U$ is a *regular system* (resp. *quasi-regular system*) of generators of $\mathcal{J} | U$.

**Definition (16.9.2).**

<!-- label: IV.16.9.2 -->

*Let $j : Y \to X$ be an immersion of preschemes and let $U$ be an open set of $X$ such that $j(Y) \subset U$ and $j$ is
a closed immersion of $Y$ into $U$. We say that $j$ is **regular** (resp. **quasi-regular**) if the closed sub-prescheme
$j(Y)$ of $U$ associated to $j$ is defined by a regular (resp. quasi-regular) Ideal of $\mathcal{O}_{U}$ (a condition
independent of the chosen open set $U$).*

We say that a sub-prescheme $Y$ of a prescheme $X$ is *regularly immersed* (resp. *quasi-regularly immersed*) if the
canonical injection $j : Y \to X$ is a regular (resp. quasi-regular) immersion. If $Y$ is a closed sub-prescheme of $X$
and $\mathcal{J}$ is the Ideal of $\mathcal{O}_{X}$ defining $Y$, this amounts to saying that $\mathcal{J}$ is regular
(resp. quasi-regular).

For example, if $A$ is an *integral* ring and $f$ is a nonzero element of $A$, the closed sub-prescheme $V(f)$ of
$\operatorname{Spec}(A)$ (isomorphic to $\operatorname{Spec}(A/fA)$) is *regularly immersed* in
$\operatorname{Spec}(A)$.

Every regular Ideal is quasi-regular `(0, 15.2.2)`; every regular immersion is quasi-regular (cf. `(16.9.11)` for a
partial converse).

**Proposition (16.9.3).**

<!-- label: IV.16.9.3 -->

*Let $X$ be a ringed space, $\mathcal{J}$ an Ideal of $\mathcal{O}_{X}$, $(f_{i})_{1 \leq i \leq n}$ a finite sequence
of sections of $\mathcal{O}_{X}$ over $X$ generating $\mathcal{J}$. For $(f_{i})$ to be a quasi-regular sequence
`(0, 15.2.2)`, it is necessary and sufficient that the following conditions hold:*

*(i) The canonical images of the $f_{i}$ in $\mathcal{J}/\mathcal{J}^{2}$ form a basis of this
$\mathcal{O}_{X}/\mathcal{J}$-Module.*

*(ii) The canonical surjective homomorphism `(16.1.2.2)`*

$$ \mathbb{S}^{\bullet}_{\mathcal{O}_{X}/\mathcal{J}}(\mathcal{J}/\mathcal{J}^{2}) \to
gr^{\bullet}_{\mathcal{J}}(\mathcal{O}_{X}) $$

*is bijective.*

*Moreover, if this is so, every sequence $(f'_{i})_{1 \leq i \leq n}$ of $n$ sections of $\mathcal{J}$ over $X$ which
generates $\mathcal{J}$ is quasi-regular.*

<!-- original page 47 -->

The two conditions of the statement merely translate the definition given in `(0, 15.2.2)`, taking into account the
definition of the canonical homomorphisms `(0, 15.2.1.1)`. The last assertion follows from the fact that if a module $M$
over a commutative ring $A$ admits a basis of $n$ elements, then every system of $n$ generators of $M$ is a basis of $M$
(Bourbaki, *Alg. comm.*, chap. II, §3, cor. 5 of th. 1).

**Corollary (16.9.4).**

<!-- label: IV.16.9.4 -->

*Let $X$ be a locally ringed space, $\mathcal{J}$ an Ideal of $\mathcal{O}_{X}$. For $\mathcal{J}$ to be quasi-regular,
it is necessary and sufficient that the following conditions hold:*

*(i) $\mathcal{J}$ is of finite type.*

*(ii) $\mathcal{J}/\mathcal{J}^{2}$ is a locally free $(\mathcal{O}_{X}/\mathcal{J})$-Module.*

*(iii) The canonical homomorphism*

$$ (16.9.4.1) \mathbb{S}^{\bullet}_{\mathcal{O}_{X}/\mathcal{J}}(\mathcal{J}/\mathcal{J}^{2}) \to
gr^{\bullet}_{\mathcal{J}}(\mathcal{O}_{X}) $$

*is bijective.*

The necessity of the conditions follows immediately from `(16.9.3)`. To see that the conditions are sufficient, it
suffices, by virtue of `(16.9.3)`, to show that if, at a point $x \in Supp(\mathcal{O}_{X}/\mathcal{J})$, there exist an
open neighbourhood $U$ of $x$ in $X$ and $n$ sections $f_{i}$ ($1 \leq i \leq n$) of $\mathcal{J}$ over $U$ whose
canonical images in $\mathcal{J}/\mathcal{J}^{2}$ form a basis of $(\mathcal{J}/\mathcal{J}^{2}) | U$ over
$(\mathcal{O}_{X}/\mathcal{J}) | U$, then there exists an open neighbourhood $V \subset U$ of $x$ such that the $f_{i} |
V$ generate $\mathcal{J} | V$. Now, by hypothesis, $\mathcal{J}_{x} \neq \mathcal{O}_{x}$, so that $\mathcal{J}_{x}$ is
contained in the maximal ideal of $\mathcal{O}_{x}$; since $\mathcal{J}_{x}$ is an $\mathcal{O}_{x}$-module of finite
type and the classes of the $(f_{i})_{x}$ in $\mathcal{J}_{x}/\mathcal{J}^{2}_{x}$ generate this
$(\mathcal{O}_{x}/\mathcal{J}_{x})$-module, Nakayama's lemma shows that the $(f_{i})_{x}$ generate $\mathcal{J}_{x}$.
Since $\mathcal{J}$ is of finite type, one concludes by $(0_{I}, 5.2.2)$.

**Corollary (16.9.5).**

<!-- label: IV.16.9.5 -->

*Let $X$ be a locally ringed space, $\mathcal{J}$ a quasi-regular Ideal of $\mathcal{O}_{X}$, $(f_{i})_{1 \leq i \leq
n}$ a sequence of sections of $\mathcal{J}$ over $X$, $x$ a point of $Supp(\mathcal{O}_{X}/\mathcal{J})$. The following
conditions are equivalent:*

*a) There exists an open neighbourhood $U$ of $x$ in $X$ such that the $f_{i} | U$ form a quasi-regular sequence of
elements of $\Gamma(U, \mathcal{O}_{X})$ generating $\mathcal{J} | U$.*

*b) The $(f_{i})_{x}$ form a system of generators of $\mathcal{J}_{x}$ of smallest possible cardinality.*

*b') The $(f_{i})_{x}$ form a minimal system of generators of $\mathcal{J}_{x}$.*

*c) If $\bar{f}_{i}$ is the canonical image of $f_{i}$ in $\Gamma(X, \mathcal{J}/\mathcal{J}^{2})$, the
$(\bar{f}_{i})_{x}$ form a basis of the $(\mathcal{O}_{x}/\mathcal{J}_{x})$-module
$\mathcal{J}_{x}/\mathcal{J}^{2}_{x}$.*

By hypothesis, $\mathcal{O}_{x}$ is a local ring and $\mathcal{J}_{x}$ is an ideal of finite type of $\mathcal{O}_{x}$
contained in the maximal ideal of $\mathcal{O}_{x}$; the equivalence of b), b') and c) thus follows from Nakayama's
lemma (Bourbaki, *Alg. comm.*, chap. II, §3, n° 2, prop. 5). It is clear that a) implies c) by virtue of `(16.9.3)`; on
the other hand, it follows from $(0_{I}, 5.2.2)$ that, if condition c) is verified (hence also b)), there exists an open
neighbourhood $U$ of $x$ in $X$ such that $(\mathcal{J}/\mathcal{J}^{2}) | U$ has constant rank $n$, and such that the
$f_{i} | U$ generate $\mathcal{J} | U$; it suffices then to apply, in $U$, the last assertion of `(16.9.3)`.

**Remarks (16.9.6).**

<!-- label: IV.16.9.6 -->

(i) Under the general hypotheses of `(16.9.5)`, it is not enough that the $(\bar{f}_{i})_{y}$ form a basis of the
$(\mathcal{O}_{y}/\mathcal{J}_{y})$-module $\mathcal{J}_{y}/\mathcal{J}^{2}_{y}$ for every $y \in X$ for the sequence
$(f_{i})$ to generate $\mathcal{J}$. One has an example by

<!-- original page 48 -->

taking $X = \operatorname{Spec}(A)$, where $A$ is a Dedekind ring, and $\mathcal{J} = \tilde{\mathfrak{J}}$, where
$\mathfrak{J}$ is a *non-principal* prime ideal of $A$; then $\mathcal{J}_{y}/\mathcal{J}^{2}_{y} = 0$ at every point
$y$ distinct from the point $x \in X$ corresponding to $\mathfrak{J}$, and $\mathcal{J}_{x}/\mathcal{J}^{2}_{x}$ has
rank `1` over the field $\mathcal{O}_{x}/\mathcal{J}_{x}$; moreover, $\mathcal{J}$ is clearly a regular Ideal.

(ii) In `(16.9.5)`, one cannot replace "quasi-regular" by "regular", even when $X$ is a prescheme (cf. `(16.9.12)`).
Indeed, let $B$ denote the ring of germs of infinitely differentiable functions at the point `0` of $\mathbb{R}$; it has
a maximal ideal $\mathfrak{m}$ generated by the germ $t$ of the identity map of $\mathbb{R}$ at the point `0`, and the
intersection $\mathfrak{n}$ of the $\mathfrak{m}^{k}$ for $k > 0$ is not reduced to `0`. Now let $A$ be the quotient
ring $B[T]/\mathfrak{n} T B[T]$, and let $f_{1}, f_{2}$ be the canonical images in $A$ of the elements $t$ and $T$ of
`B[T]`. The sequence $(f_{1}, f_{2})$ is *regular* in $A$: indeed, $f_{1}$ is not a zero-divisor in $A$, since the
relation $t P[T] \in \mathfrak{n} T B[T]$, for a polynomial $P \in B[T]$, entails that the products of $t$ by the
coefficients of $P$ belong to the ideal $\mathfrak{n}$, and it follows immediately that these coefficients are
themselves in $\mathfrak{n}$, hence $P[T] \in \mathfrak{n} T B[T]$. As $B/tB$ is isomorphic to $\mathbb{R}$, $A/f_{1} A$
is isomorphic to the polynomial ring $\mathbb{R}[T]$, hence integral, and the image of $f_{2}$ in $A/f_{1} A$, being
equal to $T$, is not a zero-divisor, which proves our assertion. However, $f_{2}$ is a zero-divisor in $A$, for, given
any non-zero element $x \in \mathfrak{n}$, the image of $x$ in $A$ is $\neq 0$, but the image of `xT` is zero. One
concludes that the sequence $(f_{2}, f_{1})$ is *not regular* in $A$; on the other hand, the ideal $\mathfrak{J} = f_{1}
A + f_{2} A$ is distinct from $A$, so conditions b), b') and c) of `(16.9.5)` do not imply condition a) when one
replaces "quasi-regular" by "regular".

**(16.9.7).**

<!-- label: IV.16.9.7 -->

If $X = \operatorname{Spec}(A)$ is an affine scheme, we shall say that an ideal $\mathfrak{J}$ of $A$ is *regular*
(resp. *quasi-regular*) if the Ideal $\mathcal{J} = \tilde{\mathfrak{J}}$ of $\mathcal{O}_{X}$ is regular (resp.
quasi-regular); note that this notion is *local* and does not in any way imply the existence of a system of generators
of $\mathfrak{J}$ forming in $A$ a regular (resp. quasi-regular) sequence, as the example `(16.9.6, (i))` shows;
however, this does hold when $A$ is local `(16.9.5)`.

Proposition `(16.9.4)` is translated in terms of quasi-regular immersions as follows:

**Proposition (16.9.8).**

<!-- label: IV.16.9.8 -->

*Let $j : Y \to X$ be a morphism of preschemes; for $j$ to be a quasi-regular immersion, it is necessary and sufficient
that $j$ satisfy the following conditions:*

*(i) $j$ is an immersion locally of finite presentation.*

*(ii) The conormal sheaf $gr^{1}(j) = \mathcal{N}_{Y/X}$ `(16.1.2)` is a locally free $\mathcal{O}_{Y}$-Module.*

*(iii) The canonical homomorphism `(16.1.2.2)`*

$$ \mathbb{S}^{\bullet}_{\mathcal{O}_{Y}}(gr^{1}(j)) \to gr^{\bullet}(j) $$

*is bijective.*

The question being local on $Y$, one may restrict to the case where $j$ is the canonical injection of a closed
sub-prescheme $Y$ of $X$, in which case the translation of `(16.9.4)` into `(16.9.8)` results from the description of
$gr^{1}(j)$ and $gr^{\bullet}(j)$ in terms of the Ideal $\mathcal{J}$ of $\mathcal{O}_{X}$ defining the sub-prescheme
$Y$ `(16.1.3, (ii))`.

**Corollary (16.9.9).**

<!-- label: IV.16.9.9 -->

*Let $Y$ be a prescheme, $X$ a $Y$-prescheme, $j : Y \to X$ a $Y$-section of $X$, so that the $n$-th normal invariant
$\mathcal{A}^{(n)}$ of $j$ `(16.1.2)` is an augmented $\mathcal{O}_{Y}$-Algebra `(16.1.7)`; set $\mathcal{A}^{(\infty)}
= \varprojlim \mathcal{A}^{(n)}$. For $j$ to be a quasi-regular immersion, it is necessary and sufficient that $j$ be
locally of finite presentation and that every $y \in Y$ admit an affine open neighbourhood $U$ of ring $C$ such that
$\mathcal{A}^{(\infty)} | U$ is isomorphic, as an augmented topological $\mathcal{O}_{U}$-Algebra, to
$\mathcal{O}_{U}[[T_{1}, \cdots, T_{n}]]$.*

One may restrict to the case where $j$ is a closed immersion by passing to a sufficiently small neighbourhood of $y$
(see the argument of `(16.4.11)`), and then $\mathcal{O}_{Y}$ is identified with a quotient Algebra
$\mathcal{O}_{X}/\mathcal{J}$ and the canonical surjective homomorphism $\mathcal{O}_{X} \to \mathcal{O}_{Y}$ admits a

<!-- original page 49 -->

right inverse `(16.1.7)`. One may therefore suppose $X = \operatorname{Spec}(B)$ and $Y = \operatorname{Spec}(A)$
affine, $B$ being an augmented $A$-algebra and the augmentation ideal $\mathfrak{J}$ being of finite type. Since
$\mathcal{A}^{(n)}$ is then identified with $(B/\mathfrak{J}^{n+1})^{\sim}$, the corollary follows from the equivalence
of b) and c) in `(0, 19.5.4)`, since $B/\mathfrak{J} = A$.

One notes that, in the affine case considered, the fact that $j$ is a quasi-regular immersion is moreover equivalent, by
virtue of `(0, 19.5.4)`, to the statement that $B$ is a *formally smooth* $A$-algebra for the $\mathfrak{J}$-preadic
topology.

One also notes that the condition that $j$ be an immersion locally of finite presentation is always satisfied when the
morphism $X \to Y$ is locally of finite type `(IV, 1.4.3, (v))`.

**Proposition (16.9.10).**

<!-- label: IV.16.9.10 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a sub-prescheme of $X$, $j : Y \to X$ the canonical injection, $y$ a
point of $Y$.*

*(i) For there to exist an open neighbourhood $U$ of $y$ in $X$ such that the restriction $Y \cap U \to U$ of $j$ is a
regular immersion, it is necessary and sufficient that the kernel $\mathcal{J}_{y}$ of the surjective homomorphism
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, y}$ be generated by a regular sequence of elements of $\mathcal{O}_{X, y}$.*

*(ii) For the immersion $j$ to be regular, it is necessary and sufficient that it be quasi-regular.*

(i) One may restrict to the case where $Y$ is a closed sub-prescheme of $X$ defined by a coherent Ideal $\mathcal{J}$ of
$\mathcal{O}_{X}$. The condition is obviously necessary. Conversely, if $\mathcal{J}_{y}$ is generated by a regular
sequence $(s_{i})_{y}$, where the $s_{i}$ are sections of $\mathcal{J}$ over an open neighbourhood $U$ of $y$ in $X$,
one may suppose that the $s_{i}$ generate $\mathcal{J} | U$ $(0_{I}, 5.2.2)$ and form a regular sequence `(0, 15.2.4)`,
whence the assertion.

(ii) The fact that a quasi-regular immersion is regular follows from (i) and from the identification of quasi-regular
sequences and regular sequences in $\mathcal{O}_{X, y}$ consisting of elements of the maximal ideal `(0, 15.1.11)`.

When (without Noetherian hypothesis on $X$) the kernel $\mathcal{J}$ of $\mathcal{O}_{X} \to \mathcal{O}_{Y}$ is
generated by a regular sequence of elements of $\mathcal{O}_{X}$, one says that the immersion $j$ is *regular at the
point $y$*.

**Corollary (16.9.11).**

<!-- label: IV.16.9.11 -->

*Let $X$ be a locally Noetherian prescheme; then every quasi-regular Ideal of $\mathcal{O}_{X}$ is regular.*

**Remarks (16.9.12).**

<!-- label: IV.16.9.12 -->

(i) One notes that a regular immersion is not in general a flat morphism, nor *a fortiori* a regular morphism in the
sense of `(IV, 6.8.1)`.

(ii) Let $A$ be a local Noetherian ring; it follows immediately from `(16.9.4)` and from `(0, 17.1.1)` that for $A$ to
be *regular*, it is necessary and sufficient that its maximal ideal $\mathfrak{m}$ be *quasi-regular* (or regular, which
amounts to the same since $A$ is Noetherian). For a Noetherian affine scheme $X$ to be *regular*, it is necessary and
sufficient that, for every closed point $x \in X$, the canonical injection $\operatorname{Spec}(\kappa(x)) \to X$ be a
*regular* immersion.

**Proposition (16.9.13).**

<!-- label: IV.16.9.13 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a sub-prescheme of $X$, $Y'$ a sub-prescheme of $Y$ such that the
canonical injection $j : Y' \to Y$ is regular. Then the sequence of $\mathcal{O}_{Y'}$-Modules*

$$ (16.9.13.1) 0 \to j*(\mathcal{N}_{Y/X}) \to \mathcal{N}_{Y'/X} \to \mathcal{N}_{Y'/Y} \to 0 $$

<!-- original page 50 -->

*is exact; moreover, for every $x \in X$, there exists an open neighbourhood $U$ of $x$ such that the restrictions to
$U$ of the homomorphisms in `(16.9.13.1)` form an exact and split sequence.*

Let us first prove the following lemma:

**Lemma (16.9.13.2).**

<!-- label: IV.16.9.13.2 -->

*Let $A$ be a ring, $\mathfrak{J}$ an ideal of $A$, $A' = A/\mathfrak{J}$, $(f_{i})_{1 \leq i \leq r}$ a sequence of
elements of $A$ which is $A'$-regular, $\mathfrak{K} = \sum_{i} f_{i} A$, $\mathfrak{L} = \mathfrak{J} + \mathfrak{K}$,
$\mathfrak{K}' = \sum_{i} f'_{i} A'$ (where $f'_{i}$ is the image of $f_{i}$ in $A'$), so that $C = A/\mathfrak{L}$ is
isomorphic to $A'/\mathfrak{K}'$. Then for every integer $n > 0$ and every integer $N \geq n$, one has the relation*

```text
  (16.9.13.3)    𝔍 ∩ 𝔎^n = 𝔍 𝔎^n + 𝔍 𝔎^N.
```

It clearly suffices to prove that every element of the left-hand side is contained in the right-hand side, and by
induction on $n$ one is reduced to the case $N = n + 1$. An element of the left-hand side of `(16.9.13.3)`, being in
$\mathfrak{K}^{n}$, is written $P(f_{1}, \cdots, f_{r})$, where $P \in A[T_{1}, \cdots, T_{r}]$ is homogeneous of degree
$n$. If $f'_{i}$ is the canonical image of $f_{i}$ in $A'$, the hypothesis $P(f_{1}, \cdots, f_{r}) \in \mathfrak{J}$
means that $P(f'_{1}, \cdots, f'_{r}) = 0$. But $P(f'_{1}, \cdots, f'_{r}) \in \mathfrak{K}'^{n}$, so the canonical
image of $P(f'_{1}, \cdots, f'_{r})$ in $\mathfrak{K}'^{n}/\mathfrak{K}'^{n+1}$ is zero. Now the hypothesis that the
sequence $(f'_{i})$ is $A'$-regular implies that the canonical homomorphism
$\mathbb{S}^{n}_{C}(\mathfrak{K}'/\mathfrak{K}'^{2}) \to \mathfrak{K}'^{n}/\mathfrak{K}'^{n+1}$ is bijective
`(0, 15.1.9)`; one concludes that the coefficients of $P$ belong to $\mathfrak{L} = \mathfrak{J} + \mathfrak{K}$. It
follows immediately that $P(f_{1}, \cdots, f_{r}) \in \mathfrak{J} \mathfrak{K}^{n} + \mathfrak{K}^{n+1}$, and since
$P(f_{1}, \cdots, f_{r}) \in \mathfrak{J}$, one finally has $P(f_{1}, \cdots, f_{r}) \in \mathfrak{J} \mathfrak{K}^{n} +
\mathfrak{J} \mathfrak{K}^{n+1}$, which proves the lemma.

Taking the quotient of the two sides of `(16.9.13.3)` by $\mathfrak{J} \mathfrak{K}^{n}$, one sees that the relations
`(16.9.13.3)` for $N \geq n$ entail

```text
  (16.9.13.4)    (𝔍 ∩ 𝔎^n)/𝔍 𝔎^n ⊂ ⋂_{N ≥ n} 𝔎^N · (A/(𝔍 𝔎^n)).
```

One deduces the

**Corollary (16.9.13.5).**

<!-- label: IV.16.9.13.5 -->

*Suppose the hypotheses of `(16.9.13.2)` are verified and, moreover, that the ring $A$ is Noetherian and that
$\mathfrak{K}$ is contained in the radical of $A$. Then for every integer $n > 0$,*

```text
  (16.9.13.6)    𝔍 ∩ 𝔎^n = 𝔍 𝔎^n.
```

Indeed, the right-hand side of `(16.9.13.4)` is then zero, since $A/\mathfrak{J} \mathfrak{K}^{n}$ is an $A$-module of
finite type (Bourbaki, *Alg. comm.*, chap. III, §3, n° 3, prop. 6).

Taking in particular $n = 2$ in `(16.9.13.6)`, and noting that one has $\mathfrak{L}^{2} = \mathfrak{J}^{2} +
\mathfrak{JK} + \mathfrak{K}^{2} = \mathfrak{JL} + \mathfrak{K}^{2}$; since $\mathfrak{JL} \subset \mathfrak{L}^{2}$,
one deduces

```text
  𝔍 ∩ 𝔏² = 𝔍𝔏 + (𝔍 ∩ 𝔎²) = 𝔍𝔏 + 𝔍 𝔎² = 𝔍𝔏,
```

in other words

$$ (16.9.13.7) \mathfrak{J} \cap \mathfrak{L}^{2} = \mathfrak{JL}, $$

which can also be expressed by saying that the canonical homomorphism

$$ \mathfrak{J}/\mathfrak{JL} \to (\mathfrak{J} + \mathfrak{K}^{2})/\mathfrak{K}^{2} $$

is bijective.

These lemmas being established, let us prove the first assertion of `(16.9.13)`: it clearly suffices

<!-- original page 51 -->

to prove that the sequence of stalks of the sheaves appearing in `(16.9.13.1)`, at a point $x \in Y'$, is exact. Now, on
setting $A = \mathcal{O}_{X, x}$, one can write $\mathcal{O}_{Y, x} = A' = A/\mathfrak{J}$, where $\mathfrak{J}$ is an
ideal contained in the maximal ideal of $A$, then $\mathcal{O}_{Y', x} = A'/\mathfrak{K}'$, where $\mathfrak{K}'$ is
generated by an $A'$-regular sequence of elements of $A'$, themselves images of elements of an $A'$-regular sequence of
elements of $A$ belonging to the maximal ideal of $A$. If $\mathfrak{K}$ is the ideal generated by the latter and
$\mathfrak{L} = \mathfrak{J} + \mathfrak{K}$, one has $\mathcal{O}_{Y', x} = A/\mathfrak{L}$, and since one is in the
situation of `(16.9.13.5)`, the canonical homomorphism $\mathfrak{J}/\mathfrak{JL} \to (\mathfrak{J} +
\mathfrak{K}^{2})/\mathfrak{K}^{2}$ is bijective. But this shows that the sequence

$$ 0 \to \mathfrak{J}/\mathfrak{JL} \to \mathfrak{L}/\mathfrak{L}^{2} \to
(\mathfrak{L}/\mathfrak{J})/(\mathfrak{L}/\mathfrak{J})^{2} \to 0 $$

is exact (see the proof of `(16.2.7)`), and the modules figuring in this sequence are precisely the stalks at $x$ of the
sheaves in `(16.9.13.1)`. The second assertion follows from the fact that $\mathcal{N}_{Y'/Y}$ is a locally free
$\mathcal{O}_{Y'}$-Module `(16.9.8)` and from Bourbaki, *Alg.*, chap. II, 3rd ed., §1, n° 11, prop. 21.

### 16.10. Differentially smooth morphisms

**Definition (16.10.1).**

<!-- label: IV.16.10.1 -->

*We say that a morphism of preschemes $f : X \to S$ is **differentially smooth** (or that $X$ is **differentially
smooth** over $S$) if it satisfies the following conditions:*

*(i) $\Omega^{1}_{X/S}$ is a locally projective $\mathcal{O}_{X}$-Module, that is, every point of $X$ admits an affine
open neighbourhood $U$ such that $\Gamma(U, \Omega^{1}_{X/S})$ is a projective $\Gamma(U, \mathcal{O}_{X})$-module (not
necessarily of finite type).*

*(ii) The canonical homomorphism `(16.3.1.1)`*

$$ \mathbb{S}^{\bullet}_{\mathcal{O}_{X}}(\Omega^{1}_{X/S}) \to gr^{\bullet}(\mathcal{P}_{X/S}) $$

*is bijective.*

*In particular, if $\Omega^{1}_{X/S}$ is locally free of finite rank, the $\mathcal{P}^{n}_{X/S}$ are locally free
$\mathcal{O}_{X}$-Modules of finite rank (being extensions of such Modules).*

We say that $f$ is *differentially smooth at a point $x \in X$* (or that $X$ is differentially smooth over $S$ at the
point $x$) if there exists an open neighbourhood $U$ of $x$ in $X$ such that $f | U$ is differentially smooth.

We shall see later `(17.12.4)` that a smooth morphism is differentially smooth, which justifies the terminology; but the
converse is not true. Indeed, a *monomorphism* $f : X \to S$ is differentially smooth, since $\Omega^{1}_{X/S} = 0$ by
virtue of `(I, 5.3.8)`, and consequently the surjective homomorphism `(16.3.1.1)` is clearly bijective; yet a
monomorphism is not even necessarily flat, hence *a fortiori* not necessarily smooth. Let us limit ourselves to noting
the following proposition:

**Proposition (16.10.2).**

<!-- label: IV.16.10.2 -->

*Let $A$ be a ring, $B$ a formally smooth $A$-algebra for the discrete topologies `(0, 19.3.1)`. Then
$\operatorname{Spec}(B)$ is differentially smooth over $\operatorname{Spec}(A)$.*

Indeed, $B \otimes_{A} B$ is then (for the discrete topologies) a formally smooth $B$-algebra (for either of the
canonical homomorphisms $b \mapsto b \otimes 1$, $b \mapsto 1 \otimes b$ of $B$

<!-- original page 52 -->

into $B \otimes_{A} B$) `(0, 19.3.5, (iii))`; hence $B \otimes_{A} B$ is also a formally smooth $A$-algebra for the
discrete topologies `(0, 19.3.5, (ii))`. On setting $\mathfrak{J} = \mathfrak{J}_{B/A}$, it follows that $B \otimes_{A}
B$ is also a formally smooth $A$-algebra for the $\mathfrak{J}$-preadic topology `(0, 19.3.8)`; since by hypothesis $B =
(B \otimes_{A} B)/\mathfrak{J}$ is a formally smooth $A$-algebra for the discrete topologies, the proposition follows
from the equivalence of a) and b) in `(0, 19.5.4)`.

**Proposition (16.10.3).**

<!-- label: IV.16.10.3 -->

*For a morphism $f : X \to S$ to be differentially smooth, it is necessary and sufficient that, for every $x \in X$,
there exist an affine open neighbourhood $U$ of $x$, of ring $A$, such that $\Gamma(U, \mathcal{P}^{\infty}_{X/S})$ is
an augmented topological $A$-algebra isomorphic to the completed algebra $\hat{B}$, where $B = \mathbb{S}_{A}(V)$, $V$
being a projective $A$-module and $B$ being endowed with the $B^{+}$-preadic topology (where $B^{+}$ is the augmentation
ideal). If $\Omega^{1}_{X/S}$ is locally free of finite rank, one may replace $\hat{B}$ by the formal power series
algebra $A[[T_{1}, \cdots, T_{n}]]$.*

The notion of a differentially smooth morphism being clearly local on $X$, one may restrict to the case where $S =
\operatorname{Spec}(B)$, $X = \operatorname{Spec}(C)$. Consider $C \otimes_{B} C$ as a $C$-algebra (via the first
factor); set $\mathfrak{J} = \mathfrak{J}_{C/B}$ and endow $C \otimes_{B} C$ with the $\mathfrak{J}$-preadic topology;
one may apply to the $C$-algebra $C \otimes_{B} C$ and to the ideal $\mathfrak{J}$ of $C \otimes_{B} C$ the equivalence
of b) and c) in `(0, 19.5.4)`, since $(C \otimes_{B} C)/\mathfrak{J} = C$ is obviously a formally smooth $C$-algebra for
the discrete topologies. The topology on $\Gamma(U, \mathcal{P}^{\infty}_{X/S})$ is clearly the projective limit
topology on this ring `(16.1.11)`.

One notes that the integer $n$ in the statement of `(16.10.3)` is the rank of $\Omega^{1}_{X/S}$ at the point $x$. We
shall see below `(17.13.5)` that, when $f$ is differentially smooth and locally of finite type, $n$ is moreover equal to
the dimension of the fibre $f^{-1}(f(x))$ at the point $x$.

**Proposition (16.10.4).**

<!-- label: IV.16.10.4 -->

*Let $f : X \to S$, $g : S' \to S$ be two morphisms, and set $X' = X \times_{S} S'$, $f' = f_{(S')} : X' \to S'$.*

*(i) If $f$ is differentially smooth, the same is true of $f'$.*

*(ii) Conversely, if $g$ is faithfully flat and quasi-compact, and if $f'$ is differentially smooth and
$\Omega^{1}_{X'/S'}$ is an $\mathcal{O}_{X'}$-Module of finite type, then $f$ is differentially smooth and
$\Omega^{1}_{X/S}$ is an $\mathcal{O}_{X}$-Module of finite type.*

Indeed, if $f$ is differentially smooth, the $gr_{n}(\mathcal{P}^{n}_{X/S})$ are flat $\mathcal{O}_{X}$-Modules;
consequently `(16.4.6)`, the homomorphism $gr_{n}(\mathcal{P}^{n}_{X/S}) \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'} \to
gr_{n}(\mathcal{P}^{n}_{X'/S'})$ is bijective for every $n$, and by virtue of the commutativity of the diagram
`(16.2.1.3)`, it follows from the definition `(16.10.1)` that $f'$ is differentially smooth. On the other hand, if $g$
is faithfully flat and quasi-compact, it again follows from `(16.4.6)` that $gr_{n}(\mathcal{P}^{n}_{X/S})
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'} \to gr_{n}(\mathcal{P}^{n}_{X'/S'})$ is bijective for every $n$. Suppose then
that $f'$ is differentially smooth and $\Omega^{1}_{X'/S'}$ of finite rank. Since the canonical projection $X' \to X$ is
faithfully flat and quasi-compact, it follows first from `(2.5.2)` that $\Omega^{1}_{X/S}$ is a locally free
$\mathcal{O}_{X}$-Module of finite rank, then from `(2.2.7)` that the canonical homomorphism `(16.3.1.1)` is bijective,
and therefore $f$ is differentially smooth.

**Proposition (16.10.5).**

<!-- label: IV.16.10.5 -->

*For a morphism locally of finite type $f : X \to S$ to be differentially smooth, it is necessary and sufficient that
the diagonal immersion $\Delta_{f} : X \to X \times_{S} X$ be quasi-regular.*

<!-- original page 53 -->

The question being local, one may restrict to the case where $S$ and $X$ are affine, in which case the diagonal
sub-prescheme of $X \times_{S} X$ is closed. The hypothesis that $f$ is locally of finite type entails that $\Delta_{f}$
is locally of finite presentation `(IV, 1.4.3.1)`, hence the diagonal sub-prescheme of $X \times_{S} X$ is defined by an
Ideal $\mathcal{J}$ of finite type, and $\Omega^{1}_{X/S} = \mathcal{J}/\mathcal{J}^{2}$ is an $\mathcal{O}_{X}$-Module
of finite type. The proposition then follows immediately from the comparison of the conditions of `(16.10.1)` and
`(16.9.4)`.

**Remark (16.10.6).**

<!-- label: IV.16.10.6 -->

Let $f : X \to S$ be a morphism such that the $\mathcal{O}_{X}$-Module $\Omega^{1}_{X/S}$ is locally free of finite
rank. It follows from `(0, 20.4.7)` that every $x \in X$ has an open neighbourhood $U$ such that there exists a finite
family $(z_{\lambda})_{\lambda \in L}$ of sections of $\mathcal{O}_{X}$ over $U$ for which $(dz_{\lambda})_{\lambda \in
L}$ forms a basis of the $\Gamma(U, \mathcal{O}_{X})$-module $\Gamma(U, \Omega^{1}_{X/S})$.

### 16.11. Differential operators on a differentially smooth $S$-prescheme

**(16.11.1).**

<!-- label: IV.16.11.1 -->

Let $f : X \to S$ be a morphism, $U$ an open set of $X$, and $(z_{\lambda})_{\lambda \in L}$ a family of sections of
$\mathcal{O}_{X}$ over $U$ such that the $dz_{\lambda}$ form a system of generators of $\Omega^{1}_{X/S} | U =
\Omega^{1}_{U/S}$. Let $m$ be an integer or the symbol $\infty$, and set, for every $\lambda$,

```text
  (16.11.1.1)    ζ_λ = δ z_λ = d^m z_λ − z_λ ∈ Γ(U, 𝒫^m_{X/S}).
```

We shall use the customary notations of analysis; for every $\mathbf{p} = (p_{\lambda}) \in \mathbb{N}^{(L)}$ (so that
$p_{\lambda} = 0$ except for finitely many indices), we set

```text
  (16.11.1.2)    |𝐩| = ∑_λ p_λ,    𝐩! = ∏_λ (p_λ!),
```

```text
  (16.11.1.3)    binom(𝐩, 𝐪) = 𝐩!/(𝐪!(𝐩 − 𝐪)!)    for 𝐩, 𝐪 in ℕ^{(L)}, 𝐪 ≤ 𝐩,
```

with the convention that $binom(\mathbf{p}, \mathbf{q}) = 0$ if $\mathbf{q} \nprec \mathbf{p}$,

```text
  (16.11.1.4)    𝐳^𝐩 = ∏_λ (z_λ)^{p_λ},    𝛇^𝐩 = ∏_λ (ζ_λ)^{p_λ}.
```

One thus has, with these notations,

```text
  (16.11.1.5)    d^m(𝐳^𝐩) = (d^m 𝐳)^𝐩 = (𝛇 + 𝐳)^𝐩 = ∑_{𝐪 ≤ 𝐩} binom(𝐩, 𝐪) 𝐳^{𝐩 − 𝐪} 𝛇^𝐪,
```

```text
  (16.11.1.6)    𝛇^𝐩 = (d^m 𝐳 − 𝐳)^𝐩 = ∑_{𝐪 ≤ 𝐩} (−1)^{|𝐩 − 𝐪|} binom(𝐩, 𝐪) 𝐳^{𝐩 − 𝐪} d^m(𝐳^𝐪).
```

Since the $dz_{\lambda}$ generate $\Omega^{1}_{X/S}$ and are the images of the $\delta z_{\lambda}$, and the canonical
homomorphism `(16.3.1.1)` is surjective, one concludes that, for finite $m$, the $\delta z_{\lambda}$ generate the
$\mathcal{O}_{U}$-Algebra $\mathcal{P}^{m}_{U/S}$ (Bourbaki, *Alg. comm.*, chap. III, §2, n° 8, cor. 2 of th. 1).
Therefore the $\epsilon^{\mathbf{p}}$ (for $|\mathbf{p}| \leq m$) generate the $\mathcal{O}_{U}$-Module
$\mathcal{P}^{m}_{U/S}$. A differential operator $D \in Diff^{m}_{U/S}$ is consequently entirely determined by the
values of $\langle \epsilon^{\mathbf{p}}, D\rangle$ for $|\mathbf{p}| \leq m$, or, what amounts to the same by
`(16.11.1.5)` and `(16.11.1.6)`, by the values

<!-- original page 54 -->

of the $\langle d^{m}(\mathbf{z}^{\mathbf{p}}), D\rangle = D(\mathbf{z}^{\mathbf{p}})$ for $|\mathbf{p}| \leq m$; more
precisely, it follows from `(16.11.1.5)` that one has

```text
  (16.11.1.7)    D(𝐳^𝐩) = ⟨d^m(𝐳^𝐩), D⟩ = ∑_{𝐪 ≤ 𝐩} binom(𝐩, 𝐪) ⟨𝛇^𝐪, D⟩ 𝐳^{𝐩 − 𝐪}.
```

**Theorem (16.11.2).**

<!-- label: IV.16.11.2 -->

*Let $f : X \to S$ be a morphism, $U$ an open set of $X$, $(z_{\lambda})_{\lambda \in L}$ a family of sections of
$\mathcal{O}_{X}$ over $U$ such that the family $(dz_{\lambda})_{\lambda \in L}$ generates $\Omega^{1}_{X/S} | U =
\Omega^{1}_{U/S}$. The following conditions are equivalent:*

*a) $f | U$ is differentially smooth and $(dz_{\lambda})$ is a basis of the $\mathcal{O}_{U}$-Module
$\Omega^{1}_{U/S}$.*

*b) There exists a family $(D_{\mathbf{p}})_{\mathbf{p} \in \mathbb{N}^{(L)}}$ of differential operators from
$\mathcal{O}_{U}$ into itself satisfying the conditions*

```text
  (16.11.2.1)    D_𝐩(𝐳^𝐪) = binom(𝐪, 𝐩) 𝐳^{𝐪 − 𝐩}    (𝐩, 𝐪 in ℕ^{(L)}).
```

*Moreover, when these conditions are verified, the family $(D_{\mathbf{p}})$ is uniquely determined by the conditions
`(16.11.2.1)` and satisfies the relations*

```text
  (16.11.2.2)    D_𝐩 ∘ D_𝐪 = D_𝐪 ∘ D_𝐩 = ((𝐩 + 𝐪)!/(𝐩! 𝐪!)) D_{𝐩 + 𝐪}    (𝐩, 𝐪 in ℕ^{(L)}).
```

*Finally, if $L$ is finite, then for every integer $m$ the $D_{\mathbf{p}}$ such that $|\mathbf{p}| \leq m$ form a basis
of the $\mathcal{O}_{U}$-Module $\mathcal{D}iff^{m}_{U/S}$; in other words, every differential operator of order $\leq
m$ on $U$ can be written in one and only one way in the form*

```text
  D = ∑_{|𝐩| ≤ m} a_𝐩 D_𝐩
```

*where the $a_{\mathbf{p}}$ are sections of $\mathcal{O}_{X}$ over $U$.*

Note first that, by virtue of `(16.11.1.6)` and `(16.11.1.5)`, one verifies immediately that the conditions
`(16.11.2.1)` are equivalent to

```text
  (16.11.2.3)    ⟨𝛇^𝐩, D_𝐪⟩ = δ_{𝐩 𝐪}    (Kronecker's symbol).
```

The existence of the family $(D_{\mathbf{p}})$ satisfying these relations first entails (on taking $|\mathbf{p}| = 1$)
that the $dz_{\lambda}$ are linearly independent, hence form a basis of the $\mathcal{O}_{U}$-Module $\Omega^{1}_{U/S}$.
Then, for every integer $m \geq 1$, one similarly deduces from `(16.11.2.3)` that the $\epsilon^{\mathbf{p}}$ such that
$|\mathbf{p}| \leq m$ are linearly independent; consequently the canonical homomorphism `(16.3.1.1)` is injective, hence
bijective, and this proves that b) implies a). The converse follows at once from the definition `(16.10.1)`: the fact
that the $\epsilon^{\mathbf{p}}$ form a basis of $\mathcal{P}^{m}_{U/S}$ for $|\mathbf{p}| \leq m$ entails the existence
and uniqueness of a family of homomorphisms $u_{\mathbf{q}, m} : \mathcal{P}^{m}_{U/S} \to \mathcal{O}_{U}$
($|\mathbf{q}| \leq m$) such that $\langle \epsilon^{\mathbf{p}}, u_{\mathbf{q}, m}\rangle = \delta_{\mathbf{p}
\mathbf{q}}$ for $|\mathbf{p}| \leq m$, $|\mathbf{q}| \leq m$. For a given value of $\mathbf{q}$, the differential
operators corresponding to the $u_{\mathbf{q}, m}$ for $m \geq |\mathbf{q}|$ are identified to a single operator
$D_{\mathbf{q}}$. This proves that a) implies b) and moreover that the family $(D_{\mathbf{p}})$ is uniquely determined,
and that, if $L$ is finite, for $|\mathbf{p}| \leq m$, the $D_{\mathbf{p}}$ form a basis of the dual
$\mathcal{D}iff^{m}_{U/S}$ of $\mathcal{P}^{m}_{U/S}$. Finally, the relations `(16.11.2.2)` follow at once from the
expression of the values of the three operators considered on the $\mathbf{z}^{\mathbf{r}}$, and from the fact that the
$\epsilon^{\mathbf{r}}$ for $|\mathbf{r}| \leq m$ generate $\mathcal{P}^{m}_{U/S}$.

<!-- original page 55 -->

**Remarks (16.11.3).**

<!-- label: IV.16.11.3 -->

(i) The fact that the $D_{\mathbf{p}}$ commute pairwise by virtue of `(16.11.2.2)` does not, of course, imply that the
$\mathcal{O}_{U}$-Algebra $\mathcal{D}iff_{U/S}$ is commutative, since the $D_{\mathbf{p}}$ commute with multiplication
by sections of $\mathcal{O}_{U}$ only when $n = 0$.

(ii) The indices $\mathbf{p}$ such that $|\mathbf{p}| = 1$ are the `𝛜_λ = (ε_{λμ})_{μ ∈ L}`, where $\epsilon_{\lambda
\mu} = 0$ if $\mu \neq \lambda$ and $\epsilon_{\lambda \lambda} = 1$; when $L$ is finite, the operators `D_{𝛜_λ}` are
none other than the $S$-derivations $D_{i}$ introduced in `(16.5.7)`. One notes that in general (and contrary to what
happens in classical analysis), it is not the case that a differential operator of arbitrary order can be written as a
linear combination of powers of the $D_{i}$ (cf. `(16.12)`).

(iii) For every integer $r \geq 1$, one can define the notion of a morphism *differentially smooth up to order $r$* by
replacing in `(16.10.1)` condition (ii) by the requirement that the homomorphisms

$$ \mathbb{S}^{m}_{\mathcal{O}_{X}}(\Omega^{1}_{X/S}) \to gr_{m}(\mathcal{P}^{m}_{X/S}) $$

be bijective for every $m \leq r$. The argument of `(16.11.2)` then shows that if, in condition a), one replaces
"differentially smooth" by "differentially smooth up to order $r$", this condition is equivalent to condition b)
restricted to $\mathbf{p} \in \mathbb{N}^{(L)}$, $\mathbf{q} \in \mathbb{N}^{(L)}$ with $|\mathbf{p}| \leq r$,
$|\mathbf{q}| \leq r$.

### 16.12. Case of characteristic zero — Jacobian criterion for differentially smooth morphisms

**(16.12.1).**

<!-- label: IV.16.12.1 -->

We say that a prescheme $X$ is *of characteristic $p$* ($p$ equal to `0` or to a prime number) if, for every affine open
set $U$ of $X$, the ring $\Gamma(U, \mathcal{O}_{X})$ is of characteristic $p$ `(0, 21.1.1)`. It follows from
`(0, 21.1.3)` that for $X$ to be of characteristic `0` it is necessary and sufficient that, for every closed point $x$
of $X$, the residue field $\kappa(x)$ is of characteristic `0`, or equivalently that $X$ can be endowed with a structure
of $\mathbb{Q}$-prescheme (necessarily unique).

**Theorem (16.12.2).**

<!-- label: IV.16.12.2 -->

*Let $X$ be a prescheme of characteristic `0`, $f : X \to S$ a morphism. If $\Omega^{1}_{X/S}$ is a locally free
$\mathcal{O}_{X}$-Module (not necessarily of finite type), then $f$ is differentially smooth.*

The question being local on $X$, one may suppose that there exists a family $(z_{\lambda})$ of sections of
$\mathcal{O}_{X}$ over $X$ such that $(dz_{\lambda})$ is a basis of the $\mathcal{O}_{X}$-Module $\Omega^{1}_{X/S}$.
Applying criterion `(16.11.2)`, it suffices to verify that the operators

```text
  D_𝐩 = (𝐩!)^{−1} ∏_λ D_λ^{p_λ}
```

(where the $D_{\lambda}$ are the coordinate forms corresponding to the basis $(dz_{\lambda})$) satisfy the relations
`(16.11.2.1)`, which is a consequence of the fact that the $D_{\lambda}$ are derivations.

**(16.12.3).**

<!-- label: IV.16.12.3 -->

The preceding theorem no longer holds if one drops the hypothesis that $X$ is of characteristic `0`. For example, if $S
= \operatorname{Spec}(k)$, where $k$ is a field of characteristic $p > 0$, $X = \operatorname{Spec}(K)$ where $K =
k(\alpha)$ with $\alpha \notin k$, $\alpha^{p} \in k$, one verifies immediately

<!-- original page 56 -->

that $\Omega^{1}_{X/S}$ is of rank `1`, and that the morphism $X \to S$ is differentially smooth up to order $p - 1$
`(16.11.3, (iii))`, but not up to order $p$. However, the proof of `(16.12.2)` shows that if $\Omega^{1}_{X/S}$ is
locally free, and if $n! \cdot 1_{\mathcal{O}_{X}}$ is invertible in $\Gamma(X, \mathcal{O}_{X})$, then $X$ is
differentially smooth over $S$ up to order $n$.

[^16.8-gabriel]: For a more general formalism, see Exposé VII of `[42]` (due to P. Gabriel).
