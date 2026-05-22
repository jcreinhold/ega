<!-- original page 173 -->

## §12. Study of the fibres of flat morphisms of finite presentation

### 12.0. Introduction

Throughout this section we shall use the general notations of `(9.4.1)`.

**(12.0.1)**

<!-- label: IV.12.0.1 -->

Given a morphism $f : X \to Y$ locally of finite presentation, we saw `(9.9)` that for certain *local* properties $P$ of
preschemes over fields or of Modules on such preschemes, the set $E$ of $x \in X$ such that the property $P$ holds for
the fibre $X_{f(x)}$ at the point $x$ of that fibre is locally constructible in $X$. We propose to show that, for most
of these properties, if one supposes moreover that the morphism $f$ is *flat*, then the set $E$ is even *open* in $X$.
Likewise (`(9.2)` through `(9.8)`) we have shown that if $f$ is of finite presentation, and if this time $P$ denotes
certain *global* properties of preschemes over fields or of Modules on such preschemes, then the set $F$ of $y \in Y$
such that the property $P$ holds for the fibre $X_{y}$ is locally constructible in $Y$. We shall show that if one
supposes moreover that the morphism $f$ is *proper and flat*, then $F$ is even *open* in $Y$.

**(12.0.2)**

<!-- label: IV.12.0.2 -->

The general method of proof of the properties in question comprises three steps. One first reduces to the case where $Y$
is affine and $X$ of finite presentation; then:

A) Using `(8.9.1)` (and possibly other results of §8) and `(11.2.6)`, one reduces to the case where $X$ and $Y$ are
Noetherian.

B) One applies the results of §9 recalled in `(12.0.1)` proving that $E$ (resp. $F$) is constructible.

C) To see that $E$ is open, it suffices, by virtue of $(0_{III}, 9.2.5)$, to show that if $x \in E$, then every
generization $x'$ of $x$ also belongs to $E$. Using `(II, 7.1.7)`, one sees, since $Y$ is Noetherian, that there exists
a spectrum of a discrete valuation ring `Y_1` and a morphism $h : Y_{1} \to X$ such that, if $y_{1}$ (resp. $y'_{1}$) is
the closed point (resp. the generic point) of `Y_1`, one has $h(y_{1}) = x$, $h(y'_{1}) = x'$. One then makes the base
change $g = f \circ h : Y_{1} \to Y$; taking into account the results of §§4 and 6 on locally Noetherian preschemes over
fields and changes of base field, one is reduced to proving the assertion in question for a point $x_{1}$ of $X_{1} = X
\times_{Y} Y_{1}$ above $y_{1}$ and for a generization $x'_{1}$ of $x_{1}$ above $y'_{1}$. Since $Y_{1} =
\operatorname{Spec}(A)$, where $A$ is a discrete valuation ring with uniformizer $t$, one must in the end, for an
$A$-module $M$, prove a property of $M$, knowing that $M/tM$ has the same property and that $t$ is $M$-regular (which
follows from the flatness hypothesis); for this one uses the results of `(3.4)` and `(5.12)`. One proceeds in the same
way for the set $F \subset Y$.

<!-- original page 174 -->

### 12.1. Local properties of the fibres of a flat morphism locally of finite presentation

**Theorem (12.1.1).**

<!-- label: IV.12.1.1 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module that is
$f$-flat and of finite presentation, $\Phi$ a finite subset of $\mathbb{Z} \cup {\pm\infty}$, $k$ an integer. The
following subsets of $X$ are open:*

*(i) The set of $x \in X$ such that the dimensions of the associated prime cycles of $\mathcal{F}_{f(x)}$ containing $x$
are elements of $\Phi$.*

*(ii) The set of $x \in X$ such that the associated prime cycles of $\mathcal{F}_{f(x)}$ containing $x$ all have
dimension $k$.*

*(iii) The set of $x \in X$ such that $x$ belongs to no embedded associated prime cycle of $\mathcal{F}_{f(x)}$.*

*(iv) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is equidimensional at the point $x$ and possesses property
$(S_{k})$ at the point $x$ `(5.7.2)`.*

*(v) The set of $x \in X$ such that $coprof((\mathcal{F}_{f(x)})_{x}) \leq k$ `(0, 16.4.9)`.*

*(vi) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is a Cohen-Macaulay $\mathcal{O}_{X}$-Module at the point $x$
`(5.7.1)`.*

*(vii) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is geometrically reduced at the point $x$ `(4.6.22)`.*

*(viii) The set of $x \in X$ such that $\mathcal{F}_{f(x)}$ is geometrically pointwise integral at the point $x$
`(4.6.22)`.*

The questions being local on $X$, one reduces first to the case where $X = \operatorname{Spec}(B)$ and $Y =
\operatorname{Spec}(A)$ are affine, with $f$ a morphism of finite presentation. There then exists a Noetherian sub-ring
`A_0` of $A$, an `A_0`-prescheme of finite type `X_0`, and a coherent $\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$
such that $\mathcal{F}_{0} \otimes_{A_{0}} A$ is isomorphic to $\mathcal{F}$ `(8.9.1)`; in addition, by virtue of
`(11.2.6)`, one may suppose that $\mathcal{F}_{0}$ is `Y_0`-flat (with $Y_{0} = \operatorname{Spec}(A_{0})$). If $h : X
\to X_{0}$ is the canonical projection, the set $E$ of points $x \in X$ where one of properties (i) to (viii) holds is
equal to $h^{-1}(E_{0})$, where `E_0` is the set of $x_{0} \in X_{0}$ where the corresponding property for
$\mathcal{F}_{0}$ holds: this follows, for properties (i) to (iii), from `(4.2.7)`; for properties (iv) to (vi), from
`(6.7.1)`; for properties (vii) and (viii), from `(4.7.11)`.

One is thus reduced to the case where $A$ and $B$ are Noetherian, $f$ of finite type, and $\mathcal{F} = \tilde{M}$,
where $M$ is a $B$-module of finite type. By virtue of `(9.9.2)`, one knows that the set $E$ is constructible for all
the properties considered, and there remains in each case step C) of `(12.0.2)`, where one must prove that $E$ is stable
under generization.

**(12.1.1.1)**

<!-- label: IV.12.1.1.1 -->

Let us begin with case (iii), which is the simplest. Let $x' \neq x$ be a generization of $x$ in $X$. Set $y = f(x)$,
$y' = f(x')$; there exists a spectrum of a discrete valuation ring `Y_1` and a morphism $u : Y_{1} \to X$ such that, if
$y_{1}$ and $y'_{1}$ are the closed point and the generic point of `Y_1`, one has $u(y_{1}) = x$ and $u(y'_{1}) = x'$
`(II, 7.1.7)`; set $g = f \circ u : Y_{1} \to Y$; if $X_{1} = X \times_{Y} Y_{1}$, there exists a `Y_1`-section $u_{1} :
Y_{1} \to X_{1}$ such that $u = g_{1} \circ u_{1}$, where $g_{1} : X_{1} \to X$ is the canonical projection. Setting
$x_{1} = u_{1}(y_{1})$, $x'_{1} = u_{1}(y'_{1})$, one therefore has $g_{1}(x_{1}) = x$ and $g_{1}(x'_{1}) = x'$, and
$x'_{1}$ is a generization of $x_{1}$. Applying `(4.2.7)` again, one sees

<!-- original page 175 -->

that one is reduced to the case where $Y = \operatorname{Spec}(A)$ is the spectrum of a discrete valuation ring, $y$
being the closed point and $y'$ the generic point of $Y$. If $t$ is a uniformizer of $A$, the hypothesis that
$\mathcal{F}$ is $f$-flat entails that $t$ is $\mathcal{F}$-regular $(0_{I}, 6.3.4)$. By hypothesis none of the embedded
associated prime cycles of $\mathcal{F}/t\mathcal{F}$ contains $x$. Then, it follows from `(3.4.4)` that $x$ belongs to
no embedded associated prime cycle of $\mathcal{F}$, and the same is therefore true of every generization of $x$. In
particular, $x'$ belongs to no embedded associated prime cycle of $\mathcal{F}$, nor *a fortiori* to any of those
associated to $\mathcal{F}_{y'}$ ($X_{y'}$ being a sub-prescheme induced on an open set of $X$).

**(12.1.1.2)**

<!-- label: IV.12.1.1.2 -->

Let us consider next cases (iv) and (v) ((vi) is only a special case of (v)). One proceeds as above (using `(6.7.1)`
instead of `(4.2.7)`) and one is reduced to the case where $Y$ is the spectrum of a discrete valuation ring $A$.

