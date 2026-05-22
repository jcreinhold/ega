# Chapter I — The Language of Schemes

## §9. Complements on Quasi-coherent Sheaves

<!-- label: I.9 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference .

### 9.1. Tensor product of quasi-coherent sheaves

<!-- label: I.9.1 -->

**Proposition (9.1.1).** For quasi-coherent $\mathcal{O}_{X}$-modules $\mathcal{F}$, $\mathcal{G}$ on a prescheme $X$,
$\mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{G}$ is quasi-coherent.

**Definition (9.1.2).** For preschemes $X_{1}, X_{2}$ and quasi-coherent $\mathcal{O}_{X_{i}}$-modules $\mathcal{F}_{i}$
($i = 1, 2$), the _tensor product on distinct preschemes_ $\mathcal{F}_{1} \boxtimes \mathcal{F}_{2} =
p^{*}_{1}(\mathcal{F}_{1}) \otimes_{\mathcal{O}_{X_{1} \times_{S} X_{2}}} p^{*}_{2}(\mathcal{F}_{2})$ on $X_{1}
\times_{S} X_{2}$ (where $p_{i}$ is the projection).

**Proposition (9.1.3).** External tensor product is quasi-coherent; bifunctorial in $\mathcal{F}_{1}, \mathcal{F}_{2}$.

**Proposition (9.1.4).** _Restriction of scalars and base change preserve quasi-coherence:_ for $f : X \to Y$ and
$\mathcal{F}$ quasi-coherent on $Y$, $f*(\mathcal{F})$ is quasi-coherent on $X$.

**Corollaries (9.1.5)–(9.1.7).** Behavior under sub- and quotient-modules, kernels, cokernels, inductive limits.

**Proposition (9.1.9)–(9.1.12).** Exactness properties: $f*$ is right exact; if $f$ is flat, $f*$ is exact.

**Corollary (9.1.13).** Stalks of pullback: $(f*(\mathcal{F}))_{x} = \mathcal{F}_{f(x)} \otimes_{\mathcal{O}_{f(x)}}
\mathcal{O}_{x}$.

### 9.2. Direct image of a quasi-coherent sheaf

<!-- label: I.9.2 -->

**Proposition (9.2.1).** For $f : X \to Y$ a _quasi-compact, separated_ morphism, and $\mathcal{F}$ quasi-coherent on
$X$, the direct image $f_{*}(\mathcal{F})$ is quasi-coherent on $Y$.

**Corollary (9.2.2).** For an affine morphism $f : X \to Y$ (i.e., the preimage of every affine open is affine), $f_{*}$
preserves quasi-coherence.

### 9.3. Extension of sections

<!-- label: I.9.3 -->

**Theorem (9.3.1).** Let $X$ be a Noetherian prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-module, $U
\subset X$ open. Every section $s \in \Gamma(U, \mathcal{F})$ extends to a section of $\mathcal{F} \otimes
\mathcal{O}_{X}(D)$ for some divisor $D$ supported on $X \setminus U$ (after multiplying by powers of local equations).

**Corollary (9.3.2)–(9.3.3).** Sections over $U = X_{f}$ extend to global sections after multiplying by a power of $f$.

**Proposition (9.3.4).** Behavior of section extension under flat base change.

**Corollary (9.3.5).** For Noetherian $X$ and quasi-compact $U$, $\Gamma(U, \mathcal{F})$ is a localization of
$\Gamma(X, \mathcal{F})$ in a precise functorial sense.

### 9.4. Extension of quasi-coherent sheaves

<!-- label: I.9.4 -->

**(9.4.1)** For $X$ a Noetherian prescheme, $U \subset X$ open, and $\mathcal{F}$ quasi-coherent on $U$, an _extension_
of $\mathcal{F}$ to $X$ is a quasi-coherent $\mathcal{O}_{X}$-module $\tilde{\mathcal{F}}$ with $\tilde{\mathcal{F}} | U
\cong \mathcal{F}$.

