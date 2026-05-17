# §2. Cohomological study of projective morphisms

<!-- original page 95 -->

## 2.1. Explicit calculations of certain cohomology groups

**2.1.1.**

<!-- label: III.2.1.1 -->

Let `X` be a prescheme and `ℒ` an invertible `𝒪_X`-module; consider the graded ring `(0_I, 5.4.6)`

```text
  S = Γ_*(X, ℒ) = ⊕_{n ∈ ℤ} Γ(X, ℒ^{⊗n}).                                    (2.1.1.1)
```

Let `(f_i)_{1 ≤ i ≤ r}` be a finite family of homogeneous elements of `S`, with `f_i ∈ S_{d_i}`; set

```text
  U_i = X_{f_i},   U = ⋃_i U_i,
```

and denote by `𝔘` the cover `(U_i)` of `U`. For every quasi-coherent `𝒪_X`-module `ℱ`, set

```text
  H^•(𝔘, ℱ(*)) = ⊕_{n ∈ ℤ} H^•(𝔘, ℱ ⊗ ℒ^{⊗n})                                (2.1.1.2)
```

```text
  H^•(U, ℱ(*)) = ⊕_{n ∈ ℤ} H^•(U, ℱ ⊗ ℒ^{⊗n}).                               (2.1.1.3)
```

The abelian groups `(2.1.1.2)` and `(2.1.1.3)` are *bigraded*, by setting

```text
  (H^•(𝔘, ℱ(*)))^{m,n} = H^m(𝔘, ℱ ⊗ ℒ^{⊗n})
```

and an analogous definition for `(2.1.1.3)`. For the second degree, it is clear that these groups are graded
`S`-modules, as follows for instance from the fact that `ℱ ↦ H^p(𝔘, ℱ)` and `ℱ ↦ H^p(U, ℱ)` are functors.

**2.1.2.**

<!-- label: III.2.1.2 -->

Consider now the graded `S`-module `(0_I, 5.4.6)`

```text
  M = Γ_*(ℱ) = H^0(X, ℱ(*)) = ⊕_{n ∈ ℤ} Γ(X, ℱ ⊗ ℒ^{⊗n}).                    (2.1.2.1)
```

<!-- original page 96 -->

If `X` is a prescheme whose underlying space is Noetherian, or a quasi-compact scheme, it follows from `(I, 9.3.1)`
that, setting as usual `U_{i_0 … i_p} = ⋂_{k=0}^p U_{i_k}`, we have, up to a canonical isomorphism,

```text
  Γ(U_{i_0 … i_p}, ℱ(*)) = H^0(U_{i_0 … i_p}, ℱ(*)) = M_{f_{i_0} … f_{i_p}}.
```

One can also, with the notation of `(1.2.2)`, identify `M_{f_{i_0} … f_{i_p}}` with `lim_→ M^{(n)}_{i_0 … i_p}`. This
identification is an isomorphism of graded `S`-modules, provided that one defines the degree of a homogeneous element
`ξ ∈ lim_→ M^{(n)}_{i_0 … i_p}` as follows: `ξ` is the canonical image of a homogeneous element
`x ∈ M^{(n)}_{i_0 … i_p} = M` of degree `m`; one then takes for the degree of `ξ` the number
`m − n (d_{i_0} + d_{i_1} + ⋯ + d_{i_p})`. Taking the definition of the homomorphisms
`φ_{nm} : M^{(n)}_{i_0 … i_p} → M^{(m)}_{i_0 … i_p}` `(1.2.2)` into account, one sees at once that this definition does
not depend on the "representative" `x` of `ξ` chosen. Denoting, as in `(1.2.2)`, by `C^p_a(M)` the set of alternating
maps from `[1, r]^{p+1}` to `M` (for every `n`), one defines in the same way as above a structure of graded `S`-module
on `lim_→ C^p_a(M)`; one has again as in `(1.2.2)`

```text
  C^p(𝔘, ℱ(*)) = lim_→ C^p_a(M),                                              (2.1.2.2)
```

the isomorphism of the two sides preserving degrees. One then has, as in `(1.2.2)`,

```text
  C'^p(𝔘, ℱ(*)) = C^{p+1}_a(𝐟, M) = lim_→ K^{p+1}(𝐟^n, M),                    (2.1.2.3)
```

the isomorphism preserving degrees: the degree of an element of `lim_→ K^{p+1}(𝐟^n, M)`, the canonical image of a
cochain `ζ ∈ K^{p+1}(𝐟^n, M)` whose values `ζ(i_0, …, i_p)` lie in a single homogeneous component `M_m` of `M`, is
`m − n(d_{i_0} + ⋯ + d_{i_p})`, and is independent of the choice of this cochain as a representative of the element
considered.

Since the preceding isomorphisms are compatible with the coboundary operators, we conclude, as in `(1.2.2)`, the
following.

**Proposition (2.1.3).**

<!-- label: III.2.1.3 -->

*Let `X` be a prescheme whose underlying space is Noetherian, or a quasi-compact scheme. There exists a canonical
isomorphism, functorial in `ℱ`,*

```text
  H^p(𝔘, ℱ(*)) ⥲ H^{p+1}(𝐟, M)                              for every p ≥ 1.   (2.1.3.1)
```

*Moreover, one has an exact sequence functorial in `ℱ`*

```text
  0 → H^0(𝐟, M) → M → H^0(𝔘, ℱ(*)) → H^1(𝐟, M) → 0.                          (2.1.3.2)
```

*Furthermore, all the homomorphisms introduced are of degree `0` for the graded `S`-module structures (`S` being the
ring `(2.1.1.1)`).*

<!-- original page 97 -->

**Corollary (2.1.4).**

<!-- label: III.2.1.4 -->

*If `X` is a quasi-compact scheme and the `U_i = X_{f_i}` are affine, there exists a canonical isomorphism, functorial
in `ℱ`, of degree `0`,*

```text
  H^p(U, ℱ(*)) ⥲ H^{p+1}(𝐟, M)                              for p ≥ 1         (2.1.4.1)
```

*and an exact sequence functorial in `ℱ`*

```text
  0 → H^0(𝐟, M) → M → H^0(U, ℱ(*)) → H^1(𝐟, M) → 0                           (2.1.4.2)
```

*where all homomorphisms are of degree `0`.*

**Proof.** It suffices to apply `(1.4.1)` to the result of `(2.1.3)`.

The "local" proposition analogous to `(2.1.3)` is the following.

**Proposition (2.1.5).**

<!-- label: III.2.1.5 -->

*Let `S` be a graded ring with positive degrees, `f_i (1 ≤ i ≤ r)` a homogeneous element of `S_+` of degree `d_i`, `M` a
graded `S`-module. Let `X = Proj(S)` be the homogeneous prime spectrum of `S` and set `U_i = D_+(f_i)`, `U = ⋃ U_i`,
`H^•(U, M̃(*)) = ⊕_n H^•(U, (M(n))∼)`. There then exist canonical isomorphisms functorial in `M`, of degree `0` for the
graded `S`-module structures,*

```text
  H^p(U, M̃(*)) ⥲ H^{p+1}(𝐟, M)                             for p ≥ 1         (2.1.5.1)
```

*and an exact sequence functorial in `M`*

```text
  0 → H^0(𝐟, M) → M → H^0(U, M̃(*)) → H^1(𝐟, M) → 0                          (2.1.5.2)
```

*where all homomorphisms are of degree `0`.*

**Proof.** We have `Γ(U_{i_0 … i_p}, (M(n))∼) = (M_{f_{i_0} … f_{i_p}})_n` by definition `(II, 2.5.2)`, hence
`Γ(U_{i_0 … i_p}, M̃(*)) = M_{f_{i_0} … f_{i_p}}`. The rest of the argument is then the same as for the proof of
`(2.1.4)`, taking into account that `X` is a scheme.

**Remarks (2.1.6).**

<!-- label: III.2.1.6 -->

(i) Under the conditions of `(2.1.5)`, the functors `M ↦ M_{f_{i_0} … f_{i_p}}` are exact in `M`, by virtue of
`(0_I, 1.3.2)`; the same reasoning as in `(1.2.5)` then shows that if `0 → M' → M → M'' → 0` is an exact sequence of
graded `S`-modules (where the homomorphisms are of degree `0`), one has commutative diagrams for every `p ≥ 0`

```text
  H^p(U, M̃''(*))    →    H^{p+1}(U, M̃'(*))

      ↓                          ↓

  H^{p+1}(𝐟, M'')   →    H^{p+2}(𝐟, M')                                      (2.1.6.1)
```

(ii) Proposition `(2.1.5)` will be especially interesting when `S` is an `A`-algebra generated by a finite number of
elements of degree `1`, `A` being assumed Noetherian; for

<!-- original page 98 -->

then, every quasi-coherent `𝒪_X`-module is of the form `M̃` `(II, 2.7.7)`.

**2.1.7.**

<!-- label: III.2.1.7 -->

We are going to apply `(2.1.5)` in the case `S = A[T_0, …, T_r]`, where `A` is an arbitrary ring, the `T_i` are
indeterminates, with `M = S` and `f_i = T_i`. One is therefore essentially reduced to computing `H^•(𝐓, S)`, where
`𝐓 = (T_i)_{0 ≤ i ≤ r}`.

**Lemma (2.1.8).**

<!-- label: III.2.1.8 -->

*If `S = A[T_0, …, T_r]`, one has, with `𝐓 = (T_i)_{0 ≤ i ≤ r}`,*

```text
  H^i(𝐓^n, S) = 0                                          if i ≠ r + 1      (2.1.8.1)
```

```text
  H^{r+1}(𝐓^n, S) = S/(𝐓^n).                                                 (2.1.8.2)
```

*The `A`-module `H^{r+1}(𝐓^n, S)` thus has a basis over `A` formed of the classes mod. `(𝐓^n)` of the monomials
`𝐓^𝐩 = T_0^{p_0} … T_r^{p_r}` with `𝐩 = (p_0, …, p_r)`, `0 ≤ p_i < n` for all `i`.*

**Proof.** This is an immediate consequence of `(1.1.3.5)` and Proposition `(1.1.4)`, whose hypotheses are trivially
verified.

**2.1.9.**

<!-- label: III.2.1.9 -->