The ring $C = \mathcal{O}_{X, x}$ is then a localization of a finitely generated $A$-algebra, hence catenary `(5.6.4)`,
and by hypothesis the $C$-module $M_{x}/tM_{x}$ satisfies $(S_{k})$ and is equidimensional (resp. one has
$coprof(M_{x}/tM_{x}) \leq k$); one therefore deduces from `(5.12.2)` (resp. from `(0, 16.4.10)`) that $M_{x}$ satisfies
$(S_{k})$ and is equidimensional (resp. that $coprof(M_{x}) \leq k$), since $t$ is $M_{x}$-regular and belongs to the
maximal ideal of $C$. Whence the conclusions, since $x'$ is a generization of $x$ and $(\mathcal{F}_{y'})_{x'} =
\mathcal{F}_{x'}$.

**(12.1.1.3)**

<!-- label: IV.12.1.1.3 -->

Let us pass to cases (vii) and (viii). One may evidently replace $Y$ by the integral sub-scheme having $\overline{y}$ as
underlying space, and $X$ by $f^{-1}(\overline{y})$, without changing the fibres at $y$ and $y'$; one may therefore
suppose $A$ integral, with field of fractions $K = k(y)$. One knows (`(4.5.11)` and `(4.7.8)`) that there exists a
finite extension $K'$ of $K$ such that, for the $(\mathcal{O}_{X} \otimes_{A} K')$-Module $\mathcal{F}' = \mathcal{F}
\otimes_{A} K'$, the associated prime cycles are geometrically irreducible and the geometric lengths of $\mathcal{F}'$
at the maximal points $z'$ of its support are respectively equal to the lengths of $\mathcal{F}'_{z'}$ at these points;
it therefore amounts to the same to say that $\mathcal{F}$ is geometrically reduced (resp. geometrically pointwise
integral) at a point $x'$ of $X_{y'} = X \otimes_{A} K$, or to say that $\mathcal{F}'$ is reduced (resp. integral) at
the points of $X \otimes_{A} K'$ above $x'$, taking `(4.2.7)` into account. Let $A'$ be a finite $A$-algebra of which
$K'$ is the field of fractions; it follows from `(4.7.11)` that at every point of $X \otimes_{A} A'$ above $x$,
$\mathcal{F} \otimes_{A} A'$ has property (vii) (resp. (viii)). Replacing $A$ by $A'$ and $X$ by $X \otimes_{A} A'$, one
sees that one may confine oneself to proving that $\mathcal{F}_{x}$ is reduced (resp. integral) at every generization
$x'$ of $x$. One then proceeds as in `(12.1.1.1)`, this time using `(4.7.11)`, and one is once again reduced to the case
where $A$ is a discrete valuation ring, $y$ being the closed point and $y'$ the generic point of $Y$, with the
uniformizer $t$ of $A$ being an $\mathcal{F}$-regular element. Since by hypothesis $\mathcal{F}/t\mathcal{F}$ is reduced
(resp. integral) at the point $x$, it follows from `(3.4.6)` (resp. `(3.4.5)`) that $\mathcal{F}$ is reduced (resp.
integral) at the point $x$, hence also in a neighbourhood of $x$, and in particular at the point $x'$, which completes
the proof in cases (vii) and (viii).

**(12.1.1.4)**

<!-- label: IV.12.1.1.4 -->

It remains to examine cases (i) and (ii). Replacing $Y$ by the integral sub-scheme having $\overline{y}$ as underlying
space, one may confine oneself to the case where $Y$ is irreducible and $y$ its generic point. Let $z'$ be a generic
point of an associated prime cycle of $\mathcal{F}_{y'}$

<!-- original page 176 -->

containing $x'$, and let $Z'$ be the closure of $z'$ in $X$, so that one has $x \in Z'$. To treat case (i), it will
suffice to prove:

**Proposition (12.1.1.5).**

<!-- label: IV.12.1.1.5 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module that is $f$-flat; for every $y \in Y$, set $\mathcal{F}_{y} = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} k(y)$. Let $z'$ be a point of $X$, $y' = f(z')$, and suppose that $z' \in
Ass(\mathcal{F}_{y'})$. Let $Z'$ (resp. $Y'$) be the reduced sub-prescheme of $X$ (resp. $Y$) having as underlying space
the closure of `{z'}` in $X$ (resp. of `{y'}` in $Y$). Then, for every $y \in f(Z')$, the dimensions of all the
irreducible components of $Z'_{y}$ are equal to $\dim(Z'_{y'})$ (the dimension of the closure of $z'$ in $X_{y'}$)
(which we shall express later `(13.2.2)` by saying that the restriction $Z' \to Y'$ of $f$ is an **equidimensional
morphism**); moreover, at every maximal point $z$ of $Z'_{y}$, one has $z \in Ass(\mathcal{F}_{y})$.*

For this, we shall reduce to the case where $Y$ is the spectrum of a discrete valuation ring. Take a spectrum of a
discrete valuation ring `Y_1` and a morphism $h : Y_{1} \to X$ such that $h(y_{1}) = z$, $h(y'_{1}) = z'$, where $y_{1}$
and $y'_{1}$ are the closed point and the generic point of `Y_1` respectively `(II, 7.1.7)`. Let $g = f \circ h : Y_{1}
\to Y$, $X_{1} = X \times_{Y} Y_{1}$, and let $f_{1} : X_{1} \to Y_{1}$, $g_{1} : X_{1} \to X$ be the canonical
projections; there is a `Y_1`-section $h_{1} : Y_{1} \to X_{1}$ such that $h = g_{1} \circ h_{1}$ `(I, 3.3.14)`. If
$Z'_{1} = Z'_{y'} \otimes_{k(y')} k(y'_{1})$, one knows `(4.2.6)` that the irreducible components of $Z'_{1}$ dominate
$Z'_{y'}$; let $z'_{1}$ be the generic point of one of these components which contains $h_{1}(y'_{1})$, so that
$f_{1}(z'_{1}) = y'_{1}$ and $g_{1}(z'_{1}) = z'$. Since $h_{1}(y_{1})$ is a specialization of $h_{1}(y'_{1})$, it is *a
fortiori* a specialization of $z'_{1}$; let $z_{1}$ be a generic point of one of the irreducible components of
$\overline{z'_{1}} \cap (X_{1})_{y_{1}}$ containing $h_{1}(y_{1})$. Then $g_{1}(z_{1})$ is a specialization of
$g_{1}(z'_{1}) = z'$ in $X$, and $z = h(y_{1}) = g_{1}(h_{1}(y_{1}))$ is a specialization of $g_{1}(z_{1})$; but since
$f(g_{1}(z_{1})) = y$ and $z$ is a generic point of $Z'_{y}$, one necessarily has $z = g_{1}(z_{1})$.

Suppose now that one has proved that, if one sets $\mathcal{F}_{1} = \mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{O}_{Y_{1}}$, one has $z_{1} \in Ass((\mathcal{F}_{1})_{y_{1}})$; it will follow from `(4.2.7)` that $z \in
Ass(\mathcal{F}_{y})$; moreover, the dimensions of $\overline{z_{1}} \cap (X_{1})_{y_{1}}$ and of $\overline{z} \cap
X_{y}$ are equal, and likewise the dimensions of $\overline{z'_{1}} \cap (X_{1})_{y'_{1}}$ and of $\overline{z'} \cap
X_{y'}$ `(4.2.7)`; one has therefore indeed reduced, as announced, to the case where $Y$ is the spectrum of a discrete
valuation ring $A$, $y$ and $y'$ being its closed point and its generic point respectively.

This being so, since $z_{1} \in Ass((\mathcal{F}_{1})_{y_{1}})$, one has *a fortiori* $z' \in Ass(\mathcal{F})$. If $t$
is a uniformizer of $A$, $t$ is $\mathcal{F}$-regular by flatness, hence `(3.4.3)` one has $z \in
Ass(\mathcal{F}/t\mathcal{F}) = Ass(\mathcal{F}_{y})$. As for the assertion concerning dimensions, it follows from
`(7.1.13)`, applied to a closed sub-prescheme of $X$ having $Z'$ as underlying space.

Let us tackle finally case (ii) of `(12.1.1)`. With the same notation, one must prove that if all the associated prime
cycles of $\mathcal{F}_{y}$ containing $x$ have dimension $k$, then the same is true of all the associated prime cycles
of $\mathcal{F}_{y'}$ containing $x'$. Now we have just seen that every associated prime cycle of $\mathcal{F}_{y'}$
containing $x'$ has the same dimension as one of the associated prime cycles of $\mathcal{F}_{y}$ containing $x$; this
therefore proves (ii).

**Remarks (12.1.2).**

<!-- label: IV.12.1.2 -->

*(i) Under the conditions of `(12.1.1.5)` with $\mathcal{F} = \mathcal{O}_{X}$ (so that $f$ is flat), one cannot in
general assert that the restriction $Z' \to Y'$ of $f$ is a flat morphism, nor even an open morphism. This is what the
example* \`(6.5.5,\*

<!-- original page 177 -->

*(ii))`*shows, where one takes for`Z'`one of the two irreducible components of`X =
Spec(B)`. It is immediate that this restriction morphism is not open at the points of`Z'`above the "double point" of`Y'
= Y\`.*

*(ii) In the hypotheses of `(12.1.1.5)`, with $\mathcal{F} = \mathcal{O}_{X}$, one cannot weaken the condition "$f$ is
flat" to "$f$ is universally open" (cf. `(2.4.6)`), as we shall see later from an example `(14.4.10, (i))`.*

**Corollary (12.1.3).**

<!-- label: IV.12.1.3 -->

*Under the hypotheses of `(12.1.1)`, the function $x \mapsto coprof((\mathcal{F}_{f(x)})_{x})$ is upper semi-continuous
in $X$ and the function $x \mapsto prof_{x}(\mathcal{F}_{x})$ `(10.8.1)` is lower semi-continuous in $X$.*

The first assertion is none other than an equivalent formulation of `(12.1.1, (v))`. To prove the second, one may first,
taking `(10.8.7)` and `(10.8.8)` into account, reduce as in `(12.1.1)` to the case where $Y$ is the spectrum of a
discrete valuation ring $A$ with closed point $y$ and generic point $y'$, with $X = \operatorname{Spec}(B)$ affine,
$\mathcal{F} = \tilde{M}$, where $M$ is a $B$-module of finite type. Since $\mathcal{F}$ is $f$-flat, every irreducible
component of $Supp(\mathcal{F})$ that contains $x \in X_{y}$ dominates $Y$ `(2.3.4)`, in other words its generic point
$z'$ belongs to $X_{y'}$; the irreducible components $Z$ of $Supp(\mathcal{F})$ that contain a generization $x'$ of $x$
belonging to $X_{y'}$ are therefore exactly those that contain $x$, and moreover, by `(12.1.1.5)`, one has $\dim(Z_{y'})
= \dim(Z_{y})$, whence, if $T = Supp(\mathcal{F})$, $\dim_{x}(T_{y}) = \dim_{x'}(T_{y'})$. In addition, for a
uniformizer $t$ of $A$, one saw in `(12.1.1, (v))` that one has $coprof(M_{x}) = coprof(M_{x}/tM_{x})$, and since on the
other hand $coprof(M_{x'}) \leq coprof(M_{x})$ `(6.11.5)`, one sees that one has $coprof_{x'}(\mathcal{F}_{y'}) \leq
coprof_{x}(\mathcal{F}_{y})$; the relation $prof_{x'}(\mathcal{F}_{y'}) \geq prof_{x}(\mathcal{F}_{y})$ then follows
from `(10.8.7)`.

**Remark (12.1.4).**

<!-- label: IV.12.1.4 -->

*One also deduces from `(12.1.1, (i))` that the function $x \mapsto \dim_{x}(X_{f(x)})$ is upper semi-continuous in $X$,
but we shall see later `(13.1.3)` that this property is true even without supposing $f$ flat.*

**Corollary (12.1.5).**

<!-- label: IV.12.1.5 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module that is $f$-flat, $\mathcal{G}$ a coherent $\mathcal{O}_{Y}$-Module, $x$ a point of $X$, $y =
f(x)$. Suppose that $\mathcal{G}$ has property $(S_{k})$ at the point $y$, and that $\mathcal{F}_{y}$ has property
$(S_{k})$ at the point $x$ and is equidimensional at the point $x$. Then:*

*(i) $\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G}$ possesses property $(S_{k})$ at the point $x$.*

*(ii) If moreover $Y$ is locally immersible in a regular scheme, or is an excellent prescheme `(7.8.5)`, there exists a
neighbourhood of $x$ in $X$ such that $\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G}$ has property $(S_{k})$ in this
neighbourhood.*

Indeed, by `(12.1.1, (iv))`, there exists an open neighbourhood $V$ of $x$ such that for every $x' \in V$,
$\mathcal{F}_{f(x')}$ satisfies $(S_{k})$ at the point $x'$. On the other hand, $\mathcal{G}$ satisfies $(S_{k})$ at
every point of $Y' = \operatorname{Spec}(\mathcal{O}_{y})$ `(5.7.2)`. Replacing $Y$ by $Y'$ and $X$ by $V \times_{Y}
Y'$, one is reduced (taking `(I, 3.6.5)` into account) to the case where $\mathcal{G}$ satisfies $(S_{k})$ in $Y$
entirely and where, for every $y \in f(X)$, $\mathcal{F}_{y}$ possesses property $(S_{k})$ at every point of
$f^{-1}(y)$; since $\mathcal{F}$ is $f$-flat, one then knows `(6.4.1)` that $\mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{G}$ possesses property $(S_{k})$ in $X$, which proves (i). To prove (ii), it suffices to observe that, under
the hypotheses made, $\mathcal{G}$ possesses

<!-- original page 178 -->

property $(S_{k})$ in a neighbourhood $U$ of $y$ in $Y$ (`(6.11.2)` and `(7.8.3, (iv))`); one then concludes in the same
way, replacing this time $Y$ by $U$ and $X$ by $V \times_{Y} U$.

**Theorem (12.1.6).**

<!-- label: IV.12.1.6 -->

*Let $f : X \to Y$ be a flat morphism locally of finite presentation, $k$ an integer. The following subsets of $X$ are
open:*

*(i) The set of points $x \in X$ such that $X_{f(x)}$ satisfies property $(S_{k})$ at the point $x$.*

*(ii) The set of $x \in X$ such that $X_{f(x)}$ satisfies geometric property $(R_{k})$ at the point $x$, is
equidimensional at the point $x$, and moreover $x$ belongs to no embedded associated prime cycle of $X_{f(x)}$.*

*(iii) The set of $x \in X$ such that $X_{f(x)}$ is geometrically regular (i.e. smooth) at the point $x$.*

*(iv) The set of $x \in X$ such that $X_{f(x)}$ is geometrically normal at the point $x$.*

Steps A) and B) of `(12.0.2)` are carried out here as in `(12.1.1)`; for step A), one uses `(6.7.8)`, as well as
`(4.2.7)` for (ii); for step B), one uses `(9.9.2)` and `(9.9.4)`. It remains to examine step C) in each case.

(i) As in `(12.1.1.2)`, one reduces (using `(6.7.8)`) to the case where $Y$ is the spectrum of a discrete valuation ring
$A$, $X = \operatorname{Spec}(B)$, where $B$ is an $A$-algebra of finite type, $x$, $x'$ two points of $X$ such that
$f(x) = y$ is the closed point and $y' = f(x')$ the generic point of $Y$, with $x'$ moreover a generization of $x$.
Since the task is to prove that $X$ satisfies $(S_{k})$ at the point $x'$, one may replace $X$ by
$\operatorname{Spec}(\mathcal{O}_{X, x'})$, that is, suppose the ring $B$ local, the homomorphism $A \to B$ local, and
$B$ essentially of finite type over $A$ `(1.3.8)`. Then, by hypothesis, if $t$ is a uniformizer of $A$, $t$ is a
$B$-regular element by flatness, and $B/tB$ satisfies $(S_{k})$. But since $A$ is a universally catenary ring `(5.6.4)`,
$B$ is catenary, hence, by `(5.12.4)`, it follows that $B$ satisfies $(S_{k})$, which completes the proof in case (i).

(iii) Here step C) is unnecessary; since $f$ is flat, one knows in effect `(6.8.7)` that when $Y$ is locally Noetherian
and $f$ locally of finite type, the set of $x \in X$ such that $X_{f(x)}$ is geometrically regular at the point $x$ is
open in $X$.

(ii) Reasoning as in `(12.1.1.3)`, to prove that the property considered is stable under generization, one may first, by
considering an arbitrary finite extension $K'$ of $k(y)$, and taking account of definition `(6.7.6)` of geometric
property $(R_{k})$, as well as of the invariance under base-field change of the two other properties figuring in (ii),
replace in (ii) the geometric property $(R_{k})$ by property $(R_{k})$. Proceeding then as in (i), one reduces to the
case where $Y$ is the spectrum of a discrete valuation ring $A$, and since $A$ is catenary, it suffices to apply
`(5.12.5)` to conclude.

(iv) The set of points $x \in X$ such that $X_{f(x)}$ is geometrically normal at the point $x$ is contained in the set
of $x \in X$ such that $X_{f(x)}$ is geometrically pointwise integral and satisfies `(S_2)` at the point $x$, and the
latter is open in $X$ by virtue of `(12.1.1, (viii))`. One may therefore already suppose that, for every $x \in X$,
$X_{f(x)}$ is geometrically pointwise integral and satisfies `(S_2)` at the point $x$, and *a fortiori* it is
equidimensional. On the other hand, by virtue of Serre's criterion `(5.8.6)`, to say that $X_{f(x)}$ is geometrically
normal at the point $x$ means that $X_{f(x)}$ satisfies `(S_2)` and geometric property `(R_1)` at $x$;

<!-- original page 179 -->

but by virtue of (ii) and the preceding remarks, this set is the intersection of two open sets of $X$, hence is open in
$X$. Q.E.D.

**Corollary (12.1.7).**

<!-- label: IV.12.1.7 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation. Then the set of points $x \in X$ where $f$ possesses
one of the following properties `(6.8.1)`:*

*(i) satisfies property $(S_{n})$;*

*(ii) is of codepth $\leq n$;*

*(iii) is Cohen-Macaulay;*

*(iv) is regular (or smooth, which amounts to the same);*

*(v) is normal;*

*(vi) is reduced;*

*is open in $X$.*

Indeed, it follows from `(11.3.1)` that the set of $x \in X$ where $f$ is flat is open. One may therefore confine
oneself to the case where $f$ is flat, and then the corollary follows from `(12.1.1, (iv), (vi), and (vii))` and from
`(12.1.6, (i), (ii), and (iv))`.

**Remarks (12.1.8).**

<!-- label: IV.12.1.8 -->

*(i) In `(12.1.6, (ii))`, one cannot suppress the hypothesis that $x$ belongs to no embedded associated prime cycle of
$X_{f(x)}$. This is what the example `(5.12.3)` shows, where one takes $X = \operatorname{Spec}(A)$, $Y$ being the
spectrum of the local ring `A_0` of `k[T]` corresponding to the prime ideal `(T)` and the morphism $X \to Y$
corresponding to the injective homomorphism $A_{0} \to A$, deduced by localization and passage to the quotient from the
injection $k[T] \to k[T, U, V]$; this morphism is flat since $A$ is a torsion-free `A_0`-module $(0_{I}, 6.3.4)$. Here
the fibre $X_{y}$ at the closed point $y$ of $Y$, equal to $\operatorname{Spec}(A/tA)$, is irreducible, of dimension
`1`, and satisfies the geometric condition `(R_0)`, since the local ring at its generic point is a field. By contrast,
at the generic point $y'$ of $Y$, the fibre $X_{y'}$ has two irreducible components of respective dimensions `0` and
`1`, and the one of dimension `0` is not reduced, so $X_{y'}$ does not satisfy condition `(R_0)`.*

*(ii) In `(12.1.6, (ii))`, neither can one suppress the hypothesis that $X_{f(x)}$ is equidimensional at the point $x$.
One sees this here on the example `(5.12.6)` with $X = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(A_{0})$, where
`A_0` is defined as in (i), the morphism $X \to Y$ coming again from the injection $k[T] \to k[T, U, V, W]$ by
localization and passage to the quotient, and being flat since $A$ is a torsion-free `A_0`-module $(0_{I}, 6.3.4)$. The
fibre $X_{y}$ at the closed point $y$ of $Y$ is reduced (hence satisfies `(S_1)`) and satisfies `(R_1)`, but has two
irreducible components of dimensions `2` and `1`, while the fibre $X_{y'}$ at the generic point $y'$ of $Y$ does not
satisfy \[condition `(R_1)`\].*

### 12.2. Local and global properties of the fibres of a proper, flat morphism of finite presentation

**Theorem (12.2.1).**

<!-- label: IV.12.2.1 -->

*Let $f : X \to Y$ be a proper morphism of finite presentation, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module that is
$f$-flat and of finite presentation, $\Phi$ a finite subset of $\mathbb{Z} \cup {\pm\infty}$, $k$ an integer. The
following subsets of $Y$ are open:*

*(i) The set of $y \in Y$ such that the set of dimensions of the associated prime cycles of $\mathcal{F}_{y}$ is
contained in $\Phi$.*

*(ii) The set of $y \in Y$ such that the set of dimensions of the irreducible components of $Supp(\mathcal{F}_{y})$
contains $\Phi$.*

*(iii) The set of $y \in Y$ such that all the associated prime cycles of $\mathcal{F}_{y}$ have the same dimension equal
to $k$.*

*(iv) The set of $y \in Y$ such that $\mathcal{F}_{y}$ has no embedded associated prime cycle and that the set of
dimensions of the irreducible components of $Supp(\mathcal{F}_{y})$ is equal to $\Phi$.*

<!-- original page 180 -->

*(v) The set of $y \in Y$ such that $\mathcal{F}_{y}$ has property $(S_{k})$ and is equidimensional at every point of
$X_{y}$.*

*(vi) The set of $y \in Y$ such that $coprof(\mathcal{F}_{y}) \leq k$.*

*(vii) The set of $y \in Y$ such that $\mathcal{F}_{y}$ is a Cohen-Macaulay $\mathcal{O}_{X}$-Module.*

*(viii) The set of $y \in Y$ such that $\mathcal{F}_{y}$ is geometrically reduced.*

*(ix) The set of $y \in Y$ such that $\mathcal{F}_{y}$ is geometrically pointwise integral at each point of $X_{y}$.*

*(x) The set of $y \in Y$ such that $\mathcal{F}_{y}$ is geometrically integral.*

*(xi) The set of $y \in Y$ such that $\mathcal{F}_{y}$ has no embedded associated prime cycle and that the sum $l(y)$ of
the total multiplicities `(4.7.12)` of $\mathcal{F}_{y}$ at the maximal points of $Supp(\mathcal{F}_{y})$ is $\leq k$.*

With the exception of (ii), (iii), (iv), (x), and (xi), the properties $P(y)$ considered are of the following form: "for
every $x \in X_{y}$, $\mathcal{F}_{y}$ has property $Q(x)$", where $Q(x)$ is one of properties (i) to (viii) of
`(12.1.1)`. It follows from `(12.1.1)` that the set $U$ of $x \in X$ such that $Q(x)$ is true is open, and the set $V$
of $y \in Y$ such that $P(y)$ is true is none other than the set $Y - f(X - U)$; in all these cases, the theorem is
therefore already true on the sole hypothesis that the morphism $f$ is closed. For (iii), one applies (i) with $\Phi$
reduced to a single element. There remain cases (ii), (iv), and (xi) to examine separately ((x) deducing at once from
(xi) and `(4.7.14)`), always applying the method described in `(12.0.2)`.

**(12.2.1.1)**

<!-- label: IV.12.2.1.1 -->

*Case (ii):* Steps A) and B) of the proof proceed as in the beginning of `(12.1.1)`; for step A), one uses `(8.9.1)`,
`(11.2.6)`, and `(4.2.7)`; for step B), one uses `(9.5.5)` applied to $Supp(\mathcal{F})$. It remains to show that if
(supposing $Y$ Noetherian) the set of dimensions of the irreducible components of $Supp(\mathcal{F}_{y})$ contains
$\Phi$, then the same is true of the set of dimensions of the irreducible components of $Supp(\mathcal{F}_{y'})$, for
every generization $y'$ of $y$ in $Y$. Let `Y_1` be a spectrum of a discrete valuation ring such that, if $y_{1}$ and
$y'_{1}$ are the closed point and the generic point of `Y_1`, there is a morphism $h : Y_{1} \to Y$ with $h(y_{1}) = y$,
$h(y'_{1}) = y'$ `(II, 7.1.7)`. Applying `(4.2.7)`, one sees that one may replace $Y$ by `Y_1` and $X$ by $X_{1} = X
\times_{Y} Y_{1}$, in other words confine oneself to the case where $Y$ is the spectrum of a discrete valuation ring,
$y$ its closed point and $y'$ its generic point.

Using $(Err_{III}, 30)$, one may confine oneself to the case where $Supp(\mathcal{F}) = X$, so that $f$ is quasi-flat
`(2.3.3)`; the irreducible components $Z_{i}$ of $X$ then dominate $Y$ `(2.3.4)`, in other words their generic points
belong to $X_{y'}$ and the $Z_{i} \cap X_{y'}$ are the irreducible components of $X_{y'}$. But every irreducible
component of $X_{y}$ is contained in one of the $Z_{i}$, hence is an irreducible component of $(Z_{i})_{y}$; now one
knows `(7.1.13)` that the dimensions of all the irreducible components of $(Z_{i})_{y}$ are equal to
$\dim((Z_{i})_{y'})$, which completes the proof of (ii).

**(12.2.1.2)**

<!-- label: IV.12.2.1.2 -->

*Case (iv):* The same reasoning as at the beginning shows, using `(12.1.1, (iii))`, that one may already suppose
(replacing $Y$ by an open set of $Y$) that for every $y \in Y$, $\mathcal{F}_{y}$ has no embedded associated prime
cycle. The assertion of case (iv) is then an immediate consequence of the assertions of cases (i) and (ii).

<!-- original page 181 -->

**(12.2.1.3)**

<!-- label: IV.12.2.1.3 -->

*Case (xi):* For step A) of the reasoning, one uses `(8.9.1)`, `(11.2.6)`, `(8.10.5, (xii))` (to preserve the hypothesis
that $f$ is proper), as well as `(4.2.7)`, `(4.5.6)`, and `(4.7.9)`. For step B), one sees, as in case (iv), that one
may suppose that for every $y \in Y$, $\mathcal{F}_{y}$ has no embedded associated prime cycle, and one applies
`(9.8.8)`, which proves that the function $z \mapsto l(z)$ is constructible. It therefore remains to see (supposing $Y$
Noetherian and $f$ proper) that for every generization $y'$ of a point $y \in Y$, one has $l(y') \leq l(y)$. Reasoning
as in `(12.1.1.3)`, one sees (using `(4.7.8)` and `(4.5.11)`) that one may suppose that the irreducible components of
$Supp(\mathcal{F}_{y'})$ are geometrically irreducible and that $l(y')$ is the sum of the lengths of
$(\mathcal{F}_{y'})_{z'_{j}}$ at the maximal points $z'_{j}$ of $Supp(\mathcal{F}_{y'})$. Applying `(4.2.7)`, `(4.5.6)`,
and `(4.7.9)` again, one reduces, as in `(12.2.1.1)`, to the case where $Y$ is the spectrum of a discrete valuation
ring, $y$ its closed point and $y'$ its generic point. The fact that $l(y') \leq l(y)$ will then be a consequence of:

**Lemma (12.2.1.4).**

<!-- label: IV.12.2.1.4 -->

*Let $Y$ be the spectrum of a discrete valuation ring, $y$ its closed point, $y'$ its generic point, $f : X \to Y$ a
proper morphism, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module that is $f$-flat, $z_{i}$ (resp. $z'_{j}$) the
maximal points of $Supp(\mathcal{F}_{y})$ (resp. $Supp(\mathcal{F}_{y'})$). Suppose that $\mathcal{F}_{y}$ has no
embedded associated prime cycle. Then one has*

```text
  (12.2.1.4.1)         ∑_j long((ℱ_{y'})_{z'_j}) ≤ ∑_i long((ℱ_y)_{z_i}).
```

One has $Y = \operatorname{Spec}(A)$, where $A$ is a discrete valuation ring, of which we denote by $t$ a uniformizer,
so that $\mathcal{F}_{y} = \mathcal{F}/t\mathcal{F}$. Since $\mathcal{F}$ is $f$-flat, the $z'_{j}$ are also the maximal
points of $Supp(\mathcal{F})$ `(2.3.4)`; for every $z_{i}$, let us denote by $z'_{ij}$ those of the $z'_{j}$ that are
generizations of $z_{i}$; it follows from `(3.4.1.1)` that one has

$$ long((\mathcal{F}_{y})_{z_{i}}) \geq \sum_{j} long((\mathcal{F}_{y'})_{z'_{ij}}), $$

whence on summing

```text
  ∑_i long((ℱ_y)_{z_i}) ≥ ∑_{i, j} long((ℱ_{y'})_{z'_{ij}}).
```

The lemma will therefore be proved if we establish that for every $z'_{j}$ there is at least one index $i$ such that
$z'_{j}$ is one of the $z'_{ij}$. Now, since $f$ is proper (hence closed) and $f(z'_{j}) = y'$, there exists $x \in X$
which is a specialization of $z'_{j}$ and is such that $f(x) = y$, in other words $\overline{z'_{j}} \cap X_{y}$ is
non-empty. Since $t$ is $\mathcal{F}$-regular by flatness, one deduces from `(3.4.3)` that there is at least one point
of $Ass(\mathcal{F}_{y})$ of which $z'_{j}$ is a generization; but since the points of $Ass(\mathcal{F}_{y})$ are by
hypothesis the $z_{i}$, this completes the proof.

**Corollary (12.2.2).**

<!-- label: IV.12.2.2 -->

*Under the hypotheses of `(12.2.1)`:*

*(i) The function $y \mapsto \dim(Supp(\mathcal{F}_{y}))$ is continuous (hence locally constant) in $Y$.*

*(ii) The function $y \mapsto coprof(\mathcal{F}_{y})$ `(5.7.1)` is upper semi-continuous in $Y$.*

*(iii) The function $y \mapsto l(y)$ `(12.2.1, (xi))` is upper semi-continuous in $Y$ when the $\mathcal{F}_{y}$ have no
embedded associated prime cycle.*

*(iv) The function $y \mapsto prof_{*}(\mathcal{F}_{y})$ `(10.8.1)` is lower semi-continuous in $Y$.*

<!-- original page 182 -->

(i) It follows from `(12.2.1, (i))` applied to $\Phi$ equal to the smallest interval of $\mathbb{N}$ containing the
dimensions of the associated prime cycles of $\mathcal{F}_{y}$, that $z \mapsto \dim(Supp(\mathcal{F}_{z}))$ is upper
semi-continuous at the point $y$; it follows on the other hand from `(12.2.1, (ii))` applied to $\Phi$ equal to the set
of dimensions of the irreducible components of $Supp(\mathcal{F}_{y})$, that this same function is lower semi-continuous
at the point $y$, whence the conclusion. Assertions (ii) and (iii) are nothing but other formulations of
`(12.2.1, (vi) and (xi))`. Finally, by `(12.1.3)`, the set of $x \in X$ such that $prof_{x}(\mathcal{F}_{x}) \geq k$ is
open, and the conclusion of (iv) follows by the same reasoning as at the beginning of `(12.2.1)`.

**Remarks (12.2.3).**

<!-- label: IV.12.2.3 -->

*(i) One will observe that for `(12.2.1, (ii))`, one may dispense with the hypothesis that $f$ is proper.*

*(ii) In `(12.2.1, (ii))`, one cannot replace the condition that the set $E(y)$ of dimensions of the irreducible
components of $Supp(\mathcal{F}_{y})$ contain $\Phi$, by the condition that $E(y)$ be equal to $\Phi$. Indeed, let $k$
be a field, and consider the projective space of dimension `3`, $P = P^{3}_{k} = \operatorname{Proj}(C)$, where $C =
k[t_{0}, t_{1}, t_{2}, t_{3}]$ (with $t_{i}$ indeterminates); in $P$, let `X_0` be the closed sub-scheme "union of the
line `X_1` defined by $t_{1} = t_{2} = 0$ and of the plane `X_2` defined by $t_{2} - t_{3} = 0$", which describes in
geometric terms the fact that `X_0` is equal to $\operatorname{Proj}(C/\mathfrak{a})$, where the graded ideal
$\mathfrak{a}$ is equal to $\mathfrak{bc}$, with $\mathfrak{b} = Ct_{1} + Ct_{2}$, $\mathfrak{c} = C(t_{2} - t_{3})$;
consider the morphism $f_{0} : X_{0} \to X_{1}$ which, in geometric terms, is the "projection of `X_0` onto `X_1` from
the line at infinity $D$ defined by $t_{0} - t_{2} = 0$"; in algebraic form, $f_{0}$ corresponds to the homomorphism of
graded algebras $k[t_{0}, t_{1}] \to k[t_{0}, t_{1}, t_{2}, t_{3}]/\mathfrak{a}$ obtained by passage to the quotient
from the canonical injection $k[t_{0}, t_{1}] \to k[t_{0}, t_{1}, t_{2}, t_{3}]$. It is clear that $f_{0}$ is a
projective morphism, hence proper; so is its restriction $f : X \to Y$, where $Y = D_{+}(t_{0})$ and $X =
f^{-1}_{0}(Y)$; to see that $f$ is flat, it suffices to remark that $k[t_{1}]$ is a principal ring and the ring $C' =
k[t_{1}, t_{2}, t_{3}]/(t_{2} - t_{3})(t_{1}) + (t_{2})$ a torsion-free $k[t_{1}]$-module $(0_{I}, 6.3.4)$. For every $y
\in Y$ distinct from the point $y_{0}$ defined by $t_{2} = 0$, $f^{-1}(y)$ then has two irreducible components, of
dimensions `0` and `1`, while $f^{-1}(y_{0})$ has only one irreducible component of dimension `1`.*

*(iii) In `(12.2.1, (i))`, one cannot either replace the condition that the set $E'(y) \supset E(y)$ of dimensions of
the associated prime cycles of $\mathcal{F}_{y}$ be contained in $\Phi$ by the condition that it be equal to $\Phi$.
Indeed, let $k$ be a field, $A$ the polynomial ring `k[t]`, $B$ the sub-ring $k[t^{4}, t^{3} u, tu^{3}, u^{4}]$ of the
polynomial ring `k[t, u]` (with $t$, $u$ indeterminates); $B$ is not integrally closed, the element $t^{2} u^{2}$
belonging to its integral closure but not being in $B$; if $\mathfrak{m}$ is the maximal ideal of $B$, generated by
$t^{4}$, $t^{3} u$, $tu^{3}$, and $u^{4}$, $\mathfrak{m}$ is an embedded associated prime ideal of $A/tA$. Set $Y =
\operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, and let $f : X \to Y$ be the morphism corresponding to the
homomorphism $A \to B$ which transforms $t$ into $t^{4}$. Since this homomorphism makes $B$ a torsion-free $A$-module,
$f$ is flat $(0_{I}, 6.3.4)$. If $y$ is the point of $Y$ corresponding to the maximal ideal `tA`, the prescheme
$f^{-1}(y)$ is irreducible and of dimension `1`, but admits an embedded associated prime cycle of dimension `0`; on the
contrary, if $y'$ is the generic point of $Y$, $f^{-1}(y')$ has no embedded associated prime cycle, being the spectrum
of an integral $k(y')$-algebra of dimension `1`. In this example, $f$ is an affine morphism that is not proper; one can
immediately deduce from it an analogous example where $f$ is proper and flat by considering $X$ as a dense open set of a
projective scheme over $Y$ (`(II, 5.3.4 and 5.3.2)`), or by proceeding directly as in Remark (ii).*

*Remarks (ii) and (iii) show the necessity of including in `(12.2.1, (iv))` the condition that $\mathcal{F}_{y}$ have no
embedded associated prime cycle.*

*(iv) In `(12.2.1, (xi))`, one cannot suppress the hypothesis that $f$ is proper. Indeed, let $k$ be a field, $Y$ the
"affine line", spectrum of the polynomial ring `k[t]` ($t$ indeterminate), $X$ the sum prescheme of $Y$ and of the
complementary open set of the closed point $y$ of $Y$ defined by $t = 0$. It is clear that the morphism $f : X \to Y$
which is equal to the canonical injections on each of the components of $X$ is flat and that if one takes $\mathcal{F} =
\mathcal{O}_{X}$, $\mathcal{F}_{z}$ has no embedded associated prime cycle for any $z \in Y$. However, one sees at once
that one has $l(y) = 1$ and $l(z) = 2$ for every $z \neq y$.*

*(v) In `(12.2.1, (xi))`, neither can one suppress the hypothesis that $\mathcal{F}_{y}$ is without embedded associated
prime cycle. This is what the example of Remark (ii) shows: one sees at once in effect that one has, with $\mathcal{F} =
\mathcal{O}_{X}$, $l(y_{0}) = 1$ and $l(y) = 2$ for $y \neq y_{0}$ in $Y$.*

*(vi) We do not know whether in `(12.2.1, (xi))` one may replace the hypothesis that $\mathcal{F}$ is $f$-flat by the
hypothesis that $Supp(\mathcal{F}) = X$ and that $f$ is universally open. Taking up the proof of `(12.2.1.4)` again, one
sees (also using `(14.3.6)`) that one would have to resolve the following question: let $A$ be a Noetherian local ring,
$M$ an $A$-module*

<!-- original page 183 -->

*of finite type, $t$ an element of the maximal ideal $\mathfrak{m}$ of $A$ that is contained in no minimal prime ideal
of $A$; if there exists one of these minimal prime ideals $\mathfrak{p}$ such that $\dim(A/\mathfrak{p}) = 1$, is it
true that $\mathfrak{m}$ is an associated prime ideal of $M/tM$ ($t$ not being supposed $M$-regular)?*

*One will note however that one cannot, in `(12.2.1, (xi))`, suppress purely and simply the hypothesis that
$\mathcal{F}$ is $f$-flat. One will take here $P$ as in Remark (ii), then in $P$ the closed sub-scheme `X_0` union of
the three lines `X_1`, `X_2`, `X_3` defined respectively by $t_{1} = t_{3} = 0$, $t_{1} - t_{0} = t_{3} = 0$, $t_{2} =
t_{3} = 0$; one defines the projection $f_{0}$ of `X_0` onto `X_1` as before, and its restriction $f : X \to Y$, where
$Y = D_{+}(t_{0})$ is the affine line and $X = f^{-1}_{0}(Y)$; $f$ is proper but not flat, and if one takes $\mathcal{F}
= \mathcal{O}_{X}$, $\mathcal{F}_{y}$ has no embedded associated prime cycles for any $y \in Y$. But one has $l(y_{0}) =
1$ and $l(y) = 2$ for $y \neq y_{0}$ in $Y$.*

**Theorem (12.2.4).**

<!-- label: IV.12.2.4 -->

*Let $f : X \to Y$ be a proper, flat morphism of finite presentation, $k$ an integer $\geq 1$. The following subsets of
$Y$ are open:*

*(i) The set of $y \in Y$ such that $X_{y}$ possesses property $(S_{k})$.*

*(ii) The set of $y \in Y$ such that $X_{y}$ satisfies geometric property $(R_{k})$, is equidimensional at every point,
and has no embedded associated prime cycle.*

*(iii) The set of $y \in Y$ such that $X_{y}$ is geometrically regular (i.e. smooth over $k(y)$).*

*(iv) The set of $y \in Y$ such that $X_{y}$ is geometrically normal.*

*(v) The set of $y \in Y$ such that $X_{y}$ is geometrically reduced.*

*(vi) The set of $y \in Y$ such that $X_{y}$ is geometrically reduced and that the geometric number of connected
components of $X_{y}$ is equal to $k$.*

*(vii) The set of $y \in Y$ such that $X_{y}$ is geometrically pointwise integral `(4.6.9)`.*

*(viii) The set of $y \in Y$ such that $X_{y}$ is geometrically integral.*

*(ix) The set of $y \in Y$ such that $X_{y}$ has no embedded associated prime cycle and that the total multiplicity
`(4.7.4)` of $X_{y}$ over $k(y)$ is $\leq k$.*

Except for (vi), these assertions are special cases of assertions of `(12.2.1)`, or are deduced from assertions of
`(12.1.6)` as at the beginning of the proof of `(12.2.1)`. For (vi), one reduces as always (taking into account the
invariance under base change of the geometric number of connected components `(4.5.6)`) to the case where $Y$ is
Noetherian. The set $U$ of $y \in Y$ such that $X_{y}$ is geometrically reduced is open in $Y$ by virtue of (v); it then
follows from `(III, 7.8.7 and 7.8.6)` that for every $y \in U$, there is a neighbourhood $V \subset U$ of $y$ and an
integer $m$ such that, for every $z \in V$, $\Gamma(X_{z}, \mathcal{O}_{X_{z}})$ is isomorphic to $(k(z))^{m}$; but by
virtue of `(III, 4.3.4)`, $m$ is then the geometric number of connected components of $X_{z}$, whence the conclusion.
One will give another proof of (vi) in `(15.5.9)`.

### 12.3. Local cohomological properties of the fibres of a flat morphism locally of finite presentation

**Lemma (12.3.1).**

<!-- label: IV.12.3.1 -->

*Let $A$ be a ring, $B$ an $A$-algebra of finite presentation that is a flat $A$-module, $M$ a $B$-module of finite
presentation that is a flat $A$-module. Then the following conditions are equivalent:*

*a) $M$ is a projective $B$-module.*

*b) $M$ is a flat $B$-module.*

*c) For every $y \in \operatorname{Spec}(A)$, $M \otimes_{A} k(y)$ is a projective $(B \otimes_{A} k(y))$-module.*

<!-- original page 184 -->

The equivalence of a) and b) follows from Bourbaki, *Alg. comm.*, chap. II, §5, n° 2, cor. 2 of th. 1. Since a) implies
c) trivially, it remains to prove that c) implies b), which follows from the fibrewise flatness criterion `(11.3.10)`,
applied with $g = h$, $f = 1_{X}$.

**Proposition (12.3.2).**

<!-- label: IV.12.3.2 -->

*Let $A$ be a ring, $B$ an $A$-algebra of finite presentation that is a flat $A$-module, $M$ a $B$-module of finite
presentation that is a flat $A$-module. Then:*

*(i) There exists a left resolution of $M$ by free $B$-modules of finite type.*

*(ii) One has*

```text
  (12.3.2.1)    dim. proj_B(M) = sup_{y ∈ Spec(A)} dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) = Tor.dim_B(M)
```

*where $Tor.\dim_{B}(M)$ is the smallest integer $i$ such that $Tor^{B}_{j}(M, N) = 0$ for every $j > i$ and every
$B$-module $N$ (and $+\infty$ if no such integer $i$ exists).*

(i) By virtue of `(8.9.1)`, there exists a Noetherian sub-ring `A_0` of $A$, an `A_0`-algebra of finite type `B_0` and a
`B_0`-module of finite type `M_0` such that $B$ is isomorphic to $B_{0} \otimes_{A_{0}} A$ and $M$ to $M_{0}
\otimes_{A_{0}} A$. Moreover `(11.2.7)`, one may suppose that `B_0` and `M_0` are flat `A_0`-modules. There then exists
a left resolution $(L_{0})_{\bullet}$ of `M_0` formed of free `B_0`-modules of finite type, and since `M_0` and the
$L_{0, i}$ are flat `A_0`-modules, $(L_{0})_{\bullet} \otimes_{A_{0}} A$ is a left resolution of $M$ formed of free
$B$-modules of finite type `(2.1.10)`.

(ii) By virtue of `(0, 17.2.2, (ii))`, one has `Tor.dim_B(M) ≤ dim. proj_B(M)`, and the definition of the projective
dimension immediately shows that, for every $y \in \operatorname{Spec}(A)$, one has
`dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) ≤ dim. proj_B(M)`. To prove the reverse inequalities, consider a left resolution
$(L_{i})$ of $M$ by free $B$-modules of finite type, and suppose that $Tor.\dim_{B}(M) = n$ (resp. $\dim. proj_{B
\otimes_{A} k(y)}(M \otimes_{A} k(y)) \leq n$ for every $y \in \operatorname{Spec}(A)$). Then $R = Im(L_{n} \to L_{n-1})
= Ker(L_{n-1} \to L_{n-2})$ is a $B$-module of finite type that is also a flat $A$-module, by virtue of the hypothesis
on $M$ and $B$ and of `(2.1.10)`. In addition, one has $Tor^{B}_{j+1}(M, N) = Tor^{B}_{j}(R, N)$ for every $B$-module
$N$ `(M, V, 7)`. The hypothesis $Tor.\dim_{B}(M) = n$ therefore entails $Tor^{B}_{1}(R, N) = 0$ for every $B$-module
$N$, that is to say that $R$ is a flat $B$-module, hence projective by virtue of `(12.3.1)`; this establishes that
$\dim. proj_{B}(M) \leq n$. The hypothesis $\dim. proj_{B \otimes_{A} k(y)}(M \otimes_{A} k(y)) \leq n$ for every $y \in
\operatorname{Spec}(A)$ entails on the other hand, by tensorization with $k(y)$, that in each of the sequences (exact by
virtue of the flatness over $A$ of $M$, of the $L_{i}$, and of $R$ `(2.1.10)`)

```text
  0 → R ⊗_A k(y) → L_{n−1} ⊗_A k(y) → ⋯ → L_0 ⊗_A k(y) → M ⊗_A k(y) → 0,
```

$R \otimes_{A} k(y)$ is a projective $(B \otimes_{A} k(y))$-module (for $y \in \operatorname{Spec}(A)$). One concludes
once again from `(12.3.1)` that $R$ is a projective $B$-module, hence $\dim. proj_{B}(M) \leq n$.

**Proposition (12.3.3).**

<!-- label: IV.12.3.3 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $\mathcal{L}_{\bullet}$ a complex formed of
quasi-coherent $\mathcal{O}_{X}$-Modules of finite presentation; for every $s \in S$, let $(\mathcal{L}_{\bullet})_{s}$
be the complex $\mathcal{L}_{\bullet} \otimes_{\mathcal{O}_{S}} k(s)$ of $\mathcal{O}_{X_{s}}$-Modules of finite type.
Suppose that $\mathcal{L}_{n-1}$ is $f$-flat. Then the set $U$ of $x \in X$ such that
$(\mathcal{H}_{n}((\mathcal{L}_{\bullet})_{f(x)}))_{x} = 0$ is open in $X$. If moreover $\mathcal{L}_{n}$ is $f$-flat,
then one has $\mathcal{H}_{n}(\mathcal{L}_{\bullet}) | U = 0$.*

One may evidently confine oneself to the case where $n = 1$ and where the complex $\mathcal{L}_{\bullet}$ reduces to $0
\to \mathcal{L}_{2} \to \mathcal{L}_{1} \to \mathcal{L}_{0} \to 0$. One may first reduce to the case where $S =
\operatorname{Spec}(A)$ and $X$

<!-- original page 185 -->

are affine, then to the case where $S$ is Noetherian; indeed, by `(8.9.1)` and `(8.5.2)`, one knows that there exist a
Noetherian prescheme $S' = \operatorname{Spec}(A')$, where $A'$ is a sub-ring of $A$, a morphism of finite type $f' : X'
\to S'$, and three coherent $\mathcal{O}_{X'}$-Modules $\mathcal{L}'_{i}$ ($0 \leq i \leq 2$) such that $X = X'
\times_{S'} S$, $f = f'_{(S)}$, $\mathcal{L}_{i} = \mathcal{L}'_{i} \otimes_{S'} S$, as well as two homomorphisms $u'$,
$v'$ such that $u = u' \otimes 1$, $v = v' \otimes 1$, and $v' \circ u' = 0$. One may moreover suppose that
$\mathcal{L}'_{0}$ is $f'$-flat `(11.2.7)`, and that $\mathcal{L}'_{1}$ is $f'$-flat when $\mathcal{L}_{1}$ is supposed
$f$-flat. By faithful flatness, the hypothesis $(\mathcal{H}_{1}((\mathcal{L}_{\bullet})_{f(x)}))_{x} = 0$ is equivalent
to $(\mathcal{H}_{1}((\mathcal{L}'_{\bullet})_{f'(x')}))_{x'} = 0$, where $x'$ is the projection of $x$ in $X'$; if $U'$
is the set of $x' \in X'$ such that $(\mathcal{H}_{1}((\mathcal{L}'_{\bullet})_{f'(x')}))_{x'} = 0$, then $U$ is the
inverse image of $U'$ by the projection $X \to X'$, which reduces, for the first assertion, to the case where $S$ is
Noetherian. For the second assertion, one further remarks that $A$ is an inductive limit of its sub-rings $A_{\lambda}$
that are $A'$-algebras of finite type; set $X_{\lambda} = X' \times_{S'} S_{\lambda}$, where $S_{\lambda} =
\operatorname{Spec}(A_{\lambda})$, $\mathcal{L}^{(\lambda)}_{\bullet} = \mathcal{L}'_{\bullet} \otimes_{S'}
S_{\lambda}$, and let $u_{\lambda} = u' \otimes 1 : \mathcal{L}^{(\lambda)}_{2} \to \mathcal{L}^{(\lambda)}_{1}$,
$v_{\lambda} = v' \otimes 1 : \mathcal{L}^{(\lambda)}_{1} \to \mathcal{L}^{(\lambda)}_{0}$, so that one has
$\mathcal{H}_{1}(\mathcal{L}^{(\lambda)}_{\bullet}) = Ker(v_{\lambda})/Im(u_{\lambda})$. Now, since the functor `lim` is
exact in the category of commutative groups, one has `Ker(v) = lim Ker(v_λ)`, $Im(u) = \lim Im(u_{\lambda})$, and
$\mathcal{H}_{1}(\mathcal{L}_{\bullet}) = \lim \mathcal{H}_{1}(\mathcal{L}^{(\lambda)}_{\bullet})$. If one has supposed
that $\mathcal{L}_{1}$ is $f$-flat and (by reducing to the case where $X = U$) that one has proved
$\mathcal{H}_{1}(\mathcal{L}^{(\lambda)}_{\bullet}) = 0$ for every $\lambda$, one will indeed deduce the assertion.

I) Suppose henceforth $S$ Noetherian. One knows (without flatness hypothesis on $\mathcal{L}_{0}$) that the set $U$ is
constructible in $X$ `(9.9.6)`. Using now $(0_{III}, 9.2.5)$, it remains to show that for every generization $x'$ of $x
\in U$ in $X$, one has also $x' \in U$. The method exposed in `(12.0.2)` applies without change (taking into account the
fact that for a prescheme $Z$ over a field $k$ and an extension $k'$ of $k$, the projection $Z \otimes_{k} k' \to Z$ is
faithfully flat). One may therefore suppose that $S$ is the spectrum of a discrete valuation ring $A$, of which one
denotes by $t$ a uniformizer, with $x$ above the closed point of $S$ and $x'$ above the generic point of $S$. The
hypothesis that $\mathcal{L}_{0}$ is $f$-flat entails that $t$ is $\mathcal{L}_{0}$-regular $(0_{I}, 6.3.4)$. One is
then reduced to proving the following lemma (where $B$, $M$, $N$, $P$ will be replaced by $\mathcal{O}_{x}$,
$(\mathcal{L}_{2})_{x}$, $(\mathcal{L}_{1})_{x}$, and $(\mathcal{L}_{0})_{x}$ respectively):

**Lemma (12.3.3.1).**

<!-- label: IV.12.3.3.1 -->

*Let $B$ be a Noetherian local ring, $M$, $N$, $P$ three $B$-modules, with $N$ of finite type, $M \xrightarrow{u} N
\xrightarrow{v} P$ two homomorphisms such that $v \circ u = 0$. Let $t$ be an element of the maximal ideal of $B$ such
that $t$ is $P$-regular and such that the sequence*

```text
  (12.3.3.2)        M/tM ─u⊗1→ N/tN ─v⊗1→ P/tP
```

*is exact. Then the sequence $M \to N \to P$ is exact.*

Let us first note that if one replaces $M$ by its image $Q$ in $N$ and $u$ by the injection $j : Q \hookrightarrow N$,
the image of $j \otimes 1$ is the same as that of $u \otimes 1$, hence one may, without changing the hypothesis nor the
conclusion, suppose $u$ injective. On the other hand, if $R$ is the image of $v$ and $p : N \to R$ the canonical
surjection, $t$ is evidently $R$-regular, one has $p \circ u = 0$, and the kernel of $p \otimes 1$ is contained in that
of $v \otimes 1$; it is consequently equal to it if the sequence `(12.3.3.2)` is exact; since on the other hand one has
evidently $Ker(p) = Ker(v)$,

<!-- original page 186 -->

one sees that one may, to prove the lemma, suppose moreover $v$ surjective. The lemma will then be a consequence of:

**Lemma (12.3.3.3).**

<!-- label: IV.12.3.3.3 -->

*Let $B$ be a ring, $M$, $N$, $P$ three $B$-modules, $u : M \to N$, $v : N \to P$ two homomorphisms such that $u$ is
injective, $v$ surjective, and $v \circ u = 0$. Let $t$ be an element of $B$ such that $t$ is $P$-regular. Then one has*

```text
  (12.3.3.4)        Ker(v ⊗ 1)/Im(u ⊗ 1) = (Ker(v)/Im(u)) ⊗_B (B/tB)
```

*up to a canonical isomorphism.*

Indeed, the hypothesis that the sequence `(12.3.3.2)` is exact will then entail $(Ker(v)/Im(u)) \otimes_{B} (B/tB) = 0$,
and since $t$ belongs to the maximal ideal of $B$ and $Ker(v)$ is a $B$-module of finite type (since $B$ is supposed
Noetherian in `(12.3.3.1)`), Nakayama's lemma will prove that $Ker(v) = Im(u)$.

It therefore remains to prove `(12.3.3.3)`. Set $u' = u \otimes 1$, $v' = v \otimes 1$, $Z = Ker(v)$, $H = Z/Im(u)$, so
that one has the exact sequences

```text
  0 → M → Z → H → 0
  0 → Z → N ─v→ P → 0
```

whence, by tensorizing with $B/tB$ and using lemma `(3.4.1.4)` and the fact that $t$ is $P$-regular, the exact sequences

```text
  M/tM ─w'→ Z/tZ → H/tH → 0
  0 → Z/tZ → N/tN ─v'→ P/tP → 0
```

whence $Ker(v') = Z/tZ$, and since $Im(w') = Im(u')$, one obtains `(12.3.3.4)`.

II) Suppose now in addition that $\mathcal{L}_{1}$ is $f$-flat; replacing furthermore possibly $X$ by $U$, one may
suppose that $X = U$. The task is to see that for every $x \in X$, one has $(\mathcal{H}_{1}(\mathcal{L}_{\bullet}))_{x}
= 0$. Let $s = f(x)$, and let $\mathfrak{n}$ be the ideal $\mathfrak{m}_{s} \mathcal{O}_{X, x}$, which is contained in
the maximal ideal of $\mathcal{O}_{X, x}$; since $(\mathcal{H}_{1}(\mathcal{L}_{\bullet}))_{x}$ is an $\mathcal{O}_{X,
x}$-module of finite type ($X$ being locally Noetherian), it is separated for the $\mathfrak{n}$-adic topology $(0_{I},
7.3.5)$, hence it suffices to show that its separated completion for this topology is `0`. Now, by virtue of
`(III, 7.4.7.2)`, this separated completion is equal to $\lim_{k} \mathcal{H}_{1}(\mathcal{L}_{\bullet}
\otimes_{\mathcal{O}_{S}} (\mathcal{O}_{S, s}/\mathfrak{m}^{k+1}_{s}))$, and it will therefore suffice to prove that
each of the terms of this projective system is null. But this is true by hypothesis for $k = 0$; let us therefore reason
by induction on $k$. The conclusion will follow from the more general lemma below (which one will apply for $A =
\mathcal{O}_{S, s}/\mathfrak{m}^{k+1}_{s}$ and $\mathfrak{J}$ equal to the maximal ideal
$\mathfrak{m}_{s}/\mathfrak{m}^{k+1}_{s}$ of $A$):

**Lemma (12.3.3.5).**

<!-- label: IV.12.3.3.5 -->

*Let $A$ be a ring, $\mathfrak{J}$ a nilpotent ideal of $A$, $L_{\bullet} : P \xrightarrow{u} Q \xrightarrow{v} R$ a
complex of $A$-modules. Set $A_{0} = A/\mathfrak{J}$, $L^{(0)}_{\bullet} = L_{\bullet} \otimes_{A} A_{0} : P_{0}
\xrightarrow{u_{0}} Q_{0} \xrightarrow{v_{0}} R_{0}$, and suppose that $gr^{\bullet}_{\mathfrak{J}}(A)$ is a flat
`A_0`-module, and that $Q$ and $R$ are flat $A$-modules. Then the relation $H_{1}(L^{(0)}_{\bullet}) = 0$ entails
$H_{1}(L_{\bullet}) = 0$.*

Set $L^{(k)}_{\bullet} = L_{\bullet} \otimes_{A} (A/\mathfrak{J}^{k+1}) : P_{k} \xrightarrow{u_{k}} Q_{k}
\xrightarrow{v_{k}} R_{k}$; since there exists an integer $k \geq 1$ such that $L^{(k)}_{\bullet} = L_{\bullet}$, it
will suffice to prove, by induction on $k$, that the sequence $P_{k} \xrightarrow{u_{k}} Q_{k} \xrightarrow{v_{k}}
R_{k}$ is

<!-- original page 187 -->

exact (this assertion following from the hypothesis for $k = 0$). Let then $x \in Q_{k}$ be an element such that
$v_{k}(x) = 0$. Since by the inductive hypothesis the sequence $P_{k-1} \xrightarrow{u_{k-1}} Q_{k-1}
\xrightarrow{v_{k-1}} R_{k-1}$ is exact, the canonical image of $x$ in $Q_{k-1} = Q_{k}/(\mathfrak{J}^{k}
Q_{k}/\mathfrak{J}^{k+1} Q_{k})$ belongs to $Im(u_{k-1})$, hence there exists $z \in P_{k}$ such that $x = u_{k}(z) +
x'$ with $x' \in \mathfrak{J}^{k} Q_{k}/\mathfrak{J}^{k+1} Q_{k}$. Since one has $v_{k} \circ u_{k} = 0$, the relation
$v_{k}(x) = 0$ entails $v_{k}(x') = 0$, and on the other hand one evidently has $v_{k}(x') \in \mathfrak{J}^{k}
R_{k}/\mathfrak{J}^{k+1} R_{k}$; everything therefore comes down to proving that the sequence

```text
  𝔍^k P/𝔍^{k+1} P ─u''→ 𝔍^k Q/𝔍^{k+1} Q ─v''→ 𝔍^k R/𝔍^{k+1} R
```

(where `u''` and `v''` come from $u$ and $v$ by restriction and passage to the quotients) is exact. Now, by hypothesis,
$\mathfrak{J}^{k}/\mathfrak{J}^{k+1}$ is a flat $(A/\mathfrak{J})$-module, hence the sequence

```text
  (P/𝔍P) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1}) ─u''→ (Q/𝔍Q) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1}) ─v''→ (R/𝔍R) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1})
```

is exact. But $(Q/\mathfrak{J}Q) \otimes_{A/\mathfrak{J}} (\mathfrak{J}^{k}/\mathfrak{J}^{k+1}) = Q \otimes_{A}
(\mathfrak{J}^{k}/\mathfrak{J}^{k+1})$ identifies with $\mathfrak{J}^{k} Q/\mathfrak{J}^{k+1} Q$, by virtue of the
flatness of $Q$ over $A$, and likewise $(R/\mathfrak{J}R) \otimes_{A/\mathfrak{J}}
(\mathfrak{J}^{k}/\mathfrak{J}^{k+1})$ identifies with $\mathfrak{J}^{k} R/\mathfrak{J}^{k+1} R$. Finally, the image of
$u'$ identifies with that of `u''`, and this completes the proof.

**Corollary (12.3.4).**

<!-- label: IV.12.3.4 -->

*Let $f : X \to S$ be a flat morphism locally of finite presentation, $\mathcal{F}$, $\mathcal{G}$ two
$\mathcal{O}_{X}$-Modules of finite presentation and $f$-flat. Let $n$ be an integer $\geq 0$, $U$ the set of $x \in X$
such that $(\mathcal{E}xt^{n}_{\mathcal{O}_{X_{f(x)}}}(\mathcal{F}_{f(x)}, \mathcal{G}_{f(x)}))_{x} = 0$ (resp.
$(\mathcal{T}or^{\mathcal{O}_{X_{f(x)}}}_{n}(\mathcal{F}_{f(x)}, \mathcal{G}_{f(x)}))_{x} = 0$). Then $U$ is open, and
one has $\mathcal{E}xt^{n}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}) | U = 0$ (resp.
$\mathcal{T}or^{\mathcal{O}_{X}}_{n}(\mathcal{F}, \mathcal{G}) | U = 0$).*

One may evidently confine oneself to the case where $S$ and $X$ are affine. Then `(12.3.2)`, there exists a left
resolution $\mathcal{L}_{\bullet} = (\mathcal{L}_{i})$ of $\mathcal{F}$ formed of free $\mathcal{O}_{X}$-Modules of
finite type. If one sets $\mathcal{M}^{\bullet} = \mathcal{H}om(\mathcal{L}_{\bullet}, \mathcal{G})$ (resp.
$\mathcal{N}_{\bullet} = \mathcal{L}_{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{G}$), one deduces that each of the
$\mathcal{M}^{i}$ (resp. $\mathcal{N}_{i}$) is isomorphic to an $\mathcal{O}_{X}$-Module of the form $\mathcal{G}^{m}$,
hence the $\mathcal{M}^{i}$ and $\mathcal{N}_{i}$ are $\mathcal{O}_{X}$-Modules of finite presentation and $f$-flat. In
addition, for every base change $S' \to S$, if one sets $X' = X \times_{S} S'$, $\mathcal{F}' = \mathcal{F} \otimes_{S}
S'$, $\mathcal{G}' = \mathcal{G} \otimes_{S} S'$, then $\mathcal{L}'_{\bullet} = \mathcal{L}_{\bullet} \otimes_{S} S'$
is still a left resolution of $\mathcal{F}'$ by free $\mathcal{O}_{X'}$-Modules of finite type `(2.1.10)`, and
$\mathcal{M}'^{\bullet} = \mathcal{M}^{\bullet} \otimes_{S} S'$ is equal to $\mathcal{H}om(\mathcal{L}'_{\bullet},
\mathcal{G}')$ (resp. $\mathcal{N}'_{\bullet} = \mathcal{N}_{\bullet} \otimes_{S} S'$ is equal to
$\mathcal{L}'_{\bullet} \otimes_{\mathcal{O}_{X'}} \mathcal{G}'$) according to what precedes. In particular, one has,
for every $s \in S$, $\mathcal{E}xt^{n}_{\mathcal{O}_{X_{s}}}(\mathcal{F}_{s}, \mathcal{G}_{s}) =
\mathcal{H}^{n}((\mathcal{M}^{\bullet})_{s})$ (resp. $\mathcal{T}or^{\mathcal{O}_{X_{s}}}_{n}(\mathcal{F}_{s},
\mathcal{G}_{s}) = \mathcal{H}_{n}((\mathcal{N}_{\bullet})_{s})$). Applying `(12.3.3)` to the complexes of $f$-flat
Modules $\mathcal{M}^{\bullet}$ and $\mathcal{N}_{\bullet}$, one deduces the corollary at once.
