# §3. The finiteness theorem for proper morphisms

<!-- original page 115 -->

## 3.1. The dévissage lemma

**Definition (3.1.1).**

<!-- label: III.3.1.1 -->

Let $\mathcal{C}$ be an abelian category. We say that a subset $\mathcal{C}'$ of the set of objects of $\mathcal{C}$ is
*exact* if $0 \in \mathcal{C}'$ and if, for every exact sequence $0 \to A' \to A \to A'' \to 0$ in $\mathcal{C}$ such
that two of the objects $A$, $A'$, `A''` are in $\mathcal{C}'$, then the third is also in $\mathcal{C}'$.

**Theorem (3.1.2).**

<!-- label: III.3.1.2 -->

*Let $X$ be a Noetherian prescheme; denote by $\mathcal{C}$ the abelian category of coherent $\mathcal{O}_{X}$-modules.
Let $\mathcal{C}'$ be an exact subset of $\mathcal{C}$, and $X'$ a closed subset of the underlying space of $X$. Suppose
that for every closed irreducible subset $Y$ of $X'$, with generic point $y$, there exists an $\mathcal{O}_{X}$-module
$\mathcal{G} \in \mathcal{C}'$ such that $\mathcal{G}_{y}$ is a $\kappa(y)$-vector space of dimension `1`. Then every
coherent $\mathcal{O}_{X}$-module with support contained in $X'$ belongs to $\mathcal{C}'$ (and in particular, if $X' =
X$, then $\mathcal{C}' = \mathcal{C}$).*

**Proof.** Consider the following property $P(Y)$ of a closed subset $Y$ of $X'$: every coherent
$\mathcal{O}_{X}$-module with support contained in $Y$ belongs to $\mathcal{C}'$. By virtue of the principle of
Noetherian induction $(0_{I}, 2.2.2)$, we see that we are reduced to proving that *if $Y$ is a closed subset of $X'$
such that the property $P(Y')$ is true for every closed subset $Y'$ of $Y$, distinct from $Y$, then $P(Y)$ is true*.

So let $\mathcal{F} \in \mathcal{C}$ have support contained in $Y$, and let us prove that $\mathcal{F} \in
\mathcal{C}'$. Denote also by $Y$ the closed reduced subprescheme of $X$ having $Y$ for underlying space `(I, 5.2.1)`;
it is defined by a coherent sheaf of ideals $\mathcal{J}$ of $\mathcal{O}_{X}$. We know `(I, 9.3.4)` that there exists
an integer $n > 0$ such that $\mathcal{J}^{n} \mathcal{F} = 0$; for $1 \leq k \leq n$, we thus have an exact sequence

```text
  0 → 𝒥^{k−1} ℱ / 𝒥^k ℱ → ℱ / 𝒥^k ℱ → ℱ / 𝒥^{k−1} ℱ → 0
```

of coherent $\mathcal{O}_{X}$-modules $(0_{I}, 5.3.6 and 5.3.3)$; as $\mathcal{C}'$ is exact, we see, by induction on
$k$, that it suffices to show that each of the $\mathcal{F}_{k} = \mathcal{J}^{k-1} \mathcal{F} / \mathcal{J}^{k}
\mathcal{F}$ is in $\mathcal{C}'$. We are thus reduced to proving that $\mathcal{F} \in \mathcal{C}'$ under the
additional hypothesis that $\mathcal{J} \mathcal{F} = 0$; this is equivalent to saying that $\mathcal{F} =
j_{*}(j^{*}(\mathcal{F}))$, where $j$ is the canonical injection $Y \to X$. We now distinguish two cases:

a) *$Y$ is reducible.* Let $Y = Y' \cup Y''$, where $Y'$ and `Y''` are closed subsets of $Y$, distinct from $Y$; denote
also by $Y'$, `Y''` the closed reduced subpreschemes of $X$ having $Y'$, `Y''` respectively for underlying spaces,
defined respectively by the coherent sheaves of ideals $\mathcal{J}'$, $\mathcal{J}''$ of $\mathcal{O}_{X}$. Set
$\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X} / \mathcal{J}')$ and $\mathcal{F}'' = \mathcal{F}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X} / \mathcal{J}'')$. The canonical homomorphisms $\mathcal{F} \to
\mathcal{F}'$, $\mathcal{F} \to \mathcal{F}''$ thus define a homomorphism $u : \mathcal{F} \to \mathcal{F}' \oplus
\mathcal{F}''$. We show that for every $z \notin Y' \cap Y''$, the homomorphism $u_{z} : \mathcal{F}_{z} \to
\mathcal{F}'_{z} \oplus \mathcal{F}''_{z}$ is *bijective*. Indeed, we have $\mathcal{J}' \cap \mathcal{J}'' =
\mathcal{J}$, since the question is local and

<!-- original page 116 -->

