<!-- original page 249 -->

## §21. Differentials in characteristic-$p$ rings

The results of the present section, of a more special and technical nature than those of §§19, 20 and 22, will be used
only exceptionally in the course of Chap. IV. Their principal role here is in the proof of three theorems of §22
(22.3.3, 22.5.8 and 22.7.3), the first and the last of which intervene in an essential way in the "fine" theory of
Noetherian local rings of Chap. IV, §7.

### 21.1. Systems of $p$-generators and $p$-bases

(21.1.1) Given a number $p$ which is either `0` or a prime number, we shall say that a ring $A$ is *of characteristic
$p$* if there exists a ring homomorphism $P \to A$, where $P$ is the prime field of characteristic $p$; note that this
homomorphism is then unique, the composite $\mathbb{Z} \to P \to A$ being the unique homomorphism of $\mathbb{Z}$ into
$A$. If $A \neq 0$, this amounts to saying that $A$ contains a field of characteristic $p$, the image of $P$ being
necessarily a field isomorphic to $P$ (and moreover the only subfield of $A$ isomorphic to $P$).

(21.1.2) If $p > 0$, saying that $A$ is of characteristic $p$ is equivalent to saying that, in $A$, one has $p\cdot 1 =
0$, or again $pA = 0$. If $p = 0$, saying that $A$ is of characteristic $p$ is equivalent to saying that for every
integer $n \neq 0$, $n\cdot 1$ is invertible in $A$. If $A \neq 0$, there can exist only one $p$ (prime or `0`) such
that $A$ is of characteristic $p$; this follows from the preceding and from Bezout's identity $ap + bq = 1$ for two
distinct primes `p, q`. By contrast the zero ring is of characteristic $p$ for every $p$.

(21.1.3) If $A$ is of characteristic $p$, so is every algebra over $A$. In particular, for every prime ideal
$\mathfrak{p}$ of $A$, the residue field of $A$ at $\mathfrak{p}$ is of characteristic $p$. Conversely, if $p = 0$ and
if for every maximal ideal $\mathfrak{m}$ of $A$ the residue field of $A$ at $\mathfrak{m}$ is of characteristic `0`,
the same holds for $A$, for every integer $n \neq 0$ is then invertible in all the $A_{\mathfrak{m}}$, hence also in
$A$. By contrast, if $p > 0$, a local ring may have its residue field of characteristic $p$ without itself being of
characteristic $p$, as is shown by the example of the prime ring (integral) $\mathbb{Z}_{(p)}$ `(19.8.3)` or of the
Artinian local ring $\mathbb{Z}/p^{2} \mathbb{Z}$ for $p \geq 2$, which do not contain a field.

Let us finally note that for a ring (even reduced), the residue fields at its prime ideals may have different
characteristics, as is shown by the example of $\mathbb{Z}$.

(21.1.4) In all the rest of this section, we suppose fixed a prime number $p$ and all rings will be supposed of
characteristic $p$, unless expressly mentioned otherwise. For such a ring $A$, the map $x \mapsto x^{p}$ is an
endomorphism of $A$, which we denote `F_A`; if $A$ is reduced, `F_A` is injective. One sets $A^{p} = F_{A}(A)$ (subring
of $A$ consisting of the $x^{p}$ for $x \in A$); one can naturally consider $A$ as an $A^{p}$-algebra.

One can also consider $A$ as an $A$-algebra by means of the homomorphism $F_{A} : x \mapsto x^{p}$ of $A$ into $A$; in
other words, this is the $A$-algebra $A_{F_{A}}$ for which the product $\lambda \cdot x$ of $x \in A$ by a scalar
$\lambda \in A$ is the product $\lambda^{p} x$ in the ring $A$; we shall denote this $A$-algebra $A^{[p]}$. It is clear
that for every ring homomorphism $u : A \to B$ the pair $(u, u)$ is a di-homomorphism of $A$-algebras $A^{[p]} \to
B^{[p]}$. For every $A$-module $E$, one sets $E^{[p]} = E \otimes_{A} A^{[p]}$ where $A^{[p]}$ is considered as an $(A,
A)$-bimodule, the left $A$-module structure being the one just defined, and the right $A$-module structure defined by
multiplication in $A$; $E^{[p]}$ is equipped with the $A$-module structure coming from the right $A$-module structure of
$A^{[p]}$, so that for $x \in E$, $\alpha, \beta$ in $A$, one has

```text
  α(x ⊗ β) = x ⊗ (αβ)    and    (αx) ⊗ β = α(x ⊗ β) = x ⊗ α^p β.
```

<!-- original page 250 -->

Setting $x^{[p]} = x \otimes 1$, one therefore has $(\alpha x)^{[p]} = \alpha^{p} x^{[p]}$. When `F_A` is injective, one
can identify $A^{[p]}$ with the ring $A$ considered as algebra over its subring $A^{p}$.

**Proposition (21.1.5).**

<!-- label: 0_IV.21.1.5 -->

*Let $A$, $B$ be two rings, $u : A \to B$ a homomorphism.*

*(i) Every $A$-derivation of $B$ into a $B$-module $L$ is zero on $A[B^{p}]$ (and is therefore an
$A[B^{p}]$-derivation).*

*(ii) For every sub-$A$-algebra $A'$ of $A[B^{p}]$, if $j : A' \to B$ is the canonical injection, the canonical
homomorphism*

$$ \gamma_{B/A'/A} : \Omega_{B/A} \to \Omega_{B/A'} $$

*is bijective.*

*(iii) Suppose there exists an integer $s \geq 0$ such that $u(A) \supset B^{p^{s}}$. Then, in the ring $B \otimes_{A}
B$, $\mathfrak{J}_{B/A}$ is a nilideal.*

(i) By induction starting from `(20.1.1.1)`, one deduces for every $A$-derivation $D : B \to L$ that one has $D(x^{k}) =
k x^{k-1} D(x)$, whence in particular $D(x^{p}) = 0$.

(ii) By `(20.4.8)`, assertion (ii) is only a translation of (i), the latter being written $\operatorname{Der}_{A}(B, L)
= \operatorname{Der}_{A[B^{p}]}(B, L)$ for every $B$-module $L$.

(iii) For every $x \in B$, one has $(x \otimes 1 - 1 \otimes x)^{p^{s}} = x^{p^{s}} \otimes 1 - 1 \otimes x^{p^{s}} =
x^{p^{s}}(1 \otimes 1 - 1 \otimes 1) = 0$, since $x^{p^{s}} \in u(A)$. The conclusion follows from the fact that the
elements $1 \otimes x - x \otimes 1$ generate $\mathfrak{J}_{B/A}$ `(20.4.4)`.

It follows at once from `(21.1.5)` that for every pair of ring homomorphisms $A \to B \to C$,

$$ \gamma_{C/B/A} = \gamma_{C/B/A} (21.1.5.1) $$

for every sub-$A$-algebra $A' \subset A[B^{p}]$ of $B$.

On the other hand, `(21.1.5)` also shows in particular that for "absolute" modules of differentials,

$$ \Omega_{A} = \Omega_{A/A^{p}}. (21.1.5.2) $$

**Corollary (21.1.6).**

<!-- label: 0_IV.21.1.6 -->

*Suppose that $B$ is an $A$-algebra of finite type and that there exists an integer $s \geq 0$ such that $u(A) \supset
B^{p^{s}}$. If $\Omega_{B/A} = 0$, then $u$ is surjective.*

By `(21.1.5, (iii))`, $\mathfrak{J}_{B/A}$ is a nilideal; moreover, by `(20.4.4)` and the hypothesis,
$\mathfrak{J}_{B/A}$ is an ideal of finite type, so it is nilpotent; as the relation $\Omega_{B/A} = 0$ means that
$\mathfrak{J}^{2}_{B/A} = \mathfrak{J}_{B/A}$, one concludes that $\mathfrak{J}_{B/A} = 0$, that is, that $\pi : B
\otimes_{A} B \to B$ is bijective. Moreover, every element of $B$ having its $p^{s}$-th power in $u(A)$, $B$ is integral
over $A$, and being of finite type, it is a finite $A$-algebra. One is thus reduced to proving the following lemma (in
which the rings considered are not supposed of characteristic $p$):

**Lemma (21.1.6.1).**

<!-- label: 0_IV.21.1.6.1 -->

*Let $R$ be a ring, $S$ a finite $R$-algebra; if the canonical homomorphism $\pi : S \otimes_{R} S \to S$ is bijective,
then the structural homomorphism $u : R \to S$ is surjective.*

It suffices to show that for every maximal ideal $\mathfrak{m}$ of $R$, if one sets $T = R - \mathfrak{m}$, the
homomorphism $u_{\mathfrak{m}} : R_{\mathfrak{m}} \to T^{-1} S$ is surjective (Bourbaki, Alg. comm., chap. II, §3, n° 3,
th. 1); now the hypothesis entails that the homomorphism $(T^{-1} S) \otimes_{R_{\mathfrak{m}}} (T^{-1} S) \to T^{-1} S$
is bijective $(0_{I}, 1.3.4)$, and since $T^{-1} S$ is a finite $R_{\mathfrak{m}}$-algebra,

<!-- original page 251 -->

one sees that one can restrict to the case where $R$ is a local ring. Denoting still by $\mathfrak{m}$ its maximal
ideal, it suffices to prove that $u \otimes 1 : R/\mathfrak{m} \to S/\mathfrak{m} S$ is surjective, by Nakayama's lemma
($S$ being an $R$-module of finite type); as the canonical homomorphism $(S/\mathfrak{m} S) \otimes_{R/\mathfrak{m}}
(S/\mathfrak{m} S) \to S/\mathfrak{m} S$ is bijective and $S/\mathfrak{m} S$ is a finite $(R/\mathfrak{m})$-algebra, one
is finally reduced to the case where $R$ is a field; but then the ranks of $S \otimes_{R} S$ and of $S$ over $R$ can
only be equal if $S$ is of rank `0` or `1`, that is, if $u : R \to S$ is surjective.

**Proposition (21.1.7).**

<!-- label: 0_IV.21.1.7 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $(x_{\alpha})_{\alpha \in I}$ a family of elements of $B$. Consider the
following properties:*

*a) $B = A[B^{p}, (x_{\alpha})]$, in other words the $A[B^{p}]$-algebra $B$ is generated by the family
$(x_{\alpha})_{\alpha \in I}$.*

*b) The $A[B^{p}]$-module $B$ is generated by the monomials $\prod x^{n(\alpha)}_{\alpha}$, where $(n(\alpha))_{\alpha
\in I}$ is a family of integers of finite support such that $0 \leq n(\alpha) < p$ for every $\alpha \in I$.*

*c) The $B$-module $\Omega_{B/A}$ is generated by the $d_{B/A}(x_{\alpha})$ $(\alpha \in I)$.*

*Then properties a) and b) are equivalent and entail c); if moreover $B$ is an $A[B^{p}]$-algebra of finite type, c) is
equivalent to a) and b).*

It is clear that b) entails a), and conversely a) entails b), for every monomial $\prod_{\alpha}
x^{m(\alpha)}_{\alpha}$, where the $m(\alpha)$ are integers $\geq 0$ (forming a family of finite support), can be
written $(\prod_{\alpha} x^{q(\alpha)}_{\alpha})^{p} \cdot \prod_{\alpha} x^{r(\alpha)}_{\alpha}$, by dividing each
$m(\alpha)$ by $p$, which gives $m(\alpha) = p \cdot q(\alpha) + r(\alpha)$ with $0 \leq r(\alpha) < p$. The fact that
a) entails c) follows from `(21.1.5, (ii))` and from `(20.4.7)`. Conversely suppose c) verified and that $B$ is an
$A[B^{p}]$-algebra of finite type; let $B'$ be the sub-$A[B^{p}]$-algebra of $B$ generated by the $x_{\alpha}$; in the
exact sequence `(20.5.7.1)`

```text
  Ω_{B'/A[B^p]} ⊗_{B'} B → Ω_{B/A[B^p]} → Ω_{B/B'} → 0
```

the hypothesis entails that the left arrow is surjective (taking account of `(21.1.5, (ii))`); one therefore has
$\Omega_{B/B'} = 0$, and as $B^{p} \subset B' \subset B$ and $B$ is a $B'$-algebra of finite type, one necessarily has
$B' = B$ by `(21.1.6)`.

**Remark (21.1.8).**

<!-- label: 0_IV.21.1.8 -->

*When $B$ is a field, we shall prove the equivalence of properties a), b) and c) without hypothesis of finiteness
`(21.4.5)`.*

**Definition (21.1.9).**

<!-- label: 0_IV.21.1.9 -->

*Let $A$ be a ring (of characteristic $p$), $B$ an $A$-algebra. One says that a family $(x_{\alpha})_{\alpha \in I}$ of
elements of $B$ is **$p$-free over $A$** (resp. a **system of $p$-generators of $B$ over $A$**, resp. a **$p$-basis of
$B$ over $A$**) if the family of monomials $\prod_{\alpha} x^{n(\alpha)}_{\alpha}$ ($0 \leq n(\alpha) < p$,
$(n(\alpha))_{\alpha \in I}$ of finite support) is a free family (resp. a system of generators, resp. a basis) in the
$A[B^{p}]$-module $B$.*

One has corresponding definitions for a set $M$ of elements of $B$, by considering the family defined by the canonical
injection $M \to B$. When one takes for $A$ the prime field $\mathbb{F}_{p}$ (in which case $A[B^{p}] = B^{p}$), one
omits the mention of $A$ in the preceding definition (or one says further that a family is "absolutely" $p$-free, resp.
an "absolute" system of $p$-generators, resp. an "absolute" $p$-basis).

<!-- original page 252 -->

It is clear that the notions defined in `(21.1.9)` do not change when one replaces $A$ therein by the subring $A[B^{p}]$
of $B$; in other words one can always suppose that one has $B^{p} \subset A \subset B$.

If $M$ is a $p$-free part of $B$ over $A$, it is clear that every subset of $M$ is $p$-free over $A$. Moreover:

**Lemma (21.1.10).**

<!-- label: 0_IV.21.1.10 -->

*Let $C$ be a sub-$A$-algebra of $B$ such that $B^{p} \subset C$, $M$ a subset of $C$, $N$ a subset of $B$.*

*(i) If $M$ is a system of $p$-generators of $C$ over $A$ and $N$ a system of $p$-generators of $B$ over $C$, then $M
\cup N$ is a system of $p$-generators of $B$ over $A$.*

*(ii) Suppose that $M$ is a $p$-basis of $C$ over $A$; then, for $N$ to be $p$-free over $C$, it is necessary and
sufficient that $M \cup N$ be $p$-free over $A$.*

One can restrict to the case where $B^{p} \subset A \subset C \subset B$. Then (i) is a particular case of the fact that
if $P$ (resp. $Q$) is a system of generators of the $A$-module $C$ (resp. of the $C$-module $B$), the set of `xy`, where
$x \in P$ and $y \in Q$, is a system of generators of the $A$-module $B$. Keeping the same notation, if $P$ is a basis
of the $A$-module $C$, saying that $Q$ is a free family over $C$ means that the relation $\sum_{\lambda, \mu} a_{\lambda
\mu} x_{\lambda} y_{\mu} = 0$, where $a_{\lambda \mu} \in A$, $x_{\lambda} \in P$, $y_{\mu} \in Q$ (the $x_{\lambda}$
(resp. $y_{\mu}$) being pairwise distinct), is equivalent to $\sum_{\lambda} a_{\lambda \mu} x_{\lambda} = 0$ for every
$\mu$, or again to $a_{\lambda \mu} = 0$ for every pair $(\lambda, \mu)$; whence assertion (ii).

