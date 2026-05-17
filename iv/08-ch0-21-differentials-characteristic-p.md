<!-- original page 249 -->

## §21. Differentials in characteristic-`p` rings

The results of the present section, of a more special and technical nature than those of §§19, 20 and 22, will be used
only exceptionally in the course of Chap. IV. Their principal role here is in the proof of three theorems of §22
(22.3.3, 22.5.8 and 22.7.3), the first and the last of which intervene in an essential way in the "fine" theory of
Noetherian local rings of Chap. IV, §7.

### 21.1. Systems of `p`-generators and `p`-bases

(21.1.1) Given a number `p` which is either `0` or a prime number, we shall say that a ring `A` is *of characteristic
`p`* if there exists a ring homomorphism `P → A`, where `P` is the prime field of characteristic `p`; note that this
homomorphism is then unique, the composite `ℤ → P → A` being the unique homomorphism of `ℤ` into `A`. If `A ≠ 0`, this
amounts to saying that `A` contains a field of characteristic `p`, the image of `P` being necessarily a field isomorphic
to `P` (and moreover the only subfield of `A` isomorphic to `P`).

(21.1.2) If `p > 0`, saying that `A` is of characteristic `p` is equivalent to saying that, in `A`, one has `p·1 = 0`,
or again `pA = 0`. If `p = 0`, saying that `A` is of characteristic `p` is equivalent to saying that for every integer
`n ≠ 0`, `n·1` is invertible in `A`. If `A ≠ 0`, there can exist only one `p` (prime or `0`) such that `A` is of
characteristic `p`; this follows from the preceding and from Bezout's identity `ap + bq = 1` for two distinct primes
`p, q`. By contrast the zero ring is of characteristic `p` for every `p`.

(21.1.3) If `A` is of characteristic `p`, so is every algebra over `A`. In particular, for every prime ideal `𝔭` of
`A`, the residue field of `A` at `𝔭` is of characteristic `p`. Conversely, if `p = 0` and if for every maximal ideal
`𝔪` of `A` the residue field of `A` at `𝔪` is of characteristic `0`, the same holds for `A`, for every integer `n ≠ 0`
is then invertible in all the `A_𝔪`, hence also in `A`. By contrast, if `p > 0`, a local ring may have its residue
field of characteristic `p` without itself being of characteristic `p`, as is shown by the example of the prime ring
(integral) `ℤ_{(p)}` `(19.8.3)` or of the Artinian local ring `ℤ/p^2 ℤ` for `p ≥ 2`, which do not contain a field.

Let us finally note that for a ring (even reduced), the residue fields at its prime ideals may have different
characteristics, as is shown by the example of `ℤ`.

(21.1.4) In all the rest of this section, we suppose fixed a prime number `p` and all rings will be supposed of
characteristic `p`, unless expressly mentioned otherwise. For such a ring `A`, the map `x ↦ x^p` is an endomorphism of
`A`, which we denote `F_A`; if `A` is reduced, `F_A` is injective. One sets `A^p = F_A(A)` (subring of `A` consisting of
the `x^p` for `x ∈ A`); one can naturally consider `A` as an `A^p`-algebra.

One can also consider `A` as an `A`-algebra by means of the homomorphism `F_A : x ↦ x^p` of `A` into `A`; in other
words, this is the `A`-algebra `A_{F_A}` for which the product `λ · x` of `x ∈ A` by a scalar `λ ∈ A` is the product
`λ^p x` in the ring `A`; we shall denote this `A`-algebra `A^{[p]}`. It is clear that for every ring homomorphism
`u : A → B` the pair `(u, u)` is a di-homomorphism of `A`-algebras `A^{[p]} → B^{[p]}`. For every `A`-module `E`, one
sets `E^{[p]} = E ⊗_A A^{[p]}` where `A^{[p]}` is considered as an `(A, A)`-bimodule, the left `A`-module structure
being the one just defined, and the right `A`-module structure defined by multiplication in `A`; `E^{[p]}` is equipped
with the `A`-module structure coming from the right `A`-module structure of `A^{[p]}`, so that for `x ∈ E`, `α, β` in
`A`, one has

```text
  α(x ⊗ β) = x ⊗ (αβ)    and    (αx) ⊗ β = α(x ⊗ β) = x ⊗ α^p β.
```

<!-- original page 250 -->

Setting `x^{[p]} = x ⊗ 1`, one therefore has `(αx)^{[p]} = α^p x^{[p]}`. When `F_A` is injective, one can identify
`A^{[p]}` with the ring `A` considered as algebra over its subring `A^p`.

**Proposition (21.1.5).**

<!-- label: 0_IV.21.1.5 -->

*Let `A`, `B` be two rings, `u : A → B` a homomorphism.*

*(i) Every `A`-derivation of `B` into a `B`-module `L` is zero on `A[B^p]` (and is therefore an `A[B^p]`-derivation).*

*(ii) For every sub-`A`-algebra `A'` of `A[B^p]`, if `j : A' → B` is the canonical injection, the canonical
homomorphism*

```text
  γ_{B/A'/A} : Ω_{B/A} → Ω_{B/A'}
```

*is bijective.*

*(iii) Suppose there exists an integer `s ≥ 0` such that `u(A) ⊃ B^{p^s}`. Then, in the ring `B ⊗_A B`, `𝔍_{B/A}` is a
nilideal.*

(i) By induction starting from `(20.1.1.1)`, one deduces for every `A`-derivation `D : B → L` that one has
`D(x^k) = k x^{k-1} D(x)`, whence in particular `D(x^p) = 0`.

(ii) By `(20.4.8)`, assertion (ii) is only a translation of (i), the latter being written
`Der_A(B, L) = Der_{A[B^p]}(B, L)` for every `B`-module `L`.

(iii) For every `x ∈ B`, one has `(x ⊗ 1 − 1 ⊗ x)^{p^s} = x^{p^s} ⊗ 1 − 1 ⊗ x^{p^s} = x^{p^s}(1 ⊗ 1 − 1 ⊗ 1) = 0`,
since `x^{p^s} ∈ u(A)`. The conclusion follows from the fact that the elements `1 ⊗ x − x ⊗ 1` generate `𝔍_{B/A}`
`(20.4.4)`.

It follows at once from `(21.1.5)` that for every pair of ring homomorphisms `A → B → C`,

```text
  γ_{C/B/A} = γ_{C/B/A}                                                              (21.1.5.1)
```

for every sub-`A`-algebra `A' ⊂ A[B^p]` of `B`.

On the other hand, `(21.1.5)` also shows in particular that for "absolute" modules of differentials,

```text
  Ω_A = Ω_{A/A^p}.                                                                   (21.1.5.2)
```

**Corollary (21.1.6).**

<!-- label: 0_IV.21.1.6 -->

*Suppose that `B` is an `A`-algebra of finite type and that there exists an integer `s ≥ 0` such that `u(A) ⊃ B^{p^s}`.
If `Ω_{B/A} = 0`, then `u` is surjective.*

By `(21.1.5, (iii))`, `𝔍_{B/A}` is a nilideal; moreover, by `(20.4.4)` and the hypothesis, `𝔍_{B/A}` is an ideal of
finite type, so it is nilpotent; as the relation `Ω_{B/A} = 0` means that `𝔍_{B/A}^2 = 𝔍_{B/A}`, one concludes that
`𝔍_{B/A} = 0`, that is, that `π : B ⊗_A B → B` is bijective. Moreover, every element of `B` having its `p^s`-th power
in `u(A)`, `B` is integral over `A`, and being of finite type, it is a finite `A`-algebra. One is thus reduced to
proving the following lemma (in which the rings considered are not supposed of characteristic `p`):

**Lemma (21.1.6.1).**

<!-- label: 0_IV.21.1.6.1 -->

*Let `R` be a ring, `S` a finite `R`-algebra; if the canonical homomorphism `π : S ⊗_R S → S` is bijective, then the
structural homomorphism `u : R → S` is surjective.*

It suffices to show that for every maximal ideal `𝔪` of `R`, if one sets `T = R − 𝔪`, the homomorphism
`u_𝔪 : R_𝔪 → T^{-1} S` is surjective (Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1); now the hypothesis entails
that the homomorphism `(T^{-1} S) ⊗_{R_𝔪} (T^{-1} S) → T^{-1} S` is bijective `(0_I, 1.3.4)`, and since `T^{-1} S` is
a finite `R_𝔪`-algebra,

<!-- original page 251 -->

one sees that one can restrict to the case where `R` is a local ring. Denoting still by `𝔪` its maximal ideal, it
suffices to prove that `u ⊗ 1 : R/𝔪 → S/𝔪 S` is surjective, by Nakayama's lemma (`S` being an `R`-module of finite
type); as the canonical homomorphism `(S/𝔪 S) ⊗_{R/𝔪} (S/𝔪 S) → S/𝔪 S` is bijective and `S/𝔪 S` is a finite
`(R/𝔪)`-algebra, one is finally reduced to the case where `R` is a field; but then the ranks of `S ⊗_R S` and of `S`
over `R` can only be equal if `S` is of rank `0` or `1`, that is, if `u : R → S` is surjective.

**Proposition (21.1.7).**

<!-- label: 0_IV.21.1.7 -->

*Let `A` be a ring, `B` an `A`-algebra, `(x_α)_{α ∈ I}` a family of elements of `B`. Consider the following properties:*

*a) `B = A[B^p, (x_α)]`, in other words the `A[B^p]`-algebra `B` is generated by the family `(x_α)_{α ∈ I}`.*

*b) The `A[B^p]`-module `B` is generated by the monomials `∏ x_α^{n(α)}`, where `(n(α))_{α ∈ I}` is a family of
integers of finite support such that `0 ≤ n(α) < p` for every `α ∈ I`.*

*c) The `B`-module `Ω_{B/A}` is generated by the `d_{B/A}(x_α)` `(α ∈ I)`.*

*Then properties a) and b) are equivalent and entail c); if moreover `B` is an `A[B^p]`-algebra of finite type, c) is
equivalent to a) and b).*

It is clear that b) entails a), and conversely a) entails b), for every monomial `∏_α x_α^{m(α)}`, where the `m(α)` are
integers `≥ 0` (forming a family of finite support), can be written `(∏_α x_α^{q(α)})^p · ∏_α x_α^{r(α)}`, by dividing
each `m(α)` by `p`, which gives `m(α) = p · q(α) + r(α)` with `0 ≤ r(α) < p`. The fact that a) entails c) follows from
`(21.1.5, (ii))` and from `(20.4.7)`. Conversely suppose c) verified and that `B` is an `A[B^p]`-algebra of finite
type; let `B'` be the sub-`A[B^p]`-algebra of `B` generated by the `x_α`; in the exact sequence `(20.5.7.1)`

```text
  Ω_{B'/A[B^p]} ⊗_{B'} B → Ω_{B/A[B^p]} → Ω_{B/B'} → 0
```

the hypothesis entails that the left arrow is surjective (taking account of `(21.1.5, (ii))`); one therefore has
`Ω_{B/B'} = 0`, and as `B^p ⊂ B' ⊂ B` and `B` is a `B'`-algebra of finite type, one necessarily has `B' = B` by
`(21.1.6)`.

**Remark (21.1.8).**

<!-- label: 0_IV.21.1.8 -->

*When `B` is a field, we shall prove the equivalence of properties a), b) and c) without hypothesis of finiteness
`(21.4.5)`.*

**Definition (21.1.9).**

<!-- label: 0_IV.21.1.9 -->

*Let `A` be a ring (of characteristic `p`), `B` an `A`-algebra. One says that a family `(x_α)_{α ∈ I}` of elements of
`B` is **`p`-free over `A`** (resp. a **system of `p`-generators of `B` over `A`**, resp. a **`p`-basis of `B` over
`A`**) if the family of monomials `∏_α x_α^{n(α)}` (`0 ≤ n(α) < p`, `(n(α))_{α ∈ I}` of finite support) is a free
family (resp. a system of generators, resp. a basis) in the `A[B^p]`-module `B`.*

One has corresponding definitions for a set `M` of elements of `B`, by considering the family defined by the canonical
injection `M → B`. When one takes for `A` the prime field `𝔽_p` (in which case `A[B^p] = B^p`), one omits the mention of
`A` in the preceding definition (or one says further that a family is "absolutely" `p`-free, resp. an "absolute" system
of `p`-generators, resp. an "absolute" `p`-basis).

<!-- original page 252 -->

It is clear that the notions defined in `(21.1.9)` do not change when one replaces `A` therein by the subring `A[B^p]`
of `B`; in other words one can always suppose that one has `B^p ⊂ A ⊂ B`.

If `M` is a `p`-free part of `B` over `A`, it is clear that every subset of `M` is `p`-free over `A`. Moreover:

**Lemma (21.1.10).**

<!-- label: 0_IV.21.1.10 -->

*Let `C` be a sub-`A`-algebra of `B` such that `B^p ⊂ C`, `M` a subset of `C`, `N` a subset of `B`.*

*(i) If `M` is a system of `p`-generators of `C` over `A` and `N` a system of `p`-generators of `B` over `C`, then
`M ∪ N` is a system of `p`-generators of `B` over `A`.*

*(ii) Suppose that `M` is a `p`-basis of `C` over `A`; then, for `N` to be `p`-free over `C`, it is necessary and
sufficient that `M ∪ N` be `p`-free over `A`.*

One can restrict to the case where `B^p ⊂ A ⊂ C ⊂ B`. Then (i) is a particular case of the fact that if `P` (resp.
`Q`) is a system of generators of the `A`-module `C` (resp. of the `C`-module `B`), the set of `xy`, where `x ∈ P` and
`y ∈ Q`, is a system of generators of the `A`-module `B`. Keeping the same notation, if `P` is a basis of the
`A`-module `C`, saying that `Q` is a free family over `C` means that the relation `∑_{λ, μ} a_{λμ} x_λ y_μ = 0`, where
`a_{λμ} ∈ A`, `x_λ ∈ P`, `y_μ ∈ Q` (the `x_λ` (resp. `y_μ`) being pairwise distinct), is equivalent to
`∑_λ a_{λμ} x_λ = 0` for every `μ`, or again to `a_{λμ} = 0` for every pair `(λ, μ)`; whence assertion (ii).

