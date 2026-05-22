# Chapter I — The Language of Schemes

## §3. Product of Preschemes

<!-- label: I.3 -->

> **Translation status.** This section is a translation skeleton: subsection headings and the principal definitions and
> statements are translated; longer proofs are summarized or referenced. Proofs in full follow the structure of and the
> source PDF.

### 3.1. Sums of preschemes

<!-- label: I.3.1 -->

**(3.1.1)** Let $(X_{\lambda})_{\lambda \in L}$ be a family of preschemes. The topological sum $X = \bigsqcup_{\lambda}
X_{\lambda}$ carries a sheaf of rings $\mathcal{O}_{X}$ whose restriction to each $X_{\lambda}$ is
$\mathcal{O}_{X_{\lambda}}$. The ringed space $(X, \mathcal{O}_{X})$ is a prescheme, called the _sum_ of the
$(X_{\lambda})$. The canonical injections $X_{\lambda} \to X$ are open immersions. For an $S$-prescheme structure, the
sum is the coproduct in the category of $S$-preschemes.

### 3.2. Products of preschemes

<!-- label: I.3.2 -->

**Definition (3.2.1).** Let $X$, $Y$ be $S$-preschemes with structure morphisms $f : X \to S$ and $g : Y \to S$. A
_product of $X$ and $Y$ over $S$_ is an $S$-prescheme $Z$ together with $S$-morphisms $p : Z \to X$ and $q : Z \to Y$
(the _canonical projections_) such that, for every $S$-prescheme $T$, the map

```
Hom_S(T, Z) → Hom_S(T, X) × Hom_S(T, Y),   u ↦ (p ∘ u, q ∘ u)
```

is a _bijection_. By the universal property, when it exists, $Z$ is unique up to unique $S$-isomorphism. Write $Z = X
\times_{S} Y$.

**Proposition (3.2.2).** The product $X \times_{S} Y$ exists when $X$, $Y$, and $S$ are affine. Specifically, if $X =
\operatorname{Spec}(A)$, $Y = \operatorname{Spec}(B)$, $S = \operatorname{Spec}(C)$, then $X \times_{S} Y =
\operatorname{Spec}(A \otimes_{C} B)$, with projections corresponding to $a \mapsto a \otimes 1$ and $b \mapsto 1
\otimes b$.

**Corollary (3.2.3).** For affine $S$, $X \times_{S} Y$ exists if $X$ is affine over $S$, etc.

**Proposition (3.2.4).** Existence of products is _local_: if it holds when $X$, $Y$, $S$ are replaced by affine opens
forming covers, then it holds in general.

**Theorem (3.2.6).** For any $S$-preschemes $X$, $Y$, the product $X \times_{S} Y$ exists.

The proof glues affine local products using a cocycle argument and (3.2.4); see Lemmas (3.2.6.1)–(3.2.6.4).

**Corollary (3.2.7).** Products are functorial: for $S$-morphisms $u : X \to X'$, $v : Y \to Y'$, there is a unique
$S$-morphism $u \times v : X \times_{S} Y \to X' \times_{S} Y'$ compatible with projections.

### 3.3. Formal properties of the product; change of base prescheme

<!-- label: I.3.3 -->

**(3.3.1)** _Commutativity:_ there is a canonical isomorphism $X \times_{S} Y \cong Y \times_{S} X$.

**(3.3.2)** _Associativity:_ for three $S$-preschemes, $(X \times_{S} Y) \times_{S} Z \cong X \times_{S} (Y \times_{S}
Z) \cong X \times_{S} Y \times_{S} Z$.

**Proposition (3.3.3).** Identity: $X \times_{S} S \cong X$ canonically.