Pass to the inductive limit on `n`; the relations `(2.1.8.1)` give `H^i(𝐓, S) = 0` for `i ≠ r + 1`. For `i = r + 1`, the
inductive system is formed of the `S/(𝐓^n)`, the homomorphism `φ_{nm} : S/(𝐓^n) → S/(𝐓^m)` for `0 ≤ n ≤ m` being
multiplication by `(T_0 … T_r)^{m−n}`. For `n ≥ sup(p_i)_{0 ≤ i ≤ r}`, denote by `ξ^{(n)}_{p_0, …, p_r}` the class of
`T_0^{n−p_0} … T_r^{n−p_r}` mod. `(𝐓^n)`; one then has `φ_{nm}(ξ^{(n)}_𝐩) = ξ^{(m)}_𝐩`, and these elements thus have the
same canonical image `ξ_𝐩 = ξ_{p_0, …, p_r}` in the inductive limit `H^{r+1}(𝐓, S)`; by virtue of the definition of
degree given in `(2.1.2)`, the degree of `ξ_𝐩` is therefore equal to `−|𝐩| = −(p_0 + p_1 + ⋯ + p_r)`. It is clear that
the `ξ^{(n)}_𝐩` for `0 < p_i ≤ n` and `0 ≤ i ≤ r` form a basis of `S/(𝐓^n)`. One immediately deduces from `(2.1.8)`:

**Corollary (2.1.10).**

<!-- label: III.2.1.10 -->

*With the notation of `(2.1.8)`, one has*

```text
  H^i(𝐓, S) = 0                                            for i ≠ r + 1     (2.1.10.1)
```

*and `H^{r+1}(𝐓, S)` is a free `A`-module with a basis formed of the elements `ξ_{p_0, …, p_r}` such that `p_i > 0` for
`0 ≤ i ≤ r`.*

**Remark (2.1.11).**

<!-- label: III.2.1.11 -->

Let `N` be an arbitrary `A`-module and set `M = S ⊗_A N`; the reasoning of `(2.1.8)` shows that one has more generally

```text
  H^i(𝐓^n, M) = 0                                          if i ≠ r + 1      (2.1.11.1)
```

```text
  H^{r+1}(𝐓^n, M) = (S/(𝐓^n)) ⊗_A N,                                         (2.1.11.2)
```

since the latter formula follows directly from `(1.1.3.5)`, and on the other hand it is clear that
`M / (T_0^n M + ⋯ + T_{r−1}^n M)` is identified with the tensor product `(S/(T_0^n S + ⋯ + T_{r−1}^n S)) ⊗_A N`, the
ideal `T_0^n S + ⋯ + T_{r−1}^n S` being a direct factor in the `A`-module `S`; this allows one to apply `(1.1.4)` to
`M`, and one thus obtains `(2.1.11.1)`.

Combining `(2.1.10)` and `(2.1.5)`, one obtains:

**Proposition (2.1.12).**

<!-- label: III.2.1.12 -->

*Let `A` be a ring, `r` an integer `> 0`, and `X = ℙ^r_A` `(II, 4.1.1)`. Then:*

*(i) One has `H^i(X, 𝒪_X(*)) = 0` for `i ≠ 0, r`.*

*(ii) The canonical homomorphism `α : S → H^0(X, 𝒪_X(*))` `(II, 2.6.2)` is bijective.*

<!-- original page 99 -->

*(iii) `H^r(X, 𝒪_X(*))` is a free `A`-module having a basis formed of elements `ξ_{p_0, …, p_r}`, where `p_i > 0` for
`0 ≤ i ≤ r`, `ξ_{p_0, …, p_r}` being of degree `−|𝐩| = −(p_0 + ⋯ + p_r)`, and the product `T_i · ξ_{p_0, …, p_r}` being
equal to `ξ_{p_0, …, p_i − 1, …, p_r}`.*

**Proof.** Note that, in the exact sequence `(2.1.5.2)` applied to `M = S = A[T_0, …, T_r]`, one has `H^0(𝐓, S) = 0` and
`H^1(𝐓, S) = 0` by `(2.1.10.1)`, and that Proposition `(2.1.5)` applies to `U = X`, since `X` is the union of the
`D_+(T_i)` `(II, 2.3.14)`. It remains to identify the map `S → H^0(X, 𝒪_X(*))` of the exact sequence `(2.1.5.1)` with
the canonical map `α`; but this follows from the canonical identification of `H^0(U, 𝒪_X(*))` and `H^0(𝔘, 𝒪_X(*))`.

**Corollary (2.1.13).**

<!-- label: III.2.1.13 -->

*The only values of `(i, n)` for which one can have `H^i(X, 𝒪_X(n)) ≠ 0` are the following: `i = 0` and `n ≥ 0`; `i = r`
and `n ≤ −(r + 1)`.*

Note that if `A ≠ 0`, one effectively has `H^i(X, 𝒪_X(n)) ≠ 0` for the pairs enumerated in `(2.1.13)`; this follows from
`(2.1.12)`, since `S_n` is then `≠ 0` for all degrees `n ≥ 0`.

In the applications which will be made in this chapter, we shall mostly use the less precise result:

**Corollary (2.1.14).**

<!-- label: III.2.1.14 -->

*The `A`-modules `H^i(X, 𝒪_X(n))` are free of finite type; if `i > 0`, they are zero for `n > 0`.*

**Proposition (2.1.15).**

<!-- label: III.2.1.15 -->

*Let `Y` be a prescheme, `ℰ` an `𝒪_Y`-module locally free of rank `r + 1`, `X = ℙ(ℰ)` the projective bundle defined by
`ℰ`, `f : X → Y` the structure morphism. The only values of `i` and `n` for which `R^i f_*(𝒪_X(n)) ≠ 0` are `i = 0` and
`n ≥ 0`, `i = r` and `n ≤ −(r + 1)`; in addition, the canonical homomorphism `(II, 3.3.2)`*

```text
  α : 𝐒_{𝒪_Y}(ℰ) → 𝚪_*(𝒪_X) = R^0 f_*(𝒪_X(*)) = ⊕_{n ∈ ℤ} f_*(𝒪_X(n))
```

*is an isomorphism.*

**Proof.** The question being local on `Y`, we may suppose `Y` affine with ring `A` and `ℰ = Ẽ`, where `E = A^{r+1}`;
one is then immediately reduced to `(2.1.12)`, taking `(1.4.11)` into account.

**Remark (2.1.16).**

<!-- label: III.2.1.16 -->

We shall later complete the results of `(2.1.15)` by proving the following propositions: set `ω = f^*(⋀^{r+1} ℰ)(−r−1)`,
which is an invertible `𝒪_X`-module. Then:

(i) One has a canonical isomorphism

```text
  ρ : R^r f_*(ω) ⥲ 𝒪_Y.                                                      (2.1.16.1)
```

(ii) The cup-product pairing `(0, 12.2.2)`

```text
  R^r f_*(𝒪_X(n)) × R^0 f_*(ω(−n)) → R^r f_*(ω)                              (2.1.16.2)
```

composed with the isomorphism `ρ^{−1}`, defines an isomorphism of `R^r f_*(𝒪_X(n))` onto the *dual* of the locally free
`𝒪_Y`-module

```text
  R^0 f_*(ω(−n)) = (⋀^{r+1} ℰ) ⊗_{𝒪_Y} (𝐒_{𝒪_Y}(ℰ))_{−n}.
```

<!-- original page 100 -->

## 2.2. The fundamental theorem of projective morphisms

**Theorem (2.2.1) (Serre).**

<!-- label: III.2.2.1 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a proper morphism, `ℒ` an invertible `𝒪_X`-module ample for `f`. For
every `𝒪_X`-module `ℱ`, set `ℱ(n) = ℱ ⊗_{𝒪_X} ℒ^{⊗n}` for every `n ∈ ℤ`. Then, for every coherent `𝒪_X`-module `ℱ`:*

*(i) The `R^q f_*(ℱ)` are coherent `𝒪_Y`-modules.*

*(ii) There exists an integer `N` such that for `n ≥ N`, one has `R^q f_*(ℱ(n)) = 0` for every `q > 0`.*

*(iii) There exists an integer `N` such that, for `n ≥ N`, the canonical homomorphism `f^*(f_*(ℱ(n))) → ℱ(n)` is
surjective.*

**Proof.** Let us first note that if the theorem is true when one replaces `ℒ` by `ℒ^{⊗d}` (`d > 0`), it is true in its
initial form. Indeed, one may then write `ℱ(n) = (ℱ ⊗ ℒ^{⊗r}) ⊗ ℒ^{⊗hd}` with `h ≥ 0` and `0 ≤ r < d`, and by
hypothesis, for each `r` there is an integer `N_r` such that for `h ≥ N_r`, properties (ii) and (iii) hold for the
`𝒪_X`-module `ℱ ⊗ ℒ^{⊗r}`; taking for `N` the largest of the `d N_r`, (ii) and (iii) will hold for `n ≥ N`. One may
therefore suppose `ℒ` very ample relative to `f` `(II, 4.6.11)`; consequently, there is a dominant `Y`-open immersion
`i : X → P`, where `P = Proj(𝒮)`, with `𝒮` a quasi-coherent graded `𝒪_Y`-algebra with positive degrees, in which `𝒮_1`
is of finite type and generates `𝒮`; in addition, `ℒ` is isomorphic to `i^*(𝒪_P(1))` `(II, 4.4.7)`. But since `f` is
proper, so is `i` `(II, 5.4.4)`, so `i` is an isomorphism `X ⥲ P`. One may thus restrict to the case where `X = Proj(𝒮)`
and `ℒ = 𝒪_X(1)`. Theorem `(2.2.1)` is then a consequence of the following.

**Proposition (2.2.2).**

<!-- label: III.2.2.2 -->

*Let `A` be a Noetherian ring, `S` an `A`-algebra graded with positive degrees, in which `S_1` is an `A`-module having a
system of `r + 1` generators, and which generates the algebra `S`. Let `X = Proj(S)`. For every coherent `𝒪_X`-module
`ℱ`:*

*(i) The `A`-modules `H^q(X, ℱ)` are of finite type.*

*(ii) One has `H^q(X, ℱ) = 0` for `q > r`.*

*(iii) There exists an integer `N` such that for `n ≥ N`, one has `H^q(X, ℱ(n)) = 0` for every `q > 0`.*

*(iv) There exists an integer `N` such that for `n ≥ N`, `ℱ(n)` is generated by its sections over `X`.*

**Proof.** Let us first show how `(2.2.2)` entails `(2.2.1)`: in `(2.2.1)` (reduced to the particular case `X = Proj(𝒮)`
considered above), `Y` is quasi-compact, so can be covered by a finite number of affine open sets, with Noetherian
rings, such that the restriction of `𝒮_1` to each of these open sets `U_α` is generated by a finite number of sections
of `𝒮_1` over `U_α`. Assuming `(2.2.2)` proved, it then suffices to take for `N` in parts (ii) and (iii) of `(2.2.1)`
the largest of the analogous integers corresponding to the `U_α` (taking `(1.4.11)` and `(II, 3.4.7)` into account).

