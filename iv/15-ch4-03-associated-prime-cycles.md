<!-- original page 36 -->

## §3. Associated prime cycles and primary decompositions

In this section we mainly give the translation of the results on modules expounded in Bourbaki, *Alg. comm.*, chap. IV,
which we follow very closely. The notions that follow seem to be of interest only in the case of *locally Noetherian*
preschemes.

### 3.1. Associated prime cycles of a Module

**Definition (3.1.1).**

<!-- label: IV.3.1.1 -->

*Let $X$ be a prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. We say that a point $x \in X$ is
**associated to** $\mathcal{F}$ if the maximal ideal $\mathfrak{m}_{x}$ of $\mathcal{O}_{x}$ is associated to the
$\mathcal{O}_{x}$-Module $\mathcal{F}_{x}$ (in other words, if $\mathfrak{m}_{x}$ is the annihilator of an element of
$\mathcal{F}_{x}$). We denote by $Ass(\mathcal{F})$ the set of $x \in X$ associated to $\mathcal{F}$. We say that a
closed irreducible subset $Z$ of $X$ is an **associated prime cycle of $\mathcal{F}$** if its generic point is
associated to $\mathcal{F}$. When $\mathcal{F} = \mathcal{O}_{X}$, we shall also say that the points (resp. prime
cycles) associated to $\mathcal{F}$ are associated to the prescheme $X$.*

*We say that an associated prime cycle of $\mathcal{F}$ (resp. $X$) is **embedded** if it is contained in another
associated prime cycle of $\mathcal{F}$ (resp. $X$) (in other words, if it is not maximal in the set of these cycles).*

If $X$ is locally Noetherian, the irreducible components of $X$ are nothing other than the maximal (or non-embedded)
prime cycles associated to $X$.

It is clear that if $x \in Ass(\mathcal{F})$, then $\mathcal{F}_{x} \neq 0$; in other words

$$ (3.1.1.1) Ass(\mathcal{F}) \subset Supp(\mathcal{F}). $$

If $x \in X$ is associated to $\mathcal{F}$, it is evidently associated to $\mathcal{F}|U$ for every open neighbourhood
$U$ of $x$, and conversely, if it is associated to $\mathcal{F}|U$ for one of these neighbourhoods, it is associated to
$\mathcal{F}$.

We note finally that for a quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, the existence of embedded associated
prime cycles is a *local* question, since if $y$ and $z$ are two points of $Ass(\mathcal{F})$ with $y \in \overline{z}$,
every neighbourhood of $y$ contains $z$.

**Proposition (3.1.2).**

<!-- label: IV.3.1.2 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module, $X = \operatorname{Spec}(A)$, $\mathcal{F} = \tilde{M}$; for a point
$x \in X$ to be associated to $\mathcal{F}$, it is necessary and sufficient that the prime ideal $\mathfrak{j}_{x}$ of
$A$ be associated to the module $M$ (in other words, be the annihilator of an element $f \in M$).*

This results from the definition `(3.1.1)` and from Bourbaki, *loc. cit.*, §1, n° 2, cor. of prop. 5, applied to
$S = A - \mathfrak{j}_{x}$.

**Proposition (3.1.3).**

<!-- label: IV.3.1.3 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, $x$ a point of $X$,
$Z$ the reduced closed sub-prescheme of $X$ having $\overline{x}$ as underlying space `(I, 5.2.1)`. The following
conditions are equivalent:*

*a) $x \in Ass(\mathcal{F})$.*

<!-- original page 37 -->

*b) There exists an open neighbourhood $U$ of $x$ and a section $f \in \Gamma(U, \mathcal{F})$ such that $U \cap Z$ is
equal to $Supp(\mathcal{O}_{U} \cdot f)$.*

*b') There exists an open neighbourhood $U$ of $x$ and a section $f \in \Gamma(U, \mathcal{F})$ such that $U \cap Z$ is
an irreducible component of $Supp(\mathcal{O}_{U} \cdot f)$.*

*c) There exists an open neighbourhood $U$ of $x$ and a sub-Module of $\mathcal{F}|U$ isomorphic to $\mathcal{O}_{Z}|U$
($\mathcal{O}_{Z}$ being identified with a quotient of $\mathcal{O}_{X}$).*

*c') There exists an open neighbourhood $U$ of $x$ and a coherent sub-Module $\mathcal{G}$ of $\mathcal{F}|U$ such that
$U \cap Z$ is an irreducible component of $Supp(\mathcal{G})$.*

It is clear that c) implies b), since it suffices to take for $f$ the element of $\Gamma(U, \mathcal{F})$ corresponding
to the unit section of $\mathcal{O}_{Z}|U$. As $U \cap Z$ is irreducible $(0_{I}, 2.1.6)$, b) implies b'), and b')
implies c') since $\mathcal{O}_{X}$ is coherent $(0_{I}, 5.3.4)$. To see that c') implies a), we may restrict to the
case where $U = X = \operatorname{Spec}(A)$ is affine, $A$ therefore Noetherian, and where $\mathcal{F} = \tilde{M}$,
$M$ being an $A$-module, and $\mathcal{G} = \tilde{N}$, where $N$ is a sub-module of $M$, of finite type. We then know
that the minimal elements of $Supp(\mathcal{G})$ are the maximal points of $V(Ann(N))$ $(0_{I}, 1.7.4)$, and these are
also the minimal elements of $Ass(N)$ (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 3, cor. 1 of prop. 7); since
`Ass(N) ⊂ Ass(M) = Ass(ℱ)`, we see that c') implies a). Finally, a) implies c) by virtue of `(3.1.2)`, taking again $X$
affine, $\mathcal{F} = \tilde{M}$, and $Z$ defined by the ideal $\mathfrak{j}_{x} \cdot A$ (with the notation of
`(3.1.2)`).

**Corollary (3.1.4).**

<!-- label: IV.3.1.4 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Then the maximal prime
cycles associated to $\mathcal{F}$ are the irreducible components of $Supp(\mathcal{F})$, and the generic points of
these components are the points $x \in X$ such that $\mathcal{F}_{x}$ is an $\mathcal{O}_{x}$-Module of finite length
and $\neq 0$.*

Indeed, if $x$ is the generic point of one of the irreducible components $Z$ of $Supp(\mathcal{F})$, it follows from the
equivalence of a) and c') in `(3.1.3)` that $x$ belongs to $Ass(\mathcal{F})$, and $Z$ is an associated prime cycle of
$\mathcal{F}$, necessarily maximal by virtue of `(3.1.1.1)`; the converse follows trivially from `(3.1.1.1)`. Finally,
the last assertion, being evidently local, follows from Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 2 of prop. 7.

**Corollary (3.1.5).**

<!-- label: IV.3.1.5 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. For $\mathcal{F} =
0$, it is necessary and sufficient that $Ass(\mathcal{F}) = \emptyset$.*

The question being local, we are reduced to the case where $X$ is affine, and the conclusion follows immediately from
`(3.1.2)` and from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, cor. 1 of prop. 2.

**Proposition (3.1.6).**

<!-- label: IV.3.1.6 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module; then $Ass(\mathcal{F})$
is locally finite (that is to say, every point of $X$ admits a neighbourhood whose intersection with $Ass(\mathcal{F})$
is finite).*

It suffices to consider the case where $X$ is affine, hence Noetherian, and then the proposition follows from `(3.1.2)`
and from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, cor. of th. 2.

<!-- original page 38 -->

**Proposition (3.1.7).**

<!-- label: IV.3.1.7 -->

*Let $X$ be a prescheme.*

*(i) Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence of quasi-coherent
$\mathcal{O}_{X}$-Modules. Then `Ass(ℱ') ⊂ Ass(ℱ) ⊂ Ass(ℱ') ∪ Ass(ℱ'')`.*

*(ii) Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module, $(\mathcal{F}_{\alpha})$ a family of
quasi-coherent sub-$\mathcal{O}_{X}$-Modules of $\mathcal{F}$ such that $\mathcal{F}$ is the union of the
$\mathcal{F}_{\alpha}$. Then $Ass(\mathcal{F}) = \bigcup_{\alpha} Ass(\mathcal{F}_{\alpha})$.*

*(iii) For every family $(\mathcal{F}_{\alpha})$ of quasi-coherent $\mathcal{O}_{X}$-Modules, one has
$Ass(\bigoplus_{\alpha} \mathcal{F}_{\alpha}) = \bigcup_{\alpha} Ass(\mathcal{F}_{\alpha})$.*

One is immediately reduced to the corresponding propositions for modules (Bourbaki, *loc. cit.*, §1, n° 1, formula (1),
prop. 3 and cor. 1 of prop. 3).

**Proposition (3.1.8).**

<!-- label: IV.3.1.8 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, $U$ an open subset
of $X$, $\mathfrak{J}$ a coherent Ideal of $\mathcal{O}_{X}$ defining a closed sub-prescheme of $X$ having $X - U$ as
underlying space. The following conditions are equivalent:*

*a) $Ass(\mathcal{F}) \subset U$.*

*b) For every affine open subset $V$, every section of $\mathcal{F}$ over $V$ whose restriction to $V \cap U$ is zero,
is equal to `0`.*

*c) The canonical homomorphism $\mathcal{F} \to \mathcal{H}om_{\mathcal{O}_{X}}(\mathfrak{J}, \mathcal{F})$ is
injective.*

