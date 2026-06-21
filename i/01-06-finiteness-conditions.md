# §6. Finiteness Conditions

<!-- label: I.6 -->

## 6.1. Noetherian and locally Noetherian preschemes

<!-- label: I.6.1 -->

**Definition (6.1.1).** A prescheme $X$ is said to be _Noetherian_ (resp. _locally Noetherian_) if it is a finite union
(resp. a union) of affine opens $V_{\lambda}$ such that the ring of each of the schemes induced on the $V_{\lambda}$ is
Noetherian.

It follows at once from (1.5.2) that if $X$ is locally Noetherian, the structure sheaf $\mathcal{O}_{X}$ is a coherent
sheaf of rings, the question being local. Every quasi-coherent sub-$\mathcal{O}_{X}$-Module (resp. every quasi-coherent
quotient $\mathcal{O}_{X}$-Module) of a coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ is then coherent, for the
question is again local, and it suffices to apply (1.5.1), (1.4.1), and (1.3.10), together with the fact that a
submodule (resp. quotient module) of a module of finite type over a Noetherian ring is of finite type. More
particularly, every quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$ is coherent.

If a prescheme $X$ is a finite union (resp. a union) of opens $W_{\lambda}$ such that the preschemes induced on the
$W_{\lambda}$ are Noetherian (resp. locally Noetherian), it is clear that $X$ is Noetherian (resp. locally Noetherian).

**Proposition (6.1.2).** For a prescheme $X$ to be Noetherian, it is necessary and sufficient that it be locally
Noetherian and that its underlying space be quasi-compact; the underlying space of $X$ is then Noetherian.

**Proof.** The first assertion follows at once from the definitions and from (1.1.10 (ii)). The second results from
(1.1.6) and from the fact that every space which is a finite union of Noetherian subspaces is Noetherian (0, 2.2.3).

**Proposition (6.1.3).** Let $X$ be an affine scheme with ring $A$. The following conditions are equivalent: a) $X$ is
Noetherian; b) $X$ is locally Noetherian; c) $A$ is Noetherian.

**Proof.** The equivalence of a) and b) results from (6.1.2) and from the fact that every affine scheme has a
quasi-compact underlying space (1.1.10); it is moreover clear that c) implies a). To see that a) implies c), note that
there is a finite covering $(V_{i})$ of $X$ by affine opens such that the ring $A_{i}$ of the prescheme induced on
$V_{i}$ is Noetherian. Let $(\mathfrak{a}_{n})$ be an increasing sequence of ideals of $A$; there corresponds to it
canonically and bijectively (1.3.7) an increasing sequence $(\tilde{\mathfrak{a}}_{n})$ of sheaves of ideals in
$\tilde{A} = \mathcal{O}_{X}$. To see that the sequence $(\mathfrak{a}_{n})$ is stationary, it suffices to prove that
the sequence $(\tilde{\mathfrak{a}}_{n})$ is. Now the restriction $\tilde{\mathfrak{a}}_{n}|V_{i}$ is a quasi-coherent
sheaf of ideals in $\mathcal{O}_{X}|V_{i}$, being the inverse image of $\tilde{\mathfrak{a}}_{n}$ under the canonical
injection $V_{i} \to X$ (0, 5.1.4); $\tilde{\mathfrak{a}}_{n}|V_{i}$ is therefore of the form
$\tilde{\mathfrak{a}}_{ni}$, where $\mathfrak{a}_{ni}$ is an ideal of $A_{i}$ (1.3.7). Since $A_{i}$ is Noetherian, the
sequence $(\mathfrak{a}_{ni})$ is stationary for every $i$, whence the proposition.

It will be noted that the preceding argument also proves that if $X$ is a Noetherian prescheme, every increasing
sequence of coherent sheaves of ideals of $\mathcal{O}_{X}$ is stationary.

**Proposition (6.1.4).** Every subprescheme of a Noetherian (resp. locally Noetherian) prescheme is Noetherian (resp.
locally Noetherian).

**Proof.** It suffices to give the proof for a Noetherian prescheme $X$; moreover, by definition (6.1.1) one is at once
reduced to the case where $X$ is an affine scheme. Since every subprescheme of $X$ is a closed subprescheme of a
prescheme induced on an open (4.1.3), one may restrict oneself to the case of a subprescheme $Y$ that is either closed
or induced on an open of $X$. The case where $Y$ is closed is immediate, for if $A$ is the ring of $X$, one knows that
$Y$ is an affine scheme with ring $A/\mathfrak{J}$, where $\mathfrak{J}$ is an ideal of $A$ (4.2.3); since $A$ is
Noetherian (6.1.3), so is $A/\mathfrak{J}$. Suppose now $Y$ open in $X$; the underlying space $Y$ is Noetherian (6.1.2),
hence quasi-compact, and consequently a finite union of opens $D(f_{i})$ ($f_{i} \in A$); everything reduces to proving
the proposition when $Y = D(f)$ with $f \in A$. But then $Y$ is an affine scheme whose ring is isomorphic to $A_{f}$
(1.3.6); since $A$ is Noetherian (6.1.3), so is $A_{f}$.

**(6.1.5)** It will be noted that the product of two Noetherian $S$-preschemes is not necessarily Noetherian, even if
these preschemes are affine, for the tensor product of two Noetherian algebras is not necessarily a Noetherian ring (cf.
(6.3.8)).

**Proposition (6.1.6).** If $X$ is a Noetherian prescheme, the Nilradical $\mathcal{N}_{X}$ of $\mathcal{O}_{X}$ is
nilpotent.

**Proof.** One may indeed cover $X$ by a finite number of affine opens $U_{i}$, and it suffices to prove that there
exist integers $n_{i}$ such that $(\mathcal{N}_{X}|U_{i})^{n_{i}} = 0$; if $n$ is the largest of the $n_{i}$, one will
then have $\mathcal{N}_{X}^{n} = 0$. One is thus reduced to the case where $X = \operatorname{Spec}(A)$ is affine, $A$
being a Noetherian ring; by virtue of (5.1.1) and (1.3.13), it suffices to observe that the nilradical of $A$ is
nilpotent ([11], p. 127, cor. 4).

**Corollary (6.1.7).** Let $X$ be a Noetherian prescheme; for $X$ to be an affine scheme, it is necessary and sufficient
that $X_{\mathrm{red}}$ be one.

**Proof.** This results from (6.1.6) and (5.1.10).

**Lemma (6.1.8).** Let $X$ be a topological space, $x$ a point of $X$, and $U$ an open neighborhood of $x$ having only a
finite number of irreducible components. Then there exists a neighborhood $V$ of $x$ such that every open neighborhood
of $x$ contained in $V$ is connected.

**Proof.** Let $U_{i}$ ($1 \leq i \leq m$) be the irreducible components of $U$ not containing $x$; the complement in
$U$ of the union of the $U_{i}$ is an open neighborhood $V$ of $x$ in $U$, hence also in $X$; it is moreover the
complement in $X$ of the union of the irreducible components of $X$ that do not contain $x$ (0, 2.1.6). Let then $W$ be
an open neighborhood of $x$ contained in $V$. The irreducible components of $W$ are the traces on $W$ of the irreducible
components of $U$ that meet $W$ (0, 2.1.6), so these components contain $x$; since they are connected, so is $W$.

**Corollary (6.1.9).** A locally Noetherian topological space is locally connected (which implies among other things
that its connected components are open).

