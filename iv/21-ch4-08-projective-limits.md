<!-- original page 5 -->

## §8. Projective limits of preschemes

### 8.1. Introduction

**(8.1.1)** In this section we shall systematically study the following situation. Let $I$ be a filtered (increasing)
preordered set, $(A_{\alpha}, \phi_{\beta \alpha})$ an inductive system of rings indexed by $I$, and $A = \lim
A_{\alpha}$ its inductive limit. For every $\alpha \in I$ and every $A_{\alpha}$-prescheme $X_{\alpha}$, consider the
$A_{\lambda}$-preschemes $X_{\lambda} = X_{\alpha} \otimes_{A_{\alpha}} A_{\lambda}$ for $\lambda \geq \alpha$, and the
$A$-prescheme $X = X_{\alpha} \otimes_{A_{\alpha}} A$; it is clear that the preschemes $X_{\lambda}$ (for $\lambda \geq
\alpha$) form a projective system, and one will see `(8.2.5)` that $X$ is a projective limit of this system in the
category of preschemes. We propose to find conditions on $X_{\alpha}$ or on the $A_{\lambda}$ allowing us to prove
properties of the following type: in order that $X$ possess a property $P$ (for example, the property of being proper
over $S = \operatorname{Spec}(A)$, or irreducible, or connected, etc.), it is necessary and sufficient that there exist
an index $\mu \geq \alpha$ such that, for every $\lambda \geq \mu$, $X_{\lambda}$ has (with respect to $S_{\lambda} =
\operatorname{Spec}(A_{\lambda})$, if applicable) the same property $P$. We shall obtain analogous statements for
properties of $\mathcal{O}$-Modules, of $A$-morphisms of $A$-preschemes, etc. We shall also show `(8.9.1)` that giving
an $A$-prescheme of finite presentation `(1.6.1)` is essentially equivalent to giving an $A_{\lambda}$-prescheme of
finite presentation $X_{\lambda}$ for $\lambda$ large enough, $X$ being then isomorphic to $X_{\lambda}
\otimes_{A_{\lambda}} A$. One has analogous statements for $\mathcal{O}_{X}$-Modules of finite presentation, their
homomorphisms, the $A$-morphisms of $A$-preschemes of finite presentation, etc.

**(8.1.2)** The utility of such results will appear, for example, in the following questions:

a) Let $Y$ be a prescheme, $y$ a point of $Y$, $(U_{\alpha})$ the filtered (decreasing) projective system of affine open
neighbourhoods of $y$ in $Y$; if $A_{\alpha}$ is the ring of $U_{\alpha}$, the $A_{\alpha}$ form a filtered (increasing)
inductive system whose inductive limit $A$ is the local ring $\mathcal{O}_{y}$. Moreover, if one denotes by
$\mathfrak{p}_{\alpha}$ the prime ideal of $y$ in the ring $A_{\alpha}$, the inductive system $(A_{\alpha})$ is cofinal
with every inductive system $(A_{\alpha,f})$, where $f$ runs through $A_{\alpha} - \mathfrak{p}_{\alpha}$ (for a fixed
$\alpha$), since the $D(f)$ form a fundamental system of neighbourhoods of $y$ in $U_{\alpha}$, hence in $Y$. The
results of the present section will imply that the algebraic geometry of $\mathcal{O}_{y}$-preschemes of finite
presentation (and the theory of Modules of finite presentation on these preschemes) is essentially equivalent to the
algebraic geometry of preschemes of finite presentation on "sufficiently small" open neighbourhoods of $y$. Thus, the
statement `(8.10.5, (xiii))` implies that if a morphism $f : X \to Y$ is of finite presentation, then, in order that $X
\times_{Y} \operatorname{Spec}(\mathcal{O}_{y})$ be proper over $\operatorname{Spec}(\mathcal{O}_{y})$, it is necessary
and sufficient that there exist an open neighbourhood $U$ of $y$ in $Y$ such that $f^{-1}(U)$ be proper over $U$.

<!-- original page 6 -->

A particularly important case, and to a certain extent classical, is that in which $Y$ is integral and $y$ is its
generic point, so that $\mathcal{O}_{y}$ is none other than the field $R(Y) = K$ of rational functions on $Y$. The
results of the present section then amount to interpreting the algebraic geometry over $K$ in terms of the algebraic
geometry above non-empty "sufficiently small" open sets of $Y$, that is to say, intuitively, in terms of "families" of
geometric objects indexed by the points of such an open set. This point of view has moreover been commonly used for a
long time, not only in algebraic geometry over algebraically closed fields, but also in the arithmetic study of
varieties defined over a number field $K$ (finite extension of $\mathbb{Q}$), by considering this latter as the field of
fractions of its ring of integers $A$ ("theory of reduction modulo $\mathfrak{p}$", $\mathfrak{p}$ a prime ideal of $A$;
cf. `(I, 3.7)`). The results of §§8 and 9 thus furnish among other things foundations of the language of "reduction
modulo $\mathfrak{p}$" in arithmetic.

One will note that in the example envisaged here, the morphisms $S_{\mu} \to S_{\lambda}$ (for $\lambda \leq \mu$) are
the canonical open immersions $U_{\mu} \to U_{\lambda}$, and *a fortiori* are flat morphisms (but not faithfully flat in
general), which explains the interest of statements that appeal to such a restriction.

b) Suppose that the $A_{\lambda}$ are *fields*, so that $A = \lim A_{\lambda}$ is also a field. This case generally
arises when one starts from geometric data above an arbitrary field $K$, which one considers as an extension of a field
$k$ (for example the prime subfield of $K$). It is then advantageous to consider $K$ as the inductive limit of its
sub-extensions that are *of finite type over $k$*, which permits in many questions to reduce to the case where $K$ is an
extension of finite type of $k$. Using also the method sketched in a), one can then generally reduce to the case of a
base ring $A$ that is *an integral algebra of finite type over $k$*.

One will note that in this example, the morphisms $S_{\mu} \to S_{\lambda}$ are faithfully flat.

c) Suppose one is interested in the properties, local on $Y$, of preschemes of finite presentation above an arbitrary
prescheme $Y$, which one may therefore assume affine with ring $A$. It is then advantageous to consider $A$ as the
inductive limit of its sub-rings that are $\mathbb{Z}$-algebras of finite type, which permits to reduce many questions
to the case where $Y$ is the spectrum of such an algebra. This is the explicit form of the "Kroneckerian point of view",
according to which algebraic geometry reduces to the algebraic geometry of preschemes of finite type over $\mathbb{Z}$
(which is sometimes called "absolute algebraic geometry"). This example shows us in particular that in most "relative"
questions over a base prescheme $Y$, one can reduce to the case where $Y$ is Noetherian.

One will note that in this example, contrary to the preceding ones, the morphisms $S_{\mu} \to S_{\lambda}$ have in
general no particular regularity property.

In what follows, when we apply the results that follow to any one of the three particular situations just described, we
shall dispense with redescribing in detail the procedure that permits these applications, contenting ourselves with
referring back to the foregoing.

**(8.1.3)** In example a) of `(8.1.2)`, we saw that if $Y$ is an integral prescheme with generic point $y$, and $f : X
\to Y$ a morphism of finite presentation, then, if the generic fibre $f^{-1}(y)$ is proper over $k(y)$, there is an open
neighbourhood $U$ of $y$ such that $f^{-1}(U)$ is proper over $U$; *a fortiori*, for every $s \in U$, $f^{-1}(s)$ is
proper over $k(s)$. There are occasions when one needs a converse, asserting that if $f^{-1}(s)$ is proper over $k(s)$
for "sufficiently many" points $s \in U$, then $f^{-1}(y)$ is proper over $k(y)$. For example, suppose that $X$ and $Y$
are algebraic preschemes over an algebraically closed field $k$ (one can take for $k$ the field $\mathbb{C}$ of complex
numbers, to fix the ideas); one sometimes needs to know that if, for every $s \in Y$ rational over $k$, the fibre
$f^{-1}(s)$ is proper over $k(s)$, then $f^{-1}(y)$ is proper over $k(y)$, and consequently $f^{-1}(U)$ is proper over
$U$ for some neighbourhood $U$ of $y$ (¹). Now this statement will follow easily from the following: the set $E$ of
points $s \in Y$ such that $f^{-1}(s)$ is proper over $k(s)$ is *constructible* (and consequently identical to all of
$Y$ if it contains the closed points of $Y$, thanks to Hilbert's Nullstellensatz `(10.4.8)`); this also amounts to
saying that if $f^{-1}(y)$ is not proper over $k(y)$, then there exists an open neighbourhood $U$ of $y$ such that
$f^{-1}(s)$ is not proper over $k(s)$ for every $s \in U$ (cf. `(9.6.1, (iv))`). This example illustrates the interest
of systematically developing *constructibility criteria* for the most important notions: this is what will be done in
§9.

> (¹) One will note that such a statement is in the end purely geometric, in the sense that it only appeals to points
> rational over $k$, and not to generic points; for example, when $k = \mathbb{C}$, this statement has an obvious
> topological meaning for the analyst, when one interprets "proper" in the topological sense of the term, for the spaces
> underlying the analytic spaces formed by the points of $X$ and $Y$ rational over $\mathbb{C}$.

<!-- original page 7 -->

### 8.2. Projective limits of preschemes

**(8.2.1)** Let `S_0` be a ringed space, $L$ a filtered (increasing) preordered set, $(\mathcal{A}_{\lambda}, \phi_{\mu
\lambda})$ an inductive system of $\mathcal{O}_{S_{0}}$-Algebras (not necessarily commutative) indexed by $L$. One knows
that, considered as an inductive system of $\mathcal{O}_{S_{0}}$-Modules, $(\mathcal{A}_{\lambda}, \phi_{\mu \lambda})$
admits an inductive limit $\mathcal{A}$; let us denote by $\phi_{\lambda} : \mathcal{A}_{\lambda} \to \mathcal{A}$ the
canonical homomorphism (of $\mathcal{O}_{S_{0}}$-Modules). Let $m_{\lambda} : \mathcal{A}_{\lambda} \otimes
\mathcal{A}_{\lambda} \to \mathcal{A}_{\lambda}$ be the homomorphism of $\mathcal{O}_{S_{0}}$-Modules that defines the
multiplication in the $\mathcal{O}_{S_{0}}$-Algebra $\mathcal{A}_{\lambda}$; the hypothesis on the $\phi_{\mu \lambda}$
entails that the $m_{\lambda}$ form an inductive system of homomorphisms, and since the functor `lim` commutes with
tensor product, $m = \lim m_{\lambda}$ is a homomorphism $\mathcal{A} \otimes \mathcal{A} \to \mathcal{A}$ of
$\mathcal{O}_{S_{0}}$-Modules; by passage to the limit on the commutative diagrams expressing the associativity of
$m_{\lambda}$ and the existence of a unit section in $\mathcal{A}_{\lambda}$, one sees that $m$ defines on $\mathcal{A}$
a structure of $\mathcal{O}_{S_{0}}$-Algebra and that $\phi_{\lambda}$ is a homomorphism of
$\mathcal{O}_{S_{0}}$-Algebras for every $\lambda \in L$. Moreover $\mathcal{A}$ is the inductive limit of the system
$(\mathcal{A}_{\lambda}, \phi_{\mu \lambda})$ in the category of $\mathcal{O}_{S_{0}}$-Algebras; in other words, for
every $\mathcal{O}_{S_{0}}$-Algebra $\mathcal{B}$, the canonical map

```text
  (8.2.1.1)    Hom_{S_0-Alg.}(𝒜, ℬ) → lim Hom_{S_0-Alg.}(𝒜_λ, ℬ)
```

which to every homomorphism $f : \mathcal{A} \to \mathcal{B}$ of $\mathcal{O}_{S_{0}}$-Algebras associates the family
$(f \circ \phi_{\lambda})$, is bijective. Indeed, one already knows that it is injective and identifies
$\operatorname{Hom}_{S_{0}-Alg.}(\mathcal{A}, \mathcal{B})$ with a part of `lim Hom_{S_0-Mod.}(𝒜_λ, ℬ)`; everything
comes down to seeing that if $(f_{\lambda})$ is an inductive system of homomorphisms of $\mathcal{O}_{S_{0}}$-Algebras,
$f_{\lambda} : \mathcal{A}_{\lambda} \to \mathcal{B}$, its inductive limit $f : \mathcal{A} \to \mathcal{B}$, which by
definition is a homomorphism of $\mathcal{O}_{S_{0}}$-Modules, is also a homomorphism of $\mathcal{O}_{S_{0}}$-Algebras;
but this results from passage to the inductive limit in the commutative diagram of homomorphisms of
$\mathcal{O}_{S_{0}}$-Modules expressing that the $f_{\lambda}$ are Algebra homomorphisms, and from the fact that the
functor `lim` commutes with tensor products.

One will note finally that if the $\mathcal{A}_{\lambda}$ are commutative $\mathcal{O}_{S_{0}}$-Algebras, the same is
true of $\mathcal{A}$.

**(8.2.2)** Suppose now that `S_0` is a prescheme and that the $\mathcal{A}_{\lambda}$ are *quasi-coherent*
(commutative) $\mathcal{O}_{S_{0}}$-Algebras; one knows then that $\mathcal{A} = \lim \mathcal{A}_{\lambda}$ is a
quasi-coherent $\mathcal{O}_{S_{0}}$-Algebra `(I, 4.1.1)`. Let us denote by $S_{\lambda}$ (resp. $S$) the spectrum of
the $\mathcal{O}_{S_{0}}$-Algebra $\mathcal{A}_{\lambda}$ (resp. $\mathcal{A}$) `(II, 1.3.1)`, and let
$u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ (for $\lambda \leq \mu$) and $u_{\lambda} : S \to S_{\lambda}$ be the
`S_0`-morphisms corresponding to the homomorphisms $\phi_{\mu \lambda}$ and $\phi_{\lambda}$ respectively `(II, 1.2.7)`;
it is clear that $(S_{\lambda}, u_{\mu \lambda})$ is a projective system in the category of `S_0`-preschemes. One will
note that the $u_{\mu \lambda}$ and $u_{\lambda}$ are *affine* morphisms `(II, 1.6.2)`, hence *quasi-compact* and
*separated*.

**Proposition (8.2.3).**

<!-- label: IV.8.2.3 -->

*With the notations of `(8.2.2)`, the morphisms $u_{\lambda} : S \to S_{\lambda}$ make $S$ a projective limit of the
projective system $(S_{\lambda}, u_{\mu \lambda})$ in the category of preschemes. Moreover, if $h : S_{0} \to T$ is a
morphism, making every `S_0`-prescheme a $T$-prescheme, $S$ is also a projective limit of the system $(S_{\lambda},
u_{\mu \lambda})$ in the category of $T$-preschemes.*

Let us first prove the second assertion of the statement in the case $T = S_{0}$.

<!-- original page 8 -->

Everything comes down to showing that if $X$ is an arbitrary `S_0`-prescheme, the canonical map

```text
  (8.2.3.1)    Hom_{S_0}(X, S) → lim Hom_{S_0}(X, S_λ)
```

which to every `S_0`-morphism $v : X \to S$ associates the family $(u_{\lambda} \circ v)$, is bijective. Now, if $g : X
\to S_{0}$ is the structure morphism and if one sets $\mathcal{B} = g_{*}(\mathcal{O}_{X})$, which is an
$\mathcal{O}_{S_{0}}$-Algebra, the map `(8.2.3.1)` is canonically identified with `(8.2.1.1)` `(II, 1.2.7)`, and the
conclusion therefore results from what was seen in `(8.2.1)`.

The other assertions of `(8.2.3)` are consequences of the following general lemma:

**Lemma (8.2.4).**

<!-- label: IV.8.2.4 -->

*Let $\mathcal{C}$ be a category, $T$ an object of $\mathcal{C}$, $\mathcal{C}_{T}$ the subcategory of objects of
$\mathcal{C}$ above $T$. Let $(S_{\lambda}, u_{\mu \lambda})$ be a projective system in $\mathcal{C}_{T}$; then every
projective limit of this system in $\mathcal{C}_{T}$ is also a projective limit in $\mathcal{C}$, and conversely.*

Let $f_{\lambda} : S_{\lambda} \to T$ be the structure morphism. Suppose that $S$ is a projective limit of
$(S_{\lambda}, u_{\mu \lambda})$ in $\mathcal{C}$, and denote by $u_{\lambda} : S \to S_{\lambda}$ the corresponding
canonical morphisms. Consider then a projective system of $T$-morphisms $w_{\lambda} : Y \to S_{\lambda}$, where $Y \in
\mathcal{C}_{T}$. There exists by hypothesis a unique morphism $w : Y \to S$ (in $\mathcal{C}$) such that $w_{\lambda} =
u_{\lambda} \circ w$ for every $\lambda$. The hypothesis that the $u_{\lambda}$ are $T$-morphisms entails that the
morphisms $f_{\lambda} \circ u_{\lambda} : S \to T$ are all equal, and this morphism $f$ therefore makes $S$ a
$T$-object. If $g : Y \to T$ is the structure morphism of $Y$, one has then $f \circ w = f_{\lambda} \circ u_{\lambda}
\circ w = f_{\lambda} \circ w_{\lambda} = g$ for every $\lambda$, which proves that $w$ is a $T$-morphism. Conversely,
suppose (with the same notations) that $S$ is a projective limit of $(S_{\lambda}, u_{\mu \lambda})$ in
$\mathcal{C}_{T}$, and consider now a projective system of morphisms (of $\mathcal{C}$) $w_{\lambda} : Y \to
S_{\lambda}$. The composite morphisms $f_{\lambda} \circ w_{\lambda} : Y \to T$ are then all equal: indeed, for any two
indices $\lambda$, $\mu$, there is an index $\nu$ such that $\lambda \leq \nu$ and $\mu \leq \nu$, whence $f_{\nu} =
f_{\lambda} \circ u_{\lambda \nu} = f_{\mu} \circ u_{\mu \nu}$; since $w_{\lambda} = u_{\lambda \nu} \circ w_{\nu}$ and
$w_{\mu} = u_{\mu \nu} \circ w_{\nu}$, one has $f_{\lambda} \circ w_{\lambda} = f_{\lambda} \circ u_{\lambda \nu} \circ
w_{\nu} = f_{\nu} \circ w_{\nu}$ and one sees in the same way that $f_{\mu} \circ w_{\mu} = f_{\nu} \circ w_{\nu}$. If
$g : Y \to T$ is the unique morphism thus defined, $g$ makes $Y$ a $T$-object, and the $w_{\lambda}$ are then
$T$-morphisms; they consequently have a projective limit $w : Y \to S$ which is a $T$-morphism, and *a fortiori* a
morphism of $\mathcal{C}$; moreover the first part of the reasoning shows that every projective limit $w'$ (in
$\mathcal{C}$) of the projective system $(w_{\lambda})$ is necessarily also a $T$-morphism, hence equal to $w$, which
completes the proof of the lemma.

**Proposition (8.2.5).**

<!-- label: IV.8.2.5 -->

*Under the conditions of `(8.2.2)`, let $\alpha$ be an element of $L$, $X_{\alpha}$ an $S_{\alpha}$-prescheme. For every
$\lambda \geq \alpha$, set $X_{\lambda} = X_{\alpha} \times_{S_{\alpha}} S_{\lambda}$, and for $\alpha \leq \lambda \leq
\mu$, set $v_{\mu \lambda} = 1_{X_{\alpha}} \times u_{\mu \lambda}$, so that $(X_{\lambda}, v_{\mu \lambda})$ is a
projective system of $X_{\alpha}$-preschemes, whose index set is formed of the $\lambda \geq \alpha$ in $L$. Set
likewise $X = X_{\alpha} \times_{S_{\alpha}} S$ and $v_{\lambda} = 1_{X_{\alpha}} \times u_{\lambda}$. Then the
$X_{\alpha}$-morphisms $v_{\lambda} : X \to X_{\lambda}$ make $X$ a projective limit of the projective system
$(X_{\lambda}, v_{\mu \lambda})$ in the category of $X_{\alpha}$-preschemes, or in the category of all preschemes.*

This will again result from the following general lemma:

**Lemma (8.2.6).**

<!-- label: IV.8.2.6 -->

*Let $\mathcal{C}$ be a category in which fibre products exist, $q : T' \to T$ a morphism of $\mathcal{C}$,
$\mathcal{C}_{T}$ (resp. $\mathcal{C}_{T'}$) the category of objects of $\mathcal{C}$ above $T$ (resp. $T'$).*

<!-- original page 9 -->

*Let $(S_{\lambda}, u_{\mu \lambda})$ be a projective system (not necessarily filtered) in $\mathcal{C}_{T}$, and set
$S'_{\lambda} = S_{\lambda} \times_{T} T'$, $u'_{\mu \lambda} = u_{\mu \lambda} \times 1_{T'}$, so that $(S'_{\lambda},
u'_{\mu \lambda})$ is a projective system in $\mathcal{C}_{T'}$. Then, if $(S, u_{\lambda})$ is a projective limit of
$(S_{\lambda}, u_{\mu \lambda})$ in $\mathcal{C}_{T}$, $(S \times_{T} T', u_{\lambda} \times 1_{T'})$ is a projective
limit of $(S'_{\lambda}, u'_{\mu \lambda})$ in $\mathcal{C}_{T'}$.*

One has by hypothesis, for every $\lambda$, a commutative diagram

```text
  S'  ──u'_λ──→  S'_λ  ──h'_λ──→  T'
   │              │                │
   p│            p_λ│               q
   ↓              ↓                ↓
   S   ──u_λ───→  S_λ  ───f_λ───→  T
```

where one has set $S' = S \times_{T} T'$, $u'_{\lambda} = u_{\lambda} \times 1_{T'}$, $h'_{\lambda} = f_{\lambda} \times
1_{T'}$. Let $Y$ be a $T'$-object, $g' : Y \to T'$ the corresponding morphism, and consider a projective system of
$T'$-morphisms $w'_{\lambda} : Y \to S'_{\lambda}$. Then $Y$ is a $T$-object via the morphism $g = q \circ g'$, and the
$w_{\lambda} = p_{\lambda} \circ w'_{\lambda}$ are $T$-morphisms, since $h_{\lambda} \circ w_{\lambda} = h_{\lambda}
\circ p_{\lambda} \circ w'_{\lambda} = q \circ h'_{\lambda} \circ w'_{\lambda} = q \circ g'$ by hypothesis. Moreover,
one verifies at once that $(w_{\lambda})$ is a projective system. There exists therefore by hypothesis a unique
$T$-morphism $w : Y \to S$ such that $u_{\lambda} \circ w = w_{\lambda}$ for every $\lambda$. By definition of the fibre
product, there is a unique $T'$-morphism $w' : Y \to S'$ such that $p \circ w' = w$. One has then $u_{\lambda} \circ p
\circ w' = u_{\lambda} \circ w = w_{\lambda} = p_{\lambda} \circ w'_{\lambda}$, which can also be written $p_{\lambda}
\circ u'_{\lambda} \circ w' = p_{\lambda} \circ w'_{\lambda}$; on the other hand, by writing that $w'$ is a
$T'$-morphism, one gets $h'_{\lambda} \circ u'_{\lambda} \circ w' = g' = h'_{\lambda} \circ w'_{\lambda}$. The
definition of $S'_{\lambda}$ as fibre product $S_{\lambda} \times_{T} T'$ thus gives $u'_{\lambda} \circ w' =
w'_{\lambda}$, and it is immediate that $w'$ is the unique $T'$-morphism verifying these relations, whence the lemma.

**Remark (8.2.7).**

<!-- label: IV.8.2.7 -->

Given an arbitrary ringed space $S$, the inductive limits with respect to an arbitrary preordered set $L$ (not
necessarily filtered) exist in the category of commutative $\mathcal{O}_{S}$-Algebras, since the filtered inductive
limit exists by `(8.2.1)` and on the other hand, for two homomorphisms of $\mathcal{O}_{S}$-Algebras $\mathcal{A} \to
\mathcal{B}$, $\mathcal{A} \to \mathcal{C}$, the tensor product $\mathcal{B} \otimes_{\mathcal{A}} \mathcal{C}$ is the
corresponding "amalgamated sum" in this category. When $S$ is a prescheme, one knows that the tensor product
$\mathcal{B} \otimes_{\mathcal{A}} \mathcal{C}$ is a quasi-coherent $\mathcal{O}_{S}$-Algebra when this is so of
$\mathcal{A}$, $\mathcal{B}$ and $\mathcal{C}$ `(I, 1.3.13)`; one concludes that, in the category of *quasi-coherent*
$\mathcal{O}_{S}$-Algebras, the inductive limits for an arbitrary preordered index set always exist. This permits one to
generalize the definition of a projective limit of preschemes and Propositions `(8.2.3)` and `(8.2.5)` to the case where
the preordered set $L$ is not necessarily filtered.

**(8.2.8)** With the notations of `(8.2.2)`, set $u_{\mu \lambda} = (\psi_{\mu \lambda}, \theta_{\mu \lambda})$ and
$u_{\lambda} = (\psi_{\lambda}, \theta_{\lambda})$; thus $(S_{\lambda}, \psi_{\mu \lambda})$ is a projective system of
topological spaces and $(\psi_{\lambda})$ an inductive system of continuous maps $S \to S_{\lambda}$ of the spaces
underlying the preschemes $S$ and $S_{\lambda}$ respectively.

**Proposition (8.2.9).**

<!-- label: IV.8.2.9 -->

*With the notations of `(8.2.8)`, the projective limit of the projective system $(\psi_{\lambda})$ of continuous maps is
a homeomorphism of the space underlying $S$ onto the projective limit of the projective system $(S_{\lambda}, \psi_{\mu
\lambda})$ of topological spaces.*

Let $T$ be the topological space limit of the system $(S_{\lambda}, \psi_{\mu \lambda})$ and set $\psi = \lim
\psi_{\lambda} : S \to T$. One may restrict to the case where $S_{0} = S_{\alpha}$ for some $\alpha \in L$, and $\lambda
\geq \alpha$.

<!-- original page 10 -->

(i) Let us show first that the topology of $S$ is the inverse image under $\psi$ of the topology of $T$; in other words,
if $\pi_{\lambda} : T \to S_{\lambda}$ is the canonical map, one must show that every open set of $S$ is a union of open
sets of the form $\psi^{-1}(\pi^{-1}_{\lambda}(U_{\lambda}))$, where $U_{\lambda}$ is open in $S_{\lambda}$. Now every
open set of $S$ is by definition a union of open sets obtained as follows: one considers an affine open set `U_0` of
`S_0`, with ring `A_0`, so that $u^{-1}_{0}(U_{0})$ is the affine open set of $S$ with ring $A = \Gamma(U_{0},
\mathcal{A})$, then one takes an element $f \in A$ and one considers in $\operatorname{Spec}(A)$, identified with
$u^{-1}_{0}(U_{0})$, the open set $D(f)$. It is these open sets $D(f)$ that form a base of the topology of $S$
`(II, 1.3.1)`. Now, if one sets $A_{\lambda} = \Gamma(U_{0}, \mathcal{A}_{\lambda})$, one has $A = \lim A_{\lambda}$
`(I, 1.3.9)`, so there exists an index $\lambda$ such that $f$ is the canonical image of an element $f_{\lambda} \in
A_{\lambda}$; one has then $D(f) = \psi^{-1}_{\lambda}(D(f_{\lambda}))$ `(I, 1.2.2)`, and since $\psi_{\lambda} =
\pi_{\lambda} \circ \psi$, our assertion is proved.

(ii) Let us now prove that $\psi$ is bijective, which will complete the proof. Since $S$ is a Kolmogorov space, it
already follows from (i) that $\psi$ is injective, and it therefore remains to show that $\psi$ is surjective. One can
evidently replace $T$ for this purpose by an open set $\pi^{-1}_{0}(U_{0})$, where `U_0` is an affine open set in
$S_{\alpha} = S_{0}$, so one can limit oneself to the case where the $S_{\lambda}$ and $S$ are affine, in other words
$\mathcal{A}_{\lambda}$ is the sheaf associated with an `A_0`-algebra $A_{\lambda}$, and $\mathcal{A}$ the sheaf of
algebras associated with $A = \lim A_{\lambda}$; we shall again denote by $\phi_{\mu \lambda} : A_{\lambda} \to A_{\mu}$
and $\phi_{\lambda} : A_{\lambda} \to A$ the canonical homomorphisms. By definition, an element of $T$ is a family
$(\mathfrak{p}_{\lambda})_{\lambda \in L}$, where $\mathfrak{p}_{\lambda}$ is a prime ideal of $A_{\lambda}$ and where
one has $\mathfrak{p}_{\lambda} = \phi^{-1}_{\mu \lambda}(\mathfrak{p}_{\mu})$ for $\lambda \leq \mu$. One knows then
`((5.13.3) and (5.13.1))` that there is a prime ideal $\mathfrak{p}$ of $A$ such that $\mathfrak{p}_{\lambda} =
\phi^{-1}_{\lambda}(\mathfrak{p})$ for every $\lambda \in L$, which completes the proof.

In particular, we have thus proved the

**Corollary (8.2.10).**

<!-- label: IV.8.2.10 -->

*Let $(A_{\lambda})_{\lambda \in L}$ be a filtered inductive system of rings, and let $A = \lim A_{\lambda}$,
$\phi_{\lambda} : A_{\lambda} \to A$ the canonical homomorphisms. The canonical map $\mathfrak{p} \mapsto
(\phi^{-1}_{\lambda}(\mathfrak{p}))$ is a homeomorphism of $\operatorname{Spec}(A)$ onto the topological space $\lim
\operatorname{Spec}(A_{\lambda})$.*

**Corollary (8.2.11).**

<!-- label: IV.8.2.11 -->

*With the notations of `(8.2.8)`, for every quasi-compact open set $U$ of $S$, there exist an index $\lambda$ and a
quasi-compact open set $U_{\lambda}$ of $S_{\lambda}$ such that $U = \psi^{-1}_{\lambda}(U_{\lambda})$.*

This results from the fact that, by definition of the projective limit topology, the $\psi^{-1}_{\lambda}(U_{\lambda})$
($U_{\lambda}$ quasi-compact open in $S_{\lambda}$) form a base of the topology of $S$, and from the fact that the index
set $L$ is filtered.

**Corollary (8.2.12).**

<!-- label: IV.8.2.12 -->

*With the notations of `(8.2.8)`, the inductive limit of the inductive system of homomorphisms $\theta^{#}_{\lambda} :
\psi^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}}) \to \mathcal{O}_{S}$ of sheaves of rings on $S$ is an isomorphism*