The question being local, we may suppose $X = \operatorname{Spec}(A)$ affine, $A$ being a Noetherian ring, $\mathcal{F}
= \tilde{M}$, $M$ an $A$-module, and $\mathfrak{J} = \tilde{\mathfrak{J}}$, where $\mathfrak{J}$ is an ideal of $A$. The
homomorphism $M \to \operatorname{Hom}_{A}(\mathfrak{J}, M)$ associates to $m \in M$ the homomorphism $x \mapsto x m$
from $\mathfrak{J}$ to $M$; to say that it is not injective means that there exists $m \neq 0$ in $M$ such that
$\mathfrak{J} m = 0$.

Let us first show that c) implies a): indeed, if $Ass(\mathcal{F})$ then met $X - U$, there would be a prime ideal
$\mathfrak{p} \in Ass(M)$ containing $\mathfrak{J}$, hence an element $m \neq 0$ of $M$ such that $\mathfrak{p} m = 0$.
Secondly, b) implies c): indeed, if one then had $\mathfrak{J} m = 0$ for some $m \neq 0$ in $M$, then for every prime
ideal $\mathfrak{q} \nsupseteq \mathfrak{J}$, there exists $a \in \mathfrak{J}$ not in $\mathfrak{q}$, hence the
relation $a m = 0$ entails that the canonical image of $m$ in $M_{\mathfrak{q}}$ is `0`; in other words $m$ would be a
section $\neq 0$ of $\mathcal{F}$ over $X$ whose restriction to $U$ would be zero. Finally, a) entails b). To see this,
let us note that the canonical homomorphism $M \to \prod_{\mathfrak{p} \in Ass(M)} M_{\mathfrak{p}}$ is injective:
indeed, if $N$ is the kernel of this homomorphism, one has $Ass(N) \subset Ass(M)$; if there existed $\mathfrak{p} \in
Ass(N)$, there would be an element $n \in N$ whose annihilator would be $\mathfrak{p}$; but by definition of $N$, there
is an element $s \notin \mathfrak{p}$ such that $s n = 0$, which is absurd; one concludes that $Ass(N) = \emptyset$,
whence $N = 0$. Now condition a) entails that if $m \in M$ is a section of $\mathcal{F}$ whose restriction to $U$ is
zero, the canonical image of $m$ in $M_{\mathfrak{p}}$ is zero for every $\mathfrak{p} \in Ass(M)$, hence $m = 0$.
Q.E.D.

**Corollary (3.1.9).**

<!-- label: IV.3.1.9 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, $f$ a section of
$\mathcal{O}_{X}$ over $X$. For $f$ to be $\mathcal{F}$-regular `(0, 15.2.2)`, it is necessary and sufficient that
$Ass(\mathcal{F}) \subset X_{f}$.*

Indeed, it is immediate that to say that $f$ is $\mathcal{F}$-regular means that the canonical homomorphism $\mathcal{F}
\to \mathcal{H}om_{\mathcal{O}_{X}}(f \mathcal{O}_{X}, \mathcal{F})$ is injective, and it suffices to apply `(3.1.8)` to
the Ideal $\mathfrak{J} = f \mathcal{O}_{X}$.

<!-- original page 39 -->

**Proposition (3.1.10).**

<!-- label: IV.3.1.10 -->

*Let $X$, $Y$ be locally Noetherian preschemes, $f : X \to Y$ an integral morphism. Then, for every quasi-coherent
$\mathcal{O}_{X}$-Module $\mathcal{F}$, one has $f(Ass(\mathcal{F})) = Ass(f_{*}(\mathcal{F}))$.*

The question being local on $Y$ and the morphism $f$ being affine, one is immediately reduced to the case where $Y$ is
affine; in other words, to the

**Lemma (3.1.10.1).**

<!-- label: IV.3.1.10.1 -->

*Let $A$, $B$ be two Noetherian rings, $\rho : A \to B$ a ring homomorphism making $B$ into an integral $A$-algebra, $M$
a $B$-module. Then the prime ideals $\mathfrak{p} \in Ass(M_{[\rho]})$ are the inverse images by $\rho$ of the prime
ideals $\mathfrak{q} \in Ass(M)$.*

Indeed, if $\mathfrak{q} \in Ass(M)$, $\mathfrak{q}$ is the annihilator in $B$ of an element $x \in M$, hence
$\rho^{-1}(\mathfrak{q})$ is the annihilator in $A$ of $x$. Conversely, let $\mathfrak{p} \in Ass(M_{[\rho]})$, so that
$\mathfrak{p}$ is the inverse image by $\rho$ of the annihilator $\mathfrak{b}$ in $B$ of an element $x \in M$; it
follows from the first theorem of Cohen-Seidenberg that there exists a prime ideal $\mathfrak{q}$ of $B$ containing
$\mathfrak{b}$ and whose inverse image is $\mathfrak{p}$ (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, cor. 2 of th. 1);
on considering one of the prime ideals minimal among those contained in $\mathfrak{q}$ and containing $\mathfrak{b}$, we
may evidently suppose that $\mathfrak{q}$ itself is one of these minimal ideals. But as $B \cdot x \subset M$ is
isomorphic to $B/\mathfrak{b}$, we know that one then has $\mathfrak{q} \in Ass(B/\mathfrak{b}) \subset Ass(M)$
(Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, th. 2).

**Corollary (3.1.11).**

<!-- label: IV.3.1.11 -->

*Under the hypotheses of `(3.1.10)`, for $\mathcal{F}$ to be without embedded associated prime cycle, it suffices that
the same be true of $f_{*}(\mathcal{F})$.*

Suppose indeed that $f_{*}(\mathcal{F})$ has no embedded associated prime cycle. Note that if $A$ is an integral algebra
over a field $k$, all the prime ideals of $A$ are maximal (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, prop. 1); it
follows from `(I, 6.2.2)` that the fibres of $f$ are *discrete* spaces. If $x$, $x'$ are two distinct points of
$Ass(\mathcal{F})$, neither of them can be adherent to the other if $f(x) = f(x')$; and if $f(x) \neq f(x')$, `(3.1.10)`
and the hypothesis entail that neither of the two points $f(x)$, $f(x')$ can be adherent to the other, hence the same is
true of $x$ and $x'$.

**Remark (3.1.12).**

<!-- label: IV.3.1.12 -->

*Under the hypotheses of `(3.1.10)`, it can on the other hand happen that $\mathcal{F}$ is without embedded associated
prime cycle, but not $f_{*}(\mathcal{F})$. Take for example $Y = \operatorname{Spec}(k[T])$ where $k$ is a field
("affine line"), and $X$ the sum of $X_{1} = Y$ and $X_{2} = \operatorname{Spec}(k)$, the morphism $X_{2} \to Y$
corresponding to the canonical homomorphism $k[T] \to k[T]/\mathfrak{m}$, where $\mathfrak{m}$ is the maximal ideal
`(T)`. It is clear that the morphism $f : X \to Y$ is finite; if one takes $\mathcal{F} = \mathcal{O}_{X}$, then
$\mathcal{F}$ is without embedded associated prime cycle, but $f_{*}(\mathcal{F}) = \tilde{M}$, where $M$ is the
`k[T]`-module direct sum of `k[T]` and $k$, hence $Ass(M)$ is formed of the generic point `(0)` of $Y$ and the point
$\mathfrak{m}$.*

**Proposition (3.1.13).**

<!-- label: IV.3.1.13 -->

*Let $X$ be a locally Noetherian prescheme, $U$ an open subset of $X$, $i : U \to X$ the canonical injection. For every
quasi-coherent $\mathcal{O}_{U}$-Module $\mathcal{F}$, one has $Ass(i_{*}(\mathcal{F})) = Ass(\mathcal{F})$.*

Recall that $i_{*}(\mathcal{F})$ is a quasi-coherent $\mathcal{O}_{X}$-Module `(1.2.2 and 1.7.4)`; as
$i_{*}(\mathcal{F})|U = \mathcal{F}$, one has $(Ass(i_{*}(\mathcal{F}))) \cap U = Ass(\mathcal{F})$, and it therefore
remains to prove that $Ass(i_{*}(\mathcal{F})) \subset U$. But by `(3.1.8)`, this relation means that for every affine
open $V$ of $X$, every section of $i_{*}(\mathcal{F})$ over $V$ which is zero in $U \cap V$, is zero, a condition
trivially verified since $\Gamma(V, i_{*}(\mathcal{F})) = \Gamma(U \cap V, \mathcal{F}) = \Gamma(U \cap V,
i_{*}(\mathcal{F}))$.

<!-- original page 40 -->

### 3.2. Irredundant decompositions

**Proposition (3.2.1).**

<!-- label: IV.3.2.1 -->

*Let $X$ be a locally Noetherian prescheme, $U$ a dense open subset of $X$. The following conditions are equivalent:*

*a) $X$ is reduced.*

*b) The induced sub-prescheme on $U$ is reduced and $X$ is without embedded prime cycle.*

*c) $X$ is without embedded prime cycle and for every generic point $x$ of an irreducible component of $X$, one has
$long(\mathcal{O}_{x}) = 1$.*

*The prime cycles associated to $X$ are then identical to the irreducible components of $X$.*

It is clear that if $X$ is reduced, the same is true of the sub-prescheme induced on $U$. Moreover, the existence of
embedded prime cycles being local, we may restrict to the case where $X = \operatorname{Spec}(A)$ is affine, $A$
Noetherian. If $A$ is reduced, we know that the minimal prime ideals of $A$ form a reduced primary decomposition of
`(0)` (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, prop. 10) and are the elements of $Ass(A)$, hence there exist no
embedded prime ideals associated to $A$, which shows that a) implies b). It is immediate that b) entails c), since a
generic point $x$ of an irreducible component of $X$ belongs to $U$, hence $\mathcal{O}_{x}$ is a field. Finally, c)
entails a): it suffices indeed to note that if $\mathcal{N}$ is the Nilradical of $\mathcal{O}_{X}$, which is a coherent
Ideal, $Supp(\mathcal{N})$ cannot contain any of the generic points of the irreducible components of $X$ by hypothesis;
if $Supp(\mathcal{N})$ were not empty and if $x$ were one of the maximal points of this closed set, the criterion
`(3.1.3, c'))` would show that $x \in Ass(\mathcal{O}_{X})$, and $\overline{x}$ would therefore be an *embedded* prime
cycle of $X$, contrary to the hypothesis; hence $\mathcal{N} = 0$.

