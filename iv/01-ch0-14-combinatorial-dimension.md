<!-- original page 102 -->

## §14. Combinatorial dimension of a topological space

### 14.1. Combinatorial dimension of a topological space

**(14.1.1)** Let $I$ be an ordered set; a *chain* of elements of $I$ is by definition a finite strictly increasing
sequence $i_{0} < i_{1} < \cdots < i_{n}$ of elements of $I$ ($n \geq 0$); by definition the *length* of this chain is
$n$. If $X$ is a topological space, the set of its irreducible closed subsets is ordered by inclusion, whence the notion
of a *chain of irreducible closed subsets of $X$*.

**Definition (14.1.2).**

<!-- label: 0_IV.14.1.2 -->

*Let $X$ be a topological space. We call **combinatorial dimension** of $X$ (or simply **dimension** of $X$, if no
confusion can arise) and denote $\dim_{c}(X)$, or simply $\dim(X)$, the supremum of the lengths of chains of irreducible
closed subsets of $X$. For every $x \in X$, we call **combinatorial dimension of $X$ at $x$** (or simply **dimension of
$X$ at $x$**) and denote $\dim_{x}(X)$ the number $\inf_{U}(\dim(U))$, where $U$ ranges over the set of open
neighbourhoods of $x$ in $X$.*

It follows from this definition that one has

$$ \dim(\emptyset) = -\infty $$

(the supremum in $\bar{R}$ of the empty subset being $-\infty$). If $(X_{\alpha})$ is the family of irreducible
components of $X$, one has

```text
  dim(X) = sup_α dim(X_α)                                                                  (14.1.2.1)
```

since every chain of irreducible closed subsets of $X$ is by definition contained in an irreducible component of $X$,
and conversely these components are closed in $X$, so every irreducible closed subset of an $X_{\alpha}$ is an
irreducible closed subset of $X$.

**Definition (14.1.3).**

<!-- label: 0_IV.14.1.3 -->

*We say that a topological space $X$ is **equidimensional** if all its irreducible components have the same dimension
(then equal to $\dim(X)$ by `(14.1.2.1)`).*

**Proposition (14.1.4).**

<!-- label: 0_IV.14.1.4 -->

*(i) For every subset $Y$ of a topological space $X$, one has $\dim(Y) \leq \dim(X)$.*

*(ii) If a topological space $X$ is a finite union of closed subsets $X_{i}$, one has `dim(X) = sup_i dim(X_i)`.*

For every irreducible closed subset $Z$ of $Y$, the closure $\bar{Z}$ of $Z$ in $X$ is irreducible $(0_{I}, 2.1.2)$ and
$\bar{Z} \cap Y = Z$, whence (i). On the other hand, if $X = \bigcup^{n}_{i=1} X_{i}$, where the $X_{i}$ are closed,
every irreducible closed subset of $X$ is contained in one of the $X_{i}$ $(0_{I}, 2.1.1)$, and consequently every chain
of irreducible closed subsets of $X$ is contained in one of the $X_{i}$; whence (ii).

From `(14.1.4, (i))` one deduces that for every $x \in X$, one can also write

```text
  dim_x(X) = lim_U dim(U)                                                                  (14.1.4.1)
```

the limit being taken along the decreasing filtered set of open neighbourhoods of $x$ in $X$.

<!-- original page 103 -->

**Corollary (14.1.5).**

<!-- label: 0_IV.14.1.5 -->

*Let $X$ be a topological space, $x$ a point of $X$, $U$ a neighbourhood of $x$, $Y_{i}$ $(1 \leq i \leq n)$ closed
subsets of $U$ such that $x \in Y_{i}$ for every $i$ and such that $U$ is the union of the $Y_{i}$. Then one has*

```text
  dim_x(X) = sup_i (dim_x(Y_i)).                                                           (14.1.5.1)
```

It follows from `(14.1.4, (ii))` that one has `dim_x(X) = inf_V (sup_i (dim(Y_i ∩ V)))` as $V$ ranges over the set of
open neighbourhoods of $x$ contained in $U$; likewise one has `dim_x(Y_i) = inf_V (dim(Y_i ∩ V))` for every $i$. The
corollary is thus obvious if