**Proposition (9.4.2).** _Existence of extension:_ every quasi-coherent sheaf on $U$ extends to a quasi-coherent sheaf
on $X$.

**Corollary (9.4.3).** Coherent extensions: a coherent sheaf on $U$ extends to a coherent sheaf on $X$ whose restriction
to $U$ is the given one.

**Corollary (9.4.5).** Quasi-coherent sub-Modules of a coherent sheaf extend to quasi-coherent sub-Modules.

**Lemma (9.4.6).** Bounded-from-below $\mathcal{J}$-adic filtrations: for a quasi-coherent ideal $\mathcal{J}$ and
coherent $\mathcal{F}$, the canonical filtration $\mathcal{J}^{n} \mathcal{F}$ decreases to a quasi-coherent submodule.

**Theorem (9.4.7).** _Theorem of extension of subsheaves:_ every quasi-coherent subsheaf of $\mathcal{F} | U$ extends to
a quasi-coherent subsheaf of $\mathcal{F}$ on $X$.

**Corollaries (9.4.8)–(9.4.10).** Consequences for closed subpreschemes, base change, and morphisms.

### 9.5. Closed image of a prescheme; closure of a subprescheme

<!-- label: I.9.5 -->

**Proposition (9.5.1).** For $f : X \to Y$ with $X$ Noetherian (or $f$ quasi-compact), the kernel $\mathcal{J} =
Ker(\mathcal{O}_{Y} \to f_{*}(\mathcal{O}_{X}))$ is a quasi-coherent ideal sheaf, defining the _closed image_ $f\bar{X}$
(with reduced subprescheme structure) — the smallest closed subprescheme of $Y$ through which $f$ factors.

**Corollary (9.5.2).** The closed image is the closure of the set-theoretic image in $Y$ with its reduced subprescheme
structure when $Y$ is reduced.

**Definition (9.5.3).** The _closure_ of a subprescheme $Y' \hookrightarrow Y$ (or _adherence_ of a subprescheme) is the
closed image of $Y' \to Y$.

**Propositions (9.5.4)–(9.5.6).** Functoriality of the closure under base change and composition.

**Propositions (9.5.8)–(9.5.10).** Closures and irreducible components: the closure of $Y'$ decomposes by the
irreducible components of $Y\bar{'}$.

**Corollary (9.5.11).** _Closure of a subprescheme_: $Y' \hookrightarrow Y$ extends uniquely (up to isomorphism) to a
closed subprescheme of $Y$ containing $Y'$ as a dense open subprescheme.

### 9.6. Quasi-coherent sheaves of algebras; change of structure sheaf

<!-- label: I.9.6 -->

**Proposition (9.6.1).** For a quasi-coherent $\mathcal{O}_{X}$-algebra $\mathcal{A}$, the ringed space $(X,
\mathcal{A})$ is not in general a prescheme, but its "Spec" is — see (9.6.5).

**Proposition (9.6.3).** Quasi-coherence is preserved under change of structure sheaf for affine morphisms.

**Corollary (9.6.4).** Tensor products of quasi-coherent algebras are quasi-coherent.

**Proposition (9.6.5) (Spec of a quasi-coherent algebra).** For $(X, \mathcal{O}_{X})$ a prescheme and $\mathcal{A}$ a
quasi-coherent $\mathcal{O}_{X}$-algebra, there is an affine morphism $f : \operatorname{Spec}(\mathcal{A}) \to X$ such
that $f_{*}(\mathcal{O}_{\operatorname{Spec}(\mathcal{A})}) = \mathcal{A}$ and $\operatorname{Spec}(\mathcal{A})$ is
universal among $X$-preschemes whose direct image yields $\mathcal{A}$.

**Proposition (9.6.6).** Properties of $\operatorname{Spec}(\mathcal{A})$: it is separated; coherent if $\mathcal{A}$ is
locally finitely presented; functorial in $\mathcal{A}$.