To prove `(2.2.2)`, note that `X` identifies with a closed subscheme of `P = ℙ^r_A` `(II, 3.6.2)`; in addition, if
`j : X → P` is the canonical injection, `j_*(ℱ)` is a coherent `𝒪_P`-module, and one has `j_*(ℱ(n)) = (j_*(ℱ))(n)`
`(II, 3.4.5 and 3.5.2)`. Taking `(G, II, cor. of th. 4.9.1)` into account, one is therefore reduced to proving `(2.2.2)`
in the particular case where `X = ℙ^r_A` and `S = A[T_0, …, T_r]`. As `X` is covered by the affine opens

<!-- original page 101 -->

`D_+(T_i)` in number `r + 1`, (ii) results from `(1.4.12)`. Note on the other hand that (iv) has already been proved
`(II, 2.7.9)`.

We shall prove (i) and (iii) simultaneously. Note that these assertions are true for `ℱ = 𝒪_X(m)` `(2.1.13)`; they are
therefore also true when `ℱ` is a direct sum of a finite number of `𝒪_X`-modules of the form `𝒪_X(m_j)`. On the other
hand, (i) and (iii) are trivially true for `q > r` by virtue of (ii). We shall proceed by *descending induction* on `q`.
We know that `ℱ` is isomorphic to a quotient of a direct sum `ℰ` of a finite number of sheaves `𝒪_X(m_j)`
`(II, 2.7.10)`; in other words, one has an exact sequence `0 → ℛ → ℰ → ℱ → 0`, where `ℛ` is coherent `(0_I, 5.3.3)` and
`ℰ` satisfies (i) and (iii). Since `ℱ ↦ ℱ(n)` is an exact functor in `ℱ`, one also has the exact sequence

```text
  0 → ℛ(n) → ℰ(n) → ℱ(n) → 0
```

for every `n ∈ ℤ`. One deduces the exact cohomology sequence

```text
  H^{q−1}(X, ℰ(n)) → H^{q−1}(X, ℱ(n)) → H^q(X, ℛ(n)).
```

Since `ℰ(n)` is a direct sum of the `𝒪_X(n + m_j)` `(II, 2.5.14)`, `H^{q−1}(X, ℰ(n))` is of finite type, and so is
`H^q(X, ℛ(n))` by the induction hypothesis; since `A` is Noetherian, one concludes that `H^{q−1}(X, ℱ(n))` is of finite
type for every `n ∈ ℤ`, and in particular for `n = 0`. On the other hand, by the induction hypothesis, there exists an
integer `N` such that for `n ≥ N` one has `H^q(X, ℛ(n)) = 0`; furthermore, one may also suppose `N` chosen so that
`H^{q−1}(X, ℰ(n)) = 0` for `n ≥ N`, since `ℰ` satisfies (iii); one concludes that `H^{q−1}(X, ℱ(n)) = 0` for `n ≥ N`,
which completes the proof.

**Corollary (2.2.3).**

<!-- label: III.2.2.3 -->

*Under the hypotheses of `(2.2.1)`, let `ℱ → 𝒢 → ℋ` be an exact sequence of coherent `𝒪_X`-modules. There then exists an
integer `N` such that for `n ≥ N`, the sequence*

```text
  f_*(ℱ(n)) → f_*(𝒢(n)) → f_*(ℋ(n))
```

*is exact.*

**Proof.** Let `ℱ'`, `𝒢'`, `𝒢''` be the kernel, image, and cokernel of `ℱ → 𝒢`; `𝒢'` is the kernel and `𝒢''` the image
of `𝒢 → ℋ`, let `ℋ''` be the cokernel of this homomorphism; all these `𝒪_X`-modules are coherent `(0_I, 5.3.4)`. Since
`ℱ ↦ ℱ(n)` is an exact functor in `ℱ`, it suffices to show that for `n` large enough, each of the sequences

```text
  0 → f_*(ℱ'(n)) → f_*(ℱ(n)) → f_*(𝒢'(n)) → 0
  0 → f_*(𝒢'(n)) → f_*(𝒢(n)) → f_*(𝒢''(n)) → 0
  0 → f_*(𝒢''(n)) → f_*(ℋ(n)) → f_*(ℋ''(n)) → 0
```

is exact; consequently, one may assume that `0 → ℱ → 𝒢 → ℋ → 0` is exact. One then has the exact cohomology sequence

```text
  0 → f_*(ℱ(n)) → f_*(𝒢(n)) → f_*(ℋ(n)) → R^1 f_*(ℱ(n)) → ⋯
```

and the conclusion follows from `(2.2.1, (ii))`.

**Corollary (2.2.4).**

<!-- label: III.2.2.4 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a morphism of finite type, `ℒ` an invertible `𝒪_X`-module ample for `f`;
for every `𝒪_X`-module `ℱ`, set `ℱ(n) = ℱ ⊗_{𝒪_X} ℒ^{⊗n}` (for `n ∈ ℤ`). Let `ℱ → 𝒢 → ℋ` be an exact sequence of
coherent `𝒪_X`-modules,*

<!-- original page 102 -->

*such that the supports of `ℱ` and `ℋ` are proper over `Y` `(II, 5.4.10)`. There then exists an integer `N` such that,
for `n ≥ N`, the sequence*

```text
  f_*(ℱ(n)) → f_*(𝒢(n)) → f_*(ℋ(n))
```

*is exact.*

**Proof.** The same reasoning as at the beginning of `(2.2.1)` shows that if the corollary is true for `ℒ^{⊗d}`
(`d > 0`), it is also true for `ℒ`; one may therefore restrict to the case where `ℒ` is very ample for `f`
`(II, 4.6.11)`, and consequently one may identify `X` with an open set in a `Y`-scheme `Z = Proj(𝒮)`, where `𝒮` is a
quasi-coherent graded `𝒪_Y`-algebra with positive degrees, in which `𝒮_1` is of finite type and generates `𝒮`, so that
`ℒ = i^*(𝒪_Z(1))`, where `i` is the canonical immersion `X → Z` `(II, 4.4.7)`. This being so, as `Supp(𝒢)` is closed in
`X` and contained in `Supp(ℱ) ∩ Supp(ℋ)`, it is proper over `Y`; the supports of `ℱ`, `𝒢`, `ℋ` are thus closed in `Z`
`(II, 5.4.10)`. The sheaves `ℱ' = i_*(ℱ)`, `𝒢' = i_*(𝒢)`, `ℋ' = i_*(ℋ)` are therefore coherent `𝒪_Z`-modules, and the
sequence `ℱ' → 𝒢' → ℋ'` is exact; in addition, if `g : Z → Y` is the structure morphism, one has `f = g ∘ i`, and it is
clear that `ℱ(n) = i^*(ℱ'(n))` and similarly for `𝒢` and `ℋ`; the conclusion thus follows from `(2.2.3)` applied to
`ℱ'`, `𝒢'`, `ℋ'`.

**Remarks (2.2.5).**

<!-- label: III.2.2.5 -->

(i) Assertion (i) of `(2.2.1)` is still true when one supposes only that `Y` is *locally Noetherian*; indeed, the
property is evidently local on `Y`; on the other hand, the hypotheses of `(2.2.1)` imply that for every open `U ⊂ Y`,
the restriction of `f` to `f^{−1}(U)` is a projective morphism `f^{−1}(U) → U` `(II, 5.5.5, (iii))` and `ℒ ∣ f^{−1}(U)`
is ample for this morphism `(II, 4.6.4)`.

(ii) Assertion (iii) of `(2.2.1)` is still valid, as we have seen, when one supposes only that `X` is a quasi-compact
scheme or a prescheme whose underlying space is Noetherian, and `f : X → Y` a quasi-compact morphism `(II, 4.6.8)`. But
it should be noted that even when one supposes that `Y` is the spectrum of a field `K` and that `f` is quasi-projective,
assertion (ii) of `(2.2.1)` is no longer necessarily verified. For example, let `X' = Spec(K[T_0, …, T_r])` and let `X`
be the union of the affine opens `D(T_i)` of `X'` (`0 ≤ i ≤ r`); since the immersion `X → X'` is quasi-compact, the
structure morphism `f : X → Y` is quasi-affine `(II, 5.1.10)`, so `𝒪_X` is very ample for `f` `(II, 5.1.6)`. But the
ring `Γ(X, 𝒪_X)` identifies with the intersection of the rings of fractions `(K[T_0, …, T_r])_{T_i}` for `0 ≤ i ≤ r`
`(I, 8.2.1.1)`, that is, with `K[T_0, …, T_r]`. Consequently, it follows from formulas `(1.4.3.1)` and `(1.1.3.5)` that
one has `H^r(X, 𝒪_X^{⊗n}) = H^r(X, 𝒪_X) = A ≠ 0` for every `n`.

## 2.3. Application to graded sheaves of algebras and of modules

**Theorem (2.3.1).**

<!-- label: III.2.3.1 -->

*Let `Y` be a Noetherian prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra of finite type with positive degrees,
`X = Proj(𝒮)`, `q : X → Y` the structure morphism, `ℳ` a quasi-coherent graded `𝒮`-module satisfying condition `(TF)`.
Then there exists an integer `N` such that, for `n ≥ N`, the canonical homomorphism `(II, 8.14.5.1)`*

```text
  α_n : ℳ_n → q_*(𝒫roj(ℳ(n))) = q_*((𝒫roj(ℳ))_n)
```

<!-- original page 103 -->

*is bijective. In other words, the canonical homomorphism*

```text
  α : ℳ → 𝚪_*(𝒫roj(ℳ))
```

*is a `(TN)`-isomorphism.*

**Proof.** One may restrict to the case where `ℳ` is an `𝒮`-module of finite type `(II, 3.4.2)`.

As `Y` is quasi-compact, there exists an integer `d > 0` such that `𝒮^{(d)}` is generated by the quasi-coherent
`𝒪_Y`-module `𝒮_d`, the latter being of finite type `(II, 3.1.10)`, hence coherent since `Y` is Noetherian. Note now
that `ℳ` is a direct sum of the `ℳ^{(d,k)}` for `0 ≤ k < d`, and that each of the `ℳ^{(d,k)}` is a quasi-coherent
`𝒮^{(d)}`-module of finite type, as follows from `(II, 2.1.6, (iii))`, the question being local on `Y`. Now, it
obviously suffices to prove that each of the canonical homomorphisms `α : ℳ^{(d,k)} → 𝚪_*(𝒫roj(ℳ))^{(d,k)}` is a
`(TN)`-isomorphism. Taking `(II, 8.14.13)` into account (and notably the diagram `(8.14.13.4)`), one sees that one is
reduced to proving the theorem when `𝒮` is generated by `𝒮_1` and `𝒮_1` is a coherent `𝒪_Y`-module. Since `Y` is
Noetherian, the same reasoning as at the beginning of `(2.2.2)` shows that one may restrict to the case where
`Y = Spec(A)`, `𝒮 = S̃`, `ℳ = M̃`, `A` being a Noetherian ring, `S_1` an `A`-module of finite type and `M` a graded
`S`-module of finite type. Let us show that it then suffices to prove the theorem when `M = S`. Indeed, in the general
case, one has an exact sequence `L' → L → M → 0`, where `L` and `L'` are direct sums of graded modules of the form
`S(m)`. If the result is true for `M = S`, it is also true for `M = S(m)`, hence for `L` and `L'`. Consider then the
commutative diagram