### 21.2. $p$-bases and formal smoothness

**Theorem (21.2.1).**

<!-- label: 0_IV.21.2.1 -->

*Let $B$ be a ring, $A$ a subring of $B$ such that $B^{p} \subset A \subset B$, $(x_{\alpha})_{\alpha \in I}$ a
$p$-basis of $B$ over $A$. Let $E$ be an $A$-algebra, $u : A \to E$ the structural homomorphism, $q : E \to B$ a
surjective $A$-homomorphism, $\mathfrak{K}$ its kernel, and suppose that $\mathfrak{K}^{2} = 0$. Then:*

*(i) For there to exist an $A$-homomorphism $v : B \to E$ right inverse to the homomorphism $q : E \to B$, it is
necessary and sufficient that one have $u(q(z)^{p}) = z^{p}$ for every $z \in E$.*

*(ii) When the condition of (i) is satisfied, for every family $(z_{\alpha})_{\alpha \in I}$ of elements of $E$ such
that $q(z_{\alpha}) = x_{\alpha}$ for every $\alpha \in I$, there exists one and only one $A$-homomorphism $v : B \to E$
such that $v(x_{\alpha}) = z_{\alpha}$ for every $\alpha \in I$, and $v$ is right inverse to $q$.*

If there exists an $A$-homomorphism $v : B \to E$, one must have $v(a) = u(a)$ for every $a \in A \subset B$, hence
$v(q(z)^{p}) = u(q(z)^{p})$ for every $z \in E$, since $B^{p} \subset A$. But one has $v(q(z)^{p}) = (v(q(z)))^{p}$ and
by definition $v(q(z)) \equiv z (mod \mathfrak{K})$ if $q \circ v = 1_{B}$, hence $(v(q(z)))^{p} = z^{p}$ since
$\mathfrak{K}^{2} = 0$; whence the necessity of (i). The sufficiency of condition (i) will follow from (ii). Now, under
the hypotheses of (ii), the uniqueness of $v$ is evident since the monomials $\prod_{\alpha} x^{n(\alpha)}_{\alpha}$

<!-- original page 253 -->

generate the $A$-module $B$; as these monomials moreover form a basis of the $A$-module $B$, there exists an $A$-linear
map $v$ of $B$ into $E$ such that $v(\prod_{\alpha} x^{n(\alpha)}_{\alpha}) = \prod_{\alpha} z^{n(\alpha)}_{\alpha}$ for
every family $(n(\alpha))_{\alpha \in I}$ of finite support with $0 \leq n(\alpha) < p$ for every $\alpha$. It remains
to see that $v$ is a ring homomorphism. Now, one can write $(\prod_{\alpha} x^{m(\alpha)}_{\alpha})(\prod_{\alpha}
x^{n(\alpha)}_{\alpha}) = a \cdot \prod_{\alpha} x^{r(\alpha)}_{\alpha}$, where $r(\alpha) = m(\alpha) + n(\alpha)$ if
$m(\alpha) + n(\alpha) < p$, $r(\alpha) = m(\alpha) + n(\alpha) - p$ in the contrary case, and $a \in A$ is the product
of the $x^{p}_{\alpha}$ for those $\alpha \in I$ such that $m(\alpha) + n(\alpha) \geq p$; we have to see that $u(a) =
\prod_{\alpha} z^{p}_{\alpha}$ (the product over the same set of $\alpha$); but as $x^{p}_{\alpha} = q(z_{\alpha})^{p}$,
this follows from the hypothesis. Q.E.D.

**Corollary (21.2.2).**

<!-- label: 0_IV.21.2.2 -->

*Let $B$ be a ring, $A$ a subring of $B$ such that $B^{p} \subset A \subset B$. If there exists a $p$-basis of $B$ over
$A$, $B$ is an $A$-algebra formally smooth relative to $B^{p}$ (for the discrete topologies).*

In fact, let $E$ be an $A$-extension of $B$ by a $B$-module $L$, $q : E \to B$ the augmentation, $u : A \to E$ the
structural homomorphism. Saying that $E$ is $B^{p}$-trivial means that there exists a ring homomorphism $v : B \to E$
such that $q(v(b)) = b$ and $v(b^{p}) = u(b^{p})$ for every $b \in B$. One deduces from this that, for $z \in E$, one
has $u(q(z)^{p}) = v(q(z)^{p}) = (v(q(z)))^{p}$; but by virtue of the relation $L^{2} = 0$, one has $\mathfrak{K}^{2} =
0$, and as $v(q(z)) - z \in L$, one has $(v(q(z)))^{p} = z^{p}$; the condition of `(21.2.1, (i))` is therefore
satisfied, and $E$ is $B$-trivial.

**Corollary (21.2.3).**

<!-- label: 0_IV.21.2.3 -->

*Let $B$ be a ring, $A$ a subring of $B$ such that $B^{p} \subset A \subset B$, and $(x_{\alpha})_{\alpha \in I}$ a
$p$-basis of $B$ over $A$. Let $L$ be a $B$-module. Then:*

*(i) For a derivation $D$ of $A$ into $L$ to extend to a derivation of $B$ into $L$, it is necessary and sufficient that
$D$ vanish on $B^{p}$.*

*(ii) If $D$ vanishes on $B^{p}$, then, for every family $(y_{\alpha})_{\alpha \in I}$ of elements of $L$, there exists
one and only one derivation $D'$ of $B$ into $L$ extending $D$ and such that $D'(x_{\alpha}) = y_{\alpha}$ for every
$\alpha \in I$.*

