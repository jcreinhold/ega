# Chapter 0_III

## §13. Projective limits in homological algebra

<!-- original page 64 -->

### 13.1. The Mittag–Leffler condition

**13.1.1.**

<!-- label: 0_III.13.1.1 -->

Let $\mathcal{C}$ be an abelian category in which infinite products exist (axiom **AB 3\*** of `(T, 1.5)`); then the
infimum of a family of subobjects of an object of $\mathcal{C}$ exists, and every projective system of objects of
$\mathcal{C}$ admits a projective limit, which is a left-exact functor of the projective system considered `(T, 1.8)`.
Let

<!-- original page 65 -->

$(A_{\alpha}, f_{\alpha \beta})$ be a projective system of objects of $\mathcal{C}$ whose index set $I$ is
right-filtered; set $A = \varprojlim A_{\alpha}$ and, for every $\alpha \in I$, let $f_{\alpha} : A \to A_{\alpha}$ be
the canonical morphism. For every $\alpha \in I$, the $f_{\alpha \beta}(A_{\beta})$ for $\beta \geq \alpha$ form a
filtered decreasing family of subobjects of $A_{\alpha}$; the subobject

```text
  A'_α = inf_{β ≥ α} f_{αβ}(A_β)
```

is called the subobject of "universal images" in $A_{\alpha}$; it is clear that $f_{\alpha}(A) \subset A'_{\alpha}$ and
$f_{\alpha \beta}(A'_{\beta}) \subset A'_{\alpha}$ for $\alpha \leq \beta$, so $(A'_{\alpha}, f_{\alpha
\beta}|A'_{\beta})$ is a projective system, and $A = \varprojlim A'_{\alpha}$.

**13.1.2.**

<!-- label: 0_III.13.1.2 -->

Given a projective system $(A_{\alpha}, f_{\alpha \beta})$ in $\mathcal{C}$, the *Mittag–Leffler condition* is the
following condition:

> `(ML)` For every index $\alpha$, there exists $\beta \geq \alpha$ such that, for every $\gamma \geq \beta$, one has
> $f_{\alpha \gamma}(A_{\gamma}) = f_{\alpha \beta}(A_{\beta})$.

It is clear that if the $f_{\alpha \beta}$ are epimorphisms, condition `(ML)` is satisfied. Conversely, if `(ML)` is
satisfied, and if for every $\alpha \in I$, $A'_{\alpha}$ is the subobject of "universal images" in $A_{\alpha}$, the
restriction of $f_{\alpha \beta}$ to $A'_{\beta}$ is an epimorphism $A'_{\beta} \to A'_{\alpha}$ for $\alpha \leq
\beta$: indeed, if $\gamma \geq \beta$ is such that $f_{\beta \delta}(A_{\delta}) = f_{\beta \gamma}(A_{\gamma})$ for
$\delta \geq \gamma$, one has $A'_{\beta} = f_{\beta \gamma}(A_{\gamma})$, and this entails on the other hand $f_{\alpha
\delta}(A_{\delta}) = f_{\alpha \gamma}(A_{\gamma})$ for $\delta \geq \gamma$, so $A'_{\alpha} = f_{\alpha
\gamma}(A_{\gamma}) = f_{\alpha \beta}(A'_{\beta})$.

Note also that condition `(ML)` is satisfied whenever the objects $A_{\alpha}$ are *artinian* in $\mathcal{C}$, that is,
every family of subobjects of $A_{\alpha}$ admits a minimal element: a minimal element of the filtered decreasing family
$(f_{\alpha \beta}(A_{\beta}))$ of subobjects of $A_{\alpha}$ is then necessarily the smallest of these subobjects.

> _Translator's note._ Throughout §13, EGA's `(ML)` denotes the Mittag–Leffler condition; we keep the EGA abbreviation.
> Modern accounts often write "ML condition" or "satisfies ML" interchangeably.

**Remark (13.1.3).**

<!-- label: 0_III.13.1.3 -->

Condition `(ML)` can also be formulated when $\mathcal{C}$ is, for example, the category of sets; one can then again
define the subset of "universal images" in $A_{\alpha}$, and the remarks made on this subject in `(13.1.1)` and
`(13.1.2)` remain valid.

### 13.2. The Mittag–Leffler condition for abelian groups

**Proposition (13.2.1).**

<!-- label: 0_III.13.2.1 -->

Let

```text
  0 → A_α --u_α--> B_α --v_α--> C_α → 0
```

be an exact sequence of projective systems of abelian groups (relative to the same right-filtered index set $I$).

- _(i)_ If $(B_{\alpha})$ satisfies `(ML)`, so does $(C_{\alpha})$.
- _(ii)_ If $(A_{\alpha})$ and $(C_{\alpha})$ satisfy `(ML)`, so does $(B_{\alpha})$.

Let $(f_{\alpha \beta})$, $(g_{\alpha \beta})$, $(h_{\alpha \beta})$ be the systems of homomorphisms defining the
projective systems $(A_{\alpha})$, $(B_{\alpha})$, $(C_{\alpha})$ respectively.

_(i)_ Suppose $g_{\alpha \beta}(B_{\beta}) = g_{\alpha \lambda}(B_{\lambda})$ for $\lambda \geq \beta$; since
$v_{\beta}$ and $v_{\lambda}$ are surjective, one has $h_{\alpha \beta}(C_{\beta}) = v_{\alpha}(g_{\alpha
\beta}(B_{\beta})) = v_{\alpha}(g_{\alpha \lambda}(B_{\lambda})) = h_{\alpha \lambda}(C_{\lambda})$ for $\lambda \geq
\beta$.

_(ii)_ Let $\alpha \in I$, and let $\beta \geq \alpha$ be an index such that for $\lambda \geq \beta$, one has
$f_{\alpha \beta}(A_{\beta}) = f_{\alpha \lambda}(A_{\lambda})$; let also $\gamma \geq \beta$ be an index such that, for
$\lambda \geq \gamma$, one has $h_{\beta \lambda}(C_{\lambda}) = h_{\beta \gamma}(C_{\gamma})$. Let then $x_{\alpha}$ be
an element of $g_{\alpha \gamma}(B_{\gamma})$; one has $x_{\alpha} = g_{\alpha \gamma}(y_{\gamma})$ with $y_{\gamma} \in
B_{\gamma}$; set $y_{\beta} = g_{\beta \gamma}(y_{\gamma})$, so that $x_{\alpha} = g_{\alpha \beta}(g_{\beta
\gamma}(y_{\gamma}))$. For every $\lambda \geq \gamma$, there exists by hypothesis $y_{\lambda} \in B_{\lambda}$ such
that $h_{\beta \gamma}(v_{\gamma}(y_{\gamma})) = h_{\beta \lambda}(v_{\lambda}(y_{\lambda})) = v_{\beta}(g_{\beta
\lambda}(y_{\lambda}))$, whence $v_{\beta}(y_{\beta} - g_{\beta \lambda}(y_{\lambda})) = 0$, and consequently there
exists $x_{\beta} \in A_{\beta}$

<!-- original page 66 -->

such that $y_{\beta} = g_{\beta \lambda}(y_{\lambda}) + u_{\beta}(x_{\beta})$. One deduces $x_{\alpha} = g_{\alpha
\lambda}(y_{\lambda}) + u_{\alpha}(f_{\alpha \beta}(x_{\beta}))$; but since $\lambda \geq \beta$, there exists
$x_{\lambda} \in A_{\lambda}$ such that $f_{\alpha \beta}(x_{\beta}) = f_{\alpha \lambda}(x_{\lambda})$, and finally
$x_{\alpha} = g_{\alpha \lambda}(y_{\lambda} + u_{\lambda}(x_{\lambda})) \in g_{\alpha \lambda}(B_{\lambda})$, which
completes the demonstration.

**Proposition (13.2.2).**

<!-- label: 0_III.13.2.2 -->

Let $I$ be a right-filtered ordered set having a countable cofinal part. Let

```text
  0 → A_α --u_α--> B_α --v_α--> C_α → 0
```

be an exact sequence of projective systems of abelian groups having $I$ as index set. If $(A_{\alpha})$ satisfies
condition `(ML)`, the sequence

```text
  0 → lim_← A_α → lim_← B_α → lim_← C_α → 0
```

is exact.

It comes down to proving that the homomorphism `v = lim_← v_α : lim_← B_α → lim_← C_α` is surjective. Let $z =
(z_{\alpha})$ be an element of $\varprojlim C_{\alpha}$, and set $E_{\alpha} = v^{-1}_{\alpha}(z_{\alpha})$; it is clear
that the $E_{\alpha}$ form a projective system of non-empty sets for the restrictions of the homomorphisms $g_{\alpha
\beta} : B_{\beta} \to B_{\alpha}$. Let us show that this projective system satisfies condition `(ML)`; identifying
$A_{\alpha}$ with a part of $B_{\alpha}$ via $u_{\alpha}$ for every $\alpha \in I$, there exists $\beta \geq \alpha$
such that $g_{\alpha \beta}(A_{\beta}) = g_{\alpha \lambda}(A_{\lambda})$ for $\lambda \geq \beta$; let us show that one
also has $g_{\alpha \beta}(E_{\beta}) = g_{\alpha \lambda}(E_{\lambda})$ for $\lambda \geq \beta$. Indeed, take
$y_{\lambda} \in E_{\lambda}$ and set $y_{\beta} = g_{\beta \lambda}(y_{\lambda})$, $y_{\alpha} = g_{\alpha
\lambda}(y_{\lambda})$; let $y'_{\alpha} \in g_{\alpha \beta}(E_{\beta})$, so that $y'_{\alpha} = g_{\alpha
\beta}(y'_{\beta})$ for some $y'_{\beta} \in E_{\beta}$; one has $y'_{\beta} - y_{\beta} = x_{\beta} \in A_{\beta}$, and
by hypothesis there exists $x_{\lambda} \in A_{\lambda}$ such that $g_{\alpha \beta}(x_{\beta}) = g_{\alpha
\lambda}(x_{\lambda})$; therefore

```text
  y'_α = g_{αβ}(y_β) + g_{αβ}(x_β) = g_{αλ}(y_λ) + g_{αλ}(x_λ)
       = g_{αλ}(y_λ + x_λ) ∈ g_{αλ}(E_λ),
```

which proves our assertion. That being so, one knows (Bourbaki, _Top. gén._, ch. II, 3rd ed., §3, th. 1) that under the
hypotheses made on $I$, a projective system of non-empty sets satisfying `(ML)` has a non-empty projective limit; in
consequence, there exists a point $y = (y_{\alpha}) \in \varprojlim E_{\alpha}$, and since $v_{\alpha}(y_{\alpha}) =
z_{\alpha}$ by definition for every $\alpha$, one has $z = v(y)$. Q.E.D.

**Proposition (13.2.3).**

<!-- label: 0_III.13.2.3 -->

The hypotheses on $I$ being those of `(13.2.2)`, let $(K^{\bullet}_{\alpha})_{\alpha \in I}$ be a projective system of
complexes of abelian groups $K^{\bullet}_{\alpha} = (K^{n}_{\alpha})_{n \in \mathbb{Z}}$ whose differential operator is
of degree `+1`. For each $n$, there exists a canonical functorial homomorphism

```text
  h_n : H^n(lim_← K^•_α) → lim_← H^n(K^•_α).                                  (13.2.3.1)
```

If, for every degree $n$, the projective system of abelian groups $(K^{n}_{\alpha})_{\alpha \in I}$ satisfies `(ML)`,
then all the homomorphisms $h_{n}$ are surjective. If in addition, for some degree $n$, the projective system
$(H^{n-1}(K^{\bullet}_{\alpha}))_{\alpha \in I}$ satisfies `(ML)`, the homomorphism $h_{n}$ is bijective.

Set, for every $n$, $K^{n} = \varprojlim K^{n}_{\alpha}$; the definition of the homomorphisms $h_{n}$ comes from the
commutativity of the diagrams

```text
  … → K^{n−1} ----> K^n ----> K^{n+1} → …
        ↓            ↓            ↓
  … → K^{n−1}_α → K^n_α → K^{n+1}_α → …
```

<!-- original page 67 -->

the differential operators in $K^{\bullet}$ being projective limits of the corresponding operators in the
$K^{\bullet}_{\alpha}$.

Consider the exact sequences

```text
  (*_n)     0 → B^n(K^•_α) → Z^n(K^•_α) → H^n(K^•_α) → 0
  (**_n)    0 → Z^{n−1}(K^•_α) → K^{n−1}_α → B^n(K^•_α) → 0
```

The hypothesis and Proposition `(13.2.1, (i))` show that the projective system $(B^{n}(K^{\bullet}_{\alpha}))_{\alpha
\in I}$ satisfies `(ML)` for every $n$; it therefore results from `(13.2.2)` that the sequence

```text
  (***_n)   0 → lim_α B^n(K^•_α) → lim_α Z^n(K^•_α) → lim_α H^n(K^•_α) → 0
```

is exact. Now it is clear that $\varprojlim B^{n}(K^{\bullet}_{\alpha})$ identifies with a subgroup of $K^{n+1}$
containing $B^{n}(K^{\bullet})$, and that $\varprojlim Z^{n}(K^{\bullet}_{\alpha})$ identifies with a subgroup of
$Z^{n}(K^{\bullet})$; in consequence, $h_{n}$ is surjective. If now one supposes furthermore that the projective system
$(H^{n-1}(K^{\bullet}_{\alpha}))_{\alpha \in I}$ satisfies `(ML)`, the exact sequences $(*_{n-1})$ and Proposition
`(13.2.1, (ii))` show that the projective system $(Z^{n-1}(K^{\bullet}_{\alpha}))_{\alpha \in I}$ satisfies `(ML)`; but
then, `(13.2.2)` applied to the exact sequences $(**_{n})$ shows that the sequence

```text
  0 → lim_α Z^{n−1}(K^•_α) → K^{n−1} --u--> lim_α B^n(K^•_α) → 0
```

is exact; since $\varprojlim B^{n}(K^{\bullet}_{\alpha}) \supset B^{n}(K^{\bullet})$, and the composite of the injection
$\varprojlim B^{n}(K^{\bullet}_{\alpha}) \to K^{n}$ with $u$ is the differential operator $K^{n-1} \to K^{n}$, the fact
that $u$ is surjective entails $\varprojlim B^{n}(K^{\bullet}_{\alpha}) = B^{n}(K^{\bullet})$, so $h_{n}$ is injective.
Q.E.D.

**Remarks (13.2.4).**

<!-- label: 0_III.13.2.4 -->

_(i)_ The reasoning of `(13.2.2)` (cf. Bourbaki, _loc. cit._) shows that the conclusion of this proposition remains
valid when one supposes only that the $A_{\alpha}$ can be equipped with structures of *complete metrizable spaces*, in
which the translations are homeomorphisms, that the maps $f_{\alpha \beta} : A_{\beta} \to A_{\alpha}$ defining the
projective system $(A_{\alpha})$ are *uniformly continuous* for the distances considered, and finally that the system
$(A_{\alpha})$ satisfies the condition

> `(ML')` For every index $\alpha$, there exists $\beta \geq \alpha$ such that, for every $\gamma \geq \beta$,
> $f_{\alpha \gamma}(A_{\gamma})$ is dense in $f_{\alpha \beta}(A_{\beta})$.

This allows one to add an analogous complement to `(13.2.3)`: suppose that $K^{n}_{\alpha} = 0$ for $n < 0$ and for
every $\alpha$; suppose moreover that $(K^{n}_{\alpha})_{\alpha \in I}$ satisfies `(ML)` for $n \geq 0$ and that the
$A_{\alpha} = H^{0}(K^{\bullet}_{\alpha})$ can be equipped with structures of metric spaces satisfying the above
properties. Then the conclusions of `(13.2.3)` are unchanged for $n \geq 2$, and in addition $h_{1}$ is bijective, since
the reasoning of `(13.2.2)` shows again that $(B^{1}(K^{\bullet}_{\alpha}))_{\alpha \in I}$ satisfies `(ML)`, that the
sequence $(***_{1})$ is exact, and finally, by virtue of the foregoing, that $\varprojlim B^{1}(K^{\bullet}_{\alpha}) =
B^{1}(K^{\bullet})$. We have thus established, among others, the assertions of `(T, 3.10.2)`.

_(ii)_ It is possible to introduce the right-derived functors $\lim^{(i)}_{\leftarrow}$ of the functor $\varprojlim$,
and to obtain more complete statements than the preceding ones `[28]`.

<!-- original page 68 -->

### 13.3. Application: cohomology of a projective limit of sheaves

**Proposition (13.3.1).**

<!-- label: 0_III.13.3.1 -->

Let $X$ be a topological space, $(\mathcal{F}_{k})_{k \in \mathbb{N}}$ a projective system of sheaves of abelian groups
on $X$, and let $\mathcal{F} = \varprojlim \mathcal{F}_{k}$. Suppose the following conditions are satisfied:

- _(i)_ There exists a base $\mathfrak{B}$ of the topology of $X$ such that, for every $U \in \mathfrak{B}$ and every $i
  \geq 0$, the projective system $(H^{i}(U, \mathcal{F}_{k}))_{k \in \mathbb{N}}$ satisfies `(ML)`.
- _(ii)_ For every $x \in X$ and every $i > 0$, one has $\lim_{U} (\varprojlim H^{i}(U, \mathcal{F}_{k})) = 0$ as $U$
  runs over the set of neighborhoods of $x$ belonging to $\mathfrak{B}$.
- _(iii)_ The homomorphisms $u_{hk} : \mathcal{F}_{k} \to \mathcal{F}_{h}$ ($h \leq k$) defining the projective system
  $(\mathcal{F}_{k})$ are surjective.

Under these conditions, for every $i > 0$, the canonical homomorphism

```text
  h_i : H^i(X, ℱ) → lim_← H^i(X, ℱ_k)
```

is surjective; if in addition, for some value of $i$, the projective system $(H^{i-1}(X, \mathcal{F}_{k}))_{k \in
\mathbb{N}}$ satisfies `(ML)`, $h_{i}$ is bijective.

_a)_ We shall first suppose that the $\mathcal{F}_{k}$ are *flasque* as well as the kernels $\mathcal{N}_{hk}$ of the
$u_{hk}$; we shall then show that condition (iii) of the statement entails $H^{i}(X, \mathcal{F}) = 0$ for $i > 0$. It
will suffice to prove that for *every* open $U$ of $X$ and every cover $\mathfrak{U}$ of $U$ by open subsets of $U$, one
has $H^{i}(\mathfrak{U}, \mathcal{F}) = 0$ for $i > 0$. It will result, first, that for Čech cohomology, one has
$\check{H}^{i}(U, \mathcal{F}) = 0$ for every $i > 0$, then (by virtue of `(G, II, 5.9.2)` applied to the set of all
open subsets of $X$) that $H^{i}(X, \mathcal{F}) = 0$ for every $i > 0$. Since the $\mathcal{F}_{k}$ are flasque, one
has $H^{i}(\mathfrak{U}, \mathcal{F}_{k}) = 0$ for $i > 0$ `(G, II, 5.2.3)`; consider for each $k$ the complex
$C^{\bullet}(\mathfrak{U}, \mathcal{F}_{k})$ of alternating cochains of the nerve of the cover $\mathfrak{U}$
`(G, II, 5.1)`, which evidently forms a projective system of complexes of abelian groups. Let us show that all the maps
$C^{\bullet}(\mathfrak{U}, \mathcal{F}_{k}) \to C^{\bullet}(\mathfrak{U}, \mathcal{F}_{h})$ ($h \leq k$) are
*surjective*. It clearly suffices, by definition, to show that for every open $V$ of $X$, the map $\Gamma(V,
\mathcal{F}_{k}) \to \Gamma(V, \mathcal{F}_{h})$ is surjective; but the sequence $0 \to \mathcal{N}_{hk} \to
\mathcal{F}_{k} \to \mathcal{F}_{h} \to 0$ being exact by hypothesis gives the exact cohomology sequence

```text
  Γ(V, ℱ_k) → Γ(V, ℱ_h) → H^1(V, 𝒩_{hk}) = 0
```

since $\mathcal{N}_{hk}$ is flasque. The projective system $(C^{\bullet}(\mathfrak{U}, \mathcal{F}_{k}))_{k \in
\mathbb{N}}$ therefore satisfies `(ML)`; the same holds for $(H^{i}(\mathfrak{U}, \mathcal{F}_{k}))_{k \in \mathbb{N}}$
for every $i \geq 0$, since this is trivial for $i > 0$, and since $H^{0}(\mathfrak{U}, \mathcal{F}_{k}) = \Gamma(U,
\mathcal{F}_{k})$ `(G, II, 5.2.2)`, condition `(ML)` is also met for $i = 0$ by what precedes. One can therefore apply
`(13.2.3)`, which shows that $H^{i}(\mathfrak{U}, \mathcal{F}) = \varprojlim H^{i}(\mathfrak{U}, \mathcal{F}_{k}) = 0$
for every $i > 0$.

_b)_ Let us pass to the general case, and consider for each $k \in \mathbb{N}$ the canonical resolution
$\mathcal{C}^{\bullet}(X, \mathcal{F}_{k}) = (\mathcal{C}^{i}(X, \mathcal{F}_{k}))_{i \geq 0}$ of $\mathcal{F}_{k}$ by
flasque sheaves `(G, II, 4.3)`. For each $i \geq 0$, it is clear that $(\mathcal{C}^{i}(X, \mathcal{F}_{k}))_{k \in
\mathbb{N}}$ is a projective system of flasque sheaves; let us