**Proposition (6.1.10).** Let $X$ be a locally Noetherian topological space. The following conditions are equivalent:

a) The irreducible components of $X$ are open.

b) The irreducible components of $X$ are identical with its connected components.

c) The connected components of $X$ are irreducible.

d) Two distinct irreducible components of $X$ do not meet.

Finally, if $X$ is a prescheme, these conditions are also equivalent to:

e) For every $x \in X$, $\operatorname{Spec}(\mathcal{O}_{x})$ is irreducible (in other words, the nilradical of
$\mathcal{O}_{x}$ is prime).

**Proof.** It is immediate that a) implies b), for an irreducible space is connected, and a) implies that the
irreducible components of $X$ are sets that are at once open and closed. It is trivial that b) implies c); conversely, a
closed set $F$ containing a connected component $C$ of $X$ and distinct from $C$ cannot be irreducible, for this set,
not being connected, is the union of two nonempty disjoint sets at once open and closed in $F$, hence closed in $X$;
consequently c) implies b). One concludes at once that c) implies d), two distinct connected components having no common
point. We have not used up to now the fact that $X$ is locally Noetherian. Suppose now this hypothesis realized and let
us show that d) implies a): by virtue of (0, 2.1.6), one may restrict oneself to the case where the space $X$ is
Noetherian, hence has only a finite number of irreducible components. Since these are closed and pairwise disjoint, they
are open.

Finally the equivalence of d) and e) holds without supposing that the underlying space of the prescheme $X$ is locally
Noetherian. One may indeed reduce to the case where $X = \operatorname{Spec}(A)$ is affine by virtue of (0, 2.1.6); to
say that $x$ is contained in only a single irreducible component of $X$ then means that $\mathfrak{j}_{x}$ contains only
a single minimal ideal of $A$ (1.1.14), which amounts to saying that $\mathfrak{j}_{x}\mathcal{O}_{x}$ contains only a
single minimal ideal of $\mathcal{O}_{x}$, whence the conclusion.

**Corollary (6.1.11).** Let $X$ be a locally Noetherian space. For $X$ to be irreducible, it is necessary and sufficient
that $X$ be connected and nonempty, and that two distinct irreducible components of $X$ do not meet. If $X$ is a
prescheme, this last condition is equivalent to $\operatorname{Spec}(\mathcal{O}_{x})$ being irreducible for every $x
\in X$.

**Proof.** The last part has been seen in (6.1.10); there is thus only the sufficiency of the conditions of the first
assertion to prove. But by (6.1.10), these conditions imply that the irreducible components of $X$ are its connected
components, and since $X$ is connected and nonempty, it is irreducible.

**Corollary (6.1.12).** Let $X$ be a locally Noetherian prescheme. For $X$ to be integral, it is necessary and
sufficient that $X$ be connected and that $\mathcal{O}_{x}$ be integral for every $x \in X$.

**Proposition (6.1.13).** Let $X$ be a locally Noetherian prescheme, and let $x \in X$ be a point such that the
nilradical $\mathcal{N}_{x}$ of $\mathcal{O}_{x}$ is prime (resp. that $\mathcal{O}_{x}$ is reduced, resp. integral);
then there exists an open neighborhood $U$ of $x$ that is irreducible (resp. reduced, resp. integral).

**Proof.** It suffices to consider the two cases where $\mathcal{N}_{x}$ is prime and where $\mathcal{N}_{x} = 0$, the
third hypothesis being the conjunction of the first two. If $\mathcal{N}_{x}$ is prime, $x$ belongs to only a single
irreducible component $Y$ of $X$ (6.1.10); the union of the irreducible components of $X$ not containing $x$ is closed
(the set of these components being locally finite), and the complement $U$ of this union is therefore open and contained
in $Y$, hence irreducible (0, 2.1.6). If $\mathcal{N}_{x} = 0$, one also has $\mathcal{N}_{y} = 0$ for every $y$ in a
neighborhood of $x$, for $\mathcal{N}$ is quasi-coherent (5.1.1), hence coherent since $X$ is locally Noetherian, and
the conclusion results from (0, 5.2.2).

## 6.2. Artinian preschemes

<!-- label: I.6.2 -->

**Definition (6.2.1).** A prescheme is said to be _Artinian_ if it is affine and if its ring is Artinian.

**Proposition (6.2.2).** Given a prescheme $X$, the following conditions are equivalent:

a) $X$ is an Artinian scheme;

b) $X$ is Noetherian and its underlying space is discrete;

c) $X$ is Noetherian and the points of its underlying space are closed (condition $T_{1}$).

When this is so, the underlying space of $X$ is finite, and the ring $A$ of $X$ is the direct composite of the
(Artinian) local rings of the points of $X$.

**Proof.** One knows that a) implies the last assertion ([13], p. 205, th. 3); every prime ideal of $A$ is then maximal
and is the inverse image of the maximal ideal of one of the local components of $A$, so the space $X$ is finite and
discrete; a) therefore implies b), and b) evidently implies c). To see that c) implies a), let us first show that $X$ is
then finite; one may indeed reduce to the case where $X$ is affine, and one knows that a Noetherian ring all of whose
prime ideals are maximal is Artinian ([13], p. 203), whence our assertion. The underlying space $X$ is then discrete,
the topological sum of a finite number of points $x_{i}$, and the local rings $\mathcal{O}_{x_{i}} = A_{i}$ are
Artinian; it is clear that $X$ is isomorphic to the affine scheme prime spectrum of the ring $A$ direct composite of the
$A_{i}$ (1.7.3).

## 6.3. Morphisms of finite type

<!-- label: I.6.3 -->

**Definition (6.3.1).** A morphism $f : X \to Y$ is said to be _of finite type_ if $Y$ is a union of a family
$(V_{\alpha})$ of affine opens having the following property:

(P) $f^{-1}(V_{\alpha})$ is a finite union of affine opens $U_{\alpha i}$ such that each of the rings $A(U_{\alpha i})$
is an algebra of finite type over $A(V_{\alpha})$.

One also says then that $X$ is a _prescheme of finite type over $Y$_, or a _$Y$-prescheme of finite type_.

**Proposition (6.3.2).** If $f : X \to Y$ is a morphism of finite type, every affine open $W$ of $Y$ possesses property
(P) of (6.3.1).

**Proof.** We shall first prove the

**Lemma (6.3.2.1).** If $T \subset Y$ is an affine open possessing property (P), then, for every $g \in A(T)$, $D(g)$
possesses property (P).

Indeed, by hypothesis, $f^{-1}(T)$ is a finite union of affine opens $Z_{j}$ such that $A(Z_{j})$ is an algebra of
finite type over $A(T)$; let $\varphi_{j} : A(T) \to A(Z_{j})$ be the ring homomorphism corresponding to the restriction
of $f$ to $Z_{j}$ (2.2.4), and set $g_{j} = \varphi_{j}(g)$; one then has $f^{-1}(D(g)) \cap Z_{j} = D(g_{j})$
(1.2.2.2). Now $A(D(g_{j})) = A(Z_{j})_{\varphi_{j}(g)} = A(Z_{j})[1/g_{j}]$ is of finite type over $A(Z_{j})$ and a
fortiori over $A(T)$ by virtue of the hypothesis, hence also over $A(D(g)) = A(T)[1/g]$, which proves the lemma.

