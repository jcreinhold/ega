# §7. Rational Maps

<!-- label: I.7 -->

## 7.1. Rational maps and rational functions

<!-- label: I.7.1 -->

**(7.1.1)** Let $X$, $Y$ be two preschemes, $U$, $V$ two dense opens in $X$, and $f$ (resp. $g$) a morphism of $U$
(resp. $V$) into $Y$; we say that $f$ and $g$ are _equivalent_ if they coincide on a dense open in $U \cap V$. Since a
finite intersection of dense opens in $X$ is a dense open in $X$, it is clear that this relation is an _equivalence
relation_.

**Definition (7.1.2).** Given two preschemes $X$, $Y$, one calls a _rational map_ of $X$ into $Y$ an equivalence class
of morphisms of dense open subsets of $X$ into $Y$, for the relation defined in (7.1.1). If $X$ and $Y$ are
$S$-preschemes, one says that such a class is an _$S$-rational map_ if there exists a representative of this class which
is an $S$-morphism. One calls an _$S$-rational section_ of $X$ any $S$-rational map of $S$ into $X$. One calls a
_rational function_ on a prescheme $X$ any $X$-rational section of the $X$-prescheme $X \otimes_{\mathbb{Z}}
\mathbb{Z}[T]$ (where $T$ is an indeterminate).

By abuse of language, when only $S$-preschemes are in question, one says "rational map" instead of "$S$-rational map" if
no confusion can result.

Let $f$ be a rational map of $X$ into $Y$, and $U$ an open of $X$; if $f_{1}, f_{2}$ are morphisms belonging to the
class $f$, defined respectively in dense opens $V$, $W$ of $X$, the restrictions $f_{1}|(U \cap V)$, $f_{2}|(U \cap W)$
coincide in $U \cap V \cap W$, which is dense in $U$; the class of morphisms $f$ thus defines a rational map of $U$ into
$Y$, called the _restriction of $f$ to $U$_ and written $f|U$.

If, to each $S$-morphism $f : X \to Y$, one makes correspond the $S$-rational map to which $f$ belongs, one defines a
canonical map of $\operatorname{Hom}_{S}(X, Y)$ into the set of $S$-rational maps of $X$ into $Y$. One denotes by
$\Gamma_{\mathrm{rat}}(X/Y)$ the set of $Y$-rational sections of $X$, and one thus has a canonical map $\Gamma(X/Y) \to
\Gamma_{\mathrm{rat}}(X/Y)$. It is moreover clear that if $X$ and $Y$ are two $S$-preschemes, the set of $S$-rational
maps of $X$ into $Y$ is canonically identified with $\Gamma_{\mathrm{rat}}((X \times_{S} Y)/X)$ (3.3.14).

**(7.1.3)** It follows at once from (7.1.2) and (3.3.14) that the rational functions on $X$ are canonically identified
with the _equivalence classes of sections of the structure sheaf $\mathcal{O}_{X}$_ above everywhere-dense opens of $X$,
two such sections being equivalent if they coincide in an everywhere-dense open contained in the intersection of their
sets of definition. It follows in particular that the rational functions on $X$ form a _ring_ $R(X)$.

**(7.1.4)** When $X$ is an _irreducible_ prescheme, every nonempty open is dense in $X$; one may also say that the
nonempty opens of $X$ are the _open neighborhoods of the generic point_ $x$ of $X$. To say that two morphisms of
nonempty open subsets of $X$ into $Y$ are equivalent thus means in this case that they have the _same germ at the point_
$x$. In other words, the rational maps (resp. $S$-rational maps) $X \to Y$ are identified with the _germs of morphisms_
(resp. of $S$-morphisms) of nonempty open subsets of $X$ into $Y$ at the generic point $x$ of $X$. In particular:

**Proposition (7.1.5).** If $X$ is an irreducible prescheme, the ring $R(X)$ of rational functions on $X$ is canonically
identified with the local ring $\mathcal{O}_{x}$ of the generic point $x$ of $X$. It is a local ring of dimension $0$,
and consequently an artinian local ring when $X$ is noetherian; it is a field when $X$ is integral, and it is identified
with the field of fractions of $A(X)$ when moreover $X$ is an affine scheme.

**Proof.** In view of what precedes and of the identification of rational functions with sections of $\mathcal{O}_{X}$
above an everywhere-dense open, the first assertion is none other than the definition of the stalk of a sheaf at a
point. For the other assertions, one may restrict to the case where $X$ is affine with ring $A$; then $\mathfrak{j}_{x}$
is the nilradical of $A$, and $\mathcal{O}_{x}$ is therefore of dimension $0$; if $A$ is integral, $\mathfrak{j}_{x} =
(0)$, and $\mathcal{O}_{x}$ is therefore the field of fractions of $A$. Finally, if $A$ is noetherian, one knows ([11],
p. 127, cor. 4) that $\mathfrak{j}_{x}$ is nilpotent and $\mathcal{O}_{x} = A_{\mathfrak{p}}$ is artinian.

