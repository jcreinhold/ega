<!-- original page 199 -->

## §14. Universally open morphisms

§§14 and 15 are devoted to the study of the notion of *universally open morphism* `(2.4.2)`. One has already seen
`(2.4.6)` that a flat morphism locally of finite presentation is universally open, the converse being inexact. In §14 we
first examine the properties of the dimensions of the fibres of a universally open morphism $f : X \to Y$; when $X$ and
$Y$ are locally Noetherian, $f$ behaves in this respect `(14.2.1)` like a flat morphism (cf. `(6.1.2)`), and is in
particular equidimensional when it is locally of finite type and dominant and $X$ is irreducible `(14.2.2)`. Conversely,
an equidimensional morphism $f : X \to Y$ locally of finite type is universally open when one supposes in addition that
$Y$ is geometrically unibranch, and in particular when $Y$ is normal (Chevalley's criterion, `(14.4.4)`). We show also
that the universally open morphisms $f : X \to Y$ locally of finite type (when $X$ and $Y$ are locally Noetherian and
$Y$ is irreducible) admit "sufficiently many" quasi-sections, i.e. in a neighbourhood of a closed point $x$ of a fibre
$f^{-1}(y)$, there exists a closed subprescheme $X'$ of $X$ containing $x$ such that the restriction $X' \to Y$ of $f$
is a quasi-finite (hence with discrete fibres) and dominant morphism `(14.5.3)`.

<!-- original page 200 -->

In §15 we study various properties of the fibres of universally open morphisms $f : X \to Y$ locally of finite type,
notably when $X$ and $Y$ are locally Noetherian. One thus obtains in particular a criterion for a point $x \in X$ to
belong to only one irreducible component of $X$, in terms of properties of the fibre $f^{-1}(f(x))$ of $x$: it suffices
that $Y$ be geometrically unibranch (for example normal) at the point $f(x)$ and that $f^{-1}(f(x))$ be geometrically
pointwise integral at the point $x$ `(15.3.3)`; if in addition $Y$ is locally integral at the point $f(x)$, $f$ is flat
at the point $x$ and $X$ is locally integral at the point $x$. We also study the variation of the geometric number of
connected components of a fibre $f^{-1}(y)$; for example, if $f$ is universally open and proper, and the fibres of $f$
are geometrically reduced, this number is locally constant `(15.5.7)`. Finally, when $f$ admits a section $g$ (which
will be the case when $X$ is a $Y$-group scheme), and when for every $y \in Y$ one denotes by $X^{\circ}_{y}$ the
connected component of the fibre $X_{y} = f^{-1}(y)$ at the point $g(y)$ (the "neutral component" in the case of
groups), one studies the union $X^{\circ}$ of the $X^{\circ}_{y}$ for $y \in Y$, and one shows `(15.6.4)` that if $f$ is
universally open and the fibres $X_{y}$ geometrically reduced, then $X^{\circ}$ is an open set in $X$.

### 14.1. Open morphisms

**(14.1.1)**

<!-- label: IV.14.1.1 -->

Recall `(1.10.2)` that a continuous map $\psi : X \to Y$ is said to be **open at a point $x \in X$** if the image under
$\psi$ of every neighbourhood of $x$ in $X$ is a neighbourhood of $\psi(x)$ in $Y$.

One notes that this does not imply that there exists a fundamental system of neighbourhoods of $x$ whose images are open
in $Y$.

**Proposition (14.1.2).**

<!-- label: IV.14.1.2 -->

*Let $X$, $Y$ be two topological spaces, $\psi : X \to Y$ a continuous map, $x$ a point of $X$, $y = \psi(x)$.*

*(i) If $\psi$ is open at $x$, then for every part $Y'$ of $Y$ containing $\psi(x)$ the restriction $\psi^{-1}(Y') \to
Y'$ of $\psi$ to $Y'$ is open at the point $x$.*

*(ii) Suppose that $Y$ is the union of a locally finite family of closed parts $(Y_{i})$ and that for every $i$ such
that $\psi(x) \in Y_{i}$, the restriction $\psi^{-1}(Y_{i}) \to Y_{i}$ of $\psi$ is open at the point $x$; then $\psi$
is open at the point $x$.*

*(iii) Let $\gamma : X' \to X$ be a continuous map, $x'$ a point of $X'$; if the composite map $\psi \circ \gamma : X'
\to Y$ is open at the point $x'$, then $\psi$ is open at the point $\gamma(x')$.*