This lemma being established, since $W$ is quasi-compact (1.1.10), there exists a finite covering of $W$ by sets of the
form $D(g_{i})$, where each $g_{i}$ belongs to a ring $A(V_{\alpha(i)})$. Each $D(g_{i})$, being quasi-compact, is a
finite union of sets $D(h_{ik})$ where $h_{ik} \in A(W)$; if $\varphi_{i} : A(W) \to A(D(g_{i}))$ is the canonical map,
one has $D(h_{ik}) = D(\varphi_{i}(h_{ik}))$ by virtue of (1.2.2.2). By virtue of (6.3.2.1), each of the
$f^{-1}(D(h_{ik}))$ admits a finite covering by affine opens $U_{ijk}$ such that $A(U_{ijk})$ is an algebra of finite
type over $A(D(h_{ik})) = A(W)[1/h_{ik}]$, whence the proposition.

One may therefore say that the notion of prescheme of finite type over $Y$ is local on $Y$.

**Proposition (6.3.3).** Let $X$, $Y$ be two affine schemes; for $X$ to be of finite type over $Y$, it is necessary and
sufficient that $A(X)$ be an algebra of finite type over $A(Y)$.

**Proof.** The condition being evidently sufficient, let us prove that it is necessary. Set $A = A(Y)$, $B = A(X)$; by
virtue of (6.3.2), there exists a finite affine open covering $(V_{i})$ of $X$ such that each of the rings $A(V_{i})$ is
an $A$-algebra of finite type. Moreover, the $V_{i}$ being quasi-compact, one may cover each of them by a finite number
of opens of the form $D(g_{ij}) \subset V_{i}$, where $g_{ij} \in B$; if $\varphi_{i}$ is the homomorphism $B \to
A(V_{i})$ corresponding to the canonical injection $V_{i} \to X$, one has $B_{g_{ij}} = (A(V_{i}))_{\varphi_{i}(g_{ij})}
= A(V_{i})[1/\varphi_{i}(g_{ij})]$, so $B_{g_{ij}}$ is an $A$-algebra of finite type. One may therefore reduce to the
case where $V_{i} = D(g_{i})$ with $g_{i} \in B$. By hypothesis, there exist a finite subset $F_{i}$ of $B$ and an
integer $n_{i} \geq 0$ such that $B_{g_{i}}$ is the algebra generated over $A$ by the elements $b_{i}/g_{i}^{n_{i}}$,
where $b_{i}$ runs through $F_{i}$. Since the $g_{i}$ are finite in number, one may moreover suppose all the $n_{i}$
equal to a single integer $n$. Moreover, since the $D(g_{i})$ form a covering of $X$, the ideal generated in $B$ by the
$g_{i}$ is equal to $B$; in other words, there exist $h_{i} \in B$ such that $\sum_{i} h_{i} g_{i} = 1$. Let then $F$ be
the finite subset of $B$, the union of the $F_{i}$, of the set of the $g_{i}$, and of the set of the $h_{i}$; let us
show that the subring $B' = A[F]$ of $B$ is equal to $B$. By hypothesis, for every $b \in B$ and every $i$, the
canonical image of $b$ in $B_{g_{i}}$ is of the form $b'_{i}/g_{i}^{m_{i}}$, where $b'_{i} \in B'$; on multiplying the
$b'_{i}$ by suitable powers of the $g_{i}$, one may further suppose all the $m_{i}$ equal to a single integer $m$. By
definition of the rings of fractions, there is therefore an integer $N$ (depending on $b$) such that $N \geq m$ and
$g_{i}^{N} b \in B'$ for every $i$; now, in the ring $B'$, the $g_{i}^{N}$ generate the ideal $B'$, since this is so of
the $g_{i}$ (the $h_{i}$ belonging to $B'$); there are therefore $c_{i} \in B'$ such that $\sum_{i} c_{i} g_{i}^{N} =
1$, whence $b = \sum_{i} c_{i} g_{i}^{N} b \in B'$, Q.E.D.

**Proposition (6.3.4).** (i) Every closed immersion is of finite type.

(ii) The composite of two morphisms of finite type is of finite type.

(iii) If $f : X \to X'$, $g : Y \to Y'$ are two $S$-morphisms of finite type, $f \times_{S} g$ is of finite type.

(iv) If $f : X \to Y$ is an $S$-morphism of finite type, $f_{(S')}$ is of finite type for every extension $g : S' \to S$
of the base prescheme.

(v) If the composite $g \circ f$ of two morphisms is of finite type, and if $g$ is separated, $f$ is of finite type.

(vi) If a morphism $f$ is of finite type, so is $f_{\mathrm{red}}$.

**Proof.** By virtue of (5.5.12), it suffices to prove (i), (ii), and (iv).

To establish (i), one may restrict oneself to the case of a canonical injection $X \to Y$, $X$ being a closed
subprescheme of $Y$; moreover (6.3.2), one may suppose $Y$ affine, in which case $X$ is also affine (4.2.3) and its ring
is isomorphic to a quotient ring $A/\mathfrak{J}$, where $A$ is the ring of $Y$ and $\mathfrak{J}$ an ideal of $A$;
since $A/\mathfrak{J}$ is of finite type over $A$, the conclusion follows.

Let us now prove (ii). Let $f : X \to Y$, $g : Y \to Z$ be two morphisms of finite type, and let $U$ be an affine open
of $Z$; $g^{-1}(U)$ admits a finite covering by affine opens $V_{i}$ such that $A(V_{i})$ is an algebra of finite type
over $A(U)$ (6.3.2); likewise, each of the $f^{-1}(V_{i})$ admits a finite covering by affine opens $W_{ij}$ such that
$A(W_{ij})$ is an algebra of finite type over $A(V_{i})$, and consequently also an algebra of finite type over $A(U)$;
whence the conclusion.

Finally, to prove (iv), one may restrict oneself to the case where $S = Y$; indeed, $f_{(S')}$ is also equal to
$f_{(Y_{(S')})}$, $f$ being regarded as a $Y$-morphism, and the base extension being $Y_{(S')} \to Y$ (3.3.9). Let then
$p$, $q$ be the projections $X_{(S')} \to X$ and $X_{(S')} \to S'$. Let $V$ be an affine open in $S$; $f^{-1}(V)$ is a
finite union of affine opens $W_{i}$ each of which is such that $A(W_{i})$ is an algebra of finite type over $A(V)$
(6.3.2). Let $V'$ be an affine open of $S'$ contained in $g^{-1}(V)$; since $f \circ p = g \circ q$, $q^{-1}(V')$ is
contained in the union of the $p^{-1}(W_{i})$; on the other hand, the intersection $p^{-1}(W_{i}) \cap q^{-1}(V')$ is
identified with the product $W_{i} \times_{V} V'$ (3.2.7), which is an affine scheme with ring isomorphic to $A(W_{i})
\otimes_{A(V)} A(V')$ (3.2.2); the latter being by hypothesis an algebra of finite type over $A(V')$, the proposition is
proved.

**Corollary (6.3.5).** Let $f : X \to Y$ be an immersion morphism. If the underlying space of $Y$ (resp. $X$) is locally
Noetherian (resp. Noetherian), $f$ is of finite type.

**Proof.** One may always suppose $Y$ affine (6.3.2); if the underlying space of $Y$ is locally Noetherian, one may
moreover suppose it Noetherian, and then the underlying space of $X$, which is a subspace of it, is Noetherian. In other
words, one may suppose $Y$ affine and the underlying space of $X$ Noetherian; there then exists a covering of $X$ by a
finite number of affine opens $D(g_{i}) \subset Y$, where $g_{i} \in A(Y)$, such that $X \cap D(g_{i})$ is closed in
$D(g_{i})$ (hence an affine scheme (4.2.3)), since $X$ is locally closed in $Y$ (4.1.3). Then $A(X \cap D(g_{i}))$ is an
algebra of finite type over $A(D(g_{i}))$, by (6.3.4, (i)) and (6.3.3), and $A(D(g_{i})) = A(Y)_{g_{i}} = A(Y)[1/g_{i}]$
is of finite type over $A(Y)$, which completes the proof.

**Corollary (6.3.6).** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms. If $g \circ f$ is of finite type, and if $X$
is Noetherian, or $X \times_{Z} Y$ locally Noetherian, $f$ is of finite type.

**Proof.** This results at once from the proof of (5.5.12) and from (6.3.5) applied to the immersion morphism
$\Gamma_{f}$.

**Proposition (6.3.7).** Let $f : X \to Y$ be a morphism of finite type; if $Y$ is Noetherian (resp. locally
Noetherian), $X$ is Noetherian (resp. locally Noetherian).

**Proof.** One may restrict oneself to giving the proof when $Y$ is Noetherian. Then $Y$ is a finite union of affine
opens $V_{i}$ such that the $A(V_{i})$ are Noetherian rings. By virtue of (6.3.2), each of the $f^{-1}(V_{i})$ is a
union of a finite number of affine opens $W_{ij}$ such that the $A(W_{ij})$ are algebras of finite type over $A(V_{i})$,
hence Noetherian rings; this proves that $X$ is Noetherian.

**Corollary (6.3.8).** Let $X$ be a prescheme of finite type over $S$. For every extension of the base $S' \to S$ such
that $S'$ is Noetherian (resp. locally Noetherian), $X_{(S')}$ is Noetherian (resp. locally Noetherian).

**Proof.** This results from (6.3.7), $X_{(S')}$ being of finite type over $S'$ by virtue of (6.3.4, (iv)).

One may further say that in a product $X \times_{S} Y$ of $S$-preschemes, if one of the factors $X$, $Y$ is of finite
type over $S$ and the other Noetherian (resp. locally Noetherian), then $X \times_{S} Y$ is Noetherian (resp. locally
Noetherian).

**Corollary (6.3.9).** Let $X$ be a prescheme of finite type over a locally Noetherian prescheme $S$. Then every
$S$-morphism $f : X \to Y$ is of finite type.

**Proof.** Indeed, one may suppose $S$ Noetherian; if $\varphi : X \to S$, $\psi : Y \to S$ are the structure morphisms,
one has $\varphi = \psi \circ f$, and $X$ is Noetherian by virtue of (6.3.7); $f$ is therefore of finite type by virtue
of (6.3.6).

**Proposition (6.3.10).** Let $f : X \to Y$ be a morphism of finite type. For $f$ to be surjective, it is necessary and
sufficient that, for every algebraically closed field $\Omega$, the map $X(\Omega) \to Y(\Omega)$ corresponding to $f$
(3.4.1) be surjective.

**Proof.** The condition is sufficient, as one sees by considering, for every $y \in Y$, an algebraically closed
extension $\Omega$ of $\kappa(y)$, and the commutative diagram

$$ \begin{array}{ccc} & & X \\ & \nearrow & \downarrow f \\ \operatorname{Spec}(\Omega) & \to & Y \end{array} $$

(cf. (3.5.3)). Conversely, suppose $f$ surjective, and let $g : \{\xi\} = \operatorname{Spec}(\Omega) \to Y$ be a
morphism, $\Omega$ being an algebraically closed field. If one considers the diagram

$$ \begin{array}{ccc} X & \leftarrow & X_{(\Omega)} \\ f \downarrow & & \downarrow f_{(\Omega)} \\ Y & \leftarrow &
\operatorname{Spec}(\Omega) \end{array} $$

it then suffices to show that there exists in $X_{(\Omega)}$ a point rational over $\Omega$ (3.3.14, 3.4.3, and 3.4.4).
Since $f$ is surjective, $X_{(\Omega)}$ is not empty (3.5.10), and since $f$ is of finite type, so is $f_{(\Omega)}$
(6.3.4, (iv)); hence $X_{(\Omega)}$ contains a nonempty affine open $Z$ such that $A(Z)$ is a nonzero algebra of finite
type over $\Omega$. By virtue of Hilbert's Nullstellensatz [21], there exists an $\Omega$-homomorphism $A(Z) \to
\Omega$, hence a section of $X_{(\Omega)}$ over $\operatorname{Spec}(\Omega)$, which proves the proposition.

## 6.4. Algebraic preschemes

<!-- label: I.6.4 -->

**Definition (6.4.1).** Given a field $K$, one calls _algebraic $K$-prescheme_ a prescheme $X$ of finite type over $K$;
$K$ is called the _base field_ of $X$. If in addition $X$ is a scheme (or, what amounts to the same (5.5.8), if $X$ is a
$K$-scheme), one also says that $X$ is an _algebraic $K$-scheme_.

Every algebraic $K$-prescheme is Noetherian (6.3.7).

**Proposition (6.4.2).** Let $X$ be an algebraic $K$-prescheme. For a point $x \in X$ to be closed, it is necessary and
sufficient that $\kappa(x)$ be an algebraic extension of $K$, of finite degree.

**Proof.** One may suppose $X$ affine, the ring $A$ of $X$ being a $K$-algebra of finite type. Indeed, the affine opens
$U$ of $X$ such that $A(U)$ is a $K$-algebra of finite type form a covering of $X$ (6.3.1). The closed points of $X$ are
then the points such that $\mathfrak{j}_{x}$ is a maximal ideal of $A$, in other words such that $A/\mathfrak{j}_{x}$ is
a field (necessarily equal to $\kappa(x)$). Since $A/\mathfrak{j}_{x}$ is a $K$-algebra of finite type, one sees that if
$x$ is closed, $\kappa(x)$ is a field which is an algebra of finite type over $K$, hence necessarily a $K$-algebra of
finite rank [21]. Conversely, if $\kappa(x)$ is of finite rank over $K$, so is $A/\mathfrak{j}_{x} \subset \kappa(x)$,
and since every integral ring which is a $K$-algebra of finite rank is a field, one has $A/\mathfrak{j}_{x} =
\kappa(x)$, so $x$ is closed.

**Corollary (6.4.3).** Let $K$ be an algebraically closed field, $X$ an algebraic $K$-prescheme; the closed points of
$X$ are then the points rational over $K$ (3.4.4) and are canonically identified with the points of $X$ with values in
$K$.

**Proposition (6.4.4).** Let $X$ be an algebraic prescheme over a field $K$. The following properties are equivalent:

a) $X$ is Artinian.

b) The underlying space of $X$ is discrete.

c) The underlying space of $X$ has only a finite number of closed points.

c') The underlying space of $X$ is finite.

d) The points of $X$ are closed.

e) $X$ is isomorphic to $\operatorname{Spec}(A)$, where $A$ is a $K$-algebra of finite rank.

**Proof.** Since $X$ is Noetherian, it results from (6.2.2) that the conditions a), b), d) are equivalent and imply c)
and c'); moreover, it is clear that e) implies a). It remains to see that c) implies d) and e); one may restrict oneself
to the case where $X$ is affine. Then $A(X)$ is a $K$-algebra of finite type (6.3.3), hence a Jacobson ring ([1], p.
3-11 and 3-12), in which there is by hypothesis only a finite number of maximal ideals. Since a finite intersection of
prime ideals can be a prime ideal only if it is equal to one of them, every prime ideal of $A(X)$ is therefore maximal,
whence d). Moreover, one knows then (6.2.2) that $A(X)$ is an Artinian $K$-algebra of finite type, hence necessarily of
finite rank [21].