If $X$ is _integral_, the ring $\mathcal{O}_{z}$ is integral for every $z \in X$; every affine open $U$ containing $z$
also contains $x$, and $R(U)$, equal to the field of fractions of $A(U)$, is thus identified with $R(X)$; one concludes
that $R(X)$ is also identified with the _field of fractions of $\mathcal{O}_{z}$_: the canonical identification of
$\mathcal{O}_{z}$ with a subring of $R(X)$ consists in making correspond to each germ of section $s \in \mathcal{O}_{z}$
the unique rational function on $X$, the class of a section of $\mathcal{O}_{X}$ (necessarily defined on an
everywhere-dense open) having germ $s$ at the point $z$.

**(7.1.6)** Suppose now that $X$ has a finite number of irreducible components $X_{i}$ ($1 \leq i \leq n$) (which is the
case when the space underlying $X$ is noetherian); let $X'_{i}$ be the open of $X_{i}$ complementary, relative to
$X_{i}$, to the union of the $X_{j} \cap X_{i}$ for $j \neq i$; $X'_{i}$ is irreducible, its generic point $x_{i}$ is
the generic point of $X_{i}$, and the $X'_{i}$ are pairwise disjoint, their union being dense in $X$ (0, 2.1.6). For
every everywhere-dense open $U$ of $X$, $U'_{i} = U \cap X'_{i}$ is a nonempty open dense in $X'_{i}$, the $U'_{i}$
being pairwise without common point, so that $U' = \bigcup_{i} U'_{i}$ is dense in $X$. To give a morphism of $U'$ into
$Y$ amounts to giving (arbitrarily) a morphism of each of the $U'_{i}$ into $Y$. Therefore:

**Proposition (7.1.7).** Let $X$, $Y$ be two preschemes (resp. $S$-preschemes) such that $X$ has a finite number of
irreducible components $X_{i}$, with generic points $x_{i}$ ($1 \leq i \leq n$). If $R_{i}$ is the set of germs of
morphisms (resp. $S$-morphisms) of open subsets of $X$ into $Y$ at the point $x_{i}$, the set of rational maps (resp.
$S$-rational maps) of $X$ into $Y$ is identified with the product of the $R_{i}$ ($1 \leq i \leq n$).

**Corollary (7.1.8).** Let $X$ be a noetherian prescheme. The ring of rational functions on $X$ is an artinian ring,
whose local components are the rings $\mathcal{O}_{x_{i}}$ of the generic points $x_{i}$ of the irreducible components
of $X$.

**Corollary (7.1.9).** Let $A$ be a noetherian ring, and let $X = \operatorname{Spec}(A)$. If $Q$ is the complement of
the union of the minimal prime ideals of $A$, the ring of rational functions on $X$ is canonically identified with the
ring of fractions $Q^{-1}A$.

This will follow from the following lemma:

**Lemma (7.1.9.1).** For an element $f \in A$ to be such that $D(f)$ is everywhere dense in $X$, it is necessary and
sufficient that $f \in Q$; every dense open in $X$ contains an open of the form $D(f)$, where $f \in Q$.

In fact, suppose this lemma proved; since the ring of sections $\Gamma(D(f), \mathcal{O}_{X})$ is identified with
$A_{f}$ (1.3.6 and 1.3.7), it follows from the fact that the $D(f)$ with $f \in Q$ form a cofinal set in the ordered set
(for $\supset$) of dense opens in $X$, and from def. (7.1.1), that the ring of rational functions on $X$ is identified
with the inductive limit of the $A_{f}$ for $f \in Q$ (for the preorder relation "$g$ is a multiple of $f$"), that is,
with $Q^{-1}A$ (0, 1.4.5).

To prove (7.1.9.1), let us again denote by $X_{i}$ the irreducible components of $X$ ($1 \leq i \leq n$); if $D(f)$ is
dense in $X$, then $D(f) \cap X_{i} \neq \emptyset$ for $1 \leq i \leq n$, and conversely; but this means that $f \notin
\mathfrak{p}_{i}$ for $1 \leq i \leq n$, on setting $\mathfrak{p}_{i} = \mathfrak{j}(X_{i})$, and since the
$\mathfrak{p}_{i}$ are the minimal prime ideals of $A$ (1.1.14), the relations $f \notin \mathfrak{p}_{i}$ ($1 \leq i
\leq n$) are equivalent to $f \in Q$, whence the first assertion of the lemma. On the other hand, if $U$ is a dense open
in $X$, the complement of $U$ is a set of the form $V(\mathfrak{a})$, where $\mathfrak{a}$ is an ideal contained in none
of the $\mathfrak{p}_{i}$; it is therefore not contained in their union ([10], p. 13), and there thus exists an $f \in
\mathfrak{a}$ belonging to $Q$; whence $D(f) \subset U$, which completes the proof.

