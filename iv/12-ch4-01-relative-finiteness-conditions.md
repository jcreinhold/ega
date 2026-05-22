<!-- original page 224 -->

## §1. Relative finiteness conditions. Constructible sets in preschemes

In this section we resume, in completed form, the exposition of the "finiteness conditions" for a morphism of preschemes
$f : X \to Y$ given in `(I, 6.3 and 6.6)`. There are essentially two notions of "finiteness" of *global* nature on $X$,
that of *quasi-compact* morphism (defined in `(I, 6.6.1)`) and that of *quasi-separated* morphism; there are on the
other hand two notions of "finiteness" of *local* nature on $X$, that of morphism *locally of finite type* (defined in
`(I, 6.6.2)`) and that of morphism *locally of finite presentation*. Combining these local notions with the preceding
global notions, one obtains the notions of morphism *of finite type* (defined in `(I, 6.3.1)`) and of morphism *of
finite presentation*. For the reader's convenience we shall give again, in this section, the principal properties stated
in `(I, 6.3 and 6.6)`, of course referring back to those numbers of Chapter I for their proofs.

In nos. (1.8) and (1.9) we complete, in the framework of preschemes and making use of the preceding finiteness notions,
the results on constructible sets given in `(0_III, §9)`.

### 1.1. Quasi-compact morphisms

**Definition (1.1.1).**

<!-- label: IV.1.1.1 -->

*We say that a morphism of preschemes $f : X \to Y$ is **quasi-compact** if the continuous map $f$ from the topological
space $X$ to the topological space $Y$ is quasi-compact $(0_{I}, 9.1.1)$, in other words if the inverse image
$f^{-1}(U)$ of every quasi-compact open set $U$ of $Y$ is quasi-compact (cf. `(I, 6.6.1)`).*

If $\mathfrak{B}$ is a base of the topology of $Y$ formed of affine open sets, then for $f$ to be quasi-compact it is
necessary and sufficient that for every $V \in \mathfrak{B}$, $f^{-1}(V)$ be a finite union of affine open sets. For
example, if $Y$ is affine and $X$ is quasi-compact, every morphism $f : X \to Y$ is quasi-compact `(I, 6.6.1)`.

If $f : X \to Y$ is a quasi-compact morphism, it is clear that for every open set $V$ of $Y$ the restriction of $f$ to
$f^{-1}(V)$ is a quasi-compact morphism $f^{-1}(V) \to V$. Conversely, if $(U_{\alpha})$ is an open cover of $Y$ and
$f : X \to Y$ is a morphism such that the restrictions $f^{-1}(U_{\alpha}) \to U_{\alpha}$ are quasi-compact, then $f$
is quasi-compact. Consequently, if $f : X \to Y$ is an $S$-morphism of $S$-preschemes and there exists an open cover
$(S_{\lambda})$ of $S$ such that the restrictions $g^{-1}(S_{\lambda}) \to h^{-1}(S_{\lambda})$ of $f$ (where $g$ and
$h$ are the structure morphisms) are quasi-compact, then $f$ is quasi-compact.

**Proposition (1.1.2).**

<!-- label: IV.1.1.2 -->

*(i) An immersion $X \to Y$ is quasi-compact if it is closed, or if the space underlying $Y$ is locally Noetherian, or
if the space underlying $X$ is Noetherian.*

*(ii) The composite of two quasi-compact morphisms is quasi-compact.*

*(iii) If $f : X \to Y$ is a quasi-compact $S$-morphism, then so is $f_{(S')} : X_{(S')} \to Y_{(S')}$ for every
extension $g : S' \to S$ of the base prescheme.*

*(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two quasi-compact $S$-morphisms,*

```text
  f ×_S g : X ×_S Y → X' ×_S Y'
```

*is quasi-compact.*

*(v) If the composite $g \circ f$ of two morphisms $f : X \to Y$, $g : Y \to Z$ is quasi-compact, and if $g$ is
separated, or the space underlying $X$ locally Noetherian, then $f$ is quasi-compact.*

*(vi) For a morphism $f$ to be quasi-compact, it is necessary and sufficient that $f_{red}$ be so.*

For the proof, see `(I, 6.6.4)`. We note that assertion (vi) is also a consequence of the more general proposition:

**Proposition (1.1.3).**

<!-- label: IV.1.1.3 -->

*Let $f : X \to Y$, $g : Y \to Z$ be two morphisms. If $g \circ f$ is quasi-compact and $f$ is surjective, then $g$ is
quasi-compact.*

Indeed, if $V$ is a quasi-compact open set in $Z$, $f^{-1}(g^{-1}(V))$ is quasi-compact by hypothesis, and one has
$g^{-1}(V) = f(f^{-1}(g^{-1}(V)))$, since $f$ is surjective; hence $g^{-1}(V)$ is quasi-compact.

<!-- original page 225 -->

**Corollary (1.1.4).**

<!-- label: IV.1.1.4 -->

*Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$; suppose $g$ is
quasi-compact and surjective (resp. surjective). Then, for $f$ to be quasi-compact (resp. dominant), it suffices that
$f'$ be so.*

If $g' : X' \to X$ is the canonical projection, $g'$ is a surjective morphism `(I, 3.5.2)`, and one has $f \circ g' = g
\circ f'$; if $f'$ is quasi-compact (resp. dominant), so is $g \circ f'$, since $g$ is quasi-compact `(1.1.2)` (resp.
surjective); since $f \circ g'$ is quasi-compact (resp. dominant) and $g'$ is surjective, one deduces from `(1.1.3)`
that $f$ is quasi-compact (resp. dominant).

To abbreviate, we shall call a **maximal point** of a prescheme $X$ any generic point of an irreducible component of
$X$; if $X = \operatorname{Spec}(A)$ is affine, the maximal points of $X$ are the *minimal* prime ideals of $A$.

**Proposition (1.1.5).**

<!-- label: IV.1.1.5 -->

*Let $f : X \to Y$ be a quasi-compact morphism. The following conditions are equivalent:*

*a) $f$ is dominant;*

*b) for every maximal point $y$ of $Y$, one has $f^{-1}(y) \neq \emptyset$;*

*c) for every maximal point $y$ of $Y$, $f^{-1}(y)$ contains a maximal point of $X$.*

The equivalence of a) and c) was proved in `(I, 6.6.5)`. It is clear that c) implies b); on the other hand, if $X'$ is
an irreducible component of $X$ meeting $f^{-1}(y)$, then $f(X')$ is irreducible and contains $y$, so it is contained in
the irreducible component $Y' = \overline{y}$ of $Y$ $(0_{I}, 2.1.6)$; if $x$ is the generic point of $X'$, one
therefore has necessarily $f(x) = y$ $(0_{I}, 2.1.5)$; hence b) implies c).

<!-- original page 226 -->

**Proposition (1.1.6).**

<!-- label: IV.1.1.6 -->

*Let $f' : X' \to Y$, $f'' : X'' \to Y$ be two morphisms, $X$ the sum prescheme $X' \amalg X''$, $f : X \to Y$ the
morphism equal to $f'$ on $X'$ and to `f''` on `X''`. For $f$ to be quasi-compact it is necessary and sufficient that
$f'$ and `f''` be so.*

This results immediately from the definition.

### 1.2. Quasi-separated morphisms

**Definition (1.2.1).**

<!-- label: IV.1.2.1 -->

*Let $X$, $Y$ be two preschemes. We say that a morphism $f : X \to Y$ is **quasi-separated** (or that $X$ is
**quasi-separated over $Y$**) if the diagonal morphism $\Delta_{f} = (1_{X}, 1_{X})_{Y} : X \to X \times_{Y} X$ is
quasi-compact. We say that a prescheme $X$ is **quasi-separated** if it is quasi-separated over
$\operatorname{Spec}(\mathbb{Z})$.*

By definition, every separated morphism is quasi-separated, $\Delta_{f}$ being a closed immersion `(1.1.2, (i))`; a
scheme $X$ is a quasi-separated prescheme, being separated over $\operatorname{Spec}(\mathbb{Z})$ `(I, 5.4.1)`.

**Proposition (1.2.2).**

<!-- label: IV.1.2.2 -->

*(i) Every monomorphism of preschemes $f : X \to Y$ (in particular, every immersion) is quasi-separated.*

*(ii) If $f : X \to Y$ and $g : Y \to Z$ are two quasi-separated morphisms, then $g \circ f : X \to Z$ is
quasi-separated.*

*(iii) Let $X$, $Y$ be two $S$-preschemes, $f : X \to Y$ a quasi-separated $S$-morphism. Then, for every base change
$g : S' \to S$, the morphism $f_{(S')} : X_{(S')} \to Y_{(S')}$ is quasi-separated.*

*(iv) If $f : X \to Y$, $f' : X' \to Y'$ are two quasi-separated $S$-morphisms, then*

```text
  f ×_S f' : X ×_S X' → Y ×_S Y'
```

*is quasi-separated.*

*(v) If $f : X \to Y$, $g : Y \to Z$ are two morphisms such that $g \circ f$ is quasi-separated, then $f$ is
quasi-separated.*

*(vi) If $f : X \to Y$ is a quasi-separated morphism, then `f_red : X_red → Y_red` is quasi-separated.*

By virtue of `(I, 5.5.12)`, it suffices to prove (i), (ii), and (iii).

Assertion (i) is trivial, every monomorphism being separated `(I, 5.5.1)`. To prove (iii), one reduces immediately to
the case where $Y = S$ `(I, 3.3.11)`, and the assertion results from the fact that $\Delta_{f'} = (\Delta_{f})_{(S')}$
`(I, 5.3.4)` and from `(1.1.2, (iii))`. To prove (ii), consider the projections $p$ and $q$ from $X \times_{Y} X$ onto
$X$; if $i = (p, q)_{Z}$, one knows that the diagram

```text
  X ×_Y X  ──i──→  X ×_Z X
    │                │
    π│              │f ×_Z f
    ↓                ↓
    Y    ──Δ_g──→  Y ×_Z Y
```

(where $\pi$ is the structure morphism) is commutative and identifies $X \times_{Y} X$ with the product of the $(Y
\times_{Z} Y)$-preschemes $Y$ and $X \times_{Z} X$ `(I, 5.3.5)`. If $g$ is quasi-separated, $\Delta_{g}$ is
quasi-compact,

<!-- original page 227 -->

so the same is true of $i$ `(1.1.2, (iii))`; if in addition $f$ is quasi-separated, $\Delta_{f}$ is quasi-compact, hence
so is $i \circ \Delta_{f}$ `(1.1.2, (ii))`, which is equal to $\Delta_{g \circ f}$.

**Corollary (1.2.3).**

<!-- label: IV.1.2.3 -->

*(i) Let $X$ be a quasi-separated prescheme. Then every morphism $f : X \to Y$ is quasi-separated.*

*(ii) Let $Y$ be a quasi-separated prescheme. For a morphism $f : X \to Y$ to be quasi-separated, it is necessary and
sufficient that the prescheme $X$ be quasi-separated.*

This results at once from `(1.2.2, (ii) and (v))` applied to $X$, $Y$, and $\operatorname{Spec}(\mathbb{Z})$.

**Proposition (1.2.4).**

<!-- label: IV.1.2.4 -->

*Let $f : X \to Y$ be a morphism, $g : Y \to Z$ a quasi-separated morphism. If $g \circ f$ is quasi-compact, then so is
$f$.*

One knows that $f$ is the composite morphism $X \xrightarrow{\Gamma_{f}} X \times_{Z} Y \xrightarrow{pr_{2}} Y$
`(I, 5.3.13)`; on the other hand, $pr_{2}$ identifies with $(g \circ f) \times_{Z} 1_{Y}$ `(I, 3.3.4)`, and if $g \circ
f$ is quasi-compact, then so is $pr_{2}$ `(1.1.2, (iv))`. Finally, one has the commutative diagram

```text
  X        ──Γ_f──→  X ×_Z Y                                    (1.2.4.1)
  │                    │
  f│                  │f × 1_Y
  ↓                    ↓
  Y        ──Δ_g──→  Y ×_Z Y
```

which identifies $X$ with the product of the $(Y \times_{Z} Y)$-preschemes $Y$ and $X \times_{Z} Y$ `(I, 5.3.7)`. Since
by hypothesis $\Delta_{g}$ is a quasi-compact morphism, so is $\Gamma_{f}$ `(1.1.2, (iii))`; the conclusion therefore
follows from `(1.1.2, (ii))`.

**Proposition (1.2.5).**

<!-- label: IV.1.2.5 -->

*Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. If $g$ is
quasi-compact and surjective and $f'$ is quasi-separated, then $f$ is quasi-separated.*

Indeed, one has $(X' \times_{Y'} X') = (X \times_{Y} X)_{(Y')}$ and $\Delta_{f'} = (\Delta_{f})_{(Y')}$ `(I, 5.3.4)`; as
the projection $X' \times_{Y'} X' \to X \times_{Y} X$ is quasi-compact `(1.1.2, (iii))` and surjective `(I, 3.5.2)`, one
may, by virtue of `(I, 3.3.11)`, apply `(1.1.4)`, which shows that since $\Delta_{f'}$ is a quasi-compact morphism, so
is $\Delta_{f}$.

**Proposition (1.2.6).**

<!-- label: IV.1.2.6 -->

*Let $f : X \to Y$ be a morphism, $(U_{\alpha})$ a cover of $Y$ by open sets such that the induced preschemes
$U_{\alpha}$ are quasi-separated. For $f$ to be quasi-separated it is necessary and sufficient that each of the
preschemes induced by $X$ on the open sets $f^{-1}(U_{\alpha})$ be quasi-separated.*

The inverse image in $X \times_{Y} X$ of $U_{\alpha}$ is $X_{\alpha} \times_{U_{\alpha}} X_{\alpha}$, where $X_{\alpha}
= f^{-1}(U_{\alpha})$, and the restriction $X_{\alpha} \to X_{\alpha} \times_{U_{\alpha}} X_{\alpha}$ of $\Delta_{f}$ is
none other than $\Delta_{f_{\alpha}}$, denoting by $f_{\alpha}$ the restriction $X_{\alpha} \to U_{\alpha}$ of $f$. By
virtue of definition `(1.2.1)` and of the local character of the notion of quasi-compact morphism `(1.1.1)`, for $f$ to
be quasi-separated it is necessary and sufficient that each of the morphisms $f_{\alpha}$ be so. But since by hypothesis
the morphism $U_{\alpha} \to \operatorname{Spec}(\mathbb{Z})$ is quasi-separated, to say that $f_{\alpha}$ is
quasi-separated is the same as to say that the composite $X_{\alpha} \xrightarrow{f_{\alpha}} U_{\alpha} \to
\operatorname{Spec}(\mathbb{Z})$ is so `(1.2.2, (ii) and (v))`, whence the proposition.

<!-- original page 228 -->

To check that a morphism is quasi-separated, one is therefore reduced to giving criteria for a prescheme to be
quasi-separated:

**Proposition (1.2.7).**

<!-- label: IV.1.2.7 -->

*Let $X$ be a prescheme, $(U_{\alpha})$ a cover of $X$ formed of quasi-compact open sets. The following properties are
equivalent:*

*a) $X$ is quasi-separated.*

