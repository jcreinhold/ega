# Chapter 0_III

## §13. Projective limits in homological algebra

<!-- original page 64 -->

### 13.1. The Mittag–Leffler condition

**13.1.1.**

<!-- label: 0_III.13.1.1 -->

Let `𝒞` be an abelian category in which infinite products exist (axiom **AB 3\*** of `(T, 1.5)`); then the infimum of a
family of subobjects of an object of `𝒞` exists, and every projective system of objects of `𝒞` admits a projective
limit, which is a left-exact functor of the projective system considered `(T, 1.8)`. Let

<!-- original page 65 -->

`(A_α, f_{αβ})` be a projective system of objects of `𝒞` whose index set `I` is right-filtered; set `A = lim_← A_α` and,
for every `α ∈ I`, let `f_α : A → A_α` be the canonical morphism. For every `α ∈ I`, the `f_{αβ}(A_β)` for `β ≥ α` form
a filtered decreasing family of subobjects of `A_α`; the subobject

```text
  A'_α = inf_{β ≥ α} f_{αβ}(A_β)
```

is called the subobject of "universal images" in `A_α`; it is clear that `f_α(A) ⊂ A'_α` and `f_{αβ}(A'_β) ⊂ A'_α` for
`α ≤ β`, so `(A'_α, f_{αβ}|A'_β)` is a projective system, and `A = lim_← A'_α`.

**13.1.2.**

<!-- label: 0_III.13.1.2 -->

Given a projective system `(A_α, f_{αβ})` in `𝒞`, the *Mittag–Leffler condition* is the following condition:

> `(ML)` For every index `α`, there exists `β ≥ α` such that, for every `γ ≥ β`, one has `f_{αγ}(A_γ) = f_{αβ}(A_β)`.

It is clear that if the `f_{αβ}` are epimorphisms, condition `(ML)` is satisfied. Conversely, if `(ML)` is satisfied,
and if for every `α ∈ I`, `A'_α` is the subobject of "universal images" in `A_α`, the restriction of `f_{αβ}` to `A'_β`
is an epimorphism `A'_β → A'_α` for `α ≤ β`: indeed, if `γ ≥ β` is such that `f_{βδ}(A_δ) = f_{βγ}(A_γ)` for `δ ≥ γ`,
one has `A'_β = f_{βγ}(A_γ)`, and this entails on the other hand `f_{αδ}(A_δ) = f_{αγ}(A_γ)` for `δ ≥ γ`, so
`A'_α = f_{αγ}(A_γ) = f_{αβ}(A'_β)`.

Note also that condition `(ML)` is satisfied whenever the objects `A_α` are *artinian* in `𝒞`, that is, every family of
subobjects of `A_α` admits a minimal element: a minimal element of the filtered decreasing family `(f_{αβ}(A_β))` of
subobjects of `A_α` is then necessarily the smallest of these subobjects.

> _Translator's note._ Throughout §13, EGA's `(ML)` denotes the Mittag–Leffler condition; we keep the EGA abbreviation.
> Modern accounts often write "ML condition" or "satisfies ML" interchangeably.

**Remark (13.1.3).**

<!-- label: 0_III.13.1.3 -->

Condition `(ML)` can also be formulated when `𝒞` is, for example, the category of sets; one can then again define the
subset of "universal images" in `A_α`, and the remarks made on this subject in `(13.1.1)` and `(13.1.2)` remain valid.

### 13.2. The Mittag–Leffler condition for abelian groups

**Proposition (13.2.1).**

<!-- label: 0_III.13.2.1 -->

Let

```text
  0 → A_α --u_α--> B_α --v_α--> C_α → 0
```

be an exact sequence of projective systems of abelian groups (relative to the same right-filtered index set `I`).

- _(i)_ If `(B_α)` satisfies `(ML)`, so does `(C_α)`.
- _(ii)_ If `(A_α)` and `(C_α)` satisfy `(ML)`, so does `(B_α)`.

Let `(f_{αβ})`, `(g_{αβ})`, `(h_{αβ})` be the systems of homomorphisms defining the projective systems `(A_α)`, `(B_α)`,
`(C_α)` respectively.

_(i)_ Suppose `g_{αβ}(B_β) = g_{αλ}(B_λ)` for `λ ≥ β`; since `v_β` and `v_λ` are surjective, one has
`h_{αβ}(C_β) = v_α(g_{αβ}(B_β)) = v_α(g_{αλ}(B_λ)) = h_{αλ}(C_λ)` for `λ ≥ β`.

_(ii)_ Let `α ∈ I`, and let `β ≥ α` be an index such that for `λ ≥ β`, one has `f_{αβ}(A_β) = f_{αλ}(A_λ)`; let also
`γ ≥ β` be an index such that, for `λ ≥ γ`, one has `h_{βλ}(C_λ) = h_{βγ}(C_γ)`. Let then `x_α` be an element of
`g_{αγ}(B_γ)`; one has `x_α = g_{αγ}(y_γ)` with `y_γ ∈ B_γ`; set `y_β = g_{βγ}(y_γ)`, so that
`x_α = g_{αβ}(g_{βγ}(y_γ))`. For every `λ ≥ γ`, there exists by hypothesis `y_λ ∈ B_λ` such that
`h_{βγ}(v_γ(y_γ)) = h_{βλ}(v_λ(y_λ)) = v_β(g_{βλ}(y_λ))`, whence `v_β(y_β − g_{βλ}(y_λ)) = 0`, and consequently there
exists `x_β ∈ A_β`

<!-- original page 66 -->

such that `y_β = g_{βλ}(y_λ) + u_β(x_β)`. One deduces `x_α = g_{αλ}(y_λ) + u_α(f_{αβ}(x_β))`; but since `λ ≥ β`, there
exists `x_λ ∈ A_λ` such that `f_{αβ}(x_β) = f_{αλ}(x_λ)`, and finally `x_α = g_{αλ}(y_λ + u_λ(x_λ)) ∈ g_{αλ}(B_λ)`,
which completes the demonstration.

**Proposition (13.2.2).**

<!-- label: 0_III.13.2.2 -->

Let `I` be a right-filtered ordered set having a countable cofinal part. Let

```text
  0 → A_α --u_α--> B_α --v_α--> C_α → 0
```

be an exact sequence of projective systems of abelian groups having `I` as index set. If `(A_α)` satisfies condition
`(ML)`, the sequence

```text
  0 → lim_← A_α → lim_← B_α → lim_← C_α → 0
```

is exact.

It comes down to proving that the homomorphism `v = lim_← v_α : lim_← B_α → lim_← C_α` is surjective. Let `z = (z_α)` be
an element of `lim_← C_α`, and set `E_α = v_α^{−1}(z_α)`; it is clear that the `E_α` form a projective system of
non-empty sets for the restrictions of the homomorphisms `g_{αβ} : B_β → B_α`. Let us show that this projective system
satisfies condition `(ML)`; identifying `A_α` with a part of `B_α` via `u_α` for every `α ∈ I`, there exists `β ≥ α`
such that `g_{αβ}(A_β) = g_{αλ}(A_λ)` for `λ ≥ β`; let us show that one also has `g_{αβ}(E_β) = g_{αλ}(E_λ)` for
`λ ≥ β`. Indeed, take `y_λ ∈ E_λ` and set `y_β = g_{βλ}(y_λ)`, `y_α = g_{αλ}(y_λ)`; let `y'_α ∈ g_{αβ}(E_β)`, so that
`y'_α = g_{αβ}(y'_β)` for some `y'_β ∈ E_β`; one has `y'_β − y_β = x_β ∈ A_β`, and by hypothesis there exists
`x_λ ∈ A_λ` such that `g_{αβ}(x_β) = g_{αλ}(x_λ)`; therefore

```text
  y'_α = g_{αβ}(y_β) + g_{αβ}(x_β) = g_{αλ}(y_λ) + g_{αλ}(x_λ)
       = g_{αλ}(y_λ + x_λ) ∈ g_{αλ}(E_λ),
```