<!-- original page 69 -->

show that it satisfies the conditions of _a)_. Indeed, if $\mathcal{N}_{hk}$ is the kernel of $u_{hk}$ for $h \leq k$,
the sequence $0 \to \mathcal{N}_{hk} \to \mathcal{F}_{k} \to \mathcal{F}_{h} \to 0$ is exact by (iii), and our assertion
follows from the fact that the functor $\mathcal{A} \rightsquigarrow \mathcal{C}^{i}(X, \mathcal{A})$ is exact
`(G, II, 4.3)`. Let $\mathcal{G}^{i} = \varprojlim \mathcal{C}^{i}(X, \mathcal{F}_{k})$; one therefore has $H^{j}(X,
\mathcal{G}^{i}) = 0$ for $j > 0$ and $i \geq 0$ by virtue of _a)_. We shall show that $\mathcal{G}^{\bullet} =
(\mathcal{G}^{i})_{i \geq 0}$ is a *resolution* of the sheaf $\mathcal{F}$; since $H^{j}(X, \mathcal{G}^{\bullet}) = 0$
for $j > 0$, the cohomology $H^{\bullet}(X, \mathcal{F})$ will equal $H^{\bullet}(\Gamma(X, \mathcal{G}^{\bullet}))$
`(G, II, 4.7.1)`.