*b) For every quasi-compact open set $U$ of $X$, the canonical immersion $U \to X$ is quasi-compact (in other words, $U$
is **retrocompact** in $X$).*

*b') The intersection of two quasi-compact open sets of $X$ is quasi-compact.*

*c) For every pair of indices $(\alpha, \beta)$, the intersection $U_{\alpha} \cap U_{\beta}$ is quasi-compact.*

Properties b) and b') are trivially equivalent by definition of a quasi-compact morphism. Since a quasi-compact open set
is a finite union of affine open sets, for two quasi-compact open sets $U$, $V$ of $X$, $U \times_{\mathbb{Z}} V$ is a
quasi-compact open set of $X \times_{\mathbb{Z}} X$ `(I, 3.2.7)`, whose inverse image under $\Delta_{X}$ is $U \cap V$;
hence a) implies b'). It is trivial that b') implies c); finally, if c) holds, the $U_{\alpha} \times_{\mathbb{Z}}
U_{\beta}$ form a cover of $X \times_{\mathbb{Z}} X$ by quasi-compact open sets, and one knows that for the morphism
$\Delta_{X} : X \to X \times_{\mathbb{Z}} X$ to be quasi-compact it suffices that the inverse images $U_{\alpha} \cap
U_{\beta}$ of the $U_{\alpha} \times_{\mathbb{Z}} U_{\beta}$ under $\Delta_{X}$ be quasi-compact `(1.1.1)`; hence c)
implies a).

**Corollary (1.2.8).**

<!-- label: IV.1.2.8 -->

*Every prescheme $X$ whose underlying space is locally Noetherian (for example, a locally Noetherian prescheme) is
quasi-separated; every morphism $f : X \to Y$ is then quasi-separated.*

**Proposition (1.2.9).**

<!-- label: IV.1.2.9 -->

*Let $X'$, `X''` be two preschemes, $X = X' \amalg X''$ their sum, $f' : X' \to Y$, $f'' : X'' \to Y$ two morphisms,
$f : X \to Y$ the morphism that coincides with $f'$ on $X'$ and with `f''` on `X''`. For $f$ to be quasi-separated it is
necessary and sufficient that $f'$ and `f''` be so.*

