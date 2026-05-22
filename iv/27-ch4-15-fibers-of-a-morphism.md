<!-- original page 223 -->

## §15. Study of the fibres of a universally open morphism

### 15.1. Multiplicities of the fibres of a universally open morphism

**Proposition (15.1.1).**

<!-- label: IV.15.1.1 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, of generic point $\eta$, $f : X \to Y$ a morphism locally of
finite type, $y$ a point of $Y$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module; one sets $\mathcal{F}_{y} =
\mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$ (sheaf of modules on the fibre $f^{-1}(y)$). Let $z$ be the generic point of
an irreducible component of $Supp(\mathcal{F}_{y})$, and let $X_{i}$ ($1 \leq i \leq m$) be those of the reduced closed
subpreschemes of $X$ whose underlying space is an irreducible component of $Supp(\mathcal{F})$ containing $z$, and such
that the restriction $X_{i} \to Y$ of $f$ is a morphism universally open at the point $z$; let $z_{i}$ be the generic
point of $X_{i}$ ($1 \leq i \leq m$). If $\lambda_{x}(\mathcal{F}_{y})$ (resp. $\lambda_{t}(\mathcal{F}_{\eta})$)
denotes the geometric length of $\mathcal{F}_{y}$ at a point $x \in f^{-1}(y)$ (resp. that of $\mathcal{F}_{\eta}$ at a
point $t \in f^{-1}(\eta)$) `(4.7.5)`, then one has*

$$ (15.1.1.1) \lambda_{z}(\mathcal{F}_{y}) \geq \sum^{m}_{i=1} \lambda_{z_{i}}(\mathcal{F}_{\eta}). $$

*If moreover one supposes the ring $\mathcal{O}_{y}$ regular, then one has*

$$ (15.1.1.2) long((\mathcal{F}_{y})_{z}) \geq \sum^{m}_{i=1} long((\mathcal{F}_{\eta})_{z_{i}}). $$

