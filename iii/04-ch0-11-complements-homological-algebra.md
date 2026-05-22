# Chapter 0_III

## §11. Complements on homological algebra

> _Translator's note._ In the OCR'd French source, the content of §11 is housed inside the file named for §10
> (`03-c0-s10-complements-modules-plats.md`, lines 266–1485). It is given its own translated file here.

<!-- original page 367 -->

### 11.1. Recall on spectral sequences

**11.1.1.**

<!-- label: 0_III.11.1.1 -->

In what follows we shall use a notion of spectral sequence more general than the one defined in `(T, 2.4)`; keeping the
notation of `(T, 2.4)`, we shall call a *spectral sequence in an abelian category $\mathcal{C}$* a system $E$ consisting
of the following data:

a) A family $(E^{p,q}_{r})$ of objects of $\mathcal{C}$ defined for $p \in \mathbb{Z}$, $q \in \mathbb{Z}$, and $r \geq
2$.

b) A family of morphisms $d^{p,q}_{r} : E^{p,q}_{r} \to E^{p+r, q-r+1}_{r}$ such that $d^{p+r, q-r+1}_{r} \circ
d^{p,q}_{r} = 0$.

We set $Z_{r+1}(E^{p,q}_{2}) = Ker(d^{p,q}_{r})$, $B_{r+1}(E^{p,q}_{2}) = Im(d^{p-r, q+r-1}_{r})$, so that

$$ B_{r+1}(E^{p,q}_{2}) \subset Z_{r+1}(E^{p,q}_{2}) \subset E^{p,q}_{2}. $$

c) A family of isomorphisms $\alpha^{p,q}_{r} : Z_{r}(E^{p,q}_{2})/B_{r}(E^{p,q}_{2}) \xrightarrow{\sim} E^{p,q}_{r}$.

One then defines, for $k \geq r + 1$, by induction on $k$, the subobjects $B_{k}(E^{p,q}_{2})$ and $Z_{k}(E^{p,q}_{2})$
as the inverse images, under the canonical morphism $E^{p,q}_{2} \to E^{p,q}_{2}/B_{r}(E^{p,q}_{2})$, of the subobjects
of this quotient identified by $\alpha^{p,q}_{r}$ with the subobjects $B_{k}(E^{p,q}_{r})$ and $Z_{k}(E^{p,q}_{r})$
respectively. It is clear that one then has, up to isomorphism,

$$ Z_{k}(E^{p,q}_{2})/B_{k}(E^{p,q}_{2}) = E^{p,q}_{k} (11.1.1.1) $$

for $k \geq r + 1$, and, if we further set $B_{1}(E^{p,q}_{2}) = 0$ and $Z_{1}(E^{p,q}_{2}) = E^{p,q}_{2}$, one has the
inclusion relations

```text
  0 = B_1(E_2^{p,q}) ⊂ B_2(E_2^{p,q}) ⊂ B_3(E_2^{p,q}) ⊂ …
       … ⊂ Z_3(E_2^{p,q}) ⊂ Z_2(E_2^{p,q}) ⊂ Z_1(E_2^{p,q}) = E_2^{p,q}.       (11.1.1.2)
```

The remaining data of $E$ are then:

d) Two subobjects $B_{\infty}(E^{p,q}_{2})$ and $Z_{\infty}(E^{p,q}_{2})$ of $E^{p,q}_{2}$ such that one has
$B_{\infty}(E^{p,q}_{2}) \subset Z_{\infty}(E^{p,q}_{2})$ and, for every $k \geq 2$,

```text
  B_k(E_2^{p,q}) ⊂ B_∞(E_2^{p,q})    and    Z_∞(E_2^{p,q}) ⊂ Z_k(E_2^{p,q}).
```

One sets

$$ E^{p,q}_{\infty} = Z_{\infty}(E^{p,q}_{2})/B_{\infty}(E^{p,q}_{2}). (11.1.1.3) $$

<!-- original page 368 -->

e) A family $(E^{n})$ of objects of $\mathcal{C}$, each equipped with a decreasing filtration $(F^{p}(E^{n}))_{p \in
\mathbb{Z}}$. As usual we denote by $gr(E^{n})$ the graded object associated to the filtered object $E^{n}$, the direct
sum of the $gr_{p}(E^{n}) = F^{p}(E^{n})/F^{p+1}(E^{n})$.

f) For every pair $(p, q) \in \mathbb{Z} \times \mathbb{Z}$, an isomorphism $\beta^{p,q} : E^{p,q}_{\infty}
\xrightarrow{\sim} gr_{p}(E^{p+q})$.

The family $(E^{n})$, without the filtrations, is called the *abutment* of the spectral sequence $E$.

Suppose either that the category $\mathcal{C}$ admits infinite direct sums, or that for every $r \geq 2$ and every $n
\in \mathbb{Z}$, the pairs $(p, q)$ such that $p + q = n$ and $E^{p,q}_{r} \neq 0$ are finite in number (it suffices
that this hold for $r = 2$). Then the $E^{(n)}_{r} = \oplus_{p+q=n} E^{p,q}_{r}$ are defined, and denoting by
$d^{(n)}_{r}$ the morphism $E^{(n)}_{r} \to E^{(n+1)}_{r}$ whose restriction to $E^{p,q}_{r}$ is $d^{p,q}_{r}$ for each
pair $(p, q)$ with $p + q = n$, one has $d^{(n+1)}_{r} \circ d^{(n)}_{r} = 0$; in other words, $(E^{(n)}_{r})_{n \in
\mathbb{Z}}$ is a complex $E^{(\bullet)}_{r}$ in $\mathcal{C}$, with derivation operator of degree `+1`, and it follows
from c) that $H^{\bullet}(E^{(\bullet)}_{r})$ is isomorphic to $E^{(\bullet)}_{r+1}$ for every $r \geq 2$.

**11.1.2.**

<!-- label: 0_III.11.1.2 -->

A *morphism* $u : E \to E'$ from a spectral sequence $E$ to a spectral sequence $E' = (E_{r}'^{p,q}, E'^{n})$ consists
of systems of morphisms $u^{p,q}_{r} : E^{p,q}_{r} \to E_{r}'^{p,q}$, $u^{n} : E^{n} \to E'^{n}$, the $u^{n}$ being
compatible with the filtrations of $E^{n}$ and $E'^{n}$, the diagrams

$$ d^{p,q}_{r} E^{p,q}_{r} \to E^{p+r, q-r+1}_{r} \downarrow \downarrow u^{p,q}_{r} u^{p+r, q-r+1}_{r} \downarrow
\downarrow E_{r}'^{p,q} \to E_{r}'^{p+r, q-r+1} d_{r}'^{p,q} $$

being commutative; moreover, on passing to quotients, $u^{p,q}_{r}$ induces a morphism $\bar{u}^{p,q}_{r} :
Z_{r+1}(E^{p,q}_{2})/B_{r+1}(E^{p,q}_{2}) \to Z_{r+1}(E_{2}'^{p,q})/B_{r+1}(E_{2}'^{p,q})$, and one must have
$\alpha_{r+1}'^{p,q} \circ \bar{u}^{p,q}_{r} = u^{p,q}_{r+1} \circ \alpha^{p,q}_{r+1}$; finally, one must have
$u^{p,q}_{2}(B_{\infty}(E^{p,q}_{2})) \subset B_{\infty}(E_{2}'^{p,q})$ and $u^{p,q}_{2}(Z_{\infty}(E^{p,q}_{2}))
\subset Z_{\infty}(E_{2}'^{p,q})$; on passing to quotients, $u^{p,q}_{2}$ then gives a morphism $u^{p,q}_{\infty} :
E^{p,q}_{\infty} \to E_{\infty}'^{p,q}$, and the diagram

$$ u^{p,q}_{\infty} E^{p,q}_{\infty} \to E_{\infty}'^{p,q} \downarrow \downarrow \beta^{p,q} \beta'^{p,q} \downarrow
\downarrow gr_{p}(E^{p+q}) \to gr_{p}(E'^{p+q}) gr_{p}(u^{p+q}) $$

must be commutative.

The preceding definitions show, by induction on $r$, that if the $u^{p,q}_{2}$ are *isomorphisms*, then so are the
$u^{p,q}_{r}$ for $r \geq 2$; if one further knows that $u^{p,q}_{2}(B_{\infty}(E^{p,q}_{2})) =
B_{\infty}(E_{2}'^{p,q})$ and $u^{p,q}_{2}(Z_{\infty}(E^{p,q}_{2})) = Z_{\infty}(E_{2}'^{p,q})$ and that the $u^{n}$ are
isomorphisms, then one can conclude that $u$ is an isomorphism.

<!-- original page 369 -->

**11.1.3.**

<!-- label: 0_III.11.1.3 -->

Recall that if $(F^{p}(X))_{p \in \mathbb{Z}}$ is a (decreasing) filtration of an object $X \in \mathcal{C}$, the
filtration is said to be *separated* if $\inf_{p} (F^{p}(X)) = 0$, *discrete* if there exists $p$ such that $F^{p}(X) =
0$, *exhaustive* (or *co-separated*) if $\sup_{p} (F^{p}(X)) = X$, *co-discrete* if there exists $p$ such that $F^{p}(X)
= X$.

We shall say that a spectral sequence $E = (E^{p,q}_{r}, E^{n})$ is *weakly convergent* if one has
$B_{\infty}(E^{p,q}_{2}) = \sup_{k}(B_{k}(E^{p,q}_{2}))$, $Z_{\infty}(E^{p,q}_{2}) = \inf_{k}(Z_{k}(E^{p,q}_{2}))$ (in
other words, the objects $B_{\infty}(E^{p,q}_{2})$ and $Z_{\infty}(E^{p,q}_{2})$ are determined by data a) through c) of
the spectral sequence $E$). We shall say that the spectral sequence $E$ is *regular* if it is weakly convergent and
moreover:

1° For every pair $(p, q)$, the decreasing sequence $(Z_{k}(E^{p,q}_{2}))_{k \geq 2}$ is stationary; the hypothesis that
$E$ is weakly convergent then implies $Z_{\infty}(E^{p,q}_{2}) = Z_{k}(E^{p,q}_{2})$ for $k$ sufficiently large
(depending on $p$ and $q$).

2° For every $n$, the filtration $(F^{p}(E^{n}))_{p \in \mathbb{Z}}$ of $E^{n}$ is discrete and exhaustive.

One says that the spectral sequence $E$ is *co-regular* if it is weakly convergent and moreover:

3° For every pair $(p, q)$, the increasing sequence $(B_{k}(E^{p,q}_{2}))_{k \geq 2}$ is stationary, which entails
$B_{\infty}(E^{p,q}_{2}) = B_{k}(E^{p,q}_{2})$, and consequently $E^{p,q}_{\infty} = \inf_{k} E^{p,q}_{k}$.

4° For every $n$, the filtration of $E^{n}$ is co-discrete.

Finally, one says that $E$ is *biregular* if it is both regular and co-regular; in other words, if the following
conditions hold:

a) For every pair $(p, q)$, the sequences $(B_{k}(E^{p,q}_{2}))_{k \geq 2}$ and $(Z_{k}(E^{p,q}_{2}))_{k \geq 2}$ are
stationary, and one has $B_{\infty}(E^{p,q}_{2}) = B_{k}(E^{p,q}_{2})$ and $Z_{\infty}(E^{p,q}_{2}) =
Z_{k}(E^{p,q}_{2})$ for $k$ sufficiently large (which entails $E^{p,q}_{\infty} = E^{p,q}_{k}$).

b) For every $n$, the filtration $(F^{p}(E^{n}))_{p \in \mathbb{Z}}$ is *discrete* and co-discrete (which one also
expresses by saying that it is *finite*).

The spectral sequences defined in `(T, 2.4)` are thus the biregular spectral sequences.

**11.1.4.**

<!-- label: 0_III.11.1.4 -->

Suppose that in the category $\mathcal{C}$ filtered inductive limits exist and that the functor $\varinjlim$ is exact
(which is equivalent to saying that axiom AB 5) of `(T, 1.5)` is verified (cf. `T, 1.8`)). The condition that the
filtration $(F^{p}(X))_{p \in \mathbb{Z}}$ of an object $X \in \mathcal{C}$ be exhaustive then also reads $\lim_{p \to
-\infty} F^{p}(X) = X$. If a spectral sequence $E$ is weakly convergent, one has $B_{\infty}(E^{p,q}_{2}) = \lim_{k \to
\infty} B_{k}(E^{p,q}_{2})$; if moreover $u : E \to E'$ is a morphism of $E$ into a weakly convergent spectral sequence
$E'$ of $\mathcal{C}$, one has $u^{p,q}_{2}(B_{\infty}(E^{p,q}_{2})) = B_{\infty}(E_{2}'^{p,q})$ by exactness of
$\varinjlim$. Moreover:

**Proposition (11.1.5).**

<!-- label: 0_III.11.1.5 -->

Let $\mathcal{C}$ be an abelian category in which filtered inductive limits are exact, let $E$, $E'$ be two regular
spectral sequences in $\mathcal{C}$, and let $u : E \to E'$ be a morphism of spectral sequences. If the $u^{p,q}_{2}$
are isomorphisms, then so is $u$.

**Proof.** We already know `(11.1.2)` that the $u^{p,q}_{r}$ are isomorphisms and that

$$ u^{p,q}_{2}(B_{\infty}(E^{p,q}_{2})) = B_{\infty}(E_{2}'^{p,q}); $$

<!-- original page 370 -->

the hypothesis that $E$ and $E'$ are regular also implies $u^{p,q}_{2}(Z_{\infty}(E^{p,q}_{2})) =
Z_{\infty}(E_{2}'^{p,q})$, and since $u^{p,q}_{2}$ is an isomorphism, so is $u^{p,q}_{\infty}$; one therefore concludes
that $gr_{p}(u^{p+q})$ is also an isomorphism. But since the filtrations of the $E^{n}$ and the $E'^{n}$ are discrete
and exhaustive, this entails that the $u^{n}$ are also isomorphisms (Bourbaki, _Alg. comm._, chap. III, § 2, n° 8, th.
1).

**11.1.6.**

<!-- label: 0_III.11.1.6 -->

It follows from `(11.1.1.2)` and from definition `(11.1.1.3)` that if, in a spectral sequence $E$, one has $E^{p,q}_{r}
= 0$, then one has $E^{p,q}_{k} = 0$ for $k \geq r$ and $E^{p,q}_{\infty} = 0$. One says that a spectral sequence is
*degenerate* if there exists an integer $r \geq 2$ and, for every integer $n \in \mathbb{Z}$, an integer $q(n)$ such
that $E^{n-q, q}_{r} = 0$ for every $q \neq q(n)$. From the preceding remark one first deduces that one also has
$E^{n-q, q}_{k} = 0$ for $k \geq r$ (including $k = \infty$) and $q \neq q(n)$. Moreover, the definition of
$E^{p,q}_{r+1}$ shows that one has $E^{n-q(n), q(n)}_{r+1} = E^{n-q(n), q(n)}_{r}$; if $E$ is weakly convergent, one
therefore also has $E^{n-q(n), q(n)}_{\infty} = E^{n-q(n), q(n)}_{r}$; in other words, for every $n \in \mathbb{Z}$,
$gr_{p}(E^{n}) = 0$ for $p \neq q(n)$ and $gr_{q(n)}(E^{n}) = E^{n-q(n), q(n)}_{r}$. If moreover the filtration of
$E^{n}$ is discrete and exhaustive, the sequence $E$ is regular and one has $E^{n} = E^{n-q(n), q(n)}_{r}$ up to
isomorphism.

**11.1.7.**

<!-- label: 0_III.11.1.7 -->

Suppose that in the category $\mathcal{C}$ filtered inductive limits exist and are exact, and let $(E_{\lambda},
u_{\lambda \mu})$ be an inductive system (over a filtered index set) of spectral sequences in $\mathcal{C}$. Then the
*inductive limit of this inductive system exists in the additive category of spectral sequences of objects of
$\mathcal{C}$*: to see this it suffices to define $E^{p,q}_{r}$, $d^{p,q}_{r}$, $\alpha^{p,q}_{r}$,
$B_{k}(E^{p,q}_{2})$, $Z_{k}(E^{p,q}_{2})$, $E^{n}$, $F^{p}(E^{n})$ and $\beta^{p,q}$ as the respective inductive limits
of $E^{p,q}_{r,\lambda}$, $d^{p,q}_{r,\lambda}$, $\alpha^{p,q}_{r,\lambda}$, $B_{k}(E^{p,q}_{2,\lambda})$,
$Z_{k}(E^{p,q}_{2,\lambda})$, $E^{n}_{\lambda}$, $F^{p}(E^{n}_{\lambda})$ and $\beta^{p,q}_{\lambda}$; the verification
of the conditions of `(11.1.1)` follows from the exactness of the functor $\varinjlim$ in $\mathcal{C}$.

**Remark (11.1.8).**

<!-- label: 0_III.11.1.8 -->

Suppose that the category $\mathcal{C}$ is the category of $A$-modules over a Noetherian ring $A$ (resp. over a ring
$A$). Then the definitions of `(11.1.1)` show that if, for a given $r$, the $E^{p,q}_{r}$ are $A$-modules of finite type
(resp. of finite length), then so are all the modules $E^{p,q}_{s}$ for $s \geq r$, as well as the $E^{p,q}_{\infty}$.
If moreover the filtration of the abutment $(E^{n})$ is discrete and co-discrete for every $n$, one concludes that each
of the $E^{n}$ is also an $A$-module of finite type (resp. of finite length).

**11.1.9.**

<!-- label: 0_III.11.1.9 -->

We shall have to consider conditions ensuring that a spectral sequence $E$ is biregular "uniformly" in $p + q = n$. We
shall then use the following lemma:

**Lemma (11.1.10).**

<!-- label: 0_III.11.1.10 -->

Let $(E^{p,q}_{r})$ be a family of objects of $\mathcal{C}$ linked by data a), b), c) of `(11.1.1)`. For a fixed integer
$n$, the following properties are equivalent:

