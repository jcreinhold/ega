<!-- original page 135 -->

## §17. Regular rings

### 17.1. Definition of regular rings

**Proposition (17.1.1).**

<!-- label: 0_IV.17.1.1 -->

*Let $A$ be a Noetherian local ring of dimension $n$, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue
field. The following conditions are equivalent:*

*a) The canonical surjective homomorphism of graded $k$-modules `(15.1.1.1)`*

$$ \phi : S_{\bullet}(\mathfrak{m}/\mathfrak{m}^{2}) \to gr_{\mathfrak{m}}(A) $$

*(where the right-hand side is the graded $k$-module associated with $A$ equipped with the $\mathfrak{m}$-preadic
filtration) is bijective.*

*b) One has $rg_{k}(\mathfrak{m}/\mathfrak{m}^{2}) = n$.*

*c) The ideal $\mathfrak{m}$ admits a system of generators with $n$ elements.*

*d) The ideal $\mathfrak{m}$ admits a system of generators which is an $A$-regular sequence.*

By Nakayama's lemma, $rg_{k}(\mathfrak{m}/\mathfrak{m}^{2})$ is the smallest number of elements in a system of
generators of $\mathfrak{m}$, so b) and c) are equivalent. On the other hand, if $(x_{i})_{1 \leq i \leq n}$ is a system
of generators of $\mathfrak{m}$ whose classes $\bar{x}_{i} mod \mathfrak{m}^{2}$ form a basis of the $k$-vector space
$\mathfrak{m}/\mathfrak{m}^{2}$, then $S_{\bullet}(\mathfrak{m}/\mathfrak{m}^{2})$ is isomorphic to the polynomial ring

<!-- original page 136 -->

$k[T_{1}, \cdots, T_{n}]$; taking into account that every $A$-module of finite type is separated for the
$\mathfrak{m}$-preadic filtration $(0_{I}, 7.3.5)$, it follows from `(15.1.9)` that conditions a) and d) are equivalent;
furthermore, since every $A$-regular sequence of elements of $\mathfrak{m}$ has at most $n$ elements `(16.4.1)`, one
sees that d) implies c). It remains to prove that c) implies a). For brevity put $S =
S_{\bullet}(\mathfrak{m}/\mathfrak{m}^{2}) = k[T_{1}, \cdots, T_{n}]$, $G = gr_{\mathfrak{m}}(A)$, and consider the
exact sequence $0 \to \mathfrak{J} \to S \to^{\phi} G \to 0$, where the kernel $\mathfrak{J}$ of $\phi$ is a graded
ideal of $S$. For every integer $s \geq 0$ one has therefore

```text
(17.1.1.1)               C(s+n-1, n-1) = long(S_s) = long(G_s) + long(𝔍_s).
```

Suppose $\mathfrak{J} \neq 0$, so that there exists a homogeneous element $u \in \mathfrak{J}$ of degree $h \geq 0$;
$\mathfrak{J}_{s}$ contains $u S_{s-h}$ for $s \geq h$, and since $u \neq 0$ and $S$ is an integral domain, $u S_{s-h}$
is isomorphic to $S_{s-h}$ as a $k$-vector space; one would therefore have $long(\mathfrak{J}_{s}) \geq long(S_{s-h}) =
C(s-h+n-1, n-1)$, whence for $s \geq h$,

```text
(17.1.1.2)              long(G_s) ≤ C(s+n-1, n-1) − C(s-h+n-1, n-1).
```

Now, the right-hand side of `(17.1.1.2)` is a polynomial in $s$ of degree $\leq n-2$; but one has $G_{s} =
\mathfrak{m}^{s}/\mathfrak{m}^{s+1}$, and for $s$ large enough, $long(G_{s})$ is a polynomial in $s$ of degree exactly
equal to `n-1` whose leading coefficient is `> 0` `(16.2.1)`, which contradicts the inequality `(17.1.1.2)`. Q.E.D.

**Definition (17.1.2).**

<!-- label: 0_IV.17.1.2 -->

*One says that a Noetherian local ring which satisfies the equivalent conditions of `(17.1.1)` is **regular**.*

**Corollary (17.1.3).**

<!-- label: 0_IV.17.1.3 -->

*A regular local ring is an integral domain, integrally closed, and a Cohen-Macaulay ring.*

The last assertion follows from `(17.1.1, d))`; on the other hand, if $A$ is regular, $gr_{\mathfrak{m}}(A)$ is an
integral domain and completely integrally closed, being isomorphic to $k[T_{1}, \cdots, T_{n}]$; one concludes that $A$
also possesses these two properties
`(Bourbaki, Alg. comm., chap. III, §2, n° 3, cor. of prop. 1 and chap. V, §1, n° 5, prop. 15)`.

**Examples (17.1.4).** — (i) A regular local ring of dimension `0`, being an integral domain by `(17.1.3)`, is
necessarily a field, and conversely.

(ii) For a Noetherian local ring of dimension `1` to be regular, it is necessary and sufficient that it be a *discrete
valuation ring*: indeed, to say that a Noetherian local ring of dimension `1` is regular means that its maximal ideal is
principal, and the conclusion follows from `Bourbaki, Alg. comm., chap. VI, §3, n° 6, prop. 9`.

(iii) Let $k$ be a field; the ring of formal power series $A = k[[T_{1}, \cdots, T_{n}]]$ is a *regular ring of
dimension $n$*; indeed, it is clear that the $T_{i}$ $(1 \leq i \leq n)$ generate the maximal ideal $\mathfrak{m}$ of
$A$ and form an $A$-regular sequence, since $A/(T_{1} A + \cdots + T_{i} A)$ is isomorphic to $k[[T_{i+1}, \cdots,
T_{n}]]$.

**Proposition (17.1.5).**

<!-- label: 0_IV.17.1.5 -->

*For a Noetherian local ring $A$ to be regular, it is necessary and sufficient that its completion `Â` be so.*

<!-- original page 137 -->

Indeed, the maximal ideal of `Â` is $\mathfrak{m}\hat{A}$, and one knows that $\mathfrak{m}^{h}/\mathfrak{m}^{h+1}$ and
$(\mathfrak{m}\hat{A})^{h}/(\mathfrak{m}\hat{A})^{h+1}$ are isomorphic $k$-vector spaces; condition a) of `(17.1.1)` is
therefore the same for $A$ and `Â`.

**Definition (17.1.6).**

<!-- label: 0_IV.17.1.6 -->

*Given a Noetherian local ring $A$ with maximal ideal $\mathfrak{m}$, one calls a **regular system of parameters** of
$A$ a system of parameters for $A$ `(16.3.5)` that generates $\mathfrak{m}$.*