If $U$ is a neighbourhood of $x$, one has $\psi(U \cap \psi^{-1}(Y')) = \psi(U) \cap Y'$; whence (i) at once. To prove
(ii), note that there is a neighbourhood $W$ of $\psi(x)$ in $Y$ meeting only finitely many of the closed parts $Y_{i}$
that contain $\psi(x)$; hence $W$ is the union of the $W \cap Y_{i}$ for these indices. Now, if $U$ is a neighbourhood
of $x$ such that $\psi(U) \cap Y_{i}$ is a neighbourhood of $\psi(x)$ in $Y_{i}$, there exists a neighbourhood $V
\subset W$ of $\psi(x)$ in $Y$ such that for all $i$ with $\psi(x) \in Y_{i}$ one has $V \cap Y_{i} \subset \psi(U) \cap
Y_{i}$, and since the union of the $V \cap Y_{i}$ for these indices is $V$, one has $V \subset \psi(U)$, hence $\psi(U)$
is a neighbourhood of $\psi(x)$ in $Y$. Assertion (iii) is trivial.

**Remarks (14.1.3).**

<!-- label: IV.14.1.3 -->

*(i) The set $Z$ of points $x \in X$ where a morphism is open is not necessarily open.* For example, let $K$ be a field,
$A$ the polynomial ring `K[S, T]`, $V$ the affine plane $\operatorname{Spec}(A)$, $X$ the closed subprescheme of $V$
"the union of the line `X_1` defined by $T = 0$ and the line `X_2` defined by $S = 0$", that is to say
$\operatorname{Spec}(A/\mathfrak{a})$, where $\mathfrak{a} = AST$; take $Y = X_{2} = \operatorname{Spec}(A/AS)$ and for
$f$ the projection corresponding to the canonical injection $K[T] \to A/\mathfrak{a}$; then one has $Z = X_{2}$, which
is not open in $X$.

*(ii)* Let $X$, $Y$ be two Noetherian irreducible preschemes with generic points $\xi$, $\eta$ respectively, and $f : X
\to Y$ a dominant morphism locally of finite type; then $f$ is open at the point $\xi$. Indeed, one may obviously
restrict to the case where $X$ and $Y$ are reduced (hence integral) `(1.5.4)` and affine; by virtue of the generic
flatness theorem `(6.9.1)`, there exists a non-empty open set $V$ of $Y$ such that the restriction $f^{-1}(V) \to V$ of
$f$ is a flat morphism, and one concludes from `(2.4.6)` that this restriction is an open morphism. However, as there
exist dominant morphisms of finite type $f : X \to Y$ (where $X$ and $Y$ are irreducible) which are not open (see for
example `(II, 8.1)`), the set of points where such a morphism is open is not necessarily closed in $X$.

*(iii)* We do not know whether, when $X$ and $Y$ are locally Noetherian and $f : X \to Y$ is a morphism locally of
finite type, the set of points of $X$ where $f$ is open is or is not locally constructible.

**Proposition (14.1.4).**

<!-- label: IV.14.1.4 -->

*Let $X$, $Y$ be two topological spaces, $\psi : X \to Y$ a continuous map. For every $y \in Y$, the set of $x \in
\psi^{-1}(y)$ where $\psi$ is open is a closed part of $\psi^{-1}(y)$.*

Indeed, suppose that $\psi$ is not open at a point $x \in \psi^{-1}(y)$; there exists then an open neighbourhood $V$ of
$x$ in $X$ such that $\psi(V)$ is not a neighbourhood of $y$; it follows that for every $x' \in V \cap \psi^{-1}(y)$,
$\psi$ is not open at the point $x'$.

**Remark (14.1.5).**

<!-- label: IV.14.1.5 -->

Even if $X$ and $Y$ are locally Noetherian and $f$ is a finite morphism, it can happen that $f$ be open at all points of
a fibre $f^{-1}(y)$, without there existing a neighbourhood of $f^{-1}(y)$ at all points of which $f$ is open. Let for
example $K$ be a field, $A$ the polynomial ring $K[T_{1}, T_{2}, T_{3}]$, $V = \operatorname{Spec}(A)$ affine 3-space
over $K$, $X = \operatorname{Spec}(A/\mathfrak{a})$, where $\mathfrak{a} = \mathfrak{bc}$, with $\mathfrak{b} = (T_{3})$
and $\mathfrak{c} = (T_{1}) + (T_{2} - T_{3})$ in $A$, so that $X$ is the union of the plane $X_{1} =
\operatorname{Spec}(A/\mathfrak{b})$ ("plane of equation $T_{3} = 0$") and the line $X_{2} =
\operatorname{Spec}(A/\mathfrak{c})$ ("line of equations $T_{1} = 0$, $T_{2} = T_{3}$"), which are its irreducible
components. Take $Y = X_{1}$ and let $f : X \to Y$ be the projection corresponding to the canonical injection $K[T_{1},
T_{2}] \to A/\mathfrak{a}$; if $y$ is the point common to `X_1` and `X_2`, $f^{-1}(y)$ reduces to $y$ and $f$ is open at
this point but is open at no point of `X_2` in a neighbourhood of $y$ and distinct from $y$.

**(14.1.6)**

<!-- label: IV.14.1.6 -->

In what follows, the essential role will be played by the criterion `(1.10.3)` characterizing the morphisms locally of
finite presentation $f : X \to Y$ that are open at a point $x$ by "lifting of generizations": for every generization
$y'$ of $y = f(x)$, there exists $x' \in X$, a generization of $x$, such that $y' = f(x')$.

<!-- original page 201 -->

### 14.2. Open morphisms and the dimension formula

**Theorem (14.2.1).**

<!-- label: IV.14.2.1 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism, $x$ a point of $X$, $y = f(x)$. Suppose
that $f$ is open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$. Then one has the
relation*

```text
  (14.2.1.1)             dim(𝒪_x) = dim(𝒪_y) + dim_x(f⁻¹(y)).
```

Let $y'$ be any generization of $y$ distinct from $y$, and consider the reduced closed subprescheme $Y'$ of $Y$ with
underlying space $\overline{y'}$; then no irreducible component $X'$ of $f^{-1}(Y')$ containing $x$ can be contained in
$f^{-1}(y)$: indeed, if $x'$ is the generic point of $X'$, one would have $f(x') = y \neq y'$, and as $x'$ is its only
generization in $f^{-1}(Y')$, this would contradict the hypothesis that $f$ is open at the point $x'$, by virtue of the
fact that a) implies c) in `(1.10.3)`. One can therefore apply `(6.1.2)` to the local homomorphism of Noetherian rings
$\mathcal{O}_{y} \to \mathcal{O}_{x}$, whence the conclusion.

**Corollary (14.2.2).**

<!-- label: IV.14.2.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $y =
f(x)$. Suppose $f$ open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$. Then $f$ is
equidimensional at the point $x$ in each of the following two cases:*

*(i) $X$ is irreducible and $f$ is dominant.*

*(ii) The rings $\mathcal{O}_{x}$ and $\mathcal{O}_{y}$ are equidimensional.*

For (i), this results from `(14.2.1)` and `(13.2.3)`. For (ii), this results from `(14.2.1)` and `(13.3.6)`.

**Proposition (14.2.3).**

<!-- label: IV.14.2.3 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, $\eta$ its generic point, $f : X \to Y$ a morphism locally of
finite type, $y$ a point of $f(X)$, $Z$ an irreducible component of $f^{-1}(y)$ such that $f$ is open at the generic
point of $Z$. Then $Z$ is contained in an irreducible component $X'$ of $X$ dominating $Y$ and such that*

```text
  dim_z(X') = dim(𝒪_y) + dim(Z) = dim(𝒪_y) + dim_z(f⁻¹(y)).
```

This results indeed from `(14.2.1)` applied to the generic point of $Z$, and from `(13.2.7)`.

**Corollary (14.2.4).**

<!-- label: IV.14.2.4 -->

*With the notation of `(14.2.3)`, suppose that $f$ is open at all points of $f^{-1}(y)$. For every $z \in Y$, let $E(z)$
be the set of dimensions of the irreducible components of $f^{-1}(z)$ and $d(z) = \sup E(z) = \dim(f^{-1}(z))$. Then one
has $E(y) \subset E(\eta)$, whence $d(y) \leq d(\eta)$.*

This results at once from `(14.2.3)`.

**Corollary (14.2.5).**

<!-- label: IV.14.2.5 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism, $y \in Y$ a point such that $f$ is open at
all points of $f^{-1}(y)$. Then the function $z \mapsto \dim(f^{-1}(z))$ is constant in a neighbourhood of $y$.*

Let $Y_{i}$ ($1 \leq i \leq n$) be the reduced closed subpreschemes of $Y$ whose underlying spaces are the irreducible
components of $Y$ containing $y$; if $f_{i} : f^{-1}(Y_{i}) \to Y_{i}$ is the restriction of $f$, one knows that each of
the $f_{i}$ is proper `(II, 5.4.5)` and open at all points of $f^{-1}(y)$ `(14.1.2)`. As the union of the $Y_{i}$ is a
neighbourhood of $y$ in $Y$,

<!-- original page 202 -->

one sees that one may restrict to proving the corollary when $Y$ is irreducible; let $\eta$ be its generic point. It
follows from `(14.2.4)` that $d(y) \leq d(\eta)$; on the other hand, since $f$ is proper, one deduces from `(13.1.5)`
that $z \mapsto \dim(f^{-1}(z))$ is upper semi-continuous; in particular $d(y) \geq d(\eta)$, hence $d(y) = d(\eta)$.
Moreover, there is a neighbourhood $V$ of $y$ such that $d(z) \leq d(y)$ for every $z \in V$; but as $z$ is a
specialization of $\eta$, one has on the other hand $d(z) \geq d(\eta)$, whence finally $d(z) = d(y)$ for $z \in V$.

**Corollary (14.2.6).**

<!-- label: IV.14.2.6 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ an open morphism of finite type, $y$ a point of $Y$. Let
$y_{i}$ ($1 \leq i \leq n$) be the generic points of the irreducible components of $Y$ containing $y$. Then, with the
notation of `(14.2.4)`:*

*(i) If for $1 \leq i \leq n$, one has $E(y) = E(y_{i})$ (resp. $d(y) = d(y_{i})$), the function $E$ (resp. $d$) is
constant in a neighbourhood of $y$.*

*(ii) There exists an open neighbourhood $U$ of $f^{-1}(y)$ such that the function $z \mapsto \dim(U \cap f^{-1}(z))$ is
constant in a neighbourhood of $y$.*

(i) The same reasoning as in `(14.2.5)` shows that one may restrict to the case where $Y$ is irreducible, of generic
point $\eta$. If $y'$ is any generization of $y$, one has (applying `(14.2.4)` to the restriction $f^{-1}(Y') \to Y'$ of
$f$, where $Y' = \overline{y'}$, and using `(14.1.2)`) $E(y) \subset E(y') \subset E(\eta)$ and $d(y) \leq d(y') \leq
d(\eta)$; this shows that the relation $E(y) = E(\eta)$ (resp. $d(y) = d(\eta)$) entails $E(y) = E(y')$ (resp. $d(y) =
d(y')$) for every generization $y'$ of $y$. Now, by virtue of `(9.5.5)`, the functions $E$ and $d$ are locally
constructible, hence it follows from $(0_{III}, 9.2.5)$ applied to the set of $z$ such that $E(z) = E(y)$ (resp. $d(z) =
d(y)$) that this set is a neighbourhood of $y$.

(ii) For each of the $y_{i}$, $f^{-1}(y_{i})$ is a Noetherian space since $f$ is of finite type; let $x_{ij}$ ($1 \leq j
\leq m_{i}$) be the generic points of its irreducible components, and set $X_{ij} = \overline{x_{ij}}$; we show that the
complement $U$ in $X$ of the union of the $X_{ij}$ that do not meet $f^{-1}(y)$ (which is evidently an open
neighbourhood of $f^{-1}(y)$) answers the question. Indeed, the restriction $f|U : U \to Y$ of $f$ is an open morphism
of finite type `(I, 6.3.5)`; for every pair $(i, j)$ such that $x_{ij} \in U$, $x_{ij}$ is a maximal point of $U \cap
f^{-1}(y_{i})$ and it follows from `(13.1.1)` applied to the restriction $X_{ij} \to \overline{y_{i}}$ of $f$ (taking
into account `(I, 5.2.2)` and `(I, 5.4)`) that all the irreducible components of $X_{ij} \cap f^{-1}(y)$ have a
dimension $\geq \dim(X_{ij} \cap f^{-1}(y_{i}))$. Taking into account `(14.2.3)` applied to the restriction
$f^{-1}(Y_{i}) \to Y_{i}$ of $f$ which is an open morphism `(14.1.2)`, $f^{-1}(y)$ is, for each $i$, the union of the
irreducible components of $X_{ij} \cap f^{-1}(y)$ ($1 \leq j \leq m_{i}$), hence $\dim(f^{-1}(y)) \geq \dim(U \cap
f^{-1}(y))$; but since $f|U$ is open, one also has $\dim(f^{-1}(y)) \leq \dim(f^{-1}(y) \cap U)$ by virtue of
`(14.2.4)`; one sees therefore that one may apply (i) to $f|U$, whence the conclusion.

**Remark (14.2.7).**

<!-- label: IV.14.2.7 -->

The example `(13.2.12, (iii))` shows that under the hypotheses of `(14.2.5)` or `(14.2.6, (ii))`, one cannot, in the
conclusion, replace the function $z \mapsto \dim(f^{-1}(z))$ by the function $z \mapsto E(z)$; indeed, in that example,
$f$ is proper and flat (hence universally open `(2.4.6)`) and every neighbourhood of the unique point of $f^{-1}(y)$
contains the generic points of the irreducible components of $f^{-1}(\eta)$.

<!-- original page 203 -->

### 14.3. Universally open morphisms

**(14.3.1)**

<!-- label: IV.14.3.1 -->

Recall `(2.4.2)` that to say that a morphism $f : X \to Y$ is **universally open** signifies that for every morphism
$g : Y' \to Y$, $f_{(Y')} : X_{(Y')} \to Y'$ is open; it moreover suffices that this hold when
$Y' = Y[T_{1}, \cdots, T_{e}]$, for every $e$ `(8.10.2)` (and if $Y$ is locally Noetherian, it therefore suffices that
this hold for every locally Noetherian $Y'$).

**Proposition (14.3.2).**

<!-- label: IV.14.3.2 -->

*Let $f : X \to Y$ be a morphism of preschemes. If $f$ is universally open, then, for every morphism $g : Y' \to Y$,
where $Y'$ is irreducible, the image under $f' = f_{(Y')} : X_{(Y')} \to Y'$ of every irreducible component of
$X_{(Y')}$ is dense in $Y'$. Conversely, if this condition is satisfied for every irreducible $Y'$ and every morphism of
finite type $g : Y' \to Y$, and if moreover $f$ is locally of finite presentation, then $f$ is universally open.*

Indeed, it follows from `(1.10.4)` that if $f$ is universally open, it satisfies the condition of the statement.
Conversely, suppose that $f$ is locally of finite presentation, and let us show that for every integer $e$, if one sets
$Y'' = Y[T_{1}, \cdots, T_{e}]$, $f_{(Y'')}$ is open. Indeed, let $Y'$ be a closed subprescheme of `Y''` whose
underlying space is an irreducible closed part of `Y''`; the composite morphism $Y' \to Y'' \to Y$ is of finite type,
hence every irreducible component of $X_{(Y')}$ dominates $Y'$ by hypothesis; one therefore deduces from `(1.10.4)` that
$f_{(Y'')}$ is an open morphism.

This proposition shows that the definition `(III, 4.3.9)` coincides in the case considered with the general definition
of universally open morphisms given in `(2.4.2)`.

To the notion of morphism open at a point `(14.1.1)` likewise corresponds the following:

**Definition (14.3.3).**

<!-- label: IV.14.3.3 -->

*Let $f : X \to Y$ be a morphism of preschemes, $x$ a point of $X$. One says that $f$ is **universally open at the point
$x$** if, for every morphism $g : Y' \to Y$, setting $X' = X \times_{Y} Y'$, the morphism $f' = f_{(Y')} : X' \to Y'$ is
open at every point $x'$ of $X'$ whose projection in $X$ is $x$.*

**Remarks (14.3.3.1).**

<!-- label: IV.14.3.3.1 -->

*(i)* The reasoning of `(8.10.1)` shows (with the same notation) that if $x$ is a point of $X$ and $x_{\lambda}$ its
projection in $X_{\lambda}$, then, if $f_{\lambda}$ is open at the point $x_{\lambda}$ for every $\lambda \in X$, $f$ is
open at the point $x$; it suffices to restrict to the open sets $U$ of $X$ containing $x$ and to remark that the
hypothesis implies that $f_{\lambda}(U_{\lambda})$ is a neighbourhood of $f_{\lambda}(x_{\lambda})$, hence
$f(p^{-1}_{\lambda}(U_{\lambda}))$ is a neighbourhood of $f(x)$. One deduces that the statement `(8.10.2)` is still
exact when one replaces "universally open" by "universally open at the point $x$", and "open morphism" by "open morphism
at every point `x''` of `X''` whose projection in $X$ is $x$": it suffices in the proof to restrict to the open sets $V$
containing some `x''`.

*(ii)* The result of `(14.1.4)` remains valid for a morphism $f : X \to Y$, replacing "open" by "universally open".
Indeed, suppose that $f$ is not universally open at a point $x \in f^{-1}(y)$; there is consequently a morphism $Y' \to
Y$ and a point $x' \in X'$ projecting to $x$, such that $f'$ is not open at the point $x'$.

<!-- original page 204 -->

Now, if $y' = f'(x')$, the projection $f'^{-1}(y') \to f^{-1}(y)$ is an open morphism `(2.4.10)`, and there is, by
virtue of `(14.1.4)`, a neighbourhood $V$ of $x'$ in $f'^{-1}(y')$ where $f'$ is not open; hence $f$ is not universally
open at the points of the image of $V$ in $f^{-1}(y)$, which is a neighbourhood of $x$ in $f^{-1}(y)$.

**Proposition (14.3.4).**

<!-- label: IV.14.3.4 -->

*(i) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $x$ a point of $X$, $y = f(x)$. If $f$ is universally open at
the point $x$ and $g$ universally open at the point $y$, then $g \circ f$ is universally open at the point $x$.
Conversely, if $g \circ f$ is universally open at the point $x$, $g$ is universally open at the point $y$.*

*(ii) If $f : X \to Y$ is an $S$-morphism universally open at the point $x \in X$, then, for every base change $S' \to
S$, $f_{(S')} : X_{(S')} \to Y_{(S')}$ is universally open at every point of $X_{(S')}$ above $x$.*

*(iii) For $f : X \to Y$ to be universally open at the point $x \in X$, it is necessary and sufficient that $f_{red}$ be
so.*

*(iv) Let $f : X \to Y$ be a morphism locally of finite presentation, $x$ a point of $X$, $y = f(x)$; set $Y_{1} =
\operatorname{Spec}(\mathcal{O}_{y})$, $X_{1} = X \times_{Y} Y_{1}$, $f_{1} = f_{(Y_{1})}$. For $f$ to be universally
open at the point $x$, it is necessary and sufficient that $f_{1}$ be so* (one recalls `(I, 3.6.5)` that `X_1` is
canonically identified with a subspace of $X$).

Indeed (ii) is an evident consequence of the definition `(14.3.3)`; it also results from the definition that to prove
assertion (i), it suffices to do so when one suppresses the word "universally" everywhere, and this then results from
`(14.1.2)`. Assertion (iii) results from (ii) and from the fact that the canonical morphism $X_{red} \to X$ is
surjective. Finally, condition (iv) is trivially necessary. On the other hand, if it is satisfied, and if $g : Y' \to Y$
is an arbitrary morphism, $X' = X_{(Y')}$, $f' = f_{(Y')}$, $x'$ a point of $X'$ above $x$, then $f'$ is locally of
finite presentation, and to see that it is open at the point $x'$, it suffices to apply the criterion `(1.10.3, c))`.
Set $y' = f'(x')$, $Y'_{1} = \operatorname{Spec}(\mathcal{O}_{y'})$, $X'_{1} = X' \times_{Y'} Y'_{1}$, $f'_{1} =
f'_{(Y'_{1})}$. Since $g(y') = y$, the composite morphism $Y'_{1} \to Y' \to Y$ factors as $Y'_{1} \to Y_{1} \to Y$
`(I, 2.4.4)`, hence $X'_{1} = X_{1} \times_{Y_{1}} Y'_{1}$ and $f'_{1} = (f_{1})_{(Y'_{1})}$; the conclusion then
results at once from the hypothesis that $f_{1}$ is open at the point $x'$ and from `(1.10.3)`.

**Proposition (14.3.5).**

<!-- label: IV.14.3.5 -->

*Let $X$, $Y$ be two preschemes, $f : X \to Y$ a morphism, $x$ a point of $X$. Let $(Y_{i})_{1 \leq i \leq n}$ be a
locally finite family of closed subpreschemes of $Y$ such that the space $Y$ is the union of the $Y_{i}$, and suppose
that for every $i$ such that $f(x) \in Y_{i}$, the restriction $f^{-1}(Y_{i}) \to Y_{i}$ of $f$ is a morphism
universally open at the point $x$; then $f$ is universally open at the point $x$.*

Taking the definition into account, this results from the analogous proposition `(14.1.2, (ii))` for morphisms open at a
point.

**Proposition (14.3.6).**

<!-- label: IV.14.3.6 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type. For $f$ to be universally
open at a point $x \in X$, it is necessary and sufficient that the following condition be satisfied: for every morphism
$g : Y' \to Y$, where $Y' = \operatorname{Spec}(A)$ is the spectrum of a discrete valuation ring, such that the image
$g(y')$ of the closed point $y'$ of $Y'$ is equal to $y = f(x)$, and for every point $x' \in X' = X \times_{Y} Y'$ whose
projections on $X$ and $Y'$ are $x$ and $y'$ respectively, there exists a generization $z'$ of $x'$ in $X'$ whose
projection in $Y'$ is the generic point of $Y'$ (in other words, there exists an irreducible component of $X'$
containing $x'$ and dominating $Y'$).*

<!-- original page 205 -->

*Moreover, one may, in the preceding condition, restrict to the case where $A$ is complete, has an algebraically closed
residue field, and where $x'$ is rational over $k(y')$.*

If $Y'$ is as in the statement, the necessity of the condition results from the fact that $f'$ must be open at the point
$x'$, and from the criterion `(1.10.3)`. To see that the condition is sufficient, consider a morphism of finite type
$g : Y'' \to Y$, and let $X'' = X \times_{Y} Y''$, $f'' = f_{(Y'')} : X'' \to Y''$, and `x''` a point of `X''` above
$x$. Set $y'' = f''(x'')$, and let $t$ be a generization of `y''` in `Y''`, distinct from `y''`. Since `Y''` is locally
Noetherian, it follows from `(II, 7.1.9)` and $(0_{III}, 10.3.1)$ that there exists a scheme
$Y' = \operatorname{Spec}(A)$, where $A$ is a complete discrete valuation ring whose residue field is an algebraic
closure of $k(x'')$, and a morphism $g : Y' \to Y''$ such that, if $s'$ and $y'$ are the generic point and closed point
of $Y'$, one has $g(s') = t$ and $g(y') = y''$. There is then a point $x'$ of
$X' = X \times_{Y} Y' = X'' \times_{Y''} Y'$ whose projections in `X''` and $Y'$ are `x''` and $y'$ respectively, and
which is rational over $k(y')$ `(I, 3.4.9)`. The hypothesis implies that there is a generization $z'$ of $x'$ in $X'$
whose projection in $Y'$ is $s'$; if `z''` is the projection of $z'$ in `X''`, `z''` is a generization of `x''` and its
projection in `Y''` is $t$; one therefore concludes from `(1.10.3)` that `f''` is open at the point `x''`, hence that
$f$ is universally open at the point $x$ `(14.3.3.1, (i))`.

**Corollary (14.3.7).**

<!-- label: IV.14.3.7 -->

*The notation being that of `(14.3.6)`:*

*(i) Given a point $y \in Y$, for $f$ to be universally open at all points of $f^{-1}(y)$, it is necessary and
sufficient that for every morphism $g : Y' \to Y$, where $Y'$ is the spectrum of a discrete valuation ring, and where
the image $g(y')$ of the closed point $y'$ of $Y'$ is $y$, every irreducible component of $X' = X \times_{Y} Y'$
dominates $Y'$.*

*(ii) For $f$ to be universally open, it is necessary and sufficient that for every morphism $g : Y' \to Y$, where $Y'$
is the spectrum of a discrete valuation ring, every irreducible component of $X' = X \times_{Y} Y'$ dominates $Y'$.*

It is clear that it suffices to prove (i); the necessity of (i) results from `(14.3.2)` and its sufficiency from
`(14.3.6)`.

**Proposition (14.3.8).**

<!-- label: IV.14.3.8 -->

*Let $Y$ be a locally Noetherian prescheme, irreducible, regular and of dimension `1` (for example the spectrum of a
Dedekind ring), $f : X \to Y$ a morphism locally of finite type, $y$ a point of $Y$. The following conditions are
equivalent:*

*a) $f_{red}$ is flat at every point of $f^{-1}(y)$.*

*b) $f$ is universally open in a neighbourhood of $f^{-1}(y)$.*

*c) $f$ is open in a neighbourhood of $f^{-1}(y)$.*

*d) Every irreducible component of $X$ meeting $f^{-1}(y)$ dominates $Y$.*

Since $f_{red}$ is locally of finite type `(1.3.4)`, a) entails that $f_{red}$ is flat in a neighbourhood of $f^{-1}(y)$
`(11.1.1)`, and it suffices to apply `(2.4.6)` in such a neighbourhood to see that a) entails b). The implication b) ⟹
c) is trivial, and the implication c) ⟹ d) results from `(1.10.4)` applied to a neighbourhood of $f^{-1}(y)$. It remains
to see that d) entails a). One may obviously, by virtue of `(1.3.4)`, restrict to the case where $X$ is reduced. The
question being moreover local on $X$ and on $Y$, one may suppose $Y = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ affine; if $X_{i}$ ($1 \leq i \leq n$) are the closed (integral) subpreschemes of $X$ whose

