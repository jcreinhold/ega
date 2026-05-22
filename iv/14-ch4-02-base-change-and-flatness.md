<!-- original page 5 -->

# Chapter IV (continued)

## §2. Base change and flatness

This section (unlike §6) appeals only exceptionally to Noetherian techniques. Nos. 1 and 2 are scarcely more than
translations of elementary properties of flatness from commutative algebra (cf. Bourbaki, _Alg. comm._, chap. I) and are
included here for the convenience of references. The following numbers are devoted above all to "descent" properties
along flat or faithfully flat morphisms: if $g : Y' \to Y$ is such a morphism, the issue is to be able to assert that a
part of $Y$, or an $\mathcal{O}_{Y}$-Module, or a morphism $X \to Y$, has a certain property, when one knows that its
inverse image under $g$ has that property. We restrict ourselves here to properties that do not appeal to the general
technique of "descent", which will be developed in Chapter V.

### 2.1. Flat modules on preschemes

**(2.1.1)**

<!-- label: IV.2.1.1 -->

Let $f : X \to Y$ be a morphism of preschemes and $\mathcal{F}$ an $\mathcal{O}_{X}$-Module; recall $(0_{I}, 6.7.1)$
that $\mathcal{F}$ is said to be **$f$-flat** (or **$Y$-flat**) **at a point $x \in X$** if $\mathcal{F}_{x}$ is a flat
$\mathcal{O}_{f(x)}$-module, **$f$-flat** (or **$Y$-flat**) if it is $f$-flat at every $x \in X$, and finally that the
morphism $f$ is said to be **flat at the point $x \in X$** (resp. **flat**) if $\mathcal{O}_{X}$ is $f$-flat at $x$
(resp. $f$-flat). When $f = 1_{X}$, one says simply that an $\mathcal{O}_{X}$-Module $\mathcal{F}$ is **flat at the
point $x$** (resp. **flat**) if it is $X$-flat at this point (resp. at every point $x \in X$), that is, if
$\mathcal{F}_{x}$ is a flat $\mathcal{O}_{x}$-module (resp. if this holds for every $x \in X$). Recall that we have
proved `(III, 1.4.15.1)` the following property:

**Proposition (2.1.2).**

<!-- label: IV.2.1.2 -->

*Let $A$, $B$ be two rings, $\phi : A \to B$ a ring homomorphism, $X = \operatorname{Spec}(B)$, $Y =
\operatorname{Spec}(A)$, $f : X \to Y$ the morphism corresponding to $\phi$, $M$ a $B$-module. For $\mathcal{F} =
\tilde{M}$ to be $f$-flat, it is necessary and sufficient that $M$ be a flat $A$-module.*

<!-- original page 6 -->

**Proposition (2.1.3).**

<!-- label: IV.2.1.3 -->

*Let $f : X \to Y$ be a morphism of preschemes, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. The following
conditions are equivalent:*

*a) For every base change $g : Y' \to Y$, if one sets $X' = X \times_{Y} Y'$, the functor $\mathcal{F}' \mapsto
\mathcal{F} \otimes_{Y} \mathcal{F}'$ from the category of quasi-coherent $\mathcal{O}_{Y'}$-Modules to that of
quasi-coherent $\mathcal{O}_{X'}$-Modules is exact.*

*a') Condition a) is satisfied for all canonical morphisms $g : \operatorname{Spec}(\mathcal{O}_{y}) \to Y$
`(I, 2.4.1)`, where $y$ runs over $Y$.*

*b) $\mathcal{F}$ is $f$-flat.*

The questions being local on $X$ and $Y$, one may restrict to the case where $Y = \operatorname{Spec}(B)$, $X =
\operatorname{Spec}(A)$, $\mathcal{F} = \tilde{M}$, where $M$ is an $A$-module. It is clear that a) entails a');
condition a') entails that for every $x \in X$ the functor $N \mapsto M_{\mathfrak{n}} \otimes_{B_{\mathfrak{n}}} N$ is
exact in the category of $B_{\mathfrak{n}}$-modules, $\mathfrak{n}$ being the ideal $\mathfrak{j}_{f(x)}$ of $B$; this
means that $M_{\mathfrak{n}}$ is a flat $B_{\mathfrak{n}}$-module, and it results from $(0_{I}, 6.3.3)$ and from
`(2.1.2)` that $\mathcal{F}$ is $f$-flat. Finally, to see that b) entails a), one may also restrict to the case where
$Y' = \operatorname{Spec}(A')$ is affine and $\mathcal{F}' = \tilde{N}'$, where $N'$ is an $A'$-module; the conclusion
then again follows from `(2.1.2)` and the definition of flatness, since $(M \otimes_{A} N')~ = \mathcal{F} \otimes_{Y}
\mathcal{F}'$.

**Proposition (2.1.4).**

<!-- label: IV.2.1.4 -->

*Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms of preschemes, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module; set $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, $\mathcal{F}' = \mathcal{F}
\otimes_{Y} \mathcal{O}_{Y'}$, and let $g'$ be the canonical projection $X' \to X$. Let $x'$ be a point of $X'$, $x =
g'(x')$, $y' = f'(x')$, $y = f(x) = g(y')$. If $\mathcal{F}$ is $f$-flat at the point $x$, then $\mathcal{F}'$ is
$f'$-flat at the point $x'$; in particular if $\mathcal{F}$ is $f$-flat, $\mathcal{F}'$ is $f'$-flat; if $f$ is flat,
$f'$ is flat.*

It suffices to prove the first assertion; applying `(I, 3.6.5)` three times, as well as `(I, 2.4.4)`, one may reduce to
the case where $Y = \operatorname{Spec}(\mathcal{O}_{y})$, $X = \operatorname{Spec}(\mathcal{O}_{x})$, $Y' =
\operatorname{Spec}(\mathcal{O}_{y'})$, $\mathcal{F} = \tilde{M}$, where $M = \mathcal{F}_{x}$; the hypothesis and
`(2.1.2)` then entail that $\mathcal{F}$ is $f$-flat — in other words one is reduced to proving a particular case of the
second assertion, and this last follows at once from `(2.1.3)`.

**Proposition (2.1.5).**

<!-- label: IV.2.1.5 -->

*Consider a commutative diagram of morphisms of preschemes*

```text
  X  ←─g'──  X'
  │           │
  f│         │f'
  ↓           ↓
  Y  ←──g──  Y'
              │
              │h
              ↓
              Z
```

*where $X' = X \times_{Y} Y'$ and $f' = f_{(Y')}$. Let $x'$ be a point of $X'$, and set $x = g'(x')$, $y' = f'(x')$, $y
= f(x) = g(y')$, $z = h(y')$. Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module that is $f$-flat at the
point $x$ (resp. $f$-flat), and $\mathcal{G}'$ a quasi-coherent $\mathcal{O}_{Y'}$-Module that is $h$-flat at the point
$y'$ (resp. $h$-flat); then $\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G}'$ is a quasi-coherent
$\mathcal{O}_{X'}$-Module that is $(h \circ f')$-flat at the point $x'$ (resp. $(h \circ f')$-flat).*

As in `(2.1.4)`, one reduces to the case where $X = \operatorname{Spec}(\mathcal{O}_{x})$, $Y =
\operatorname{Spec}(\mathcal{O}_{y})$,

<!-- original page 7 -->

$Y' = \operatorname{Spec}(\mathcal{O}_{y'})$ and $Z = \operatorname{Spec}(\mathcal{O}_{z})$, and it then suffices to
prove that $\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G}'$ is $(h \circ f')$-flat. Taking `(2.1.2)` into account,
the proposition follows from Bourbaki, _Alg. comm._, chap. I, §2, n° 7, prop. 8.

**Corollary (2.1.6).**

<!-- label: IV.2.1.6 -->

*Let $f : X \to Y$, $g : Y \to Z$ be two morphisms of preschemes, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module. If
$\mathcal{F}$ is $f$-flat at the point $x \in X$ and $g$ is flat at the point $f(x)$, then $\mathcal{F}$ is $(g \circ
f)$-flat at the point $x$. In particular, if $f$ and $g$ are flat morphisms, so is $g \circ f$.*

This is the particular case of `(2.1.5)` with $Y' = Y$, $\mathcal{G}' = \mathcal{O}_{Y'}$.

**Corollary (2.1.7).**

<!-- label: IV.2.1.7 -->

*If $f : X \to X'$, $g : Y \to Y'$ are two flat $S$-morphisms, then $f \times_{S} g : X \times_{S} Y \to X' \times_{S}
Y'$ is a flat morphism.*

This follows from `(2.1.4)` and `(2.1.6)` (cf. `(I, 3.5.1)`).

**Proposition (2.1.8).**

<!-- label: IV.2.1.8 -->

*Let $f : X \to Y$ be a morphism of preschemes,*

$$ 0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0 $$

*an exact sequence of quasi-coherent $\mathcal{O}_{X}$-Modules such that $\mathcal{F}''$ is $Y$-flat.*

*(i) For every morphism $g : Y' \to Y$ and every quasi-coherent $\mathcal{O}_{Y'}$-Module $\mathcal{G}'$, the sequence*

```text
  0 → ℱ' ⊗_Y 𝒢' → ℱ ⊗_Y 𝒢' → ℱ'' ⊗_Y 𝒢' → 0
```

*of $\mathcal{O}_{X'}$-Modules (where $X' = X \times_{Y} Y'$) is exact.*

*(ii) For $\mathcal{F}$ to be $Y$-flat, it is necessary and sufficient that $\mathcal{F}'$ be so.*

One may obviously suppose $X$, $Y$, $Y'$ affine; the conclusion then follows from `(2.1.2)` and $(0_{I}, 6.1.2)$.

**Corollary (2.1.9).**

<!-- label: IV.2.1.9 -->

*Let $\mathcal{L}^{\bullet}$ be a complex of quasi-coherent $\mathcal{O}_{X}$-Modules, $i$ an index such that if one
denotes by $d^{i} : \mathcal{L}^{i} \to \mathcal{L}^{i+1}$ the differential, $\mathcal{B}^{i+1}(\mathcal{L}^{\bullet}) =
Im(d^{i})$ and $\mathcal{Z}^{i+1}(\mathcal{L}^{\bullet}) = Coker(d^{i})$ are $Y$-flat. Then, with the notations of
`(2.1.8)`, the canonical homomorphism*

```text
  ℋ^i(ℒ^•) ⊗_Y 𝒢' → ℋ^i(ℒ^• ⊗_Y 𝒢')
```

*is bijective.*

Since the tensor product is right exact, one has

```text
  𝒵^{i+1}(ℒ^•) ⊗_Y 𝒢' = Coker(d^i ⊗ 1) = 𝒵^{i+1}(ℒ^• ⊗_Y 𝒢')
```

and $\mathcal{Z}^{'i}(\mathcal{L}^{\bullet}) \otimes_{Y} \mathcal{G}' = \mathcal{Z}^{'i}(\mathcal{L}^{\bullet}
\otimes_{Y} \mathcal{G}')$. Moreover, in the exact sequence

$$ 0 \to \mathcal{B}^{i+1}(\mathcal{L}^{\bullet}) \to \mathcal{L}^{i+1} \to \mathcal{Z}^{i+1}(\mathcal{L}^{\bullet}) \to
0 $$

$\mathcal{Z}^{i+1}(\mathcal{L}^{\bullet})$ is $Y$-flat, so it follows from `(2.1.8, (i))` that one has the exact
sequence

```text
  0 → ℬ^{i+1}(ℒ^•) ⊗_Y 𝒢' → ℒ^{i+1} ⊗_Y 𝒢' → 𝒵^{i+1}(ℒ^• ⊗_Y 𝒢') → 0
```

whence $\mathcal{B}^{i+1}(\mathcal{L}^{\bullet}) \otimes_{Y} \mathcal{G}' = Im(d^{i} \otimes 1) =
\mathcal{B}^{i+1}(\mathcal{L}^{\bullet} \otimes_{Y} \mathcal{G}')$. Then, in the exact sequence

$$ 0 \to \mathcal{H}^{i}(\mathcal{L}^{\bullet}) \to \mathcal{Z}^{i}(\mathcal{L}^{\bullet}) \to
\mathcal{B}^{i+1}(\mathcal{L}^{\bullet}) \to 0 $$

$\mathcal{B}^{i+1}(\mathcal{L}^{\bullet})$ is $Y$-flat, so it follows from `(2.1.8, (i))` and what precedes that one has
the exact sequence

```text
  0 → ℋ^i(ℒ^•) ⊗_Y 𝒢' → 𝒵^i(ℒ^• ⊗_Y 𝒢') → ℬ^{i+1}(ℒ^• ⊗_Y 𝒢') → 0
```

which proves the corollary.

<!-- original page 8 -->

**Corollary (2.1.10).**

<!-- label: IV.2.1.10 -->

*Let $f : X \to Y$ be a morphism of preschemes, $\mathcal{F}$ a quasi-coherent and $Y$-flat $\mathcal{O}_{X}$-Module,
$\mathcal{L}_{\bullet} = (\mathcal{L}_{i})$ a left resolution of $\mathcal{F}$ formed of quasi-coherent and $Y$-flat
$\mathcal{O}_{X}$-Modules. Then, for every morphism $g : Y' \to Y$ and every quasi-coherent $\mathcal{O}_{Y'}$-Module
$\mathcal{G}'$, the complex $\mathcal{L}_{\bullet} \otimes_{Y} \mathcal{G}' = (\mathcal{L}_{i} \otimes_{Y}
\mathcal{G}')_{i \geq 0}$ is a left resolution of $\mathcal{F} \otimes_{Y} \mathcal{G}'$.*

*Moreover, if $\mathcal{Z}_{i}(\mathcal{L}_{\bullet}) = Ker(\mathcal{L}_{i} \to \mathcal{L}_{i-1})$, the
$\mathcal{Z}_{i}(\mathcal{L}_{\bullet})$ are $Y$-flat, and one has*

```text
  𝒵_i(ℒ_•) ⊗_Y 𝒢' = 𝒵_i(ℒ_• ⊗_Y 𝒢') = Ker(ℒ_i ⊗_Y 𝒢' → ℒ_{i−1} ⊗_Y 𝒢').
```

Set $\mathcal{R}_{i} = Im(\mathcal{L}_{i+1} \to \mathcal{L}_{i}) = \mathcal{Z}_{i}(\mathcal{L}_{\bullet})$; one then has
the exact sequences

```text
  0 ← ℱ ← ℒ_0 ← ℛ_0 ← 0
  ⋮
  0 ← ℛ_i ← ℒ_{i+1} ← ℛ_{i+1} ← 0
  ⋮
```

and since $\mathcal{F}$ and the $\mathcal{L}_{i}$ are $Y$-flat, one deduces from `(2.1.8, (ii))` by induction that all
the $\mathcal{R}_{i}$ are also $Y$-flat; using `(2.1.8, (i))`, one therefore has the exact sequences

```text
  0 ← ℱ ⊗_Y 𝒢' ← ℒ_0 ⊗_Y 𝒢' ← ℛ_0 ⊗_Y 𝒢' ← 0
  0 ← ℛ_i ⊗_Y 𝒢' ← ℒ_{i+1} ⊗_Y 𝒢' ← ℛ_{i+1} ⊗_Y 𝒢' ← 0          (i ≥ 0)
```

which prove the corollary.

**Proposition (2.1.11).**

<!-- label: IV.2.1.11 -->

*Let $f : X \to Y$ be a flat morphism, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{Y}$-Module of finite presentation.
If $\mathcal{J}$ is the Ideal of $\mathcal{O}_{Y}$ annihilator of $\mathcal{F}$, then $f*(\mathcal{J})$ is the Ideal of
$\mathcal{O}_{X}$ annihilator of $f*(\mathcal{F})$.*

One has by definition an exact sequence $(0_{I}, 5.3.7)$

```text
  0 → 𝒥 → 𝒪_Y → ℋom_{𝒪_Y}(ℱ, ℱ)
```

whence, since $f$ is flat, an exact sequence

```text
  0 → f*(𝒥) → 𝒪_X → f*(ℋom_{𝒪_Y}(ℱ, ℱ))
```

and since by hypothesis $\mathcal{F}$ is an $\mathcal{O}_{Y}$-Module of finite presentation,
$f*(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{F}))$ is canonically identified with
$\mathcal{H}om_{\mathcal{O}_{X}}(f*(\mathcal{F}), f*(\mathcal{F}))$ $(0_{I}, 6.7.6)$, whence the conclusion.

**Proposition (2.1.12).**

<!-- label: IV.2.1.12 -->

*Let $X$ be a prescheme, $\mathcal{F}$ an $\mathcal{O}_{X}$-Module of finite presentation, $x$ a point of $X$. The
following conditions are equivalent:*

*a) $\mathcal{F}_{x}$ is a flat $\mathcal{O}_{x}$-module.*

*b) There exists an open neighbourhood $U$ of $x$ such that $\mathcal{F}|U$ is a locally free
$(\mathcal{O}_{X}|U)$-Module.*

Indeed, $\mathcal{F}_{x}$ is an $\mathcal{O}_{x}$-module of finite presentation and $\mathcal{O}_{x}$ a local ring; it
therefore amounts to the same to say that $\mathcal{F}_{x}$ is a flat $\mathcal{O}_{x}$-module or a free
$\mathcal{O}_{x}$-module (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. 2 of prop. 5); whence the conclusion, taking
account of $(0_{I}, 5.2.7)$. We note that the proposition is valid for an arbitrary ringed space in local rings.

**Proposition (2.1.13).**

<!-- label: IV.2.1.13 -->

\*Let $f : X \to Y$ be a morphism of preschemes. If $f$ is flat at a point $x \in X$ and the ring $\mathcal{O}_{x}$ is
reduced (resp. integral and integrally closed), then the ring $\mathcal{O}_{f(x)}$

<!-- original page 9 -->

is reduced (resp. integral and integrally closed). If $f$ is faithfully flat and $X$ is reduced (resp. normal), then $Y$
is reduced (resp. normal).\*

Set $\mathcal{O}_{f(x)} = A$, $\mathcal{O}_{x} = B$. If $B$ is a flat $A$-module, it is also a faithfully flat
$A$-module $(0_{I}, 6.6.2)$, so $A$ is identified with a subring of $B$; if $B$ is reduced, so therefore is $A$. Suppose
now that $B$ is integral and integrally closed, and let $L$ be its field of fractions; then $A \subset B$ is integral;
denote by $K \subset L$ its field of fractions. The hypothesis entails that $B \cap K = A$ (Bourbaki, _Alg. comm._,
chap. I, §3, n° 5, prop. 10). If then $t \in K$ is integral over $A$, it is also integral over $B$, hence belongs to $B$
by hypothesis, and consequently $t \in A$, which proves that $A$ is integrally closed.

**Proposition (2.1.14).**

<!-- label: IV.2.1.14 -->

*Let $f : X \to Y$ be a faithfully flat morphism. If $X$ is locally integral and the space underlying $Y$ is locally
Noetherian, then $Y$ is locally integral.*

Indeed, every $y \in Y$ is of the form $f(x)$ for some $x \in X$ and by hypothesis $\mathcal{O}_{y}$ is identified with
a subring of $\mathcal{O}_{x}$ $(0_{I}, 6.6.1)$; since $\mathcal{O}_{x}$ is integral, so is $\mathcal{O}_{y}$, and this
proves the proposition `(I, 5.1.4)`.

### 2.2. Faithfully flat modules on preschemes

**Proposition (2.2.1).**

<!-- label: IV.2.2.1 -->

*Let $f : X \to Y$ be a morphism of preschemes, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module. The following
conditions are equivalent:*

*a) For every base change $g : Y' \to Y$, if one sets $X' = X \times_{Y} Y'$, the functor $\mathcal{G}' \mapsto
\mathcal{F} \otimes_{Y} \mathcal{G}'$ from the category of quasi-coherent $\mathcal{O}_{Y'}$-Modules to that of
quasi-coherent $\mathcal{O}_{X'}$-Modules is exact and faithful.*

*a') Condition a) is satisfied for all canonical morphisms $g : \operatorname{Spec}(\mathcal{O}_{y}) \to Y$
`(I, 2.4.1)`, where $y$ runs over $Y$.*

*a'') Condition a) is satisfied for all canonical immersions $Y' \to Y$, where $Y'$ runs over the set of affine open
subschemes of $Y$.*

