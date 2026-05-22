# §4. The fundamental theorem of proper morphisms; applications

<!-- original page 122 -->

## 4.1. The fundamental theorem

**(4.1.1)**

<!-- label: III.4.1.1 -->

Let $X$, $Y$ be two usual Noetherian preschemes, $f : X \to Y$ a proper morphism, $Y'$ a closed subset of $Y$, and $X'$
its inverse image $f^{-1}(Y')$. We denote by $\mathfrak{X}$ and $\mathfrak{Y}$ the formal preschemes $X_{/X'}$ and
$Y_{/Y'}$, the completions of $X$ and $Y$ along $X'$ and $Y'$ respectively `(I, 10.8.5)`; we write $\hat{\mathit{f}}$
for the extension of $f$ to these completions `(I, 10.9.1)`, which is a morphism $\mathfrak{X} \to \mathfrak{Y}$ of
formal preschemes. For every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, we denote by $\hat{\mathcal{F}}$ its
completion along $X'$ `(I, 10.8.4)`, which is a coherent $\mathcal{O}_{\mathfrak{X}}$-module `(I, 10.8.8)`.

<!-- original page 123 -->

**(4.1.2)**

<!-- label: III.4.1.2 -->

Let $\mathcal{J}$ be a coherent ideal of $\mathcal{O}_{Y}$ such that $Supp(\mathcal{O}_{Y}/\mathcal{J}) = Y'$
`(I, 5.2.1)`; we know `(I, 4.4.5)` that $\mathcal{K} = f^{*}(\mathcal{J}) \mathcal{O}_{X}$ is a coherent ideal of
$\mathcal{O}_{X}$ such that

$$ Supp(\mathcal{O}_{X} / \mathcal{K}) = X'. $$

We consider, for every $k \geq 0$, the coherent $\mathcal{O}_{X}$-modules

```text
  ℱ_k = ℱ / 𝒦^{k+1} ℱ.
```

The $\mathcal{O}_{Y}$-modules $R^{n} f_{*}(\mathcal{F})$ and $R^{n} f_{*}(\mathcal{F}_{k})$ are coherent for every $n$
(3.2.1). For every $k' \geq k$ and every $n$, the canonical homomorphism $\mathcal{F}_{k'} \to \mathcal{F}_{k}$ defines
by functoriality a homomorphism

```text
  R^n f_*(ℱ_{k'}) → R^n f_*(ℱ_k).                                            (4.1.2.1)
```

Moreover, since $\mathcal{F}_{k}$ is an $\mathcal{O}_{X} / \mathcal{K}^{k+1}$-module, $R^{n} f_{*}(\mathcal{F}_{k})$ is
an $\mathcal{O}_{Y} / \mathcal{J}^{k+1}$-module $(0_{III}, 12.2.1)$, and one deduces from (4.1.2.1) a homomorphism

```text
  R^n f_*(ℱ_{k'}) ⊗_{𝒪_Y} (𝒪_Y / 𝒥^{k+1}) → R^n f_*(ℱ_k).                    (4.1.2.2)
```

