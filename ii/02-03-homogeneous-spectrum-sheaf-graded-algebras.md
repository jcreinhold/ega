# §3. Homogeneous spectrum of a sheaf of graded algebras

## 3.1. Homogeneous spectrum of a quasi-coherent graded $\mathcal{O}_{Y}$-algebra

**(3.1.1)**

<!-- label: II.3.1.1 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a graded $\mathcal{O}_{Y}$-algebra, and $\mathcal{M}$ a graded
$\mathcal{S}$-module. If $\mathcal{S}$ is _quasi-coherent_, then each of its homogeneous components $\mathcal{S}_{n}$ is
a quasi-coherent $\mathcal{O}_{Y}$-module, since they are the images of $\mathcal{S}$ under a homomorphism from
$\mathcal{S}$ to itself (`I, 1.3.8` and `1.3.9`); likewise, if $\mathcal{M}$ is quasi-coherent as an
$\mathcal{O}_{Y}$-module, then its homogeneous components $\mathcal{M}_{n}$ are also quasi-coherent, and conversely. For
an integer $d > 0$, we denote by $\mathcal{S}^{(d)}$ the direct sum of the $\mathcal{O}_{Y}$-modules $\mathcal{S}_{nd}$
(for $n \in \mathbb{Z}$), which is quasi-coherent if $\mathcal{S}$ is `(I, 1.3.9)`; for every integer $k$ with $0 \leq k
\leq d - 1$, we denote by $\mathcal{M}^{(d, k)}$ (or $\mathcal{M}^{(d)}$ for $k = 0$) the direct sum of the
$\mathcal{M}_{nd+k}$ (for $n \in \mathbb{Z}$), which is a graded $\mathcal{S}^{(d)}$-module, quasi-coherent if
$\mathcal{S}$ and $\mathcal{M}$ are quasi-coherent `(I, 9.6.1)`. We denote by $\mathcal{M}(n)$ the graded
$\mathcal{S}$-module such that $(\mathcal{M}(n))_{k} = \mathcal{M}_{n+k}$ for all $k \in \mathbb{Z}$; if $\mathcal{S}$
and $\mathcal{M}$ are quasi-coherent, then $\mathcal{M}(n)$ is a quasi-coherent graded $\mathcal{S}$-module
`(I, 9.6.1)`.

We say that $\mathcal{M}$ is a graded $\mathcal{S}$-module _of finite type_ (resp. admits a _finite presentation_) if,
for every $y \in Y$, there exists an open neighbourhood $U$ of $y$ and integers $n_{i}$ (resp. integers $m_{i}$ and
$n_{j}$) such that there is a surjective degree-`0` homomorphism

$$ \oplus^{r}_{i=1} (\mathcal{S}(n_{i})|U) \to \mathcal{M}|U $$

(resp. such that $\mathcal{M}|U$ is isomorphic to the cokernel of a degree-`0` homomorphism

```text
  ⊕_{i=1}^r (𝒮(m_i)|U) → ⊕_{j=1}^s (𝒮(n_j)|U)).
```

<!-- original page 49 -->

Let $U$ be an affine open of $Y$, with ring $A = \Gamma(U, \mathcal{O}_{Y})$; by hypothesis, the graded
$(\mathcal{O}_{Y}|U)$-algebra $\mathcal{S}|U$ is isomorphic to $\tilde{S}$, where $S = \Gamma(U, \mathcal{S})$ is a
graded $A$-algebra `(I, 1.4.3)`. Set $X_{U} = \operatorname{Proj}(\Gamma(U, \mathcal{S}))$. Let $U' \subset U$ be a
second affine open of $Y$, with ring $A'$, and let $j : U' \to U$ be the canonical injection, which corresponds to the
restriction homomorphism $A \to A'$; we have $\mathcal{S}|U' = j*(\mathcal{S}|U)$, and so $S' = \Gamma(U', \mathcal{S})$
is canonically identified with $S \otimes_{A} A'$ `(I, 1.6.5)`. We

<!-- original page 50 -->