$$ (8.2.12.1) \lim \psi^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}}) \xrightarrow{\sim} \mathcal{O}_{S}. $$

One can evidently suppose the $S_{\lambda}$ affine; with the notations of the proof of `(8.2.9)`, everything comes down
to seeing that the inductive limit of the system of canonical maps $(A_{\lambda})_{\mathfrak{p}_{\lambda}} \to
A_{\mathfrak{p}}$ is an isomorphism, which is none other than `(5.13.3, (ii))`.

<!-- original page 11 -->

**Proposition (8.2.13).**

<!-- label: IV.8.2.13 -->

*Suppose that the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are open immersions, so that $S_{\mu}$ is
identified with the sub-prescheme induced on an open set of $S_{\lambda}$ for $\lambda \leq \mu$. Then, for every
$\alpha \in L$, the space underlying the prescheme $S$ is identified with the subspace of $S_{\alpha}$ intersection of
the $S_{\lambda}$ for $\lambda \geq \alpha$, and the structure sheaf $\mathcal{O}_{S}$ with the sheaf induced
`(G, II, 1.5)` by $\mathcal{O}_{S_{\alpha}}$ on this intersection; more generally, for every
$\mathcal{O}_{S_{\alpha}}$-Module $\mathcal{F}_{\alpha}$, $u^{*}_{\alpha}(\mathcal{F}_{\alpha})$ is identified with the
$\mathcal{O}_{S}$-Module induced by $\mathcal{F}_{\alpha}$ on $S$.*

The first assertion results from `(8.2.9)`, in view of the definition of a projective limit of topological spaces; in
addition all the $\psi^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}})$ are equal to the sheaf induced by
$\mathcal{O}_{S_{\alpha}}$ on $S$ by definition $(0_{I}, 3.7.1)$ and, with the notations of the proof of `(8.2.9)`, the
homomorphisms $(A_{\lambda})_{\mathfrak{p}_{\lambda}} \to (A_{\alpha})_{\mathfrak{p}}$ are bijective for a system
$(\mathfrak{p}_{\lambda})$ of prime ideals corresponding to a single point of $S$; the assertion relative to
$\mathcal{O}_{S}$ therefore follows from `(8.2.12)`. The last assertion results then from the definition of
$u^{*}_{\alpha}(\mathcal{F}_{\alpha})$ $(0_{I}, 4.3.1)$.

**Remark (8.2.14).**

<!-- label: IV.8.2.14 -->

The results of `(8.2.9)` and `(8.2.12)` show that $S$ is the projective limit of the projective system $(S_{\lambda},
u_{\mu \lambda})$ in the category of all ringed spaces (or of all ringed spaces in local rings). Indeed, let $Y$ be a
ringed space, and consider a projective system of morphisms of ringed spaces $w_{\lambda} : Y \to S_{\lambda}$. If one
sets $w_{\lambda} = (p_{\lambda}, \omega_{\lambda})$, the $p_{\lambda}$ form a projective system of continuous maps and,
by virtue of `(8.2.9)`, their projective limit $p$ is identified with a continuous map $Y \to S$ such that $p_{\lambda}
= \psi_{\lambda} \circ p$. On the other hand, the $\omega^{#}_{\lambda} : p^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}}) \to
\mathcal{O}_{Y}$ form an inductive system of homomorphisms of sheaves of rings; since one may write
$p^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}}) = p^{*}(\psi^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}}))$ and the functor
$p^{*}$ is exact, the inductive limit of the $p^{*}_{\lambda}(\mathcal{O}_{S_{\lambda}})$ is $p^{*}(\mathcal{O}_{S})$ by
virtue of `(8.2.12)`, and there is therefore a unique homomorphism $\omega^{#} : p^{*}(\mathcal{O}_{S}) \to
\mathcal{O}_{Y}$ such that $\omega^{#}_{\lambda} = \omega^{#} \circ p^{*}(\theta^{#}_{\lambda})$, which proves our
assertion.

### 8.3. Constructible parts in a projective limit of preschemes

**(8.3.1)** In all that follows in this section, we suppose the conditions of `(8.2.2)` to be satisfied, and we preserve
its notations.

**Theorem (8.3.2).**

<!-- label: IV.8.3.2 -->

*For every $\lambda$, let $E_{\lambda}$, $F_{\lambda}$ be two parts of $S_{\lambda}$. Set*

```text
  (8.3.2.1)    E = ⋂_λ u_λ⁻¹(E_λ),    F = ⋃_λ u_λ⁻¹(F_λ).
```

*Assume the following conditions:*

*(i) For every $\lambda$, $E_{\lambda}$ is pro-constructible and $F_{\lambda}$ is ind-constructible `(1.9.4)`.*

*(ii) For $\lambda \leq \mu$, one has $u^{-1}_{\mu \lambda}(E_{\lambda}) \supset E_{\mu}$ and $u^{-1}_{\mu
\lambda}(F_{\lambda}) \subset F_{\mu}$.*

*(iii) There exists $\alpha \in L$ such that $S_{\alpha}$ is quasi-compact (which entails that $S_{\lambda}$ is
quasi-compact for $\lambda \geq \alpha$).*

*Then the following properties are equivalent:*

*a) $E \subset F$.*

<!-- original page 12 -->

*b) There exists $\lambda \geq \alpha$ such that $u^{-1}_{\lambda}(E_{\lambda}) \subset u^{-1}_{\lambda}(F_{\lambda})$
(and one then has $u^{-1}_{\mu}(E_{\mu}) \subset u^{-1}_{\mu}(F_{\mu})$ for $\mu \geq \lambda$).*

*c) There exists $\lambda \geq \alpha$ such that $E_{\lambda} \subset F_{\lambda}$ (and one then has $E_{\mu} \subset
F_{\mu}$ for $\mu \geq \lambda$).*

The remarks in parentheses in b) and c) result from (ii). Set

```text
  G_λ = E_λ ∩ (S_λ − F_λ),    G = E ∩ (S − F).
```

Then $G_{\lambda}$ is a pro-constructible part of $S_{\lambda}$ `(1.9.5, (i))`, and by virtue of `(8.3.2.1)` and (ii),
one has $G = \bigcap_{\lambda} u^{-1}_{\lambda}(G_{\lambda})$.

One is thus reduced to proving the particular case of `(8.3.2)` corresponding to $F_{\lambda} = \emptyset$ for every
$\lambda$:

**Corollary (8.3.3).**

<!-- label: IV.8.3.3 -->

*For every $\lambda$, let $E_{\lambda}$ be a pro-constructible part of $S_{\lambda}$ such that, for $\lambda \leq \mu$,
one has $E_{\mu} \subset u^{-1}_{\mu \lambda}(E_{\lambda})$. Suppose there exists $\alpha \in L$ such that $S_{\alpha}$
is quasi-compact. Then the following conditions are equivalent:*

*a) $E = \bigcap_{\lambda} u^{-1}_{\lambda}(E_{\lambda}) = \emptyset$.*

*b) There exists $\lambda$ such that $u^{-1}_{\lambda}(E_{\lambda}) = \emptyset$ (and then $u^{-1}_{\mu}(E_{\mu}) =
\emptyset$ for $\mu \geq \lambda$).*

*c) There exists $\lambda$ such that $E_{\lambda} = \emptyset$ (and then $E_{\mu} = \emptyset$ for $\mu \geq \lambda$).*

It is clear that c) implies a). Let us prove that a) entails b): since $S_{\alpha}$ is quasi-compact, so is $S$
`(8.2.2)`; $E_{\lambda}$ being pro-constructible, so is $u^{-1}_{\lambda}(E_{\lambda})$ `(1.9.5, (vi))`; the filtered
decreasing family of pro-constructible sets $u^{-1}_{\lambda}(E_{\lambda})$ then has empty intersection, hence `(1.9.9)`
one of them is empty.

Finally, let us show that b) entails c). Since $S_{\alpha}$ is quasi-compact and $L$ filtered, one can replace
$S_{\alpha}$ by an affine open set, so one can suppose `(8.2.2)` that $S$ and the $S_{\lambda}$ for $\lambda \geq
\alpha$ are affine; one has then `(1.9.2.1)`, for $\mu \geq \lambda$,

```text
  u_λ⁻¹(E_λ) = ⋂_{μ ≥ λ} (E_λ ∩ u_{μλ}(S_μ)),
```

whence $E_{\lambda} \cap u_{\lambda}(S) = \bigcap_{\mu \geq \lambda} (E_{\lambda} \cap u_{\mu \lambda}(S_{\mu}))$.

Now, since $u_{\lambda}$ and the $u_{\mu \lambda}$ are quasi-compact, $u_{\lambda}(S)$ and $u_{\mu \lambda}(S_{\mu})$
are pro-constructible in $S_{\lambda}$ `(1.9.5, (vii))`, so the sets $E_{\lambda} \cap u_{\mu \lambda}(S_{\mu})$ for
$\mu \geq \lambda$ form a filtered decreasing family of pro-constructible parts of $S_{\lambda}$. Since $S_{\lambda}$ is
quasi-compact, hypothesis b) entails that the intersection of this family is empty, hence `(1.9.9)` one of the sets
$E_{\lambda} \cap u_{\mu \lambda}(S_{\mu})$ is empty, hence $E_{\mu} \subset u^{-1}_{\mu \lambda}(E_{\lambda})$ is
empty. Q.E.D.

**Corollary (8.3.4).**

<!-- label: IV.8.3.4 -->

*For every $\lambda$, let $F_{\lambda}$ be an ind-constructible part of $S_{\lambda}$ such that for $\lambda \leq \mu$
one has $u^{-1}_{\mu \lambda}(F_{\lambda}) \subset F_{\mu}$. Suppose there exists $\alpha \in L$ such that $S_{\alpha}$
is quasi-compact. Then the following conditions are equivalent:*

*a) The set $F = \bigcup_{\lambda} u^{-1}_{\lambda}(F_{\lambda})$ is equal to $S$.*

*b) There exists $\lambda$ such that $u^{-1}_{\lambda}(F_{\lambda}) = S$ (and then $u^{-1}_{\mu}(F_{\mu}) = S$ for $\mu
\geq \lambda$).*

<!-- original page 13 -->

*c) There exists $\lambda$ such that $F_{\lambda} = S_{\lambda}$ (and then $F_{\mu} = S_{\mu}$ for $\mu \geq \lambda$).*

This follows at once from `(8.3.3)` by passage to complements.

**Corollary (8.3.5).**

<!-- label: IV.8.3.5 -->

*For every $\lambda$, let $E_{\lambda}$, $F_{\lambda}$ be two constructible parts of $S_{\lambda}$ such that, for
$\lambda \leq \mu$, one has $E_{\mu} \subset u^{-1}_{\mu \lambda}(E_{\lambda})$ and $F_{\mu} \supset u^{-1}_{\mu
\lambda}(F_{\lambda})$. Suppose there exists an index $\alpha$ such that $S_{\alpha}$ is quasi-compact. Then, in order
that $E \subset F$ (resp. $E = F$), it is necessary and sufficient that there exist $\lambda$ such that $E_{\lambda}
\subset F_{\lambda}$ (resp. $E_{\lambda} = F_{\lambda}$), in which case one also has $E_{\mu} \subset F_{\mu}$ (resp.
$E_{\mu} = F_{\mu}$) for $\mu \geq \lambda$.*

This is a particular case of `(8.3.2)`.

In particular:

**Corollary (8.3.6).**

<!-- label: IV.8.3.6 -->

*Suppose there exists an $\alpha$ such that $S_{\alpha}$ is quasi-compact. In order that $S = \emptyset$, it is
necessary and sufficient that there exist $\lambda$ such that $S_{\lambda} = \emptyset$.*

**Corollary (8.3.7).**

<!-- label: IV.8.3.7 -->

*One has, for every $\lambda$,*

```text
  (8.3.7.1)    u_λ(S) = ⋂_{μ ≥ λ} u_{μλ}(S_μ).
```

It is clear that the first member of `(8.3.7.1)` is contained in the second. Let $s$ be a point of $S_{\lambda}$ and set
$X_{\lambda} = \operatorname{Spec}(k(s))$; consider the projective system $(X_{\mu}, z_{\nu \mu})$ where $X_{\mu} =
X_{\lambda} \times_{S_{\lambda}} S_{\mu}$ and $z_{\nu \mu} = 1 \times u_{\nu \mu}$ for $\lambda \leq \mu \leq \nu$; its
projective limit is $X = X_{\lambda} \times_{S_{\lambda}} S$ and $p_{\lambda} = 1 \times u_{\lambda}$ is the canonical
map $X \to X_{\lambda}$ `(8.2.5)`. If $s \in \bigcap_{\mu \geq \lambda} u_{\mu \lambda}(S_{\mu})$, this entails that
$X_{\mu} \neq \emptyset$ for every $\mu \geq \lambda$ `(I, 3.4.8)`; it follows then from `(8.3.6)` that $X \neq
\emptyset$, hence $s \in u_{\lambda}(S)$ by `(I, 3.4.8)`.

**Proposition (8.3.8).**

<!-- label: IV.8.3.8 -->

*(i) In order that the morphism $u_{\lambda} : S \to S_{\lambda}$ be dominant (resp. surjective), it is necessary and
sufficient that for $\mu \geq \lambda$ the morphism $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ be dominant (resp.
surjective).*

*(ii) If, for some index $\lambda$, the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are flat (resp. faithfully
flat) for all $\mu \geq \lambda$, then the morphism $u_{\lambda} : S \to S_{\lambda}$ is flat (resp. faithfully flat).*

*(iii) Suppose that the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are surjective for $\mu \geq \lambda$. In
order that $u_{\lambda}$ be an open morphism (resp. universally open), it is necessary and sufficient that, for every
$\mu \geq \lambda$, $u_{\mu \lambda}$ be an open morphism (resp. universally open).*

(i) Since $u_{\lambda}(S) \subset u_{\mu \lambda}(S_{\mu})$ for $\mu \geq \lambda$, the necessity of the conditions is
trivial, and it follows at once from `(8.3.7.1)` that if the $u_{\mu \lambda}$ are surjective, so is $u_{\lambda}$.
Suppose now the $u_{\mu \lambda}$ dominant for $\mu \geq \lambda$, and consider in $S_{\lambda}$ a non-empty
quasi-compact open set $U_{\lambda}$; then the $U_{\mu} = u^{-1}_{\mu \lambda}(U_{\lambda})$ for $\mu \geq \lambda$ form
a projective system whose projective limit is $U = u^{-1}_{\lambda}(U_{\lambda})$ `(8.2.5)`. By hypothesis the $U_{\mu}$
are all non-empty, so the same is true of $U$ by `(8.3.6)`, which proves that $u_{\lambda}$ is dominant.

(ii) By virtue of (i), it suffices to consider the case where the $u_{\mu \lambda}$ are flat; one can then restrict to
the case where $S_{\lambda}$ is affine, so also the $S_{\mu}$ for $\mu \geq \lambda$ and $S$, and the assertion follows
then from `(2.1.2)` and $(0_{I}, 6.2.3)$.

(iii) By virtue of `(8.2.5)` and `(I, 3.5.2)`, it suffices to treat the case of open morphisms. Since $u_{\lambda} =
u_{\mu \lambda} \circ u_{\mu}$ and $u_{\mu}$ is surjective, one knows that if $u_{\lambda}$ is open so is $u_{\mu
\lambda}$ for $\mu \geq \lambda$ `(Bourbaki, Top. gén., chap. I, 3rd ed., §5, n° 1, prop. 1)`.

<!-- original page 14 -->

Conversely, to show that $u_{\lambda}$ is open when all the $u_{\mu \lambda}$ are open for $\mu \geq \lambda$, it
suffices to see that for every quasi-compact open set $V$ of $S$, $u_{\lambda}(V)$ is open in $S_{\lambda}$; but there
exists then $\mu \geq \lambda$ such that $V = u^{-1}_{\mu}(V_{\mu})$, where $V_{\mu}$ is open in $S_{\mu}$ `(8.2.11)`;
since $u_{\mu}$ is surjective, one has $V_{\mu} = u_{\mu}(V)$ and $u_{\lambda}(V) = u_{\mu \lambda}(u_{\mu}(V))$ is
therefore open by hypothesis.

One will note that it may happen that all the $u_{\mu \lambda}$ are open without $u_{\lambda}$ being so when the $u_{\mu
\lambda}$ are not surjective. One has an example by considering an integral ring $A$ which is not a field, and its field
of fractions $K$, which is the inductive limit of the $A_{f}$, where $f$ runs through $A - {0}$; if one sets $S_{1} =
\operatorname{Spec}(A)$, $S_{f} = \operatorname{Spec}(A_{f})$, one has $S = \lim S_{f} = \operatorname{Spec}(K)$, and
the morphism $S \to S_{1}$ is not open, although the morphisms $S_{f} \to S_{1}$ are.

**(8.3.9)** For every prescheme $X$, we shall denote as usual by $\mathfrak{P}(X)$ the set of parts of the underlying
set of $X$, by $\mathfrak{E}(X)$ (resp. $\mathfrak{Oc}(X)$, $\mathfrak{Fc}(X)$, $\mathfrak{LFc}(X)$) the set of
constructible (resp. constructible and open, resp. constructible and closed, resp. constructible and locally closed)
parts of $X$. It is clear that $(\mathfrak{P}(S_{\lambda}), u^{-1}_{\mu \lambda})$ is an inductive system of sets and
that the maps $u^{-1}_{\lambda} : \mathfrak{P}(S_{\lambda}) \to \mathfrak{P}(S)$ form an inductive system of maps,
whence, by passage to the inductive limit, a canonical map

$$ (8.3.9.1) \lim \mathfrak{P}(S_{\lambda}) \to \mathfrak{P}(S). $$

Moreover, it follows from `(1.8.2)` that $u^{-1}_{\mu \lambda}$ carries $\mathfrak{E}(S_{\lambda})$ (resp.
$\mathfrak{Oc}(S_{\lambda})$, $\mathfrak{Fc}(S_{\lambda})$, $\mathfrak{LFc}(S_{\lambda})$) into $\mathfrak{E}(S_{\mu})$
(resp. $\mathfrak{Oc}(S_{\mu})$, $\mathfrak{Fc}(S_{\mu})$, $\mathfrak{LFc}(S_{\mu})$) and that $u^{-1}_{\lambda}$
carries $\mathfrak{E}(S_{\lambda})$ (resp. $\mathfrak{Oc}(S_{\lambda})$, $\mathfrak{Fc}(S_{\lambda})$,
$\mathfrak{LFc}(S_{\lambda})$) into $\mathfrak{E}(S)$ (resp. $\mathfrak{Oc}(S)$, $\mathfrak{Fc}(S)$,
$\mathfrak{LFc}(S)$). One therefore has by restriction of `(8.3.9.1)` canonical maps

$$ (8.3.9.2) \lim \mathfrak{E}(S_{\lambda}) \to \mathfrak{E}(S) (8.3.9.3) \lim \mathfrak{Oc}(S_{\lambda}) \to
\mathfrak{Oc}(S) (8.3.9.4) \lim \mathfrak{Fc}(S_{\lambda}) \to \mathfrak{Fc}(S) (8.3.9.5) \lim
\mathfrak{LFc}(S_{\lambda}) \to \mathfrak{LFc}(S). $$

**(8.3.10)** Let $g_{\alpha} : X_{\alpha} \to S_{\alpha}$ be a morphism; with the notations of `(8.2.5)` one has as
above a canonical map $v^{-1}_{\alpha} : \lim \mathfrak{P}(X_{\lambda}) \to \mathfrak{P}(X)$; on the other hand, one has
projection morphisms $g_{\lambda} : X_{\lambda} \to S_{\lambda}$ for every $\lambda \geq \alpha$ and a projection
morphism $g : X \to S$. It is clear that the $g^{-1}_{\lambda} : \mathfrak{P}(S_{\lambda}) \to
\mathfrak{P}(X_{\lambda})$ form an inductive system of maps, and that the diagrams

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

and it follows from `(1.8.2)` that one has analogous diagrams on replacing $\mathfrak{P}$ by $\mathfrak{E}$,
$\mathfrak{Oc}$, $\mathfrak{Fc}$ or $\mathfrak{LFc}$.

It results from `(8.3.5)` that under the hypothesis that for some $\alpha \in L$, $S_{\alpha}$ is quasi-compact, the
canonical map `(8.3.9.2)` is injective. Moreover:

**Theorem (8.3.11).**

<!-- label: IV.8.3.11 -->

*Suppose there exists $\alpha \in L$ such that $S_{\alpha}$ is quasi-compact and quasi-separated. Then the canonical
maps `(8.3.9.2)`, `(8.3.9.3)`, `(8.3.9.4)` and `(8.3.9.5)` are bijective.*

By virtue of the preceding remark, it remains to prove that these maps are surjective; since every constructible part of
$S$ is a finite union of sets of the form $U \cap \complement V$, where $U$ and $V$ are open and constructible, it will
suffice to prove that `(8.3.9.3)` is surjective for the same to hold of `(8.3.9.2)` (and also of `(8.3.9.4)`, by passage
to complements). Now, since the morphisms $S_{\lambda} \to S_{\alpha}$ and $S \to S_{\alpha}$ are affine, hence
separated, the $S_{\lambda}$ for $\lambda \geq \alpha$ and $S$ are quasi-compact and quasi-separated `(1.2.2)`, and one
knows that the constructible open parts in such a prescheme are none other than the quasi-compact open parts `(1.8.1)`.
The conclusion therefore follows from `(8.2.11)` except for the map `(8.3.9.5)`. To prove that this last map is
surjective, consider a part $Z$ locally closed and constructible in $S$; $Z$ is therefore quasi-compact $(0_{III},
9.1.4)$. Since every point $x \in Z$ admits by hypothesis a quasi-compact open neighbourhood $V_{x}$ in $S$ such that $Z
\cap V_{x}$ is closed in $V_{x}$, one can cover $Z$ by a finite number of the $V_{x}$; in other words, there is a
quasi-compact open set $U$ containing $Z$ and such that $Z$ is closed in $U$; since $Z$ is constructible in $S$, it is
so also in $U$ $(0_{III}, 9.1.8)$. One knows `(8.2.11)` that there is an index $\lambda$ and a quasi-compact open set
$U_{\lambda}$ in $S_{\lambda}$ such that $U = u^{-1}_{\lambda}(U_{\lambda})$. Applying to $U$ (which is the projective
limit of the $U_{\mu} = u^{-1}_{\mu \lambda}(U_{\lambda})$ for $\mu \geq \lambda$) the fact that the map `(8.3.9.4)` is
surjective, one sees that there exists $\mu \geq \lambda$ and a constructible closed set $Z_{\mu}$ in $U_{\mu}$ such
that $Z = u^{-1}_{\mu}(Z_{\mu})$. But since the canonical immersion $U_{\mu} \to S_{\mu}$ is quasi-compact by hypothesis
`(1.2.7)`, it is of finite presentation `(1.6.2, (i))`, and $Z_{\mu}$ is also a constructible part of $S_{\mu}$ by
virtue of `(1.8.4)` and `(1.8.1)`; since $Z_{\mu}$ is evidently locally closed in $S_{\mu}$, this completes the proof.

**Corollary (8.3.12).**

<!-- label: IV.8.3.12 -->

*Suppose there exists $\alpha$ such that $S_{\alpha}$ is quasi-compact, and let, for every $\lambda$, $Z_{\lambda}$ be a
constructible part of $S_{\lambda}$ such that $Z_{\mu} = u^{-1}_{\mu \lambda}(Z_{\lambda})$ for $\mu \geq \lambda$. If
$Z = u^{-1}_{\lambda}(Z_{\lambda})$,*

<!-- original page 16 -->

*then, in order that $Z$ be open (resp. closed, resp. locally closed) in $S$, it is necessary and sufficient that there
exist $\lambda \geq \alpha$ such that $Z_{\lambda}$ be so in $S_{\lambda}$.*

Cover $S_{\alpha}$ by a finite number of affine open sets $U^{(i)}_{\alpha}$; then the $U^{(i)} =
u^{-1}_{\alpha}(U^{(i)}_{\alpha})$ form an open affine cover of $S$, and for $Z$ to be open (resp. closed, resp. locally
closed) in $S$, it is necessary and sufficient that each of the $Z \cap U^{(i)}$ be so in $U^{(i)}$. Since $L$ is
filtered and each of the $Z \cap U^{(i)}$ is constructible in $U^{(i)}$ $(0_{III}, 9.1.8)$, one can restrict to proving
the corollary when $S_{\alpha}$ is affine, hence quasi-compact and quasi-separated; but in that case it follows from
`(8.3.11)`.

**Proposition (8.3.13).**

<!-- label: IV.8.3.13 -->

*Suppose that the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are flat for $\lambda \leq \mu$, and that there
exists $\alpha$ such that $S_{\alpha}$ is quasi-compact. For every $\lambda$, let $Z_{\lambda}$, $Z'_{\lambda}$ be two
pro-constructible parts of $S_{\lambda}$, such that $Z_{\mu} = u^{-1}_{\mu \lambda}(Z_{\lambda})$ and $Z'_{\mu} =
u^{-1}_{\mu \lambda}(Z'_{\lambda})$ for $\mu \geq \lambda$; suppose moreover that $Z_{\alpha}$ is constructible in
$S_{\alpha}$. Let $Z' = u^{-1}_{\lambda}(Z_{\lambda})$, $Z'' = u^{-1}_{\lambda}(Z'_{\lambda})$; in order that
$\overline{Z}'' \subset \overline{Z}'$, it is necessary and sufficient that there exist $\lambda \geq \alpha$ such that
$\overline{Z}'_{\lambda} \subset \overline{Z}_{\lambda}$.*

Indeed, one knows that $u_{\lambda} : S \to S_{\lambda}$ is also a flat morphism for every $\lambda$ `(8.3.8)`; since
$Z_{\lambda}$ is pro-constructible, the closure of $Z_{\mu}$ for $\mu \geq \lambda$ (resp. of $Z'$) in $S_{\mu}$ (resp.
$S$) is equal to $u^{-1}_{\mu \lambda}(\overline{Z}_{\lambda})$ (resp. $u^{-1}_{\lambda}(\overline{Z}_{\lambda})$)
`(2.3.10)`. Since the $u^{-1}_{\mu \lambda}(\overline{Z}_{\lambda})$ and $u^{-1}_{\lambda}(\overline{Z}_{\lambda})$ are
constructible `(1.8.2)`, the conclusion follows from `(8.3.2)`.

### 8.4. Irreducibility and connectedness criteria for projective limits of preschemes

**Proposition (8.4.1).**

<!-- label: IV.8.4.1 -->

*Suppose there exists an index $\alpha$ such that $S_{\alpha}$ is quasi-compact.*

*(i) If $S$ is not irreducible and if in addition the space underlying $S$ is Noetherian and $S_{\alpha}$
quasi-separated, there exists $\lambda \geq \alpha$ such that, for $\mu \geq \lambda$, $S_{\mu}$ is not irreducible.*

*(ii) If $S$ is not connected, there exists $\lambda \geq \alpha$ such that, for $\mu \geq \lambda$, $S_{\mu}$ is not
connected.*

Suppose that $S$ is the union of two closed sets $S'$, `S''` distinct from $S$ (resp. disjoint non-empty closed sets).
In case (i), $S'$ and `S''` are constructible since the space $S$ is Noetherian. By virtue of `(8.3.11)`, there exist
therefore $\lambda \geq \alpha$ and two constructible closed sets $S'_{\lambda}$, $S''_{\lambda}$ of $S_{\lambda}$ such
that $S' = u^{-1}_{\lambda}(S'_{\lambda})$, $S'' = u^{-1}_{\lambda}(S''_{\lambda})$; since $S = S' \cup S''$, it follows
also from `(8.3.11)` that one can suppose that $S_{\lambda} = S'_{\lambda} \cup S''_{\lambda}$; since $S'_{\lambda}$ and
$S''_{\lambda}$ are distinct from $S_{\lambda}$, this proves that $S_{\lambda}$ is not irreducible.

In case (ii), $S'$ and `S''` are quasi-compact open sets, hence, by virtue of `(8.2.11)`, there exist $\lambda \geq
\alpha$ and two quasi-compact open sets $S'_{\lambda}$, $S''_{\lambda}$ of $S_{\lambda}$ such that $S' =
u^{-1}_{\lambda}(S'_{\lambda})$, $S'' = u^{-1}_{\lambda}(S''_{\lambda})$. Moreover, since $S'$ and `S''` are open and
closed in $S$, they are at once pro-constructible and ind-constructible `(1.9.6)`, hence constructible `(1.9.11)`, and
it follows therefore from `(8.3.5)` that one can suppose $\lambda$ taken such that $S_{\lambda} = S'_{\lambda} \cup
S''_{\lambda}$ and $S'_{\lambda} \cap S''_{\lambda} = \emptyset$, which shows that $S_{\lambda}$ is not connected.

**Proposition (8.4.2).**

<!-- label: IV.8.4.2 -->

*Suppose that the space underlying $S$ is Noetherian and that one of the following two conditions is satisfied:*

*a) For $\lambda \leq \mu$, $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ is dominant, and there exists $\alpha$ such that
$S_{\alpha}$ is quasi-compact.*