**(7.1.10)** Suppose again $X$ irreducible, with generic point $x$. Since every nonempty open $U$ of $X$ contains $x$,
and consequently also contains every $z \in X$ such that $x \in \overline{\{z\}}$, every morphism $U \to Y$ may be
composed with the canonical morphism $\operatorname{Spec}(\mathcal{O}_{x}) \to X$ (2.4.1); and two morphisms into $Y$ of
two nonempty open subsets of $X$, which coincide in a nonempty open subset of $X$, give by composition the same morphism
$\operatorname{Spec}(\mathcal{O}_{x}) \to Y$. In other words, to each rational map of $X$ into $Y$ there thus
corresponds a well-determined morphism $\operatorname{Spec}(\mathcal{O}_{x}) \to Y$.

**Proposition (7.1.11).** Let $X$, $Y$ be two $S$-preschemes; suppose $X$ irreducible, with generic point $x$, and $Y$
of finite type over $S$. Two $S$-rational maps of $X$ into $Y$, to which corresponds the same $S$-morphism
$\operatorname{Spec}(\mathcal{O}_{x}) \to Y$, are identical. If one supposes in addition $S$ locally noetherian, every
$S$-morphism of $\operatorname{Spec}(\mathcal{O}_{x})$ into $Y$ corresponds to an $S$-rational map (and only one) of $X$
into $Y$.

**Proof.** Taking account of the fact that every nonempty open of $X$ is everywhere dense, this follows at once from
(6.5.1).

**Corollary (7.1.12).** Suppose $S$ locally noetherian, and the other hypotheses of (7.1.11) satisfied. The $S$-rational
maps of $X$ into $Y$ are then identified with the points of the $S$-prescheme $Y$, with values in the $S$-prescheme
$\operatorname{Spec}(\mathcal{O}_{x})$.

This is none other than (7.1.11), with the terminology introduced in (3.4.1).

**Corollary (7.1.13).** Suppose the conditions of (7.1.12) fulfilled. Let $s$ be the image of $x$ in $S$. To give an
$S$-rational map of $X$ into $Y$ is equivalent to giving a point $y$ of $Y$ above $s$, and a local
$\mathcal{O}_{s}$-homomorphism $\mathcal{O}_{y} \to \mathcal{O}_{x} = R(X)$.

This follows from (7.1.11) and (2.4.4).

In particular:

**Corollary (7.1.14).** Under the conditions of (7.1.12), the $S$-rational maps of $X$ into $Y$ depend (for $Y$ given)
only on the $S$-prescheme $\operatorname{Spec}(\mathcal{O}_{x})$, and in particular remain the same when one replaces
$X$ by $\operatorname{Spec}(\mathcal{O}_{z})$, for any $z \in X$.

**Proof.** In fact, since $z \in \overline{\{x\}}$, $x$ is the generic point of $Z =
\operatorname{Spec}(\mathcal{O}_{z})$, and $\mathcal{O}_{X,x} = \mathcal{O}_{Z,x}$.

When $X$ is integral, $R(X) = \mathcal{O}_{x} = \kappa(x)$ is a field (7.1.5); the preceding corollaries then specialize
to:

**Corollary (7.1.15).** Suppose the conditions of (7.1.12) verified and moreover that $X$ is integral. Let $s$ be the
image of $x$ in $S$. Then the $S$-rational maps of $X$ into $Y$ are identified with the geometric points of $Y
\otimes_{S} \kappa(s)$ with values in the extension $R(X)$ of $\kappa(s)$; in other words, each of them is equivalent to
giving a point $y \in Y$ above $s$ and a $\kappa(s)$-monomorphism of $\kappa(y)$ into $\kappa(x) = R(X)$.

**Proof.** The points of $Y$ above $s$ are in fact identified with those of $Y \otimes_{S} \kappa(s)$ (3.6.3), and the
local $\mathcal{O}_{s}$-homomorphisms $\mathcal{O}_{y} \to R(X)$ with the $\kappa(s)$-monomorphisms $\kappa(y) \to
R(X)$.

More particularly:

**Corollary (7.1.16).** Let $k$ be a field, and $X$, $Y$ two algebraic preschemes (6.4.1) over $k$; suppose in addition
$X$ integral. Then the $k$-rational maps of $X$ into $Y$ are identified with the geometric points of $Y$ with values in
the extension $R(X)$ of $k$ (3.4.4).

## 7.2. Domain of definition of a rational map

<!-- label: I.7.2 -->

**(7.2.1)** Let $X$, $Y$ be two preschemes, $f$ a rational map of $X$ into $Y$. One says that $f$ is _defined at a
point_ $x \in X$ if there exists an everywhere-dense open set $U$ containing $x$ and a morphism $U \to Y$ belonging to
the equivalence class $f$. The set of points $x \in X$ where $f$ is defined is called the _domain of definition_ of $f$;
it is clear that it is an everywhere-dense open in $X$.

**Proposition (7.2.2).** Let $X$, $Y$ be two $S$-preschemes, such that $X$ is reduced and $Y$ separated over $S$. Let
$f$ be an $S$-rational map of $X$ into $Y$, and $U_{0}$ its domain of definition. There then exists one and only one
$S$-morphism $U_{0} \to Y$ belonging to the class $f$.