The two sides of (4.1.2.2) form two projective systems, and the projective limit of the first side is none other than
the completion $(R^{n} f_{*}(\mathcal{F}))_{/Y'}$ which we shall denote $(R^{n} f_{*}(\mathcal{F}))^{\wedge}$.
Furthermore, it is immediate that the homomorphisms (4.1.2.2) form a projective system, whence by passage to the limit a
canonical homomorphism

```text
  φ_n : (R^n f_*(ℱ))^∧ → lim_← R^n f_*(ℱ_k).                                 (4.1.2.3)
                          k
```

Moreover, (4.1.2.2) is a homomorphism of $(\mathcal{O}_{Y} / \mathcal{J}^{k+1})$-modules, and therefore `(I, 10.8.3)`
may be considered as a continuous homomorphism of pseudo-discrete topological $\mathcal{O}_{\mathfrak{Y}}$-modules
$(0_{I}, 3.8.1)$. The homomorphism $\phi_{n}$ is consequently a continuous homomorphism of topological
$\mathcal{O}_{\mathfrak{Y}}$-modules.

**(4.1.3)**

<!-- label: III.4.1.3 -->

Let $i : \mathfrak{X} \to X$ be the canonical morphism of ringed spaces defined in `(I, 10.8.7)`, so that we have the
commutative diagram

$$ X_{k} \to^{h_{k}} X \downarrow f_{k} \downarrow f (4.1.3.1) Y_{k} \to Y $$

where $X_{k}$ is the closed subprescheme of $X$ defined by the ideal $\mathcal{K}^{k+1}$, $i_{k}$ the canonical
injection, $h_{k}$ the morphism of ringed spaces corresponding to the identity on the underlying spaces and to the
canonical homomorphism $\mathcal{O}_{X} \to \mathcal{O}_{X} / \mathcal{K}^{k+1}$ `(I, 10.5.2)`. Moreover, we have
$\hat{\mathcal{F}} = i^{*}(\mathcal{F})$ `(I, 10.8.8)` up to canonical isomorphism. We know that

```text
  H^n(X_k, ℱ_k) = H^n(X, ℱ_k)                                                (4.1.3.2)
```

up to canonical isomorphism, since $\mathcal{F}_{k} = (h_{k})_{*}((i_{k})^{*}(\mathcal{F}_{k}))$ $(0_{I}, 4.9.1)$; the
canonical homomorphism $H^{n}(X, \mathcal{F}) \to H^{n}(X_{k}, \mathcal{F}_{k})$ $(0_{III}, 12.1.3.5)$ thus also reads

```text
  H^n(X, ℱ) → H^n(X, ℱ_k),                                                   (4.1.3.3)
```

and these homomorphisms obviously form a projective system, whence by passage to the limit a canonical homomorphism

```text
  ψ_X : H^n(X, ℱ) → lim_← H^n(X, ℱ_k).                                       (4.1.3.4)
                      k
```

<!-- original page 124 -->

Replacing $X$ by an open set of the form $f^{-1}(V)$, where $V$ is an affine open set of $Y$, and taking (1.4.11) into
account, we have homomorphisms

```text
  ψ_V : H^n(X ∩ f^{-1}(V), ℱ) → lim_← Γ(V, R^n f_*(ℱ_k));                    (4.1.3.5)
                                  k
```

these homomorphisms obviously commute with restriction from $V$ to a smaller affine open set, and therefore finally
define a canonical homomorphism of sheaves

```text
  ψ : R^n f_*(ℱ) → lim_← R^n f_*(ℱ_k).                                       (4.1.3.6)
                     k
```

**(4.1.4)**

<!-- label: III.4.1.4 -->

Let finally $j : \mathfrak{Y} \to Y$ be the canonical morphism of ringed spaces `(I, 10.8.7)`; since $R^{n}
f_{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{Y}$-module (3.2.1), we have $j^{*}(R^{n} f_{*}(\mathcal{F})) = (R^{n}
f_{*}(\mathcal{F}))^{\wedge}$ up to canonical isomorphism `(I, 10.8.8)`, and we therefore have a canonical homomorphism

```text
  ρ_n : (R^n f_*(ℱ))^∧ = j^*(R^n f_*(ℱ)) → R^n 𝑓̂_*(j^*(ℱ)) = R^n 𝑓̂_*(ℱ̂),     (4.1.4.1)
```

defined in general for ringed spaces (see the proof of `(1.4.15)`). We show that the diagram

```text
  (R^n f_*(ℱ))^∧ ────→ R^n 𝑓̂_*(ℱ̂)
        ↓ φ_n             ↑ ψ_n                                              (4.1.4.2)
        lim_← R^n f_*(ℱ_k)
          k
```

is commutative. It clearly suffices to prove the commutativity of the corresponding diagram of homomorphisms of
presheaves, so we may restrict to the case where $Y$ is affine, and everything reduces to proving that the diagram

```text
  (H^n(X, ℱ))^∧ ────→ H^n(𝔛, ℱ̂)
        ↓ φ_n           ↑ ψ_{n,𝔛}                                            (4.1.4.3)
        lim_← H^n(X, ℱ_k)
          k
```

is commutative. But the commutativity of (4.1.3.1) and the relations seen in (4.1.3) between the cohomology groups give
at once the commutative diagram

```text
  H^n(X, ℱ) ────→ H^n(𝔛, ℱ̂) = H^n(𝔛, i^*(ℱ))
         ╲         ╱
          H^n(X_k, ℱ_k) = H^n(X, ℱ_k)
```

whence we deduce immediately the commutativity of (4.1.4.3).

**Theorem (4.1.5).**

<!-- label: III.4.1.5 -->

*Let $f : X \to Y$ be a proper morphism of Noetherian preschemes, $Y'$ a closed subset of $Y$, $X' = f^{-1}(Y')$. Then,
for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, $R^{n} \hat{\mathit{f}}_{*}(\hat{\mathcal{F}})$ is a coherent
$\mathcal{O}_{\mathfrak{Y}}$-module, and the homomorphisms $\phi_{n}$, $\psi_{n}$, and $\rho_{n}$ of the diagram
(4.1.4.2) are topological isomorphisms.*

**Proof.** It clearly suffices to prove that $\phi_{n}$ and $\psi_{n}$ are isomorphisms; since $R^{n}
f_{*}(\mathcal{F})$ is coherent (3.2.1), it will follow that $(R^{n} f_{*}(\mathcal{F}))^{\wedge}$ is coherent
`(I, 10.8.8)`, and the bicontinuity of $\phi_{n}$, $\psi_{n}$, and $\rho_{n}$ is then automatic `(I, 10.11.6)`.

**Remarks (4.1.6).**

<!-- label: III.4.1.6 -->

(i) If we set $\hat{\mathcal{F}}_{k} = \hat{\mathcal{F}} / \hat{\mathcal{K}}^{k+1} \hat{\mathcal{F}}$, it is immediate
that $\hat{\mathcal{F}}_{k} = i^{*}(\mathcal{F}_{k})$, and the canonical homomorphism (4.1.3.6) is none other than the
homomorphism already defined in (3.4.2.2)

```text
  R^n 𝑓̂_*(ℱ̂) → lim_← R^n 𝑓̂_*(ℱ̂_k);                                          (4.1.6.1)
                 k
```

<!-- original page 125 -->

consequently, the fact that $\psi_{n}$ is an isomorphism is a particular case of (3.4.3). But we shall give below a
direct proof, avoiding the delicate considerations on projective limits of spectral sequences $(0_{III}, 13.7)$ on which
the general theorem (3.4.3) rests.

(ii) Taking account of the fact that the $\psi_{n}$ are isomorphisms, it is equivalent to say that the $\phi_{n}$ or the
$\rho_{n} = \psi_{n} \circ \phi^{-1}_{n}$ are isomorphisms. Theorem (4.1.5) expresses, among other things, that *the
formation of $R^{n} f_{*}(\mathcal{F})$ commutes with completion*, and may be called the *first comparison theorem
between the "algebraic" and "formal" theories*.

We shall begin by establishing the affine form of (4.1.5):

**Corollary (4.1.7).**

<!-- label: III.4.1.7 -->

*The hypotheses being those of (4.1.5), suppose in addition that $Y = \operatorname{Spec}(A)$, where $A$ is Noetherian,
and $\mathcal{J} = \tilde{\mathfrak{J}}$, where $\mathfrak{J}$ is an ideal of $A$, so that $\mathcal{F}_{k} =
\mathcal{F} / \mathfrak{J}^{k+1} \mathcal{F}$. The canonical homomorphism*

```text
  φ_n : (H^n(X, ℱ))^∧ → lim_← H^n(X, ℱ_k)                                    (4.1.7.1)
                          k
```

*(where the first member is the Hausdorff completion of $H^{n}(X, \mathcal{F})$ for the $\mathfrak{J}$-preadic topology)
is an isomorphism. The projective system $(H^{n}(X, \mathcal{F}_{k}))_{k \geq 0}$ satisfies condition (ML) for every
$n$, and the canonical homomorphism*

```text
  ψ_n : H^n(X, ℱ) → lim_← H^n(X, ℱ_k)                                        (4.1.7.2)
                       k
```

*is an isomorphism. Finally, the filtration on $H^{n}(X, \mathcal{F})$ defined by the kernels of the canonical
homomorphisms*

<!-- original page 126 -->

*$H^{n}(X, \mathcal{F}) \to H^{n}(X, \mathcal{F}_{k})$ is $\mathfrak{J}$-good $(0_{III}, 13.7.7)$, and $\psi_{n}$ is a
topological isomorphism* (1).

> (1) The following proof, simpler than the original proof, and the complement on the filtration of $H^{n}(X,
> \mathcal{F})$, were communicated to us by J.-P. Serre.

**Proof.** The integer $n \geq 0$ being fixed in this proof, we shall set for simplicity

```text
  H = H^n(X, ℱ),    H_k = H^n(X, ℱ_k),                                       (4.1.7.3)
  R_k = Ker(H → H_k),     a sub-`A`-module of `H`.                           (4.1.7.4)
```

The exact sequence of cohomology

```text
  H^n(X, 𝔍^{k+1} ℱ) → H^n(X, ℱ) → H^n(X, ℱ_k) → H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, ℱ)
```

shows that we also have $R_{k} = Im(H^{n}(X, \mathfrak{J}^{k+1} \mathcal{F}) \to H^{n}(X, \mathcal{F}))$; we shall set

```text
  Q_k = Ker(H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, ℱ))
      = Im(H^n(X, ℱ_k) → H^{n+1}(X, 𝔍^{k+1} ℱ)).                             (4.1.7.5)
```

We thus have the exact sequence

```text
  0 → R_k → H → H_k → Q_k → 0.                                               (4.1.7.6)
```

**(4.1.7.7).** Let $x$ be an element of $\mathfrak{J}^{r}$ ($r \geq 0$); multiplication by $x$ in $\mathfrak{J}^{k}
\mathcal{F}$ is a homomorphism $\mathfrak{J}^{k} \mathcal{F} \to \mathfrak{J}^{k+r} \mathcal{F}$ and consequently gives
rise to a homomorphism

```text
  μ_x : H^n(X, 𝔍^k ℱ) → H^n(X, 𝔍^{k+r} ℱ).                                   (4.1.7.8)
```

If we denote by $S$ the graded $A$-algebra $\oplus \mathfrak{J}^{k}$, we know that the multiplications $\mu_{x}$ endow
$E = \oplus H^{n}(X, \mathfrak{J}^{k} \mathcal{F})$ with a structure of graded module of finite type over the graded
ring $S$ (3.3.2), which is Noetherian `(II, 2.1.5)`.

**Lemma (4.1.7.9).** *The submodules $R_{k}$ of $H$ define on $H$ a $\mathfrak{J}$-good filtration.*

**Proof.** First, we show that we have

$$ \mathfrak{J} R_{k} \subset R_{k+1}, (4.1.7.10) $$

multiplication in $H = H^{n}(X, \mathcal{F})$ by an element $x \in \mathfrak{J}$ being therefore the map $\mu_{x}$ for
$r = 1$. For every $x \in \mathfrak{J}$, the diagram

```text
  𝔍^{k+1} ℱ ────→ 𝔍^{k+2} ℱ
       ↓             ↓
       ℱ   ────→     ℱ
```

<!-- original page 127 -->

(where the horizontal arrows are multiplication by $x$, and the vertical arrows the canonical injections) is
commutative; hence the corresponding diagram

```text
  H^n(X, 𝔍^{k+1} ℱ) ──^{μ_{x,n}}──→ H^n(X, 𝔍^{k+2} ℱ)
           ↓                                ↓                                (4.1.7.11)
         H^n(X, ℱ)  ──^{μ_{x,0}}──→  H^n(X, ℱ)
```

is commutative, which, taking into account the interpretation of $R_{k}$ as the image of $H^{n}(X, \mathfrak{J}^{k+1}
\mathcal{F}) \to H^{n}(X, \mathcal{F})$, proves (4.1.7.10) and shows in addition that the graded $S$-module $R = \oplus
R_{k}$ is a quotient of the sub-$S$-module $M = \oplus H^{n}(X, \mathfrak{J}^{k+1} \mathcal{F})$ of $E$; the remark made
above thus shows that $R$ is an $S$-module of finite type, which is equivalent to the assertion of (4.1.7.9) (Bourbaki,
*Alg. comm.*, chap. III, § 3, n° 1, th. 1).

**(4.1.7.12).** Consider now the graded $S$-module $N = \oplus H^{n+1}(X, \mathfrak{J}^{k+1} \mathcal{F})$ defined as in
(4.1.7.8); it is again an $S$-module of finite type by virtue of (3.3.2); we have $Q_{k} \subset N_{k}$ for every $k$ by
(4.1.7.5), and the diagram (4.1.7.11) where we replace $n$ by $n+1$ shows that $\mathfrak{J}^{r} Q_{k} \subset Q_{k+r}$.
In other words, $Q = \oplus Q_{k}$ is a graded sub-$S$-module of $N$, and is therefore of finite type.

**(4.1.7.13).** Denote by $a_{k}$ the canonical injection $\mathfrak{J}^{k} \to A$, which we may write $a_{k} : S_{k}
\to S_{0}$. Since $\mathfrak{J}^{k+1} \mathcal{F}$ is annihilated by $S_{k+1}$, the $A$-module $H^{n}(X,
\mathfrak{J}^{k+1} \mathcal{F})$ is annihilated by $S_{k+1}$; since $Q_{k}$ is the image of the $A$-homomorphism
$H^{n}(X, \mathcal{F}_{k}) \to H^{n+1}(X, \mathfrak{J}^{k+1} \mathcal{F})$, $Q_{k}$, as an $A$-module, is also
annihilated by $S_{k+1}$. This still means that, in the $S$-module $Q$, we have

$$ a_{k+1}(S_{k+1}) Q_{k} = 0. (4.1.7.14) $$

Since $Q$ is an $S$-module of finite type, there exist an integer $k_{0}$ and an integer $h$ such that $Q_{k+h} = S_{h}
Q_{k}$ for $k \geq k_{0}$ `(II, 2.1.6, (ii))`; from this relation and (4.1.7.14), one deduces that there exists an
integer $r > 0$ such that

$$ a_{r}(S_{r}) Q = 0. (4.1.7.15) $$

**(4.1.7.16).** Note now that the canonical injection $\mathfrak{J}^{k+1} \mathcal{F} \to \mathfrak{J}^{k} \mathcal{F}$
gives, on passage to cohomology, an $A$-homomorphism

```text
  v_k : H^{n+1}(X, 𝔍^{k+1} ℱ) → H^{n+1}(X, 𝔍^k ℱ),                           (4.1.7.17)
```

and, for every $x \in \mathfrak{J}$, we have the obvious factorization

```text
  μ_{x,0} : H^{n+1}(X, ℱ) → H^{n+1}(X, 𝔍^{k+1} ℱ) →^{v_k} H^{n+1}(X, 𝔍^k ℱ), (4.1.7.18)
```

<!-- original page 128 -->

from which we conclude that, for every sub-$A$-module $P$ of $H^{n+1}(X, \mathfrak{J}^{k+1} \mathcal{F})$, we have, in
the $S$-module $N$,

```text
  v_k(S_1 P) = a_1(S_1) P.                                                   (4.1.7.19)
```

**Lemma (4.1.7.20).** *There exists an integer $m > 0$ such that $v_{k}(Q_{k+m}) = 0$ for every $k \geq k_{0}$.*

**Proof.** Take for $m$ a multiple of $h$ that is $\geq r$; since $Q_{k+m} = S_{m} Q_{k}$ for $k \geq k_{0}$, we have by
virtue of (4.1.7.19) and (4.1.7.15) $v_{k}(Q_{k+m}) = a_{m}(S_{m}) Q \subset a_{r}(S_{r}) Q = 0$.

**(4.1.7.21).** Note that from the commutative diagram

```text
  H^n(X, ℱ) ──→ H^n(X, ℱ_k) ──→ H^{n+1}(X, 𝔍^{k+1} ℱ) ──→ H^{n+1}(X, ℱ)
      ║              ↓                       ↓                  ║
  H^n(X, ℱ) ──→ H^n(X, ℱ_{k+m}) → H^{n+1}(X, 𝔍^{k+m+1} ℱ) → H^{n+1}(X, ℱ)
```

itself coming from the commutative diagram

```text
  0 → 𝔍^{k+1} ℱ ──→ ℱ ──→ ℱ_k ──→ 0
        ↑          ║      ↑
  0 → 𝔍^{k+m+1} ℱ → ℱ → ℱ_{k+m} → 0
```

where the vertical arrows are the canonical maps, one deduces a commutative diagram

```text
  0 → R_k    ──→ H ──→ H_k    ──→ Q_k    → 0
       ↓        id      ↓           ↓
  0 → R_{k+m} → H → H_{k+m} ──→ Q_{k+m} → 0
```

where the rows are exact. Since the last vertical arrow is zero for $k \geq k_{0}$ (4.1.7.20), the image of $H_{k+m}$ in
$H_{k}$ is contained in $Ker(H_{k} \to Q_{k}) = Im(H \to H_{k})$, but moreover it contains $Im(H \to H_{k})$ by the
commutativity of the diagram, so it is equal to it; the same therefore holds for the images in $H_{k}$ of the $H_{k'}$
for $k' \geq k + m$, which proves condition (ML) for the projective system $(H_{k})_{k \geq 0}$. Moreover, for every
affine open set $U$ of $X$, we have $H^{i}(U, \mathcal{F}) = 0$ for $i > 0$ (1.3.1), and for $m > 0$, the map $H^{0}(U,
\mathcal{F}_{k+m}) \to H^{0}(U, \mathcal{F}_{k})$ is surjective `(I, 1.3.9)`. We may therefore apply $(0_{III},
13.3.1)$, and the canonical homomorphism $H^{n}(X, \mathcal{F}) \to \varprojlim H^{n}(X, \mathcal{F}_{k})$ is bijective
for every $n \geq 0$.

<!-- original page 129 -->

Since the projective system $(H/R_{k})_{k \geq 0}$ is strict, we may pass to the projective limit in the exact sequences

$$ 0 \to H/R_{k} \to H_{k} \to Q_{k} \to 0 (4.1.7.22) $$

$(0_{III}, 13.2.2)$; since $v_{k}(Q_{k+m}) = 0$, we have $\varprojlim Q_{k} = 0$, whence a topological isomorphism
$\varprojlim (H/R_{k}) \xrightarrow{\sim} \varprojlim H_{k}$. But since the filtration $(R_{k})$ of $H$ is
$\mathfrak{J}$-good, it defines on $H$ the $\mathfrak{J}$-preadic topology; therefore $\varprojlim (H/R_{k})$ is the
Hausdorff completion of $H$ for the $\mathfrak{J}$-preadic topology, which completes the proof of (4.1.7).

**(4.1.8)**

<!-- label: III.4.1.8 -->

We now pass to the proof of (4.1.5). For every affine open set $V$ of $Y$, $\Gamma(V, (R^{n}
f_{*}(\mathcal{F}))^{\wedge})$ is the Hausdorff completion of $\Gamma(V, R^{n} f_{*}(\mathcal{F}))$ for the
$\mathfrak{J}$-preadic topology (if $\mathcal{J} \mid V = \tilde{\mathfrak{J}}$) since $R^{n} f_{*}(\mathcal{F})$ is a
coherent $\mathcal{O}_{Y}$-module `(I, 10.8.4)`, and $\Gamma(V, \varprojlim R^{n} f_{*}(\mathcal{F}_{k})) = \varprojlim
\Gamma(V, R^{n} f_{*}(\mathcal{F}_{k}))$ $(0_{I}, 3.2.6)$; the fact that $\phi_{n}$ is a topological isomorphism then
results from (4.1.7) and (1.4.11). On the other hand (again by virtue of (1.4.11)), it follows from (4.1.7) that the
homomorphism $\psi_{n}$ of (4.1.3.3) is an isomorphism, hence $\psi_{n}$ is an isomorphism by definition of $R^{n}
\hat{\mathit{f}}_{*}(\hat{\mathcal{F}})$.

**Corollary (4.1.9).**

<!-- label: III.4.1.9 -->

*Under the hypotheses of (4.1.4), for every affine open set $V$ of $Y$, the canonical homomorphism*

```text
  H^n(𝔛 ∩ 𝑓̂^{-1}(V), ℱ̂) → Γ(𝔜 ∩ V, R^n 𝑓̂_*(ℱ̂))
```

*is bijective.*

**Remark (4.1.10).**

<!-- label: III.4.1.10 -->

Let $f : X \to Y$ be a morphism of finite type of (usual) Noetherian preschemes, and let $\mathcal{F}$ be a coherent
$\mathcal{O}_{X}$-module whose support is proper over $Y$ `(II, 5.4.10)`. We then know (3.2.4) that $R^{n}
f_{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{Y}$-module for every $n \geq 0$. Moreover, we may always assume that
$\mathcal{F} = u_{*}(\mathcal{G})$, where $\mathcal{G} = u^{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{Z}$-module, $Z$
denoting a suitable closed subprescheme of $X$ whose underlying space is $Supp(\mathcal{F})$, and $u : Z \to X$ the
canonical injection `(I, 9.3.5)`. If we set $\mathcal{G}_{k} = \mathcal{G} / \mathfrak{J}^{k+1} \mathcal{G}$ (with
$\mathfrak{J} = u^{*}(\mathcal{J}) \mathcal{O}_{Z}$), we have $\mathcal{F}_{k} = u_{*}(\mathcal{G}_{k})$, $R^{n}
f_{*}(\mathcal{F}) = R^{n} (f \circ u)_{*}(\mathcal{G})$, and $R^{n} f_{*}(\mathcal{F}_{k}) = R^{n} (f \circ
u)_{*}(\mathcal{G}_{k})$ (1.3.4), and finally, taking `(I, 10.9.5)` into account,

```text
  R^n 𝑓̂_*(ℱ̂) = R^n (f ∘ u)^∧_*(𝒢̂).
```

We may then apply (4.1.5) to $\mathcal{G}$ and to the proper morphism $f \circ u$, and we conclude that under these
hypotheses, the results of (4.1.5) are valid for $\mathcal{F}$ and $f$.

## 4.2. Particular cases and variants

The most useful form of the comparison theorem (4.1.5) is the following:

**Proposition (4.2.1).**

<!-- label: III.4.2.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-module. Then, for every $y \in Y$ and every $p$, $(R^{p} f_{*}(\mathcal{F}))_{y}$ is*

<!-- original page 130 -->

*an $\mathcal{O}_{y}$-module of finite type, hence separated for the $\mathfrak{m}_{y}$-preadic topology, and we have a
canonical topological isomorphism*

```text
  ((R^p f_*(ℱ))_y)^∧ ⥲ lim_← H^p(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{k+1}))      (4.2.1.1)
                         k
```

*where the first member is the completion of $(R^{p} f_{*}(\mathcal{F}))_{y}$ for the $\mathfrak{m}_{y}$-preadic
topology, and at the second member $f^{-1}(y)$ is considered, for every $k \geq 0$, as the underlying space of the
prescheme* *$X \times_{Y} \operatorname{Spec}(\mathcal{O}_{y} / \mathfrak{m}^{k+1}_{y})$ `(I, 3.6.1)`.*

**Proof.** Since $\mathcal{O}_{y}$ is a Noetherian local ring and $(R^{p} f_{*}(\mathcal{F}))_{y}$ is a finitely
generated $\mathcal{O}_{y}$-module (3.2.1), the $\mathfrak{m}_{y}$-preadic topology on $(R^{p} f_{*}(\mathcal{F}))_{y}$
is separated $(0_{I}, 7.3.5)$. The other assertions are consequences of (4.1.7) when $Y$ is Noetherian and the point $y$
is closed, on replacing $Y$ by an affine neighbourhood of $y$ and taking $Y' = {y}$, in view of `(G, II, 4.9.1)`. In the
general case, set $Y_{1} = \operatorname{Spec}(\mathcal{O}_{y})$, $X_{1} = X \times_{Y} Y_{1}$, $\mathcal{F}_{1} =
\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{y}$, and let $f_{1} = f \times_{Y} 1_{Y_{1}} : X_{1} \to Y_{1}$;
`Y_1` is Noetherian and $f_{1}$ is proper `(II, 5.4.2, (iii))`, and $\mathcal{F}_{1}$ is coherent $(0_{I}, 5.3.11)$. Let
$y_{1}$ be the unique closed point of `Y_1`; the proposition is valid for $f_{1}$, $y_{1}$, and $\mathcal{F}_{1}$; we
have $\mathcal{O}_{y_{1}} = \mathcal{O}_{y}$, $f^{-1}_{1}(y_{1}) = f^{-1}(y)$ `(I, 3.6.5)`, the preschemes $X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{y} / \mathfrak{m}^{k+1}_{y})$ and $X_{1} \times_{Y_{1}}
\operatorname{Spec}(\mathcal{O}_{y_{1}} / \mathfrak{m}^{k+1}_{y_{1}})$ being canonically identified `(I, 3.3.9)`;
moreover, $\mathcal{F}_{1} \otimes_{\mathcal{O}_{y_{1}}} (\mathcal{O}_{y_{1}} / \mathfrak{m}^{k+1}_{y_{1}})$ is
identified with $\mathcal{F} \otimes_{\mathcal{O}_{y}} (\mathcal{O}_{y} / \mathfrak{m}^{k+1}_{y})$ `(I, 9.1.6)`. It
remains to see that $R^{p} f_{1*}(\mathcal{F}_{1})$ is canonically isomorphic to $R^{p} f_{*}(\mathcal{F})
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{y}$, which results from `(1.4.15)`, the local morphism
$\operatorname{Spec}(\mathcal{O}_{y}) \to Y$ being flat $(0_{I}, 6.7.1 and I, 2.4.2)$.

The following corollary uses the terminology of dimension theory (chap. IV) and will not be applied before chap. IV.

**Corollary (4.2.2).**

<!-- label: III.4.2.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism, $y$ a point of $Y$, $r$ the dimension of
$f^{-1}(y)$. Then, for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, the sheaves $R^{p} f_{*}(\mathcal{F})$ are
zero in a neighbourhood of $y$ for every $p > r$.*

**Proof.** Indeed, we then have $H^{p}(f^{-1}(y), \mathcal{F} \otimes (\mathcal{O}_{y} / \mathfrak{m}^{k+1}_{y})) = 0$
`(G, II, 4.15.2)` for every $k$, hence (4.2.1) the Hausdorff completion of $(R^{p} f_{*}(\mathcal{F}))_{y}$ for the
$\mathfrak{m}_{y}$-preadic topology is zero, and as this topology is separated, we also have $(R^{p}
f_{*}(\mathcal{F}))_{y} = 0$; whence the conclusion, since $R^{p} f_{*}(\mathcal{F})$ is coherent $(0_{I}, 5.2.2)$.

**(4.2.3).** The result (4.2.1) is principally used for $p = 0$; we thus obtain the following corollary:

**Corollary (4.2.4).**

<!-- label: III.4.2.4 -->

*Under the hypotheses of (4.2.1), we have a canonical topological isomorphism*

```text
  ((f_*(ℱ))_y)^∧ ⥲ lim_← Γ(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{k+1})).           (4.2.4.1)
                     k
```

## 4.3. Zariski's connection theorem

The results of this section and of the next generalize well-known theorems of Zariski, and may all be deduced from
(4.2.4). They are consequences of the following theorem:

**Theorem (4.3.1) (Connection theorem).**

<!-- label: III.4.3.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism. Then $\mathcal{B}(X) =
f_{*}(\mathcal{O}_{X})$ is a coherent $\mathcal{O}_{Y}$-algebra.*

<!-- original page 131 -->

*Let $Y'$ be the finite $Y$-scheme over $Y$ such that $\mathcal{A}(Y') = f_{*}(\mathcal{O}_{X})$, determined up to
$Y$-isomorphism `(II, 1.3.1 and 6.1.3)`; if $f' = \nu(e)$ is the $Y$-morphism $X \to Y'$ deduced from the identity
isomorphism $e : \mathcal{A}(Y') \xrightarrow{\sim} f_{*}(\mathcal{O}_{X})$ `(II, 1.2.7)`, then $f'$ is proper,
$f'_{*}(\mathcal{O}_{X})$ is isomorphic to $\mathcal{O}_{Y'}$, and the fibres $f'^{-1}(y')$ of the morphism $f'$ are
connected and non-empty for every $y' \in Y'$.*

**Proof.** Let $g : Y' \to Y$ be the structure morphism. To prove that the homomorphism $\theta : \mathcal{O}_{Y'} \to
f'_{*}(\mathcal{O}_{X})$ entering the definition of the morphism $f'$ is bijective, it suffices, since $Y'$ is affine
over $Y$, to prove that $g_{*}(\theta) : g_{*}(\mathcal{O}_{Y'}) \to g_{*}(f'_{*}(\mathcal{O}_{X})) =
f_{*}(\mathcal{O}_{X})$ is the identity `(II, 1.4.2)`; but this results from the definitions since
$g_{*}(\mathcal{O}_{Y'}) = \mathcal{A}(Y')$ and $f_{*}(\mathcal{O}_{X}) = \mathcal{B}(X)$. The fact that
$\mathcal{B}(X)$ is coherent is a particular case of the finiteness theorem (3.2.1). Since $f$ is proper and $g$
separated, $f'$ is proper `(II, 5.4.3, (i))`; to complete the proof of (4.3.1), it suffices therefore to prove the

**Corollary (4.3.2).**

<!-- label: III.4.3.2 -->

*Under the hypotheses of (4.3.1), suppose in addition that $f_{*}(\mathcal{O}_{X})$ is isomorphic to $\mathcal{O}_{Y}$.
Then the fibres $f^{-1}(y)$ of $f$ are connected and non-empty for every $y \in Y$.*

**Proof.** The hypothesis that $f_{*}(\mathcal{O}_{X})$ is isomorphic to $\mathcal{O}_{Y}$ already implies that $f$ is
dominant, hence surjective since $f$ is a closed map. We may reduce, as in (4.2.1), to the case where $y$ is closed in
$Y$; $f^{-1}(y)$, being a Noetherian space, has a finite number of connected components, and it is the underlying space
of the completion $\mathfrak{X}$ along $f^{-1}(y)$. If $Z_{i}$ ($1 \leq i \leq n$) are these connected components, it is
clear that $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ is the direct sum of the rings $\Gamma(Z_{i},
\mathcal{O}_{\mathfrak{X}})$, and each of these is not reduced to `0`, since the unit section is distinct from `0` at
each point of $X$. Now, if we apply (4.1.5) to $\mathcal{F} = \mathcal{O}_{X}$, whose completion along $f^{-1}(y)$ is
$\mathcal{O}_{\mathfrak{X}}$, we see that $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ is isomorphic to the
Hausdorff $\mathfrak{m}_{y}$-adic completion $\hat{\mathcal{O}}_{y}$ of the local ring $\mathcal{O}_{y}$; it is
therefore a local ring which cannot be a direct sum of several rings not reduced to `0` (otherwise it would have several
distinct maximal ideals). We thus have $n = 1$, which proves the corollary.

**Corollary (4.3.3).**

<!-- label: III.4.3.3 -->

*Under the hypotheses of (4.3.1), for every $y \in Y$, the set of connected components of the fibre $f^{-1}(y)$ is in
one-to-one correspondence with the finite set of points of the fibre $g^{-1}(y)$, where $g : Y' \to Y$ is the structure
morphism (in other words, the set of maximal ideals of $(f_{*}(\mathcal{O}_{X}))_{y}$).*

**Proof.** Since $Y'$ is finite over $Y$, we know indeed that $g^{-1}(y)$ is a finite discrete space `(II, 6.1.7)`.
Since $f^{-1}(y) = f'^{-1}(g^{-1}(y))$, the corollary follows from this remark and from (4.3.1).

We thus have a remarkable interpretation of the $Y$-prescheme $Y'$ defined in (4.3.1). The factorization $f = g \circ
f'$ of the proper morphism $f$ is analogous to the factorization obtained by K. Stein for holomorphic maps of analytic
spaces, and we shall call it henceforth the *Stein factorization* of $f$.

**Remark (4.3.4).**

<!-- label: III.4.3.4 -->

Let $k$ be an extension of the field $\kappa(y)$: if the prescheme $f^{-1}(y) \otimes_{\kappa(y)} k = f^{-1}(y)
\times_{Y} \operatorname{Spec}(k)$ is connected, then so is $f^{-1}(y)$, which is its image under a projection morphism
`(I, 3.4.7)`. We shall say that, for a morphism $f : X \to Y$ of preschemes and a point $y \in Y$, the fibre $f^{-1}(y)$
is *geometrically connected* if, for every extension $k$ of $\kappa(y)$, the prescheme $f^{-1}(y) \otimes_{\kappa(y)} k
= f^{-1}(y) \times_{Y} \operatorname{Spec}(k)$ is connected.

<!-- original page 132 -->

Under the hypotheses of (4.3.2), one may then strengthen its conclusion: the fibres $f^{-1}(y)$ are in fact
*geometrically connected*. To see this, observe that for every extension $k$ of $\kappa(y)$, there exists a Noetherian
local ring $A$ and a local homomorphism $\phi : \mathcal{O}_{y} \to A$ which makes $A$ a flat $\mathcal{O}_{y}$-module
and such that the residue field of $A$ is $\kappa(y)$-isomorphic to $k$ $(0_{III}, 10.3.1)$. Let then $Y_{1} =
\operatorname{Spec}(A)$ and let $h : Y_{1} \to Y$ be the local morphism corresponding to $\phi$, transforming the unique
closed point of `Y_1` into $y$ `(I, 2.4.1)`; set $X_{1} = X \times_{Y} Y_{1}$ and $f_{1} = f \times_{Y} 1_{Y_{1}}$;
$f_{1}$ is proper `(II, 5.4.2, (iii))` and $f^{-1}_{1}(y_{1})$ is a $\kappa(y_{1})$-prescheme isomorphic to $X
\times_{Y} \operatorname{Spec}(k)$. It thus suffices to show that $f_{1*}(\mathcal{O}_{X_{1}}) = \mathcal{O}_{Y_{1}}$ in
order to apply (4.3.2) to $f_{1}$. Now, $h$ is a flat morphism, as follows from `(I, 2.4.2)` and `(1.4.15.5)`; we
therefore have $f_{1*}(\mathcal{O}_{X_{1}}) = h^{*}(f_{*}(\mathcal{O}_{X})) = h^{*}(\mathcal{O}_{Y}) =
\mathcal{O}_{Y_{1}}$ by virtue of `(1.4.15)` applied for $q = 0$.

In the general case (4.3.1), the same reasoning shows that we have (with the notation of (4.3.1))
$f_{1*}(\mathcal{O}_{X_{1}}) = h^{*}(f_{*}(\mathcal{O}_{X}))$, and the Stein factorization $f_{1} = g_{1} \circ f'_{1}$
of $f_{1}$ is such that $g_{1} = g \times_{Y} 1_{Y_{1}}$ `(II, 1.5.2)`, the corresponding finite `Y_1`-scheme being
$Y'_{1} = Y' \times_{Y} Y_{1}$. Taking the transitivity of fibres `(I, 3.6.4)` into account, we therefore see that the
number of connected components of $f^{-1}_{1}(y_{1})$ is, by virtue of (4.3.3), equal to the number of elements of
$g^{-1}_{1}(y_{1}) = g^{-1}(y) \otimes_{\kappa(y)} k$. If we take for $k$ an algebraically closed extension of
$\kappa(y)$, this number is independent of the algebraically closed extension considered and equal to the *geometric
number of points* of $g^{-1}(y)$ `(I, 6.4.7)`, or again to the sum of the separable ranks $[\kappa(y'_{i}) :
\kappa(y)]_{s}$ where $y'_{i}$ runs over the finite set $g^{-1}(y)$. We also say that this number is the *geometric
number of connected components* of $f^{-1}(y)$. Note that the $\kappa(y'_{i})$ are none other than the residue fields of
the semi-local ring $(f_{*}(\mathcal{O}_{X}))_{y}$.

**Proposition (4.3.5).**

<!-- label: III.4.3.5 -->

*Let $X$ and $Y$ be two locally Noetherian integral preschemes and $f : X \to Y$ a proper dominant morphism. For every
$y \in Y$, the number of connected components of $f^{-1}(y)$ is at most equal to the number of maximal ideals of the
integral closure $\mathcal{O}'_{y}$ of $\mathcal{O}_{y}$ in the field of rational functions $R(X)$.*

**Proof.** Indeed, for every open set $U$ of $Y$, $\Gamma(U, f_{*}(\mathcal{O}_{X})) = \Gamma(f^{-1}(U),
\mathcal{O}_{X})$ is the intersection of the local rings $\mathcal{O}_{x}$ such that $x \in f^{-1}(U)$ `(I, 8.2.1.1)`.
We thus conclude immediately that the stalk $(f_{*}(\mathcal{O}_{X}))_{y}$ is a subring of $R(X)$ containing
$\mathcal{O}_{y}$. Moreover, since $f_{*}(\mathcal{O}_{X})$ is a coherent $\mathcal{O}_{Y}$-module,
$(f_{*}(\mathcal{O}_{X}))_{y}$ is a finitely generated $\mathcal{O}_{y}$-module, and is therefore contained in
$\mathcal{O}'_{y}$; we know ([13], vol. I, p. 257 and 259) that every maximal ideal of such a ring $A$ is the
intersection of $A$ and a maximal ideal of $\mathcal{O}'_{y}$, whence the proposition.

**Definition (4.3.6).**

<!-- label: III.4.3.6 -->

*We say that an integral local ring is *unibranch* if its integral closure is a local ring. We say that a point $y$ of
an integral prescheme $Y$ is *unibranch* if the local ring $\mathcal{O}_{y}$ is unibranch (which is in particular the
case when $Y$ is normal at the point $y$).*

Let $A$ be an integral local ring, and let $K$ be its field of fractions; for $A$ to be unibranch, it is necessary and
sufficient that every subring `A_1` of $K$ containing $A$ and which is a finite $A$-algebra be a local ring. Indeed, let
$A'$ be the integral closure of $A$; it follows from the first Cohen–Seidenberg theorem (Bourbaki, *Alg. comm.*, chap.
V, § 2, n° 1, th. 1) that every maximal ideal of `A_1` is the trace of a maximal ideal of $A'$, so if $A'$ is local,
then so is `A_1`. Conversely, $A'$ is the inductive limit

<!-- original page 133 -->

of the increasing filtered family of finite sub-$A$-algebras `A_1` of $A'$, and if each of the `A_1` is a local ring,
the maximal ideal of `A_1` is the trace on `A_1` of that of `A_2`, for $A_{1} \subset A_{2}$, by the same reasoning as
above, so $A'$ is a local ring $(0_{I}, 10.3.1.3)$.

Note that if the completion of a Noetherian local ring $A$ is integral (which we express by saying that $A$ is
*analytically integral*), then $A$ is unibranch. Indeed, let $\mathfrak{m}$ be the maximal ideal of $A$, $K$ its field
of fractions, $K'$ the field of fractions of `Â`; we then have $K' = K \otimes_{A} \hat{A}$. Let `A_1` be a finite
sub-$A$-algebra of $K$. The subring `B_1` of $K'$ generated by `Â` and `A_1` is isomorphic to $A_{1} \otimes_{A}
\hat{A}$; it is an `Â`-module of finite type, the completion of `A_1` for the $\mathfrak{m}$-adic topology $(0_{I},
7.3.3 and 7.3.6)$. Since `A_1` is a semi-local ring (Bourbaki, *Alg. comm.*, chap. IV, § 2, n° 5, cor. 3 of prop. 9) and
its completion is integral, `A_1` can have only one maximal ideal $\mathfrak{m}_{1}$, and we have
$\hat{\mathfrak{m}}_{1} \cap A = \mathfrak{m}$; whence our assertion.

**Corollary (4.3.7).**

<!-- label: III.4.3.7 -->

*Under the hypotheses of (4.3.5), suppose that the algebraic closure of $R(Y)$ in $R(X)$ is of separable degree $n$, and
that $y \in Y$ is unibranch. Then the fibre $f^{-1}(y)$ has at most $n$ connected components. In particular, if the
algebraic closure of $R(Y)$ in $R(X)$ is radicial over $R(Y)$, then $f^{-1}(y)$ is connected.*

**Proof.** Indeed, let $\mathcal{O}'_{y}$ be the integral closure of $\mathcal{O}_{y}$; the integral closure
$\tilde{\mathcal{O}}_{y}$ of $\mathcal{O}_{y}$ in $R(X)$ is also that of $\mathcal{O}'_{y}$; but we know that if
$\mathcal{O}'_{y}$ is a local ring, then $\tilde{\mathcal{O}}_{y}$ is a semi-local ring whose number of maximal ideals
is at most equal to $n$ ([13], vol. I, p. 289, th. 22).

This corollary is essentially the form in which Zariski states his "connection theorem" for algebraic schemes.

**Remark (4.3.8).**

<!-- label: III.4.3.8 -->

If one adds to the hypotheses of (4.3.7) the hypothesis that $Y$ is normal at $y$, the fibre $f^{-1}(y)$ is
*geometrically connected*, since (with the notation of (4.3.4)) $g^{-1}(y)$ is reduced to a point $y'$ and $\kappa(y')$
is radicial over $\kappa(y)$.

**Definition (4.3.9).**

<!-- label: III.4.3.9 -->

*Given a locally Noetherian prescheme $Y$, we say that a morphism of finite type $f : X \to Y$ is *universally open* if,
for every irreducible locally Noetherian prescheme $Y'$ and every dominant morphism $g : Y' \to Y$, every irreducible
component of $X' = X \times_{Y} Y'$ dominates $Y'$.*

If $Y$ is irreducible, this comes to saying that if $\eta$, $\eta'$ are the generic points of $Y$ and $Y'$ respectively
(so that $g(\eta') = \eta$), and if we set $f' = f_{(Y')}$, every irreducible component of $X'$ meets $f'^{-1}(\eta')$
$(0_{I}, 2.1.8)$; this implies that for every open set $U$ of $Y$, the morphism $f^{-1}(U) \to U$, restriction of $f$,
is universally open.

**Corollary (4.3.10).**

<!-- label: III.4.3.10 -->

*Let $X$, $Y$ be two locally Noetherian integral preschemes, $f : X \to Y$ a proper dominant universally open morphism.
If the algebraic closure of $R(Y)$ in $R(X)$ is radicial over $R(Y)$, every fibre $f^{-1}(y)$ ($y \in Y$) is
geometrically connected.*

**Proof.** We may restrict to the case where $Y = \operatorname{Spec}(B)$, $B$ being an integral Noetherian ring. It
then follows from `(II, 7.1.7)` that there exists an integrally closed Noetherian local ring $A$ which dominates
$\mathcal{O}_{y}$ and has $R(Y)$ for field of fractions. Let $Y' = \operatorname{Spec}(A)$, and let $h : Y' \to Y$ be
the morphism corresponding to the canonical injection $B \to A$, which is birational (hence dominant); moreover, if $y'$
is the unique closed point of $Y'$, we have $h(y') = y$. Let

<!-- original page 134 -->

$X' = X \times_{Y} Y'$, $f' = f \times_{Y} 1_{Y'}$; denote by $\eta$, $\eta'$, $\xi$ the generic points of $Y$, $Y'$,
and $X$ respectively, so that $f(\xi) = \eta$ and $h^{-1}(\eta) = {\eta'}$; moreover, $\kappa(\eta') = \kappa(\eta) =
R(Y)$, so $f'^{-1}(\eta')$ is isomorphic to $f^{-1}(\eta)$ `(I, 3.6.4)`, and in particular, since $\xi$ is the generic
point of $f^{-1}(\eta)$ $(0_{I}, 2.1.8)$, $f'^{-1}(\eta')$ has a single generic point. But by hypothesis, every
irreducible component of $X'$ has its generic point in $f'^{-1}(\eta')$, so $X'$ is necessarily irreducible, its generic
point $\xi'$ is the generic point of $f'^{-1}(\eta')$, and we have $\kappa(\xi') = \kappa(\xi)$. Set $X'' = X'_{red}$;
`X''` is then integral and Noetherian, `f''` is proper `(II, 5.4.6)` and the underlying spaces of the fibres
$f''^{-1}(y')$ and $f'^{-1}(y')$ are the same; moreover, $R(X'') = \kappa(\xi') = R(X)$, so `f''` satisfies the
hypotheses of (4.3.8), and $f''^{-1}(y')$ is geometrically connected. Now let $k$ be an arbitrary extension of
$\kappa(y)$; there exists an extension $k_{1}$ of $\kappa(y')$ such that $\kappa(y)$ and $k$ can be considered as
subextensions of $k_{1}$ (Bourbaki, *Alg.*, chap. V, § 4, prop. 2). By hypothesis, $f''^{-1}(y') \times_{Y'}
\operatorname{Spec}(k_{1})$ is connected, and it has the same reduced prescheme as $f'^{-1}(y') \times_{Y'}
\operatorname{Spec}(k_{1})$ `(I, 5.1.8)`, so the latter is connected, and since it is isomorphic to $f^{-1}(y)
\times_{Y} \operatorname{Spec}(k_{1})$ `(I, 3.6.4)`, we conclude that the latter is connected; *a fortiori*, the same
holds for $f^{-1}(y) \times_{Y} \operatorname{Spec}(k)$ by the remark at the beginning of (4.3.4), which completes the
proof.

**Remarks (4.3.11).**

<!-- label: III.4.3.11 -->

(i) The preceding reasoning is due in substance to Zariski [20], except that he can take for $A$ the integral closure of
$\mathcal{O}_{y}$, the latter being a Noetherian ring for the local rings of classical algebraic geometry. On the other
hand, Zariski proves that if $Y$ is the Chow variety of a projective space $P^{r}_{k}$ over a field $k$, and if $X$ is
the closed part of $P^{r}_{k} \times Y$ which defines the Chow correspondence between $P^{r}_{k}$ and $Y$, then the
projection $X \to Y$ is a universally open morphism (loc. cit., lemma on p. 82). It appears indeed to be the only formal
property of "Chow coordinates" that has been used in certain applications; consequently, in such a situation, it is of
interest to substitute the language of *fibres of a proper morphism* (possibly assumed universally open or subject to
other analogous restrictions of local regularity) for the language of *specialization of cycles in projective space*.

(ii) In chap. IV, we shall see that a universally open morphism $f : X \to Y$ may also be defined in the following way
(which justifies the terminology): for every morphism $Z \to Y$, the morphism $f_{(Z)} : X_{(Z)} \to Z$ is open. One may
moreover show that if $f$ satisfies the hypotheses of (4.3.10), then if $y$, $y'$ are two points of $Y$ such that $y'$
is a specialization of $y$, the *geometric number of connected components* of $f^{-1}(y')$ is at most equal to that of
the connected components of $f^{-1}(y)$.

**Corollary (4.3.12).**

<!-- label: III.4.3.12 -->

*Under the hypotheses of (4.3.5), suppose in addition that $R(Y)$ is algebraically closed in $R(X)$, and let $y$ be a
normal point of $Y$. Then $f^{-1}(y)$ is geometrically connected, and there exists an open neighbourhood $U$ of $y$ in
$Y$ such that $f_{*}(\mathcal{O}_{X})(f^{-1}(U))$ is isomorphic to $\mathcal{O}_{Y} \mid U$. More particularly, if we
assume $Y$ normal (and $R(Y)$ algebraically closed in $R(X)$), then $f_{*}(\mathcal{O}_{X})$ is isomorphic to
$\mathcal{O}_{Y}$.*

**Proof.** The first assertion relative to $f^{-1}(y)$ is a particular case of (4.3.8). We

<!-- original page 135 -->

deduce that if $f : X \to Y' \to Y$ is the Stein factorization of $f$ (4.3.3), $g^{-1}(y)$ is reduced to a single point
$y'$; moreover, we have $\mathcal{O}_{y} \subset \mathcal{O}_{y'} = (f_{*}(\mathcal{O}_{X}))_{y} \subset R(X)$, and
since $\mathcal{O}_{y'}$ is finite over $\mathcal{O}_{y}$ (and *a fortiori* over $R(Y)$), it is contained in $R(Y)$ by
virtue of the hypothesis; since $y$ is normal, we necessarily have $\mathcal{O}_{y'} = \mathcal{O}_{y}$, from which we
conclude that $g$ is a local isomorphism at the point $y'$ `(I, 6.5.4)`, which completes the proof of the first part of
the corollary. The second results from the first, for the additional hypothesis implies that $g$ is bijective and a
local isomorphism in the neighbourhood of every point of $Y'$, hence an isomorphism.

The fact that (4.3.7) is established in the framework of schemes permits applications such as the following:

**Proposition (4.3.13).**

<!-- label: III.4.3.13 -->

*Let $A$ be a Noetherian unibranch local ring, $\mathfrak{a}$ an ideal of definition of $A$, $A_{0} = A/\mathfrak{a}$,
$S = gr_{\mathfrak{a}}(A)$ the graded ring associated to $A$ for the $\mathfrak{a}$-preadic filtration; $S$ is a graded
`A_0`-algebra generated by `S_1`, `S_1` being a finitely generated `A_0`-module. Then $\operatorname{Proj}(S)$ is a
connected `A_0`-scheme.*

**Proof.** Let $\mathfrak{m}$ be the maximal ideal of $A$; $Y = \operatorname{Spec}(A)$ is an integral scheme whose
point corresponding to $\mathfrak{m}$ is the unique closed point. By hypothesis, we have $\mathfrak{m}^{p} \subset
\mathfrak{a} \subset \mathfrak{m}$ for an integer $p$, so $V(\mathfrak{a}) = {\mathfrak{m}}$. Let $S' = \oplus_{n \geq
0} \mathfrak{a}^{n}$, and let $X = \operatorname{Proj}(S')$, which is the $Y$-scheme obtained by blowing up the ideal
$\mathfrak{a}$; $X$ is integral and the structure morphism $f : X \to Y$ is birational `(II, 8.1.4)` and obviously
projective. Consequently, (4.3.7) is applicable and shows that $f^{-1}(\mathfrak{m})$ is connected; but the space
$f^{-1}(\mathfrak{m})$ is the underlying space of $\operatorname{Proj}(S' \otimes_{A} A_{0})$
`(I, 3.6.1 and II, 2.8.10)`; since $S' \otimes_{A} A_{0} = S$ by definition, the proposition is proved.

## 4.4. Zariski's "main theorem"

**Proposition (4.4.1).**

<!-- label: III.4.4.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism. Let $X'$ be the set of points $x \in X$
which are isolated in their fibre $f^{-1}(f(x))$. Then the set $X'$ is open in $X$, and if $f = g \circ f'$ is the Stein
factorization of $f$ (4.3.3), the restriction of $f'$ to $X'$ is an isomorphism of $X'$ onto a subprescheme induced on
an open set $U$ of $Y'$, and we have $X' = f'^{-1}(U)$.*

**Proof.** Since $g^{-1}(f(x))$ is finite and discrete (4.3.3 and `II, 6.1.7`), for $x$ to be isolated in
$f^{-1}(f(x))$, it is necessary and sufficient that it be isolated in $f'^{-1}(f'(x))$; we may thus restrict to the case
where $f' = f$, hence $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$. Then, if $x \in X'$, $f^{-1}(f(x))$, which is
connected (4.3.2), is necessarily reduced to the point $x$. Since $f$ is closed, for every open neighbourhood $V$ of $x$
in $X$, $f(X - V)$ is closed in $Y$ and does not contain $y = f(x)$, since $f^{-1}(y) = {x}$; if $U$ is the complement
of $f(X - V)$ in $Y$, we have $f^{-1}(U) \subset V$, and we conclude that the inverse images by $f$ of a fundamental
system of open neighbourhoods of $y$ form a fundamental system of open neighbourhoods of $x$. The hypothesis
$f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$ and the definition of the direct image of a sheaf $(0_{I}, 3.4.1 and 4.2.1)$
then imply that, if $f = (\psi, \theta)$, the homomorphism $\theta^{\sharp}_{x} : \mathcal{O}_{y} \to \mathcal{O}_{x}$
is an isomorphism. We conclude that there exists an open neighbourhood $V$ of $x$ and an open neighbourhood $U$ of $y$
such that the restriction of $f$ to $V$ is an isomorphism of $V$ onto $U$ `(I, 6.5.4)`; furthermore, by what we have
just seen,

<!-- original page 136 -->

we may suppose $f^{-1}(U) = V$, whence we conclude immediately, by definition, that $V \subset X'$, which completes the
proof.

The following proposition was proved by Chevalley in the case of algebraic schemes:

**Proposition (4.4.2).**

<!-- label: III.4.4.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism. The following conditions are equivalent:*

*a) $f$ is finite.*

*b) $f$ is affine and proper.*

*c) $f$ is proper and, for every $y \in Y$, $f^{-1}(y)$ is a finite set.*

**Proof.** We know that a) implies b) `(II, 6.1.2 and 6.1.11)`. If $f$ is proper and affine, the same holds for the
morphism $f^{-1}(y) \to \operatorname{Spec}(\kappa(y))$ `(II, 1.6.2, (iii) and 5.4.2, (iii))`, and the finiteness
theorem (3.2.1) applied to the structure sheaf of $f^{-1}(y)$ shows that $f^{-1}(y) = \operatorname{Spec}(A)$, where $A$
is a finite $\kappa(y)$-algebra; hence $f^{-1}(y)$ is a finite set `(II, 6.1.7)`, and we see that b) implies c).
Finally, since $f^{-1}(y)$ is an algebraic prescheme over $\kappa(y)$, the hypothesis that the set $f^{-1}(y)$ is finite
implies that the space $f^{-1}(y)$ is discrete `(I, 6.4.4)`. With the notation of (4.4.1), we therefore have $X' = X$,
and $f' : X \to Y'$ is an isomorphism; since $g$ is a finite morphism, we see that c) implies a).