<!-- original page 18 -->

*b) There exists $\alpha$ such that the space underlying $S_{\alpha}$ is Noetherian, and for $\mu \geq \lambda$, $u_{\mu
\lambda}$ is a homeomorphism of $S_{\mu}$ onto a subspace of $S_{\lambda}$.*

*Under these conditions, there exists $\lambda$ such that, for every $\mu \geq \lambda$:*

*(i) For every irreducible component $Y_{i}$ of $S$ ($1 \leq i \leq m$), $\overline{u_{\mu}(Y_{i})}$ is an irreducible
component of $S_{\mu}$, and the map $Y_{i} \mapsto \overline{u_{\mu}(Y_{i})}$ is a bijection of the set of irreducible
components of $S$ onto the set of irreducible components of $S_{\mu}$.*

*(ii) For every connected component $C_{j}$ of $S$ ($1 \leq j \leq n$), $u_{\mu}(C_{j})$ is a connected component of
$S_{\mu}$, and the map $C_{j} \mapsto u_{\mu}(C_{j})$ is a bijection of the set of connected components of $S$ onto the
set of connected components of $S_{\mu}$.*

We shall first establish the

**Lemma (8.4.2.1).**

<!-- label: IV.8.4.2.1 -->

*Under condition a) or b) of `(8.4.2)`, there exists $\lambda$ such that, for $\mu \geq \lambda$, $u_{\mu} : S \to
S_{\mu}$ is dominant.*

In case a), this has already been proved without supposing the space $S$ Noetherian `(8.3.8, (i))`. In case b), set
$Z_{\alpha} = \overline{u_{\alpha}(S)}$; as a closed part of the Noetherian space $S_{\alpha}$, $Z_{\alpha}$ is
constructible, and since $u^{-1}_{\alpha}(Z_{\alpha}) = S$, it follows from `(8.3.5)` that there exists $\lambda \geq
\alpha$ such that, for $\mu \geq \lambda$, one has $Z_{\mu} = u^{-1}_{\mu \alpha}(Z_{\alpha}) = S_{\mu}$. But since
$u_{\alpha \mu}$ is a homeomorphism of $S_{\mu}$ onto a subspace of $S_{\alpha}$, and since the composite map $S \to
Z_{\mu} \to Z_{\alpha}$ is dominant, the same is true of $S \to Z_{\mu} = S_{\mu}$.

This lemma being proved, one may suppose that for every $\lambda$, $u_{\lambda}$ is a dominant morphism.

(i) Each of the $S_{\lambda}$ is the union of the $u_{\lambda}(Y_{i})$, which are irreducible. On the other hand, if
$U_{i}$ is the open set of $S$ complementary to the union of the $Y_{j}$ of index $j \neq i$ ($1 \leq i \leq m$), the
$U_{i}$ are pairwise disjoint and $Y_{i} = \overline{U_{i}}$ $(0_{I}, 2.1.6)$. Since the space underlying $S$ is
Noetherian, the $U_{i}$ are quasi-compact, hence there exists an index $\lambda$ and open sets $U_{i\lambda}$ of
$S_{\lambda}$ such that $U_{i} = u^{-1}_{\lambda}(U_{i\lambda})$ for $1 \leq i \leq m$ `(8.2.11)`. One concludes that if
one sets $U_{i\mu} = u^{-1}_{\mu \lambda}(U_{i\lambda})$ for $\lambda \leq \mu$, the $U_{i\mu}$ are pairwise disjoint,
for the $U_{i} = u^{-1}_{\mu}(U_{i\mu})$ are, and $u_{\mu}$ is dominant. Consequently, none of the closures
$\overline{U_{i\mu}}$ is contained in another, and $u_{\mu}(Y_{i})$ is dense in $U_{i\mu}$ since $u_{\mu}$ is dominant;
one has therefore $\overline{U_{i\mu}} = \overline{u_{\mu}(Y_{i})}$, which proves that the $\overline{U_{i\mu}}$ are the
irreducible components of $S_{\mu}$ $(0_{I}, 2.1.7)$ and completes the proof.

(ii) Since the space $S$ is Noetherian, the $C_{j}$ are open and closed in $S$ and quasi-compact; the same reasoning as
in (i) therefore shows that there exists $\lambda$ and open sets $V_{j\lambda}$ of $S_{\lambda}$ such that $C_{j} =
u^{-1}_{\lambda}(V_{j\lambda})$ for $1 \leq j \leq n$. One sees also, as in (i), that if one sets $V_{j\mu} =
u^{-1}_{\mu \lambda}(V_{j\lambda})$ for $\mu \geq \lambda$, the $V_{j\mu}$ are pairwise disjoint, and $u_{\mu}(C_{j})$
is dense in $V_{j\mu}$; this entails that $V_{j\mu}$ is connected. Moreover, it follows from `(8.3.4)` that for $\mu$
large enough, the union of the $V_{j\mu}$ is $S_{\mu}$, since every open set in a prescheme is ind-constructible
`(1.9.6)`. The $V_{j\mu}$ are therefore the connected components of $S_{\mu}$, which completes the proof.

One will note that if the morphisms $u_{\mu \lambda}$ are immersions, they will satisfy in particular condition b) of
`(8.4.2)`.

<!-- original page 19 -->

**Corollary (8.4.3).**

<!-- label: IV.8.4.3 -->

*Suppose one of the conditions a), b) of `(8.4.2)` is satisfied, the space underlying $S$ being Noetherian; then, in
order that $S$ be irreducible, it is necessary and sufficient that there exist $\lambda$ such that $S_{\mu}$ be so for
every $\mu \geq \lambda$.*

**Proposition (8.4.4).**

<!-- label: IV.8.4.4 -->

*Suppose there exists $\alpha$ such that $S_{\alpha}$ is quasi-compact and that, for $\lambda \leq \mu$, $u_{\mu
\lambda} : S_{\mu} \to S_{\lambda}$ is dominant. Then, in order that $S$ be connected, it is necessary and sufficient
that there exist $\lambda$ such that $S_{\mu}$ be so for every $\mu \geq \lambda$.*

The condition is sufficient by virtue of `(8.4.1)`; on the other hand, one has seen `(8.3.8, (i))` that $u_{\lambda} : S
\to S_{\lambda}$ is dominant for $\lambda$ large enough, hence, if $S$ is connected, so is $S_{\lambda}$, since
$u_{\lambda}(S)$ is dense in $S_{\lambda}$ and connected.

**Corollary (8.4.5).**

<!-- label: IV.8.4.5 -->

*Let $k$ be a field, $X$ a quasi-compact $k$-prescheme. In order that $X$ be geometrically connected `(4.5.2)`, it is
necessary and sufficient that, for every finite separable extension $K$ of $k$, $X \otimes_{k} K$ be connected.*

The condition is trivially necessary. To see that it is sufficient, we must prove that if $\Omega$ is an algebraic
closure of $k$, $X \otimes_{k} \Omega$ is connected `(4.5.1)`. Now, $\Omega$ is the filtered inductive limit of the
finite sub-extensions $k'$ of $k$, and for $k \subset k' \subset k'' \subset \Omega$, the morphism $X \otimes_{k} k''
\to X \otimes_{k} k'$ is surjective. One is therefore reduced, by virtue of `(8.4.4)`, to proving that $X \otimes_{k}
k'$ is connected for every finite extension $k'$ of $k$. But if $K$ is the largest separable extension contained in
$k'$, the morphism $X \otimes_{k} k' \to X \otimes_{k} K$ is finite, surjective and radicial, hence `(2.4.5)` a
homeomorphism, and since $X \otimes_{k} K$ is connected by hypothesis, the same is true of $X \otimes_{k} k'$.

**Remarks (8.4.6).**

<!-- label: IV.8.4.6 -->

(i) The proof of `(8.4.2)` shows that the conclusion of this proposition is valid if one supposes that the space
underlying $S$ is Noetherian, that there exists $\alpha$ such that $S_{\alpha}$ is quasi-compact, and finally that the
$u_{\lambda} : S \to S_{\lambda}$ are dominant.

(ii) By contrast, the conclusion of `(8.4.2)` can fail when the $u_{\lambda}$ are not dominant for $\lambda$ large
enough, even when the $S_{\lambda}$ and $S$ are Noetherian, as the following example shows. Take for index set
$\mathbb{N}$, all the $S_{n}$ equal to `Spec(A × K) = Spec(A) ⨿ Spec(K)`, where $K$ is a field, $A$ an arbitrary
$K$-algebra, and all the morphisms $u_{n, n+1}$ equal to the same morphism corresponding to the homomorphism $(x, y)
\mapsto (j(y), y)$ of $A \times K$ into itself, where $j : K \to A$ is the canonical homomorphism. One verifies easily
that the inductive limit of this system of rings is $K$, the canonical homomorphism $u_{n}$ corresponding to the second
projection $A \times K \to K$. One sees therefore that $S = \operatorname{Spec}(K)$ is irreducible although none of the
$S_{n}$ is connected.

### 8.5. Modules of finite presentation over a projective limit of preschemes

**(8.5.1)** We continue to use the notations of `(8.2.2)`; we shall in addition restrict to the case where `S_0` is one
of the $S_{\lambda}$, to which one may always reduce.

When, in this section, we consider a family $(\mathcal{F}_{\lambda})$, where, for every $\lambda \in L$,
$\mathcal{F}_{\lambda}$ is an $\mathcal{O}_{S_{\lambda}}$-Module, it shall be understood that this family satisfies the
condition

```text
  (8.5.1.1)    ℱ_μ = u_{μλ}^*(ℱ_λ)    for λ ≤ μ.
```

We shall then set

$$ (8.5.1.2) \mathcal{F} = u^{*}_{\lambda}(\mathcal{F}_{\lambda}), $$

which is an $\mathcal{O}_{S}$-Module not depending on the index $\lambda \in L$, by virtue of hypothesis `(8.5.1.1)`.

Let now $(\mathcal{F}_{\lambda})$, $(\mathcal{G}_{\lambda})$ be two such families of
$\mathcal{O}_{S_{\lambda}}$-Modules. It is clear that the maps $f_{\lambda} \mapsto u^{*}_{\mu \lambda}(f_{\lambda})$
from $\operatorname{Hom}_{S_{\lambda}}(\mathcal{F}_{\lambda}, \mathcal{G}_{\lambda})$ to
$\operatorname{Hom}_{S_{\mu}}(\mathcal{F}_{\mu}, \mathcal{G}_{\mu})$ define an inductive system of abelian groups
$(\operatorname{Hom}_{S_{\lambda}}(\mathcal{F}_{\lambda}, \mathcal{G}_{\lambda}), u^{*}_{\mu \lambda})$, and that the
maps $f_{\lambda} \mapsto u^{*}_{\lambda}(f_{\lambda})$ form an inductive system of homomorphisms of abelian groups,
whence, by passing to the inductive limit, a canonical homomorphism of abelian groups

```text
  (8.5.1.3)    u_λ^* : lim Hom_{S_λ}(ℱ_λ, 𝒢_λ) → Hom_S(ℱ, 𝒢).
```

Let us note that when $\mathcal{F}_{\lambda} = \mathcal{O}_{S_{\lambda}}$ condition `(8.5.1.1)` is satisfied, and one
has $\mathcal{F} = \mathcal{O}_{S}$; homomorphism `(8.5.1.3)` thus gives $(0_{I}, 5.1.1)$ a canonical homomorphism of
abelian groups

```text
  (8.5.1.4)    lim Γ(S_λ, 𝒢_λ) → Γ(S, 𝒢).
```

**Theorem (8.5.2).**

<!-- label: IV.8.5.2 -->

*(i) Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated) and that, for some $\lambda \in L$,
$\mathcal{F}_{\lambda}$ is quasi-coherent and of finite type (resp. of finite presentation) and $\mathcal{G}_{\lambda}$
quasi-coherent. Then the homomorphism $u^{*}_{\lambda}$ is injective (resp. bijective).*

*(ii) Suppose `S_0` quasi-compact and quasi-separated. For every quasi-coherent $\mathcal{O}_{S}$-Module $\mathcal{F}$
of finite presentation, there exist $\lambda \in L$ and a quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Module
$\mathcal{F}_{\lambda}$ of finite presentation such that $\mathcal{F}$ is isomorphic to
$u^{*}_{\lambda}(\mathcal{F}_{\lambda})$.*

(i) One can evidently restrict to the case where $S_{0} = S_{\lambda}$ since the morphisms $u_{0\lambda} : S_{\lambda}
\to S_{0}$ are affine, hence quasi-compact and separated. Consider first the case where $S_{0} =
\operatorname{Spec}(A_{0})$ is affine. Then assertion (i) is equivalent to the

**Lemma (8.5.2.1).**

<!-- label: IV.8.5.2.1 -->

*Let `A_0` be a ring, $(A_{\lambda})_{\lambda \in L}$ an inductive system of `A_0`-algebras, $A = \lim A_{\lambda}$; let
`M_0`, `N_0` be two `A_0`-modules, and set $M_{\lambda} = M_{0} \otimes_{A_{0}} A_{\lambda}$, $N_{\lambda} = N_{0}
\otimes_{A_{0}} A_{\lambda}$, $M = M_{0} \otimes_{A_{0}} A = \lim M_{\lambda}$, $N = N_{0} \otimes_{A_{0}} A = \lim
N_{\lambda}$. If `M_0` is of finite type (resp. of finite presentation), the canonical homomorphism*

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

which, to every inductive system of homomorphisms of `A_0`-modules $\theta_{\lambda} : M_{0} \to N_{\lambda}$,
associates its inductive limit.

Now, if `M_0` is of finite type (resp. of finite presentation), one has an exact sequence $A^{m}_{0} \to M_{0} \to 0$
(resp. $A^{n}_{0} \to A^{m}_{0} \to M_{0} \to 0$); since it is clear that `(8.5.2.3)` is bijective when `M_0` is of the
form $A^{m}_{0}$, it suffices to use the left-exactness of the functor $M_{0} \mapsto \operatorname{Hom}_{A_{0}}(M_{0},
P)$ and the exactness of the functor `lim` (in the category of abelian groups) to conclude.

Let us pass to the case where `S_0` is quasi-compact, and let $(U_{i})$ be a finite cover of `S_0` by affine open sets;
for every $\lambda$, the $U_{i\lambda} = u^{-1}_{0\lambda}(U_{i})$ form an affine open cover of $S_{\lambda}$, and the
$V_{i} = u^{-1}_{0}(U_{i})$ an affine open cover of $S$. To see that $u^{*}_{\lambda}$ is injective, one must prove that
if $f_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$ is such that $f = u^{*}_{\lambda}(f_{\lambda}) = 0$,
then there exists $\mu \geq \lambda$ such that $f_{\mu} = u^{*}_{\mu \lambda}(f_{\lambda}) = 0$. By virtue of Lemma
`(8.5.2.1)`, for each $i$ there exists $\mu_{i}$ such that $f_{\mu_{i}} | U_{i\mu_{i}} = 0$ for $\mu \geq \mu_{i}$. It
therefore suffices to take $\mu$ greater than all the $\mu_{i}$.

Suppose in addition `S_0` quasi-separated and $\mathcal{F}_{\lambda}$ of finite presentation, and let $f : \mathcal{F}
\to \mathcal{G}$ be a homomorphism of $\mathcal{O}_{S}$-Modules. By virtue of Lemma `(8.5.2.1)`, for every $i$, there
exists an index $\mu_{i}$ and a homomorphism $f^{(i)}_{\mu_{i}} : \mathcal{F}_{\mu_{i}} | U_{i\mu_{i}} \to
\mathcal{G}_{\mu_{i}} | U_{i\mu_{i}}$ such that $u^{*}_{\mu_{i}}(f^{(i)}_{\mu_{i}}) = f | V_{i}$. Since $L$ is filtered,
one can in addition suppose all the $\mu_{i}$ equal to a single $\lambda$. Note now that $S_{\lambda}$ is
quasi-separated `(1.2.3)` and $\mathcal{F}_{\lambda}$ is a quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Module of finite
presentation $(0_{I}, 5.2.5)$; since, for every pair of indices $i$, $j$, $U_{ij\lambda} = U_{i\lambda} \cap
U_{j\lambda}$ is quasi-compact and one has $u^{*}_{\lambda}(f^{(i)}_{\lambda} | U_{ij\lambda}) =
u^{*}_{\lambda}(f^{(j)}_{\lambda} | U_{ij\lambda}) = f | (V_{i} \cap V_{j})$ by definition, it results from what was
seen above that there exists an index $\lambda_{ij}$ such that $u^{*}_{\lambda_{ij}\lambda}(f^{(i)}_{\lambda}) |
U_{ij\lambda_{ij}} = u^{*}_{\lambda_{ij}\lambda}(f^{(j)}_{\lambda}) | U_{ij\lambda_{ij}}$ for $\mu \geq \lambda_{ij}$;
taking $\mu$ greater than all the $\lambda_{ij}$, one sees therefore that $u^{*}_{\mu \lambda}(f^{(i)}_{\lambda})$ and
$u^{*}_{\mu \lambda}(f^{(j)}_{\lambda})$ coincide in $U_{i\mu} \cap U_{j\mu}$ for every pair $(i, j)$, and consequently
define a homomorphism $f_{\mu} : \mathcal{F}_{\mu} \to \mathcal{G}_{\mu}$ such that $f = u^{*}_{\mu}(f_{\mu})$.

Before passing to the proof of (ii), let us note the following corollaries of (i):

**Corollary (8.5.2.4).**

<!-- label: IV.8.5.2.4 -->

*Suppose `S_0` quasi-compact, $\mathcal{F}_{\lambda}$ quasi-coherent of finite type, $\mathcal{G}_{\lambda}$
quasi-coherent of finite presentation. Let $f_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$ be a
homomorphism. In order that $f = u^{*}_{\lambda}(f_{\lambda}) : \mathcal{F} \to \mathcal{G}$ be an isomorphism, it is
necessary and sufficient that there exist $\mu \geq \lambda$ such that $f_{\mu} = u^{*}_{\mu \lambda}(f_{\lambda}) :
\mathcal{F}_{\mu} \to \mathcal{G}_{\mu}$ be an isomorphism.*

One may always suppose $S_{\lambda} = S_{0}$; the question being local on `S_0`, one can in addition (`S_0` being
quasi-compact and $L$ filtered) reduce to the case where `S_0` is affine, hence quasi-separated. The condition being
trivially sufficient, it remains to show it is necessary: now, by hypothesis there is an $\mathcal{O}_{S}$-homomorphism
$g : \mathcal{G} \to \mathcal{F}$ such that $g \circ f = 1_{\mathcal{F}}$ and $f \circ g = 1_{\mathcal{G}}$. Since
$\mathcal{G}$ is of finite presentation, there exist $\nu \geq \lambda$ and a homomorphism $g_{\nu} : \mathcal{G}_{\nu}
\to \mathcal{F}_{\nu}$ such that $g = u^{*}_{\nu}(g_{\nu})$ by virtue of `(8.5.2, (i))`; one has consequently
$u^{*}_{\nu}(g_{\nu} \circ f_{\nu}) = 1_{\mathcal{F}}$

<!-- original page 22 -->

and $u^{*}_{\nu}(f_{\nu} \circ g_{\nu}) = 1_{\mathcal{G}}$; taking into account that $\mathcal{F}_{\nu}$ and
$\mathcal{G}_{\nu}$ are of finite type, one concludes by `(8.5.2, (i))` that there exists $\mu \geq \nu$ such that
$g_{\mu} \circ f_{\mu} = 1_{\mathcal{F}_{\mu}}$ and $f_{\mu} \circ g_{\mu} = 1_{\mathcal{G}_{\mu}}$, whence the
corollary.

**Corollary (8.5.2.5).**

<!-- label: IV.8.5.2.5 -->

*Suppose `S_0` quasi-compact and quasi-separated. Suppose that $\mathcal{F}_{\lambda}$, $\mathcal{G}_{\lambda}$ are
quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Modules of finite presentation. In order that $\mathcal{F}$ and $\mathcal{G}$
be isomorphic, it is necessary and sufficient that there exist $\mu \geq \lambda$ such that $\mathcal{F}_{\mu}$ and
$\mathcal{G}_{\mu}$ be isomorphic. Moreover, for every isomorphism $f : \mathcal{F} \xrightarrow{\sim} \mathcal{G}$,
there exist $\nu \geq \mu$ and an isomorphism $f_{\nu} : \mathcal{F}_{\nu} \xrightarrow{\sim} \mathcal{G}_{\nu}$ such
that $f = u^{*}_{\nu}(f_{\nu})$.*

This follows from `(8.5.2.4)` and `(8.5.2, (i))` since every homomorphism $f : \mathcal{F} \to \mathcal{G}$ is of the
form $u^{*}_{\mu}(f_{\mu})$ for some $\mu \geq \lambda$ and a homomorphism $f_{\mu} : \mathcal{F}_{\mu} \to
\mathcal{G}_{\mu}$.

(ii) Consider again first the case where $S_{0} = \operatorname{Spec}(A_{0})$ is affine. Then the assertion is
equivalent to Lemma `(5.13.7.1)`.

In the general case, starting from a finite affine open cover $(U_{i})$ of `S_0`, one deduces from `(5.13.7.1)` that for
every $i$, there exists an index $\lambda(i)$ and a quasi-coherent $\mathcal{O}_{U_{i\lambda(i)}}$-Module of finite
presentation $\mathcal{F}^{(i)}$ such that $u^{*}_{\lambda(i)}(\mathcal{F}^{(i)}) = \mathcal{F} | V_{i}$ (with the
notations of (i)). Moreover, since $L$ is filtered, one can suppose that all the $\lambda(i)$ are equal to a single
$\lambda$. Since $U_{ij\lambda} = U_{i\lambda} \cap U_{j\lambda}$ is quasi-compact and quasi-separated `(1.2.7)`, it
follows from `(8.5.2.5)` that for every pair $(i, j)$, there exists an index $\lambda_{ij} \geq \lambda$ and an
isomorphism $\theta^{(\lambda)}_{ij} : u^{*}_{\lambda_{ij}\lambda}(\mathcal{F}^{(i)} | U_{ij\lambda}) \xrightarrow{\sim}
u^{*}_{\lambda_{ij}\lambda}(\mathcal{F}^{(j)} | U_{ij\lambda})$ such that
$u^{*}_{\lambda_{ij}}(\theta^{(\lambda)}_{ij})$ is the identity automorphism of $\mathcal{F} | (V_{i} \cap V_{j})$; one
can again suppose all the $\lambda_{ij}$ equal to $\lambda$. Changing notations, one can therefore suppose that there
exists for every pair $(i, j)$ an isomorphism $\theta_{ij} : \mathcal{F}^{(i)} | U_{ij\lambda} \xrightarrow{\sim}
\mathcal{F}^{(j)} | U_{ij\lambda}$, such that $u^{*}_{\lambda}(\theta_{ij})$ is the identity automorphism of
$\mathcal{F} | (V_{i} \cap V_{j})$. Finally, for any three indices $i$, $j$, $k$, if one sets $U_{ijk\lambda} =
U_{i\lambda} \cap U_{j\lambda} \cap U_{k\lambda}$, $U_{ijk\lambda}$ is quasi-compact, and if $\theta'_{ij}$,
$\theta'_{jk}$ and $\theta'_{ik}$ denote the restrictions of $\theta_{ij}$, $\theta_{jk}$ and $\theta_{ik}$ to
$U_{ijk\lambda}$, one has $u^{*}_{\lambda}(\theta'_{ij} \circ \theta'_{jk}) = u^{*}_{\lambda}(\theta'_{ik})$. There
exists therefore, by virtue of (i), an index $\mu \geq \lambda$ such that one has $u^{*}_{\mu \lambda}(\theta'_{ik}) =
u^{*}_{\mu \lambda}(\theta'_{ij} \circ \theta'_{jk})$; thus the isomorphisms $u^{*}_{\mu \lambda}(\theta_{ij}) :
u^{*}_{\mu \lambda}(\mathcal{F}^{(i)}) | U_{ij\mu} \xrightarrow{\sim} u^{*}_{\mu \lambda}(\mathcal{F}^{(j)}) |
U_{ij\mu}$ verify the gluing condition, and consequently define on $S_{\mu}$ a quasi-coherent
$\mathcal{O}_{S_{\mu}}$-Module $\mathcal{F}_{\mu}$ of finite presentation $(0_{I}, 3.3.1)$ such that $\mathcal{F}$ is
isomorphic to $u^{*}_{\mu}(\mathcal{F}_{\mu})$.

**Scholium (8.5.3).**

<!-- label: IV.8.5.3 -->

The result of `(8.5.2)` may again be expressed by saying that if `S_0` is quasi-compact and quasi-separated, the
category of quasi-coherent $\mathcal{O}_{S}$-Modules of finite presentation is determined up to equivalence by the data
of the categories of quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Modules of finite presentation, the functors $u^{*}_{\mu
\lambda}$ between these categories, and the transition isomorphisms $u^{*}_{\nu \mu} \circ u^{*}_{\mu \lambda}
\xrightarrow{\sim} u^{*}_{\nu \lambda}$. Pictorially, one can say that giving a quasi-coherent $\mathcal{O}_{S}$-Module
of finite presentation $\mathcal{F}$ amounts "functorially" to giving an $\mathcal{O}_{S_{\lambda}}$-Module of finite
presentation $\mathcal{F}_{\lambda}$ for $\lambda$ large; and if a quasi-coherent $\mathcal{O}_{S_{\mu}}$-Module of
finite presentation $\mathcal{F}'_{\mu}$ also has $\mathcal{F}$ as inverse image, then $\mathcal{F}_{\lambda}$ and
$\mathcal{F}'_{\mu}$ have the same inverse image in a suitable $S_{\nu}$ ($\nu \geq \lambda$, $\nu \geq \mu$).

We are going to interpret various notions related to quasi-coherent $\mathcal{O}_{S}$-Modules from this point of view.

<!-- original page 23 -->

**Corollary (8.5.4).**

<!-- label: IV.8.5.4 -->

*Suppose `S_0` quasi-compact and quasi-separated; then, for every quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Module
$\mathcal{G}_{\lambda}$, the canonical homomorphism `(8.5.1.4)` is bijective.*

Indeed, it suffices to apply `(8.5.2, (i))` to the case where $\mathcal{F}_{\lambda} = \mathcal{O}_{S_{\lambda}}$, which
is of finite presentation.

**Proposition (8.5.5).**

<!-- label: IV.8.5.5 -->

*Suppose `S_0` quasi-compact, and suppose that $\mathcal{F}_{\lambda}$ is a quasi-coherent
$\mathcal{O}_{S_{\lambda}}$-Module of finite presentation. In order that $\mathcal{F}$ be locally free (resp. locally
free of rank $n$), it is necessary and sufficient that there exist $\mu \geq \lambda$ such that $\mathcal{F}_{\mu}$ be
so.*

The condition being trivially sufficient, let us prove that it is necessary. If $\mathcal{F}$ is locally free (resp.
locally free of rank $n$), there exists a finite affine open cover $(V_{i})$ of $S$ such that $\mathcal{F} | V_{i}$ is
isomorphic to $\mathcal{O}^{n_{i}}_{S} | V_{i}$ (resp. $\mathcal{O}^{n}_{S} | V_{i}$) for every $i$. By virtue of
`(8.2.11)`, there exists $\nu \geq \lambda$ and for each $i$ a quasi-compact open set $U_{i\nu}$ of $S_{\nu}$ such that
$V_{i} = u^{-1}_{\nu}(U_{i\nu})$. Since $S_{\nu}$ is quasi-compact, each $U_{i\nu}$ is a finite union of affine open
sets; one is therefore reduced to the case where `S_0` is affine and $\mathcal{F} = \mathcal{O}^{n}_{S}$; one then knows
that there exists $\mu \geq \lambda$ such that $\mathcal{F}_{\mu}$ is isomorphic to $\mathcal{O}^{n}_{S_{\mu}}$
`(8.5.2.5)`.

**Proposition (8.5.6).**

<!-- label: IV.8.5.6 -->

*Suppose `S_0` quasi-compact, and consider a sequence*

$$ \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda} \to \mathcal{H}_{\lambda} \to 0 $$

*of homomorphisms of quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Modules, where $\mathcal{F}_{\lambda}$ and
$\mathcal{G}_{\lambda}$ are of finite type and $\mathcal{H}_{\lambda}$ of finite presentation. In order that the
corresponding sequence $\mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ be exact, it is necessary and sufficient that
there exist $\mu \geq \lambda$ such that the sequence $\mathcal{F}_{\mu} \to \mathcal{G}_{\mu} \to \mathcal{H}_{\mu} \to
0$ be so (in which case the same is true of the sequence $\mathcal{F}_{\nu} \to \mathcal{G}_{\nu} \to \mathcal{H}_{\nu}
\to 0$ for $\nu \geq \mu$).*

The fact that the condition is sufficient and the last assertion result from the fact that the functor $u^{*}_{\lambda}$
(resp. $u^{*}_{\mu \lambda}$) is right exact. To prove that the condition is necessary, note that it follows from the
hypothesis and from `(8.5.2, (i))` that there exists $\nu \geq \lambda$ such that the composite $\mathcal{F}_{\nu} \to
\mathcal{G}_{\nu} \to \mathcal{H}_{\nu}$ is zero. If one sets $\mathcal{H}'_{\nu} = Coker(\mathcal{F}_{\nu} \to
\mathcal{G}_{\nu})$, one has therefore a homomorphism $f_{\nu} : \mathcal{H}'_{\nu} \to \mathcal{H}_{\nu}$; by
hypothesis, $u^{*}_{\nu}(f_{\nu})$ is an isomorphism, and it follows therefore from `(8.5.2.4)` that there exists $\mu
\geq \nu$ such that $u^{*}_{\mu \nu}(f_{\nu})$ is an isomorphism, which completes the proof.

