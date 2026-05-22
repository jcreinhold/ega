<!-- original page 147 -->

## §18. Complements on extensions of algebras

This section assembles a number of functorial constructions on rings which will be used repeatedly in §§19 and 20; it
contains no non-trivial result.

### 18.1. Inverse images of augmented rings

**(18.1.1)** Given a ring $A$ (not necessarily commutative), the category of $A$-*rings* has as objects the pairs $(B,
\rho)$ formed by a ring $B$ and a ring homomorphism $\rho : A \to B$, and as morphisms (also called $A$-*homomorphisms*)
the ring homomorphisms $u : B \to C$ such that, if $\rho : A \to B$ and $\sigma : A \to C$ are the homomorphisms (called
*structural*) defining the $A$-ring structure on $B$ and $C$ respectively, the diagram

```text
                                       u
                                  B ───────→ C
                                   ↖       ↗
                                   ρ       σ
(18.1.1.1)                            ↖   ↗
                                        A
```

is commutative. The kernel $\mathfrak{J}$ of $u$ is a two-sided ideal which is an $A$-bimodule (for $\rho$).

If $f : A' \to A$ is a ring homomorphism, then for every $A$-ring $(B, \rho)$, the pair $(B, \rho \circ f)$ is an
$A'$-ring, and if $u : B \to C$ is an $A$-homomorphism from the $A$-ring $(B, \rho)$

<!-- original page 148 -->

to the $A$-ring $(C, \sigma)$, it is also an $A'$-homomorphism from the $A'$-ring $(B, \rho \circ f)$ to the $A'$-ring
$(C, \sigma \circ f)$; one defines in this way a canonical functor from the category of $A$-rings to that of $A'$-rings.

**(18.1.2)** Let $B$, $E$, $F$ be three $A$-rings, and $f : E \to B$, $g : F \to B$ two $A$-homomorphisms. Recall that
one calls *fibre product* of $E$ and $F$ over $B$ (for the $A$-homomorphisms $f$ and $g$), and denotes by $E \times_{B}
F$, the sub-ring $G$ of the product ring $E \times F$ consisting of the pairs $(x, y)$ such that $f(x) = g(y)$; the
restrictions $p_{1} : G \to E$, $p_{2} : G \to F$ of the projections $pr_{1}$ and $pr_{2}$ to $G$ are still called the
*canonical projections*; the $A$-ring structure on $G$ is defined by the homomorphism $\alpha \mapsto (\rho(\alpha),
\sigma(\alpha))$ (where $\rho : A \to E$ and $\sigma : A \to F$ are the structural homomorphisms), which does send $A$
into $G$ by virtue of `(18.1.1)`. The characteristic property of $E \times_{B} F$ is that, for every pair of
$A$-homomorphisms $u : C \to E$, $v : C \to F$ such that $f \circ u = g \circ v$, there exists a unique $A$-homomorphism
$w : C \to G$ such that $u = p_{1} \circ w$, $v = p_{2} \circ w$. One may also say that $E \times_{B} F$ is the
*projective limit* of the projective system formed by $B$, $E$, $F$ and the $A$-homomorphisms $f$, $g$, in the category
of $A$-rings $(0_{III}, 8.1.9)$.

**(18.1.3)** Let $\mathfrak{J}$ be the two-sided ideal of $E$, kernel of $f$; it is immediate that the kernel
$\mathfrak{J}'$ of $p_{2} : G \to F$ is the ideal formed by the elements `(x, 0)` with $x \in \mathfrak{J}$; the
restriction $i_{1} : \mathfrak{J}' \to \mathfrak{J}$ of $p_{1}$ is thus an isomorphism of *rings without unit element*,
and also an isomorphism of $A$-bimodules. Likewise, if $\mathfrak{K}$ is the kernel of $g$, the kernel $\mathfrak{K}'$
of $p_{1} : G \to E$ is the ideal of elements `(0, y)` with $y \in \mathfrak{K}$, and the restriction $i_{2} :
\mathfrak{K}' \to \mathfrak{K}$ of $p_{2}$ is an isomorphism (in the same sense). Finally, it is clear that the kernel
of the $A$-homomorphism $q = f \circ p_{1} = g \circ p_{2}$ of $E \times_{B} F$ into $B$ is $\mathfrak{J}' \times
\mathfrak{K}' = \mathfrak{J}' \oplus \mathfrak{K}'$, so that one has the commutative diagram

```text
                            0           0          0
                            │           │          │
                            ↓           ↓          ↓
                                       i_2
                          𝔍' ⊕ 𝔎' ───→ 𝔎' ──────→ 𝔎
                            │           │          │
(18.1.3.1)                  │           ↓ j        ↓
                            │     q              p_1
                       0 ──→𝔍' ───────→ G ───────→ F  ──→ 0
                            │           │          │
                          i_1│       p_1│          │ g
                            ↓           ↓          ↓
                       0 ──→𝔍 ────────→ E ───────→ B  ──→ 0
                                       f
```

The definitions and results of `(18.1.2)` and `(18.1.3)` extend at once to the fibre product of an *arbitrary* family
$(E_{\lambda})_{\lambda \in I}$ of $A$-rings defined by a family of $A$-homomorphisms $f_{\lambda} : E_{\lambda} \to B$.
We leave the formulation of these results to the reader.

**(18.1.4)** In agreement with the terminology of `(M, VIII)`, we shall call an $A$-*ring augmented over* $B$ an
$A$-ring $E$ equipped with a surjective $A$-homomorphism (called the *augmentation* of $E$), $f : E \to B$; the kernel
$\mathfrak{J}$ of $f$ is called the *augmentation ideal*. One says that the augmented $A$-ring $E$ is *trivial* if there
exists an $A$-homomorphism of $A$-rings $s : B \to E$ which is a right inverse of the augmentation $f : E \to B$ (in
other words $f \circ s = 1_{B}$). The exact sequence of $A$-bimodules

$$ 0 \to \mathfrak{J} \to E \to B \to 0 $$

<!-- original page 149 -->

is then *split*; in other words, one can identify the $A$-bimodule $E$ with $B \times \mathfrak{J}$, and the
multiplication in $E$ is then given by

```text
                       (b, z)(b', z') = (bb', bz' + zb' + zz'),
```

$\mathfrak{J}$ being considered as a $B$-bimodule by means of $s : B \to E$.

**(18.1.5)** With the notations of `(18.1.2)`, suppose that the $A$-homomorphism $f$ is surjective, in other words that
it makes $E$ an augmented $A$-ring over $B$. Then it is clear that $p_{2} : G \to F$ is also surjective, in other words
defines on $G$ a structure of augmented $A$-ring over $F$, which one calls the *inverse image by* $g : F \to B$ *of the
augmented ring* $E$.

**Proposition (18.1.6).**

<!-- label: 0_IV.18.1.6 -->

*For the inverse image $G = E \times_{B} F$ by $g : F \to B$ of the augmented $A$-ring $E$ to be a trivial augmented
$A$-ring, it is necessary and sufficient that there exist an $A$-homomorphism $u : F \to E$ making commutative the
diagram*

```text
                                              F
                                            ↙ │
                                          u   │ g
                                          ↙   ↓
                                         E ──→ B
                                            f
```

The condition is evidently necessary, taking $u = p_{1} \circ s$, where $s : F \to G$ is an $A$-homomorphism right
inverse of $p_{2}$. Conversely, if there exists an $A$-homomorphism $u$ satisfying the condition of the statement, the
existence of the right inverse $s$ of $p_{2}$ follows from the universal property of the fibre product `(18.1.2)`
applied to the $A$-homomorphisms $u : F \to E$ and $1_{F} : F \to F$.

This result entails in particular that if $E$ is a trivial augmented ring, so are all its inverse images.