**(6.4.5)** When the conditions of (6.4.4) are satisfied, one says that $X$ is a _finite scheme over $K$_ (cf. (II,
6.1.1)), or a _finite $K$-scheme_, of _rank_ $[A : K]$, which one also writes $rg_{K}(X)$; if $X$, $Y$ are two finite
schemes over $K$, one has

$$ rg_{K}(X \amalg Y) = rg_{K}(X) + rg_{K}(Y) \tag{6.4.5.1} $$

$$ rg_{K}(X \times_{K} Y) = rg_{K}(X) rg_{K}(Y) \tag{6.4.5.2} $$

as results from (3.2.2).

**Corollary (6.4.6).** Let $X$ be a finite scheme over a field $K$. For every extension $K'$ of $K$, $X \otimes_{K} K'$
is a finite scheme over $K'$, and its rank over $K'$ is equal to the rank of $X$ over $K$.

**Proof.** Indeed, if $A = A(X)$, one has $[A \otimes_{K} K' : K'] = [A : K]$.

**Corollary (6.4.7).** Let $X$ be a finite scheme over a field $K$; one sets $n = \sum_{x \in X} [\kappa(x) : K]_{s}$
(one recalls that if $K'$ is an extension of $K$, $[K' : K]_{s}$ is the _separable rank_ of $K'$ over $K$, the rank of
the largest separable algebraic extension of $K$ contained in $K'$); then, for every algebraically closed extension
$\Omega$ of $K$, the underlying space of $X \otimes_{K} \Omega$ has exactly $n$ points, which are identified with the
points of $X$ with values in $\Omega$.