conclude (2.8.10) that $X_{U'}$ is canonically identified with $X_{U} \times_{U} U'$, and so also with $f^{-1}_{U}(U')$,
where $f_{U}$ denotes the structure morphism $X_{U} \to U$ `(I, 4.4.1)`. We denote by $\sigma_{U', U}$ the canonical
isomorphism $f^{-1}_{U}(U') \xrightarrow{\sim} X_{U'}$ so defined, and by $\rho_{U', U}$ the open immersion $X_{U'} \to
X_{U}$ obtained by composing $\sigma^{-1}_{U', U}$ with the canonical injection $f^{-1}_{U}(U') \to X_{U}$. It is
immediate that, if $U'' \subset U'$ is a third affine open of $Y$, then $\rho_{U'', U} = \rho_{U'', U'} \circ \rho_{U',
U}$.

**Proposition.**

<!-- label: II.3.1.2 -->

Let $Y$ be a prescheme. For every quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$, there exists
a prescheme $X$ over $Y$, unique up to $Y$-isomorphism, with the following property: if $f : X \to Y$ is the structure
morphism, then for every affine open $U$ of $Y$, there exists an isomorphism $\eta_{U}$ from the induced prescheme
$f^{-1}(U)$ to $X_{U} = \operatorname{Proj}(\Gamma(U, \mathcal{S}))$ such that, if $V$ is a second affine open of $Y$
contained in $U$, then the diagram

```text
              η_V
   f⁻¹(V) ─────────→ X_V                                                  (3.1.2.1)
     │                │
     ↓                ↓ ρ_{V, U}
   f⁻¹(U) ─────────→ X_U
              η_U
```

commutes.

**Proof.** For two affine opens $U$, $V$ of $Y$, let $X_{U, V}$ be the prescheme induced on $f^{-1}_{U}(U \cap V)$ by
`X_U`; we will define a $Y$-isomorphism $\theta_{U, V} : X_{V, U} \xrightarrow{\sim} X_{U, V}$. For this, consider an
affine open $W \subset U \cap V$: by composing the isomorphisms

```text
                   σ_{W, U}            σ_{W, V}⁻¹
   f_U⁻¹(W) ─────────────→ X_W ─────────────→ f_V⁻¹(W),
```

we obtain an isomorphism $\tau_{W}$, and one checks at once that, if $W' \subset W$ is an affine open, then $\tau_{W'}$
is the restriction of $\tau_{W}$ to $f^{-1}_{U}(W')$; the $\tau_{W}$ are therefore the restrictions of a $Y$-isomorphism
$\theta_{V, U}$. Moreover, if $U$, $V$, $W$ are three affine opens of $Y$, and $\theta'_{U, V}$, $\theta'_{V, W}$,
$\theta'_{U, W}$ denote the restrictions of $\theta_{U, V}$, $\theta_{V, W}$, $\theta_{U, W}$ to the inverse images of
$U \cap V \cap W$ in `X_V`, `X_W`, `X_W` respectively, it follows from the above definitions that $\theta'_{U, V} \circ
\theta'_{V, W} = \theta'_{U, W}$. The existence of an $X$ satisfying the stated properties therefore follows from
`(I, 2.3.1)`; its uniqueness up to $Y$-isomorphism is trivial in view of (3.1.2.1).

**(3.1.3)**

<!-- label: II.3.1.3 -->

We say that the prescheme $X$ defined in (3.1.2) is the _homogeneous spectrum_ of the quasi-coherent graded
$\mathcal{O}_{Y}$-algebra $\mathcal{S}$, and we denote it by $\operatorname{Proj}(\mathcal{S})$. It is immediate that
$\operatorname{Proj}(\mathcal{S})$ is _separated over_ $Y$ ((2.4.2) and `(I, 5.5.5)`); if $\mathcal{S}$ is an
$\mathcal{O}_{Y}$-algebra _of finite type_ `(I, 9.6.2)`, then $\operatorname{Proj}(\mathcal{S})$ is _of finite type_
over $Y$ ((2.7.1, (ii)) and `(I, 6.3.1)`).

If $f$ is the structure morphism $X \to Y$, then for every prescheme induced by $Y$ on an open subset $U$ of $Y$,
$f^{-1}(U)$ is identified with the homogeneous spectrum $\operatorname{Proj}(\mathcal{S}|U)$.

**Proposition.**

<!-- label: II.3.1.4 -->

Let $f \in \Gamma(Y, \mathcal{S}_{d})$ for $d > 0$. There exists an open subset $X_{f}$ of the underlying space of $X =
\operatorname{Proj}(\mathcal{S})$ with the following property: for every affine open $U$ of $Y$, $X_{f} \cap
\phi^{-1}(U) = D_{+}(f|U)$ in $\phi^{-1}(U)$ identified with $X_{U} = \operatorname{Proj}(\Gamma(U, \mathcal{S}))$
(where $\phi$ denotes the structure morphism $X \to Y$).

<!-- original page 51 -->

Furthermore, the prescheme induced on $X_{f}$ is affine over $Y$ and is canonically isomorphic to
$\operatorname{Spec}(\mathcal{S}^{(d)}/(f - 1)\mathcal{S}^{(d)})$ (1.3.1).

**Proof.** We have $f|U \in \Gamma(U, \mathcal{S}_{d}) = (\Gamma(U, \mathcal{S}))_{d}$. If $U$, $U'$ are affine opens of
$Y$ with $U' \subset U$, then $f|U'$ is the image of $f|U$ under the restriction homomorphism

```text
  Γ(U, 𝒮) → Γ(U', 𝒮),
```

so $D_{+}(f|U')$ is equal (with the notation of (3.1.1)) to the prescheme induced on the inverse image $\rho^{-1}_{U',
U}(D_{+}(f|U))$ in $X_{U'}$ (2.8.1); whence the first assertion. Furthermore, the prescheme induced on $D_{+}(f|U)$ by
`X_U` is canonically identified with $\operatorname{Spec}((\Gamma(U, \mathcal{S}))_{(f|U)})$, these identifications
being compatible with the restriction homomorphisms (2.8.1); the second assertion then follows from (2.2.5) and the
commutativity of diagram (2.8.2.1).

We also say that $X_{f}$ (as an open subset of the underlying space $X$) is the set of $x \in X$ where $f$ _does not
vanish_.

**Corollary.**

<!-- label: II.3.1.5 -->

If $f \in \Gamma(Y, \mathcal{S}_{d})$ and $g \in \Gamma(Y, \mathcal{S}_{e})$, then

$$ X_{fg} = X_{f} \cap X_{g}. (3.1.5.1) $$

**Proof.** It suffices to consider the intersection of both sides with a set $\phi^{-1}(U)$, where $U$ is an affine open
of $Y$, and to apply formula (2.3.3.2).

**Corollary.**

<!-- label: II.3.1.6 -->

Let $(f_{\alpha})$ be a family of sections of $\mathcal{S}$ over $Y$ such that $f_{\alpha} \in \Gamma(Y,
\mathcal{S}_{d_{\alpha}})$; if the sheaf of ideals of $\mathcal{S}$ generated by this family `(0, 5.1.1)` contains all
the $\mathcal{S}_{n}$ from some rank on, then the underlying space $X$ is the union of the $X_{f_{\alpha}}$.

**Proof.** For every affine open $U$ of $Y$, $\phi^{-1}(U)$ is the union of the $X_{f_{\alpha}} \cap \phi^{-1}(U)$
(2.3.14).

**Corollary.**

<!-- label: II.3.1.7 -->

Let $\mathcal{A}$ be a quasi-coherent $\mathcal{O}_{Y}$-algebra; set

```text
  𝒮 = 𝒜[T] = 𝒜 ⊗_ℤ ℤ[T]
```

where $T$ is an indeterminate (and $\mathbb{Z}$, $\mathbb{Z}[T]$ are viewed as constant sheaves on $Y$). Then $X =
\operatorname{Proj}(\mathcal{S})$ is canonically identified with $\operatorname{Spec}(\mathcal{A})$. In particular,
$\operatorname{Proj}(\mathcal{O}_{Y}[T])$ is identified with $Y$.

**Proof.** Applying (3.1.6) to the unique section $f \in \Gamma(Y, \mathcal{S})$ that equals $T$ at each point of $Y$,
we see that $X_{f} = X$. Here $d = 1$, and $\mathcal{S}^{(1)}/(f - 1)\mathcal{S}^{(1)} = \mathcal{S}/(f - 1)\mathcal{S}$
is canonically isomorphic to $\mathcal{A}$; whence the corollary, by (1.2.2).

Let $g \in \Gamma(Y, \mathcal{O}_{Y})$; taking $\mathcal{S} = \mathcal{O}_{Y}[T]$, we have $g \in \Gamma(Y,
\mathcal{S}_{0})$; set

```text
  h = gT ∈ Γ(Y, 𝒮_1).
```

If $X = \operatorname{Proj}(\mathcal{S})$, then the canonical identification defined in (3.1.7) identifies $X_{h}$ with
the open subset $Y_{g}$ of $Y$ (in the sense of `(0, 5.5.2)`): indeed, we may reduce to the case $Y =
\operatorname{Spec}(A)$ affine, and everything then reduces (taking (2.2.5) into account) to the fact that the ring of
fractions $A_{g}$ is canonically identified with $A[T]/(gT - 1)A[T]$ `(0, 1.2.3)`.

**Proposition.**

<!-- label: II.3.1.8 -->

Let $\mathcal{S}$ be a quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebra.

1. For every $d > 0$, there is a canonical $Y$-isomorphism from $\operatorname{Proj}(\mathcal{S})$ to
   $\operatorname{Proj}(\mathcal{S}^{(d)})$.

<!-- original page 52 -->

1. Let $\mathcal{S}'$ be the graded $\mathcal{O}_{Y}$-algebra given by the direct sum of $\mathcal{O}_{Y}$ with the
   $\mathcal{S}_{n}$ ($n \geq 0$); then $\operatorname{Proj}(\mathcal{S}')$ and $\operatorname{Proj}(\mathcal{S})$ are
   canonically $Y$-isomorphic.
1. Let $\mathcal{L}$ be an invertible $\mathcal{O}_{Y}$-module `(0, 5.4.1)`, and let $\mathcal{S}_{(\mathcal{L})}$ be
   the graded $\mathcal{O}_{Y}$-algebra given by the direct sum of the $\mathcal{S}_{d} \otimes \mathcal{L}^{\otimes d}$
   ($d \geq 0$); then $\operatorname{Proj}(\mathcal{S})$ and $\operatorname{Proj}(\mathcal{S}_{(\mathcal{L})})$ are
   canonically $Y$-isomorphic.

**Proof.** In each of the three cases, it suffices to define the isomorphism locally on $Y$, since the verification of
compatibility with restriction from one open to a smaller one is trivial. We may thus suppose $Y$ affine, and then (i)
follows from (2.4.7, (i)) and (ii) from (2.4.8). As for (iii), if we further suppose $\mathcal{L}$ isomorphic to
$\mathcal{O}_{Y}$ (allowed, the question being local on $Y$), the isomorphism between $\operatorname{Proj}(\mathcal{S})$
and $\operatorname{Proj}(\mathcal{S}_{(\mathcal{L})})$ is evident; to define a _canonical_ isomorphism, let $Y =
\operatorname{Spec}(A)$ and $\mathcal{S} = \tilde{S}$, where $S$ is a graded $A$-algebra, and let $c$ be a generator of
the free $A$-module $L$ such that $\mathcal{L} = \tilde{L}$; then, for every $n > 0$, $x_{n} \mapsto x_{n} \otimes
c^{\otimes n}$ is an $A$-isomorphism from $S_{n}$ to $S_{n} \otimes L^{\otimes n}$, and these $A$-isomorphisms define an
$A$-isomorphism of graded algebras $\phi_{c} : S \to S_{(L)} = \oplus_{n \geq 0} S_{n} \otimes L^{\otimes n}$. Now let
$f \in S_{+}$ be homogeneous of degree $d$; for every $x \in S_{nd}$, we have $(x \otimes c^{nd})/(f \otimes c^{d})^{n}
= (x \otimes (\epsilon c)^{nd})/(f \otimes (\epsilon c)^{d})^{n}$ for every invertible $\epsilon \in A$, which shows
that the isomorphism $S_{(f)} \to (S_{(L)})_{(f \otimes c^{d})}$ induced from $\phi_{c}$ is _independent_ of the
generator $c$ of $L$, completing the proof.

**(3.1.9)**

<!-- label: II.3.1.9 -->

Recall `(0, 4.1.3)` and `(I, 1.3.14)` that, for the quasi-coherent graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ to be
_generated by the $\mathcal{O}_{Y}$-module $\mathcal{S}_{1}$_, it is necessary and sufficient that there exist an affine
open covering $(U_{\alpha})$ of $Y$ such that the graded algebra $\Gamma(U_{\alpha}, \mathcal{S})$ over
$\Gamma(U_{\alpha}, \mathcal{S}_{0})$ is generated by the set $\Gamma(U_{\alpha}, \mathcal{S}_{1})$ of its homogeneous
elements of degree `1`. For every open $V$ of $Y$, $\mathcal{S}|V$ is then generated by the $(\mathcal{O}_{Y}|V)$-module
$\mathcal{S}_{1}|V$.

**Proposition.**

<!-- label: II.3.1.10 -->

Suppose there exists a finite affine open covering $(U_{i})$ of $Y$ such that each graded algebra $\Gamma(U_{i},
\mathcal{S})$ is of finite type over $\Gamma(U_{i}, \mathcal{O}_{Y})$. Then there exists $d > 0$ such that
$\mathcal{S}^{(d)}$ is generated by $\mathcal{S}_{d}$, with $\mathcal{S}_{d}$ an $\mathcal{O}_{Y}$-module of finite
type.

**Proof.** By (2.1.6, (v)), for each $i$ there exists an integer $m_{i}$ such that $\Gamma(U_{i}, \mathcal{S}_{nm_{i}})
= (\Gamma(U_{i}, \mathcal{S}_{m_{i}}))^{n}$ for every $n > 0$; it suffices to take $d$ to be a common multiple of the
$m_{i}$, in view of (2.1.6, (i)).

**Corollary.**

<!-- label: II.3.1.11 -->

Under the hypotheses of (3.1.10), $\operatorname{Proj}(\mathcal{S})$ is $Y$-isomorphic to a homogeneous spectrum
$\operatorname{Proj}(\mathcal{S}')$, where $\mathcal{S}'$ is a graded $\mathcal{O}_{Y}$-algebra generated by
$\mathcal{S}'_{1}$, with $\mathcal{S}'_{1}$ an $\mathcal{O}_{Y}$-module of finite type.

**Proof.** It suffices to take $\mathcal{S}' = \mathcal{S}^{(d)}$, with $d$ determined by the property of (3.1.10), and
to apply (3.1.8, (i)).

**(3.1.12)**

<!-- label: II.3.1.12 -->

If $\mathcal{S}$ is a quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebra, we know `(I, 5.1.1)` that its
_nilradical_ $\mathcal{N}$ is a quasi-coherent $\mathcal{O}_{Y}$-module; we say that $\mathcal{N}_{+} = \mathcal{N} \cap
\mathcal{S}_{+}$ is the _nilradical of $\mathcal{S}_{+}$_; this is a quasi-coherent graded $\mathcal{S}_{0}$-module,
since we reduce at once to the case $Y$ affine, and the proposition then follows from (2.1.10). For every $y \in Y$,
$(\mathcal{N}_{+})_{y}$ is then the nilradical of $(\mathcal{S}_{+})_{y} = (\mathcal{S}_{y})_{+}$ `(I, 5.1.1)`. We say
that the graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ is _essentially reduced_ if $\mathcal{N}_{+} = 0$, which is
equivalent

<!-- original page 53 -->

to saying that $\mathcal{S}_{y}$ is an essentially reduced graded $\mathcal{O}_{y}$-algebra for every $y \in Y$. For
every graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$, $\mathcal{S}/\mathcal{N}_{+}$ is essentially reduced.

We say that $\mathcal{S}$ is _integral_ if, for every $y \in Y$, $\mathcal{S}_{y}$ is an integral ring and moreover
$(\mathcal{S}_{y})_{+} = (\mathcal{S}_{+})_{y} \neq 0$.

**Proposition.**

<!-- label: II.3.1.13 -->

Let $\mathcal{S}$ be a positively-graded $\mathcal{O}_{Y}$-algebra. If $X = \operatorname{Proj}(\mathcal{S})$, then the
$Y$-scheme $X_{red}$ is canonically isomorphic to $\operatorname{Proj}(\mathcal{S}/\mathcal{N}_{+})$; in particular, if
$\mathcal{S}$ is essentially reduced, then $X$ is reduced.

**Proof.** That $X' = \operatorname{Proj}(\mathcal{S}/\mathcal{N}_{+})$ is reduced follows immediately from (2.4.4,
(i)), the property being local; moreover, for every affine open $U \subset Y$, $\phi'^{-1}(U) = (\phi^{-1}(U))_{red}$
(where $\phi$ and $\phi'$ denote the structure morphisms $X \to Y$ and $X' \to Y$); one checks at once that the
canonical $U$-morphisms $\phi'^{-1}(U) \to \phi^{-1}(U)$ are compatible with restriction and so define a closed
immersion $X' \to X$ that is a homeomorphism of underlying spaces; whence the conclusion `(I, 5.1.2)`.

**Proposition.**

<!-- label: II.3.1.14 -->

Let $Y$ be an integral prescheme, and $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra such that
$\mathcal{S}_{0} = \mathcal{O}_{Y}$.

1. If $\mathcal{S}$ is integral (3.1.12), then $X = \operatorname{Proj}(\mathcal{S})$ is integral and the structure
   morphism $\phi : X \to Y$ is dominant.
1. Suppose further that $\mathcal{S}$ is essentially reduced. Then conversely, if $X$ is integral and $\phi$ is
   dominant, then $\mathcal{S}$ is integral.

**Proof.**

(i) If $(U_{\alpha})$ is a base of $Y$ consisting of non-empty affine opens, it suffices to prove the proposition with
$Y$ replaced by one of the $U_{\alpha}$ and $\mathcal{S}$ by $\mathcal{S}|U_{\alpha}$: indeed, on the one hand the
underlying spaces $\phi^{-1}(U_{\alpha})$ will be irreducible (hence non-empty) opens of $X$ such that
$\phi^{-1}(U_{\alpha}) \cap \phi^{-1}(U_{\beta}) \neq \emptyset$ for every pair of indices (since $U_{\alpha} \cap
U_{\beta}$ contains some $U_{\gamma}$), so $X$ will be irreducible `(0, 2.1.4)`; on the other hand, $X$ will be reduced,
since this is a local property, and so $X$ will be integral and $\phi(X)$ dense in $Y$.

Suppose then that $Y = \operatorname{Spec}(A)$, $A$ integral `(I, 5.1.4)`, and $\mathcal{S} = \tilde{S}$, with $S$ a
graded $A$-algebra; the hypothesis is that for every $y \in Y$, $\tilde{S}_{y} = S_{y}$ is an integral graded ring with
$(S_{y})_{+} \neq 0$. It suffices to show $S$ is an _integral_ ring, since then $S_{+} \neq 0$ and we may apply (2.4.4,
(ii)). Let $f, g \neq 0$ in $S$ and suppose $fg = 0$; for every $y \in Y$ we have $(f/1)(g/1) = 0$ in $S_{y}$, so $f/1 =
0$ or $g/1 = 0$ by hypothesis. Suppose, say, $f/1 = 0$ in $S_{y}$; this means there exists $a \in A$ with $a \notin
\mathfrak{j}_{y}$ and $af = 0$; then for every $z \in Y$, $(a/1)(f/1) = 0$ in the integral ring $S_{z}$, and since $a/1
\neq 0$ (since $A$ is integral), $f/1 = 0$, which forces $f = 0$.

(ii) The question being local on $Y$, we may again assume $Y = \operatorname{Spec}(A)$, $A$ integral, and $\mathcal{S} =
\tilde{S}$. By hypothesis, for every $y \in Y$, $(S_{y})_{+}$ contains no non-zero nilpotent element, and the same holds
for $(S_{0})_{y} = A_{y}$ by hypothesis; so $S_{y}$ is a reduced ring for every $y \in Y$, whence $S$ itself is reduced
`(I, 5.1.1)`. The hypothesis that $X$ is integral implies that $S$ is essentially integral (2.4.4, (ii)), and everything
reduces to showing that the annihilator $\mathfrak{J}$ of $S_{+}$ in $A = S_{0}$ is reduced to `0` (2.1.11). Otherwise
we would have

<!-- original page 54 -->

$(S_{h})_{+} = 0$ for some $h \neq 0$ in $\mathfrak{J}$, hence (3.1.1) $\phi^{-1}(D(h)) = \emptyset$, and $\phi(X)$
would not be dense in $Y$ contrary to hypothesis (since $D(h) \neq \emptyset$, $h$ being non-nilpotent).

## 3.2. Sheaf on $\operatorname{Proj}(\mathcal{S})$ associated to a graded $\mathcal{S}$-module

**(3.2.1)**

<!-- label: II.3.2.1 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebra, and $\mathcal{M}$ a
quasi-coherent graded $\mathcal{S}$-module (on $(Y, \mathcal{O}_{Y})$, or equivalently `(I, 9.6.1)` on the ringed space
$(Y, \mathcal{S})$). With the notation of (3.1.1), we denote by $\tilde{\mathcal{M}}_{U}$ the quasi-coherent
$\mathcal{O}_{X_{U}}$-module $\tilde{\Gamma(U, \mathcal{M})}$; for $U' \subset U$, $\Gamma(U', \mathcal{M})$ is
canonically identified with $\Gamma(U, \mathcal{M}) \otimes_{A} A'$ `(I, 1.6.4)`; thus $\tilde{\mathcal{M}}_{U'} =
\rho_{U', U}*(\tilde{\mathcal{M}}_{U})$ (2.8.11).

**Proposition.**

<!-- label: II.3.2.2 -->

There exists on $\operatorname{Proj}(\mathcal{S}) = X$ a unique quasi-coherent $\mathcal{O}_{X}$-module
$\tilde{\mathcal{M}}$ such that, for every affine open $U$ of $Y$, $\eta_{U}*(\tilde{\Gamma(U, \mathcal{M})}) =
\tilde{\mathcal{M}}|f^{-1}(U)$ (where $\eta_{U}$ denotes the isomorphism $f^{-1}(U) \xrightarrow{\sim}
\operatorname{Proj}(\Gamma(U, \mathcal{S}))$ and $f$ is the structure morphism $X \to Y$).

**Proof.** Since $\rho_{U', U}$ is identified with the injection morphism $f^{-1}(U') \to f^{-1}(U)$ (3.1.2.1), the
proposition follows at once from the relation $\tilde{\mathcal{M}}_{U'} = \rho_{U', U}*(\tilde{\mathcal{M}}_{U})$ and
the gluing principle for sheaves `(0, 3.3.1)`.

We say that $\tilde{\mathcal{M}}$ is the $\mathcal{O}_{X}$-module _associated to_ the quasi-coherent graded
$\mathcal{S}$-module $\mathcal{M}$.

**Proposition.**

<!-- label: II.3.2.3 -->

Let $\mathcal{M}$ be a quasi-coherent graded $\mathcal{S}$-module, and let $f \in \Gamma(Y, \mathcal{S}_{d})$ ($d > 0$).
If $\xi_{f}$ is the canonical isomorphism from $X_{f}$ to the $Y$-prescheme $Z_{f} =
\operatorname{Spec}(\mathcal{S}^{(d)}/(f - 1)\mathcal{S}^{(d)})$ (3.1.4), then
$(\xi_{f})_{*}(\tilde{\mathcal{M}}|X_{f})$ is the $\mathcal{O}_{Z_{f}}$-module $\tilde{\mathcal{M}^{(d)}/(f -
1)\mathcal{M}^{(d)}}$ (1.4.3).

**Proof.** The question being local on $Y$, we reduce immediately to (2.2.5), using the commutativity of diagram
(2.8.12.1).

**Proposition.**

<!-- label: II.3.2.4 -->

The $\mathcal{O}_{X}$-module $\tilde{\mathcal{M}}$ is a covariant additive exact functor in $\mathcal{M}$ from the
category of quasi-coherent graded $\mathcal{S}$-modules to the category of quasi-coherent $\mathcal{O}_{X}$-modules,
which commutes with inductive limits and direct sums.

**Proof.** The question being local on $Y$, we reduce to `(I, 1.3.11)`, `(I, 1.3.9)`, and (2.5.4).

In particular, if $\mathcal{N}$ is a quasi-coherent graded sub-$\mathcal{S}$-module of $\mathcal{M}$, then
$\tilde{\mathcal{N}}$ is canonically identified with a quasi-coherent sub-$\mathcal{O}_{X}$-module of
$\tilde{\mathcal{M}}$; more specifically, for every quasi-coherent graded sheaf of ideals $\mathcal{J}$ of
$\mathcal{S}$, $\tilde{\mathcal{J}}$ is a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$.

If $\mathcal{M}$ is a quasi-coherent graded $\mathcal{S}$-module and $\mathcal{I}$ a quasi-coherent sheaf of ideals of
$\mathcal{O}_{Y}$, then $\mathcal{IM}$ is a quasi-coherent graded sub-$\mathcal{S}$-module of $\mathcal{M}$, and

$$ \tilde{\mathcal{IM}} = \mathcal{I} \cdot \tilde{\mathcal{M}} (3.2.4.1) $$

(the right-hand side in the sense of `(0, 4.3.5)`). It suffices to verify this in the case $Y = \operatorname{Spec}(A)$
affine, $\mathcal{S} = \tilde{S}$ with $S$ a graded $A$-algebra, $\mathcal{M} = \tilde{M}$

<!-- original page 55 -->

with $M$ a graded $S$-module, and $\mathcal{I} = \mathfrak{J}$ with $\mathfrak{J}$ an ideal of $A$. For every
homogeneous element $f$ of $S_{+}$, the restriction to $D_{+}(f) = \operatorname{Spec}(S_{(f)})$ of the left-hand side
of (3.2.4.1) is associated to $(\mathfrak{J}M)_{(f)} = \mathfrak{J} \cdot M_{(f)}$, and the same holds for the
restriction of the right-hand side, by `(I, 1.3.13)` and `(I, 1.6.9)`.

**Proposition.**

<!-- label: II.3.2.5 -->

Let $f \in \Gamma(Y, \mathcal{S}_{d})$ ($d > 0$). On the open subset $X_{f}$, the $(\mathcal{O}_{X}|X_{f})$-module
$\tilde{\mathcal{S}(nd)}|X_{f}$ is canonically isomorphic to $\mathcal{O}_{X}|X_{f}$ for every $n \in \mathbb{Z}$. In
particular, if the $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ is generated by $\mathcal{S}_{1}$ (3.1.9), then the
$\mathcal{O}_{X}$-modules $\tilde{\mathcal{S}(n)}$ are invertible for every $n \in \mathbb{Z}$.

**Proof.** Indeed, for every affine open $U$ of $Y$, we defined in (2.5.7) a canonical isomorphism from
$\tilde{\mathcal{S}(nd)}|(X_{f} \cap \phi^{-1}(U))$ to $\mathcal{O}_{X}|(X_{f} \cap \phi^{-1}(U))$, in view of (3.1.4)
(where $\phi$ is the structure morphism $X \to Y$); one checks at once that these isomorphisms are compatible with
restriction from $U$ to an affine open $U' \subset U$, whence the first assertion. For the second, note that if
$\mathcal{S}$ is generated by $\mathcal{S}_{1}$, there is an affine open covering $(U_{\alpha})$ of $Y$ such that
$\Gamma(U_{\alpha}, \mathcal{S})$ is generated by $\Gamma(U_{\alpha}, \mathcal{S})_{1} = \Gamma(U_{\alpha},
\mathcal{S}_{1})$; we then apply (2.5.9), the property of being invertible being local.

We also set, for every $n \in \mathbb{Z}$,

$$ \mathcal{O}_{X}(n) = \tilde{\mathcal{S}(n)} (3.2.5.1) $$

and, for every $\mathcal{O}_{X}$-module $\mathcal{F}$,

```text
  ℱ(n) = ℱ ⊗_{𝒪_X} 𝒪_X(n).                                                (3.2.5.2)
```

It follows at once from these definitions that, for every open $U$ of $Y$,

$$ \tilde{(\mathcal{S}|U)(n)} = \mathcal{O}_{X}(n)|f^{-1}(U) $$

where $f$ is the structure morphism $X \to Y$.

**Proposition.**

<!-- label: II.3.2.6 -->

Let $\mathcal{M}$ and $\mathcal{N}$ be quasi-coherent graded $\mathcal{S}$-modules. There is a canonical homomorphism,
functorial in $\mathcal{M}$ and $\mathcal{N}$,

```text
  λ : ℳ̃ ⊗_{𝒪_X} 𝒩̃ → (ℳ ⊗_𝒮 𝒩)̃                                            (3.2.6.1)
```

and a canonical homomorphism, functorial in $\mathcal{M}$ and $\mathcal{N}$,

```text
  μ : (𝓗𝓸𝓶_𝒮(ℳ, 𝒩))̃ → 𝓗𝓸𝓶_{𝒪_X}(ℳ̃, 𝒩̃).                                   (3.2.6.2)
```

Furthermore, if $\mathcal{S}$ is generated by $\mathcal{S}_{1}$ (3.1.9), then $\lambda$ is an isomorphism; if in
addition $\mathcal{M}$ admits a finite presentation (3.1.1), then $\mu$ is an isomorphism.

**Proof.** The isomorphisms $\lambda$ and $\mu$ were defined in (2.5.11.2) and (2.5.12.2) when $Y$ is affine; these
definitions being local, they extend at once to the general case considered here, in view of (2.8.14).

**Corollary.**

<!-- label: II.3.2.7 -->

If $\mathcal{S}$ is generated by $\mathcal{S}_{1}$, then for any $m, n \in \mathbb{Z}$,

```text
  𝒪_X(m) ⊗_{𝒪_X} 𝒪_X(n) = 𝒪_X(m + n)                                      (3.2.7.1)

  𝒪_X(n) = (𝒪_X(1))^{⊗ n}                                                 (3.2.7.2)
```

up to canonical isomorphism.

<!-- original page 56 -->

**Corollary.**

<!-- label: II.3.2.8 -->

If $\mathcal{S}$ is generated by $\mathcal{S}_{1}$, then for every graded $\mathcal{S}$-module $\mathcal{M}$ and every
$n \in \mathbb{Z}$,

$$ \tilde{\mathcal{M}(n)} = \tilde{\mathcal{M}}(n) (3.2.8.1) $$

up to canonical isomorphism.

**Proof.** This follows from the corresponding properties for $Y$ affine ((2.5.14) and (2.5.15)) together with (2.8.11).

**Remarks.**

<!-- label: II.3.2.9 -->

(i) If $\mathcal{S} = \mathcal{A}[T]$ with $\mathcal{A}$ a quasi-coherent $\mathcal{O}_{Y}$-algebra (3.1.7), one checks
at once that all the invertible $\mathcal{O}_{X}$-modules $\mathcal{O}_{X}(n)$ are canonically isomorphic to
$\mathcal{O}_{X}$.

Furthermore, let $\mathcal{N}$ be a quasi-coherent $\mathcal{A}$-module, and set $\mathcal{M} = \mathcal{N}
\otimes_{\mathcal{A}} \mathcal{A}[T]$. It then follows from (3.2.3) and (3.1.7) that, under the canonical identification
of $X = \operatorname{Proj}(\mathcal{A}[T])$ with $X' = \operatorname{Spec}(\mathcal{A})$, the $\mathcal{O}_{X}$-module
$\tilde{\mathcal{M}}$ is identified with the $\mathcal{O}_{X'}$-module $\tilde{\mathcal{N}}$ associated to $\mathcal{N}$
(in the sense of (1.4.3)).

(ii) Let $\mathcal{S}$ be an arbitrary graded $\mathcal{O}_{Y}$-algebra, and let $\mathcal{S}'$ be the graded
$\mathcal{O}_{Y}$-algebra such that $\mathcal{S}'_{0} = \mathcal{O}_{Y}$ and $\mathcal{S}'_{n} = \mathcal{S}_{n}$ for
every $n > 0$; the canonical isomorphism from $X = \operatorname{Proj}(\mathcal{S})$ to $X' =
\operatorname{Proj}(\mathcal{S}')$ (3.1.8, (ii)) identifies $\mathcal{O}_{X}(n)$ with $\mathcal{O}_{X'}(n)$ for every $n
\in \mathbb{Z}$: this follows from the same proposition in the affine case (2.5.16) and from the fact that, on the
affine opens of $Y$, these identifications commute with restriction. Similarly, let $X^{(d)} =
\operatorname{Proj}(\mathcal{S}^{(d)})$; the canonical isomorphism from $X$ to $X^{(d)}$ (3.1.8, (i)) identifies
$\mathcal{O}_{X}(nd)$ with $\mathcal{O}_{X^{(d)}}(n)$ for every $n \in \mathbb{Z}$.

**Proposition.**

<!-- label: II.3.2.10 -->

Let $\mathcal{L}$ be an invertible $\mathcal{O}_{Y}$-module, and let $g$ be the canonical isomorphism $X_{(\mathcal{L})}
= \operatorname{Proj}(\mathcal{S}_{(\mathcal{L})}) \xrightarrow{\sim} X = \operatorname{Proj}(\mathcal{S})$ (3.1.8,
(iii)). For every $n \in \mathbb{Z}$, $g_{*}(\mathcal{O}_{X_{(\mathcal{L})}}(n))$ is canonically isomorphic to
$\mathcal{O}_{X}(n) \otimes_{Y} \mathcal{L}^{\otimes n}$.

**Proof.** Suppose first that $Y$ is affine with ring $A$ and $\mathcal{L} = \tilde{L}$, with $L$ a free $A$-module of
rank `1`. With the notation of the proof of (3.1.8, (iii)), we define, for $f \in S_{d}$, an isomorphism from
$(S(n))_{(f)} \otimes_{A} L^{\otimes n}$ to $(S_{(L)}(n))_{(f \otimes c^{d})}$ by sending $(x/f^{k}) \otimes c^{n}$,
with $x \in S_{kd+n}$, to $(x \otimes c^{n+kd})/(f \otimes c^{d})^{k}$; one checks at once that this isomorphism is
independent of the chosen generator $c$ of $L$; furthermore, the isomorphisms so defined for each $f \in S_{+}$ are
compatible with the restriction operators $D_{+}(f) \to D_{+}(fg)$. Finally, in the general case, one sees easily, going
back to the definitions (3.1.1), that the isomorphisms so defined for each affine open $U$ of $Y$ are compatible with
passage from $U$ to an affine open $U' \subset U$.

## 3.3. Graded $\mathcal{S}$-module associated to a sheaf on $\operatorname{Proj}(\mathcal{S})$

_Throughout this entire section we suppose that the graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ is generated by
$\mathcal{S}_{1}$ (3.1.9)._ Recall that, by (3.1.8, (i)), this restriction is not essential, given the finiteness
conditions (3.1.10).

**(3.3.1)**

<!-- label: II.3.3.1 -->

Let $p$ be the structure morphism $X = \operatorname{Proj}(\mathcal{S}) \to Y$. For every $\mathcal{O}_{X}$-module
$\mathcal{F}$, set

```text
  Γ_*(ℱ) = ⊕_{n ∈ ℤ} p_*(ℱ(n))                                            (3.3.1.1)
```

<!-- original page 57 -->

and in particular

```text
  Γ_*(𝒪_X) = ⊕_{n ∈ ℤ} p_*(𝒪_X(n)).                                       (3.3.1.2)
```

We know `(0, 4.2.2)` that there is a canonical homomorphism

```text
  p_*(ℱ) ⊗_{𝒪_Y} p_*(𝒢) → p_*(ℱ ⊗_{𝒪_X} 𝒢)
```

for two $\mathcal{O}_{X}$-modules $\mathcal{F}$ and $\mathcal{G}$; we therefore deduce from (3.2.7.1) that
$\Gamma_{*}(\mathcal{O}_{X})$ is endowed with the structure of a _graded $\mathcal{O}_{Y}$-algebra_, and (3.2.5.2)
similarly defines on $\Gamma_{*}(\mathcal{F})$ the structure of a _graded $\Gamma_{*}(\mathcal{O}_{X})$-module_.

By (3.2.5) and the left-exactness of $p_{*}$ `(0, 4.2.1)`, $\Gamma_{*}(\mathcal{F})$ is a covariant additive left-exact
functor in $\mathcal{F}$ from the category of $\mathcal{O}_{X}$-modules to the category of graded
$\mathcal{O}_{Y}$-modules (with morphisms of degree `0`). In particular, if $\mathcal{J}$ is a sheaf of ideals of
$\mathcal{O}_{X}$, then $\Gamma_{*}(\mathcal{J})$ is identified with a graded sheaf of ideals of
$\Gamma_{*}(\mathcal{O}_{X})$.

**(3.3.2)**

<!-- label: II.3.3.2 -->

Let $\mathcal{M}$ be a quasi-coherent graded $\mathcal{S}$-module. For every affine open $U$ of $Y$, we defined in
(2.6.2) a homomorphism of abelian groups

```text
  α_{0, U} : Γ(U, ℳ_0) → Γ(p⁻¹(U), ℳ̃).
```

It is immediate that these homomorphisms commute with restriction (2.8.13.1) and so define (without using the hypothesis
that $\mathcal{S}$ is generated by $\mathcal{S}_{1}$) a homomorphism of sheaves of abelian groups

$$ \alpha_{0} : \mathcal{M}_{0} \to p_{*}(\tilde{\mathcal{M}}). (3.3.2.1) $$

Applying this to each $\mathcal{M}_{n} = (\mathcal{M}(n))_{0}$ and using (3.2.8.1), we define a homomorphism of sheaves
of abelian groups

$$ \alpha_{n} : \mathcal{M}_{n} \to p_{*}(\tilde{\mathcal{M}}(n)) (3.3.2.2) $$

for every $n \in \mathbb{Z}$, whence a functorial homomorphism (of degree `0`) of graded sheaves of abelian groups

$$ \alpha : \mathcal{M} \to \Gamma_{*}(\tilde{\mathcal{M}}) (3.3.2.3) $$

(also denoted $\alpha_{\mathcal{M}}$).

Taking $\mathcal{M} = \mathcal{S}$ in particular, one checks that $\alpha : \mathcal{S} \to \Gamma_{*}(\mathcal{O}_{X})$
is a homomorphism of graded $\mathcal{O}_{Y}$-algebras, and that (3.3.2.3) is a di-homomorphism of graded modules
relative to this homomorphism of graded algebras.

We also note that to each $\alpha_{n}$ corresponds `(0, 4.4.3)` a canonical homomorphism of $\mathcal{O}_{X}$-modules

$$ \alpha_{n}\sharp : p*(\mathcal{M}_{n}) \to \tilde{\mathcal{M}}(n). (3.3.2.4) $$

One checks without difficulty that this homomorphism is precisely the one which corresponds functorially (3.2.4) to the
canonical homomorphism (of degree `0`) of graded $\mathcal{O}_{Y}$-modules

```text
  ℳ_n ⊗_{𝒪_Y} 𝒮 → ℳ(n)                                                   (3.3.2.5)
```

<!-- original page 58 -->

where the grading on the right-hand side comes naturally from that of $\mathcal{S}$. We may restrict to the case $Y =
\operatorname{Spec}(A)$ affine, $\mathcal{M} = \tilde{M}$, and $\mathcal{S} = \tilde{S}$, with the graded $A$-algebra
$S$ generated by `S_1`, so that as $f$ runs over `S_1` the $D_{+}(f)$ form a covering of $X$. Returning to the
definitions (2.6.2) and using `(I, 1.6.7)`, the restriction to $D_{+}(f)$ of the homomorphism (3.3.2.4) corresponds
`(I, 1.3.8)` to the homomorphism of $S_{(f)}$-modules $M_{n} \otimes_{A} S_{(f)} \to (S(n))_{(f)}$ sending $x \otimes 1$
(with $x \in M_{n}$) to $x/1$; this proves the claim.

**Proposition.**

<!-- label: II.3.3.3 -->

For every section $f \in \Gamma(Y, \mathcal{S}_{d})$ ($d > 0$), $X_{f}$ coincides with the set of points of $X$ where
$\alpha_{d}(f)$ (considered as a section of $\mathcal{O}_{X}(d)$) does not vanish `(0, 5.5.2)`.

**Proof.** (Note that $\alpha_{d}(f)$ is a section of $p_{*}(\mathcal{O}_{X}(d))$ over $Y$, but by definition such a
section is also a section of $\mathcal{O}_{X}(d)$ over $X$ `(0, 4.2.1)`.) The definition of $X_{f}$ (3.1.4) reduces us
to the case $Y$ affine, which was handled in (2.6.3).

**(3.3.4)**

<!-- label: II.3.3.4 -->

From now on, in addition to the hypothesis at the start of this section, we suppose that for every quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, the $p_{*}(\mathcal{F}(n))$ are quasi-coherent on $Y$, so that
$\Gamma_{*}(\mathcal{F}) = \oplus_{n \in \mathbb{Z}} p_{*}(\mathcal{F}(n))$ is also a quasi-coherent
$\mathcal{O}_{Y}$-module (`(I, 1.4.1)` and `(I, 1.3.9)`); this will always be the case in particular if $X$ is of finite
type over $Y$ `(I, 9.2.2)`. We thus conclude that $\tilde{\Gamma_{*}(\mathcal{F})}$ is defined and is a quasi-coherent
$\mathcal{O}_{X}$-module. For every affine open $U$ of $Y$, we have (`(I, 1.3.9)` and (2.5.4))

```text
  (Γ(U, ⊕_{n ∈ ℤ} p_*(ℱ(n))))̃
    = ⊕_{n ∈ ℤ} (Γ(U, p_*(ℱ(n))))̃
    = ⊕_{n ∈ ℤ} (Γ(p⁻¹(U), ℱ(n)))̃
    = (⊕_{n ∈ ℤ} Γ(p⁻¹(U), ℱ(n)))̃
    = (Γ_*(ℱ|p⁻¹(U)))̃
```

and so (2.6.4) we have a canonical homomorphism

```text
  β_U : (Γ(U, ⊕_{n ∈ ℤ} p_*(ℱ(n))))̃ → ℱ|p⁻¹(U).
```

Furthermore, the commutativity of (2.8.13.2) shows that these homomorphisms commute with restriction on $Y$; we thus
obtain a canonical functorial homomorphism

$$ \beta : \tilde{\Gamma_{*}(\mathcal{F})} \to \mathcal{F} (3.3.4.1) $$

(also denoted $\beta_{\mathcal{F}}$) for quasi-coherent $\mathcal{O}_{X}$-modules.

**Proposition.**

<!-- label: II.3.3.5 -->

Let $\mathcal{M}$ be a quasi-coherent graded $\mathcal{S}$-module, and $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-module; the composite homomorphisms

```text
                α̃                    β
  ℳ̃ ─────→ (Γ_*(ℳ̃))̃ ─────→ ℳ̃                                            (3.3.5.1)

                  α                          Γ_*(β)
  Γ_*(ℱ) ─────→ Γ_*((Γ_*(ℱ))̃) ─────→ Γ_*(ℱ)                              (3.3.5.2)
```

are the identity isomorphisms.

**Proof.** The question is local on $Y$, so we reduce to (2.6.5).

<!-- original page 59 -->

## 3.4. Finiteness conditions

**Proposition.**

<!-- label: II.3.4.1 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent $\mathcal{O}_{Y}$-algebra generated by $\mathcal{S}_{1}$ (3.1.9);
suppose further that $\mathcal{S}_{1}$ is of finite type. Then $X = \operatorname{Proj}(\mathcal{S})$ is of finite type
over $Y$.

**Proof.** The question being local on $Y$, we may suppose $Y$ affine with ring $A$; then $\mathcal{S} = \tilde{S}$ with
$S = \Gamma(Y, \mathcal{S})$, and by hypothesis $S$ is an $A$-algebra generated by $S_{1} = \Gamma(Y, \mathcal{S}_{1})$,
where we may further assume that `S_1` is an $A$-module of finite type (`(I, 1.3.9)` and `(I, 1.3.12)`). Then $S$ is a
graded $A$-algebra of finite type, and we reduce to (2.7.1, (ii)).

**(3.4.2)**

<!-- label: II.3.4.2 -->

Let $\mathcal{S}$ be a quasi-coherent graded $\mathcal{O}_{Y}$-algebra; for a quasi-coherent graded $\mathcal{S}$-module
$\mathcal{M}$, we consider the following finiteness conditions:

- **(TF)** _There exists an integer $n$ such that the $\mathcal{S}$-module $\oplus_{k \geq n} \mathcal{M}_{k}$ is of
  finite type._
- **(TN)** _There exists an integer $n$ such that $\mathcal{M}_{k} = 0$ for $k \geq n$._

If $\mathcal{M}$ satisfies (TN), then $\tilde{\mathcal{M}} = 0$, since this is a local property on $Y$ (2.7.2).

Let $\mathcal{M}$, $\mathcal{N}$ be quasi-coherent graded $\mathcal{S}$-modules; we say that a homomorphism $u :
\mathcal{M} \to \mathcal{N}$ of degree `0` is _(TN)-injective_ (resp. _(TN)-surjective_, _(TN)-bijective_) if there
exists an integer $n$ such that $u_{k} : \mathcal{M}_{k} \to \mathcal{N}_{k}$ is injective (resp. surjective, bijective)
for $k \geq n$; then $\tilde{u} : \tilde{\mathcal{M}} \to \tilde{\mathcal{N}}$ is injective (resp. surjective,
bijective) by (2.7.2), the question being local on $Y$, and in view of `(I, 1.3.9)`; when $u$ is (TN)-bijective, we also
say that $u$ is a _(TN)-isomorphism_.

**Proposition.**

<!-- label: II.3.4.3 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra generated by $\mathcal{S}_{1}$,
with $\mathcal{S}_{1}$ assumed of finite type. Let $\mathcal{M}$ be a quasi-coherent graded $\mathcal{S}$-module.

1. If $\mathcal{M}$ satisfies (TF), then $\tilde{\mathcal{M}}$ is of finite type.
1. Suppose $\mathcal{M}$ satisfies (TF); for $\tilde{\mathcal{M}} = 0$, it is necessary and sufficient that
   $\mathcal{M}$ satisfy (TN).

**Proof.** The questions being local on $Y$, we reduce to the case $Y$ affine with ring $A$, $\mathcal{S} = \tilde{S}$
with $S$ a graded $A$-algebra such that the ideal $S_{+}$ is of finite type, and $\mathcal{M} = \tilde{M}$ with $M$ a
graded $S$-module; the proposition then follows from (2.7.3).

**Theorem.**

<!-- label: II.3.4.4 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra generated by $\mathcal{S}_{1}$,
with $\mathcal{S}_{1}$ assumed of finite type; let $X = \operatorname{Proj}(\mathcal{S})$. For every quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, the canonical homomorphism $\beta$ (3.3.4) is an isomorphism.

**Proof.** First, $\beta$ is defined by virtue of (3.4.1). To see that $\beta$ is an isomorphism, we reduce to the case
$Y$ affine with ring $A$, $\mathcal{S} = \tilde{S}$ with $S$ a graded $A$-algebra generated by `S_1`, and `S_1` an
$A$-module of finite type. It then suffices to apply (2.7.5).

**Corollary.**

<!-- label: II.3.4.5 -->

Under the hypotheses of (3.4.4), every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ is isomorphic to an
$\mathcal{O}_{X}$-module of the form $\tilde{\mathcal{M}}$, where $\mathcal{M}$ is a quasi-coherent graded
$\mathcal{S}$-module. If furthermore $\mathcal{F}$ is of finite type, and if we assume that $Y$ is a quasi-compact
scheme or that the underlying space of $Y$ is Noetherian, then we may take $\mathcal{M}$ to be of finite type.

<!-- original page 60 -->

**Proof.** The first assertion follows at once from (3.4.4) by taking $\mathcal{M} = \Gamma_{*}(\mathcal{F})$. To
establish the second, it suffices to show that $\mathcal{M}$ is the inductive limit of its _graded_
sub-$\mathcal{S}$-modules of finite type $\mathcal{N}_{\lambda}$: indeed, it will follow that $\tilde{\mathcal{M}}$ is
the inductive limit of the $\tilde{\mathcal{N}}_{\lambda}$ (3.2.4), hence $\mathcal{F}$ is the inductive limit of the
$\beta(\tilde{\mathcal{N}}_{\lambda})$; since $X$ is quasi-compact ((3.4.1) and `(I, 6.3.1)`) and $\mathcal{F}$ is of
finite type, $\mathcal{F}$ will necessarily equal one of the $\beta(\tilde{\mathcal{N}}_{\lambda})$ `(0, 5.2.3)`.

To define the $\mathcal{N}_{\lambda}$ having $\mathcal{M}$ as inductive limit, it suffices to consider, for each $n \in
\mathbb{Z}$, the quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}_{n}$, which is the inductive limit of its
sub-$\mathcal{O}_{Y}$-modules $\mathcal{M}^{(\mu_{n})}_{n}$ of finite type, by the hypothesis on $Y$ `(I, 9.4.9)`; one
sees at once that $\mathcal{P}_{\mu_{n}} = \mathcal{S} \cdot \mathcal{M}^{(\mu_{n})}_{n}$ is a graded
$\mathcal{S}$-module of finite type, and that taking the $\mathcal{N}_{\lambda}$ to be the finite sums of
$\mathcal{S}$-modules of the form $\mathcal{P}_{\mu_{n}}$ gives the desired objects.

**Corollary.**

<!-- label: II.3.4.6 -->

Suppose the hypotheses of (3.4.4) are satisfied and, moreover, that the underlying space of $Y$ is quasi-compact; let
$\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-module of finite type. Then there exists $n_{0}$ such that for every
$n \geq n_{0}$ the canonical homomorphism $\sigma : p*(p_{*}(\mathcal{F}(n))) \to \mathcal{F}(n)$ `(0, 4.4.3)` is
surjective.

**Proof.** For every $y \in Y$, let $U$ be an affine open neighbourhood of $y$ in $Y$. There exists an integer
$n_{0}(U)$ such that, for $n \geq n_{0}(U)$, $\mathcal{F}(n)|p^{-1}(U)$ is generated by finitely many of its sections
over $p^{-1}(U)$ (2.7.9); but these sections are the canonical images of sections of $p*(p_{*}(\mathcal{F}(n)))$ over
$p^{-1}(U)$ (`(0, 3.7.1)` and `(0, 4.4.3)`), so $\mathcal{F}(n)|p^{-1}(U)$ equals the canonical image of
$p*(p_{*}(\mathcal{F}(n)))|p^{-1}(U)$. Finally, since $Y$ is quasi-compact, there is a finite cover of $Y$ by affine
opens $U_{i}$, and taking $n_{0}$ to be the largest of the $n_{0}(U_{i})$ finishes the proof.

**Remarks.**

<!-- label: II.3.4.7 -->

If $p = (\psi, \theta) : X \to Y$ is a morphism of ringed spaces and $\mathcal{F}$ an $\mathcal{O}_{X}$-module, then the
fact that the canonical homomorphism $\sigma : p*(p_{*}(\mathcal{F})) \to \mathcal{F}$ is surjective can be made
explicit as follows `(0, 4.4.1)`: for every $x \in X$ and every section $s$ of $\mathcal{F}$ over an open neighbourhood
$V$ of $x$, there exist an open neighbourhood $U$ of $p(x)$ in $Y$, finitely many sections $t_{i}$ ($1 \leq i \leq m$)
of $\mathcal{F}$ over $p^{-1}(U)$, a neighbourhood $W \subset V \cap p^{-1}(U)$ of $x$, and sections $a_{i}$ ($1 \leq i
\leq m$) of $\mathcal{O}_{X}$ over $W$ such that

```text
  s|W = ∑_{i=1}^m a_i · (t_i|W).
```

When $Y$ is an _affine scheme_ and $p_{*}(\mathcal{F})$ is _quasi-coherent_, this condition is equivalent to
$\mathcal{F}$ being _generated by its sections over $X$_ `(0, 5.5.1)`: indeed, if $Y = \operatorname{Spec}(A)$, we may
suppose $U = D(f)$ with $f \in A$; then there exist an integer $n > 0$ and sections $s_{i}$ of $\mathcal{F}$ over $X$
such that $t_{i}$ is the restriction to $p^{-1}(U)$ of $s_{i} g^{n}$, with $g = \theta(f)$ (by applying `(I, 1.4.1)` to
$p_{*}(\mathcal{F})$); since $g$ is invertible over $p^{-1}(U)$, we have

```text
  s|W = ∑_i b_i · (s_i|W)
```

with $b_{i} = a_{i} (g|W)^{-n}$, whence the claim. When $Y$ is affine, corollary (3.4.6) thus recovers (2.7.9).

We thus conclude that, when $Y$ is an arbitrary prescheme, the following three conditions on a quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$ such that $p_{*}(\mathcal{F})$ is

<!-- original page 61 -->

quasi-coherent are equivalent:

- a) _The canonical homomorphism $\sigma : p*(p_{*}(\mathcal{F})) \to \mathcal{F}$ is surjective._
- b) _There exists a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{G}$ and a surjective homomorphism
  $p*(\mathcal{G}) \to \mathcal{F}$._
- c) _For every affine open $U$ of $Y$, $\mathcal{F}|p^{-1}(U)$ is generated by its sections over $p^{-1}(U)$._