a) There exists an integer $r(n)$ such that for $r \geq r(n)$, $p + q = n$ or $p + q = n - 1$, the morphisms
$d^{p,q}_{r}$ are all zero.

b) There exists an integer $r(n)$ such that for $p + q = n$ or $p + q = n + 1$, one has $B_{s}(E^{p,q}_{2}) =
B_{r}(E^{p,q}_{2})$ for $s \geq r \geq r(n)$.

c) There exists an integer $r(n)$ such that for $p + q = n$ or $p + q = n - 1$, one has $Z_{s}(E^{p,q}_{2}) =
Z_{r}(E^{p,q}_{2})$ for $s \geq r \geq r(n)$.

d) There exists an integer $r(n)$ such that for $p + q = n$, one has $B_{s}(E^{p,q}_{2}) = B_{r}(E^{p,q}_{2})$ and
$Z_{s}(E^{p,q}_{2}) = Z_{r}(E^{p,q}_{2})$ for $s \geq r \geq r(n)$.

<!-- original page 371 -->

**Proof.** Indeed, by conditions a), b), c) of `(11.1.1)`, to say that $Z_{r+1}(E^{p,q}_{2}) = Z_{r}(E^{p,q}_{2})$ is
equivalent to saying that $d^{p,q}_{r} = 0$, and to say that $B_{r+1}(E^{p+r, q-r+1}_{2}) = B_{r}(E^{p+r, q-r+1}_{2})$
is also equivalent to saying that $d^{p,q}_{r} = 0$; the lemma follows at once from this remark.

### 11.2. The spectral sequence of a filtered complex

**11.2.1.**

<!-- label: 0_III.11.2.1 -->

Given an abelian category $\mathcal{C}$, we shall use notation such as $K^{\bullet}$ for complexes $(K^{i})_{i \in
\mathbb{Z}}$ of objects of $\mathcal{C}$ in which the derivation operator is of degree `+1`, and notation such as
$K_{\bullet}$ for complexes $(K_{i})_{i \in \mathbb{Z}}$ of objects of $\mathcal{C}$ in which the derivation operator is
of degree $-1$. To any complex $K^{\bullet} = (K^{i})$ whose derivation operator $d$ is of degree `+1`, one can
associate a complex $K_{\bullet}' = (K_{i}')$ by setting $K_{i}' = K^{-i}$, the derivation operator $K_{i}' \to
K_{i-1}'$ being the operator $d : K^{-i} \to K^{-i+1}$; and conversely, which will allow us, according to circumstances,
to consider one type of complex or the other and to translate every result for one type into a result for the other. We
shall denote similarly by notation such as $K^{\bullet,\bullet} = (K^{i,j})$ (resp. $K_{\bullet,\bullet} = (K_{i,j})$)
*bicomplexes* of objects of $\mathcal{C}$ in which the two derivation operators are of degree `+1` (resp. $-1$); one
again passes from one type to the other by changing the signs of the indices, and one has analogous notation and remarks
for arbitrary multicomplexes. The notation $K^{\bullet}$ or $K_{\bullet}$ will also be used for graded objects of
$\mathcal{C}$, of type $\mathbb{Z}$, which are not necessarily complexes (or which one may consider as such with zero
derivation operators); for instance, we shall write $H^{\bullet}(K^{\bullet}) = (H^{i}(K^{\bullet}))_{i \in \mathbb{Z}}$
for the cohomology of a complex $K^{\bullet}$ whose derivation operator is of degree `+1`, and $H_{\bullet}(K_{\bullet})
= (H_{i}(K_{\bullet}))_{i \in \mathbb{Z}}$ for the homology of a complex $K_{\bullet}$ whose derivation operator is of
degree $-1$; when one passes from $K^{\bullet}$ to $K_{\bullet}'$ by the operation described above, one has
$H_{i}(K_{\bullet}') = H^{-i}(K^{\bullet})$.

Recall in this connection that for a complex $K^{\bullet}$ (resp. $K_{\bullet}$), we shall generally write
$Z^{i}(K^{\bullet}) = Ker(K^{i} \to K^{i+1})$ ("object of cocycles") and $B^{i}(K^{\bullet}) = Im(K^{i-1} \to K^{i})$
("object of coboundaries") (resp. $Z_{i}(K_{\bullet}) = Ker(K_{i} \to K_{i-1})$ ("object of cycles") and
$B_{i}(K_{\bullet}) = Im(K_{i+1} \to K_{i})$ ("object of boundaries")), so that $H^{i}(K^{\bullet}) =
Z^{i}(K^{\bullet})/B^{i}(K^{\bullet})$ (resp. $H_{i}(K_{\bullet}) = Z_{i}(K_{\bullet})/B_{i}(K_{\bullet})$).

If $K^{\bullet} = (K^{i})$ (resp. $K_{\bullet} = (K_{i})$) is a complex in $\mathcal{C}$, and $T : \mathcal{C} \to
\mathcal{C}'$ a functor from $\mathcal{C}$ to an abelian category $\mathcal{C}'$, we shall denote by $T(K^{\bullet})$
(resp. $T(K_{\bullet})$) the complex $(T(K^{i}))$ (resp. $(T(K_{i}))$) in $\mathcal{C}'$.

We do not return to the definition of $\partial$-functors `(T, 2.1)`, except to point out that we shall also say
*$\partial$-functor* in place of *$\partial^{*}$-functor* when the morphism $\partial$ lowers the degree by one unit;
the context should make this clear when there could be doubt.

Finally, we shall say that a graded object $(A^{i})_{i \in \mathbb{Z}}$ of $\mathcal{C}$ is *bounded below* (resp.
*bounded above*) if there exists $i_{0}$ such that $A^{i} = 0$ for $i < i_{0}$ (resp. $i > i_{0}$).

**11.2.2.**

<!-- label: 0_III.11.2.2 -->

Let $K^{\bullet}$ be a complex in $\mathcal{C}$ whose derivation operator $d$ is of degree `+1`, and suppose it equipped
with a *filtration* $F(K^{\bullet}) = (F^{p}(K^{\bullet}))_{p \in \mathbb{Z}}$ formed of graded subobjects of
$K^{\bullet}$,

<!-- original page 372 -->

in other words $F^{p}(K^{\bullet}) = (K^{i} \cap F^{p}(K^{\bullet}))_{i \in \mathbb{Z}}$; moreover, we assume that
$d(F^{p}(K^{\bullet})) \subset F^{p}(K^{\bullet})$ for every $p \in \mathbb{Z}$. We now briefly recall how one
functorially defines a spectral sequence $E(K^{\bullet})$ from $K^{\bullet}$ `(M, XV, 4` and `G, I, 4.3)`. For $r \geq
2$, the canonical morphism $F^{p}(K^{\bullet})/F^{p+r}(K^{\bullet}) \to F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet})$ defines
a morphism in cohomology

$$ H^{p+q}(F^{p}(K^{\bullet})/F^{p+r}(K^{\bullet})) \to H^{p+q}(F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet})). $$

One denotes by $Z^{p,q}_{r}(K^{\bullet})$ the image of this morphism. Similarly, from the exact sequence

$$ 0 \to F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet}) \to F^{p-r+1}(K^{\bullet})/F^{p+1}(K^{\bullet}) \to
F^{p-r+1}(K^{\bullet})/F^{p}(K^{\bullet}) \to 0 $$

one deduces, by the long exact sequence of cohomology, a morphism

$$ H^{p+q-1}(F^{p-r+1}(K^{\bullet})/F^{p}(K^{\bullet})) \to H^{p+q}(F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet})) $$

and one denotes by $B^{p,q}_{r}(K^{\bullet})$ the image of this morphism; one shows that $B^{p,q}_{r}(K^{\bullet})
\subset Z^{p,q}_{r}(K^{\bullet})$ and one sets $E^{p,q}_{r}(K^{\bullet}) =
Z^{p,q}_{r}(K^{\bullet})/B^{p,q}_{r}(K^{\bullet})$; we shall not specify the definitions of the $d^{p,q}_{r}$ or the
$\alpha^{p,q}_{r}$.

We note here that all the $Z^{p,q}_{r}(K^{\bullet})$ and $B^{p,q}_{r}(K^{\bullet})$, for $p$, $q$ fixed, are subobjects
of the same object $H^{p+q}(F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet}))$, which one denotes $Z^{p,q}_{1}(K^{\bullet})$; one
sets $B^{p,q}_{1}(K^{\bullet}) = 0$, so that the preceding definitions for $Z^{p,q}_{r}(K^{\bullet})$ and
$B^{p,q}_{r}(K^{\bullet})$ also apply for $r = 1$; one further sets $E^{p,q}_{1}(K^{\bullet}) =
Z^{p,q}_{1}(K^{\bullet})$. One also defines the $d^{p,q}_{1}$ and $\alpha^{p,q}_{1}$ so that the conditions of
`(11.1.1)` are satisfied for $r = 1$. One defines on the other hand the subobjects $Z^{p,q}_{\infty}(K^{\bullet})$,
image of the morphism

$$ H^{p+q}(F^{p}(K^{\bullet})) \to H^{p+q}(F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet})) = E^{p,q}_{1}(K^{\bullet}) $$

and $B^{p,q}_{\infty}(K^{\bullet})$, image of the morphism

$$ H^{p+q-1}(K^{\bullet}/F^{p}(K^{\bullet})) \to H^{p+q}(F^{p}(K^{\bullet})/F^{p+1}(K^{\bullet})) =
E^{p,q}_{1}(K^{\bullet}) $$

obtained as above from a long exact sequence of cohomology. One takes for $Z_{\infty}(E^{p,q}_{2}(K^{\bullet}))$ and
$B_{\infty}(E^{p,q}_{2}(K^{\bullet}))$ the canonical images in $E^{p,q}_{2}(K^{\bullet})$ of
$Z^{p,q}_{\infty}(K^{\bullet})$ and $B^{p,q}_{\infty}(K^{\bullet})$.

Finally, one denotes by $F^{p}(H^{n}(K^{\bullet}))$ the image in $H^{n}(K^{\bullet})$ of the morphism
$H^{n}(F^{p}(K^{\bullet})) \to H^{n}(K^{\bullet})$ coming from the canonical injection $F^{p}(K^{\bullet}) \to
K^{\bullet}$; by the long exact sequence of cohomology, it is also the kernel of the morphism $H^{n}(K^{\bullet}) \to
H^{n}(K^{\bullet}/F^{p}(K^{\bullet}))$. One thus defines a filtration on $E^{n}(K^{\bullet}) = H^{n}(K^{\bullet})$; we
shall not give the definition of the isomorphisms $\beta^{p,q}$ here either.

**11.2.3.**

<!-- label: 0_III.11.2.3 -->