**Proof.** One may evidently restrict oneself to the case where the ring $A = A(X)$ is local (6.2.2); let $\mathfrak{m}$
be its maximal ideal, $L = A/\mathfrak{m}$ its residue field, an algebraic extension of $K$. The points of $X$ with
values in $\Omega$ then correspond bijectively to the $\Omega$-sections of $X \otimes_{K} \Omega$ (3.4.1 and 3.3.14),
and also to the $K$-homomorphisms of $L$ into $\Omega$ (1.7.3), whence the proposition (Bourbaki, Alg., chap. V, § 7, n°
5, prop. 8), taking (6.4.3) into account.

**(6.4.8)** The number $n$ defined in (6.4.7) is called the _separable rank_ of $A$ (or of $X$) over $K$, or also the
_geometric number of points_ of $X$; it is therefore equal to the number of elements of $X(\Omega)_{K}$. It results at
once from this definition that, for every extension $K'$ of $K$, $X \otimes_{K} K'$ has the same geometric number of
points as $X$. If one denotes this number by $n(X)$, it is clear that if $X$, $Y$ are two finite schemes over $K$, one
has

$$ n(X \amalg Y) = n(X) + n(Y). \tag{6.4.8.1} $$

Under the same hypotheses, one also has

$$ n(X \times_{K} Y) = n(X) n(Y) \tag{6.4.8.2} $$

as results at once from the interpretation of $n(X)$ as the number of elements of $X(\Omega)_{K}$ and from the formula
(3.4.3.1).

**Proposition (6.4.9).** Let $K$ be a field, $X$, $Y$ two algebraic $K$-preschemes, $f : X \to Y$ a $K$-morphism,
$\Omega$ an algebraically closed extension of $K$, of infinite transcendence degree over $K$. For $f$ to be surjective,
it is necessary and sufficient that the map $X(\Omega)_{K} \to Y(\Omega)_{K}$ corresponding to $f$ (3.4.1) be
surjective.

**Proof.** The necessity results from (6.3.10), on remarking that $f$ is necessarily of finite type (6.3.9). To see that
the condition is sufficient, one reasons as in (6.3.10), on remarking that for every $y \in Y$, $\kappa(y)$ is an
extension of $K$ of finite type, and consequently is $K$-isomorphic to a subfield of $\Omega$.

**Remark (6.4.10).** We shall see in chap. IV that the conclusion of (6.4.9) is still valid without any hypothesis
relative to the transcendence degree of $\Omega$ over $K$.

**Proposition (6.4.11).** If $f : X \to Y$ is a morphism of finite type, then for every $y \in Y$, the fiber $f^{-1}(y)$
is an algebraic prescheme over the residue field $\kappa(y)$, and for every $x \in f^{-1}(y)$, $\kappa(x)$ is an
extension of finite type of $\kappa(y)$.

**Proof.** Since $f^{-1}(y) = X \otimes_{Y} \kappa(y)$ (3.6.3), the proposition results from (6.3.4, (iv)) and from
(6.3.3).