Indeed, $X \times_{Y} X$ is the sum of the four preschemes $X' \times_{Y} X'$, $X' \times_{Y} X''$, $X'' \times_{Y} X'$,
and $X'' \times_{Y} X''$, and $\Delta_{f}$ is the morphism that coincides with $\Delta_{f'}$ on $X'$ and with
$\Delta_{f''}$ on `X''`; the proposition therefore results at once from the definitions.

### 1.3. Morphisms locally of finite type

**(1.3.1)**

<!-- label: IV.1.3.1 -->

Recall that if $A$ is a ring, an (commutative) $A$-algebra $B$ is said to be **of finite type** if it is generated by a
finite number of elements of $B$, or — what amounts to the same — if it is isomorphic to a quotient of a polynomial
algebra $A[T_{1}, \cdots, T_{n}]$ by an ideal of that algebra. It is clear that for every (commutative) $A$-algebra
$A'$, $B \otimes_{A} A'$ is then an $A'$-algebra of finite type. If $B$ is an $A$-algebra of finite type and $C$ a
$B$-algebra of finite type, then $C$ is an $A$-algebra of finite type; for if $C$ is a quotient of $B[T_{1}, \cdots,
T_{n}]$ and $B$ a quotient of $A[S_{1}, \cdots, S_{m}]$, then $B[T_{1}, \cdots, T_{n}] = B \otimes_{A} A[T_{1}, \cdots,
T_{n}]$ is a quotient of $A[S_{1}, \cdots, S_{m}, T_{1}, \cdots, T_{n}]$, hence so is $C$.

**Definition (1.3.2).**

<!-- label: IV.1.3.2 -->

*Let $f : X \to Y$ be a morphism of preschemes, $x$ a point of $X$, $y = f(x)$. We say that $f$ is **of finite type at
$x$** if there exist an affine open neighbourhood $V$ of $y$ and an affine open neighbourhood $U$ of $x$ such that $f(U)
\subset V$ and the ring $A(U)$ is an $A(V)$-algebra of finite type. We say that $f$ is **locally of finite type** if it
is of finite type at every point of $X$.*

<!-- original page 229 -->

**Proposition (1.3.3).**

<!-- label: IV.1.3.3 -->

*If $Y$ is a locally Noetherian prescheme and $f : X \to Y$ a morphism locally of finite type, then $X$ is locally
Noetherian.*

For the proof, see `(I, 6.3.7)`.

**Proposition (1.3.4).**

<!-- label: IV.1.3.4 -->

*(i) Every local immersion is locally of finite type.*

*(ii) If two morphisms $f : X \to Y$, $g : Y \to Z$ are locally of finite type, then so is $g \circ f$.*

*(iii) If $f : X \to Y$ is an $S$-morphism locally of finite type, then $f_{(S')} : X_{(S')} \to Y_{(S')}$ is locally of
finite type for every extension $S' \to S$ of the base prescheme.*

*(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two $S$-morphisms locally of finite type, then $f \times_{S} g$ is
locally of finite type.*

*(v) If the composite $g \circ f$ of two morphisms is locally of finite type, then $f$ is locally of finite type.*

*(vi) If a morphism $f$ is locally of finite type, then so is $f_{red}$.*

For the proof, see `(I, 6.6.6)`.

**Corollary (1.3.5).**

<!-- label: IV.1.3.5 -->

*Let $f : X \to Y$ be a morphism locally of finite type. For every morphism $Y' \to Y$ such that $Y'$ is locally
Noetherian, $X \times_{Y} Y'$ is locally Noetherian.*

Indeed, $f_{(Y')} : X \times_{Y} Y' \to Y'$ is locally of finite type by `(1.3.4, (iii))`, and it suffices to apply
`(1.3.3)`.

**Proposition (1.3.6).**

<!-- label: IV.1.3.6 -->

*Let $\phi : A \to B$ be a ring homomorphism. For the corresponding morphism $f : \operatorname{Spec}(B) \to
\operatorname{Spec}(A)$ to be locally of finite type, it is necessary and sufficient that $B$ be an $A$-algebra of
finite type.*

For the proof, see `(I, 6.3.3)`, taking into account that $f$ is quasi-compact and that `(I, 6.6.3)` holds.

**Proposition (1.3.7).**

<!-- label: IV.1.3.7 -->

*For a morphism $f : X \to Y$ locally of finite type to be surjective, it is necessary and sufficient that for every
algebraically closed field $\Omega$ the map $X(\Omega) \to Y(\Omega)$ corresponding to $f$ `(I, 3.4.1)` be surjective.*

For the proof, see `(I, 6.3.10)`.

**(1.3.8)**

<!-- label: IV.1.3.8 -->

Let $A$ be a ring. We say that an $A$-algebra $B$ is **essentially of finite type** if $B$ is $A$-isomorphic to an
$A$-algebra of the form $S^{-1}C$, where $C$ is an $A$-algebra of finite type and $S$ a multiplicative subset of $C$.

**Proposition (1.3.9).**

<!-- label: IV.1.3.9 -->

*(i) If $B$ is an $A$-algebra essentially of finite type and $C$ a $B$-algebra essentially of finite type, then $C$ is
an $A$-algebra essentially of finite type.*

*(ii) Let $B$ be an $A$-algebra essentially of finite type, $A'$ an $A$-algebra; then $B' = B \otimes_{A} A'$ is an
$A'$-algebra essentially of finite type.*

(i) Let $B = S'^{-1}B'$ and $C = T'^{-1}C'$, where $B'$ (resp. $C'$) is an $A$-algebra (resp. a $B$-algebra) of finite
type and $S'$ (resp. $T'$) a multiplicative subset of $B'$ (resp. $C'$); then $C'$ is of the form $S'^{-1}C''$, where
`C''` is a $B'$-algebra of finite type, so $C$ is also a ring of fractions of `C''`; since `C''` is an $A$-algebra of
finite type, this proves our assertion.

(ii) If $B$ is a ring of fractions of an $A$-algebra of finite type $C$, then $B'$ is a ring of fractions of the
$A'$-algebra of finite type $C \otimes_{A} A'$, whence (ii).

<!-- original page 230 -->

**(1.3.10)**

<!-- label: IV.1.3.10 -->

If $B$ is a *local* $A$-algebra essentially of finite type, then $B$ is of the form $C_{\mathfrak{q}}$, where $C$ is an
$A$-algebra of finite type and $\mathfrak{q}$ a prime ideal of $C$ `(Bourbaki, Alg. comm., chap. II, §5, prop. 11)`. Let
$\mathfrak{p}$ be the inverse image in $A$ of the ideal $\mathfrak{q}$; setting $S = A - \mathfrak{p}$,
$C_{\mathfrak{q}}$ is also a local ring at a prime ideal of $S^{-1}C$; since $S^{-1}C$ is an algebra of finite type over
$A_{\mathfrak{p}} = S^{-1}A$, one sees that $B$ is also an $A_{\mathfrak{p}}$-algebra essentially of finite type, and in
addition the homomorphism $A_{\mathfrak{p}} \to B$ is local.

**Proposition (1.3.11).**

<!-- label: IV.1.3.11 -->

*If $B$ is a local $A$-algebra essentially of finite type, then $B$ is $A$-isomorphic to a quotient $A$-algebra of an
$A$-algebra of the form $C_{\mathfrak{q}}$, where $C$ is a polynomial algebra $A[T_{1}, \cdots, T_{n}]$ and
$\mathfrak{q}$ a prime ideal of $C$.*

Indeed, by definition, $B$ is isomorphic to $C'_{\mathfrak{q}'}$, where $C'$ is an $A$-algebra of finite type and
$\mathfrak{q}'$ a prime ideal of $C'$; but $C' = C/\mathfrak{b}$, where $C = A[T_{1}, \cdots, T_{n}]$ and $\mathfrak{b}$
is an ideal of $C$; so $\mathfrak{q}' = \mathfrak{q}/\mathfrak{b}$, where $\mathfrak{q}$ is a prime ideal of $C$, and
$C'_{\mathfrak{q}'}$ is isomorphic to $C_{\mathfrak{q}} / \mathfrak{b} C_{\mathfrak{q}}$.

### 1.4. Morphisms locally of finite presentation

**(1.4.1)**

<!-- label: IV.1.4.1 -->

Given a ring $A$, we shall say that an (commutative) $A$-algebra $B$ is **of finite presentation** if it is isomorphic
to the quotient $A[T_{1}, \cdots, T_{n}] / \mathfrak{a}$ of a polynomial algebra over $A$ by an *ideal of finite type*
$\mathfrak{a}$ of $A[T_{1}, \cdots, T_{n}]$. For every (commutative) $A$-algebra $A'$, $B \otimes_{A} A'$ is then an
$A'$-algebra of finite presentation, being isomorphic to the quotient of $A'[T_{1}, \cdots, T_{n}]$ by the canonical
image in this ring of $\mathfrak{a} \otimes_{A} A'$, which is manifestly an $A'[T_{1}, \cdots, T_{n}]$-module of finite
type. If $B$ is an $A$-algebra of finite presentation and $C$ a $B$-algebra of finite presentation, then $C$ is an
$A$-algebra of finite presentation. Indeed, let $B = A[S_{1}, \cdots, S_{m}] / \mathfrak{a}$ and $C = B[T_{1}, \cdots,
T_{n}] / \mathfrak{b}$, where $\mathfrak{a}$ (resp. $\mathfrak{b}$) is an ideal of finite type of $A[S_{1}, \cdots,
S_{m}]$ (resp. of $B[T_{1}, \cdots, T_{n}]$); the ring $B[T_{1}, \cdots, T_{n}]$ is isomorphic to $A[S_{1}, \cdots,
S_{m}, T_{1}, \cdots, T_{n}] / \mathfrak{a}'$, where $\mathfrak{a}'$ is the canonical image of $\mathfrak{a} \otimes_{A}
A[T_{1}, \cdots, T_{n}]$, and is therefore an ideal of finite type of $A[S_{1}, \cdots, S_{m}, T_{1}, \cdots, T_{n}]$;
the ideal $\mathfrak{b}$ of $B[T_{1}, \cdots, T_{n}]$ is of the form $\mathfrak{b}'/\mathfrak{a}'$, where
$\mathfrak{b}'$ is an ideal of $A[S_{1}, \cdots, S_{m}, T_{1}, \cdots, T_{n}]$; since $\mathfrak{a}'$ and
$\mathfrak{b}'/\mathfrak{a}'$ are modules of finite type over $A[S_{1}, \cdots, S_{m}, T_{1}, \cdots, T_{n}]$, so is
$\mathfrak{b}'$, and $C$, isomorphic to $A[S_{1}, \cdots, S_{m}, T_{1}, \cdots, T_{n}] / \mathfrak{b}'$, is therefore an
$A$-algebra of finite presentation. Note finally that if $A$ is Noetherian, then so is $A[T_{1}, \cdots, T_{n}]$, so
every $A$-algebra of finite type is then of finite presentation.

**Definition (1.4.2).**

<!-- label: IV.1.4.2 -->

*Let $f : X \to Y$ be a morphism of preschemes, $x$ a point of $X$, $y = f(x)$. We say that $f$ is **of finite
presentation at $x$** if there exist an affine open neighbourhood $V$ of $y$ and an affine open neighbourhood $U$ of $x$
such that $f(U) \subset V$ and the ring $A(U)$ is an $A(V)$-algebra of finite presentation. We say that $f$ is **locally
of finite presentation** if it is of finite presentation at every point of $X$.*

If $Y$ is locally Noetherian, to say that $f$ is locally of finite type and to say that $f$ is locally of finite
presentation are equivalent.

**Proposition (1.4.3).**

<!-- label: IV.1.4.3 -->

*(i) Every local isomorphism is locally of finite presentation.*

*(ii) If two morphisms $f : X \to Y$, $g : Y \to Z$ are locally of finite presentation, then so is $g \circ f$.*

<!-- original page 231 -->

*(iii) If $f : X \to Y$ is an $S$-morphism locally of finite presentation, then $f_{(S')} : X_{(S')} \to Y_{(S')}$ is
locally of finite presentation for every extension $S' \to S$ of the base prescheme.*

*(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two $S$-morphisms locally of finite presentation, then $f \times_{S} g$
is locally of finite presentation.*

*(v) If the composite $g \circ f$ of two morphisms is locally of finite presentation and if $g$ is locally of finite
type, then $f$ is locally of finite presentation.*

Assertion (i) is trivial. To prove (iii) one may restrict to the case where $S = Y$ `(I, 3.3.11)`; let $x'$ be a point
of $X_{(S')}$, and $s'$, $x$ its projections onto $S'$ and $X$ respectively, $s$ the common projection of $s'$ and $x$
onto $S$. By hypothesis there is an affine open neighbourhood $V$ (resp. $U$) of $s$ (resp. $x$) such that the image of
$U$ is contained in $V$ and $A(U)$ is an $A(V)$-algebra of finite presentation; let $V'$ be an affine open neighbourhood
of $s'$ whose image in $S$ is contained in $V$; then $U \times_{V} V'$ is an affine open neighbourhood of $x'$ whose
image in $S'$ is contained in $V'$, and whose ring $A(U) \otimes_{A(V)} A(V')$ is an $A(V')$-algebra of finite
presentation `(1.4.1)`.

To prove (ii), consider a point $x \in X$, and let $y = f(x)$, $z = g(f(x))$. By hypothesis there is an affine open
neighbourhood $W = \operatorname{Spec}(C)$ (resp. $V = \operatorname{Spec}(B)$) of $z$ (resp. $y$) such that $g(V)
\subset W$ and $B$ is a $C$-algebra of finite presentation. On the other hand, there is an affine open neighbourhood $V'
= \operatorname{Spec}(B')$ (resp. $U = \operatorname{Spec}(A)$) of $y$ (resp. $x$) such that $f(U) \subset V'$ and $A$
is a $B'$-algebra of finite presentation. Let $s \in B$ be such that the open set $D(s) = \operatorname{Spec}(B_{s})$ in
$V$ is a neighbourhood of $y$ contained in $V'$, and let $U' = f^{-1}(D(s)) \subset U$; one has $U' =
\operatorname{Spec}(A \otimes_{B'} B_{s})$, and $A \otimes_{B'} B_{s}$ is a $B_{s}$-algebra of finite presentation
`(1.4.1)`; on the other hand, $B_{s} = B[T] / (1 - sT)$ is a $B$-algebra of finite presentation by definition;
consequently `(1.4.1)`, $A \otimes_{B'} B_{s}$ is a $C$-algebra of finite presentation, which proves (ii).

One knows that (iv) results from (i), (ii), and (iii) `(I, 3.5.1)`. To prove (v), consider the commutative diagram

```text
  X        ──Γ_f──→  X ×_Z Y
  │                    │
  f│                  │f × 1
  ↓                    ↓
  Y        ──Δ_g──→  Y ×_Z Y
```

which identifies $X$ with the product of the $(Y \times_{Z} Y)$-preschemes $Y$ and $X \times_{Z} Y$ `(I, 5.3.7)`,
$\Delta_{g}$ being the diagonal morphism. If we know that $\Delta_{g}$ is locally of finite presentation, it will follow
from (iii) that the same is true of $\Gamma_{f}$. On the other hand, one has the factorization of $f$ as $X
\xrightarrow{\Gamma_{f}} X \times_{Z} Y \xrightarrow{p_{2}} Y$ `(I, 5.3.13)`, where the projection $p_{2}$ is equal to
$(g \circ f) \times_{Z} 1_{Y}$; since $g \circ f$ is supposed locally of finite presentation, so is $p_{2}$ by (iv), and
it will finally result from (ii) that $f$ too is locally of finite presentation. One sees therefore that one is reduced
to proving:

**Corollary (1.4.3.1).**

<!-- label: IV.1.4.3.1 -->

*Let $g : Y \to Z$ be a morphism locally of finite type; then the diagonal morphism $\Delta_{g} : Y \to Y \times_{Z} Y$
is locally of finite presentation.*

<!-- original page 232 -->

One may restrict to the case where $Z = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(B)$, $B$ being an $A$-algebra
of finite type; the morphism $\Delta_{g}$ then corresponds to the *augmentation homomorphism* $\delta : B \otimes_{A} B
\to B$ such that $\delta(x \otimes y) = xy$. In view of definition `(1.4.2)`, it suffices to show that the kernel
$\mathfrak{J}$ of $\delta$ is an ideal of finite type, which results from $(0_{IV}, 20.4.4)$.

**Proposition (1.4.4).**

<!-- label: IV.1.4.4 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $B'$ a polynomial algebra $A[T_{1}, \cdots, T_{n}]$, $u : B' \to B$ a surjective
homomorphism of $A$-algebras. For $B$ to be an $A$-algebra of finite presentation it is necessary and sufficient that
the kernel $\mathfrak{J}$ of $u$ be an ideal of finite type of $B'$.*

The condition is sufficient by definition `(1.4.1)`. To see that it is necessary, remark that the morphism $g :
\operatorname{Spec}(B') \to \operatorname{Spec}(A)$ is locally of finite type; if $B$ is an $A$-algebra of finite
presentation, the morphism $f : \operatorname{Spec}(B) \to \operatorname{Spec}(B')$ corresponding to $u$ is such that $g
\circ f : \operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is locally of finite presentation, so it results from
`(1.4.3, (v))` that $f$ is also locally of finite presentation. Now, to show that the ideal $\mathfrak{J}$ is of finite
type, it suffices to prove that $\tilde{\mathfrak{J}}$ is a $\tilde{B}'$-Module of finite type `(II, 6.1.4.1)`.
Returning to definition `(1.4.2)`, one is finally reduced to proving:

**Lemma (1.4.4.1).**

<!-- label: IV.1.4.4.1 -->

*Let $\mathfrak{a}$ be an ideal of a ring $C$, $s$ an element of $C$, such that $C_{s} / \mathfrak{a}_{s}$ is a
$C$-algebra of finite presentation; then $\mathfrak{a}_{s}$ is an ideal of finite type in the ring $C_{s}$.*

By hypothesis, there exist a polynomial $C$-algebra $C' = C[T_{1}, \cdots, T_{n}]$ and a surjective $C$-homomorphism
$v : C' \to C_{s} / \mathfrak{a}_{s}$ whose kernel $\mathfrak{b}$ is of finite type. Let
$p : C_{s} \to C_{s} / \mathfrak{a}_{s}$ be the canonical homomorphism; for each $i$ there is a $t_{i} \in C$ such that
$p(t_{i} / s^{k}) = v(T_{i})$ (one may suppose the exponent $k$ is the same for all indices $i$). Consider then the
$C_{s}$-algebra $D = C_{s}[T_{1}, \cdots, T_{n}]$, and the homomorphism of $C_{s}$-algebras $w : D \to C_{s}$ such that
$w(T_{i}) = t_{i} / s^{k}$; $w$ is manifestly surjective, and consequently so is
$v' = p \circ w : D \to C_{s} / \mathfrak{a}_{s}$. On the other hand, every polynomial in $D$ may be written
$P / s^{m}$, where $P \in C' = C[T_{1}, \cdots, T_{n}]$, and one has $v'(P / s^{m}) = (1 / s^{m}) v(P)$; since $1 / s$
is invertible in $C_{s}$, the relation $v'(P / s^{m}) = 0$ in $C_{s} / \mathfrak{a}_{s}$ is equivalent to $v(P) = 0$,
and consequently the kernel $\mathfrak{b}'$ of $v'$ is generated by the canonical image of $\mathfrak{b}$ in $D$, and *a
fortiori* is of finite type in the ring $D$. But
$\mathfrak{b}' = v'^{-1}(0) = w^{-1}(p^{-1}(0)) = w^{-1}(\mathfrak{a}_{s})$, and since $w$ is surjective,
$\mathfrak{a}_{s} = w(\mathfrak{b}')$, which proves that $\mathfrak{a}_{s}$ is an ideal of finite type of $C_{s}$.

**Corollary (1.4.5).**

<!-- label: IV.1.4.5 -->

*Let $X$, $Y$ be two preschemes, $j : X \to Y$ an immersion, $U$ an open set of $Y$ such that $j(X)$ is closed in $U$,
$\mathcal{J}$ the quasi-coherent Ideal of $\mathcal{O}_{U}$ defining the closed subprescheme of $U$ associated with $j$.
For $j$ to be locally of finite presentation it is necessary and sufficient that $\mathcal{J}$ be an
$\mathcal{O}_{U}$-Module of finite type.*

**Proposition (1.4.6).**

<!-- label: IV.1.4.6 -->

*Let $\phi : A \to B$ be a ring homomorphism. For the corresponding morphism $f : \operatorname{Spec}(B) \to
\operatorname{Spec}(A)$ to be locally of finite presentation, it is necessary and sufficient that $B$ be an $A$-algebra
of finite presentation.*

The condition being trivially sufficient, it remains to prove that it is necessary. If $f$ is locally of finite
presentation, it already follows from `(1.3.6)` that $B$ is an $A$-algebra of finite type, so there exists a surjective
homomorphism $u : B' = A[T_{1}, \cdots, T_{n}] \to B$ of $A$-algebras; it results from `(1.4.3, (v))` that the immersion
$j : \operatorname{Spec}(B) \to \operatorname{Spec}(B')$ is locally

<!-- original page 233 -->

of finite presentation; therefore `(1.4.5)`, if $\mathfrak{J}$ is the kernel of $u$, the $\tilde{B}'$-Module
$\tilde{\mathfrak{J}}$ is of finite type, and consequently `(II, 6.1.4.1)` $\mathfrak{J}$ is an ideal of finite type.

**Proposition (1.4.7).**

<!-- label: IV.1.4.7 -->

*Let $\rho : A \to B$ be a ring homomorphism making $B$ into a finite $A$-algebra. For $B$ to be an $A$-algebra of
finite presentation it is necessary and sufficient that $B$ be an $A$-module of finite presentation.*

We will use:

**Lemma (1.4.7.1).**

<!-- label: IV.1.4.7.1 -->

*If $B$ is a finite $A$-algebra, there exists a surjective $A$-homomorphism of algebras $u : B' \to B$, where $B'$ is a
finite $A$-algebra and of finite presentation which is a free $A$-module.*

Indeed, there is a finite system $(a_{i})_{1 \leq i \leq m}$ of generators of the $A$-algebra $B$ such that each $a_{i}$
satisfies a relation $F_{i}(a_{i}) = 0$, where $F_{i} \in A[X]$ is a unitary polynomial of degree `> 0`; the quotient
$A$-algebra $B'_{i} = A[X] / (F_{i})$ is therefore free of finite rank over $A$; let $c_{i}$ be the class of $X$ in
$B'_{i}$. There exists an $A$-homomorphism of algebras $u_{i} : B'_{i} \to B$ such that $u_{i}(c_{i}) = a_{i}$; it then
suffices to take for $B'$ the tensor product $B'_{1} \otimes_{A} B'_{2} \otimes \cdots \otimes_{A} B'_{m}$, and to
consider the homomorphism $u_{1} \otimes u_{2} \otimes \cdots \otimes u_{m} : B' \to B$, which is surjective by
construction. Moreover, if $B'' = A[T_{1}, \cdots, T_{m}]$ and if $b'_{i}$ denotes the canonical image of $c_{i}$ in
$B'$, the $A$-homomorphism of algebras $v : B'' \to B'$ such that $v(T_{i}) = b'_{i}$ ($1 \leq i \leq m$) is surjective,
and its kernel $\mathfrak{b}'$ is the ideal of `B''` generated by the $F_{i}(T_{i})$, hence of finite type; this proves
that $B'$ is an $A$-algebra of finite presentation.

This lemma being proved, keep the same notations and let $w = v \circ u : B'' \to B$. If $\mathfrak{b}$ (resp.
$\mathfrak{a}$) is the kernel of $w$ (resp. $u$), one has $\mathfrak{a} = v(\mathfrak{b})$ since $v$ is surjective. Now
`(1.4.4)`, if $B$ is an $A$-algebra of finite presentation, $\mathfrak{b}$ is an ideal of finite type of `B''`, so
$\mathfrak{a}$ is an ideal of finite type of $B'$, hence an $A$-module of finite type since $B'$ is a finite
$A$-algebra; since $B'$ is a free $A$-module, $B$ is an $A$-module of finite presentation. Conversely, if $B$ is an
$A$-module of finite presentation, $\mathfrak{a}$ is an $A$-module of finite type
`(Bourbaki, Alg. comm., chap. I, §2, n° 8, lemme 9)`, and *a fortiori* an ideal of finite type of $B'$; consequently,
$B$ is by definition a $B'$-algebra of finite presentation, and since $B'$ is an $A$-algebra of finite presentation, $B$
is an $A$-algebra of finite presentation.

### 1.5. Morphisms of finite type

**Proposition (1.5.1).**

<!-- label: IV.1.5.1 -->

*Let $f : X \to Y$ be a morphism, $(U_{\alpha})$ a cover of $Y$ formed of affine open sets. The following conditions are
equivalent:*

*a) $f$ is locally of finite type and quasi-compact.*

*b) For every $\alpha$, $f^{-1}(U_{\alpha})$ is a finite union of affine open sets $V_{\alpha i}$ such that each ring
$A(V_{\alpha i})$ is an $A(U_{\alpha})$-algebra of finite type.*

*c) For every affine open set $U$ of $Y$, $f^{-1}(U)$ is a finite union of affine open sets $V_{i}$ such that the rings
$A(V_{i})$ are $A(U)$-algebras of finite type.*

For the proof, see `(I, 6.3.2 and 6.6.3)`.

**Definition (1.5.2).**

<!-- label: IV.1.5.2 -->

*We say that a morphism $f$ is **of finite type** if it satisfies the equivalent conditions of proposition `(1.5.1)`.*

<!-- original page 234 -->

**Proposition (1.5.3).**

<!-- label: IV.1.5.3 -->

*Let $f : X \to Y$ be a morphism of finite type; if $Y$ is Noetherian, then so is $X$.*

For the proof, see `(I, 6.3.7)`.

**Proposition (1.5.4).**

<!-- label: IV.1.5.4 -->

*(i) Let $j : X \to Y$ be a morphism of immersion. If $j$ is quasi-compact (which is the case if $j$ is a closed
immersion, or if the space underlying $X$ is Noetherian, or if the space underlying $Y$ is locally Noetherian), then $j$
is of finite type.*

*(ii) The composite of two morphisms of finite type is of finite type.*

*(iii) If $f : X \to Y$ is an $S$-morphism of finite type, then $f_{(S')} : X_{(S')} \to Y_{(S')}$ is of finite type for
every extension $S' \to S$ of the base prescheme.*

*(iv) If $f : X \to X'$ and $g : Y \to Y'$ are two $S$-morphisms of finite type, then $f \times_{S} g$ is of finite
type.*

*(v) If the composite $g \circ f$ of two morphisms is of finite type, and if $g$ is quasi-separated or $X$ is
Noetherian, then $f$ is of finite type.*

*(vi) If a morphism $f$ is of finite type, then so is $f_{red}$.*

This results at once (except case (v) where $X$ is Noetherian, proved in `(I, 6.3.6)`) from the definitions and from
`(1.1.2)`, `(1.2.4)`, and `(1.3.4)`.

**Corollary (1.5.5).**

<!-- label: IV.1.5.5 -->

*Let $f : X \to Y$ be a morphism of finite type. For every morphism $Y' \to Y$ such that $Y'$ is Noetherian, $X
\times_{Y} Y'$ is Noetherian.*

This results from `(1.5.4, (iii))` and from `(1.5.3)`.

**Corollary (1.5.6).**

<!-- label: IV.1.5.6 -->

*Let $X$ be a prescheme of finite type over a locally Noetherian prescheme $S$. Then every $S$-morphism $f : X \to Y$ is
of finite type.*

For the proof, see `(I, 6.3.9)`.

**Proposition (1.5.7).**

<!-- label: IV.1.5.7 -->

*Let $\phi : A \to B$ be a ring homomorphism. For the corresponding morphism $f : \operatorname{Spec}(B) \to
\operatorname{Spec}(A)$ to be of finite type, it is necessary and sufficient that $\phi$ make $B$ into an $A$-algebra of
finite type.*

For the proof, see `(I, 6.3.3)`.

### 1.6. Morphisms of finite presentation

**Definition (1.6.1).**

<!-- label: IV.1.6.1 -->

*Let $X$, $Y$ be two preschemes. We say that a morphism $f : X \to Y$ is **of finite presentation** if it satisfies the
three following conditions:*

*(i) $f$ is locally of finite presentation;*

*(ii) $f$ is quasi-compact (which, when (i) is satisfied, is equivalent to saying that $f$ is of finite type
`(1.5.2)`);*

*(iii) $f$ is quasi-separated.*

*We say in this case that $X$ is **of finite presentation over $Y$**, or a **$Y$-prescheme of finite presentation**.*

Condition (iii) is automatically satisfied if $f$ is separated, or if $X$ is locally Noetherian `(1.2.8)`; when $Y$ is
locally Noetherian, to say that $f$ is of finite presentation and to say that $f$ is of finite type are equivalent (the
latter condition implying that $X$ is locally Noetherian `(1.3.3)`).

<!-- original page 235 -->

**Proposition (1.6.2).**

<!-- label: IV.1.6.2 -->

*(i) Every quasi-compact immersion locally of finite presentation (in particular, every quasi-compact open immersion) is
of finite presentation.*

*(ii) The composite of two morphisms of finite presentation is of finite presentation.*

*(iii) Let $X$, $Y$ be two $S$-preschemes, $f : X \to Y$ an $S$-morphism of finite presentation. Then, for every
morphism $S' \to S$, the morphism $f_{(S')} : X_{(S')} \to Y_{(S')}$ is of finite presentation.*

*(iv) Let $f : X \to Y$, $f' : X' \to Y'$ be two $S$-morphisms of finite presentation; then $f \times_{S} f' : X
\times_{S} X' \to Y \times_{S} Y'$ is of finite presentation.*

*(v) If the composite $g \circ f$ of two morphisms is of finite presentation, and if $g$ is quasi-separated and locally
of finite presentation, then $f$ is of finite presentation.*

This results immediately from `(1.1.2)`, `(1.2.2)`, `(1.2.4)`, and `(1.4.3)`.

It follows in particular from `(1.6.2, (iii))` that if $f$ is a morphism of finite presentation and $U$ an open set of
$Y$, the restriction $f^{-1}(U) \to U$ of $f$ is a morphism of finite presentation. Conversely, let $(U_{\alpha})$ be a
cover of $Y$ by affine open sets, and suppose that the restrictions $f^{-1}(U_{\alpha}) \to U_{\alpha}$ of $f$ are
morphisms of finite presentation; it then follows that $f$ is of finite presentation, since $f$ is manifestly locally of
finite presentation, quasi-compact by virtue of `(1.1.1)`, and quasi-separated by virtue of `(1.2.6)`. One may therefore
say that the property of a morphism $f : X \to Y$ of being of finite presentation is *local on $Y$*.

If $X$ is a quasi-separated prescheme, every morphism $f : X \to Y$ is quasi-separated `(1.2.3)`. Therefore, if $f$ is
quasi-compact and locally of finite presentation, $f$ is then of finite presentation.

In particular:

**Corollary (1.6.3).**

<!-- label: IV.1.6.3 -->

*Let $\phi : A \to B$ be a ring homomorphism. For the corresponding morphism $f : \operatorname{Spec}(B) \to
\operatorname{Spec}(A)$ to be of finite presentation, it is necessary and sufficient that $\phi$ make $B$ into an
$A$-algebra of finite presentation.*

The necessity of the condition results from `(1.4.6)`.

**Remark (1.6.4).**

<!-- label: IV.1.6.4 -->

In definition `(1.6.1)`, condition (iii) is not a consequence of the two others. Let, for example, $Y$ be an affine
scheme whose underlying space is not Noetherian, and let $U$ be a non-quasi-compact open set in $Y$. Let $X$ be the
prescheme obtained by gluing two preschemes `Y_1`, `Y_2` isomorphic to $Y$ along the open sets `U_1`, `U_2`
corresponding to $U$ $(0_{I}, 4.1.7)$, so that $X$ is a union of two open sets isomorphic respectively to `Y_1` and
`Y_2` (and which we identify with these), with $Y_{1} \cap Y_{2} = U$. In addition, there is a morphism $f : X \to Y$
that coincides on $Y_{i}$ with the given isomorphism $Y_{i} \to Y$ ($i = 1, 2$). It is clear that $f$ satisfies
condition (i) of `(1.6.1)`, being a local isomorphism; it also satisfies (ii), the inverse image of a quasi-compact open
set of $Y$ being the union of its images in `Y_1` and `Y_2`; but as $Y_{1} \cap Y_{2}$ is not quasi-compact, $f$ is not
quasi-separated `(1.2.7)`.

**Proposition (1.6.5).**

<!-- label: IV.1.6.5 -->

*Let $X'$, `X''` be two preschemes, $X = X' \amalg X''$ their sum, $f' : X' \to Y$, $f'' : X'' \to Y$ two morphisms,
$f : X \to Y$ the morphism that coincides with $f'$ on $X'$ and with `f''` on `X''`. For $f$ to be of finite
presentation it is necessary and sufficient that $f'$ and `f''` be so.*

It suffices to show that for $f$ to possess one of the three properties of definition

<!-- original page 236 -->

`(1.6.1)`, it is necessary and sufficient that $f'$ and `f''` possess it; this is clear for the property of being
locally of finite presentation, which is local on $X$; for the property of being quasi-compact, this was seen in
`(1.1.6)`, and for the property of being quasi-separated, in `(1.2.9)`.

### 1.7. Improvements of earlier results

We give in this number a list of propositions proved in the preceding chapters whose statement may be improved by means
of the new finiteness conditions introduced above.

**(1.7.1)** In the statements of `(I, 6.4.2, 6.4.3, and 6.4.9)`, one may, instead of supposing that $X$ and $Y$ are of
finite type over the field $K$, suppose only that they are *locally of finite type* over $K$; for `(I, 6.4.2)`, it
suffices to observe that every point of a prescheme $X$ which is closed in every affine open set of $X$ is closed in
$X$, and an affine scheme locally of finite type over $K$ is *ipso facto* of finite type `(1.5.1)`. For `(I, 6.4.9)`,
one uses `(1.3.7)` and `(1.3.4, (v))`.

**(1.7.2)** In `(I, 6.5.1, (ii))`, one may, instead of supposing that $S$ is locally Noetherian and $Y$ of finite type
over $S$, suppose only that $Y$ is *locally of finite presentation* over $S$, as the proof immediately shows (applying
definition `(1.4.2)`). Similarly, in `(I, 6.5.4, (ii))` and `(I, 6.5.5, (ii))` it suffices to suppose that $f$ is an
$S$-morphism, $Y$ being locally of finite presentation over $S$.

**(1.7.3)** In `(I, 7.1.11)`, for the second assertion, instead of supposing $S$ locally Noetherian and $Y$ of finite
type over $S$, one may suppose only $Y$ locally of finite presentation over $S$ (the proof depending on
`(I, 6.5.1, (ii))`); similarly in `(I, 7.1.12 to 7.1.15)`.

**(1.7.4)** In `(I, 9.2.2)`, one may replace the three hypotheses by the single hypothesis (entailed by each of the
others) that $f$ is *quasi-compact and quasi-separated*, by virtue of `(1.2.6)` and `(1.2.7)`. Note that in
`(I, 9.2.1)`, the hypothesis means exactly that $f$ is quasi-compact and quasi-separated.

**(1.7.5)** In `(I, 9.3.1, 9.3.2, and 9.3.3)`, one may replace the two hypotheses on $X$ by the hypothesis (less
restrictive) that $X$ is a *quasi-compact and quasi-separated* prescheme, the proof using exactly these two properties
(by virtue of `(1.2.7)`).

**(1.7.6)** In `(I, 9.3.4 and 9.3.5)`, it suffices to suppose $X$ quasi-compact, and $\mathcal{F}$ and $\mathcal{J}$
quasi-coherent and of finite type.

**(1.7.7)** In `(I, 9.4.7)`, one may weaken hypothesis b) by supposing only $X$ *quasi-separated*, since it suffices
only that the canonical immersion $U \to X$ be quasi-compact `(1.2.7)`. One may make the same modification in
`(I, 9.4.8, 9.4.9, and 9.4.10)`.

**(1.7.8)** In `(I, 9.5.1)`, the conditions indicated in parentheses in the statement may be replaced by the condition
that $f$ be quasi-compact and quasi-separated.

**(1.7.9)** In `(I, 9.6.5)`, one may replace the hypotheses on $X$ by the less restrictive hypothesis that $X$ is
*quasi-compact and quasi-separated*, as the proof shows, since it

<!-- original page 237 -->

uses only `(I, 9.4.7)`. In `(I, 9.6.6)`, the hypothesis "$X$ is a quasi-compact scheme" may be replaced by "$X$ is a
quasi-compact and quasi-separated prescheme".

**(1.7.10)** In `(II, 1.7.15)`, one may suppose only that $Y$ is quasi-compact and quasi-separated, the proof using only
`(I, 9.6.5)`.

**(1.7.11)** In the second assertion of `(II, 3.4.5)`, one may substitute for the two hypotheses on $Y$ the weaker
hypothesis that $Y$ is quasi-compact and quasi-separated. Similarly in `(II, 3.4.8)`.

**(1.7.12)** In `(II, 3.8.5)`, one may likewise suppose only that $Y$ is quasi-compact and quasi-separated, this
hypothesis intervening through `(I, 9.4.7)`.

**(1.7.13)** In `(II, 4.4.1, 4.4.6, and 4.4.7)`, it suffices to suppose that $Y$ is *quasi-compact and quasi-separated*,
taking account of `(1.2.3)` in the proof of `(II, 4.4.7)`. Similarly, in `(II, 4.4.10.1)`, it suffices to suppose $Z$
quasi-compact and quasi-separated.

**(1.7.14)** In `(II, 4.5.2)` and `(II, 4.5.5)`, it suffices to suppose $X$ *quasi-compact and quasi-separated*, this
hypothesis intervening through `(I, 9.3.1 and 9.3.2)`.

**(1.7.15)** In `(II, 4.6.8)`, it again suffices to suppose $X$ *quasi-compact and quasi-separated*, this hypothesis
intervening through `(I, 9.4.7)`.

**(1.7.16)** In `(II, 5.1.2)`, it suffices to suppose that $X$ is quasi-compact and quasi-separated (the hypothesis
intervening through `(II, 4.5.2 and 4.5.5)`). Similarly in `(II, 5.1.9)`, where one uses `(I, 9.6.5)`.

**(1.7.17)** In `(II, 5.2.1)`, it again suffices to suppose $X$ quasi-compact and quasi-separated (the hypothesis
intervening through `(II, 4.5.2)`).

**(1.7.18)** In `(II, 5.2.2)`, one must suppose $f$ quasi-compact and $X$ quasi-separated; the present proof is in fact
insufficient (with the hypotheses made), for from the fact that for every quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ one has $R^{1} f_{*}(\mathcal{F}) = 0$, it does not necessarily follow, for an affine open set $U$ of $Y$,
that the same property holds for the quasi-coherent $(\mathcal{O}_{X} | f^{-1}(U))$-Modules, if one does not know that
such a Module is the *restriction* of a quasi-coherent $\mathcal{O}_{X}$-Module (the same remark applying to conditions
b) and c')); when $f$ is quasi-compact and $X$ quasi-separated, this extension is possible by virtue of `(I, 9.4.7)`,
modified above `(1.7.7)`.

**(1.7.19)** In `(II, 5.3.2)`, it suffices to suppose $Y$ quasi-compact and quasi-separated (which intervenes through
`(II, 4.4.6 and 4.4.7)`). Similarly in `(II, 5.5.3, (ii))`.

**(1.7.20)** In `(III, 1.2.2, 1.2.3, and 1.2.4)`, one may replace the two hypotheses on $X$ by the less restrictive
hypothesis that $X$ is a quasi-compact and quasi-separated prescheme, the proof using only `(I, 9.3.3)`.

**(1.7.21)** In `(III, 1.4.10 to 1.4.14)`, one may replace "separated" by "quasi-separated", this hypothesis serving
only to allow application of `(I, 9.2.2)` (see above `(1.7.4)`). Similarly, in `(III, 1.4.15)`, it suffices to suppose
that the morphism $u$ is quasi-separated and quasi-compact.

**(1.7.22)** In `(III, 2.1.3)`, one may again replace the hypotheses by the less restrictive hypothesis that $X$ is a
quasi-compact and quasi-separated prescheme, the reasoning being the same as in `(III, 1.2.2)`.

<!-- original page 238 -->

### 1.8. Morphisms of finite presentation and constructible sets

**(1.8.1)**

<!-- label: IV.1.8.1 -->

Let $X$ be a prescheme; one knows that every quasi-compact open set in $X$ is a finite union of affine open sets, and
conversely. For an open set $U$ of $X$ to be **retrocompact** in $X$ $(0_{III}, 9.1.1)$, it is therefore necessary and
sufficient that for every affine open set $V$ of $X$, $U \cap V$ be quasi-compact. When $X$ is *quasi-separated*
`(1.2.1)`, every quasi-compact open set in $X$ is retrocompact in $X$ `(1.2.7)`, so every locally constructible part of
$X$ is retrocompact in $X$ $(0_{III}, 9.1.13)$; if moreover $X$ is *quasi-compact*, there is identity between
constructible parts and locally constructible parts in $X$ $(0_{III}, 9.1.12)$, and between open constructible parts and
open quasi-compact parts $(0_{III}, 9.1.5)$.

**Proposition (1.8.2).**

<!-- label: IV.1.8.2 -->

*Let $X$, $Y$ be two preschemes, $f : X \to Y$ a morphism. For every constructible (resp. locally constructible) part
$Z$ of $Y$, $f^{-1}(Z)$ is a constructible (resp. locally constructible) part of $X$.*

Suppose $Z$ locally constructible; for every $x \in X$ there will be an affine open neighbourhood $V$ of $f(x)$ such
that $Z \cap V$ is constructible in $V$; if the proposition is proved for constructible parts, $f^{-1}(Z) \cap
f^{-1}(V)$ will be constructible in $f^{-1}(V)$, so $f^{-1}(Z)$ will be locally constructible. It therefore suffices to
consider the case where $Z$ is constructible, and, taking account of $(0_{III}, 9.1.3)$, one is reduced to the case
where $Z$ is open and retrocompact in $Y$, that is, such that the canonical injection $Z \to Y$ is a quasi-compact
morphism; it then suffices to see that $f^{-1}(Z)$ is retrocompact in $X$, that is, such that the canonical injection
$f^{-1}(Z) \to X$ is a quasi-compact morphism; but this results from `(1.1.2, (iii))`, since $f^{-1}(Z) = Z \times_{Y}
X$ `(I, 4.4.1)`.

**Lemma (1.8.3).**

<!-- label: IV.1.8.3 -->

*Let $X$ be a quasi-compact and quasi-separated prescheme, $Z$ a constructible part of $X$. There then exist an affine
scheme $X'$ and a morphism of finite presentation $f : X' \to X$ such that $f(X') = Z$.*

As $X$ is quasi-compact, it is a finite union of affine open sets $X_{i}$ ($i \in I$), and as $X$ is quasi-separated, it
follows from `(1.2.7)` that each of the canonical immersions $g_{i} : X_{i} \to X$ is of finite presentation; one
concludes that if $f_{i} : X'_{i} \to X_{i}$ is a morphism of finite presentation, so is $g_{i} \circ f_{i} : X'_{i} \to
X$ `(1.6.2)`, and if $X'$ is the sum prescheme of the $X'_{i}$, the morphism $h : X' \to X$ coinciding with $g_{i} \circ
f_{i}$ on each $X'_{i}$ is also of finite presentation `(1.6.5)`. As $Z \cap X_{i}$ is constructible in $X_{i}$
$(0_{III}, 9.1.8)$, one sees that one is reduced to proving the lemma when $X_{i}$ is affine of ring $A$. Since $Z$ is
then a finite union of sets of the form $U \cap \complement V$, where $U$ and $V$ are quasi-compact open sets $(0_{III},
9.1.3)$, one sees, by considering again a suitable sum of preschemes, that one may reduce to the case where $Z = U \cap
\complement V$; moreover, since $U$ is a finite union of affine open sets, one may even restrict to the case where $U$
is affine. Since $V$ is quasi-compact, it is a finite union of open sets of the form $X_{f_{i}}$, where $f_{i} \in A$;
let $\mathfrak{J}$ be the ideal of $A$ generated by the $f_{i}$, and let $Z'$ be the closed affine subscheme of $X$ that
it defines (and which is by construction of finite presentation over $X$); by definition $V = \complement Z'$, so $U
\cap \complement V = U \cap Z'$. Consider the affine scheme $X' = Z' \times_{X} U$,

<!-- original page 239 -->

and let $f : X' \to X$ be the structure morphism; one has just seen that the canonical immersion $Z' \to X$ is of finite
presentation, and the same is true of the open immersion $U \to X$, which is quasi-compact since $U$ and $X$ are affine;
one concludes therefore from `(1.6.2, (iv))` that $f$ is of finite presentation, and one has $f(X') = Z' \cap U$
`(I, 3.4.8)`, which completes the proof.

**Theorem (1.8.4) (Chevalley).**

<!-- label: IV.1.8.4 -->

*Let $f : X \to Y$ be a morphism of finite presentation. For every locally constructible part $Z$ of $X$, $f(Z)$ is
locally constructible in $Y$.*

Let $y \in Y$ and $V$ an affine open neighbourhood of $y$; since $f$ is quasi-compact and quasi-separated, so is its
restriction $f^{-1}(V) \to V$, hence $f^{-1}(V)$ is a quasi-compact and quasi-separated prescheme `(1.2.3)`; as $Z \cap
f^{-1}(V)$ is constructible in $f^{-1}(V)$ `(1.8.1)`, one sees that one may restrict to the case where $Y$ is affine and
$Z$ constructible; $X$ is then quasi-compact and quasi-separated, so `(1.8.3)` there exists a morphism of finite
presentation $g : X' \to X$ such that $Z = g(X')$; since $f \circ g$ is of finite presentation, one sees that one is
reduced to the case where $Z = X$; in other words, it will suffice to prove:

**Lemma (1.8.4.1).**

<!-- label: IV.1.8.4.1 -->

*Let $Y$ be an affine scheme, $f : X \to Y$ a quasi-compact morphism locally of finite presentation; then $f(X)$ is a
constructible part of $Y$.*

As $X$ is quasi-compact, it is a finite union of affine open sets; one may therefore restrict to the case where $Y =
\operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, $B$ being an $A$-algebra of finite presentation `(1.4.6)`. Now,
one has:

**Lemma (1.8.4.2).**

<!-- label: IV.1.8.4.2 -->

*Let `A_0` be a ring, $(A_{\lambda})_{\lambda \in L}$ an inductive system of `A_0`-algebras, $A = \varinjlim
A_{\lambda}$; if $B$ is an $A$-algebra of finite presentation, there exist a $\lambda$ and an $A_{\lambda}$-algebra of
finite presentation $B_{\lambda}$ such that $B$ is isomorphic to $B_{\lambda} \otimes_{A_{\lambda}} A$.*

By hypothesis, $B$ is isomorphic to an algebra of the form $A[T_{1}, \cdots, T_{n}] / \mathfrak{J}$, where the $T_{i}$
are indeterminates and $\mathfrak{J}$ an ideal of finite type; let $(F_{j})$ ($1 \leq j \leq m$) be a system of
generators of $\mathfrak{J}$. Let $\phi_{\lambda} : A_{\lambda} \to A$ be the canonical homomorphism. As $L$ is
filtered, there exists $\lambda$ such that each of the coefficients of each of the polynomials $F_{j}$ is the image
under $\phi_{\lambda}$ of an element of $A_{\lambda}$. In other words, there exists a system of polynomials $(F_{j
\lambda})_{1 \leq j \leq m}$ of $A_{\lambda}[T_{1}, \cdots, T_{n}]$ such that $F_{j} = \phi_{\lambda}(F_{j \lambda})$
for $1 \leq j \leq m$. If $\mathfrak{J}_{\lambda}$ is the ideal of $A_{\lambda}[T_{1}, \cdots, T_{n}]$ generated by the
$F_{j \lambda}$, $\mathfrak{J}$ is the image of $\mathfrak{J}_{\lambda} \otimes_{A_{\lambda}} A$ in $A[T_{1}, \cdots,
T_{n}] = A_{\lambda}[T_{1}, \cdots, T_{n}] \otimes_{A_{\lambda}} A$; the ring $B_{\lambda} = A_{\lambda}[T_{1}, \cdots,
T_{n}] / \mathfrak{J}_{\lambda}$ answers the question.

One will apply this lemma here by considering $A$ as the inductive limit of its sub-$\mathbb{Z}$-algebras of finite
type. One sees therefore that there exists such a sub-$\mathbb{Z}$-algebra `A_0` of $A$, and an `A_0`-algebra of finite
presentation `B_0` such that $B$ is isomorphic to $B_{0} \otimes_{A_{0}} A$; set $X_{0} = \operatorname{Spec}(B_{0})$,
$Y_{0} = \operatorname{Spec}(A_{0})$, so that $X = X_{0} \times_{Y_{0}} Y$, $f$ being the projection $X \to Y$; let
$f_{0} : X_{0} \to Y_{0}$, $g_{0} : Y \to Y_{0}$ be the structure morphisms; it follows from `(I, 3.4.8)` that one has
$f(X) = g^{-1}_{0}(f_{0}(X_{0}))$; taking account of `(1.8.2)`, it therefore suffices to show that $f_{0}(X_{0})$ is
constructible. In other words, one is finally reduced to proving:

**Corollary (1.8.5).**

<!-- label: IV.1.8.5 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a morphism of finite type. For every constructible part $Z$ of $X$,
$f(Z)$ is a constructible part of $Y$.*

<!-- original page 240 -->

One reduces as above to proving that $f(X)$ is constructible. Apply criterion $(0_{III}, 9.2.3)$: it suffices to prove
that for every irreducible closed part $T$ of $Y$, $T \cap f(X) = f(f^{-1}(T))$ is either rare in $T$ or contains a
non-empty open of $T$; taking a subprescheme of $Y$ having $T$ as underlying space `(I, 5.2.1)` and considering its
inverse image under $f$, one sees finally (taking account of `(1.5.4, (iii))`) that one is reduced to proving that if
one supposes $Y$ *irreducible* and $f$ *dominant*, then $f(X)$ contains a non-empty open of $Y$. One may further suppose
$Y$ affine; then $X$ is a finite union of affine open sets $V_{i}$, and as $f(X)$ is dense in $Y$, the same is true of
at least one of the $f(V_{i})$. One may therefore also suppose $X$ affine; if $(X_{j})$ is the (finite) family of
irreducible components of $X$, one sees as above that at least one of the $f(X_{j})$ is dense in $Y$; one may therefore
suppose $X$ irreducible. Finally, replacing $f$ by $f_{red}$ `(1.5.4, (vi))`, one may suppose $X$ and $Y$ integral. Then
$X = \operatorname{Spec}(B)$, $Y = \operatorname{Spec}(A)$, where $A$ is a Noetherian integral ring, $B$ an integral
$A$-algebra of finite type containing $A$ `(I, 1.2.7)`. It suffices to show that there exists $g \in A$ such that, for
every $y \in D(g)$ (that is, such that $g \notin \mathfrak{j}_{y}$), the ideal $\mathfrak{j}_{y}$ is the intersection of
$A$ and a prime ideal of $B$, for this will show that $D(g) \subset f(X)$. Finally, it suffices to prove:

**Lemma (1.8.5.1).**

<!-- label: IV.1.8.5.1 -->

*Let $A$ be an integral ring, $B$ an integral $A$-algebra of finite type. There exists $g \in A$ such that every
homomorphism of $A$ into an algebraically closed field $\Omega$, non-zero on $g$, extends to a homomorphism of $B$ into
$\Omega$.*

Now, this is a classical result of commutative algebra `(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 3 du th. 1)`.

**Corollary (1.8.6).**

<!-- label: IV.1.8.6 -->

*Let $Y$ be an irreducible prescheme, $\eta$ its generic point, $f : X \to Y$ a morphism locally of finite type. If
$f^{-1}(\eta)$ is not empty, there exists an open neighbourhood $U$ of $\eta$ in $Y$ such that $f^{-1}(y)$ is non-empty
for every $y \in U$. If $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module of finite type, and if
$\mathcal{F}_{\eta} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(\eta)$ is not zero, then there exists an open
neighbourhood $U'$ of $\eta$ in $Y$ such that $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$ is not zero
for every $y \in U'$.*

If $p_{y}$ is the canonical projection of the fibre $f^{-1}(y) = X \times_{Y} \operatorname{Spec}(k(y))$ into $X$, one
has $\mathcal{F}_{y} = p^{*}_{y}(\mathcal{F})$, so `Supp(ℱ_y) = p_y⁻¹(Supp(ℱ)) = Supp(ℱ) ∩ f⁻¹(y)` by virtue of
`(I, 9.1.13.1)` and `(I, 3.6.1)`, since $\mathcal{F}$ is of finite type; furthermore $Supp(\mathcal{F})$ is closed in
$X$ $(0_{I}, 5.2.2)$, and if $Z$ is a closed subprescheme of $X$ having $Supp(\mathcal{F})$ as underlying space
`(I, 5.2.1)`, and $j$ the canonical immersion $Z \to X$, $f \circ j$ is locally of finite type `(1.3.4)`; this shows
that the first assertion entails the second. To prove the first assertion, remark first that one may suppose $X$ and $Y$
reduced `(1.3.4, (vi))`, that is, $Y$ integral. Let $\xi$ be a point of $f^{-1}(\eta)$; one may replace $X$ and $Y$ by
affine open neighbourhoods of $\xi$ and $\eta$ respectively, and hence suppose that $X = \operatorname{Spec}(B)$, $Y =
\operatorname{Spec}(A)$, $B$ being an $A$-algebra of finite type. In addition, if $Z$ is the reduced closed subprescheme
of $X$ having $\overline{\xi}$ as underlying set `(I, 5.2.1)`, one may, as above, replace $X$ by $Z$, that is, suppose
$B$ integral `(I, 5.1.4)`. As the morphism $f$ is then dominant, the corresponding homomorphism $\phi : A \to B$ is
injective `(I, 1.2.7)`; so the corollary results finally from lemma `(1.8.5.1)`.

<!-- original page 241 -->

**Proposition (1.8.7).**

<!-- label: IV.1.8.7 -->

*Let $S$ be a prescheme, $g : X \to S$, $h : Y \to S$ two morphisms of finite presentation, $f : X \to Y$ an
$S$-morphism. For every $s \in S$, set $X_{s} = g^{-1}(s) = X \times_{S} \operatorname{Spec}(k(s))$, $Y_{s} = h^{-1}(s)
= Y \times_{S} \operatorname{Spec}(k(s))$, $f_{s} = f \times 1 : X_{s} \to Y_{s}$. Then the set of $s \in S$ such that
$f_{s}$ is surjective (resp. radicial) is locally constructible.*

Let $E$ be the set of $s \in S$ such that $f_{s}$ is surjective; the set $S - E$ is equal to $h(Y - f(X))$; now $f$ is
of finite presentation `(1.6.2, (v))`, so $f(X)$ is locally constructible in $Y$ `(1.8.4)`; since $h$ is of finite
presentation, $h(Y - f(X))$ is locally constructible in $S$, hence so is $E$.

To show that the set $E'$ of $s \in S$ such that $f_{s}$ is radicial is locally constructible, we will use:

**Lemma (1.8.7.1).**

<!-- label: IV.1.8.7.1 -->

*Let $U$, $V$ be two preschemes; for a morphism $f : U \to V$ to be radicial, it is necessary and sufficient that the
diagonal morphism $\Delta_{f} : U \to U \times_{V} U$ be surjective. Consequently, every radicial morphism is
separated.*

Indeed, $\Delta_{f}$, being an immersion `(I, 5.3.9)`, is a morphism locally of finite type `(1.3.4)`; to say that
$\Delta_{f}$ is surjective therefore means that for every algebraically closed field $K$, the corresponding map $U(K)
\to (U \times_{V} U)(K) = U(K) \times_{V(K)} U(K)$ is surjective `(1.3.7 and I, 3.4.2.1)`; but by definition of a fibre
product of sets, this means that the map $U(K) \to V(K)$ corresponding to $f$ is injective, and this is equivalent to
saying that $f$ is radicial `(I, 3.5.5)`.

This being so, $\Delta_{f_{s}}$ is deduced from $\Delta_{f} : X \to X \times_{Y} X$ by the base change
$\operatorname{Spec}(k(s)) \to S$ `(I, 5.3.4)`. Since $f$ is of finite presentation, so is the structure morphism $X
\times_{Y} X \to Y$ `(1.6.2, (iv))`, hence also $\Delta_{f}$ `(1.6.2, (v))`; it therefore suffices to apply the first
part of the proposition to $\Delta_{f}$, using lemma `(1.8.7.1)`.

### 1.9. Pro-constructible and ind-constructible sets

**Lemma (1.9.1).**

<!-- label: IV.1.9.1 -->

*Let $(A_{\alpha})_{\alpha \in I}$ be an inductive system of rings whose index set $I$ is filtered to the right, and let
$A = \varinjlim A_{\alpha}$. For $A = 0$ it is necessary and sufficient that there exist an index $\gamma$ such that
$A_{\gamma} = 0$ (and one then has $A_{\beta} = 0$ for every $\beta \geq \gamma$).*

Indeed, for every $\alpha \in I$, the canonical homomorphism $\phi_{\alpha} : A_{\alpha} \to A$ transforms the unit
element into the unit element; to say that $A = 0$ means that $\phi_{\alpha}(1) = 0$, or again that $\phi_{\alpha}(1) =
\phi_{\alpha}(0)$; one knows that this is equivalent to saying that there exists an index $\gamma \geq \alpha$ such that
the homomorphism $\phi_{\gamma \alpha} : A_{\alpha} \to A_{\gamma}$ is such that $\phi_{\gamma \alpha}(1) = \phi_{\gamma
\alpha}(0)$, and this last relation is equivalent to $A_{\gamma} = 0$, whence the lemma.

**Proposition (1.9.2).**

<!-- label: IV.1.9.2 -->

*Let $B$ be a ring, $(A_{\alpha})_{\alpha \in I}$ an inductive system of $B$-algebras whose index set $I$ is filtered to
the right, and let $A = \varinjlim A_{\alpha}$; set $Y = \operatorname{Spec}(B)$, $X_{\alpha} =
\operatorname{Spec}(A_{\alpha})$, $X = \operatorname{Spec}(A)$, and let $u : X \to Y$, $u_{\alpha} : X_{\alpha} \to Y$
be the morphisms corresponding to the structure homomorphisms $B \to A$, $B \to A_{\alpha}$. Then:*

*(i) For $X = \emptyset$ it is necessary and sufficient that there exist a $\gamma \in I$ such that $X_{\gamma} =
\emptyset$, and one then has $X_{\alpha} = \emptyset$ for $\alpha \geq \gamma$.*

<!-- original page 242 -->

*(ii) One has*

```text
  u(X) = ⋂_{α ∈ I} u_α(X_α).                                                    (1.9.2.1)
```

Assertion (i) is nothing but the translation of `(1.9.1)`. To prove (ii), note that, since $u$ factors as $X \to
X_{\alpha} \xrightarrow{u_{\alpha}} Y$, the first member of `(1.9.2.1)` is contained in the second. Conversely, let $y
\in Y - u(X)$; one has $u^{-1}(y) = \emptyset$, and $u^{-1}(y)$ is the space underlying the $k(y)$-prescheme
$\operatorname{Spec}(A \otimes_{B} k(y))$; as in the category of $B$-modules the functor $\varinjlim$ commutes with the
tensor product, $A \otimes_{B} k(y)$ is the inductive limit of the inductive system of rings $A_{\alpha} \otimes_{B}
k(y)$; lemma `(1.9.1)` shows that there exists $\alpha$ such that $A_{\alpha} \otimes_{B} k(y) = 0$, that is,
$u^{-1}_{\alpha}(y) = \emptyset$, hence $y \notin u_{\alpha}(X_{\alpha})$. C.Q.F.D.

**Proposition (1.9.3).**

<!-- label: IV.1.9.3 -->

*Let $X$ be a quasi-compact and quasi-separated prescheme, $E$ a part of $X$, $(X_{\alpha})_{\alpha \in I}$ an affine
open cover of $X$, and for every $\alpha \in I$, set $E_{\alpha} = E \cap X_{\alpha}$. The following conditions are
equivalent:*

*a) There exists a quasi-compact morphism $f : X' \to X$ such that $E = f(X')$.*

*a') For every $\alpha$, there exists a quasi-compact morphism $f_{\alpha} : X'_{\alpha} \to X_{\alpha}$ such that
$E_{\alpha} = f_{\alpha}(X'_{\alpha})$.*

*a'') For every $\alpha$, there exist an affine scheme $X'_{\alpha}$ and a morphism $f_{\alpha} : X'_{\alpha} \to
X_{\alpha}$ such that $f_{\alpha}(X'_{\alpha}) = E_{\alpha}$.*

*b) $E$ is an intersection of constructible parts of $X$.*

*b') $F = X - E$ is a union of constructible parts of $X$.*

It is clear that b) and b') are equivalent. Condition a) entails a') by taking for $X'_{\alpha}$ the prescheme induced
on the open set $f^{-1}(X_{\alpha})$ of $X'$ and for $f_{\alpha}$ the restriction of $f$. To see that a') entails a''),
it suffices to remark that $X'_{\alpha}$ is a union of affine open sets $X''_{\alpha \lambda}$ ($\lambda \in
L_{\alpha}$); let $X''_{\alpha}$ be the sum prescheme of the $X''_{\alpha \lambda}$ ($\lambda \in L_{\alpha}$), which is
an affine scheme; if $g_{\alpha} : X''_{\alpha} \to X'_{\alpha}$ is the morphism coinciding with the identity on each of
the $X''_{\alpha \lambda}$, it is clear that if one sets $f'_{\alpha} = f_{\alpha} \circ g_{\alpha}$, one has
$E_{\alpha} = f'_{\alpha}(X''_{\alpha})$ since $g_{\alpha}$ is surjective. To show that a'') entails a), note that there
is a finite subset $J$ of $I$ such that the $X_{\alpha}$ of indices $\alpha \in J$ cover $X$; let $X'$ be the sum
prescheme of the $X'_{\alpha}$ for $\alpha \in J$, and let $f : X' \to X$ be the morphism coinciding with $j_{\alpha}
\circ f_{\alpha}$ for every $\alpha \in J$, where $j_{\alpha} : X_{\alpha} \to X$ is the canonical injection. As $E$ is
the union of the $E \cap X_{\alpha}$ for $\alpha \in J$, one has indeed $E = f(X')$, and it remains to see that $f$ is a
quasi-compact morphism; but the hypothesis that $X$ is quasi-separated entails that $j_{\alpha}$ is quasi-compact
`(1.2.7)`, hence so is $j_{\alpha} \circ f_{\alpha}$ `(1.1.1 and 1.1.2)` and finally $f$ `(1.1.6)`.

It remains then to prove the equivalence of a'') and b). Let us prove first that a'') entails b): consider a finite
subset $J$ of $I$ such that the $X_{\alpha}$ for $\alpha \in J$ cover $X$; it will suffice to show that, for every
$\alpha \in J$, $E_{\alpha}$ is an intersection of constructible parts $F_{\alpha \lambda}$ of $X_{\alpha}$ ($\lambda
\in L_{\alpha}$); indeed, every $F_{\alpha \lambda}$ is also a constructible part of $X$ by virtue of $(0_{III}, 9.1.8,
(ii))$, because the hypothesis that $X$ is quasi-separated entails that every $X_{\alpha}$ is retrocompact in $X$
`(1.2.7)`; $E$ being the union of the $E_{\alpha}$ for $\alpha \in J$, is intersection of the (finite) unions
$\bigcup_{\alpha \in J} F_{\alpha, \lambda(\alpha)}$, for all choices of $\lambda(\alpha) \in L_{\alpha}$; these unions
being constructible in $X$, this establishes our assertion. One may therefore restrict to the case

