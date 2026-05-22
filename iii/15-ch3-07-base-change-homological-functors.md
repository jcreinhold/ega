# §7. Study of base change in the covariant homological functors of modules

<!-- original page 175 -->

## 7.1. Functors of $A$-modules

**7.1.1.**

<!-- label: III.7.1.1 -->

Given a ring $A$ (not necessarily commutative), we shall denote by $Ab_{A}$ the category of left $A$-modules, and shall
denote simply by `Ab` the category of $Z$-modules, identical with commutative groups. Let $T : Ab_{A} \to Ab$ be a
*covariant additive functor*, and let $M$ be an $(A, A)$-bimodule; $T(M)$ is then naturally equipped with a structure of
right $A$-module. Indeed, for every $a \in A$, let us denote by $h_{a, M}$ (or simply $h_{a}$) the endomorphism $x
\mapsto xa$ of the left $A$-module $M$. By hypothesis, $T(h_{a})$ is an endomorphism of the $Z$-module $T(M)$; moreover,
since $T$ is a covariant additive functor, we have, for $a \in A$, $b \in A$,

```text
  T(h_{ab}) = T(h_b ∘ h_a) = T(h_b) ∘ T(h_a)   and   T(h_{a+b}) = T(h_a + h_b) = T(h_a) + T(h_b);
```

this proves that the map $(a, y) \mapsto T(h_{a})(y)$ is an external composition law of right $A$-module on $T(M)$. In
particular, $T(A_{s})$ is a right $A$-module.

**7.1.2.**

<!-- label: III.7.1.2 -->

When $A$ is a commutative ring, it follows from `(7.1.1)` that for every $A$-module $M$, $T(M)$ is naturally equipped
with a structure of $A$-module; moreover, if $u : M \to N$ is a homomorphism of $A$-modules, we have, for every $a \in
A$, $u \circ h_{a, M} = h_{a, N} \circ u$, whence $T(u) \circ T(h_{a, M}) = T(h_{a, N}) \circ T(u)$, which proves that
$T(u) : T(M) \to T(N)$ is a homomorphism of $A$-modules; we thus see that $T$ can be considered as a covariant additive
functor from the category $Ab_{A}$ into itself. More precisely, we have thereby defined a canonical equivalence between
the category of covariant additive functors $Ab_{A} \to Ab$ and the category of covariant $A$-*linear* functors $T :
Ab_{A} \to Ab_{A}$, that is, those such that $T(h_{a, M}) = h_{a, T(M)}$ for every $a \in A$. Since the inclusion
functor $I : Ab_{A} \to Ab$, sending each $A$-module to its underlying $Z$-module, is exact and faithful, the exactness
properties of the two functors associated by the preceding equivalence are the same.

**7.1.3.**

<!-- label: III.7.1.3 -->

The ring $A$ still being assumed commutative, let $B$ be an $A$-*algebra* (not necessarily commutative), and let $\rho :
A \to B$ be the ring homomorphism corresponding to this algebra structure; this homomorphism defines a covariant

<!-- original page 176 -->

additive functor $\rho_{*} : M \mapsto M_{[\rho]}$ from the category $Ab_{B}$ of left $B$-modules into the category
$Ab_{A}$ of $A$-modules. By composition, we deduce a functor $T_{(B)} : Ab_{B} \to^{\rho_{*}} Ab_{A} \to^{T} Ab$,
evidently covariant and additive, which we shall also denote by $T^{(B)}$ (for typographical reasons) or $T \otimes_{A}
B$, and which we shall say is *obtained from* $T$ *by extension of scalars from* $A$ *to* $B$. Of course, if $B$ is
commutative, one can consider $T_{(B)}$ as a functor from $Ab_{B}$ into itself `(7.1.2)`. When $B$ is commutative and
$C$ a $B$-algebra, one sees at once that $T_{(C)} = (T_{(B)})_{(C)}$; it is immediate that the extension of scalars is
*functorial* and *additive* in $T$; moreover, when $T$ commutes with inductive limits or with direct sums (resp. is left
exact, right exact, exact), the same is true of $T_{(B)}$: indeed, $\rho_{*}$ is exact and commutes with inductive
limits and direct sums.

**7.1.4.**

<!-- label: III.7.1.4 -->

Suppose still that $A$ is commutative, and let $T$ be an $A$-linear covariant additive functor $Ab_{A} \to Ab_{A}$,
*commuting with inductive limits*. Then, for every multiplicative subset $S$ of $A$ and every $A$-module $M$, we have a
canonical functorial isomorphism of $A$-modules

```text
  T(S⁻¹ M) ⥲ S⁻¹ T(M).                                                       (7.1.4.1)
```

Suppose first that $S$ is the set of powers $f^{n}$ ($n \geq 0$) of an element $f \in A$. We know then that $M_{f} =
\lim\to M_{n}$, where $(M_{n}, \phi_{nm})$ is the inductive system of $A$-modules $M_{n} = M$, with $\phi_{nm} : z
\mapsto f^{n-m} z$ $(0_{I}, 1.6.1)$; whence in this case the isomorphism `(7.1.4.1)` by virtue of the hypothesis on $T$.
If next $S$ is arbitrary, $S^{-1} M$ is the inductive limit of the $M_{f}$ for $f \in S$ $(0_{I}, 1.4.5)$, and one
concludes in the same way. Moreover, the functoriality of the isomorphism `(7.1.4.1)` shows that it is an isomorphism of
$S^{-1} A$-modules, and that one can therefore write, up to a canonical isomorphism,

```text
  T_{(S⁻¹ A)}(S⁻¹ M) = S⁻¹ T(M) = T(S⁻¹ M).                                   (7.1.4.2)
```

When $S = A - \mathfrak{p}$ is the complement of a prime ideal $\mathfrak{p}$ of $A$, one writes $T_{\mathfrak{p}}$
instead of $T_{(A_{\mathfrak{p}})}$.

**Proposition (7.1.5).**

<!-- label: III.7.1.5 -->

*Under the hypotheses of `(7.1.4)`, if $T_{\mathfrak{m}}$ is left exact (resp. right exact, exact) for every maximal
ideal $\mathfrak{m}$ of $A$, then $T$ is left exact (resp. right exact, exact).*

**Proof.** We know in fact that when two submodules $N$, $P$ of an $A$-module $M$ are such that $N_{\mathfrak{m}} =
P_{\mathfrak{m}}$ for every maximal ideal $\mathfrak{m}$ of $A$, then $N = P$ (Bourbaki, *Alg. comm.*, chap. II, § 3, n°
3, th. 1).

## 7.2. Characterizations of the tensor product functor

**7.2.1.**

<!-- label: III.7.2.1 -->

Let $A$ be a ring (not necessarily commutative), $M$ (resp. $N$) a left (resp. right) $A$-module, $P$ a $Z$-module.
Recall that giving a $Z$-homomorphism $v : N \otimes_{A} M \to P$ is equivalent to giving a $Z$-bilinear map $u : N
\times M \to P$ such that $u(ta, x) = u(t, ax)$ for $a \in A$, $t \in N$, $x \in M$, the two maps being related by $v(t
\otimes x) = u(t, x)$. On the other hand, giving $u$ is equivalent to giving a

<!-- original page 177 -->

$Z$-homomorphism $x \mapsto f_{x}$ of $M$ into $\operatorname{Hom}_{Z}(N, P)$ such that $f_{ax}(t) = f_{x}(ta)$ for $a
\in A$, $t \in N$, $x \in M$, the two maps being related by $u(t, x) = f_{x}(t)$.

**7.2.2.**

<!-- label: III.7.2.2 -->

Let $T : Ab_{A} \to Ab$ be a covariant additive functor. We are going to define, for every left $A$-module $M$, a
*canonical homomorphism functorial in* $M$, of $Z$-modules

```text
  t_M : T(A_s) ⊗_A M → T(M).                                                 (7.2.2.1)
```

It will suffice for this, by virtue of `(7.2.1)`, to define a $Z$-homomorphism $x \mapsto t'_{M}(x)$ of $M$ into
$\operatorname{Hom}_{Z}(T(A_{s}), T(M))$, such that $t'_{M}(ax)(y) = t'_{M}(x)(ya)$ for $a \in A$, $x \in M$ and $y \in
T(A_{s})$. Note for this that $\operatorname{Hom}_{Z}(T(A_{s}), T(M))$ is canonically equipped with a left $A$-module
structure coming from the right $A$-module structure of $T(A_{s})$, the external law being such that if $a \in A$, $v
\in \operatorname{Hom}_{Z}(T(A_{s}), T(M))$, then $(a \cdot v)(y) = v(ya)$ for $y \in T(A_{s})$. This being so, we
define $t'_{M}$ as the composite of the two canonical homomorphisms

```text
  M ⥲ Hom_A(A_s, M) →^T Hom_Z(T(A_s), T(M)),
```

the second arrow being the map $u \mapsto T(u)$, the first the canonical isomorphism of $A$-modules $x \mapsto
\theta_{x}$ such that $\theta_{x}(\xi) = \xi x$ for $\xi \in A$, $x \in M$. One has $\theta_{ax} = \theta_{x} \circ
h_{a}$, hence $T(\theta_{ax}) = T(\theta_{x} \circ h_{a}) = T(\theta_{x}) \circ T(h_{a})$, and consequently, for $y \in
T(A_{s})$,

$$ T(\theta_{ax})(y) = T(\theta_{x})(T(h_{a})(y)) = T(\theta_{x})(ya) $$

by definition of the external law on $T(A_{s})$, which proves the existence of $t_{M}$; it is immediate to verify that
this homomorphism is functorial in $M$, that is, that for every homomorphism $w : M \to M'$ of left $A$-modules, the
diagram

```text
                       t_M
  T(A_s) ⊗_A M  ─────────────→  T(M)
        │                        │
   1 ⊗ w│                        │T(w)                                       (7.2.2.2)
        ↓                        ↓
  T(A_s) ⊗_A M' ─────────────→  T(M')
                      t_{M'}
```

is commutative.

The functoriality of the homomorphism `(7.2.2.1)` shows that when $A$ is commutative, it is a homomorphism of
$A$-modules (cf. `(7.1.2)`).

**7.2.3.**

<!-- label: III.7.2.3 -->

When $A$ is commutative, one can more generally define a canonical homomorphism of $A$-modules

```text
  T(N) ⊗_A M → T(N ⊗_A M)                                                    (7.2.3.1)
```

for every $A$-module $N$; it suffices in the construction of `(7.2.2)` to replace the homomorphism $\theta_{x}$ by the
homomorphism of $A$-modules $N \to N \otimes_{A} M$ sending each $y \in N$ to $y \otimes x$. It is immediate that this
homomorphism is functorial in $M$ and $N$.

<!-- original page 178 -->

In particular, if $B$ is an $A$-algebra (not necessarily commutative), one has a homomorphism functorial in $M$

```text
  (T(M))_{(B)} = T(M) ⊗_A B → T(M ⊗_A B) = T_{(B)}(M_{(B)})                  (7.2.3.2)
```

which, by virtue of the functoriality of `(7.2.3.1)` in $M$, is a homomorphism of $B$-modules.

One has moreover the commutative diagram

```text
                       t_M
   T(A) ⊗_A M  ───────────────→  T(M)
        │                         │
        │                         │                                          (7.2.3.3)
        ↓                         ↓
   T_{(B)}(B_s) ⊗_B M_{(B)} ───→ T_{(B)}(M_{(B)})
                       t_{M_{(B)}}
```

where the right vertical arrow is the composite homomorphism

```text
  T(M) → T(M) ⊗_A B → T(M ⊗_A B) = T_{(B)}(M_{(B)})
```

of `(7.2.3.2)` and the canonical homomorphism; as for the left vertical arrow of `(7.2.3.3)`, it is the homomorphism
$T(A) \otimes_{A} M \to T_{(B)}(B_{s}) \otimes_{B} (B \otimes_{A} M) = T_{(B)}(B_{s}) \otimes_{A} M$, where $T(A) \to
T_{(B)}(B_{s}) = T(B)$ is $T(\rho)$, $\rho$ being considered as a homomorphism of $A$-modules $A \to B_{[\rho]}$.

**Lemma (7.2.4).**

<!-- label: III.7.2.4 -->

*If $T$ is a covariant additive functor from $Ab_{A}$ into `Ab`, commuting with direct sums, the canonical homomorphism
$t_{L}$ `(7.2.2.1)` is an isomorphism for every free $A$-module $L$.*

**Proof.** Indeed, one has $L = \oplus_{\alpha \in I} L_{\alpha}$ where $L_{\alpha}$ is isomorphic to $A_{s}$ for every
$\alpha \in I$; the definition of $t_{M}$ given in `(7.2.2)` shows that $t_{L} = \oplus_{\alpha \in I} t_{L_{\alpha}}$,
since

```text
  T : Hom_A(A_s, L) → Hom_Z(T(A_s), T(L))
```

is the direct sum of the $Z$-linear maps $T_{\alpha} : \operatorname{Hom}_{A}(A_{s}, L_{\alpha}) \to
\operatorname{Hom}_{Z}(T(A_{s}), T(L_{\alpha}))$ by virtue of the hypothesis on $T$. We are thus reduced to proving the
lemma for $L = A_{s}$; but $t_{L}$ is then none other than the canonical isomorphism $T(A_{s}) \otimes_{A} A_{s}
\xrightarrow{\sim} T(A_{s})$ valid for every right $A$-module.

**Proposition (7.2.5).**

<!-- label: III.7.2.5 -->

*Let $T$ be a covariant additive functor from $Ab_{A}$ into `Ab`, commuting with direct sums. The following conditions
are equivalent:*

- *a) $T$ is right exact.*
- *b) The canonical homomorphism $t_{M}$ `(7.2.2.1)` is an isomorphism for every left $A$-module $M$.*
- *b') $T$ is semi-exact and the homomorphism $t_{M}$ is surjective for every left $A$-module $M$.*
- *c) $T$ is isomorphic to a functor in $M$ of the form $N \otimes_{A} M$, where $N$ is a right $A$-module.*

**Proof.** It is clear that b) implies c) and that c) implies a); let us show that a) implies b).

<!-- original page 179 -->

Set $T'(M) = T(A_{s}) \otimes_{A} M$ for every left $A$-module $M$. There exists an exact sequence $L' \to L \to M \to
0$, where $L$ and $L'$ are two free left $A$-modules; since $T$ and $T'$ are right exact, we have the commutative
diagram

```text
  T'(L') → T'(L) → T'(M) → 0
    │        │       │
    │t_{L'}  │t_L    │t_M
    ↓        ↓       ↓
  T(L')  →  T(L)  →  T(M)  → 0
```

where the two rows are exact; since $t_{L}$ and $t_{L'}$ are isomorphisms by virtue of `(7.2.4)`, the same is true of
$t_{M}$ by the five lemma. Finally, it is clear that b) implies b'). To show that b') implies a), it suffices to prove

**Lemma (7.2.5.1).**

<!-- label: III.7.2.5.1 -->

*Let $\mathcal{K}$, $\mathcal{K}'$ be two abelian categories, $F$, $G$ two covariant additive functors from
$\mathcal{K}$ into $\mathcal{K}'$, $f : F \to G$ a functorial morphism `(T, I, 1.2)` such that, for every object $E$ of
the category $\mathcal{K}$, $f_{E} : F(E) \to G(E)$ is an epimorphism. Then, if $F$ is right exact and $G$ semi-exact,
$G$ is right exact.*

**Proof.** It all comes down to showing that for every epimorphism $v : E' \to E$ in $\mathcal{K}$, $G(v) : G(E') \to
G(E)$ is an epimorphism; one has the commutative diagram

```text
            F(v)
  F(E') ─────────→  F(E)
   │                 │
   │f_{E'}           │f_E
   ↓                 ↓
  G(E') ─────────→  G(E)
            G(v)
```

in which $F(v)$, $f_{E'}$ and $f_{E}$ are epimorphisms; hence so is $G(v)$.

**Remark (7.2.6).**

<!-- label: III.7.2.6 -->

For every right $A$-module $N$, set $T_{N}(M) = N \otimes_{A} M$ for every left $A$-module $M$, so that `T_N` is a
covariant additive functor from $Ab_{A}$ into `Ab`, right exact and commuting with direct sums. If one canonically
identifies $T_{N}(A_{s})$ with $N$, one verifies at once that the corresponding homomorphism `(7.2.2.1)` becomes the
identity. One concludes that the right $A$-module $N$ in the statement of `(7.2.5, c))` is determined up to unique
isomorphism and is canonically isomorphic to $T(A_{s})$. One can also say that the functorial morphisms $T
\rightsquigarrow T(A_{s})$ and $N \rightsquigarrow T_{N}$ constitute an equivalence `(T, I, 1.2)` of the category of
right $A$-modules and the category of covariant additive functors $Ab_{A} \to Ab$ that are right exact and commute with
direct sums.

**Proposition (7.2.7).**

<!-- label: III.7.2.7 -->

*Let $A$ be a left artinian ring whose quotient by its radical $\mathfrak{m}$ is a field $k$. Let $T$ be a covariant
additive functor from $Ab_{A}$ into `Ab`, commuting with direct sums. The conditions of `(7.2.5)` are then also
equivalent to*

- *d) $T$ is semi-exact and the homomorphism $T(\epsilon) : T(A_{s}) \to T(k)$ deduced from the canonical homomorphism
  $\epsilon : A_{s} \to k$ is surjective.*

<!-- original page 180 -->

**Proof.** It is clear that condition b') of `(7.2.5)` implies d); let us prove that d) implies b'). There exists an
integer $n$ such that $\mathfrak{m}^{n} = 0$; set, for every $A$-module $M$, $M_{h} = \mathfrak{m}^{h} M$; we shall
prove by descending induction on $h$ that $t_{M_{h}}$ is surjective. The proposition is evident for $h = n$; for $h <
n$, one has an exact sequence

```text
  0 → M_{h+1} → M_h → M_h / M_{h+1} → 0
```

and the induction hypothesis implies that $t_{M_{h+1}}$ is surjective. On the other hand, $M_{h} / M_{h+1}$ is
annihilated by $\mathfrak{m}$ and is therefore an $(A/\mathfrak{m})$-module, in other words a direct sum of $A$-modules
isomorphic to $k$. To prove that $t_{M_{h} / M_{h+1}}$ is surjective, it suffices therefore to prove that $t_{k}$ is,
since $T$ commutes with direct sums. Now, by virtue of the commutativity of the diagram

```text
                    t_{A_s}
  T(A_s) ⊗_A A_s ───────────→  T(A_s)
        │                        │
   1 ⊗ ε│                        │T(ε)
        ↓                        ↓
  T(A_s) ⊗_A k  ───────────→  T(k)
                     t_k
```

and of `(7.2.4)`, hypothesis d) implies that $t_{k}$ is indeed surjective. To finish the proof, it will suffice to show
that if one has an exact sequence $0 \to M' \to^{u} M \to^{v} M'' \to 0$ of $A$-modules, such that $t_{M'}$ and
$t_{M''}$ are surjective, then $t_{M}$ is surjective. Now, one has a commutative diagram

```text
  T'(M') ────→ T'(M)  ────→ T'(M'') ────→ 0
    │           │            │
    │t_{M'}     │t_M         │t_{M''}
    ↓           ↓            ↓
  T(M')  ────→ T(M)   ────→ T(M'')  ────→ Coker(T(v))
                      T(v)
```

in which the two rows are exact, by virtue of the hypothesis that $T$ is semi-exact. Since by the induction hypothesis
$t_{M'}$ and $t_{M''}$ are epimorphisms and the last vertical arrow is a monomorphism, the five lemma `(M, I, 1.1)`
shows that $t_{M}$ is an epimorphism.

## 7.3. Exactness criteria for the homological functors of modules

**Proposition (7.3.1).**

<!-- label: III.7.3.1 -->

*Let $A$ be a ring (not necessarily commutative), $T_{\bullet}$ a covariant homological functor `(T, II, 2.1)` from the
category $Ab_{A}$ into the category `Ab`, commuting with direct sums. Let $p$ be an integer such that $T_{p}$ and
$T_{p-1}$ are defined. The following conditions are equivalent:*

- *a) $T_{p}$ is right exact.*
- *b) $T_{p-1}$ is left exact.*

