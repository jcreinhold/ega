<!-- original page 213 -->

## §23. Japanese rings

The results of this section will be completed in `(IV, 7.6)` and `(7.7)`.

### 23.1. Japanese rings

**Definition (23.1.1).**

<!-- label: 0_IV.23.1.1 -->

*We say that an integral ring $A$ is a **Japanese ring** if, for every finite extension $K'$ of its field of fractions
$K$, the integral closure $A'$ of $A$ in $K'$ is an $A$-module of finite type (in other words, a finite $A$-algebra). We
say that a ring $A$ is **universally Japanese** if every integral $A$-algebra of finite type is a Japanese ring.*

> _Translator's note._ "Japanese ring" is EGA's vocabulary, following Akizuki's circle and Nagata's early papers. The
> modern literature usually calls these "Nagata rings" or, with a slightly different condition, "pseudo-geometric rings"
> (Matsumura). We preserve EGA's term throughout.

<!-- original page 214 -->

It is clear that if $A$ is a Japanese ring, then every ring of fractions $S^{-1}A$ is also a Japanese ring, since (with
the preceding notation) $S^{-1}A'$ is the integral closure of $S^{-1}A$ in $K'$, and is evidently an $S^{-1}A$-module of
finite type.

An integral Noetherian ring, even a discrete valuation ring, is not necessarily a Japanese ring `[30]`.

**Proposition (23.1.2).**

<!-- label: 0_IV.23.1.2 -->

*Let $A$ be an integral Noetherian ring, $K$ its field of fractions. If, for every finite radicial extension $K'$ of
$K$, the integral closure of $A$ in $K'$ is an $A$-module of finite type, then $A$ is a Japanese ring.*

Since $A$ is Noetherian, in order to verify that $A$ is a Japanese ring, it suffices to see that for every finite
quasi-Galois extension $L$ of $K$, the integral closure $B$ of $A$ in $L$ is an $A$-module of finite type. Now $L$ is a
Galois extension of the greatest radicial extension $K'$ of $K$ contained in $L$; and if $A'$ is the integral closure of
$A$ in $K'$, then $B$ is the integral closure of $A'$ in $L$. But we know that in a separable extension of $K'$, the
integral closure of $A'$ is an $A'$-module of finite type (Bourbaki, _Alg. comm._, chap. V, §1, n° 6, cor. 1 of prop.
20), whence the proposition.

It follows from `(23.1.2)` that when $K$ is of characteristic `0`, to say that $A$ is a Japanese ring means that its
integral closure $A'$ is an $A$-module of finite type.

**Theorem (23.1.3) (Tate).**

<!-- label: 0_IV.23.1.3 -->

*Let $A$ be an integral Noetherian ring, $x \neq 0$ an element of $A$. Suppose the following conditions are satisfied:*

*(i) $A$ is integrally closed.*

*(ii) $\mathfrak{p} = xA$ is prime and $A$ is separated and complete for the $\mathfrak{p}$-preadic topology.*

*(iii) $A/xA$ is a Japanese ring.*

*Then $A$ is a Japanese ring.*

We shall use the following lemma:

**Lemma (23.1.3.1).**

<!-- label: 0_IV.23.1.3.1 -->

*Let $A$ be a ring, $x$ an element of $A$ not a zero-divisor in $A$ and such that $xA = \mathfrak{p}$ is prime; then,
for every integer $n > 0$, the inverse image of $x^{n}A_{\mathfrak{p}}$ in $A$ is $x^{n}A$.*

Indeed, suppose that $b \in A$ is an element such that $b/1 = x^{n}a/s$ in $A_{\mathfrak{p}}$, where $a \in A$ and $s
\notin \mathfrak{p}$; there exists therefore $s' \notin \mathfrak{p}$ such that $s'sb = x^{n}as$, whence $s'sb \in
\mathfrak{p}$, and since $s's \notin \mathfrak{p}$, this entails $b \in \mathfrak{p}$, in other words $b = xb'$ with $b'
\in A$; since $x$ is not a zero-divisor, we conclude $s'sb' = x^{n-1}as$ and it suffices to reason by induction on $n$.

To prove the theorem, we may restrict to the case where the field of fractions $K$ of $A$ is of characteristic $p > 0$,
since $A$ is integrally closed. Let $K'$ be a finite radicial extension of $K$, so that there exists a power $q = p^{e}$
such that $K'^{q} \subset K$; by replacing $K'$ by a larger radicial extension, we may even suppose that there exists $y
\in K'$ such that $y^{q} = x$. Let $A'$ be the integral closure of $A$ in $K'$; since $A$ is integrally closed, $A'$ is
the set of $x' \in K'$ such that $x'^{q} \in A' \cap K = A$. Set $V = A_{\mathfrak{p}}$; the maximal ideal $\mathfrak{m}
= xV$ of $V$ being principal, we know that the Noetherian local ring $V$ is a discrete valuation ring `(17.1.4)`; since
$V$ is integrally closed, the same