which proves our assertion. That being so, one knows (Bourbaki, _Top. gén._, ch. II, 3rd ed., §3, th. 1) that under the
hypotheses made on `I`, a projective system of non-empty sets satisfying `(ML)` has a non-empty projective limit; in
consequence, there exists a point `y = (y_α) ∈ lim_← E_α`, and since `v_α(y_α) = z_α` by definition for every `α`, one
has `z = v(y)`. Q.E.D.

**Proposition (13.2.3).**

<!-- label: 0_III.13.2.3 -->

The hypotheses on `I` being those of `(13.2.2)`, let `(K^•_α)_{α ∈ I}` be a projective system of complexes of abelian
groups `K^•_α = (K^n_α)_{n ∈ ℤ}` whose differential operator is of degree `+1`. For each `n`, there exists a canonical
functorial homomorphism

```text
  h_n : H^n(lim_← K^•_α) → lim_← H^n(K^•_α).                                  (13.2.3.1)
```

If, for every degree `n`, the projective system of abelian groups `(K^n_α)_{α ∈ I}` satisfies `(ML)`, then all the
homomorphisms `h_n` are surjective. If in addition, for some degree `n`, the projective system
`(H^{n−1}(K^•_α))_{α ∈ I}` satisfies `(ML)`, the homomorphism `h_n` is bijective.

Set, for every `n`, `K^n = lim_← K^n_α`; the definition of the homomorphisms `h_n` comes from the commutativity of the
diagrams

```text
  … → K^{n−1} ----> K^n ----> K^{n+1} → …
        ↓            ↓            ↓
  … → K^{n−1}_α → K^n_α → K^{n+1}_α → …
```

<!-- original page 67 -->

the differential operators in `K^•` being projective limits of the corresponding operators in the `K^•_α`.

Consider the exact sequences

```text
  (*_n)     0 → B^n(K^•_α) → Z^n(K^•_α) → H^n(K^•_α) → 0
  (**_n)    0 → Z^{n−1}(K^•_α) → K^{n−1}_α → B^n(K^•_α) → 0
```

The hypothesis and Proposition `(13.2.1, (i))` show that the projective system `(B^n(K^•_α))_{α ∈ I}` satisfies `(ML)`
for every `n`; it therefore results from `(13.2.2)` that the sequence

```text
  (***_n)   0 → lim_α B^n(K^•_α) → lim_α Z^n(K^•_α) → lim_α H^n(K^•_α) → 0
```

is exact. Now it is clear that `lim_← B^n(K^•_α)` identifies with a subgroup of `K^{n+1}` containing `B^n(K^•)`, and
that `lim_← Z^n(K^•_α)` identifies with a subgroup of `Z^n(K^•)`; in consequence, `h_n` is surjective. If now one
supposes furthermore that the projective system `(H^{n−1}(K^•_α))_{α ∈ I}` satisfies `(ML)`, the exact sequences
`(*_{n−1})` and Proposition `(13.2.1, (ii))` show that the projective system `(Z^{n−1}(K^•_α))_{α ∈ I}` satisfies
`(ML)`; but then, `(13.2.2)` applied to the exact sequences `(**_n)` shows that the sequence

```text
  0 → lim_α Z^{n−1}(K^•_α) → K^{n−1} --u--> lim_α B^n(K^•_α) → 0
```

is exact; since `lim_← B^n(K^•_α) ⊃ B^n(K^•)`, and the composite of the injection `lim_← B^n(K^•_α) → K^n` with `u` is
the differential operator `K^{n−1} → K^n`, the fact that `u` is surjective entails `lim_← B^n(K^•_α) = B^n(K^•)`, so
`h_n` is injective. Q.E.D.

**Remarks (13.2.4).**

<!-- label: 0_III.13.2.4 -->

_(i)_ The reasoning of `(13.2.2)` (cf. Bourbaki, _loc. cit._) shows that the conclusion of this proposition remains
valid when one supposes only that the `A_α` can be equipped with structures of *complete metrizable spaces*, in which
the translations are homeomorphisms, that the maps `f_{αβ} : A_β → A_α` defining the projective system `(A_α)` are
*uniformly continuous* for the distances considered, and finally that the system `(A_α)` satisfies the condition

> `(ML')` For every index `α`, there exists `β ≥ α` such that, for every `γ ≥ β`, `f_{αγ}(A_γ)` is dense in
> `f_{αβ}(A_β)`.

This allows one to add an analogous complement to `(13.2.3)`: suppose that `K^n_α = 0` for `n < 0` and for every `α`;
suppose moreover that `(K^n_α)_{α ∈ I}` satisfies `(ML)` for `n ≥ 0` and that the `A_α = H^0(K^•_α)` can be equipped
with structures of metric spaces satisfying the above properties. Then the conclusions of `(13.2.3)` are unchanged for
`n ≥ 2`, and in addition `h_1` is bijective, since the reasoning of `(13.2.2)` shows again that `(B^1(K^•_α))_{α ∈ I}`
satisfies `(ML)`, that the sequence `(***_1)` is exact, and finally, by virtue of the foregoing, that
`lim_← B^1(K^•_α) = B^1(K^•)`. We have thus established, among others, the assertions of `(T, 3.10.2)`.

_(ii)_ It is possible to introduce the right-derived functors `lim^{(i)}_←` of the functor `lim_←`, and to obtain more
complete statements than the preceding ones `[28]`.

<!-- original page 68 -->

### 13.3. Application: cohomology of a projective limit of sheaves

**Proposition (13.3.1).**

<!-- label: 0_III.13.3.1 -->

Let `X` be a topological space, `(ℱ_k)_{k ∈ ℕ}` a projective system of sheaves of abelian groups on `X`, and let
`ℱ = lim_← ℱ_k`. Suppose the following conditions are satisfied:

- _(i)_ There exists a base `𝔅` of the topology of `X` such that, for every `U ∈ 𝔅` and every `i ≥ 0`, the projective
    system `(H^i(U, ℱ_k))_{k ∈ ℕ}` satisfies `(ML)`.
- _(ii)_ For every `x ∈ X` and every `i > 0`, one has `lim_U (lim_← H^i(U, ℱ_k)) = 0` as `U` runs over the set of
    neighborhoods of `x` belonging to `𝔅`.
- _(iii)_ The homomorphisms `u_{hk} : ℱ_k → ℱ_h` (`h ≤ k`) defining the projective system `(ℱ_k)` are surjective.

Under these conditions, for every `i > 0`, the canonical homomorphism

```text
  h_i : H^i(X, ℱ) → lim_← H^i(X, ℱ_k)
```

is surjective; if in addition, for some value of `i`, the projective system `(H^{i−1}(X, ℱ_k))_{k ∈ ℕ}` satisfies
`(ML)`, `h_i` is bijective.

_a)_ We shall first suppose that the `ℱ_k` are *flasque* as well as the kernels `𝒩_{hk}` of the `u_{hk}`; we shall then
show that condition (iii) of the statement entails `H^i(X, ℱ) = 0` for `i > 0`. It will suffice to prove that for
*every* open `U` of `X` and every cover `𝔘` of `U` by open subsets of `U`, one has `H^i(𝔘, ℱ) = 0` for `i > 0`. It will
result, first, that for Čech cohomology, one has `Ȟ^i(U, ℱ) = 0` for every `i > 0`, then (by virtue of `(G, II, 5.9.2)`
applied to the set of all open subsets of `X`) that `H^i(X, ℱ) = 0` for every `i > 0`. Since the `ℱ_k` are flasque, one
has `H^i(𝔘, ℱ_k) = 0` for `i > 0` `(G, II, 5.2.3)`; consider for each `k` the complex `C^•(𝔘, ℱ_k)` of alternating
cochains of the nerve of the cover `𝔘` `(G, II, 5.1)`, which evidently forms a projective system of complexes of abelian
groups. Let us show that all the maps `C^•(𝔘, ℱ_k) → C^•(𝔘, ℱ_h)` (`h ≤ k`) are *surjective*. It clearly suffices, by
definition, to show that for every open `V` of `X`, the map `Γ(V, ℱ_k) → Γ(V, ℱ_h)` is surjective; but the sequence
`0 → 𝒩_{hk} → ℱ_k → ℱ_h → 0` being exact by hypothesis gives the exact cohomology sequence