**Definition (3.2.2).**

<!-- label: IV.3.2.2 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. We say that $\mathcal{F}$
is **reduced** if it satisfies the two following conditions: 1° $\mathcal{F}$ is without embedded associated prime
cycle; 2° for every maximal point $x$ of $Supp(\mathcal{F})$, one has $long(\mathcal{F}_{x}) = 1$.*

Condition 1° means that the associated prime cycles of $\mathcal{F}$ are the irreducible components of
$Supp(\mathcal{F})$ `(3.1.4)`, and condition 2° means that for every generic point $x$ of such a component one has
$long(\mathcal{F}_{x}) = 1$.

For an affine scheme $X$, this definition gives in particular the notion of *reduced module* on a Noetherian ring $A$;
an $A$-module of finite type $M$ is said to be *reduced* if it has no embedded associated prime ideals and if, for every
$\mathfrak{p} \in Ass(M)$, $long_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) = 1$. Returning to the case of a locally
Noetherian prescheme $X$ and of a coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, we say that $\mathcal{F}$ is *reduced
at a point* $x \in X$ if $\mathcal{F}_{x}$ is a reduced $\mathcal{O}_{x}$-module; that signifies again that, on the
local scheme $\operatorname{Spec}(\mathcal{O}_{x})$, $\tilde{\mathcal{F}}_{x}$ is reduced; it therefore amounts to the
same to say *that $x$ belongs to no embedded associated prime cycle of $\mathcal{F}$ and that $long(\mathcal{F}_{z}) =
1$ for every maximal point $z$ of $Supp(\mathcal{F})$ such that $x \in \overline{z}$*. It is clear that if $\mathcal{F}$
is a reduced coherent $\mathcal{O}_{X}$-Module, it is reduced at every point of $X$; conversely, if $\mathcal{F}$ is
reduced at a point $x$, there exists an open neighbourhood $U$ of $x$ such that $\mathcal{F}|U$ is a reduced
$\mathcal{O}_{U}$-Module: it suffices indeed to take $U$ meeting no embedded associated prime cycle of $\mathcal{F}$
(such a neighbourhood exists since these cycles form a locally finite set of closed parts

<!-- original page 41 -->

of $X$). To say that $\mathcal{O}_{X}$ is reduced at a point $x$ amounts to saying that $X$ is reduced at the point $x$.

**Proposition (3.2.3).**

<!-- label: IV.3.2.3 -->

*Let $X$ be a locally Noetherian prescheme, $U$ an open subset of $X$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module
such that $U \cap Supp(\mathcal{F})$ is dense in $Supp(\mathcal{F})$. The following conditions are equivalent:*

*a) $\mathcal{F}$ is reduced.*

*b) $\mathcal{F}|U$ is reduced and $\mathcal{F}$ is without embedded associated prime cycle.*

*c) There exist a reduced closed sub-prescheme $X'$ of $X$ and a coherent $\mathcal{O}_{X'}$-Module $\mathcal{F}'$
torsion-free and of rank 1 on every irreducible component of $X'$ such that, if $j : X' \to X$ is the canonical
injection, one has $j_{*}(\mathcal{F}') = \mathcal{F}$.*

*Moreover, when this is so, the sub-prescheme $X'$ is defined by the Ideal $\mathfrak{J}$ of $\mathcal{O}_{X}$
annihilator of $\mathcal{F}$.*

To see that c) implies a), one may, by virtue of `(3.1.3)`, restrict to the case where $X' = X$ is integral, with
generic point $x$, and one may moreover suppose $X = \operatorname{Spec}(A)$ affine and $\mathcal{F} = \tilde{M}$, where
$A$ is therefore integral and $M$ is a torsion-free $A$-module of rank 1; the annihilator of every element of $M$ then
being reduced to `0`, one has $Ass(\mathcal{F}) = {x}$ and $\mathcal{F}_{x}$ is isomorphic to $\mathcal{O}_{x}$, the
field of fractions of $A$, so the conditions of definition `(3.2.2)` are satisfied. As the existence of embedded
associated prime cycles is local, it is clear that if $\mathcal{F}$ has no such cycles and if $U \cap Supp(\mathcal{F})$
is dense in $Supp(\mathcal{F})$, then $Ass(\mathcal{F}) = Ass(\mathcal{F}|U)$, hence a) and b) are equivalent. If a) is
satisfied, take for $X'$ the reduced closed sub-prescheme of $X$ whose underlying space is $Supp(\mathcal{F})$
`(I, 5.2.1)`, and let $\mathcal{F}' = j*(\mathcal{F})$; a point $x$ of $Ass(\mathcal{F})$ is necessarily a maximal point
of $X'$, and as $long(\mathcal{F}_{x}) = 1$, $\mathcal{F}'_{x}$ is isomorphic to $\mathcal{F}_{x}$, hence to the field
$k(x) = \mathcal{O}_{X', x}$, which proves that $\mathcal{F}'$ is torsion-free and of rank `1` `(I, 7.4.6 and 7.4.2)`.
Finally, the last assertion is trivial, since for every $y \in X'$, the annihilator of the $\mathcal{O}_{X', y}$-Module
$\mathcal{F}'_{y}$ is zero.

**Definition (3.2.4).**

<!-- label: IV.3.2.4 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. We say that
$\mathcal{F}$ is **irredundant** if $Ass(\mathcal{F})$ is reduced to a single element $x$; if $\mathcal{F}$ is of finite
type, we say that $\mathcal{F}$ is **integral** if moreover $\mathcal{F}$ is reduced (in other words if
$long(\mathcal{F}_{x}) = 1$). We say that a quasi-coherent sub-$\mathcal{O}_{X}$-Module $\mathcal{G}$ of a
quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ is **primary in $\mathcal{F}$** if $\mathcal{F}/\mathcal{G}$ is
irredundant.*

For an affine scheme $X$, this definition gives in particular the notion of *integral module* on a Noetherian ring $A$;
an $A$-module $M$ is said to be *integral* if it is of finite type, if $M$ is primary (that is, $Ass(M)$ is reduced to a
single prime ideal $\mathfrak{p}$) and if moreover $long_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) = 1$. Returning to the
case of an arbitrary locally Noetherian prescheme $X$ and of a coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, we say
that $\mathcal{F}$ is *integral at a point* $x \in X$ if $\mathcal{F}_{x}$ is an integral $\mathcal{O}_{x}$-module: that
means again that $x$ belongs to only a single associated prime cycle (necessarily non-embedded) of $\mathcal{F}$ and
that $long(\mathcal{F}_{z}) = 1$ at its generic point $z$. It is clear that if $\mathcal{F}$ is an integral coherent
$\mathcal{O}_{X}$-Module, it is integral at every point of $X$; conversely, if $\mathcal{F}$ is integral at a point $x$,
there exists an open neighbourhood $U$ of $x$ such that $\mathcal{F}|U$ is

<!-- original page 42 -->

an integral $\mathcal{O}_{U}$-Module: it suffices indeed to take $U$ such that $\mathcal{F}|U$ is a reduced
$\mathcal{O}_{U}$-Module `(3.2.2)`.

We say that the locally Noetherian prescheme $X$ is *irredundant* if $\mathcal{O}_{X}$ is irredundant (which implies
that $X$ is *irreducible*); for $X$ to be *integral*, it is necessary and sufficient that the $\mathcal{O}_{X}$-Module
$\mathcal{O}_{X}$ be integral (`(I, 2.1.8)` and `(3.2.1)`). If $\mathcal{O}_{X}$ is integral at a point $x$, that is, if
the ring $\mathcal{O}_{x}$ is integral, we say that $X$ is *integral at the point* $x$. We say that a closed
sub-prescheme $Y$ of $X$ is *primary in $X$* if the Ideal $\mathfrak{J}$ of $\mathcal{O}_{X}$ that defines $Y$ is
primary in $\mathcal{O}_{X}$.

**Definition (3.2.5).**

<!-- label: IV.3.2.5 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. We call an **irredundant
decomposition** of $\mathcal{F}$ a family $(\mathcal{F}_{\alpha})_{\alpha \in I}$ of $\mathcal{O}_{X}$-Module quotients
of $\mathcal{F}$ such that the $\mathcal{F}_{\alpha}$ are irredundant, the family $(Supp(\mathcal{F}_{\alpha}))$ is
locally finite, and the canonical homomorphism $\mathcal{F} \to \bigoplus_{\alpha} \mathcal{F}_{\alpha}$ is injective.
We say that such a decomposition is **reduced** if the sets $Ass(\mathcal{F}_{\alpha})$ are pairwise distinct, and if
there exists no subset $J \neq I$ such that the sub-family $(\mathcal{F}_{\alpha})_{\alpha \in J}$ is an irredundant
decomposition of $\mathcal{F}$.*