We have just shown the equivalence of a) and c). On the other hand, it is clear that a) implies b), $p_{*}(\mathcal{F})$
being quasi-coherent by hypothesis. Conversely, every homomorphism $u : p*(\mathcal{G}) \to \mathcal{F}$ factors as
$p*(\mathcal{G}) \to p*(p_{*}(\mathcal{F})) \xrightarrow{\sigma} \mathcal{F}$ `(0, 3.5.4.4)`, so if $u$ is surjective so
is $\sigma$, which shows that b) implies a).

**Corollary.**

<!-- label: II.3.4.8 -->

Suppose the hypotheses of (3.4.4) are satisfied, and further that $Y$ is a quasi-compact scheme or that the underlying
space of $Y$ is Noetherian. Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-module of finite type; then there
exists an integer $n_{0}$ such that for every $n \geq n_{0}$, $\mathcal{F}$ is isomorphic to a quotient of an
$\mathcal{O}_{X}$-module of the form $(p*(\mathcal{G}))(-n)$, where $\mathcal{G}$ is a quasi-coherent
$\mathcal{O}_{Y}$-module of finite type (depending on $n$).

**Proof.** Since the structure morphism $X \to Y$ is separated and of finite type, $p_{*}(\mathcal{F}(n))$ is
quasi-coherent (`(I, 9.2.2, b)`), hence the inductive limit of its quasi-coherent sub-$\mathcal{O}_{Y}$-modules of
finite type, by the hypothesis on $Y$ `(I, 9.4.9)`. We thus deduce from (3.4.6), `(0, 4.3.2)`, and `(0, 5.2.3)` that
$\mathcal{F}(n)$ is the canonical image of an $\mathcal{O}_{X}$-module of the form $p*(\mathcal{G})$, where
$\mathcal{G}$ is a quasi-coherent sub-$\mathcal{O}_{Y}$-module of $p_{*}(\mathcal{F}(n))$ of finite type; the corollary
follows from (3.2.5.2) and (3.2.7.1).