**Corollary (8.5.7).**

<!-- label: IV.8.5.7 -->

*Suppose `S_0` quasi-compact, $\mathcal{F}_{\lambda}$ quasi-coherent, $\mathcal{G}_{\lambda}$ quasi-coherent of finite
type, and let $f_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$ be a homomorphism. In order that $f =
u^{*}_{\lambda}(f_{\lambda}) : \mathcal{F} \to \mathcal{G}$ be surjective, it is necessary and sufficient that there
exist $\mu \geq \lambda$ such that $f_{\mu} = u^{*}_{\mu \lambda}(f_{\lambda}) : \mathcal{F}_{\mu} \to
\mathcal{G}_{\mu}$ be so.*

This is the particular case of `(8.5.6)` applied to the sequence $\mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda} \to
\mathcal{H}_{\lambda} \to 0$, where $\mathcal{H}_{\lambda} = Coker(f_{\lambda})$, which is quasi-coherent and of finite
type (taking into account that one has $\mathcal{H} = Coker(f)$ and $\mathcal{H}_{\mu} = Coker(f_{\mu})$, by virtue of
the right exactness of the functors $u^{*}_{\lambda}$ and $u^{*}_{\mu \lambda}$).

**Corollary (8.5.8).**

<!-- label: IV.8.5.8 -->

*Suppose `S_0` quasi-compact and the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ flat. Then:*

<!-- original page 24 -->

*(i) Let $\mathcal{F}_{\lambda} \xrightarrow{f_{\lambda}} \mathcal{G}_{\lambda} \xrightarrow{g_{\lambda}}
\mathcal{H}_{\lambda}$ be a sequence of homomorphisms of quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Modules, such that
$Im f_{\lambda}$ and $Ker g_{\lambda}$ are of finite type. In order that the corresponding sequence $\mathcal{F} \to
\mathcal{G} \to \mathcal{H}$ be exact, it is necessary and sufficient that there exist $\mu \geq \lambda$ such that the
sequence $\mathcal{F}_{\mu} \xrightarrow{f_{\mu}} \mathcal{G}_{\mu} \xrightarrow{g_{\mu}} \mathcal{H}_{\mu}$ be exact.*

*(ii) Let $f_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$ be a homomorphism of quasi-coherent
$\mathcal{O}_{S_{\lambda}}$-Modules such that $Ker f_{\lambda}$ is of finite type. In order that $f =
u^{*}_{\lambda}(f_{\lambda}) : \mathcal{F} \to \mathcal{G}$ be injective, it is necessary and sufficient that there
exist $\mu \geq \lambda$ such that $f_{\mu} = u^{*}_{\mu \lambda}(f_{\lambda}) : \mathcal{F}_{\mu} \to
\mathcal{G}_{\mu}$ be so.*

(i) Taking into account `(8.3.8, (ii))`, note that, by flatness, `Im f` and `Ker g` (resp. $Im f_{\mu}$ and $Ker
g_{\mu}$ for $\mu \geq \lambda$) are the inverse images of $Im f_{\lambda}$ and $Ker g_{\lambda}$ $(0_{I}, 6.7.2)$.
Suppose that the sequence $\mathcal{F} \to \mathcal{G} \to \mathcal{H}$ is exact. Since $Im f_{\lambda}$ is of finite
type, there exists $\mu \geq \lambda$ such that the composite $\mathcal{F}_{\mu} \to \mathcal{G}_{\mu} \to
\mathcal{H}_{\mu}$ is zero, by virtue of `(8.5.2, (i))`. Changing notations, one can therefore already suppose that
$g_{\lambda} \circ f_{\lambda} = 0$. Then since the homomorphism $\mathcal{F} \to Ker g$ is surjective and $Ker
g_{\lambda}$ is of finite type, it follows from `(8.5.7)` that there exists $\mu \geq \lambda$ such that the
homomorphism $\mathcal{F}_{\mu} \to Ker g_{\mu}$ is surjective, which completes the proof of (i).

(ii) The assertion is the particular case of (i) applied to the sequence $0 \to \mathcal{F}_{\lambda} \to
\mathcal{G}_{\lambda}$.

**Lemma (8.5.9).**

<!-- label: IV.8.5.9 -->

*Suppose `S_0` quasi-compact, $\mathcal{F}_{\lambda}$ quasi-coherent of finite type; let $\mathcal{G}'_{\lambda}$ and
$\mathcal{G}''_{\lambda}$ be two quasi-coherent quotients of $\mathcal{F}_{\lambda}$, $\mathcal{G}'_{\lambda}$ being
moreover supposed of finite presentation. In order that $\mathcal{G}''$ be a quotient of $\mathcal{G}'$, it is necessary
and sufficient that there exist $\mu \geq \lambda$ such that $\mathcal{G}''_{\mu}$ be a quotient of
$\mathcal{G}'_{\mu}$.*

By hypothesis, there are two surjective homomorphisms $p'_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}'_{\lambda}$,
$p''_{\lambda} : \mathcal{F}_{\lambda} \to \mathcal{G}''_{\lambda}$; by virtue of the right exactness of
$u^{*}_{\lambda}$ and $u^{*}_{\mu \lambda}$, $p' = u^{*}_{\lambda}(p'_{\lambda})$, $p'' =
u^{*}_{\lambda}(p''_{\lambda})$, $p'_{\mu} = u^{*}_{\mu \lambda}(p'_{\lambda})$, $p''_{\mu} = u^{*}_{\mu
\lambda}(p''_{\lambda})$ are also surjective; moreover, if there exists a homomorphism $f : \mathcal{G}' \to
\mathcal{G}''$ (resp. $f_{\mu} : \mathcal{G}'_{\mu} \to \mathcal{G}''_{\mu}$) such that $p'' = f \circ p'$ (resp.
$p''_{\mu} = f_{\mu} \circ p'_{\mu}$), this homomorphism is necessarily unique, which shows that the question is local
on $S_{\lambda}$, and that one can therefore (`S_0` being quasi-compact and $L$ filtered) suppose $S_{\lambda}$ affine,
hence quasi-separated. It is clear that the condition of the statement is sufficient. Conversely, since
$\mathcal{G}'_{\lambda}$ is of finite presentation, $S_{\lambda}$ quasi-compact and quasi-separated, it follows from
`(8.5.2, (i))` that if there exists a homomorphism $f : \mathcal{G}' \to \mathcal{G}''$ such that $p'' = f \circ p'$,
there exist $\mu \geq \lambda$ and a homomorphism $f_{\mu} : \mathcal{G}'_{\mu} \to \mathcal{G}''_{\mu}$ such that $f =
u^{*}_{\mu}(f_{\mu})$ and $p''_{\mu} = f_{\mu} \circ p'_{\mu}$, whence the lemma.

**(8.5.10)** In what follows in this number, for every quasi-coherent Module $\mathcal{F}$ on a prescheme, let us denote
by $\mathcal{Q}(\mathcal{F})$ the set of quotient Modules of $\mathcal{F}$ that are of finite presentation. If
$\mathcal{F}_{\lambda}$ is quasi-coherent and $\mathcal{G}_{\lambda} \in \mathcal{Q}(\mathcal{F}_{\lambda})$, it follows
from the fact that $u^{*}_{\mu \lambda}$ and $u^{*}_{\lambda}$ are right exact, that one has $\mathcal{G}_{\mu} \in
\mathcal{Q}(\mathcal{F}_{\mu})$ for $\mu \geq \lambda$ and $\mathcal{G} \in \mathcal{Q}(\mathcal{F})$; it is clear that
$(\mathcal{Q}(\mathcal{F}_{\lambda}), u^{*}_{\mu \lambda})$ is an inductive system of sets, and that the
$u^{*}_{\lambda} : \mathcal{Q}(\mathcal{F}_{\lambda}) \to \mathcal{Q}(\mathcal{F})$ form an inductive system of maps,
whence, by passage to the inductive limit, a canonical map

```text
  (8.5.10.1)    u_𝒬 : lim 𝒬(ℱ_λ) → 𝒬(ℱ).
```

Moreover, if $(\mathcal{F}'_{\lambda})$ is a second family of quasi-coherent $\mathcal{O}_{S_{\lambda}}$-Modules and if,
for every $\lambda$, $\mathcal{F}'_{\lambda}$ is a quotient of $\mathcal{F}_{\lambda}$, then $\mathcal{F}'$ is a
quotient of $\mathcal{F}$ and one has a commutative diagram

<!-- original page 25 -->

```text
  (8.5.10.2)    lim 𝒬(ℱ_λ)  ──→  𝒬(ℱ)
                    │              │
                    ↓              ↓
                lim 𝒬(ℱ'_λ)  ──→  𝒬(ℱ').
```

**Proposition (8.5.11).**

<!-- label: IV.8.5.11 -->

*Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated). Suppose $\mathcal{F}_{\lambda}$ quasi-coherent
of finite type (resp. of finite presentation) for every $\lambda$; then the canonical map `(8.5.10.1)` is injective
(resp. bijective).*

The first assertion results from the more precise lemma `(8.5.9)`. To prove the second, consider a quotient
$\mathcal{O}_{S}$-Module $\mathcal{G}$ of $\mathcal{F}$ that is of finite presentation. It follows from `(8.5.2, (ii))`
that there exist $\lambda' \in L$ and a quasi-coherent $\mathcal{O}_{S_{\lambda'}}$-Module $\mathcal{G}_{\lambda'}$ of
finite presentation such that $\mathcal{G} = u^{*}_{\lambda'}(\mathcal{G}_{\lambda'})$; since $L$ is filtered, one can
suppose $\lambda' = \lambda$ (replacing $\lambda$ and $\lambda'$ by an index majoring them). Consider then the canonical
homomorphism $p : \mathcal{F} \to \mathcal{G}$; it follows from `(8.5.2, (i))` that there exist $\mu \geq \lambda$ and a
homomorphism $p_{\mu} : \mathcal{F}_{\mu} \to \mathcal{G}_{\mu}$ such that $p = u^{*}_{\mu}(p_{\mu})$. Moreover, by
virtue of `(8.5.7)`, one can suppose $\mu$ chosen large enough so that $p_{\mu}$ is surjective, which finishes the
proof.

### 8.6. Sub-preschemes of finite presentation of a projective limit of preschemes

**(8.6.1)** Given a prescheme $Y$, let us denote in this number by $\mathfrak{Spr}(Y)$ the ordered set `(I, 4.1.10)` of
sub-preschemes of $Y$ that are of finite presentation over $Y$ `(1.6.1)`, by $\mathfrak{Spr}_{o}(Y)$ (resp.
$\mathfrak{Spr}_{f}(Y)$) the part of $\mathfrak{Spr}(Y)$ formed of sub-preschemes induced on open sets (resp. closed
sub-preschemes) of $Y$, of finite presentation over $Y$; this amounts to saying that a sub-prescheme $Z$ of $Y$ belongs
to $\mathfrak{Spr}_{o}(Y)$ (resp. $\mathfrak{Spr}_{f}(Y)$) precisely when it is induced on an open set and the
underlying space $Z$ is retrocompact in $Y$ (resp. when it is closed and the Ideal $\mathcal{J}$ of $\mathcal{O}_{Y}$
that defines it is of finite type, which also means that $j_{*}(\mathcal{O}_{Z}) \in \mathcal{Q}(\mathcal{O}_{Y})$ if
$j : Z \to Y$ is the canonical injection) `(1.6.1 and 1.4.5)`.

**(8.6.2)** We continue to use the notations of `(8.2.2)` and suppose that `S_0` is one of the $S_{\lambda}$. Let
$Y_{\lambda}$ be a sub-prescheme of $S_{\lambda}$; then $Y_{\mu} = u^{-1}_{\mu \lambda}(Y_{\lambda})$ (resp. $Y =
u^{-1}_{\lambda}(Y_{\lambda})$) is a sub-prescheme of $S_{\mu}$ for $\mu \geq \lambda$ (resp. of $S$); it is induced on
an open set (resp. it is closed) if $Y_{\lambda}$ is `(I, 4.3.2)` and of finite presentation over $S_{\mu}$ (resp. $S$)
if $Y_{\lambda}$ is of finite presentation over $S_{\lambda}$ `(1.6.2, (iii))`. Consequently
$(\mathfrak{Spr}(S_{\lambda}), u^{-1}_{\mu \lambda})$ (resp. $(\mathfrak{Spr}_{o}(S_{\lambda}), u^{-1}_{\mu \lambda})$,
$(\mathfrak{Spr}_{f}(S_{\lambda}), u^{-1}_{\mu \lambda})$) is an inductive system, and the maps $u^{-1}_{\lambda} :
\mathfrak{Spr}(S_{\lambda}) \to \mathfrak{Spr}(S)$ (resp. $\mathfrak{Spr}_{o}(S_{\lambda}) \to \mathfrak{Spr}_{o}(S)$,
$\mathfrak{Spr}_{f}(S_{\lambda}) \to \mathfrak{Spr}_{f}(S)$) form an inductive system of maps; whence, by passage to the
inductive limit, canonical maps

$$ (8.6.2.1) \lim \mathfrak{Spr}(S_{\lambda}) \to \mathfrak{Spr}(S) (8.6.2.2) \lim \mathfrak{Spr}_{o}(S_{\lambda}) \to
\mathfrak{Spr}_{o}(S) (8.6.2.3) \lim \mathfrak{Spr}_{f}(S_{\lambda}) \to \mathfrak{Spr}_{f}(S). $$

<!-- original page 26 -->

Let us recall `(I, 4.1.10)` that $\mathfrak{Spr}(X)$, for every prescheme $X$, is a set ordered by the relation "$Z$ is
a sub-prescheme of the sub-prescheme $Y$", which is written $Z \leq Y$. The maps $u^{-1}_{\mu \lambda}$ and
$u^{-1}_{\lambda}$ are increasing for the corresponding order relations in $\mathfrak{Spr}(S_{\lambda})$,
$\mathfrak{Spr}(S_{\mu})$, $\mathfrak{Spr}(S)$. Moreover, one defines an order relation in the set $\lim
\mathfrak{Spr}(S_{\lambda})$ by writing that $\eta \leq \eta'$ for two elements of this set when there exist a $\lambda$
and two elements $Y_{\lambda}$, $Y'_{\lambda}$ of $\mathfrak{Spr}(S_{\lambda})$, of which $\eta$ and $\eta'$ are the
canonical images, and which are such that $Y_{\lambda} \leq Y'_{\lambda}$; one verifies easily that this does not depend
on the representatives $Y_{\lambda}$, $Y'_{\lambda}$ considered, and that one thus has indeed an order relation. That
being so, the fact that the $u^{-1}_{\mu \lambda}$ are increasing entails at once that the canonical map `(8.6.2.1)` is
increasing; the same is evidently true of `(8.6.2.2)` and `(8.6.2.3)`.

**Proposition (8.6.3).**

<!-- label: IV.8.6.3 -->

*Suppose `S_0` quasi-compact (resp. quasi-compact and quasi-separated). Then the maps `(8.6.2.1)`, `(8.6.2.2)`,
`(8.6.2.3)` are injective (resp. bijective).*

Taking into account the remarks of `(8.6.1)`, the assertions relative to `(8.6.2.3)` follow from `(8.5.11)` applied to
$\mathcal{F}_{\lambda} = \mathcal{O}_{S_{\lambda}}$; similarly, the assertions relative to `(8.6.2.2)` are particular
cases of `(8.3.5)` and `(8.3.11)`, taking into account that the $S_{\lambda}$ and $S$ are quasi-compact. It remains to
consider the map `(8.6.2.1)`. Let us first prove that it is surjective when `S_0` is quasi-compact and quasi-separated.
Let $Z$ be a sub-prescheme of $S$, of finite presentation over $S$; since $S$ is quasi-compact, so is $Z$, hence there
exists a quasi-compact open set $U$ of $S$ such that $Z$ is a closed sub-prescheme of $U$, of finite presentation over
$U$. There exist then an index $\lambda$ and a quasi-compact open set $U_{\lambda}$ of $S_{\lambda}$ such that $U =
u^{-1}_{\lambda}(U_{\lambda})$ `(8.2.11)`; since $S_{\lambda}$ is quasi-separated, so is $U_{\lambda}$ `(1.2.7)`, and
consequently one can restrict to the case where $U = S$; but in this case, one is reduced to the fact that `(8.6.2.3)`
is surjective.

Finally, to see that `(8.6.2.1)` is injective when `S_0` is quasi-compact, it will suffice to prove the following more
precise result:

**Corollary (8.6.3.1).**

<!-- label: IV.8.6.3.1 -->

*Suppose `S_0` quasi-compact and let $Z_{\lambda}$, $Z'_{\lambda}$ be two sub-preschemes of $S_{\lambda}$, of finite
presentation over $S_{\lambda}$. In order that $Z' = u^{-1}_{\lambda}(Z_{\lambda})$ be majorized by $Z'' =
u^{-1}_{\lambda}(Z'_{\lambda})$ `(I, 4.1.10)`, it is necessary and sufficient that there exist $\mu \geq \lambda$ such
that $Z_{\mu} = u^{-1}_{\mu \lambda}(Z_{\lambda})$ be majorized by $Z'_{\mu} = u^{-1}_{\mu \lambda}(Z'_{\lambda})$.*

It is trivial that the condition is sufficient. To see that it is necessary, note first that the underlying sets
$Z_{\lambda}$ and $Z'_{\lambda}$ are locally constructible in $S_{\lambda}$ by hypothesis `(1.8.4)`, hence the
hypothesis entails the existence of $\nu \geq \lambda$ such that $Z_{\nu} \subset Z'_{\nu}$ `(8.3.5)`; replacing
$\lambda$ by $\nu$, one can therefore already suppose that one has $Z_{\lambda} \subset Z'_{\lambda}$. Moreover, by
hypothesis `(1.6.1)`, the subspaces $Z_{\lambda}$ and $Z'_{\lambda}$ of $S_{\lambda}$ are quasi-compact; for every point
$x \in Z_{\lambda}$, there is a quasi-compact open neighbourhood $V(x)$ in $S_{\lambda}$ such that $V(x) \cap
Z_{\lambda}$ and $V(x) \cap Z'_{\lambda}$ are closed in $V(x)$. By covering $S_{\lambda}$ by a finite number of
neighbourhoods $V(x_{i})$ one sees therefore that there is a quasi-compact open set $U_{\lambda}$ of $S_{\lambda}$
containing $Z_{\lambda}$ and such that $Z_{\lambda}$ and $Z'_{\lambda} \cap U_{\lambda}$ are closed in $U_{\lambda}$. If
one denotes by $Y_{\lambda}$ the sub-prescheme induced by $Z'_{\lambda}$ on $U_{\lambda} \cap Z'_{\lambda}$, it is clear
that with the usual notations, $Y_{\mu}$ (resp. $Y$) is induced by $Z'_{\mu}$ on $U_{\mu} \cap Z'_{\mu}$ for $\mu \geq
\lambda$ (resp. by `Z''` on $U \cap Z''$); moreover $Z'$ is majorized by $Y$ `(I, 4.4.1)`, and since it suffices to
prove that $Z_{\mu}$ is majorized by $Y_{\mu}$ for $\mu$

<!-- original page 27 -->

large enough, one sees finally that one is reduced (replacing $S_{\lambda}$ by $U_{\lambda}$) to the case where
$Z_{\lambda}$ and $Z'_{\lambda}$ are closed sub-preschemes of $S_{\lambda}$. But then this has already been proved since
`(8.6.2.3)` is increasing and injective.

**Corollary (8.6.4).**

<!-- label: IV.8.6.4 -->

*Suppose `S_0` quasi-compact, and let $Z_{\lambda}$ be a sub-prescheme of $S_{\lambda}$, of finite presentation over
$S_{\lambda}$. In order that $Z = u^{-1}_{\lambda}(Z_{\lambda})$ be a sub-prescheme induced on an open set (resp. a
closed sub-prescheme) of $S$, it is necessary and sufficient that there exist $\mu \geq \lambda$ such that $Z_{\mu} =
u^{-1}_{\mu \lambda}(Z_{\lambda})$ be induced on an open set (resp. a closed sub-prescheme) of $S_{\mu}$.*

Let $(U^{(i)}_{\lambda})$ be a finite affine open cover of $S_{\lambda}$, and set $U^{(i)}_{\mu} = u^{-1}_{\mu
\lambda}(U^{(i)}_{\lambda})$ for $\mu \geq \lambda$ and $U^{(i)} = u^{-1}_{\lambda}(U^{(i)}_{\lambda})$. If $Z$ is open
(resp. closed) in $S$, $Z \cap U^{(i)}$ is so in $U^{(i)}$, and conversely if each of the $Z_{\mu} \cap U^{(i)}_{\mu}$
is open (resp. closed) in $U^{(i)}_{\mu}$, $Z_{\mu}$ is so in $S_{\mu}$. Since $L$ is filtered, it suffices to prove the
corollary when $S_{\lambda}$ is affine, hence quasi-separated. But then the result follows from the fact that the maps
`(8.6.2.1)`, `(8.6.2.2)` and `(8.6.2.3)` are bijective.

### 8.7. Criteria for a projective limit of preschemes to be a reduced (resp. integral) prescheme

We continue to use the hypotheses and notations of `(8.2.2)` and suppose always that `S_0` is one of the $S_{\lambda}$.

**Proposition (8.7.1).**

<!-- label: IV.8.7.1 -->

*Suppose that $S$ is non-reduced. Then there exists $\lambda_{0}$ such that for $\lambda \geq \lambda_{0}$,
$S_{\lambda}$ is non-reduced.*

The question being local on `S_0`, one can suppose $S_{0} = \operatorname{Spec}(A_{0})$ affine, whence $S =
\operatorname{Spec}(A)$, where $A = \lim A_{\lambda}$ is the inductive limit of an inductive system of `A_0`-algebras
$(A_{\lambda})$. One knows then `(5.13.2)` that the nilradical of $A$ is the inductive limit of those of the
$A_{\lambda}$; if it is not zero, one of the $A_{\lambda}$ thus contains a nilpotent element $a_{\lambda} \neq 0$ whose
image in $A$ is a nilpotent and non-zero element, and the image of $a_{\lambda}$ in the $A_{\mu}$ for $\mu \geq \lambda$
is consequently a nilpotent and non-zero element.

**Proposition (8.7.2).**

<!-- label: IV.8.7.2 -->

*Suppose one of the following hypotheses is satisfied:*

*a) `S_0` is quasi-compact, the nilradical $\mathcal{N}_{0}$ of $\mathcal{O}_{S_{0}}$ is an Ideal of finite type (which
will be the case for example when `S_0` is Noetherian), and the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$
are open immersions.*

*b) The morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are faithfully flat.*

*Under these conditions, in order that $S$ be reduced, it is necessary and sufficient that there exist $\lambda_{0}$
such that $S_{\lambda}$ be reduced for $\lambda \geq \lambda_{0}$.*

*Moreover, in case b), if $S$ is reduced, all the $S_{\lambda}$ are.*

The last assertion follows from the fact that the morphism $S \to S_{\lambda}$ is then faithfully flat for every
$\lambda$ `(8.3.8)` and from `(2.1.13)`. On the other hand, `(8.7.1)` proves that the condition of the statement is
sufficient (without hypothesis on `S_0` nor on the $u_{\mu \lambda}$). It remains therefore to see that the condition is
necessary in hypothesis a); then `(8.2.13)`, the space underlying $S$ is identified with the intersection of the spaces
underlying the $S_{\lambda}$ (the $S_{\lambda}$ being identified with sub-preschemes induced on open sets of `S_0`), and
the structure sheaf $\mathcal{O}_{S}$ is identified with the

<!-- original page 28 -->

sheaf induced on $S$ by all the $\mathcal{O}_{S_{\lambda}}$; in particular for every $s \in S$, the local ring
$\mathcal{O}_{s}$ is the same for $S$ and for all the $S_{\lambda}$. If $\mathcal{N}_{\lambda}$ is the Nilradical of
$\mathcal{O}_{S_{\lambda}}$, the Nilradical $\mathcal{N}$ of $\mathcal{O}_{S}$ has therefore at each point of $S$ the
same fibre $\mathcal{N}_{s}$ (nilradical of $\mathcal{O}_{s}$) as $u^{*}_{\lambda}(\mathcal{N}_{\lambda})$ (induced on
$S$ by $\mathcal{N}_{\lambda}$). The hypothesis that $S$ is reduced thus entails $u^{*}_{\lambda}(\mathcal{N}_{\lambda})
= 0$; since $\mathcal{N}_{0}$ is supposed of finite type, the same is true of $\mathcal{N}_{\lambda}$, and the
conclusion therefore follows from `(8.5.7)`.

**Corollary (8.7.3).**

<!-- label: IV.8.7.3 -->

*Suppose one of the following hypotheses is satisfied:*

*a) `S_0` is a Noetherian prescheme and the morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are open immersions.*

*b) The morphisms $u_{\mu \lambda} : S_{\mu} \to S_{\lambda}$ are faithfully flat.*

*Then, in order that $S$ be integral, it is necessary and sufficient that there exist $\lambda_{0}$ such that
$S_{\lambda}$ be integral for $\lambda \geq \lambda_{0}$.*

To say that a prescheme is integral means that it is at once reduced and irreducible; the corollary therefore follows
from `(8.7.2)` and `(8.4.3)`.

**Remark (8.7.4).**

<!-- label: IV.8.7.4 -->

If one makes no hypothesis on the $u_{\mu \lambda}$, it may happen that $S$ is integral although all the $S_{\lambda}$
are non-reduced and non-connected, as the example `(8.4.6)` shows, where one takes the ring $A$ non-reduced.

### 8.8. Preschemes of finite presentation over a projective limit of preschemes

**(8.8.1)** Continuing to use the notations and hypotheses of `(8.2.2)`, we shall assume given in this section two
$S_{\alpha}$-preschemes $X_{\alpha}$, $Y_{\alpha}$, which defines `(8.2.5)` two projective systems of preschemes
$(X_{\lambda}, v_{\mu \lambda})$ and $(Y_{\lambda}, w_{\mu \lambda})$ by setting $X_{\lambda} = X_{\alpha}
\times_{S_{\alpha}} S_{\lambda}$, $Y_{\lambda} = Y_{\alpha} \times_{S_{\alpha}} S_{\lambda}$, $v_{\mu \lambda} =
1_{X_{\alpha}} \times u_{\mu \lambda}$, $w_{\mu \lambda} = 1_{Y_{\alpha}} \times u_{\mu \lambda}$ (for $\alpha \leq
\lambda \leq \mu$), whose projective limits are respectively $X = X_{\alpha} \times_{S_{\alpha}} S$, $Y = Y_{\alpha}
\times_{S_{\alpha}} S$, the canonical morphisms $v_{\lambda} : X \to X_{\lambda}$ and $w_{\lambda} : Y \to Y_{\lambda}$
being respectively equal to $1_{X_{\alpha}} \times u_{\lambda}$ and $1_{Y_{\alpha}} \times u_{\lambda}$. For $\alpha
\leq \lambda \leq \mu$, one has a canonical map $e_{\mu \lambda} : \operatorname{Hom}_{S_{\lambda}}(X_{\lambda},
Y_{\lambda}) \to \operatorname{Hom}_{S_{\mu}}(X_{\mu}, Y_{\mu})$, which to every $S_{\lambda}$-morphism $f_{\lambda} :
X_{\lambda} \to Y_{\lambda}$ associates $f_{\mu} = f_{\lambda} \times 1_{S_{\mu}} : X_{\lambda} \times_{S_{\lambda}}
S_{\mu} \to Y_{\lambda} \times_{S_{\lambda}} S_{\mu}$, and it is clear that
$(\operatorname{Hom}_{S_{\lambda}}(X_{\lambda}, Y_{\lambda}), e_{\mu \lambda})$ is an inductive system of sets.
Similarly, one has a canonical map $e_{\lambda} : \operatorname{Hom}_{S_{\lambda}}(X_{\lambda}, Y_{\lambda}) \to
\operatorname{Hom}_{S}(X, Y)$ which to $f_{\lambda}$ associates $f = f_{\lambda} \times 1_{S} : X_{\lambda}
\times_{S_{\lambda}} S \to Y_{\lambda} \times_{S_{\lambda}} S$ and $(e_{\lambda})$ is an inductive system of maps;
whence, by passage to the inductive limit, a canonical map, functorial in $S_{\alpha}$, $X_{\alpha}$ and $Y_{\alpha}$:

```text
  (8.8.1.1)    e : lim Hom_{S_λ}(X_λ, Y_λ) → Hom_S(X, Y).
```

**Theorem (8.8.2).**

<!-- label: IV.8.8.2 -->

*(i) Suppose $X_{\alpha}$ quasi-compact (resp. quasi-compact and quasi-separated), and $Y_{\alpha}$ locally of finite
type (resp. locally of finite presentation) over $S_{\alpha}$. Then the map `(8.8.1.1)` is injective (resp. bijective).*

*(ii) Suppose `S_0` quasi-compact and quasi-separated. For every prescheme $X$ of finite presentation over $S$, there
exist $\lambda \in L$, a prescheme $X_{\lambda}$ of finite presentation over $S_{\lambda}$, and an $S$-isomorphism
$X_{\lambda} \times_{S_{\lambda}} S \xrightarrow{\sim} X$.*

<!-- original page 29 -->

(i) Consider first the case where $S_{0} = \operatorname{Spec}(A_{0})$, $X_{\alpha} = \operatorname{Spec}(B_{\alpha})$
and $Y_{\alpha} = \operatorname{Spec}(C_{\alpha})$ are affine; then the $S_{\lambda} = \operatorname{Spec}(A_{\lambda})$
and $S = \operatorname{Spec}(A)$ are also affine, with $A = \lim A_{\lambda}$, and the assertions of (i) are equivalent
to the