```text
  L̃'_n         →    L̃_n          →    M̃_n          →    0

   ↓ α_n              ↓ α_n              ↓ α_n

  q_*(L̃'(n))   →    q_*(L̃(n))    →    q_*(M̃(n))    →    0
```

The second line is exact by virtue of `(2.2.3)` as soon as `n` is large enough; as the same holds for the first, and as
the two left vertical arrows are isomorphisms, so is the third.

This being so, to prove the theorem when `M = S`, suppose first that `S = A[T_0, …, T_r]` (`T_i` indeterminates); in
this case, our assertion is none other than `(2.1.11, (ii))`. In the general case, `S` identifies with a quotient of a
ring `S' = A[T_0, …, T_r]` by a graded ideal, hence `X` with a closed subscheme of `X' = ℙ^r_A` `(II, 2.9.2)`. If `j` is
the canonical injection `X → X'`, `j_*(S̃(n))` is none other than the `𝒪_{X'}`-module `(𝒫roj(S̃))(n)` where `S` is
considered as a graded `S'`-module; this follows immediately from `(II, 2.8.7)`. As `j_*(S̃(n))` is an `𝒪_{X'}`-module
satisfying `(TF)`, the canonical homomorphism `α_n : S_n → Γ(X', j_*(S̃(n)))` is bijective for `n` large enough, by
virtue of what precedes; this completes the proof, since `Γ(X', j_*(S̃(n))) = Γ(X, S̃(n))`.

<!-- original page 104 -->

**Corollary (2.3.2).**

<!-- label: III.2.3.2 -->

*Under the hypotheses of `(2.3.1)`, let `𝒮_X = ⊕_{n ∈ ℤ} 𝒪_X(n)`, and let `ℱ` be a quasi-coherent graded `𝒮_X`-module of
finite type. Then `𝚪_*(ℱ)` satisfies condition `(TF)`.*

**Proof.** We have seen in the proof of `(2.3.1)` that `X`, which is isomorphic to `Proj(𝒮^{(d)})` `(II, 3.1.8)`, is of
finite type over `Y` `(II, 3.4.1)`. It then follows from `(II, 8.14.9)` that `ℱ` is isomorphic to an `𝒪_X`-graded module
of the form `𝒫roj(ℳ)`, where `ℳ` is a quasi-coherent graded `𝒮`-module of finite type. By virtue of `(2.3.1)`, `𝚪_*(ℱ)`
is `(TN)`-isomorphic to `ℳ`, and consequently satisfies `(TF)`.

**Scholium (2.3.3).**

<!-- label: III.2.3.3 -->

Let `Y` be a Noetherian prescheme, `𝒮` an `𝒪_Y`-algebra graded satisfying the conditions of `(2.3.1)` and `X = Proj(𝒮)`.
Let `𝐊_𝒮` be the abelian category of quasi-coherent graded `𝒮`-modules satisfying `(TF)`, `𝐊'_𝒮` the subcategory of
`𝐊_𝒮` formed of `𝒮`-modules satisfying `(TN)`; finally, let `𝐊_X` be the category of quasi-coherent graded `𝒮_X`-modules
of finite type `ℱ` (which amounts to saying, since `𝒮_X` is periodic `(II, 8.14.4 and 8.14.12)`, that the `ℱ_i` are
coherent `𝒪_X`-modules). Then the functors `ℳ ↦ 𝒫roj(ℳ)` in `𝐊_𝒮` and `ℱ ↦ 𝚪_*(ℱ)` in `𝐊_X` define, by virtue of
`(II, 8.14.8 and 8.14.10)` and `(2.3.2)`, an *equivalence* `(T, I, 1.2)` of the quotient category `𝐊_𝒮 / 𝐊'_𝒮`
`(T, I, 1.11)` with the category `𝐊_X`. When `𝒮` is generated by `𝒮_1`, one may replace `𝐊_X` by the category of
coherent `𝒪_X`-modules `(II, 8.14.12)`.

**Proposition (2.3.4).**

<!-- label: III.2.3.4 -->

*Let `Y` be a Noetherian prescheme.*

*(i) Let `𝒮` be a quasi-coherent graded `𝒪_Y`-algebra of finite type with positive degrees. Let `X = Proj(𝒮)` and
`𝒮_X = 𝒫roj(𝒮) = ⊕_{n ∈ ℤ} 𝒪_X(n)`. Then `𝒮_X` is a periodic graded `𝒪_Y`-algebra `(II, 8.14.12)` whose homogeneous
components `(𝒮_X)_n = 𝒪_X(n)` are coherent `𝒪_X`-modules, and if `d > 0` is a period of `𝒮_X`, `(𝒮_X)_d = 𝒪_X(d)` is an
invertible `𝒪_X`-module `Y`-ample. In addition, the canonical homomorphism `α : 𝒮 → 𝚪_*(𝒮_X)` is a `(TN)`-isomorphism.*

*(ii) Conversely, let `q : X → Y` be a projective morphism, and let `𝒮'` be a graded `𝒪_X`-algebra whose homogeneous
components `𝒮'_n` (`n ∈ ℤ`) are coherent `𝒪_X`-modules, and which admits a period `d > 0` such that `𝒮'_d` is an
invertible `𝒪_X`-module ample for `q`. Then `𝒮 = ⊕_{n ≥ 0} q_*(𝒮'_n)` is a quasi-coherent graded `𝒪_Y`-algebra with
positive degrees of finite type, and there exists a `Y`-isomorphism `r : X ⥲ Proj(𝒮)` such that `r^*(𝒫roj(𝒮))` is
isomorphic (as a graded `𝒪_X`-algebra) to `𝒮'`.*

**Proof.** (i) All the assertions have essentially already been proved, the last being none other than a particular case
of `(2.3.2)`. The fact that `𝒮_X` is periodic has been seen in `(II, 8.14.14)`, and the fact that there is a period
`d > 0` such that `𝒪_X(d)` is invertible and `Y`-ample is none other than `(II, 4.6.18)`. Finally, for `0 ≤ k < d`,
`(𝒮_X)^{(d,k)}` is a `(𝒮_X)^{(d)}`-module of finite type `(II, 8.14.14)`, so each of the `(𝒮_X)_n` is a quasi-coherent
`𝒮_X`-module of finite type by virtue of `(II, 2.1.6, (ii))`, the question being local; as `𝒮_X` is coherent, so are the
`(𝒮_X)_n`.

(ii) Up to replacing the period `d` by one of its multiples, one may suppose that `ℒ = 𝒮'_d` is an `𝒪_X`-module very
ample relative to `q` `(II, 4.6.11)`. We have in addition `𝒮'^{(d)} = ⊕ ℒ^{⊗n}` by hypothesis, so
`𝒮^{(d)} = ⊕ q_*(ℒ^{⊗n})`; we know `(II, 3.1.8 and 3.2.9)` that there is a `Y`-isomorphism `s` of `X' = Proj(𝒮)` onto
`X'' = Proj(𝒮^{(d)})` such that

<!-- original page 105 -->

`s^*(𝒪_{X''}(n)) = 𝒪_{X'}(nd)`. One will therefore establish the existence of a `Y`-isomorphism `X ⥲ X'` if one proves
the following.

**Proposition (2.3.4.1).**

<!-- label: III.2.3.4.1 -->

*Let `Y` be a Noetherian prescheme, `q : X → Y` a projective morphism, `ℒ` an invertible `𝒪_X`-module very ample for
`q`. Then `𝒮 = ⊕_{n ≥ 0} q_*(ℒ^{⊗n})` is a quasi-coherent graded `𝒪_Y`-algebra of finite type, such that `𝒮_n = 𝒮_1^n`
for `n` large enough, and there exists a `Y`-isomorphism `r : X ⥲ P = Proj(𝒮)` such that `ℒ = r^*(𝒪_P(1))`.*

**Proof.** As `q` is a projective morphism, it follows from `(II, 5.4.4 and 4.4.7)` that there exists a `Y`-isomorphism
`r' : X ⥲ P' = Proj(𝒯)`, where `𝒯` is a quasi-coherent `𝒪_Y`-algebra such that `𝒯_1` is an `𝒪_Y`-module of finite type
and generates `𝒯`, and one has `ℒ = r'^*(𝒪_{P'}(1))`. One then has `𝒮 = ⊕_{n ≥ 0} q'_*(𝒪_{P'}(n))`, where `q' : P' → Y`
is the structure morphism, and it follows from `(2.3.1)` that for `n` large enough, the canonical homomorphism
`α_n : 𝒯_n → 𝒮_n = q'_*(𝒪_{P'}(n))` is bijective; as `𝒯_n = 𝒯_1^n`, one has *a fortiori* `𝒮_n = 𝒮_1^n` as soon as `n` is
large enough. In addition, as the canonical homomorphism `α : 𝒯 → 𝒮` of graded `𝒪_Y`-algebras is a `(TN)`-isomorphism,
`Φ = Proj(α) : Proj(𝒮) → Proj(𝒯)` is an isomorphism `(II, 3.6.1)` and one has `Φ_*(𝒪_P(n)) = (𝒪_{P'}(n))_{[α]}`
`(II, 3.5.2)`; but since the `𝒯`-graded modules `(𝒮(n))_{[α]}` and `𝒯(n)` are `(TN)`-isomorphic, one has
`Φ_*(𝒪_P(n)) = 𝒪_{P'}(n)` for every `n` `(II, 3.4.2)`; to complete the proof of `(2.3.4.1)`, it remains to show that `𝒮`
is an `𝒪_Y`-algebra of finite type; now the `𝒮_n = q'_*(𝒪_{P'}(n))` are coherent `𝒪_Y`-modules by virtue of `(2.2.1)`
and, since `𝒮_n = 𝒮_1^n` for `n ≥ n_0`, `𝒮` is generated by `⊕_{i ≤ n_0} 𝒮_i`, which is coherent, whence our assertion
`(I, 9.6.2)`.