### 21.2. `p`-bases and formal smoothness

**Theorem (21.2.1).**

<!-- label: 0_IV.21.2.1 -->

*Let `B` be a ring, `A` a subring of `B` such that `B^p ⊂ A ⊂ B`, `(x_α)_{α ∈ I}` a `p`-basis of `B` over `A`. Let `E`
be an `A`-algebra, `u : A → E` the structural homomorphism, `q : E → B` a surjective `A`-homomorphism, `𝔎` its kernel,
and suppose that `𝔎^2 = 0`. Then:*

*(i) For there to exist an `A`-homomorphism `v : B → E` right inverse to the homomorphism `q : E → B`, it is necessary
and sufficient that one have `u(q(z)^p) = z^p` for every `z ∈ E`.*

*(ii) When the condition of (i) is satisfied, for every family `(z_α)_{α ∈ I}` of elements of `E` such that
`q(z_α) = x_α` for every `α ∈ I`, there exists one and only one `A`-homomorphism `v : B → E` such that `v(x_α) = z_α`
for every `α ∈ I`, and `v` is right inverse to `q`.*

If there exists an `A`-homomorphism `v : B → E`, one must have `v(a) = u(a)` for every `a ∈ A ⊂ B`, hence
`v(q(z)^p) = u(q(z)^p)` for every `z ∈ E`, since `B^p ⊂ A`. But one has `v(q(z)^p) = (v(q(z)))^p` and by definition
`v(q(z)) ≡ z (mod 𝔎)` if `q ∘ v = 1_B`, hence `(v(q(z)))^p = z^p` since `𝔎^2 = 0`; whence the necessity of (i). The
sufficiency of condition (i) will follow from (ii). Now, under the hypotheses of (ii), the uniqueness of `v` is
evident since the monomials `∏_α x_α^{n(α)}`

<!-- original page 253 -->

generate the `A`-module `B`; as these monomials moreover form a basis of the `A`-module `B`, there exists an
`A`-linear map `v` of `B` into `E` such that `v(∏_α x_α^{n(α)}) = ∏_α z_α^{n(α)}` for every family
`(n(α))_{α ∈ I}` of finite support with `0 ≤ n(α) < p` for every `α`. It remains to see that `v` is a ring
homomorphism. Now, one can write `(∏_α x_α^{m(α)})(∏_α x_α^{n(α)}) = a · ∏_α x_α^{r(α)}`, where
`r(α) = m(α) + n(α)` if `m(α) + n(α) < p`, `r(α) = m(α) + n(α) − p` in the contrary case, and `a ∈ A` is the product
of the `x_α^p` for those `α ∈ I` such that `m(α) + n(α) ≥ p`; we have to see that
`u(a) = ∏_α z_α^p` (the product over the same set of `α`); but as `x_α^p = q(z_α)^p`, this follows from the
hypothesis. Q.E.D.

**Corollary (21.2.2).**

<!-- label: 0_IV.21.2.2 -->

*Let `B` be a ring, `A` a subring of `B` such that `B^p ⊂ A ⊂ B`. If there exists a `p`-basis of `B` over `A`, `B` is
an `A`-algebra formally smooth relative to `B^p` (for the discrete topologies).*

In fact, let `E` be an `A`-extension of `B` by a `B`-module `L`, `q : E → B` the augmentation, `u : A → E` the
structural homomorphism. Saying that `E` is `B^p`-trivial means that there exists a ring homomorphism `v : B → E` such
that `q(v(b)) = b` and `v(b^p) = u(b^p)` for every `b ∈ B`. One deduces from this that, for `z ∈ E`, one has
`u(q(z)^p) = v(q(z)^p) = (v(q(z)))^p`; but by virtue of the relation `L^2 = 0`, one has `𝔎^2 = 0`, and as
`v(q(z)) − z ∈ L`, one has `(v(q(z)))^p = z^p`; the condition of `(21.2.1, (i))` is therefore satisfied, and `E` is
`B`-trivial.

**Corollary (21.2.3).**

<!-- label: 0_IV.21.2.3 -->

*Let `B` be a ring, `A` a subring of `B` such that `B^p ⊂ A ⊂ B`, and `(x_α)_{α ∈ I}` a `p`-basis of `B` over `A`. Let
`L` be a `B`-module. Then:*

*(i) For a derivation `D` of `A` into `L` to extend to a derivation of `B` into `L`, it is necessary and sufficient
that `D` vanish on `B^p`.*

*(ii) If `D` vanishes on `B^p`, then, for every family `(y_α)_{α ∈ I}` of elements of `L`, there exists one and only
one derivation `D'` of `B` into `L` extending `D` and such that `D'(x_α) = y_α` for every `α ∈ I`.*

Given a derivation `D` of `A` into `L`, consider the ring `E = D_B(L)` and the homomorphism `u : A → E` defined by
`u(a) = (a, D(a))`; an `A`-homomorphism `v : B → E` right inverse to the canonical homomorphism `q : E → B` is then of
the form `x ↦ (x, D'(x))`, where `D'` is a derivation of `B` into `L` extending `D` `(20.1.5)`; as
`u(q(z)^p) = (q(z)^p, p q(z)^{p-1} D'(q(z)))` for `z ∈ E`, the corollary follows immediately from `(21.2.1)` applied to
`E`.

It follows from `(21.2.3)` that the sequence

```text
  0 → Der_A(B, L) → Der_{B^p}(B, L) → Der_{B^p}(A, L) → 0                            (21.2.3.1)
```

(cf. `(20.2.2.1)`) is exact, and that the map

```text
  D' ↦ (D'(x_α))_{α ∈ I}                                                             (21.2.3.2)
```

is an isomorphism of the `B`-module `Der_A(B, L)` onto the `B`-module product `L^I` (by taking `D = 0` in `(21.2.3)`).

**Corollary (21.2.4).**

<!-- label: 0_IV.21.2.4 -->

*Under the hypotheses of `(21.2.3)`, the sequence*

```text
  0 → Ω_{A/B^p} ⊗_A B → Ω_{B/B^p} → Ω_{B/A} → 0                                      (21.2.4.1)
```

*is exact and split, and the family `(d_{B/A}(x_α))_{α ∈ I}` is a basis of the `B`-module `Ω_{B/A}`.*

This follows at once from `(21.2.3)` and from the formula `Der_A(B, L) = Hom_B(Ω_{B/A}, L)` `(20.4.8)`.

**Corollary (21.2.5).**

<!-- label: 0_IV.21.2.5 -->

*Let `A` be a ring, `B` an `A`-algebra, `(x_α)_{α ∈ I}` a `p`-basis of `B` over `A`. Then `(d_{B/A}(x_α))_{α ∈ I}` is
a basis of the `B`-module `Ω_{B/A}`.*

Using `(21.1.5, (ii))`, one reduces to the case where `A = A[B^p]`, and it then suffices to apply `(21.2.4)`.

<!-- original page 254 -->

(21.2.6) Let `A`, `B` be two rings, `u : A → B` a ring homomorphism; one has (with the notation of `(21.1.4)`) a
commutative diagram

```text
  A^{[p]} —u^{[p]}→ B^{[p]}
    │                │
    F_A              F_B                                                             (21.2.6.1)
    │                │
    ↓                ↓
    A   ———u———→    B.
```

One therefore deduces canonically a homomorphism of `B`-algebras

```text
  u ⊗ 1 : A^{[p]} ⊗_A B → B^{[p]}                                                    (21.2.6.2)
```

whose image is the ring `A[B^p]` (which is a `B`-algebra by the homomorphism `F_B : B → B^{[p]}`).

**Theorem (21.2.7).**

<!-- label: 0_IV.21.2.7 -->

*Let `A` be a ring, `B` an `A`-algebra, `u : A → B` the structural homomorphism. Suppose verified the following
conditions:*

*(i) The homomorphism `(21.2.6.2)` deduced from `u` is injective.*

*(ii) `B` admits a `p`-basis `(x_α)_{α ∈ I}` relative to `A`.*

*Then `B` is an `A`-algebra formally smooth (for the discrete topologies). More precisely, equip `A` and `B` with the
discrete topologies; let `E` be an admissible topological `A`-algebra `(0_I, 7.1.2)`, `𝔎` an ideal of definition of
`E`, `C = E/𝔎`, `v : B → C` an `A`-homomorphism, `q : E → C` the augmentation. Then, for every family
`(z_α)_{α ∈ I}` of elements of `E` such that `v(x_α) = q(z_α)` for every `α ∈ I`, there exists one and only one
`A`-homomorphism `w : B → E` such that `v = q ∘ w` and `w(x_α) = z_α` for every `α ∈ I`.*

Consider first the case where `E` is discrete, hence `𝔎` nilpotent. One can restrict to the case where `v` is
surjective; moreover, the reasoning of `(19.4.3)` permits supposing `𝔎^2 = 0` and consequently `𝔎^2 = 0`. Finally, by
considering the inverse image by `v` of the extension `E` of `C` by `𝔎`, one can restrict to the case where `C = B`
and `v` is the identity `(19.4.4)`. Since the ring homomorphism `F_E : E → E` vanishes on `𝔎`, it factors as
`E → B → E`, and `F'`, considered as homomorphism of `B` into `E^{[p]}`, is an `A`-homomorphism by definition of the
`A`-algebra structure of `E^{[p]}` by means of the composite homomorphism `A → E → E^{[p]}`, where `r : A → E` is the
structural homomorphism of the `A`-algebra `E`; moreover `r : A^{[p]} → E^{[p]}` is also an `A`-homomorphism. There
is therefore a unique `A`-homomorphism `f : A^{[p]} ⊗_A B → E^{[p]}` such that the composites of `f` with the canonical
homomorphisms `A^{[p]} → A^{[p]} ⊗_A B` and `B → A^{[p]} ⊗_A B` are respectively `r` and `F'`. Now, by hypothesis, one
can identify `A^{[p]} ⊗_A B` with `A[B^p]`, the canonical homomorphisms `A^{[p]} → A^{[p]} ⊗_A B` and
`B → A^{[p]} ⊗_A B` identifying respectively with `u` and `F_B`. One can therefore now consider `E` as an
`A[B^p]`-algebra by means of the homomorphism `f`, and, by construction, one has `f(q(z)^p) = z^p` for every `z ∈ E`;
one is thus in the conditions of application of `(21.2.1)`, whence the theorem in this case.

To pass to the general case, consider a fundamental system `(𝔍_λ)` of open ideals of `E`, and set `E_λ = E/𝔍_λ`,
`𝔎_λ = (𝔎 + 𝔍_λ)/𝔍_λ`, `C_λ = E_λ/𝔎_λ = E/(𝔎 + 𝔍_λ)`; as `E` is admissible, one has `E = lim E_λ` `(0_I, 7.2.2)`. For
every pair `(α, λ)`, denote by `z_{α, λ}` the canonical image of `z_α` in `E_λ`, by `p_λ : C → C_λ` the canonical
homomorphism,

<!-- original page 255 -->

by `q_λ` the canonical homomorphism `E_λ → C_λ`. As by hypothesis `𝔎_λ` is nilpotent in `E_λ`, the first part of the
proof proves the existence and uniqueness of an `A`-homomorphism `w_λ : B → E_λ` such that `p_λ ∘ v = q_λ ∘ w_λ` and
`w_λ(x_α) = z_{α, λ}` for every `α`. The uniqueness of the `w_λ` then shows immediately that `(w_λ)` is a projective
system of homomorphisms, and `w = lim w_λ` answers the question.

**Remark (21.2.8).**

<!-- label: 0_IV.21.2.8 -->

*The verification of the existence and uniqueness of the homomorphism `w : B → E` such that `w(x_α) = z_α` for every
`α` can be deduced directly from the fact that `B` is an `A`-algebra formally smooth and from the fact that the
`d_{B/A}(x_α)` form a basis of the `B`-module `Ω_{B/A}` `(21.2.4)`, without bringing in the fact that one deals with a
`p`-basis (so that the result is valid without supposing the rings of characteristic `p`).*

In fact, one can restrict to the case where `𝔎^2 = 0`; as `Der_A(B, 𝔎) = Hom_B(Ω_{B/A}, 𝔎)` by `(20.4.8)`, there
exists one and only one `A`-derivation `D` of `B` into `𝔎` such that `D(x_α) = t_α` for every family `(t_α)` of
elements of `𝔎`; the conclusion follows from `(20.1.1)`.

### 21.3. `p`-bases and imperfection modules

(21.3.1) Let `A`, `B` be two rings (of characteristic `p`), `i : A → B`, `j : B → A` two ring homomorphisms such that
one has

```text
  j(i(a)) = a^p              for every a ∈ A,                                        (21.3.1.1)
  i(j(b)) = b^p              for every b ∈ B.                                        (21.3.1.2)
```

Most often, `i` will be injective, so that `A` will be identified by `i : A → B` to a subring of `B`; once this
identification is made, the existence of `j` implies that `B^p ⊂ A`, and `j` is then identified with `F_B`.

(21.3.2) If `h : A^p → A` is the canonical injection, one has, by `(21.3.1.1)`, a commutative diagram

```text
  B ——j——→ A
  │         │
  i         h                                                                        (21.3.2.1)
  │         │
  ↓         ↓
  A ——F_A→ A^p
```

so that the pair `(j, F_A)` may be considered as a di-homomorphism of the `A`-algebra `B` (for `i`) into the
`A^p`-algebra `A` (for `h`). One deduces a canonical homomorphism of `A`-modules

```text
  π_{B/A} : Ω_{B/A} ⊗_{B, j} A → Ω_A = Ω^1_A                                         (21.3.2.2)
```