Given a derivation $D$ of $A$ into $L$, consider the ring $E = D_{B}(L)$ and the homomorphism $u : A \to E$ defined by
$u(a) = (a, D(a))$; an $A$-homomorphism $v : B \to E$ right inverse to the canonical homomorphism $q : E \to B$ is then
of the form $x \mapsto (x, D'(x))$, where $D'$ is a derivation of $B$ into $L$ extending $D$ `(20.1.5)`; as $u(q(z)^{p})
= (q(z)^{p}, p q(z)^{p-1} D'(q(z)))$ for $z \in E$, the corollary follows immediately from `(21.2.1)` applied to $E$.

It follows from `(21.2.3)` that the sequence

```text
  0 → Der_A(B, L) → Der_{B^p}(B, L) → Der_{B^p}(A, L) → 0                            (21.2.3.1)
```

(cf. `(20.2.2.1)`) is exact, and that the map

$$ D' \mapsto (D'(x_{\alpha}))_{\alpha \in I} (21.2.3.2) $$

is an isomorphism of the $B$-module $\operatorname{Der}_{A}(B, L)$ onto the $B$-module product $L^{I}$ (by taking $D =
0$ in `(21.2.3)`).

**Corollary (21.2.4).**

<!-- label: 0_IV.21.2.4 -->

*Under the hypotheses of `(21.2.3)`, the sequence*

```text
  0 → Ω_{A/B^p} ⊗_A B → Ω_{B/B^p} → Ω_{B/A} → 0                                      (21.2.4.1)
```

*is exact and split, and the family $(d_{B/A}(x_{\alpha}))_{\alpha \in I}$ is a basis of the $B$-module $\Omega_{B/A}$.*

This follows at once from `(21.2.3)` and from the formula $\operatorname{Der}_{A}(B, L) =
\operatorname{Hom}_{B}(\Omega_{B/A}, L)$ `(20.4.8)`.

**Corollary (21.2.5).**

<!-- label: 0_IV.21.2.5 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $(x_{\alpha})_{\alpha \in I}$ a $p$-basis of $B$ over $A$. Then
$(d_{B/A}(x_{\alpha}))_{\alpha \in I}$ is a basis of the $B$-module $\Omega_{B/A}$.*

Using `(21.1.5, (ii))`, one reduces to the case where $A = A[B^{p}]$, and it then suffices to apply `(21.2.4)`.

<!-- original page 254 -->

(21.2.6) Let $A$, $B$ be two rings, $u : A \to B$ a ring homomorphism; one has (with the notation of `(21.1.4)`) a
commutative diagram

```text
  A^{[p]} —u^{[p]}→ B^{[p]}
    │                │
    F_A              F_B                                                             (21.2.6.1)
    │                │
    ↓                ↓
    A   ———u———→    B.
```

One therefore deduces canonically a homomorphism of $B$-algebras

```text
  u ⊗ 1 : A^{[p]} ⊗_A B → B^{[p]}                                                    (21.2.6.2)
```

whose image is the ring $A[B^{p}]$ (which is a $B$-algebra by the homomorphism $F_{B} : B \to B^{[p]}$).

**Theorem (21.2.7).**

<!-- label: 0_IV.21.2.7 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $u : A \to B$ the structural homomorphism. Suppose verified the following
conditions:*

*(i) The homomorphism `(21.2.6.2)` deduced from $u$ is injective.*

*(ii) $B$ admits a $p$-basis $(x_{\alpha})_{\alpha \in I}$ relative to $A$.*

*Then $B$ is an $A$-algebra formally smooth (for the discrete topologies). More precisely, equip $A$ and $B$ with the
discrete topologies; let $E$ be an admissible topological $A$-algebra $(0_{I}, 7.1.2)$, $\mathfrak{K}$ an ideal of
definition of $E$, $C = E/\mathfrak{K}$, $v : B \to C$ an $A$-homomorphism, $q : E \to C$ the augmentation. Then, for
every family $(z_{\alpha})_{\alpha \in I}$ of elements of $E$ such that $v(x_{\alpha}) = q(z_{\alpha})$ for every
$\alpha \in I$, there exists one and only one $A$-homomorphism $w : B \to E$ such that $v = q \circ w$ and
$w(x_{\alpha}) = z_{\alpha}$ for every $\alpha \in I$.*

Consider first the case where $E$ is discrete, hence $\mathfrak{K}$ nilpotent. One can restrict to the case where $v$ is
surjective; moreover, the reasoning of `(19.4.3)` permits supposing $\mathfrak{K}^{2} = 0$ and consequently
$\mathfrak{K}^{2} = 0$. Finally, by considering the inverse image by $v$ of the extension $E$ of $C$ by $\mathfrak{K}$,
one can restrict to the case where $C = B$ and $v$ is the identity `(19.4.4)`. Since the ring homomorphism $F_{E} : E
\to E$ vanishes on $\mathfrak{K}$, it factors as $E \to B \to E$, and $F'$, considered as homomorphism of $B$ into
$E^{[p]}$, is an $A$-homomorphism by definition of the $A$-algebra structure of $E^{[p]}$ by means of the composite
homomorphism $A \to E \to E^{[p]}$, where $r : A \to E$ is the structural homomorphism of the $A$-algebra $E$; moreover
$r : A^{[p]} \to E^{[p]}$ is also an $A$-homomorphism. There is therefore a unique $A$-homomorphism $f : A^{[p]}
\otimes_{A} B \to E^{[p]}$ such that the composites of $f$ with the canonical homomorphisms $A^{[p]} \to A^{[p]}
\otimes_{A} B$ and $B \to A^{[p]} \otimes_{A} B$ are respectively $r$ and $F'$. Now, by hypothesis, one can identify
$A^{[p]} \otimes_{A} B$ with $A[B^{p}]$, the canonical homomorphisms $A^{[p]} \to A^{[p]} \otimes_{A} B$ and $B \to
A^{[p]} \otimes_{A} B$ identifying respectively with $u$ and `F_B`. One can therefore now consider $E$ as an
$A[B^{p}]$-algebra by means of the homomorphism $f$, and, by construction, one has $f(q(z)^{p}) = z^{p}$ for every $z
\in E$; one is thus in the conditions of application of `(21.2.1)`, whence the theorem in this case.

To pass to the general case, consider a fundamental system $(\mathfrak{J}_{\lambda})$ of open ideals of $E$, and set
$E_{\lambda} = E/\mathfrak{J}_{\lambda}$, $\mathfrak{K}_{\lambda} = (\mathfrak{K} +
\mathfrak{J}_{\lambda})/\mathfrak{J}_{\lambda}$, $C_{\lambda} = E_{\lambda}/\mathfrak{K}_{\lambda} = E/(\mathfrak{K} +
\mathfrak{J}_{\lambda})$; as $E$ is admissible, one has $E = \lim E_{\lambda}$ $(0_{I}, 7.2.2)$. For every pair
$(\alpha, \lambda)$, denote by $z_{\alpha, \lambda}$ the canonical image of $z_{\alpha}$ in $E_{\lambda}$, by
$p_{\lambda} : C \to C_{\lambda}$ the canonical homomorphism,

<!-- original page 255 -->

by $q_{\lambda}$ the canonical homomorphism $E_{\lambda} \to C_{\lambda}$. As by hypothesis $\mathfrak{K}_{\lambda}$ is
nilpotent in $E_{\lambda}$, the first part of the proof proves the existence and uniqueness of an $A$-homomorphism
$w_{\lambda} : B \to E_{\lambda}$ such that $p_{\lambda} \circ v = q_{\lambda} \circ w_{\lambda}$ and
$w_{\lambda}(x_{\alpha}) = z_{\alpha, \lambda}$ for every $\alpha$. The uniqueness of the $w_{\lambda}$ then shows
immediately that $(w_{\lambda})$ is a projective system of homomorphisms, and $w = \lim w_{\lambda}$ answers the
question.

**Remark (21.2.8).**

<!-- label: 0_IV.21.2.8 -->

*The verification of the existence and uniqueness of the homomorphism $w : B \to E$ such that $w(x_{\alpha}) =
z_{\alpha}$ for every $\alpha$ can be deduced directly from the fact that $B$ is an $A$-algebra formally smooth and from
the fact that the $d_{B/A}(x_{\alpha})$ form a basis of the $B$-module $\Omega_{B/A}$ `(21.2.4)`, without bringing in
the fact that one deals with a $p$-basis (so that the result is valid without supposing the rings of characteristic
$p$).*

In fact, one can restrict to the case where $\mathfrak{K}^{2} = 0$; as $\operatorname{Der}_{A}(B, \mathfrak{K}) =
\operatorname{Hom}_{B}(\Omega_{B/A}, \mathfrak{K})$ by `(20.4.8)`, there exists one and only one $A$-derivation $D$ of
$B$ into $\mathfrak{K}$ such that $D(x_{\alpha}) = t_{\alpha}$ for every family $(t_{\alpha})$ of elements of
$\mathfrak{K}$; the conclusion follows from `(20.1.1)`.

### 21.3. $p$-bases and imperfection modules

(21.3.1) Let $A$, $B$ be two rings (of characteristic $p$), $i : A \to B$, $j : B \to A$ two ring homomorphisms such
that one has

```text
  j(i(a)) = a^p              for every a ∈ A,                                        (21.3.1.1)
  i(j(b)) = b^p              for every b ∈ B.                                        (21.3.1.2)
```

Most often, $i$ will be injective, so that $A$ will be identified by $i : A \to B$ to a subring of $B$; once this
identification is made, the existence of $j$ implies that $B^{p} \subset A$, and $j$ is then identified with `F_B`.

(21.3.2) If $h : A^{p} \to A$ is the canonical injection, one has, by `(21.3.1.1)`, a commutative diagram

```text
  B ——j——→ A
  │         │
  i         h                                                                        (21.3.2.1)
  │         │
  ↓         ↓
  A ——F_A→ A^p
```

so that the pair $(j, F_{A})$ may be considered as a di-homomorphism of the $A$-algebra $B$ (for $i$) into the
$A^{p}$-algebra $A$ (for $h$). One deduces a canonical homomorphism of $A$-modules

```text
  π_{B/A} : Ω_{B/A} ⊗_{B, j} A → Ω_A = Ω^1_A                                         (21.3.2.2)
```

(cf. `(20.5.4)`; the identification of $\Omega^{1}_{A/A^{p}}$ and of the module of absolute differentials
$\Omega^{1}_{A}$ comes from `(21.1.5, (ii))`).

One sets

```text
  Θ_{B/A} = Ω_{B/A} ⊗_{B, j} A                                                       (21.3.2.3)
  Ξ_{B/A} = Ker(π_{B/A})                                                             (21.3.2.4)
```

<!-- original page 256 -->

so that one has the exact sequence

$$ 0 \to \Xi_{B/A} \to \Theta_{B/A} \to \Omega^{1}_{A} (21.3.2.5) $$

(one notes that this notation may lead to confusion since $\Theta_{B/A}$ and $\pi_{B/A}$ depend not only on $A$ and $B$,
but also on $i$ and $j$).

(21.3.3) Since by `(21.3.1.2)`, one has $F_{B} = i \circ j$, one can write for every $B$-module $M$ (cf. `(21.1.4)`)

```text
  M^{[p]} = M ⊗_B B = (M ⊗_B A) ⊗_A B                                                (21.3.3.1)
```

whence in particular

```text
  (Ω_{B/A})^{[p]} = Θ_{B/A} ⊗_A B                                                    (21.3.3.2)
```

and one deduces from `(21.3.2.2)` a canonical homomorphism of $B$-modules

```text
  ω_{B/A} : (Ω_{B/A})^{[p]} → Ω^1_A ⊗_A B.                                           (21.3.3.3)
```

Taking account of `(20.5.4.2)`, the image of this homomorphism is the $B$-module generated by the elements $d_{A}(j(b))
\otimes 1$ for $b \in B$. Their image by the canonical homomorphism $i_{B/A} : \Omega^{1}_{A} \otimes_{A} B \to
\Omega^{1}_{B}$ deduced from $i$ `(20.5.2)` is therefore in the sub-$B$-module of $\Omega^{1}_{B}$ generated by the
$d_{B}(i(j(b)))$ for $b \in B$; by virtue of `(21.3.1.2)`, this image is zero. In other words, one has a sequence of
homomorphisms

```text
  0 → Ξ_{B/A} ⊗_A B → (Ω_{B/A})^{[p]} → Υ_{B/A}                                      (21.3.3.4)
```

which is not necessarily exact, but in which the composite of two consecutive homomorphisms is zero.

**Proposition (21.3.4).**

<!-- label: 0_IV.21.3.4 -->

*If $B$ is an $A$-module flat (for $i$), the sequence `(21.3.3.4)` is exact.*

This follows from the definition of flatness.

Proposition `(21.3.4)` applies in particular when one has $B^{p} \subset A \subset B$, $i$ and $j$ being respectively
the canonical injection and `F_B`, and $B$ admits a $p$-basis over $A$ (so that $B$ is then a free $A$-module). But even
in this case the kernel $\Xi_{B/A}$ is not necessarily zero. Nevertheless:

**Proposition (21.3.5).**

<!-- label: 0_IV.21.3.5 -->

*Let $B$ be a reduced ring, $A$ a subring of $B$ such that $B^{p} \subset A \subset B$. Suppose there exists a $p$-basis
$(x_{\lambda})_{\lambda \in L}$ of $B$ over $A$ and a $p$-basis $(y_{\mu})_{\mu \in M}$ of $A$ over $A^{p}$; then the
canonical homomorphism `(21.3.3.4)`*

$$ (\Omega_{B/A})^{[p]} \to \Upsilon_{B/A} (21.3.5.1) $$

*is bijective, and the elements $d_{B}(x_{\lambda}) \otimes 1$ form a basis of the $B$-module $\Upsilon_{B/A}$.*

Since $B$ is reduced, $x \mapsto x^{p}$ is an isomorphism of $B$ onto $B^{p}$, and by transport of structure by means of
this isomorphism, one sees that $(x^{p}_{\lambda})_{\lambda \in L}$ is a $p$-basis of $B^{p}$ over $A^{p}$; one
concludes that the $x^{p}_{\lambda}$ and the $y_{\mu}$ form a $p$-basis of $A$ over $A^{p}$ `(21.1.10)`; consequently
`(21.1.5, (ii) and 21.2.5)` the $d_{A}(x^{p}_{\lambda})$ and the $d_{A}(y_{\mu})$ form a basis of the $A$-module
$\Omega^{1}_{A}$; hence the $d_{A}(x^{p}_{\lambda}) \otimes 1$ and $d_{A}(y_{\mu}) \otimes 1$ form a basis of the
$B$-module $\Omega^{1}_{A} \otimes_{A} B$. Now, the image of $d_{A}(x^{p}_{\lambda}) \otimes 1$ by $i_{B/A}$ is
$d_{B}(x^{p}_{\lambda}) = 0$; on the other hand, the image of $d_{A}(y_{\mu}) \otimes 1$ by $i_{B/A}$

<!-- original page 257 -->

is $d_{B}(y_{\mu})$, and as the $y_{\mu}$ and the $x_{\lambda}$ form a $p$-basis of $B$ over $B^{p}$ `(21.1.10)`, the
$d_{B}(y_{\mu})$ are linearly independent (over $B$) in $\Omega^{1}_{B}$ `(21.2.5)`; one deduces at once that the kernel
of $i_{B/A}$ has a basis formed of the $d_{A}(x^{p}_{\lambda}) \otimes 1$; as these are the images by `(21.3.5.1)` of
the elements $d_{B}(x_{\lambda}) \otimes 1$ in $\Omega_{B/A} \otimes_{B} B^{[p]}$, and as the latter form a basis of the
$B$-module $\Omega_{B/A} \otimes_{B} B^{[p]}$ `(21.2.5)`, the homomorphism `(21.3.5.1)` of $B$-modules is bijective.

**Remarks (21.3.6).**

<!-- label: 0_IV.21.3.6 -->

*(i) Let $A'$, $B'$ be two rings of characteristic $p$, and suppose one has two homomorphisms $i' : A' \to B'$, $j' : B'
\to A'$ verifying `(21.3.1.1)` and `(21.3.1.2)`, and ring homomorphisms $f : A \to A'$, $g : B \to B'$ making the
diagram*

```text
  A'  ——i'——→ B'  ——j'——→ A'
  ↑           ↑           ↑
  f           g           f
  │           │           │
  A   ——i——→  B   ——j——→  A
```

*commute. Then the canonical homomorphism $\Omega_{B/A} \to \Omega_{B'/A'}$ `(20.5.4.3)` gives a canonical
di-homomorphism $\Theta_{B/A} \to \Theta_{B'/A'}$ making the diagram*

$$ \pi_{B/A} 0 \to \Xi_{B/A} \to \Theta_{B/A} \to \Omega^{1}_{A} \downarrow \downarrow \downarrow 0 \to \Xi_{B'/A'} \to
\Theta_{B'/A'} \to \Omega^{1}_{A'} \pi_{B'/A'} $$

*commute.*

*(ii) Let $A'$ be any $A$-algebra, and set $B' = B \otimes_{A} A'$; then $i' = i \otimes 1 : A' \to B'$ and $j' = j
\otimes 1 : B' \to A'$ verify `(21.3.1.1)` and `(21.3.1.2)`, and one has*

```text
  Ω_{B'/A'} = Ω_{B/A} ⊗_A A' = Ω_{B/A} ⊗_B B'
```

*`(20.5.5)`; one deduces a canonical $A'$-isomorphism*

```text
  Θ_{B/A} ⊗_A A' ⥲ Θ_{B'/A'}                                                         (21.3.6.1)
```

*and also a canonical $B'$-homomorphism*

```text
  Υ_{B/A} ⊗_A A' → Υ_{B'/A'}.                                                        (21.3.6.2)
```

### 21.4. Case of field extensions

(21.4.0) Let $K$ be a field of characteristic $p > 0$, $k$ a subfield of $K$; then the ring $k[K^{p}]$ is equal to the
field $k(K^{p})$ since $k$ is algebraic over $K^{p}$. One can therefore apply the results of the preceding numbers by
replacing throughout $A$, $B$ and $A[B^{p}]$ by $k$, $K$ and $k(K^{p})$.

**Lemma (21.4.1).**

<!-- label: 0_IV.21.4.1 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$. For an element $x \in K$ to be $p$-free over
$k$, it is necessary and sufficient that $x \notin k(K^{p})$.*

<!-- original page 258 -->

In fact, $x$ is a root of the polynomial $X^{p} - x^{p}$ of $k(K^{p})[X]$, and one knows (Bourbaki, Alg., chap. V, §8,
n° 1, prop. 1) that if $x \notin k(K^{p})$, this polynomial is irreducible, so that the elements $1, x, \cdots, x^{p-1}$
form a basis of the $k(K^{p})$-module $k(K^{p})(x)$.

**Theorem (21.4.2).**

<!-- label: 0_IV.21.4.2 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$, $S$ a system of $p$-generators of $K$ over $k$,
$L \subset S$ a part $p$-free over $k$. Then there exists a $p$-basis $B$ of $K$ over $k$ such that $L \subset B \subset
S$. In particular, every extension of $k$ admits a $p$-basis over $k$.*

One can restrict to the case where $K^{p} \subset k$. By Zorn's theorem, there exists in $K$ a subset $B$ such that $L
\subset B \subset S$, $p$-free over $k$ and maximal among the subsets of $S$ having these properties. It suffices to see
that the subfield $K'$ of $K$ generated by $k$ and $B$ is equal to $K$. In the contrary case, there would exist $x \in
S$ not in $K'$; as $K^{p} \subset k$, one has $K' \supset k(K^{p})$; hence $x$ would be $p$-free over $K'$ `(21.4.1)`,
and consequently $B \cup {x}$ would be $p$-free over $k$ `(21.1.10)`, contrary to the definition of $B$. The last
assertion of `(21.4.2)` is obtained by taking $L = \emptyset$, $S = K$. Q.E.D.

**Corollary (21.4.3).**

<!-- label: 0_IV.21.4.3 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$. For a family $(x_{\alpha})$ of elements of $K$
to be $p$-free over $k$, it is necessary and sufficient that, for every $\alpha$, $x_{\alpha}$ not belong to the field
$K_{\alpha}$ generated by $k(K^{p})$ and by the $x_{\beta}$ of index $\beta \neq \alpha$.*

The condition is necessary by `(21.1.10)`. Conversely, suppose it satisfied; one can restrict to the case where
$(x_{\alpha})$ is a system of $p$-generators of $K$. There then exists a sub-family of $(x_{\alpha})$ which is a
$p$-basis of $K$ `(21.4.2)`, but this family cannot be distinct from $(x_{\alpha})$, otherwise, by the hypothesis, it
would not be a family of $p$-generators of $K$.

**Corollary (21.4.4).**

<!-- label: 0_IV.21.4.4 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$. For $\Omega^{1}_{K/k} = 0$, it is necessary and
sufficient that $K = k(K^{p})$. In particular, for $\Omega^{1}_{K} = 0$, it is necessary and sufficient that $K$ be a
perfect field.*

In fact, if $(x_{\alpha})$ is a $p$-basis of $K$ over $k$, the $d_{K}(x_{\alpha})$ form a basis of the $K$-vector space
$\Omega^{1}_{K/k}$ `(21.2.5)`.

**Theorem (21.4.5).**

<!-- label: 0_IV.21.4.5 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$, $(x_{\alpha})$ a family of elements of $K$. For
$(x_{\alpha})$ to be $p$-free over $k$ (resp. a family of $p$-generators of $K$ over $k$, resp. a $p$-basis of $K$ over
$k$), it is necessary and sufficient that the family $(d_{K/k}(x_{\alpha}))$ be a free family (resp. a system of
generators, resp. a basis) in the $K$-vector space $\Omega^{1}_{K/k}$.*

Let $K'$ be the subfield (equal to the subring) of $K$ generated by $k(K^{p})$ and the $x_{\alpha}$; taking account of
`(20.4.7)`, one sees that the $d_{K'/k}(x_{\alpha})$ generate $\Omega^{1}_{K'/k} = \Omega^{1}_{K'/k(K^{p})}$. If the
$d_{K/k}(x_{\alpha})$ generate $\Omega^{1}_{K/k} = \Omega^{1}_{K/k(K^{p})}$, the left arrow in the exact sequence
`(20.5.7.1)`

```text
  Ω^1_{K'/k(K^p)} ⊗_{K'} K → Ω^1_{K/k(K^p)} → Ω^1_{K/K'} → 0
```

is surjective, hence $\Omega^{1}_{K/K'} = 0$, which implies $K' = K$ by `(21.4.4)`.

If now $(x_{\alpha})$ is a $p$-free family, it is a sub-family of a $p$-basis of $K$ over $k$ `(21.4.2)`, hence the
$d_{K}(x_{\alpha})$ form part of a basis of the $K$-vector space $\Omega^{1}_{K/k}$ `(21.2.5)`, and are consequently
linearly independent over $K$. Conversely let us prove that if the $d_{K/k}(x_{\alpha})$ are linearly independent over
$K$, the family $(x_{\alpha})$ is $p$-free over $k$.

<!-- original page 259 -->

Taking account of `(21.4.3)`, it suffices to see that, for each $\alpha$, $x_{\alpha}$ does not belong to $K_{\alpha}$.
Now, in the exact sequence

```text
  Ω^1_{K_α/k(K^p)} ⊗_{K_α} K → Ω^1_{K/k(K^p)} → Ω^1_{K/K_α} → 0,
```

the images by the left arrow of the $d_{K/k}(x_{\beta})$ for $\beta \neq \alpha$ are the $d_{K_{\alpha}/k}(x_{\beta})$,
which therefore generate a sub-vector space of $\Omega^{1}_{K_{\alpha}/k(K^{p})}$ not containing $d_{K/k}(x_{\alpha})$,
and as this sub-vector space is the kernel of the right arrow, one sees that $d_{K/K_{\alpha}}(x_{\alpha}) \neq 0$,
hence $x_{\alpha} \notin K_{\alpha}$.

**Corollary (21.4.6).**

<!-- label: 0_IV.21.4.6 -->

*Let $k$ be a field of characteristic $p > 0$, $K$ an extension of $k$, $x$ an element of $K$. The three following
conditions are equivalent:*

*a) $x \notin k(K^{p})$.*

*b) $d_{K/k}(x) \neq 0$.*

*c) The element $x$ is $p$-free over $k$.*

**Proposition (21.4.7).**

<!-- label: 0_IV.21.4.7 -->

*Let $L$ be a field of characteristic $p > 0$, $K$ a subfield of $L$ such that $L^{p} \subset K \subset L$. Then the
sequence of $L$-vector spaces*

```text
  0 → Ω^1_{K/L^p} ⊗_K L → Ω^1_{L/L^p} → Ω^1_{L/K} → 0                                (21.4.7.1)
```

*is exact; in other words, one has $\Upsilon_{L/K/L^{p}} = 0$.*

This is a particular case of `(21.2.4)`, taking account of `(21.4.2)`.

**Proposition (21.4.8).**

<!-- label: 0_IV.21.4.8 -->

*Under the hypotheses of `(21.4.7)`, the canonical homomorphism*

$$ (\Omega_{L/K})^{[p]} \to \Upsilon_{L/K} (21.4.8.1) $$

*is bijective; if $(x_{\alpha})$ is a $p$-basis of $L$ over $K$, the elements $d_{L}(x_{\alpha}) \otimes 1$ form a basis
of the $L$-vector space $\Upsilon_{L/K}$.*

This is a particular case of `(21.3.5)`.

### 21.5. Application: separability criteria

In this number and the two following, we no longer suppose that the rings considered are of characteristic $p > 0$.

(21.5.1) Note first that the criterion `(21.2.7)` permits proving a part of Cohen's theorem on separable extensions
`(19.6.1)`, namely that if $k$ is of characteristic $p > 0$ and if $K$ is a separable extension of $k$, then $K$ is an
$A$-algebra formally smooth. In fact, $K$ admits a $p$-basis over $k$ `(21.4.2)`, and on the other hand, it follows from
MacLane's criterion (Bourbaki, Alg., chap. V, §8, n° 2, prop. 3) that in an algebraic closure of $K$, $k^{1/p}$ and $K$
are linearly disjoint over $k$, and consequently the canonical homomorphism $k^{1/p} \otimes_{k} K \to k^{1/p}(K)$ is
bijective, which is precisely condition (i) of `(21.2.7)`, after transport of structure by the isomorphism $k^{1/p}
\xrightarrow{\sim} k$.

**Proposition (21.5.2) (MacLane).**

<!-- label: 0_IV.21.5.2 -->

*Let $A$, $B$ be two complete discrete valuation rings, $\mathfrak{m}$, $\mathfrak{n}$ their respective maximal ideals,
$K = A/\mathfrak{m}$ and $L = B/\mathfrak{n}$ their residue fields, $u : A \to B$ a homomorphism such that $B
u(\mathfrak{m}) = \mathfrak{n}$, $u_{0} = u \otimes 1 : K \to L$ the corresponding homomorphism for residue fields.
Consider the following conditions:*

*a) $L$ is a separable extension of $K$ (for $u_{0}$).*