```text
  Γ(V, ℱ_k) → Γ(V, ℱ_h) → H^1(V, 𝒩_{hk}) = 0
```

since `𝒩_{hk}` is flasque. The projective system `(C^•(𝔘, ℱ_k))_{k ∈ ℕ}` therefore satisfies `(ML)`; the same holds for
`(H^i(𝔘, ℱ_k))_{k ∈ ℕ}` for every `i ≥ 0`, since this is trivial for `i > 0`, and since `H^0(𝔘, ℱ_k) = Γ(U, ℱ_k)`
`(G, II, 5.2.2)`, condition `(ML)` is also met for `i = 0` by what precedes. One can therefore apply `(13.2.3)`, which
shows that `H^i(𝔘, ℱ) = lim_← H^i(𝔘, ℱ_k) = 0` for every `i > 0`.

_b)_ Let us pass to the general case, and consider for each `k ∈ ℕ` the canonical resolution
`𝒞^•(X, ℱ_k) = (𝒞^i(X, ℱ_k))_{i ≥ 0}` of `ℱ_k` by flasque sheaves `(G, II, 4.3)`. For each `i ≥ 0`, it is clear that
`(𝒞^i(X, ℱ_k))_{k ∈ ℕ}` is a projective system of flasque sheaves; let us

<!-- original page 69 -->

show that it satisfies the conditions of _a)_. Indeed, if `𝒩_{hk}` is the kernel of `u_{hk}` for `h ≤ k`, the sequence
`0 → 𝒩_{hk} → ℱ_k → ℱ_h → 0` is exact by (iii), and our assertion follows from the fact that the functor `𝒜 ↝ 𝒞^i(X, 𝒜)`
is exact `(G, II, 4.3)`. Let `𝒢^i = lim_← 𝒞^i(X, ℱ_k)`; one therefore has `H^j(X, 𝒢^i) = 0` for `j > 0` and `i ≥ 0` by
virtue of _a)_. We shall show that `𝒢^• = (𝒢^i)_{i ≥ 0}` is a *resolution* of the sheaf `ℱ`; since `H^j(X, 𝒢^•) = 0` for
`j > 0`, the cohomology `H^•(X, ℱ)` will equal `H^•(Γ(X, 𝒢^•))` `(G, II, 4.7.1)`.

It is clear that, by passage to the projective limit, one deduces from the exact sequences

```text
  0 → ℱ_k → 𝒞^0(X, ℱ_k) → 𝒞^1(X, ℱ_k) → …
```

a complex of sheaves of abelian groups

```text
  0 → ℱ → 𝒢^0 → 𝒢^1 → … .
```

To prove our assertion, one must establish that `ℋ^i(𝒢^•) = 0` for `i > 0`. This sheaf is generated by the presheaf
`U ↦ H^i(Γ(U, 𝒢^•))` `(G, II, 4.1)`; now, the complex `Γ(U, 𝒢^•)` is the projective limit of the projective system of
complexes of abelian groups `(Γ(U, 𝒞^•(X, ℱ_k)))_{k ∈ ℕ}` `(0_I, 3.2.6)`. We have seen in _a)_ that for each `i ≥ 0`,
the maps `Γ(U, 𝒞^i(X, ℱ_k)) → Γ(U, 𝒞^i(X, ℱ_h))` (`h ≤ k`) are *surjective*; on the other hand, one has
`H^i(U, ℱ_k) = H^i(Γ(U, 𝒞^•(X, ℱ_k)))`, the canonical resolution `𝒞^•(U, ℱ_k|U)` being induced on `U` by `𝒞^•(X, ℱ_k)`;
by virtue of hypothesis (i), for every `U ∈ 𝔅`, one can apply `(13.2.3)` to the projective system of complexes
`(Γ(U, 𝒞^•(X, ℱ_k)))_{k ∈ ℕ}`, and one therefore has `H^i(Γ(U, 𝒢^•)) = lim_← H^i(U, ℱ_k)` for every `i ≥ 0`. Hypothesis
(ii) then proves indeed, by definition, that the sheaves `ℋ^i(𝒢^•)` are zero for `i > 0`.

One has then for every `i ≥ 0`, `H^i(X, ℱ) = H^i(Γ(X, 𝒢^•))` and

```text
  Γ(X, 𝒢^•) = lim_← Γ(X, 𝒞^•(X, ℱ_k)).
```

We have just remarked that the maps `Γ(X, 𝒞^i(X, ℱ_k)) → Γ(X, 𝒞^i(X, ℱ_h))` (`h ≤ k`) are all surjective; the conclusion
therefore again results from `(13.2.3)`.

**Remarks (13.3.2).**

<!-- label: 0_III.13.3.2 -->

_(i)_ The statement `(13.3.1)` is of interest only for `i > 0`, since for `i = 0`, `h_0` is always an isomorphism
without hypothesis `(0_I, 3.2.6)`.

_(ii)_ Conditions (i) and (ii) of `(13.3.1)` will in particular be satisfied if `H^i(U, ℱ_k) = 0` for every `k`, every
`i > 0` and every `U ∈ 𝔅`, and if for `U ∈ 𝔅`, the maps `Γ(U, ℱ_k) → Γ(U, ℱ_h)` are surjective. This will be the most
frequent case of application of `(13.3.1)`.

### 13.4. The Mittag–Leffler condition and graded objects associated to projective systems

**13.4.1.**

<!-- label: 0_III.13.4.1 -->

Let `𝐀 = (A_k, u_{hk})_{k ∈ ℤ}` be a projective system in an abelian category `𝒞`; we shall say that it is *bounded
below* if there exists `k_0` such that `A_k = 0` for `k < k_0`.

We shall define on each `A_k` a filtration `(F^p(A_k))_{p ∈ ℤ}` by the formulas

```text
  F^p(A_k) = Ker(A_k → A_{p−1})    for p ≤ k+1                              (13.4.1.1)
  F^p(A_k) = 0                      for p ≥ k+1
```

<!-- original page 70 -->

One has therefore by hypothesis `F^k(A_k) = A_k` and `F^{k+1}(A_k) = 0`, in other words the filtration considered is
*finite* `(11.1.3)`. The graded objects associated to this filtration are therefore

```text
  gr^p(A_k) = Ker(A_k → A_{p−1}) / Ker(A_k → A_p)
```

and consequently `gr^p(A_k)` is isomorphic to the image under `A_k → A_p` of `Ker(A_k → A_{p−1})`; by virtue of the
transitivity of the morphisms defining a projective system, one therefore has

```text
  gr^p(A_k) = Ker(A_p → A_{p−1}) ∩ Im(A_k → A_p)                            (13.4.1.2)
```

but since, by virtue of `(13.4.1.1)`, one has `Ker(A_p → A_{p−1}) = gr^p(A_p)`, one also has

```text
  gr^p(A_k) = gr^p(A_p) ∩ Im(A_k → A_p).                                    (13.4.1.3)
```

The preceding definitions show, moreover, that one has for `k ≤ h`

```text
  u_{hk}(F^p(A_k)) ⊂ F^p(A_h)
```

and consequently that the `gr^p(u_{hk})` define a projective system `(gr^p(A_k))_{k ∈ ℤ}` for every `p ∈ ℤ`.

**13.4.2.**

<!-- label: 0_III.13.4.2 -->

We shall say that the projective system `𝐀` is *essentially constant* if the morphisms `A_{k+1} → A_k` are isomorphisms
for `k` large enough. We shall say that the projective system `𝐀` is *strict* if the morphisms `A_i → A_j` (`j ≤ i`) are
epimorphisms. When `𝐀` is strict, it follows from `(13.4.1.3)` that for `p ≤ k ≤ h`, the canonical morphism
`gr^p(A_h) → gr^p(A_k)` is an isomorphism, in other words, the projective system `(gr^p(A_k))_{k ∈ ℤ}` is *essentially
constant*. The sequence of objects `gr^p(A_p)` (identified with `lim_← gr^p(A_k)` for every `p`) is then denoted
`gr^•(𝐀)` and called the *graded object associated to the strict projective system* `𝐀 = (A_k)`.