(cf. `(20.5.4)`; the identification of `Ω^1_{A/A^p}` and of the module of absolute differentials `Ω^1_A` comes from
`(21.1.5, (ii))`).

One sets

```text
  Θ_{B/A} = Ω_{B/A} ⊗_{B, j} A                                                       (21.3.2.3)
  Ξ_{B/A} = Ker(π_{B/A})                                                             (21.3.2.4)
```

<!-- original page 256 -->

so that one has the exact sequence

```text
  0 → Ξ_{B/A} → Θ_{B/A} → Ω^1_A                                                      (21.3.2.5)
```

(one notes that this notation may lead to confusion since `Θ_{B/A}` and `π_{B/A}` depend not only on `A` and `B`, but
also on `i` and `j`).

(21.3.3) Since by `(21.3.1.2)`, one has `F_B = i ∘ j`, one can write for every `B`-module `M` (cf. `(21.1.4)`)

```text
  M^{[p]} = M ⊗_B B = (M ⊗_B A) ⊗_A B                                                (21.3.3.1)
```

whence in particular

```text
  (Ω_{B/A})^{[p]} = Θ_{B/A} ⊗_A B                                                    (21.3.3.2)
```

and one deduces from `(21.3.2.2)` a canonical homomorphism of `B`-modules

```text
  ω_{B/A} : (Ω_{B/A})^{[p]} → Ω^1_A ⊗_A B.                                           (21.3.3.3)
```

Taking account of `(20.5.4.2)`, the image of this homomorphism is the `B`-module generated by the elements
`d_A(j(b)) ⊗ 1` for `b ∈ B`. Their image by the canonical homomorphism `i_{B/A} : Ω^1_A ⊗_A B → Ω^1_B` deduced from `i`
`(20.5.2)` is therefore in the sub-`B`-module of `Ω^1_B` generated by the `d_B(i(j(b)))` for `b ∈ B`; by virtue of
`(21.3.1.2)`, this image is zero. In other words, one has a sequence of homomorphisms

```text
  0 → Ξ_{B/A} ⊗_A B → (Ω_{B/A})^{[p]} → Υ_{B/A}                                      (21.3.3.4)
```

which is not necessarily exact, but in which the composite of two consecutive homomorphisms is zero.

**Proposition (21.3.4).**

<!-- label: 0_IV.21.3.4 -->

*If `B` is an `A`-module flat (for `i`), the sequence `(21.3.3.4)` is exact.*

This follows from the definition of flatness.

Proposition `(21.3.4)` applies in particular when one has `B^p ⊂ A ⊂ B`, `i` and `j` being respectively the canonical
injection and `F_B`, and `B` admits a `p`-basis over `A` (so that `B` is then a free `A`-module). But even in this
case the kernel `Ξ_{B/A}` is not necessarily zero. Nevertheless:

**Proposition (21.3.5).**

<!-- label: 0_IV.21.3.5 -->

*Let `B` be a reduced ring, `A` a subring of `B` such that `B^p ⊂ A ⊂ B`. Suppose there exists a `p`-basis
`(x_λ)_{λ ∈ L}` of `B` over `A` and a `p`-basis `(y_μ)_{μ ∈ M}` of `A` over `A^p`; then the canonical homomorphism
`(21.3.3.4)`*

```text
  (Ω_{B/A})^{[p]} → Υ_{B/A}                                                          (21.3.5.1)
```

*is bijective, and the elements `d_B(x_λ) ⊗ 1` form a basis of the `B`-module `Υ_{B/A}`.*

Since `B` is reduced, `x ↦ x^p` is an isomorphism of `B` onto `B^p`, and by transport of structure by means of this
isomorphism, one sees that `(x_λ^p)_{λ ∈ L}` is a `p`-basis of `B^p` over `A^p`; one concludes that the `x_λ^p` and
the `y_μ` form a `p`-basis of `A` over `A^p` `(21.1.10)`; consequently `(21.1.5, (ii) and 21.2.5)` the
`d_A(x_λ^p)` and the `d_A(y_μ)` form a basis of the `A`-module `Ω^1_A`; hence the `d_A(x_λ^p) ⊗ 1` and
`d_A(y_μ) ⊗ 1` form a basis of the `B`-module `Ω^1_A ⊗_A B`. Now, the image of `d_A(x_λ^p) ⊗ 1` by `i_{B/A}` is
`d_B(x_λ^p) = 0`; on the other hand, the image of `d_A(y_μ) ⊗ 1` by `i_{B/A}`

<!-- original page 257 -->

is `d_B(y_μ)`, and as the `y_μ` and the `x_λ` form a `p`-basis of `B` over `B^p` `(21.1.10)`, the `d_B(y_μ)` are
linearly independent (over `B`) in `Ω^1_B` `(21.2.5)`; one deduces at once that the kernel of `i_{B/A}` has a basis
formed of the `d_A(x_λ^p) ⊗ 1`; as these are the images by `(21.3.5.1)` of the elements `d_B(x_λ) ⊗ 1` in
`Ω_{B/A} ⊗_B B^{[p]}`, and as the latter form a basis of the `B`-module `Ω_{B/A} ⊗_B B^{[p]}` `(21.2.5)`, the
homomorphism `(21.3.5.1)` of `B`-modules is bijective.

**Remarks (21.3.6).**

<!-- label: 0_IV.21.3.6 -->

*(i) Let `A'`, `B'` be two rings of characteristic `p`, and suppose one has two homomorphisms `i' : A' → B'`,
`j' : B' → A'` verifying `(21.3.1.1)` and `(21.3.1.2)`, and ring homomorphisms `f : A → A'`, `g : B → B'` making the
diagram*

```text
  A'  ——i'——→ B'  ——j'——→ A'
  ↑           ↑           ↑
  f           g           f
  │           │           │
  A   ——i——→  B   ——j——→  A
```

*commute. Then the canonical homomorphism `Ω_{B/A} → Ω_{B'/A'}` `(20.5.4.3)` gives a canonical di-homomorphism
`Θ_{B/A} → Θ_{B'/A'}` making the diagram*

```text
                            π_{B/A}
  0 ——→  Ξ_{B/A}   ——→  Θ_{B/A}   ———→  Ω^1_A
           ↓               ↓               ↓
  0 ——→ Ξ_{B'/A'}  ——→ Θ_{B'/A'} ———→ Ω^1_{A'}
                            π_{B'/A'}
```

*commute.*

*(ii) Let `A'` be any `A`-algebra, and set `B' = B ⊗_A A'`; then `i' = i ⊗ 1 : A' → B'` and `j' = j ⊗ 1 : B' → A'`
verify `(21.3.1.1)` and `(21.3.1.2)`, and one has*

```text
  Ω_{B'/A'} = Ω_{B/A} ⊗_A A' = Ω_{B/A} ⊗_B B'
```

*`(20.5.5)`; one deduces a canonical `A'`-isomorphism*

```text
  Θ_{B/A} ⊗_A A' ⥲ Θ_{B'/A'}                                                         (21.3.6.1)
```

*and also a canonical `B'`-homomorphism*

```text
  Υ_{B/A} ⊗_A A' → Υ_{B'/A'}.                                                        (21.3.6.2)
```

### 21.4. Case of field extensions

(21.4.0) Let `K` be a field of characteristic `p > 0`, `k` a subfield of `K`; then the ring `k[K^p]` is equal to the
field `k(K^p)` since `k` is algebraic over `K^p`. One can therefore apply the results of the preceding numbers by
replacing throughout `A`, `B` and `A[B^p]` by `k`, `K` and `k(K^p)`.

**Lemma (21.4.1).**

<!-- label: 0_IV.21.4.1 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`. For an element `x ∈ K` to be `p`-free over `k`,
it is necessary and sufficient that `x ∉ k(K^p)`.*

<!-- original page 258 -->

In fact, `x` is a root of the polynomial `X^p − x^p` of `k(K^p)[X]`, and one knows (Bourbaki, Alg., chap. V, §8, n° 1,
prop. 1) that if `x ∉ k(K^p)`, this polynomial is irreducible, so that the elements `1, x, …, x^{p-1}` form a basis of
the `k(K^p)`-module `k(K^p)(x)`.

**Theorem (21.4.2).**

<!-- label: 0_IV.21.4.2 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`, `S` a system of `p`-generators of `K` over `k`,
`L ⊂ S` a part `p`-free over `k`. Then there exists a `p`-basis `B` of `K` over `k` such that `L ⊂ B ⊂ S`. In
particular, every extension of `k` admits a `p`-basis over `k`.*

One can restrict to the case where `K^p ⊂ k`. By Zorn's theorem, there exists in `K` a subset `B` such that
`L ⊂ B ⊂ S`, `p`-free over `k` and maximal among the subsets of `S` having these properties. It suffices to see that
the subfield `K'` of `K` generated by `k` and `B` is equal to `K`. In the contrary case, there would exist `x ∈ S` not
in `K'`; as `K^p ⊂ k`, one has `K' ⊃ k(K^p)`; hence `x` would be `p`-free over `K'` `(21.4.1)`, and consequently
`B ∪ {x}` would be `p`-free over `k` `(21.1.10)`, contrary to the definition of `B`. The last assertion of `(21.4.2)`
is obtained by taking `L = ∅`, `S = K`. Q.E.D.

**Corollary (21.4.3).**

<!-- label: 0_IV.21.4.3 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`. For a family `(x_α)` of elements of `K` to be
`p`-free over `k`, it is necessary and sufficient that, for every `α`, `x_α` not belong to the field `K_α` generated by
`k(K^p)` and by the `x_β` of index `β ≠ α`.*

The condition is necessary by `(21.1.10)`. Conversely, suppose it satisfied; one can restrict to the case where
`(x_α)` is a system of `p`-generators of `K`. There then exists a sub-family of `(x_α)` which is a `p`-basis of `K`
`(21.4.2)`, but this family cannot be distinct from `(x_α)`, otherwise, by the hypothesis, it would not be a family
of `p`-generators of `K`.

**Corollary (21.4.4).**

<!-- label: 0_IV.21.4.4 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`. For `Ω^1_{K/k} = 0`, it is necessary and
sufficient that `K = k(K^p)`. In particular, for `Ω^1_K = 0`, it is necessary and sufficient that `K` be a perfect
field.*

In fact, if `(x_α)` is a `p`-basis of `K` over `k`, the `d_K(x_α)` form a basis of the `K`-vector space `Ω^1_{K/k}`
`(21.2.5)`.

**Theorem (21.4.5).**

<!-- label: 0_IV.21.4.5 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`, `(x_α)` a family of elements of `K`. For
`(x_α)` to be `p`-free over `k` (resp. a family of `p`-generators of `K` over `k`, resp. a `p`-basis of `K` over `k`),
it is necessary and sufficient that the family `(d_{K/k}(x_α))` be a free family (resp. a system of generators, resp.
a basis) in the `K`-vector space `Ω^1_{K/k}`.*

Let `K'` be the subfield (equal to the subring) of `K` generated by `k(K^p)` and the `x_α`; taking account of
`(20.4.7)`, one sees that the `d_{K'/k}(x_α)` generate `Ω^1_{K'/k} = Ω^1_{K'/k(K^p)}`. If the `d_{K/k}(x_α)` generate
`Ω^1_{K/k} = Ω^1_{K/k(K^p)}`, the left arrow in the exact sequence `(20.5.7.1)`

```text
  Ω^1_{K'/k(K^p)} ⊗_{K'} K → Ω^1_{K/k(K^p)} → Ω^1_{K/K'} → 0
```

is surjective, hence `Ω^1_{K/K'} = 0`, which implies `K' = K` by `(21.4.4)`.

If now `(x_α)` is a `p`-free family, it is a sub-family of a `p`-basis of `K` over `k` `(21.4.2)`, hence the
`d_K(x_α)` form part of a basis of the `K`-vector space `Ω^1_{K/k}` `(21.2.5)`, and are consequently linearly
independent over `K`. Conversely let us prove that if the `d_{K/k}(x_α)` are linearly independent over `K`, the
family `(x_α)` is `p`-free over `k`.

<!-- original page 259 -->

Taking account of `(21.4.3)`, it suffices to see that, for each `α`, `x_α` does not belong to `K_α`. Now, in the
exact sequence

```text
  Ω^1_{K_α/k(K^p)} ⊗_{K_α} K → Ω^1_{K/k(K^p)} → Ω^1_{K/K_α} → 0,
```

the images by the left arrow of the `d_{K/k}(x_β)` for `β ≠ α` are the `d_{K_α/k}(x_β)`, which therefore generate a
sub-vector space of `Ω^1_{K_α/k(K^p)}` not containing `d_{K/k}(x_α)`, and as this sub-vector space is the kernel of
the right arrow, one sees that `d_{K/K_α}(x_α) ≠ 0`, hence `x_α ∉ K_α`.

**Corollary (21.4.6).**

<!-- label: 0_IV.21.4.6 -->

*Let `k` be a field of characteristic `p > 0`, `K` an extension of `k`, `x` an element of `K`. The three following
conditions are equivalent:*

*a) `x ∉ k(K^p)`.*

*b) `d_{K/k}(x) ≠ 0`.*

*c) The element `x` is `p`-free over `k`.*

**Proposition (21.4.7).**

<!-- label: 0_IV.21.4.7 -->

*Let `L` be a field of characteristic `p > 0`, `K` a subfield of `L` such that `L^p ⊂ K ⊂ L`. Then the sequence of
`L`-vector spaces*

```text
  0 → Ω^1_{K/L^p} ⊗_K L → Ω^1_{L/L^p} → Ω^1_{L/K} → 0                                (21.4.7.1)
```

*is exact; in other words, one has `Υ_{L/K/L^p} = 0`.*

This is a particular case of `(21.2.4)`, taking account of `(21.4.2)`.

**Proposition (21.4.8).**

<!-- label: 0_IV.21.4.8 -->