the preceding equality results from `(I, 5.2.1 and 1.1.5)`; if $z \notin Y''$, we then have $\mathcal{J}''_{z} =
\mathcal{O}_{X,z}$, hence $\mathcal{F}''_{z} = 0$ and $\mathcal{F}'_{z} = \mathcal{F}_{z}$, which establishes our
assertion in this case; we reason similarly for $z \notin Y'$. Consequently, the kernel and cokernel of $u$, which are
in $\mathcal{C}$ $(0_{I}, 5.3.4)$, have their support in $Y' \cap Y''$, and are thus in $\mathcal{C}'$ by hypothesis;
for the same reason, $\mathcal{F}'$ and $\mathcal{F}''$ are in $\mathcal{C}'$, hence also $\mathcal{F}' \oplus
\mathcal{F}''$, since $\mathcal{C}'$ is exact. The conclusion then follows from the consideration of the two exact
sequences

```text
  0 → Im u → ℱ' ⊕ ℱ'' → Coker u → 0,
  0 → Ker u → ℱ → Im u → 0,
```

and from the hypothesis that $\mathcal{C}'$ is exact.

b) *$Y$ is irreducible*, and consequently the subprescheme $Y$ of $X$ is *integral*. If $y$ is its generic point, we
have $(\mathcal{O}_{Y})_{y} = \kappa(y)$, and as $j^{*}(\mathcal{F})$ is a coherent $\mathcal{O}_{Y}$-module,
$\mathcal{F}_{y} = (j^{*}(\mathcal{F}))_{y}$ is a $\kappa(y)$-vector space of finite dimension $m$. By hypothesis, there
is a coherent $\mathcal{O}_{X}$-module $\mathcal{G} \in \mathcal{C}'$ (necessarily of support $Y$) such that
$\mathcal{G}_{y}$ is a $\kappa(y)$-vector space of dimension `1`. Consequently, there is a $\kappa(y)$-isomorphism
$(\mathcal{G}_{y})^{m} \xrightarrow{\sim} \mathcal{F}_{y}$, which is also an $\mathcal{O}_{Y}$-isomorphism, and since
$\mathcal{G}^{m}$ and $\mathcal{F}$ are coherent, there exists an open neighbourhood $W$ of $y$ in $X$ and an
isomorphism $\mathcal{G}^{m} \mid W \xrightarrow{\sim} \mathcal{F} \mid W$ $(0_{I}, 5.2.7)$. Let $\mathcal{H}$ be the
graph of this isomorphism, which is a coherent $(\mathcal{O}_{X} \mid W)$-submodule of $(\mathcal{G}^{m} \oplus
\mathcal{F}) \mid W$, canonically isomorphic to $\mathcal{G}^{m} \mid W$ and to $\mathcal{F} \mid W$; there thus exists
a coherent $\mathcal{O}_{X}$-submodule $\mathcal{H}_{0}$ of $\mathcal{G}^{m} \oplus \mathcal{F}$, inducing $\mathcal{H}$
on $W$ and `0` on $X - Y$, since $\mathcal{G}^{m}$ and $\mathcal{F}$ have $Y$ for support `(I, 9.4.7)`. The restrictions
$v : \mathcal{H}_{0} \to \mathcal{G}^{m}$ and $w : \mathcal{H}_{0} \to \mathcal{F}$ of the canonical projections of
$\mathcal{G}^{m} \oplus \mathcal{F}$ are then homomorphisms of coherent $\mathcal{O}_{X}$-modules, which, on $W$ and on
$X - Y$, reduce to isomorphisms; in other words, the kernels and cokernels of $v$ and $w$ have their support in the
closed set $Y - (Y \cap W)$, distinct from $Y$. They are thus in $\mathcal{C}'$; on the other hand, $\mathcal{G}^{m} \in
\mathcal{C}'$ since $\mathcal{G} \in \mathcal{C}'$ and $\mathcal{C}'$ is exact. We conclude successively, by the
exactness of $\mathcal{C}'$, that $\mathcal{H}_{0} \in \mathcal{C}'$ and then $\mathcal{F} \in \mathcal{C}'$. Q.E.D.

**Corollary (3.1.3).**

<!-- label: III.3.1.3 -->

*Suppose that the exact subset $\mathcal{C}'$ of $\mathcal{C}$ has in addition the property that every coherent direct
factor of a coherent $\mathcal{O}_{X}$-module $\mathcal{M} \in \mathcal{C}'$ is again in $\mathcal{C}'$. Under these
conditions, the conclusion of (3.1.2) remains valid when the condition "$\mathcal{G}_{y}$ is a $\kappa(y)$-vector space
of dimension `1`" is replaced by $\mathcal{G}_{y} \neq 0$ (which is equivalent to $Supp(\mathcal{G}) = Y$).*

**Proof.** Indeed, the reasoning of (3.1.2) need be modified only in case b); this time $\mathcal{G}_{y}$ is a
$\kappa(y)$-vector space of dimension $q > 0$, and we have consequently an $\mathcal{O}_{Y}$-isomorphism
$(\mathcal{G}_{y})^{m} \xrightarrow{\sim} (\mathcal{F}_{y})^{q}$; the end of the reasoning of (3.1.2) then proves that
$\mathcal{F}^{q} \in \mathcal{C}'$, and the additional hypothesis on $\mathcal{C}'$ implies that $\mathcal{F} \in
\mathcal{C}'$.