**Theorem (4.4.3) ("Main theorem" of Zariski).**

<!-- label: III.4.4.3 -->

*Let $Y$ be a Noetherian prescheme, $f : X \to Y$ a quasi-projective morphism, $X'$ the set of points $x \in X$ which
are isolated in their fibre $f^{-1}(f(x))$. Then $X'$ is an open part of $X$, and the subprescheme induced $X'$ is
isomorphic to a prescheme induced on an open part of a $Y$-prescheme $Y'$ finite over $Y$.*

**Proof.** The hypothesis implies that there exists a projective $Y$-prescheme $Z$ such that $X$ is $Y$-isomorphic to a
subprescheme induced on an open set of $Z$ `(II, 5.3.2 and 5.5.1)`. We are thus reduced to proving the theorem when $f$
is a projective morphism, hence proper `(II, 5.5.3)`, and it then follows at once from (4.4.1).

**Remark (4.4.4).**

<!-- label: III.4.4.4 -->

If $X$ is reduced (resp. irreducible, and $X'$ non-empty), one may suppose, in the statement of (4.4.3), that $Y'$ is
reduced (resp. irreducible). Indeed, one may always replace $Y'$ by the subprescheme closure $\bar{X}'$ of $X'$ in $Y'$
`(I, 9.5.11 and II, 6.1.5, (i) and (ii))`, and one knows that if $X'$ is reduced, the same holds for $\bar{X}'$
`(I, 9.5.9, (i))`; on the other hand, if $X'$ is non-empty, it is irreducible if $X$ is, and $\bar{X}'$ is then also
irreducible.

**Corollary (4.4.5).**

<!-- label: III.4.4.5 -->

*Let $Y$ be a locally Noetherian scheme, $f : X \to Y$ a morphism of finite type, $x$ a point of $X$ isolated in its
fibre $f^{-1}(f(x))$. Then there exists an open neighbourhood of $x$ in $X$ which is isomorphic to an open part of a
$Y$-prescheme finite over $Y$.*

**Proof.** Let $y = f(x)$, $U$ an affine open neighbourhood of $y$ in $Y$, $V$ an affine open neighbourhood of $x$ in
$X$, contained in $f^{-1}(U)$. Since $Y$ is separated, the injection $U \to Y$ is affine `(II, 1.6.3)`, and since $V$ is
affine over $U$ (*ibid.*), the restriction of $f$ to $V$ is an affine morphism $V \to Y$ `(II, 1.6.2, (ii))`; *a
fortiori*, this restriction is a quasi-projective morphism since it is of finite type `(I, 6.3.5 and II, 5.3.4, (i))`.
It then suffices to apply (4.4.3) to this restriction.

Corollary (4.4.5) may be stated in the language of commutative algebra:

<!-- original page 137 -->

**Corollary (4.4.6).**

<!-- label: III.4.4.6 -->

*Let $A$ be a Noetherian ring, $B$ an $A$-algebra of finite type, $\mathfrak{q}$ a prime ideal of $B$, $\mathfrak{p}$
its inverse image in $A$. Suppose that $\mathfrak{q}$ is both maximal and minimal in the set of prime ideals of $B$
whose inverse image is $\mathfrak{p}$. Then there exist $g \in B - \mathfrak{q}$, a finite $A$-algebra $A'$, and an
element $f' \in A'$ such that the $A$-algebras $B_{g}$ and $A'_{f'}$ are isomorphic.*