*b) $\mathcal{F}$ is $Y$-flat and, for every $y \in Y$, if one denotes by $X_{y}$ the fibre $f^{-1}(y)$, the
$\mathcal{O}_{X_{y}}$-Module $\mathcal{F}_{y} = \mathcal{F} \otimes_{Y} k(y)$ is $\neq 0$.*

It is clear that a) implies a') and a''); condition a') first implies that $\mathcal{F}$ is $Y$-flat `(2.1.3)`; on the
other hand it implies that for every $y \in Y$ the functor $N \mapsto \mathcal{F}_{y} \otimes_{\mathcal{O}_{y}}
\tilde{N}$ is faithful in the category of $\mathcal{O}_{y}$-modules; taking in particular $N = k(y)$, one obtains the
second assertion of b). To show that b) implies a), one may restrict to the case where $Y$ is affine, the question being
local on $Y$. Similarly, to prove that a'') implies a), one is reduced to proving that when $Y$ is affine, the fact that
$\mathcal{G}' \mapsto \mathcal{F} \otimes_{Y} \mathcal{G}'$ is an exact and faithful functor entails condition a). In
other words, one is reduced to proving the following more precise proposition:

**Proposition (2.2.2).**

<!-- label: IV.2.2.2 -->

*Let $Y = \operatorname{Spec}(A)$ be an affine scheme, $f : X \to Y$ a morphism of preschemes, $\mathcal{F}$ a
quasi-coherent $\mathcal{O}_{X}$-Module. Condition a) of `(2.2.1)` is equivalent to each of the following:*

*b') $\mathcal{F}$ is $Y$-flat and, for every closed point $y$ of $Y$, one has $\mathcal{F}_{y} \neq 0$.*

<!-- original page 10 -->

*c) The functor $\mathcal{G} \mapsto \mathcal{F} \otimes_{Y} \mathcal{G}$ from the category of quasi-coherent
$\mathcal{O}_{Y}$-Modules to that of quasi-coherent $\mathcal{O}_{X}$-Modules is exact and faithful.*

If b') is satisfied, there is at least one $x \in f^{-1}(y)$ such that $(\mathcal{F}_{y})_{x} \neq 0$; let $U =
\operatorname{Spec}(B)$ be an affine open neighbourhood of $x$, and let $\mathcal{F}|U = \tilde{M}$, where $M$ is a
$B$-module. Then b') implies that $M/\mathfrak{j}_{y} M \neq 0$, and consequently (since $M$ is a flat $A$-module by
`(2.1.2)`) that $M \otimes_{A} A_{y}$ is a faithfully flat $A_{y}$-module $(0_{I}, 6.4.5)$. The relation $(\mathcal{F}
\otimes_{Y} \mathcal{G}) \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{y} = 0$ for a closed point $y$ of $Y$ implies
$(\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{U})_{x} \otimes_{\mathcal{O}_{y}} \mathcal{G}_{y} = 0$, hence
$\mathcal{G}_{y} = 0$. But if $\mathcal{G}_{y} = 0$ for every closed point $y$ of $Y$, one concludes that $\mathcal{G} =
0$; indeed, if $\mathcal{G} = \tilde{N}$, the annihilator of an element of $N$ is contained in no maximal ideal of $A$,
so it equals all of $A$. The relation $\mathcal{F} \otimes_{Y} \mathcal{G} = 0$ therefore implies $\mathcal{G} = 0$; in
other words, the functor $\mathcal{G} \mapsto \mathcal{F} \otimes_{Y} \mathcal{G}$ is faithful; we know moreover that
this functor is exact `(2.1.3)`, which shows that b') entails c).