**Proof.** Since for every morphism $U \to Y$ belonging to the class $f$ one necessarily has $U \subset U_{0}$, it is
clear that the proposition will be a consequence of the

**Lemma (7.2.2.1).** Under the hypotheses of (7.2.2), let $U_{1}, U_{2}$ be two everywhere-dense opens of $X$, $f_{i} :
U_{i} \to Y$ ($i = 1, 2$) two $S$-morphisms such that there exists an open $V \subset U_{1} \cap U_{2}$ dense in $X$ and
in which $f_{1}$ and $f_{2}$ coincide. Then $f_{1}$ and $f_{2}$ coincide in $U_{1} \cap U_{2}$.

**Proof.** One may evidently restrict to the case where $X = U_{1} = U_{2}$. Since $X$ (hence $V$) is reduced, $X$ is
the smallest closed subprescheme of $X$ majorizing $V$ (5.2.2). Let $g = (f_{1}, f_{2})_{S} : X \to Y \times_{S} Y$;
since by hypothesis the diagonal $T = \Delta_{Y}(Y)$ is a closed subprescheme of $Y \times_{S} Y$, $Z = g^{-1}(T)$ is a
closed subprescheme of $X$ (4.4.1). If $h : V \to Y$ is the common restriction of $f_{1}$ and $f_{2}$ to $V$, the
restriction of $g$ to $V$ is $g' = (h, h)_{S}$, which factors as $g' = \Delta_{Y} \circ h$; since $\Delta_{Y}^{-1}(T) =
Y$, one has $g'^{-1}(T) = V$, and consequently $Z$ is a closed subprescheme of $X$ inducing $V$, hence majorizing $V$,
which entails $Z = X$. From the relation $g^{-1}(T) = X$ one deduces (4.4.1) that $g$ factors as $\Delta_{Y} \circ f$,
where $f$ is a morphism $X \to Y$, which entails by definition of the diagonal morphism that $f_{1} = f_{2} = f$.

It is clear that the morphism $U_{0} \to Y$ defined in (7.2.2) is the unique morphism of the class $f$ which _cannot be
prolonged_ to a morphism of an open subset of $X$ strictly containing $U_{0}$. Under the hypotheses of (7.2.2), one may
thus _identify the rational maps of $X$ into $Y$ with the non-prolongeable morphisms_ (to strictly larger opens) of
everywhere-dense opens of $X$ into $Y$. With this identification, prop. (7.2.2) entails:

**Corollary (7.2.3).** The hypotheses on $X$ and $Y$ being those of (7.2.2), let $U$ be an everywhere-dense open of $X$.
There exists a canonical one-to-one correspondence between the $S$-morphisms of $U$ into $Y$ and the $S$-rational maps
of $X$ into $Y$ defined at all points of $U$.

**Proof.** By virtue of (7.2.2), for every $S$-morphism $f$ of $U$ into $Y$, there exists in fact one and only one
$S$-rational map $\bar{f}$ of $X$ into $Y$ which prolongs $f$.

**Corollary (7.2.4).** Let $S$ be a scheme, $X$ a reduced $S$-prescheme, $Y$ an $S$-scheme, $f : U \to Y$ an
$S$-morphism of a dense open $U$ of $X$ into $Y$. If $\bar{f}$ is the $\mathbb{Z}$-rational map of $X$ into $Y$ which
prolongs $f$, then $\bar{f}$ is an $S$-morphism (and is consequently the $S$-rational map of $X$ into $Y$ prolonging
$f$).

**Proof.** In fact, if $\varphi : X \to S$, $\psi : Y \to S$ are the structure morphisms, $U_{0}$ the domain of
definition of $\bar{f}$, $j$ the injection $U_{0} \to X$, it suffices to prove that $\psi \circ \bar{f} = \varphi \circ
j$, which follows at once from (7.2.2.1), since $f$ is an $S$-morphism.

**Corollary (7.2.5).** Let $X$, $Y$ be two $S$-preschemes; suppose $X$ reduced, $X$ and $Y$ separated over $S$. Let $p :
Y \to X$ be an $S$-morphism (making $Y$ an $X$-prescheme), $U$ an everywhere-dense open of $X$, $f$ a $U$-section of
$Y$; then the rational map $\bar{f}$ of $X$ into $Y$ prolonging $f$ is an $X$-rational section of $Y$.

**Proof.** One must prove that $p \circ \bar{f}$ is the identity in the domain of definition of $\bar{f}$; since $X$ is
separated over $S$, this again follows from (7.2.2.1).

**Corollary (7.2.6).** Let $X$ be a reduced prescheme, $U$ an everywhere-dense open of $X$. There is a canonical
one-to-one correspondence between the sections of $\mathcal{O}_{X}$ above $U$ and the rational functions $f$ on $X$
defined at every point of $U$.

**Proof.** Taking account of (7.2.3), (7.1.2), and (7.1.3), it suffices to remark that the $X$-prescheme $X
\otimes_{\mathbb{Z}} \mathbb{Z}[T]$ is separated above $X$ (5.5.15 (iv)).

