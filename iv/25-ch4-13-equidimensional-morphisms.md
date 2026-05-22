<!-- original page 187 -->

## §13. Equidimensional morphisms

This section is devoted to the study of the variation of the dimension of the fibres of a morphism locally of finite
type $f : X \to Y$ (which has already come up in connection with the "dimension formula" in `(5.5)` and `(5.6)`). We
prove first `(13.1.3)` that the function $x \mapsto \dim_{x}(f^{-1}(f(x)))$ is always upper semi-continuous in $X$
(Chevalley's *semi-continuity theorem*). We then study more specifically the morphisms, called *equidimensional*, for
which this function is locally constant. Unfortunately the notion of equidimensional morphism is not stable under base
change;

<!-- original page 188 -->

this is why in numerous questions it is more convenient to work with the notion of universally open morphism, the study
of which is the object of §§14 and 15.

### 13.1. Chevalley's semi-continuity theorem

**Lemma (13.1.1).**

<!-- label: IV.13.1.1 -->

*Let $Y$ be a locally Noetherian irreducible prescheme, $X$ an irreducible prescheme, $f : X \to Y$ a dominant morphism
of finite type. Let $\xi$ (resp. $\eta$) be the generic point of $X$ (resp. $Y$) and let $e = \dim(f^{-1}(\eta))$. Then,
for every $x \in X$, every irreducible component of $f^{-1}(f(x))$ is of dimension $\geq e$.*

The proposition is immediate when, for every $y \in f(X)$, $\mathcal{O}_{y}$ is a universally catenary ring: indeed, if
$x$ is the generic point of an irreducible component $Z$ of $f^{-1}(y)$, it follows from `(5.6.5)`, joined with
`(5.2.1)`, that one has `e + dim(𝒪_y) = dim(Z) + dim(𝒪_x)`; but by virtue of `(0, 16.3.9)` one has
$\dim(\mathcal{O}_{x}) \leq \dim(\mathcal{O}_{y})$, whence the conclusion in this case.

We shall reduce the general case to this particular case. The question is evidently local on $Y$, and, in view of
`(4.1.1.3)`, it is also local on $X$; one may therefore restrict to the case where $Y = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine and irreducible, $B$ being an $A$-algebra of finite type. Moreover `(1.5.4)`, one may
suppose $X$ and $Y$ reduced, hence $A$ and $B$ integral, and, since $f$ is dominant, $A$ is then a sub-ring of $B$.
Consider $A$ as the inductive limit of its sub-$\mathbb{Z}$-algebras of finite type; it then follows from `(8.9.1)` that
there exists such a sub-algebra `A_0` and an `A_0`-algebra of finite type `B_0` such that $B = B_{0} \otimes_{A_{0}} A$.
Set $Y_{0} = \operatorname{Spec}(A_{0})$, $X_{0} = \operatorname{Spec}(B_{0})$, and let $f_{0} : X_{0} \to Y_{0}$ be the
morphism corresponding to the homomorphism $A_{0} \to B_{0}$, so that $f = f_{0} \times_{Y_{0}} 1_{Y}$. It is not
evident a priori that the prescheme `X_0` is integral, but we shall see that one can reduce to this case. Let $\eta_{0}$
be the generic point of `Y_0`, so that if $g$ is the morphism $Y \to Y_{0}$, one has $g(\eta) = \eta_{0}$; by
transitivity of fibres `(I, 3.6.4)`, one has $f^{-1}(\eta) = f^{-1}_{0}(\eta_{0}) \otimes_{\mathit{k}(\eta_{0})}
\mathit{k}(\eta)$, and since $f^{-1}(\eta)$ is irreducible by hypothesis, so is $f^{-1}_{0}(\eta_{0})$ `(4.4.1)`. Our
assertion will then result from the following lemma:

**Lemma (13.1.2).**

<!-- label: IV.13.1.2 -->

*Let `Y_0`, $Y$ be two integral preschemes with generic points $\eta_{0}$, $\eta$, $g : Y \to Y_{0}$ a dominant
morphism, $f_{0} : X_{0} \to Y_{0}$ a dominant morphism such that $f^{-1}_{0}(\eta_{0})$ is irreducible. Let $X'_{0}$ be
the unique irreducible component of `X_0` meeting $f^{-1}_{0}(\eta_{0})$ $(0_{I}, 2.1.8)$, and denote again by $X'_{0}$
the reduced closed sub-prescheme of `X_0` having $X'_{0}$ as underlying space. Suppose that the prescheme $X = X'_{0}
\times_{Y_{0}} Y$ is integral; then $X$ is isomorphic to $X'_{0} \times_{Y_{0}} Y$.*

Indeed, if $j_{0} : X'_{0} \to X_{0}$ is the canonical injection, which is a closed immersion, $j = j_{0} \times_{Y_{0}}
1_{Y} : X'_{0} \times_{Y_{0}} Y \to X_{0} \times_{Y_{0}} Y = X$ is a closed immersion. On the other hand, $X'_{0}$
contains the fibre $f^{-1}_{0}(\eta_{0})$, so $X'_{0} \times_{Y_{0}} Y$ contains $f^{-1}(\eta)$; note moreover that
$f^{-1}(\eta)$ is non-empty `(I, 3.4.7)`, hence contains the generic point of $X$; consequently the image of $j$ is
necessarily all of $X$. But since $X$ is integral, the only closed sub-prescheme of $X$ having $X$ as underlying space
is $X$ itself, hence $j$ is an isomorphism.

This lemma being established, one may therefore suppose that `X_0` is integral; for every $y_{0} \in Y_{0}$,
$\mathcal{O}_{y_{0}}$ is a $\mathbb{Z}$-algebra essentially of finite type, hence a universally catenary ring

<!-- original page 189 -->

`(5.6.4)`; consequently, for every $y_{0} \in f_{0}(X_{0})$, every irreducible component of $f^{-1}_{0}(y_{0})$ has
dimension $\geq e$, since one knows that $\dim(f^{-1}_{0}(\eta_{0})) = e$ by transitivity of fibres `(4.1.4)`. For every
$y \in f(X)$, one then has $y_{0} = g(y) \in f_{0}(X_{0})$, and by transitivity of fibres and `(4.2.7)` one completes
the proof.

**Theorem (13.1.3) (Chevalley).**

<!-- label: IV.13.1.3 -->

*Let $f : X \to Y$ be a morphism locally of finite type. For every integer $n$, the set $F_{n}(X)$ of $x \in X$ such
that $\dim_{x}(f^{-1}(f(x))) \geq n$ is closed; in other words, the function $x \mapsto \dim_{x}(f^{-1}(f(x)))$ is upper
semi-continuous in $X$.*

I) Suppose first that $f$ is locally of finite presentation.