*b) For every complete discrete valuation ring $B'$ of maximal ideal $\mathfrak{n}'$ and residue field $L'$,*

<!-- original page 260 -->

*every homomorphism $u' : A \to B'$ such that $B' u'(\mathfrak{m}) = \mathfrak{n}'$, and every $K$-isomorphism $\sigma :
L \to L'$ (relative to $u_{0}$ and $u'_{0} = u' \otimes 1 : K \to L'$), there exists an isomorphism $w : B \to B'$ such
that $u' = w \circ u$ and that $w_{0} = w \otimes 1$ be equal to $\sigma$.*

*b') For every homomorphism $u' : A \to B$ such that $B u'(\mathfrak{m}) = \mathfrak{n}$ and such that $u'_{0} = u'
\otimes 1 : K \to L$ be equal to $u_{0}$, there exists an automorphism $w$ of $B$ such that $u' = w \circ u$ and that
$w_{0} = w \otimes 1 : L \to L$ be the identity.*

*c) Denoting by $u_{1} : A/\mathfrak{m}^{2} \to B/\mathfrak{n}^{2}$ the homomorphism deduced from $u$ by passage to
quotients, then, for every local homomorphism $u'_{1} : A/\mathfrak{m}^{2} \to B/\mathfrak{n}^{2}$ such that
$gr_{0}(u'_{1}) = gr_{0}(u_{1}) (= u_{0})$, there exists an automorphism $w_{1}$ of $B/\mathfrak{n}^{2}$ such that
$gr_{0}(w_{1})$ be the identity and that $u'_{1} = w_{1} \circ u_{1}$.*

*c') For every local homomorphism $u'_{1} : A/\mathfrak{m}^{2} \to B/\mathfrak{n}^{2}$ such that $gr_{0}(u'_{1}) =
gr_{0}(u_{1})$ and $gr_{1}(u'_{1}) = gr_{1}(u_{1})$ (homomorphism of $\mathfrak{m}/\mathfrak{m}^{2}$ into
$\mathfrak{n}/\mathfrak{n}^{2}$), there exists an automorphism $w_{1}$ of $B/\mathfrak{n}^{2}$ such that $gr_{0}(w_{1})$
be the identity and that $u'_{1} = w_{1} \circ u_{1}$.*

*Then one has the implications `c) ⇔ c') ⇔ a) ⇒ b) ⇒ b')`.*

*If moreover $A$ is a Cohen ring, the five preceding conditions are equivalent.*

The implications `b) ⇒ b')` and `c) ⇒ c')` are trivial. Let us show that a) implies b). The homomorphism $u$ makes $B$
an $A$-module without torsion, since it transforms by hypothesis a uniformizer of $A$ into a uniformizer of $B$; it
follows that $B$ is a flat $A$-module $(0_{I}, 6.3.4)$, hence a Cohen $A$-algebra `(19.8.1)`; the fact that a) implies
b) is then a consequence of `(19.8.2, (i))` applied with $C = B'$, $\mathfrak{J} = \mathfrak{n}'$, $B'$ being considered
as $A$-algebra for $u'$ and the homomorphism $B \to B'/\mathfrak{n}'$ being the composite $B \to B/\mathfrak{n} \to
B'/\mathfrak{n}'$, which is an $A$-homomorphism by virtue of the hypothesis $u'_{0} = \sigma \circ u_{0}$. The same
reasoning proves that a) entails c), by taking this time $C = B/\mathfrak{n}^{2}$, $\mathfrak{J} =
\mathfrak{n}/\mathfrak{n}^{2}$, $C$ being considered as $A$-algebra for $u'_{1}$.

Let us prove in the second place that c') implies a). The two homomorphisms $u_{1}$ and $u'_{1}$ are such that $u'_{1} =
u_{1} + D$, where $D$ is a derivation of $A/\mathfrak{m}^{2}$ into $\mathfrak{n}/\mathfrak{n}^{2}$ `(20.1.1)`; moreover,
the hypothesis $gr_{1}(u'_{1}) = gr_{1}(u_{1})$ means that $D$ vanishes on $\mathfrak{m}/\mathfrak{m}^{2}$, and can
consequently be considered as a derivation of $K = A/\mathfrak{m}$ into $\mathfrak{n}/\mathfrak{n}^{2}$, and
$\mathfrak{n}/\mathfrak{n}^{2}$ is identified (by choice of a uniformizer of $B$) with the $K$-module $L$ (for $u_{0}$).
On the other hand, the conditions imposed on $w_{1}$ entail that $gr_{1}(w_{1})$ is also the identity (since
$u_{1}(\mathfrak{m}/\mathfrak{m}^{2})$ generates $\mathfrak{n}/\mathfrak{n}^{2}$); $w_{1}$ is therefore of the form $z
\mapsto z + D'(z)$, where $D'$ is this time a derivation of $B/\mathfrak{n}^{2}$ into the $(B/\mathfrak{n}^{2})$-module
$\mathfrak{n}/\mathfrak{n}^{2}$; as $w_{1}$ is the identity on $\mathfrak{n}/\mathfrak{n}^{2}$, $D'$ can again (by the
preceding identification of $\mathfrak{n}/\mathfrak{n}^{2}$ and of $L$) be considered as a derivation of $L$ into $L$;
finally, the relation $u'_{1} = w_{1} \circ u_{1}$ means that $D'$ extends $D$. Note on the other hand that every
derivation $D$ of $K$ into $L$ corresponds to a homomorphism $u'_{1}$ verifying the conditions of c') `(20.1.1)`;
condition c') means therefore that every derivation of $K$ into $L$ extends to a derivation of $L$ into itself, that is
to say `(20.6.5)` that $L$ is separable over $K$.

Let us prove finally that, when $A$ is a Cohen ring, b') entails c'). Let us prove first that under the hypotheses of
c'), there exists a homomorphism $u' : A \to B$ which verifies the hypotheses of b') and, by passage to quotients,
yields $u'_{1} : A/\mathfrak{m}^{2} \to B/\mathfrak{n}^{2}$. In fact, this follows from `(19.8.6, (i))` applied to the
composite homomorphism $v' : A \to A/\mathfrak{m}^{2} \to B/\mathfrak{n}^{2}$;

<!-- original page 261 -->

this last factors as $A \to B \to B/\mathfrak{n}^{2}$ and the hypotheses on $gr_{0}(u'_{1})$ and $gr_{1}(u'_{1})$ entail
$gr_{0}(u') = gr_{0}(u) = u_{0}$ and $gr_{1}(u') = gr_{1}(u)$, hence the image by $u'$ of a uniformizer of $A$ is a
uniformizer of $B$, and one has consequently $B u'(\mathfrak{m}) = \mathfrak{n}$. It then suffices, in order to obtain
an automorphism $u'_{1}$ answering the question, to take the automorphism deduced by passage to quotients from the
automorphism $w$ of $B$ furnished by the application of b') to the homomorphism $u'$.

**Remarks (21.5.3).**

<!-- label: 0_IV.21.5.3 -->

*(i) The differential properties of fields permit solving the question of uniqueness of the field of representatives in
a complete Noetherian local ring $C$ `(19.8.7, (ii))`. Let in fact $\mathfrak{J}$ be the maximal ideal of $C$, $K =
C/\mathfrak{J}$ the residue field of $C$; one can restrict to the case $\mathfrak{J} \neq 0$. Suppose there exists a
homomorphism $u : K \to C$ which, composed with the augmentation $C \to K$, yields the identity; then, for this
homomorphism to be unique, it is necessary and sufficient that $\Omega^{1}_{K} = 0$. In fact, the condition
$\Omega^{1}_{K} = 0$ entails that $K$ is formally unramified over its prime field `(20.7.4)`; if there existed a second
homomorphism $v \neq u$ answering the question, there would be a greatest integer $n$ such that $\mathfrak{J}^{n}$
contains the set of $u(x) - v(x)$ for $x \in K$; by passage to quotient, $u$ and $v$ would yield two distinct
homomorphisms `u', v'` of $K$ into $C/\mathfrak{J}^{n+1}$, whose composites with $C/\mathfrak{J}^{n+1} \to
C/\mathfrak{J}^{n}$ would be equal, which contradicts the definition `(19.10.2)`. Conversely, suppose $\Omega^{1}_{K}
\neq 0$; there then exists a derivation $D \neq 0$ of $K$ into $\mathfrak{J}/\mathfrak{J}^{2}$ `(20.4.8)`, hence a
homomorphism $v_{1} : K \to C/\mathfrak{J}^{2}$ such that, if $u_{1} : K \to C/\mathfrak{J}^{2}$ is obtained by passage
to quotient from $u$, one has $v_{1} = u_{1} + D$ `(20.1.1)`. If $k$ is the prime field of $K$, $C$ is a $k$-algebra and
$K$ a $k$-algebra formally smooth `(19.6.1)`, and the restrictions of $u_{1}$ and $v_{1}$ to $k$ coincide, hence $v_{1}$
factors as $K \to C \to C/\mathfrak{J}^{2}$ and one has $v \neq u$.*

*Let us recall (`(20.6.20)` and `(21.4.4)`) that the condition $\Omega^{1}_{K} = 0$ means that $K$ is perfect if it is
of characteristic $\neq 0$, and an algebraic extension of $\mathbb{Q}$ if it is of characteristic `0`.*

*(ii) In the same manner, let $W$ be a Cohen ring, $C$ a complete Noetherian local ring, $\mathfrak{J} \neq 0$ an ideal
of $C$ contained in the maximal ideal; for the factorization $W \to C \to C/\mathfrak{J}$ in `(19.8.6, (i))` to be
unique, it is necessary and sufficient that the residue field $K$ of the Cohen ring $W$ satisfy $\Omega^{1}_{K} = 0$. In
fact, if $\Omega^{1}_{K} \neq 0$ and if $\mathfrak{m}$ denotes the maximal ideal of $W$, it suffices to compose a
derivation $D \neq 0$ of $K$ into $\mathfrak{J}/\mathfrak{m} \mathfrak{J}$ with the augmentation $W \to K$ to obtain a
derivation $D' \neq 0$ of $W$ into $\mathfrak{J}/\mathfrak{m} \mathfrak{J}$, and one finishes the reasoning as in (i) by
forming with the aid of $D'$ a homomorphism $v_{1} : W \to C/\mathfrak{m} \mathfrak{J}$ distinct from the homomorphism
$u_{1} : W \to C/\mathfrak{m} \mathfrak{J}$ deduced from $u$ by passage to quotient; one completes the reasoning by
invoking this time `(19.8.6, (i))`. If on the contrary $\Omega^{1}_{K} = 0$, the uniqueness of $v$ follows already from
(i) when $W = K$ is a field of characteristic `0`. In the contrary case, one has $\Omega^{1}_{W} = 0$; in fact, one then
has $\mathfrak{m} = pW$, $p$ being the characteristic of $K$ `(19.8.5)`, and the canonical homomorphism
$\mathfrak{m}/\mathfrak{m}^{2} \to \Omega^{1}_{W}/\mathfrak{m} \Omega^{1}_{W}$ `(20.5.11.2)` is consequently zero. The
exact sequence `(20.5.12.1)` applied to $W$ and to $K = W/\mathfrak{m}$ then entails that $\Omega^{1}_{W} = \mathfrak{m}
\Omega^{1}_{W}$, whence our assertion. But then `(20.7.4)` $W$ is formally unramified (for its adic topology) over
$\mathbb{Z}$, and the uniqueness of $v$ is proved as in (i).*

<!-- original page 262 -->

### 21.6. Admissible fields for an extension

(21.6.1) Given four fields $k_{0} \subset k \subset K \subset L$, it follows from `(20.6.16)` and `(20.6.17)` that one
has an exact sequence

```text
  0 → Υ_{K/k/k_0} ⊗_K L → Υ_{L/k/k_0} → Υ_{L/K/k_0} → Υ_{L/K/k} → 0.                  (21.6.1.1)
```

When one keeps $k_{0}$, $K$ and $L$ fixed and one lets the intermediate field $k$ between $k_{0}$ and $K$ "vary", one
evidently has $\Upsilon_{L/K/k_{0}} = \Upsilon_{L/K/k}$ when $k = k_{0}$. When the canonical homomorphism $s$ of
`(21.6.1.1)` is again bijective, one says that $k$ is a $k_{0}$-**admissible** field for the extension $L$ of $K$. The
interest of the existence, under certain conditions, of such fields $k$, which are nevertheless "sufficiently close" to
$K$ (for example such that $[K : k]$ be finite) is that they permit replacing in certain questions the differential
modules $\Omega^{1}_{K/k_{0}}$ and $\Omega^{1}_{L/k_{0}}$ (which may be "too large", for example when $k_{0}$ is the
prime field) by $\Omega^{1}_{K/k}$ and $\Omega^{1}_{L/k}$, more easily handled.

When $k_{0}$ is the prime field, one will say "admissible field" instead of "$k_{0}$-admissible field".

One sets

```text
  Δ(L/K, k/k_0) = Coker(Υ_{K/k/k_0} ⊗_K L → Υ_{L/k/k_0}) ≅ Ker(Υ_{L/K/k_0} → Υ_{L/K/k})  (21.6.1.2)
```

(vector space over $L$); its rank will be denoted $d(L/K, k/k_{0})$ and called the **$k_{0}$-admissibility defect** of
$k$ for the extension $L$ of $K$ (it is evidently zero if and only if $k$ is $k_{0}$-admissible for this extension).
When $k_{0}$ is the prime field, one writes $\Delta(L/K, k)$ and $d(L/K, k)$ instead of $\Delta(L/K, k/k_{0})$ and
$d(L/K, k/k_{0})$.

