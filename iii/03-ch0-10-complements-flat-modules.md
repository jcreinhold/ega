# §10. Complements on flat modules

<!-- original page 361 -->

For the proofs of the properties stated without proof in nos. `(10.1)` and `(10.2)`, we refer the reader to Bourbaki,
_Alg. comm._, chap. II and III.

## 10.1. Relations between flat modules and free modules

**10.1.1.**

<!-- label: 0_III.10.1.1 -->

Let $A$ be a ring, $\mathfrak{J}$ an ideal of $A$, $M$ an $A$-module; for every integer $p \geq 0$, one has a canonical
homomorphism of $(A/\mathfrak{J})$-modules

```text
  φ_p : (M/𝔍 M) ⊗_{A/𝔍} (𝔍^p/𝔍^{p+1}) → 𝔍^p M/𝔍^{p+1} M               (10.1.1.1)
```

which is obviously surjective. We shall denote by $gr(A) = \oplus_{p\geq 0} \mathfrak{J}^{p}/\mathfrak{J}^{p+1}$ the
graded ring associated to $A$ filtered by the $\mathfrak{J}^{p}$, and by $gr(M) = \oplus_{p\geq 0} \mathfrak{J}^{p}
M/\mathfrak{J}^{p+1} M$ the graded $gr(A)$-module associated to $M$ filtered by the $\mathfrak{J}^{p} M$; we therefore
have $gr_{p}(A) = \mathfrak{J}^{p}/\mathfrak{J}^{p+1}$, $gr_{p}(M) = \mathfrak{J}^{p} M/\mathfrak{J}^{p+1} M$; the
$\phi_{p}$ define a surjective homomorphism of graded $gr(A)$-modules

```text
  φ : gr_0(M) ⊗_{gr_0(A)} gr(A) → gr(M).                                 (10.1.1.2)
```

<!-- original page 362 -->

**10.1.2.**

<!-- label: 0_III.10.1.2 -->

*Suppose that one of the following hypotheses holds:*

*(i) $\mathfrak{J}$ is nilpotent;*

*(ii) $A$ is Noetherian, $\mathfrak{J}$ is contained in the radical of $A$, and $M$ is of finite type.*

*Then the following properties are equivalent:*

*a) $M$ is a free $A$-module.*

*b) $M/\mathfrak{J} M = M \otimes_{A} (A/\mathfrak{J})$ is a free $(A/\mathfrak{J})$-module, and $Tor^{A}_{1}(M,
A/\mathfrak{J}) = 0$.*

*c) $M/\mathfrak{J} M$ is a free $(A/\mathfrak{J})$-module and the canonical homomorphism `(10.1.1.2)` is injective
(hence bijective).*

**10.1.3.**

<!-- label: 0_III.10.1.3 -->

*Suppose that $A/\mathfrak{J}$ is a field (in other words, that $\mathfrak{J}$ is maximal), and that one of the
hypotheses (i), (ii) of `(10.1.2)` holds. Then the following properties are equivalent:*

*a) $M$ is a free $A$-module.*

*b) $M$ is a projective $A$-module.*

*c) $M$ is a flat $A$-module.*

*d) $Tor^{A}_{1}(M, A/\mathfrak{J}) = 0$.*

*e) The canonical homomorphism `(10.1.1.2)` is bijective.*

This result will apply in particular in the following two cases:

(i) $M$ is an arbitrary module over a local ring $A$ whose maximal ideal $\mathfrak{J}$ is nilpotent (for example an
Artinian local ring).

(ii) $M$ is a module of finite type over a Noetherian local ring.

## 10.2. Local criteria of flatness

**10.2.1.**

<!-- label: 0_III.10.2.1 -->

*The hypotheses and notation being those of `(10.1.1)`, consider the following conditions:*

*a) $M$ is a flat $A$-module.*

*b) $M/\mathfrak{J} M$ is a flat $(A/\mathfrak{J})$-module and $Tor^{A}_{1}(M, A/\mathfrak{J}) = 0$.*

*c) $M/\mathfrak{J} M$ is a flat $(A/\mathfrak{J})$-module and the canonical homomorphism `(10.1.1.2)` is bijective.*