**(18.1.7)** Let us resume the situation described in `(18.1.2)` and `(18.1.3)`; we evidently have on $\mathfrak{K}$ a
structure of $G$-bimodule, coming from its structure of $F$-bimodule and from the ring homomorphism $p_{2} : G \to F$.
Since $i_{2}$ is bijective, we have furthermore an *injection* $\theta = j \circ i^{-1}_{2} : \mathfrak{K} \to G$, which
is a *homomorphism of* $G$-*bimodules*. We shall see conversely that, when one further assumes that $f$ and $g$ are
*surjective*, in other words that $E$ and $F$ are augmented $A$-rings over $B$, the datum of such a homomorphism
$\theta$ allows one to reconstitute the augmented ring $E$ (over $B$) from the augmented ring $G$ (over $F$).

More precisely, let us give ourselves an $A$-ring $F$ augmented over $B$ and an $A$-ring $G$ augmented over $F$, the
augmentation ideals being denoted by $\mathfrak{K}$ and $\mathfrak{J}'$ respectively:

```text
                                              0
                                              │
                                              ↓
                                              𝔎
                                          θ   │
                                              ↓
(18.1.7.1)               0 ──→ 𝔍' ──→ G ────→ F ──→ 0
                                          h
                                              │
                                              ↓ g
                                              B
                                              │
                                              ↓
                                              0
```

<!-- original page 150 -->

The homomorphism $h$ defines on all ideals of $F$ (and in particular on $\mathfrak{K}$) a structure of $G$-bimodule. Let
$\theta : \mathfrak{K} \to G$ be a homomorphism of $G$-bimodules making the diagram `(18.1.7.1)` commutative; this
implies that $\theta$ is injective and that $\mathfrak{J}' \cap \theta(\mathfrak{K}) = 0$; since $\theta(\mathfrak{K})$
is a two-sided ideal of $G$, and since $h(\theta(\mathfrak{K})) = \mathfrak{K}$, the composite homomorphism $g \circ h :
G \to B$ factors as $G \to G / \theta(\mathfrak{K}) \to B$, where $f$ is surjective; furthermore, the image
$\mathfrak{J}$ of $\mathfrak{J}'$ in $E = G / \theta(\mathfrak{K})$ is the kernel of $f$ (that of $g \circ h$ being
$\mathfrak{J}' \oplus \theta(\mathfrak{K})$), and the restriction to $\mathfrak{J}'$ of the canonical homomorphism $q :
G \to E$ is injective. One can therefore form the fibre product $G' = E \times_{B} F$, and since the two
$A$-homomorphisms $q : G \to E$ and $h : G \to F$ are such that $f \circ q = g \circ h$, they define a unique
$A$-homomorphism $u : G \to G'$ by the universal property of $G'$ `(18.1.2)`; we shall see that $u$ is bijective. It
suffices to prove this when $u$ is considered as a homomorphism of $A$-bimodules; one notes then that $u$ is compatible
with the finite filtrations on $G'$ and $G$ formed respectively by $G'$ and $\mathfrak{J}'' = Ker(G' \to F)$, and by $G$
and $\mathfrak{J}'$; furthermore, one has seen `(18.1.3)` that $gr_{0} u : F \to F$ is the identity and that $gr_{1} u :
\mathfrak{J}' \to \mathfrak{J}''$ is bijective, hence $u$ itself is bijective
`(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`.

### 18.2. Extensions of a ring by a bimodule

**(18.2.1)** Let $E$ be an augmented $A$-ring over $B$, $f : E \to B$ the augmentation, $\mathfrak{J} = Ker(f)$ the
augmentation ideal. If one has $\mathfrak{J}^{2} = 0$, then $\mathfrak{J}$ is not only an $E$-bimodule but also a
$B$-bimodule, since $B$ is isomorphic to $E/\mathfrak{J}$; more precisely, every $b \in B$ is of the form $f(x)$ with $x
\in E$, and if $z$, $z'$ are in $\mathfrak{J}$ one has $(x + z)z' = xz'$ (resp. $z'(x + z) = z'x$), so that the value of
`xz'` (resp. `z'x`) does not depend on the element $x \in f^{-1}(b)$, and can be written `bz'` (resp. `z'b`), which
defines the $B$-bimodule structure under consideration. Conversely, if $\mathfrak{J}$ is equipped with a structure of
$B$-bimodule such that $xz' = f(x)z'$ and $z'x = z'f(x)$ for $x \in E$ and $z' \in \mathfrak{J}$, it is clear that
$\mathfrak{J}^{2} = 0$.

**(18.2.2)** One calls an $A$-*extension of an $A$-ring* $B$ *by a $B$-bimodule* $L$ an exact sequence of homomorphisms
of $A$-bimodules

```text
                              0 → L ─→ E ─→ B → 0
                                    j     f
```

where $E$ is an $A$-ring, $f$ an $A$-homomorphism of rings, and one has, for $x \in E$ and $z \in L$,

```text
                        j(f(x) z) = x j(z),       j(z f(x)) = j(z) x,
```

whence it follows `(18.2.1)` that $j(L)$ is a two-sided ideal of square zero of $E$. By abuse of language one also says
that $E$ is an *extension* of $B$ by $L$. One says that two $A$-extensions $E$, $E'$ of $B$ by $L$ are $A$-*equivalent*
if there exists an isomorphism of $A$-rings $u : E \xrightarrow{\sim} E'$ (also called an $A$-*equivalence of
$A$-extensions*) making commutative the diagram

```text
                                            E
                                          ↗ │ ↘
                                        j   │u  f
                                          ↗ ↓ ↘
(18.2.2.1)                       0 → L         B → 0
                                          ↘ ↑ ↗
                                        j'  │   f'
                                          ↘ │ ↗
                                            E'
```

<!-- original page 151 -->

**(18.2.3)** One says that an $A$-extension $E$ of $B$ by a $B$-bimodule $L$ is $A$-*trivial* if $E$ is a trivial
augmented $A$-ring (over $B$) `(18.1.4)`. One defines on the product $A$-bimodule $B \times L$ a structure of $A$-ring
by setting $(x, s)(y, t) = (xy, xt + sy)$, as one verifies at once, and it is immediate that the canonical maps $j : L
\to B \times L$ and $f : B \times L \to B$ define an $A$-extension of $B$ by $L$ which is $A$-trivial, the canonical map
$g : B \to B \times L$ being an $A$-homomorphism right inverse of $f$. One says that this extension is the *trivial type
extension* of $B$ by $L$ and denotes it by $D_{B}(L)$; it is immediate that every $A$-trivial $A$-extension of $B$ by
$L$ is $A$-equivalent to $D_{B}(L)$.

One will note that every extension of the $A$-ring $A$ itself by an $A$-bimodule is necessarily $A$-trivial.

**(18.2.4)** Given two $A$-extensions $L \to E \to B$, $L' \to E' \to B'$, a *morphism* of the first to the second is by
definition a triple of homomorphisms of $A$-bimodules $(u, v, w)$ such that the diagram

```text
                              0 ──→ L ──→ E ──→ B ──→ 0
                                       j      f
(18.2.4.1)                          w │    u │    v │
                                      ↓      ↓      ↓
                              0 ──→ L' ─→ E' ─→ B' ─→ 0
                                       j'      f'
```