<!-- original page 181 -->

- *c) For every left $A$-module $M$, the canonical functorial homomorphism `(7.2.2.1)`*
    ```text
      T_p(A_s) ⊗_A M → T_p(M)                                                (7.3.1.1)
    ```
    *is an isomorphism.*
- *d) For every left $A$-module $M$, the homomorphism `(7.3.1.1)` is an epimorphism.*
- *e) $T_{p}$ is isomorphic to a functor $M \mapsto N \otimes_{A} M$, where $N$ is a right $A$-module.*

*If moreover the conditions of `(7.2.7)` on $A$ and $\mathfrak{m}$ are satisfied, the preceding conditions are also
equivalent to*

- *f) The canonical homomorphism $T_{p}(\epsilon) : T_{p}(A_{s}) \to T_{p}(k)$ is an epimorphism.*

**Proof.** Since by definition of a homological functor, $T_{i}$ is semi-exact for every $i$ such that $T_{i}$ is
defined, and since for every exact sequence $0 \to M' \to^{u} M \to^{v} M'' \to 0$ one has $Ker(T_{i-1}(u)) =
Coker(T_{i}(v))$, it is clear that a) and b) are equivalent and the other assertions follow trivially from `(7.2.5)` and
`(7.2.7)`.

**Corollary (7.3.2).**

<!-- label: III.7.3.2 -->

*Let $A$ be a commutative ring. With the notations of `(7.3.1)`, suppose $T_{p}$ is right exact. If $f \in A$ does not
belong to the annihilator of any element $\neq 0$ of an $A$-module $M$, then $f$ does not belong to the annihilator of
any element $\neq 0$ of $T_{p-1}(M)$. In particular, if $A$ is an integral domain, the $A$-module $T_{p-1}(A)$ is
torsion-free.*

**Proof.** Indeed, if $h_{f}$ denotes the homothety $x \mapsto fx$ of $M$, the hypothesis means that $h_{f}$ is
injective; hence so is $T_{p-1}(h_{f})$ by condition b) of `(7.3.1)`.

**Proposition (7.3.3).**

<!-- label: III.7.3.3 -->

*Let $A$ be a ring, $T_{\bullet}$ a covariant homological functor from $Ab_{A}$ into `Ab`, commuting with direct sums.
Let $p$ be an integer such that $T_{p-1}$, $T_{p}$ and $T_{p+1}$ are defined. The following conditions are equivalent:*

- *a) $T_{p}$ is exact.*
- *b) $T_{p+1}$ and $T_{p}$ are right exact.*
- *c) $T_{p}$ and $T_{p-1}$ are left exact.*
- *d) $T_{p+1}$ is right exact and $T_{p-1}$ is left exact.*
- *e) For every $A$-module $M$, the canonical homomorphisms*
    ```text
      T_i(A_s) ⊗_A M → T_i(M)                                                (7.3.3.1)
    ```
    *are isomorphisms for $i = p$ and $i = p + 1$.*
- *e') For every $A$-module $M$, the canonical homomorphisms `(7.3.3.1)` are epimorphisms for $i = p$ and $i = p + 1$.*
- *f) For every $A$-module $M$, the homomorphism `(7.3.3.1)` is an isomorphism for $i = p$ and $T_{p}(A_{s})$ is a flat
  right $A$-module.*
- *f') For every $A$-module $M$, the homomorphism `(7.3.3.1)` is an epimorphism for $i = p$ and $T_{p}(A_{s})$ is a flat
  right $A$-module.*

**Proof.** The equivalence of conditions a), b), c), d) results from the equivalence of conditions a) and b) of
`(7.3.1)`. The equivalence of b), e) and e') results from the equivalence of a), c) and d) in `(7.3.1)`. Finally, to say
that $T_{p}(A_{s})$ is flat means that the functor $M \mapsto T_{p}(A_{s}) \otimes_{A} M$ is left exact; the equivalence
of a), f) and f') again results from the equivalence of a), c), d) in `(7.3.1)`.

<!-- original page 182 -->

**Corollary (7.3.4).**

<!-- label: III.7.3.4 -->

*Suppose $A$ commutative, $T_{p}$ exact, and suppose moreover that $T_{p}(A)$ is an $A$-module of finite presentation.
Then the function $x \mapsto rang_{\kappa(x)}(T_{p}(\kappa(x)))$ is locally constant on $X = \operatorname{Spec}(A)$,
hence constant if $\operatorname{Spec}(A)$ is connected.*

**Proof.** Indeed, since $T_{p}(A)$ is a flat $A$-module by virtue of `(7.3.3, f))`, it is projective of finite type,
and $(T_{p}(A))^{\sim}$ is therefore a locally free $\mathcal{O}_{X}$-module (Bourbaki, *Alg. comm.*, chap. II, § 5, n°
2, th. 1); one has moreover $T_{p}(\kappa(x)) = T_{p}(A) \otimes_{A} \kappa(x)$ `(7.3.3, e))` and we know that the rank
at the point $x$ of the $A$-module $T_{p}(A)$ is locally constant (*loc. cit.*), whence the corollary.

**Proposition (7.3.5).**

<!-- label: III.7.3.5 -->

*Suppose that $A$ is a left artinian ring whose quotient by its radical $\mathfrak{m}$ is a field $k$. Then the
conditions of `(7.3.3)` are also equivalent to each of the following:*

- *g) The canonical homomorphism $T_{i}(\epsilon) : T_{i}(A_{s}) \to T_{i}(k)$ is an epimorphism for $i = p$ and
  $i = p + 1$.*
- *h) $T_{p}(\epsilon)$ is an epimorphism and $T_{p}(A_{s})$ is a flat right $A$-module (or, what amounts to the same
  (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5) a free $A$-module).*

*Suppose moreover that $A$ is commutative and the $A$-module $T_{p}(k)$ of finite length $d$. Then the preceding
conditions are also equivalent to each of the following:*

- *i) For every $A$-module $M$ of finite length, one has*
    ```text
      long(T_p(M)) = d · long(M).                                            (7.3.5.1)
    ```
- *j) One has*
    ```text
      long(T_p(A)) = d · long(A).                                            (7.3.5.2)
    ```

**Proof.** The equivalence of g) and h) with the conditions of `(7.3.3)` follows immediately from `(7.2.7)`. To prove
the other assertions, we shall use the following lemma:

**Lemma (7.3.5.3).**

<!-- label: III.7.3.5.3 -->

*Let $\mathcal{K}$, $\mathcal{K}'$ be two abelian categories, $F : \mathcal{K} \to \mathcal{K}'$ a covariant additive
functor; suppose that $F$ is semi-exact, and that, for every simple object $S$ of $\mathcal{K}$, $F(S)$ is an object of
finite length in $\mathcal{K}'$. Then, for every object $E$ of finite length in $\mathcal{K}$, $F(E)$ is of finite
length in $\mathcal{K}'$. For every exact sequence $0 \to E' \to^{u} E \to^{v} E'' \to 0$ of objects of finite length in
$\mathcal{K}$, one has*

```text
  long F(E) ≤ long F(E') + long F(E'')                                       (7.3.5.4)
```

*and for the two members of `(7.3.5.4)` to be equal, it is necessary and sufficient that the sequence*

$$ 0 \to F(E') \to F(E) \to F(E'') \to 0 $$

*be exact.*

**Proof.** Indeed, the sequence $F(E') \to^{F(u)} F(E) \to^{F(v)} F(E'')$ is exact by hypothesis; if one supposes
$F(E')$ and $F(E'')$ of finite length, the same is true of $Im(F(u))$ and $Im(F(v))$, and since $Ker(F(v)) = Im(F(u))$,
$F(E)$ is of finite length and one has

```text
  long F(E) = long Im(F(u)) + long Im(F(v)) ≤ long F(E') + long F(E'').      (7.3.5.5)
```

<!-- original page 183 -->

By induction on the length of $E$, this already proves the first assertion; moreover, the two members of `(7.3.5.5)` can
be equal only if $long Im(F(u)) = long F(E')$ (which is equivalent to $long Ker(F(u)) = 0$, or $Ker(F(u)) = 0$) and
$long Im(F(v)) = long F(E'')$ (which is equivalent to $long Coker(F(v)) = 0$, or $Coker(F(v)) = 0$).

We now note that if $M$ is an $A$-module of finite length ($A$ being commutative), the quotients of a Jordan–Hölder
sequence of $M$ are necessarily isomorphic to the $A$-module $k$; therefore, by `(7.3.5.4)` and induction on the length
of $M$,

```text
  long T_p(M) ≤ d · long(M).                                                 (7.3.5.6)
```

Moreover, it follows from `(7.3.5.3)` that if $T_{p}$ is exact, one has the equality `(7.3.5.1)`; hence condition a) of
`(7.3.3)` implies i); it is clear that i) implies j), and it remains to prove

**Lemma (7.3.5.7).**

<!-- label: III.7.3.5.7 -->

*The relation $long T_{p}(A) = d \cdot long A$ implies that $T_{p}(\epsilon)$ is an epimorphism and that $T_{p}(A)$ is a
flat $A$-module.*

**Proof.** Indeed, starting from the exact sequence $0 \to \mathfrak{m} \to A \to k \to 0$, it follows from `(7.3.5.4)`
and `(7.3.5.6)` that one has

```text
  long T_p(A) ≤ long T_p(𝔪) + long T_p(k) ≤ d(long 𝔪 + long k) = d · long A
```

and that equality can hold `(7.3.5.3)` only if the sequence

$$ 0 \to T_{p}(\mathfrak{m}) \to T_{p}(A) \to T_{p}(k) \to 0 (7.3.5.8) $$

is exact. By virtue of `(7.2.7)` and `(7.2.5)`, $T_{p}$ is isomorphic to a functor $M \mapsto N \otimes_{A} M$, and the
exactness of the sequence `(7.3.5.8)` shows, by virtue of the exact sequence of Tor's, that one has $Tor^{A}_{1}(N, k) =
0$. One concludes that $N = T_{p}(A)$ is a flat $A$-module $(0_{I}, 10.1.3)$.

**Lemma (7.3.6).**

<!-- label: III.7.3.6 -->

*Let $A$ be a ring, $T_{\bullet}$ a covariant homological functor from $Ab_{A}$ into `Ab`, commuting with direct sums.
Suppose $T_{p}$ and $T_{p+1}$ defined, and $T_{p}$ left exact. For $T_{p+1}$ to be exact, it is necessary and sufficient
that $T_{p+1}(A_{s})$ be a flat right $A$-module.*

**Proof.** Indeed, one knows by `(7.3.1)` that the canonical homomorphism

```text
  T_{p+1}(A_s) ⊗_A M → T_{p+1}(M)
```

is an isomorphism of functors; it suffices to apply the definition of a flat $A$-module.

**Proposition (7.3.7).**

<!-- label: III.7.3.7 -->

*Let $A$ be a ring, $T_{\bullet}$ a covariant homological functor from $Ab_{A}$ into `Ab`, commuting with direct sums.
Suppose there exists $i_{0}$ such that $T_{i}$ is exact for $i \leq i_{0}$. Then, for every integer $p > i_{0}$, the
following conditions are equivalent:*

- *a) $T_{q}$ is exact for $q \leq p$;*
- *b) $T_{q}(A_{s})$ is a flat right $A$-module for $q \leq p$.*
- *c) For every $A$-module $M$, the canonical homomorphism $T_{q}(A_{s}) \otimes_{A} M \to T_{q}(M)$ is surjective for
  $q \leq p + 1$.*

**Proof.** The equivalence of a) and b) results from `(7.3.6)` by induction on $q$, since $T_{i_{0}}$ is exact by
hypothesis; the equivalence of a) and c) results from the equivalence of conditions a) and e') in `(7.3.3)`.

<!-- original page 184 -->

**7.3.8.**

<!-- label: III.7.3.8 -->

If $A$ is a commutative ring, $B$ an $A$-algebra (not necessarily commutative), $T_{\bullet}$ a covariant homological
functor from $Ab_{A}$ into `Ab`, it follows from the definitions `(7.1.3)` that the functor from $Ab_{B}$ into `Ab`
obtained by extension of scalars from $A$ to $B$, and which we shall denote $T^{(B)}_{\bullet} = (T_{\bullet})_{(B)}$,
is again a *homological* functor.

**Corollary (7.3.9).**

<!-- label: III.7.3.9 -->

*Suppose that $T_{\bullet}$ satisfies the general conditions of `(7.3.7)` and commutes with inductive limits, and
moreover that $A$ is an integral ring and all the $T_{n}(A)$ are $A$-modules of finite presentation. Then, for every
integer $N$, there exists $f \in A - {0}$ such that the functor $T^{(A_{f})}_{\bullet} : Ab_{A_{f}} \to Ab$ is exact for
$p \leq N$.*

**Proof.** By hypothesis, $T_{i}$ is exact for $i \leq i_{0}$, hence $T_{i}(A)$ is flat for these values of $i$. By
virtue of `(7.3.7, b))`, it suffices to take $f$ such that $T^{(A_{f})}_{p}(A_{f}) = T_{p}(A_{f})$ is a free
$A_{f}$-module for $i_{0} < p \leq N$. Now, one has $T_{p}(A_{f}) = (T_{p}(A))_{f}$ since $T_{p}$ commutes with
inductive limits `(7.1.4)`. If $x$ is the generic point of $\operatorname{Spec}(A)$, $(T_{p}(A))_{x}$ is a
finite-dimensional vector space over the fraction field of $A$. Since each $T_{p}(A)$ is of finite presentation, there
does indeed exist an $f$ with the desired property (Bourbaki, *Alg. comm.*, chap. II, § 5, n° 1, cor. of prop. 2).

One will note that if there are only finitely many indices $i$ such that $T_{i} \neq 0$, there exists $f \in A - {0}$
such that *all* the $T^{(A_{f})}_{p}$ are exact.

**Corollary (7.3.10).**

<!-- label: III.7.3.10 -->

*Suppose that $T_{\bullet}$ satisfies the general conditions of `(7.3.7)` and commutes with inductive limits, that $A$
is commutative and noetherian, and the $T_{n}(A)$ $A$-modules of finite type. Then, for every integer $N$, there exists
a dense open set $U$ of $\operatorname{Spec}(A)$ such that, for every $p \leq N$, the function $x \mapsto
rang_{\kappa(x)}(T_{p}(\kappa(x)))$ is constant on $U$.*

**Proof.** Let $\mathfrak{p}$ be a minimal prime ideal of $A$; by hypothesis, the ring $B = A/\mathfrak{p}$ is integral
and $\operatorname{Spec}(B)$ is identified with an irreducible component of the topological space
$\operatorname{Spec}(A)$. We shall show by induction on $p \leq N$ that there exists $f_{p} \in B - {0}$ such that, on
setting $B' = B_{f_{p}}$, $T^{(B')}_{i}$ is exact and the $T_{i}(B')$ are $B'$-modules of finite type for $i \leq p$.
The proposition is true for $p \leq i_{0}$ by virtue of the hypothesis, taking $f_{p} = 1$ (hence $B' = B =
A/\mathfrak{p}$): for $T_{p}$ being then exact, $T_{p}(B)$ is isomorphic to $T_{p}(A)/T_{p}(\mathfrak{p})$, hence is an
$A$-module (and a fortiori a $B$-module) of finite type. Let us argue by induction on $p$; $f_{p}$ is the canonical
image in $B$ of an element $g_{p} \in A$, and if one sets $A' = A_{g_{p}}$, one has $B' = A'/\mathfrak{p}'$ where
$\mathfrak{p}'$ is a minimal prime ideal of $A'$, equal to $\mathfrak{p}_{g_{p}}$. Since $T_{i}(A_{g_{p}}) =
(T_{i}(A))_{g_{p}}$, the $T_{i}(A')$ are $A'$-modules of finite type, so the functor $T^{(A')}_{\bullet}$ satisfies the
same hypotheses as $T_{\bullet}$, but replacing $i_{0}$ by $p$. One can therefore restrict to the case where $A' = A$
and where $T_{p}$ is exact; the exact sequence $0 \to \mathfrak{p} \to A \to A/\mathfrak{p} \to 0$ then gives the exact
sequence $T_{p+1}(A) \to T_{p+1}(A/\mathfrak{p}) \to^{\partial} T_{p}(\mathfrak{p}) \to T_{p}(A)$, and since $T_{p}$ is
exact, the rightmost arrow is injective, hence $T_{p+1}(A/\mathfrak{p})$ is a quotient of $T_{p+1}(A)$ and is
consequently of finite type. We now note that the argument of `(7.3.9)` used the fact that the $T_{p}(A)$ are of finite
type only for $p \leq N$; one can therefore apply it to the integral ring $B$, the functor $T^{(B)}_{\bullet}$ and $N =
p + 1$, which completes the induction. This being so, there exists $f_{N} \in B - {0}$ such that
$\operatorname{Spec}(B_{f_{N}})$ is an open set $V$ everywhere dense in $\operatorname{Spec}(B)$ meeting no other
irreducible component of $\operatorname{Spec}(A)$. If the proposition

<!-- original page 185 -->

is proved for $B_{f_{N}}$, one will have an open set $W$ everywhere dense in $V$ in which the functions of the statement
will be constant, since $A_{x} = (B_{f_{N}})_{x}$ for every $x \in W$. Doing the same reasoning for every irreducible
component of $\operatorname{Spec}(A)$, the corollary will be proved. One can therefore restrict to the case where $A$ is
integral; the reasoning of `(7.3.9)` then proves the existence of $f \in A - {0}$ such that the $T_{p}(A_{f})$ are free
$A_{f}$-modules of finite type for $p \leq N$, which entails the conclusion of `(7.3.10)` by virtue of `(7.3.4)`.

**Proposition (7.3.11).**

<!-- label: III.7.3.11 -->

*Let $A$ be a commutative local ring, $k$ its residue field, $T_{\bullet}$ a covariant homological functor from $Ab_{A}$
into `Ab`, commuting with direct sums. Suppose that there exists $i_{0}$ such that $T_{i}$ is exact for $i \leq i_{0}$,
and that all the $T_{n}(A)$ are $A$-modules of finite presentation. Then the equivalent conditions a), b), c) of
`(7.3.7)` imply the two following ones, and are equivalent to them when the ring is moreover reduced:*

- *d) For every $x \in \operatorname{Spec}(A)$, one has $rang_{\kappa(x)} T_{q}(\kappa(x)) = rang_{k} T_{q}(k)$ for $q
  \leq p$.*
- *d') For every generic point $x_{j}$ of an irreducible component of $\operatorname{Spec}(A)$, one has*
    ```text
      rang_{κ(x_j)} T_q(κ(x_j)) = rang_k T_q(k)   for q ≤ p.
    ```

**Proof.** Since $T_{q}(A)$ is an $A$-module of finite presentation, condition b) of `(7.3.7)` is equivalent to saying
that $T_{q}(A)$ is a *free* $A$-module for $q \leq p$ (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5);
condition c) implies that $T_{q}(\kappa(x)) = T_{q}(A) \otimes_{A} \kappa(x)$ for $q \leq p$, hence the equivalent
conditions of `(7.3.7)` imply d), and it is trivial that d) implies d'). It remains to prove that d') implies a) when
$A$ is *reduced*. We argue by induction on $q \leq p$, since $T_{q}$ is exact for $q \leq i_{0}$. Suppose then that
$T_{k}$ is exact for $k \leq q < p$ and let us show that $T_{q+1}(A)$ is a free $A$-module. By virtue of the induction
hypothesis, $T_{q+1}(A) \otimes_{A} M$ is isomorphic to $T_{q+1}(M)$ for every $A$-module $M$, by condition c) of
`(7.3.7)` and `(7.3.3)`; applying this property to $M = \kappa(x_{j})$ and $M = k$, one finds, by virtue of hypothesis
d'), that