## 3.2. The finiteness theorem: case of usual schemes

**Theorem (3.2.1).**

<!-- label: III.3.2.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a proper morphism. For every coherent $\mathcal{O}_{X}$-module
$\mathcal{F}$, the $\mathcal{O}_{Y}$-modules $R^{q} f_{*}(\mathcal{F})$ are coherent for $q \geq 0$.*

**Proof.** The question being local on $Y$, we may suppose $Y$ Noetherian, hence $X$ Noetherian `(I, 6.3.7)`. The
coherent $\mathcal{O}_{X}$-modules $\mathcal{F}$ for which the conclusion of Theorem (3.2.1) is true form an *exact*
subset $\mathcal{C}'$ of the category $\mathcal{C}$ of coherent $\mathcal{O}_{X}$-modules.

<!-- original page 117 -->

Indeed, let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence of coherent
$\mathcal{O}_{X}$-modules; suppose for example that $\mathcal{F}'$ and $\mathcal{F}''$ belong to $\mathcal{C}'$; we have
the long exact sequence in cohomology

```text
  R^{q−1} f_*(ℱ'') →^∂ R^q f_*(ℱ') → R^q f_*(ℱ) → R^q f_*(ℱ'') →^∂ R^{q+1} f_*(ℱ'),
```

in which by hypothesis the four outer terms are coherent; the middle term $R^{q} f_{*}(\mathcal{F})$ is therefore
likewise coherent by $(0_{I}, 5.3.4 and 5.3.3)$. One shows in the same way that when $\mathcal{F}$ and $\mathcal{F}'$
(resp. $\mathcal{F}$ and $\mathcal{F}''$) are in $\mathcal{C}'$, so is $\mathcal{F}''$ (resp. $\mathcal{F}'$). Moreover,
every coherent *direct factor* $\mathcal{F}'$ of an $\mathcal{O}_{X}$-module $\mathcal{F} \in \mathcal{C}'$ also belongs
to $\mathcal{C}'$: indeed, $R^{q} f_{*}(\mathcal{F}')$ is then a direct factor of $R^{q} f_{*}(\mathcal{F})$
`(G, II, 4.4.4)`, hence of finite type, and since it is quasi-coherent (1.4.10), it is coherent, $Y$ being Noetherian.
By virtue of (3.1.3), we are reduced to proving that when $X$ is *irreducible* with generic point $x$, there exists
*one* coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ belonging to $\mathcal{C}'$ such that $\mathcal{F}_{x} \neq 0$:
indeed, if this point is established, it can be applied to every irreducible closed subprescheme $Y$ of $X$, since if
$j : Y \to X$ is the canonical injection, then $f \circ j$ is proper `(II, 5.4.2)`, and if $\mathcal{G}$ is a coherent
$\mathcal{O}_{Y}$-module with support $Y$, then $j_{*}(\mathcal{G})$ is a coherent $\mathcal{O}_{X}$-module such that
$R^{q} (f \circ j)_{*}(\mathcal{G}) = R^{q} f_{*}(j_{*}(\mathcal{G}))$ `(G, II, 4.9.1)`, so we are indeed in the
conditions of application of (3.1.3).