The existence of such a system is equivalent to the fact that $A$ is regular `(17.1.1)`; if $(x_{i})_{1 \leq i \leq n}$
is a regular system of parameters, it is a minimal system of generators of $\mathfrak{m}$, whose classes mod
$\mathfrak{m}^{2}$ form a basis of $\mathfrak{m}/\mathfrak{m}^{2}$ over $k$; by virtue of `(17.1.1, a))` and `(15.1.9)`,
$(x_{i})$ is a maximal $A$-regular sequence (whence the terminology).

One should beware, however, that in a regular ring, a system of parameters for $A$ which is also an $A$-regular sequence
is not necessarily a regular system of parameters, as the example of the $k$-th powers of a regular system of parameters
shows `(15.1.20)`.

**Proposition (17.1.7).**

<!-- label: 0_IV.17.1.7 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue field,
$(x_{i})_{1 \leq i \leq r}$ a sequence of elements of $\mathfrak{m}$, $\mathfrak{J} = x_{1} A + \cdots + x_{r} A$. The
following conditions are equivalent:*

*a) $A$ is regular and the $x_{i}$ are part of a regular system of parameters of $A$.*

*a′) $A$ is regular and the classes $\bar{x}_{i}$ of the $x_{i}$ mod $\mathfrak{m}^{2}$ are linearly independent over
$k$.*

*b) The $x_{i}$ are part of a system of parameters for $A$ and $A/\mathfrak{J}$ is a regular ring.*

*Moreover, when these conditions are satisfied, $\mathfrak{J}$ is a prime ideal.*

The last assertion follows trivially from the fact that $A/\mathfrak{J}$, being regular, is an integral domain
`(17.1.3)`. Put $n = \dim(A)$. The equivalence of a) and a′) is immediate; indeed, the classes mod $\mathfrak{m}^{2}$ of
the elements of a regular system of parameters form a basis of $\mathfrak{m}/\mathfrak{m}^{2}$ over $k$, and conversely,
if the $\bar{x}_{i}$ $(1 \leq i \leq r)$ are linearly independent over $k$, one can find $n - r$ elements $x_{i} \in
\mathfrak{m}$ $(r + 1 \leq i \leq n)$ such that the $\bar{x}_{i}$ $(1 \leq i \leq n)$ form a basis of
$\mathfrak{m}/\mathfrak{m}^{2}$, hence $(x_{i})_{1 \leq i \leq n}$ is a regular system of parameters. To see that a)
implies b), let us remark that since the $x_{i}$ are part of a system of parameters of $A$, one has
$\dim(A/\mathfrak{J}) = n - r$ `(16.3.6)`; let $\mathfrak{n} = \mathfrak{m}/\mathfrak{J}$ be the maximal ideal of
$A/\mathfrak{J}$. One has an exact sequence

```text
(17.1.7.1)              0 → (𝔪² + 𝔍)/𝔪² → 𝔪/𝔪² → 𝔫/𝔫² → 0
```

since $\mathfrak{n}^{2} = (\mathfrak{m}^{2} + \mathfrak{J})/\mathfrak{J}$; hypothesis a) implies that
$rg_{k}((\mathfrak{m}^{2} + \mathfrak{J})/\mathfrak{m}^{2}) = r$, hence $rg_{k}(\mathfrak{n}/\mathfrak{n}^{2}) = n - r =
\dim(A/\mathfrak{J})$, which proves b) by virtue of `(17.1.1, b))`.

Conversely, to prove that b) implies a), note that the fact that the $x_{i}$ are part of a system of parameters implies
that $\dim(A/\mathfrak{J}) = n - r$ `(16.3.6)`; on the other hand, the hypothesis that $A/\mathfrak{J}$ is regular
implies $rg_{k}(\mathfrak{n}/\mathfrak{n}^{2}) = n - r$ `(17.1.1)`; moreover one obviously has
$rg_{k}((\mathfrak{m}^{2} + \mathfrak{J})/\mathfrak{m}^{2}) \leq r$, so one deduces from `(17.1.7.1)` that
$rg_{k}(\mathfrak{m}/\mathfrak{m}^{2}) \leq r + (n - r) = n$; hence $A$ is regular by virtue of `(16.2.6)` and
`(17.1.1)`. Furthermore, the relation $rg_{k}(\mathfrak{m}/\mathfrak{m}^{2}) = n$ then implies
$rg_{k}((\mathfrak{m}^{2} + \mathfrak{J})/\mathfrak{m}^{2}) = r$, and consequently the $\bar{x}_{i}$ are linearly
independent over $k$. Q.E.D.

<!-- original page 138 -->

**Corollary (17.1.8).**

<!-- label: 0_IV.17.1.8 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $t$ an element of $\mathfrak{m}$. The following
conditions are equivalent:*

*a) $A/tA$ is regular and $t$ is not a zero-divisor in $A$.*

*b) $A$ is regular and $t \notin \mathfrak{m}^{2}$.*

This is the special case $r = 1$ of `(17.1.7)` (taking into account that an element of $\mathfrak{m}$ which is not a
zero-divisor is part of a system of parameters `(16.4.1)`).

**Corollary (17.1.9).**

<!-- label: 0_IV.17.1.9 -->

*Let $A$ be a regular local ring, $\mathfrak{m}$ its maximal ideal, $\mathfrak{J}$ an ideal of $A$ contained in
$\mathfrak{m}$. The following conditions are equivalent:*

*a) The ring $A/\mathfrak{J}$ is regular.*

*b) $\mathfrak{J}$ is generated by a sequence $(x_{i})_{1 \leq i \leq r}$ which is part of a regular system of
parameters of $A$.*

We have already seen `(17.1.7)` that b) implies a). Conversely, suppose $A/\mathfrak{J}$ is regular (which implies that
$\mathfrak{J}$ is prime) and let $n = \dim(A)$, $n - r = \dim(A/\mathfrak{J})$; with the notations of `(17.1.7)`, the
exact sequence `(17.1.7.1)` gives $rg_{k}((\mathfrak{m}^{2} + \mathfrak{J})/\mathfrak{m}^{2}) = r$, hence there exists a
sequence $(x_{i})_{1 \leq i \leq r}$ of elements of $\mathfrak{J}$ that is part of a regular system of parameters of
$A$. Put $\mathfrak{J}' = x_{1} A + \cdots + x_{r} A$; it follows from `(17.1.7)` that $\mathfrak{J}'$ is a prime ideal
of $A$ and that $A/\mathfrak{J}'$ is regular and of dimension $n - r$; but since $A/\mathfrak{J} =
(A/\mathfrak{J}')/(\mathfrak{J}/\mathfrak{J}')$ and $\mathfrak{J}/\mathfrak{J}'$ is prime in the integral domain
$A/\mathfrak{J}'$, the dimensions of $A/\mathfrak{J}$ and $A/\mathfrak{J}'$ can be equal only if $\mathfrak{J} =
\mathfrak{J}'$ `(16.1.2.2)`.