```text
  rang_{κ(x_j)} (T_{q+1}(A) ⊗_A κ(x_j)) = rang_k T_{q+1}(k)
```

for every $j$; but this implies that $T_{q+1}(A)$ is free (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, prop. 7), which
completes the proof.

The preceding results will be considerably improved for the homological functors of particular type that we shall study
in `(7.4)`; we shall obtain in fact exactness criteria involving only one of the $T_{p}$.

## 7.4. Exactness criteria for the functors $H_{\bullet}(P_{\bullet} \otimes_{A} M)$

**7.4.1.**

<!-- label: III.7.4.1 -->

Let $A$ be a ring (not necessarily commutative), $P_{\bullet}$ a complex of flat right $A$-modules. Since the functor $M
\mapsto P_{k} \otimes_{A} M$ is then exact on $Ab_{A}$ for every $k$, the $\partial$-functor

```text
  T_•(M) = H_•(P_• ⊗_A M)                                                    (7.4.1.1)
```

<!-- original page 186 -->

is a homological functor from $Ab_{A}$ into `Ab`, evidently $A$-linear when $A$ is commutative `(7.1.2)`, and commuting
with inductive limits.

If $A$ is commutative, then, for every $A$-algebra $B$, the homological functor $T^{(B)}_{\bullet}$ `(7.3.8)` is given
by definition by

```text
  T_•^{(B)}(N) = H_•(P_• ⊗_A N_{[ρ]})                                        (7.4.1.2)
```

where $\rho : A \to B$ is the homomorphism defining the algebra structure of $B$; since one can also write $P_{\bullet}
\otimes_{A} N_{[\rho]} = P_{\bullet} \otimes_{A} (B \otimes_{B} N)_{[\rho]} = (P_{\bullet} \otimes_{A} B) \otimes_{B}
N$, one sees that one has

```text
  T_•^{(B)}(N) = H_•(P'_• ⊗_B N)                                             (7.4.1.3)
```

for every $B$-module $N$, $P'_{\bullet}$ being the complex $P_{\bullet} \otimes_{A} B$ of flat $B$-modules $(0_{I},
6.2.1)$.

**Proposition (7.4.2).**

<!-- label: III.7.4.2 -->

*Under the general conditions of `(7.4.1)`, and for a given integer $p \in Z$, the following properties are equivalent:*

- *a) $T_{p}$ is left exact (or, what amounts to the same, $T_{p+1}$ is right exact).*
- *b) $Z'_{p}(P_{\bullet}) = Coker(P_{p+1} \to P_{p})$ is a flat right $A$-module.*
- *c) There exists a complex $P'_{\bullet}$ of flat right $A$-modules such that the differential*
    ```text
      d'_{p+1} : P'_{p+1} → P'_p
    ```
    *is zero, and an isomorphism of homological functors from $H_{\bullet}(P_{\bullet} \otimes_{A} M)$ onto $H_{\bullet}(P'_{\bullet} \otimes_{A} M)$.*

**Proof.** By definition, one has an exact sequence functorial in $M$

```text
  0 → T_p(M) → Z'_p(P_• ⊗ M) → P_{p−1} ⊗ M
```

where $Z'_{p}(P_{\bullet} \otimes M) = Coker(P_{p+1} \otimes M \to P_{p} \otimes M) = Z'_{p}(P_{\bullet}) \otimes M$ by
virtue of the right exactness of the tensor product. For every homomorphism $f : M \to N$, one therefore has a
commutative diagram

```text
  0 → T_p(M) ──── Z'_p(P_•) ⊗ M ──── P_{p−1} ⊗ M
        │              │                │
        │u             │v               │w                                   (7.4.2.1)
        ↓              ↓                ↓
  0 → T_p(N) ──── Z'_p(P_•) ⊗ N ──── P_{p−1} ⊗ N
```

whose rows are exact. If $f$ is a monomorphism, so is $w$ since $P_{p-1}$ is flat; if $T_{p}$ is left exact, $u$ is also
a monomorphism; one concludes that $v$ is a monomorphism, which implies that $Z'_{p}(P_{\bullet})$ is flat. Conversely,
if it is so, $v$ is a monomorphism for every monomorphism $f : M \to N$, hence the diagram `(7.4.2.1)` shows that $u$ is
a monomorphism, and consequently $T_{p}$ (which is already semi-exact) is left exact. Thus a) and b) are equivalent. It
is immediate that c) implies a), for if $d'_{p+1} : P'_{p+1} \to P'_{p}$ is zero, and $0 \to M' \to M \to M'' \to 0$ is
an exact sequence of $A$-modules, the boundary operator $\partial$ in the exact sequence

```text
  H_{p+1}(P'_• ⊗ M'') →^∂ H_p(P'_• ⊗ M') → H_p(P'_• ⊗ M)
```

<!-- original page 187 -->

is zero by definition `(M, IV, 1)`, hence $T_{p}$ is left exact. Let us show conversely that b) implies c). If
$Z_{p+1}(P_{\bullet}) = Ker(P_{p+1} \to P_{p})$, one has an exact sequence

$$ 0 \to Z_{p+1}(P_{\bullet}) \to P_{p+1} \to Z'_{p}(P_{\bullet}) \to 0 $$

in which $P_{p+1}$ and $Z'_{p}(P_{\bullet})$ are flat, hence $Z_{p+1}(P_{\bullet})$ is flat $(0_{I}, 6.1.2)$. We shall
take

```text
  P'_i = P_i  for  i ≠ p  and  i ≠ p+1,   P'_p = Z'_p(P_•)  and  P'_{p+1} = Z_{p+1}(P_•);
```

for the differential $d'_{i} : P'_{i} \to P'_{i-1}$, we shall take that of the complex $P_{\bullet}$ for $i \neq p$ and
$i \neq p + 1$, `0` for $i = p + 1$ and for $i = p$ the homomorphism $Z'_{p}(P_{\bullet}) \to P_{p-1}$ deduced from
$d_{p}$ by passage to the quotient. Since the $P_{i}$ are flat, one has

```text
  Z'_i(P_• ⊗ M) = Z'_i(P_•) ⊗ M,  Z_i(P_• ⊗ M) = Z_i(P_•) ⊗ M  and  B_i(P_• ⊗ M) = B_i(P_•) ⊗ M
```

(setting $B_{i}(P_{\bullet}) = Im(P_{i+1} \to P_{i})$); one concludes at once for every $M$ the functorial isomorphisms
$H_{i}(P_{\bullet} \otimes M) \xrightarrow{\sim} H_{i}(P'_{\bullet} \otimes M)$ for every $i$, and the verification of
the fact that this is an isomorphism of $\partial$-functors follows without difficulty from the definition of $\partial$
`(M, IV, 1)`.

One notes that the conditions of `(7.4.2)` also imply that $B_{p}(P_{\bullet})$ is flat, for one has an exact sequence
$0 \to B_{p}(P_{\bullet}) \to P_{p} \to Z'_{p}(P_{\bullet}) \to 0$, in which $P_{p}$ and $Z'_{p}(P_{\bullet})$ are flat
$(0_{I}, 6.1.2)$.

**Corollary (7.4.3).**

<!-- label: III.7.4.3 -->

*Suppose that $A$ is a noetherian regular ring of dimension 1 (in other words a product of Dedekind rings $(0_{IV},
17.1.3 and 17.3.7)$, for example a principal ring). Then, for $T_{p}$ to be left exact, it is necessary and sufficient
that $T_{p}(A)$ be a flat $A$-module. For $T_{p}$ to be exact, it is necessary and sufficient that $T_{p}(A)$ and
$T_{p-1}(A)$ be flat $A$-modules.*

**Proof.** Recall that for a module $M$ over a Dedekind ring, it amounts to the same to say that $M$ is flat or that it
is torsion-free $(0_{I}, 6.3.3 and 6.3.4)$; under the hypotheses of `(7.4.3)`, every submodule of a flat $A$-module is
therefore flat.

The second assertion of `(7.4.3)` results from the first, since to say that $T_{p}$ is exact means that $T_{p}$ and
$T_{p-1}$ are left exact. To prove the first assertion, note that one has an exact sequence

$$ 0 \to H_{p}(P_{\bullet}) \to Z'_{p}(P_{\bullet}) \to B_{p-1}(P_{\bullet}) \to 0 $$

in which $B_{p-1}(P_{\bullet})$ is a flat $A$-module, as a submodule of the flat $A$-module $P_{p-1}$. It is therefore
equivalent to say that $H_{p}(P_{\bullet})$ is flat or that $Z'_{p}(P_{\bullet})$ is flat $(0_{I}, 6.1.2)$.

The most important applications of `(7.4.2)` are the following:

**Proposition (7.4.4).**

<!-- label: III.7.4.4 -->

*Let $A$ be a noetherian ring, $P_{\bullet}$ a complex of flat $A$-modules: suppose, either that the $P_{i}$ are of
finite type, or that the $H_{i}(P_{\bullet})$ are $A$-modules of finite type and that there exists $i_{0}$ such that
$H_{i}(P_{\bullet}) = 0$ for $i < i_{0}$. Let $T_{\bullet}$ be the homological functor defined by `(7.4.1.1)`. Then the
set $U$ of $y \in \operatorname{Spec}(A)$ such that $(T_{p})_{y}$ `(7.1.4)` is right exact (resp. left exact, exact) is
open in $\operatorname{Spec}(A)$.*

**Proof.** In the second hypothesis on $P_{\bullet}$, one can replace $P_{\bullet}$ by a complex $P'_{\bullet}$ of

<!-- original page 188 -->

free $A$-modules of finite type for which the functor $H_{\bullet}(P'_{\bullet} \otimes_{A} M)$ is isomorphic (as a
$\partial$-functor) to $T_{\bullet}(M)$ `(0, 11.9.3)`. One can therefore always reduce to the first hypothesis, and in
this case the $Z'_{p}(P_{\bullet})$ are of finite type; moreover, one can restrict to proving the assertions relative to
left exactness (cf. `(7.4.2, a))`). This being so, let $x \in U$; since the functor $M \mapsto M_{x}$ is exact, one has
$(Z'_{p}(P_{\bullet}))_{x} = Z'_{p}((P_{\bullet})_{x})$, and (taking `(7.4.1.3)` into account) the hypothesis implies,
by virtue of `(7.4.2, b))`, that $(Z'_{p}(P_{\bullet}))_{x}$ is a flat $A_{x}$-module, hence free since it is of finite
type and $A_{x}$ is a noetherian local ring (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5). One
concludes that there is $f \in A$ such that $(Z'_{p}(P_{\bullet}))_{f}$ is free over $A_{f}$ (Bourbaki, *Alg. comm.*,
chap. II, § 5, n° 1, cor. of prop. 2), and a fortiori $(Z'_{p}(P_{\bullet}))_{y}$ is free over $A_{y}$ for every $y \in
D(f)$, which completes the proof by virtue of `(7.4.2, b))`.

**Corollary (7.4.5).**

<!-- label: III.7.4.5 -->

*Under the hypotheses of `(7.4.4)`, suppose moreover that $A$ is integral. Then the set $U$ of $x \in
\operatorname{Spec}(A)$ such that $(T_{p})_{x}$ is exact is open and non-empty.*

**Proof.** It suffices to prove that $(T_{p})_{x}$ is exact for the generic point $x$ of $\operatorname{Spec}(A)$, which
is immediate since $A_{x}$ is a field, hence every additive functor on $Ab_{A_{x}}$ is exact.

**Proposition (7.4.6).**

<!-- label: III.7.4.6 -->

*Under the general hypotheses of `(7.4.4)`, conditions a), b) and c) of `(7.4.2)` are also equivalent to:*

- *d) There exists an $A$-module $Q$ and a functorial isomorphism*
    ```text
      T_p(M) ⥲ Hom_A(Q, M).                                                  (7.4.6.1)
    ```

*Moreover, the $A$-module $Q$ is determined up to unique isomorphism by this property, and it is of finite type.*

**Proof.** The uniqueness of $Q$ is a particular case of the uniqueness of a representative object of a representable
functor `(0, 8.1.5)`. It is clear that the second member of `(7.4.6.1)` is left exact. Conversely, to prove the
existence of $Q$, when $T_{p}$ is left exact, one can first, as in `(7.4.4)`, reduce to the case where the $P_{i}$ are
flat and of finite type, hence (since $A$ is noetherian) *projective of finite type* (Bourbaki, *Alg. comm.*, chap. II,
§ 5, n° 2, cor. of th. 1). The *dual* $\check{P}_{i}$ of $P_{i}$ is then also a projective $A$-module of finite type,
$P_{i}$ is canonically isomorphic to the dual of $\check{P}_{i}$, and the canonical homomorphism $P_{i} \otimes_{A} M
\to \operatorname{Hom}_{A}(\check{P}_{i}, M)$ is bijective (Bourbaki, *Alg.*, chap. II, 3rd ed., § 4, n° 2, prop. 2).
One knows on the other hand `(7.4.2, c))` that one can suppose $d_{p+1} : P_{p+1} \to P_{p}$ is zero, hence one has an
exact sequence

```text
  0 → T_p(M) → P_p ⊗ M →^v P_{p−1} ⊗ M
```

where $v = d_{p} \otimes 1$. Set then $Q' = Ker(d_{p})$, so that one has the exact sequence $0 \to Q' \to^{w} P_{p}
\to^{d_{p}} P_{p-1}$, whence by transposition the exact sequence $\check{P}_{p-1} \to^{{}^{t}d_{p}} \check{P}_{p}
\to^{{}^{t}w} \check{Q}' \to 0$. We shall see that $Q = \check{Q}' = Coker({}^{t}d_{p})$ answers the question. Indeed,
one has the exact sequence

```text
  0 → Hom(Q, M) → Hom(P̌_p, M) →^{v'} Hom(P̌_{p−1}, M)
```

<!-- original page 189 -->

where $v' = \operatorname{Hom}({}^{t}d_{p}, 1)$; when one canonically identifies $P_{i} \otimes M$ to
$\operatorname{Hom}(\check{P}_{i}, M)$, $v'$ is therefore identified with $v = d_{p} \otimes 1$, and one has
consequently the functorial isomorphism $T_{p}(M) \xrightarrow{\sim} \operatorname{Hom}_{A}(Q, M)$ sought. Moreover,
$Q$, being a quotient of $\check{P}_{p}$, is of finite type.

**Proposition (7.4.7).**

<!-- label: III.7.4.7 -->

*Suppose the general conditions of `(7.4.4)` satisfied. Then, for every $A$-module $M$ of finite type:*

- *(i) The $T_{i}(M)$ are $A$-modules of finite type.*
- *(ii) For every ideal $\mathfrak{m}$ of $A$, the canonical homomorphism*
    ```text
      (T_i(M))^∧ → lim←_n T_i(M ⊗_A (A/𝔪^{n+1}))                             (7.4.7.1)
    ```
    *(where the left member is the Hausdorff completion of $T_{i}(M)$ for the $\mathfrak{m}$-preadic topology) is bijective.*

**Proof.** As in `(7.4.4)`, one reduces first to the case where the $P_{i}$ are of finite type; $A$ being noetherian,
the submodules of $P_{i} \otimes_{A} M$ are of finite type, whence trivially assertion (i). As for assertion (ii), it
follows more generally from the following lemma:

**Lemma (7.4.7.2).**

<!-- label: III.7.4.7.2 -->

*Let $A$ be a noetherian ring, $u : E \to F$ a homomorphism of $A$-modules of finite type. For every $A$-module of
finite type, set $K(M) = Ker(u \otimes 1_{M})$, $C(M) = Coker(u \otimes 1_{M})$; then the canonical homomorphisms*

```text
  (K(M))^∧ → lim←_n K(M_n),    (C(M))^∧ → lim←_n C(M_n)                      (7.4.7.3)
```

*(where one has set $M_{n} = M \otimes_{A} (A/\mathfrak{m}^{n+1}) = M/\mathfrak{m}^{n+1} M$) are bijective for every
ideal $\mathfrak{m}$ of $A$.*

**Proof.** Since $E \otimes M$ and $F \otimes M$ are of finite type, and the functor $M \mapsto \hat{M}$ is exact in the
category of $A$-modules of finite type $(0_{I}, 7.3.3)$, $(K(M))^{\wedge}$ and $(C(M))^{\wedge}$ are respectively the
kernel and the cokernel of $(u \otimes 1)^{\wedge} : (E \otimes M)^{\wedge} \to (F \otimes M)^{\wedge}$. The left
exactness of the functor $\lim\leftarrow$ shows therefore that $(K(M))^{\wedge} = \lim\leftarrow_{n} K(M_{n})$; on the
other hand, the right exactness of the tensor product proves that $C(M_{n}) = C(M) \otimes_{A} (A/\mathfrak{m}^{n+1})$,
hence $(C(M))^{\wedge} = \lim\leftarrow_{n} C(M_{n})$ by definition.

**Remark (7.4.8).**

<!-- label: III.7.4.8 -->

Taking `(6.10.5)` and `(6.10.6)` into account, one sees that, given an additional flatness hypothesis, `(7.4.7)` gives
back the fact that `(4.1.7.1)` is an isomorphism, that is, the essence of the "first comparison theorem" for proper
morphisms; moreover, the statement applies not only to a coherent $\mathcal{O}_{X}$-module, but to a *complex* of such
modules. It would be interesting to obtain a statement comprising at the same time `(7.4.7)` and `(4.1.7.1)` as
particular cases. One will note that when the $P_{i}$ are of finite type, the proof of `(7.4.7)` does not use the fact
that they are flat modules; it would be worthwhile examining whether the conclusion of `(7.4.7)` is still valid when the
$P_{i}$ are not supposed flat nor of finite type, but the $H_{i}(P_{\bullet})$ are supposed of finite type for every $i$
and zero for $i < i_{0}$. Is it then possible to replace $P_{\bullet}$ by a complex $P'_{\bullet}$ of $A$-modules of
finite type such that the functors $H_{\bullet}(P_{\bullet} \otimes M)$ and $H_{\bullet}(P'_{\bullet} \otimes M)$ (which
are no longer homological) are still isomorphic?

<!-- original page 190 -->

## 7.5. The case of noetherian local rings

**7.5.1.**

<!-- label: III.7.5.1 -->

Let $A$ be a noetherian local ring, $\mathfrak{m}$ its maximal ideal, and for every $A$-module $M$, denote by $\hat{M}$
its Hausdorff completion for the $\mathfrak{m}$-preadic topology, isomorphic to $\lim\leftarrow(M \otimes_{A}
(A/\mathfrak{m}^{n+1})) = \lim\leftarrow(M/\mathfrak{m}^{n+1} M)$. Let $T$ be a covariant additive functor from $Ab_{A}$
into `Ab`; the canonical homomorphisms `(7.2.3.1)`

```text
  T(M) ⊗_A (A/𝔪^{n+1}) → T(M ⊗_A (A/𝔪^{n+1}))
```

evidently form a projective system of $A$-homomorphisms, which thus give in the limit an `Â`-homomorphism functorial in
$M$

$$ (T(M))^{\wedge} \to \lim\leftarrow_{n} T(M_{n}) (7.5.1.1) $$

where one has set $M_{n} = M \otimes_{A} (A/\mathfrak{m}^{n+1})$, $A_{n} = A/\mathfrak{m}^{n+1}$.

**Proposition (7.5.2).**

<!-- label: III.7.5.2 -->

*Let $A$ be a noetherian local ring with maximal ideal $\mathfrak{m}$, $k = A/\mathfrak{m}$ its residue field, $T$ a
covariant additive functor from $Ab_{A}$ into `Ab`, semi-exact and commuting with inductive limits. Suppose moreover
that for every $A$-module of finite type $M$, $T(M)$ is an $A$-module of finite type and that the canonical homomorphism
`(7.5.1.1)` is an isomorphism. Under these conditions, the following properties are equivalent:*