**Proposition (6.4.12).** Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms; set $X' = X \times_{Y} Y'$ and let $f' =
f_{(Y')} : X' \to Y'$. Let $y' \in Y'$, $y = g(y')$; if the fiber $f^{-1}(y)$ is a finite algebraic scheme over
$\kappa(y)$, then the fiber $f'^{-1}(y')$ is a finite algebraic scheme over $\kappa(y')$, having the same rank and the
same geometric number of points as $f^{-1}(y)$.

**Proof.** Taking into account the transitivity of fibers (3.6.5), this results at once from (6.4.6) and (6.4.8).

**(6.4.13)** Proposition (6.4.11) shows that morphisms of finite type correspond intuitively to "algebraic families of
algebraic varieties," the points of $Y$ playing the role of "parameters," which gives these morphisms a "geometric"
meaning. The morphisms that are not of finite type will intervene above all in what follows in questions of "change of
the base prescheme," for example by localization or completion.

## 6.5. Local determination of a morphism

<!-- label: I.6.5 -->

**Proposition (6.5.1).** Let $X$, $Y$ be two $S$-preschemes, $Y$ being of finite type over $S$; let $x \in X$, $y \in Y$
be above one and the same point $s \in S$.

(i) If two $S$-morphisms $f = (\psi, \theta)$, $f' = (\psi', \theta')$ of $X$ into $Y$ are such that $\psi(x) = \psi'(x)
= y$, and that the (local) $\mathcal{O}_{s}$-homomorphisms $\theta_{x}^{\sharp}$ and $\theta_{x}'^{\sharp}$ of
$\mathcal{O}_{y}$ into $\mathcal{O}_{x}$ are identical, then $f$ and $f'$ coincide in an open neighborhood of $x$.

(ii) Suppose in addition $S$ locally Noetherian. For every local $\mathcal{O}_{s}$-homomorphism $\varphi :
\mathcal{O}_{y} \to \mathcal{O}_{x}$, there exist an open neighborhood $U$ of $x$ in $X$ and an $S$-morphism $f = (\psi,
\theta)$ of $U$ into $Y$ such that $\psi(x) = y$ and $\theta_{x}^{\sharp} = \varphi$.

**Proof.** (i) The question being local on $S$, $X$, and $Y$, one may suppose $S$, $X$, $Y$ affine with respective rings
$A$, $B$, $C$, $f$ and $f'$ being of the form $({}^{a}\varphi, \tilde{\varphi})$ and $({}^{a}\varphi',
\tilde{\varphi}')$ respectively, where $\varphi$ and $\varphi'$ are two $A$-homomorphisms of $C$ into $B$ such that
$\varphi^{-1}(\mathfrak{j}_{x}) = \varphi'^{-1}(\mathfrak{j}_{x}) = \mathfrak{j}_{y}$, and the homomorphisms
$\varphi_{x}$ and $\varphi'_{x}$ of $C_{y}$ into $B_{x}$, deduced from $\varphi$ and $\varphi'$, are identical; one may
further suppose that $C$ is an $A$-algebra of finite type. Let $c_{i}$ ($1 \leq i \leq n$) be generators of the
$A$-algebra $C$, and set $b_{i} = \varphi(c_{i})$, $b'_{i} = \varphi'(c_{i})$; by hypothesis, one has $b_{i}/1 =
b'_{i}/1$ in the ring of fractions $B_{x}$ ($1 \leq i \leq n$). This means that there exist elements $s_{i} \in B -
\mathfrak{j}_{x}$ such that $s_{i}(b_{i} - b'_{i}) = 0$ for $1 \leq i \leq n$, and one may evidently suppose all the
$s_{i}$ equal to a single element $g \in B - \mathfrak{j}_{x}$. One concludes that one has $b_{i}/1 = b'_{i}/1$ for $1
\leq i \leq n$ in the ring of fractions $B_{g}$; if $i_{g}$ is the canonical homomorphism $B \to B_{g}$, one has
consequently $i_{g} \circ \varphi = i_{g} \circ \varphi'$; so the restrictions of $f$ and $f'$ to $D(g)$ are identical.

(ii) One may reduce to the same situation as in (i), and suppose in addition that the ring $A$ is Noetherian. Let
$c_{i}$ ($1 \leq i \leq n$) be generators of the $A$-algebra $C$, and let $\alpha : A[X_{1}, \ldots, X_{n}] \to C$ be
the homomorphism of the polynomial algebra $A[X_{1}, \ldots, X_{n}]$ onto $C$ transforming $X_{i}$ into $c_{i}$ for $1
\leq i \leq n$. Let on the other hand $i_{y}$ be the canonical homomorphism $C \to C_{y}$, and consider the composite
homomorphism

$$ \beta : A[X_{1}, \ldots, X_{n}] \xrightarrow{\alpha} C \xrightarrow{i_{y}} C_{y} \xrightarrow{\varphi} B_{x}. $$

Denote by $\mathfrak{a}$ the kernel of $\beta$; since $A$ is Noetherian, so is $A[X_{1}, \ldots, X_{n}]$, and
consequently $\mathfrak{a}$ admits a finite system of generators $Q_{j}(X_{1}, \ldots, X_{n})$ ($1 \leq j \leq m$). On
the other hand, each of the elements $\varphi(i_{y}(c_{i}))$ may be written $b_{i}/s_{i}$, where $b_{i} \in B$ and
$s_{i} \notin \mathfrak{j}_{x}$; one may in addition suppose all the $s_{i}$ equal to a single element $g \in B -
\mathfrak{j}_{x}$. This being so, one has by hypothesis $Q_{j}(b_{1}/g, \ldots, b_{n}/g) = 0$ in $B_{x}$; set

$$ Q_{j}(X_{1}/T, \ldots, X_{n}/T) = P_{j}(X_{1}, \ldots, X_{n}, T)/T^{k_{j}} $$

where $P_{j}$ is homogeneous of degree $k_{j}$. Let then $d_{j} = P_{j}(b_{1}, \ldots, b_{n}, g) \in B$. By hypothesis,
one has $t_{j} d_{j} = 0$ for a $t_{j} \in B - \mathfrak{j}_{x}$ ($1 \leq j \leq m$), and one may evidently suppose all
the $t_{j}$ equal to a single element $h \in B - \mathfrak{j}_{x}$; one concludes that $P_{j}(h b_{1}, \ldots, h b_{n},
h g) = 0$ for $1 \leq j \leq m$. This being so, consider the homomorphism $\rho$ of $A[X_{1}, \ldots, X_{n}]$ into the
ring of fractions $B_{hg}$ which sends $X_{i}$ to $h b_{i}/h g$ ($1 \leq i \leq n$); the image of $\mathfrak{a}$ under
this homomorphism is $0$, and a fortiori so is the image under $\rho$ of the kernel $\alpha^{-1}(0)$. So $\rho$ factors
as $A[X_{1}, \ldots, X_{n}] \xrightarrow{\alpha} C \xrightarrow{\gamma} B_{hg}$, with $\gamma(c_{i}) = h b_{i}/h g$, and
it is clear that if $i_{x}$ is the canonical homomorphism $B_{hg} \to B_{x}$, the diagram

$$ \begin{array}{ccc} C & \xrightarrow{\gamma} & B_{hg} \\ i_{y} \downarrow & & \downarrow i_{x} \\ C_{y} &
\xrightarrow{\varphi} & B_{x} \end{array} \tag{6.5.1.1} $$

is commutative; one has therefore $\varphi = \gamma_{x}$, and since $\varphi$ is a local homomorphism, ${}^{a}\gamma(x)
= y$. $f = ({}^{a}\gamma, \tilde{\gamma})$ is thus an $S$-morphism of the neighborhood $D(hg)$ of $x$ into $Y$ which
answers the question.

**Corollary (6.5.2).** Under the hypotheses of (6.5.1, (ii)), if in addition $X$ is of finite type over $S$, one may
suppose the morphism $f$ of finite type.

**Proof.** This results from (6.3.6).

**Corollary (6.5.3).** Suppose the hypotheses of (6.5.1, (ii)) verified, and suppose in addition that $Y$ is integral,
and $\varphi$ an injective homomorphism. Then one may suppose that $f = ({}^{a}\gamma, \tilde{\gamma})$ where $\gamma$
is injective.

**Proof.** Indeed, one may suppose $C$ integral (5.1.4), hence $i_{y}$ injective; it then results from the diagram
(6.5.1.1) that $\gamma$ is injective.

**Proposition (6.5.4).** Let $f = (\psi, \theta) : X \to Y$ be a morphism of finite type, $x$ a point of $X$, $y =
\psi(x)$.

(i) For $f$ to be a local immersion at the point $x$ (4.5.1), it is necessary and sufficient that $\theta_{x}^{\sharp} :
\mathcal{O}_{y} \to \mathcal{O}_{x}$ be surjective.

(ii) Suppose in addition $Y$ locally Noetherian. For $f$ to be a local isomorphism at the point $x$ (4.5.2), it is
necessary and sufficient that $\theta_{x}^{\sharp}$ be an isomorphism.

**Proof.** (ii) By virtue of (6.5.1), there then exist an open neighborhood $V$ of $y$ and a morphism $g : V \to X$ such
that $g \circ f$ (resp. $f \circ g$) is defined and coincides with the identity in a neighborhood of $x$ (resp. $y$),
whence one easily deduces that $f$ is a local isomorphism.

(i) The question being local on $X$ and $Y$, one may suppose $X$ and $Y$ affine, with respective rings $A$, $B$; one has
$f = ({}^{a}\varphi, \tilde{\varphi})$, where $\varphi$ is a ring homomorphism $B \to A$ that makes $A$ a $B$-algebra of
finite type; one has $\psi(\mathfrak{j}_{x}) = \mathfrak{j}_{y}$ and the homomorphism $\varphi_{x} : B_{y} \to A_{x}$,
deduced from $\varphi$, is surjective. Let $(t_{i})$ ($1 \leq i \leq n$) be a system of generators of the $B$-algebra
$A$; the hypothesis on $\varphi_{x}$ implies that there exist $b_{i} \in B$ and a $c \notin \mathfrak{j}_{y}$ such that,
in the ring of fractions $A_{x}$, one has $t_{i}/1 = \varphi(b_{i})/\varphi(c)$ for $1 \leq i \leq n$. Consequently
(1.3.3), there exists $a \in A - \mathfrak{j}_{x}$ such that, if one sets $g = a\varphi(c)$, one also has $t_{i}/1 =
a\varphi(b_{i})/g$ in the ring of fractions $A_{g}$. This being so, there exists by hypothesis a polynomial $Q(X_{1},
\ldots, X_{n})$ with coefficients in the ring $\varphi(B)$, such that $a = Q(t_{1}, \ldots, t_{n})$; set $Q(X_{1}/T,
\ldots, X_{n}/T) = P(X_{1}, \ldots, X_{n}, T)/T^{m}$ where $P$ is homogeneous of degree $m$. In the ring $A_{g}$, one
has

$$ a/1 = a^{m} P(\varphi(b_{1}), \ldots, \varphi(b_{n}), \varphi(c))/g^{m} = a^{m} \varphi(d)/g^{m} $$

where $d \in B$. Since, in $A_{g}$, $g/1 = (a/1)(\varphi(c)/1)$ is invertible by definition, so are $a/1$ and
$\varphi(c)/1$, and one may therefore write $a/1 = (\varphi(d)/1)(\varphi(c)/1)^{-m}$. One concludes that $\varphi(d)/1$
is also invertible in $A_{g}$. Set then $h = cd$; since $\varphi(h)/1$ is invertible in $A_{g}$, the composite
homomorphism $B \to A \to A_{g}$ factors as $B \to B_{h} \to A_{g}$ (0, 1.2.4). Let us show that $\gamma$ is surjective;
it suffices to verify that the image of $B_{h}$ in $A_{g}$ contains the $t_{i}/1$ and $(g/1)^{-1}$. Now, one has
$(g/1)^{-1} = (\varphi(c)/1)^{m-1}(\varphi(d)/1)^{-1} = \gamma(c^{m}/h)$, and $a/1 = \gamma(d^{m+1}/h^{m})$, hence
$\varphi(b_{i})/1 = \gamma(b_{i} d^{m+1}/h^{m})$, and since $t_{i}/1 = (a\varphi(b_{i})/1)(g/1)^{-1}$, our assertion is
proved. The choice of $h$ implies that $\psi(D(g)) \subset D(h)$, and the restriction of $f$ to $D(g)$ is equal to
$({}^{a}\gamma, \tilde{\gamma})$; since $\gamma$ is surjective, this restriction is a closed immersion of $D(g)$ into
$D(h)$ (4.2.3).

**Corollary (6.5.5).** Let $f = (\psi, \theta) : X \to Y$ be a morphism of finite type. Suppose $X$ irreducible, denote
by $x$ its generic point, and set $y = \psi(x)$.

(i) For $f$ to be a local immersion at a point of $X$, it is necessary and sufficient that $\theta_{x}^{\sharp} :
\mathcal{O}_{y} \to \mathcal{O}_{x}$ be surjective.

(ii) Suppose in addition $Y$ irreducible and locally Noetherian. For $f$ to be a local isomorphism at a point of $X$, it
is necessary and sufficient that $y$ be the generic point of $Y$ (or, what amounts to the same (0, 2.1.4), that $f$ be a
dominant morphism) and that $\theta_{x}^{\sharp}$ be an isomorphism (in other words, that $f$ be birational (2.2.9)).

**Proof.** It is clear that (i) results from (6.5.4, (i)), taking into account that every nonempty open of $X$ contains
$x$; likewise (ii) results from (6.5.4, (ii)).

## 6.6. Quasi-compact morphisms and morphisms locally of finite type

<!-- label: I.6.6 -->

**Definition (6.6.1).** A morphism $f : X \to Y$ is said to be _quasi-compact_ if the inverse image under $f$ of every
quasi-compact open of $Y$ is quasi-compact.

Let $\mathfrak{B}$ be a base for the topology of $Y$ formed of quasi-compact opens (for example of affine opens); for
$f$ to be quasi-compact, it is necessary and sufficient that the inverse image under $f$ of every set of $\mathfrak{B}$
be quasi-compact (or, what amounts to the same, a finite union of affine opens), for every quasi-compact open of $Y$ is
a finite union of sets of $\mathfrak{B}$. For example, if $X$ is quasi-compact and $Y$ affine, then every morphism $f :
X \to Y$ is quasi-compact: indeed, $X$ is a finite union of affine open sets $U_{i}$, and for every affine open $V$ of
$Y$, $U_{i} \cap f^{-1}(V)$ is affine (5.5.10), hence quasi-compact.

If $f : X \to Y$ is a quasi-compact morphism, it is clear that for every open $V$ of $Y$, the restriction of $f$ to
$f^{-1}(V)$ is a quasi-compact morphism $f^{-1}(V) \to V$. Conversely, if $(U_{\alpha})$ is an open covering of $Y$ and $f
: X \to Y$ a morphism such that the restrictions $f^{-1}(U_{\alpha}) \to U_{\alpha}$ are quasi-compact, then $f$ is
quasi-compact.

**Definition (6.6.2).** A morphism $f : X \to Y$ is said to be _locally of finite type_ if, for every $x \in X$, there
exist an open neighborhood $U$ of $x$ and an open neighborhood $V \supset f(U)$ of $y$ such that the restriction of $f$
to $U$ is a morphism of finite type of $U$ into $V$. One also says then that $X$ is a _prescheme locally of finite type
over $Y$_, or a _$Y$-prescheme locally of finite type_.

It follows at once from (6.3.2) that if $f$ is locally of finite type, then, for every open $W$ of $Y$, the restriction
of $f$ to $f^{-1}(W)$ is a morphism $f^{-1}(W) \to W$ which is locally of finite type.

If $Y$ is locally Noetherian and if $X$ is locally of finite type over $Y$, $X$ is locally Noetherian by virtue of
(6.3.7).

**Proposition (6.6.3).** For a morphism $f : X \to Y$ to be of finite type, it is necessary and sufficient that it be
quasi-compact and locally of finite type.

**Proof.** The necessity of the conditions is immediate, in view of (6.3.1) and the remark following (6.6.1).
Conversely, suppose these conditions satisfied and let $U$ be an affine open of $Y$, with ring $A$; for every $x \in
f^{-1}(U)$, there is by hypothesis a neighborhood $V(x) \subset f^{-1}(U)$ of $x$ and a neighborhood $W(x) \subset U$ of
$y = f(x)$, containing $f(V(x))$ and such that the restriction of $f$ to $V(x)$ is a morphism $V(x) \to W(x)$ which is
of finite type. On replacing $W(x)$ by a neighborhood $W_{1}(x) \subset W(x)$ of $x$ of the form $D(g)$ (with $g \in
A$), and $V(x)$ by $V(x) \cap f^{-1}(W_{1}(x))$, one may suppose that $W(x)$ is of the form $D(g)$, hence of finite type
over $U$ (since its ring is written $A[1/g]$); consequently $V(x)$ is of finite type over $U$. Moreover $f^{-1}(U)$ is
quasi-compact by hypothesis, hence a union of a finite number of opens $V(x_{i})$, which completes the proof.

**Proposition (6.6.4).** (i) An immersion $X \to Y$ is quasi-compact if it is closed; or if the underlying space of $Y$
is locally Noetherian or if the underlying space of $X$ is Noetherian.

(ii) The composite of two quasi-compact morphisms is quasi-compact.

(iii) If $f : X \to Y$ is a quasi-compact $S$-morphism, so is $f_{(S')} : X_{(S')} \to Y_{(S')}$ for every extension $g :
S' \to S$ of the base prescheme.

(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two quasi-compact $S$-morphisms, $f \times_{S} g$ is quasi-compact.

(v) If the composite of two morphisms $f : X \to Y$, $g : Y \to Z$ is quasi-compact and if $g$ is separated, or the
underlying space of $X$ locally Noetherian, $f$ is quasi-compact.

(vi) For a morphism $f$ to be quasi-compact, it is necessary and sufficient that $f_{\mathrm{red}}$ be.

**Proof.** It will be noted that (vi) is evident, since the property of being quasi-compact for a morphism depends only
on the corresponding continuous map of the underlying spaces. Let us likewise prove the part of (v) corresponding to the
case where the underlying space $X$ is supposed locally Noetherian. Set $h = g \circ f$, and let $U$ be a quasi-compact
open in $Y$; $g(U)$ is quasi-compact (not necessarily open) in $Z$, hence contained in a finite union of quasi-compact
opens $V_{j}$ (2.1.3), and $f^{-1}(U)$ is consequently contained in the union of the $h^{-1}(V_{j})$, which are
quasi-compact subspaces of $X$, hence Noetherian subspaces. One concludes (0, 2.2.3) that $f^{-1}(U)$ is a Noetherian
space, and a fortiori quasi-compact.

To prove the other assertions, it suffices to prove (i), (ii), and (iii) (5.5.12). Now, (ii) is evident, and (i) results
from (6.3.5) when the space $Y$ is locally Noetherian or the space $X$ Noetherian, and is evident for a closed
immersion. To establish (iii), one may restrict oneself to the case where $S = Y$ (3.3.11); set $f' = f_{(S')}$ and let
$U'$ be a quasi-compact open in $S'$. For every $s' \in U'$, let $T$ be an affine open neighborhood of $g(s')$ in $S$,
and let $W$ be an affine open neighborhood of $s'$ contained in $U' \cap g^{-1}(T)$; it will suffice to show that
$f'^{-1}(W)$ is quasi-compact; in other words, one may reduce to proving that when $S$ and $S'$ are affine, the
underlying space of $X \times_{S} S'$ is quasi-compact. But since $X$ is then by hypothesis a finite union of affine
opens $V_{j}$, $X \times_{S} S'$ is the union of the underlying spaces of the affine schemes $V_{j} \times_{S} S'$
(3.2.2 and 3.2.7), which completes the proof of the proposition.

One will also note that if $X = X' \amalg X''$ is the sum of two preschemes, a morphism $f : X \to Y$ is quasi-compact
if and only if its restrictions to $X'$ and $X''$ are.

**Proposition (6.6.5).** Let $f : X \to Y$ be a quasi-compact morphism. For $f$ to be dominant, it is necessary and
sufficient that for every generic point $y$ of an irreducible component of $Y$, $f^{-1}(y)$ contain the generic point of
an irreducible component of $X$.

**Proof.** It is immediate that the condition is sufficient (without supposing $f$ quasi-compact). To see that it is
necessary, consider an affine open neighborhood $U$ of $y$; $f^{-1}(U)$ is quasi-compact, hence a finite union of affine
opens $V_{i}$, and the hypothesis that $f$ is dominant implies that $y$ belongs to the closure in $U$ of one of the
$f(V_{i})$. One may evidently suppose $X$ and $Y$ reduced; since the closure in $X$ of an irreducible component of
$V_{i}$ is an irreducible component of $X$ (0, 2.1.6), one may replace $X$ by $V_{i}$, $Y$ by the reduced closed
subprescheme of $U$ having $\overline{f(V_{i})} \cap U$ for underlying space (5.2.1), and one is thus reduced to proving
the proposition when $X = \operatorname{Spec}(A)$ and $Y = \operatorname{Spec}(B)$ are affine and reduced. Since $f$ is
dominant, $B$ is then a subring of $A$ (1.2.7), and the proposition results from the fact that every minimal prime ideal
of $B$ is the intersection of $B$ and a minimal prime ideal of $A$ (0, 1.5.8).

**Proposition (6.6.6).** (i) Every local immersion is locally of finite type.

(ii) If two morphisms $f : X \to Y$, $g : Y \to Z$ are locally of finite type, so is $g \circ f$.

(iii) If $f : X \to Y$ is an $S$-morphism locally of finite type, $f_{(S')} : X_{(S')} \to Y_{(S')}$ is locally of
finite type for every extension $S' \to S$ of the base prescheme.

(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two $S$-morphisms locally of finite type, $f \times_{S} g$ is locally of
finite type.

(v) If the composite $g \circ f$ of two morphisms is locally of finite type, $f$ is locally of finite type.

(vi) If a morphism $f$ is locally of finite type, so is $f_{\mathrm{red}}$.

**Proof.** By virtue of (5.5.12), it suffices to prove (i), (ii), and (iii). If $j : X \to Y$ is a local immersion, for
every $x \in X$, there is an open neighborhood $V$ of $j(x)$ in $Y$ and an open neighborhood $U$ of $x$ in $X$ such that
the restriction of $j$ to $U$ is a closed immersion $U \to V$ (4.5.1), so this restriction is of finite type. To
establish (ii), consider a point $x \in X$; there is by hypothesis an open neighborhood $W$ of $g(f(x))$ and an open
neighborhood $V$ of $f(x)$ such that $g(V) \subset W$ and such that $V$ is of finite type over $W$; moreover $f^{-1}(V)$
is locally of finite type over $V$ (6.6.2), so there is an open neighborhood $U$ of $x$ which is contained in
$f^{-1}(V)$ and of finite type over $V$; consequently $g(f(U)) \subset W$ and $U$ is of finite type over $W$ (6.3.4,
(ii)). Finally, to prove (iii), one may restrict oneself to the case where $Y = S$ (3.3.11); for every $x' \in X' =
X_{(S')}$, let $x$ be the image of $x'$ in $X$, $s$ the image of $x$ in $S$, $T$ an open neighborhood of $s$, $T'$ its
inverse image in $S'$, $U$ an open neighborhood of $x$ whose image is contained in $T$ and which is of finite type over
$T$; then $U \times_{S} T' = U \times_{T} T'$ is an open neighborhood of $x'$ (3.2.7) which is of finite type over $T'$
(6.3.4, (iv)).

**Corollary (6.6.7).** Let $X$, $Y$ be two $S$-preschemes which are locally of finite type over $S$. If $S$ is locally
Noetherian, $X \times_{S} Y$ is locally Noetherian.

**Proof.** Indeed, $X$, being locally of finite type over $S$, is locally Noetherian, and $X \times_{S} Y$ is locally of
finite type over $X$, hence is also locally Noetherian.

**Remark (6.6.8).** The proposition (6.3.10) and its proof extend at once to the case where one supposes only that the
morphism $f$ is locally of finite type. Likewise, the propositions (6.4.2) and (6.4.9) remain valid when one supposes
that the preschemes $X$, $Y$ figuring in their statement are only locally of finite type over the field $K$.
