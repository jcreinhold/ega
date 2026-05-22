# §2. Cohomological study of projective morphisms

<!-- original page 95 -->

## 2.1. Explicit calculations of certain cohomology groups

**2.1.1.**

<!-- label: III.2.1.1 -->

Let $X$ be a prescheme and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module; consider the graded ring $(0_{I},
5.4.6)$

```text
  S = Γ_*(X, ℒ) = ⊕_{n ∈ ℤ} Γ(X, ℒ^{⊗n}).                                    (2.1.1.1)
```

Let $(f_{i})_{1 \leq i \leq r}$ be a finite family of homogeneous elements of $S$, with $f_{i} \in S_{d_{i}}$; set

```text
  U_i = X_{f_i},   U = ⋃_i U_i,
```

and denote by $\mathfrak{U}$ the cover $(U_{i})$ of $U$. For every quasi-coherent $\mathcal{O}_{X}$-module
$\mathcal{F}$, set

```text
  H^•(𝔘, ℱ(*)) = ⊕_{n ∈ ℤ} H^•(𝔘, ℱ ⊗ ℒ^{⊗n})                                (2.1.1.2)
```

```text
  H^•(U, ℱ(*)) = ⊕_{n ∈ ℤ} H^•(U, ℱ ⊗ ℒ^{⊗n}).                               (2.1.1.3)
```

The abelian groups `(2.1.1.2)` and `(2.1.1.3)` are *bigraded*, by setting

```text
  (H^•(𝔘, ℱ(*)))^{m,n} = H^m(𝔘, ℱ ⊗ ℒ^{⊗n})
```

and an analogous definition for `(2.1.1.3)`. For the second degree, it is clear that these groups are graded
$S$-modules, as follows for instance from the fact that $\mathcal{F} \mapsto H^{p}(\mathfrak{U}, \mathcal{F})$ and
$\mathcal{F} \mapsto H^{p}(U, \mathcal{F})$ are functors.

**2.1.2.**

<!-- label: III.2.1.2 -->

Consider now the graded $S$-module $(0_{I}, 5.4.6)$

```text
  M = Γ_*(ℱ) = H^0(X, ℱ(*)) = ⊕_{n ∈ ℤ} Γ(X, ℱ ⊗ ℒ^{⊗n}).                    (2.1.2.1)
```

<!-- original page 96 -->

If $X$ is a prescheme whose underlying space is Noetherian, or a quasi-compact scheme, it follows from `(I, 9.3.1)`
that, setting as usual $U_{i_{0} \cdots i_{p}} = \bigcap^{p}_{k=0} U_{i_{k}}$, we have, up to a canonical isomorphism,

```text
  Γ(U_{i_0 … i_p}, ℱ(*)) = H^0(U_{i_0 … i_p}, ℱ(*)) = M_{f_{i_0} … f_{i_p}}.
```

One can also, with the notation of `(1.2.2)`, identify $M_{f_{i_{0}} \cdots f_{i_{p}}}$ with $\varinjlim M^{(n)}_{i_{0}
\cdots i_{p}}$. This identification is an isomorphism of graded $S$-modules, provided that one defines the degree of a
homogeneous element $\xi \in \varinjlim M^{(n)}_{i_{0} \cdots i_{p}}$ as follows: $\xi$ is the canonical image of a
homogeneous element $x \in M^{(n)}_{i_{0} \cdots i_{p}} = M$ of degree $m$; one then takes for the degree of $\xi$ the
number $m - n (d_{i_{0}} + d_{i_{1}} + \cdots + d_{i_{p}})$. Taking the definition of the homomorphisms $\phi_{nm} :
M^{(n)}_{i_{0} \cdots i_{p}} \to M^{(m)}_{i_{0} \cdots i_{p}}$ `(1.2.2)` into account, one sees at once that this
definition does not depend on the "representative" $x$ of $\xi$ chosen. Denoting, as in `(1.2.2)`, by $C^{p}_{a}(M)$ the
set of alternating maps from $[1, r]^{p+1}$ to $M$ (for every $n$), one defines in the same way as above a structure of
graded $S$-module on $\varinjlim C^{p}_{a}(M)$; one has again as in `(1.2.2)`

```text
  C^p(𝔘, ℱ(*)) = lim_→ C^p_a(M),                                              (2.1.2.2)
```

the isomorphism of the two sides preserving degrees. One then has, as in `(1.2.2)`,

```text
  C'^p(𝔘, ℱ(*)) = C^{p+1}_a(𝐟, M) = lim_→ K^{p+1}(𝐟^n, M),                    (2.1.2.3)
```

the isomorphism preserving degrees: the degree of an element of $\varinjlim K^{p+1}(\mathbf{f}^{n}, M)$, the canonical
image of a cochain $\zeta \in K^{p+1}(\mathbf{f}^{n}, M)$ whose values $\zeta(i_{0}, \cdots, i_{p})$ lie in a single
homogeneous component $M_{m}$ of $M$, is $m - n(d_{i_{0}} + \cdots + d_{i_{p}})$, and is independent of the choice of
this cochain as a representative of the element considered.

Since the preceding isomorphisms are compatible with the coboundary operators, we conclude, as in `(1.2.2)`, the
following.

**Proposition (2.1.3).**

<!-- label: III.2.1.3 -->

*Let $X$ be a prescheme whose underlying space is Noetherian, or a quasi-compact scheme. There exists a canonical
isomorphism, functorial in $\mathcal{F}$,*

```text
  H^p(𝔘, ℱ(*)) ⥲ H^{p+1}(𝐟, M)                              for every p ≥ 1.   (2.1.3.1)
```

*Moreover, one has an exact sequence functorial in $\mathcal{F}$*

```text
  0 → H^0(𝐟, M) → M → H^0(𝔘, ℱ(*)) → H^1(𝐟, M) → 0.                          (2.1.3.2)
```

*Furthermore, all the homomorphisms introduced are of degree `0` for the graded $S$-module structures ($S$ being the
ring `(2.1.1.1)`).*

<!-- original page 97 -->

**Corollary (2.1.4).**

<!-- label: III.2.1.4 -->

*If $X$ is a quasi-compact scheme and the $U_{i} = X_{f_{i}}$ are affine, there exists a canonical isomorphism,
functorial in $\mathcal{F}$, of degree `0`,*

```text
  H^p(U, ℱ(*)) ⥲ H^{p+1}(𝐟, M)                              for p ≥ 1         (2.1.4.1)
```

*and an exact sequence functorial in $\mathcal{F}$*

```text
  0 → H^0(𝐟, M) → M → H^0(U, ℱ(*)) → H^1(𝐟, M) → 0                           (2.1.4.2)
```

*where all homomorphisms are of degree `0`.*

**Proof.** It suffices to apply `(1.4.1)` to the result of `(2.1.3)`.

The "local" proposition analogous to `(2.1.3)` is the following.

**Proposition (2.1.5).**

<!-- label: III.2.1.5 -->

*Let $S$ be a graded ring with positive degrees, $f_{i} (1 \leq i \leq r)$ a homogeneous element of $S_{+}$ of degree
$d_{i}$, $M$ a graded $S$-module. Let $X = \operatorname{Proj}(S)$ be the homogeneous prime spectrum of $S$ and set
$U_{i} = D_{+}(f_{i})$, $U = \bigcup U_{i}$, $H^{\bullet}(U, \tilde{M}(*)) = \oplus_{n} H^{\bullet}(U, (M(n))\sim)$.
There then exist canonical isomorphisms functorial in $M$, of degree `0` for the graded $S$-module structures,*

```text
  H^p(U, M̃(*)) ⥲ H^{p+1}(𝐟, M)                             for p ≥ 1         (2.1.5.1)
```

*and an exact sequence functorial in $M$*

```text
  0 → H^0(𝐟, M) → M → H^0(U, M̃(*)) → H^1(𝐟, M) → 0                          (2.1.5.2)
```

*where all homomorphisms are of degree `0`.*

**Proof.** We have $\Gamma(U_{i_{0} \cdots i_{p}}, (M(n))\sim) = (M_{f_{i_{0}} \cdots f_{i_{p}}})_{n}$ by definition
`(II, 2.5.2)`, hence $\Gamma(U_{i_{0} \cdots i_{p}}, \tilde{M}(*)) = M_{f_{i_{0}} \cdots f_{i_{p}}}$. The rest of the
argument is then the same as for the proof of `(2.1.4)`, taking into account that $X$ is a scheme.

**Remarks (2.1.6).**

<!-- label: III.2.1.6 -->

(i) Under the conditions of `(2.1.5)`, the functors $M \mapsto M_{f_{i_{0}} \cdots f_{i_{p}}}$ are exact in $M$, by
virtue of $(0_{I}, 1.3.2)$; the same reasoning as in `(1.2.5)` then shows that if $0 \to M' \to M \to M'' \to 0$ is an
exact sequence of graded $S$-modules (where the homomorphisms are of degree `0`), one has commutative diagrams for every
$p \geq 0$

```text
  H^p(U, M̃''(*))    →    H^{p+1}(U, M̃'(*))

      ↓                          ↓

  H^{p+1}(𝐟, M'')   →    H^{p+2}(𝐟, M')                                      (2.1.6.1)
```

(ii) Proposition `(2.1.5)` will be especially interesting when $S$ is an $A$-algebra generated by a finite number of
elements of degree `1`, $A$ being assumed Noetherian; for

<!-- original page 98 -->

then, every quasi-coherent $\mathcal{O}_{X}$-module is of the form $\tilde{M}$ `(II, 2.7.7)`.

**2.1.7.**

<!-- label: III.2.1.7 -->

We are going to apply `(2.1.5)` in the case $S = A[T_{0}, \cdots, T_{r}]$, where $A$ is an arbitrary ring, the $T_{i}$
are indeterminates, with $M = S$ and $f_{i} = T_{i}$. One is therefore essentially reduced to computing
$H^{\bullet}(\mathbf{T}, S)$, where $\mathbf{T} = (T_{i})_{0 \leq i \leq r}$.

**Lemma (2.1.8).**

<!-- label: III.2.1.8 -->

*If $S = A[T_{0}, \cdots, T_{r}]$, one has, with $\mathbf{T} = (T_{i})_{0 \leq i \leq r}$,*

```text
  H^i(𝐓^n, S) = 0                                          if i ≠ r + 1      (2.1.8.1)
```

$$ H^{r+1}(\mathbf{T}^{n}, S) = S/(\mathbf{T}^{n}). (2.1.8.2) $$

*The $A$-module $H^{r+1}(\mathbf{T}^{n}, S)$ thus has a basis over $A$ formed of the classes mod. $(\mathbf{T}^{n})$ of
the monomials $\mathbf{T}^{\mathbf{p}} = T^{p_{0}}_{0} \cdots T^{p_{r}}_{r}$ with $\mathbf{p} = (p_{0}, \cdots, p_{r})$,
$0 \leq p_{i} < n$ for all $i$.*

**Proof.** This is an immediate consequence of `(1.1.3.5)` and Proposition `(1.1.4)`, whose hypotheses are trivially
verified.

**2.1.9.**

<!-- label: III.2.1.9 -->

Pass to the inductive limit on $n$; the relations `(2.1.8.1)` give $H^{i}(\mathbf{T}, S) = 0$ for $i \neq r + 1$. For $i
= r + 1$, the inductive system is formed of the $S/(\mathbf{T}^{n})$, the homomorphism $\phi_{nm} : S/(\mathbf{T}^{n})
\to S/(\mathbf{T}^{m})$ for $0 \leq n \leq m$ being multiplication by $(T_{0} \cdots T_{r})^{m-n}$. For $n \geq
\sup(p_{i})_{0 \leq i \leq r}$, denote by $\xi^{(n)}_{p_{0}, \cdots, p_{r}}$ the class of $T^{n-p_{0}}_{0} \cdots
T^{n-p_{r}}_{r}$ mod. $(\mathbf{T}^{n})$; one then has $\phi_{nm}(\xi^{(n)}_{\mathbf{p}}) = \xi^{(m)}_{\mathbf{p}}$, and
these elements thus have the same canonical image $\xi_{\mathbf{p}} = \xi_{p_{0}, \cdots, p_{r}}$ in the inductive limit
$H^{r+1}(\mathbf{T}, S)$; by virtue of the definition of degree given in `(2.1.2)`, the degree of $\xi_{\mathbf{p}}$ is
therefore equal to $-|\mathbf{p}| = -(p_{0} + p_{1} + \cdots + p_{r})$. It is clear that the $\xi^{(n)}_{\mathbf{p}}$
for $0 < p_{i} \leq n$ and $0 \leq i \leq r$ form a basis of $S/(\mathbf{T}^{n})$. One immediately deduces from
`(2.1.8)`:

**Corollary (2.1.10).**

<!-- label: III.2.1.10 -->

*With the notation of `(2.1.8)`, one has*

```text
  H^i(𝐓, S) = 0                                            for i ≠ r + 1     (2.1.10.1)
```

*and $H^{r+1}(\mathbf{T}, S)$ is a free $A$-module with a basis formed of the elements $\xi_{p_{0}, \cdots, p_{r}}$ such
that $p_{i} > 0$ for $0 \leq i \leq r$.*

**Remark (2.1.11).**

<!-- label: III.2.1.11 -->

Let $N$ be an arbitrary $A$-module and set $M = S \otimes_{A} N$; the reasoning of `(2.1.8)` shows that one has more
generally

```text
  H^i(𝐓^n, M) = 0                                          if i ≠ r + 1      (2.1.11.1)
```

```text
  H^{r+1}(𝐓^n, M) = (S/(𝐓^n)) ⊗_A N,                                         (2.1.11.2)
```

since the latter formula follows directly from `(1.1.3.5)`, and on the other hand it is clear that $M / (T^{n}_{0} M +
\cdots + T^{n}_{r-1} M)$ is identified with the tensor product $(S/(T^{n}_{0} S + \cdots + T^{n}_{r-1} S)) \otimes_{A}
N$, the ideal $T^{n}_{0} S + \cdots + T^{n}_{r-1} S$ being a direct factor in the $A$-module $S$; this allows one to
apply `(1.1.4)` to $M$, and one thus obtains `(2.1.11.1)`.

Combining `(2.1.10)` and `(2.1.5)`, one obtains:

**Proposition (2.1.12).**

<!-- label: III.2.1.12 -->

*Let $A$ be a ring, $r$ an integer `> 0`, and $X = \mathbb{P}^{r}_{A}$ `(II, 4.1.1)`. Then:*

*(i) One has $H^{i}(X, \mathcal{O}_{X}(*)) = 0$ for $i \neq 0, r$.*

*(ii) The canonical homomorphism $\alpha : S \to H^{0}(X, \mathcal{O}_{X}(*))$ `(II, 2.6.2)` is bijective.*

<!-- original page 99 -->

*(iii) $H^{r}(X, \mathcal{O}_{X}(*))$ is a free $A$-module having a basis formed of elements
$\xi_{p_{0}, \cdots, p_{r}}$, where $p_{i} > 0$ for $0 \leq i \leq r$, $\xi_{p_{0}, \cdots, p_{r}}$ being of degree
$-|\mathbf{p}| = -(p_{0} + \cdots + p_{r})$, and the product $T_{i} \cdot \xi_{p_{0}, \cdots, p_{r}}$ being equal to
$\xi_{p_{0}, \cdots, p_{i} - 1, \cdots, p_{r}}$.*

**Proof.** Note that, in the exact sequence `(2.1.5.2)` applied to $M = S = A[T_{0}, \cdots, T_{r}]$, one has
$H^{0}(\mathbf{T}, S) = 0$ and $H^{1}(\mathbf{T}, S) = 0$ by `(2.1.10.1)`, and that Proposition `(2.1.5)` applies to $U
= X$, since $X$ is the union of the $D_{+}(T_{i})$ `(II, 2.3.14)`. It remains to identify the map $S \to H^{0}(X,
\mathcal{O}_{X}(*))$ of the exact sequence `(2.1.5.1)` with the canonical map $\alpha$; but this follows from the
canonical identification of $H^{0}(U, \mathcal{O}_{X}(*))$ and $H^{0}(\mathfrak{U}, \mathcal{O}_{X}(*))$.

**Corollary (2.1.13).**

<!-- label: III.2.1.13 -->

*The only values of $(i, n)$ for which one can have $H^{i}(X, \mathcal{O}_{X}(n)) \neq 0$ are the following: $i = 0$ and
$n \geq 0$; $i = r$ and $n \leq -(r + 1)$.*

Note that if $A \neq 0$, one effectively has $H^{i}(X, \mathcal{O}_{X}(n)) \neq 0$ for the pairs enumerated in
`(2.1.13)`; this follows from `(2.1.12)`, since $S_{n}$ is then $\neq 0$ for all degrees $n \geq 0$.

In the applications which will be made in this chapter, we shall mostly use the less precise result:

**Corollary (2.1.14).**

<!-- label: III.2.1.14 -->

*The $A$-modules $H^{i}(X, \mathcal{O}_{X}(n))$ are free of finite type; if $i > 0$, they are zero for $n > 0$.*

**Proposition (2.1.15).**

<!-- label: III.2.1.15 -->

*Let $Y$ be a prescheme, $\mathcal{E}$ an $\mathcal{O}_{Y}$-module locally free of rank $r + 1$, $X =
\mathbb{P}(\mathcal{E})$ the projective bundle defined by $\mathcal{E}$, $f : X \to Y$ the structure morphism. The only
values of $i$ and $n$ for which $R^{i} f_{*}(\mathcal{O}_{X}(n)) \neq 0$ are $i = 0$ and $n \geq 0$, $i = r$ and $n \leq
-(r + 1)$; in addition, the canonical homomorphism `(II, 3.3.2)`*

```text
  α : 𝐒_{𝒪_Y}(ℰ) → 𝚪_*(𝒪_X) = R^0 f_*(𝒪_X(*)) = ⊕_{n ∈ ℤ} f_*(𝒪_X(n))
```

*is an isomorphism.*

**Proof.** The question being local on $Y$, we may suppose $Y$ affine with ring $A$ and $\mathcal{E} = \tilde{E}$, where
$E = A^{r+1}$; one is then immediately reduced to `(2.1.12)`, taking `(1.4.11)` into account.

**Remark (2.1.16).**

<!-- label: III.2.1.16 -->

We shall later complete the results of `(2.1.15)` by proving the following propositions: set $\omega =
f^{*}(\bigwedge^{r+1} \mathcal{E})(-r-1)$, which is an invertible $\mathcal{O}_{X}$-module. Then:

(i) One has a canonical isomorphism

```text
  ρ : R^r f_*(ω) ⥲ 𝒪_Y.                                                      (2.1.16.1)
```

(ii) The cup-product pairing `(0, 12.2.2)`

```text
  R^r f_*(𝒪_X(n)) × R^0 f_*(ω(−n)) → R^r f_*(ω)                              (2.1.16.2)
```

composed with the isomorphism $\rho^{-1}$, defines an isomorphism of $R^{r} f_{*}(\mathcal{O}_{X}(n))$ onto the *dual*
of the locally free $\mathcal{O}_{Y}$-module

```text
  R^0 f_*(ω(−n)) = (⋀^{r+1} ℰ) ⊗_{𝒪_Y} (𝐒_{𝒪_Y}(ℰ))_{−n}.
```

<!-- original page 100 -->

## 2.2. The fundamental theorem of projective morphisms

**Theorem (2.2.1) (Serre).**

<!-- label: III.2.2.1 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module ample for $f$. For every $\mathcal{O}_{X}$-module $\mathcal{F}$, set $\mathcal{F}(n) =
\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ for every $n \in \mathbb{Z}$. Then, for every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$:*

*(i) The $R^{q} f_{*}(\mathcal{F})$ are coherent $\mathcal{O}_{Y}$-modules.*

*(ii) There exists an integer $N$ such that for $n \geq N$, one has $R^{q} f_{*}(\mathcal{F}(n)) = 0$ for every $q >
0$.*

*(iii) There exists an integer $N$ such that, for $n \geq N$, the canonical homomorphism $f^{*}(f_{*}(\mathcal{F}(n)))
\to \mathcal{F}(n)$ is surjective.*

**Proof.** Let us first note that if the theorem is true when one replaces $\mathcal{L}$ by $\mathcal{L}^{\otimes d}$
($d > 0$), it is true in its initial form. Indeed, one may then write $\mathcal{F}(n) = (\mathcal{F} \otimes
\mathcal{L}^{\otimes r}) \otimes \mathcal{L}^{\otimes hd}$ with $h \geq 0$ and $0 \leq r < d$, and by hypothesis, for
each $r$ there is an integer $N_{r}$ such that for $h \geq N_{r}$, properties (ii) and (iii) hold for the
$\mathcal{O}_{X}$-module $\mathcal{F} \otimes \mathcal{L}^{\otimes r}$; taking for $N$ the largest of the $d N_{r}$,
(ii) and (iii) will hold for $n \geq N$. One may therefore suppose $\mathcal{L}$ very ample relative to $f$
`(II, 4.6.11)`; consequently, there is a dominant $Y$-open immersion $i : X \to P$, where $P =
\operatorname{Proj}(\mathcal{S})$, with $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra with positive
degrees, in which $\mathcal{S}_{1}$ is of finite type and generates $\mathcal{S}$; in addition, $\mathcal{L}$ is
isomorphic to $i^{*}(\mathcal{O}_{P}(1))$ `(II, 4.4.7)`. But since $f$ is proper, so is $i$ `(II, 5.4.4)`, so $i$ is an
isomorphism $X \xrightarrow{\sim} P$. One may thus restrict to the case where $X = \operatorname{Proj}(\mathcal{S})$ and
$\mathcal{L} = \mathcal{O}_{X}(1)$. Theorem `(2.2.1)` is then a consequence of the following.

**Proposition (2.2.2).**

<!-- label: III.2.2.2 -->

*Let $A$ be a Noetherian ring, $S$ an $A$-algebra graded with positive degrees, in which `S_1` is an $A$-module having a
system of $r + 1$ generators, and which generates the algebra $S$. Let $X = \operatorname{Proj}(S)$. For every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$:*

*(i) The $A$-modules $H^{q}(X, \mathcal{F})$ are of finite type.*

*(ii) One has $H^{q}(X, \mathcal{F}) = 0$ for $q > r$.*

*(iii) There exists an integer $N$ such that for $n \geq N$, one has $H^{q}(X, \mathcal{F}(n)) = 0$ for every $q > 0$.*

*(iv) There exists an integer $N$ such that for $n \geq N$, $\mathcal{F}(n)$ is generated by its sections over $X$.*

**Proof.** Let us first show how `(2.2.2)` entails `(2.2.1)`: in `(2.2.1)` (reduced to the particular case $X =
\operatorname{Proj}(\mathcal{S})$ considered above), $Y$ is quasi-compact, so can be covered by a finite number of
affine open sets, with Noetherian rings, such that the restriction of $\mathcal{S}_{1}$ to each of these open sets
$U_{\alpha}$ is generated by a finite number of sections of $\mathcal{S}_{1}$ over $U_{\alpha}$. Assuming `(2.2.2)`
proved, it then suffices to take for $N$ in parts (ii) and (iii) of `(2.2.1)` the largest of the analogous integers
corresponding to the $U_{\alpha}$ (taking `(1.4.11)` and `(II, 3.4.7)` into account).