The question is evidently local on $X$ and on $Y$, and one may therefore suppose $Y = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$ affine, $B$ being an $A$-algebra of finite presentation. One then knows `(8.9.1)` that there is
a Noetherian sub-ring `A_0` of $A$ and an `A_0`-algebra of finite type `B_0` such that, if one sets $Y_{0} =
\operatorname{Spec}(A_{0})$, $X_{0} = \operatorname{Spec}(B_{0})$, one has $X = X_{0} \times_{Y_{0}} Y$, $f = f_{0}
\times_{Y_{0}} 1_{Y}$, where $f_{0} : X_{0} \to Y_{0}$ corresponds to the homomorphism $A_{0} \to B_{0}$. Let $g : Y \to
Y_{0}$ be the morphism corresponding to the canonical injection $A_{0} \to A$, $y$ a point of $Y$, $y_{0} = g(y)$; one
knows that $f^{-1}(y) = f^{-1}_{0}(y_{0}) \otimes_{\mathit{k}(y_{0})} \mathit{k}(y)$, and it follows from `(4.2.7)` that
if $p$ is the canonical projection $f^{-1}(y) \to f^{-1}_{0}(y_{0})$, the irreducible components of $f^{-1}(y)$ are the
irreducible components of the sets $p^{-1}(Z_{0})$, where `Z_0` ranges over the set of irreducible components of
$f^{-1}_{0}(y_{0})$, and each of the irreducible components of $p^{-1}(Z_{0})$ dominates `Z_0` and has dimension equal
to $\dim(Z_{0})$. Taking `(0, 14.1.5)` into account, one sees that if $g' : X \to X_{0}$ is the canonical projection,
$x$ a point of $X$ and $x_{0} = g'(x)$, one has $\dim_{x}(f^{-1}(f(x))) = \dim_{x_{0}}(f^{-1}_{0}(f_{0}(x_{0})))$,
whence $F_{n}(X) = g'^{-1}(F_{n}(X_{0}))$, and one is consequently reduced to proving the theorem when $Y$ is
Noetherian, which we shall suppose henceforth.

One may evidently suppose $X$ and $Y$ reduced `(1.5.4)`. Considering the set of closed subsets $Y'$ of $Y$ such that the
theorem is true for the closed sub-prescheme of $Y$ having $Y'$ as underlying space and for $X' = f^{-1}(Y')$, one may
argue by Noetherian induction $(0_{I}, 2.2.2)$ and suppose that the theorem is true for every closed subset $Y' \neq Y$
of $Y$. If $X_{i}$ ($1 \leq i \leq m$) are the reduced closed sub-preschemes of $X$ having as underlying spaces the
irreducible components of $X$, one has $F_{n}(X) = \bigcup_{i} F_{n}(X_{i})$ by virtue of `(0, 14.1.5)`, and one may
therefore restrict to proving the theorem for each of the $X_{i}$; in other words, one may suppose $X$ irreducible. If
$Z$ is the closed sub-prescheme of $Y$ having $\overline{f(X)}$ as underlying space, $f$ factors as $X \xrightarrow{g} Z
\xrightarrow{j} Y$, where $j$ is the canonical injection `(I, 5.2.2)`, and $g$ is of finite type `(1.5.4)`, hence it
suffices to prove the theorem for $Z$ and $g$; by virtue of the inductive hypothesis, one is therefore reduced to
considering only the case where $Z = Y$, in other words where $Y$ is irreducible and $f$ dominant. Let then $\eta$ be
the generic point of $Y$ and set $e = \dim(f^{-1}(\eta))$; it follows from `(13.1.1)` that for $n \leq e$ one has
$F_{n}(X) = X$, and consequently one may restrict to the case where $n > e$. But then `(9.5.6)`, there is an open
neighbourhood $U$ of $\eta$ in $Y$ such that $F_{n}(X) \subset f^{-1}(Y - U)$; since $Y - U \neq Y$, the inductive
hypothesis entails that $F_{n}(X)$ is closed.

II) We now pass to the general case, still supposing that $S = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$
are affine, $B$ being an $A$-algebra of finite type, hence of the form

<!-- original page 190 -->

$B = A[T_{1}, \cdots, T_{n}]/\mathfrak{J}$. Let $(\mathfrak{J}_{\lambda})$ be the family of ideals of finite type of
$A[T_{1}, \cdots, T_{n}]$ contained in $\mathfrak{J}$, so that $\mathfrak{J}$ is the filtered union of the
$\mathfrak{J}_{\lambda}$; if $X$ and the $X_{\lambda} = \operatorname{Spec}(A[T_{1}, \cdots,
T_{n}]/\mathfrak{J}_{\lambda})$ are considered as closed sub-preschemes of $Z = \operatorname{Spec}(A[T_{1}, \cdots,
T_{n}])$, one therefore has, for the underlying spaces, $X = \bigcap_{\lambda} X_{\lambda}$. If $f_{\lambda} :
X_{\lambda} \to S$ is the structure morphism, one deduces that $f^{-1}(s) = \bigcap_{\lambda} f^{-1}_{\lambda}(s)$ for
every $s \in S$, and since the sets $f^{-1}_{\lambda}(s)$ are closed in the Noetherian space $Z_{s}$, there exists a
$\lambda$ (depending on $s$) such that $f^{-1}(s) = f^{-1}_{\lambda}(s)$. If then, for every $x \in X$, one sets $d(x) =
\dim_{x}(f^{-1}(f(x)))$, $d_{\lambda}(x) = \dim_{x}(f^{-1}_{\lambda}(f_{\lambda}(x)))$, what precedes proves that one
has $d(x) = \inf_{\lambda} d_{\lambda}(x)$; the functions $d_{\lambda}$ being upper semi-continuous by the first part of
the proof, so is $d$. Q.E.D.

**Corollary (13.1.4).**

<!-- label: IV.13.1.4 -->

*Under the hypotheses of `(13.1.3)`, the set of $x \in X$ such that $x$ is isolated in $f^{-1}(f(x))$ is open in $X$.*

Indeed, it is the complement of $F_{1}(X)$ `(0, 14.1.10)`.

One notes that one recovers in this way, under more general hypotheses, the consequence `(III, 4.4.10)` of Zariski's
"Main theorem".

**Corollary (13.1.5).**

<!-- label: IV.13.1.5 -->