The fibres $f^{-1}(y')$ of $f$ (for every $y' \in Y$) do not change when one replaces $f$ by $f_{red}$; one may
therefore suppose that $X$ and $Y$ are reduced `(2.4.3, (vi))`, hence $Y$ integral; one will set $K = k(\eta)$. One may
in addition replace $f$ by the restriction $Supp(\mathcal{F}) \to Y$ of $f$ to the reduced closed subprescheme of $X$
having $Supp(\mathcal{F})$ as underlying space, hence restrict to the case where $X = Supp(\mathcal{F})$. Finally, if $y
= \eta$, there is only one irreducible component $X_{i}$ of $X$ containing $z$ $(0_{I}, 2.1.8)$ and one has $z_{i} = z$,
which makes `(15.1.1.1)` and `(15.1.1.2)` trivial (without hypotheses on $f$). One may therefore restrict to the case $y
\neq \eta$; it then follows from the hypothesis and from `(1.10.3)` that the $z_{i}$ belong to $f^{-1}(\eta)$, the
right-hand sides of `(15.1.1.1)` and `(15.1.1.2)` being therefore defined. Let $Z_{i}$ be the reduced closed
subprescheme of $f^{-1}(\eta)$ having $X_{i} \cap f^{-1}(\eta)$ as underlying space; one knows `(4.6.6)` that there
exists a finite radicial extension $K'$ of $K$ such that, for every $i$, the $K'$-prescheme $(Z_{i} \otimes_{K}
K')_{red}$ is geometrically reduced over $K'$. Moreover, the projection morphism $f^{-1}(\eta) \otimes_{K} K' \to
f^{-1}(\eta)$ is finite, dominant and radicial `(I, 3.5.7)`, hence is a homeomorphism `(2.4.5)`. If $\zeta_{i}$ is the
unique point of $f^{-1}(\eta) \otimes_{K} K'$ above $z_{i}$, it follows from `(4.7.9)` and `(4.7.5)` that one has

```text
  (15.1.1.3)             λ_{z_i}(ℱ_η) = λ_{ζ_i}(ℱ_η ⊗_K K').
```

Let $V$ be a discrete valuation ring, of fraction field $K'$, dominating $\mathcal{O}_{y}$ `(II, 7.1.7)`; set $Y' =
\operatorname{Spec}(V)$, $X' = X \times_{Y} Y'$, $\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$, $f' = f_{(Y')} : X' \to
Y'$; if $g : Y' \to Y$ is the structure morphism, $\eta'$ the generic point of $Y'$ and $y'$ its closed point, one has
$g(y') = y$, $g(\eta') = \eta$; the morphism $\operatorname{Spec}(k(y')) \to \operatorname{Spec}(k(y))$ being faithfully
flat, the same is true of the projection $g' : f'^{-1}(y') \to f^{-1}(y)$ `(2.2.13)`, hence `(2.3.4)` there is a generic
point $z'$ of an irreducible component of $f'^{-1}(y')$ such that $g'(z') = z$. By construction, one has $k(\eta') =
K'$, hence $f'^{-1}(\eta') = f^{-1}(\eta) \otimes_{K} K'$; on the other hand, if one sets $X'_{i} = X_{i} \times_{Y}
Y'$, the restriction $X'_{i} \to Y'$ of $f'$ is a morphism universally open at the point $z'$, hence `(1.10.3)` there
exists a point $\zeta'_{i} \in f'^{-1}(\eta')$ which is a generization of $z'$, and one may evidently suppose that
$\zeta'_{i}$ is a generic point of an irreducible component of $X'_{i} \cap f'^{-1}(\eta')$; as the projection of
$X'_{i} \cap f'^{-1}(\eta')$ into $f^{-1}(\eta)$ is $Z_{i}$, one has $\zeta'_{i} = \zeta_{i}$. By virtue of `(4.7.9)`
and `(4.7.5)`, one has

$$ (15.1.1.4) \lambda_{z'}(\mathcal{F}'_{y'}) = \lambda_{z}(\mathcal{F}_{y}), $$

and it therefore follows from this inequality and from `(15.1.1.3)` that, in order to establish `(15.1.1.1)`, it
suffices to demonstrate the inequality

<!-- original page 224 -->

$$ (15.1.1.5) \lambda_{z'}(\mathcal{F}'_{y'}) \geq \sum^{m}_{i=1} \lambda_{\zeta_{i}}(\mathcal{F}'_{\eta'}). $$

Consider now the second inequality `(15.1.1.2)`; we shall use the following lemma:

**Lemma (15.1.1.6).**

<!-- label: IV.15.1.1.6 -->

*Let $A$ be a regular local ring that is not a field, $K$ its fraction field, $k$ its residue field. There exists a
discrete valuation ring $V$ dominating $A$, having $K$ as fraction field and whose residue field is a pure
transcendental extension of $k$.*

Set $S = \operatorname{Spec}(A)$, and consider the $S$-scheme $P$ obtained by blowing up the closed point $s$ of $S$
`(II, 8.1.3)`; if $\mathfrak{m}$ is the maximal ideal of $A$, one has by definition $P = \operatorname{Proj}(B)$, where
$B$ is the graded $A$-algebra $\oplus_{n \geq 0} \mathfrak{m}^{n}$. If $h : P \to S$ is the structure morphism, the
fibre $h^{-1}(s)$ is isomorphic to $\operatorname{Proj}(B \otimes_{A} k)$ `(II, 2.8.10)`, and by definition $B
\otimes_{A} k$ is the graded $A$-algebra $\oplus_{n \geq 0} \mathfrak{m}^{n} / \mathfrak{m}^{n+1}$; but since $A$ is
regular, this algebra is isomorphic to a polynomial algebra $k[t_{1}, \cdots, t_{e}]$ ($t_{i}$ indeterminates)
`(0, 17.1.1)`, and consequently $h^{-1}(s)$ is isomorphic to $P^{e-1}_{k}$. Let $\zeta$ be the generic point of
$h^{-1}(s)$; if $t_{i}$ ($1 \leq i \leq e$) are the elements of $\mathfrak{m}$ whose classes mod $\mathfrak{m}^{2}$ are
the $t_{i}$, $B_{(t_{e})}$ is the ring of an affine open neighbourhood of $\zeta$ in $P$, and one has $k(\zeta) =
k(t_{1}, \cdots, t_{e-1})$; on the other hand, as $A$ is integrally closed, one verifies easily that the same holds for
$B$ (Bourbaki, _Alg. comm._, chap. V, §1, n° 8, cor. 1 of prop. 21), hence $B_{(t_{e})}$ is also integrally closed, and
consequently so is the local ring $\mathcal{O}_{P,\zeta}$. Finally, since $A = \mathcal{O}_{s}$ is regular, hence a
universally catenary ring `(5.6.4)`, one has, by virtue of `(5.6.5)`, $\dim(\mathcal{O}_{P,\zeta}) =
\dim(\mathcal{O}_{s}) - (e - 1)$, since $h$ is a birational morphism, $\dim(h^{-1}(s)) = e - 1$, and the local ring of
the fibre $h^{-1}(s)$ at its generic point $\zeta$ is of dimension `0`. But $\dim(\mathcal{O}_{s}) = e$, hence
$\dim(\mathcal{O}_{P,\zeta}) = 1$, and $\mathcal{O}_{P,\zeta} = V$ is a discrete valuation ring, being Noetherian, of
dimension `1` and integrally closed `(II, 7.1.6)`; it evidently answers the question.

This lemma being established, one may resume the reasoning made for the inequality `(15.1.1.1)` with $Y' =
\operatorname{Spec}(V)$; this time $k(y')$ is a separable extension of $k(y)$, and consequently `(4.7.9)`, one has
$long((\mathcal{F}_{y})_{z}) = long((\mathcal{F}'_{y'})_{z'})$; as moreover $f'^{-1}(\eta') = f^{-1}(\eta)$ and
$\mathcal{F}'_{\eta'} = \mathcal{F}_{\eta}$, one is again reduced to proving the inequality `(15.1.1.5)`. Now, if $t$ is
a uniformizer of $\mathcal{O}_{y'}$, $f'^{-1}(y')$ is the closed subprescheme of $X'$ defined by the Ideal $t
\mathcal{O}_{X'}$, and one has $\mathcal{O}_{y'} = \mathcal{O}'/t \mathcal{O}'$; on the other hand, one verifies at once
`(I, 9.1.12)` that $(\mathcal{F}'_{\eta'})_{z'} = \mathcal{F}'_{z'}$; the inequality to be demonstrated `(15.1.1.5)` is
then nothing but a particular case of `(3.4.1.1)`.

**Corollary (15.1.2).**

<!-- label: IV.15.1.2 -->

*The hypotheses being those of `(15.1.1)`, suppose moreover that $\lambda_{z}(\mathcal{F}_{y}) = 1$ (resp. that
$\mathcal{O}_{y}$ is regular and $long((\mathcal{F}_{y})_{z}) = 1$). Then there exists at most one irreducible component
$X_{i}$ of $Supp(\mathcal{F})$ containing $z$ and such that the restriction $X_{i} \to Y$ of $f$ is universally open at
the point $z$. Moreover, if $z_{i}$ is the generic point of this component, one has $\lambda_{z_{i}}(\mathcal{F}_{\eta})
= 1$ (resp. $long((\mathcal{F}_{\eta})_{z_{i}}) = 1$).*

This results at once from `(15.1.1)` on noting that one necessarily has, by definition of $X_{i}$,
$(\mathcal{F}_{\eta})_{z_{i}} \neq 0$ `(I, 9.1.13)`.

**Corollary (15.1.3).**

<!-- label: IV.15.1.3 -->

*Let $Y$ be an irreducible locally Noetherian prescheme with generic point $\eta$, $f : X \to Y$ a morphism locally of
finite type, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module of support $X$, $x$ a point of $X$, $y = f(x)$. Suppose
that: 1° $x$ belongs to only one irreducible component $Z$ of $f^{-1}(y)$; 2° $\mathcal{F}_{y} = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} k(y)$ is geometrically reduced over $k(y)$, in other words, if $z$ is the generic point of
$Z$, $\lambda_{z}(\mathcal{F}_{y}) = 1$ (resp. $\mathcal{O}_{y}$ is regular and $long((\mathcal{F}_{y})_{z}) = 1$).
Then, there exists at most one irreducible component $X'$ of $X$ containing $x$, such that $\dim_{x}(X' \cap f^{-1}(y))
= \dim_{x}(f^{-1}(y))$ and that the restriction $X' \to Y$ of $f$ is universally open at the generic points of the
irreducible components of $X' \cap f^{-1}(y)$ containing $x$. Moreover, if there exists such a component $X'$ and if
$z'$ is its generic point, one has $\lambda_{z'}(\mathcal{F}_{\eta}) = 1$ (resp. $long((\mathcal{F}_{\eta})_{z'}) =
1$).*

<!-- original page 225 -->

Indeed, an irreducible component $X'$ of $X$ containing $x$ and such that $\dim_{x}(X' \cap f^{-1}(y)) =
\dim_{x}(f^{-1}(y))$ necessarily contains $Z$, since an irreducible component of $X' \cap f^{-1}(y)$ containing $x$ must
be of the same dimension as the unique irreducible component $Z$ of $f^{-1}(y)$ containing $x$. One may then apply
`(15.1.2)` to $z$.

**Remarks (15.1.4).**

<!-- label: IV.15.1.4 -->

*(i)* In the statement of `(15.1.1)`, one cannot replace "universally open" by "equidimensional", as is shown by the
example `(14.4.10, (ii))` where one takes $\mathcal{F} = \mathcal{O}_{X}$; the fibres of $f$ are then reduced Artinian
schemes, hence (with the notation introduced *loc. cit.*) one has $\lambda_{\zeta}(\mathcal{F}_{\eta}) = 1$, but there
are two irreducible components `X_1`, `X_2` of $X$ containing $x'$, and the right-hand side of `(15.1.1.1)` is therefore
equal to `2`, although the restriction of $f$ to each of the components `X_1`, `X_2` is a morphism equidimensional at
every point. The same example shows also that in `(15.1.2)` and `(15.1.3)`, one cannot replace the hypothesis
"universally open" by "equidimensional".

*(ii)* It is plausible that for the validity of the inequality `(15.1.1.2)`, one cannot suppress the hypothesis that
$\mathcal{O}_{y}$ is regular.

### 15.2. Flatness of universally open morphisms with geometrically reduced fibres

**(15.2.1)**

<!-- label: IV.15.2.1 -->

One has seen `(2.4.6)` that a flat morphism locally of finite presentation is universally open. One has a partial
converse of this result by means of additional hypotheses:

**Theorem (15.2.2).**

<!-- label: IV.15.2.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module, $x$ a point of $X$, $y = f(x)$. Suppose the following conditions verified:*

*(i) $Supp(\mathcal{F}) = X$.*

*(ii) $f$ is universally open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$.*

*(iii) $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$ is geometrically reduced at the point $x$
`(4.6.22)`.*

*(iv) The ring $\mathcal{O}_{y}$ is reduced.*

*Then $\mathcal{F}$ is $f$-flat at the point $x$.*

Since $\mathcal{O}_{y}$ is reduced and Noetherian, we shall apply the valuative criterion of flatness `(11.8.1)`.
Consider then a local homomorphism $\mathcal{O}_{y} \to A'$, where $A'$ is a discrete valuation ring; set $Y' =
\operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, and let $x'$ be a point of $X'$ whose
projections in $X$ and $Y'$ are respectively $x$ and the closed point $y'$ of $Y'$; if one sets $\mathcal{F}' =
\mathcal{F} \otimes_{Y} Y'$, one has $Supp(\mathcal{F}') = X'$ by `(I, 9.1.13)`; every generic point $z'$ of an
irreducible component of $f'^{-1}(y')$ containing $x'$ has as projection in $f^{-1}(y)$ a generic point $z$ of an
irreducible component of $f^{-1}(y)$ containing $x$, by virtue of `(4.2.6)`; hence $f'$ is universally open at the point
$z'$. Finally, it follows from `(4.7.11)` that $\mathcal{F}'_{y'}$ is geometrically reduced at the point $x'$. One sees
therefore that one is reduced to demonstrating the

**Lemma (15.2.2.1).**

<!-- label: IV.15.2.2.1 -->

*Let $Y = \operatorname{Spec}(A)$ be the spectrum of a discrete valuation ring, $y$ its closed point, $f : X \to Y$ a
morphism locally of finite type, $x$ a point of $f^{-1}(y)$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Suppose
the following conditions verified:*

*(i) $Supp(\mathcal{F}) = X$.*

*(ii) $f$ is open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$.*

*(iii) $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$ is reduced at the point $x$ `(3.2.2)`.*

*Then $\mathcal{F}$ is $f$-flat at the point $x$.*

Designate then by $t$ a uniformizer of $A$, set $B = \mathcal{O}_{x}$ and $\mathcal{F}_{x} = M$; condition (i) implies
that $Supp(M) = \operatorname{Spec}(B)$ `(I, 9.1.13)`. Condition (ii) implies, by virtue of `(14.3.2)`, that every
irreducible component of $X$ containing $x$ dominates $Y$; in other words, the inverse image in $A$ of every minimal
prime ideal $\mathfrak{p}_{i}$ of $B$ is `0`, which means again that one has $t \notin \mathfrak{p}_{i}$ for every $i$.
Finally, (iii) means that $M/tM$ is a reduced $(B/tB)$-module `(3.2.2)`. It is a question of showing that under these
conditions $M$ is a torsion-free $A$-module $(0_{I}, 6.3.4)$, and for this it suffices evidently to show that $t$ is an
$M$-regular element; but this results from `(3.4.6.1)`.

**Corollary (15.2.3).**

<!-- label: IV.15.2.3 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $y =
f(x)$. Suppose the following conditions verified:*

*(i) $f$ is universally open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$.*

*(ii) $f^{-1}(y)$ is geometrically reduced (over $k(y)$) at the point $x$ `(4.6.9)`.*

*(iii) The ring $\mathcal{O}_{y}$ is reduced.*

*Under these conditions $f$ is flat at the point $x$.*

It suffices to apply `(15.2.2)` to $\mathcal{F} = \mathcal{O}_{X}$ `(4.6.22)`.

<!-- original page 226 -->

**Remarks (15.2.4).**

<!-- label: IV.15.2.4 -->

*(i)* The first three of the conditions of `(15.2.2)` do not change when one replaces $f$ by $f_{red}$; but if
$\mathfrak{N}$ is the nilradical of a Noetherian local ring $A$, $A/\mathfrak{N}$ is flat over $A/\mathfrak{N}$ but not
over $A$ itself when $\mathfrak{N} \neq 0$ (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. 2 of prop. 5). One sees
therefore that one cannot in `(15.2.2)` suppress condition (iv).

*(ii)* It follows from `(2.4.6)` that if the conclusion of `(15.2.2)` is true, as well as hypothesis (i), $f$ is
universally open in a neighbourhood of $x$, and in particular at the generic points of the irreducible components of
$f^{-1}(y)$ containing $x$. Even when (i), (iii) and (iv) are verified, one cannot replace (ii) by the weaker hypothesis
that $f$ is universally open at the point $x$ only. This is what is shown by the example `(14.1.3, (i))`, where $f$ is
evidently universally open at every point of `X_2`, hence in particular at the point $x$, intersection of `X_1` and
`X_2`; conditions (ii) and (iii) of `(15.2.3)` are also verified by this example. Nevertheless, $\mathcal{O}_{x}$ is not
a torsion-free $\mathcal{O}_{y}$-module, $\mathcal{O}_{y}$ being identified with a subring of $\mathcal{O}_{x}$ that
contains zero-divisors in $\mathcal{O}_{x}$; hence $f$ is not flat at the point $x$.

*(iii)* In `(15.2.3)`, the conclusion is no longer necessarily valid when one replaces hypothesis (ii) by the weaker
hypothesis that $f^{-1}(y)$, considered as a $k(y)$-prescheme, has no embedded associated prime cycles. An example is
furnished by taking for $Y$ a curve having a cusp at a point $y$, for example $Y = \operatorname{Spec}(K[S, T]/(S^{3} -
T^{2}))$, $K$ being an algebraically closed field, and for $X$ its normalization `(II, 6.3.8)`. If $s$ and $t$ are the
classes of $S$ and $T$ in $A = K[S, T]/(S^{3} - T^{2})$, one verifies at once that $X = \operatorname{Spec}(B)$, where
$B = K[s, t, u]$, $u$ being the element $t/s$ of the fraction field of $A$, and as $s = u^{2}$, $t = u^{3}$, one has
also $B = K[u]$, isomorphic to the polynomial ring in one indeterminate over $K$. The only point $x$ of $X$ above the
point $y$ corresponding to the maximal ideal $(s) + (t)$ corresponds to the maximal ideal `(u)`; but as the class `ū` of
$u$ in $\mathcal{O}_{x} / \mathfrak{m}_{y} \mathcal{O}_{x}$ is such that $\bar{u}^{2} = 0$, $f^{-1}(y)$ is not a reduced
$k(y)$-prescheme. Here $f$ is a finite, surjective and radicial morphism, hence a universal homeomorphism `(2.4.5)`, but
is not flat at the point $x$, for if $\mathcal{O}_{x}$ were a flat $\mathcal{O}_{y}$-module, it would be a free
$\mathcal{O}_{y}$-module of rank `1` generated by the element `1` of $\mathcal{O}_{x}$ (Bourbaki, _Alg. comm._, chap.
II, §3, n° 2, prop. 5), which is absurd.

*(iv)* Let us show finally that in `(15.2.2)` or `(15.2.3)`, one cannot replace "geometrically reduced" by "reduced". We
shall in fact define two rings $A$, $A'$ having the following properties:

1. $A$ is a Noetherian local ring of maximal ideal $\mathfrak{m}$, integral, complete, of dimension `1` and
   geometrically unibranch.

1. $A'$ is the integral closure of $A$, a finite $A$-algebra whose maximal ideal is $\mathfrak{m} A'$, and the residue
   field $k'$ a finite radicial non-trivial extension of the residue field $k = A/\mathfrak{m}$ of $A$.

One may then take $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(A')$, $y = \mathcal{O}_{y}$, $y$ and $x$ being
the closed points of $Y$ and $X$ respectively; hypotheses (i) and (iv) of `(15.2.2)` are trivially verified; as $A$ is
of dimension `1`, $f : X \to Y$ is radicial, finite and surjective, hence a universal homeomorphism `(2.4.5)`, which
proves hypothesis (i) of `(15.2.3)`. Finally, it is clear that $f^{-1}(y)$ is reduced. Nevertheless $f$ is not flat at
the point $x$, for if $A'$ were a flat $A$-module, it would be a free $A$-module of rank `1` (since it has the same
fraction field as $A$) generated by the element `1` of $A$ (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, prop. 5), which
is absurd.

To construct the rings $A$ and $A'$, start from an imperfect field $k$ of characteristic $p > 0$; let $K_{0} = k((T))$
be the field of formal power series over $k$, `A_0` the valuation ring for `K_0` corresponding to the discrete valuation
equal to the *order* of the formal series; the residue field of `A_0` is therefore $k$. Let $\alpha$ be an element of
$k$ which is not a $p$-th power, and take $k' = k(\alpha^{1/p})$; $K = k'((T))$ is then a finite radicial extension of
`K_0`, and $A' = A_{0} \otimes_{k} k'$ the discrete valuation ring for $K$ corresponding to the order of formal series
over $K$. If $\mathfrak{m}'$ is the maximal ideal of $A'$, one will answer conditions 1) and 2) by taking $A = A_{0} +
\mathfrak{m}'$: indeed, as `A_0` is Noetherian and $A'$ an `A_0`-module of finite type, $A$ is a finite `A_0`-algebra,
hence a Noetherian ring; as $A'$ is finite over $A$, $\mathfrak{m}'$ is the only maximal ideal of $A$, which is
therefore a complete local ring, evidently of dimension `1` (being finite over `A_0`) and geometrically unibranch since
$A'$ is integrally closed and has the same fraction field $K$ as $A$.

*(v)* The proof of `(15.2.2)` shows nevertheless that one may weaken condition (iii) by replacing in it "geometrically
reduced" by "reduced" when one can apply the valuative criterion of flatness `(11.8.1)` using only discrete valuation
rings $A'$ whose residue field $k'$ is separable over $k(y)$; indeed, if $x'$ and $z'$ have the same significations as
in `(15.2.2)`, the radicial multiplicities $\mu_{r}(k(x') | k')$ and $\mu_{r}(k(z) | k(y))$ are the same, by virtue of
`(4.7.3)`, hence it follows from `(4.7.9)` that $long((\mathcal{F}_{y})_{z})$ and $long((\mathcal{F}'_{y'})_{z'})$ are
equal, and one is again reduced to the case where $Y$ is the spectrum of a discrete valuation ring and $y$ its closed
point. For example, one will be able to obtain this stronger result when $\mathcal{O}_{y}$ is unibranch and dominated by
a discrete valuation ring whose residue field is a separable extension of $k(y)$, by virtue of `(11.6.4)`. This is the
case when $\mathcal{O}_{y}$ is a regular ring, after `(15.1.1.6)`. But, as Hironaka has pointed out to us, there exist
integrally closed Noetherian local rings of dimension `2` (coming from algebraic schemes over imperfect fields) which do
not satisfy the preceding condition.

### 15.3. Applications: criteria of reduction and of irreducibility

**Proposition (15.3.1).**

<!-- label: IV.15.3.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module, $x$ a point of $X$, $y = f(x)$. Suppose conditions (i), (ii) and (iii) of `(15.2.2)` verified.
Then:*

*(i) There exists a neighbourhood $U$ of $x$ in $X$ such that $f | U$ be universally open and that, for every $x' \in
U$, $\mathcal{F}_{x'}$ be geometrically reduced over $k(f(x'))$ at the point $x'$.*

*(ii) If moreover $Y$ is reduced at the point $y$, there exists a neighbourhood $U_{1} \subset U$ of $x$ such that
$\mathcal{F} | U_{1}$ be $f$-flat and reduced.*

<!-- original page 227 -->

Taking into account `(I, 5.1.8)`, `(4.2.7)` and `(4.7.11)`, the hypotheses do not change, nor the conclusion (i) of the
statement, if one replaces $Y$ by $Y_{red}$ and $X$ by $X \times_{Y} Y_{red}$, and one may therefore suppose $Y$
reduced. It then follows from `(15.2.2)` that $\mathcal{F}$ is $f$-flat at the point $x$, hence also `(11.1.1)` in a
neighbourhood of $x$, and a fortiori $f$ is universally open in this neighbourhood `(2.4.6)`. The fact that
$\mathcal{F}_{x'}$ is then geometrically reduced at the point $x'$ for all points of a neighbourhood of $x$ follows from
`(12.1.1, (vii))`. Assertion (ii) therefore follows from what precedes and from `(3.3.4)`.

**Proposition (15.3.2).**

<!-- label: IV.15.3.2 -->

*The notation being that of `(15.3.1)`, suppose that conditions (i), (ii), (iii) of `(15.2.2)` are verified, and
moreover that $f^{-1}(y)$ is equidimensional at the point $x$. Then $f$ is equidimensional at the point $x$.*

One has, for every $y' \in Y$, $Supp(\mathcal{F}_{y'}) = f^{-1}(y')$. By hypothesis $\mathcal{F}_{y}$ is reduced (hence
satisfies `(S_1)`) and is equidimensional at the point $x$. By virtue of `(12.1.1, (ii))`, one may therefore suppose
that $\mathcal{F}_{y'}$ is equidimensional and of constant dimension $e = \dim_{x}(f^{-1}(y))$ at the point $x'$ for all
$x' \in U$, which means that $f^{-1}(f(x'))$ is equidimensional and of dimension $e$ at the point $x'$. As moreover
$\mathcal{F} | U$ is $f$-flat, it follows from `(2.3.4)` and from `(13.3.1, a))` that $f$ is equidimensional at the
point $x$.

**Corollary (15.3.3).**

<!-- label: IV.15.3.3 -->

*The notation being that of `(15.3.1)`, suppose the following conditions verified:*

*(i) $Supp(\mathcal{F}) = X$.*

*(ii) $f$ is universally open at the generic points of the irreducible components of $f^{-1}(y)$ containing $x$.*

*(iii) $\mathcal{F}_{y}$ is geometrically pointwise integral over $k(y)$ at the point $x$ `(4.6.22)`.*

*(iv) $Y$ is geometrically unibranch at the point $y$.*

*Then $x$ belongs to only one irreducible component of $X$.*

*If moreover $Y$ is integral at the point $y$ and $\mathcal{F} = \mathcal{O}_{X}$, then $X$ is integral at the point $x$
and $f$ is flat at the point $x$.*

Note first that (i) and (iii) entail that $x$ belongs to only one irreducible component $Z$ of $f^{-1}(y)$. It follows
therefore from `(14.4.7)` and from `(15.3.2)` that for every irreducible component $X_{i}$ of $X$ containing $x$ (hence
$Z$), the restriction $f_{i}$ of $f$ to $X_{i}$ is a morphism equidimensional at the point $x$, and universally open at
the generic point of $Z$. The first assertion of the statement then follows from `(15.1.3)` and the second from
`(15.3.1)`.

**Remarks (15.3.4).**

<!-- label: IV.15.3.4 -->

*(i)* The example `(14.4.10, (ii))` shows that, in `(15.3.3)`, one cannot suppress the hypothesis that $Y$ is
geometrically unibranch at the point $y$.

*(ii)* The remark `(15.2.4, (v))` shows that the conclusion of `(15.3.3)` is still valid under the following hypotheses:
$\mathcal{O}_{y}$ is regular, $Supp(\mathcal{F}) = X$ and $\mathcal{F}_{y}$ is integral at the point $x$. We do not know
whether in this statement, one may replace the hypothesis that $\mathcal{O}_{y}$ is regular by the hypothesis that it is
geometrically unibranch, or even integral and integrally closed.

### 15.4. Complements on Cohen-Macaulay morphisms

**Proposition (15.4.1).**

<!-- label: IV.15.4.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module such that $Supp(\mathcal{F}) = X$, $x$ a point of $X$, $y = f(x)$. One sets, for every $x' \in
X$, $X_{f(x')} = f^{-1}(f(x'))$, $\mathcal{F}_{f(x')} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(f(x'))$. Suppose that
$\mathcal{F}$ is $f$-flat at the point $x$ and that $\mathcal{F}_{y}$ is a Cohen-Macaulay $\mathcal{O}_{X_{y}}$-Module
at the point $x$. Then $f$ is equidimensional at the point $x$.*

<!-- original page 228 -->

Indeed (`(11.1.1)` and `(12.1.1, (vi))`), there exists a neighbourhood $U$ of $x$ such that $\mathcal{F} | U$ be
$f$-flat and that for every $x' \in U$, $\mathcal{F}_{f(x')}$ be a Cohen-Macaulay $\mathcal{O}_{X_{f(x')}}$-Module at
the point $x'$; this latter property entails that $\mathcal{F}_{f(x')}$ is equidimensional at the point $x'$ and that
$x'$ belongs to no embedded associated prime cycle associated with $\mathcal{F}_{f(x')}$ $(0_{IV}, 16.5.4)$. Moreover,
by virtue of `(12.1.1, (ii))`, one may suppose that the dimensions of the irreducible components of
$Supp(\mathcal{F}_{f(x')} | (U \cap X_{f(x')}))$ have a (same) value independent of $x'$. As $Supp(\mathcal{F}_{f(x')})
= X_{f(x')}$ by hypothesis, it follows from `(2.3.4)` and from `(13.3.1, a))` that $f$ is equidimensional at the point
$x$.

**Proposition (15.4.2).**

<!-- label: IV.15.4.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module such that $Supp(\mathcal{F}) = X$, $x$ a point of $X$, $y = f(x)$. Suppose that
$\mathcal{O}_{y}$ is regular and that $\mathcal{F}$ is a Cohen-Macaulay $\mathcal{O}_{X}$-Module at the point $x$. Then
(with the notation of `(15.4.1)`) the following conditions are equivalent:*

*a) $\mathcal{F}$ is $f$-flat at the point $x$ and $\mathcal{F}_{y}$ is a Cohen-Macaulay $\mathcal{O}_{X_{y}}$-Module at
the point $x$.*

*b) $\mathcal{F}$ is $f$-flat at the point $x$.*

*c) $f$ is universally open in a neighbourhood of $x$.*

*d) $f$ is open at the generic points of the irreducible components of $X_{y}$ containing $x$.*

*e) `dim(𝒪_{X_y, x}) = dim(𝒪_x) − dim(𝒪_y)`.*