**Proposition (21.6.2).**

<!-- label: 0_IV.21.6.2 -->

*Let $k_{0} \subset k \subset K \subset L$ be four fields.*

*(i) The following conditions are equivalent:*

*a) The field $k$ is $k_{0}$-admissible for the extension $L$ of $K$ (in other words, the homomorphism
$\Upsilon_{L/K/k_{0}} \to \Upsilon_{L/K/k}$ is injective, hence bijective).*

*b) The canonical homomorphism $u : \Upsilon_{K/k_{0}} \to \Upsilon_{K/k}$ is zero.*

*c) The canonical homomorphism $v : \Omega^{1}_{K/k} \otimes_{K} L \to \Upsilon_{L/k}$ is surjective (hence bijective).*

*d) One has $d(L/K, k/k_{0}) = 0$ (or $\Delta(L/K, k/k_{0}) = 0$).*

*(ii) The equivalent conditions of (i) are verified when one is in one of the following cases: α) $L$ is separable over
$k$; β) $L$ is separable over $K$; γ) one has $k \subset k_{0}(K^{p})$, denoting by $p$ the characteristic exponent of
$k_{0}$.*

(i) The assertions follow trivially from the exactness of the sequence `(21.6.1.1)`.

(ii) If $L$ is separable over $k$, one has $\Upsilon_{L/k_{0}} = 0$ `(20.6.19)`, hence condition b) of (i) is satisfied;
if $L$ is separable over $K$, one has $\Upsilon_{L/K/k_{0}} = 0$ `(20.6.19)`, hence condition a) of (i) is satisfied;
finally, if one has $k \subset k_{0}(K^{p})$, it follows that $\Omega^{1}_{K/k_{0}} = \Omega^{1}_{K/k}$ by virtue of
`(21.1.5.1)`, and condition a) of (i) is verified.

<!-- original page 263 -->

(21.6.3) Suppose that one has a commutative diagram of field monomorphisms

```text
  k'_0 ——→ k' ——→ K' ——→ L'
   ↑       ↑       ↑      ↑
   │       │       │      │
   k_0 ——→  k ——→  K ——→  L.
```

It follows then from `(20.6.17, (ii))` that one has a canonical homomorphism

```text
  Δ(L/K, k/k_0) → Δ(L'/K', k'/k'_0)                                                  (21.6.3.1)
```

with an evident transitivity property, so that one can say that $\Delta(L/K, k/k_{0})$ is a functor in the quadruple
$(k_{0}, k, K, L)$.

**Proposition (21.6.4).**

<!-- label: 0_IV.21.6.4 -->

*(i) Let $k \subset k' \subset k'' \subset K \subset L$ be five fields. One has an exact sequence of canonical
homomorphisms*

```text
  0 → Δ(L/K, k'/k) → Δ(L/K, k''/k) → Δ(L/K, k''/k') → 0                              (21.6.4.1)
```

*and consequently the equality*

```text
  d(L/K, k''/k) = d(L/K, k''/k') + d(L/K, k'/k).                                     (21.6.4.2)
```

*(ii) Let $k_{0} \subset k \subset K \subset L \subset M$ be five fields. One has an exact sequence of canonical
homomorphisms*

```text
  0 → Δ(L/K, k/k_0) ⊗_L M → Δ(M/K, k/k_0) → Δ(M/L, k/k_0) → 0                        (21.6.4.3)
```

*and consequently the equality*

```text
  d(M/K, k/k_0) = d(M/L, k/k_0) + d(L/K, k/k_0).                                     (21.6.4.4)
```

(i) Consider the commutative diagram

```text
  0 → Υ_{K/k'/k} ⊗_K L → Υ_{K/k''/k} ⊗_K L → Υ_{K/k''/k'} ⊗_K L → 0
            ↓                   ↓                   ↓
  0 →   Υ_{L/k'/k}    →   Υ_{L/k''/k}    →   Υ_{L/k''/k'}    → 0
            ↓                   ↓                   ↓
  0 → Δ(L/K, k'/k)    →  Δ(L/K, k''/k)   →  Δ(L/K, k''/k')   → 0
```

where one may consider the three rows as complexes $T'_{1}, T_{2}, T'_{3}$ respectively;

<!-- original page 264 -->

the exact sequence `(21.6.1.1)` and the definition of $\Delta$ `(21.6.1.2)` show that one has an exact sequence of
complexes $0 \to T'_{1} \to T_{2} \to T'_{3} \to 0$; let us apply to it the long exact sequence of cohomology, and let
us note that, by virtue of the exactness of `(21.6.1.1)`, the cohomology of $T'_{1}$ and that of `T_2` are zero except
in a single and the same degree, for which the cohomology modules are both equal to $\Upsilon_{L/K/k} \otimes_{K} L$; as
$T'_{1}$ and `T_2` have thus the same cohomology, that of $T'_{3}$ is necessarily zero, which proves (i).

(ii) Consider similarly the commutative diagram

```text
  0 → Δ(L/K, k/k_0) ⊗_L M → Δ(M/K, k/k_0)   → Δ(M/L, k/k_0)   → 0
            ↓                   ↓                   ↓
        Υ_{L/K/k_0} ⊗_L M  →  Υ_{M/K/k_0}    →  Υ_{M/L/k_0}
            ↓                   ↓                   ↓
        Υ_{L/K/k} ⊗_L M    →  Υ_{M/K/k}      →  Υ_{M/L/k}
```

where again one considers the three rows as complexes $T''_{1}$, `T_2`, $T''_{3}$; the exact sequence `(21.6.1.1)` and
the definition of $\Delta$ `(21.6.1.2)` give here an exact sequence of complexes $0 \to T''_{1} \to T_{2} \to T''_{3}
\to 0$ to which one again applies the long exact sequence of cohomology; this time, by virtue of the exactness of
`(21.6.1.1)`, the cohomology of `T_2` and that of $T''_{3}$ are zero except in a single and the same degree, for which
the cohomology modules are both equal to $\Upsilon_{M/L/K}$; one concludes here that the cohomology of $T''_{1}$ is
zero, which establishes (ii).

**Corollary (21.6.5).**

<!-- label: 0_IV.21.6.5 -->

*(i) Given five fields $k \subset k' \subset k'' \subset K \subset L$, for `k''` to be $k$-admissible for the extension
$L$ of $K$, it is necessary and sufficient that $k'$ be $k$-admissible and that `k''` be $k'$-admissible for the
extension $L$ of $K$.*

*(ii) Given five fields $k_{0} \subset k \subset K \subset L \subset M$, for $k$ to be $k_{0}$-admissible for the
extension $M$ of $K$, it is necessary and sufficient that it be so for the extension $L$ of $K$ and for the extension
$M$ of $L$.*

This follows at once from the relations `(21.6.4.2)` and `(21.6.4.4)`, the values of $d$ being $\geq 0$.

**Corollary (21.6.6).**

<!-- label: 0_IV.21.6.6 -->

*Let $k_{0} \subset k \subset K \subset L$ be four fields, and suppose that $k$ is $k_{0}$-admissible for the extension
$L$ of $K$. Then, if $k'_{0}, k', K', L'$ are four fields such that $k_{0} \subset k'_{0} \subset k' \subset k \subset K
\subset K' \subset L' \subset L$, $k'$ is $k'_{0}$-admissible for the extension $L'$ of $K'$.*

### 21.7. Cartier's equality

The following result translates in terms of differentials a theorem of MacLane on derivations:

<!-- original page 265 -->

**Theorem (21.7.1) (Cartier).**

<!-- label: 0_IV.21.7.1 -->

*Let $K$ be a field, $L$ an extension of finite type of $K$. Then $\Omega^{1}_{L/K}$ and $\Upsilon_{L/K}$ are $L$-vector
spaces of finite rank, and one has*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K} = deg.tr_K L.                                            (21.7.1.1)
```

If $L'$ is a field such that $K \subset L' \subset L$, one has the exact sequence `(20.6.15.1)` (applied to $A = P$,
prime field of $K$, $A = K$, $B = L'$, $C = L$)

```text
  0 → Υ_{L/K} → Υ_{L/L'} → Υ_{L'/K} ⊗_{L'} L → Ω^1_{L'/K} ⊗_{L'} L → Ω^1_{L/K} → Ω^1_{L/L'} → 0
```

whence $(0_{III}, 11.10.2)$

```text
  rg_L Ω^1_{L/K} − rg_L Υ_{L/K} = (rg_L Ω^1_{L/L'} − rg_L Υ_{L/L'}) + (rg_{L'} Ω^1_{L'/K} − rg_{L'} Υ_{L'/K}).
```

Since on the other hand `deg.tr_K L = deg.tr_K L' + deg.tr_{L'} L`, one sees, by induction on the number of generators
of the extension $L$, that one is reduced to proving `(21.7.1.1)` when $L = K(x)$. Let us distinguish three cases:

a) $x$ is transcendental over $K$; as $L$ is separable over $K$, one has then $\Upsilon_{L/K} = 0$ `(20.6.3)`; on the
other hand, `(20.5.9)` and `(20.4.13)` show that $\Omega^{1}_{L/K}$ is of rank `1`, whence `(21.7.1.1)` in this case.

b) $L$ is an algebraic separable extension of $K$, so that one still has $\Upsilon_{L/K} = 0$ `(20.6.3)`. On the other
hand, one has $\Omega^{1}_{L/K} = 0$ by `(20.6.20)`, whence again `(21.7.1.1)`.

c) $L$ is an algebraic inseparable extension of $K$; the reasoning at the beginning shows that one can restrict to the
case where $L^{p} \subset K$; it then follows from `(21.4.8)` that one has $rg \Omega^{1}_{L/K} = rg \Upsilon_{L/K}$,
whence again `(21.7.1.1)`.

**Corollary (21.7.2).**

<!-- label: 0_IV.21.7.2 -->

*Let $K$ be a field, $L$ an extension of finite type of $K$, $k$ a subfield of $K$. Then $\Omega^{1}_{L/K}$ and
$\Upsilon_{L/K/k}$ are vector spaces of finite rank over $L$, and one has*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K/k} = deg.tr_K L + d(L/K, k).                              (21.7.2.1)
```

*Consequently, one has the inequality*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K/k} ≥ deg.tr_K L.                                          (21.7.2.2)
```

*Moreover, for the two sides of `(21.7.2.2)` to be equal, it is necessary and sufficient that $k$ be an admissible field
for the extension $L$ of $K$.*

In fact, since the homomorphism $\Upsilon_{L/K} \to \Upsilon_{L/K/k}$ is surjective, one has by definition `(21.6.1.2)`
$rg \Upsilon_{L/K} - rg \Upsilon_{L/K/k} = d(L/K, k)$, and the corollary thus follows at once from `(21.7.1)` and from
`(21.6.2)`.

**Corollary (21.7.3).**

<!-- label: 0_IV.21.7.3 -->

*Let $k \subset K \subset L$ be three fields such that $L$ is an extension of finite type of $k$. Then one has*

```text
  rg Ω^1_{L/k} − rg Ω^1_{K/k} ⊗_K L = deg.tr_K L + d(L/K, k).                        (21.7.3.1)
```

<!-- original page 266 -->

*Consequently, one has the inequality*

```text
  rg Ω^1_{L/k} − rg_K Ω^1_{K/k} ≥ deg.tr_K L                                         (21.7.3.2)
```

*the equality being attained if and only if $k$ is an admissible field for the extension $L$ of $K$.*

One has in fact the exact sequence `(20.6.1.1)`

```text
  0 → Υ_{L/K/k} → Ω^1_{K/k} ⊗_K L → Ω^1_{L/k} → Ω^1_{L/K} → 0
```

hence the first side of `(21.7.3.1)` is equal to

```text
  rg_L Ω^1_{L/K} − rg_L Υ_{L/K/k}
```

and it suffices to apply `(21.7.2)`.

The interest of this last corollary is that it brings in only modules of differentials, to the exclusion of imperfection
modules. We shall see moreover further on `(21.8.6)` that for every extension $L$ of $K$ of finite type, there exists a
subfield $k$ of $K$ such that $[K : k]$ be finite and which is admissible for the extension $L$ of $K$, so that the two
sides of `(21.7.3.2)` are then equal.

**Corollary (21.7.4).**

<!-- label: 0_IV.21.7.4 -->

*Let $K$ be an extension of finite type of a field $k$. The following conditions are equivalent:*

*a) $K$ is a finite separable extension of $k$.*

*b) $K$ is a $k$-algebra formally unramified `(19.10.2)`.*

*c) $K$ is a $k$-algebra formally étale `(19.10.2)`.*

*d) One has $\Omega^{1}_{K/k} = 0$.*

In fact, one knows (the topologies being discrete) that conditions b) and d) are equivalent `(20.7.4)` and that a)
entails that $K$ is a $k$-algebra formally smooth `(19.6.1)`, hence the conjunction of a) and b) is equivalent to c).
Everything comes down to seeing that d) entails a). Now, by virtue of `(21.7.1.1)`, the relation $\Omega^{1}_{K/k} = 0$
entails that $K$ is algebraic (hence finite) over $k$ and that $\Upsilon_{K/k} = 0$, that is to say `(20.6.3)` that $K$
is separable over $k$.

**Remark (21.7.5).**

<!-- label: 0_IV.21.7.5 -->

*By virtue of `(20.6.3.2)` and of $(0_{III}, 11.10.2)$ the first side of `(21.7.1.1)` is none other than the
Euler-Poincaré characteristic of the complex $K.(C/B/A)$ introduced in `(20.6.3)`, for $C = L$, $B = K$ and $A = P$
(prime field of $K$). In the chapter devoted to the theory of intersections and the Riemann-Roch theorem, an important
role will be played also by generalized Euler-Poincaré characteristics (with values in groups of classes of
$\mathcal{O}$-Modules) of complexes generalizing the complexes $\Gamma.(C/A)$ considered in `(20.6.22)`.*

### 21.8. Admissibility criteria

We return to our earlier conventions and therefore suppose that all the fields considered in this number are of
characteristic $p > 0$.

**Lemma (21.8.1).**

<!-- label: 0_IV.21.8.1 -->

*Let $K$ be a field, $k$ a subfield of $K$, $(k_{\alpha})_{\alpha \in I}$ a filtered decreasing family of subfields of
$K$ such that $k = \bigcap_{\alpha \in I} k_{\alpha}$. Let $V$ be a vector space over $K$, $(a_{i})_{1 \leq i \leq n}$*

<!-- original page 267 -->

*a finite family of vectors of $V$; if the family $(a_{i})$ is free over $k$, there exists an index $\gamma$ such that
it is also free over $k_{\gamma}$.*

Let $r$ be the rank of the family $(a_{i})_{1 \leq i \leq n}$ over $K$, and let us reason by induction on $n - r$; the
proposition is evident for $n = r$, for then the family $(a_{i})_{1 \leq i \leq r}$ is free over $K$, hence over every
subfield of $K$. Suppose for example that $(a_{i})_{1 \leq i \leq r}$ is free over $K$, and write $a_{r+1} =
\sum^{r}_{i=1} \lambda_{i} a_{i}$, with $\lambda_{i} \in K$; the family $(a_{i})_{1 \leq i \leq r+1}$ being free over
$k$, the $\lambda_{i}$ cannot all belong to $k$; suppose for example that $\lambda_{1} \notin k$. Then there exists an
index $\beta$ such that $\lambda_{1} \notin k_{\beta}$; one concludes that the family $(a_{i})_{1 \leq i \leq r+1}$ is
free over $k_{\beta}$; in fact, as the family $(a_{i})_{1 \leq i \leq r}$ is free over every subfield of $K$, if the
family $(a_{i})_{1 \leq i \leq r+1}$ were not free over $k_{\beta}$, $a_{r+1}$ would be equal to a linear combination of
the $a_{i}$ with coefficients in $k_{\beta}$, and as these coefficients are necessarily the $\lambda_{i}$, one arrives
at a contradiction. It now suffices to apply the induction hypothesis replacing $K$ by $k_{\beta}$ and the family
$(k_{\alpha})_{\alpha \in I}$ by the sub-family of the $k_{\alpha}$ contained in $k_{\beta}$.

**Lemma (21.8.2).**

<!-- label: 0_IV.21.8.2 -->

*Let $K$ be a field, $p$ its characteristic exponent, $k_{0}$ a subfield of $K$, $(k_{\alpha})_{\alpha \in I}$ a
filtered decreasing family of subfields of $K$ such that $\bigcap_{\alpha} k_{\alpha}(K^{p}) = k_{0}(K^{p})$. If
$(x_{i})_{1 \leq i \leq n}$ is a finite family of elements of $K$ which is $p$-free over $k_{0}$, there exists an index
$\alpha$ such that $(x_{i})$ is $p$-free over $k_{\alpha}$.*

In fact, saying that the family $(x_{i})$ is $p$-free over a subfield $k$ of $K$ means that the finite family of
monomials $\prod^{n}_{i=0} x^{m(i)}_{i}$ with $0 \leq m(i) < p$ is free over $k(K^{p})$; it therefore suffices to apply
lemma `(21.8.1)` to this family of monomials in the vector space $V = K$, and to the subfields $k_{\alpha}(K^{p})$ and
$k_{0}(K^{p})$ of $K$.

**Theorem (21.8.3).**

<!-- label: 0_IV.21.8.3 -->

*Let $K$ be a field of characteristic $p > 0$, $k_{0}$ a subfield of $K$, $(k_{\alpha})_{\alpha \in I}$ a filtered
decreasing family of subfields of $K$ containing $k_{0}$. The following conditions are equivalent:*

*a) $\bigcap_{\alpha} k_{\alpha}(K^{p}) = k_{0}(K^{p})$.*

*b) For every extension $L$ of $K$ such that $\Upsilon_{L/K/k_{0}}$ is an $L$-vector space of finite rank (which holds
in particular if $L$ is an extension of finite type by virtue of `(21.7.2)`), there exists $\alpha \in I$ such that
$k_{\alpha}$ is $k_{0}$-admissible for the extension $L$ of $K$.*

*b') For every extension $L = K(x)$ of $K$, with $x \in K$, there exists $\alpha \in I$ such that $k_{\alpha}$ is
$k_{0}$-admissible for the extension $L$ of $K$.*

*c) The canonical map*

$$ \Omega^{1}_{K/k_{0}} \to \lim_{\alpha} \Omega^{1}_{K/k_{\alpha}} (21.8.3.1) $$

*is injective.*

The canonical map `(21.8.3.1)` is of course obtained by passage to the projective limit in the projective system of
homomorphisms $\Omega^{1}_{K/k_{0}} \to \Omega^{1}_{K/k_{\alpha}}$ `(20.5.3.3)`. We shall prove the theorem according to
the logical schema `c) ⇒ b) ⇒ b') ⇒ a) ⇒ c)`.