<!-- original page 243 -->

where $X = \operatorname{Spec}(A)$ and where $E = f(X')$, $X' = \operatorname{Spec}(A')$ being affine, $f : X' \to X$ a
morphism corresponding to a ring homomorphism $A \to A'$. Note now that $A'$ is the inductive limit of the family
$(A'_{\lambda})$ of its sub-$A$-algebras of finite type, ordered by inclusion; if $X'_{\lambda} =
\operatorname{Spec}(A'_{\lambda})$, $f$ factors as $X' \to X'_{\lambda} \xrightarrow{f_{\lambda}} X$ and it results from
`(1.9.2, (ii))` that one has $f(X') = \bigcap_{\lambda} f_{\lambda}(X'_{\lambda})$; if one shows that
$f_{\lambda}(X'_{\lambda})$ is an intersection of constructible parts of $X$, the same will be true of $f(X')$. One may
therefore restrict to the case where $A'$ is an $A$-algebra of finite type. Now, one has the following lemma:

**Lemma (1.9.3.1).**

<!-- label: IV.1.9.3.1 -->

*Let $A$ be a ring, $A'$ an $A$-algebra of finite type. Then $A'$ is $A$-isomorphic to a filtered inductive limit
$\varinjlim A''_{\mu}$ where the $A''_{\mu}$ are $A$-algebras of finite presentation `(1.4.1)`.*

Indeed, one may write $A' = B / \mathfrak{J}$, with $B = A[T_{1}, \cdots, T_{n}]$ and $\mathfrak{J}$ an ideal of $B$.
But $\mathfrak{J}$ is the inductive limit of the ideals of finite type $\mathfrak{J}'_{\mu}$ of $B$, contained in
$\mathfrak{J}$, ordered by inclusion; as in the category of $B$-modules the functor $\varinjlim$ is exact, one concludes
that $A' \cong \varinjlim B / \mathfrak{J}'_{\mu}$ up to an $A$-isomorphism.

The same reasoning as above then allows one to reduce to the case where $A'$ is an $A$-algebra of finite presentation;
but then $f(X')$ is constructible in $X$ by virtue of Chevalley's theorem `(1.8.5)`, which proves b).

Let us finally prove that b) entails a''). If $E$ is an intersection of a family $(G_{\lambda})_{\lambda \in L}$ of
constructible parts of $X$, each $E_{\alpha}$ is the intersection of the $G_{\lambda} \cap X_{\alpha}$, which are
constructible in $X_{\alpha}$ $(0_{III}, 9.1.8, (i))$, so one is reduced to the case where $X = \operatorname{Spec}(A)$
is affine.

One then knows `(1.8.3)` that for every $\lambda \in L$ there exists a morphism $f_{\lambda} : X'_{\lambda} \to X$,
where $X'_{\lambda} = \operatorname{Spec}(A'_{\lambda})$ is affine, such that $f_{\lambda}(X'_{\lambda}) = G_{\lambda}$.
It therefore suffices to prove the following lemma:

**Lemma (1.9.3.2).**

<!-- label: IV.1.9.3.2 -->

*Let $(A'_{\lambda})_{\lambda \in L}$ be a family of $A$-algebras, $X = \operatorname{Spec}(A)$, $X'_{\lambda} =
\operatorname{Spec}(A'_{\lambda})$, and let $f_{\lambda} : X'_{\lambda} \to X$ be the structure morphism. For every
finite subset $J$ of $L$, set $A'_{J} = \bigotimes_{\lambda \in J} A'_{\lambda}$ (tensor product of $A$-algebras),
$X'_{J} = \operatorname{Spec}(A'_{J})$, and let $f_{J} : X'_{J} \to X$ be the structure morphism. One then has*

```text
  f_J(X'_J) = ⋂_{λ ∈ J} f_λ(X'_λ).
```

*If $A' = \varinjlim A'_{J}$, $J$ running over the filtered set of finite parts of $L$, $X' = \operatorname{Spec}(A')$,
and if $f : X' \to X$ is the structure morphism, one has*

```text
  f(X') = ⋂_{λ ∈ L} f_λ(X'_λ).
```

The first assertion results from `(I, 3.4.7)`; the second results from `(1.9.2, (ii))`, which gives the relation $f(X')
= \bigcap_{J} f_{J}(X'_{J})$.

**Definition (1.9.4).**

<!-- label: IV.1.9.4 -->

*Let $X$ be a topological space. We say that a part $E$ of $X$ is **pro-constructible** (resp. **ind-constructible**) in
$X$ if, for every $x \in X$, there exists an open neighbourhood $U$ of $x$ in $X$ such that $E \cap U$ is the
intersection (resp. union) of locally constructible parts of $U$.*

Taking account of `(1.2.7)` and $(0_{III}, 9.1.8 and 9.1.12)$, the equivalent conditions of proposition `(1.9.3)` are
therefore expressed by saying that $E$ is pro-constructible in $X$, the locally constructible sets in $X$ being
identical to the constructible sets in $X$ under the hypotheses of `(1.9.3)`.

<!-- original page 244 -->

**Proposition (1.9.5).**

<!-- label: IV.1.9.5 -->

*Let $X$ be a prescheme.*

*(i) For a part $E$ of $X$ to be pro-constructible, it is necessary and sufficient that $X - E$ be ind-constructible.*

*(ii) Every finite union and every intersection of pro-constructible parts of $X$ is pro-constructible. Every finite
intersection and every union of ind-constructible parts of $X$ is ind-constructible.*

*(iii) Every intersection (resp. union) of locally constructible parts of $X$ is pro-constructible (resp.
ind-constructible). Conversely, if $X$ is quasi-compact and quasi-separated, every pro-constructible (resp.
ind-constructible) part of $X$ is an intersection (resp. union) of constructible parts of $X$.*

*(iv) Let $(U_{\alpha})$ be an open cover of $X$. For a part $E$ of $X$ to be pro-constructible (resp.
ind-constructible) in $X$, it is necessary and sufficient that for every $\alpha$, $E \cap U_{\alpha}$ be
pro-constructible (resp. ind-constructible) in $U_{\alpha}$.*

*(v) Every pro-constructible part $E$ of $X$ is retrocompact in $X$. For a locally closed part $E$ of $X$ to be
retrocompact in $X$, it is necessary and sufficient that it be pro-constructible in $X$.*

*(vi) Let $f : X' \to X$ be a morphism of preschemes; for every pro-constructible (resp. ind-constructible) part $E$ of
$X$, $f^{-1}(E)$ is pro-constructible (resp. ind-constructible) in $X'$.*

*(vii) Let $f : X' \to X$ be a quasi-compact morphism; for every pro-constructible part $E'$ of $X'$, $f(E')$ is
pro-constructible in $X$; in particular $f(X')$ is pro-constructible in $X$.*

*(viii) Let $f : X' \to X$ be a morphism locally of finite presentation; for every ind-constructible part $E'$ of $X'$,
$f(E')$ is ind-constructible in $X$; in particular $f(X')$ is ind-constructible in $X$.*

*(ix) Suppose $X$ is quasi-compact and quasi-separated; then, for a part $E$ of $X$ to be pro-constructible, it is
necessary and sufficient that there exist an affine scheme $X'$ and a morphism (necessarily quasi-compact) $f : X' \to
X$ such that $E = f(X')$.*

Properties (i), (ii), (iv), and the first assertion of (iii) result from definition `(1.9.4)` and are valid for an
arbitrary topological space, using the mutual distributivity of intersection and union and the fact that if $T$ is
locally constructible in $X$, $T \cap U$ is locally constructible in $U$ for every open $U$ of $X$. If $X$ is
quasi-compact and quasi-separated and $E$ is pro-constructible in $X$, there is a finite cover $(U_{i})$ of $X$ formed
of affine open sets such that $E \cap U_{i}$ is the intersection of constructible parts $M_{i\lambda}$ of $U_{i}$
($\lambda \in L_{i}$); the $M_{i\lambda}$ are also constructible in $X$ by virtue of `(1.2.7)` and $(0_{III}, 9.1.8,
(ii))$, and $E$ is the intersection of the finite unions $\bigcup_{i} M_{i, \lambda(i)}$ (where $\lambda(i) \in L_{i}$
for every $i$), which are constructible parts of $X$; this proves the second assertion of (iii). Assertion (ix) results
from (iii) and from `(1.9.3)`. To prove the first assertion of (v), one may restrict to the case where $X$ is affine,
and prove then that $E$ is quasi-compact $(0_{III}, 9.1.1)$; but since $X$ is then quasi-separated, there exists by
virtue of (ix) a quasi-compact morphism $f : X' \to X$ such that $E = f(X')$; as $X'$ is quasi-compact, the same is true
of its image $E$ under a continuous map.

To prove (vi), one may restrict, by virtue of (iv), to the case where $X$ is affine; the conclusion then results from
(iii) and from `(1.8.2)`.

<!-- original page 245 -->

Similarly, to prove (vii), one may restrict to the case where $X$ is affine; then $X'$ is a finite union of affine open
sets $X'_{i}$ and $f(E')$ is the union of the $f(E' \cap X'_{i})$, so that one may also suppose $X'$ affine, by virtue
of (ii); but then $E' = g(X'')$, where $g : X'' \to X'$ is a quasi-compact morphism, by virtue of (ix), and one has
$f(E') = f(g(X''))$, hence $f(E')$ is pro-constructible since $g \circ f$ is quasi-compact.

One deduces from (vii) the proof of the second assertion of (v): indeed, let $E$ be a locally closed and retrocompact
part of $X$, and consider a subprescheme of $X$ having $E$ as underlying space `(I, 5.2.1)`; the canonical injection
$j : E \to X$ is then by hypothesis a quasi-compact morphism, and it results from (vii) that $E = j(E)$ is
pro-constructible in $X$.

Finally, to prove (viii), one may again suppose $X$ affine; in addition, if $(X'_{\alpha})$ is an affine open cover of
$X'$ such that $E' \cap X'_{\alpha}$ is a union of constructible parts of $X'_{\alpha}$ ((iii) and (iv)), $f(E')$ is the
union of the $f(E' \cap X'_{\alpha})$, and, by virtue of Chevalley's theorem `(1.8.4)`, each of the $f(E' \cap
X'_{\alpha})$ is a union of constructible parts of $X$, whence the conclusion.

**Exemples (1.9.6).**

<!-- label: IV.1.9.6 -->

Every *finite* part of a prescheme $X$ is pro-constructible: indeed, it suffices to consider the parts ${x}$ reduced to
a single point `(1.9.5, (ii))`, and ${x}$ is the image of $\operatorname{Spec}(k(x))$ under the canonical morphism
$\operatorname{Spec}(k(x)) \to X$, which is quasi-compact; whence the conclusion by `(1.9.5, (vii))`. By contrast, a
part ${x}$ reduced to a point is not necessarily ind-constructible; for example, let $A$ be a Noetherian integral ring
having an infinity of maximal ideals, and let $x$ be the generic point of $X = \operatorname{Spec}(A)$; if ${x}$ were
ind-constructible in $X$, it would be constructible by virtue of `(1.9.5, (iii))` and consequently would contain a
non-empty open of $X$ $(0_{III}, 9.2.2)$; but this contradicts the hypothesis that $A$ has infinitely many maximal
ideals, by virtue of Artin–Tate's theorem $(0_{IV}, 16.3.3)$.

Every *closed* part $Y$ of a prescheme $X$ is pro-constructible, by `(1.9.5, (v))`. Every open part of $X$ is therefore
ind-constructible, but an open part $U$ of $X$ is pro-constructible only if it is *retrocompact*, again by virtue of
`(1.9.5, (v))`.

Finally, if $X$ is a *Noetherian* prescheme, hence quasi-separated `(1.2.8)`, it follows from `(1.9.5, (iii))` and from
$(0_{III}, 9.1.7)$ that the ind-constructible parts of $X$ are the *unions of locally closed parts* of $X$.

**Theorem (1.9.7).**

<!-- label: IV.1.9.7 -->

*Let $X$ be a quasi-compact prescheme, $E$ an ind-constructible part of $X$, $(F_{\lambda})_{\lambda \in L}$ a family of
pro- constructible parts of $X$ such that $\bigcap_{\lambda \in L} F_{\lambda} \subset E$; then there exists a finite
subset $J$ of $L$ such that $\bigcap_{\lambda \in J} F_{\lambda} \subset E$.*

Note that the sets $F = X - E$ and $F \cap F_{\lambda}$ are pro-constructible, so one is reduced to:

**Corollary (1.9.8).**

<!-- label: IV.1.9.8 -->

*Let $X$ be a quasi-compact prescheme, $(F_{\lambda})_{\lambda \in L}$ a family of pro-constructible parts of $X$ whose
intersection is empty; then there exists a finite subfamily $(F_{\lambda})_{\lambda \in J}$ whose intersection is
empty.*

Covering $X$ by a finite number of affine open sets, and using `(1.9.5, (iv))`, one is reduced to the case where $X$ is
affine; by virtue of `(1.9.5, (ix))`, one has $F_{\lambda} = f_{\lambda}(X'_{\lambda})$,

<!-- original page 246 -->

where $X'_{\lambda} = \operatorname{Spec}(A'_{\lambda})$ is affine, and $f_{\lambda}$ is a morphism $X'_{\lambda} \to
X$; then, with the notations of `(1.9.3.2)`, one has by hypothesis $f(X') = \emptyset$, hence $X' = \emptyset$; but this
entails by `(1.9.2, (i))` that there exists a finite subset $J$ of $L$ such that $X'_{J} = \emptyset$, hence
$f_{J}(X'_{J}) = \bigcap_{\lambda \in J} F_{\lambda} = \emptyset$.

**Corollary (1.9.9).**

<!-- label: IV.1.9.9 -->

*Let $X$ be a quasi-compact prescheme, $F$ a pro-constructible part of $X$, $(E_{\lambda})_{\lambda \in L}$ a family of
ind- constructible parts of $X$ such that $F \subset \bigcup_{\lambda \in L} E_{\lambda}$; then there exists a finite
subset $J$ of $L$ such that $F \subset \bigcup_{\lambda \in J} E_{\lambda}$. In particular, from every cover of $X$ by
ind-constructible parts, one can extract a finite cover of $X$.*

This results from `(1.9.7)` by passing to complements.

**Proposition (1.9.10).**

<!-- label: IV.1.9.10 -->

*Let $X$ be a prescheme. For a part $E$ of $X$ to be ind-constructible, it is necessary that, for every $x \in X$, the
intersection $E \cap \overline{x}$ be a neighbourhood of $x$ in $\overline{x}$. If $X$ is locally Noetherian, this
condition is sufficient.*

Suppose $E$ is ind-constructible, and let $Y$ be the intersection of $\overline{x}$ and an affine open in $X$ containing
$x$; there is therefore a subprescheme of $X$ having $Y$ as underlying space `(I, 5.2.1)`, and if $j : Y \to X$ is the
canonical injection, $E \cap Y = j^{-1}(E)$ is ind-constructible in $Y$ `(1.9.5, (vi))`. Since $Y$ is quasi-compact and
separated, $E \cap Y$ is therefore a union of constructible parts of $Y$ `(1.9.5, (iii))`; consequently, there are two
opens $U$, $V$ in $Y$ such that $x \in U \cap \complement V \subset E \cap Y$ $(0_{III}, 9.1.3)$. But as $x$ is generic
point of the irreducible space $Y$, $V$ is necessarily empty and one has $U \subset E \cap Y$.

Suppose now $X$ locally Noetherian, and let $E$ be a part of $X$ satisfying the condition of the statement. By virtue of
definition `(1.9.4)`, one may restrict to the case where $X$ is Noetherian. Then, for every $x \in X$, $E \cap
\overline{x}$ contains a non-empty part of the form $U \cap \overline{x}$, where $U$ is open in $X$; this shows that $E$
is a union of locally closed parts of $X$, hence is ind-constructible `(1.9.6)`.

**Proposition (1.9.11).**

<!-- label: IV.1.9.11 -->

*Let $X$ be a prescheme, $E$ a part of $X$. The following properties are equivalent:*

*a) $E$ is locally constructible.*

*b) $E$ is ind-constructible and pro-constructible.*

*c) $E$ and $X - E$ are pro-constructible.*

*d) $E$ and $X - E$ are ind-constructible.*

It manifestly suffices to prove that d) entails a), and one may restrict to the case where $X$ is affine. Then
`(1.9.5, (iii))`, $E$ (resp. $X - E$) is a union of a family $(E_{\lambda})$ (resp. $(E'_{\mu})$) of constructible parts
of $X$; as the $E_{\lambda}$ and the $E'_{\mu}$ form a cover of $X$, it follows from `(1.9.9)` that there are indices in
finite number $\lambda_{i}$, $\mu_{j}$ such that the $E_{\lambda_{i}}$ and the $E'_{\mu_{j}}$ form a cover of $X$; this
implies that $E$ is the union of the $E_{\lambda_{i}}$, hence is constructible.

**Corollary (1.9.12).**

<!-- label: IV.1.9.12 -->

*Let $f : X \to Y$ be a surjective morphism, which is either quasi-compact or locally of finite presentation. For a part
$E$ of $Y$ to be locally constructible (resp. pro-constructible, resp. ind-constructible), it is necessary and
sufficient that $f^{-1}(E)$ be so in $X$.*

<!-- original page 247 -->

One knows that the condition is necessary `((1.8.2)` and `(1.9.5, (vi)))`; to show that it is sufficient, one is reduced
to the case where $X$ is affine, by virtue of `(1.9.5, (iv))`; moreover, by virtue of `(1.9.11)`, one may restrict to
the case where $f^{-1}(E)$ is pro-constructible, or to the case where $f^{-1}(E)$ is ind-constructible. If $f$ is
surjective and quasi-compact, and $f^{-1}(E)$ pro-constructible, it follows from `(1.9.5, (vii))` that $E =
f(f^{-1}(E))$ is pro-constructible. If $f$ is surjective and locally of finite presentation, and $f^{-1}(E)$
ind-constructible, $E = f(f^{-1}(E))$ is ind-constructible by `(1.9.5, (viii))`, which completes the proof.

**(1.9.13)**

<!-- label: IV.1.9.13 -->

Let $X$ be a prescheme, $\mathcal{T}$ its topology; it follows from `(1.9.5, (i) and (ii))` that the ind-constructible
(resp. pro-constructible) parts of $X$ are the open (resp. closed) parts for a topology on $X$, called the
**constructible topology** and which we shall denote $\mathcal{T}_{cons}$; we shall denote by $X^{cons}$ the set $X$
endowed with the topology $\mathcal{T}_{cons}$.

**Proposition (1.9.14).**

<!-- label: IV.1.9.14 -->

*Let $X$ be a prescheme, $\mathcal{T}$ its topology, $\mathcal{T}_{cons}$ the constructible topology on $X$.*

*(i) The topology $\mathcal{T}_{cons}$ is finer than $\mathcal{T}$.*

*(ii) The locally constructible parts of $X$ are identical to the parts of the space $X^{cons}$ that are at once open
and closed.*

*(iii) For every morphism $f : X \to Y$, the underlying map from $X^{cons}$ to $Y^{cons}$ is continuous; we denote it
$f^{cons}$.*

*(iv) If the morphism $f : X \to Y$ is quasi-compact, $f^{cons}$ is a closed map; in particular, if $f$ is quasi-compact
and bijective, $f^{cons}$ is a homeomorphism.*

*(v) If a morphism $f : X \to Y$ is locally of finite presentation, $f^{cons}$ is an open map; in particular, if $f$ is
bijective and locally of finite presentation, $f^{cons}$ is a homeomorphism.*

*(vi) For every open $U$ of $X$, the topology induced by $\mathcal{T}_{cons}$ on $U$ is identical to the topology of
$U^{cons}$.*

Indeed, (i) results from the fact that every open for $\mathcal{T}$ is an open for $\mathcal{T}_{cons}$ `(1.9.6)`, and
(ii) is a translation of `(1.9.11)`; (iii), (iv), and (v) translate respectively `(1.9.5)`, (vi), (vii), and (viii).
Finally to prove (vi), it suffices to remark that the canonical injection $j : U \to X$ is locally of finite
presentation `(1.4.3)`, so `j^cons : U^cons → X^cons` is a continuous open map.

**Proposition (1.9.15).**

<!-- label: IV.1.9.15 -->

*Let $X$ be a prescheme.*

*(i) For $X^{cons}$ to be quasi-compact, it is necessary and sufficient that $X$ be quasi-compact.*

*(ii) For $X^{cons}$ to be separated, it is necessary and sufficient that $X$ be quasi-separated, and $X^{cons}$ is then
locally compact and totally disconnected.*

*(iii) For $X^{cons}$ to be compact, it is necessary and sufficient that $X$ be quasi-compact and quasi-separated.*

*(iv) Every point of $X$ admits, for the topology $\mathcal{T}_{cons}$, an open and compact neighbourhood.*

*(v) For a morphism $f : X \to Y$ to be quasi-compact, it is necessary and sufficient that the continuous map
`f^cons : X^cons → Y^cons` be proper.*

(i) Since $\mathcal{T}_{cons}$ is finer than $\mathcal{T}$, it is clear that if $X^{cons}$ is quasi-compact, so is $X$;
the converse results from `(1.9.9)`.

(ii) Suppose $X$ quasi-separated, and let us show that $X^{cons}$ is totally disconnected: indeed, if $x$, $y$ are two
distinct points of $X$ and if for example $x \notin \overline{y}$, there exists an

<!-- original page 248 -->

affine open neighbourhood $U$ of $x$ in $X$ not containing $y$; as $X$ is quasi-separated, $U$ is retrocompact in $X$
`(1.2.7)`, so $U$ and $X - U$ are locally constructible in $X$, and consequently open in $X^{cons}$ by virtue of
`(1.9.11)`, whence our assertion. Since on every affine open $U$ of $X$ the topology induced by $\mathcal{T}_{cons}$ is
that of $U^{cons}$ by virtue of `(1.9.14, (vi))`, it follows from the foregoing that $X^{cons}$ is locally compact,
since $U$ is open in $X^{cons}$ and $U^{cons}$ is compact. It remains to prove that if $X^{cons}$ is separated, then $X$
is quasi-separated; consider in effect an affine open $U$ of $X$; the topology induced on $U$ by $\mathcal{T}_{cons}$ is
that of $U^{cons}$ `(1.9.14, (vi))`, so $U$ is compact for this induced topology, since $U^{cons}$ is compact by the
first part of the reasoning. If $V$ is a second affine open in $X$, $U \cap V$ is then a compact part of the separated
space $X^{cons}$, being the intersection of two compact parts of this space; as the topology induced by
$\mathcal{T}_{cons}$ on $U \cap V$ is that of $(U \cap V)^{cons}$ `(1.9.14, (vi))` and the identity map $(U \cap
V)^{cons} \to U \cap V$ is continuous, one concludes that $U \cap V$ is quasi-compact for the topology induced by
$\mathcal{T}$; $X$ is consequently quasi-separated by virtue of `(1.2.7)`.

(iii) is an immediate corollary of (i) and (ii).

(iv) For every $x \in X$, an affine open neighbourhood $U$ of $x$ for $\mathcal{T}$ is also a neighbourhood of $x$ for
$\mathcal{T}_{cons}$, and it is compact by virtue of (iii) and `(1.9.14, (vi))`, the topology induced on $U$ by
$\mathcal{T}_{cons}$ being identical to that of $U^{cons}$.

(v) Suppose $f$ quasi-compact; then one already knows `(1.9.14, (iv))` that $f^{cons}$ is a closed map. Let on the other
hand $y$ be a point of $Y$, and set

```text
  Z = f⁻¹(y) = X ×_Y Spec(k(y));
```

$Z$ is quasi-compact `(1.1.2, (iii))` and as the canonical morphism $p : Z \to X$ is injective, it results from (i) and
from the fact that the map $p^{cons}$ is continuous that the topology induced on $f^{-1}(y)$ by that of $X^{cons}$ makes
$f^{-1}(y)$ a quasi-compact space. This proves that $f^{cons}$ is a proper map
`(Bourbaki, Top. gén., chap. I, 3e éd., §10, n° 2, th. 1)`. Conversely, suppose the continuous map $f^{cons}$ is proper,
and let $V$ be a quasi-compact open of $Y$; if $h : V \to Y$ is the canonical injection, `h^cons : V^cons → Y^cons` is
continuous and injective and $V^{cons}$ is quasi-compact by (i), so the topology induced on $V$ by that of $Y^{cons}$
makes $V$ a quasi-compact space. The hypothesis that $f^{cons}$ is proper then entails that the topology induced on
$f^{-1}(V)$ by that of $X^{cons}$ makes $f^{-1}(V)$ a quasi-compact space `(loc. cit., prop. 6)`, so $f^{-1}(V)$ is also
a quasi-compact subspace of $X$, which shows that the morphism $f$ is quasi-compact.

**(1.9.16)**

<!-- label: IV.1.9.16 -->

We shall show later how one may, for every prescheme $X$, endow the space $X^{cons}$ with a sheaf of rings making it a
prescheme whose local rings are all fields, identical to the residue fields at the points of $X$. Such preschemes are
introduced, for example, in a natural way in the translation, in the language of schemes, of Néron's constructions [32]
in his theory of the reduction of abelian varieties.

<!-- original page 249 -->

### 1.10. Application to open morphisms

**Theorem (1.10.1).**

<!-- label: IV.1.10.1 -->

*Let $X$ be a prescheme, $E$ an ind-constructible part of $X$ `(1.9.4)`, $x$ a point of $X$. For $x$ to be interior to
$E$, it is necessary and sufficient that every generization $(0_{I}, 2.1.2)$ $x'$ of $x$ belong to $E$, in other words
`(I, 2.4.2)` that one have $\operatorname{Spec}(\mathcal{O}_{X,x}) \subset E$.*

The condition is obviously necessary, every neighbourhood of $x$ containing the generizations of $x$. To see that it is
sufficient, one may obviously restrict to the case where $X = \operatorname{Spec}(A)$ is affine, $x$ being a prime ideal
$\mathfrak{p}$ of $A$. One then knows `(1.9.5, (ix))` that there exists an affine scheme $X' = \operatorname{Spec}(A')$
and a morphism $f : X' \to X$ such that $f(X') = X - E$. Set $Y = \operatorname{Spec}(\mathcal{O}_{X,x})$ and $Y' = X'
\times_{X} Y$; the hypothesis means (by virtue of `(I, 3.6.5)`) that one has $Y' = \emptyset$, in other words $A'
\otimes_{A} A_{\mathfrak{p}} = 0$. As $A_{\mathfrak{p}} = \varinjlim A_{t}$, where $t$ runs over $A - \mathfrak{p}$
$(0_{I}, 1.4.5)$, one has $\varinjlim A'_{t} = 0$, the functor $\varinjlim$ commuting with the tensor product.
Consequently `(1.9.1)`, there exists a $t \in A - \mathfrak{p}$ such that $A'_{t} = 0$, and $D(t)$ is then an open
neighbourhood of $x$ in $X$ contained in $E$.

**Corollary (1.10.2).**

<!-- label: IV.1.10.2 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, and let $y \in Y$. For $y$ to be interior to $f(X)$ it
is necessary and sufficient that every generization $y'$ of $y$ belong to $f(X)$.*

One knows indeed `(1.9.5, (viii))` that $f(X)$ is ind-constructible in $Y$, and it suffices to apply `(1.10.1)`.

We shall say that a continuous map $f : X \to Y$ is **open at a point $x \in X$** if the image under $f$ of every
neighbourhood of $x$ in $X$ is a neighbourhood of $f(x)$ in $Y$.

**Proposition (1.10.3).**

<!-- label: IV.1.10.3 -->

*Let $f : X \to Y$ be a morphism, $x$ a point of $X$, $y = f(x)$. Consider the following conditions:*

*a) $f$ is open at the point $x$.*