$$ \sup_{i} (\dim_{x}(Y_{i})) = +\infty; $$

in the contrary case, there is an open neighbourhood $V_{0} \subset U$ of $x$ such that $\dim(Y_{i} \cap V) =
\dim_{x}(Y_{i})$ for $1 \leq i \leq n$ and for every $V \subset V_{0}$, whence the conclusion.

**Proposition (14.1.6).**

<!-- label: 0_IV.14.1.6 -->

*For every topological space $X$, one has `dim(X) = sup_{x ∈ X} dim_x(X)`.*

It follows from definition `(14.1.2)` and proposition `(14.1.4)` that $\dim_{x}(X) \leq \dim(X)$ for every $x \in X$. On
the other hand, let $Z_{0} \subset Z_{1} \subset \cdots \subset Z_{n}$ be a chain of irreducible closed subsets of $X$,
and let $x \in Z_{0}$; for every open set $U \subset X$ containing $x$, $U \cap Z_{i}$ is irreducible $(0_{I}, 2.1.6)$
and closed in $U$, and since $U \cap Z_{i} \overline{=} Z_{i}$ in $X$, the $U \cap Z_{i}$ are pairwise distinct; hence
$\dim(U) \geq n$, which completes the proof.

**Corollary (14.1.7).**

<!-- label: 0_IV.14.1.7 -->

*If $(X_{\alpha})$ is an open cover of $X$, or a locally finite closed cover of $X$, one has
`dim(X) = sup_α (dim(X_α))`.*

If $X_{\alpha}$ is a neighbourhood of $x \in X$, one has $\dim_{x}(X) \leq \dim(X_{\alpha})$, whence the first
assertion. On the other hand, if the $X_{\alpha}$ are closed and if $U$ is a neighbourhood of $x \in X$ meeting only a
finite number of the sets $X_{\alpha}$, one has `dim_x(X) ≤ dim(U) = sup_α (dim(U ∩ X_α)) ≤ sup_α (dim(X_α))` by
`(14.1.4)`, whence the second assertion.

**Corollary (14.1.8).**

<!-- label: 0_IV.14.1.8 -->

*Let $X$ be a Noetherian Kolmogorov space $(0_{I}, 2.1.3)$, and let $F$ be the set of closed points of $X$. Then
`dim(X) = sup_{x ∈ F} dim_x(X)`.*

With the notation of the proof of `(14.1.6)`, it suffices to remark that there exists in `Z_0` a closed point $(0_{I},
2.1.3)$.

**Proposition (14.1.9).**

<!-- label: 0_IV.14.1.9 -->

*Let $X$ be a non-empty Noetherian Kolmogorov space. For $\dim(X) = 0$, it is necessary and sufficient that $X$ be
finite and discrete.*

If a space $X$ is Hausdorff (and a fortiori if $X$ is a discrete space), the only irreducible closed subsets of $X$ are
reduced to a point, so $\dim(X) = 0$. Conversely, suppose that $X$ is a Noetherian Kolmogorov space such that $\dim(X) =
0$; since every irreducible component of $X$ contains a closed point $(0_{I}, 2.1.3)$, it must be reduced to that point.
Since $X$ has only a finite number of irreducible components, it is finite and discrete.

**Corollary (14.1.10).**

<!-- label: 0_IV.14.1.10 -->

*Let $X$ be a Noetherian Kolmogorov space. For a point $x \in X$ to be isolated, it is necessary and sufficient that
$\dim_{x}(X) = 0$.*

The condition is obviously necessary (without hypothesis on $X$). It is sufficient,

<!-- original page 104 -->

since it follows that $\dim(U) = 0$ for an open neighbourhood $U$ of $x$, and since $U$ is a Noetherian Kolmogorov
space, $U$ is finite and discrete.

**Proposition (14.1.11).**

<!-- label: 0_IV.14.1.11 -->

*The function $x \mapsto \dim_{x}(X)$ is upper semi-continuous on $X$.*