*Under the hypotheses of `(13.1.3)`, suppose moreover that $f$ is a closed morphism. Then, for every integer $n$, the
set of $y \in Y$ such that $\dim(f^{-1}(y)) \geq n$ is closed; in other words, the map $y \mapsto \dim(f^{-1}(y))$ is
upper semi-continuous; in particular, if $y$ is a specialization of $y'$, one has $\dim(f^{-1}(y)) \geq
\dim(f^{-1}(y'))$.*

Indeed, to say that $\dim(f^{-1}(y)) \geq n$ means that $y \in f(F_{n}(X))$ `(0, 14.1.6)`.

**Corollary (13.1.6).**

<!-- label: IV.13.1.6 -->

*Let $X$, $Y$ be two irreducible preschemes, $f : X \to Y$ a dominant morphism locally of finite type. Let $\xi$ (resp.
$\eta$) be the generic point of $X$ (resp. $Y$) and let $e = \dim(f^{-1}(\eta))$. Then, for every $x \in X$, one has
$\dim_{x}(f^{-1}(f(x))) \geq e$.*

Indeed, the set of $x$ such that $\dim_{x}(f^{-1}(f(x))) < e$ is open by virtue of `(13.1.3)`, and since it cannot
contain $\xi$, it is empty.

Let us finally note the following easier result:

**Proposition (13.1.7).**

<!-- label: IV.13.1.7 -->

*Let $Y$ be a quasi-compact prescheme, $f : X \to Y$ a morphism of finite type. There exists an integer $n$ such that,
for every $y \in Y$, one has $\dim(f^{-1}(y)) \leq n$.*

Since there is a finite affine open cover $(V_{i})$ of $Y$ such that each $f^{-1}(V_{i})$ is a finite union of affine
open sets, one is immediately reduced to the case where $Y = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$
are affine, $B$ being an $A$-algebra of finite type. If $B$ admits a system of $n$ generators, then for every $y \in Y$,
$B \otimes_{A} \mathit{k}(y)$ is a $\mathit{k}(y)$-algebra admitting $n$ generators, hence $\dim(f^{-1}(y)) \leq n$ by
virtue of `(4.1.1)`.

### 13.2. Equidimensional morphisms: case of dominant morphisms of irreducible preschemes

**(13.2.1)** Let $Y$ be an irreducible prescheme, $X$ an irreducible prescheme, $f : X \to Y$ a dominant morphism
locally of finite type; let $\eta$ be the generic point of $Y$. One knows `(13.1.6)` that for every $x \in X$, one has

<!-- original page 191 -->

$$ \dim_{x}(f^{-1}(f(x))) \geq \dim(f^{-1}(\eta)). $$

**Definition (13.2.2).**

<!-- label: IV.13.2.2 -->

*Under the hypotheses of `(13.2.1)`, we say that $f$ is **equidimensional at the point $x$** (or that $X$ is
**equidimensional over $Y$ at the point $x$**) if*

$$ \dim_{x}(f^{-1}(f(x))) = \dim(f^{-1}(\eta)). $$

*We say that $f$ is **equidimensional** (or that $X$ is **equidimensional over $Y$**) if $f$ is equidimensional at every
point $x \in X$.*

It follows from Chevalley's theorem `(13.1.3)` that the set of $x \in X$ where $f$ is equidimensional is *open and
non-empty*. Moreover, if $f$ is equidimensional at the point $x$, every irreducible component of $f^{-1}(f(x))$ that
contains $x$ has the same dimension, since each of them has a dimension which is $\geq \dim(f^{-1}(\eta))$ `(13.1.6)`
and $\leq \dim_{x}(f^{-1}(f(x)))$ by virtue of `(0, 14.1.5)`.

**Proposition (13.2.3).**

<!-- label: IV.13.2.3 -->

*Let $Y$ be a locally Noetherian irreducible prescheme, $X$ an irreducible prescheme, $f : X \to Y$ a dominant morphism
locally of finite type; let $\eta$ be the generic point of $Y$, $x$ a point of $X$, $y = f(x)$, and suppose that one
has*

```text
  (13.2.3.1)            dim(𝒪_x) = dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} 𝒌(y)).
```

*Then $f$ is equidimensional at the point $x$. The converse is true if the two sides of the inequality `(5.6.5.2)` are
equal, in particular if $\mathcal{O}_{y}$ is universally catenary.*

This follows at once from `(5.6.5.2)` and the inequality $\delta(x) \geq 0$ `(13.1.1)`.

**(13.2.4)** Let now, in a general way, $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism of finite type,
$x$ a point of $X$, $X'$ an irreducible closed subset of $X$ containing $x$, $y = f(x)$, $Y' = \overline{f(X')}$,
$\eta'$ the generic point of $Y'$. Denote again by $X'$ and $Y'$ the reduced closed sub-preschemes of $X$ and $Y$
respectively having $X'$ and $Y'$ as underlying spaces; the restriction $X' \to Y$ of $f$ factors then as $X'
\xrightarrow{f'} Y' \xrightarrow{j} Y$, where $j$ is the canonical injection `(I, 5.2.2)`, and $f'$ is of finite type
`(1.5.4)`. Set then, to abbreviate,

```text
  (13.2.4.1)        A = 𝒪_{Y, y},   B = 𝒪_{X, x},   A' = 𝒪_{Y', y},   B' = 𝒪_{X', x}.
```

Formula `(5.6.5.2)` applied to the dominant morphism $f'$ and to the irreducible preschemes $X'$, $Y'$ gives

```text
  (13.2.4.2)        dim(B') ≤ dim(A') + dim(B' ⊗_{A'} 𝒌(y)) − (dim_x(f'⁻¹(y)) − dim(f'⁻¹(η'))).
```

On the other hand, the local ring $A'$ (resp. $B'$, $B' \otimes_{A'} \mathit{k}(y)$) is a quotient ring of $A$ (resp.
$B$, $B \otimes_{A} \mathit{k}(y)$), hence `(0, 16.1.2.1)` one has

```text
  (13.2.4.3)    dim(A') ≤ dim(A),   dim(B') ≤ dim(B),   dim(B' ⊗_{A'} 𝒌(y)) ≤ dim(B ⊗_A 𝒌(y)).
```

One deduces therefore first from `(13.2.4.3)` and `(0, 16.3.9)`

```text
  (13.2.4.4)            dim(B') ≤ dim(A') + dim(B' ⊗_{A'} 𝒌(y)) ≤ dim(A) + dim(B ⊗_A 𝒌(y)).
```

Moreover, by virtue of `(0, 16.3.9)`, one also has the inequalities

```text
  (13.2.4.5)            dim(B') ≤ dim(B) ≤ dim(A) + dim(B ⊗_A 𝒌(y)).
```

<!-- original page 192 -->

The comparison of these inequalities therefore shows that:

**Lemma (13.2.5).**

<!-- label: IV.13.2.5 -->

*With the notations of `(13.2.4)`, the following conditions are equivalent:*

*a) `dim(B') = dim(A) + dim(B ⊗_A 𝒌(y))`.*

*b) One has simultaneously the following relations:*

*(i) $\dim(A') = \dim(A)$.*

*(ii) $\dim(B' \otimes_{A'} \mathit{k}(y)) = \dim(B \otimes_{A} \mathit{k}(y))$, in other words*

$$ \dim_{x}(X' \cap f^{-1}(y)) = \dim_{x}(f^{-1}(y)). $$

*(iii) $\dim_{x}(f'^{-1}(y)) = \dim(f'^{-1}(\eta'))$, in other words $f' : X' \to Y'$ is equidimensional `(13.2.2)` at
the point $x$.*

*(iv) One has the equality*

```text
                       dim(B') = dim(A') + dim(B' ⊗_{A'} 𝒌(y))
```

*(a relation which is always satisfied when $A = \mathcal{O}_{Y, y}$ is a universally catenary ring, in virtue of
`(5.6.5)`).*

*c) One has simultaneously the following relations:*

*(i) $\dim(B') = \dim(B)$.*

*(ii) `dim(B) = dim(A) + dim(B ⊗_A 𝒌(y))`.*

**(13.2.6)** Let us now recall that the irreducible components $X_{i}$ of $X$ containing $x$ are in finite number and
that one has (`(5.1.2.1)` and `(0, 14.2.1.1)`)

```text
  (13.2.6.1)            dim(𝒪_{X, x}) = sup_i dim(𝒪_{X_i, x}).
```

The equivalence of conditions b) and c) in `(13.2.5)` implies consequently, in view of `(0, 16.3.9)` and `(0, 14.2.1)`:

**Proposition (13.2.7).**

<!-- label: IV.13.2.7 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism of finite type, $x$ a point of $X$, $f(x) = y$; one
has*

```text
  (13.2.7.1)            dim(𝒪_{X, x}) ≤ dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*For the two sides of `(13.2.7.1)` to be equal, it is necessary and sufficient that there exist an irreducible closed
subset $X'$ of $X$ containing $x$ and satisfying simultaneously the following conditions:*

*(i) If $Y' = \overline{f(X')}$, one has $\dim(\mathcal{O}_{Y', y}) = \dim(\mathcal{O}_{Y, y})$.*

*(ii) $\dim_{x}(X' \cap f^{-1}(y)) = \dim_{x}(f^{-1}(y))$ (in other words, $X'$ contains one of the irreducible
components of $f^{-1}(y)$ that contain $x$, of maximal dimension among all these components). This amounts to saying
that $\dim(\mathcal{O}_{X, x} \otimes_{\mathcal{O}_{Y, y}} \mathit{k}(y)) = \dim(\mathcal{O}_{X', x}
\otimes_{\mathcal{O}_{Y', y}} \mathit{k}(y))$.*

*(iii) $X'$ is equidimensional over $Y'$ at the point $x$, in other words, one has*

```text
                       dim_x(X' ∩ f⁻¹(y)) = dim(X' ∩ f'⁻¹(η')),
```

*where $\eta'$ is the generic point of $Y'$ (and consequently, all the irreducible components of $X' \cap f^{-1}(y)$
containing $x$ have the same dimension `(13.2.2)`).*

<!-- original page 193 -->

*(iv) One has the equality*

```text
                       dim(𝒪_{X', x}) = dim(𝒪_{Y', y}) + dim(𝒪_{X', x} ⊗_{𝒪_{Y', y}} 𝒌(y))