If one now supposes that the projective system `𝐀` (bounded below) satisfies `(ML)`, one knows `(13.1.2)` that the
projective system `𝐀' = (A'_k)` of objects of "universal images" is *strict*, and is moreover bounded below; the graded
object `gr^•(𝐀')` associated to `𝐀'` is then again called the *graded object associated to* `𝐀` and denoted `gr^•(𝐀)`.

**Proposition (13.4.3).**

<!-- label: 0_III.13.4.3 -->

Let `𝐀 = (A_k)_{k ∈ ℤ}` be a projective system bounded below in an abelian category `𝒞`. The following two conditions
are equivalent:

- _a)_ `𝐀` satisfies condition `(ML)`.
- _b)_ For every `p ∈ ℤ`, the projective system `(gr^p(A_k))_{k ∈ ℤ}` is essentially constant.

In addition, when these conditions are satisfied, one has for every `p ∈ ℤ` a canonical isomorphism

```text
  gr^p(𝐀) ⥲ lim_← gr^p(A_k).                                                (13.4.3.1)
            k
```

It follows immediately from `(13.4.1.2)` that _a)_ implies _b)_; the same formula applied to the projective system `𝐀'`
(notations of `(13.4.2)`) gives the isomorphism `(13.4.3.1)` by definition. For `k ≤ h`, set `A_{kh} = Im(A_h → A_k)`;
if `k ≤ h ≤ j`, one has `A_{kj} ⊂ A_{kh} ⊂ A_k`. Equip `A_{kh}` with the filtration induced by `(F^p(A_k))`; one
verifies immediately, by virtue of the transitivity of the morphisms defining `𝐀`, that this filtration is also the
quotient filtration of `(F^p(A_h))`; consequently, one has

```text
  gr^p(A_{kh}) = Im(gr^p(A_h) → gr^p(A_k)).                                  (13.4.3.2)
```

<!-- original page 71 -->

That being so, suppose _b)_ verified; for every `p ∈ ℤ` and every `k ≥ p`, there exists an integer `L(p, k)` such that
the right-hand side of `(13.4.3.2)` is constant for `h ≥ L(p, k)`; since `gr^p(A_k) = 0` for `p < k_0`, there is only
(for `k` given) a finite number of `L(p, k)` non-zero when `p` runs over the set of integers `≤ k`. Let `L(k) = m` be
the largest of these integers; for every `h ≥ m`, one has `A_{kh} ⊂ A_{km}`, and by definition of `m`, the canonical
injection `A_{kh} → A_{km}` defines an isomorphism `gr^•(A_{kh}) ⥲ gr^•(A_{km})`; since the filtrations are finite, one
concludes that the preceding injection is itself bijective (Bourbaki, _Alg. comm._, ch. III, §2, n° 8, th. 1), which
proves that `𝐀` satisfies `(ML)`.

**13.4.4.**

<!-- label: 0_III.13.4.4 -->

Suppose that in `𝒞` the projective limit `A = lim_← A_k` exists. In the definitions of `(13.4.1)`, one can then replace
`A_k` by `A`, and the filtration thus defined on `A` is again such that

```text
  gr^p(A) = gr^p(A_p) ∩ Im(A → A_p).                                         (13.4.4.1)
```

**Corollary (13.4.5).**

<!-- label: 0_III.13.4.5 -->

Suppose that `𝒞` is the category of abelian groups. If the projective system `𝐀` satisfies `(ML)` and if
`A = lim_← A_k`, one has for every `p ∈ ℤ` a canonical isomorphism

```text
  gr^p(A) ⥲ lim_← gr^p(A_k).                                                 (13.4.5.1)
            k
```

Indeed, one has `Im(A_k → A_p) = Im(A → A_p)` whenever `k` is large enough (Bourbaki, _Top. gén._, ch. II, 3rd ed., §3,
n° 5, th. 1), and the conclusion results from `(13.4.1.3)` and `(13.4.4.1)`.

### 13.5. Projective limits of spectral sequences of filtered complexes

**13.5.1.**

<!-- label: 0_III.13.5.1 -->

Let `𝒞` be an abelian category, `X^•` a complex of objects of `𝒞` equipped with a filtration `(F^p(X^•))_{p ∈ ℤ}` such
that `F^{p_0}(X^•) = X^•` for some index `p_0`. Consider for each `k ∈ ℤ` the complex `X^•_k = X^•/F^{k+1}(X^•)`; it is
canonically equipped with the filtration formed by the `F^p(X^•_k) = F^p(X^•)/F^{k+1}(X^•)` for `p ≤ k` and
`F^p(X^•_k) = 0` for `p ≥ k+1`. Moreover, one has canonical morphisms `X^•_{k+1} → X^•_k`, which make
`𝐗^• = (X^•_k)_{k ∈ ℤ}` a projective system of filtered complexes of objects of `𝒞`. Note that this projective system is
*strict* and is such that `X^•_k = 0` for `k < p_0`.

**13.5.2.**

<!-- label: 0_III.13.5.2 -->

Consider more generally a *strict* projective system `𝐗^• = (X^•_k)_{k ∈ ℤ}` of complexes of objects of `𝒞`, bounded
below; consider on each `X^•_k` the filtration defined in `(13.4.1)` (placing oneself in the abelian category of
complexes of `𝒞` bounded below). The `X^•_k → X^•_p` (`p ≤ k`) become morphisms of filtered complexes, with finite
filtrations. The functorial character of the spectral sequences of filtered complexes `(11.2.3)` shows that the
morphisms defining the projective system `𝐗^•` furnish morphisms making `E(𝐗^•) = (E(X^•_k))` a projective system of
spectral sequences.

**Lemma (13.5.3).**

<!-- label: 0_III.13.5.3 -->

Suppose that the projective system `𝐗^• = (X^•_k)_{k ∈ ℤ}` of filtered complexes is obtained as in `(13.5.2)`. Then:

- _a)_ For `r ≥ p − p_0`, one has `B^{pq}_r(X^•_k) = B^{pq}_∞(X^•_k)` for every `k ∈ ℤ`.
- _b)_ For `k + 1 ≥ p + r`, one has `Z^{pq}_r(X^•_k) = Z^{pq}_∞(X^•_k)`.
- _c)_ For `k + 1 ≥ p + r`, the morphisms `Z^{pq}_r(X^•_h) → Z^{pq}_r(X^•_k)` and `B^{pq}_r(X^•_h) → B^{pq}_r(X^•_k)`
    are isomorphisms for every `h ≥ k`.

<!-- original page 72 -->

These three properties result immediately from the definitions of `(11.2.2)`, taking into account that
`F^{p−r+1}(X^•_k) = X^•_k` for `p − r < p_0`.

**13.5.4.**

<!-- label: 0_III.13.5.4 -->

Suppose the hypotheses of `(13.5.3)` are satisfied. Then, for `p`, `q`, `r` fixed (`r` finite), the projective systems
`(Z^{pq}_r(X^•_k))_{k ∈ ℤ}`, `(B^{pq}_r(X^•_k))_{k ∈ ℤ}`, `(E^{pq}_r(X^•_k))_{k ∈ ℤ}` are *essentially constant*; one
will denote by `Z^{pq}_r(𝐗^•)`, `B^{pq}_r(𝐗^•)` and `E^{pq}_r(𝐗^•) = Z^{pq}_r(𝐗^•)/B^{pq}_r(𝐗^•)` their respective
projective limits. The `Z^{pq}_r(𝐗^•)` and `B^{pq}_r(𝐗^•)` identify canonically with subobjects of `E^{pq}_1(𝐗^•)`. The
definition of the `d^{pq}_r` `(M, XV, 1)` shows that these morphisms (relative to the `X^•_k`) are also essentially
constant, and consequently define morphisms