It is clear that, by passage to the projective limit, one deduces from the exact sequences

```text
  0 → ℱ_k → 𝒞^0(X, ℱ_k) → 𝒞^1(X, ℱ_k) → …
```

a complex of sheaves of abelian groups

$$ 0 \to \mathcal{F} \to \mathcal{G}^{0} \to \mathcal{G}^{1} \to \cdots . $$

To prove our assertion, one must establish that $\mathcal{H}^{i}(\mathcal{G}^{\bullet}) = 0$ for $i > 0$. This sheaf is
generated by the presheaf $U \mapsto H^{i}(\Gamma(U, \mathcal{G}^{\bullet}))$ `(G, II, 4.1)`; now, the complex
$\Gamma(U, \mathcal{G}^{\bullet})$ is the projective limit of the projective system of complexes of abelian groups
$(\Gamma(U, \mathcal{C}^{\bullet}(X, \mathcal{F}_{k})))_{k \in \mathbb{N}}$ $(0_{I}, 3.2.6)$. We have seen in _a)_ that
for each $i \geq 0$, the maps $\Gamma(U, \mathcal{C}^{i}(X, \mathcal{F}_{k})) \to \Gamma(U, \mathcal{C}^{i}(X,
\mathcal{F}_{h}))$ ($h \leq k$) are *surjective*; on the other hand, one has $H^{i}(U, \mathcal{F}_{k}) =
H^{i}(\Gamma(U, \mathcal{C}^{\bullet}(X, \mathcal{F}_{k})))$, the canonical resolution $\mathcal{C}^{\bullet}(U,
\mathcal{F}_{k}|U)$ being induced on $U$ by $\mathcal{C}^{\bullet}(X, \mathcal{F}_{k})$; by virtue of hypothesis (i),
for every $U \in \mathfrak{B}$, one can apply `(13.2.3)` to the projective system of complexes $(\Gamma(U,
\mathcal{C}^{\bullet}(X, \mathcal{F}_{k})))_{k \in \mathbb{N}}$, and one therefore has $H^{i}(\Gamma(U,
\mathcal{G}^{\bullet})) = \varprojlim H^{i}(U, \mathcal{F}_{k})$ for every $i \geq 0$. Hypothesis (ii) then proves
indeed, by definition, that the sheaves $\mathcal{H}^{i}(\mathcal{G}^{\bullet})$ are zero for $i > 0$.

One has then for every $i \geq 0$, $H^{i}(X, \mathcal{F}) = H^{i}(\Gamma(X, \mathcal{G}^{\bullet}))$ and

```text
  Γ(X, 𝒢^•) = lim_← Γ(X, 𝒞^•(X, ℱ_k)).
```

We have just remarked that the maps $\Gamma(X, \mathcal{C}^{i}(X, \mathcal{F}_{k})) \to \Gamma(X, \mathcal{C}^{i}(X,
\mathcal{F}_{h}))$ ($h \leq k$) are all surjective; the conclusion therefore again results from `(13.2.3)`.

**Remarks (13.3.2).**

<!-- label: 0_III.13.3.2 -->

_(i)_ The statement `(13.3.1)` is of interest only for $i > 0$, since for $i = 0$, $h_{0}$ is always an isomorphism
without hypothesis $(0_{I}, 3.2.6)$.

_(ii)_ Conditions (i) and (ii) of `(13.3.1)` will in particular be satisfied if $H^{i}(U, \mathcal{F}_{k}) = 0$ for
every $k$, every $i > 0$ and every $U \in \mathfrak{B}$, and if for $U \in \mathfrak{B}$, the maps $\Gamma(U,
\mathcal{F}_{k}) \to \Gamma(U, \mathcal{F}_{h})$ are surjective. This will be the most frequent case of application of
`(13.3.1)`.

### 13.4. The Mittag–Leffler condition and graded objects associated to projective systems

**13.4.1.**

<!-- label: 0_III.13.4.1 -->

Let $\mathbf{A} = (A_{k}, u_{hk})_{k \in \mathbb{Z}}$ be a projective system in an abelian category $\mathcal{C}$; we
shall say that it is *bounded below* if there exists $k_{0}$ such that $A_{k} = 0$ for $k < k_{0}$.

We shall define on each $A_{k}$ a filtration $(F^{p}(A_{k}))_{p \in \mathbb{Z}}$ by the formulas

```text
  F^p(A_k) = Ker(A_k → A_{p−1})    for p ≤ k+1                              (13.4.1.1)
  F^p(A_k) = 0                      for p ≥ k+1
```

<!-- original page 70 -->

One has therefore by hypothesis $F^{k}(A_{k}) = A_{k}$ and $F^{k+1}(A_{k}) = 0$, in other words the filtration
considered is *finite* `(11.1.3)`. The graded objects associated to this filtration are therefore

```text
  gr^p(A_k) = Ker(A_k → A_{p−1}) / Ker(A_k → A_p)
```

and consequently $gr^{p}(A_{k})$ is isomorphic to the image under $A_{k} \to A_{p}$ of $Ker(A_{k} \to A_{p-1})$; by
virtue of the transitivity of the morphisms defining a projective system, one therefore has

```text
  gr^p(A_k) = Ker(A_p → A_{p−1}) ∩ Im(A_k → A_p)                            (13.4.1.2)
```

but since, by virtue of `(13.4.1.1)`, one has $Ker(A_{p} \to A_{p-1}) = gr^{p}(A_{p})$, one also has

```text
  gr^p(A_k) = gr^p(A_p) ∩ Im(A_k → A_p).                                    (13.4.1.3)
```

The preceding definitions show, moreover, that one has for $k \leq h$