Let us return to the proof of `(2.3.4)`, whose notation we resume. We have proved the existence of a `Y`-isomorphism
`r'' : X ⥲ X''` such that `r''^*(ℒ^{⊗n}) = 𝒪_{X''}(nd)` for every `n ∈ ℤ`; we shall denote by `q''` the structure
morphism `X'' → Y`. Note now that `𝒮'` is a direct sum of the `𝒮'^{(d)}`-graded modules `𝒮'^{(d,k)}`; each of the latter
is a quasi-coherent `𝒮'^{(d)}`-module of finite type, by virtue of the periodicity of `𝒮'` and the hypothesis that the
`𝒮'_n` are `𝒪_X`-modules of finite type `(II, 8.14.12)`. Set `ℱ^{(k)} = r''_*(𝒮'^{(d,k)})`, so the `ℱ^{(k)}` are
quasi-coherent graded `𝒮_{X''}`-modules of finite type; consequently `(II, 8.14.8)`, the canonical homomorphism
`β : 𝒫roj(𝚪_*(ℱ^{(k)})) → ℱ^{(k)}` is an isomorphism of `𝒮_{X''}`-modules. But one has
`q''_*((ℱ^{(k)})_n) = q_*((𝒮'^{(d,k)})_n)` and for `n ≥ 0`, this last `𝒪_Y`-module is by definition equal to
`(𝒮^{(d,k)})_n`. In other words, the canonical injection `𝒮^{(d,k)} → 𝚪_*(ℱ^{(k)})` is a `(TN)`-isomorphism, hence
`(II, 3.4.2)` one has `𝒫roj(𝒮^{(d,k)}) = 𝒫roj(𝚪_*(ℱ^{(k)}))`, and consequently `r''^*(𝒫roj(𝒮^{(d,k)})) = 𝒮'^{(d,k)}`. It
remains to note that `𝒫roj(𝒮^{(d,k)}) = (𝒫roj(𝒮))^{(d,k)}` up to a canonical isomorphism `(II, 8.14.13.1)` in order to
have proved the isomorphism of `r^*(𝒫roj(𝒮))` and `𝒮'`. Finally, by virtue of `(2.3.2)`, each of the `𝚪_*(ℱ^{(k)})`
satisfies condition `(TF)`, so the same holds for each of the `𝒮^{(d,k)}`; in addition, since the `𝒮'_n` are coherent,
the same holds for the `𝒮_n = q_*(𝒮'_n)` by `(2.2.1)`, and one concludes at once that the `𝒮_n` are `𝒪_Y`-modules of
finite type. As we have seen in `(2.3.4.1)` that `𝒮^{(d)}` is an `𝒪_Y`-algebra of finite type, one concludes that `𝒮` is
also an `𝒪_Y`-algebra of finite type.

<!-- original page 106 -->

**Proposition (2.3.5).**

<!-- label: III.2.3.5 -->

*Let `Y` be an integral Noetherian prescheme, `X` an integral prescheme, `f : X → Y` a birational projective morphism.
There then exists a coherent fractional ideal sheaf `𝒥 ⊂ ℛ(Y)` `(II, 8.1.2)` such that `X` is `Y`-isomorphic to the
prescheme obtained by blowing up `𝒥` `(II, 8.1.3)`. In addition, there exists an open set `U` of `Y` such that the
restriction of `f` to `f^{−1}(U)` is an isomorphism of `f^{−1}(U)` onto `U` (cf. `(I, 6.5.5)`), and such that `𝒥 ∣ U` is
invertible.*

**Proof.** As there exists an invertible `𝒪_X`-module `ℒ` very ample for `f` `(II, 4.4.2 and 5.3.2)`, one may apply
`(2.3.4.1)`, and one sees that `X` identifies with `Proj(𝒮)`, where `𝒮 = ⊕ f_*(ℒ^{⊗n})`. We know in addition that the
`f_*(ℒ^{⊗n})` are torsion-free `𝒪_Y`-modules `(I, 7.4.5)`, so the same holds for the `𝒪_Y`-module `𝒮`, and consequently
`𝒮` identifies canonically with a sub-`𝒪_Y`-module of `𝒮 ⊗_{𝒪_Y} ℛ(Y)` `(I, 7.4.1)`; the latter is a *simple* sheaf
`(I, 7.3.6)`, which is known when one knows its restriction to a nonempty open set, for instance to a nonempty open
`U' ⊂ U` such that `ℒ ∣ f^{−1}(U')` is isomorphic to `𝒪_X ∣ f^{−1}(U')`. Since by hypothesis the `f_*(ℒ^{⊗n}) ∣ U'` are
then isomorphic to `𝒪_Y ∣ U'`, one sees that `𝒮 ⊗_{𝒪_Y} ℛ(Y)` is an `ℛ(Y)`-module isomorphic to `ℛ(Y)[T]`, where `T` is
an indeterminate, and `𝒮` is `(TN)`-isomorphic to the sub-`𝒪_Y`-algebra generated by the canonical image of `f_*(ℒ)` in
`𝒮 ⊗ ℛ(Y)` `(2.3.4.1)`; but if one identifies `𝒮 ⊗ ℛ(Y)` with `ℛ(Y)[T]`, the image of `f_*(ℒ)` identifies with `𝒥 · T`,
where `𝒥` is a coherent sub-`𝒪_Y`-module `(2.2.1)` of `ℛ(Y)`, whose restriction to `U'` is isomorphic to `𝒪_Y ∣ U'`, and
which consequently is such that `𝒥 ∣ U` is invertible. One then sees that `𝒮` is `(TN)`-isomorphic to `⊕ 𝒥^n`, which
completes the proof.

**Corollary (2.3.6).**

<!-- label: III.2.3.6 -->

*Under the hypotheses of `(2.3.5)`, suppose in addition that for every coherent sub-`𝒪_Y`-module `𝒥 ≠ 0` of `ℛ(Y)`,
there exists an invertible `𝒪_Y`-module `ℒ` such that `Γ(Y, ℒ ⊗_{𝒪_Y} ℋom(𝒥, 𝒪_Y)) ≠ 0`; then, in the statement of
`(2.3.5)`, one may suppose that `𝒥` is an ideal of `𝒪_Y`. This additional condition is always satisfied if there exists
an ample `𝒪_Y`-module.*

**Proof.** Indeed, one has `(0_I, 5.4.2)`

```text
  ℒ ⊗ ℋom(𝒥, 𝒪_Y) = ℋom(ℒ^{−1}, ℋom(𝒥, 𝒪_Y)) = ℋom(𝒥 ⊗ ℒ^{−1}, 𝒪_Y);
```

the hypothesis thus signifies that there is a nonzero homomorphism `u` of `𝒥 ⊗ ℒ^{−1}` into `𝒪_Y`. As, for every
`y ∈ Y`, `(𝒥 ⊗ ℒ^{−1})_y` identifies with a sub-`𝒪_y`-module of the field of fractions `(ℛ(Y))_y` of `𝒪_y` `(I, 7.1.5)`,
`u_y` is necessarily injective, so `u` is an isomorphism of `𝒥 ⊗ ℒ^{−1}` onto an ideal `𝒥'` of `𝒪_Y`. But since
`Proj(⊕_{n ≥ 0} 𝒥^n)` and `Proj(⊕_{n ≥ 0} (𝒥 ⊗ ℒ^{−1})^n)` are `Y`-isomorphic `(II, 3.1.8)`, this proves the first
assertion of the corollary. To prove the second, note that `ℱ = ℋom_{𝒪_Y}(𝒥, 𝒪_Y)` is coherent and `≠ 0`, since there
exists an open set `U` of `Y` such that `𝒥 ∣ U` is invertible. If `ℒ` is an ample `𝒪_Y`-module, there exists an integer
`n` such that `ℱ(n) = ℱ ⊗ ℒ^{⊗n}` is generated by its sections over `Y` `(II, 4.5.5)`; *a fortiori*, one has
`Γ(Y, ℱ(n)) ≠ 0`, whence the conclusion.

**Corollary (2.3.7).**

<!-- label: III.2.3.7 -->

*Let `X` and `Y` be two integral schemes, projective over a field `k`, and let `f : X → Y` be a birational `k`-morphism.
Then `X` is `k`-isomorphic to a `k`-scheme obtained by blowing up a closed subscheme `Y'` (not necessarily reduced) of
`Y`.*

<!-- original page 107 -->

**Proof.** Indeed, `f` is projective `(II, 5.5.5, (v))`, and as `Y` is projective over `k`, the additional condition of
`(2.3.6)` is satisfied; it then suffices to consider the closed subscheme `Y'` of `Y` defined by the coherent ideal `𝒥`
of cor. `(2.3.6)`.

**Remark (2.3.8).**

<!-- label: III.2.3.8 -->

In Chap. IV, in studying the notion of divisor, we shall see that if, in the statement of `(2.3.5)`, one supposes that
the rings `𝒪_y` (`y ∈ Y`) are factorial (which is the case for instance if `Y` is non-singular), then `X` may be deduced
from `Y` by blowing up a closed sub-prescheme `Y'` of `Y` whose underlying space is contained in `Y − U`.

## 2.4. A generalization of the fundamental theorem

**Theorem (2.4.1).**

<!-- label: III.2.4.1 -->

*Let `Y` be a Noetherian prescheme, `𝒮` a quasi-coherent `𝒪_Y`-algebra of finite type. Let `f : X → Y` be a projective
morphism, `𝒮' = f^*(𝒮)`, `ℳ` a quasi-coherent `𝒮'`-module of finite type. Then:*

*(i) For every `p ∈ ℤ`, `R^p f_*(ℳ)` is an `𝒮`-module of finite type.*

*(ii) Let in addition `ℒ` be an invertible `𝒪_X`-module ample for `f`, and set `ℳ(n) = ℳ ⊗ ℒ^{⊗n}` for every `n ∈ ℤ`.
There exists an integer `N` such that, for `n ≥ N`, one has*

```text
  R^p f_*(ℳ(n)) = 0                                                          (2.4.1.1)
```

*for every `p > 0`, and the canonical homomorphism `f^*(f_*(ℳ(n))) → ℳ(n)` `(0_I, 4.4.3)` is surjective.*

**Proof.** Set `Y' = Spec(𝒮)`, `X' = Spec(𝒮')`, so that `X' = X ×_Y Y'` `(II, 1.5.5)`; let `g : Y' → Y`, `g' : X' → X`
be the structure morphisms, which are affine by definition, and `f' = f_{(Y')} : X' → Y'`; one therefore has a
commutative diagram

```text
        g'
   X ←──── X'
   |       |
 f |  ↘ h  | f'
   ↓       ↓
   Y ←──── Y'
        g
```

and the morphism `f'` is projective `(II, 5.5.5, (iii))`; set `h = f ∘ g' = g ∘ f'`.