Finally, to see that c) entails a), one may restrict to the case where $Y'$ is also affine; as $g : Y' \to Y$ is then an
affine morphism, so is the projection $g' : X' \to X$ `(II, 1.5.5)`; in addition, the functor $\mathcal{H} \mapsto
g'_{*}(\mathcal{H})$ is then exact in the category of quasi-coherent $\mathcal{O}_{X'}$-Modules `(I, 1.6.4)`, and if
$g'_{*}(\mathcal{H}) = \mathcal{H}$, one has $\mathcal{H}' = \tilde{\mathcal{H}}$, so the preceding functor is also
faithful; to see that $\mathcal{G}' \mapsto \mathcal{F} \otimes_{Y} \mathcal{G}'$ is exact and faithful, it therefore
suffices to see that the functor $\mathcal{G}' \mapsto g'_{*}(\mathcal{F} \otimes_{Y} \mathcal{G}')$ is. Now, if $f' =
f_{(Y')} : X' \to Y'$, one has $g'_{*}(\mathcal{F} \otimes_{Y} \mathcal{G}') = g'_{*}(g'*(\mathcal{F})
\otimes_{\mathcal{O}_{X'}} f'*(\mathcal{G}'))$; the fact that $g$ is affine entails that one has a canonical isomorphism

```text
  ℱ ⊗_{𝒪_X} f*(g_*(𝒢')) ⥲ g'_*(g'*(ℱ) ⊗_{𝒪_{X'}} f'*(𝒢')).            (2.2.2.1)
```

Indeed, one knows `(II, 1.5.2)` that one has a canonical isomorphism

$$ f*(g_{*}(\mathcal{G}')) \xrightarrow{\sim} g'_{*}(f'*(\mathcal{G}')), $$

and on the other hand one has a canonical homomorphism $\mathcal{F} \to g'_{*}(g'*(\mathcal{F}))$ $(0_{I}, 4.4.3.2)$;
composing the homomorphism $\mathcal{F} \otimes_{\mathcal{O}_{X}} f*(g_{*}(\mathcal{G}')) \to g'_{*}(g'*(\mathcal{F}))
\otimes_{\mathcal{O}_{X}} g'_{*}(f'*(\mathcal{G}'))$ with the canonical homomorphism $(0_{I}, 4.2.2.1)$, one deduces the
homomorphism `(2.2.2.1)`; the verification that it is an isomorphism is immediate by reducing to the case where $X$ is
affine. This being so, the functor $\mathcal{G}' \mapsto g_{*}(\mathcal{G}')$ is exact and faithful and by hypothesis so
is $\mathcal{G} \mapsto \mathcal{F} \otimes_{Y} \mathcal{G} = \mathcal{F} \otimes_{\mathcal{O}_{X}} f*(\mathcal{G})$;
their composite is therefore exact and faithful, which completes the proof of `(2.2.1)` and `(2.2.2)`.

**Corollary (2.2.3).**

<!-- label: IV.2.2.3 -->

*Let $X = \operatorname{Spec}(B)$, $Y = \operatorname{Spec}(A)$ be two affine schemes, $f : X \to Y$ a morphism,
$\mathcal{F} = \tilde{M}$ a quasi-coherent $\mathcal{O}_{X}$-Module. For $\mathcal{F}$ to satisfy the equivalent
conditions of `(2.2.1)` (or `(2.2.2)`), it is necessary and sufficient that the $A$-module $M$ be faithfully flat.*

Indeed, condition c) of `(2.2.2)` then means that the functor $N \mapsto M \otimes_{A} N$ from the category of
$A$-modules to that of $B$-modules is exact and faithful, and the conclusion follows from $(0_{I}, 6.4.1)$.

**Definition (2.2.4).**

<!-- label: IV.2.2.4 -->

*When the equivalent conditions of `(2.2.1)` are satisfied, one says that the quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ is **faithfully flat relative to $f$** (or **to $Y$**).*

<!-- original page 11 -->

One notes that this notion is local on $Y$, but *not* on $X$; in particular one can have $\mathcal{F}_{x} = 0$ for
certain $x \in X$, in other words $Supp(\mathcal{F})$ is not necessarily equal to $X$. Nevertheless, it follows at once
from criterion `(2.2.1, b)` that for every $y \in Y$ there exists at least one $x \in f^{-1}(y)$ such that
$(\mathcal{F}_{y})_{x} = \mathcal{F}_{x} \otimes_{\mathcal{O}_{y}} k(y) \neq 0$, and *a fortiori* $\mathcal{F}_{x} \neq
0$; in other words:

**Corollary (2.2.5).**

<!-- label: IV.2.2.5 -->

*If $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module, faithfully flat relative to $f$, one has
$f(Supp(\mathcal{F})) = Y$, and a fortiori $f$ is a surjective morphism.*

This result admits a partial converse:

**Corollary (2.2.6).**

<!-- label: IV.2.2.6 -->

*Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module of finite type. For $\mathcal{F}$ to be faithfully flat
relative to $f$, it is necessary and sufficient that $\mathcal{F}$ be $f$-flat and that $f(Supp(\mathcal{F})) = Y$.*

Indeed `(I, 9.1.13 and 3.6.1)` one has $Supp(\mathcal{F}_{y}) = f^{-1}(y) \cap Supp(\mathcal{F})$, so in this case
criterion `(2.2.1, b)` is none other than the condition of the corollary.

In particular, the $\mathcal{O}_{X}$-Module $\mathcal{O}_{X}$ is faithfully flat relative to $f$ if and only if it is
$f$-flat and $f$ is surjective, in other words if and only if the morphism $f$ is **faithfully flat** $(0_{I}, 6.7.8)$.

Let us make explicit the properties involved in definition `(2.2.4)`:

**Proposition (2.2.7).**

<!-- label: IV.2.2.7 -->

*Let $f : X \to Y$ be a morphism of preschemes, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module faithfully flat
relative to $f$. Then, for a sequence $\mathcal{G}' \to \mathcal{G} \to \mathcal{G}''$ of quasi-coherent
$\mathcal{O}_{Y}$-Modules to be exact, it is necessary and sufficient that the corresponding sequence $\mathcal{F}
\otimes_{Y} \mathcal{G}' \to \mathcal{F} \otimes_{Y} \mathcal{G} \to \mathcal{F} \otimes_{Y} \mathcal{G}''$ be so. In
particular, for a homomorphism $u : \mathcal{G} \to \mathcal{G}'$ of quasi-coherent $\mathcal{O}_{Y}$-Modules to be
injective (resp. surjective, bijective, zero), it is necessary and sufficient that $1_{\mathcal{F}} \otimes f*(u) :
\mathcal{F} \otimes_{Y} \mathcal{G} \to \mathcal{F} \otimes_{Y} \mathcal{G}'$ be so. For a quasi-coherent
$\mathcal{O}_{Y}$-Module $\mathcal{G}$ to be zero, it is necessary and sufficient that $\mathcal{F} \otimes_{Y}
\mathcal{G} = 0$. For every quasi-coherent $\mathcal{O}_{Y}$-Module $\mathcal{G}$, the map $\mathcal{G}' \mapsto
\mathcal{F} \otimes_{Y} \mathcal{G}'$ from the set of quasi-coherent sub-$\mathcal{O}_{Y}$-Modules of $\mathcal{G}$ to
the set of quasi-coherent sub-$\mathcal{O}_{X}$-Modules of $\mathcal{F} \otimes_{Y} \mathcal{G}$ is injective.*

To prove the last assertion — that is, that for two quasi-coherent sub-$\mathcal{O}_{Y}$-Modules $\mathcal{G}'$,
$\mathcal{G}''$ of $\mathcal{G}$, the relation $\mathcal{F} \otimes_{Y} \mathcal{G}' = \mathcal{F} \otimes_{Y}
\mathcal{G}''$ entails $\mathcal{G}' = \mathcal{G}''$ — one may (replacing $\mathcal{G}''$ by $\mathcal{G}' +
\mathcal{G}''$) reduce to the case where $\mathcal{G}' \subset \mathcal{G}''$, and it then suffices to apply the second
assertion of the statement to the injection $u : \mathcal{G}' \to \mathcal{G}''$.

**Corollary (2.2.8).**

<!-- label: IV.2.2.8 -->

*Let $f : X \to Y$ be a faithfully flat morphism. For every quasi-coherent $\mathcal{O}_{Y}$-Module $\mathcal{G}$, the
canonical map*

```text
  Γ(Y, 𝒢) → Γ(X, f*(𝒢))                                       (2.2.8.1)
```

*is injective.*

Indeed, $\Gamma(Y, \mathcal{G})$ is canonically identified with $\operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{O}_{Y},
\mathcal{G})$ $(0_{I}, 5.1.1)$ and likewise $\Gamma(X, f*(\mathcal{G}))$ with
$\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{O}_{X}, f*(\mathcal{G}))$. By virtue of `(2.2.1)` and `(2.2.4)`, the
hypothesis entails that the functor $\mathcal{G} \mapsto f*(\mathcal{G})$ is exact and faithful in the category of
quasi-coherent $\mathcal{O}_{Y}$-Modules, and consequently a homomorphism $u : \mathcal{O}_{Y} \to \mathcal{G}$ is zero
if and only if $f*(u) : f*(\mathcal{O}_{Y}) = \mathcal{O}_{X} \to f*(\mathcal{G})$ is zero.

**Remark (2.2.9).**

<!-- label: IV.2.2.9 -->

*The results of `(2.2.7)` and `(2.2.8)` still hold when the $\mathcal{O}_{Y}$-Modules $\mathcal{G}'$, $\mathcal{G}$,
$\mathcal{G}''$ appearing there are arbitrary (not necessarily quasi-coherent). Indeed, for every $y \in Y$, there
exists $x \in f^{-1}(y)$ such that $\mathcal{F}_{x}$ is a $\mathcal{O}_{y}$-module*

<!-- original page 12 -->

*faithfully flat, and consequently the functor $\mathcal{G}_{y} \mapsto \mathcal{G}_{y} \otimes_{\mathcal{O}_{y}}
\mathcal{F}_{x}$ is faithful; since moreover for every $x \in f^{-1}(y)$ the functor $\mathcal{G}_{y} \mapsto
\mathcal{G}_{y} \otimes_{\mathcal{O}_{y}} \mathcal{F}_{x}$ is exact, one deduces the conclusion at once.*

**Proposition (2.2.10).**

<!-- label: IV.2.2.10 -->

*Let $f : X \to Y$, $g : Y' \to Y$, $h : Y' \to Z$ be three morphisms of preschemes, $X' = X \times_{Y} Y'$,
$\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, faithfully flat relative to $Y$, $\mathcal{G}'$ a
quasi-coherent $\mathcal{O}_{Y'}$-Module. For $\mathcal{G}'$ to be flat (resp. faithfully flat) relative to $Z$, it is
necessary and sufficient that $\mathcal{F} \otimes_{Y} \mathcal{G}'$ be a flat (resp. faithfully flat)
$\mathcal{O}_{X'}$-Module relative to $Z$.*

One knows already that if $\mathcal{G}'$ is $Z$-flat, then so is $\mathcal{F} \otimes_{Y} \mathcal{G}'$ `(2.1.5)`.
Consider an arbitrary base change $Z'' \to Z$ and set $X'' = X' \times_{Z} Z''$; if $\mathcal{G}'$ is faithfully flat
relative to $Z$, the functor

```text
  ℋ'' ↦ ℋ'' ⊗_Z 𝒢' → (ℋ'' ⊗_Z 𝒢') ⊗_Y ℱ = ℋ'' ⊗_Z (𝒢' ⊗_Y ℱ)        (2.2.10.1)
```

from the category of quasi-coherent $\mathcal{O}_{Z''}$-Modules to that of $\mathcal{O}_{X''}$-Modules is the composite
of two exact and faithful functors, hence is exact and faithful. Conversely, if this composite functor is exact (resp.
exact and faithful), so is $\mathcal{M}'' \mapsto \mathcal{M}'' \otimes_{Z} \mathcal{G}'$, since the functor
$\mathcal{M}' \mapsto \mathcal{M}' \otimes_{Y} \mathcal{F}$ (from the category of quasi-coherent
$\mathcal{O}_{Y'}$-Modules to that of $\mathcal{O}_{X'}$-Modules) is exact and faithful by hypothesis.

**Corollary (2.2.11).**

<!-- label: IV.2.2.11 -->

*(i) Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms, $X' = X \times_{Y} Y'$, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module. If $\mathcal{F}$ is faithfully flat relative to $Y$, then $\mathcal{F}' = \mathcal{F}
\otimes_{Y} \mathcal{O}_{Y'}$ is faithfully flat relative to $Y'$.*

*(ii) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module,
faithfully flat relative to $Y$. For $g$ to be a faithfully flat morphism, it is necessary and sufficient that
$\mathcal{F}$ be faithfully flat relative to $Z$.*

*(iii) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $\mathcal{G}$ a quasi-coherent $\mathcal{O}_{Y}$-Module.
Suppose the morphism $f$ is faithfully flat. For $\mathcal{G}$ to be flat (resp. faithfully flat) relative to $Z$, it is
necessary and sufficient that $f*(\mathcal{G})$ be flat (resp. faithfully flat) relative to $Z$.*

*(iv) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $x$ a point of $X$. Suppose $f$ is flat at the point $x$. For
$g \circ f$ to be flat at the point $x$, it is necessary and sufficient that $g$ be flat at the point $f(x)$.*

To prove (i), one applies `(2.2.10)` replacing $Z$ by $Y'$ and $\mathcal{G}'$ by $\mathcal{O}_{Y'}$. To prove (ii), one
applies `(2.2.10)` taking the identity for the morphism $Y' \to Y$ and replacing $\mathcal{G}'$ by $\mathcal{O}_{Y}$. To
prove (iii), one applies `(2.2.10)` again taking the identity for $Y' \to Y$ and replacing $\mathcal{F}$ by
$\mathcal{O}_{X}$ and $\mathcal{G}'$ by $\mathcal{G}$. Finally (iv) is deduced from (ii) by replacing $X$ by
$\operatorname{Spec}(\mathcal{O}_{x})$, $\mathcal{F}$ by $\mathcal{O}_{X}$, $Y$ by
$\operatorname{Spec}(\mathcal{O}_{f(x)})$, and $Z$ by $\operatorname{Spec}(\mathcal{O}_{g(f(x))})$, taking account of
$(0_{I}, 6.6.2)$.

**Corollary (2.2.12).**

<!-- label: IV.2.2.12 -->

*Let $Y$ be an affine scheme, $f : X \to Y$ a quasi-compact morphism, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module. If $\mathcal{F}$ is faithfully flat relative to $f$, there exists an affine scheme $X'$ and a
surjective local isomorphism $g : X' \to X$ such that $g*(\mathcal{F})$ is faithfully flat relative to $f \circ g$.*

Indeed, $X$ is quasi-compact, hence a finite union of affine open sets $X_{i}$; it suffices to take for $X'$ the affine
scheme sum of the preschemes induced on the open sets $X_{i}$, and for $g : X' \to X$ the canonical morphism; it is
clear that $g$ is faithfully flat, and

<!-- original page 13 -->

the hypothesis entails that $g*(\mathcal{F})$ is faithfully flat relative to $f \circ g$, by virtue of
`(2.2.11, (iii))`.

**Corollary (2.2.13).**

<!-- label: IV.2.2.13 -->

*(i) Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. If $f$ is
a faithfully flat morphism, so is $f'$.*

*(ii) If $f : X \to X'$, $g : Y \to Y'$ are two faithfully flat $S$-morphisms, then*

```text
  f ×_S g : X ×_S Y → X' ×_S Y'
```

*is faithfully flat.*

*(iii) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms such that $f$ is faithfully flat. For $g$ to be a flat (resp.
faithfully flat) morphism, it is necessary and sufficient that $g \circ f$ be a flat (resp. faithfully flat) morphism.*

**Proposition (2.2.14).**

<!-- label: IV.2.2.14 -->

*Let $f : X \to Y$ be a faithfully flat and quasi-compact morphism. If $X$ is locally Noetherian, so is $Y$.*

The question being local on $Y$, one may suppose $Y = \operatorname{Spec}(A)$ affine; since $f$ is quasi-compact, it
follows from `(2.2.12)` that one may also restrict to the case where $X = \operatorname{Spec}(B)$ is affine. Then $B$ is
a Noetherian ring by hypothesis, and a faithfully flat $A$-module `(2.2.3)`; hence $A$ is Noetherian $(0_{I}, 6.5.2)$.

**Proposition (2.2.15).**

<!-- label: IV.2.2.15 -->

*Let $f : X \to Y$ be a faithfully flat morphism. If $\mathfrak{S}(X)$ and $\mathfrak{S}(Y)$ denote respectively the set
of sub-preschemes of $X$ and $Y$, the map $Z \mapsto f^{-1}(Z)$ from $\mathfrak{S}(Y)$ to $\mathfrak{S}(X)$ is
injective.*

Since $f$ is surjective, one has, for the underlying set of a sub-prescheme $Z$ of $Y$, $f(f^{-1}(Z)) = Z$. On the other
hand, if $U$ is an open set of $Y$ containing $Z$ and in which $Z$ is closed, $f^{-1}(U)$ is open in $X$, $f^{-1}(Z)$ is
closed in $f^{-1}(U)$, and the restriction $f^{-1}(U) \to U$ of $f$ is a faithfully flat morphism. One may therefore
restrict to considering only closed sub-preschemes of $Y$. Now, if $Z$ is a closed sub-prescheme of $Y$ corresponding to
a quasi-coherent Ideal $\mathcal{J}$ of $\mathcal{O}_{Y}$, one knows that $f^{-1}(Z)$ corresponds to the quasi-coherent
Ideal $f*(\mathcal{J}) \mathcal{O}_{X}$ of $\mathcal{O}_{X}$ `(I, 4.4.5)`, and since $f$ is flat, $f*(\mathcal{J})
\mathcal{O}_{X}$ is identified with $f*(\mathcal{J})$. But the map $\mathcal{J} \mapsto f*(\mathcal{J})$ from the set of
quasi-coherent Ideals of $\mathcal{O}_{Y}$ to the set of quasi-coherent Ideals of $\mathcal{O}_{X}$ is injective
`(2.2.7)`, whence the conclusion.

**Corollary (2.2.16).**

<!-- label: IV.2.2.16 -->

*Let $X$, $Y$ be two $S$-preschemes; if $S' \to S$ is a faithfully flat morphism, the map $f \mapsto f_{(S')}$ from
$\operatorname{Hom}_{S}(X, Y)$ to $\operatorname{Hom}_{S'}(X_{(S')}, Y_{(S')})$ is injective.*

One has $X_{(S')} \times_{S'} Y_{(S')} = (X \times_{S} Y)_{(S')}$ `(I, 3.3.10)`, so the projection morphism $X_{(S')}
\times_{S'} Y_{(S')} \to X \times_{S} Y$ is faithfully flat `(2.2.13)`. The elements of $\operatorname{Hom}_{S}(X, Y)$
correspond bijectively to the sub-preschemes of $X \times_{S} Y$ that are the *graphs* of these $S$-morphisms
`(I, 5.3.11)`, and if $Z_{f}$ is the graph of $f \in \operatorname{Hom}_{S}(X, Y)$, one has $Z_{f_{(S')}} =
g^{-1}(Z_{f})$ `(I, 5.3.12)`. It therefore suffices to apply proposition `(2.2.15)` to $g$.

**Proposition (2.2.17).**

<!-- label: IV.2.2.17 -->

*Let $A$ be a ring, $B$ an $A$-algebra such that $B$ is a faithfully flat and finitely presented $A$-module. Then the
structure homomorphism $\phi : A \to B$ is an isomorphism of the $A$-module $A$ onto a direct factor of the $A$-module
$B$. If $A$ is a local ring, $B$ is a free $A$-module and there exists a basis of this module containing the unit
element of $B$.*

<!-- original page 14 -->

By virtue of Bourbaki, _Alg. comm._, chap. II, §3, n° 3, prop. 12, it suffices to prove the proposition when $A$ is a
local ring; one then knows (_loc. cit._, n° 2, cor. 2 of prop. 5) that $B$ is a free $A$-module of finite type, and the
conclusion follows from _loc. cit._, prop. 5.

### 2.3. Topological properties of flat morphisms

**Lemma (2.3.1).**

<!-- label: IV.2.3.1 -->

*Let $f : X \to Y$ be a quasi-compact and quasi-separated morphism, $g : Y' \to Y$ a flat morphism; set $X' = X
\times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$. Then, for every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, the
canonical homomorphism*

```text
  g*(f_*(ℱ)) → f'_*(ℱ ⊗_{𝒪_X} 𝒪_{X'})                            (2.3.1.1)
```

*is bijective.*

This is a particular case of `(III, 1.4.15)` (improved in `(1.7.21)`).

**Proposition (2.3.2).**

<!-- label: IV.2.3.2 -->

*Let $S$ be a prescheme, $f : X \to Y$ a quasi-compact and quasi-separated $S$-morphism; let $Z$ be the sub-prescheme of
$Y$, closed image of $X$ under $f$ `((I, 9.5.3)` and `(1.7.8))`, and let $j : Z \to Y$ be the canonical injection, so
that one has $f = j \circ g$, where $g : X \to Z$ is a morphism `(loc. cit.)`. Let $h : S' \to S$ be a flat morphism,
and set $f' = f_{(S')} : X_{(S')} \to Y_{(S')}$; then $j' = j_{(S')} : Z_{(S')} \to Y_{(S')}$ is identified with the
canonical injection of the sub-prescheme of $Y_{(S')}$ closed image of $X_{(S')}$ under $f'$.*

Since the morphism $Y_{(S')} \to Y$ is flat `(2.1.4)`, one may restrict to the case where $S = Y$ `(I, 3.3.11)`; if $f =
(\psi, \theta)$, one knows that $Z$ is the closed sub-prescheme of $S$ defined by the (quasi-coherent) Ideal
$\mathcal{J}$ of $\mathcal{O}_{S}$, kernel of the homomorphism $\theta : \mathcal{O}_{S} \to f_{*}(\mathcal{O}_{X})$
`(I, 9.5.2)`. Since $h$ is a flat morphism, the quasi-coherent Ideal $\mathcal{J} \mathcal{O}_{S'}$ of
$\mathcal{O}_{S'}$ is identified with the kernel of $h*(\theta) : \mathcal{O}_{S'} \to h*(f_{*}(\mathcal{O}_{X}))$. Now,
if $f' = (\psi', \theta')$, one verifies easily (for example by reducing to the case where $Y$ and $Y'$ are affine and
using `(I, 2.2.4)`) that $\theta' : \mathcal{O}_{S'} \to f'_{*}(\mathcal{O}_{X'})$ is the composite of the canonical
homomorphism `(2.3.1.1)` $h*(f_{*}(\mathcal{O}_{X})) \to f'_{*}(\mathcal{O}_{X'})$ and of $h*(\theta)$; the conclusion
therefore follows from `(2.3.1)` and `(I, 9.5.2)`, since $f$ is quasi-compact and quasi-separated `(1.1.2 and 1.2.2)`.

**(2.3.3)**

<!-- label: IV.2.3.3 -->

We shall say that a morphism $f : X \to Y$ is **quasi-flat** if there exists a quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ of finite type that is $f$-flat and whose support is equal to $X$. We shall say that $f$ is
**quasi-faithfully flat** if it is quasi-flat and surjective. Every flat (resp. faithfully flat) morphism is quasi-flat
(resp. quasi-faithfully flat), since then $\mathcal{F} = \mathcal{O}_{X}$ satisfies the preceding conditions.

It follows at once from `(2.1.4)` and `(I, 9.1.13)` that if $f$ is quasi-flat, then for every morphism $Y' \to Y$ the
morphism $f_{(Y')} : X \times_{Y} Y' \to Y'$ is quasi-flat. Similarly (taking `(I, 3.5.2)` into account), if $f$ is
quasi-faithfully flat, so is $f_{(Y')}$.

**Proposition (2.3.4).**

<!-- label: IV.2.3.4 -->

*Let $f : X \to Y$ be a quasi-flat morphism `(2.3.3)`. Then $f$ possesses the following properties (which are equivalent
by virtue of `(1.10.4)`):*

*(i) For every $x \in X$ and every generization $y'$ of $y = f(x)$, there exists a generization $x'$ of $x$ such that
$f(x') = y'$.*

*(ii) For every $x \in X$, the image under $f$ of $\operatorname{Spec}(\mathcal{O}_{X,x})$ is
$\operatorname{Spec}(\mathcal{O}_{Y,y})$.*

<!-- original page 15 -->

*(iii) For every irreducible closed part $Y'$ of $Y$, every irreducible component of $f^{-1}(Y')$ dominates $Y'$.*

It suffices, for example, to prove (ii). By hypothesis, there is a quasi-coherent $\mathcal{O}_{X}$-Module of finite
type $\mathcal{F}$, which is $f$-flat and such that $Supp(\mathcal{F}) = X$. For every $x \in X$, $\mathcal{F}_{x}$ is
then an $\mathcal{O}_{x}$-module of finite type, not reduced to `0`, and moreover $\mathcal{F}_{x}$ is a flat
$\mathcal{O}_{y}$-module, for the homomorphism $\rho : \mathcal{O}_{y} \to \mathcal{O}_{x}$. Since this latter is local
and $\mathcal{F}_{x} \neq 0$, Nakayama's lemma shows that $\mathcal{F}_{x} \otimes_{\mathcal{O}_{y}} k(y) \neq 0$, hence
$\mathcal{F}_{x}$ is a faithfully flat $\mathcal{O}_{y}$-module $(0_{I}, 6.4.1)$. It results that for every prime ideal
$\mathfrak{q}$ of $\mathcal{O}_{y}$, there exists a prime ideal $\mathfrak{p}$ of $\mathcal{O}_{x}$ such that
$\mathfrak{q} = \rho^{-1}(\mathfrak{p})$ $(0_{I}, 6.5.1)$, which proves (ii).

**Corollary (2.3.5).**

<!-- label: IV.2.3.5 -->

*Let $f : X \to Y$ be a morphism satisfying the equivalent conditions (i), (ii), (iii) of `(2.3.4)` (in particular a
quasi-flat morphism, or an open morphism `(1.10.4)`).*

*(i) Let $Z$, $Z'$ be two irreducible closed parts of $Y$ such that $Z \subset Z'$, and let $T$ be an irreducible
component of $f^{-1}(Z)$; then there exists an irreducible component $T'$ of $f^{-1}(Z')$ containing $T$ (and dominating
$Z'$).*

*(ii) For every irreducible component $T$ of $X$, $\overline{f(T)}$ is an irreducible component of $Y$.*

*(iii) Suppose $Y$ is irreducible, and, if $y$ is its generic point, suppose that $f^{-1}(y)$ is irreducible. Then $X$
is irreducible.*

(i) It suffices to apply `(2.3.4, (i))` taking for $x$ the generic point of $T$ ($y = f(x)$ then being the generic point
of $Z$) and for $y'$ the generic point of $Z'$.

(ii) It is clear that $f(T) = Z$ is irreducible, and by virtue of (i), $Z$ cannot be strictly contained in an
irreducible closed part $Z'$ of $Y$.

(iii) By virtue of (ii), every irreducible component of $X$ dominates $Y$, hence meets $f^{-1}(y)$; the conclusion then
follows from $(0_{I}, 2.1.8)$.

**Proposition (2.3.6).**

<!-- label: IV.2.3.6 -->

*Let $Y$ be a prescheme whose set of irreducible components is locally finite (which is the case if the space underlying
$Y$ is locally Noetherian (cf. `(I, 6.1.9)`)).*

*(i) Every closed part $W$ of $Y$ stable under generization $(0_{I}, 2.1.2)$ is open. In particular, every connected
component of $Y$ is open.*

*(ii) Let $f : X \to Y$ be a closed morphism satisfying moreover the equivalent conditions (i), (ii), (iii) of `(2.3.4)`
(which will be the case if $f$ is quasi-flat or open). Then the image under $f$ of every connected component $C$ of $X$
is a connected component of $Y$.*

*(iii) Let $f : X \to Y$ be a morphism satisfying the equivalent conditions (i), (ii), (iii) of `(2.3.4)` and such
moreover that for every $y \in Y$ the set $f^{-1}(y)$ is finite (which will be the case if $f$ is quasi-finite or
radicial). Then the set of irreducible components of $X$ is locally finite.*

(i) If $y \in W$, the generic points $\eta_{i}$ ($1 \leq i \leq m$) of the irreducible components $Y_{i}$ of $Y$
containing $y$ belong by hypothesis to $W$; hence, since $W$ is closed, these components themselves are contained in
$W$; since by hypothesis there is a neighbourhood $U$ of $y$ such that $U$ is the union of the $U \cap Y_{i}$ $(0_{I},
2.1.6)$, one has $U \subset W$, so $W$

<!-- original page 16 -->

is open. Since for every $y \in Y$, $\overline{y}$ is connected, a connected component of $Y$ is stable under
generization, so the second assertion follows at once from the first.

(ii) Since $C$ is closed in $X$, $f(C)$ is closed in $Y$ by hypothesis. Furthermore, since $C$ is stable under
generization, the hypothesis on $f$ entails that $f(C)$ is stable under generization; hence, by virtue of (i), $f(C)$ is
open and closed, and since it is connected it is a connected component of $Y$.

(iii) Let $x \in X$; by hypothesis, there is an open neighbourhood $U$ of $y = f(x)$ meeting only a finite number of
irreducible components $Y_{i}$ of $Y$ ($1 \leq i \leq n$); let $y_{i}$ be the generic point of $Y_{i}$ ($1 \leq i \leq
n$). For every irreducible component $Z$ of $X$ meeting $f^{-1}(U)$, the generic point $z$ of $Z$ is necessarily in one
of the sets $f^{-1}(y_{i})$ `(2.3.4)`. Since each of these sets is finite by hypothesis, this proves our assertion.

**Proposition (2.3.7).**

<!-- label: IV.2.3.7 -->

*Let $f : X \to Y$ be a morphism, $g : Y' \to Y$ a quasi-flat morphism, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to
Y'$.*

*(i) If $f$ is quasi-compact and dominant, so is $f'$.*

*(ii) If every irreducible component of $X$ dominates an irreducible component of $Y$, then every irreducible component
of $X'$ dominates an irreducible component of $Y'$.*

Denote by $g' : X' \to X$ the canonical projection, which is a quasi-flat morphism `(2.3.3)`.

(i) One already knows `(1.1.2)` that $f'$ is quasi-compact; furthermore, if $y'$ is a maximal point `(1.1.4)` of $Y'$,
$y = g(y')$ is a maximal point of $Y$, as results from `(2.3.4, (iii))`. By hypothesis `(1.1.5)` there exists $x \in X$
such that $f(x) = y$; hence `(I, 3.4.7)` there exists $x' \in X'$ such that $f'(x') = y'$.

(ii) Let $x'$ be a maximal point of $X'$, and let $x = g'(x')$; it follows from `(2.3.4, (ii))` that $x$ is a maximal
point of $X$, and by hypothesis $y = f(x)$ is a maximal point of $Y$. Set $y' = f'(x')$, so that $g(y') = y$; the issue
is to show that $y'$ is a maximal point of $Y'$. By virtue of `(I, 5.1.7)` and `(2.3.3)`, one may restrict to the case
where $X$ and $Y$ are reduced, so $\mathcal{O}_{x}$ and $\mathcal{O}_{y}$ are fields; moreover, by virtue of
`(I, 3.6.5)` applied twice and of `(I, 2.4.4)`, one may restrict to the case where $Y =
\operatorname{Spec}(\mathcal{O}_{y})$ and $Y' = \operatorname{Spec}(\mathcal{O}_{y'})$. Then $f$ is a flat morphism
since $\mathcal{O}_{y}$ is a field `(2.1.2)`, and the same is true of $f'$ `(2.1.4)`; hence it follows from
`(2.3.4, (ii))` that $y' = f'(x')$ is a maximal point of $Y'$.

**Corollary (2.3.8) (Zariski).**

<!-- label: IV.2.3.8 -->

*Let $A$, $B$ be two Noetherian local rings, $\mathfrak{m}$, $\mathfrak{n}$ their respective maximal ideals, $\phi : A
\to B$ a local homomorphism. Suppose the following hypotheses are satisfied:*

*1° $B$ is an $A$-algebra essentially of finite type `(1.3.8)`.*

*2° The completion `Â` of $A$ for the $\mathfrak{m}$-adic topology is integral.*

*3° $\phi$ is injective.*

*Then the $\mathfrak{m}$-adic topology of $A$ is induced by the $\mathfrak{n}$-adic topology of $B$.*

Set $B' = B \otimes_{A} \hat{A}$; by virtue of 1°, $B'$ is of the form $S^{-1}(C \otimes_{A} \hat{A})$, where $C$ is an
$A$-algebra of finite type and $S$ a multiplicative subset of $C$, so $B'$ is a Noetherian ring. Since $A$ is identified
with a subring of `Â` $(0_{I}, 7.3.5)$, $A$ is integral by 2°. Hypothesis 3° then entails that there exists a prime
ideal $\mathfrak{q}$ of $B$ inducing the ideal `0` of $A$ $(0_{I}, 1.5.8)$, and consequently the local homomorphism $A
\to B/\mathfrak{q}$ is injective. One may therefore restrict to proving the conclusion of `(2.3.8)` by adding the
hypothesis that $B$ is an integral local ring. Apply `(2.3.7, (ii))` to $Y = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$, $Y' = \operatorname{Spec}(\hat{A})$ and $X' = \operatorname{Spec}(B')$; since the morphism $Y'
\to Y$ is flat and $X$

<!-- original page 17 -->

(which is integral) dominates the integral scheme $Y$, every irreducible component of $X'$ dominates the scheme
(integral by hypothesis) $Y'$. If $y$, $x$, $y'$ are the closed points of $Y$, $X$, $Y'$ respectively, there is a point
$x' \in X'$ (in fact unique) above $x$ and $y'$ `(I, 3.4.9)` and $\operatorname{Spec}(\mathcal{O}_{x'})$ therefore
dominates $\operatorname{Spec}(\mathcal{O}_{y'})$; consequently one has a commutative diagram of local homomorphisms of
Noetherian local rings

```text
  B = 𝒪_x ────────→ 𝒪_{x'}
    ↑                  ↑
   φ│                 │v
    │                  │
  A = 𝒪_y ────u────→ 𝒪_{y'} = Â
```

such that $u$ and $v$ are injective `(I, 1.2.7)`; identifying $A$ and `Â` with subrings of $\mathcal{O}_{x'}$, and
denoting by $\mathfrak{r}$ the maximal ideal of $\mathcal{O}_{x'}$, the intersection of the ideals $\mathfrak{r}^{k}
\cap \hat{A}$ is therefore zero $(0_{I}, 7.3.5)$; since `Â` is complete and these ideals are open in `Â`, this entails
(Bourbaki, _Alg. comm._, chap. III, §2, n° 7, prop. 8) that the topology of `Â` is induced by the $\mathfrak{r}$-preadic
topology of $\mathcal{O}_{x'}$; a fortiori the same is true of the topology of $A$ $(0_{I}, 7.3.5)$. Moreover one has
$\mathfrak{n}^{k} \cap A \subset \mathfrak{r}^{k} \cap A$, so the $\mathfrak{n}$-preadic topology of $B$ induces on $A$
a topology finer than the $\mathfrak{m}$-preadic topology; but since $\mathfrak{m}^{k} \subset \mathfrak{n}^{k} \cap A$,
these two topologies are identical. Q.E.D.

**Remark (2.3.9).**

<!-- label: IV.2.3.9 -->

*We shall see further on `(7.8.3, (vii))` that for the Noetherian local rings $A$ most usual in algebraic geometry, the
hypothesis that $A$ is integral and integrally closed implies that the same holds for `Â`. That is why, in algebraic
geometry over a base field, one generally states `(2.3.8)` under the hypothesis that $A$ is integral and integrally
closed.*

**Theorem (2.3.10).**

<!-- label: IV.2.3.10 -->

*Let $f : X \to Y$ be a quasi-flat morphism `(2.3.3)`. Then, for every proconstructible part `(1.9.4)` $Z$ of $Y$, one
has $\overline{f^{-1}(Z)} = f^{-1}(\overline{Z})$.*

Since $f$ is continuous, one has $f^{-1}(Z) \subset f^{-1}(\overline{Z})$ and everything reduces to proving that for
every $x \in X$ such that $f(x) \in \overline{Z}$, $x$ is adherent to $f^{-1}(Z)$; it is clear that the question is
local on $Y$, so one may suppose $Y$ affine. By virtue of the hypothesis, there exists an affine scheme $Y'$ and a
morphism $g : Y' \to Y$ such that $g(Y') = Z$ `(1.9.5, (ix))`. Let `Y_1` be the closed image of $Y'$ under $g$
`(I, 9.5.3)`, and let `X_1` be the closed sub-prescheme $f^{-1}(Y_{1})$ of $X$; if $f_{1} : X_{1} \to Y_{1}$ is the
restriction of $f$ to `X_1`, one knows that $f_{1}$ is quasi-flat `(2.3.3)`; one may therefore replace $X$, $Y$ by
`X_1`, `Y_1` respectively, in other words suppose that $g$ is dominant. Set then $X' = X \times_{Y} Y'$, and let $f'$
and $g'$ be the projections of $X'$ onto $Y'$ and $X$ respectively, so that one has the commutative diagram

```text
  X  ←─g'──  X'
  │           │
  f│         │f'
  ↓           ↓
  Y  ←──g──  Y'
```

Since $f$ is quasi-flat, $g$ quasi-compact and dominant, it follows from `(2.3.7)` (where the roles of $f$ and $g$ are
interchanged) that $g'$ is a dominant morphism, which proves the theorem.

**Corollary (2.3.11).**

<!-- label: IV.2.3.11 -->

*Let $f$ be a quasi-flat and quasi-compact morphism, $F$ a closed part of $X$ such that $F = f^{-1}(f(F))$; then one has
$F = f^{-1}(\overline{f(F)})$.*

Let $Y'$ be the reduced sub-prescheme of $X$ having $F$ as underlying space `(I, 5.2.1)` and let $j : Y' \to X$ be the
canonical injection; then $f \circ j$ is quasi-compact `(1.1.2)`,

<!-- original page 18 -->

so $Z = f(F)$ is pro-constructible in $Y$ `(1.9.5, (vii))`, and the corollary follows from the fact that $F$ is closed.

One may further write the result of `(2.3.11)` in the form $F = f^{-1}(f(X) \cap \overline{f(F)})$, in other words, the
closed sets of the subspace $f(X)$ of $Y$ are the parts $Z \subset f(X)$ such that $f^{-1}(Z)$ is closed in $X$; this
also means that *the topology induced by $Y$ on $f(X)$ is the quotient of that of $X$ by the equivalence relation
defined by $f$*. In particular:

**Corollary (2.3.12).**

<!-- label: IV.2.3.12 -->

*Let $f : X \to Y$ be a quasi-faithfully flat `(2.3.3)` and quasi-compact morphism. Then the topology of $Y$ is the
quotient of that of $X$ by the equivalence relation defined by $f$ (in other words, for $Z \subset Y$ to be open (resp.
closed) in $Y$, it is necessary and sufficient that $f^{-1}(Z)$ be open (resp. closed) in $X$).*

Indeed, one then has $f(X) = Y$.

**Corollary (2.3.13).**

<!-- label: IV.2.3.13 -->

*Let $X$, $Y$ be two $S$-preschemes, $f : X \to Y$ a faithfully flat and quasi-compact $S$-morphism. For $Y$ to be
separated over $S$, it is necessary and sufficient that the canonical immersion $j : X \times_{Y} X \to X \times_{S} X$
`(I, 5.3.10)` be closed.*

Let us note for this that one has the commutative diagram `(I, 5.3.5)`

```text
  X ×_Y X  ──j──→  X ×_S X
    │                │
    π│              │f ×_S f
    ↓                ↓
    Y    ──Δ_Y──→  Y ×_S Y
```

identifying $X \times_{Y} X$ with the product of the $(Y \times_{S} Y)$-preschemes $Y$ and $X \times_{S} X$. Since $f$
is surjective, so are $\pi$ and $f \times_{S} f$, so the diagonal $\Delta_{Y}(Y)$ has as inverse image under $f
\times_{S} f$ the image $j(X \times_{Y} X)$ `(I, 3.4.8)`. Since $f \times_{S} f$ is faithfully flat and quasi-compact
`(1.1.2 and 2.2.13)`, it suffices to apply `(2.3.12)` to this morphism.

**Corollary (2.3.14).**

<!-- label: IV.2.3.14 -->

*Let $f : X \to Y$ be a quasi-faithfully flat and quasi-compact morphism, and let $Z$ be a part of $Y$. For $Z$ to be a
locally closed pro-constructible part of $Y$, it is necessary and sufficient that $f^{-1}(Z)$ be a locally closed
pro-constructible part of $X$.*

One already knows `(1.9.12)` that, for $Z$ to be a pro-constructible part of $Y$, it is necessary and sufficient that
$f^{-1}(Z)$ be a pro-constructible part of $X$. The condition is evidently necessary. To prove that it is sufficient,
consider the reduced closed sub-prescheme `Y_1` of $Y$ having $\overline{Z}$ as underlying space, and let `X_1` be its
inverse image under $f$, which has as underlying space $f^{-1}(\overline{Z}) = \overline{f^{-1}(Z)}$ by virtue of
`(2.3.10)`. Since $f^{-1}(Z)$ is locally closed in $X$, it is open in $\overline{f^{-1}(Z)}$, hence in `X_1`; now the
morphism $f_{1} : X_{1} \to Y_{1}$ deduced from $f$ by restriction is quasi-faithfully flat and quasi-compact
`(1.1.2 and 2.3.3)`; one therefore deduces from `(2.3.12)` that $Z$ is open in $\overline{Z}$, which shows that $Z$ is
locally closed in $Y$.

**Remark (2.3.15).**

<!-- label: IV.2.3.15 -->

*It does not suffice, in `(2.3.12)`, to suppose only that $f$ is faithfully flat. For example, take for $Y$ a reduced
irreducible algebraic curve*

<!-- original page 19 -->

*`(II, 7.4.2)`, for $X$ the prescheme sum of the schemes $\operatorname{Spec}(\mathcal{O}_{y})$, where $y$ runs over $Y$
`(I, 3.1)`, for $f$ the canonical morphism, which is faithfully flat `(I, 2.4.2)`; if $\eta$ denotes the generic point
of $Y$, $Z = {\eta}$ is not open in $Y$ `(II, 7.4.3)`, but $f^{-1}(Z) = \operatorname{Spec}(\mathcal{O}_{\eta})$ since
$\mathcal{O}_{\eta}$ is a field, and consequently $f^{-1}(Z)$ is open in $X$.*

### 2.4. Universally open morphisms and flat morphisms

**(2.4.1)**

<!-- label: IV.2.4.1 -->

We have already defined `(II, 5.4.9)` the notion of *universally closed* morphism; in the same way, one poses the
following definitions:

**Definition (2.4.2).**

<!-- label: IV.2.4.2 -->

*One says that a morphism of preschemes $f : X \to Y$ is **universally open** (resp. **universally bicontinuous**, resp.
a **universal homeomorphism**) if, for every morphism $g : Y' \to Y$, the morphism $f_{(Y')} : X \times_{Y} Y' \to Y'$
is open (resp. a homeomorphism onto its image, resp. a homeomorphism onto $Y'$).*

We shall see further on `(14.3.2)` that when $Y$ is locally Noetherian, the definition of universally open morphism
given here is equivalent to the definition `(III, 4.3.9)` for morphisms of finite type; the reader may verify that we do
not use this latter definition before §14.

**Proposition (2.4.3).**

<!-- label: IV.2.4.3 -->

*(i) An immersion (resp. an open immersion, resp. a closed immersion) is universally bicontinuous (resp. universally
open, resp. universally closed).*

*(ii) The composite of two universally open (resp. universally closed, resp. universally bicontinuous, resp. two
universal homeomorphisms) morphisms is also.*

*(iii) If $f : X \to Y$ is a universally open (resp. universally closed, resp. universally bicontinuous, resp. a
universal homeomorphism) $S$-morphism, so is $f_{(S')} : X_{(S')} \to Y_{(S')}$ for every base change $S' \to S$.*

*(iv) If $f : X \to X'$, $g : Y \to Y'$ are two universally open (resp. universally closed, resp. universally
bicontinuous, resp. two universal homeomorphism) $S$-morphisms, so is $f \times_{S} g : X \times_{S} Y \to X' \times_{S}
Y'$.*

*(v) Let $f : X \to Y$, $g : Y \to Z$ be two morphisms such that $f$ is surjective; if $g \circ f$ is universally open
(resp. universally closed, resp. universally bicontinuous, resp. a universal homeomorphism), so is $g$.*

*(vi) For $f$ to be a universally open (resp. universally closed, resp. universally bicontinuous, resp. a universal
homeomorphism) morphism, it is necessary and sufficient that $f_{red}$ be so.*

*(vii) Let $(U_{\alpha})$ be an open cover of $Y$. For $f : X \to Y$ to be universally open (resp. universally closed,
resp. universally bicontinuous, resp. a universal homeomorphism), it is necessary and sufficient that for every
$\alpha$, its restriction $f^{-1}(U_{\alpha}) \to U_{\alpha}$ be so.*

Assertion (i) results from `(I, 4.3.2)`. Assertion (ii) follows at once from the definitions, and so does (iii) on
reducing to the case where $Y = S$, $Y' = S'$, which one may do thanks to `(I, 3.3.11)`; one knows that (iv) follows
from (ii) and (iii) `(I, 3.5.1)`. To prove (v), note that for every morphism $Z' \to Z$, $f_{(Z')} : X_{(Z')} \to
Y_{(Z')}$ is surjective `(I, 3.5.2)`; one may therefore restrict to proving that if $g \circ f$ is open (resp. closed,
resp. a

<!-- original page 20 -->

homeomorphism onto its image, resp. a bijective homeomorphism), so is $g$, and so the matter is a purely topological
question. For the case where $g \circ f$ is open (resp. closed), the fact that $g$ is then open (resp. closed) results
from Bourbaki, _Top. gén._, chap. I, 3rd ed., §5, n° 1, prop. 1; for the two other cases, one may restrict to supposing
that $g(f(X)) = g(Y) = Z$, in other words to the case where $g \circ f$ is a homeomorphism of $X$ onto $Z$; since $f$ is
surjective, $g$ is necessarily bijective, and since $g$ is a continuous open map by what precedes, $g$ is indeed a
homeomorphism of $Y$ onto $Z$.

To prove (vi), note that saying that a morphism $g$ is open (resp. closed, resp. a homeomorphism onto its image, resp. a
bijective homeomorphism) amounts to saying that $g_{red}$ has the same property. On the other hand `(I, 5.1.8)`, for
every morphism $Y' \to Y$, one has `(X_red ×_{Y_red} Y'_red)_red = (X ×_Y Y')_red`, so the preceding remark shows that
if $f_{red}$ is universally open (resp. universally closed, resp. universally bicontinuous, resp. a universal
homeomorphism), so is $f$. The converse is proved similarly, noting here that for every morphism $Y'' \to Y_{red}$, one
has `(X_red ×_{Y_red} Y'')_red = (X ×_Y Y'')_red` `(I, 5.1.3)`.

Finally, the necessity of (vii) results at once from (iii). Conversely, suppose condition (vii) holds, and let $g : Y'
\to Y$ be a morphism; then the $g^{-1}(U_{\alpha}) = U'_{\alpha}$ form an open cover of $Y'$, and if one denotes by
$f_{\alpha}$ the restriction $f^{-1}(U_{\alpha}) \to U_{\alpha}$ of $f$, and by $f'$ the morphism $f_{(Y')}$, the
restriction $f'^{-1}(U'_{\alpha}) \to U'_{\alpha}$ is none other than $(f_{\alpha})_{(U'_{\alpha})}$. One may therefore
restrict to proving that $f$ is open (resp. closed, resp. a homeomorphism onto its image, resp. a homeomorphism onto
$Y$), which is immediate.

**Proposition (2.4.4).**

<!-- label: IV.2.4.4 -->

*A universally bicontinuous morphism $f : X \to Y$ is radicial (hence separated `(1.7.7.1)`).*

Indeed, $f$ is universally injective by hypothesis `(I, 3.5.11)`.

**Proposition (2.4.5).**

<!-- label: IV.2.4.5 -->

*(i) A morphism $f : X \to Y$ that is integral, surjective and radicial is a universal homeomorphism.*

*(ii) Conversely, suppose $Y$ locally Noetherian. Then, if a morphism of finite type $f : X \to Y$ is a universal
homeomorphism, it is finite, surjective and radicial.*

(i) It suffices to observe that the three properties of $f$ are preserved by base change
`(I, 3.5.2, I, 3.5.7 and II, 6.1.5)`, and since an integral morphism is closed `(II, 6.1.10)`, it is clear that $f$ is a
homeomorphism of $X$ onto $Y$.

(ii) Since $f$ is of finite type and universally closed by hypothesis and separated by `(2.4.4)`, it is proper
`(II, 5.4.1)`, and for every $y \in Y$, $f^{-1}(y)$ is reduced to a single element; hence `(III, 4.4.2)` $f$ is finite;
it is clear that $f$ is surjective, and it is radicial since it is universally injective `(I, 3.5.11)`.

**Theorem (2.4.6).**

<!-- label: IV.2.4.6 -->

*Let $f : X \to Y$ be a quasi-flat `(2.3.3)` and locally of finite presentation morphism. Then $f$ is universally open.
In particular, a flat morphism locally of finite presentation is universally open.*

One knows that for every base change $Y' \to Y$, $f_{(Y')}$ is quasi-flat `(2.3.3)` and locally of finite presentation
`(1.4.3, (iii))`. It therefore suffices to prove that $f$ is an

<!-- original page 21 -->

open morphism. But this follows from criterion `(1.10.4)` for morphisms locally of finite presentation, conditions b),
b'), and c) of `(1.10.4)` being none other than conditions (i), (ii), (iii) of `(2.3.4)`.

**Corollary (2.4.7).**

<!-- label: IV.2.4.7 -->

*For every prescheme $Y$, the structure morphism $\mathbf{V}^{n}_{Y} \to Y$ (where $\mathbf{V}^{n}_{Y} = Y
\otimes_{\mathbb{Z}} \operatorname{Spec}(\mathbb{Z}[T_{1}, \cdots, T_{n}])$, also denoted $Y[T_{1}, \cdots, T_{n}]$) is
universally open.*

Indeed, for $Y = \operatorname{Spec}(A)$, $Y[T_{1}, \cdots, T_{n}] = \operatorname{Spec}(A[T_{1}, \cdots, T_{n}])$, and
$A[T_{1}, \cdots, T_{n}]$ is a free $A$-algebra of finite presentation.

**Remarks (2.4.8).**

<!-- label: IV.2.4.8 -->

*(i) One notes that a faithfully flat and quasi-compact morphism $f : X \to Y$ is not necessarily open, even when $X$
and $Y$ are Noetherian. Take for example for $Y$ a reduced irreducible algebraic curve `(II, 7.4)` with generic point
$y$, and let $X$ be the prescheme sum $Y \amalg \operatorname{Spec}(k(y))$, $f$ being the canonical morphism; it is
clear that $f$ is flat and surjective, hence faithfully flat, and quasi-compact, but the image under $f$ of the open
part $\operatorname{Spec}(k(y))$ of $X$ is the set ${y}$, which is not open in $Y$ `(II, 7.4.3)`.*

*(ii) For every prescheme $X$, the canonical morphism $f : X_{red} \to X$ is a closed immersion and a universal
homeomorphism `(2.4.4, (vi))`; but when $X$ is locally Noetherian, $f$ is flat only if $X$ is reduced, hence $f = 1_{X}$
`(2.2.17)`.*

**Proposition (2.4.9).**

<!-- label: IV.2.4.9 -->

*Let $Y$ be a discrete prescheme. Then every morphism $f : X \to Y$ is universally open.*

The question being local on $Y$ `(2.4.3, (vii))`, one may restrict to the case where the space underlying $Y$ is reduced
to a point; replacing $f$ by $f_{red}$ `(2.4.3, (vi))`, one may furthermore suppose that $Y$ is the spectrum of a field
$k$; on the other hand, for every base change $Y' \to Y$, the open sets of $X' = X \times_{Y} Y'$ inverse images of the
affine open sets of $X$ cover $X'$, so one may suppose $X = \operatorname{Spec}(B)$ affine, $B$ being a $k$-algebra. The
issue is therefore to prove that for every $k$-algebra $A'$, if one sets $B' = B \otimes_{k} A'$, the image under $f' :
\operatorname{Spec}(B') \to \operatorname{Spec}(A')$ of every open set of the form $U = D(t)$ ($t \in B'$) is open in
$\operatorname{Spec}(A')$. Now, $B$ is the direct limit of the increasing filtered family $(B_{\alpha})$ of its
sub-$k$-algebras of finite type, hence (the functor `lim` commuting with tensor products), $B'$ is the direct limit of
the $A'$-algebras $B_{\alpha} \otimes_{k} A' = B'_{\alpha}$; there exists $\alpha$ such that $t$ is the image in $B'$ of
an element $t_{\alpha} \in B'_{\alpha}$, hence $D(t)$ is the inverse image under the canonical morphism $u_{\alpha} :
\operatorname{Spec}(B') \to \operatorname{Spec}(B'_{\alpha})$ of the open set $U_{\alpha} = D(t_{\alpha})$
`(I, 1.2.2.2)`. But since $k$ is a field, $B_{\alpha}$ is a $k$-algebra of finite presentation and a flat $k$-module,
hence $B'_{\alpha}$ is an $A'$-algebra of finite presentation and a flat $A'$-module; one therefore concludes from
`(2.4.6)` that the image of $U_{\alpha}$ under $f'_{\alpha} : \operatorname{Spec}(B'_{\alpha}) \to
\operatorname{Spec}(A')$ is open in $\operatorname{Spec}(A')$. Everything therefore reduces to seeing that $f'(U) =
f'_{\alpha}(U_{\alpha})$; it is clear that $f'(U) \subset f'_{\alpha}(U_{\alpha})$, and it therefore remains to see that
for every point $y' \in f'_{\alpha}(U_{\alpha})$, the intersection $V = U \cap f'^{-1}(y')$ is non-empty. Now one has $V
= v^{-1}(V_{\alpha})$, where $V_{\alpha} = U_{\alpha} \cap f'^{-1}_{\alpha}(y')$; in other words, $V_{\alpha}$ is a
non-empty open set (by definition of $y'$) of the prescheme $\operatorname{Spec}(B'_{\alpha} \otimes_{A'} k(y')) =
\operatorname{Spec}(B_{\alpha} \otimes_{k} k(y'))$ and $V$ is its inverse image under the morphism $v :
\operatorname{Spec}(B \otimes_{k} k(y')) \to \operatorname{Spec}(B_{\alpha} \otimes_{k} k(y'))$. Since $B_{\alpha}$ is a
subalgebra of $B$ and $k$ is a field, the homomorphism $B_{\alpha} \otimes_{k} k(y') \to B \otimes_{k} k(y')$

<!-- original page 22 -->

is injective by flatness, so the morphism $v$ is dominant `(I, 1.2.7)`, which completes the proof.

**Corollary (2.4.10).**

<!-- label: IV.2.4.10 -->

*Let $k$ be a field; $X$, $Y$ $k$-preschemes; then the projection morphism $X \times_{k} Y \to X$ is universally open.
In particular, for every extension $K$ of $k$, the projection morphism $X_{(K)} \to X$ is universally open.*

It suffices to apply `(2.4.9)` to the structure morphism $Y \to \operatorname{Spec}(k)$.

**Remark (2.4.11).**

<!-- label: IV.2.4.11 -->

*If $f : X \to Y$ is an open morphism, one knows that, for every part $E$ of $Y$, one has $f^{-1}(\overline{E}) =
\overline{f^{-1}(E)}$ (Bourbaki, _Top. gén._, chap. I, 3rd ed., §5, n° 4, prop. 7). This remark applies for example when
$f$ is a flat morphism locally of finite presentation `(2.4.6)`, or a projection morphism $X \times_{k} Y \to X$ where
$X$, $Y$ are preschemes over a field $k$ `(2.4.10)`, and then generalizes `(2.3.10)`.*

<!-- original page 22 -->

### 2.5. Permanence of properties of Modules under faithfully flat descent

**Proposition (2.5.1).**

<!-- label: IV.2.5.1 -->

*Let $f : X \to Y$ be a morphism, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, $g : Y' \to Y$ a faithfully
flat morphism, $X' = X \times_{Y} Y'$, $f' = f_{(Y')} : X' \to Y'$, $\mathcal{F}' = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$. For $\mathcal{F}$ to be flat (resp. faithfully flat) relative to $f$, it is
necessary and sufficient that $\mathcal{F}'$ be flat (resp. faithfully flat) relative to $f'$.*

It suffices to apply `(2.2.10)` after replacing $X$, $Y'$, $Z$, $\mathcal{F}$, $\mathcal{G}$ by $Y'$, $X$, $Y$,
$\mathcal{O}_{Y'}$, $\mathcal{F}$ respectively; one concludes that for $\mathcal{F}'$ to be flat (resp. faithfully flat)
relative to $f'$, it is necessary and sufficient that $\mathcal{F}$ be flat (resp. faithfully flat) relative to $g \circ
f'$. But if $g' : X' \to X$ is the canonical projection, $g'$ is faithfully flat `(2.2.13)` and one has $g \circ f' = f
\circ g'$; hence for $\mathcal{F}$ to be flat (resp. faithfully flat) relative to $f \circ g'$, it is necessary and
sufficient that $\mathcal{F}$ be so relative to $f$ `(2.2.11, (iii))`.

**Proposition (2.5.2).**

<!-- label: IV.2.5.2 -->

*Let $f : X' \to X$ be a faithfully flat and quasi-compact morphism, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module, $\mathcal{F}' = f*(\mathcal{F})$. Consider, for a quasi-coherent Module, the property of
being:*

*(i) of finite type;*

*(ii) of finite presentation;*

*(iii) locally free of finite type;*

*(iv) locally free of rank $n$.*

*Then, if $P$ denotes one of the preceding properties, for $\mathcal{F}$ to possess the property $P$ it is necessary and
sufficient that $\mathcal{F}'$ possess it.*

For a quasi-coherent $\mathcal{O}_{X}$-Module to be locally free of finite type, it is necessary and sufficient that it
be flat over $X$ and of finite presentation (Bourbaki, *Alg. comm.*, chap. II, §5, n° 2, cor. 2 of th. 1, taking
`(2.1.2)` into account); since $\mathcal{F}$ is flat over $X$ if and only if $\mathcal{F}'$ is flat over $X'$ by virtue
of `(2.5.1)` (applied with $f$ taken to be the identity), one sees that in order to prove the proposition in case (iii)
it suffices to have proved it in cases (i) and (ii); the same holds for (iv), since $f*(\mathcal{O}_{X}) =
\mathcal{O}_{X'}$, so that if $\mathcal{F}$ and $\mathcal{F}'$ are locally free of finite type and $x = f(x')$, the rank
of $\mathcal{F}'$ at $x'$ equals that of $\mathcal{F}$ at $x$, and our assertion follows from the surjectivity of $f$.
To treat cases (i) and (ii),

<!-- original page 23 -->

note that the question is local on $X$, and one may therefore suppose $X$ affine; one then knows `(2.2.12)` that there
exists an affine scheme `X''` and a faithfully flat morphism $g : X'' \to X'$ which is a local isomorphism.
Consequently, it amounts to the same thing to say that $f*(\mathcal{F})$ possesses the property $P$ or that
$g*(f*(\mathcal{F}))$ does. We are thus reduced to the case where $X = \operatorname{Spec}(A)$, $X' =
\operatorname{Spec}(A')$; in view of `(2.2.3)` and `(II, 6.1.4.1)`, it therefore suffices to prove the

**Lemma (2.5.3).**

<!-- label: IV.2.5.3 -->

*Let $A$ be a ring, $A'$ a faithfully flat $A$-algebra, $M$ an $A$-module, $M' = M \otimes_{A} A'$. For $M$ to be of
finite type (resp. of finite presentation), it is necessary and sufficient that $M'$ be so.*

For the proof, see Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop. 11.

**Remark (2.5.4).**

<!-- label: IV.2.5.4 -->

*The assertions of `(2.5.2)` for the properties (i) and (ii) are still valid if one supposes only that $f$ is
quasi-faithfully flat `(2.3.3)` and quasi-compact. Indeed, one is reduced (Bourbaki, *loc. cit.*) to proving the*

**Lemma (2.5.4.1).**

<!-- label: IV.2.5.4.1 -->

*Let $\rho : A \to A'$ be a homomorphism of rings such that the corresponding morphism $f : \operatorname{Spec}(A') \to
\operatorname{Spec}(A)$ is surjective; suppose there exists an $A'$-module $N'$ of finite type which is $A$-flat and has
$\operatorname{Spec}(A')$ as support. Then, if $u : P \to Q$ is a homomorphism of $A$-modules such that $u \otimes 1 : P
\otimes_{A} A' \to Q \otimes_{A} A'$ is surjective, $u$ is surjective.*

Indeed, one deduces first that the homomorphism $u \otimes 1_{N'} : (P \otimes_{A} A') \otimes_{A'} N' \to (Q
\otimes_{A} A') \otimes_{A'} N'$ is surjective. Let $\mathfrak{q}$ be a prime ideal of $A'$, and let $\mathfrak{p} =
\rho^{-1}(\mathfrak{q})$; the corresponding homomorphism $(P \otimes_{A} N')_{\mathfrak{q}} \to (Q \otimes_{A}
N')_{\mathfrak{q}}$ is surjective, and it can be written $u_{\mathfrak{p}} \otimes 1 : P_{\mathfrak{p}}
\otimes_{A_{\mathfrak{p}}} N'_{\mathfrak{q}} \to Q_{\mathfrak{p}} \otimes_{A_{\mathfrak{p}}} N'_{\mathfrak{q}}$ $(0_{I},
1.5.4)$. By hypothesis $N'_{\mathfrak{q}} \neq 0$, and $N'_{\mathfrak{q}}$ is a flat $A_{\mathfrak{p}}$-module $(0_{I},
6.3.1)$; by virtue of Nakayama's lemma, $\mathfrak{q} N'_{\mathfrak{q}} \neq N'_{\mathfrak{q}}$, and a fortiori
$\mathfrak{p} N'_{\mathfrak{q}} \neq N'_{\mathfrak{q}}$, so $N'_{\mathfrak{q}}$ is a faithfully flat
$A_{\mathfrak{p}}$-module $(0_{I}, 6.4.1)$. It follows that $u_{\mathfrak{p}}$ is surjective $(0_{I}, 6.4.1)$, and since
this holds for every $\mathfrak{p} \in \operatorname{Spec}(A)$, $f$ being surjective, one finally concludes that $u$ is
surjective (Bourbaki, *Alg. comm.*, chap. II, §3, n° 3, th. 1).

**Proposition (2.5.5).**

<!-- label: IV.2.5.5 -->

*Let $f : X \to Y$ be a morphism, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite type and $f$-flat,
$\mathcal{G}$ a quasi-coherent $\mathcal{O}_{Y}$-Module of finite type; for every $y \in Y$, put $\mathcal{F}_{y} =
\mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$. For a point $x \in X$ to be a maximal point of $Supp(\mathcal{F}
\otimes_{Y} \mathcal{G})$, it is necessary and sufficient that $y = f(x)$ be a maximal point of $Supp(\mathcal{G})$ and
that $x$ be a maximal point of $Supp(\mathcal{F}_{y})$ in $f^{-1}(y)$. When this is so, one has*

```text
(2.5.5.1)         long((ℱ ⊗_Y 𝒢)_x) = long(𝒢_y) · long((ℱ_y)_x).
```

It is clear that $f(Supp(\mathcal{F} \otimes_{Y} \mathcal{G})) \subset Supp(\mathcal{G})$ $(0_{I}, 5.2.2)$; the image
under $f$ of every irreducible component of $Supp(\mathcal{F} \otimes_{Y} \mathcal{G})$ is therefore contained in an
irreducible component of $Supp(\mathcal{G})$. One may restrict to the case where $Supp(\mathcal{G}) = Y$. Indeed
$(Err_{II}, 30)$, since $\mathcal{G}$ is of finite type, there exists a closed sub-prescheme $Y'$ of $Y$ having
$Supp(\mathcal{G})$ as underlying space and a quasi-coherent $\mathcal{O}_{Y'}$-Module of finite type $\mathcal{G}_{1}$
such that, if $j : Y' \to Y$ is the canonical injection, one has $\mathcal{G} = j_{*}(\mathcal{G}_{1})$. If one then
puts $f_{1} = j \circ f'$, where $f' : X' = X \times_{Y} Y' \to Y'$, it is clear that $\mathcal{F}' = \mathcal{F}
\otimes_{Y} \mathcal{O}_{Y'}$ is $f'$-flat and that $Supp(\mathcal{F}' \otimes_{Y'} \mathcal{G}_{1}) = Supp(\mathcal{F}
\otimes_{Y} \mathcal{G})$.

Suppose therefore $Supp(\mathcal{G}) = Y$; if $Z$ is an irreducible component of $Supp(\mathcal{G})$, one has $f^{-1}(Z)
\subset Supp(\mathcal{F} \otimes_{Y} \mathcal{G})$ `(I, 9.1.13)`, and it follows from `(2.3.4)` that every irreducible
component of $f^{-1}(Z)$ dominates $Z$. In other words, if $x$ is the generic point of an irreducible component of
$Supp(\mathcal{F} \otimes_{Y} \mathcal{G})$ contained in $f^{-1}(Z)$, then $y = f(x)$ is the generic point of $Z$;
furthermore $(0_{I}, 2.1.8)$, $x$ is the generic point of an irreducible component of $f^{-1}(y) =
Supp(\mathcal{F}_{y})$ `(I, 9.1.13)`, and conversely every generic point of one of these components is the generic point
of an irreducible component of $f^{-1}(Z)$.

<!-- original page 24 -->

It remains to prove `(2.5.5.1)`; one has $(\mathcal{F} \otimes_{Y} \mathcal{G})_{x} = \mathcal{F}_{x}
\otimes_{\mathcal{O}_{y}} \mathcal{G}_{y}$ `(I, 9.1.12)` and $(\mathcal{F}_{y})_{x} = \mathcal{F}_{x} / \mathfrak{m}_{y}
\mathcal{F}_{x}$; one is therefore reduced to proving the

**Lemma (2.5.5.2).**

<!-- label: IV.2.5.5.2 -->

*Let $A$, $B$ be two local rings, $\rho : A \to B$ a local homomorphism, $\mathfrak{m}$ the maximal ideal of $A$. Let
$M$ be an $A$-module, $N$ a $B$-module which is a faithfully flat $A$-module and is such that $N/\mathfrak{m} N$ is a
$B$-module of finite length; then one has*

```text
(2.5.5.3)         long_B(M ⊗_A N) = long_A(M) · long_B(N/𝔪 N).
```

If $M$ has infinite length, then so does $M \otimes_{A} N$, for every strictly increasing sequence of $n$ sub-modules
$M_{i} \subset M$ ($1 \leq i \leq n$) yields sub-modules $M_{i} \otimes_{A} N$ of $M \otimes_{A} N$ which are pairwise
distinct; since $N \neq \mathfrak{m} N$ (because $N$ is a faithfully flat $A$-module), the formula `(2.5.5.3)` is true
in this case. Suppose then that $M$ has finite length. If $M = 0$, both members of `(2.5.5.3)` are zero, so we may
suppose $M \neq 0$. The $\mathfrak{m}^{k} M$ are sub-modules of $M$, hence of finite length, and if $\mathfrak{m}^{k} M
\neq 0$, Nakayama's lemma implies $\mathfrak{m}^{k+1} M \neq \mathfrak{m}^{k} M$; consequently there exists necessarily
an integer $r$ such that $\mathfrak{m}^{r} M = 0$. The $\mathfrak{m}^{k} M \otimes_{A} N$ then identify with
sub-$B$-modules of $M \otimes_{A} N$, and $(\mathfrak{m}^{k} M \otimes_{A} N) / (\mathfrak{m}^{k+1} M \otimes_{A} N)$ is
isomorphic to $(\mathfrak{m}^{k} M / \mathfrak{m}^{k+1} M) \otimes_{A} N$, hence also to $(\mathfrak{m}^{k} M /
\mathfrak{m}^{k+1} M) \otimes_{A/\mathfrak{m}} (N/\mathfrak{m} N)$ $(0 \leq k \leq r - 1)$. The length of the latter,
regarded as a $B$-module, is therefore the product of $long_{B}(N/\mathfrak{m} N)$ by the rank of the
$(A/\mathfrak{m})$-vector space $\mathfrak{m}^{k} M / \mathfrak{m}^{k+1} M$, which equals the length of the $A$-module
$\mathfrak{m}^{k} M / \mathfrak{m}^{k+1} M$. Summing over $0 \leq k \leq r - 1$, one deduces at once the formula
`(2.5.5.3)`.

**Remark (2.5.5.4).**

<!-- label: IV.2.5.5.4 -->

*Note that when $N$ is an $A$-module of finite type, to say that $N$ is a faithfully flat $A$-module amounts to saying
that $N \neq 0$ and that $N$ is a flat $A$-module; indeed, Nakayama's lemma then shows that $\mathfrak{m} N \neq N$.*

**Lemma (2.5.6).**

<!-- label: IV.2.5.6 -->

*Let $B$ be a (not necessarily commutative) ring, $V$, $W$ two isomorphic left $B$-modules, $C =
\operatorname{End}_{B}(V)$, and let $M = \operatorname{Hom}_{B}(V, W)$, equipped with its canonical structure of right
$C$-module. Then $M$ is a $C$-module isomorphic to $C_{d}$; furthermore, for every $u \in M$, the following conditions
are equivalent:*

*a) ${u}$ is a basis of the $C$-module $M$.*

*b) $u$ is an isomorphism of $V$ onto $W$.*

If $u$ is an isomorphism of $V$ onto $W$, the map $v \mapsto u \circ v$ from $C$ to $M$ is obviously a bijection, so b)
implies a). Conversely, suppose that ${u}$ is a basis of the $C$-module $M$. By hypothesis there exists an isomorphism
$u'$ of $V$ onto $W$, and `{u'}` is then a basis of $M$; hence there is an invertible element $w$ of $C$ (i.e. an
automorphism of $V$) such that $u = u' \circ w$, which implies that $u$ is an isomorphism of $V$ onto $W$.

**Corollary (2.5.7).**

<!-- label: IV.2.5.7 -->

*The hypotheses on $B$, $V$, $W$ being those of `(2.5.6)`, suppose furthermore that one of the following conditions
holds:*

*(i) $V$ and $W$ are Noetherian $B$-modules;*

*(ii) $V$ and $W$ are modules of finite presentation over a commutative subring of $B$.*

*Then the conditions a) and b) of `(2.5.6)` are also equivalent to the following:*

*a') $u$ is a generator of the $C$-module $M$.*

*b') $u$ is an epimorphism of $V$ onto $W$.*

One knows that an epimorphism of an $A$-module $E$ onto itself is bijective in the following two cases: 1° $E$ is a
Noetherian $A$-module (Bourbaki, *Alg.*, chap. VIII, §2, n° 2, lemma 3); 2° $A$ is commutative and $E$ is an $A$-module
of finite presentation `(8.9.3)` (¹); hence b) and b') are equivalent. On the other hand, if $u$ generates $M$

______________________________________________________________________

(¹) The reader may verify that `(2.5.7)` and `(2.5.8)` are not used before §9.

<!-- original page 25 -->

and `{u'}` is a basis of $M$, there exists $v \in C$ such that $u' = u \circ v$, which proves that $u$ is surjective;
therefore a') implies b'), and as a) evidently implies a'), this finishes the proof of the corollary.

**Proposition (2.5.8).**

<!-- label: IV.2.5.8 -->

*Let $A$ be a commutative semi-local ring, $B$ an $A$-algebra (not necessarily commutative), $V$ and $W$ two
$B$-modules. Let $A'$ be a commutative $A$-algebra which is a faithfully flat $A$-module; put $B' = B \otimes_{A} A'$,
$V' = V \otimes_{A} A'$, $W' = W \otimes_{A} A'$, so that $B'$ is an $A'$-algebra and $V'$, $W'$ are $B'$-modules.
Suppose furthermore that one of the following conditions holds:*

*(i) $A$ and $A'$ are Noetherian, $V$ and $W$ are $A$-modules of finite type.*

*(ii) $B$ is an $A$-module of finite type, $V$ is a projective $B$-module of finite type and an $A$-module of finite
presentation.*

*Then, if $V'$ and $W'$ are isomorphic as $B'$-modules, $V$ and $W$ are isomorphic as $B$-modules.*

We note that in case (ii), $W'$, being $A'$-isomorphic to $V'$, is an $A'$-module of finite type, from which it follows
that $W$ is an $A$-module of finite type (Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop. 11); hence in all cases $V$
and $W$ are $A$-modules of finite type. Furthermore:

*(2.5.8.1) Under either of the hypotheses (i), (ii), $\operatorname{Hom}_{B}(V, W)$ is an $A$-module of finite type.*

This is evident in case (i), for $\operatorname{Hom}_{A}(V, W)$ is then an $A$-module of finite type, and
$\operatorname{Hom}_{B}(V, W)$ is an $A$-sub-module of $\operatorname{Hom}_{A}(V, W)$. In case (ii), $V$ is a direct
factor of a free $B$-module $B^{n}$, so $\operatorname{Hom}_{B}(V, W)$ is a direct factor of
$\operatorname{Hom}_{B}(B^{n}, W) = W^{n}$, and since $W$ is an $A$-module of finite type, so is
$\operatorname{Hom}_{B}(V, W)$.

Put

```text
                  C = End_B(V),     M = Hom_B(V, W),
```

which are $A$-modules of finite type in cases (i) and (ii). One knows that under either of the conditions (i), (ii), the
canonical homomorphism

```text
(2.5.8.2)         Hom_A(V, W) ⊗_A A' → Hom_{A'}(V', W')
```

is bijective (Bourbaki, *Alg. comm.*, chap. II, §2, n° 10, prop. 11). Since $A'$ is a flat $A$-module,
$\operatorname{Hom}_{B}(V, W) \otimes_{A} A'$ is canonically identified with a sub-$A'$-module of
$\operatorname{Hom}_{A}(V, W) \otimes_{A} A'$. The image of this sub-module under the homomorphism `(2.5.8.2)` is
contained in $\operatorname{Hom}_{B'}(V', W')$, for if $u \in \operatorname{Hom}_{B}(V, W)$ and $a' \in A'$, the image
of $u \otimes a'$ under `(2.5.8.2)` is the homomorphism $u' : V' \to W'$ such that $u'(x \otimes 1) = u(x) \otimes a'$;
for every $b \in B$, one has $u'((b \otimes 1)(x \otimes 1)) = u'(bx \otimes 1) = u(bx) \otimes a' = b u(x) \otimes a' =
(b \otimes 1)(u(x) \otimes a')$, whence our assertion. This being so:

*(2.5.8.3) Under either of the hypotheses (i), (ii), the homomorphism*

```text
(2.5.8.4)         Hom_B(V, W) ⊗_A A' → Hom_{B'}(V', W')
```

*is bijective.*

For every $b \in B$, write $h(b)$ (resp. `h'(b)`) for the homothety $x \mapsto bx$ of $V$ (resp. $W$), which is an
$A$-endomorphism. Let $(b_{\alpha})_{\alpha \in I}$ be a system of generators of the $A$-algebra $B$; the map

```text
                  u ↦ (h'(b_α) ∘ u − u ∘ h(b_α))_α
```

from $\operatorname{Hom}_{A}(V, W)$ to $(\operatorname{Hom}_{A}(V, W))^{I}$ is $A$-linear, and by definition its kernel
is precisely $\operatorname{Hom}_{B}(V, W)$; in other words, one has an exact sequence

```text
                  0 → Hom_B(V, W) → Hom_A(V, W) → (Hom_A(V, W))^I.
```

The same reasoning applies upon replacing $A$, $B$, $V$, $W$ by $A'$, $B'$, $V'$, $W'$; moreover, one has a diagram

```text
                  0 ──→ Hom_B(V, W) ⊗_A A' ──→ Hom_A(V, W) ⊗_A A' ──→ (Hom_A(V, W))^I ⊗_A A'

(2.5.8.5)                       │ r                       │ s                          │ t
                                ↓                         ↓                            ↓

                  0 ──→ Hom_{B'}(V', W') ───→ Hom_{A'}(V', W') ───→ (Hom_{A'}(V', W'))^I
```

where $r$ is the homomorphism `(2.5.8.4)`, $s$ is the homomorphism `(2.5.8.2)`, and $t$ is the composite homomorphism

```text
                  (Hom_A(V, W))^I ⊗_A A' →w (Hom_A(V, W) ⊗_A A')^I →s^I (Hom_{A'}(V', W'))^I,
```

$w$ being the canonical homomorphism (Bourbaki, *Alg.*, chap. II, 3rd ed., §3, n° 7). One verifies at once that the
diagram `(2.5.8.5)` is commutative, and since $A'$ is a flat $A$-module its rows are exact. Finally, we have seen

<!-- original page 26 -->

that $s$ is an isomorphism, hence so is $s^{I}$; in case (ii), one may take $I$ finite, and one then knows that $w$ is
bijective (Bourbaki, *loc. cit.*, prop. 7); in case (i), one notes that if $B'$ (resp. `B''`) is the image of $B$ under
$h$ (resp. $h'$) in $\operatorname{End}_{A}(V)$ (resp. $\operatorname{End}_{A}(W)$), then $B'$ and `B''` are $A$-modules
of finite type, so one may again take $I$ finite. Thus in all cases $t$ is bijective, and one concludes that $r$ is
bijective too.

It therefore follows from `(2.5.8.4)` that, if one puts

```text
                  C' = C ⊗_A A',    M' = M ⊗_A A',
```

one has canonical bijections

```text
(2.5.8.6)         C' ≅ End_{B'}(V'),    M' ≅ Hom_{B'}(V', W'),
```

the first of which is an isomorphism of $A'$-algebras, the second forming with the first a di-isomorphism of right
$C'$-modules.

*(2.5.8.7) Reduction to the case $V = B_{d}$.* The hypothesis that $V'$ and $W'$ are isomorphic $B'$-modules implies
that $C'_{d}$ and $M'$ are isomorphic right $C'$-modules `(2.5.6)`. We show that to prove `(2.5.8)`, it suffices to find
an element $u \in M$ which is a generator of $M$ as a right $C$-module. Indeed, $u' = u \otimes 1$ will be a generator
of $M'$ as a right $C'$-module; now in case (i), $V'$ and $W'$ are $A'$-modules of finite type, hence Noetherian since
$A'$ is Noetherian; in case (ii), $V'$ and $W'$ are (isomorphic) $A'$-modules of finite presentation. One may therefore
apply `(2.5.7)` to $A'$, $B'$, $V'$, $W'$ and conclude that $u'$ is a $B'$-isomorphism of $V'$ onto $W'$. But since $A'$
is faithfully flat over $A$, this implies that $u$ is bijective $(0_{I}, 6.4.1)$, which is the conclusion of `(2.5.8)`.
Noting that in case (i), $C$ and $M$ are $A$-modules of finite type, and that in case (ii), $C$ is (as seen in
`(2.5.8.1)`) a direct factor of $V^{n}$, hence a projective $A$-module of finite type, one sees that one is reduced
(changing notation) to proving `(2.5.8)` in the particular case where $V = B_{d}$, and that it suffices to prove the
existence of a generator of the $B$-module $W$. Note that in this case $B$ is an $A$-module of finite type.

*(2.5.8.8) Reduction to the case where $A$ and $A'$ are fields, $B$ a simple $A$-algebra with centre $A$.* Let
$\mathfrak{r}$ be the radical of the semi-local ring $A$; it suffices to prove that $W/\mathfrak{r} W$ is a monogenic
$(B/\mathfrak{r} B)$-module, for if there exists a surjective homomorphism $B_{d}/\mathfrak{r} B_{d} \to W/\mathfrak{r}
W$, it gives by composition a homomorphism $B_{d} \to B_{d}/\mathfrak{r} B_{d} \to W/\mathfrak{r} W$, which itself
(since $B_{d}$ is a free $B$-module) can be written $B_{d} \to W \to W/\mathfrak{r} W$, so that the surjective
homomorphism considered is $f \otimes 1 : B_{d} \otimes_{A} (A/\mathfrak{r}) \to W \otimes_{A} (A/\mathfrak{r})$. Since
$W$ is an $A$-module of finite type, Nakayama's lemma shows that $f$ is surjective (Bourbaki, *Alg. comm.*, chap. II,
§3, n° 2, cor. 1 of prop. 4). If one puts $A_{1} = A/\mathfrak{r}$, $A'_{1} = A' \otimes_{A} A_{1} = A'/\mathfrak{r}
A'$, $B_{1} = B/\mathfrak{r} B = B \otimes_{A} A_{1}$, $W_{1} = W/\mathfrak{r} W = W \otimes_{A} A_{1}$, the hypotheses
(i) (resp. (ii)) remain satisfied when one replaces in them $A$, $A'$, $B$, $V = B_{d}$, $W$ by `A_1`, $A'_{1}$, `B_1`,
$V_{1} = (B_{1})_{d}$, `W_1` respectively; furthermore, $V'_{1} = V' \otimes_{A} A_{1} = V_{1} \otimes_{A_{1}} A'_{1}$
and $W'_{1} = W' \otimes_{A} A_{1} = W_{1} \otimes_{A_{1}} A'_{1}$ are $B'_{1}$-isomorphic (with $B'_{1} = B'
\otimes_{A} A_{1} = B_{1} \otimes_{A_{1}} A'_{1}$), and $A'_{1}$ is a faithfully flat `A_1`-module. One may therefore
suppose, for the proof of `(2.5.8)`, that $A$ is a finite product of (commutative) fields. Since $B$ is an $A$-module of
finite type, it is an Artinian ring; let $\mathfrak{N}$ be its radical. It will now suffice to prove that
$W/\mathfrak{N} W$ is a monogenic $(B/\mathfrak{N})$-module, for one sees as above, using Nakayama's lemma, that this
implies $W$ is a monogenic $B$-module; on the other hand, $W'/\mathfrak{N} W'$ is $(B'/\mathfrak{N} B')$-isomorphic to
$(B'/\mathfrak{N} B')_{d}$, and one has $B'/\mathfrak{N} B' = (B \otimes_{A} A')/(\mathfrak{N} \otimes_{A} A') =
(B/\mathfrak{N}) \otimes_{A} A'$, and likewise $W'/\mathfrak{N} W' = (W \otimes_{A} A')/(\mathfrak{N} W \otimes_{A} A')
= (W/\mathfrak{N} W) \otimes_{A} A'$. We may therefore further suppose $\mathfrak{N} = 0$, i.e. that $B$ is a
semi-simple $A$-algebra.

Note now that since $A$ is a finite product of fields $k_{i}$ ($1 \leq i \leq n$), $A'$ is a direct composite of
$k_{i}$-algebras $A'_{i}$ ($1 \leq i \leq n$), each $A'_{i}$ being annihilated by the $k_{j}$ with $j \neq i$; the
hypothesis that $A'$ is a faithfully flat $A$-module implies that the $A'_{i}$ are non-zero. Consequently, there exists
a quotient $A''_{i}$ of $A'_{i}$ which is a field, and `A''`, the direct composite of the $A''_{i}$, is a faithfully
flat $A$-module and a quotient of $A'$. Considering then the ring $B'' = B \otimes_{A} A'' = B' \otimes_{A'} A''$, $W''
= W \otimes_{A} A'' = W' \otimes_{A'} A''$ is a `B''`-module isomorphic to $B''_{d}$; one may therefore restrict to
proving `(2.5.8)` after replacing $A'$ by `A''`, i.e. one may also suppose that $A'$ is a finite product of fields.

Let $Z$ be the centre of $B$, which is a finite product of fields and an $A$-module of finite type; note that $B$ and
$W$ are $Z$-modules of finite type, projective like every $Z$-module; furthermore, one has $B' = B \otimes_{Z} Z'$ and
$W' = W \otimes_{Z} Z'$, where $Z' = Z \otimes_{A} A'$, and $Z'$ is a faithfully flat $Z$-module. One may therefore
replace $A$ by $Z$ in the hypothesis, in other words suppose that $A$ is the centre of $B$, with $B$ semi-simple and
$A'$ a finite product of fields. If $k_{i}$ ($1 \leq i \leq n$) are the field components of $A$, then $B$ is a direct
composite of simple rings $B_{i}$, $k_{i}$ being the centre of $B_{i}$, and $W$ is a direct sum of sub-modules $W_{i}$
($1 \leq i \leq n$), $W_{i}$ being annihilated by the $B_{j}$ with $j \neq i$; furthermore, the reasoning made above
shows that one may suppose that $A'$ is a product of fields $k'_{i}$ ($1 \leq i \leq n$), $k'_{i}$ being an extension of
$k_{i}$ and annihilated by the $k_{j}$ with $j \neq i$. The hypothesis that $B'_{d}$ and $W'$ are isomorphic
$B'$-modules then implies that, for

<!-- original page 27 -->

every $i$, $(B_{i} \otimes_{k_{i}} k'_{i})_{d}$ and $W_{i} \otimes_{k_{i}} k'_{i}$ are isomorphic $(B_{i}
\otimes_{k_{i}} k'_{i})$-modules; it therefore suffices to prove `(2.5.8)` when $n = 1$, i.e. in the case where $A$ and
$A'$ are fields and $B$ is a simple algebra with centre $A$.

*(2.5.8.9) End of the proof.* One knows (Bourbaki, *Alg.*, chap. VIII, §5, props. 6 and 8) that every $B$-module is a
direct sum of modules isomorphic to a minimal ideal of $B$, and two $B$-modules of finite rank over $A$ are therefore
isomorphic if and only if they have the same rank over $A$. By hypothesis, one has $[W' : A'] = [B'_{d} : A']$. But
$[W' : A'] = [W : A]$ and $[B'_{d} : A'] = [B_{d} : A]$; hence $[W : A] = [B_{d} : A]$, which finishes the proof.

### 2.6. Permanence of set-theoretic and topological properties of morphisms under faithfully flat descent

**Proposition (2.6.1).**

<!-- label: IV.2.6.1 -->

*Let $f : X \to Y$ be an $S$-morphism of $S$-preschemes, $g : S' \to S$ a surjective morphism, $X' = X_{(S')}$, $Y' =
Y_{(S')}$, $f' = f_{(S')} : X' \to Y'$. Consider, for a morphism, the property of being:*

*(i) surjective;*

*(ii) injective;*

*(iii) with finite fibres (as sets);*

*(iv) bijective;*

*(v) radicial.*

*Then, if $P$ denotes one of the preceding properties and $f'$ possesses the property $P$, the same holds for $f$.*

Since the projection morphism $Y' \to Y$ is itself surjective `(I, 3.5.2)`, one may, by virtue of `(I, 3.3.11)`,
restrict to the case where $Y = S$, $Y' = S'$. For every $y \in Y$ (resp. $y' \in Y'$) denote by $X_{y}$ (resp.
$X'_{y'}$) the fibre prescheme $f^{-1}(y)$ (resp. $f'^{-1}(y')$) `(I, 3.6.2)`; one knows that for $y' \in Y'$ over $y =
g(y')$ one has a canonical isomorphism $X'_{y'} \cong X_{y} \otimes_{k(y)} k(y')$ `(I, 3.6.4)`; since the morphism
$\operatorname{Spec}(k(y')) \to \operatorname{Spec}(k(y))$ is surjective, so is the projection $X'_{y'} \to X_{y}$
`(I, 3.5.2)`. Hence if $X'_{y'}$ is non-empty (resp. has at most one point, resp. is a finite set), so is $X_{y}$; since
$g : Y' \to Y$ is surjective, this proves the proposition in cases (i), (ii) and (iii), and (iv) follows from (i) and
(ii). Finally, to prove (v), it suffices to show that if $f'$ is universally injective `(I, 3.5.11)`, then so is $f$;
now let $Y_{1} \to Y$ be an arbitrary morphism; put $X_{1} = X \times_{Y} Y_{1}$ and $f_{1} = f_{(Y_{1})}$. On the other
hand, put $Y'_{1} = Y_{1} \times_{Y} Y'$, $X'_{1} = X' \times_{Y'} Y'_{1} = X_{1} \times_{Y_{1}} Y'_{1}$, $f'_{1} =
f_{(Y'_{1})} = (f_{1})_{(Y'_{1})} : X'_{1} \to Y'_{1}$; since $g_{1} = g_{(Y_{1})} : Y'_{1} \to Y_{1}$ is surjective
`(I, 3.5.2)` and $f'$ is universally injective, $f'_{1}$ is injective, and it follows from (ii) that $f_{1}$ is
injective, whence our assertion.

**Proposition (2.6.2).**

<!-- label: IV.2.6.2 -->

*The notations being those of `(2.6.1)`, suppose the morphism $g : S' \to S$ faithfully flat and quasi-compact.
Consider, for a morphism, the property of being:*

*(i) open;*

*(ii) closed;*

*(iii) quasi-compact and a homeomorphism onto the image subspace;*

*(iv) a homeomorphism.*

*Then, if $P$ denotes one of the preceding properties and $f'$ possesses the property $P$, the same holds for $f$.*

<!-- original page 28 -->

Since the morphism $Y' \to Y$ is faithfully flat and quasi-compact `(2.2.13` and `1.1.2)`, one may, by virtue of
`(I, 3.3.11)`, restrict to the case where $Y = S$, $Y' = S'$. If $g'$ is the projection $X' \to X$, one knows that for
every subset $M$ of $X$, one has $g^{-1}(f(M)) = f'(g'^{-1}(M))$ `(I, 3.4.8)`. If $f'$ is an open (resp. closed)
morphism, then, for every open (resp. closed) subset $M$ of $X$, $f'(g'^{-1}(M))$ is open (resp. closed) in $Y'$, and
since $g$ is faithfully flat and quasi-compact, one concludes that $f(M)$ is open (resp. closed) in $Y$ by virtue of
`(2.3.12)`. This proves the proposition in cases (i) and (ii). Let us prove it in case (iii) (which will imply case
(iv), taking `(2.6.1, (iv))` into account). By virtue of `(2.6.1, (ii))`, $f$ is injective, and it remains to prove that
$f$, viewed as a map of $X$ onto $f(X)$, is a quasi-compact and open map. Since $f'$ is quasi-compact, so is $f$
`(1.1.4)`. It therefore suffices to prove that for every closed subset $Z$ of $X$, one has $Z = f^{-1}(f(Z))$; since
$g'$ is surjective, this relation is equivalent to $g'^{-1}(Z) = g'^{-1}(f^{-1}(f(Z)))$, or again to $g'^{-1}(Z) =
f'^{-1}(g^{-1}(f(Z)))$. Now, since $f$ is quasi-compact, so is its composite with the canonical injection $Z \to X$ ($Z$
here being the reduced closed sub-prescheme of $X$ having $Z$ as underlying space). Applying `(2.3.10)` to the subset
$f(Z)$ of $Y$ (the image of the morphism $f|Z$), one obtains $g^{-1}(f(Z)) = f'(g'^{-1}(Z))$; the formula to be proved
therefore amounts to $Z' = f'^{-1}(f'(Z'))$, where $Z' = g'^{-1}(Z)$; but this formula follows from the hypothesis that
$f'$ is a homeomorphism of $X'$ onto `f'(X')`.

**Remark (2.6.3).**

<!-- label: IV.2.6.3 -->

*In cases (i) and (ii), the conclusions of `(2.6.2)` remain valid when one supposes only $g$ quasi-faithfully flat
`(2.3.3)` and quasi-compact; indeed, by virtue of `(2.1.4)`, `(I, 3.5.2)` and `(I, 9.1.13.1)`, one may again reduce to
the case where $Y = S$, $Y' = S'$; the conclusion then follows from `(2.3.12)`. In cases (iii) and (iv), the conclusions
remain valid when one supposes only $g$ quasi-faithfully flat, provided one supposes additionally that $f'$ is
quasi-compact; indeed, one then uses only `(2.3.10)` and the fact that $g$ is surjective. Finally, if $g$ is faithfully
flat and locally of finite presentation, or if $g$ is surjective and $S$ discrete, the conclusion of `(2.6.2)` is valid
when $P$ is the property:*

*(iii bis) being a homeomorphism onto the image subspace;*

*this results indeed from the proof given in `(2.6.2)` and from Remark `(2.4.11)`.*

**Corollary (2.6.4).**

<!-- label: IV.2.6.4 -->

*The notations being those of `(2.6.1)`, suppose the morphism $g : S' \to S$ faithfully flat and quasi-compact. Consider
for a morphism the property of being:*

*(i) universally open;*

*(ii) universally closed;*

*(iii) quasi-compact and universally bicontinuous;*

*(iv) a universal homeomorphism;*

*(v) quasi-compact;*

*(vi) quasi-compact and dominant.*

*Then, if $P$ denotes one of the preceding properties, for $f$ to possess the property $P$, it is necessary and
sufficient that $f'$ possess it.*

<!-- original page 29 -->

Properties (v) and (vi) are mentioned only for the record, being consequences of `(1.1.4)`, `(1.1.6)` and `(2.3.7)`. As
for the others, the condition is necessary by virtue of `(2.4.3)`. Conversely, suppose for instance that $f'$ is
universally open, and let $Y_{1} \to Y$ be an arbitrary morphism; put $X_{1} = X \times_{Y} Y_{1}$ and $f_{1} =
f_{(Y_{1})}$. On the other hand, put $Y'_{1} = Y_{1} \times_{Y} Y'$, $X'_{1} = X' \times_{Y'} Y'_{1} = X_{1}
\times_{Y_{1}} Y'_{1}$, $f'_{1} = f'_{(Y'_{1})} = (f_{1})_{(Y'_{1})} : X'_{1} \to Y'_{1}$; since $g_{1} = g_{(Y'_{1})} :
Y'_{1} \to Y_{1}$ is faithfully flat and quasi-compact `(2.2.13` and `1.1.2)` and $f'$ is universally open, $f'_{1}$ is
open, and it follows from `(2.6.2)` that $f_{1}$ is open; hence $f$ is universally open. The same reasoning applies in
the other cases.

One notes again here that one may replace "faithfully flat" by "quasi-faithfully flat", and, when $g$ is additionally
locally of finite presentation, or when $g$ is surjective and $S$ discrete, one may replace property (iii) by:

*(iii bis) universally bicontinuous.*

### 2.7. Permanence of various properties of morphisms under faithfully flat descent

**Proposition (2.7.1).**

<!-- label: IV.2.7.1 -->

*Let $f : X \to Y$ be an $S$-morphism of $S$-preschemes, $g : S' \to S$ a faithfully flat and quasi-compact morphism,
$X' = X_{(S')}$, $Y' = Y_{(S')}$, $f' = f_{(S')} : X' \to Y'$. Consider, for a morphism, the property of being:*

*(i) separated;*

*(ii) quasi-separated;*

*(iii) locally of finite type;*

*(iv) locally of finite presentation;*

*(v) of finite type;*

*(vi) of finite presentation;*

*(vii) proper;*

*(viii) an isomorphism;*

*(ix) a monomorphism;*

*(x) an open immersion;*

*(xi) a quasi-compact immersion;*

*(xii) a closed immersion;*

*(xiii) affine;*

*(xiv) quasi-affine;*

*(xv) finite;*

*(xvi) quasi-finite;*

*(xvii) integral.*

*Then, if $P$ denotes one of the preceding properties, for $f$ to possess the property $P$, it is necessary and
sufficient that $f'$ possess it.*

It has been proved in chapters I, II, and in chapter IV §1, that if $f$ possesses one of the above properties $P$, the
same holds for $f'$ (without any hypothesis on the morphism $g : S' \to S$). It therefore remains to prove the converse;
since the projection $Y' \to Y$ is

<!-- original page 30 -->

a faithfully flat and quasi-compact morphism `(2.2.13` and `1.1.2)`, one may restrict to the case where $S = Y$, $S' =
Y'$ by virtue of `(I, 3.3.11)`.

(i) To say that $f$ is separated means that the diagonal morphism $\Delta_{f} : X \to X \times_{Y} X$ is closed; since
$\Delta_{f'} = (\Delta_{f})_{(Y')}$ `(I, 5.3.4)`, if $\Delta_{f'}$ is closed, so is $\Delta_{f}$ by virtue of `(2.6.2)`,
hence $f$ is separated.

(ii) has already been proved under weaker hypotheses `(1.2.5)`.

(iii) and (iv): The question is evidently local on $X$ and $Y$, and, taking `(2.2.12)` into account, it therefore
suffices to prove the

**Lemma (2.7.1.1).**

<!-- label: IV.2.7.1.1 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $A'$ an $A$-algebra which is a faithfully flat $A$-module, $B' = B \otimes_{A}
A'$. For $B$ to be an $A$-algebra of finite type (resp. of finite presentation), it is necessary and sufficient that
$B'$ be an $A'$-algebra of finite type (resp. of finite presentation).*

One knows already that the condition is necessary without any hypothesis on $A$ `(1.3.4, 1.3.6, 1.4.3, 1.4.6)`. Suppose
that $B'$ is an $A'$-algebra of finite type; let $(B_{\alpha})_{\alpha \in I}$ be the filtered increasing family of
$A$-sub-algebras of $B$, so that $B = \lim B_{\alpha}$, and therefore also $B' = \lim (B_{\alpha} \otimes_{A} A')$,
since the tensor product commutes with inductive limits; if $(x'_{i})$ is a finite system of generators of the
$A'$-algebra $B'$, there exists an index $\alpha$ such that all the $x'_{i}$ belong to the sub-algebra $B_{\alpha}
\otimes_{A} A'$ of $B'$, whence $B' = B_{\alpha} \otimes_{A} A'$, and since $A'$ is faithfully flat, $B = B_{\alpha}$
$(0_{I}, 6.4.1)$.

Suppose now that $B'$ is an $A'$-algebra of finite presentation; one knows already from what precedes that $B$ is an
$A$-algebra of finite type, so there exists a polynomial $A$-algebra $C = A[T_{1}, \cdots, T_{n}]$ and a surjective
$A$-homomorphism of algebras $C \to B$; let $\mathfrak{j}$ be the kernel of this homomorphism, so that one has an exact
sequence $0 \to \mathfrak{j} \to C \to B \to 0$, and therefore also an exact sequence $0 \to \mathfrak{j}' \to C' \to B'
\to 0$ (since $A'$ is $A$-flat), upon putting $C' = C \otimes_{A} A' = A'[T_{1}, \cdots, T_{n}]$ and $\mathfrak{j}' =
\mathfrak{j} \otimes_{A} A'$ (identified with an ideal of $C'$). Since $B'$ is an $A'$-algebra of finite presentation,
$\mathfrak{j}'$ is a $C'$-module of finite type `(1.4.4)`; but one has $\mathfrak{j}' = \mathfrak{j} \otimes_{C} C'$,
and $C'$ is a faithfully flat $C$-module `(2.2.13` and `2.2.3)`; one knows then that the hypothesis that $\mathfrak{j}'$
is a $C'$-module of finite type implies that $\mathfrak{j}$ is a $C$-module of finite type (Bourbaki, *Alg. comm.*,
chap. I, §3, n° 6, prop. 11); hence $B$ is an $A$-algebra of finite presentation.

(v) follows from (iii) and from `(2.6.2, (v))` by virtue of `(1.5.2)`.

(vi) follows similarly from (iv), (v) and (ii) by virtue of `(1.6.1)`.

(vii) follows from (i), (v) and `(2.6.4, (ii))` `(II, 5.4.1)`.

(viii) Note first that since $f'$ is an isomorphism, it is a universal homeomorphism, so the same is true of $f$
`(2.6.4)`; one already concludes that $f$ is quasi-compact and separated `(2.4.4)`. Write $f = (\psi, \theta)$, where
$\psi$ is therefore a homeomorphism; it must be proved that $\theta : \mathcal{O}_{Y} \to f_{*}(\mathcal{O}_{X})$ is an
isomorphism of $\mathcal{O}_{Y}$-Modules. Now, if one writes $f' = (\psi', \theta')$, the homomorphism $\theta' :
\mathcal{O}_{Y'} \to f'_{*}(\mathcal{O}_{X'})$ is composed of the canonical homomorphism $g*(f_{*}(\mathcal{O}_{X})) \to
f'_{*}(\mathcal{O}_{X'})$ and of $g*(\theta)$ `(2.3.2)`; but the first of these two homomorphisms is bijective by virtue
of the hypothesis on $g$ `(2.3.1)`, so if $\theta'$ is bijective,

<!-- original page 31 -->

so is $g*(\theta)$, and since $g$ is faithfully flat, $\theta$ is bijective `(2.2.7)`, which proves (viii).

(ix) The proposition follows from (viii), from `(I, 5.3.4)`, and from `(I, 5.3.8)`, which reduces monomorphisms to
isomorphisms.

(x) If $f'$ is an open immersion, `f'(X')` is open in $Y'$, and one has $f'(X') = g^{-1}(f(X))$ `(I, 3.4.8)`; it follows
from `(2.3.12)` that $f(X)$ is open. One may then replace $Y$ (resp. $Y'$) by the sub-prescheme induced on the open set
$f(X)$ (resp. `f'(X')`), taking `(1.1.2)` and `(2.2.13)` into account; then $f'$ becomes an isomorphism, hence the same
is true of $f$ by (viii), and this establishes (x).

(xi) If $f'$ is a quasi-compact immersion, $f'$ is a quasi-compact and quasi-separated morphism `(1.2.2)`, so the same
holds for $f$ by (ii) and `(2.6.2, (v))`. Let $Z$ be the sub-prescheme of $Y$ closed image of $X$ under $f$ `(1.7.8)`,
and put $f = j \circ g$, where $j : Z \to Y$ is the canonical injection; one then has $f' = j' \circ g'$ with $j' =
j_{(Y')}$, $g' = g_{(Y')}$, and one knows that $j'$ identifies with the canonical injection $Z' \to Y'$ of the
sub-prescheme $Z'$ of $Y'$, the closed image of $X'$ under $f'$ `(2.3.2)`. The hypothesis on $f'$ then means that $g'$
is an open immersion `(I, 9.5.10)`, hence the same holds for $g$ by (x), and this shows that $f$ is an immersion.

(xii) To say that $f'$ (resp. $f$) is a closed immersion means that $f'$ (resp. $f$) is a quasi-compact immersion and a
closed morphism; one therefore sees that (xii) follows from (xi) and from `(2.6.2, (ii))`.

(xiii) and (xiv) Suppose $f'$ affine (resp. quasi-affine); note then that $f'$ is quasi-compact and quasi-separated
`(II, 5.1.1)`, so the same holds for $f$ by (ii) and `(2.6.2, (v))`. Put $\mathcal{A} = f_{*}(\mathcal{O}_{X})$,
$\mathcal{A}' = f'_{*}(\mathcal{O}_{X'})$; by virtue of `(2.3.1)`, the canonical homomorphism of
$\mathcal{O}_{Y'}$-Algebras $g*(\mathcal{A}) \to \mathcal{A}'$ is bijective; consequently, if $h : Z =
\operatorname{Spec}(\mathcal{A}) \to Y$ is the structure morphism, the structure morphism $h' : Z' =
\operatorname{Spec}(\mathcal{A}') \to Y'$ identifies with $h_{(Y')}$ `(II, 1.5.2)`. Let then $u : X \to Z$ (resp. $u' :
X' \to Z'$) be the canonical $Y$-morphism (resp. $Y'$-morphism) corresponding to the identity homomorphism of
$\mathcal{A}$ (resp. $\mathcal{A}'$) `(II, 1.2.7)`; since one has the commutative diagram

```text
                       X  ←—— X'
                       │       │
                       u│      │u'
                       ↓       ↓
                       Z  ←—— Z'
                       │       │
                       h│      │h'
                       ↓       ↓
                       Y  ←—— Y'
                          g
```

and $h' \circ u' = f'$, it follows from `(II, 1.2.7)` that $u' = u_{(Y')}$. Moreover, $g'$ is faithfully flat and
quasi-compact `(1.1.2` and `2.2.13)`. This being so, the hypothesis on $f'$ means that $u'$ is an isomorphism (resp. an
open immersion) `(II, 5.1.6)`; it then follows from (viii) (resp. (x)) that $u$ is an isomorphism (resp. an open
immersion), whence (xiii) (resp. (xiv)).

<!-- original page 32 -->

(xv) If $f'$ is finite, it is affine, hence so is $f$ by (xiii); furthermore, with the notations of the proof of (xiii),
$\mathcal{A}'$ is an $\mathcal{O}_{Y'}$-Module of finite type, and $\mathcal{A}'$ is isomorphic to $g*(\mathcal{A})$; it
follows from `(2.5.2)` that $\mathcal{A}$ is an $\mathcal{O}_{Y}$-Module of finite type, hence $f$ is a finite morphism.

(xvi) To say that $f$ is quasi-finite means that $f$ is a morphism of finite type and that for every $y \in Y$,
$f^{-1}(y)$ is finite `(II, 6.2.2` and `I, 6.4.4)`; the conclusion therefore follows from (v) and (xv).

(xvii) One sees as in (xv) that $f$ is affine. One may restrict to the case where $Y = \operatorname{Spec}(A)$, $Y' =
\operatorname{Spec}(A')$, and then $X = \operatorname{Spec}(B)$, $X' = \operatorname{Spec}(B')$, where $B' = B
\otimes_{A} A'$; $B$ is equal to the inductive limit of its $A$-sub-algebras of finite type $B_{\alpha}$, so one has $B'
= \lim B'_{\alpha}$, where $B'_{\alpha} = B_{\alpha} \otimes_{A} A'$, and $B'_{\alpha}$ is an $A'$-algebra of finite
type. But by hypothesis $B'$ is integral over $A'$, so $B'_{\alpha}$ is an $A'$-module of finite type, and $B_{\alpha}$
is therefore an $A$-module of finite type `(2.5.2)`. Q.E.D.

**Corollary (2.7.2).**

<!-- label: IV.2.7.2 -->

*The hypotheses and notations being those of `(2.7.1)`, suppose $f$ quasi-compact; let $\mathcal{L}$ be an invertible
$\mathcal{O}_{X}$-Module, $\mathcal{L}' = \mathcal{L} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$ its inverse image. For
$\mathcal{L}$ to be ample (resp. very ample) for $f$, it is necessary and sufficient that $\mathcal{L}'$ be ample (resp.
very ample) for $f'$.*

The condition is necessary without any hypothesis on $g : S' \to S$ `(II, 4.4.10` and `4.6.13)`; to see that it is
sufficient, one may, as in `(2.7.1)`, restrict to the case where $S = Y$, $S' = Y'$. The hypothesis on $\mathcal{L}'$
implies that $f'$ is quasi-compact and separated `(II, 4.6.1)`, hence the same holds for $f$ (by `(2.6.2, (v))` and
`(2.7.1, (i))`). Put $\mathcal{E} = f_{*}(\mathcal{L})$, $\mathcal{E}' = f'_{*}(\mathcal{L}')$; it follows from
`(2.3.1)` that the canonical homomorphism $u : g*(\mathcal{E}) \to \mathcal{E}'$ is bijective. If $\mathcal{L}'$ is very
ample for $f'$, the canonical homomorphism $\sigma' : f'*(\mathcal{E}') \to \mathcal{L}'$ is surjective, and the
morphism $r' = r_{\mathcal{E}', \mathcal{L}'} : X' \to P(\mathcal{E}')$ is an immersion `(II, 4.4.4, b))`, necessarily
quasi-compact `(1.1.2, (v))`. The fact that $u : g*(\mathcal{E}) \to \mathcal{E}'$ is bijective implies that, if $h :
P(\mathcal{E}) \to Y$, $h' : P(\mathcal{E}') \to Y'$ are the structure morphisms, then $h'$ identifies with $h_{(Y')}$
`(II, 4.1.3)`. On the other hand, denoting by $g'$ the projection $X' \to X$, $g'$ is faithfully flat `(2.2.13)`, one
has $f \circ g' = g \circ f'$, and one verifies easily that the homomorphism $g'*(f*(\mathcal{E})) \cong
f'*(g*(\mathcal{E})) \to f'*(\mathcal{E}')$ is identical with the composite homomorphism

$$ g'*(f*(f_{*}(\mathcal{L}))) \to g'*(\mathcal{L}) \to \mathcal{L}' $$

(for example by reducing to the case where $Y$ and $Y'$ are affine). Since $\sigma'$ is surjective and $f'*(u)$ is
bijective, one sees that $g'*(\sigma)$ is surjective, hence the same is true of $\sigma$ `(2.2.7)`. One concludes that
the morphism $r = r_{\mathcal{E}, \mathcal{L}} : X \to P(\mathcal{E})$ is everywhere defined `(II, 3.7.4)`; furthermore,
if one puts $P = P(\mathcal{E})$, $P' = P(\mathcal{E}')$ and if `g''` is the projection $P' \to P$, then $r'$ identifies
with $r_{(Y')}$ `(II, 4.2.10)` and `g''` is faithfully flat and quasi-compact `(1.1.2` and `2.2.13)`. One therefore
concludes from `(2.7.1, (xi))` that $r$ is an immersion, and consequently $\mathcal{L}$ is very ample `(II, 4.4.4, b))`.

Suppose now that $\mathcal{L}'$ is ample for $f'$; to prove that $\mathcal{L}$ is ample for $f$, one may restrict to the
case where $Y$ is affine `(II, 4.6.4)`, and by virtue of `(2.2.12)` and `(II, 4.6.13)`, one may also suppose that $Y'$
is affine. Then $X$ and $X'$ are

<!-- original page 33 -->

quasi-compact schemes, and to prove that $\mathcal{L}$ is $f$-ample, one may apply the criterion of `(II, 4.6.8, a))`.
Let then $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module of finite type; if $\sigma : f*(f_{*}(\mathcal{F}
\otimes \mathcal{L}^{\otimes n})) \to \mathcal{F} \otimes \mathcal{L}^{\otimes n}$ is the canonical homomorphism, one
sees as above that $g'*(\sigma)$ is the composite homomorphism

```text
                  f'*(g*(f_*(ℱ ⊗ ℒ^{⊗ n}))) →u f'*(f'_*(ℱ' ⊗ ℒ'^{⊗ n})) →σ' ℱ' ⊗ ℒ'^{⊗ n},
```

upon putting $\mathcal{F}' = g'*(\mathcal{F})$, taking $(0_{I}, 4.3.3.1)$ into account and denoting by $u$ the canonical
homomorphism $g*(f_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n})) \to f'_{*}(g'*(\mathcal{F} \otimes
\mathcal{L}^{\otimes n}))$. Now, one knows that $u$ is bijective for every $n$ `(2.3.1)`; on the other hand, since
$\mathcal{F}$ is quasi-coherent and of finite type, the hypothesis that $\mathcal{L}'$ is ample for $f'$ implies the
existence of an $n_{0}$ such that $\sigma'$ is surjective for $n \geq n_{0}$; one therefore sees that $g'*(\sigma)$ is
surjective for $n \geq n_{0}$, and since $g'$ is faithfully flat, $\sigma$ is surjective for these values of $n$
`(2.2.7)`, which completes the proof.

**Remarks (2.7.3).**

<!-- label: IV.2.7.3 -->

*(i) It follows from `(2.6.1)`, `(2.6.4)` and `(2.5.4.1)` that the conclusions of `(2.7.1)` are still valid in cases
(i), (iii), (v), (vii) and (xvi) when one supposes only that $g$ is quasi-compact and quasi-faithfully flat `(2.3.3)`;
we have already remarked that `(2.7.1)` is valid in case (ii) under the sole hypothesis that $g$ is surjective and
quasi-compact.*

*(ii) With the notations and hypotheses of `(2.7.1)`, it may happen that $f$ is proper and $f'$ projective without $f$
being quasi-projective. Indeed, Hironaka [34] has given an example of a proper, non-projective morphism $f : X \to Y$,
where $X$ and $Y$ are two regular algebraic schemes $(0_{I}, 4.1.4)$ over the same field $k$, with $Y$ projective over
$k$; furthermore, $Y$ is the union of two affine open sets $Y_{i}$ ($i = 1, 2$) such that $f : X \times_{Y} Y_{i} \to
Y_{i}$ is projective for $i = 1, 2$. Let then $Y' = Y_{1} \amalg Y_{2}$ be the sum prescheme; it is clear that the
canonical morphism $g : Y' \to Y$, coinciding with the canonical injections on `Y_1` and `Y_2`, is faithfully flat, and
is quasi-compact by virtue of `(I, 5.5.10)`; yet, although $f' : X \times_{Y} Y' \to Y'$ (coinciding with $f_{i}$ on
each of the $Y_{i}$) is projective `(II, 5.5.6)`, the same is not true of $f$. There therefore exists an invertible
$\mathcal{O}_{X'}$-Module $\mathcal{L}'$ which is $f'$-ample but is not of the form $g'*(\mathcal{L})$ for an invertible
$\mathcal{O}_{X}$-Module $\mathcal{L}$, by virtue of `(2.7.2)`.*

*(iii) Under the hypotheses of `(2.7.1)`, it may happen that $f'$ is a local isomorphism without $f$ being a local
immersion. Indeed, let $k$ be a field, $\bar{k}$ an algebraic closure of $k$, $K$ a separable extension of finite degree
of $k$, distinct from $k$; then the structure morphism $f : X \to Y$, where $X = \operatorname{Spec}(K)$ and $Y =
\operatorname{Spec}(k)$, is not a local immersion, but if one takes $Y' = \operatorname{Spec}(\bar{k})$, the morphism
$Y' \to Y$ is faithfully flat and quasi-compact, and $f' = f_{(Y')}$ is a local isomorphism, since $X' = X \times_{Y}
Y'$ is a sum of a finite number of schemes isomorphic to $Y'$.*

### 2.8. Preschemes over a regular base of dimension 1; closure of a closed sub-prescheme of the generic fibre

**Proposition (2.8.1).**

<!-- label: IV.2.8.1 -->

*Let $Y$ be a locally Noetherian, regular, irreducible prescheme of dimension 1, with generic point $\eta$, $f : X \to
Y$ a morphism, $X_{\eta} = f^{-1}(\eta)$ the fibre at the*

<!-- original page 34 -->

*generic point, $i : X_{\eta} \to X$ the canonical morphism. Let $\mathcal{F}$ be a quasi-coherent
$\mathcal{O}_{X}$-Module, $\mathcal{F}_{\eta} = i*(\mathcal{F})$, $\mathcal{G}_{\eta}$ an
$\mathcal{O}_{X_{\eta}}$-Module quotient of $\mathcal{F}_{\eta}$, and let $\mathcal{G}$ be the $\mathcal{O}_{X}$-Module
image of $\mathcal{F}$ under the composite homomorphism \`(0_I, 4.4.3.2)*

```text
                  ℱ →ρ i_*(i*(ℱ)) = i_*(ℱ_η) → i_*(𝒢_η).
```

*Then $\mathcal{G}$ is a quasi-coherent and $f$-flat $\mathcal{O}_{X}$-Module quotient of $\mathcal{F}$, such that
$i*(\mathcal{G}) = \mathcal{G}_{\eta}$, and it is the unique $\mathcal{O}_{X}$-Module quotient of $\mathcal{F}$ having
these properties.*

Since $i$ is quasi-compact and quasi-separated `(1.1.2` and `1.2.2)`, it follows from `(1.7.4)` that for every
quasi-coherent $\mathcal{O}_{X_{\eta}}$-Module $\mathcal{H}$, $i_{*}(\mathcal{H})$ is a quasi-coherent
$\mathcal{O}_{X}$-Module; furthermore, for every open $U$ of $X$, one has $(i_{*}(\mathcal{H}))(U) =
(i_{*}(\mathcal{H}|U \cap X_{\eta}))(U \cap X_{\eta}) = \mathcal{H}(U \cap X_{\eta})$ by definition $(0_{I}, 3.4.1)$. If
one proves the proposition when $X$ and $Y$ are affine, it will follow by gluing in the general case, in view of the
uniqueness assertion valid in the affine case. In other words, one is reduced to proving the

**Lemma (2.8.1.1).**

<!-- label: IV.2.8.1.1 -->

*Let $A$ be a regular Noetherian ring `(0, 17.3.6)`, integral and of dimension 1, $K$ its field of fractions, $M$ an
$A$-module, $N'_{\eta}$ a $K$-module quotient of $M_{(K)} = M \otimes_{A} K$ by a sub-$K$-module $P'$, $N$ the image of
$M$ under the composite homomorphism $M \to M_{(K)} \to N'_{\eta}$. Then $N$ is a flat $A$-module, and it is the unique
quotient module $N$ of $M$ which is a flat $A$-module and such that the kernel of the surjective homomorphism $M_{(K)}
\to N_{(K)}$ equals $P'$.*

Since for every maximal ideal $\mathfrak{m}$ of $A$, $A_{\mathfrak{m}}$ is a regular local ring of dimension 1, hence a
discrete valuation ring, it amounts to the same thing to say that an $A$-module $N$ is flat or that it is torsion-free
$(0_{I}, 6.3.4)$. Since $N'_{\eta}$ is a $K$-vector space, it is a torsion-free $A$-module, so the same is true of $N$,
a sub-module of $N'_{\eta}$; furthermore, it is immediate to verify that $N_{(K)}$ identifies with $N'_{\eta}$.
Conversely, if $N$ is a quotient $A$-module of $M$ having the properties of the statement, the fact that $N$ is a flat
$A$-module implies that the canonical homomorphism $N \to N_{(K)} = N \otimes_{A} K$ is injective. Since $N_{(K)}$
identifies with $N'_{\eta}$, the conclusion follows from the commutativity of the diagram

```text
                  M     ──→  N
                  │           │
                  ↓           ↓
                  M_{(K)} ──→ N_{(K)}.
```

**Corollary (2.8.2).**

<!-- label: IV.2.8.2 -->

*Under the conditions of `(2.8.1)`, for $\mathcal{F}$ to be $f$-flat, it is necessary and sufficient that the canonical
homomorphism $\mathcal{F} \to i_{*}(i*(\mathcal{F})) = i_{*}(\mathcal{F}_{\eta})$ be injective.*

**(2.8.3)**

<!-- label: IV.2.8.3 -->

The formation of the $\mathcal{O}_{X}$-Module $\mathcal{G}$ is functorial in $\mathcal{F}$ and $\mathcal{G}_{\eta}$:
more precisely, if $\mathcal{F}_{1}$, $\mathcal{F}_{2}$ are two quasi-coherent $\mathcal{O}_{X}$-Modules, $u :
\mathcal{F}_{1} \to \mathcal{F}_{2}$ an $\mathcal{O}_{X}$-homomorphism, $\mathcal{G}_{\eta,i}$ an
$\mathcal{O}_{X_{\eta}}$-Module quotient of $(\mathcal{F}_{i})_{\eta}$ ($i = 1, 2$) and $v : \mathcal{G}_{\eta,1} \to
\mathcal{G}_{\eta,2}$ a homomorphism making the diagram

```text
                  (ℱ_1)_η ──→ (ℱ_2)_η
                       │          │
                       ↓          ↓
                  𝒢_{η,1}  ──v──→ 𝒢_{η,2}
```

<!-- original page 35 -->

commutative (homomorphism uniquely determined (when it exists) by this property), then the diagram

```text
                  ℱ_1            ──→         ℱ_2
                       │                          │
                       ↓                          ↓
                  i_*(𝒢_{η,1})  ──i_*(v)──→  i_*(𝒢_{η,2})
```

is commutative, and consequently there is a unique homomorphism $w : \mathcal{G}_{1} \to \mathcal{G}_{2}$ making the
diagram

```text
                  ℱ_1   ──→  ℱ_2
                       │          │
                       ↓          ↓
                  𝒢_1  ──w──→ 𝒢_2
```

commutative.

**Proposition (2.8.4).**

<!-- label: IV.2.8.4 -->

*The hypotheses on $Y$ being those of `(2.8.1)`, let `X_1`, `X_2` be two $Y$-preschemes, $\mathcal{F}_{i}$ a
quasi-coherent $\mathcal{O}_{X_{i}}$-Module, $\mathcal{G}_{\eta,i}$ an $\mathcal{O}_{(X_{i})_{\eta}}$-Module quotient of
$(\mathcal{F}_{i})_{\eta}$ ($i = 1, 2$). Then one has*

```text
(2.8.4.1)         (𝒢_{η,1} ⊠_{k(η)} 𝒢_{η,2})^∼ = 𝒢_1 ⊠_Y 𝒢_2.
```

Indeed, put $X = X_{1} \times_{Y} X_{2}$; the left-hand side of `(2.8.4.1)` is a quasi-coherent $\mathcal{O}_{X}$-Module
which is $Y$-flat $(0_{I}, 6.2.1)$, whose inverse image in $X_{\eta}$ is $\mathcal{G}_{\eta,1} \boxtimes
\mathcal{G}_{\eta,2}$ `(I, 9.1.5)`, and which is a quotient of $\mathcal{F}_{1} \boxtimes_{Y} \mathcal{F}_{2}$; the
conclusion therefore follows from the uniqueness property of `(2.8.1)`.

**Proposition (2.8.5).**

<!-- label: IV.2.8.5 -->

*The hypotheses on $X$ and $Y$ being those of `(2.8.1)`, let $Z'$ be a closed sub-prescheme of $X_{\eta}$. There then
exists a unique closed sub-prescheme $\bar{Z}$ of $X$ which is $Y$-flat and such that $i^{-1}(\bar{Z}) = Z'$.*

If $\mathcal{J}'$ is the quasi-coherent Ideal of $\mathcal{O}_{X_{\eta}}$ defining $Z'$, it suffices to apply `(2.8.1)`
to the case where $\mathcal{F} = \mathcal{O}_{X}$ and $\mathcal{G}_{\eta} = \mathcal{O}_{X_{\eta}}/\mathcal{J}'$; if
$\mathcal{G} = \mathcal{O}_{X}/\bar{\mathcal{J}}$, one has indeed $\mathcal{J}' = i*(\bar{\mathcal{J}})$, so
$i^{-1}(\bar{Z}) = Z'$ `(I, 4.4.5)`.

One notes that the prescheme $\bar{Z}$ is the closed image of $Z'$ under the composite morphism $Z' \to X_{\eta} \to X$,
where the first arrow is the canonical injection `(I, 9.5.3)`; its underlying space is the closure in $X$ of $Z'$
`(I, 9.5.4)`, which justifies the notation adopted. One also says that $\bar{Z}$ is the **closure sub-prescheme** of
$Z'$ in $X$.

**Corollary (2.8.6).**

<!-- label: IV.2.8.6 -->

*Let `X_1`, `X_2` be two $Y$-preschemes, $Z'_{i}$ a closed sub-prescheme of $(X_{i})_{\eta}$ ($i = 1, 2$). Then one has*

```text
(2.8.6.1)         (Z'_1 ×_{k(η)} Z'_2)^− = Z̄_1 ×_Y Z̄_2.
```

This results from `(2.8.4)` and `(2.8.5)`.