*Under the hypotheses of `(21.4.7)`, the canonical homomorphism*

```text
  (Ω_{L/K})^{[p]} → Υ_{L/K}                                                          (21.4.8.1)
```

*is bijective; if `(x_α)` is a `p`-basis of `L` over `K`, the elements `d_L(x_α) ⊗ 1` form a basis of the `L`-vector
space `Υ_{L/K}`.*

This is a particular case of `(21.3.5)`.

### 21.5. Application: separability criteria

In this number and the two following, we no longer suppose that the rings considered are of characteristic `p > 0`.

(21.5.1) Note first that the criterion `(21.2.7)` permits proving a part of Cohen's theorem on separable extensions
`(19.6.1)`, namely that if `k` is of characteristic `p > 0` and if `K` is a separable extension of `k`, then `K` is an
`A`-algebra formally smooth. In fact, `K` admits a `p`-basis over `k` `(21.4.2)`, and on the other hand, it follows
from MacLane's criterion (Bourbaki, Alg., chap. V, §8, n° 2, prop. 3) that in an algebraic closure of `K`, `k^{1/p}`
and `K` are linearly disjoint over `k`, and consequently the canonical homomorphism `k^{1/p} ⊗_k K → k^{1/p}(K)` is
bijective, which is precisely condition (i) of `(21.2.7)`, after transport of structure by the isomorphism
`k^{1/p} ⥲ k`.

**Proposition (21.5.2) (MacLane).**

<!-- label: 0_IV.21.5.2 -->

*Let `A`, `B` be two complete discrete valuation rings, `𝔪`, `𝔫` their respective maximal ideals, `K = A/𝔪` and
`L = B/𝔫` their residue fields, `u : A → B` a homomorphism such that `B u(𝔪) = 𝔫`, `u_0 = u ⊗ 1 : K → L` the
corresponding homomorphism for residue fields. Consider the following conditions:*

*a) `L` is a separable extension of `K` (for `u_0`).*

*b) For every complete discrete valuation ring `B'` of maximal ideal `𝔫'` and residue field `L'`,*

<!-- original page 260 -->

*every homomorphism `u' : A → B'` such that `B' u'(𝔪) = 𝔫'`, and every `K`-isomorphism `σ : L → L'` (relative to `u_0`
and `u'_0 = u' ⊗ 1 : K → L'`), there exists an isomorphism `w : B → B'` such that `u' = w ∘ u` and that
`w_0 = w ⊗ 1` be equal to `σ`.*

*b') For every homomorphism `u' : A → B` such that `B u'(𝔪) = 𝔫` and such that `u'_0 = u' ⊗ 1 : K → L` be equal to
`u_0`, there exists an automorphism `w` of `B` such that `u' = w ∘ u` and that `w_0 = w ⊗ 1 : L → L` be the identity.*

*c) Denoting by `u_1 : A/𝔪^2 → B/𝔫^2` the homomorphism deduced from `u` by passage to quotients, then, for every local
homomorphism `u'_1 : A/𝔪^2 → B/𝔫^2` such that `gr_0(u'_1) = gr_0(u_1) (= u_0)`, there exists an automorphism `w_1` of
`B/𝔫^2` such that `gr_0(w_1)` be the identity and that `u'_1 = w_1 ∘ u_1`.*

*c') For every local homomorphism `u'_1 : A/𝔪^2 → B/𝔫^2` such that `gr_0(u'_1) = gr_0(u_1)` and
`gr_1(u'_1) = gr_1(u_1)` (homomorphism of `𝔪/𝔪^2` into `𝔫/𝔫^2`), there exists an automorphism `w_1` of `B/𝔫^2` such
that `gr_0(w_1)` be the identity and that `u'_1 = w_1 ∘ u_1`.*

*Then one has the implications `c) ⇔ c') ⇔ a) ⇒ b) ⇒ b')`.*

*If moreover `A` is a Cohen ring, the five preceding conditions are equivalent.*

The implications `b) ⇒ b')` and `c) ⇒ c')` are trivial. Let us show that a) implies b). The homomorphism `u` makes
`B` an `A`-module without torsion, since it transforms by hypothesis a uniformizer of `A` into a uniformizer of `B`;
it follows that `B` is a flat `A`-module `(0_I, 6.3.4)`, hence a Cohen `A`-algebra `(19.8.1)`; the fact that a)
implies b) is then a consequence of `(19.8.2, (i))` applied with `C = B'`, `𝔍 = 𝔫'`, `B'` being considered as
`A`-algebra for `u'` and the homomorphism `B → B'/𝔫'` being the composite `B → B/𝔫 → B'/𝔫'`, which is an
`A`-homomorphism by virtue of the hypothesis `u'_0 = σ ∘ u_0`. The same reasoning proves that a) entails c), by
taking this time `C = B/𝔫^2`, `𝔍 = 𝔫/𝔫^2`, `C` being considered as `A`-algebra for `u'_1`.

Let us prove in the second place that c') implies a). The two homomorphisms `u_1` and `u'_1` are such that
`u'_1 = u_1 + D`, where `D` is a derivation of `A/𝔪^2` into `𝔫/𝔫^2` `(20.1.1)`; moreover, the hypothesis
`gr_1(u'_1) = gr_1(u_1)` means that `D` vanishes on `𝔪/𝔪^2`, and can consequently be considered as a derivation of
`K = A/𝔪` into `𝔫/𝔫^2`, and `𝔫/𝔫^2` is identified (by choice of a uniformizer of `B`) with the `K`-module `L` (for
`u_0`). On the other hand, the conditions imposed on `w_1` entail that `gr_1(w_1)` is also the identity (since
`u_1(𝔪/𝔪^2)` generates `𝔫/𝔫^2`); `w_1` is therefore of the form `z ↦ z + D'(z)`, where `D'` is this time a derivation
of `B/𝔫^2` into the `(B/𝔫^2)`-module `𝔫/𝔫^2`; as `w_1` is the identity on `𝔫/𝔫^2`, `D'` can again (by the preceding
identification of `𝔫/𝔫^2` and of `L`) be considered as a derivation of `L` into `L`; finally, the relation
`u'_1 = w_1 ∘ u_1` means that `D'` extends `D`. Note on the other hand that every derivation `D` of `K` into `L`
corresponds to a homomorphism `u'_1` verifying the conditions of c') `(20.1.1)`; condition c') means therefore that
every derivation of `K` into `L` extends to a derivation of `L` into itself, that is to say `(20.6.5)` that `L` is
separable over `K`.

Let us prove finally that, when `A` is a Cohen ring, b') entails c'). Let us prove first that under the hypotheses of
c'), there exists a homomorphism `u' : A → B` which verifies the hypotheses of b') and, by passage to quotients,
yields `u'_1 : A/𝔪^2 → B/𝔫^2`. In fact, this follows from `(19.8.6, (i))` applied to the composite homomorphism
`v' : A → A/𝔪^2 → B/𝔫^2`;

<!-- original page 261 -->

this last factors as `A → B → B/𝔫^2` and the hypotheses on `gr_0(u'_1)` and `gr_1(u'_1)` entail
`gr_0(u') = gr_0(u) = u_0` and `gr_1(u') = gr_1(u)`, hence the image by `u'` of a uniformizer of `A` is a uniformizer
of `B`, and one has consequently `B u'(𝔪) = 𝔫`. It then suffices, in order to obtain an automorphism `u'_1` answering
the question, to take the automorphism deduced by passage to quotients from the automorphism `w` of `B` furnished by
the application of b') to the homomorphism `u'`.

**Remarks (21.5.3).**

<!-- label: 0_IV.21.5.3 -->

*(i) The differential properties of fields permit solving the question of uniqueness of the field of
representatives in a complete Noetherian local ring `C` `(19.8.7, (ii))`. Let in fact `𝔍` be the maximal ideal of
`C`, `K = C/𝔍` the residue field of `C`; one can restrict to the case `𝔍 ≠ 0`. Suppose there exists a homomorphism
`u : K → C` which, composed with the augmentation `C → K`, yields the identity; then, for this homomorphism to be
unique, it is necessary and sufficient that `Ω^1_K = 0`. In fact, the condition `Ω^1_K = 0` entails that `K` is
formally unramified over its prime field `(20.7.4)`; if there existed a second homomorphism `v ≠ u` answering the
question, there would be a greatest integer `n` such that `𝔍^n` contains the set of `u(x) − v(x)` for `x ∈ K`; by
passage to quotient, `u` and `v` would yield two distinct homomorphisms `u', v'` of `K` into `C/𝔍^{n+1}`, whose
composites with `C/𝔍^{n+1} → C/𝔍^n` would be equal, which contradicts the definition `(19.10.2)`. Conversely,
suppose `Ω^1_K ≠ 0`; there then exists a derivation `D ≠ 0` of `K` into `𝔍/𝔍^2` `(20.4.8)`, hence a homomorphism
`v_1 : K → C/𝔍^2` such that, if `u_1 : K → C/𝔍^2` is obtained by passage to quotient from `u`, one has
`v_1 = u_1 + D` `(20.1.1)`. If `k` is the prime field of `K`, `C` is a `k`-algebra and `K` a `k`-algebra formally
smooth `(19.6.1)`, and the restrictions of `u_1` and `v_1` to `k` coincide, hence `v_1` factors as `K → C → C/𝔍^2`
and one has `v ≠ u`.*

*Let us recall (`(20.6.20)` and `(21.4.4)`) that the condition `Ω^1_K = 0` means that `K` is perfect if it is of
characteristic `≠ 0`, and an algebraic extension of `ℚ` if it is of characteristic `0`.*

*(ii) In the same manner, let `W` be a Cohen ring, `C` a complete Noetherian local ring, `𝔍 ≠ 0` an ideal of `C`
contained in the maximal ideal; for the factorization `W → C → C/𝔍` in `(19.8.6, (i))` to be unique, it is necessary
and sufficient that the residue field `K` of the Cohen ring `W` satisfy `Ω^1_K = 0`. In fact, if `Ω^1_K ≠ 0` and if
`𝔪` denotes the maximal ideal of `W`, it suffices to compose a derivation `D ≠ 0` of `K` into `𝔍/𝔪 𝔍` with the
augmentation `W → K` to obtain a derivation `D' ≠ 0` of `W` into `𝔍/𝔪 𝔍`, and one finishes the reasoning as in (i) by
forming with the aid of `D'` a homomorphism `v_1 : W → C/𝔪 𝔍` distinct from the homomorphism `u_1 : W → C/𝔪 𝔍`
deduced from `u` by passage to quotient; one completes the reasoning by invoking this time `(19.8.6, (i))`. If on the
contrary `Ω^1_K = 0`, the uniqueness of `v` follows already from (i) when `W = K` is a field of characteristic `0`.
In the contrary case, one has `Ω^1_W = 0`; in fact, one then has `𝔪 = pW`, `p` being the characteristic of `K`
`(19.8.5)`, and the canonical homomorphism `𝔪/𝔪^2 → Ω^1_W/𝔪 Ω^1_W` `(20.5.11.2)` is consequently zero. The exact
sequence `(20.5.12.1)` applied to `W` and to `K = W/𝔪` then entails that `Ω^1_W = 𝔪 Ω^1_W`, whence our assertion. But
then `(20.7.4)` `W` is formally unramified (for its adic topology) over `ℤ`, and the uniqueness of `v` is proved as in
(i).*

<!-- original page 262 -->

### 21.6. Admissible fields for an extension

(21.6.1) Given four fields `k_0 ⊂ k ⊂ K ⊂ L`, it follows from `(20.6.16)` and `(20.6.17)` that one has an exact
sequence

```text
  0 → Υ_{K/k/k_0} ⊗_K L → Υ_{L/k/k_0} → Υ_{L/K/k_0} → Υ_{L/K/k} → 0.                  (21.6.1.1)
```

When one keeps `k_0`, `K` and `L` fixed and one lets the intermediate field `k` between `k_0` and `K` "vary", one
evidently has `Υ_{L/K/k_0} = Υ_{L/K/k}` when `k = k_0`. When the canonical homomorphism `s` of `(21.6.1.1)` is again
bijective, one says that `k` is a `k_0`-**admissible** field for the extension `L` of `K`. The interest of the
existence, under certain conditions, of such fields `k`, which are nevertheless "sufficiently close" to `K` (for
example such that `[K : k]` be finite) is that they permit replacing in certain questions the differential modules
`Ω^1_{K/k_0}` and `Ω^1_{L/k_0}` (which may be "too large", for example when `k_0` is the prime field) by `Ω^1_{K/k}`
and `Ω^1_{L/k}`, more easily handled.

When `k_0` is the prime field, one will say "admissible field" instead of "`k_0`-admissible field".

One sets

```text
  Δ(L/K, k/k_0) = Coker(Υ_{K/k/k_0} ⊗_K L → Υ_{L/k/k_0}) ≅ Ker(Υ_{L/K/k_0} → Υ_{L/K/k})  (21.6.1.2)
```

(vector space over `L`); its rank will be denoted `d(L/K, k/k_0)` and called the **`k_0`-admissibility defect** of `k`
for the extension `L` of `K` (it is evidently zero if and only if `k` is `k_0`-admissible for this extension). When
`k_0` is the prime field, one writes `Δ(L/K, k)` and `d(L/K, k)` instead of `Δ(L/K, k/k_0)` and `d(L/K, k/k_0)`.

**Proposition (21.6.2).**

<!-- label: 0_IV.21.6.2 -->

*Let `k_0 ⊂ k ⊂ K ⊂ L` be four fields.*

*(i) The following conditions are equivalent:*

*a) The field `k` is `k_0`-admissible for the extension `L` of `K` (in other words, the homomorphism
`Υ_{L/K/k_0} → Υ_{L/K/k}` is injective, hence bijective).*

*b) The canonical homomorphism `u : Υ_{K/k_0} → Υ_{K/k}` is zero.*

*c) The canonical homomorphism `v : Ω^1_{K/k} ⊗_K L → Υ_{L/k}` is surjective (hence bijective).*