- *a) $T$ is right exact.*
- *b) For every $n$, the functor $N \mapsto T(N)$ is right exact in the category of $A_{n}$-modules of finite type
  (which amounts to saying that $T$ is right exact in the category of $A$-modules of finite length).*
- *c) The canonical homomorphism $T(\epsilon) : T(A) \to T(k)$ is surjective.*
- *d) For every $n$ sufficiently large, the canonical homomorphism $T(A_{n}) \to T(k)$ is surjective.*

**Proof.** It is clear that a) implies b). Let us show that b) implies a), that is, that if $u : M \to N$ is an
epimorphism of $A$-modules, $T(u)$ is an epimorphism. Since $T$ commutes with inductive limits and the functor $\lim\to$
is exact in the category of modules (for filtered index sets), one can restrict to the case where $M$ and $N$ are of
finite type. Since $T(M)$ and $T(N)$ are then of finite type, and $A$ is a noetherian local ring, it suffices to show
that $(T(u))^{\wedge} : (T(M))^{\wedge} \to (T(N))^{\wedge}$ is surjective $(0_{I}, 7.3.5 and 0_{I}, 6.4.1)$. By
hypothesis, $(T(M))^{\wedge}$ and $(T(N))^{\wedge}$ are respectively $\lim\leftarrow_{n} T(M_{n})$ and
$\lim\leftarrow_{n} T(N_{n})$, hence $(T(u))^{\wedge}$ is the limit of the projective system of homomorphisms $T(u
\otimes 1_{A_{n}}) : T(M_{n}) \to T(N_{n})$. Now, b) means that these homomorphisms are surjective; moreover, $T(M_{n})$
is an $A_{n}$-module of finite type, and $A_{n}$ is an artinian ring by hypothesis; one concludes that $(T(u))^{\wedge}$
is surjective `(0, 13.1.2 and 13.2.2)`. It is clear that a) implies c), and since $T(\epsilon)$ factors as $T(A) \to
T(A_{n}) \to T(k)$, c) implies d); finally, it follows from `(7.2.7)` that b) and d) are equivalent since $T$ is
semi-exact in $Ab_{A_{n}}$, which completes the proof.

**Corollary (7.5.3).**

<!-- label: III.7.5.3 -->

*Under the general hypotheses of `(7.5.2)`, if $T(k) = 0$, then $T(M) = 0$ for every $A$-module $M$.*

<!-- original page 191 -->

**Proof.** Since $k$ is the only simple $A$-module, one deduces from `(7.3.5.4)` that $T(E) = 0$ for every $A$-module of
finite length $E$. If now $M$ is of finite type, $(T(M))^{\wedge}$ is isomorphic to $\lim\leftarrow_{n} T(M_{n})$, and
since the $M_{n}$ are of finite length, one has $(T(M))^{\wedge} = 0$; since $T(M)$ is of finite type by hypothesis, it
is isomorphic to a submodule of $(T(M))^{\wedge}$ $(0_{I}, 7.3.5)$, hence one has $T(M) = 0$. Finally, for an arbitrary
$A$-module $M$, $T(M)$ is the inductive limit of the $T(N_{\alpha})$ for the submodules of finite type $N_{\alpha}$ of
$M$, which completes the proof.

**Proposition (7.5.4).**

<!-- label: III.7.5.4 -->

*Let $A$ be a noetherian local ring with maximal ideal $\mathfrak{m}$, $k = A/\mathfrak{m}$ its residue field,
$T_{\bullet}$ a homological functor from $Ab_{A}$ into `Ab`, commuting with inductive limits. Suppose moreover that for
every $i$ and every $A$-module $M$ of finite type, $T_{i}(M)$ is of finite type and the canonical homomorphism
$(T_{i}(M))^{\wedge} \to \lim\leftarrow_{n} T_{i}(M_{n})$ is bijective. For a given integer $p$, the following
conditions are then equivalent:*

- *a) $T_{p}$ is exact.*
- *b) $T_{p}$ is right exact, and $T_{p}(A)$ is a free $A$-module.*
- *c) The canonical homomorphisms $T_{p+1}(A) \to T_{p+1}(k)$ and $T_{p}(A) \to T_{p}(k)$ are surjective.*
- *d) For every $n$, the canonical homomorphisms $T_{p+1}(A_{n}) \to T_{p+1}(k)$ and $T_{p}(A_{n}) \to T_{p}(k)$ are
  surjective.*
- *e) For every $n$, the functor $N \mapsto T_{p}(N)$ is exact in the category of $A_{n}$-modules of finite type.*

**Proof.** One knows `(7.3.3)` that a) is equivalent to saying that $T_{p+1}$ and $T_{p}$ are right exact; since
$T_{\bullet}$ is a homological functor in the category $Ab_{A_{n}}$, the same reasoning as in `(7.3.1)` shows that e) is
equivalent to saying that $T_{p}$ and $T_{p+1}$ are right exact in the category of $A_{n}$-modules of finite type. One
therefore deduces from `(7.5.2)` that a) and e) are equivalent; the equivalence of a), c) and d) also results from
`(7.5.2)`. Finally, one knows that every flat $A$-module of finite type is free (Bourbaki, *Alg. comm.*, chap. II, § 3,
n° 2, cor. 2 of prop. 5); the equivalence of a) and b) results then from `(7.3.1)` and `(7.3.3)`.

**Corollary (7.5.5).**

<!-- label: III.7.5.5 -->

*Suppose the general conditions of `(7.5.4)` satisfied.*

- *(i) If $T_{p}(k) = 0$, one has $T_{p} = 0$, $T_{p+1}$ is right exact and $T_{p-1}$ is left exact.*
- *(ii) If $T_{p-1}(k) = T_{p+1}(k) = 0$, $T_{p}$ is exact, the canonical homomorphism*
    ```text
      T_p(A) ⊗_A M → T_p(M)
    ```
    *is bijective and $T_{p}(A)$ is a free $A$-module.*

**Proof.** (i) follows immediately from `(7.5.3)` since $T_{p}$ is semi-exact, the last assertion resulting from the
definition of a homological functor. One concludes immediately from (i) the first two assertions of (ii), taking
`(7.3.3)` into account; the fact that $T_{p}(A)$ is free results from `(7.5.4)`.

**Corollary (7.5.6).**

<!-- label: III.7.5.6 -->

*Suppose the general hypotheses of `(7.5.4)` satisfied, and suppose moreover that $A$ is a discrete valuation ring.*

- *(i) For $T_{p}$ to be right exact, it is necessary and sufficient that $T_{p-1}(A)$ be a free $A$-module.*
- *(ii) For $T_{p}$ to be exact, it is necessary and sufficient that $T_{p+1}(A)$ and $T_{p}(A)$ be free $A$-modules.*

<!-- original page 192 -->

**Proof.** It is clear that (i) implies (ii) (cf. `(7.3.3)`). To prove (i), note that if $f$ is a generator of the
maximal ideal of $A$ ("uniformizer" of $A$), for an $A$-module of finite type $M$ to be free (or flat, which amounts to
the same), it is necessary and sufficient that the homothety $h_{f} : x \mapsto fx$ of $M$ be injective, since this is
equivalent here to saying that $M$ is torsion-free $(0_{I}, 6.3.4)$. Consider then the exact sequence $0 \to A
\to^{h_{f}} A \to k \to 0$, which provides the exact sequence of homology

```text
  T_p(A) → T_p(k) → T_{p−1}(A) →^{h_f} T_{p−1}(A).
```

One sees that $T_{p-1}(A)$ is free if and only if $T_{p}(A) \to T_{p}(k)$ is surjective; the conclusion then results
from `(7.5.2)`.

**Remark (7.5.7).**

<!-- label: III.7.5.7 -->

One will note that, by virtue of `(7.4.7)`, the general hypotheses of `(7.4.4)` imply that the homological functor
$T_{\bullet}$ defined by `(7.4.1.1)` satisfies the general hypotheses of `(7.5.4)`. In this case, `(7.5.6)` is therefore
contained in `(7.4.3)`.

## 7.6. Descent of exactness properties. Semi-continuity theorem and exactness criterion of Grauert

**Proposition (7.6.1).**

<!-- label: III.7.6.1 -->

*Under the conditions of `(7.4.1)`, let $B$ be a commutative $A$-algebra. If $T_{p}$ is right exact (resp. left exact,
exact), the same is true of $T^{(B)}_{p}$; the converse is true when $B$ is a faithfully flat $A$-module.*

**Proof.** The first assertion is a particular case of a trivial assertion of `(7.1.3)`. Conversely, suppose first that
$B$ is a flat $A$-module. One has then, for every $A$-module $M$, $H_{\bullet}(P_{\bullet} \otimes_{A} (M \otimes_{A}
B)) = (H_{\bullet}(P_{\bullet} \otimes_{A} M)) \otimes_{A} B$, which can also be written, for every $p$,

```text
  T_p(M) ⊗_A B = T_p^{(B)}(M_{(B)})                                          (7.6.1.1)
```

up to a canonical isomorphism. Suppose $T^{(B)}_{p}$ right exact (resp. left exact, exact); since $M \mapsto M_{(B)}$ is
an exact functor, the first member of `(7.6.1.1)` is a functor right exact (resp. left exact, exact) in $M$; if now $B$
is faithfully flat over $A$, one deduces that $T_{p}$ has the same exactness property $(0_{I}, 6.4.1)$.

**Proposition (7.6.2).**

<!-- label: III.7.6.2 -->

*Under the conditions of `(7.4.1)`, suppose moreover that $A$ is a reduced noetherian ring and that the $P_{i}$ are
$A$-modules of finite type. For $T_{p}$ to be right exact (resp. left exact, exact), it is necessary and sufficient
that, for every $A$-algebra $B$ which is a discrete valuation ring, $T^{(B)}_{p}$ be so.*

**Proof.** By virtue of `(7.3.1)` and `(7.3.3)`, one can restrict to considering right exactness, and there is of course
only the sufficiency of the condition to prove `(7.6.1)`. By virtue of `(7.4.2)`, it suffices to show that
$Z'_{p-1}(P_{\bullet})$ is a flat $A$-module; since $P_{p-1}$ is of finite type, $Z'_{p-1}(P_{\bullet})$ is also of
finite type; the criterion `(0, 10.2.8)` shows that it then suffices that $Z'_{p-1}(P_{\bullet}) \otimes_{A} B$ be a
flat $B$-module for every $A$-algebra $B$ which is a discrete valuation ring. Now, since $P_{\bullet}$ is a complex of
flat $A$-modules, one has

```text
  Z'_{p−1}(P_•) ⊗_A B = Z'_{p−1}(P_• ⊗_A B);
```

<!-- original page 193 -->

$P_{\bullet} \otimes_{A} B$ is a complex of flat $B$-modules $(0_{I}, 6.2.1)$, and for every $B$-module $N$, one has
$H_{\bullet}(P_{\bullet} \otimes_{A} N) = H_{\bullet}((P_{\bullet} \otimes_{A} B) \otimes_{B} N)$, hence
$T^{(B)}_{\bullet}(N) = H_{\bullet}((P_{\bullet} \otimes_{A} B) \otimes_{B} N)$; applying `(7.4.2)` to $T^{(B)}_{p}$,
one sees that the hypothesis that $T^{(B)}_{p}$ is right exact is equivalent to the fact that $Z'_{p-1}(P_{\bullet}
\otimes_{A} B)$ is a flat $B$-module.

The preceding criterion leads to studying more closely the case of discrete valuation rings:

**Proposition (7.6.3).**

<!-- label: III.7.6.3 -->

*Under the conditions of `(7.4.1)`, suppose that $A$ is a noetherian regular ring of dimension 1 (in other words, $A$ is
noetherian and, for every $x \in \operatorname{Spec}(A)$, $A_{x}$ is a field or a discrete valuation ring). Then, for
every integer $p$ and every $A$-module $M$, one has a canonical exact sequence functorial in $M$*

```text
  0 → T_p(A) ⊗_A M →^{t_M} T_p(M) → Tor_1^A(T_{p−1}(A), M) → 0.              (7.6.3.1)
```

**Proof.** In what follows, we shall suppress for simplicity the mention of the complex $P_{\bullet}$ in the usual
homological notations $H_{p}(P_{\bullet})$, $B_{p}(P_{\bullet})$, $Z_{p}(P_{\bullet})$ and $Z'_{p}(P_{\bullet})$. One
has the three exact sequences

$$ 0 \to H_{p} \to Z'_{p} \to B_{p-1} \to 0 0 \to B_{p-1} \to Z_{p-1} \to H_{p-1} \to 0 0 \to Z_{p-1} \to P_{p-1} \to
B_{p-2} \to 0 $$

Since $P_{p-1}$ and $P_{p-2}$ are flat, the same is true of their respective *submodules* $B_{p-1}$, $Z_{p-1}$ and
$B_{p-2}$, since there is identity between flat $A_{x}$-modules and torsion-free $A_{x}$-modules (for every $x \in
\operatorname{Spec}(A)$); by tensorization with $M$, one thus has the exact sequences

```text
  0 = Tor_1^A(B_{p−1}, M) → H_p ⊗ M → Z'_p ⊗ M →^u B_{p−1} ⊗ M → 0           (7.6.3.2)
  0 → Tor_1^A(Z_{p−1}, M) → Tor_1^A(H_{p−1}, M) → B_{p−1} ⊗ M →^v Z_{p−1} ⊗ M  (7.6.3.3)
  0 = Tor_1^A(B_{p−2}, M) → Z_{p−1} ⊗ M →^w P_{p−1} ⊗ M.                     (7.6.3.4)
```

By definition, $T_{p}(M) = Ker(d_{p} \otimes 1) / Im(d_{p+1} \otimes 1)$; it is therefore the kernel of the homomorphism
$(P_{p} \otimes M) / Im(d_{p+1} \otimes 1) \to P_{p-1} \otimes M$ obtained from $d_{p} \otimes 1$ by passage to the
quotient, a homomorphism which is also written $Z'_{p} \otimes M \to P_{p-1} \otimes M$ by definition of $Z'_{p} = P_{p}
/ B_{p}$; now, this homomorphism can be considered as the composite

```text
  Z'_p ⊗ M →^u B_{p−1} ⊗ M →^v Z_{p−1} ⊗ M →^w P_{p−1} ⊗ M.
```

Since $w$ is injective by `(7.6.3.4)`, one has an exact sequence

```text
  0 → Ker u → T_p(M) → Ker v → 0,
```

which is none other than `(7.6.3.1)`, taking `(7.6.3.2)` and `(7.6.3.3)` and the fact that $H_{p} = T_{p}(A)$ by
definition into account.

**Remarks (7.6.4).**

<!-- label: III.7.6.4 -->

(i) $H_{\bullet}(P_{\bullet} \otimes_{A} M)$ is the homology of the bicomplex $P_{\bullet} \otimes_{A} M$, where $M$ is
considered as a complex reduced to its term of degree `0`; it is consequently `(6.3.6 and 6.3.2)` the abutment of the
regular spectral sequence whose `E_2` term is

```text
  E_2^{p,q} = Tor_p^A(H_q(P_•), M) = Tor_p^A(T_q(A), M).
```

<!-- original page 194 -->

Now, the hypothesis on the ring $A$ implies that $Tor^{A}_{p}(E, F) = 0$ for $p \geq 2$ and for arbitrary $A$-modules
$(0_{IV}, 17.2.2)$; one knows `(M, XV)` that this implies the exactness of the sequence

```text
  0 → E_{0,q}^2 → H_q(P_• ⊗_A M) → E_{1, q−1}^2 → 0
```

which is none other than `(7.6.3.1)`.

(ii) Taking `(7.3.1)` into account, the exact sequence `(7.6.3.1)` recovers as a particular case the result of
`(7.4.3)`.

**Corollary (7.6.5).**

<!-- label: III.7.6.5 -->

*Under the conditions of `(7.4.1)`, suppose that $A$ is a discrete valuation ring, with fraction field $K$, residue
field $k$, and that the $T_{i}(A)$ are $A$-modules of finite type. One has then*

```text
  rang_k T_p(k) ≥ rang_k(T_p(A) ⊗_A k) ≥ rang_A T_p(A) = rang_K T_p(K).      (7.6.5.1)
```

*Moreover, for the extreme terms of this inequality to be equal, it is necessary and sufficient that $T_{p}$ be exact,
or equivalently that $T_{p}(A)$ and $T_{p-1}(A)$ be free $A$-modules.*

**Proof.** Indeed, setting $M = k$ in the exact sequence `(7.6.3.1)`, since one is dealing with vector spaces over $k$,

```text
  rang_k T_p(k) = rang_k(T_p(A) ⊗_A k) + rang_k(Tor_1^A(T_{p−1}(A), k)).
```

On the other hand, since $T_{p}(A)$ is a module of finite type over the integral local ring $A$, one has (Bourbaki,
*Alg. comm.*, chap. II, § 3, n° 2, cor. 1 of prop. 4)

```text
  rang_k(T_p(A) ⊗_A k) ≥ rang_A T_p(A) = rang_K(T_p(A) ⊗_A K)                (7.6.5.2)
```

and moreover the two members of `(7.6.5.2)` are equal if and only if $T_{p}(A)$ is a free $A$-module (*loc. cit.*, prop.
7). One will note moreover that since $K$ is a flat $A$-module, one has by definition $T_{p}(A) \otimes_{A} K =
H_{p}(P_{\bullet}) \otimes_{A} K = H_{p}(P_{\bullet} \otimes_{A} K) = T_{p}(K)$. One has therefore indeed the inequality
`(7.6.5.1)`, and one sees moreover that equality is possible only if: 1° $T_{p}(A)$ is free; 2° $Tor^{A}_{1}(T_{p-1}(A),
k) = 0$, a condition which is equivalent, as one knows `(0, 10.1.3)`, to the fact that $T_{p-1}(A)$ is a free
$A$-module. Finally, since the $T_{i}(A)$ are $A$-modules of finite type, it amounts to the same to say that they are
flat or free (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5), and one concludes by `(7.4.3)`.

**7.6.6.**

<!-- label: III.7.6.6 -->

The hypotheses still being those of `(7.4.1)`, we shall set, for every $x \in \operatorname{Spec}(A)$,

```text
  d_p(x) = d_p^T(x) = rang_{κ(x)} T_p(κ(x)).                                 (7.6.6.1)
```

**Lemma (7.6.7).**

<!-- label: III.7.6.7 -->

*Let $\phi : A \to A'$ be a ring homomorphism, and let*

```text
  f = ᵃφ : Spec(A') → Spec(A)
```

*be the corresponding map `(I, 1.2.1)`. If one sets $T'_{\bullet} = T^{(A')}_{\bullet}$ `(7.1.3)`, one has*