**Lemma (8.8.2.1).**

<!-- label: IV.8.8.2.1 -->

*Let `A_0` be a ring, $(A_{\lambda})_{\lambda \in L}$ an inductive system of `A_0`-algebras, $A = \lim A_{\lambda}$; let
$B_{\alpha}$ be an $A_{\alpha}$-algebra, $C_{\alpha}$ an $A_{\alpha}$-algebra of finite type (resp. of finite
presentation). Then the canonical homomorphism*

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

*Let $E$ be a ring, $G$ an $E$-algebra of finite type (resp. of finite presentation), $(F_{\lambda})$ an inductive
system of $E$-algebras. Then the canonical homomorphism*

```text
  lim Hom_{E-alg.}(G, F_λ) → Hom_{E-alg.}(G, lim F_λ)
```

*which, to every inductive system of homomorphisms $\theta_{\lambda} : G \to F_{\lambda}$ of $E$-algebras, associates
its inductive limit, is injective (resp. bijective).*

Suppose first the $E$-algebra $G$ of finite type, and let $(t_{i})_{1 \leq i \leq n}$ be a system of generators of this
$E$-algebra; let us show that if $(\theta_{\lambda})$, $(\theta'_{\lambda})$ are two inductive systems of homomorphisms
$G \to F_{\lambda}$ such that $\lim \theta_{\lambda} = \lim \theta'_{\lambda}$, there exists $\mu \geq \lambda$ such
that $\theta_{\mu} = \theta'_{\mu}$. Indeed, if $\phi_{\mu \lambda} : F_{\lambda} \to F_{\mu}$ and $\phi_{\lambda} :
F_{\lambda} \to F = \lim F_{\lambda}$ are the canonical homomorphisms of the inductive system $(F_{\lambda})$, by
hypothesis, for each index $i$, there exists an index $\lambda_{i}$ such that
$\phi_{\lambda_{i}}(\theta_{\lambda}(t_{i})) = \phi_{\lambda_{i}}(\theta'_{\lambda}(t_{i}))$, and one can suppose all
the $\lambda_{i}$ equal to a single $\lambda$; it follows likewise the existence of $\mu \geq \lambda$ such that
$\phi_{\mu \lambda}(\theta_{\lambda}(t_{i})) = \phi_{\mu \lambda}(\theta'_{\lambda}(t_{i}))$ for $1 \leq i \leq n$, that
is, $\theta_{\mu}(t_{i}) = \theta'_{\mu}(t_{i})$ for $1 \leq i \leq n$, whence $\theta_{\mu} = \theta'_{\mu}$.

Suppose secondly $G$ of finite presentation, so that one has $G = E[T_{1}, \cdots, T_{n}]/\mathfrak{J}$, where
$\mathfrak{J}$ is an ideal of finite type, $t_{i}$ being the class of $T_{i}$ mod. $\mathfrak{J}$. Let $(P_{j})_{1 \leq
j \leq m}$ be a system of generators of $\mathfrak{J}$. Suppose given a homomorphism of $E$-algebras $\theta : G \to F$;
set $b_{i} = \theta(t_{i})$; by definition, one has therefore $P_{j}(b_{1}, b_{2}, \cdots, b_{n}) = \theta(P_{j}(t_{1},
\cdots, t_{n})) = 0$ for $1 \leq j \leq m$. Now, there exist $\lambda$ and elements $a_{1}, \cdots, a_{n}$ in
$F_{\lambda}$ such that $b_{i} = \phi_{\lambda}(a_{i})$ for $1 \leq i \leq n$; one has therefore
$\phi_{\lambda}(P_{j}(a_{1}, \cdots, a_{n})) = P_{j}(b_{1}, \cdots, b_{n}) = 0$, and consequently there exists $\mu \geq
\lambda$ such that $\phi_{\mu \lambda}(P_{j}(a_{1}, \cdots, a_{n})) = P_{j}(\phi_{\mu \lambda}(a_{1}), \cdots, \phi_{\mu
\lambda}(a_{n})) = 0$ for $1 \leq j \leq m$; one concludes that there exists a homomorphism of $E$-algebras
$\theta_{\mu} : G \to F_{\mu}$ such that $\theta_{\mu}(t_{i}) = \phi_{\mu \lambda}(a_{i})$

<!-- original page 30 -->

for $1 \leq i \leq n$; one deduces for every $\nu \geq \mu$ a homomorphism of $E$-algebras $\theta_{\nu} = \phi_{\nu
\mu} \circ \theta_{\mu}$ from $G$ to $F_{\nu}$, and it is clear that $\theta$ is the inductive limit of this inductive
system of homomorphisms, which finishes proving the lemma.

Let us now pass to the case where $X_{\alpha}$ is quasi-compact and $Y_{\alpha}$ locally of finite type over
$S_{\alpha}$. Set $Z_{\alpha} = X_{\alpha} \times_{S_{\alpha}} Y_{\alpha}$ and introduce the corresponding projective
system of $Z_{\lambda} = Z_{\alpha} \times_{S_{\alpha}} S_{\lambda} = X_{\lambda} \times_{S_{\lambda}} Y_{\lambda}$ and
its limit $Z = Z_{\alpha} \times_{S_{\alpha}} S = X \times_{S} Y$; the canonical bijections `(I, 3.3.14)` give
commutative diagrams

```text
  Hom_{S_λ}(X_λ, Y_λ)  ─────→  Hom_S(X, Y)
        │                          │
        ↓                          ↓
  Hom_{X_λ}(X_λ, Z_λ)  ─────→  Hom_X(X, Z)
```

and consequently one is reduced to proving that `(8.8.1.1)` is injective in the particular case where $S_{\alpha} =
X_{\alpha}$ (taking into account `(1.3.4)`). Moreover, since $X_{\alpha}$ is quasi-compact, hence a finite union of
affine open sets, one can suppose $X_{\alpha}$ affine ($L$ being filtered). Suppose then given two
$X_{\alpha}$-morphisms $f'_{\alpha} : X_{\alpha} \to Y_{\alpha}$, $f''_{\alpha} : X_{\alpha} \to Y_{\alpha}$ such that
$f'$ and `f''` are equal $X$-morphisms from $X$ to $Y$; one must prove that $f'_{\mu} = f''_{\mu}$ for $\mu \geq \alpha$
large enough. Since $X_{\alpha}$ is quasi-compact, so is $f'_{\alpha}(X_{\alpha}) \cup f''_{\alpha}(X_{\alpha})$, and
since $Y_{\alpha}$ is locally of finite type over $X_{\alpha}$, $f'_{\alpha}(X_{\alpha}) \cup f''_{\alpha}(X_{\alpha})$
is contained in a finite union of affine open sets $V_{i\alpha}$ of $Y_{\alpha}$, of finite type over $X_{\alpha}$. Set
$U'_{i\alpha} = f'^{-1}_{\alpha}(V_{i\alpha})$, $U''_{i\alpha} = f''^{-1}_{\alpha}(V_{i\alpha})$, $U_{i\alpha} =
U'_{i\alpha} \cap U''_{i\alpha}$, $U_{\alpha} = \bigcup U_{i\alpha}$. The hypothesis $f' = f''$ entails
$v^{-1}_{\alpha}(U'_{i\alpha}) = v^{-1}_{\alpha}(U''_{i\alpha})$, these two sets being respectively equal to
$f'^{-1}(w^{-1}_{\alpha}(V_{i\alpha}))$ and $f''^{-1}(w^{-1}_{\alpha}(V_{i\alpha}))$. Since the $V_{i\alpha}$ cover
$Y_{\alpha}$, one has $v^{-1}_{\alpha}(U_{\alpha}) = f'^{-1}(Y) = X$. Since $X_{\alpha}$ is quasi-compact and every open
part of $X_{\alpha}$ is ind-constructible, it follows from `(8.3.4)` that there is an index $\lambda \geq \alpha$ such
that the $U_{i\lambda} = v^{-1}_{\lambda \alpha}(U_{i\alpha})$ form a cover of $X_{\lambda}$. Replacing $\alpha$ by
$\lambda$, one can therefore suppose that the $U_{i\alpha}$ cover $X_{\alpha}$; this entails that for every $x \in
X_{\alpha}$, there is an affine open neighbourhood $W(x)$ contained in one of the $U_{i\alpha}$, in other words such
that the restrictions of $f'_{\alpha}$ and $f''_{\alpha}$ to $W(x)$ send $W(x)$ into a single affine open set
$V_{i\alpha}$. Since $X_{\alpha}$ is quasi-compact, it is covered by a finite number of affine open sets $W(x_{k})$; by
virtue of Lemma `(8.8.2.1)` and the fact that $L$ is filtered, there exists $\lambda \geq \alpha$ such that the
restrictions of $f'_{\lambda}$ and $f''_{\lambda}$ to each of the open sets $v^{-1}_{\lambda \alpha}(W(x_{k}))$ are
equal, whence $f'_{\lambda} = f''_{\lambda}$.

Suppose now $X_{\alpha}$ quasi-compact and quasi-separated and $Y_{\alpha}$ locally of finite presentation over
$S_{\alpha}$, and let us prove that `(8.8.1.1)` is surjective. Suppose therefore given an $S$-morphism $f : X \to Y$.
Since $X$ is quasi-compact, so is $f(X)$, and consequently there is a quasi-compact open set $Y'$ in $Y$ that contains
$f(X)$; there exists consequently $\lambda \geq \alpha$ and a quasi-compact open set $Y'_{\lambda}$ in $Y_{\lambda}$
such that $Y' = w^{-1}_{\lambda}(Y'_{\lambda})$ `(8.2.11)`.

<!-- original page 31 -->

Replacing if need be $\alpha$ by $\lambda$ and $Y_{\alpha}$ by $Y'_{\lambda}$, one can therefore restrict to the case
where $Y_{\alpha}$ is quasi-compact, so also $Y$ and the $Y_{\lambda}$. Since $Y$ is quasi-compact, it is a finite union
of affine open sets $V_{i}$, and consequently $X$ is the union of the open sets $f^{-1}(V_{i})$. Since every point of
$X$ has a quasi-compact open neighbourhood contained in one of the $f^{-1}(V_{i})$ and $X$ is quasi-compact, one can,
taking into account `(8.2.11)` and replacing if need be $\alpha$ by an index $\lambda \geq \alpha$, suppose that $Y$ is
a finite union of open sets $V_{i} = w^{-1}_{\alpha}(V_{i\alpha})$, where the $V_{i\alpha}$ are affine open sets of
$Y_{\alpha}$; consequently $X$ is the union of the open sets $f^{-1}(V_{i})$. Since every point of $X$ has a
quasi-compact open neighbourhood contained in one of the $f^{-1}(V_{i})$ and $X$ is quasi-compact, one can cover $X$ by
a finite number of such neighbourhoods, and (repeating if need be some of the $V_{i}$) suppose that one has a cover
$(U_{i})$ of $X$ by quasi-compact open sets having the same index set as $(V_{i})$ and such that $f(U_{i}) \subset
V_{i}$ for every $i$. Moreover, with the help of `(8.2.11)` (and replacing if need be $\alpha$ by an index $\lambda \geq
\alpha$), one can suppose that one has $U_{i} = v^{-1}_{\alpha}(U_{i\alpha})$ where the $U_{i\alpha}$ are quasi-compact
open sets in $X_{\alpha}$; furthermore, using `(8.3.4)` as above, one can suppose that $(U_{i\alpha})$ is a cover of
$X_{\alpha}$.

That being so, it will suffice to show that there exist $\lambda \geq \alpha$ and, for each $i$, a morphism
$f^{(i)}_{\lambda} : U_{i\lambda} \to V_{i\lambda}$ (with $U_{i\lambda} = v^{-1}_{\lambda \alpha}(U_{i\alpha})$ and
$V_{i\lambda} = w^{-1}_{\lambda \alpha}(V_{i\alpha})$) such that the corresponding morphism $f^{(i)} =
e_{\lambda}(f^{(i)}_{\lambda}) : U_{i} \to V_{i}$ is equal to the restriction of $f$ to $U_{i}$. Indeed, if so, since
$X_{\lambda}$ is quasi-separated `(1.2.3)`, the $U_{i\lambda} \cap U_{j\lambda}$ are quasi-compact and the uniqueness
result proved above (which applies since $Y_{\lambda}$ is locally of finite type over $S_{\lambda}$) proves that there
exists $\mu \geq \lambda$ such that $f^{(i)}_{\mu}$ and $f^{(j)}_{\mu}$ coincide in $U_{i\mu} \cap U_{j\mu}$ for every
pair $(i, j)$, and consequently define an $S_{\mu}$-morphism $f_{\mu} : X_{\mu} \to Y_{\mu}$ such that $e_{\mu}(f_{\mu})
= f$.

One is thus reduced to the case where $Y_{\alpha}$ is affine, and since moreover one can suppose that the $V_{i\alpha}$
have images in $S_{\alpha}$ contained in affine open sets, one can also suppose that $S_{\alpha}$ is affine; let then
$S_{\alpha} = \operatorname{Spec}(A_{\alpha})$, $Y_{\alpha} = \operatorname{Spec}(C_{\alpha})$, $C_{\alpha}$ being an
$A_{\alpha}$-algebra of finite presentation, $S = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(C)$, with $A = \lim
A_{\lambda}$, $C = C_{\alpha} \otimes_{A_{\alpha}} A$. One has then

```text
  Hom_S(X, Y) = Hom_{A-alg.}(C, Γ(X, 𝒪_X)) = Hom_{A_α-alg.}(C_α, Γ(X, 𝒪_X))
```

`(I, 2.2.4)` and likewise

```text
  Hom_{S_λ}(X_λ, Y_λ) = Hom_{A_λ-alg.}(C_α ⊗_{A_α} A_λ, Γ(X_λ, 𝒪_{X_λ})) = Hom_{A_α-alg.}(C_α, Γ(X_λ, 𝒪_{X_λ})).
```

But since $X_{\alpha}$ is quasi-compact and quasi-separated, one knows `(8.5.4)` that one has $\lim \Gamma(X_{\lambda},
\mathcal{O}_{X_{\lambda}}) = \Gamma(X, \mathcal{O}_{X})$; since $C_{\alpha}$ is an $A_{\alpha}$-algebra of finite
presentation, the fact that `(8.8.1.1)` is bijective then follows from `(8.8.2.3)`.

Before passing to the proof of (ii), let us note the following corollaries of (i):

**Corollary (8.8.2.4).**

<!-- label: IV.8.8.2.4 -->

*Suppose `S_0` quasi-compact, $X_{\alpha}$ of finite presentation over $S_{\alpha}$, $Y_{\alpha}$ of finite type over
$S_{\alpha}$ and quasi-separated over $S_{\alpha}$ (which will be the case for example if $Y_{\alpha}$ is also*

<!-- original page 32 -->

*of finite presentation over $S_{\alpha}$). Let $f_{\alpha} : X_{\alpha} \to Y_{\alpha}$ be an $S_{\alpha}$-morphism. In
order that $f : X \to Y$ be an isomorphism, it is necessary and sufficient that there exist $\lambda \geq \alpha$ such
that $f_{\lambda} : X_{\lambda} \to Y_{\lambda}$ be an isomorphism.*

The condition is evidently sufficient. To prove that it is necessary, note first that the question being local on `S_0`
(since $L$ is filtered), one can always suppose `S_0` affine, hence quasi-separated. There is by hypothesis an
$S$-morphism $g : Y \to X$ such that $g \circ f = 1_{X}$ and $f \circ g = 1_{Y}$. Since $X_{\alpha}$ is of finite
presentation over $S_{\alpha}$, and $Y_{\alpha}$ quasi-compact and quasi-separated (since $S_{\alpha}$ is quasi-compact
and quasi-separated), there exist $\mu \geq \alpha$ and an $S_{\mu}$-morphism $g_{\mu} : Y_{\mu} \to X_{\mu}$ such that
$g = g_{\mu} \times 1_{S}$ by virtue of `(8.8.2, (i))`. On the other hand, it also follows from `(8.8.2, (i))` and from
the relations $g \circ f = 1_{X}$ and $f \circ g = 1_{Y}$ that there exists $\nu \geq \mu$ such that one has $g_{\nu}
\circ f_{\nu} = 1_{X_{\nu}}$ and $f_{\nu} \circ g_{\nu} = 1_{Y_{\nu}}$, since $X_{\alpha}$ and $Y_{\alpha}$ are of
finite type over $S_{\alpha}$ and quasi-compact. This means that $f_{\nu} : X_{\nu} \to Y_{\nu}$ is an isomorphism,
whence the corollary.

**Corollary (8.8.2.5).**

<!-- label: IV.8.8.2.5 -->

*Suppose `S_0` quasi-compact and quasi-separated, $X_{\alpha}$ and $Y_{\alpha}$ of finite presentation over
$S_{\alpha}$. In order that $X$ and $Y$ be $S$-isomorphic, it is necessary and sufficient that there exist $\lambda \geq
\alpha$ such that $X_{\lambda}$ and $Y_{\lambda}$ be $S_{\lambda}$-isomorphic. Moreover, for every $S$-isomorphism $f :
X \to Y$, there exist $\mu \geq \lambda$ and an $S_{\mu}$-isomorphism $f_{\mu} : X_{\mu} \to Y_{\mu}$ such that $f =
f_{\mu} \times 1_{S}$.*

The condition is evidently sufficient; conversely, if there exists an $S$-isomorphism $f : X \to Y$, it follows from
`(8.8.2, (i))` that $f$ is of the form $f_{\mu} \times 1_{S}$ for some $\mu \geq \alpha$ and a homomorphism $f_{\mu} :
X_{\mu} \to Y_{\mu}$; but since $f$ is an isomorphism, it follows from `(8.8.2.4)` that there exists $\nu \geq \mu$ such
that $f_{\nu} : X_{\nu} \to Y_{\nu}$ is an isomorphism.

(ii) Consider again first the case where $S_{0} = \operatorname{Spec}(A_{0})$ and $X = \operatorname{Spec}(B)$ are
affine; then the assertion of (ii) is equivalent to Lemma `(1.8.4.2)`.

To prove (ii) in the general case, note that $S$ is quasi-compact and quasi-separated; since $X$ is of finite
presentation over $S$ and $S$ affine over `S_0`, there exists therefore a finite cover $(U_{i})$ of `S_0` and, if
$(W_{i})$ is the affine open cover of $S$ formed by the inverse images of the $U_{i}$ under the morphism $S \to S_{0}$,
a finite cover $(X_{r})$ of $X$ by affine open sets such that the image under $X \to S$ of each $X_{r}$ is contained in
some $W_{i(r)}$; the ring $A(X_{r})$ is then an algebra of finite presentation over the ring $A(W_{i(r)})$ `(1.4.6)`. By
virtue of Lemma `(1.8.4.2)` and the fact that $L$ is filtered, there exist an index $\lambda \in L$ and, for each index
$r$, an affine scheme $Z_{r\lambda}$ of finite presentation over the inverse image $W_{i(r), \lambda}$ of $U_{i(r)}$ in
$S_{\lambda}$, and an $S$-isomorphism $g_{r} : Z_{r\lambda} \times_{S_{\lambda}} S \xrightarrow{\sim} X_{r}$. Let
$Z_{rs}$ be the inverse image under $g_{r}$ of the sub-prescheme induced on the open set $X_{r} \cap X_{s}$ of $X_{r}$,
which is quasi-compact since $X$ is quasi-separated, and denote by $g'_{rs}$ the restriction $Z_{rs} \to X_{r} \cap
X_{s}$ of the isomorphism $g_{r}$. By virtue of `(8.8.2.5)`, there exist $\nu \geq \lambda$ and, for every pair $(r,
s)$, a quasi-compact open set $Z_{rs\mu}$ of $Z_{r\mu} = v^{-1}_{\mu \lambda}(Z_{r\lambda})$ such that $Z_{rs}$ is the
inverse image of $Z_{rs\mu}$; moreover, since $S_{\mu}$ is quasi-separated, and $W_{i(r), \mu}$ an open quasi-compact
set in $S_{\mu}$, each of the $Z_{rs\mu}$ is of finite presentation over $S_{\mu}$ `(1.6.2)`. Consider then, for every
pair $(r, s)$, the isomorphism $h_{sr} = g'^{-1}_{sr} \circ g'_{rs}$ from $Z_{rs}$ onto $Z_{sr}$; it follows from
`(8.8.2.4)` that there exist $\nu \geq \mu$ and, for every pair $(r, s)$, an isomorphism $h_{sr\nu} : Z_{rs\nu} \to
Z_{sr\nu}$ such that $h_{sr} = h_{sr\nu} \times 1_{S}$. Finally, for every triple $(r, s, t)$ let us denote by $h'_{sr}$
the restriction of $h_{sr}$ to

<!-- original page 33 -->

$Z_{rs} \cap Z_{rt}$; it follows at once from the definitions that $h'_{sr}$ is an isomorphism of $Z_{rs} \cap Z_{rt}$
onto $Z_{sr} \cap Z_{st}$, and that one has the relation $h'_{ts} \circ h'_{sr} = h'_{tr}$. By virtue of `(8.8.2, (i))`,
there exists therefore $\rho \geq \nu$ such that, for every triple $(r, s, t)$, one has $h'_{ts\rho} \circ h'_{sr\rho} =
h'_{tr\rho}$. One concludes that the isomorphisms $h_{sr\rho}$ verify the gluing condition $(0_{I}, 4.1.7)$ and
therefore define a prescheme $X_{\rho}$ such that $X$ is isomorphic to $X_{\rho} \times_{S_{\rho}} S$. Moreover, the
$Z_{r\rho}$ are of finite presentation over $S_{\rho}$ and, if one identifies them with open sets of $X_{\rho}$, the
intersections $Z_{r\rho} \cap Z_{s\rho}$, isomorphic to the $Z_{rs\rho}$, are quasi-compact, hence `(1.6.3)` $X_{\rho}$
is of finite presentation over $S_{\rho}$. Q.E.D.

**Scholium (8.8.3).**

<!-- label: IV.8.8.3 -->

The essential content of `(8.8.2)` may again be expressed by saying that if `S_0` is quasi-compact and quasi-separated,
the category of $S$-preschemes of finite presentation is determined up to equivalence by the data of the categories of
$S_{\lambda}$-preschemes of finite presentation, the functors $p_{\mu \lambda} : X_{\lambda} \mapsto X_{\lambda}
\times_{S_{\lambda}} S_{\mu}$ (for $\lambda \leq \mu$) between these categories, and the transitivity isomorphisms
$p_{\nu \mu} \circ p_{\mu \lambda} \xrightarrow{\sim} p_{\nu \lambda}$. Pictorially, one can say that giving an
$S$-prescheme of finite presentation $X$ amounts "functorially" to giving an $S_{\lambda}$-prescheme of finite
presentation $X_{\lambda}$; if an $S_{\mu}$-prescheme of finite presentation $X'_{\mu}$ is such that $X$ is
$S$-isomorphic to $X'_{\mu} \times_{S_{\mu}} S$, there exists $\nu$ such that $\lambda \leq \nu$, $\mu \leq \nu$ and
such that $X_{\lambda} \times_{S_{\lambda}} S_{\nu}$ and $X'_{\mu} \times_{S_{\mu}} S_{\nu}$ are $S_{\nu}$-isomorphic.
The fact that $L$ is filtered moreover entails that if one gives a finite family $(X^{(i)})_{i \in I}$ of $S$-preschemes
of finite presentation, and a finite family $(f^{(j)})_{j \in J}$ of $S$-morphisms between these preschemes ($f^{(j)}$
being therefore of the form $X^{(\sigma(j))} \to X^{(\tau(j))}$ where $\sigma$ and $\tau$ are two maps from $J$ to $I$),
then there is an index $\lambda \in L$, a family $(X^{(i)}_{\lambda})_{i \in I}$ of $S_{\lambda}$-preschemes of finite
presentation and a family $(f^{(j)}_{\lambda})_{j \in J}$ of $S_{\lambda}$-morphisms such that $X^{(i)}$ is identified
with $X^{(i)}_{\lambda} \times_{S_{\lambda}} S$ and $f^{(j)}$ with $f^{(j)}_{\lambda} \times 1_{S}$ for every $i$ and
$j$; moreover, if one has a relation $f^{(j)} = f^{(k)}$, one can suppose $\lambda$ chosen so that $f^{(j)}_{\lambda} =
f^{(k)}_{\lambda}$.

Consider in particular three $S$-preschemes of finite presentation $X$, $Y$, $Z$ and two $S$-morphisms $f : X \to Z$,
$g : Y \to Z$, so that the product $X \times_{Z} Y$ relative to these morphisms is again an $S$-prescheme of finite
presentation `(1.6.2)`. Then it follows from what precedes and from `(I, 3.3.11)` that one can write
$X \times_{Z} Y = (X_{\lambda} \times_{Z_{\lambda}} Y_{\lambda}) \times_{S_{\lambda}} S$ for a suitable $\lambda$,
$X_{\lambda}$, $Y_{\lambda}$, $Z_{\lambda}$ being $S_{\lambda}$-preschemes of finite presentation; one can therefore say
that the determination of $S$-preschemes of finite presentation by giving the $S_{\lambda}$-preschemes of finite
presentation is "compatible with fibre products". One has seen on the other hand `(8.6.3)` that if $g$ is an immersion,
one can suppose the same of $g_{\lambda} : Y_{\lambda} \to Z_{\lambda}$; identifying $Y$ (resp. $Y_{\lambda}$) with a
sub-prescheme of $Z$ (resp. $Z_{\lambda}$), one sees therefore that one can write, for a suitable $\lambda$,
$f^{-1}(Y) = f^{-1}_{\lambda}(Y_{\lambda}) \times_{S_{\lambda}} S$ `(I, 4.4.1)`; there is therefore also "compatibility
with the formation of inverse images of sub-preschemes". More particularly, if $f_{1}$, $f_{2}$ are two $S$-morphisms
from $X$ to $Y$, one calls *kernel* of this pair of morphisms the inverse image $N$ of the diagonal sub-prescheme of
$Y \times_{S} Y$ under the $S$-morphism $(f_{1}, f_{2})_{S}$; one deduces from what precedes that one will have, for a
suitable $\lambda$, $N = N_{\lambda} \times_{S_{\lambda}} S$, where $N_{\lambda}$ is the kernel of the pair of
$S_{\lambda}$-morphisms $(f_{1\lambda}, f_{2\lambda})$ from $X_{\lambda}$ to $Y_{\lambda}$. These remarks extend to
arbitrary finite products and to the "kernels" of arbitrary finite systems of $S$-morphisms from one $S$-prescheme of
finite presentation

<!-- original page 34 -->

into another; one concludes that in a general way the formation of $S$-preschemes of finite presentation by giving the
$S_{\lambda}$-preschemes of finite presentation is "compatible with finite projective limits", such a limit being by
definition the kernel of a finite system of morphisms from a single $S$-prescheme into a product of $S$-preschemes
`(T, 1.8)`.

We shall permit ourselves currently in what follows to make the translations implied by the preceding properties (as
well as by `(8.3.11)`, `(8.5.2)` and `(8.6.3)`) without always constraining ourselves to justify them step by step as
above. For example, giving a "prescheme in groups" $G$ of finite presentation over $S$ is equivalent to giving a
prescheme in groups $G_{\lambda}$ of finite presentation over an $S_{\lambda}$ for $\lambda$ sufficiently large; for
indeed to write the associativity condition for the $S$-morphism "composition law" $G \times_{S} G \to G$ of the
prescheme in groups amounts to writing that the kernel of two $S$-morphisms of the form $G \times_{S} G \times_{S} G \to
G$ is equal to $G \times_{S} G \times_{S} G$ `(II, 8.3.9)`, and the other conditions intervening in the definition of a
prescheme in groups are interpreted likewise.

<!-- original page 34 -->

### 8.9. First applications to the elimination of Noetherian hypotheses

**Proposition (8.9.1).**

<!-- label: IV.8.9.1 -->

*Let $A$ be a ring and $X$ an $A$-prescheme.*

*(i) The following conditions are equivalent:*

*a) $X$ is of finite presentation over $A$.*

*b) There exists a Noetherian ring `A_0`, a prescheme `X_0` of finite type over `A_0`, a ring homomorphism $A_{0} \to
A$, and an $A$-isomorphism $X_{0} \otimes_{A_{0}} A \xrightarrow{\sim} X$.*

*c) There exists a sub-ring `A_0` of $A$, which is a $Z$-algebra of finite type, a prescheme `X_0` of finite type over
`A_0`, and an $A$-isomorphism $X_{0} \otimes_{A_{0}} A \xrightarrow{\sim} X$.*

*(ii) If $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation, one may suppose the sub-ring
`A_0` chosen so that there exists a coherent $\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$ such that $\mathcal{F}$ is
isomorphic to $\mathcal{F}_{0} \otimes_{A_{0}} A$; $Supp(\mathcal{F})$ is constructible and closed in $X$, and there is
a closed sub-prescheme $Z$ of $X$, having $Supp(\mathcal{F})$ as underlying space, such that the canonical immersion $Z
\to X$ is of finite presentation.*

*(iii) If $Y$ is a second $A$-prescheme of finite presentation, and $f : X \to Y$ an $A$-morphism, one may suppose the
sub-ring `A_0` of $A$ chosen so that there exist a prescheme `Y_0` of finite type over `A_0`, an $A$-isomorphism $Y_{0}
\otimes_{A_{0}} A \xrightarrow{\sim} Y$ and an `A_0`-morphism $f_{0} : X_{0} \to Y_{0}$ (necessarily of finite type)
such that $f$ is identified with $f_{0} \otimes 1_{A}$.*