*d) One has `d(L/K, k/k_0) = 0` (or `Δ(L/K, k/k_0) = 0`).*

*(ii) The equivalent conditions of (i) are verified when one is in one of the following cases: α) `L` is separable
over `k`; β) `L` is separable over `K`; γ) one has `k ⊂ k_0(K^p)`, denoting by `p` the characteristic exponent of
`k_0`.*

(i) The assertions follow trivially from the exactness of the sequence `(21.6.1.1)`.

(ii) If `L` is separable over `k`, one has `Υ_{L/k_0} = 0` `(20.6.19)`, hence condition b) of (i) is satisfied; if
`L` is separable over `K`, one has `Υ_{L/K/k_0} = 0` `(20.6.19)`, hence condition a) of (i) is satisfied; finally, if
one has `k ⊂ k_0(K^p)`, it follows that `Ω^1_{K/k_0} = Ω^1_{K/k}` by virtue of `(21.1.5.1)`, and condition a) of (i) is
verified.

<!-- original page 263 -->

(21.6.3) Suppose that one has a commutative diagram of field monomorphisms

```text
  k'_0 ——→ k' ——→ K' ——→ L'
   ↑       ↑       ↑      ↑
   │       │       │      │
   k_0 ——→  k ——→  K ——→  L.
```

It follows then from `(20.6.17, (ii))` that one has a canonical homomorphism

```text
  Δ(L/K, k/k_0) → Δ(L'/K', k'/k'_0)                                                  (21.6.3.1)
```

with an evident transitivity property, so that one can say that `Δ(L/K, k/k_0)` is a functor in the quadruple
`(k_0, k, K, L)`.

**Proposition (21.6.4).**

<!-- label: 0_IV.21.6.4 -->

*(i) Let `k ⊂ k' ⊂ k'' ⊂ K ⊂ L` be five fields. One has an exact sequence of canonical homomorphisms*

```text
  0 → Δ(L/K, k'/k) → Δ(L/K, k''/k) → Δ(L/K, k''/k') → 0                              (21.6.4.1)
```

*and consequently the equality*

```text
  d(L/K, k''/k) = d(L/K, k''/k') + d(L/K, k'/k).                                     (21.6.4.2)
```

*(ii) Let `k_0 ⊂ k ⊂ K ⊂ L ⊂ M` be five fields. One has an exact sequence of canonical homomorphisms*

```text
  0 → Δ(L/K, k/k_0) ⊗_L M → Δ(M/K, k/k_0) → Δ(M/L, k/k_0) → 0                        (21.6.4.3)
```

*and consequently the equality*

```text
  d(M/K, k/k_0) = d(M/L, k/k_0) + d(L/K, k/k_0).                                     (21.6.4.4)
```

(i) Consider the commutative diagram

```text
  0 → Υ_{K/k'/k} ⊗_K L → Υ_{K/k''/k} ⊗_K L → Υ_{K/k''/k'} ⊗_K L → 0
            ↓                   ↓                   ↓
  0 →   Υ_{L/k'/k}    →   Υ_{L/k''/k}    →   Υ_{L/k''/k'}    → 0
            ↓                   ↓                   ↓
  0 → Δ(L/K, k'/k)    →  Δ(L/K, k''/k)   →  Δ(L/K, k''/k')   → 0
```

where one may consider the three rows as complexes `T'_1, T_2, T'_3` respectively;

<!-- original page 264 -->

the exact sequence `(21.6.1.1)` and the definition of `Δ` `(21.6.1.2)` show that one has an exact sequence of
complexes `0 → T'_1 → T_2 → T'_3 → 0`; let us apply to it the long exact sequence of cohomology, and let us note that,
by virtue of the exactness of `(21.6.1.1)`, the cohomology of `T'_1` and that of `T_2` are zero except in a single
and the same degree, for which the cohomology modules are both equal to `Υ_{L/K/k} ⊗_K L`; as `T'_1` and `T_2` have
thus the same cohomology, that of `T'_3` is necessarily zero, which proves (i).

(ii) Consider similarly the commutative diagram

```text
  0 → Δ(L/K, k/k_0) ⊗_L M → Δ(M/K, k/k_0)   → Δ(M/L, k/k_0)   → 0
            ↓                   ↓                   ↓
        Υ_{L/K/k_0} ⊗_L M  →  Υ_{M/K/k_0}    →  Υ_{M/L/k_0}
            ↓                   ↓                   ↓
        Υ_{L/K/k} ⊗_L M    →  Υ_{M/K/k}      →  Υ_{M/L/k}
```

where again one considers the three rows as complexes `T''_1`, `T_2`, `T''_3`; the exact sequence `(21.6.1.1)` and
the definition of `Δ` `(21.6.1.2)` give here an exact sequence of complexes
`0 → T''_1 → T_2 → T''_3 → 0` to which one again applies the long exact sequence of cohomology; this time, by virtue
of the exactness of `(21.6.1.1)`, the cohomology of `T_2` and that of `T''_3` are zero except in a single and the
same degree, for which the cohomology modules are both equal to `Υ_{M/L/K}`; one concludes here that the cohomology
of `T''_1` is zero, which establishes (ii).

**Corollary (21.6.5).**

<!-- label: 0_IV.21.6.5 -->

*(i) Given five fields `k ⊂ k' ⊂ k'' ⊂ K ⊂ L`, for `k''` to be `k`-admissible for the extension `L` of `K`, it is
necessary and sufficient that `k'` be `k`-admissible and that `k''` be `k'`-admissible for the extension `L` of `K`.*

*(ii) Given five fields `k_0 ⊂ k ⊂ K ⊂ L ⊂ M`, for `k` to be `k_0`-admissible for the extension `M` of `K`, it is
necessary and sufficient that it be so for the extension `L` of `K` and for the extension `M` of `L`.*

This follows at once from the relations `(21.6.4.2)` and `(21.6.4.4)`, the values of `d` being `≥ 0`.

**Corollary (21.6.6).**

<!-- label: 0_IV.21.6.6 -->

*Let `k_0 ⊂ k ⊂ K ⊂ L` be four fields, and suppose that `k` is `k_0`-admissible for the extension `L` of `K`. Then, if
`k'_0, k', K', L'` are four fields such that `k_0 ⊂ k'_0 ⊂ k' ⊂ k ⊂ K ⊂ K' ⊂ L' ⊂ L`, `k'` is `k'_0`-admissible for
the extension `L'` of `K'`.*

### 21.7. Cartier's equality

The following result translates in terms of differentials a theorem of MacLane on derivations:

<!-- original page 265 -->

**Theorem (21.7.1) (Cartier).**

<!-- label: 0_IV.21.7.1 -->

*Let `K` be a field, `L` an extension of finite type of `K`. Then `Ω^1_{L/K}` and `Υ_{L/K}` are `L`-vector spaces of
finite rank, and one has*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K} = deg.tr_K L.                                            (21.7.1.1)
```

If `L'` is a field such that `K ⊂ L' ⊂ L`, one has the exact sequence `(20.6.15.1)` (applied to `A = P`, prime field
of `K`, `A = K`, `B = L'`, `C = L`)

```text
  0 → Υ_{L/K} → Υ_{L/L'} → Υ_{L'/K} ⊗_{L'} L → Ω^1_{L'/K} ⊗_{L'} L → Ω^1_{L/K} → Ω^1_{L/L'} → 0
```

whence `(0_III, 11.10.2)`

```text
  rg_L Ω^1_{L/K} − rg_L Υ_{L/K} = (rg_L Ω^1_{L/L'} − rg_L Υ_{L/L'}) + (rg_{L'} Ω^1_{L'/K} − rg_{L'} Υ_{L'/K}).
```

Since on the other hand `deg.tr_K L = deg.tr_K L' + deg.tr_{L'} L`, one sees, by induction on the number of generators
of the extension `L`, that one is reduced to proving `(21.7.1.1)` when `L = K(x)`. Let us distinguish three cases:

a) `x` is transcendental over `K`; as `L` is separable over `K`, one has then `Υ_{L/K} = 0` `(20.6.3)`; on the other
hand, `(20.5.9)` and `(20.4.13)` show that `Ω^1_{L/K}` is of rank `1`, whence `(21.7.1.1)` in this case.

b) `L` is an algebraic separable extension of `K`, so that one still has `Υ_{L/K} = 0` `(20.6.3)`. On the other hand,
one has `Ω^1_{L/K} = 0` by `(20.6.20)`, whence again `(21.7.1.1)`.

c) `L` is an algebraic inseparable extension of `K`; the reasoning at the beginning shows that one can restrict to
the case where `L^p ⊂ K`; it then follows from `(21.4.8)` that one has `rg Ω^1_{L/K} = rg Υ_{L/K}`, whence again
`(21.7.1.1)`.

**Corollary (21.7.2).**

<!-- label: 0_IV.21.7.2 -->

*Let `K` be a field, `L` an extension of finite type of `K`, `k` a subfield of `K`. Then `Ω^1_{L/K}` and `Υ_{L/K/k}`
are vector spaces of finite rank over `L`, and one has*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K/k} = deg.tr_K L + d(L/K, k).                              (21.7.2.1)
```

*Consequently, one has the inequality*

```text
  rg Ω^1_{L/K} − rg Υ_{L/K/k} ≥ deg.tr_K L.                                          (21.7.2.2)
```

*Moreover, for the two sides of `(21.7.2.2)` to be equal, it is necessary and sufficient that `k` be an admissible
field for the extension `L` of `K`.*

In fact, since the homomorphism `Υ_{L/K} → Υ_{L/K/k}` is surjective, one has by definition `(21.6.1.2)`
`rg Υ_{L/K} − rg Υ_{L/K/k} = d(L/K, k)`, and the corollary thus follows at once from `(21.7.1)` and from `(21.6.2)`.

**Corollary (21.7.3).**

<!-- label: 0_IV.21.7.3 -->

*Let `k ⊂ K ⊂ L` be three fields such that `L` is an extension of finite type of `k`. Then one has*

```text
  rg Ω^1_{L/k} − rg Ω^1_{K/k} ⊗_K L = deg.tr_K L + d(L/K, k).                        (21.7.3.1)
```

<!-- original page 266 -->

*Consequently, one has the inequality*

```text
  rg Ω^1_{L/k} − rg_K Ω^1_{K/k} ≥ deg.tr_K L                                         (21.7.3.2)
```

*the equality being attained if and only if `k` is an admissible field for the extension `L` of `K`.*

One has in fact the exact sequence `(20.6.1.1)`

```text
  0 → Υ_{L/K/k} → Ω^1_{K/k} ⊗_K L → Ω^1_{L/k} → Ω^1_{L/K} → 0
```

hence the first side of `(21.7.3.1)` is equal to

```text
  rg_L Ω^1_{L/K} − rg_L Υ_{L/K/k}
```

and it suffices to apply `(21.7.2)`.

The interest of this last corollary is that it brings in only modules of differentials, to the exclusion of
imperfection modules. We shall see moreover further on `(21.8.6)` that for every extension `L` of `K` of finite type,
there exists a subfield `k` of `K` such that `[K : k]` be finite and which is admissible for the extension `L` of
`K`, so that the two sides of `(21.7.3.2)` are then equal.

**Corollary (21.7.4).**

<!-- label: 0_IV.21.7.4 -->

*Let `K` be an extension of finite type of a field `k`. The following conditions are equivalent:*

*a) `K` is a finite separable extension of `k`.*

*b) `K` is a `k`-algebra formally unramified `(19.10.2)`.*

*c) `K` is a `k`-algebra formally étale `(19.10.2)`.*

*d) One has `Ω^1_{K/k} = 0`.*

In fact, one knows (the topologies being discrete) that conditions b) and d) are equivalent `(20.7.4)` and that a)
entails that `K` is a `k`-algebra formally smooth `(19.6.1)`, hence the conjunction of a) and b) is equivalent to
c). Everything comes down to seeing that d) entails a). Now, by virtue of `(21.7.1.1)`, the relation `Ω^1_{K/k} = 0`
entails that `K` is algebraic (hence finite) over `k` and that `Υ_{K/k} = 0`, that is to say `(20.6.3)` that `K` is
separable over `k`.

**Remark (21.7.5).**

<!-- label: 0_IV.21.7.5 -->

*By virtue of `(20.6.3.2)` and of `(0_III, 11.10.2)` the first side of `(21.7.1.1)` is none other than the
Euler-Poincaré characteristic of the complex `K.(C/B/A)` introduced in `(20.6.3)`, for `C = L`, `B = K` and `A = P`
(prime field of `K`). In the chapter devoted to the theory of intersections and the Riemann-Roch theorem, an
important role will be played also by generalized Euler-Poincaré characteristics (with values in groups of classes of
`𝒪`-Modules) of complexes generalizing the complexes `Γ.(C/A)` considered in `(20.6.22)`.*

### 21.8. Admissibility criteria

We return to our earlier conventions and therefore suppose that all the fields considered in this number are of
characteristic `p > 0`.

**Lemma (21.8.1).**

<!-- label: 0_IV.21.8.1 -->

*Let `K` be a field, `k` a subfield of `K`, `(k_α)_{α ∈ I}` a filtered decreasing family of subfields of `K` such that
`k = ⋂_{α ∈ I} k_α`. Let `V` be a vector space over `K`, `(a_i)_{1 ≤ i ≤ n}`*

<!-- original page 267 -->

*a finite family of vectors of `V`; if the family `(a_i)` is free over `k`, there exists an index `γ` such that it is
also free over `k_γ`.*

Let `r` be the rank of the family `(a_i)_{1 ≤ i ≤ n}` over `K`, and let us reason by induction on `n − r`; the
proposition is evident for `n = r`, for then the family `(a_i)_{1 ≤ i ≤ r}` is free over `K`, hence over every
subfield of `K`. Suppose for example that `(a_i)_{1 ≤ i ≤ r}` is free over `K`, and write
`a_{r+1} = ∑_{i=1}^r λ_i a_i`, with `λ_i ∈ K`; the family `(a_i)_{1 ≤ i ≤ r+1}` being free over `k`, the `λ_i` cannot
all belong to `k`; suppose for example that `λ_1 ∉ k`. Then there exists an index `β` such that `λ_1 ∉ k_β`; one
concludes that the family `(a_i)_{1 ≤ i ≤ r+1}` is free over `k_β`; in fact, as the family `(a_i)_{1 ≤ i ≤ r}` is free
over every subfield of `K`, if the family `(a_i)_{1 ≤ i ≤ r+1}` were not free over `k_β`, `a_{r+1}` would be equal to
a linear combination of the `a_i` with coefficients in `k_β`, and as these coefficients are necessarily the `λ_i`,
one arrives at a contradiction. It now suffices to apply the induction hypothesis replacing `K` by `k_β` and the
family `(k_α)_{α ∈ I}` by the sub-family of the `k_α` contained in `k_β`.

**Lemma (21.8.2).**

<!-- label: 0_IV.21.8.2 -->

*Let `K` be a field, `p` its characteristic exponent, `k_0` a subfield of `K`, `(k_α)_{α ∈ I}` a filtered decreasing
family of subfields of `K` such that `⋂_α k_α(K^p) = k_0(K^p)`. If `(x_i)_{1 ≤ i ≤ n}` is a finite family of elements
of `K` which is `p`-free over `k_0`, there exists an index `α` such that `(x_i)` is `p`-free over `k_α`.*

In fact, saying that the family `(x_i)` is `p`-free over a subfield `k` of `K` means that the finite family of
monomials `∏_{i=0}^n x_i^{m(i)}` with `0 ≤ m(i) < p` is free over `k(K^p)`; it therefore suffices to apply lemma
`(21.8.1)` to this family of monomials in the vector space `V = K`, and to the subfields `k_α(K^p)` and `k_0(K^p)` of
`K`.

**Theorem (21.8.3).**

<!-- label: 0_IV.21.8.3 -->

*Let `K` be a field of characteristic `p > 0`, `k_0` a subfield of `K`, `(k_α)_{α ∈ I}` a filtered decreasing family
of subfields of `K` containing `k_0`. The following conditions are equivalent:*

*a) `⋂_α k_α(K^p) = k_0(K^p)`.*

*b) For every extension `L` of `K` such that `Υ_{L/K/k_0}` is an `L`-vector space of finite rank (which holds in
particular if `L` is an extension of finite type by virtue of `(21.7.2)`), there exists `α ∈ I` such that `k_α` is
`k_0`-admissible for the extension `L` of `K`.*

*b') For every extension `L = K(x)` of `K`, with `x ∈ K`, there exists `α ∈ I` such that `k_α` is `k_0`-admissible
for the extension `L` of `K`.*

*c) The canonical map*

```text
  Ω^1_{K/k_0} → lim_α Ω^1_{K/k_α}                                                    (21.8.3.1)