### 17.2. Recollections on the projective dimension and the injective dimension of modules

**(17.2.1)** Let $A$ be a ring, $M$ an $A$-module. Recall `(M, VI, 2)` that one calls the *projective dimension* (resp.
*injective dimension*) of $M$, and denotes by $\dim. proj(M)$ or $\dim. proj_{A}(M)$ (resp. $\dim. inj(M)$ or $\dim.
inj_{A}(M)$), the smallest $n$ (an integer or equal to $+\infty$) such that there exists a left projective resolution
(resp. a right injective resolution) of $M$ of length $n$. It comes to the same thing *(loc. cit.)* to say that $n$ is
the smallest number such that for every $A$-module $N$, one has $Ext^{i}_{A}(M, N) = 0$ (resp. $Ext^{i}_{A}(N, M) = 0$)
for every $i > n$, or only for $i = n + 1$. For every direct factor $M'$ of $M$, one therefore has
`dim. proj(M') ≤ dim. proj(M)` since $Ext^{i}_{A}(M', N)$ is a direct factor of $Ext^{i}_{A}(M, N)$; similarly
`dim. inj(M') ≤ dim. inj(M)`. An equivalent condition to $\dim. proj(M) = n$ (resp. $\dim. inj(M) = n$) is that $n$ is
the smallest number such that, for every exact sequence

```text
                        0 → R → P_{n-1} → ⋯ → P_0 → M → 0
```

(resp. $0 \to M \to Q_{0} \to \cdots \to Q_{n-1} \to C \to 0$), where all the $P_{i}$ for $0 \leq i < n$ are projective
(resp. all the $Q_{i}$ for $0 \leq i < n$ are injective), $R$ is projective (resp. $C$ is injective).

**Remarks (17.2.2).** — (i) To say that $M$ is a projective (resp. injective) $A$-module is therefore equivalent to
saying that $\dim. proj(M) = 0$ (resp. $\dim. inj(M) = 0$).

(ii) Let $T$ be an additive covariant functor from the category of $A$-modules to an abelian category. It follows at
once from the definitions of `(17.2.1)` and from that of

<!-- original page 139 -->

derived functors that if $\dim. proj(M) \leq n$ (resp. $\dim. inj(M) \leq n$), one has $L_{i} T(M) = 0$ (resp. $R^{i}
T(M) = 0$) for every $i > n$.

(iii) If one assumes $A$ Noetherian and $M$ of finite type, the last interpretation of the projective dimension given in
`(17.2.1)` shows that if $\dim. proj(M) = n$, then $M$ admits a left resolution of length $n$ formed of projective
modules *of finite type*. If moreover $A$ is a Noetherian local ring, $M$ admits a resolution of length $n$ by *free
modules of finite type*, a projective $A$-module of finite type being then free
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`.

**Lemma (17.2.3).**

<!-- label: 0_IV.17.2.3 -->

*Let $A$ be a ring, $M$ an $A$-module. For $\dim. inj(M) \leq n$, it is necessary and sufficient that for every
monogenic $A$-module $N$, one have $Ext^{n+1}_{A}(N, M) = 0$.*

With the notations of `(17.2.1)`, it suffices to prove that $C$ is injective; for every $A$-module $N$,
$Ext^{n+1}_{A}(N, M)$ is isomorphic to $Ext^{1}_{A}(N, C)$ `(M, V, 7)`, so one has $Ext^{1}_{A}(N, C) = 0$ for every
$A$-module $N$ of the form $A/\mathfrak{J}$, where $\mathfrak{J}$ is an arbitrary ideal of $A$. The exact sequence of
Ext then shows that the canonical homomorphism $\operatorname{Hom}(A, C) \to \operatorname{Hom}(\mathfrak{J}, C)$ is
surjective for every ideal $\mathfrak{J}$ of $A$, which implies that $C$ is an injective $A$-module `(M, I, 3.2)`.

**Lemma (17.2.4).**

<!-- label: 0_IV.17.2.4 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type. For $\dim. proj(M) \leq n$, it is necessary and
sufficient that for every monogenic $A$-module $N$, one have $Ext^{n+1}_{A}(M, N) = 0$.*

One knows indeed `(M, VI, 2.5)` that the condition $\dim. proj(M) \leq n$ is equivalent to $Ext^{n+1}_{A}(M, N) = 0$ for
every $A$-module $N$ of finite type. To see that the condition of the statement is also sufficient, one argues by
induction on the number of generators $m$ of $N$: there is a submodule `N_1` of $N$ generated by $m - 1$ elements and
such that $N_{2} = N/N_{1}$ is monogenic; from the exact sequence $0 \to N_{1} \to N \to N_{2} \to 0$, one then deduces
the exact sequence `Ext^{n+1}_A(M, N_1) → Ext^{n+1}_A(M, N) → Ext^{n+1}_A(M, N_2)`, and the induction hypothesis shows
that the condition of the statement does indeed imply $Ext^{n+1}_{A}(M, N) = 0$.

**Corollary (17.2.5).**

<!-- label: 0_IV.17.2.5 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module. One has*

```text
(17.2.5.1)              dim. inj_A(M) = sup_𝔪(dim. inj_{A_𝔪}(M_𝔪))
```

*and if $M$ is of finite type*

```text
(17.2.5.2)              dim. proj_A(M) = sup_𝔪(dim. proj_{A_𝔪}(M_𝔪))
```

*where $\mathfrak{m}$ runs through the set of prime ideals (or the set of maximal ideals) of $A$.*

Indeed, if $N$ is an $A$-module of finite type (hence of finite presentation), one has, for every multiplicative subset
$S$ of $A$ and every $i \geq 0$,

```text
                        S^{-1} Ext^i_A(N, M) ≅ Ext^i_{S^{-1} A}(S^{-1} N, S^{-1} M)
```

by flatness, considering a free resolution of $M$ and using the fact that the preceding relation is true for $i = 0$
`(Bourbaki, Alg. comm., chap. II, §2, n° 7, prop. 19)`. In particular
$Ext^{i}_{A_{\mathfrak{m}}}(A_{\mathfrak{m}}/\mathfrak{J} A_{\mathfrak{m}}, M_{\mathfrak{m}}) =
(Ext^{i}_{A}(A/\mathfrak{J}, M))_{\mathfrak{m}}$ for every prime ideal $\mathfrak{m}$ and every ideal $\mathfrak{J}$ of
$A$; taking `(17.2.3)` into account, and the fact that every

<!-- original page 140 -->

ideal of $A_{\mathfrak{m}}$ is of the form $\mathfrak{J} A_{\mathfrak{m}}$ for a suitable ideal $\mathfrak{J}$ of $A$,
one deduces formula `(17.2.5.1)` from what precedes and from `Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1`. One
proceeds similarly for `(17.2.5.2)`, this time using `(17.2.4)` and exchanging the roles of $M$ and $N$.

For Noetherian rings and modules of finite type, the study of projective dimension or injective dimension is therefore
reduced by `(17.2.5)` to the case of *local* rings. One then has the following:

**Lemma (17.2.6).**

<!-- label: 0_IV.17.2.6 -->

*Let $A$ be a Noetherian local ring, $k$ its residue field, $M$ an $A$-module of finite type. For $\dim. proj(M) \leq
n$, it is necessary that $Tor^{A}_{i}(M, k) = 0$ for $i > n$, and sufficient that $Tor^{A}_{n+1}(M, k) = 0$.*

Necessity is a special case of remark `(17.2.2, (ii))`, applied to the covariant functor $M \mapsto k \otimes_{A} M$. To
prove that the condition is sufficient, one must, with the notations of `(17.2.1)`, establish that $R$ is projective
when the $P_{i}$ are assumed of finite type; now $Tor^{A}_{n+1}(M, k)$ is isomorphic to $Tor^{A}_{1}(R, k)$ `(M, V, 7)`;
and one knows that, since $R$ is of finite type, the condition $Tor^{A}_{1}(R, k) = 0$ implies that $R$ is free
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`.

**Corollary (17.2.7).**

<!-- label: 0_IV.17.2.7 -->

*Under the hypotheses of `(17.2.6)`, let $x$ be an $M$-regular element of $A$ belonging to the maximal ideal of $A$;
then one has*

```text
(17.2.7.1)              dim. proj(M/xM) = dim. proj(M) + 1.
```

Indeed, from the exact sequence $0 \to M \to^{x} M \to M/xM \to 0$ defined by multiplication by $x$ in $M$, one deduces
the exact sequence of Tor:

```text
        Tor^A_i(M, k) →^x Tor^A_i(M, k) → Tor^A_i(M/xM, k) → Tor^A_{i-1}(M, k) →^x Tor^A_{i-1}(M, k)
```

for every $i \geq 1$. Now, for every $A$-module $N$, the homothety of ratio $x$ in $M \otimes_{A} N$ comes both from the
homothety of ratio $x$ in $M$ and from the homothety of ratio $x$ in $N$; one concludes at once, since the homothety of
ratio $x$ in $k$ is zero by definition, that for every $i$, the homomorphism $Tor^{A}_{i}(M, k) \to^{x} Tor^{A}_{i}(M,
k)$ is zero; in other words, one has the exact sequence

```text
                        0 → Tor^A_i(M, k) → Tor^A_i(M/xM, k) → Tor^A_{i-1}(M, k) → 0.
```

If $\dim. proj(M) = n$, then $Tor^{A}_{n}(M, k) \neq 0$ and $Tor^{A}_{n+1}(M, k) = Tor^{A}_{n+2}(M, k) = 0$ by virtue of
`(17.2.6)`. It follows from what precedes that one has $Tor^{A}_{n+1}(M/xM, k) \neq 0$ and $Tor^{A}_{n+2}(M/xM, k) = 0$,
hence $\dim. proj(M/xM) = n + 1$ by `(17.2.6)`.

**Proposition (17.2.8) (M. Auslander).**

<!-- label: 0_IV.17.2.8 -->

*Let $A$ be a ring. The following conditions are equivalent:*

*a) Every $A$-module is of projective dimension $\leq n$.*