<!-- original page 215 -->

reasoning as above shows that the integral closure $V'$ of $V$ in $K'$ is the set of $x' \in K'$ such that $x'^{q} \in
V$; we know (Bourbaki, _Alg. comm._, chap. VI, §8, n° 6, prop. 6, and chap. V, §2, n° 3, lemma 4) that $V'$ is a
discrete valuation ring, whose maximal ideal $\mathfrak{m}'$ is the set of $x' \in K'$ such that $x'^{q} \in
\mathfrak{m}$, and moreover the residue field $V'/\mathfrak{m}'$ is a finite extension of $V/\mathfrak{m}$ (_loc. cit._,
chap. VI, §8, n° 1, lemma 2). Let us show that, for every integer $n > 0$, we have

$$ \mathfrak{m}'^{n} \cap A' = y^{n}A'. (23.1.3.2) $$

Indeed, since $y^{q} = x$, we have $y^{q} \in \mathfrak{m}'$, hence $y^{n}A' \subset \mathfrak{m}'^{n} \cap A'$.
Conversely, let $x' \in \mathfrak{m}'^{n} \cap A'$, and set $x' = z'y^{n}$ with $z' \in K'$. We have $x'^{q} \in A'$; on
the other hand, $x'^{q}$ is a sum of products $t'_{1} \cdots t'_{n}$ with $t'_{i} \in \mathfrak{m}'$, hence $t'^{q}_{i}
\in \mathfrak{m}$, and we conclude that $x'^{q} \in \mathfrak{m}^{n} \cap A$. Now lemma `(23.1.3.1)` proves that
$\mathfrak{m}^{n} \cap A = x^{n}A$, hence we have $z'^{q} x^{n} \in x^{n}A$, or again $z'^{q} \in A$ since $x \neq 0$,
which establishes `(23.1.3.2)`.

Let us show in the second place that on $A'$ the `xA'`-preadic topology is separated; this topology is also the
`yA'`-preadic topology of $A'$, and it follows from `(23.1.3.2)` that this topology is induced by the
$\mathfrak{m}'$-preadic topology of $V'$, which is separated since $V'$ is a discrete valuation ring.

Let us next prove that $A'/xA'$ is an $A$-module of finite type. Since $x = y^{q}$ and $y^{k} A' / y^{k+1} A'$ is
isomorphic to $A'/yA'$, we may restrict to showing that $A'/yA'$ is an $A$-module of finite type; but formula
`(23.1.3.2)` applied for $n = 1$ shows that $A'/yA'$ is a subring of $V'/\mathfrak{m}'$, that is to say of the residue
field of $V'$, which is a finite extension of the residue field $V/\mathfrak{m}$ of $V$. Now $V/\mathfrak{m}$ is the
field of fractions of $A/\mathfrak{p}$, and since $A'$ is integral over $A$, $A'/yA'$ is integral over $A/\mathfrak{p}$,
hence contained in the integral closure of $A/\mathfrak{p}$ in $V'/\mathfrak{m}'$; since by hypothesis $A/\mathfrak{p}$
is a Noetherian Japanese ring, $A'/yA'$ is an $(A/\mathfrak{p})$-module of finite type, and _a fortiori_ an $A$-module
of finite type.

This being so, the `xA'`-preadic topology of $A'$ being separated, $A'$ is a subring of its completion `Â'` for this
topology; but since $A'/xA'$ is an $A$-module of finite type and $A$ is separated and complete for the `xA`-preadic
topology, `Â'` is an $A$-module of finite type by virtue of $(0_{I}, 7.2.9)$, hence so is $A'$. `Q.E.D.`

**Corollary (23.1.4).**

<!-- label: 0_IV.23.1.4 -->

*Let $A$ be a Noetherian integrally closed Japanese ring. Then every ring of formal power series $A[[T_{1}, \cdots,
T_{r}]]$ is a Japanese ring.*

We know that for every Noetherian integrally closed ring $B$, the ring of formal power series `B[[T]]` is Noetherian and
integrally closed (Bourbaki, _Alg. comm._, chap. V, §1, n° 4, prop. 14); we may therefore, by induction on $n$, restrict
to proving that `A[[T]]` is a Japanese ring. Now the element $x = T$ verifies all the conditions of `(23.1.3)`, whence
the conclusion.