Saying that $k_{\alpha}$ is $k_{0}$-admissible for the extension $L$ of $K$ means that the canonical homomorphism

<!-- original page 268 -->

$\Upsilon_{L/K/k_{0}} \to \Upsilon_{L/K/k_{\alpha}}$ is injective; now, if $N_{\alpha}$ is the kernel of this
homomorphism, the $N_{\alpha}$ form a filtered decreasing system of sub-vector spaces of $\Upsilon_{L/K/k_{0}}$, and as
$\Upsilon_{L/K/k_{0}}$ is by hypothesis of finite rank, it amounts to the same to say that one of the $N_{\alpha}$ is
`0` or that their intersection is `0`. But this intersection is none other than the kernel of the homomorphism limit
projective $\Upsilon_{L/K/k_{0}} \to \lim_{\alpha} \Upsilon_{L/K/k_{\alpha}}$. Now, one has the commutative diagram

```text
  Υ_{L/K/k_0}                ——→ lim_α Υ_{L/K/k_α}
       ↓                                ↓
  Ω^1_{K/k_0} ⊗_K L          ——→ lim_α (Ω^1_{K/k_α} ⊗_K L)
```

where the left vertical arrow is injective by definition. In order to prove that c) entails b), it therefore suffices to
show that c) entails that the canonical map

```text
  Ω^1_{K/k_0} ⊗_K V → lim_α (Ω^1_{K/k_α} ⊗_K V)                                      (21.8.3.2)
```

is injective for every vector space $V$ over $K$ (and in particular for $V = L$). Now this is evident if $V = K^{n}$
since then $W \otimes_{K} V = W^{n}$ for every vector space $W$ over $K$ and products and projective limits commute. On
the other hand, for every element $\xi$ of the first side of `(21.8.3.2)` there exists a sub-vector space $V'$ of $V$ of
finite rank such that $\xi \in \Omega^{1}_{K/k_{0}} \otimes_{K} V'$ (canonically identified with a sub-space of
$\Omega^{1}_{K/k_{0}} \otimes_{K} V$); if $\xi \neq 0$, its image in $\lim_{\alpha} (\Omega^{1}_{K/k_{\alpha}}
\otimes_{K} V')$ is therefore non zero; as the functor `lim` is left exact, the image of $\xi$ in the second side of
`(21.8.3.2)` is therefore also $\neq 0$, which finishes showing that c) implies b).

It is trivial that b) entails b'); let us show that b') entails a). With the notation of b'), one can suppose that $L
\neq K$. It then follows from `(21.4.7)` that one has $rg_{L} \Upsilon_{L/K/k_{0}} \leq 1$. If $\Upsilon_{L/K/k_{0}} =
0$ there is nothing to prove by virtue of `(21.6.1.1)`. Otherwise, $\Upsilon_{L/K/k_{0}}$ is identified canonically with
$\Upsilon_{L/K}$ and if one sets $a = x^{p}$, $\Upsilon_{L/K}$ has a basis formed by the single element $d_{L} a \otimes
1$ `(21.4.7)`; $\Upsilon_{L/K/k_{\alpha}}$ therefore has a basis formed by the single element $d_{K/k_{\alpha}}(a)
\otimes 1$, and saying that a subfield $k_{\alpha}$ is $k_{0}$-admissible for the extension $L$ of $K$ means that one
has $d_{K/k_{\alpha}}(a) \neq 0$, or again `(21.4.5)` that $a \notin k_{\alpha}(K^{p})$. Now, for every $a \notin
k_{0}(K^{p})$, one has $d_{K/k_{0}}(a) \neq 0$ and $K(a^{1/p}) \neq K$, hence one can apply b'), which proves the
existence of an $\alpha$ such that $a \notin k_{\alpha}(K^{p})$; in other words b') implies a).

It remains to show that a) implies c). Let $(x_{\lambda})_{\lambda \in M}$ be a $p$-basis of $K$ over $k_{0}$; then, the
$d_{K/k_{0}}(x_{\lambda})$ form a basis of the $K$-vector space $\Omega^{1}_{K/k_{0}}$ `(21.4.5)`, and condition c)
means that for every finite part $J$ of the index set $M$, there exists an $\alpha \in I$ such that the
$d_{K/k_{\alpha}}(x_{\mu})$ for $\mu \in J$ are linearly independent in $\Omega^{1}_{K/k_{\alpha}}$; but this means also
`(21.4.5)` that the $x_{\mu}$ for $\mu \in J$ form a $p$-free family over $k_{\alpha}$, and the existence of an $\alpha$
having this property follows from `(21.8.2)` and from hypothesis a).

<!-- original page 269 -->

**Corollary (21.8.4).**

<!-- label: 0_IV.21.8.4 -->

*Let $K$ be a field of characteristic $p > 0$, $k_{0}$ a subfield of $K$, $(k_{\alpha})_{\alpha \in I}$ a filtered
decreasing family of subfields of $K$, containing $k_{0}$, such that*

$$ \bigcap_{\alpha} k_{\alpha}(K^{p}) = k_{0}(K^{p}). $$

*Let $L$ be an extension of $K$ such that $\Upsilon_{L/K/k_{0}}$ is an $L$-vector space of finite rank; then, for every
field $K'$ such that $K \subset K' \subset L$, there exists $\alpha \in I$ such that $k_{\alpha}$ is $k_{0}$-admissible
for the extension $L$ of $K'$.*

It suffices to apply `(21.8.3)` and `(21.6.6)`.

**Corollary (21.8.5).**

<!-- label: 0_IV.21.8.5 -->

*Let $K$ be a field of characteristic $p > 0$, $k_{0}$ a subfield of $K$, $(k_{\alpha})_{\alpha \in I}$ a filtered
decreasing family of subfields of $K$ containing $k_{0}$, such that*

$$ \bigcap_{\alpha} k_{\alpha}(K^{p}) = k_{0}(K^{p}). $$

*Then, for every extension $L$ of $K$ such that $\Upsilon_{L/K/k_{0}}$ is an $L$-vector space of finite rank, one has
$\bigcap_{\alpha} k_{\alpha}(L^{p}) = k_{0}(L^{p})$.*

Suppose in fact that $M$ is an extension of $L$ such that $\Upsilon_{M/L/k_{0}}$ is an $M$-vector space of finite rank.
The exact sequence `(21.6.1.1)`

```text
  0 → Υ_{L/K/k_0} ⊗_L M → Υ_{M/K/k_0} → Υ_{M/L/k_0}
```

and the hypothesis then show that $\Upsilon_{M/K/k_{0}}$ is also an $M$-vector space of finite rank. There therefore
exists an index $\alpha$ such that $k_{\alpha}$ is $k_{0}$-admissible for the extension $M$ of $K$ `(21.8.3)`, hence
also for the extension $M$ of $L$ `(21.6.6)`; this taking place for every extension $M$ of $L$ such that
$\Upsilon_{M/L/k_{0}}$ be of finite rank, the corollary follows from the equivalence of a) and b) in `(21.8.3)`.

**Corollary (21.8.6).**

<!-- label: 0_IV.21.8.6 -->

*Let $K$ be a field, $p$ its characteristic exponent, $k_{0}$ a subfield of $K$. If $L$ is an extension of $K$ such that
$\Upsilon_{L/K/k_{0}}$ is an $L$-vector space of finite rank, there exists a subfield $k$ of $K$, containing
$k_{0}(K^{p})$, such that $[K : k]$ be finite, and which is $k_{0}$-admissible for the extension $L$ of $K$.*

It suffices in fact, by virtue of `(21.8.3)`, to construct a filtered decreasing family $(k_{\alpha})_{\alpha \in I}$ of
subfields of $K$, containing $K^{p}$ and $k_{0}$, for which $[K : k_{\alpha}] < +\infty$ and $\bigcap_{\alpha}
k_{\alpha} = k_{0}(K^{p})$. For this one considers a $p$-basis $(x_{\lambda})_{\lambda \in J}$ of $K$ over $k_{0}$ and,
for every finite part $H$ of $J$, one considers the subfield $k_{H}$ of $K$ generated by $k_{0}(K^{p})$ and the
$x_{\lambda}$ of index $\lambda \in J - H$; it follows from this definition that $(x_{\lambda})_{\lambda \in H}$ is a
$p$-basis of $K$ over $k_{H}$, and one concludes at once that the $k_{H}$ verify the desired conditions.

**Remarks (21.8.7).**

<!-- label: 0_IV.21.8.7 -->

*(i) One has already seen `(21.7.2)` that if $L$ is an extension of finite type of $K$, $\Upsilon_{L/K/k_{0}}$ is of
finite rank for every subfield $k_{0}$ of $K$. The same holds if $L$ is a separable extension of $K$, for by virtue of
`(20.6.19)`, one has $\Upsilon_{L/K/k_{0}} = 0$. Finally, if $L$ is an extension of finite type of a separable extension
`L_0` of $K$, the same reasoning as in `(21.8.5)` shows that $\Upsilon_{L/K/k_{0}}$ is still of finite rank (and in fact
is isomorphic to a sub-space of $\Upsilon_{L/L_{0}/k_{0}}$).*

<!-- original page 270 -->

*(ii) In the statement of `(21.8.5)`, and consequently also in that of `(21.8.3, b))`, one cannot omit the hypothesis
that $\Upsilon_{L/K/k_{0}}$ is of finite rank over $L$. Let us take for $k_{0}$ the prime field $\mathbb{F}_{p}$, for
$K$ a field such that $[K : K^{p}]$ be countably infinite (for example the field of rational fractions
$\mathbb{F}_{p}(X_{1}, \cdots, X_{n}, \cdots)$ in infinitely many indeterminates); the construction procedure of
`(21.8.6)` shows at once that there exists a strictly decreasing infinite sequence $(K_{n})$ of subfields of $K$ such
that $K_{0} = K$ and $\bigcap_{n} K_{n} = K^{p}$. We are going to construct an increasing sequence of finite extensions
$M_{n}$ of $K$, such that if $M$ is the union of the $M_{n}$, the extension $L = M^{1/p}$ of $K$ provides a
counter-example to `(21.8.5)`. For this, let $x$ be an element of $K - K_{1}$, set $M_{0} = K$ and $M_{n} = K(a_{1} x,
a_{2} x, \cdots, a_{n} x)$ for $n \geq 1$, where the $a_{n}$ are constructed by induction so that $a_{n} \in K_{n}$ and
$a_{n+1} \notin M_{n}(x)$ for every $n$: this is possible, for $M_{n}(x)$ is of finite degree over $K_{n}$, while the
same is not so of $K_{n}$. One concludes at once that $x \notin M = L^{p}$, but as $x = (a_{n} x) a^{-1}_{n}$, one has
$x \in K_{n}(M) = K_{n}(L^{p})$ for every $n$.*

**Proposition (21.8.8).**

<!-- label: 0_IV.21.8.8 -->

*Let $k$ be a field of characteristic $p > 0$, and let $A = k[[T_{1}, \cdots, T_{r}]]$ be the ring of formal power
series in $r$ indeterminates over $k$, $K = k((T_{1}, \cdots, T_{r}))$ its field of fractions. Then there exists a
filtered decreasing family $(A_{\alpha})$ of Noetherian subrings of $A$ such that $A$ be a free $A_{\alpha}$-module of
finite type for every $\alpha$ and that, if $K_{\alpha}$ is the field of fractions of $A_{\alpha}$, one has
$\bigcap_{\alpha} K_{\alpha} = K^{p}$.*

One can write $K^{p} = k^{p}((T^{p}_{1}, \cdots, T^{p}_{r}))$; one has seen in the proof of `(21.8.6)` that there exists
a decreasing family $(k_{\alpha})$ of subfields of $k$ such that $[k : k_{\alpha}]$ is finite for every $\alpha$ and
$\bigcap_{\alpha} k_{\alpha} = k^{p}$; it is clear that if one sets $A_{\alpha} = k_{\alpha}[[T^{p}_{1}, \cdots,
T^{p}_{r}]]$, $A$ is a free $A_{\alpha}$-module of finite type; everything therefore comes down to proving the relation

```text
  ⋂_α k_α((T_1^p, …, T_r^p)) = k^p((T_1^p, …, T_r^p)).                                (21.8.8.1)
```