$$ u_{hk}(F^{p}(A_{k})) \subset F^{p}(A_{h}) $$

and consequently that the $gr^{p}(u_{hk})$ define a projective system $(gr^{p}(A_{k}))_{k \in \mathbb{Z}}$ for every $p
\in \mathbb{Z}$.

**13.4.2.**

<!-- label: 0_III.13.4.2 -->

We shall say that the projective system $\mathbf{A}$ is *essentially constant* if the morphisms $A_{k+1} \to A_{k}$ are
isomorphisms for $k$ large enough. We shall say that the projective system $\mathbf{A}$ is *strict* if the morphisms
$A_{i} \to A_{j}$ ($j \leq i$) are epimorphisms. When $\mathbf{A}$ is strict, it follows from `(13.4.1.3)` that for $p
\leq k \leq h$, the canonical morphism $gr^{p}(A_{h}) \to gr^{p}(A_{k})$ is an isomorphism, in other words, the
projective system $(gr^{p}(A_{k}))_{k \in \mathbb{Z}}$ is *essentially constant*. The sequence of objects
$gr^{p}(A_{p})$ (identified with $\varprojlim gr^{p}(A_{k})$ for every $p$) is then denoted $gr^{\bullet}(\mathbf{A})$
and called the *graded object associated to the strict projective system* $\mathbf{A} = (A_{k})$.

If one now supposes that the projective system $\mathbf{A}$ (bounded below) satisfies `(ML)`, one knows `(13.1.2)` that
the projective system $\mathbf{A}' = (A'_{k})$ of objects of "universal images" is *strict*, and is moreover bounded
below; the graded object $gr^{\bullet}(\mathbf{A}')$ associated to $\mathbf{A}'$ is then again called the *graded object
associated to* $\mathbf{A}$ and denoted $gr^{\bullet}(\mathbf{A})$.

**Proposition (13.4.3).**

<!-- label: 0_III.13.4.3 -->

Let $\mathbf{A} = (A_{k})_{k \in \mathbb{Z}}$ be a projective system bounded below in an abelian category $\mathcal{C}$.
The following two conditions are equivalent:

- _a)_ $\mathbf{A}$ satisfies condition `(ML)`.
- _b)_ For every $p \in \mathbb{Z}$, the projective system $(gr^{p}(A_{k}))_{k \in \mathbb{Z}}$ is essentially constant.

In addition, when these conditions are satisfied, one has for every $p \in \mathbb{Z}$ a canonical isomorphism

```text
  gr^p(𝐀) ⥲ lim_← gr^p(A_k).                                                (13.4.3.1)
            k
```

It follows immediately from `(13.4.1.2)` that _a)_ implies _b)_; the same formula applied to the projective system
$\mathbf{A}'$ (notations of `(13.4.2)`) gives the isomorphism `(13.4.3.1)` by definition. For $k \leq h$, set $A_{kh} =
Im(A_{h} \to A_{k})$; if $k \leq h \leq j$, one has $A_{kj} \subset A_{kh} \subset A_{k}$. Equip $A_{kh}$ with the
filtration induced by $(F^{p}(A_{k}))$; one verifies immediately, by virtue of the transitivity of the morphisms
defining $\mathbf{A}$, that this filtration is also the quotient filtration of $(F^{p}(A_{h}))$; consequently, one has

$$ gr^{p}(A_{kh}) = Im(gr^{p}(A_{h}) \to gr^{p}(A_{k})). (13.4.3.2) $$

<!-- original page 71 -->

That being so, suppose _b)_ verified; for every $p \in \mathbb{Z}$ and every $k \geq p$, there exists an integer $L(p,
k)$ such that the right-hand side of `(13.4.3.2)` is constant for $h \geq L(p, k)$; since $gr^{p}(A_{k}) = 0$ for $p <
k_{0}$, there is only (for $k$ given) a finite number of $L(p, k)$ non-zero when $p$ runs over the set of integers $\leq
k$. Let $L(k) = m$ be the largest of these integers; for every $h \geq m$, one has $A_{kh} \subset A_{km}$, and by
definition of $m$, the canonical injection $A_{kh} \to A_{km}$ defines an isomorphism $gr^{\bullet}(A_{kh})
\xrightarrow{\sim} gr^{\bullet}(A_{km})$; since the filtrations are finite, one concludes that the preceding injection
is itself bijective (Bourbaki, _Alg. comm._, ch. III, §2, n° 8, th. 1), which proves that $\mathbf{A}$ satisfies `(ML)`.

**13.4.4.**

<!-- label: 0_III.13.4.4 -->

Suppose that in $\mathcal{C}$ the projective limit $A = \varprojlim A_{k}$ exists. In the definitions of `(13.4.1)`, one
can then replace $A_{k}$ by $A$, and the filtration thus defined on $A$ is again such that

```text
  gr^p(A) = gr^p(A_p) ∩ Im(A → A_p).                                         (13.4.4.1)
```

**Corollary (13.4.5).**

<!-- label: 0_III.13.4.5 -->

Suppose that $\mathcal{C}$ is the category of abelian groups. If the projective system $\mathbf{A}$ satisfies `(ML)` and
if $A = \varprojlim A_{k}$, one has for every $p \in \mathbb{Z}$ a canonical isomorphism

```text
  gr^p(A) ⥲ lim_← gr^p(A_k).                                                 (13.4.5.1)
            k
```

Indeed, one has $Im(A_{k} \to A_{p}) = Im(A \to A_{p})$ whenever $k$ is large enough (Bourbaki, _Top. gén._, ch. II, 3rd
ed., §3, n° 5, th. 1), and the conclusion results from `(13.4.1.3)` and `(13.4.4.1)`.

### 13.5. Projective limits of spectral sequences of filtered complexes

**13.5.1.**

<!-- label: 0_III.13.5.1 -->

Let $\mathcal{C}$ be an abelian category, $X^{\bullet}$ a complex of objects of $\mathcal{C}$ equipped with a filtration
$(F^{p}(X^{\bullet}))_{p \in \mathbb{Z}}$ such that $F^{p_{0}}(X^{\bullet}) = X^{\bullet}$ for some index $p_{0}$.
Consider for each $k \in \mathbb{Z}$ the complex $X^{\bullet}_{k} = X^{\bullet}/F^{k+1}(X^{\bullet})$; it is canonically
equipped with the filtration formed by the $F^{p}(X^{\bullet}_{k}) = F^{p}(X^{\bullet})/F^{k+1}(X^{\bullet})$ for $p
\leq k$ and $F^{p}(X^{\bullet}_{k}) = 0$ for $p \geq k+1$. Moreover, one has canonical morphisms $X^{\bullet}_{k+1} \to
X^{\bullet}_{k}$, which make $\mathbf{X}^{\bullet} = (X^{\bullet}_{k})_{k \in \mathbb{Z}}$ a projective system of
filtered complexes of objects of $\mathcal{C}$. Note that this projective system is *strict* and is such that
$X^{\bullet}_{k} = 0$ for $k < p_{0}$.

**13.5.2.**

<!-- label: 0_III.13.5.2 -->

Consider more generally a *strict* projective system $\mathbf{X}^{\bullet} = (X^{\bullet}_{k})_{k \in \mathbb{Z}}$ of
complexes of objects of $\mathcal{C}$, bounded below; consider on each $X^{\bullet}_{k}$ the filtration defined in
`(13.4.1)` (placing oneself in the abelian category of complexes of $\mathcal{C}$ bounded below). The $X^{\bullet}_{k}
\to X^{\bullet}_{p}$ ($p \leq k$) become morphisms of filtered complexes, with finite filtrations. The functorial
character of the spectral sequences of filtered complexes `(11.2.3)` shows that the morphisms defining the projective
system $\mathbf{X}^{\bullet}$ furnish morphisms making $E(\mathbf{X}^{\bullet}) = (E(X^{\bullet}_{k}))$ a projective
system of spectral sequences.

**Lemma (13.5.3).**

<!-- label: 0_III.13.5.3 -->

Suppose that the projective system $\mathbf{X}^{\bullet} = (X^{\bullet}_{k})_{k \in \mathbb{Z}}$ of filtered complexes
is obtained as in `(13.5.2)`. Then:

- _a)_ For $r \geq p - p_{0}$, one has $B^{pq}_{r}(X^{\bullet}_{k}) = B^{pq}_{\infty}(X^{\bullet}_{k})$ for every $k \in
  \mathbb{Z}$.
- _b)_ For $k + 1 \geq p + r$, one has $Z^{pq}_{r}(X^{\bullet}_{k}) = Z^{pq}_{\infty}(X^{\bullet}_{k})$.
- _c)_ For $k + 1 \geq p + r$, the morphisms $Z^{pq}_{r}(X^{\bullet}_{h}) \to Z^{pq}_{r}(X^{\bullet}_{k})$ and
  $B^{pq}_{r}(X^{\bullet}_{h}) \to B^{pq}_{r}(X^{\bullet}_{k})$ are isomorphisms for every $h \geq k$.

<!-- original page 72 -->

These three properties result immediately from the definitions of `(11.2.2)`, taking into account that
$F^{p-r+1}(X^{\bullet}_{k}) = X^{\bullet}_{k}$ for $p - r < p_{0}$.

**13.5.4.**

<!-- label: 0_III.13.5.4 -->