(i) Since $A$ is the inductive limit of its sub-rings of finite type over $Z$, a) implies c) by virtue of
`(8.8.2, (ii))`; c) implies b) since a $Z$-algebra of finite type is a Noetherian ring; finally, if `A_0` is Noetherian,
an `A_0`-prescheme of finite type is of finite presentation `(1.6.1)`, hence b) implies a) by virtue of
`(1.6.2, (iii))`.

Assertion (ii) is deduced immediately from `(8.5.2, (ii))`, `(8.3.11)` and `(1.8.2)`, and assertion (iii) from
`(8.8.2, (i))`.

**(8.9.2)**

<!-- label: IV.8.9.2 -->

Proposition `(8.9.1)` and the results of `(8.5.2)` and `(8.8.2)` make it possible to extend, in many cases, to morphisms
of finite presentation $X \to Y$ results proved by Noetherian techniques under the assumption that $Y$ is locally
Noetherian.

<!-- original page 35 -->

We shall see numerous examples of this in what follows; here we restrict ourselves to giving a few results of this type.

**Proposition (8.9.3).**

<!-- label: IV.8.9.3 -->

*Let $A$ be a ring and $M$ an $A$-module of finite presentation. Then every surjective $A$-endomorphism of $M$ is
bijective.*

Indeed, view $A$ as the inductive limit of its sub-$Z$-algebras of finite type. It follows from `(8.5.2.6)` that there
exists one of these sub-algebras `A_0` and an `A_0`-module `M_0` of finite presentation such that $M$ is $A$-isomorphic
to $M_{0} \otimes_{A_{0}} A$; moreover, if $f : M \to M$ is a surjective $A$-endomorphism, one may suppose
`(8.5.2, (i))` that there exists an `A_0`-endomorphism $f_{0} : M_{0} \to M_{0}$ such that $f = f_{0} \otimes 1_{A}$;
finally `(8.5.7)` one may suppose $f_{0}$ to be surjective. But since `A_0` is Noetherian and `M_0` is an `A_0`-module
of finite type, `M_0` is a Noetherian `A_0`-module, hence (Bourbaki, *Alg.*, chap. VIII, §2, n° 2, lemma 3) $f_{0}$ is
bijective, and consequently so is $f$.

**Proposition (8.9.4) ("generic flatness theorem").**

<!-- label: IV.8.9.4 -->

*Let $Y$ be an integral prescheme, $u : X \to Y$ a morphism of finite type and locally of finite presentation,
$\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation. Then there exists a non-empty open $U$
of $Y$ such that $\mathcal{F}|u^{-1}(U)$ is flat over $U$.*

The reasoning of the beginning of `(6.9.1)` reduces matters to proving the

**Lemma (8.9.4.1).**

<!-- label: IV.8.9.4.1 -->

*Let $A$ be an integral ring, $B$ an $A$-algebra of finite presentation, $M$ a $B$-module of finite presentation. Then
there exists an $f \neq 0$ in $A$ such that $M_{f}$ is a free $A_{f}$-module.*

Indeed, by `(8.9.1)` there is a sub-$Z$-algebra of finite type `A_0` of $A$, an `A_0`-algebra of finite type `B_0` and a
`B_0`-module of finite type `M_0` such that $B$ is $A$-isomorphic to $B_{0} \otimes_{A_{0}} A$ and $M$ is $B$-isomorphic
to $M_{0} \otimes_{A_{0}} A$; by `(6.9.2)`, there exists $f_{0} \neq 0$ in `A_0` such that $(M_{0})_{f_{0}}$ is a free
$(A_{0})_{f_{0}}$-module. Since $M_{f_{0}} = (M_{0})_{f_{0}} \otimes_{A_{0}} A$ and $A_{f_{0}} = (A_{0})_{f_{0}}
\otimes_{A_{0}} A$, $M_{f_{0}}$ is a free $A_{f_{0}}$-module.

**Corollary (8.9.5).**

<!-- label: IV.8.9.5 -->

*Let $S$ be a quasi-compact and quasi-separated prescheme, $u : X \to S$ a morphism of finite presentation,
$\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation. Then there exists a partition
$(S_{i})_{1 \leq i \leq n}$ of $S$ into a finite number of locally closed sets in $S$ such that, for $1 \leq i \leq n$,
there exists a sub-prescheme $S_{i}'$ of $S$, having $S_{i}$ as underlying space, of finite presentation over $S$, such
that if one sets $X_{i} = X \times_{S} S_{i}'$, the $\mathcal{O}_{X_{i}}$-Module $\mathcal{F}_{i} = \mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{X_{i}}$ is flat over $S_{i}'$.*

Consider a finite cover $(U_{j})_{1 \leq j \leq n}$ of $S$ by affine opens, and define by induction $T_{1} = U_{1}$,
$T_{j} = U_{j} - \bigcup_{k < j} (U_{j} \cap U_{k})$ for $j \geq 2$; each $T_{j}$ is closed in the affine open $U_{j}$,
and the $T_{j}$ are pairwise disjoint; moreover the $U_{j} \cap U_{k}$ are quasi-compact since $S$ is quasi-separated,
and consequently ($S$ being also quasi-compact) are constructible in $S$ `(1.8.1)`, hence so are the $T_{j}$. It will
obviously suffice to prove the corollary for a suitable sub-prescheme $T_{j}'$ of $S$ having $T_{j}$ as underlying
space, of finite presentation over $S$, and for the morphism and the Module deduced respectively from $u$ and
$\mathcal{F}$ by the base change $T_{j}' \to S$. Note for this that if one takes on $U_{j}$ the prescheme structure
induced by that of $S$, the open immersion $U_{j} \to S$ is quasi-compact since $S$ is quasi-separated `(1.2.7)`, hence
is of finite presentation `(1.6.2, (i))`.

<!-- original page 36 -->

It therefore suffices that $T_{j}'$ be of finite presentation over $U_{j}$; in other words, one may already restrict to
the case where $U = S$ and $T_{j} = T$ is closed constructible in $S$. Let $S = \operatorname{Spec}(A)$, and view $A$ as
inductive limit of its sub-$Z$-algebras of finite type, so that $S = \lim S_{\lambda}$, where the $S_{\lambda}$ are
affine and Noetherian. By virtue of `(8.3.11)`, there exist a $\lambda$ and a closed part (necessarily constructible)
$T_{\lambda}$ of $S_{\lambda}$ such that $T = u^{-1}_{\lambda}(T_{\lambda})$ ($u_{\lambda} : S \to S_{\lambda}$ being
the canonical morphism). One equips $T_{\lambda}$ with a structure of sub-prescheme of $S_{\lambda}$ and takes $T' =
T_{\lambda} \times_{S_{\lambda}} S$; since the canonical immersion $T_{\lambda} \to S_{\lambda}$ is of finite
presentation `(1.6.1)`, so is the immersion $T' \to S$. Since $T'$ is affine, one sees finally that one can restrict to
the case where $T' = S$ is affine. Then `(8.9.1)`, with the same notation, there exist a $\lambda$, a morphism of finite
type $u_{\lambda} : X_{\lambda} \to S_{\lambda}$ and a coherent $\mathcal{O}_{X_{\lambda}}$-Module
$\mathcal{F}_{\lambda}$ such that $X$ is isomorphic to $X_{\lambda} \times_{S_{\lambda}} S$ and $\mathcal{F}$ to
$\mathcal{F}_{\lambda} \otimes_{\mathcal{O}_{X_{\lambda}}} \mathcal{O}_{X}$. One may then apply to $S_{\lambda}$,
$X_{\lambda}$ and $\mathcal{F}_{\lambda}$ the result of `(6.9.3)`, and there are sub-preschemes $S_{\lambda,i}$ of
$S_{\lambda}$ whose underlying sets form a partition of $S_{\lambda}$ and which are such that, setting $X_{\lambda,i} =
X_{\lambda} \times_{S_{\lambda}} S_{\lambda,i}$ and $\mathcal{F}_{\lambda,i} = \mathcal{F}_{\lambda}
\otimes_{\mathcal{O}_{X_{\lambda}}} \mathcal{O}_{X_{\lambda,i}}$, the Module $\mathcal{F}_{\lambda,i}$ is flat over
$S_{\lambda,i}$. The $S_{i}' = S_{\lambda,i} \times_{S_{\lambda}} S$ are then sub-preschemes of $S$ answering the
question, by virtue of `(2.1.4)`.

### 8.10. Permanence properties of morphisms under projective passage to the limit

In this section we keep the general hypotheses and notation of `(8.8.1)`.

**Proposition (8.10.1).**

<!-- label: IV.8.10.1 -->

*If there exists $\lambda$ such that, for $\mu \geq \lambda$, $f_{\mu}$ is an open morphism (resp. universally open),
then $f$ is an open morphism (resp. universally open).*

Since $X = X_{\lambda} \times_{Y_{\lambda}} Y$, the assertion relative to universally open morphisms is a special case
of `(2.4.3, (vi))`. Suppose then $f_{\mu}$ open for $\mu \geq \lambda$; it suffices to see that for every quasi-compact
open $U$ of $X$, $f(U)$ is open in $Y$. Now there exists $\mu \geq \lambda$ such that $U = v^{-1}_{\mu}(U_{\mu})$, where
$U_{\mu}$ is a quasi-compact open in $X_{\mu}$ `(2.3.11)`; one then has $f(v^{-1}_{\mu}(U_{\mu})) =
w^{-1}_{\mu}(f_{\mu}(U_{\mu}))$ `(I, 3.4.8)`, hence $f(U)$ is open in $Y$.

**Corollary (8.10.2).**

<!-- label: IV.8.10.2 -->

*Let $f : X \to Y$ be a morphism. In order that $f$ be universally open, it suffices that, for every integer $n > 0$, if
one sets $Y_{n} = Y \otimes_{Z} Z[T_{1}, \cdots, T_{n}] (= \mathbb{V}^{n}_{Y})$ and $X_{n} = X \times_{Y} Y_{n}$, the
canonical projection $f_{n} = f \times 1_{Y_{n}} : X_{n} \to Y_{n}$ be an open morphism.*

To prove that $f$ is universally open, it suffices to prove that this is so for the restriction $f^{-1}(U) \to U$ of $f$
for every affine open $U$ of $Y$; since, by hypothesis, if $U_{n} = U \otimes_{Z} Z[T_{1}, \cdots, T_{n}]$ is the
inverse image of $U$ in $Y_{n}$, the morphism $f^{-1}_{n}(U_{n}) \to U_{n}$, restriction of $f_{n}$, is open, one sees
that one may restrict to the case where $Y = \operatorname{Spec}(A)$ is affine. Moreover, it obviously suffices to show
that for every morphism $Y' \to Y$, where $Y' = \operatorname{Spec}(A')$ is itself also affine, $f' = f_{(Y')}$ is open.
Suppose first that $A'$ is an $A$-algebra of finite type, hence quotient of a polynomial algebra $A[T_{1}, \cdots,
T_{n}]$; then $Y'$ is a closed sub-prescheme of $Y_{n}$ and $f'$ the

<!-- original page 37 -->

restriction of $f_{n}$ to $f^{-1}_{n}(Y')$; but for every open $V$ of $X_{n}$ one has $f'(V \cap f^{-1}_{n}(Y')) =
f_{n}(V) \cap Y'$, and since by hypothesis $f_{n}(V)$ is open in $Y_{n}$, this shows that $f'$ is also an open morphism.
When $A'$ is arbitrary, it may be viewed as inductive limit of its sub-$A$-algebras of finite type $A_{\lambda}'$, and
the fact that $f'$ is an open morphism results from what precedes and from `(8.10.1)`.

**Proposition (8.10.3).**

<!-- label: IV.8.10.3 -->

*Suppose there exists $\alpha$ such that: 1° $S_{\alpha}$ is quasi-compact; 2° the morphisms $X_{\alpha} \to
S_{\alpha}$, $Y_{\alpha} \to S_{\alpha}$ are quasi-compact and the morphism $Y_{\alpha} \to S_{\alpha}$ is
quasi-separated; 3° for $\alpha \leq \lambda \leq \mu$, the morphisms $u_{\lambda \mu} : S_{\mu} \to S_{\lambda}$ are
flat; 4° $f_{\alpha}(X_{\alpha})$ is constructible in $Y_{\alpha}$. Then, in order that $f$ be dominant, it is necessary
and sufficient that there exist $\lambda \geq \alpha$ such that $f_{\lambda}$ be dominant.*

The hypotheses entail that $Y_{\alpha}$ is quasi-compact and that the morphism $f_{\alpha}$ is quasi-compact `(1.2.4)`;
consequently $f_{\alpha}(X_{\alpha}) = Z_{\alpha}$ is pro-constructible `(1.9.5, (v"))` in $Y_{\alpha}$. If one sets
$Z_{\lambda} = w^{-1}_{\alpha \lambda}(Z_{\alpha})$ for $\lambda \geq \alpha$ and $Z = w^{-1}_{\alpha}(Z_{\alpha})$, one
then has $Z_{\lambda} = f_{\lambda}(X_{\lambda})$ and $Z = f(X)$ `(I, 3.4.8)`, and $Z_{\lambda}$ is pro-constructible in
$Y_{\lambda}$ `(1.9.5, (vi))`. It then suffices to apply `(8.3.13)` after replacing $S_{\lambda}$, $Z_{\lambda}$ and
$Z_{\lambda}'$ by $Y_{\lambda}$, $Y_{\lambda}$ and $Z_{\lambda}$ respectively.

**Proposition (8.10.4).**

<!-- label: IV.8.10.4 -->

*Suppose there exists $\alpha$ such that $Y_{\alpha}$ is quasi-compact and $f_{\alpha}$ of finite type and
quasi-separated. In order that the morphism $f$ be separated, it is necessary and sufficient that there exist $\lambda
\geq \alpha$ such that $f_{\lambda}$ be separated.*

The question being local on $Y_{\alpha}$ (since $Y_{\alpha}$ is quasi-compact and $L$ filtered), one may restrict to the
case where $Y_{\alpha}$ is affine, hence quasi-separated, and the hypothesis entails that $X_{\alpha}$ (hence the
$X_{\lambda}$ and $X$) are quasi-compact and quasi-separated. Set $X_{\lambda}' = X_{\lambda} \times_{Y_{\lambda}}
X_{\lambda}$ for $\lambda \geq \alpha$ and $X' = X \times_{Y} X$; one has $X_{\lambda}' = X_{\alpha}'
\times_{Y_{\alpha}} Y_{\lambda}$ and $X' = X_{\alpha}' \times_{Y_{\alpha}} Y$; the first-projection morphism
$X_{\lambda}' \to X_{\alpha}'$ is quasi-compact and quasi-separated by hypothesis `(1.2.3, (iii))`, hence $X_{\lambda}'$
is quasi-compact and quasi-separated. Note now that if one denotes by $\Delta_{\lambda}$ (resp. $\Delta$) the diagonal
of $X_{\lambda} \times_{Y_{\lambda}} X_{\lambda}$ (resp. of $X \times_{Y} X$), it follows from `(I, 5.3.4 and 3.4.8)`
that $\Delta_{\mu}$ (resp. $\Delta$) is the inverse image of $\Delta_{\lambda}$ under the morphism $v_{\lambda \mu}' :
X_{\mu}' \to X_{\lambda}'$ (resp. $v_{\lambda}' : X' \to X_{\lambda}'$). On the other hand, $\Delta_{\alpha}$ is
constructible in $X_{\alpha}'$: indeed, since $f_{\alpha}$ is quasi-separated, the diagonal immersion $X_{\alpha} \to
X_{\alpha}'$ is quasi-compact, and locally of finite presentation since $f_{\alpha}$ is of finite type `(1.4.3` and
`I, 5.4, (iii))`; it then follows from `(1.8.4.1)` that $\Delta_{\alpha}$ is locally constructible, hence constructible
since $X_{\alpha}'$ is quasi-compact. One may now apply `(8.3.12)` after replacing $S_{\lambda}$ and $Z_{\lambda}$ by
$X_{\lambda}'$ and $\Delta_{\lambda}$ respectively.

**Theorem (8.10.5).**

<!-- label: IV.8.10.5 -->

*Suppose `S_0` quasi-compact, $X_{\alpha}$ and $Y_{\alpha}$ of finite presentation over $S_{\alpha}$, and let
$f_{\alpha} : X_{\alpha} \to Y_{\alpha}$ be an $S_{\alpha}$-morphism. Consider, for a morphism, the property of being:*

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

*Then, if $P$ denotes one of the preceding properties, in order that $f$ have property $P$, it is necessary and
sufficient that there exist $\lambda \geq \alpha$ such that $f_{\lambda}$ have property $P$ (in which case $f_{\mu}$
also has it for $\mu \geq \lambda$).*

*If `S_0` is moreover supposed quasi-separated, the same conclusion is valid when $P$ is the property of being:*

*(xiii) projective;*

*(xiv) quasi-projective.*

The case where $P$ is one of the properties (i) or (v) is inserted in the statement only for the record; in these cases,
the theorem follows from what has been proved respectively in `(8.8.2.4)` and `(8.10.4)`. Moreover, taking into account
`(I, 5.4.1` and `5.3.4)`, (v) also results from (iv). The case (i bis) is deduced at once from (i), using `(I, 5.3.8)`
and noting (as was already used in `(8.10.4)`) that the diagonal $\Delta$ is deduced from $\Delta_{\lambda}$ by the base
change $S \to S_{\lambda}$.

One notes on the other hand that (vi), (vii) and (xi) are in fact conditions on the fibres $f^{-1}(y)$ of the morphisms
considered, taking into account the transitivity of fibres under base change `(I, 3.6.4)`: condition (vi) signifies in
effect that all the fibres must be non-empty, condition (vii) that they must be radicial `(I, 3.5.8)`, and condition
(xi) that they must be finite `(II, 6.2.2` and `6.2.3` and `II, 6.4.4`, taking into account that $f$ and the
$f_{\lambda}$ are morphisms of finite type by `(1.5.4, (v))`. The theorem in these three cases will therefore again be
consequence of a general result on this type of properties concerning only the fibres, which will be established in
`(9.3.3)`; we therefore postpone until that moment the demonstration of the theorem in case (xi) (of course, the reader
can verify that, except in nos. `8.11` and `8.12`, we shall not make use of the theorem in this case until `(9.3.3)`,
and that `(8.11)` and `(8.12)` will not be used before `(9.3.3)`).

For the cases that remain to be proved, one may restrict to showing that the condition of the statement is necessary,
all the properties $P$ considered being invariant under base change (see chap. I and II in the numbers concerning each
of these properties). One may moreover suppose that $S_{\alpha} = S_{0}$ and that $Y_{\alpha} = S_{\alpha}$, hence
$Y_{\lambda} = S_{\lambda}$ for all $\lambda \geq \alpha$. Finally, properties (i) to (xii) are local on `S_0`, hence,
since `S_0` is a finite union of affine opens and $L$ is filtered, one may restrict for proving them to the case where
$S_{0} = \operatorname{Spec}(A_{0})$ is affine (hence quasi-separated). One denotes by $A_{\lambda}$ (resp. $A$) the
ring of $S_{\lambda}$ (resp. $S$).

*Cases (ii), (iii), (iv):* Suppose that $f$ is an immersion (resp. an open immersion, resp. a closed immersion), and let
$X'$ be the sub-prescheme (resp. induced on an open, resp. closed) of $S$ associated with $f$, which is therefore an
$S$-prescheme of finite presentation.

<!-- original page 39 -->

By virtue of `(8.6.3)`, there exist therefore a $\lambda \geq \alpha$ and a sub-prescheme (resp. induced on an open,
resp. closed) $X_{\lambda}'$ of $S_{\lambda}$, of finite presentation over $S_{\lambda}$, such that $X'$ is isomorphic
to $X_{\lambda}' \times_{S_{\lambda}} S$. For every $\mu \geq \lambda$, $X_{\mu}' = X_{\lambda}' \times_{S_{\lambda}}
S_{\mu}$ is therefore a sub-prescheme (resp. induced on an open, resp. closed) of $S_{\mu}$, of finite presentation over
$S_{\mu}$, and it therefore follows from `(8.8.2.4)` and `(8.8.2.5)` that there exist a $\mu \geq \lambda$ and an
isomorphism $g_{\mu} : X_{\mu} \to X_{\mu}'$ such that $g = g_{\mu} \times 1_{S}$ is the isomorphism $X \to X'$
associated with $f$; whence the conclusion.

*Cases (vi) and (vii):* One knows `(1.8.4.1)` that $Z_{\alpha} = f_{\alpha}(X_{\alpha})$ is constructible in
$S_{\alpha}$; if one sets $Z_{\lambda} = u^{-1}_{\alpha \lambda}(Z_{\alpha})$ for $\lambda \geq \alpha$ and $Z =
u^{-1}_{\alpha}(Z_{\alpha})$, one has $Z_{\lambda} = f_{\lambda}(X_{\lambda})$ and $Z = f(X)$ `(I, 3.4.8)`. Since, by
virtue of `(8.3.11)`, the canonical application $\lim \mathcal{C}(S_{\lambda}) \to \mathcal{C}(S)$ is injective, the
relation $f(X) = S$ implies the existence of a $\lambda \geq \alpha$ such that $f_{\lambda}(X_{\lambda}) = S_{\lambda}$,
which proves the theorem in case (vi). To prove it in case (vii), it suffices to note that the structure morphism
$X_{\alpha} \times_{S_{\alpha}} X_{\alpha} \to S_{\alpha}$ is of finite presentation since this is so of the first
projection $X_{\alpha} \times_{S_{\alpha}} X_{\alpha} \to X_{\alpha}$ `(1.6.2)`; it therefore suffices, by virtue of
`(1.8.7.1)`, to apply case (vi) of the theorem to the diagonal morphism $\Delta_{f_{\alpha}} : X_{\alpha} \to X_{\alpha}
\times_{S_{\alpha}} X_{\alpha}$, noting that one has $\Delta_{f_{\lambda}} = \Delta_{f_{\alpha}} \times 1_{S_{\lambda}}$
and $\Delta_{f} = \Delta_{f_{\alpha}} \times 1_{S}$ `(I, 5.3.4` and `3.3.11)`.

*Cases (viii) and (ix):* Since $S = \operatorname{Spec}(A)$ is affine, to say that $f : X \to S$ is affine (resp.
quasi-affine) signifies that there exists an integer $r$ and a closed immersion (resp. an immersion) $j : X \to
\mathbb{V}^{r}_{S} = \operatorname{Spec}(A[T_{1}, \cdots, T_{r}])$ of $S$-preschemes, since $f$ is of finite type and
$S$ quasi-compact `(II, 5.1.9)`. Since $\mathbb{V}^{r}_{S} = \mathbb{V}^{r}_{S_{0}} \times_{S_{0}} S$, and
$\mathbb{V}^{r}_{S_{0}}$ is an `S_0`-prescheme of finite presentation, it follows from `(8.8.2, (i))` applied to the
$S$-morphism $j$ that there exists a $\lambda$ and an $S_{\lambda}$-morphism $j_{\lambda} : X_{\lambda} \to
\mathbb{V}^{r}_{S_{\lambda}}$ such that $j = j_{\lambda} \times 1_{S}$; applying then (iv) (resp. (ii)) to $j$, one
deduces that there exists $\mu \geq \lambda$ such that $j_{\mu}$ is a closed immersion (resp. an immersion);
consequently $f_{\mu}$ is affine (resp. quasi-affine).

*Case (x):* By hypothesis, one has $X = \operatorname{Spec}(B)$, where $B$ is an $A$-algebra which is an $A$-module of
finite presentation `(1.4.7)`; it follows therefore from `(8.5.2, (ii))` that there is a $\lambda$ and an
$A_{\lambda}$-module of finite presentation $B_{\lambda}$ such that the $A$-module $B$ is isomorphic to $B_{\lambda}
\otimes_{A_{\lambda}} A$. The $A$-algebra structure of $B$ is defined by an $A$-homomorphism $m : B \otimes_{A} B \to
B$; since one has $B \otimes_{A} B = (B_{\lambda} \otimes_{A_{\lambda}} B_{\lambda}) \otimes_{A_{\lambda}} A$, there
exists according to `(8.5.2, (i))` a $\mu \geq \lambda$ and an $A_{\mu}$-homomorphism $m_{\mu} : B_{\mu}
\otimes_{A_{\mu}} B_{\mu} \to B_{\mu}$ such that $m = m_{\mu} \otimes 1$. Considering the usual diagrams expressing the
associativity and commutativity of $m$, one sees by applying again `(8.5.2, (i))` that there exists $\nu \geq \mu$ such
that $m_{\nu}$ defines on $B_{\nu}$ an associative and commutative multiplication; in the same way one sees that one can
suppose $\nu$ taken large enough so that the ring $B_{\nu}$ thus defined admits a unit element. If $X_{\nu} =
\operatorname{Spec}(B_{\nu})$, it is then clear that $X$ is $S$-isomorphic to $X_{\nu} \times_{S_{\nu}} S$, hence, by
virtue of (i), there exists $\rho \geq \nu$ such that $X_{\rho}$ and $X_{\nu} \times_{S_{\nu}} S_{\rho}$ are
$S_{\rho}$-isomorphic, which finishes the demonstration in this case.

To prove the theorem in case (xii), we first prove the following proposition:

**Proposition (8.10.5.1) (Chow's lemma for morphisms of finite presentation).**

<!-- label: IV.8.10.5.1 -->

*Let $A$ be a ring, $X$, $Y$ two $A$-preschemes of finite presentation, $f : X \to Y$*

<!-- original page 40 -->

*an $A$-morphism, separated. Then there exist two $A$-preschemes $X'$, $P$ of finite presentation, and $A$-morphisms
$p : P \to Y$, $j : X' \to P$, $g : X' \to X$, such that the diagram*

```text
                          X' ───j──→ P
                          │           │
                          g           p
                          ↓           ↓
                          X ────f──→ Y
```

*is commutative, and: 1° $p$ is projective; 2° $g$ is projective and surjective; 3° $j$ is an open immersion.*

Indeed, let $A_{0} \subset A$, `X_0`, `Y_0` and $f_{0}$ be determined as in `(8.9.1)` so that `Y_0` is Noetherian and
$f_{0}$ is of finite type; one may moreover suppose $f_{0}$ separated by `(8.10.4)`. Chow's lemma `(II, 5.6.1)` then
shows the existence of three morphisms $p_{0} : P_{0} \to Y_{0}$, $g_{0} : X_{0}' \to X_{0}$ and $j_{0} : X_{0}' \to
P_{0}$, of finite type, such that the diagram

```text
                          X_0' ──j_0──→ P_0
                          │              │
                          g_0            p_0
                          ↓              ↓
                          X_0 ───f_0──→ Y_0
```

is commutative, and $p_{0}$ is projective, $g_{0}$ projective and surjective, and $j_{0}$ an open immersion. The
properties of the statement then result from the invariance of the preceding properties under base change
`(II, 5.5.5, (iii)` and `I, 3.5.2` and `4.3.2)`.

*Case (xii):* Apply to the morphism $f_{0} : X_{0} \to S_{0}$ proposition `(8.10.5.1)`: one then has a commutative
diagram

```text
                          X_0' ──j_0──→ P_0
                          │              │
                          g_0            p_0
                          ↓              ↓
                          X_0 ───f_0──→ S_0
```

where $p_{0}$ is projective, $g_{0}$ projective and surjective, and $j_{0}$ an open immersion; one deduces for each
$\lambda$ an analogous diagram where the morphisms $p_{\lambda} = p_{0} \times 1_{S_{\lambda}}$, $g_{\lambda} = g_{0}
\times 1_{S_{\lambda}}$ and $j_{\lambda} = j_{0} \times 1_{S_{\lambda}}$ have respectively the same properties, and
likewise for the projective-limit morphisms $p = p_{0} \times 1_{S}$, $g = g_{0} \times 1_{S}$, $j = j_{0} \times
1_{S}$. Since $g$ is proper `(II, 5.5.3)`, so is $p \circ j = f \circ g$ `(II, 5.4.2)`, and since $p$ is separated, $j$
is proper, hence a closed immersion; applying case (iv) to the morphism $j$ (noting that $X_{0}'$ and `P_0` are
`S_0`-preschemes of finite presentation `(8.10.5.1` and `1.6.2)`), one sees that there exists $\lambda$ such that
$j_{\lambda}$ is a closed immersion, hence is proper `(II, 5.4.2)`. But then $f_{\lambda} \circ g_{\lambda} =
p_{\lambda} \circ j_{\lambda}$ is proper `(II, 5.5.3` and `5.4.2)`, and since $g_{\lambda}$ is surjective, and one can
suppose $f_{\lambda}$ separated by virtue of the hypothesis on $f$ and of (v), it follows from `(II, 5.4.3)` that
$f_{\lambda}$ is proper.

*Cases (xiii) and (xiv):* By virtue of (xii) and of `(II, 5.5.3)` (which is applicable since the $S_{\lambda}$ are
quasi-compact and quasi-separated, taking into account `(1.7.19)`), it suffices to

<!-- original page 41 -->

consider the case where $f$ is quasi-projective. Suppose then that there exists an invertible $\mathcal{O}_{X}$-Module
$\mathcal{L}$ which is $f$-ample; since `S_0` is quasi-compact and quasi-separated, so is `X_0` `(1.2.3)`, and there is
therefore a $\lambda$ and a quasi-coherent $\mathcal{O}_{X_{\lambda}}$-Module $\mathcal{L}_{\lambda}$ of finite
presentation such that $\mathcal{L} = v^{*}_{\lambda}(\mathcal{L}_{\lambda})$ `(8.5.2, (ii))`; moreover, by virtue of
`(8.5.5)`, one may suppose $\mathcal{L}_{\lambda}$ invertible. The theorem in this case is then consequence of the more
precise lemma:

**Lemma (8.10.5.2).**

<!-- label: IV.8.10.5.2 -->

*Suppose `S_0` quasi-compact, and let $\mathcal{L}_{\lambda}$ be an invertible $\mathcal{O}_{X_{\lambda}}$-Module. In
order that $\mathcal{L}$ be an $\mathcal{O}_{X}$-Module ample for $f$ (resp. very ample for $f$), it is necessary and
sufficient that there exist $\mu \geq \lambda$ such that $\mathcal{L}_{\mu}$ be ample for $f_{\mu}$ (resp. very ample
for $f_{\mu}$).*

The condition being obviously sufficient `(II, 4.4.10` and `4.6.13)`, let us show that it is necessary; the
$S_{\lambda}$ being quasi-compact and the $f_{\lambda}$ of finite type, one may, by replacing $\mathcal{L}$ by a
suitable tensor power, restrict to the case where $\mathcal{L}$ is very ample `(II, 4.6.11)`. Moreover, the question
being here local on `S_0` (in view of `(II, 4.4.5)` and the fact that $L$ is filtered), one may restrict to the case
where `S_0` (and consequently $S$) is affine. Then, by virtue of `(II, 4.4.1, (ii)` and `II, 4.1.2)`, there exists an
$S$-immersion $j : X \to \mathbb{P}^{r}_{S} = P$ such that $\mathcal{L}$ is isomorphic to $j^{*}(\mathcal{O}_{P}(1))$.
Taking into account `(8.8.2, (i))`, of (ii) and of `(II, 4.1.3)`, there exists therefore a $\mu \geq \lambda$ and an
immersion $j_{\mu} : X_{\mu} \to \mathbb{P}^{r}_{S_{\mu}} = P_{\mu}$ such that $j = j_{\mu} \times 1_{S}$; using next
`(II, 4.1.3.2)` and `(8.5.2.5)`, one sees that there exists $\nu \geq \mu$ such that $\mathcal{L}_{\nu}$ is isomorphic
to $j^{*}_{\nu}(\mathcal{O}_{P_{\nu}}(1))$, which shows that $\mathcal{L}_{\nu}$ is very ample for $f_{\nu}$
`(II, 4.4.2)`.

### 8.11. Application to quasi-finite morphisms

We propose in this section to prove the two following theorems:

**Theorem (8.11.1).**

<!-- label: IV.8.11.1 -->

*Let $f : X \to Y$ be a proper morphism, locally of finite presentation, and quasi-finite. Then the morphism $f$ is
finite.*

**Theorem (8.11.2).**

<!-- label: IV.8.11.2 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, quasi-finite and separated. Then the morphism $f$ is
quasi-affine, and a fortiori quasi-projective.*

**Remark (8.11.3).**

<!-- label: IV.8.11.3 -->

We shall see below that, for the proof of `(8.11.1)` and `(8.11.2)`, one may reduce to the case where $Y$ is locally
Noetherian; one notes that in this case one obtains thereby another demonstration of Chevalley's theorem `(III, 4.4.2)`.

**(8.11.4)**

<!-- label: IV.8.11.4 -->

The hypotheses and conclusions of `(8.11.1)` and `(8.11.2)` are all local on $Y$
`(1.6.1, 1.2.6, (II, 5.1.1), (II, 5.4.1)` and `(II, 6.2.2))`, hence one may suppose $Y = \operatorname{Spec}(A)$ affine.
One knows that there then exists a sub-ring `A_0` of $A$, which is a $Z$-algebra of finite type, and a morphism of
finite type $f_{0} : X_{0} \to \operatorname{Spec}(A_{0})$ such that $X$ identifies with $X_{0} \otimes_{A_{0}} A$ and
$f$ with $f_{0} \times 1$ `(8.9.1)`. Moreover, $A$ may be viewed as inductive limit of its sub-rings containing `A_0`
and which are $Z$-algebras of finite type; using the method of `(8.1.2, c))` as well as `(8.10.5, (v), (xi)` and
`(xii))`, one sees that it suffices to prove the theorems `(8.11.1)` and `(8.11.2)` for $f_{0}$. Suppose then henceforth
$Y$ Noetherian; using now the method of `(8.1.2, a))` as well as `(8.10.5, (v), (ix), (x), (xi)` and `(xii))`, one may
replace $Y$ by $\operatorname{Spec}(\mathcal{O}_{y})$, where $y$ is a

<!-- original page 42 -->

point of $Y$, hence one sees finally that one may suppose $Y = \operatorname{Spec}(A)$, where $A$ is a Noetherian local
ring. Let $\mathfrak{m}$ be the maximal ideal of $A$, `Â` the completion of $A$ for the $\mathfrak{m}$-preadic topology;
one knows that `Â` is a Noetherian local ring and that the morphism $\operatorname{Spec}(\hat{A}) \to
\operatorname{Spec}(A)$ is faithfully flat and quasi-compact $(0_{I}, 7.3.5)$; applying
`(2.7.1, (i), (vii), (xiv), (xv)` and `(xvi))`, one sees moreover that one may restrict to the case where $A$ is
complete. It then follows from `(II, 6.2.6)` that $X = X' \sqcup X''$, where $X'$ is a $Y$-scheme finite and `X''` a
$Y$-scheme quasi-finite such that $X'' \cap f^{-1}(y) = \emptyset$.

Place ourselves first in the hypotheses of `(8.11.1)`; since $f$ is proper, `X''`, which is closed in $X$, is proper
over $Y$ `(II, 5.4.10)`, hence $f(X'')$ is closed in $Y$; but $y$ is not contained in $f(X'')$, and moreover is in the
closure of every point of $Y$, hence $f(X'') = \emptyset$, and consequently `X''` is empty and $f$ is finite.

Place ourselves now in the hypotheses of `(8.11.2)` and, restricting (as one may do by what precedes) to the case where
$Y = \operatorname{Spec}(A)$ is affine and Noetherian of finite dimension, reason moreover by induction on the dimension
of $Y$. Reducing as above to the case where $A$ is in addition local and complete, one has `dim(𝒪_y) = dim(A) = dim(Y)`
and for every $\xi \neq y$, $\dim(\mathcal{O}_{\xi}) < \dim(\mathcal{O}_{y})$, hence $\dim(Y - {y}) < \dim(Y)$. Now, by
hypothesis one has $f(X'') \subset Y - {y}$ and the restriction of $f$ to `X''` is obviously a quasi-finite and
separated morphism; applying to $Y - {y}$ and `X''` the inductive hypothesis, one sees that `X''` is quasi-affine over
$Y - {y}$; but the open $Y - {y}$ being quasi-affine over $Y$ since $Y$ is Noetherian, `X''` is also quasi-affine over
$Y$ `(II, 5.1.10, (ii))`; since moreover $X'$ is finite (and a fortiori affine) over $Y$, $X$ is quasi-affine over $Y$
`(II, 4.6.17` and `5.1.2, c'))`.

**Proposition (8.11.5).**

<!-- label: IV.8.11.5 -->

*Let $f : X \to Y$ be a morphism of finite presentation. The following properties are equivalent:*

*a) $f$ is a closed immersion.*

*b) $f$ is a proper monomorphism.*

*c) $f$ is proper and for every $y \in Y$, $f^{-1}(y)$ is radicial and geometrically reduced over $k(y)$ (that is to
say, empty or $k(y)$-isomorphic to $\operatorname{Spec}(k(y))$).*

It is clear that a) implies b). To see that b) implies c), note `(I, 3.3.12)` that for every $y \in Y$, the morphism
$f^{-1}(y) \to \operatorname{Spec}(k(y))$ deduced from $f$ by base change is a monomorphism, hence is injective, and
consequently $f^{-1}(y)$ is empty or reduced to a point, and in any case affine. Moreover, if $A$ is the ring of
$f^{-1}(y)$, the canonical homomorphism $A \otimes_{k(y)} A \to A$ is bijective `(I, 5.3.8)`. This entails obviously
that $A = k(y)$, otherwise there would be an element $a \in A$ not in $k(y)$ and the images of $a \otimes 1$ and $1
\otimes a$ in $A$ would both be equal to $a$, whereas $a \otimes 1 \neq 1 \otimes a$ since `1` and $a$ form a linearly
independent system over $k(y)$.