$$ d^{T'}_{p} = d^{T}_{p} \circ f. (7.6.7.1) $$

<!-- original page 195 -->

**Proof.** Indeed, for every $x' \in \operatorname{Spec}(A')$, on setting $x = f(x')$, one has

```text
  H_•(P_• ⊗_A κ(x')) = H_•((P_• ⊗_A κ(x)) ⊗_{κ(x)} κ(x')) = H_•(P_• ⊗_A κ(x)) ⊗_{κ(x)} κ(x'),
```

since $\kappa(x')$ is flat over $\kappa(x)$, whence the relation `(7.6.7.1)`.

**Lemma (7.6.8).**

<!-- label: III.7.6.8 -->

*If the ring $A$ is noetherian and the complex $P_{\bullet}$ formed of $A$-modules of finite type, the function $x
\mapsto d^{T}_{p}(x)$ on $\operatorname{Spec}(A)$ is constructible.*

**Proof.** It must be proved that for every irreducible closed part $Y$ of $X = \operatorname{Spec}(A)$, there exists a
non-empty open $U$ of $Y$ on which $d_{p}$ is constant `(0, 9.2.2)`; since $Y = \operatorname{Spec}(A/\mathfrak{a})$,
where $\mathfrak{a}$ is an ideal of $A$ such that $A/\mathfrak{a}$ is reduced, one can, by virtue of `(7.6.7)`, restrict
to the case where $Y = X$ and $A$ is a noetherian integral ring; but then the assertion results from `(7.4.5)`.

**Theorem (7.6.9).**

<!-- label: III.7.6.9 -->

*Let $A$ be a noetherian ring, $P_{\bullet}$ a complex of flat $A$-modules of finite type, $T_{\bullet}(M) =
H_{\bullet}(P_{\bullet} \otimes_{A} M)$ the homological functor defined by $P_{\bullet}$; for every $x \in
\operatorname{Spec}(A)$ let $d_{p}(x) = rang_{\kappa(x)} T_{p}(\kappa(x))$. Then:*

- *(i) The function $d_{p}$ is constructible and upper semi-continuous on $\operatorname{Spec}(A)$.*
- *(ii) If $T_{p}$ is exact, $d_{p}$ is continuous (hence locally constant) on $\operatorname{Spec}(A)$; the converse is
  true when the ring $A$ is reduced.*

**Proof.**

(i) The first assertion was proved in `(7.6.8)`. To prove the second, it suffices `(0, 9.2.4)` to show that if $x' \neq
x$ is a generization of $x$ in $\operatorname{Spec}(A)$, one has $d_{p}(x') \leq d_{p}(x)$. Now, there exists then a
discrete valuation ring $B$ and a morphism $f : \operatorname{Spec}(B) \to \operatorname{Spec}(A)$ such that, if $a$
denotes the closed point of $\operatorname{Spec}(B)$ and $b$ its generic point, one has $f(a) = x$ and $f(b) = x'$
`(II, 7.1.9)`. By virtue of formula `(7.6.7.1)`, one sees that one is reduced to proving the inequality $d_{p}(a) \geq
d_{p}(b)$ in $\operatorname{Spec}(B)$; but this is none other than the inequality `(7.6.5.1)` (¹).

(ii) The first assertion was already proved `(7.3.4)`. To prove the converse, let us use the valuative criterion
`(7.6.2)`; taking formula `(7.6.7.1)` into account, one is therefore reduced to the case where $A$ is a discrete
valuation ring; but since $\operatorname{Spec}(A)$ comprises only two points, the hypothesis that $d_{p}$ is constant
indeed implies that $T_{p}$ is exact, by virtue of `(7.6.5)`.

> (¹) The principle of the proof of (i) by reduction to the case of a discrete valuation ring was orally communicated to
> us by Hironaka.

**Corollary (7.6.10).**

<!-- label: III.7.6.10 -->

*Let $A$ be a noetherian ring, $\mathfrak{p}_{i}$ ($1 \leq i \leq r$) its minimal prime ideals, $k_{i}$ the residue
field of $A_{\mathfrak{p}_{i}}$ ($1 \leq i \leq r$).*

- *(i) For every $x \in \operatorname{Spec}(A)$, there exists an index $i$ such that*
    ```text
      d_p(x) ≥ rang_{k_i} T_p(k_i).                                          (7.6.10.1)
    ```

*In particular, if $A$ is integral and $K$ is its fraction field, one has*

$$ d_{p}(x) \geq rang_{K} T_{p}(K) (7.6.10.2) $$

*for every $x \in \operatorname{Spec}(A)$.*

<!-- original page 196 -->

- *(ii) Suppose moreover that $A$ is local and reduced, and let $k$ be its residue field. Then, for $T_{p}$ to be exact,
  it is necessary and sufficient that one have*
    ```text
      rang_k T_p(k) = rang_{k_i} T_p(k_i)   for 1 ≤ i ≤ r.                   (7.6.10.3)
    ```

**Proof.** (i) is immediate since every neighbourhood of $x$ contains one of the $\mathfrak{p}_{i}$, and it suffices to
apply the definition of semi-continuity. On the other hand, if $A$ is local, the only neighbourhood in
$\operatorname{Spec}(A)$ of the maximal ideal $\mathfrak{m}$ is $\operatorname{Spec}(A)$ in its entirety, hence one has
$d_{p}(x) \leq rang_{k} T_{p}(k)$ for every $x \in \operatorname{Spec}(A)$; this relation, joined to (i), shows that
condition `(7.6.10.3)` implies that $d_{p}(x)$ is constant on $\operatorname{Spec}(A)$, and consequently that $T_{p}$ is
exact by virtue of `(7.6.9, (ii))`; the converse is obvious by virtue of `(7.6.9, (ii))`.

**Remark (7.6.11).**

<!-- label: III.7.6.11 -->

One can ask whether the assertion of `(7.6.9, (i))` cannot be strengthened by the inequality

```text
  rang_{κ(x)} T_p(κ(x)) ≥ rang_{κ(x)} (T_p(A) ⊗_A κ(x))                      (7.6.11.1)
```

for every $x \in \operatorname{Spec}(A)$, which effectively holds when $A$ is a discrete valuation ring and $x$ its
maximal ideal `(7.6.5)`. Let us restrict to the case where $A$ is a noetherian local ring with maximal ideal
$\mathfrak{m}$ and residue field $k$. Then, the following conditions are equivalent:

- a) For every complex $P_{\bullet}$ of flat $A$-modules of finite type, one has
    ```text
      rang_k(T_p(k)) ≥ rang_k(T_p(A) ⊗_A k)   for every integer p.           (7.6.11.2)
    ```
- b) For every $A$-module $M$ of finite type, one has
    ```text
      rang_k(M ⊗_A k) ≥ rang_k(M̌ ⊗_A k).                                     (7.6.11.3)
    ```
- c) For every $A$-module $N$ of finite type, one has
    ```text
      rang_k(Tor_1^A(N, k)) ≥ rang_k(Tor_2^A(N, k)).                         (7.6.11.4)
    ```

One will note that it amounts to the same, by shifting `(M, V, 7.2)`, to say that one has, for every $i \geq 1$,

```text
  rang_k(Tor_i^A(N, k)) ≥ rang_k(Tor_{i+1}^A(N, k)).                         (7.6.11.5)
```

Let us give quickly some indications on the proof. To see that a) implies b), one considers an exact sequence $L_{1}
\to^{d} L_{0} \to M \to 0$ where `L_0` and `L_1` are free of finite type, and one applies a) to the complex $P_{1}
\to^{{}^{t}d} P_{0}$ with $P_{0} = \check{L}_{1}$, $P_{1} = \check{L}_{0}$, the other terms being zero; one has then
$T_{1}(A) = \check{M}$ and $T_{1}(k) = \operatorname{Hom}_{k}(M, k) = \operatorname{Hom}_{k}(M/\mathfrak{m} M, k)$, that
is, $T_{1}(k)$ is the dual of the vector space $M \otimes_{A} k$, and therefore has the same rank as the latter. To
prove that b) implies c), we shall first establish the following lemma:

**Lemma (7.6.11.6).**

<!-- label: III.7.6.11.6 -->

*Given a complex $\cdots \to 0 \to P_{1} \to^{d} P_{0} \to 0 \to \cdots$ of flat $A$-modules, one has an exact sequence*

```text
  0 → Tor_2^A(Z'_0, k) → T_1(A) ⊗_A k → T_1(k) → Tor_1^A(Z'_0, k) → 0.        (7.6.11.7)
```

<!-- original page 197 -->

**Proof.** Indeed, starting from the exact sequence $0 \to Z_{1} \to P_{1} \to B_{0} \to 0$, one deduces the exact
sequence $0 \to Tor^{A}_{1}(B_{0}, k) \to Z_{1} \otimes k \to P_{1} \otimes k \to^{u} B_{0} \otimes k \to 0$. From the
exact sequence $0 \to B_{0} \to Z_{0} \to Z'_{0} \to 0$, one deduces, since $Z_{0} = P_{0}$ is flat, $Tor^{A}_{1}(B_{0},
k) = Tor^{A}_{2}(Z'_{0}, k)$; by definition, one has $Z_{1} = T_{1}(A)$; finally, one has $T_{1}(k) = Ker(d \otimes 1)$,
and $d \otimes 1$ factors as $P_{1} \otimes k \to^{u} B_{0} \otimes k \to^{v} Z_{0} \otimes k = P_{0} \otimes k$; one
has $T_{1}(k) = u^{-1}(R)$, where $R = Ker v$, and since $u$ is surjective, $R = u(T_{1}(k))$; finally, $R =
Tor^{A}_{1}(Z'_{0}, k)$ by definition of $v$, which finishes establishing the exact sequence `(7.6.11.7)`.

To deduce c) from b), one considers an exact sequence $L_{1} \to^{d} L_{0} \to N \to 0$, where `L_0` and `L_1` are free
modules of finite type; consider the functor $T$ associated to the complex formed of `L_1` and `L_0`; since `L_0` and
`L_1` are free, they are identified with their biduals; hence if $M = Coker({}^{t}d)$, $T_{1}(A) = Ker(d) = \check{M}$;
on the other hand, $M \otimes_{A} k = Coker({}^{t}d \otimes 1_{k})$ has the same rank over $k$ as $Ker(d \otimes
1_{k})$. The hypothesis b) implies consequently that

```text
  rang_k(T_1(A) ⊗_A k) ≤ rang_k(T_1(k));
```

since $Z'_{0} = N$, inequality `(7.6.11.4)` results from the exact sequence `(7.6.11.7)`. Finally, to prove that c)
implies a), let us apply `(7.6.11.6)` replacing `P_0` and `P_1` by $P_{p}$ and $P_{p-1}$; hypothesis c) applied to the
module $Z'_{p}$ gives $rang_{k} R \geq rang_{k} S$, where $R = Ker(P_{p} \otimes k \to P_{p-1} \otimes k)$ and $S =
Z'_{p} \otimes k$. Now, if one factors $d_{p+1} : P_{p+1} \to P_{p}$ as $P_{p+1} \to^{v} Z_{p} \to^{j} P_{p}$, one has
$Im(d_{p+1} \otimes 1) = (j \otimes 1)(Im(v \otimes 1))$. Since

```text
  T_p(A) ⊗_A k = (Z_p / B_p) ⊗_A k = (Z_p ⊗ k) / Im(v ⊗ 1),
```

and $T_{p}(k) = R / Im(d_{p+1} \otimes 1)$, one indeed concludes the inequality `(7.6.11.2)`.

This being so, suppose that the local ring $A$ is regular of dimension $n$; one knows then [17] that the $A$-module
$Tor^{A}_{i}(k, k)$ is isomorphic to the $i$th exterior power $\wedge^{i}(\mathfrak{m}/\mathfrak{m}^{2})$; one sees
therefore that condition `(7.6.11.4)` is not satisfied for $N = k$, as soon as $n \geq 4$. On the other hand, if the
integral local ring $A$ is such that every reflexive $A$-module of finite type is free (which is the case when $A$ is a
regular ring of dimension 2), condition `(7.6.11.3)` is satisfied: indeed, one knows that the dual $\check{M}$ of an
$A$-module of finite type $M$ is reflexive, hence free, and consequently `rang_k(M̌ ⊗_A k) = rang_K(M̌) = rang_K(M)` ($K$
fraction field of $A$); on the other hand, one knows that every basis over $k$ of $M \otimes_{A} k$ is formed of images
of a system of generators of $M$ (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 4), hence $rang_{K}(M)
\leq rang_{k}(M \otimes_{A} k)$, which proves our assertion.

## 7.7. Application to proper morphisms: I. The exchange property

The three subsections that follow are, essentially, translations into the language of morphisms of preschemes of the
results of the preceding subsections.

**7.7.1.**

<!-- label: III.7.7.1 -->

Let $f : X \to Y$ be a quasi-compact and separated morphism of preschemes, and let $\mathcal{P}_{\bullet}$ be a complex
of quasi-coherent $\mathcal{O}_{X}$-modules whose derivation operator is of degree $-1$; suppose moreover that the
$\mathcal{O}_{X}$-modules $\mathcal{P}_{i}$ are $Y$-flat $(0_{I}, 6.7.1)$.

<!-- original page 198 -->

We are going to consider the $\partial$-functor $\mathcal{M} \mapsto \mathcal{T}_{\bullet}(\mathcal{M})$ (also denoted
$\mathcal{T}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{M})$) in the category of quasi-coherent
$\mathcal{O}_{Y}$-modules, with values in the category of quasi-coherent $\mathcal{O}_{Y}$-modules (by virtue of
`(6.2.3)`), defined by

```text
  𝒯_n(𝒫_•, ℳ) = 𝒯_n(ℳ) = ℋ^{−n}(f, 𝒫^• ⊗_{𝒪_X} ℳ)   for n ∈ Z,                 (7.7.1.1)
```

where $\mathcal{P}^{\bullet}$ is the complex whose term of degree $j$ is $P_{-j}$, the derivation operator being then of
degree `+1`. The functor $\mathcal{T}_{\bullet}$ thus defined is a *homological functor* in $\mathcal{M}$ `(6.2.6)`.

**7.7.2.**

<!-- label: III.7.7.2 -->

Let $g : Y' \to Y$ be a morphism, and set $X' = X_{(Y')} = X \times_{Y} Y'$ and $f' = f_{(Y')} : X' \to Y'$, which is a
quasi-compact and separated morphism; let on the other hand $\mathcal{P}'_{\bullet} = \mathcal{P}_{\bullet}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$; this is a complex of quasi-coherent $\mathcal{O}_{X'}$-modules which are
$Y'$-flat by virtue of `(I, 9.1.12)` and $(0_{I}, 6.2.1)$. We shall set (with the same conventions on degrees)

```text
  𝒯'_•^{Y'}(ℳ') = ℋ^•(f', 𝒫'^• ⊗_{𝒪_{X'}} ℳ') = ℋ^•(f', 𝒫^• ⊗_{𝒪_X} ℳ')        (7.7.2.1)
```

which is a homological functor in the quasi-coherent $\mathcal{O}_{Y'}$-module $\mathcal{M}'$. When $Y'$ is an affine
scheme with ring $A'$, one will write $\mathcal{T}^{A'}_{\bullet}$ instead of $\mathcal{T}^{Y'}_{\bullet}$; for every
$A'$-module $M'$, one has then $\mathcal{T}^{A'}_{\bullet}(\tilde{M}') = (\Gamma(Y',
\mathcal{T}^{Y'}_{\bullet}(\tilde{M}')))^{\sim}$; one will set $T^{A'}_{\bullet}(M') = \Gamma(Y',
\mathcal{T}^{Y'}_{\bullet}(\tilde{M}'))$, which is a homological functor of $A'$-modules, with values in the category of
$A'$-modules. One will observe that if $Y = \operatorname{Spec}(A)$ is also affine, the functor of $A'$-modules
$T^{A'}_{\bullet}$ coincides with the functor obtained by extension of scalars from $A$ to $A'$ from the homological
functor of $A$-modules $T^{A}_{\bullet}$ `(7.1.3)`: indeed, let $g : Y' \to Y$ be the morphism corresponding to the ring
homomorphism $A \to A'$, and let $g' : X' \to X$ be the corresponding morphism, which is affine `(II, 1.6.2)`; if
$\mathfrak{U}$ is an affine open cover of $X$, $\mathfrak{U}' = g'^{-1}(\mathfrak{U})$ is an affine open cover of $X'$;
by virtue of `(6.2.2)`, it all comes down to seeing that $C^{\bullet}(\mathfrak{U}', \mathcal{P}^{\bullet}
\otimes_{\mathcal{O}_{X}} g'_{*}(\mathcal{M}')) = C^{\bullet}(\mathfrak{U}', \mathcal{P}^{\bullet}
\otimes_{\mathcal{O}_{X}} \mathcal{M}')$, and finally, that for every affine open $U$ of $X$, on setting $U' =
g'^{-1}(U)$, one has $\Gamma(U, \mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{X}} g'_{*}(\mathcal{M}')) = \Gamma(U',
\mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{M}')$, which is trivial `(I, 1.3 and 3.2)`.

In particular, if $U$ is an open of $Y$, one has, for every quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}$,

```text
  𝒯_•^U(ℳ | U) = (𝒯_•(ℳ)) | U.                                                (7.7.2.2)
```

**7.7.3.**

<!-- label: III.7.7.3 -->

For every quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}$, one has a canonical homomorphism, functorial in
$\mathcal{M}$:

```text
  𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ → 𝒯_p(ℳ).                                                (7.7.3.1)
```

Indeed, if $Y$ is affine, this homomorphism has been defined in `(7.2.2)`; this definition extends without difficulty to
the general case, by noting that if $U$, $V$ are two affine opens of $Y$ such that $V \subset U$, the diagram

<!-- original page 199 -->

```text
  (𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ) | U = 𝒯_p^U(𝒪_Y | U) ⊗_{𝒪_Y | U} (ℳ | U) → 𝒯_p^U(ℳ | U) = (𝒯_p(ℳ)) | U
                │                                                          │
                ↓                                                          ↓
  (𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ) | V = 𝒯_p^V(𝒪_Y | V) ⊗_{𝒪_Y | V} (ℳ | V) → 𝒯_p^V(ℳ | V) = (𝒯_p(ℳ)) | V
```

is commutative by `(7.2.3.3)`.

For every morphism $g : Y' \to Y$ one has a canonical homomorphism

```text
  𝒯_p(𝒪_Y) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒯_p^{Y'}(𝒪_{Y'})                                  (7.7.3.2)
```

which is none other than the particular case of `(6.7.11.2)` (for the abutments) in the case where $S = Y$, $v_{1} = f$,
$v_{2} = 1_{Y}$, $\mathcal{P}'^{(2)}_{\bullet}$ reduced to the single term $\mathcal{M}$ of degree `0`.

When $Y = \operatorname{Spec}(A)$, $Y' = \operatorname{Spec}(A')$ are affine, `(7.7.3.2)` is none other than the
homomorphism of sheaves corresponding to the canonical homomorphism of $A'$-modules defined in `(7.2.2)`

```text
  T_p^A(A) ⊗_A A' → T_p^{A'}(A') = T_p^A(A')
```

as easily results from `(6.7.11)` (since in the case envisaged, one can take $\mathfrak{U}'^{(i)} =
u^{-1}_{i}(\mathfrak{U}^{(i)})$ in `(6.7.11)`).

**7.7.4.**

<!-- label: III.7.7.4 -->

When $f$ is a *proper* morphism, $Y = \operatorname{Spec}(A)$ a noetherian affine scheme and $\mathcal{P}_{\bullet}$ a
complex of coherent and $Y$-flat $\mathcal{O}_{X}$-modules bounded below, we saw `(6.10.5)` that one can write up to an
isomorphism, $\mathcal{T}_{\bullet}(\mathcal{M}) = \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{\mathcal{O}_{Y}}
\mathcal{M})$, with $\mathcal{L}_{\bullet} = \tilde{L}_{\bullet}$, where $L_{\bullet}$ is a complex of free $A$-modules
of finite type bounded below; the functor $\mathcal{T}_{\bullet}$ is therefore of the type that has been studied in
detail in `(7.4)` and `(7.6)`. We are going to translate the results of this study:

**Theorem (7.7.5).**

<!-- label: III.7.7.5 -->

*Let $Y$ be a locally noetherian prescheme, $(U_{\alpha})$ an open affine cover of $Y$, $f : X \to Y$ a proper morphism,
$\mathcal{P}_{\bullet}$ a complex of coherent and $Y$-flat $\mathcal{O}_{X}$-modules bounded below. The homological
functor $\mathcal{T}_{\bullet}(\mathcal{M})$ defined by `(7.7.1.1)` then has the following properties:*

- *I) (The semi-continuity property) (¹). The function*
    ```text
      y ↦ d_p(y) = rang_{κ(y)} T_p^{κ(y)}(κ(y))                              (7.7.5.1)
    ```
    *is upper semi-continuous.*