*a′) Every $A$-module of finite type is of projective dimension $\leq n$.*

*b) Every $A$-module is of injective dimension $\leq n$.*

*c) For every pair of $A$-modules `M, N` one has $Ext^{n+1}_{A}(M, N) = 0$.*

*c′) For every pair of $A$-modules `M, N` such that $M$ is of finite type (or only monogenic), one has $Ext^{n+1}_{A}(M,
N) = 0$.*

<!-- original page 141 -->

This follows at once from `(17.2.1)` and `(17.2.3)`.

The smallest number $n$ (an integer or $+\infty$) for which the equivalent conditions of `(17.2.8)` are satisfied is
called the *global cohomological dimension* (or simply *cohomological dimension*) of $A$ and denoted $\dim. coh(A)$.

**Proposition (17.2.9).**

<!-- label: 0_IV.17.2.9 -->

*Let $A$ be a Noetherian ring. The following conditions are equivalent:*

*a) $\dim. coh(A) \leq n$.*

*b) Every $A$-module of finite type is of injective dimension $\leq n$.*

*c) For every pair of $A$-modules of finite type `M, N`, one has $Ext^{n+1}_{A}(M, N) = 0$.*

This follows at once from the definition and from `(17.2.4)`.

**Corollary (17.2.10).**

<!-- label: 0_IV.17.2.10 -->

*If $A$ is a Noetherian ring, one has*

```text
(17.2.10.1)             dim. coh(A) = sup_𝔪(dim. coh(A_𝔪))
```

*where $\mathfrak{m}$ runs through the spectrum of $A$ (or the set of maximal ideals of $A$).*

This follows from `(17.2.9)` and `(17.2.5)`.

**Proposition (17.2.11).**

<!-- label: 0_IV.17.2.11 -->

*Let $A$ be a Noetherian local ring, $k$ its residue field. For $\dim. coh(A) \leq n$, it is necessary that
$Tor^{A}_{i}(k, k) = 0$ for $i > n$, and sufficient that $Tor^{A}_{n+1}(k, k) = 0$.*

Taking `(17.2.6)` into account, it suffices to prove that the relations $\dim. coh(A) \leq n$ and $\dim. proj_{A}(k)
\leq n$ are equivalent. It is clear that the first implies the second by definition. Conversely, if $\dim. proj_{A}(k)
\leq n$, one has $Tor^{A}_{i}(M, k) = 0$ for $i > n$ and every $A$-module $M$ by virtue of `(17.2.2, (ii))`; hence
$\dim. proj(M) \leq n$, which proves the proposition by virtue of `(17.2.8)`.

**Corollary (17.2.12).**

<!-- label: 0_IV.17.2.12 -->

*Let $A$ be a Noetherian ring. For $\dim. coh(A) \leq n$, it is necessary that, for every maximal ideal $\mathfrak{m}$
of $A$, one have $Tor^{A_{\mathfrak{m}}}_{i}(A/\mathfrak{m}, A/\mathfrak{m}) = 0$ for $i > n$, and sufficient that these
relations be satisfied for $i = n + 1$.*

This follows at once from `(17.2.11)` and `(17.2.10)`.

**Proposition (17.2.13).**