```

*(a condition always implied by (iii) when $\mathcal{O}_{Y, y}$ is a universally catenary ring).*

*Moreover, $X'$ is then an irreducible component of $X$ and $Y'$ an irreducible component of $Y$.*

In the statement, the local rings $\mathcal{O}_{X', x}$ and $\mathcal{O}_{Y', y}$ refer to the reduced closed
sub-preschemes of $X$, $Y$ having $X'$ and $Y'$ respectively as underlying spaces.

Moreover, this proves the following:

**Corollary (13.2.8).**

<!-- label: IV.13.2.8 -->

*If the two sides of `(13.2.7.1)` are equal, the irreducible closed subsets $X'$ of $X$ containing $x$ and satisfying
conditions (i) to (iv) of `(13.2.7)` are exactly those for which one has $\dim(\mathcal{O}_{X', x}) =
\dim(\mathcal{O}_{X, x})$ (which necessarily implies that $X'$ is an irreducible component of $X$).*

Proposition `(13.2.7)` entails:

**Corollary (13.2.9).**

<!-- label: IV.13.2.9 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism of finite type, $x$ a point of $X$, $f(x) = y$.
Suppose that $\mathcal{O}_{Y, y}$ is a universally catenary ring. Then the following conditions are equivalent:*

*a) The two sides of `(13.2.7.1)` are equal.*

*b) There exists an irreducible component $Z$ of $f^{-1}(y)$ containing $x$, of dimension $\dim_{x}(f^{-1}(y))$, such
that for every $x'$ in a neighbourhood of $x$ in $Z$, one has*

```text
  (13.2.9.1)        dim(𝒪_{X, x'}) = dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*c) There exists an irreducible component $Z$ of $f^{-1}(y)$ containing $x$, of dimension $\dim_{x}(f^{-1}(y))$, such
that for the generic point $z$ of $Z$, one has*

```text
  (13.2.9.2)            dim(𝒪_{X, z}) = dim(𝒪_{Y, y}).
```

Let us show that a) entails b). Set $\dim_{x}(f^{-1}(y)) = n$; by virtue of `(13.2.7)`, there exists an irreducible
component $X'$ of $X$ satisfying conditions (i) to (iv) of `(13.2.7)`; let $Z$ be an irreducible component of dimension
$n$ of $f^{-1}(y)$, containing $x$ and contained in $X'$. Since $f^{-1}(y)$ is locally Noetherian, there exists an open
neighbourhood $U$ of $x$ in $Z$ such that $U$ meets no irreducible component of $f^{-1}(y)$ other than those that
contain $x$, hence `(4.1.1.3)` $\dim_{x'}(f^{-1}(y)) = n$ for every $x' \in U$; it is then clear that conditions (i) to
(iii) of `(13.2.7)` are satisfied when one replaces $x$ by an arbitrary point $x' \in U$, and so is condition (iv) since
$\mathcal{O}_{Y, y}$ is universally catenary; whence the conclusion by `(13.2.7)`. Condition b) trivially entails c) by
virtue of `(5.1.2)`. Finally, if c) is satisfied and if `X''` is an irreducible component of $X$ containing $Z$ and such
that conditions (i) to (iv) of `(13.2.7)` are satisfied when one replaces $X'$ by `X''` and $x$ by $z$, it is clear that
these conditions are also satisfied for `X''` and $x$ since $\mathcal{O}_{Y, y}$ is universally catenary, hence c)
implies a).