*e') `dim_x(ℱ_y) = dim_x(ℱ) − dim(𝒪_y)`.*

Since $Supp(\mathcal{F}) = X$, conditions e) and e') are equivalent by definition `(5.1.12)`. Condition a) implies
trivially b); b) entails that $\mathcal{F}$ is $f$-flat at the points of a neighbourhood of $x$ `(11.1.1)`, hence b)
entails c) `(2.4.6)`; c) entails trivially d), and d) entails e') by `(14.2.1)`. Finally, since $\mathcal{O}_{y}$ is
regular and $\mathcal{F}_{x}$ is a Cohen-Macaulay $\mathcal{O}_{x}$-module, it follows from `(6.1.4)` that e) entails
a).

**Proposition (15.4.3).**

<!-- label: IV.15.4.3 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module of finite
presentation, such that $Supp(\mathcal{F}) = X$, $x$ a point of $X$, $y = f(x)$. Then (with the notation of `(15.4.1)`)
the following conditions are equivalent:*

*a) $\mathcal{F}$ is $f$-flat at the point $x$ and $\mathcal{F}_{y}$ is a Cohen-Macaulay $\mathcal{O}_{X_{y}}$-Module at
the point $x$.*

*b) There exists an open neighbourhood $U$ of $x$ in $X$, and a $Y$-morphism quasi-finite $g : U \to Y' = Y[T_{1},
\cdots, T_{m}]$ ($T_{i}$ indeterminates), such that $\mathcal{F} | U$ be $g$-flat at the point $x$.*

Let us first show that b) entails a). Set $h : Y' \to Y$; the $k(y)$-prescheme $Y'_{y} = h^{-1}(y)$ is regular
`(0, 17.3.7)`; let $A$ be the local ring of this prescheme at the point $y' = g(x)$, $k$ its residue field, and let $B$
be the local ring of $X_{y}$ at the point $x$; set on the other hand $(\mathcal{F}_{y})_{x} = M$, which is a $B$-module
of finite type. The hypothesis that the morphism $g$ is quasi-finite entails that the same holds for $g_{y} : X_{y} \to
Y'_{y}$ `(II, 6.2.4)`, hence $M \otimes_{A} k$ is a $(B \otimes_{A} k)$-module of finite length `(II, 6.2.2)`; as by
hypothesis $M$ is a flat $A$-module and $A$ a Cohen-Macaulay ring, $M$ is a Cohen-Macaulay $B$-module `(6.3.3)`. The
fact that $\mathcal{F}$ is $f$-flat at the point $x$ follows from the fact that it is $g$-flat and from the fact that
the morphism $h$ is flat `(2.1.6)`.

Let us now show that a) entails b). The question being local on $X$ and $Y$, one may suppose $X$ and $Y$ affine; using
`(8.9.1)` and `(11.2.7)`, one reduces to the case where $X$ and $Y$ are Noetherian, taking `(6.7.1)` into account. The
hypothesis entails that $f$ is

<!-- original page 229 -->

equidimensional at the point $x$ `(15.4.1)`, whence the existence of a quasi-finite morphism $g : U \to Y'$ such that
every irreducible component of $U$ dominates $Y'$ `(13.3.1, b))` and that $g_{y} : U_{y} \to Y'_{y}$ be finite and
surjective `(13.3.1.1)`. On the other hand, in order to prove that $\mathcal{F} | U$ is $g$-flat at the point $x$, it
suffices, since $h : Y' \to Y$ is flat, to show (by virtue of the fibrewise flatness criterion `(11.3.10)`) that
$\mathcal{F}_{y}$ is $g_{y}$-flat at the point $x$. But by hypothesis $\mathcal{F}_{y}$ is a Cohen-Macaulay
$\mathcal{O}_{X_{y}}$-Module at the point $x$ and $Y'_{y}$ a regular prescheme; on the other hand, as $g_{y}$ is finite
and surjective, it satisfies condition e') of `(15.4.2)` by virtue of `(5.6.10)`; it therefore suffices to conclude to
apply `(15.4.2)` to $g_{y}$ and to $\mathcal{F}_{y}$.

### 15.5. Separable rank of the fibres of a quasi-finite and universally open morphism. Application to the geometric connected components of the fibres of a proper morphism

**Proposition (15.5.1).**

<!-- label: IV.15.5.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a separated and quasi-finite morphism. For every $z \in Y$,
let $n(z)$ be the geometric number of points of $f^{-1}(z)$ (or separable rank of $f^{-1}(z)$ over $k(z)$; cf.
`(I, 6.4.8)`). One has the following properties:*

*(i) The function $z \mapsto n(z)$ is lower semi-continuous at every point $y \in Y$ such that $f$ is universally open
at the points of $f^{-1}(y)$.*

*(ii) Let $y$ be a point of $Y$ such that $f$ is universally open at the points of $f^{-1}(y)$; if the function $z
\mapsto n(z)$ is constant in a neighbourhood of $y$, then $f$ is proper at the point $y$ `(15.7.1)`.*

*(iii) Suppose that $f$ is universally open and that every point of $Y$ is geometrically unibranch; then, if the
function $z \mapsto n(z)$ is locally constant in $Y$, the irreducible components of $X$ are pairwise disjoint.*

(i) Note that since $f$ is quasi-finite, the number $n(z)$ is the geometric number of connected components of
$f^{-1}(z)$; one knows that the function $z \mapsto n(z)$ is locally constructible `(9.7.9)`; taking $(0_{III}, 9.3.4)$
into account, one is reduced to proving the

**Corollary (15.5.2).**

<!-- label: IV.15.5.2 -->

*Under the general hypotheses of `(15.5.1)`, let $y$ be a point of $Y$ such that $f$ is universally open at the points
of $f^{-1}(y)$. Then, if $y'$ is a generization of $y$, one has*