*d) For every $n \geq 1$, $M/\mathfrak{J}^{n} M$ is a flat $(A/\mathfrak{J}^{n})$-module.*

*One then has the implications*

```text
  a) ⟹ b) ⟹ c) ⟹ d)
```

*and if $\mathfrak{J}$ is nilpotent, the four conditions a), b), c), d) are equivalent. The same holds if $A$ is
Noetherian and if moreover $M$ is **ideally separated**, that is, if for every ideal $\mathfrak{a}$ of $A$, the
$A$-module $\mathfrak{a} \otimes_{A} M$ is separated for the $\mathfrak{J}$-preadic topology.*

**10.2.2.**

<!-- label: 0_III.10.2.2 -->

*Let $A$ be a Noetherian ring, $B$ a commutative Noetherian $A$-algebra, $\mathfrak{J}$ an ideal of $A$ such that
$\mathfrak{J} B$ is contained in the radical of $B$, $M$ a $B$-module of finite type. Then, when $M$ is considered as an
$A$-module, the conditions a), b), c), d) of `(10.2.1)` are equivalent.*

<!-- original page 363 -->

This result applies above all when $A$ and $B$ are Noetherian local rings, the homomorphism $A \to B$ a local
homomorphism. More particularly, if $\mathfrak{J}$ is then the maximal ideal of $A$, one may, in conditions b) and c),
drop the hypothesis that $M/\mathfrak{J} M$ is flat, which is automatically satisfied, and condition d) means that the
modules $M/\mathfrak{J}^{n} M$ are free over the $A/\mathfrak{J}^{n}$.

**10.2.3.**

<!-- label: 0_III.10.2.3 -->

*The hypotheses on $A$, $B$, $\mathfrak{J}$, $M$ being those formulated at the beginning of `(10.2.2)`, let `Â` be the
Hausdorff completion of $A$ for the $\mathfrak{J}$-preadic topology, $\hat{M}$ the Hausdorff completion of $M$ for the
$\mathfrak{J} B$-preadic topology. Then, for $M$ to be a flat $A$-module, it is necessary and sufficient that $\hat{M}$
be a flat `Â`-module.*

**10.2.4.**

<!-- label: 0_III.10.2.4 -->

*Let $\rho : A \to B$ be a local homomorphism of Noetherian local rings, $k$ the residue field of $A$, $M$, $N$ two
$B$-modules of finite type, $N$ being assumed to be $A$-flat. Let $u : M \to N$ be a $B$-homomorphism. Then the
following conditions are equivalent:*

*a) $u$ is injective and $Coker(u)$ is a flat $A$-module.*

*b) $u \otimes 1 : M \otimes_{A} k \to N \otimes_{A} k$ is injective.*

**10.2.5.**

<!-- label: 0_III.10.2.5 -->

*Let $\rho : A \to B$, $\sigma : B \to C$ be local homomorphisms of Noetherian local rings, $k$ the residue field of
$A$, $M$ a $C$-module of finite type. Suppose that $B$ is a flat $A$-module. Then the following conditions are
equivalent:*

*a) $M$ is a flat $B$-module.*

*b) $M$ is a flat $A$-module, and $M \otimes_{A} k$ is a flat $(B \otimes_{A} k)$-module.*

**Proposition (10.2.6).**

<!-- label: 0_III.10.2.6 -->

*Let $A$, $B$ be two Noetherian local rings, $\rho : A \to B$ a local homomorphism, $\mathfrak{J}$ an ideal of $B$
contained in the maximal ideal, $M$ a $B$-module of finite type. Suppose that for every $n \geq 0$, $M_{n} =
M/\mathfrak{J}^{n+1} M$ is a flat $A$-module. Then $M$ is a flat $A$-module.*