It is clear that this function is upper semi-continuous at every point where it equals $+\infty$. So suppose
$\dim_{x}(X) = n < +\infty$; then formula `(14.1.4.1)` shows that there exists an open neighbourhood `U_0` of $x$ such
that $\dim(U) = n$ for every open neighbourhood $U \subset U_{0}$ of $x$. Granting that, for every $y \in U_{0}$ and
every open neighbourhood $V \subset U_{0}$ of $y$, one has $\dim(V) \leq \dim(U_{0}) = n$ `(14.1.4)`; one then deduces
from `(14.1.4.1)` that $\dim_{y}(X) \leq n$.

**Remark (14.1.12).**

<!-- label: 0_IV.14.1.12 -->

*If $X$, $Y$ are two topological spaces, and $f : X \to Y$ a continuous map, one can have $\dim(f(X)) > \dim(X)$; an
example is obtained by taking for $X$ a discrete space with two elements $a$, $b$, for $Y$ the set `{a, b}` equipped
with the topology for which the closed sets are $\emptyset$, ${a}$ and `{a, b}`; if $f : X \to Y$ is the identity map,
one has $\dim(Y) = 1$ and $\dim(X) = 0$. One will note that $Y$ is the spectrum of a discrete valuation ring $A$, of
which $a$ is the unique closed point and $b$ the generic point; if $K$ and $k$ are the field of fractions and the
residue field of $A$, $X$ is the spectrum of the ring $k \times K$ and $f$ the continuous map corresponding to the
homomorphism $(\phi, \psi) : A \to k \times K$, where $\phi : A \to k$ and $\psi : A \to K$ are the canonical
homomorphisms (cf. `(IV, 5.4.3)`).*

### 14.2. Codimension of a closed subset

**Definition (14.2.1).**

<!-- label: 0_IV.14.2.1 -->

*Given an irreducible closed subset $Y$ of a topological space $X$, we call **combinatorial codimension** (or simply
**codimension**) of $Y$ in $X$, and denote $codim(Y, X)$, the supremum of the lengths of chains of irreducible closed
subsets of $X$ of which $Y$ is the smallest element. If $Y$ is an arbitrary closed subset of $X$, we call **codimension
of $Y$ in $X$**, and again denote $codim(Y, X)$, the infimum of the codimensions in $X$ of the irreducible components of
$Y$. We say that $X$ is **equicodimensional** if all the minimal irreducible closed subsets of $X$ have the same
codimension in $X$.*

It follows from this definition that $codim(\emptyset, X) = +\infty$, the infimum in $\bar{R}$ of the empty subset being
$+\infty$. If $Y$ is closed in $X$ and if $(X_{\alpha})$ (resp. $(Y_{\beta})$) is the family of irreducible components
of $X$ (resp. $Y$), every $Y_{\beta}$ is contained in some $X_{\alpha}$, and more generally every chain of irreducible
closed subsets of $X$ of which $Y_{\beta}$ is the smallest element consists of subsets of some $X_{\alpha}$; one
therefore has

```text
  codim(Y, X) = inf_β (sup_α (codim(Y_β, X_α)))                                            (14.2.1.1)
```

where for each $\beta$, $\alpha$ ranges over the set of indices such that $Y_{\beta} \subset X_{\alpha}$.

**Proposition (14.2.2).**

<!-- label: 0_IV.14.2.2 -->

*Let $X$ be a topological space.*

*(i) If $\Phi$ is the set of irreducible closed subsets of $X$, one has*

```text
  dim(X) = sup_{Y ∈ Φ} (codim(Y, X)).                                                      (14.2.2.1)
```

<!-- original page 105 -->

*(ii) For every non-empty closed subset $Y$ of $X$, one has*

```text
  dim(Y) + codim(Y, X) ≤ dim(X).                                                           (14.2.2.2)
```

*(iii) If $Y$, $Z$, $T$ are three closed subsets of $X$ such that $Y \subset Z \subset T$, one has*

```text
  codim(Y, Z) + codim(Z, T) ≤ codim(Y, T).                                                 (14.2.2.3)
```

*(iv) For a closed subset $Y$ of $X$ to be such that $codim(Y, X) = 0$, it is necessary and sufficient that $Y$ contain
an irreducible component of $X$.*