**Theorem (23.1.5) (Nagata).**

<!-- label: 0_IV.23.1.5 -->

*Every complete integral Noetherian local ring $A$ is a Japanese ring.*

We know `(19.8.8, (ii))` that there exists a subring $B$ of $A$ which is a complete regular local ring, such that $A$ is
a finite $B$-algebra; it evidently suffices to prove

<!-- original page 216 -->

that $B$ is a Japanese ring, in other words, we may restrict to the case where $A$ is moreover regular. Let us reason by
induction on $n = \dim(A)$, the theorem being evident for $n = 0$. So suppose $n > 0$, and, denoting by $\mathfrak{m}$
the maximal ideal of $A$, let $x$ be an element of $\mathfrak{m} - \mathfrak{m}^{2}$; we know `(17.1.8)` that $A/xA$ is
a regular ring, and moreover (`(17.1.7)` and `(16.3.4)`) that $\dim(A/xA) = n - 1$; furthermore, the ideal `xA` is
closed in $A$ $(0_{I}, 7.3.5)$, hence $A/xA$ is complete. By virtue of the induction hypothesis, $A/xA$ is therefore a
Japanese ring, and it then follows from `(23.1.3)` that so is $A$.

**Corollary (23.1.6).**

<!-- label: 0_IV.23.1.6 -->

*Let $A$ be a complete integral Noetherian local ring, $K$ its field of fractions, $K'$ a finite extension of $K$; then
the integral closure $A'$ of $A$ in $K'$ is a complete local ring.*

We already know by `(23.1.5)` that $A'$ is a finite $A$-algebra, hence a complete Noetherian semi-local ring, and
consequently a direct composite of local rings; but since $A'$ is integral, it is necessarily a local ring.

**Proposition (23.1.7).**

<!-- label: 0_IV.23.1.7 -->

*Let $A$ be an integral Noetherian local ring, $K$ its field of fractions, $K'$ a finite extension of $K$, $A'$ the
integral closure of $A$ in $K'$. Suppose that the completion `Â` is reduced, and denote by $R$ its total ring of
fractions.*

*(i) If the ring $R \otimes_{K} K'$ is reduced (which will happen in particular when $K'$ is a separable extension of
$K$, $R$ being a direct composite of fields, extensions of $K$ (Bourbaki, _Alg._, chap. VIII, §7, n° 3, cor. 1 of th.
1)), then $A'$ is an $A$-module of finite type.*

*(ii) If in particular $R$ is a separable $K$-algebra, then $A$ is a Japanese ring.*

(i) Set for simplicity $A_{1} = \hat{A}$, $A'_{1} = A' \otimes_{A} A_{1}$, $K'_{1} = K' \otimes_{A} A_{1}$. Since `A_1`
is a flat $A$-module $(0_{I}, 7.3.5)$, $A'_{1}$ identifies with a subring of $K'_{1}$ and is evidently integral over
`A_1`. On the other hand, if we set $K_{1} = K \otimes_{A} A_{1}$, we may write $K'_{1} = K' \otimes_{K} K_{1}$; since
$A$ is integral and `A_1` is a flat $A$-module, every element $\neq 0$ of $A$ is `A_1`-regular $(0_{I}, 6.3.4)$; since
$K = S^{-1}A$, where $S = A - {0}$, we have $K_{1} = S^{-1}A_{1}$, and the preceding remark proves that `K_1` identifies
with a subring of the total ring of fractions $R$ of `A_1`. Since every $K$-module is flat, $K'_{1}$ identifies with a
subring of $K' \otimes_{K} R$, which by hypothesis is reduced and is a finite $R$-algebra. Denote by $\mathfrak{q}_{i}
(1 \leq i \leq n)$ the minimal prime ideals of `A_1`, by $B_{i}$ the integral ring $A_{1}/\mathfrak{q}_{i}$, by $L_{i}$
the field of fractions of $B_{i}$, so that $R$ is a direct composite of the $L_{i}$, and $K' \otimes_{K} R$ a direct
composite of the $K' \otimes_{K} L_{i}$; these latter $K$-algebras, being reduced, are direct composites of fields,
finite extensions of the $L_{i}$. Since $B_{i}$ is a complete integral local ring, Nagata's theorem `(23.1.5)` proves
that the integral closure of $B_{i}$ in $K' \otimes_{K} L_{i}$ is a $B_{i}$-module of finite type, and _a fortiori_ an
`A_1`-module of finite type; since every element of $K' \otimes_{K} R$ which is integral over `A_1` is also integral
over $B_{i}$ (being annihilated by $\mathfrak{q}_{i}$), we finally conclude that the integral closure of `A_1` in $K'
\otimes_{K} R$ is an `A_1`-module of finite type. But since $A'_{1}$ is contained in this integral closure and `A_1` is
Noetherian, $A'_{1}$ is also an `A_1`-module of finite type. Finally, since `A_1` is a faithfully flat $A$-module
$(0_{I}, 7.3.5)$, we conclude that $A'$ is an $A$-module of finite type (Bourbaki, _Alg. comm._, chap. I, §3, n° 6,
prop. 11).