**Proof.** It suffices to apply (4.4.5) to $Y = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$, the hypothesis
on $\mathfrak{q}$ meaning exactly that $\mathfrak{q}$ is isolated in its fibre `(I, 1.1.7)`.

We deduce the following less general-looking result:

**Corollary (4.4.7).**

<!-- label: III.4.4.7 -->

*Let $A$ be a Noetherian local ring, $B$ an $A$-algebra of finite type, $\mathfrak{n}$ a prime ideal of $B$ whose
inverse image in $A$ is the maximal ideal $\mathfrak{m}$. Suppose that $\mathfrak{n}$ is maximal in $B$ and is minimal
in the set of prime ideals of $B$ whose inverse image is $\mathfrak{m}$ (which also means that $B_{\mathfrak{n}}$ is
primary for $\mathfrak{n}$). Then there exists a finite $A$-algebra $A'$ and a maximal ideal $\mathfrak{m}'$ of $A'$ (of
which $\mathfrak{m}$ is the inverse image in $A$) such that $B_{\mathfrak{n}}$ is isomorphic to the $A$-algebra
$A'_{\mathfrak{m}'}$.*

The following particular case of (4.4.7) is also sometimes called the "Main Theorem":

**Corollary (4.4.8).**

<!-- label: III.4.4.8 -->