**Corollary (3.3.4).** For $S' \to S$ a morphism, the base change $X_{(S')} = X \times_{S} S'$ is an $S'$-prescheme,
with structure morphism the second projection. This $X \mapsto X_{(S')}$ is a functor
`(S\text{-preschemes}) → (S′\text{-preschemes})`.

**Proposition (3.3.9).** _Transitivity of base change:_ for $S'' \to S' \to S$, $(X \times_{S} S') \times_{S'} S'' \cong
X \times_{S} S''$.

**Corollary (3.3.10).** Base change commutes with finite products: $(X \times_{S} Y)_{(S')} = X_{(S')} \times_{S'}
Y_{(S')}$.

**Corollary (3.3.11).** Open immersions are preserved by base change: if $j : U \to X$ is an open immersion, so is $j
\times_{S} 1_{S'} : U_{(S')} \to X_{(S')}$.

### 3.4. Points of a prescheme with values in a prescheme; geometric points

<!-- label: I.3.4 -->

**Definition (3.4.1).** Let $X$ be an $S$-prescheme, $T$ an $S$-prescheme. A _$T$-valued point_ of $X$ (or _$T$-point_)
is an $S$-morphism $T \to X$; the set of such is $X(T) = \operatorname{Hom}_{S}(T, X)$.

**(3.4.2)** A _fiber product of sets_: for sets $A \to C \leftarrow B$, $A \times_{C} B = {(a, b) \in A \times B : f(a)
= g(b)}$.

**Proposition (3.4.3).** $(X \times_{S} Y)(T) = X(T) \times_{S(T)} Y(T)$ for every $S$-prescheme $T$.

**(3.4.4)** _Points with values in a ring $A$_: if $T = \operatorname{Spec}(A)$, write $X(A) = X(T)$. For $S =
\operatorname{Spec}(C)$, `X(A) = Hom_{C\text{-alg}}(\text{some algebra}, A)` when $X$ is affine.

**(3.4.5) Geometric points.** A _geometric point_ of $X$ is a morphism $\operatorname{Spec}(K) \to X$ for $K$ a field.
The _value field_ of the geometric point is $K$. A _geometric point above $s \in S$_ is a geometric point
$\operatorname{Spec}(K) \to X$ whose composition with $X \to S$ factors through $\operatorname{Spec}(K) \to
\operatorname{Spec}(\kappa(s)) \to S$. A geometric point _localized at_ $x \in X$ is one whose underlying map sends the
unique point to $x$.

**Lemma (3.4.6).** Geometric points of $X$ above $s \in S$ correspond to pairs $(x, K_{x})$ with $x \in X$ over $s$ and
$K_{x}$ an extension of $\kappa(x)$.

**Proposition (3.4.7).** For $f : X \to Y$ an $S$-morphism, every geometric point of $X$ maps via $f$ to a geometric
point of $Y$ with the same value field.

### 3.5. Surjections and injections

<!-- label: I.3.5 -->

**Proposition (3.5.2).** A morphism $f : X \to Y$ is surjective iff every geometric point of $Y$ lifts to a geometric
point of $X$.

**Proposition (3.5.3).** Surjectivity is preserved by base change: if $f : X \to Y$ is surjective and $g : Y' \to Y$ is
a morphism, then $f_{(Y')} : X \times_{Y} Y' \to Y'$ is surjective.

**Definition (3.5.4).** A morphism $f : X \to Y$ is _radicial_ (or _universally injective_) if for every base change $Y'
\to Y$, $f_{(Y')}$ is injective; equivalently, for every field $K$, $X(K) \to Y(K)$ is injective. A radicial morphism is
injective.

**Proposition (3.5.6).** $f$ is radicial iff it is injective and induces purely inseparable residue-field extensions at
every point.

**Proposition (3.5.7).** Composition and base change preserve radicial morphisms.

**Proposition (3.5.8).** _Geometric injection_: $f : X \to Y$ is radicial iff the diagonal $X \to X \times_{Y} X$ is
surjective.

### 3.6. Fibers

<!-- label: I.3.6 -->

**Proposition (3.6.1).** For an $S$-prescheme $X$ with structure morphism $f$, and a geometric point $s :
\operatorname{Spec}(K) \to S$, the _fiber_ $X_{s} = X \times_{S} \operatorname{Spec}(K)$ is a $K$-prescheme.
Set-theoretically, the underlying space of $X_{s}$ (where $K = \kappa(s)$) is $f^{-1}(s)$.

**Proposition (3.6.4).** Fibers commute with base change: $(X \times_{S} Y)_{s} = X_{s} \times_{K} Y_{s}$ ($K =
\kappa(s)$).

**Proposition (3.6.5).** Surjectivity and radiciality of a morphism are detected fiber-by-fiber.

### 3.7. Reduction mod 𝔍

<!-- label: I.3.7 -->

For an ideal $\mathfrak{J} \subset A$ and an $A$-prescheme $X$, the _reduction_ $X mod \mathfrak{J}$ is $X
\times_{\operatorname{Spec}(A)} \operatorname{Spec}(A/\mathfrak{J})$. This is a functor from $A$-preschemes to
$(A/\mathfrak{J})$-preschemes.