Assertions (i) and (iv) are immediate consequences of the definition `(14.2.1)`. To prove (ii), one can restrict to the
case where $Y$ is irreducible, and then the formula follows from the definitions `(14.1.1)` and `(14.2.1)`. Finally, to
prove (iii), one can, by virtue of definition `(14.2.1)`, first restrict to the case where $Y$ is irreducible; then
`codim(Y, Z) = sup_α (codim(Y, Z_α))` for the irreducible components $Z_{\alpha}$ of $Z$ containing $Y$; it is clear
that $codim(Y, T) \geq codim(Y, Z)$, so the inequality is true if $codim(Y, Z) = +\infty$; otherwise, there exists an
$\alpha$ such that $codim(Y, Z) = codim(Y, Z_{\alpha})$ and by virtue of `(14.2.1)`, one can restrict to the case where
$Z$ is also irreducible; but then the inequality `(14.2.2.3)` is an obvious consequence of definition `(14.2.1)`.

**Proposition (14.2.3).**

<!-- label: 0_IV.14.2.3 -->

*Let $X$ be a topological space, $Y$ a closed subset of $X$. For every open set $U$ in $X$, one has*

```text
  codim(Y ∩ U, U) ≥ codim(Y, X).                                                           (14.2.3.1)
```

*Moreover, for the two members of `(14.2.3.1)` to be equal, it is necessary and sufficient that, if $(Y_{\alpha})$ is
the family of irreducible components of $Y$ meeting $U$, one have `codim(Y, X) = inf_α (codim(Y_α, X))`.*

We know $(0_{I}, 2.1.6)$ that $Z \mapsto \bar{Z}$ is a bijection from the set of irreducible closed subsets of $U$ onto
the set of irreducible closed subsets of $X$ meeting $U$, and in particular makes the irreducible components of $Y \cap
U$ correspond to the irreducible components of $Y$ meeting $U$; if $Y_{\alpha}$ is one of the latter, one therefore has
$codim(Y_{\alpha}, X) = codim(Y_{\alpha} \cap U, U)$, and the proposition then follows from definition `(14.2.1)`.

**Definition (14.2.4).**

<!-- label: 0_IV.14.2.4 -->

*Let $X$ be a topological space, $Y$ a closed subset of $X$, $x$ a point of $X$. We call **codimension of $Y$ in $X$ at
the point $x$** and denote $codim_{x}(Y, X)$ the number $\sup_{U} (codim(Y \cap U, U))$, where $U$ ranges over the set
of open neighbourhoods of $x$ in $X$.*

By virtue of `(14.2.3)`, one can also write

```text
  codim_x(Y, X) = lim_U (codim(Y ∩ U, U))                                                  (14.2.4.1)
```

the limit being taken along the decreasing filtered set of open neighbourhoods of $x$ in $X$. One will note that one has

```text
  codim_x(Y, X) = +∞    if    x ∈ X − Y.
```

<!-- original page 106 -->

**Proposition (14.2.5).**

<!-- label: 0_IV.14.2.5 -->

*If $(Y_{i})_{1 \leq i \leq n}$ is a finite family of closed subsets of a topological space $X$, and $Y$ the union of
this family, one has*

```text
  codim(Y, X) = inf_i (codim(Y_i, X)).                                                     (14.2.5.1)
```

Indeed, every irreducible component of one of the $Y_{i}$ is contained in an irreducible component of $Y$, and
conversely every irreducible component of $Y$ is also an irreducible component of one of the $Y_{i}$ $(0_{I}, 2.1.1)$;
the conclusion thus follows from definition `(14.2.1)` and inequality `(14.2.2.3)`.

**Corollary (14.2.6).**

<!-- label: 0_IV.14.2.6 -->

*Let $X$ be a topological space, $Y$ a locally Noetherian closed subspace of $X$.*

*(i) For every $x \in X$, there exist only a finite number of irreducible components $Y_{i}$ $(1 \leq i \leq n)$ of $Y$
containing $x$, and one has `codim_x(Y, X) = inf_i (codim(Y_i, X))`.*

*(ii) The function $x \mapsto codim_{x}(Y, X)$ is lower semi-continuous on $X$.*

