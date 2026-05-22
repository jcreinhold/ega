# Chapter 0_III

## §12. Complements on the cohomology of sheaves

<!-- original page 49 -->

### 12.1. Cohomology of sheaves of modules on ringed spaces

**12.1.1.**

<!-- label: 0_III.12.1.1 -->

Let $(X, \mathcal{O}_{X})$ be a ringed space. Recall that for every $\mathcal{O}_{X}$-module $\mathcal{F}$ one defines
the cohomology $H^{\bullet}(X, \mathcal{F})$, which is a universal cohomological functor `(T, 2.2)` from the category
$C(X)$ of $\mathcal{O}_{X}$-modules to the category of abelian groups; it is the right-derived functor of the left-exact
functor $\mathcal{F} \mapsto \Gamma(X, \mathcal{F})$. The functor $H^{\bullet}(X, \mathcal{F})$ is isomorphic

<!-- original page 50 -->

to the restriction to the category $C(X)$ of the cohomological functor defined in the same way on the category of
*sheaves of abelian groups* on $X$ `(G, II, 7.2.1)`.

**12.1.2.**

<!-- label: 0_III.12.1.2 -->

Set $A = \Gamma(X, \mathcal{O}_{X})$. Since every element of $A$ defines an endomorphism of the abelian group $\Gamma(X,
\mathcal{F})$, it defines by functoriality an endomorphism of the $\partial$-functor $H^{\bullet}(X, \mathcal{F})$;
these endomorphisms equip each $H^{p}(X, \mathcal{F})$ with a structure of $A$-module, and the operator $\partial$ is
$A$-linear. Moreover, for any two non-negative integers $p$, $q$ and any two $\mathcal{O}_{X}$-modules $\mathcal{F}$,
$\mathcal{G}$, one has a homomorphism of $A$-modules, called the *cup product*

```text
  H^p(X, ℱ) ⊗_A H^q(X, 𝒢) → H^{p+q}(X, ℱ ⊗_{𝒪_X} 𝒢)                          (12.1.2.1)
```

`(G, II, 6.6)`. These homomorphisms make the direct sum $S$ of the $H^{p}(X, \mathcal{O}_{X})$ (for $p \geq 0$) into a
graded anticommutative $A$-algebra, and the direct sum of the $H^{p}(X, \mathcal{F})$ into a graded $S$-module.

For every open cover $\mathfrak{U}$ of $X$, we shall always denote by $C^{\bullet}(\mathfrak{U}, \mathcal{F})$ (contrary
to `(G, II, 5.1)`) the complex of *alternating* cochains of the nerve of $\mathfrak{U}$ with values in the system of
coefficients $\Gamma(U_{\sigma}, \mathcal{F})$. It is clear that $C^{\bullet}(\mathfrak{U}, \mathcal{F})$ is a graded
$A$-module, so the cohomology groups $H^{\bullet}(\mathfrak{U}, \mathcal{F})$ of this complex are endowed with a
structure of $A$-module; moreover, the canonical maps $H^{\bullet}(\mathfrak{U}, \mathcal{F}) \to H^{\bullet}(X,
\mathcal{F})$ `(G, II, 5.4)` are $A$-linear.

**12.1.3.**

<!-- label: 0_III.12.1.3 -->

Let $(X', \mathcal{O}_{X'})$ be a second ringed space, and let $f = (\psi, \theta)$ be a morphism from $X'$ to $X$.