The functorial character of $E(K^{\bullet})$ is to be understood as follows: given two *filtered* complexes
$K^{\bullet}$, $K'^{\bullet}$ of $\mathcal{C}$ and a morphism of complexes $u : K^{\bullet} \to K'^{\bullet}$
*compatible with the filtrations*, one deduces from it in an obvious way the morphisms $u^{p,q}_{r}$ (for $r \geq 1$)
and $u^{n}$, and one shows that these morphisms are compatible with the $d^{p,q}_{r}$, $\alpha^{p,q}_{r}$ and
$\beta^{p,q}$ in the sense of `(11.1.2)`, so that they indeed define a morphism $E(u) : E(K^{\bullet}) \to
E(K'^{\bullet})$ of spectral sequences. Moreover, one shows that if $u$ and $v$ are morphisms $K^{\bullet} \to
K'^{\bullet}$ of the preceding type, *homotopic of order $\leq k$*, then $u^{p,q}_{r} = v^{p,q}_{r}$ for $r > k$ and
$u^{n} = v^{n}$ for every $n$ `(M, XV, 3.1)`.

<!-- original page 373 -->

**11.2.4.**

<!-- label: 0_III.11.2.4 -->

Suppose that in $\mathcal{C}$ filtered inductive limits are exact. Then, if the filtration $(F^{p}(K^{\bullet}))$ of
$K^{\bullet}$ is exhaustive, so is the filtration $(F^{p}(H^{n}(K^{\bullet})))$ for every $n$, since by hypothesis
$K^{\bullet} = \lim_{p \to -\infty} F^{p}(K^{\bullet})$ and the hypothesis on $\mathcal{C}$ implies that cohomology
commutes with inductive limits. Moreover, for the same reason, one has $B_{\infty}(E^{p,q}_{2}(K^{\bullet})) = \sup_{k}
B_{k}(E^{p,q}_{2}(K^{\bullet}))$. One says that the filtration $(F^{p}(K^{\bullet}))$ of $K^{\bullet}$ is *regular* if
for every $n$ there exists an integer $u(n)$ such that $H^{n}(F^{p}(K^{\bullet})) = 0$ for $p > u(n)$. This holds in
particular when the filtration of $K^{\bullet}$ is discrete. When the filtration of $K^{\bullet}$ is regular and
exhaustive, and filtered inductive limits in $\mathcal{C}$ are exact, one shows `(M, XV, 4)` that the spectral sequence
$E(K^{\bullet})$ is regular.

### 11.3. The spectral sequences of a bicomplex

**11.3.1.**

<!-- label: 0_III.11.3.1 -->

As regards the conventions on bicomplexes, we follow those of `(T, 2.4)` rather than those of `(M)`, the two derivations
$d'$, $d''$ (of degree `+1`) of such a bicomplex $K^{\bullet,\bullet} = (K^{i,j})$ being therefore *assumed to commute*.
Suppose that *one of the two following conditions* is verified: 1° infinite direct sums exist in $\mathcal{C}$; 2° for
every $n \in \mathbb{Z}$, there are only finitely many pairs $(p, q)$ such that $p + q = n$ and $K^{p,q} \neq 0$. Then
the bicomplex $K^{\bullet,\bullet}$ defines a (simple) complex $(K^{(n)})_{n \in \mathbb{Z}}$ with $K^{(n)} =
\oplus_{i+j=n} K^{i,j}$, the derivation operator $d$ (of degree `+1`) of this complex being given by $dx = d'x +
(-1)^{i} d''x$ for $x \in K^{i,j}$. *Whenever in what follows we speak of the (simple) complex defined by a bicomplex
$K^{\bullet,\bullet}$, it will always be understood that one of the preceding conditions is satisfied.* One adopts
analogous conventions for multicomplexes.

We denote by $K^{i,\bullet}$ (resp. $K^{\bullet,j}$) the simple complex $(K^{i,j})_{j \in \mathbb{Z}}$ (resp.
$(K^{i,j})_{i \in \mathbb{Z}}$), and by $Z^{q}_{II}(K^{i,\bullet})$, $B^{q}_{II}(K^{i,\bullet})$,
$H^{q}_{II}(K^{i,\bullet})$ (resp. $Z^{p}_{I}(K^{\bullet,j})$, $B^{p}_{I}(K^{\bullet,j})$, $H^{p}_{I}(K^{\bullet,j})$)
its $q$th (resp. $p$th) objects of cocycles, coboundaries, and cohomology respectively; the derivation $d' :
K^{i,\bullet} \to K^{i+1,\bullet}$ is a morphism of complexes, which therefore gives an operator on the cocycles,
coboundaries, and cohomology,

$$ d' : Z^{q}_{II}(K^{i,\bullet}) \to Z^{q}_{II}(K^{i+1,\bullet}) d' : B^{q}_{II}(K^{i,\bullet}) \to
B^{q}_{II}(K^{i+1,\bullet}) d' : H^{q}_{II}(K^{i,\bullet}) \to H^{q}_{II}(K^{i+1,\bullet}) $$

and it is clear that for these operators, $(Z^{q}_{II}(K^{i,\bullet}))_{i \in \mathbb{Z}}$,
$(B^{q}_{II}(K^{i,\bullet}))_{i \in \mathbb{Z}}$, and $(H^{q}_{II}(K^{i,\bullet}))_{i \in \mathbb{Z}}$ are complexes; we
shall denote the complex $(H^{q}_{II}(K^{i,\bullet}))_{i \in \mathbb{Z}}$ by $H^{q}_{II}(K^{\bullet,\bullet})$, and its
$p$th objects of cocycles, coboundaries, and cohomology by $Z^{p}_{I}(H^{q}_{II}(K^{\bullet,\bullet}))$,
$B^{p}_{I}(H^{q}_{II}(K^{\bullet,\bullet}))$, and $H^{p}_{I}(H^{q}_{II}(K^{\bullet,\bullet}))$. One defines similarly
the complexes $H^{p}_{I}(K^{\bullet,\bullet})$ and their objects of cohomology
$H^{q}_{II}(H^{p}_{I}(K^{\bullet,\bullet}))$. Recall on the other hand that $H^{n}(K^{\bullet,\bullet})$ denotes the
$n$th object of cohomology of the (simple) complex defined by $K^{\bullet,\bullet}$.

**11.3.2.**

<!-- label: 0_III.11.3.2 -->

On the complex defined by a bicomplex $K^{\bullet,\bullet}$, one may consider two *canonical filtrations*
$(F^{p}_{I}(K^{\bullet,\bullet}))$ and $(F^{p}_{II}(K^{\bullet,\bullet}))$ given by

```text
  F_I^p(K^{•,•}) = (⊕_{i+j=n, i ≥ p} K^{i,j})_{n ∈ ℤ},   F_{II}^p(K^{•,•}) = (⊕_{i+j=n, j ≥ p} K^{i,j})_{n ∈ ℤ}.   (11.3.2.1)
```

<!-- original page 374 -->

which are by definition graded subobjects of the (simple) complex defined by $K^{\bullet,\bullet}$, and thus make this
complex into a *filtered complex*; moreover, it is clear that these filtrations are *exhaustive and separated*.

To each of these filtrations there corresponds a spectral sequence `(11.2.2)`; we shall denote by
$'E(K^{\bullet,\bullet})$ and $''E(K^{\bullet,\bullet})$ the spectral sequences corresponding to
$(F^{p}_{I}(K^{\bullet,\bullet}))$ and $(F^{p}_{II}(K^{\bullet,\bullet}))$ respectively, called the *spectral sequences
of the bicomplex $K^{\bullet,\bullet}$*, both having as abutment the cohomology $(H^{n}(K^{\bullet,\bullet}))$. One
shows moreover `(M, XV, 6)` that

```text
  'E_2^{p,q}(K^{•,•}) = H_I^p(H_{II}^q(K^{•,•})),    ″E_2^{p,q}(K^{•,•}) = H_{II}^p(H_I^q(K^{•,•})).   (11.3.2.2)
```

Any morphism $u : K^{\bullet,\bullet} \to K'^{\bullet,\bullet}$ of bicomplexes is ipso facto compatible with the
filtrations of the same type on $K^{\bullet,\bullet}$ and $K'^{\bullet,\bullet}$, and thus defines a morphism for each
of the two spectral sequences; moreover, two homotopic morphisms define a homotopy of order $\leq 1$ of the
corresponding (simple) filtered complexes, hence the same morphism for each of the two spectral sequences
`(M, XV, 6.1)`.

**Proposition (11.3.3).**

<!-- label: 0_III.11.3.3 -->

Let $K^{\bullet,\bullet} = (K^{i,j})$ be a bicomplex in an abelian category $\mathcal{C}$.

(i) If there exist $i_{0}$ and $j_{0}$ such that $K^{i,j} = 0$ for $i < i_{0}$ or $j < j_{0}$ (resp. $i > i_{0}$ or $j >
j_{0}$), the two spectral sequences $'E(K^{\bullet,\bullet})$ and $''E(K^{\bullet,\bullet})$ are biregular.

(ii) If there exist $i_{0}$ and $i_{1}$ such that $K^{i,j} = 0$ for $i < i_{0}$ or $i > i_{1}$ (resp. if there exist
$j_{0}$ and $j_{1}$ such that $K^{i,j} = 0$ for $j < j_{0}$ or $j > j_{1}$), the two spectral sequences
$'E(K^{\bullet,\bullet})$ and $''E(K^{\bullet,\bullet})$ are biregular.

Suppose moreover that in $\mathcal{C}$ filtered inductive limits exist and are exact. Then:

(iii) If there exists $i_{0}$ such that $K^{i,j} = 0$ for $i > i_{0}$ (resp. if there exists $j_{0}$ such that $K^{i,j}
= 0$ for $j < j_{0}$), the sequence $'E(K^{\bullet,\bullet})$ is regular.

(iv) If there exists $i_{0}$ such that $K^{i,j} = 0$ for $i < i_{0}$ (resp. if there exists $j_{0}$ such that $K^{i,j} =
0$ for $j > j_{0}$), the sequence $''E(K^{\bullet,\bullet})$ is regular.

**Proof.** The proposition follows at once from the definitions `(11.1.3)` and from `(11.2.4)`, together with the
following observations concerning the filtration `F_I` (and the analogous observations one deduces for $F_{II}$ by
exchanging the roles of the two indices in $K^{\bullet,\bullet}$):

1° If there exists $i_{0}$ such that $K^{i,j} = 0$ for $i > i_{0}$, the filtration $F_{I}(K^{\bullet,\bullet})$ is
*discrete*.

2° If there exists $i_{0}$ such that $K^{i,j} = 0$ for $i < i_{0}$, the filtration $F_{I}(K^{\bullet,\bullet})$ is
*co-discrete*. One deduces at once that the same holds for the corresponding filtration
$F_{I}(H^{n}(K^{\bullet,\bullet}))$ for every $n$; moreover, the definition of $B^{p,q}_{r}$ corresponding to the
filtration $F_{I}(K^{\bullet,\bullet})$ `(11.2.2)` shows that for every pair $(p, q)$, the sequence $(B^{p,q}_{r})_{r
\geq 2}$ is stationary.

3° If there exists $j_{0}$ such that $K^{i,j} = 0$ for $j < j_{0}$, one has

$$ F^{p+r}_{I}(K^{\bullet,\bullet}) \cap (\oplus_{i+j=n} K^{i,j}) = 0 $$

whenever $p + r + j_{0} > n$, hence $Z^{p,q}_{r} = Z_{\infty}(E^{p,q}_{2})$ for $r > q - j_{0} + 1$; on the other hand,
$H^{n}(F^{p}_{I}(K^{\bullet,\bullet})) = 0$ for $p > n - j_{0} + 1$.

4° If there exists $j_{0}$ such that $K^{i,j} = 0$ for $j > j_{0}$, one has

```text
  F_I^{p-r+1}(K^{•,•}) ∩ (⊕_{i+j=n} K^{i,j}) = ⊕_{i+j=n} K^{i,j}
```

<!-- original page 375 -->

whenever $p - r + 1 + j_{0} < n$, hence $B^{p,q}_{r} = B_{\infty}(E^{p,q}_{2})$ for $r < j_{0} - q + 1$; on the other
hand, $H^{n}(F^{p}_{I}(K^{\bullet,\bullet})) = H^{n}(K^{\bullet,\bullet})$ for $p + j_{0} < n - 1$.

**11.3.4.**

<!-- label: 0_III.11.3.4 -->

Suppose that the bicomplex $K^{\bullet,\bullet} = (K^{i,j})$ is such that $K^{i,j} = 0$ for $i < 0$ or $j < 0$. It is
known that one can then define for every $p \in \mathbb{Z}$ a canonical "edge homomorphism"

$$ 'E^{p,0}_{2}(K^{\bullet,\bullet}) \to H^{p}(K^{\bullet,\bullet}) (11.3.4.1) $$

`(M, XV, 6)`. We briefly recall that this is due, on the one hand, to the fact that one has $Z^{p,0}_{r} =
Z_{\infty}(E^{p,0}_{2})$ in the spectral sequence $'E(K^{\bullet,\bullet})$ for $2 \leq r \leq +\infty$, and, on the
other hand, to the fact that $H^{p}(F^{p+1}_{I}(K^{\bullet,\bullet})) = 0$, so that the isomorphism $\beta^{p,0} :
'E^{p,0}_{\infty} \xrightarrow{\sim} H^{p}(F^{p}_{I})/H^{p}(F^{p+1}_{I})$ gives a homomorphism $'E^{p,0}_{\infty} \to
H^{p}(F^{p}_{I}(K^{\bullet,\bullet})) \to H^{p}(K^{\bullet,\bullet})$; the equality of all the $Z^{p,0}_{r}$ then makes
it possible to define canonical homomorphisms $'E^{p,0}_{r} \to 'E^{p,0}_{s}$ for $r \leq s$, in particular a
homomorphism $'E^{p,0}_{2} \to 'E^{p,0}_{\infty}$, whence by composition the edge homomorphism $'E^{p,0}_{2} \to
H^{p}(K^{\bullet,\bullet})$; moreover, one verifies at once that, to the class mod. $B^{p,0}_{\infty}$ of an element $z
\in Z^{0}_{II}(K^{\bullet,\bullet}) \subset K^{p,0}$ such that $d'z = 0$, the edge homomorphism so defined associates in
$'E^{p,0}_{\infty}$ the class of $z$ mod. $B^{p,0}_{\infty}$, and then, to this last, the cohomology class of $z$ in
$H^{p}(K^{\bullet,\bullet})$. One thus sees finally that the edge homomorphism `(11.3.4.1)` comes, by passage to
cohomology, from the canonical injection $Z^{0}_{II}(K^{\bullet,\bullet}) \to K^{\bullet,\bullet}$ (where
$K^{\bullet,\bullet}$ is considered as a simple complex). One similarly interprets the edge homomorphism

$$ ''E^{p,0}_{2}(K^{\bullet,\bullet}) \to H^{p}(K^{\bullet,\bullet}) (11.3.4.2) $$

as coming from the canonical injection $Z^{0}_{I}(K^{\bullet,\bullet}) \to K^{\bullet,\bullet}$.

**11.3.5.**

<!-- label: 0_III.11.3.5 -->

Let now $K_{\bullet,\bullet} = (K_{i,j})$ be a bicomplex in $\mathcal{C}$ whose two derivation operators are of degree
$-1$. We shall then write $K_{i,\bullet}$ (resp. $K_{\bullet,j}$) for the simple complex $(K_{i,j})_{j \in \mathbb{Z}}$
(resp. $(K_{i,j})_{i \in \mathbb{Z}}$), $H^{II}_{p}(K_{i,\bullet})$ (resp. $H^{I}_{p}(K_{\bullet,j})$) for its $p$th
object of homology, $H^{II}_{p}(K_{\bullet,\bullet})$ (resp. $H^{I}_{p}(K_{\bullet,\bullet})$) for the complex
$(H^{II}_{p}(K_{i,\bullet}))_{i \in \mathbb{Z}}$ (resp. $(H^{I}_{p}(K_{\bullet,j}))_{j \in \mathbb{Z}}$),
$H^{I}_{q}(H^{II}_{p}(K_{\bullet,\bullet}))$ (resp. $H^{II}_{q}(H^{I}_{p}(K_{\bullet,\bullet}))$) for its $q$th object
of homology; analogous notation for the objects of cycles and boundaries; finally, $H_{n}(K_{\bullet,\bullet})$ will
denote (when it exists) the $n$th object of homology of the simple complex (with derivation operator of degree $-1$)
defined by $K_{\bullet,\bullet}$.

Let $K^{\bullet,\bullet} = (K^{i,j})$ with $K^{i,j} = K_{-i,-j}$ be the bicomplex with derivation operators of degree
`+1` associated to $K_{\bullet,\bullet}$; by definition, the spectral sequences of $K_{\bullet,\bullet}$ are those of
$K^{\bullet,\bullet}$, which one writes $'E(K_{\bullet,\bullet})$ and $''E(K_{\bullet,\bullet})$, where one changes the
notation, however, by setting

```text
  'E_{p,q}^r(K_{•,•}) = 'E_r^{-p,-q}(K^{•,•}),    ″E_{p,q}^r(K_{•,•}) = ″E_r^{-p,-q}(K^{•,•})
```

for $2 \leq r \leq \infty$. With this notation, one has

```text
  'E_{p,q}^2(K_{•,•}) = H_p^I(H_q^{II}(K_{•,•})),    ″E_{p,q}^2(K_{•,•}) = H_p^{II}(H_q^I(K_{•,•})).
```

To avoid sign errors, it will generally be preferable, for the relations between these spectral sequences and their
abutment, to return to the complex $K^{\bullet,\bullet}$. Let us note nonetheless the criteria corresponding to
`(11.3.3)`:

**11.3.6.**

<!-- label: 0_III.11.3.6 -->

The spectral sequences $'E(K_{\bullet,\bullet})$ and $''E(K_{\bullet,\bullet})$ are biregular in the following cases: a)
There exist $i_{0}$ and $j_{0}$ such that $K_{i,j} = 0$ for $i > i_{0}$ or for $j > j_{0}$ (resp. for $i < i_{0}$

<!-- original page 376 -->

or for $j < j_{0}$); b) There exist $i_{0}$ and $i_{1}$ such that $K_{i,j} = 0$ for $i < i_{0}$ and $i > i_{1}$; c)
There exist $j_{0}$ and $j_{1}$ such that $K_{i,j} = 0$ for $j < j_{0}$ and $j > j_{1}$.

The sequence $'E(K_{\bullet,\bullet})$ is regular if there exists $i_{0}$ such that $K_{i,j} = 0$ for $i < i_{0}$, or if
there exists $j_{0}$ such that $K_{i,j} = 0$ for $j > j_{0}$.

The sequence $''E(K_{\bullet,\bullet})$ is regular if there exists $i_{0}$ such that $K_{i,j} = 0$ for $i > i_{0}$, or
if there exists $j_{0}$ such that $K_{i,j} = 0$ for $j < j_{0}$.

### 11.4. Hypercohomology of a functor with respect to a complex $K^{\bullet}$

**11.4.1.**

<!-- label: 0_III.11.4.1 -->

Let $\mathcal{C}$ be an abelian category; recall that one calls a *right resolution* (or *cohomological resolution*) of
an object $A$ of $\mathcal{C}$ a complex of objects of $\mathcal{C}$, whose derivation operator is of degree `+1`,

$$ 0 \to L^{0} \to L^{1} \to L^{2} \to \cdots $$