```text
  d^{pq}_r : E^{pq}_r(𝐗^•) → E^{p+r, q−r+1}_r(𝐗^•)                          (13.5.4.1)
```

such that `d^{p+r, q−r+1}_r ∘ d^{pq}_r = 0`; moreover, one has canonical isomorphisms of `Ker(d^{pq}_r)` onto
`Z^{pq}_{r+1}(𝐗^•)/B^{pq}_r(𝐗^•)` and of `Im(d^{pq}_r)` onto `B^{p+r, q−r+1}_{r+1}(𝐗^•)/B^{p+r, q−r+1}_r(𝐗^•)`.

**Lemma (13.5.5).**

<!-- label: 0_III.13.5.5 -->

Under the hypotheses of `(13.5.3)`, one has, for `s ≥ r > p − p_0`, a canonical monomorphism

```text
  i : E^{pq}_s(𝐗^•) → E^{pq}_r(𝐗^•)                                         (13.5.5.1)
```

and a canonical isomorphism

```text
  j_r : E^{pq}_r(𝐗^•) ⥲ E^{pq}_∞(X^•_{p+r−1})                               (13.5.5.2)
```

such that the diagram

```text
                       j_s
  E^{pq}_s(𝐗^•) ----------> E^{pq}_∞(X^•_{p+s−1})
       ↓ i                          ↓
  E^{pq}_r(𝐗^•) ----------> E^{pq}_∞(X^•_{p+r−1})                           (13.5.5.3)
                       j_r
```

is commutative (the right-hand vertical arrow coming from the morphism `X^•_{p+s−1} → X^•_{p+r−1}`).

The existence of `i` comes from the fact that `B^{pq}_r(X^•_k) = B^{pq}_∞(X^•_k)` for `r > p − p_0` `(13.5.3, a))`; one
has `Z^{pq}_r(X^•_k) = Z^{pq}_∞(X^•_k)` for `k + 1 ≥ p + r` `(13.5.3, b))`, whence in particular
`Z^{pq}_r(X^•_{p+r−1}) = Z^{pq}_∞(X^•_{p+r−1})`, and on the other hand `Z^{pq}_r(X^•_{p+r−1})` and
`B^{pq}_r(X^•_{p+r−1})` identify canonically with `Z^{pq}_r(𝐗^•)` and `B^{pq}_r(𝐗^•)` by virtue of `(13.5.3, c))`,
whence the existence of `j_r` and the commutativity of `(13.5.5.3)`.

**Corollary (13.5.6).**

<!-- label: 0_III.13.5.6 -->

Under the hypotheses of `(13.5.3)`, if one of the projective limits `lim_← E^{pq}_r(𝐗^•)`, `lim_← E^{pq}_∞(X^•_k)`
exists, so does the other, and one has a canonical isomorphism

```text
  j_∞ : lim_r E^{pq}_r(𝐗^•) ⥲ lim_k E^{pq}_∞(X^•_k).                        (13.5.6.1)
```

In addition, for the projective system `(E^{pq}_r(𝐗^•))_{r ∈ ℤ}` to be essentially constant `(13.4.2)`, it is necessary
and sufficient that the projective system `(E^{pq}_∞(X^•_k))_{k ∈ ℤ}` be so.

**13.5.7.**

<!-- label: 0_III.13.5.7 -->

One denotes by `B^{pq}_∞(𝐗^•)` and `Z^{pq}_∞(𝐗^•)` the subobjects of `E^{pq}_1(𝐗^•)` respectively equal to
`B^{pq}_r(𝐗^•)` for `r > p − p_0` and to `inf_r Z^{pq}_r(𝐗^•)` (when the latter exists), so that `lim_← E^{pq}_r(𝐗^•)`

<!-- original page 73 -->

identifies canonically with `E^{pq}_∞(𝐗^•) = Z^{pq}_∞(𝐗^•)/B^{pq}_∞(𝐗^•)`. One will note that the objects
`Z^{pq}_∞(𝐗^•)`, `B^{pq}_∞(𝐗^•)`, `E^{pq}_r(𝐗^•)` (`1 ≤ r ≤ +∞`) and `d^{pq}_r` depend *functorially* on the projective
system `𝐗^•` submitted to the restrictions of `(13.5.5)`, and that the morphisms defined in `(13.5.5)` and `(13.5.6)`
are functorial.

### 13.6. Spectral sequence of a functor relative to an object equipped with a finite filtration

**13.6.1.**

<!-- label: 0_III.13.6.1 -->

Let `𝒞`, `𝒞'` be two abelian categories, `T : 𝒞 → 𝒞'` a covariant additive functor. Suppose that every object of `𝒞` is
isomorphic to a subobject of an injective object, so that the right-derived functors `R^p T` (`p ≥ 0`) exist.

**Lemma (13.6.2).**

<!-- label: 0_III.13.6.2 -->

Let `A` be an object of `𝒞`, equipped with a finite filtration `(F^i(A))_{i ∈ ℤ}`. There exists an injective resolution
`X^• = (X^i)_{i ≥ 0}` of `A` equipped with a finite filtration `(F^i(X^•))_{i ∈ ℤ}` such that the relation `F^i(A) = A`
(resp. `F^i(A) = 0`) entails `F^i(X^•) = X^•` (resp. `F^i(X^•) = 0`) and such that, for every `i ∈ ℤ`, `F^i(X^•)` is an
injective resolution of `F^i(A)`.

Let `p` (resp. `q > p`) be the largest index such that `F^p(A) = A` (resp. the smallest index for which `F^q(A) = 0`).
One reasons by induction on `q − p`, the lemma being evident for `q − p = 1`. Having formed an injective resolution
`X'''^•` of `A/F^{q−1}(A)` having the desired properties, one considers the exact sequence
`0 → F^{q−1}(A) → A → A/F^{q−1}(A) → 0`, one takes an injective resolution `X''^•` of `F^{q−1}(A)`, then one determines
an injective resolution `X^•` of `A` so as to have an exact sequence `0 → X''^• → X^• → X'''^• → 0` compatible with the
preceding `(M, V, 2.2)`; it is clear that `X^•` answers the question.

**Corollary (13.6.3).**

<!-- label: 0_III.13.6.3 -->

Let `B` be a second object of `𝒞`, equipped with a finite filtration `(F^i(B))_{i ∈ ℤ}`, `s` an integer, and let
`u : A → B` be a morphism such that `u(F^i(A)) ⊂ F^{i+s}(B)` for every `i ∈ ℤ`. If `Y^• = (Y^i)_{i ≥ 0}` is an injective
resolution of `B` equipped with a filtration `(F^i(Y^•))_{i ∈ ℤ}` having the properties stated in `(13.6.2)`, there
exists a morphism `v : X^• → Y^•` compatible with `u` and such that `v(F^i(X^•)) ⊂ F^{i+s}(Y^•)` for every `i ∈ ℤ`. In
addition, two such morphisms `v`, `v'` are homotopic.

This results immediately by induction on `q − p` from the preceding construction and from `(M, V, 2.3)`.

**13.6.4.**

<!-- label: 0_III.13.6.4 -->

Under the hypotheses of `(13.6.2)`, consider now the complex `T(X^•)` in `𝒞'`, which is evidently filtered by the
complexes `T(F^i(X^•))`, since `F^i(X^•)` is a direct factor of `X^•`. It follows from `(13.6.3)` that the spectral
sequence of this filtered complex depends only on the filtered object `A`, up to isomorphism. Its abutment is the
cohomology `R^•T(A)`, with the filtration

```text
  F^p(R^n T(A)) = Im(R^n T(F^p(A)) → R^n T(A))
                = Ker(R^n T(A) → R^n T(A/F^p(A)))                           (13.6.4.1)
```

`(11.2.2)`, and its term `E_1` is given by

```text
  E^{pq}_1 = R^{p+q} T(gr^p(A))                                              (13.6.4.2)
```

`gr^p(A)` denoting as usual `F^p(A)/F^{p+1}(A)`. It is clear, by `(11.2.2)`, that the filtration of the abutment is
finite, and that for `p`, `q` given, the sequences of

<!-- original page 74 -->

