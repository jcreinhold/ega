# Chapter I — The Language of Schemes

## §8. Chevalley Schemes

<!-- label: I.8 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference .

### 8.1. Allied local rings

<!-- label: I.8.1 -->

**Lemma (8.1.1).** Let $(A_{\lambda})$ be a family of local rings inside a fixed field $K$, with $A_{\lambda} \subset
A_{\mu}$ if and only if the corresponding maximal ideals satisfy $\mathfrak{m}_{\lambda} \supset \mathfrak{m}_{\mu} \cap
A_{\lambda}$. Then there is a unique smallest local ring containing all the $A_{\lambda}$ inside $K$.

**(8.1.1)** Two local subrings $A_{1}, A_{2} \subset K$ are _allied_ (or _related_, _apparentés_ in EGA) if there is a
chain $A_{1} = B_{0} \subset B_{1} \supset B_{2} \subset B_{3} \supset \cdots \supset B_{n} = A_{2}$ of local subrings
with each inclusion either an extension of dominating local rings or its inverse.

**Lemma (8.1.3).** Allied is an equivalence relation. Allied local rings have the same field of fractions.

**Lemma (8.1.4).** For local rings $A_{1}, A_{2} \subset K$ with the same fraction field, alliance is captured by
intersection: `A_1` and `A_2` are allied iff there is a finite sequence of local rings between them with successive
dominance/anti-dominance.

**Definition (8.1.4).** A local subring $A_{2} \subset K$ _dominates_ `A_1` if $A_{1} \subset A_{2}$ and
$\mathfrak{m}_{1} \subset \mathfrak{m}_{2}$ (where $\mathfrak{m}_{i}$ is the maximal ideal of $A_{i}$). A _local ring of
integral type_ over $K$ is one that dominates a finitely generated subalgebra of $K$.

**Proposition (8.1.5).** Allied local rings have the same dimension and the same residue field up to isomorphism.

### 8.2. Local rings of an integral scheme

<!-- label: I.8.2 -->

**(8.2.1)** Let $X$ be an integral prescheme with function field $K = R(X)$. For every $x \in X$, $\mathcal{O}_{x}$ is a
local subring of $K$. The collection ${\mathcal{O}_{x} : x \in X}$ determines $X$ up to canonical isomorphism in a
precise sense:

**Proposition (8.2.2).** Let $K$ be a field. A _scheme $X$ over $K$_ in Chevalley's sense is a family
$(A_{\alpha})_{\alpha \in I}$ of local subrings of $K$, with shared field of fractions $K$, satisfying:

> (a) Every two $A_{\alpha}, A_{\beta}$ are allied; (b) Every prime ideal of every $A_{\alpha}$ is the contraction of
> some $A_{\beta}$'s prime; (c) The corresponding "spectrum" is irreducible.

The set $X$ of these local subrings is then in canonical bijection with the points of an integral prescheme over
$\operatorname{Spec}(K)$, with $\mathcal{O}_{x} = A_{\alpha}$ for the corresponding $\alpha$.

**Corollary (8.2.3).** An integral $K$-scheme is determined by its function field and the family of its local rings.

**Corollary (8.2.4).** Morphisms of integral schemes correspond to compatible families of local-ring inclusions.

**Corollary (8.2.5).** Integral subschemes of an integral scheme $X$ correspond to "irreducible closed" subfamilies of
the local rings.

**Proposition (8.2.7).** Chevalley's classical schemes (in his _Séminaire_) are equivalent to integral algebraic schemes
over a field.

**Proposition (8.2.8).** Algebraic varieties in the sense of Serre's (FAC) are precisely integral algebraic $K$-schemes.

### 8.3. Chevalley schemes

<!-- label: I.8.3 -->

A _Chevalley scheme_ over a field $K$ is an integral algebraic $K$-scheme (in the EGA sense) — i.e., a finite-type,
separated, integral $K$-scheme. The terminology is preserved historically; see (8.2.7).
