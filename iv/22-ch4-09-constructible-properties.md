<!-- original page 54 -->

## §9. Constructible properties

Let $S$ be a prescheme, $f : X \to S$ a morphism *of finite presentation* `(1.6.1)`, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module of finite presentation. We propose, in this section, to give criteria ensuring, for example,
that the set of $s \in S$ such that the $k(s)$-prescheme $X_{s} = f^{-1}(s) = X \times_{S} \operatorname{Spec}(k(s))$
has a certain property, or such that the $\mathcal{O}_{X_{s}}$-Module $\mathcal{F}_{s} = \mathcal{F}
\otimes_{\mathcal{O}_{S}} k(s)$ has a certain property, is locally constructible, or at least *ind-constructible*
`(1.9.4)`; we shall see that this is the case for most of the properties that arise in algebraic geometry. Assuming only
$f$ locally of finite presentation, we shall also give `(9.9)` criteria for the set of points $x \in X$ where the fibre
$X_{f(x)}$ (or the $\mathcal{O}_{X_{f(x)}}$-Module $\mathcal{F}_{f(x)}$) has a certain property to be locally
constructible. We shall see in §12 that these results, combined with the additional hypothesis that $f$ is flat (resp.
proper and flat), allow one to prove that the sets considered in $X$ (resp. in $S$) are even *open* in many cases.

### 9.1. The principle of finite extension

**Proposition (9.1.1) (Principle of finite extension).**

<!-- label: IV.9.1.1 -->

*Let $k$ be a field, $\mathcal{C}$ a set of extensions of $k$. Assume the following conditions are satisfied:*

*(i) If $K \in \mathcal{C}$ and there exists a $k$-homomorphism $K \to K'$ (where $K'$ belongs to the universe in which
one places oneself), then $K' \in \mathcal{C}$.*

*(ii) If $K \in \mathcal{C}$, there exists a sub-extension $K'$ of $K$, of finite type over $k$, such that $K' \in
\mathcal{C}$.*

*(iii) If $K \in \mathcal{C}$ is the field of fractions of an integral $k$-algebra $A$ of finite type, there exists $f
\in A - {0}$ such that for every maximal ideal $\mathfrak{m}$ of $A_{f}$ one has $A_{f}/\mathfrak{m} \in \mathcal{C}$.*

<!-- original page 55 -->

*Let $\Omega$ be an algebraically closed extension of $k$ (in the universe under consideration). The following
conditions are equivalent:*

*a) $\mathcal{C}$ is non-empty.*

*b) There exists $K' \in \mathcal{C}$ which is a finite extension of $k$.*

*c) One has $\Omega \in \mathcal{C}$.*

Condition (i) evidently implies that b) entails c), and c) entails trivially a); let us prove that a) entails b). By
virtue of (ii) and (iii) there exists an extension $K' \in \mathcal{C}$ of the form $A/\mathfrak{m}$, where $A$ is a
$k$-algebra of finite type over $k$ and $\mathfrak{m}$ is a maximal ideal of $A$. One knows, by Hilbert's
Nullstellensatz `(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 2 of th. 1)`, that $K'$ is a finite extension of $k$.

**Corollary (9.1.2).**

<!-- label: IV.9.1.2 -->

*Under the hypotheses (i), (ii), (iii) of `(9.1.1)`, if $k$ is algebraically closed and if $\mathcal{C}$ is non-empty,
then $\mathcal{C}$ contains all extensions of $k$ in the universe considered.*

Indeed, since a) entails c), one has $k \in \mathcal{C}$, and the conclusion results from hypothesis (i).

**Remark (9.1.3).**

<!-- label: IV.9.1.3 -->

In practice, one will verify condition (ii) of `(9.1.1)` by noting that $K$ is the inductive limit of its sub-extensions
$K_{\alpha}$ of finite type, and by applying the results of §8, taking into account if necessary that for $K_{\alpha}
\subset K_{\beta}$, $K_{\beta}$ is faithfully flat over $K_{\alpha}$. Frequently the set $\mathcal{C}$ is formed of the
fields belonging to a set $\mathcal{C}'$ of $k$-algebras that satisfies the following condition:

*(i bis) If $A \in \mathcal{C}'$ and there exists a $k$-algebra homomorphism $A \to A'$ (where $A'$ belongs to the
universe in which one places oneself), then $A' \in \mathcal{C}'$.*

When this is the case, condition (i) is trivially satisfied, and one will generally verify condition (iii) of `(9.1.1)`
by noting that the field of fractions $K$ of $A$ is the inductive limit of the algebras $A_{f}$ (for the relation $D(f)
\supset D(g)$), and by applying the results of §8, taking into account if necessary that the morphisms $D(g) \to D(f)$
are open immersions.

By contrast, when (i bis) is not satisfied, the proof of (iii) is often more delicate, and is tied to constructibility
criteria that will be developed below.

Here are some typical examples of application of the principle of finite extension.

**Proposition (9.1.4).**

<!-- label: IV.9.1.4 -->

*Let $k$ be a field, $\Omega$ an algebraically closed extension of $k$, $X$ and $Y$ two preschemes of finite type over
$k$. The following conditions are equivalent:*

*a) There exists an $\Omega$-morphism $X_{(\Omega)} \to Y_{(\Omega)}$ (resp. an $\Omega$-morphism possessing one
(specified) of the properties (i) to (xiv) of `(8.10.5)`).*

*b) There exists a finite extension $k'$ of $k$ and a $k'$-morphism $X_{(k')} \to Y_{(k')}$ (resp. a $k'$-morphism
possessing the property considered).*

*c) There exists an extension $K$ of $k$ and a $K$-morphism $X_{(K)} \to Y_{(K)}$ (resp. a $K$-morphism possessing the
property considered).*

One applies remark `(9.1.3)`, taking for $\mathcal{C}'$ the set of all $k$-algebras $A$ (of the universe in which one is
placed) such that there exists an $A$-morphism $X \otimes_{k} A \to Y \otimes_{k} A$ (resp. a morphism having that one
of the properties of `(8.10.5)` that one considers). Condition (i bis) of `(9.1.3)` is then verified thanks to the fact
that the

<!-- original page 56 -->

properties envisaged in `(8.10.5)` are all stable under base change. Condition (iii) of `(9.1.1)` is therefore satisfied
by virtue of `(8.8.2, (i))` (resp. `(8.10.5)`), since $\operatorname{Spec}(k)$ is quasi-compact and quasi-separated. It
remains to verify condition (ii) of `(9.1.1)`, which follows again from `(8.8.2, (i))` and `(8.10.5)`, by viewing $K$ as
the inductive limit of its sub-extensions of finite type. One concludes therefore by `(9.1.1)`.

In particular, if there exists an extension $K$ of $k$ and a $K$-isomorphism $X_{(K)} \xrightarrow{\sim} Y_{(K)}$, one
says that $X$ and $Y$ are *geometrically isomorphic*.

The following corollary generalizes `(II, 6.6.5)`.

**Corollary (9.1.5).**

<!-- label: IV.9.1.5 -->

*Let $k$ be a field, $X$ a $k$-prescheme. If there exists an extension $K$ of $k$ such that $X_{(K)}$ is projective
(resp. quasi-projective) over $K$, then $X$ is projective (resp. quasi-projective) over $k$.*

