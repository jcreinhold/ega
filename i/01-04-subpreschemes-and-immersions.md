# Chapter I — The Language of Schemes

## §4. Subpreschemes and Immersion Morphisms

<!-- label: I.4 -->

> **Translation status.** Translation skeleton with key definitions and theorem statements; full proofs reference .

### 4.1. Subpreschemes

<!-- label: I.4.1 -->

**Proposition (4.1.2).** Let $(X, \mathcal{O}_{X})$ be a prescheme and $\mathcal{J} \subset \mathcal{O}_{X}$ a
quasi-coherent sheaf of ideals. The support of $\mathcal{O}_{X} / \mathcal{J}$ is _closed_ in $X$; on this support, the
pair $(Supp(\mathcal{O}_{X}/\mathcal{J}), (\mathcal{O}_{X}/\mathcal{J})|Supp)$ is a prescheme.

**Definition (4.1.3).** A _closed subprescheme_ of $(X, \mathcal{O}_{X})$ is a prescheme of the form $(Y,
\mathcal{O}_{X} / \mathcal{J} | Y)$ with $\mathcal{J} \subset \mathcal{O}_{X}$ a quasi-coherent ideal sheaf and $Y =
Supp(\mathcal{O}_{X}/\mathcal{J})$. An _open subprescheme_ is the prescheme $(U, \mathcal{O}_{X} | U)$ induced on an
open $U \subset X$. A _subprescheme_ is the closed subprescheme of an open subprescheme.

**Proposition (4.1.5).** A closed subprescheme is uniquely determined by its sheaf of ideals.

**Proposition (4.1.6).** For an affine scheme $X = \operatorname{Spec}(A)$: closed subpreschemes correspond bijectively
to ideals $\mathfrak{J} \subset A$, the closed subprescheme being $\operatorname{Spec}(A/\mathfrak{J})$.

**Proposition (4.1.9).** Closed subpreschemes of a Noetherian prescheme satisfy the descending chain condition.

**Corollary (4.1.10).** Every prescheme is a union of its open affine subpreschemes (a closed cover of finite type, if
Noetherian).

### 4.2. Immersion morphisms

<!-- label: I.4.2 -->

**Definition (4.2.1).** A morphism $j : Y \to X$ of preschemes is an _open immersion_ (resp. _closed immersion_, resp.
_immersion_) if $j$ is a homeomorphism of $Y$ onto an open (resp. closed, resp. locally closed) subspace of $X$ and
$j^{\sharp} : \mathcal{O}_{X} \to j_{*}(\mathcal{O}_{Y})$ is surjective onto the structure sheaf of the corresponding
subprescheme. Equivalently, $j$ factors as $Y \xrightarrow{\sim} Y' \hookrightarrow X$ with $Y'$ an open (resp. closed,
resp. locally closed) subprescheme.

**Proposition (4.2.2).** Composition of immersions is an immersion; the composite of two open (resp. closed) immersions
is open (resp. closed).

**Corollary (4.2.3).** Immersions are monomorphisms of preschemes.

**Corollary (4.2.4).** An immersion is radicial.

**Proposition (4.2.5).** Immersions are preserved under base change.

### 4.3. Products of immersions

<!-- label: I.4.3 -->

**Proposition (4.3.1).** If $j_{1} : Y_{1} \to X_{1}$ and $j_{2} : Y_{2} \to X_{2}$ are immersions of $S$-preschemes,
then $j_{1} \times_{S} j_{2} : Y_{1} \times_{S} Y_{2} \to X_{1} \times_{S} X_{2}$ is an immersion (open or closed if
both factors are).

**Corollary (4.3.2).** Open immersions and closed immersions are stable under fiber products.

### 4.4. Inverse images of subpreschemes

<!-- label: I.4.4 -->

**Proposition (4.4.1).** For a morphism $f : X \to Y$ and a closed subprescheme $Y' \subset Y$ with ideal sheaf
$\mathcal{J}$, the inverse image $f^{-1}(Y') = X \times_{Y} Y'$ is a closed subprescheme of $X$ with ideal sheaf
$f*(\mathcal{J}) \cdot \mathcal{O}_{X} = \mathcal{J} \mathcal{O}_{X}$.

**Corollary (4.4.2).** Inverse images preserve closed (resp. open) subpreschemes.

**Corollary (4.4.3).** For composable morphisms, $(g \circ f)^{-1}(Z) = f^{-1}(g^{-1}(Z))$.

**Corollary (4.4.4).** Inverse images preserve immersions.

**Proposition (4.4.5).** For morphisms $X \to Y \to S$ and a subprescheme $Y' \subset Y$, $X \times_{Y} Y' = X
\times_{S} Y'$ (when $Y' \hookrightarrow Y$ is an immersion).

### 4.5. Local immersions and local isomorphisms

<!-- label: I.4.5 -->

**Definition (4.5.1).** A morphism $f : X \to Y$ is a _local immersion at_ $x \in X$ if there is an open $U \ni x$ such
that $f | U : U \to Y$ is an immersion. $f$ is a _local immersion_ if it is so at every point.

**Definition (4.5.2).** A morphism $f : X \to Y$ is a _local isomorphism at_ $x$ if there is an open $U \ni x$ and an
open $V \supset f(U)$ such that $f | U \to V$ is an isomorphism. $f$ is a _local isomorphism_ if it is so at every
point.

**Proposition (4.5.4).** A local immersion is radicial (and so injective on geometric points stalkwise).

**Proposition (4.5.5).** A local isomorphism is open. A radicial local isomorphism is a local immersion.