To prove `(2.2.2)`, note that $X$ identifies with a closed subscheme of $P = \mathbb{P}^{r}_{A}$ `(II, 3.6.2)`; in
addition, if $j : X \to P$ is the canonical injection, $j_{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{P}$-module, and
one has $j_{*}(\mathcal{F}(n)) = (j_{*}(\mathcal{F}))(n)$ `(II, 3.4.5 and 3.5.2)`. Taking `(G, II, cor. of th. 4.9.1)`
into account, one is therefore reduced to proving `(2.2.2)` in the particular case where $X = \mathbb{P}^{r}_{A}$ and $S
= A[T_{0}, \cdots, T_{r}]$. As $X$ is covered by the affine opens

<!-- original page 101 -->

$D_{+}(T_{i})$ in number $r + 1$, (ii) results from `(1.4.12)`. Note on the other hand that (iv) has already been proved
`(II, 2.7.9)`.

We shall prove (i) and (iii) simultaneously. Note that these assertions are true for $\mathcal{F} = \mathcal{O}_{X}(m)$
`(2.1.13)`; they are therefore also true when $\mathcal{F}$ is a direct sum of a finite number of
$\mathcal{O}_{X}$-modules of the form $\mathcal{O}_{X}(m_{j})$. On the other hand, (i) and (iii) are trivially true for
$q > r$ by virtue of (ii). We shall proceed by *descending induction* on $q$. We know that $\mathcal{F}$ is isomorphic
to a quotient of a direct sum $\mathcal{E}$ of a finite number of sheaves $\mathcal{O}_{X}(m_{j})$ `(II, 2.7.10)`; in
other words, one has an exact sequence $0 \to \mathcal{R} \to \mathcal{E} \to \mathcal{F} \to 0$, where $\mathcal{R}$ is
coherent $(0_{I}, 5.3.3)$ and $\mathcal{E}$ satisfies (i) and (iii). Since $\mathcal{F} \mapsto \mathcal{F}(n)$ is an
exact functor in $\mathcal{F}$, one also has the exact sequence

$$ 0 \to \mathcal{R}(n) \to \mathcal{E}(n) \to \mathcal{F}(n) \to 0 $$

for every $n \in \mathbb{Z}$. One deduces the exact cohomology sequence

```text
  H^{q−1}(X, ℰ(n)) → H^{q−1}(X, ℱ(n)) → H^q(X, ℛ(n)).
```

Since $\mathcal{E}(n)$ is a direct sum of the $\mathcal{O}_{X}(n + m_{j})$ `(II, 2.5.14)`, $H^{q-1}(X, \mathcal{E}(n))$
is of finite type, and so is $H^{q}(X, \mathcal{R}(n))$ by the induction hypothesis; since $A$ is Noetherian, one
concludes that $H^{q-1}(X, \mathcal{F}(n))$ is of finite type for every $n \in \mathbb{Z}$, and in particular for $n =
0$. On the other hand, by the induction hypothesis, there exists an integer $N$ such that for $n \geq N$ one has
$H^{q}(X, \mathcal{R}(n)) = 0$; furthermore, one may also suppose $N$ chosen so that $H^{q-1}(X, \mathcal{E}(n)) = 0$
for $n \geq N$, since $\mathcal{E}$ satisfies (iii); one concludes that $H^{q-1}(X, \mathcal{F}(n)) = 0$ for $n \geq N$,
which completes the proof.

**Corollary (2.2.3).**

<!-- label: III.2.2.3 -->

*Under the hypotheses of `(2.2.1)`, let $\mathcal{F} \to \mathcal{G} \to \mathcal{H}$ be an exact sequence of coherent
$\mathcal{O}_{X}$-modules. There then exists an integer $N$ such that for $n \geq N$, the sequence*

$$ f_{*}(\mathcal{F}(n)) \to f_{*}(\mathcal{G}(n)) \to f_{*}(\mathcal{H}(n)) $$

*is exact.*

**Proof.** Let $\mathcal{F}'$, $\mathcal{G}'$, $\mathcal{G}''$ be the kernel, image, and cokernel of $\mathcal{F} \to
\mathcal{G}$; $\mathcal{G}'$ is the kernel and $\mathcal{G}''$ the image of $\mathcal{G} \to \mathcal{H}$, let
$\mathcal{H}''$ be the cokernel of this homomorphism; all these $\mathcal{O}_{X}$-modules are coherent $(0_{I}, 5.3.4)$.
Since $\mathcal{F} \mapsto \mathcal{F}(n)$ is an exact functor in $\mathcal{F}$, it suffices to show that for $n$ large
enough, each of the sequences

$$ 0 \to f_{*}(\mathcal{F}'(n)) \to f_{*}(\mathcal{F}(n)) \to f_{*}(\mathcal{G}'(n)) \to 0 0 \to f_{*}(\mathcal{G}'(n))
\to f_{*}(\mathcal{G}(n)) \to f_{*}(\mathcal{G}''(n)) \to 0 0 \to f_{*}(\mathcal{G}''(n)) \to f_{*}(\mathcal{H}(n)) \to
f_{*}(\mathcal{H}''(n)) \to 0 $$

is exact; consequently, one may assume that $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ is exact. One then
has the exact cohomology sequence

```text
  0 → f_*(ℱ(n)) → f_*(𝒢(n)) → f_*(ℋ(n)) → R^1 f_*(ℱ(n)) → ⋯
```

and the conclusion follows from `(2.2.1, (ii))`.

**Corollary (2.2.4).**

<!-- label: III.2.2.4 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a morphism of finite type, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module ample for $f$; for every $\mathcal{O}_{X}$-module $\mathcal{F}$, set $\mathcal{F}(n) =
\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ (for $n \in \mathbb{Z}$). Let $\mathcal{F} \to
\mathcal{G} \to \mathcal{H}$ be an exact sequence of coherent $\mathcal{O}_{X}$-modules,*

<!-- original page 102 -->

*such that the supports of $\mathcal{F}$ and $\mathcal{H}$ are proper over $Y$ `(II, 5.4.10)`. There then exists an
integer $N$ such that, for $n \geq N$, the sequence*

$$ f_{*}(\mathcal{F}(n)) \to f_{*}(\mathcal{G}(n)) \to f_{*}(\mathcal{H}(n)) $$

*is exact.*

**Proof.** The same reasoning as at the beginning of `(2.2.1)` shows that if the corollary is true for
$\mathcal{L}^{\otimes d}$ ($d > 0$), it is also true for $\mathcal{L}$; one may therefore restrict to the case where
$\mathcal{L}$ is very ample for $f$ `(II, 4.6.11)`, and consequently one may identify $X$ with an open set in a
$Y$-scheme $Z = \operatorname{Proj}(\mathcal{S})$, where $\mathcal{S}$ is a quasi-coherent graded
$\mathcal{O}_{Y}$-algebra with positive degrees, in which $\mathcal{S}_{1}$ is of finite type and generates
$\mathcal{S}$, so that $\mathcal{L} = i^{*}(\mathcal{O}_{Z}(1))$, where $i$ is the canonical immersion $X \to Z$
`(II, 4.4.7)`. This being so, as $Supp(\mathcal{G})$ is closed in $X$ and contained in $Supp(\mathcal{F}) \cap
Supp(\mathcal{H})$, it is proper over $Y$; the supports of $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are thus closed
in $Z$ `(II, 5.4.10)`. The sheaves $\mathcal{F}' = i_{*}(\mathcal{F})$, $\mathcal{G}' = i_{*}(\mathcal{G})$,
$\mathcal{H}' = i_{*}(\mathcal{H})$ are therefore coherent $\mathcal{O}_{Z}$-modules, and the sequence $\mathcal{F}' \to
\mathcal{G}' \to \mathcal{H}'$ is exact; in addition, if $g : Z \to Y$ is the structure morphism, one has $f = g \circ
i$, and it is clear that $\mathcal{F}(n) = i^{*}(\mathcal{F}'(n))$ and similarly for $\mathcal{G}$ and $\mathcal{H}$;
the conclusion thus follows from `(2.2.3)` applied to $\mathcal{F}'$, $\mathcal{G}'$, $\mathcal{H}'$.

**Remarks (2.2.5).**

<!-- label: III.2.2.5 -->

(i) Assertion (i) of `(2.2.1)` is still true when one supposes only that $Y$ is *locally Noetherian*; indeed, the
property is evidently local on $Y$; on the other hand, the hypotheses of `(2.2.1)` imply that for every open $U \subset
Y$, the restriction of $f$ to $f^{-1}(U)$ is a projective morphism $f^{-1}(U) \to U$ `(II, 5.5.5, (iii))` and
$\mathcal{L} \mid f^{-1}(U)$ is ample for this morphism `(II, 4.6.4)`.

(ii) Assertion (iii) of `(2.2.1)` is still valid, as we have seen, when one supposes only that $X$ is a quasi-compact
scheme or a prescheme whose underlying space is Noetherian, and $f : X \to Y$ a quasi-compact morphism `(II, 4.6.8)`.
But it should be noted that even when one supposes that $Y$ is the spectrum of a field $K$ and that $f$ is
quasi-projective, assertion (ii) of `(2.2.1)` is no longer necessarily verified. For example, let $X' =
\operatorname{Spec}(K[T_{0}, \cdots, T_{r}])$ and let $X$ be the union of the affine opens $D(T_{i})$ of $X'$ ($0 \leq i
\leq r$); since the immersion $X \to X'$ is quasi-compact, the structure morphism $f : X \to Y$ is quasi-affine
`(II, 5.1.10)`, so $\mathcal{O}_{X}$ is very ample for $f$ `(II, 5.1.6)`. But the ring $\Gamma(X, \mathcal{O}_{X})$
identifies with the intersection of the rings of fractions $(K[T_{0}, \cdots, T_{r}])_{T_{i}}$ for $0 \leq i \leq r$
`(I, 8.2.1.1)`, that is, with $K[T_{0}, \cdots, T_{r}]$. Consequently, it follows from formulas `(1.4.3.1)` and
`(1.1.3.5)` that one has $H^{r}(X, \mathcal{O}^{\otimes n}_{X}) = H^{r}(X, \mathcal{O}_{X}) = A \neq 0$ for every $n$.

## 2.3. Application to graded sheaves of algebras and of modules

**Theorem (2.3.1).**

<!-- label: III.2.3.1 -->

*Let $Y$ be a Noetherian prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra of finite type with
positive degrees, $X = \operatorname{Proj}(\mathcal{S})$, $q : X \to Y$ the structure morphism, $\mathcal{M}$ a
quasi-coherent graded $\mathcal{S}$-module satisfying condition `(TF)`. Then there exists an integer $N$ such that, for
$n \geq N$, the canonical homomorphism `(II, 8.14.5.1)`*

```text
  α_n : ℳ_n → q_*(𝒫roj(ℳ(n))) = q_*((𝒫roj(ℳ))_n)
```

<!-- original page 103 -->

*is bijective. In other words, the canonical homomorphism*

$$ \alpha : \mathcal{M} \to \Gamma_{*}(\mathcal{P}roj(\mathcal{M})) $$

*is a `(TN)`-isomorphism.*

**Proof.** One may restrict to the case where $\mathcal{M}$ is an $\mathcal{S}$-module of finite type `(II, 3.4.2)`.

As $Y$ is quasi-compact, there exists an integer $d > 0$ such that $\mathcal{S}^{(d)}$ is generated by the
quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{S}_{d}$, the latter being of finite type `(II, 3.1.10)`, hence
coherent since $Y$ is Noetherian. Note now that $\mathcal{M}$ is a direct sum of the $\mathcal{M}^{(d,k)}$ for $0 \leq k
< d$, and that each of the $\mathcal{M}^{(d,k)}$ is a quasi-coherent $\mathcal{S}^{(d)}$-module of finite type, as
follows from `(II, 2.1.6, (iii))`, the question being local on $Y$. Now, it obviously suffices to prove that each of the
canonical homomorphisms $\alpha : \mathcal{M}^{(d,k)} \to \Gamma_{*}(\mathcal{P}roj(\mathcal{M}))^{(d,k)}$ is a
`(TN)`-isomorphism. Taking `(II, 8.14.13)` into account (and notably the diagram `(8.14.13.4)`), one sees that one is
reduced to proving the theorem when $\mathcal{S}$ is generated by $\mathcal{S}_{1}$ and $\mathcal{S}_{1}$ is a coherent
$\mathcal{O}_{Y}$-module. Since $Y$ is Noetherian, the same reasoning as at the beginning of `(2.2.2)` shows that one
may restrict to the case where $Y = \operatorname{Spec}(A)$, $\mathcal{S} = \tilde{S}$, $\mathcal{M} = \tilde{M}$, $A$
being a Noetherian ring, `S_1` an $A$-module of finite type and $M$ a graded $S$-module of finite type. Let us show that
it then suffices to prove the theorem when $M = S$. Indeed, in the general case, one has an exact sequence $L' \to L \to
M \to 0$, where $L$ and $L'$ are direct sums of graded modules of the form $S(m)$. If the result is true for $M = S$, it
is also true for $M = S(m)$, hence for $L$ and $L'$. Consider then the commutative diagram

$$ \tilde{L}'_{n} \to \tilde{L}_{n} \to \tilde{M}_{n} \to 0

   \downarrow \alpha_{n}              \downarrow \alpha_{n}              \downarrow \alpha_{n}

  q_{*}(\tilde{L}'(n))   \to    q_{*}(\tilde{L}(n))    \to    q_{*}(\tilde{M}(n))    \to    0
$$

The second line is exact by virtue of `(2.2.3)` as soon as $n$ is large enough; as the same holds for the first, and as
the two left vertical arrows are isomorphisms, so is the third.

This being so, to prove the theorem when $M = S$, suppose first that $S = A[T_{0}, \cdots, T_{r}]$ ($T_{i}$
indeterminates); in this case, our assertion is none other than `(2.1.11, (ii))`. In the general case, $S$ identifies
with a quotient of a ring $S' = A[T_{0}, \cdots, T_{r}]$ by a graded ideal, hence $X$ with a closed subscheme of $X' =
\mathbb{P}^{r}_{A}$ `(II, 2.9.2)`. If $j$ is the canonical injection $X \to X'$, $j_{*}(\tilde{S}(n))$ is none other
than the $\mathcal{O}_{X'}$-module $(\mathcal{P}roj(\tilde{S}))(n)$ where $S$ is considered as a graded $S'$-module;
this follows immediately from `(II, 2.8.7)`. As $j_{*}(\tilde{S}(n))$ is an $\mathcal{O}_{X'}$-module satisfying `(TF)`,
the canonical homomorphism $\alpha_{n} : S_{n} \to \Gamma(X', j_{*}(\tilde{S}(n)))$ is bijective for $n$ large enough,
by virtue of what precedes; this completes the proof, since $\Gamma(X', j_{*}(\tilde{S}(n))) = \Gamma(X, \tilde{S}(n))$.

<!-- original page 104 -->

**Corollary (2.3.2).**

<!-- label: III.2.3.2 -->

*Under the hypotheses of `(2.3.1)`, let $\mathcal{S}_{X} = \oplus_{n \in \mathbb{Z}} \mathcal{O}_{X}(n)$, and let
$\mathcal{F}$ be a quasi-coherent graded $\mathcal{S}_{X}$-module of finite type. Then $\Gamma_{*}(\mathcal{F})$
satisfies condition `(TF)`.*

**Proof.** We have seen in the proof of `(2.3.1)` that $X$, which is isomorphic to
$\operatorname{Proj}(\mathcal{S}^{(d)})$ `(II, 3.1.8)`, is of finite type over $Y$ `(II, 3.4.1)`. It then follows from
`(II, 8.14.9)` that $\mathcal{F}$ is isomorphic to an $\mathcal{O}_{X}$-graded module of the form
$\mathcal{P}roj(\mathcal{M})$, where $\mathcal{M}$ is a quasi-coherent graded $\mathcal{S}$-module of finite type. By
virtue of `(2.3.1)`, $\Gamma_{*}(\mathcal{F})$ is `(TN)`-isomorphic to $\mathcal{M}$, and consequently satisfies `(TF)`.

**Scholium (2.3.3).**

<!-- label: III.2.3.3 -->

Let $Y$ be a Noetherian prescheme, $\mathcal{S}$ an $\mathcal{O}_{Y}$-algebra graded satisfying the conditions of
`(2.3.1)` and $X = \operatorname{Proj}(\mathcal{S})$. Let $\mathbf{K}_{\mathcal{S}}$ be the abelian category of
quasi-coherent graded $\mathcal{S}$-modules satisfying `(TF)`, $\mathbf{K}'_{\mathcal{S}}$ the subcategory of
$\mathbf{K}_{\mathcal{S}}$ formed of $\mathcal{S}$-modules satisfying `(TN)`; finally, let $\mathbf{K}_{X}$ be the
category of quasi-coherent graded $\mathcal{S}_{X}$-modules of finite type $\mathcal{F}$ (which amounts to saying, since
$\mathcal{S}_{X}$ is periodic `(II, 8.14.4 and 8.14.12)`, that the $\mathcal{F}_{i}$ are coherent
$\mathcal{O}_{X}$-modules). Then the functors $\mathcal{M} \mapsto \mathcal{P}roj(\mathcal{M})$ in
$\mathbf{K}_{\mathcal{S}}$ and $\mathcal{F} \mapsto \Gamma_{*}(\mathcal{F})$ in $\mathbf{K}_{X}$ define, by virtue of
`(II, 8.14.8 and 8.14.10)` and `(2.3.2)`, an *equivalence* `(T, I, 1.2)` of the quotient category
$\mathbf{K}_{\mathcal{S}} / \mathbf{K}'_{\mathcal{S}}$ `(T, I, 1.11)` with the category $\mathbf{K}_{X}$. When
$\mathcal{S}$ is generated by $\mathcal{S}_{1}$, one may replace $\mathbf{K}_{X}$ by the category of coherent
$\mathcal{O}_{X}$-modules `(II, 8.14.12)`.

**Proposition (2.3.4).**

<!-- label: III.2.3.4 -->

*Let $Y$ be a Noetherian prescheme.*

*(i) Let $\mathcal{S}$ be a quasi-coherent graded $\mathcal{O}_{Y}$-algebra of finite type with positive degrees. Let $X
= \operatorname{Proj}(\mathcal{S})$ and $\mathcal{S}_{X} = \mathcal{P}roj(\mathcal{S}) = \oplus_{n \in \mathbb{Z}}
\mathcal{O}_{X}(n)$. Then $\mathcal{S}_{X}$ is a periodic graded $\mathcal{O}_{Y}$-algebra `(II, 8.14.12)` whose
homogeneous components $(\mathcal{S}_{X})_{n} = \mathcal{O}_{X}(n)$ are coherent $\mathcal{O}_{X}$-modules, and if $d >
0$ is a period of $\mathcal{S}_{X}$, $(\mathcal{S}_{X})_{d} = \mathcal{O}_{X}(d)$ is an invertible
$\mathcal{O}_{X}$-module $Y$-ample. In addition, the canonical homomorphism $\alpha : \mathcal{S} \to
\Gamma_{*}(\mathcal{S}_{X})$ is a `(TN)`-isomorphism.*

*(ii) Conversely, let $q : X \to Y$ be a projective morphism, and let $\mathcal{S}'$ be a graded
$\mathcal{O}_{X}$-algebra whose homogeneous components $\mathcal{S}'_{n}$ ($n \in \mathbb{Z}$) are coherent
$\mathcal{O}_{X}$-modules, and which admits a period $d > 0$ such that $\mathcal{S}'_{d}$ is an invertible
$\mathcal{O}_{X}$-module ample for $q$. Then $\mathcal{S} = \oplus_{n \geq 0} q_{*}(\mathcal{S}'_{n})$ is a
quasi-coherent graded $\mathcal{O}_{Y}$-algebra with positive degrees of finite type, and there exists a $Y$-isomorphism
$r : X \xrightarrow{\sim} \operatorname{Proj}(\mathcal{S})$ such that $r^{*}(\mathcal{P}roj(\mathcal{S}))$ is isomorphic
(as a graded $\mathcal{O}_{X}$-algebra) to $\mathcal{S}'$.*

**Proof.** (i) All the assertions have essentially already been proved, the last being none other than a particular case
of `(2.3.2)`. The fact that $\mathcal{S}_{X}$ is periodic has been seen in `(II, 8.14.14)`, and the fact that there is a
period $d > 0$ such that $\mathcal{O}_{X}(d)$ is invertible and $Y$-ample is none other than `(II, 4.6.18)`. Finally,
for $0 \leq k < d$, $(\mathcal{S}_{X})^{(d,k)}$ is a $(\mathcal{S}_{X})^{(d)}$-module of finite type `(II, 8.14.14)`, so
each of the $(\mathcal{S}_{X})_{n}$ is a quasi-coherent $\mathcal{S}_{X}$-module of finite type by virtue of
`(II, 2.1.6, (ii))`, the question being local; as $\mathcal{S}_{X}$ is coherent, so are the $(\mathcal{S}_{X})_{n}$.

(ii) Up to replacing the period $d$ by one of its multiples, one may suppose that $\mathcal{L} = \mathcal{S}'_{d}$ is an
$\mathcal{O}_{X}$-module very ample relative to $q$ `(II, 4.6.11)`. We have in addition $\mathcal{S}'^{(d)} = \oplus
\mathcal{L}^{\otimes n}$ by hypothesis, so $\mathcal{S}^{(d)} = \oplus q_{*}(\mathcal{L}^{\otimes n})$; we know
`(II, 3.1.8 and 3.2.9)` that there is a $Y$-isomorphism $s$ of $X' = \operatorname{Proj}(\mathcal{S})$ onto $X'' =
\operatorname{Proj}(\mathcal{S}^{(d)})$ such that

<!-- original page 105 -->

$s^{*}(\mathcal{O}_{X''}(n)) = \mathcal{O}_{X'}(nd)$. One will therefore establish the existence of a $Y$-isomorphism $X
\xrightarrow{\sim} X'$ if one proves the following.

**Proposition (2.3.4.1).**

<!-- label: III.2.3.4.1 -->

*Let $Y$ be a Noetherian prescheme, $q : X \to Y$ a projective morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module very ample for $q$. Then $\mathcal{S} = \oplus_{n \geq 0} q_{*}(\mathcal{L}^{\otimes n})$ is a
quasi-coherent graded $\mathcal{O}_{Y}$-algebra of finite type, such that $\mathcal{S}_{n} = \mathcal{S}^{n}_{1}$ for
$n$ large enough, and there exists a $Y$-isomorphism $r : X \xrightarrow{\sim} P = \operatorname{Proj}(\mathcal{S})$
such that $\mathcal{L} = r^{*}(\mathcal{O}_{P}(1))$.*

**Proof.** As $q$ is a projective morphism, it follows from `(II, 5.4.4 and 4.4.7)` that there exists a $Y$-isomorphism
$r' : X \xrightarrow{\sim} P' = \operatorname{Proj}(\mathcal{T})$, where $\mathcal{T}$ is a quasi-coherent
$\mathcal{O}_{Y}$-algebra such that $\mathcal{T}_{1}$ is an $\mathcal{O}_{Y}$-module of finite type and generates
$\mathcal{T}$, and one has $\mathcal{L} = r'^{*}(\mathcal{O}_{P'}(1))$. One then has $\mathcal{S} = \oplus_{n \geq 0}
q'_{*}(\mathcal{O}_{P'}(n))$, where $q' : P' \to Y$ is the structure morphism, and it follows from `(2.3.1)` that for
$n$ large enough, the canonical homomorphism $\alpha_{n} : \mathcal{T}_{n} \to \mathcal{S}_{n} =
q'_{*}(\mathcal{O}_{P'}(n))$ is bijective; as $\mathcal{T}_{n} = \mathcal{T}^{n}_{1}$, one has *a fortiori*
$\mathcal{S}_{n} = \mathcal{S}^{n}_{1}$ as soon as $n$ is large enough. In addition, as the canonical homomorphism
$\alpha : \mathcal{T} \to \mathcal{S}$ of graded $\mathcal{O}_{Y}$-algebras is a `(TN)`-isomorphism,
`Φ = Proj(α) : Proj(𝒮) → Proj(𝒯)` is an isomorphism `(II, 3.6.1)` and one has $\Phi_{*}(\mathcal{O}_{P}(n)) =
(\mathcal{O}_{P'}(n))_{[\alpha]}$ `(II, 3.5.2)`; but since the $\mathcal{T}$-graded modules
$(\mathcal{S}(n))_{[\alpha]}$ and $\mathcal{T}(n)$ are `(TN)`-isomorphic, one has $\Phi_{*}(\mathcal{O}_{P}(n)) =
\mathcal{O}_{P'}(n)$ for every $n$ `(II, 3.4.2)`; to complete the proof of `(2.3.4.1)`, it remains to show that
$\mathcal{S}$ is an $\mathcal{O}_{Y}$-algebra of finite type; now the $\mathcal{S}_{n} = q'_{*}(\mathcal{O}_{P'}(n))$
are coherent $\mathcal{O}_{Y}$-modules by virtue of `(2.2.1)` and, since $\mathcal{S}_{n} = \mathcal{S}^{n}_{1}$ for $n
\geq n_{0}$, $\mathcal{S}$ is generated by $\oplus_{i \leq n_{0}} \mathcal{S}_{i}$, which is coherent, whence our
assertion `(I, 9.6.2)`.

Let us return to the proof of `(2.3.4)`, whose notation we resume. We have proved the existence of a $Y$-isomorphism
$r'' : X \xrightarrow{\sim} X''$ such that $r''^{*}(\mathcal{L}^{\otimes n}) = \mathcal{O}_{X''}(nd)$ for every $n \in
\mathbb{Z}$; we shall denote by `q''` the structure morphism $X'' \to Y$. Note now that $\mathcal{S}'$ is a direct sum
of the $\mathcal{S}'^{(d)}$-graded modules $\mathcal{S}'^{(d,k)}$; each of the latter is a quasi-coherent
$\mathcal{S}'^{(d)}$-module of finite type, by virtue of the periodicity of $\mathcal{S}'$ and the hypothesis that the
$\mathcal{S}'_{n}$ are $\mathcal{O}_{X}$-modules of finite type `(II, 8.14.12)`. Set $\mathcal{F}^{(k)} =
r''_{*}(\mathcal{S}'^{(d,k)})$, so the $\mathcal{F}^{(k)}$ are quasi-coherent graded $\mathcal{S}_{X''}$-modules of
finite type; consequently `(II, 8.14.8)`, the canonical homomorphism $\beta :
\mathcal{P}roj(\Gamma_{*}(\mathcal{F}^{(k)})) \to \mathcal{F}^{(k)}$ is an isomorphism of $\mathcal{S}_{X''}$-modules.
But one has $q''_{*}((\mathcal{F}^{(k)})_{n}) = q_{*}((\mathcal{S}'^{(d,k)})_{n})$ and for $n \geq 0$, this last
$\mathcal{O}_{Y}$-module is by definition equal to $(\mathcal{S}^{(d,k)})_{n}$. In other words, the canonical injection
$\mathcal{S}^{(d,k)} \to \Gamma_{*}(\mathcal{F}^{(k)})$ is a `(TN)`-isomorphism, hence `(II, 3.4.2)` one has
$\mathcal{P}roj(\mathcal{S}^{(d,k)}) = \mathcal{P}roj(\Gamma_{*}(\mathcal{F}^{(k)}))$, and consequently
$r''^{*}(\mathcal{P}roj(\mathcal{S}^{(d,k)})) = \mathcal{S}'^{(d,k)}$. It remains to note that
$\mathcal{P}roj(\mathcal{S}^{(d,k)}) = (\mathcal{P}roj(\mathcal{S}))^{(d,k)}$ up to a canonical isomorphism
`(II, 8.14.13.1)` in order to have proved the isomorphism of $r^{*}(\mathcal{P}roj(\mathcal{S}))$ and $\mathcal{S}'$.
Finally, by virtue of `(2.3.2)`, each of the $\Gamma_{*}(\mathcal{F}^{(k)})$ satisfies condition `(TF)`, so the same
holds for each of the $\mathcal{S}^{(d,k)}$; in addition, since the $\mathcal{S}'_{n}$ are coherent, the same holds for
the $\mathcal{S}_{n} = q_{*}(\mathcal{S}'_{n})$ by `(2.2.1)`, and one concludes at once that the $\mathcal{S}_{n}$ are
$\mathcal{O}_{Y}$-modules of finite type. As we have seen in `(2.3.4.1)` that $\mathcal{S}^{(d)}$ is an
$\mathcal{O}_{Y}$-algebra of finite type, one concludes that $\mathcal{S}$ is also an $\mathcal{O}_{Y}$-algebra of
finite type.

<!-- original page 106 -->

**Proposition (2.3.5).**

<!-- label: III.2.3.5 -->

*Let $Y$ be an integral Noetherian prescheme, $X$ an integral prescheme, $f : X \to Y$ a birational projective morphism.
There then exists a coherent fractional ideal sheaf $\mathcal{J} \subset \mathcal{R}(Y)$ `(II, 8.1.2)` such that $X$ is
$Y$-isomorphic to the prescheme obtained by blowing up $\mathcal{J}$ `(II, 8.1.3)`. In addition, there exists an open
set $U$ of $Y$ such that the restriction of $f$ to $f^{-1}(U)$ is an isomorphism of $f^{-1}(U)$ onto $U$ (cf.
`(I, 6.5.5)`), and such that $\mathcal{J} \mid U$ is invertible.*

**Proof.** As there exists an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ very ample for $f$
`(II, 4.4.2 and 5.3.2)`, one may apply `(2.3.4.1)`, and one sees that $X$ identifies with
$\operatorname{Proj}(\mathcal{S})$, where $\mathcal{S} = \oplus f_{*}(\mathcal{L}^{\otimes n})$. We know in addition
that the $f_{*}(\mathcal{L}^{\otimes n})$ are torsion-free $\mathcal{O}_{Y}$-modules `(I, 7.4.5)`, so the same holds for
the $\mathcal{O}_{Y}$-module $\mathcal{S}$, and consequently $\mathcal{S}$ identifies canonically with a
sub-$\mathcal{O}_{Y}$-module of $\mathcal{S} \otimes_{\mathcal{O}_{Y}} \mathcal{R}(Y)$ `(I, 7.4.1)`; the latter is a
*simple* sheaf `(I, 7.3.6)`, which is known when one knows its restriction to a nonempty open set, for instance to a
nonempty open $U' \subset U$ such that $\mathcal{L} \mid f^{-1}(U')$ is isomorphic to $\mathcal{O}_{X} \mid f^{-1}(U')$.
Since by hypothesis the $f_{*}(\mathcal{L}^{\otimes n}) \mid U'$ are then isomorphic to $\mathcal{O}_{Y} \mid U'$, one
sees that $\mathcal{S} \otimes_{\mathcal{O}_{Y}} \mathcal{R}(Y)$ is an $\mathcal{R}(Y)$-module isomorphic to
$\mathcal{R}(Y)[T]$, where $T$ is an indeterminate, and $\mathcal{S}$ is `(TN)`-isomorphic to the
sub-$\mathcal{O}_{Y}$-algebra generated by the canonical image of $f_{*}(\mathcal{L})$ in $\mathcal{S} \otimes
\mathcal{R}(Y)$ `(2.3.4.1)`; but if one identifies $\mathcal{S} \otimes \mathcal{R}(Y)$ with $\mathcal{R}(Y)[T]$, the
image of $f_{*}(\mathcal{L})$ identifies with $\mathcal{J} \cdot T$, where $\mathcal{J}$ is a coherent
sub-$\mathcal{O}_{Y}$-module `(2.2.1)` of $\mathcal{R}(Y)$, whose restriction to $U'$ is isomorphic to $\mathcal{O}_{Y}
\mid U'$, and which consequently is such that $\mathcal{J} \mid U$ is invertible. One then sees that $\mathcal{S}$ is
`(TN)`-isomorphic to $\oplus \mathcal{J}^{n}$, which completes the proof.

**Corollary (2.3.6).**

<!-- label: III.2.3.6 -->

*Under the hypotheses of `(2.3.5)`, suppose in addition that for every coherent sub-$\mathcal{O}_{Y}$-module
$\mathcal{J} \neq 0$ of $\mathcal{R}(Y)$, there exists an invertible $\mathcal{O}_{Y}$-module $\mathcal{L}$ such that
$\Gamma(Y, \mathcal{L} \otimes_{\mathcal{O}_{Y}} \mathcal{H}om(\mathcal{J}, \mathcal{O}_{Y})) \neq 0$; then, in the
statement of `(2.3.5)`, one may suppose that $\mathcal{J}$ is an ideal of $\mathcal{O}_{Y}$. This additional condition
is always satisfied if there exists an ample $\mathcal{O}_{Y}$-module.*

**Proof.** Indeed, one has $(0_{I}, 5.4.2)$

```text
  ℒ ⊗ ℋom(𝒥, 𝒪_Y) = ℋom(ℒ^{−1}, ℋom(𝒥, 𝒪_Y)) = ℋom(𝒥 ⊗ ℒ^{−1}, 𝒪_Y);
```

the hypothesis thus signifies that there is a nonzero homomorphism $u$ of $\mathcal{J} \otimes \mathcal{L}^{-1}$ into
$\mathcal{O}_{Y}$. As, for every $y \in Y$, $(\mathcal{J} \otimes \mathcal{L}^{-1})_{y}$ identifies with a
sub-$\mathcal{O}_{y}$-module of the field of fractions $(\mathcal{R}(Y))_{y}$ of $\mathcal{O}_{y}$ `(I, 7.1.5)`, $u_{y}$
is necessarily injective, so $u$ is an isomorphism of $\mathcal{J} \otimes \mathcal{L}^{-1}$ onto an ideal
$\mathcal{J}'$ of $\mathcal{O}_{Y}$. But since $\operatorname{Proj}(\oplus_{n \geq 0} \mathcal{J}^{n})$ and
$\operatorname{Proj}(\oplus_{n \geq 0} (\mathcal{J} \otimes \mathcal{L}^{-1})^{n})$ are $Y$-isomorphic `(II, 3.1.8)`,
this proves the first assertion of the corollary. To prove the second, note that $\mathcal{F} =
\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{J}, \mathcal{O}_{Y})$ is coherent and $\neq 0$, since there exists an open set
$U$ of $Y$ such that $\mathcal{J} \mid U$ is invertible. If $\mathcal{L}$ is an ample $\mathcal{O}_{Y}$-module, there
exists an integer $n$ such that $\mathcal{F}(n) = \mathcal{F} \otimes \mathcal{L}^{\otimes n}$ is generated by its
sections over $Y$ `(II, 4.5.5)`; *a fortiori*, one has $\Gamma(Y, \mathcal{F}(n)) \neq 0$, whence the conclusion.

**Corollary (2.3.7).**

<!-- label: III.2.3.7 -->

*Let $X$ and $Y$ be two integral schemes, projective over a field $k$, and let $f : X \to Y$ be a birational
$k$-morphism. Then $X$ is $k$-isomorphic to a $k$-scheme obtained by blowing up a closed subscheme $Y'$ (not necessarily
reduced) of $Y$.*

<!-- original page 107 -->

**Proof.** Indeed, $f$ is projective `(II, 5.5.5, (v))`, and as $Y$ is projective over $k$, the additional condition of
`(2.3.6)` is satisfied; it then suffices to consider the closed subscheme $Y'$ of $Y$ defined by the coherent ideal
$\mathcal{J}$ of cor. `(2.3.6)`.

**Remark (2.3.8).**

<!-- label: III.2.3.8 -->

In Chap. IV, in studying the notion of divisor, we shall see that if, in the statement of `(2.3.5)`, one supposes that
the rings $\mathcal{O}_{y}$ ($y \in Y$) are factorial (which is the case for instance if $Y$ is non-singular), then $X$
may be deduced from $Y$ by blowing up a closed sub-prescheme $Y'$ of $Y$ whose underlying space is contained in $Y - U$.

## 2.4. A generalization of the fundamental theorem

**Theorem (2.4.1).**

<!-- label: III.2.4.1 -->

*Let $Y$ be a Noetherian prescheme, $\mathcal{S}$ a quasi-coherent $\mathcal{O}_{Y}$-algebra of finite type. Let $f : X
\to Y$ be a projective morphism, $\mathcal{S}' = f^{*}(\mathcal{S})$, $\mathcal{M}$ a quasi-coherent
$\mathcal{S}'$-module of finite type. Then:*

*(i) For every $p \in \mathbb{Z}$, $R^{p} f_{*}(\mathcal{M})$ is an $\mathcal{S}$-module of finite type.*

*(ii) Let in addition $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-module ample for $f$, and set $\mathcal{M}(n) =
\mathcal{M} \otimes \mathcal{L}^{\otimes n}$ for every $n \in \mathbb{Z}$. There exists an integer $N$ such that, for $n
\geq N$, one has*

$$ R^{p} f_{*}(\mathcal{M}(n)) = 0 (2.4.1.1) $$

*for every $p > 0$, and the canonical homomorphism $f^{*}(f_{*}(\mathcal{M}(n))) \to \mathcal{M}(n)$ $(0_{I}, 4.4.3)$ is
surjective.*

**Proof.** Set $Y' = \operatorname{Spec}(\mathcal{S})$, $X' = \operatorname{Spec}(\mathcal{S}')$, so that $X' = X
\times_{Y} Y'$ `(II, 1.5.5)`; let $g : Y' \to Y$, $g' : X' \to X$ be the structure morphisms, which are affine by
definition, and $f' = f_{(Y')} : X' \to Y'$; one therefore has a commutative diagram

```text
        g'
   X ←──── X'
   |       |
 f |  ↘ h  | f'
   ↓       ↓
   Y ←──── Y'
        g
```

and the morphism $f'$ is projective `(II, 5.5.5, (iii))`; set $h = f \circ g' = g \circ f'$.

(i) Let $\tilde{\mathcal{M}}$ be the $\mathcal{O}_{X'}$-module associated to the quasi-coherent $\mathcal{S}'$-module
$\mathcal{M}$, when $X'$ is considered as an affine $X$-scheme `(II, 1.4.3)`, so that one has $\mathcal{M} =
g'_{*}(\tilde{\mathcal{M}})$; as $\mathcal{M}$ is an $\mathcal{S}'$-module of finite type, $\tilde{\mathcal{M}}$ is an
$\mathcal{O}_{X'}$-module of finite type `(II, 1.4.5)`; as $h$ is of finite type, since $g$ and $f'$ are
`(II, 1.3.7 and I, 6.3.4, (ii))`, $X'$ is Noetherian `(I, 6.3.7)` and $\tilde{\mathcal{M}}$ is consequently coherent.
This being so, as $g'$ is affine, the canonical homomorphism $R^{p} f_{*}(\mathcal{M}) \to R^{p}
h_{*}(\tilde{\mathcal{M}})$ is bijective `(1.3.4)`. In addition, this homomorphism is a homomorphism of
$\mathcal{S}$-modules; indeed, from the canonical homomorphism

```text
  g^*(𝒮) ⊗_{𝒪_{X'}} g'^*(ℳ) → g'^*(ℳ)                                       (2.4.1.2)
```

which defines the $\mathcal{S}'$-module structure of $\mathcal{M}$ (recalling that $\mathcal{S}' =
g'^{*}(\mathcal{O}_{X'})$), one canonically deduces a homomorphism

```text
  f_*(g^*(𝒮)) ⊗ R^p f_*(g'^*(ℳ)) → R^p f_*(g'^*(ℳ))
```

<!-- original page 108 -->

`(0, 12.2.2)`, and since `(2.4.1.2)` itself comes (by application of $(0_{I}, 4.2.2.1)$) from the homomorphism
$\mathcal{O}_{X'} \otimes \tilde{\mathcal{M}} \to \tilde{\mathcal{M}}$ defining the $\mathcal{O}_{X'}$-module structure
of $\tilde{\mathcal{M}}$, the diagram

```text
  f_*(g'_*(𝒪_{X'})) ⊗ R^p f_*(g'_*(ℳ̃))    →    R^p f_*(g'_*(ℳ̃))

           ↓                                            ↓

  h_*(𝒪_{X'}) ⊗ R^p h_*(ℳ̃)                →    R^p h_*(ℳ̃)
```

is commutative `(0, 12.2.6)`; composing the horizontal arrows with the homomorphism coming from the canonical
homomorphism $\mathcal{S} \to f_{*}(f^{*}(\mathcal{S})) = f_{*}(\mathcal{S}') = f_{*}(g'_{*}(\mathcal{O}_{X'})) =
h_{*}(\mathcal{O}_{X'})$, one obtains our assertion. On the other hand, since $g$ is affine and $f'$ is separated and
quasi-compact, the canonical homomorphism $R^{p} h_{*}(\tilde{\mathcal{M}}) \to g_{*}(R^{p}
f'_{*}(\tilde{\mathcal{M}}))$ is bijective `(1.4.14)`, and one shows as above that it is an isomorphism of
$\mathcal{S}$-modules (this time using the commutativity of `(0, 12.2.6.2)`). Now, since $f'$ is projective and
$\tilde{\mathcal{M}}$ is coherent, $R^{p} f'_{*}(\tilde{\mathcal{M}})$ is a coherent $\mathcal{O}_{Y'}$-module by virtue
of `(2.2.1)`; one concludes that $g_{*}(R^{p} f'_{*}(\tilde{\mathcal{M}}))$ is an $\mathcal{S}$-module of finite type
`(II, 1.4.5)`.

(ii) Let $\mathcal{L}' = g'^{*}(\mathcal{L})$, which is an invertible $\mathcal{O}_{X'}$-module; for every $n \in
\mathbb{Z}$, one has $g'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n}) = g'_{*}(\tilde{\mathcal{M}}) \otimes
\mathcal{L}^{\otimes n} = \mathcal{M}(n)$ $(0_{I}, 5.4.10)$ up to an isomorphism; one may apply to $\tilde{\mathcal{M}}
\otimes \mathcal{L}'^{\otimes n}$ the reasoning made in (i) for $\tilde{\mathcal{M}}$, which proves that $R^{p}
f_{*}(\mathcal{M}(n))$ is isomorphic to $g_{*}(R^{p} f'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n}))$. Now
$\mathcal{L}'$ is ample for $f'$ `(II, 4.6.13, (iii))`, so it follows from `(2.2.1)` that there exists an integer $N$
such that $R^{p} f'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n}) = 0$ for every $p$ and every $n \geq N$,
which proves `(2.4.1.1)`. Finally, it follows again from `(2.2.1)` that one may suppose $N$ chosen so that for $n \geq
N$, the canonical homomorphism $f'^{*}(f'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n})) \to
\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n}$ is surjective; as $g'_{*}$ is an exact functor `(II, 1.4.4)`, the
corresponding homomorphism

```text
  g'_*(f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) → g'_*(ℳ̃ ⊗ ℒ'^{⊗n}) = ℳ(n)
```

is surjective. Now, one has $g'_{*}(f'^{*}(f'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n}))) =
f^{*}(g_{*}(f'_{*}(\tilde{\mathcal{M}} \otimes \mathcal{L}'^{\otimes n})))$ `(II, 1.5.2)` and since $g \circ f' = f
\circ g'$, one finally sees that one has

```text
  g'_*(f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) = f^*(f_*(g'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) = f^*(f_*(ℳ(n))),
```

which completes the proof.

**2.4.2.**

<!-- label: III.2.4.2 -->

We shall in particular have to apply `(2.4.1)` when $\mathcal{S}$ is an $\mathcal{O}_{Y}$-graded algebra with positive
degrees, $\mathcal{M} = \oplus_{k \in \mathbb{Z}} \mathcal{M}_{k}$ an $\mathcal{S}'$-graded module. Then (with the

<!-- original page 109 -->

same hypotheses of finiteness on $\mathcal{S}$ and $\mathcal{M}$) one concludes from `(2.4.1)` that $\oplus_{k \in
\mathbb{Z}} R^{p} f_{*}(\mathcal{M}_{k})$ is an $\mathcal{S}$-module of finite type for every $p$, and (under the
additional hypotheses of `(2.4.1, (ii))`) that there exists $N$ such that for $n \geq N$, one has $R^{p}
f_{*}(\mathcal{M}_{k}(n)) = 0$ for every $p > 0$ and every $k \in \mathbb{Z}$, and that the canonical homomorphism
$f^{*}(f_{*}(\mathcal{M}_{k}(n))) \to \mathcal{M}_{k}(n)$ is surjective for every $k \in \mathbb{Z}$.

## 2.5. Euler–Poincaré characteristic and the Hilbert polynomial

**2.5.1.**

<!-- label: III.2.5.1 -->

Let $A$ be an Artinian ring, $X$ an $A$-scheme projective over $Y = \operatorname{Spec}(A)$. For every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, the $H^{i}(X, \mathcal{F})$ ($i \geq 0$) are $A$-modules of finite type
`(2.2.1)`, hence here of *finite length* since $A$ is Artinian. One knows in addition `(2.2.1)` that $H^{i}(X,
\mathcal{F}) = 0$ except for a finite number of values of $i \geq 0$; the integer

```text
  χ_A(ℱ) = Σ_{i=0}^∞ (−1)^i long(H^i(X, ℱ))                                  (2.5.1.1)
```

is thus defined for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$. When $A$ is an Artinian *local* ring, one
says that $\chi_{A}(\mathcal{F})$ is the *Euler–Poincaré characteristic of $\mathcal{F}$* (with respect to the ring
$A$). For $\mathcal{F} = \mathcal{O}_{X}$, one says that $\chi_{A}(\mathcal{O}_{X})$ is the *arithmetic genus* of $X$
(with respect to $A$).

**Proposition (2.5.2).**

<!-- label: III.2.5.2 -->

*Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence of coherent
$\mathcal{O}_{X}$-modules; one then has*

$$ \chi_{A}(\mathcal{F}) = \chi_{A}(\mathcal{F}') + \chi_{A}(\mathcal{F}''). (2.5.2.1) $$

**Proof.** As the cohomology modules of $\mathcal{F}'$, $\mathcal{F}$, $\mathcal{F}''$ are zero except for a finite
number of them, there is an integer $r > 0$ such that the exact cohomology sequence is written

```text
  0 → H^0(X, ℱ') → H^0(X, ℱ) → H^0(X, ℱ'') → H^1(X, ℱ') → ⋯
       ⋯ → H^r(X, ℱ') → H^r(X, ℱ) → H^r(X, ℱ'') → 0.
```

Now, we know that in an exact sequence of $A$-modules of finite length, with `0` at both ends, the alternating sum of
the lengths is zero `(0, 11.10.1)`; applying this result, one immediately finds the formula `(2.5.2.1)`.

One notes that the result of `(2.5.2)` applies whenever one knows that $X$ is a quasi-compact $A$-scheme and that the
$A$-modules $H^{i}(X, \mathcal{F})$ are of finite type for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$
`(1.4.12)`.

**Theorem (2.5.3).**

<!-- label: III.2.5.3 -->

*Let $A$ be an Artinian local ring, $X$ a scheme projective over $Y = \operatorname{Spec}(A)$, $\mathcal{L}$ an
invertible $\mathcal{O}_{X}$-module very ample relative to $Y$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-module; set
$\mathcal{F}(n) = \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ for every $n \in \mathbb{Z}$.*

*(i) There exists a unique polynomial $P \in \mathbb{Q}[T]$ such that $\chi_{A}(\mathcal{F}(n)) = P(n)$ for every $n \in
\mathbb{Z}$ (one says that $P$ is the *Hilbert polynomial of $\mathcal{F}$ with respect to $A$*).*

*(ii) For $n$ large enough, one has $\chi_{A}(\mathcal{F}(n)) = long_{A} \Gamma(X, \mathcal{F}(n))$.*

*(iii) The leading coefficient of $\chi_{A}(\mathcal{F}(n))$ is $\geq 0$.*

Let us add that in Chap. IV, in the paragraph devoted to the notion of dimension, we shall in addition show that *the
degree of $\chi_{A}(\mathcal{F}(n))$ is equal to the dimension of the support of $\mathcal{F}$*.

**Proof.** As one has $H^{i}(X, \mathcal{F}(n)) = 0$ for every $i > 0$ as soon as $n$ is large enough `(2.2.1)`,

<!-- original page 110 -->

one has $\chi_{A}(\mathcal{F}(n)) = long H^{0}(X, \mathcal{F}(n)) = long \Gamma(X, \mathcal{F}(n))$ for $n$ large
enough, whence (ii); this implies $\chi_{A}(\mathcal{F}(n)) \geq 0$ for $n$ large enough, and (iii) thus follows from
(i); as moreover the assertion of uniqueness in (i) is immediate, it remains to prove the existence of the polynomial
$P$.

Let us first show that one may suppose $\mathfrak{m} \mathcal{F} = 0$, where $\mathfrak{m}$ is the maximal ideal of $A$.
Indeed, there exists an integer $s > 0$ such that $\mathfrak{m}^{s} = 0$, and $\mathcal{F}(n)$ thus admits a finite
filtration

```text
  ℱ(n) ⊃ 𝔪 ℱ(n) ⊃ ⋯ ⊃ 𝔪^{s−1} ℱ(n) ⊃ 0.
```

By induction, one deduces from `(2.5.2.1)` that

```text
  χ_A(ℱ(n)) = Σ_{k=1}^s χ_A(𝔪^{k−1} ℱ(n) / 𝔪^k ℱ(n));
```

since $\mathfrak{m}^{k-1} \mathcal{F}(n) / \mathfrak{m}^{k} \mathcal{F}(n) = \mathcal{F}'_{k}(n)$, where
$\mathcal{F}'_{k} = \mathfrak{m}^{k-1} \mathcal{F} / \mathfrak{m}^{k} \mathcal{F}$, this proves our assertion.

So suppose $\mathfrak{m} \mathcal{F} = 0$; if $X'$ is the closed subscheme of $X$, inverse image by the structure
morphism $X \to \operatorname{Spec}(A)$ of the unique closed point of $\operatorname{Spec}(A)$, and $j : X' \to X$ the
canonical injection, one has $\mathcal{F} = j_{*}(\mathcal{F}')$, where $\mathcal{F}'$ is a coherent
$\mathcal{O}_{X'}$-module; $X'$ is a scheme projective over $\operatorname{Spec}(K)$, where $K = A/\mathfrak{m}$. If
$\mathcal{L}' = j^{*}(\mathcal{L})$, $\mathcal{L}'$ is very ample relative to $\operatorname{Spec}(K)$ `(II, 4.4.10)`,
and one has $\mathcal{F}(n) = j_{*}(\mathcal{F}'(n))$, where $\mathcal{F}'(n) = \mathcal{F}' \otimes_{\mathcal{O}_{X'}}
\mathcal{L}'^{\otimes n}$ $(0_{I}, 5.4.10)$. One concludes that $\chi_{A}(\mathcal{F}(n)) = \chi_{K}(\mathcal{F}'(n))$
`(G, II, 4.9.1)`, and one is thus reduced to the case where $A$ is a *field*.

Note now that $X$ can be considered as a closed subscheme of $P = \mathbb{P}^{r}_{A}$ for a suitable $r$
`(II, 5.5.4, (ii))`; if $i : X \to P$ is the canonical injection, one sees as above that one has
$\chi_{A}(\mathcal{F}(n)) = \chi_{A}(i_{*}(\mathcal{F})(n))$, so that one may restrict to the case where $X =
\mathbb{P}^{r}_{A} = \operatorname{Proj}(S)$ with $S = A[T_{0}, \cdots, T_{r}]$, $A$ being a field.

This being so, one has $\mathcal{F} = \tilde{M}$, where $M$ is a graded $S$-module of finite type `(II, 2.7.8)`; there
exists consequently a finite resolution of $M$ by graded free $S$-modules of finite type

```text
  0 → L_q → L_{q−1} → ⋯ → L_1 → M → 0
```

by virtue of Hilbert's syzygy theorem `(M, VIII, 6.5)`; as $M \mapsto \tilde{M}$ is an exact functor in $M$
`(II, 2.5.4)`, one also has an exact sequence

```text
  0 → L̃_q → L̃_{q−1} → ⋯ → L̃_1 → M̃ → 0
```

and consequently, for every $n \in \mathbb{Z}$, the sequence

```text
  0 → L̃_q(n) → L̃_{q−1}(n) → ⋯ → L̃_1(n) → M̃(n) → 0
```

is exact; applying by induction on $q$ Proposition `(2.5.1)`, it comes

```text
  χ_A(M̃(n)) = Σ_{i=1}^q (−1)^{i+1} χ_A(L̃_i(n))
```

and to prove (i), one is therefore reduced to the case where $M$ is free and graded of finite type, hence to the case
where $M = S(h)$ for an $h \in \mathbb{Z}$. As we then have $\tilde{M}(n) = (M(n))\sim = (S(n + h))\sim$ `(II, 2.5.15)`,
one finally sees that the theorem will follow from the following.

<!-- original page 111 -->

**Lemma (2.5.3.1).**

<!-- label: III.2.5.3.1 -->

*Let $A$ be a field, $r$ an integer `> 0`, and $X = \mathbb{P}^{r}_{A}$; one then has $\chi_{A}(\mathcal{O}_{X}(n)) =
(n+r choose r)$ for every $n \in \mathbb{Z}$.*

**Proof.** Indeed, for $n \geq 0$, one has $\chi_{A}(\mathcal{O}_{X}(n)) = long H^{0}(X, \mathcal{O}_{X}(n))$, which is
the number of monomials in the $T_{i}$ of total degree $n$, that is, $(n+r choose r)$ `(2.1.12)`. For $n \leq -r - 1$,
one has similarly $\chi_{A}(\mathcal{O}_{X}(n)) = (-1)^{r} long H^{r}(X, \mathcal{O}_{X}(n))$; if $n = -r - h$, the
dimension of $H^{r}(X, \mathcal{O}_{X}(n))$ over $A$ is the number of sequences $(p_{i})_{0 \leq i \leq r}$ of integers
$p_{i} > 0$ such that $\Sigma^{r}_{i=0} p_{i} = r + h$ `(2.1.12)`, or equivalently the number of sequences of integers
$q_{i} \geq 0$ ($0 \leq i \leq r$) such that $\Sigma^{r}_{i=0} q_{i} = h - 1$; this is therefore the number $(h-1+r
choose r) = (-1)^{r} (n+r choose r)$. Finally, for $-r \leq n \leq 0$, one has $(n+r choose r) = 0$ and on the other
hand $H^{i}(X, \mathcal{O}_{X}(n)) = 0$ for every $i \geq 0$ `(2.1.12)`, which proves the lemma.

**Corollary (2.5.4).**

<!-- label: III.2.5.4 -->

*Let $A$ be an Artinian local ring, $S$ a graded $A$-algebra of finite type generated by `S_1`, $M$ a graded $S$-module
of finite type, $X = \operatorname{Proj}(S)$. One then has $\chi_{A}(\tilde{M}(n)) = long M_{n}$ for $n$ large enough.*

**Proof.** This follows from the fact that $M_{n}$ and $\Gamma(X, \tilde{M}(n))$ are isomorphic for $n$ large enough
`(2.3.1)`.

## 2.6. Application: ampleness criteria

**Proposition (2.6.1).**

<!-- label: III.2.6.1 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module. The following conditions are equivalent:*

*a) $\mathcal{L}$ is ample for $f$.*

*b) For every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, there exists an integer $N$ such that for $n \geq N$, one
has $R^{q} f_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n}) = 0$ for every $q > 0$.*

*c) For every coherent ideal sheaf $\mathcal{J}$ of $\mathcal{O}_{X}$, there exists an integer $N$ such that for $n \geq
N$ one has $R^{1} f_{*}(\mathcal{J} \otimes \mathcal{L}^{\otimes n}) = 0$.*

**Proof.** We have seen that a) entails b) `(2.2.1, (ii))`. It is trivial that b) entails c), and it remains to prove
that c) implies a). One may restrict to the case where $Y$ is affine `(II, 4.6.4)`, and prove in this case that
$\mathcal{L}$ is ample; it will suffice to show that as $h$ runs over the set of sections of the $\mathcal{L}^{\otimes
n}$ ($n > 0$) over $X$, those of the $X_{h}$ which are affine form a cover of $X$ `(II, 4.5.2)`. For this, let us show
that for every closed point $x$ of $X$ and every affine open neighbourhood $U$ of $x$, there exist an $n$ and an $h \in
\Gamma(X, \mathcal{L}^{\otimes n})$ such that $x \in X_{h} \subset U$; $X_{h}$ will necessarily be affine `(I, 1.3.6)`
and the union of these $X_{h}$ will be an open set of $X$ containing all the closed points of $X$, and consequently $X$
itself, since $X$ is Noetherian $(I, 6.3.7 and 0_{I}, 2.1.3)$. Let $\mathcal{J}$ (resp. $\mathcal{J}'$) be the
quasi-coherent ideal sheaf of $\mathcal{O}_{X}$ defining the closed reduced subprescheme of $X$ having for underlying
space $X - U$ (resp. $(X - U) \cup {x}$) `(I, 5.2.1)`; it is clear that $\mathcal{J}$ and $\mathcal{J}'$ are coherent
`(I, 6.1.1)`, that $\mathcal{J}' \subset \mathcal{J}$, and that $\mathcal{J}'' = \mathcal{J} / \mathcal{J}'$ is a
coherent $\mathcal{O}_{X}$-module $(0_{I}, 5.3.3)$ with support ${x}$ and such that $\mathcal{J}''_{x} = \kappa(x)$. As
$\mathcal{L}$ is locally free, the sequence $0 \to \mathcal{J}' \otimes \mathcal{L}^{\otimes n} \to \mathcal{J} \otimes
\mathcal{L}^{\otimes n} \to \mathcal{J}'' \otimes \mathcal{L}^{\otimes n} \to 0$ is exact for every $n$, and by
hypothesis there exists $n$ large enough such that $H^{1}(X, \mathcal{J}' \otimes \mathcal{L}^{\otimes n}) = 0$; the
exact cohomology sequence

<!-- original page 112 -->

therefore proves that the homomorphism $\Gamma(X, \mathcal{J} \otimes \mathcal{L}^{\otimes n}) \to \Gamma(X,
\mathcal{J}'' \otimes \mathcal{L}^{\otimes n})$ is surjective. A section $g$ of $\mathcal{J}'' \otimes
\mathcal{L}^{\otimes n}$ over $X$ such that $g(x) \neq 0$ is therefore the image of a section $h \in \Gamma(X,
\mathcal{J} \otimes \mathcal{L}^{\otimes n}) \subset \Gamma(X, \mathcal{L}^{\otimes n})$ (since by virtue of $(0_{I},
5.4.1)$, $\mathcal{J} \otimes \mathcal{L}^{\otimes n}$ is a sub-$\mathcal{O}_{X}$-module of $\mathcal{L}^{\otimes n}$);
one has by definition $h(x) \neq 0$ and $h(z) = 0$ for $z \notin U$, which completes the proof.

**Proposition (2.6.2).**

<!-- label: III.2.6.2 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a morphism of finite type, $g : X' \to X$ a finite surjective
morphism, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module and $\mathcal{L}' = g^{*}(\mathcal{L})$. Suppose the
following condition is satisfied: there exists a subset $Z$ of $X$, proper over $Y$ `(II, 5.4.10)`, such that for every
$x \in X - Z$, either $X$ is normal at the point $x$, or $(g_{*}(\mathcal{O}_{X'}))_{x}$ is a free
$\mathcal{O}_{x}$-module. Under these conditions, for $\mathcal{L}$ to be ample for $f$, it is necessary and sufficient
that $\mathcal{L}'$ be ample for $f \circ g$.*

**Proof.**

**(2.6.2.1)**

<!-- label: III.2.6.2.1 -->

Since $g$ is affine, the condition is necessary `(II, 5.1.12)`. To see that it is sufficient, one may suppose $Y$ affine
`(II, 4.6.4)`. Let us further show that one may restrict to the case where $X$ is reduced. Indeed, let $j : X_{red} \to
X$ be the canonical injection, and set $X_{1} = X_{red}$, $X'_{1} = X' \times_{X} X_{1}$, so that one has the
commutative diagram

```text
         j'
    X' ←───── X'_1
    |          |
  g |          | g_1
    ↓          ↓
    X  ←───── X_1
         j

                                                                              (2.6.2.2)
```

The morphism $f \circ j$ is then of finite type `(I, 6.3.4)` and $g_{1}$ is a finite morphism `(II, 6.1.5, (iii))`; if
$\mathcal{L}'$ is ample for $f \circ g$, $j'^{*}(\mathcal{L}')$ is ample for $f \circ g \circ j'$ since $j'$ is a closed
immersion `(II, 5.1.12 and I, 4.3.2)`. If one sets $Z_{1} = j^{-1}(Z)$, `Z_1` is proper over $Y$ `(II, 5.4.10)`; on the
other hand, if $X$ is normal at a point $x$, the same is evidently true of $X_{red}$; finally, if
$(g_{*}(\mathcal{O}_{X'}))_{x}$ is a free $\mathcal{O}_{x}$-module, it follows at once from `(II, 1.5.2)` that
$((g_{1})_{*}(\mathcal{O}_{X'_{1}}))_{x}$ is a free $\mathcal{O}_{X_{1}, x}$-module. Finally, since $X$ is Noetherian
`(I, 6.3.7)`, if $j^{*}(\mathcal{L})$ is ample, $\mathcal{L}$ is ample `(II, 4.5.14)`, and as $j'^{*}(\mathcal{L}') =
g^{*}_{1}(j^{*}(\mathcal{L}))$, this completes the reduction announced. We therefore suppose henceforth $Y$ affine and
$X$ reduced.

The hypotheses of `(II, 6.6.11)` then being verified, there exists a reduced $Y$-prescheme `X_2` and a $Y$-morphism $h :
X_{2} \to X$ finite and birational such that the restriction of $h$ to $h^{-1}(X - Z)$ is an isomorphism onto $X - Z$
and that $h^{*}(\mathcal{L})$ is ample. Replacing $X'$ by `X_2`, one sees that one is reduced to proving the proposition
supposing in addition that $g$ has the properties just enumerated for $h$. We shall again denote by $Z$ a sub-prescheme
of $X$ having $Z$ for underlying space, which is proper over $Y$ `(II, 5.4.10)`.

**(2.6.2.3)**

<!-- label: III.2.6.2.3 -->

Let now `X_1` be a closed sub-prescheme of $X$, $j : X_{1} \to X$ the canonical injection, $X'_{1} = g^{-1}(X_{1}) = X'
\times_{X} X_{1}$ its inverse image, $j' : X'_{1} \to X'$ the canonical injection, so that one has the commutative
diagram `(2.6.2.2)`; set $\mathcal{L}_{1} = j^{*}(\mathcal{L})$, $\mathcal{L}'_{1} = j'^{*}(\mathcal{L}') =
g^{*}_{1}(\mathcal{L}_{1})$, so that $\mathcal{L}'_{1}$ is ample for $f \circ g \circ j'$ `(II, 5.1.12)`. If one sets
$Z_{1} = j^{-1}(Z)$, the closed sub-prescheme `Z_1` of `X_1` is proper over $Y$ `(II, 5.4.2, (ii))`. In other words, the
hypotheses of `(2.6.2)` are verified for `X_1`, $\mathcal{L}_{1}$, $g_{1}$, and `Z_1`.

<!-- original page 113 -->

This will allow us to prove `(2.6.2)` by Noetherian induction $(0_{I}, 2.2.2)$ in the case where the restriction of $g$
to $g^{-1}(X - Z)$ is an isomorphism onto $X - Z$ (which is sufficient for our purpose, as one has seen in `(2.6.2.2)`):
it will suffice to establish that if, for every closed sub-prescheme `X_1` of $X$ whose underlying space is $\neq X$,
the conclusion of `(2.6.2)` is true for the sheaf $\mathcal{L}_{1}$, then it is also true for the sheaf $\mathcal{L}$.

**(2.6.2.4)**

<!-- label: III.2.6.2.4 -->

Let then $\mathcal{A} = \mathcal{O}_{X}$, $\mathcal{B} = g_{*}(\mathcal{O}_{X'})$, so that $\mathcal{B}$ is a
sub-$\mathcal{A}$-algebra of $\mathcal{R}(X)$, which is a coherent $\mathcal{A}$-module; in addition, the restriction
$\mathcal{B} \mid (X - Z)$ is equal to $\mathcal{A} \mid (X - Z)$. Let $\mathcal{K}$ be the *conductor* of $\mathcal{B}$
over $\mathcal{A}$, that is, the largest sub-$\mathcal{A}$-module quasi-coherent of $\mathcal{A}$ such that
$\mathcal{B} \cdot \mathcal{K} \subset \mathcal{A}$ (or equivalently the *annihilator* of the $\mathcal{A}$-module
$\mathcal{B} / \mathcal{A}$ $(0_{I}, 5.3.7)$), which entails $\mathcal{B} \cdot \mathcal{K} = \mathcal{K}$. It is clear
that $\mathcal{B}_{z} = \mathcal{A}_{z}$ at every point admitting a neighbourhood $W_{z}$ such that $g$ is an
isomorphism of $g^{-1}(W_{z})$ onto $W_{z}$, and in particular at every point of $X - Z$ and in a neighbourhood of every
generic point of an irreducible component of $X$. Consider then the closed sub-prescheme
$Z_{1} = \operatorname{Spec}(\mathcal{A} / \mathcal{K})$ of $X$ defined by $\mathcal{K}$; it is still proper over $Y$,
since the sub-space `Z_1` is closed in $Z$ `(II, 5.4.10)`. Moreover, the definition of $\mathcal{K}$ shows that
$\mathcal{B} \mid (X - Z_{1}) = \mathcal{A} \mid (X - Z_{1})$; one thus sees that one can always reduce to the case
where $Z = \operatorname{Spec}(\mathcal{A} / \mathcal{K})$, and as we have seen that $X - Z_{1}$ is a nonempty open set
of $X$, one may always suppose that the space $Z$ is distinct from $X$.

**(2.6.2.5)**

<!-- label: III.2.6.2.5 -->

Consider $X'$ as equal to $\operatorname{Spec}(\mathcal{B})$ (since $g$ is affine) and let $\mathcal{K}' =
\tilde{\mathcal{K}}$, a coherent ideal sheaf of $\mathcal{O}_{X'}$ such that $g_{*}(\mathcal{K}') = \mathcal{K}$
`(II, 1.4.1)`; the closed sub-prescheme $Z' = g^{-1}(Z) = Z \times_{X} X'$ of $X'$ is defined by $\mathcal{K}'$ and
equal to $\operatorname{Spec}(\mathcal{B}/\mathcal{K})$ `(II, 1.4.10)`; as $h : Z' \to Z$ is a finite morphism
`(II, 6.1.5, (iii))`, $Z'$ is proper over $Y$ `(II, 6.1.11 and 5.4.2, (ii))`.

This being so, we must prove that for every $x \in X$ and every open neighbourhood $U$ of $x$, there exists a section
$s$ of an $\mathcal{L}^{\otimes n}$ ($n > 0$) over $X$ such that $x \in X_{s} \subset U$ `(II, 4.5.2)`; we distinguish
two cases:

1° One has $x \in X - Z$; one may evidently then suppose that one also has $U \subset X - Z$, so the open set $U' =
g^{-1}(U)$ does not meet $Z'$. As $\mathcal{L}'$ is ample by hypothesis, there exist an $n > 0$ and a section $s'$ of
$\mathcal{L}'^{\otimes n}$ over $X'$ such that $x' = g^{-1}(x) \in X'_{s'} \subset g^{-1}(U)$ `(II, 4.5.2)`. In
addition, one may suppose that $\mathcal{K}' \otimes \mathcal{L}'^{\otimes n}$ is generated by its sections over $X'$
`(II, 4.5.5)`, so, since $\mathcal{K}'_{x'} = \mathcal{O}_{x'}$, there is a section `s''` of these such that $s''(x')
\neq 0$; multiplying it by $s'$ (which amounts to replacing $n$ by `2n`), one sees that one may also suppose that $x'
\in X'_{s''} \subset g^{-1}(U)$. This being so, it follows from $(0_{I}, 5.4.10)$ that one has a canonical isomorphism

```text
  Γ(X, 𝒦 ⊗ ℒ^{⊗n}) ⥲ Γ(X', 𝒦' ⊗ ℒ'^{⊗n}).
```

The section $s$ of $\mathcal{K} \otimes \mathcal{L}^{\otimes n}$ corresponding to `s''` under this isomorphism evidently
has the desired properties.

2° One has $x \in Z$. Let $\mathcal{J}$ be the coherent ideal sheaf of $\mathcal{O}_{X}$ defining the closed reduced
sub-prescheme of $X$ having for underlying space $X - U$, and consider in $\mathcal{B}$ the coherent ideals

<!-- original page 114 -->

$\mathcal{J} \mathcal{B}$ and $\mathcal{J}_{1} = \mathcal{J} \mid (\mathcal{J} \mathcal{B} \cap \mathcal{A}) =
\mathcal{J}(\mathcal{J} \mathcal{B})$, so that one has the diagram of inclusions

```text
   𝒥 ℬ    →    ℬ
   ↑           ↑
   𝒥     →    𝒜
   ↑           ↑
   𝒥 𝒦 ℬ = 𝒥 𝒦  →   𝒦                                                       (2.6.2.6)
```

Let $\mathcal{J}'$ be the coherent ideal sheaf $(\mathcal{J} \mathcal{B})\sim$ of $\mathcal{O}_{X'}$, so that
$\mathcal{J} \mathcal{B} = g_{*}(\mathcal{J}')$, $\mathcal{J} \mathcal{K} = (\mathcal{J} \mathcal{K}')\sim$, and
consequently $\mathcal{J}' / \mathcal{J}' \mathcal{K}' = (\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K}
\mathcal{B})\sim$ `(II, 1.4.4)`. As $\mathcal{J} \mid V = \mathcal{J} \mathcal{K} \mid V$ for every open set $V$ not
meeting $Z$, one sees that the support of $\mathcal{J}' / \mathcal{J}' \mathcal{K}'$ is contained in $Z'$. As $Z'$ is
proper over $Y$, one may apply `(2.2.4)` and one sees that for $n$ large enough, the canonical map

```text
  Γ(X', 𝒥' ⊗ ℒ'^{⊗n}) → Γ(X', (𝒥' / 𝒥' 𝒦') ⊗ ℒ'^{⊗n})
```

is surjective.

But by virtue of $(0_{I}, 5.4.10)$, one concludes that the canonical map

```text
  Γ(X, 𝒥 ℬ ⊗ ℒ^{⊗n}) → Γ(X, (𝒥 ℬ / 𝒥 𝒦 ℬ) ⊗ ℒ^{⊗n})
```

is surjective.

This being so, let $i : Z \to X$ be the canonical injection, $i' : Z' \to X'$ the canonical injection, so that one has
the commutative diagram

```text
         i'
    X' ←───── Z'
    |          |
  g |          | h
    ↓          ↓
    X  ←───── Z
         i
```

Let $\mathcal{M} = i^{*}(\mathcal{L})$, $\mathcal{M}' = i'^{*}(\mathcal{L}')$; as $\mathcal{L}'$ is ample,
$\mathcal{M}'$ is ample `(II, 5.1.12)`, and on the other hand $\mathcal{M}' = h^{*}(\mathcal{M})$; one concludes
therefore from the hypothesis of Noetherian induction (since $Z \neq X$) that $\mathcal{M}$ is ample. Consequently
$i^{*}((\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K}) \otimes \mathcal{L}^{\otimes n})$ is generated by its
sections over $Z$ for $n$ large enough `(II, 4.5.5)`. As $\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K} =
i_{*}(i^{*}(\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K}))$, one deduces again from $(0_{I}, 5.4.10)$ that there
exists a section $s$ of $(\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K}) \otimes \mathcal{L}^{\otimes n}$ over $X$
(for $n$ large enough) such that $s(x) \neq 0$, since one has $\mathcal{B}_{x} = \mathcal{A}_{x}$ by definition of $Z$
and $\mathcal{K}_{x} \neq \mathcal{A}_{x}$ by hypothesis. The diagram `(2.6.2.6)` shows that $s$ is also a section of
$(\mathcal{J} \mathcal{B} / \mathcal{J} \mathcal{K} \mathcal{B}) \otimes \mathcal{L}^{\otimes n}$ over $X$, hence $s$ is
the canonical image of a section $t$ of $\mathcal{J} \mathcal{B} \otimes \mathcal{L}^{\otimes n}$ over $X$. But by
definition, the canonical image $s$ of $t$ mod $(\mathcal{J} \mathcal{K} \mathcal{B}) \otimes \mathcal{L}^{\otimes n}$
is in $(\mathcal{J} \otimes \mathcal{L}^{\otimes n}) / ((\mathcal{J} \mathcal{K} \mathcal{B}) \otimes
\mathcal{L}^{\otimes n})$, hence by virtue of `(2.6.2.6)`, this implies that $t$ is a *section of $\mathcal{J} \otimes
\mathcal{L}^{\otimes n}$* over $X$, and *a fortiori* a section of $\mathcal{L}^{\otimes n}$. One has seen above that
$t(x) \neq 0$, so $x \in X_{t}$, and by definition of $\mathcal{J}$, $t(y) = 0$ in $X - U$ which is the support of
$\mathcal{O}_{X} / \mathcal{J}$; thus $X_{t} \subset U$, which completes the proof.

**Remark (2.6.3).**

<!-- label: III.2.6.3 -->

When $X$ is proper over $Y$, one can prove `(2.6.2)` more simply, by reasoning as in Chevalley's theorem `(II, 6.7.1)`,
using `(2.6.1)` and Lemma `(II, 6.7.1.1)`.