<!-- original page 206 -->

underlying spaces are the irreducible components of $X$, then, for every $x \in X$, $\mathcal{O}_{X,x}$, being reduced,
is a sub-ring of the direct product of the $\mathcal{O}_{X_{i},x}$; if $y = f(x)$, it will suffice to show that each of
the $\mathcal{O}_{X_{i},x}$ is a torsion-free $\mathcal{O}_{y}$-module, for it will then be the same for
$\mathcal{O}_{X,x}$; as by hypothesis $\mathcal{O}_{y}$ is a regular local ring of dimension `1`, that is to say
`(II, 7.1.6)` a discrete valuation ring, it will then result from $(0_{I}, 6.3.4)$ that $\mathcal{O}_{X,x}$ is a flat
$\mathcal{O}_{y}$-module. But if $X_{i} = \operatorname{Spec}(B_{i})$, where $B_{i}$ is an integral ring, hypothesis d)
entails that the homomorphism $A \to B_{i}$ is injective `(I, 1.2.7)`; hence $B_{i}$ is a torsion-free $A$-module, and
*a fortiori* $\mathcal{O}_{X_{i},x}$ is a torsion-free $\mathcal{O}_{y}$-module.

**Remarks (14.3.9).**

<!-- label: IV.14.3.9 -->

*(i)* In the statement of `(14.3.8)`, one cannot dispense with the hypothesis that $Y$ is regular. With the notation of
`(11.7.5)`, take indeed $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(\hat{A})$, so that $f : X \to Y$ is a
finite surjective morphism; as $A$ is an integral local ring of dimension `1`, as is `Â`, it follows at once from
`(1.10.4)` that the morphism $f$ is open. However $f$ is not universally open (nor *a fortiori* flat), as is shown by
`(11.7.5)`. One would have an analogous example by taking for $Y$ the local scheme at the double point of an algebraic
curve having an "ordinary double point" and for $X$ the normalization of $Y$.

*(ii)* The example of `(14.1.3, (i))` shows that the set of points of $X$ where a morphism is universally open is not
necessarily open, the morphism $f$ in that example being universally open at all points where it is open. The example
$f : X \to Y$ seen above in (i) shows similarly that the set of points where a morphism is universally open is not
necessarily closed, for it is immediate that at all points of $X$ except one the morphism $f$ is universally open (it is
even a local isomorphism). It would be interesting to know whether the set of points where a morphism is universally
open is locally constructible.

The two following propositions have been pointed out to us by M. Artin:

**Lemma (14.3.10).**

<!-- label: IV.14.3.10 -->

*Let $A$ be a valuation ring (not necessarily discrete), $k$ its residue field, $K$ its field of fractions, and set $S =
\operatorname{Spec}(A)$. Let $X$ be an irreducible prescheme, $f : X \to S$ a dominant morphism of finite type; let
$X_{0} = X \otimes_{A} k$ (resp. $X_{1} = X \otimes_{A} K$) be the fibre of $f$ at the closed point (resp. at the
generic point) of $S$. Then, if $X_{0} \neq \emptyset$, one has $\dim(X_{0}) = \dim(X_{1})$.*

One may restrict to the case where $X$ is affine, replacing $X$ if need be by an affine open set containing a generic
point of an irreducible component of `X_0` of maximal dimension, and using `(4.1.1.3)`. Let $n = \dim(X_{0}) \geq 0$; it
follows from `(13.3.1.1)` that there exists a neighbourhood $U$ of `X_0` in $X$ and an $S$-morphism quasi-finite
$g : U \to S[T_{1}, \cdots, T_{n}] = Z$ such that the restriction morphism
$g_{0} : U_{0} = U \cap X_{0} \to Z_{0} = \operatorname{Spec}(k[T_{1}, \cdots, T_{n}])$ is finite and surjective. By the
base change $\operatorname{Spec}(K) \to S$ and restriction to the open set $U_{1} = U \cap X_{1}$ of `X_1`, one deduces
from $g$ a quasi-finite morphism $g_{1} : U_{1} \to Z_{1} = \operatorname{Spec}(K[T_{1}, \cdots, T_{n}])$. Since `U_1`
is dense in `X_1`, one has $\dim(U_{1}) = \dim(X_{1})$ `(4.1.1.3)`; the proposition will be established, by virtue of
`(4.1.2)`, if we prove that the morphism $g_{1}$ is dominant. Suppose the contrary; there would then exist a non-zero
polynomial $F_{1} \in K[T_{1}, \cdots, T_{n}]$ such that $g_{1}(U_{1}) \subset V(F_{1})$. If $\omega$ is a valuation on
$K$ associated with $A$, and if $(c_{\alpha})$ is the family of coefficients of `F_1`, one may, after multiplication of
`F_1` by a non-zero element of $K$, suppose that one has $\inf_{\alpha}(\omega(c_{\alpha})) = 0$; in other words, `F_1`
comes from a polynomial $F \in A[T_{1}, \cdots, T_{n}]$

<!-- original page 207 -->

(with which it identifies) such that the image `F_0` of $F$ in $k[T_{1}, \cdots, T_{n}]$ is non-zero. Consider then in
$Z$ the closed set $V(F)$; one has $V(F) \cap Z_{1} = V(F_{1})$, and as `U_1` is dense in $U$ (since it contains the
generic point of $X$), $g(U) \subset V(F)$; in

<!-- original page 208 -->

particular, one would have $g_{0}(U_{0}) \subset V(F) \cap Z_{0} = V(F_{0})$; but since $F_{0} \neq 0$, $V(F_{0})$ is a
closed part of `Z_0` distinct from `Z_0`, and one reaches a contradiction. Q.E.D.

**Proposition (14.3.11).**

<!-- label: IV.14.3.11 -->

*Let $f : X \to S$ be a morphism of finite type, $(g_{\lambda})_{\lambda \in L}$ a family of universally open morphisms
$g_{\lambda} : Y_{\lambda} \to S$, and for every $\lambda \in L$, let $u_{\lambda} : Y_{\lambda} \to X$ be an
$S$-morphism. For every $s \in S$, set $X_{s} = X \times_{S} \operatorname{Spec}(k(s))$, $(Y_{\lambda})_{s} =
Y_{\lambda} \times_{S} \operatorname{Spec}(k(s))$, and let $(u_{\lambda})_{s} : (Y_{\lambda})_{s} \to X_{s}$ be the
morphism $u_{\lambda} \times_{S} 1$ deduced from $u_{\lambda}$ by base change. Let $Z(s)$ be the closure in $X_{s}$ of
the union of the sets $(u_{\lambda})_{s}((Y_{\lambda})_{s})$, and set $d(s) = \dim(Z(s))$. Then, for every generization
$s'$ of a point $s \in S$, one has $d(s) \leq d(s')$.*