If $(\mathcal{F}_{\alpha})_{\alpha \in I}$ is an irredundant decomposition (resp. reduced irredundant decomposition) of
$\mathcal{F}$ and if one sets $\mathcal{F}_{\alpha} = \mathcal{F}/\mathcal{G}_{\alpha}$, we also say that the family
$(\mathcal{G}_{\alpha})_{\alpha \in I}$ of sub-$\mathcal{O}_{X}$-Modules of $\mathcal{F}$ is a *primary decomposition*
of `0` in $\mathcal{F}$; we note that the hypothesis of injectivity of the canonical homomorphism $\mathcal{F} \to
\bigoplus_{\alpha} \mathcal{F}_{\alpha}$ is equivalent to the condition $\bigcap_{\alpha \in I} \mathcal{G}_{\alpha} =
0$.

If $(\mathcal{F}_{\alpha})$ is an irredundant decomposition of $\mathcal{F}$, to say that it is reduced is equivalent to
saying that the $Ass(\mathcal{F}_{\alpha})$ are pairwise distinct and contained in $Ass(\mathcal{F})$; if
$Ass(\mathcal{F}_{\alpha}) = {x_{\alpha}}$ for every $\alpha \in I$, $\alpha \mapsto x_{\alpha}$ is a bijection of $I$
onto $Ass(\mathcal{F})$: these properties are indeed local and therefore result from Bourbaki, *Alg. comm.*, chap. IV,
§2, n° 3, prop. 4.

**Proposition (3.2.6).**

<!-- label: IV.3.2.6 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Then there exists a
reduced irredundant decomposition $(\mathcal{F}^{(x)})_{x \in Ass(\mathcal{F})}$ formed of coherent
$\mathcal{O}_{X}$-Modules such that for every $x \in Ass(\mathcal{F})$, one has $Ass(\mathcal{F}^{(x)}) = {x}$. For
every $x \in Ass(\mathcal{F})$ such that $\overline{x}$ is not embedded, $\mathcal{F}^{(x)}$ is uniquely determined as
the image of the canonical homomorphism $\mathcal{F} \to i_{*}(i^{*}(\mathcal{F}))$, where $i$ is the canonical morphism
$\operatorname{Spec}(k(x)) \to X$.*

For every $x \in Ass(\mathcal{F})$, let $U$ be an affine open neighbourhood of $x$, with ring $A$, and let
$\mathcal{F}|U = \tilde{M}$, where $M$ is an $A$-module of finite type. We know (Bourbaki, *Alg. comm.*, chap. IV, §1,
n° 1, prop. 4) that there exists a sub-module $N$ of $M$ such that, if one sets $P = M/N$, one has $Ass(P) = {x}$ and
$Ass(N) = Ass(M) - {x}$. Let $\mathcal{G} = \tilde{P}$, which is a quasi-coherent $\mathcal{O}_{U}$-Module, and let $j$
be the canonical injection $U \to X$; let $u : j*(\mathcal{F}) \to \mathcal{G}$ be the surjective homomorphism
corresponding to the homomorphism $M \to P$; from this one deduces a homomorphism $j_{*}(u) : j_{*}(j*(\mathcal{F})) \to
j_{*}(\mathcal{G})$, whence by composition a homomorphism

```text
                            ρ_ℱ                j_*(u)
                  v : ℱ ──────→ j_*(j*(ℱ)) ────────→ j_*(𝒢)
```

of which $u$ is the restriction to $U$; we shall designate by $\mathcal{F}^{(x)}$ the image of $\mathcal{F}$ by this
homomorphism, which is a coherent $\mathcal{O}_{X}$-Module `(I, 6.1.1)`. One has $Ass(j_{*}(\mathcal{G})) = {x}$ by
virtue of `(3.1.13)`, and a fortiori `(3.1.7)` $Ass(\mathcal{F}^{(x)}) = {x}$, since $\mathcal{F}^{(x)} \neq 0$.
Moreover, if

<!-- original page 43 -->

$\mathcal{N}^{(x)} = Ker(v)$, one has $\mathcal{N}^{(x)}|U = \tilde{N}$, hence $x \notin Ass(\mathcal{N}^{(x)})$. It
follows that the homomorphism $\mathcal{F} \to \bigoplus_{x \in Ass(\mathcal{F})} \mathcal{F}^{(x)}$ is injective, for
its kernel $\mathcal{H}$ is contained in every $\mathcal{N}^{(x)}$, hence $Ass(\mathcal{H})$ is contained in the
intersection of the $Ass(\mathcal{N}^{(x)})$, which is empty; consequently `(3.1.5)`, $\mathcal{H} = 0$. Taking into
account that $Ass(\mathcal{F})$ is locally finite `(3.1.6)`, it is clear that $(\mathcal{F}^{(x)})_{x \in
Ass(\mathcal{F})}$ is a reduced irredundant decomposition of $\mathcal{F}$ verifying the conditions of the statement.
The characterization of $\mathcal{F}^{(x)}$ when $\overline{x}$ is not embedded follows from Bourbaki, *Alg. comm.*,
chap. IV, §2, n° 3, prop. 5, the question being local, and taking account of `(I, 1.6.7)`.

**Corollary (3.2.7).**

<!-- label: IV.3.2.7 -->

*Under the hypotheses of `(3.2.6)`, if $\mathcal{F}$ has no embedded associated prime cycle, there exists only one
reduced irredundant decomposition of $\mathcal{F}$.*

**Corollary (3.2.8).**

<!-- label: IV.3.2.8 -->

*Let $X$ be a Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. There exists a finite filtration
$(\mathcal{F}_{i})_{0 \leq i \leq n}$ of $\mathcal{F}$ such that $\mathcal{F}_{0} = \mathcal{F}$, $\mathcal{F}_{n} = 0$,
formed of coherent $\mathcal{O}_{X}$-Modules and such that the quotients $\mathcal{F}_{i}/\mathcal{F}_{i+1}$ are zero or
irredundant, and $Ass(\mathcal{F}_{i}/\mathcal{F}_{i+1}) \subset Ass(\mathcal{F})$.*

Indeed, $\mathcal{F}$ is isomorphic to a sub-$\mathcal{O}_{X}$-Module of a finite direct sum $\bigoplus^{n}_{j=1}
\mathcal{G}_{j}$, where the $\mathcal{G}_{j}$ are irredundant and coherent `(3.2.6)`; as every quasi-coherent
sub-$\mathcal{O}_{X}$-Module of $\mathcal{G}_{j}$ is zero or irredundant `(3.1.7)`, the $\mathcal{F}_{i} = \mathcal{F}
\cap (\bigoplus^{n-i}_{j=1} \mathcal{G}_{j})$ answer the question, $\mathcal{F}_{i}/\mathcal{F}_{i+1}$ being isomorphic
to a coherent sub-$\mathcal{O}_{X}$-Module of $\mathcal{G}_{n-i}$.

### 3.3. Relations with flatness

**Proposition (3.3.1).**

<!-- label: IV.3.3.1 -->

*Let $f : X \to Y$ be a morphism, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module and $f$-flat, $\mathcal{G}$ a
quasi-coherent $\mathcal{O}_{Y}$-Module. If, for every $y \in Y$, one sets $\mathcal{F}_{y} = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} k(y)$, one has*

```text
(3.3.1.1)                       Ass(ℱ ⊗_{𝒪_Y} 𝒢) ⊃ ⋃_{y ∈ Ass(𝒢)} Ass(ℱ_y)
```

*and the two sides are equal if $Y$ is locally Noetherian.*

(Of course, $\mathcal{F}_{y}$ is a sheaf on the fibre $f^{-1}(y)$, and one identifies this fibre with a subspace of $X$
`(I, 3.6.1)`.) The question being local on $X$ and on $Y$, one is reduced to the case where $X$ and $Y$ are affine, and
the proposition is then proved in Bourbaki, *Alg. comm.*, chap. IV, §2, n° 6, th. 2.

**Corollary (3.3.2).**

<!-- label: IV.3.3.2 -->

*Let $Y$ be a locally Noetherian prescheme without embedded associated prime cycles, $f : X \to Y$ a morphism,
$\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module and $f$-flat. Then, for every $x \in Ass(\mathcal{F})$, $f(x)$
is a maximal point of $Y$.*

It suffices to apply `(3.3.1)` with $\mathcal{G} = \mathcal{O}_{Y}$, since $Ass(\mathcal{O}_{Y})$ is by hypothesis the
set of maximal points of $Y$.

**Corollary (3.3.3).**

<!-- label: IV.3.3.3 -->

*Under the hypotheses of `(3.3.1)`, suppose in addition that $X$ and $Y$ are locally Noetherian, $\mathcal{E}$ and
$\mathcal{F}$ coherent. Then the following conditions are equivalent:*

*a) $\mathcal{E} \otimes_{Y} \mathcal{F}$ is without embedded associated prime cycle.*

*b) For every point $y \in Ass(\mathcal{E}) \cap f(Supp(\mathcal{F}))$, $\overline{y}$ is a non-embedded associated
prime cycle of $\mathcal{E}$ and $\mathcal{E}_{y} \otimes \mathcal{F}_{y}$ is without embedded associated prime cycle.*

<!-- original page 44 -->

Suppose a) verified. The hypotheses imply that $\mathcal{E} \otimes_{Y} \mathcal{F}$ is a coherent
$\mathcal{O}_{X}$-Module $(0_{I}, 5.3.11 and 5.3.5)$; its associated prime cycles are therefore the irreducible
components of $Supp(\mathcal{E} \otimes_{Y} \mathcal{F})$ `(3.1.4)`, and for every maximal point $x$ of
$Supp(\mathcal{E} \otimes_{Y} \mathcal{F})$, $f(x) = y$ is a maximal point of $Supp(\mathcal{E})$ and $x$ a maximal
point of $Supp(\mathcal{F}_{y})$ `(2.5.5)`. Since, by virtue of `(3.3.1)` and the fact that the relation $y \in
f(Supp(\mathcal{F}))$ entails $\mathcal{F}_{y} \neq 0$ `(I, 9.1.13)`, every point of $Ass(\mathcal{E}) \cap
f(Supp(\mathcal{F}))$ is the image by $f$ of a maximal point of $Supp(\mathcal{E} \otimes_{Y} \mathcal{F})$, we see that
condition b) is verified.