Suppose the hypotheses of `(13.5.3)` are satisfied. Then, for $p$, $q$, $r$ fixed ($r$ finite), the projective systems
$(Z^{pq}_{r}(X^{\bullet}_{k}))_{k \in \mathbb{Z}}$, $(B^{pq}_{r}(X^{\bullet}_{k}))_{k \in \mathbb{Z}}$,
$(E^{pq}_{r}(X^{\bullet}_{k}))_{k \in \mathbb{Z}}$ are *essentially constant*; one will denote by
$Z^{pq}_{r}(\mathbf{X}^{\bullet})$, $B^{pq}_{r}(\mathbf{X}^{\bullet})$ and $E^{pq}_{r}(\mathbf{X}^{\bullet}) =
Z^{pq}_{r}(\mathbf{X}^{\bullet})/B^{pq}_{r}(\mathbf{X}^{\bullet})$ their respective projective limits. The
$Z^{pq}_{r}(\mathbf{X}^{\bullet})$ and $B^{pq}_{r}(\mathbf{X}^{\bullet})$ identify canonically with subobjects of
$E^{pq}_{1}(\mathbf{X}^{\bullet})$. The definition of the $d^{pq}_{r}$ `(M, XV, 1)` shows that these morphisms (relative
to the $X^{\bullet}_{k}$) are also essentially constant, and consequently define morphisms

```text
  d^{pq}_r : E^{pq}_r(𝐗^•) → E^{p+r, q−r+1}_r(𝐗^•)                          (13.5.4.1)
```

such that $d^{p+r, q-r+1}_{r} \circ d^{pq}_{r} = 0$; moreover, one has canonical isomorphisms of $Ker(d^{pq}_{r})$ onto
$Z^{pq}_{r+1}(\mathbf{X}^{\bullet})/B^{pq}_{r}(\mathbf{X}^{\bullet})$ and of $Im(d^{pq}_{r})$ onto $B^{p+r,
q-r+1}_{r+1}(\mathbf{X}^{\bullet})/B^{p+r, q-r+1}_{r}(\mathbf{X}^{\bullet})$.

**Lemma (13.5.5).**

<!-- label: 0_III.13.5.5 -->

Under the hypotheses of `(13.5.3)`, one has, for $s \geq r > p - p_{0}$, a canonical monomorphism

$$ i : E^{pq}_{s}(\mathbf{X}^{\bullet}) \to E^{pq}_{r}(\mathbf{X}^{\bullet}) (13.5.5.1) $$

and a canonical isomorphism

$$ j_{r} : E^{pq}_{r}(\mathbf{X}^{\bullet}) \xrightarrow{\sim} E^{pq}_{\infty}(X^{\bullet}_{p+r-1}) (13.5.5.2) $$

such that the diagram

```text
                       j_s
  E^{pq}_s(𝐗^•) ----------> E^{pq}_∞(X^•_{p+s−1})
       ↓ i                          ↓
  E^{pq}_r(𝐗^•) ----------> E^{pq}_∞(X^•_{p+r−1})                           (13.5.5.3)
                       j_r
```

is commutative (the right-hand vertical arrow coming from the morphism $X^{\bullet}_{p+s-1} \to X^{\bullet}_{p+r-1}$).

The existence of $i$ comes from the fact that $B^{pq}_{r}(X^{\bullet}_{k}) = B^{pq}_{\infty}(X^{\bullet}_{k})$ for $r >
p - p_{0}$ `(13.5.3, a))`; one has $Z^{pq}_{r}(X^{\bullet}_{k}) = Z^{pq}_{\infty}(X^{\bullet}_{k})$ for $k + 1 \geq p +
r$ `(13.5.3, b))`, whence in particular $Z^{pq}_{r}(X^{\bullet}_{p+r-1}) = Z^{pq}_{\infty}(X^{\bullet}_{p+r-1})$, and on
the other hand $Z^{pq}_{r}(X^{\bullet}_{p+r-1})$ and $B^{pq}_{r}(X^{\bullet}_{p+r-1})$ identify canonically with
$Z^{pq}_{r}(\mathbf{X}^{\bullet})$ and $B^{pq}_{r}(\mathbf{X}^{\bullet})$ by virtue of `(13.5.3, c))`, whence the
existence of $j_{r}$ and the commutativity of `(13.5.5.3)`.

**Corollary (13.5.6).**

<!-- label: 0_III.13.5.6 -->

Under the hypotheses of `(13.5.3)`, if one of the projective limits $\varprojlim E^{pq}_{r}(\mathbf{X}^{\bullet})$,
$\varprojlim E^{pq}_{\infty}(X^{\bullet}_{k})$ exists, so does the other, and one has a canonical isomorphism

```text
  j_∞ : lim_r E^{pq}_r(𝐗^•) ⥲ lim_k E^{pq}_∞(X^•_k).                        (13.5.6.1)
```

In addition, for the projective system $(E^{pq}_{r}(\mathbf{X}^{\bullet}))_{r \in \mathbb{Z}}$ to be essentially
constant `(13.4.2)`, it is necessary and sufficient that the projective system $(E^{pq}_{\infty}(X^{\bullet}_{k}))_{k
\in \mathbb{Z}}$ be so.

**13.5.7.**

<!-- label: 0_III.13.5.7 -->

One denotes by $B^{pq}_{\infty}(\mathbf{X}^{\bullet})$ and $Z^{pq}_{\infty}(\mathbf{X}^{\bullet})$ the subobjects of
$E^{pq}_{1}(\mathbf{X}^{\bullet})$ respectively equal to $B^{pq}_{r}(\mathbf{X}^{\bullet})$ for $r > p - p_{0}$ and to
$\inf_{r} Z^{pq}_{r}(\mathbf{X}^{\bullet})$ (when the latter exists), so that $\varprojlim
E^{pq}_{r}(\mathbf{X}^{\bullet})$

<!-- original page 73 -->

identifies canonically with $E^{pq}_{\infty}(\mathbf{X}^{\bullet}) =
Z^{pq}_{\infty}(\mathbf{X}^{\bullet})/B^{pq}_{\infty}(\mathbf{X}^{\bullet})$. One will note that the objects
$Z^{pq}_{\infty}(\mathbf{X}^{\bullet})$, $B^{pq}_{\infty}(\mathbf{X}^{\bullet})$, $E^{pq}_{r}(\mathbf{X}^{\bullet})$ ($1
\leq r \leq +\infty$) and $d^{pq}_{r}$ depend *functorially* on the projective system $\mathbf{X}^{\bullet}$ submitted
to the restrictions of `(13.5.5)`, and that the morphisms defined in `(13.5.5)` and `(13.5.6)` are functorial.

### 13.6. Spectral sequence of a functor relative to an object equipped with a finite filtration

**13.6.1.**

<!-- label: 0_III.13.6.1 -->

Let $\mathcal{C}$, $\mathcal{C}'$ be two abelian categories, $T : \mathcal{C} \to \mathcal{C}'$ a covariant additive
functor. Suppose that every object of $\mathcal{C}$ is isomorphic to a subobject of an injective object, so that the
right-derived functors $R^{p} T$ ($p \geq 0$) exist.

**Lemma (13.6.2).**

<!-- label: 0_III.13.6.2 -->

Let $A$ be an object of $\mathcal{C}$, equipped with a finite filtration $(F^{i}(A))_{i \in \mathbb{Z}}$. There exists
an injective resolution $X^{\bullet} = (X^{i})_{i \geq 0}$ of $A$ equipped with a finite filtration
$(F^{i}(X^{\bullet}))_{i \in \mathbb{Z}}$ such that the relation $F^{i}(A) = A$ (resp. $F^{i}(A) = 0$) entails
$F^{i}(X^{\bullet}) = X^{\bullet}$ (resp. $F^{i}(X^{\bullet}) = 0$) and such that, for every $i \in \mathbb{Z}$,
$F^{i}(X^{\bullet})$ is an injective resolution of $F^{i}(A)$.

Let $p$ (resp. $q > p$) be the largest index such that $F^{p}(A) = A$ (resp. the smallest index for which $F^{q}(A) =
0$). One reasons by induction on $q - p$, the lemma being evident for $q - p = 1$. Having formed an injective resolution
$X'''^{\bullet}$ of $A/F^{q-1}(A)$ having the desired properties, one considers the exact sequence $0 \to F^{q-1}(A) \to
A \to A/F^{q-1}(A) \to 0$, one takes an injective resolution $X''^{\bullet}$ of $F^{q-1}(A)$, then one determines an
injective resolution $X^{\bullet}$ of $A$ so as to have an exact sequence $0 \to X''^{\bullet} \to X^{\bullet} \to
X'''^{\bullet} \to 0$ compatible with the preceding `(M, V, 2.2)`; it is clear that $X^{\bullet}$ answers the question.

**Corollary (13.6.3).**

<!-- label: 0_III.13.6.3 -->

Let $B$ be a second object of $\mathcal{C}$, equipped with a finite filtration $(F^{i}(B))_{i \in \mathbb{Z}}$, $s$ an
integer, and let $u : A \to B$ be a morphism such that $u(F^{i}(A)) \subset F^{i+s}(B)$ for every $i \in \mathbb{Z}$. If
$Y^{\bullet} = (Y^{i})_{i \geq 0}$ is an injective resolution of $B$ equipped with a filtration $(F^{i}(Y^{\bullet}))_{i
\in \mathbb{Z}}$ having the properties stated in `(13.6.2)`, there exists a morphism $v : X^{\bullet} \to Y^{\bullet}$
compatible with $u$ and such that $v(F^{i}(X^{\bullet})) \subset F^{i+s}(Y^{\bullet})$ for every $i \in \mathbb{Z}$. In
addition, two such morphisms $v$, $v'$ are homotopic.

This results immediately by induction on $q - p$ from the preceding construction and from `(M, V, 2.3)`.

**13.6.4.**

<!-- label: 0_III.13.6.4 -->