Set $A' = \Gamma(X', \mathcal{O}_{X'})$; the $\psi$-morphism $\theta$ defines canonically a ring homomorphism $A \to
A'$. Let $\mathcal{F}$ be an $\mathcal{O}_{X}$-module and $\mathcal{F}'$ an $\mathcal{O}_{X'}$-module; for every
$f$-morphism $u : \mathcal{F} \to \mathcal{F}'$ $(0_{I}, 4.4.1)$ we shall see that one can define, for every $p \geq 0$,
a di-homomorphism

```text
  u_p : H^p(X, ℱ) → H^p(X', ℱ').                                             (12.1.3.1)
```

Indeed, since $\psi^{*}$ is exact in the category of sheaves of abelian groups on $X$, $\mathcal{F} \mapsto
H^{\bullet}(X', \psi^{*}(\mathcal{F}))$ is a $\partial$-functor in this category, and one knows that one has a canonical
homomorphism of $\partial$-functors

```text
  H^•(X, ℱ) → H^•(X', ψ^*(ℱ))                                                (12.1.3.2)
```

uniquely determined by the condition of reducing to the canonical homomorphism $\Gamma(X, \mathcal{F}) \to \Gamma(X',
\psi^{*}(\mathcal{F}))$ in degree `0` `(T, 3.2.2)`. Moreover, every element of $A$ determines an endomorphism $\mu$ of
$\Gamma(X, \mathcal{F})$ and an endomorphism $\mu'$ of $\Gamma(X', \psi^{*}(\mathcal{F}))$ such that the diagram

```text
                 Γ(X, ℱ)   →   Γ(X', ψ^*(ℱ))
                    ↓μ              ↓μ'                                       (12.1.3.3)
                 Γ(X, ℱ)   →   Γ(X', ψ^*(ℱ))
```

<!-- original page 51 -->

is commutative; by the uniqueness property of extension of morphisms for universal cohomological functors `(T, 2.2)`,
one deduces unique extensions of $\mu$ and $\mu'$ to the cohomology making the diagrams analogous to `(12.1.3.3)`
commutative, which means that `(12.1.3.2)` is a homomorphism of $A$-modules. Now note that one has $f^{*}(\mathcal{F}) =
\psi^{*}(\mathcal{F}) \otimes_{\psi^{*}(\mathcal{O}_{X})} \mathcal{O}_{X'}$, so one has a canonical di-homomorphism
$\psi^{*}(\mathcal{F}) \to f^{*}(\mathcal{F})$ of the $\psi^{*}(\mathcal{O}_{X})$-module $\psi^{*}(\mathcal{F})$ into
the $\mathcal{O}_{X'}$-module $f^{*}(\mathcal{F})$. By functoriality, one therefore deduces a functorial di-homomorphism

```text
  H^p(X', ψ^*(ℱ)) → H^p(X', f^*(ℱ))                                          (12.1.3.4)
```

with corresponding rings $A$ and $A'$; composing this di-homomorphism with `(12.1.3.2)`, one obtains a canonical
di-homomorphism functorial in $\mathcal{F}$

```text
  θ_p : H^p(X, ℱ) → H^p(X', f^*(ℱ)).                                         (12.1.3.5)
```

Finally, by functoriality, one deduces from the homomorphism $u^{\flat} : f^{*}(\mathcal{F}) \to \mathcal{F}'$ a
homomorphism of $A'$-modules $H^{p}(X', f^{*}(\mathcal{F})) \to H^{p}(X', \mathcal{F}')$, which, composed with
`(12.1.3.5)`, gives `(12.1.3.1)`.

Let $f' = (\psi', \theta') : X'' \to X'$ be a second morphism of ringed spaces, $f'' = f \circ f'$ the composite
morphism. Taking into account the commutativity of the functor $\psi^{*}$ with tensor product $(0_{I}, 4.3.3)$, one
verifies immediately that the composite of the di-homomorphism $H^{p}(X', f^{*}(\mathcal{F})) \to H^{p}(X'',
f'^{*}(f^{*}(\mathcal{F})))$ with `(12.1.3.5)` is the corresponding di-homomorphism $H^{p}(X, \mathcal{F}) \to
H^{p}(X'', f''^{*}(\mathcal{F}))$.

**12.1.4.**

<!-- label: 0_III.12.1.4 -->

A direct definition of the homomorphism `(12.1.3.2)` can be obtained as follows: one considers an injective resolution
$\mathcal{L}^{\bullet} = (\mathcal{L}^{i})$ of $\mathcal{F}$ formed of sheaves of abelian groups on $X$; since the
functor $\psi^{*}$ is exact, $\psi^{*}(\mathcal{L}^{\bullet})$ is a resolution of $\psi^{*}(\mathcal{F})$ formed of
sheaves on $X'$. If $\mathcal{L}'^{\bullet} = (\mathcal{L}'^{i})$ is an injective resolution of $\psi^{*}(\mathcal{F})$
in the category of sheaves of abelian groups on $X'$, there is therefore a morphism $\psi^{*}(\mathcal{L}^{\bullet}) \to
\mathcal{L}'^{\bullet}$ of complexes of sheaves of abelian groups, compatible with the augmentations `(M, V, 1.1 a))`,
well-determined up to homotopy. One thus deduces homomorphisms

```text
  Γ(X, ℒ^•) → Γ(X', ψ^*(ℒ^•)) → Γ(X', ℒ'^•)
```

of complexes of abelian groups, whose composite, by passage to cohomology, gives a morphism of $\partial$-functors
$H^{\bullet}(X, \mathcal{F}) \to H^{\bullet}(X', \psi^{*}(\mathcal{F}))$; since it coincides with `(12.1.3.2)` in degree
`0`, it is identical to it `(T, 2.2)`.

Now consider an open cover $\mathfrak{U} = (U_{\alpha})$ of $X$, and let $\mathfrak{U}' = (\psi^{-1}(U_{\alpha}))$ be
the open cover of $X'$ obtained as the inverse image of $\mathfrak{U}$. The canonical homomorphisms $\Gamma(V,
\mathcal{F}) \to \Gamma(\psi^{-1}(V), f^{*}(\mathcal{F}))$ for every open $V$ of $X$ define at once (cf. `G, II, 5.1`) a
homomorphism of complexes $C^{\bullet}(\mathfrak{U}, \mathcal{F}) \to C^{\bullet}(\mathfrak{U}', f^{*}(\mathcal{F}))$,
whence the canonical homomorphisms

```text
  θ_p : H^p(𝔘, ℱ) → H^p(𝔘', f^*(ℱ)).                                         (12.1.4.1)
```

<!-- original page 52 -->

Moreover, one has commutative diagrams

```text
              H^p(𝔘, ℱ)    →^{θ_p}    H^p(𝔘', f^*(ℱ))
                  ↓                       ↓                                   (12.1.4.2)
              H^p(X, ℱ)    →^{θ_p}    H^p(X', f^*(ℱ))
```

where the vertical arrows are the canonical homomorphisms of `(G, II, 5.2)`. To establish the commutativity of
`(12.1.4.2)`, consider the complex of sheaves of (alternating) cochains of $\mathcal{F}$ relative to $\mathfrak{U}$,
$\mathcal{C}^{\bullet}(\mathfrak{U}, \mathcal{F})$, such that $\Gamma(X, \mathcal{C}^{\bullet}(\mathfrak{U},
\mathcal{F})) = C^{\bullet}(\mathfrak{U}, \mathcal{F})$ `(G, II, 5.2)`. The canonical homomorphisms $\Gamma(V,
\mathcal{F}) \to \Gamma(\psi^{-1}(V), \psi^{*}(\mathcal{F}))$ then define a $\psi$-morphism
$\mathcal{C}^{\bullet}(\mathfrak{U}, \mathcal{F}) \to \mathcal{C}^{\bullet}(\mathfrak{U}', \psi^{*}(\mathcal{F}))$, and
one has, with the notation above, a commutative diagram

```text
   Γ(X, 𝒞^•(𝔘, ℱ))   →   Γ(X', 𝒞^•(𝔘', ψ^*(ℱ)))
         ↓                          ↓
   Γ(X, ℒ^•)         →   Γ(X', ψ^*(ℒ^•))   →   Γ(X', ℒ'^•)
```

which, on passing to cohomology, gives commutative diagrams

```text
              H^p(𝔘, ℱ)    →    H^p(𝔘', ψ^*(ℱ))
                  ↓                  ↓
              H^p(X, ℱ)    →    H^p(X', ψ^*(ℱ))
```

where the vertical arrows are the canonical homomorphisms of `(G, II, 5.2)`. It then suffices to combine these diagrams
with the commutative diagrams

```text
              H^p(𝔘', ψ^*(ℱ))   →   H^p(𝔘', f^*(ℱ))
                  ↓                       ↓
              H^p(X', ψ^*(ℱ))   →   H^p(X', f^*(ℱ))
```

<!-- original page 53 -->

which come from the homomorphism $\psi^{*}(\mathcal{F}) \to f^{*}(\mathcal{F})$ and from the functorial character of the
canonical homomorphisms of `(G, II, 5.2)`, to obtain the commutativity of `(12.1.4.2)`.

Note that if $A = \Gamma(X, \mathcal{O}_{X})$, $A' = \Gamma(X', \mathcal{O}_{X'})$, the homomorphism `(12.1.4.1)` is a
di-homomorphism of modules corresponding to the rings $A$ and $A'$. One has a *transitivity* property for `(12.1.4.1)`
with respect to the composite of two morphisms, analogous to the transitivity of `(12.1.3.5)`. Finally, note that in the
preceding definitions, instead of an injective resolution $\mathcal{L}^{\bullet}$ of $\mathcal{F}$, one could equally
well have started from a resolution such that $H^{p}(X, \mathcal{L}^{i}) = 0$ for all $i$ and all $p > 0$
`(G, II, 4.7.1)`.

**12.1.5.**

<!-- label: 0_III.12.1.5 -->

Let $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ be three $\mathcal{O}_{X}$-modules, and consider an
$\mathcal{O}_{X}$-homomorphism $u : \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{G} \to \mathcal{H}$, which gives, for
cohomology, homomorphisms

```text
  H^p(X, ℱ) ⊗_A H^q(X, 𝒢) → H^{p+q}(X, 𝓗)                                    (12.1.5.1)
```

deduced from the cup product `(12.1.2.1)`. We show that, with the hypotheses and notation of `(12.1.3)`, one has
commutative diagrams

```text
   H^p(X, ℱ) ⊗_A H^q(X, 𝒢)                  →   H^{p+q}(X, 𝓗)
            ↓                                          ↓                      (12.1.5.2)
   H^p(X', f^*(ℱ)) ⊗_{A'} H^q(X', f^*(𝒢))   →   H^{p+q}(X', f^*(𝓗))
```

where the vertical arrows come from the canonical homomorphisms `(12.1.3.5)`. For this, recall that `(12.1.5.1)` can be
obtained by starting from the *canonical* resolutions `(G, II, 4.3)` $\mathcal{L}^{\bullet}$, $\mathcal{M}^{\bullet}$,
$\mathcal{N}^{\bullet}$ of $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ respectively (which are formed of
$\mathcal{O}_{X}$-modules), from the linear map $\mathcal{L}^{\bullet} \otimes_{\mathcal{O}_{X}} \mathcal{M}^{\bullet}
\to \mathcal{N}^{\bullet}$ of complexes of $\mathcal{O}_{X}$-modules corresponding to $u$, which yields a homomorphism
of complexes of $A$-modules $\Gamma(X, \mathcal{L}^{\bullet}) \otimes_{A} \Gamma(X, \mathcal{M}^{\bullet}) \to \Gamma(X,
\mathcal{N}^{\bullet})$, and by passing to cohomology, the homomorphisms $H^{p}(\Gamma(X, \mathcal{L}^{\bullet}))
\otimes_{A} H^{q}(\Gamma(X, \mathcal{M}^{\bullet})) \to H^{p+q}(\Gamma(X, \mathcal{N}^{\bullet}))$ `(G, II, 6.6)`. Now,
one clearly has a commutative diagram

```text
   Γ(X, ℒ^•) ⊗_A Γ(X, ℳ^•)                                              →   Γ(X, 𝒩^•)
            ↓                                                                  ↓        (12.1.5.3)
   Γ(X', ψ^*(ℒ^•)) ⊗_{Γ(X', ψ^*(𝒪_X))} Γ(X', ψ^*(ℳ^•))                  →   Γ(X', ψ^*(𝒩^•))
```

<!-- original page 54 -->

which gives, on passing to cohomology, the commutative diagrams

```text
   H^p(X, ℱ) ⊗_A H^q(X, 𝒢)                                                                                →   H^{p+q}(X, 𝓗)
            ↓                                                                                                       ↓                        (12.1.5.4)
   H^p(Γ(X', ψ^*(ℒ^•))) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(Γ(X', ψ^*(ℳ^•)))                                       →   H^{p+q}(Γ(X', ψ^*(𝒩^•))).
```

But since $\psi^{*}(\mathcal{L}^{\bullet})$, $\psi^{*}(\mathcal{M}^{\bullet})$ and $\psi^{*}(\mathcal{N}^{\bullet})$ are
*resolutions* of $\psi^{*}(\mathcal{F})$, $\psi^{*}(\mathcal{G})$, $\psi^{*}(\mathcal{H})$ respectively, one has a
commutative diagram `(G, II, 6.6.1)`

```text
   H^p(Γ(X', ψ^*(ℒ^•))) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(Γ(X', ψ^*(ℳ^•)))   →   H^{p+q}(Γ(X', ψ^*(𝒩^•)))
            ↓                                                                  ↓                                 (12.1.5.5)
   H^p(X', ψ^*(ℱ)) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(X', ψ^*(𝒢))            →   H^{p+q}(X', ψ^*(𝓗)).
```

Finally, by functoriality, one has a commutative diagram

```text
   H^p(X', ψ^*(ℱ)) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(X', ψ^*(𝒢))   →   H^{p+q}(X', ψ^*(𝓗))
            ↓                                                       ↓                       (12.1.5.6)
   H^p(X', f^*(ℱ)) ⊗_{A'} H^q(X', f^*(𝒢))                →   H^{p+q}(X', f^*(𝓗))
```

and by combining the three diagrams `(12.1.5.4)`, `(12.1.5.5)` and `(12.1.5.6)`, one obtains the desired commutative
diagram `(12.1.5.2)`.

<!-- original page 55 -->

**Remark (12.1.6).**

<!-- label: 0_III.12.1.6 -->

With the notation of `(12.1.3)`, suppose one has a commutative diagram

```text
   0  →  ℱ   →^r   𝒢   →^s   𝓗   →  0
              ↓u         ↓v         ↓w                                        (12.1.6.1)
   0  →  ℱ'  →^{r'}  𝒢'  →^{s'}  𝓗'  →  0
```

where $r$, $s$ are homomorphisms of $\mathcal{O}_{X}$-modules, $r'$, $s'$ are homomorphisms of
$\mathcal{O}_{X'}$-modules, $u$, $v$, $w$ are $f$-morphisms, and the rows are exact. One then deduces a commutative
diagram

```text
   ⋯ → H^p(X, ℱ)   → H^p(X, 𝒢)   → H^p(X, 𝓗)   →^∂  H^{p+1}(X, ℱ)   → ⋯
            ↓u_p          ↓v_p          ↓w_p           ↓u_{p+1}                (12.1.6.2)
   ⋯ → H^p(X', ℱ') → H^p(X', 𝒢') → H^p(X', 𝓗') →^∂ H^{p+1}(X', ℱ') → ⋯.
```

Indeed, `(12.1.6.1)` factors as

$$ 0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0 \downarrow \downarrow \downarrow 0 \to \psi^{*}(\mathcal{F})
\to \psi^{*}(\mathcal{G}) \to \psi^{*}(\mathcal{H}) \to 0 \downarrow \downarrow \downarrow 0 \to \mathcal{F}' \to
\mathcal{G}' \to \mathcal{H}' \to 0 $$

where the middle row is exact $(0_{I}, 3.7.2)$, and it suffices to use the fact that `(12.1.3.2)` is a homomorphism of
$\partial$-functors and that the $H^{p}(X', \mathcal{F}')$ form a $\partial$-functor in $\mathcal{F}'$.

**12.1.7.**

<!-- label: 0_III.12.1.7 -->

The hypotheses and notation being those of `(12.1.3)`, consider now the case where $\mathcal{F} = f_{*}(\mathcal{F}') =
\psi_{*}(\mathcal{F}')$; we shall see that the di-homomorphism defined in `(12.1.3)`

```text
  H^p(X, f_*(ℱ')) → H^p(X', ℱ')                                              (12.1.7.1)
```

can be obtained (up to an automorphism of $H^{p}(X', \mathcal{F}')$) as an *edge homomorphism* of a spectral sequence of
the composite functor $\mathcal{F}' \mapsto \Gamma(X', \psi_{*}(\mathcal{F}'))$ `(T, 2.4)`. The description of the
homomorphism `(12.1.7.1)` given in `(12.1.4)` shows here that one can obtain this homomorphism as follows: one considers
injective resolutions $\mathcal{L}^{\bullet}$ and $\mathcal{L}'^{\bullet}$ of $\psi_{*}(\mathcal{F}')$ and of
$\mathcal{F}'$ respectively, then one takes a homomorphism of complexes $v : \psi^{*}(\mathcal{L}^{\bullet}) \to
\mathcal{L}'^{\bullet}$ "lying above" the canonical homomorphism $\psi^{*}(\psi_{*}(\mathcal{F}')) \to \mathcal{F}'$;

<!-- original page 56 -->

one then notes that one has $\Gamma(X', \mathcal{L}'^{\bullet}) = \Gamma(X, \psi_{*}(\mathcal{L}'^{\bullet}))$ and that
the composite homomorphism

```text
  Γ(X, ℒ^•) → Γ(X', ψ^*(ℒ^•)) →^{Γ(v)} Γ(X', ℒ'^•)
```

is none other than

```text
  Γ(v^♭) : Γ(X, ℒ^•) → Γ(X, ψ_*(ℒ'^•))                                       (12.1.7.2)
```

$(0_{I}, 3.7.1)$, and `(12.1.7.1)` is obtained by passage to cohomology in `(12.1.7.2)`. On the other hand, the spectral
sequences of the composite functor $\mathcal{F}' \mapsto \Gamma(X, \psi_{*}(\mathcal{F}'))$ are obtained by considering
an injective Cartan–Eilenberg resolution $\mathcal{M}^{\bullet\bullet} = (\mathcal{M}^{ij})$ of the complex
$\psi_{*}(\mathcal{L}'^{\bullet})$ in the category of sheaves of abelian groups on $X$; the spectral sequences in
question are those of the bicomplex $\Gamma(X, \mathcal{M}^{\bullet\bullet})$ (which are biregular since
$\mathcal{M}^{ij} = 0$ for $i < 0$ or $j < 0$). Now, the first spectral sequence of this bicomplex *degenerates*, for
the sheaves $\psi_{*}(\mathcal{L}'^{i})$ are flasque `(G, II, 3.1.1)`, hence $H^{q}_{II}(\Gamma(X,
\mathcal{M}^{i\bullet})) = H^{q}(\psi_{*}(\mathcal{L}'^{i})) = 0$ for $q > 0$ `(G, II, 4.4.3)`; one therefore has
*bijective* edge homomorphisms `(11.1.6)`

```text
  'E_2^{i,0} = H^i(H_{II}^0(Γ(X, ℳ^{••}))) → H^i(Γ(X, ℳ^{••}))               (12.1.7.3)
```

and one knows `(11.3.4)` that this homomorphism comes, by passage to cohomology, from the augmentation

```text
  Γ(X, ψ_*(ℒ'^•)) → Γ(X, ℳ^{••})                                             (12.1.7.4)
```

which itself comes from the augmentation $\eta : \psi_{*}(\mathcal{L}'^{\bullet}) \to \mathcal{M}^{\bullet 0}$. On the
other hand, for the second spectral sequence one has edge homomorphisms

```text
  ″E_2^{i,0} = H^i(H_I^0(Γ(X, ℳ^{••}))) → H^i(Γ(X, ℳ^{••}))                  (12.1.7.5)
```

coming `(11.3.4)`, by passage to cohomology, from the homomorphism of complexes $Z^{0}_{I}(\Gamma(X,
\mathcal{M}^{\bullet\bullet})) \to \Gamma(X, \mathcal{M}^{\bullet\bullet})$. Now, since $\psi_{*}$ is left-exact, the
sequence

$$ 0 \to \psi_{*}(\mathcal{F}') \to \psi_{*}(\mathcal{L}'^{0}) \to \psi_{*}(\mathcal{L}'^{1}) $$

is exact; by the definition of a Cartan–Eilenberg resolution `(11.4.2)`, one can therefore take
$B^{0}_{I}(\mathcal{M}^{\bullet\bullet}) = 0$, $Z^{0}_{I}(\mathcal{M}^{\bullet\bullet}) = \mathcal{L}^{\bullet}$; since
the diagram

```text
                    ℒ^0   →^{i^0}   ℳ^{00}
                  ε ↓         ↗^{ε''}     ↑η^0
                    ψ_*(ℱ')   →^{ε'}    ψ_*(ℒ'^0)
```

is commutative, the injection of complexes $i : \mathcal{L}^{\bullet} \to \mathcal{M}^{\bullet 0}$ is compatible with
the augmentations $\epsilon$ and $\epsilon''$. One thus has two homomorphisms of complexes from $\mathcal{L}^{\bullet}$
into $\mathcal{M}^{\bullet 0}$

```text
                    ℒ^•   →^i      ℳ^{•0}
                  v^♭ ↘    ↗ η
                    ψ_*(ℒ'^•)
```

<!-- original page 57 -->

compatible with the augmentations $\epsilon$ and $\epsilon''$; since $\mathcal{L}^{\bullet}$ is an injective resolution
and $\mathcal{M}^{\bullet 0}$ is formed of injective sheaves, it follows from `(M, V, 1.1 a))` that these two
homomorphisms are *homotopic*; the same is therefore true of the two corresponding homomorphisms $\Gamma(X,
\mathcal{L}^{\bullet}) \to \Gamma(X, \mathcal{M}^{\bullet 0})$, and on passing to cohomology one obtains the *same*
homomorphism; in other words, one has shown that the edge homomorphism `(12.1.7.5)`, which is written $H^{p}(X,
\psi_{*}(\mathcal{F}')) \to H^{p}(\Gamma(X, \mathcal{M}^{\bullet\bullet}))$, is composed of `(12.1.7.1)` and of
`(12.1.7.3)`, which is written $H^{p}(X', \mathcal{F}') \to H^{p}(\Gamma(X, \mathcal{M}^{\bullet\bullet}))$ and which we
have seen to be an *isomorphism*; whence our assertion.

### 12.2. Higher direct images

**12.2.1.**

<!-- label: 0_III.12.2.1 -->

Let $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ be two ringed spaces, $f = (\psi, \theta)$ a morphism from $X$ to
$Y$, which defines the *direct image functor* $f_{*} : C(X) \to C(Y)$, identical moreover with the restriction to $C(X)$
of the functor $\psi_{*}$ defined in the category of sheaves of abelian groups on $X$. This last functor is additive and
left-exact, and since every sheaf of abelian groups on $X$ is isomorphic to a subsheaf of an *injective* sheaf of
abelian groups, one defines the *right-derived functors* $\mathcal{F} \mapsto R^{p} \psi_{*}(\mathcal{F})$ of the
functor $\psi_{*}$; the $R^{p} \psi_{*}(\mathcal{F})$ are sheaves of abelian groups on $Y$, and the $R^{p} \psi_{*}$
form a *universal cohomological functor* `(T, 2.3)`.

Moreover, the sheaf $R^{p} \psi_{*}(\mathcal{F})$ is the sheaf associated to the presheaf $V \mapsto H^{p}(\psi^{-1}(V),
\mathcal{F})$ `(T, 3.7.2)`. Suppose now that $\mathcal{F}$ is an $\mathcal{O}_{X}$-module. Then $H^{p}(\psi^{-1}(V),
\mathcal{F})$ is naturally endowed with a structure of $\Gamma(\psi^{-1}(V), \mathcal{O}_{X})$-module, hence of
$\Gamma(V, \psi_{*}(\mathcal{O}_{X}))$-module, and the data of the homomorphism $\theta : \mathcal{O}_{Y} \to
\psi_{*}(\mathcal{O}_{X})$ allows one to deduce a structure of $\Gamma(V, \mathcal{O}_{Y})$-module. For the structures
thus defined, it is clear that restriction from an open set $V$ to an open set $V' \subseteq V$ defines a
di-homomorphism, and this permits us to define on each of the $R^{p} \psi_{*}(\mathcal{F})$ a structure of
$\mathcal{O}_{Y}$-module; this is the $\mathcal{O}_{Y}$-module that we shall denote by $R^{p} f_{*}(\mathcal{F})$, with
$R^{p} f_{*}$ thus defined as an additive functor from $C(X)$ to $C(Y)$. Moreover, the $R^{p} f_{*}$ form a
$\partial$-functor, for if $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is an exact sequence of
$\mathcal{O}_{X}$-modules, the description of the $R^{p} \psi_{*}$ and of the $\mathcal{O}_{Y}$-module structure on
$R^{p} f_{*}(\mathcal{F})$ given above shows at once that the homomorphism $\partial : R^{p} f_{*}(\mathcal{F}'') \to
R^{p+1} f_{*}(\mathcal{F}')$ is in this case a homomorphism of $\mathcal{O}_{Y}$-modules. Finally, the $R^{p} f_{*}$
identify with the right-derived functors of $f_{*}$: indeed, every $\mathcal{O}_{X}$-module admits an injective
resolution formed of $\mathcal{O}_{X}$-modules, and since such a resolution is formed of flasque sheaves of abelian
groups `(G, II, 7.1)`, it can serve to compute the $R^{p} \psi_{*}(\mathcal{F})$, since $R^{n} \psi_{*}(\mathcal{G}) =
0$ for $n \geq 1$ and every flasque sheaf $\mathcal{G}$ `(T, 2.4.1, Remark 3, and cor. of Prop. 3.3.2)`. One thus
concludes that the $R^{p} f_{*}$ form a *universal cohomological functor* from $C(X)$ to $C(Y)$ `(T, 2.3)`.

**12.2.2.**

<!-- label: 0_III.12.2.2 -->

Let $\mathcal{F}$ and $\mathcal{G}$ be two $\mathcal{O}_{X}$-modules. With the notation of `(12.2.1)`, for every open
$V$ of $Y$ one has the cup-product homomorphism `(12.1.2.1)`

```text
  H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(ψ^{-1}(V), 𝒪_X)} H^q(ψ^{-1}(V), 𝒢)
      → H^{p+q}(ψ^{-1}(V), ℱ ⊗_{𝒪_X} 𝒢)
```

<!-- original page 58 -->

and it follows at once from the definition of the cup product `(G, II, 6.6)` that these homomorphisms commute with
passage from $V$ to an open subspace $V'$ of $V$. On the other hand, one has a homomorphism of rings

```text
  Γ(V, 𝒪_Y) → Γ(V, ψ_*(𝒪_X)) = Γ(ψ^{-1}(V), 𝒪_X)
```

coming from $\theta$, whence a canonical homomorphism of tensor products

```text
  H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(V, 𝒪_Y)} H^q(ψ^{-1}(V), 𝒢)
      → H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(ψ^{-1}(V), 𝒪_X)} H^q(ψ^{-1}(V), 𝒢)
```

which is also compatible with the restriction from $V$ to $V'$. By composition, one therefore obtains a homomorphism of
$\Gamma(V, \mathcal{O}_{Y})$-modules, which defines a canonical functorial-in-$\mathcal{F}$-and-$\mathcal{G}$
homomorphism for the sheaves associated to the presheaves considered:

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} R^q f_*(𝒢) → R^{p+q} f_*(ℱ ⊗_{𝒪_X} 𝒢).                  (12.2.2.1)
```

Note that for $p = q = 0$, this homomorphism reduces to $(0_{I}, 4.2.2.1)$.

**Proposition (12.2.3).**

<!-- label: 0_III.12.2.3 -->

*For every $\mathcal{O}_{X}$-module $\mathcal{F}$ and every $\mathcal{O}_{Y}$-module locally free of finite rank
$\mathcal{L}$, one has canonical functorial isomorphisms*

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} ℒ ⥲ R^p f_*(ℱ ⊗_{𝒪_X} f^*(ℒ)).                          (12.2.3.1)
```

**Proof.** The homomorphism `(12.2.3.1)` is obtained by composing the homomorphism, a particular case of `(12.2.2.1)`,

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} f_*(f^*(ℒ)) → R^p f_*(ℱ ⊗_{𝒪_X} f^*(ℒ))                 (12.2.3.2)
```

with the homomorphism from the first member of `(12.2.3.1)` to that of `(12.2.3.2)` coming from the canonical
homomorphism $(0_{I}, 4.4.3.2)$. To verify that `(12.2.3.1)` is an isomorphism when $\mathcal{L}$ is locally free, one
can immediately reduce to the case $\mathcal{L} = \mathcal{O}_{Y}$, the question being local on $Y$, and the functors
considered being additive in $\mathcal{L}$. But then, the proposition reduces, in view of the definition of
`(12.2.2.1)`, to the verification that the corresponding homomorphism of presheaves is bijective, which is immediate by
virtue of the relation $f^{*}(\mathcal{O}_{Y}) = \mathcal{O}_{X}$.

**12.2.4.**

<!-- label: 0_III.12.2.4 -->

Let $(Z, \mathcal{O}_{Z})$ be a third ringed space, $g : Y \to Z$ a morphism of ringed spaces. One knows
`(G, II, 7.1 and 3.1.1)` that for every injective $\mathcal{O}_{Y}$-module $\mathcal{G}$, $f_{*}(\mathcal{G})$ is a
flasque sheaf of abelian groups, and consequently `(12.2.1)` one has $R^{p} g_{*}(f_{*}(\mathcal{G})) = 0$ for every
$p > 0$. It follows `(T, 2.4.1)` that the *Leray spectral sequence* of the composed functors is applicable to the
composite functor $g_{*} f_{*}$: there is a biregular spectral sequence whose abutment is the functor
$R^{\bullet} h_{*}$ where $h = g \circ f$, and whose `E_2` term is given by

```text
  E_2^{p,q} = R^p g_*(R^q f_*(ℱ)).                                           (12.2.4.1)
```

**12.2.5.**

<!-- label: 0_III.12.2.5 -->

Under the conditions of `(12.2.4)`, we shall define directly canonical homomorphisms of $\mathcal{O}_{Z}$-modules

```text
  R^n g_*(f_*(ℱ)) → R^n h_*(ℱ)                                               (12.2.5.1)
  R^n h_*(ℱ) → g_*(R^n f_*(ℱ))                                               (12.2.5.2)
```

<!-- original page 59 -->

which could be identified with the "edge homomorphisms" of the Leray spectral sequence (cf. `(12.1.7)`). It suffices to
operate on the presheaves to which the higher direct image sheaves `(12.2.1)` are associated. For this, consider any
open set $W$ of $Z$ and its inverse image $g^{-1}(W)$ in $Y$; one has a canonical di-homomorphism

```text
  H^n(g^{-1}(W), f_*(ℱ)) → H^n(f^{-1}(g^{-1}(W)), f^*(f_*(ℱ)))                (12.2.5.3)
```

with corresponding rings $\Gamma(g^{-1}(W), \mathcal{O}_{Y})$ and $\Gamma(h^{-1}(W), \mathcal{O}_{X})$; on the other
hand, the canonical homomorphism $(0_{I}, 4.4.3.3)$ yields by functoriality canonical homomorphisms

```text
  H^n(h^{-1}(W), f^*(f_*(ℱ))) → H^n(h^{-1}(W), ℱ)                            (12.2.5.4)
```

which are homomorphisms of $\Gamma(h^{-1}(W), \mathcal{O}_{X})$-modules. Taking into account the ring homomorphism
$\Gamma(W, \mathcal{O}_{Z}) \to \Gamma(h^{-1}(W), \mathcal{O}_{X})$, one sees that by composing `(12.2.5.4)` and
`(12.2.5.3)` one obtains a homomorphism of presheaves, which yields the homomorphism of sheaves `(12.2.5.1)`.

The definition of `(12.2.5.2)` is even simpler; by definition, $R^{n} h_{*}(\mathcal{F})$ is associated to the presheaf
$W \mapsto H^{n}(f^{-1}(g^{-1}(W)), \mathcal{F})$ and $R^{n} f_{*}(\mathcal{F})$ to the presheaf $V \mapsto
H^{n}(f^{-1}(V), \mathcal{F})$; one therefore has a canonical homomorphism

```text
  H^n(f^{-1}(g^{-1}(W)), ℱ) → Γ(g^{-1}(W), R^n f_*(ℱ)),
```

and it is immediate that these homomorphisms define a homomorphism of presheaves, which in turn defines `(12.2.5.2)`.

**12.2.6.**

<!-- label: 0_III.12.2.6 -->

Under the hypotheses of `(12.2.4)`, let $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ be three $\mathcal{O}_{X}$-modules
and $u : \mathcal{F} \otimes \mathcal{G} \to \mathcal{H}$ an $\mathcal{O}_{X}$-homomorphism. One then has commutative
diagrams

```text
   R^p g_*(f_*(ℱ)) ⊗_{𝒪_Z} R^q g_*(f_*(𝒢))   →   R^{p+q} g_*(f_*(𝓗))
            ↓                                          ↓                       (12.2.6.1)
   R^p h_*(ℱ) ⊗_{𝒪_Z} R^q h_*(𝒢)             →   R^{p+q} h_*(𝓗)
```

and

```text
   R^p h_*(ℱ) ⊗_{𝒪_Z} R^q h_*(𝒢)             →   R^{p+q} h_*(𝓗)
            ↓                                          ↓                       (12.2.6.2)
   g_*(R^p f_*(ℱ)) ⊗_{𝒪_Z} g_*(R^q f_*(𝒢))   →   g_*(R^{p+q} f_*(𝓗))
```

<!-- original page 60 -->

where the horizontal arrows come from `(12.2.2.1)` (the last combined with $(0_{I}, 4.2.2.1)$) and the vertical arrows
from the homomorphisms `(12.2.5.1)` and `(12.2.5.2)` respectively.

It indeed suffices to verify this for the corresponding homomorphisms of presheaves; returning to the definitions given
in `(12.2.2)` and `(12.2.5)` for these homomorphisms, one is immediately reduced, for `(12.2.6.1)`, to the commutative
diagrams `(12.1.5.2)`; the verification is even simpler for `(12.2.6.2)`.

### 12.3. Complements on the Ext functors of sheaves

**12.3.1.**

<!-- label: 0_III.12.3.1 -->

Consider a ringed space $(X, \mathcal{O}_{X})$; we shall not return to the definition and principal properties of the
bifunctors $Ext^{p}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})$ from the category of $\mathcal{O}_{X}$-modules to
that of $\Gamma(X, \mathcal{O}_{X})$-modules, and $\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ from
the category of $\mathcal{O}_{X}$-modules to itself, nor to the biregular spectral sequence $E(\mathcal{F},
\mathcal{G})$ relating them `(T, 4.2 and G, II, 7.3)`.

**12.3.2.**

<!-- label: 0_III.12.3.2 -->

One defines, in the same way as in `(M, XIV, 1)`, the notion of *extension* of an $\mathcal{O}_{X}$-module $\mathcal{F}$
by an $\mathcal{O}_{X}$-module $\mathcal{G}$ and the composition law between classes of equivalent extensions: the
arguments made for modules adapt indeed in an obvious way to any abelian category. The second proof of `(M, XIV, 1.1)`,
which uses only the existence of embeddings in injective objects, is therefore still valid for the category of
$\mathcal{O}_{X}$-modules, and thus shows that $Ext^{1}_{\mathcal{O}_{X}}(X; \mathcal{F}, \mathcal{G})$ is canonically
identified with the abelian group of classes of *extensions* of $\mathcal{F}$ by $\mathcal{G}$.

**Proposition (12.3.3).**

<!-- label: 0_III.12.3.3 -->

*Let $(X, \mathcal{O}_{X})$ be a ringed space such that the sheaf of rings $\mathcal{O}_{X}$ is coherent. Then, for
every pair of coherent $\mathcal{O}_{X}$-modules $\mathcal{F}$, $\mathcal{G}$ and every $p \geq 0$,
$\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ is a coherent $\mathcal{O}_{X}$-module.*

**Proof.** Note that the $\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ form a cohomological functor
contravariant in $\mathcal{F}$. Since $\mathcal{F}$ is coherent, there exist, for every $p$ and every point $x \in X$,
an open neighborhood $U$ of $x$ and an exact sequence of $(\mathcal{O}_{X} \mid U)$-modules

```text
  0 → ℛ → ℒ_{p−1} → ⋯ → ℒ_0 → ℱ ∣ U → 0
```

where each of the $\mathcal{L}_{i}$ ($0 \leq i \leq p-1$) is isomorphic to an $\mathcal{O}^{n_{i}}_{X} \mid U$ and
$\mathcal{R}$ is coherent: this follows by induction on $p$ from $(0_{I}, 5.3.2)$ and $(0_{I}, 5.3.4)$, in view of the
hypothesis that $\mathcal{O}_{X}$ is coherent.

Now note that, for $p \geq 1$, one has $Ext^{p}_{\mathcal{O}_{X} \mid U}(\mathcal{L} \mid U, \mathcal{G} \mid U) = 0$
for every $\mathcal{O}_{X}$-module $\mathcal{L}$ such that $\mathcal{L} \mid U$ is isomorphic to an $\mathcal{O}^{n}_{X}
\mid U$ `(T, 4.2.3)`; the argument of `(M, V, 7.2)` therefore applies to the contravariant cohomological functor
$\mathcal{F} \mapsto \mathcal{H}om_{\mathcal{O}_{X} \mid U}(\mathcal{F} \mid U, \mathcal{G} \mid U)$, and gives an exact
sequence

```text
  ℋom_{𝒪_X ∣ U}(ℒ_{p−1}, 𝒢 ∣ U) → ℋom_{𝒪_X ∣ U}(ℛ, 𝒢 ∣ U) → ℰxt^p_{𝒪_X ∣ U}(ℱ ∣ U, 𝒢 ∣ U) → 0
```

and since the first two terms of this sequence are coherent $(\mathcal{O}_{X} \mid U)$-modules $(0_{I}, 5.3.5)$, so is
the third $(0_{I}, 5.3.4)$.

<!-- original page 61 -->

**Proposition (12.3.4).**

<!-- label: 0_III.12.3.4 -->

*Let $f : X \to Y$ be a flat morphism of ringed spaces, and let $\mathcal{F}$, $\mathcal{G}$ be two
$\mathcal{O}_{Y}$-modules.*

*(i) There exists a homomorphism of cohomological bifunctors*

```text
  f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) ⥲ ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢))                       (12.3.4.1)
```

*reducing in degree `0` to the canonical homomorphism $(0_{I}, 4.4.6)$.*

*(ii) There exists a canonical morphism of spectral sequences*

```text
  E(ℱ, 𝒢) → E(f^*(ℱ), f^*(𝒢))                                                (12.3.4.2)
```

*which, for the `E_2` terms, reduces to the homomorphisms*

```text
  H^p(Y, ℰxt^q_{𝒪_Y}(ℱ, 𝒢)) → H^p(X, ℰxt^q_{𝒪_X}(f^*(ℱ), f^*(𝒢)))             (12.3.4.3)
```

*deduced from `(12.3.4.1)` and `(12.1.3.1)`.*

**Proof.**

*(i)* Since $f^{*}$ is an exact functor on the category of $\mathcal{O}_{Y}$-modules $(0_{I}, 6.7.2)$, the functors
$\mathcal{G} \mapsto f^{*}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{G}))$ and $\mathcal{G} \mapsto
\mathcal{H}om_{\mathcal{O}_{X}}(f^{*}(\mathcal{F}), f^{*}(\mathcal{G}))$ are left-exact; one deduces canonically from
$(0_{I}, 4.4.6)$ a homomorphism of their derived functors. To compute the latter, one takes an injective resolution
$\mathcal{L}^{\bullet} = (\mathcal{L}^{i})$ of $\mathcal{G}$, and one therefore has morphisms
$\mathcal{H}^{p}(f^{*}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{L}^{\bullet}))) \to
\mathcal{H}^{p}(\mathcal{H}om_{\mathcal{O}_{X}}(f^{*}(\mathcal{F}), f^{*}(\mathcal{L}^{\bullet})))$ of cohomologies of
complexes of sheaves. Moreover, by the exactness of $f^{*}$, one has
$\mathcal{H}^{p}(f^{*}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{L}^{\bullet}))) =
f^{*}(\mathcal{H}^{p}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{L}^{\bullet}))) =
f^{*}(\mathcal{E}xt^{p}_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{G}))$ by definition. On the other hand, the exactness of
$f^{*}$ entails that $f^{*}(\mathcal{L}^{\bullet})$ is a resolution of $f^{*}(\mathcal{G})$; if $\mathcal{L}'^{\bullet}
= (\mathcal{L}'^{i})$ is an injective resolution of $f^{*}(\mathcal{G})$ in the category of $\mathcal{O}_{X}$-modules,
there is therefore a homomorphism of complexes $f^{*}(\mathcal{L}^{\bullet}) \to \mathcal{L}'^{\bullet}$, determined up
to homotopy, and which defines by consequence a well-determined homomorphism in cohomology; composing this homomorphism
with the one defined above, one obtains `(12.3.4.1)`.

*(ii)* With the preceding notation, one has a homomorphism of complexes of sheaves of $\mathcal{O}_{X}$-modules
$f^{*}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{L}^{\bullet})) \to
\mathcal{H}om_{\mathcal{O}_{X}}(f^{*}(\mathcal{F}), \mathcal{L}'^{\bullet})$. Let $\mathcal{M}^{\bullet\bullet}$ be a
Cartan–Eilenberg injective resolution of the complex $\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F},
\mathcal{L}^{\bullet})$ in the category of $\mathcal{O}_{Y}$-modules; then, by the exactness of the functor $f^{*}$,
$f^{*}(\mathcal{M}^{\bullet\bullet})$ is a Cartan–Eilenberg resolution of the complex
$f^{*}(\mathcal{H}om_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{L}^{\bullet}))$; if $\mathcal{M}'^{\bullet\bullet}$ is a
Cartan–Eilenberg injective resolution of the complex $\mathcal{H}om_{\mathcal{O}_{X}}(f^{*}(\mathcal{F}),
\mathcal{L}'^{\bullet})$, there is therefore `(11.4.2)` a homomorphism (determined up to homotopy)
$f^{*}(\mathcal{M}^{\bullet\bullet}) \to \mathcal{M}'^{\bullet\bullet}$ compatible with the homomorphism considered
above, in other words an $f$-morphism $\mathcal{M}^{\bullet\bullet} \to \mathcal{M}'^{\bullet\bullet}$ of bicomplexes of
sheaves. From this one deduces a di-homomorphism $\Gamma(Y, \mathcal{M}^{\bullet\bullet}) \to \Gamma(X,
\mathcal{M}'^{\bullet\bullet})$ of bicomplexes of modules, determined up to homotopy, and a well-determined morphism of
spectral sequences `(11.3.2)`, which is none other than the morphism `(12.3.4.2)` sought, the characterization of
`(12.3.4.3)` following at once from the definitions.

**Proposition (12.3.5).**

<!-- label: 0_III.12.3.5 -->

*Under the hypotheses of `(12.3.4)`, suppose in addition the sheaf of rings $\mathcal{O}_{Y}$ coherent; then, for every
coherent $\mathcal{O}_{Y}$-module $\mathcal{F}$, the canonical homomorphisms `(12.3.4.1)` are bijective.*

<!-- original page 62 -->

**Proof.** The question being local on $Y$, one may suppose there exists an exact sequence $0 \to \mathcal{R} \to
\mathcal{O}^{n}_{Y} \to \mathcal{F} \to 0$, and $\mathcal{R}$ is then also a coherent $\mathcal{O}_{Y}$-module $(0_{I},
5.3.4)$. To prove that the homomorphisms

```text
  f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) → ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢))
```

are bijective, we argue by induction on $p$, the proposition resulting from $(0_{I}, 6.7.6.1)$ when $p = 0$. Now, one
has the commutative diagram

```text
   f^*(ℰxt^{p−1}_{𝒪_Y}(𝒪_Y^n, 𝒢)) → f^*(ℰxt^{p−1}_{𝒪_Y}(ℛ, 𝒢)) →^∂ f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) → f^*(ℰxt^p_{𝒪_Y}(𝒪_Y^n, 𝒢))
            ↓                              ↓                              ↓                                ↓
   ℰxt^{p−1}_{𝒪_X}(𝒪_X^n, f^*(𝒢)) → ℰxt^{p−1}_{𝒪_X}(f^*(ℛ), f^*(𝒢)) →^∂ ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢)) → ℰxt^p_{𝒪_X}(𝒪_X^n, f^*(𝒢))
```

since $f^{*}(\mathcal{O}_{Y}) = \mathcal{O}_{X}$; as $f^{*}$ is exact, the two rows are exact. Moreover, one has
$\mathcal{E}xt^{p}_{\mathcal{O}_{Y}}(\mathcal{O}^{n}_{Y}, \mathcal{G}) = 0$ for every $p > 0$ and likewise
$\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(\mathcal{O}^{n}_{X}, f^{*}(\mathcal{G})) = 0$ for every $p > 0$ `(T, 4.2.3)`. In
view of the induction hypothesis, the first two vertical arrows of the preceding diagram are isomorphisms, and the terms
on the right are `0`, hence $f^{*}(\mathcal{E}xt^{p}_{\mathcal{O}_{Y}}(\mathcal{F}, \mathcal{G})) \to
\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(f^{*}(\mathcal{F}), f^{*}(\mathcal{G}))$ is an isomorphism.

### 12.4. Hypercohomology of the direct image functor

**12.4.1.**

<!-- label: 0_III.12.4.1 -->

Let $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ be two ringed spaces, $f : X \to Y$ a morphism of ringed spaces. One
can take the *hypercohomology* of $f_{*}$ with respect to any complex of $\mathcal{O}_{X}$-modules
$\mathcal{K}^{\bullet} = (\mathcal{K}^{i})_{i \in \mathbb{Z}}$ `(11.4.4)`, for in the abelian category of
$\mathcal{O}_{Y}$-modules, filtered inductive limits exist and are exact `(T, 3.1.1)`. The $\mathcal{O}_{Y}$-modules of
hypercohomology $R^{p} f_{*}(\mathcal{K}^{\bullet})$ will also be denoted $\mathcal{H}^{p}(f, \mathcal{K}^{\bullet})$ or
$\mathcal{H}^{p}(\mathcal{K}^{\bullet})$. Recall that $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is the
cohomology of the bicomplex of $\mathcal{O}_{Y}$-modules $f_{*}(\mathcal{L}^{\bullet\bullet})$, where
$\mathcal{L}^{\bullet\bullet}$ is an injective Cartan–Eilenberg resolution of $\mathcal{K}^{\bullet}$ in the category of
$\mathcal{O}_{X}$-modules; $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is the abutment of two spectral sequences
$'\mathcal{E}(f, \mathcal{K}^{\bullet})$ and $''\mathcal{E}(f, \mathcal{K}^{\bullet})$ whose `E_2` terms are given by

```text
  'E_2^{pq} = ℋ^p(ℋ^q(f, 𝒦^•))                                               (12.4.1.1)
  ″E_2^{pq} = ℋ^p(f, ℋ^q(𝒦^•))     (= R^p f_*(ℋ^q(𝒦^•)))                     (12.4.1.2)
```

In these formulas, we have adopted the general notation $T(A^{\bullet})$ for the transform of a complex by a functor
`(11.2.1)`, and one writes $\mathcal{H}^{p}(f, \mathcal{F})$ instead of $R^{p} f_{*}(\mathcal{F})$ for an
$\mathcal{O}_{X}$-module $\mathcal{F}$. Recall further that the sequence $'\mathcal{E}(f, \mathcal{K}^{\bullet})$ is
always *regular*; the two spectral sequences $'\mathcal{E}(f, \mathcal{K}^{\bullet})$ and $''\mathcal{E}(f,
\mathcal{K}^{\bullet})$ are *biregular* when $\mathcal{K}^{\bullet}$ is bounded below,

<!-- original page 63 -->

or when there exists an integer $m$ such that every $\mathcal{O}_{X}$-module admits a flasque resolution of length $\leq
m$ `(11.4.4)`.

**12.4.2.**

<!-- label: 0_III.12.4.2 -->

We shall likewise denote by $H^{\bullet}(X, \mathcal{K}^{\bullet})$ the hypercohomology of the functor $\Gamma$ with
respect to a complex $\mathcal{K}^{\bullet}$ of $\mathcal{O}_{X}$-modules; the $H^{p}(X, \mathcal{K}^{\bullet})$ are
therefore $\Gamma(X, \mathcal{O}_{X})$-modules. One can moreover consider $H^{\bullet}(X, \mathcal{K}^{\bullet})$ as a
particular case of $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$, where $f$ is a morphism of $(X, \mathcal{O}_{X})$
to a ringed space reduced to a point endowed with the ring $\Gamma(X, \mathcal{O}_{X})$.

For every open set $V$ of $X$, we shall write $H^{\bullet}(V, \mathcal{K}^{\bullet})$ instead of $H^{\bullet}(V,
\mathcal{K}^{\bullet} \mid V)$.

**Proposition (12.4.3).**

<!-- label: 0_III.12.4.3 -->

*For every integer $p \in \mathbb{Z}$, the $\mathcal{O}_{Y}$-module $\mathcal{H}^{p}(f, \mathcal{K}^{\bullet})$ is
canonically isomorphic to the sheaf associated to the presheaf $U \mapsto H^{p}(f^{-1}(U), \mathcal{K}^{\bullet})$ on
$Y$.*

**Proof.** Indeed, with the notation of `(12.4.1)`, the cohomology sheaf
$\mathcal{H}^{p}(f_{*}(\mathcal{L}^{\bullet\bullet}))$ is associated to the presheaf $U \mapsto H^{p}(\Gamma(U,
f_{*}(\mathcal{L}^{\bullet\bullet}))) = H^{p}(\Gamma(f^{-1}(U), \mathcal{L}^{\bullet\bullet}))$. But it is clear that
$\mathcal{L}^{\bullet\bullet} \mid f^{-1}(U)$ is an injective Cartan–Eilenberg resolution of $\mathcal{K}^{\bullet} \mid
f^{-1}(U)$ `(T, 3.1.3)`, so $H^{p}(\Gamma(f^{-1}(U), \mathcal{L}^{\bullet\bullet})) = H^{p}(f^{-1}(U),
\mathcal{K}^{\bullet})$ by definition.

**Proposition (12.4.4).**

<!-- label: 0_III.12.4.4 -->

*The hypercohomology $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is a cohomological functor in
$\mathcal{K}^{\bullet}$ in each of the following cases:*

*a) $\mathcal{K}^{\bullet}$ varies in the category of complexes bounded below.*

*b) There exists an integer $m$ such that every $\mathcal{O}_{X}$-module admits a flasque resolution of length $\leq
m$.*

*c) $X$ is a Noetherian space.*

**Proof.** Cases *a)* and *b)* are particular cases of `(11.5.4)`. On the other hand, case *c)* follows from `(11.5.2)`,
for one knows that in this case the functor $f_{*}$ commutes with inductive limits `(G, II, 3.10.1)`.

**12.4.5.**

<!-- label: 0_III.12.4.5 -->

Consider now an open cover $\mathfrak{U} = (U_{\alpha})$ of $X$, and for every complex of presheaves
$\mathcal{K}^{\bullet} = (\mathcal{K}^{j})$ on $X$, the bicomplex $C^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$,
whose component of indices $(i, j)$ is $C^{i}(\mathfrak{U}, \mathcal{K}^{j})$, the group of $i$-cochains alternating in
the nerve of $\mathfrak{U}$ with values in $\mathcal{K}^{j}$ `(G, II, 5.1)`. We shall say that the cohomology of this
bicomplex is the *hypercohomology of the cover $\mathfrak{U}$ with coefficients in $\mathcal{K}^{\bullet}$*, and we
shall denote it $H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet}) = H^{\bullet}(C^{\bullet}(\mathfrak{U},
\mathcal{K}^{\bullet}))$. The Leray spectral sequence of a cover `(T, 3.8.1 and G, II, 5.9.1)` generalizes as follows to
hypercohomology:

**Proposition (12.4.6).**

<!-- label: 0_III.12.4.6 -->

*Let $\mathcal{K}^{\bullet} = (\mathcal{K}^{j})$ be a complex of $\mathcal{O}_{X}$-modules. There exists a regular
spectral functor in $\mathcal{K}^{\bullet}$ having as abutment the hypercohomology $H^{\bullet}(X,
\mathcal{K}^{\bullet})$, and whose `E_2` term is given by*

$$ E^{pq}_{2} = H^{p}(\mathfrak{U}, h^{q}(\mathcal{K}^{\bullet})) (12.4.6.1) $$

*where $h^{q}(\mathcal{K}^{\bullet})$ denotes the complex of presheaves $V \mapsto H^{q}(V, \mathcal{K}^{\bullet})$ on
$X$. The preceding spectral sequence is biregular if $\mathcal{K}^{\bullet}$ is bounded below.*

**Proof.** Consider an injective Cartan–Eilenberg resolution $\mathcal{L}^{\bullet\bullet}$ of $\mathcal{K}^{\bullet}$,
and the tricomplex $C^{\bullet}(\mathfrak{U}, \mathcal{L}^{\bullet\bullet}) = (C^{i}(\mathfrak{U}, \mathcal{L}^{jk}))$;
consider this tricomplex first as a bicomplex for the degrees $i$ and $j + k$. Since $i$ takes only values $\geq 0$, the
second spectral sequence of this bicomplex is regular `(11.3.3)` and degenerate, for one has $H^{q}(\mathfrak{U},
\mathcal{L}^{jk}) = 0$ for every $q > 0$, the $\mathcal{O}_{X}$-modules $\mathcal{L}^{jk}$ being flasque sheaves

<!-- original page 64 -->

`(G, II, 5.2.3)`. One therefore has `(11.1.6)` a canonical isomorphism $H^{n}(C^{\bullet}(\mathfrak{U},
\mathcal{L}^{\bullet\bullet})) \xrightarrow{\sim} H^{n}(\Gamma(X, \mathcal{L}^{\bullet\bullet}))$ (by virtue of
`(G, II, 5.2.2)`), hence by definition `(12.4.2)` an isomorphism $H^{n}(C^{\bullet}(\mathfrak{U},
\mathcal{L}^{\bullet\bullet})) \xrightarrow{\sim} H^{n}(X, \mathcal{K}^{\bullet})$. Consider on the other hand the
tricomplex $C^{\bullet}(\mathfrak{U}, \mathcal{L}^{\bullet\bullet})$ as a bicomplex for the degrees $i + j$ and $k$.
Since $k$ takes only values $\geq 0$, the first spectral sequence of this bicomplex is always regular; it is biregular
if $\mathcal{L}^{jk} = 0$ for $j < j_{0}$, that is, when $\mathcal{K}^{\bullet}$ is bounded below `(11.3.3)`. This
spectral sequence is the one sought; indeed, for every $j$, $\mathcal{L}^{j\bullet}$ is an injective resolution of
$\mathcal{K}^{j}$; consequently, $H^{q}(C^{\bullet}(\mathfrak{U}, \mathcal{L}^{j\bullet}))$ is none other than the
complex of cochains $C^{\bullet}(\mathfrak{U}, h^{q}(\mathcal{K}^{j}))$, which completes the proof.

**Corollary (12.4.7).**

<!-- label: 0_III.12.4.7 -->

*If, for every simplex $\sigma$ of the nerve of $\mathfrak{U}$, and for every integer $i$, one has $H^{q}(U_{\sigma},
\mathcal{K}^{i}) = 0$ for $q > 0$, then one has a canonical isomorphism*

```text
  H^•(𝔘, 𝒦^•) ⥲ H^•(X, 𝒦^•).                                                 (12.4.7.1)
```

**Proof.** Indeed, the hypothesis entails that $C^{\bullet}(\mathfrak{U}, h^{q}(\mathcal{K}^{j})) = 0$ for $q > 0$,
hence $E^{pq}_{2} = 0$ for $q > 0$; the sequence `(12.4.6.1)` being degenerate and regular, the conclusion follows from
the definition `(12.4.5)` of $H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ and from `(11.1.6)`.

**12.4.8.**

<!-- label: 0_III.12.4.8 -->

Let $(X', \mathcal{O}_{X'})$ be a second ringed space, and let $f = (\psi, \theta)$ be a morphism from $X'$ to $X$. By
the same method as in `(12.1.3)` and `(12.1.4)`, one defines a di-homomorphism for the hypercohomology of a complex
$\mathcal{K}^{\bullet}$ of $\mathcal{O}_{X}$-modules

```text
  H^p(X, 𝒦^•) → H^p(X', f^*(𝒦^•)).                                           (12.4.8.1)
```

One starts from a Cartan–Eilenberg injective resolution $\mathcal{L}^{\bullet\bullet}$ of $\mathcal{K}^{\bullet}$, and
since $\psi^{*}$ is exact, $\psi^{*}(\mathcal{L}^{\bullet\bullet})$ is a Cartan–Eilenberg resolution of
$\psi^{*}(\mathcal{K}^{\bullet})$ in the category of $\psi^{*}(\mathcal{O}_{X})$-modules; there is then a morphism
$\psi^{*}(\mathcal{L}^{\bullet\bullet}) \to \mathcal{L}'^{\bullet\bullet}$, where $\mathcal{L}'^{\bullet\bullet}$ is a
Cartan–Eilenberg injective resolution of $\psi^{*}(\mathcal{K}^{\bullet})$, and from this one deduces a morphism for
cohomology $H^{\bullet}(X, \mathcal{K}^{\bullet}) \to H^{\bullet}(X', \psi^{*}(\mathcal{K}^{\bullet}))$; by composition
with the morphism deduced by functoriality from $\psi^{*}(\mathcal{K}^{\bullet}) \to f^{*}(\mathcal{K}^{\bullet})$, one
obtains the morphism `(12.4.8.1)` sought.

Starting from `(12.4.8.1)` and `(12.4.3)`, one can then, reasoning as in `(12.2.5)`, define, for two morphisms $f : X
\to Y$, $g : Y \to Z$ of ringed spaces, homomorphisms for the hypercohomology of a complex $\mathcal{K}^{\bullet}$ of
$\mathcal{O}_{X}$-modules

```text
  ℋ^n(g, f_*(𝒦^•)) → ℋ^n(h, 𝒦^•)                                             (12.4.8.2)
  ℋ^n(h, 𝒦^•) → g_*(ℋ^n(f, 𝒦^•)).                                            (12.4.8.3)
```

We leave the details of the definitions to the reader.