It remains to prove that c) implies a). It follows first of all from `(8.11.1)` that $f$ is a finite morphism, hence $X
= \operatorname{Spec}(\mathcal{A})$, where $\mathcal{A}$ is a finite $\mathcal{O}_{Y}$-Algebra. It therefore suffices to
prove that the canonical homomorphism $\mathcal{O}_{Y} \to \mathcal{A}$ is surjective `(II, 1.4.10)`, or equivalently
that for every $y \in Y$, the homomorphism $\mathcal{O}_{y} \to \mathcal{A}_{y}$ is surjective. But by hypothesis

<!-- original page 43 -->

$f^{-1}(y) = \operatorname{Spec}(\mathcal{A}_{y} / \mathfrak{m}_{y} \mathcal{A}_{y})$ `(II, 1.5.5)` is such that the
corresponding homomorphism $k(y) = \mathcal{O}_{y} / \mathfrak{m}_{y} \to \mathcal{A}_{y} / \mathfrak{m}_{y}
\mathcal{A}_{y}$ is bijective; since $\mathcal{A}_{y}$ is an $\mathcal{O}_{y}$-module of finite type, Nakayama's lemma
shows that $\mathcal{O}_{y} \to \mathcal{A}_{y}$ is surjective, which finishes the demonstration.

**Remark (8.11.5.1).**

<!-- label: IV.8.11.5.1 -->

One notes that the preceding reasoning proves that if $f$ is a monomorphism, then, for every $y \in Y$, $f^{-1}(y)$ is
empty or $k(y)$-isomorphic to $\operatorname{Spec}(k(y))$.

**Proposition (8.11.6).**

<!-- label: IV.8.11.6 -->

*If a morphism $f : X \to Y$ of finite presentation is a universal homeomorphism, it is finite, surjective and radicial
(the converse being true by `(2.4.5, (iv))`).*

Indeed, $f$ being of finite type, universally closed, and separated by virtue of `(2.4.4)`, is proper by definition
`(II, 5.4.1)`. Since it is obviously quasi-finite `(II, 6.2.3)`, it is finite by `(8.11.1)`. One knows moreover that it
is radicial `(2.4.4)`, and obviously surjective.

### 8.12. New demonstration and generalization of Zariski's *Main Theorem*

**Lemma (8.12.1).**

<!-- label: IV.8.12.1 -->

*Let $f : X \to Y$ be a quasi-compact and quasi-separated morphism, $\mathcal{C}$ a quasi-coherent
$\mathcal{O}_{Y}$-Algebra, $Z = \operatorname{Spec}(\mathcal{C})$, which is a $Y$-prescheme affine over $Y$. Let $g : X
\to Z$ be a $Y$-morphism, $\phi = \mathcal{A}(g) : \mathcal{C} \to f_{*}(\mathcal{O}_{X})$ the corresponding
$\mathcal{O}_{Y}$-homomorphism of $\mathcal{O}_{Y}$-Algebras `(II, 1.2.7)`. Suppose that $g$ is an immersion. Then, in
order that the closed image of $X$ under $g$ `(I, 9.5.3)` be equal to $Z$, it is necessary and sufficient that $\phi$ be
injective; $g$ is then an open immersion.*

The hypothesis entails that $f_{*}(\mathcal{O}_{X})$ is a quasi-coherent $\mathcal{O}_{Y}$-Algebra `(1.7.5)`; moreover,
since the canonical morphism $h : Z \to Y$ is affine, hence quasi-compact and separated, $g$ is a quasi-compact and
quasi-separated morphism `(1.2.2` and `1.1.2)`, hence $g_{*}(\mathcal{O}_{X})$ is a quasi-coherent
$\mathcal{O}_{Z}$-Algebra `(1.7.5)`. This being so, to say that the closed image of $X$ under $g$ is equal to $Z$
signifies `(I, 9.5.2)` that the canonical homomorphism $\theta : \mathcal{O}_{Z} \to g_{*}(\mathcal{O}_{X})$ is
injective. But one has $h_{*}(\mathcal{O}_{Z}) = \mathcal{C}$ by definition of $Z$ `(II, 1.3.1)`, and
$h_{*}(g_{*}(\mathcal{O}_{X})) = f_{*}(\mathcal{O}_{X})$. Since $Z$ is affine over $Y$, it comes to the same thing to
say that the homomorphism $\theta : \mathcal{O}_{Z} \to g_{*}(\mathcal{O}_{X})$ is injective or that the corresponding
homomorphism $\phi = h_{*}(\theta) : \mathcal{C} \to f_{*}(\mathcal{O}_{X})$ is injective `(I, 1.3.9)`. The fact that
$g$ is then an open immersion results from `(I, 9.5.10)` and the hypothesis that $g$ is an immersion.

**Lemma (8.12.2).**

<!-- label: IV.8.12.2 -->

*Let $Y$ be a quasi-compact and quasi-separated prescheme, $f : X \to Y$ a quasi-separated morphism of finite type,
$\mathcal{C}$ a quasi-coherent $\mathcal{O}_{Y}$-Algebra, $Z = \operatorname{Spec}(\mathcal{C})$. Let $g : X \to Z$ be a
$Y$-morphism, $\phi : \mathcal{C} \to f_{*}(\mathcal{O}_{X})$ the corresponding $\mathcal{O}_{Y}$-homomorphism of
$\mathcal{O}_{Y}$-Algebras. Let $(\mathcal{C}_{\lambda})$ be the increasing filtered family of quasi-coherent
sub-$\mathcal{O}_{Y}$-Algebras of finite type of $\mathcal{C}$ (of which $\mathcal{C}$ is the union `((I, 9.6.6)` and
`(1.7.9))`); set $Z_{\lambda} = \operatorname{Spec}(\mathcal{C}_{\lambda})$ and let $g_{\lambda}$ be the composite
morphism $X \to Z \to Z_{\lambda}$. Then the following conditions are equivalent:*

*a) $g$ is an immersion.*

*b) There exists $\lambda$ such that $g_{\lambda}$ is an immersion.*

<!-- original page 44 -->

*Moreover, when $g_{\lambda}$ is an immersion, so is $g_{\mu}$ for $\mu \geq \lambda$.*

It suffices to apply `(II, 3.8.4)` after replacing $\mathcal{L}$ by $\mathcal{O}_{X}$ and $\mathcal{A}$ by
$\mathcal{C}[T]$, and taking into account `(II, 3.1.7)`.

**Proposition (8.12.3).**

<!-- label: IV.8.12.3 -->

*Let $Y$ be a quasi-compact and quasi-separated prescheme, $f : X \to Y$ a separated morphism of finite type. Let
$\mathcal{B} = f_{*}(\mathcal{O}_{X})$, which is a quasi-coherent $\mathcal{O}_{Y}$-Algebra `(I, 9.2.2)`; let
$\mathcal{C}$ be the integral closure of $\mathcal{O}_{Y}$ in $\mathcal{B}$, which is a quasi-coherent
$\mathcal{O}_{Y}$-Algebra `(II, 6.3.4)`; set $Z = \operatorname{Spec}(\mathcal{C})$, and let $g : X \to Z$ be the
$Y$-morphism corresponding to the canonical injection $\phi : \mathcal{C} \to \mathcal{B} = f_{*}(\mathcal{O}_{X})$
`(II, 1.2.7)`. Let $(\mathcal{C}_{\lambda})$ be the increasing filtered family of quasi-coherent
sub-$\mathcal{O}_{Y}$-Algebras of finite type of $\mathcal{C}$ (of which $\mathcal{C}$ is the union `((I, 9.6.6)` and
`(1.7.9))`), and, for every $\lambda$, let $g_{\lambda} : X \to Z_{\lambda} =
\operatorname{Spec}(\mathcal{C}_{\lambda})$ be the $Y$-morphism corresponding to the injection $\mathcal{C}_{\lambda}
\to \mathcal{B} = f_{*}(\mathcal{O}_{X})$. Then the following conditions are equivalent:*

*a) There exists a factorization of $f$ as*

```text
                                    f'        u
                                X ───→ Y' ───→ Y
```

*where $f'$ is an immersion and $u$ a finite morphism.*

*a') There exists a factorization $X \to^{f'} Y' \to^{u} Y$ of $f$, where $f'$ is an open immersion and $u$ a finite
morphism.*

*b) The morphism $g : X \to Z$ is an immersion.*

*c) There exists $\lambda$ such that $g_{\lambda} : X \to Z_{\lambda}$ is an immersion.*

*Moreover, when this is so, $g$ is an open immersion, $g(X)$ is dense in $Z$, and there exists $\lambda$ such that, for
$\mu \geq \lambda$, $g_{\mu}$ is an open immersion.*

Since the homomorphism $\phi : \mathcal{C} \to f_{*}(\mathcal{O}_{X})$ is injective, it follows from `(8.12.1)` that if
$g$ is an immersion, it is an open immersion and $g(X)$ is dense in $Z$, and likewise for $g_{\lambda}$. The fact that
a) implies a') also follows from `(8.12.1)`, applied with $Z$ replaced by $Y'$ and $g$ by $f'$ ($Y'$ being finite, hence
affine over $Y$): indeed, if `Y''` is the closed image of $X$ under $f'$, `Y''` is finite over $Y$ and $f'$ factors as
$X \to^{f''} Y'' \to^{j} Y'$, where $j$ is the canonical injection, and `f''` is an immersion `(I, 4.1.10)`; it then
follows from `(8.12.1)` that `f''` is an open immersion.