**Corollary (7.2.7).** Let $Y$ be a reduced prescheme, $f : X \to Y$ a separated morphism, $U$ an everywhere-dense open
of $Y$, $g : U \to f^{-1}(U)$ a $U$-section of $f^{-1}(U)$, $Z$ the reduced subprescheme of $X$ having $g(U)$ as
underlying space (5.2.1). For $g$ to be the restriction of a $Y$-section of $X$ (in other words (7.2.5), for the
rational map of $Y$ into $X$ prolonging $g$ to be defined everywhere), it is necessary and sufficient that the
restriction of $f$ to $Z$ be an isomorphism of $Z$ onto $Y$.

**Proof.** The restriction of $f$ to $f^{-1}(U)$ is a separated morphism (5.5.1, (i)), so $g$ is a closed immersion
(5.4.6), and consequently $g(U) = Z \cap f^{-1}(U)$ and the subprescheme induced by $Z$ on the open $g(U)$ of $Z$ is
identical with the closed subprescheme of $f^{-1}(U)$ associated with $g$ (5.2.1). It is then clear that the condition
of the statement is sufficient, for if it is fulfilled and if $h : Z \to Y$ is the restriction of $f$ to $Z$ and
$\bar{g} : Y \to Z$ the inverse isomorphism, $\bar{g}$ prolongs $g$. Conversely, if $g$ is the restriction to $U$ of a
$Y$-section $h$ of $X$, $h$ is a closed immersion (5.4.6), so $h(Y)$ is closed, and since it is contained in $Z$, it is
equal to $Z$, and it follows from (5.2.1) that $h$ is necessarily an isomorphism of $Y$ onto the closed subprescheme $Z$
of $X$.

**(7.2.8)** Let $X$, $Y$ be two $S$-preschemes, $X$ being supposed reduced and $Y$ separated over $S$. Let $f$ be an
$S$-rational map of $X$ into $Y$, and let $x$ be a point of $X$; one may compose $f$ with the canonical $S$-morphism
$\operatorname{Spec}(\mathcal{O}_{x}) \to X$ (2.4.1) provided that the trace on $\operatorname{Spec}(\mathcal{O}_{x})$
of the domain of definition of $f$ is dense in $\operatorname{Spec}(\mathcal{O}_{x})$ (identified with the set of $z \in
X$ such that $x \in \overline{\{z\}}$ (2.4.2)). This will be the case in the following situations:

1° $X$ is _irreducible_ (hence _integral_), for then the generic point $\xi$ of $X$ is the generic point of
$\operatorname{Spec}(\mathcal{O}_{x})$; since the domain of definition $U$ of $f$ contains $\xi$, $U \cap
\operatorname{Spec}(\mathcal{O}_{x})$ contains $\xi$, hence is dense in $\operatorname{Spec}(\mathcal{O}_{x})$.

2° $X$ is _locally noetherian_; our assertion in fact follows then from the

**Lemma (7.2.8.1).** Let $X$ be a prescheme whose underlying space is locally noetherian, $x$ a point of $X$. The
irreducible components of $\operatorname{Spec}(\mathcal{O}_{x})$ are the traces on
$\operatorname{Spec}(\mathcal{O}_{x})$ of the irreducible components of $X$ containing $x$. For an open $U \subset X$ to
be such that $U \cap \operatorname{Spec}(\mathcal{O}_{x})$ is dense in $\operatorname{Spec}(\mathcal{O}_{x})$, it is
necessary and sufficient that it meet the irreducible components of $X$ containing $x$ (which is the case in particular
if $U$ is dense in $X$).

**Proof.** The second assertion evidently follows from the first, and it thus suffices to prove the latter. Since
$\operatorname{Spec}(\mathcal{O}_{x})$ is contained in every affine open $U$ containing $x$, and since the irreducible
components of $U$ containing $x$ are the traces on $U$ of the irreducible components of $X$ containing $x$ (0, 2.1.6),
one may suppose $X$ affine with ring $A$. Since the prime ideals of $A_{x}$ correspond bijectively to the prime ideals
of $A$ contained in $\mathfrak{j}_{x}$ (0, 1.2.6), the minimal prime ideals of $A_{x}$ correspond to the minimal prime
ideals of $A$ contained in $\mathfrak{j}_{x}$, whence the lemma (1.1.14).

This being so, suppose that one is in one of the two cases cited above. If $U$ is the domain of definition of the
$S$-rational map $f$, let us denote by $f'$ the rational map of $\operatorname{Spec}(\mathcal{O}_{x})$ into $Y$ which
coincides (taking account of (2.4.2)) with $f$ in $U \cap \operatorname{Spec}(\mathcal{O}_{x})$; we shall say that this
rational map is _induced by_ $f$.