Now, by virtue of Chow's lemma `(II, 5.6.2)`, there exists an irreducible prescheme $X'$ and a *projective* and
surjective morphism $g : X' \to X$ such that $f \circ g : X' \to Y$ is *projective*. There exists an
$\mathcal{O}_{X'}$-module $\mathcal{L}$ ample for $g$ `(II, 5.3.1)`; let us apply the fundamental theorem of projective
morphisms (2.2.1) to $g : X' \to X$ and to $\mathcal{L}$: there thus exists an integer $n$ such that
$\mathcal{F} = g_{*}(\mathcal{O}_{X'}(n))$ is a coherent $\mathcal{O}_{X}$-module and
$R^{q} g_{*}(\mathcal{O}_{X'}(n)) = 0$ for all $q > 0$; in addition, since
$g^{*}(g_{*}(\mathcal{O}_{X'}(n))) \to \mathcal{O}_{X'}(n)$ is surjective for $n$ large enough (2.2.1), we see that we
may suppose that, at the generic point $x$ of $X$, we have $\mathcal{F}_{x} \neq 0$ `(II, 3.4.7)`. On the other hand,
since $f \circ g$ is projective and $Y$ Noetherian, the $R^{p}(f \circ g)_{*}(\mathcal{O}_{X'}(n))$ are *coherent*
(2.2.1). This being so, $R^{\bullet}(f \circ g)_{*}(\mathcal{O}_{X'}(n))$ is the abutment of a Leray spectral sequence,
whose `E_2`-term is given by $E^{p,q}_{2} = R^{p} f_{*}(R^{q} g_{*}(\mathcal{O}_{X'}(n)))$; what precedes shows that
this spectral sequence is degenerate, and we then know $(0_{III}, 11.1.6)$ that $E^{p,0}_{2} = R^{p} f_{*}(\mathcal{F})$
is isomorphic to $R^{p}(f \circ g)_{*}(\mathcal{O}_{X'}(n))$, which completes the proof.

**Corollary (3.2.2).**

<!-- label: III.3.2.2 -->

*Let $Y$ be a locally Noetherian prescheme. For every proper morphism $f : X \to Y$, the direct image under $f$ of any
coherent $\mathcal{O}_{X}$-module is a coherent $\mathcal{O}_{Y}$-module.*

**Corollary (3.2.3).**

<!-- label: III.3.2.3 -->

*Let $A$ be a Noetherian ring, $X$ a proper scheme over $A$; for every coherent $\mathcal{O}_{X}$-module $\mathcal{F}$,
the $H^{p}(X, \mathcal{F})$ are $A$-modules of finite type, and there exists an integer $r > 0$ such that for every
coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ and every $p > r$, $H^{p}(X, \mathcal{F}) = 0$.*

**Proof.** The second assertion has already been proved (1.4.12); the first follows from the finiteness theorem (3.2.1),
taking (1.4.11) into account.

In particular, if $X$ is a *proper algebraic scheme* over a field $k$, then, for every coherent $\mathcal{O}_{X}$-module
$\mathcal{F}$, the $H^{p}(X, \mathcal{F})$ are $k$-vector spaces of *finite dimension*.

**Corollary (3.2.4).**

<!-- label: III.3.2.4 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism of finite type. For every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$ whose support is proper over $Y$ `(II, 5.4.10)`, the $\mathcal{O}_{Y}$-modules
$R^{q} f_{*}(\mathcal{F})$ are coherent.*

<!-- original page 118 -->

**Proof.** The question being local on $Y$, we may suppose $Y$ Noetherian, and it is then the same for $X$ `(I, 6.3.7)`.
By hypothesis, every closed subprescheme $Z$ of $X$ whose underlying space is $Supp(\mathcal{F})$ is proper over $Y$; in
other words, if $j : Z \to X$ is the canonical injection, then $f \circ j : Z \to Y$ is proper. Now, we may suppose $Z$
is such that $\mathcal{F} = j_{*}(\mathcal{G})$, where $\mathcal{G} = j^{*}(\mathcal{F})$ is a coherent
$\mathcal{O}_{Z}$-module `(I, 9.3.5)`; as we have $R^{q} f_{*}(\mathcal{F}) = R^{q} (f \circ j)_{*}(\mathcal{G})$ by
(1.3.4), the conclusion follows immediately from (3.2.1).

## 3.3. Generalization of the finiteness theorem (usual schemes)

**Proposition (3.3.1).**

<!-- label: III.3.3.1 -->

*Let $Y$ be a Noetherian prescheme, $\mathcal{S}$ a quasi-coherent $\mathcal{O}_{Y}$-algebra of finite type, graded in
positive degrees, $Y' = \operatorname{Proj}(\mathcal{S})$ and $g : Y' \to Y$ the structure morphism. Let $f : X \to Y$
be a proper morphism, $\mathcal{S}' = f^{*}(\mathcal{S})$, $\mathcal{M} = \oplus_{k \in \mathbb{Z}} \mathcal{M}_{k}$ a
quasi-coherent graded $\mathcal{S}'$-module of finite type. Then the $R^{p} f_{*}(\mathcal{M}) = \oplus_{k \in
\mathbb{Z}} R^{p} f_{*}(\mathcal{M}_{k})$ are graded $\mathcal{S}$-modules of finite type for every $p$. Suppose in
addition that $\mathcal{S}$ is generated by $\mathcal{S}_{1}$; then, for each $p \in \mathbb{Z}$, there exists an
integer $k_{p}$ such that for every $k \geq k_{p}$ and every $r \geq 0$, we have*

```text
  R^p f_*(ℳ_{k+r}) = 𝒮_r R^p f_*(ℳ_k).                                       (3.3.1.1)
```

**Proof.** The first assertion is identical to the statement of (2.4.1, (i)), where one has simply replaced "projective
morphism" by "proper morphism". Now, in the proof of (2.4.1, (i)), the hypothesis on $f$ was used only to show (with the
notation of that proof) that $R^{p} f'_{*}(\tilde{\mathcal{M}})$ is a coherent $\mathcal{O}_{Y'}$-module. With the
hypotheses of (3.3.1), $f'$ is proper `(II, 5.4.2, (iii))`, so the entire proof of (2.4.1, (i)) can be taken over
without change, thanks to the finiteness theorem (3.2.1).

As for the second assertion, it suffices to remark that there is a finite affine open cover $(U_{i})$ of $Y$ such that
the restrictions to $U_{i}$ of the two sides of (3.3.1.1) are equal for every $k \geq k_{p,i}$ `(II, 2.1.6, (ii))`; it
suffices to take for $k_{p}$ the largest of the $k_{p,i}$.

**Corollary (3.3.2).**

<!-- label: III.3.3.2 -->

*Let $A$ be a Noetherian ring, $\mathfrak{m}$ an ideal of $A$, $X$ a proper $A$-scheme, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-module. Then, for every $p \geq 0$, the direct sum $\oplus_{k \geq 0} H^{p}(X, \mathfrak{m}^{k}
\mathcal{F})$ is a module of finite type over the ring $S = \oplus_{k \geq 0} \mathfrak{m}^{k}$; in particular, there
exists an integer $k_{p} \geq 0$ such that for every $k \geq k_{p}$ and every $r \geq 0$, we have*

```text
  H^p(X, 𝔪^{k+r} ℱ) = 𝔪^r H^p(X, 𝔪^k ℱ).                                     (3.3.2.1)
```

**Proof.** It suffices to apply (3.3.1) with $Y = \operatorname{Spec}(A)$, $\mathcal{S} = \tilde{S}$, $\mathcal{M}_{k} =
\mathfrak{m}^{k} \mathcal{F}$, taking (1.4.11) into account.

It is worth recalling that the $S$-module structure on $\oplus_{k \geq 0} H^{p}(X, \mathfrak{m}^{k} \mathcal{F})$ is
obtained by considering, for every $a \in \mathfrak{m}^{r}$, the map $H^{p}(X, \mathfrak{m}^{k} \mathcal{F}) \to
H^{p}(X, \mathfrak{m}^{k+r} \mathcal{F})$ which comes by passage to cohomology from the multiplication $\mathfrak{m}^{k}
\mathcal{F} \to \mathfrak{m}^{k+r} \mathcal{F}$ defined by $a$ (2.4.1).

<!-- original page 119 -->

## 3.4. The finiteness theorem: case of formal schemes

The results of this section (apart from definition (3.4.1)) will not be used in the rest of this chapter.

**(3.4.1)**

<!-- label: III.3.4.1 -->

Let $\mathfrak{X}$ and $\mathfrak{S}$ be two locally Noetherian formal preschemes `(I, 10.4.2)`, $f : \mathfrak{X} \to
\mathfrak{S}$ a morphism of formal preschemes. We say that $f$ is a *proper morphism* if it satisfies the following
conditions:

1° *$f$ is a morphism of finite type `(I, 10.13.3)`*.

2° *If $\mathcal{K}$ is a sheaf of ideals of definition of $\mathfrak{S}$ and if we set $\mathcal{J} =
f^{*}(\mathcal{K}) \mathcal{O}_{\mathfrak{X}}$, $X_{0} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J})$,
$S_{0} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}} / \mathcal{K})$, the morphism $f_{0} : X_{0} \to S_{0}$ deduced from
$f$ `(I, 10.5.6)` is proper.*

It is immediate that this definition does not depend on the sheaf of ideals of definition $\mathcal{K}$ of
$\mathfrak{S}$ considered; indeed, if $\mathcal{K}'$ is a second sheaf of ideals of definition such that $\mathcal{K}'
\subset \mathcal{K}$, and if we set $\mathcal{J}' = f^{*}(\mathcal{K}') \mathcal{O}_{\mathfrak{X}}$, $X'_{0} =
(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J}')$, $S'_{0} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}} /
\mathcal{K}')$, the morphism $f'_{0} : X'_{0} \to S'_{0}$ deduced from $f$ is such that the diagram

$$ X_{0} \to^{f_{0}} S_{0} \downarrow i \downarrow j X'_{0} \to^{f'_{0}} S'_{0} $$

is commutative, $i$ and $j$ being surjective immersions; it thus comes to the same thing to say that $f_{0}$ or $f'_{0}$
is proper, by virtue of `(II, 5.4.5)`.

Note that, for every $n \geq 0$, if we set $X_{n} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J}^{n+1})$,
$S_{n} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}} / \mathcal{K}^{n+1})$, the morphism $f_{n} : X_{n} \to S_{n}$ deduced
from $f$ `(I, 10.5.6)` is proper for every $n$ as soon as it is for $n = 0$ `(II, 5.4.6)`.