**Proof.** We must prove that for every injective homomorphism $u : N' \to N$ of $A$-modules of finite type,
$v = 1 \otimes u : M \otimes_{A} N' \to M \otimes_{A} N$ is injective. Now, $M \otimes_{A} N'$ and $M \otimes_{A} N$ are
$B$-modules of finite type, hence separated for the $\mathfrak{J}$-preadic topology $(0_{I}, 7.3.5)$; it therefore
suffices to prove that the homomorphism $\hat{v} : (M \otimes_{A} N')^{\wedge} \to (M \otimes_{A} N)^{\wedge}$ between
Hausdorff completions is injective. Now, one has $\hat{v} = \lim v_{n}$, where $v_{n}$ is the homomorphism
$1 \otimes u : M_{n} \otimes_{A} N' \to M_{n} \otimes_{A} N$; since by hypothesis $M_{n}$ is $A$-flat, $v_{n}$ is
injective for every $n$, and so the same holds for $\hat{v}$, the functor `lim` being left exact.

**Corollary (10.2.7).**

<!-- label: 0_III.10.2.7 -->

*Let $A$ be a Noetherian ring, $B$ a Noetherian local ring, $\rho : A \to B$ a homomorphism, $f$ an element of the
maximal ideal of $B$, $M$ a $B$-module of finite type. Suppose that the homothety $f_{M} : x \mapsto fx$ of $M$ is
injective and that $M/fM$ is a flat $A$-module. Then $M$ is a flat $A$-module.*

**Proof.** Set $M_{i} = f^{i} M$ for $i \geq 0$; since $f_{M}$ is injective, $M_{i}/M_{i+1}$ is isomorphic to $M/fM$,
hence $A$-flat for every $i \geq 0$; from the exact sequence

$$ 0 \to M_{i}/M_{i+1} \to M/M_{i+1} \to M/M_{i} \to 0 $$

one deduces by induction on $i$ that $M/M_{i}$ is $A$-flat for every $i \geq 0$ $(0_{I}, 6.1.2)$; one can therefore
apply `(10.2.6)`. One may also argue directly as follows: for every $A$-module $N$ of finite type, $M \otimes_{A} N$ is
a $B$-module of finite type; since $f$ belongs to the radical $\mathfrak{n}$ of $B$, the `(f)`-adic topology on $M
\otimes_{A} N$ is finer than the $\mathfrak{n}$-adic topology, and the latter is known to be separated $(0_{I}, 7.3.5)$.

<!-- original page 364 -->

Moreover, since $M/M_{i}$ is $A$-flat, one has $f^{i}(M \otimes_{A} N) = Im(M_{i} \otimes_{A} N \to M \otimes_{A} N) =
Ker(M \otimes_{A} N \to (M/M_{i}) \otimes_{A} N)$ $(0_{I}, 6.1.2)$. Let then $N$ be an $A$-module of finite type, $N'$ a
submodule of $N$, $j : N' \to N$ the canonical injection; in the commutative diagram

```text
  M ⊗_A N'    →    (M/M_i) ⊗_A N'
     │                  │
     │ 1_M ⊗ j           │ 1_{M/M_i} ⊗ j
     ↓                  ↓
  M ⊗_A N     →    (M/M_i) ⊗_A N
```

$1_{M/M_{i}} \otimes j$ is injective since $M/M_{i}$ is $A$-flat; one concludes that

```text
  Ker(M ⊗_A N' → M ⊗_A N) ⊂ Ker(M ⊗_A N' → (M/M_i) ⊗_A N')
```

whatever the value of $i$; since the intersection of the right-hand sides is reduced to `0` as seen above, the same
holds for the left-hand side, and consequently $M$ is $A$-flat.

**Proposition (10.2.8).**

<!-- label: 0_III.10.2.8 -->

*Let $A$ be a reduced Noetherian ring, $M$ an $A$-module of finite type. Suppose that for every $A$-algebra $B$ which is
a discrete valuation ring, $M \otimes_{A} B$ is a flat $B$-module (hence free `(10.1.3)`). Then $M$ is a flat
$A$-module.*

**Proof.** It is known that for $M$ to be flat, it is necessary and sufficient that for every maximal ideal
$\mathfrak{m}$ of $A$, $M_{\mathfrak{m}}$ be a flat $A_{\mathfrak{m}}$-module $(0_{I}, 6.3.3)$; one may therefore
restrict to the case where $A$ is local $(0_{I}, 1.2.8)$. Let then $\mathfrak{m}$ be the maximal ideal of $A$,
$\mathfrak{p}_{i}$ $(1 \leq i \leq r)$ its minimal prime ideals, $k = A/\mathfrak{m}$ the residue field. It is known
`(II, 7.1.7)` that for each $i$ there exists a discrete valuation ring $B_{i}$ having the same field of fractions
$K_{i}$ as the integral ring $A/\mathfrak{p}_{i}$, and dominating the latter. Set $M_{i} = M \otimes_{A} B_{i}$. By
hypothesis, $M_{i}$ is free over $B_{i}$, so one has, denoting by $k_{i}$ the residue field of $B_{i}$,

```text
  rg_{k_i}(M_i ⊗_{B_i} k_i) = rg_{K_i}(M_i ⊗_{B_i} K_i).                 (10.2.8.1)
```

But it is clear that the composite homomorphism $A \to A/\mathfrak{p}_{i} \to B_{i}$ is local, so $k_{i}$ is an
extension of $k$, and one has $M_{i} \otimes_{B_{i}} k_{i} = M \otimes_{A} k_{i} = (M \otimes_{A} k) \otimes_{k} k_{i}$,
and on the other hand $M_{i} \otimes_{B_{i}} K_{i} = M \otimes_{A} K_{i}$. The equality `(10.2.8.1)` therefore yields

```text
  rg_k(M ⊗_A k) = rg_{K_i}(M ⊗_A K_i)                  for 1 ≤ i ≤ r
```

and since $A$ is reduced, this condition is known to imply that $M$ is a free $A$-module (Bourbaki, _Alg. comm._, chap.
II, § 3, no. 2, prop. 7).

## 10.3. Existence of flat extensions of local rings

**Proposition (10.3.1).**

<!-- label: 0_III.10.3.1 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{J}$ its maximal ideal, $k = A/\mathfrak{J}$ its residue field. Let $K$
be an extension of the field $k$. There exists a local homomorphism from $A$ into a Noetherian local ring $B$, such that
$B/\mathfrak{J} B$ is $k$-isomorphic to $K$, and such that $B$ is a flat $A$-module.*

**Proof.** We shall prove this proposition in several steps.

**10.3.1.1.**

<!-- label: 0_III.10.3.1.1 -->

Suppose first that $K = k(T)$, where $T$ is an indeterminate. In the polynomial ring $A' = A[T]$, consider the prime
ideal $\mathfrak{J}' = \mathfrak{J} A'$ formed by the

<!-- original page 365 -->

polynomials with coefficients in the ideal $\mathfrak{J}$; it is clear that $A'/\mathfrak{J}'$ is canonically isomorphic
to `k[T]`. Let us show that the ring of fractions $B = A'_{\mathfrak{J}'}$ answers the question; it is evidently a
Noetherian local ring whose maximal ideal is $\mathfrak{L} = \mathfrak{J} B$. Furthermore, $B/\mathfrak{L} =
(A'/\mathfrak{J}')_{\mathfrak{J}'} = (k[T])_{(0)}$ is nothing other than the field of fractions $K$ of `k[T]`. Finally,
$B$ is a flat $A'$-module and $A'$ a free $A$-module, hence $B$ is a flat $A$-module $(0_{I}, 6.2.1)$.

**10.3.1.2.**

<!-- label: 0_III.10.3.1.2 -->

Suppose next that $K = k(t) = k[t]$, where $t$ is algebraic over $k$; let $f \in k[T]$ be the minimal polynomial of $t$;
there exists a unitary polynomial $F \in A[T]$ whose canonical image in `k[T]` is $f$. Set again $A' = A[T]$, and let
$\mathfrak{J}'$ be the ideal $\mathfrak{J} A' + (F)$ in $A'$. We are going to see that the quotient ring $B = A'/(F)$
answers the question this time. First of all, it is clear that $B$ is a free $A$-module, hence flat. The ring
$A'/\mathfrak{J}'$ is isomorphic to $(A'/\mathfrak{J} A')/((\mathfrak{J} A' + (F))/\mathfrak{J} A') = k[T]/(f) = K$; the
image $\mathfrak{L}$ of $\mathfrak{J}'$ in $B$ is therefore maximal and one obviously has $\mathfrak{L} = \mathfrak{J}
B$. Finally, $B$ is a semi-local ring, since it is an $A$-module of finite type (Bourbaki, _Alg. comm._, chap. IV, § 2,
no. 5, cor. 3 of prop. 9), and its maximal ideals are in bijective correspondence with those of $B/\mathfrak{J} B$
(`[13]`, vol. I, p. 259); what precedes therefore proves that $B$ is a local ring.

**Lemma (10.3.1.3).**

<!-- label: 0_III.10.3.1.3 -->

*Let $(A_{\lambda}, f_{\mu \lambda})$ be a filtered inductive system of local rings, such that the $f_{\mu \lambda}$ are
local homomorphisms; let $\mathfrak{m}_{\lambda}$ be the maximal ideal of $A_{\lambda}$, and let $K_{\lambda} =
A_{\lambda}/\mathfrak{m}_{\lambda}$. Then $A' = \lim A_{\lambda}$ is a local ring whose maximal ideal is $\mathfrak{m}'
= \lim \mathfrak{m}_{\lambda}$, and whose residue field is $K = \lim K_{\lambda}$. Furthermore, if $\mathfrak{m}_{\mu} =
\mathfrak{m}_{\lambda} A_{\mu}$ for $\lambda < \mu$, then $\mathfrak{m}' = \mathfrak{m}_{\lambda} A'$ for every
$\lambda$. If, in addition, $A_{\mu}$ is a flat $A_{\lambda}$-module for $\lambda < \mu$, and if all the $A_{\lambda}$
are Noetherian, then $A'$ is Noetherian and is a flat $A_{\lambda}$-module for every $\lambda$.*

**Proof.** Since $f_{\mu \lambda}(\mathfrak{m}_{\lambda}) \subset \mathfrak{m}_{\mu}$ for $\lambda < \mu$ by hypothesis,
the $\mathfrak{m}_{\lambda}$ form an inductive system, and its limit $\mathfrak{m}'$ is obviously an ideal of $A'$.
Furthermore, if $x' \notin \mathfrak{m}'$, there exists $\lambda$ such that $x' = f_{\lambda}(x_{\lambda})$ for some
$x_{\lambda} \in A_{\lambda}$ ($f_{\lambda} : A_{\lambda} \to A'$ denoting the canonical homomorphism); since $x' \notin
\mathfrak{m}'$, we necessarily have $x_{\lambda} \notin \mathfrak{m}_{\lambda}$, so $x_{\lambda}$ admits an inverse
$y_{\lambda}$ in $A_{\lambda}$, and $y' = f_{\lambda}(y_{\lambda})$ is the inverse of $x'$ in $A'$, which proves that
$A'$ is a local ring with maximal ideal $\mathfrak{m}'$; the assertion concerning $K$ follows immediately from the fact
that `lim` is an exact functor. The hypothesis $\mathfrak{m}_{\mu} = \mathfrak{m}_{\lambda} A_{\mu}$ means that the
canonical map $\mathfrak{m}_{\lambda} \otimes_{A_{\lambda}} A_{\mu} \to \mathfrak{m}_{\mu}$ is surjective; the relation
$\mathfrak{m}' = \mathfrak{m}_{\lambda} A'$ thus follows again from the exactness of the functor `lim` and the fact that
it commutes with the tensor product.

Suppose now that for $\lambda < \mu$ one has $\mathfrak{m}_{\mu} = \mathfrak{m}_{\lambda} A_{\mu}$ and that $A_{\mu}$ is
a flat $A_{\lambda}$-module. Then $A'$ is a flat $A_{\lambda}$-module for every $\lambda$, by virtue of $(0_{I},
6.2.3)$; since $A'$ and $A_{\lambda}$ are local rings and $\mathfrak{m}' = \mathfrak{m}_{\lambda} A'$, $A'$ is even a
faithfully flat $A_{\lambda}$-module $(0_{I}, 6.6.2)$. Suppose finally, in addition, that the $A_{\lambda}$ are
Noetherian; the $\mathfrak{m}_{\lambda}$-preadic topologies are then separated $(0_{I}, 7.3.5)$; let us show that it
follows first that on $A'$ the $\mathfrak{m}'$-adic topology is separated. Indeed, if $x' \in A'$ belongs to every
$\mathfrak{m}'^{n}$ $(n > 0)$, it is the image of some $x_{\mu} \in A_{\mu}$ for a certain index $\mu$, and since the
inverse image in $A_{\mu}$ of $\mathfrak{m}'^{n} = \mathfrak{m}^{n}_{\mu} A'$ is $\mathfrak{m}^{n}_{\mu}$ $(0_{I},
6.6.1)$, $x_{\mu}$ belongs to every $\mathfrak{m}^{n}_{\mu}$, hence $x_{\mu} = 0$ by hypothesis, and consequently $x' =
0$. Denote by `Â'` the completion of $A'$ for the $\mathfrak{m}'$-adic topology; what precedes shows that $A' \subset
\hat{A}'$. We shall show that `Â'` is Noetherian and $A_{\lambda}$-flat for every $\lambda$; it will

<!-- original page 366 -->

follow that `Â'` is $A'$-flat $(0_{I}, 6.2.3)$, and since $\mathfrak{m}' \hat{A}' \neq \hat{A}'$, `Â'` is a faithfully
flat $A'$-module $(0_{I}, 6.6.2)$, whence one will finally conclude that $A'$ is Noetherian $(0_{I}, 6.5.2)$, which will
complete the proof of the lemma.

One has $\hat{A}' = \lim_{n} A'/\mathfrak{m}'^{n}$; on account of the fact that $A'$ is $A_{\lambda}$-flat, one has

```text
  𝔪'^n/𝔪'^{n+1} = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{A_λ} A'
                = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{K_λ} (K_λ ⊗_{A_λ} A')
                = (𝔪_λ^n/𝔪_λ^{n+1}) ⊗_{K_λ} K;
```

since $\mathfrak{m}^{n}_{\lambda}/\mathfrak{m}^{n+1}_{\lambda}$ is a $K_{\lambda}$-vector space of finite dimension,
$\mathfrak{m}'^{n}/\mathfrak{m}'^{n+1}$ is a $K$-vector space of finite dimension for every $n \geq 0$. It therefore
follows from $(0_{I}, 7.2.12)$ and $(0_{I}, 7.2.8)$ that `Â'` is Noetherian. We further know that the maximal ideal of
`Â'` is $\mathfrak{m}' \hat{A}'$ and that $\hat{A}'/\mathfrak{m}'^{n} \hat{A}'$ is isomorphic to $A'/\mathfrak{m}'^{n}$;
since $A'/\mathfrak{m}'^{n} = (A_{\lambda}/\mathfrak{m}^{n}_{\lambda}) \otimes_{A_{\lambda}} A'$, $A'/\mathfrak{m}'^{n}$
is a flat $(A_{\lambda}/\mathfrak{m}^{n}_{\lambda})$-module $(0_{I}, 6.2.1)$; criterion `(10.2.2)` is therefore
applicable to the Noetherian $A_{\lambda}$-algebra `Â'`, and shows that `Â'` is $A_{\lambda}$-flat.

**10.3.1.4.**

<!-- label: 0_III.10.3.1.4 -->

We now take up the general case. There exist an ordinal $\gamma$ and, for every ordinal $\lambda \leq \gamma$, a
subfield $k_{\lambda}$ of $K$ containing $k$, such that: 1° For every $\lambda < \gamma$, $k_{\lambda+1}$ is an
extension of $k_{\lambda}$ generated by a single element; 2° For every ordinal $\mu$ without predecessor, $k_{\mu} =
\bigcup_{\lambda<\mu} k_{\lambda}$; 3° $K = k_{\gamma}$. Indeed, it suffices to consider a bijection $\xi \mapsto
t_{\xi}$ of the set of ordinals $\xi \leq \beta$ (for a suitable $\beta$) onto $K$, to define $k_{\lambda}$ by
transfinite induction (for $\lambda \leq \beta$) as the union of the $k_{\mu}$ for $\mu < \lambda$ if $\lambda$ has no
predecessor, and, if $\lambda = \nu + 1$, as $k_{\nu}(t_{\xi})$, where $\xi$ is the smallest ordinal such that $t_{\xi}
\notin k_{\nu}$; $\gamma$ is then by definition the smallest ordinal $\leq \beta$ such that $k_{\gamma} = K$.

This being so, we shall define, by transfinite recursion, a family of Noetherian local rings $A_{\lambda}$ for $\lambda
\leq \gamma$, and local homomorphisms $f_{\mu \lambda} : A_{\lambda} \to A_{\mu}$ for $\lambda \leq \mu$, satisfying the
following conditions:

(i) $(A_{\lambda}, f_{\mu \lambda})$ is an inductive system and $A_{0} = A$.

(ii) For every $\lambda$, one has a $k$-isomorphism $A_{\lambda}/\mathfrak{J} A_{\lambda} \xrightarrow{\sim}
k_{\lambda}$.

(iii) For $\lambda \leq \mu$, $A_{\mu}$ is a flat $A_{\lambda}$-module.

Suppose then that the $A_{\lambda}$ and the $f_{\mu \lambda}$ are defined for $\lambda < \mu < \xi$, and suppose first
that $\xi = \zeta + 1$, so that $k_{\xi} = k_{\zeta}(t)$. If $t$ is transcendental over $k_{\zeta}$, one defines
$A_{\xi}$ following the procedure of `(10.3.1.1)` as equal to $(A_{\zeta}[T])_{\mathfrak{J} A_{\zeta}[T]}$; $f_{\xi
\zeta}$ is the canonical map, and for $\lambda < \zeta$ one takes $f_{\xi \lambda} = f_{\xi \zeta} \circ f_{\zeta
\lambda}$; the verification of conditions (i) to (iii) is then immediate, in view of what was proved in `(10.3.1.1)`.
Suppose next that $t$ is algebraic, and let $h$ be its minimal polynomial in $k_{\zeta}[T]$, $H$ a unitary polynomial of
$A_{\zeta}[T]$ whose image in $k_{\zeta}[T]$ is $h$; one then takes $A_{\xi}$ equal to $A_{\zeta}[T]/(H)$, the $f_{\xi
\lambda}$ being defined as before; the verification of conditions (i) to (iii) then follows from what was seen in
`(10.3.1.2)`.

Suppose now that $\xi$ has no predecessor; one then takes for $A_{\xi}$ the inductive limit of the inductive system of
local rings $(A_{\lambda}, f_{\mu \lambda})$ for $\lambda < \xi$; $f_{\xi \lambda}$ is defined as the canonical map for
$\lambda < \xi$. The fact that $A_{\xi}$ is local Noetherian, that the $f_{\xi \lambda}$ are local homomorphisms, and
conditions (i) to (iii) for $\lambda \leq \xi$

<!-- original page 367 -->

then follow from the inductive hypothesis and from Lemma `(10.3.1.3)`. This construction being done, it is clear that
the ring $B = A_{\gamma}$ satisfies the statement of `(10.3.1)`.

One should note that by virtue of `(10.2.1, c))`, one has a canonical isomorphism

```text
  gr(A) ⊗_k K ⥲ gr(B).                                                  (10.3.1.5)
```

On the other hand, one may replace $B$ by its $\mathfrak{J} B$-adic completion $\hat{B}$ without changing the
conclusions of `(10.3.1)`, since $\hat{B}$ is a flat $B$-module $(0_{I}, 7.3.3)$, hence a flat $A$-module $(0_{I},
6.2.1)$.

We have moreover proved the

**Corollary (10.3.2).**

<!-- label: 0_III.10.3.2 -->

*If $K$ is an extension of finite degree, one may suppose that $B$ is a finite $A$-algebra.*