*b) For every generization $y'$ of $y$, there exists a generization $x'$ of $x$ such that $f(x') = y'$.*

*b') The image under $f$ of $\operatorname{Spec}(\mathcal{O}_{X,x})$ is $\operatorname{Spec}(\mathcal{O}_{Y,y})$.*

*c) For every irreducible closed part $Y'$ of $Y$ containing $y$, there exists an irreducible component of $X' =
f^{-1}(Y')$ containing $x$ and dominating $Y'$.*

*Then one has the implications a) ⟹ b) ⟺ b') ⟸ c). If in addition $f$ is locally of finite presentation, the four
conditions are equivalent.*

By definition of a generization, the image under $f$ of $\operatorname{Spec}(\mathcal{O}_{X,x})$ is always contained in
$\operatorname{Spec}(\mathcal{O}_{Y,y})$, so b) and b') are equivalent. It is immediate that c) entails b), because if
$y'$ is a generization of $y$, $Y' = \overline{y'}$ is an irreducible part of $Y$ containing $y$; if $x'$ is the generic
point of an irreducible component of $f^{-1}(Y')$ which contains $x$ and dominates $Y'$, one has $f(x') = y'$ $(0_{I},
2.1.5)$ and $x'$ is a generization of $x$. Conversely, b) entails c): indeed, let $y'$ be the generic point of $Y'$ and
let $x'$ be a generization of $x$ such that $f(x') = y'$; let $Z'$ be an irreducible component of $f^{-1}(Y')$
containing $x'$ (hence $x$); as $f(x')$ is already dense in $Y'$, *a fortiori* so is $f(Z')$.

To see that a) entails b'), one may obviously restrict to the case where $X = \operatorname{Spec}(B)$ and $Y =
\operatorname{Spec}(A)$ are affine, $x$ being a prime ideal $\mathfrak{q}$ of $B$, so that $\mathcal{O}_{X,x} =
B_{\mathfrak{q}} = \varinjlim B_{t}$,