If $g : Y \to Z$ is a proper morphism of usual locally Noetherian preschemes, $Z'$ a closed subset of $Z$, $Y'$ a closed
subset of $Y$ such that $g(Y') \subset Z'$, the extension $\hat{g} : Y_{/Y'} \to Z_{/Z'}$ of $g$ to the completions
`(I, 10.9.1)` is a proper morphism of formal preschemes, as follows from the definition and from `(II, 5.4.5)`.

Let $\mathfrak{X}$ and $\mathfrak{S}$ be two locally Noetherian formal preschemes, $f : \mathfrak{X} \to \mathfrak{S}$ a
morphism of finite type `(I, 10.13.3)`; with the notation being the same as above, one says that a subset $Z$ of the
underlying space of $\mathfrak{X}$ is *proper over $\mathfrak{S}$* (or *proper for $f$*) if, considered as a subset of
`X_0`, $Z$ is *proper over `S_0`* `(II, 5.4.10)`. All the properties of proper subsets of usual preschemes stated in
`(II, 5.4.10)` are still valid for proper subsets of formal preschemes, as follows immediately from the definitions.

**Theorem (3.4.2).**

<!-- label: III.3.4.2 -->

*Let $\mathfrak{X}$, $\mathfrak{Y}$ be two locally Noetherian formal preschemes, $f : \mathfrak{X} \to \mathfrak{Y}$ a
proper morphism. For every coherent $\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, the
$\mathcal{O}_{\mathfrak{Y}}$-modules $R^{q} f_{*}(\mathcal{F})$ are coherent for every $q \geq 0$.*

Let $\mathcal{J}$ be a sheaf of ideals of definition of $\mathfrak{Y}$, $\mathcal{K} = f^{*}(\mathcal{J})
\mathcal{O}_{\mathfrak{X}}$, and consider the $\mathcal{O}_{\mathfrak{X}}$-modules

```text
  ℱ_k = ℱ ⊗_{𝒪_𝔜} (𝒪_𝔜 / 𝒥^{k+1}) = ℱ / 𝒦^{k+1} ℱ            (k ≥ 0)         (3.4.2.1)
```

which obviously form a *projective system* of topological $\mathcal{O}_{\mathfrak{X}}$-modules, such that

<!-- original page 120 -->

$\mathcal{F} = \varprojlim \mathcal{F}_{k}$ `(I, 10.11.3)`. On the other hand, it will follow from (3.4.2) that each of
the $R^{q} f_{*}(\mathcal{F})$, being coherent, is naturally equipped with a structure of topological
$\mathcal{O}_{\mathfrak{Y}}$-module `(I, 10.11.6)`, and the same is true of the $R^{q} f_{*}(\mathcal{F}_{k})$. To the
canonical homomorphisms $\mathcal{F} \to \mathcal{F}_{k} = \mathcal{F} / \mathcal{K}^{k+1} \mathcal{F}$ there
canonically correspond homomorphisms

```text
  R^q f_*(ℱ) → R^q f_*(ℱ_k),
```

which are necessarily continuous for the topological $\mathcal{O}_{\mathfrak{Y}}$-module structures above
`(I, 10.11.6)`, and form a projective system, giving in the limit a canonical functorial homomorphism

```text
  R^q f_*(ℱ) → lim_← R^q f_*(ℱ_k),                                           (3.4.2.2)
                k
```

which will be a continuous homomorphism of topological $\mathcal{O}_{\mathfrak{Y}}$-modules. We shall prove at the same
time as (3.4.2) the

**Corollary (3.4.3).**

<!-- label: III.3.4.3 -->

*Each of the homomorphisms (3.4.2.2) is a topological isomorphism. Furthermore, if $\mathfrak{Y}$ is Noetherian, the
projective system $(R^{q} f_{*}(\mathcal{F} / \mathcal{K}^{k+1} \mathcal{F}))_{k \geq 0}$ satisfies the (ML)-condition
$(0_{III}, 13.1.1)$.*

We shall begin by establishing (3.4.2) and (3.4.3) when $\mathfrak{Y}$ is a Noetherian formal affine scheme
`(I, 10.4.1)`:

**Corollary (3.4.4).**

<!-- label: III.3.4.4 -->

*Under the hypotheses of (3.4.2), suppose in addition that $\mathfrak{Y} = Spf(A)$, where $A$ is an adic Noetherian
ring. Let $\mathfrak{J}$ be an ideal of definition of $A$, and set $\mathcal{F}_{k} = \mathcal{F} / \mathfrak{J}^{k+1}
\mathcal{F}$ for $k \geq 0$. Then the $H^{n}(\mathfrak{X}, \mathcal{F})$ are $A$-modules of finite type; the projective
system $(H^{n}(\mathfrak{X}, \mathcal{F}_{k}))_{k \geq 0}$ satisfies the (ML)-condition for every $n$; if we set*

```text
  N_{n,k} = Ker(H^n(𝔛, ℱ) → H^n(𝔛, ℱ_k))                                     (3.4.4.1)
```

*(also equal to $Im(H^{n}(\mathfrak{X}, \mathfrak{J}^{k+1} \mathcal{F}) \to H^{n}(\mathfrak{X}, \mathcal{F}))$ by the
exact sequence in cohomology), the $N_{n,k}$ define on $H^{n}(\mathfrak{X}, \mathcal{F})$ a $\mathfrak{J}$-good
filtration $(0_{III}, 13.7.7)$; finally, the canonical homomorphism*

```text
  H^n(𝔛, ℱ) → lim_← H^n(𝔛, ℱ_k)                                              (3.4.4.2)
                k
```

*is a topological isomorphism for every $n$ (the left-hand side being equipped with the $\mathfrak{J}$-adic topology,
the $H^{n}(\mathfrak{X}, \mathcal{F}_{k})$ with the discrete topology).*

**Proof.** Set

```text
  S = gr(A) = ⊕_{k ≥ 0} 𝔍^k / 𝔍^{k+1},   ℳ = gr(ℱ) = ⊕_{k ≥ 0} 𝔍^k ℱ / 𝔍^{k+1} ℱ. (3.4.4.3)
```

We know that $\mathfrak{J}^{\Delta}$ is a sheaf of ideals of definition of $\mathfrak{Y}$ `(I, 10.3.1)`; let
$\mathcal{K} = f^{*}(\mathfrak{J}^{\Delta}) \mathcal{O}_{\mathfrak{X}}$, $X_{0} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}} / \mathcal{K})$, $Y_{0} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / \mathfrak{J}^{\Delta})
= \operatorname{Spec}(A_{0})$ with $A_{0} = A / \mathfrak{J}$. It is clear that the $\mathcal{M}_{k} = \mathfrak{J}^{k}
\mathcal{F} / \mathfrak{J}^{k+1} \mathcal{F}$ are coherent $\mathcal{O}_{X_{0}}$-modules `(I, 10.11.3)`. On the other
hand, consider the quasi-coherent graded $\mathcal{O}_{X_{0}}$-algebra