`B^{pq}_r(A) = B^{pq}_r(T(X^•))` and `Z^{pq}_r(A) = Z^{pq}_r(T(X^•))` are stationary, so the preceding spectral sequence
is *biregular* `(11.1.3)`. We shall denote this sequence `E(A) = (E^{pq}_r(A))` and we shall say that it is the
*spectral sequence of the functor* `T` *relative to the filtered object* `A`.

**13.6.5.**

<!-- label: 0_III.13.6.5 -->

Suppose now the hypotheses of `(13.6.3)` are satisfied, whose notations we keep. Since `F^i(X^•)` (resp. `F^i(Y^•)`) is
a direct factor of `X^•` (resp. `Y^•`), one has `(Tv)(T(F^i(X^•))) ⊂ T(F^{i+s}(Y^•))` for every `i ∈ ℤ`; the definitions
of `(11.2.2)` show then that for `1 ≤ r ≤ +∞`, `Tv` defines a morphism `B^{pq}_r(T(X^•)) → B^{p+s, q−s}_r(T(Y^•))` and a
morphism `Z^{pq}_r(T(X^•)) → Z^{p+s, q−s}_r(T(Y^•))`, whence a morphism

```text
  w_r : E^{pq}_r(A) → E^{p+s, q−s}_r(B);
```

similarly, one has for the abutment morphisms `u_n : R^n T(A) → R^n T(B)` such that
`u_n(F^p(R^n T(A))) ⊂ F^{p+s}(R^n T(B))`.

The definition of the `d^{pq}_r` `(M, XV, 1)` shows moreover that the diagrams

```text
                       d^{pq}_r
       E^{pq}_r(A) ----------------> E^{p+r, q−r+1}_r(A)
            ↓ w_r                            ↓ w_r
  E^{p+s, q−s}_r(B) -------------> E^{p+r+s, q−r−s+1}_r(B)
                  d^{p+s, q−s}_r
```

are commutative; one deduces an analogous commutative diagram for the isomorphisms `α^{pq}_r`, which we shall leave to
the reader the care of making explicit. Finally `(loc. cit.)`, one also has commutative diagrams for the abutments

```text
                    β^{pq}
       E^{pq}_∞(A) -------> gr^p(R^{p+q} T(A))
            ↓ w_∞                  ↓ u_{p+q}
  E^{p+s, q−s}_∞(B) ----> gr^{p+s}(R^{p+q} T(B))
                  β^{p+s, q−s}
```

**13.6.6.**

<!-- label: 0_III.13.6.6 -->

Suppose in particular that there exists a ring `𝒮`, equipped with a filtration `(F^i(𝒮))_{i ∈ ℤ}`, and a ring
homomorphism

```text
  h : 𝒮 → Hom_𝒞(A, A)                                                       (13.6.6.1)
```

<!-- original page 75 -->

such that for every `t ∈ F^i(𝒮)`, one has `h_t(F^j(A)) ⊂ F^{i+j}(A)` for every pair `i`, `j`. We shall say for brevity
that `A` is then equipped with a structure of `𝒮`-`𝒞`-module filtered over the filtered ring `𝒮`. By passage to the
associated graded objects, every `h_t` for `t ∈ F^j(𝒮)` defines a graded endomorphism `h̄_t` of `gr^•(A)`, homogeneous
of degree `j`; moreover, this morphism depends only on the class of `t` in `gr^j(𝒮)`, and one thus defines a
homomorphism of graded rings

```text
  h̄ : gr^•(𝒮) → Hom_𝒞(gr^•(A), gr^•(A))
```

where the right-hand side is the ring of graded endomorphisms of `gr^•(A)`. We shall say that `gr^•(A)` is equipped with
a structure of `gr^•(𝒮)`-`𝒞`-module graded. It follows then from `(13.6.5)` that for `1 ≤ r ≤ +∞`, every `t̄ ∈ gr^j(𝒮)`
canonically defines in the bigraded objects `(B^{pq}_r(A))_{(p,q) ∈ ℤ × ℤ}`, `(Z^{pq}_r(A))_{(p,q) ∈ ℤ × ℤ}` and
`E_r(A) = (E^{pq}_r(A))_{(p,q) ∈ ℤ × ℤ}` bigraded endomorphisms of degrees `(j, −j)`; in `E_r(A)` (for `r` finite), this
endomorphism commutes with the bigraded endomorphism defined by the `d^{pq}_r`. Since these endomorphisms satisfy the
usual conditions of associativity and distributivity with respect to the addition in `gr^•(𝒮)` and in the bigraded
objects considered, we shall say for brevity that the latter are `gr^•(𝒮)`-`𝒞'`-modules *bigraded*; it is immediate that
the `α^{pq}_r` define an isomorphism for this type of structures. For every integer `n`, one will denote by
`B^{(n)}_r(A)` (resp. `Z^{(n)}_r(A)`, `E^{(n)}_r(A)`) the graded subobject of `B^{••}_r(A)` (resp. `Z^{••}_r(A)`,
`E^{••}_r(A)`) formed by the `B^{pq}_r(A)` (resp. `Z^{pq}_r(A)`, `E^{pq}_r(A)`) such that `p + q = n` (for
`1 ≤ r < +∞`); it is immediate that these are `gr^•(𝒮)`-`𝒞'`-modules graded. Finally, every `t̄ ∈ gr^j(𝒮)` defines for
every `n` a graded endomorphism of degree `j` in the graded object `gr^•(R^n T(A))`, which is thus equipped with a
structure of `gr^•(𝒮)`-`𝒞'`-module graded, the `β^{pq}` (for `p + q = n`) define an isomorphism of `E^{(n)}_∞(A)` onto
`gr^•(R^n T(A))` for this kind of structure.

Note that when `𝒞'` is the category of abelian groups, the structures of `𝒮`-`𝒞'`-module (resp. of `gr^•(𝒮)`-`𝒞'`-module
graded or bigraded) are none other than the usual structures of `𝒮`-module (resp. `gr^•(𝒮)`-module graded, bigraded).

### 13.7. Derived functors of a projective limit of arguments

**13.7.1.**

<!-- label: 0_III.13.7.1 -->

Let `𝒞`, `𝒞'` be two abelian categories, `𝒞` being supposed such that every object of `𝒞` is a subobject of an injective
object; let `T : 𝒞 → 𝒞'` be a covariant additive functor. Consider a *strict* projective system `𝐀 = (A_k)_{k ∈ ℤ}` in
`𝒞`, *bounded below*; to be precise, we shall suppose that `A_k = 0` for `k < k_0`. We associate canonically to this
system a filtration `(F^p(A_k))_{p ∈ ℤ}` on each `A_k` by the formulas `(13.4.1.1)`, and since this is a strict
projective system, the canonical morphisms

```text
  F^i(A_h)/F^j(A_h) → F^i(A_k)/F^j(A_k)    (h ≥ k)                           (13.7.1.1)
```

for `i ≤ j ≤ k + 1` are isomorphisms. Recall in addition that one has `F^k(A_k) = A_k` and `F^{k+1}(A_k) = 0` for every
`k`.

**13.7.2.**

<!-- label: 0_III.13.7.2 -->

Let us construct now for each `k` an injective resolution `X^•_k = (X^i_k)_{i ≥ 0}` of `A_k` having the properties of
`(13.6.2)`. The canonical morphisms `A_{k+1} → A_k` allow `(13.6.3)` to define for each `k` a morphism of complexes
`X^•_{k+1} → X^•_k` compatible

<!-- original page 76 -->

with the filtrations, and making `𝐗^• = (X^•_k)_{k ∈ ℤ}` a projective system of complexes. One can in addition suppose
that this projective system is *strict*. For this, one observes that by virtue of the isomorphism `(13.7.1.1)`, `A_k` is
isomorphic to `A_{k+1}/F^{k+1}(A_{k+1})`; one can therefore take, in the construction of `X^•_{k+1}`, the injective
resolution of `A_{k+1}/F^{k+1}(A_{k+1})` equal to `X^•_k`, and it results from `(M, V, 2.3)` that the construction of
the morphism of complexes `X^•_{k+1} → X^•_k` can be done so that this morphism furnishes by passage to the quotients an
isomorphism `X^•_{k+1}/F^{k+1}(X^•_{k+1}) ⥲ X^•_k` respecting the filtrations, which is the condition of `(13.5.1)`.