**Proposition (7.2.9).** Let $S$ be a locally noetherian prescheme, $X$ a reduced $S$-prescheme, $Y$ an $S$-scheme of
finite type. Suppose in addition $X$ irreducible or locally noetherian. Let then $f$ be an $S$-rational map of $X$ into
$Y$, and $x$ a point of $X$. For $f$ to be defined at the point $x$, it is necessary and sufficient that the rational
map $f'$ of $\operatorname{Spec}(\mathcal{O}_{x})$ into $Y$, induced by $f$ (7.2.8), be a morphism.

**Proof.** The condition being evidently necessary (since $\operatorname{Spec}(\mathcal{O}_{x})$ is contained in every
open containing $x$), let us prove that it is sufficient. By virtue of (6.5.1), there exists an open neighborhood $U$ of
$x$ in $X$ and an $S$-morphism $g$ of $U$ into $Y$, inducing $f'$ on $\operatorname{Spec}(\mathcal{O}_{x})$. If $X$ is
irreducible, $U$ is dense in $X$, and by virtue of (7.2.3) one may suppose that $g$ is an $S$-rational map. Moreover,
the generic point of $X$ belongs to $\operatorname{Spec}(\mathcal{O}_{x})$ and to the domain of definition of $f$, so
$f$ and $g$ coincide at this point, and consequently in a nonempty open set of $X$ (6.5.1). But since $f$ and $g$ are
$S$-rational maps, they are identical (7.2.3), so $f$ is defined at $x$.

If now one supposes $X$ locally noetherian, one may suppose $U$ noetherian; there is then only a finite number of
irreducible components $X_{i}$ of $X$ containing $x$ (7.2.8.1), and one may suppose that these are the only ones meeting
$U$, by replacing $U$ if necessary by a smaller open (since there are only a finite number of irreducible components of
$X$ meeting $U$, $U$ being noetherian). One sees then, as above, that $f$ and $g$ coincide in a nonempty open of each of
the $X_{i}$. Taking account of the fact that each of the $X_{i}$ is contained in $U$, let us then consider the morphism
$f_{1}$, defined in a dense open of $U \cup (X - U)$, equal to $g$ in $U$ and to $f$ in the intersection of $X - U$ and
the domain of definition of $f$. Since $U \cup (X - U)$ is dense in $X$, $f_{1}$ and $f$ coincide in a dense open of
$X$, and since $f$ is a rational map, $f$ is an extension of $f_{1}$ (7.2.3), hence is defined at the point $x$.

## 7.3. Sheaf of rational functions

<!-- label: I.7.3 -->

**(7.3.1)** Let $X$ be a prescheme. For every open $U \subset X$, let us denote by $R(U)$ the ring of rational functions
on $U$ (7.1.3); it is a $\Gamma(U, \mathcal{O}_{X})$-algebra. Moreover, if $V \subset U$ is a second open of $X$, every
section of $\mathcal{O}_{X}$ above an everywhere-dense open subset of $U$ gives, by restriction to $V$, a section above
an everywhere-dense open subset of $V$, and if two sections coincide above an everywhere-dense open subset of $U$, their
restrictions to $V$ coincide above an everywhere-dense open subset of $V$. One thus defines a $\mathrm{di}$-homomorphism
of algebras $\rho_{V,U} : R(U) \to R(V)$, and it is clear that if $U \supset V \supset W$ are three opens of $X$, one
has $\rho_{W,U} = \rho_{W,V} \circ \rho_{V,U}$; the $R(U)$ thus define a _presheaf_ of algebras on $X$.

**Definition (7.3.2).** One calls the _sheaf of rational functions_ on a prescheme $X$, and one denotes by
$\mathcal{R}(X)$, the $\mathcal{O}_{X}$-Algebra associated with the presheaf formed by the $R(U)$.

For every prescheme $X$ and every open $U \subset X$, it is clear that the induced sheaf $\mathcal{R}(X)|U$ is none
other than $\mathcal{R}(U)$.

**Proposition (7.3.3).** Let $X$ be a prescheme such that the family $(X_{\lambda})$ of its irreducible components is
locally finite (which is in particular the case when the space underlying $X$ is locally noetherian). Then the
$\mathcal{O}_{X}$-Module $\mathcal{R}(X)$ is quasi-coherent, and for every open $U$ of $X$ meeting only a finite number
of components $X_{\lambda}$, $R(U)$ is equal to $\Gamma(U, \mathcal{R}(X))$ and is canonically identified with the
direct composite of the local rings of the generic points of the $X_{\lambda}$ such that $U \cap X_{\lambda} \neq
\emptyset$.