**Proposition (13.2.10).**

<!-- label: IV.13.2.10 -->

*Let $Y$ be a locally Noetherian irreducible prescheme, $\eta$ its generic point, $f : X \to Y$ a morphism of finite
type, $y$ a point of $f(X)$. Let $Z_{i}$ be the*

<!-- original page 194 -->

*irreducible components of $f^{-1}(y)$, $z_{i}$ the generic point of $Z_{i}$, and consider the following conditions:*

*a) For every $x \in f^{-1}(y)$, one has the relation*

```text
  (13.2.10.1)       dim(𝒪_{X, x}) = dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*b) For every $i$, one has*

```text
  (13.2.10.2)           dim(𝒪_{X, z_i}) = dim(𝒪_{Y, y}).
```

*c) For every $i$, there exists an irreducible component $X_{i}$ of $X$ containing $Z_{i}$ and such that $\dim(X_{i}
\cap f^{-1}(\eta)) = \dim(Z_{i})$ (in other words, such that the reduced closed sub-prescheme $X_{i}$ of $X$ is
equidimensional over $Y$ at the point $z_{i}$).*

*Then a) entails b) and b) entails c); moreover, if $\mathcal{O}_{Y, y}$ is universally catenary, the three conditions
a), b), c) are equivalent.*

The ring $\mathcal{O}_{X, z_{i}} \otimes_{\mathcal{O}_{Y, y}} \mathit{k}(y)$ being of dimension `0` `(5.1.2)`, a)
evidently entails b); b) entails c) by virtue of `(13.2.7)` applied at the point $z_{i}$. Conversely, suppose that
$\mathcal{O}_{Y, y}$ is universally catenary; since condition c) implies that $f(X_{i})$ is dense in $Y$, it follows
from c) that conditions (i) to (iv) of `(13.2.7)` are satisfied on replacing $X'$ by $X_{i}$ and $x$ by $z_{i}$, hence
c) implies b); finally b) implies a) by virtue of `(13.2.9)`.

**Corollary (13.2.11).**

<!-- label: IV.13.2.11 -->

*The notations being those of `(13.2.10)`, suppose that $\mathcal{O}_{Y, y}$ is universally catenary. For every $y' \in
Y$, let $E(y')$ be the set of dimensions of the irreducible components of $f^{-1}(y')$ and set $d(y') = \dim(f^{-1}(y'))
= \sup(E(y'))$. Then, if the equivalent conditions a), b), c) of `(13.2.10)` are satisfied, one has $E(y) \subset
E(\eta)$, whence $d(y) \leq d(\eta)$.*

Indeed, with the notations of `(13.2.10)`, $X_{i} \cap f^{-1}(\eta)$ is non-empty and is consequently an irreducible
component of $f^{-1}(\eta)$ $(0_{I}, 2.1.8)$.

**Remarks (13.2.12).**

<!-- label: IV.13.2.12 -->

(i) Recall `(6.1.2)` that the relation `(13.2.10.1)` is always satisfied when the morphism $f$ is flat at the point $x$.

(ii) With the notations of `(13.2.10)`, suppose that $\mathcal{O}_{Y, y}$ is universally catenary and moreover that the
morphism $f$ is proper; then, if the equivalent conditions a), b), c) of `(13.2.10)` are satisfied, one has even $d(y) =
d(\eta)$, since it follows from `(13.1.5)` that one has $d(y) \geq d(\eta)$.

(iii) The morphism of `(12.2.3, (b))` is proper and flat and all local rings of $Y$ are universally catenary; moreover,
the two irreducible components `X_1`, `X_2` of $X$ are equidimensional over $Y$ at every point; but $E(y)$ has *two*
elements for every $y \neq y_{0}$, while $E(y_{0})$ is reduced to a *single* element, hence $E(y)$ is not constant on
$Y$.

### 13.3. Equidimensional morphisms: general case

**Proposition (13.3.1).**

<!-- label: IV.13.3.1 -->

*Let $Y$ be a prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $y = f(x)$. Denote by
$Y_{\alpha}$ the irreducible components of $Y$ containing $y$. Then the following conditions are equivalent:*

<!-- original page 195 -->

*a) There exist an integer $e$ and an open neighbourhood $U$ of $x$ such that the image under $f$ of every irreducible
component of $U$ is dense in some $Y_{\alpha}$, and that, for every $x' \in U$, the space $U \cap f^{-1}(f(x'))$ is
equidimensional and of dimension $e$.*

*a') There exist an integer $e$ and an open neighbourhood $U$ of $x$ such that the image under $f$ of every irreducible
component of $U$ is dense in some $Y_{\alpha}$ and such that, if one denotes by $y_{\alpha}$ the generic point of
$Y_{\alpha}$, every irreducible component of the spaces $U \cap f^{-1}(y)$, $U \cap f^{-1}(y_{\alpha})$ is of dimension
$e$.*

*a'') There exist an integer $e$ and an open neighbourhood $U$ of $x$ such that, for each of the irreducible components
$U_{\lambda}$ of $U$, $f(U_{\lambda})$ is dense in some $Y_{\alpha}$ and such that, for every $x' \in U_{\lambda}$, the
irreducible components of $U_{\lambda} \cap f^{-1}(f(x'))$ are all of dimension $e$.*

*b) There exist an integer $e$, an open neighbourhood $U$ of $x$ and a $Y$-morphism quasi-finite $g : U \to Y
\otimes_{\mathbb{Z}} \mathbb{Z}[T_{1}, \cdots, T_{e}]$ (a prescheme that we shall also denote $Y[T_{1}, \cdots, T_{e}]$
for brevity) such that the image under $g$ of every irreducible component of $U$ is dense in an irreducible component of
$Y[T_{1}, \cdots, T_{e}]$.*

It is immediate that a'') entails a), for, for every $x \in U$, the irreducible components of $U \cap f^{-1}(f(x))$ are
each an irreducible component of one of the $U_{\lambda} \cap f^{-1}(f(x))$, whence the conclusion by `(0, 14.1.4)`.
Condition a) trivially entails a'). Let us next show that a') entails a''); one may restrict to the case where $f$ is of
finite type and $X$ and $Y$ reduced `(1.5.4)`. Let $U_{\lambda}$ be an irreducible component of $U$, and suppose that
$f(U_{\lambda})$ is dense in $Y_{\alpha}$; then the restriction of $f$ to $U_{\lambda}$ factors as $U_{\lambda}
\xrightarrow{f_{\alpha}} Y_{\alpha} \to Y$, where $f_{\alpha}$ is of finite type and dominant `(I, 5.2.2)`. Let
$x_{\lambda}$ be the generic point of $U_{\lambda}$; by virtue of $(0_{I}, 2.1.8)$, $U_{\lambda} \cap
f^{-1}_{\alpha}(y_{\alpha})$ is the unique irreducible component of $U \cap f^{-1}(y_{\alpha})$ containing $x_{\lambda}$
and is by hypothesis of dimension $e$, equal to the dimensions of all the irreducible components of $U_{\lambda} \cap
f^{-1}(y)$, by virtue of the hypothesis and of `(13.1.1)`. But by virtue of Chevalley's theorem `(13.1.3)` and of
`(13.1.1)`, the set $V_{\lambda}$ of $x' \in U_{\lambda}$ such that $\dim_{x'}(f^{-1}_{\alpha}(f_{\alpha}(x'))) = e$ is
open and contains $x$, and it suffices to take the union of the $V_{\lambda}$ to obtain an open set satisfying the
conditions of a'').

Let us now prove that a) entails b); one may restrict to the case where $Y = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine and where $U = X$. Let us first prove the following lemma:

**Lemma (13.3.1.1).**

<!-- label: IV.13.3.1.1 -->

*Let $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ be two affine schemes, $f : X \to Y$ a morphism of
finite type, $y$ a point of $f(X)$, and set $e = \dim(f^{-1}(y))$. Then there exists a $Y$-morphism $g : X \to Y[T_{1},
\cdots, T_{e}]$ such that (if one sets $X_{y} = X \times_{Y} \operatorname{Spec}(\mathit{k}(y))$) the morphism $g_{y} :
X_{y} \to \operatorname{Spec}(\mathit{k}(y)[T_{1}, \cdots, T_{e}])$ is finite. Moreover, for such a morphism $g$,
$g_{y}$ is necessarily surjective and there exists an open neighbourhood $U$ of $f^{-1}(y)$ in $X$ such that $g|U$ is
quasi-finite.*

Set $\mathfrak{p} = j_{y}$; the ring $B \otimes_{A} \mathit{k}(\mathfrak{p})$ is a $\mathit{k}(\mathfrak{p})$-algebra of
finite type, hence the normalization lemma (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, th. 1) proves that there is in $B
\otimes_{A} \mathit{k}(\mathfrak{p})$ a finite sequence $(t_{i})_{1 \leq i \leq r}$ of elements algebraically
independent over $\mathit{k}(\mathfrak{p})$ and such that, if one sets $C' = \mathit{k}(\mathfrak{p})[t_{1}, \cdots,
t_{r}]$, $B \otimes_{A} \mathit{k}(\mathfrak{p})$ is a *finite* $C'$-algebra; one therefore has $\dim(B \otimes_{A}
\mathit{k}(\mathfrak{p})) = \dim(C')$ `(0, 16.1.5)`, and since $\dim(C') = r$ `(5.2.1)`, one has $r = e$. Since $B
\otimes_{A} \mathit{k}(\mathfrak{p}) = (B/\mathfrak{p}B) \otimes_{A/\mathfrak{p}} \mathit{k}(\mathfrak{p})$, one can, by
multiplying the $t_{i}$ by a suitable non-zero element

<!-- original page 196 -->

of $A/\mathfrak{p}$, suppose that each $t_{i}$ is the canonical image in $B \otimes_{A} \mathit{k}(\mathfrak{p})$ of an
element $s_{i} \in B$. Let then $u : A[T_{1}, \cdots, T_{e}] \to B$ be the homomorphism such that $u(T_{i}) = s_{i}$ for
every $i$, and let $g : X \to Y[T_{1}, \cdots, T_{e}]$ be the corresponding morphism. It is clear that, by reason of the
choice of the $s_{i}$, $g_{y}$ is a finite morphism. For every morphism $g : X \to Y[T_{1}, \cdots, T_{e}]$ such that
$g_{y}$ is finite, it follows from `(5.4.2)` and `(4.1.2.1)` that $g_{y}$ is necessarily surjective. On the other hand,
by virtue of `(13.1.4)`, the set $U$ of $x \in X$ that are isolated in their fibre $g^{-1}(g(x))$ is open in $X$ and
contains $f^{-1}(y)$, and by definition the restriction $g|U$ is a quasi-finite morphism.

This lemma being established, to prove that a) implies b), it remains to see that if $x_{\lambda}$ is a maximal point of
$U$, $g(x_{\lambda}) = z_{\lambda}$ is a maximal point of $Z = Y[T_{1}, \cdots, T_{e}]$. By virtue of hypothesis a), one
may (on restricting $U$ if necessary) suppose that $f(x_{\lambda})$ is one of the generic points $y_{\alpha}$ of the
irreducible components of $Y$ containing $y$; if $p : Z \to Y$ is the structure morphism, one therefore has
$p(z_{\lambda}) = y_{\alpha}$, and one consequently deduces from $g$ a $\mathit{k}(y_{\alpha})$-morphism quasi-finite
$h : U \cap f^{-1}(y_{\alpha}) \to p^{-1}(y_{\alpha})$. Now
$p^{-1}(y_{\alpha}) = \operatorname{Spec}(\mathit{k}(y_{\alpha})[T_{1}, \cdots, T_{e}])$ is integral and of dimension
$e$; if $z_{\lambda}$ were not a maximal point of $Z$, it would not be a maximal point of $p^{-1}(y_{\alpha})$
$(0_{I}, 2.1.8)$ and its closure $Z'_{\lambda}$ in $p^{-1}(y_{\alpha})$ would therefore be of dimension $< e$
`(4.1.2.1)`. But since $h$ is quasi-finite, it follows from `(4.1.2)` and from hypothesis a) that one has
$\dim(Z'_{\lambda}) \geq e$ (the restriction of $h$ to $\overline{x_{\lambda}}$ factoring as
$\overline{x_{\lambda}} \to Z'_{\lambda} \to p^{-1}(y_{\alpha})$ by virtue of `(I, 5.2.2)`); one thus arrives at a
contradiction, which shows that a) entails b).

Let us finally prove that b) implies a). Note that the structure morphism $p : Z = Y[T_{1}, \cdots, T_{e}] \to Y$ is
faithfully flat; hence `(2.3.4)` the maximal points of $Z$ have as their images under $p$ the maximal points of $Y$;
this already proves that the $f(x_{\lambda})$ are generic points of the $Y_{\alpha}$. Moreover, if $f(x_{\lambda}) =
y_{\alpha}$, the $\mathit{k}(y_{\alpha})$-morphism $h : U \cap f^{-1}(y_{\alpha}) \to p^{-1}(y_{\alpha})$ deduced from
$g$ is dominant and quasi-finite by hypothesis; one therefore has $\dim(U_{\lambda} \cap f^{-1}(y_{\alpha})) = e$ by
virtue of `(4.1.2)` ($U_{\lambda}$ being the irreducible component of $U$ with generic point $x_{\lambda}$). Likewise,
for every $x' \in U_{\lambda}$, the morphism $U_{\lambda} \cap f^{-1}(f(x')) \to p^{-1}(f(x'))$ deduced from $g$ is a
$\mathit{k}(f(x'))$-morphism quasi-finite, hence `(4.1.2)` one has $\dim(f^{-1}(f(x')) \cap U_{\lambda}) \leq e$; but on
the other hand one knows `(13.1.6)` that all the irreducible components of $U_{\lambda} \cap f^{-1}(f(x'))$ are of
dimension $\geq e$; one thus sees that these components are exactly of dimension $e$, hence b) entails a). Q.E.D.

**Definition (13.3.2).**

<!-- label: IV.13.3.2 -->

*Let $Y$ be a prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$. We say that $f$ is
**equidimensional at the point $x$** (or that $X$ is **equidimensional over $Y$ at the point $x$**) if the equivalent
conditions of `(13.3.1)` are satisfied. We say that $f$ is **equidimensional** (or that $X$ is **equidimensional over
$Y$**) if $f$ is equidimensional at every point $x \in X$.*

It is clear that, for $f$ to be equidimensional at a point $x$, it is necessary and sufficient that $f_{red}$ be so.
Moreover, the conditions of `(13.3.1)` show that the set of points where $f$ is equidimensional is *open* in $X$.

One notes that when $X$ and $Y$ are irreducible, to say that $f$ is equidimensional

<!-- original page 197 -->

at the point $x$ means, by virtue of `(13.3.1, a'')`, that $f$ is dominant and that $\dim_{x}(f^{-1}(f(x))) =
\dim(f^{-1}(\eta))$ (where $\eta$ is the generic point of $Y$); definition `(13.3.2)` therefore coincides in this case
with definition `(13.2.2)`.

**Proposition (13.3.3).**

<!-- label: IV.13.3.3 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $X_{j}$
the irreducible components of $X$ (in finite number) containing $x$. For $f$ to be equidimensional at the point $x$, it
is necessary and sufficient that, for every $j$, $Y_{j} = \overline{f(X_{j})}$ be an irreducible component of $Y$ and,
denoting by $X_{j}$ and $Y_{j}$ the reduced closed sub-preschemes of $X$ and $Y$ with $X_{j}$ and $Y_{j}$ as underlying
spaces, by $f_{j} : X_{j} \to Y_{j}$ the morphism deduced from $f$ `(I, 5.2.2)`, by $y_{j}$ the generic point of
$Y_{j}$, that $f_{j}$ be equidimensional at the point $x$ and that all the numbers $\dim(f^{-1}_{j}(y_{j}))$ be equal.*

This follows at once from `(13.3.1, a')`.

**Corollary (13.3.4).**

<!-- label: IV.13.3.4 -->

*With the notations of `(13.3.3)`, set $y = f(x)$. If $\mathcal{O}_{Y, y}$ is a universally catenary ring and if $f$ is
equidimensional at the point $x$, one has*

```text
  (13.3.4.1)        dim(𝒪_{X_j, x}) = dim(𝒪_{Y_j, y}) + e − deg.tr_{𝒌(y)} 𝒌(x)
```

*where $e$ is the common value of the numbers $\dim(f^{-1}_{j}(y_{j}))$.*

Since each of the $\mathcal{O}_{Y_{j}, y}$, a quotient of $\mathcal{O}_{Y, y}$, is a universally catenary ring
`(5.6.1)`, the equality is a consequence of `(5.6.5)`.

**Corollary (13.3.5).**

<!-- label: IV.13.3.5 -->

*With the notations of `(13.3.4)`, suppose that $f$ is equidimensional at the point $x$ and that $\mathcal{O}_{Y, y}$ is
a universally catenary ring. If the ring $\mathcal{O}_{Y, y}$ is equidimensional, so is $\mathcal{O}_{X, x}$. The
converse is true if the image under $f$ of the union of the $X_{j}$ is dense in a neighbourhood of $y$.*

Indeed, to say that $\mathcal{O}_{Y, y}$ is equidimensional means that the numbers $\dim(\mathcal{O}_{Y'_{i}, y})$ are
equal for all the irreducible components $Y'_{i}$ of $Y$ containing $y$, as follows from `(5.1.1.5)` applied to the
local scheme $\operatorname{Spec}(\mathcal{O}_{Y, y})$; since one has the relation `(13.3.4.1)`, it follows by the same
reasoning that $\mathcal{O}_{X, x}$ is then equidimensional. Conversely, if $\mathcal{O}_{X, x}$ is equidimensional, all
the numbers $\dim(\mathcal{O}_{Y_{j}, y})$ are equal by `(13.3.4.1)`; one deduces that $\mathcal{O}_{Y, y}$ is
equidimensional if the $Y_{j}$ are *all* the irreducible components of $Y$ containing $y$, which follows from the
additional hypothesis.

**Proposition (13.3.6).**

<!-- label: IV.13.3.6 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $y =
f(x)$. Suppose that the ring $\mathcal{O}_{y}$ is equidimensional. Then, if $\mathcal{O}_{x}$ is equidimensional and if
one has the equality*

```text
  (13.3.6.1)        dim(𝒪_x) = dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} 𝒌(y))
```

*(cf. `(13.2.7.1)`), $f$ is equidimensional at the point $x$, and the converse is true if $\mathcal{O}_{y}$ is a
universally catenary ring.*

Let us keep the notations of `(13.3.3)`; it follows from `(13.2.8)` and from the hypothesis that $\mathcal{O}_{x}$ is
equidimensional, that each of the $Y_{j}$ is an irreducible component of $Y$ and that each of the $f_{j}$ is
equidimensional at the point $x$; moreover `(13.2.8)`, one has (taking `(5.6.5)` into account)

```text
  dim(𝒪_{X_j, x}) = dim(𝒪_{Y_j, y}) + dim_x(X_j ∩ f⁻¹(y)) − deg.tr_{𝒌(y)} 𝒌(x).
```

<!-- original page 198 -->

Now, since $\mathcal{O}_{y}$ is supposed equidimensional, this equality is written

```text
  (13.3.6.2)        dim_x(X_j ∩ f⁻¹(y)) = dim(𝒪_{X, x}) − dim(𝒪_{Y, y}) + deg.tr_{𝒌(y)} 𝒌(x).
```

The left-hand side of `(13.3.6.2)` is therefore independent of $j$; but since $f_{j}$ is equidimensional at the point
$x$, one has $\dim_{x}(X_{j} \cap f^{-1}(y)) = \dim(f^{-1}_{j}(y_{j}))$, hence the criterion `(13.3.3)` shows that $f$
is equidimensional at the point $x$.

Conversely, suppose that $\mathcal{O}_{Y, y}$ is a universally catenary ring and that $f$ is equidimensional at the
point $x$; then `(13.3.5)` $\mathcal{O}_{X, x}$ is equidimensional, and it then follows from `(13.3.4)` that one has the
relation

```text
  dim(𝒪_{X, x}) = dim(𝒪_{Y, y}) + e − deg.tr_{𝒌(y)} 𝒌(x)
```

where $e$ is the common value of the numbers $\dim(f^{-1}_{j}(y_{j})) = \dim_{x}(X_{j} \cap f^{-1}(y))$; but by
definition $e$ is also equal to $\dim_{x}(f^{-1}(y))$, whence the relation `(13.3.6.1)`, taking `(5.6.5.2)` into
account.

**Proposition (13.3.7).**

<!-- label: IV.13.3.7 -->

*Let $Y$ be a prescheme, $f : X \to Y$ a morphism locally of finite type and equidimensional, $Z$ a closed subset of
$X$. Then the function*

```text
  (13.3.7.1)            x ↦ codim_x(Z ∩ f⁻¹(f(x)), f⁻¹(f(x)))
```

*is lower semi-continuous in $X$.*

Since all the irreducible components of $f^{-1}(f(x))$ containing $x$ have by hypothesis the same dimension `(13.3.1)`,
one has, by virtue of `(5.2.1)`,

```text
  codim_x(Z ∩ f⁻¹(f(x)), f⁻¹(f(x))) = dim_x(f⁻¹(f(x))) − dim_x(Z ∩ f⁻¹(f(x))).
```

But by hypothesis the first term of the right-hand side is a *continuous* function of $x$ `(13.3.1)` and the second is
an upper semi-continuous function of $x$ by virtue of `(13.3.3)`; whence the conclusion.

**Proposition (13.3.8).**

<!-- label: IV.13.3.8 -->

*Let $Y$ be a prescheme, $f : X \to Y$ a morphism locally of finite type, $x$ a point of $X$. Let $Y'$ be a prescheme,
$g : Y' \to Y$ a flat morphism, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$; if $f$ is equidimensional at the
point $x$, then $f'$ is equidimensional at every point $x' \in X'$ above $x$.*

The question being local on $X$ and $Y$, one may restrict to the case where every irreducible component of $X$ (resp.
$Y$) contains $x$ (resp. $y$); since the image under $f$ of every irreducible component of $X$ is then dense in an
irreducible component of $Y$ `(13.3.1)`, one knows `(2.3.5)` that the image under $f'$ of every irreducible component of
$X'$ is dense in an irreducible component of $Y'$. On the other hand, by transitivity of fibres `(I, 3.6.4)`, it follows
from `(4.2.8)` and from `(13.3.1)` that, for every $z' \in X'$, the set of dimensions of the irreducible components of
$f'^{-1}(f'(z'))$ is the same as the set of dimensions of the irreducible components of $f^{-1}(f(z))$, where $z$ is the
projection of $z'$ in $X$; whence the conclusion by virtue of `(13.3.1, a)`.

**Remark (13.3.9).**

<!-- label: IV.13.3.9 -->

The equidimensionality property of a morphism $f : X \to Y$ is not stable under arbitrary base change $g : Y' \to Y$,
even when $g$ is the canonical injection of an irreducible component $Y'$ of $Y$ into $Y$ ($Y'$ being

<!-- original page 199 -->

considered as a reduced closed sub-prescheme of $Y$). For example, let $k$ be a field, $A_{0} = k[S, T]$ the polynomial
ring in two indeterminates, $\mathfrak{a} = \mathfrak{p}_{1} \mathfrak{p}_{2}$, where $\mathfrak{p}_{1}$ and
$\mathfrak{p}_{2}$ are the prime ideals $A_{0} S$ and $A_{0} T$ of `A_0`; let $A = A_{0}/\mathfrak{a}$ and $Y =
\operatorname{Spec}(A)$, which has two irreducible components $Y_{1} = \operatorname{Spec}(A/\mathfrak{p}_{1})$, $Y_{2}
= \operatorname{Spec}(A/\mathfrak{p}_{2})$; take $X = Y_{1}$, $f : X \to Y$ being the canonical injection, which is
evidently an equidimensional morphism. Take on the other hand $Y' = Y_{2}$, $g : Y' \to Y$ being the canonical
injection; then one has $X' = X \times_{Y} Y' = \operatorname{Spec}((A/\mathfrak{p}_{1}) \otimes_{A}
(A/\mathfrak{p}_{2})) = \operatorname{Spec}(A/(\mathfrak{p}_{1} + \mathfrak{p}_{2}))$, and $\mathfrak{p}_{1} +
\mathfrak{p}_{2}$ is a maximal ideal of $A$, hence $X'$ is reduced to a point, and the morphism $f' : X' \to Y'$ is *not
dominant*, the image under $f'$ of the unique point of $X'$ being a closed point of $Y'$; hence $f'$ is not
equidimensional.

One can also give a counterexample where $X$ and $Y$ are integral, $f$ finite and birational (and a fortiori
equidimensional by `(13.3.1, b)`), $g : Y' \to Y$ finite and dominant. Let $A$ and `Ā` be the local rings defined in
`(11.7.5)`, and take $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(\bar{A})$; on the other hand, with the
notations of `(11.7.5)`, take $Y' = \operatorname{Spec}(B)$; then $X' = \operatorname{Spec}(\bar{A} \otimes_{A} B) =
\operatorname{Spec}(\bar{B} \otimes_{B} B)$; but one verifies at once that $\bar{B} \otimes_{B} B$ is the direct
composite of the rings $\bar{B}/\mathfrak{p}'$, $\bar{B}/\mathfrak{p}''$ and of two rings isomorphic to
$\bar{B}/\mathfrak{n}$, whose spectra are therefore reduced to a point; since the projections of these points are closed
points of $Y'$, here again one sees that $f'$ does not transform an irreducible component of $X'$ into an everywhere
dense part of an irreducible component of $Y'$, hence $f'$ is not equidimensional.

In this example, the ring $A$ is not geometrically unibranch; we shall see in the following section `(14.4.6)` that such
phenomena cannot occur when the points of $Y$ are geometrically unibranch. The lack of stability of the notion of
equidimensional morphism greatly restricts its interest, in favour of the notion of universally open morphism, which
will be studied in detail in the following section.