<!-- original page 200 -->

- *II) (The exchange property). For a given integer $p$, the following conditions are equivalent:*
    - *a) $\mathcal{T}_{p}$ is right exact.*
    - *a') $\mathcal{T}_{p}(\mathcal{M})$ is isomorphic to a functor of the form $\mathcal{N} \otimes_{\mathcal{O}_{Y}}
      \mathcal{M}$ ($\mathcal{N}$ being necessarily isomorphic to $\mathcal{T}_{p}(\mathcal{O}_{Y}) =
      \mathcal{H}^{-p}(f, \mathcal{P}^{\bullet})$).*
    - *a'') The canonical functorial homomorphism `(7.7.3.1)` is an isomorphism.*
    - *b) $\mathcal{T}_{p-1}$ is left exact.*
    - *b') There exists an $\mathcal{O}_{Y}$-module $\mathcal{Q}$ (necessarily coherent, and determined up to unique
      isomorphism) and an isomorphism of functors*
        ```text
          𝒯_{p−1}(ℳ) ⥲ ℋom_{𝒪_Y}(𝒬, ℳ).                                       (7.7.5.2)
        ```
    - *c) Denoting by $A_{\alpha}$ the ring of the affine open $U_{\alpha}$, for every index $\alpha$ the functor of
      $A_{\alpha}$-modules $T^{A_{\alpha}}_{p}$ is right exact.*
    - *d) For every morphism $g : Y' \to Y$, the canonical homomorphism*
        ```text
          𝒯_p(𝒪_Y) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒯_p^{Y'}(𝒪_{Y'})                          (7.7.5.3)
        ```
        *is an isomorphism.*

> (¹) A particular case of this theorem is already found in note [3] of Chow–Igusa. The semi-continuity property has
> been discovered, in the context of analytic spaces (and under fairly particular hypotheses), by Kodaira–Spencer (*On
> the variations of almost-complex structures*, *Algebraic Geometry and Topology, A Symposium in honor of S. Lefschetz*,
> Princeton Series n° 12, p. 139–150, Princeton, 1957) and the general version proved by Grauert [5].

**Proof.** The semi-continuity property is local on $Y$ and therefore results from remark `(7.7.4)` and from `(7.6.9)`.
It is clear that a'') implies a') and that a') implies a). The equivalence of a), a''), b) and b') has been proved in
`(7.3.1)` and `(7.4.6)`, taking remark `(7.7.4)` into account, when $Y$ is affine. To pass to the general case, let us
first prove that a) is equivalent to c), which will prove the *local* character on $Y$ of property a); the proof will
likewise serve to prove the local character of a'') and b). Since it is clear that c) implies a), it all comes down to
proving the converse. It evidently suffices to show that for every affine open $U$ of $Y$ and every exact sequence $0
\to \mathcal{G}' \to \mathcal{G} \to \mathcal{G}'' \to 0$ of quasi-coherent $(\mathcal{O}_{Y} | U)$-modules, there
exists an exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ of quasi-coherent
$\mathcal{O}_{Y}$-modules such that $\mathcal{G}' = \mathcal{F}' | U$, $\mathcal{G} = \mathcal{F} | U$, $\mathcal{G}'' =
\mathcal{F}'' | U$; now, this results at once from the hypothesis that $Y$ is locally noetherian, and from `(I, 9.4.2)`:
one extends in fact $\mathcal{G}$ to a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{F}$, $\mathcal{G}'$ to a
sub-$\mathcal{O}_{X}$-module $\mathcal{F}'$ of $\mathcal{F}$, and it suffices to take $\mathcal{F}'' = \mathcal{F} /
\mathcal{F}'$.

To prove the equivalence of b) and b') in the general case, note that when $Y$ is affine, one knows that $\mathcal{Q}$
is determined up to unique isomorphism; if then $U$ is an affine open of the affine scheme $Y$, one concludes that there
exists a functorial isomorphism $\mathcal{T}_{p-1}(\mathcal{M} | U) \xrightarrow{\sim} \mathcal{H}om_{\mathcal{O}_{Y} |
U}(\mathcal{Q} | U, \mathcal{M} | U)$. In the general case, for every affine open $U$ of $Y$, there is a coherent
$(\mathcal{O}_{Y} | U)$-module $\mathcal{Q}_{U}$ and a functorial isomorphism $\mathcal{T}^{U}_{p-1}(\mathcal{M} | U)
\to \mathcal{H}om_{\mathcal{O}_{Y} | U}(\mathcal{Q}_{U}, \mathcal{M} | U)$; the preceding remark shows that if $V$ is an
affine open contained in $U$, one has $\mathcal{Q}_{U} | V = \mathcal{Q}_{V}$; whence the existence and uniqueness of
the $\mathcal{O}_{Y}$-module $\mathcal{Q}$ satisfying `(7.7.5.2)`.

It remains to show the equivalence of a) and d); it is clear that d) is of local character on $Y$, and one has seen
above that the same is true of a); moreover, d) is also local on $Y'$. Now, when $Y = \operatorname{Spec}(A)$, $Y' =
\operatorname{Spec}(A')$, one has seen that $T^{A'}_{p}$ is the functor obtained

<!-- original page 201 -->

from $T^{A}_{p}$ by extension of scalars to $A'$, and it is then clear that a') implies that `(7.7.5.3)` is an
isomorphism. Conversely, suppose still $Y = \operatorname{Spec}(A)$ affine and let $A'$ be the $A$-algebra $A \oplus M$,
where $M$ is an arbitrary $A$-module, the multiplication in $A'$ being given by $(a_{1}, m_{1})(a_{2}, m_{2}) = (a_{1}
a_{2}, a_{1} m_{2} + a_{2} m_{1})$; then

```text
  T_p^{A'}(A') = T_p(A ⊕ M) = T_p(A) ⊕ T_p(M),
```

and the hypothesis that `(7.7.5.3)` is bijective implies that the canonical map $T_{p}(A) \otimes_{A} M \to T_{p}(M)$ is
bijective, in other words d) implies a''), which completes the proof.

**Theorem (7.7.6).**

<!-- label: III.7.7.6 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{F}$ a coherent and $Y$-flat
$\mathcal{O}_{X}$-module. There exists then a coherent $\mathcal{O}_{Y}$-module $\mathcal{Q}$ (determined up to unique
isomorphism) and an isomorphism of functors in the quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}$:*

```text
  f_*(ℱ ⊗_{𝒪_Y} ℳ) ⥲ ℋom_{𝒪_Y}(𝒬, ℳ)                                        (7.7.6.1)
```

*(whence an isomorphism of functors*

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬, ℳ).)                                     (7.7.6.2)
```

**Proof.** Indeed, since $\mathcal{M} \mapsto \mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{M}$ is exact $(0_{I},
6.7.4)$ and $f_{*}$ is left exact, the functor $\mathcal{M} \mapsto f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{M})$ is left exact. It then suffices to apply the equivalence of `(7.7.5, b))` and `(7.7.5, b'))` for $p = 1$.

**Corollary (7.7.7).**

<!-- label: III.7.7.7 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{F}$, $\mathcal{F}'$ two coherent
and $Y$-flat $\mathcal{O}_{X}$-modules, $u : \mathcal{F} \to \mathcal{F}'$ a homomorphism. Consider the two functors in
the quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}$:*

```text
  𝒯(ℳ) = Ker(f_*(ℱ ⊗_{𝒪_Y} ℳ) → f_*(ℱ' ⊗_{𝒪_Y} ℳ))
  T(ℳ) = Γ(Y, 𝒯(ℳ)) = Ker(Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ)).
```

*Then there exists a coherent $\mathcal{O}_{Y}$-module $\mathcal{R}$ (determined up to unique isomorphism) and
isomorphisms of functors*

$$ \mathcal{T}(\mathcal{M}) \xrightarrow{\sim} \mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{R}, \mathcal{M}) (7.7.7.1)
T(\mathcal{M}) \xrightarrow{\sim} \operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{R}, \mathcal{M}). (7.7.7.2) $$

**Proof.** One can restrict to proving `(7.7.7.2)`; this will prove `(7.7.7.1)` in the case where $Y$ is affine, and one
will pass from there to the general case by reasoning as in the proof of the equivalence of `(7.7.5, b)` and `b')`,
thanks to the uniqueness up to unique isomorphism of a representative of a representable functor `(0, 8.1.8)`. It
follows from `(7.7.6)` that there exist two coherent $\mathcal{O}_{Y}$-modules $\mathcal{Q}$, $\mathcal{Q}'$ defining
functorial isomorphisms

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬, ℳ),   Γ(X, ℱ' ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬', ℳ).
```

Now, $u : \mathcal{F} \to \mathcal{F}'$ defines canonically a morphism of functors

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ);
```

<!-- original page 202 -->

to this corresponds a unique homomorphism $v : \mathcal{Q}' \to \mathcal{Q}$ of $\mathcal{O}_{Y}$-modules such that the
diagram

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ)
        │                    │
        ↓                    ↓
  Hom_{𝒪_Y}(𝒬, ℳ)   → Hom_{𝒪_Y}(𝒬', ℳ)
```

be commutative `(0, 8.1.4)`. Since the contravariant functor $\mathcal{N} \rightsquigarrow
\operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{N}, \mathcal{M})$ is left exact in the category of
$\mathcal{O}_{Y}$-modules, it suffices to take $\mathcal{R} = Coker(v)$ to obtain the isomorphism `(7.7.7.2)` sought.

**Corollary (7.7.8).**

<!-- label: III.7.7.8 -->

*Under the hypotheses of `(7.7.6)` relative to $X$, $Y$ and $f$, let $\mathcal{F}$, $\mathcal{G}$ be two coherent
$\mathcal{O}_{X}$-modules satisfying the following conditions: (i) $\mathcal{F}$ is $Y$-flat; (ii) $\mathcal{G}$ is
isomorphic to the cokernel of a homomorphism of locally free $\mathcal{O}_{X}$-modules of finite type $\mathcal{E}_{1}
\to \mathcal{E}_{0}$. Consider the two functors in the quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{M}$:*

```text
  𝒯(ℳ) = f_*(ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ))
  T(ℳ) = Γ(Y, 𝒯(ℳ)) = Hom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ).
```

*Then there exists a coherent $\mathcal{O}_{Y}$-module $\mathcal{N}$ (determined up to unique isomorphism) and
isomorphisms of functors*

$$ \mathcal{T}(\mathcal{M}) \xrightarrow{\sim} \mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{N}, \mathcal{M}) (7.7.8.1)
T(\mathcal{M}) \xrightarrow{\sim} \operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{N}, \mathcal{M}). (7.7.8.2) $$

**Proof.** By virtue of the functorial isomorphism $(0_{I}, 5.4.2.1)$, one has functorial isomorphisms in $\mathcal{E}$

```text
  ℋom_{𝒪_X}(ℰ_i, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Ě_i ⊗_{𝒪_X} (ℱ ⊗_{𝒪_Y} ℳ) ⥲ (Ě_i ⊗_{𝒪_X} ℱ) ⊗_{𝒪_Y} ℳ ⥲ ℋom_{𝒪_X}(ℰ_i, ℱ) ⊗_{𝒪_Y} ℳ
```

for $i = 0, 1$. Set $\mathcal{F}_{i} = \mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{E}_{i}, \mathcal{F})$ for $i = 0, 1$;
these are coherent $\mathcal{O}_{X}$-modules $(0_{I}, 5.3.5)$ and $Y$-flat $(0_{I}, 5.4.2)$; let $u = \mathcal{H}om(v,
1_{\mathcal{F}}) : \mathcal{F}_{0} \to \mathcal{F}_{1}$. By virtue of the left exactness of the functor $\mathcal{H}
\rightsquigarrow \mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{H}, \mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{M})$, one
has functorial isomorphisms in $\mathcal{M}$

```text
  ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Ker(ℋom_{𝒪_X}(ℰ_0, ℱ ⊗_{𝒪_Y} ℳ) → ℋom_{𝒪_X}(ℰ_1, ℱ ⊗_{𝒪_Y} ℳ)) ⥲
                                                                          Ker(ℱ_0 ⊗_{𝒪_Y} ℳ → ℱ_1 ⊗_{𝒪_Y} ℳ).
```

Since $f_{*}$ is left exact, one deduces a functorial isomorphism

```text
  f_*(ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ)) ⥲ Ker(f_*(ℱ_0 ⊗_{𝒪_Y} ℳ) → f_*(ℱ_1 ⊗_{𝒪_Y} ℳ))