Under the hypotheses of `(13.6.2)`, consider now the complex $T(X^{\bullet})$ in $\mathcal{C}'$, which is evidently
filtered by the complexes $T(F^{i}(X^{\bullet}))$, since $F^{i}(X^{\bullet})$ is a direct factor of $X^{\bullet}$. It
follows from `(13.6.3)` that the spectral sequence of this filtered complex depends only on the filtered object $A$, up
to isomorphism. Its abutment is the cohomology $R^{\bullet }T(A)$, with the filtration

```text
  F^p(R^n T(A)) = Im(R^n T(F^p(A)) → R^n T(A))
                = Ker(R^n T(A) → R^n T(A/F^p(A)))                           (13.6.4.1)
```

`(11.2.2)`, and its term `E_1` is given by

$$ E^{pq}_{1} = R^{p+q} T(gr^{p}(A)) (13.6.4.2) $$

$gr^{p}(A)$ denoting as usual $F^{p}(A)/F^{p+1}(A)$. It is clear, by `(11.2.2)`, that the filtration of the abutment is
finite, and that for $p$, $q$ given, the sequences of

<!-- original page 74 -->

$B^{pq}_{r}(A) = B^{pq}_{r}(T(X^{\bullet}))$ and $Z^{pq}_{r}(A) = Z^{pq}_{r}(T(X^{\bullet}))$ are stationary, so the
preceding spectral sequence is *biregular* `(11.1.3)`. We shall denote this sequence $E(A) = (E^{pq}_{r}(A))$ and we
shall say that it is the *spectral sequence of the functor* $T$ *relative to the filtered object* $A$.

**13.6.5.**

<!-- label: 0_III.13.6.5 -->

Suppose now the hypotheses of `(13.6.3)` are satisfied, whose notations we keep. Since $F^{i}(X^{\bullet})$ (resp.
$F^{i}(Y^{\bullet})$) is a direct factor of $X^{\bullet}$ (resp. $Y^{\bullet}$), one has $(Tv)(T(F^{i}(X^{\bullet})))
\subset T(F^{i+s}(Y^{\bullet}))$ for every $i \in \mathbb{Z}$; the definitions of `(11.2.2)` show then that for $1 \leq
r \leq +\infty$, `Tv` defines a morphism $B^{pq}_{r}(T(X^{\bullet})) \to B^{p+s, q-s}_{r}(T(Y^{\bullet}))$ and a
morphism $Z^{pq}_{r}(T(X^{\bullet})) \to Z^{p+s, q-s}_{r}(T(Y^{\bullet}))$, whence a morphism

```text
  w_r : E^{pq}_r(A) → E^{p+s, q−s}_r(B);
```

similarly, one has for the abutment morphisms $u_{n} : R^{n} T(A) \to R^{n} T(B)$ such that $u_{n}(F^{p}(R^{n} T(A)))
\subset F^{p+s}(R^{n} T(B))$.

The definition of the $d^{pq}_{r}$ `(M, XV, 1)` shows moreover that the diagrams

```text
                       d^{pq}_r
       E^{pq}_r(A) ----------------> E^{p+r, q−r+1}_r(A)
            ↓ w_r                            ↓ w_r
  E^{p+s, q−s}_r(B) -------------> E^{p+r+s, q−r−s+1}_r(B)
                  d^{p+s, q−s}_r
```

are commutative; one deduces an analogous commutative diagram for the isomorphisms $\alpha^{pq}_{r}$, which we shall
leave to the reader the care of making explicit. Finally `(loc. cit.)`, one also has commutative diagrams for the
abutments

```text
                    β^{pq}
       E^{pq}_∞(A) -------> gr^p(R^{p+q} T(A))
            ↓ w_∞                  ↓ u_{p+q}
  E^{p+s, q−s}_∞(B) ----> gr^{p+s}(R^{p+q} T(B))
                  β^{p+s, q−s}
```

**13.6.6.**

<!-- label: 0_III.13.6.6 -->

Suppose in particular that there exists a ring $\mathcal{S}$, equipped with a filtration $(F^{i}(\mathcal{S}))_{i \in
\mathbb{Z}}$, and a ring homomorphism

```text
  h : 𝒮 → Hom_𝒞(A, A)                                                       (13.6.6.1)
```

<!-- original page 75 -->

such that for every $t \in F^{i}(\mathcal{S})$, one has $h_{t}(F^{j}(A)) \subset F^{i+j}(A)$ for every pair $i$, $j$. We
shall say for brevity that $A$ is then equipped with a structure of $\mathcal{S}$-$\mathcal{C}$-module filtered over the
filtered ring $\mathcal{S}$. By passage to the associated graded objects, every $h_{t}$ for $t \in F^{j}(\mathcal{S})$
defines a graded endomorphism $\bar{h}_{t}$ of $gr^{\bullet}(A)$, homogeneous of degree $j$; moreover, this morphism
depends only on the class of $t$ in $gr^{j}(\mathcal{S})$, and one thus defines a homomorphism of graded rings

```text
  h̄ : gr^•(𝒮) → Hom_𝒞(gr^•(A), gr^•(A))
```

where the right-hand side is the ring of graded endomorphisms of $gr^{\bullet}(A)$. We shall say that $gr^{\bullet}(A)$
is equipped with a structure of $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}$-module graded. It follows then from `(13.6.5)`
that for $1 \leq r \leq +\infty$, every $\bar{t} \in gr^{j}(\mathcal{S})$ canonically defines in the bigraded objects
$(B^{pq}_{r}(A))_{(p,q) \in \mathbb{Z} \times \mathbb{Z}}$, $(Z^{pq}_{r}(A))_{(p,q) \in \mathbb{Z} \times \mathbb{Z}}$
and $E_{r}(A) = (E^{pq}_{r}(A))_{(p,q) \in \mathbb{Z} \times \mathbb{Z}}$ bigraded endomorphisms of degrees $(j, -j)$;
in $E_{r}(A)$ (for $r$ finite), this endomorphism commutes with the bigraded endomorphism defined by the $d^{pq}_{r}$.
Since these endomorphisms satisfy the usual conditions of associativity and distributivity with respect to the addition
in $gr^{\bullet}(\mathcal{S})$ and in the bigraded objects considered, we shall say for brevity that the latter are
$gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-modules *bigraded*; it is immediate that the $\alpha^{pq}_{r}$ define an
isomorphism for this type of structures. For every integer $n$, one will denote by $B^{(n)}_{r}(A)$ (resp.
$Z^{(n)}_{r}(A)$, $E^{(n)}_{r}(A)$) the graded subobject of $B^{\bullet\bullet}_{r}(A)$ (resp.
$Z^{\bullet\bullet}_{r}(A)$, $E^{\bullet\bullet}_{r}(A)$) formed by the $B^{pq}_{r}(A)$ (resp. $Z^{pq}_{r}(A)$,
$E^{pq}_{r}(A)$) such that $p + q = n$ (for $1 \leq r < +\infty$); it is immediate that these are
$gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-modules graded. Finally, every $\bar{t} \in gr^{j}(\mathcal{S})$ defines for
every $n$ a graded endomorphism of degree $j$ in the graded object $gr^{\bullet}(R^{n} T(A))$, which is thus equipped
with a structure of $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module graded, the $\beta^{pq}$ (for $p + q = n$) define
an isomorphism of $E^{(n)}_{\infty}(A)$ onto $gr^{\bullet}(R^{n} T(A))$ for this kind of structure.

Note that when $\mathcal{C}'$ is the category of abelian groups, the structures of $\mathcal{S}$-$\mathcal{C}'$-module
(resp. of $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module graded or bigraded) are none other than the usual structures
of $\mathcal{S}$-module (resp. $gr^{\bullet}(\mathcal{S})$-module graded, bigraded).

### 13.7. Derived functors of a projective limit of arguments

**13.7.1.**

<!-- label: 0_III.13.7.1 -->

Let $\mathcal{C}$, $\mathcal{C}'$ be two abelian categories, $\mathcal{C}$ being supposed such that every object of
$\mathcal{C}$ is a subobject of an injective object; let $T : \mathcal{C} \to \mathcal{C}'$ be a covariant additive
functor. Consider a *strict* projective system $\mathbf{A} = (A_{k})_{k \in \mathbb{Z}}$ in $\mathcal{C}$, *bounded
below*; to be precise, we shall suppose that $A_{k} = 0$ for $k < k_{0}$. We associate canonically to this system a
filtration $(F^{p}(A_{k}))_{p \in \mathbb{Z}}$ on each $A_{k}$ by the formulas `(13.4.1.1)`, and since this is a strict
projective system, the canonical morphisms

```text
  F^i(A_h)/F^j(A_h) → F^i(A_k)/F^j(A_k)    (h ≥ k)                           (13.7.1.1)
```

for $i \leq j \leq k + 1$ are isomorphisms. Recall in addition that one has $F^{k}(A_{k}) = A_{k}$ and $F^{k+1}(A_{k}) =
0$ for every $k$.

**13.7.2.**

<!-- label: 0_III.13.7.2 -->

Let us construct now for each $k$ an injective resolution $X^{\bullet}_{k} = (X^{i}_{k})_{i \geq 0}$ of $A_{k}$ having
the properties of `(13.6.2)`. The canonical morphisms $A_{k+1} \to A_{k}$ allow `(13.6.3)` to define for each $k$ a
morphism of complexes $X^{\bullet}_{k+1} \to X^{\bullet}_{k}$ compatible

<!-- original page 76 -->