equipped with a morphism $\epsilon : A \to L^{0}$ called the *augmentation* of the resolution (and which one can
consider as a morphism of complexes

```text
  0 → A → 0 → 0 → …
        ↓   ↓   ↓
  0 → L^0 → L^1 → L^2 → … )
```

such that the sequence

```text
  0 → A →^ε L^0 → L^1 → …
```

is exact; similarly, a *left resolution* (or *homological resolution*) of $A$ is a complex $0 \leftarrow L_{0}
\leftarrow L_{1} \leftarrow \cdots$ of objects of $\mathcal{C}$ whose derivation operator is of degree $-1$, equipped
with an augmentation $\epsilon : L_{0} \to A$, such that the sequence

```text
  0 ← A ←^ε L_0 ← L_1 ← …
```

is exact.

When a right resolution $(L^{i})_{i \geq 0}$ of an object $A$ is such that $L^{i} = 0$ for $i \geq n + 1$, one says that
this resolution is *of length $\leq n$*. One defines similarly a left resolution of length $\leq n$. A resolution that
is of length $\leq n$ for some integer $n$ is said to be *finite*.

A resolution of $A$ is called *projective* (resp. *injective*) if the objects of $\mathcal{C}$ other than $A$ that
compose it are projective (resp. injective). When $\mathcal{C}$ is the category of modules (left modules, say) over a
ring, one will say similarly that a resolution of $A$ is *flat* (resp. *free*) when the modules other than $A$ that
compose it are flat (resp. free).

**11.4.2.**

<!-- label: 0_III.11.4.2 -->

Let $K^{\bullet} = (K^{i})_{i \in \mathbb{Z}}$ be a complex of objects of $\mathcal{C}$ whose derivation operator is of
degree `+1`.

We call a *right Cartan–Eilenberg resolution of $K^{\bullet}$* the pair consisting of a bicomplex $L^{\bullet,\bullet} =
(L^{i,j})$ with derivation operators of degree `+1`, with $L^{i,j} = 0$ for $j < 0$, and a morphism of simple complexes
$\epsilon : K^{\bullet} \to L^{\bullet,0}$, such that the following conditions are satisfied:

<!-- original page 377 -->

(i) For each index $i$, the sequences

```text
  0 → K^i →^ε L^{i,0} → L^{i,1} → …
  0 → B^i(K^•) →^ε B_I^i(L^{•,0}) → B_I^i(L^{•,1}) → …
  0 → Z^i(K^•) →^ε Z_I^i(L^{•,0}) → Z_I^i(L^{•,1}) → …
  0 → H^i(K^•) →^ε H_I^i(L^{•,0}) → H_I^i(L^{•,1}) → …
```

are exact; in other words, $(L^{i,\bullet})$, $(B^{i}_{I}(L^{\bullet,\bullet}))$, $(Z^{i}_{I}(L^{\bullet,\bullet}))$ and
$(H^{i}_{I}(L^{\bullet,\bullet}))$ are respectively resolutions of $K^{i}$, $B^{i}(K^{\bullet})$, $Z^{i}(K^{\bullet})$
and $H^{i}(K^{\bullet})$.

(ii) For each $j$, the simple complex $L^{\bullet,j}$ is *split*; in other words, the exact sequences

$$ 0 \to B^{i}_{I}(L^{\bullet,j}) \to Z^{i}_{I}(L^{\bullet,j}) \to H^{i}_{I}(L^{\bullet,j}) \to 0 (11.4.2.1) 0 \to
Z^{i}_{I}(L^{\bullet,j}) \to L^{i,j} \to B^{i+1}_{I}(L^{\bullet,j}) \to 0 (11.4.2.2) $$

are split.

One proves `(M, XVII, 1.2)` that if every object of $\mathcal{C}$ is a subobject of an injective object, every complex
$K^{\bullet}$ of $\mathcal{C}$ admits an *injective* Cartan–Eilenberg resolution, that is, one formed of injective
objects $L^{i,j}$ (condition (ii) above then entails that the $B^{i}_{I}(L^{\bullet,j})$, $Z^{i}_{I}(L^{\bullet,j})$ and
$H^{i}_{I}(L^{\bullet,j})$ are also injective objects). Moreover, for every morphism $f : K^{\bullet} \to K'^{\bullet}$
of complexes of $\mathcal{C}$, every Cartan–Eilenberg resolution $L^{\bullet,\bullet}$ of $K^{\bullet}$ and every
*injective* Cartan–Eilenberg resolution $L'^{\bullet,\bullet}$ of $K'^{\bullet}$, there exists a morphism of bicomplexes
$F : L^{\bullet,\bullet} \to L'^{\bullet,\bullet}$ compatible with $f$ and the augmentations; and if $f$ and $g$ are two
*homotopic* morphisms from $K^{\bullet}$ to $K'^{\bullet}$, the corresponding morphisms from $L^{\bullet,\bullet}$ to
$L'^{\bullet,\bullet}$ are homotopic `(loc. cit.)`.

When $K^{\bullet}$ is bounded below (resp. bounded above), one may take $L^{\bullet,\bullet}$ such that $L^{i,\bullet} =
0$ for $i < i_{0}$ (resp. $i > i_{0}$) if $K^{i} = 0$ for $i < i_{0}$ (resp. $i > i_{0}$) `(M, XVII, 1.3)`.

Suppose on the other hand that there exists an integer $n$ such that every object of $\mathcal{C}$ admits an injective
resolution of length $\leq n$; then one may suppose that $L^{i,j} = 0$ for $j > n$ `(M, XVII, 1.4)`.

**11.4.3.**

<!-- label: 0_III.11.4.3 -->

Let now $T$ be a *covariant additive functor* from $\mathcal{C}$ to an abelian category $\mathcal{C}'$. Given a complex
$K^{\bullet}$ of $\mathcal{C}$ and an injective Cartan–Eilenberg resolution $L^{\bullet,\bullet}$ of $K^{\bullet}$,
suppose that the (simple) complex defined by the bicomplex $T(L^{\bullet,\bullet})$ exists (cf. `11.3.1`); then the two
spectral sequences $'E(T(L^{\bullet,\bullet}))$ and $''E(T(L^{\bullet,\bullet}))$ of this bicomplex are called the
*spectral sequences of hypercohomology of $T$ with respect to the complex $K^{\bullet}$*; by virtue of `(11.4.2)` and
`(11.3.2)`, they in fact depend only on $K^{\bullet}$ and not on the chosen injective Cartan–Eilenberg resolution
$L^{\bullet,\bullet}$; moreover, they depend *functorially* on $K^{\bullet}$. They have a common abutment
$H^{\bullet}(T(L^{\bullet,\bullet}))$, called the *hypercohomology of $T$ with respect to $K^{\bullet}$*, and denoted
$R^{\bullet }T(K^{\bullet})$. One shows that the terms `E_2` of the two preceding spectral sequences are given by

$$ 'E^{p,q}_{2} = H^{p}(R^{qT}(K^{\bullet})) (11.4.3.1) ''E^{p,q}_{2} = R^{pT}(H^{q}(K^{\bullet})) (11.4.3.2) $$

<!-- original page 378 -->

$R^{pT}$ denoting as usual the $p$th derived functor of $T$ for $p \in \mathbb{Z}$; $R^{\bullet }T(K^{\bullet})$ denotes
the complex $(R^{pT}(K^{i}))_{p \in \mathbb{Z}}$. Unless expressly stated otherwise, *we shall henceforth assume that
every object of $\mathcal{C}$ is a subobject of an injective object of $\mathcal{C}$*, so that injective
Cartan–Eilenberg resolutions exist for every complex of $\mathcal{C}$. Since $L^{i,j} = 0$ for $j < 0$, the criteria of
`(11.3.3)` show that the two hypercohomology spectral sequences of $T$ with respect to $K^{\bullet}$ exist and are
*biregular* in each of the two following cases: 1° $K^{\bullet}$ is bounded below; 2° every object of $\mathcal{C}$
admits an injective resolution of length at most equal to an integer $n$ (independent of the object considered). Indeed,
in the first case, one may suppose `(11.4.2)` that there exists $i_{0}$ such that $L^{i,j} = 0$ for $i < i_{0}$, and in
the second that there exists $j_{1}$ such that $L^{i,j} = 0$ for $j > j_{1}$; in each of the two cases, it is moreover
clear that for given $n$, there are only finitely many pairs $(i, j)$ such that $L^{i,j} \neq 0$ and $i + j = n$, which
establishes our assertions.

When one supposes that in $\mathcal{C}'$ filtered inductive limits exist and are exact (which implies in particular the
existence in $\mathcal{C}'$ of infinite direct sums), then the complex defined by the bicomplex $T(L^{\bullet,\bullet})$
exists, and criterion `(11.3.3)` shows that the spectral sequence $'E(T(L^{\bullet,\bullet}))$ is always regular.

**11.4.4.**

<!-- label: 0_III.11.4.4 -->

When $K^{\bullet}$ is a complex all of whose terms $K^{i}$ are zero except for a single $K^{i_{0}}$,
$R^{nT}(K^{\bullet})$ is isomorphic to $R^{n-i_{0}}T(K^{i_{0}})$, as follows at once from the definitions on taking a
Cartan–Eilenberg resolution $L^{\bullet,\bullet}$ such that $L^{i,j} = 0$ for $i \neq i_{0}$.

If $K^{\bullet}$ and $K'^{\bullet}$ are two complexes of $\mathcal{C}$, $f$, $g$ two homotopic morphisms from
$K^{\bullet}$ to $K'^{\bullet}$, then the morphisms $R^{\bullet }T(K^{\bullet}) \to R^{\bullet }T(K'^{\bullet})$ deduced
from $f$ and $g$ are identical, and likewise for the morphisms of the cohomology spectral sequences.

**Proposition (11.4.5).**

<!-- label: 0_III.11.4.5 -->

Suppose that in $\mathcal{C}'$ filtered inductive limits exist and are exact. If $R^{nT}(K^{i}) = 0$ for every $n > 0$
and every $i \in \mathbb{Z}$, one has functorial isomorphisms

$$ R^{iT}(K^{\bullet}) \xrightarrow{\sim} H^{i}(T(K^{\bullet})) (11.4.5.1) $$

for $i \in \mathbb{Z}$.

**Proof.** The only nonzero terms `E_2` of the first spectral sequence `(11.4.3.1)` are then $'E^{p,0}_{2} =
H^{p}(T(K^{\bullet}))$; in other words, this sequence is *degenerate*; since it is regular `(11.4.4)`, the conclusion
follows from `(11.1.6)`.

**11.4.6.**

<!-- label: 0_III.11.4.6 -->