Indeed, by hypothesis there is an open neighbourhood `U_0` of $x$ in $X$ such that $Y \cap U_{0}$ is Noetherian, hence
has only a finite number of irreducible components, which are traces on `U_0` of irreducible components of $Y$; a
fortiori, there are only a finite number of irreducible components $Y_{i}$ $(1 \leq i \leq n)$ of $Y$ containing $x$,
and one can, by replacing `U_0` by an open neighbourhood $U \subset U_{0}$ of $x$ meeting none of the $Y_{i}$ that do
not contain $x$, assume that the $Y_{i} \cap U$ are the irreducible components of $Y \cap U$; for every open
neighbourhood $V \subset U$ of $x$ in $X$, the $Y_{i} \cap V$ are then the irreducible components of $Y \cap V$, and
`(14.2.3)` then shows that $codim(Y_{i}, X) = codim(Y_{i} \cap V, V)$, which proves (i). Moreover, for every $x' \in U$,
the irreducible components of $Y$ containing $x'$ are some of the $Y_{i}$, so $codim_{x'}(Y, X) \geq codim_{x}(Y, X)$,
which proves (ii).

### 14.3. The chain condition

**(14.3.1)** In a topological space $X$, we shall say that a chain $Z_{0} \subset Z_{1} \subset \cdots \subset Z_{n}$ of
irreducible closed subsets is *saturated* if there is no irreducible closed subset $Z'$ distinct from the $Z_{i}$ and
such that $Z_{k} \subset Z' \subset Z_{k+1}$ for some index $k$.

**Proposition (14.3.2).**

<!-- label: 0_IV.14.3.2 -->

*Let $X$ be a topological space such that, for any two irreducible closed subsets $Y$, $Z$ of $X$ with $Y \subset Z$,
one has $codim(Y, Z) < +\infty$. The two following conditions are equivalent:*

*a) Two saturated chains of irreducible closed subsets of $X$, having the same extremities, have the same length.*

*b) If $Y$, $Z$, $T$ are three irreducible closed subsets of $X$ such that $Y \subset Z \subset T$, one has*

```text
  codim(Y, T) = codim(Y, Z) + codim(Z, T).                                                 (14.3.2.1)
```

It is immediate that a) entails b). Conversely, suppose b) verified, and let us show that if two saturated chains with
the same extremities have lengths $m$ and $n \leq m$, one necessarily has $m = n$. We argue by induction on $n$, the
proposition being obvious for $n = 1$. So suppose $n > 1$, $n < m$, and let $Z_{0} \subset Z_{1} \subset \cdots \subset
Z_{n}$ be a

<!-- original page 107 -->

saturated chain such that there exists another saturated chain with extremities `Z_0`, $Z_{n}$ and of length $m$. Since
$codim(Z_{0}, Z_{n}) \geq m > n$ and $codim(Z_{0}, Z_{1}) = 1$, it follows from b) that $codim(Z_{1}, Z_{n}) =
codim(Z_{0}, Z_{n}) - 1 > n - 1$, which contradicts the induction hypothesis.

When the conditions of `(14.3.2)` are satisfied, one says that $X$ satisfies the *chain condition*, or also is a
*catenary space*. It is clear that every closed subspace of a catenary space is catenary.

**Proposition (14.3.3).**

<!-- label: 0_IV.14.3.3 -->

*Let $X$ be a Noetherian Kolmogorov space of finite dimension. The following conditions are equivalent:*

*a) Two maximal chains of irreducible closed subsets of $X$ have the same length.*

*b) $X$ is equidimensional, equicodimensional, and catenary.*

*c) $X$ is equidimensional, and for any two irreducible closed subsets $Y$, $Z$ of $X$ such that $Y \subset Z$, one has*

```text
  dim(Z) = dim(Y) + codim(Y, Z).                                                           (14.3.3.1)
```

*d) $X$ is equicodimensional and for any two irreducible closed subsets $Y$, $Z$ of $X$ such that $Y \subset Z$, one
has*

```text
  codim(Y, X) = codim(Y, Z) + codim(Z, X).                                                 (14.3.3.2)
```