One knows `(II, 7.1.4)` that there exists a valuation ring $A'$ and a morphism $h : S' = \operatorname{Spec}(A') \to S$
such that if $a$ (resp. $b$) is the closed point (resp. the generic point) of $S'$, one has $h(a) = s$, $h(b) = s'$.
Moreover, the projection morphism $p : X_{s} \otimes_{k(s)} k(a) \to X_{s}$ is surjective and open `(2.4.10)`, hence
makes $X_{s}$ a quotient space of $X_{s} \otimes_{k(s)} k(a)$ by an open equivalence relation; for every part $M$ of
$X_{s}$, $p^{-1}(\bar{M})$ is therefore equal to the closure $\overline{p^{-1}(M)}$ (Bourbaki, *Top. gén.*, chap. I, 4th
ed., §5, n° 3, prop. 7); one reasons similarly for $X_{s'}$, and taking into account `(I, 3.4.8)`, `(4.2.7)` and the
fact that the $g_{\lambda}$ are universally open, one sees that one may reduce to proving the proposition in the
situation obtained after base change $S' \to S$. Suppose therefore $S' = S$, $s$ being the closed point and $s'$ the
generic point of $S$. The hypothesis that $g_{\lambda}$ is open entails that every irreducible component of
$Y_{\lambda}$ dominates $S$ `(1.10.4)`, hence that its generic point is a maximal point of $(Y_{\lambda})_{s'}$; if $Z$
denotes the closure in $X$ of $Z(s')$, one therefore has $u_{\lambda}(Y_{\lambda}) \subset Z$, and consequently
$(u_{\lambda})_{s}((Y_{\lambda})_{s}) \subset Z_{s} = Z \cap X_{s}$; in other words, one has $Z(s) \subset Z_{s}$,
whence $\dim(Z(s)) \leq \dim(Z_{s})$. But applying `(14.3.10)` to a reduced subprescheme of $X$ whose underlying space
is an irreducible component of $Z$, one obtains $\dim(Z_{s}) \leq \dim(Z_{s'})$ (the inequality coming from the fact
that there may be irreducible components of $Z$ not meeting $X_{s}$). On the other hand, since $Z(s')$ is by definition
closed in $X_{s'}$, one has $Z_{s'} = Z(s')$, which completes the proof.

**Remark (14.3.12).**

<!-- label: IV.14.3.12 -->

The case envisaged by M. Artin was that where $Y_{\lambda} = S$ for every $\lambda$, in other words the case where
$(u_{\lambda})$ is a family of $S$-sections of $X$. Another useful case is that where the family $(u_{\lambda})$ is
reduced to a single element; one can moreover always reduce to this case by considering the prescheme $Y$ sum of the
$Y_{\lambda}$ and the morphisms $g : Y \to S$ and $u : Y \to X$ whose restrictions to each $Y_{\lambda}$ are
respectively $g_{\lambda}$ and $u_{\lambda}$.

**Proposition (14.3.13).**

<!-- label: IV.14.3.13 -->

*Let $f : X \to Y$ be a morphism locally of finite type, $y$ a point of $Y$, $x$ a maximal point of the fibre $X_{y} = X
\times_{Y} \operatorname{Spec}(k(y))$.*

*Consider the following conditions:*

*a) $f$ is universally open at the point $x$ (or equivalently, at every point of the irreducible component of $X_{y}$ of
generic point $x$ `(14.3.3.1, (ii))`).*

*b) For every irreducible component `Y_0` of $Y$ containing $y$, there exists an irreducible component $Z$ of $X$
containing $x$, dominating `Y_0` and such that `dim_x(X_y) = dim_x(Z ∩ X_y) ≤ dim(Z ∩ X_η)`, where $\eta$ is the generic
point of `Y_0` (which entails that $Z$ is equidimensional over `Y_0` at the point $x$ `(13.2.2)`).*

<!-- original page 209 -->

*b') For every open neighbourhood $U$ of $x$ in $X$ and every generization $y'$ of $y$, one has $\dim(U \cap X_{y'})
\geq \dim_{x}(U \cap X_{y})$.*

*Then one has the implications a) ⟹ b) ⟺ b').*

To show that b) implies b'), it suffices to remark that $y'$ belongs to an irreducible component `Y_0` of $Y$ containing
$y$, of generic point $\eta$; taking $Z$ as in b) and noting that the generic point of $Z$ (which is also that of $Z
\cap X_{\eta}$ $(0_{I}, 2.1.8)$) is contained in $U$, one has $\dim(U \cap X_{y'}) \geq \dim(U \cap Z \cap X_{y'})$,
and, by virtue of `(13.1.6)`, $\dim(U \cap Z \cap X_{y'}) \geq \dim(Z \cap X_{\eta})$; whence the assertion, since
$\dim_{x}(U \cap X_{y}) = \dim_{x}(X_{y})$ `(4.1.1.3)`.

To prove that b') implies b), one may first replace $X$ by $f^{-1}(Y_{0})$, hence suppose $Y_{0} = Y$; one may restrict
to the case where $X$ and $Y$ are affine, since $\dim_{x}(U \cap X_{y}) = \dim_{x}(X_{y})$ `(4.1.1.3)`. The irreducible
components $W_{i}$ of the Noetherian prescheme $X_{y}$ are then finite in number, and the complement of the union of the
$\bar{W}_{i}$ (closures in $X$) that do not contain $x$ is an open neighbourhood $V$ of $x$. Replacing $X$ by $V$, one
may therefore suppose that $x \in \bar{W}_{i}$ for every $i$ (hypothesis b') entails $\dim(V \cap X_{y}) \geq 0$, hence
$x$ belongs to one of the $\bar{W}_{i}$ for at least one $i$). Moreover, the $\bar{W}_{i}$ are exactly the irreducible
components of $X$ that dominate $Y$ $(0_{I}, 2.1.8)$; this being so, if one had, for each of these components $Z$,
$\dim(Z \cap X_{\eta}) < \dim_{x}(X_{y})$, one would conclude $\dim(X_{\eta}) < \dim_{x}(X_{y})$, contrary to hypothesis
b'). The relation $\dim_{x}(Z \cap X_{y}) = \dim(Z \cap X_{\eta})$ then results from `(13.1.6)`.

It remains to prove that a) entails b'). Taking `(II, 7.1.4)` and the invariance of the hypotheses and the conclusion
under base change into account (by virtue of `(4.2.7)`), one may restrict to the case where $Y$ is a spectrum of a
valuation ring, with closed point $y$ and generic point $y'$, and where $U = X$. The hypothesis that $f$ is open at the
point $x$ entails that there exists an irreducible component $Z$ of $X$ containing $x$ and dominating $Y$ `(1.10.3)`.
Applying `(14.3.10)` to a neighbourhood of $x$ in $Z$, one concludes that $\dim(Z \cap X_{y'}) = \dim(Z \cap X_{y})$;
but since $x$ is maximal in $X_{y}$, $Z \cap X_{y}$ contains the irreducible component of $X_{y}$ of generic point $x$,
hence $\dim_{x}(Z \cap X_{y}) = \dim_{x}(X_{y})$; on the other hand, one has $\dim(X_{y'}) \geq \dim(Z \cap X_{y'})$,
which completes the proof of b').

**Remark (14.3.14).**

<!-- label: IV.14.3.14 -->

We do not know whether in `(14.3.13)` the conclusion remains valid when one replaces the hypothesis a) by the weaker
hypothesis that $f$ is open at the point $x$. One may show easily that it would suffice to treat the case where $Y$ is
the spectrum of an integral local ring whose generic point is isolated, and where $X$ is a closed subprescheme of the
vector bundle `Y[T]`.

### 14.4. Chevalley's criterion for universally open morphisms

**Theorem (14.4.1).**

<!-- label: IV.14.4.1 -->

*Let $f : X \to Y$ be a morphism locally of finite type, $y$ a point of $Y$, $x$ a maximal point of the fibre $X_{y} = X
\times_{Y} \operatorname{Spec}(k(y))$. Suppose $y$ geometrically unibranch. Then the following conditions are
equivalent:*

*a) $f$ is universally open at the point $x$ (or equivalently, at every point of the irreducible component of $X_{y}$ of
generic point $x$ `(14.3.3.1, (ii))`).*

<!-- original page 210 -->

*b) If `Y_0` is the unique irreducible component of $Y$ containing $y$ and $\eta$ its generic point, there exists an
irreducible component $Z$ of $X$ containing $x$, dominating `Y_0` and such that $\dim_{x}(Z \cap X_{y}) = \dim(Z \cap
X_{\eta})$ (which signifies that $Z$ is equidimensional over `Y_0` at the point $x$ `(13.2.2)`).*

*b') For every open neighbourhood $U$ of $x$ in $X$ and every generization $y'$ of $y$, one has $\dim(U \cap X_{y'})
\geq \dim_{x}(U \cap X_{y})$.*

*If moreover $Y$ is locally Noetherian, these conditions are also equivalent to the following:*

*c) $f$ is open at the point $x$.*

Note first that since $(\mathcal{O}_{y})_{red}$ is integral, $y$ belongs to only one irreducible component `Y_0` of $Y$.
The fact that b) and b') are equivalent and that a) implies b') results from `(14.3.13)`; on the other hand, if $Y$ is
locally Noetherian, one has seen in `(14.2.3)` that c) implies b). It therefore remains to show that when $y$ is
geometrically unibranch, b) entails a).

**Lemma (14.4.1.1).**

<!-- label: IV.14.4.1.1 -->

*Let $Y$ be a prescheme, $Y' = Y[T_{1}, \cdots, T_{n}]$, $y'$ a point of $Y'$, $y$ its image in $Y$. If $Y$ is
geometrically unibranch at the point $y$, then $Y'$ is geometrically unibranch at the point $y'$.*

Indeed, since for every $y \in Y$, $\operatorname{Spec}(k(y)[T_{1}, \cdots, T_{n}])$ is geometrically regular over
$k(y)$ `(0, 17.3.7)`, the structure morphism $Y' \to Y$ is smooth `(6.8.1)`, and it suffices to apply `(11.3.14)`.

**Lemma (14.4.1.2).**

<!-- label: IV.14.4.1.2 -->

*Let $A$ be an integral unibranch local ring, $B$ an integral ring containing $A$ and integral over $A$, $\mathfrak{n}$
a prime ideal of $B$ above the maximal ideal $\mathfrak{m}$ of $A$. Then the morphism
$\operatorname{Spec}(B_{\mathfrak{n}}) \to \operatorname{Spec}(A)$ is surjective; in other words, for every prime ideal
$\mathfrak{p}$ of $A$, there exists a prime ideal $\mathfrak{q}$ of $B$ such that $\mathfrak{q} \subset \mathfrak{n}$
and $\mathfrak{q} \cap A = \mathfrak{p}$.*

Let $K$ (resp. $L$) be the field of fractions of $A$ (resp. $B$), $A'$ the integral closure of $A$, $B'$ the sub-ring of
$L$ generated by $A'$ and $B$, so that one has a commutative diagram of canonical injections

```text
                B  ─→  B'
                ↑       ↑
                A  ─→  A'
```

As $B'$ is integral over $B$, there exists a prime ideal $\mathfrak{n}'$ of $B'$ such that $\mathfrak{n}' \cap B =
\mathfrak{n}$ (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, th. 1), and (for the same reason) $\operatorname{Spec}(A') \to
\operatorname{Spec}(A)$ is surjective. On the other hand, since $A$ is unibranch, $A'$ is a local ring; hence
$\mathfrak{n}' \cap A'$, which is above the maximal ideal $\mathfrak{m}$ of $A$, is necessarily equal to the unique
maximal ideal $\mathfrak{m}'$ of $A'$. By virtue of the second Cohen-Seidenberg theorem (*loc. cit.*, §2, n° 4, th. 3),
the morphism $\operatorname{Spec}(B'_{\mathfrak{n}'}) \to \operatorname{Spec}(A')$ is surjective, hence so is the
composite `Spec(B'_{𝔫'}) → Spec(A') → Spec(A)`; but this morphism is also the composite
`Spec(B'_{𝔫'}) → Spec(B_𝔫) → Spec(A)`, hence the morphism $\operatorname{Spec}(B_{\mathfrak{n}}) \to
\operatorname{Spec}(A)$ is surjective.

These lemmas being established, let us return to the proof of the implication b) ⟹ a) in `(14.4.1)`. By virtue of
`(14.3.3.1, (i))`, it suffices to prove that, for every integer $n \geq 0$ and every point $x'$ of $X' = X[T_{1},
\cdots, T_{n}]$ above $x$, the morphism

<!-- original page 211 -->

$f' : X' \to Y' = Y[T_{1}, \cdots, T_{n}]$, deduced from $f$ by base change, is open at the point $x'$. Taking the lemma
`(14.4.1.1)`, `(2.3.4)` and `(4.2.7)` into account, one is therefore reduced to proving that $f$ is open at the point
$x$: moreover, it evidently suffices `(14.1.2, (iii))` to show that the restriction of $f$ to a closed subprescheme of
$X$ having $Z$ for underlying space is open at the point $x$, so that one may restrict to the case where $X = Z$ is
irreducible. Replacing $X$ by an open neighbourhood $V$ of $x$ such that $V \cap X_{y}$ is irreducible, one may suppose,
by virtue of `(13.3.1)`, that the morphism $f$ factors as $X \to Y'' = Y[T_{1}, \cdots, T_{m}] \to Y$, where $g$ is
quasi-finite, dominant and locally of finite type. As the structure morphism $Y'' \to Y$ is open `(2.4.6)`, one is
reduced to proving that $g : X \to Y''$ is open at the point $x$. Moreover, by virtue of `(14.4.1.1)`, $g(x)$ is a
geometrically unibranch point of `Y''`. One is therefore reduced to proving the following lemma:

**Lemma (14.4.1.3).**

<!-- label: IV.14.4.1.3 -->

*Let $X$, $Y$ be two irreducible preschemes, $f : X \to Y$ a morphism locally quasi-finite and dominant. If $x \in X$ is
such that $y = f(x)$ is unibranch over $Y$, then $f$ is open at the point $x$.*