**13.7.3.**

<!-- label: 0_III.13.7.3 -->

By construction, the projective system `T(𝐗^•)` of complexes `T(X^•_k)` satisfies the hypotheses of `(13.5.3)`. The
results of `(13.5.4)`, `(13.5.5)` and `(13.5.6)` are therefore applicable to the spectral sequences
`E(T(X^•_k)) = E(A_k)`; we shall write `E^{pq}_r(𝐀)` instead of `E^{pq}_r(T(𝐗^•))` for `1 ≤ r ≤ +∞` (cf. `(13.5.7)` for
`r = +∞`) and similarly for analogous notations. One will note in particular that one has

```text
  E^{pq}_1(𝐀) = R^{p+q} T(gr^p(𝐀))                                          (13.7.3.1)
```

by virtue of `(13.6.4.2)` and of the fact that the system `(gr^p(A_k))` is essentially constant.

These results and `(13.4.3)` give the following proposition, first proved by Shih Weishu by a different (unpublished)
method:

**Proposition (13.7.4) (Shih).**

<!-- label: 0_III.13.7.4 -->

Let `n` be an integer. The following two conditions are equivalent:

- _a)_ For every pair `(p, q)` such that `p + q = n`, the projective system `(E^{pq}_r(𝐀))_{r ≥ 2}` is essentially
    constant.
- _b)_ The projective system `R^n T(𝐀) = (R^n T(A_k))_{k ∈ ℤ}` satisfies `(ML)`.

In addition, when these conditions are satisfied, one has a canonical isomorphism

```text
  gr^p(R^n T(𝐀)) ⥲ E^{p, n−p}_∞(𝐀)    for every p ∈ ℤ.                       (13.7.4.1)
```

Indeed, by virtue of `(13.5.6)`, condition _a)_ is equivalent to saying that the projective system
`(E^{pq}_∞(A_k))_{k ∈ ℤ}` is essentially constant for `p + q = n`, and on the other hand `gr^p(R^n T(A_k))` is
canonically isomorphic to `E^{p, n−p}_∞(A_k)`, so it results from `(13.4.3)` that _a)_ and _b)_ are equivalent; the
isomorphism `(13.7.4.1)` is none other than `(13.5.6.1)` applied to the case considered here.

**Corollary (13.7.5).**

<!-- label: 0_III.13.7.5 -->

Let `ℱ = (ℱ_k)_{k ∈ ℕ}` be a projective system of sheaves of abelian groups satisfying conditions (i), (ii) and (iii) of
`(13.3.1)` and let `ℱ = lim_← ℱ_k`. Suppose that, for the functor `𝒢 ↦ Γ(X, 𝒢)`, the projective system
`(E^{pq}_r(ℱ))_{r ∈ ℤ}` is essentially constant for every pair `(p, q)` such that `p + q = n` or `p + q = n + 1`.
Consider on `H^{n+1}(X, ℱ)` the filtration defined by `F^p(H^{n+1}(X, ℱ)) = Ker(H^{n+1}(X, ℱ) → H^{n+1}(X, ℱ_{p−1}))`.
One has then a canonical isomorphism

```text
  gr^p(H^{n+1}(X, ℱ)) ⥲ E^{p, n−p+1}_∞(ℱ)    for every p ∈ ℤ.                (13.7.5.1)
```

It results from `(13.7.4)` applied to the case where `𝒞` is the category of sheaves of abelian groups on `X`, `𝒞'` the
category of abelian groups, and `T = Γ`, that one has a canonical isomorphism

<!-- original page 77 -->

`gr^p(R^{n+1} Γ(ℱ)) ⥲ E^{p, n−p+1}_∞(ℱ)` for every `p ∈ ℤ`. On the other hand, since by virtue of `(13.7.4)`, the
projective system `(H^n(X, ℱ_k))_{k ∈ ℤ}` satisfies `(ML)`, one deduces from `(13.3.1)` a canonical isomorphism

```text
  H^{n+1}(X, ℱ) ⥲ lim_← H^{n+1}(X, ℱ_k).                                    (13.7.5.1)
                  k
```

Since the projective system `R^{n+1} Γ(ℱ)` satisfies `(ML)` by virtue of `(13.7.4)`, one has a canonical isomorphism
`gr^p(R^{n+1} Γ(ℱ)) ⥲ lim_← gr^p(H^{n+1}(X, ℱ_k))` `(13.4.3)`, and a canonical isomorphism
`lim_← gr^p(H^{n+1}(X, ℱ_k)) ⥲ gr^p(lim_← H^{n+1}(X, ℱ_k))` `(13.4.5)`. It therefore all comes down to seeing that the
isomorphism `(13.7.5.1)` is compatible with the filtrations of the two sides; but this results immediately from the
definitions and from the commutativity of the diagram

```text
  H^{n+1}(X, ℱ) ⥲ lim_← H^{n+1}(X, ℱ_k)
              ↘            ↙
              H^{n+1}(X, ℱ_{p−1})
```

for every `p`.

**13.7.6.**

<!-- label: 0_III.13.7.6 -->

Let `𝒮` be a ring equipped with a filtration `(F^i(𝒮))_{i ∈ ℤ}` such that `F^0(𝒮) = 𝒮` (so `gr^i(𝒮) = 0` for `i < 0`).
Suppose that each of the `A_k`, equipped with the filtration defined in `(13.7.1)`, is an `𝒮`-`𝒞`-module filtered
`(13.6.6)`, the morphisms `A_h → A_k` for `k ≤ h` being morphisms for the structure of `𝒮`-`𝒞`-module filtered; we shall
say for brevity that `𝐀` is a *projective system of `𝒮`-`𝒞`-modules filtered*. Then it is immediate that the morphisms
`B^{pq}_r(A_h) → B^{pq}_r(A_k)` and `Z^{pq}_r(A_h) → Z^{pq}_r(A_k)` for `k ≤ h`, `1 ≤ r ≤ +∞`, are morphisms for the
structures of `gr^•(𝒮)`-`𝒞'`-module bigraded `(13.6.5)`, and that the families `(Z^{pq}_r(𝐀))`, `(B^{pq}_r(𝐀))` and
`(E^{pq}_r(𝐀))` are `gr^•(𝒮)`-`𝒞'`-modules bigraded for `r` finite, the first two being submodules of `(E^{pq}_r(𝐀))`.
One will again denote by `Z^{(n)}_r(𝐀)`, `B^{(n)}_r(𝐀)`, `E^{(n)}_r(𝐀)` the respective subobjects of the preceding
obtained by taking only the terms such that `p + q = n`; these are `gr^•(𝒮)`-`𝒞'`-modules graded.

When the system `(E^{pq}_r(𝐀))_{r ∈ ℤ}` is essentially constant, `(E^{pq}_∞(𝐀))` is therefore also a
`gr^•(𝒮)`-`𝒞'`-module bigraded, and each `E^{(n)}_∞(𝐀)` a `gr^•(𝒮)`-`𝒞'`-module graded. In addition, the
`β^{p, n−p} : E^{p, n−p}_∞(A_k) ⥲ gr^p(R^n T(A_k))` constitute for each `k` an isomorphism for the structure of
`gr^•(𝒮)`-`𝒞'`-module graded of `E^{(n)}_∞(A_k)` onto `gr^•(R^n T(A_k))`; if one is in the preceding conditions,
`β^{p, n−p} : E^{p, n−p}_∞(𝐀) ⥲ lim_← gr^•(R^n T(A_k))` will therefore also be an isomorphism for these structures, and
it is evidently the same for the canonical isomorphism `gr^•(R^n T(𝐀)) ⥲ lim_← gr^•(R^n T(A_k))`, so the isomorphisms
`(13.7.4.1)` constitute an isomorphism for the structures of `gr^•(𝒮)`-`𝒞'`-module graded.