```text
  𝒮 = 𝒪_{X_0} ⊗_{A_0} S = gr(𝒪_𝔛) = ⊕_{k ≥ 0} 𝒦^k / 𝒦^{k+1}.                  (3.4.4.4)
```

The hypothesis that $\mathcal{F}$ is an $\mathcal{O}_{\mathfrak{X}}$-module of finite type implies first that
$\mathcal{M}$ is

<!-- original page 121 -->

a graded $\mathcal{S}$-module *of finite type*. Indeed, the question is local on $\mathfrak{X}$, and we may therefore
suppose, in order to treat it, that $\mathfrak{X} = Spf(B)$, where $B$ is an adic Noetherian ring, and $\mathcal{F} =
N^{\Delta}$, where $N$ is a $B$-module of finite type `(I, 10.10.5)`; we have in addition $X_{0} =
\operatorname{Spec}(B_{0})$ where $B_{0} = B / \mathfrak{J} B$, and the quasi-coherent $\mathcal{O}_{X_{0}}$-modules
$\mathcal{S}$ and $\mathcal{M}$ are respectively equal to $\tilde{S}'$ and $\tilde{M}'$, where $S' = \oplus_{k \geq 0}
((\mathfrak{J}^{k} / \mathfrak{J}^{k+1}) \otimes_{A_{0}} B_{0})$ and $M' = \oplus_{k \geq 0} ((\mathfrak{J}^{k} /
\mathfrak{J}^{k+1}) \otimes_{A_{0}} N_{0})$, with $N_{0} = N / \mathfrak{J} N$; we then obviously have $M' = S'
\otimes_{B_{0}} N_{0}$, and since `N_0` is a `B_0`-module of finite type, $M'$ is an $S'$-module of finite type, whence
our assertion `(I, 1.3.13)`.