$$ (15.5.2.1) n(y') \geq n(y). $$

For every base change $g : Z \to Y$, $f_{(Z)} : X_{(Z)} \to Z$ is separated, quasi-finite and universally open at the
points of $X_{(Z)}$ projecting into $f^{-1}(y)$; moreover, if $z$, $z'$ are two points of $Z$ such that $g(z) = y$,
$g(z') = y'$ and that $z'$ is a generization of $z$, one has $n(z) = n(y)$ and $n(z') = n(y')$ `(I, 6.4.12)`; it
therefore suffices to demonstrate `(15.5.2.1)` for a suitable $g$. One may evidently suppose $y \neq y'$. We shall use
the following lemma:

**Lemma (15.5.2.2).**

<!-- label: IV.15.5.2.2 -->

*Under the general hypotheses of `(15.5.1)`, if $y$ is a point of $Y$, $y'$ a generization of $y$ distinct from $y$,
there exists a spectrum of a discrete valuation ring $Z$, of closed point $z$ and of generic point $z'$, and a morphism
$g : Z \to Y$ such that: 1° $g(z) = y$, $g(z') = y'$; 2° if one sets $f' = f_{(Z)}$, $n(y)$ is the number of points of
$f'^{-1}(z)$ and $n(y')$ is the number of points of $f'^{-1}(z')$.*

Indeed, there exists a discrete valuation ring `A_1` and a morphism $g_{1}$ of $Z_{1} = \operatorname{Spec}(A_{1})$ into
$Y$ such that if $z_{1}$ and $z'_{1}$ are the closed point and the generic point of `Z_1`,

<!-- original page 230 -->

one has $g_{1}(z_{1}) = y$ and $g_{1}(z'_{1}) = y'$ `(II, 7.1.9)`; one may therefore already suppose that $Y$ is the
spectrum of a discrete valuation ring $A$, $y$ its closed point and $y'$ its generic point. For every $x \in f^{-1}(y)$,
$k(x)$ is a finite extension of $k(y)$ by hypothesis `(II, 6.2.2)`; one deduces from `(4.5.11)` that there exists a
finite algebraic extension $k$ of $k(y)$ such that the number of points of $f^{-1}(y) \otimes_{k(y)} k$ be equal to
$n(y)$. As there is a discrete valuation ring `A_2` dominating $A$ and whose residue field is finite over $k(y)$ and
contains $k$ `(II, 7.1.2)`, one may in the second place suppose that $n(y)$ is the number of points of $f^{-1}(y)$.
Finally, the same reasoning shows that there is a finite extension $K$ of $k(y')$ such that the number of points of
$f^{-1}(y') \otimes_{k(y')} K$ be equal to $n(y')$; if $w$ is a valuation of $k(y')$ associated with $A$, there is a
discrete valuation of $K$ extending $w$, and the ring `A_3` of this valuation dominates $A$, has $K$ as fraction field,
and answers the conditions of the lemma.

One may therefore henceforth suppose that $Y$ is the spectrum of a discrete valuation ring, $y$ its closed point, $y'$
its generic point, and that $n(y)$ and $n(y')$ are the numbers of points of $f^{-1}(y)$ and $f^{-1}(y')$, so that for
every $x \in f^{-1}(y)$ (resp. every $x' \in f^{-1}(y')$) one has $k(x) = k(y)$ (resp. $k(x') = k(y')$).

Designate then by $X_{i}$ the reduced subpreschemes of $X$ having as underlying spaces the irreducible components of $X$
($1 \leq i \leq m$). By virtue of `(1.10.4)`, the restriction $X_{i} \to Y$ of $f$ to every $X_{i}$ is a dominant
morphism, and as $f^{-1}(y')$ is discrete, each of the intersections $X_{i} \cap f^{-1}(y')$ reduces to the generic
point of $X_{i}$, whence (denoting by $n_{i}(z)$ the geometric number of points of $X_{i} \cap f^{-1}(z)$ for every $z
\in Y$), $n_{i}(y') = 1$ for every $i$, and $n(y') = \sum_{i} n_{i}(y') = m$. On the other hand, $f^{-1}(y)$ is the
union of the $X_{i} \cap f^{-1}(y)$, whence

$$ (15.5.2.3) n(y) \leq \sum_{i} n_{i}(y), $$

and to prove `(15.5.2.1)`, it suffices to establish that $n_{i}(y) \leq 1$ for every $i$. In other words, one may
suppose $X$ integral, and the morphism $f$ birational. But then, for every $x \in f^{-1}(y)$, one has $\mathcal{O}_{y}
\subset \mathcal{O}_{x} \subset K$, where $K = k(y')$ is the fraction field of $\mathcal{O}_{y}$. As $\mathcal{O}_{y}$
is a valuation ring and $\mathcal{O}_{x}$ dominates $\mathcal{O}_{y}$, one necessarily has $\mathcal{O}_{y} =
\mathcal{O}_{x}$ `(II, 7.1.1)`. There exists then a $Y$-section $h : Y \to X$ such that $h(y) = x$ `(I, 2.4.4)`; as $Y$
is reduced and $X$ is separated over $Y$, such a section is unique `(I, 7.2.2)`, hence the set $f^{-1}(y)$ contains only
a single point, which finishes proving (i).

(ii) As at the beginning of (i), one is reduced to showing that if the two sides of `(15.5.2.1)` are equal for every
generization $y'$ of $y$, $f$ is proper at the point $y$. Thanks to the criterion of local properness `(15.7.5)` and the
remarks at the beginning one may again suppose that $Y = \operatorname{Spec}(A)$ is the spectrum of a discrete valuation
ring $A$, $y$ its closed point and $y'$ its generic point, and it is then a question of showing that $f$ is proper.

Using `(15.5.2.2)` and noting that if $A'$ is a discrete valuation ring dominating $A$, $A'$ is a torsion-free
$A$-module, hence the morphism $\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is faithfully flat and
quasi-compact, it amounts to the same to say that $f$ is proper or that the morphism deduced from $f$ by the base change
$\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is proper

<!-- original page 231 -->

`(2.7.1, (vii))`; one may therefore suppose that $n(y)$ and $n(y')$ are the numbers of points of the fibres $f^{-1}(y)$
and $f^{-1}(y')$ respectively. With the notation of (i), one then has by `(15.5.2.3)` and `(15.5.2.1)`

```text
  (15.5.2.4)             n(y) ≤ ∑_i n_i(y) ≤ ∑_i n_i(y') = n(y'),
```

and for the extreme terms to be equal, it is necessary that $n_{i}(y) = n_{i}(y') = 1$ for every $i$. As one has seen in
(i), if $n_{i}(y) = 1$ for every $i$, $X_{i} \cap f^{-1}(y)$ is non-empty and the restriction $X_{i} \to Y$ of $f$ is an
isomorphism; as the $X_{i}$ are closed subpreschemes of $X$, this entails that $f$ is proper `(II, 5.4.5)`.

(iii) One may restrict to the case where $Y$ is affine and reduced, and as $Y$ is by hypothesis locally integral
`(I, 5.1.4)`, one may suppose $Y$ integral, and the function $y \mapsto n(y)$ constant in $Y$. Let again $X_{i}$ ($1
\leq i \leq m$) be the irreducible components of $X$. It follows from `(1.10.4)` that if $y'$ is the generic point of
$Y$, each of the $X_{i} \cap f^{-1}(y')$ reduces to a single point; the restriction $f_{i} : X_{i} \to Y$ of $f$ being a
quasi-finite and dominant morphism and every point of $Y$ being geometrically unibranch, it follows from Chevalley's
criterion `(14.4.4)` that $f_{i}$ is universally open. If then $y$ is any point of $Y$, one has $n_{i}(y) \geq
n_{i}(y')$; on the other hand, as the $X_{i} \cap f^{-1}(y')$ are pairwise disjoint, $\sum_{i} n_{i}(y') = n(y')$; one
therefore has again the relations `(15.5.2.4)`. But by hypothesis the extreme terms are equal, hence $n(y) = \sum_{i}
n_{i}(y)$, which implies that the $X_{i} \cap f^{-1}(y)$ are pairwise disjoint, and finishes the demonstration.

Combining this proposition with Zariski's connectedness theorem and its consequences `(III, 4.3)`, one obtains the
following results which complete `(III, 4.3.7 and 4.3.10)`:

**Proposition (15.5.3).**

<!-- label: IV.15.5.3 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, $f : X \to Y$ a proper morphism; for every $y \in Y$, let
$n(y)$ be the geometric number of connected components `(4.5.2)` of $f^{-1}(y)$. Suppose that the restriction of $f$ to
every irreducible component of $X$ is a morphism dominant in $Y$. Then, if $y_{0}$ is a geometrically unibranch point of
$Y$, the function $y \mapsto n(y)$ is lower semi-continuous at the point $y_{0}$.*

Consider the Stein factorization $f = g \circ f'$ of $f$ `(III, 4.3.3)`, where $g : Y' \to Y$ is a finite morphism and
$f' : X \to Y'$ a surjective morphism whose fibres are geometrically connected `(III, 4.3.4)`. Since $f'$ is surjective,
the inverse image under $f'$ of every irreducible component of $Y'$ contains an irreducible component of $X$ at least;
hence each of the irreducible components of $Y'$ dominates $Y$. One may therefore apply Chevalley's criterion `(14.4.4)`
to the restrictions of $g$ to each of these irreducible components, and one concludes that $g$ is universally open at
every point of $g^{-1}(y_{0})$. The conclusion therefore follows from `(15.5.2)` and from the fact that the geometric
number of connected components of $f^{-1}(y)$ is equal to the geometric number of points of $g^{-1}(y)$ `(III, 4.3.4)`.

**Corollary (15.5.4).**

<!-- label: IV.15.5.4 -->

\*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism; let $y$ be a point of $Y$ such that $f$ be
universally open at the points of $f^{-1}(y)$;

<!-- original page 232 -->

then, with the notation of `(15.5.3)`, the function $z \mapsto n(z)$ is lower semi-continuous at the point $y$.\*

With the notation of `(15.5.3)`, note that in the Stein factorization $f = g \circ f'$, $f'$ is surjective; as $f$ is
universally open at the points of $f^{-1}(y)$, $g$ is universally open at the points of $g^{-1}(y)$ `(14.3.4, (i))`; it
then suffices to apply to $g$ proposition `(15.5.1, (i))` taking `(III, 4.3.4)` into account.

**Remarks (15.5.5).**

<!-- label: IV.15.5.5 -->

*(i)* Even if $Y$ is integral and normal, $X$ integral, $f$ finite and surjective (hence universally open by virtue of
Chevalley's criterion `(14.4.4)`), the function $y \mapsto n(y)$ is not necessarily locally constant. One has an example
of this by taking $Y = \operatorname{Spec}(k[T])$ where $k$ is algebraically closed, and $X = \operatorname{Spec}(A)$,
where $A = k[S, T]/(S^{2} + T^{2} - 1)$; at the points $y'$, `y''` of $Y$ corresponding to the maximal ideals $(T - 1)$
and $(T + 1)$, one has $n(y') = n(y'') = 1$, but $n(y) = 2$ at all the other points of $Y$. We shall give below an
additional condition assuring that $y \mapsto n(y)$ is locally constant `(15.5.7)`.

*(ii)* The example `(14.4.10, (ii))` shows that in `(15.5.1, (iii))`, one cannot suppress the hypothesis that the points
of $Y$ are geometrically unibranch.

*(iii)* The example `(11.7.5)` shows that the conclusion of `(15.5.1, (i))` is no longer valid if one supposes only that
the morphism $f$ is open (even if, as is the case in the example cited, $f$ is finite and surjective).

*(iv)* Finally, in `(15.5.1)`, one cannot dispense with the hypothesis that the morphism $f$ is separated, as is shown
by the example where $X$ is the affine line of which one has "doubled a point" `(I, 5.5.11)`, and $Y$ the affine line:
here $f$ is a local isomorphism (hence is flat) and is quasi-finite, but $z \mapsto n(z)$ is not lower semi-continuous.

**Lemma (15.5.6).**

<!-- label: IV.15.5.6 -->

*Let $Y$ be the spectrum of a discrete valuation ring, $a$ its closed point, $b$ its generic point. Let $f : X \to Y$ be
a morphism locally of finite type and open. Suppose that $X$ is connected and that the fibre $f^{-1}(a)$ is a reduced
prescheme. Then $f^{-1}(b)$ is connected.*

We shall use the following purely topological lemma (particular case of a more general result of chap. III, 3rd Part):

**Lemma (15.5.6.1).**

<!-- label: IV.15.5.6.1 -->

*Let $X$ be a locally Noetherian space, every closed irreducible part of which admits a generic point. Let $Z$ be a rare
closed part of $X$ having the following property: for every $x \in Z$, if one designates by $T_{x}$ the set of
generizations of $x$ in $X$, then $T_{x} - {x}$ is connected. Under these conditions, if $X$ is connected, $X - Z$ is
connected.*

Let us give an independent demonstration. Reasoning by contradiction, suppose that the open set $U = X - Z$, everywhere
dense in $X$, is the union of two non-empty open sets with no common point $U'$, `U''`, and designate by $X'$ and `X''`
the closures in $X$ of $U'$ and `U''`. As $X = U \subset X' \cup X''$ and $X$ is connected, one has
$X' \cap X'' \neq \emptyset$, and it is clear that $X' \cap X'' \subset Z$. Let $x$ be a generic point of an irreducible
component of $X' \cap X''$. As $X$ is locally Noetherian, there is an open neighbourhood $V$ of $x$ in $X$ such that
$V \cap U'$ and $V \cap U''$ have only a finite number of irreducible components; as $x$ is adherent to $U'$ and to
`U''`, it is necessarily in the closure of an irreducible component $Z'$ of $V \cap U'$ and in the closure of an
irreducible component `Z''` of $V \cap U''$. But $Z'$ (resp. `Z''`) is closed and irreducible in $X$, hence admits a
generic point $z'$ (resp. `z''`), and one necessarily has $z' \in U'$ and $z'' \in U''$. This proves that the
intersections of $T_{x} - {x}$ with $U'$ and `U''` are non-empty. But by definition
$(X' \cap X'') \cap (T_{x} - {x}) = \emptyset$; hence the intersections of $X'$ and `X''` with $T_{x} - {x}$ are two
non-empty closed disjoint subsets in $T_{x} - {x}$, whose union is $T_{x} - {x}$; now this contradicts the hypothesis
that $T_{x} - {x}$ is connected. Q.E.D.

<!-- original page 233 -->

To prove `(15.5.6)`, we shall apply the lemma `(15.5.6.1)` to $X$ and to its closed part $Z = f^{-1}(a)$ which is rare
since $f$ is open. Note that the hypothesis, taking `(15.2.2.1)` into account, implies that $f$ is flat at the points of
$f^{-1}(a)$. For such a point $x$, $\mathcal{O}_{x}$ is then a torsion-free $\mathcal{O}_{a}$-module $(0_{I}, 6.3.4)$,
and in particular, if $t$ is a uniformizer of $\mathcal{O}_{a}$, $t$ is $\mathcal{O}_{x}$-regular. Moreover
$\mathcal{O}_{x} / t \mathcal{O}_{x}$ is reduced by hypothesis; if it is of depth `0`, it is therefore a field
`(0, 16.4.7)`, and as $t \mathcal{O}_{x}$ is then the maximal ideal of $\mathcal{O}_{x}$, $\mathcal{O}_{x}$ is a
discrete valuation ring `(0, 17.1.4)`, hence $\operatorname{Spec}(\mathcal{O}_{x}) - {x}$ reduces to a point, and *a
fortiori* is connected. If on the contrary $prof(\mathcal{O}_{x} / t \mathcal{O}_{x}) \geq 1$, one has
$prof(\mathcal{O}_{x}) \geq 2$ since $t$ is $\mathcal{O}_{x}$-regular `(0, 16.4.6)`; it then follows from Hartshorne's
theorem `(5.10.7)` that $\operatorname{Spec}(\mathcal{O}_{x}) - {x}$ is connected, which ends the demonstration.

**Proposition (15.5.7).**

<!-- label: IV.15.5.7 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism. For every $z \in Y$, let $n(z)$ be the
geometric number of connected components of $f^{-1}(z)$. Let $y$ be a point of $Y$ such that $f$ be universally open at
the points of $f^{-1}(y)$ and that $f^{-1}(y)$ be geometrically reduced over $k(y)$ `(4.6.2)`. Then the function $z
\mapsto n(z)$ is constant in a neighbourhood of $y$.*

One knows already `(15.5.4)` that under the conditions of the statement, $z \mapsto n(z)$ is lower semi-continuous at
the point $y$; everything comes down to seeing that it is also upper semi-continuous, and by the same reasoning as at
the beginning of the demonstration of `(15.5.1, (i))`, it suffices to show that if $y'$ is a generization of $y$, one
has

$$ (15.5.7.1) n(y') \leq n(y). $$

Using the reasoning at the beginning of the demonstration of `(15.5.2)` and the lemma `(15.5.2.2)` applied to the finite
morphism $g$ of the Stein factorization $f = g \circ f'$ of $f$ (recalling that the geometric number of points of
$g^{-1}(y)$ is equal to that of the connected components of $f^{-1}(y)$ `(III, 4.3.4)`), one is reduced to the case
where $n(y)$ and $n(y')$ are respectively the number of connected components of $f^{-1}(y)$ and $f^{-1}(y')$, and where
$Y$ is the spectrum of a discrete valuation ring, $y$ the closed point and $y'$ the generic point of $Y$. One may in
addition replace $X$ by any one of its connected components, these latter being open and closed in $X$, and proper over
$Y$. Suppose then $X$ connected; the hypothesis that $f$ is open at the points of $f^{-1}(y)$ entails that if $f^{-1}(y)
\neq \emptyset$, one has also $f^{-1}(y') \neq \emptyset$ `(1.10.3)`; the hypothesis that $f$ is closed entails that if
$f^{-1}(y') \neq \emptyset$, one has also $f^{-1}(y) \neq \emptyset$ `(II, 7.2.1)`. Hence, if $X \neq \emptyset$ (which
one may evidently suppose, the proposition being trivial in the contrary case), $f^{-1}(y)$ and $f^{-1}(y')$ are both
non-empty. Moreover, the hypothesis entails that the prescheme $f^{-1}(y)$ is reduced `(4.6.1)`; as $f$ is open at the
points of $f^{-1}(y)$, the lemma `(15.5.6)` implies that $f^{-1}(y')$ is connected, in other words $n(y') = 1$. As
$f^{-1}(y)$ is not empty, this proves `(15.5.7.1)`.

**Remark (15.5.8).**

<!-- label: IV.15.5.8 -->

The relation `(15.5.7.1)` is no longer necessarily valid if $f$ is not supposed proper, even if it verifies the other
hypotheses of `(15.5.7)`. With the notation of `(15.5.5, (i))`, it suffices to see this to consider the restriction of
$f$ to $X - {x'}$, where $x'$ is one of the two points of $X$ above a point $y$ distinct from $y'$ and `y''`; one then
has $n(y) = 1$, while if $\eta$ is the generic point of $Y$, $n(\eta) = 2$.

<!-- original page 234 -->

**Proposition (15.5.9).**

<!-- label: IV.15.5.9 -->

*Let $f : X \to Y$ be a flat morphism locally of finite presentation; for every $y \in Y$, let $n(y)$ be the geometric
number of connected components of $f^{-1}(y)$.*

*(i) If $f$ is separated and quasi-finite, the function $y \mapsto n(y)$ (then equal to the geometric number of points
of $f^{-1}(y)$) is lower semi-continuous in $Y$; if it is constant in a neighbourhood of $y_{0}$, $f$ is proper at the
point $y_{0}$.*

*(ii) If $f$ is proper, the function $y \mapsto n(y)$ is lower semi-continuous in $Y$; if moreover $f^{-1}(y_{0})$ is
geometrically reduced over $k(y_{0})$, $n(y)$ is constant in a neighbourhood of $y_{0}$.*

In all cases, the questions are local on $Y$, hence one may suppose $Y$ affine and $f$ of finite presentation; using
`(8.9.1)`, `(8.10.5)` and `(11.2.7)`, one is reduced to the case where $Y$ is Noetherian (using in addition `(8.2.11)`
for the second assertion of (i)). As moreover $f$ is then universally open `(2.4.6)`, it suffices to apply `(15.5.1)`,
`(15.5.4)` and `(15.5.7)` to conclude.

**Remark (15.5.10).**

<!-- label: IV.15.5.10 -->

One will note that one has thus obtained another demonstration of `(12.2.4, (vi))`. Conversely, one may deduce
`(15.5.7)` from `(12.2.4, (vi))`: indeed, one may restrict to the case where $Y$ is reduced (replacing $f$ by
$f_{red}$), and it then follows from the hypotheses of `(15.5.7)` and from `(15.2.3)` that $f$ is flat in an open
neighbourhood of $f^{-1}(y)$; as moreover $f$ is proper, one may suppose that this neighbourhood is of the form
$f^{-1}(U)$, where $U$ is an open neighbourhood of $y$ in $Y$. One then concludes by `(12.2.4, (vi))`. The demonstration
of `(15.5.7)` given above has the advantage of bringing out the result `(15.5.6)`, which has an independent interest.

### 15.6. Connected components of the fibres along a section

**Proposition (15.6.1).**

<!-- label: IV.15.6.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $g : Y \to X$ a $Y$-section
of $X$ `(I, 2.5.5)`. For every $y \in Y$, designate by $X^{\circ}_{y}$ the connected component of $f^{-1}(y)$ containing
the point $g(y)$. Let $y$ be a point of $Y$, $y'$ a generization of $y$ in $Y$. Then:*

*(i) If there exists an irreducible component $Z$ of $X^{\circ}_{y'}$, of dimension equal to $\dim(X^{\circ}_{y'})$ and
containing $g(y')$ (which will be the case if $X^{\circ}_{y'}$ is irreducible), one has*

$$ (15.6.1.1) \dim(X^{\circ}_{y}) \geq \dim(X^{\circ}_{y'}). $$

*(ii) If moreover $X^{\circ}_{y}$ is irreducible and if the two sides of `(15.6.1.1)` are equal, then $X^{\circ}_{y}
\subset \overline{X^{\circ}_{y'}}$ (closure in $X$).*

(i) Let $\overline{Z}$ be the closure of $Z$ in $X$; as $y$ is adherent to $y'$ and $g$ continuous, one has $g(y) \in
\overline{Z}$. As $Z = \overline{Z} \cap f^{-1}(y')$, it follows from Chevalley's semi-continuity theorem `(13.1.3)`
applied to the restriction of $f$ to the reduced closed subprescheme of $X$ having $\overline{Z}$ as underlying space,
that one has $\dim_{g(y)}(\overline{Z} \cap f^{-1}(y)) \geq \dim(Z)$; but the irreducible components of $\overline{Z}
\cap f^{-1}(y)$ containing $g(y)$ are evidently contained in $X^{\circ}_{y}$, whence *a fortiori* the inequality
`(15.6.1.1)`.

(ii) The reasoning of (i) shows in addition that if the two sides of `(15.6.1.1)` are equal, one necessarily has
$\dim_{g(y)}(\overline{Z} \cap f^{-1}(y)) = \dim_{g(y)}(X^{\circ}_{y})$; if $X^{\circ}_{y}$ is irreducible, this entails
$\overline{Z} \cap f^{-1}(y) = X^{\circ}_{y}$, hence $X^{\circ}_{y}$ is contained in $\overline{Z}$, and *a fortiori* in
$\overline{X^{\circ}_{y'}}$.

<!-- original page 235 -->

**Corollary (15.6.2).**

<!-- label: IV.15.6.2 -->

*With the notation of `(15.6.1)`, suppose in addition that for every $y \in Y$, $X^{\circ}_{y}$ is irreducible. Then the
function $z \mapsto \dim(X^{\circ}_{z})$ is upper semi-continuous in $Y$. If moreover this function is constant in a
neighbourhood of a point $y \in Y$, then one has $X^{\circ}_{y} \subset \overline{X^{\circ}_{y'}}$ for every
generization $y'$ of $y$.*

Let $y$ be a point of $Y$, and let $U$ be an affine open neighbourhood of $g(y)$ in $X$; then there is an open
neighbourhood $V$ of $y$ in $Y$ such that $g(V) \subset U$, and for every $z \in V$, $U \cap X^{\circ}_{z}$ is dense in
$X^{\circ}_{z}$, hence $\dim(X^{\circ}_{z}) = \dim(U \cap X^{\circ}_{z})$ `(4.1.1.3)`. Replacing $X$ by $U$, one may
therefore suppose that $f$ is a morphism of finite type. One then knows `(9.7.10)` that the function $z \mapsto
\dim(X^{\circ}_{z})$ is locally constructible, and the assertions of the corollary therefore follow from `(15.6.1)` and
from $(0_{III}, 9.3.4)$.

**Proposition (15.6.3).**

<!-- label: IV.15.6.3 -->

*With the notation of `(15.6.1)`, suppose that for every $y \in Y$, $X^{\circ}_{y}$ is geometrically irreducible
`(4.5.2)`. Then, for every $y \in Y$ such that the function $z \mapsto \dim(X^{\circ}_{z})$ is constant in a
neighbourhood of $y$, $f$ is universally open at the points of $X^{\circ}_{y}$.*

Let us apply criterion `(14.3.7)`. Let then $h : Y' \to Y$ be a morphism, $Y'$ being the spectrum of a discrete
valuation ring, of which we shall designate by $t$, $t'$ the closed point and the generic point respectively, and
suppose that $h(t) = y$, so that $y' = h(t')$ is a generization of $y$. Set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X'
\to Y'$, $g' = g_{(Y')} : Y' \to X'$. With the same notation as in `(15.6.1)`, the hypothesis made on the
$X^{\circ}_{z}$ implies that $X'^{\circ}_{t} = X^{\circ}_{y} \otimes_{k(y)} k(t)$ and $X'^{\circ}_{t'} = X^{\circ}_{y'}
\otimes_{k(y')} k(t')$, and that $X'^{\circ}_{t}$ and $X'^{\circ}_{t'}$ are irreducible `(4.4.1)`; as
$\dim(X^{\circ}_{y}) = \dim(X'^{\circ}_{t})$ and $\dim(X^{\circ}_{y'}) = \dim(X'^{\circ}_{t'})$ `(4.1.4)`, one sees that
one is reduced to proving the proposition for $f'$ and $X'^{\circ}_{t}$, in other words one may restrict to the case
where $Y$ is the spectrum of a discrete valuation ring, $y$ its closed point and $y'$ its generic point; if $x'$ is the
generic point of $X^{\circ}_{y'}$, it follows then from `(15.6.2)` that every point of $X^{\circ}_{y}$ is a
specialization of $x'$, whence the conclusion.

**Proposition (15.6.4).**

<!-- label: IV.15.6.4 -->

*Under the general hypotheses of `(15.6.1)`, let $X^{\circ}$ be the union of the $X^{\circ}_{y}$ as $y$ runs over $Y$.
If $y \in Y$ is such that $X^{\circ}_{y}$ is geometrically reduced over $k(y)$ `(4.6.2)` and if $f$ is universally open
at every point of $X^{\circ}_{y}$, then $X^{\circ}$ is a neighbourhood of $X^{\circ}_{y}$ in $X$. In particular, if $f$
is universally open and if, for every $y \in Y$, $X^{\circ}_{y}$ is geometrically reduced over $k(y)$, $X^{\circ}$ is
open in $X$.*

Let us first show that one may reduce to the case where $f$ is a morphism of finite type. Let $x$ be a point of
$X^{\circ}_{y}$; it follows from `(5.10.8.1)` (with $S = {0}$) that there is a finite sequence $(Z_{i})_{0 \leq i \leq
n}$ of irreducible components of $f^{-1}(y)$ such that $g(y) \in Z_{0}$, $x \in Z_{n}$, and $Z_{i} \cap Z_{i+1} \neq
\emptyset$ for $0 \leq i \leq n - 1$; the $Z_{i}$ being irreducible, there is a finite sequence $(U_{i})$ ($0 \leq i
\leq n$) of affine open sets in $f^{-1}(y)$ such that $g(y) \in U_{0}$, $x \in U_{n}$, $U_{i}$ being an affine
neighbourhood of a point $x_{i}$ of $Z_{i} \cap Z_{i-1}$ for $1 \leq i \leq n$. There is for each $i$ a quasi-compact
open set $W_{i}$ in $X$ such that $U_{i} = f^{-1}(y) \cap W_{i}$; let $W$ be the quasi-compact open set of $X$ union of
the $W_{i}$. As $g$ is continuous, there is an affine open neighbourhood $V$ of $y$ in $Y$ such that $g(V) \subset W$;
if $X' = W \cap f^{-1}(V)$, the restriction of $f$ to $X'$ is of finite type; moreover, if, for every $z \in V$,
$X'^{\circ}_{z}$ is the connected component of $X' \cap f^{-1}(z)$ containing $g(z)$, one has $X'^{\circ}_{z} \subset
X^{\circ}_{z}$, and $x$ belongs to $X'^{\circ}_{y}$. Indeed, each of the $U_{i}$ contains the two irreducible sets
$U_{i} \cap Z_{i-1}$ and $U_{i} \cap Z_{i}$ which meet, and the irreducible sets $U_{i} \cap Z_{i-1}$ and $U_{i-1} \cap
Z_{i-1}$ meet for $1 \leq i \leq n$;

<!-- original page 236 -->

the union of the $U_{i} \cap Z_{i-1}$ and the $U_{i} \cap Z_{i}$ for $0 \leq i \leq n$ is therefore connected and
contains $x$ and $g(y)$. As $f | X'$ is universally open at the points of $X'^{\circ}_{y}$, this ends proving our
assertion, for if the proposition is proved when $f$ is of finite type, the union $X'^{\circ}$ of the $X'^{\circ}_{z}$
for $z \in V$ will be a neighbourhood of $x$, and the same will hold for $X^{\circ}$.

Suppose then $f$ of finite type. Then $X^{\circ}$ is locally constructible `(9.7.12)`; it therefore suffices to show
that $X^{\circ}$ contains every generization $x'$ of $x$ $(0_{III}, 9.2.5)$. Set $y' = f(x')$; there exists a discrete
valuation ring $A$ and a morphism $u$ of $Y' = \operatorname{Spec}(A)$ into $X$ such that, if $z$ is the closed point
and $z'$ the generic point of $Y'$, one has $u(z) = x$ and $u(z') = x'$ `(II, 7.1.9)`; if $h = f \circ u$, one therefore
has $h(z) = y$ and $h(z') = y'$. Set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, which is a morphism of finite
type universally open at the points of $f'^{-1}(z)$, and $g' = g_{(Y')}$, which is a $Y'$-section of $X'$. If $p_{y} :
f'^{-1}(z) \to f^{-1}(y)$ (resp. $p_{y'} : f'^{-1}(z') \to f^{-1}(y')$) is the canonical projection,
$p^{-1}_{y}(X^{\circ}_{y})$ (resp. $p^{-1}_{y'}(X^{\circ}_{y'})$) is the connected component of $f'^{-1}(z)$ (resp.
$f'^{-1}(z')$) containing `g'(z)` (resp. `g'(z')`), for the $X^{\circ}_{z}$ are geometrically connected `(4.5.13)` and
it suffices to apply `(4.4.1)`. Moreover, the morphism $u$ corresponds to a $Y'$-section $v$ of $X'$ such that
$p_{y}(v(y)) = x$, $p_{y'}(v(y')) = x'$, so that $v(y')$ is a generization of $v(y)$, and it will therefore suffice to
prove that $v(y')$ belongs to $p^{-1}_{y'}(X^{\circ}_{y'})$. Finally, it is clear that $p^{-1}_{y}(X^{\circ}_{y})$ is
geometrically reduced over $k(z)$.

In other words, one is reduced to the case where $Y$ is the spectrum of a discrete valuation ring, $y$ its closed point,
$y'$ its generic point. As $f^{-1}(y) - X^{\circ}_{y}$ is then closed in $X$, one may, replacing $X$ by the open set
$X - (f^{-1}(y) - X^{\circ}_{y})$, suppose that $X^{\circ}_{y} = f^{-1}(y)$; in the same way, one may replace $X$ by the
open set, connected component of $X$, which contains $g(Y)$, this connected component evidently containing $X^{\circ}$;
in other words, one may suppose $X$ connected. The proposition will then be established if one shows that
$X^{\circ} = X$, or again that $X^{\circ}_{y'}$ is connected; but $f^{-1}(y')$ is geometrically reduced over $k(y')$,
and *a fortiori* reduced; as moreover $f$ is open at the points of $f^{-1}(y)$, one may apply the lemma `(15.5.6)`,
whence the conclusion.

**Corollary (15.6.5).**

<!-- label: IV.15.6.5 -->

*Let $f : X \to Y$ be a flat morphism of finite presentation, $g$ a $Y$-section of $X$; for every $y \in Y$, let
$X^{\circ}_{y}$ be the connected component of $f^{-1}(y)$ containing $g(y)$, and let $X^{\circ}$ be the union of the
$X^{\circ}_{y}$ as $y$ runs over $Y$. Then, for every $y \in Y$ such that $X^{\circ}_{y}$ be geometrically reduced over
$k(y)$, $X^{\circ}$ is a neighbourhood of $X^{\circ}_{y}$ in $X$. In particular, if $f$ is reduced `(6.8.1)`,
$X^{\circ}$ is open in $X$.*

The question being local on $Y$, one may suppose $Y = \operatorname{Spec}(A)$ affine. There exists therefore a
Noetherian subring `A_0` and a flat morphism of finite type $f_{0} : X_{0} \to Y_{0} = \operatorname{Spec}(A_{0})$ such
that $X = X_{0} \times_{Y_{0}} Y$ and $f = (f_{0})_{(Y)}$ (`(8.9.1)` and `(11.2.7)`); moreover, one may suppose that
there exists a `Y_0`-section $g_{0}$ of `X_0` such that $g = (g_{0})_{(Y)}$ `(8.8.2)`. For every $y \in Y$, let $y_{0}$
be its projection in `Y_0`; it follows from `(4.5.13)` that $(X_{0})^{\circ}_{y_{0}}$ is geometrically connected, hence,
if $p : f^{-1}(y) \to f^{-1}_{0}(y_{0})$ is the canonical projection, one has $X^{\circ}_{y} =
p^{-1}((X_{0})^{\circ}_{y_{0}})$ `(4.4.1)`; in addition, the hypothesis that $X^{\circ}_{y}$ is geometrically reduced
over $k(y)$ entails that $(X_{0})^{\circ}_{y_{0}}$ is geometrically reduced over $k(y_{0})$ `(4.6.10)`. One is thus
reduced to the case where one supposes

<!-- original page 237 -->

in addition $Y$ Noetherian; as $f$ is universally open `(11.1.1)`, it then suffices to apply `(15.6.4)`.

**Proposition (15.6.6).**

<!-- label: IV.15.6.6 -->

*Let $f : X \to Y$ be a morphism such that $Y$ be locally Noetherian and $f$ locally of finite type, or that $f$ be of
finite presentation. Let $g$ be a $Y$-section of $X$; for every $y \in Y$, let $X^{\circ}_{y}$ be the connected
component of $f^{-1}(y)$ containing $g(y)$; finally, let $X^{\circ}$ be the union of the $X^{\circ}_{y}$ as $y$ runs
over $Y$.*

*Suppose that, for every $y \in Y$, $X^{\circ}_{y}$ is geometrically irreducible. Then:*

*(i) The function $y \mapsto \dim(X^{\circ}_{y})$ is upper semi-continuous in $Y$.*

*(ii) Let $x_{0} \in X^{\circ}$, $y_{0} = f(x_{0})$. If the function $y \mapsto \dim(X^{\circ}_{y})$ is constant in a
neighbourhood of $y_{0}$, there exists an open neighbourhood $U$ of $y_{0}$ such that $f$ be universally open at the
points of $X^{\circ} \cap f^{-1}(U)$. If moreover $Y$ is reduced and $f^{-1}(y_{0})$ geometrically reduced over
$k(y_{0})$ at the point $x_{0}$, $f$ is flat at the point $x_{0}$.*

*(iii) Conversely, suppose that $f$ is universally open at the generic point of $X^{\circ}_{y_{0}}$ and moreover that
one of the following conditions is verified:*

*α) The fibre $f^{-1}(y_{0})$ is geometrically reduced over $k(y_{0})$ at the point $g(y_{0})$ and the ring
$\mathcal{O}_{Y, y_{0}}$ is Noetherian.*

*β) For every generic point $y'$ of an irreducible component of $Y$ containing $y_{0}$, one has*

$$ \dim(X^{\circ}_{y'}) \geq \dim(X^{\circ}_{y_{0}}). $$

*Then the function $y \mapsto \dim(X^{\circ}_{y})$ is constant in a neighbourhood of $y_{0}$.*

*(iv) The set $W$ of points $x \in X^{\circ}$ such that the function $y \mapsto \dim(X^{\circ}_{y})$ be constant in a
neighbourhood of $f(x)$ and that $X^{\circ}_{f(x)}$ be geometrically reduced over $k(f(x))$, is open in $X$.*

The questions being local on $Y$, one may suppose that $Y = \operatorname{Spec}(A)$ is affine. When $f$ is of finite
presentation, there exists therefore a Noetherian subring `A_1` of $A$ and a morphism of finite type $f_{1} : X_{1} \to
Y_{1} = \operatorname{Spec}(A_{1})$ such that $X = X_{1} \times_{Y_{1}} Y$ and $f = (f_{1})_{(Y)}$ `(8.9.1)`; moreover,
one may suppose that there exists a `Y_1`-section $g_{1}$ of `X_1` such that $g = (g_{1})_{(Y)}$ `(8.8.2)`. For every $y
\in Y$, let $y_{1}$ be its projection in `Y_1`; it follows from `(4.5.13)` that $(X_{1})^{\circ}_{y_{1}}$ is
geometrically connected, hence, if $p : f^{-1}(y) \to f^{-1}_{1}(y_{1})$ is the canonical projection, one has
$X^{\circ}_{y} = p^{-1}((X_{1})^{\circ}_{y_{1}})$ `(4.4.1)`. Note on the other hand that one may, by virtue of
`(9.7.11)` and `(9.7.12)`, apply `(9.3.3)` to the property of being geometrically irreducible; one may therefore suppose
`A_1` chosen so that $(X_{1})^{\circ}_{y_{1}}$ be geometrically irreducible for every $y_{1} \in Y_{1}$. One has
$\dim(X^{\circ}_{y}) = \dim((X_{1})^{\circ}_{y_{1}})$ `(4.1.4)`, and by applying again `(9.3.3)` to the property of
having a given dimension (and using `(9.5.5)` and `(9.7.12)`), one may suppose (restricting if necessary $Y$ to a
neighbourhood of $y_{0}$) that if $\dim(X^{\circ}_{y})$ is constant in $Y$, then $\dim((X_{1})^{\circ}_{y_{1}})$ is
constant in `Y_1`. If $Y$ is reduced, the same holds for `Y_1` since $A_{1} \subset A$; on the other hand, if
$f^{-1}(y_{0})$ is geometrically reduced at the point $x_{0}$, $f^{-1}_{1}(y_{01})$ is so at the point $x_{01}$
($x_{01}$ and $y_{01}$ being the respective projections in `X_1` and `Y_1` of $x_{0}$ and $y_{0}$) `(4.6.10)`.

These remarks show that to demonstrate (i) and (ii), one may restrict to the case where $Y$ is Noetherian and $f$
locally of finite type. But in this case, the assertion (i) follows from `(15.6.2)` and the first assertion of (ii) from
`(15.6.3)`. On the other hand, if $Y$ is reduced and $f^{-1}(y_{0})$ geometrically reduced over $k(y_{0})$ at the point
$x_{0}$ ($Y$ being always supposed

<!-- original page 238 -->

Noetherian), as $X^{\circ}_{y}$ is the only irreducible component of $f^{-1}(y)$ containing $x_{0}$, one deduces from
`(15.6.3)` and `(15.2.3)` that if $\dim(X^{\circ}_{y})$ is constant in a neighbourhood of $y_{0}$, $f$ is flat at the
point $x_{0}$.

To prove (iii), let us first remark that the set $X^{\circ}$ is locally constructible in $X$ `(9.7.12)`, hence, by
`(9.5.5)`, the set $E$ of $y \in Y$ such that $\dim(X^{\circ}_{y}) = \dim(X^{\circ}_{y_{0}})$ is locally constructible
in $Y$. Let us then apply `(1.10.1)` to $E$: it suffices to prove (taking (i) into account) that $\dim(X^{\circ}_{y'}) =
\dim(X^{\circ}_{y_{0}})$ for the generic point $y'$ of an irreducible component of $Y$ containing $y_{0}$; this already
allows us to suppose that $Y = \operatorname{Spec}(\mathcal{O}_{Y, y_{0}})$.

If one is in case α), one reduces at once, by virtue of `(II, 7.1.9)`, and using `(4.5.13)` and `(4.4.1)` as in
`(15.6.4)`, to the case where $Y$ is the spectrum of a discrete valuation ring, $y_{0}$ its closed point and $y'$ its
generic point. But then the hypotheses entail, by virtue of `(15.2.2.1)`, that $f$ is flat at the point $g(y_{0})$,
hence also in a neighbourhood $V$ of this point in $X$ `(11.1.1)`. To demonstrate our assertion, one may replace $X$ by
$V$, for $V \cap X^{\circ}_{y'}$ is not empty by virtue of `(2.3.4)`, hence is an everywhere dense open set in
$X^{\circ}_{y'}$, and consequently has the same dimension `(4.1.1.3)`; moreover, as $X^{\circ}_{y'}$ is also the
connected component of $f^{-1}(y')$ containing $g(y')$, one may suppose $V$ chosen such that $V$ meets no other
irreducible component of $f^{-1}(y_{0})$ nor of $f^{-1}(y')$, in other words one may suppose that $X^{\circ}_{y} = X$;
but then the conclusion follows from `(12.1.1, (i))`, since by hypothesis $X^{\circ}_{y_{0}}$ is integral.

Suppose now that one is in case β). Let us apply this time `(II, 7.1.4)` in the same way as `(II, 7.1.9)` in case α):
one is then reduced to the case where $Y$ is the spectrum of a valuation ring (not necessarily discrete), $y_{0}$ its
closed point and $y'$ its generic point. By virtue of `(14.3.13)`, there exists an irreducible component $Z$ of $X$
containing $X^{\circ}_{y_{0}}$ and dominating $Y$, and such that $\dim(Z \cap f^{-1}(y')) = \dim(X^{\circ}_{y_{0}})$;
but hypothesis β) and the fact that $\dim(Z \cap f^{-1}(y_{0})) \leq \dim(f^{-1}(y_{0}))$ show that
$\dim(X^{\circ}_{y_{0}}) \leq \dim(X^{\circ}_{y'})$, whence $\dim(X^{\circ}_{y_{0}}) = \dim(X^{\circ}_{y'})$ by virtue
of (i).

It remains to prove (iv). Note first that the sets envisaged do not change when one replaces $f$ by
`f_{(Y_red)} : X ×_Y Y_red → Y_red`, the projection $X \times_{Y} Y_{red} \to X$ being a homeomorphism. In other words,
one may suppose $Y$ reduced, and then it follows from (ii) that $f$ is flat at the points of $W$. Consider a point
$x_{0}$ of $W$ and let us prove that $W$ is a neighbourhood of $x_{0}$; proceeding as at the beginning of the
demonstration, and using also `(11.2.7)`, one may in addition suppose $Y$ Noetherian; it then follows from (ii) and from
`(15.6.4)` that $X^{\circ}$ is a neighbourhood of $x_{0}$ in $X$, and from `(12.1.1, (vii))` that $W$ is also a
neighbourhood of $x_{0}$ in $X$.

**Corollary (15.6.7).**

<!-- label: IV.15.6.7 -->

*Suppose the preliminary conditions of `(15.6.6)` on $f$ verified, and suppose in addition that for every $y \in Y$,
$X^{\circ}_{y}$ is geometrically integral over $k(y)$. Then the following conditions are equivalent:*

*a) The function $y \mapsto \dim(X^{\circ}_{y})$ is locally constant in $Y$.*

*b) The morphism `f_{(Y_red)} : X ×_Y Y_red → Y_red` deduced from $f$ by base change, is flat at the points of
$X^{\circ}$.*

<!-- original page 239 -->

*Moreover, these conditions entail that $X^{\circ}$ is open in $X$. Finally, when $Y$ is locally Noetherian, a) and b)
are also equivalent to*

*b') $f$ is universally open at the points of $X^{\circ}$.*

The fact that a) entails b) follows from `(15.6.6, (ii))`, as well as the fact that $X^{\circ}$ is then open in $X$. If
b) is verified, one may restrict to the case where $Y$ is reduced and $f$ flat; then, one reduces, as at the beginning
of `(15.6.6)`, and using in addition `(11.2.7)`, to the case where $Y$ is Noetherian, a case where the conclusion
follows from `(15.6.6, (iii), case α))`. The equivalence of b) and b') has already been proved when $Y$ is locally
Noetherian `(15.2.2.1)`, taking into account that the morphism $X \times_{Y} Y_{red} \to X$ is a universal
homeomorphism.

**Proposition (15.6.8).**

<!-- label: IV.15.6.8 -->

*Let $f : X \to Y$ be a separated morphism of finite presentation, $g$ a $Y$-section of $X$; for every $y \in Y$, let
$X^{\circ}_{y}$ be the connected component of $f^{-1}(y)$ that contains $g(y)$, and let $X^{\circ}$ be the union of the
$X^{\circ}_{y}$ as $y$ runs over $Y$. Then, if $y \in Y$ is such that $X^{\circ}_{y}$ be proper over $k(y)$, $X^{\circ}$
is proper over $Y$ at the point $y$ (i.e. `(15.7.1)`, there exists an open neighbourhood $U$ of $y$ in $Y$ such that
$X^{\circ} \cap f^{-1}(U)$ be closed in $f^{-1}(U)$ and proper over $U$).*

Proceeding as at the beginning of `(15.6.6)` (where one uses `(8.10.5, (v))`, and where one replaces `(9.7.11)` by
`(9.6.7)`), one reduces to the case where $Y$ is Noetherian and $f$ of finite type. One then knows `(9.7.12)` that
$X^{\circ}$ is locally constructible in $X$; on the other hand, the $X^{\circ}_{z}$ are geometrically connected (for
every $z \in Y$) by virtue of `(4.5.13)`; finally, as $g(Y) \subset X^{\circ}$, $X^{\circ}$ is universally submersive
over $Y$ `(15.7.8)`. It then suffices to apply to $X^{\circ}$ the criterion `(15.7.9)`.

**Corollary (15.6.9).**

<!-- label: IV.15.6.9 -->

*Let $f : X \to Y$ be a separated morphism such that $Y$ be locally Noetherian and $f$ locally of finite type, or that
$f$ be of finite presentation. Let $g$ be a $Y$-section of $X$, and for every $y \in Y$, let $X^{\circ}_{y}$ be the
connected component of $f^{-1}(y)$ containing $g(y)$. Let $y$ be a point of $Y$ such that $X^{\circ}_{y}$ be proper over
$k(y)$. Then, for every generization $y'$ of $y$, one has $\dim(X^{\circ}_{y'}) \leq \dim(X^{\circ}_{y})$.*

Suppose first $f$ of finite presentation; then by replacing if necessary $Y$ by a neighbourhood of $y$, one may suppose
that $f | X^{\circ}$ is proper `(15.6.8)`, and it suffices to apply `(13.1.5)` to this restriction. If $Y$ is locally
Noetherian and $f$ locally of finite type, $X$ is locally Noetherian; moreover the hypothesis that $X^{\circ}_{y}$ is
proper over $k(y)$ entails that $X^{\circ}_{y}$ is Noetherian; there exists therefore a Noetherian open set $V \subset
X$ containing $X^{\circ}_{y}$; consequently there is an open neighbourhood $W$ of $y$ in $Y$ such that $g(W) \subset V$.
Moreover, if $z$ is a maximal point of $X^{\circ}_{y'}$, one may suppose that $z \in V$. The restriction of $f$ to $V
\cap f^{-1}(W)$ is then a morphism of finite type, and $g | W$ a $W$-section; by applying to this morphism the result
already obtained, one sees that if $Z$ is the irreducible component of $X^{\circ}_{y'}$ of generic point $z$, one has
$\dim(Z) \leq \dim(X^{\circ}_{y})$. As $z$ is any maximal point of $X^{\circ}_{y'}$, one has indeed
$\dim(X^{\circ}_{y'}) \leq \dim(X^{\circ}_{y})$.

**Remarks (15.6.10).**

<!-- label: IV.15.6.10 -->

*(i)* The additional hypothesis on the existence of an irreducible component of $X^{\circ}_{y'}$ containing $g(y')$ and
of dimension equal to $\dim(X^{\circ}_{y'})$, made in `(15.6.1)`, is not superfluous, as is shown by the following
example. Let $A$ be a discrete valuation ring, $\pi$ a uniformizer of $A$, $K$ the fraction field of $A$, $k$ its
residue field. Take $Y = \operatorname{Spec}(A)$, and designate by $y$ and $y'$ the closed point and the generic point
of $Y$. Consider the two following $Y$-schemes: $X_{1} = \operatorname{Spec}(A[t])$, $X_{2} = \operatorname{Spec}(K[u,
v])$, where $t$, $u$, $v$ are indeterminates

<!-- original page 240 -->

(one will note that the projection of `X_2` into $Y$ is therefore `{y'}`). In the ring `A[t]`, the principal ideal $(\pi
t - 1)$ is maximal, and therefore corresponds to a closed point $x_{1}$ of `X_1`, which projects to the generic point
$y'$ of $Y$ and is such that $k(x_{1}) = K$. Consider on the other hand the closed point $x_{2}$ of `X_2` corresponding
to the maximal ideal $(u) + (v)$ of `K[u, v]`; one has also $k(x_{2}) = K$. As one will see in chap. V, one may
therefore glue `X_1` and `X_2` along the two closed subpreschemes `Z_1`, `Z_2` of `X_1`, `X_2` having respectively
${x_{1}}$ and ${x_{2}}$ as underlying spaces, following the unique $Y$-isomorphism of `Z_1` onto `Z_2`. Designate by $X$
the $Y$-prescheme thus obtained, by $x$ the point of $X$ image of $x_{1}$ and $x_{2}$. The "zero section" $g$ of `X_1`
`(II, 1.7.9)` is then again a $Y$-section of $X$; $f^{-1}(y)$ is equal to $(X_{1})_{y}$, while $f^{-1}(y')$ has two
irreducible components, respectively isomorphic to $(X_{1})_{y'}$ and $(X_{2})_{y'}$, having a unique common point $x$,
and of respective dimensions `1` and `2`. See however prop. `(15.6.9)`.

*(ii)* Consider the morphism $f$ defined in `(12.2.3, (ii))`, which is proper and flat; moreover, the restriction of $f$
to $X_{1} \cap f^{-1}_{0}(Y)$ is an isomorphism, hence the inverse morphism $g : Y \to X$ is a $Y$-section of $X$. One
then has $\dim(X^{\circ}_{y_{0}}) = 1$ while $\dim(X^{\circ}_{y}) = 0$ for $y \neq y_{0}$, although $X^{\circ}_{y}$ is
geometrically irreducible for every $y \in Y$ (but $X^{\circ}_{y_{0}}$ is not reduced); one sees therefore that in
`(15.6.6, (iii))`, one cannot suppress the hypotheses α) and β). Moreover, $X^{\circ}$ is not a neighbourhood of
$X^{\circ}_{y_{0}}$, which proves that in `(15.6.4)`, one cannot dispense with the hypothesis that $X^{\circ}_{y}$ is
reduced.

*(iii)* In chap. VI, we shall apply the preceding results to the $Y$-preschemes in groups locally of finite type over a
locally Noetherian prescheme $Y$. If $G$ is such a prescheme, there exists a canonical $Y$-section $g$, the "unit
section", and one shows that $G_{y}$ is always geometrically irreducible and that one has $\dim(G^{\circ}_{y}) =
\dim(G_{y})$, on setting $G_{y} = f^{-1}(y)$. It will therefore follow from `(15.6.2)` and `(15.6.3)` that the function
$z \mapsto \dim(G_{z})$ is upper semi-continuous, and that if it is constant in the neighbourhood of a point $y$, $f$ is
universally open at the points of $G^{\circ}_{y}$. If moreover $G_{y}$ is geometrically reduced over $k(y)$ at one of
its points, one shows that $G_{y}$ is smooth `(6.8.1)` over $k(y)$ at all its points; it will then follow from
`(15.6.6)` that if moreover $\mathcal{O}_{y}$ is reduced, then $f$ is smooth at all the points of $G^{\circ}$ (but not
necessarily at all the points of $G_{y}$). These results will apply for example in the theory of Picard schemes, where
we shall have at our disposal a general theorem assuring that, under certain conditions, the function $z \mapsto
\dim(G_{z})$ is locally constant. Let us remark that it is in view of applications of this nature that the statements
such as `(15.6.1)` are given for morphisms locally of finite type, and not only for morphisms of finite type.

One will also note that in the case of a $Y$-prescheme in groups $G$, hypothesis β) of `(15.6.6)` is always verified.

### 15.7. Appendix: Valuative criteria of local properness

This number gives complements to the valuative criterion of properness demonstrated in `(II, 7.3.10)`; it is independent
of the rest of §15.

**Definition (15.7.1).**

<!-- label: IV.15.7.1 -->

*Let $f : X \to Y$ be a morphism of preschemes, $y$ a point of $Y$. One says that $f$ is **proper at the point $y$** if
there exists an open neighbourhood $U$ of $y$ in $Y$ such that the restriction $f^{-1}(U) \to U$ of $f$ be a proper
morphism. One says that a part $Z$ of $X$ is **proper over $Y$ at the point $y$** if there exists an open neighbourhood
$U$ of $y$ such that $Z \cap f^{-1}(U)$ be closed in $f^{-1}(U)$ and proper over $U$ `(II, 5.4.10)` (which amounts to
saying that for every closed subprescheme of $X$ having $Z$ as underlying space, the restriction $Z \to Y$ of $f$ to $Z$
is proper at the point $y$).*

Let $g : Y' \to Y$ be an arbitrary morphism; set $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$ and, if $p : X' \to X$ is the
canonical projection, $Z' = p^{-1}(Z)$. Then, if $Z$ is proper over $Y$ at the point $y$, $Z'$ is proper over $Y'$ at
every point $y'$ above $y$ `(II, 5.4.2)`.

**Proposition (15.7.2).**

<!-- label: IV.15.7.2 -->

*Let $Y$ be an integral locally Noetherian prescheme, $X$ an integral prescheme, $f : X \to Y$ a separated, dominant
morphism of finite type, $y$ a point of $Y$. The following conditions are equivalent:*

*a) $f$ is proper at the point $y$.*

*b) If $Y_{1} = \operatorname{Spec}(\mathcal{O}_{y})$, $X_{1} = X \times_{Y} Y_{1}$, the morphism $f_{1} = f_{(Y_{1})} :
X_{1} \to Y_{1}$ is proper.*

*c) Every discrete valuation ring having $R(X)$ as fraction field and dominating $\mathcal{O}_{y}$ dominates a local
ring $\mathcal{O}_{x}$ of $X$ (in which case one has necessarily $f(x) = y$).*

<!-- original page 241 -->

The fact that a) implies b) follows from `(II, 5.4.2)`, and the implication b) ⟹ c) follows from `(II, 7.3.10)`. There
remains therefore to show that c) entails a). The question being local on $Y$, one may suppose $Y$ affine, hence
Noetherian. By virtue of Chow's lemma `(II, 5.6.1)`, there exists an integral prescheme $X'$, a projective morphism $p :
P \to Y$, a dominant open immersion $j : X' \to P$, and a projective and birational (hence surjective) morphism $q : X'
\to X$ such that the diagram

```text
                       j
              P  ←──────────  X'
              │                │
            p │              q │
              ↓                ↓
              Y  ←─────f─────  X
```

is commutative. As $X'$ is integral and $j$ dominant, $P$ is irreducible, and one may, replacing $P$ by $P_{red}$,
suppose $P$ integral `(I, 5.2.2 and II, 5.5.5, (vi))`. Everything comes down to proving that there exists an open
neighbourhood $U$ of $y$ such that $p^{-1}(U) \subset j(X')$, for then the restriction of $j$ to $j^{-1}(p^{-1}(U)) =
q^{-1}(f^{-1}(U)) = V$ will be an isomorphism onto $p^{-1}(U)$, hence the restriction $V \to U$ of $p \circ q$ will be
proper, and as the restriction $V \to f^{-1}(U)$ of $q$ is surjective, the restriction $f^{-1}(U) \to U$ will be proper
`(II, 5.4.3)`. As $T = P - j(X')$ is closed in $P$, $p(T)$ is closed in $Y$, and it suffices to show that $y \notin
p(T)$, or again that every $z' \in P$ such that $p(z') = y$ belongs to $j(X')$. Now, the field of rational functions
$R(P)$ is equal to $R(X')$, hence to $R(X)$ by construction; as one may restrict to the case where $z'$ is not the
generic point of $P$, there exists a discrete valuation ring $A$ having $R(X)$ as fraction field and dominating
$\mathcal{O}_{z'}$ `(II, 7.1.7)`; as $p(z') = y$, $A$ dominates also $\mathcal{O}_{y}$, hence by hypothesis there exists
$x \in X$ such that $f(x) = y$ and that $A$ dominates $\mathcal{O}_{x}$. As $q$ is proper, there exists $x' \in X'$ such
that $q(x') = x$ and that $A$ dominates $\mathcal{O}_{x'}$ `(II, 7.3.10)`; hence $z'$ and $j(x')$ are two points of $P$
whose local rings $\mathcal{O}_{z'}$ and $\mathcal{O}_{j(x')} = \mathcal{O}_{x'}$ are related `(I, 8.1.4)`; as $P$ is a
scheme, this entails $z' = j(x')$ `(I, 8.2.2)`, which finishes the demonstration.

**Remark (15.7.3).**

<!-- label: IV.15.7.3 -->

One may in `(15.7.2)` suppress the hypothesis that $Y$ is locally Noetherian, by replacing in condition c) the discrete
valuation rings by arbitrary valuation rings; the demonstration is then unchanged, taking `(II, 7.3.10)` into account.

**Corollary (15.7.4).**

<!-- label: IV.15.7.4 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a separated morphism of finite type, $Z$ a part of $X$ such that the
maximal points of its closure $\overline{Z}$ belong to $Z$ (which is the case when $Z$ is finite, or when $Z$ is
constructible $(0_{III}, 9.2.2)$). Let $y$ be a point of $Y$. The following conditions are equivalent:*

*a) The set $Z$ is proper over $Y$ at the point $y$.*

*b) If $Y_{1} = \operatorname{Spec}(\mathcal{O}_{y})$, $X_{1} = X \times_{Y} Y_{1}$, and if $g_{1} : X_{1} \to X$ is the
canonical projection and $Z_{1} = g^{-1}_{1}(Z)$, the closure $\overline{Z}_{1}$ of `Z_1` in `X_1` is proper over
`Y_1`.*

\*c) For every scheme $Y' = \operatorname{Spec}(A')$, where $A'$ is a discrete valuation ring, and every morphism $g :
Y' \to Y$, such that the image $g(y')$ of the closed point $y'$ of $Y'$ be $y$, one has the following property: setting
$X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, $g' = g_{(Y')} : X' \to X$, $Z' = g'^{-1}(Z)$, and designating by
$\eta'$

<!-- original page 242 -->

the generic point of $Y'$, then, for every point $x' \in \overline{Z'} \cap f'^{-1}(\eta')$ rational over $k(\eta')$,
there exists a $Y'$-section of $X'$ containing $x'$.\*

The fact that a) entails b) follows from the fact that $Z_{1} \subset g^{-1}_{1}(Z)$ and that $g^{-1}_{1}(Z)$ is proper
over `Y_1` `(15.7.1)`. The fact that b) entails c) follows from `(II, 7.3.3)`. There remains therefore to see that c)
implies a). It suffices evidently to prove that every irreducible component of $\overline{Z}$ is proper over $Y$ at the
point $y$, and the hypothesis therefore allows us to restrict to the case where $Z$ is reduced to a single point $z$.
One may evidently also, taking into account `(I, 5.2.2)` and `(II, 5.4.6)`, suppose that $X$ and $Y$ are reduced, then
(by definition of a proper part `(II, 5.4.10)`) suppose that $Z = X = {z}$ and (applying again `(I, 5.2.2)`) that $f$ is
dominant, hence $X$ and $Y$ integral and Noetherian; it must then be proved that $f$ is proper at the point $y$ of $Y$.
Let us show for this that $f$ verifies condition c) of `(15.7.2)`. Let $A'$ be a discrete valuation ring having $R(X) =
k(z)$ as fraction field and dominating $\mathcal{O}_{y}$; with the notation of c), one has therefore $g(y') = y$, and
$g(\eta')$ is the generic point $\eta = f(z)$ of $Y$. As by definition $k(\eta') = k(z)$, there exists a
$k(\eta')$-morphism $\operatorname{Spec}(k(\eta')) \to \operatorname{Spec}(k(z))$ taking $\eta'$ to $z$, hence a
$k(\eta')$-section of $f'^{-1}(\eta')$ `(I, 3.3.14)`; if $z'$ is the image of $\eta'$ by this section, $z'$ is therefore
rational over $k(\eta')$ and $g'(z') = z$. One therefore concludes from hypothesis c) that there exists a $Y'$-section
$h'$ of $X'$ such that $h'(\eta') = z'$; let $h = g' \circ h' : Y' \to X$ be the corresponding $Y$-morphism, and let $x
= h(y')$; it is clear that $f(x) = y$ and that $A' = \mathcal{O}_{y'}$ dominates $\mathcal{O}_{x}$, which finishes the
demonstration.

**Corollary (15.7.5).**

<!-- label: IV.15.7.5 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a separated morphism of finite type, $y$ a point of $Y$. The
following conditions are equivalent:*

*a) $f$ is proper at the point $y$.*

*b) If $Y_{1} = \operatorname{Spec}(\mathcal{O}_{y})$, $X_{1} = X \times_{Y} Y_{1}$, the morphism $f_{1} = f_{(Y_{1})} :
X_{1} \to Y_{1}$ is proper.*

*c) For every scheme $Y' = \operatorname{Spec}(A')$, where $A'$ is a discrete valuation ring, and every morphism $g : Y'
\to Y$, such that the image $g(y')$ of the closed point $y'$ of $Y'$ be $y$, one has the following property: setting $X'
= X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$ and designating by $\eta'$ the generic point of $Y'$, then, for every
$x' \in f'^{-1}(\eta')$ rational over $k(\eta')$, there exists a $Y'$-section of $X'$ containing $x'$.*

**Corollary (15.7.6).**

<!-- label: IV.15.7.6 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism of finite type. The following conditions are
equivalent:*

*a) There exists a proper morphism $g : X \to Z$ and an immersion $h : Z \to Y$ such that $f = h \circ g$.*

*b) The subspace $f(X)$ is locally closed in $Y$, and if $Z'$ is the subprescheme of $Y$ closed image of $X$ by $f$
`(I, 9.5.3 and 9.5.1)`, and `Z''` the prescheme induced by $Z'$ on the open set $f(X)$ of $Z'$, so that $f$ factors in
unique fashion as $f = j \circ g$ (where $j : Z'' \to Y$ is the canonical injection), then $g : X \to Z''$ is proper.*