The hypotheses on $X$ entail that the extremities of a maximal chain of irreducible closed subsets of $X$ are
necessarily a closed point and an irreducible component of $X$ $(0_{I}, 2.1.3)$; moreover, every saturated chain with
extremities $Y$, $Z$ (with $Y \subset Z$) is contained in a maximal chain whose elements other than those of the given
chain are either contained in $Y$ or contain $Z$. These remarks at once establish the equivalence of a) and b), and also
prove that if a) is verified, one has, for every irreducible closed subset $Y$ of $X$,

```text
  dim(Y) + codim(Y, X) = dim(X);                                                           (14.3.3.3)
```

since `(14.3.2.1)` holds, one deduces `(14.3.3.1)` and `(14.3.3.2)` at once from `(14.3.3.3)`. Conversely, `(14.3.3.1)`
entails `(14.3.2.1)`, hence `(14.3.3.1)` entails the chain condition by virtue of `(14.3.2)`; moreover, applying
`(14.3.3.1)` to the case where $Y$ is reduced to a closed point $x$ of $X$ and $Z$ to an irreducible component of $X$,
one obtains $codim({x}, X) = \dim(Z)$; one concludes that c) entails b). Similarly, `(14.3.3.2)` entails `(14.3.2.1)`,
hence the chain condition; moreover, with the same choice of $Y$ and $Z$ as above, `(14.3.3.2)` again entails
$codim({x}, X) = \dim(Z)$, so (since every irreducible component of $X$ contains a closed point by virtue of $(0_{I},
2.1.3)$), d) entails b).

One says that a Noetherian Kolmogorov space is *biequidimensional* if it is of finite dimension and if it verifies the
equivalent conditions of `(14.3.3)`.

**Corollary (14.3.4).**

<!-- label: 0_IV.14.3.4 -->

*Let $X$ be a biequidimensional Noetherian Kolmogorov space; then, for every closed point $x$ of $X$ and every
irreducible component $Z$ of $X$, one has*

```text
  dim(X) = dim(Z) = codim({x}, X) = dim_x(X).                                              (14.3.4.1)
```

<!-- original page 108 -->

The last equality follows from the fact that if $Y_{0} = {x} \subset Y_{1} \subset \cdots \subset Y_{m}$ is a maximal
chain of irreducible closed subsets of $X$ and $U$ an open neighbourhood of $x$, the $U \cap Y_{i}$ are pairwise
distinct irreducible closed subsets of $U$ (since $U \cap Y_{i} \overline{=} Y_{i}$), whence $\dim(U) = \dim(X)$ by
virtue of `(14.1.4)`.

**Corollary (14.3.5).**

<!-- label: 0_IV.14.3.5 -->

*Let $X$ be a Noetherian Kolmogorov space; if $X$ is biequidimensional, so is every union of irreducible components of
$X$ and every irreducible closed subset of $X$. Moreover, for every closed subset $Y$ of $X$, one then has*

```text
  dim(Y) + codim(Y, X) = dim(X).                                                           (14.3.5.1)
```

Every chain of irreducible closed subsets of $X$ being contained in an irreducible component of $X$, the first assertion
follows at once from `(14.3.3)`. Moreover, if $X'$ is an irreducible closed subset of $X$, $X'$ trivially verifies
conditions `(14.3.3, c))`, whence the second assertion.

Finally, to prove `(14.3.5.1)`, we remark that we have seen in the proof of `(14.3.3)` that this relation is verified
when $Y$ is irreducible; if $Y_{i}$ $(1 \leq i \leq m)$ are the irreducible components of $Y$, the one among the $Y_{i}$
for which $\dim(Y_{i})$ is greatest is also the one for which $codim(Y_{i}, X)$ is smallest; hence `(14.3.5.1)` follows
from the definitions of $\dim(Y)$ and $codim(Y, X)$.

**Remark (14.3.6).**

<!-- label: 0_IV.14.3.6 -->

*The reader will note that the proof of `(14.3.2)` applies to an arbitrary ordered set, the fact that one is dealing
with irreducible closed subsets of a topological space not intervening in that proof. The same holds for the proof of
`(14.3.3)` in an ordered set $E$ such that for every $x \in E$, there exists $z \leq x$ which is minimal in $E$, and in
which the length of chains of elements of $E$ is bounded.*