Since the morphism $f_{0} : X_{0} \to Y_{0}$ is *proper* by hypothesis, we may apply (3.3.2) to $\mathcal{S}$,
$\mathcal{M}$, and the morphism $f_{0}$; taking (1.4.11) into account, we conclude that for *every $n \geq 0$*,
$\oplus_{k \geq 0} H^{n}(X_{0}, \mathcal{M}_{k})$ is a graded $S$-module *of finite type*. This proves that condition
$(F_{n})$ of $(0_{III}, 13.7.7)$ is satisfied for every $n \geq 0$, when we consider the strict projective system
$(\mathcal{F} / \mathfrak{J}^{k} \mathcal{F})_{k \geq 0}$ of sheaves of abelian groups on `X_0`, each equipped with its
natural structure of "filtered $A$-module". We may therefore apply $(0_{III}, 13.7.7)$, which proves that:

1° The projective system $(H^{n}(\mathfrak{X}, \mathcal{F}_{k}))_{k \geq 0}$ satisfies the (ML)-condition.

2° If $H'^{n} = \varprojlim H^{n}(\mathfrak{X}, \mathcal{F}_{k})$, then $H'^{n}$ is an $A$-module of finite type.

3° The filtration defined on $H'^{n}$ by the kernels of the canonical homomorphisms $H'^{n} \to H^{n}(\mathfrak{X},
\mathcal{F}_{k})$ is $\mathfrak{J}$-good.

Note on the other hand that if we set $X_{k} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{K}^{k+1})$,
$\mathcal{F}_{k}$ is a coherent $\mathcal{O}_{X_{k}}$-module `(I, 10.11.3)`, and if $U$ is an affine open set in `X_0`,
then $U$ is also an affine open set in each of the $X_{k}$ `(I, 5.1.9)`, so $H^{n}(U, \mathcal{F}_{k}) = 0$ for every
$n > 0$ and every $k$ (1.3.1) and $H^{0}(U, \mathcal{F}_{k}) \to H^{0}(U, \mathcal{F}_{h})$ is surjective for $h \leq k$
`(I, 1.3.9)`. We are therefore in the conditions of $(0_{III}, 13.3.2)$, and the application of $(0_{III}, 13.3.1)$
proves that $H'^{n}$ is canonically identified with
$H^{n}(\mathfrak{X}, \varprojlim \mathcal{F}_{k}) = H^{n}(\mathfrak{X}, \mathcal{F})$; this completes the proof of
(3.4.4).