*c) For every $y \in f(X)$, $f$ is proper at the point $y$.*

*d) For every scheme $Y' = \operatorname{Spec}(A')$, where $A'$ is a discrete valuation ring, and every morphism $g : Y'
\to Y$ such that $g(Y') \subset f(X)$, every rational $Y'$-section `(I, 7.1.2)` of $X' = X \times_{Y} Y'$ extends in a
unique way to a $Y'$-section of $X'$.*

It is clear that b) entails a). To see that a) entails c), let us first remark that a) entails that $h(Z)$ is locally
closed in $Y$ and $g(X)$ closed in $Z$, hence $f(X)$ is locally closed in $Y$; for every $y \in f(X)$, there is
therefore an open neighbourhood $U$

<!-- original page 243 -->

of $y$ in $Y$ such that $f(X) \cap U$ be closed in $U$; then the restriction $h^{-1}(U) \to U$ of $h$ is a closed
immersion, and the restriction $f^{-1}(U) = g^{-1}(h^{-1}(U)) \to h^{-1}(U)$ of $g$ is proper, hence the restriction
$f^{-1}(U) \to U$ of $f$ is proper `(II, 5.4.2)`. To see that c) entails b), note first that, for every $y \in f(X)$,
there exists, by virtue of c), an open neighbourhood $U$ of $y$ in $Y$ such that $f(X) \cap U$ be closed in $U$, hence
$f(X)$ is locally closed, and consequently open in its closure. As this latter is the underlying space of $Z'$, and as
$f$ factors as $f = j_{0} \circ g_{0}$, where $j_{0} : Z' \to Y$ is the canonical injection and $g_{0}$ is a morphism of
$X$ into $Z'$, the fact that $g_{0}(X) = Z''$ (which is open in $Z'$) entails the factorization of the statement of b);
the fact that $g$ is proper then follows from the local character (over `Z''`) of this property, and from `(II, 5.4.3)`.
It is clear that c) implies d) by virtue of `(15.7.5)`, the uniqueness of the extension of a rational $Y'$-section
following from the hypothesis that $f$ is separated `(I, 7.2.2)`. Let us finally prove that d) entails c); in the first
place, it follows from d), taking `(II, 7.2.3 and 7.2.4)` into account, that $f$ is separated; one may then apply the
criterion `(15.7.5, c))`, which shows that $f$ is proper at every point of $f(X)$.