```

*is injective.*

The canonical map `(21.8.3.1)` is of course obtained by passage to the projective limit in the projective system of
homomorphisms `Ω^1_{K/k_0} → Ω^1_{K/k_α}` `(20.5.3.3)`. We shall prove the theorem according to the logical schema
`c) ⇒ b) ⇒ b') ⇒ a) ⇒ c)`.

Saying that `k_α` is `k_0`-admissible for the extension `L` of `K` means that the canonical homomorphism

<!-- original page 268 -->

`Υ_{L/K/k_0} → Υ_{L/K/k_α}` is injective; now, if `N_α` is the kernel of this homomorphism, the `N_α` form a filtered
decreasing system of sub-vector spaces of `Υ_{L/K/k_0}`, and as `Υ_{L/K/k_0}` is by hypothesis of finite rank, it
amounts to the same to say that one of the `N_α` is `0` or that their intersection is `0`. But this intersection is
none other than the kernel of the homomorphism limit projective `Υ_{L/K/k_0} → lim_α Υ_{L/K/k_α}`. Now, one has the
commutative diagram

```text
  Υ_{L/K/k_0}                ——→ lim_α Υ_{L/K/k_α}
       ↓                                ↓
  Ω^1_{K/k_0} ⊗_K L          ——→ lim_α (Ω^1_{K/k_α} ⊗_K L)
```

where the left vertical arrow is injective by definition. In order to prove that c) entails b), it therefore suffices
to show that c) entails that the canonical map

```text
  Ω^1_{K/k_0} ⊗_K V → lim_α (Ω^1_{K/k_α} ⊗_K V)                                      (21.8.3.2)
```

is injective for every vector space `V` over `K` (and in particular for `V = L`). Now this is evident if `V = K^n`
since then `W ⊗_K V = W^n` for every vector space `W` over `K` and products and projective limits commute. On the
other hand, for every element `ξ` of the first side of `(21.8.3.2)` there exists a sub-vector space `V'` of `V` of
finite rank such that `ξ ∈ Ω^1_{K/k_0} ⊗_K V'` (canonically identified with a sub-space of `Ω^1_{K/k_0} ⊗_K V`); if
`ξ ≠ 0`, its image in `lim_α (Ω^1_{K/k_α} ⊗_K V')` is therefore non zero; as the functor `lim` is left exact, the
image of `ξ` in the second side of `(21.8.3.2)` is therefore also `≠ 0`, which finishes showing that c) implies b).

It is trivial that b) entails b'); let us show that b') entails a). With the notation of b'), one can suppose that
`L ≠ K`. It then follows from `(21.4.7)` that one has `rg_L Υ_{L/K/k_0} ≤ 1`. If `Υ_{L/K/k_0} = 0` there is nothing
to prove by virtue of `(21.6.1.1)`. Otherwise, `Υ_{L/K/k_0}` is identified canonically with `Υ_{L/K}` and if one sets
`a = x^p`, `Υ_{L/K}` has a basis formed by the single element `d_L a ⊗ 1` `(21.4.7)`; `Υ_{L/K/k_α}` therefore has a
basis formed by the single element `d_{K/k_α}(a) ⊗ 1`, and saying that a subfield `k_α` is `k_0`-admissible for the
extension `L` of `K` means that one has `d_{K/k_α}(a) ≠ 0`, or again `(21.4.5)` that `a ∉ k_α(K^p)`. Now, for every
`a ∉ k_0(K^p)`, one has `d_{K/k_0}(a) ≠ 0` and `K(a^{1/p}) ≠ K`, hence one can apply b'), which proves the existence
of an `α` such that `a ∉ k_α(K^p)`; in other words b') implies a).

It remains to show that a) implies c). Let `(x_λ)_{λ ∈ M}` be a `p`-basis of `K` over `k_0`; then, the
`d_{K/k_0}(x_λ)` form a basis of the `K`-vector space `Ω^1_{K/k_0}` `(21.4.5)`, and condition c) means that for every
finite part `J` of the index set `M`, there exists an `α ∈ I` such that the `d_{K/k_α}(x_μ)` for `μ ∈ J` are
linearly independent in `Ω^1_{K/k_α}`; but this means also `(21.4.5)` that the `x_μ` for `μ ∈ J` form a `p`-free
family over `k_α`, and the existence of an `α` having this property follows from `(21.8.2)` and from hypothesis a).

<!-- original page 269 -->

**Corollary (21.8.4).**

<!-- label: 0_IV.21.8.4 -->

*Let `K` be a field of characteristic `p > 0`, `k_0` a subfield of `K`, `(k_α)_{α ∈ I}` a filtered decreasing family
of subfields of `K`, containing `k_0`, such that*

```text
  ⋂_α k_α(K^p) = k_0(K^p).
```

*Let `L` be an extension of `K` such that `Υ_{L/K/k_0}` is an `L`-vector space of finite rank; then, for every field
`K'` such that `K ⊂ K' ⊂ L`, there exists `α ∈ I` such that `k_α` is `k_0`-admissible for the extension `L` of `K'`.*

It suffices to apply `(21.8.3)` and `(21.6.6)`.

**Corollary (21.8.5).**

<!-- label: 0_IV.21.8.5 -->

*Let `K` be a field of characteristic `p > 0`, `k_0` a subfield of `K`, `(k_α)_{α ∈ I}` a filtered decreasing family
of subfields of `K` containing `k_0`, such that*

```text
  ⋂_α k_α(K^p) = k_0(K^p).
```

*Then, for every extension `L` of `K` such that `Υ_{L/K/k_0}` is an `L`-vector space of finite rank, one has
`⋂_α k_α(L^p) = k_0(L^p)`.*

Suppose in fact that `M` is an extension of `L` such that `Υ_{M/L/k_0}` is an `M`-vector space of finite rank. The
exact sequence `(21.6.1.1)`

```text
  0 → Υ_{L/K/k_0} ⊗_L M → Υ_{M/K/k_0} → Υ_{M/L/k_0}
```

and the hypothesis then show that `Υ_{M/K/k_0}` is also an `M`-vector space of finite rank. There therefore exists
an index `α` such that `k_α` is `k_0`-admissible for the extension `M` of `K` `(21.8.3)`, hence also for the
extension `M` of `L` `(21.6.6)`; this taking place for every extension `M` of `L` such that `Υ_{M/L/k_0}` be of finite
rank, the corollary follows from the equivalence of a) and b) in `(21.8.3)`.

**Corollary (21.8.6).**

<!-- label: 0_IV.21.8.6 -->

*Let `K` be a field, `p` its characteristic exponent, `k_0` a subfield of `K`. If `L` is an extension of `K` such that
`Υ_{L/K/k_0}` is an `L`-vector space of finite rank, there exists a subfield `k` of `K`, containing `k_0(K^p)`, such
that `[K : k]` be finite, and which is `k_0`-admissible for the extension `L` of `K`.*

It suffices in fact, by virtue of `(21.8.3)`, to construct a filtered decreasing family `(k_α)_{α ∈ I}` of subfields
of `K`, containing `K^p` and `k_0`, for which `[K : k_α] < +∞` and `⋂_α k_α = k_0(K^p)`. For this one considers a
`p`-basis `(x_λ)_{λ ∈ J}` of `K` over `k_0` and, for every finite part `H` of `J`, one considers the subfield `k_H` of
`K` generated by `k_0(K^p)` and the `x_λ` of index `λ ∈ J − H`; it follows from this definition that `(x_λ)_{λ ∈ H}`
is a `p`-basis of `K` over `k_H`, and one concludes at once that the `k_H` verify the desired conditions.

**Remarks (21.8.7).**

<!-- label: 0_IV.21.8.7 -->

*(i) One has already seen `(21.7.2)` that if `L` is an extension of finite type of `K`, `Υ_{L/K/k_0}` is of finite
rank for every subfield `k_0` of `K`. The same holds if `L` is a separable extension of `K`, for by virtue of
`(20.6.19)`, one has `Υ_{L/K/k_0} = 0`. Finally, if `L` is an extension of finite type of a separable extension `L_0`
of `K`, the same reasoning as in `(21.8.5)` shows that `Υ_{L/K/k_0}` is still of finite rank (and in fact is
isomorphic to a sub-space of `Υ_{L/L_0/k_0}`).*

<!-- original page 270 -->

*(ii) In the statement of `(21.8.5)`, and consequently also in that of `(21.8.3, b))`, one cannot omit the hypothesis
that `Υ_{L/K/k_0}` is of finite rank over `L`. Let us take for `k_0` the prime field `𝔽_p`, for `K` a field such that
`[K : K^p]` be countably infinite (for example the field of rational fractions `𝔽_p(X_1, …, X_n, …)` in infinitely
many indeterminates); the construction procedure of `(21.8.6)` shows at once that there exists a strictly decreasing
infinite sequence `(K_n)` of subfields of `K` such that `K_0 = K` and `⋂_n K_n = K^p`. We are going to construct an
increasing sequence of finite extensions `M_n` of `K`, such that if `M` is the union of the `M_n`, the extension
`L = M^{1/p}` of `K` provides a counter-example to `(21.8.5)`. For this, let `x` be an element of `K − K_1`, set
`M_0 = K` and `M_n = K(a_1 x, a_2 x, …, a_n x)` for `n ≥ 1`, where the `a_n` are constructed by induction so that
`a_n ∈ K_n` and `a_{n+1} ∉ M_n(x)` for every `n`: this is possible, for `M_n(x)` is of finite degree over `K_n`, while
the same is not so of `K_n`. One concludes at once that `x ∉ M = L^p`, but as `x = (a_n x) a_n^{-1}`, one has
`x ∈ K_n(M) = K_n(L^p)` for every `n`.*

**Proposition (21.8.8).**

<!-- label: 0_IV.21.8.8 -->

*Let `k` be a field of characteristic `p > 0`, and let `A = k[[T_1, …, T_r]]` be the ring of formal power series in
`r` indeterminates over `k`, `K = k((T_1, …, T_r))` its field of fractions. Then there exists a filtered decreasing
family `(A_α)` of Noetherian subrings of `A` such that `A` be a free `A_α`-module of finite type for every `α` and
that, if `K_α` is the field of fractions of `A_α`, one has `⋂_α K_α = K^p`.*

One can write `K^p = k^p((T_1^p, …, T_r^p))`; one has seen in the proof of `(21.8.6)` that there exists a decreasing
family `(k_α)` of subfields of `k` such that `[k : k_α]` is finite for every `α` and `⋂_α k_α = k^p`; it is clear that
if one sets `A_α = k_α[[T_1^p, …, T_r^p]]`, `A` is a free `A_α`-module of finite type; everything therefore comes down
to proving the relation

```text
  ⋂_α k_α((T_1^p, …, T_r^p)) = k^p((T_1^p, …, T_r^p)).                                (21.8.8.1)
```

Since `⋂_α k_α = k^p`, this will follow from the two following lemmas:

**Lemma (21.8.8.2).**

<!-- label: 0_IV.21.8.8.2 -->