(i) Let `ℳ̃` be the `𝒪_{X'}`-module associated to the quasi-coherent `𝒮'`-module `ℳ`, when `X'` is considered as an
affine `X`-scheme `(II, 1.4.3)`, so that one has `ℳ = g'_*(ℳ̃)`; as `ℳ` is an `𝒮'`-module of finite type, `ℳ̃` is an
`𝒪_{X'}`-module of finite type `(II, 1.4.5)`; as `h` is of finite type, since `g` and `f'` are
`(II, 1.3.7 and I, 6.3.4, (ii))`, `X'` is Noetherian `(I, 6.3.7)` and `ℳ̃` is consequently coherent. This being so, as
`g'` is affine, the canonical homomorphism `R^p f_*(ℳ) → R^p h_*(ℳ̃)` is bijective `(1.3.4)`. In addition, this
homomorphism is a homomorphism of `𝒮`-modules; indeed, from the canonical homomorphism

```text
  g^*(𝒮) ⊗_{𝒪_{X'}} g'^*(ℳ) → g'^*(ℳ)                                       (2.4.1.2)
```

which defines the `𝒮'`-module structure of `ℳ` (recalling that `𝒮' = g'^*(𝒪_{X'})`), one canonically deduces a
homomorphism

```text
  f_*(g^*(𝒮)) ⊗ R^p f_*(g'^*(ℳ)) → R^p f_*(g'^*(ℳ))
```

<!-- original page 108 -->

`(0, 12.2.2)`, and since `(2.4.1.2)` itself comes (by application of `(0_I, 4.2.2.1)`) from the homomorphism
`𝒪_{X'} ⊗ ℳ̃ → ℳ̃` defining the `𝒪_{X'}`-module structure of `ℳ̃`, the diagram

```text
  f_*(g'_*(𝒪_{X'})) ⊗ R^p f_*(g'_*(ℳ̃))    →    R^p f_*(g'_*(ℳ̃))

           ↓                                            ↓

  h_*(𝒪_{X'}) ⊗ R^p h_*(ℳ̃)                →    R^p h_*(ℳ̃)
```

is commutative `(0, 12.2.6)`; composing the horizontal arrows with the homomorphism coming from the canonical
homomorphism `𝒮 → f_*(f^*(𝒮)) = f_*(𝒮') = f_*(g'_*(𝒪_{X'})) = h_*(𝒪_{X'})`, one obtains our assertion. On the other
hand, since `g` is affine and `f'` is separated and quasi-compact, the canonical homomorphism
`R^p h_*(ℳ̃) → g_*(R^p f'_*(ℳ̃))` is bijective `(1.4.14)`, and one shows as above that it is an isomorphism of
`𝒮`-modules (this time using the commutativity of `(0, 12.2.6.2)`). Now, since `f'` is projective and `ℳ̃` is coherent,
`R^p f'_*(ℳ̃)` is a coherent `𝒪_{Y'}`-module by virtue of `(2.2.1)`; one concludes that `g_*(R^p f'_*(ℳ̃))` is an
`𝒮`-module of finite type `(II, 1.4.5)`.

(ii) Let `ℒ' = g'^*(ℒ)`, which is an invertible `𝒪_{X'}`-module; for every `n ∈ ℤ`, one has
`g'_*(ℳ̃ ⊗ ℒ'^{⊗n}) = g'_*(ℳ̃) ⊗ ℒ^{⊗n} = ℳ(n)` `(0_I, 5.4.10)` up to an isomorphism; one may apply to `ℳ̃ ⊗ ℒ'^{⊗n}`
the reasoning made in (i) for `ℳ̃`, which proves that `R^p f_*(ℳ(n))` is isomorphic to `g_*(R^p f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))`.
Now `ℒ'` is ample for `f'` `(II, 4.6.13, (iii))`, so it follows from `(2.2.1)` that there exists an integer `N` such
that `R^p f'_*(ℳ̃ ⊗ ℒ'^{⊗n}) = 0` for every `p` and every `n ≥ N`, which proves `(2.4.1.1)`. Finally, it follows again
from `(2.2.1)` that one may suppose `N` chosen so that for `n ≥ N`, the canonical homomorphism
`f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n})) → ℳ̃ ⊗ ℒ'^{⊗n}` is surjective; as `g'_*` is an exact functor `(II, 1.4.4)`, the corresponding
homomorphism

```text
  g'_*(f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) → g'_*(ℳ̃ ⊗ ℒ'^{⊗n}) = ℳ(n)
```

is surjective. Now, one has `g'_*(f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) = f^*(g_*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n})))` `(II, 1.5.2)` and since
`g ∘ f' = f ∘ g'`, one finally sees that one has

```text
  g'_*(f'^*(f'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) = f^*(f_*(g'_*(ℳ̃ ⊗ ℒ'^{⊗n}))) = f^*(f_*(ℳ(n))),
```

which completes the proof.

**2.4.2.**

<!-- label: III.2.4.2 -->

We shall in particular have to apply `(2.4.1)` when `𝒮` is an `𝒪_Y`-graded algebra with positive degrees,
`ℳ = ⊕_{k ∈ ℤ} ℳ_k` an `𝒮'`-graded module. Then (with the

<!-- original page 109 -->

same hypotheses of finiteness on `𝒮` and `ℳ`) one concludes from `(2.4.1)` that `⊕_{k ∈ ℤ} R^p f_*(ℳ_k)` is an
`𝒮`-module of finite type for every `p`, and (under the additional hypotheses of `(2.4.1, (ii))`) that there exists `N`
such that for `n ≥ N`, one has `R^p f_*(ℳ_k(n)) = 0` for every `p > 0` and every `k ∈ ℤ`, and that the canonical
homomorphism `f^*(f_*(ℳ_k(n))) → ℳ_k(n)` is surjective for every `k ∈ ℤ`.

## 2.5. Euler–Poincaré characteristic and the Hilbert polynomial

**2.5.1.**

<!-- label: III.2.5.1 -->

Let `A` be an Artinian ring, `X` an `A`-scheme projective over `Y = Spec(A)`. For every coherent `𝒪_X`-module `ℱ`, the
`H^i(X, ℱ)` (`i ≥ 0`) are `A`-modules of finite type `(2.2.1)`, hence here of *finite length* since `A` is Artinian. One
knows in addition `(2.2.1)` that `H^i(X, ℱ) = 0` except for a finite number of values of `i ≥ 0`; the integer

```text
  χ_A(ℱ) = Σ_{i=0}^∞ (−1)^i long(H^i(X, ℱ))                                  (2.5.1.1)
```

is thus defined for every coherent `𝒪_X`-module `ℱ`. When `A` is an Artinian *local* ring, one says that `χ_A(ℱ)` is the
*Euler–Poincaré characteristic of `ℱ`* (with respect to the ring `A`). For `ℱ = 𝒪_X`, one says that `χ_A(𝒪_X)` is the
*arithmetic genus* of `X` (with respect to `A`).

**Proposition (2.5.2).**

<!-- label: III.2.5.2 -->

*Let `0 → ℱ' → ℱ → ℱ'' → 0` be an exact sequence of coherent `𝒪_X`-modules; one then has*

```text
  χ_A(ℱ) = χ_A(ℱ') + χ_A(ℱ'').                                               (2.5.2.1)
```

**Proof.** As the cohomology modules of `ℱ'`, `ℱ`, `ℱ''` are zero except for a finite number of them, there is an
integer `r > 0` such that the exact cohomology sequence is written

```text
  0 → H^0(X, ℱ') → H^0(X, ℱ) → H^0(X, ℱ'') → H^1(X, ℱ') → ⋯
       ⋯ → H^r(X, ℱ') → H^r(X, ℱ) → H^r(X, ℱ'') → 0.
```

Now, we know that in an exact sequence of `A`-modules of finite length, with `0` at both ends, the alternating sum of
the lengths is zero `(0, 11.10.1)`; applying this result, one immediately finds the formula `(2.5.2.1)`.

One notes that the result of `(2.5.2)` applies whenever one knows that `X` is a quasi-compact `A`-scheme and that the
`A`-modules `H^i(X, ℱ)` are of finite type for every coherent `𝒪_X`-module `ℱ` `(1.4.12)`.

**Theorem (2.5.3).**

<!-- label: III.2.5.3 -->

*Let `A` be an Artinian local ring, `X` a scheme projective over `Y = Spec(A)`, `ℒ` an invertible `𝒪_X`-module very
ample relative to `Y`, `ℱ` a coherent `𝒪_X`-module; set `ℱ(n) = ℱ ⊗_{𝒪_X} ℒ^{⊗n}` for every `n ∈ ℤ`.*

*(i) There exists a unique polynomial `P ∈ ℚ[T]` such that `χ_A(ℱ(n)) = P(n)` for every `n ∈ ℤ` (one says that `P` is
the *Hilbert polynomial of `ℱ` with respect to `A`*).*

*(ii) For `n` large enough, one has `χ_A(ℱ(n)) = long_A Γ(X, ℱ(n))`.*

*(iii) The leading coefficient of `χ_A(ℱ(n))` is `≥ 0`.*

Let us add that in Chap. IV, in the paragraph devoted to the notion of dimension, we shall in addition show that *the
degree of `χ_A(ℱ(n))` is equal to the dimension of the support of `ℱ`*.

**Proof.** As one has `H^i(X, ℱ(n)) = 0` for every `i > 0` as soon as `n` is large enough `(2.2.1)`,

<!-- original page 110 -->

one has `χ_A(ℱ(n)) = long H^0(X, ℱ(n)) = long Γ(X, ℱ(n))` for `n` large enough, whence (ii); this implies
`χ_A(ℱ(n)) ≥ 0` for `n` large enough, and (iii) thus follows from (i); as moreover the assertion of uniqueness in (i) is
immediate, it remains to prove the existence of the polynomial `P`.

Let us first show that one may suppose `𝔪 ℱ = 0`, where `𝔪` is the maximal ideal of `A`. Indeed, there exists an integer
`s > 0` such that `𝔪^s = 0`, and `ℱ(n)` thus admits a finite filtration

```text
  ℱ(n) ⊃ 𝔪 ℱ(n) ⊃ ⋯ ⊃ 𝔪^{s−1} ℱ(n) ⊃ 0.
```

By induction, one deduces from `(2.5.2.1)` that

```text
  χ_A(ℱ(n)) = Σ_{k=1}^s χ_A(𝔪^{k−1} ℱ(n) / 𝔪^k ℱ(n));
```

since `𝔪^{k−1} ℱ(n) / 𝔪^k ℱ(n) = ℱ'_k(n)`, where `ℱ'_k = 𝔪^{k−1} ℱ / 𝔪^k ℱ`, this proves our assertion.