Conversely, suppose b) verified, and let us show that if $z$, $z'$ are two distinct points of $Ass(\mathcal{E}
\otimes_{Y} \mathcal{F})$, neither of them can be adherent to the other. First, if $f(z) = f(z') = y$, one has $y \in
Ass(\mathcal{E})$ and $z$ and $z'$ belong to $Ass(\mathcal{F}_{y})$ by `(3.3.1)`, whence $y \in f(Supp(\mathcal{F}))$;
as by hypothesis neither of the two points $z$, $z'$ is adherent to the other in $f^{-1}(y)$, neither of them can be
adherent to the other in $X$. If $y = f(z)$ and $y' = f(z')$ are distinct, they belong to $Ass(\mathcal{E}) \cap
f(Supp(\mathcal{F}))$, hence neither of them can be adherent to the other in $Y$; it follows from the continuity of $f$
that neither of the points $z$, $z'$ can be adherent to the other in $X$.

**Proposition (3.3.4).**

<!-- label: IV.3.3.4 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism, $\mathcal{E}$ a coherent
$\mathcal{O}_{Y}$-Module, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module and $f$-flat. Then the following conditions
are equivalent:*

*a) $\mathcal{E} \otimes_{Y} \mathcal{F}$ is reduced `(3.2.2)`.*

*b) For every point $y \in Ass(\mathcal{E}) \cap f(Supp(\mathcal{F}))$, $\overline{y}$ is a non-embedded associated
prime cycle of $\mathcal{E}$, $long(\mathcal{E}_{y}) = 1$ and $\mathcal{F}_{y}$ is reduced.*

Suppose a) verified. We already know `(3.3.3)` that for every $y \in Ass(\mathcal{E}) \cap f(Supp(\mathcal{F}))$,
$\overline{y}$ is a non-embedded associated prime cycle of $\mathcal{E}$ and $\mathcal{F}_{y}$ is without embedded
associated prime cycle. Moreover `(2.5.5)`, for every $x \in Ass(\mathcal{E} \otimes_{Y} \mathcal{F}) \cap f^{-1}(y)$,
one has `1 = long((ℰ ⊗_Y ℱ)_x) = long(ℰ_y) · long((ℱ_y)_x)`, hence $long(\mathcal{E}_{y}) = long((\mathcal{F}_{y})_{x})
= 1$, which proves b).

Conversely, suppose b) verified; we already know that every point $x \in Ass(\mathcal{E} \otimes_{Y} \mathcal{F})$ is a
maximal point of $Supp(\mathcal{E} \otimes_{Y} \mathcal{F})$, that $y = f(x)$ is a maximal point of $Supp(\mathcal{E})$
and $x$ a maximal point of $Supp(\mathcal{F}_{y})$ `(3.3.1 and 3.3.3)`; moreover it follows from the hypothesis and from
`(2.5.5)` that $long((\mathcal{E} \otimes_{Y} \mathcal{F})_{x}) = 1$, which proves a).

**Corollary (3.3.5).**

<!-- label: IV.3.3.5 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a flat morphism; if $Y$ is reduced at the points of
$f(X)$ and if $f^{-1}(y)$ is a reduced $k(y)$-prescheme for every $y \in f(X)$, then $X$ is reduced.*

Since the Nilradical $\mathcal{N}_{Y}$ is coherent, the set of points where $Y$ is reduced is open $(0_{I}, 5.2.2)$, and
one may restrict to the case where $Y$ is reduced. It then suffices to apply `(3.3.4)` to $\mathcal{E} =
\mathcal{O}_{Y}$ and $\mathcal{F} = \mathcal{O}_{X}$.

**Proposition (3.3.6).**

<!-- label: IV.3.3.6 -->

*Let $f : X \to S$, $g : Y \to S$ be two morphisms, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module,
$\mathcal{G}$ a quasi-coherent $\mathcal{O}_{Y}$-Module. Suppose that: 1° $\mathcal{G}$ is $g$-flat; 2° $X$ is locally
Noetherian, and for every $s \in S$, $g^{-1}(s)$ is locally Noetherian (which will be the case if $Y$ is also locally
Noetherian). Let $Z = X \times_{S} Y$; for every couple $(x, y)$ such that $x \in X$, $y \in Y$ and*

<!-- original page 45 -->

*$f(x) = g(y) = s$, let $T_{x,y}$ be the prescheme $\operatorname{Spec}(k(x) \otimes_{k(s)} k(y))$, and let $I_{x,y}$ be
the image of $Ass(\mathcal{O}_{T_{x,y}})$ by the canonical monomorphism $T_{x,y} \to Z$ `(I, 3.4.9)`. One then has*

```text
(3.3.6.1)              Ass(ℱ ⊗_S 𝒢) = ⋃_{x ∈ Ass(ℱ)} ( ⋃_{y ∈ Ass(𝒢_{f(x)})} I_{x,y} )
```

*where for every $s \in S$, $\mathcal{G}_{s} = \mathcal{G} \otimes_{\mathcal{O}_{S}} k(s)$.*

Let $p : Z \to X$, $q : Z \to Y$ be the canonical projections, so that one has the commutative diagram

```text
                                X ←─── Z
                                       p
                                ↓ f    ↓ q
                                S ←─── Y
                                   g
```

Set $\mathcal{G}' = q*(\mathcal{G})$, so that $\mathcal{F} \otimes_{S} \mathcal{G} = \mathcal{F} \otimes_{X}
\mathcal{G}'$; as $\mathcal{G}'$ is $p$-flat `(2.1.4)`, it follows from `(3.3.1)` that one has

```text
(3.3.6.2)                       Ass(ℱ ⊗_X 𝒢') = ⋃_{x ∈ Ass(ℱ)} Ass(𝒢'_x)
```

with $\mathcal{G}'_{x} = \mathcal{G}' \otimes_{\mathcal{O}_{X}} k(x)$. If $s = f(x)$, one has $\mathcal{G}_{s} =
\mathcal{G} \otimes_{\mathcal{O}_{S}} k(s)$, and $p^{-1}(x) = g^{-1}(s) \otimes_{k(s)} k(x)$; moreover, since the field
$k(x)$ is a flat $k(s)$-module, the morphism $p^{-1}(x) \to g^{-1}(s)$ is flat `(2.1.4)`; applying `(3.3.1)` to this
morphism, it comes

```text
(3.3.6.3)                       Ass(𝒢'_x) = ⋃_{y ∈ Ass(𝒢_s)} Ass(𝒪_{T_{x,y}})
```

whence the proposition.

We note that if, in the statement, one suppresses hypothesis 2°, one may still conclude, by virtue of `(3.3.1)`, the
relation

```text
(3.3.6.4)             Ass(ℱ ⊗_S 𝒢) ⊃ ⋃_{x ∈ Ass(ℱ)} ( ⋃_{y ∈ Ass(𝒢_{f(x)})} I_{x,y} ).
```

**Corollary (3.3.7).**

<!-- label: IV.3.3.7 -->

*Under the hypotheses of `(3.3.6)`, suppose in addition that $S$ is locally Noetherian and that $f(Ass(\mathcal{F}))
\subset Ass(\mathcal{O}_{S})$. Then one has*

```text
(3.3.7.1)                             Ass(ℱ ⊗_S 𝒢) = ⋃_{(x,y) ∈ C} I_{x,y}
```

*where $C$ is the set of couples $(x, y)$ such that $x \in Ass(\mathcal{F})$, $y \in Ass(\mathcal{G})$ and $f(x) =
g(y)$.*

Since $\mathcal{G}$ is $g$-flat, it follows indeed from `(3.3.1)` that the relation "$s \in Ass(\mathcal{O}_{S})$ and $y
\in Ass(\mathcal{G}_{s})$" is equivalent to $y \in Ass(\mathcal{G})$: the conclusion follows from `(3.3.6.1)`.

**Remarks (3.3.8).**

<!-- label: IV.3.3.8 -->

*We shall see later `(4.2.2)` that under the hypotheses of `(3.3.6)`, $T_{x,y}$ is a prescheme without embedded
associated prime cycle; it will follow that if $\mathcal{F}$ and the $\mathcal{G}_{s}$ are without embedded associated
prime cycle, the same is true of $\mathcal{F} \otimes_{S} \mathcal{G}$.*

**Corollary (3.3.9).**

<!-- label: IV.3.3.9 -->

*Under the conditions of `(3.3.7)`, one has*

```text
(3.3.9.1)                             q(Ass(ℱ ⊗_S 𝒢)) ⊂ Ass(𝒢)
```

*(where $q : X \times_{S} Y \to Y$ is the canonical projection).*

Indeed, if $(x, y) \in Z$, one has $q(I_{x,y}) = {y} \subset Ass(\mathcal{G})$.

<!-- original page 46 -->

### 3.4. Properties of the sheaves $\mathcal{F}/t\mathcal{F}$

**Proposition (3.4.1).**

<!-- label: IV.3.4.1 -->