<!-- label: 0_IV.17.2.13 -->

*Let $A$, $B$ be two Noetherian local rings, $\phi : A \to B$ a local homomorphism making $B$ a flat $A$-module. Then
one has*

```text
(17.2.13.1)             dim. coh(A) ≤ dim. coh(B).
```

Suppose that $\dim. coh(B) = n$ is finite; it suffices to prove that for every pair $(M, N)$ of $A$-modules of finite
type, one has $Tor^{A}_{i}(M, N) = 0$ for $i > n$ `(17.2.11)`. Since $B$ is a faithfully flat $A$-module $(0_{I},
6.6.2)$, it comes to the same thing $(0_{I}, 6.4.1)$ to show that one has

```text
(17.2.13.2)             Tor^A_i(M, N) ⊗_A B = 0.
```

Now, if $L_{\bullet} = (L_{j})$ is a right resolution of $M$ by free $A$-modules, it follows from the fact that $B$ is a
flat $A$-module that $L_{\bullet} \otimes_{A} B = (L_{j} \otimes_{A} B)$ is a right resolution of the $B$-module $M
\otimes_{A} B$ by free $B$-modules; moreover, one has $(L_{j} \otimes_{A} B) \otimes_{B} (N \otimes_{A} B) = (L_{j}
\otimes_{A} N) \otimes_{A} B$, whence one concludes at once that the left-hand side

<!-- original page 142 -->

of `(17.2.13.2)` equals $Tor^{B}_{i}(M \otimes_{A} B, N \otimes_{A} B)$; the hypothesis on $B$ implies that this
$B$-module is zero for $i > n$ `(17.2.2, (ii))`, whence the conclusion.

**(17.2.14)** Let $(X, \mathcal{O}_{X})$ be a ringed space, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module; one calls the
*pointwise projective* (resp. *injective*) *dimension* of $\mathcal{F}$ and denotes by $\dim. proj(\mathcal{F})$ (resp.
$\dim. inj(\mathcal{F})$) the number `sup_{x ∈ X}(dim. proj(ℱ_x))` (resp. `sup_{x ∈ X}(dim. inj(ℱ_x))`). One calls the
*pointwise cohomological dimension* of $X$ and denotes by $\dim. coh(X)$ the number `sup_{x ∈ X}(dim. coh(𝒪_x))`. It
follows from `(17.2.5)` and `(17.2.10)` that when $A$ is a Noetherian ring, $M$ an $A$-module of finite type and $X =
\operatorname{Spec}(A)$, one has `dim. proj(M̃) = dim. proj(M)`, `dim. inj(M̃) = dim. inj(M)` and
`dim. coh(X) = dim. coh(A)`. One calls the *projective* (resp. *injective*) *dimension* of $\mathcal{F}$ *at a point* $x
\in X$ the projective (resp. injective) dimension of $\mathcal{F}_{x}$, the *cohomological dimension* of $X$ *at a
point* $x$ the cohomological dimension of $\mathcal{O}_{x}$.

**Proposition (17.2.15).**

<!-- label: 0_IV.17.2.15 -->

*Let $X$, $Y$ be two ringed spaces with Noetherian local rings, $f : X \to Y$ a flat morphism. If $\dim. coh(X) \leq n$,
then $Y$ is of cohomological dimension $\leq n$ at every point of $f(X)$.*

This follows at once from `(17.2.13)`.

### 17.3. Cohomological theory of regular rings

**Theorem (17.3.1) (Hilbert-Serre).**

<!-- label: 0_IV.17.3.1 -->

*Let $A$ be a Noetherian local ring. For $A$ to be of finite cohomological dimension, it is necessary and sufficient
that $A$ be regular; one has then*

```text
(17.3.1.1)              dim. coh(A) = dim(A).
```