<!-- original page 217 -->

(ii) The hypothesis entails that the $L_{i}$ are separable extensions of $K$, hence $K' \otimes_{K} R$ is reduced
(Bourbaki, _Alg._, chap. VIII, §7, n° 3, th. 1), and one may apply (i) to every finite extension $K'$ of $K$, which
proves our assertion.

### 23.2. Integral closure of an integral Noetherian local ring.

**(23.2.1)**

<!-- label: 0_IV.23.2.1 -->

In what follows, for every ring $A$, we shall write $A_{red}$ for short to denote the quotient of $A$ by its nilradical
(so that if $X = \operatorname{Spec}(A)$, we have `X_red = Spec(A_red)`).

We shall say that a local ring $A$ is **unibranch** if the ring $A_{red}$ is integral and if the integral closure of
$A_{red}$ is a local ring, which generalizes the definition given in `(III, 4.3.6)`. We shall say that $A$ is
**geometrically unibranch** if it is unibranch and if the residue field of the local ring (which is the integral closure
of $A_{red}$) is a radicial extension of that of $A$. It is clear that an integrally closed local ring is geometrically
unibranch; it follows from `(23.1.6)` that a complete integral Noetherian local ring is unibranch.

**Lemma (23.2.2)** [\*].

<!-- label: 0_IV.23.2.2 -->

*Let $A$ be an integral ring, $A'$ its integral closure; for the canonical morphism $f : \operatorname{Spec}(A') \to
\operatorname{Spec}(A)$ to be radicial, it is necessary and sufficient that for every $\mathfrak{p} \in
\operatorname{Spec}(A)$, $A_{\mathfrak{p}}$ be geometrically unibranch; when this is the case, $f$ is a homeomorphism.*

Indeed, for every $\mathfrak{p} \in \operatorname{Spec}(A)$, the integral closure of $A_{\mathfrak{p}}$ is
$A'_{\mathfrak{p}}$ (Bourbaki, _Alg. comm._, chap. V, §1, n° 5, prop. 16), and all the prime ideals of
$A'_{\mathfrak{p}}$ above $\mathfrak{p}A_{\mathfrak{p}}$ are maximal (_loc. cit._, §2, n° 1, prop. 1). To say that $f$
is injective therefore means that for every $\mathfrak{p} \in \operatorname{Spec}(A)$, $A'_{\mathfrak{p}}$ is a local
ring, that is to say that the $A_{\mathfrak{p}}$ are unibranch. To say that every $A_{\mathfrak{p}}$ is geometrically
unibranch then means that $f$ is radicial by virtue of `(I, 3.5.8)`. When this is the case, $f$ is surjective and closed
`(II, 6.1.10)`, hence a homeomorphism.

[\*] _In the remainder of this number, we use notions and results expounded in chap. IV, §§2 and 5; since the results of
this number are not used before chap. IV, §6, this does not entail any vicious circle._

**Lemma (23.2.3).**

<!-- label: 0_IV.23.2.3 -->

*Let $A$ be an integral ring, $K$ its field of fractions, $B$ a Noetherian ring, $\phi : A \to B$ a ring homomorphism
making $B$ a flat $A$-module. Let $K'$ be an extension of $K$; set $B_{1} = B_{red}$, and let $R$ be the total ring of
fractions of `B_1`. Then, for every sub-$A$-algebra $A'$ of $K'$, the canonical homomorphism*

```text
  (A' ⊗_A B)_red → (K' ⊗_A R)_red                                             (23.1.8.1)
```

*is injective.*

We may consider the canonical homomorphism $h : A' \otimes_{A} B \to K' \otimes_{A} R$ as the composite of the following
homomorphisms

```text
  A' ⊗_A B  ⟶  K' ⊗_A B  ⟶  K' ⊗_A B_1  ⟶  K' ⊗_A R.
            u            v              w
```