with the filtrations, and making $\mathbf{X}^{\bullet} = (X^{\bullet}_{k})_{k \in \mathbb{Z}}$ a projective system of
complexes. One can in addition suppose that this projective system is *strict*. For this, one observes that by virtue of
the isomorphism `(13.7.1.1)`, $A_{k}$ is isomorphic to $A_{k+1}/F^{k+1}(A_{k+1})$; one can therefore take, in the
construction of $X^{\bullet}_{k+1}$, the injective resolution of $A_{k+1}/F^{k+1}(A_{k+1})$ equal to $X^{\bullet}_{k}$,
and it results from `(M, V, 2.3)` that the construction of the morphism of complexes $X^{\bullet}_{k+1} \to
X^{\bullet}_{k}$ can be done so that this morphism furnishes by passage to the quotients an isomorphism
$X^{\bullet}_{k+1}/F^{k+1}(X^{\bullet}_{k+1}) \xrightarrow{\sim} X^{\bullet}_{k}$ respecting the filtrations, which is
the condition of `(13.5.1)`.

**13.7.3.**

<!-- label: 0_III.13.7.3 -->

By construction, the projective system $T(\mathbf{X}^{\bullet})$ of complexes $T(X^{\bullet}_{k})$ satisfies the
hypotheses of `(13.5.3)`. The results of `(13.5.4)`, `(13.5.5)` and `(13.5.6)` are therefore applicable to the spectral
sequences $E(T(X^{\bullet}_{k})) = E(A_{k})$; we shall write $E^{pq}_{r}(\mathbf{A})$ instead of
$E^{pq}_{r}(T(\mathbf{X}^{\bullet}))$ for $1 \leq r \leq +\infty$ (cf. `(13.5.7)` for $r = +\infty$) and similarly for
analogous notations. One will note in particular that one has

$$ E^{pq}_{1}(\mathbf{A}) = R^{p+q} T(gr^{p}(\mathbf{A})) (13.7.3.1) $$

by virtue of `(13.6.4.2)` and of the fact that the system $(gr^{p}(A_{k}))$ is essentially constant.

These results and `(13.4.3)` give the following proposition, first proved by Shih Weishu by a different (unpublished)
method:

**Proposition (13.7.4) (Shih).**

<!-- label: 0_III.13.7.4 -->

Let $n$ be an integer. The following two conditions are equivalent:

- _a)_ For every pair $(p, q)$ such that $p + q = n$, the projective system $(E^{pq}_{r}(\mathbf{A}))_{r \geq 2}$ is
  essentially constant.
- _b)_ The projective system $R^{n} T(\mathbf{A}) = (R^{n} T(A_{k}))_{k \in \mathbb{Z}}$ satisfies `(ML)`.

In addition, when these conditions are satisfied, one has a canonical isomorphism

```text
  gr^p(R^n T(𝐀)) ⥲ E^{p, n−p}_∞(𝐀)    for every p ∈ ℤ.                       (13.7.4.1)
```

Indeed, by virtue of `(13.5.6)`, condition _a)_ is equivalent to saying that the projective system
$(E^{pq}_{\infty}(A_{k}))_{k \in \mathbb{Z}}$ is essentially constant for $p + q = n$, and on the other hand
$gr^{p}(R^{n} T(A_{k}))$ is canonically isomorphic to $E^{p, n-p}_{\infty}(A_{k})$, so it results from `(13.4.3)` that
_a)_ and _b)_ are equivalent; the isomorphism `(13.7.4.1)` is none other than `(13.5.6.1)` applied to the case
considered here.

**Corollary (13.7.5).**

<!-- label: 0_III.13.7.5 -->

Let $\mathcal{F} = (\mathcal{F}_{k})_{k \in \mathbb{N}}$ be a projective system of sheaves of abelian groups satisfying
conditions (i), (ii) and (iii) of `(13.3.1)` and let $\mathcal{F} = \varprojlim \mathcal{F}_{k}$. Suppose that, for the
functor $\mathcal{G} \mapsto \Gamma(X, \mathcal{G})$, the projective system $(E^{pq}_{r}(\mathcal{F}))_{r \in
\mathbb{Z}}$ is essentially constant for every pair $(p, q)$ such that $p + q = n$ or $p + q = n + 1$. Consider on
$H^{n+1}(X, \mathcal{F})$ the filtration defined by $F^{p}(H^{n+1}(X, \mathcal{F})) = Ker(H^{n+1}(X, \mathcal{F}) \to
H^{n+1}(X, \mathcal{F}_{p-1}))$. One has then a canonical isomorphism

```text
  gr^p(H^{n+1}(X, ℱ)) ⥲ E^{p, n−p+1}_∞(ℱ)    for every p ∈ ℤ.                (13.7.5.1)
```

It results from `(13.7.4)` applied to the case where $\mathcal{C}$ is the category of sheaves of abelian groups on $X$,
$\mathcal{C}'$ the category of abelian groups, and $T = \Gamma$, that one has a canonical isomorphism

<!-- original page 77 -->

$gr^{p}(R^{n+1} \Gamma(\mathcal{F})) \xrightarrow{\sim} E^{p, n-p+1}_{\infty}(\mathcal{F})$ for every $p \in
\mathbb{Z}$. On the other hand, since by virtue of `(13.7.4)`, the projective system $(H^{n}(X, \mathcal{F}_{k}))_{k \in
\mathbb{Z}}$ satisfies `(ML)`, one deduces from `(13.3.1)` a canonical isomorphism

```text
  H^{n+1}(X, ℱ) ⥲ lim_← H^{n+1}(X, ℱ_k).                                    (13.7.5.1)
                  k
```

Since the projective system $R^{n+1} \Gamma(\mathcal{F})$ satisfies `(ML)` by virtue of `(13.7.4)`, one has a canonical
isomorphism $gr^{p}(R^{n+1} \Gamma(\mathcal{F})) \xrightarrow{\sim} \varprojlim gr^{p}(H^{n+1}(X, \mathcal{F}_{k}))$
`(13.4.3)`, and a canonical isomorphism $\varprojlim gr^{p}(H^{n+1}(X, \mathcal{F}_{k})) \xrightarrow{\sim}
gr^{p}(\varprojlim H^{n+1}(X, \mathcal{F}_{k}))$ `(13.4.5)`. It therefore all comes down to seeing that the isomorphism
`(13.7.5.1)` is compatible with the filtrations of the two sides; but this results immediately from the definitions and
from the commutativity of the diagram

```text
  H^{n+1}(X, ℱ) ⥲ lim_← H^{n+1}(X, ℱ_k)
              ↘            ↙
              H^{n+1}(X, ℱ_{p−1})
```

for every $p$.

**13.7.6.**

<!-- label: 0_III.13.7.6 -->

Let $\mathcal{S}$ be a ring equipped with a filtration $(F^{i}(\mathcal{S}))_{i \in \mathbb{Z}}$ such that
$F^{0}(\mathcal{S}) = \mathcal{S}$ (so $gr^{i}(\mathcal{S}) = 0$ for $i < 0$). Suppose that each of the $A_{k}$,
equipped with the filtration defined in `(13.7.1)`, is an $\mathcal{S}$-$\mathcal{C}$-module filtered `(13.6.6)`, the
morphisms $A_{h} \to A_{k}$ for $k \leq h$ being morphisms for the structure of $\mathcal{S}$-$\mathcal{C}$-module
filtered; we shall say for brevity that $\mathbf{A}$ is a *projective system of $\mathcal{S}$-$\mathcal{C}$-modules
filtered*. Then it is immediate that the morphisms $B^{pq}_{r}(A_{h}) \to B^{pq}_{r}(A_{k})$ and $Z^{pq}_{r}(A_{h}) \to
Z^{pq}_{r}(A_{k})$ for $k \leq h$, $1 \leq r \leq +\infty$, are morphisms for the structures of
$gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module bigraded `(13.6.5)`, and that the families $(Z^{pq}_{r}(\mathbf{A}))$,
$(B^{pq}_{r}(\mathbf{A}))$ and $(E^{pq}_{r}(\mathbf{A}))$ are $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-modules
bigraded for $r$ finite, the first two being submodules of $(E^{pq}_{r}(\mathbf{A}))$. One will again denote by
$Z^{(n)}_{r}(\mathbf{A})$, $B^{(n)}_{r}(\mathbf{A})$, $E^{(n)}_{r}(\mathbf{A})$ the respective subobjects of the
preceding obtained by taking only the terms such that $p + q = n$; these are
$gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-modules graded.

When the system $(E^{pq}_{r}(\mathbf{A}))_{r \in \mathbb{Z}}$ is essentially constant, $(E^{pq}_{\infty}(\mathbf{A}))$
is therefore also a $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module bigraded, and each $E^{(n)}_{\infty}(\mathbf{A})$
a $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module graded. In addition, the $\beta^{p, n-p} : E^{p,
n-p}_{\infty}(A_{k}) \xrightarrow{\sim} gr^{p}(R^{n} T(A_{k}))$ constitute for each $k$ an isomorphism for the structure
of $gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module graded of $E^{(n)}_{\infty}(A_{k})$ onto $gr^{\bullet}(R^{n}
T(A_{k}))$; if one is in the preceding conditions, $\beta^{p, n-p} : E^{p, n-p}_{\infty}(\mathbf{A}) \xrightarrow{\sim}
\varprojlim gr^{\bullet}(R^{n} T(A_{k}))$ will therefore also be an isomorphism for these structures, and it is
evidently the same for the canonical isomorphism $gr^{\bullet}(R^{n} T(\mathbf{A})) \xrightarrow{\sim} \varprojlim
gr^{\bullet}(R^{n} T(A_{k}))$, so the isomorphisms `(13.7.4.1)` constitute an isomorphism for the structures of
$gr^{\bullet}(\mathcal{S})$-$\mathcal{C}'$-module graded.