Suppose $A$ regular; let $\mathfrak{m}$ be its maximal ideal, $\mathbf{x} = (x_{i})_{1 \leq i \leq n}$ a regular system
of parameters of $A$ `(17.1.6)`; consider the complex of the exterior algebra $K_{\bullet}(\mathbf{x})$ `(III, 1.1.1)`,
which is formed of free $A$-modules, with $K_{i}(\mathbf{x}) = 0$ for $i > n$; since $(x_{i})$ is a regular sequence,
one has $H_{i}(K_{\bullet}(\mathbf{x})) = 0$ for $i > 0$ `(III, 1.1.4 and 1.1.3.3)` and $H_{0}(K_{\bullet}(\mathbf{x}))
= A/(x_{1} A + \cdots + x_{n} A) = A/\mathfrak{m} = k$; the $K_{i}(\mathbf{x})$ therefore form a *free resolution* of
$k$ of length $n$. Now, the fact that the $x_{i}$ belong to $\mathfrak{m}$ implies at once that in the complex
$K_{\bullet}(\mathbf{x}, k) = K_{\bullet}(\mathbf{x}) \otimes_{A} k$, the boundary operator is zero in all dimensions,
so that one has, by definition, $Tor^{A}_{i}(k, k) = \Lambda^{i}(k^{n})$; equality `(17.3.1.1)` therefore follows at
once from `(17.2.11)` (this result is essentially Hilbert's "syzygy theorem").

Let us now show that if $A$ is a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, and if $\dim.
proj_{A}(\mathfrak{m})$ is finite, then $A$ is regular, which will complete the proof of `(17.3.1)`. We proceed by
induction on $n = rg_{k}(\mathfrak{m}/\mathfrak{m}^{2})$. For $n = 0$, one has $\mathfrak{m} = 0$ and the assertion is
trivial.

**Lemma (17.3.1.2) (Nagata).**

<!-- label: 0_IV.17.3.1.2 -->

*If every element of $\mathfrak{m} - \mathfrak{m}^{2}$ is a zero-divisor in $A$, there exists $c \neq 0$ in $A$ such
that $c\mathfrak{m} = 0$ (in other words, one has $\mathfrak{m} \in Ass(A)$).*

One can restrict to the case where $\mathfrak{m} \neq 0$, hence $\mathfrak{m} \neq \mathfrak{m}^{2}$. The hypothesis
implies that $\mathfrak{m} - \mathfrak{m}^{2}$ is contained in the union of the ideals $\mathfrak{p}_{i}$ of $Ass(A)$
`(Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 3 of prop. 2)`; hence $\mathfrak{m}$ is contained in the union of
$\mathfrak{m}^{2}$

<!-- original page 143 -->

and the $\mathfrak{p}_{i}$, hence in one of the $\mathfrak{p}_{i}$ since $\mathfrak{m} \neq \mathfrak{m}^{2}$
`(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`; $\mathfrak{m}$ being maximal, this proves the lemma.

**Lemma (17.3.1.3).**

<!-- label: 0_IV.17.3.1.3 -->

*If $a \in \mathfrak{m} - \mathfrak{m}^{2}$, $\mathfrak{m}/Aa$ is isomorphic to a direct factor of
$\mathfrak{m}/a\mathfrak{m}$.*

There exists a minimal system of generators of $\mathfrak{m}$ containing $a$ (whose images in
$\mathfrak{m}/\mathfrak{m}^{2}$ form a basis of this $k$-vector space); let $\mathfrak{b}$ be the ideal generated by the
elements of this system other than $a$. Since the relation $xa \in \mathfrak{b}$ implies $x \in \mathfrak{m}$ (by
considering the image of `xa` in $\mathfrak{m}/\mathfrak{m}^{2}$), one has $\mathfrak{b} \cap Aa \subset a\mathfrak{m}$,
whence a homomorphism $\mathfrak{b}/(\mathfrak{b} \cap Aa) \to \mathfrak{m}/a\mathfrak{m}$ deduced from the injection
$\mathfrak{b} \to \mathfrak{m}$ by passage to the quotients, and which is *injective*. Furthermore, $\mathfrak{b} + Aa =
\mathfrak{m}$, and the composite homomorphism

```text
                𝔪/Aa = (𝔟 + Aa)/Aa ≅ 𝔟/(𝔟 ∩ Aa) → 𝔪/a𝔪 → 𝔪/Aa
```

is the identity; whence the lemma.

**Lemma (17.3.1.4).**

<!-- label: 0_IV.17.3.1.4 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $E$ an $A$-module of finite type and of finite
projective dimension. If $a \in \mathfrak{m}$ is $A$-regular and $E$-regular, then $E/aE$ is an $(A/aA)$-module of
finite projective dimension, at most equal to $\dim. proj_{A}(E)$.*

We argue by induction on $h = \dim. proj_{A}(E)$, the case $h = 0$ being trivial since $E$ is then a projective
$A$-module, hence $E/aE$ is a projective $(A/aA)$-module. There exists an exact sequence

$$ 0 \to N \to L \to E \to 0 $$

where $L$ is free and $\dim. proj_{A}(N) = h - 1$ `(17.2.2, (iii))`, with $N$ of finite type. Moreover, the sequence

$$ 0 \to N/aN \to L/aL \to E/aE \to 0 $$

is exact `(15.1.18)`. Since $a$ is $A$-regular, it is also $N$-regular since $L$ is free; the induction hypothesis
implies that $N/aN$ is an $(A/aA)$-module of projective dimension $\leq h - 1$, and since $L/aL$ is a free
$(A/aA)$-module, $E/aE$ is an $(A/aA)$-module of projective dimension $\leq h$.

Let us now examine two cases:

I. — Suppose first that every element of $\mathfrak{m} - \mathfrak{m}^{2}$ is a zero-divisor in $A$, in which case
`(17.3.1.2)` there exists $c \neq 0$ in $A$ such that $c\mathfrak{m} = 0$. Let us show that then $\mathfrak{m} = 0$.
Were this not so, let us first note that $\mathfrak{m}$ could not be a projective $A$-module, for it would be free
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, which contradicts the relation $c\mathfrak{m} = 0$. One
would therefore have $n = \dim. coh(A) \geq 1$. Since $\mathfrak{m} \in Ass(A)$, there would exist an exact sequence of
$A$-homomorphisms

$$ 0 \to k \to A \to E \to 0. $$

But this is absurd, for by virtue of the relation $n \geq 1$, the exact sequence of Tor would give the exact sequence $0
\to Tor^{A}_{n+1}(E, k) \to Tor^{A}_{n}(k, k) \to 0$; now one has $Tor^{A}_{n+1}(E, k) = 0$ `(17.2.2, (ii))` and
$Tor^{A}_{n}(k, k) \neq 0$ `(17.2.11)`, and we have reached a contradiction.

II. — One can therefore restrict to the case where there exists $a \in \mathfrak{m} - \mathfrak{m}^{2}$ which is an
$A$-regular element, and consequently also $\mathfrak{m}$-regular. Consider the ring $A' = A/aA$ and its

<!-- original page 144 -->

maximal ideal $\mathfrak{m}' = \mathfrak{m}/aA$; it is clear that $rg_{k}(\mathfrak{m}'/\mathfrak{m}'^{2}) = n - 1$. By
virtue of `(17.3.1.4)`, $\mathfrak{m}/a\mathfrak{m}$ is an $A'$-module of finite projective dimension, hence so is
$\mathfrak{m}' = \mathfrak{m}/aA$, which is a direct factor of it `(17.3.1.3 and 17.2.1)`. The induction hypothesis
therefore implies that $A' = A/aA$ is regular, which proves by `(17.1.8)` that $A$ is regular.

**Corollary (17.3.2).**

<!-- label: 0_IV.17.3.2 -->

*If $A$ is a regular local ring, $A_{\mathfrak{p}}$ is regular for every prime ideal $\mathfrak{p}$ of $A$.*

Indeed, one has seen `(17.2.10)` that `dim. coh(A_𝔭) ≤ dim. coh(A)`, hence the conclusion follows at once from
`(17.3.1)`.

**Proposition (17.3.3).**

<!-- label: 0_IV.17.3.3 -->

*Let $A$, $B$ be two Noetherian local rings, $\rho : A \to B$ a local homomorphism, $\mathfrak{m}$ (resp.
$\mathfrak{n}$) the maximal ideal of $A$ (resp. $B$), $k = A/\mathfrak{m}$ (resp. $k' = B/\mathfrak{n}$) the residue
field of $A$ (resp. $B$). One has therefore a canonical homomorphism of $k'$-vector spaces*

```text
(17.3.3.1)              ψ : (𝔪/𝔪²) ⊗_k k′ → 𝔫/𝔫².
```

*(i) If $B$ is regular and if $B$ is a flat $A$-module, $A$ is regular.*

*(ii) The following conditions are equivalent:*

*a) $B$ is regular and the homomorphism $\psi$ `(17.3.3.1)` is injective.*

*b) $A$ and $B$ are regular, and for a regular system of parameters $(x_{i})_{1 \leq i \leq m}$ of $A$, the
$\phi(x_{i})$ are part of a regular system of parameters of $B$ (in which case this property holds for every regular
system of parameters of $A$).*

*c) $B$ and $B \otimes_{A} k$ are regular, and $B$ is a flat $A$-module.*

*d) $A$ and $B \otimes_{A} k$ are regular, and $B$ is a flat $A$-module.*

*e) $A$ and $B \otimes_{A} k$ are regular, and one has*

```text
(17.3.3.2)              dim(B) = dim(A) + dim(B ⊗_A k).
```