Since $B$ is a flat $A$-module, $u$ is injective; similarly, $K'$ being a flat $K$-module and $K$ a flat $A$-module,
$K'$ is a flat $A$-module, and $w$ is therefore injective since `B_1` is reduced, hence the homomorphism $B_{1} \to R$
injective. Finally, for the same reason, if $\mathfrak{N}$ is

<!-- original page 218 -->

the nilradical of $B$, the kernel of $v$ is $K' \otimes_{A} \mathfrak{N}$, hence it is contained in the nilradical of
$K' \otimes_{A} B$; we conclude immediately that if the image under $h = w \circ v \circ u$ of an element $x \in A'
\otimes_{A} B$ is nilpotent, then $x$ is nilpotent, which proves the lemma.

**Proposition (23.2.4).**

<!-- label: 0_IV.23.2.4 -->

*Let $A$ be an integral ring, $K$ its field of fractions, $B$ a Noetherian ring, $\mathfrak{q}_{i} (1 \leq i \leq n)$
its minimal prime ideals, $\phi : A \to B$ a ring homomorphism. Suppose that the $B/\mathfrak{q}_{i}$ are Japanese
rings, and that $B$ is a flat $A$-module. Let $K'$ be a finite extension of $K$, and let $(C_{\lambda})$ be the
increasing filtering family of subrings of $K'$ which are finite $A$-algebras and admit $K'$ for field of fractions; the
union $A'$ of the $C_{\lambda}$ is therefore the integral closure of $A$ in $K'$. Then:*

*(i) There exists an index $\alpha$ such that for $\lambda \geq \alpha$, the canonical homomorphism*

```text
  (C_α ⊗_A B)_red → (C_λ ⊗_A B)_red                                           (23.2.4.1)
```

*is bijective.*