*Under the conditions of (4.4.7), suppose in addition that $A$ and $B$ are integral and have the same field of fractions
$K$. Then, if $A$ is integrally closed, we have $B_{\mathfrak{n}} = A$.*

**Proof.** Indeed, Remark (4.4.4) shows that we may suppose, in the application of (4.4.7), that $A'$ is integral and
has $K$ for field of fractions; the hypothesis on $A$ then implies $A' = A$, hence $B_{\mathfrak{n}} = A$; since we have
$A \subset B \subset B_{\mathfrak{n}}$, we indeed conclude $A = B$.

The statement (4.4.8) is the form given by Zariski to his "Main theorem" (extended to arbitrary Noetherian integral
local rings).

The preceding corollaries were local-type variants of (4.4.3), which is a global result. Here is another consequence of
global nature:

**Corollary (4.4.9).**

<!-- label: III.4.4.9 -->

*Let $Y$ be a locally Noetherian integral prescheme, $f : X \to Y$ a separated morphism, of finite type and birational.
Suppose in addition $Y$ normal and all the fibres $f^{-1}(y)$ finite for $y \in Y$. Then $f$ is an open immersion; if in
addition $f$ is closed (in particular if $f$ is proper), $f$ is an isomorphism.*

**Proof.** Indeed, let $x \in X$, and set $y = f(x)$. Since $f^{-1}(y)$ is an algebraic scheme over $\kappa(y)$, the
hypothesis that it is finite implies that it is discrete `(I, 6.4.4)`; in addition, $\mathcal{O}_{y}$ is integrally
closed and $\mathcal{O}_{x}$ and $\mathcal{O}_{y}$ have the same field of fractions `(I, 7.1.5)`. We may thus apply
(4.4.8), and if $f = (\psi, \theta)$, the homomorphism $\theta^{\sharp}_{x} : \mathcal{O}_{y} \to \mathcal{O}_{x}$ is
bijective; we conclude `(I, 6.5.4)` that $f$ is a local isomorphism. But since $f$ is separated and $X$ integral, $f$ is
an open immersion `(I, 8.2.8)`. The last assertion follows from the fact that $f$ is dominant.

**Proposition (4.4.10).**

<!-- label: III.4.4.10 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type. The set $X'$ of $x \in X$
isolated in their fibre $f^{-1}(f(x))$ is open in $X$.*

**Proof.** The question being local on $X$ and $Y$, we may suppose $X$ and $Y$ affine Noetherian and $f$ of finite type;
$f$ is then an affine morphism of finite type, hence quasi-projective `(II, 5.3.4, (i))`, and it suffices to apply
(4.4.3).

<!-- original page 138 -->

**Corollary (4.4.11).**

<!-- label: III.4.4.11 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism. The set $U$ of points $y \in Y$ such that
$f^{-1}(y)$ is discrete is open in $Y$, and the morphism $f^{-1}(U) \to U$ restriction of $f$ is finite. In particular,
a proper and quasi-finite morphism $X \to Y$ is finite.*

**Proof.** Indeed, the complement of $U$ in $Y$ is the image by $f$ of $X - X'$ which is closed in $X$ by virtue of
(4.4.10); since $f$ is a closed map, $U$ is open. Moreover, it follows from `(II, 6.2.2)` that $f^{-1}(y)$ is finite for
every $y \in U$; since the morphism $f^{-1}(U) \to U$ restriction of $f$ is proper `(II, 5.4.1)`, it is finite by virtue
of (4.4.2).

**Remarks (4.4.12).**

<!-- label: III.4.4.12 -->

(i) As announced in `(II, 6.2.7)`, we shall show in chap. V that if $Y$ is locally Noetherian, every quasi-finite and
separated morphism $f : X \to Y$ is quasi-affine, hence quasi-projective. It will then follow that, in the Main Theorem
(4.4.3), the conclusion remains valid when one supposes only $f$ separated and of finite type. Indeed, it follows from
(4.4.10) that $X'$ is open in $X$, and since $X$ is locally Noetherian, the restriction of $f$ to $X'$ is again of
finite type `(I, 6.3.5)`, hence quasi-finite by definition of $X'$, and obviously separated; one may therefore apply
(4.4.3) to this restriction, whence the conclusion.

(ii) We shall give in chap. IV a more elementary proof of (4.4.10), using dimension theory.

## 4.5. Completions of modules of homomorphisms

**Proposition (4.5.1).**

<!-- label: III.4.5.1 -->

*Let $A$ be a Noetherian ring, $\mathfrak{J}$ an ideal of $A$, $X$ an $A$-prescheme of finite type, $\mathcal{F}$,
$\mathcal{G}$ two coherent $\mathcal{O}_{X}$-modules whose supports have a proper intersection over $Y =
\operatorname{Spec}(A)$ `(II, 5.4.10)`. Then, for every integer $n \geq 0$, $Ext^{n}_{\mathcal{O}_{X}}(X; \mathcal{F},
\mathcal{G})$ is an $A$-module of finite type, and its Hausdorff completion for the $\mathfrak{J}$-preadic topology is
canonically identified (with the notation of (4.1.7)) with $Ext^{n}_{\mathcal{O}_{\mathfrak{X}}}(\mathfrak{X};
\hat{\mathcal{F}}, \hat{\mathcal{G}})$.*

**Proof.** We know `(T, 4.2)` that there exists a biregular spectral sequence $E(\mathcal{F}, \mathcal{G})$ whose
abutment is $Ext^{\bullet}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})$ and whose `E_2` terms are given by
$E^{p,q}_{2} = H^{p}(X, \mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))$. We know that
$\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ is a coherent $\mathcal{O}_{X}$-module
$(0_{III}, 12.3.3)$ whose support is contained in the intersection of those of $\mathcal{F}$ and $\mathcal{G}$
`(T, 4.2.2)`, and is consequently proper over $Y$ `(II, 5.4.10)`. We conclude from (3.2.4) that the $E^{p,q}_{2}$ are
$A$-modules of finite type, and consequently $(0_{III}, 11.1.8)$ so are all the terms $E^{p,q}_{r}$ of the spectral
sequence and its abutment. On the other hand, if $i : \mathfrak{X} \to X$ is the canonical morphism, $\hat{\mathcal{F}}$
and $\hat{\mathcal{G}}$ are canonically identified with $i^{*}(\mathcal{F})$ and $i^{*}(\mathcal{G})$, and $i$ is flat
`(I, 10.8.8 and 10.8.9)`. We then know $(0_{III}, 12.3.4)$ that for every $q \geq 0$, there exists a canonical
$i$-morphism $\omega_{q} : \mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}) \to
\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{\mathfrak{X}}}(\hat{\mathcal{F}}, \hat{\mathcal{G}})$, and that the
corresponding $\mathcal{O}_{\mathfrak{X}}$-homomorphism $\omega^{\sharp}_{q} :
i^{*}(\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})) \to
\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{\mathfrak{X}}}(\hat{\mathcal{F}}, \hat{\mathcal{G}})$ is an isomorphism
$(0_{III}, 12.3.5)$; in other words `(I, 10.8.8)`,
$\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{\mathfrak{X}}}(\hat{\mathcal{F}}, \hat{\mathcal{G}})$ is canonically
identified with the completion $(\mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))^{\wedge}$
(with the notation of (4.1.7)). We then conclude from the comparison theorem (4.1.10) that for every $p \geq 0$,
$H^{p}(\mathfrak{X}, \mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{\mathfrak{X}}}(\hat{\mathcal{F}}, \hat{\mathcal{G}}))$ is
canonically identified with the Hausdorff completion

<!-- original page 139 -->

of $H^{p}(X, \mathcal{E}\mathcal{xt}^{q}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))$ for the $\mathfrak{J}$-preadic
topology. If we denote by $E(\hat{\mathcal{F}}, \hat{\mathcal{G}})$ the biregular spectral sequence defined in
`(T, 4.2)` relative to $\hat{\mathcal{F}}$ and $\hat{\mathcal{G}}$, we therefore see that if `Â` denotes the Hausdorff
completion of $A$ for the $\mathfrak{J}$-preadic topology, we have, up to canonical isomorphism,
$E^{p,q}_{2}(\hat{\mathcal{F}}, \hat{\mathcal{G}}) = E^{p,q}_{2}(\mathcal{F}, \mathcal{G}) \otimes_{A} \hat{A}$ $(0_{I},
7.3.3)$.

This being so, we know that the data of the flat morphism $i$ defines a canonical homomorphism of spectral sequences

```text
  φ : E(ℱ, 𝒢) → E(ℱ̂, 𝒢̂) = E(i^*(ℱ), i^*(𝒢))
```

which, for the `E_2`-terms (resp. the abutment), reduces to the homomorphism

```text
  ω_q^♯♯ : H^p(X, 𝓔𝓍𝓉_{𝒪_X}^q(ℱ, 𝒢)) → H^p(𝔛, 𝓔𝓍𝓉_{𝒪_𝔛}^q(ℱ̂, 𝒢̂))
```

(resp. $u_{n} : Ext^{n}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G}) \to
Ext^{n}_{\mathcal{O}_{\mathfrak{X}}}(\mathfrak{X}; \hat{\mathcal{F}}, \hat{\mathcal{G}})$) deduced from $\omega_{q}$
(resp. $u_{0}$) by functoriality $(0_{III}, 12.3.4)$. By tensoring with `Â`, the $\omega^{\sharp}_{q}\sharp$ and $u_{n}$
give homomorphisms of $A$-modules

```text
  ω̃_q^♯♯ : E_2^{p,q}(ℱ, 𝒢) ⊗_A Â → E_2^{p,q}(ℱ̂, 𝒢̂),
  ũ_n   : Ext_{𝒪_X}^n(X; ℱ, 𝒢) ⊗_A Â → Ext_{𝒪_𝔛}^n(𝔛; ℱ̂, 𝒢̂).
```

Since `Â` is a flat $A$-module $(0_{I}, 7.3.3)$, the $A$-modules $E^{p,q}_{r}(\mathcal{F}, \mathcal{G}) \otimes_{A}
\hat{A}$ form a biregular spectral sequence with abutment the $Ext^{n}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})
\otimes_{A} \hat{A}$, and the $\tilde{\omega}^{\sharp}_{q}\sharp$ and $\tilde{u}_{n}$ a morphism of spectral sequences.
Since the $\tilde{\omega}^{\sharp}_{q}\sharp$ are isomorphisms, so are the $\tilde{u}_{n}$ $(0_{III}, 11.1.5)$.

**Corollary (4.5.2).**

<!-- label: III.4.5.2 -->

*Under the hypotheses of (4.5.1), suppose in addition that $A$ is a Noetherian $\mathfrak{J}$-adic ring. Then, for every
integer $n \geq 0$, $Ext^{n}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})$ is canonically identified with
$Ext^{n}_{\mathcal{O}_{\mathfrak{X}}}(\mathfrak{X}; \hat{\mathcal{F}}, \hat{\mathcal{G}})$.*

**Proof.** It suffices to remark that $Ext^{n}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})$, being an $A$-module of
finite type, is separated and complete for the $\mathfrak{J}$-preadic topology $(0_{I}, 7.3.6)$.

The particular case $n = 0$ of (4.5.1) is stated as follows:

**Corollary (4.5.3).**

<!-- label: III.4.5.3 -->

*Under the hypotheses of (4.5.1), for every homomorphism $u : \mathcal{F} \to \mathcal{G}$, denote by `û` the completed
homomorphism $\hat{\mathcal{F}} \to \hat{\mathcal{G}}$ `(I, 10.8.4)`. Then we have a canonical isomorphism*

```text
  (Hom_{𝒪_X}(ℱ, 𝒢))^∧ ⥲ Hom_{𝒪_𝔛}(ℱ̂, 𝒢̂)                                     (4.5.3.1)
```

*where the first member is the Hausdorff completion for the $\mathfrak{J}$-preadic topology of the $A$-module
$\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$, this isomorphism being obtained by passage to
Hausdorff completions from the homomorphism $u \mapsto \hat{u}$.*

## 4.6. Relations between formal morphisms and usual morphisms

**Proposition (4.6.1).**

<!-- label: III.4.6.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-module and $f$-flat, $y$ a point of $Y$. Suppose that for some*

<!-- original page 140 -->

*integer $n$, we have $H^{n}(f^{-1}(y), \mathcal{F} \otimes_{\mathcal{O}_{X}} \kappa(y)) = 0$. Then there exists a
neighbourhood $U$ of $y$ in $Y$ such that $R^{n} f_{*}(\mathcal{F}) \mid U = 0$, and for every integer $p \geq 0$, the
canonical homomorphism*

```text
  (R^{n-1} f_*(ℱ))_y → H^{n-1}(f^{-1}(y), ℱ ⊗_{𝒪_Y} (𝒪_y / 𝔪_y^{p+1}))
```

*of (4.2.1.1) is surjective.*