*Let $X$ be a locally Noetherian prescheme, $t$ a section of $\mathcal{O}_{X}$ over $X$, $Y$ the closed sub-prescheme of
$X$ defined by the Ideal $t \mathcal{O}_{X}$ of $\mathcal{O}_{X}$. Let $\mathcal{F}$ be a coherent
$\mathcal{O}_{X}$-Module, $S$ the reduced closed sub-prescheme of $X$ having $Supp(\mathcal{F})$ as underlying space,
$(S_{i})$ the family of reduced closed sub-preschemes of $X$ having as underlying spaces the irreducible components of
$S$; we designate by $s_{i}$ the generic point of $S_{i}$. Finally, let $Z$ be an irreducible component of
$Supp(\mathcal{F}/t\mathcal{F}) = S \cap Y$, $z$ its generic point.*

*(i) For every $i$ such that $Z \subset S_{i}$, $Z$ is an irreducible component of $S_{i} \cap Y$.*

*(ii) If $Z$ is not equal to any of the $S_{i}$, one has*

$$ (3.4.1.1) long((\mathcal{F}/t\mathcal{F})_{z}) \geq \sum_{i} long(\mathcal{F}_{s_{i}}) $$

*where the sum on the right-hand side is extended to all $i$ such that $Z \subset S_{i}$.*

*(iii) Suppose that $Z$ is equal to none of the $S_{i}$. For the two sides of `(3.4.1.1)` to be equal, it is necessary
and sufficient that the two following conditions be satisfied:*

*α) $t_{z}$ is $\mathcal{F}_{z}$-regular `(0, 15.1.4)`.*

*β) For every $i$ such that $Z \subset S_{i}$, the canonical image of the germ $t_{z}$ in $\mathcal{O}_{S_{i}, z}$
generates the maximal ideal of this ring (which entails that $\mathcal{O}_{S_{i}, z}$ is a discrete valuation ring and
the image of $t_{z}$ a uniformizer of this ring).*

(i) If $j : Y \to X$ is the canonical injection, one has $\mathcal{F}/t\mathcal{F} = \mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{Y} = j*(\mathcal{F})$, hence $Supp(\mathcal{F}/t\mathcal{F}) = j^{-1}(S) = S \cap
Y$ `(I, 9.1.13)`, whence the assertion.

(ii) and (iii). As the $s_{i}$ such that $Z \subset S_{i}$ are those belonging to
$\operatorname{Spec}(\mathcal{O}_{z})$, we may, in order to prove (ii) and (iii), replace $X$ by
$\operatorname{Spec}(\mathcal{O}_{z})$; and if $M = \mathcal{F}_{z}$, we may therefore suppose that $\mathcal{F} =
\tilde{M}$, whence $\mathcal{F}_{s_{i}} = M_{\mathfrak{p}_{i}}$, where we designate by $\mathfrak{p}_{i}$ the minimal
ideals of $\mathcal{O}_{z}$. Moreover, as $M$ is an $\mathcal{O}_{z}$-module of finite type, one has $S = S'_{red}$,
with $S' = \operatorname{Spec}(\mathcal{O}_{z}/\mathfrak{a})$, where $\mathfrak{a}$ is the annihilator of $M$ in
$\mathcal{O}_{z}$ $(0_{I}, 1.7.4)$, and the two sides of `(3.4.1.1)` keep the same values, whether one considers $M$ as
an $\mathcal{O}_{z}$-module or as an $(\mathcal{O}_{z}/\mathfrak{a})$-module; one therefore sees that one can finally
replace $X$ by $S' = \operatorname{Spec}(A)$, where $A$ is a Noetherian local ring, $M$ being a *faithful* $A$-module;
since $Z$ is closed in $S$, the hypothesis that $Z \neq S_{i}$ for every $i$ means that $s_{i} \notin Z$, hence that
$\dim(A) > 0$; finally, to say that $z$ is the generic point of $Z$, an irreducible component of $S \cap V(t)$, means
that $A/tA$ is of dimension `0` (in other words, is a local Artinian ring). One is therefore reduced to proving the
following statement:

**Lemma (3.4.1.2).**

<!-- label: IV.3.4.1.2 -->

*Let $A$ be a Noetherian local ring of dimension `> 0`, $\mathfrak{p}_{i}$ the minimal prime ideals of $A$,
$\mathfrak{m}$ its maximal ideal, $t$ an element of $\mathfrak{m}$ such that $A/tA$ is Artinian. Then, for every
$A$-module of finite type $M$, one has*

$$ (3.4.1.3) long(M/tM) \geq \sum_{i} long(M_{\mathfrak{p}_{i}}); $$

*moreover, for the two sides of `(3.4.1.3)` to be equal, it is necessary and sufficient that the following conditions be
satisfied:*

<!-- original page 47 -->

*α) $t$ is $M$-regular;*

*β) for every $i$ such that $M_{\mathfrak{p}_{i}} \neq 0$, the image of $t$ in $A/\mathfrak{p}_{i}$ generates the
maximal ideal of this ring (which entails that $A/\mathfrak{p}_{i}$ is a discrete valuation ring).*

As $A$ is not of dimension `0` and $A/tA$ is Artinian, one has necessarily $\dim(A) = 1$ `(0, 16.3.4)` and $t \notin
\mathfrak{p}_{i}$ for every $i$: the principal ideal `(t)` is therefore an ideal of definition of $A$, and hence
contains a power of its maximal ideal $\mathfrak{m}$. Let $N$ be the submodule of elements of $M$ annihilated by a power
of $t$ (or by a power of $\mathfrak{m}$, which amounts to the same thing as we have just seen); if one sets $P = M/N$,
$t$ is $P$-regular, since the relation $tx \in N$ for an $x \in M$ entails $t^{k}(tx) = 0$ for some integer $k$, hence
$x \in N$. This being so, one has the

**Lemma (3.4.1.4).**

<!-- label: IV.3.4.1.4 -->

*Let $A$ be a ring,*

$$ 0 \to M' \to M \to M'' \to 0 $$

*an exact sequence of $A$-modules. If $t \in A$ is `M''`-regular, the sequence*

$$ 0 \to M'/tM' \to M/tM \to M''/tM'' \to 0 $$

*is exact.*

Since $M/tM = M \otimes_{A} (A/tA)$, it suffices to prove exactness at $M'/tM'$; now, if the image $x \in M$ of an
element $x'$ of $M'$ is such that $x = ty$ with $y \in M$, one deduces, for the images `x''`, `y''` of `x, y` in `M''`,
$x'' = ty''$; but as $x'' = 0$, the hypothesis entails $y'' = 0$, hence $y$ is the image of an element $y' \in M'$, and
the relation $x = ty$ entails $x' = ty'$ since $M' \to M$ is injective.

This lemma established, one derives from it the relation

```text
(3.4.1.5)                       long(M/tM) = long(N/tN) + long(P/tP).
```

On the other hand, for every $i$, one has $N_{\mathfrak{p}_{i}} = 0$ since $t \notin \mathfrak{p}_{i}$, hence
$M_{\mathfrak{p}_{i}} = P_{\mathfrak{p}_{i}}$; to prove `(3.4.1.3)`, it suffices to do so by replacing $M$ by $P$; on
the other hand, if the two sides of `(3.4.1.3)` are equal, it follows from the same inequality for $P$ and from
`(3.4.1.5)` that one necessarily has $long(N/tN) = 0$, hence $N/tN = 0$ and finally $N = 0$, by Nakayama's lemma, $N$
being of finite type; now, $N = 0$ means that $t$ is $M$-regular. One may therefore reduce to the case where $M = P$,
that is, suppose already that $t$ is $M$-regular. Note that this entails $\mathfrak{m} \notin Ass(M)$, since $t$ cannot
annihilate an element $\neq 0$ of $M$. As $A$ is of dimension `1`, one therefore has necessarily $Ass(M) \subset
\bigcup_{i} {\mathfrak{p}_{i}}$.

Let us then proceed by induction on $n = \sum_{i} long(M_{\mathfrak{p}_{i}})$. If $n = 0$, one has necessarily
$M_{\mathfrak{p}_{i}} = 0$ for every $i$, hence $M = 0$ since none of the $\mathfrak{p}_{i}$ belongs to $Ass(M)$; the
two sides of `(3.4.1.3)` are then zero, and assertion β) of `(3.4.1.2)` is trivial. If $n > 0$, the reasoning at the
beginning of the proof of `(3.4.1)` allows us to suppose moreover that the $A$-module $M$ is faithful: this entails
$M_{\mathfrak{p}_{i}} \neq 0$ for every $i$ (Bourbaki, *Alg. comm.*, chap. II, §2, n° 2, cor. 2 of prop. 4), and
consequently $Ass(M) = \bigcup_{i} {\mathfrak{p}_{i}}$.

Suppose first $n = 1$; there is then only a single minimal prime ideal $\mathfrak{p}$ of $A$,

<!-- original page 48 -->

and to say that $M_{\mathfrak{p}}$ is of length `1` means that $M_{\mathfrak{p}}$ is isomorphic to the residue field $k
= A_{\mathfrak{p}}/\mathfrak{p} A_{\mathfrak{p}}$ as an $A_{\mathfrak{p}}$-module. Consequently $M_{\mathfrak{p}}$ is
annihilated by $\mathfrak{p} A_{\mathfrak{p}}$, hence $\mathfrak{p}$ is the annihilator of $M$ (Bourbaki, *Alg. comm.*,
chap. II, §2, n° 4, formula (9)), which entails $\mathfrak{p} = 0$ since $M$ is supposed faithful; the ring $A$ is
therefore integral. This being so, the hypothesis $M \neq 0$ entails $M/tM \neq 0$ by Nakayama's lemma, and consequently
$long(M/tM) \geq 1$, which proves `(3.4.1.3)` in this case. Moreover, if $long(M/tM) = 1$, $M$ is necessarily monogenic
(Bourbaki, *Alg. comm.*, chap. II, §3, n° 2, cor. 2 of prop. 4), hence isomorphic to a quotient $A/\mathfrak{b}$; since
it is faithful, one necessarily has $\mathfrak{b} = 0$ and $M$ is isomorphic to $A$; as $long(A/tA) = 1$, `tA` is
necessarily equal to the maximal ideal $\mathfrak{m}$, and as $A$ is a Noetherian integral local ring, this proves that
$A$ is a discrete valuation ring (Bourbaki, *Alg. comm.*, chap. VI, §3, n° 6, prop. 9), of which $t$ is the uniformizer.
Conversely, if $A$ is a discrete valuation ring, $t$ its uniformizer, $long(M_{\mathfrak{p}}) = 1$ and if $t$ is
$M$-regular, then $M$ is torsion-free, hence isomorphic to a sub-module of $A$ ($M$ being of finite type), and
consequently isomorphic to $A$ itself, whence $long(M/tM) = long(A/tA) = 1$.