## 3.5. Functorial behaviour

**(3.5.1)**

<!-- label: II.3.5.1 -->

Let $Y$ be a prescheme, $\mathcal{S}$, $\mathcal{S}'$ two quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebras;
set $X = \operatorname{Proj}(\mathcal{S})$, $X' = \operatorname{Proj}(\mathcal{S}')$, and let $p$, $p'$ be the structure
morphisms of $X$ and $X'$ into $Y$. Let $\phi : \mathcal{S}' \to \mathcal{S}$ be an $\mathcal{O}_{Y}$-homomorphism of
graded algebras. For every affine open $U$ of $Y$, set $S_{U} = \Gamma(U, \mathcal{S})$, $S'_{U} = \Gamma(U,
\mathcal{S}')$; the homomorphism $\phi$ defines a homomorphism $\phi_{U} : S'_{U} \to S_{U}$ of graded `A_U`-algebras,
where $A_{U} = \Gamma(U, \mathcal{O}_{Y})$. There corresponds in $p^{-1}(U)$ an open subset $G(\phi_{U})$ and a morphism
$\Phi_{U} : G(\phi_{U}) \to p'^{-1}(U)$ (2.8.1). Furthermore, if $V \subset U$ is an affine open, the diagram

```text
              φ_U
   S'_U ───────────→ S_U                                                  (3.5.1.1)
     │                │
     ↓                ↓
   S'_V ───────────→ S_V
              φ_V
```