**Proof.** Since $R^{n} f_{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{Y}$-module (3.2.1), the first assertion of the
proposition will be established if we prove that $(R^{n} f_{*}(\mathcal{F}))_{y} = 0$ $(0_{I}, 5.2.2)$; by virtue of
(4.2.1), it suffices to prove that $H^{n}(f^{-1}(y), \mathcal{F} \otimes (\mathcal{O}_{y} / \mathfrak{m}^{p+1}_{y})) =
0$ for every $p$. This is true by hypothesis for $p = 0$; we shall prove it by induction on $p$. Set $X_{p} = X
\times_{Y} \operatorname{Spec}(\mathcal{O}_{y} / \mathfrak{m}^{p+1}_{y})$, so that $X_{p-1}$ is a closed subprescheme of
$X_{p}$, having the same underlying space `(I, 3.6.1)`; the induction hypothesis $H^{n}(X_{p-1}, \mathcal{F}
\otimes_{\mathcal{O}_{Y}} (\mathcal{O}_{y} / \mathfrak{m}^{p}_{y})) = 0$ therefore entails $H^{n}(X_{p}, \mathcal{F}
\otimes_{\mathcal{O}_{Y}} (\mathcal{O}_{y} / \mathfrak{m}^{p}_{y})) = 0$; on the other hand, the exact sequence in
cohomology gives, from the exact sequence

```text
  0 → 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ → ℱ / 𝔪_y^{p+1} ℱ → ℱ / 𝔪_y^p ℱ → 0
```

of $\mathcal{O}_{X}$-modules, the exact sequence

```text
  H^n(X_p, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) → H^n(X_p, ℱ / 𝔪_y^{p+1} ℱ) → H^n(X_p, ℱ / 𝔪_y^p ℱ)
```

and it will suffice to show that we have

```text
  H^n(X_p, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) = 0                                        (4.6.1.1)
```

for then $H^{n}(X_{p}, \mathcal{F} / \mathfrak{m}^{p+1}_{y} \mathcal{F})$ will be a submodule of $H^{n}(X_{p},
\mathcal{F} / \mathfrak{m}^{p}_{y} \mathcal{F})$, hence `0` by virtue of the induction hypothesis.

Note now that the fibre $Z = f^{-1}(y) = X \times_{Y} \operatorname{Spec}(\kappa(y))$ is a closed subprescheme of
$X_{p}$, and that $\mathfrak{m}^{p}_{y} \mathcal{F} / \mathfrak{m}^{p+1}_{y} \mathcal{F}$ is annihilated by
$\mathfrak{m}_{y}$, hence may be considered as an $\mathcal{O}_{Z}$-module, so that $H^{n}(Z, \mathfrak{m}^{p}_{y}
\mathcal{F} / \mathfrak{m}^{p+1}_{y} \mathcal{F}) = H^{n}(X_{p}, \mathfrak{m}^{p}_{y} \mathcal{F} /
\mathfrak{m}^{p+1}_{y} \mathcal{F})$. This being so, we shall show that the canonical $\mathcal{O}_{Z}$-homomorphism

```text
  (ℱ / 𝔪_y ℱ) ⊗_{κ(y)} (𝔪_y^p / 𝔪_y^{p+1}) → 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ           (4.6.1.2)
```

is bijective; this established, it will follow, since $\mathfrak{m}^{p}_{y} / \mathfrak{m}^{p+1}_{y}$ is a free
$\kappa(y)$-module, that we have

```text
  H^n(Z, 𝔪_y^p ℱ / 𝔪_y^{p+1} ℱ) = H^n(Z, ℱ / 𝔪_y ℱ) ⊗_{κ(y)} (𝔪_y^p / 𝔪_y^{p+1}) = 0
```

$(0_{III}, 12.2.3)$, since $H^{n}(Z, \mathcal{F} / \mathfrak{m}_{y} \mathcal{F}) = 0$ by hypothesis, whence (4.6.1.1).
To establish the first assertion, it remains therefore to prove that (4.6.1.2) is bijective; since the question is
pointwise on $X$ and $\mathcal{F}_{x}$ is an $\mathcal{O}_{y}$-flat module by hypothesis for every $x \in f^{-1}(y)$, it
suffices to apply `(0_III, 10.2.1, c))`, since $\mathcal{F}_{x} / \mathfrak{m}_{y} \mathcal{F}_{x}$ is a flat module
over the field $\kappa(y) = \mathcal{O}_{y} / \mathfrak{m}_{y}$.

To prove the second assertion of (4.6.1), we reduce at once, as in (4.2.1), to the case where $Y$ is affine and $y$
closed. Note that (4.6.1.1) gives, by an analogous reasoning, for every $k > 0$, the relation

```text
  H^n(X_{p+k}, 𝔪_y^p ℱ / 𝔪_y^{p+k+1} ℱ) = 0                                  (4.6.1.3)
```

<!-- original page 141 -->

whence one deduces, by (4.2.1), that we also have

$$ (R^{n} f_{*}(\mathfrak{m}^{p}_{y} \mathcal{F}))_{y} = 0. (4.6.1.4) $$

This being so, one draws from the exact sequence in cohomology the exactness of the sequence

```text
  (R^{n-1} f_*(ℱ))_y → (R^{n-1} f_*(ℱ / 𝔪_y^p ℱ))_y → (R^n f_*(𝔪_y^p ℱ))_y = 0
```

and since $y$ is closed and $Y$ affine, we have (1.4.11)

```text
  R^{n-1} f_*(ℱ / 𝔪_y^p ℱ) = (H^{n-1}(X, ℱ / 𝔪_y^p ℱ))^∼ = (H^{n-1}(f^{-1}(y), ℱ / 𝔪_y^p ℱ))^∼
```

`(G, II, 4.9.1)`; now $H^{n-1}(f^{-1}(y), \mathcal{F} / \mathfrak{m}^{p}_{y} \mathcal{F})$ is an $(\mathcal{O}_{y} /
\mathfrak{m}^{p}_{y})$-module, whence

```text
  (R^{n-1} f_*(ℱ / 𝔪_y^p ℱ))_y = H^{n-1}(f^{-1}(y), ℱ / 𝔪_y^p ℱ)
```

and this completes the proof of (4.6.1).

**Corollary (4.6.2).**

<!-- label: III.4.6.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper and flat morphism, $\mathcal{F}$, $\mathcal{G}$ two
locally free $\mathcal{O}_{X}$-modules, $y$ a point of $Y$. Set $X_{y} = f^{-1}(y) = X \otimes_{\mathcal{O}_{Y}}
\kappa(y)$, $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} \kappa(y)$, $\mathcal{G}_{y} = \mathcal{G}
\otimes_{\mathcal{O}_{Y}} \kappa(y)$, and suppose that*

$$ H^{1}(X_{y}, \operatorname{Hom}_{\mathcal{O}_{X_{y}}}(\mathcal{F}_{y}, \mathcal{G}_{y})) = 0. (4.6.2.1) $$

*Then, for every homomorphism $u_{0} : \mathcal{F}_{y} \to \mathcal{G}_{y}$, there exists an open neighbourhood $U$ of
$y$ and a homomorphism $u : \mathcal{F} \mid f^{-1}(U) \to \mathcal{G} \mid f^{-1}(U)$ such that $u_{y}$ is equal to the
homomorphism $u_{0} \otimes 1$.*

**Proof.** Indeed, the hypothesis permits applying (4.6.1) to the coherent $\mathcal{O}_{X}$-module $\mathcal{H} =
\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ for $n = 1$ and $p = 0$, for $\mathcal{F}$ is locally
free and *a fortiori* $f$-flat, and the $\mathcal{O}_{X_{y}}$-module $\mathcal{H} \otimes_{\mathcal{O}_{Y}} \kappa(y)$
is then identified with $\operatorname{Hom}_{\mathcal{O}_{X_{y}}}(\mathcal{F}_{y}, \mathcal{G}_{y})$ $(0_{I}, 6.2.2)$.
We may suppose $Y = \operatorname{Spec}(A)$ affine, and then (1.4.11) $R^{0} f_{*}(\mathcal{H}) =
(\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))^{\sim}$, hence $(R^{0} f_{*}(\mathcal{H}))_{y} =
\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}) \otimes_{A} \mathcal{O}_{y}$; the canonical homomorphism

```text
  Hom_{𝒪_X}(ℱ, 𝒢) ⊗_A 𝒪_y → Hom_{𝒪_{X_y}}(ℱ_y, 𝒢_y)
```

being surjective by (4.6.1), this establishes the corollary, since every element of
$\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}) \otimes_{A} \mathcal{O}_{y}$ may always be put under the
form $u_{0} \otimes (1/s)$, where $s \notin \mathfrak{m}_{y}$ is an element of $A$.

This corollary can be supplemented by the following:

**Corollary (4.6.3).**

<!-- label: III.4.6.3 -->

*Under the hypotheses of (4.6.2), if $u_{0}$ is injective (resp. surjective, bijective), one may suppose that the same
holds for $u$.*

**Proof.** We may restrict to the case where $U = Y$. It suffices to prove that if $u_{0}$ is injective (resp.
surjective), $Ker u_{x} = 0$ (resp. $Coker u_{x} = 0$) for every $x \in f^{-1}(y)$: indeed, `Ker u` and `Coker u` are
coherent $\mathcal{O}_{X}$-modules $(0_{I}, 5.3.4)$, so there will exist a neighbourhood $V$ of $f^{-1}(y)$ in $X$ such
that the restriction of `Ker u` (resp. `Coker u`) to $V$ is `0` $(0_{I}, 5.2.2)$; since $f$ is closed, there will exist
a neighbourhood $U' \subset U$ of $y$ such that $f^{-1}(U') \subset V$, and (4.6.3) will be proved. By hypothesis,
$u_{0} \otimes 1 : \mathcal{F}_{x} \otimes_{\mathcal{O}_{x}} \kappa(y) \to \mathcal{G}_{x} \otimes_{\mathcal{O}_{x}}
\kappa(y)$ is injective (resp. surjective),

<!-- original page 142 -->

$\mathcal{F}_{x}$ and $\mathcal{G}_{x}$ are free $\mathcal{O}_{x}$-modules of finite type and $\mathcal{O}_{x}$ is a
flat $\mathcal{O}_{y}$-module. When we suppose $u_{0} \otimes 1$ injective, the fact that $u_{x}$ is injective results
from $(0_{III}, 10.2.4)$. When we suppose $u_{0} \otimes 1$ surjective, *a fortiori* the homomorphism $\mathcal{F}_{x} /
\mathfrak{m}_{y} \mathcal{F}_{x} \to \mathcal{G}_{x} / \mathfrak{m}_{y} \mathcal{G}_{x}$ which is deduced from it by
passage to quotients, is surjective; since $\mathcal{G}_{x}$ is an $\mathcal{O}_{x}$-module of finite type and
$\mathcal{O}_{x}$ is a local ring of maximal ideal $\mathfrak{m}_{x}$, the conclusion follows from Nakayama's lemma
(Bourbaki, *Alg.*, chap. VIII, § 6, n° 3, cor. 4 of prop. 6).

One deduces in particular from (4.6.3):

**Corollary (4.6.4).**

<!-- label: III.4.6.4 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper and flat morphism, $y$ a point of $Y$, $X_{y} = X
\otimes_{Y} \kappa(y)$. Let $\mathcal{E}_{y}$ be a locally free $\mathcal{O}_{X_{y}}$-module such that*

$$ H^{1}(X_{y}, \operatorname{Hom}_{\mathcal{O}_{X_{y}}}(\mathcal{E}_{y}, \mathcal{E}_{y})) = 0. (4.6.4.1) $$

*Let $\mathcal{F}$, $\mathcal{G}$ be two locally free $\mathcal{O}_{X}$-modules such that $\mathcal{F}_{y}$ and
$\mathcal{G}_{y}$ (with the notation of (4.6.2)) are isomorphic to $\mathcal{E}_{y}$. Then there exists an open
neighbourhood $U$ of $y$ such that $\mathcal{F} \mid f^{-1}(U)$ and $\mathcal{G} \mid f^{-1}(U)$ are isomorphic.*

More particularly:

**Corollary (4.6.5).**

<!-- label: III.4.6.5 -->

*Under the hypotheses of (4.6.4) on $f$, $X$, $Y$, suppose that $H^{1}(X_{y}, \mathcal{O}_{X_{y}}) = 0$. If
$\mathcal{L}$ and $\mathcal{S}$ are two invertible $\mathcal{O}_{X}$-modules such that $\mathcal{L}_{y}$ and
$\mathcal{S}_{y}$ are isomorphic, there exists an open neighbourhood $U$ of $y$ such that $\mathcal{L} \mid f^{-1}(U)$
and $\mathcal{S} \mid f^{-1}(U)$ are isomorphic.*

**Proof.** It suffices to apply (4.6.4) to the modules $\mathcal{L}^{-1} \otimes \mathcal{S}$ and $\mathcal{O}_{X}$.

**Remarks (4.6.6).**

<!-- label: III.4.6.6 -->

(i) Using (4.6.5), we shall establish in chap. V the classification of invertible sheaves on a projective fibre,
announced in `(II, 4.2.7)`.

(ii) The result of (4.6.1) will appear in § 7 as a consequence of more general propositions.

**Proposition (4.6.7).**

<!-- label: III.4.6.7 -->

*Let $Z$ be a locally Noetherian prescheme, $X$, $Y$ two $Z$-preschemes such that the structure morphisms $g : X \to Z$,
$h : Y \to Z$ are proper. Let $f : X \to Y$ be a $Z$-morphism, $z$ a point of $Z$, and let $f_{z} = f \otimes_{Z} 1 : X
\otimes_{Z} \kappa(z) \to Y \otimes_{Z} \kappa(z)$.*

*(i) If $f_{z}$ is a finite morphism (resp. a closed immersion), there exists an open neighbourhood $U$ of $z$ such that
the morphism $g^{-1}(U) \to h^{-1}(U)$, restriction of $f$, is a finite morphism (resp. a closed immersion).*

*(ii) Suppose in addition that $g$ is a flat morphism. Then, if $f_{z}$ is an isomorphism, there exists an open
neighbourhood $U$ of $z$ such that the morphism $g^{-1}(U) \to h^{-1}(U)$, restriction of $f$, is an isomorphism.*

**Proof.** In both cases, it will suffice to prove that for every $y \in h^{-1}(z)$, there exists a neighbourhood
$V_{y}$ of $y$ such that the restriction $f^{-1}(V_{y}) \to V_{y}$ of $f$ is a finite morphism (resp. a closed
immersion, an isomorphism); it will then follow that if $V$ is the union of the $V_{y}$, the restriction $f^{-1}(V) \to
V$ of $f$ is a finite morphism (resp. a closed immersion, an isomorphism) `(II, 6.1.1 and I, 4.2.4)`. Since $h$ is a
closed morphism, there will exist an open neighbourhood $U$ of $z$ such that $h^{-1}(U) \subset V$, and the proposition
will be proved.

(i) Note first that $f$ is a proper morphism `(II, 5.4.3)`; if we

<!-- original page 143 -->

suppose $f_{z}$ finite, the existence for every $y \in h^{-1}(z)$ of a neighbourhood $V_{y}$ such that $f^{-1}(V_{y})
\to V_{y}$ is finite results from (4.4.11). To treat the case where $f_{z}$ is a closed immersion, we may therefore
already suppose that the morphism $f$ is finite, hence $X = \operatorname{Spec}(\mathcal{B})$, where $\mathcal{B}$ is a
coherent $\mathcal{O}_{Y}$-algebra, the morphism $f$ corresponding `(II, 1.2.7)` to the canonical homomorphism $u :
\mathcal{O}_{Y} \to \mathcal{B}$. If we prove that for every $y \in h^{-1}(z)$, the homomorphism $u_{y} :
\mathcal{O}_{y} \to \mathcal{B}_{y}$ is surjective, it will follow that for a neighbourhood $V_{y}$ of $y$, $u \mid
V_{y}$ is surjective, the sheaf `Coker u` being coherent $(0_{I}, 5.3.4 and 5.2.2)$. This being so, the finite morphism
$f_{z}$ corresponds to the homomorphism $v = u \otimes 1 : \mathcal{O}_{Y} \otimes_{\mathcal{O}_{Z}} \kappa(z) \to
\mathcal{B} \otimes_{\mathcal{O}_{Z}} \kappa(z)$, and the hypothesis that $f_{z}$ is a closed immersion implies that the
homomorphism $u \otimes 1 : \mathcal{O}_{y} \otimes_{\mathcal{O}_{z}} \kappa(z) \to \mathcal{B}_{y}
\otimes_{\mathcal{O}_{z}} \kappa(z)$ is surjective. Since $\mathcal{B}_{y}$ is an $\mathcal{O}_{y}$-module of finite
type and $\mathcal{O}_{y}$ is a Noetherian local ring, the conclusion results as in (4.6.3) from Nakayama's lemma.