**Proof.** One may evidently limit oneself to the case where $X$ has only a finite number of irreducible components
$X_{i}$, with generic points $x_{i}$ ($1 \leq i \leq n$). The fact that $R(U)$ is canonically identified with the direct
composite of the $\mathcal{O}_{x_{i}} = R(X_{i})$ such that $U \cap X_{i} \neq \emptyset$ then follows from (7.1.7). Let
us show moreover that the presheaf $U \to R(U)$ verifies the sheaf axioms, which will prove that $R(U) = \Gamma(U,
\mathcal{R}(X))$. In fact, it verifies (F 1) according to what precedes. To see that it satisfies (F 2), consider a
cover of an open $U$ of $X$ by opens $V_{\alpha} \subset U$; if the $s_{\alpha} \in R(V_{\alpha})$ are such that the
restrictions of $s_{\alpha}$ and $s_{\beta}$ to $V_{\alpha} \cap V_{\beta}$ coincide for every pair of indices, one
concludes that for every index $i$ such that $U \cap X_{i} \neq \emptyset$, the components in $R(X_{i})$ of all the
$s_{\alpha}$ such that $V_{\alpha} \cap X_{i} \neq \emptyset$ are the same; denoting by $t_{i}$ this component, it is
clear that the element of $R(U)$ having the $t_{i}$ as components has restriction $s_{\alpha}$ on each $V_{\alpha}$.
Finally, to see that $\mathcal{R}(X)$ is quasi-coherent, one may limit oneself to the case where $X =
\operatorname{Spec}(A)$ is affine; taking for $U$ the affine opens of the form $D(f)$, where $f \in A$, it follows from
what precedes and from the definition (1.3.4) that one has $\mathcal{R}(X) = \tilde{M}$, where $M$ is the direct sum of
the $A$-modules $A_{x_{i}}$.

**Corollary (7.3.4).** Let $X$ be a reduced prescheme having only a finite number of irreducible components, and let
$X_{i}$ ($1 \leq i \leq n$) be the reduced closed subpreschemes of $X$ having for underlying spaces the irreducible
components of $X$ (5.2.1). If $h_{i}$ is the canonical injection $X_{i} \to X$, then $\mathcal{R}(X)$ is the direct
composite of the $\mathcal{O}_{X}$-Algebras $(h_{i})_{*}(\mathcal{R}(X_{i}))$.

**Corollary (7.3.5).** If $X$ is irreducible, every quasi-coherent $\mathcal{R}(X)$-Module $\mathcal{F}$ is a simple
sheaf.

**Proof.** It suffices to show that every $x \in X$ admits a neighborhood $U$ such that $\mathcal{F}|U$ is a simple
sheaf (0, 3.6.2), in other words one is reduced to the case where $X$ is affine; one may moreover suppose that
$\mathcal{F}$ is the cokernel of a homomorphism $(\mathcal{R}(X))^{(I)} \to (\mathcal{R}(X))^{(J)}$ (0, 5.1.3), and
everything comes down to seeing that $\mathcal{R}(X)$ is a simple sheaf; but this is evident since $\Gamma(U,
\mathcal{R}(X)) = R(X)$ for every nonempty open $U$, $U$ containing the generic point of $X$.

**Corollary (7.3.6).** If $X$ is irreducible, for every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$,
$\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{R}(X)$ is a simple sheaf; if in addition $X$ is reduced (hence
integral), $\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{R}(X)$ is isomorphic to a sheaf of the form
$(\mathcal{R}(X))^{(I)}$.

**Proof.** The second assertion follows from the fact that $R(X)$ is then a field.

**Proposition (7.3.7).** Suppose that the prescheme $X$ is locally integral or locally noetherian. Then $\mathcal{R}(X)$
is a quasi-coherent $\mathcal{O}_{X}$-Algebra; if in addition $X$ is reduced (which is the case when $X$ is locally
integral), the canonical homomorphism $\mathcal{O}_{X} \to \mathcal{R}(X)$ is injective.

**Proof.** The question being local, the first assertion follows from (7.3.3); the second follows at once from (7.2.3).

**(7.3.8)** Let $X$, $Y$ be two preschemes each having a finite number of irreducible components, and let $f : X \to Y$
be a morphism whose restriction to the set of generic points of the irreducible components of $X$ is a surjection onto
the set of generic points of the irreducible components of $Y$. Then one has

$$ f^{*}(\mathcal{R}(Y)) = \mathcal{R}(X). \tag{7.3.8.1} $$

In fact, one is reduced (by virtue of (7.3.3)) to the case where $X$ and $Y$ are irreducible, with generic points $x$,
$y$, with $f(x) = y$; hence $(f^{*}(\mathcal{R}(Y)))_{x} = \mathcal{O}_{y} \otimes_{\mathcal{O}_{y}} \mathcal{O}_{x} =
\mathcal{O}_{x}$ (0, 4.3.1), which proves (7.3.8.1) by virtue of (7.3.5).

## 7.4. Torsion sheaves and torsion-free sheaves

<!-- label: I.7.4 -->