The equivalence of b) and c) follows from `(8.12.2)`, as does the fact that $g_{\lambda}$ is then an immersion for
$\lambda$ large enough. It is clear that c) implies a), since $Z_{\lambda}$ is finite over $Y$ `(II, 6.3.4` and
`6.1.2)`. Finally let us show that a) implies c). One saw above that one can suppose that $Y'$ is the closed image of
$X$ under $f'$, and it then follows from `(8.12.1)` that, setting $\mathcal{B}' = u_{*}(\mathcal{O}_{Y'})$, so that $Y'$
identifies with $\operatorname{Spec}(\mathcal{B}')$, the homomorphism $\phi' : \mathcal{B}' \to \mathcal{B} =
f_{*}(\mathcal{O}_{X})$ is injective. But since by hypothesis $\mathcal{B}'$ is a finite $\mathcal{O}_{Y}$-Algebra, it
identifies by definition of $\mathcal{B}$ with one of the sub-$\mathcal{O}_{Y}$-Algebras $\mathcal{C}_{\lambda}$, which
proves c).

We say that a morphism $f : X \to Y$, where $Y$ is quasi-compact and quasi-separated, is *pseudo-finite* if it is of
finite type and satisfies condition a) of `(8.12.3)` (in which case it is necessarily separated).

**Corollary (8.12.4).**

<!-- label: IV.8.12.4 -->

*Let $Y$ be a quasi-compact and quasi-separated prescheme, $f : X \to Y$ a morphism.*

<!-- original page 45 -->

*(i) Suppose $f$ pseudo-finite. Then, for every morphism $Y' \to Y$, where $Y'$ is quasi-compact and quasi-separated,
$f_{(Y')} : X' = X_{(Y')} \to Y'$ is pseudo-finite.*

*(ii) Let $(U_{\lambda})$ be a cover of $Y$ formed of quasi-compact opens. In order that $f$ be pseudo-finite, it is
necessary and sufficient that for every $\lambda$, the restriction $f_{\lambda} : f^{-1}(U_{\lambda}) \to U_{\lambda}$
of $f$ be a pseudo-finite morphism.*

*(iii) Suppose moreover $Y$ Noetherian, and $f$ of finite type. Then, in order that $f$ be pseudo-finite, it is
necessary and sufficient that, for every $y \in Y$, the morphism $f_{y} = f \times 1 : X_{y} = X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{y}) \to \operatorname{Spec}(\mathcal{O}_{y})$ be so.*

(i) It is clear that $f_{(Y')}$ is of finite type `(1.5.4)`; moreover, a factorization $X \to^{f'} Z \to^{u} Y$ where
$g$ is an immersion and $u$ is finite, gives a factorization $X' \to Z' \to Y'$ of $f_{(Y')}$, where $Z' = Z_{(Y')}$,
$g' = g_{(Y')}$ and $u' = u_{(Y')}$; $g'$ is an immersion `(I, 4.3.2)` and $u'$ is finite `(II, 6.1.5)`; hence
$f_{(Y')}$ is pseudo-finite.

(ii) The condition is necessary by virtue of (i), the $U_{\lambda}$ being quasi-separated since $Y$ is. To see that it
is sufficient, observe (with the notation of `(8.12.3)`) that if one sets $X_{\lambda} = f^{-1}(U_{\lambda})$, one has
$\mathcal{B}|U_{\lambda} = (f_{\lambda})_{*}(\mathcal{O}_{X_{\lambda}})$, $\mathcal{C}|U_{\lambda}$ is the integral
closure of $\mathcal{O}_{U_{\lambda}}$ in $\mathcal{B}|U_{\lambda}$, and consequently, if $h : Z \to Y$ is the canonical
morphism, $Z_{\lambda}' = \operatorname{Spec}(\mathcal{C}|U_{\lambda})$ identifies with $h^{-1}(U_{\lambda})$. Now, in
order that $g : X \to Z$ be an immersion, it is necessary and sufficient that for every $\lambda$, the restriction
$g_{\lambda} : f^{-1}(U_{\lambda}) \to h^{-1}(U_{\lambda})$ of $g$ be so `(I, 4.2.4)`. This entails the conclusion by
virtue of `(8.12.3)`.

(iii) It suffices, by virtue of (ii), to prove that $y$ admits a neighbourhood $U$ such that the restriction $f^{-1}(U)
\to U$ of $f$ is a pseudo-finite morphism. Denote by $(U_{\lambda})$ the decreasing filtered projective system of affine
open neighbourhoods of $y$, and apply the method of `(8.1.2, a))`. Since $Y$ is Noetherian, the restrictions
$f_{\lambda} : f^{-1}(U_{\lambda}) \to U_{\lambda}$ of $f$ are of finite presentation, and so is $f_{y}$. By hypothesis
$f_{y}$ factors as $X_{y} \to^{g_{y}} Z_{y} \to^{u_{y}} \operatorname{Spec}(\mathcal{O}_{y})$, where $u_{y}$ is finite
and $g_{y}$ is an immersion. Since $\mathcal{O}_{y}$ is Noetherian, so is $Z_{y}$, and since $Z_{y}$ is of finite
presentation over $\operatorname{Spec}(\mathcal{O}_{y})$, there exist a $\lambda$ and a morphism of finite presentation
$u_{\lambda} : Z_{\lambda} \to U_{\lambda}$ such that $Z_{y}$ identifies with $Z_{\lambda} \times_{U_{\lambda}}
\operatorname{Spec}(\mathcal{O}_{y})$ and $u_{y}$ with $u_{\lambda} \times 1$ `(8.8.2, (ii))`; moreover, there exists a
morphism $g_{\lambda} : X_{\lambda} \to Z_{\lambda}$ such that $g_{y} = g_{\lambda} \times 1$ and $f_{\lambda} =
u_{\lambda} \circ g_{\lambda}$ `(8.8.2, (i))`. Moreover, one can suppose $\lambda$ chosen so that $g_{\lambda}$ is an
immersion and $u_{\lambda}$ a finite morphism `(8.10.5, (ii)` and `(x))`, which proves that $f_{\lambda}$ is
pseudo-finite.

**(8.12.5)**

<!-- label: IV.8.12.5 -->

We can now give of Zariski's *Main Theorem* `(III, 4.4.3)` a demonstration not using the cohomological results of
"global" nature of chap. III, but appealing on the other hand to the finer properties of Noetherian local rings; we
shall moreover generalize the statement of the theorem by ridding it of Noetherian hypotheses:

**Theorem (8.12.6) (Zariski's *Main Theorem*).**

<!-- label: IV.8.12.6 -->

*Let $Y$ be a quasi-compact and quasi-separated prescheme. If a morphism $f : X \to Y$ is quasi-finite, separated and of
finite presentation, there exists a factorization of $f$*

```text
(8.12.6.1)                          X ──f'──→ Y' ──u──→ Y
```

*where $f'$ is an open immersion and $u$ a finite morphism.*

<!-- original page 46 -->

By virtue of `(8.12.4, (ii))` and of the local character (on $Y$) of the notions of quasi-finite, separated and finite
presentation morphisms, one may restrict to the case where $Y = \operatorname{Spec}(A)$ is affine. Applying `(8.9.1)`,
one may suppose that there is a sub-ring `A_0` of $A$, which is a $Z$-algebra of finite type, and an $A$-isomorphism
$X_{0} \otimes_{A_{0}} A \xrightarrow{\sim} X$, $f$ being identified by this isomorphism with $f_{0} \times 1$, where
$f_{0} : X_{0} \to \operatorname{Spec}(A_{0})$ is a morphism of finite type; moreover `(8.10.5, (v)` and `(xi))` one may
suppose that $f_{0}$ is separated and quasi-finite; if one proves that $f_{0}$ is pseudo-finite, so will $f$ be by
`(8.12.4, (i))`. Since `A_0` is then Noetherian and the notions of morphism of finite type, separated and quasi-finite
are preserved by base change, it follows from `(8.12.4, (iii))` that one may even suppose that $A$ is a local ring,
essentially of finite type over $Z$ `(1.3.8)`. Set $n = \dim(A)$, and proceed by induction on $n$; for $n = 0$, the
theorem is evident, $A$ being a field and the morphism $f$ being already finite `(II, 6.2.2)`. Set $B = \Gamma(X,
\mathcal{O}_{X})$; denote by $C$ the integral closure of $A$ in $B$, set $Z = \operatorname{Spec}(C)$ and let $g : X \to
Z$ be the $Y$-morphism corresponding to the canonical injective $A$-homomorphism $C \to B$; by virtue of `(8.12.3)`, it
remains to show that $g$ is an open immersion. Let $a$ be the closed point of $Y$, and let $U = Y - {a}$; $U$ is
Noetherian and all its local rings are essentially of finite type over $Z$ and of dimension $< n$; taking into account
the induction hypothesis, and `(8.12.4, (iii))`, one sees that the restriction $f^{-1}(U) \to U$ of $f$ is a
pseudo-finite morphism. One concludes `(8.12.3)` that, if $h : Z \to Y$ is the structure morphism, the restriction
$f^{-1}(U) \to h^{-1}(U)$ of $g$ is an open immersion. Set $A' = \hat{A}$, $Y' = \operatorname{Spec}(A')$, $X' =
X_{(Y')}$, $f' = f_{(Y')} : X' \to Y'$. Since the canonical morphism $u : Y' \to Y$ is flat, it follows from `(2.3.1)`
that $B' = \Gamma(X', \mathcal{O}_{X'})$ identifies with the $A'$-algebra $B \otimes_{A} A'$. On the other hand, since
$A$ is an excellent local ring `(7.8.3)`, the morphism $u : Y' \to Y$ is regular, and a fortiori normal, and
consequently `(6.14.4)` the integral closure of $A'$ in $B'$ is equal to $C' = C \otimes_{A} A'$. One sees therefore
that $Z' = \operatorname{Spec}(C')$ is equal to $Z_{(Y')}$ and the morphism $g' : X' \to Z'$ coming from the injection
$C' \to B'$ is equal to $g_{(Y')}$. Since $u : Y' \to Y$ is faithfully flat and quasi-compact, to prove that $g$ is an
open immersion, it suffices to prove that $g'$ is an open immersion `(2.7.1, (x))`. Note now that $u^{-1}(a)$ is reduced
to the closed point $a'$ of $Y'$ and consequently $U' = Y' - {a'} = u^{-1}(U)$. If $h' : Z' \to Y'$ is the canonical
morphism, the fact that the restriction $f^{-1}(U) \to h^{-1}(U)$ of $g$ is an open immersion entails that this is also
so of the restriction $f'^{-1}(U') \to h'^{-1}(U')$ of $g'$. Note now that $f'$ is a separated and quasi-finite morphism
`(II, 6.2.4)`; since $A'$ is complete, one deduces from `(II, 6.2.6)` that $X'$ is $Y'$-isomorphic to a sum $X_{1}'
\sqcup X_{2}'$, where the restriction $f'|X_{1}' = f_{1}' : X_{1}' \to Y'$ is a finite morphism, and $X_{2}' \subset
f'^{-1}(U')$. It follows that $B'$ is direct composition of the two $A'$-algebras $\Gamma(X_{1}', \mathcal{O}_{X_{1}'})
= B_{1}'$ and $\Gamma(X_{2}', \mathcal{O}_{X_{2}'}) = B_{2}'$; one concludes at once that the integral closure $C'$ of
$A'$ in $B'$ is direct composition of the integral closures $C_{1}'$, $C_{2}'$ of $A'$ in $B_{1}'$, $B_{2}'$
respectively, whence $Z' = Z_{1}' \sqcup Z_{2}'$, where $Z_{i}' = \operatorname{Spec}(C_{i}')$ $(i = 1, 2)$; and the
canonical morphism $g' : X' \to Z'$ is such that $g'|X_{i}'$ is the canonical morphism $g_{i}' : X_{i}' \to Z_{i}'$ $(i
= 1, 2)$. But since $B_{1}'$ is already a finite $A'$-algebra, one has $C_{1}' = B_{1}'$, and $g_{1}'$ is therefore an
isomorphism. On the other hand, since $X_{2}' \subset f'^{-1}(U')$ and is open in $f'^{-1}(U')$, one knows

<!-- original page 47 -->

already that $g_{2}'$ is an open immersion. One concludes indeed that $g'$ is an open immersion, Q.E.D.

**Remark (8.12.7).**

<!-- label: IV.8.12.7 -->

When, in `(8.12.6)`, one supposes that $Y$ is an affine scheme, the demonstration by reduction to the Noetherian case
shows that, in the factorization `(8.12.6.1)`, the morphisms $f'$ and $u$ are also morphisms of finite presentation
`(1.6.2)`.

**Corollary (8.12.8).**

<!-- label: IV.8.12.8 -->

*Let $Y$ be a quasi-compact scheme such that there exists an ample $\mathcal{O}_{Y}$-Module `(II, 4.5.3)`, $f : X \to Y$
a quasi-finite and quasi-projective morphism. Then there exists a factorization of $f$ as*

```text
                                X ──f'──→ Y' ──u──→ Y
```

*where $f'$ is an open immersion and $u$ a finite morphism.*

The hypothesis entails that $X$ identifies with a quasi-compact sub-$Y$-scheme of a $Y$-scheme of the form $Z =
\mathbb{P}^{r}_{Y}$ `(II, 5.3.3)`. There is consequently a quasi-compact open neighbourhood $U$ of $X$ in $Z$ such that
$X$ is closed in $U$; since $Z$ is a scheme, the canonical injection $U \to Z$ is a morphism of finite presentation
`((1.2.7)` and `(1.6.2))`, hence the composite morphism $g : U \to Z \to Y$ is also a morphism of finite presentation
(the fact that $\mathbb{P}^{r}_{Y}$ is of finite presentation over $Y$ resulting at once from the definition
`(II, 4.1.1)`). Let $\mathcal{I}$ be the quasi-coherent Ideal of $\mathcal{O}_{U}$ defining the closed sub-prescheme
$X$; since $U$ is a quasi-compact scheme, $\mathcal{I}$ is the filtered inductive limit of its quasi-coherent sub-Ideals
of finite type $\mathcal{I}_{\lambda}$ `(I, 9.4.9)`. If $X_{\lambda}$ is the closed sub-prescheme of $U$ defined by
$\mathcal{I}_{\lambda}$, one has consequently $X = \bigcap X_{\lambda}$. For every $y \in Y$, one therefore has
$f^{-1}(y) = \bigcap (X_{\lambda} \cap g^{-1}(y))$, and since the sets $X_{\lambda} \cap g^{-1}(y)$ are closed in the
Noetherian space $g^{-1}(y)$, there exists for every $y$ an index $\lambda(y)$ such that $f^{-1}(y) = X_{\lambda(y)}
\cap g^{-1}(y)$. Denote by $E_{\lambda}$ the set of $y \in Y$ such that the fibre $X_{\lambda} \cap g^{-1}(y)$ of the
restriction of $g$ to $X_{\lambda}$ is a finite $k(y)$-prescheme. The hypothesis that $f$ is quasi-finite entails, by
virtue of what precedes, that $Y = \bigcup E_{\lambda}$. Now, each of the $X_{\lambda}$ is, by definition, of finite
presentation over $Y$; it therefore follows from `(9.2.3)` and `(9.2.6)` (\*) that the $E_{\lambda}$ are constructible
sets in the scheme $Y$; since they form an increasing filtered family, there exists an index $\lambda$ such that
$E_{\lambda} = Y$ `(1.9.9)`, and for this index $\lambda$, the morphism $f_{\lambda} : X_{\lambda} \to Y$, restriction
of $g$ to $X_{\lambda}$, is therefore quasi-finite. Since it is of finite presentation and separated, one may apply
`(8.12.6)` to it, and $f_{\lambda}$ factors therefore as

```text
                                X_λ ──j_λ──→ Y_λ ──u_λ──→ Y
```

where $j_{\lambda}$ is an immersion and $u_{\lambda}$ a finite morphism. Since $X$ is a closed sub-prescheme of
$X_{\lambda}$, one has thus proved that $f$ has property `(8.12.3, a))`, whence the corollary by virtue of the
equivalence of `(8.12.3, a))` and `(8.12.3, a'))`.

The reader will verify that the corollaries `(8.12.8)` to `(8.12.11)` are not used in §9.

<!-- original page 48 -->

**Corollary (8.12.9).**

<!-- label: IV.8.12.9 -->

*Let $f : X \to Y$ be a locally quasi-finite morphism (Errm, 20). For every $x \in X$ there exists an open neighbourhood
$U$ of $x$ in $X$, an open neighbourhood $V$ of $y = f(x)$ in $Y$, such that $f(U) \subset V$ and a factorization*

```text
                                U ──f'──→ V' ──u──→ V
```

*of the restriction of $f$ to $U$, where $f'$ is an open immersion and $u$ a finite morphism.*

It obviously suffices to take for $V$ an affine neighbourhood of $y$ in $Y$, for $U$ an affine neighbourhood of $x$ in
$X$ contained in $f^{-1}(V)$ and such that $f|U$ is quasi-finite. The morphism $U \to V$ restriction of $f$ being then
affine (hence quasi-projective), one may apply `(8.12.8)` to it.

**Corollary (8.12.10).**

<!-- label: IV.8.12.10 -->

*Let $Y$ be an integral and normal prescheme, $X$ an integral prescheme, $f : X \to Y$ a birational and locally
quasi-finite morphism (Errm, 20). Then $f$ is a local isomorphism; in order that $f$ be an open immersion, it is
necessary and sufficient that $f$ be moreover separated.*

The second assertion results at once from the first and from `(I, 8.2.8)`. To prove the first assertion, one may suppose
$X$ and $Y$ affine and $f$ quasi-finite; consider the factorization $f = u \circ f'$ of `(8.12.8)`, which permits to
identify $X$ by $f'$ with a sub-prescheme induced on an open of $Y'$. Since $X$ is integral, one may, by virtue of
`(I, 5.2.3)`, replace $Y'$ by the reduced sub-prescheme of $Y'$ having $X$ as underlying space, hence one may also
suppose that $Y'$ is integral. Moreover, since $f$ is birational, so is $u$. The conclusion results then from the
following lemma:

**Lemma (8.12.10.1).**

<!-- label: IV.8.12.10.1 -->

*Let $Y'$ be an integral prescheme, $Y$ an integral and normal prescheme; then a finite and birational morphism $u : Y'
\to Y$ is an isomorphism.*

Set indeed $\mathcal{A} = u_{*}(\mathcal{O}_{Y'})$, so that $\mathcal{A}$ is a finite $\mathcal{O}_{Y}$-Algebra, $Y'$
identifying with $\operatorname{Spec}(\mathcal{A})$ `(II, 1.3.6)`. If $R(Y)$ is the field of rational functions of $Y$,
one has therefore, for every $y \in Y$, $\mathcal{O}_{y} \subset \mathcal{A}_{y} \subset R(Y)$; but since the ring
$\mathcal{O}_{y}$ is by hypothesis integrally closed and has $R(Y)$ as field of fractions, one necessarily has
$\mathcal{A}_{y} = \mathcal{O}_{y}$, whence the lemma.

**Corollary (8.12.11).**

<!-- label: IV.8.12.11 -->

*Let $Y$ be an integral prescheme, $X$ an integral and normal prescheme, $f : X \to Y$ a dominant and locally
quasi-finite morphism. Let $K$ and $L$ (extension of $K$) be the fields of rational functions of $Y$ and $X$
respectively, and let $Y'$ be the integral closure of $Y$ relative to $L$ `(II, 6.3.4)`; then $f$ factors in a unique
way as $f : X \to^{f'} Y' \to^{u} Y$, where $f'$ is birational, and corresponds to the identity automorphism of $L$;
$f'$ is then a local isomorphism, and in order that $f'$ be an open immersion, it is necessary and sufficient that $f$
be separated.*

The existence and uniqueness of the factorization of $f$ result from `(II, 6.3.9)`. It follows from `(II, 6.2.4, (v))`,
by reducing to the affine case, that $f'$ is locally quasi-finite; moreover, it follows from `(I, 5.5.1)` that, in order
that $f'$ be separated, it is necessary and sufficient that $f$ be so, since $u$ is affine, hence separated; the last
two assertions are therefore consequences of `(8.12.10)` applied to $f'$.

<!-- original page 49 -->

### 8.13. Translation in terms of pro-objects

The following proposition is essentially equivalent to `(8.8.2, (i))`:

**Proposition (8.13.1).**

<!-- label: IV.8.13.1 -->

*Let $S$ be a prescheme, $(X_{\lambda}, v_{\lambda \mu})$ a filtered projective system of $S$-preschemes; suppose there
exists $\alpha$ such that $v_{\alpha \lambda}$ is an affine morphism for every $\lambda \geq \alpha$ (which entails
`(II, 1.6.2)` that $v_{\lambda \mu}$ is affine for $\alpha \leq \lambda \leq \mu$), so that the projective limit $X =
\lim X_{\lambda}$ exists in the category of $S$-preschemes `(8.2.3)`. Let $Y$ be an $S$-prescheme, and, for every
$\lambda \geq \alpha$, let $\theta_{\lambda} : \operatorname{Hom}_{S}(X_{\lambda}, Y) \to \operatorname{Hom}_{S}(X, Y)$
be the application which, to every $S$-morphism $f_{\lambda} : X_{\lambda} \to Y$, makes correspond $f = f_{\lambda}
\circ v_{\lambda}$, where $v_{\lambda} : X \to X_{\lambda}$ is the canonical morphism. The family $(\theta_{\lambda})$
is an inductive system of applications, which therefore defines a canonical application*

```text
(8.13.1.1)                lim Hom_S(X_λ, Y) → Hom_S(X, Y).
```

*Suppose $X_{\alpha}$ quasi-compact (resp. quasi-compact and quasi-separated), and the structure morphism $Y \to S$
locally of finite type (resp. locally of finite presentation). Then the application `(8.13.1.1)` is injective (resp.
bijective).*

Set indeed, for $\lambda \geq \alpha$, $Z_{\lambda} = Y \times_{S} X_{\lambda}$, so that one has $Z_{\lambda} =
Z_{\alpha} \times_{X_{\alpha}} X_{\lambda}$. Set likewise $Z = Y \times_{S} X = Z_{\alpha} \times_{X_{\alpha}} X$; one
then knows `(8.2.5)` that, if one also sets $w_{\lambda \mu} = 1 \times v_{\lambda \mu} : Z_{\mu} \to Z_{\lambda}$ for
$\alpha \leq \lambda \leq \mu$ and $w_{\lambda} = 1 \times v_{\lambda} : Z \to Z_{\lambda}$ for $\alpha \leq \lambda$,
$Z$ is projective limit of the projective system $(Z_{\lambda}, w_{\lambda \mu})$ and the $w_{\lambda}$ are the
corresponding canonical morphisms. Note on the other hand that the morphism $Z_{\alpha} \to X_{\alpha}$ is locally of
finite type (resp. locally of finite presentation) `(1.3.4` and `1.4.3)`. Finally, one knows that one has

```text
            Hom_S(X_λ, Y) = Hom_{X_λ}(X_λ, Z_λ)    and    Hom_S(X, Y) = Hom_X(X, Z)
```

`(I, 3.3.14)`. It now suffices to apply `(8.8.2, (i))` taking $X_{\lambda} = S_{\lambda}$ and replacing $Y_{\lambda}$ by
$Z_{\lambda}$.

**Corollary (8.13.2).**

<!-- label: IV.8.13.2 -->

*With the notation of `(8.13.1)`, suppose $X_{\alpha}$ quasi-compact and quasi-separated, and the $v_{\alpha \lambda}$
affine for $\alpha \leq \lambda$; suppose moreover that $Y = \lim Y_{\rho}$, where $(Y_{\rho}, t_{\rho \sigma})$ is a
filtered projective system of $S$-preschemes such that, for each $\rho$, the structure morphism $Y_{\rho} \to S$ is
locally of finite presentation. One then has a canonical bijection*

```text
(8.13.2.1)              Hom_S(X, Y) ⥲ lim_ρ (lim_λ Hom_S(X_λ, Y_ρ)).
```

Indeed, the fact that $Y$ is projective limit of the $Y_{\rho}$ entails in particular that the canonical application
`Hom_S(X, Y) → lim_ρ Hom_S(X, Y_ρ)` is bijective; and on the other hand, the hypotheses entail, for each $\rho$, the
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
omit until then the reading of the end of this number). Given a category $\mathcal{C}$, the category $Pro(\mathcal{C})$
of pro-objects of $\mathcal{C}$ has as objects the projective systems (in the universe in which one places oneself) $X =
(X_{\mu})_{\mu \in M}$ of objects of $\mathcal{C}$ whose index sets (depending on the projective system considered) are
assumed pre-ordered filtered. Given two such pro-objects $X = (X_{\mu})_{\mu \in M}$, $X' = (X_{\mu'}')_{\mu' \in M'}$,
the morphisms from $X$ to $X'$ are by definition the elements of the set `lim_{μ'}(lim_μ Hom(X_μ, X_{μ'}'))`; the
verification of the fact that one may take these sets for sets of morphisms is immediate, the composition of systems of
morphisms $u^{\mu}_{\mu'} : X_{\mu} \to X_{\mu'}'$, $u^{\mu'}_{\mu''} : X_{\mu'}' \to X_{\mu''}''$, which are inductive
in the upper index and projective in the lower index, being done "argument by argument", in other words by considering
the system of the $u^{\mu}_{\mu''} = u^{\mu'}_{\mu''} \circ u^{\mu}_{\mu'}$.

**(8.13.4)**

<!-- label: IV.8.13.4 -->

Consider then a quasi-compact and quasi-separated prescheme $S$, and denote by $\mathcal{C}$ the full sub-category of
the category $(Sch)_{/S}$ of $S$-preschemes formed by the $S$-preschemes $X$ having the following property: the
structure morphism $X \to S$ factors as $X \to^{g} X_{0} \to^{f} S$, where $g : X \to X_{0}$ is affine and $f : X_{0}
\to S$ of finite presentation; we say for brevity that the preschemes of $\mathcal{C}$ are *essentially affine* over
$S$.

Consider on the other hand the full sub-category $\mathcal{C}_{0}'$ of $(Sch)_{/S}$ formed by the $S$-preschemes of
finite presentation, and the category $Pro(\mathcal{C}_{0}')$ of pro-objects of $\mathcal{C}_{0}'$. We say that an
object $X = (X_{\mu})_{\mu \in M}$ of $Pro(\mathcal{C}_{0}')$ is *essentially affine* if there exists $\gamma \in M$
such that for every $\mu \geq \gamma$, the transition morphism $v_{\gamma \mu} : X_{\mu} \to X_{\gamma}$ is affine
(which entails that for $\gamma \leq \mu \leq \nu$, $v_{\mu \nu} : X_{\nu} \to X_{\mu}$ is affine). One notes that an
object of $Pro(\mathcal{C}_{0}')$ isomorphic to an essentially affine object is not necessarily essentially affine
itself. We shall denote by $\mathcal{C}'$ the full sub-category of $Pro(\mathcal{C}_{0}')$ formed by the essentially
affine pro-objects of $\mathcal{C}_{0}'$.

This being so, it follows from `(8.2.2)` and `(8.2.3)` that for every object $X = (X_{\mu})_{\mu \in M}$ of
$\mathcal{C}'$, the $S$-prescheme $X = \lim X_{\mu}$ exists; moreover, since, for $\mu$ large enough, the morphism $X
\to X_{\mu}$ is affine `(8.2.2)`, $X$ is essentially affine over $S$ by definition. Set $X = L(X)$; let us show that one
has thus defined a *canonical functor*

$$ (8.13.4.1) L : \mathcal{C}' \to \mathcal{C}. $$

One has in effect, for two objects $X = (X_{\mu})$, $X' = (X_{\mu'}')$ of $\mathcal{C}'$, a canonical application for
each $\mu'$

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

obviously functorial in $X$ and $X'$, and which completes the definition of the functor $L$.

**Proposition (8.13.5).**

<!-- label: IV.8.13.5 -->

*The hypotheses and notation being those of `(8.13.4)`, the functor $L$ is fully faithful. If moreover $S$ is a
Noetherian prescheme (which already implies that $S$ is quasi-compact and quasi-separated `(1.2.8)`), $L$ is an
equivalence of categories.*

To say that $L$ is fully faithful means that the application `(8.13.4.2)` is bijective for every $X$, $X'$ in
$\mathcal{C}'$, which is a particular case of `(8.13.2)`: indeed, the structure morphisms $X_{\mu} \to S$ being of
finite presentation, are in particular quasi-compact and quasi-separated, hence the $X_{\mu}$ are quasi-compact and
quasi-separated.

To show that when $S$ is Noetherian $L$ is an equivalence of categories, it suffices, since one already knows that $L$
is fully faithful, to prove that every essentially affine $S$-prescheme $X$ is $S$-isomorphic to an object of the form
$L(X)$ where $X \in \mathcal{C}'$ $(0_{III}, 8.1.5)$. Now, by hypothesis there is a factorization $X \to^{g} X_{0}
\to^{f} S$ of the structure morphism, $f$ being of finite presentation and $g$ affine. One may therefore write $X =
\operatorname{Spec}(\mathcal{A})$, where $\mathcal{A}$ is a quasi-coherent $\mathcal{O}_{X_{0}}$-Algebra `(II, 1.3.1)`.
Now, since `X_0` is Noetherian (since this is so for $S$ and $f$ is of finite type), $\mathcal{A}$ is the filtered
inductive limit of the family $(\mathcal{A}_{\lambda})$ of its quasi-coherent sub-$\mathcal{O}_{X_{0}}$- Algebras of
finite type `(I, 9.6.6)`. Set $X_{\lambda} = \operatorname{Spec}(\mathcal{A}_{\lambda})$; the morphisms $X_{\lambda} \to
X_{0}$ are of finite type, hence of finite presentation since `X_0` is Noetherian, and consequently so are the composite
morphisms $X_{\lambda} \to X_{0} \to S$ `(1.6.2)`; in other words, the $X_{\lambda}$ belong to $\mathcal{C}_{0}'$, and
since the morphisms $X_{\lambda} \to X_{0}$ are affine, $X = (X_{\lambda})$ is an object of $\mathcal{C}'$ whose
projective limit exists and is $S$-isomorphic to $X$ by virtue of `(8.2.2)`. This finishes the demonstration.

**Remark (8.13.6).**

<!-- label: IV.8.13.6 -->

It follows from `(1.6.2)` and from `(II, 1.6.2)` that if $X$ and $Y$ are essentially affine over $S$, then so is $X
\times_{S} Y$. One concludes for example $(0_{III}, 8.2.5)$ that a $\mathcal{C}$-group is nothing other than a
$(Sch)_{/S}$-group which is an essentially affine prescheme over $S$. On the other hand, finite products exist in the
category $\mathcal{C}'$: indeed, if $X = (X_{\mu})_{\mu \in M}$, $Y = (Y_{\rho})_{\rho \in R}$ are two objects of
$\mathcal{C}'$, the products $X_{\mu} \times_{S} Y_{\rho}$ are $S$-preschemes of finite presentation, and taking for
transition morphisms $X_{\nu} \times_{S} Y_{\sigma} \to X_{\mu} \times_{S} Y_{\rho}$ the products of the transition
morphisms $X_{\nu} \to X_{\mu}$ and $Y_{\sigma} \to Y_{\rho}$, one sees at once that $(X_{\mu} \times_{S} Y_{\rho})$ is
the product of $X$ and $Y$ in $Pro(\mathcal{C}_{0}')$; moreover `(II, 1.6.2)` the transition morphisms thus defined are
affine for $\mu$ and $\rho$ large enough, hence the product $X \times Y$ thus defined belongs indeed to $\mathcal{C}'$.
One concludes then as above that a $\mathcal{C}'$-group is a $Pro(\mathcal{C}_{0}')$-group which is essentially affine.
One deduces therefore from `(8.13.5)` that the categories of $\mathcal{C}'$-groups and of $\mathcal{C}$-groups are
equivalent when $S$ is Noetherian. It seems plausible that when $S$ is the spectrum of a field $k$, the category of
$\mathcal{C}$-groups is equivalent to that of $\mathcal{K}$-groups, where $\mathcal{K}$ is the category of quasi-compact
$S$-preschemes; in other words, every group prescheme over $k$ that is quasi-compact would be essentially affine. On the
other hand, if one denotes

<!-- original page 52 -->

by $\mathcal{C}_{0}'-gr$ the category of $\mathcal{C}_{0}'$-groups, it is plausible that the category of
$\mathcal{C}'$-groups is equivalent to the full sub-category of $Pro(\mathcal{C}_{0}'-gr)$ formed by the "essentially
affine pro-algebraic groups", that is to say the projective systems $G = (G_{\mu})_{\mu \in M}$, where the $G_{\mu}$ are
algebraic groups over $k$ and the transition morphisms $G_{\nu} \to G_{\mu}$ are affine for $\mu$ large enough (which
one may also express by saying that $G$ is an extension of an algebraic group by an affine pro-algebraic group). The
conjunction of these two conjectures is moreover equivalent to the following: every group prescheme quasi-compact over
$k$ is an "extension" of an "algebraic group" (i.e. a group prescheme of finite type over $k$) by an affine group
prescheme over $k$.

The only pro-algebraic groups encountered in practice up to the present being in fact essentially affine, there will
therefore no doubt be advantage in substituting for the study of general pro-algebraic groups (introduced and studied by
Serre [40]) that of quasi-compact group schemes over $k$, whose definition is conceptually simpler.

### 8.14. Characterization of a prescheme locally of finite presentation over another, in terms of the functor it represents

**(8.14.1)**

<!-- label: IV.8.14.1 -->

Given a prescheme $S$, we say again, as in `(8.13.4)`, that a filtered projective system $(X_{\lambda}, v_{\lambda
\mu})$ of $S$-preschemes is *essentially affine* if there exists $\alpha$ such that $v_{\alpha \lambda}$ is an affine
morphism for $\lambda \geq \alpha$.

The following statement, which will above all be useful in chap. V, makes `(8.8.2, (i))` more precise by furnishing a
converse:

**Proposition (8.14.2).**

<!-- label: IV.8.14.2 -->

*Let $S$ be a prescheme, $f : X \to S$ a morphism. For every $S$-prescheme $T$, set*

$$ h_{X}(T) = \operatorname{Hom}_{S}(T, X) $$

*so that $h_{X}$ is a contravariant functor from the category $(Sch)_{/S}$ of $S$-preschemes to the category Ens of sets
$(0_{III}, 8.1.1)$, and $X$ an object representing this functor $(0_{III}, 8.1.8)$. The following conditions are
equivalent:*

*a) $f$ is locally of finite presentation.*

*b) For every filtered projective system $(Z_{\lambda})$ of $S$-preschemes, essentially affine `(8.13.4)` and formed of
quasi-compact and quasi-separated preschemes, the canonical application `(8.13.1.1)`*

```text
(8.14.2.1)                          lim h_X(Z_λ) → h_X(lim Z_λ)
```

*is bijective.*

*c) For every filtered projective system $(Z_{\lambda})$ of $S$-preschemes such that the $Z_{\lambda}$ are affine
schemes, the application `(8.14.2.1)` is bijective.*

*c') For every affine open $U$ of $S$ and every filtered projective system $(Z_{\lambda})$ of $U$-preschemes such that
the $Z_{\lambda}$ are affine schemes, the application `(8.14.2.1)` is bijective.*

The fact that a) implies b) is none other than `(8.13.1)`; it is trivial that b) implies c) and that c) implies c'). It
remains to see that c') entails a), and since property a) is local on $S$, one may restrict to the case where $S$ is
affine.

<!-- original page 53 -->

Suppose first that $X$ is also affine; the assertion to be proved is then equivalent to the

**Corollary (8.14.2.2).**

<!-- label: IV.8.14.2.2 -->

*Let $A$ be a ring, $B$ an $A$-algebra. In order that, for every filtered inductive system $(C_{\lambda})$ of
$A$-algebras, the canonical application*

```text
(8.14.2.3)             lim Hom_{A-alg.}(B, C_λ) → Hom_{A-alg.}(B, lim C_λ)
```

*be bijective, it is necessary and sufficient that $B$ be an $A$-algebra of finite presentation.*

It remains only to show that the condition is necessary. Take first for $(C_{\lambda})$ the filtered inductive system of
sub-$A$-algebras of finite type of $B$, so that $\lim C_{\lambda} = B$. The fact that `(8.14.2.3)` is bijective entails
in particular that the identity application `1_B` factors as $B \to C_{\lambda} \to B$ for a suitable $\lambda$, which
entails $C_{\lambda} = B$, hence $B$ is an $A$-algebra of finite type. Set then $B = C/\mathfrak{J}$, where $C =
A[T_{1}, \cdots, T_{n}]$ and $\mathfrak{J}$ is an ideal of $C$. Then $\mathfrak{J}$ is the filtered inductive limit of
the ideals of finite type $\mathfrak{J}_{\lambda} \subset \mathfrak{J}$ of $C$; setting $C_{\lambda} =
C/\mathfrak{J}_{\lambda}$, and using the exactness of the functor `lim`, one sees that $B$ is again isomorphic to the
inductive limit of the filtered inductive system $(C_{\lambda})$. There exists therefore a $\lambda$ and an
$A$-homomorphism $u : B \to C_{\lambda}$ such that the composite $B \to^{u} C_{\lambda} \to^{p_{\lambda}} B$ (where
$p_{\lambda}$ is the canonical homomorphism) is the identity. Let $q_{\lambda} : C \to C_{\lambda}$ be the canonical
homomorphism, and set $t_{i} = p_{\lambda}(q_{\lambda}(T_{i}))$; one has therefore $p_{\lambda}(u(t_{i})) =
p_{\lambda}(q_{\lambda}(T_{i}))$, in other words $u(t_{i}) - q_{\lambda}(T_{i}) \in
\mathfrak{J}/\mathfrak{J}_{\lambda}$. There exists therefore $\mu \geq \lambda$ such that the $n$ elements $u(t_{i}) -
q_{\lambda}(T_{i})$ belong to $\mathfrak{J}_{\mu}/\mathfrak{J}_{\lambda}$ $(1 \leq i \leq n)$; if $p_{\lambda \mu} :
C_{\lambda} \to C_{\mu}$ is the canonical homomorphism, one has consequently $p_{\lambda \mu}(u(t_{i})) = p_{\lambda
\mu}(q_{\lambda}(T_{i})) = q_{\mu}(T_{i})$. Replacing $\lambda$ by $\mu$ and $u$ by $p_{\lambda \mu} \circ u$, one may
therefore suppose that $u(t_{i}) = q_{\lambda}(T_{i})$ for every $i$, and if $r = p_{\lambda} \circ q_{\lambda}$ is the
canonical homomorphism $C \to C/\mathfrak{J} = B$, one may therefore write $u(r(T_{i})) = q_{\lambda}(T_{i})$ for every
$i$, whence $q_{\lambda} = u \circ r$. But this entails necessarily that $\mathfrak{J} = \mathfrak{J}_{\lambda}$, since
if $z \in \mathfrak{J}$, one has $r(z) = 0$; hence one has $B = C_{\lambda}$.

Let us pass now to the case where $S$ is affine and $X$ arbitrary; everything comes down to proving that an affine open
$V$ of $X$ is of finite presentation over $S$, and by virtue of what has just been demonstrated, it suffices to prove
that for every filtered projective system $(Z_{\lambda})$ of affine $S$-preschemes, the application

```text
(8.14.2.4)                Hom_S(Z_λ, V) → Hom_S(lim Z_λ, V)
```

is bijective. It is immediate that this application is injective, for if $(v_{\lambda})$, $(v_{\lambda}')$ are two
inductive systems of $S$-homomorphisms $v_{\lambda} : Z_{\lambda} \to V$, $v_{\lambda}' : Z_{\lambda} \to V$ such that
the corresponding morphisms

```text
                 Z ──u_λ──→ Z_λ ──v_λ──→ V,        Z ──u_λ──→ Z_λ ──v_λ'──→ V
```

are equal ($u_{\lambda}$ being the canonical morphism), then the morphisms

```text
              Z ──u_λ──→ Z_λ ──v_λ──→ V ──j──→ X,      Z ──u_λ──→ Z_λ ──v_λ'──→ V ──j──→ X
```

(where $j$ is the canonical injection) are equal, which entails $j \circ v_{\lambda} = j \circ v_{\lambda}'$ by
hypothesis for a suitable $\lambda$, hence $v_{\lambda} = v_{\lambda}'$.

<!-- original page 54 -->

It remains to prove that `(8.14.2.4)` is surjective. Let then $v : Z \to V$ be an $S$-morphism; by hypothesis there
exist a $\lambda$ and an $S$-morphism $w_{\lambda} : Z_{\lambda} \to X$ such that $j \circ v$ factors as $Z
\to^{u_{\lambda}} Z_{\lambda} \to^{w_{\lambda}} X$, and everything comes down to proving that there exists $\mu \geq
\lambda$ such that the morphism

```text
                            Z_μ ──w_λ ∘ u_{λμ}──→ X
```

(where $u_{\lambda \mu}$ is the transition morphism) factors as $Z_{\mu} \to^{v_{\mu}} V \to^{j} X$. Set, for every
$\lambda$, $U_{\lambda} = w^{-1}_{\lambda}(V)$. One has $u^{-1}_{\lambda}(U_{\lambda}) = u^{-1}_{\lambda}(U_{\lambda}) =
w^{-1}_{\lambda}(j^{-1}(V)) = v^{-1}(V) = Z$. Since the $Z_{\lambda}$ are quasi-compact and the $U_{\lambda}$, being
open, are ind-constructible `(1.9.6)`, one deduces from `(8.3.4)` that there exists $\mu \geq \lambda$ such that
$U_{\mu} = Z_{\mu}$. Q.E.D.

**Remark (8.14.3).**

<!-- label: IV.8.14.3 -->

The fact that the application `(8.14.2.1)` is injective when $f$ is locally of finite type `(8.8.2, (i))` naturally
leads one to ask whether this result also admits a converse. There is nothing of the sort, even when $S$ and $X$ are
affine, since there exist monomorphisms $X \to S$ which are not of finite type `(I, 2.4.2)`, and which therefore put
this conjecture in default.