**Proposition (13.7.7).**

<!-- label: 0_III.13.7.7 -->

Let $S$ be a noetherian $\mathfrak{J}$-adic ring. Suppose that $\mathcal{C}$ is an abelian category every object of
which is isomorphic to a subobject of an injective object, and let $T$ be a covariant additive functor from
$\mathcal{C}$ to the category of abelian groups. Let $\mathbf{A} = (A_{k})_{k \in \mathbb{Z}}$ be a

<!-- original page 78 -->

strict projective system of $S$-$\mathcal{C}$-modules filtered (for the $\mathfrak{J}$-adic filtration on $S$) bounded
below. One supposes that for some given integer $n$, the following condition is satisfied:

> $(F_{n})$ The $gr^{\bullet}(S)$-module graded $E^{(m)}_{1}(\mathbf{A}) = (R^{m} T(gr^{p}(\mathbf{A})))_{p \in
> \mathbb{Z}}$ `(13.7.3.1)` is of finite type for $m = n$ and $m = n + 1$.

Under these conditions:

- _(i)_ The projective systems $(R^{n} T(A_{k}))_{k \in \mathbb{Z}}$ and $(R^{n+1} T(A_{k}))_{k \in \mathbb{Z}}$ satisfy
  `(ML)`.
- _(ii)_ If one sets $R^{n} T(\mathbf{A}) = \varprojlim R^{n} T(A_{k})$, $R^{n} T(\mathbf{A})$ is an $S$-module of
  finite type.
- _(iii)_ The filtration defined by $F^{p}(R^{n} T(\mathbf{A})) = Ker(R^{n} T(\mathbf{A}) \to R^{n} T(A_{p-1}))$ ($p \in
  \mathbb{Z}$) on $R^{n} T(\mathbf{A})$ is *$\mathfrak{J}$-good* (that is, $\mathfrak{J} F^{p}(R^{n} T(\mathbf{A}))
  \subset F^{p+1}(R^{n} T(\mathbf{A}))$ for every $p$, the equality of the two sides holding whenever $p$ is large
  enough). In particular, the topology on $R^{n} T(\mathbf{A})$ defined by this filtration is identical to the
  $\mathfrak{J}$-adic topology.
- _(iv)_ The projective system $(E^{pq}_{r}(\mathbf{A}))_{r \in \mathbb{Z}}$ is essentially constant for $p + q = n$ and
  $p + q = n + 1$, $E^{pq}_{\infty}(\mathbf{A})$ is therefore defined `(13.5.7)` and one has a canonical isomorphism of
  $gr^{\bullet}(S)$-modules graded

```text
  gr^p(R^n T(𝐀)) ⥲ E^{p, n−p}_∞(𝐀)    (p ∈ ℤ).                              (13.7.7.1)
```

One will note that the isomorphism `(13.7.7.1)` will allow one to denote $R^{n} T(\mathbf{A})$ by abuse of language the
projective limit $R^{n} T(\mathbf{A})$ of the projective system $R^{\bullet} T(\mathbf{A})$, taking into account the
isomorphisms `(13.7.4.1)`.

Since the graded ring $gr^{\bullet}(S)$ is noetherian (Bourbaki, _Alg. comm._, ch. III, §2, n° 9, cor. 5 of th. 2), the
increasing sequence of graded $gr^{\bullet}(S)$-submodules $B^{(m)}_{r}(\mathbf{A})$ of $E^{(m)}_{1}(\mathbf{A})$
`(13.6.6)` is stationary for $m = n$ and $m = n + 1$, and consequently condition _b)_ of `(11.1.10)` is satisfied. It
follows that condition _a)_ of `(13.7.4)` is fulfilled for $n$ and for $n + 1$, and this already proves (i). In
addition, the isomorphisms `(13.7.4.1)` (taking into account the remarks of `(13.7.6)`) show that $gr^{\bullet}(R^{n}
T(\mathbf{A}))$ is a $gr^{\bullet}(S)$-module graded isomorphic to $E^{(n)}_{\infty}(\mathbf{A}) =
Z^{(n)}_{\infty}(\mathbf{A})/B^{(n)}_{\infty}(\mathbf{A})$; since $Z^{(n)}_{\infty}(\mathbf{A})$ is a submodule of
$E^{(n)}_{1}(\mathbf{A})$, it is of finite type, and the same holds for $E^{(n)}_{\infty}(\mathbf{A})$. In addition, for
the filtration $(F^{p}(R^{n} T(\mathbf{A})))$, it follows from `(13.4.5)` that $gr^{\bullet}(R^{n} T(\mathbf{A}))$ and
$gr^{\bullet}(R^{n} T(\mathbf{A}))$ are $gr^{\bullet}(S)$-modules isomorphic, which demonstrates (iv). The assertions
(ii) and (iii) will finally be consequences of the preceding results and of the following lemma:

**Lemma (13.7.7.2).**

<!-- label: 0_III.13.7.7.2 -->

Let $S$ be a noetherian $\mathfrak{J}$-adic ring, $M$ an $S$-module equipped with a co-discrete filtration
$(F^{p}(M))_{p \in \mathbb{Z}}$ such that $\mathfrak{J} F^{p}(M) \subset F^{p+1}(M)$ (which expresses that $M$ is a
module filtered over the ring $S$ filtered by the $\mathfrak{J}$-adic filtration). Suppose in addition $M$ is separated
for the topology defined by the filtration $(F^{p}(M))$. Then the following conditions are equivalent:

- _a)_ $M$ is an $S$-module of finite type and $(F^{p}(M))$ is a $\mathfrak{J}$-good filtration.
- _b)_ $gr^{\bullet}(M)$ is a $gr^{\bullet}(S)$-module of finite type.
- _c)_ The $gr^{p}(M)$ are $S$-modules of finite type and for $p$ large enough the canonical homomorphisms

```text
  𝔍 ⊗_S gr^p(M) → gr^{p+1}(M)                                                (13.7.7.3)
```

<!-- original page 79 -->

(deduced from $\mathfrak{J} \otimes_{S} F^{p}(M) \to F^{p+1}(M)$, taking into account that the image of the composite
homomorphism $\mathfrak{J} \otimes_{S} F^{p+1}(M) \to \mathfrak{J} \otimes_{S} F^{p}(M) \to F^{p+1}(M)$ is $\mathfrak{J}
F^{p+1}(M) \subset F^{p+2}(M)$) are surjective.

For the demonstration, see Bourbaki, _Alg. comm._, ch. III, §3, n° 1, prop. 3.

**13.7.7.4.**

<!-- label: 0_III.13.7.7.4 -->

To apply Lemma `(13.7.7.2)`, it remains to observe that the topology defined on $R^{n} T(\mathbf{A})$ by the filtration
considered makes $R^{n} T(\mathbf{A})$ a separated and complete $S$-module, this topology being that of the projective
limit of the discrete groups $R^{n} T(A_{k})$; on the other hand, if $A_{k} = 0$ for $k < k_{0}$, one also has $R^{n}
T(A_{k}) = 0$ for $k < k_{0}$, so $F^{k_{0}}(R^{n} T(\mathbf{A})) = R^{n} T(\mathbf{A})$, and one is indeed in the
conditions of application of the lemma.

**Corollary (13.7.8).**

<!-- label: 0_III.13.7.8 -->

If hypothesis $(F_{n})$ is satisfied, one has, for every element $f \in S$, a canonical isomorphism

```text
  lim_← ((R^n T(A_k))_f) ⥲ R^n T(𝐀) ⊗_S S_{{f}}.                            (13.7.8.1)
    k
```

Indeed, $R^{n} T(\mathbf{A})$ is an $S$-module of finite type, $S_{{f}}$ a noetherian adic $S$-algebra $(0_{I},
7.6.11)$, separated completion of $S_{f}$ for the $\mathfrak{J}$-preadic topology $(0_{I}, 7.6.2)$. One concludes from
$(0_{I}, 7.7.8)$ and $(0_{I}, 7.7.1)$ that $R^{n} T(\mathbf{A}) \otimes_{S} S_{{f}}$ is isomorphic to the separated
completion of $R^{n} T(\mathbf{A}) \otimes_{S} S_{f}$ for the $\mathfrak{J}$-preadic topology; a fundamental system of
neighborhoods of `0` for this topology is $(\mathfrak{J}^{p} R^{n} T(\mathbf{A})) \otimes_{S} S_{f}$, so $F^{p}(R^{n}
T(\mathbf{A})) \otimes_{S} S_{f}$ is also such a system; the latter is the kernel of the canonical map $(R^{n}
T(\mathbf{A}))_{f} \to (R^{n} T(A_{p-1}))_{f}$, and consequently the separated group associated to $R^{n} T(\mathbf{A})
\otimes_{S} S_{f}$ identifies with a subgroup $G$ of $\varprojlim ((R^{n} T(A_{k}))_{f})$. But the projective system
$((R^{n} T(A_{k}))_{f})$ evidently satisfies condition `(ML)`, and the image of $(R^{n} T(\mathbf{A}))_{f}$ in each of
the $(R^{n} T(A_{k}))_{f}$ equals the common image of the $(R^{n} T(A_{h}))_{f}$ for $h \geq k$ large enough. One
concludes immediately that $G$ is *everywhere dense* in $\varprojlim ((R^{n} T(A_{k}))_{f})$, and since this latter
group is separated and complete, the corollary is demonstrated.

(_To be continued._)