**Remarks (15.7.7).**

<!-- label: IV.15.7.7 -->

*(i)* In `(15.7.4, c))`, `(15.7.5, c))` and `(15.7.6, d))`, one may restrict to the case where the discrete valuation
ring $A'$ is complete and admits an algebraically closed residue field. Indeed, in the demonstration of `(15.7.4)`, if
one considers a complete discrete valuation ring `A''` dominating $A'$ and having an algebraically closed residue field
$(0_{III}, 10.3.1)$, hypothesis c) is then verified for $Y'' = \operatorname{Spec}(A'')$, $X'' = X \times_{Y} Y''$ and
$f'' = f_{(Y'')}$; but $X'' = X' \times_{Y'} Y''$, and it follows then from the remark `(II, 7.3.9, (i))` that $f'$ is
proper; consequently $Y'$, $X'$ and $f'$ also verify hypothesis c) `(II, 7.3.8)`.

*(ii)* Taking `(II, 7.3.8)` into account, condition c) of `(15.7.5)` can be replaced by the condition that $f'$ is
proper.

**(15.7.8)**

<!-- label: IV.15.7.8 -->

One says that a morphism of preschemes $f : X \to Y$ is **submersive** if it is surjective and if the topology of $Y$ is
equal to the quotient of the topology of $X$ by the equivalence relation defined by $f$. One says that $f$ is
**universally submersive** if for every base change $Y' \to Y$, the morphism $f' = f_{(Y')} : X \times_{Y} Y' \to Y'$ is
submersive. Every surjective universally open, or universally closed, or faithfully flat and quasi-compact morphism is
universally submersive `(2.3.12)`. Given a morphism $f : X \to Y$, one says that a subset $Z$ of $X$ is submersive over
$f(Z)$ if the topology of the subspace $f(Z)$ of $Y$ is quotient of the topology of the subspace $Z$ of $X$ by the
equivalence relation defined by $f | Z$. One says that $Z$ is universally submersive over $f(Z)$ if, for every base
change $g : Y' \to Y$, the inverse image $Z' = p^{-1}(Z)$ of $Z$ under the projection $p : X \times_{Y} Y' \to Y'$ is a
submersive set over $f'(Z') = g^{-1}(f(Z))$. One will note that if the morphism $f$ admits a $Y$-section $h : Y \to X$,
every set $Z$ containing $h(Y)$ is universally submersive over $Y$.

**Proposition (15.7.9).**

<!-- label: IV.15.7.9 -->

*Let $Y$ be a locally Noetherian prescheme, $y$ a point of $Y$, $f : X \to Y$ a separated morphism of finite type. Let
$Z$ be a locally constructible part of $X$ having the following properties:*

*(i) For every generization $y'$ of $y$, $Z_{y'} = Z \cap f^{-1}(y')$ is a connected component of $f^{-1}(y')$ and is
geometrically connected over $k(y')$ `(4.5.2)`.*

<!-- original page 244 -->

*(ii) $Z_{y}$ is proper over $\operatorname{Spec}(k(y))$.*

*(iii) $Z$ is universally submersive over $f(Z)$ `(15.7.8)`.*

*Then $Z$ is proper over $Y$ at the point $y$ (in other words `(15.7.1)`, there exists an open neighbourhood $U$ of $y$
such that $Z \cap f^{-1}(U)$ be closed in $f^{-1}(U)$ and proper over $U$).*

Using the method of `(8.1.2, a))` and `(8.10.5, (xii))`, one is reduced to proving that when $Y =
\operatorname{Spec}(A)$ is the spectrum of a Noetherian local ring, hypotheses (i), (ii) and (iii) entail that $Z$ is
proper over $Y$.

Note first that if $A'$ is a Noetherian local ring, $\phi : A \to A'$ a local homomorphism, $Y' =
\operatorname{Spec}(A')$ and $g : Y' \to Y$ the morphism corresponding to $\phi$, the inverse image $Z'$ of $Z$ by the
canonical projection $p : X \times_{Y} Y' \to X$ has, with respect to $Y'$, the properties (i), (ii), (iii) of the
statement, taking `(1.8.2)` into account; using `(2.7.1, (vii))`, it amounts to the same to demonstrate that $Z'$ is
proper over $Y'$, provided that $A'$ be a faithfully flat $A$-module. We shall use this remark by taking $A' =
\overline{A}$ $(0_{I}, 7.3.5)$, in other words we may restrict to the case where $A$ is complete. As $Z_{y}$ is a
connected component of $f^{-1}(y)$, proper over $k(y)$, it follows from `(III, 5.5.2)` that $X$ is a sum of two
subpreschemes `X_0`, `X_1` induced on open and closed parts of $X$, such that `X_0` be proper over $Y$ and that $X_{0}
\cap f^{-1}(y) = Z_{y}$. Set $Z_{0} = X_{0} \cap Z$, $Z_{1} = X_{1} \cap Z$, so that these sets form a partition of $Z$
into two parts open and closed in $Z$. As the $Z_{y'}$ are connected, one necessarily has $Z_{y'} \subset Z_{0}$ or
$Z_{y'} \subset Z_{1}$, hence $f(Z_{0}) \cap f(Z_{1}) = \emptyset$. But as `Z_0` and `Z_1` are saturated for the
equivalence relation defined by $f | Z$, it follows from (iii) that $f(Z_{0})$ and $f(Z_{1})$ are open in $f(Z)$. But
$f(Z_{0})$ contains $y$, and every neighbourhood of $y$ in $Y$ is equal to $Y$, hence $f(Z_{0}) = f(Z)$, and
consequently $f(Z_{1}) = \emptyset$, hence $Z_{1} = \emptyset$ and $Z \subset X_{0}$.

One may therefore now suppose in addition that $f$ is proper, and there remains to prove that $Z$ is closed in $X$. In
other words, it will suffice to prove that a constructible part $Z$ of a prescheme $X$ proper over $Y$ that satisfies
the two sole conditions (i) and (iii), is closed in $X$. By virtue of $(0_{III}, 9.2.5)$, it therefore suffices to prove
that for every $x' \in Z$ and every specialization $x$ of $x'$ in $X$, one has $x \in Z$. Let `A_1` be a complete
discrete valuation ring, $u$ a morphism of $Y_{1} = \operatorname{Spec}(A_{1})$ into $X$ such that, if $y_{1}$ and
$y'_{1}$ are the closed point and the generic point of `Y_1`, one has $u(y_{1}) = x$, $u(y'_{1}) = x'$ `(II, 7.1.7)`;
set $g = f \circ u : Y_{1} \to Y$ and $X_{1} = X \times_{Y} Y_{1}$; there exists a `Y_1`-section $u_{1} : Y_{1} \to
X_{1}$ of $f_{1} = f_{(Y_{1})}$ such that $u = p \circ u_{1}$, where $p : X_{1} \to X$ is the canonical projection. If
$x_{1} = u_{1}(y_{1})$, $x'_{1} = u_{1}(y'_{1})$, one has therefore $p(x_{1}) = x$ and $p(x'_{1}) = x'$, and $x_{1}$ is
a specialization of $x'_{1}$. Moreover, one has $x'_{1} \in Z_{1} = p^{-1}(Z)$; as we have remarked that conditions (i)
and (iii) are stable under every base change, as well as the property of being constructible, one sees that one is
reduced to the following situation: $Y$ is the spectrum of a complete discrete valuation ring, $X$ is proper over $Y$,
$f(x) = y$ is the closed point of $Y$, $y' = f(x')$ its generic point, there exists a $Y$-section $h$ of $X$ such that
$h(y) = x$, $h(y') = x'$, and finally one has $x' \in Z$; it must be proved that $x \in Z$. Now, $Z_{y}$ is a connected
component of $f^{-1}(y)$, proper over $\operatorname{Spec}(k(y))$ since $X$ is proper over $Y$. Applying again
`(III, 5.5.2)`, one sees as above that there is an open and closed part $X'$ of $X$ such that $X' \cap f^{-1}(y) =
Z_{y}$; as $Z_{y}$ is connected,

<!-- original page 245 -->

one may suppose $X'$ connected (replacing if necessary $X'$ by that of its connected components containing $Z_{y}$). But
then the same reasoning as at the beginning proves that one necessarily has $Z \subset X'$; as $h(Y)$ is connected and
contains $x'$, it is necessarily contained in $X'$, hence $x = h(y) \in X' \cap f^{-1}(y) = Z_{y}$. Q.E.D.

**Corollary (15.7.10).**

<!-- label: IV.15.7.10 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a separated morphism of finite type, universally submersive
`(15.7.8)` and such that all the fibres $X_{y} = f^{-1}(y)$ be geometrically connected. Then, if $y \in Y$ is such that
$X_{y}$ be proper over $k(y)$, $f$ is proper at the point $y$.*

Taking `(15.7.5)` into account, one is reduced to the case where $Y = \operatorname{Spec}(\mathcal{O}_{y})$ since the
hypotheses are stable under base change. But in this case it suffices to apply `(15.7.9)` to $Z = X$.

**Corollary (15.7.11).**

<!-- label: IV.15.7.11 -->

*Let $f : X \to Y$ be a separated morphism of finite presentation; suppose that there exists a surjective morphism of
finite presentation $g : Y' \to Y$, which is in addition proper or flat, and such that if one sets $X' = X \times_{Y}
Y'$, there exists a $Y'$-section of $X'$ (or again a $Y$-morphism $Y' \to X$ `(I, 3.3.14)`). Suppose finally that the
fibres $X_{y} = f^{-1}(y)$ be geometrically connected. Then the set $U$ of $y \in Y$ such that $X_{y}$ be proper over
$k(y)$ is open in $Y$, and the restriction $f^{-1}(U) \to U$ of $f$ is proper.*