So suppose `𝔪 ℱ = 0`; if `X'` is the closed subscheme of `X`, inverse image by the structure morphism `X → Spec(A)` of
the unique closed point of `Spec(A)`, and `j : X' → X` the canonical injection, one has `ℱ = j_*(ℱ')`, where `ℱ'` is a
coherent `𝒪_{X'}`-module; `X'` is a scheme projective over `Spec(K)`, where `K = A/𝔪`. If `ℒ' = j^*(ℒ)`, `ℒ'` is very
ample relative to `Spec(K)` `(II, 4.4.10)`, and one has `ℱ(n) = j_*(ℱ'(n))`, where `ℱ'(n) = ℱ' ⊗_{𝒪_{X'}} ℒ'^{⊗n}`
`(0_I, 5.4.10)`. One concludes that `χ_A(ℱ(n)) = χ_K(ℱ'(n))` `(G, II, 4.9.1)`, and one is thus reduced to the case where
`A` is a *field*.

Note now that `X` can be considered as a closed subscheme of `P = ℙ^r_A` for a suitable `r` `(II, 5.5.4, (ii))`; if
`i : X → P` is the canonical injection, one sees as above that one has `χ_A(ℱ(n)) = χ_A(i_*(ℱ)(n))`, so that one may
restrict to the case where `X = ℙ^r_A = Proj(S)` with `S = A[T_0, …, T_r]`, `A` being a field.

This being so, one has `ℱ = M̃`, where `M` is a graded `S`-module of finite type `(II, 2.7.8)`; there exists
consequently a finite resolution of `M` by graded free `S`-modules of finite type

```text
  0 → L_q → L_{q−1} → ⋯ → L_1 → M → 0
```

by virtue of Hilbert's syzygy theorem `(M, VIII, 6.5)`; as `M ↦ M̃` is an exact functor in `M` `(II, 2.5.4)`, one also
has an exact sequence

```text
  0 → L̃_q → L̃_{q−1} → ⋯ → L̃_1 → M̃ → 0
```

and consequently, for every `n ∈ ℤ`, the sequence

```text
  0 → L̃_q(n) → L̃_{q−1}(n) → ⋯ → L̃_1(n) → M̃(n) → 0
```

is exact; applying by induction on `q` Proposition `(2.5.1)`, it comes

```text
  χ_A(M̃(n)) = Σ_{i=1}^q (−1)^{i+1} χ_A(L̃_i(n))
```

and to prove (i), one is therefore reduced to the case where `M` is free and graded of finite type, hence to the case
where `M = S(h)` for an `h ∈ ℤ`. As we then have `M̃(n) = (M(n))∼ = (S(n + h))∼` `(II, 2.5.15)`, one finally sees that
the theorem will follow from the following.

<!-- original page 111 -->

**Lemma (2.5.3.1).**

<!-- label: III.2.5.3.1 -->

*Let `A` be a field, `r` an integer `> 0`, and `X = ℙ^r_A`; one then has `χ_A(𝒪_X(n)) = (n+r choose r)` for every
`n ∈ ℤ`.*

**Proof.** Indeed, for `n ≥ 0`, one has `χ_A(𝒪_X(n)) = long H^0(X, 𝒪_X(n))`, which is the number of monomials in the
`T_i` of total degree `n`, that is, `(n+r choose r)` `(2.1.12)`. For `n ≤ −r − 1`, one has similarly
`χ_A(𝒪_X(n)) = (−1)^r long H^r(X, 𝒪_X(n))`; if `n = −r − h`, the dimension of `H^r(X, 𝒪_X(n))` over `A` is the number of
sequences `(p_i)_{0 ≤ i ≤ r}` of integers `p_i > 0` such that `Σ_{i=0}^r p_i = r + h` `(2.1.12)`, or equivalently the
number of sequences of integers `q_i ≥ 0` (`0 ≤ i ≤ r`) such that `Σ_{i=0}^r q_i = h − 1`; this is therefore the number
`(h−1+r choose r) = (−1)^r (n+r choose r)`. Finally, for `−r ≤ n ≤ 0`, one has `(n+r choose r) = 0` and on the other
hand `H^i(X, 𝒪_X(n)) = 0` for every `i ≥ 0` `(2.1.12)`, which proves the lemma.

**Corollary (2.5.4).**

<!-- label: III.2.5.4 -->

*Let `A` be an Artinian local ring, `S` a graded `A`-algebra of finite type generated by `S_1`, `M` a graded `S`-module
of finite type, `X = Proj(S)`. One then has `χ_A(M̃(n)) = long M_n` for `n` large enough.*

**Proof.** This follows from the fact that `M_n` and `Γ(X, M̃(n))` are isomorphic for `n` large enough `(2.3.1)`.

## 2.6. Application: ampleness criteria

**Proposition (2.6.1).**

<!-- label: III.2.6.1 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a proper morphism, `ℒ` an invertible `𝒪_X`-module. The following
conditions are equivalent:*

*a) `ℒ` is ample for `f`.*

*b) For every coherent `𝒪_X`-module `ℱ`, there exists an integer `N` such that for `n ≥ N`, one has
`R^q f_*(ℱ ⊗ ℒ^{⊗n}) = 0` for every `q > 0`.*

*c) For every coherent ideal sheaf `𝒥` of `𝒪_X`, there exists an integer `N` such that for `n ≥ N` one has
`R^1 f_*(𝒥 ⊗ ℒ^{⊗n}) = 0`.*

**Proof.** We have seen that a) entails b) `(2.2.1, (ii))`. It is trivial that b) entails c), and it remains to prove
that c) implies a). One may restrict to the case where `Y` is affine `(II, 4.6.4)`, and prove in this case that `ℒ` is
ample; it will suffice to show that as `h` runs over the set of sections of the `ℒ^{⊗n}` (`n > 0`) over `X`, those of
the `X_h` which are affine form a cover of `X` `(II, 4.5.2)`. For this, let us show that for every closed point `x` of
`X` and every affine open neighbourhood `U` of `x`, there exist an `n` and an `h ∈ Γ(X, ℒ^{⊗n})` such that
`x ∈ X_h ⊂ U`; `X_h` will necessarily be affine `(I, 1.3.6)` and the union of these `X_h` will be an open set of `X`
containing all the closed points of `X`, and consequently `X` itself, since `X` is Noetherian
`(I, 6.3.7 and 0_I, 2.1.3)`. Let `𝒥` (resp. `𝒥'`) be the quasi-coherent ideal sheaf of `𝒪_X` defining the closed reduced
subprescheme of `X` having for underlying space `X − U` (resp. `(X − U) ∪ {x}`) `(I, 5.2.1)`; it is clear that `𝒥` and
`𝒥'` are coherent `(I, 6.1.1)`, that `𝒥' ⊂ 𝒥`, and that `𝒥'' = 𝒥 / 𝒥'` is a coherent `𝒪_X`-module `(0_I, 5.3.3)` with
support `{x}` and such that `𝒥''_x = κ(x)`. As `ℒ` is locally free, the sequence
`0 → 𝒥' ⊗ ℒ^{⊗n} → 𝒥 ⊗ ℒ^{⊗n} → 𝒥'' ⊗ ℒ^{⊗n} → 0` is exact for every `n`, and by hypothesis there exists `n` large
enough such that `H^1(X, 𝒥' ⊗ ℒ^{⊗n}) = 0`; the exact cohomology sequence

<!-- original page 112 -->

therefore proves that the homomorphism `Γ(X, 𝒥 ⊗ ℒ^{⊗n}) → Γ(X, 𝒥'' ⊗ ℒ^{⊗n})` is surjective. A section `g` of
`𝒥'' ⊗ ℒ^{⊗n}` over `X` such that `g(x) ≠ 0` is therefore the image of a section `h ∈ Γ(X, 𝒥 ⊗ ℒ^{⊗n}) ⊂ Γ(X, ℒ^{⊗n})`
(since by virtue of `(0_I, 5.4.1)`, `𝒥 ⊗ ℒ^{⊗n}` is a sub-`𝒪_X`-module of `ℒ^{⊗n}`); one has by definition `h(x) ≠ 0`
and `h(z) = 0` for `z ∉ U`, which completes the proof.

**Proposition (2.6.2).**

<!-- label: III.2.6.2 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a morphism of finite type, `g : X' → X` a finite surjective morphism,
`ℒ` an invertible `𝒪_X`-module and `ℒ' = g^*(ℒ)`. Suppose the following condition is satisfied: there exists a subset
`Z` of `X`, proper over `Y` `(II, 5.4.10)`, such that for every `x ∈ X − Z`, either `X` is normal at the point `x`, or
`(g_*(𝒪_{X'}))_x` is a free `𝒪_x`-module. Under these conditions, for `ℒ` to be ample for `f`, it is necessary and
sufficient that `ℒ'` be ample for `f ∘ g`.*

**Proof.**

**(2.6.2.1)**

<!-- label: III.2.6.2.1 -->

Since `g` is affine, the condition is necessary `(II, 5.1.12)`. To see that it is sufficient, one may suppose `Y` affine
`(II, 4.6.4)`. Let us further show that one may restrict to the case where `X` is reduced. Indeed, let `j : X_red → X`
be the canonical injection, and set `X_1 = X_red`, `X'_1 = X' ×_X X_1`, so that one has the commutative diagram

```text
         j'
    X' ←───── X'_1
    |          |
  g |          | g_1
    ↓          ↓
    X  ←───── X_1
         j

                                                                              (2.6.2.2)
```

The morphism `f ∘ j` is then of finite type `(I, 6.3.4)` and `g_1` is a finite morphism `(II, 6.1.5, (iii))`; if `ℒ'` is
ample for `f ∘ g`, `j'^*(ℒ')` is ample for `f ∘ g ∘ j'` since `j'` is a closed immersion `(II, 5.1.12 and I, 4.3.2)`. If
one sets `Z_1 = j^{−1}(Z)`, `Z_1` is proper over `Y` `(II, 5.4.10)`; on the other hand, if `X` is normal at a point `x`,
the same is evidently true of `X_red`; finally, if `(g_*(𝒪_{X'}))_x` is a free `𝒪_x`-module, it follows at once from
`(II, 1.5.2)` that `((g_1)_*(𝒪_{X'_1}))_x` is a free `𝒪_{X_1, x}`-module. Finally, since `X` is Noetherian `(I, 6.3.7)`,
if `j^*(ℒ)` is ample, `ℒ` is ample `(II, 4.5.14)`, and as `j'^*(ℒ') = g_1^*(j^*(ℒ))`, this completes the reduction
announced. We therefore suppose henceforth `Y` affine and `X` reduced.