```

and it then suffices to apply `(7.7.7)`.

<!-- original page 203 -->

**Remarks (7.7.9).**

<!-- label: III.7.7.9 -->

(i) In `(7.7.6)`, `(7.7.7)`, `(7.7.8)`, *the formation of the $\mathcal{O}_{Y}$-modules $\mathcal{Q}$, $\mathcal{R}$,
$\mathcal{N}$ commutes with base change*. For example (keeping the notations of `(7.7.2)`), in the case `(7.7.6)`, one
has, for every quasi-coherent $\mathcal{O}_{Y'}$-module $\mathcal{M}'$, the isomorphism

```text
  f'_*(ℱ' ⊗_{𝒪_{Y'}} ℳ') ⥲ ℋom_{𝒪_{Y'}}(g^*(𝒬), ℳ')
```

for, by virtue of the remark made in `(7.7.2)`, everything comes down to seeing that one has

```text
  Hom_{𝒪_Y}(𝒬, g_*(ℳ')) = Hom_{𝒪_{Y'}}(g^*(𝒬), ℳ')
```

which is none other than $(0_{I}, 4.4.3.1)$. Similarly, when in `(7.7.7)` one replaces $Y, f, \mathcal{M}, \mathcal{F},
\mathcal{F}'$ by $Y', f', \mathcal{M}', \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}, \mathcal{F}'
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$, one must replace $\mathcal{R}$ by $g^{*}(\mathcal{R})$. Finally, in
`(7.7.8)`, when one replaces $X, Y, f, \mathcal{M}, \mathcal{F}$ by $X', Y', f', \mathcal{M}', \mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$, and $\mathcal{G}$ by $\mathcal{G}' = \mathcal{G} \otimes_{\mathcal{O}_{X}}
\mathcal{O}_{X'}$, one must replace $\mathcal{N}$ by $g^{*}(\mathcal{N})$: this follows from the fact that one has again
an exact sequence $\mathcal{E}'_{1} \to \mathcal{E}'_{0} \to \mathcal{G}' \to 0$ with $\mathcal{E}'_{i} =
\mathcal{E}_{i} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$, and from the fact that $\check{E}'_{i}
\otimes_{\mathcal{O}_{X'}} (\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{M}') = \check{E}_{i}
\otimes_{\mathcal{O}_{X}} (\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{M}')$ ($i = 0, 1$).

(ii) Condition (ii) of the statement of `(7.7.8)` relative to $\mathcal{G}$ is always satisfied for an arbitrary
coherent $\mathcal{O}_{X}$-module $\mathcal{G}$ when there exists an invertible $Y$-ample $\mathcal{O}_{X}$-module, for
example when $Y$ is affine and $f : X \to Y$ is a projective morphism. It then suffices to note (taking `(II, 5.5.1)`
into account) that there exists a locally free $\mathcal{O}_{X}$-module of finite type $\mathcal{E}_{0}$ such that
$\mathcal{G}$ is isomorphic to a quotient of $\mathcal{E}_{0}$ `(II, 2.7.10)`; since $\mathcal{E}_{0}$ and $\mathcal{G}$
are coherent, the same is true of the kernel $\mathcal{E}_{1}$ of $\mathcal{E}_{0} \to \mathcal{G}$, and applying the
same result to $\mathcal{E}_{1}$, one indeed obtains an exact sequence $\mathcal{E}_{1} \to \mathcal{E}_{0} \to
\mathcal{G} \to 0$ where $\mathcal{E}_{0}$ and $\mathcal{E}_{1}$ are locally free of finite type.

(iii) We shall prove in chap. V that, in `(7.7.8)`, the restrictive hypothesis (ii) is superfluous.

**Proposition (7.7.10) (local criteria for the exchange property).**

<!-- label: III.7.7.10 -->

*Under the general conditions of `(7.7.5)`, let $y$ be a point of $Y$, $p$ an integer. The following properties are
equivalent:*

- *a) The functor $T^{\mathcal{O}_{y}}_{p}$ is right exact.*
- *b) The canonical homomorphism $T^{\mathcal{O}_{y}}_{p}(\mathcal{O}_{y}) \to T^{\mathcal{O}_{y}}_{p}(\kappa(y))$ is
  surjective.*
- *c) For every integer $n$, the canonical homomorphism $T^{\mathcal{O}_{y}}_{p}(\mathcal{O}_{y} /
  \mathfrak{m}^{n+1}_{y}) \to T^{\mathcal{O}_{y}}_{p}(\kappa(y))$ is surjective.*

*Moreover, the set of $y \in Y$ satisfying these conditions is the largest open $U$ of $Y$ such that
$\mathcal{T}^{U}_{p}$ is right exact.*

**Proof.** Taking `(7.7.4)` into account, the equivalence of a), b) and c) results from `(7.4.7)` and `(7.5.2)`. The
fact that the set $U$ where $T^{\mathcal{O}_{y}}_{p}$ is right exact is open is also a consequence of `(7.4.4)`, and
conversely if $\mathcal{T}^{U}_{p}$ is right exact, the same is true of $T^{\mathcal{O}_{y}}_{p}$ for every $y \in V$,
by condition c) of `(7.7.5)` and `(7.6.1)`.

**Corollary (7.7.11).**

<!-- label: III.7.7.11 -->

*If $\mathcal{T}_{p}$ is right exact (resp. left exact), then, for every morphism $g : Y' \to Y$, $\mathcal{T}^{Y'}_{p}$
is right exact (resp. left exact). The converse is true when the morphism $g$ is faithfully flat.*

<!-- original page 204 -->

**Proof.** The first assertion is an immediate consequence of `(7.6.1)` and the fact that the question is local on $Y$
and $Y'$, by `(7.7.5, c) and b))`. To prove the second assertion, it suffices to see that for every $y \in Y$,
$T^{\mathcal{O}_{y}}_{p}$ is right exact (resp. left exact), by virtue of `(7.7.10)`. But by hypothesis, there exists
$y' \in Y'$ such that $g(y') = y$, and $\mathcal{O}_{y'}$ is a faithfully flat $\mathcal{O}_{y}$-module; the conclusion
then results from the hypothesis and from `(7.6.1)`.

**Remarks (7.7.12).**

<!-- label: III.7.7.12 -->

(i) Under the hypotheses of `(7.7.4)`, suppose moreover that $\mathcal{P}_{\bullet}$ is a *finite* complex; then it
results from `(7.7.1)` (since one can take for $\mathfrak{U}$ a finite affine open cover of $X$) that the bicomplex
$C^{\bullet}(\mathfrak{U}, \mathcal{P}^{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{M})$ is also finite, and more
precisely that there exists a finite set $E$ of pairs, independent of $\mathcal{M}$, such that $C^{h}(\mathfrak{U},
\mathcal{P}^{k} \otimes_{\mathcal{O}_{X}} \mathcal{M}) = 0$ for all pairs $(h, k) \notin E$. One concludes that there
exists $i_{1}$ such that, for $i \geq i_{1}$, one has $\mathcal{T}_{i}(\mathcal{M}) = 0$ for every quasi-coherent
$\mathcal{O}_{Y}$-module $\mathcal{M}$. In particular, $\mathcal{T}_{i}$ is trivially an exact functor in $\mathcal{M}$
for these values of $i$, and consequently `(7.4.1)`, $Z'_{i_{1}}(L_{\bullet})$ is a flat $A$-module of finite type
(hence projective of finite type, since $A$ is noetherian) for these values of $i$. Consider then the complex $(L'_{i})$
of $A$-modules such that $L'_{i} = L_{i}$ for $i < i_{1}$, $L'_{i_{1}} = Z'_{i_{1}}(L_{\bullet})$ and $L'_{i} = 0$ for
$i > i_{1}$ and let $\mathcal{L}'_{\bullet} = \tilde{L}'_{\bullet}$. It is clear that
$\mathcal{H}_{i}(\mathcal{L}'_{\bullet} \otimes_{\mathcal{O}_{Y}} \mathcal{M}) = \mathcal{H}_{i}(\mathcal{L}_{\bullet}
\otimes_{\mathcal{O}_{Y}} \mathcal{M})$ for $i < i_{1} - 1$ and also for $i \geq i_{1}$ (the two members being then
zero); finally, since $Im(Z'_{i_{1}} \otimes_{A} M) = Im(L_{i_{1}} \otimes_{A} M)$ by definition, one also has
$\mathcal{H}_{i}(\mathcal{L}'_{\bullet} \otimes_{\mathcal{O}_{Y}} \mathcal{M}) = \mathcal{H}_{i}(\mathcal{L}_{\bullet}
\otimes_{\mathcal{O}_{Y}} \mathcal{M})$ for $i = i_{1} - 1$. One thus sees that one can suppose in `(7.7.4)` that
$\mathcal{L}_{\bullet}$ is also a *finite* complex, on condition of requiring only that the $\mathcal{L}_{i}$ be locally
free $\mathcal{O}_{Y}$-modules (associated with projective $A$-modules of finite type).

This reasoning applies in particular to the case where $\mathcal{P}_{\bullet}$ is reduced to a single term $\mathcal{F}
\neq 0$, of degree `0` (in which case $\mathcal{T}_{n}(\mathcal{E}) = R^{-n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{E})$); one can then suppose that the $\mathcal{L}_{i}$ are zero for $i > 0$; one will use preferentially in
this case the cohomological notations, thus writing $\mathcal{T}^{-p}$ instead of $\mathcal{T}_{p}$.

(ii) When in the statement of `(7.7.5)` one no longer supposes that the $\mathcal{P}_{i}$ are $Y$-flat, the conclusions
remain valid on condition that one sets this time

```text
  𝒯_p(ℰ) = 𝒯or_n^Y(f, 1_Y; 𝒫_•, ℰ).                                          (7.7.12.1)
```

Indeed, $\mathcal{T}or^{Y}_{n}(f, 1_{Y}; \mathcal{P}_{\bullet}, \mathcal{O}_{Y})$ is then a coherent
$\mathcal{O}_{Y}$-module by virtue of `(6.7.9)`. The proof of `(6.10.5)` applies without change, taking `(6.10.1)` into
account, and shows again that when $Y = \operatorname{Spec}(A)$ is affine, one has $\mathcal{T}_{p}(\mathcal{E}) =
\mathcal{H}_{p}(\mathcal{L}_{\bullet} \otimes_{\mathcal{O}_{Y}} \mathcal{E})$, with $\mathcal{L}_{\bullet} =
\tilde{L}_{\bullet}$, where $L_{\bullet}$ is a complex of free $A$-modules of finite type; this proves our assertion.

## 7.8. Application to proper morphisms: II. Cohomological flatness criteria

**Definition (7.8.1).**

<!-- label: III.7.8.1 -->

*Let $X$, $Y$ be two preschemes, $f : X \to Y$ a quasi-compact and separated morphism, $\mathcal{P}_{\bullet}$ a complex
of quasi-coherent and $Y$-flat $\mathcal{O}_{X}$-modules, $\mathcal{T}_{\bullet}$ the homological functor of
quasi-coherent*

<!-- original page 205 -->

*$\mathcal{O}_{Y}$-modules defined by `(7.7.1.1)`, $y$ a point of $Y$. One says that $\mathcal{P}_{\bullet}$ is*
homologically flat over $Y$ at the point $y$, in dimension $p$ *(or* cohomologically flat over $Y$ at the point $y$, in
dimension $-p$*) if there exists an open neighbourhood $U$ of $y$ in $Y$ such that $\mathcal{T}^{U}_{p} =
\mathcal{T}^{-p}_{U}$ is exact. One says that $\mathcal{P}_{\bullet}$ is* homologically flat in dimension $p$ over $Y$
*(or* cohomologically flat in dimension $-p$ over $Y$*) if it is homologically flat over $Y$ at every point $y \in Y$,
in dimension $p$.*

*When $\mathcal{P}_{\bullet}$ is homologically flat over $Y$ (resp. over $Y$ at the point $y$) for every dimension $p$,
one says simply that $\mathcal{P}_{\bullet}$ is* homologically flat over $Y$ *(resp. over $Y$ at the point $y$) or*
cohomologically flat over $Y$ *(resp. over $Y$ at the point $y$).*

**7.8.2.**

<!-- label: III.7.8.2 -->

By definition, the notion of homological flatness over $Y$ is *local* on $Y$. If $Y$ is locally noetherian, or a scheme,
for $\mathcal{P}_{\bullet}$ to be homologically flat over $Y$ in dimension $p$, it is necessary and sufficient that the
functor $\mathcal{T}_{p}$ be exact: the proof has been done in the case where $Y$ is locally noetherian in the course of
the proof of `(7.7.5)`; the reasoning is the same (based on `(I, 9.4.2)` applied to an affine open in a quasi-compact
scheme) when $Y$ is a scheme.

**Proposition (7.8.3).**

<!-- label: III.7.8.3 -->

*The notations and hypotheses being those of `(7.8.1)`, the following conditions are equivalent:*

- *a) $\mathcal{P}_{\bullet}$ is homologically flat over $Y$ at the point $y$ in dimension $p$.*
- *b) There exists an open neighbourhood $U$ of $y$ in $Y$ such that $\mathcal{T}^{U}_{p}$ and $\mathcal{T}^{U}_{p+1}$
  are right exact.*
- *c) There exists an open neighbourhood $U$ of $y$ in $Y$ such that $\mathcal{T}^{U}_{p}$ and $\mathcal{T}^{U}_{p-1}$
  are left exact.*
- *d) There exists an open neighbourhood $U$ of $y$ in $Y$ such that $\mathcal{T}^{U}_{p+1}$ is right exact and
  $\mathcal{T}^{U}_{p-1}$ is left exact.*

**Proof.** Taking the interpretation of $\mathcal{T}_{p}$ when $Y$ is affine into account, this is but a translation of
part of `(7.3.3)`.

**Proposition (7.8.4).**

<!-- label: III.7.8.4 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{P}_{\bullet}$ a complex of
coherent and $Y$-flat $\mathcal{O}_{X}$-modules bounded below, $\mathcal{T}_{\bullet}$ the functor defined by
`(7.7.1.1)`. For every $y \in Y$, the following conditions are equivalent:*

- *a) $\mathcal{P}_{\bullet}$ is homologically flat over $Y$ at $y$ in dimension $p$.*
- *b) The functor $T^{\mathcal{O}_{y}}_{p}$ is exact.*
- *c) There exists an integer $n_{0}$ such that for $n \geq n_{0}$, one has*
    ```text
      long T_p^{𝒪_y}(𝒪_y / 𝔪_y^{n+1}) = long T_p^{𝒪_y}(κ(y)) · long 𝒪_y / 𝔪_y^{n+1}     (7.8.4.1)
    ```
    *(where one is dealing with lengths of $\mathcal{O}_{y}$-modules).*
- *d) There is an open neighbourhood $U$ of $y$ such that $(\mathcal{H}^{-p}(f, \mathcal{P}^{\bullet})) | U$ is
  isomorphic to a $(\mathcal{O}_{Y} | U)$-module of the form $(\mathcal{O}_{Y} | U)^{m}$ and such that, for every
  quasi-coherent $(\mathcal{O}_{Y} | U)$-module $\mathcal{M}$, the canonical homomorphism*
    ```text
      ((ℋ^{−p}(f, 𝒫^•)) | U) ⊗_{𝒪_Y | U} ℳ → ℋ^{−p}(f, (𝒫^• | U) ⊗_{𝒪_Y | U} ℳ)         (7.8.4.2)
    ```
    *is bijective.*

*When these conditions are satisfied, one has moreover the following property:*

- *e) There exists a neighbourhood of $y$ in which the function $z \mapsto d_{p}(z)$ (defined in `(7.7.5.1)`) is
  constant.*

*Moreover, if $Y$ is reduced at the point $y$ $(0_{I}, 4.1.4)$, e) is equivalent to the other conditions.*

<!-- original page 206 -->

**Proof.** Indeed, condition b) is equivalent to saying that $T^{\mathcal{O}_{y}}_{p}$ and $T^{\mathcal{O}_{y}}_{p+1}$
are right exact `(7.3.3)`. The equivalence of a) and b) results then from `(7.7.10)` and `(7.8.3)`. Since
$\mathcal{O}_{y} / \mathfrak{m}^{n+1}_{y}$ is artinian, and $T^{\mathcal{O}_{y}}_{p}(\mathcal{O}_{y} /
\mathfrak{m}^{n+1}_{y})$ and $T^{\mathcal{O}_{y}}_{p}(\kappa(y))$ are $(\mathcal{O}_{y} /
\mathfrak{m}^{n+1}_{y})$-modules of finite type `(7.7.4)`, hence of finite length, the equivalence of b) and c) again
results from `(7.7.10)` and from `(7.3.5.7)`. The fact that a) implies e), and is equivalent to it when
$\mathcal{O}_{y}$ is reduced, is a consequence of `(7.6.9)`. Finally, a) implies that `(7.8.4.2)` is bijective by virtue
of definition `(7.8.1)` and of `(7.7.5)`; on the other hand, a) implies that $(\mathcal{H}^{-p}(f,
\mathcal{P}^{\bullet}))_{y}$ is a flat $\mathcal{O}_{y}$-module `(7.3.3, f)`, hence free `(0, 10.1.3)`, since it is an
$\mathcal{O}_{y}$-module of finite type by virtue of `(7.7.4)`; since $\mathcal{H}^{-p}(f, \mathcal{P}^{\bullet})$ is a
coherent $\mathcal{O}_{Y}$-module `(7.7.4)`, it is locally free in a neighbourhood of $y$ $(0_{I}, 5.2.7)$. Conversely,
it is clear that d) implies a) by definition of the functor $\mathcal{T}^{U}_{p}$ `(7.7.2.2)`.

**Proposition (7.8.5).**

<!-- label: III.7.8.5 -->

*Under the hypotheses of `(7.8.4)`, the following conditions are equivalent:*

- *a) $\mathcal{P}_{\bullet}$ is homologically flat over $Y$ in every dimension $i \leq p$.*
- *b) For $i \leq p + 1$ the functors $\mathcal{T}_{i}$ are right exact.*
- *c) For $i \geq -p$, the $\mathcal{O}_{Y}$-modules $\mathcal{H}^{i}(f, \mathcal{P}^{\bullet})$ are locally free.*

**Proof.** The equivalence of a) and b) is trivial `(7.8.3)` and a) implies c) by virtue of `(7.8.4)`. Conversely,
suppose c) verified, note on the other hand that one has $\mathcal{L}_{i} = 0$ for $i \leq i_{0}$ `(7.7.4)`, hence also
$\mathcal{T}_{i} = 0$ for $i \leq i_{0}$. Every point $y \in Y$ has therefore an affine neighbourhood $U =
\operatorname{Spec}(A)$ such that $T^{A}_{i}(A)$ is a free $A$-module for $i \leq p$; by virtue of `(7.3.7)`, one
concludes that $\mathcal{T}^{U}_{i} = T^{A}_{i}$ is exact for $i \leq p$.

We shall mainly apply the cohomological flatness criteria to the case where the complex $\mathcal{P}_{\bullet}$ is
reduced to a single coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ flat over $Y$, taken equal to $\mathcal{P}_{0}$;
recall that one has then $\mathcal{T}_{n}(\mathcal{M}) = R^{-n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{M})$.

**Proposition (7.8.6).**

<!-- label: III.7.8.6 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper and flat morphism, $y$ a point of $Y$; denote by
$X_{y}$ the fibre $f^{-1}(y) = X \otimes_{Y} \kappa(y)$. Suppose that $\Gamma(X_{y}, \mathcal{O}_{X_{y}}) = R$ is a
separable $\kappa(y)$-algebra (Bourbaki, *Alg.*, chap. VIII, § 7, n° 5), that is, composed of a finite number of
separable extensions of finite degree of $\kappa(y)$. Then $\mathcal{O}_{X}$ is cohomologically flat over $Y$ at the
point $y$ in dimension `0`.*

**Proof.** By virtue of `(7.8.4)`, one can restrict to the case where $Y$ is the spectrum of the local ring $A =
\mathcal{O}_{y}$; the hypothesis that $f$ is flat implies $\mathcal{T}_{-1} = 0$, hence one already sees that
$T^{A}_{0}$ is left exact and it all comes down to seeing that it is right exact; by virtue of `(7.7.10, c))`, one is
even reduced to the case where $A = \mathcal{O}_{y}$ is artinian. Let $k'$ be a finite extension of $\kappa(y)$ which is
a splitting field of $R$, so that $R \otimes_{\kappa(y)} k'$ is the direct sum of a finite number of fields isomorphic
to $k'$. We know that there exists a local homomorphism of $A$ into a local ring $A'$, making $A'$ a finite free
$A$-algebra, and such that the residue field of $A'$ is isomorphic to $k'$ `(0, 10.3.2)`. By virtue of `(7.6.1)`, one is
reduced to proving that $T^{A'}_{0}$ is right exact, in other words one can suppose that $R$ is the direct sum of $m$
fields isomorphic to $\kappa(y)$. Let us now note the following elementary lemma:

**Lemma (7.8.6.1).**

<!-- label: III.7.8.6.1 -->

*Let $Z$ be a space ringed in local rings; for $Z$ to be connected, it is necessary*

<!-- original page 207 -->

*and sufficient that the ring $\Gamma(Z, \mathcal{O}_{Z})$ not be a product of two rings not reduced to `0`.*

**Proof.** It is clear in fact that if $Z$ is the union of two non-empty disjoint opens, $\Gamma(Z, \mathcal{O}_{Z})$ is
isomorphic to the product of the two rings $\Gamma(Z_{1}, \mathcal{O}_{Z})$ and $\Gamma(Z_{2}, \mathcal{O}_{Z})$ not
reduced to `0`. Conversely, to say that $\Gamma(Z, \mathcal{O}_{Z})$ is such a product amounts to saying that there is
in $\Gamma(Z, \mathcal{O}_{Z})$ an idempotent $s$ distinct from `0` and `1`; for every $z \in Z$, $s_{z}$ is then an
idempotent in $\mathcal{O}_{z}$, hence equal to `0` or `1`. But it is clear that the set of $z$ such that $s_{z} = 0$ is
open; on the other hand, if $s_{z} = 1$, one has by definition $s(z) \neq 0$, hence the set of $z$ where $s_{z} = 1$ is
also open $(0_{I}, 5.5.2)$; whence the conclusion.

It results from this lemma that $X_{y}$ has exactly $m$ connected components $X'_{i}$ and that $\Gamma(X'_{i},
\mathcal{O}_{X'_{i}}) = \kappa(y)$ for every $i$. Since $A$ was supposed local and artinian, its spectrum is reduced to
a point, hence $X$ and $X_{y}$ have the same underlying space; $X$ therefore has $m$ connected components $X_{i}$ such
that $X'_{i} = X_{i} \otimes_{Y} \kappa(y)$. One is thus finally reduced to the case where $R = \kappa(y)$; by virtue of
`(7.7.10, b))`, one is reduced to proving that the canonical homomorphism $\Gamma(X, \mathcal{O}_{X}) \to \Gamma(X_{y},
\mathcal{O}_{X_{y}})$ is surjective; but this is trivial, since the composite

```text
  Γ(Y, 𝒪_Y) = A → Γ(X, 𝒪_X) → Γ(X_y, 𝒪_{X_y}) = κ(y)
```

is already surjective.

**Corollary (7.8.7).**

<!-- label: III.7.8.7 -->

*Under the hypotheses of `(7.8.6)`, there exists an open neighbourhood $U$ of $y$ such that:*

- *(i) $f_{*}(\mathcal{O}_{X}) | U$ is isomorphic to a $(\mathcal{O}_{Y} | U)$-module of the form $(\mathcal{O}_{Y} |
  U)^{m}$.*
- *(ii) For every $z \in U$, the canonical homomorphism*
    ```text
      (f_*(𝒪_X))_z ⊗_{𝒪_z} κ(z) → Γ(X_z, 𝒪_{X_z})
    ```
    *is bijective.*

**Proof.**

(i) follows from `(7.8.6)` and `(7.8.4)`.

(ii) follows from the fact that $\mathcal{T}^{U}_{0}$ is exact (for $U$ suitably chosen), and from `(7.7.5.3)`.

**Corollary (7.8.8).**

<!-- label: III.7.8.8 -->

*Suppose the conditions of `(7.8.6)` satisfied and moreover that $\Gamma(X_{y}, \mathcal{O}_{X_{y}}) = \kappa(y)$. Then
there exists an open neighbourhood $U$ of $y$ such that the canonical homomorphism $\mathcal{O}_{Y} | U \to
f_{*}(\mathcal{O}_{X}) | U$ is bijective.*

**Proof.** Indeed, it follows from `(7.8.7, (ii))` that the integer $m$ appearing in `(7.8.7, (i))` is necessarily equal
to `1`.

**Corollary (7.8.9).**

<!-- label: III.7.8.9 -->

*Under the hypotheses of `(7.8.6)`, there exists an open neighbourhood $U$ of $y$, a coherent $\mathcal{O}_{U}$-module
$\mathcal{Q}$ (determined up to unique isomorphism) and an isomorphism of functors in the quasi-coherent
$\mathcal{O}_{U}$-module $\mathcal{M}$:*

```text
  R^1 f_*(f^*(ℳ)) ⥲ ℋom_{𝒪_U}(𝒬, ℳ).                                         (7.8.9.1)
