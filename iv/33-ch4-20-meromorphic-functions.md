<!-- original page 225 -->

## §20. Meromorphic functions; pseudo-morphisms

### 20.0. Introduction

Most of the notions and results of §§20 and 21 attach directly to chap. I, and depend hardly at all on chaps. II to IV,
except for the occasional use of the notion of depth and of regular local ring (in `(20.6)`, `(21.11)`, `(21.13)` and
`(21.15)`), of Zariski's "Main theorem" in `(20.4)` and `(21.12)`, and of properties of transversely regular immersions
in `(20.6)` and `(21.15)`.

<!-- original page 226 -->

In §20, we introduce several variants of the notion of rational map, already studied in `(I, 7)` from a point of view
still rather close to the classical viewpoint, and for this reason rather poorly adapted to the case of preschemes that
are not necessarily reduced. The notions and results of §20 are used in §21 (nos. 21.1 to 21.7) to develop the general
notion of divisor and its most elementary properties. This notion is especially convenient when the local rings of the
preschemes under consideration are Noetherian and integrally closed, and especially when they are moreover *factorial*
`(21.6 and 21.7)`, because of its identification in this latter case with the notion of *`1`-codimensional cycle*
(linear combination of irreducible subpreschemes of codimension `1`). In `(21.9)`, one determines the divisors on a
Noetherian prescheme of dimension `1` but not necessarily normal, which is useful for various applications. Nos.
`(21.11)` and `(21.12)` give two important theorems, due respectively to Auslander-Buchsbaum and Van der Waerden, and
related to the notion of factorial ring (nos. `(21.9)`, `(21.11)` and `(21.12)` are independent of one another). In nos.
`(21.13)` and `(21.14)`, also independent of the previous three, we study a useful variant of the notion of factorial
local ring, that of *parafactorial* local ring, which is introduced notably `[41]` in the development of comparison
theorems between the Picard group of a projective prescheme $X$ over a field $k$ and that of a "hyperplane section". One
will see in `(21.14.1)` (Ramanujam-Samuel theorem) that parafactorial local rings are much more numerous than one might
*a priori* have expected.

In `(20.5)`, `(20.6)` and `(21.15)`, we take up the preceding notions again but from a viewpoint "relative" to a fixed
base prescheme. For the moment these notions are used only rather rarely; in particular, the notion of relative divisor
is scarcely used except when one is dealing with positive divisors, and in this case it is explained advantageously
without recourse to the notion of relative meromorphic function, by means of the notion of transversely regular
immersion of codimension `1`. The reader will therefore find it advantageous to omit these sections on a first reading.

### 20.1. Meromorphic functions

**(20.1.1).** Let $(X, \mathcal{O}_{X})$ be a ringed space, and let $\mathcal{S}$ be a subsheaf *of sets* of
$\mathcal{O}_{X}$. For every open $U$ of $X$, consider the *ring of fractions* $\Gamma(U, \mathcal{O}_{X})[\Gamma(U,
\mathcal{S})^{-1}]$ (Bourbaki, _Alg. comm._, chap. II, §2, n° 1). It is immediate that the map $U \mapsto \Gamma(U,
\mathcal{O}_{X})[\Gamma(U, \mathcal{S})^{-1}]$ is a *presheaf of rings* $(0_{I}, 1.5.1 and 1.5.7)$. We denote by
$\mathcal{O}_{X}[\mathcal{S}^{-1}]$ the *sheaf of rings* associated to this presheaf and we say that this is the *sheaf
of rings of fractions of $\mathcal{O}_{X}$ with denominators in $\mathcal{S}$*; it is a *flat* $\mathcal{O}_{X}$-module.
It is immediate that for every $x \in X$, one has a canonical isomorphism

<!-- label: IV.20.1.1 -->

$$ (20.1.1.1) (\mathcal{O}_{X}[\mathcal{S}^{-1}])_{x} \xrightarrow{\sim} \mathcal{O}_{x}[\mathcal{S}^{-1}_{x}], $$

since the reasoning of $(0_{I}, 1.4.5)$ generalizes immediately to the case where one has an inductive system
$(A_{\alpha}, \phi_{\beta \alpha})$ of rings, and for each index $\alpha$ a subset $S_{\alpha}$ of $A_{\alpha}$ such
that

<!-- original page 227 -->

$\phi_{\beta \alpha}(S_{\alpha}) \subset S_{\beta}$ for $\alpha \leq \beta$; one then takes for $S$ the inductive limit
in $A = \lim A_{\alpha}$ of the inductive system of subsets $(S_{\alpha})$.

**(20.1.2).** Let now $\mathcal{F}$ be an $\mathcal{O}_{X}$-module. One then sets

```text
  (20.1.2.1)             ℱ[𝒮⁻¹] = ℱ ⊗_{𝒪_X} 𝒪_X[𝒮⁻¹]
```

and one says that this is the *sheaf of modules of fractions of $\mathcal{F}$ with denominators in $\mathcal{S}$*; it is
immediate that it is associated to the presheaf of modules $U \mapsto \Gamma(U, \mathcal{F})[\Gamma(U,
\mathcal{S})^{-1}]$, and that for every $x \in X$ one has a canonical isomorphism

$$ (20.1.2.2) (\mathcal{F}[\mathcal{S}^{-1}])_{x} \xrightarrow{\sim} \mathcal{F}_{x}[\mathcal{S}^{-1}_{x}]. $$

**(20.1.3).** We shall be interested here in the case where $\mathcal{S}$ is the subsheaf $\mathcal{S}(\mathcal{O}_{X})$
of $\mathcal{O}_{X}$ such that for every open $U$, $\Gamma(U, \mathcal{S})$ is the *set of regular elements* of the ring
$\Gamma(U, \mathcal{O}_{X})$; it is immediate that this is a sheaf (and not only a presheaf), the regularity of a
section of $\mathcal{O}_{X}$ over $U$ being verified "fibre by fibre" (i.e. meaning that the germ of the section at $x$
is regular in $\mathcal{O}_{X,x}$ for every $x \in U$); in other words $\mathcal{S}(\mathcal{O}_{X})_{x}$ is none other
than the set of regular elements of $\mathcal{O}_{X,x}$. The corresponding sheaf of rings

$$ \mathcal{M}_{X} = \mathcal{O}_{X}[\mathcal{S}^{-1}] $$

is called the *sheaf of germs of meromorphic functions on $X$*, and the sections of $\mathcal{M}_{X}$ over $X$ are
called the *meromorphic functions on $X$*; they form a ring which one denotes $M(X)$. For every $\mathcal{O}_{X}$-Module
$\mathcal{F}$,

```text
                         ℱ ⊗_{𝒪_X} 𝓜_X = ℱ[𝒮⁻¹]
```

is also denoted $\mathcal{M}_{X}(\mathcal{F})$ and called the *sheaf of germs of meromorphic sections of $\mathcal{F}$*;
its sections over $X$ form an $M(X)$-module denoted $M(X, \mathcal{F})$, whose elements are called *meromorphic sections
of $\mathcal{F}$ over $X$*. These definitions imply that for every open $U$ of $X$, one has a canonical isomorphism
$\mathcal{M}_{X}(\mathcal{F}) | U \xrightarrow{\sim} \mathcal{M}_{U}(\mathcal{F} | U)$, in particular $\mathcal{M}_{X} |
U \xrightarrow{\sim} \mathcal{M}_{U}$.

**(20.1.3.1).** If $X$ is a *reduced prescheme*, one will note that if an element $s \in \Gamma(U, \mathcal{O}_{X})$ is
such that $s_{\xi} \neq 0$ for every maximal point $\xi$ of $U$, then $s$ is *regular*. Indeed, if $st = 0$ for a $t \in
\Gamma(U, \mathcal{O}_{X})$, one has $s_{\xi} t_{\xi} = 0$, hence $t_{\xi} = 0$ since $\mathcal{O}_{X,\xi}$ is a field,
and to say that $t_{\xi} = 0$ for every maximal point $\xi$ of $X$ means that $t = 0$: one is at once reduced to the
case where $U$ is affine, and an element of a reduced ring belonging to every minimal prime ideal is zero by definition.
The converse is true if the set of irreducible components of $X$ is *locally finite*. One is at once reduced to the case
where $X = \operatorname{Spec}(A)$ is affine; if $\mathfrak{p}_{i}$ ($1 \leq i \leq n$) are the minimal prime ideals of
$A$ and $s \in \mathfrak{p}_{i}$ for some index $i$, then there exists $t \in A$ such that $t \in \mathfrak{p}_{j}$ for
$j \neq i$ and $t \notin \mathfrak{p}_{i}$ (Bourbaki, _Alg. comm._, chap. II, §1, n° 1, prop. 1); one therefore has $st
\in \mathfrak{p}_{i}$ for every $i$, hence $st = 0$ since $A$ is reduced; so $s$ is not regular.

**(20.1.4).** For every open $U$ of $X$, the homomorphism $t \mapsto t/1$ from $\Gamma(U, \mathcal{O}_{X})$ to
$\Gamma(U, \mathcal{O}_{X})[\Gamma(U, \mathcal{S})^{-1}]$ (which is none other than the *total ring of fractions* of

<!-- original page 228 -->

$\Gamma(U, \mathcal{O}_{X})$) is injective; these homomorphisms therefore define a *canonical injective homomorphism*

$$ (20.1.4.1) i : \mathcal{O}_{X} \to \mathcal{M}_{X} $$

which allows one to identify $\mathcal{O}_{X}$ with a subsheaf of $\mathcal{M}_{X}$. Given a meromorphic function $\phi
\in M(X)$, one says that $\phi$ is *defined* on an open $U$ of $X$ if $\phi | U$ is a section of $\mathcal{O}_{X}$ over
$U$; the sheaf axioms show that, for a given section $\phi$, there is a *largest* open on which $\phi$ is defined; one
calls this the *domain of definition* of $\phi$ and denotes it $dom(\phi)$.

**(20.1.5).** For every $\mathcal{O}_{X}$-Module $\mathcal{F}$, one deduces from `(20.1.4.1)` a di-homomorphism formed
of $i$ and the homomorphism of sheaves of additive groups

```text
  (20.1.5.1)             1_ℱ ⊗ i : ℱ → 𝓜_X(ℱ) = ℱ ⊗_{𝒪_X} 𝓜_X.
```

One will note that the latter is no longer injective in general; when it is injective, one says that $\mathcal{F}$ is
*strictly torsion-free*: this means that for every open $U$ of $X$ and every section $s \in \Gamma(U, \mathcal{O}_{X})$
which is a regular element of that ring, the homothety $z \mapsto sz$ of $\Gamma(U, \mathcal{F})$ is injective; this
condition is evidently satisfied if $\mathcal{F}$ is *locally free*.

**Proposition (20.1.6).**

<!-- label: IV.20.1.6 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. For $\mathcal{F}$
to be strictly torsion-free, it is necessary and sufficient that $Ass(\mathcal{F}) \subset Ass(\mathcal{O}_{X})$.*

One is at once reduced to the case where $X = \operatorname{Spec}(A)$ is affine, $\mathcal{F} = \tilde{M}$, and one
knows that the elements $s$ of $A$ belonging to an ideal of $Ass(M)$ are exactly those for which the homothety $z
\mapsto sz$ is not injective (Bourbaki, _Alg. comm._, chap. IV, §1, n° 1, cor. 2 of prop. 2).

**(20.1.7).** If $u$ is a section of $\mathcal{M}_{X}(\mathcal{F})$ over $X$, one says that $u$ is *defined* at a point
$x \in X$ if there exists an open neighbourhood $V$ of $x$ in $X$ such that $u | V$ is the image of a section of
$\mathcal{F}$ over $V$ under the di-homomorphism `(20.1.5.1)`. One says that $u$ is *defined* on an open $U$ of $X$ if
it is defined at every point of $U$; there is again a largest open on which $u$ is defined, called the *domain of
definition* of $u$ and denoted $dom(u)$. When $\mathcal{F}$ is strictly torsion-free, so that $\mathcal{F}$ is
identified by `(20.1.5.1)` with a subsheaf of $\mathcal{M}_{X}(\mathcal{F})$, saying that $u$ is defined on $U$ means
that $u | U$ is a section of $\mathcal{F}$ over $U$.

**(20.1.8).** In accordance with the general notation $(0_{I}, 5.4.7)$, one denotes by $\mathcal{M}^{\times}_{X}$ the
sheaf of multiplicative groups such that $\Gamma(U, \mathcal{M}^{\times}_{X})$ is (for every open $U$ of $X$) the group
of *invertible elements* of $\Gamma(U, \mathcal{M}_{X})$. This sheaf is none other than the sheaf
$\mathcal{S}(\mathcal{M}_{X})$ defined in `(20.1.3)`: indeed, if $s \in \Gamma(U, \mathcal{S}(\mathcal{M}_{X}))$, then
for every $x \in U$ there exists an open neighbourhood $V \subset U$ of $x$ such that $s | V$ is a regular element in
the *total ring of fractions* of $\Gamma(V, \mathcal{O}_{X})$, and one knows that such an element is necessarily
invertible in this ring of fractions. We shall say that the sections of $\mathcal{M}^{\times}_{X}$ over $X$ are the
*regular meromorphic functions* (one will note that we are departing here from the terminology followed by certain
authors, who call "regular" meromorphic functions those which are sections of $\mathcal{O}_{X}$, identified with a
subsheaf of $\mathcal{M}_{X}$).

Let $\mathcal{L}$ be an *invertible $\mathcal{O}_{X}$-Module* $(0_{I}, 5.4.1)$; then it is clear that
$\mathcal{M}_{X}(\mathcal{L}) = \mathcal{L} \otimes_{\mathcal{O}_{X}} \mathcal{M}_{X}$

<!-- original page 229 -->

is an invertible $\mathcal{M}_{X}$-Module. Let $U$ be an open such that $\mathcal{L} | U$ is isomorphic to
$\mathcal{O}_{U}$; since every automorphism of $\mathcal{M}_{U}$ is multiplication by an invertible element of
$\Gamma(U, \mathcal{M}_{X})$ $(0_{I}, 5.4.7)$, it amounts to the same thing to say that a section $s \in \Gamma(U,
\mathcal{M}_{X}(\mathcal{L}))$ has invertible image in $\Gamma(U, \mathcal{M}_{X})$ under *an* isomorphism or under
*every* isomorphism onto $\Gamma(U, \mathcal{M}_{X})$; one will say in this case that $s$ is a *regular meromorphic
section of $\mathcal{L}$* over $U$; a section $s$ of $\mathcal{L}$ over $X$ will be called a *regular meromorphic
section of $\mathcal{L}$* if, for every open $U$ such that $\mathcal{L} | U$ is isomorphic to $\mathcal{O}_{U}$, $s | U$
is a regular meromorphic section of $\mathcal{L}$ over $U$. One denotes by $(\mathcal{M}_{X}(\mathcal{L}))^{\times}$ the
subsheaf of $\mathcal{M}_{X}(\mathcal{L})$ such that for every open $U$, $\Gamma(U,
(\mathcal{M}_{X}(\mathcal{L}))^{\times})$ is the set of regular meromorphic sections of $\mathcal{L}$ over $U$. Let $s$
be a meromorphic section of $\mathcal{L}$ over $X$ (i.e. a section of $\mathcal{M}_{X}(\mathcal{L})$); it defines a
homomorphism $h_{s} : \mathcal{M}_{X} \to \mathcal{M}_{X}(\mathcal{L})$ which to every section $t$ of $\mathcal{M}_{X}$
over an open $U$ associates $(s | U) t$. It follows at once from the foregoing that, for $s$ to be *regular*, it is
necessary and sufficient that $h_{s}$ be *injective*, and in fact $h_{s}$ is then a *bijective* homomorphism from
$\mathcal{M}_{X}$ to $\mathcal{M}_{X}(\mathcal{L})$, and its restriction to $\mathcal{M}^{\times}_{X}$ is a bijection
onto $(\mathcal{M}_{X}(\mathcal{L}))^{\times}$. One concludes that the homothety $t \mapsto ts$ is an isomorphism from
$M(X)$ onto $M(X, \mathcal{L})$.

**(20.1.9).** Let $s$ be a regular meromorphic section of the invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ over
$X$; then, for every $\mathcal{O}_{X}$-Module $\mathcal{F}$, $s$ likewise defines a homomorphism $h_{s} \otimes
1_{\mathcal{F}} : \mathcal{M}_{X}(\mathcal{F}) \to \mathcal{M}_{X}(\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L})$,
which is again *bijective*.

**(20.1.10).** Let $s$ be a meromorphic section of an invertible $\mathcal{O}_{X}$-Module $\mathcal{L}$ over $X$; for
$s$ to be regular, it is necessary and sufficient that there exist a meromorphic section $s'$ of $\mathcal{L}^{-1}$ over
$X$ such that the canonical image of $s \otimes s'$ in $\mathcal{M}_{X}$ $(0_{I}, 5.4.3)$ is the unit section, and this
section $s'$ is then unique: indeed, the necessity of the local existence of such a section is evident, and its local
uniqueness entails its global existence (and uniqueness); moreover, the existence of $s'$ is trivially sufficient for
$s$ to be regular. One will set $s' = s^{-1}$.

