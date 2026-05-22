# Chapter I — The Language of Schemes

## §7. Rational Maps

<!-- label: I.7 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference .

### 7.1. Rational maps and rational functions

<!-- label: I.7.1 -->

**(7.1.1)** Two $S$-morphisms $f_{1} : U_{1} \to Y$, $f_{2} : U_{2} \to Y$ from dense open subsets $U_{1}, U_{2} \subset
X$ are _equivalent_ if they agree on a dense open of $U_{1} \cap U_{2}$. This is an equivalence relation among morphisms
from dense opens; an equivalence class is a _rational $S$-map_ $X \dashrightarrow Y$.

**Definition (7.1.2).** A _rational $S$-map_ from $X$ to $Y$ (or _$S$-rational map_) is an equivalence class as above. A
_rational function_ on $X$ is a rational map $X \dashrightarrow \operatorname{Spec}(\mathbb{Z}[T])$ — equivalently, an
element of the _ring of rational functions_ of $X$ (defined below).

**Proposition (7.1.5).** When $X$ is irreducible with generic point $\eta$, every rational map $X \dashrightarrow Y$ is
determined by a morphism $\operatorname{Spec}(\kappa(\eta)) \to Y$ of $S$-preschemes (i.e., by a $\kappa(\eta)$-rational
point of $Y$).

**Proposition (7.1.7).** For $X$ irreducible, rational $S$-maps $X \dashrightarrow Y$ correspond bijectively to
morphisms $\operatorname{Spec}(\mathcal{O}_{X,\eta}) \to Y$ of $S$-preschemes.

**Corollary (7.1.8).** For $X$ integral, the _ring of rational functions on $X$_ $R(X)$ is the field of fractions of
$\mathcal{O}_{X,\eta}$ (the local ring at the generic point).

**Corollary (7.1.9).** For $X$ integral with function field $R(X) = K$, rational maps $X \dashrightarrow Y$ correspond
bijectively to $K$-rational points of $Y$ (when $Y \to S$ is appropriate).

**Proposition (7.1.11).** For $X$ having finitely many irreducible components $X_{i}$ with generic points $\eta_{i}$,
the _ring of rational functions_ is $R(X) = \prod_{i} \mathcal{O}_{X,\eta_{i}}$ (product of local rings at generic
points).

**Corollaries (7.1.12)–(7.1.16).** Functoriality and base-change properties of $R(X)$; rational maps compose when
defined; the field/ring $R(X)$ is the ring of rational sections of $\mathcal{O}_{X}$ along the generic-fiber
subprescheme.

### 7.2. Domain of definition of a rational map

<!-- label: I.7.2 -->

**Definition (7.2.1).** The _domain of definition_ of a rational map $f : X \dashrightarrow Y$ is the union of all open
$U \subset X$ on which $f$ is represented by an honest morphism $U \to Y$. A rational map is _defined at_ $x \in X$ if
$x$ is in its domain.

**Proposition (7.2.2).** The domain of definition is open.

**Corollaries (7.2.3)–(7.2.7).** Properties of domains of definition: stability under composition; restriction; behavior
under base change.

**(7.2.8)** A rational map $f : X \dashrightarrow \operatorname{Spec}(B)$ to an affine target is defined at $x$ iff each
generator $b \in B$ "extends" to a section of $\mathcal{O}_{X}$ in a neighborhood of $x$.

**Proposition (7.2.9).** For $X$ integral and $Y$ separated, a rational map $f : X \dashrightarrow Y$ is determined by
its restriction to any nonempty open of the domain of definition.

### 7.3. Sheaf of rational functions

<!-- label: I.7.3 -->

**(7.3.1)** Define the _sheaf of rational functions_ $\mathcal{K}_{X}$ on $X$ as the sheaf associated with the presheaf
`U ↦ R(U) = (ring of rational functions on U)`.

**Definition (7.3.2).** A _meromorphic function_ on $X$ is a section of $\mathcal{K}_{X}$. The sheaf $\mathcal{K}_{X}$
is an $\mathcal{O}_{X}$-module containing $\mathcal{O}_{X}$ as a subsheaf.

**Proposition (7.3.3).** When $X$ is integral, $\mathcal{K}_{X}$ is the constant sheaf with stalks $R(X)$.

**Corollaries (7.3.4)–(7.3.6).** Behavior of $\mathcal{K}_{X}$ under open immersions, sums, and reduction.

**Proposition (7.3.7).** For $X$ locally Noetherian, the _total ring of fractions_ sheaf $\mathcal{K}_{X}$ is the
sheafification of $U \mapsto S^{-1}_{U} \Gamma(U, \mathcal{O}_{X})$ where `S_U` is the set of non-zero-divisors in
$\Gamma(U, \mathcal{O}_{X})$.

### 7.4. Torsion and torsion-free sheaves

<!-- label: I.7.4 -->

**(7.4.1)** For an $\mathcal{O}_{X}$-module $\mathcal{F}$, the _torsion subsheaf_ $t(\mathcal{F}) \subset \mathcal{F}$
is the kernel of $\mathcal{F} \to \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{K}_{X}$. $\mathcal{F}$ is
_torsion-free_ if $t(\mathcal{F}) = 0$, _torsion_ if $t(\mathcal{F}) = \mathcal{F}$.

**Proposition (7.4.2).** Torsion is functorial; $t(\mathcal{F})$ is the largest torsion subsheaf.

**(7.4.2)** For $\mathcal{F}$ torsion-free of finite rank, the _rank_ is the rank of $\mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{K}_{X}$ as an $\mathcal{K}_{X}$-module.

**Corollary (7.4.3).** On an integral prescheme, the rank of a torsion-free coherent sheaf is well-defined (constant).

**Proposition (7.4.5)–(7.4.6).** Torsion behavior under direct sums, tensor products, and pullback.