The hypotheses of `(II, 6.6.11)` then being verified, there exists a reduced `Y`-prescheme `X_2` and a `Y`-morphism
`h : X_2 → X` finite and birational such that the restriction of `h` to `h^{−1}(X − Z)` is an isomorphism onto `X − Z`
and that `h^*(ℒ)` is ample. Replacing `X'` by `X_2`, one sees that one is reduced to proving the proposition supposing
in addition that `g` has the properties just enumerated for `h`. We shall again denote by `Z` a sub-prescheme of `X`
having `Z` for underlying space, which is proper over `Y` `(II, 5.4.10)`.

**(2.6.2.3)**

<!-- label: III.2.6.2.3 -->

Let now `X_1` be a closed sub-prescheme of `X`, `j : X_1 → X` the canonical injection, `X'_1 = g^{−1}(X_1) = X' ×_X X_1`
its inverse image, `j' : X'_1 → X'` the canonical injection, so that one has the commutative diagram `(2.6.2.2)`; set
`ℒ_1 = j^*(ℒ)`, `ℒ'_1 = j'^*(ℒ') = g_1^*(ℒ_1)`, so that `ℒ'_1` is ample for `f ∘ g ∘ j'` `(II, 5.1.12)`. If one sets
`Z_1 = j^{−1}(Z)`, the closed sub-prescheme `Z_1` of `X_1` is proper over `Y` `(II, 5.4.2, (ii))`. In other words, the
hypotheses of `(2.6.2)` are verified for `X_1`, `ℒ_1`, `g_1`, and `Z_1`.

<!-- original page 113 -->

This will allow us to prove `(2.6.2)` by Noetherian induction `(0_I, 2.2.2)` in the case where the restriction of `g` to
`g^{−1}(X − Z)` is an isomorphism onto `X − Z` (which is sufficient for our purpose, as one has seen in `(2.6.2.2)`): it
will suffice to establish that if, for every closed sub-prescheme `X_1` of `X` whose underlying space is `≠ X`, the
conclusion of `(2.6.2)` is true for the sheaf `ℒ_1`, then it is also true for the sheaf `ℒ`.

**(2.6.2.4)**

<!-- label: III.2.6.2.4 -->

Let then `𝒜 = 𝒪_X`, `ℬ = g_*(𝒪_{X'})`, so that `ℬ` is a sub-`𝒜`-algebra of `ℛ(X)`, which is a coherent `𝒜`-module; in
addition, the restriction `ℬ ∣ (X − Z)` is equal to `𝒜 ∣ (X − Z)`. Let `𝒦` be the *conductor* of `ℬ` over `𝒜`, that is,
the largest sub-`𝒜`-module quasi-coherent of `𝒜` such that `ℬ · 𝒦 ⊂ 𝒜` (or equivalently the *annihilator* of the
`𝒜`-module `ℬ / 𝒜` `(0_I, 5.3.7)`), which entails `ℬ · 𝒦 = 𝒦`. It is clear that `ℬ_z = 𝒜_z` at every point admitting a
neighbourhood `W_z` such that `g` is an isomorphism of `g^{−1}(W_z)` onto `W_z`, and in particular at every point of
`X − Z` and in a neighbourhood of every generic point of an irreducible component of `X`. Consider then the closed
sub-prescheme `Z_1 = Spec(𝒜 / 𝒦)` of `X` defined by `𝒦`; it is still proper over `Y`, since the sub-space `Z_1` is
closed in `Z` `(II, 5.4.10)`. Moreover, the definition of `𝒦` shows that `ℬ ∣ (X − Z_1) = 𝒜 ∣ (X − Z_1)`; one thus sees
that one can always reduce to the case where `Z = Spec(𝒜 / 𝒦)`, and as we have seen that `X − Z_1` is a nonempty open
set of `X`, one may always suppose that the space `Z` is distinct from `X`.

**(2.6.2.5)**

<!-- label: III.2.6.2.5 -->

Consider `X'` as equal to `Spec(ℬ)` (since `g` is affine) and let `𝒦' = 𝒦̃`, a coherent ideal sheaf of `𝒪_{X'}` such
that `g_*(𝒦') = 𝒦` `(II, 1.4.1)`; the closed sub-prescheme `Z' = g^{−1}(Z) = Z ×_X X'` of `X'` is defined by `𝒦'` and
equal to `Spec(ℬ/𝒦)` `(II, 1.4.10)`; as `h : Z' → Z` is a finite morphism `(II, 6.1.5, (iii))`, `Z'` is proper over `Y`
`(II, 6.1.11 and 5.4.2, (ii))`.

This being so, we must prove that for every `x ∈ X` and every open neighbourhood `U` of `x`, there exists a section `s`
of an `ℒ^{⊗n}` (`n > 0`) over `X` such that `x ∈ X_s ⊂ U` `(II, 4.5.2)`; we distinguish two cases:

1° One has `x ∈ X − Z`; one may evidently then suppose that one also has `U ⊂ X − Z`, so the open set `U' = g^{−1}(U)`
does not meet `Z'`. As `ℒ'` is ample by hypothesis, there exist an `n > 0` and a section `s'` of `ℒ'^{⊗n}` over `X'`
such that `x' = g^{−1}(x) ∈ X'_{s'} ⊂ g^{−1}(U)` `(II, 4.5.2)`. In addition, one may suppose that `𝒦' ⊗ ℒ'^{⊗n}` is
generated by its sections over `X'` `(II, 4.5.5)`, so, since `𝒦'_{x'} = 𝒪_{x'}`, there is a section `s''` of these such
that `s''(x') ≠ 0`; multiplying it by `s'` (which amounts to replacing `n` by `2n`), one sees that one may also suppose
that `x' ∈ X'_{s''} ⊂ g^{−1}(U)`. This being so, it follows from `(0_I, 5.4.10)` that one has a canonical isomorphism

```text
  Γ(X, 𝒦 ⊗ ℒ^{⊗n}) ⥲ Γ(X', 𝒦' ⊗ ℒ'^{⊗n}).
```

The section `s` of `𝒦 ⊗ ℒ^{⊗n}` corresponding to `s''` under this isomorphism evidently has the desired properties.

2° One has `x ∈ Z`. Let `𝒥` be the coherent ideal sheaf of `𝒪_X` defining the closed reduced sub-prescheme of `X` having
for underlying space `X − U`, and consider in `ℬ` the coherent ideals

<!-- original page 114 -->

`𝒥 ℬ` and `𝒥_1 = 𝒥 ∣ (𝒥 ℬ ∩ 𝒜) = 𝒥(𝒥 ℬ)`, so that one has the diagram of inclusions

```text
   𝒥 ℬ    →    ℬ
   ↑           ↑
   𝒥     →    𝒜
   ↑           ↑
   𝒥 𝒦 ℬ = 𝒥 𝒦  →   𝒦                                                       (2.6.2.6)
```

Let `𝒥'` be the coherent ideal sheaf `(𝒥 ℬ)∼` of `𝒪_{X'}`, so that `𝒥 ℬ = g_*(𝒥')`, `𝒥 𝒦 = (𝒥 𝒦')∼`, and consequently
`𝒥' / 𝒥' 𝒦' = (𝒥 ℬ / 𝒥 𝒦 ℬ)∼` `(II, 1.4.4)`. As `𝒥 ∣ V = 𝒥 𝒦 ∣ V` for every open set `V` not meeting `Z`, one sees that
the support of `𝒥' / 𝒥' 𝒦'` is contained in `Z'`. As `Z'` is proper over `Y`, one may apply `(2.2.4)` and one sees that
for `n` large enough, the canonical map

```text
  Γ(X', 𝒥' ⊗ ℒ'^{⊗n}) → Γ(X', (𝒥' / 𝒥' 𝒦') ⊗ ℒ'^{⊗n})
```

is surjective.

But by virtue of `(0_I, 5.4.10)`, one concludes that the canonical map

```text
  Γ(X, 𝒥 ℬ ⊗ ℒ^{⊗n}) → Γ(X, (𝒥 ℬ / 𝒥 𝒦 ℬ) ⊗ ℒ^{⊗n})
```

is surjective.

This being so, let `i : Z → X` be the canonical injection, `i' : Z' → X'` the canonical injection, so that one has the
commutative diagram

```text
         i'
    X' ←───── Z'
    |          |
  g |          | h
    ↓          ↓
    X  ←───── Z
         i
```

Let `ℳ = i^*(ℒ)`, `ℳ' = i'^*(ℒ')`; as `ℒ'` is ample, `ℳ'` is ample `(II, 5.1.12)`, and on the other hand `ℳ' = h^*(ℳ)`;
one concludes therefore from the hypothesis of Noetherian induction (since `Z ≠ X`) that `ℳ` is ample. Consequently
`i^*((𝒥 ℬ / 𝒥 𝒦) ⊗ ℒ^{⊗n})` is generated by its sections over `Z` for `n` large enough `(II, 4.5.5)`. As
`𝒥 ℬ / 𝒥 𝒦 = i_*(i^*(𝒥 ℬ / 𝒥 𝒦))`, one deduces again from `(0_I, 5.4.10)` that there exists a section `s` of
`(𝒥 ℬ / 𝒥 𝒦) ⊗ ℒ^{⊗n}` over `X` (for `n` large enough) such that `s(x) ≠ 0`, since one has `ℬ_x = 𝒜_x` by definition of
`Z` and `𝒦_x ≠ 𝒜_x` by hypothesis. The diagram `(2.6.2.6)` shows that `s` is also a section of `(𝒥 ℬ / 𝒥 𝒦 ℬ) ⊗ ℒ^{⊗n}`
over `X`, hence `s` is the canonical image of a section `t` of `𝒥 ℬ ⊗ ℒ^{⊗n}` over `X`. But by definition, the canonical
image `s` of `t` mod `(𝒥 𝒦 ℬ) ⊗ ℒ^{⊗n}` is in `(𝒥 ⊗ ℒ^{⊗n}) / ((𝒥 𝒦 ℬ) ⊗ ℒ^{⊗n})`, hence by virtue of `(2.6.2.6)`, this
implies that `t` is a *section of `𝒥 ⊗ ℒ^{⊗n}`* over `X`, and *a fortiori* a section of `ℒ^{⊗n}`. One has seen above
that `t(x) ≠ 0`, so `x ∈ X_t`, and by definition of `𝒥`, `t(y) = 0` in `X − U` which is the support of `𝒪_X / 𝒥`; thus
`X_t ⊂ U`, which completes the proof.

**Remark (2.6.3).**

<!-- label: III.2.6.3 -->

When `X` is proper over `Y`, one can prove `(2.6.2)` more simply, by reasoning as in Chevalley's theorem `(II, 6.7.1)`,
using `(2.6.1)` and Lemma `(II, 6.7.1.1)`.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iii/08-c3-s02-etude-cohomologique-morphismes-projectifs.md;
     PDF: ~/Code/pdfs/ega/EGA-III-1.pdf, pp. 95–113 -->