*If `k'` is an extension of a field `k`, one has*

```text
  k'[[T_1, …, T_r]] ∩ k((T_1, …, T_r)) = k[[T_1, …, T_r]].
```

In fact, set `C = k[[T_1, …, T_r]]`, `D = k'[[T_1, …, T_r]]`; as `k((T_1, …, T_r))` is the field of fractions of `C`,
it will suffice to prove that `D` is a faithfully flat `C`-module (Bourbaki, Alg. comm., chap. I, §3, n° 5, prop. 10).
Now, `C` and `D` are Noetherian local rings, and if `𝔪` is the maximal ideal of `C`, one has
`D/𝔪 D = (C/𝔪) ⊗_k k'`, hence `D/𝔪 D`

<!-- original page 271 -->

is a flat `(C/𝔪)`-module; it therefore suffices to apply `(0_III, 10.2.1)` and `(0_I, 6.6.2)`.

**Lemma (21.8.8.3).**

<!-- label: 0_IV.21.8.8.3 -->

*Let `k` be a field, `(k_α)` a filtered decreasing family of subfields of `k`, and set `k_0 = ⋂_α k_α`. Suppose there
exists a power `q` of the characteristic exponent of `k` such that `k^q ⊂ k_0`. Then one has*

```text
  ⋂_α k_α((T_1, …, T_r)) = k_0((T_1, …, T_r)).                                       (21.8.8.4)
```

It suffices to prove that an element `f ≠ 0` of the first side of `(21.8.8.4)` belongs to the second side. Let `γ`
be an index, `g_γ ∈ k_γ[[T_1, …, T_r]]` such that `g_γ f ∈ k_γ[[T_1, …, T_r]]`; up to replacing `g` by `g^q`, one can
suppose that `g ∈ k_0[[T_1, …, T_r]]`. Then, for every `α ≥ γ`, one has

```text
  k_α[[T_1, …, T_r]] ∩ k_γ((T_1, …, T_r)) = k_α[[T_1, …, T_r]]
```

by virtue of lemma `(21.8.8.2)`. But it is clear that the intersection of the rings `k_α[[T_1, …, T_r]]` is none
other than `k_0[[T_1, …, T_r]]`, and one has therefore indeed `f ∈ k_0((T_1, …, T_r))`.

### 21.9. Completed differential modules in formal power series rings

In this number, the fields are no longer necessarily supposed to be of characteristic `> 0`.

**Lemma (21.9.1).**

<!-- label: 0_IV.21.9.1 -->

*Let `k` be a field, `A` a complete Noetherian local ring which is a `k`-algebra, `K` the residue field of `A`. If `K`
is an extension of finite type of `k`, the `A`-module `Ω̂^1_{A/k}` is of finite type.*

By virtue of `(20.7.15)`, it suffices to prove that `Ω^1_{K/k}` is a `K`-vector space of finite rank. Now, by
hypothesis, `K` is the field of fractions of a `k`-algebra of finite type `B`; as `Ω^1_{B/k}` is a `B`-module of
finite type by virtue of `(20.4.7)`, the conclusion follows from `(20.5.9)`.

**Proposition (21.9.2).**

<!-- label: 0_IV.21.9.2 -->

*Let `k_0` be a field, `A` a complete Noetherian local ring which is a `k_0`-algebra formally smooth, `𝔪` its maximal
ideal, `K = A/𝔪` its residue field (so that as a ring `A` is isomorphic to a ring of formal power series
`K[[T_1, …, T_n]]` `(19.6.5)`). If `K` is an extension of finite type of `k_0`, then `Ω̂^1_{A/k_0}` is a free
`A`-module of rank equal to `dim(A) + deg.tr_{k_0} K`. Moreover, for every subfield `k` of `k_0` such that
`Ω^1_{k_0/k}` is of finite rank, `Ω̂^1_{A/k}` is a free `A`-module of rank equal to
`dim(A) + deg.tr_k K + rg_{k_0}(Ω^1_{k_0/k})`.*

It is clear that, if `P` is the prime subfield of `k_0`, `K` is a `P`-algebra formally smooth `(19.6.1)`. Note on
the other hand that one has `Υ_{k_0/P} = 0`: in fact, this comes down to seeing that the homomorphism

```text
  Ω̂^1_{k_0/P} ⊗̂_{k_0} K = Ω^1_{k_0/P} ⊗_{k_0} K → Ω^1_{A/P} ⊗_A K
```

is injective `(20.6.14.5)`, `u` denoting the structural homomorphism `k_0 → A`. But as `A` is a `k_0`-algebra
formally smooth by hypothesis, it follows from `(20.7.2)` that `u^*_P` is formally left invertible, hence
`(19.1.7)` `u^*_P ⊗ 1_K` is left invertible and a fortiori injective, which proves our assertion. Applying the exact
sequence `(20.6.22.1)`, where `A, k, B, C` are replaced by `P, k_0, A, K`, one has the exact sequence

```text
  0 → Υ_{K/k_0/P} → 𝔪/𝔪^2 → Ω^1_{k_0/P} ⊗_{k_0} K → Ω^1_{K/P} → Ω^1_{K/k_0} → 0
```

so that one has

```text
  rg_K(Ω̂^1_{A/k_0} ⊗_A K) = rg_K(𝔪/𝔪^2) + (rg_K(Ω^1_{K/k_0}) − rg_K(Υ_{K/k_0/P})) = rg_K(𝔪/𝔪^2) + deg.tr_{k_0} K
```

by virtue of `(21.7.1)`. On the other hand, `Ω̂^1_{A/k_0}` is a formally projective `A`-module `(20.4.9)`, and as its
topology is the `𝔪`-preadic topology `(20.4.5)`, `Ω̂^1_{A/k_0}/𝔪^{j+1} Ω̂^1_{A/k_0}` is a projective
`(A/𝔪^{j+1})`-module for every `j` `(19.2.4)`, hence free `(0_I, 10.1.2)` and of rank

<!-- original page 272 -->

`= rg_K(Ω̂^1_{A/k_0} ⊗_A K)`. By virtue of `(21.9.1)`, `Ω̂^1_{A/k_0}` is an `A`-module of finite type, and moreover
this `A`-module is flat by virtue of `(0_I, 10.2.1)`; it is therefore free `(0_I, 10.1.3)` of rank `n`, whence the
first assertion.

Since by hypothesis `Ω^1_{k_0/k}` is of finite rank over `k_0`, the completed tensor product
`Ω^1_{k_0/k} ⊗̂_{k_0} A` is identified with `Ω^1_{k_0/k} ⊗_{k_0} A`; as `A` is a `k_0`-algebra formally smooth, it
follows from `(20.7.18)` that the homomorphism

```text
  u^*_{A/k_0/k} : Ω̂^1_{k_0/k} ⊗̂_{k_0} A → Ω̂^1_{A/k}
```

admits a left inverse which is a continuous `A`-homomorphism, which implies in particular that its image is closed
in `Ω̂^1_{A/k}`; the sequence

```text
  0 → Ω^1_{k_0/k} ⊗_{k_0} A → Ω̂^1_{A/k} → Ω̂^1_{A/k_0} → 0
```

is therefore exact and split by virtue of `(20.7.17)` and of what precedes; which finishes proving the proposition.

**Corollary (21.9.3).**

<!-- label: 0_IV.21.9.3 -->

*Let `k` be a field, `A` the formal power series ring `k[[T_1, …, T_r]]`, equipped with its usual `k`-algebra structure.
Then `Ω̂^1_{A/k}` is a free `A`-module of rank `r = dim(A)`.*

It suffices to note that `A` is a `k`-algebra formally smooth `(19.3.4)`, and to apply `(21.9.2)` with
`k_0 = k = K`.

**Lemma (21.9.4).**

<!-- label: 0_IV.21.9.4 -->

*Let `k` be a field of characteristic `p > 0`, `A` a `k`-algebra which is a complete Noetherian local ring, `B` a
sub-`k`-algebra of `A` isomorphic to a topological `k`-algebra of the form `k[[T_1, …, T_r]]` and such that `A` be a
`B`-algebra of finite type. If `B_1` is the subalgebra `k[[T_1^p, …, T_r^p]]` of `B`, `Ω̂^1_{A/B}` is identified
canonically with `Ω̂^1_{A/B_1}`.*

Every continuous derivation of `B_1` into a topological `A`-module `P`, which is the restriction of a continuous
`A`-derivation of `A` into `P`, is zero, for it is so on the subring `k[T_1^p, …, T_r^p]` of polynomials, and this
last is dense in `B_1`. The exact sequence `(20.3.7.1)` therefore shows that the canonical homomorphism

```text
  Der.cont_B(A, P) → Der.cont_{B_1}(A, P)
```

is bijective; the conclusion follows from `(20.7.14.4)`, taking account of the fact that `Ω̂^1_{A/B}` is an
`A`-module of finite type `(20.4.7)`, hence separated and complete since `A` is a complete Noetherian local ring.

**Proposition (21.9.5).**

<!-- label: 0_IV.21.9.5 -->

*Let `A` be an integral complete Noetherian local ring, `A_0` a subring of `A` isomorphic to a formal power series
ring `k[[T_1, …, T_r]]` over a field `k`, such that `A` be a finite `A_0`-algebra and that the field of fractions `E`
of `A` be a separable extension of the field of fractions `L_0` of `A_0`. Then one has*

```text
  rg_A Ω̂^1_{A/A_0} = rg_E(Ω̂^1_{A/A_0} ⊗_A E) = dim(A).                               (21.9.5.1)
```

Note that if `𝔪_0` is the maximal ideal of `A_0`, the topology of `A` is the `𝔪_0`-adic topology since `A` is a
finite `A_0`-algebra (Bourbaki, Alg. comm., chap. IV, §2, n° 5, cor. 3 of prop. 9) and induces on `A_0` the
`𝔪_0`-adic topology (Bourbaki, Alg. comm., chap. III, §3, n° 4, th. 3). One knows `(21.9.1)` that `Ω̂^1_{A/A_0}` is an
`A`-module of finite type, and

<!-- original page 273 -->

by virtue of `(21.9.3)` `Ω̂^1_{A_0/k}` is a free `A_0`-module of rank `r = dim(A_0) = dim(A)` `(16.1.5)`; the tensor
product `Ω̂^1_{A_0/k} ⊗_{A_0} A` is therefore a free `A`-module of rank `r` identical with its separated completion;
finally `Ω̂^1_{A/k}` is an `A`-module of finite type `(20.4.7)`, hence identical with its separated completion `(0_I,
7.3.6)`. This being so, in the sequence of homomorphisms

```text
  Ω̂^1_{A_0/k} ⊗_{A_0} A → Ω̂^1_{A/k} → Ω̂^1_{A/A_0} → 0                                (21.9.5.2)
```

one knows that `v` is surjective and that `Im(u)` is dense in `Ker(v)` `(20.7.17)`; but every sub-`A_0`-module of
`Ω̂^1_{A/k}` is closed for the `𝔪_0`-adic topology `(0_I, 7.3.5)`, hence the sequence `(21.9.5.2)` is exact. Note on
the other hand that since `A` is integral over `A_0`, `A_0` integrally closed and `E` separable over `L_0`,
`Ω̂^1_{A/A_0}` is a torsion `A`-module `(20.4.13, (iv))`; tensorizing the exact sequence `(21.9.5.2)` by `E`, one
obtains an exact sequence

```text
  Ω̂^1_{A_0/k} ⊗_{A_0} E → Ω̂^1_{A/k} ⊗_A E → 0
```

whence `rg_E(Ω̂^1_{A/k} ⊗_A E) ≤ r`. It remains therefore to show that there exist, in `Ω̂^1_{A/k} ⊗_A E`, `r` elements
linearly independent over `E`. Now, let `D_i = ∂/∂T_i` be the canonical derivations of `A_0` into itself
`(1 ≤ i ≤ r)`; they extend in a unique manner to derivations (still denoted `D_i`) of `E` into itself, since `E` is a
finite separable extension of `L_0`; by restriction to `A`, these derivations give derivations of `A` into `E`, and
it is immediate that these derivations take their values in a same sub-`A`-module of finite type of `E`; as they are
continuous on `A_0` and the topology of `A` is the `𝔪_0`-adic topology, one has thus formed `r` continuous
derivations of `A` into a topological `A`-module, which are evidently linearly independent since `D_i(T_j) = δ_{ij}`;
this finishes proving the proposition.

The following proposition is a "formal" analogue of `(21.7.3)`:

**Proposition (21.9.6).**

<!-- label: 0_IV.21.9.6 -->

*Let `k_0 ⊂ k ⊂ K_0` be three fields of characteristic `p > 0`, such that `[K_0 : k] < +∞`; set*

```text
  L_0 = K_0((T_1, …, T_r)),     M_0 = K_0((T_1^p, …, T_r^p))
  L = k((T_1, …, T_r)),         M = k((T_1^p, …, T_r^p)),     N = k((T_1^p, …, T_r^p)).
```

*Let `E` be an extension of finite type of `L_0`.*

*(i) If `Υ_{K_0/k_0}` is of finite rank, one has*

```text
  rg_E Ω^1_{E/M_0} − rg_{K_0} Ω^1_{K_0/k_0} = (r + deg.tr_k E) + d(E/K_0, k/k_0) + d(E/M_0, N/k_0)   (21.9.6.1)
```

*(notation of `(21.6.1)`), and in particular one has*

```text
  rg_E Ω^1_{E/M} − rg_K Ω^1_{K/k} ≥ r + deg.tr_k E + d(E/K_0, k_0).                   (21.9.6.2)
```

*Moreover, if the two sides of `(21.9.6.2)` are equal, they remain so when one replaces `k` by a field `k'` such that
`k_0 ⊂ k' ⊂ k`.*