is commutative, $u$ and $v$ being $A$-homomorphisms of rings and $w$ being such that $w(bz) = v(b) w(z)$ and $w(zb) =
w(z) v(b)$ for $z \in L$ and $b \in B$ (in other words, the pair $(v, w)$ constitutes a *di-homomorphism* of the
$B$-bimodule $L$ into the $B'$-bimodule $L'$); it is clear that if `(u', v', w')` is a morphism from $L' \to E' \to B'$
to an $A$-extension $L'' \to E'' \to B''$, then $(u' \circ u, v' \circ v, w' \circ w)$ is still a morphism, which
justifies the terminology.

The consideration of the two commutative squares of the diagram `(18.2.4.1)` will lead us to two operations on
extensions of $A$-rings.

**(18.2.5)** In the first place, consider an $A$-extension $E'$ of $B'$ by $L'$

```text
                              0 → L' ─→ E' ─→ B' → 0
                                     j'     f'
```

and an $A$-homomorphism of rings $v : B \to B'$, and let $F = E' \times_{B'} B$ be the inverse image by $v$ of the
augmented $A$-ring $E'$ `(18.1.5)`, so that one has a commutative diagram

```text
                              0 ──→ L_0 ──→ F ──→ B ──→ 0
                                          p_1     p_2 │
                                        i ↓        ↓ v
                              0 ──→ L'  ──→ E' ──→ B' ──→ 0
                                          j'      f'
```

whose rows are exact, $p_{1}$ and $p_{2}$ being the canonical homomorphisms; one has seen `(18.1.3)` that $i$ is
bijective, and it also follows from the definition `(18.1.2)` that $L^{2}_{0} = 0$, so that one can consider $F$ as an
$A$-extension of $B$ by $L'$, which one calls the *inverse image by* $v$ *of the extension* $E'$ *of* $B'$ *by* $L'$
($L'$ being naturally considered as $B$-bimodule by means of the ring homomorphism $v$). The functorial

<!-- original page 152 -->

character of the fibre product with respect to each of the factors shows furthermore that if one has a morphism between
two extensions of $B'$

```text
                              0 ──→ L'_1 ──→ E'_1 ──→ B' ──→ 0
                                            g'        1_{B'} │
                                        h │       │          ↓
                                          ↓       ↓
                              0 ──→ L'_2 ──→ E'_2 ──→ B' ──→ 0
```

one deduces from it a morphism *inverse image by* $v$

```text
                          0 ──→ L'_1 ──→ E'_1 ×_{B'} B ──→ B ──→ 0
                              h │       g' ×_{B'} 1_B │     1_B │
                                ↓                     ↓         ↓
                          0 ──→ L'_2 ──→ E'_2 ×_{B'} B ──→ B ──→ 0
```

In particular, if $E'_{1}$ and $E'_{2}$ are $A$-equivalent $A$-extensions of $B'$ by $L'$, their inverse images by $v$
are $A$-equivalent $A$-extensions of $B$ by $L'$.

The definition of the fibre product shows that when one has a morphism `(18.2.4.1)` of $A$-extensions, it factors
through the inverse image of $E'$ by $v$; more precisely, there exists a unique $A$-homomorphism $u_{0} : E \to F = E'
\times_{B'} B$ making commutative the diagram

```text
                              0 ──→ L ──→ E ──→ B ──→ 0
                                    w_0│   u_0│   1_B │
                                       ↓      ↓      ↓
                              0 ──→ L_0 ─→ F ──→ B ──→ 0
                                          p_1     p_2 │
                                        i ↓        ↓ v
                              0 ──→ L' ──→ E' ──→ B' ──→ 0
                                          j'      f'
```

where $w_{0}$ is the restriction of $u_{0}$ to $L$ and $p_{1} \circ u_{0} = u$, $i \circ w_{0} = w$.

**(18.2.6)** Let us study in particular the inverse images of extensions by surjective $A$-homomorphisms. Consider a
surjective $A$-homomorphism $v : B \to B'$, an $A$-extension $F$ of $B$ by a $B$-bimodule $L$, and the two-sided ideal
$\mathfrak{K}$ of $B$, kernel of $v$ (which can be considered as $F$-bimodule by means of the augmentation $F \to B$);
one has seen `(18.1.7)` that every homomorphism of $F$-bimodules $\theta : \mathfrak{K} \to F$ making commutative the
diagram

```text
                                              𝔎
                                          θ   │
                                              ↓
                                         F ──→ B
```

determines an extension $E'$ of $B' = B / \mathfrak{K}$ by $L$ whose inverse image by $v : B \to B'$ is equivalent to
$F$, and that every $A$-extension $E'$ of $B'$ by $L$ having this latter property is obtained in this way (up to
$A$-equivalence). Furthermore, for two homomorphisms $\theta_{1}$, $\theta_{2}$ of $F$-bimodules from $\mathfrak{K}$
into $F$ to give two $A$-equivalent $A$-extensions of $B$ by $L$, it is necessary and sufficient that there exist an
$A$-equivalence $u$ of the $A$-extension $F$ onto itself such that

<!-- original page 153 -->

$\theta_{2} = u \circ \theta_{1}$; this follows at once from what was seen in `(18.2.5)` and from the definition of the
canonical bijection of $F$ onto the fibre product $E' \times_{B'} B$ `(18.1.7)`.

**(18.2.7)** Consider now the left square of `(18.2.4.1)`, and let us first recall the notion of *amalgamated sum* in
the category of $A$-bimodules: given three $A$-bimodules $X$, $Y$, $Z$ and two $A$-homomorphisms $f : X \to Y$,
$g : X \to Z$, the *amalgamated sum* $Y \oplus_{X} Z$ is the inductive limit of the inductive system formed by $X$, $Y$,
$Z$ and the $A$-homomorphisms $f$, $g$ in the category of $A$-bimodules $(0_{III}, 8.1.11)$. One defines this
$A$-bimodule as the quotient of the product $Y \times Z$ by the sub-$A$-bimodule $M$ image of $X$ under the homomorphism
$x \mapsto (f(x), -g(x))$. Its characteristic property is that, for every pair of homomorphisms of $A$-bimodules
$u : Y \to T$, $v : Z \to T$ such that $u \circ f = v \circ g$, there exists a unique homomorphism
$w : Y \oplus_{X} Z \to T$ such that $u = w \circ j_{1}$ and $v = w \circ j_{2}$, where $j_{1} : Y \to Y \oplus_{X} Z$
and $j_{2} : Z \to Y \oplus_{X} Z$ are the canonical maps.

**(18.2.8)** Consider now an $A$-extension $E$ of $B$ by a $B$-bimodule $L$:

$$ 0 \to L \to E \to B \to 0 $$

and on the other hand let $w : L \to L'$ be a homomorphism of $B$-bimodules. Let $H$ be the amalgamated sum $A$-bimodule
$E \oplus_{L} L'$; let us show how one can endow this $A$-bimodule with a structure of $A$-ring and define an
$A$-extension

$$ 0 \to L' \to H \to B \to 0. $$

For this, note that $L'$ is endowed with a structure of $E$-bimodule by means of the augmentation homomorphism $E \to
B$; one can therefore form the trivial type $A$-extension $G = D_{E}(L')$ `(18.2.3)`. Consider then the map $\theta : z
\mapsto (j(z), -w(z))$ from $L$ into $G$; this is a homomorphism of $G$-bimodules ($L$ being considered as $G$-bimodule
by means of the canonical homomorphism $p : G \to E$). Indeed, for $(x, z') \in G$ and $z \in L$, one has $(j(z),
-w(z))(x, z') = (j(z)x, j(z)z' - w(z)x)$; now $j(z)z' = f(j(z))z' = 0$ by definition of the $E$-bimodule structure on
$L'$, and $j(z)x = j(z f(x))$ and $w(z)x = w(z f(x))$; one verifies likewise that $\theta$ is a homomorphism of left
$G$-modules. One can then apply to the commutative diagram

```text
                                              0
                                              │
                                              ↓
                                              L
                                          θ   │
                                              ↓ j
                              0 ──→ L' ──→ G ──→ E ──→ 0
                                              │
                                              ↓ f
                                              B
                                              │
                                              ↓
                                              0
```

the result of `(18.1.7)`. As $H = G / \theta(L)$ by definition, our assertion is an immediate consequence of `(18.1.7)`.

<!-- original page 154 -->

One says that the $A$-extension $H$ of $B$ by $L'$ is *deduced from $E$ by means of the homomorphism* $w : L \to L'$.
The functorial character of the amalgamated sum in each of its summands shows furthermore that if one has a morphism of
extensions

```text
                              0 ──→ L ──→ E_1 ──→ B_1 ──→ 0
                                    1_L│    g │     h │
                                       ↓      ↓        ↓
                              0 ──→ L ──→ E_2 ──→ B_2 ──→ 0
```

one deduces from it canonically a morphism of extensions

```text
                          0 ──→ L' ──→ E_1 ⊕_L L' ──→ B_1 ──→ 0
                                1_{L'}│   g ⊕ 1_{L'}│     h │
                                      ↓             ↓        ↓
                          0 ──→ L' ──→ E_2 ⊕_L L' ──→ B_2 ──→ 0
```

In particular, if `E_1` and `E_2` are $A$-equivalent $A$-extensions of $B$ by $L$, the extensions of $B$ by $L'$ which
one deduces from them by means of $w$ are $A$-equivalent.

When one has a morphism `(18.2.4.1)` of $A$-extensions, it factors through the $A$-extension $H$ of $B$ by $L'$ deduced
from $E$ by means of the homomorphism $w : L \to L'$ ($L'$ being considered as $B$-bimodule by means of the homomorphism
$v : B \to B'$): indeed, the definition of the amalgamated sum shows that there exists a unique $A$-homomorphism
$u_{0} : H \to E'$ of $A$-bimodules, making commutative the diagram

```text
                              0 ──→ L ──→ E ──→ B ──→ 0
                                    j_1│    u_0│   1_B │
                                       ↓       ↓       ↓
                              0 ──→ L' ──→ H ──→ B ──→ 0
                                       j_0       f_0
                                    1_{L'}│   u_0│     v │
                                          ↓      ↓       ↓
                              0 ──→ L' ──→ E' ──→ B' ──→ 0
                                          j'      f'
```

with $u = u_{0} \circ j_{1}$, $w = j_{0} \circ w_{0}$, $j_{1}$ and $j_{2}$ being the canonical homomorphisms; one
verifies immediately that $u_{0}$ is also a ring homomorphism.

Let us finally note the functorial properties relative to trivial extensions:

**Proposition (18.2.9).**

<!-- label: 0_IV.18.2.9 -->

*Let $B$, $B'$ be two $A$-rings, $L$ a $B$-bimodule, $L'$ a $B'$-bimodule, $v : B \to B'$ an $A$-homomorphism of rings,
$w : L \to L'$ a homomorphism of $A$-bimodules such that $(v, w)$ is a di-homomorphism of bimodules. Then there exists a
unique $A$-homomorphism of rings $u : D_{B}(L) \to D_{B'}(L')$ making commutative the diagrams*

```text
                   D_B(L) ──→ D_{B'}(L')        D_B(L) ──→ D_{B'}(L')
                          u                            u
                       ↑                            ↑           ↑
                       │                            │           │
                       B  ───→  B'                  L  ───→     L'
                            v                            w
```

*where the vertical arrows are the canonical injections.*

<!-- original page 155 -->

Indeed, $u$ can only be the map $(x, s) \mapsto (v(x), w(s))$, and it remains to verify that this is an $A$-homomorphism
of rings, which results trivially from the definition `(18.2.3)`. One notes that $u$ also makes commutative the diagram

```text
                              D_B(L) ──→ D_{B'}(L')
                                     u
                                  │      │
                                  ↓      ↓
                                  B ───→ B'
                                       v
```

where this time the vertical arrows are the augmentations.

**Proposition (18.2.10).**

<!-- label: 0_IV.18.2.10 -->

*Let $B$ be an $A$-ring, $L$ a $B$-bimodule, $E$ an $A$-extension of $B$ by $L$. One defines a bijective map of the set
$G$ of homomorphisms of $B$-rings of $B$ into $E$ (in other words, the set of $A$-homomorphisms right inverse of the
augmentation $E \to B$) onto the set $G'$ of $A$-equivalences of $D_{B}(L)$ onto $E$ by making correspond to every $g
\in G$ the $A$-equivalence $g' : (x, s) \mapsto g(x) + s$; the inverse map makes correspond to every $g' \in G'$ the
$B$-homomorphism $x \mapsto g'(x, 0)$.*

This results at once from the definitions.

### 18.3. The group of classes of $A$-extensions

**(18.3.1)** Consider a fixed $A$-ring $B$ and a fixed $B$-bimodule $L$; then the relation "$E$ and $E'$ are
$A$-equivalent" between $A$-extensions $E$, $E'$ of $B$ by $L$ is an equivalence relation, and for this relation one can
speak of the *set of classes of $A$-equivalent $A$-extensions of $B$ by $L$*. To see this, it suffices to remark that
if, for every $x \in B$, $c_{x}$ is an element of $E$ whose image in $B$ is $x$, every $z \in E$ is written in a unique
way in the form $c_{x} + t$, where $t \in L$, and one can write $c_{x} + c_{y} = c_{x+y} + \phi(x, y)$, $c_{x} c_{y} =
c_{xy} + \psi(x, y)$, where $\phi(x, y)$ and $\psi(x, y)$ are elements of $L$, the maps $\phi$ and $\psi$ from $B \times
B$ to $L$ having to satisfy conditions expressing that $E$ is an $A$-ring, which it is pointless to write here. Every
$A$-extension of $B$ by $L$ is therefore $A$-equivalent to an $A$-extension of which $B \times L$ is the underlying set,
from which one draws our conclusion at once.

**(18.3.2)** The $A$-ring $B$ being fixed, let us provisionally denote by $T(L)$ the set of classes of $A$-extensions of
$B$ by $L$. For every $B$-homomorphism $w : L \to L'$ of $B$-bimodules, one defines canonically a map $T(w) : T(L) \to
T(L')$ by making correspond to the class of an $A$-extension $E$ of $B$ by $L$ the class of the $A$-extension $E
\oplus_{L} L'$ deduced from it by means of $w$, by virtue of `(18.2.8)`. If $w' : L' \to L''$ is a second homomorphism
of $B$-bimodules, one has in addition

```text
(18.3.2.1)                       T(w' ∘ w) = T(w') ∘ T(w).
```

Indeed, one knows that there exists a canonical isomorphism of $A$-bimodules

```text
                              E ⊕_L L'' ⥲ (E ⊕_L L') ⊕_{L'} L''
```

by virtue of the general properties of inductive limits (cf. for example `(I, 3.3.9)`), and it is immediate to verify
that this is indeed an $A$-equivalence of $A$-extensions, whence

<!-- original page 156 -->

the relation `(18.3.2.1)`. If $\mathcal{C}_{B}$ denotes the category of $B$-bimodules, one sees that one has thus
defined a covariant functor $T : \mathcal{C}_{B} \to Ens$.

**(18.3.3)** Consider now a family $(L_{\alpha})_{\alpha \in I}$ of $B$-bimodules and their product $L = \prod_{\alpha}
L_{\alpha}$; the projections $pr_{\alpha} : L \to L_{\alpha}$ define maps

$$ T(pr_{\alpha}) : T(L) \to T(L_{\alpha}), $$

whence a canonical map

```text
(18.3.3.1)                ∏_α T(pr_α) : T(L) → ∏_{α ∈ I} T(L_α).
```

We shall see that this map is bijective. Indeed, for every $\alpha \in I$, let $E_{\alpha}$ be an $A$-extension of $B$
by $L_{\alpha}$, and let $F$ be the fibre product of the $E_{\alpha}$ over $B$ `(18.1.3)`; it is immediate that $F$ is
an $A$-extension of $B$ by $L = \prod_{\alpha \in I} L_{\alpha}$ and that if one replaces each $E_{\alpha}$ by an
$A$-equivalent $A$-extension $E'_{\alpha}$, the fibre product $F'$ of the $E'_{\alpha}$ over $B$ is $A$-equivalent to
$F$. One has thus defined a map $\prod_{\alpha \in I} T(L_{\alpha}) \to T(L)$, and it is clear that this map is inverse
to `(18.3.3.1)`, whence our assertion. One will canonically identify $T(L)$ with $\prod_{\alpha \in I} T(L_{\alpha})$ by
the map `(18.3.3.1)`. One further verifies immediately that if $(L'_{\alpha})_{\alpha \in I}$ is a second family of
$B$-bimodules and, for each $\alpha$, $w_{\alpha} : L_{\alpha} \to L'_{\alpha}$ is a homomorphism of $B$-bimodules,
then, setting $w = \prod w_{\alpha} : L \to L' = \prod_{\alpha \in I} L'_{\alpha}$, $T(w)$ is identified with
$\prod_{\alpha \in I} T(w_{\alpha})$ when one makes the preceding identification.

**(18.3.4)** This being so, for a $B$-bimodule $L$, the addition is a homomorphism $s : L \times L \to L$ of
$B$-bimodules, and the same holds for the symmetry $t : L \to L$ of the additive law of $L$. One deduces from this a
composition law

```text
                              T(s) : T(L) × T(L) → T(L)
```

on $T(L)$ by virtue of `(18.3.3)`, and this law is a commutative group law of which $T(t)$ is the symmetry, as follows
from the definition of a group object by means of commutative diagrams $(0_{III}, 8.2.5 and 8.2.6)$. We shall denote by
$Exan_{A}(B, L)$ the commutative group thus defined and we shall say that it is the *group of classes of $A$-extensions
of $B$ by $L$*.

**(18.3.5)** Let us denote by $\mathcal{K}$ the category whose objects are the triples $(A, B, L)$ where $A$ is a ring,
$B$ an $A$-ring and $L$ a $B$-bimodule; the morphisms of this category are the triples $(u, v, w)$ where $u : A' \to A$
and $v : B' \to B$ are two ring homomorphisms making commutative the left square of the diagram

```text
                                  A ────→  B           L
                                u │      v │         w │
                                  ↑        ↑           ↓
                                  A' ───→  B'          L'
```

where the horizontal arrows are the structural homomorphisms; finally $w : L \to L'$ is a homomorphism of commutative
groups such that $w(v(b') z) = b' w(z)$ and

<!-- original page 157 -->

$w(z v(b')) = w(z) b'$ whatever $z \in L$ and $b' \in B'$ (in other words, $w$ is a homomorphism of $B'$-bimodules when
one endows $L$ with the $B'$-bimodule structure defined by $v$). The composition of morphisms is defined by $(u', v',
w') \circ (u, v, w) = (u \circ u', v \circ v', w' \circ w)$, which is justified at once. We propose to show that

```text
(18.3.5.1)                       (A, B, L) ↦ Exan_A(B, L)
```

*is a covariant functor from the category $\mathcal{K}$ to the category `Ab` of commutative groups.* It is thus a matter
of, for every triple $(u, v, w)$ as above, defining a homomorphism of commutative groups

```text
                  (u, v, w)_* : Exan_A(B, L) → Exan_{A'}(B', L').
```

By virtue of the definition of morphisms in $\mathcal{K}$, one can write

```text
                  (u, v, w) = (1_{A'}, 1_{B'}, w) ∘ (1_{A'}, v, 1_L) ∘ (u, 1_B, 1_L)
```

where, in the first factor, $L$ is endowed with its $B'$-bimodule structure defined by $v$; we shall therefore first
define $(u, v, w)_{*}$ when two of the homomorphisms $u$, $v$, $w$ are reduced to the identity.

**(18.3.6)** We shall take first for $(1_{A}, 1_{B}, w)_{*}$ the map

```text
(18.3.6.1)                 w_* : Exan_A(B, L) → Exan_A(B, L')
```

denoted $T(w)$ in `(18.3.2)`; it is immediate to verify that this is a group homomorphism, this property expressing
itself by the commutativity of diagrams, transformed by $T$ from analogous diagrams for $L$ and $L'$.

The map $(1_{A}, v, 1_{L})_{*}$ is the map

```text
(18.3.6.2)                   v^* : Exan_A(B, L) → Exan_A(B', L)
```

defined in the following way: if $E$ is an $A$-extension of $B$ by $L$, one has seen that $E \times_{B} B'$ is an
$A$-extension of $B'$ by $L$ `(18.2.5)`, and that if one replaces $E$ by an $A$-equivalent $A$-extension $E'$, $E'
\times_{B} B'$ is $A$-equivalent to $E \times_{B} B'$; the image by $v^{*}$ of the class of $E$ is the class of $E
\times_{B} B'$. One verifies at once that if $w : L \to L'$ is a homomorphism of $B$-bimodules, the diagram

```text
                              Exan_A(B, L)  ──→ Exan_A(B', L)
                                          v^*
                                  w_* │              │ w_*
                                      ↓              ↓
(18.3.6.3)
                              Exan_A(B, L') ──→ Exan_A(B', L')
                                          v^*
```

is commutative, $L$ and $L'$ being considered as $B'$-bimodules by means of $v$ in the right-hand column. Replacing $L$
and $L'$ respectively by $L \times L$ and $L$, and $w$ by the addition $s$ in $L$, one concludes that $v^{*}$ is indeed
a group homomorphism.

<!-- original page 158 -->

Finally, the map $(u, 1_{B}, 1_{L})_{*}$ is the map

```text
(18.3.6.4)                   u^* : Exan_A(B, L) → Exan_{A'}(B, L)
```

obtained by making correspond to an $A$-extension $E$ of $B$ by $L$ the ring $E$ considered as $A'$-ring by means of $u$
`(18.1.1)`, which is evidently an $A'$-extension of $B$ by $L$, $B$ being also considered as $A'$-ring by means of $u$;
it is clear that an $A$-equivalence is also an $A'$-equivalence, whence the map `(18.3.6.4)`, which, for every
homomorphism $w : L \to L'$ of $B$-bimodules, still makes commutative the diagram

```text
                              Exan_A(B, L) ──→ Exan_{A'}(B, L)
                                          u^*
                                  w_* │              │ w_*
                                      ↓              ↓
(18.3.6.5)
                              Exan_A(B, L') ─→ Exan_{A'}(B, L')
                                          u^*
```

from which one concludes as above that $u^{*}$ is a group homomorphism.

This being so, one sets $(u, v, w)_{*} = (1_{A}, 1_{B'}, w)_{*} \circ (1_{A'}, v, 1_{L})_{*} \circ (u, 1_{B},
1_{L})_{*}$, and one verifies easily, on account of the commutativity of the diagrams `(18.3.6.3)` and `(18.3.6.5)`,
that one has $(u \circ u', v \circ v', w' \circ w)_{*} = (u', v', w')_{*} \circ (u, v, w)_{*}$, which completes the
proof that `(18.3.5.1)` is a functor.

The existence of the group homomorphism `(18.3.6.1)` shows in particular that if $E$ is a trivial $A$-extension of $B$
by $L$, the extension $E \oplus_{L} L'$ of $B$ by $L'$ defined in `(18.2.8)` is also trivial, which one moreover
verifies without difficulty in a direct fashion.

On the other hand, for every element $z$ of the centre $Z$ of $B$, the homothety $h_{z} : y \mapsto yz = zy$ is an
endomorphism of the $B$-bimodule $L$, hence $(h_{z})_{*}$ is an endomorphism of the commutative group $Exan_{A}(B, L)$,
and by functoriality, these endomorphisms define on $Exan_{A}(B, L)$ a canonical structure of $Z$-module.

**(18.3.7)** Let $A$, $A'$ be two rings, $u : A' \to A$ a homomorphism, $B$ an $A$-ring and $L$ a $B$-bimodule. The
kernel of the group homomorphism

```text
                              u^* : Exan_A(B, L) → Exan_{A'}(B, L)
```

is formed by definition of the classes of $A$-extensions of $B$ by $L$ which are $A'$-trivial when one considers them as
$A'$-extensions by means of $u$. One denotes this kernel by the notation $Exan_{A/A'}(B, L)$ when this does not lead to
confusion.

If $\Lambda$ is a ring, and if one has a commutative diagram of $\Lambda$-homomorphisms of $\Lambda$-rings

```text
                                          B' ──→ B
(18.3.7.1)                                ↑       ↑
                                          │       │
                                          A' ──→ A
```

<!-- original page 159 -->

one deduces canonically homomorphisms

```text
(18.3.7.2)         Exan_{A/Λ}(B, L) → Exan_{A'/Λ}(B, L) → Exan_{A'/Λ}(B', L)
```

which come from the commutativity of the diagram

```text
                      Exan_Λ(B, L) ──→ Exan_{A'}(B, L) ──→ Exan_{A'}(B', L)
                            │                │                    │
                            ↓                ↓                    ↓
                      Exan_A(B, L)  ──→  Exan_A(B, L) ──→ Exan_A(B', L)
```

where the arrows are deduced from those of `(18.3.7.1)` by functoriality.

**Proposition (18.3.8).**

<!-- label: 0_IV.18.3.8 -->

*Let $B$ be a ring, $\mathfrak{J}$ a two-sided ideal of $B$, $C = B / \mathfrak{J}$ the quotient ring; $\mathfrak{J} /
\mathfrak{J}^{2}$ is then canonically endowed with a structure of $C$-bimodule. For every $C$-bimodule $L$, let
$\operatorname{Hom}_{C}(\mathfrak{J} / \mathfrak{J}^{2}, L)$ be the additive group of homomorphisms of $C$-bimodules
from $\mathfrak{J} / \mathfrak{J}^{2}$ to $L$. One then defines a canonical isomorphism of commutative groups*

```text
(18.3.8.1)                  η_L : Hom_C(𝔍 / 𝔍^2, L) ⥲ Exan_B(C, L)
```

*by making correspond to every $C$-homomorphism $w : \mathfrak{J} / \mathfrak{J}^{2} \to L$ (which is a fortiori a
$B$-homomorphism) the class of the extension $(B / \mathfrak{J}^{2}) \oplus_{\mathfrak{J} / \mathfrak{J}^{2}} L$ deduced
from the extension $B / \mathfrak{J}^{2}$ of $C$ by $\mathfrak{J} / \mathfrak{J}^{2}$ by means of $w$; the inverse
isomorphism makes correspond to the class of a $B$-extension $E$ of $C$ by $L$ the homomorphism $w$ such that the
composite $\mathfrak{J} \to \mathfrak{J} / \mathfrak{J}^{2} \to L$ is the restriction to $\mathfrak{J}$ of the
structural homomorphism $B \to E$.*

Let $F = B / \mathfrak{J}^{2}$, which is a $B$-extension of $C$ by $\mathfrak{J} / \mathfrak{J}^{2}$. For every
$B$-extension $0 \to L \to E \to C \to 0$ of $C$ by $L$, the structural homomorphism $f : B \to E$ is such that the
composite $B \to E \to C$ is the canonical homomorphism $B \to B / \mathfrak{J} = C$. As the image of $\mathfrak{J}$ by
$p \circ f$ is null, $f(\mathfrak{J})$ is contained in the kernel of $p$, that is $j(L)$, and as $j(L)$ is of square
zero, one has $f(\mathfrak{J}^{2}) = 0$; hence $f$ factors as $B \to B / \mathfrak{J}^{2} = F \to E$, and if $w$ is the
restriction of $u$ to $\mathfrak{J} / \mathfrak{J}^{2}$, one has a commutative diagram

```text
                              0 ──→ 𝔍 / 𝔍^2 ──→ F ──→ C ──→ 0
                                          w │      u │   1_C │
                                            ↓        ↓        ↓
                              0 ──→ L ──→ E ──→ C ──→ 0
                                        j     p
```

in other words $(u, 1_{C}, w)$ is a morphism of extensions `(18.2.4)`. One deduces from it a morphism of extensions

```text
                              0 ──→ L ──→ E' ──→ C ──→ 0
                                    1_L│    u' │   1_C │
                                       ↓       ↓        ↓
                              0 ──→ L ──→ E ──→ C ──→ 0
```

<!-- original page 160 -->

where $E' = F \oplus_{\mathfrak{J} / \mathfrak{J}^{2}} L$ `(18.2.8)`; it is a matter of proving that $u'$ is a
$B$-equivalence, which will establish that $\eta_{L}$ is bijective. By virtue of the construction made in `(18.2.8)`,
everything comes down to proving (taking account of `(18.1.7)`) that the inverse image $G$ of the extension $E$ of $C$
by the canonical homomorphism $g : F \to C$ is $F$-trivial, which is evident since $g$ factors as $F \to E \to C$
`(18.1.6)`.

It remains to see that $\eta_{L}$ is a group homomorphism; now, for every $B$-homomorphism $h : L \to L'$, it is
immediate that the diagram

```text
                                              η_L
                              Hom_C(𝔍 / 𝔍^2, L)  ─⥲  Exan_B(C, L)
                                       │                   │
                              Hom(1, h)│                h_*│
                                       ↓                   ↓
                              Hom_C(𝔍 / 𝔍^2, L') ─⥲  Exan_B(C, L')
                                              η_{L'}
```

is commutative. It suffices to apply this remark to the homomorphism $L \times L \to L$ defining the addition to
conclude.

### 18.4. Extensions of algebras

**(18.4.1)** Let $A$ be a commutative ring. The category of $A$-*algebras* is then a full subcategory of that of
$A$-rings, characterized by the fact that the structural homomorphisms $\rho : A \to B$ are *central*.

If $B$ is an $A$-algebra and $L$ a $B$-bimodule, it is immediate that the trivial type $A$-extension $D_{B}(L)$ is an
$A$-algebra. Likewise, in the construction of `(18.2.5)` (resp. of `(18.2.8)`), if $B$, $B'$ and $E'$ (resp. $B$ and
$E$) are $A$-algebras, the same holds for $E' \times_{B'} B$ (resp. for $E \oplus_{L} L'$). Finally, it is clear that if
$B$ is an $A$-algebra and $E$ an $A$-extension of $B$ by a $B$-bimodule $L$ which is an $A$-algebra, every $A$-extension
of $B$ by $L$, $A$-equivalent to $E$, is also an $A$-algebra. One then deduces at once from the definition `(18.3.4)`
that the classes of equivalent $A$-extensions of $B$ by $L$ which are $A$-algebras form a subgroup, denoted $Exal_{A}(B,
L)$, of $Exan_{A}(B, L)$. Let $\mathcal{K}'$ be the full subcategory of the category $\mathcal{K}$ defined in
`(18.3.5)`, whose objects $(A, B, L)$ are such that $A$ is commutative and $B$ an $A$-algebra. Then what precedes shows
that

```text
                                   (A, B, L) ↦ Exal_A(B, L)
```

*is a covariant functor from $\mathcal{K}'$ to `Ab`*. The results of `(18.3.7)` are unchanged when one replaces `Exan`
by `Exal` everywhere.

**(18.4.2)** Suppose always the ring $A$ commutative. The remarks of `(18.4.1)` remain valid when one replaces "algebra"
by "commutative algebra" and "bimodule" by "module". If $B$ is a commutative $A$-algebra and $L$ a $B$-module,

<!-- original page 161 -->

the classes of equivalent $A$-extensions of $B$ by $L$ which are commutative $A$-algebras (or, what comes to the same
thing, commutative $A$-rings) form a subgroup of $Exal_{A}(B, L)$, denoted $Exalcom_{A}(B, L)$. If $\mathcal{K}''$ is
the full subcategory of $\mathcal{K}'$ formed by the triples $(A, B, L)$ where $A$ and $B$ are commutative and $L$ is a
$B$-module,

```text
                              (A, B, L) ↦ Exalcom_A(B, L)
```

is still a covariant functor from $\mathcal{K}''$ to `Ab`. One can also in `(18.3.7)` replace `Exan` by `Exalcom`
everywhere. Finally, if in `(18.3.8)` one supposes that $B$ is a commutative ring and that $L$ is a $C$-module, the same
reasoning gives a canonical isomorphism

```text
(18.4.2.1)                 Hom_C(𝔍 / 𝔍^2, L) ⥲ Exalcom_B(C, L)
```

where the first member is the group of homomorphisms of $C$-module.

**(18.4.3)** Let $A$ be a commutative ring. An important case of extensions of $A$-algebras is formed by the
$A$-algebras $E$, extensions of an $A$-algebra $B$ by a $B$-bimodule $L$, such that $E$, as an $A$-module, is a trivial
extension of the $A$-module $B$ by the $A$-module $L$; in other words, the exact sequence of $A$-modules $0 \to L \to E
\to B \to 0$ is split. One then says that $E$ is an *extension of Hochschild* of $B$ by $L$. This will always be the
case when $B$ is a projective $A$-module, and in particular when $A$ is a commutative field. As an $A$-module, one can
identify $E$ with $B \times L$, the multiplication in $E$ being given by $(x, s)(y, t) = (xy, xt + sy + f(x, y))$ with
$f(x, y) \in L$. If one writes that this multiplication defines on $B \times L$ a structure of $A$-algebra, one finds
`(M, XIV, 2)` that $f$ must be an $A$-bilinear map of $B \times B$ into $L$, such that

```text
(18.4.3.1)                f(xy, z) + f(x, y) z = x f(y, z) + f(x, yz)
```

in other words, $f$ is a *2-cocycle on $B$ with values in $L$*, in the sense of Hochschild; for the extension $E$ to be
$A$-trivial, it is necessary and sufficient that one have

```text
(18.4.3.2)                  f(x, y) = x g(y) − g(xy) + g(x) y
```

where $g$ is an $A$-linear map of $B$ into $L$, in other words $f$ must be a *2-coboundary in the sense of Hochschild*.
One deduces at once that the classes of Hochschild extensions of $B$ by $L$ form a subgroup of $Exal_{A}(B, L)$,
isomorphic to the *Hochschild cohomology* group $H^{2}_{A}(B, L)$.

If $B$ is a commutative $A$-algebra, and $L$ a $B$-module, the commutative Hochschild extensions of $B$ by $L$
correspond to the *symmetric 2-cocycles*, that is to say those such that $f(y, x) = f(x, y)$. The classes of commutative
Hochschild extensions of $B$ by $L$ therefore form a subgroup of $Exalcom_{A}(B, L)$, isomorphic to the subgroup of
$H^{2}_{A}(B, L)$ image of the group of symmetric 2-cocycles, which we shall denote $H^{2}_{A}(B, L)^{s}$.

**(18.4.4)** Let us limit ourselves to the case where $A$ and $B$ are commutative and $L$ a $B$-module, and recall in
this case the equivalent definition of the Hochschild cohomology groups $H^{i}_{A}(B, L)$ `(M, IX, 6)`. One considers a
complex $P_{\bullet} = (P_{n})_{n \geq 0}$ of $B$-modules, where $P_{n} = B^{\otimes (n+1)} = B \otimes_{A} B
\otimes_{A} \cdots \otimes_{A} B$ ($n + 1$ times), the $B$-module structure being defined

<!-- original page 162 -->

by $x(y_{1} \otimes \cdots \otimes y_{n+1}) = (x y_{1}) \otimes y_{2} \otimes \cdots \otimes y_{n+1}$; the boundary, of
degree $-1$, $d_{n} : P_{n} \to P_{n-1}$, is defined by

```text
d_n(x_1 ⊗ x_2 ⊗ ⋯ ⊗ x_{n+1}) = (x_1 x_2) ⊗ x_3 ⊗ ⋯ ⊗ x_{n+1}
                              − x_1 ⊗ (x_2 x_3) ⊗ ⋯ ⊗ x_{n+1} + ⋯
                              + (−1)^{n−1} x_1 ⊗ x_2 ⊗ ⋯ ⊗ (x_n x_{n+1})
                              + (−1)^n (x_{n+1} x_1) ⊗ x_2 ⊗ ⋯ ⊗ x_n
```

which is indeed $B$-linear since $B$ is commutative.

A 2-cocycle of this complex with values in $L$ is a $B$-linear map $h$ of $B \otimes B \otimes B$ into $L$ such that
$h(d_{3}(x \otimes y \otimes z \otimes t)) = 0$; but as $h(x \otimes y \otimes z) = x h(1 \otimes y \otimes z)$, the
cocycle $h$ is determined by the $A$-bilinear map $(y, z) \mapsto f(y, z) = h(1 \otimes y \otimes z)$ of $B \times B$
into $L$, and on writing the preceding condition for $h$, one recovers for $f$ the condition `(18.4.3.1)`. Likewise, a
2-coboundary will be a map of the form $x \otimes y \otimes z \mapsto h'(d_{2}(x \otimes y \otimes z))$, where $h' : B
\otimes_{A} B \to L$ is linear, and here again $h'$ is determined by the $B$-linear map $g : y \mapsto h'(1 \otimes y)$
of $B$ into $L$; one then obtains $h'(d_{2}(1 \otimes x \otimes y)) = x g(y) - g(xy) + y g(x)$, which gives `(18.4.3.2)`
again. One proceeds likewise for every $i$, and one thus sees that one has

```text
(18.4.4.1)                      H^i_A(B, L) = H^i(Hom_B(P_•, L)).
```

**(18.4.5)** Under the conditions of `(18.4.4)`, one can interpret in the same way the group $H^{2}_{A}(B, L)^{s}$
`(18.4.3)`. For this, let us modify the complex $P_{\bullet}$ in degree `3`, by considering a new complex

```text
                                P'_• : P'_3 ──→ P_2 ──→ P_1;
                                            d'_3      d_2
```

we shall take $P'_{3} = P_{3} \oplus (B \otimes_{A} B \otimes_{A} B)$, $d'_{3}$ coinciding with $d_{3}$ on `P_3`, and
being given on $B \otimes_{A} B \otimes_{A} B$ by

```text
                                d'_3(x ⊗ y ⊗ z) = x ⊗ y ⊗ z − x ⊗ z ⊗ y.
```

The relation $d_{2} d'_{3} = 0$ follows from the commutativity of $B$. With the notations introduced above, a 2-cocycle
of $P'_{\bullet}$ now corresponds to an $A$-bilinear map $f : B \times B \to L$ which is *symmetric* and satisfies
`(18.4.3.1)`; consequently, one has

```text
                                H^2_A(B, L)^s = H^2(Hom_B(P'_•, L)).
```

**(18.4.6)** In the particular case where one considers a commutative field $k$, an extension $K$ of $k$, one has
$Ext^{1}_{k}(M, L) = 0$ whatever the $K$-vector spaces $L$, $M$, and consequently `(M, VI, 3.3 a))`, one has a canonical
isomorphism

```text
(18.4.6.1)                      H^i_k(K, L) ⥲ Hom_K(H_i(P_•), L)
```

and likewise

```text
(18.4.6.2)                      H^2_k(K, L)^s ⥲ Hom_K(H_2(P'_•), L).
```

### 18.5. Case of topological rings

**(18.5.1)** Let $A$, $B$ be two topological rings whose topology is linear, $\rho : A \to B$ a continuous homomorphism,
$L$ a topological $B$-bimodule, and suppose that there exists an open two-sided ideal $\mathfrak{K}_{0}$ of $B$ such
that $\mathfrak{K}_{0} \cdot L = L \cdot \mathfrak{K}_{0} = 0$, so that $L$ can be

<!-- original page 163 -->

considered as a $(B / \mathfrak{K})$-bimodule for every open ideal $\mathfrak{K} \subset \mathfrak{K}_{0}$. Let then
$\mathfrak{K} \subset \mathfrak{K}_{0}$ be an open two-sided ideal of $B$, $\mathfrak{J}$ an open two-sided ideal of $A$
such that $\rho(\mathfrak{J}) \subset \mathfrak{K}$, so that $B / \mathfrak{K}$ can be considered as a discrete $(A /
\mathfrak{J})$-ring. The preceding remark proves that the group $Exan_{A/\mathfrak{J}}(B / \mathfrak{K}, L)$ is defined;
furthermore, if $\mathfrak{K}' \subset \mathfrak{K}$, $\mathfrak{J}' \subset \mathfrak{J}$ are two open two-sided ideals
of $A$ and $B$ respectively such that $\rho(\mathfrak{J}') \subset \mathfrak{K}'$, one has by `(18.3.5.1)` a canonical
homomorphism

```text
(18.5.1.1)                Exan_{A/𝔍}(B / 𝔎, L) → Exan_{A/𝔍'}(B / 𝔎', L).
```

The set of pairs of open ideals $(\mathfrak{J}, \mathfrak{K})$ such that $\rho(\mathfrak{J}) \subset \mathfrak{K}
\subset \mathfrak{K}_{0}$ is evidently right-filtered for the relation "$\mathfrak{J} \supset \mathfrak{J}'$ and
$\mathfrak{K} \supset \mathfrak{K}'$", and the maps `(18.5.1.1)` define an inductive system of additive groups with this
set as indexing set. One sets, by abuse of notation (for it is no longer a question of a group in natural bijective
correspondence with a set of extensions)

```text
(18.5.1.2)               Exantop_A(B, L) = lim Exan_{A/𝔍}(B / 𝔎, L).
                                         ─────→
```

To say that the second member of `(18.5.1.2)` is zero therefore means that, for every pair of open ideals $\mathfrak{J}
\subset A$, $\mathfrak{K} \subset B$ such that $\rho(\mathfrak{J}) \subset \mathfrak{K} \subset \mathfrak{K}_{0}$ and
every $(A / \mathfrak{J})$-extension $E$ of $B / \mathfrak{K}$ by $L$, there exist two open ideals $\mathfrak{J}'
\subset \mathfrak{J}$, $\mathfrak{K}' \subset \mathfrak{K}$ such that $\rho(\mathfrak{J}') \subset \mathfrak{K}'$ and
that the inverse image by the homomorphism $B / \mathfrak{K}' \to B / \mathfrak{K}$ of $E$ is trivial.

We leave to the reader the analogous definition of the inductive limits $Exaltop_{A}(B, L)$, $Exalcotop_{A}(B, L)$
starting from $Exal_{A/\mathfrak{J}}(B / \mathfrak{K}, L)$ and $Exalcom_{A/\mathfrak{J}}(B / \mathfrak{K}, L)$, for the
case where $A$ is commutative and $B$ a topological $A$-algebra (resp. commutative $A$-algebra).

**(18.5.2)** If one has a commutative diagram of continuous homomorphisms of rings

```text
                                          B' ──→ B
                                          ↑       ↑
                                          │       │
                                          A' ──→ A
```

one deduces from it canonically two homomorphisms of additive groups

```text
                 Exantop_A(B, L) → Exantop_{A'}(B, L) → Exantop_{A'}(B', L)
```

by passage to the inductive limit starting from `(18.3.5.1)`.

By virtue of the exactness of the functor `lim` in the category of commutative groups, the kernel of the homomorphism

```text
                            Exantop_A(B, L) → Exantop_{A'}(B, L)
```

is the inductive limit of the kernels of the homomorphisms

```text
                          Exan_{A/𝔍}(B / 𝔎, L) → Exan_{A'/𝔍'}(B / 𝔎, L)
```

where one has taken for $\mathfrak{J}'$ the inverse image of $\mathfrak{J}$; one denotes this kernel by
$Exantop_{A/A'}(B, L)$. One defines similarly $Exaltop_{A/A'}(B, L)$ and $Exalcotop_{A/A'}(B, L)$. Finally, if one has a
homomorphism

<!-- original page 164 -->

continuous of $B$-bimodules $L \to L'$, one deduces from it canonically a homomorphism of additive groups

```text
                       Exantop_A(B, L) → Exantop_A(B, L')
```

by passage to the inductive limit starting from `(18.3.6.1)`.

**(18.5.3)** Given a topological ring $C$ and two topological $C$-bimodules $M$, $N$, one denotes by
$\operatorname{Hom}.cont_{C}(M, N)$ the additive group of continuous $C$-homomorphisms of $M$ into $N$.

**Lemma (18.5.3.1).**

<!-- label: 0_IV.18.5.3.1 -->

*Let $C$ be a topological ring, $E$, $L$ two topological $C$-bimodules; one supposes that the topologies are linear,
that $L$ is discrete and annihilated by an open two-sided ideal of $C$. Then one has a canonical isomorphism*

```text
(18.5.3.2)                lim Hom_{C/𝔎}(E / V, L) ⥲ Hom.cont_C(E, L)
                          ─────→
```

*where in the first member the inductive limit is taken following the right-filtered ordered set of pairs
$(\mathfrak{K}, V)$ such that $\mathfrak{K}$ is an open two-sided ideal of $C$, $V$ an open sub-$C$-bimodule of $E$,
such that $\mathfrak{K} \cdot L = L \cdot \mathfrak{K} = 0$, $\mathfrak{K} \cdot E \subset V$, $E \cdot \mathfrak{K}
\subset V$.*

As $C / \mathfrak{K}$ and $E / V$ are discrete, one has canonical homomorphisms
`w_{𝔎, V} : Hom_{C/𝔎}(E / V, L) → Hom.cont_C(E, L)` forming an inductive system, whence a homomorphism `(18.5.3.2)` by
passage to the inductive limit. As the homomorphism $E / V' \to E / V$ is surjective for $V' \subset V$, it follows at
once from the definition that the homomorphism $\operatorname{Hom}_{C/\mathfrak{K}}(E / V, L) \to
\operatorname{Hom}_{C/\mathfrak{K}}(E / V', L)$ (with $\mathfrak{K} \cdot L = L \cdot \mathfrak{K} = 0$, $\mathfrak{K}
\cdot E \subset V$, $E \cdot \mathfrak{K} \subset V$) is injective, and the same evidently holds for the homomorphism

```text
                              Hom_{C/𝔎}(E / V, L) → Hom_{C/𝔎'}(E / V, L)
```

for $\mathfrak{K}' \subset \mathfrak{K}$; one concludes that the homomorphism `(18.5.3.2)` is injective. On the other
hand, if $u$ is a continuous $C$-homomorphism of $E$ into $L$, its kernel is an open sub-bimodule `V_0` of $E$, and if
$\mathfrak{K}_{0}$ is an open two-sided ideal of $C$ such that $\mathfrak{K}_{0} \cdot L = L \cdot \mathfrak{K}_{0} = 0$
and $\mathfrak{K}_{0} \cdot E \subset V_{0}$, $E \cdot \mathfrak{K}_{0} \subset V_{0}$, it is clear that $u$ is the
canonical image of a $(C / \mathfrak{K}_{0})$-homomorphism of $E / V_{0}$ into $L$, hence `(18.5.3.2)` is surjective.

This being so, the proposition `(18.3.8)` generalizes as follows to topological rings:

**Proposition (18.5.4).**

<!-- label: 0_IV.18.5.4 -->

*Let $B$ be a linearly topologized topological ring, $\mathfrak{J}$ a two-sided ideal of $B$, $C = B / \mathfrak{J}$ the
quotient topological ring; $\mathfrak{J} / \mathfrak{J}^{2}$ (where $\mathfrak{J}$ is endowed with the topology induced
by that of $B$ and $\mathfrak{J} / \mathfrak{J}^{2}$ with the quotient topology of that of $\mathfrak{J}$) is then
canonically endowed with a structure of topological $C$-bimodule. For every discrete $C$-bimodule $L$ annihilated by an
open ideal of $C$, there exists then a canonical isomorphism*

```text
(18.5.4.1)                  Hom.cont_C(𝔍 / 𝔍^2, L) ⥲ Exantop_B(C, L).
```

Indeed, for every open ideal $\mathfrak{K}$ of $B$ such that $(\mathfrak{J} + \mathfrak{K}) / \mathfrak{J}$ annihilates
$L$, one has, by `(18.3.9)`, a canonical isomorphism

```text
                 Hom_{B/(𝔍 + 𝔎)}((𝔍 + 𝔎) / (𝔍^2 + 𝔎), L) ⥲ Exan_B(B / (𝔍 + 𝔎), L)
```

and it suffices to pass to the inductive limit, taking account of `(18.5.3.1)`.