```

**Proof.** Indeed, the hypothesis implies that $\mathcal{T}^{U}_{0}$ is exact for a suitable $U$; it therefore suffices
to apply the equivalence of `(7.7.5, a))` and `(7.7.5, b'))` in the case $p = 0$ and taking for $\mathcal{P}_{\bullet}$
the complex reduced to its term of degree `0` equal to $\mathcal{O}_{X}$.

**Remarks (7.8.10).**

<!-- label: III.7.8.10 -->

(i) Under the conditions of `(7.8.6)`, consider the Stein factorization of $f$ `(4.3.3)`

```text
  X →^{f'} Y' →^g Y
```

<!-- original page 208 -->

with $Y' = \operatorname{Spec}(f_{*}(\mathcal{O}_{X}))$; the finite morphism $g$ is then such that
$g_{*}(\mathcal{O}_{Y'}) = f_{*}(\mathcal{O}_{X})$ is locally free in a neighbourhood of $y$, and its fibre at $y$ is
the spectrum of a separable algebra over $\kappa(y)$ `(II, 1.5.1)`. We shall deduce in chap. IV that there is an open
neighbourhood $U$ of $y$ in $Y$ such that for the restriction $g^{-1}(U) \to U$ of $g$, every fibre $g^{-1}(z)$ (where
$z \in U$) is the spectrum of a separable algebra over $\kappa(z)$ (this is what we shall call an *étale cover* of $U$);
it will then result from `(7.8.7, (ii))` that the hypothesis made on the point $y$ in `(7.8.6)` is satisfied also at
every point of a neighbourhood of $y$.

(ii) We shall see in chap. V that, even if $X$ is projective over $Y$ (and even if it is moreover "smooth" over $Y$, a
property which will be defined in chap. IV), the $\mathcal{O}_{Y}$-module $\mathcal{Q}$ of `(7.8.9)` is not necessarily
locally free; in other words, $\mathcal{O}_{X}$ (under these conditions) is not necessarily cohomologically flat in
dimension 1 over $Y$ at the point $y$. In chap. V, we shall interpret $\mathcal{Q}$ as the sheaf of 1-differentials of
the Picard scheme of $X$ with respect to $Y$ along the unit section.

## 7.9. Application to proper morphisms: III. Invariance of the Euler–Poincaré characteristic and the Hilbert polynomial

**7.9.1.**

<!-- label: III.7.9.1 -->

Let $A$ be a ring, $M$ a projective $A$-module of finite type; recall (Bourbaki, *Alg. comm.*, chap. II, § 5, n° 2) that
it amounts to the same to say that the $\mathcal{O}_{X}$-module $\tilde{M}$ associated on $X = \operatorname{Spec}(A)$
is locally free of finite type. For every $\mathfrak{p} \in \operatorname{Spec}(A)$ one calls *rank of $M$ at*
$\mathfrak{p}$ and one denotes by $rang_{\mathfrak{p}}(M)$ the rank of the free $A_{\mathfrak{p}}$-module
$M_{\mathfrak{p}}$ (or equivalently the rank at $\mathfrak{p}$ of the locally free $\mathcal{O}_{X}$-module
$\tilde{M}$). One has therefore

```text
  rang_𝔭 M = rang_{A_𝔭}(M_𝔭) = rang_{κ(𝔭)}(M ⊗_A κ(𝔭)).                       (7.9.1.1)
```

**Proposition (7.9.2).**

<!-- label: III.7.9.2 -->

*Let $P_{\bullet}$ be a finite complex of projective $A$-modules of finite type, and for every $A$-module $M$, let
$T_{\bullet}(M) = H_{\bullet}(P_{\bullet} \otimes_{A} M)$. Then, for every $\mathfrak{p} \in \operatorname{Spec}(A)$,
one has*

```text
  Σ_i (−1)^i rang_{κ(𝔭)} T_i(κ(𝔭)) = Σ_i (−1)^i rang_𝔭(P_i).                 (7.9.2.1)
```

**Proof.** Indeed, one has by definition $T_{i}(\kappa(\mathfrak{p})) = H_{i}(P_{\bullet} \otimes_{A}
\kappa(\mathfrak{p}))$ and, taking `(7.9.1.1)` into account, formula `(7.9.2.1)` is none other than the invariance of
the Euler–Poincaré characteristic of a finite complex of finite-dimensional vector spaces under passage to homology
`(0, 11.10.2)`.

**Corollary (7.9.3).**

<!-- label: III.7.9.3 -->

*The function*

```text
  𝔭 ↦ Σ_i (−1)^i rang_{κ(𝔭)} T_i(κ(𝔭))
```

*is locally constant on $\operatorname{Spec}(A)$.*

**Theorem (7.9.4).**

<!-- label: III.7.9.4 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{P}_{\bullet}$ a finite complex of
coherent and $Y$-flat $\mathcal{O}_{X}$-modules. If one sets $\mathcal{T}_{\bullet}(\mathcal{M}) =
\mathcal{H}^{\bullet}(f, \mathcal{P}^{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{M})$ (cf. `(7.7.1.1)`), the function*

<!-- original page 209 -->

```text
  y ↦ Σ_i (−1)^i rang_{κ(y)} T_i(κ(y))                                       (7.9.4.1)
```

*is locally constant on $Y$.*

**Proof.** One can restrict to the case where $Y = \operatorname{Spec}(A)$ is affine with noetherian ring $A$. Since the
complex $\mathcal{P}_{\bullet}$ is finite, one knows `(7.7.12, (i))` that one has $\mathcal{T}_{p}(\mathcal{M}) =
\mathcal{H}_{p}(\mathcal{L}_{\bullet} \otimes_{\mathcal{O}_{Y}} \mathcal{M})$, where $\mathcal{L}_{\bullet} =
\tilde{L}_{\bullet}$, $L_{\bullet}$ being a finite complex of projective $A$-modules of finite type. The theorem then
results from `(7.9.3)`.

**7.9.5.**

<!-- label: III.7.9.5 -->

Under the conditions of `(7.9.4)`, the function `(7.9.4.1)` is constant when $Y$ is connected. When $Y$ is connected and
non-empty, one denotes the unique (integer) value of `(7.9.4.1)` by $EP(f, \mathcal{P}_{\bullet})$ or $EP(Y,
\mathcal{P}_{\bullet})$, or simply $EP(\mathcal{P}_{\bullet})$ if there can be no confusion, and one says that this
integer is the *Euler–Poincaré characteristic of $\mathcal{P}_{\bullet}$ relative to $f$* (or to $Y$). In the general
case, one will also denote $EP(f, \mathcal{P}_{\bullet}; y)$ or $EP(Y, \mathcal{P}_{\bullet}; y)$ or
$EP(\mathcal{P}_{\bullet}; y)$ the second member of `(7.9.4.1)`.

**7.9.6.**

<!-- label: III.7.9.6 -->

Under the hypotheses of `(7.9.4)` relative to $X$, $Y$ and $f$, let

```text
  0 → 𝒫'_• →^u 𝒫_• →^v 𝒫''_• → 0
```

be an exact sequence of finite complexes of coherent and $Y$-flat $\mathcal{O}_{X}$-modules, the homomorphisms $u$ and
$v$ being of *even* degrees `2d`, `2d'` respectively. Since $\mathcal{T}_{\bullet}$ is a homological functor `(7.7.1)`,
one has an exact sequence of homology

```text
  → 𝒯_i(𝒫'_•, κ(y)) → 𝒯_{i+2d}(𝒫_•, κ(y)) → 𝒯_{i+2d'}(𝒫''_•, κ(y)) → 𝒯_{i−1}(𝒫'_•, κ(y)) → …
```

having moreover only a finite number of terms. By writing that the Euler–Poincaré characteristic of this complex is zero
`(0, 11.10.1)`, it follows at once

```text
  EP(𝒫_•; y) = EP(𝒫'_•; y) + EP(𝒫''_•; y)                                    (7.9.6.1)
```

for every $y \in Y$. Now, if for example $\mathcal{P}_{\bullet} = (\mathcal{P}_{i})$ with $\mathcal{P}_{i} = 0$ for $i <
0$, one has the exact sequence of complexes

$$ \cdots \to 0 \to 0 \to 0 \to 0 \to \cdots \downarrow \downarrow \downarrow \cdots \to 0 \to 0 \to \mathcal{P}_{1} \to
\mathcal{P}_{2} \to \cdots \downarrow \downarrow \downarrow \downarrow \cdots \to 0 \to \mathcal{P}_{0} \to
\mathcal{P}_{1} \to \mathcal{P}_{2} \to \cdots \downarrow \downarrow \downarrow \downarrow \cdots \to 0 \to
\mathcal{P}_{0} \to 0 \to 0 \to \cdots \downarrow \downarrow \downarrow \cdots \to 0 \to 0 \to 0 \to 0 \to \cdots $$

the non-zero vertical arrows being the identity automorphisms; one can apply `(7.9.6.1)` to this exact sequence, whence,
by induction on the length of $\mathcal{P}_{\bullet}$, the formula

```text
  EP(𝒫_•; y) = Σ_i (−1)^i EP(𝒫_i; y)                                         (7.9.6.2)
```

<!-- original page 210 -->

where, for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, flat on $Y$, one denotes by $EP(\mathcal{F}; y)$ (or
$EP(f, \mathcal{F}; y)$ or $EP(Y, \mathcal{F}; y)$) the function $EP(\mathcal{P}_{\bullet}; y)$ corresponding to the
complex $\mathcal{P}_{\bullet}$ whose only term $\neq 0$ is of degree `0` and equal to $\mathcal{F}$. One thus sees that
one can reduce to studying the Euler–Poincaré characteristics of complexes reduced to a single term.

**Proposition (7.9.7).**

<!-- label: III.7.9.7 -->

*Under the hypotheses of `(7.9.4)`, let $Y'$ be a locally noetherian prescheme, $g : Y' \to Y$ a morphism, $X' = X
\times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, $\mathcal{P}'_{\bullet}$ the finite complex $\mathcal{P}_{\bullet}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$ of $\mathcal{O}_{X'}$-modules; $\mathcal{P}'_{\bullet}$ is formed of
coherent and $Y'$-flat $\mathcal{O}_{X'}$-modules, and for every $y' \in Y'$, one has*

```text
  EP(𝒫'_•; y') = EP(𝒫_•; g(y')).                                             (7.9.7.1)
```

**Proof.** The $\mathcal{O}_{X'}$-modules $\mathcal{P}'_{i}$, being inverse images of the $\mathcal{P}_{i}$ by the
projection $X' \to X$, are coherent, they are $Y'$-flat by virtue of $(0_{I}, 6.2.1)$ and `(1.4.14.5)`, the question
being local on $X$, $Y$ and $Y'$; finally, one knows that $f'$ is proper `(II, 5.4.2)`, hence the first member of
`(7.9.7.1)` is defined. Formula `(7.9.7.1)` then results from `(6.10.4.2)`, `(7.7.2)` and from lemma `(7.6.7)`, by
reducing, as one can always do, to the case where $Y$ and $Y'$ are affine.

**Proposition (7.9.8).**

<!-- label: III.7.9.8 -->

*Suppose the hypotheses of `(7.9.4)` satisfied and moreover that there exists an integer $i_{0}$ such that
$T_{i}(\kappa(y)) = 0$ for $i \neq i_{0}$ and every $y \in Y$. Then $\mathcal{T}_{i_{0}}(\mathcal{O}_{Y}) =
\mathcal{H}^{-i_{0}}(f, \mathcal{P}^{\bullet})$ is a locally free $\mathcal{O}_{Y}$-module, whose rank at $y \in Y$ is
equal to $(-1)^{i_{0}} EP(f, \mathcal{P}_{\bullet}; y)$.*

**Proof.** Note first that the hypotheses of `(7.4.4)` are satisfied by the $T^{\mathcal{O}_{y}}_{\bullet}$, hence
`(7.4.7)` is applicable to them, and the hypothesis implies that $T^{\mathcal{O}_{y}}_{i}$ is zero for $i \neq i_{0}$ by
virtue of `(7.5.3)`; in view of `(7.3.3)`, $\mathcal{T}_{i_{0}}$ is therefore also exact, and consequently `(7.8.4)`,
$\mathcal{H}^{-i_{0}}(f, \mathcal{P}^{\bullet})$ is locally free and its rank at a point $y \in Y$ is

```text
  rang_{κ(y)} T_{i_0}(κ(y)) = EP(f, 𝒫_•; y)
```

by definition, since $T_{i}(\kappa(y)) = 0$ for $i \neq i_{0}$.

**Corollary (7.9.9).**

<!-- label: III.7.9.9 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{F}$ a coherent and $Y$-flat
$\mathcal{O}_{X}$-module; suppose that there exists an integer $i_{0}$ such that $H^{i}(f^{-1}(y), \mathcal{F}
\otimes_{\mathcal{O}_{X}} \kappa(y)) = 0$ for every $i \neq i_{0}$ and every $y \in Y$. Then $R^{i_{0}}
f_{*}(\mathcal{F})$ is a locally free $\mathcal{O}_{Y}$-module, whose rank at $y$ is equal to $(-1)^{i_{0}} EP(f,
\mathcal{F}; y)$.*

In particular:

**Corollary (7.9.10).**

<!-- label: III.7.9.10 -->

*Under the preliminary conditions of `(7.9.9)` for $X$, $Y$ and $\mathcal{F}$, suppose that one has $R^{i}
f_{*}(\mathcal{F}) = 0$ for every $i > 0$. Then $f_{*}(\mathcal{F})$ is a locally free $\mathcal{O}_{Y}$-module, whose
rank at $y$ is equal to $EP(f, \mathcal{F}; y)$.*

**Proof.** It will suffice, by virtue of `(7.9.9)`, to prove the following lemma:

**Lemma (7.9.10.1).**

<!-- label: III.7.9.10.1 -->

*Under the hypotheses of `(7.9.10)`, one has $H^{i}(f^{-1}(y), \mathcal{F} \otimes_{\mathcal{O}_{X}} \kappa(y)) = 0$ for
every $i > 0$ and every $y \in Y$.*

**Proof.** Indeed, one can restrict to the case where $Y = \operatorname{Spec}(A)$ is affine. With the notations of
`(7.9.4)`, and $\mathcal{P}_{\bullet}$ being reduced to its term of degree `0` equal to $\mathcal{F}$, one has indeed
$\mathcal{T}_{p}(\mathcal{O}_{Y}) = 0$ for $p < 0$ by hypothesis; one concludes from `(7.3.7)` that $\mathcal{T}_{p}$ is
exact for $p < 0$, and the lemma results then from the equivalence of `(7.7.5, a))` and `(7.7.5, d))`.

<!-- original page 211 -->

**Proposition (7.9.11).**

<!-- label: III.7.9.11 -->

*The hypotheses being those of `(7.9.4)`, let $\mathcal{L}$ be a very ample invertible $\mathcal{O}_{X}$-module for $Y$,
and set $\mathcal{P}_{\bullet}(n) = \mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ for every
$n \in Z$. Then, for every $y \in Y$, the function*

```text
  n ↦ EP(f, 𝒫_•(n); y)                                                       (7.9.11.1)
```

*is a polynomial with coefficients in $Q$, which is the same for all points of one and the same connected component of
$Y$.*

**Proof.** It is clear that $\mathcal{P}_{\bullet}(n)$ is a complex of $Y$-flat $\mathcal{O}_{X}$-modules. By virtue of
`(7.9.6.2)`, one can restrict to the case where $\mathcal{P}_{\bullet}$ is reduced to a single term $\mathcal{F} \neq 0$
of degree `0`; moreover, since these are local questions on $Y$, one can suppose $Y$ affine and $f$ projective
`(II, 5.5.3)`; set $X_{y} = f^{-1}(y)$, and let $\mathcal{L}_{y} = \mathcal{L} \otimes_{\mathcal{O}_{X}} \kappa(y)$,
which is a very ample $\mathcal{O}_{X_{y}}$-module `(II, 4.4.10)`; by virtue of `(7.7.2)`, one has, for the functor
$\mathcal{T}_{\bullet}$ relative to the complex $\mathcal{P}_{\bullet}(n)$, $T_{i}(\kappa(y)) = H^{-i}(X_{y},
\mathcal{F}_{y} \otimes \mathcal{L}^{\otimes n}_{y})$ (where $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{X}}
\kappa(y)$); whence it follows that $EP(f, \mathcal{F}(n); y)$ is none other than the Euler–Poincaré characteristic
$\chi_{\kappa(y)}(\mathcal{F}_{y}(n))$ defined in `(2.5.1)`; the fact that `(7.9.11.1)` is a polynomial then results
from `(2.5.3)`; moreover, for each $n$, its value is constant on a connected component of $Y$ `(7.9.4)`, which completes
the proof.

We shall denote by $PH(f, \mathcal{P}_{\bullet}; y)$ or $PH(\mathcal{P}_{\bullet}; y)$ the polynomial `(7.9.11.1)`, with
rational coefficients, and we shall say that it is the *Hilbert polynomial at $y$ relative to $\mathcal{P}_{\bullet}$,
$f$ and $\mathcal{L}$* (or simply the *Hilbert polynomial at $y$ of $\mathcal{P}_{\bullet}$*, or *of $f$*, if no
confusion results); when $Y$ is connected non-empty, one suppresses the mention of $y$ in the notation and the
terminology. The invariant thus obtained will play an essential role in chap. V, in the theory of "modules" of coherent
quotient sheaves of a given coherent sheaf.

**7.9.12.**

<!-- label: III.7.9.12 -->

With the notations of `(7.9.6)` and `(7.9.11)`, one has

```text
  PH(𝒫_•; y) = PH(𝒫'_•; y) + PH(𝒫''_•; y)                                    (7.9.12.1)
```

and in particular

```text
  PH(𝒫_•; y) = Σ_i (−1)^i PH(𝒫_i; y);                                        (7.9.12.2)
```

this results trivially from `(7.9.6.1)` and `(7.9.6.2)`. Similarly, with the notations and hypotheses of `(7.9.7)`, one
has

```text
  PH(𝒫'_•; y') = PH(𝒫_•; g(y')).                                             (7.9.12.3)
```

Formula `(7.9.12.2)` reduces the study of Hilbert polynomials of a complex to that of Hilbert polynomials of a single
$Y$-flat $\mathcal{O}_{X}$-module. The latter admit a remarkable interpretation independent of homological
considerations:

**Corollary (7.9.13).**

<!-- label: III.7.9.13 -->

*Let $Y$ be a noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{L}$ a very ample invertible
$\mathcal{O}_{X}$-module for $Y$, $\mathcal{F}$ a coherent and $Y$-flat $\mathcal{O}_{X}$-module. There exists an
integer $n_{0}$ such that for $n \geq n_{0}$, $f_{*}(\mathcal{F}(n))$ is a locally free $\mathcal{O}_{Y}$-module, of
rank at $y \in Y$ equal to $PH(f, \mathcal{F}; y)(n)$.*

**Proof.** Since the morphism $f$ is projective `(II, 5.5.3)`, there exists $n_{0}$ such that for $n \geq n_{0}$

<!-- original page 212 -->

one has $R^{i} f_{*}(\mathcal{F}(n)) = 0$ for every $i > 0$ `(2.2.1)`; the conclusion therefore results from `(7.9.10)`.

The following flatness criterion will be important in the theory of "modules" of coherent sheaves in chap. V:

**Proposition (7.9.14).**

<!-- label: III.7.9.14 -->

*Let $Y$ be a noetherian prescheme, $f : X \to Y$ a projective morphism, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module ample for $f$, and set $\mathcal{F}(n) = \mathcal{F} \otimes \mathcal{L}^{\otimes n}$ for every
$\mathcal{O}_{X}$-module $\mathcal{F}$ and every $n \in Z$. For a coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ to be
$Y$-flat, it is necessary and sufficient that there exist an integer $n_{0}$ such that, for every $n \geq n_{0}$,
$f_{*}(\mathcal{F}(n))$ be a locally free $\mathcal{O}_{Y}$-module.*

**Proof.** The necessity of the condition is proved as in `(7.9.13)` (the result of `(2.2.1)` applying to an ample sheaf
$\mathcal{L}$, since $f$ is projective). To prove the converse, one can restrict to the case where $Y$ is affine with
ring $A$; by virtue of the hypothesis and of `(2.2.2, (i))`, the $A$-modules $\Gamma(X, \mathcal{F}(n))$ are of finite
type and projective (Bourbaki, *Alg. comm.*, chap. II, § 5, n° 2, th. 1). Let $S$ be the graded ring $\oplus_{n \geq 0}
\Gamma(X, \mathcal{L}^{\otimes n})$; one knows that $X$ is canonically identified with $\operatorname{Proj}(S)$
`(II, 4.5.2, (b) and 5.4.4)`. Let $M = \oplus_{n \geq n_{0}} \Gamma(X, \mathcal{F}(n))$; replacing if necessary
$\mathcal{L}$ by a power $\mathcal{L}^{\otimes d}$, one can suppose that $S$ is generated by a finite number of elements
of degree 1 `(2.3.5.1)`, and it then results from `(II, 2.7.5 and 2.7.2)` that $\mathcal{F}$ is identified with
$\mathcal{P}\mathit{r}\mathcal{Oj}_{0}(M)$. For every homogeneous element $g \in S$ of degree `> 0`, one has therefore
$\Gamma(X_{g}, \mathcal{F}) = M_{(g)}$; now, $M$, the direct sum of projective $A$-modules, is a flat $A$-module, hence
so is $M_{g}$ $(0_{I}, 6.3.2)$, and consequently so is $M_{(g)}$, which is a direct factor of $M_{g}$ $(0_{I}, 6.1.2)$.
One concludes `(1.4.14.5)` that $\mathcal{F}$ is $Y$-flat at every point of $X_{g}$, and since the $X_{g}$ cover $X$,
the proposition is proved.

(*To be continued.*)