Suppose now $n \geq 2$; there then exists an exact sequence

$$ 0 \to M' \to M \to M'' \to 0 $$

with $M' \neq 0$, $M'' \neq 0$ and `Ass(M) = Ass(M') ∪ Ass(M'')`; indeed, if $Ass(M)$ is not reduced to a single
element, this follows from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, prop. 4; if on the contrary $Ass(M)$ is reduced
to a single prime ideal, this latter is necessarily the unique minimal prime ideal $\mathfrak{p}$ of $A$; the hypothesis
then entails $long(M_{\mathfrak{p}}) \geq 2$ and it suffices to take for $M'$ the inverse image of a submodule of
$M_{\mathfrak{p}}$ distinct from `0` and from $M_{\mathfrak{p}}$. As $t$ is $M$-regular, $t$ does not belong to any of
the prime ideals of $Ass(M)$ (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, cor. 2 of prop. 2), hence, for the same
reason, $t$ is $M'$-regular and `M''`-regular. This last property entails by `(3.4.1.4)` that the sequence

$$ 0 \to M'/tM' \to M/tM \to M''/tM'' \to 0 $$

is exact; as it is moreover the case for the sequence

$$ 0 \to M'_{\mathfrak{p}_{i}} \to M_{\mathfrak{p}_{i}} \to M''_{\mathfrak{p}_{i}} \to 0 $$

for every $i$, one has

```text
                  long(M/tM)     = long(M'/tM') + long(M''/tM'')
                  long(M_{𝔭_i})  = long(M'_{𝔭_i}) + long(M''_{𝔭_i})
```

and the induction hypothesis therefore entails the inequality `(3.4.1.3)`. Moreover the two sides cannot be equal unless
the analogous inequalities for $M'$ and `M''` are also equalities. By virtue of the induction hypothesis, this is
equivalent to property β) for the $\mathfrak{p}_{i}$ such that $M'_{\mathfrak{p}_{i}} \neq 0$ or $M''_{\mathfrak{p}_{i}}
\neq 0$; but these ideals are precisely those for which $M_{\mathfrak{p}_{i}} \neq 0$. Q.E.D.

<!-- original page 49 -->

**Corollary (3.4.2).**

<!-- label: IV.3.4.2 -->

*Under the general hypotheses of `(3.4.1)`, suppose that $Z$ is not equal to any of the $S_{i}$ and that
$long((\mathcal{F}/t\mathcal{F})_{z}) = 1$. Then there exists only one of the $S_{i}$ containing $Z$, and for this value
of $i$, one has $long(\mathcal{F}_{s_{i}}) = 1$; moreover $\mathcal{O}_{S_{i}, z}$ is a discrete valuation ring of which
$t_{z}$ is a uniformizer, and $t_{z}$ is $\mathcal{F}_{z}$-regular.*

This results from `(3.4.1)`, the two sides of `(3.4.1.1)` then being equal.

**Proposition (3.4.3).**

<!-- label: IV.3.4.3 -->

*Let $X$ be a locally Noetherian prescheme, $t$ a section of $\mathcal{O}_{X}$ over $X$, $Y$ the closed sub-prescheme of
$X$ defined by the Ideal $t \mathcal{O}_{X}$ of $\mathcal{O}_{X}$. Let $\mathcal{F}$ be a coherent
$\mathcal{O}_{X}$-Module, $T$ an associated prime cycle of $\mathcal{F}$, $T'$ an irreducible component of $T \cap Y$,
$x$ the generic point of $T'$. Suppose that $t_{x}$ is $\mathcal{F}_{x}$-regular; then one has $x \in
Ass(\mathcal{F}/t\mathcal{F})$.*

As in the proof of `(3.4.1)`, we can reduce to the case where $X = \operatorname{Spec}(\mathcal{O}_{x})$; the
proposition is then (taking into account `(3.1.2)`) a consequence of `(0, 16.4.6.3)`.

**Proposition (3.4.4).**

<!-- label: IV.3.4.4 -->

*Let $X$ be a locally Noetherian prescheme, $t$ a section of $\mathcal{O}_{X}$ over $X$, $Y$ the closed sub-prescheme of
$X$ defined by the Ideal $t \mathcal{O}_{X}$ of $\mathcal{O}_{X}$. Let $\mathcal{F}$ be a coherent
$\mathcal{O}_{X}$-Module, $(S_{i})$ the family of irreducible components of $Supp(\mathcal{F})$. Let $y$ be a point of
$Y$ such that $t_{y}$ is $\mathcal{F}_{y}$-regular and no embedded associated prime cycle of $\mathcal{F}/t\mathcal{F}$
contains $y$. Then the irreducible components of $Supp(\mathcal{F}/t\mathcal{F})$ that contain $y$ are exactly the
irreducible components of the $S_{i} \cap Y$ that contain $y$, and the associated prime cycles of $\mathcal{F}$
containing $y$ are non-embedded.*

Let us first prove the last assertion. Let $T \supset T_{1}$ be two associated prime cycles of $\mathcal{F}$ containing
$y$; if $x$ is the generic point of an irreducible component of $T \cap Y$ containing $y$, $x$ is a generization of $y$,
hence contained in every neighbourhood of $y$, and the hypothesis that $t_{y}$ is $\mathcal{F}_{y}$-regular entails that
$t_{x}$ is $\mathcal{F}_{x}$-regular `(0, 15.2.4)`, hence, by virtue of `(3.4.3)`, one has $x \in
Ass(\mathcal{F}/t\mathcal{F})$. Let $x_{1}$ be the generic point of an irreducible component of $T_{1} \cap Y$
containing $y$, and let $x$ be the generic point of an irreducible component of $T \cap Y$ containing $x_{1}$; it
follows from what precedes that $x_{1}$ and $x$ both belong to $Ass(\mathcal{F}/t\mathcal{F})$, and as $x_{1} \in
\overline{x}$, the hypothesis entails that $x_{1} = x$. Let us again denote by $T$ and `T_1` the integral closed
sub-preschemes of $X$ having $T$ and `T_1` as underlying spaces respectively, and set $A = \mathcal{O}_{T, x}$, $A_{1} =
\mathcal{O}_{T_{1}, x}$; one has therefore $A_{1} = A/\mathfrak{p}$, where $\mathfrak{p}$ is a prime ideal of $A$. By
the definition of $x$ and $x_{1}$, $A/tA$ and $A_{1}/tA_{1}$ are Artinian rings; on the other hand, we saw above that
$t_{x}$ is $\mathcal{F}_{x}$-regular, hence $x$ cannot belong to $Ass(\mathcal{F})$, and consequently `A_1` is not
Artinian. One therefore has $\dim A = \dim A_{1} = 1$; but this entails $\mathfrak{p} = 0$ and $A = A_{1}$
`(0, 16.1.2.2)`; as $\operatorname{Spec}(A)$ and $\operatorname{Spec}(A_{1})$ are respectively dense in $T$ and `T_1`,
one has indeed $T = T_{1}$.

The $S_{i}$ containing $y$ are therefore all the associated prime cycles of $\mathcal{F}$ containing $y$; if $x$ is the
generic point of an irreducible component of $S_{i} \cap Y$ containing $y$, one again deduces from `(0, 15.2.4)` that
$t_{x}$ is $\mathcal{F}_{x}$-regular, hence, by `(3.4.3)`, that $x \in Ass(\mathcal{F}/t\mathcal{F})$; this proves the
first assertion of `(3.4.4)`.

**Proposition (3.4.5).**

<!-- label: IV.3.4.5 -->

*Let $X$ be a locally Noetherian prescheme, $t$ a section of $\mathcal{O}_{X}$ over $X$, $Y$ the closed sub-prescheme of
$X$ defined by the Ideal $t \mathcal{O}_{X}$ of $\mathcal{O}_{X}$. Let $\mathcal{F}$*

<!-- original page 50 -->

*be a coherent $\mathcal{O}_{X}$-Module, $y$ a point of $Y$; suppose that $t_{y}$ is $\mathcal{F}_{y}$-regular and that
$\mathcal{F}/t\mathcal{F}$ is integral at the point $y$ `(3.2.4)`. Then $\mathcal{F}$ is integral at the point $y$.*

Taking into account `(3.4.4)`, it suffices to prove that $y$ is contained in a single irreducible component of
$Supp(\mathcal{F})$, and that if $s$ is the generic point of this component, one has $long(\mathcal{F}_{s}) = 1$. Now,
by hypothesis, $y$ belongs to only a single irreducible component of $Supp(\mathcal{F}/t\mathcal{F})$, and if $z$ is the
generic point of this component, one has $long((\mathcal{F}/t\mathcal{F})_{z}) = 1$; the conclusion therefore follows
from `(3.4.2)`.

**Proposition (3.4.6).**

<!-- label: IV.3.4.6 -->

*The hypotheses being those of `(3.4.1)`, let $x$ be a point of $Y$. Suppose that $Y$ contains none of the $S_{i}$
containing $x$, and that $\mathcal{F}/t\mathcal{F}$ is reduced at the point $x$ `(3.2.2)`. Then $t_{x}$ is
$\mathcal{F}_{x}$-regular and $\mathcal{F}$ is reduced at the point $x$. Moreover, if $z$ is the generic point of an
irreducible component of $Supp(\mathcal{F}/t\mathcal{F})$ containing $x$, $z$ is contained in a single one of the
$S_{i}$, and $\mathcal{O}_{S_{i}, z}$ is a discrete valuation ring of which $t_{z}$ is a uniformizer.*

The fact that $t_{x}$ is $\mathcal{F}_{x}$-regular results from the following lemma applied to the ring
$\mathcal{O}_{x}$:

**Lemma (3.4.6.1).**

<!-- label: IV.3.4.6.1 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type, $\mathfrak{p}_{i}$ the minimal elements of $Supp(M)$,
$t$ an element of $A$. Suppose that $t$ belongs to none of the $\mathfrak{p}_{i}$ and that $M/tM$ is a reduced
$A$-module `(3.2.2)`. Then $t$ is $M$-regular.*

Every prime ideal $\mathfrak{p} \in Supp(M)$ contains one of the $\mathfrak{p}_{i}$; as $t$ belongs to none of the
$\mathfrak{p}_{i}$, the homothety of ratio $t$ in $M_{\mathfrak{p}}$ is not nilpotent (Bourbaki, *Alg. comm.*, chap. IV,
§1, n° 4, cor. of prop. 9). Let us designate by $N$ the submodule of $M$ formed of elements annihilated by a power of
$t$, and set $P = M/N$; we shall show that $N = 0$. Since $t$ is $P$-regular, one has an exact sequence `(3.4.1.4)`

$$ 0 \to N/tN \to M/tM \to P/tP \to 0. $$

As $N$ is of finite type, it is annihilated by a power of $t$, and it therefore suffices to show that $N/tN = 0$. As
$N/tN$ is a submodule of $M/tM$, it suffices to prove that $(N/tN)_{\mathfrak{p}} = 0$ for every $\mathfrak{p} \in
Ass(M/tM)$, or again that the homomorphism $u_{\mathfrak{p}} : (M/tM)_{\mathfrak{p}} \to (P/tP)_{\mathfrak{p}}$ is
bijective for every $\mathfrak{p} \in Ass(M/tM)$. Now one has $(P/tP)_{\mathfrak{p}} \neq 0$; indeed, as $\mathfrak{p}
\in Supp(M/tM) = Supp(M) \cap V(t)$ $(0_{I}, 1.7.5)$, the image of $t$ in $A_{\mathfrak{p}}$ is contained in the maximal
ideal $\mathfrak{p} A_{\mathfrak{p}}$, hence the hypothesis $P_{\mathfrak{p}} = tP_{\mathfrak{p}}$ would entail
$P_{\mathfrak{p}} = 0$ by Nakayama's lemma; one would therefore have $M_{\mathfrak{p}} = N_{\mathfrak{p}}$ and the
homothety of ratio $t$ in $M_{\mathfrak{p}}$ would be nilpotent; but this contradicts the remark made at the beginning,
since $\mathfrak{p} \in Supp(M)$. This being so, the hypothesis that $M/tM$ is reduced entails
$long((M/tM)_{\mathfrak{p}}) = 1$, and as $(P/tP)_{\mathfrak{p}} \neq 0$, $u_{\mathfrak{p}}$ is necessarily bijective,
which proves the lemma.

By hypothesis, none of the embedded associated prime cycles of $\mathcal{F}/t\mathcal{F}$ contains $x$, hence none of
the embedded associated prime cycles of $\mathcal{F}$ contains $x$, by virtue of `(3.4.4)`. On the other hand, applying
`(3.4.2)` to an irreducible component of $Supp(\mathcal{F}/t\mathcal{F})$ containing $x$, one sees that
$long(\mathcal{F}_{s_{i}}) = 1$ for every $S_{i}$ containing $x$, which completes the proof that $\mathcal{F}_{x}$ is
reduced; finally, the last assertions are also consequences of `(3.4.2)`.

**Corollary (3.4.7).**

<!-- label: IV.3.4.7 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $M$ an $A$-module of finite type, $(x_{i})_{1
\leq i \leq k}$ a family of elements of $\mathfrak{m}$ forming part of a system of*

<!-- original page 51 -->

*parameters for $M$ `(0, 16.3.6)`. If the $A$-module $N = M/(\sum^{k}_{i=1} x_{i} M)$ is integral `(3.2.4)`, then $M$ is
integral and the sequence $(x_{i})_{1 \leq i \leq k}$ is $M$-regular.*

By induction on $k$, one is immediately reduced to the case $k = 1$; we shall write $x$ instead of $x_{1}$; the
hypothesis that $x$ is part of a system of parameters for $M$ entails that $\dim(N) = \dim(M) - 1$ `(0, 16.3.7)`. Set $n
= \dim(N)$; there is therefore a minimal element $\mathfrak{p}$ of $Supp(M)$ such that $\dim(M/\mathfrak{p} M) = n + 1$
`(0, 16.3.4)`, and for every integer $j > 0$ one also then has $\dim(M/\mathfrak{p}^{j} M) = n + 1$ `(0, 16.3.5)`;
moreover $x$ is part of a system of parameters for $M/\mathfrak{p}^{j} M$ `(0, 16.3.5)`, hence, if one sets $M' =
M/\mathfrak{p}^{j} M$ and $N' = M'/xM'$, one has $\dim(N') = n$. It is clear that one has a surjective homomorphism $v :
N \to N'$; let us show that $v$ is bijective. Indeed, if $P = Ker(v)$, one has $Ass(P) \subset Ass(N)$, and since $N$ is
integral, the hypothesis $P \neq 0$ would entail that $Ass(P)$ and $Ass(N)$ would both be reduced to the unique point
$\mathfrak{q}$ of $Ass(N) = Supp(N)$; but since $\dim(N') = \dim(N)$, one has $N'_{\mathfrak{q}} \neq 0$, and the
hypothesis $long(N_{\mathfrak{q}}) = 1$ entails $long(N'_{\mathfrak{q}}) = 1$ since $N_{\mathfrak{q}} \to
N'_{\mathfrak{q}}$ is surjective. One would therefore have $P_{\mathfrak{q}} = 0$, contrary to the hypothesis, whence
our assertion. But then $N'$, being isomorphic to $N$, is integral; moreover, the support of $N'$ (equal to the
intersection of $Supp(M)$ and $V(x)$) cannot contain $Supp(M')$, and this latter set is irreducible by construction. The
hypothesis that $M'/xM'$ is integral (hence reduced) then entails that $x$ is $M'$-regular by virtue of `(3.4.6)`. One
concludes that the kernel of the homothety $z \mapsto x z$ in $M$ is contained in $\mathfrak{p}^{j} M \subset
\mathfrak{m}^{j} M$ for every integer $j$, and this kernel is therefore reduced to `0` $(0_{I}, 7.3.5)$, which proves
that $x$ is $M$-regular. One can then apply `(3.4.5)`, which proves that $M$ is integral.

**Remark (3.4.8).**

<!-- label: IV.3.4.8 -->

*The proposition analogous to `(3.4.7)`, where one replaces "integral" by "reduced", is no longer necessarily exact.
Consider for example the polynomial ring $C = K[X, Y, Z]$ over a field $K$, the quotient ring $B = C/\mathfrak{pq}$,
where $\mathfrak{p} = CZ$, $\mathfrak{q} = CX^{2} + CY$; let $A$ be the local ring of $B$ corresponding to the image
maximal ideal of $CX + CY + CZ$ in $B$. If $x$, $z$ are the canonical images of $X$, $Z$ in $A$, it is clear that $xz
\neq 0$ but $x^{2} z^{2} = 0$; on the other hand, as $A/xA$ is isomorphic to $K[Y, Z]/(YZ)$, one has $\dim(A/xA) = 1$
while $\dim(A) = 2$, hence $x$ belongs to a system of parameters for $A$ `(0, 16.3.4)`, $A/xA$ is reduced, but $A$ is
not.*

**Proposition (3.4.9).**

<!-- label: IV.3.4.9 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type, $f$ an $M$-regular element of $A$ such that $M/fM$ has
no embedded associated prime ideals. If $\mathfrak{p}_{i}$ $(1 \leq i \leq m)$ are the prime ideals associated to
$M/fM$, then, for every integer $n > 0$, $f^{n} M$ is the intersection of the inverse images of the $f^{n}
M_{\mathfrak{p}_{i}}$ by the canonical maps $M \to M_{\mathfrak{p}_{i}}$ $(1 \leq i \leq m)$.*

Everything reduces to showing that the $\mathfrak{p}_{i}$ are also the prime ideals associated to $M/f^{n} M$, since
then the saturates of $f^{n} M$ for the $\mathfrak{p}_{i}$ are the submodules of the reduced primary decomposition
(necessarily unique) of $f^{n} M$ in $M$. Now, one has

```text
        Ass(f^{n-1} M/f^n M) ⊂ Ass(M/f^n M) ⊂ Ass(M/f^{n-1} M) ∪ Ass(f^{n-1} M/f^n M)
```

by `(3.1.7)`, and since $f$ is $M$-regular, $f^{n-1} M/f^{n} M$ is isomorphic to $M/fM$; it then suffices to reason by
induction on $n$.