commutes, and one checks at once from the definitions (2.8.1) that

$$ G(\phi_{V}) = G(\phi_{U}) \cap p^{-1}(V) $$

and that $\Phi_{V}$ is the restriction of $\Phi_{U}$ to $G(\phi_{V})$. We have thus defined an open subset $G(\phi)$ of
$X$ such that $G(\phi) \cap p^{-1}(U) = G(\phi_{U})$ for every affine open $U \subset Y$, and an affine $Y$-morphism
$\Phi : G(\phi) \to X'$, which we say is

<!-- original page 62 -->

_associated_ to $\phi$ and which we denote by $\operatorname{Proj}(\phi)$. When, for every $y \in Y$, there is an affine
neighbourhood $U$ of $y$ such that the $\Gamma(U, \mathcal{O}_{Y})$-module $\Gamma(U, \mathcal{S}_{+})$ is generated by
$\phi(\Gamma(U, \mathcal{S}'_{+}))$, then $G(\phi_{U}) = p^{-1}(U)$, and so $G(\phi) = X$.

**Proposition.**

<!-- label: II.3.5.2 -->

1. If $\mathcal{M}$ is a quasi-coherent graded $\mathcal{S}$-module, there is a canonical functorial isomorphism from
   the $\mathcal{O}_{X'}$-module $\tilde{\mathcal{M}_{[\phi]}}$ to the $\mathcal{O}_{X'}$-module
   $\Phi_{*}(\tilde{\mathcal{M}}|G(\phi))$.
1. If $\mathcal{M}'$ is a quasi-coherent graded $\mathcal{S}'$-module, there is a canonical functorial homomorphism
   $\nu$ from the $(\mathcal{O}_{X}|G(\phi))$-module $\Phi*(\tilde{\mathcal{M}}')$ to the
   $(\mathcal{O}_{X}|G(\phi))$-module $\tilde{\mathcal{M}' \otimes_{\mathcal{S}'} \mathcal{S}}|G(\phi)$. If
   $\mathcal{S}'$ is generated by $\mathcal{S}'_{1}$, then $\nu$ is an isomorphism.

**Proof.** The homomorphisms considered have already been defined when $Y$ is affine ((2.8.7) and (2.8.8)); in the
general case, it suffices to check that they are compatible with restriction from an affine open of $Y$ to a smaller
one, which follows at once from the commutativity of (3.5.1.1).

In particular, for every $n \in \mathbb{Z}$, we have a canonical homomorphism

$$ \Phi*(\mathcal{O}_{X'}(n)) \to \mathcal{O}_{X}(n)|G(\phi). (3.5.2.1) $$

**Proposition.**

<!-- label: II.3.5.3 -->

Let $Y$, $Y'$ be two preschemes, $\psi : Y' \to Y$ a morphism, and $\mathcal{S}$ a quasi-coherent graded
$\mathcal{O}_{Y}$-algebra; set $\mathcal{S}' = \psi*(\mathcal{S})$. Then the $Y'$-scheme $X' =
\operatorname{Proj}(\mathcal{S}')$ is canonically identified with $\operatorname{Proj}(\mathcal{S}) \times_{Y} Y'$.
Furthermore, if $\mathcal{M}$ is a quasi-coherent graded $\mathcal{S}$-module, then the $\mathcal{O}_{X'}$-module
$\tilde{\psi*(\mathcal{M})}$ is identified with $\tilde{\mathcal{M}} \otimes_{Y} \mathcal{O}_{Y'}$.

**Proof.** First note that $\psi*(\mathcal{S})$ and $\psi*(\mathcal{M})$ are quasi-coherent $\mathcal{O}_{Y'}$-modules,
as are their homogeneous components `(0, 5.1.4)`. Let $U$ be an affine open of $Y$, $U' \subset \psi^{-1}(U)$ an affine
open of $Y'$, $A$, $A'$ the rings of $U$, $U'$; then $\mathcal{S}|U = \tilde{S}$, with $S$ a graded $A$-algebra, and
$\mathcal{S}'|U'$ is identified with $\tilde{S \otimes_{A} A'}$ `(I, 1.6.5)`; the first assertion then follows from
(2.8.10) and `(I, 3.2.6.2)`, since one verifies at once that the projection $\operatorname{Proj}(\mathcal{S}'|U') \to
\operatorname{Proj}(\mathcal{S}|U)$ defined by the above identification is compatible with restriction on $U$ and $U'$
and so defines a morphism $\operatorname{Proj}(\mathcal{S}') \to \operatorname{Proj}(\mathcal{S})$. Now let

```text
  q  : Proj(𝒮) → Y,    q' : Proj(𝒮') → Y'
```

be the structure morphisms; $q'^{-1}(U')$ is then identified with $q^{-1}(U) \times_{U} U'$, and the two sheaves
$\tilde{\psi*(\mathcal{M})}|q'^{-1}(U')$ and $(\tilde{\mathcal{M}} \otimes_{Y} \mathcal{O}_{Y'})|q'^{-1}(U')$ are then
both canonically identified with $\tilde{M \otimes_{A} A'}$, where $M = \Gamma(U, \mathcal{M})$, by (2.8.10) and
`(I, 1.6.5)`; whence the second assertion, the compatibility of the above identifications with restriction again being
immediate.

**Corollary.**

<!-- label: II.3.5.4 -->

With the notation of (3.5.3), $\mathcal{O}_{X'}(n)$ is canonically identified with $\mathcal{O}_{X}(n) \otimes_{Y}
\mathcal{O}_{Y'}$ for every $n \in \mathbb{Z}$ (with $X = \operatorname{Proj}(\mathcal{S})$).

**Proof.** Indeed, with the notation of (3.5.3), it is clear that $\psi*(\mathcal{S}(n)) = \mathcal{S}'(n)$ for every $n
\in \mathbb{Z}$.

**(3.5.5)**

<!-- label: II.3.5.5 -->

Keeping the previous notation, denote by $\Psi$ the canonical projection $X' \to X$, and set $\mathcal{M}' =
\psi*(\mathcal{M})$; we further suppose that $\mathcal{S}$ is generated by $\mathcal{S}_{1}$

<!-- original page 63 -->

and that $X$ is of finite type over $Y$; it then follows that $\mathcal{S}'$ is generated by $\mathcal{S}'_{1}$ (as one
sees by reducing to the case $Y$ and $Y'$ affine) and that $X'$ is of finite type over $Y'$ `(I, 6.3.4)`. Let
$\mathcal{F}$ be an $\mathcal{O}_{X}$-module and set $\mathcal{F}' = \Psi*(\mathcal{F})$; it then follows from (3.5.4)
and `(0, 4.3.3)` that $\mathcal{F}'(n) = \Psi*(\mathcal{F}(n))$ for every $n \in \mathbb{Z}$. We further define a
canonical $\Psi$-homomorphism $\theta_{n} : q_{*}(\mathcal{F}(n)) \to q'_{*}(\mathcal{F}'(n))$ as follows: in view of
the commutativity of the diagram

```text
                  Ψ
   X ←───────── X'
   │             │
 q │             │ q'
   ↓             ↓
   Y ←───────── Y'
                  ψ
```

it suffices to define a homomorphism $q_{*}(\mathcal{F}(n)) \to \psi_{*}(q'_{*}(\Psi*(\mathcal{F}(n)))) =
q_{*}(\Psi_{*}(\Psi*(\mathcal{F}(n))))$, and we take the homomorphism $\theta_{n} = q_{*}(\rho_{n})$, with $\rho_{n}$
the canonical homomorphism $\mathcal{F}(n) \to \Psi_{*}(\Psi*(\mathcal{F}(n)))$ `(0, 4.4.3)`. It is immediate that for
every affine open $U$ of $Y$ and every affine open $U'$ of $Y'$ with $U' \subset \psi^{-1}(U)$, the homomorphism
$\theta_{n}$ gives, on sections, the canonical homomorphism `(0, 3.7.2)` $\Gamma(q^{-1}(U), \mathcal{F}(n)) \to
\Gamma(q'^{-1}(U'), \mathcal{F}'(n))$.

The commutativity of (2.8.13.2) then shows that if $\mathcal{F}$ is quasi-coherent, the diagram

```text
                      ρ
              ℱ ─────────→ ℱ'
              ↑               ↑
       β_ℱ    │               │  β_ℱ'
              │               │
        (Γ_*(ℱ))̃ ─────→ (Γ_*(ℱ'))̃
                      θ̃
```

commutes (the top horizontal arrow being the canonical $\Psi$-morphism $\mathcal{F} \to \Psi*(\mathcal{F})$).

Similarly, the commutativity of (2.8.13.1) shows that the diagram

```text
                      θ
   Γ_*(ℳ̃) ─────────→ Γ_*(ℳ̃')
       ↑                 ↑
 α_ℳ   │                 │  α_ℳ'
       │                 │
       ℳ ─────────────→ ℳ'
                  ρ
```

commutes (the bottom horizontal arrow being the canonical $\psi$-morphism $\mathcal{M} \to \psi*(\mathcal{M})$).

**(3.5.6)**

<!-- label: II.3.5.6 -->

Now consider two preschemes $Y$, $Y'$, a morphism $g : Y' \to Y$, a quasi-coherent graded $\mathcal{O}_{Y}$-algebra
(resp. $\mathcal{O}_{Y'}$-algebra) $\mathcal{S}$ (resp. $\mathcal{S}'$), and a $g$-morphism of graded algebras $u :
\mathcal{S} \to \mathcal{S}'$ — that is, an $\mathcal{O}_{Y}$-homomorphism of graded algebras $\mathcal{S} \to
g_{*}(\mathcal{S}')$; we already know this is equivalent to giving an $\mathcal{O}_{Y'}$-homomorphism of graded algebras
$u\sharp : g*(\mathcal{S}) \to \mathcal{S}'$. From $u\sharp$ we canonically obtain a $Y'$-morphism $W =
\operatorname{Proj}(u\sharp) : G(u\sharp) \to \operatorname{Proj}(g*(\mathcal{S}))$, where $G(u\sharp)$ is an open
subset of $X' = \operatorname{Proj}(\mathcal{S}')$ (3.5.1). On the other hand, $X'' =
\operatorname{Proj}(g*(\mathcal{S}))$ is canonically

<!-- original page 64 -->

identified with $X \times_{Y} Y'$, with $X = \operatorname{Proj}(\mathcal{S})$ (3.5.3); composing the first projection
$p : X \times_{Y} Y' \to X$ with $\operatorname{Proj}(u\sharp)$, we obtain a morphism $v : G(u\sharp) \to X$, which we
denote by $\operatorname{Proj}(u)$, and such that the diagram

```text
              v
   G(u♯) ─────→ X
     │           │
     ↓           ↓
     Y' ─────→ Y
              g
```

commutes.

Furthermore, for every quasi-coherent graded $\mathcal{O}_{Y}$-module $\mathcal{M}$, we have a canonical $v$-morphism

```text
  ν : ℳ̃ → (g*(ℳ) ⊗_{g*(𝒮)} 𝒮')̃|G(u♯).                                   (3.5.6.1)
```

Indeed, $\nu\sharp$ is obtained by composing the homomorphisms

```text
  v*(ℳ̃) = w*(p*(ℳ̃)) → w*((g*(ℳ))̃) → (g*(ℳ) ⊗_{g*(𝒮)} 𝒮')̃|G(u♯)
```

where the first arrow comes from the isomorphism (3.5.3) and the second is the homomorphism (3.5.2, (i)); when
$\mathcal{S}$ is generated by $\mathcal{S}_{1}$, it follows from (3.5.2) that $\nu\sharp$ is an isomorphism.

As a particular case of (3.5.6.1), we have, for every $n \in \mathbb{Z}$, a canonical $v$-morphism

$$ \nu : \mathcal{O}_{X}(n) \to \mathcal{O}_{X'}(n)|G(u\sharp). (3.5.6.2) $$

## 3.6. Closed subpreschemes of a prescheme $\operatorname{Proj}(\mathcal{S})$

**(3.6.1)**

<!-- label: II.3.6.1 -->

Let $Y$ be a prescheme, $\phi : \mathcal{S} \to \mathcal{S}'$ a degree-`0` homomorphism of quasi-coherent graded
$\mathcal{O}_{Y}$-algebras. We say that $\phi$ is _(TN)-surjective_ (resp. _(TN)-injective_, _(TN)-bijective_) if there
exists $n$ such that, for every $k \geq n$, $\phi_{k} : \mathcal{S}_{k} \to \mathcal{S}'_{k}$ is surjective (resp.
injective, bijective). When this is the case, the study of the corresponding morphism $\Phi :
\operatorname{Proj}(\mathcal{S}') \to \operatorname{Proj}(\mathcal{S})$ reduces to the case where $\phi$ is surjective
(resp. injective, bijective). This is shown as in (2.9.1) (which is the particular case $Y$ affine) using (3.1.8).
Instead of saying that $\phi$ is (TN)-bijective, we also say that it is a _(TN)-isomorphism_.

**Proposition.**

<!-- label: II.3.6.2 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra, and $X =
\operatorname{Proj}(\mathcal{S})$.

1. If $\phi : \mathcal{S} \to \mathcal{S}'$ is a (TN)-surjective homomorphism of graded $\mathcal{O}_{Y}$-algebras, then
   the corresponding morphism $\Phi = \operatorname{Proj}(\phi)$ (3.5.1) is defined on all of
   $\operatorname{Proj}(\mathcal{S}')$ and is a closed immersion of $\operatorname{Proj}(\mathcal{S}')$ into $X$. If
   $\mathcal{J}$ is the kernel of $\phi$, then the closed subprescheme of $X$ associated to $\Phi$ is defined by the
   quasi-coherent sheaf of ideals $\tilde{\mathcal{J}}$ of $\mathcal{O}_{X}$.
1. Suppose further that $\mathcal{S}_{0} = \mathcal{O}_{Y}$, that $\mathcal{S}$ is generated by $\mathcal{S}_{1}$, and
   that $\mathcal{S}_{1}$ is of finite type. Let $X'$ be a closed subprescheme of $X = \operatorname{Proj}(\mathcal{S})$
   defined by a quasi-coherent sheaf of ideals $\mathcal{I}$ of $\mathcal{O}_{X}$. Let $\mathcal{J}$ be

<!-- original page 65 -->

```
the quasi-coherent graded sheaf of ideals of `𝒮` given by the inverse image of
`Γ_*(ℐ)` under the canonical homomorphism `α : 𝒮 → Γ_*(𝒪_X)` (3.3.2), and set
`𝒮' = 𝒮/𝒥`. Then `X'` is the subprescheme associated `(I, 4.2.1)` to the
closed immersion `Proj(𝒮') → X` corresponding to the canonical homomorphism
`𝒮 → 𝒮'` of graded `𝒪_Y`-algebras.
```

**Proof.**

(i) We may assume $\phi$ is surjective (3.6.1). Then, for every affine open $U$ of $Y$, $\Gamma(U, \mathcal{S}) \to
\Gamma(U, \mathcal{S}')$ is surjective `(I, 1.3.9)`, so (3.5.1) $G(\phi) = X$. We reduce immediately to proving the
proposition when $Y$ is affine, where it follows from (2.9.2, (i)).

(ii) We reduce to proving that the homomorphism $\tilde{\mathcal{J}} \to \mathcal{O}_{X}$ deduced from the canonical
injection $\mathcal{J} \to \mathcal{S}$ is an isomorphism from $\tilde{\mathcal{J}}$ onto $\mathcal{I}$; since the
question is local on $Y$, we may take $Y$ affine with ring $A$, so $\mathcal{S} = \tilde{S}$ with $S$ a graded
$A$-algebra generated by `S_1`, with `S_1` of finite type over $A$. It then suffices to apply (2.9.2, (ii)).

**Corollary.**

<!-- label: II.3.6.3 -->

Under the conditions of (3.6.2, (i)), suppose further that $\mathcal{S}$ is generated by $\mathcal{S}_{1}$. Then
$\Phi*(\mathcal{O}_{X}(n))$ is canonically identified with $\mathcal{O}_{X'}(n)$ for every $n \in \mathbb{Z}$.

**Proof.** We defined such a canonical isomorphism when $Y$ is affine (2.9.3); in the general case, it suffices to check
that the isomorphisms so defined for each affine open $U$ of $Y$ are compatible with passage from $U$ to an affine open
$U' \subset U$, which is immediate.

**Corollary.**

<!-- label: II.3.6.4 -->

Let $Y$ be a prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra generated by $\mathcal{S}_{1}$,
$\mathcal{E}$ a quasi-coherent $\mathcal{O}_{Y}$-module, $u$ a surjective $\mathcal{O}_{Y}$-homomorphism $\mathcal{E}
\to \mathcal{S}_{1}$, and $\bar{u} : \mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}) \to \mathcal{S}$ the homomorphism of
graded $\mathcal{O}_{Y}$-algebras extending $u$ (1.7.4). Then the morphism corresponding to `ū` is a closed immersion of
$\operatorname{Proj}(\mathcal{S})$ into $\operatorname{Proj}(\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))$.

**Proof.** Indeed, `ū` is surjective by hypothesis, and we apply (3.6.1, (i)).

## 3.7. Morphisms from a prescheme to a homogeneous spectrum

**(3.7.1)**

<!-- label: II.3.7.1 -->

Let $q : X \to Y$ be a morphism of preschemes, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module, and $\mathcal{S}$ a
quasi-coherent positively-graded $\mathcal{O}_{Y}$-algebra; then $q*(\mathcal{S})$ is a quasi-coherent positively-graded
$\mathcal{O}_{X}$-algebra. Consider the quasi-coherent graded $\mathcal{O}_{X}$-algebra $\mathcal{S}' = \oplus_{n \geq
0} \mathcal{L}^{\otimes n}$ and suppose given an $\mathcal{O}_{X}$-homomorphism of graded algebras

```text
  ψ : q*(𝒮) → 𝒮' = ⊕_{n ≥ 0} ℒ^{⊗ n}
```

which is equivalent to giving a $q$-morphism of graded algebras

$$ \psi\flat : \mathcal{S} \to q_{*}(\mathcal{S}'). $$

We know that $\operatorname{Proj}(\mathcal{S}')$ is canonically identified with $X$ ((3.1.7) and (3.1.8, (iii))); we
canonically obtain from $\psi$ an open subset $G(\psi)$ of $X$ and a $Y$-morphism

```text
  r_{ℒ, ψ} : G(ψ) → Proj(𝒮) = P                                          (3.7.1.1)
```

<!-- original page 66 -->

which we call the morphism _associated to_ $\mathcal{L}$ and $\psi$; recall (3.5.6) that this morphism is obtained by
composing the $Y$-morphism

```text
  τ = Proj(ψ) : G(ψ) → Proj(q*(𝒮))
```

with the first projection $\pi : \operatorname{Proj}(q*(\mathcal{S})) = P \times_{Y} X \to P$.

**(3.7.2)**

<!-- label: II.3.7.2 -->

We make $r = r_{\mathcal{L}, \psi}$ explicit when $Y = \operatorname{Spec}(A)$ is affine, so $\mathcal{S} = \tilde{S}$
with $S$ a positively-graded $A$-algebra. Suppose first that $X = \operatorname{Spec}(B)$ is also affine and that
$\mathcal{L} = \tilde{L}$, with $L$ a free $B$-module of rank `1`. Then $q*(\mathcal{S}) = \tilde{S \otimes_{A} B}$
`(I, 1.6.5)`; if $c$ is a generator of $L$, then $\psi_{n} : q*(\mathcal{S}_{n}) \to \mathcal{L}^{\otimes n}$
corresponds to a homomorphism $w_{n} : s \otimes b \mapsto b v_{n}(s) c^{\otimes n}$ from $S_{n} \otimes_{A} B$ to
$L^{\otimes n}$, where $v_{n} : S_{n} \to B$ is a homomorphism of $A$-modules, the $v_{n}$ forming a homomorphism of
algebras $S \to B$. Let $f \in S_{d}$ ($d > 0$) and set $g = v_{d}(f)$; we have $\pi^{-1}(D_{+}(f)) = D_{+}(f \otimes
1)$ by (2.8.10) and the identification of $D_{+}(f)$ with $\operatorname{Spec}(S_{(f)})$ (2.3.6); furthermore, by
formula (2.8.1.1) (in view of the canonical identification of $X$ with $\operatorname{Proj}(\mathcal{S}')$),

$$ \tau^{-1}(D_{+}(f \otimes 1)) = D(g) $$

whence

$$ r^{-1}(D_{+}(f)) = D(g). (3.7.2.1) $$

Moreover, the morphism $\tau = \operatorname{Proj}(\psi)$, restricted to $D(g)$, corresponds to the homomorphism that
sends $(s \otimes 1)/(f \otimes 1)^{n}$ (for $s \in S_{nd}$) to $v_{nd}(s)/g^{n}$ (2.8.1), and the projection $\pi$,
restricted to $D_{+}(f \otimes 1)$, corresponds to the homomorphism $s/f^{n} \mapsto (s \otimes 1)/(f \otimes 1)^{n}$;
we conclude that $r$, restricted to $D(g)$, corresponds to the homomorphism of $A$-algebras $\omega : S_{(f)} \to B_{g}$
such that $\omega(s/f^{n}) = v_{nd}(s)/g^{n}$ (for $s \in S_{nd}$, $n > 0$). Passing to the case where $X$ is arbitrary
(still with $Y$ affine), and taking (2.8.1) into account, we obtain:

**Proposition.**

<!-- label: II.3.7.3 -->

If $Y = \operatorname{Spec}(A)$ is affine and $\mathcal{S} = \tilde{S}$, with $S$ a graded $A$-algebra, then for every
$f \in S_{d} = \Gamma(Y, \mathcal{S}_{d})$,

```text
  r_{ℒ, ψ}⁻¹(D_+(f)) = X_{ψ♭(f)}     (where ψ♭(f) ∈ Γ(X, ℒ^{⊗ d}))       (3.7.3.1)
```

and the restriction $X_{\psi\flat(f)} \to D_{+}(f) = \operatorname{Spec}(S_{(f)})$ of $r_{\mathcal{L}, \psi}$
corresponds `(I, 2.2.4)` to the homomorphism of algebras

```text
  ψ♭_{(f)} : S_{(f)} → Γ(X_{ψ♭(f)}, 𝒪_X)                                 (3.7.3.2)
```

such that, for $s \in S_{nd} = \Gamma(Y, \mathcal{S}_{nd})$,

$$ \psi\flat_{(f)}(s/f^{n}) = (\psi\flat(s)|X_{\psi\flat(f)}) \cdot (\psi\flat(f)|X_{\psi\flat(f)})^{-n}. (3.7.3.3) $$

We say that $r_{\mathcal{L}, \psi}$ is _everywhere defined_ if $G(\psi) = X$. For this it is clearly necessary and
sufficient that $G(\psi) \cap q^{-1}(U) = q^{-1}(U)$ for every affine open $U \subset Y$; in other words, the question
is local on $Y$. If $Y$ is affine, $G(\psi)$ is the union of the $r^{-1}(D_{+}(f))$ for $f$ homogeneous in $S_{+}$
(2.8.1); by (3.7.3.1), the $X_{\psi\flat(f)}$ must therefore form a covering of $X$; in other words:

**Corollary.**

<!-- label: II.3.7.4 -->

Under the hypotheses of (3.7.3), for $r_{\mathcal{L}, \psi}$ to be everywhere defined it is necessary and sufficient
that, for every $x \in X$, there exist an integer $n > 0$ and a section $s$ of $\mathcal{S}_{n}$ over $Y$ such that,
setting $t = \psi\flat(s) \in \Gamma(X, \mathcal{L}^{\otimes n})$, we have $t(x) \neq 0$.

<!-- original page 67 -->

Note that this condition is always satisfied if $\psi$ is (TN)-surjective.

Similarly, whether $r_{\mathcal{L}, \psi}$ is dominant is a local question on $Y$, and we have:

**Corollary.**

<!-- label: II.3.7.5 -->

Under the hypotheses of (3.7.3), for $r_{\mathcal{L}, \psi}$ to be dominant it is necessary and sufficient that, for
every integer $n > 0$, every section $s \in S_{n}$ such that $\psi\flat(s) \in \Gamma(X, \mathcal{L}^{\otimes n})$ is
locally nilpotent be itself nilpotent.

**Proof.** We must express that $r^{-1}_{\mathcal{L}, \psi}(D_{+}(s))$ is non-empty only if $D_{+}(s)$ is non-empty, and
the corollary follows from (3.7.3.1) and (2.3.7).

**Proposition.**

<!-- label: II.3.7.6 -->

Let $q : X \to Y$ be a morphism, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module, $\mathcal{S}$, $\mathcal{S}'$ two
quasi-coherent graded $\mathcal{O}_{Y}$-algebras, $u : \mathcal{S}' \to \mathcal{S}$ a homomorphism of graded algebras,
$\psi : q*(\mathcal{S}) \to \oplus_{n \geq 0} \mathcal{L}^{\otimes n}$ a homomorphism of graded algebras, and $\psi' =
\psi \circ q*(u)$ the composite. If $r_{\mathcal{L}, \psi'}$ is everywhere defined, so is $r_{\mathcal{L}, \psi}$; if
$u$ is (TN)-surjective and $r_{\mathcal{L}, \psi'}$ is dominant, then so is $r_{\mathcal{L}, \psi}$; conversely, if $u$
is (TN)-injective and $r_{\mathcal{L}, \psi}$ is dominant, then $r_{\mathcal{L}, \psi'}$ is dominant.

**Proof.** We have $G(\psi') \subset G(\psi)$ (2.8.4), whence the first assertion; if $u$ is (TN)-surjective, then
`Proj(u) : Proj(𝒮) → Proj(𝒮')` is everywhere defined and is a closed immersion; since $r_{\mathcal{L}, \psi'}$ is the
composition of $\operatorname{Proj}(u)$ with the restriction of $r_{\mathcal{L}, \psi}$ to $G(\psi')$, we conclude that
if $r_{\mathcal{L}, \psi'}$ is dominant so is $r_{\mathcal{L}, \psi}$. Finally, if $u$ is (TN)-injective, we know that
$\operatorname{Proj}(u)$ is a dominant morphism from $G(u)$ to $\operatorname{Proj}(\mathcal{S}')$ (2.8.3); since
$G(\psi')$ is the inverse image of $G(u)$ under $r_{\mathcal{L}, \psi}$, we see that if $r_{\mathcal{L}, \psi}$ is
dominant so is $r_{\mathcal{L}, \psi'}$.

**Proposition.**

<!-- label: II.3.7.7 -->

Let $Y$ be a quasi-compact prescheme, $q : X \to Y$ a quasi-compact morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra given as the filtered
inductive limit of an inductive system $(\mathcal{S}^{\lambda})$ of quasi-coherent $\mathcal{O}_{Y}$-algebras. Let
$\phi_{\lambda} : \mathcal{S}^{\lambda} \to \mathcal{S}$ be the canonical homomorphism, $\psi : q*(\mathcal{S}) \to
\oplus_{n \geq 0} \mathcal{L}^{\otimes n}$ a homomorphism of graded algebras, and set $\psi_{\lambda} = \psi \circ
q*(\phi_{\lambda})$. For $r_{\mathcal{L}, \psi}$ to be everywhere defined it is necessary and sufficient that there
exist $\lambda$ such that $r_{\mathcal{L}, \psi_{\lambda}}$ is everywhere defined; $r_{\mathcal{L}, \psi_{\mu}}$ is then
everywhere defined for every $\mu \geq \lambda$.

**Proof.** The condition is sufficient by (3.7.6). Conversely, suppose $r_{\mathcal{L}, \psi}$ is everywhere defined; we
may reduce to $Y$ affine, since if for every affine open $U \subset Y$ there exists $\lambda(U)$ such that the
restriction of $r_{\mathcal{L}, \psi_{\lambda(U)}}$ to $q^{-1}(U)$ is everywhere defined, it suffices ($Y$ being
quasi-compact) to cover $Y$ by finitely many affine opens $U_{i}$ and to take $\lambda \geq \lambda(U_{i})$ for all $i$,
by (3.7.6). If $Y$ is affine, the hypothesis implies that, for every $x \in X$, there is a section $s^{(x)}$ of some
$S_{n}$ such that, setting $t^{(x)} = \psi\flat(s^{(x)})$, we have $t^{(x)}(x) \neq 0$ (with $t^{(x)}$ considered as a
section of $\mathcal{L}^{\otimes n}$ over $X$), which implies that $t^{(x)}(z) \neq 0$ for every $z$ in some
neighbourhood $V(x)$ of $x$. Cover $X$ by finitely many $V(x_{i})$ and let $s^{(i)}$ be the corresponding sections of
$S$; then there exists $\lambda$ such that all the $s^{(i)}$ are of the form $\phi_{\lambda}(s'^{(i)}_{\lambda})$, with
$s'^{(i)}_{\lambda} \in S^{\lambda}$ for every $i$; it then follows from (3.7.4) that $r_{\mathcal{L}, \psi_{\lambda}}$
is everywhere defined. The last assertion is a trivial consequence of (3.7.6).

**Corollary.**

<!-- label: II.3.7.8 -->

Under the hypotheses of (3.7.7), if the $r_{\mathcal{L}, \psi_{\lambda}}$ are dominant, so is $r_{\mathcal{L}, \psi}$;
the converse holds if the $\phi_{\lambda}$ are injective.

<!-- original page 68 -->

**Proof.** The second assertion is a particular case of (3.7.6); to show that $r_{\mathcal{L}, \psi}$ is dominant, we
may restrict to $Y$ affine; if $s \in S$ is such that $\psi\flat(s)$ is locally nilpotent, since we can write $s =
\phi_{\lambda}(s_{\lambda})$ for at least one $\lambda$, we conclude from the hypothesis and (3.7.5) that $s_{\lambda}$
is nilpotent, hence so is $s$, and the criterion of (3.7.5) applies.

**Remarks.**

<!-- label: II.3.7.9 -->

(i) With the notation of (3.7.1), and taking (3.2.10) into account, we have, for every $n \in \mathbb{Z}$, a canonical
homomorphism

```text
  θ : r_{ℒ, ψ}*(𝒪_P(n)) → ℒ^{⊗ n}                                        (3.7.9.1)
```

defined in general in (3.5.6.2). One sees at once that under the conditions of (3.7.3), the restriction of this
homomorphism to $X_{\psi\flat(f)}$ sends $s/f^{k}$ (with $s \in S_{n+kd}$) to the element
$(\psi\flat(s)|X_{\psi\flat(f)}) \cdot (\psi\flat(f)|X_{\psi\flat(f)})^{-k}$.

(ii) Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-module, and suppose $q$ is quasi-compact and separated, so
that for every $n \geq 0$, $q_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n})$ is a quasi-coherent
$\mathcal{O}_{Y}$-module `(I, 9.2.2)`. Let $\mathcal{M}' = \oplus_{n \geq 0} \mathcal{F} \otimes \mathcal{L}^{\otimes
n}$, which is a quasi-coherent graded $\mathcal{S}'$-module, and consider its image $\mathcal{M} = q_{*}(\mathcal{M}') =
\oplus_{n \geq 0} q_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n})$ (which is a quasi-coherent $\mathcal{S}$-module,
via the homomorphism $\psi\flat$). We are going to show the existence of a canonical homomorphism of
$\mathcal{O}_{X}$-modules

```text
  ξ : r_{ℒ, ψ}*(ℳ̃) → ℱ|G(ψ).                                            (3.7.9.2)
```

Indeed, we have already defined (3.5.6.1) a canonical homomorphism

```text
  r_{ℒ, ψ}*(ℳ̃) → (q*(ℳ) ⊗_{q*(𝒮)} 𝒮')̃|G(ψ)                              (3.7.9.3)
```

where the right-hand side is regarded as a quasi-coherent sheaf on $\operatorname{Proj}(\mathcal{S}')$. We also have a
canonical homomorphism

```text
  q*(q_*(ℳ')) ⊗_{q*(𝒮)} 𝒮' → ℳ'                                         (3.7.9.4)
```

for every quasi-coherent graded $\mathcal{S}'$-module $\mathcal{M}'$: for every open $U$ of $X$, every section $t'$ of
$q*(q_{*}(\mathcal{M}'_{h}))$ over $U$, and every section $b'$ of $\mathcal{S}'_{k}$ over $U$, we send $t' \otimes b'$
to the section $b' \sigma(t')$ of $\mathcal{M}'_{h+k}$, where $\sigma(t')$ is the section of $\mathcal{M}'_{h}$ over $U$
corresponding canonically `(0, 4.4.3)` to $t'$. We thus obtain a canonical homomorphism

```text
  (q*(q_*(ℳ')) ⊗_{q*(𝒮)} 𝒮')̃|G(ψ) → ℳ̃'|G(ψ)                             (3.7.9.5)
```

and since finally $\tilde{\mathcal{M}}'$ is canonically identified with $\mathcal{F}$ (3.2.9, (i)), we obtain the
desired canonical homomorphism.

Under the conditions of (3.7.3), the restriction of this homomorphism to $X_{\psi\flat(f)}$ is made explicit as follows:
given a section $t_{nd}$ of $\mathcal{F} \otimes \mathcal{L}^{\otimes nd}$ over $X$, if $t'_{nd}$ is $t_{nd}$ viewed as
a section of $q_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n})$ over $Y$, then $t'_{nd}/f^{n}$ is sent to the section
$(t_{nd}|X_{\psi\flat(f)}) \cdot (\psi\flat(f)|X_{\psi\flat(f)})^{-n}$ of $\mathcal{F}$ over $X_{\psi\flat(f)}$.

## 3.8. Criteria for immersion into a homogeneous spectrum

<!-- original page 69 -->

**(3.8.1)**

<!-- label: II.3.8.1 -->

With the notation of (3.7.1), whether $r_{\mathcal{L}, \psi}$ is an immersion (resp. an open immersion, a closed
immersion) is clearly _local on $Y$_.

**Proposition.**

<!-- label: II.3.8.2 -->

Under the hypotheses of (3.7.3), for $r_{\mathcal{L}, \psi}$ to be everywhere defined and an immersion, it is necessary
and sufficient that there exist a family of sections $s_{\alpha} \in S_{n_{\alpha}}$ (with $n_{\alpha} > 0$) such that,
setting $f_{\alpha} = \psi\flat(s_{\alpha})$, the following conditions are satisfied:

1. The $X_{f_{\alpha}}$ form a covering of $X$.
1. The $X_{f_{\alpha}}$ are affine opens.
1. For every $\alpha$ and every $t \in \Gamma(X_{f_{\alpha}}, \mathcal{O}_{X})$, there exist an integer $m > 0$ and an
   $s \in S_{m n_{\alpha}}$ such that $t = (\psi\flat(s)|X_{f_{\alpha}}) \cdot (f_{\alpha}|X_{f_{\alpha}})^{-m}$.

For $r_{\mathcal{L}, \psi}$ to be everywhere defined and an open immersion, it is necessary and sufficient that there
exist a family $(s_{\alpha})$ satisfying (i), (ii), (iii) and:

- (iv) For every $n > 0$ and every $s \in S_{n n_{\alpha}}$ such that $\psi\flat(s)|X_{f_{\alpha}} = 0$, there exists an
  integer $k > 0$ such that $s^{k}_{\alpha} s = 0$.

For $r_{\mathcal{L}, \psi}$ to be everywhere defined and a closed immersion, it is necessary and sufficient that there
exist a family $(s_{\alpha})$ satisfying (i), (ii), (iii) and:

- (v) The $D_{+}(s_{\alpha})$ form a covering of $P = \operatorname{Proj}(\mathcal{S})$.

**Proof.** For $r$ to be an immersion (resp. a closed immersion), it is necessary and sufficient that there exist a
covering of $r(G(\psi))$ (resp. of $P$) by the $D_{+}(s_{\alpha})$ such that, setting $V_{\alpha} =
r^{-1}(D_{+}(s_{\alpha}))$, the restriction of $r$ to $V_{\alpha}$ is a closed immersion of $V_{\alpha}$ into
$D_{+}(s_{\alpha})$ `(I, 4.2.4)`. Condition (i) expresses both that $r$ is everywhere defined and that the
$D_{+}(s_{\alpha})$ cover $r(X)$, by (3.7.3.1); since $D_{+}(s_{\alpha})$ is affine, conditions (ii) and (iii) express
that the restriction of $r$ to $X_{f_{\alpha}}$ is a closed immersion into $D_{+}(s_{\alpha})$, by `(I, 4.2.3)`;
finally, since (iii) and (iv) express that $\psi\flat_{(s_{\alpha})}$ is bijective (notation of (3.7.3.2)), conditions
(ii), (iii), and (iv) express that the restriction of $r$ to $X_{f_{\alpha}}$ is an isomorphism onto $D_{+}(s_{\alpha})$
for every $\alpha$, so (i), (ii), (iii), and (iv) together express that $r$ is an open immersion.

**Corollary.**

<!-- label: II.3.8.3 -->

Under the hypotheses of (3.7.6), if $r_{\mathcal{L}, \psi'}$ is everywhere defined and an immersion, so is
$r_{\mathcal{L}, \psi}$. If we further suppose $u$ is (TN)-surjective, then if $r_{\mathcal{L}, \psi'}$ is an open
(resp. closed) immersion, so is $r_{\mathcal{L}, \psi}$.

**Proof.** By (3.8.2), there is a family $s'_{\alpha} \in S'_{n_{\alpha}}$ such that, setting $f_{\alpha} =
\psi'\flat(s'_{\alpha})$, conditions (i), (ii), (iii) are satisfied. Setting $s_{\alpha} = u(s'_{\alpha})$, we also have
$f_{\alpha} = \psi\flat(s_{\alpha})$, and if $t = (\psi'\flat(s')|X_{f_{\alpha}}) \cdot
(f_{\alpha}|X_{f_{\alpha}})^{-m}$, then also $t = (\psi\flat(s)|X_{f_{\alpha}}) \cdot (f_{\alpha}|X_{f_{\alpha}})^{-m}$
on setting $s = u(s')$, whence the first assertion. The second follows at once from the fact that
$\operatorname{Proj}(u)$ is a closed immersion.

**Proposition.**

<!-- label: II.3.8.4 -->

Suppose the hypotheses of (3.7.7) are satisfied and, in addition, that $q : X \to Y$ is a morphism of finite type. Then,
for $r_{\mathcal{L}, \psi}$ to be everywhere defined and an immersion, it is necessary and sufficient that there exist
$\lambda$ such that $r_{\mathcal{L}, \psi_{\lambda}}$ is everywhere defined and an immersion; in this case
$r_{\mathcal{L}, \psi_{\mu}}$ is everywhere defined and an immersion for every $\mu \geq \lambda$.

<!-- original page 70 -->

**Proof.** In view of (3.8.3), it suffices to show that if $r_{\mathcal{L}, \psi}$ is everywhere defined and an
immersion, then so is $r_{\mathcal{L}, \psi_{\lambda}}$ for at least one $\lambda$. By the same argument as in (3.7.7),
using the quasi-compactness of $Y$, we first reduce to $Y$ affine. Since $X$ is quasi-compact, (3.8.2) shows the
existence of a finite family $(s_{i})$ of elements of $S$ ($s_{i} \in S_{n_{i}}$) satisfying (i), (ii), (iii). The
morphism $X_{f_{i}} \to Y$ (where $f_{i} = \psi\flat(s_{i})$) is of finite type: indeed, it is a morphism of affine
schemes, so it is quasi-compact `(I, 6.6.1)`, and locally of finite type since $q$ is of finite type `(I, 6.3.2)`, and
the conclusion follows from `(I, 6.6.3)`. The ring $B_{i}$ of $X_{f_{i}}$ is therefore an $A$-algebra of finite type
`(I, 6.3.3)`; let $(t_{ij})$ be a family of generators of this algebra. By hypothesis, there are elements $s'_{ij} \in
S_{m_{ij} n_{i}}$ such that

$$ t_{ij} = (\psi\flat(s'_{ij})|X_{f_{i}}) \cdot (\psi\flat(s_{i})|X_{f_{i}})^{-m_{ij}}. $$

Also by hypothesis, there exist $\lambda$ and elements $s_{i\lambda} \in S^{\lambda}_{n_{i}}$, $s'_{ij\lambda} \in
S^{\lambda}_{m_{ij} n_{i}}$ whose images under $\phi_{\lambda}$ are $s_{i}$ and $s'_{ij}$ respectively; it is clear that
$r_{\mathcal{L}, \psi_{\lambda}}$ satisfies conditions (i), (ii), and (iii) of (3.8.2).

**Proposition.**

<!-- label: II.3.8.5 -->

Let $Y$ be a quasi-compact scheme, or a prescheme whose underlying space is Noetherian, $q : X \to Y$ a morphism _of
finite type_, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module, $\mathcal{S}$ a quasi-coherent graded
$\mathcal{O}_{Y}$-algebra, and $\psi : q*(\mathcal{S}) \to \oplus_{n \geq 0} \mathcal{L}^{\otimes n}$ a homomorphism of
graded algebras. For $r_{\mathcal{L}, \psi}$ to be everywhere defined and an immersion, it is necessary and sufficient
that there exist an integer $n > 0$ and a quasi-coherent sub-$\mathcal{O}_{Y}$-module of finite type $\mathcal{E}$ of
$\mathcal{S}_{n}$ such that

- a) the homomorphism $\psi_{n} \circ q*(j_{n}) : q*(\mathcal{E}) \to \mathcal{L}^{\otimes n}$ (where $j_{n} :
  \mathcal{E} \to \mathcal{S}$ is the canonical injection) is surjective;
- b) if $\mathcal{S}'$ denotes the (graded) sub-$\mathcal{O}_{Y}$-algebra of $\mathcal{S}$ generated by $\mathcal{E}$,
  and $\psi'$ the homomorphism $\psi \circ q*(j')$ (with $j'$ the injection of $\mathcal{S}'$ into $\mathcal{S}$), then
  $r_{\mathcal{L}, \psi'}$ is everywhere defined and an immersion.

When this is the case, every quasi-coherent sub-$\mathcal{O}_{Y}$-module $\mathcal{E}'$ of $\mathcal{S}_{n}$ containing
$\mathcal{E}$ has the same property, as does the image of $\otimes^{k} \mathcal{E}$ in $\mathcal{S}_{kn}$ for every $k >
0$.

**Proof.** The sufficiency of the condition and the last two assertions are particular cases of (3.8.3), in view of the
canonical isomorphism between $\operatorname{Proj}(\mathcal{S})$ and $\operatorname{Proj}(\mathcal{S}^{(k)})$ (3.1.8).

Let $(U_{i})$ be a finite cover of $Y$ by affine opens and set $A_{i} = A(U_{i})$. Since $q^{-1}(U_{i})$ is
quasi-compact, the hypothesis that $r_{\mathcal{L}, \psi}$ be everywhere defined and an immersion implies, together with
(3.8.2), the existence of a finite family $(s_{ij} \in S^{(i)}_{n_{ij}})$ of elements of $S^{(i)} = \Gamma(U_{i},
\mathcal{S})$ satisfying (i), (ii), (iii). As in the proof of (3.8.4), one sees that the morphism $X_{f_{ij}} \to U_{i}$
(where $f_{ij} = \psi\flat(s_{ij})$) is of finite type, and so the ring $B_{ij}$ of $X_{f_{ij}}$ is an $A_{i}$-algebra
of finite type, with a system of generators of the form $(\psi\flat(t_{ijk})|X_{f_{ij}}) \cdot
(f_{ij}|X_{f_{ij}})^{-m_{ijk}}$, where $t_{ijk} \in S^{(i)}_{m_{ijk} n_{ij}}$. Let $n$ be a common multiple of the
$m_{ijk} n_{ij}$; replacing (for each $(i, j, k)$) $s_{ij}$ by a power $s^{\rho}_{ij}$ such that $\rho m_{ijk} n_{ij} =
n$, and multiplying $t_{ijk}$ by $s^{\rho - m_{ijk}}_{ij}$, we may assume that for each $i$ all the $s_{ij}$ and
$t_{ijk}$ belong to $S^{(i)}_{n}$ and that $m_{ijk} = 1$. Let $E_{i}$ be the sub-$A_{i}$-module of $S^{(i)}_{n}$
generated by these elements (for fixed $i$). There exists a coherent sub-$\mathcal{O}_{Y}$-module of finite type
$\mathcal{E}_{i}$ of $\mathcal{S}_{n}$ such that $\mathcal{E}_{i}|U_{i} = \tilde{E_{i}}$ `(I, 9.4.7)`.

<!-- original page 71 -->

It is clear that the sub-$\mathcal{O}_{Y}$-module $\mathcal{E}$ of $\mathcal{S}_{n}$ given by the sum of the
$\mathcal{E}_{i}$ solves the problem (each section $f_{ij}$ is such that, for every $x \in X_{f_{ij}}$, there is an
affine neighbourhood $V \subset X_{f_{ij}}$ of $x$ such that $f|V$ is a basis for $\Gamma(V, \mathcal{L}^{\otimes n})$).