**(7.4.1)** Let $X$ be an integral prescheme. For every $\mathcal{O}_{X}$-Module $\mathcal{F}$, the canonical
homomorphism $\mathcal{O}_{X} \to \mathcal{R}(X)$ defines by tensorization a homomorphism (again called _canonical_)
$\mathcal{F} \to \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{R}(X)$ which, on each fiber, is none other than the
homomorphism $z \to z \otimes 1$ of $\mathcal{F}_{x}$ into $\mathcal{F}_{x} \otimes_{\mathcal{O}_{x}} R(X)$. The kernel
$\mathcal{T}$ of this homomorphism is a sub-$\mathcal{O}_{X}$-Module of $\mathcal{F}$, called the _torsion sheaf of
$\mathcal{F}$_; it is quasi-coherent if $\mathcal{F}$ is quasi-coherent (4.1.1 and 7.3.6). One says that $\mathcal{F}$
is _torsion-free_ if $\mathcal{T} = 0$ and that $\mathcal{F}$ is a _torsion sheaf_ if $\mathcal{T} = \mathcal{F}$. For
every $\mathcal{O}_{X}$-Module $\mathcal{F}$, $\mathcal{F}/\mathcal{T}$ is torsion-free. One deduces from (7.3.5) that:

**Proposition (7.4.2).** If $X$ is an integral prescheme, every quasi-coherent torsion-free $\mathcal{O}_{X}$-Module
$\mathcal{F}$ is isomorphic to a subsheaf $\mathcal{G}$ of a simple sheaf of the form $(\mathcal{R}(X))^{(I)}$,
generated (as $\mathcal{R}(X)$-Module) by $\mathcal{G}$.

The cardinal of $I$ is called the _rank_ of $\mathcal{F}$; for every nonempty affine open $U$ of $X$, the rank of
$\mathcal{F}$ is equal to the rank of $\Gamma(U, \mathcal{F})$ as a $\Gamma(U, \mathcal{O}_{X})$-module, as one sees at
once by considering the generic point of $X$, contained in $U$. In particular:

**Corollary (7.4.3).** On an integral prescheme $X$, every quasi-coherent torsion-free $\mathcal{O}_{X}$-Module of rank
$1$ (in particular every invertible $\mathcal{O}_{X}$-Module) is isomorphic to a sub-$\mathcal{O}_{X}$-Module of
$\mathcal{R}(X)$, and conversely.

**Corollary (7.4.4).** Let $X$ be an integral prescheme, $\mathcal{L}$, $\mathcal{L}'$ two torsion-free
$\mathcal{O}_{X}$-Modules, $f$ (resp. $f'$) a section of $\mathcal{L}$ (resp. $\mathcal{L}'$) above $X$. For $f \otimes
f' = 0$, it is necessary and sufficient that one of the sections $f, f'$ be zero.

**Proof.** Let $x$ be the generic point of $X$; one has by hypothesis $(f \otimes f')_{x} = f_{x} \otimes f'_{x} = 0$.
Since $\mathcal{L}_{x}$ and $\mathcal{L}'_{x}$ are identified with sub-$\mathcal{O}_{x}$-Modules of the field
$\mathcal{O}_{x}$, the preceding relation entails $f_{x} = 0$ or $f'_{x} = 0$, and consequently $f = 0$ or $f' = 0$
since $\mathcal{L}$ and $\mathcal{L}'$ are torsion-free (7.3.5).

**Proposition (7.4.5).** Let $X$, $Y$ be two integral preschemes, $f : X \to Y$ a dominant morphism. For every
quasi-coherent torsion-free $\mathcal{O}_{X}$-Module $\mathcal{F}$, $f_{*}(\mathcal{F})$ is a torsion-free
$\mathcal{O}_{Y}$-Module.

**Proof.** Since $f_{*}$ is left exact (0, 4.2.1), it suffices, by virtue of (7.4.2), to prove the proposition when
$\mathcal{F} = (\mathcal{R}(X))^{(I)}$. Now, every nonempty open $U$ of $Y$ contains the generic point of $Y$, so
$f^{-1}(U)$ contains the generic point of $X$ (0, 2.1.5), so one then has $\Gamma(U, f_{*}(\mathcal{F})) =
\Gamma(f^{-1}(U), \mathcal{F}) = (R(X))^{(I)}$; in other words, $f_{*}(\mathcal{F})$ is the simple sheaf with fiber
$(R(X))^{(I)}$, considered as $\mathcal{R}(Y)$-Module, and it is evidently torsion-free.

**Proposition (7.4.6).** Let $X$ be an integral prescheme, $x$ its generic point. For every quasi-coherent
$\mathcal{O}_{X}$-Module of finite type $\mathcal{F}$, the following conditions are equivalent: a) $\mathcal{F}$ is a
torsion sheaf; b) $\mathcal{F}_{x} = 0$; c) $\operatorname{Supp}(\mathcal{F}) \neq X$.

**Proof.** By virtue of (7.3.5) and (7.4.1), the relations $\mathcal{F}_{x} = 0$ and $\mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{R}(X) = 0$ are equivalent, so a) and b) are equivalent; on the other hand,
$\operatorname{Supp}(\mathcal{F})$ is closed in $X$ (0, 5.2.2), and since every nonempty open of $X$ contains $x$, b)
and c) are equivalent.

**(7.4.7)** One extends (by abuse of language) the definitions of (7.4.1) to the case where $X$ is a reduced prescheme
having only a finite number of irreducible components; it then follows from (7.3.4) that the equivalence of a) and c) in
(7.4.6) is still valid for such a prescheme.