(ii) The same reasoning as above shows that it suffices this time to prove that $u_{y}$ is bijective, knowing that
$u_{y} \otimes 1$ is bijective.

This will result from the following lemma:

**Lemma (4.6.7.1).**

<!-- label: III.4.6.7.1 -->

*Let $A$, $B$ be two Noetherian local rings, $\rho : A \to B$ a local homomorphism, $u : N \to M$ a homomorphism of
$B$-modules. Suppose that $M$ is a flat $A$-module, $N$ a $B$-module of finite type and that $u \otimes 1 : N
\otimes_{A} k \to M \otimes_{A} k$ (where $k$ is the residue field of $A$) is injective. Then $N$ is a flat $A$-module
and $u$ is injective.*

**Proof.** To establish the first assertion, we must show that for every pair of $A$-modules of finite type $P$, $Q$ and
every injective $A$-homomorphism $v : P \to Q$, $1_{N} \otimes v : N \otimes_{A} P \to N \otimes_{A} Q$ is injective.
Now, we have the commutative diagram

```text
  N ⊗_A P ───^{1_N ⊗ v}───→ N ⊗_A Q
      ↓ u ⊗ 1_P                  ↓ u ⊗ 1_Q
  M ⊗_A P ───^{1_M ⊗ v}───→ M ⊗_A Q
```

and since $1_{M} \otimes v$ is injective by hypothesis, it suffices to prove the same for $u \otimes 1_{P}$. Let
$\mathfrak{m}$ be the maximal ideal of $A$; the $\mathfrak{m}$-adic filtration on the $A$-module $N \otimes_{A} P$ is
also its $\mathfrak{m}B$-adic filtration as a $B$-module; the topology defined by this filtration is therefore
separated, since $B$ is Noetherian, $\mathfrak{m}B$ is contained in the radical of $B$, and $N \otimes_{A} P$ is a
$B$-module of finite type, $N$ being a $B$-module of finite type and $P$ an $A$-module of finite type $(0_{I}, 7.3.5)$.
It therefore suffices to prove that the homomorphism $gr(u \otimes 1_{P}) : gr_{\bullet}(N \otimes_{A} P) \to
gr_{\bullet}(M \otimes_{A} P)$ (where the graded modules are relative to the $\mathfrak{m}$-adic filtrations) is
injective (Bourbaki, *Alg. comm.*, chap. III, § 2, n° 8, cor. 1 of th. 1). Note now that since $M$ is a flat $A$-module,
the homomorphisms $M \otimes_{A} (\mathfrak{m}^{n} P) \to \mathfrak{m}^{n}(M \otimes_{A} P)$ are bijective; the same
therefore holds for the canonical homomorphism

```text
  φ_M : gr_0(M) ⊗_A gr_•(P) → gr_•(M ⊗_A P).
```

<!-- original page 144 -->

Now we have a commutative diagram

```text
  gr_0(N) ⊗_A gr_•(P) ──^{gr(u) ⊗ 1}──→ gr_0(M) ⊗_A gr_•(P)
        ↓ φ_N                                      ↓ φ_M
  gr_•(N ⊗_A P)       ──^{gr(u ⊗ 1_P)}──→ gr_•(M ⊗_A P)
```

in which $\phi_{M}$ is bijective, $\phi_{N}$ surjective; moreover, $gr(u)$ is injective by hypothesis, and since
$gr_{0}(N) \otimes_{A} gr_{\bullet}(P) = gr_{0}(N) \otimes_{k} gr_{\bullet}(P)$, $gr_{0}(M) \otimes_{A} gr_{\bullet}(P)
= gr_{0}(M) \otimes_{k} gr_{\bullet}(P)$, $gr(u) \otimes 1$ is also injective. We conclude that $gr(u \otimes 1)$ is
injective, which completes the proof of the first assertion. The second is deduced from the preceding reasoning on
taking $P = A$.

**Proposition (4.6.8).**

<!-- label: III.4.6.8 -->

*Let $Z$ be a locally Noetherian prescheme, $X$, $Y$ two $Z$-preschemes such that the structure morphisms $g : X \to Z$,
$h : Y \to Z$ are proper, $Z'$ a closed part of $Z$, $X' = g^{-1}(Z')$, $Y' = h^{-1}(Z')$ its inverse images,
$\mathfrak{X} = X_{/X'}$, $\mathfrak{Y} = Y_{/Y'}$, $\mathfrak{z} = Z_{/Z'}$ the formal completions of $X$, $Y$, $Z$
along these closed parts, $f : X \to Y$ a $Z$-morphism, $\hat{\mathit{f}} : \mathfrak{X} \to \mathfrak{Y}$ its extension
to the completions. For $\hat{\mathit{f}}$ to be an isomorphism (resp. a closed immersion), it is necessary and
sufficient that there exists an open neighbourhood $U$ of $Z'$ such that the morphism $g^{-1}(U) \to h^{-1}(U)$,
restriction of $f$, is an isomorphism (resp. a closed immersion).*

**Proof.** The sufficiency of the condition is immediate `(I, 10.14.7)`. To show its necessity, it suffices again to
prove that for every $y \in Y'$, there exists an open neighbourhood $V_{y}$ of $y$ such that the restriction
$f^{-1}(V_{y}) \to V_{y}$ of $f$ is an isomorphism (resp. a closed immersion), by the same reasoning as in (4.6.7). We
are thus reduced to the case where $Y = Z$, $Y = \operatorname{Spec}(A)$ being affine Noetherian. By hypothesis
`(I, 10.9.1 and 10.14.2)` the fibre $f^{-1}(y)$ is reduced to a point for $y \in Y'$, hence since $f$ is proper
`(II, 5.4.3)`, there exists an open neighbourhood $U$ of $y$ such that the restriction $f^{-1}(U) \to U$ of $f$ is a
finite morphism (4.4.11). We may therefore already suppose that $f$ is a finite morphism, hence $X =
\operatorname{Spec}(B)$, where $B$ is an $A$-algebra finite over $A$. If $Y' = V(\mathfrak{J})$, we then have
$\mathfrak{Y} = Spf(\hat{A})$, $\mathfrak{X} = Spf(\hat{B})$, `Â` being the Hausdorff completion of $A$ for the
$\mathfrak{J}$-preadic topology, $\hat{B}$ the Hausdorff completion of $B$ for the $\mathfrak{J}B$-preadic topology, or
(which amounts to the same thing), the Hausdorff completion of the $A$-module $B$ for the $\mathfrak{J}$-preadic
topology; moreover, $\hat{\mathit{f}}$ is the morphism of affine formal schemes corresponding to the continuous
extension $\hat{\phi} : \hat{A} \to \hat{B}$ of the canonical homomorphism of rings $\phi : A \to B$, and the hypothesis
is that $\hat{\phi}$ is surjective (resp. bijective) `(I, 10.14.2)`. Now, $\hat{\phi}$ is also the continuous extension
of $\phi$ considered as a homomorphism of $A$-modules; we know then `(I, 10.8.14)` that there exists an open
neighbourhood $U$ of $Y'$ such that the restriction to $U$ of the homomorphism $\tilde{\phi} : \tilde{A} \to \tilde{B}$
of $\mathcal{O}_{Y}$-modules is surjective (resp. bijective), which completes the proof.

<!-- original page 145 -->

## 4.7. An ampleness criterion

**Theorem (4.7.1).**

<!-- label: III.4.7.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module, $y$ a point of $Y$, $X_{y} = X \otimes_{Y} \kappa(y) = f^{-1}(y)$, $q$ the projection of
$X_{y}$ into $X$. If $\mathcal{L}_{y} = q^{*}(\mathcal{L}) = \mathcal{L} \otimes_{\mathcal{O}_{Y}} \kappa(y)$ is ample
on $X_{y}$, there exists an open neighbourhood $U$ of $y$ in $Y$ such that $\mathcal{L} \mid f^{-1}(U)$ is ample for the
restriction of $f$ to $f^{-1}(U)$.*

**Proof.**

I) Set $Y' = \operatorname{Spec}(\mathcal{O}_{y})$, $X' = X \times_{Y} Y'$, and let $\mathcal{L}' = \mathcal{O}_{X'}
\otimes_{\mathcal{O}_{X}} \mathcal{L}$; we shall first prove that $\mathcal{L}'$ is ample for $f' = f_{(Y')}$. We have
the commutative diagram

```text
  X ←──── X' ←──── X_y
  ↓ f      ↓ f'      ↓
  Y ←──── Y' ←──── Spec(κ(y))
```

Since $f'$ is proper `(II, 5.4.2, (iii))` and $\mathcal{O}_{y}$ Noetherian, we see that we may restrict to the case
where $Y = Y' = \operatorname{Spec}(\mathcal{O}_{y})$, hence $X = X'$, suppose $\mathcal{L}_{y}$ ample for $f_{y}$, and
prove that $\mathcal{L}$ is ample for $f$ `(II, 4.6.6)`. We shall apply the criterion `(2.6.1, b))` and shall in fact
show that for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, there exists an integer $N$ such that $H^{q}(X,
\mathcal{F}(n)) = 0$ for every $n \geq N$, with $\mathcal{F}(n) = \mathcal{F} \otimes_{\mathcal{O}_{X}}
\mathcal{L}^{\otimes n}$. Note that $y$ is a closed point of $Y$ corresponding to the maximal ideal $\mathfrak{m}$ of
$\mathcal{O}_{y}$; $X_{y}$ is therefore a closed subprescheme of $X$ defined by the coherent ideal $\mathcal{J} =
f^{*}(\tilde{\mathfrak{m}}) \mathcal{O}_{X} = \mathfrak{m} \mathcal{O}_{X}$ of $\mathcal{O}_{X}$ `(I, 4.4.5)`, and $q$
the canonical injection. Consider then the graded $\kappa(y)$-algebra $S = gr(\mathcal{O}_{y}) = \oplus_{k \geq 0}
\mathfrak{m}^{k} / \mathfrak{m}^{k+1}$, which is of finite type since $\mathcal{O}_{y}$ is Noetherian; the
$\mathcal{O}_{X}$-algebra $\mathcal{S} = f^{*}(\tilde{S})$ is therefore quasi-coherent and of finite type, and it is
obviously annihilated by $\mathcal{J}$, so if we set $\mathcal{S}_{y} = q^{*}(\mathcal{S})$, $\mathcal{S}_{y}$ is a
quasi-coherent $\mathcal{O}_{X_{y}}$-algebra of finite type, and $\mathcal{S}_{y} = \tilde{q}^{*}(\tilde{S})$. Set, on
the other hand, $\mathcal{M}_{k} = \mathfrak{m}^{k} \mathcal{F} / \mathfrak{m}^{k+1} \mathcal{F}$ and $\mathcal{M} =
\oplus_{k \geq 0} \mathcal{M}_{k} = gr(\mathcal{F})$; since $\mathcal{F}$ is coherent, $\mathcal{M}$ is a quasi-coherent
$\mathcal{O}_{X}$-module of finite type $(0_{III}, 10.1.1)$ which is also annihilated by $\mathcal{J}$, so if we set
$\mathcal{M}_{y} = q^{*}(\mathcal{M})$, $\mathcal{M}_{y} = q^{*}(\mathcal{M}) = \oplus_{j} \mathcal{M}'_{j}$ is a
quasi-coherent graded $\mathcal{S}_{y}$-module of finite type such that $\mathcal{M} = q_{*}(\mathcal{M}_{y})$.
Moreover, if we set $\mathcal{M}_{y}(n) = \mathcal{M}_{y} \otimes_{\mathcal{O}_{X_{y}}} \mathcal{L}^{\otimes n}_{y}$, we
have $\mathcal{M}_{y}(n) = q^{*}(\mathcal{M}(n))$. This being so, $f_{y}$ is proper `(II, 5.4.2, (iii))` and
$\mathcal{L}_{y}$ ample, so $f_{y}$ is projective `(II, 5.5.4 and 4.6.11)`, and we may apply to
$\operatorname{Spec}(\kappa(y))$, $f_{y}$, $\mathcal{S}_{y}$, $\mathcal{L}_{y}$ and $\mathcal{M}_{y}$ the theorem
`(2.4.1, (ii))`: there exists an integer $N$ such that for $n \geq N$, we have $H^{q}(X_{y}, \mathcal{M}_{y}(n)) = 0$
for every $q > 0$ and every $j$; consequently, we also have $H^{q}(X, \mathcal{M}_{j}(n)) = 0$ for every $q > 0$ and
every $j$ `(G, II, 4.9.1)`. Set then $\mathcal{F}(n)_{j} = \mathcal{F}(n) / \mathfrak{m}^{j+1} \mathcal{F}(n)$, so that
$\mathcal{M}_{j}(n) = \mathcal{F}(n)_{j} / \mathcal{F}(n)_{j-1}$ for $j \geq 1$ and $\mathcal{M}_{0}(n) =
\mathcal{F}(n)_{0}$. We have $H^{q}(X, \mathcal{F}(n)_{0}) = 0$, and, by the exact sequence of cohomology, $H^{q}(X,
\mathcal{F}(n)_{j}) = H^{q}(X, \mathcal{F}(n)_{j-1})$ for every $j \geq 1$, hence $H^{q}(X, \mathcal{F}(n)_{j}) = 0$ for
every $j \geq 0$. We conclude from (4.2.1) that $H^{q}(X, \mathcal{F}(n)) = 0$, which completes the proof of our
assertion.

II) Returning to the notation of the beginning of the proof, note that we

<!-- original page 146 -->

may always suppose $Y = \operatorname{Spec}(A)$ affine; since $f'$ is of finite type and $\mathcal{L}'$ ample for $f'$,
there exists an integer $m > 0$ such that $\mathcal{L}'^{\otimes m}$ is very ample for $f'$ `(II, 4.6.11)`; replacing
$\mathcal{L}$ by $\mathcal{L}^{\otimes m}$ if necessary, we may restrict to considering the case where $\mathcal{L}'$ is
very ample for $f'$, and prove that $\mathcal{L} \mid f^{-1}(U)$ is then very ample for $f$. Since $f'$ is proper, there
then exists a $Y'$-closed immersion $j : X' \to P = P^{r}_{Y'}$ for a suitable integer $r > 0$, such that $\mathcal{L}'$
is isomorphic to $j^{*}(\mathcal{O}_{P}(1))$ `(II, 5.5.4, (ii))`; this immersion corresponds canonically to a surjective
$\mathcal{O}_{X'}$-homomorphism $u : \mathcal{O}^{r+1}_{X'} \to \mathcal{L}'$ `(II, 4.2.3)`. The latter corresponds
$(0_{I}, 5.1.1)$ to the data of $r + 1$ sections $s'_{i}$ ($0 \leq i \leq r$) of $\mathcal{L}'$ over $X'$ which generate
this $\mathcal{O}_{X'}$-module. These sections are also by definition sections of $f'_{*}(\mathcal{L}')$ over $Y'$; we
have $f'_{*}(\mathcal{L}') = f_{*}(\mathcal{L}) \otimes_{A} \mathcal{O}_{y}$ $(0_{I}, 5.4.10)$, $Y$ is affine and
$\mathcal{O}_{y}$ is the local ring at the prime ideal $\mathfrak{p}_{y}$ of $A$, so we have $s'_{i} = s''_{i} / t_{i}$,
where the $s''_{i}$ are sections of $f_{*}(\mathcal{L})$ over $Y$ and the $t_{i}$ elements of $A$ not belonging to
$\mathfrak{p}_{y}$; we conclude that there exists an affine open neighbourhood $V$ of $y$ in $Y$ and sections $s_{i}$ of
$f_{*}(\mathcal{L}) \mid V$ such that $s'_{i} = s_{i} / 1$ (recall that the space $Y'$ is contained in $V$, cf.
`I, 2.4.2`). The $s_{i}$ are then sections of $\mathcal{L}$ over $f^{-1}(V)$, defining therefore a homomorphism $v :
(\mathcal{O}_{X} \mid f^{-1}(V))^{r+1} \to \mathcal{L} \mid f^{-1}(V)$ which, by hypothesis, is surjective at every
point of $f^{-1}(y)$; since $Coker(v)$ is coherent $(0_{I}, 5.3.4)$, its support is closed $(0_{I}, 5.2.2)$ and
consequently there exists an open neighbourhood $W \subset f^{-1}(V)$ of $f^{-1}(y)$ such that the restriction of $v$ to
$W$ is a surjective homomorphism. Since the morphism $f$ is closed, we may suppose that $W$ is of the form $f^{-1}(U)$,
where $U$ is an open neighbourhood of $y$, and the conclusion then follows from `(II, 4.2.3)`.

## 4.8. Finite morphisms of formal preschemes

**Proposition (4.8.1).**

<!-- label: III.4.8.1 -->

*Let $\mathfrak{Y}$ be a locally Noetherian formal prescheme, $\mathcal{K}$ an ideal of definition of $\mathfrak{Y}$,
$f : \mathfrak{X} \to \mathfrak{Y}$ a morphism of formal preschemes. The following conditions are equivalent:*

*a) $\mathfrak{X}$ is locally Noetherian, $f$ is an adic morphism `(I, 10.12.1)` and if we set $\mathcal{J} =
f^{*}(\mathcal{K}) \mathcal{O}_{\mathfrak{X}}$, the morphism $f_{0} : (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} /
\mathcal{J}) \to (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / \mathcal{K})$ deduced from $f$ is finite.*

*b) $\mathfrak{X}$ is locally Noetherian and is the inductive limit of a $(Y_{n})$-inductive adic system $(X_{n})$ such
that the morphism $X_{0} \to Y_{0}$ is finite.*

*c) Every point of $\mathfrak{Y}$ possesses a Noetherian affine formal open neighbourhood $V$ such that $f^{-1}(V)$ is
an affine formal open set and that $\Gamma(f^{-1}(V), \mathcal{O}_{\mathfrak{X}})$ is a $\Gamma(V,
\mathcal{O}_{\mathfrak{Y}})$-module of finite type.*

**Proof.** It is immediate that a) implies b) by virtue of `(I, 10.12.3)`. To see that b) implies c), we may suppose
that $\mathfrak{Y} = Spf(B)$, where $B$ is adic Noetherian and $\mathcal{K} = \tilde{\mathfrak{J}}$, where
$\mathfrak{J}$ is an ideal of definition of $B$. By hypothesis, `X_0` is an affine scheme whose ring `A_0` is a
$B/\mathfrak{J}$-module of finite type `(II, 6.1.3)`. By virtue of `(I, 5.1.9)`, each of the $X_{n}$ is an affine
scheme, and if $A_{n}$ is its ring, hypothesis b) implies that for $m \leq n$, $A_{m}$ is isomorphic to $A_{n} /
\mathfrak{J}^{m+1} A_{n}$. We deduce that $\mathfrak{X}$ is isomorphic to $Spf(A)$, where $A = \varprojlim A_{n}$; one
concludes by virtue of $(0_{I}, 7.2.9)$. Finally, to prove that c)