<!-- original page 250 -->

where $t$ runs over $B - \mathfrak{q}$. One then has, by `(1.9.2)`, $f(\operatorname{Spec}(\mathcal{O}_{X,x})) =
\bigcap_{t} f(\operatorname{Spec}(B_{t})) = \bigcap_{t} f(D(t))$, and by hypothesis, for every $t \in B - \mathfrak{q}$,
$y$ is interior to $f(D(t))$, so $f(D(t))$ contains $\operatorname{Spec}(\mathcal{O}_{Y,y})$; whence
$\operatorname{Spec}(\mathcal{O}_{Y,y}) \subset f(\operatorname{Spec}(\mathcal{O}_{X,x}))$, which establishes our
assertion. Finally, when $f$ is locally of finite presentation, b) implies a) by virtue of `(1.10.2)` applied to the
restriction $U \to Y$ of $f$ to an arbitrary open neighbourhood $U$ of $x$.

**Corollary (1.10.4).**

<!-- label: IV.1.10.4 -->

*Let $f : X \to Y$ be a morphism. Consider the following conditions:*

*a) $f$ is open.*

*b) For every $x \in X$ and every generization $y'$ of $y = f(x)$, there exists a generization $x'$ of $x$ such that
$f(x') = y'$.*

*b') For every $x \in X$, the image under $f$ of $\operatorname{Spec}(\mathcal{O}_{X,x})$ is
$\operatorname{Spec}(\mathcal{O}_{Y,f(x)})$.*

*c) For every irreducible closed part $Y'$ of $Y$, every irreducible component of $f^{-1}(Y')$ dominates $Y'$.*

*Then one has the implications a) ⟹ b) ⟺ b') ⟸ c). If in addition $f$ is locally of finite presentation, the four
conditions are equivalent.*

To say that $f$ is open means that $f$ is open at every point $x \in X$, so the implications a) ⟹ b) ⟺ b') result from
the analogous implications in `(1.10.3)`, as does the implication b) ⟹ a) when $f$ is locally of finite presentation.
The implication c) ⟹ b) also results from the analogous implication in `(1.10.3)`; let us finally prove that b) entails
c). Indeed, let $x'$ be the generic point of an irreducible component of $f^{-1}(Y')$, and let us show that $y' = f(x')$
is the generic point of $Y'$. Let `y''` be a generization of $y'$; there exists by hypothesis a generization `x''` of
$x'$ such that $f(x'') = y''$, and as $x'' \in f^{-1}(Y')$, one has necessarily $x'' = x'$, hence $y'' = y'$, which
completes the proof.

*(To be continued.)*