Finally, if $\mathcal{L}'$ is a second invertible $\mathcal{O}_{X}$-Module, $s$ (resp. $s'$) a regular meromorphic
section of $\mathcal{L}$ (resp. $\mathcal{L}'$) over $X$, then $s \otimes s'$ is evidently a regular meromorphic section
of $\mathcal{L} \otimes \mathcal{L}'$ over $X$.

**(20.1.11).** If $f : X' \to X$ is a morphism of ringed spaces, there is in general no natural map sending a
meromorphic function on $X$ to a meromorphic function on $X'$. For example, if $X$ is the spectrum of an integral local
ring $A$, $X'$ that of its residue field $k$, there is no natural homomorphism from the field of fractions $K$ of $A$ to
$k$, and one can send an element of $K$ to an element of $k$ only if it is already in $A$.

More generally, if $f = (\psi, \theta)$, denote, for every open $U$ of $X$, by $\mathcal{S}_{f}(U)$ the set of *regular*
sections $s \in \Gamma(U, \mathcal{O}_{X})$ such that the image of $s$ under

```text
                         Γ(θ♯) : Γ(U, 𝒪_X) → Γ(f⁻¹(U), 𝒪_{X'})
```

is a regular section. It is immediate that $U \mapsto \mathcal{S}_{f}(U)$ is a *subsheaf* of the sheaf of sets
$\mathcal{S}(\mathcal{O}_{X})$, which one denotes $\mathcal{S}_{f}$. One sets $\mathcal{M}_{f} =
\mathcal{O}_{X}[\mathcal{S}^{-1}_{f}]$; this is a subsheaf

<!-- original page 230 -->

of rings of $\mathcal{M}_{X}$, and one canonically deduces from $\theta\sharp : \psi*(\mathcal{O}_{X}) \to
\mathcal{O}_{X'}$ a homomorphism of sheaves of rings $\theta'\sharp : \psi*(\mathcal{M}_{f}) \to \mathcal{M}_{X'}$
extending $\theta\sharp$ (Bourbaki, _Alg. comm._, chap. II, §2, n° 1, prop. 2); whence, recalling that
$f*(\mathcal{M}_{f}) = \psi*(\mathcal{M}_{f}) \otimes_{\psi*(\mathcal{O}_{X})} \mathcal{O}_{X'}$, a canonical
homomorphism of $\mathcal{O}_{X'}$-Algebras

$$ (20.1.11.1) f*(\mathcal{M}_{f}) \to \mathcal{M}_{X'}. $$

For every meromorphic function $\phi$ on $X$ which is a section of $\mathcal{M}_{f}$, $\Gamma(\theta'\sharp)(\phi)$ is a
meromorphic function on $X'$, called the *inverse image of $\phi$ under $f$*, and denoted $\phi \circ f$ if this entails
no confusion.

Similarly, if $\mathcal{F}$ is an $\mathcal{O}_{X}$-Module, one sets $\mathcal{M}_{f}(\mathcal{F}) = \mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{M}_{f}$, and one immediately deduces from $\theta'\sharp$ a canonical homomorphism
(also written $u \mapsto u \circ f$)

```text
                         Γ(X, 𝓜_f(ℱ)) → Γ(X', 𝓜_{X'}(f*(ℱ))).
```

Moreover, if $u \in \Gamma(X, \mathcal{M}_{f}(\mathcal{F}))$ is defined `(20.1.7)` at a point $x$, $u$ coincides, on a
neighbourhood $U$ of $x$, with a section of the form $\sum_{i} h_{i} \otimes (t_{i} / s_{i})$, where the $h_{i}$ belong
to $\Gamma(U, \mathcal{F})$, the $t_{i}$ to $\Gamma(U, \mathcal{O}_{X})$, and the $s_{i}$ to $\Gamma(U,
\mathcal{S}_{f})$. As by hypothesis the images of the $s_{i}$ in $\Gamma(f^{-1}(U), \mathcal{O}_{X'})$ are regular, one
sees that $u \circ f$ is defined at every point of $f^{-1}(U)$; in other words, one has

$$ (20.1.11.2) f^{-1}(dom(u)) \subset dom(u \circ f). $$

We shall see later `(20.6.5, (i))` examples (with $\mathcal{F} = \mathcal{O}_{X}$) where the two sides of `(20.1.11.2)`
may be distinct.

Consider in particular the case where $\mathcal{M}_{f} = \mathcal{M}_{X}$; then, if $\mathcal{L}$ is an invertible
$\mathcal{O}_{X}$-Module, the image in $\mathcal{M}_{X'}(f*(\mathcal{L}))$, under $\Gamma(\theta'\sharp)$, of a
*regular* meromorphic section of $\mathcal{L}$ over $X$ `(20.1.8)` is a *regular* meromorphic section of
$f*(\mathcal{L})$ over $X'$, as follows at once from the definition of these sections and from the fact that a
homomorphism of rings sends an invertible element to an invertible element.

Let $f' : X'' \to X'$ be a second morphism of ringed spaces, and suppose that $\mathcal{M}_{f} = \mathcal{M}_{X}$ and
$\mathcal{M}_{f'} = \mathcal{M}_{X'}$; then, if one sets $f'' = f \circ f'$, one also has $\mathcal{M}_{f''} =
\mathcal{M}_{X}$, and one sees at once that for every meromorphic section $u$ of $\mathcal{F}$ over $X$, one has $u
\circ f'' = (u \circ f) \circ f'$.

**Proposition (20.1.12).**

<!-- label: IV.20.1.12 -->

*If the morphism $f : X' \to X$ is flat $(0_{I}, 6.7.1)$, one has $\mathcal{M}_{f} = \mathcal{M}_{X}$, and the
homomorphism $\phi \mapsto \phi \circ f$ is defined on all of $M(X)$. Moreover, if $f$ is a (flat) morphism of ringed
spaces in local rings, one has $dom(\phi \circ f) = f^{-1}(dom(\phi))$; if in addition $f$ is surjective (hence
faithfully flat), the homomorphism $\phi \mapsto \phi \circ f$ is injective.*

The first assertion follows from the fact that, if $B$ is an $A$-algebra which is a flat $A$-module, every element of
$A$ which is not a zero-divisor in $A$ is not a zero-divisor in $B$ $(0_{I}, 6.3.4)$. To prove the other assertions,
note that, for every $x' \in X'$, if $x = f(x')$, $\mathcal{O}_{X', x'}$ is a flat $\mathcal{O}_{X,x}$-module, and since
the homomorphism $\mathcal{O}_{X,x} \to \mathcal{O}_{X', x'}$ is local by hypothesis, it is injective $(0_{I}, 6.5.1 and
6.6.2)$; if one sets $A = \mathcal{O}_{X,x}$, $B = \mathcal{O}_{X', x'}$, so that $A$ identifies with a subring of $B$,
$(f*(\mathcal{M}_{X}))_{x'}$ is equal to $S^{-1}A \otimes_{A} B = S^{-1}B$, where $S$ is the set of regular elements of
$A$, $(\mathcal{M}_{X'})_{x'}$ is equal to $T^{-1}B$, where $T$ is the set

<!-- original page 231 -->

of regular elements of $B$, and as we have seen that $S \subset T$, the homomorphism $S^{-1}B \to T^{-1}B$ is injective;
in other words, this proves that the homomorphism `(20.1.11.1)` $f*(\mathcal{M}_{X}) \to \mathcal{M}_{X'}$ is
*injective* (whence the last assertion of the statement). The quotient $f*(\mathcal{M}_{X}) / \mathcal{O}_{X'}$
identifies with an $\mathcal{O}_{X'}$-submodule of $\mathcal{M}_{X'} / \mathcal{O}_{X'}$, and $(f*(\mathcal{M}_{X}) /
\mathcal{O}_{X'})_{x'}$ identifies with $(\mathcal{M}_{X} / \mathcal{O}_{X})_{x} \otimes_{\mathcal{O}_{X,x}}
\mathcal{O}_{X', x'}$. Now suppose that $x \notin dom(\phi)$; the image of $\phi_{x}$ in $(\mathcal{M}_{X} /
\mathcal{O}_{X})_{x}$ is therefore $\neq 0$; by faithful flatness, one deduces that the same holds for the image of
$(\phi \circ f)_{x'}$ in $(\mathcal{M}_{X'} / \mathcal{O}_{X'})_{x'}$, hence $x' \notin dom(\phi \circ f)$, which
finishes the proof.

**Remark (20.1.13).**

<!-- label: IV.20.1.13 -->

Let $X$ be a *reduced* complex analytic space; then the notion of meromorphic function on $X$ defined above coincides
with the usual notion. Consider on the other hand a prescheme $Y$, locally of finite type over the field $\mathbb{C}$;
one then knows that one can associate to $Y$ an analytic space $Y^{an}$ having the same underlying topological space,
and that the canonical morphism $f : Y^{an} \to Y$ is flat `[37]`; by virtue of `(20.1.12)`, the canonical homomorphism
$u \mapsto u \circ f$ from $M(Y)$ to $M(Y^{an})$ is therefore everywhere defined and injective; but it is not
*surjective* in general. For example, when $Y = \mathbb{V}^{r}_{0}$ ($Err_{III}, 14$) is the affine space of dimension
$r$ over $\mathbb{C}$, $M(Y)$ identifies canonically with the field $R(Y)$ of rational functions on $Y$
`(20.2.13, (i))`, while $M(Y^{an})$ is the field of usual meromorphic functions on $\mathbb{C}^{r}$. By reason of this
fact, it is often preferable, in algebraic geometry, to refrain from the terminology introduced in this section, and to
use the equivalent terminology of "pseudo-function" which will be defined below.

### 20.2. Pseudo-morphisms and pseudo-functions

*The only ringed spaces considered in this section are preschemes.*

**(20.2.1).** Recall `(11.10.2)` that in a prescheme $X$ one says that an open $U$ is *schematically dense* if, for
every open $V$ of $X$, the canonical homomorphism $\Gamma(V, \mathcal{O}_{X}) \to \Gamma(V \cap U, \mathcal{O}_{X})$ is
injective.

Consider two preschemes $X$, $Y$, and two schematically dense opens $U$, $U'$ of $X$; one says that two morphisms $u : U
\to Y$, $u' : U' \to Y$ are *equivalent* if there exists an open $U'' \subset U \cap U'$, schematically dense in $X$,
such that $u | U'' = u' | U''$. As it follows at once from the definition of schematically dense opens that the
intersection of two such opens is again one, it is immediate that the previous relation is indeed an equivalence
relation. An equivalence class under this relation is called a *pseudo-morphism of $X$ into $Y$*, or a *strict rational
map of $X$ into $Y$*.

If $S$ is a prescheme and $X$, $Y$ are two $S$-preschemes, one calls *pseudo-$S$-morphism* the equivalence class (for
the foregoing relation) of an $S$-morphism from a schematically dense open of $X$ to $Y$. A pseudo-morphism is therefore
nothing other than a pseudo-$S$-morphism for $S = \operatorname{Spec}(\mathbb{Z})$.

One denotes by `Ps.hom(X, Y)` (resp. $Ps.hom_{S}(X, Y)$) the set of pseudo-morphisms (resp. pseudo-$S$-morphisms) of $X$
into $Y$.

<!-- original page 232 -->

**(20.2.2).** It follows from the definition recalled above that if $U$ is a schematically dense open in $X$, then for
every open $V$ of $X$, $U \cap V$ is schematically dense in $V$. If two morphisms $u : U \to Y$, $u' : U' \to Y$ of
schematically dense opens of $X$ into $Y$ are equivalent, it follows that their restrictions $u | (V \cap U)$ and $u' |
(V \cap U')$ are also equivalent morphisms (for the prescheme induced on $V$); their class is called the *restriction to
$V$* of the pseudo-morphism $\omega$, the class of $u$, and this pseudo-morphism is denoted $\omega | V$. If $W \subset
V$ is an open of $X$, it is clear that $(\omega | V) | W = \omega | W$. This shows that the restriction maps define a
presheaf of sets $U \mapsto Ps.hom(U, Y)$; one will note that this presheaf is not in general a sheaf (cf. `(20.2.16)`);
the associated sheaf is denoted $\mathcal{Ps}.hom(X, Y)$. For pseudo-$S$-morphisms, one sees likewise that $U \mapsto
Ps.hom_{S}(U, Y)$ is a presheaf of sets, whose associated sheaf is denoted $\mathcal{Ps}.hom_{S}(X, Y)$.

If $V$ is schematically dense in $X$, then for every open $U$ schematically dense in $X$, $U \cap V$ is also
schematically dense in $X$, so the map $\omega \mapsto \omega | V$ is a bijection from `Ps.hom(X, Y)` (resp.
$Ps.hom_{S}(X, Y)$) onto `Ps.hom(V, Y)` (resp. $Ps.hom_{S}(V, Y)$).

**(20.2.3).** Given a pseudo-$S$-morphism $\omega$ of $X$ into $Y$, one says that it is *defined* at a point $x \in X$
if there exists an open neighbourhood $V$ of $x$ in $X$, an open $U \subset V$ containing $x$ and schematically dense in
$V$, and an $S$-morphism $u : U \to Y$ whose class in $Ps.hom_{S}(V, Y)$ equals $\omega | V$ `(20.2.2)`; one calls
*domain of definition* of $\omega$, and one denotes by $dom_{S}(\omega)$ (or simply $dom(\omega)$ if $S =
\operatorname{Spec}(\mathbb{Z})$), the set of $x \in X$ where $\omega$ is defined; it is evidently an open of $X$.
Moreover, for every open $W$ of $X$, one has

```text
  (20.2.3.1)             dom_S(ω | W) = (dom_S(ω)) ∩ W
```

by virtue of the property of schematically dense opens recalled in `(20.2.2)`.

**Proposition (20.2.4).**

<!-- label: IV.20.2.4 -->

*Suppose that $X$, $Y$ are $S$-preschemes such that the structure morphism $Y \to S$ is separated; then, if $\omega$ is
a pseudo-$S$-morphism of $X$ into $Y$, $dom_{S}(\omega)$ is the largest of the schematically dense opens $U$ of $X$ such
that there exists an $S$-morphism $u : U \to Y$ belonging to the class $\omega$.*

It evidently suffices to prove that if $U$, $U'$ are two schematically dense opens in $X$ such that two $S$-morphisms
$u : U \to Y$ and $u' : U' \to Y$ are equivalent, then the restrictions of $u$ and $u'$ to $U \cap U'$ are equal. Now by
hypothesis there exists an open $U'' \subset U \cap U'$, schematically dense in $X$ and on which $u$ and $u'$ coincide;
as `U''` is also schematically dense in $U \cap U'$, our assertion follows from `(11.10.1, d)`.

**Corollary (20.2.5).**

<!-- label: IV.20.2.5 -->

*Let $S$ be an `S_0`-scheme, $X$, $Y$ two $S$-preschemes such that the composite $Y \to S \to S_{0}$ is separated (which
implies `(I, 5.5.1)` that $Y \to S$ is also separated). For every pseudo-$S$-morphism $\omega$ of $X$ into $Y$, one has
then $dom_{S}(\omega) = dom_{S_{0}}(\omega)$. In particular, if $Y$ is a scheme, one has $dom_{S}(\omega) =
dom(\omega)$.*

Indeed, it is clear that $dom_{S}(\omega) \subset dom_{S_{0}}(\omega)$ without any separation hypothesis; by virtue of
`(20.2.4)`, it suffices to prove that if an `S_0`-morphism $u_{0} : U_{0} \to Y$ from a schematically dense

<!-- original page 233 -->

open `U_0` of $X$ into $Y$ is such that the composite $v_{0} : U_{0} \to Y \to S$ coincides with the restriction of the
structure morphism $w_{0} : U_{0} \to S$ on an open $U \subset U_{0}$ schematically dense in $X$, then $v_{0} = w_{0}$.
But by virtue of the hypothesis that the morphism $S \to S_{0}$ is separated, this again follows from `(11.10.1, d)`.

**Corollary (20.2.6).**

<!-- label: IV.20.2.6 -->

*Under the hypotheses of `(20.2.4)`, the presheaf $U \mapsto Ps.hom_{S}(U, Y)$ is a sheaf.*

Indeed, let $U$ be an open of $X$, $(U_{\alpha})$ a cover of $U$ by opens of $U$; suppose given for each $\alpha$ a
pseudo-$S$-morphism $\omega_{\alpha}$ of $U_{\alpha}$ into $Y$, so that for every pair of indices $\alpha$, $\beta$, the
restrictions `(20.2.2)` of the pseudo-$S$-morphisms $\omega_{\alpha}$ and $\omega_{\beta}$ to $U_{\alpha} \cap
U_{\beta}$ are equal; by virtue of `(20.2.3.1)`, this entails $dom_{S}(\omega_{\alpha}) \cap U_{\beta} =
dom_{S}(\omega_{\beta}) \cap U_{\alpha}$. Let $W$ be the union of the opens $dom_{S}(\omega_{\alpha})$, and, for each
$\alpha$, let $u_{\alpha}$ be the unique $S$-morphism $dom_{S}(\omega_{\alpha}) \to Y$ belonging to the class
$\omega_{\alpha}$ `(20.2.4)`; by reason of the hypothesis and of `(20.2.4)`, the restrictions of $u_{\alpha}$ and
$u_{\beta}$ to $dom_{S}(\omega_{\alpha}) \cap dom_{S}(\omega_{\beta})$ are equal, so there exists a morphism $u : W \to
Y$ whose restriction to each open $dom_{S}(\omega_{\alpha})$ equals $u_{\alpha}$. It is clear that $W$ is schematically
dense in $U$, hence defines a pseudo-$S$-morphism $\omega$ of $U$ into $Y$ whose restrictions to the $U_{\alpha}$ are
the $\omega_{\alpha}$.

**Remark (20.2.7).**

<!-- label: IV.20.2.7 -->

One knows `(11.10.4)` that when $X$ is reduced, it amounts to the same to say that an open of $X$ is dense in $X$ or
that it is schematically dense in $X$; the notion of pseudo-morphism (resp. pseudo-$S$-morphism) of $X$ into $Y$ then
coincides with that of *rational map* (resp. *$S$-rational map*) of $X$ into $Y$ `(I, 7.1.2)`. In the general case, the
notion of pseudo-morphism seems more useful than that of rational map.

**(20.2.8).** One calls *pseudo-function* on $X$ a pseudo-morphism of $X$ into $\operatorname{Spec}(\mathbb{Z}[T])$ ($T$
indeterminate), or, what amounts to the same, an $X$-pseudo-morphism of $X$ into $X \otimes_{\mathbb{Z}} \mathbb{Z}[T]$;
it amounts also to the same `(I, 3.3.15)` to say that a pseudo-function on $X$ is an equivalence class of *sections of
$\mathcal{O}_{X}$ over schematically dense opens of $X$*, two sections $g \in \Gamma(U, \mathcal{O}_{X})$, $g' \in
\Gamma(U', \mathcal{O}_{X})$ over such opens being equivalent if there exists an open $U'' \subset U \cap U'$,
schematically dense in $X$, on which $g$ and $g'$ coincide. One may here apply `(20.2.4)` with $S = X$ and $Y = X
\otimes_{\mathbb{Z}} \mathbb{Z}[T]$; hence, for every pseudo-function $\phi$ on $X$, there exists a largest
schematically dense open $dom(\phi)$ in $X$ on which there is a section of $\mathcal{O}_{X}$ over $dom(\phi)$ belonging
to the class $\phi$. It is clear that the sheaf $\mathcal{Ps}.hom(X, X \otimes_{\mathbb{Z}} \mathbb{Z}[T])$ is here a
sheaf of rings, even an $\mathcal{O}_{X}$-Algebra, which we shall denote $\mathcal{M}'_{X}$; it follows from `(20.2.6)`
that, for every open $U$ of $X$, $\Gamma(U, \mathcal{M}'_{X})$ equals the set of pseudo-morphisms of $U$ into
$\operatorname{Spec}(\mathbb{Z}[T])$; one sets $M'(X) = \Gamma(X, \mathcal{M}'_{X})$. To say that a section $\phi$ of
$\mathcal{M}'_{X}$ over $U$ is invertible in the ring $\Gamma(U, \mathcal{M}'_{X})$ means that there exists an open $U'$
schematically dense in $dom(\phi)$, hence in $U$, such that, if $g$ is the unique section of $\mathcal{O}_{X}$ over
$dom(\phi)$ belonging to $\phi$, $g | U'$ is invertible in $\Gamma(U', \mathcal{O}_{X})$. It follows from `(I, 3.3.15)`
that, in the canonical correspondence between $\Gamma(V, \mathcal{O}_{X})$ and $\operatorname{Hom}(V, \mathbb{Z}[T])$
($V$ open

<!-- original page 234 -->

of $X$), the invertible elements of $\Gamma(V, \mathcal{O}_{X})$ correspond to morphisms which factor as $V \to
\operatorname{Spec}(\mathbb{Z}[T, T^{-1}]) \to \operatorname{Spec}(\mathbb{Z}[T])$. One concludes that the sheaf
$\mathcal{M}'^{\times}_{X}$ of germs of invertible sections of $\mathcal{M}'_{X}$ identifies canonically with the sheaf
$\mathcal{Ps}.hom(X, X \otimes_{\mathbb{Z}} \mathbb{Z}[T, T^{-1}])$.

**Lemma (20.2.9).**

<!-- label: IV.20.2.9 -->

*Let $U$ be an open of $X$, $s$ a regular element of the ring $\Gamma(U, \mathcal{O}_{X})$; then the open set $U_{s}$ of
$x \in U$ such that $s(x) \neq 0$ is schematically dense in $U$.*

Indeed, let $V$ be an open of $U$, $t$ a section of $\mathcal{O}_{X}$ over $V$ such that $t | (V \cap U_{s}) = 0$. For
every affine open $W \subset V$, there then exists an integer $n$ such that $s^{n} t | W = 0$ `(I, 1.4.1)`; but since
$s$ is a regular element of $\Gamma(U, \mathcal{O}_{X})$, this entails $t | W = 0$, whence $t = 0$.

**(20.2.10).** Consider a meromorphic function $f \in M(X)$ `(20.1.4)`; then $dom(f)$ is *schematically dense* in $X$:
indeed, every point of $X$ admits an open neighbourhood $U$ such that there exists a section $s \in \Gamma(U,
\mathcal{S})$ which is a regular element of this ring, and such that $s(f | U) \in \Gamma(U, \mathcal{O}_{X})$; since $s
| U_{s}$ is invertible, one concludes that $f | U_{s} \in \Gamma(U_{s}, \mathcal{O}_{X})$, hence $U_{s} \subset dom(f)$
by definition `(20.1.4)`, and our assertion follows from the lemma `(20.2.9)`. One may therefore associate to $f$ the
pseudo-function equal to the class of the section of $\mathcal{O}_{X}$ over $dom(f)$, the restriction of $f$; operating
similarly with $X$ replaced by an arbitrary open of $X$, one obtains in this way a canonical homomorphism of
$\mathcal{O}_{X}$-Algebras

$$ (20.2.10.1) \mathcal{M}_{X} \to \mathcal{M}'_{X} $$

which, by restriction, evidently gives a homomorphism of sheaves of abelian groups

$$ (20.2.10.2) \mathcal{M}^{\times}_{X} \to \mathcal{M}'^{\times}_{X} $$

for the sheaves of germs of invertible sections of $\mathcal{M}_{X}$ and $\mathcal{M}'_{X}$.

**Proposition (20.2.11).**

<!-- label: IV.20.2.11 -->

*(i) The canonical homomorphism `(20.2.10.1)` (and consequently also `(20.2.10.2)`) is injective.*

*(ii) Suppose either that $X$ is locally Noetherian, or that $X$ is reduced and the set of its irreducible components is
locally finite. Then the canonical homomorphism `(20.2.10.1)` (and consequently also `(20.2.10.2)`) is bijective.*

The questions being local on $X$, one may restrict to the case $X = \operatorname{Spec}(A)$ affine, and then show that
the canonical homomorphism $M(X) \to M'(X)$ is always injective, and that it is bijective in the cases considered in
(ii). Taking into account the definition of the sheaf $\mathcal{M}_{X}$ `(20.1.3)`, one may moreover note that
`(20.2.10.1)` actually comes from a homomorphism of presheaves

```text
                         Γ(U, 𝒪_X)[Γ(U, 𝒮)⁻¹] → Γ(U, 𝓜'_X)
```

and it suffices to show that, for $U$ affine, this latter is injective (resp. bijective under the hypotheses of (ii)).
Denoting by $S$ the set of regular elements of $A$ (so that $S^{-1}A$ is the total ring of fractions of $A$), one must
therefore consider the canonical homomorphism

$$ (20.2.11.1) S^{-1}A \to M'(X) $$

<!-- original page 235 -->

and show that it is injective (resp. bijective under the conditions of (ii)). Now, one may write $S^{-1}A = \lim A_{t}$,
where $t$ runs over the set of regular elements of $A$, ordered by the relation "$t$ is a divisor of $t'$" $(0_{I},
1.4.5)$; one may also write $A_{t} = \Gamma(D(t), \mathcal{O}_{X})$. On the other hand, one has by definition $M'(X) =
\lim \Gamma(U, \mathcal{O}_{X})$, where $U$ runs over the set of schematically dense opens of $X$ (ordered by
$\supset$), and the map `(20.2.11.1)` is none other than the canonical map coming from the fact that the $D(t)$
constitute a part of the set of schematically dense opens in $X$ `(20.2.9)`. Note that, by definition of a schematically
dense open, the homomorphism $\Gamma(U, \mathcal{O}_{X}) \to \Gamma(U', \mathcal{O}_{X})$ for two such opens $U' \subset
U$ is always injective, hence so are the homomorphisms $\Gamma(U, \mathcal{O}_{X}) \to M'(X)$, and one concludes that
`(20.2.11.1)` is injective. To prove that `(20.2.11.1)` is bijective, it suffices to show that the set of $D(t)$ is
cofinal in the set of schematically dense opens, in other words that for such an open $U$, there exists $t$ regular in
$A$ such that $D(t) \subset U$. Now, when $X$ is reduced and the irreducible components of $X$ form a locally finite
set, this set is finite since $X$ was supposed affine, in other words $A$ has only a finite number of minimal prime
ideals $\mathfrak{p}_{i}$; as $A$ is reduced, the intersection of the $\mathfrak{p}_{i}$ reduces to `0`, and to say that
$t$ is regular is therefore equivalent to saying that $t$ does not belong to any of the $\mathfrak{p}_{i}$; one
concludes by the reasoning of `(I, 7.1.9.1)`. When $A$ is Noetherian, saying that $U = X - Y$ (where $Y =
V(\mathfrak{i})$ is closed in $X$) is schematically dense means `(5.10.2)` that $Y$ does not meet
$Ass(\mathcal{O}_{X})$, and by virtue of Bourbaki, _Alg. comm._, chap. IV, §1, n° 4, prop. 8, this entails the existence
of a $t \in \mathfrak{i}$ such that $t$ is $A$-regular, hence $U \supset D(t)$.

One has moreover proved in the course of this proof the

**Corollary (20.2.12).**

<!-- label: IV.20.2.12 -->

*If $X = \operatorname{Spec}(A)$, where $A$ is Noetherian, or reduced and having only a finite number of minimal prime
ideals, the schematically dense opens in $X$ are those which contain an open of the form $D(t)$, where $t$ is regular in
$A$, and $M(X) = M'(X)$ is the total ring of fractions $S^{-1}A$, where $S$ is the set of regular elements of $X$.*

**Remarks (20.2.13).**

<!-- label: IV.20.2.13 -->

(i) Let $\phi$ be an element of $M(X)$, $\phi'$ its image in `M'(X)`; one has evidently, by definition (`(20.1.4)` and
`(20.2.8)`), $dom(\phi) \subset dom(\phi')$; but in fact one has equality $dom(\phi) = dom(\phi')$, since there exists a
section of $\mathcal{O}_{X}$ over $dom(\phi')$ belonging to the class $\phi'$, and the corresponding meromorphic
function equals $\phi$ `(20.2.11, (i))`, so $dom(\phi') \subset dom(\phi)$.

(ii) One has already noted that when $X$ is reduced, one has $\mathcal{M}'_{X} = \mathcal{R}(X)$ (sheaf of rational
functions on $X$ `(I, 7.3.2)`); if moreover the irreducible components of $X$ form a locally finite set, one has
$\mathcal{M}_{X} = \mathcal{M}'_{X} = \mathcal{R}(X)$. In general, since every schematically dense open set is dense,
one has a canonical homomorphism $\mathcal{M}'_{X} \to \mathcal{R}(X)$, but even when $X$ is locally Noetherian, this
homomorphism is not necessarily injective. For example, if $X = \operatorname{Spec}(A)$, where $A$ is a Noetherian ring
such that $Ass(A)$ contains immersed prime ideals (which entails that $A$ is not reduced), one has seen that $M(X)$ and
`M'(X)` identify with the total ring of fractions $S^{-1}A$,

<!-- original page 236 -->

where $S$ is the set of regular elements of $A$, the complement of the union of the ideals $\mathfrak{p} \in Ass(A)$; on
the other hand, $R(X)$ identifies with $Q^{-1}A$, where $Q$ is the complement of the union of the minimal prime ideals
of $A$ `(I, 7.1.9)`, and the canonical homomorphism $A \to Q^{-1}A$ (and *a fortiori* $S^{-1}A \to Q^{-1}A$) is
therefore not injective, since there exist in $A - Q$ elements $\neq 0$ of $A$ annihilated by elements of $Q$ (Bourbaki,
_Alg. comm._, chap. IV, §1, n° 1, cor. 2 of prop. 1).

(iii) One will note that even when $X$ is locally Noetherian, the $\mathcal{O}_{X}$-Module $\mathcal{M}_{X}$ is not
necessarily quasi-coherent. Consider for example a Noetherian local ring $A$ of dimension $\geq 2$, whose maximal ideal
$\mathfrak{m}$ is such that $\mathfrak{m} \in Ass(A)$ and such that, on setting $X = \operatorname{Spec}(A)$, the scheme
induced on the open $U$ of $X$, complement of ${\mathfrak{m}}$, is integral. The only regular elements of $A$ are then
the invertible elements, so $\Gamma(X, \mathcal{M}_{X}) = M(X) = A$; if $\mathcal{M}_{X}$ were quasi-coherent, it would
therefore equal $\mathcal{O}_{X}$, but as $U$ is an integral scheme, $\mathcal{M}_{X} | U = R(U)$ is a simple sheaf
`(I, 7.3.5)`, whereas $\mathcal{O}_{X}$ is not a simple sheaf since $\dim(A) \geq 2$.

It remains to give an example of a ring $A$ having the preceding properties. It suffices to consider an integral local
ring $B$ of dimension $\geq 2$ and residue field $k$, and to take $A = B \oplus k$ with the multiplication law $(b,
x)(b', x') = (bb', bx' + b'x)$.

(iv) If $X$ is locally Noetherian, it follows from `(5.10.2)` that the schematically dense opens in $X$ are those which
contain the set $Ass(\mathcal{O}_{X})$.

**(20.2.14).** Let $X$ be a prescheme, $\mathcal{F}$ a quasi-coherent and *strictly torsion-free*
$\mathcal{O}_{X}$-Module `(20.1.5)`, so that $\mathcal{F}$ identifies with an $\mathcal{O}_{X}$-submodule of
$\mathcal{M}_{X}(\mathcal{F})$. For every meromorphic section $u$ of $\mathcal{F}$ over $X$, one calls *Ideal of
denominators of $u$* the annihilator $\mathcal{J}$ of the section `ū` image of $u$ in $\mathcal{M}_{X}(\mathcal{F}) /
\mathcal{F}$. The Ideal $\mathcal{J}$ is quasi-coherent: indeed, the question being local on $X$, one may restrict to
the case where $X$ is affine, and there exists a section $s \in \Gamma(X, \mathcal{S}(\mathcal{O}_{X}))$ such that $v =
su \in \Gamma(X, \mathcal{F})$. To say that, for an open $U \subset X$, a section $f \in \Gamma(U, \mathcal{O}_{X})$
belongs to $\Gamma(U, \mathcal{J})$ means that $f (u | U) \in \Gamma(U, \mathcal{F})$, and since $s | U$ is a regular
element of $\Gamma(U, \mathcal{O}_{X})$ and $\mathcal{F}$ is strictly torsion-free, the preceding relation is again
equivalent to $f ((sv) | U) \in \Gamma(U, s\mathcal{F})$; if $\bar{v}$ is the section of $\mathcal{F} / s\mathcal{F}$
which is the canonical image of $v$, one sees therefore that $\mathcal{J}$ is the kernel of the homomorphism
$\mathcal{O}_{X} \to \mathcal{F} / s\mathcal{F}$ obtained by multiplication by the section $\bar{v}$. As $\mathcal{F} /
s\mathcal{F}$ is quasi-coherent, so is $\mathcal{J}$.

It follows at once from the foregoing definition that $dom(u)$ is the open complement of the closed subprescheme of $X$
defined by the Ideal of denominators of $u$.

**Proposition (20.2.15).**

<!-- label: IV.20.2.15 -->

*Let $f : X' \to X$ be a morphism, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, $\phi$ a section of
$\mathcal{M}_{X}(\mathcal{F})$ over $X$ `(20.1.11)`. Then $f^{-1}(dom(\phi))$ is schematically dense in $X'$.*

The question being evidently local on $X$ and $X'$, one may suppose $X = \operatorname{Spec}(A)$, $X' =
\operatorname{Spec}(A')$ affine, $\mathcal{F} = \tilde{M}$, and $\phi = h \otimes (1/s)$, where $h \in M$ and $s$ is a
regular element of $A$ whose image $s'$ in $A'$ is a regular element. One knows then `(20.2.9)` that $D(s')$ is a
schematically dense open in $X'$, and it is the inverse image under $f$ of $D(s)$, which is contained in $dom(\phi)$.

**Remark (20.2.16).**

<!-- label: IV.20.2.16 -->

When $Y$ is not separated, the presheaf $U \mapsto Ps.hom_{S}(U, Y)$ on $X$ is not necessarily a sheaf, even when $X$ is
Noetherian, as the following example shows. We shall take for $X$ a spectrum of a semi-local Noetherian ring $A$ of
dimension $\geq 2$, having exactly two maximal ideals

<!-- original page 237 -->

$\mathfrak{m}'$, $\mathfrak{m}''$ (so that $X$ has exactly two closed points $x'$, `x''`), such that $\mathfrak{m}'$ and
$\mathfrak{m}''$ belong to $Ass(A)$ and such that the open $U = X - {x', x''}$ is integral. Let $U' = X - {x'}$, $U'' =
X - {x''}$, so that $U = U' \cap U''$. Note that the only schematically dense opens in $X$ are those that contain $x'$
and `x''` `(20.2.13, (iv))`, so they necessarily equal $X$. To have a counter-example, it will therefore suffice to
define two $S$-morphisms $u' : U' \to Y$, $u'' : U'' \to Y$ (with $S = X$) whose restrictions to $U$ belong to the same
pseudo-morphism of $U$ into $Y$, but which are such that, for every neighbourhood $V'$ of `x''` in $U'$ and every
neighbourhood `V''` of $x'$ in `U''`, the restrictions of $u'$ and `u''` to $V' \cap V''$ are distinct. For this,
consider an irreducible closed subset $Z$ of $X$ containing $x'$ and `x''`, distinct from $X$; let $Y$ be the
$X$-prescheme obtained by gluing two preschemes $Y'$, `Y''` isomorphic to $X$ along the everywhere dense open $X - Z$
`(I, 2.3.1)`. One will take for $u'$ and `u''` respectively the restrictions to $U'$ and `U''` of the inverse
isomorphisms of the structural isomorphisms $Y' \xrightarrow{\sim} X$, $Y'' \xrightarrow{\sim} X$. Since $V'$ and `V''`
contain the generic point of $Z$, the restrictions of $u'$ and `u''` to $V' \cap V''$ are distinct, but the restrictions
of $u'$ and `u''` to $U - (U \cap Z)$ are equal, and $U - (U \cap Z)$ is a dense open in $U$, hence schematically dense
since $U$ is reduced.

It remains then only to define $A$ and $Z$ so as to have the preceding properties. Let $X_{0} = \operatorname{Spec}(B)$
be an integral affine scheme (for example the affine plane over a field $k$), $Y$ an irreducible closed subset of `X_0`
(for example an affine line) containing two distinct closed points $x'$ and `x''`, corresponding to maximal ideals
$\mathfrak{n}'$, $\mathfrak{n}''$ of $B$. Consider the ring $C = B \oplus (B/\mathfrak{n}' \oplus B/\mathfrak{n}'')$
with the multiplication $(b, z)(b', z') = (bb', bz' + b'z)$. If $X_{1} = \operatorname{Spec}(C)$, one has $X_{0} =
(X_{1})_{red}$ and `X_1` is reduced except at the points $x'$, `x''`. It then suffices to take $A = R^{-1}C$, where $R$
is the complement of the union of the maximal ideals of $C$ at the points $x'$, `x''`, and for $Z$ the trace of $Y$ on
$X = \operatorname{Spec}(A)$.

### 20.3. Composition of pseudo-morphisms

**(20.3.1).** Let $X$, $Y$, $Z$ be three preschemes, $\omega$ a pseudo-morphism of $X$ into $Y$, $f : Y \to Z$ a
morphism. It is clear that if $U'$, `U''` are two schematically dense opens in $X$, $u' : U' \to Y$, $u'' : U'' \to Y$
two morphisms of the class $\omega$, the morphisms $f \circ u'$ and $f \circ u''$ are equivalent (for the relation
defined in `(20.2.1)`); hence, for all morphisms $u$ of the class $\omega$, the morphisms $f \circ u$ belong to one and
the same equivalence class, which one denotes $f \circ \omega$ and which one calls the *pseudo-morphism of $X$ into $Z$
composed of $f$ and $\omega$*. One has $dom(f \circ \omega) = dom(\omega)$. If $g : Z \to T$ is a morphism, it is clear
that $g \circ (f \circ \omega) = (g \circ f) \circ \omega$.

**(20.3.2).** Suppose now given a pseudo-$S$-morphism $\omega$ of $X$ into $Y$, where $Y$ is separated over $S$, so that
there exists an $S$-morphism $u : dom_{S}(\omega) \to Y$ of the class $\omega$ `(20.2.4)`. Let $f : X' \to X$ be an
$S$-morphism such that the open $V = f^{-1}(dom_{S}(\omega))$ is schematically dense in $X'$; one then says that the
class (for the equivalence relation of `(20.2.1)`) of the $S$-morphism $u \circ (f | V)$ (a class defined by virtue of
the foregoing hypothesis) is the *pseudo-$S$-morphism composed of $\omega$ and $f$*, and one denotes it $\omega \circ
f$; it is clear that one has

$$ (20.3.2.1) f^{-1}(dom_{S}(\omega)) \subset dom_{S}(\omega \circ f). $$

For $f : X' \to X$ given, one denotes by $Ps.hom_{S}(X, Y)^{f}$ the set of pseudo-$S$-morphisms $\omega$ of $X$ into $Y$
satisfying the foregoing condition. If $\omega$ is such a pseudo-$S$-morphism, it is clear that for every open $V$ of
$X$,

```text
                         f⁻¹(dom_S(ω | V)) = f⁻¹(V ∩ dom_S(ω)) = f⁻¹(V) ∩ f⁻¹(dom_S(ω))
```

is schematically dense in $f^{-1}(V)$, so, if $f^{V} : f^{-1}(V) \to V$ is the restriction of $f$, the composite
$(\omega | V) \circ f^{V}$ is defined and equal to $(\omega \circ f) | f^{-1}(V)$. One thus defines a

<!-- original page 238 -->

canonical restriction map $Ps.hom_{S}(X, Y)^{f} \to Ps.hom_{S}(V, Y)^{f^{V}}$, which permits one to define a presheaf of
sets $V \mapsto Ps.hom_{S}(V, Y)^{f^{V}}$ on $X$, a sub-presheaf of $V \mapsto Ps.hom_{S}(V, Y)$, whence an associated
sheaf of sets which one denotes $\mathcal{Ps}.hom_{S}(X, Y)^{f}$. Moreover, for every open $V$ of $X$, one has a map
$\omega \mapsto \omega \circ f^{V}$ from $Ps.hom_{S}(V, Y)^{f^{V}}$ to $Ps.hom_{S}(f^{-1}(V), Y)$, which therefore
defines an $f$-morphism of sheaves of sets

```text
                         𝒫𝓈.hom_S(X, Y)^f → 𝒫𝓈.hom_S(X', Y).
```

**(20.3.3).** Let now $f' : X'' \to X'$ be an $S$-morphism such that the open $f'^{-1}(f^{-1}(dom_{S}(\omega)))$ is
schematically dense in `X''`; then $\omega \circ (f \circ f')$ is defined and $u \circ f \circ f'$ belongs to this
pseudo-$S$-morphism; moreover, by virtue of `(20.3.2.1)`, $f'^{-1}(dom_{S}(\omega \circ f))$ is *a fortiori*
schematically dense in `X''`, so $(\omega \circ f) \circ f'$ is also defined and $u \circ f \circ f'$ belongs to this
pseudo-$S$-morphism, so one has $(\omega \circ f) \circ f' = \omega \circ (f \circ f')$.

On the other hand, for every $S$-morphism $g : Y \to Z$, one has $dom_{S}(g \circ \omega) = dom_{S}(\omega)$ `(20.3.1)`,
so $(g \circ \omega) \circ f$ is defined, and $g \circ u \circ f$ belongs to this pseudo-$S$-morphism, which shows that
$(g \circ \omega) \circ f = g \circ (\omega \circ f)$.

**(20.3.4).** The most important case in the definition `(20.3.2)` is the one where $\mathcal{Ps}.hom_{S}(X, Y)^{f} =
\mathcal{Ps}.hom_{S}(X, Y)$: for this it suffices that for every open $U$ of $X$ and every open $V$ schematically dense
in $U$, $f^{-1}(V)$ be schematically dense in $f^{-1}(U)$; when this is the case, then, for every open $U$ of $X$ and
every pseudo-$S$-morphism $\omega : U \to Y$, one may define the composite $\omega \circ f^{U}$, *even if $Y$ is not
separated over $S$*. Indeed, if $u' : U' \to Y$ and $u'' : U'' \to Y$ are two morphisms of the class $\omega$, they
coincide on an open `U_0` schematically dense in $U$, hence the composite morphisms $f^{-1}(U') \to U' \to Y$ and
$f^{-1}(U'') \to U'' \to Y$ coincide on $f^{-1}(U_{0})$, which is by hypothesis schematically dense in $f^{-1}(U)$; one
may therefore define $\omega \circ f^{U}$ as the class of any of the morphisms $f^{-1}(U') \to U' \to Y$, where $u'$
belongs to $\omega$.

**Proposition (20.3.5).**

<!-- label: IV.20.3.5 -->

*Let $X$, $X'$ be two preschemes, $f : X' \to X$ a morphism. Then, in each of the following three cases, for every open
$U$ of $X$ and every open $V$ schematically dense in $U$, $f^{-1}(V)$ is schematically dense in $f^{-1}(U)$:*

*(i) $f$ is flat and locally of finite presentation.*

*(ii) $f$ is flat and the underlying space of $X$ is locally Noetherian.*

*(iii) $X'$ is reduced, the set of irreducible components of $X$ is locally finite, and every irreducible component of
$X'$ dominates an irreducible component of $X$.*

Assertion (i) follows from `(11.10.5, (ii), b))`; assertion (ii) follows from `(11.10.5, (ii), a))`, since then every
open $V$ in $U$ is retrocompact, in other words the canonical injection $j : V \to U$ is a quasi-compact morphism.
Finally, to prove (iii), note that since $X'$ is reduced, it suffices to show that for every open $U$ of $X$ and every
open $V$ dense in $U$, $f^{-1}(V)$ is dense in $f^{-1}(U)$. Now, for $f^{-1}(V)$ to be dense in $f^{-1}(U)$, it suffices
that $f^{-1}(V)$ contain all the maximal points of $X'$ belonging to $f^{-1}(U)$; the conclusion therefore follows from
the hypothesis that the image under $f$ of every

<!-- original page 239 -->

maximal point of $X'$ belonging to $f^{-1}(U)$ is a maximal point of $X$ belonging to $U$, hence to $V$ since the set of
irreducible components of $X$ is locally finite.

**(20.3.6).** Let $X$, $Y$ be two $S$-preschemes; suppose that $X$ satisfies one of the two following hypotheses:

a) *$X$ is locally Noetherian*;

b) *$X$ is reduced and the set of its irreducible components is locally finite*.

Then, for every $x \in X$, the canonical $S$-morphism $j : \operatorname{Spec}(\mathcal{O}_{X,x}) \to X$ is flat and
satisfies condition (ii) of `(20.3.5)` in case a), condition (iii) of `(20.3.5)` in case b). For every
pseudo-$S$-morphism $\omega$ of $X$ into $Y$, the composite $\omega \circ j$ is therefore defined and is a
pseudo-$S$-morphism of $\operatorname{Spec}(\mathcal{O}_{X,x})$ into $Y$, called the *restriction of $\omega$ to
$\operatorname{Spec}(\mathcal{O}_{X,x})$*. Note now that if $X$ satisfies condition a) (resp. b)) of `(20.3.6)`, so does
every prescheme induced on an open $U$ of $X$ containing $x$. By passage to the inductive limit, one therefore deduces,
from the canonical maps `Ps.hom_S(U, Y) → Ps.hom_S(Spec(𝒪_{X,x}), Y)` thus obtained, a canonical map

```text
  (20.3.6.1)             (𝒫𝓈.hom_S(X, Y))_x → Ps.hom_S(Spec(𝒪_{X,x}), Y)
```

where the first member is the fibre at the point $x$ of the sheaf $\mathcal{Ps}.hom_{S}(X, Y)$, the set of germs at $x$
of pseudo-$S$-morphisms from open neighbourhoods of $x$ into $Y$.

**Proposition (20.3.7).**

<!-- label: IV.20.3.7 -->

*Under the hypotheses of `(20.3.6)`, the canonical map `(20.3.6.1)` is injective. If moreover $Y$ is locally of finite
presentation over $S$, the map `(20.3.6.1)` is bijective.*

By application of the method of `(8.1.2, a))`, this proposition will be a particular case of the following:

**Proposition (20.3.8).**

<!-- label: IV.20.3.8 -->

*With the notations of `(8.8.1)`, suppose $X_{\alpha}$ quasi-compact (resp. quasi-compact and quasi-separated) and
$Y_{\alpha}$ locally of finite type (resp. locally of finite presentation) over $S_{\alpha}$. Suppose moreover that one
of the following conditions is satisfied:*

*(i) The transition morphisms $S_{\lambda} \to S_{\alpha}$ (for $\lambda \geq \alpha$) are flat, and the $X_{\lambda}$
and $X$ are Noetherian.*

*(ii) The $X_{\lambda}$ are reduced, the set of irreducible components of $X$ and of each of the $X_{\lambda}$ is
finite, and, for $\lambda \geq \mu$, every irreducible component of $X_{\lambda}$ dominates an irreducible component of
$X_{\mu}$.*

*Then the canonical map*

```text
  (20.3.8.1)             lim Ps.hom_{S_λ}(X_λ, Y_λ) → Ps.hom_S(X, Y)
```

*is injective (resp. bijective).*

Note first that, in case (i), the morphisms $X_{\lambda} \to X_{\mu}$ (for $\lambda \geq \mu$) and $X \to X_{\lambda}$
are flat, so it follows from `(20.3.4)` and `(20.3.5)` that the canonical maps

```text
                         Ps.hom_{S_μ}(X_μ, Y_μ) → Ps.hom_{S_λ}(X_λ, Y_λ)
```

<!-- original page 240 -->

for $\lambda \geq \mu$ and $Ps.hom_{S_{\lambda}}(X_{\lambda}, Y_{\lambda}) \to Ps.hom_{S}(X, Y)$ are defined (without
any separation hypothesis on the $Y_{\lambda}$ or $Y$); the same is therefore true of the map `(20.3.8.1)`. The
proposition will follow from the following lemma:

**Lemma (20.3.8.2).**

<!-- label: IV.20.3.8.2 -->

*With the notations of `(8.8.1)`, suppose $X_{\alpha}$ quasi-compact, and let $U_{\alpha}$ be an open in $X_{\alpha}$;
let $U_{\lambda}$ and $U$ be its inverse images in $X_{\lambda}$ and $X$ for $\lambda \geq \alpha$. Suppose that one of
the conditions (i), (ii) of `(20.3.8)` is satisfied. Then, for $U$ to be schematically dense in $X$, it is necessary and
sufficient that there exist $\lambda \geq \alpha$ such that $U_{\lambda}$ is schematically dense in $X_{\lambda}$, and
in this case $U_{\mu}$ is schematically dense in $X_{\mu}$ for $\mu \geq \lambda$.*

Suppose first that condition (i) is satisfied; denote by $j_{\lambda} : U_{\lambda} \to X_{\lambda}$ and $j : U \to X$
the canonical injections, by $\mathcal{J}_{\lambda}$ the kernel of the canonical homomorphism $\mathcal{O}_{X_{\lambda}}
\to (j_{\lambda})_{*}(\mathcal{O}_{U_{\lambda}})$. The immersion $j_{\lambda}$ being quasi-compact and quasi-separated,
$(j_{\lambda})_{*}(\mathcal{O}_{U_{\lambda}})$ is a quasi-coherent $\mathcal{O}_{X_{\lambda}}$-Module, so
$\mathcal{J}_{\lambda}$ is a quasi-coherent Ideal of $\mathcal{O}_{X_{\lambda}}$, and since $X_{\lambda}$ is Noetherian,
$\mathcal{J}_{\lambda}$ is coherent, hence of finite type. On the other hand, the transition morphism $p_{\mu \lambda} :
X_{\mu} \to X_{\lambda}$ (resp. $p_{\lambda} : X \to X_{\lambda}$) being flat, it follows from `(2.3.1)` that one may
identify $\mathcal{J}_{\mu}$ with $p_{\mu \lambda}*(\mathcal{J}_{\lambda})$ (resp. $\mathcal{J}$ with
$p_{\lambda}*(\mathcal{J}_{\lambda})$). The assertion then follows from the definition of a schematically dense open and
from `(8.5.8, (ii))`.

To establish `(20.3.8.2)` when condition (ii) is satisfied, we shall first prove two lemmas.

**Lemma (20.3.8.3).**

<!-- label: IV.20.3.8.3 -->

*Under the hypotheses of `(8.2.2)`, let $M_{\lambda}$ (resp. $M$) be the set of maximal points of $S_{\lambda}$ (resp.
$S$). Suppose that for every $\lambda$, the set $M_{\lambda}$ is finite, and that the $M_{\lambda}$ form a projective
system of sets. Then $M$ is the projective limit of the system of $M_{\lambda}$.*

Let us first show that a point $s \in \lim M_{\lambda}$ is maximal in $S$: indeed, if $s'$ is a generization of $s$, the
image $s'_{\lambda}$ of $s'$ in $S_{\lambda}$ is a generization of the image $s_{\lambda}$ of $s$, hence equal to
$s_{\lambda}$ for every $\lambda$, which implies $s' = s$, since the underlying set of $S$ is the projective limit of
the underlying sets of the $S_{\lambda}$ `(8.2.9)`. Conversely, let $s$ be a maximal point of $S$ and prove that it
belongs to $\lim M_{\lambda}$. Let $s_{\lambda}$ be the image of $s$ in $S_{\lambda}$, $M'_{\lambda}$ the set of maximal
points of $S_{\lambda}$ which are generizations of $s_{\lambda}$; the $M'_{\lambda}$ are non-empty finite sets, which
form a projective system, so $M' = \lim M'_{\lambda}$ is non-empty and the map $M' \to M'_{\lambda}$ is surjective
(Bourbaki, _Ens._, chap. III, 2nd ed., §7, n° 4, Example I). On the other hand, one has
`Spec(𝒪_{S,s}) = lim Spec(𝒪_{S_λ, s_λ})` by virtue of `(8.2.12)` and `(8.2.9)`, so the points of $\lim M'_{\lambda}$ are
also maximal points of $\operatorname{Spec}(\mathcal{O}_{S,s})$ by the first part of the reasoning. Hence $M' = \lim
M'_{\lambda}$ necessarily reduces to the point $s$; one concludes that $M'_{\lambda}$ reduces to the point
$s_{\lambda}$, and consequently the $s_{\lambda}$ are maximal in the $S_{\lambda}$, which finishes the proof of the
lemma.

**Lemma (20.3.8.4).**

<!-- label: IV.20.3.8.4 -->

*With the hypotheses being those of `(20.3.8.3)`, suppose moreover $S_{\alpha}$ quasi-compact; let $U_{\alpha}$ be an
open set of $S_{\alpha}$, and let $U_{\lambda}$ and $U$ be its inverse images in $S_{\lambda}$ for $\lambda \geq \alpha$
and in $S$. If $U_{\alpha}$ is dense in $S_{\alpha}$, $U_{\lambda}$ is dense in $S_{\lambda}$ for $\lambda \geq \alpha$
and $U$ is dense in $S$. Conversely, if $U$ is dense in $S$ and if moreover the set $M$ of maximal points of $S$ is
finite, there exists $\lambda \geq \alpha$ such that $U_{\lambda}$ is dense in $S_{\lambda}$.*

Indeed, since $M_{\alpha}$ is finite, the hypothesis that $U_{\alpha}$ is dense in $S_{\alpha}$ entails that

<!-- original page 241 -->

$M_{\alpha} \subset U_{\alpha}$, hence $M_{\lambda} \subset U_{\lambda}$ for $\lambda \geq \alpha$ and $M \subset U$ by
virtue of `(20.3.8.3)`, which proves the first assertion. Conversely, suppose $M$ finite and $U$ dense in $S$, hence $M
\subset U$; note that the $U_{\lambda}$ are open, hence ind-constructible, and the $M_{\lambda}$ finite, hence
pro-constructible `(1.9.6)`. The second assertion then follows from `(8.3.2)`.

**(20.3.8.5) End of the proof of (20.3.8.2).** Suppose condition (ii) verified, and note that $X$ is then reduced by
virtue of `(8.7.1)`; it amounts to the same to say that $U_{\lambda}$ (resp. $U$) is schematically dense in
$X_{\lambda}$ (resp. $X$) or that it is dense in $X_{\lambda}$ (resp. $X$), and the conclusion follows from `(20.3.8.4)`
applied to the $X_{\lambda}$ and to $X$.

**(20.3.8.6) End of the proof of (20.3.8).** To show that the map `(20.3.8.1)` is injective, consider two morphisms
$u'_{\alpha}$, $u''_{\alpha}$ from a schematically dense open $U_{\alpha} \subset X_{\alpha}$ into $Y_{\alpha}$, and
suppose that their images $u'$, `u''`, morphisms of $U$ into $Y$, coincide on a schematically dense open $V$ of $U$.
Moreover, in either of the hypotheses (i), (ii), one may suppose $V$ quasi-compact; this is evident if $X$ is
Noetherian; otherwise, as $X$ has only a finite number of maximal points and is reduced, it suffices to replace $V$ by
the union of a finite number of affine open neighbourhoods of these maximal points (contained in $V$ by hypothesis).
Then there exists $\lambda \geq \alpha$ such that $V$ is the inverse image of a quasi-compact open $V_{\lambda}$ of
$X_{\lambda}$ `(8.2.11)`, and it follows from `(20.3.8.2)` that, on taking $\lambda$ large enough, one may suppose
$V_{\lambda}$ schematically dense in $X_{\lambda}$. It then follows from `(8.8.2, (i))` that, on taking $\lambda$ large
enough, $u'_{\lambda}$ and $u''_{\lambda}$ coincide on $V_{\lambda}$, hence belong to the same pseudo-homomorphism.

Let us finally prove that the map `(20.3.8.1)` is surjective. Consider now a morphism $u$ from a schematically dense
open $U$ of $X$ into $Y$; as above, one may suppose $U$ quasi-compact and quasi-separated ($U$ may be replaced, in case
(ii), by a union of a finite number of pairwise disjoint affine opens). One may then again suppose that there exists
$\lambda \geq \alpha$ such that $U$ is the inverse image of a quasi-compact open $U_{\lambda}$ of $X_{\lambda}$
`(8.2.11)` which is automatically quasi-separated, and by `(20.3.8.2)` one may further suppose that $U_{\lambda}$ is
schematically dense in $X_{\lambda}$. Since the $Y_{\lambda}$ are supposed locally of finite presentation, it follows
from `(8.8.2, (i))` that there exists $\lambda$ such that $u$ is the image of a morphism $u_{\lambda} : U_{\lambda} \to
Y_{\lambda}$; whence the conclusion.

**Remarks (20.3.8.7).**

<!-- label: IV.20.3.8.7 -->

(i) To prove that the map `(20.3.8.1)` is injective, it is not necessary, under hypothesis (i) of `(20.3.8)`, to suppose
$X$ Noetherian. Indeed, the lemma `(20.3.8.2)` does not use this hypothesis. With the notations of `(20.3.8.6)`, let
$Z_{\lambda}$ be the sub-prescheme of coincidences of $u'_{\lambda}$ and $u''_{\lambda}$, and let $Z$ be the
sub-prescheme of coincidences of $u'$ and `u''`; it follows from the definition `(17.4.5)` and from `(I, 3.3.10.1)` that
$Z$ is the projective limit of the $Z_{\lambda}$ for $\mu \geq \lambda$. Now, by hypothesis, $Z$ majorizes a
schematically dense open in $X$; it follows that $Z$ is itself induced on an open of $X$ by virtue of the following
lemma:

**Lemma (20.3.8.8).**

<!-- label: IV.20.3.8.8 -->

*Let $T$ be a prescheme. Then every sub-prescheme $W$ of $T$ which majorizes a schematically dense open $V$ of $T$ is
induced on a (schematically dense) open of $T$.*

Indeed, the subspace of $T$ underlying $W$ is locally closed, hence open

<!-- original page 242 -->

in its closure, which already proves that the space underlying $W$ is open in $T$; the conclusion then follows from
`(11.10.1, c))`.

This lemma being established, one concludes that for $\mu \geq \lambda$ large enough, $Z_{\mu}$ is induced on an open of
$X_{\mu}$ by virtue of `(8.6.3)`, since $Z_{\lambda}$, as sub-prescheme of a Noetherian prescheme, is of finite
presentation over $X_{\lambda}$ `(1.6.2)`, and the same therefore holds for the $Z_{\mu}$ for $\mu \geq \lambda$ over
$X_{\mu}$ and for $Z$ over $X$. One may now apply `(20.3.8.2)` which shows that for $\mu \geq \lambda$ large enough, $Z$
is schematically dense in $X$, whence the conclusion.

(ii) If, under hypothesis (i) of `(20.3.8)`, one suppresses the condition that $X$ is Noetherian, one sees that the
reasoning of `(20.3.8.6)` still shows that the image of `(20.3.8.1)` is formed of the pseudo-$S$-morphisms having a
representative which is an $S$-morphism $U \to Y$, where $U$ is schematically dense in $X$ and quasi-compact and
quasi-separated.

**Corollary (20.3.9).**

<!-- label: IV.20.3.9 -->

*Suppose one or the other hypothesis a), b) of `(20.3.6)` on $X$ is satisfied, and that $Y$ is locally of finite
presentation over $S$. Then, for a pseudo-$S$-morphism $\omega$ of $X$ into $Y$ to be defined at the point $x$
`(20.2.3)`, it is necessary and sufficient that its restriction to $\operatorname{Spec}(\mathcal{O}_{X,x})$ be
everywhere defined (in other words, be an $S$-morphism from $\operatorname{Spec}(\mathcal{O}_{X,x})$ into $Y$).*

The following result, which we shall use in the proof of `(20.3.11)`, uses the theory of faithfully flat descent of
chap. VI. The reader can check that the results of `(20.3)` will not be used in this theory.

**Lemma (20.3.10).**

<!-- label: IV.20.3.10 -->

*Let $f : X' \to X$ be a faithfully flat and quasi-compact $S$-morphism, $X'' = X' \times_{X} X'$, $p_{1}$ and $p_{2}$
the canonical projections of `X''` onto $X'$, $Y$ a prescheme separated over $S$. Let $U$ be an open of $X$, $U' =
f^{-1}(U)$, $U'' = f^{-1}(U') = p^{-1}_{1}(U') \cap p^{-1}_{2}(U')$, and suppose that `U''` is schematically dense in
`X''`. Let $g : U \to Y$ be an $S$-morphism; then, if $g \circ (f | U')$ extends to an $S$-morphism $X' \to Y$, $g$
extends to an $S$-morphism $X \to Y$.*

One will note that the hypotheses entail that $U$ (resp. $U'$) is schematically dense in $X$ (resp. $X'$)
`(11.10.5, (i))`; one may therefore again say that if $\omega$ denotes the pseudo-$S$-morphism class of $g$, the
statement of `(20.3.10)` means that if $\omega \circ f$ is everywhere defined, so is $\omega$.

To prove `(20.3.10)`, denote by $g'$ an $S$-morphism $X' \to Y$ which extends $g \circ (f | U')$, and set $g'_{i} = g'
\circ p_{i} : X'' \to Y$ ($i = 1, 2$). If one sets $f'' = f \circ p_{1} = f \circ p_{2} : X'' \to X$, it is clear that
$g'_{1}$ and $g'_{2}$ coincide on `U''` with $g \circ (f'' | U'')$. But since $Y$ is separated over $S$ and `U''`
schematically dense in `X''`, one has $g'_{1} = g'_{2}$ `(11.10.1, d))`. Since $f$ is faithfully flat and quasi-compact,
it follows from the theory of descent (chap. VI) that there exists a unique $S$-morphism $h : X \to Y$ such that $h
\circ f = g'$; since the restriction $U' \to U$ of $f$ is a faithfully flat and quasi-compact morphism and that $U'' =
U' \times_{U} U'$, the foregoing uniqueness result, applied to $U$ in place of $X$, shows that $h | U = g$, which proves
the lemma.

**Proposition (20.3.11).**

<!-- label: IV.20.3.11 -->

*Let $Y$ be an $S$-prescheme separated over $S$, $\omega$ a pseudo-$S$-morphism of $X$ into $Y$, $f : X' \to X$ an
$S$-morphism. Suppose that $f$ is flat, and that one of the following conditions is satisfied:*

<!-- original page 243 -->

*(i) $f$ is an open morphism, or surjective and quasi-compact, and $dom_{S}(\omega)$ contains an open $U$ schematically
dense in $X$ and retrocompact in $X$.*

*(ii) $f$ is locally of finite presentation.*

*(iii) $Y$ is locally of finite presentation over $S$, and $X$ satisfies one of the conditions a), b) of `(20.3.6)`.*

*Then $f^{-1}(dom_{S}(\omega))$ is schematically dense in $X'$, so that $\omega \circ f$ is defined `(20.3.2)` and one
has*

$$ (20.3.11.1) dom_{S}(\omega \circ f) = f^{-1}(dom_{S}(\omega)). $$

Let us prove first that $f^{-1}(dom_{S}(\omega))$ is schematically dense in $X'$. The question being local on $X$ and
$X'$, one may suppose $X$ and $X'$ affine, and since $f$ is flat, it suffices to see, by virtue of
`(11.10.5, (ii), a))`, that $dom_{S}(\omega)$ contains an open set $U$ retrocompact and schematically dense in $X$. This
follows from the hypothesis in case (i), and from `(20.2.12)` in case (iii), taking into account that in an affine
scheme, every open of the form $D(t)$ is retrocompact; finally, in case (ii), one sees directly that
$f^{-1}(dom_{S}(\omega))$ is schematically dense in $X'$ by applying `(20.3.5, (i))`.

Let us now prove `(20.3.11.1)`, in other words that, for every point $x' \in dom_{S}(\omega \circ f)$, one has $x =
f(x') \in dom_{S}(\omega)$. Note first that one may restrict to the case where $f$ is *faithfully flat* and
quasi-compact. This is indeed the hypothesis in the second case of (i); in the other cases, the question is local on
$X'$, so one may suppose $X$ and $X'$ already affine, hence $f$ quasi-compact. In the first case of (i) and in case
(ii), $f$ is an open morphism `(11.3.1)`, so one may, by replacing $X$ by the open $f(X')$, suppose $f$ surjective,
hence faithfully flat. In case (iii), using `(20.3.9)`, one may restrict to proving that the restriction of $\omega$ to
$\operatorname{Spec}(\mathcal{O}_{X,x})$ is everywhere defined, and one may therefore replace $X$ by
$\operatorname{Spec}(\mathcal{O}_{X,x})$, $X'$ by $X' \times_{X} \operatorname{Spec}(\mathcal{O}_{X,x})$, and $f$ by its
restriction to this latter prescheme, which is a surjective morphism `(2.3.4)`, hence faithfully flat.

Suppose then $f$ faithfully flat and quasi-compact; with the notations of the lemma `(20.3.10)`, it suffices to see that
`U''` is schematically dense in `X''`, taking for $U$ an open schematically dense in $X$ and contained in
$dom_{S}(\omega)$; this will be the case, by virtue of `(11.10.5, (ii), a))`, if $U$ is taken retrocompact in $X$ (since
the morphism $f'' : X'' \to X$ is flat). Now the existence of such an open $U$ is part of the hypothesis in case (i); in
case (iii) it follows from `(20.2.12)` and from the fact that in an affine scheme $\operatorname{Spec}(A)$, every open
of the form $D(t)$ is retrocompact. Finally, in case (ii), let us take $U = dom_{S}(\omega)$ and show directly that
`U''` is schematically dense in `X''`: it suffices for this to note that $f'' : X'' \to X$ is flat and locally of finite
presentation and to apply `(11.10.5, (ii), b))`.

**Corollary (20.3.12).**

<!-- label: IV.20.3.12 -->

*Let $\phi$ be a pseudo-function on a prescheme $X$. Then, for every flat and locally of finite presentation morphism
$f : X' \to X$, the pseudo-function $\phi \circ f$ is defined and one has $dom(\phi \circ f) = f^{-1}(dom(\phi))$.*

<!-- original page 244 -->

**Remark (20.3.13).**

<!-- label: IV.20.3.13 -->

When $X$ satisfies one of the conditions a), b) of `(20.3.6)`, one has seen `(20.2.11)` that the pseudo-functions on $X$
identify with the meromorphic functions on $X$. By virtue of `(20.1.12)` and of `(20.2.13, (i))`, if one supposes only
that the morphism $f : X' \to X$ is flat, then, for every pseudo-function $\phi$ on $X$, $\phi \circ f$ is defined and
one has $dom(\phi \circ f) = f^{-1}(dom(\phi))$.

### 20.4. Properties of the domains of definition of rational maps

**(20.4.1).** Let $X$, $Y$ be two $S$-preschemes, $\omega$ a pseudo-$S$-morphism of $X$ into $Y$. Let $u$ be an
$S$-morphism $U \to Y$ belonging to $\omega$, where $U$ is schematically dense in $X$, and consider the graph
$\Gamma_{u}$, a sub-prescheme of $U \times_{S} Y$ `(I, 5.3.11)`, hence a sub-prescheme of $X \times_{S} Y$. Suppose that
this sub-prescheme admits a closure `(I, 9.5.11)` in $X \times_{S} Y$; if $j : \Gamma_{u} \to X \times_{S} Y$ is the
canonical injection, this will be the case when the $\mathcal{O}_{X \times_{S} Y}$-Module
$j_{*}(\mathcal{O}_{\Gamma_{u}})$ is quasi-coherent; it follows from the definition of the equivalence class $\omega$
`(20.2.1)` that $j_{*}(\mathcal{O}_{\Gamma_{u}})$ does not depend on the representative $u$ considered, hence the
closure prescheme of $\Gamma_{u}$ is then well determined by $\omega$; one says that this closed sub-prescheme of $X
\times_{S} Y$ is the *graph of the pseudo-$S$-morphism $\omega$*, and one denotes it $\Gamma_{\omega}$. One will note
that $\Gamma_{\omega}$ is defined if there exists a morphism $u : U \to Y$ of the class $\omega$ such that $U$ is
retrocompact in $X$ and if moreover $Y$ is quasi-separated over $S$, since then the injection $j$ is a quasi-compact and
quasi-separated morphism `((1.2.2)` and `(1.7.4))`; the first hypothesis will always be verified when $X$ is locally
Noetherian. Note also that when $X$ is reduced, so is $\Gamma_{u}$, which is isomorphic to $U$ `(I, 5.3.11)`; then
$\Gamma_{\omega}$ exists and is none other than the reduced sub-prescheme of $X \times_{S} Y$ whose underlying space is
the closure in $X \times_{S} Y$ of the space underlying $\Gamma_{u}$ `(I, 5.2.1 and 5.2.2)`.

Note finally that if $Y$ is separated over $S$, $\Gamma_{u}$ is closed in $U \times_{S} Y$ `(I, 5.4.3)`, hence is
induced by $\Gamma_{\omega}$ (when this latter exists) on the open $\Gamma_{\omega} \cap (U \times_{S} Y)$
`(I, 9.5.10)`; on the other hand, this induced prescheme is in general different from $\Gamma_{u}$ when $Y$ is not
separated. In particular, if $v : X \to Y$ is an $S$-morphism, the graph $\Gamma_{\omega}$ of the class $\omega$ of $v$
may be distinct from the graph $\Gamma_{v}$. Accordingly, we shall in what follows, when there is a question of the
graph of a pseudo-$S$-morphism, restrict to the case where $Y$ is separated over $S$.

**(20.4.2).** Suppose then $\Gamma_{\omega}$ defined and $Y$ separated over $S$; denote by $p$ and $q$ the restrictions
to $\Gamma_{\omega}$ of the canonical projections

```text
                              X ×_S Y
                              ╱      ╲
                             p        q
                            ╱          ╲
                           X            Y
```

Then, if $U \subset dom_{S}(\omega)$, the restriction $p^{-1}(U) \to U$ of $p$ is an isomorphism `(I, 5.3.11)`;
conversely, if $U$ is an open of $X$ having this property, and if $u$ is the inverse isomorphism of the restriction
$p^{-1}(U) \to U$ of $p$, $q \circ u$ is an $S$-morphism of $U$ into $Y$ which coincides with a morphism of the class
$\omega$ on $U \cap dom_{S}(\omega)$. One concludes that $dom_{S}(\omega)$ is the *largest open $U$ of $X$ such that the
restriction $p^{-1}(U) \to U$ of $p$ is an*

<!-- original page 245 -->

*isomorphism*. Let $v : dom_{S}(\omega) \to \Gamma_{\omega}$ be the $S$-morphism inverse of the restriction
$p^{-1}(dom_{S}(\omega)) \to dom_{S}(\omega)$ of $p$; one sometimes denotes $p^{-1}$ the pseudo-$S$-morphism of $X$ into
$\Gamma_{\omega}$, the class of $v$ (whose associated rational map `(20.2.13, (ii))` is then birational); as
$p^{-1}(dom_{S}(\omega))$ is the graph of the $S$-morphism $u = q \circ v : dom_{S}(\omega) \to Y$, it is schematically
dense in $\Gamma_{\omega}$ `(11.10.3, (iv))`, so $\omega$ may be regarded as the composite $q \circ p^{-1}$ `(20.3.2)`.
For every subset $M$ of the underlying space of $X$, one sometimes sets $\omega(M) = q(p^{-1}(M))$, which then amounts
to regarding $\omega$ as a map from $X$ into $\mathfrak{P}(Y)$ (or, as certain authors say, a "multivalued function").
One will note that when $x \in dom_{S}(\omega)$, $\omega({x})$ is the set `{u(x)}`; in general, for an arbitrary $x \in
X$, if one denotes by $s$ the image of $x$ in $S$, by $Y_{s}$ the fibre at the point $s$ of the structure morphism $Y
\to S$, the set $\omega({x})$ is a subset of the prescheme $Y_{s}$.

**(20.4.3).** In all the rest of this number, we restrict to the case where $X$ is *reduced*, so that there is then
identity between pseudo-$S$-morphisms and $S$-rational maps `(20.2.7)`. Moreover, the graph of every $S$-rational map of
$X$ into $Y$ is then defined `(20.4.1)`.

**Proposition (20.4.4).**

<!-- label: IV.20.4.4 -->

*Let $X$ be a locally integral $S$-prescheme, $Y$ an $S$-prescheme locally of finite type and separated over $S$,
$\omega$ an $S$-rational map of $X$ into $Y$, $p : \Gamma_{\omega} \to X$ the canonical projection. Then, if $x \in X$
is a normal point such that the set $p^{-1}(x)$ contains an isolated point, $\omega$ is defined at the point $x$.*

Indeed, the first projection $p_{1} : X \times_{S} Y \to X$ is then a separated morphism, locally of finite type, so the
same is true of its restriction $p : \Gamma_{\omega} \to X$, which is moreover birational; and since $\Gamma_{u}$ is
reduced and $X$ integral, $\Gamma_{\omega}$ is integral; it then follows from $(Err_{IV}, 30)$ that the hypothesis on
$x$ entails the existence of an open neighbourhood $U$ of $x$ such that the restriction $p^{-1}(U) \to U$ of $p$ is an
isomorphism; whence the conclusion `(20.4.2)`.

One will note that the statement `(20.4.4)` is the original formulation given by Zariski of his *Main theorem* (with the
restriction that he was restricting to algebraic schemes over a base field).

**Proposition (20.4.5).**

<!-- label: IV.20.4.5 -->

*The hypotheses and notations being those of `(20.4.4)`, suppose moreover $X$ normal, and let $X'$ be a reduced
prescheme, $f : X' \to X$ a morphism locally of finite type and universally open. Then $\omega \circ f$ is defined, and
one has $dom_{S}(\omega \circ f) = f^{-1}(dom_{S}(\omega))$ (in other words, if $x' \in X'$ and $x = f(x')$, then, for
$\omega$ to be defined at the point $x$, it is necessary and sufficient that $\omega \circ f$ be so at the point $x'$).*

As $X'$ is reduced and $f^{-1}(dom_{S}(\omega))$ everywhere dense in $X'$ by virtue of `(2.4.11)`, the composite $\omega
\circ f$ is defined; to prove that, when $\omega \circ f$ is defined at the point $x'$, $\omega$ is so at the point $x$,
one may evidently replace $X'$ by an open neighbourhood of $x'$, hence suppose $\omega \circ f$ everywhere defined;
moreover, as $f(X')$ is open in $X$, one may suppose $f$ surjective. By virtue of the hypothesis on $f$, the morphism
$f_{(Y)} : X' \times_{S} Y \to X \times_{S} Y$ is then open, hence $f_{(Y)}(\bar{M}) = \overline{f_{(Y)}(M)}$ for every
subset $M$ of $X \times_{S} Y$; taking for $M$ the set $\Gamma_{u}$, where $u : dom_{S}(\omega) \to Y$ is the
restriction of $\omega$ to $dom_{S}(\omega)$, it follows from the preceding relation and from `(I, 5.3.12)` that the set
underlying $\Gamma_{\omega \circ f}$ equals $f_{(Y)}(\Gamma_{\omega})$; as one knows

<!-- original page 246 -->

that $\Gamma_{\omega \circ f}$ is a reduced prescheme `(20.4.1)`, one sees that the $X'$-prescheme $\Gamma_{\omega \circ
f}$ equals $(\Gamma_{\omega} \times_{X} X')_{red}$. But since by hypothesis the composite morphism $\Gamma_{\omega \circ
f} \to \Gamma_{\omega} \times_{X} X' \to X'$ is an isomorphism, $p_{(X')}$ is necessarily radicial; as $f$ is
surjective, the same is true of $p : \Gamma_{\omega} \to X$ `(I, 3.4.8)`, so $p^{-1}(x)$ is a set reduced to a point
`(I, 3.6.4)`; it then follows from `(20.4.4)` that $\omega$ is defined at the point $x$.

The following proposition gives a valuative criterion for a rational map to be defined at a point:

**Proposition (20.4.6).**

<!-- label: IV.20.4.6 -->

*Let $S$ be a prescheme, $X$, $Y$ two $S$-preschemes; suppose $X$ locally Noetherian, $Y$ locally of finite type over
$S$. Let $U$ be a dense open in $X$, $h : U \to Y$ an $S$-morphism, $x \in X - U$ a normal point of $X$, $h_{x} :
\operatorname{Spec}(k(x)) \to Y$ an $S$-morphism. In order that $h$ can be extended to an $S$-morphism $h' : U' \to Y$,
where $U'$ is an open of $X$ containing $U$ and $x$, and such that the composite morphism $\operatorname{Spec}(k(x)) \to
U' \to Y$ is the given $S$-morphism $h_{x}$, it is necessary and sufficient that the following condition be verified:*

*(P) For every spectrum `S_1` of a discrete valuation ring, with closed point $a$ and generic point $b$, and every
morphism $u : S_{1} \to X$ such that $u(a) = x$, $u(b) \in U$, the composite morphism $h'_{1} = h \circ (u | {b}) : {b}
= u^{-1}(U) \to Y$ extends to a morphism $h'_{1} : S_{1} \to Y$ such that the diagram*

```text
                         Spec(k(a)) ────→ S_1
                              │            │
                              │            │ h'_1
                              ↓            ↓
                         Spec(k(x)) ────→ Y
                                    h_x
```

*is commutative.*

*Moreover, if this condition is verified, and if $h'' : U'' \to Y$ is a morphism satisfying the same conditions as $h'$,
then there exists an open set containing $U \cup {x}$ on which $h'$ and `h''` coincide.*

Let us first prove the last assertion; one may suppose $h'$ and `h''` defined on the same open $U_{0} \supset U \cup
{x}$. The sub-prescheme $Z$ of coincidences of $h'$ and `h''` `(17.4.5)` contains $U$ and $x$, so there is an open
neighbourhood $V$ of $x$ in `U_0` such that the sub-prescheme induced by $Z$ on the open $Z \cap V$ is a closed
sub-prescheme of the prescheme induced by $X$ on $V$; as this prescheme $Z \cap V$ majorizes the sub-prescheme induced
by $V$ on the open $U \cap V$, and this latter is schematically dense in $V$, $Z \cap V$ is necessarily equal to $V$
`(20.3.8.8)`, which proves that $h'$ and `h''` coincide on $U \cup V$.

The necessity of the condition of the statement being evident, let us prove that it is sufficient. By virtue of the
biunivocal correspondence between $S$-morphisms of $X$ into $Y$ and $X$-sections of $X \times_{S} Y$ `(I, 3.3.15)`, one
may restrict to the case where $S = X$ and where $h$ is therefore a $U$-section of $Y$; one will note that then $Y$ is
locally Noetherian, and one may evidently (since $X$ is locally integral and locally Noetherian) suppose $X = S$
irreducible. Moreover, taking into account `(20.3.7)`, one may suppose that $X = \operatorname{Spec}(A)$, where $A$ is a
Noetherian integral integrally closed local ring.

<!-- original page 247 -->

Note that for every $x' \in U$, $h(x')$ is a specialization of $h_{x}(x) = y$. Indeed, there exists a spectrum `S_1` of
a discrete valuation ring and a morphism $u : S_{1} \to X$ such that $u(a) = x$, $u(b) = x'$ `(II, 7.1.9)`. Applying the
condition of the statement, one obtains at once our assertion, since $h(x') = h_{1}(b) = h'_{1}(b)$ and $y = h'_{1}(a)$.
If $Y'$ is an open affine neighbourhood of $y$, one therefore has $h(X \cap U) \subset Y'$; one may consequently replace
$Y$ by $Y'$, in other words *suppose $Y$ affine*, hence separated over $X$. Let $\omega$ be the $X$-rational section of
$Y$ to which $h$ belongs, so that its graph has here as underlying set the closure of $h(U)$ in $Y$. Since $Y$ is
separated over $X$, one may apply `(20.4.4)` to $\omega$: it will suffice to prove that, if $p : \Gamma_{\omega} \to X$
is the canonical projection, $p^{-1}(x)$ is reduced to a single point $y$ and that $h_{x}(x) = y$. Indeed, by
`(20.4.4)`, $h$ will extend to a section $h'$ over an open $U'$ containing $U \cup {x}$, such that $h'(x) = y$, and
since then there exists only one $X$-morphism $\operatorname{Spec}(k(x)) \to Y$ sending $x$ to $y$, this will prove the
identity of $h_{x}$ and the composite of $h'$ and $\operatorname{Spec}(k(x)) \to U'$.

Since for $x' \in X \cap U$, $h(x')$ is a specialization of $y$, one has $y \in p^{-1}(x)$. Suppose then that $\eta$ is
an arbitrary point of $p^{-1}(x)$. Since $\Gamma_{\omega}$ is the closure of $h(U)$ and $h(U)$ is formed of points
adherent to $h(\xi)$, where $\xi$ is the generic point of $X$, $\Gamma_{\omega}$ is the closure of $h(\xi)$ in $Y$. One
then takes a spectrum `S_1` of a discrete valuation ring and a morphism $v : S_{1} \to Y$ such that $v(a) = \eta$, $v(b)
= h(\xi)$ `(II, 7.1.9)`, and one sets $u = p \circ v$, so that $u(a) = x$, $u(b) = \xi$. Applying to $u$ the condition
of the statement, one sees that one obtains a morphism $h'_{1} : S_{1} \to Y$ such that $h'_{1}(a) = y$ and $h'_{1}(b) =
h(\xi)$; but this entails $\eta = y$ by virtue of `(II, 7.2.3)`, since $Y$ is separated over $X$ and $v$ and $h'_{1}$
must therefore coincide, since they are equal at the point $b$. Q.E.D.

**Corollary (20.4.7).**

<!-- label: IV.20.4.7 -->

*The hypotheses on $S$, $X$, $Y$, $U$ and $h$ being those of `(20.4.6)`, let $E$ be a subset of $X - U$ such that $X$ is
normal at every point of $E$, and for each $x \in E$, let $h_{x} : \operatorname{Spec}(k(x)) \to Y$ be an $S$-morphism
such that the condition (P) of `(20.4.6)` is verified. Suppose moreover that the union $F$ of the graphs of the $h_{x}$
(identified with subsets of $X \times_{S} Y$) for $x \in E$ is contained in the union of a finite number of opens
$V_{i}$ of $X \times_{S} Y$ which are separated over $X$ (a condition automatically verified if $Y$ is separated over
$S$, or if $X$ is quasi-compact and $Y$ of finite type over $S$). Then there exists an $S$-morphism $h' : U' \to Y$,
where $U'$ is an open of $X$ containing $U \cup E$, such that, for every $x \in E$, the composite*

$$ \operatorname{Spec}(k(x)) \to U' \to Y $$

*equals $h_{x}$.*

Note first that, in `(20.4.6)`, if $Y$ is supposed separated, there is a largest open $U_{0} \supset U$, equal to the
domain of the $S$-rational map corresponding to $h$, on which $h$ can be extended, and this extension is unique
`(I, 7.2.2)`; whence the conclusion in this case, thanks to `(20.4.6)`. In the general case, let $E_{i}$ be the set of
$x \in E$ such that $(x, h_{x}(x)) \in V_{i}$. By virtue of `(20.4.6)`, for every $x \in E$, there is an extension
$h^{(x)}$ of $h$ to $U \cup W^{(x)}$, where $W^{(x)}$ is a neighbourhood of $x$ in $X$ such that the graph of $h^{(x)} |
W^{(x)}$ is contained in every $V_{i}$ such that $x \in E_{i}$. Since $V_{i}$ is separated over $X$ and $X$ reduced, for
two points $x'$, `x''` of $E_{i}$, $h^{(x')}$ and $h^{(x'')}$ coincide on $W^{(x')} \cap W^{(x'')}$ since they

<!-- original page 248 -->

coincide on the everywhere dense open $U \cap W^{(x')} \cap W^{(x'')}$ of this set. There is therefore a morphism
$h_{i} : U \cup U_{i} \to Y$ which extends $h$ to an open $U \cup U_{i}$ containing $E_{i}$; moreover, for every pair of
indices $i$, $j$, the graphs of the restrictions $h_{i} | (U_{i} \cap U_{j})$ and $h_{j} | (U_{i} \cap U_{j})$ are
contained in $V_{i} \cap V_{j}$; as $V_{i} \cap V_{j}$ is separated over $X$ and the foregoing morphisms coincide on an
everywhere dense open $U \cap U_{i} \cap U_{j}$ of $U_{i} \cap U_{j}$, they are equal. The morphism $h'$ equal to $h$ on
$U$, to $h_{i}$ on each of the $U_{i}$, answers the question.

**Remark (20.4.8).**

<!-- label: IV.20.4.8 -->

When $E = X - U$, it is clear that if, for every affine open $T$ of $X$, there exists an $S$-morphism $h_{T} : T \to Y$
extending $h | (U \cap T)$ and such that the composite $\operatorname{Spec}(k(x)) \to T \to Y$ equals $h_{x}$ for every
$x \in T - (U \cap T)$, then the $h_{T}$ are the restrictions of an $S$-morphism $h' : X \to Y$ (everywhere defined) by
virtue of the uniqueness assertion in `(20.4.6)`. To prove the existence of $h'$, one is therefore reduced to the case
where $X$ is affine, and then it suffices that the set $F$, union of the graphs of the $h_{x}$, be quasi-compact in $X
\times_{S} Y$ for one to be able to apply `(20.4.7)`. This will be the case when the $h_{x}$ are of the form
$\operatorname{Spec}(k(x)) \to Z \to Y$, where $Z$ is a closed sub-prescheme of $X$ having $X - U$ as underlying space,
and $h_{x}$ an $S$-morphism.

**Corollary (20.4.9).**

<!-- label: IV.20.4.9 -->

*Let $S$ be a locally Noetherian prescheme, $X$ a locally Noetherian prescheme, $f : X \to S$ a flat morphism,
$g : Y \to S$ a morphism locally of finite type. Let $U$ be a dense open in $S$, $h : f^{-1}(U) \to Y$ an $S$-morphism,
$T = S - U$, $Z$ the reduced closed sub-prescheme of $X$ having $f^{-1}(T)$ as underlying space, $h_{0} : Z \to Y$ an
$S$-morphism. Suppose $X$ normal at every point of $Z$. In order that there exist an $S$-morphism (necessarily unique)
$h' : X \to Y$ extending $h$ and $h_{0}$, it is necessary and sufficient that the following condition be satisfied:*

*For every spectrum `S_1` of a discrete valuation ring, with closed point $a$ and generic point $b$, and every morphism
$u : S_{1} \to S$ such that $u(a) \in T$ and $u(b) \in U$, there exists an `S_1`-morphism $h'_{1} : X_{(S_{1})} \to
Y_{(S_{1})}$ extending $h_{1} : f^{-1}(b) \to Y_{b}$ and such that the diagram*

```text
                         Spec(k(z)) ────→ Z_{(S_1)}
                              │              │
                              │              │ h_0(S_1)
                              ↓              ↓
                          X_{(S_1)} ────→ Y_{(S_1)}
                                     h'_1
```

*is commutative for every $z \in Z_{(S_{1})}$.*

Indeed, the hypothesis that $f$ is flat entails that $f^{-1}(U)$ is dense in $X$ `(2.3.10)`, and it then suffices to
apply `(20.4.8)`.

**Corollary (20.4.10).**

<!-- label: IV.20.4.10 -->

*Under the hypotheses of `(20.4.6)`, suppose moreover $Y$ separated and locally quasi-finite over $S$. Let $U$ be a
dense open in $X$, $h : U \to Y$ an $S$-morphism, $\omega$ the corresponding $S$-rational map, $x \in X - U$ a normal
point of $X$. In order that $\omega$ be defined at the point $x$, it is necessary and sufficient that the following
condition be verified: there exists a spectrum `S_1` of a discrete valuation ring, with closed point $a$ and generic
point $b$, and a morphism $u : S_{1} \to X$*

<!-- original page 249 -->

*such that $u(a) = x$, $u(b) \in U$ and such that the $S$-rational map $\omega \circ u$ is everywhere defined.*

Indeed, by hypothesis all the fibres of the projection morphism $X \times_{S} Y \to X$ are formed of isolated points,
and to apply `(20.4.4)` it suffices to know that the fibre $p^{-1}(x)$ is non-empty in $\Gamma_{\omega}$. Now if $h_{1}$
is the unique morphism of the class $\omega \circ u$, the unique point of $X \times_{S} Y$ above $x$ and $h_{1}(a)$
belongs to $\Gamma_{\omega}$, whence the conclusion.

**Proposition (20.4.11).**

<!-- label: IV.20.4.11 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ an $S$-prescheme affine over $S$, $U$ an open of $X$, $Z = X - U$.
Suppose that one has $prof_{Z}(\mathcal{O}_{X}) \geq 2$ `(5.10.1)`; then every $S$-morphism $f : U \to Y$ extends in a
unique way to an $S$-morphism of $X$ into $Y$.*

One may restrict to the case where $S$ and $X$ are affine and (by virtue of `(I, 3.3.14)`) to the case where $S = X$;
one has therefore $X = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(B)$, $B$ being an $A$-algebra of finite type.
As $B$ is a quotient of a polynomial algebra $A[(T_{\lambda})]_{\lambda \in L}$, $Y$ is a closed sub-prescheme of $Y' =
X[(T_{\lambda})]_{\lambda \in L}$. On the other hand, the hypothesis on $Z$ entails that $U$ is schematically dense in
$X$ by virtue of `(20.2.13, (iv))` and `(5.10.2)`. If one proves that every $X$-morphism $u : U \to Y'$ extends in a
unique way to an $X$-morphism $v' : X \to Y'$, it will result that $v'$ factors as $X \to Y \to Y'$: indeed, the
sub-prescheme $v'^{-1}(Y)$ is closed and majorizes $U$ `(I, 4.4.1)`, so is identical to $X$ `(20.3.8.8)`. Under these
conditions, $v$ will be the unique $S$-morphism of $X$ into $Y$ extending $u$. One may therefore restrict to the case $Y
= Y'$. But then there is a biunivocal correspondence between the $X$-morphisms from an open $U \subset X$ into $Y'$ and
the families $(s_{\lambda})_{\lambda \in L}$ of sections of $\mathcal{O}_{X}$ over $U$ `(II, 1.7.9)`; the conclusion
therefore follows from `(5.10.5)`.

**Corollary (20.4.12).**

<!-- label: IV.20.4.12 -->

*Let $X$ be a locally Noetherian reduced $S$-prescheme satisfying condition `(S_2)` `(5.7.2)` (for example a locally
Noetherian normal $S$-prescheme `(5.8.6)`), $Y$ an $S$-prescheme affine over $S$, $f$ an $S$-rational map of $X$ into
$Y$; then every irreducible component of $X - dom(f)$ is of codimension `1` in $X$.*

It amounts to the same to say that if `Z_2` is the set of $x \in X$ such that $\dim(\mathcal{O}_{X,x}) \geq 2$, then,
for every closed subset $Z \subset Z_{2}$ of $X$, every $S$-morphism of $X - Z$ into $Y$ extends to an $S$-morphism of
$X$ into $Y$; now this follows from the hypothesis on $X$ `(5.7.2)` and from `(20.4.11)`.

### 20.5. Relative pseudo-morphisms

**(20.5.1).** Let $X$, $Y$ be two $S$-preschemes. It follows from the definitions `(11.10.8)` that the intersection of
two opens $U$, $U'$ of $X$, *universally schematically dense relative to $S$*, again possesses this property. One
therefore defines an equivalence relation between $S$-morphisms $u : U \to Y$ by replacing in `(20.2.1)` "schematically
dense" by "universally schematically dense relative to $S$". An equivalence class under this relation is called a
*pseudo-morphism of $X$ into $Y$ relative to $S$*, and the set of these classes is denoted $Ps.hom_{X/S}(X, Y)$.

**(20.5.2).** Since every open of $X$ universally schematically dense relative to $S$ is in particular schematically
dense, the elements of a pseudo-morphism

<!-- original page 250 -->

of $X$ into $Y$ relative to $S$ are equivalent in the sense of `(20.2.1)`, whence a canonical map

```text
  (20.5.2.1)             Ps.hom_{X/S}(X, Y) → Ps.hom_S(X, Y).
```

**Proposition (20.5.3).**

<!-- label: IV.20.5.3 -->

*Suppose $Y$ separated over $S$. Then:*

*(i) The map `(20.5.2.1)` is injective and identifies $Ps.hom_{X/S}(X, Y)$ with the subset of $Ps.hom_{S}(X, Y)$ formed
of pseudo-$S$-morphisms $\omega$ such that $dom_{S}(\omega)$ is universally schematically dense relative to $S$.*

*(ii) The presheaf $U \mapsto Ps.hom_{U/S}(U, Y)$ on $X$ is a sheaf.*

Assertion (i) is immediate, since saying that two $S$-morphisms $u : U \to Y$, $u' : U' \to Y$ are equivalent in the
sense of `(20.2.1)` means then that they are the restrictions of the same morphism $dom_{S}(\omega) \to Y$ `(20.2.4)`,
and if $U$ and $U'$ are universally schematically dense relative to $S$, the same is *a fortiori* true of
$dom_{S}(\omega)$. To prove (ii), note that $U \mapsto Ps.hom_{S}(U, Y)$ is then a sheaf `(20.2.6)`; on the other hand,
given an open cover $(U_{\alpha})$ of $U$, and a pseudo-$S$-morphism $\omega$ of $U$ into $Y$, for $dom_{S}(\omega)$ to
be universally schematically dense in $U$ relative to $S$, it follows at once from the definitions (cf. `(20.2.1)`) that
it is necessary and sufficient that each of the sets $dom_{S}(\omega) \cap U_{\alpha} = dom_{S}(\omega | U_{\alpha})$ be
universally schematically dense in $U_{\alpha}$ relative to $S$; whence (ii).

When $Y$ is separated, one will denote $\mathcal{Ps}.hom_{X/S}(X, Y)$ the subsheaf

$$ U \mapsto Ps.hom_{U/S}(U, Y) $$

of $\mathcal{Ps}.hom_{S}(X, Y)$.

When $X$ is flat and locally of finite presentation over $S$ and $Y$ separated over $S$, the pseudo-morphisms of $X$
into $Y$ relative to $S$ again identify with the pseudo-$S$-morphisms $\omega$ such that, for every fibre $X_{s}$ of the
morphism $X \to S$, $dom_{S}(\omega) \cap X_{s}$ is schematically dense in $X_{s}$ `(11.10.10)`.

**(20.5.4).** A particularly important case where $Y$ is separated over $S$ is the case $Y = S[T] = S
\otimes_{\mathbb{Z}} \operatorname{Spec}(\mathbb{Z}[T])$ ($T$ indeterminate). There is then a biunivocal correspondence
between the pseudo-$S$-morphisms of $X$ into $Y$ and the pseudo-functions on $X$ `(20.2.8)` by virtue of the definition
of a product of ℤ-preschemes. The pseudo-morphisms of $X$ into $Y$ relative to $S$ then identify, by virtue of
`(20.5.3)`, with the *pseudo-functions $\phi$ on $X$ such that $dom(\phi)$ is universally schematically dense relative
to $S$*. The sheaf $\mathcal{Ps}.hom_{X/S}(X, Y)$ is a subsheaf of *rings* of $\mathcal{M}'_{X}$, which one denotes
$\mathcal{M}'_{X/S}$.

One then sets $Ps.hom_{X/S}(X, Y) = M'(X/S)$ and one says that its elements are the *pseudo-functions on $X$ relative to
$S$*.

**(20.5.5).** Let $X$, $Y$, $Z$ be three $S$-preschemes, $f : Y \to Z$ an $S$-morphism. One may, in the reasoning of
`(20.3.1)`, replace everywhere "schematically dense" by "universally schematically dense relative to $S$"; for every
pseudo-morphism $\omega \in Ps.hom_{X/S}(X, Y)$, the morphisms $f \circ u$, where $u$ runs through $\omega$, therefore
belong to one and the same equivalence class (for the relation defined in `(20.5.1)`), which one

<!-- original page 251 -->

calls the *pseudo-morphism of $X$ into $Z$, relative to $S$, composed of $f$ and $\omega$*, and which one denotes $f
\circ \omega$. If $g : Z \to T$ is a morphism, it is immediate that $g \circ (f \circ \omega) = (g \circ f) \circ
\omega$.

**(20.5.6).** Suppose $Y$ separated over $S$, and let $\omega$ be a pseudo-morphism of $X$ into $Y$ relative to $S$. If
$f : X' \to X$ is an $S$-morphism such that $f^{-1}(dom_{S}(\omega))$ is universally schematically dense in $X'$
relative to $S$, it follows from `(20.3.2)` that the pseudo-$S$-morphism $\omega \circ f$ has a domain universally
schematically dense relative to $S$, hence `(20.5.3)` may be considered as a pseudo-morphism relative to $S$. When $X'$
is flat and locally of finite presentation over $S$, the condition that $f^{-1}(dom_{S}(\omega))$ be universally
schematically dense relative to $S$ is again equivalent to saying that for every $s \in S$,
$(f^{-1}(dom_{S}(\omega)))_{s}$ (notation of `(11.10.10)`) be schematically dense in $X'_{s}$, or further, denoting
$f_{s} : X'_{s} \to X_{s}$ the morphism deduced from $f$ by base change, that the inverse image under $f_{s}$ of
$(dom_{S}(\omega))_{s}$ be schematically dense in $X'_{s}$. This latter condition will in particular be verified if, for
every $s \in S$, $X_{s}$, $X'_{s}$ and $f_{s}$ satisfy one of the three conditions (i), (ii), (iii) of `(20.3.5)`.

**(20.5.7).** Suppose now that $X$ and $X'$ are both $S$-preschemes flat and locally of finite presentation over $S$,
and that $f : X' \to X$ is a flat $S$-morphism (or, what amounts to the same `(11.3.10)`, that for every $s \in S$,
$f_{s} : X'_{s} \to X_{s}$ is a flat morphism). Then, for every open $U$ of $X$ and every open $V \subset U$ universally
schematically dense in $U$ relative to $S$, it follows from `(11.10.5)` and `(11.10.9)` that $f^{-1}(V)$ is universally
schematically dense in $f^{-1}(U)$ relative to $S$. For every pseudo-morphism $\omega$ of $X$ into $Y$ relative to $S$,
it follows from `(20.3.4)` that the pseudo-$S$-morphism $\omega \circ f$ is defined and is a pseudo-morphism of $X'$
into $Y$ relative to $S$, *even when $Y$ is not supposed separated over $S$*. One deduces that in this case, for every
$S$-morphism $g : Y \to Z$, $(g \circ \omega) \circ f$ is again defined and equal to $g \circ (\omega \circ f)$ (with
the definitions of `(20.5.1)`), and is therefore a pseudo-morphism relative to $S$.

**(20.5.8).** Let $X$ be an $S$-prescheme, $S' \to S$ an arbitrary morphism, $X' = X_{(S')}$, $g : X' \to X$ the
canonical projection. Then, for every open $U$ of $X$ and every open $V \subset U$ universally schematically dense in
$U$ relative to $S$, $V' = g^{-1}(V)$ is universally schematically dense in $U' = g^{-1}(U)$ relative to $S'$ by
definition `(11.10.8)`. Let then $\omega$ be a pseudo-morphism of $X$ into an $S$-prescheme $Y$ relative to $S$; if
$u_{1}$, $u_{2}$ are $S$-morphisms of the class $\omega$, defined respectively on opens `U_1`, `U_2` of $X$ universally
schematically dense in $X$ relative to $S$, it follows from the foregoing that the morphisms $u'_{1} = u_{1} \circ (g |
g^{-1}(U_{1}))$ and $u'_{2} = u_{2} \circ (g | g^{-1}(U_{2}))$ coincide on an open $U'_{3}$ universally schematically
dense relative to $S'$. Now, if $Y' = Y_{(S')}$ and if $h : Y' \to Y$ is the canonical projection, $u'_{1}$ and $u'_{2}$
factor canonically as $u'_{1} = h \circ v_{1}$, $u'_{2} = h \circ v_{2}$, and $v_{1}$ and $v_{2}$ are two $S'$-morphisms
into $Y'$ which coincide on $U'_{3}$. One therefore sees that when $u_{1}$ runs through the class $\omega$, the
corresponding $S'$-morphisms $v_{1}$ belong to one and the same pseudo-morphism relative to $S'$, called the *inverse
image of $\omega$ under the base-change morphism $S' \to S$* and denoted $\omega_{(S')}$. It is clear that if $S'' \to
S'$ is a second morphism, one has $(\omega_{(S')})_{(S'')} = \omega_{(S'')}$ (for the composite base-change morphism
$S'' \to S' \to S$).

<!-- original page 252 -->

### 20.6. Relative meromorphic functions

**(20.6.1).** Let $S$ be a prescheme, $X$ an $S$-prescheme which is flat and locally of finite presentation over $S$;
for every $s \in S$, we shall denote by $X_{s}$ the fibre at the point $s$ of the structure morphism $X \to S$. In
general, if $\phi$ is a meromorphic function on $X$, it is not possible to associate to it, in a "natural" way, for each
$s \in S$, an "induced" meromorphic function on $X_{s}$ `(20.1.11)`. For every open $U$ of $X$, denote by
$\mathcal{S}_{X/S}(U)$ the set of sections $t \in \Gamma(U, \mathcal{O}_{X})$ such that, for every $s \in S$, the image
$t_{s}$ of $t$ under the canonical homomorphism $\Gamma(U, \mathcal{O}_{X}) \to \Gamma(U \cap X_{s},
\mathcal{O}_{X_{s}})$ is a *regular* section; this implies moreover, by the equivalence of a) and b) in `(11.3.7)`, that
$t$ is itself a regular section. It is clear that $U \mapsto \mathcal{S}_{X/S}(U)$ is a subsheaf of the sheaf of sets
$\mathcal{S} = \mathcal{S}(\mathcal{O}_{X})$ (notation of `(20.1.3)`), which one denotes $\mathcal{S}_{X/S}$; one sets

$$ (20.6.1.1) \mathcal{M}_{X/S} = \mathcal{O}_{X}[\mathcal{S}^{-1}_{X/S}] $$

(notation of `(20.1.1)`) and one says that this sheaf of rings is the *sheaf of germs of meromorphic functions on $X$
relative to $S$*; its sections over $X$ are called *meromorphic functions on $X$ relative to $S$* and their set is
denoted $M(X/S)$. It is clear that $\mathcal{M}_{X/S}$ is a subsheaf of $\mathcal{M}_{X} =
\mathcal{O}_{X}[\mathcal{S}^{-1}]$; for every meromorphic function $\phi \in M(X/S)$ and every $s \in S$, the inverse
image of $\phi$ under the canonical injection morphism $j_{s} : X_{s} \to X$ is then defined `(20.1.11)`, and denoted
$\phi_{s}$.

**(20.6.2).** Now let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module; one sets

```text
  (20.6.2.1)             𝓜_{X/S}(ℱ) = ℱ ⊗_{𝒪_X} 𝓜_{X/S};
```

the sections of $\mathcal{M}_{X/S}(\mathcal{F})$ are called *meromorphic sections of $\mathcal{F}$ over $X$, relative to
$S$* and their set is denoted $M(X/S, \mathcal{F})$. The canonical homomorphism $\mathcal{F} \to
\mathcal{M}_{X/S}(\mathcal{F})$ is not necessarily injective; when it is, one says that $\mathcal{F}$ is *torsion-free
relative to $S$*: this means that for every open $U$ of $X$ and every section $t \in \mathcal{S}_{X/S}(U)$, $t$ is
$(\mathcal{F} | U)$-regular; this condition is *a fortiori* verified when $\mathcal{F}$ is strictly torsion-free
`(20.1.5)`. In this latter case, it follows at once from the definitions `(20.1.2)` that the canonical homomorphism of
$\mathcal{O}_{X}$-Modules

$$ (20.6.2.2) \mathcal{M}_{X/S}(\mathcal{F}) \to \mathcal{M}_{X}(\mathcal{F}) $$

is injective, so that the meromorphic sections of $\mathcal{F}$ relative to $S$ are meromorphic sections of
$\mathcal{F}$ in the sense of `(20.1.3)`.

**Proposition (20.6.3).**

<!-- label: IV.20.6.3 -->

*The image, under the injective homomorphism `(20.2.10.1)`, of the subsheaf $\mathcal{M}_{X/S}$ of $\mathcal{M}_{X}$ is
the subsheaf $\mathcal{M}'_{X/S}$ of pseudo-functions on $X$ relative to $S$ (i.e. of pseudo-functions whose domain of
definition is universally schematically dense relative to $S$ `(20.5.4)`).*

One may evidently restrict to proving that the image of $M(X/S)$ under the canonical homomorphism $M(X) \to M'(X)$
equals $M'(X/S)$; the proposition is then a consequence of the following more general proposition:

<!-- original page 253 -->

**Proposition (20.6.4).**

<!-- label: IV.20.6.4 -->

*Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation and strictly torsion-free. Then,
for a meromorphic section $\phi$ of $\mathcal{F}$ over $X$ to be a meromorphic section relative to $S$, it is necessary
and sufficient that $dom(\phi)$ be universally schematically dense relative to $S$.*

The necessity of the condition follows from `(20.2.15)` applied to each canonical injection $X_{s} \to X$ ($s \in S$),
taking `(11.10.9)` into account. To see that the condition is sufficient, one must prove that for every $x \in X$, there
exists an open neighbourhood $U$ of $x$ in $X$ and a section of $\mathcal{M}_{X/S}(\mathcal{F})$ over $U$ whose
restriction to $U \cap dom(\phi)$ coincides with $\phi$ on a schematically dense open of $U \cap dom(\phi)$. Consider
the *Ideal of denominators* $\mathcal{J}$ of $\phi$ `(20.2.14)`, which is quasi-coherent, and which defines a closed
sub-prescheme of $X$ whose underlying space is $X - dom(\phi)$. By hypothesis, if $s$ is the image of $x$ in $S$,
$dom(\phi) \cap X_{s}$ is schematically dense in the locally Noetherian prescheme $X_{s}$, hence `(20.2.13, (iv))`
contains $Ass(\mathcal{O}_{X_{s}})$; this implies that the ideal $\mathcal{J}_{x}$ of $\mathcal{O}_{X,x}$ has an image
in $\mathcal{O}_{X_{s}, x} = \mathcal{O}_{X,x} / \mathfrak{m}_{s} \mathcal{O}_{X,x}$ which is not contained in any of
the prime ideals $\mathfrak{p}_{i} \in Ass(\mathcal{O}_{X_{s}, x})$ (finite in number); hence (Bourbaki, _Alg. comm._,
chap. II, §1, n° 1, prop. 2) there exists an element $t_{x} \in \mathcal{J}_{x}$ whose image in $\mathcal{O}_{X_{s}, x}$
does not belong to any of the $\mathfrak{p}_{i}$, and is consequently regular in this Noetherian ring. Let $t$ be a
section of $\mathcal{J}$ over an affine open neighbourhood $U$ of $x$ whose germ at the point $x$ is $t_{x}$; since $X$
is flat and locally of finite presentation over $S$, one may suppose `(11.3.8)` that $t$ is a regular section of
$\mathcal{O}_{X}$ over $U$ and that, for every $s' \in S$, the image of $t$ in $\Gamma(U \cap X_{s'},
\mathcal{O}_{X_{s'}})$ is also regular; in other words, one has $t \in \mathcal{S}_{X/S}(U)$. But then, by definition of
$\mathcal{J}$, since $\mathcal{F}$ is strictly torsion-free, $t(\phi | (U \cap dom(\phi)))$ is a section $u$ of
$\mathcal{F}$ over $U \cap dom(\phi)$; on the other hand, $U \cap dom(\phi)$ contains the open set $U_{t}$ of points $x'
\in U$ where $t(x') \neq 0$, and this latter contains $x$ and is schematically dense in $U$ `(20.2.9)`. One therefore
sees that on $U_{t}$, $\phi$ coincides with the restriction to $U_{t}$ of the section $u/t$ of
$\mathcal{M}_{X/S}(\mathcal{F})$ over $U$. Q.E.D.

**Remarks (20.6.5).**

<!-- label: IV.20.6.5 -->

(i) Let $\phi$ be a meromorphic function on $X$ relative to $S$, so that for every $s \in S$, $\phi_{s}$ is a
meromorphic function on $X_{s}$ `(20.6.1)`; by virtue of `(20.1.11.1)`, one has

$$ (20.6.5.1) dom(\phi) \cap X_{s} \subset dom(\phi_{s}). $$

But it is worth noting that even when $S$ is the spectrum of a discrete valuation ring $A$ and $X = S[T]$ ($T$
indeterminate), the two sides of `(20.6.5.1)` are not necessarily equal: for example, if $\pi$ is a uniformizer of $A$,
it is immediate that $\phi = \pi/T$ is a meromorphic function on $S$ relative to $S$, since if $a$ and $b$ are the
closed point and the generic point of $S$, $T$ is regular in $\Gamma(X_{a}, \mathcal{O}_{X_{a}}) = k[T]$ and in
$\Gamma(X_{b}, \mathcal{O}_{X_{b}}) = K[T]$, $k$ and $K$ being the residue field and the field of fractions of $A$. One
has $dom(\phi) = D(T)$ in $X$, but $dom(\phi_{a}) = X_{a}$ since $\phi_{a} = 0$.

(ii) For a meromorphic function $\phi$ relative to $S$ to be invertible in the ring $M(X/S)$, it is necessary and
sufficient that for every $s \in S$, $\phi_{s}$ be invertible in $M(X_{s})$ (in other words, that $\phi_{s}$ be a
regular meromorphic function on $X_{s}$ `(20.1.8)`). The condition is

<!-- original page 254 -->

indeed trivially necessary. Conversely, if it is verified, and if $x$ is any point of $X$, $s$ its image in $S$, there
exists by hypothesis an open neighbourhood $U$ of $x$ in $X$ and two sections $u$, $t$ of $\mathcal{O}_{X}$ over $U$
such that $t \in \mathcal{S}_{X/S}(U)$ and $\phi | U = u/t$; the hypothesis entails that if $u_{s}$ is the image of $u$
in $\Gamma(U \cap X_{s}, \mathcal{O}_{X_{s}})$, $u_{s}$ is regular at the point $x$. By restricting $U$, one may
therefore suppose, by virtue of `(11.3.8)`, that $u \in \mathcal{S}_{X/S}(U)$, whence the conclusion.

When $\phi$ is invertible in $M(X/S)$, one again says that $\phi$ is a *regular meromorphic function relative to $S$*.
One will note that $\phi \in M(X/S)$ may be invertible in $M(X)$ (in other words, regular in the sense of `(20.1.8)`)
without being so in $M(X/S)$, as the example in (i) at once shows.

(iii) Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module, and let $\phi$ be a regular meromorphic section of
$\mathcal{L}$ over $X$ `(20.1.8)`; one says that $\phi$ is *regular relative to $S$* if, for every open $U$ of $X$ such
that $\mathcal{L} | U$ is isomorphic to $\mathcal{O}_{U}$, $\phi | U$ corresponds to an element of $\Gamma(U,
\mathcal{M}_{X})$ which is regular relative to $S$; by virtue of (ii), it is immediate that it is necessary and
sufficient for this that, for every $s \in S$, $\phi_{s}$ be a regular meromorphic section `(20.1.8)` of the invertible
$\mathcal{O}_{X_{s}}$-Module $\mathcal{L}_{s} = \mathcal{L} \otimes_{\mathcal{O}_{X}} k(s)$. If $\phi'$ is the inverse
of $\phi$ in $\mathcal{L}^{-1}$ `(20.1.10)`, $\phi'$ is then also regular relative to $S$. If $\mathcal{L}_{1}$ is a
second invertible $\mathcal{O}_{X}$-Module, $\phi_{1}$ a meromorphic section of $\mathcal{L}_{1}$ over $X$, regular
relative to $S$, then $\phi \otimes \phi_{1}$ is a meromorphic section of $\mathcal{L} \otimes \mathcal{L}_{1}$ over
$X$, regular relative to $S$.

**Proposition (20.6.6).**

<!-- label: IV.20.6.6 -->

*Let $X$ be an $S$-prescheme flat and locally of finite presentation over $S$, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module
locally free of finite type; for every $s \in S$, denote by $X_{s}$ the fibre at the point $s$ of the structure morphism
$f : X \to S$. Let $\phi$ be a meromorphic section of $\mathcal{F}$ over $X$, relative to $S$, and suppose that $\phi$
is defined at every point $x \in X$ such that $prof(\mathcal{O}_{X_{f(x)}, x}) \leq 1$. Then $\phi$ is everywhere
defined.*

By hypothesis, $dom(\phi) \cap X_{s}$ is schematically dense in $X_{s}$ for every $s \in S$, hence contains the points
$x$ of $X_{s}$ such that $prof(\mathcal{O}_{X_{s}, x}) = 0$ `(5.10.2)`; the hypothesis means therefore that if one sets
$Z = X - dom(\phi)$, one has $prof(\mathcal{O}_{X_{f(x)}, x}) \geq 2$ at every point of $Z$. It therefore suffices to
apply `(19.9.8)`.

**(20.6.7).** Let $X$, $X'$ be two $S$-preschemes flat and locally of finite presentation over $S$,
$f = (\psi, \theta) : X' \to X$ an $S$-morphism. For every open $U$ of $X$, denote by $\mathcal{S}_{f, /S}(U)$ the set
of sections $t \in \mathcal{S}_{X/S}(U)$ whose image in $\Gamma(f^{-1}(U), \mathcal{O}_{X'})$ belongs to
$\mathcal{S}_{X'/S}(f^{-1}(U))$; it is immediate that $U \mapsto \mathcal{S}_{f, /S}(U)$ is a subsheaf of the sheaf of
sets $\mathcal{S}_{X/S}$, which one denotes $\mathcal{S}_{f, /S}$. One sets
$\mathcal{M}_{X/S, f} = \mathcal{O}_{X}[\mathcal{S}^{-1}_{f, /S}]$; this is a subsheaf of rings of $\mathcal{M}_{X/S}$,
and one canonically deduces from $\theta\sharp : \psi*(\mathcal{O}_{X}) \to \mathcal{O}_{X'}$ a homomorphism of sheaves
of rings $\theta'\sharp : \psi*(\mathcal{M}_{X/S, f}) \to \mathcal{M}_{X'/S}$ extending $\theta\sharp$. If a meromorphic
function $\phi$ on $X$, relative to $S$, is a section of $\mathcal{M}_{X/S, f}$, $\Gamma(\theta'\sharp)(\phi)$ is a
meromorphic function on $X'$, called the *inverse image of $\phi$ under $f$*, and denoted $\phi \circ f$ if this entails
no confusion. One extends in the same way the definitions of `(20.1.11)` relative to $\mathcal{O}_{X}$-Modules.

**Proposition (20.6.8).**

<!-- label: IV.20.6.8 -->

*With the notations of `(20.6.7)`, if the $S$-morphism $f : X' \to X$ is flat, one has $\mathcal{M}_{X/S, f} =
\mathcal{M}_{X/S}$, and the homomorphism $\phi \mapsto \phi \circ f$ is defined on all of $M(X/S)$.*

<!-- original page 255 -->

Indeed, the hypothesis entails, by virtue of `(11.3.10)`, that for every $s \in S$, $f_{s} : X'_{s} \to X_{s}$ is flat;
so, for every section $t \in \mathcal{S}_{X/S}(U)$, if $t'$ is its inverse image in $\Gamma(f^{-1}(U),
\mathcal{O}_{X'})$, $t'_{s}$, which is the inverse image of $t_{s}$, is a regular section of $\mathcal{O}_{X'_{s}}$ over
$f^{-1}(U) \cap X'_{s}$, by virtue of `(20.1.12)`; one concludes that by definition $t' \in
\mathcal{S}_{X'/S}(f^{-1}(U))$, whence the proposition.

One deduces from this, as in `(20.1.12)`, a canonical homomorphism of $\mathcal{O}_{X'}$-Algebras

$$ (20.6.8.1) f*(\mathcal{M}_{X/S}) \to \mathcal{M}_{X'/S}. $$

**(20.6.9).** Consider finally an arbitrary morphism $S' \to S$, and set $X' = X \times_{S} S'$, which is flat and
locally of finite presentation over $S'$; let $p : X' \to X$ be the canonical projection. Let $U$ be an open of $X$, $t$
a section belonging to $\mathcal{S}_{X/S}(U)$, $t'$ its image in $\Gamma(p^{-1}(U), \mathcal{O}_{X'})$; for every $s'
\in S'$, if $s \in S$ is the image of $s'$, one has $X'_{s'} = X_{s} \otimes_{k(s)} k(s')$, hence the morphism $X'_{s'}
\to X_{s}$ is flat, and consequently `(20.1.12)` the inverse image $t'_{s'}$ of $t_{s}$ in $\Gamma(p^{-1}(U) \cap
X'_{s'}, \mathcal{O}_{X'_{s'}})$ is regular; this proves that one has $t' \in \mathcal{S}_{X'/S'}(p^{-1}(U))$. This
permits one to define canonically, as in `(20.6.8)`, a canonical homomorphism of $\mathcal{O}_{X'}$-Algebras

$$ (20.6.9.1) p*(\mathcal{M}_{X/S}) \to \mathcal{M}_{X'/S'}. $$

By means of the identification permitted by `(20.6.3)`, this notion of base change for relative meromorphic functions is
a particular case of the analogous notion for relative pseudo-morphisms `(20.5.8)`.