Since $\bigcap_{\alpha} k_{\alpha} = k^{p}$, this will follow from the two following lemmas:

**Lemma (21.8.8.2).**

<!-- label: 0_IV.21.8.8.2 -->

*If $k'$ is an extension of a field $k$, one has*

```text
  k'[[T_1, …, T_r]] ∩ k((T_1, …, T_r)) = k[[T_1, …, T_r]].
```

In fact, set $C = k[[T_{1}, \cdots, T_{r}]]$, $D = k'[[T_{1}, \cdots, T_{r}]]$; as $k((T_{1}, \cdots, T_{r}))$ is the
field of fractions of $C$, it will suffice to prove that $D$ is a faithfully flat $C$-module (Bourbaki, Alg. comm.,
chap. I, §3, n° 5, prop. 10). Now, $C$ and $D$ are Noetherian local rings, and if $\mathfrak{m}$ is the maximal ideal of
$C$, one has $D/\mathfrak{m} D = (C/\mathfrak{m}) \otimes_{k} k'$, hence $D/\mathfrak{m} D$

<!-- original page 271 -->

is a flat $(C/\mathfrak{m})$-module; it therefore suffices to apply $(0_{III}, 10.2.1)$ and $(0_{I}, 6.6.2)$.

**Lemma (21.8.8.3).**

<!-- label: 0_IV.21.8.8.3 -->

*Let $k$ be a field, $(k_{\alpha})$ a filtered decreasing family of subfields of $k$, and set $k_{0} = \bigcap_{\alpha}
k_{\alpha}$. Suppose there exists a power $q$ of the characteristic exponent of $k$ such that $k^{q} \subset k_{0}$.
Then one has*

```text
  ⋂_α k_α((T_1, …, T_r)) = k_0((T_1, …, T_r)).                                       (21.8.8.4)
```

It suffices to prove that an element $f \neq 0$ of the first side of `(21.8.8.4)` belongs to the second side. Let
$\gamma$ be an index, $g_{\gamma} \in k_{\gamma}[[T_{1}, \cdots, T_{r}]]$ such that $g_{\gamma} f \in k_{\gamma}[[T_{1},
\cdots, T_{r}]]$; up to replacing $g$ by $g^{q}$, one can suppose that $g \in k_{0}[[T_{1}, \cdots, T_{r}]]$. Then, for
every $\alpha \geq \gamma$, one has

```text
  k_α[[T_1, …, T_r]] ∩ k_γ((T_1, …, T_r)) = k_α[[T_1, …, T_r]]
```

by virtue of lemma `(21.8.8.2)`. But it is clear that the intersection of the rings $k_{\alpha}[[T_{1}, \cdots, T_{r}]]$
is none other than $k_{0}[[T_{1}, \cdots, T_{r}]]$, and one has therefore indeed $f \in k_{0}((T_{1}, \cdots, T_{r}))$.

### 21.9. Completed differential modules in formal power series rings

In this number, the fields are no longer necessarily supposed to be of characteristic `> 0`.

**Lemma (21.9.1).**

<!-- label: 0_IV.21.9.1 -->

*Let $k$ be a field, $A$ a complete Noetherian local ring which is a $k$-algebra, $K$ the residue field of $A$. If $K$
is an extension of finite type of $k$, the $A$-module $\hat{\Omega}^{1}_{A/k}$ is of finite type.*

By virtue of `(20.7.15)`, it suffices to prove that $\Omega^{1}_{K/k}$ is a $K$-vector space of finite rank. Now, by
hypothesis, $K$ is the field of fractions of a $k$-algebra of finite type $B$; as $\Omega^{1}_{B/k}$ is a $B$-module of
finite type by virtue of `(20.4.7)`, the conclusion follows from `(20.5.9)`.

**Proposition (21.9.2).**

<!-- label: 0_IV.21.9.2 -->

*Let $k_{0}$ be a field, $A$ a complete Noetherian local ring which is a $k_{0}$-algebra formally smooth, $\mathfrak{m}$
its maximal ideal, $K = A/\mathfrak{m}$ its residue field (so that as a ring $A$ is isomorphic to a ring of formal power
series $K[[T_{1}, \cdots, T_{n}]]$ `(19.6.5)`). If $K$ is an extension of finite type of $k_{0}$, then
$\hat{\Omega}^{1}_{A/k_{0}}$ is a free $A$-module of rank equal to $\dim(A) + deg.tr_{k_{0}} K$. Moreover, for every
subfield $k$ of $k_{0}$ such that $\Omega^{1}_{k_{0}/k}$ is of finite rank, $\hat{\Omega}^{1}_{A/k}$ is a free
$A$-module of rank equal to $\dim(A) + deg.tr_{k} K + rg_{k_{0}}(\Omega^{1}_{k_{0}/k})$.*

It is clear that, if $P$ is the prime subfield of $k_{0}$, $K$ is a $P$-algebra formally smooth `(19.6.1)`. Note on the
other hand that one has $\Upsilon_{k_{0}/P} = 0$: in fact, this comes down to seeing that the homomorphism

```text
  Ω̂^1_{k_0/P} ⊗̂_{k_0} K = Ω^1_{k_0/P} ⊗_{k_0} K → Ω^1_{A/P} ⊗_A K
```

is injective `(20.6.14.5)`, $u$ denoting the structural homomorphism $k_{0} \to A$. But as $A$ is a $k_{0}$-algebra
formally smooth by hypothesis, it follows from `(20.7.2)` that $u^{*}_{P}$ is formally left invertible, hence `(19.1.7)`
$u^{*}_{P} \otimes 1_{K}$ is left invertible and a fortiori injective, which proves our assertion. Applying the exact
sequence `(20.6.22.1)`, where `A, k, B, C` are replaced by $P, k_{0}, A, K$, one has the exact sequence

```text
  0 → Υ_{K/k_0/P} → 𝔪/𝔪^2 → Ω^1_{k_0/P} ⊗_{k_0} K → Ω^1_{K/P} → Ω^1_{K/k_0} → 0
```

so that one has

```text
  rg_K(Ω̂^1_{A/k_0} ⊗_A K) = rg_K(𝔪/𝔪^2) + (rg_K(Ω^1_{K/k_0}) − rg_K(Υ_{K/k_0/P})) = rg_K(𝔪/𝔪^2) + deg.tr_{k_0} K
```

by virtue of `(21.7.1)`. On the other hand, $\hat{\Omega}^{1}_{A/k_{0}}$ is a formally projective $A$-module `(20.4.9)`,
and as its topology is the $\mathfrak{m}$-preadic topology `(20.4.5)`, $\hat{\Omega}^{1}_{A/k_{0}}/\mathfrak{m}^{j+1}
\hat{\Omega}^{1}_{A/k_{0}}$ is a projective $(A/\mathfrak{m}^{j+1})$-module for every $j$ `(19.2.4)`, hence free
$(0_{I}, 10.1.2)$ and of rank

<!-- original page 272 -->

$= rg_{K}(\hat{\Omega}^{1}_{A/k_{0}} \otimes_{A} K)$. By virtue of `(21.9.1)`, $\hat{\Omega}^{1}_{A/k_{0}}$ is an
$A$-module of finite type, and moreover this $A$-module is flat by virtue of $(0_{I}, 10.2.1)$; it is therefore free
$(0_{I}, 10.1.3)$ of rank $n$, whence the first assertion.

Since by hypothesis $\Omega^{1}_{k_{0}/k}$ is of finite rank over $k_{0}$, the completed tensor product
$\Omega^{1}_{k_{0}/k} \hat{\otimes}_{k_{0}} A$ is identified with $\Omega^{1}_{k_{0}/k} \otimes_{k_{0}} A$; as $A$ is a
$k_{0}$-algebra formally smooth, it follows from `(20.7.18)` that the homomorphism

```text
  u^*_{A/k_0/k} : Ω̂^1_{k_0/k} ⊗̂_{k_0} A → Ω̂^1_{A/k}
```

admits a left inverse which is a continuous $A$-homomorphism, which implies in particular that its image is closed in
$\hat{\Omega}^{1}_{A/k}$; the sequence

```text
  0 → Ω^1_{k_0/k} ⊗_{k_0} A → Ω̂^1_{A/k} → Ω̂^1_{A/k_0} → 0
```

is therefore exact and split by virtue of `(20.7.17)` and of what precedes; which finishes proving the proposition.

**Corollary (21.9.3).**

<!-- label: 0_IV.21.9.3 -->

*Let $k$ be a field, $A$ the formal power series ring $k[[T_{1}, \cdots, T_{r}]]$, equipped with its usual $k$-algebra
structure. Then $\hat{\Omega}^{1}_{A/k}$ is a free $A$-module of rank $r = \dim(A)$.*

It suffices to note that $A$ is a $k$-algebra formally smooth `(19.3.4)`, and to apply `(21.9.2)` with $k_{0} = k = K$.

**Lemma (21.9.4).**

<!-- label: 0_IV.21.9.4 -->

*Let $k$ be a field of characteristic $p > 0$, $A$ a $k$-algebra which is a complete Noetherian local ring, $B$ a
sub-$k$-algebra of $A$ isomorphic to a topological $k$-algebra of the form $k[[T_{1}, \cdots, T_{r}]]$ and such that $A$
be a $B$-algebra of finite type. If `B_1` is the subalgebra $k[[T^{p}_{1}, \cdots, T^{p}_{r}]]$ of $B$,
$\hat{\Omega}^{1}_{A/B}$ is identified canonically with $\hat{\Omega}^{1}_{A/B_{1}}$.*

Every continuous derivation of `B_1` into a topological $A$-module $P$, which is the restriction of a continuous
$A$-derivation of $A$ into $P$, is zero, for it is so on the subring $k[T^{p}_{1}, \cdots, T^{p}_{r}]$ of polynomials,
and this last is dense in `B_1`. The exact sequence `(20.3.7.1)` therefore shows that the canonical homomorphism

```text
  Der.cont_B(A, P) → Der.cont_{B_1}(A, P)
```

is bijective; the conclusion follows from `(20.7.14.4)`, taking account of the fact that $\hat{\Omega}^{1}_{A/B}$ is an
$A$-module of finite type `(20.4.7)`, hence separated and complete since $A$ is a complete Noetherian local ring.

**Proposition (21.9.5).**

<!-- label: 0_IV.21.9.5 -->

*Let $A$ be an integral complete Noetherian local ring, `A_0` a subring of $A$ isomorphic to a formal power series ring
$k[[T_{1}, \cdots, T_{r}]]$ over a field $k$, such that $A$ be a finite `A_0`-algebra and that the field of fractions
$E$ of $A$ be a separable extension of the field of fractions `L_0` of `A_0`. Then one has*

```text
  rg_A Ω̂^1_{A/A_0} = rg_E(Ω̂^1_{A/A_0} ⊗_A E) = dim(A).                               (21.9.5.1)
```

Note that if $\mathfrak{m}_{0}$ is the maximal ideal of `A_0`, the topology of $A$ is the $\mathfrak{m}_{0}$-adic
topology since $A$ is a finite `A_0`-algebra (Bourbaki, Alg. comm., chap. IV, §2, n° 5, cor. 3 of prop. 9) and induces
on `A_0` the $\mathfrak{m}_{0}$-adic topology (Bourbaki, Alg. comm., chap. III, §3, n° 4, th. 3). One knows `(21.9.1)`
that $\hat{\Omega}^{1}_{A/A_{0}}$ is an $A$-module of finite type, and

<!-- original page 273 -->

by virtue of `(21.9.3)` $\hat{\Omega}^{1}_{A_{0}/k}$ is a free `A_0`-module of rank $r = \dim(A_{0}) = \dim(A)$
`(16.1.5)`; the tensor product $\hat{\Omega}^{1}_{A_{0}/k} \otimes_{A_{0}} A$ is therefore a free $A$-module of rank $r$
identical with its separated completion; finally $\hat{\Omega}^{1}_{A/k}$ is an $A$-module of finite type `(20.4.7)`,
hence identical with its separated completion $(0_{I}, 7.3.6)$. This being so, in the sequence of homomorphisms

```text
  Ω̂^1_{A_0/k} ⊗_{A_0} A → Ω̂^1_{A/k} → Ω̂^1_{A/A_0} → 0                                (21.9.5.2)
```

one knows that $v$ is surjective and that $Im(u)$ is dense in $Ker(v)$ `(20.7.17)`; but every sub-`A_0`-module of
$\hat{\Omega}^{1}_{A/k}$ is closed for the $\mathfrak{m}_{0}$-adic topology $(0_{I}, 7.3.5)$, hence the sequence
`(21.9.5.2)` is exact. Note on the other hand that since $A$ is integral over `A_0`, `A_0` integrally closed and $E$
separable over `L_0`, $\hat{\Omega}^{1}_{A/A_{0}}$ is a torsion $A$-module `(20.4.13, (iv))`; tensorizing the exact
sequence `(21.9.5.2)` by $E$, one obtains an exact sequence

```text
  Ω̂^1_{A_0/k} ⊗_{A_0} E → Ω̂^1_{A/k} ⊗_A E → 0
```

whence $rg_{E}(\hat{\Omega}^{1}_{A/k} \otimes_{A} E) \leq r$. It remains therefore to show that there exist, in
$\hat{\Omega}^{1}_{A/k} \otimes_{A} E$, $r$ elements linearly independent over $E$. Now, let $D_{i} = \partial/\partial
T_{i}$ be the canonical derivations of `A_0` into itself $(1 \leq i \leq r)$; they extend in a unique manner to
derivations (still denoted $D_{i}$) of $E$ into itself, since $E$ is a finite separable extension of `L_0`; by
restriction to $A$, these derivations give derivations of $A$ into $E$, and it is immediate that these derivations take
their values in a same sub-$A$-module of finite type of $E$; as they are continuous on `A_0` and the topology of $A$ is
the $\mathfrak{m}_{0}$-adic topology, one has thus formed $r$ continuous derivations of $A$ into a topological
$A$-module, which are evidently linearly independent since $D_{i}(T_{j}) = \delta_{ij}$; this finishes proving the
proposition.

The following proposition is a "formal" analogue of `(21.7.3)`:

**Proposition (21.9.6).**

<!-- label: 0_IV.21.9.6 -->

*Let $k_{0} \subset k \subset K_{0}$ be three fields of characteristic $p > 0$, such that $[K_{0} : k] < +\infty$; set*

```text
  L_0 = K_0((T_1, …, T_r)),     M_0 = K_0((T_1^p, …, T_r^p))
  L = k((T_1, …, T_r)),         M = k((T_1^p, …, T_r^p)),     N = k((T_1^p, …, T_r^p)).
```

*Let $E$ be an extension of finite type of `L_0`.*

*(i) If $\Upsilon_{K_{0}/k_{0}}$ is of finite rank, one has*

```text
  rg_E Ω^1_{E/M_0} − rg_{K_0} Ω^1_{K_0/k_0} = (r + deg.tr_k E) + d(E/K_0, k/k_0) + d(E/M_0, N/k_0)   (21.9.6.1)
```

*(notation of `(21.6.1)`), and in particular one has*

```text
  rg_E Ω^1_{E/M} − rg_K Ω^1_{K/k} ≥ r + deg.tr_k E + d(E/K_0, k_0).                   (21.9.6.2)
```

*Moreover, if the two sides of `(21.9.6.2)` are equal, they remain so when one replaces $k$ by a field $k'$ such that
$k_{0} \subset k' \subset k$.*