*(ii) If moreover $B$ is a faithfully flat $A$-module, the morphism $\operatorname{Spec}(A' \otimes_{A} B) \to
\operatorname{Spec}(C_{\alpha} \otimes_{A} B)$ is radicial.*

(i) Let $B_{1} = B_{red}$, and let $R$ be the total ring of fractions of `B_1`; since $A$ is integral and $B$ a flat
$A$-module, every element $\neq 0$ of $A$ is $B$-regular $(0_{I}, 6.3.4)$, hence the composite homomorphism $A \to B \to
B_{1}$ extends to a homomorphism $K \to R$; we may then write $K' \otimes_{A} R = K' \otimes_{K} K \otimes_{A} R$, and
since $K' \otimes_{K} K$ identifies with $K'$, we have $K' \otimes_{A} R = K' \otimes_{K} R$. Since $R$ is a direct
composite of the fields of fractions $L_{i}$ of the $B/\mathfrak{q}_{i}$, $K' \otimes_{K} R$ is a direct composite of
the $K' \otimes_{K} L_{i}$, and consequently $(K' \otimes_{K} R)_{red}$ is a direct composite of a finite number of
finite extensions of the $L_{i}$. By virtue of the hypothesis, the integral closure of $B/\mathfrak{q}_{i}$ in a finite
extension of $L_{i}$ is a $(B/\mathfrak{q}_{i})$-module of finite type, hence a $B$-module of finite type; we conclude
that the integral closure $B'$ of $B$ in $(K' \otimes_{A} R)_{red}$ is a $B$-module of finite type. By virtue of
`(23.2.3)`, the $(C_{\lambda} \otimes_{A} B)_{red}$ identify canonically with subrings of $(K' \otimes_{A} R)_{red}$
which are finite $B$-algebras, hence contained in $B'$. Since $B$ is Noetherian and $B'$ a $B$-module of finite type,
the filtering family of the $(C_{\lambda} \otimes_{A} B)_{red}$ admits a greatest element $(C_{\alpha} \otimes_{A}
B)_{red}$, which proves (i).

(ii) Since $B$ is a faithfully flat $A$-module, it suffices `(IV, 2.6.1, (v))` to show that the morphism
$\operatorname{Spec}(A' \otimes_{A} B) \to \operatorname{Spec}(C_{\alpha} \otimes_{A} B)$ is radicial, or, what amounts
to the same `(I, 5.1.6)`, that the morphism `Spec(A' ⊗_A B)_red → Spec(C_α ⊗_A B)_red` is radicial; but one has $A'
\otimes_{A} B = \varinjlim_{\lambda} (C_{\lambda} \otimes_{A} B)$, hence `(IV, 5.13.2)`
`(A' ⊗_A B)_red = lim⃗_λ (C_λ ⊗_A B)_red`, and the conclusion results from (i).

**Corollary (23.2.5).**

<!-- label: 0_IV.23.2.5 -->

*Let $A$ be an integral Noetherian local ring, $K$ its field of fractions, $K'$ a finite extension of $K$. Let
$(C_{\lambda})$ be the increasing filtering family of subrings of $K'$ which are finite $A$-algebras (hence Noetherian
semi-local rings (Bourbaki, _Alg. comm._, chap. IV, §2, n° 5, cor. 3 of prop. 9)) and admit $K'$ for field of fractions.
Then there exists $\alpha$ such that the homomorphism $(\hat{C}_{\alpha})_{red} \to (\hat{C}_{\lambda})_{red}$ is an
isomorphism for $\lambda \geq \alpha$, and if $A'$ is the integral closure of $A$ in $K'$, the morphism
$\operatorname{Spec}(\hat{A}') \to \operatorname{Spec}(\hat{C}_{\alpha})$ is radicial (cf. `(23.2.2)`).*

<!-- original page 219 -->

We apply `(23.2.4)` taking $B = \hat{A}$; since the $B/\mathfrak{q}_{i}$ are complete Noetherian local rings, they are
Japanese rings `(23.1.5)` and $B$ is a faithfully flat $A$-module $(0_{I}, 7.3.5)$; moreover one has $C_{\lambda}
\otimes_{A} B = \hat{C}_{\lambda}$ (Bourbaki, _Alg. comm._, chap. III, §3, n° 4, th. 3 and chap. IV, §2, n° 5, cor. 3 of
prop. 9).

**Corollary (23.2.6).**

<!-- label: 0_IV.23.2.6 -->

*Under the hypotheses of `(23.2.5)`, the integral closure $A'$ of $A$ in $K'$ is a semi-local ring; if $\mathfrak{m}$ is
the maximal ideal of $A$, then, for every maximal ideal $\mathfrak{m}'$ of $A'$, $A'/\mathfrak{m}'$ is a finite
extension of $A/\mathfrak{m}$.*

The fact that the homomorphism $(\hat{C}_{\alpha})_{red} \to (\hat{C}_{\lambda})_{red}$ is bijective for $\lambda \geq
\alpha$ entails that the number of maximal ideals of $C_{\lambda}$ is constant for $\lambda \geq \alpha$ and that if
$\mathfrak{m}_{\alpha}$ is a maximal ideal of $C_{\alpha}$ and $\mathfrak{m}_{\lambda}$ the unique maximal ideal of
$C_{\lambda}$ above $\mathfrak{m}_{\alpha}$, the fields $C_{\lambda}/\mathfrak{m}_{\lambda}$ and
$C_{\alpha}/\mathfrak{m}_{\alpha}$ are canonically isomorphic. The conclusion results from the fact that $\mathfrak{m}'
= \varinjlim \mathfrak{m}_{\lambda}$ and $A'/\mathfrak{m}' = \varinjlim (C_{\lambda}/\mathfrak{m}_{\lambda})$ $(0_{III},
10.3.1.3)$.

**Proposition (23.2.7) (Y. Mori).**

<!-- label: 0_IV.23.2.7 -->

*Let $A$ be an integral Noetherian local ring, $K$ its field of fractions, $A'$ the integral closure of $A$. Then $A'$
is a semi-local Krull ring (Bourbaki, _Alg. comm._, chap. VII, §1); in other words, there exists a family
$(V_{\lambda})$ of discrete valuation rings having $K$ for field of fractions, such that $A' = \bigcap V_{\lambda}$ and
that every $x \in K$ belongs to all the $V_{\lambda}$ save for a finite number of them. Moreover, there exists a subring
$C$ of $K$ which is a finite $A$-algebra, and such that the $V_{\lambda}$ are the integral closures of the rings
$C_{\mathfrak{p}_{\lambda}}$, where $(\mathfrak{p}_{\lambda})$ is the family of prime ideals of height `1` of the local
ring $C$.*

Let us first prove the following lemma:

**Lemma (23.2.7.1).**

<!-- label: 0_IV.23.2.7.1 -->

*Let $A$, $B$ be two rings, $\phi : A \to B$ a homomorphism making $B$ a faithfully flat $A$-module. Suppose that $A$ is
integral; then, if $C = B_{red}$, the composite homomorphism $\psi : A \to B \to B_{red} = C$ is injective and extends
to an injective homomorphism of the field of fractions $K$ of $A$ into the total ring of fractions $R$ of $C$; moreover,
if $C'$ is the integral closure of $C$ in $R$, then $C' \cap K$ is the integral closure of $A$.*

Since $A$ is integral and $\phi$ injective, the intersection of $\phi(A)$ and the nilradical $\mathfrak{N}$ of $B$ is
reduced to `0`, and since $C = B/\mathfrak{N}$, $\psi$ is injective. Every $a \neq 0$ in $A$ being a non-zero-divisor in
$A$ is no more so in $B$ by flatness $(0_{I}, 6.3.4)$; we deduce that $a$ is also not a zero-divisor in $C$, for if one
had $ax \in \mathfrak{N}$ for an $x \notin \mathfrak{N}$ in $B$, one would deduce $a^{n}x^{n} = 0$ for an integer $n$,
which contradicts the preceding since $x^{n} \neq 0$. We may therefore extend $\psi$ to an injective homomorphism of $K$
into $R$. To prove the last assertion, note that it is clear that the integral closure $A'$ of $A$ is contained in $C'
\cap K$. Conversely, let $x \in C' \cap K$; $x$ is therefore integral over $C$, and _a fortiori_ over $B$, in other
words `B[x]` is a finite $B$-algebra; moreover, $K$ identifies with a subring of $B \otimes_{A} K$, and the subring
`B[x]` of $B \otimes_{A} K$ identifies with $B \otimes_{A} A[x]$ by flatness; we conclude that `A[x]` is an $A$-module
of finite type (Bourbaki, _Alg. comm._, chap. I, §3, n° 6, prop. 11), hence that $x \in A'$.

This lemma being established, we shall apply it to the canonical injection of $A$ into its completion `Â`, which is a
faithfully flat $A$-module; $B = (\hat{A})_{red} = \hat{A}/\mathfrak{N}$ (where $\mathfrak{N}$ is the nilradical of `Â`)
is a reduced complete Noetherian local ring, whose total ring of

<!-- original page 220 -->

fractions $R$ is therefore a direct composite of a finite number of fields $L_{i}$; the canonical image $B_{i}$ of $B$
in $L_{i}$ is an integral and complete Noetherian local ring, of which $L_{i}$ is the field of fractions, and the
integral closure $B'$ of $B$ in $R$ is the direct composite of the $B'_{i}$, where $B'_{i}$ is the integral closure of
$B_{i}$. But by virtue of `(23.1.5)`, $B'_{i}$ is a finite $B_{i}$-algebra, hence an integrally closed Noetherian local
ring. We know (Bourbaki, _Alg. comm._, chap. VII, §1, n° 3, cor. of th. 2) that $B'_{i}$ is a Krull ring. Now, for every
$i$, we have a homomorphism $\phi_{i} : K \to L_{i}$, which is injective, and consequently $\phi^{-1}_{i}(B'_{i})$ is a
Krull ring in $K$. But since $A' = B' \cap K$ by virtue of the lemma and $B' = \bigcap_{i} \phi^{-1}_{i}(B'_{i})$, $A'$
is the intersection of a finite number of Krull rings and is consequently a Krull ring. To prove the last assertion of
the proposition, note that there exists a finite $A$-algebra $C \subset K$ such that the morphism
$\operatorname{Spec}(A') \to \operatorname{Spec}(C)$ is radicial and a homeomorphism `(23.2.4)`; for every prime ideal
$\mathfrak{p}' \in \operatorname{Spec}(A')$, $\mathfrak{p}'$ is therefore the only prime ideal of $A'$ above
$\mathfrak{p} = \mathfrak{p}' \cap C$ and $A'_{\mathfrak{p}'}$ the integral closure of $C_{\mathfrak{p}}$; on the other
hand, the fact that $\operatorname{Spec}(A') \to \operatorname{Spec}(C)$ is a homeomorphism entails that the map
$\mathfrak{p}' \mapsto \mathfrak{p}' \cap C$ is a bijection from the set of prime ideals of height `1` of $A'$ onto the
set of prime ideals of height `1` of $C$; whence the conclusion, taking account of Bourbaki, _Alg. comm._, chap. VII,
§1, n° 6, th. 4.

**Remarks (23.2.8).**

<!-- label: 0_IV.23.2.8 -->

*(i) One must take care to note, in the application of `(23.2.6)` and `(23.2.7)`, that the ring $A'$ is not necessarily
a Noetherian ring, as an example of Nagata with $\dim(A) = 3$ shows `[30]`.*

*(ii) The conclusions of `(23.2.7)` are still valid if $A'$ is the integral closure of $A$ in a finite extension $K'$ of
$K$; it suffices in fact to consider a finite $A$-algebra $B$ of which $K'$ is the field of fractions; $B$ is a
Noetherian semi-local ring, hence an intersection of a finite number of Noetherian local rings $B_{\mathfrak{m}_{i}}$
($\mathfrak{m}_{i}$ maximal ideals of $B$), and its integral closure (which is equal to $A'$) is the intersection of the
$A'_{\mathfrak{m}_{i}}$ (Bourbaki, _Alg. comm._, chap. II, §3, n° 3, cor. 4 of th. 1) which are the integral closures of
the $B_{\mathfrak{m}_{i}}$, hence Krull rings by `(23.2.7)`; consequently $A'$ is a Krull ring.*

*(iii) One can show (`[30]`, 3.3.10) that for every integral Noetherian ring $A$ (not necessarily local), the integral
closure of $A$ is a Krull ring.*

**Corollary (23.2.9).**

<!-- label: 0_IV.23.2.9 -->

*Let $A$ be an integral Noetherian ring, $A'$ its integral closure. Suppose that for every ring $C$ such that $A \subset
C \subset A'$ and such that $C$ is a finite $A$-algebra, and for every prime ideal $\mathfrak{q}$ of height `1` in $C$,
$\mathfrak{q} \cap A$ is a prime ideal of height `1` in $A$. Let $P$ be the set of prime ideals of height `1` in $A'$;
then one has*

```text
  A' = ⋂_{𝔭 ∈ P} A'_𝔭.
```

Since $A'$ is a torsion-free $A$-module, one has $A' = \bigcap_{\mathfrak{m}} A'_{\mathfrak{m}}$, where $\mathfrak{m}$
runs through the set of maximal ideals of $A$ (Bourbaki, _Alg. comm._, chap. II, §3, n° 3, cor. 4 of th. 1); it will
therefore suffice to prove that $A'_{\mathfrak{m}}$ is the intersection of the $A'_{\mathfrak{p}}$ for the prime ideals
$\mathfrak{p} \subset \mathfrak{m}$ of height `1`. Since $A'_{\mathfrak{m}}$ is the integral closure of
$A_{\mathfrak{m}}$, we see that we may restrict to demonstrating the corollary for $A_{\mathfrak{m}}$. Now there is
then, by virtue of `(23.2.7)`, an $A_{\mathfrak{m}}$-algebra

<!-- original page 221 -->

$B$ of finite type contained in $A'_{\mathfrak{m}}$ such that $A'_{\mathfrak{m}}$ is the intersection of the integral
closures of the rings $B_{\mathfrak{q}}$, where $\mathfrak{q}$ runs through the set of prime ideals of height `1` of
$B$. But $B$ is of the form $C_{\mathfrak{m}}$, where $C$ is a finite $A$-algebra; hence, for every prime ideal
$\mathfrak{q}$ of height `1` in $B$, $\mathfrak{q} \cap A$ is by hypothesis a prime ideal of height `1` in $A$; since
the integral closure of $B_{\mathfrak{q}}$ contains that of $A_{\mathfrak{q} \cap A}$ and the latter contains
$A'_{\mathfrak{m}}$, it indeed follows that $A'_{\mathfrak{m}}$ is the intersection of the $A'_{\mathfrak{p}}$ for
$\mathfrak{p} \in P$ and $\mathfrak{p} \subset \mathfrak{m}$, which completes the proof.

**Remarks (23.2.10).**

<!-- label: 0_IV.23.2.10 -->

*(i) We shall see (`(IV, 5.6.3)` and `(5.6.10)`) that the hypothesis of `(23.2.9)` is satisfied when $A$ is universally
catenary, in particular (`(IV, 5.10.17)` and `(5.11.2)`) when $A$ is a quotient of a regular ring; finally, it is
evidently satisfied if $\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is a homeomorphism, in particular if this
morphism is radicial `(23.2.2)`.*

*(ii) The conclusion of `(23.2.9)` is no longer necessarily exact when one omits the hypothesis on the finite
sub-$A$-algebras of $A'$. Indeed, one can define an integral Noetherian local ring $A$, of dimension `2`, whose integral
closure $A'$ is a finite $A$-algebra, but such that there is a prime ideal $\mathfrak{p}'$ of $A'$ of height `1` above
the maximal ideal $\mathfrak{m}$ (of height `2`) of $A$, and such moreover that for every prime ideal $\mathfrak{p}$ of
height `1` in $A$, $A_{\mathfrak{p}}$ is integrally closed `(IV, 5.6.11)`; the intersection of these rings
$A_{\mathfrak{p}}$ cannot then be equal to $A'$ since $A'$ is a Krull ring (Bourbaki, _Alg. comm._, chap. VII, §1, n° 5,
prop. 9).*

(_To be continued._)