Consider now, for example, a *covariant bifunctor* $(M, N) \mapsto T(M, N)$ from $\mathcal{C} \times \mathcal{C}'$ to
$\mathcal{C}''$, where $\mathcal{C}$, $\mathcal{C}'$, $\mathcal{C}''$ are three abelian categories; one assumes, for
simplicity, that $T$ is additive in each of its arguments, and moreover that every object of $\mathcal{C}$ and every
object of $\mathcal{C}'$ is a subobject of an injective object, and that filtered inductive limits exist in
$\mathcal{C}''$ and are exact. One then defines the *hypercohomology of $T$* with respect to two complexes
$K^{\bullet}$, $K'^{\bullet}$ of $\mathcal{C}$ and $\mathcal{C}'$ respectively, with derivation operators of degree
`+1`, by taking for $K^{\bullet}$ (resp. $K'^{\bullet}$) an injective Cartan–Eilenberg resolution $L^{\bullet,\bullet}$
(resp. $L'^{\bullet,\bullet}$); then $T(L^{\bullet,\bullet}, L'^{\bullet,\bullet})$ is a quadricomplex of
$\mathcal{C}''$, which one regards as a bicomplex of $\mathcal{C}''$ by taking as degrees of $T(L^{i,j}, L'^{h,k})$ the
integers $i + h$ and $j + k$. The *hypercohomology of $T$* with respect to $K^{\bullet}$ and $K'^{\bullet}$ is by
definition the cohomology $H^{\bullet}(T(L^{\bullet,\bullet}, L'^{\bullet,\bullet}))$ of this bicomplex (in other words,
that of the associated simple complex),

<!-- original page 379 -->

denoted $R^{\bullet }T(K^{\bullet}, K'^{\bullet})$; it is the abutment of two spectral sequences whose terms `E_2` are
given by

```text
  'E_2^{p,q} = H^p(R^qT(K^•, K'^•))                                            (11.4.6.1)
  ″E_2^{p,q} = ⊕_{q'+q″=q} R^pT(H^{q'}(K^•), H^{q″}(K'^•))   (cf. M, XVII, 2). (11.4.6.2)
```

Here $R^{\bullet }T(K^{\bullet}, K'^{\bullet})$ is the bicomplex $(R^{\bullet }T(K^{i}, K'^{j}))_{(i,j) \in \mathbb{Z}
\times \mathbb{Z}}$ and the second member of `(11.4.6.1)` is its cohomology when one regards it as a simple complex.

Moreover, the first spectral sequence is always regular, and the two spectral sequences are biregular when there exists
$n$ such that every object of $\mathcal{C}$ and every object of $\mathcal{C}'$ admits an injective resolution of length
$\leq n$, or when $K^{\bullet}$ and $K'^{\bullet}$ are bounded below; in the latter case, one may moreover omit the
hypothesis that inductive limits exist in $\mathcal{C}$ and $\mathcal{C}'$.

If $K^{\bullet}_{1}$, $K_{1}'^{\bullet}$ are two other complexes of $\mathcal{C}$ and $\mathcal{C}'$ respectively, $f$,
$g$ two homotopic morphisms from $K^{\bullet}$ to $K^{\bullet}_{1}$, $f'$, $g'$ two homotopic morphisms from
$K'^{\bullet}$ to $K_{1}'^{\bullet}$, then the morphisms $R^{\bullet }T(K^{\bullet}, K'^{\bullet}) \to R^{\bullet
}T(K^{\bullet}_{1}, K_{1}'^{\bullet})$ deduced from $f$ and $f'$ on the one hand, from $g$ and $g'$ on the other, are
identical, and likewise for the morphisms of the hypercohomology spectral sequences.

One generalizes easily to any covariant additive multifunctor.

**Proposition (11.4.7).**

<!-- label: 0_III.11.4.7 -->

Suppose that for every injective object $I$ of $\mathcal{C}$ (resp. $I'$ of $\mathcal{C}'$), $A' \mapsto T(I, A')$
(resp. $A \mapsto T(A, I')$) is an exact functor. Then, with the notation of `(11.4.6)`, one has canonical isomorphisms

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, K'^•)) ⥲ H^•(T(K^•, L'^{•,•}))               (11.4.7.1)
```

where the last two terms are the cohomology of the simple complexes defined by the tricomplexes $T(L^{\bullet,\bullet},
K'^{\bullet})$ and $T(K^{\bullet}, L'^{\bullet,\bullet})$ respectively.

**Proof.** Let us define, for example, the first of these isomorphisms. The quadricomplex $T(L^{\bullet,\bullet},
L'^{\bullet,\bullet})$ can be considered as a bicomplex, by taking as degrees of $T(L^{i,j}, L'^{h,k})$ the numbers $i +
j + h$ and $k$. As for each $h$, $L'^{h,\bullet}$ is a resolution of $K'^{h}$, one has, for this bicomplex, by virtue of
the hypothesis on $T$, $H^{q}_{II}(T(L^{\bullet,\bullet}, L'^{\bullet,\bullet})) = 0$ for $q \neq 0$ and
$H^{0}_{II}(T(L^{\bullet,\bullet}, L'^{\bullet,\bullet})) = T(L^{\bullet,\bullet}, K'^{\bullet})$; the first spectral
sequence of this bicomplex is therefore degenerate; since $L'^{h,k} = 0$ for $k < 0$, this sequence is moreover regular
`(11.3.3)`, and the conclusion follows from `(11.1.6)`.

One has analogous results for a covariant multifunctor in any number $n$ of arguments: in computing the hypercohomology,
it is not necessary to replace *all* the complexes by a Cartan–Eilenberg resolution, but only $n - 1$ of them, provided
that when one fixes any $n - 1$ arguments giving them as values injective objects, the covariant functor in the
remaining argument is *exact*.

### 11.5. Passage to the inductive limit in hypercohomology

**Lemma (11.5.1).**

<!-- label: 0_III.11.5.1 -->

Let $K^{\bullet} = (K^{i})_{i \in \mathbb{Z}}$ be a complex of $\mathcal{C}$, and for every integer $r \in \mathbb{Z}$,
let $K^{\bullet}_{(r)}$ be the complex such that $K^{i}_{(r)} = 0$ for $i < r$, $K^{i}_{(r)} = K^{i}$ for $i \geq r$.
Let $T$ be a covariant additive functor

<!-- original page 380 -->

from $\mathcal{C}$ to $\mathcal{C}'$, commuting with inductive limits (one assumes that filtered inductive limits exist
and are exact in $\mathcal{C}$ and $\mathcal{C}'$). Then $R^{\bullet }T(K^{\bullet})$ is isomorphic to the inductive
limit $\varinjlim R^{\bullet }T(K^{\bullet}_{(r)})$ as $r$ tends to $-\infty$.

**Proof.** The construction of an injective Cartan–Eilenberg resolution of $K^{\bullet}$ is performed by choosing
arbitrarily, for each $i$, an injective resolution $(X^{i,j}_{B})_{j \geq 0}$ of $B^{i}(K^{\bullet})$ and an injective
resolution $(X^{i,j}_{H})_{j \geq 0}$ of $H^{i}(K^{\bullet})$; that done, the method of construction shows that the
injective resolution $(L^{i,j})_{j \geq 0}$ of $K^{i}$ and the derivation operators $L^{i,j} \to L^{i+1,j}$ depend only
on the resolutions $(X^{i,\bullet}_{B})$, $(X^{i,\bullet}_{H})$ and $(X^{i+1,\bullet}_{B})$ `(M, XVII, 1.2)`. Now, it is
clear that one has $B^{i}(K^{\bullet}_{(r)}) = B^{i}(K^{\bullet})$ and $H^{i}(K^{\bullet}_{(r)}) = H^{i}(K^{\bullet})$
for $i \geq r + 1$. One has, on the other hand, for each $r$, a canonical injection $\phi_{r-1, r} : K^{\bullet}_{(r)}
\to K^{\bullet}_{(r-1)}$, $\phi_{r-1, r}$ being the identity for $i \neq r - 1$. The preceding remark shows that if
$L^{\bullet,\bullet} = (L^{i,j})$ is an injective Cartan–Eilenberg resolution of $K^{\bullet}$, one can for each $r$
define an injective Cartan–Eilenberg resolution $L^{\bullet,\bullet}_{(r)} = (L^{i,j}_{(r)})$ of $K^{\bullet}_{(r)}$
such that $L^{i,j}_{(r)} = 0$ for $i < r$ and $L^{i,j}_{(r)} = L^{i,j}$ for $i \geq r + 1$. One can, on the other hand,
define a morphism of bicomplexes $\Phi^{\bullet,\bullet}_{r-1, r} : L^{\bullet,\bullet}_{(r)} \to
L^{\bullet,\bullet}_{(r-1)}$ corresponding to $\phi_{r-1, r}$, and the method of definition of this morphism
`(loc. cit.)` shows once again that one may construct it so that $\Phi^{i,j}_{r-1, r}$ is the identity for $i \neq r$
and $i \neq r - 1$. One has thus defined an inductive system $(L^{\bullet,\bullet}_{(r)})$ of bicomplexes of
$\mathcal{C}$, of which $L^{\bullet,\bullet}$ is evidently the inductive limit as $r$ tends to $-\infty$; by reason of
the commutativity of direct sums and inductive limits, the simple complex associated to $L^{\bullet,\bullet}$ is also
the inductive limit of the simple complex associated to $L^{\bullet,\bullet}_{(r)}$. Since $T$ commutes by hypothesis
with inductive limits, and the same holds for cohomology (by exactness of the functor $\varinjlim$), one indeed has
$H^{\bullet}(T(L^{\bullet,\bullet})) = \varinjlim H^{\bullet}(T(L^{\bullet,\bullet}_{(r)}))$ up to isomorphism.

Lemma `(11.5.1)` allows one to extend to arbitrary complexes $K^{\bullet}$, by passage to the inductive limit,
properties valid for complexes *bounded below*. As a first example, we shall prove:

**Proposition (11.5.2).**

<!-- label: 0_III.11.5.2 -->

Under the hypotheses of `(11.5.1)` concerning $\mathcal{C}$, $\mathcal{C}'$ and $T$, $R^{\bullet }T(K^{\bullet})$ is a
cohomological functor in the abelian category of complexes of $\mathcal{C}$.

**Proof.** We show that we can reduce to the case of complexes bounded below: if one has an exact sequence $0 \to
K'^{\bullet} \to K^{\bullet} \to K''^{\bullet} \to 0$ of complexes, one evidently deduces from it for each $r$ an exact
sequence $0 \to K_{(r)}'^{\bullet} \to K^{\bullet}_{(r)} \to K_{(r)}''^{\bullet} \to 0$, whence by hypothesis an exact
sequence

```text
  … → R^nT(K_{(r)}'^•) → R^nT(K_{(r)}^•) → R^nT(K_{(r)}″^•) →^∂ R^{n+1}T(K_{(r)}'^•) → …
```

these exact sequences forming an inductive system; lemma `(11.5.1)` and the exactness of the functor $\varinjlim$ show
that one has an exact sequence

```text
  … → R^nT(K'^•) → R^nT(K^•) → R^nT(K″^•) →^∂ R^{n+1}T(K'^•) → …
```

To deal with the case of complexes bounded below, we may confine ourselves to those for which $K^{i} = 0$ for $i < 0$;
these evidently form an abelian category $\mathcal{K}$.

**Lemma (11.5.2.1).**

<!-- label: 0_III.11.5.2.1 -->

In $\mathcal{K}$, let $\mathcal{J}$ be the set of complexes $Q^{\bullet} = (Q^{i})_{i \geq 0}$ having the

<!-- original page 381 -->

following properties: 1° Every $Q^{i}$ is an injective object of $\mathcal{C}$; 2° For every $i \geq 0$, one has
$Z^{i}(Q^{\bullet}) = B^{i}(Q^{\bullet})$, and $Z^{i}(Q^{\bullet})$ is a direct factor of $Q^{i}$. Then:

(i) Every $Q^{\bullet} \in \mathcal{J}$ is an injective object of $\mathcal{K}$.

(ii) Every object of $\mathcal{K}$ is isomorphic to a subcomplex of a complex belonging to $\mathcal{J}$.

**Proof.** (i) Let $A^{\bullet} = (A^{i})$ be an object of $\mathcal{K}$, $A'^{\bullet} = (A'^{i})$ a subobject of
$A^{\bullet}$, $Q^{\bullet} = (Q^{i})$ an object of $\mathcal{J}$, and suppose given a morphism $f = (f^{i}) :
A'^{\bullet} \to Q^{\bullet}$, which we wish to extend to a morphism $g = (g^{i}) : A^{\bullet} \to Q^{\bullet}$. We
shall use the language of the category of modules for simplicity (cf. `[27]`).

We identify $Q^{i}$ with $B^{i}(Q^{\bullet}) \oplus B^{i+1}(Q^{\bullet})$; we proceed by induction on $i$, supposing
therefore the $g^{j}$ defined for $j < i$, compatible with the derivation operators $d^{j} : A^{j} \to A^{j+1}$ and
$d^{j} : Q^{j} \to Q^{j+1}$ for $j < i - 1$ and such moreover that: 1° $g^{i-1}(Z^{i-1}(A^{\bullet})) \subset
Z^{i-1}(Q^{\bullet})$; 2° If one sets $C^{j} = (d^{j})^{-1}(A'^{j+1})$ for every $j$, then $d^{i-1} \circ g^{i-1}$
coincides with $f^{i} \circ d^{i-1}$ on $C^{i-1}$. The morphism $f^{i} : A'^{i} \to Q^{i}$ gives, by composition with
the projections, two morphisms $f^{i'} : A'^{i} \to B^{i}(Q^{\bullet})$ and $f^{ii} : A'^{i} \to B^{i+1}(Q^{\bullet})$.
Since $d^{i-1} \circ g^{i-1}$ carries $A^{i-1}$ into $B^{i}(Q^{\bullet})$ and vanishes on $Z^{i-1}(A^{\bullet})$, it
defines a morphism $h^{i} : B^{i}(A^{\bullet}) \to B^{i}(Q^{\bullet})$, and since $d^{i-1} \circ g^{i-1}$ coincides with
$f^{i} \circ d^{i-1}$ on $C^{i-1}$, $h^{i}$ coincides with $f^{i}_{1}$ on $B^{i}(A^{\bullet}) \cap A'^{i}$. Since
$B^{i}(Q^{\bullet})$, a direct factor of $Q^{i}$, is injective, there is a morphism $g^{i'} : A^{i} \to
B^{i}(Q^{\bullet})$ which coincides with $h^{i}$ on $B^{i}(A^{\bullet})$ and with $f^{i'}$ on $A'^{i}$. Consider on the
other hand the morphism $f^{ii+1} \circ d^{i} : C^{i} \to B^{i+1}(Q^{\bullet})$, which vanishes on $Z^{i}(A^{\bullet})$;
since $B^{i+1}(Q^{\bullet})$ is injective, there is a morphism $g^{ii} : A^{i} \to B^{i+1}(Q^{\bullet})$, which
coincides with $f^{ii+1} \circ d^{i}$ on $C^{i}$ and with `0` on $Z^{i}(A^{\bullet})$. It suffices then to take $g^{i} =
g^{i'} + g^{ii}$ to be able to continue the induction.

(ii) To embed $A^{\bullet} = (A^{i})$ in a complex belonging to $\mathcal{J}$, one takes for each $i \geq 1$ an
injective object $Q'^{i}$ of $\mathcal{C}$ such that there exists an injection $f'^{i} : A^{i} \to Q'^{i}$. Then set
$Q^{i} = 0$ for $i < 0$, $Q^{0} = Q'^{1}$ and $Q^{i} = Q'^{i} \oplus Q'^{i+1}$ for $i \geq 1$, with the obvious
derivation operator. Set $f^{i} = f'^{i+1} + (f'^{i+1} \circ d^{i})$ for every $i$ (with $f'^{i} = 0$ for $i \leq 0$);
it is immediate that $f^{i}$ is injective for every $i$, and that the $f^{i}$ are compatible with the derivation
operators.

**Corollary (11.5.2.2).**

<!-- label: 0_III.11.5.2.2 -->

Every object $K^{\bullet}$ of $\mathcal{K}$ admits a right resolution formed of objects of $\mathcal{J}$. If
$L^{\bullet,\bullet}$ is such a resolution, then for any resolution $L'^{\bullet,\bullet}$ of $K^{\bullet}$ formed of
objects of $\mathcal{K}$, there is a morphism of bicomplexes $F : L'^{\bullet,\bullet} \to L^{\bullet,\bullet}$
compatible with the augmentations, and any two such morphisms $F$, $F'$ are homotopic.

**Proof.** This is none other than `(M, V, 1.1 a))` applied to the abelian category $\mathcal{K}$.

**11.5.2.3.**

<!-- label: 0_III.11.5.2.3 -->

These preliminaries laid, consider an injective Cartan–Eilenberg resolution $L'^{\bullet,\bullet}$ of $K^{\bullet}$ and
a resolution $L^{\bullet,\bullet}$ of $K^{\bullet}$ formed of objects of $\mathcal{J}$, and let us show that one has an
isomorphism $H^{\bullet}(T(L'^{\bullet,\bullet})) \xrightarrow{\sim} H^{\bullet}(T(L^{\bullet,\bullet}))$. Indeed, one
deduces from `(11.5.2.2)` a morphism of bicomplexes $T(L'^{\bullet,\bullet}) \to T(L^{\bullet,\bullet})$, and
consequently a morphism $'E(T(L'^{\bullet,\bullet})) \to 'E(T(L^{\bullet,\bullet}))$ of the first spectral sequences of
these bicomplexes. Since by virtue of `(11.3.3)` these spectral sequences are regular, it suffices `(11.1.5)` to see
that the preceding morphism is an isomorphism for the terms `E_2`, or, equivalently, that $H^{q}_{II}(T(L^{i,\bullet}))$
is equal to $R^{qT}(K^{i})$; since $L^{i,\bullet}$ is a right resolution of $K^{i}$, one is reduced to proving the

<!-- original page 382 -->

**Lemma (11.5.2.4).**

<!-- label: 0_III.11.5.2.4 -->

If $L^{\bullet} = (L^{i})_{i \in \mathbb{Z}}$ is a right resolution of an object $A$ of $\mathcal{C}$ such that
$R^{nT}(L^{i}) = 0$ for every $i \in \mathbb{Z}$ and every $n > 0$, then one has $H^{\bullet }T(L^{\bullet}) =
R^{\bullet }T(A)$.

**Proof.** This is a particular case of `(T, 2.5.2)`.

**11.5.2.5.**

<!-- label: 0_III.11.5.2.5 -->

The proof of `(11.5.2)` now concludes at once, for $L'^{\bullet,\bullet}$ is an injective resolution of $K^{\bullet}$ in
the abelian category $\mathcal{K}$; in other words, $K^{\bullet} \mapsto H^{\bullet}(T(L'^{\bullet,\bullet}))$ is none
other than the right-derived cohomological functor of $T$ in the category $\mathcal{K}$ `(T, 2.3)`.

**Proposition (11.5.3).**

<!-- label: 0_III.11.5.3 -->

Under the hypotheses of `(11.5.1)` concerning $\mathcal{C}$, $\mathcal{C}'$ and $T$, let $L^{\bullet,\bullet} =
(L^{i,j})$ be a bicomplex such that $L^{i,j} = 0$ for $j < 0$ and such that, for every $i$, $L^{i,\bullet}$ is a
resolution of $K^{i}$; suppose finally that $R^{nT}(L^{i,j}) = 0$ for every pair $(i, j)$ and every $n > 0$. Then there
exists a functorial isomorphism

$$ R^{\bullet }T(K^{\bullet}) \xrightarrow{\sim} H^{\bullet}(T(L^{\bullet,\bullet})). (11.5.3.1) $$

**Proof.** Let $L^{\bullet,\bullet}_{(r)} = (L^{i,j}_{(r)})$ be the bicomplex such that $L^{i,j}_{(r)} = 0$ for $i < r$,
$L^{i,j}_{(r)} = L^{i,j}$ for $i \geq r$; it is immediate that $L^{\bullet,\bullet}$ is the inductive limit of
$L^{\bullet,\bullet}_{(r)}$ as $r$ tends to $-\infty$; by virtue of the hypothesis on $T$ and of `(11.5.1)`, it suffices
therefore to prove the proposition when $K^{\bullet}$ is bounded below, for example $K^{i} = 0$ for $i < 0$, and
$L^{i,j} = 0$ for $i < 0$. Let then $L'^{\bullet,\bullet} = (L'^{i,j})$ be a right resolution of $K^{\bullet}$ formed of
objects of $\mathcal{J}$ `(11.5.2.2)`; there is a morphism of bicomplexes $L^{\bullet,\bullet} \to L'^{\bullet,\bullet}$
compatible with the augmentations, whence a morphism $'E(T(L^{\bullet,\bullet})) \to 'E(T(L'^{\bullet,\bullet}))$ for
the first spectral sequences; lemma `(11.5.2.4)` shows, as in `(11.5.2.3)`, that this morphism is an isomorphism, whence
the conclusion.

**Remark (11.5.4).**

<!-- label: 0_III.11.5.4 -->

The preceding arguments prove that the conclusions of `(11.5.2)` and `(11.5.3)` are valid in the category of complexes
$K^{\bullet}$ bounded below, without supposing that $T$ commutes with filtered inductive limits. Moreover, when one
considers only the category $\mathcal{K}$ of complexes $K^{\bullet}$ such that $K^{i} = 0$ for $i < 0$, the
characterization of $R^{\bullet }T(K^{\bullet})$ as the system of right-derived functors of $T$ in $\mathcal{K}$ shows
that this cohomological functor is *universal* `(T, 2.3)`.

Another case in which `(11.5.2)` is valid without making any additional hypothesis on $T$ is the case where there exists
an integer $m > 0$ such that every object of $\mathcal{C}$ admits an injective resolution of length $\leq m$. Indeed, in
the proof of `(11.5.1)`, all the injective resolutions of objects of $\mathcal{C}$ that intervene may be taken of length
$\leq m$, whence it follows at once that the terms of total degree $n$ of the bicomplex $T(L^{\bullet,\bullet}_{(r)})$
are equal to those of $T(L^{\bullet,\bullet})$ and finite in number, as soon as $r$ is sufficiently large; this entails
that for every $n$, $H^{n}(T(L^{\bullet,\bullet})) = H^{n}(T(L^{\bullet,\bullet}_{(r)}))$ as soon as $r$ is sufficiently
large. With the notation of `(11.5.2)`, one therefore also has $R^{nT}(K^{\bullet}_{(r)}) = R^{nT}(K^{\bullet})$ for $r$
sufficiently large (depending on $n$), and likewise for $K'^{\bullet}$ and $K''^{\bullet}$, whence the conclusion. In
the same way, `(11.5.3)` is valid without additional condition on $T$ when $\mathcal{C}$ satisfies the preceding
hypothesis and one supposes that the resolutions $L^{i,\bullet}$ are of length $\leq m$.

**11.5.5.**

<!-- label: 0_III.11.5.5 -->

The result of `(11.5.2)` generalizes to covariant multifunctors. Consider for example the situation of `(11.4.6)`, where
one supposes that in $\mathcal{C}$, $\mathcal{C}'$ and $\mathcal{C}''$

<!-- original page 383 -->

filtered inductive limits exist and are exact, and that $T$ commutes with inductive limits. Then $R^{\bullet
}T(K^{\bullet}, K'^{\bullet})$ is a *bifunctor* cohomological in each of the complexes $K^{\bullet}$, $K'^{\bullet}$; to
see this, one reduces as in `(11.5.2)` to the case where $K^{\bullet}$ and $K'^{\bullet}$ are bounded below; taking then
injective resolutions of $K^{\bullet}$ and $K'^{\bullet}$ of the type described in `(11.5.2.2)`, one is reduced to the
general property proved in `(M, V, 4.1)`.

**11.5.6.**

<!-- label: 0_III.11.5.6 -->

Similarly, the results of `(11.4.7)` and `(11.5.3)` generalize as follows. Suppose (under the hypotheses of `(11.5.5)`)
that one has two bicomplexes $L^{\bullet,\bullet} = (L^{i,j})$, $L'^{\bullet,\bullet} = (L'^{i,j})$ such that $L^{i,j} =
0$ and $L'^{i,j} = 0$ for $j < 0$, that for every $i$, $L^{i,\bullet}$ is a resolution of $K^{i}$ and $L'^{i,\bullet}$
is a resolution of $K'^{i}$, and finally that $R^{nT}(L^{i,j}, L'^{h,k}) = 0$ for $n > 0$ and for every system of
indices $(i, j, h, k)$. Then one has a functorial isomorphism in $K^{\bullet}$ and $K'^{\bullet}$

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, L'^{•,•})).                                  (11.5.6.1)
```

This is established as in `(11.5.3)` by reducing to the case where $K^{\bullet}$ and $K'^{\bullet}$ are bounded below.

Suppose moreover that for every pair $(i, j)$ and for every pair $(h, k)$, the functors $A \mapsto T(A, L'^{h,k})$ and
$A' \mapsto T(L^{i,j}, A')$ are exact in $\mathcal{C}$ and $\mathcal{C}'$ respectively. Then one also has functorial
isomorphisms

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, K'^•)) ⥲ H^•(T(K^•, L'^{•,•})).              (11.5.6.2)
```

The proof is similar to that of `(11.4.7)`.

**11.5.7.**

<!-- label: 0_III.11.5.7 -->

One again notes that the results of `(11.5.5)` and `(11.5.6)` are valid without supposing that $T$ commutes with
inductive limits, provided one restricts oneself to complexes $K^{\bullet}$, $K'^{\bullet}$ bounded below, or one
supposes that every object of $\mathcal{C}$ (resp. $\mathcal{C}'$) admits an injective resolution of bounded length, and
that in `(11.5.6)` the bicomplexes $L^{\bullet,\bullet}$ and $L'^{\bullet,\bullet}$ have their second degree bounded
above.

### 11.6. Hyperhomology of a functor with respect to a complex $K_{\bullet}$

**11.6.1.**

<!-- label: 0_III.11.6.1 -->

Let $\mathcal{C}$ be an abelian category, $K_{\bullet} = (K_{i})_{i \in \mathbb{Z}}$ a complex of objects of
$\mathcal{C}$ whose derivation operator is of degree $-1$. A *left Cartan–Eilenberg resolution* of $K_{\bullet}$
consists of a bicomplex $L_{\bullet,\bullet} = (L_{i,j})$ with derivation operators of degree $-1$ with $L_{i,j} = 0$
for $j < 0$, and a morphism of simple complexes $\epsilon : L_{\bullet,0} \to K_{\bullet}$, such that the conditions
obtained from those of `(11.4.2)` by "reversal of arrows" are satisfied. If every object of $\mathcal{C}$ is a quotient
of a projective object, every complex $K_{\bullet}$ of $\mathcal{C}$ admits a *projective* Cartan–Eilenberg resolution,
that is, one formed of projective objects $L_{i,j}$, with functorial properties similar to those of `(11.4.2)`.
Moreover, if $K_{\bullet}$ is bounded below (resp. bounded above), one may suppose that $L_{i,j} = 0$ for $i < i_{0}$
(resp. $i > i_{0}$) if $K_{i} = 0$ for $i < i_{0}$ (resp. $i > i_{0}$). If every object of $\mathcal{C}$ admits a
projective resolution of length $\leq n$, one may suppose that $L_{i,j} = 0$ for $j > n$.

<!-- original page 384 -->

**11.6.2.**

<!-- label: 0_III.11.6.2 -->

Suppose that $T$ is a *covariant additive functor* from $\mathcal{C}$ to an abelian category $\mathcal{C}'$. The
definition of the *hyperhomology* $L_{\bullet }T(K_{\bullet})$ and of the *spectral sequences of hyperhomology* of $T$
with respect to a complex $K_{\bullet}$ of $\mathcal{C}$ (when they exist) is performed again from `(11.4.3)` by
"reversal of arrows", the terms $E^{2}$ of the two spectral sequences thus obtained being

$$ 'E^{2}_{p,q} = H_{p}(L_{qT}(K_{\bullet})) (11.6.2.1) ''E^{2}_{p,q} = L_{pT}(H_{q}(K_{\bullet})) (11.6.2.2) $$

where $L_{pT}$ denotes the $p$th derived functor of $T$ for $p \geq 0$, and `0` for $p < 0$; $L_{\bullet
}T(K_{\bullet})$ denotes the complex $(L_{qT}(K_{i}))_{i \in \mathbb{Z}}$.

The properties of hyperhomology are not all deducible by simple "reversal of arrows" from those of hypercohomology
(unless one makes additional hypotheses of type AB 5\*) of `T, 1.5` on the category $\mathcal{C}'$) because of the
regularity conditions on the two preceding spectral sequences, to which one must this time apply the criteria of
`(11.3.4)`. These last show that when one supposes that in $\mathcal{C}'$ filtered inductive limits exist and are exact,
then the complex defined by the bicomplex $T(L_{\bullet,\bullet})$ exists, and the second spectral sequence
$''E(T(L_{\bullet,\bullet}))$ is this time regular. If one supposes either that $K_{\bullet}$ is bounded below, or that
there exists an integer $n$ such that every object of $\mathcal{C}$ admits a projective resolution of length $\leq n$,
then the *two* hyperhomology spectral sequences exist (without hypothesis on $\mathcal{C}'$) and are biregular.

**Proposition (11.6.3).**

<!-- label: 0_III.11.6.3 -->

Let $\mathcal{C}$, $\mathcal{C}'$ be two abelian categories, $T$ a covariant additive functor from $\mathcal{C}$ to
$\mathcal{C}'$. Then:

(i) Hyperhomology $L_{\bullet }T(K_{\bullet})$ is a homological functor in the abelian category of complexes of
$\mathcal{C}$ bounded below.

(ii) Let $K_{\bullet}$ be a complex of $\mathcal{C}$ bounded below. If $L_{nT}(K_{i}) = 0$ for every $n > 0$ and every
$i \in \mathbb{Z}$, one has functorial isomorphisms

$$ L_{iT}(K_{\bullet}) \xrightarrow{\sim} H_{i}(T(K_{\bullet})) (11.6.3.1) $$

for $i \in \mathbb{Z}$.

(iii) Let $K_{\bullet}$ be a complex of $\mathcal{C}$ bounded below. Let $L_{\bullet,\bullet} = (L_{i,j})$ be a
bicomplex such that $L_{i,j} = 0$ for $j < 0$ and such that, for every $i$, $L_{i,\bullet}$ is a resolution of $K_{i}$;
suppose finally that $L_{nT}(L_{i,j}) = 0$ for every pair $(i, j)$ and every $n > 0$. Then there exists a functorial
isomorphism

$$ L_{\bullet }T(K_{\bullet}) \xrightarrow{\sim} H_{\bullet}(T(L_{\bullet,\bullet})). (11.6.3.2) $$

The proofs proceed as those of `(11.5.2)`, `(11.4.5)` and `(11.5.3)` in the case of complexes bounded below. We leave
the details of these arguments to the reader.

**11.6.4.**

<!-- label: 0_III.11.6.4 -->

One has entirely analogous results for covariant multifunctors additive in each of the arguments. For example, for a
bifunctor $T$, one has the two hyperhomology spectral sequences with terms $E^{2}$ given by

<!-- original page 385 -->

```text
  'E_{p,q}^2 = H_p(L_qT(K_•, K_•'))                                            (11.6.4.1)
  ″E_{p,q}^2 = ⊕_{q'+q″=q} L_pT(H_{q'}(K_•), H_{q″}(K_•')).                    (11.6.4.2)
```

Here too, it is the *second* spectral sequence which is regular, the two sequences being biregular when one deals with
complexes $K_{\bullet}$, $K_{\bullet}'$ bounded below, or when the objects of the abelian categories considered have
projective resolutions of fixed length.

Moreover:

**Proposition (11.6.5).**

<!-- label: 0_III.11.6.5 -->

Let $\mathcal{C}$, $\mathcal{C}'$, $\mathcal{C}''$ be three abelian categories, $T$ a covariant bifunctor biadditive
from $\mathcal{C} \times \mathcal{C}'$ to $\mathcal{C}''$.

(i) $L_{\bullet }T(K_{\bullet}, K_{\bullet}')$ is a homological bifunctor in each of the complexes bounded below
$K_{\bullet}$, $K_{\bullet}'$ (formed respectively of objects of $\mathcal{C}$ and of objects of $\mathcal{C}'$).

(ii) Suppose $K_{\bullet}$ and $K_{\bullet}'$ bounded below. Let $L_{\bullet,\bullet} = (L_{i,j})$,
$L_{\bullet,\bullet}' = (L_{i,j}')$ be two bicomplexes such that $L_{i,j} = 0$ and $L_{i,j}' = 0$ for $j < 0$, such that
for every $i$, $L_{i,\bullet}$ is a resolution of $K_{i}$ and $L_{i,\bullet}'$ is a resolution of $K_{i}'$, and finally
that $L_{nT}(L_{i,j}, L_{h,k}') = 0$ for $n > 0$ and every system $(i, j, h, k)$. Then one has a functorial isomorphism

```text
  L_•T(K_•, K_•') ⥲ H_•(T(L_{•,•}, L_{•,•}')).                                 (11.6.5.1)