The question being local on $Y$, one may suppose $Y = \operatorname{Spec}(A)$ affine. Applying `(8.9.1)` to $f$ and to
$g$, one sees that there exists a Noetherian subring `A_0` of $A$ and two morphisms of finite type $f_{0} : X_{0} \to
Y_{0} = \operatorname{Spec}(A_{0})$, $g_{0} : Y'_{0} \to Y_{0}$ such that $X = X_{0} \times_{Y_{0}} Y$, $Y' = Y'_{0}
\times_{Y_{0}} Y$, $f = (f_{0})_{(Y)}$ and $g = (g_{0})_{(Y)}$; moreover, using `(8.10.5, (v), (vi) and (xii))` and
`(11.2.7)`, one may suppose $f_{0}$ separated, $g_{0}$ surjective and proper (resp. flat) if $g$ is proper (resp. flat);
using `(8.8.2)`, one may moreover suppose that there exists a $Y'_{0}$-section of `X_0`. On the other hand, using
`(9.7.7)`, one may apply `(9.3.3)` to the property of being geometrically connected, and one may therefore suppose `A_0`
chosen so that the $f^{-1}_{0}(y_{0})$ be geometrically connected for every $y_{0} \in Y_{0}$. Finally, using
`(2.7.1, (vii))`, it amounts to the same to say that $f^{-1}(y)$ is proper over $k(y)$ or that $f^{-1}_{0}(y_{0})$ is
proper over $k(y_{0})$, where $y_{0}$ is the projection of $y$ in `Y_0`. These remarks show that one is reduced to
demonstrating the corollary when $Y$ is Noetherian. Note now the