(i) One has `dim. coh(A) ≤ dim. coh(B)` by `(17.2.13)`, so it suffices to apply `(17.3.1)`.

(ii) When $A$ is assumed regular and $(x_{i})$ is a regular system of parameters of $A$, to say that $B$ is a flat
$A$-module is equivalent, by virtue of `(15.1.21)`, to saying that the sequence of $y_{i} = \phi(x_{i})$ is $B$-regular
(since $B \otimes_{A} k$ is a $k$-flat module). On the other hand, since $\dim(A) = m$, and the sequence $(y_{i})$
generates the ideal $\mathfrak{m}B$, the relation `(17.3.3.2)`, which is also written $\dim(B/\mathfrak{m}B) = \dim(B) -
m$, is equivalent to saying that the sequence $(y_{i})_{1 \leq i \leq m}$ is part of a system of parameters of $B$
`(16.3.7)`. One therefore sees that conditions b), d) and e) are equivalent respectively to the following:

b′) $A$ and $B$ are regular and $(y_{i})_{1 \leq i \leq m}$ is part of a regular system of parameters of $B$.

d′) $A$ is regular, $B/(\sum^{m}_{i=1} y_{i} B)$ is regular and the sequence $(y_{i})$ is $B$-regular.

e′) $A$ is regular, $B/(\sum^{m}_{i=1} y_{i} B)$ is regular and the sequence $(y_{i})$ is part of a system of parameters
of $B$.

Now, b′) and e′) are equivalent by virtue of `(17.1.7)`, and since d′) implies e′) `(16.4.1)` and is implied by b′)
`(17.1.7)`, it is equivalent to them. The conjunction

<!-- original page 145 -->

of b) and d) trivially implies c), and by virtue of (i), c) implies d); we have therefore proved the equivalence of b),
c), d) and e). Furthermore, it is clear that b) implies a), the classes of the $x_{i}$ in
$\mathfrak{m}/\mathfrak{m}^{2}$ forming then a basis of this $k$-vector space and the classes of the $y_{i}$ in
$\mathfrak{n}/\mathfrak{n}^{2}$ a linearly independent system of this $k'$-vector space. It remains therefore to prove
that a) implies e). Put $V = \mathfrak{m}/\mathfrak{m}^{2}$, $W = \mathfrak{n}/\mathfrak{n}^{2}$; it is immediate that
one has $\psi(V \otimes_{k} k') = (\mathfrak{m}^{2} + \mathfrak{m}B)/\mathfrak{n}^{2}$. One has on the one hand, by
virtue of `(16.3.9)`,

```text
(17.3.3.3)              dim(B) ≤ dim(A) + dim(B ⊗_A k);
```

in the second place, by `(16.2.6)`, one has

```text
(17.3.3.4)              dim(A) ≤ rg_k(V) ⊗_k k′.
```

Finally, in the local ring $B \otimes_{A} k = B/\mathfrak{m}B$, $\mathfrak{n}' = \mathfrak{n}/\mathfrak{m}B$ is the
maximal ideal, $k'$ the residue field and $\mathfrak{n}'/\mathfrak{n}'^{2}$ is isomorphic to
$\mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B) = W/\psi(V \otimes_{k} k')$; one has therefore, by `(16.2.6)`,

```text
(17.3.3.5)              dim(B ⊗_A k) ≤ rg_{k′} W - rg_{k′} ψ(V ⊗_k k′).
```

Finally, since $B$ is assumed regular, one has $\dim(B) = rg_{k'} W$ `(17.1.1)`; one therefore concludes from
`(17.3.3.3)`, `(17.3.3.4)` and `(17.3.3.5)` that one has

```text
        rg_{k′} W ≤ dim(A) + dim(B ⊗_A k) ≤ rg_{k′} W + rg_{k′}(V ⊗_k k′) - rg_{k′} ψ(V ⊗_k k′)
```

and to say that the two extreme terms of this inequality are equal means that $\psi$ is injective. Condition a)
therefore necessarily implies that in each of the relations `(17.3.3.3)`, `(17.3.3.4)` and `(17.3.3.5)`, the two sides
are equal; now, equality in `(17.3.3.4)` (resp. `(17.3.3.5)`) means that $A$ (resp. $B \otimes_{A} k$) is regular
`(17.1.1)`; one has therefore indeed proved that a) implies e).

**Proposition (17.3.4).**

<!-- label: 0_IV.17.3.4 -->

*Let $A$ be a regular local ring of dimension $n$, $\mathfrak{m}$ its maximal ideal. For every non-zero $A$-module of
finite type $M$, one has*

```text
(17.3.4.1)              prof(M) + dim. proj(M) = n.
```

We argue by induction on $m = prof(M)$. If $m = 0$, one knows `(16.4.6, (i))` that there exists a submodule $N$ of $M$
isomorphic to $k = A/\mathfrak{m}$; applying the exact sequence of Tor to the exact sequence $0 \to N \to M \to M/N \to
0$, one obtains an exact sequence

```text
                        Tor^A_{n+1}(M/N, k) → Tor^A_n(N, k) → Tor^A_n(M, k),
```

and the hypothesis that $A$ is regular implies $Tor^{A}_{n+1}(M/N, k) = 0$ `((17.3.1.1)` and `(17.2.6))`, hence
$Tor^{A}_{n}(k, k)$ is isomorphic to a sub-$A$-module of $Tor^{A}_{n}(M, k)$; applying again `(17.3.1.1)` and
`(17.2.6)`, one sees that $Tor^{A}_{n}(M, k) \neq 0$, hence $\dim. proj(M) \geq n$ `(17.2.6)`; but since $\dim. proj(M)
\leq n$ by `(17.3.1.1)`, one has indeed $\dim. proj(M) = n$. Suppose now $m > 0$, and let $x$ be an $M$-regular element
belonging to $\mathfrak{m}$; one knows then `(16.4.6, (i))` that one has $prof(M/xM) = m - 1$, and on the other hand
`(17.2.7)` `dim. proj(M/xM) = dim. proj(M) + 1`; the induction hypothesis at once proves the relation `(17.3.4.1)`.

<!-- original page 146 -->

**Corollary (17.3.5).**

<!-- label: 0_IV.17.3.5 -->

*(i) Let $A$ be a regular local ring of dimension $n$; for an $A$-module $M \neq 0$ of finite type to be free, it is
necessary and sufficient that $M$ be a Cohen-Macaulay $A$-module of dimension $n$.*

*(ii) Let $A$ be a regular local ring, $B$ a local ring, $\rho : A \to B$ a local homomorphism making $B$ an $A$-module
of finite type. For $B$ to be a free $A$-module, it is necessary and sufficient that $B$ be a Cohen-Macaulay ring and
that $\rho$ be injective (or, what comes to the same thing `(16.1.5)`, that $\dim(B) = \dim(A)$).*