<!-- original page 147 -->

implies a), we may again restrict to the case where $\mathfrak{Y} = Spf(B)$, $\mathfrak{X} = Spf(A)$, $A$ being a finite
$B$-algebra; since $A / \mathfrak{J}A$ is then a finite $B/\mathfrak{J}$-algebra, it follows from `(I, 10.10.9)` that
the conditions of a) are satisfied.

**Definition (4.8.2).**

<!-- label: III.4.8.2 -->

*When the equivalent properties a), b), c) of (4.8.1) are satisfied, we say that the morphism $f$ is *finite*, or that
$\mathfrak{X}$ is a finite $\mathfrak{Y}$-formal prescheme, or a finite formal prescheme over $\mathfrak{Y}$.*

**Proposition (4.8.3).**

<!-- label: III.4.8.3 -->

*(i) A closed immersion of locally Noetherian formal preschemes is a finite morphism.*

*(ii) The composition of two finite morphisms of locally Noetherian formal preschemes is a finite morphism.*

*(iii) Let $\mathfrak{X}$, $\mathfrak{Y}$, $\mathfrak{S}$ be three locally Noetherian formal preschemes, $f :
\mathfrak{X} \to \mathfrak{S}$ a finite morphism, $g : \mathfrak{Y} \to \mathfrak{S}$ a morphism; then the morphism
$\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y} \to \mathfrak{Y}$ is finite.*

*(iv) Let $\mathfrak{S}$ be a locally Noetherian formal prescheme, $\mathfrak{X}'$, $\mathfrak{Y}'$ two locally
Noetherian formal preschemes such that $\mathfrak{X}' \times_{\mathfrak{S}} \mathfrak{Y}'$ is locally Noetherian. If
$\mathfrak{X}$, $\mathfrak{Y}$ are locally Noetherian $\mathfrak{S}$-formal preschemes, $f : \mathfrak{X} \to
\mathfrak{X}'$, $g : \mathfrak{Y} \to \mathfrak{Y}'$ two finite $\mathfrak{S}$-morphisms, then $f \times_{\mathfrak{S}}
g$ is a finite morphism.*

*(v) Let $f : \mathfrak{X} \to \mathfrak{Y}$, $g : \mathfrak{Y} \to \mathfrak{S}$ be two morphisms of locally Noetherian
formal preschemes such that $g$ is of finite type and separated; then, if $g \circ f$ is a finite morphism, $f$ is a
finite morphism.*

**Proof.** (i) is trivial, and the other assertions reduce immediately to the corresponding propositions for morphisms
of usual preschemes `(II, 6.1.5)` by means of the criterion a) of (4.8.1); we leave the details to the reader, modelled
on `(I, 10.13.5)`.

**Corollary (4.8.4).**

<!-- label: III.4.8.4 -->

*Under the hypotheses of `(I, 10.9.9)`, if $f$ is a finite morphism, the same holds for its extension $\hat{\mathit{f}}$
to the completions.*

**Corollary (4.8.5).**

<!-- label: III.4.8.5 -->

*If $\mathfrak{X}$ is a finite formal prescheme over $\mathfrak{Y}$, $f : \mathfrak{X} \to \mathfrak{Y}$ the structure
morphism, then, for every open set $U \subset \mathfrak{Y}$, $f^{-1}(U)$ is finite over $U$.*

**Proposition (4.8.6).**

<!-- label: III.4.8.6 -->

*If $f : \mathfrak{X} \to \mathfrak{Y}$ is a finite morphism of locally Noetherian formal preschemes,
$f_{*}(\mathcal{O}_{\mathfrak{X}})$ is a coherent $\mathcal{O}_{\mathfrak{Y}}$-algebra.*

**Proof.** One may consider $f$ as the inductive limit of an inductive system $(f_{n})$ of morphisms $f_{n} : X_{n} \to
Y_{n}$; we shall show that the $f_{n}$ are finite morphisms and that $f_{*}(\mathcal{O}_{\mathfrak{X}})$ is isomorphic
to the projective limit of the $(f_{n})_{*}(\mathcal{O}_{X_{n}})$, which will establish our assertion `(I, 10.10.5)`. It
suffices to restrict to the case where $\mathfrak{Y} = Spf(B)$, $\mathfrak{X} = Spf(A)$, and to remark that if
$\mathfrak{J}$ is an ideal of definition of $B$ and $A$ a $B$-module of finite type, $A / \mathfrak{J}^{n+1} A$ is a
module of finite type over $B / \mathfrak{J}^{n+1} B$, and that $A$ is the projective limit of the $A /
\mathfrak{J}^{n+1} A$.

Conversely:

**Proposition (4.8.7).**

<!-- label: III.4.8.7 -->

*Let $\mathfrak{Y}$ be a locally Noetherian formal prescheme, $\mathcal{A}$ a coherent
$\mathcal{O}_{\mathfrak{Y}}$-algebra. There exists a formal prescheme $\mathfrak{X}$ finite over $\mathfrak{Y}$, defined
up to $\mathfrak{Y}$-isomorphism unique, and such that $f_{*}(\mathcal{O}_{\mathfrak{X}}) = \mathcal{A}$, $f :
\mathfrak{X} \to \mathfrak{Y}$ being the structure morphism.*

**Proof.** Let $\mathcal{K}$ be an ideal of definition of $\mathfrak{Y}$, and set $Y_{n} = (\mathfrak{Y},
\mathcal{O}_{\mathfrak{Y}} / \mathcal{K}^{n+1})$ and $\mathcal{A}_{n} = \mathcal{A} / \mathcal{K}^{n+1} \mathcal{A}$; it
is clear that $\mathcal{A}_{n}$ is a finite $\mathcal{O}_{Y_{n}}$-algebra and defines therefore a

<!-- original page 148 -->

$Y_{n}$-prescheme finite $X_{n} = \operatorname{Spec}(\mathcal{A}_{n})$ `(II, 6.1.3)`; for $m \leq n$, the canonical
surjective homomorphism $h_{nm} : \mathcal{A}_{n} \to \mathcal{A}_{m}$ defines a morphism $u_{nm} : X_{m} \to X_{n}$
such that the diagram

```text
  X_m ──^{u_{nm}}──→ X_n
   ↓ f_m              ↓ f_n
  Y_m ──────────────→ Y_n
```

($f_{n}$ being the structure morphism) is commutative and identifies $X_{m}$ with the product $X_{n} \times_{Y_{n}}
Y_{m}$, as one sees immediately `(II, 1.4.6)`. The formal prescheme $\mathfrak{X}$, inductive limit of the inductive
system $(X_{n})$, is then locally Noetherian and such that the structure morphism $f : \mathfrak{X} \to \mathfrak{Y}$,
inductive limit of the system $(f_{n})$, is finite (4.8.1 and `II, 10.12.3.1`); we saw in addition in the proof of
(4.8.6) that $f_{*}(\mathcal{O}_{\mathfrak{X}})$ is the projective limit of the $\mathcal{A}_{n}$, hence equal to
$\mathcal{A}$ `(I, 10.10.6)`. As for the uniqueness assertion, it is a consequence of the following more general result:

**Proposition (4.8.8).**

<!-- label: III.4.8.8 -->

*Let $\mathfrak{Y}$ be a locally Noetherian formal prescheme, $\mathfrak{X}$, $\mathfrak{X}'$ two $\mathfrak{Y}$-formal
preschemes finite over $\mathfrak{Y}$, $f : \mathfrak{X} \to \mathfrak{Y}$, $f' : \mathfrak{X}' \to \mathfrak{Y}$ the
structure morphisms. There exists a canonical bijection of $\operatorname{Hom}_{\mathfrak{Y}}(\mathfrak{X},
\mathfrak{X}')$ onto $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{Y}}}(f'_{*}(\mathcal{O}_{\mathfrak{X}'}),
f_{*}(\mathcal{O}_{\mathfrak{X}}))$ (1).*

> (1) The last expression denotes the set of homomorphisms of $\mathcal{O}_{\mathfrak{Y}}$-algebras
> $f'_{*}(\mathcal{O}_{\mathfrak{X}'}) \to f_{*}(\mathcal{O}_{\mathfrak{X}})$.

**Proof.** The definition of this map $h \mapsto \mathcal{A}(h)$ is the same as in `(II, 1.1.2)`, and to see that it is
bijective, we are immediately reduced to the case where $\mathfrak{Y} = Spf(B)$ is a Noetherian affine formal scheme.
But then $\mathfrak{X} = Spf(A)$, $\mathfrak{X}' = Spf(A')$, where $A$ and $A'$ are two finite $B$-algebras and
$f_{*}(\mathcal{O}_{\mathfrak{X}}) = A^{\Delta}$, $f'_{*}(\mathcal{O}_{\mathfrak{X}'}) = A'^{\Delta}$. The conclusion
then results from the one-to-one correspondence, on the one hand between the $\mathfrak{Y}$-morphisms $\mathfrak{X} \to
\mathfrak{X}'$ and the $B$-homomorphisms (necessarily continuous) $A' \to A$ which are homomorphisms of algebras
`(I, 10.2.2)`, and on the other hand between the homomorphisms of $B$-modules $A' \to A$ and the homomorphisms of
$\mathcal{O}_{\mathfrak{Y}}$-modules $A'^{\Delta} \to A^{\Delta}$ `(I, 10.10.2.3)`.

**Corollary (4.8.9).**

<!-- label: III.4.8.9 -->

*In the canonical one-to-one correspondence defined in (4.8.8), the closed immersions $\mathfrak{X} \to \mathfrak{X}'$
correspond to the surjective homomorphisms of $\mathcal{O}_{\mathfrak{Y}}$-algebras $f'_{*}(\mathcal{O}_{\mathfrak{X}'})
\to f_{*}(\mathcal{O}_{\mathfrak{X}})$.*

**Proof.** The question being still local on $\mathfrak{Y}$, we are reduced to the definition of closed immersions of
locally Noetherian formal preschemes `(I, 10.14.2)`.

**Corollary (4.8.10).**

<!-- label: III.4.8.10 -->

*The notations and hypotheses being those of (4.8.1), for an adic morphism $f$ to be a closed immersion, it is necessary
and sufficient that $f_{0}$ be a closed immersion (of usual preschemes).*

**Proof.** This results immediately from (4.8.9) and from the condition of surjectivity for a homomorphism of coherent
$\mathcal{O}_{\mathfrak{Y}}$-modules `(I, 10.11.5)`.

**Proposition (4.8.11).**

<!-- label: III.4.8.11 -->

*For a morphism $f : \mathfrak{X} \to \mathfrak{Y}$ of locally Noetherian formal preschemes*

<!-- original page 149 -->

*to be finite, it is necessary and sufficient that it be proper and have its fibres $f^{-1}(y)$ finite (for every $y \in
\mathfrak{Y}$).*

**Proof.** Thanks to the definitions (3.4.1 and 4.8.2), we are at once reduced to the same proposition for $f_{0}$
(notation of (4.8.1)), which is none other than (4.4.2).