*(ii) Suppose moreover that `[k_0 : k_0^p] < +∞`. Let `(k_α)` be a filtered decreasing family of subfields of `K_0`
containing `k_0`, such that `[K_0 : k_α] < +∞` for every `α` and that `⋂_α k_α(K_0^p) = k_0(K_0^p)`; then there exists
an `α` such that, for `k = k_α`, the two sides of `(21.9.6.2)` are equal.*

<!-- original page 274 -->

(i) One knows `(21.1.5, (ii))` that `rg_E Ω^1_{E/M}` does not change when one replaces `M` by `M(L_0^p)`; as
`L_0^p = K_0^p((T_1^p, …, T_r^p))` and `[k(K_0^p) : k] < +∞`, one has

```text
  M(L_0^p) = k(K_0^p)((T_1^p, …, T_r^p));
```

similarly `Ω^1_{K/k}` does not change when one replaces `k` therein by `k(K_0^p)`, so that one can suppose `K_0^p ⊂ k`,
which we shall do in all the sequel. We shall also introduce the fields

```text
  k_1 = k_0(K_0^p),    N_1 = k_1((T_1^p, …, T_r^p))
```

so that one has the diagram of fields

```text
  K_0 ——→ M_0 ——→ L_0 ——→ E
   ↑       ↑       ↑       ↑
   k ———→ N  ———→ M ————→ L
   ↑       ↑       ↑
  k_1 ——→ N_1
```

We propose to evaluate the difference `δ` of the first and second sides of `(21.9.6.2)`.

It follows from `(21.7.3)` that one has

```text
  rg_E Ω^1_{E/M} − rg_{M_0} Ω^1_{M_0/M} = deg.tr_M E + d(E/M_0, M)
```

and as `L_0` is a finite extension of `M_0`, one has `deg.tr_M E = deg.tr_{L_0} E`. On the other hand, a `p`-basis
of `K_0` over `k = k(K_0^p)` is also a `p`-basis of `M_0` over `M`, hence `(21.4.5)`, one has

```text
  rg_{M_0} Ω^1_{M_0/M} = rg_{K_0} Ω^1_{K_0/k}
```

so that one has

```text
  δ = d(E/M_0, M) − d(E/K_0, k_0) − r.                                                (21.9.6.3)
```

Let us note now the classical lemma:

**Lemma (21.9.6.4).**

<!-- label: 0_IV.21.9.6.4 -->

*For every field `k`, the formal power series field `K = k((T_1, …, T_r))` is a separable extension of `k`.*

Let us briefly recall the proof of this lemma for completeness. It suffices (Bourbaki, Alg., chap. VIII, §7, n° 3,
proof of th. 1) to prove that for every finite extension `k'` of `k`, `K ⊗_k k'` is without nilpotent element; but if
one sets `A = k[[T_1, …, T_r]]` and `S = A − \{0\}`, `K ⊗_k k'` is equal to `S^{-1}(A ⊗_k k')`, and `A ⊗_k k'` is
identified canonically with the integral ring `A' = k'[[T_1, …, T_r]]` and `A` to a subring of `A'`, whence the
conclusion.

Using this lemma and `(21.6.2, (ii))`, one has `d(L_0/K_0, k_0) = 0`, and formula `(21.6.4.4)` therefore gives

```text
  d(E/K_0, k_0) = d(E/L_0, k_0).
```

<!-- original page 275 -->

Formulas `(21.6.4.4)` and `(21.6.4.2)` on the other hand give

```text
  d(E/M_0, M) = d(E/L_0, M) + d(L_0/M_0, M),
  d(L_0/M_0, M) = d(L_0/M_0, M/N) + d(L_0/M_0, N)
```

whence

```text
  δ = d(E/L_0, M) + d(L_0/M_0, N) − d(E/L_0, k_0) + d(L_0/M_0, M/N) − r.
```

We are going to show that one has the relation

```text
  d(L_0/M_0, M/N) = r.                                                                (21.9.6.5)
```

For this, note that by definition, one has

```text
  d(L_0/M_0, M/N) = rg_{L_0} Ω^1_{L_0/M/N} − rg_{M_0} Ω^1_{M_0/M/N}.
```

Taking account of the two exact sequences

```text
  0 → Υ_{L_0/M/N} → Ω^1_{M/N} ⊗_M L_0 → Ω^1_{L_0/N} → Ω^1_{L_0/M} → 0
  0 → Υ_{M_0/M/N} → Ω^1_{M/N} ⊗_M M_0 → Ω^1_{M_0/N} → Ω^1_{M_0/M} → 0
```

it follows that

```text
  d(L_0/M_0, M/N) = rg_{L_0} Ω^1_{L_0/M} − rg_{L_0} Ω^1_{L_0/N} − rg_{M_0} Ω^1_{M_0/M} + rg_{M_0} Ω^1_{M_0/N}.
```

Now, one has `N(L_0^p) ⊃ M`, hence `Ω^1_{L_0/M} = Ω^1_{L_0/N}` `(21.1.5, (ii))`. On the other hand, the `T_i`
(`1 ≤ i ≤ r`) form a `p`-basis of `M` over `N`, and a `p`-basis of `K_0` over `k` is also a `p`-basis of `M_0` over
`M`, hence, as `M_0^p ⊂ N`,

```text
  rg_{M_0} Ω^1_{M_0/N} = r + rg_{M_0} Ω^1_{M_0/M} = r + rg_K Ω^1_{K/M}
```

by virtue of `(21.4.5)` and `(21.1.10)`, which proves `(21.9.6.5)`.

One again has, by `(21.6.4.2)`,

```text
  d(E/L_0, M) = d(E/L_0, k_0) + d(E/L_0, M/k_0)
```

and

```text
  d(L_0/M_0, N) = d(L_0/M_0, N/k) + d(L_0/M_0, k).
```

But as `L_0` is separable over `K_0` `(21.9.6.4)`, one has `d(L_0/K_0, k) = 0`, and consequently also
`d(L_0/M_0, k) = 0` (`(21.6.2)` and `(21.6.4)`). One therefore obtains

```text
  δ = d(E/L_0, M/k_0) + d(L_0/M_0, N/k).
```

Let us apply `(21.6.4.2)` twice more to the first term of the second side of this formula; one obtains

```text
  d(E/L_0, M/k_0) = d(E/L_0, M/N) + d(E/L_0, N/k) + d(E/L_0, k/k_0).
```

As `M ⊂ N(L_0^p)`, one has `d(E/L_0, M/N) = 0` `(21.6.2)`, hence (by `(21.6.4.4)`)

```text
  δ = d(E/L_0, k/k_0) + d(E/M_0, N/k).
```

But `M_0` and `L_0` are separable extensions of `K_0` `(21.9.6.4)`, hence
`d(L_0/K_0, k/k_0) = d(M_0/K_0, k/k_0) = 0` `(21.6.2)`, and applying twice more `(21.6.4.4)`,

<!-- original page 276 -->

one has `d(E/L_0, k/k_0) = d(E/K_0, k/k_0) = d(E/M_0, k/k_0)`, whence, by a last application of `(21.6.4.2)`,

```text
  δ = d(E/M_0, N/k_0)
```

which proves `(21.9.6.1)`. Moreover, when `k` is replaced by a sub-extension `k'` of `k_0`, `N` is replaced by a
sub-extension `N'`, hence `d(E/M_0, N'/k_0) ≤ d(E/M_0, N/k_0)` `(21.6.4.2)`, which proves the last assertion of (i).

(ii) For every `α`, set `N_α = k_α((T_1^p, …, T_r^p))`. By virtue of `(21.9.6.1)` and of `(21.8.3)`, it amounts to
showing (taking account of the fact that `K_0^p ⊂ k_α` and that `E` is an extension of finite type of `M_0`) that
one has

```text
  ⋂_α N_α = k_0(M_0^p).
```

Now, one has

```text
  ⋂_α N_α = N' = (k_0(K_0^p))((T_1^p, …, T_r^p))                                      (21.9.6.6)
```

by virtue of `(21.8.8.3)` and of the relation `⋂_α k_α = k_0(K_0^p)` `(21.8.6)`. On the other hand, one has
`k_0(M_0^p) = k_0(K_0((T_1^p, …, T_r^p)))`. To finish the proof of `(21.9.6, (ii))`, it therefore remains to prove
the

**Lemma (21.9.6.7).**

<!-- label: 0_IV.21.9.6.7 -->

*Let `k_0` be a field of characteristic `p > 0` such that `[k_0 : k_0^p] < +∞`, `K_0` an extension of `k_0`. Then one
has*

```text
  (k_0(K_0^p))((T_1, …, T_r)) = k_0(K_0((T_1, …, T_r))).                              (21.9.6.8)
```

As `k_0 ⊂ K_0`, one has `k_0(K_0((T_1, …, T_r))) = K_0((T_1, …, T_r))`. If `(x_i)_{i ∈ I}` is a basis of `k_0` over
`k_0^p`, it is immediate that `(x_i)` is also a system of generators of each of the two sides of `(21.9.6.8)` over
`K_0^p((T_1, …, T_r))`.

**Remark (21.9.7).**

<!-- label: 0_IV.21.9.7 -->

*The assertion of `(21.9.6, (ii))` does not extend to the case where `[k_0 : k_0^p]` is infinite. Take in fact for
`k_0` the field `𝔽_p(X_n)_{n ≥ 0}` of rational fractions in infinitely many indeterminates, so that the `X_n` form a
`p`-basis of `k_0` over `𝔽_p`, and consequently `[k_0 : k_0^p] = +∞`. In the statement of `(21.9.6)`, take `K_0 = k_0`
(hence necessarily `k = k_0`), `L_0 = k_0((T))`, for `E` the extension `L_0(y)`, where `y` is a root of the polynomial
`Y^p − ∑_{n=0}^∞ X_n T^n` of `L_0[Y]`. Then the difference `δ` of the two sides of `(21.9.6.2)` is non zero. In fact,
`E` is separable over `k_0`, otherwise `y` would be an element of `k_0(L_0^p)`, and one sees at once that this is not
possible (due to the fact that there are infinitely many `X_n` algebraically independent); one therefore has
`d(E/K_0, k_0) = 0`, formula `(21.9.6.3)` reduces to `δ = d(E/M_0, M_0) − 1`, and it is clear that
`d(E/M_0, M_0) = rg_E Υ_{E/M_0}`. Everything comes down to verifying that this rank is `2`. Now one has `E^p ⊂ M_0`,
a `p`-basis of `E` over `L_0` is formed by the single element `y`, and `L_0` evidently has a `p`-basis over `M_0`
formed by the single element `T`; hence, since `E` is an algebraic extension of `M_0`, our assertion follows from
`(21.7.1)` and `(21.4.5)`.*

**Proposition (21.9.8).**

<!-- label: 0_IV.21.9.8 -->

*Let `k_0` be a field (of any characteristic), `K_0` a separable extension of `k_0`, `A` a complete Noetherian local
ring, which is a `k_0`-algebra and whose residue field*

<!-- original page 277 -->

*is a finite extension of `K_0`. For every prime ideal `𝔭` of `A`, let `k(𝔭)` be the residue field of `A` at `𝔭`. Then,
for every field `k` such that `k_0 ⊂ k ⊂ K_0` and such that `[K_0 : k] < +∞`, one has*

```text
  rg_{k(𝔭)}(Ω̂^1_{A/k} ⊗_A k(𝔭)) − rg_{K_0} Ω^1_{K_0/k} ≥ dim(A/𝔭) + r + d(k(𝔭)/K_0, k_0).   (21.9.8.1)
```

*Suppose moreover that `[k_0 : k_0^p] < +∞` (where `p` is the characteristic exponent of `k_0`). Then one can find a
field `k` such that `k_0(K_0^p) ⊂ k ⊂ K_0` and `[K_0 : k] < +∞`, for which the two sides of `(21.9.8.1)` are equal.*

Since `A/𝔭` has the same residue field `K` as `A` and is complete, one can restrict to the case where `A` is integral
and `𝔭 = 0`; one will then set `E = k(𝔭)`, the field of fractions of `A`. As `K_0` is formally smooth over `k_0`
`(19.6.1)`, there exists a `k_0`-monomorphism `K_0 → A` making `A` a `K_0`-algebra; one knows moreover that there
exists a sub-`K_0`-algebra `A_0` of `A`, `K_0`-isomorphic to a formal power series algebra `K_0[[T_1, …, T_r]]` and
such that `A` be a finite `A_0`-algebra `(19.8.9)`, which entails that `E` is a finite extension of the field of
fractions `L_0 = K_0((T_1, …, T_r))` of `A_0`. One has then `Υ_{K_0/k} = 0` since `K_0` is separable over `k_0`, and
`deg.tr_{K_0} E = 0`; moreover, since `A` is a finite `A_0`-algebra, one has `dim(A) = dim(A_0)` `(16.1.5)`.

If `p = 1`, one has `rg_E(Ω̂^1_{A/k} ⊗_A E) = r` by `(21.9.5)` and `(17.1.4, (iii))`, and `Υ_{L_0/K_0} = 0` since
`K_0` is a finite separable extension of `k` `(21.7.4)`; on the other hand `Ω^1_{K_0/k} = 0`, `E` being a separable
extension of `k_0`; the two sides of `(21.9.8.1)` are therefore equal in this case.

Suppose now that `p > 1`; if `B = k[[T_1, …, T_r]]`, `A` is a `B`-algebra of finite type, hence, setting
`B_1 = k[[T_1^p, …, T_r^p]]`, `Ω̂^1_{A/B}` is identified with `Ω̂^1_{A/B_1}` `(21.9.4)`, and denoting by `M` the field of
fractions `k((T_1^p, …, T_r^p))`, it follows from `(20.5.9)` that `Ω̂^1_{A/B} ⊗_A E` is identified with `Ω^1_{E/M}`;
the inequality `(21.9.8.1)` is then nothing but `(21.9.6.2)`, and the last assertion of the corollary follows from
`(21.9.6, (ii))`.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/08-c0-s21-differentielles-anneaux-caracteristique-p.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-1.pdf -->