(i) This follows from `(17.3.4.1)` and from the fact that for an $A$-module of finite type, it comes to the same to say
that this module is projective or free `(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`; the free
$A$-modules of finite type $M$ are therefore characterized by the relation $\dim. proj(M) = 0$ `(17.2.2, (i))`.

(ii) To say that $B$ is a Cohen-Macaulay ring is equivalent to saying that $B$ is a Cohen-Macaulay $A$-module
`(16.5.3)`, hence it suffices to apply (i), since $\dim B = \dim A$ `(16.1.5)`.

**(17.3.6)** One says that a Noetherian ring $A$ is *regular* if for every prime ideal $\mathfrak{p}$ of $A$, the local
ring $A_{\mathfrak{p}}$ is regular; when $A$ itself is a local ring, it follows from `(17.3.2)` that this definition is
equivalent to that of `(17.1.2)`. For $A$ to be regular it suffices, by virtue of `(17.3.2)`, that $A_{\mathfrak{m}}$ be
regular for every maximal ideal $\mathfrak{m}$ of $A$. Moreover, it follows at once from this definition that for every
multiplicative subset $S$ of $A$, $S^{-1} A$ is regular.

**Proposition (17.3.7).**

<!-- label: 0_IV.17.3.7 -->

*If $A$ is a regular Noetherian ring, every polynomial ring $A[T_{1}, \cdots, T_{n}]$ is regular.*

It is evidently enough to prove that the polynomial ring $B = A[T]$ is regular; since $B$ is a free $A$-module, for
every prime ideal $\mathfrak{q}$ of $B$, $B_{\mathfrak{q}}$ is a flat $A_{\mathfrak{p}}$-module, where $\mathfrak{p} =
\mathfrak{q} \cap A$ $(0_{I}, 6.3.1)$; it therefore suffices, by virtue of `(17.1.10)` [^1], to prove that
$B_{\mathfrak{q}} / \mathfrak{p} B_{\mathfrak{q}}$ is regular, and since this ring is a local ring at a prime ideal of
$A_{\mathfrak{p}}[T] / \mathfrak{p} A_{\mathfrak{p}}[T] = k[T]$ (where $k$ is the residue field
$A_{\mathfrak{p}}/\mathfrak{p} A_{\mathfrak{p}}$), it suffices to prove that $C = k[T]$ is regular; now, $C$ being
principal, the local rings at the prime ideals of $C$ are discrete valuation rings or a field (for the ideal `(0)`),
hence regular `(17.1.4)`, which completes the proof.

**Corollary (17.3.8).**

<!-- label: 0_IV.17.3.8 -->

*If $A$ is a regular ring, every formal power series ring $A[[T_{1}, \cdots, T_{n}]]$ is regular.*

Let $\mathfrak{J}$ be the ideal generated by the $T_{i}$ in the polynomial ring $A[T_{1}, \cdots, T_{n}]$; since the
latter is regular by `(17.3.7)`, and $A[[T_{1}, \cdots, T_{n}]]$ is the completion of $A[T_{1}, \cdots, T_{n}]$ for the
$\mathfrak{J}$-preadic topology `(Bourbaki, Alg. comm., chap. III, §2, n° 12, Example 1)`, the conclusion follows from
the:

**Lemma (17.3.8.1).**

<!-- label: 0_IV.17.3.8.1 -->

*Let $A$ be a regular ring, $\mathfrak{J}$ an ideal of $A$, `Â` the separated completion of $A$ for the
$\mathfrak{J}$-preadic topology. Then `Â` is regular.*

It suffices indeed `(17.3.6)` to see that for every maximal ideal $\mathfrak{n}$ of `Â`, the local ring
$\hat{A}_{\mathfrak{n}}$ is regular; one knows `(Bourbaki, Alg. comm., chap. III, §3, n° 4, prop. 8)` that
$\mathfrak{n}$

<!-- original page 147 -->

is of the form $\mathfrak{m}\hat{A}$, where $\mathfrak{m}$ is a maximal ideal of $A$ containing $\mathfrak{J}$, and that
the canonical homomorphism $A \to \hat{A}$ gives an *injective* homomorphism $A_{\mathfrak{m}} \to
\hat{A}_{\mathfrak{n}}$, such that the $\mathfrak{n}\hat{A}_{\mathfrak{n}}$-preadic topology of $\hat{A}_{\mathfrak{n}}$
induces on $A_{\mathfrak{m}}$ the $\mathfrak{m}A_{\mathfrak{m}}$-preadic topology, and such that $A_{\mathfrak{m}}$ is
dense in $\hat{A}_{\mathfrak{n}}$ for the $\mathfrak{n}\hat{A}_{\mathfrak{n}}$-preadic topology; consequently the
completions of the Noetherian local rings $A_{\mathfrak{m}}$ and $\hat{A}_{\mathfrak{n}}$ are canonically isomorphic.
Now, by hypothesis $A_{\mathfrak{m}}$ is regular, hence so is its completion `(17.1.5)`, and since the completion of
$\hat{A}_{\mathfrak{n}}$ is regular, so is $\hat{A}_{\mathfrak{n}}$ by `(17.1.5)`.

**Corollary (17.3.9).**

<!-- label: 0_IV.17.3.9 -->

*Let $A$ be a Noetherian ring, quotient of a regular Noetherian ring $B$. If $C$ is an $A$-algebra of finite type, every
ring of fractions $S^{-1} C$ of $C$ is a quotient of a regular ring.*

Indeed, $C$ is a quotient of a polynomial ring $A[T_{1}, \cdots, T_{n}]$; since $A = B/\mathfrak{J}$, where
$\mathfrak{J}$ is an ideal of $B$, one has $A[T_{1}, \cdots, T_{n}] = B[T_{1}, \cdots, T_{n}] / \mathfrak{J} B[T_{1},
\cdots, T_{n}]$; by virtue of `(17.3.7)`, one can therefore restrict to the case where $C$ is a quotient of a regular
ring $B'$; but if $S'$ is the inverse image of $S$ in $B'$, $S'$ is a multiplicative subset of $B'$ and $C$ is a
quotient ring of $S'^{-1} B'$, so that ultimately everything reduces to showing that when $C$ is regular, so is $S^{-1}
C$, which was seen in `(17.3.6)`.

The importance of quotients of regular rings lies among others in the preceding property and in the fact that they are
catenary rings `(16.5.12)`.

All the rings of importance in applications to algebraic geometry are quotients of regular rings.

[^1]: Translator's note. EGA's citation reads `(17.1.10)` but no such item exists in §17.1; the intended reference is to
    `(17.3.3, (i))` — flatness plus regularity of the special fibre implies regularity of the base.