```

(iii) Suppose moreover that for every pair $(i, j)$ and every pair $(h, k)$, the functors $A \mapsto T(A, L_{h,k}')$ and
$A' \mapsto T(L_{i,j}, A')$ are exact in $\mathcal{C}$ and $\mathcal{C}'$ respectively. Then one has functorial
isomorphisms

```text
  L_•T(K_•, K_•') ⥲ H_•(T(L_{•,•}, K_•')) ⥲ H_•(T(K_•, L_{•,•}')).             (11.6.5.2)
```

The proofs are analogous to those of `(11.5.5)` and `(11.5.6)`.

### 11.7. Hyperhomology of a functor with respect to a bicomplex $K_{\bullet,\bullet}$

**11.7.1.**

<!-- label: 0_III.11.7.1 -->

Let $\mathcal{C}$ be an abelian category in which every object is a quotient of a projective object. Consider a
bicomplex $K_{\bullet,\bullet} = (K_{i,j})$ formed of objects of $\mathcal{C}$, and *whose two degrees are bounded
below*; one may always restrict to the case where $K_{i,j} = 0$ for $i < 0$ or $j < 0$, and this is what we shall do
henceforth. One may consider $K_{\bullet,\bullet}$ as a (simple) complex formed of objects $K_{i,\bullet} = (K_{i,j})_{j
\geq 0}$ of the abelian category $\mathcal{K}$ of complexes of positive degrees of objects of $\mathcal{C}$. It follows
from lemma `(11.5.2.1)` (or rather from the "dual" lemma obtained by "reversal of arrows") and from `(M, V, 2.2)` that
$K_{\bullet,\bullet}$ admits a *projective Cartan–Eilenberg resolution* in the category $\mathcal{K}$; such a resolution
is a tricomplex $M_{\bullet,\bullet,\bullet} = (M_{i,j,k})$ of $\mathcal{C}$, with all degrees $\geq 0$, formed of
projective objects, such that for every $i$, $M_{i,\bullet,\bullet}$, $B^{I}_{j}(M_{\bullet,\bullet,\bullet})$,
$Z^{I}_{j}(M_{\bullet,\bullet,\bullet})$, $H^{I}_{j}(M_{\bullet,\bullet,\bullet})$ constitute projective resolutions of
$K_{i,\bullet}$, $B^{I}_{j}(K_{\bullet,\bullet})$, $Z^{I}_{j}(K_{\bullet,\bullet})$, $H^{I}_{j}(K_{\bullet,\bullet})$
respectively in the category $\mathcal{K}$; in particular, for every pair $(i, j)$, $M_{i,j,\bullet}$ is a projective
resolution of $K_{i,j}$ in $\mathcal{C}$.

**Proposition (11.7.2).**

<!-- label: 0_III.11.7.2 -->

Let $T$ be a covariant additive functor from $\mathcal{C}$ to an abelian category $\mathcal{C}'$. With the notation of
`(11.7.1)`, the homology $H_{\bullet}(T(M_{\bullet,\bullet,\bullet}))$ of the simple complex associated to the
tricomplex $T(M_{\bullet,\bullet,\bullet})$ is canonically isomorphic to the hyperhomology $L_{\bullet }T(K_{\bullet})$
of the

<!-- original page 386 -->

simple complex associated to $K_{\bullet,\bullet}$ `(11.6.2)`, and is the common abutment of *six biregular spectral
sequences* denoted ${}^{(t)}E$ (with $t = a$, $b$, $a'$, $b'$, $c$, or $d$), whose terms $E^{2}$ are given by the
formulas

$$ {}^{(a)}E^{2}_{p,q} = L_{pT}(H^{I}_{q}(K_{\bullet,\bullet})) {}^{(b)}E^{2}_{p,q} =
H_{p}(L^{II}_{q}T(K_{\bullet,\bullet})) {}^{(a')}E^{2}_{p,q} = L_{pT}(H^{II}_{q}(K_{\bullet,\bullet}))
{}^{(b')}E^{2}_{p,q} = H_{p}(L^{I}_{q} T(K_{\bullet,\bullet})) {}^{(c)}E^{2}_{p,q} = L_{pT}(H_{q}(K_{\bullet,\bullet}))
{}^{(d)}E^{2}_{p,q} = H_{p}(L^{I}_{q} T(K_{\bullet,\bullet})) $$

(Recall that we use the notation $F(A_{\bullet})$ to denote the complex of objects $F(A_{i})$ for every complex
$A_{\bullet} = (A_{i})$; for example $L^{II}_{q}T(K_{\bullet,\bullet})$ denotes the complex
$(L^{II}_{q}T(K_{i,\bullet}))_{i \geq 0}$, where $L^{II}_{q}T(K_{i,\bullet})$ is the hyperhomology of index $q$ of the
functor $T$ with respect to the simple complex $K_{i,\bullet}$.)

**Proof.** Denote by $L_{\bullet}$ the simple complex associated to $K_{\bullet,\bullet}$, so that $L_{i} =
\oplus_{r+s=i} K_{r,s}$, and set $N_{i,\bullet} = \oplus_{r+s=i} M_{r,s,\bullet}$; it is clear that for each $i$,
$N_{i,\bullet}$ is a projective resolution of $L_{i}$ in $\mathcal{C}$; therefore by `(11.6.3)` and `(11.6.4)`, one has
a functorial isomorphism $L_{\bullet }T(L_{\bullet}) \xrightarrow{\sim} H_{\bullet}(T(N_{\bullet,\bullet}))$; as the
simple complex associated to the bicomplex $T(N_{\bullet,\bullet})$ is also associated to the tricomplex
$T(M_{\bullet,\bullet,\bullet})$, this proves the first assertion of the statement.

Moreover, $L_{\bullet }T(L_{\bullet})$ is the abutment of the two hyperhomology spectral sequences `(11.6.2)` of $T$
relative to the simple complex $L_{\bullet}$, which are nothing other than the sequences ${}^{(b')}E$ and ${}^{(b)}E$
respectively.

Consider now $M_{\bullet,\bullet,\bullet}$ as a bicomplex $U_{\bullet,\bullet}$ with $U_{i,j} = \oplus_{r+s=j}
M_{i,r,s}$; $H_{\bullet}(T(M_{\bullet,\bullet,\bullet}))$ is again the abutment of the two spectral sequences of the
bicomplex $T(U_{\bullet,\bullet})$. Now, for every $i$, $M_{i,\bullet,\bullet}$ is a bicomplex satisfying the conditions
of `(11.6.3)` relative to the simple complex $K_{i,\bullet}$; hence $H^{II}_{q}(T(U_{i,\bullet})) =
L^{II}_{q}T(K_{i,\bullet})$, and the first spectral sequence of $T(U_{\bullet,\bullet})$ is nothing other than
${}^{(b)}E$. On the other hand, for every $r$, $M_{\bullet,r,\bullet}$ is a Cartan–Eilenberg resolution of the simple
complex $K_{\bullet,r}$; the calculation done in `(M, XV, 2)` shows that $H^{I}_{q}(T(M_{\bullet,r_{\bullet},\bullet}))
= T(H^{I}_{q}(M_{\bullet,r_{\bullet},\bullet}))$, hence $H^{I}_{q}(T(U_{\bullet,\bullet})) = \oplus_{r+s=j}
T(H^{I}_{q}(M_{\bullet,r,s}))$; in other words, the simple complex $H^{I}_{q}(T(U_{\bullet,\bullet}))$ is nothing other
than the simple complex associated to the bicomplex $T(H^{I}_{q}(M_{\bullet,\bullet,\bullet}))$. Now, for every $q$,
$H^{I}_{q}(M_{\bullet,\bullet,\bullet})$ is a *projective resolution* of the simple complex
$H^{I}_{q}(K_{\bullet,\bullet})$ in the category $\mathcal{K}$; applying `(11.6.3)`, one sees that one has

$$ H^{II}_{p}(T(H^{I}_{q}(M_{\bullet,\bullet,\bullet}))) = L_{pT}(H^{I}_{q}(K_{\bullet,\bullet})), $$

and one thus obtains the sequence ${}^{(a)}E$. Finally, the sequences ${}^{(a')}E$ and ${}^{(c)}E$ are obtained by
interchanging the roles of the indices $i$ and $j$ in the definition of the tricomplex $M_{\bullet,\bullet,\bullet}$ and
applying to this new tricomplex the preceding arguments.

One says that $L_{\bullet }T(K_{\bullet,\bullet})$ is the *hyperhomology of $T$ relative to the bicomplex
$K_{\bullet,\bullet}$*.

**Remarks (11.7.3).**

<!-- label: 0_III.11.7.3 -->

(i) It follows from `(11.6.3)` that $L_{\bullet }T(K_{\bullet,\bullet})$ is a homological functor in the category of
bicomplexes $K_{\bullet,\bullet}$ of $\mathcal{C}$ bounded below in each of their degrees.

<!-- original page 387 -->

(ii) Let $M_{\bullet,\bullet,\bullet}$ be a tricomplex of $\mathcal{C}$ such that for each pair $(r, s)$,
$M_{r,s,\bullet}$ is a resolution of $K_{r,s}$ and that $L_{nT}(M_{ijk}) = 0$ for all triples $(i, j, k)$ and every $n >
0$. Then one has an isomorphism $L_{\bullet }T(K_{\bullet,\bullet}) \xrightarrow{\sim}
H_{\bullet}(T(M_{\bullet,\bullet,\bullet}))$; indeed, with the notation of the proof of `(11.7.2)`, $N_{i,\bullet}$ is a
resolution of $L_{i}$ such that $L_{nT}(N_{i,j}) = 0$ for $n > 0$ and every pair $(i, j)$, and it suffices to apply
`(11.6.3, (iii))`.

(iii) One generalizes at once the results of `(11.7.2)` to covariant multifunctors; for example, let $\mathcal{C}'$ be a
second abelian category in which every object is a quotient of a projective object, $K_{\bullet,\bullet}'$ a bicomplex
of $\mathcal{C}'$ whose two degrees are bounded below, and $T$ a covariant additive bifunctor from $\mathcal{C} \times
\mathcal{C}'$ to an abelian category $\mathcal{C}''$. If $L_{\bullet}$ and $L_{\bullet}'$ are the simple complexes
associated to $K_{\bullet,\bullet}$ and $K_{\bullet,\bullet}'$ respectively, one defines the hyperhomology of $T$ with
respect to the two bicomplexes $K_{\bullet,\bullet}$, $K_{\bullet,\bullet}'$ as the hyperhomology $L_{\bullet
}T(L_{\bullet}, L_{\bullet}')$; applying `(11.6.4)` and `(11.6.5)`, one has, as in `(11.7.2)`, six spectral sequences
abutting to this hyperhomology, which we leave the reader to write out.

### 11.8. Complements on the cohomology of simplicial complexes

**11.8.1.**

<!-- label: 0_III.11.8.1 -->

Let $A$ be a finite set, $\Sigma(A)$ the set of finite sequences $\sigma = (\alpha_{0}, \cdots, \alpha_{h})$ of elements
of $A$ ("simplices" of $A$); one sets $|\sigma| = {\alpha_{0}, \cdots, \alpha_{h}}$; recall that the *chain complex*
$C_{\bullet}(A)$ is the free graded abelian group generated by the elements of $\Sigma(A)$, $(\alpha_{0}, \cdots,
\alpha_{h})$ being of *degree $h$*, with a differential defined by

```text
  d(α_0, …, α_h) = ∑_{i=0}^h (−1)^i (α_0, …, α̂_i, …, α_h).
```

The subgroup $D_{\bullet}(A)$ of $C_{\bullet}(A)$ generated by the chains $\sigma = (\alpha_{0}, \cdots, \alpha_{h})$
for which two of the $\alpha_{i}$ are equal, and by the chains $\pi(\sigma) - \epsilon_{\pi} \cdot \sigma$, where for
every permutation $\pi$, $\pi(\sigma) = (\alpha_{\pi(0)}, \cdots, \alpha_{\pi(h)})$ and $\epsilon_{\pi}$ is the
signature of $\pi$, is a subcomplex of $C_{\bullet}(A)$ whose elements are called *degenerate chains*; one sets
$L_{\bullet}(A) = C_{\bullet}(A)/D_{\bullet}(A)$, and one has a natural homomorphism of complexes $p : C_{\bullet}(A)
\to L_{\bullet}(A)$. One defines on the other hand a homomorphism of complexes $j : L_{\bullet}(A) \to C_{\bullet}(A)$
as follows: one totally orders $A$; to the class mod. $D_{\bullet}(A)$ of a simplex $\sigma = (\alpha_{0}, \cdots,
\alpha_{h})$, one associates `0` if two of the $\alpha_{i}$ are equal, and the sequence $(\beta_{0}, \cdots, \beta_{h})$
of the $\alpha_{i}$ arranged *in increasing order* otherwise. It is clear that $p \circ j$ is the identity of
$L_{\bullet}(A)$.

**11.8.2.**

<!-- label: 0_III.11.8.2 -->

Let $B$ be a second finite set; if $d'$, $d''$ are the differentials of $C_{\bullet}(A)$ and $C_{\bullet}(B)$, the
tensor product complex $C_{\bullet}(A) \otimes C_{\bullet}(B)$ can be considered as the free abelian group generated by
the elements of $\Sigma(A) \times \Sigma(B)$, with the differential $d(\sigma, \tau) = (d'\sigma, \tau) +
(-1)^{h+1}(\sigma, d''\tau)$ if $Card |\sigma| = h + 1$.

The natural homomorphisms $C_{\bullet}(A) \to L_{\bullet}(A)$, $C_{\bullet}(B) \to L_{\bullet}(B)$ define a homomorphism
$p : C_{\bullet}(A) \otimes C_{\bullet}(B) \to L_{\bullet}(A) \otimes L_{\bullet}(B)$, this last tensor product being
isomorphic to $(C_{\bullet}(A) \otimes C_{\bullet}(B))/(C_{\bullet}(A) \otimes D_{\bullet}(B) + D_{\bullet}(A) \otimes
C_{\bullet}(B))$. Likewise, by means of the homomorphisms $L_{\bullet}(A) \to C_{\bullet}(A)$ and $L_{\bullet}(B) \to
C_{\bullet}(B)$ defined in `(11.8.1)` (by means of total orders on $A$ and $B$), one defines a homomorphism $j :
L_{\bullet}(A) \otimes L_{\bullet}(B) \to C_{\bullet}(A) \otimes C_{\bullet}(B)$ such that $p \circ j$ is the identity.

<!-- original page 388 -->

With this notation:

**Proposition (11.8.3).**

<!-- label: 0_III.11.8.3 -->

There exists a homotopy $h : C_{\bullet}(A) \otimes C_{\bullet}(B) \to C_{\bullet}(A) \otimes C_{\bullet}(B)$ such that
$h(\sigma, \tau)$ is a linear combination of pairs of simplices $(\sigma_{i}, \tau_{i})$ with $|\sigma_{i}| \subset
|\sigma|$, $|\tau_{i}| \subset |\tau|$, and such that for $f = j \circ p$ one has

```text
  f − 1 = h ∘ d + d ∘ h.                                                       (11.8.3.1)
```

**Proof.** It suffices to define $h$ on each pair $(\sigma, \tau)$ of simplices, reasoning by induction on the sum of
the degrees of $\sigma$ and $\tau$, since one can take $h = 0$ when this sum is `0`. Let $\omega = f(\sigma, \tau) -
(\sigma, \tau) - h(d(\sigma, \tau))$; by the induction hypothesis and the definition of $d$, one has $\omega \in
C_{\bullet}(|\sigma|) \otimes C_{\bullet}(|\tau|)$. One has

```text
  dω = f(d(σ, τ)) − d(σ, τ) − d(h(d(σ, τ))) = h(d(d(σ, τ))) = 0
```

by virtue of `(11.8.3.1)` and the induction hypothesis. Now, one has $H_{q}(C_{\bullet}(A)) = 0$ for $q > 0$
`(G, I, 3.7.4)`, hence also $H_{q}(C_{\bullet}(A) \otimes C_{\bullet}(B)) = 0$ for $q > 0$, by virtue of Künneth's
formula `(G, I, 5.5.2)`. Applying this remark on replacing $A$ by $|\sigma|$ and $B$ by $|\tau|$, one sees that there
exists an element $\omega'$ of $C_{\bullet}(|\sigma|) \otimes C_{\bullet}(|\tau|)$ such that $\omega = d\omega'$; taking
$h(\sigma, \tau) = \omega'$, one verifies `(11.8.3.1)` for the pair $(\sigma, \tau)$ and the induction can continue.

**11.8.4.**

<!-- label: 0_III.11.8.4 -->

The notation being that of `(11.8.2)`, we shall set $(\sigma, \tau) \leq (\sigma', \tau')$ if $|\sigma| \subset
|\sigma'|$ and $|\tau| \subset |\tau'|$. A *system of coefficients* $\mathcal{S}$ on $\Sigma(A) \times \Sigma(B)$
consists of a family $(\Gamma_{\sigma,\tau})$ of abelian groups, where $\Gamma_{\sigma,\tau}$ depends only on the sets
$|\sigma|$ and $|\tau|$, and a family of homomorphisms $\Gamma_{\sigma,\tau} \to \Gamma_{\sigma',\tau'}$ for $(\sigma,
\tau) \leq (\sigma', \tau')$, forming an *inductive system* for this preorder relation. One then defines a *cochain
complex* $C^{\bullet}(A, B; \mathcal{S})$ as the set of families $\lambda = (\lambda(\sigma, \tau))$ where $(\sigma,
\tau)$ runs over $\Sigma(A) \times \Sigma(B)$, with $\lambda(\sigma, \tau) \in \Gamma_{\sigma,\tau}$ for every pair
$(\sigma, \tau)$. The differential is given as follows: if $d(\sigma, \tau) = \sum_{i} \pm (\sigma_{i}, \tau_{i})$, one
has $|\sigma_{i}| \subset |\sigma|$, $|\tau_{i}| \subset |\tau|$ for every $i$, and one takes

```text
  dλ(σ, τ) = ∑_i ± λ_i(σ_i, τ_i),
```

where $\lambda_{i}(\sigma_{i}, \tau_{i})$ denotes the canonical image of $\lambda(\sigma_{i}, \tau_{i})$ in
$\Gamma_{\sigma,\tau}$.

We shall say that a cochain $\lambda \in C^{\bullet}(A, B; \mathcal{S})$ is *bi-alternating* if $\lambda(\sigma, \tau) =
0$ whenever one of the two simplices $\sigma$, $\tau$ has two equal terms, and if $\lambda(\pi(\sigma), \tau) =
\epsilon_{\pi} \lambda(\sigma, \tau)$ and $\lambda(\sigma, \pi'(\tau)) = \epsilon_{\pi'} \lambda(\sigma, \tau)$ for
arbitrary permutations $\pi$, $\pi'$ of the indices. It is clear that these cochains generate a subcomplex
$L^{\bullet}(A, B; \mathcal{S})$ of $C^{\bullet}(A, B; \mathcal{S})$.

**Proposition (11.8.5).**

<!-- label: 0_III.11.8.5 -->

The canonical injection $L^{\bullet}(A, B; \mathcal{S}) \to C^{\bullet}(A, B; \mathcal{S})$ defines an isomorphism for
the cohomology of these two complexes.

**Proof.** Note that if $p$ and $j$ have the meaning defined in `(11.8.2)`, the maps ${}^{t} p : \lambda \mapsto \lambda
\circ p$ and ${}^{t} j : \lambda \mapsto \lambda \circ j$ are defined in $L^{\bullet}(A, B; \mathcal{S})$ and
$C^{\bullet}(A, B; \mathcal{S})$ respectively, the first being none other than the canonical injection. Since ${}^{t} j
\circ {}^{t} p$ is the identity, it suffices to show that ${}^{t} p \circ {}^{t} j$ is homotopic to the identity; now,
by `(11.8.3)`, ${}^{t} h : \lambda \mapsto \lambda \circ h$ is defined in $C^{\bullet}(A, B; \mathcal{S})$ and one can
therefore transpose the identity `(11.8.3.1)`, which yields the desired result.

<!-- original page 389 -->

**11.8.6.**

<!-- label: 0_III.11.8.6 -->

Proposition `(11.8.5)` reduces the computation of the cohomology of $L^{\bullet}(A, B; \mathcal{S})$ to that of the
cohomology of $C^{\bullet}(A, B; \mathcal{S})$. Recall on the other hand that this last is, by the Eilenberg–Zilber
theorem `(G, I, 3.10.2)`, canonically isomorphic to the cohomology of the cochain complex defined as follows: one forms
the chain complex $P_{\bullet}(A, B)$, consisting of the linear combinations of the $(\sigma, \tau) \in \Sigma(A) \times
\Sigma(B)$ such that $\sigma$ and $\tau$ have *the same degree*; the differential of this complex is given by $d :
(\sigma, \tau) \mapsto \sum_{j, k} (-1)^{j+k} (\sigma_{j}, \tau_{k})$ if $d\sigma = \sum_{j} (-1)^{j} \sigma_{j}$ and
$d\tau = \sum_{k} (-1)^{k} \tau_{k}$; one then has two canonical homomorphisms of complexes

```text
  f : P_•(A, B) → C_•(A) ⊗ C_•(B),    g : C_•(A) ⊗ C_•(B) → P_•(A, B),
```

and one shows `(loc. cit.)` that there are homotopies $h$, $h'$ such that

```text
  f ∘ g − 1 = d ∘ h + h ∘ d    and    g ∘ f − 1 = d ∘ h' + h' ∘ d.
```

Moreover, one has $f(\sigma, \tau) \in C_{\bullet}(|\sigma|) \otimes C_{\bullet}(|\tau|)$ and $g(\sigma, \tau) \in
P_{\bullet}(|\sigma|, |\tau|)$ and the homotopies $h$, $h'$ may be taken such that $h(\sigma, \tau) \in
C_{\bullet}(|\sigma|) \otimes C_{\bullet}(|\tau|)$ and $h'(\sigma, \tau) \in P_{\bullet}(|\sigma|, |\tau|)$. This point
arises from the fact that the definition of $h(\sigma, \tau)$ and $h'(\sigma, \tau)$ can be made by induction on the sum
of the degrees of $\sigma$ and $\tau$, and from the fact that the $H^{q}(C_{\bullet}(|\sigma|) \otimes
C_{\bullet}(|\tau|))$ and $H^{q}(P_{\bullet}(|\sigma|, |\tau|))$ are zero for $q > 0$ `(loc. cit.)`; one reasons then as
in `(11.8.3)` and the conclusion follows.

One then defines $P^{\bullet}(A, B; \mathcal{S})$ as the set of families $\lambda = (\lambda(\sigma, \tau))$ where
$(\sigma, \tau)$ runs over the pairs whose terms have the same degree, with $\lambda(\sigma, \tau) \in
\Gamma_{\sigma,\tau}$, and since one has $d\sigma = \sum_{j} (-1)^{j} \sigma_{j} \in C_{\bullet}(|\sigma|)$ and $d\tau =
\sum_{k} (-1)^{k} \tau_{k} \in C_{\bullet}(|\tau|)$,

```text
  dλ(σ, τ) = ∑_{j, k} (−1)^{j+k} λ_{j,k}(σ_j, τ_k)
```

is defined and gives the differential of the complex $P^{\bullet}(A, B; \mathcal{S})$. With this, the maps ${}^{t} f :
\lambda \mapsto \lambda \circ f$, ${}^{t} g : \lambda \mapsto \lambda \circ g$, ${}^{t} h : \lambda \mapsto \lambda
\circ h$ and ${}^{t} h' : \lambda \mapsto \lambda \circ h'$ are all defined by virtue of the preceding remarks; ${}^{t}
f \circ {}^{t} g$ and ${}^{t} g \circ {}^{t} f$ are therefore homotopic to the identity, whence the desired isomorphism
between the cohomology of $C^{\bullet}(A, B; \mathcal{S})$ and that of $P^{\bullet}(A, B; \mathcal{S})$.

**Remark (11.8.7).**

<!-- label: 0_III.11.8.7 -->

The same reasoning as in `(11.8.3)`, but applied to $C_{\bullet}(A)$ and $L_{\bullet}(A)$, shows that if $j$ and $p$ are
defined as in `(11.8.1)`, $f = j \circ p$ verifies once more a relation `(11.8.3.1)`, with $|h(\sigma)| \subset
|\sigma|$, whence one deduces as in `(11.8.5)` an isomorphism of the cohomology of $L^{\bullet}(A; \mathcal{S})$ onto
that of $C^{\bullet}(A; \mathcal{S})$, these two complexes being defined obviously. This is the result whose proof is
sketched in `(G, I, 3.8.1)`.

**11.8.8.**

<!-- label: 0_III.11.8.8 -->

Take up now the notation and hypotheses of `(11.8.2)`, and consider a *complex* $\mathcal{S}^{\bullet} =
(\mathcal{S}^{k})$ of systems of coefficients on $\Sigma(A) \times \Sigma(B)$: for each $(\sigma, \tau)$, the
$\Gamma^{k}_{\sigma,\tau}$ therefore form a complex of abelian groups $(k \in \mathbb{Z})$, and one has the commutative
diagrams

$$ \Gamma^{k}_{\sigma,\tau} \to \Gamma^{k+1}_{\sigma,\tau} \downarrow \downarrow \Gamma^{k}_{\sigma',\tau'} \to
\Gamma^{k+1}_{\sigma',\tau'} $$

<!-- original page 390 -->

for $(\sigma, \tau) \leq (\sigma', \tau')$. Then one verifies at once that $C^{\bullet}(A, B; \mathcal{S}^{\bullet}) =
(C^{h}(A, B; \mathcal{S}^{k}))_{(h, k) \in \mathbb{Z} \times \mathbb{Z}}$ is a *bicomplex* of abelian groups, and
$L^{\bullet}(A, B; \mathcal{S}^{\bullet}) = (L^{h}(A, B; \mathcal{S}^{k}))$ is a sub-bicomplex of it.

**Proposition (11.8.9).**

<!-- label: 0_III.11.8.9 -->

The canonical injection $L^{\bullet}(A, B; \mathcal{S}^{\bullet}) \to C^{\bullet}(A, B; \mathcal{S}^{\bullet})$ defines
an isomorphism for the cohomology of these two bicomplexes.

**Proof.** Set $C^{\bullet,\bullet} = C^{\bullet}(A, B; \mathcal{S}^{\bullet})$ and $L^{\bullet,\bullet} =
L^{\bullet}(A, B; \mathcal{S}^{\bullet})$ for simplicity, and note that since $C^{hk} = L^{hk} = 0$ for $h < 0$, the
second spectral sequences of these bicomplexes are regular `(11.3.3)`; the homomorphism $L^{\bullet,\bullet} \to
C^{\bullet,\bullet}$ therefore gives a morphism of spectral sequences $''E(L^{\bullet,\bullet}) \to
''E(C^{\bullet,\bullet})$ which, for the terms `E_2`, reduces to

$$ H^{p}_{II}(H^{q}_{I}(L^{\bullet,\bullet})) \to H^{p}_{II}(H^{q}_{I}(C^{\bullet,\bullet})). (11.8.9.1) $$

But for every $k \in \mathbb{Z}$, it follows from `(11.8.3)` that the homomorphism $H^{q}_{I}(L^{\bullet,k}) \to
H^{q}_{I}(C^{\bullet,k})$ is bijective; the conclusion therefore follows from `(11.1.5)`.

**11.8.10.**

<!-- label: 0_III.11.8.10 -->

Likewise, with the notation of `(11.8.6)`, one has canonical homomorphisms of bicomplexes $C^{\bullet}(A, B;
\mathcal{S}^{\bullet}) \to P^{\bullet}(A, B; \mathcal{S}^{\bullet})$ (with obvious notation), and the same reasoning as
in `(11.8.9)`, based this time on `(11.8.6)`, shows that this homomorphism again gives an isomorphism in cohomology.

### 11.9. A lemma on complexes of finite type

**Proposition (11.9.1).**

<!-- label: 0_III.11.9.1 -->

Let $\mathcal{C}$ be an abelian category, $\mathcal{K}'$ and $\mathcal{K}''$ parts of the set of objects of
$\mathcal{C}$, such that $\mathcal{K}'' \subset \mathcal{K}'$, and verifying the following conditions:

(i) For every object $A' \in \mathcal{K}'$ and every epimorphism $u : A \to A'$ in $\mathcal{C}$, there exists an object
$B \in \mathcal{K}''$ and a morphism $v : B \to A$ such that `uv` is an epimorphism.

(ii) For every pair of objects $A \in \mathcal{K}''$, $B \in \mathcal{K}'$ and every epimorphism $u : A \to B$, $Ker(u)$
belongs to $\mathcal{K}'$.

(iii) The product of two objects of $\mathcal{K}''$ belongs to $\mathcal{K}''$.

Let $P_{\bullet} = (P_{i})_{i \in \mathbb{Z}}$ be a complex in $\mathcal{C}$, such that $H_{i}(P_{\bullet}) \in
\mathcal{K}'$ for every $i$, and such that there exists $d$ with $H_{i}(P_{\bullet}) = 0$ for $i < d$. Then there exists
a complex $Q_{\bullet} = (Q_{i})_{i \in \mathbb{Z}}$ in $\mathcal{C}$ such that $Q_{i} \in \mathcal{K}''$ for every $i$
and $Q_{i} = 0$ for $i < d$, and a morphism $u : Q_{\bullet} \to P_{\bullet}$ of complexes such that the corresponding
morphism $H_{\bullet}(Q_{\bullet}) \to H_{\bullet}(P_{\bullet})$ is an isomorphism.

**Proof.** Let us first prove the following consequence of property (i):

(i bis) *Let $u : C \to B$ be an epimorphism in $\mathcal{C}$, $A$ an object of $\mathcal{K}'$, $v : A \to B$ a morphism
in $\mathcal{C}$; then there exists an object $D \in \mathcal{K}''$, an epimorphism $u' : D \to A$ and a morphism $v' :
D \to C$ such that the diagram*

```text
                u'
            D    →    A
            ↓         ↓                                                        (11.9.1.1)
           v'         v
            ↓         ↓
            C    →    B
                u
```

*is commutative.*

Indeed, consider the fibre product $C \times_{B} A$ in $\mathcal{C}$ and the canonical projections $p : C \times_{B} A
\to C$, $q : C \times_{B} A \to A$, making the diagram

<!-- original page 391 -->

```text
                          q
            C ×_B A    →    A
                ↓             ↓                                                (11.9.1.2)
                p             v
                ↓             ↓
                C    →     B
                       u
```

commutative.

It is known `([27], p. I-12)` that the cokernel of $q$ is the quotient of $A$ by $v^{-1}(u(C))$; since $u$ is an
epimorphism, $u(C) = B$ and $v^{-1}(u(C)) = A$, hence $q$ is an epimorphism; it then suffices to apply (i) to the
epimorphism $q : C \times_{B} A \to A$: there is an object $D \in \mathcal{K}''$ and a morphism $w : D \to C \times_{B}
A$ such that `qw` is an epimorphism; one takes $u' = qw$, $v' = pw$.

That being said, to prove the proposition, we proceed by induction. Suppose, for some $i \geq d - 1$, we have
constructed, for $j \leq i$, the objects $Q_{j}$, the morphisms $d_{j} : Q_{j} \to Q_{j-1}$ and the morphisms $u_{j} :
Q_{j} \to P_{j}$ so that $Q_{j} = 0$ for $j < d$, that $d_{j-1} \circ d_{j} = 0$ and $d_{j} \circ u_{j} = u_{j-1} \circ
d_{j}$ for $j \leq i$; in addition, we suppose verified the following conditions:

(I_i) One has $Q_{j} \in \mathcal{K}''$ for $j \leq i$ and $B_{j}(Q_{\bullet}) \in \mathcal{K}'$ for $j < i$.

(II_i) For $j < i$, the homomorphism $H_{j}(Q_{\bullet}) \to H_{j}(P_{\bullet})$ deduced from the family $(u_{k})_{k
\leq i}$ is an isomorphism.

(III_i) The composite morphism $v_{i} : Z_{i}(Q_{\bullet}) \to Z_{i}(P_{\bullet}) \to H_{i}(P_{\bullet})$ (where the
left arrow is the restriction of $u_{i}$ and the right arrow is the canonical morphism) is an epimorphism.

Note that, by (ii), $Z_{i}(Q_{\bullet})$, the kernel of the epimorphism $Q_{i} \to B_{i-1}(Q_{\bullet})$, belongs to
$\mathcal{K}'$ by virtue of hypothesis (I_i). One again deduces from (ii) that $N_{i} = Ker(v_{i})$ also belongs to
$\mathcal{K}'$, taking into account hypothesis (III_i). By virtue of (i bis), there exists a $Q'_{i+1} \in
\mathcal{K}''$, an epimorphism $d'_{i+1} : Q'_{i+1} \to N_{i}$ and a morphism $u'_{i+1} : Q'_{i+1} \to P_{i+1}$, such
that the diagram

$$ d'_{i+1} Q'_{i+1} \to N_{i} \downarrow \downarrow (11.9.1.3) u'_{i+1} v_{i} \downarrow \downarrow P_{i+1} \to
B_{i}(P_{\bullet}) d_{i+1} $$

is commutative.

Since the canonical morphism $Z_{i+1}(P_{\bullet}) \to H_{i+1}(P_{\bullet})$ is an epimorphism and $H_{i+1}(P_{\bullet})
\in \mathcal{K}'$ by hypothesis, it follows from (i) that there exists an object $Q''_{i+1} \in \mathcal{K}''$ and a
morphism $u''_{i+1} : Q''_{i+1} \to Z_{i+1}(P_{\bullet})$ such that the composite $Q''_{i+1} \to Z_{i+1}(P_{\bullet})
\to H_{i+1}(P_{\bullet})$ is an epimorphism. If one takes $d''_{i+1} : Q''_{i+1} \to N_{i}$ equal to `0`, the diagram

$$ d''_{i+1} Q''_{i+1} \to N_{i} \downarrow \downarrow (11.9.1.4) u''_{i+1} v_{i} \downarrow \downarrow
Z_{i+1}(P_{\bullet}) \to P_{i} d_{i+1} $$

<!-- original page 392 -->

is commutative, the horizontal arrow at the bottom being `0`. Then take $Q_{i+1} = Q'_{i+1} \times Q''_{i+1}$, which
belongs to $\mathcal{K}''$ by virtue of (iii), and $d_{i+1} = d'_{i+1} + d''_{i+1}$, $u_{i+1} = u'_{i+1} + u''_{i+1}$.
Since $d_{i+1}(Q_{i+1}) = d'_{i+1}(Q'_{i+1}) = N_{i} \subset Z_{i}(Q_{\bullet})$, one has $d_{i} \circ d_{i+1} = 0$ and,
with the usual notation, $B_{i}(Q_{\bullet}) = N_{i}$, which verifies (I\_{i+1}). The commutativity of the diagrams
`(11.9.1.3)` and `(11.9.1.4)` shows that $d_{i+1} \circ u_{i+1} = u_{i} \circ d_{i+1}$. By definition of $N_{i}$, the
morphism $H_{i}(Q_{\bullet}) = Z_{i}(Q_{\bullet})/N_{i} \to H_{i}(P_{\bullet})$ deduced from the system of the $u_{k}$
($k \leq i + 1$) is the morphism deduced from $v_{i}$ by passage to quotients, hence it is an isomorphism since $v_{i}$
is an epimorphism, whence (II\_{i+1}). Finally, one has $Q''_{i+1} \subset Z_{i+1}(Q_{\bullet})$ by definition; the
choice of $u''_{i+1}$ shows that the morphism $v_{i+1} : Z_{i+1}(Q_{\bullet}) \to Z_{i+1}(P_{\bullet}) \to
H_{i+1}(P_{\bullet})$ is an epimorphism, its restriction to $Q''_{i+1}$ already being so, whence (III\_{i+1}). The
induction can therefore continue, and the proposition is proved.

**Corollary (11.9.2).**

<!-- label: 0_III.11.9.2 -->

Let $A$ be a Noetherian ring (not necessarily commutative), $P_{\bullet} = (P_{i})_{i \in \mathbb{Z}}$ a complex of
right $A$-modules. Suppose that the $H_{i}(P_{\bullet})$ are $A$-modules of finite type and that there exists $d$ such
that $H_{i}(P_{\bullet}) = 0$ for $i < d$. Then there exists a complex $Q_{\bullet} = (Q_{i})_{i \in \mathbb{Z}}$ formed
of right $A$-modules free of finite rank, such that $Q_{i} = 0$ for $i < d$, and a homomorphism $u : Q_{\bullet} \to
P_{\bullet}$ of complexes, such that the homomorphism $H_{\bullet}(Q_{\bullet}) \to H_{\bullet}(P_{\bullet})$
corresponding to $u$ is bijective.

**Proof.** One applies `(11.9.1)` taking for $\mathcal{C}$ the category of right $A$-modules, for $\mathcal{K}'$ (resp.
$\mathcal{K}''$) the set of $A$-modules of finite type (resp. the set of $A$-modules free of finite rank); verification
of conditions (i), (ii) and (iii) of `(11.9.1)` is immediate, taking into account the hypothesis that $A$ is Noetherian.

**Remarks (11.9.3).**

<!-- label: 0_III.11.9.3 -->

(i) Under the conditions of `(11.9.2)`, suppose moreover that the $P_{i}$ are *flat* right $A$-modules. Then, for every
left $A$-module $M$, the homomorphism of complexes $u \otimes 1 : Q_{\bullet} \otimes_{A} M \to P_{\bullet} \otimes_{A}
M$ still defines an isomorphism $H_{\bullet}(Q_{\bullet} \otimes_{A} M) \xrightarrow{\sim} H_{\bullet}(P_{\bullet}
\otimes_{A} M)$ of the homology, as we shall see in chap. III.

(ii) The conclusion of `(11.9.2)` is no longer necessarily exact when one does not suppose $A$ Noetherian; indeed,
applying it to a complex reduced to `0` except for a single term, one would conclude that every left $A$-module of
finite type admits a resolution by free modules of finite type, which is not true in general (cf. Bourbaki, _Alg.
comm._, chap. I, § 2, exerc. 6).

However, instead of supposing $A$ Noetherian, one may suppose only that the $H_{i}(P_{\bullet})$ have an
$\infty$-presentation finite (cf. chap. IV).

### 11.10. Euler–Poincaré characteristic of a complex of modules of finite length

**11.10.1.**

<!-- label: 0_III.11.10.1 -->

Let $A$ be a ring (not necessarily commutative),

```text
  M^• : 0 → M^0 → M^1 → … → M^n → 0                                            (11.10.1.1)
```

a complex of left $A$-modules of finite length. One calls *Euler–Poincaré characteristic* of this complex the number

<!-- original page 393 -->

```text
  χ(M^•) = ∑_{i=0}^n (−1)^i long(M^i).                                          (11.10.1.2)
```

**Proposition (11.10.2).**

<!-- label: 0_III.11.10.2 -->

For every finite complex $M^{\bullet}$ of left $A$-modules of finite length, one has $\chi(M^{\bullet}) =
\chi(H^{\bullet}(M^{\bullet}))$ ($H^{\bullet}(M^{\bullet})$ being considered as a complex for the trivial derivation).
In particular, if the sequence `(11.10.1.1)` is exact, one has $\chi(M^{\bullet}) = 0$.

**Proof.** Set, to abbreviate, $B^{i} = B^{i}(M^{\bullet})$, $Z^{i} = Z^{i}(M^{\bullet})$, $H^{i} = H^{i}(M^{\bullet}) =
Z^{i}/B^{i}$; the $B^{i}$, $Z^{i}$, $H^{i}$ are of finite length. From the exact sequences

$$ 0 \to B^{i} \to Z^{i} \to H^{i} \to 0 0 \to Z^{i} \to M^{i} \to B^{i+1} \to 0 $$

one derives the relations

```text
  long(Z^i) = long(H^i) + long(B^i)
  long(M^i) = long(Z^i) + long(B^{i+1})
```

whence

```text
  long(M^i) − long(H^i) = long(B^{i+1}) + long(B^i)
```

Multiply this relation by $(-1)^{i}$ and sum the relations obtained for $0 \leq i \leq n$, noting that $B^{0} = B^{n+1}
= 0$; the desired equality follows.

**Corollary (11.10.3).**

<!-- label: 0_III.11.10.3 -->

Let $E = (E^{p,q}_{r})$ be a spectral sequence in the category of modules over a ring $A$. Suppose that the
$E^{p,q}_{2}$ are $A$-modules of finite length and that there are only finitely many pairs $(p, q)$ such that
$E^{p,q}_{2} \neq 0$. Then the Euler–Poincaré characteristics $\chi(E^{(n)}_{r})$ of all the complexes $E^{(n)}_{r} =
(E^{p,q}_{r})_{p+q=n}$ `(11.1.1)` are all equal. If, in addition, the sequence $E$ is weakly convergent and one sets
$E^{(n)}_{\infty} = \oplus_{p+q=n} E^{p,q}_{\infty}$ for every $n \in \mathbb{Z}$, one also has
$\chi(E^{(\bullet)}_{\infty}) = \chi(E^{(\bullet)}_{2})$, $E^{(\bullet)}_{\infty} = (E^{(n)}_{\infty})_{n \in
\mathbb{Z}}$ being considered as a complex with trivial derivation.

**Proof.** Note first that if $E^{p,q}_{2} = 0$, one has $E^{p,q}_{r} = 0$ for $2 \leq r \leq +\infty$, so all the
complexes $E^{(\bullet)}_{r}$ are finite and formed of $A$-modules of finite length; the relation
$\chi(E^{(\bullet)}_{r}) = \chi(E^{(\bullet)}_{r+1})$ for every finite $r$ therefore follows from `(11.10.2)` and the
isomorphism between $H^{\bullet}(E^{(\bullet)}_{r})$ and $E^{(\bullet)}_{r+1}$ (as complexes with trivial derivation).
The hypothesis that the $E^{p,q}_{2}$ are of finite length entails that for every pair $(p, q)$, the sequences
$(B_{k}(E^{p,q}_{2}))_{k \geq 2}$ and $(Z_{k}(E^{p,q}_{2}))_{k \geq 2}$ are stationary; the hypothesis that $E$ is
weakly convergent and that $E^{p,q}_{2} = 0$ except for finitely many pairs $(p, q)$ entails therefore that there exists
an integer $r \geq 2$ such that $E^{p,q}_{\infty} = E^{p,q}_{r}$ for every pair $(p, q)$; whence the assertion
concerning $\chi(E^{(\bullet)}_{\infty})$.