**(3.4.5)**

<!-- label: III.3.4.5 -->

We now return to the proof of (3.4.2) and (3.4.3). We first prove these propositions in the case $\mathfrak{Y} = Spf(A)$
envisaged in (3.4.4); for this, for every $g \in A$, apply (3.4.4) to the Noetherian affine formal scheme induced on the
open set $\mathfrak{Y}_{g} = \mathfrak{D}(g)$ of $\mathfrak{Y}$, which is equal to $Spf(A_{{g}})$, and to the formal
prescheme induced by $\mathfrak{X}$ on $f^{-1}(\mathfrak{Y}_{g})$; note that $\mathfrak{Y}_{g}$ is also an affine open
set in the prescheme $Y_{k} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / (\mathfrak{J}^{\Delta})^{k+1})$, and since
$\mathcal{F}_{k}$ is a coherent $\mathcal{O}_{X_{k}}$-module, we have

```text
  H^n(f^{-1}(𝔜_g), ℱ_k) = Γ(𝔜_g, R^n f_*(ℱ_k))
```

for every $k \geq 0$ by virtue of (1.4.11). The canonical homomorphism

```text
  H^n(f^{-1}(𝔜_g), ℱ) → lim_← Γ(𝔜_g, R^n f_*(ℱ_k))
                          k
```

is an isomorphism; but we have $(0_{I}, 3.2.6)$

```text
  lim_← Γ(𝔜_g, R^n f_*(ℱ_k)) = Γ(𝔜_g, lim_← R^n f_*(ℱ_k))
    k                                   k
```

<!-- original page 122 -->

and as the sheaf $R^{n} f_{*}(\mathcal{F})$ is the sheaf associated to the presheaf $\mathfrak{Y}_{g} \mapsto
H^{n}(f^{-1}(\mathfrak{Y}_{g}), \mathcal{F})$ on the $\mathfrak{Y}_{g}$ $(0_{I}, 3.2.1)$, we have indeed shown that the
homomorphism (3.4.2.2) is *bijective*. Let us next prove that $R^{n} f_{*}(\mathcal{F})$ is a coherent
$\mathcal{O}_{\mathfrak{Y}}$-module, and more precisely that we have

```text
  R^n f_*(ℱ) = (H^n(𝔛, ℱ))^Δ.                                                (3.4.5.1)
```

With the preceding notation, we have, since $\mathcal{F}_{k}$ is a coherent $\mathcal{O}_{X_{k}}$-module (1.4.13),

```text
  Γ(𝔜_g, R^n f_*(ℱ_k)) = (Γ(𝔜, R^n f_*(ℱ_k)))_g = (H^n(𝔛, ℱ_k))_g.
```

Now, the $H^{n}(\mathfrak{X}, \mathcal{F}_{k})$ form a projective system satisfying (ML), and their projective limit
$H^{n}(\mathfrak{X}, \mathcal{F})$ is an $A$-module of finite type. We conclude $(0_{III}, 13.7.8)$ that we have

```text
  lim_← ((H^n(𝔛, ℱ_k))_g) = H^n(𝔛, ℱ) ⊗_A A_{{g}} = Γ(𝔜_g, (H^n(𝔛, ℱ))^Δ),
    k
```

taking `(I, 10.10.8)` applied to $A$ and $A_{{g}}$ into account; this proves (3.4.5.1) since $\Gamma(\mathfrak{Y}_{g},
R^{n} f_{*}(\mathcal{F})) = \varprojlim \Gamma(\mathfrak{Y}_{g}, R^{n} f_{*}(\mathcal{F}_{k}))$.

As (3.4.2.2) is then an isomorphism of coherent $\mathcal{O}_{\mathfrak{Y}}$-modules, it is necessarily a *topological*
isomorphism `(I, 10.11.6)`. Finally, it follows from the relations $R^{n} f_{*}(\mathcal{F}_{k}) = (H^{n}(X,
\mathcal{F}_{k}))^{\Delta}$ that the projective system $(R^{n} f_{*}(\mathcal{F}_{k}))_{k \geq 0}$ satisfies (ML)
`(I, 10.10.2)`.

Once (3.4.2) and (3.4.3) are proved in the case where the formal prescheme $\mathfrak{Y}$ is affine Noetherian, it is
immediate to pass from there to the general case for (3.4.2) and the first assertion of (3.4.3), which are local on
$\mathfrak{Y}$. As for the second assertion of (3.4.3), it suffices, $\mathfrak{Y}$ being Noetherian, to cover it by a
finite number of Noetherian affine open sets $U_{i}$ and to remark that the restrictions of the projective system
$(R^{q} f_{*}(\mathcal{F}_{k}))$ to each of the $U_{i}$ satisfy (ML).

We have moreover proved along the way:

**Corollary (3.4.6).**

<!-- label: III.3.4.6 -->

*Under the hypotheses of (3.4.4), the canonical homomorphism*

```text
  H^q(𝔛, ℱ) → Γ(𝔜, R^q f_*(ℱ))                                               (3.4.6.1)
```

*is bijective.*