**Proposition (13.7.7).**

<!-- label: 0_III.13.7.7 -->

Let `S` be a noetherian `𝔍`-adic ring. Suppose that `𝒞` is an abelian category every object of which is isomorphic to a
subobject of an injective object, and let `T` be a covariant additive functor from `𝒞` to the category of abelian
groups. Let `𝐀 = (A_k)_{k ∈ ℤ}` be a

<!-- original page 78 -->

strict projective system of `S`-`𝒞`-modules filtered (for the `𝔍`-adic filtration on `S`) bounded below. One supposes
that for some given integer `n`, the following condition is satisfied:

> `(F_n)` The `gr^•(S)`-module graded `E^{(m)}_1(𝐀) = (R^m T(gr^p(𝐀)))_{p ∈ ℤ}` `(13.7.3.1)` is of finite type for
> `m = n` and `m = n + 1`.

Under these conditions:

- _(i)_ The projective systems `(R^n T(A_k))_{k ∈ ℤ}` and `(R^{n+1} T(A_k))_{k ∈ ℤ}` satisfy `(ML)`.
- _(ii)_ If one sets `R^n T(𝐀) = lim_← R^n T(A_k)`, `R^n T(𝐀)` is an `S`-module of finite type.
- _(iii)_ The filtration defined by `F^p(R^n T(𝐀)) = Ker(R^n T(𝐀) → R^n T(A_{p−1}))` (`p ∈ ℤ`) on `R^n T(𝐀)` is
    *`𝔍`-good* (that is, `𝔍 F^p(R^n T(𝐀)) ⊂ F^{p+1}(R^n T(𝐀))` for every `p`, the equality of the two sides holding
    whenever `p` is large enough). In particular, the topology on `R^n T(𝐀)` defined by this filtration is identical to
    the `𝔍`-adic topology.
- _(iv)_ The projective system `(E^{pq}_r(𝐀))_{r ∈ ℤ}` is essentially constant for `p + q = n` and `p + q = n + 1`,
    `E^{pq}_∞(𝐀)` is therefore defined `(13.5.7)` and one has a canonical isomorphism of `gr^•(S)`-modules graded

```text
  gr^p(R^n T(𝐀)) ⥲ E^{p, n−p}_∞(𝐀)    (p ∈ ℤ).                              (13.7.7.1)
```

One will note that the isomorphism `(13.7.7.1)` will allow one to denote `R^n T(𝐀)` by abuse of language the projective
limit `R^n T(𝐀)` of the projective system `R^• T(𝐀)`, taking into account the isomorphisms `(13.7.4.1)`.

Since the graded ring `gr^•(S)` is noetherian (Bourbaki, _Alg. comm._, ch. III, §2, n° 9, cor. 5 of th. 2), the
increasing sequence of graded `gr^•(S)`-submodules `B^{(m)}_r(𝐀)` of `E^{(m)}_1(𝐀)` `(13.6.6)` is stationary for `m = n`
and `m = n + 1`, and consequently condition _b)_ of `(11.1.10)` is satisfied. It follows that condition _a)_ of
`(13.7.4)` is fulfilled for `n` and for `n + 1`, and this already proves (i). In addition, the isomorphisms `(13.7.4.1)`
(taking into account the remarks of `(13.7.6)`) show that `gr^•(R^n T(𝐀))` is a `gr^•(S)`-module graded isomorphic to
`E^{(n)}_∞(𝐀) = Z^{(n)}_∞(𝐀)/B^{(n)}_∞(𝐀)`; since `Z^{(n)}_∞(𝐀)` is a submodule of `E^{(n)}_1(𝐀)`, it is of finite type,
and the same holds for `E^{(n)}_∞(𝐀)`. In addition, for the filtration `(F^p(R^n T(𝐀)))`, it follows from `(13.4.5)`
that `gr^•(R^n T(𝐀))` and `gr^•(R^n T(𝐀))` are `gr^•(S)`-modules isomorphic, which demonstrates (iv). The assertions
(ii) and (iii) will finally be consequences of the preceding results and of the following lemma:

**Lemma (13.7.7.2).**

<!-- label: 0_III.13.7.7.2 -->

Let `S` be a noetherian `𝔍`-adic ring, `M` an `S`-module equipped with a co-discrete filtration `(F^p(M))_{p ∈ ℤ}` such
that `𝔍 F^p(M) ⊂ F^{p+1}(M)` (which expresses that `M` is a module filtered over the ring `S` filtered by the `𝔍`-adic
filtration). Suppose in addition `M` is separated for the topology defined by the filtration `(F^p(M))`. Then the
following conditions are equivalent:

- _a)_ `M` is an `S`-module of finite type and `(F^p(M))` is a `𝔍`-good filtration.
- _b)_ `gr^•(M)` is a `gr^•(S)`-module of finite type.
- _c)_ The `gr^p(M)` are `S`-modules of finite type and for `p` large enough the canonical homomorphisms

```text
  𝔍 ⊗_S gr^p(M) → gr^{p+1}(M)                                                (13.7.7.3)
```

<!-- original page 79 -->

(deduced from `𝔍 ⊗_S F^p(M) → F^{p+1}(M)`, taking into account that the image of the composite homomorphism
`𝔍 ⊗_S F^{p+1}(M) → 𝔍 ⊗_S F^p(M) → F^{p+1}(M)` is `𝔍 F^{p+1}(M) ⊂ F^{p+2}(M)`) are surjective.

For the demonstration, see Bourbaki, _Alg. comm._, ch. III, §3, n° 1, prop. 3.

**13.7.7.4.**

<!-- label: 0_III.13.7.7.4 -->

To apply Lemma `(13.7.7.2)`, it remains to observe that the topology defined on `R^n T(𝐀)` by the filtration considered
makes `R^n T(𝐀)` a separated and complete `S`-module, this topology being that of the projective limit of the discrete
groups `R^n T(A_k)`; on the other hand, if `A_k = 0` for `k < k_0`, one also has `R^n T(A_k) = 0` for `k < k_0`, so
`F^{k_0}(R^n T(𝐀)) = R^n T(𝐀)`, and one is indeed in the conditions of application of the lemma.

**Corollary (13.7.8).**

<!-- label: 0_III.13.7.8 -->

If hypothesis `(F_n)` is satisfied, one has, for every element `f ∈ S`, a canonical isomorphism

```text
  lim_← ((R^n T(A_k))_f) ⥲ R^n T(𝐀) ⊗_S S_{{f}}.                            (13.7.8.1)
    k
```

Indeed, `R^n T(𝐀)` is an `S`-module of finite type, `S_{{f}}` a noetherian adic `S`-algebra `(0_I, 7.6.11)`, separated
completion of `S_f` for the `𝔍`-preadic topology `(0_I, 7.6.2)`. One concludes from `(0_I, 7.7.8)` and `(0_I, 7.7.1)`
that `R^n T(𝐀) ⊗_S S_{{f}}` is isomorphic to the separated completion of `R^n T(𝐀) ⊗_S S_f` for the `𝔍`-preadic
topology; a fundamental system of neighborhoods of `0` for this topology is `(𝔍^p R^n T(𝐀)) ⊗_S S_f`, so
`F^p(R^n T(𝐀)) ⊗_S S_f` is also such a system; the latter is the kernel of the canonical map
`(R^n T(𝐀))_f → (R^n T(A_{p−1}))_f`, and consequently the separated group associated to `R^n T(𝐀) ⊗_S S_f` identifies
with a subgroup `G` of `lim_← ((R^n T(A_k))_f)`. But the projective system `((R^n T(A_k))_f)` evidently satisfies
condition `(ML)`, and the image of `(R^n T(𝐀))_f` in each of the `(R^n T(A_k))_f` equals the common image of the
`(R^n T(A_h))_f` for `h ≥ k` large enough. One concludes immediately that `G` is *everywhere dense* in
`lim_← ((R^n T(A_k))_f)`, and since this latter group is separated and complete, the corollary is demonstrated.

(_To be continued._)