**Lemma (15.7.11.1).**

<!-- label: IV.15.7.11.1 -->

*Let $f : X \to Y$ be a morphism, $g : Y' \to Y$ a surjective morphism, which is in addition proper or flat and
quasi-compact. Set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. Then, if $f'$ is submersive (resp. universally
submersive), the same holds for $f$.*

One may restrict to the case where $f'$ is submersive. Indeed, suppose the lemma proved in this case, and let us show
that if $f'$ is universally submersive, $f$ is so too. Let then $Y_{1} \to Y$ be any morphism, and set $Y'_{1} = Y'
\times_{Y} Y_{1}$; if $X'_{1} = X' \times_{Y_{1}} Y'_{1}$ and $f'_{1} = (f')_{(Y'_{1})} : X'_{1} \to Y'_{1}$, $f'_{1}$
is submersive by hypothesis; moreover the morphism $g_{1} : Y'_{1} \to Y_{1}$ is surjective, and proper (resp. flat and
quasi-compact) if $g$ is. Hence, if one sets $X_{1} = X \times_{Y} Y_{1}$, $f_{1} = f_{(Y_{1})}$, it follows from the
hypothesis and from the fact that $X'_{1} = X_{1} \times_{Y_{1}} Y'_{1}$, that $f_{1}$ is submersive, hence $f$
universally submersive. Suppose then only that $f'$ be submersive. It is clear first of all that $f$ is surjective. Let
$E$ be a part of $Y$ such that $f^{-1}(E)$ be closed in $X$; then, if $p : X' \to X$ is the canonical projection,

<!-- original page 246 -->

$p^{-1}(f^{-1}(E)) = f'^{-1}(g^{-1}(E))$ is closed in $X'$, hence, since $f'$ is submersive, $g^{-1}(E)$ is closed in
$Y'$; but as $g$ is also universally submersive `(15.7.8)`, $E$ is closed in $Y$, which proves the lemma.

This being so, as there exists by hypothesis a $Y'$-section of $X'$, $f'$ is universally submersive `(15.7.8)`, hence
the same holds for $f$ according to the lemma `(15.7.11.1)`. It then suffices to apply `(15.7.10)`, remarking that the
set of $y \in Y$ such that $f$ be proper at $y$ is by definition open in $Y$.

(To be continued.)