The morphism $\operatorname{Spec}(K) \to \operatorname{Spec}(k)$ being faithfully flat and quasi-compact, it follows
already from `(2.7.1, (v))` that $X$ is of finite type over $k$. The hypothesis means that there exists a closed
immersion (resp. an immersion) $X_{(K)} \to \mathbf{P}^{r}_{K} = \mathbf{P}^{r}_{k} \otimes_{k} K$
`(II, 5.5.4, (ii) and 5.5.3)`; applying `(9.1.4)` for property (iv) (resp. (ii)) of `(8.10.5)`, one deduces that there
is a finite extension $k'$ of $k$ and a closed immersion (resp. an immersion) $X_{(k')} \to \mathbf{P}^{r}_{k'}$, that
is, $X_{(k')}$ is projective (resp. quasi-projective) over $k'$. One concludes by `(II, 6.6.5)`.

**Proposition (9.1.6).**

<!-- label: IV.9.1.6 -->

*Let $k$ be a field, $\Omega$ an algebraically closed extension of $k$, $X$ a prescheme of finite type over $k$,
$\mathcal{F}$, $\mathcal{G}$ two coherent $\mathcal{O}_{X}$-Modules. Suppose there exists an isomorphism $\mathcal{F}
\otimes_{k} \Omega \xrightarrow{\sim} \mathcal{G} \otimes_{k} \Omega$. Then there exist a finite extension $k'$ of $k$
and an isomorphism $\mathcal{F} \otimes_{k} k' \xrightarrow{\sim} \mathcal{G} \otimes_{k} k'$.*

The reasoning is the same as in `(9.1.4)`, applying `(8.5.2, (i))` (one uses here, in the proof of property (iii) of
`(9.1.1)`, the fact that the morphisms $D(g) \to D(f)$ (with the notation of `(9.1.3)`) are open immersions, and *a
fortiori* flat morphisms).

### 9.2. Constructible and ind-constructible properties

**Definition (9.2.1).**

<!-- label: IV.9.2.1 -->

*Let $P(X, \mathcal{F}, k)$ be a relation. We say that $P$ is a **constructible** (resp. **ind-constructible**)
**property of algebraic preschemes** if the following two conditions are satisfied:*

*(i) If $k$ is a field, $X$ an algebraic prescheme over $k$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module, $k'$ an
extension of $k$, then, for $P(X, \mathcal{F}, k)$ to be true, it is necessary and sufficient that $P(X_{(k')},
\mathcal{F} \otimes_{k} k', k')$ be true.*

*(ii) Let $S$ be an integral Noetherian prescheme, of generic point $\eta$, $u : X \to S$ a morphism of finite type,
$\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. For every $s \in S$, set $X_{s} = u^{-1}(s) = X \times_{S}
\operatorname{Spec}(k(s))$, $\mathcal{F}_{s} = \mathcal{F} \otimes_{\mathcal{O}_{S}} k(s)$. Let $E$ be the set of $s \in
S$ such that $P(X_{s}, \mathcal{F}_{s}, k(s))$ is true. Then one of the sets $E$, $S - E$ (resp. the set $E$) contains a
non-empty open set (and consequently is a neighbourhood of $\eta$) (resp. contains a non-empty open set if it contains
$\eta$).*

<!-- original page 57 -->

**Remarks (9.2.2).**

<!-- label: IV.9.2.2 -->

(i) This is of course a convention of language of metamathematical nature and not a mathematical definition properly
speaking. One has analogous "definitions" for relations between $k$, one or several algebraic $k$-preschemes,
$k$-morphisms between these preschemes, coherent Modules on these preschemes, or homomorphisms between these Modules.

(ii) We shall also have to consider relations in which constructible parts of preschemes figure. For example, let $P(X,
Z, k)$ be a relation; we shall say (by abuse of language) that $P$ is a **constructible** (resp. **ind-constructible**)
**property of the constructible part $Z$ of $X$** if the following two conditions are satisfied:

1° If $k$ is a field, $X$ an algebraic prescheme over $k$, $Z$ a constructible part of $X$, $k'$ an extension of $k$,
then, for $P(X, Z, k)$ to be true, it is necessary and sufficient that $P(X_{(k')}, p^{-1}(Z), k')$ be true ($p :
X_{(k')} \to X$ being the canonical projection).

2° Let $S$ be an integral Noetherian prescheme, of generic point $\eta$, $u : X \to S$ a morphism of finite type, $Z$ a
constructible part of $X$. For every $s \in S$, set $X_{s} = u^{-1}(s)$, $Z_{s} = Z \cap X_{s}$. Let $E$ be the set of
$s \in S$ such that $P(X_{s}, Z_{s}, k(s))$ is true. Then one of the sets $E$, $S - E$ (resp. the set $E$) contains a
non-empty open set (resp. contains a non-empty open set if it contains $\eta$).

One should note that in condition 2° one must assume that $Z$ is a constructible part *of $X$*, and not only that
$Z_{s}$ is a constructible part of $X_{s}$ for every $s$; the former of these two properties entails the latter
`(1.8.2)`, but not conversely.

(iii) If $P$ is a constructible property, it is clear that the same is true of "not $P$". If $P$, $Q$ are two
constructible (resp. ind-constructible) properties, the same is true of the properties "$P$ or $Q$" and "$P$ and $Q$";
indeed, if, under the hypotheses of `(9.2.1, (ii))`, $E$, $E'$ are two parts of $S$ and if $E$ contains a non-empty open
set, the same is true of $E \cup E'$, and if $S - E$ and $S - E'$ each contain a non-empty open set, the same is true of
$S - (E \cup E') = (S - E) \cap (S - E')$.

(iv) Let $P(X, \mathcal{F}, k)$ be a relation satisfying condition `(9.2.1, (i))`; let $S$ be a prescheme, $u : X \to S$
a morphism of finite type; with the notation of `(9.2.1, (ii))`, let $E$ be the set of $s \in S$ such that $P(X_{s},
\mathcal{F}_{s}, k(s))$ is true. Let on the other hand $g : S' \to S$ be an arbitrary morphism, and set $X' = X_{(S')}$,
$\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{S}} \mathcal{O}_{S'}$; then it follows from the transitivity of fibres
`(I, 3.6.4)` and from condition `(9.2.1, (i))` that *the set of $s' \in S'$ such that $P(X'_{s'}, \mathcal{F}'_{s'},
k(s'))$ is true is equal to $g^{-1}(E)$*. This extends at once to the case where several preschemes, Modules, morphisms
of preschemes, or homomorphisms of Modules figure in $P$, and to properties of the type considered in (ii).

(v) As we shall see in the remainder of this section and in the course of the rest of Chap. IV, most properties $P$
satisfying condition `(9.2.1, (i))` also satisfy `(9.2.1, (ii))`. As possible exceptions, let us note the property of
being *projective*, or *quasi-projective*, or *affine*, or *quasi-affine* over the base field (for an algebraic
prescheme); we shall see `(9.6.2)` that these properties are ind-constructible, but we shall later give an example where
$S$ is a non-empty open part of $\operatorname{Spec}(\mathbb{Z})$ (or an open part of an elliptic curve over a finite
field) and where all the fibres $X_{s}$

<!-- original page 58 -->

*except* the generic fibre $X_{\eta}$ are projective over $k(s)$ (all the preschemes $X_{s}$ being of dimension 2).

**Proposition (9.2.3).**

<!-- label: IV.9.2.3 -->

*Let $P$ be a constructible (resp. ind-constructible) property of algebraic preschemes, $S$ a prescheme, $X$ a prescheme
of finite presentation over $S$, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation. Then
the set $E$ of $s \in S$ such that $P(X_{s}, \mathcal{F}_{s}, k(s))$ is true is locally constructible (resp.
ind-constructible). Moreover, if $S$ is irreducible of generic point $\eta$, then one of the two sets $E$, $S - E$ is a
neighbourhood of $\eta$ in $S$ (resp. $E$ is a neighbourhood of $\eta$ if it contains this point).*

To prove these assertions, one may restrict to the case where $S = \operatorname{Spec}(A)$ is affine. One then knows
that there exists a sub-ring `A_0` of $A$ which is a $\mathbb{Z}$-algebra of finite type, an `A_0`-prescheme of finite
type `X_0`, and a coherent $\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$ such that $X$ is isomorphic to $X_{0}
\otimes_{A_{0}} A$ and $\mathcal{F}$ to $\mathcal{F}_{0} \otimes_{A_{0}} A$ `(8.9.1)`. Let $p : S \to S_{0} =
\operatorname{Spec}(A_{0})$ be the morphism corresponding to the injection $A_{0} \to A$, and let `E_0` be the set of
$s_{0} \in S_{0}$ such that $P((X_{0})_{s_{0}}, (\mathcal{F}_{0})_{s_{0}}, k(s_{0}))$ is true; then, by virtue of
`(9.2.2, (iv))`, one has $E = p^{-1}(E_{0})$; one may therefore `(1.8.2)` restrict to the case where $S$ is the spectrum
of a $\mathbb{Z}$-algebra of finite type, hence a Noetherian scheme. Let us use the constructibility criterion
$(0_{III}, 9.2.3)$ (resp. the ind-constructibility criterion `(1.9.10)`); one is then reduced, using as above
`(9.2.2, (iv))` and replacing $S$ by an integral closed sub-scheme of $S$, to the case where $S$ is Noetherian and
integral, and one must prove that $E$ is rare in $S$ or contains a non-empty open set of $S$ (resp. that $E$ contains a
non-empty open set of $S$ if it contains the generic point); but this is guaranteed by virtue of condition
`(9.2.1, (ii))`.

One should note that one has used `(9.2.1, (ii))` only when $S$ is the spectrum of an integral ring of finite type over
$\mathbb{Z}$. It is clear on the other hand that the statement of `(9.2.3)` also applies when several preschemes,
Modules on these preschemes, morphisms of preschemes, or homomorphisms of Modules figure in $P$. It still applies when
(finitely many) parts of the preschemes considered figure in it, provided that one imposes on these parts the condition
of being *locally constructible*. Indeed, the restriction to the case where $S$ is affine shows that one may restrict to
the case where these parts are constructible: one then applies `(8.3.11)`, which shows (with the notation above) that a
constructible part of $X$ is the inverse image of a constructible part of `X_0` for a suitable choice of `A_0`.

**Corollary (9.2.4).**

<!-- label: IV.9.2.4 -->

*Let $P$ be a constructible (resp. ind-constructible) property of algebraic preschemes, $X$, $Y$ two $S$-preschemes of
finite presentation, $f : X \to Y$ an $S$-morphism. For every $s \in S$, set $X_{s} = X \times_{S}
\operatorname{Spec}(k(s))$, $Y_{s} = Y \times_{S} \operatorname{Spec}(k(s))$, $f_{s} = f \times 1 : X_{s} \to Y_{s}$.
Then the set $E$ of $s \in S$ such that, for every $y \in Y_{s}$, the property $P(f^{-1}_{s}(y), k(y))$ is true, is
locally constructible (resp. ind-constructible).*

Indeed, let $Z$ be the set of $y \in Y$ such that $P(f^{-1}(y), k(y))$ is true. As the fibres $f^{-1}(y)$ and
$f^{-1}_{s}(y)$ are isomorphic, one sees that $E$ is the set of $s \in S$ such that $Y_{s} \subset Z$; if $g : Y \to S$
is the structure morphism, one therefore has $E = S - g(Y - Z)$.

<!-- original page 59 -->

Now $f$ is of finite presentation `(1.6.2, (v))`, so it follows from `(9.2.3)` that $Z$ is locally constructible (resp.
ind-constructible) in $Y$, hence $Y - Z$ is locally constructible (resp. pro-constructible) in $Y$. Since $g$ is of
finite presentation, $g(Y - Z)$ is locally constructible (resp. pro-constructible) in $S$, by virtue of Chevalley's
theorem `(1.8.4)` (resp. of `(1.9.5, (vii))`); hence $E$ is locally constructible (resp. ind-constructible) in $S$.

**Remark (9.2.5).**

<!-- label: IV.9.2.5 -->

One should note that if $P$ is a property of algebraic preschemes for which prop. `(9.2.3)` is true, then $P$ also
satisfies condition `(9.2.1, (ii))`: this follows from the fact that in an irreducible Noetherian space, a constructible
set is rare or contains a non-empty open set $(0_{III}, 9.2.3)$.

**Proposition (9.2.6).**

<!-- label: IV.9.2.6 -->

*Let $P$ denote one of the following properties of a $k$-prescheme $X$:*

*(i) $X$ is empty.*

*(ii) $X$ is finite over $k$.*

*(iii) $X$ is radicial over $k$.*

*(iv) $\dim(X)$ belongs to a given part $\Phi$ of the set $\overline{\mathbb{Z}} = \mathbb{Z} \cup {-\infty}$.*

*Then $P$ is constructible.*

It is clear that (i) and (ii) are special cases of (iv), taking respectively for $\Phi$ the set ${-\infty}$ and the set
${-\infty, 0}$. One has therefore only to prove (iii) and (iv). In each of these two cases condition (i) of `(9.2.1)` is
fulfilled by virtue of `(2.7.1, (xv))` and `(4.1.4)`. On the other hand, in case (iii), the property $P$ satisfies the
conclusion of `(9.2.3)` by virtue of `(1.8.7)`; it remains therefore to see that the same is true in case (iv). This
will result from the more precise proposition that follows.

**Proposition (9.2.6.1).**

<!-- label: IV.9.2.6.1 -->

*If $f : X \to S$ is a morphism of finite presentation, the function $s \mapsto \dim(f^{-1}(s))$ is locally
constructible.*

The question is local on $S$, so one may suppose that $S = \operatorname{Spec}(A)$ is affine and prove that for every
$n$, the set $E$ of $s \in S$ such that $\dim(X_{s}) = n$ is constructible. The same reasoning as in `(9.2.3)` reduces
to the case where $A$ is Noetherian and integral, and it then suffices to prove:

**Corollary (9.2.6.2).**

<!-- label: IV.9.2.6.2 -->

*Let $S$ be an integral Noetherian prescheme of generic point $\eta$, $f : X \to S$ a morphism of finite type. Then
there exists a neighbourhood of $\eta$ in $S$ such that the function $s \mapsto \dim(X_{s})$ is constant in this
neighbourhood.*

The images by $f$ of the irreducible components (finitely many) of $X$ which do not meet $X_{\eta}$ are contained in
closed parts of $S$ not containing $\eta$ (since $S$ is integral $(0_{I}, 2.1.5)$), so (replacing $S$ by an open
neighbourhood of $\eta$) one may restrict to the case where all the irreducible components $X_{i}$ of $X$ meet
$X_{\eta}$; denote again by $X_{i}$ the reduced closed sub-prescheme of $X$ having $X_{i}$ as underlying space; since
`dim(X_s) = sup_i dim((X_i)_s)` `(4.1.1)`, one may restrict

<!-- original page 60 -->

to the case where $X$ is irreducible. There then exists a finite cover $(U_{j})$ of $X$ by everywhere-dense affine open
sets, and the numbers $\dim((U_{j})_{\eta})$ are all equal to $n = \dim(X_{\eta})$ `(4.1.1.3)`; one may therefore
restrict to the case where $X$ is affine, hence also $X_{\eta}$. There then exists, by virtue of `(4.1.2)`, a non-empty
open set $W$ of $X$ such that $W \subset X_{\eta}$, and a finite surjective $k(\eta)$-morphism $h : W_{\eta} \to
\mathbf{V}^{n}_{k(\eta)} (= \operatorname{Spec}(k(\eta)[T_{1}, \cdots, T_{n}]))$; applying `(8.8.2, (i))` and the method
of `(8.1.2, a))`, one deduces (replacing $S$ if necessary by a neighbourhood of $\eta$) that $h = g_{\eta}$, where $g :
W \to \mathbf{V}^{n}_{A} (= \operatorname{Spec}(A[T_{1}, \cdots, T_{n}]))$ is an $S$-morphism, and one may suppose this
morphism finite and surjective by virtue of `(8.10.5, (vi) and (x))`. One concludes that for every $s \in S$, the
morphism $g_{s} : W_{s} \to \mathbf{V}^{n}_{k(s)}$ is finite and surjective, hence $\dim(W_{s}) = n$ `(4.1.2)`.

### 9.3. Constructible properties of morphisms of algebraic preschemes

**Proposition (9.3.1).**

<!-- label: IV.9.3.1 -->

*Let $P(X, k)$ be a constructible (resp. ind-constructible) property of algebraic preschemes. Denote by `P'(f, X, Y, k)`
the following relation: $f : X \to Y$ is a $k$-morphism of algebraic $k$-preschemes such that for every $y \in Y$, one
has the property $P(f^{-1}(y), k(y))$. Then $P'$ is a constructible (resp. ind-constructible) property.*

Indeed, since $P$ satisfies condition `(9.2.1, (i))`, the same is true of $P'$ by virtue of the transitivity of fibres
`(I, 3.6.4)`; on the other hand, the fact that $P'$ satisfies condition `(9.2.1, (ii))` results from `(9.2.4)`, in view
of remark `(9.2.5)`.

**Proposition (9.3.2).**

<!-- label: IV.9.3.2 -->

*Let $P$ denote one of the following properties of a $k$-morphism $f : X \to Y$ of algebraic $k$-preschemes:*

*(i) $f$ is surjective.*

*(ii) $f$ is quasi-finite.*

*(iii) $f$ is radicial.*

*(iv) For every $y \in Y$, $\dim(f^{-1}(y))$ belongs to $\Phi$ (notation of `(9.2.6)`).*

*Then $P$ is constructible.*

This follows at once from `(9.3.1)` and `(9.2.6)` if one takes into account that $f$ is of finite type `(1.5.4, (v))`,
the characterization of radicial morphisms `(I, 3.5.8)`, and that of quasi-finite morphisms `(II, 6.2.2)`.

**Proposition (9.3.3).**

<!-- label: IV.9.3.3 -->

*Suppose the hypotheses of `(8.8.1)` are satisfied, the notation of which we retain; suppose in addition that
$S_{\alpha}$ is quasi-compact, $X_{\alpha}$ and $Y_{\alpha}$ of finite presentation over $S_{\alpha}$, and let
$f_{\alpha} : X_{\alpha} \to Y_{\alpha}$ be an $S_{\alpha}$-morphism. Let $P$ be an ind-constructible property of
morphisms of algebraic preschemes. For every $s \in S$ (resp. $s_{\lambda} \in S_{\lambda}$) set $X_{s} = X \times_{S}
\operatorname{Spec}(k(s))$, $Y_{s} = Y \times_{S} \operatorname{Spec}(k(s))$, $f_{s} = f \times 1 : X_{s} \to Y_{s}$
(resp. $X_{\lambda, s_{\lambda}} = X_{\lambda} \times_{S_{\lambda}} \operatorname{Spec}(k(s_{\lambda}))$, $Y_{\lambda,
s_{\lambda}} = Y_{\lambda} \times_{S_{\lambda}} \operatorname{Spec}(k(s_{\lambda}))$, $f_{\lambda, s_{\lambda}} =
f_{\lambda} \times 1 : X_{\lambda, s_{\lambda}} \to Y_{\lambda, s_{\lambda}}$). Then, in order that for every $s \in S$
one has the property $P(f_{s})$, it is necessary and sufficient that there exist $\lambda \geqslant \alpha$ such that
for every $s_{\lambda} \in S_{\lambda}$, one has $P(f_{\lambda, s_{\lambda}})$.*

Indeed, let $E$ (resp. $E_{\lambda}$) be the set of $s \in S$ (resp. $s_{\lambda} \in S_{\lambda}$) such that the
property $P(f_{s})$ (resp. $P(f_{\lambda, s_{\lambda}})$) is true; it follows from `(9.2.2, (iv))` that one has $E_{\mu}
= u^{-1}_{\lambda \mu}(E_{\lambda})$ for $\lambda \leqslant \mu$, and $E = u^{-1}_{\lambda}(E_{\lambda})$; moreover, by
virtue of `(9.2.3)`, $E$ (resp. $E_{\lambda}$) is ind-constructible in $S$ (resp. $S_{\lambda}$); the proposition
therefore results from `(8.3.4)` applied to the ind-constructible part $E$ of $S$.

<!-- original page 61 -->

This result generalizes without difficulty to properties $P$ of the type considered in `(9.2.3, (i) and (ii))`.

**Remark (9.3.4).**

<!-- label: IV.9.3.4 -->

The conjunction of `(9.3.3)` and `(9.3.2, (ii))` proves the assertion `(8.10.5, (xi))`.

**Proposition (9.3.5).**

<!-- label: IV.9.3.5 -->

*Let $P(X, Y, k)$ be the property: "$X$ and $Y$ are two preschemes of finite type over the field $k$, and there exists
an extension $k'$ of $k$ and a $k'$-morphism $g : X_{(k')} \to Y_{(k')}$ satisfying $Q(g)$", where $Q$ is one of the
properties (i) to (xiv) of `(8.10.5)`. Then $P$ is an ind-constructible property.*

The definition of $P$ shows indeed that condition `(9.2.1, (i))` is satisfied, taking account of the fact that the
property $Q(g)$ is stable under change of base field, and that two extensions of $k$ can always be considered as
sub-extensions of a third extension of $k$. To verify `(9.2.1, (ii))`, one may restrict to the case where $S =
\operatorname{Spec}(A)$ is affine; if $K = k(\eta)$, the field of fractions of $A$, there exists by hypothesis and by
virtue of `(9.1.4)` a finite extension $K'$ of $K$ and a $K'$-morphism $g' : (X_{\eta})_{(K')} \to (Y_{\eta})_{(K')}$
satisfying $Q(g')$, and $K'$ is evidently the field of fractions of an integral $A$-algebra $A'$ finite over $A$. If one
sets $S' = \operatorname{Spec}(A')$, it then follows from `(8.10.5)` that there is a neighbourhood $U'$ of the generic
point $\eta'$ of $S'$ such that, if one sets $X' = X \otimes_{A} A'$, $Y' = Y \otimes_{A} A'$, there exists, for every
$s' \in U'$, a morphism $X'_{s'} \to Y'_{s'}$ having the property $Q$. But the morphism $h : S' \to S$ is finite, hence
closed, and since $h^{-1}(\eta) = {\eta'}$, $h(U')$ contains an open neighbourhood $U$ of $\eta$ in $S$; for every $s
\in U$, there is therefore $s' \in U'$ such that $h(s') = s$, and since $X'_{s'} = X_{s} \otimes_{k(s)} k(s')$, $Y'_{s'}
= Y_{s} \otimes_{k(s)} k(s')$, the property $P(X_{s}, Y_{s}, k(s))$ is true for every $s \in U$.

**Example (9.3.6).**

<!-- label: IV.9.3.6 -->

Take for example for $Q$ the property of being an isomorphism. Then, by combining `(9.3.5)` and `(9.3.3)`, one has the
following property: the notations and hypotheses being those of `(8.8.1)`, $S_{\alpha}$ being quasi-compact,
$X_{\alpha}$ and $Y_{\alpha}$ of finite presentation over $S_{\alpha}$, in order that, for every $s \in S$, $X_{s}$ and
$Y_{s}$ be geometrically isomorphic `(9.1.4)`, it is necessary and sufficient that there exist $\lambda \geqslant
\alpha$ such that, for every $s_{\lambda} \in S_{\lambda}$, $X_{\lambda, s_{\lambda}}$ and $Y_{\lambda, s_{\lambda}}$ be
geometrically isomorphic.

One has an analogous result when the preschemes one considers are equipped with "composition laws" of a certain kind
$(0_{III}, 8.2.1)$, for example "preschemes in groups", "preschemes in rings", etc. $(0_{III}, 8.2.3)$. Then the
preceding statement is still valid when by "isomorphism" one means isomorphisms of preschemes that are *homomorphisms*
for the composition laws considered $(0_{III}, 8.2.2)$; it suffices here to use not only `(8.10.5)` but also
`(8.8.2, (i))`, remarking that the notion of homomorphism for a composition law is expressed by writing that diagrams of
morphisms of preschemes are commutative (it is of course necessary that the transition morphisms $X_{\mu} \to
X_{\lambda}$ and $Y_{\mu} \to Y_{\lambda}$ for $\lambda \leqslant \mu$ be homomorphisms for the composition laws
envisaged).

One may also, instead of considering morphisms of preschemes as in `(9.3.5)`, consider homomorphisms of Modules, using
`(9.1.6)` in place of `(9.1.5)`.

<!-- original page 62 -->

### 9.4. Constructibility of certain properties of modules

**Notation (9.4.1).**

<!-- label: IV.9.4.1 -->

*In this number and the following ones up to the end of §9, we shall systematically use the following notation: given a
morphism $f : X \to S$, we shall set, for every $s \in S$, $X_{s} = f^{-1}(s) = X \times_{S} \operatorname{Spec}(k(s))$;
for every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, $\mathcal{F}_{s}$ will denote the
$\mathcal{O}_{X_{s}}$-Module $\mathcal{F} \otimes_{\mathcal{O}_{S}} k(s)$, and for every homomorphism $u : \mathcal{F}
\to \mathcal{G}$ of $\mathcal{F}$ into a quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{G}$, $u_{s} : \mathcal{F}_{s}
\to \mathcal{G}_{s}$ will be the morphism $p*(u)$, where $p$ is the canonical projection $X_{s} \to X$. For every
section $g$ of $\mathcal{F}$ above $X$, one shall denote by $g_{s}$ the image of $g$ under the canonical homomorphism
$\Gamma(X, \mathcal{F}) \to \Gamma(X_{s}, \mathcal{F}_{s})$. For every part $Z$ of $X$, one will denote by $Z_{s}$ the
inverse image $p^{-1}(Z) = Z \cap X_{s}$ `(I, 3.6.1)`. Finally, if $Y$ is a second $S$-prescheme and $h : X \to Y$ an
$S$-morphism, one will denote by $h_{s}$ the morphism $h \times 1 : X_{s} \to Y_{s}$.*

**Proposition (9.4.2).**

<!-- label: IV.9.4.2 -->

*Let $S$ be an integral prescheme of generic point $\eta$, $f : X \to S$ a morphism of finite presentation,
$\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ three quasi-coherent $\mathcal{O}_{X}$-Modules of finite presentation. Let
$u : \mathcal{F} \to \mathcal{G}$, $v : \mathcal{G} \to \mathcal{H}$ be two homomorphisms of $\mathcal{O}_{X}$-Modules,
and suppose that the sequence $\mathcal{F}_{\eta} \xrightarrow{u_{\eta}} \mathcal{G}_{\eta} \xrightarrow{v_{\eta}}
\mathcal{H}_{\eta}$ is exact. Then there exists an open neighbourhood $U$ of $\eta$ in $S$ such that, for every $s \in
U$, the sequence $\mathcal{F}_{s} \xrightarrow{u_{s}} \mathcal{G}_{s} \xrightarrow{v_{s}} \mathcal{H}_{s}$ is exact.*

With the general notation of `(9.2.1)`, this concerns the relation $P(X, \mathcal{F}, \mathcal{G}, \mathcal{H}, u, v,
k)$: "$X$ is an algebraic prescheme over the field $k$, $\mathcal{F} \to \mathcal{G} \to \mathcal{H}$ an exact sequence
of quasi-coherent $\mathcal{O}_{X}$-Modules". Since, for every extension $k'$ of $k$, the canonical projection $X_{(k')}
\to X$ is a faithfully flat morphism `(2.2.13)`, condition `(9.2.1, (i))` is satisfied `(2.2.7)`. By virtue of
`(9.2.3)`, one may restrict to the case where $S$ is integral and Noetherian, in which case $X$ is Noetherian, and
$\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are coherent $\mathcal{O}_{X}$-Modules. The hypothesis implies that there
exists an open neighbourhood $U$ of $\eta$ in $S$ such that the sequence $\mathcal{F}|f^{-1}(U) \to
\mathcal{G}|f^{-1}(U) \to \mathcal{H}|f^{-1}(U)$ is exact, by virtue of `(8.5.8, (i))` applied following the general
method of `(8.1.2, a))`, and one may therefore already suppose that the sequence $\mathcal{F} \to \mathcal{G} \to
\mathcal{H}$ is exact; it evidently suffices to prove that one has $Ker(v_{s}) = (Ker v)_{s}$ and $Im(u_{s}) = (Im
u)_{s}$ for every $s$ close to $\eta$ in $S$; consequently (taking account of the fact that the
$\mathcal{O}_{X}$-Modules $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are coherent and of $(0_{I}, 5.3.4)$) one is
reduced to proving the proposition in the particular case where the sequence $0 \to \mathcal{F} \to \mathcal{G} \to
\mathcal{H} \to 0$ is exact. But then there is an open set $U$ in $S$ containing $\eta$ and such that
$\mathcal{H}|f^{-1}(U)$ is flat over $U$ `(6.9.1)`; it then follows from `(2.1.8)` that for every $s \in U$, the
sequence $0 \to \mathcal{F}_{s} \to \mathcal{G}_{s} \to \mathcal{H}_{s} \to 0$ is exact, which completes the proof.

**Corollary (9.4.3).**

<!-- label: IV.9.4.3 -->

*Let $S$ be an integral prescheme, of generic point $\eta$, $f : X \to S$ a morphism of finite presentation. Let
$\mathcal{L}\bullet = (\mathcal{L}^{i})_{i \in \mathbb{Z}}$ be a complex of quasi-coherent $\mathcal{O}_{X}$-Modules of
finite presentation. For every $i$, there exists an open neighbourhood $U$ of $\eta$ in $S$ such that the canonical
homomorphisms*

$$ (9.4.3.1) (\mathcal{H}^{i}(\mathcal{L}\bullet))_{s} \to \mathcal{H}^{i}(\mathcal{L}\bullet_{s}) $$

*are bijective for every $s \in U$.*

<!-- original page 63 -->

One may evidently restrict to a complex with three terms of degrees $-1, 0, +1$: $\mathcal{M} \xrightarrow{u}
\mathcal{N} \xrightarrow{v} \mathcal{P}$ with $v \circ u = 0$; and to $i = 0$; the homomorphism to consider is then the
canonical homomorphism $(Ker v / Im u)_{s} \to Ker(v_{s})/Im(u_{s})$. Using `(8.9.1)` and `(8.5.2, (i))`, one sees that
one may reduce to the case where $S$ (hence also $X$) is Noetherian, and consequently $\mathcal{M}$, $\mathcal{N}$,
$\mathcal{P}$ are coherent $\mathcal{O}_{X}$-Modules; then $Im(u)$ and $Ker(v)$ are also coherent $(0_{I}, 5.3.4)$ and
moreover there exists a neighbourhood $U$ of $\eta$ such that for $s \in U$, one has $Ker(v_{s}) = (Ker(v))_{s}$ and
$Im(u_{s}) = (Im(u))_{s}$ `(9.4.2)`; the conclusion then results from `(9.4.2)` applied to the exact sequence $0 \to
Im(u) \to Ker(v) \to Ker(v)/Im(u) \to 0$, taking account of the fact that $\mathcal{O}_{\eta} = k(\eta)$ (since $S$ is
integral) and consequently the sequence

```text
  0 → (Im u)_η → (Ker v)_η → (Ker v / Im u)_η → 0
```

is exact.

**Proposition (9.4.4).**

<!-- label: IV.9.4.4 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ three
quasi-coherent $\mathcal{O}_{X}$-Modules of finite presentation. Let $u : \mathcal{F} \to \mathcal{G}$, $v : \mathcal{G}
\to \mathcal{H}$ be two homomorphisms of $\mathcal{O}_{X}$-Modules. Then the set $E$ of $s \in S$ such that the sequence
$\mathcal{F}_{s} \xrightarrow{u_{s}} \mathcal{G}_{s} \xrightarrow{v_{s}} \mathcal{H}_{s}$ is exact is locally
constructible.*

Taking account of `(9.2.3)`, one must establish that the property $P$ considered in `(9.4.2)` is constructible. One has
already remarked in the proof of `(9.4.2)` that condition `(9.2.1, (i))` is satisfied for this property, and it remains
to verify condition `(9.2.1, (ii))`. Suppose then that $S$ is integral Noetherian, of generic point $\eta$, and let us
prove that $E$ or $S - E$ is a neighbourhood of $\eta$. If $\eta \in E$, our assertion follows from `(9.4.2)`, and one
may therefore restrict to the case where $\eta \notin E$, that is, the sequence $\mathcal{F}_{\eta}
\xrightarrow{u_{\eta}} \mathcal{G}_{\eta} \xrightarrow{v_{\eta}} \mathcal{H}_{\eta}$ is not exact. Let us distinguish
two cases.

1° Set $w = v \circ u$, and suppose first that $w_{\eta} = v_{\eta} \circ u_{\eta} \neq 0$. Since $\mathcal{F}$,
$\mathcal{G}$, $\mathcal{H}$ are coherent, the same is true of $\mathcal{N} = Ker(w)$ $(0_{I}, 5.3.4)$; it then follows
from `(9.4.2)` applied to the exact sequence $0 \to \mathcal{N} \to \mathcal{F} \to \mathcal{F}$ that there is a
neighbourhood $U$ of $\eta$ in $S$ such that, for $s \in S$, $Ker(w_{s}) = \mathcal{N}_{s}$; by restricting $S$, one may
therefore suppose this relation verified for every $s \in S$. Let $j$ be the canonical injection $\mathcal{N} \to
\mathcal{F}$, and set $\mathcal{M} = Coker(j)$; the right-exactness of the functor $\mathcal{F} \mapsto \mathcal{F}_{s}$
entails that $\mathcal{M}_{s} = Coker(j_{s})$ for every $s \in S$. The hypothesis $w_{\eta} \neq 0$ means that
$\mathcal{M}_{\eta} \neq 0$; since $\mathcal{M}$ is coherent $(0_{I}, 5.3.4)$, it follows from `(1.8.6)` that there is
an open neighbourhood $U$ of $\eta$ in $S$ such that $\mathcal{M}_{s} \neq 0$ for $s \in U$, hence $w_{s} \neq 0$ for $s
\in U$, and *a fortiori* $S - E$ is a neighbourhood of $\eta$.

2° Suppose that $w_{\eta} = 0$; by virtue of `(8.5.2, (i))`, applied following the general method of `(8.1.2, a))`,
there exists an open neighbourhood $U$ of $\eta$ such that $w|f^{-1}(U) = 0$; replacing $S$ by $U$, one may already
suppose $w = 0$ in $X$. Then $\mathcal{F} \xrightarrow{u} \mathcal{G} \xrightarrow{v} \mathcal{H}$ is a complex with
three terms $\mathcal{L}\bullet$, to which one may apply `(9.4.3)`; by hypothesis one has
$(\mathcal{H}^{0}(\mathcal{L}\bullet))_{\eta} = \mathcal{H}^{0}(\mathcal{L}\bullet_{\eta}) \neq 0$, and
$\mathcal{H}^{0}(\mathcal{L}\bullet)$ is coherent $(0_{I}, 5.3.4 and 5.3.3)$, hence it follows from `(1.8.6)` that there
is an open neighbourhood $U$ of $\eta$ such that $(\mathcal{H}^{0}(\mathcal{L}\bullet))_{s} \neq 0$ for every $s \in U$;
but as one may suppose that $\mathcal{H}^{0}(\mathcal{L}\bullet)_{s} = (\mathcal{H}^{0}(\mathcal{L}\bullet))_{s}$ for $s
\in U$ by `(9.4.3)`, one sees again that $S - E$ is a neighbourhood of $\eta$ in $S$.

<!-- original page 64 -->

**Corollary (9.4.5).**

<!-- label: IV.9.4.5 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$, $\mathcal{G}$ two quasi-coherent
$\mathcal{O}_{X}$-Modules of finite presentation, $u : \mathcal{F} \to \mathcal{G}$ a homomorphism of
$\mathcal{O}_{X}$-Modules. Then the set of $s \in S$ such that $u_{s}$ is injective (resp. surjective, bijective, zero)
is locally constructible.*

It suffices to apply `(9.4.4)` to the sequences $0 \to \mathcal{F} \xrightarrow{u} \mathcal{G}$, $\mathcal{F}
\xrightarrow{u} \mathcal{G} \to 0$, $0 \to \mathcal{F} \xrightarrow{u} \mathcal{G} \to 0$, $\mathcal{F} \xrightarrow{u}
\mathcal{G} \xrightarrow{1_{\mathcal{G}}} \mathcal{G}$.

**Corollary (9.4.6).**

<!-- label: IV.9.4.6 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. Let $h$ be a section of $\mathcal{F}$ above $X$; for every $s \in S$, let $h_{s}$ be the
corresponding section of $\mathcal{F}_{s}$ above $X_{s}$ (for the projection morphism $X_{s} \to X$). Then the set of $s
\in S$ such that $h_{s} = 0$ is locally constructible.*

It suffices to note that $h$ corresponds to a homomorphism $u : \mathcal{O}_{X} \to \mathcal{F}$ $(0_{I}, 5.1.1)$ and
$h_{s}$ to the homomorphism $u_{s}$.

**Proposition (9.4.7).**

<!-- label: IV.9.4.7 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. The set $E$ (resp. $E'$) of $s \in S$ such that $\mathcal{F}_{s}$ is a locally free
$\mathcal{O}_{X_{s}}$-Module (resp. locally free of rank $n$) is locally constructible.*

If $X$ is an algebraic prescheme over a field $k$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module, $k'$ an extension
of $k$, then, for $\mathcal{F}$ to be locally free (resp. locally free of rank $n$), it is necessary and sufficient that
the same be true of $\mathcal{F} \otimes_{k} k'$, since the projection $X_{(k')} \to X$ is a faithfully flat morphism
`(2.2.7)`. In other words, condition `(9.2.1, (i))` is verified for the properties whose constructibility one wishes to
prove, and it remains to verify `(9.2.1, (ii))`; one may therefore again suppose that $S$ is affine, Noetherian, and
integral. There are once more four cases to envisage.

1° $\eta \in E$. It follows from `(8.5.5)`, applied following the general method of `(8.1.2, a))`, that there exists an
open neighbourhood $U$ of $\eta$ in $S$ such that $\mathcal{F}|f^{-1}(U)$ is locally free; *a fortiori*
$\mathcal{F}_{s}$ is locally free for every $s \in U$.

2° $\eta \in E'$. Same reasoning as in 1°.

3° $\eta \in S - E$. Since $\mathcal{F}_{\eta}$ is a coherent $\mathcal{O}_{X_{\eta}}$-Module, to say that it is not
locally free is equivalent to saying that it is *not flat* over $\mathcal{O}_{X_{\eta}}$
`(Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of th. 1)`. The fact that $S - E$ is a neighbourhood of $\eta$ will
therefore result from the more general lemma below (applied to the case where $g$ is the identity).

**Lemma (9.4.7.1).**

<!-- label: IV.9.4.7.1 -->

*Let $S$ be an integral Noetherian prescheme, of generic point $\eta$, $X$, $Y$ two $S$-preschemes of finite type over
$S$, $g : X \to Y$ an $S$-morphism, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. If $\mathcal{F}_{\eta}$ is not
$g_{\eta}$-flat, then there exists an open neighbourhood $U$ of $\eta$ in $S$ such that for every $s \in U$,
$\mathcal{F}_{s}$ is not $g_{s}$-flat.*

Taking account of `(2.1.2)` and of `Bourbaki, Alg. comm., chap. I, §2, n° 3, Remark 1`, the hypothesis means that there
exists a non-empty open set $V$ of $Y_{\eta}$ and an injective homomorphism $v : \mathcal{M} \to \mathcal{N}$ of
coherent $\mathcal{O}_{V}$-Modules, such that the homomorphism $1 \otimes v : \mathcal{F}_{\eta}
\otimes_{\mathcal{O}_{V}} \mathcal{M} \to \mathcal{F}_{\eta} \otimes_{\mathcal{O}_{V}} \mathcal{N}$ is not injective.
One has $V = Y_{\eta} \cap W$, where $W$ is open in $Y$ `(I, 3.6.1)`, and it follows from `(8.5.2, (i) and (ii))`,
applied following the method of `(8.1.2, a))`, that there exists an open neighbourhood `U_0` of $\eta$ in $S$, two
coherent $\mathcal{O}_{Z}$-Modules

<!-- original page 65 -->

$\mathcal{M}'$, $\mathcal{N}'$ (where $Z = W \cap h^{-1}(U_{0})$, $h : Y \to S$ being the structure morphism) and an
$\mathcal{O}_{Z}$-homomorphism $u : \mathcal{M}' \to \mathcal{N}'$ such that $\mathcal{M}'_{\eta} = \mathcal{M}$,
$\mathcal{N}'_{\eta} = \mathcal{N}$ and $v = u_{\eta}$; one may therefore suppose `U_0` taken such that for $s \in
U_{0}$, $u_{s} : \mathcal{M}'_{s} \to \mathcal{N}'_{s}$ is injective `(9.4.5)`. But for every $s \in U_{0}$, the
homomorphism $1 \otimes u_{s} : \mathcal{F}_{s} \otimes_{\mathcal{O}_{Y_{s}}} \mathcal{M}'_{s} \to \mathcal{F}_{s}
\otimes_{\mathcal{O}_{Y_{s}}} \mathcal{N}'_{s}$ is none other than $(1 \otimes u)_{s}$; the hypothesis that $(1 \otimes
u)_{\eta}$ is non-injective therefore entails `(9.4.5)` the existence of a non-empty open set $U \subset U_{0}$ such
that for every $s \in U$, $(1 \otimes u)_{s}$ is non-injective, and consequently $\mathcal{F}_{s}$ is not $g_{s}$-flat
for every $s \in U$.

4° $\eta \in S - E'$. It is clear that $S - E \subset S - E'$, and if $\eta \in S - E$, $S - E'$ is *a fortiori* a
neighbourhood of $\eta$ by 3°. Suppose therefore that $\eta \in E$, hence $\mathcal{F}_{\eta}$ locally free; these
hypotheses entail that $X_{\eta}$ is disconnected, and that the ranks of the locally free
$\mathcal{O}_{X_{\eta}}$-Module $\mathcal{F}_{\eta}$ are not the same on the various connected components of $X_{\eta}$.
Now it follows from `(8.4.2)`, applied following the method of `(8.1.2, a))`, that one may suppose (replacing $S$ by an
open neighbourhood of $\eta$) that $X$ and $X_{\eta}$ have the same number of connected components, the connected
components of $X_{\eta}$ being the intersections of $X_{\eta}$ with the connected components of $X$. The conclusion then
results from the reasoning made in 2°, applied to each of the connected components of $X$ (which are finite in number).

**Remark (9.4.7.2).**

<!-- label: IV.9.4.7.2 -->

The lemma `(9.4.7.1)` will be generalized later and freed of Noetherian hypotheses `(11.2.8)`.

**Proposition (9.4.8).**

<!-- label: IV.9.4.8 -->

*Let $S$ be a locally Noetherian prescheme, $f : X \to S$ a morphism of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module. Suppose that for every $s \in S$, $X_{s}$ is a locally integral prescheme. Then the set $E$
(resp. $E'$) of $s \in S$ such that $\mathcal{F}_{s}$ is a torsion $\mathcal{O}_{X_{s}}$-Module (resp. a torsion-free
$\mathcal{O}_{X_{s}}$-Module) is locally constructible.*

One may evidently suppose $S = \operatorname{Spec}(A)$ affine and Noetherian and prove that $E$ (resp. $E'$) is then
constructible by using the criterion $(0_{III}, 9.2.3)$; replacing $S$ by the reduced closed sub-prescheme of $S$ having
an irreducible closed part $Y$ of $S$ as underlying space, and noting `(I, 3.6.4)` that for $s \in Y$, the fibre
$(X_{(Y)})_{s}$ identifies canonically with $X_{s}$ and the sheaf $(\mathcal{F} \otimes_{\mathcal{O}_{S}}
\mathcal{O}_{Y})_{s}$ with $\mathcal{F}_{s}$, one sees that one is reduced to the case where $S$ is integral of generic
point $\eta$, and to proving that $E$ or $S - E$ (resp. $E'$ or $S - E'$) is a neighbourhood of $\eta$ in $S$. Note
moreover that $X$ is a finite union of affine open sets $U_{i}$ of finite type over $S$, and each of $(U_{i})_{s}$ is
induced on an open set of $X_{s}$, hence locally integral; in addition, if $(U_{i})_{\eta}$ is empty (resp. non-empty),
one knows that $(U_{i})_{s}$ is also empty (resp. non-empty) in a neighbourhood of $\eta$ `(9.2.6)`. One may therefore
suppose all the $(U_{i})_{\eta}$ non-empty and integral, and to say that $\mathcal{F}_{s}$ is torsion (resp.
torsion-free) is equivalent to saying that each of the $\mathcal{F}_{s}|(U_{i})_{s}$ is torsion (resp. torsion-free).
One is therefore reduced to the case where $X = \operatorname{Spec}(B)$ is affine, and $\mathcal{F} = \tilde{M}$, where
$M$ is a $B$-module of finite type; one sets $B_{s} = B \otimes_{A} k(s)$, $M_{s} = M \otimes_{A} k(s)$, and one may
suppose $B_{\eta}$ integral. We have four cases to envisage.

1° $\eta \in E$; $M_{\eta}$ is then a torsion $B_{\eta}$-module of finite type, and there is consequently $h \neq 0$ in
$B_{\eta}$ such that $hM_{\eta} = 0$; by virtue of `(8.5.2, (i))`, applied following the method

<!-- original page 66 -->

of `(8.1.2, a))`, one may (replacing $S$ if necessary by a neighbourhood of $\eta$) suppose that $h \in \Gamma(X_{\eta},
\mathcal{O}_{X_{\eta}})$ is of the form $g_{\eta}$, where $g \in \Gamma(X, \mathcal{O}_{X})$; let $u : \mathcal{F} \to
\mathcal{F}$ be the endomorphism of $\mathcal{F}$ defined by multiplication by $g$; by hypothesis, one has $u_{\eta} =
0$, hence `(9.4.5)` the endomorphism $u_{s} : \mathcal{F}_{s} \to \mathcal{F}_{s}$, defined by multiplication by
$g_{s}$, is zero in a neighbourhood of $\eta$. On the other hand, let $v : \mathcal{O}_{X} \to \mathcal{O}_{X}$ be the
endomorphism defined by multiplication by $g$; since $B_{\eta}$ is integral and $h = g_{\eta} \neq 0$, $v_{\eta}$ is
injective, and it therefore follows from `(9.4.5)` that $v_{s}$ is an injective endomorphism of $\mathcal{O}_{X_{s}}$
for $s$ close to $\eta$, in other words, $g_{s}$ is an $\mathcal{O}_{X_{s}}$-regular element for these values of $s$;
hence $\mathcal{F}_{s}$ is torsion in a neighbourhood of $\eta$.

2° $\eta \in S - E$. To say that a $B_{\eta}$-module $M_{\eta}$ of finite type is not a torsion module means that its
quotient $M_{\eta}/T$ by its torsion sub-module is $\neq 0$, and since it is a torsion-free $B_{\eta}$-module of finite
type, it is isomorphic to a sub-module of a $B_{\eta}$-module $B^{n}_{\eta}$; there is consequently a homomorphism $w :
M_{\eta} \to B^{n}_{\eta}$ which is $\neq 0$. Applying `(8.5.2, (i))` following the method of `(8.1.2, a))`, one deduces
(replacing $S$ if necessary by a neighbourhood of $\eta$) that there exists a homomorphism $v : \mathcal{F} \to
\mathcal{O}^{n}_{X}$ such that $v_{\eta} = w$. The hypothesis $v_{\eta} \neq 0$ therefore entails `(9.4.5)` that $v_{s}
\neq 0$ in a neighbourhood of $\eta$, and since $X_{s}$ is locally integral, $\mathcal{F}_{s}$ is not torsion for these
values of $s$.

3° $\eta \in E'$. Since $M_{\eta}$ is a torsion-free $B_{\eta}$-module of finite type, there exists an injective
homomorphism $w : M_{\eta} \to B^{n}_{\eta}$. Using `(8.5.2, (i))` and `(9.4.5)` as in 2° (restricting $S$ if
necessary), one deduces that there exists a homomorphism $v : \mathcal{F} \to \mathcal{O}^{n}_{X}$ such that $v_{\eta} =
w$ and that for $s$ close to $\eta$, $v_{s} : \mathcal{F}_{s} \to \mathcal{O}^{n}_{X_{s}}$ is injective; for these
values of $s$, $\mathcal{F}_{s}$ is therefore torsion-free.

4° $\eta \in S - E'$. Let $T$ be the torsion sub-module of $M_{\eta}$; by hypothesis $T \neq 0$, and $T$ is of finite
type since $M_{\eta}$ is Noetherian. Using this time `(8.5.2, (i) and (ii))` one sees (restricting $S$ if necessary)
that there exists a coherent $\mathcal{O}_{X}$-Module $\mathcal{G}$ and an injective homomorphism $u : \mathcal{G} \to
\mathcal{F}$ such that $\mathcal{G}_{\eta} = \tilde{T}$ and $u_{\eta}$ is the canonical injection $\tilde{T} \to
\mathcal{F}_{\eta}$. It then follows from 1° and from `(1.8.6)` that in a neighbourhood of $\eta$, $\mathcal{G}_{s}$ is
a torsion $\mathcal{O}_{X_{s}}$-Module $\neq 0$, and on the other hand it follows from `(9.4.5)` that in a neighbourhood
of $\eta$, $u_{s}$ is injective. One concludes that in a neighbourhood of $\eta$, the torsion sub-Module of
$\mathcal{F}_{s}$ is non-zero. C.Q.F.D.

**Remark (9.4.9).**

<!-- label: IV.9.4.9 -->

The property "$X$ is a locally integral algebraic $k$-prescheme" does not verify condition `(9.2.1, (i))`, and it is
therefore not certain that the statement `(9.4.8)` remains valid when one makes no hypothesis on $S$ and one supposes
only that $f$ is a morphism of finite presentation and $\mathcal{F}$ an $\mathcal{O}_{X}$-Module of finite presentation.
Let us nevertheless consider the following particular case: `S_0` being a locally Noetherian prescheme, let $f_{0} :
X_{0} \to S_{0}$ be a morphism of finite type, such that the fibres $(X_{0})_{s_{0}}$ are locally integral (for every
$s_{0} \in S_{0}$), and $\mathcal{F}_{0}$ a coherent $\mathcal{O}_{X_{0}}$-Module; let $g : S \to S_{0}$ be an arbitrary
morphism, set $X = X_{0} \times_{S_{0}} S$, $\mathcal{F} = \mathcal{F}_{0} \otimes_{\mathcal{O}_{S_{0}}}
\mathcal{O}_{S}$, $f = f_{0} \times 1_{S} : X \to S$, and suppose that for every $s \in S$, the fibre $X_{s}$ is still
locally integral. Then the set $E$ (resp. $E'$) of $s \in S$ such that $\mathcal{F}_{s}$ is torsion (resp. torsion-free)

<!-- original page 67 -->

is still locally constructible. Indeed, let $s \in S$ and let $s_{0} = g(s)$; it will suffice (taking into account
`(1.8.2)`) to prove that, for $\mathcal{F}_{s}$ to be torsion (resp. torsion-free), it is necessary and sufficient that
$(\mathcal{F}_{0})_{s_{0}}$ be so. Now, $Supp(\mathcal{F}_{s})$ is the inverse image of
$Supp((\mathcal{F}_{0})_{s_{0}})$ by the projection $p : X_{s} \to (X_{0})_{s_{0}}$ `(I, 9.1.13)`; since $p$ is
faithfully flat and quasi-compact, to say that $Supp(\mathcal{F}_{s})$ contains a maximal point of $X_{s}$ is equivalent
to saying that $Supp((\mathcal{F}_{0})_{s_{0}})$ contains a maximal point of $(X_{0})_{s_{0}}$ `(1.1.5 and 2.3.4)`;
whence our assertion concerning the set $E$ `(I, 7.4.6)`. If the torsion sub-Module $\mathcal{T}$ of
$(\mathcal{F}_{0})_{s_{0}}$ is non-zero, $\mathcal{T} \otimes_{k(s_{0})} k(s)$ (which is torsion by what precedes) is
non-zero and identifies with a sub-Module of $\mathcal{F}_{s}$ `(2.2.7)`, hence the torsion sub-Module of
$\mathcal{F}_{s}$ is non-zero. Finally, if $(\mathcal{F}_{0})_{s_{0}}$ is torsion-free, one may suppose (by considering
an affine open set of $(X_{0})_{s_{0}}$) that $(\mathcal{F}_{0})_{s_{0}}$ is isomorphic to a sub-Module of a
$\mathcal{O}^{n}_{(X_{0})_{s_{0}}}$, hence $\mathcal{F}_{s}$ is isomorphic to a sub-Module of an
$\mathcal{O}^{n}_{X_{s}}$ `(2.2.7)`, and this establishes our assertion concerning $E'$.

### 9.5. Constructibility of topological properties

**Proposition (9.5.1).**

<!-- label: IV.9.5.1 -->

*Let $f : X \to S$ be a morphism of finite presentation, $Z$ a locally constructible part of $X$. Then the set $E$ of $s
\in S$ such that $Z_{s} \neq \emptyset$ is locally constructible.*

Indeed, one has $E = f(Z)$, and it suffices to apply Chevalley's theorem `(1.8.4)`.

**Corollary (9.5.2).**

<!-- label: IV.9.5.2 -->

*If $Z'$, `Z''` are two locally constructible parts of $X$, the set of $s \in S$ such that $Z'_{s} \subset Z''_{s}$
(resp. $Z'_{s} = Z''_{s}$) is locally constructible.*

Indeed, the relation $Z'_{s} \subset Z''_{s}$ is equivalent to $(Z' \cap (\complement Z''))_{s} = \emptyset$, and $Z'
\cap \complement Z''$ is locally constructible.

**Proposition (9.5.3).**

<!-- label: IV.9.5.3 -->

*Let $f : X \to S$ be a morphism of finite presentation, $Z$, $Z'$ two locally constructible parts of $X$ such that $Z
\subset Z'$. Then the set $E$ of $s \in S$ such that $Z_{s}$ is dense in $Z'_{s}$ is locally constructible in $S$.*

One must verify the two conditions of `(9.2.2, (ii))`. As for the first, consider an algebraic prescheme $X$ over a
field $k$, two constructible parts $Z$, $Z'$ of $X$ such that $Z \subset Z'$, and an extension $k'$ of $k$. Then the
canonical projection $p : X_{(k')} \to X$ is a faithfully flat and quasi-compact morphism, and one therefore has
$p^{-1}(\overline{Z}) = \overline{p^{-1}(Z)}$ and $p^{-1}(\overline{Z}') = \overline{p^{-1}(Z')}$ by virtue of
`(2.3.10)`; since $p$ is surjective, the relation $\overline{Z} = \overline{Z}'$ is equivalent to $\overline{p^{-1}(Z)}
= \overline{p^{-1}(Z')}$.

Let us now verify the second condition, and suppose therefore $S$ affine, Noetherian, and integral, of generic point
$\eta$. Let us distinguish two cases.

1° $\eta \in S - E$, in other words, $Z_{\eta}$ is not dense in $Z'_{\eta}$; there exists therefore in $X$ an open set
$V$ such that $V \cap Z_{\eta} = \emptyset$ and $V \cap Z'_{\eta} \neq \emptyset$. As $X$ is Noetherian, $V$ is locally
constructible, hence so is $V \cap Z$, and by virtue of `(9.5.1)`, there is a neighbourhood $U$ of $\eta$ in $S$ such
that for every $s \in U$, one has $(V \cap Z)_{s} = \emptyset$ and $(V \cap Z')_{s} \neq \emptyset$; this entails that
$Z_{s}$ is not dense in $Z'_{s}$ for $s \in U$, in other words $U \subset S - E$.

<!-- original page 68 -->

2° $\eta \in E$, hence $Z_{\eta}$ is dense in $Z'_{\eta}$. Let us first show that one may suppose $Z'$ closed. Indeed,
$Z_{\eta}$ is dense in $\overline{Z'_{\eta}}$ (closure taken in $X_{\eta}$); set $V_{\eta} = X_{\eta} -
\overline{Z'_{\eta}}$, which is open in $X_{\eta}$ and does not meet $Z_{\eta}$; one may suppose $V_{\eta}$ of the form
$V \cap X_{\eta}$, where $V$ is open (hence constructible) in $X$, and the hypothesis $V_{\eta} \cap Z'_{\eta} =
\emptyset$ then entails $V_{s} \cap Z'_{s} = \emptyset$ for every $s$ close to $\eta$ by virtue of `(9.5.1)`. Replacing
$S$ by an open neighbourhood of $\eta$, one may therefore suppose that $V \cap Z' = \emptyset$, hence $V \cap
\overline{Z}' = \emptyset$ (closure taken in $X$), and consequently $(\overline{Z}')_{\eta} = \overline{Z'_{\eta}}$,
whence our assertion. The set $\overline{Z}'$ is then the union of its irreducible components in finite number, and by
restricting $S$ again to a neighbourhood of $\eta$, one may suppose that all the irreducible components $Z'_{i}$ of
$\overline{Z}'$ meet $X_{\eta}$, whence it follows that $X_{\eta}$ contains the generic points of the $Z'_{i}$ $(0_{I},
2.1.8)$. To say that $Z_{s}$ is dense in $Z'_{s}$ is then equivalent to saying that each of the $(Z \cap Z'_{i})_{s}$ is
dense in $(Z'_{i})_{s}$, and one is thus reduced to the case where $\overline{Z}'$ is irreducible. Replacing then if
necessary $X$ by the reduced sub-prescheme having $\overline{Z}'$ as underlying space, one sees that one may suppose
that $Z' = X$ and that $X$ is integral and dominates $S$. Finally, by covering $X$ by a finite number of affine open
sets $W_{j}$ and replacing $Z$ by $Z \cap W_{j}$, one may suppose that $X = \operatorname{Spec}(A)$, where $A$ is an
integral Noetherian ring. Since $X_{\eta}$ is integral Noetherian and $Z_{\eta}$ is constructible in $X_{\eta}$ and
dense in $X_{\eta}$, $Z_{\eta}$ contains a non-empty open set of $X_{\eta}$ $(0_{III}, 9.2.2)$, which one may suppose of
the form $(D(t))_{\eta}$, where $t$ is an element $\neq 0$ of $A$. Replacing $S$ if necessary by a neighbourhood of
$\eta$, one may moreover, by virtue of the relation $(D(t))_{\eta} \subset Z_{\eta}$, suppose that $D(t) \subset Z$
`(9.5.2)`. Finally, since the homothety of ratio $t$ in $\mathcal{O}_{X}$ is injective, it follows from `(9.4.5)` that
for $s$ close to $\eta$, $t_{s}$ is $\mathcal{O}_{X_{s}}$-regular, hence $(X_{s})_{t_{s}}$ is dense in $X_{s}$, and *a
fortiori* the same is true of $Z_{s}$, which contains $(X_{s})_{t_{s}}$.

**Corollary (9.5.4).**

<!-- label: IV.9.5.4 -->

*Let $f : X \to S$ be a morphism of finite presentation, $Z$ a locally constructible part of $X$. The set $E$ of $s \in
S$ such that $Z_{s}$ is closed (resp. open, resp. locally closed) in $X_{s}$ is locally constructible in $S$.*

To say that $Z_{s}$ is open in $X_{s}$ means that $(X - Z)_{s} = X_{s} - Z_{s}$ is closed in $X_{s}$, and since $X - Z$
is locally constructible, one may restrict to considering the set of $s \in S$ such that $Z_{s}$ is closed and the set
of $s \in S$ such that $Z_{s}$ is locally closed.

Let us verify in each case the two conditions of `(9.2.2, (ii))`. The first results from the fact that $p : X_{(k')} \to
X$ is faithfully flat and quasi-compact, and from `(2.3.12)` and `(2.3.14)`. Let us therefore verify the second
condition, $S$ being supposed affine, Noetherian, and integral, of generic point $\eta$. Set $Z' = \overline{Z}$; the
same reasoning as in `(9.5.3)` shows that $Z'_{\eta}$ is equal to the closure of $Z_{\eta}$ in $X_{\eta}$; by virtue of
`(9.5.3)`, there is therefore a neighbourhood $U$ of $\eta$ such that for $s \in U$, $Z_{s}$ is dense in $Z'_{s}$, the
latter being closed in $X_{s}$. To say that $Z_{s}$ is closed in $X_{s}$ then means that $Z''_{s} = \emptyset$, where
$Z'' = Z' - Z$; it therefore follows from `(9.5.1)` that the set $E$ of $s \in S$ where $Z''_{s} = \emptyset$ is such
that $E$ or $S - E$ contains a neighbourhood of $\eta$. To say that $Z_{s}$ is locally closed in $X_{s}$ means that
$Z''_{s}$ is closed in $X_{s}$; it therefore suffices to apply the preceding result, replacing $Z$ by `Z''`, which is
locally constructible in $X$.

<!-- original page 69 -->

**Proposition (9.5.5).**

<!-- label: IV.9.5.5 -->

*Let $f : X \to S$ be a morphism of finite presentation, $Z$ a locally constructible part of $X$ such that, for every $s
\in S$, $Z_{s}$ is locally closed in $X_{s}$. For every $s \in S$, let $D(s) \subset \mathbb{Z} \cup {-\infty}$ be the
set of dimensions of the irreducible components of $Z_{s}$. Then the function $s \mapsto D(s)$ is locally constructible
in $S$.*

Let $\Phi$ be a finite part of $\mathbb{Z} \cup {-\infty}$; one must show that the set of $s \in S$ such that $D(s) =
\Phi$ is locally constructible; taking account of `(9.2.3)`, we still have to verify the two conditions of
`(9.2.2, (ii))`.

As for the first, one must see that if $X$ is an algebraic prescheme over a field $k$, $Z$ a locally closed part of $X$,
$k'$ an extension of $k$, $p : X_{(k')} \to X$ the canonical projection, then the set of dimensions of the irreducible
components of $Z$ is the same as that of the dimensions of the irreducible components of $p^{-1}(Z)$; taking account of
the existence of a sub-prescheme of $X$ having $Z$ as underlying space `(I, 5.2.1)`, this results from `(4.2.8)`.

For the second condition of `(9.2.2, (ii))`, one is in the case where $S$ is Noetherian and integral of generic point
$\eta$, and $f : X \to S$ is a morphism of finite type, so that $X$ is Noetherian. The sub-space $Z_{\eta}$ of the
Noetherian space $X_{\eta}$ is by hypothesis locally closed, hence has a finite number of irreducible components
$Z_{i\eta}$, which are locally closed in $X_{\eta}$. There exists consequently for each index $i$ a locally closed part
$Z_{i}$ of $X$ such that $(Z_{i})_{\eta} = Z_{i\eta}$, hence if $Z' = \bigcup_{i} Z_{i}$, one has $Z'_{\eta} =
Z_{\eta}$. But since $Z$ and $Z'$ are locally constructible, one may, by replacing $S$ by a neighbourhood of $\eta$,
suppose that $Z' = Z$ `(9.5.1)`. Moreover, for $i \neq j$, $Z_{i\eta} \cap Z_{j\eta}$ is rare and closed in $Z_{i\eta}$;
hence `(9.5.3 and 9.5.4)`, one may suppose again, by restricting $S$, that for $j \neq i$, $(Z_{i})_{s} \cap
(Z_{j})_{s}$ is rare and closed in $(Z_{i})_{s}$. Since $Z_{i}$ is locally closed in $X$, there is a sub-prescheme of
$X$ having $Z_{i}$ as underlying space (still denoted $Z_{i}$), which is of finite type over $S$ `(I, 6.3.5)`. Set
$U_{i} = Z_{i} - \bigcup_{j \neq i}(Z_{i} \cap Z_{j})$, which is open in $Z$ and such that, for every $s \in S$,
$(U_{i})_{s}$ is open everywhere-dense in $(Z_{i})_{s}$; moreover, by construction, the $U_{i}$ are pairwise disjoint.
Since $(Z_{i})_{s}$ is an algebraic $k(s)$-prescheme, the set of dimensions of the irreducible components of $Z_{s} =
\bigcup_{i} (Z_{i})_{s}$ is the same as the set of dimensions of the irreducible components of the union of the
$(U_{i})_{s}$ `(4.1.1.3)`, each of these components being already an irreducible component of one of the $(U_{i})_{s}$.
One may therefore restrict to the case where $Z = U_{i}$; moreover, since $Z_{\eta}$ is then irreducible, there is only
one irreducible component of $\overline{Z}$ meeting $X_{\eta}$ $(0_{I}, 2.1.8)$, and one may evidently, by restricting
$Z$, suppose $Z$ irreducible. One is finally reduced to proving the following particular case of `(9.5.5)`.

**Corollary (9.5.6).**

<!-- label: IV.9.5.6 -->

*Let $S$ be a Noetherian and irreducible prescheme of generic point $\eta$, $X$ an irreducible prescheme, $f : X \to S$
a dominant morphism of finite type. Then there exists a neighbourhood $U$ of $\eta$ in $S$ such that, for every $s \in
U$, all the irreducible components of $X_{s}$ are of dimension $n = \dim(X_{\eta})$.*

One may evidently restrict to the case where $S = \operatorname{Spec}(A)$ is affine, $A$ being therefore Noetherian;
replacing $f$ by $f_{red}$, which is of finite type `(1.5.4, (vi))`, one may

<!-- original page 70 -->

suppose $A$ integral and $X$ reduced, hence integral since it is irreducible. One knows `(4.1.2)` that there exists a
dense open set $W$ in $X_{\eta}$ and a finite surjective $k(\eta)$-morphism $h : W \to \mathbf{V}((k(\eta))^{n}) =
\operatorname{Spec}(B')$, where $B' = k(\eta)[T_{1}, \cdots, T_{n}]$ ($T_{i}$ indeterminates). If $V$ is an open set of
$X$ such that $V \cap X_{\eta} = W$, one knows `(9.5.3)` that for $s$ close to $\eta$ in $S$, $V_{s}$ is a dense open
set in $X_{s}$, and one may consequently `(4.1.1.3)` restrict to the case where $V = X$, $W = X_{\eta}$. Set $B =
A[T_{1}, \cdots, T_{n}]$ and $Y = \operatorname{Spec}(B) = \mathbf{V}^{n}_{A}$, so that $\operatorname{Spec}(B') =
Y_{\eta}$; it follows from `(8.8.2, (i))` and `(8.10.5, (vi) and (x))`, applied following the method of `(8.1.2, a))`,
that by replacing $S$ if necessary by a neighbourhood of $\eta$, one may suppose that $h = g_{\eta}$, where $g : X \to
Y$ is a finite surjective morphism; in other words, one has $X = \operatorname{Spec}(C)$, where $C$ is a finite
$B$-algebra and the homomorphism $B \to C$ corresponding to $g$ is *injective*; since $C$ is an integral ring, $C$ is
therefore a torsion-free $B$-module of finite type, and $C_{\eta} = C \otimes_{A} k(\eta)$ is therefore a torsion-free
module of finite type over $B_{\eta} = B \otimes_{A} k(\eta) = k(\eta)[T_{1}, \cdots, T_{n}]$ (being a module of
fractions whose denominators are in $A - {0} \subset B - {0}$). It therefore follows from `(9.4.8)` that there is a
neighbourhood $U$ of $\eta$ in $S$ such that for $s \in U$, $C_{s} = C \otimes_{A} k(s)$ is a torsion-free module of
finite type over $B_{s} = B \otimes_{A} k(s) = k(s)[T_{1}, \cdots, T_{n}]$, and in particular the homomorphism $g_{s} :
B_{s} \to C_{s}$ is injective. Since no element of $B_{s}$ is a zero-divisor in $C_{s}$, for every minimal prime ideal
$\mathfrak{p}_{i}$ of $C_{s}$ (whose elements are zero-divisors in $C_{s}$), one has necessarily $\mathfrak{p}_{i} \cap
B_{s} = 0$, hence the canonical homomorphism $B_{s} \to C_{s}/\mathfrak{p}_{i}$ is injective. One deduces that for each
irreducible component $Z_{i} = \operatorname{Spec}(C_{s}/\mathfrak{p}_{i})$ of $X_{s}$, the restriction to $Z_{i}$ of
$g_{s}$ is a finite and dominant morphism $Z_{i} \to Y_{s}$, hence surjective `(II, 6.1.10)`. One concludes by `(4.1.2)`
that $\dim(Z_{i}) = n$, which completes the proof.

**Remark (9.5.7).**

<!-- label: IV.9.5.7 -->

One will take care to note that under the hypotheses of `(9.5.6)` it may happen that $X_{s}$ is irreducible for no $s
\neq \eta$ in a neighbourhood of $\eta$; in other words, the property "$X$ is an irreducible algebraic $k$-prescheme" is
not constructible. Take for example $S = \operatorname{Spec}(k[T])$, where $k$ is an algebraically closed field, $T$ an
indeterminate; one therefore has $k(\eta) = K = k(T)$. Let $L$ be a finite separable extension of $K$ of degree `> 1`,
and let $X$ be the integral closure of $S$ in $L$ `(II, 6.3.4)`; one has therefore $X = \operatorname{Spec}(B)$, where
$B$ is the integral closure of `k[T]` in $L$. One knows that $B$ is a Dedekind ring, and that all the maximal ideals of
`k[T]`, except a finite number, are unramified in $B$; since in addition the residue field of every maximal ideal of $B$
is necessarily $k$ (since it is a finite extension of $k$), one sees that for almost all the maximal ideals
$\mathfrak{j}_{s}$ of `k[T]`, $B_{s} = B/\mathfrak{j}_{s} B$ is a direct sum of $[L : K]$ fields isomorphic to $k$, in
other words $X_{s}$ is not irreducible, although $X_{\eta} = \operatorname{Spec}(L)$ is.

The same example shows that the property "$X$ is an integral algebraic $k$-prescheme" is not constructible. Finally, the
same is true of the property "$X$ is a reduced algebraic $k$-prescheme". To see this it suffices to take again $S =
\operatorname{Spec}(k[T])$, where this time $k$ is an algebraically closed field of characteristic $p > 0$, and for $X$
the integral closure of $S$ in $L = K^{1/p}$ (where $K = k(T)$), so that $X = \operatorname{Spec}(B)$ with $B =
k[T^{1/p}]$ ($k$ being perfect); every maximal ideal of `k[T]` is of the form $(T - \alpha)$ with $\alpha \in k$; the
unique ideal of $B$ above the ideal $(T - \alpha)$ is the principal ideal $(T^{1/p} - \alpha^{1/p})$ and it is immediate

<!-- original page 71 -->

that the quotient ring $B/(T - \alpha)B$ consequently admits nilpotent elements; in other words, $X_{s}$ is reduced for
no $s \neq \eta$, while $X_{\eta} = \operatorname{Spec}(L)$ is integral.

We shall see a little further on `(9.7)` that one obtains by contrast constructible properties when one considers the
"geometric" notions corresponding to the notions of irreducible, reduced, or integral prescheme `(4.5 and 4.6)`.

### 9.6. Constructibility of certain properties of morphisms

**Proposition (9.6.1).**

<!-- label: IV.9.6.1 -->

*Let $X$, $Y$ be two $S$-preschemes of finite presentation, $f : X \to Y$ an $S$-morphism. Let $E$ be the set of $s \in
S$ for which $f_{s}$ has one of the following properties: to be:*

*(i) surjective;*

*(ii) dominant;*

*(iii) separated;*

*(iv) proper;*

*(v) radicial;*

*(vi) finite;*

*(vii) quasi-finite;*

*(viii) an immersion;*

*(ix) a closed immersion;*

*(x) an open immersion;*

*(xi) an isomorphism;*

*(xii) a monomorphism.*

*Then $E$ is locally constructible in $S$.*

The assertions of (i), (v) and (vii) are inserted only for the record, having already been established in `(9.3.2)`.

(ii): Note first that $f$ is of finite presentation `(1.6.2, (v))`, hence, by virtue of Chevalley's theorem `(1.8.4)`,
$f(X)$ is locally constructible in $Y$. On the other hand, one has $f_{s}(X_{s}) = (f(X))_{s}$ `(I, 3.6.1)`; the set of
$s$ such that $f_{s}$ is dominant is the set of $s$ such that $(f(X))_{s}$ is dense in $Y_{s}$; the conclusion therefore
results in this case from `(9.5.3)`.

(iii): Since $f : X \to Y$ is of finite presentation, the diagonal immersion $\Delta_{f} : X \to X \times_{Y} X$ is of
finite presentation `(1.6.2, (iv) and (v))`; it follows from `(1.8.4.1)` that $\Delta_{f}(X) = \Delta_{X}$ is a locally
constructible part of $X \times_{Y} X$. To say that $f_{s}$ is separated means (taking into account `(I, 5.3.4)`) that
$(\Delta_{X})_{s}$ is closed in $X_{s} \times_{Y_{s}} X_{s} = (X \times_{Y} X)_{s}$; the conclusion therefore results
here from `(9.5.4)`.

(iv): Let us show that the property "$X$ and $Y$ are algebraic preschemes over a field $k$, and $f : X \to Y$ is a
proper $k$-morphism" is constructible. Condition `(9.2.1, (i))` is verified by virtue of `(2.7.1, (vii))`. One may
therefore restrict to the case where $S$ is affine, Noetherian, and integral, of generic point $\eta$, and one must
prove that $E$ or $S - E$ is a neighbourhood of $\eta$. Suppose first that $\eta \in E$; it follows from
`(8.10.5, (xii))` applied following the method of `(8.1.2, a))` that, by replacing $S$ by a neighbourhood of $\eta$, one
may

<!-- original page 72 -->

suppose that $f$ is itself a proper morphism; one then knows that the same is true of $f_{s}$ for every $s \in S$
`(II, 5.4.2, (iii))`. Suppose on the contrary that $\eta \in S - E$, and let us distinguish two cases.

1° Suppose that $f_{\eta}$ is not separated; then it follows from (iii) that $f_{s}$ is non-separated (and *a fortiori*
not proper) in a neighbourhood of $\eta$.

2° Suppose $f_{\eta}$ separated; $Y$ is a finite union of affine open sets $V_{i}$, and for $f_{s}$ to be proper, it is
necessary and sufficient that each of its restrictions $f^{-1}_{s}((V_{i})_{s}) \to (V_{i})_{s}$ be so `(II, 5.4.1)`;
one may therefore restrict to the case where $Y$ is affine, hence a scheme. To say that $f_{\eta}$ is not proper means
`(II, 5.6.3)` that there exists a morphism of finite type $h : Z \to Y_{\eta}$ such that the morphism
$(f_{\eta})_{(Z)} : X_{\eta} \times_{Y_{\eta}} Z \to Z$ is not closed. As $Y$ is a scheme, one deduces from
`(8.8.2, (i) and (ii))` (by restricting $S$ if necessary to a neighbourhood of $\eta$) that there exists a morphism of
finite type $g : Y' \to Y$ such that $Z$ is isomorphic to $Y'_{\eta}$ and $g_{\eta} = h$; if one sets
$X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, one has $(f_{\eta})_{(Z)} = f'_{\eta}$, and by hypothesis there
exists therefore a closed part $M'$ of $X'_{\eta}$ such that $f'_{\eta}(M')$ is not closed in $Y'_{\eta}$. Now $M'$ is
the trace on $X'_{\eta}$ of a closed part $N'$ of $X'$; since $X'$ is Noetherian and $f'$ of finite type, `f'(N')` is
constructible in $Y'$ `(1.8.4)`, and by hypothesis $(f'(N'))_{\eta} = f'_{\eta}(N'_{\eta}) = f'_{\eta}(M')$ is not
closed in $Y'_{\eta}$. One then concludes from `(9.5.4)` that there exists a neighbourhood $U$ of $\eta$ in $S$ such
that for $s \in U$, $(f'(N'))_{s} = f'_{s}(N'_{s})$ is not closed in $Y'_{s}$; in other words, the morphism $f'_{s}$ is
not closed, and *a fortiori* the morphism $f_{s}$ is not proper.

(vi): The property is the conjunction of properties (iv) and (vii) `(8.11.1)`, hence the proposition results in this
case from what has already been proved.

(ix): The verification of condition `(9.2.1, (i))` results from `(2.7.1, (xi))`. One may therefore restrict to the case
where $S$ is affine, Noetherian, and integral of generic point $\eta$, and to proving that $E$ or $S - E$ is a
neighbourhood of $\eta$. If $\eta \in E$, one may (by replacing $S$ by a neighbourhood of $\eta$) suppose that $f$ is a
closed immersion by virtue of `(8.10.5, (iv))`, and then it is clear that $f_{s}$ is a closed immersion for every $s \in
S$ `(I, 4.3.2)`. Suppose therefore that $\eta \in S - E$ and let us distinguish two cases.

1° $f_{\eta}$ is not a finite morphism. Then it follows from (vi) that in a neighbourhood of $\eta$, $f_{s}$ is not
finite, nor *a fortiori* a closed immersion.

2° $f_{\eta}$ is finite; then, by virtue of `(8.10.5, (x))`, one may suppose (by restricting $S$ if necessary) that $f$
itself is a finite morphism. In this case $\mathcal{A} = \mathcal{A}(X) = f_{*}(\mathcal{O}_{X})$ is a coherent
$\mathcal{O}_{Y}$-Module `(II, 6.1.3)` and $f = \mathcal{A}(u)$, where $u : \mathcal{O}_{Y} \to \mathcal{A}$ is a
homomorphism of $\mathcal{O}_{Y}$-Algebras `(II, 1.1.2)`; since $f_{\eta}$ is not a closed immersion by hypothesis,
$u_{\eta}$ is not surjective `(II, 1.4.10)`, hence `(9.4.5)` there is a neighbourhood of $\eta$ in which $u_{s}$ is not
surjective, and consequently `(I, 4.2.3)` $f_{s}$ is not a closed immersion.

(viii): The verification of condition `(9.2.1, (i))` is done as in (ix), this time using `(2.7.1, (x))` and the fact
that every immersion of a Noetherian prescheme into another is quasi-compact. One is therefore reduced to the case where
$S$ is affine, Noetherian, and integral of generic point $\eta$, and to proving that $E$ or $S - E$ is a neighbourhood
of $\eta$. If $\eta \in E$, one concludes as in (ix) by means of `(8.10.5, (ii))`. If $\eta \in S - E$, one
distinguishes once again two cases.

<!-- original page 73 -->

1° $f_{\eta}(X_{\eta})$ is not a locally closed part of $Y_{\eta}$. As $f(X)$ is constructible in $Y$ `(1.8.4)` and
$f_{s}(X_{s}) = (f(X))_{s}$, one deduces from `(9.5.4)` that for $s$ close to $\eta$, $f_{s}(X_{s})$ is not locally
closed in $Y_{s}$, and *a fortiori* $f_{s}$ is not an immersion.

2° $f_{\eta}(X_{\eta})$ is locally closed in $Y_{\eta}$. As $f(X)$ is constructible in $Y$ `(1.8.4)`, and the same is
true of $\overline{f(X)}$ since $Y$ is Noetherian, it follows from `(8.3.11)` that by restricting $S$ if necessary, one
may suppose that $f(X)$ is locally closed in $Y$. There is then an open set $V$ of $Y$ containing $f(X)$ and in which
$f(X)$ is closed. Since $Y$ is Noetherian, $V$ is of finite type over $S$, and by replacing $Y$ by $V$, one may
therefore reduce to the case where $f(X)$ is closed in $Y$. But then $f_{s}(X_{s}) = (f(X))_{s}$ is closed in $Y_{s}$
for every $s \in S$, and to say that $f_{s}$ is an immersion is equivalent to saying that $f_{s}$ is a closed immersion;
one is therefore reduced to what was proved in (ix).

(x): Using this time `(2.7.1, (ix))` and `(8.10.5, (iii))`, one is reduced to the case where $S$ is affine, Noetherian,
integral of generic point $\eta$, and where $\eta \in S - E$. Let us distinguish three cases.

1° $f_{\eta}(X_{\eta})$ is not open in $Y_{\eta}$. As $f(X)$ is constructible in $Y$ `(1.8.4)`, one deduces from
`(9.5.4)` that $f_{s}(X_{s})$ is not open in $Y_{s}$ for $s$ close to $\eta$, and *a fortiori* $f_{s}$ is not an open
immersion.

2° $f_{\eta}(X_{\eta})$ is open in $Y_{\eta}$ but $f_{\eta}$ is not an immersion. It then follows from (viii) that for
$s$ close to $\eta$ in $S$, $f_{s}$ is not an immersion, nor *a fortiori* an open immersion.

3° $f_{\eta}(X_{\eta})$ is open in $Y_{\eta}$ and $f_{\eta}$ is an immersion. As $f(X)$ is constructible in $Y$, it
follows from `(8.3.11)` that by restricting $S$ if necessary, one may already suppose that $f(X)$ is open in $Y$. Since
$Y$ is Noetherian, the sub-prescheme induced on $f(X)$ is of finite type over $S$, so one may reduce to the case where
$f$ is *surjective* by replacing $Y$ by $f(X)$. By hypothesis, $f_{\eta}$ is a closed immersion, hence one may, as in
(ix), suppose that $f$ is a closed immersion, and consequently that $X$ is a closed sub-prescheme of $Y$ defined by a
coherent Ideal $\mathcal{J}$ of $\mathcal{O}_{Y}$. By hypothesis $f_{\eta}$ is not an isomorphism, hence
$\mathcal{J}_{\eta} \neq 0$; one concludes `(9.4.5)` that in a neighbourhood of $\eta$, one has $\mathcal{J}_{s} \neq
0$, and consequently the surjective closed immersion $f_{s}$ is not open.

(xi): The property is the conjunction of properties (i) and (x) and therefore results from what has been proved.

(xii): By virtue of `(I, 5.3.8)`, to say that $f_{s}$ is a monomorphism means that $\Delta_{f_{s}} = (\Delta_{f})_{s} :
X_{s} \to X_{s} \times_{Y_{s}} X_{s} = (X \times_{Y} X)_{s}$ is an isomorphism, and since $X \times_{Y} X$ is an
$S$-prescheme of finite presentation `(1.6.2, (iv))`, the conclusion results from (xi).

**Proposition (9.6.2).**

<!-- label: IV.9.6.2 -->

*Let $X$, $Y$ be two $S$-preschemes of finite presentation, $f : X \to Y$ an $S$-morphism.*

*I) Let $E$ be the set of $s \in S$ for which $f_{s}$ has one of the following properties: to be:*

*(i) affine;*

*(ii) quasi-affine;*

*(iii) projective;*

*(iv) quasi-projective.*

*Then $E$ is ind-constructible in $S$.*

<!-- original page 74 -->

*II) Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module. Then the set $E'$ of $s \in S$ such that
$\mathcal{L}_{s}$ is an ample (resp. very ample) $\mathcal{O}_{X_{s}}$-Module relative to $f_{s}$ is ind-constructible
in $S$.*

I) Let us verify conditions (i) and (ii) of `(9.2.1)`. As regards condition `(9.2.1, (i))`, it results, for properties
(i) and (ii), from `(2.7.1, (xiii) and (xiv))`; for properties (iii) and (iv), it results from `(9.1.5)`. Let us then
verify condition `(9.2.1, (ii))`, supposing therefore $S$ Noetherian, integral and of generic point $\eta$, and that
$f_{\eta} : X_{\eta} \to Y_{\eta}$ has one of the properties (i) to (iv) of the statement. Applying
`(8.10.5, (viii), (ix), (xiii) and (xiv))` following the method of `(8.1.2, a))`, one sees first that there exists an
open neighbourhood $U$ of $\eta$ such that, if $V$ and $W$ are the inverse images of $U$ in $X$ and $Y$ respectively by
the structure morphisms, the restriction $V \to W$ of $f$ has that one of the properties (i) to (iv) that one considers.
The conclusion then results from the fact that these properties are all stable under base change.

II) One proceeds in the same way. Condition `(9.2.1, (i))` results this time from `(2.7.2)`. For condition
`(9.2.1, (ii))`, with the same notation as in I), it follows from `(8.10.5.2)` that for a neighbourhood $U$ of $\eta$ in
$S$, the restriction $\mathcal{L}|V$ is ample (resp. very ample) relative to the restriction $V \to W$ of $f$. The
conclusion results again from the stability of the properties considered under base change `(II, 4.6.13 and 4.4.10)`.

One may improve `(9.6.2, II))` under certain conditions.

**Proposition (9.6.3).**

<!-- label: IV.9.6.3 -->

*Let $X$, $Y$ be two $S$-preschemes of finite presentation, $f : X \to Y$ a *proper* $S$-morphism, $\mathcal{L}$ an
invertible $\mathcal{O}_{X}$-Module. Then the set $E$ (resp. $E'$) of $s \in S$ such that $\mathcal{L}_{s}$ is an ample
(resp. very ample) $\mathcal{O}_{X_{s}}$-Module relative to $f_{s} : X_{s} \to Y_{s}$ is locally constructible in $S$.*

Let $k$ be a field, $Z$, $T$ two algebraic preschemes over $k$, $\mathcal{M}$ an invertible $\mathcal{O}_{Z}$-Module,
$g : Z \to T$ a $k$-morphism of finite type; then, if $P(Z, T, \mathcal{M}, g, k)$ denotes the relation "$\mathcal{M}$
is ample (resp. very ample) relative to $g$", one has already remarked in `(9.6.2)` that $P(Z, T, \mathcal{M}, g, k)$
satisfies condition `(9.2.1, (i))` by virtue of `(2.7.2)`. One already knows on the other hand that $E$ and $E'$ are
ind-constructible. It remains therefore to see that if $S$ is Noetherian, integral, of generic point $\eta$ and if
$\eta \in S - E$ (resp. $\eta \in S - E'$), then $S - E$ (resp. $S - E'$) contains a neighbourhood of $\eta$. We shall
consider separately the case of $E'$ and that of $E$.

I) **Case of $E'$.** Note that since $f$ is separated and $Y$ quasi-compact, there exists an integer $h$ such that for
$q > h$, one has $R^{q} f_{*}(\mathcal{L}) = 0$ `(III, 1.4.12)`; on the other hand, since $f$ is proper and $Y$
Noetherian, the $R^{q} f_{*}(\mathcal{L})$ are all coherent $\mathcal{O}_{Y}$-Modules `(III, 3.2.1)`; since they are
zero except for a finite number of values of $q$, the generic flatness theorem `(6.9.1)` shows that by restricting $S$
to a neighbourhood of $\eta$, one may suppose that $\mathcal{L}$ and the $R^{q} f_{*}(\mathcal{L})$ are all $S$-flat.
One then concludes from `(III, 6.9.9)` that the canonical homomorphism

```text
  (9.6.3.1)        f_*(ℒ) ⊗_{𝒪_S} k(s) → (f_s)_*(ℒ_s)
```

*is an isomorphism*.

<!-- original page 75 -->

This being so, it follows from `(II, 4.4.4)` that to say $\mathcal{L}_{s}$ is not very ample relative to $f_{s}$ means:
either the canonical homomorphism $(f_{s})*((f_{s})_{*}(\mathcal{L}_{s})) \to \mathcal{L}_{s}$ is not surjective; or the
preceding homomorphism is surjective and the canonical morphism $r : X_{s} \to \mathbf{P}((f_{s})_{*}(\mathcal{L}_{s}))$
is not an immersion. Taking into account the isomorphism `(9.6.3.1)`, these conditions are written respectively in the
form: 1° the canonical homomorphism $(f*(f_{*}(\mathcal{L})))_{s} \to \mathcal{L}_{s}$ is not surjective; 2° the
preceding homomorphism is surjective and the canonical morphism $X_{s} \to \mathbf{P}((f_{*}(\mathcal{L}))_{s})$ is not
an immersion.

Suppose first that the canonical homomorphism $(f*(f_{*}(\mathcal{L})))_{\eta} \to \mathcal{L}_{\eta}$ is not
surjective. Since $f_{*}(\mathcal{L})$ is coherent, the same is true of $f*(f_{*}(\mathcal{L}))$, and then it follows
from `(9.4.5)` that for every $s$ in a neighbourhood of $\eta$, the homomorphism $(f*(f_{*}(\mathcal{L})))_{s} \to
\mathcal{L}_{s}$ is not surjective, which proves in this case that $S - E'$ is a neighbourhood of $\eta$.

Suppose secondly that the canonical homomorphism $(f*(f_{*}(\mathcal{L})))_{\eta} \to \mathcal{L}_{\eta}$ is surjective
but that the morphism $X_{\eta} \to \mathbf{P}((f_{*}(\mathcal{L}))_{\eta})$ is not an immersion. Then the same
reasoning as above shows first that for every $s$ sufficiently close to $\eta$, the homomorphism
$(f*(f_{*}(\mathcal{L})))_{s} \to \mathcal{L}_{s}$ is surjective; on the other hand, by virtue of `(9.6.1, (viii))`, for
$s$ sufficiently close to $\eta$, the morphism $X_{s} \to \mathbf{P}((f_{*}(\mathcal{L}))_{s})$ is not an immersion.
This completes the proof in the case of $E'$.

II) **Case of $E$.** Let us first consider the particular case where $Y = S$.

**Corollary (9.6.4).**

<!-- label: IV.9.6.4 -->

*Let $f : X \to S$ be a proper morphism of finite presentation, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-Module.
Then the set $E$ of $s \in S$ such that $\mathcal{L}_{s}$ is ample (relative to $f_{s}$) is open in $S$, and
$\mathcal{L}|f^{-1}(E)$ is ample relative to the restriction $f^{-1}(E) \to E$ of $f$.*

Since condition `(9.2.1, (i))` is verified by the property $P$ defined above, the result of `(9.2.2, (iv))` and the
reasoning of `(9.2.3)` show that one may restrict to the case where $S$ is Noetherian; but then the result follows from
`(III, 4.7.1)` and from the stability of ampleness under base change `(II, 4.6.13)`.

**Corollary (9.6.5).**

<!-- label: IV.9.6.5 -->

*Under the hypotheses of `(9.6.4)`, in order that $\mathcal{L}$ be ample relative to $f$, it is necessary and sufficient
that, for every $s \in S$, $\mathcal{L}_{s}$ be ample relative to $f_{s}$.*

**(9.6.6) End of the proof of `(9.6.3)`.**

<!-- label: IV.9.6.6 -->

Let us return to the general case, $S$ being Noetherian, integral and of generic point $\eta \in S - E$. Since $f$ is
proper, it follows from `(9.6.4)` that the set $V$ of $y \in Y$ such that $\mathcal{L}_{y}$ is an ample
$\mathcal{O}_{X_{y}}$-Module, relative to the morphism $f_{y} : X_{y} \to \operatorname{Spec}(k(y))$, is open, hence $F
= Y - V$ is closed in $Y$. This being so, since $f_{s}$ is proper and that, for every $y \in Y$ above $s \in S$, one has
$\mathcal{L}_{y} = (\mathcal{L}_{s})_{y}$, it follows from `(9.6.5)` that for $s$ to belong to $S - E$, it is necessary
and sufficient that one have $F_{s} \neq \emptyset$. But since $F$ is closed in $Y$ and $F_{\eta} \neq \emptyset$, it
follows from `(9.5.1)` that the set of $s \in S$ such that $F_{s} \neq \emptyset$ is a neighbourhood of $\eta$ in $S$.
C.Q.F.D.

**Remarks (9.6.7).**

<!-- label: IV.9.6.7 -->

(i) For each of the properties $P$ considered in `(9.6.1)`, proposition `(9.3.3)` is applicable, and these properties
(for the morphisms $f_{s}$) are therefore "stable" under passage from an essentially affine projective limit `(8.13.4)`
of preschemes $X_{\lambda}$ to a suitable one of them.

(ii) Let $Z$ be a locally constructible part of $X$ such that, for every $s \in S$, $Z \cap X_{s}$ is open in $X_{s}$,
and denote by $Z_{s}$ the sub-prescheme of $X_{s}$ induced on the open set $Z \cap X_{s}$.

<!-- original page 76 -->

Then, in propositions `(9.6.1)` and `(9.6.2, (I))`, one may everywhere replace $f_{s}$ by its restriction $f_{s}|Z_{s} :
Z_{s} \to Y_{s}$ without changing the conclusions. Indeed, the verification of `(9.2.1, (i))` is done as in `(9.6.1)`
and `(9.6.2)`. On the other hand, in the reduction to the case where $S$ is Noetherian, done in `(9.2.3)`, if $Z =
q^{-1}(Z_{0})$, where $q : X \to X_{0}$ is the canonical projection and `Z_0` a constructible part of `X_0` `(8.3.11)`,
the fact that $(Z_{0})_{s_{0}}$ is open in $(X_{0})_{s_{0}}$, for $s_{0} = p(s)$, follows from `(2.4.10)` and from the
fact that the projection $X_{s} \to (X_{0})_{s_{0}}$ is surjective. One is therefore reduced to verifying
`(9.2.1, (ii))` under the new hypotheses. Now, since $Z_{\eta}$ is open in $X_{\eta}$, there exists an open set $Z'
\subset X$ such that $Z_{\eta} = Z' \cap X_{\eta}$; as $X$ is then Noetherian, $Z'$ is constructible, and the same is
true of $Z$ by hypothesis; one therefore concludes from `(9.5.2)` and $(0_{III}, 9.2.2)$ that there is a neighbourhood
$U$ of $\eta$ in $S$ such that $Z_{s} = Z'_{s}$ for $s \in U$. Replacing $S$ by $U$, one may therefore restrict to the
case where $Z$ is open in $X$, and then one is reduced to what was proved in `(9.6.1)` and `(9.6.2)`.

<!-- original page 76 -->

### 9.7. Constructibility of separability, geometric irreducibility, and geometric connectedness

**Lemma (9.7.1).**

<!-- label: IV.9.7.1 -->

*Let $S$ be an irreducible prescheme with generic point $\eta$, and $f : X \to S$ a morphism of finite presentation. If
$X_{\eta}$ has $n$ irreducible components (resp. $n'$ connected components), there exists an open neighbourhood $U$ of
$\eta$ in $S$ such that for every $s \in U$, $X_{s}$ has at least $n$ irreducible components (resp. $n'$ connected
components).*

One may restrict to the case where $S$ is affine, so that $X$ is quasi-compact and quasi-separated.

Let $V_{i}$ ($1 \leq i \leq n$) be the interiors of the irreducible components of $X_{\eta}$; they are pairwise
disjoint, quasi- compact, and their union is dense in $X_{\eta}$. By virtue of `(8.2.11)`, applied via the method of
`(8.1.2, a))`, there exists for each $i$ a quasi-compact open $W_{i}$ in $X$ such that $W_{i} \cap X_{\eta} = V_{i}$;
since $X$ is quasi-separated, the intersections $W_{i} \cap W_{j}$ are quasi-compact `(1.2.7)`, hence, replacing $S$ by
a neighbourhood of $\eta$, we may suppose $W_{i} \cap W_{j} = \emptyset$ for $i \neq j$ by `(8.3.3)`. Moreover, since
the $W_{i}$ are constructible, there is a neighbourhood $U$ of $\eta$ in $S$ such that for every $s \in U$ the
$(W_{i})_{s}$ are non-empty `((9.5.1)` and `(9.2.3))` and such that the union of the $(W_{i})_{s}$ is dense in $X_{s}$
`((9.5.3)` and `(9.2.3))`. This being so, the (finitely many) irreducible components of the $(W_{i})_{s}$ are also the
irreducible components of the union of the $(W_{i})_{s}$ $(0_{I}, 2.1.7)$, so the closures in $X_{s}$ of these
components are the irreducible components of $X_{s}$ $(0_{I}, 2.1.6)$ and their number is evidently $\geq n$.

Now let $C_{j}$ ($1 \leq j \leq n'$) be the connected components of $X_{\eta}$; these are pairwise disjoint
quasi-compact open subsets of $X_{\eta}$. If one replaces the $V_{i}$ by the $C_{j}$ in the preceding reasoning, one
sees (using `(8.3.3)` twice) that one may suppose $X$ is the union of $n'$ pairwise disjoint quasi-compact opens $M_{j}$
($1 \leq j \leq n'$) and that, in a neighbourhood of $\eta$, the $(M_{j})_{s}$ are non-empty. Since the union of the
$(M_{j})_{s}$ is $X_{s}$, the connected components of the $(M_{j})_{s}$ are the connected components of $X_{s}$, so
their number is $\geq n'$.

<!-- original page 77 -->

**Lemma (9.7.2).**

<!-- label: IV.9.7.2 -->

*Let $S$ be an irreducible prescheme with generic point $\eta$, and $f : X \to S$ a morphism of finite presentation. If
$X_{\eta}$ is not reduced, there exists an open neighbourhood $U$ of $\eta$ in $S$ such that, for every $s \in U$,
$X_{s}$ is not reduced.*

Indeed, let $\mathcal{N}$ be the Nilradical of $\mathcal{O}_{X}$; it follows from `(8.2.13)`, applied via the method of
`(8.1.2, a))`, that $\mathcal{N}_{\eta}$ is the nilradical of $\mathcal{O}_{X_{\eta}}$, and the hypothesis is that
$\mathcal{N}_{\eta} \neq 0$. One concludes from `(9.4.5)` and `(9.2.3)` that there is a neighbourhood $U$ of $\eta$ such
that, for every $s \in U$, $\mathcal{N}_{s}$ is identified with an Ideal of $\mathcal{O}_{X_{s}}$ and $\mathcal{N}_{s}
\neq 0$; since $\mathcal{N}_{s}$ is evidently contained in the Nilradical of $\mathcal{O}_{X_{s}}$, one sees that
$X_{s}$ is not reduced for $s \in U$.

**(9.7.3)**

<!-- label: IV.9.7.3 -->

Given a polynomial $F \in A[T_{1}, \cdots, T_{n}]$, where $A$ is a ring and the $T_{i}$ are indeterminates, for every
ring homomorphism $\rho : A \to B$, we denote by $F^{\rho}$ or $F^{B}$ the polynomial of $B[T_{1}, \cdots, T_{n}]$
obtained by replacing each coefficient of $F$ by its image under $\rho$. If $k$ is a field, $F \in k[T_{1}, \cdots,
T_{n}]$ a non-constant polynomial, and $X = \operatorname{Spec}(k[T_{1}, \cdots, T_{n}]/(F))$, to say that $X$ is
integral (or that the ideal `(F)` is prime) means that $F$ is irreducible (that is, in every factorization $F = F_{1}
F_{2}$ into polynomials of $k[T_{1}, \cdots, T_{n}]$, `F_1` or `F_2` is of degree `0`); this follows from the fact that
the ring $k[T_{1}, \cdots, T_{n}]$ is factorial. From this one deduces immediately (`(4.6.2)` and `(4.5.2)`):

**Lemma (9.7.4).**

<!-- label: IV.9.7.4 -->

*Let $k$ be a field, $\Omega$ an algebraically closed extension of $k$, $F$ a non-constant polynomial of $k[T_{1},
\cdots, T_{n}]$. The following conditions are equivalent:*

*a) $X = \operatorname{Spec}(k[T_{1}, \cdots, T_{n}]/(F))$ is geometrically integral.*

*b) $F^{K}$ is irreducible for every extension $K$ of $k$.*

*c) $F^{\Omega}$ is irreducible.*

In this case we shall say that $F$ is **geometrically irreducible**.

**Lemma (9.7.5).**

<!-- label: IV.9.7.5 -->

*Let $A$ be an integral ring, $K$ its field of fractions, $F$ a non-constant polynomial of $A[T_{1}, \cdots, T_{n}]$ of
degree $d$ such that $F^{K}$ is geometrically irreducible. Then there exists $f \neq 0$ in $A$ such that for every $x
\in D(f)$, $F^{k(x)}$ is geometrically irreducible.*

Write $F = \sum_{\alpha} c_{\alpha} T^{\alpha}$ as usual, with $\alpha = (\alpha_{1}, \cdots, \alpha_{n})$, $T^{\alpha}
= T^{\alpha_{1}}_{1} T^{\alpha_{2}}_{2} \cdots T^{\alpha_{n}}_{n}$, $|\alpha| = \alpha_{1} + \alpha_{2} + \cdots +
\alpha_{n} \leq d$ (at least one of the $c_{\alpha}$ with $|\alpha| = d$ being non-zero). Since the non-zero
$c_{\alpha}$ are invertible in $K$, we may suppose, by replacing $A$ if necessary with a ring $A_{g}$ ($g \neq 0$ in
$A$), that the non-zero $c_{\alpha}$ are invertible in $A$. It follows that for every $x \in \operatorname{Spec}(A)$,
$F^{k(x)}$ is of degree $d$.

We first prove a preliminary lemma.

**Lemma (9.7.5.1).**

<!-- label: IV.9.7.5.1 -->

*Let $A$ be an integral ring, $S = \operatorname{Spec}(A)$, $\eta$ the generic point of $S$, $B$ the polynomial ring
$A[T_{1}, \cdots, T_{m}]$, $(P_{i})_{i \in I}$ a finite family of elements of $B$, and $\mathfrak{a}$ the ideal of $B$
generated by the $P_{i}$. For every $s \in S$, let $\mathfrak{a}_{s}$ be the ideal of $k(s)[T_{1}, \cdots, T_{m}]$
generated by the polynomials $(P_{i})^{k(s)}$ ($i \in I$). Then, if $V(\mathfrak{a}_{\eta}) = \emptyset$, there exists a
neighbourhood $U$ of $\eta$ in $S$ such that $V(\mathfrak{a}_{s}) = \emptyset$ for every $s \in U$.*

Indeed, let $Y = \operatorname{Spec}(B)$, and let $Z$ be the closed part $V(\mathfrak{a})$ of $Y$; since $\mathfrak{a}$
is a finitely generated ideal, $Z$ is constructible in $Y$ $(0_{III}, 9.1.5)$, and with the notations introduced in
`(9.4.1)`, one has $V(\mathfrak{a}_{s}) = Z_{s}$ for every $s \in S$; since the structure morphism $Y \to S$ is of
finite presentation, the conclusion of the lemma follows from `(9.5.1)` and `(9.2.3)`.

<!-- original page 78 -->

Let $(p, q)$ be a pair of integers `> 0` with $p + q = d$; introduce indeterminates $T'_{\beta}$, $T''_{\gamma}$ for all
systems of integers $\beta$, $\gamma$ with $|\beta| \leq p$ and $|\gamma| \leq q$; for every system of integers $\alpha$
with $|\alpha| \leq d$, consider the polynomial of $B = A[T'_{\beta}, T''_{\gamma}]_{|\beta| \leq p, |\gamma| \leq q}$:

```text
                P_α(T'_β, T''_γ) = ∑_{β + γ = α} T'_β T''_γ − c_α.
```

Let $\Omega$ be an algebraic closure of $K$; to say that there exist two polynomials `F_1`, `F_2` of $\Omega[T_{1},
\cdots, T_{n}]$, of respective degrees $p$ and $q$, such that $F_{1} F_{2} = F^{\Omega}$, is to say that the system of
equations $P_{\alpha}(\xi, \zeta) = 0$ ($|\alpha| \leq d$) admits a solution $(\xi, \zeta)$ ($|\beta| \leq p$, $|\gamma|
\leq q$) formed of elements of $\Omega$. Let $\mathfrak{a}$ be the ideal of $B$ generated by the $P_{\alpha}$; the
preceding interpretation, and Hilbert's Nullstellensatz, show that the hypothesis on $F^{K}$ implies that
$V(\mathfrak{a}_{\eta}) = \emptyset$, where $\eta$ denotes the generic point of $\operatorname{Spec}(A)$; lemma
`(9.7.5.1)` therefore proves that in a neighbourhood of $\eta$, one has $V(\mathfrak{a}_{s}) = \emptyset$, and
consequently, for these values of $x$, $F^{k(x)}$ admits no factorization $F^{k(x)} = G_{1} G_{2}$ where `G_1`, `G_2`
are polynomials of respective degrees $p$ and $q$ whose coefficients lie in an algebraic closure of $k(x)$. It suffices
to apply this result to all pairs of integers $(p, q)$ with $p > 0$, $q > 0$, and $p + q = d$ to obtain the conclusion
of lemma `(9.7.5)`.

**Proposition (9.7.6).**

<!-- label: IV.9.7.6 -->

*Let $S$ be an integral Noetherian prescheme with generic point $\eta$, $f : X \to S$ a morphism of finite type,
$\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. If $\mathcal{F}_{\eta}$ has no embedded associated prime cycle, there
exists a neighbourhood $U$ of $\eta$ in $S$ such that, for every $s \in U$, $\mathcal{F}_{s}$ has no embedded associated
prime cycle.*

Since $X_{\eta}$ is Noetherian, there exists an injective homomorphism $v : \mathcal{F}_{\eta} \to \oplus^{m}_{i=1}
\mathcal{G}_{i}$, where each $\mathcal{G}_{i}$ is irredundant and $Ass(\mathcal{G}_{i})$ is the set of $x_{i}$, where
${x_{i}} = Ass(\mathcal{F}_{\eta})$ `(3.2.6)`; if $Z_{i}$ is the closure of ${x_{i}}$ in $X_{\eta}$, one has $Z_{i} =
Supp(\mathcal{G}_{i})$ `(3.1.4)`, and by hypothesis the $Z_{i}$ are the irreducible components of $Z =
Supp(\mathcal{F}_{\eta})$. It follows from `(8.5.2, (i)` and `(ii))` (by restricting $S$ if necessary to a neighbourhood
of $\eta$) and `(8.5.8)` that there exist coherent $\mathcal{O}_{X}$-Modules $\mathcal{H}_{i}$ and an injective
homomorphism $u : \mathcal{F} \to \oplus^{m}_{i=1} \mathcal{H}_{i}$ such that $(\mathcal{H}_{i})_{\eta} =
\mathcal{G}_{i}$ for every $i$ and $v = u_{\eta}$. If $Y_{i} = Supp(\mathcal{H}_{i})$, one has $(Y_{i})_{s} =
Supp((\mathcal{H}_{i})_{s})$ for every $s \in S$ `(I, 9.1.13)`, and in particular $(Y_{i})_{\eta} = Z_{i}$ for every
$i$. The hypothesis implies that for $i \neq j$, $Z_{i} - (Z_{i} \cap Z_{j})$ is dense open in $Z_{i}$; one therefore
deduces from `(9.5.3)` and `(9.5.4)` that in a neighbourhood of $\eta$, $(Y_{i})_{s} - ((Y_{i})_{s} \cap (Y_{j})_{s})$
is open and dense in $(Y_{i})_{s}$. Suppose that we have proved that each $(\mathcal{H}_{i})_{s}$ has no embedded
associated prime cycle for $s \in U$. Then the elements of $Ass((\mathcal{H}_{i})_{s})$ are the maximal points of
$(Y_{i})_{s}$; none of them can therefore belong to a $(Y_{j})_{s}$ for $i \neq j$, and the proposition will be proved.
We may therefore suppose that $\mathcal{F}$ is irredundant; moreover, we may restrict to the case where $S =
\operatorname{Spec}(A)$ is affine; $X$ is then a union of finitely many affine opens $V_{j}$, and if $V_{j} \cap
Supp(\mathcal{F}_{\eta}) = \emptyset$, one will also have $V_{j} \cap Supp(\mathcal{F}_{s}) = \emptyset$ for $s$ near
$\eta$ `(9.5.1)`, so we may restrict to the case where $X = \operatorname{Spec}(B)$ is also affine and where the
morphism $f : X \to S$ is dominant; $A$ is therefore an integral Noetherian ring, a subring of a finitely generated
$A$-algebra $B$, and $\mathcal{F} = \tilde{M}$, where $M$ is a finitely generated $B$-module; by hypothesis, if $K$ is
the field of fractions of $A$, the $B^{K}$-module $M^{K}$ is irredundant. Let $\mathfrak{q}$ be the unique

<!-- original page 79 -->

element of $Ass(M^{K})$, and let $\mathfrak{p}$ be the prime ideal of $B$ inverse image of $\mathfrak{q}$ under the
canonical map $B \to B^{K}$. We know `(5.11.1.1)` that there exists a finite filtration $(N_{h})_{0 \leq h \leq m}$ of
$M^{K}$ such that $N_{0} = M^{K}$, $N_{m} = 0$, and $N_{h}/N_{h+1}$ is isomorphic to a non-zero sub-$B^{K}$-module of
$B^{K}/\mathfrak{q}$. Let $M_{h}$ be the inverse image of $N_{h}$ under the canonical map $M \to M^{K}$. It follows from
`(9.4.4)` that for $s$ sufficiently close to $\eta$, $(M_{h})^{k(s)}$ is identified with a sub-$B^{k(s)}$-module of
$M^{k(s)}$, and the quotient $(M_{h})^{k(s)}/(M_{h+1})^{k(s)}$ with a non-zero sub-$B^{k(s)}$-module of
$B^{k(s)}/\mathfrak{p}^{k(s)} = (B/\mathfrak{p})^{k(s)}$. Taking `(3.1.7)` into account, one sees that one is reduced to
proving, with the same notations, that if $B$ is integral, then $B^{k(s)}$ has no embedded associated prime ideals for
$s$ near $\eta$. Now, replacing $A$ if necessary by $A_{g}$ and $B$ by $B_{g}$ (where $g$ is an element $\neq 0$ of
$A$), one may suppose that $B$ contains a polynomial $A$-algebra $C = A[T_{1}, \cdots, T_{n}]$ such that $B$ is a
finitely generated $C$-module (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, cor. 1 of th. 1). Since $B^{K}$ is a
torsion-free $C^{K}$-module, one may apply again the reasoning made above by replacing $B$, $M$, and $\mathfrak{q}$ by
$C$, $B$, and `(0)` respectively, and it therefore suffices to see that for $s$ near $\eta$, $C^{k(s)}$ has no embedded
associated prime ideals. But this is evident since $C^{k(s)} = k(s)[T_{1}, \cdots, T_{n}]$ is an integral ring. Q.E.D.

**Theorem (9.7.7).**

<!-- label: IV.9.7.7 -->

*Let $f : X \to S$ be a morphism of finite presentation, and let $E$ be the set of $s \in S$ for which $X_{s}$ has one
of the following properties:*

*(i) being geometrically irreducible;*

*(ii) being geometrically connected;*

*(iii) being geometrically reduced;*

*(iv) being geometrically integral.*

*Then $E$ is locally constructible in $S$.*

To see that the properties considered are constructible, we first remark that they trivially satisfy condition
`(9.2.1, (i))`, by virtue of `(4.5.6, (i))` and `(4.6.5, (i))`. It therefore remains to verify `(9.2.1, (ii))`, so we
may suppose $S = \operatorname{Spec}(A)$ is affine, Noetherian, and integral, with generic point $\eta$. By virtue of
`(4.6.8)`, there exists a finite extension $K'$ of $K = k(\eta)$ such that $(X_{\eta})_{(K')}$ is such that its
irreducible (resp. connected) components are geometrically irreducible (resp. geometrically connected) and such that
$((X_{\eta})_{(K')})_{red}$ is geometrically reduced. Since there exists a basis of $K'$ over $K$ formed of elements
integral over $A$, the integral ring $A'$ generated by these elements is finite over $A$ and has $K'$ as its field of
fractions. Set $S' = \operatorname{Spec}(A')$; the morphism $g : S' \to S$ is finite and dominant, hence surjective
`(II, 6.1.10)`. Set $X' = X_{(S')}$, so that if $\eta'$ is the generic point of $S'$, one has
$X'_{\eta'} = (X_{\eta})_{(K')}$; the set $E'$ of $s' \in S'$ such that $X'_{s'}$ has one of properties (i), (ii),
(iii), or (iv) is equal to $g^{-1}(E)$ `(9.2.2, (iv))` ($E$ corresponding of course to the same property); since $g$ is
surjective, one has $E = g(E')$ and $S - E = g(S' - E')$; moreover, $g$ is closed and $g^{-1}(\eta) = {\eta'}$ since
$A'$ is integral and finite over $A$ (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, cor. 1 of prop. 1), so the image under
$g$ of every neighbourhood of $\eta'$ is a neighbourhood of $\eta$. The theorem will therefore be proved if we show that
$E'$ or $S' - E'$ is a neighbourhood of $\eta'$. Otherwise put, we may henceforth suppose that the irreducible (resp.
connected) components of $X_{\eta}$ are geometrically irreducible (resp. geometrically connected) and that
$(X_{\eta})_{red}$ is geometrically reduced.

<!-- original page 80 -->

Suppose first that $\eta \in S - E$ for one of properties (i) to (iv). If $X_{\eta}$ is not geometrically irreducible
(resp. geometrically connected), it is not irreducible (resp. connected) by the preceding hypothesis, so the same is
true of $X_{s}$ for $s$ in a neighbourhood of $\eta$ `(9.7.1)`, and *a fortiori* in this neighbourhood $X_{s}$ is not
geometrically irreducible (resp. geometrically connected). On the other hand, if $X_{\eta}$ is not geometrically
reduced, it is not reduced (otherwise it would be equal to $(X_{\eta})_{red}$, which is geometrically reduced by
hypothesis); hence, in a neighbourhood of $\eta$, $X_{s}$ is not reduced `(9.7.2)`, and *a fortiori* not geometrically
reduced. Finally, if $X_{\eta}$ is not geometrically integral, either it is not reduced, in which case we have just seen
that $X_{s}$ is not reduced (nor *a fortiori* integral) in a neighbourhood of $\eta$; or $X_{\eta}$ is reduced (hence
geometrically reduced by hypothesis), and then it is not geometrically irreducible, and we saw above that the same is
then true of $X_{s}$ for $s$ near $\eta$; *a fortiori* $X_{s}$ is not geometrically integral for these values of $s$.

We shall therefore henceforth suppose that $\eta \in E$ and examine separately each of the properties considered.

**1°** Suppose $X_{\eta}$ is geometrically integral. Let $L$ be the field of rational functions on $X_{\eta}$; the
hypothesis on $X_{\eta}$ implies that $L$ is a separable extension of $K$ `(4.6.3)`, hence a finite separable extension
of a pure extension $K(T_{1}, \cdots, T_{n})$ ($T_{i}$ indeterminates); there is therefore an element $z \in L$,
integral over the ring $K[T_{1}, \cdots, T_{n}]$, such that $L = K(T_{1}, \cdots, T_{n})(z)$; let $G \in K[T_{1},
\cdots, T_{n}, T_{n+1}]$ be its minimal polynomial. There exists an element $g \neq 0$ of $A$ such that all the non-zero
coefficients of $G$ (which belong to $K$) lie in the ring $A_{g}$; replacing $A$ by $A_{g}$ (which amounts to replacing
$S$ by a neighbourhood of $\eta$), we may therefore suppose that $G$ has its coefficients in $A$; denoting by $F$ the
polynomial $G$ considered as an element of $A[T_{1}, \cdots, T_{n}, T_{n+1}]$, we then have $G = F^{k(\eta)}$. Set $Y =
\operatorname{Spec}(A[T_{1}, \cdots, T_{n+1}]/(F))$, so that $Y_{\eta} = \operatorname{Spec}(k(\eta)[T_{1}, \cdots,
T_{n+1}]/(G))$; $Y_{\eta}$ is an integral scheme having $L$ as its field of rational functions. Since $X_{\eta}$ and
$Y_{\eta}$ are Noetherian, there exists a non-empty open $V \subset Y_{\eta}$ and an open immersion $v : V \to X_{\eta}$
(necessarily dominant) `((I, 6.5.1, (ii))` and `(6.5.4, (ii)))`. Let $W$ be an open of $Y$ such that $W \cap Y_{\eta} =
V$; applying `(8.8.2, (i))` and `(8.10.5, (iii))` via the method of `(8.1.2, a))`, one sees that, by replacing $S$ if
necessary by a neighbourhood of $\eta$, one may suppose that $v = w_{\eta}$, where $w : W \to X$ is an open immersion.

This being so, we saw `(4.6.3)` that the criterion for an integral algebraic prescheme to be geometrically integral
depends only on its field of rational functions; since $X_{\eta}$ is geometrically integral by hypothesis, the same is
true of $Y_{\eta}$, and the definition of $G$ therefore implies that this polynomial is geometrically irreducible
`(9.7.4)`. Applying `(9.7.5)`, one sees that there is a neighbourhood $U$ of $\eta$ in $S$ such that $F^{k(s)}$ is
geometrically irreducible for every $s \in U$, hence $Y_{s}$ is geometrically integral for $s \in U$ `(9.7.4)`;
moreover, we may suppose that for $s \in U$, $W_{s}$ is non-empty `(9.5.1)`, and consequently is geometrically integral
`(4.6.3)`; finally, we may also suppose that

<!-- original page 81 -->

for $s \in U$, $w_{s} : W_{s} \to X_{s}$ is an open immersion `(9.6.1, (x))`, and that its image in $X_{s}$ is
everywhere dense `(9.5.3)`. Otherwise put, for $s \in U$ there is in $X_{s}$ an everywhere dense open $W_{s}$ which is
geometrically integral; criterion `(4.5.9, c))` therefore already shows that $X_{s}$ is geometrically irreducible for $s
\in U$. Finally, since $X_{\eta}$ is reduced and consequently has no embedded associated prime cycle `(3.2.1)`, one may
also suppose that for $s \in U$, $X_{s}$ has no embedded associated prime cycle `(9.7.6)`; let then (for a fixed $s \in
U$) $\Omega$ be an algebraically closed extension of $k(s)$, and let $p : (X_{s})_{(\Omega)} \to X_{s}$ be the canonical
projection; $p^{-1}(W_{s})$ is a dense open in $(X_{s})_{(\Omega)}$ `(2.3.10)` and is integral by hypothesis; moreover
$(X_{s})_{(\Omega)}$ has no embedded associated prime cycle `(4.2.7)`, so one concludes from `(3.2.1)` that
$(X_{s})_{(\Omega)}$ is reduced; this completes the proof that $X_{s}$ is geometrically integral `(4.6.1)`.

**2°** Suppose $X_{\eta}$ is geometrically irreducible; since $X_{red}$ is also of finite type over $S$ `(1.5.4, (vi))`
one may, taking `(I, 5.1.8)` into account, replace $X$ by $X_{red}$; then $X_{\eta}$ is also integral, and since by
hypothesis $X_{\eta}$ is geometrically reduced, it is geometrically integral. One is then in the conditions of 1°, and
one concludes (returning to the initial hypotheses) that $X_{s}$ is geometrically irreducible for $s$ near $\eta$.

**3°** Suppose $X_{\eta}$ is geometrically connected, and let $Z_{i}$ ($1 \leq i \leq n$) be the irreducible components
of $X_{\eta}$; there exists (by virtue of `(5.10.8.1)` applied to $\Sigma = {\emptyset}$) a surjective map $j \mapsto
\nu(j)$ from an interval `[1, m]` of $\mathbb{N}$ onto `[1, n]` such that $Z_{\nu(j)} \cap Z_{\nu(j+1)} \neq \emptyset$
for $1 \leq j \leq m$. For each $i$, let $X_{i}$ be the closure of $Z_{i}$ in $X$, and let $Y$ be the union of the
$X_{i}$; since $Y_{\eta} = X_{\eta}$ by definition, we may suppose, by virtue of `(9.5.1)`, that $Y_{s} = X_{s}$ for
every $s \in S$, hence that $X_{s}$ is the union of the $(X_{i})_{s}$. But, considering the reduced closed
sub-preschemes of $X$ having the $X_{i}$ as underlying spaces, one sees by 2° that there exists a neighbourhood $U$ of
$\eta$ in $S$ such that for $s \in U$ the $(X_{i})_{s}$ are geometrically irreducible (since the $(X_{i})_{\eta}$ may be
supposed geometrically irreducible, as we saw at the start). Moreover, we may also suppose that for $s \in U$, one has
$(X_{\nu(j)})_{s} \cap (X_{\nu(j+1)})_{s} \neq \emptyset$ `(9.5.1)` for $1 \leq j \leq m$; one concludes at once that
$X_{s}$ is connected, hence `(4.5.13.1)` geometrically connected for $s \in U$.

**4°** Suppose $X_{\eta}$ is geometrically reduced; let $Z_{i}$ be the irreducible components of $X_{\eta}$, $W_{i}$ the
interior of $Z_{i}$ in $X_{\eta}$; there is for each $i$ an open $V_{i}$ of $X$ such that $W_{i} = V_{i} \cap X_{\eta}$
for every $i$; since the $W_{i}$ are open and pairwise disjoint and their union is dense in $X_{\eta}$, we may
(`(9.5.1)`, `(9.5.3)`, and `(9.5.4)`) suppose that for $s$ near $\eta$, the $(V_{i})_{s}$ are pairwise disjoint opens in
$X_{s}$ and that their union is dense in $X_{s}$. Moreover, since the $W_{i}$ are geometrically reduced and were
supposed at the start geometrically irreducible, it follows from 1° that for $s$ near $\eta$, the $(V_{i})_{s}$ are
geometrically integral, and *a fortiori* reduced. On the other hand, one draws from `(9.7.6)` that for $s$ near $\eta$,
$X_{s}$ has no embedded associated prime cycle, since this is so for $X_{\eta}$, which is reduced `(3.2.1)`; one
concludes from `(3.2.1)` that $X_{s}$ is reduced, and from `(4.6.1)` that it is geometrically reduced.

<!-- original page 82 -->

The parts of statement `(9.7.7)` concerning properties (i) and (ii) generalize as follows:

**Proposition (9.7.8).**

<!-- label: IV.9.7.8 -->

*Let $S$ be an irreducible prescheme with generic point $\eta$, and $f : X \to S$ a morphism of finite presentation. Let
$n$ (resp. $n'$) be the geometric number of irreducible (resp. connected) components of $X_{\eta}$ `(4.5.2)`. Then there
exists a neighbourhood $U$ of $\eta$ in $S$ such that for every $s \in U$ the geometric number of irreducible (resp.
connected) components of $X_{s}$ is equal to $n$ (resp. $n'$).*

Taking into account that the geometric number of irreducible (resp. connected) components of an algebraic prescheme is
invariant under extension of the base field `(4.5.6)`, one sees by the method of `(9.2.3)` that one may reduce to the
case where $S$ is affine, Noetherian, and integral. Moreover, reasoning as at the start of the proof of `(9.7.7)`, one
sees that one may suppose that the irreducible (resp. connected) components of $X_{\eta}$ are geometrically irreducible
(resp. geometrically connected). We already know `(9.7.1)` that for every $s$ near $\eta$, $X_{s}$ has at least $n$
irreducible components and $n'$ connected components. On the other hand, if $Z_{i}$ (resp. $Z'_{j}$) are the irreducible
(resp. connected) components of $X_{\eta}$, and $X_{i}$ (resp. $X'_{j}$) the reduced closed sub-prescheme of $X$ having
as underlying space the closure of $Z_{i}$ (resp. $Z'_{j}$) in $X$, it follows from `(9.5.1)` that in a neighbourhood of
$\eta$, the $(X_{i})_{s}$ (resp. $(X'_{j})_{s}$) form a covering of $X_{s}$ and that the $(X'_{j})_{s}$ are pairwise
disjoint; since the $(X_{i})_{s}$ (resp. $(X'_{j})_{s}$) are geometrically irreducible (resp. geometrically connected)
by virtue of `(9.7.7)` for $s$ near $\eta$, one sees that $X_{s}$ has at most $n$ irreducible components and at most
$n'$ connected components, whence the proposition.

**Corollary (9.7.9).**

<!-- label: IV.9.7.9 -->

*Let $f : X \to S$ be a morphism of finite presentation. For every $s \in S$, let $n(s)$ (resp. `n'(s)`) be the
geometric number of irreducible (resp. connected) components of $f^{-1}(s)$ `(4.5.2)`. Then the function $s \mapsto
n(s)$ (resp. $s \mapsto n'(s)$) is locally constructible in $S$.*

It is a matter of showing that the property "$X$ is an algebraic prescheme over a field $k$ and the geometric number of
irreducible (resp. connected) components of $X$ is equal to $n$ (resp. $n'$)" is constructible. It follows from
`(4.5.6)` that this property satisfies condition `(9.2.1, (i))`, and one is therefore reduced to the case where $S$ is
affine, Noetherian, and integral with generic point $\eta$; the conclusion then follows from `(9.7.8)`.

**Corollary (9.7.10).**

<!-- label: IV.9.7.10 -->

*Let $X$ be a locally Noetherian prescheme such that, if $X'$ is the normalization of $X_{red}$, the canonical morphism
$f : X' \to X$ is finite. Then the set of points $x \in X$ such that $X$ is geometrically unibranch at the point $x$ is
locally constructible in $X$.*

Indeed, this set is by definition the set of points $x \in X$ such that the number of geometric points of $f^{-1}(x)$ is
equal to `1`. But since $f$ is finite, this number is also the geometric number of irreducible components of the
discrete space $f^{-1}(x)$ (taking into account the definition of the normalization `(II, 6.3.8)` and `(4.5.11)`); the
conclusion therefore follows from `(9.7.9)`.

**Remark (9.7.11).**

<!-- label: IV.9.7.11 -->

\*Let $Z$ be a locally constructible part of $X$ such that, for every $s \in S$, $Z \cap X_{s}$ is open in $X_{s}$, and
denote by $Z_{s}$ the sub-prescheme of $X_{s}$ induced

<!-- original page 83 -->

on the open $Z \cap X_{s}$. Then, in theorem `(9.7.7)`, one may replace $X_{s}$ by $Z_{s}$ without changing the
conclusion: one sees this by repeating the reasoning made in `(9.6.7, (ii))`.\*

**Proposition (9.7.12).**

<!-- label: IV.9.7.12 -->

*Let $f : X \to S$ be a morphism of finite presentation, and $g : S \to X$ an $S$-section of $X$ `(I, 2.5.5)`. For every
$s \in S$, let $X^{\circ}_{s}$ be the connected component of $f^{-1}(s)$ containing $g(s)$; then, the union $X^{\circ}$
of the $X^{\circ}_{s}$ for $s \in S$ is a locally constructible part of $X$.*

Let us first show that one may reduce to the case where $S$ is affine and Noetherian. One may always suppose $S =
\operatorname{Spec}(A)$ affine; with the notations of `(9.2.3)`, one has $f = (f_{0})_{(S)}$, where $f_{0} : X_{0} \to
S_{0}$ is a morphism of finite type, and one may moreover suppose that there exists an `S_0`-section $g_{0} : S_{0} \to
X_{0}$ such that $g = (g_{0})_{(S)}$ `(8.9.1)`. Note now that if $p$ is the morphism $S \to S_{0}$, then, for every
$s_{0} \in S_{0}$, the connected component $(X_{0})^{\circ}_{s_{0}}$ of $f^{-1}_{0}(s_{0})$ containing $g_{0}(s_{0})$ is
geometrically connected `(4.5.13)`, and consequently, if $s_{0} = p(s)$, one has $X^{\circ}_{s} =
q^{-1}((X_{0})^{\circ}_{s_{0}})$ where $q : X_{s} \to (X_{0})_{s_{0}}$ is the canonical projection (`(4.5.8)` and
`(4.4.1)`); our assertion therefore follows from `(1.8.2)`.

Let us then use the constructibility criterion $(0_{III}, 9.2.3)$: let $x$ be a point of $X$, $Z$ the reduced sub-
prescheme of $X$ having $\overline{x}$ as underlying space, $Y$ the reduced sub-prescheme of $S$ having $f(Z)$ as
underlying space; since the restriction of $f$ to $Z$ factors as $Z \to Y \to S$ `(I, 5.2.2)`, we may replace $S$ by
$Y$, otherwise put suppose that $f(x) = \eta$, the generic point of the integral prescheme $S$. By hypothesis,
$X_{\eta}$ is the sum of two sub- preschemes $X^{0}_{\eta}$, $X^{1}_{\eta}$ induced on complementary opens of
$X_{\eta}$. By virtue of `(9.5.4)` and `(9.5.1)`, we may therefore, by replacing $S$ if necessary by a neighbourhood of
$\eta$, suppose that $X$ is the union of two disjoint opens $X^{0}$, $X^{1}$ such that $(X^{0})_{\eta} = X^{0}_{\eta}$
and $(X^{1})_{\eta} = X^{1}_{\eta}$. Since $g : S \to X$ is continuous and injective, $S$ is the union of the two
disjoint opens $g^{-1}(X^{0})$ and $g^{-1}(X^{1})$; but since $S$ is irreducible, and *a fortiori* connected, one of
these two opens is empty, and since $g(\eta) \in X^{0}_{\eta}$ by definition, one has $g^{-1}(X^{1}) = \emptyset$. In
other words, $g$ is an $S$-section of $X^{0}$; on the other hand, since $(X^{0})_{\eta}$ is geometrically connected
`(4.5.13)`, the same is true of $(X^{0})_{s}$ for every $s$ near $\eta$ `(9.7.7)`; since $g(s) \in (X^{0})_{s}$, one has
indeed $(X^{0})_{s} = X^{\circ}_{s}$. Q.E.D.

### 9.8. Primary decomposition near a generic fibre

**Proposition (9.8.1).**

<!-- label: IV.9.8.1 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. Then the set $E$ of $s \in S$ such that $\mathcal{F}_{s}$ is an $\mathcal{O}_{X_{s}}$-Module with
no embedded associated prime cycle is locally constructible.*

We know that for quasi-coherent Modules on algebraic preschemes, the property of having no embedded associated prime
cycle is invariant under change of base field `(4.2.7)`; we may therefore restrict to the case where $S$ is affine,
Noetherian, and integral with generic point $\eta$, and prove that in this case $E$ or $S - E$ is a neighbourhood of
$\eta$. We saw in `(9.7.6)` that if $\eta \in E$, then $E$ is a neighbourhood of $\eta$; there remains to consider the
case where $\mathcal{F}_{\eta}$ has embedded associated prime cycles. We may restrict to the case where $X$ is affine,
and where there is a sub- $\mathcal{O}_{X_{\eta}}$-Module coherent $\mathcal{F}'_{\eta}$ of $\mathcal{F}_{\eta}$ whose
support $Z'$ is non-empty and rare with respect to the support $Z$ of $\mathcal{F}_{\eta}$ `(3.1.3)`; then, by virtue of
`(8.5.2, (i)` and `(ii))`

<!-- original page 84 -->

and `(8.5.8)`, applied via the method of `(8.1.2, a))`, there exists a coherent sub-$\mathcal{O}_{X}$-Module
$\mathcal{F}'$ of $\mathcal{F}$ such that $\mathcal{F}' = \mathcal{F}'_{\eta}$; if $Y = Supp(\mathcal{F})$, $Y' =
Supp(\mathcal{F}')$, one consequently has $Y_{s} = Supp(\mathcal{F}_{s})$, $Y'_{s} = Supp(\mathcal{F}'_{s})$ for every
$s \in S$ `(I, 9.1.13)`, and in particular $Z = Y_{\eta}$, $Z' = Y'_{\eta}$; since $Z - Z'$ is dense in $Z$ and $Z' \neq
\emptyset$, there is a neighbourhood $U$ of $\eta$ such that for $s \in U$, $Y_{s} - Y'_{s}$ is dense in $Y_{s}$, and
$Y'_{s} \neq \emptyset$ (`(9.5.1)` and `(9.5.3)`); considering a generic point of an irreducible component of $Y'_{s}$
and a sufficiently small neighbourhood of this point in $X_{s}$, one deduces at once from `(3.1.3)` that
$\mathcal{F}_{s}$ has embedded associated prime cycles.

**(9.8.2)**

<!-- label: IV.9.8.2 -->

Let $S$ be an integral Noetherian prescheme with generic point $\eta$, $f : X \to S$ a morphism of finite type,
$\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Consider a reduced irredundant decomposition $(\mathcal{G}_{i})_{i
\in I}$ of $\mathcal{F}_{\eta}$ `(3.2.6)`; the $\mathcal{G}_{i}$ are thus quotients of $\mathcal{F}_{\eta}$, and there
is an injective homomorphism $h : \mathcal{F}_{\eta} \to \oplus \mathcal{G}_{i}$; moreover $Ass(\mathcal{G}_{i})$ is
reduced to a single point $x_{i}$. Let $Z_{i}$ be the closure of ${x_{i}}$ in $X$, so that $(Z_{i})_{\eta} =
Supp(\mathcal{G}_{i})$. Denote by $\mathcal{J}_{i}$ the coherent Ideal of $\mathcal{O}_{X}$ defining the reduced closed
sub-prescheme of $X$ with underlying space $Z_{i}$ (sub-prescheme also denoted $Z_{i}$). By virtue of `(8.5.2)` and
`(8.5.8)`, applied via the method of `(8.1.2, a))`, we may (by restricting $S$ if necessary to a neighbourhood of
$\eta$) suppose that there exist quotients $\mathcal{H}_{i}$ of $\mathcal{F}$ ($i \in I$) such that $\mathcal{G}_{i} =
(\mathcal{H}_{i})_{\eta}$ for every $i$, and a homomorphism $g : \mathcal{F} \to \oplus \mathcal{H}_{i}$ such that $h =
g_{\eta}$. Moreover `(I, 9.3.5)`, there exists an integer $m$ such that $((\mathcal{J}_{i})_{\eta})^{m} \mathcal{G}_{i}
= (\mathcal{J}_{i})^{m}_{\eta} \mathcal{G}_{i} = 0$, and by restricting $S$ again, we may therefore also suppose that
$\mathcal{J}^{m}_{i} \mathcal{H}_{i} = 0$ `(8.5.2.5)`, so that the support of $\mathcal{H}_{i}$ is contained in $Z_{i}$;
but since it is closed and contains $x_{i}$, it is necessarily equal to $Z_{i}$.

**Proposition (9.8.3).**

<!-- label: IV.9.8.3 -->

*Under the conditions of `(9.8.2)`, for every $s \in S$ and every $i \in I$, denote by $x_{is \alpha}$ ($\alpha \in
\mathcal{J}_{s,i}$) the maximal points of $(Z_{i})_{s}$. There exists a neighbourhood $U$ of $\eta$ in $S$ such that,
for every $s \in U$, the $x_{is \alpha}$ (for $i \in I$ and, for each $i$, $\alpha \in \mathcal{J}_{s,i}$) are pairwise
distinct and $Ass(\mathcal{F}_{s})$ is the set of the $x_{is \alpha}$ (in other words, the prime cycles associated to
$\mathcal{F}_{s}$ are the irreducible components of the $(Z_{i})_{s}$). Moreover, one may take $U$ such that, for the
closure of ${x_{is \alpha}}$ in $X_{s}$ to be a maximal associated prime cycle of $\mathcal{F}_{s}$, it is necessary and
sufficient that $(Z_{i})_{\eta}$ (closure of ${x_{i}}$ in $X_{\eta}$) be a maximal associated prime cycle of
$\mathcal{F}_{\eta}$.*

It follows from `(3.1.3, c'))` that for each $i$, there exists an open $W_{i}$ in $X_{\eta}$ such that $W_{i} \cap
(Z_{i})_{\eta}$ is non- empty, and a coherent $\mathcal{O}_{X_{\eta}}$-Module $\mathcal{H}'_{i}$, of support $W_{i} \cap
(Z_{i})_{\eta}$, such that there is an injective homomorphism $v_{i} : \mathcal{H}'_{i} \to \mathcal{F}_{\eta} | W_{i}$.
Let $V_{i}$ be an open of $X$ such that $V_{i} \cap X_{\eta} = W_{i}$; applying, as in `(9.8.2)`, the results of
`(8.5.2)` and `(8.5.8)`, we may (by restricting $S$) suppose that there exist a coherent Module
$\tilde{\mathcal{H}}_{i}$ of support $V_{i} \cap Z_{i}$ and a homomorphism $u_{i} : \tilde{\mathcal{H}}_{i} \to
\mathcal{F} | V_{i}$ such that $\mathcal{H}'_{i} = (\tilde{\mathcal{H}}_{i})_{\eta}$ and $v_{i} = (u_{i})_{\eta}$. We
shall prove that there is a neighbourhood $U$ of $\eta$ such that for $s \in U$, the following properties hold:

*(i) The $(\mathcal{H}_{i})_{s}$ have no embedded associated prime cycle.*

*(ii) The homomorphism $g_{s} : \mathcal{F}_{s} \to \oplus (\mathcal{H}_{i})_{s}$ is injective.*

*(iii) $(Z_{i})_{s} \cap (V_{i})_{s}$ is dense in $(Z_{i})_{s}$, $(\tilde{\mathcal{H}}_{i})_{s}$ has support
$(Z_{i})_{s} \cap (V_{i})_{s}$, and $(u_{i})_{s} : (\tilde{\mathcal{H}}_{i})_{s} \to \mathcal{F}_{s} | (V_{i})_{s}$ is
injective.*

<!-- original page 85 -->

*(iv) For $i \neq j$, every irreducible component of $(Z_{i})_{s}$ is distinct from every irreducible component of
$(Z_{j})_{s}$.*

Now, (i) has already been seen `(9.7.6)`; (ii) is a special case of `(9.4.5)`; (iii) follows similarly from `(9.5.3)`
and `(9.4.5)`. Finally, if $i \neq j$, $(Z_{i})_{\eta} \cap (Z_{j})_{\eta} = (Z_{i} \cap Z_{j})_{\eta}$ is rare in
$(Z_{i})_{\eta}$ or in $(Z_{j})_{\eta}$; suppose for example that $(Z_{i} \cap Z_{j})_{\eta}$ is rare in
$(Z_{j})_{\eta}$; then it follows from `(9.5.3)` and `(9.5.4)` that for $s$ near $\eta$, $(Z_{i} \cap Z_{j})_{s} =
(Z_{i})_{s} \cap (Z_{j})_{s}$ is rare in $(Z_{j})_{s}$, which shows that no irreducible component of $(Z_{j})_{s}$ can
be contained in an irreducible component of $(Z_{i})_{s}$, nor *a fortiori* equal to it.

This being so, it follows from (ii) and from `(3.1.7)` that for $s \in U$, one has $Ass(\mathcal{F}_{s}) \subset
\bigcup_{i} Ass((\mathcal{H}_{i})_{s})$, and it follows from (i) that $Ass((\mathcal{H}_{i})_{s})$ is the set of $x_{is
\alpha}$ ($\alpha \in \mathcal{J}_{s,i}$). On the other hand, by virtue of (iii) and the criterion `(3.1.3, c'))`, each
of the $x_{is \alpha}$ ($\alpha \in \mathcal{J}_{s,i}$, $i \in I$) belongs to $Ass(\mathcal{F}_{s})$. Finally, (iv)
means that the $x_{is \alpha}$ are pairwise distinct.

It remains to prove the final assertion of the statement. It follows from (iv) that for given $s$ and $i$, none of the
sets ${x_{is \alpha}}$ can be contained in another for $\alpha \in \mathcal{J}_{s,i}$. On the other hand, if
$(Z_{j})_{\eta} \subset (Z_{i})_{\eta}$, we may take $U$ so that $(Z_{j})_{s} \subset (Z_{i})_{s}$ for $s \in U$
`(9.5.1)`, hence each $x_{js \beta}$ belongs to the closure of some $x_{is \alpha}$; on the contrary, if $(Z_{j})_{\eta}
\cap (Z_{i})_{\eta}$ is rare in $(Z_{j})_{\eta}$, we saw in proving (iv) that $(Z_{j})_{s} \cap (Z_{i})_{s}$ is rare in
$(Z_{j})_{s}$, so none of the $x_{js \beta}$ is adherent to a $x_{is \alpha}$. In particular, if $(Z_{j})_{\eta}$ is
maximal, which amounts to saying that $(Z_{j})_{\eta} \cap (Z_{i})_{\eta}$ is rare in $(Z_{j})_{\eta}$ for every $i \neq
j$, one concludes that $(Z_{j})_{s} \cap (Z_{i})_{s}$ is rare in $(Z_{j})_{s}$ for every $i \neq j$, hence that every
$x_{js \beta}$ ($\beta \in \mathcal{J}_{s,j}$) is maximal. Q.E.D.

**Corollary (9.8.4).**

<!-- label: IV.9.8.4 -->

*The notations and hypotheses being those of `(9.8.2)`, there exists a neighbourhood $U$ of $\eta$ in $S$ such that, for
every $s \in U$, each $(\mathcal{H}_{i})_{s}$ has no embedded associated prime cycle; moreover, if
$(\check{\mathcal{H}}_{s i \alpha})_{\alpha \in \mathcal{J}_{s,i}}$ is the unique reduced irredundant decomposition of
$((\mathcal{H}_{i})_{\eta})_{s}$, then, for every $s \in U$, the family $(\check{\mathcal{H}}_{s i \alpha})_{i \in I,
\alpha \in \mathcal{J}_{s,i}}$ is a reduced irredundant decomposition of $\mathcal{F}_{s}$.*

The first assertion follows from `(9.8.1)` and the definition of the $\mathcal{H}_{i}$. On the other hand, we saw in
`(9.8.3)` that the homomorphism $\mathcal{F}_{s} \to \oplus (\mathcal{H}_{i})_{s}$ is injective, and by definition the
same is true of each of the homomorphisms $(\mathcal{H}_{i})_{s} \to \oplus_{\alpha} \check{\mathcal{H}}_{s i \alpha}$,
hence the homomorphism $\mathcal{F}_{s} \to \oplus \check{\mathcal{H}}_{s i \alpha}$ is injective. Since one may suppose
`(9.4.5)` that each of the $(\mathcal{H}_{i})_{s}$ is a quotient of $\mathcal{F}_{s}$, the $\check{\mathcal{H}}_{s i
\alpha}$ are quotients of $\mathcal{F}_{s}$, and there remains to verify `(3.2.5)` that the $x_{is \alpha}$ are pairwise
distinct and belong to $Ass(\mathcal{F}_{s})$, which was proved in `(9.8.3)`.

**Proposition (9.8.5).**

<!-- label: IV.9.8.5 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. For every $s \in S$, let $E(s)$ (resp. `E'(s)`) be the finite set (subset of $\mathbb{Z} \cup
{-\infty}$) of dimensions of the prime cycles associated to $\mathcal{F}_{s}$ (resp. of the maximal prime cycles
associated to $\mathcal{F}_{s}$, that is, of the irreducible components of $Supp(\mathcal{F}_{s})$). Then the functions
$s \mapsto E(s)$ and $s \mapsto E'(s)$ are locally constructible in $S$.*

<!-- original page 86 -->

It follows from `(4.2.7)` and `(4.2.8)` that condition `(9.2.1, (i))` is satisfied for the properties we wish to show
are constructible. One is therefore reduced to the case where $S$ is affine, Noetherian, and integral, and to proving
that $E$ and $E'$ are constant in a neighbourhood of the generic point $\eta$ of $S$; but this follows from `(9.8.3)`
and `(9.5.5)`.

**Proposition (9.8.6).**

<!-- label: IV.9.8.6 -->

*With the hypotheses and notations of `(9.8.2)`, let $i \in I$ be such that $(Z_{i})_{\eta}$ is maximal (in other words,
is an irreducible component of $Supp(\mathcal{F}_{\eta})$). Then, there exists a neighbourhood $U$ of $\eta$ in $S$ such
that for every $s \in U$ and every $\alpha \in \mathcal{J}_{s,i}$, the geometric length of $\mathcal{F}_{s}$ at $x_{is
\alpha}$ (relative to $k(s)$) `(4.7.5)` is equal to the geometric length of $\mathcal{F}_{\eta}$ at $x_{i}$ (relative to
$k(\eta)$).*

One may evidently restrict to the case where $S = \operatorname{Spec}(A)$ is affine; let us first show that one may
reduce to the case where the sub-prescheme $(Z_{i})_{\eta}$ of $X_{\eta}$, which is reduced, is geometrically integral.
There is indeed a finite extension $K'$ of $K = k(\eta)$ such that $(((Z_{i})_{\eta})_{(K')})_{red}$ is geometrically
reduced and the irreducible components of $((Z_{i})_{\eta})_{(K')}$ are geometrically irreducible `(4.6.8)`. Proceeding
as in the proof of `(9.7.7)` by considering a sub-$A$-algebra $A'$ of $K'$ having $K'$ as field of fractions and finite
over $A$. Set $S' = \operatorname{Spec}(A')$ and consider the finite surjective morphism $g : S' \to S$; let then $X' =
X_{(S')}$ and $\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{S}} \mathcal{O}_{S'}$, and let $\eta'$ be the generic
point of $S'$. For every $s' \in S'$, let $s = g(s')$; if $T$ is an irreducible component of $Supp(\mathcal{F}_{s})$,
the irreducible components $T'_{j}$ of $T_{(k(s'))}$ are irreducible components of $Supp(\mathcal{F}'_{s'})$ and
dominate $T$ `(4.2.7)`, and the radicial multiplicities of $T$ with respect to $\mathcal{F}_{s}$ and of each $T'_{j}$
with respect to $\mathcal{F}'_{s'}$ are the same `(4.7.9)`. The reasoning of the first part of `(9.7.7)` therefore shows
that one may restrict to proving the proposition for $X'$ and $\mathcal{F}'$; and by virtue of the choice of $K'$, the
reduced sub-preschemes with underlying spaces the irreducible components of $((Z_{i})_{\eta})_{(K')}$ are geometrically
integral `(4.6.1)`.

Suppose then henceforth that $(Z_{i})_{\eta}$ is geometrically integral; then `(9.7.7)` the same is true of
$(Z_{i})_{s}$ for $s$ near $\eta$; the definition `(4.7.5)` shows that it will therefore suffice to prove that the
length of the $\mathcal{O}_{X_{\eta}, x_{i}}$-module $(\mathcal{F}_{\eta})_{x_{i}}$ is equal to that of the
$\mathcal{O}_{X_{s}, x_{is}}$-module $(\mathcal{F}_{s})_{x_{is}}$ (here we have suppressed the index $\alpha$,
unnecessary by hypothesis). The question being evidently local on $X$, we may suppose (by restricting to a neighbourhood
of $x_{i}$) that $\mathcal{F} = \mathcal{H}_{i}$, so that $\mathcal{F}_{\eta}$ is irredundant on $X =
\operatorname{Spec}(B)$ affine, and we shall write $Z$ instead of $Z_{i}$, and $x$ for the generic point of $Z$ (and of
$Z_{\eta}$). The Noetherian ring $B$ therefore contains $A$ as a subring, and $\mathcal{F} = \tilde{M}$, where $M$ is a
finitely generated $B$-module; moreover, if $K$ is the field of fractions of $A$, the $B^{K}$-module $M^{K}$ is $\neq 0$
and irredundant. Let $\mathfrak{q}$ be the unique element of $Ass(M^{K})$ and let $\mathfrak{p}$ be the prime ideal of
$B$, inverse image of $\mathfrak{q}$. Using `(5.11.1.1)` as in the proof of `(9.7.6)`, one reduces to the case where $B$
is integral and $M$ a non-zero sub-module of $B$; then $\mathcal{F}$ is a non-zero sub-$\mathcal{O}_{X}$-Module of
$\mathcal{O}_{Z}$, and by virtue of `(9.4.5)`, for $s$ near $\eta$, $\mathcal{F}_{s}$ is isomorphic to a non-zero sub-
$\mathcal{O}_{X_{s}}$-Module of $\mathcal{O}_{Z_{s}}$; since $Z_{s}$ is geometrically integral, the lengths of
$(\mathcal{F}_{\eta})_{x}$ and of $(\mathcal{F}_{s})_{x_{s}}$ are both equal to `1`, which completes the proof.

<!-- original page 87 -->

**Corollary (9.8.7).**

<!-- label: IV.9.8.7 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. For every $s \in S$, let $M(s)$ be the set of pairs $(d, m)$ such that there exists an irreducible
component of $Supp(\mathcal{F}_{s})$ of dimension $d$ and of radicial multiplicity $m$ for $\mathcal{F}_{s}$ `(4.7.8)`.
Then the function $s \mapsto M(s)$ is locally constructible in $S$.*

It follows from `(4.2.7)` and `(4.7.9)` that condition `(9.2.1, (i))` is satisfied for the property we wish to show is
constructible. One is therefore reduced to the case where $S$ is affine, Noetherian, and integral, and to proving that
$M$ is constant in a neighbourhood of the generic point of $S$; but then the proposition follows from `(9.8.3)` and
`(9.8.6)`.

**Proposition (9.8.8).**

<!-- label: IV.9.8.8 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. For every $s \in S$, let $\ell(s)$ be the sum of the total multiplicities for $\mathcal{F}_{s}$
(relative to $k(s)$) of the generic points of the irreducible components of $Supp(\mathcal{F}_{s})$ `(4.7.12)`. Then the
function $s \mapsto \ell(s)$ is locally constructible in $S$.*

Taking `(4.7.12)` into account, condition `(9.2.1, (i))` is satisfied for the property we wish to show is constructible,
and one is therefore reduced to the case where $S$ is affine, Noetherian, and integral with generic point $\eta$, and to
showing that $\ell$ is constant in a neighbourhood of $\eta$. Using the notations of `(9.8.2)`, this follows from the
definition `(4.7.12)`, from the fact that the geometric number of irreducible components of each $(Z_{i})_{s}$ is
constant in a neighbourhood of $\eta$ `(9.7.8)`, that the geometric length of $\mathcal{F}_{s}$ at $x_{is \alpha}$ is
equal to that of $\mathcal{F}_{\eta}$ at $x_{i}$ for each $i$ such that $(Z_{i})_{\eta}$ is maximal `(9.8.6)`, and
finally from the fact that the closure of ${x_{is \alpha}}$ is a maximal associated prime cycle of $\mathcal{F}_{s}$ if
and only if $(Z_{i})_{\eta}$ is a maximal associated prime cycle of $\mathcal{F}_{\eta}$ `(9.8.3)`.

**Remark (9.8.9).**

<!-- label: IV.9.8.9 -->

*One can refine the preceding propositions in various ways; let us limit ourselves to one statement as an example. We
say that a finite part $P$ of an algebraic $k$-prescheme $X$ is **saturated** if, for every pair of points $x$, $y$ of
$P$, the generic points of the irreducible components of $\overline{x} \cap \overline{y}$ also belong to $P$; for every
finite part $Q$ of $X$, there exists a smallest finite part $P$ of $X$ containing $Q$ and saturated; we shall say that
$P$ is the **saturation** of $Q$. For every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, we shall call **primary
skeleton** of $\mathcal{F}$ the system $(P, Q, \omega, d, m)$ where $Q = Ass(\mathcal{F})$, $P$ is the saturation of
$Q$, $\omega$ the order relation $\overline{x} \subset \overline{y}$ on $P$, $d$ the function $x \mapsto \dim
\overline{x}$ on $P$, $m$ the function $x \mapsto long_{\mathcal{O}_{X,x}} \mathcal{F}_{x}$ defined on the set of
elements of $Q$ maximal for the relation $\omega$. We shall on the other hand call **virtual skeleton** any system $(P,
Q, \omega, d, m)$ where $P$ is a set, $Q$ a part of $P$, $\omega$ an order relation on $P$, $d$ a map of $P$ into
$\mathbb{N}$, $m$ a map into $\mathbb{N}$ of the set of maximal elements of $Q$; one defines in an obvious way the
notion of isomorphism of two virtual skeletons. Finally, with the preceding notations, we shall call **primary type** of
$\mathcal{F}$ the class (for the isomorphism relation of virtual skeletons) of the primary skeleton of $\mathcal{F}$. It
follows from `(4.2.6)`, `(4.2.7)`, `(4.2.8)`, `(4.5.1)`, and `(4.7.9)` that if, for an algebraically closed extension
$k'$*

<!-- original page 88 -->

*of $k$, one sets $X' = X \otimes_{k} k'$ and $\mathcal{F}' = \mathcal{F} \otimes_{k} k'$, the primary type of
$\mathcal{F}'$ is independent of the algebraically closed extension $k'$ of $k$ considered; we shall say that it is the
**geometric primary type** of $\mathcal{F}$. With these definitions, the statement we have in view is the following:*

**(9.8.9.1)**

<!-- label: IV.9.8.9.1 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of
finite presentation. For every $s \in S$, let $T(s)$ be the geometric primary type of $\mathcal{F}_{s}$. Then the
function $s \mapsto T(s)$ is locally constructible in $S$.*

Taking into account the preceding remarks, one is reduced as usual to proving that if $S$ is affine, Noetherian, and
integral with generic point $\eta$, $T(s)$ is constant in a neighbourhood of $\eta$. Reasoning as at the start of
`(9.7.7)`, one may suppose that all the irreducible parts of $X_{\eta}$ which intervene are geometrically irreducible,
and then the proposition follows from `(9.5.1)`, `(9.5.5)`, `(9.8.3)`, and `(9.8.6)`; we leave the details to the
reader. One could generalize by considering several coherent Modules and defining their "*simultaneous primary
skeleton*", etc. The general conclusion of what has been seen since the start of this section is that for all properties
of the type considered (and for an irreducible $S$) the properties valid on the "*generic fibre*" remain so on all
neighbouring fibres.

### 9.9. Constructibility of local properties of the fibres

**Proposition (9.9.1).**

<!-- label: IV.9.9.1 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $Z$ a locally constructible part of $X$ such that for
every $s \in S$, $Z_{s}$ is closed in $X_{s}$, $\Phi$ a finite part of $\mathbb{Z} \cup {\pm\infty}$. Then the following
parts of $X$ are locally constructible:*

*(i) The set of $x \in X$ such that $\dim_{x}(Z_{f(x)})$ belongs to $\Phi$.*

*(ii) The set of $x \in X$ such that $codim_{x}(Z_{f(x)}, X_{f(x)})$ belongs to $\Phi$.*

*(iii) The set of $x \in X$ such that the local ring $\mathcal{O}_{Z_{f(x)}, x}$ is equidimensional.*

One will note that properties (i) and (ii) may also be expressed by saying that the functions $x \mapsto
\dim_{x}(Z_{f(x)})$ and $x \mapsto codim_{x}(Z_{f(x)}, X_{f(x)})$ are locally constructible in $X$ $(0_{III}, 9.3.1)$.

The questions being local on $X$, we may restrict to the case where $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine and where $f$ is a morphism of finite presentation; there then exists a subring `A_0`
of $A$ which is a finitely generated $\mathbb{Z}$-algebra, an `A_0`-prescheme of finite type `X_0`, and a constructible
part `Z_0` of `X_0` such that $X = X_{0} \otimes_{A_{0}} A$ and $Z = h^{-1}(Z_{0})$, where $h : X \to X_{0}$ is the
canonical projection (`(8.9.1)` and `(8.3.11)`). Moreover, for every $s \in S$, if $s_{0}$ is the projection of $s$ in
$S_{0} = \operatorname{Spec}(A_{0})$, one has $X_{s} = (X_{0})_{s_{0}} \otimes_{k(s_{0})} k(s)$, and if $h_{s}$ is the
projection $X_{s} \to (X_{0})_{s_{0}}$, one has $Z_{s} = h^{-1}_{s}((Z_{0})_{s_{0}})$. Since the morphism $h_{s}$ is
faithfully flat and quasi-compact, the hypothesis that $Z_{s}$ is closed in $X_{s}$ entails that $(Z_{0})_{s_{0}}$ is
closed in $(X_{0})_{s_{0}}$ `(2.3.12)`.

This being so, the transitivity of fibres `(I, 3.6.4)` and proposition `(4.2.7)` entail that the set of dimensions of
the irreducible components of $Z_{s}$ containing $x$ is the same as the set of dimensions of the irreducible components
of $(Z_{0})_{s_{0}}$ containing $x_{0} = h_{s}(x)$. In particular, one has $\dim_{x}(Z_{s}) =
\dim_{x_{0}}((Z_{0})_{s_{0}})$. On the other hand, if $Z^{(\beta)}_{s}$ are the irreducible components of $Z_{s}$
containing $x$ and $X^{(\alpha)}_{s}$ the irreducible components of $X_{s}$

<!-- original page 89 -->

containing $x$, one has `codim_x(Z_s, X_s) = inf_β(sup_α(codim(Z_s^{(β)}, X_s^{(α)})))`, $(\alpha, \beta)$ varying over
the set of pairs such that $x \in Z^{(\beta)}_{s} \subset X^{(\alpha)}_{s}$ `(0, 14.2.6)`. Since irreducible algebraic
preschemes are biequidimensional `(5.2.1)`, one may write, by virtue of `(0, 14.3.3.1)`:

```text
(9.9.1.1)        codim_x(Z_s, X_s) = inf_β(sup_α(dim(X_s^{(α)}) − dim(Z_s^{(β)})))
```

with the same choice of pairs $(\alpha, \beta)$. Since $h_{s}$ is faithfully flat and quasi-compact, for every pair
formed of an irreducible component $(X_{0})^{(\alpha)}_{s_{0}}$ of $(X_{0})_{s_{0}}$ containing $x_{0}$ and of an
irreducible component $(Z_{0})^{(\beta)}_{s_{0}}$ of $(Z_{0})_{s_{0}}$ containing $x_{0}$ and contained in
$(X_{0})^{(\alpha)}_{s_{0}}$, there exists a pair $(X^{(\alpha)}_{s}, Z^{(\beta)}_{s})$ of the type described above and
such that $Z^{(\beta)}_{s}$ dominates $(Z_{0})^{(\beta)}_{s_{0}}$ and $X^{(\alpha)}_{s}$ dominates
$(X_{0})^{(\alpha)}_{s_{0}}$ `(2.3.5)`. Formula `(9.9.1.1)` (and the analogous formula applied to $(X_{0})_{s_{0}}$)
then show, by virtue of `(4.2.7)`, that one has

```text
                  codim_x(Z_s, X_s) = codim_{x_0}((Z_0)_{s_0}, (X_0)_{s_0}).
```

One sees thus that if $E$ (resp. `E_0`) is the set of $x \in X$ (resp. of $x_{0} \in X_{0}$) verifying one of the
conditions (i), (ii), (iii) of the statement (resp. the same condition), one has $E = h^{-1}(E_{0})$, and by virtue of
`(1.8.2)`, one sees that one may restrict to the case where $A$ is Noetherian, and hence so is $B$. Taking $(0_{III},
9.2.3)$ into account, as well as `(9.9.1.1)`, one is reduced to seeing that for every $x \in X$, there is a
neighbourhood $V$ of $x$ in $\overline{x}$ such that, for every $x' \in V$, the set of dimensions of the irreducible
components of $X_{f(x')}$ (resp. $Z_{f(x')}$) containing $x'$ is the same, and moreover that the same is true of the set
of pairs $(\dim(Z^{(\beta)}_{f(x')}), \dim(X^{(\alpha)}_{f(x')}))$ for pairs formed of an irreducible component
$X^{(\alpha)}_{f(x')}$ of $X_{f(x')}$ and an irreducible component $Z^{(\beta)}_{f(x')}$ of $Z_{f(x')}$ contained in
$X^{(\alpha)}_{f(x')}$ and containing $x'$. We may evidently for this replace $S$ by the reduced sub-prescheme $S'$ of
$S$ having $\overline{f(x)}$ as underlying space, and $X$ by $X' = f^{-1}(S')$, the fibres of $X$ and $X'$ at points of
$S'$ being the same. Otherwise put, we may restrict to the case where $S$ is integral and where $\eta = f(x)$ is its
generic point.

By hypothesis $Z_{\eta}$ is closed in $X_{\eta}$; since $Z$ is constructible, it follows from `(8.3.11)`, applied via
the method of `(8.1.2, a))`, that one may, by replacing $S$ if necessary by an open neighbourhood of $\eta$, suppose
that $Z$ is closed in $X$. Let $X_{i}$ (resp. $Z_{j}$) be the irreducible components of $X$ (resp. $Z$) containing $x$;
by virtue of $(0_{I}, 2.1.8)$, the $X_{i} \cap X_{\eta}$ (resp. $Z_{j} \cap X_{\eta}$) are the irreducible components of
$X_{\eta}$ (resp. $Z_{\eta}$) containing $x$; by virtue of `(9.5.1)`, we may further suppose, by restricting $S$ if
necessary to a neighbourhood of $\eta$, that the $X_{i}$ (resp. $Z_{j}$) are exactly the irreducible components of $X$
(resp. $Z$) meeting $\overline{x}$ and that the $(X_{i})_{s} \cap \overline{x}$ and $(Z_{j})_{s} \cap \overline{x}$ are
non-empty for every $s \in S$. This being so, it follows again from `(9.7.1)` that we may suppose, by restricting $S$,
that the pairs $(i, j)$ such that $(Z_{j})_{s} \subset (X_{i})_{s}$ are the same for every $s \in S$. The conclusion
then follows from `(9.5.6)`: for every $s$ sufficiently near $\eta$, all the irreducible components of $(X_{i})_{s}$
(resp. $(Z_{j})_{s}$) have the same dimension, equal to that of $(X_{i})_{\eta}$ (resp. $(Z_{j})_{\eta}$). Moreover, if
$(i, j)$ is a pair such that $Z_{j} \nsubset X_{i}$, $(X_{i})_{\eta}$ does not contain the

<!-- original page 90 -->

generic point of $(Z_{j})_{\eta}$, so $\dim((X_{i} \cap Z_{j})_{\eta}) < \dim((Z_{j})_{\eta})$; consequently, the common
dimension of the irreducible components of $(X_{i})_{s} \cap (Z_{j})_{s}$ is, for every $s \in S$, strictly less than
the common dimension of the irreducible components of $(Z_{j})_{s}$, which proves that none of the irreducible
components of $(Z_{j})_{s}$ is contained in an irreducible component of $(X_{i})_{s}$ for $s \in S$. Q.E.D.

**Proposition (9.9.2).**

<!-- label: IV.9.9.2 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation, $\Phi$ a finite part of $\mathbb{Z} \cup {\pm\infty}$. The following parts of $X$ are locally
constructible:*

*(i) The set of points $x \in X$ such that $\mathcal{F}_{f(x)}$ is equidimensional at the point $x$ `(5.1.12)`.*

*(ii) The set of $x \in X$ such that the geometric lengths of $\mathcal{F}_{f(x)}$ relative to $k(f(x))$, at the generic
points of the irreducible components of $Supp(\mathcal{F}_{f(x)})$ containing $x$ `(4.7.5)`, belong to $\Phi$.*

*(iii) The set of $x \in X$ such that the dimensions of the prime cycles associated to $\mathcal{F}_{f(x)}$ and
containing $x$ belong to $\Phi$.*

*(iv) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is geometrically reduced at the point $x$ `(4.6.17)`.*

*(v) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is geometrically integral at the point $x$ `(4.6.22)`.*

*(vi) The set of $x \in X$ such that $\dim. proj((\mathcal{F}_{f(x)})_{x}) \in \Phi$.*

*(vii) The set of $x \in X$ such that $coprof((\mathcal{F}_{f(x)})_{x}) \in \Phi$.*

*(viii) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ possesses property $(S_{k})$ at the point $x$ `(5.7.2)`.*

*(ix) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is a Cohen-Macaulay $\mathcal{O}_{X_{f(x)}}$-Module at the
point $x$ `(5.7.1)`.*

**(i)** The support $Z$ of $\mathcal{F}$ is locally constructible and closed in $X$ `(8.9.1)`, and considering a
sub-prescheme of $X$ having $Z$ as underlying space and which is of finite presentation over $S$ `(8.9.1)`, one sees
that assertion (i) is a special case of `(9.9.1, (iii))`.

**(ii)** All the properties considered are local on $X$, and we shall therefore restrict to the case where $X =
\operatorname{Spec}(B)$ and $S = \operatorname{Spec}(A)$ are affine and $f$ a morphism of finite presentation. We keep
the notations of the start of the proof of `(9.9.1)`, and moreover suppose `A_0` chosen so that there exists a coherent
$\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$ such that $\mathcal{F}$ is isomorphic to $\mathcal{F}_{0} \otimes_{A_{0}}
A$. Then (`(4.2.7)` and `(4.7.9)`) the set of geometric lengths of $(\mathcal{F}_{0})_{f(x_{0})}$ at the generic points
of the irreducible components of $Supp((\mathcal{F}_{0})_{f(x_{0})})$ which contain $x_{0}$ is the same as the analogous
set for $x$ and $\mathcal{F}_{f(x)}$; otherwise put, if $E$ (resp. `E_0`) is the set of $x \in X$ (resp. of $x_{0} \in
X_{0}$) verifying condition (ii) of the statement, one has $E = h^{-1}(E_{0})$, and by virtue of `(1.8.2)`, one sees
that one may restrict to considering the case where $A$ is Noetherian. As in the proof of `(9.9.1)`, one sees that one
is reduced to showing that, for every $x \in X$, there exists a neighbourhood $V$ of $x$ in $\overline{x}$ such that,
for every $x' \in V$, the set of geometric lengths of $\mathcal{F}_{f(x')}$ at the generic points of the irreducible
components of its support containing $x'$ is the same. Moreover, if $S'$ is the reduced sub-prescheme of $S$ having
$\overline{f(x)}$ as underlying space, and if $X' = f^{-1}(S')$, the fibres of $X$ and of $X'$ at points of $S'$ are the
same,

<!-- original page 91 -->

so we may replace $S$ by $S'$ and $X$ by $X'$, otherwise put suppose that $S$ is integral and that $\eta = f(x)$ is its
generic point.

Now, if one sets $Z = Supp(\mathcal{F})$, the same reasoning as in the proof of `(9.9.1)` shows that, if $Z_{i}$ are the
irreducible components of $Z$ containing $x$, one may suppose that these are exactly the irreducible components of $Z$
meeting $\overline{x}$ and that $(Z_{i})_{s} \cap \overline{x} \neq \emptyset$ for every $s \in S$. The conclusion then
follows from `(9.8.3)` and `(9.8.6)`.

**(iii)** One reduces as in (ii) to the case where $S$ is Noetherian and integral and $\eta = f(x)$ its generic point,
using `(4.2.7)`. As in the proof of `(9.9.1)`, one is reduced to showing that there exists a neighbourhood $V$ of $x$ in
$\overline{x}$ such that, for every $x' \in V$, the set of dimensions of the prime cycles associated to
$\mathcal{F}_{f(x')}$ which contain $x'$ is the same. Now, if $Z'_{i}$ are the closures in $X$ of the prime cycles
associated to $\mathcal{F}_{\eta}$ which contain $x$ (cf. `(9.8.2)`), it follows from `(9.8.3)` and `(9.5.1)` that for
every $s$ sufficiently near $\eta$, the prime cycles associated to $\mathcal{F}_{s}$ which meet $\overline{x}$ are
irreducible components of the $(Z'_{i})_{s}$ and, by virtue of `(9.5.6)`, all these irreducible components have the same
dimension equal to $\dim((Z'_{i})_{\eta})$, whence the conclusion.

**(iv)** One reasons as in (iii), using this time `(4.7.11)`. With the same notations as in (iii), the prime cycles
associated to $\mathcal{F}_{s}$ which are irreducible components of $(Z'_{i})_{s}$ are embedded if and only if
$(Z'_{i})_{\eta}$ is an embedded associated prime cycle of $\mathcal{F}_{\eta}$. One concludes already that if $x$
belongs to (resp. does not belong to any) embedded associated prime cycle of $\mathcal{F}_{\eta}$, the set of $x' \in
\overline{x}$ such that $x'$ belongs to (resp. does not belong to any) embedded associated prime cycle of
$\mathcal{F}_{f(x')}$ is a neighbourhood of $x$ in $\overline{x}$. The conclusion follows from this remark, from the
characterization of points where a Module is geometrically reduced `(4.7.10)`, and from (ii).

**(v)** Taking `(4.7.11)` into account, we reduce again to the case where $S$ is Noetherian and integral and where $\eta
= f(x)$ is its generic point. Let $Y$ be a closed sub-prescheme of $X$ having $Supp(\mathcal{F}_{\eta})$ as underlying
space. Reasoning as at the start of the proof of `(9.7.7)`, one sees that there exists an integral finite $A$-algebra
$A'$ (so that if $S' = \operatorname{Spec}(A')$, the morphism $S' \to S$ is finite and surjective) such that if $Y' =
Y_{(S')}$ and if $\eta'$ is the generic point of $S'$, the irreducible components of $Y'_{\eta'}$ are geometrically
irreducible. On the other hand, if $X' = X_{(S')}$, the projection morphism $h : X' \to X$ is finite and surjective,
hence closed; consequently, if $x'$ is a point of $X'$ above $x$, one has $h(\overline{x'}) = \overline{x}$ and the
image under $h$ of a neighbourhood of $x'$ in $\overline{x'}$ is a neighbourhood of $x$ in $\overline{x}$. Taking
`(4.7.11)` into account and setting $\mathcal{F}' = \mathcal{F}_{(S')}$, we are therefore reduced to proving that if
$\mathcal{F}'$ is (resp. is not) geometrically integral at the point $x'$, the set of $y' \in \overline{x'}$ such that
$\mathcal{F}'_{f'(y')}$ (where $f' = f_{(S')} : X' \to S'$) is (resp. is not) geometrically integral at the point $y'$
is a neighbourhood of $x'$ in $\overline{x'}$. We may therefore restrict to the case where $X' = X$ and where the
irreducible components of $Y_{\eta}$ are geometrically irreducible; if one denotes by $Z_{i}$ closed parts of $X$ such
that the $Z_{i} \cap X_{\eta}$ are the

<!-- original page 92 -->

irreducible components of $Y_{\eta}$, it follows from `(9.7.7)`, `(9.7.8)`, and `(9.5.3)` that for every $s$ near
$\eta$, the $(Z_{i})_{s}$ are the irreducible components of $Y_{s}$ and that they are geometrically irreducible. To say
that at a point $y \in X_{s}$, $\mathcal{F}_{s}$ is geometrically integral means then that $\mathcal{F}_{s}$ is
geometrically reduced at this point and moreover that $y$ belongs to only one of the $(Z_{i})_{s}$ `(4.6.22)`. The
conclusion therefore follows on the one hand from (iv) and on the other from `(9.5.1)` applied to the intersection of
$\overline{x}$ and each $Z_{i}$.

**(vi)** Keeping the same notations as in (ii), it follows from `(6.2.1)` that one has
`dim. proj((ℱ_s)_x) = dim. proj(((ℱ_0)_{s_0})_{x_0})`; one may therefore again restrict to the case where $A$ is
Noetherian. Moreover, one reduces again to showing that, for every $x \in X$, there exists a neighbourhood $V$ of $x$ in
$\overline{x}$ such that, for every $x' \in V$, one has `dim. proj((ℱ_{f(x')})_{x'}) = dim. proj((ℱ_{f(x)})_x)`; and as
above, we may suppose that $S$ is integral and that $\eta = f(x)$ is its generic point, so that one has
$(\mathcal{F}_{\eta})_{x} = \mathcal{F}_{x}$. By virtue of the generic flatness theorem `(6.9.1)`, we may, by replacing
$S$ if necessary by an open neighbourhood of $\eta$, suppose that the morphism $f$ is flat and that $\mathcal{F}$ is
$f$-flat; one then has `dim. proj((ℱ_{f(x')})_{x'}) = dim. proj(ℱ_{x'})` for every $x' \in X$ by virtue of `(6.2.3)`.
This being so, by virtue of `(6.11.1)`, we may (by replacing $X$ if necessary by an open neighbourhood of $x$) suppose
that `dim. proj(ℱ_{x'}) ≤ dim. proj(ℱ_x)` for every $x' \in X$. On the other hand, if $\dim. proj(\mathcal{F}_{x}) = n$,
there is by hypothesis a finitely generated $\mathcal{O}_{x}$-module $M$ such that
$Ext^{n}_{\mathcal{O}_{x}}(\mathcal{F}_{x}, M) \neq 0$ `(0, 17.2.4)`. Now, there exists a coherent
$\mathcal{O}_{X}$-Module $\mathcal{G}$ such that $M = \mathcal{G}_{x}$ (by replacing $X$ if necessary by an open
neighbourhood of $x$ $(0_{I}, 5.3.8)$); by virtue of `(T, 4.2.2)`, one therefore has
$(\mathcal{E}\mathcal{xt}^{n}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))_{x} \neq 0$. But
$\mathcal{E}\mathcal{xt}^{n}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ is a coherent $\mathcal{O}_{X}$-Module
$(0_{III}, 12.3.3)$, so its support $Y$ is closed $(0_{I}, 5.2.2)$; since it contains $x$, it also contains
$\overline{x}$, from which one concludes (by applying `(T, 4.2.2)` again) that one has $\dim. proj(\mathcal{F}_{x'})
\geq n$ for every $x' \in \overline{x}$, which completes the proof of the assertion in case (vi).

**(vii)** Since $B$ is a finitely generated $A$-algebra, $X$ is $S$-isomorphic to a closed sub-scheme of an $S$-scheme
of the form $Y = \operatorname{Spec}(A[T_{1}, \cdots, T_{r}])$; if $j : X \to Y$ is the canonical injection, and
$\mathcal{G} = j_{*}(\mathcal{F})$, one has $\mathcal{G}_{s} = (j_{s})_{*}(\mathcal{F}_{s})$ for every $s \in S$, and,
by virtue of `(0, 16.4.11)`, we may restrict to proving the assertion for $Y$ and $\mathcal{G}$. Otherwise put, we may
suppose that $B = A[T_{1}, \cdots, T_{r}]$, so that each of the schemes $X_{s} = \operatorname{Spec}(k(s)[T_{1}, \cdots,
T_{r}])$ is regular `(0, 17.3.7)`. Let then $W = Supp(\mathcal{F})$, so that $W_{s} = Supp(\mathcal{F}_{s})$
`(I, 9.1.13)`; one has, by `(6.11.2.1)`:

```text
(9.9.2.1)     coprof((ℱ_{f(x)})_x) = dim. proj((ℱ_{f(x)})_x) − codim_x(W_{f(x)}, X_{f(x)}).
```

But since $W$ is constructible `(8.9.1)` and each $W_{s}$ is closed, it follows from (vi) and from `(9.9.1, (ii))` that
the two functions in the right-hand side of `(9.9.2.1)` are constructible; the same is therefore true of their
difference, which completes the proof of the proposition in case (vii).

**(viii)** Let $U_{n}$ be the set of $x \in X$ such that $coprof((\mathcal{F}_{f(x)})_{x}) \leq n$, and set $Z_{n} = X -
U_{n}$; it follows from (vii) that the $Z_{n}$ are constructible; moreover, since the function

<!-- original page 93 -->

$x \mapsto \dim_{x}(W_{f(x)})$ is constructible by virtue of `(9.9.1, (i))`, it takes only finitely many values, hence
the numbers $\dim(W_{f(x)})$ have a finite upper bound $m$ as $x$ ranges over $X$; since
`coprof((ℱ_{f(x)})_x) ≤ dim((ℱ_{f(x)})_x) ≤ dim(W_{f(x)})`, one sees that $Z_{n} = \emptyset$ for $n \geq m$. Finally,
it follows from `(6.11.2, (i))` that for every $n$ and every $s \in S$, $(Z_{n})_{s}$ is closed in $X_{s}$. According to
`(5.7.4)`, the set of $x \in X$ where $(\mathcal{F}_{f(x)})_{x}$ possesses property $(S_{k})$ is the set of $x \in X$
verifying all the relations

```text
(9.9.2.2)               codim_x((Z_n)_{f(x)}, W_{f(x)}) ≥ n + k
```

for every $n \geq 0$; since this relation is automatically verified for $n \geq m$, one only has to consider relations
`(9.9.2.2)` for $0 \leq n < m$. But by virtue of `(9.9.1, (ii))`, the set $V_{n,k}$ of $x$ verifying `(9.9.2.2)` is
constructible, and the same is true of the intersection of these sets for $0 \leq n < m$.

**(ix)** The assertion here follows at once from (vii), the set of $x \in X$ where $(\mathcal{F}_{f(x)})_{x}$ is a
Cohen-Macaulay module being defined by the relation $coprof((\mathcal{F}_{f(x)})_{x}) = 0$.

**Corollary (9.9.3).**

<!-- label: IV.9.9.3 -->

*Let $f : X \to S$ be a morphism of finite presentation, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module of finite
presentation, $P$ one of the properties (i) to (ix) of `(9.9.2)`. Then the set of $s \in S$ such that property $P$ is
true at every point $x \in X_{s}$ is locally constructible in $S$.*

Indeed, its complement is the image under $f$ of the complement of the set $E$ of points where $P$ is true. Since $E$ is
locally constructible in $X$, the same is true of $X - E$, hence $f(X - E)$ is locally constructible in $S$ by virtue of
Chevalley's theorem `(1.8.4)`.

**Proposition (9.9.4).**

<!-- label: IV.9.9.4 -->

*Let $f : X \to S$ be a morphism locally of finite presentation.*

*The set of $x \in X$ such that $X_{f(x)}$ has at the point $x$ one (a fixed one) of the following properties:*

*(i) being geometrically regular;*

*(ii) possessing the geometric property $(R_{k})$;*

*(iii) being geometrically normal;*

*(iv) being geometrically reduced (i.e. separable);*

*(v) being geometrically pointwise integral;*

*is a locally constructible part of $X$.*

For properties (iv) and (v), this follows from `(9.9.2, (iv)` and `(v))` applied to $\mathcal{F} = \mathcal{O}_{X}$. For
the other properties, taking `(6.7.8)` into account, one reduces, as at the start of `(9.9.2)`, to the case where $S$ is
Noetherian and integral with generic point $\eta = f(x)$. Moreover, by virtue of the generic flatness theorem `(6.9.1)`,
we may, by replacing $S$ by an open neighbourhood of $\eta$, suppose that $f$ is a flat morphism. To say that $X_{f(y)}$
is geometrically regular at the point $y$ means then that $f$ is regular at the point $y$ `(6.8.1)`, and we know that
the set $L$ of these points is open in $X$ `(6.8.7)`, which proves the proposition in case (i).

To prove case (ii), set $F = X - L$, which is closed in $X$. To say that $X_{s}$

<!-- original page 94 -->

verifies the geometric property $(R_{k})$ at the point $y \in f^{-1}(s)$ means either that $y \in L$, or that the
generic points $z_{i}$ of the irreducible components of the closed set $F_{s}$ which contain $y$ verify the relation
$\dim(\mathcal{O}_{X_{s}, z_{i}}) \geq k + 1$ (taking `(4.2.7)` and `(5.2.3)` into account); otherwise put, the points
$y \in F_{s}$ where $X_{s}$ verifies the geometric property $(R_{k})$ are those such that $codim_{y}(F_{s}, X_{s}) \geq
k + 1$ `(5.1.2)`. The conclusion therefore follows from (i) and from `(9.9.1, (ii))`.

Finally, in case (iii), the conclusion follows from (ii), from `(9.9.2, (viii))`, from the fact that property $(S_{k})$
is stable under extension of the base field `(6.7.1)`, and finally from Serre's criterion `(5.8.6)`.

**Corollary (9.9.5).**

<!-- label: IV.9.9.5 -->

*Let $f : X \to S$ be a morphism of finite presentation, and denote by $P$ one of the properties (i) to (v) of
`(9.9.4)`. Then the set of $s \in S$ such that property $P$ is true at every point $x \in X_{s}$ is locally
constructible in $S$.*

The proof from `(9.9.4)` is the same as that of `(9.9.3)` from `(9.9.2)`.

**Proposition (9.9.6).**

<!-- label: IV.9.9.6 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $\mathcal{L}_{\bullet}$ a complex formed of
quasi-coherent $\mathcal{O}_{X}$-Modules of finite presentation; for every $s \in S$, let $(\mathcal{L}_{\bullet})_{s}$
be the complex $\mathcal{L}_{\bullet} \otimes k(s)$ of $\mathcal{O}_{X_{s}}$-Modules of finite type. Then, for a given
integer $n$, the set of $x \in X$ such that $(\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{f(x)}))_{x} = 0$ is locally
constructible in $X$.*

We may restrict to the case where $\mathcal{L}_{i} = 0$ except for $i = 0$, `1`, or `2`, and where $n = 1$. Moreover,
the question being local on $X$, we may restrict to the case where $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine, $B$ being an $A$-algebra of finite presentation. There then exists a Noetherian
subring `A_0` of $A$, an `A_0`-prescheme of finite type `X_0`, and a complex $\mathcal{L}^{(0)}_{\bullet}$ of coherent
$\mathcal{O}_{X_{0}}$-Modules, zero except in dimensions `0`, `1`, and `2`, such that $X = X_{0} \otimes_{A_{0}} A$ and
$\mathcal{L}_{\bullet} = \mathcal{L}^{(0)}_{\bullet} \otimes_{A_{0}} A$. For every $s \in S$, if $s_{0}$ is the
projection of $s$ in $S_{0} = \operatorname{Spec}(A_{0})$, one has $X_{s} = (X_{0})_{s_{0}} \otimes_{k(s_{0})} k(s)$,
and the projection morphism $X_{s} \to (X_{0})_{s_{0}}$ is faithfully flat; one concludes that one has
$\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{s}) = \mathcal{H}_{n}((\mathcal{L}^{(0)}_{\bullet})_{s_{0}})
\otimes_{k(s_{0})} k(s)$, and consequently, if $E$ (resp. `E_0`) is the set of $x \in X$ (resp. $x_{0} \in X_{0}$) such
that $(\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{f(x)}))_{x} = 0$ (resp.
$(\mathcal{H}_{n}((\mathcal{L}^{(0)}_{\bullet})_{f(x_{0})}))_{x_{0}} = 0$), one has $E = h^{-1}(E_{0})$, where $h : X
\to X_{0}$ is the canonical projection. By virtue of `(1.8.2)`, we may therefore restrict to the case where $A$ is
Noetherian; the question is to see $(0_{III}, 9.2.3)$ that if $x \in X$ is such that
$(\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{f(x)}))_{x} = 0$ (resp. $\neq 0$), there exists an open neighbourhood $V$ of
$x$ in $\overline{x}$ such that, for every $x' \in V$, one has $(\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{f(x')}))_{x'}
= 0$ (resp. $\neq 0$). Replacing $S$ by the reduced sub-prescheme of $S$ having $\overline{f(x)}$ as underlying space,
we may suppose that $S$ is integral and that $f(x) = \eta$ is its generic point. Then, by restricting $S$ to an open
neighbourhood of $\eta$, we may suppose that for every $s \in S$, one has $(\mathcal{H}_{n}(\mathcal{L}_{\bullet}))_{s}
= \mathcal{H}_{n}((\mathcal{L}_{\bullet})_{s})$ `(9.4.3)`, and consequently, if $Z$ is the support of
$\mathcal{H}_{n}(\mathcal{L}_{\bullet})$, the support of $\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{s})$ is $Z_{s} = Z
\cap X_{s}$ `(I, 9.1.13.1)`. The hypothesis is that $Z_{\eta} \cap \overline{x} = \emptyset$ (resp. $\neq \emptyset$).
Since $Z \cap \overline{x}$ is closed in the Noetherian space $X$, one concludes from `(9.5.1)` that there is a
neighbourhood $U$ of $\eta$ in $S$ such that, for every $s \in U$, one has $Z_{s} \cap \overline{x} = \emptyset$ (resp.
$\neq \emptyset$). The set $V = f^{-1}(U) \cap \overline{x}$ therefore answers the question.