*(ii) Suppose moreover that $[k_{0} : k^{p}_{0}] < +\infty$. Let $(k_{\alpha})$ be a filtered decreasing family of
subfields of `K_0` containing $k_{0}$, such that $[K_{0} : k_{\alpha}] < +\infty$ for every $\alpha$ and that
$\bigcap_{\alpha} k_{\alpha}(K^{p}_{0}) = k_{0}(K^{p}_{0})$; then there exists an $\alpha$ such that, for $k =
k_{\alpha}$, the two sides of `(21.9.6.2)` are equal.*

<!-- original page 274 -->

(i) One knows `(21.1.5, (ii))` that $rg_{E} \Omega^{1}_{E/M}$ does not change when one replaces $M$ by $M(L^{p}_{0})$;
as $L^{p}_{0} = K^{p}_{0}((T^{p}_{1}, \cdots, T^{p}_{r}))$ and $[k(K^{p}_{0}) : k] < +\infty$, one has

$$ M(L^{p}_{0}) = k(K^{p}_{0})((T^{p}_{1}, \cdots, T^{p}_{r})); $$

similarly $\Omega^{1}_{K/k}$ does not change when one replaces $k$ therein by $k(K^{p}_{0})$, so that one can suppose
$K^{p}_{0} \subset k$, which we shall do in all the sequel. We shall also introduce the fields

```text
  k_1 = k_0(K_0^p),    N_1 = k_1((T_1^p, …, T_r^p))
```

so that one has the diagram of fields

```text
  K_0 ——→ M_0 ——→ L_0 ——→ E
   ↑       ↑       ↑       ↑
   k ———→ N  ———→ M ————→ L
   ↑       ↑       ↑
  k_1 ——→ N_1
```

We propose to evaluate the difference $\delta$ of the first and second sides of `(21.9.6.2)`.

It follows from `(21.7.3)` that one has

```text
  rg_E Ω^1_{E/M} − rg_{M_0} Ω^1_{M_0/M} = deg.tr_M E + d(E/M_0, M)
```

and as `L_0` is a finite extension of `M_0`, one has $deg.tr_{M} E = deg.tr_{L_{0}} E$. On the other hand, a $p$-basis
of `K_0` over $k = k(K^{p}_{0})$ is also a $p$-basis of `M_0` over $M$, hence `(21.4.5)`, one has

```text
  rg_{M_0} Ω^1_{M_0/M} = rg_{K_0} Ω^1_{K_0/k}
```

so that one has

```text
  δ = d(E/M_0, M) − d(E/K_0, k_0) − r.                                                (21.9.6.3)
```

Let us note now the classical lemma:

**Lemma (21.9.6.4).**

<!-- label: 0_IV.21.9.6.4 -->

*For every field $k$, the formal power series field $K = k((T_{1}, \cdots, T_{r}))$ is a separable extension of $k$.*

Let us briefly recall the proof of this lemma for completeness. It suffices (Bourbaki, Alg., chap. VIII, §7, n° 3, proof
of th. 1) to prove that for every finite extension $k'$ of $k$, $K \otimes_{k} k'$ is without nilpotent element; but if
one sets $A = k[[T_{1}, \cdots, T_{r}]]$ and $S = A - \{0\}$, $K \otimes_{k} k'$ is equal to $S^{-1}(A \otimes_{k} k')$,
and $A \otimes_{k} k'$ is identified canonically with the integral ring $A' = k'[[T_{1}, \cdots, T_{r}]]$ and $A$ to a
subring of $A'$, whence the conclusion.

Using this lemma and `(21.6.2, (ii))`, one has $d(L_{0}/K_{0}, k_{0}) = 0$, and formula `(21.6.4.4)` therefore gives

```text
  d(E/K_0, k_0) = d(E/L_0, k_0).
```

<!-- original page 275 -->

Formulas `(21.6.4.4)` and `(21.6.4.2)` on the other hand give

```text
  d(E/M_0, M) = d(E/L_0, M) + d(L_0/M_0, M),
  d(L_0/M_0, M) = d(L_0/M_0, M/N) + d(L_0/M_0, N)
```

whence

```text
  δ = d(E/L_0, M) + d(L_0/M_0, N) − d(E/L_0, k_0) + d(L_0/M_0, M/N) − r.
```

We are going to show that one has the relation

$$ d(L_{0}/M_{0}, M/N) = r. (21.9.6.5) $$

For this, note that by definition, one has

```text
  d(L_0/M_0, M/N) = rg_{L_0} Ω^1_{L_0/M/N} − rg_{M_0} Ω^1_{M_0/M/N}.
```

Taking account of the two exact sequences

```text
  0 → Υ_{L_0/M/N} → Ω^1_{M/N} ⊗_M L_0 → Ω^1_{L_0/N} → Ω^1_{L_0/M} → 0
  0 → Υ_{M_0/M/N} → Ω^1_{M/N} ⊗_M M_0 → Ω^1_{M_0/N} → Ω^1_{M_0/M} → 0
```

it follows that

```text
  d(L_0/M_0, M/N) = rg_{L_0} Ω^1_{L_0/M} − rg_{L_0} Ω^1_{L_0/N} − rg_{M_0} Ω^1_{M_0/M} + rg_{M_0} Ω^1_{M_0/N}.
```

Now, one has $N(L^{p}_{0}) \supset M$, hence $\Omega^{1}_{L_{0}/M} = \Omega^{1}_{L_{0}/N}$ `(21.1.5, (ii))`. On the
other hand, the $T_{i}$ ($1 \leq i \leq r$) form a $p$-basis of $M$ over $N$, and a $p$-basis of `K_0` over $k$ is also
a $p$-basis of `M_0` over $M$, hence, as $M^{p}_{0} \subset N$,

```text
  rg_{M_0} Ω^1_{M_0/N} = r + rg_{M_0} Ω^1_{M_0/M} = r + rg_K Ω^1_{K/M}
```

by virtue of `(21.4.5)` and `(21.1.10)`, which proves `(21.9.6.5)`.

One again has, by `(21.6.4.2)`,

```text
  d(E/L_0, M) = d(E/L_0, k_0) + d(E/L_0, M/k_0)
```

and

```text
  d(L_0/M_0, N) = d(L_0/M_0, N/k) + d(L_0/M_0, k).
```

But as `L_0` is separable over `K_0` `(21.9.6.4)`, one has $d(L_{0}/K_{0}, k) = 0$, and consequently also
$d(L_{0}/M_{0}, k) = 0$ (`(21.6.2)` and `(21.6.4)`). One therefore obtains

```text
  δ = d(E/L_0, M/k_0) + d(L_0/M_0, N/k).
```

Let us apply `(21.6.4.2)` twice more to the first term of the second side of this formula; one obtains

```text
  d(E/L_0, M/k_0) = d(E/L_0, M/N) + d(E/L_0, N/k) + d(E/L_0, k/k_0).
```

As $M \subset N(L^{p}_{0})$, one has $d(E/L_{0}, M/N) = 0$ `(21.6.2)`, hence (by `(21.6.4.4)`)

```text
  δ = d(E/L_0, k/k_0) + d(E/M_0, N/k).
```

But `M_0` and `L_0` are separable extensions of `K_0` `(21.9.6.4)`, hence $d(L_{0}/K_{0}, k/k_{0}) = d(M_{0}/K_{0},
k/k_{0}) = 0$ `(21.6.2)`, and applying twice more `(21.6.4.4)`,

<!-- original page 276 -->

one has $d(E/L_{0}, k/k_{0}) = d(E/K_{0}, k/k_{0}) = d(E/M_{0}, k/k_{0})$, whence, by a last application of
`(21.6.4.2)`,

$$ \delta = d(E/M_{0}, N/k_{0}) $$

which proves `(21.9.6.1)`. Moreover, when $k$ is replaced by a sub-extension $k'$ of $k_{0}$, $N$ is replaced by a
sub-extension $N'$, hence $d(E/M_{0}, N'/k_{0}) \leq d(E/M_{0}, N/k_{0})$ `(21.6.4.2)`, which proves the last assertion
of (i).

(ii) For every $\alpha$, set $N_{\alpha} = k_{\alpha}((T^{p}_{1}, \cdots, T^{p}_{r}))$. By virtue of `(21.9.6.1)` and of
`(21.8.3)`, it amounts to showing (taking account of the fact that $K^{p}_{0} \subset k_{\alpha}$ and that $E$ is an
extension of finite type of `M_0`) that one has

$$ \bigcap_{\alpha} N_{\alpha} = k_{0}(M^{p}_{0}). $$

Now, one has

```text
  ⋂_α N_α = N' = (k_0(K_0^p))((T_1^p, …, T_r^p))                                      (21.9.6.6)
```

by virtue of `(21.8.8.3)` and of the relation $\bigcap_{\alpha} k_{\alpha} = k_{0}(K^{p}_{0})$ `(21.8.6)`. On the other
hand, one has $k_{0}(M^{p}_{0}) = k_{0}(K_{0}((T^{p}_{1}, \cdots, T^{p}_{r})))$. To finish the proof of
`(21.9.6, (ii))`, it therefore remains to prove the

**Lemma (21.9.6.7).**

<!-- label: 0_IV.21.9.6.7 -->

*Let $k_{0}$ be a field of characteristic $p > 0$ such that $[k_{0} : k^{p}_{0}] < +\infty$, `K_0` an extension of
$k_{0}$. Then one has*

```text
  (k_0(K_0^p))((T_1, …, T_r)) = k_0(K_0((T_1, …, T_r))).                              (21.9.6.8)
```

As $k_{0} \subset K_{0}$, one has $k_{0}(K_{0}((T_{1}, \cdots, T_{r}))) = K_{0}((T_{1}, \cdots, T_{r}))$. If $(x_{i})_{i
\in I}$ is a basis of $k_{0}$ over $k^{p}_{0}$, it is immediate that $(x_{i})$ is also a system of generators of each of
the two sides of `(21.9.6.8)` over $K^{p}_{0}((T_{1}, \cdots, T_{r}))$.

**Remark (21.9.7).**

<!-- label: 0_IV.21.9.7 -->

*The assertion of `(21.9.6, (ii))` does not extend to the case where $[k_{0} : k^{p}_{0}]$ is infinite. Take in fact for
$k_{0}$ the field $\mathbb{F}_{p}(X_{n})_{n \geq 0}$ of rational fractions in infinitely many indeterminates, so that
the $X_{n}$ form a $p$-basis of $k_{0}$ over $\mathbb{F}_{p}$, and consequently $[k_{0} : k^{p}_{0}] = +\infty$. In the
statement of `(21.9.6)`, take $K_{0} = k_{0}$ (hence necessarily $k = k_{0}$), $L_{0} = k_{0}((T))$, for $E$ the
extension $L_{0}(y)$, where $y$ is a root of the polynomial $Y^{p} - \sum^{\infty}_{n=0} X_{n} T^{n}$ of $L_{0}[Y]$.
Then the difference $\delta$ of the two sides of `(21.9.6.2)` is non zero. In fact, $E$ is separable over $k_{0}$,
otherwise $y$ would be an element of $k_{0}(L^{p}_{0})$, and one sees at once that this is not possible (due to the fact
that there are infinitely many $X_{n}$ algebraically independent); one therefore has $d(E/K_{0}, k_{0}) = 0$, formula
`(21.9.6.3)` reduces to $\delta = d(E/M_{0}, M_{0}) - 1$, and it is clear that $d(E/M_{0}, M_{0}) = rg_{E}
\Upsilon_{E/M_{0}}$. Everything comes down to verifying that this rank is `2`. Now one has $E^{p} \subset M_{0}$, a
$p$-basis of $E$ over `L_0` is formed by the single element $y$, and `L_0` evidently has a $p$-basis over `M_0` formed
by the single element $T$; hence, since $E$ is an algebraic extension of `M_0`, our assertion follows from `(21.7.1)`
and `(21.4.5)`.*

**Proposition (21.9.8).**

<!-- label: 0_IV.21.9.8 -->

*Let $k_{0}$ be a field (of any characteristic), `K_0` a separable extension of $k_{0}$, $A$ a complete Noetherian local
ring, which is a $k_{0}$-algebra and whose residue field*

<!-- original page 277 -->

*is a finite extension of `K_0`. For every prime ideal $\mathfrak{p}$ of $A$, let $k(\mathfrak{p})$ be the residue field
of $A$ at $\mathfrak{p}$. Then, for every field $k$ such that $k_{0} \subset k \subset K_{0}$ and such that $[K_{0} : k]
< +\infty$, one has*

```text
  rg_{k(𝔭)}(Ω̂^1_{A/k} ⊗_A k(𝔭)) − rg_{K_0} Ω^1_{K_0/k} ≥ dim(A/𝔭) + r + d(k(𝔭)/K_0, k_0).   (21.9.8.1)
```

*Suppose moreover that $[k_{0} : k^{p}_{0}] < +\infty$ (where $p$ is the characteristic exponent of $k_{0}$). Then one
can find a field $k$ such that $k_{0}(K^{p}_{0}) \subset k \subset K_{0}$ and $[K_{0} : k] < +\infty$, for which the two
sides of `(21.9.8.1)` are equal.*

Since $A/\mathfrak{p}$ has the same residue field $K$ as $A$ and is complete, one can restrict to the case where $A$ is
integral and $\mathfrak{p} = 0$; one will then set $E = k(\mathfrak{p})$, the field of fractions of $A$. As `K_0` is
formally smooth over $k_{0}$ `(19.6.1)`, there exists a $k_{0}$-monomorphism $K_{0} \to A$ making $A$ a `K_0`-algebra;
one knows moreover that there exists a sub-`K_0`-algebra `A_0` of $A$, `K_0`-isomorphic to a formal power series algebra
$K_{0}[[T_{1}, \cdots, T_{r}]]$ and such that $A$ be a finite `A_0`-algebra `(19.8.9)`, which entails that $E$ is a
finite extension of the field of fractions $L_{0} = K_{0}((T_{1}, \cdots, T_{r}))$ of `A_0`. One has then
$\Upsilon_{K_{0}/k} = 0$ since `K_0` is separable over $k_{0}$, and $deg.tr_{K_{0}} E = 0$; moreover, since $A$ is a
finite `A_0`-algebra, one has $\dim(A) = \dim(A_{0})$ `(16.1.5)`.

If $p = 1$, one has $rg_{E}(\hat{\Omega}^{1}_{A/k} \otimes_{A} E) = r$ by `(21.9.5)` and `(17.1.4, (iii))`, and
$\Upsilon_{L_{0}/K_{0}} = 0$ since `K_0` is a finite separable extension of $k$ `(21.7.4)`; on the other hand
$\Omega^{1}_{K_{0}/k} = 0$, $E$ being a separable extension of $k_{0}$; the two sides of `(21.9.8.1)` are therefore
equal in this case.

Suppose now that $p > 1$; if $B = k[[T_{1}, \cdots, T_{r}]]$, $A$ is a $B$-algebra of finite type, hence, setting $B_{1}
= k[[T^{p}_{1}, \cdots, T^{p}_{r}]]$, $\hat{\Omega}^{1}_{A/B}$ is identified with $\hat{\Omega}^{1}_{A/B_{1}}$
`(21.9.4)`, and denoting by $M$ the field of fractions $k((T^{p}_{1}, \cdots, T^{p}_{r}))$, it follows from `(20.5.9)`
that $\hat{\Omega}^{1}_{A/B} \otimes_{A} E$ is identified with $\Omega^{1}_{E/M}$; the inequality `(21.9.8.1)` is then
nothing but `(21.9.6.2)`, and the last assertion of the corollary follows from `(21.9.6, (ii))`.