It suffices to prove that $f(\operatorname{Spec}(\mathcal{O}_{X,x})) = \operatorname{Spec}(\mathcal{O}_{Y,y})$
`(1.10.3)`. One may therefore restrict, by the base change $\operatorname{Spec}(\mathcal{O}_{Y,y}) \to Y$, to the case
where $Y = \operatorname{Spec}(A)$, where $A$ is a local ring and $y$ is the closed point of $Y$ (taking into account
`(I, 3.6.5)` and $(0_{I}, 2.1.8)$, which prove that $X \times_{Y} \operatorname{Spec}(\mathcal{O}_{Y,y})$ is
irreducible); replacing $f$ by $f_{red}$, one may suppose $X$ and $Y$ reduced, hence integral. Replacing if necessary
$X$ and $Y$ by affine neighbourhoods of $x$ and $y$ respectively, one may suppose `(8.12.9)` that the morphism $f$
factors as $X \to X_{1} \to Y$, where $j$ is an open immersion and $g$ a *finite* morphism (evidently dominant); as $X$
and `X_1` are affine, $j$ is affine, hence separated and quasi-compact, and consequently factors as $X \to X_{2} \to
X_{1}$, where `X_2` is the closed image of $X$ by $j$, $h$ the canonical injection and $u$ an open immersion
`(I, 9.5.3)`. In other words, one may suppose that `X_1` is integral, or also of the form $X_{1} =
\operatorname{Spec}(B)$, where $B$ is an integral and finite $A$-algebra, containing $A$ since $g$ is dominant. If
$\mathfrak{n}$ is the prime ideal of $B$ corresponding to the point $x$, the hypothesis that $A$ is unibranch then
implies `(14.4.1.2)` that the morphism $\operatorname{Spec}(B_{\mathfrak{n}}) \to \operatorname{Spec}(A)$ is surjective,
that is, $\operatorname{Spec}(\mathcal{O}_{X,x}) \to \operatorname{Spec}(\mathcal{O}_{Y,y})$ is surjective. Q.E.D.

**Corollary (14.4.2).**

<!-- label: IV.14.4.2 -->

*Let $f : X \to Y$ be a morphism locally of finite type, $y$ a geometrically unibranch point of $Y$, $\eta$ the generic
point of the unique irreducible component `Y_0` of $Y$ containing $y$. The following conditions are equivalent:*

*a) $f$ is universally open at all points of $X_{y}$ (or, what comes to the same `(14.3.3.1, (ii))`, at the maximal
points of $X_{y}$).*

*b) For every $x \in X_{y}$, there exists an irreducible component $Z$ of $X$ containing $x$ and equidimensional over
$Y$ at the point $x$ `(13.2.2)`.*

*b') For every $x \in X_{y}$ and every open neighbourhood $U$ of $x$ in $X$, one has $\dim(U \cap X_{\eta}) \geq
\dim_{x}(U \cap X_{y})$.*

*b'') For every open $U$ of $X$, one has $\dim(U \cap X_{\eta}) \geq \dim(U \cap X_{y})$.*

<!-- original page 212 -->

*When moreover $Y$ is locally Noetherian, these conditions are still equivalent to the following:*

*c) $f$ is open at all points of $X_{y}$ (or, what comes to the same `(14.3.3.1, (ii))`, at the maximal points of
$X_{y}$).*

The equivalence of a) and c) when $Y$ is locally Noetherian results from `(14.4.1)`; conditions b) or b'), applied to
the maximal points of $X_{y}$, entail a) by virtue also of `(14.3.3.1, (ii))`; finally, b') and b'') are equivalent,
since

```text
   dim(U ∩ X_y) = sup_x(dim_x(U ∩ X_y)).
```

It remains to see that condition a) entails b) and b') at every point $x \in X_{y}$. Set $d = \dim_{x}(X_{y})$, and let
$x'$ be the generic point of an irreducible component of $X_{y}$ containing $x$ and of dimension $d$. By virtue of a)
and of `(14.4.1)`, there is an irreducible component $Z$ of $X$ containing $x'$ and equidimensional over $Y$ at the
point $x'$, hence such that $\dim_{x'}(Z \cap X_{y}) = \dim(Z \cap X_{\eta})$. But by construction $\dim_{x'}(Z \cap
X_{y}) = \dim_{x'}(X_{y}) = d$, and $\dim_{x}(Z \cap X_{y}) \leq \dim(Z \cap X_{y}) = d$; taking `(13.1.6)` into
account, this proves that $Z$ is equidimensional over $Y$ at the point $x$; hence a) entails b). Moreover, one has
`dim(X_η) ≥ dim(Z ∩ X_η) = d = dim_x(X_y)`. Replacing $X$ by an open neighbourhood $U$ of $x$, one sees thus that a)
entails b'). Q.E.D.

**Corollary (14.4.3).**

<!-- label: IV.14.4.3 -->

*Let $Y$ be a geometrically unibranch prescheme, $f : X \to Y$ a morphism locally of finite type. The following
conditions are equivalent:*

*a) $f$ is universally open.*

*b) For every open $U$ of $X$, every $y \in Y$ and every generization $y'$ of $y$ one has $\dim(U \cap X_{y'}) \geq
\dim(U \cap X_{y})$.*

*If moreover $Y$ is locally Noetherian, these conditions are also equivalent to the following:*

*c) $f$ is open.*

**Corollary (14.4.4) (Chevalley's criterion).**

<!-- label: IV.14.4.4 -->

*Let $f : X \to Y$ be a morphism locally of finite type.*

*(i) If $f$ is equidimensional at a point $x \in X$ `(13.3.2)` and if $y = f(x)$ is a geometrically unibranch point of
$Y$, $f$ is universally open at the point $x$.*

*(ii) If $Y$ is geometrically unibranch, $f$ is universally open at all points of $X$ where $f$ is equidimensional, and
the set of these points is open in $X$. In particular, if $f$ is equidimensional, it is universally open.*

Assertion (ii) is a trivial consequence of (i), since one already knows that the set of points where $f$ is
equidimensional is open `(13.3.2)`. As for assertion (i), it results from the fact that the hypothesis implies that
condition b) of `(14.4.1)` is satisfied at the generic point of an irreducible component of $X_{y}$ containing $x$,
taking `(13.3.1)` into account; it therefore suffices to apply `(14.4.1)`.

**Remark (14.4.5).**

<!-- label: IV.14.4.5 -->

One can prove that if $Y$ is locally Noetherian, and if all the generizations of $y = f(x)$ are geometrically unibranch
points of $Y$ (cf. `(6.15.2)`), then, if $f$ is equidimensional at the point $x$, it is universally open in a
neighbourhood of $x$.

<!-- original page 213 -->

**Corollary (14.4.6).**

<!-- label: IV.14.4.6 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type. Let $y$ be a geometrically
unibranch point of $Y$, and suppose in addition that for every $x \in f^{-1}(y)$, the ring $\mathcal{O}_{x}$ is
equidimensional. Then the following conditions are equivalent:*

*a) $f$ is equidimensional `(13.3.2)` at all points of $f^{-1}(y)$.*

*b) $f$ is open at all points of $f^{-1}(y)$.*

*c) $f$ is universally open at all points of $f^{-1}(y)$.*

Indeed, c) trivially implies b), and a) implies c) by virtue of `(14.4.4)`; finally, in view of the hypotheses on
$\mathcal{O}_{y}$ and $\mathcal{O}_{x}$, b) implies a) by `(14.2.2)`. More generally:

**Proposition (14.4.7).**

<!-- label: IV.14.4.7 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, such
that $y = f(x)$ is geometrically unibranch. The following conditions are equivalent:*

*a) $f$ is equidimensional `(13.3.2)` at the point $x$.*

*b) The ring $\mathcal{O}_{x}$ is equidimensional and $f$ is open at the generic points of the irreducible components of
$f^{-1}(y)$ containing $x$ (hence also at every point of such a component).*

*c) The ring $\mathcal{O}_{x}$ is equidimensional, and $f$ is universally open at the generic points of the irreducible
components of $f^{-1}(y)$ containing $x$ (hence also at every point of such a component).*

*Moreover, when these conditions are satisfied, for every reduced closed subprescheme $X_{i}$ of $X$ whose underlying
space is an irreducible component of $X$ containing $x$, the restriction $f_{i} : X_{i} \to Y$ of $f$ is a morphism
equidimensional at the point $x$, and universally open at all points of the irreducible components of $f^{-1}_{i}(y)
\cap X_{i}$ that contain $x$.*

Condition a) implies that $f$ is equidimensional at all generic points of the irreducible components of $f^{-1}(y)$
containing $x$ `(13.3.1)`, and consequently `(14.4.4)` universally open at these points; the same reasoning applied to
each $f_{i}$ (taking `(13.3.3)` into account) proves the last assertion of the proposition, taking `(14.3.3.1, (ii))`
into account. Moreover, by `(14.2.1)`, one has the relations

```text
  (14.4.7.1)              dim(𝒪_{X_i,x}) = dim(𝒪_y) + dim_x(f_i⁻¹(y))

  (14.4.7.2)              dim(𝒪_x) = dim(𝒪_y) + dim_x(f⁻¹(y))
```

and since $f$ is equidimensional at the point $x$, it results from `(13.3.1)` that one has

```text
  dim_x(f⁻¹(y)) = dim_x(f_i⁻¹(y))    for every i.
```

One therefore concludes that $\dim(\mathcal{O}_{X_{i},x}) = \dim(\mathcal{O}_{x})$ for every $i$, in other words
$\mathcal{O}_{x}$ is equidimensional, and this completes the proof that a) entails c). It is clear that c) entails b);
finally, b) entails the relation `(14.4.7.2)` by virtue of `(14.2.1)`; it then results from `(13.3.6)` that b) entails
a).

**Proposition (14.4.8).**

<!-- label: IV.14.4.8 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $y$ a point of $Y$, $x$ a maximal
point of $X_{y} = f^{-1}(y)$. The following conditions are equivalent:*

*a) The morphism $f$ is universally open at the point $x$, in other words, for every base change $g : Y' \to Y$, one has
the property P(Y'): for every point $x'$ of $X' = X \times_{Y} Y'$ above $x$, the morphism $f' = f_{(Y')} : X' \to Y'$
is open at the point $x'$.*

<!-- original page 214 -->

*a') Property P(Y') is true for every finite morphism $g : Y' \to Y$.*

*a'') Property P(Y'') is true for the normalization `Y''` of $Y_{red}$ `(II, 6.3.8)`.*

*b) For every point `x''` of $X'' = X \times_{Y} Y''$ above $x$, there exists an irreducible component `Z''` of `X''`
containing `x''` and equidimensional over `Y''` at the point `x''`.*

It is trivial that a) implies a'). To show that a') implies a''), note that one may write $Y'' =
\operatorname{Spec}(\mathcal{B})$, where $\mathcal{B}$ is a quasi-coherent $\mathcal{O}_{Y}$-Algebra integral over
$\mathcal{O}_{Y}$; as $Y$ is Noetherian, $\mathcal{B}$ is the inductive limit of its sub-$\mathcal{O}_{Y}$-Algebras
$\mathcal{B}_{\lambda}$ which are quasi-coherent and of finite type `(I, 9.6.6)`; but then the $\mathcal{B}_{\lambda}$
are finite $\mathcal{O}_{Y}$-Algebras `(II, 6.1.2)`; one may therefore write $Y'' = \lim Y'_{\lambda}$, where
$Y'_{\lambda} = \operatorname{Spec}(\mathcal{B}_{\lambda})$, whence $X'' = X \times_{Y} Y'' = \lim X'_{\lambda}$, with
$X'_{\lambda} = X \times_{Y} Y'_{\lambda}$. By virtue of a'), the morphisms $f'_{\lambda} : X'_{\lambda} \to
Y'_{\lambda}$ are open at all points of $X'_{\lambda}$ above $x$; one concludes that `f''` is open at all points of
`X''` above $x$, by `(8.10.1)` and `(14.3.3.1, (i))`.

As the prescheme `Y''` is normal by definition, the fact that b) entails a'') results from `(14.4.4)` applied to the
equidimensional irreducible component of the statement and to the restriction of `f''` to this component. It remains
therefore to show that a'') entails a) and b). Taking `(1.10.3)` into account, one may restrict to the case where $Y =
\operatorname{Spec}(\mathcal{O}_{y})$, noting that the canonical morphism $\operatorname{Spec}(\mathcal{O}_{y}) \to Y$
is universally bicontinuous `(I, 3.6.5)`, and on the other hand that $Y'' \times_{Y}
\operatorname{Spec}(\mathcal{O}_{y})$ is the normalization of $(\operatorname{Spec}(\mathcal{O}_{y}))_{red}$ as it
results from the permutability of the operations of integral closure and of localization (Bourbaki, *Alg. comm.*, chap.
V, §1, n° 5, prop. 16). Supposing therefore $Y = \operatorname{Spec}(A)$, where $A$ is a Noetherian local ring, and $y$
the closed point of $Y$, one knows `(0, 23.2.5)` that there exists a factorization

```text
   Y''  ─v─→  Y_1  ─u─→  Y
```

of the structure morphism, such that $v$ is a finite surjective morphism, $u$ an integral, radicial and dominant (hence
surjective `(II, 6.1.10)`, and consequently a universal homeomorphism `(2.4.5)`) morphism. If one sets $X_{1} = X
\times_{Y} Y_{1}$, the projection $X'' \to X_{1}$ is therefore a homeomorphism, and hypothesis a'') consequently entails
that $f_{1} = f_{(Y_{1})} : X_{1} \to Y_{1}$ is open at all points of `X_1` above $x$. Moreover, this shows that to
prove property b), it suffices to prove the same property where one replaces `Y''`, `X''` and `x''` by `Y_1`, `X_1` and
a point $x_{1}$ of `X_1` above $x$. But `Y_1` is Noetherian and moreover it is geometrically unibranch since `Y''` is
normal and $u$ radicial `(6.15.1)`; the property to be proven thus results from `(14.4.1)`. It remains to show that $f$
is universally open at the point $x$, which will result from the following lemma:

**Lemma (14.4.8.1).**

<!-- label: IV.14.4.8.1 -->

*Let $v : Y_{1} \to Y$ be a closed (resp. universally closed) and surjective morphism. For a morphism $f : X \to Y$ to
be open (resp. universally open) at a point $x \in X$, it suffices that $f_{1} = f_{(Y_{1})} : X_{1} = X \times_{Y}
Y_{1} \to Y_{1}$ be open (resp. universally open) at all points of `X_1` above $x$.*

The second assertion results trivially from the first and from the fact that for every base change $Y' \to Y$, the
morphism $v_{(Y')} : Y_{1} \times_{Y} Y' \to Y'$ is still surjective and is closed if $v$ is universally closed. To
prove the first assertion, consider

<!-- original page 215 -->

an open neighbourhood $U$ of $x$ in $X$; as $v$ is closed and surjective, for $f(U)$ to be a neighbourhood of $y =
f(x)$, it is necessary and sufficient that $v^{-1}(f(U))$ be a neighbourhood of $v^{-1}(y)$. But if $p : X_{1} \to X$ is
the canonical projection, one has $v^{-1}(f(U)) = f_{1}(p^{-1}(U))$ `(I, 3.4.8)`, and the hypothesis implies that
$f_{1}(p^{-1}(U))$ is a neighbourhood of $f_{1}(p^{-1}(x)) = v^{-1}(y)$ `(I, 3.4.8)`.

**Corollary (14.4.9).**

<!-- label: IV.14.4.9 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type. The following conditions are
equivalent:*

*a) $f$ is universally open, in other words, for every base change $Y' \to Y$, the morphism $f_{(Y')} : X \times_{Y} Y'
\to Y'$ is open.*

*a') For every finite morphism $Y_{1} \to Y$, $f_{(Y_{1})}$ is open.*

*a'') If `Y''` is the normalization of $Y_{red}$, $f_{(Y'')}$ is open.*

*b) For every point `x''` of $X'' = X \times_{Y} Y''$, there exists an irreducible component `Z''` of `X''` containing
`x''` and equidimensional over `Y''` at the point `x''` (cf. `(14.4.10, (ii))`).*

This results at once from `(14.4.8)` and `(14.1.4)`.

**Remarks (14.4.10).**

<!-- label: IV.14.4.10 -->

*(i)* The equivalence of conditions a) and b) in `(14.4.8)` (resp. `(14.4.9)`) remains valid for an arbitrary prescheme
$Y$ and a morphism $f$ locally of finite type. Indeed, a) entails b) by virtue of `(14.4.1)`; conversely, b) entails
that `f''` is universally open at the points of `X''` above $x$ (resp. at every point of `X''`) by virtue of `(14.4.1)`,
and one concludes property a) by applying lemma `(14.4.8.1)` to the integral surjective morphism $Y'' \to Y$.

It may be that, in `(14.4.1)`, for the equivalence of a) and c), the supplementary hypothesis that $Y$ is Noetherian is
superfluous (cf. `(14.3.14)`). If so, the Noetherian hypotheses are also superfluous in `(14.4.2)`, `(14.4.3)`,
`(14.4.8)` and `(14.4.9)`.

*(ii)* One can give examples of morphisms $f : X \to Y$ having the following properties: $Y$ is Noetherian, regular and
of dimension `2`, $f$ is universally open and of finite type, $X$ has two irreducible components `X_1`, `X_2`, but the
restriction $X_{1} \to Y$ of $f$ to one of them is not an open morphism. The principle of the construction relies on the
general method of "gluing" that will be explained in chap. V, and can therefore only be sketched here. One starts from a
closed point $y$ of $Y$, and considers the $Y$-scheme `Y_1` obtained by blowing up $y$ `(II, 8.1.3)`; if $f_{1} : Y_{1}
\to Y$ is the structure morphism, one knows that the restriction of $f_{1}$ to $f^{-1}_{1}(Y - {y})$ is an isomorphism
onto $Y - {y}$ (*loc. cit.*), while the fibre $f^{-1}_{1}(y)$ is isomorphic to $\operatorname{Proj}(S)$, where $S =
\oplus^{\infty}_{k = 0} \mathfrak{m}^{k}_{y} / \mathfrak{m}^{k+1}_{y}$ `(II, 3.5.3)`, that is to say here to
$P^{1}_{k(y)}$; it follows from `(14.4.1)` that $f_{1}$ is not open at the generic point of $f^{-1}_{1}(y)$. On the
other hand, set $Y_{2} = P^{1}_{Y}$, and let $f_{2} : Y_{2} \to Y$ be the structure morphism; it follows from
`(II, 8.4.4)` that $f_{2}$ is flat, hence universally open `(2.4.6)`; moreover `(II, 3.5.3)`, $f^{-1}_{2}(y)$ is
isomorphic to $P^{1}_{k(y)}$; it then suffices to "glue" `Y_1` and `Y_2` along the isomorphic fibres $f^{-1}_{1}(y)$ and
$f^{-1}_{2}(y)$, which gives a morphism $f : X \to Y$ where the irreducible components `X_1`, `X_2` of $X$ are
canonically identified with `Y_1` and `Y_2` respectively, and the restrictions of $f$ to these components with $f_{1}$
and $f_{2}$.

Recall nevertheless `(12.1.1.5)` that if $Y$ is locally Noetherian, $f : X \to Y$ of finite type and flat, then every
irreducible component of $X$ is equidimensional over $Y$ (and consequently the restriction of $f$ to such a component is
universally open if all points of $Y$ are geometrically unibranch).

*(iii)* Recall `(12.1.2, (i))` that there are morphisms $f : X \to Y$ having the following properties: $Y$ is Noetherian
(not geometrically unibranch), $f$ is finite and flat (and even étale `(17.6.3)`), but the restriction of $f$ to an
irreducible component of $X$ is not an open morphism (although $f$ itself is by `(2.4.6)`).

*(iv)* Chevalley's criterion `(14.4.4)` explains the importance of the notion of universally open morphism. This notion
permits in effect, in numerous more or less classical results, to replace a hypothesis of normality by the hypothesis
that a certain morphism is universally open; the more general statement

<!-- original page 216 -->

obtained will apply in particular to flat morphisms `(2.4.6)`, whose importance in algebraic geometry is increasing. One
can consider that statements involving the hypothesis that a morphism is universally open are common generalizations of
statements involving a hypothesis of normality and of statements involving a hypothesis of flatness.

### 14.5. Universally open morphisms and quasi-sections

**Lemma (14.5.1).**

<!-- label: IV.14.5.1 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of
$X$, such that $f$ is equidimensional `(13.3.2)` at the point $x$; set $y = f(x)$, $e = \dim_{x}(f^{-1}(y))$. Let $X'$
be an irreducible closed part of $X$ containing $x$, $n$ an integer such that one has $codim(X', X) \leq n$ and
$\dim_{x}(X' \cap f^{-1}(y)) \geq e - n$. Then one necessarily has $codim(X', X) = n$,
$\dim_{x}(X' \cap f^{-1}(y)) = e - n$, and the restriction $X' \to Y$ of $f$ is a morphism equidimensional at $x$ (and
*a fortiori* dominant).*

The question being local on $X$, one may suppose that $f$ is of finite type and equidimensional, so that for every $z
\in Y$, all the irreducible components of $f^{-1}(z)$ are of dimension $e$ `(13.3.1, a''))`. Let $x'$ be the generic
point of $X'$, $y' = f(x')$, $Y' = \overline{y'} = \overline{f(X')}$, and set $Z = f^{-1}(Y')$. By virtue of
`(0, 14.2.2)`, one has

$$ (14.5.1.1) codim(X', Z) \leq n $$

and if the two members are equal, one has necessarily $codim(X', X) = n$ and $Z$ contains an irreducible component of
$X$, which entails `(13.3.1)` that $f(X')$ is dense in $Y$ and consequently $Z = X$; hence the equality $codim(X', Z) =
n$ is equivalent to the conjunction of the equality $codim(X', X) = n$ and the relation $Z = X$.

On the other hand, reasoning in the reduced preschemes of $Y$ and $X$ having $Y'$ and $Z$ respectively for underlying
spaces, one deduces from `(5.1.2)` and `(I, 3.6.5)` that one has

```text
  (14.5.1.2)        codim(X' ∩ f⁻¹(y'), f⁻¹(y')) = codim(X', Z).
```

By virtue of the hypothesis, $f^{-1}(y')$ is biequidimensional `(5.2.1)` and of dimension $e$, hence `(0, 14.3.5)`, one
has, by virtue of `(14.5.1.2)` and `(14.5.1.1)`,

```text
  (14.5.1.3)        e' = dim(X' ∩ f⁻¹(y')) = e − codim(X', Z) ≥ e − n
```

the equality holding if and only if $codim(X', X) = n$ and $f(X')$ is dense in $Y$.

Finally, by `(13.1.1)`, one has $\dim_{x}(X' \cap f^{-1}(y)) \geq e'$, whence, by `(14.5.1.3)`,

```text
  (14.5.1.4)        dim_x(X' ∩ f⁻¹(y)) ≥ e' ≥ e − n.
```

Now, by hypothesis, one also has $\dim_{x}(X' \cap f^{-1}(y)) \leq e - n$, whence the conclusions of the proposition.

**Corollary (14.5.2).**

<!-- label: IV.14.5.2 -->

*The hypotheses on $f$, $X$, $Y$, $x$ being those of `(14.5.1)`, suppose in addition that $x$ is not a maximal point of
$f^{-1}(y)$. Then there exists an affine open neighbourhood $U$ of $x$ in $X$, and a section $g \in \Gamma(U,
\mathcal{O}_{X})$ such that the set $X'$ of $x' \in U$ such that $g(x') = 0$ contains $x$ and contains no maximal point
of $f^{-1}(y)$. For every $g$ having these properties, $X'$ is equidimensional over $Y$ at the point $x$, and one has*

```text
  (14.5.2.1)         dim_x(X' ∩ f⁻¹(y)) = e − 1   and   codim(X', X) = 1.
```

<!-- original page 217 -->

One may restrict to the case where $X = U$ is an affine open neighbourhood of $x$ such that all the irreducible
components of $f^{-1}(y)$ contain $x$. These components correspond to the minimal prime ideals of $\mathcal{O}_{x}|y =
\mathcal{O}_{x}/\mathfrak{m}_{y} \mathcal{O}_{x}$, and by hypothesis these ideals are distinct from
$\mathfrak{m}_{x}/\mathfrak{m}_{y} \mathcal{O}_{x}$ (Bourbaki, *Alg. comm.*, chap. II, §1, n° 1, prop. 2); to obtain a
$g \in \Gamma(U, \mathcal{O}_{X})$ satisfying the conditions of the statement, it suffices to take $g \in
\mathfrak{m}_{x}$ such that the image of $g$ in $\mathfrak{m}_{x}$ does not belong to any of the preceding prime ideals.
Moreover, one has $codim(X', X) \leq 1$ `(5.1.8)`, and as $X'$ contains none of the irreducible components of
$f^{-1}(y)$ and these are of dimension $e$, one has `(0, 14.2.2.2)` $\dim_{x}(X' \cap f^{-1}(y)) \leq e - 1$. It then
suffices to apply `(14.5.1)`.

**Proposition (14.5.3).**

<!-- label: IV.14.5.3 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of
$X$. Suppose that $f$ is equidimensional at the point $x$ and that $x$ is closed in $f^{-1}(f(x))$. Then there exists an
irreducible part $X'$ of $X$, locally closed in $X$, containing $x$ and such that the restriction $X' \to Y$ of $f$
(where $X'$ is the reduced subprescheme of $X$ having $X'$ as underlying space) is a quasi-finite dominant morphism.*

Indeed, with the notation of `(14.5.2)`, the hypothesis that $x$ is closed in $f^{-1}(y)$ entails that $x$ is not a
maximal point of $X' \cap f^{-1}(y)$ as long as $e - 1 \geq 1$. It therefore suffices to apply `(14.5.2)` reasoning by
descending induction on $e = \dim_{x}(f^{-1}(f(x)))$ until one reaches $e = 1$; the application of `(14.5.2)` in this
last case gives an $X'$ such that $X' \cap f^{-1}(f(x))$ is Noetherian and of dimension `0`, hence finite and discrete;
as $X'$ is then equidimensional over $Y$, $X' \cap f^{-1}(f(x'))$ is of dimension `0` for every $x' \in X'$, which
entails that the restriction $X' \to Y$ of $f$ is a quasi-finite morphism `(II, 6.2.2)`.

**Corollary (14.5.4).**

<!-- label: IV.14.5.4 -->

*Under the hypotheses of `(14.5.3)`, suppose in addition that $Y = \operatorname{Spec}(A)$, where $A$ is a Noetherian
integral complete local ring, and that $y = f(x)$ is the unique closed point of $Y$. Then there exists an integral local
ring $A'$, containing $A$, which is a finite $A$-algebra and has the following property: if one sets $Y' =
\operatorname{Spec}(A')$ and $X' = X \times_{Y} Y'$, there exists a $Y'$-section $h : Y' \to X'$ such that the composite
morphism $Y' \to X' \to X$ is an immersion whose image contains $x$.*

Replacing if need be $X$ by an irreducible reduced subprescheme of $X$, one may, by virtue of `(14.5.3)`, restrict to
the case where the morphism $f$ is already quasi-finite and dominant. Using `(II, 6.2.5)`, one deduces that
$\mathcal{O}_{x} = A'$ is an integral ring that is a finite $A$-algebra, and that $X$ is the disjoint sum of the closed
subprescheme $Y' = \operatorname{Spec}(A')$ and a subprescheme `Y''`; the scheme $Y'$ answers the question, the
composite morphism $Y' \to X' \to X$ being none other than the canonical morphism $\operatorname{Spec}(\mathcal{O}_{x})
\to X$.

**Remark (14.5.5).**

<!-- label: IV.14.5.5 -->

If one does not require that in the statement of `(14.5.4)`, the morphism $Y' \to X$ be an immersion, one may suppose in
addition that $A'$ is integrally closed: it suffices indeed to replace $A'$ by its integral closure `A_1`, since one
knows `(0, 23.1.5)` that `A_1` is an $A$-module of finite type.

**Proposition (14.5.6).**

<!-- label: IV.14.5.6 -->

*Let $Y$ be a locally Noetherian, irreducible, regular prescheme of dimension `1`, $f : X \to Y$ a morphism locally of
finite type, $y$ a point of $Y$. The following conditions are equivalent:*

*a) $f_{red}$ is flat at every point of $f^{-1}(y)$.*

<!-- original page 218 -->

*b) $f$ is universally open in a neighbourhood of $f^{-1}(y)$.*

*c) $f$ is open in a neighbourhood of $f^{-1}(y)$.*

*d) Every irreducible component of $X$ meeting $f^{-1}(y)$ dominates $Y$.*

*e) For every point $x \in f^{-1}(y)$, closed in $f^{-1}(y)$, and every irreducible component $X_{i}$ of $X$ containing
$x$, there exists an irreducible part $X'$ of $X$, locally closed in $X$, containing $x$, contained in $X_{i}$, and such
that the restriction $X' \to Y$ of $f$ is a quasi-finite dominant morphism.*

The equivalence of a), b), c) and d) has already been proved `(14.3.8)`. It is clear that e) entails d), for every
irreducible component $X_{i}$ of $X$ meeting $f^{-1}(y)$ contains in $X_{i} \cap f^{-1}(y)$ a point closed in this space
`(5.1.11)`. Finally, to prove that c) entails e), one may restrict to the case where $f$ is a morphism of finite type;
consider a closed point $x$ of $f^{-1}(y)$ and let $X_{i}$ be an irreducible component of $X$ containing $x$. As the
restriction $f_{i} : X_{i} \to Y$ of $f$ to $X_{i}$ is a dominant morphism, it follows from the equivalence of c) and d)
for $f_{i}$ that this morphism is open at the generic points of $X_{i} \cap f^{-1}(y)$. It follows therefore from
`(14.2.2)` that $f_{i}$ is equidimensional at the point $x$, and one then concludes with the help of `(14.5.3)`.

**Remark (14.5.7).**

<!-- label: IV.14.5.7 -->

If, in the statement of `(14.5.5)`, one supposes that $Y = \operatorname{Spec}(A)$, where $A$ is a complete discrete
valuation ring, and that $y$ is the closed point of $Y$, one may in addition suppose that $X' =
\operatorname{Spec}(A')$, where $A'$ is a discrete valuation ring that is a finite $A$-algebra, as is shown by the proof
of `(14.5.4)` and the fact that an integral regular local ring of dimension `1` is a discrete valuation ring
`(II, 7.1.6)`.

**Proposition (14.5.8).**

<!-- label: IV.14.5.8 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $y$ a point of $Y$.*

*For every $Y$-prescheme $Y'$, set $X(Y') = \operatorname{Hom}_{Y}(Y', X)$. Let $x$ be a point of $f^{-1}(y)$; in order
that $f$ be universally open at the point $x$, it is necessary and sufficient that the following condition be
satisfied:*

*For every complete discrete valuation ring $A$, with algebraically closed residue field, every morphism $g : Y' =
\operatorname{Spec}(A) \to Y$ such that the image under $g$ of the closed point $y'$ of $Y'$ is equal to $y$, and every
element $u_{0} \in X(\operatorname{Spec}(k(y')))$ such that $u_{0}(y') = x$, there exists a discrete valuation ring $B$,
a local homomorphism $A \to B$ making $B$ a finite $A$-algebra, and, setting $Z' = \operatorname{Spec}(B)$, an element
$u \in X(Z')$ such that, if $z'$ is the closed point of $Z'$, the diagram*

```text
       Spec(k(z'))  ────→  Z' = Spec(B)
            │                    │
            │                    │ u
            ↓                    ↓
       Spec(k(y'))  ──u_0────→   X
```

*is commutative.*

Note that if $A$ and $B$ satisfy the conditions of the statement, $B$ is a complete discrete valuation ring (Bourbaki,
*Alg. comm.*, chap. III, §3, n° 3, prop. 7 and chap. IV, §2, n° 2, cor. 3 of prop. 9) with residue field isomorphic to
that of $A$, hence

<!-- original page 219 -->

algebraically closed, and since $u(z') = x$, there is in $X'' = X \times_{Y} Z'$ a point `x''` whose projections in $X$
and $Z'$ are $x$ and $z'$ and which is rational over $k(z')$; in addition, since there exists a $Z'$-section $v$ of
`X''` such that $v(z') = x''$, the image under $v$ of the generic point $s$ of $Z'$ is a generization $t$ of `x''` whose
projection in $Z'$ is $s$; applying `(14.3.6)`, one sees that the condition of the statement is sufficient. Let us now
prove that it is necessary. Set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. There is by hypothesis a point $x'
\in X'$ above $x$ and $y'$ and rational over $k(y')$ `(I, 3.3.14)`, hence closed in $f'^{-1}(y')$. By virtue of
`(14.3.6)`, there is an irreducible component $T'$ of $X'$ containing $x'$ and dominating $Y'$, hence (`(14.3.8)` and
`(14.3.13)`) the restriction $T' \to Y'$ of $f'$ is equidimensional at the point $x$. One deduces from `(14.5.5)` that
there is a finite $A$-algebra $B$ that is an integral integrally closed local ring and dominates $A$ (hence is a
discrete valuation ring); and, setting $Z' = \operatorname{Spec}(B)$ and $X'' = X \times_{Y} Z' = X' \times_{Y'} Z'$, a
$Z'$-section $v : Z' \to X''$ such that the image of the closed point $z'$ of $Z'$ by the composite morphism $Z' \to X''
\to X'$ is $x'$; the composite morphism $u : Z' \to X'' \to X$ then answers the question.

**Proposition (14.5.9).**

<!-- label: IV.14.5.9 -->

*Let $Y$ be a locally Noetherian irreducible prescheme, $f : X \to Y$ a morphism locally of finite type, $y$ a
geometrically unibranch point of $Y$. Then the following conditions are equivalent:*

*a) $f$ is universally open at every point of $f^{-1}(y)$.*

*b) $f$ is open at every point of $f^{-1}(y)$.*

*c) For every irreducible component $Z$ of $f^{-1}(y)$, of generic point $z$, there exists an irreducible component
$X_{i}$ of $X$ containing $z$ and equidimensional over $Y$ at the point $z$.*

*d) For every closed point $x$ of $f^{-1}(y)$, there exists an irreducible part $X'$ of $X$, locally closed in $X$,
containing $x$, and such that the restriction $X' \to Y$ of $f$ is a quasi-finite dominant morphism.*

The equivalence of a), b) and c) has already been proved `(14.4.2)`. To prove that a) entails d), note that by virtue of
`(14.4.2)`, a) entails that there exists an irreducible component $Z$ of $X$ containing $x$ and equidimensional over $Y$
at the point $x$; the existence of $X'$ then comes from `(14.5.3)` applied to the restriction $Z \to Y$ of $f$.
Conversely, suppose d) satisfied; by virtue of Chevalley's criterion `(14.4.4)`, the restriction $X' \to Y$ of $f$ is a
morphism universally open at the point $x$, and *a fortiori* $f$ is open at the point $x$; $f$ is therefore open at all
the closed points of $X_{y} = f^{-1}(y)$. But $X_{y}$ is a $k(y)$-prescheme locally of finite type, hence a Jacobson
prescheme; the set of closed points of $X_{y}$ is therefore dense in $X_{y}$ `(10.3.1)`, and it follows from `(14.1.4)`
that $f$ is open at all points of $X_{y}$, which completes the proof that d) entails b).

The following result has been brought out by D. Mumford:

**Proposition (14.5.10).**

<!-- label: IV.14.5.10 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a universally open, surjective and locally of finite type morphism.
Then there exists a finite surjective morphism $g : Y' \to Y$ such that, setting $X' = X \times_{Y} Y'$ and $f' =
f_{(Y')} : X' \to Y'$, every point $y' \in Y'$ admits an open neighbourhood $U'$ such that there exists a $U'$-section
of $f'^{-1}(U')$.*

We shall prove the proposition in several steps.

<!-- original page 220 -->

I) *Reduction to the case where $Y$ is integral.* — If one has proved the proposition for each of the reduced
subpreschemes $Y_{i}$ having for underlying space an irreducible component of $Y$, and for the inverse images
$f^{-1}(Y_{i})$, it is clear that the prescheme $Y'$ sum of the corresponding $Y'_{i}$ will answer the question. One may
therefore suppose $Y$ integral and we shall in what follows restrict to this case. Then, in the conclusion, one may also
take $Y'$ integral (replacing it if need be by a suitable irreducible component).

II) *Local character on $Y$.* — We shall show that if one can cover $Y$ by finitely many open sets $U_{j}$ such that,
for every $j$, the conclusion of the proposition is true for the morphism $f^{-1}(U_{j}) \to U_{j}$, restriction of $f$,
then the conclusion is true also for $f$. Indeed, one may evidently suppose the $U_{j}$ affine, so that $U_{j} =
\operatorname{Spec}(A_{j})$, where $A_{j}$ is a Noetherian integral ring whose field of fractions $K = R(Y)$ is the
field of rational functions on $Y$. For every $j$, there is by hypothesis a finite integral $A_{j}$-algebra $A'_{j}$
such that the homomorphism $A_{j} \to A'_{j}$ is injective `(I, 1.2.7)` and the corresponding morphism $g_{j} : U'_{j} =
\operatorname{Spec}(A'_{j}) \to \operatorname{Spec}(A_{j}) = U_{j}$ satisfies the conditions of the proposition (for
$U_{j}$ and $f^{-1}(U_{j})$). Let then $K'$ be a finite extension of $K$ containing the fields of fractions of all the
$A'_{j}$ (which are finite extensions of $K$). Consider the normalization `Y''` of $Y$ in $K'$ `(II, 6.3.8)`, which is
of the form $\operatorname{Spec}(\mathcal{B})$, where $\mathcal{B}$ is an integral quasi-coherent
$\mathcal{O}_{Y}$-Algebra, integral closure of $\mathcal{O}_{Y}$ in $K'$ `(II, 6.3.4)`. These definitions prove that for
every $j$, $A''_{j} = \Gamma(U_{j}, \mathcal{B}) = \Gamma(U'_{j}, (g_{j})_{*}(\mathcal{O}_{U'_{j}}))$ is identified with
a finite sub-$A_{j}$-algebra of $\Gamma(U_{j}, \mathcal{B})$; in other words, $(g_{j})_{*}(\mathcal{O}_{U'_{j}}) =
\mathcal{B}_{j}$ is a coherent $\mathcal{O}_{U_{j}}$-Algebra, sub-Algebra of $\mathcal{B}|U_{j}$. There exists therefore
a coherent sub-$\mathcal{O}_{Y}$-Module $\mathcal{C}$ of $\mathcal{B}$ such that $\mathcal{C}|U_{j} = \mathcal{B}_{j}$
`(I, 9.4.7)`. If one sets $\mathcal{C}' = \mathcal{C}$, the sub-$\mathcal{O}_{Y}$-Algebra $\mathcal{B}'$ of
$\mathcal{B}$ generated by $\mathcal{C}$ is coherent since $\mathcal{B}$ is an integral $\mathcal{O}_{Y}$-Algebra. Let
us show then that $Y' = \operatorname{Spec}(\mathcal{B}')$ answers the question. Indeed, it is clear that the morphism
$g : Y' \to Y$ is finite surjective and that $Y'$ is integral; in addition, for every $j$, $\Gamma(U_{j}, \mathcal{B}')$
is a finite $A_{j}$-algebra, in other words the morphism $g^{-1}(U_{j}) \to U_{j}$, restriction of $g$, factors as
$g^{-1}(U_{j}) \to U'_{j} \to U_{j}$, and as local existence of sections is stable under base change, this establishes
our assertion, every $y \in Y$ belonging to some $U_{j}$.

III) *Reduction to the case where $Y$ is integral, local and geometrically unibranch.* — Suppose first that the
proposition has been proved when $Y$ is integral and local (with $Y'$ integral), and let us show that it is valid when
$Y$ is any (Noetherian) integral affine. Indeed, by virtue of the reduction II), it suffices to prove that for every
point $y \in Y$, the proposition is true for an affine open neighbourhood $V$ of $y$ in $Y$. Let $Y =
\operatorname{Spec}(A)$, $Y_{1} = \operatorname{Spec}(A_{\mathfrak{p}})$, where $\mathfrak{p} = \mathfrak{j}_{y}$, and
set $X_{1} = X \times_{Y} Y_{1}$; by hypothesis, there exists a finite surjective morphism $g_{1} : Y'_{1} \to Y_{1}$,
where $Y'_{1} = \operatorname{Spec}(B_{1})$, `B_1` being an integral finite $A_{\mathfrak{p}}$-algebra, hence a
semi-local ring, such that $g_{1}$ satisfies the conditions of the statement for `Y_1` and `X_1`. If $y'_{j}$ ($1 \leq j
\leq r$) are the closed points of $Y'_{1}$, there is therefore a covering of $Y'_{1}$ by open sets $U'_{j}$ such that
$y'_{j} \in U'_{j}$ and that there exists a $U'_{j}$-section $h_{j}$ of $X \times_{Y} U'_{j}$ ($1 \leq j \leq r$). The
$A_{\mathfrak{p}}$-module `B_1` admits a finite system of generators of the form $z_{j}/s$ (with $s \in A -
\mathfrak{p}$,

<!-- original page 221 -->

$z_{j}$ integral over $A$), which one may suppose (multiplying if need be $s$ by an element of $A$) to be elements of
the field of fractions of `B_1`, integral over $A_{s}$, so that if $V$ is the affine open set $D(s) =
\operatorname{Spec}(A_{s}) \subset Y$, $Y'_{1}$ is identified with $Y' \times_{Y} V$, where $Y'$ is the spectrum of the
finite $A_{s}$-algebra generated by the $z_{j}/s$; $g : Y' \to V$ is therefore a finite surjective morphism and $g_{1} =
g_{(Y_{1})}$. Moreover, applying the method of `(8.1.2, a))`, one may suppose that each of the $U'_{j}$ is the inverse
image under $p : Y'_{1} \to Y'$ of an open set $W'_{j}$ of $Y'$, such that the $W'_{j}$ cover $Y'$ `(8.3.11)`, and that
each of the sections $h_{j}$ is of the form $(v'_{j})_{(Y_{1})}$ where $v'_{j}$ is a $W'_{j}$-section of $X \times_{Y}
W'_{j}$ `(8.8.2, (i))`. One is therefore indeed reduced to proving the proposition when $Y = \operatorname{Spec}(A)$,
$A$ being a Noetherian integral local ring. One then knows that there exists a finite integral $A$-algebra $B$, having
the same field of fractions as $A$, such that $A \subset B$ and $\operatorname{Spec}(B)$ is geometrically unibranch
(`(0, 23.2.5)` and `(6.15.5)`); as the morphism $\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is surjective, one
may evidently replace $Y$ by $\operatorname{Spec}(B)$ and $X$ by $X \otimes_{A} B$ to prove the proposition. Reasoning
as at the beginning of reduction III), one may therefore suppose $A$ local, integral and $Y = \operatorname{Spec}(A)$
geometrically unibranch.

IV) *Reduction to the case where $X$ is integral, affine, and $f$ quasi-finite, surjective, birational and universally
open.* — Suppose therefore $Y = \operatorname{Spec}(A)$ integral, local and geometrically unibranch. There then exists
an irreducible subprescheme `X_0` of $X$ such that the restriction $f_{0} : X_{0} \to Y$ of $f$ is a quasi-finite
dominant morphism and $f_{0}(X_{0})$ contains the closed point $y$ of $Y$ `(14.5.9)`; since $Y$ is geometrically
unibranch, it follows from `(14.4.1)` that $f_{0}$ is still universally open. As moreover one may suppose `X_0` reduced,
hence integral, one sees that one may, replacing $X$ by `X_0`, suppose that $X$ is integral and $f$ quasi-finite and
dominant, and such that $f(X)$ contains $y$; as $f$ is open and every open of $Y$ containing $y$ is equal to $Y$, $f$ is
surjective.

Let $\xi$, $\eta$ be the generic points of $X$ and $Y$ respectively; $k(\xi)$ is then a finite extension of $K =
k(\eta)$. Consequently `(4.6.8)`, there is a finite extension $K'$ of $K$ such that $(\operatorname{Spec}(k(\xi)
\otimes_{K} K'))_{red}$ is geometrically reduced over $K'$ and its irreducible components are geometrically irreducible;
it follows (`(4.5.9)` and `(4.6.1)`) that the residue fields of $\operatorname{Spec}(k(\xi) \otimes_{K} K')$ are finite,
primary and separable extensions of $K'$, hence are equal to $K'$. Applying again `(0, 23.2.5)` and `(6.15.5)`, there
exists a finite integral $A$-algebra $B$, having $K'$ for field of fractions, containing $A$ and such that
$\operatorname{Spec}(B)$ is geometrically unibranch; one may therefore again replace $Y$ by $\operatorname{Spec}(B)$ and
$X$ by $(X \otimes_{A} B)_{red}$ to prove the proposition; the reduction III) then allows one to suppose still $A$
local, integral and $Y = \operatorname{Spec}(A)$ geometrically unibranch, with closed point $y$. Moreover, $f$ is then a
*quasi-finite, surjective and universally open* morphism; each of the irreducible components $X_{i}$ of $X$ ($1 \leq i
\leq m$) dominates $Y$ `(1.10.4)` and is birational over $Y$. Let then $x$ be a point of $f^{-1}(y)$ and let $X_{i}$ be
an irreducible component of $X$ containing $x$; let us still denote by $X_{i}$ the reduced (hence integral) subprescheme
of $X$ having $X_{i}$ as underlying space, and let $f_{i} : X_{i} \to Y$ be the restriction of $f$. Applying again
`(14.4.1)` to the quasi-finite dominant morphism $f_{i}$, one sees that $f_{i}$ is universally open; if $U$ is an affine
open of $X_{i}$ containing $x$, $f_{i}(U)$ is therefore

<!-- original page 222 -->

open in $Y$ and contains $y$, hence is equal to $Y$. One may thus replace $X$ by $U$ to prove the proposition.

V) *End of the proof.* — We therefore suppose $Y$ local, integral and geometrically unibranch, $X$ integral and affine,
$f$ quasi-finite, surjective, birational and universally open; it follows that $f$ is automatically separated. By virtue
of the Main theorem `(8.12.6)`, there exists a factorization $X \to Z \to Y$, where $j$ is an open immersion and $u$ a
finite morphism. Replacing moreover $Z$ by the closed image of $j$ `(I, 9.5.10)`, one may suppose that $Z$ is integral;
as $u$ is finite and birational and $Y$ geometrically unibranch, it follows from `(III, 4.3.5 and 4.3.4)` that $u$ (and
consequently $f$) is a *radicial* morphism; as $f$ is universally open and surjective, it is therefore a universal
homeomorphism. Consequently `(2.4.5, (ii))` $f$ is a finite morphism. But then one answers the conditions of the
statement with $Y'$ integral by simply taking $Y' = X$ and $g = f$, the $Y'$-section being the diagonal morphism
$\Delta_{f}$. Q.E.D.

This result can be used to develop "descent" criteria for various properties by universally open and surjective
morphisms. We point out in particular the following criterion, due to D. Mumford:

**Corollary (14.5.11).**

<!-- label: IV.14.5.11 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $g : Y' \to Y$ a morphism
locally of finite type, universally open and surjective; set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. Then,
for $f$ to be affine, it is necessary and sufficient that $f'$ be so.*

One must only prove that the condition is sufficient. The question being local on $Y$, one may suppose $Y$ affine, hence
Noetherian. By virtue of `(14.5.10)`, there exists a finite surjective morphism $h : Y_{1} \to Y$ such that, setting
$Y'_{1} = Y' \times_{Y} Y_{1}$, and $g' = g_{(Y_{1})} : Y'_{1} \to Y_{1}$, every point of `Y_1` admits an open
neighbourhood `U_1` such that there exists a `U_1`-section of $g'^{-1}(U_{1})$. If one sets $X_{1} = X \times_{Y}
Y_{1}$, the canonical projection $p : X_{1} \to X$ is a finite surjective morphism, hence, if one proves that `X_1` is
an affine scheme, it will result first that $X$ is quasi-compact, hence Noetherian, then that $X$ is affine by virtue of
Chevalley's theorem `(II, 6.7.1)`. It therefore suffices to prove that the morphism $f_{1} = f_{(Y_{1})} : X_{1} \to
Y_{1}$ is affine. Now, if one sets

```text
   X'_1 = X_1 ×_{Y_1} Y'_1 = X' ×_Y Y'_1   and   f'_1 = (f_1)_{(Y'_1)},
```

$f'_{1}$ is affine by virtue of the hypothesis. One is therefore reduced to proving the corollary when one replaces $Y$,
$X$, $f$ and $Y'$ by `Y_1`, `X_1`, $f_{1}$ and $Y'_{1}$, in other words, it suffices to prove that $f$ is affine when
one makes in addition, in the statement of `(14.5.11)`, the hypothesis that every point of $Y$ admits an open
neighbourhood $U$ such that there exists a $U$-section of $g^{-1}(U)$. The question being local on $Y$, one may even
suppose that there exists a $Y$-section $s$ of $Y'$. Now, one has the following elementary lemma (valid in every
category admitting fibre products):

**Lemma (14.5.11.1).**

<!-- label: IV.14.5.11.1 -->

*Let $f : X \to S$, $g : Y \to S$ be two morphisms, $p_{1} : X \times_{S} Y \to X$, $p_{2} : X \times_{S} Y \to Y$ the
canonical projections. If $s : S \to Y$ is a section of $g$, then $s' = (1, s \circ f)_{S}$ is a section of $p_{1}$ and
$X$, equipped with the morphisms $f : X \to S$ and $s' : X \to X \times_{S} Y$, is identified with the product of the
$Y$-preschemes $S$ and $X \times_{S} Y$ for the morphisms $s : S \to Y$ and $p_{2} : X \times_{S} Y \to Y$.*

<!-- original page 223 -->

This is a particular case of `(I, 3.3.11)`, where one replaces the diagram by

```text
       X  ─s'─→  X ×_S Y  ─p_1─→  X
       │            │              │
     f │          p_2│            f│
       ↓            ↓              ↓
       S  ──s──→    Y    ──g───→   S
```

Applying this lemma replacing $S$, $Y$ by $Y$, $Y'$, one sees that one may write $f = (f')_{(Y)}$ for the base change
$s : Y \to Y'$, hence $f$ is affine since $f'$ is. Q.E.D.

A variant of this criterion is the following:

**Corollary (14.5.12).**

<!-- label: IV.14.5.12 -->

*With the notation and general hypotheses of `(14.5.11)`, let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module.
Suppose that there exists a closed part $Z$ of $X$ proper over $Y$ `(II, 5.4.10)` and such that the prescheme induced by
$X$ on the open set $X - Z$ is normal. Then, for $\mathcal{L}$ to be ample relatively to $f$, it is necessary and
sufficient that $\mathcal{L}' = \mathcal{L} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$ be ample relatively to $f'$.*

Let us keep the notation of the proof of `(14.5.11)`. Set $\mathcal{L}_{1} = \mathcal{L} \otimes_{\mathcal{O}_{X}}
\mathcal{O}_{X_{1}}$; it will suffice to prove that $\mathcal{L}_{1}$ is ample relatively to $f \circ p$, by virtue of
`(III, 2.6.2)`; but $f \circ p = h \circ f_{1}$, and, taking `(II, 4.6.13, (v))` into account, it will suffice to prove
that $\mathcal{L}_{1}$ is ample relatively to $f_{1}$. The question being local on `Y_1`, one may again suppose that
$g'$ admits a section $s$; if $\mathcal{L}'_{1} = \mathcal{L}' \otimes_{\mathcal{O}_{X'}} \mathcal{O}_{X'_{1}}$, one may
then write, by virtue of lemma `(14.5.11.1)`, $\mathcal{L}_{1} = \mathcal{L}'_{1} \otimes_{\mathcal{O}_{X'_{1}}}
\mathcal{O}_{X_{1}}$ for the base change $s : Y_{1} \to Y'_{1}$; the conclusion therefore results from two applications
of `(II, 4.6.13, (iii))`.
