# Chapter 0_III

## §11. Complements on homological algebra

> _Translator's note._ In the OCR'd French source, the content of §11 is housed inside the file named for §10
> (`03-c0-s10-complements-modules-plats.md`, lines 266–1485). It is given its own translated file here.

<!-- original page 367 -->

### 11.1. Recall on spectral sequences

**11.1.1.**

<!-- label: 0_III.11.1.1 -->

In what follows we shall use a notion of spectral sequence more general than the one defined in `(T, 2.4)`; keeping the
notation of `(T, 2.4)`, we shall call a *spectral sequence in an abelian category `𝒞`* a system `E` consisting of the
following data:

a) A family `(E_r^{p,q})` of objects of `𝒞` defined for `p ∈ ℤ`, `q ∈ ℤ`, and `r ≥ 2`.

b) A family of morphisms `d_r^{p,q} : E_r^{p,q} → E_r^{p+r, q-r+1}` such that `d_r^{p+r, q-r+1} ∘ d_r^{p,q} = 0`.

We set `Z_{r+1}(E_2^{p,q}) = Ker(d_r^{p,q})`, `B_{r+1}(E_2^{p,q}) = Im(d_r^{p-r, q+r-1})`, so that

```text
  B_{r+1}(E_2^{p,q}) ⊂ Z_{r+1}(E_2^{p,q}) ⊂ E_2^{p,q}.
```

c) A family of isomorphisms `α_r^{p,q} : Z_r(E_2^{p,q})/B_r(E_2^{p,q}) ⥲ E_r^{p,q}`.

One then defines, for `k ≥ r + 1`, by induction on `k`, the subobjects `B_k(E_2^{p,q})` and `Z_k(E_2^{p,q})` as the
inverse images, under the canonical morphism `E_2^{p,q} → E_2^{p,q}/B_r(E_2^{p,q})`, of the subobjects of this quotient
identified by `α_r^{p,q}` with the subobjects `B_k(E_r^{p,q})` and `Z_k(E_r^{p,q})` respectively. It is clear that one
then has, up to isomorphism,

```text
  Z_k(E_2^{p,q})/B_k(E_2^{p,q}) = E_k^{p,q}                                    (11.1.1.1)
```

for `k ≥ r + 1`, and, if we further set `B_1(E_2^{p,q}) = 0` and `Z_1(E_2^{p,q}) = E_2^{p,q}`, one has the inclusion
relations

```text
  0 = B_1(E_2^{p,q}) ⊂ B_2(E_2^{p,q}) ⊂ B_3(E_2^{p,q}) ⊂ …
       … ⊂ Z_3(E_2^{p,q}) ⊂ Z_2(E_2^{p,q}) ⊂ Z_1(E_2^{p,q}) = E_2^{p,q}.       (11.1.1.2)
```

The remaining data of `E` are then:

d) Two subobjects `B_∞(E_2^{p,q})` and `Z_∞(E_2^{p,q})` of `E_2^{p,q}` such that one has
`B_∞(E_2^{p,q}) ⊂ Z_∞(E_2^{p,q})` and, for every `k ≥ 2`,

```text
  B_k(E_2^{p,q}) ⊂ B_∞(E_2^{p,q})    and    Z_∞(E_2^{p,q}) ⊂ Z_k(E_2^{p,q}).
```

One sets

```text
  E_∞^{p,q} = Z_∞(E_2^{p,q})/B_∞(E_2^{p,q}).                                   (11.1.1.3)
```

<!-- original page 368 -->

e) A family `(E^n)` of objects of `𝒞`, each equipped with a decreasing filtration `(F^p(E^n))_{p ∈ ℤ}`. As usual we
denote by `gr(E^n)` the graded object associated to the filtered object `E^n`, the direct sum of the
`gr_p(E^n) = F^p(E^n)/F^{p+1}(E^n)`.

f) For every pair `(p, q) ∈ ℤ × ℤ`, an isomorphism `β^{p,q} : E_∞^{p,q} ⥲ gr_p(E^{p+q})`.

The family `(E^n)`, without the filtrations, is called the *abutment* of the spectral sequence `E`.

Suppose either that the category `𝒞` admits infinite direct sums, or that for every `r ≥ 2` and every `n ∈ ℤ`, the pairs
`(p, q)` such that `p + q = n` and `E_r^{p,q} ≠ 0` are finite in number (it suffices that this hold for `r = 2`). Then
the `E_r^{(n)} = ⊕_{p+q=n} E_r^{p,q}` are defined, and denoting by `d_r^{(n)}` the morphism `E_r^{(n)} → E_r^{(n+1)}`
whose restriction to `E_r^{p,q}` is `d_r^{p,q}` for each pair `(p, q)` with `p + q = n`, one has
`d_r^{(n+1)} ∘ d_r^{(n)} = 0`; in other words, `(E_r^{(n)})_{n ∈ ℤ}` is a complex `E_r^{(•)}` in `𝒞`, with derivation
operator of degree `+1`, and it follows from c) that `H^•(E_r^{(•)})` is isomorphic to `E_{r+1}^{(•)}` for every
`r ≥ 2`.

**11.1.2.**

<!-- label: 0_III.11.1.2 -->

A *morphism* `u : E → E'` from a spectral sequence `E` to a spectral sequence `E' = (E_r'^{p,q}, E'^n)` consists of
systems of morphisms `u_r^{p,q} : E_r^{p,q} → E_r'^{p,q}`, `u^n : E^n → E'^n`, the `u^n` being compatible with the
filtrations of `E^n` and `E'^n`, the diagrams

```text
                          d_r^{p,q}
                E_r^{p,q}    →    E_r^{p+r, q-r+1}
                    ↓                      ↓
                  u_r^{p,q}            u_r^{p+r, q-r+1}
                    ↓                      ↓
                E_r'^{p,q}   →    E_r'^{p+r, q-r+1}
                          d_r'^{p,q}
```

being commutative; moreover, on passing to quotients, `u_r^{p,q}` induces a morphism
`ū_r^{p,q} : Z_{r+1}(E_2^{p,q})/B_{r+1}(E_2^{p,q}) → Z_{r+1}(E_2'^{p,q})/B_{r+1}(E_2'^{p,q})`, and one must have
`α_{r+1}'^{p,q} ∘ ū_r^{p,q} = u_{r+1}^{p,q} ∘ α_{r+1}^{p,q}`; finally, one must have
`u_2^{p,q}(B_∞(E_2^{p,q})) ⊂ B_∞(E_2'^{p,q})` and `u_2^{p,q}(Z_∞(E_2^{p,q})) ⊂ Z_∞(E_2'^{p,q})`; on passing to
quotients, `u_2^{p,q}` then gives a morphism `u_∞^{p,q} : E_∞^{p,q} → E_∞'^{p,q}`, and the diagram

```text
                          u_∞^{p,q}
                  E_∞^{p,q}   →   E_∞'^{p,q}
                       ↓                ↓
                    β^{p,q}          β'^{p,q}
                       ↓                ↓
                  gr_p(E^{p+q})  →  gr_p(E'^{p+q})
                          gr_p(u^{p+q})
```

must be commutative.

The preceding definitions show, by induction on `r`, that if the `u_2^{p,q}` are *isomorphisms*, then so are the
`u_r^{p,q}` for `r ≥ 2`; if one further knows that `u_2^{p,q}(B_∞(E_2^{p,q})) = B_∞(E_2'^{p,q})` and
`u_2^{p,q}(Z_∞(E_2^{p,q})) = Z_∞(E_2'^{p,q})` and that the `u^n` are isomorphisms, then one can conclude that `u` is an
isomorphism.

<!-- original page 369 -->

**11.1.3.**

<!-- label: 0_III.11.1.3 -->

Recall that if `(F^p(X))_{p ∈ ℤ}` is a (decreasing) filtration of an object `X ∈ 𝒞`, the filtration is said to be
*separated* if `inf_p (F^p(X)) = 0`, *discrete* if there exists `p` such that `F^p(X) = 0`, *exhaustive* (or
*co-separated*) if `sup_p (F^p(X)) = X`, *co-discrete* if there exists `p` such that `F^p(X) = X`.

We shall say that a spectral sequence `E = (E_r^{p,q}, E^n)` is *weakly convergent* if one has
`B_∞(E_2^{p,q}) = sup_k(B_k(E_2^{p,q}))`, `Z_∞(E_2^{p,q}) = inf_k(Z_k(E_2^{p,q}))` (in other words, the objects
`B_∞(E_2^{p,q})` and `Z_∞(E_2^{p,q})` are determined by data a) through c) of the spectral sequence `E`). We shall say
that the spectral sequence `E` is *regular* if it is weakly convergent and moreover:

1° For every pair `(p, q)`, the decreasing sequence `(Z_k(E_2^{p,q}))_{k ≥ 2}` is stationary; the hypothesis that `E` is
weakly convergent then implies `Z_∞(E_2^{p,q}) = Z_k(E_2^{p,q})` for `k` sufficiently large (depending on `p` and `q`).

2° For every `n`, the filtration `(F^p(E^n))_{p ∈ ℤ}` of `E^n` is discrete and exhaustive.

One says that the spectral sequence `E` is *co-regular* if it is weakly convergent and moreover:

3° For every pair `(p, q)`, the increasing sequence `(B_k(E_2^{p,q}))_{k ≥ 2}` is stationary, which entails
`B_∞(E_2^{p,q}) = B_k(E_2^{p,q})`, and consequently `E_∞^{p,q} = inf_k E_k^{p,q}`.

4° For every `n`, the filtration of `E^n` is co-discrete.

Finally, one says that `E` is *biregular* if it is both regular and co-regular; in other words, if the following
conditions hold:

a) For every pair `(p, q)`, the sequences `(B_k(E_2^{p,q}))_{k ≥ 2}` and `(Z_k(E_2^{p,q}))_{k ≥ 2}` are stationary, and
one has `B_∞(E_2^{p,q}) = B_k(E_2^{p,q})` and `Z_∞(E_2^{p,q}) = Z_k(E_2^{p,q})` for `k` sufficiently large (which
entails `E_∞^{p,q} = E_k^{p,q}`).

b) For every `n`, the filtration `(F^p(E^n))_{p ∈ ℤ}` is *discrete* and co-discrete (which one also expresses by saying
that it is *finite*).

The spectral sequences defined in `(T, 2.4)` are thus the biregular spectral sequences.

**11.1.4.**

<!-- label: 0_III.11.1.4 -->

Suppose that in the category `𝒞` filtered inductive limits exist and that the functor `lim_→` is exact (which is
equivalent to saying that axiom AB 5) of `(T, 1.5)` is verified (cf. `T, 1.8`)). The condition that the filtration
`(F^p(X))_{p ∈ ℤ}` of an object `X ∈ 𝒞` be exhaustive then also reads `lim_{p → -∞} F^p(X) = X`. If a spectral sequence
`E` is weakly convergent, one has `B_∞(E_2^{p,q}) = lim_{k → ∞} B_k(E_2^{p,q})`; if moreover `u : E → E'` is a morphism
of `E` into a weakly convergent spectral sequence `E'` of `𝒞`, one has `u_2^{p,q}(B_∞(E_2^{p,q})) = B_∞(E_2'^{p,q})` by
exactness of `lim_→`. Moreover:

**Proposition (11.1.5).**

<!-- label: 0_III.11.1.5 -->

Let `𝒞` be an abelian category in which filtered inductive limits are exact, let `E`, `E'` be two regular spectral
sequences in `𝒞`, and let `u : E → E'` be a morphism of spectral sequences. If the `u_2^{p,q}` are isomorphisms, then so
is `u`.

**Proof.** We already know `(11.1.2)` that the `u_r^{p,q}` are isomorphisms and that

```text
  u_2^{p,q}(B_∞(E_2^{p,q})) = B_∞(E_2'^{p,q});
```

<!-- original page 370 -->

the hypothesis that `E` and `E'` are regular also implies `u_2^{p,q}(Z_∞(E_2^{p,q})) = Z_∞(E_2'^{p,q})`, and since
`u_2^{p,q}` is an isomorphism, so is `u_∞^{p,q}`; one therefore concludes that `gr_p(u^{p+q})` is also an isomorphism.
But since the filtrations of the `E^n` and the `E'^n` are discrete and exhaustive, this entails that the `u^n` are also
isomorphisms (Bourbaki, _Alg. comm._, chap. III, § 2, n° 8, th. 1).

**11.1.6.**

<!-- label: 0_III.11.1.6 -->

It follows from `(11.1.1.2)` and from definition `(11.1.1.3)` that if, in a spectral sequence `E`, one has
`E_r^{p,q} = 0`, then one has `E_k^{p,q} = 0` for `k ≥ r` and `E_∞^{p,q} = 0`. One says that a spectral sequence is
*degenerate* if there exists an integer `r ≥ 2` and, for every integer `n ∈ ℤ`, an integer `q(n)` such that
`E_r^{n-q, q} = 0` for every `q ≠ q(n)`. From the preceding remark one first deduces that one also has
`E_k^{n-q, q} = 0` for `k ≥ r` (including `k = ∞`) and `q ≠ q(n)`. Moreover, the definition of `E_{r+1}^{p,q}` shows
that one has `E_{r+1}^{n-q(n), q(n)} = E_r^{n-q(n), q(n)}`; if `E` is weakly convergent, one therefore also has
`E_∞^{n-q(n), q(n)} = E_r^{n-q(n), q(n)}`; in other words, for every `n ∈ ℤ`, `gr_p(E^n) = 0` for `p ≠ q(n)` and
`gr_{q(n)}(E^n) = E_r^{n-q(n), q(n)}`. If moreover the filtration of `E^n` is discrete and exhaustive, the sequence `E`
is regular and one has `E^n = E_r^{n-q(n), q(n)}` up to isomorphism.

**11.1.7.**

<!-- label: 0_III.11.1.7 -->

Suppose that in the category `𝒞` filtered inductive limits exist and are exact, and let `(E_λ, u_{λμ})` be an inductive
system (over a filtered index set) of spectral sequences in `𝒞`. Then the *inductive limit of this inductive system
exists in the additive category of spectral sequences of objects of `𝒞`*: to see this it suffices to define `E_r^{p,q}`,
`d_r^{p,q}`, `α_r^{p,q}`, `B_k(E_2^{p,q})`, `Z_k(E_2^{p,q})`, `E^n`, `F^p(E^n)` and `β^{p,q}` as the respective
inductive limits of `E_{r,λ}^{p,q}`, `d_{r,λ}^{p,q}`, `α_{r,λ}^{p,q}`, `B_k(E_{2,λ}^{p,q})`, `Z_k(E_{2,λ}^{p,q})`,
`E_λ^n`, `F^p(E_λ^n)` and `β_λ^{p,q}`; the verification of the conditions of `(11.1.1)` follows from the exactness of
the functor `lim_→` in `𝒞`.

**Remark (11.1.8).**

<!-- label: 0_III.11.1.8 -->

Suppose that the category `𝒞` is the category of `A`-modules over a Noetherian ring `A` (resp. over a ring `A`). Then
the definitions of `(11.1.1)` show that if, for a given `r`, the `E_r^{p,q}` are `A`-modules of finite type (resp. of
finite length), then so are all the modules `E_s^{p,q}` for `s ≥ r`, as well as the `E_∞^{p,q}`. If moreover the
filtration of the abutment `(E^n)` is discrete and co-discrete for every `n`, one concludes that each of the `E^n` is
also an `A`-module of finite type (resp. of finite length).

**11.1.9.**

<!-- label: 0_III.11.1.9 -->

We shall have to consider conditions ensuring that a spectral sequence `E` is biregular "uniformly" in `p + q = n`. We
shall then use the following lemma:

**Lemma (11.1.10).**

<!-- label: 0_III.11.1.10 -->

Let `(E_r^{p,q})` be a family of objects of `𝒞` linked by data a), b), c) of `(11.1.1)`. For a fixed integer `n`, the
following properties are equivalent:

a) There exists an integer `r(n)` such that for `r ≥ r(n)`, `p + q = n` or `p + q = n − 1`, the morphisms `d_r^{p,q}`
are all zero.

b) There exists an integer `r(n)` such that for `p + q = n` or `p + q = n + 1`, one has
`B_s(E_2^{p,q}) = B_r(E_2^{p,q})` for `s ≥ r ≥ r(n)`.

c) There exists an integer `r(n)` such that for `p + q = n` or `p + q = n − 1`, one has
`Z_s(E_2^{p,q}) = Z_r(E_2^{p,q})` for `s ≥ r ≥ r(n)`.

d) There exists an integer `r(n)` such that for `p + q = n`, one has `B_s(E_2^{p,q}) = B_r(E_2^{p,q})` and
`Z_s(E_2^{p,q}) = Z_r(E_2^{p,q})` for `s ≥ r ≥ r(n)`.

<!-- original page 371 -->

**Proof.** Indeed, by conditions a), b), c) of `(11.1.1)`, to say that `Z_{r+1}(E_2^{p,q}) = Z_r(E_2^{p,q})` is
equivalent to saying that `d_r^{p,q} = 0`, and to say that `B_{r+1}(E_2^{p+r, q-r+1}) = B_r(E_2^{p+r, q-r+1})` is also
equivalent to saying that `d_r^{p,q} = 0`; the lemma follows at once from this remark.

### 11.2. The spectral sequence of a filtered complex

**11.2.1.**

<!-- label: 0_III.11.2.1 -->

Given an abelian category `𝒞`, we shall use notation such as `K^•` for complexes `(K^i)_{i ∈ ℤ}` of objects of `𝒞` in
which the derivation operator is of degree `+1`, and notation such as `K_•` for complexes `(K_i)_{i ∈ ℤ}` of objects of
`𝒞` in which the derivation operator is of degree `−1`. To any complex `K^• = (K^i)` whose derivation operator `d` is of
degree `+1`, one can associate a complex `K_•' = (K_i')` by setting `K_i' = K^{-i}`, the derivation operator
`K_i' → K_{i-1}'` being the operator `d : K^{-i} → K^{-i+1}`; and conversely, which will allow us, according to
circumstances, to consider one type of complex or the other and to translate every result for one type into a result for
the other. We shall denote similarly by notation such as `K^{•,•} = (K^{i,j})` (resp. `K_{•,•} = (K_{i,j})`)
*bicomplexes* of objects of `𝒞` in which the two derivation operators are of degree `+1` (resp. `−1`); one again passes
from one type to the other by changing the signs of the indices, and one has analogous notation and remarks for
arbitrary multicomplexes. The notation `K^•` or `K_•` will also be used for graded objects of `𝒞`, of type `ℤ`, which
are not necessarily complexes (or which one may consider as such with zero derivation operators); for instance, we shall
write `H^•(K^•) = (H^i(K^•))_{i ∈ ℤ}` for the cohomology of a complex `K^•` whose derivation operator is of degree `+1`,
and `H_•(K_•) = (H_i(K_•))_{i ∈ ℤ}` for the homology of a complex `K_•` whose derivation operator is of degree `−1`;
when one passes from `K^•` to `K_•'` by the operation described above, one has `H_i(K_•') = H^{-i}(K^•)`.

Recall in this connection that for a complex `K^•` (resp. `K_•`), we shall generally write
`Z^i(K^•) = Ker(K^i → K^{i+1})` ("object of cocycles") and `B^i(K^•) = Im(K^{i-1} → K^i)` ("object of coboundaries")
(resp. `Z_i(K_•) = Ker(K_i → K_{i-1})` ("object of cycles") and `B_i(K_•) = Im(K_{i+1} → K_i)` ("object of
boundaries")), so that `H^i(K^•) = Z^i(K^•)/B^i(K^•)` (resp. `H_i(K_•) = Z_i(K_•)/B_i(K_•)`).

If `K^• = (K^i)` (resp. `K_• = (K_i)`) is a complex in `𝒞`, and `T : 𝒞 → 𝒞'` a functor from `𝒞` to an abelian category
`𝒞'`, we shall denote by `T(K^•)` (resp. `T(K_•)`) the complex `(T(K^i))` (resp. `(T(K_i))`) in `𝒞'`.

We do not return to the definition of `∂`-functors `(T, 2.1)`, except to point out that we shall also say *`∂`-functor*
in place of *`∂^*`-functor* when the morphism `∂` lowers the degree by one unit; the context should make this clear when
there could be doubt.

Finally, we shall say that a graded object `(A^i)_{i ∈ ℤ}` of `𝒞` is *bounded below* (resp. *bounded above*) if there
exists `i_0` such that `A^i = 0` for `i < i_0` (resp. `i > i_0`).

**11.2.2.**

<!-- label: 0_III.11.2.2 -->

Let `K^•` be a complex in `𝒞` whose derivation operator `d` is of degree `+1`, and suppose it equipped with a
*filtration* `F(K^•) = (F^p(K^•))_{p ∈ ℤ}` formed of graded subobjects of `K^•`,

<!-- original page 372 -->

in other words `F^p(K^•) = (K^i ∩ F^p(K^•))_{i ∈ ℤ}`; moreover, we assume that `d(F^p(K^•)) ⊂ F^p(K^•)` for every
`p ∈ ℤ`. We now briefly recall how one functorially defines a spectral sequence `E(K^•)` from `K^•` `(M, XV, 4` and
`G, I, 4.3)`. For `r ≥ 2`, the canonical morphism `F^p(K^•)/F^{p+r}(K^•) → F^p(K^•)/F^{p+1}(K^•)` defines a morphism in
cohomology

```text
  H^{p+q}(F^p(K^•)/F^{p+r}(K^•)) → H^{p+q}(F^p(K^•)/F^{p+1}(K^•)).
```

One denotes by `Z_r^{p,q}(K^•)` the image of this morphism. Similarly, from the exact sequence

```text
  0 → F^p(K^•)/F^{p+1}(K^•) → F^{p-r+1}(K^•)/F^{p+1}(K^•) → F^{p-r+1}(K^•)/F^p(K^•) → 0
```

one deduces, by the long exact sequence of cohomology, a morphism

```text
  H^{p+q-1}(F^{p-r+1}(K^•)/F^p(K^•)) → H^{p+q}(F^p(K^•)/F^{p+1}(K^•))
```

and one denotes by `B_r^{p,q}(K^•)` the image of this morphism; one shows that `B_r^{p,q}(K^•) ⊂ Z_r^{p,q}(K^•)` and one
sets `E_r^{p,q}(K^•) = Z_r^{p,q}(K^•)/B_r^{p,q}(K^•)`; we shall not specify the definitions of the `d_r^{p,q}` or the
`α_r^{p,q}`.

We note here that all the `Z_r^{p,q}(K^•)` and `B_r^{p,q}(K^•)`, for `p`, `q` fixed, are subobjects of the same object
`H^{p+q}(F^p(K^•)/F^{p+1}(K^•))`, which one denotes `Z_1^{p,q}(K^•)`; one sets `B_1^{p,q}(K^•) = 0`, so that the
preceding definitions for `Z_r^{p,q}(K^•)` and `B_r^{p,q}(K^•)` also apply for `r = 1`; one further sets
`E_1^{p,q}(K^•) = Z_1^{p,q}(K^•)`. One also defines the `d_1^{p,q}` and `α_1^{p,q}` so that the conditions of `(11.1.1)`
are satisfied for `r = 1`. One defines on the other hand the subobjects `Z_∞^{p,q}(K^•)`, image of the morphism

```text
  H^{p+q}(F^p(K^•)) → H^{p+q}(F^p(K^•)/F^{p+1}(K^•)) = E_1^{p,q}(K^•)
```

and `B_∞^{p,q}(K^•)`, image of the morphism

```text
  H^{p+q-1}(K^•/F^p(K^•)) → H^{p+q}(F^p(K^•)/F^{p+1}(K^•)) = E_1^{p,q}(K^•)
```

obtained as above from a long exact sequence of cohomology. One takes for `Z_∞(E_2^{p,q}(K^•))` and
`B_∞(E_2^{p,q}(K^•))` the canonical images in `E_2^{p,q}(K^•)` of `Z_∞^{p,q}(K^•)` and `B_∞^{p,q}(K^•)`.

Finally, one denotes by `F^p(H^n(K^•))` the image in `H^n(K^•)` of the morphism `H^n(F^p(K^•)) → H^n(K^•)` coming from
the canonical injection `F^p(K^•) → K^•`; by the long exact sequence of cohomology, it is also the kernel of the
morphism `H^n(K^•) → H^n(K^•/F^p(K^•))`. One thus defines a filtration on `E^n(K^•) = H^n(K^•)`; we shall not give the
definition of the isomorphisms `β^{p,q}` here either.

**11.2.3.**

<!-- label: 0_III.11.2.3 -->

The functorial character of `E(K^•)` is to be understood as follows: given two *filtered* complexes `K^•`, `K'^•` of `𝒞`
and a morphism of complexes `u : K^• → K'^•` *compatible with the filtrations*, one deduces from it in an obvious way
the morphisms `u_r^{p,q}` (for `r ≥ 1`) and `u^n`, and one shows that these morphisms are compatible with the
`d_r^{p,q}`, `α_r^{p,q}` and `β^{p,q}` in the sense of `(11.1.2)`, so that they indeed define a morphism
`E(u) : E(K^•) → E(K'^•)` of spectral sequences. Moreover, one shows that if `u` and `v` are morphisms `K^• → K'^•` of
the preceding type, *homotopic of order `≤ k`*, then `u_r^{p,q} = v_r^{p,q}` for `r > k` and `u^n = v^n` for every `n`
`(M, XV, 3.1)`.

<!-- original page 373 -->

**11.2.4.**

<!-- label: 0_III.11.2.4 -->

Suppose that in `𝒞` filtered inductive limits are exact. Then, if the filtration `(F^p(K^•))` of `K^•` is exhaustive, so
is the filtration `(F^p(H^n(K^•)))` for every `n`, since by hypothesis `K^• = lim_{p → -∞} F^p(K^•)` and the hypothesis
on `𝒞` implies that cohomology commutes with inductive limits. Moreover, for the same reason, one has
`B_∞(E_2^{p,q}(K^•)) = sup_k B_k(E_2^{p,q}(K^•))`. One says that the filtration `(F^p(K^•))` of `K^•` is *regular* if
for every `n` there exists an integer `u(n)` such that `H^n(F^p(K^•)) = 0` for `p > u(n)`. This holds in particular when
the filtration of `K^•` is discrete. When the filtration of `K^•` is regular and exhaustive, and filtered inductive
limits in `𝒞` are exact, one shows `(M, XV, 4)` that the spectral sequence `E(K^•)` is regular.

### 11.3. The spectral sequences of a bicomplex

**11.3.1.**

<!-- label: 0_III.11.3.1 -->

As regards the conventions on bicomplexes, we follow those of `(T, 2.4)` rather than those of `(M)`, the two derivations
`d'`, `d″` (of degree `+1`) of such a bicomplex `K^{•,•} = (K^{i,j})` being therefore *assumed to commute*. Suppose that
*one of the two following conditions* is verified: 1° infinite direct sums exist in `𝒞`; 2° for every `n ∈ ℤ`, there are
only finitely many pairs `(p, q)` such that `p + q = n` and `K^{p,q} ≠ 0`. Then the bicomplex `K^{•,•}` defines a
(simple) complex `(K^{(n)})_{n ∈ ℤ}` with `K^{(n)} = ⊕_{i+j=n} K^{i,j}`, the derivation operator `d` (of degree `+1`) of
this complex being given by `dx = d'x + (−1)^i d″x` for `x ∈ K^{i,j}`. *Whenever in what follows we speak of the
(simple) complex defined by a bicomplex `K^{•,•}`, it will always be understood that one of the preceding conditions is
satisfied.* One adopts analogous conventions for multicomplexes.

We denote by `K^{i,•}` (resp. `K^{•,j}`) the simple complex `(K^{i,j})_{j ∈ ℤ}` (resp. `(K^{i,j})_{i ∈ ℤ}`), and by
`Z_{II}^q(K^{i,•})`, `B_{II}^q(K^{i,•})`, `H_{II}^q(K^{i,•})` (resp. `Z_I^p(K^{•,j})`, `B_I^p(K^{•,j})`,
`H_I^p(K^{•,j})`) its `q`th (resp. `p`th) objects of cocycles, coboundaries, and cohomology respectively; the derivation
`d' : K^{i,•} → K^{i+1,•}` is a morphism of complexes, which therefore gives an operator on the cocycles, coboundaries,
and cohomology,

```text
  d' : Z_{II}^q(K^{i,•}) → Z_{II}^q(K^{i+1,•})
  d' : B_{II}^q(K^{i,•}) → B_{II}^q(K^{i+1,•})
  d' : H_{II}^q(K^{i,•}) → H_{II}^q(K^{i+1,•})
```

and it is clear that for these operators, `(Z_{II}^q(K^{i,•}))_{i ∈ ℤ}`, `(B_{II}^q(K^{i,•}))_{i ∈ ℤ}`, and
`(H_{II}^q(K^{i,•}))_{i ∈ ℤ}` are complexes; we shall denote the complex `(H_{II}^q(K^{i,•}))_{i ∈ ℤ}` by
`H_{II}^q(K^{•,•})`, and its `p`th objects of cocycles, coboundaries, and cohomology by `Z_I^p(H_{II}^q(K^{•,•}))`,
`B_I^p(H_{II}^q(K^{•,•}))`, and `H_I^p(H_{II}^q(K^{•,•}))`. One defines similarly the complexes `H_I^p(K^{•,•})` and
their objects of cohomology `H_{II}^q(H_I^p(K^{•,•}))`. Recall on the other hand that `H^n(K^{•,•})` denotes the `n`th
object of cohomology of the (simple) complex defined by `K^{•,•}`.

**11.3.2.**

<!-- label: 0_III.11.3.2 -->

On the complex defined by a bicomplex `K^{•,•}`, one may consider two *canonical filtrations* `(F_I^p(K^{•,•}))` and
`(F_{II}^p(K^{•,•}))` given by

```text
  F_I^p(K^{•,•}) = (⊕_{i+j=n, i ≥ p} K^{i,j})_{n ∈ ℤ},   F_{II}^p(K^{•,•}) = (⊕_{i+j=n, j ≥ p} K^{i,j})_{n ∈ ℤ}.   (11.3.2.1)
```

<!-- original page 374 -->

which are by definition graded subobjects of the (simple) complex defined by `K^{•,•}`, and thus make this complex into
a *filtered complex*; moreover, it is clear that these filtrations are *exhaustive and separated*.

To each of these filtrations there corresponds a spectral sequence `(11.2.2)`; we shall denote by `'E(K^{•,•})` and
`″E(K^{•,•})` the spectral sequences corresponding to `(F_I^p(K^{•,•}))` and `(F_{II}^p(K^{•,•}))` respectively, called
the *spectral sequences of the bicomplex `K^{•,•}`*, both having as abutment the cohomology `(H^n(K^{•,•}))`. One shows
moreover `(M, XV, 6)` that

```text
  'E_2^{p,q}(K^{•,•}) = H_I^p(H_{II}^q(K^{•,•})),    ″E_2^{p,q}(K^{•,•}) = H_{II}^p(H_I^q(K^{•,•})).   (11.3.2.2)
```

Any morphism `u : K^{•,•} → K'^{•,•}` of bicomplexes is ipso facto compatible with the filtrations of the same type on
`K^{•,•}` and `K'^{•,•}`, and thus defines a morphism for each of the two spectral sequences; moreover, two homotopic
morphisms define a homotopy of order `≤ 1` of the corresponding (simple) filtered complexes, hence the same morphism for
each of the two spectral sequences `(M, XV, 6.1)`.

**Proposition (11.3.3).**

<!-- label: 0_III.11.3.3 -->

Let `K^{•,•} = (K^{i,j})` be a bicomplex in an abelian category `𝒞`.

(i) If there exist `i_0` and `j_0` such that `K^{i,j} = 0` for `i < i_0` or `j < j_0` (resp. `i > i_0` or `j > j_0`),
the two spectral sequences `'E(K^{•,•})` and `″E(K^{•,•})` are biregular.

(ii) If there exist `i_0` and `i_1` such that `K^{i,j} = 0` for `i < i_0` or `i > i_1` (resp. if there exist `j_0` and
`j_1` such that `K^{i,j} = 0` for `j < j_0` or `j > j_1`), the two spectral sequences `'E(K^{•,•})` and `″E(K^{•,•})`
are biregular.

Suppose moreover that in `𝒞` filtered inductive limits exist and are exact. Then:

(iii) If there exists `i_0` such that `K^{i,j} = 0` for `i > i_0` (resp. if there exists `j_0` such that `K^{i,j} = 0`
for `j < j_0`), the sequence `'E(K^{•,•})` is regular.

(iv) If there exists `i_0` such that `K^{i,j} = 0` for `i < i_0` (resp. if there exists `j_0` such that `K^{i,j} = 0`
for `j > j_0`), the sequence `″E(K^{•,•})` is regular.

**Proof.** The proposition follows at once from the definitions `(11.1.3)` and from `(11.2.4)`, together with the
following observations concerning the filtration `F_I` (and the analogous observations one deduces for `F_{II}` by
exchanging the roles of the two indices in `K^{•,•}`):

1° If there exists `i_0` such that `K^{i,j} = 0` for `i > i_0`, the filtration `F_I(K^{•,•})` is *discrete*.

2° If there exists `i_0` such that `K^{i,j} = 0` for `i < i_0`, the filtration `F_I(K^{•,•})` is *co-discrete*. One
deduces at once that the same holds for the corresponding filtration `F_I(H^n(K^{•,•}))` for every `n`; moreover, the
definition of `B_r^{p,q}` corresponding to the filtration `F_I(K^{•,•})` `(11.2.2)` shows that for every pair `(p, q)`,
the sequence `(B_r^{p,q})_{r ≥ 2}` is stationary.

3° If there exists `j_0` such that `K^{i,j} = 0` for `j < j_0`, one has

```text
  F_I^{p+r}(K^{•,•}) ∩ (⊕_{i+j=n} K^{i,j}) = 0
```

whenever `p + r + j_0 > n`, hence `Z_r^{p,q} = Z_∞(E_2^{p,q})` for `r > q − j_0 + 1`; on the other hand,
`H^n(F_I^p(K^{•,•})) = 0` for `p > n − j_0 + 1`.

4° If there exists `j_0` such that `K^{i,j} = 0` for `j > j_0`, one has

```text
  F_I^{p-r+1}(K^{•,•}) ∩ (⊕_{i+j=n} K^{i,j}) = ⊕_{i+j=n} K^{i,j}
```

<!-- original page 375 -->

whenever `p − r + 1 + j_0 < n`, hence `B_r^{p,q} = B_∞(E_2^{p,q})` for `r < j_0 − q + 1`; on the other hand,
`H^n(F_I^p(K^{•,•})) = H^n(K^{•,•})` for `p + j_0 < n − 1`.

**11.3.4.**

<!-- label: 0_III.11.3.4 -->

Suppose that the bicomplex `K^{•,•} = (K^{i,j})` is such that `K^{i,j} = 0` for `i < 0` or `j < 0`. It is known that one
can then define for every `p ∈ ℤ` a canonical "edge homomorphism"

```text
  'E_2^{p,0}(K^{•,•}) → H^p(K^{•,•})                                            (11.3.4.1)
```

`(M, XV, 6)`. We briefly recall that this is due, on the one hand, to the fact that one has `Z_r^{p,0} = Z_∞(E_2^{p,0})`
in the spectral sequence `'E(K^{•,•})` for `2 ≤ r ≤ +∞`, and, on the other hand, to the fact that
`H^p(F_I^{p+1}(K^{•,•})) = 0`, so that the isomorphism `β^{p,0} : 'E_∞^{p,0} ⥲ H^p(F_I^p)/H^p(F_I^{p+1})` gives a
homomorphism `'E_∞^{p,0} → H^p(F_I^p(K^{•,•})) → H^p(K^{•,•})`; the equality of all the `Z_r^{p,0}` then makes it
possible to define canonical homomorphisms `'E_r^{p,0} → 'E_s^{p,0}` for `r ≤ s`, in particular a homomorphism
`'E_2^{p,0} → 'E_∞^{p,0}`, whence by composition the edge homomorphism `'E_2^{p,0} → H^p(K^{•,•})`; moreover, one
verifies at once that, to the class mod. `B_∞^{p,0}` of an element `z ∈ Z_{II}^0(K^{•,•}) ⊂ K^{p,0}` such that
`d'z = 0`, the edge homomorphism so defined associates in `'E_∞^{p,0}` the class of `z` mod. `B_∞^{p,0}`, and then, to
this last, the cohomology class of `z` in `H^p(K^{•,•})`. One thus sees finally that the edge homomorphism `(11.3.4.1)`
comes, by passage to cohomology, from the canonical injection `Z_{II}^0(K^{•,•}) → K^{•,•}` (where `K^{•,•}` is
considered as a simple complex). One similarly interprets the edge homomorphism

```text
  ″E_2^{p,0}(K^{•,•}) → H^p(K^{•,•})                                            (11.3.4.2)
```

as coming from the canonical injection `Z_I^0(K^{•,•}) → K^{•,•}`.

**11.3.5.**

<!-- label: 0_III.11.3.5 -->

Let now `K_{•,•} = (K_{i,j})` be a bicomplex in `𝒞` whose two derivation operators are of degree `−1`. We shall then
write `K_{i,•}` (resp. `K_{•,j}`) for the simple complex `(K_{i,j})_{j ∈ ℤ}` (resp. `(K_{i,j})_{i ∈ ℤ}`),
`H_p^{II}(K_{i,•})` (resp. `H_p^{I}(K_{•,j})`) for its `p`th object of homology, `H_p^{II}(K_{•,•})` (resp.
`H_p^{I}(K_{•,•})`) for the complex `(H_p^{II}(K_{i,•}))_{i ∈ ℤ}` (resp. `(H_p^{I}(K_{•,j}))_{j ∈ ℤ}`),
`H_q^{I}(H_p^{II}(K_{•,•}))` (resp. `H_q^{II}(H_p^{I}(K_{•,•}))`) for its `q`th object of homology; analogous notation
for the objects of cycles and boundaries; finally, `H_n(K_{•,•})` will denote (when it exists) the `n`th object of
homology of the simple complex (with derivation operator of degree `−1`) defined by `K_{•,•}`.

Let `K^{•,•} = (K^{i,j})` with `K^{i,j} = K_{-i,-j}` be the bicomplex with derivation operators of degree `+1`
associated to `K_{•,•}`; by definition, the spectral sequences of `K_{•,•}` are those of `K^{•,•}`, which one writes
`'E(K_{•,•})` and `″E(K_{•,•})`, where one changes the notation, however, by setting

```text
  'E_{p,q}^r(K_{•,•}) = 'E_r^{-p,-q}(K^{•,•}),    ″E_{p,q}^r(K_{•,•}) = ″E_r^{-p,-q}(K^{•,•})
```

for `2 ≤ r ≤ ∞`. With this notation, one has

```text
  'E_{p,q}^2(K_{•,•}) = H_p^I(H_q^{II}(K_{•,•})),    ″E_{p,q}^2(K_{•,•}) = H_p^{II}(H_q^I(K_{•,•})).
```

To avoid sign errors, it will generally be preferable, for the relations between these spectral sequences and their
abutment, to return to the complex `K^{•,•}`. Let us note nonetheless the criteria corresponding to `(11.3.3)`:

**11.3.6.**

<!-- label: 0_III.11.3.6 -->

The spectral sequences `'E(K_{•,•})` and `″E(K_{•,•})` are biregular in the following cases: a) There exist `i_0` and
`j_0` such that `K_{i,j} = 0` for `i > i_0` or for `j > j_0` (resp. for `i < i_0`

<!-- original page 376 -->

or for `j < j_0`); b) There exist `i_0` and `i_1` such that `K_{i,j} = 0` for `i < i_0` and `i > i_1`; c) There exist
`j_0` and `j_1` such that `K_{i,j} = 0` for `j < j_0` and `j > j_1`.

The sequence `'E(K_{•,•})` is regular if there exists `i_0` such that `K_{i,j} = 0` for `i < i_0`, or if there exists
`j_0` such that `K_{i,j} = 0` for `j > j_0`.

The sequence `″E(K_{•,•})` is regular if there exists `i_0` such that `K_{i,j} = 0` for `i > i_0`, or if there exists
`j_0` such that `K_{i,j} = 0` for `j < j_0`.

### 11.4. Hypercohomology of a functor with respect to a complex `K^•`

**11.4.1.**

<!-- label: 0_III.11.4.1 -->

Let `𝒞` be an abelian category; recall that one calls a *right resolution* (or *cohomological resolution*) of an object
`A` of `𝒞` a complex of objects of `𝒞`, whose derivation operator is of degree `+1`,

```text
  0 → L^0 → L^1 → L^2 → …
```

equipped with a morphism `ε : A → L^0` called the *augmentation* of the resolution (and which one can consider as a
morphism of complexes

```text
  0 → A → 0 → 0 → …
        ↓   ↓   ↓
  0 → L^0 → L^1 → L^2 → … )
```

such that the sequence

```text
  0 → A →^ε L^0 → L^1 → …
```

is exact; similarly, a *left resolution* (or *homological resolution*) of `A` is a complex `0 ← L_0 ← L_1 ← …` of
objects of `𝒞` whose derivation operator is of degree `−1`, equipped with an augmentation `ε : L_0 → A`, such that the
sequence

```text
  0 ← A ←^ε L_0 ← L_1 ← …
```

is exact.

When a right resolution `(L^i)_{i ≥ 0}` of an object `A` is such that `L^i = 0` for `i ≥ n + 1`, one says that this
resolution is *of length `≤ n`*. One defines similarly a left resolution of length `≤ n`. A resolution that is of length
`≤ n` for some integer `n` is said to be *finite*.

A resolution of `A` is called *projective* (resp. *injective*) if the objects of `𝒞` other than `A` that compose it are
projective (resp. injective). When `𝒞` is the category of modules (left modules, say) over a ring, one will say
similarly that a resolution of `A` is *flat* (resp. *free*) when the modules other than `A` that compose it are flat
(resp. free).

**11.4.2.**

<!-- label: 0_III.11.4.2 -->

Let `K^• = (K^i)_{i ∈ ℤ}` be a complex of objects of `𝒞` whose derivation operator is of degree `+1`.

We call a *right Cartan–Eilenberg resolution of `K^•`* the pair consisting of a bicomplex `L^{•,•} = (L^{i,j})` with
derivation operators of degree `+1`, with `L^{i,j} = 0` for `j < 0`, and a morphism of simple complexes
`ε : K^• → L^{•,0}`, such that the following conditions are satisfied:

<!-- original page 377 -->

(i) For each index `i`, the sequences

```text
  0 → K^i →^ε L^{i,0} → L^{i,1} → …
  0 → B^i(K^•) →^ε B_I^i(L^{•,0}) → B_I^i(L^{•,1}) → …
  0 → Z^i(K^•) →^ε Z_I^i(L^{•,0}) → Z_I^i(L^{•,1}) → …
  0 → H^i(K^•) →^ε H_I^i(L^{•,0}) → H_I^i(L^{•,1}) → …
```

are exact; in other words, `(L^{i,•})`, `(B_I^i(L^{•,•}))`, `(Z_I^i(L^{•,•}))` and `(H_I^i(L^{•,•}))` are respectively
resolutions of `K^i`, `B^i(K^•)`, `Z^i(K^•)` and `H^i(K^•)`.

(ii) For each `j`, the simple complex `L^{•,j}` is *split*; in other words, the exact sequences

```text
  0 → B_I^i(L^{•,j}) → Z_I^i(L^{•,j}) → H_I^i(L^{•,j}) → 0                       (11.4.2.1)
  0 → Z_I^i(L^{•,j}) → L^{i,j} → B_I^{i+1}(L^{•,j}) → 0                          (11.4.2.2)
```

are split.

One proves `(M, XVII, 1.2)` that if every object of `𝒞` is a subobject of an injective object, every complex `K^•` of
`𝒞` admits an *injective* Cartan–Eilenberg resolution, that is, one formed of injective objects `L^{i,j}` (condition
(ii) above then entails that the `B_I^i(L^{•,j})`, `Z_I^i(L^{•,j})` and `H_I^i(L^{•,j})` are also injective objects).
Moreover, for every morphism `f : K^• → K'^•` of complexes of `𝒞`, every Cartan–Eilenberg resolution `L^{•,•}` of `K^•`
and every *injective* Cartan–Eilenberg resolution `L'^{•,•}` of `K'^•`, there exists a morphism of bicomplexes
`F : L^{•,•} → L'^{•,•}` compatible with `f` and the augmentations; and if `f` and `g` are two *homotopic* morphisms
from `K^•` to `K'^•`, the corresponding morphisms from `L^{•,•}` to `L'^{•,•}` are homotopic `(loc. cit.)`.

When `K^•` is bounded below (resp. bounded above), one may take `L^{•,•}` such that `L^{i,•} = 0` for `i < i_0` (resp.
`i > i_0`) if `K^i = 0` for `i < i_0` (resp. `i > i_0`) `(M, XVII, 1.3)`.

Suppose on the other hand that there exists an integer `n` such that every object of `𝒞` admits an injective resolution
of length `≤ n`; then one may suppose that `L^{i,j} = 0` for `j > n` `(M, XVII, 1.4)`.

**11.4.3.**

<!-- label: 0_III.11.4.3 -->

Let now `T` be a *covariant additive functor* from `𝒞` to an abelian category `𝒞'`. Given a complex `K^•` of `𝒞` and an
injective Cartan–Eilenberg resolution `L^{•,•}` of `K^•`, suppose that the (simple) complex defined by the bicomplex
`T(L^{•,•})` exists (cf. `11.3.1`); then the two spectral sequences `'E(T(L^{•,•}))` and `″E(T(L^{•,•}))` of this
bicomplex are called the *spectral sequences of hypercohomology of `T` with respect to the complex `K^•`*; by virtue of
`(11.4.2)` and `(11.3.2)`, they in fact depend only on `K^•` and not on the chosen injective Cartan–Eilenberg resolution
`L^{•,•}`; moreover, they depend *functorially* on `K^•`. They have a common abutment `H^•(T(L^{•,•}))`, called the
*hypercohomology of `T` with respect to `K^•`*, and denoted `R^•T(K^•)`. One shows that the terms `E_2` of the two
preceding spectral sequences are given by

```text
  'E_2^{p,q} = H^p(R^qT(K^•))                                                  (11.4.3.1)
  ″E_2^{p,q} = R^pT(H^q(K^•))                                                  (11.4.3.2)
```

<!-- original page 378 -->

`R^pT` denoting as usual the `p`th derived functor of `T` for `p ∈ ℤ`; `R^•T(K^•)` denotes the complex
`(R^pT(K^i))_{p ∈ ℤ}`. Unless expressly stated otherwise, *we shall henceforth assume that every object of `𝒞` is a
subobject of an injective object of `𝒞`*, so that injective Cartan–Eilenberg resolutions exist for every complex of `𝒞`.
Since `L^{i,j} = 0` for `j < 0`, the criteria of `(11.3.3)` show that the two hypercohomology spectral sequences of `T`
with respect to `K^•` exist and are *biregular* in each of the two following cases: 1° `K^•` is bounded below; 2° every
object of `𝒞` admits an injective resolution of length at most equal to an integer `n` (independent of the object
considered). Indeed, in the first case, one may suppose `(11.4.2)` that there exists `i_0` such that `L^{i,j} = 0` for
`i < i_0`, and in the second that there exists `j_1` such that `L^{i,j} = 0` for `j > j_1`; in each of the two cases, it
is moreover clear that for given `n`, there are only finitely many pairs `(i, j)` such that `L^{i,j} ≠ 0` and
`i + j = n`, which establishes our assertions.

When one supposes that in `𝒞'` filtered inductive limits exist and are exact (which implies in particular the existence
in `𝒞'` of infinite direct sums), then the complex defined by the bicomplex `T(L^{•,•})` exists, and criterion
`(11.3.3)` shows that the spectral sequence `'E(T(L^{•,•}))` is always regular.

**11.4.4.**

<!-- label: 0_III.11.4.4 -->

When `K^•` is a complex all of whose terms `K^i` are zero except for a single `K^{i_0}`, `R^nT(K^•)` is isomorphic to
`R^{n-i_0}T(K^{i_0})`, as follows at once from the definitions on taking a Cartan–Eilenberg resolution `L^{•,•}` such
that `L^{i,j} = 0` for `i ≠ i_0`.

If `K^•` and `K'^•` are two complexes of `𝒞`, `f`, `g` two homotopic morphisms from `K^•` to `K'^•`, then the morphisms
`R^•T(K^•) → R^•T(K'^•)` deduced from `f` and `g` are identical, and likewise for the morphisms of the cohomology
spectral sequences.

**Proposition (11.4.5).**

<!-- label: 0_III.11.4.5 -->

Suppose that in `𝒞'` filtered inductive limits exist and are exact. If `R^nT(K^i) = 0` for every `n > 0` and every
`i ∈ ℤ`, one has functorial isomorphisms

```text
  R^iT(K^•) ⥲ H^i(T(K^•))                                                       (11.4.5.1)
```

for `i ∈ ℤ`.

**Proof.** The only nonzero terms `E_2` of the first spectral sequence `(11.4.3.1)` are then `'E_2^{p,0} = H^p(T(K^•))`;
in other words, this sequence is *degenerate*; since it is regular `(11.4.4)`, the conclusion follows from `(11.1.6)`.

**11.4.6.**

<!-- label: 0_III.11.4.6 -->

Consider now, for example, a *covariant bifunctor* `(M, N) ↦ T(M, N)` from `𝒞 × 𝒞'` to `𝒞″`, where `𝒞`, `𝒞'`, `𝒞″` are
three abelian categories; one assumes, for simplicity, that `T` is additive in each of its arguments, and moreover that
every object of `𝒞` and every object of `𝒞'` is a subobject of an injective object, and that filtered inductive limits
exist in `𝒞″` and are exact. One then defines the *hypercohomology of `T`* with respect to two complexes `K^•`, `K'^•`
of `𝒞` and `𝒞'` respectively, with derivation operators of degree `+1`, by taking for `K^•` (resp. `K'^•`) an injective
Cartan–Eilenberg resolution `L^{•,•}` (resp. `L'^{•,•}`); then `T(L^{•,•}, L'^{•,•})` is a quadricomplex of `𝒞″`, which
one regards as a bicomplex of `𝒞″` by taking as degrees of `T(L^{i,j}, L'^{h,k})` the integers `i + h` and `j + k`. The
*hypercohomology of `T`* with respect to `K^•` and `K'^•` is by definition the cohomology `H^•(T(L^{•,•}, L'^{•,•}))` of
this bicomplex (in other words, that of the associated simple complex),

<!-- original page 379 -->

denoted `R^•T(K^•, K'^•)`; it is the abutment of two spectral sequences whose terms `E_2` are given by

```text
  'E_2^{p,q} = H^p(R^qT(K^•, K'^•))                                            (11.4.6.1)
  ″E_2^{p,q} = ⊕_{q'+q″=q} R^pT(H^{q'}(K^•), H^{q″}(K'^•))   (cf. M, XVII, 2). (11.4.6.2)
```

Here `R^•T(K^•, K'^•)` is the bicomplex `(R^•T(K^i, K'^j))_{(i,j) ∈ ℤ × ℤ}` and the second member of `(11.4.6.1)` is its
cohomology when one regards it as a simple complex.

Moreover, the first spectral sequence is always regular, and the two spectral sequences are biregular when there exists
`n` such that every object of `𝒞` and every object of `𝒞'` admits an injective resolution of length `≤ n`, or when `K^•`
and `K'^•` are bounded below; in the latter case, one may moreover omit the hypothesis that inductive limits exist in
`𝒞` and `𝒞'`.

If `K_1^•`, `K_1'^•` are two other complexes of `𝒞` and `𝒞'` respectively, `f`, `g` two homotopic morphisms from `K^•`
to `K_1^•`, `f'`, `g'` two homotopic morphisms from `K'^•` to `K_1'^•`, then the morphisms
`R^•T(K^•, K'^•) → R^•T(K_1^•, K_1'^•)` deduced from `f` and `f'` on the one hand, from `g` and `g'` on the other, are
identical, and likewise for the morphisms of the hypercohomology spectral sequences.

One generalizes easily to any covariant additive multifunctor.

**Proposition (11.4.7).**

<!-- label: 0_III.11.4.7 -->

Suppose that for every injective object `I` of `𝒞` (resp. `I'` of `𝒞'`), `A' ↦ T(I, A')` (resp. `A ↦ T(A, I')`) is an
exact functor. Then, with the notation of `(11.4.6)`, one has canonical isomorphisms

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, K'^•)) ⥲ H^•(T(K^•, L'^{•,•}))               (11.4.7.1)
```

where the last two terms are the cohomology of the simple complexes defined by the tricomplexes `T(L^{•,•}, K'^•)` and
`T(K^•, L'^{•,•})` respectively.

**Proof.** Let us define, for example, the first of these isomorphisms. The quadricomplex `T(L^{•,•}, L'^{•,•})` can be
considered as a bicomplex, by taking as degrees of `T(L^{i,j}, L'^{h,k})` the numbers `i + j + h` and `k`. As for each
`h`, `L'^{h,•}` is a resolution of `K'^h`, one has, for this bicomplex, by virtue of the hypothesis on `T`,
`H_{II}^q(T(L^{•,•}, L'^{•,•})) = 0` for `q ≠ 0` and `H_{II}^0(T(L^{•,•}, L'^{•,•})) = T(L^{•,•}, K'^•)`; the first
spectral sequence of this bicomplex is therefore degenerate; since `L'^{h,k} = 0` for `k < 0`, this sequence is moreover
regular `(11.3.3)`, and the conclusion follows from `(11.1.6)`.

One has analogous results for a covariant multifunctor in any number `n` of arguments: in computing the hypercohomology,
it is not necessary to replace *all* the complexes by a Cartan–Eilenberg resolution, but only `n − 1` of them, provided
that when one fixes any `n − 1` arguments giving them as values injective objects, the covariant functor in the
remaining argument is *exact*.

### 11.5. Passage to the inductive limit in hypercohomology

**Lemma (11.5.1).**

<!-- label: 0_III.11.5.1 -->

Let `K^• = (K^i)_{i ∈ ℤ}` be a complex of `𝒞`, and for every integer `r ∈ ℤ`, let `K_{(r)}^•` be the complex such that
`K_{(r)}^i = 0` for `i < r`, `K_{(r)}^i = K^i` for `i ≥ r`. Let `T` be a covariant additive functor

<!-- original page 380 -->

from `𝒞` to `𝒞'`, commuting with inductive limits (one assumes that filtered inductive limits exist and are exact in `𝒞`
and `𝒞'`). Then `R^•T(K^•)` is isomorphic to the inductive limit `lim_→ R^•T(K_{(r)}^•)` as `r` tends to `−∞`.

**Proof.** The construction of an injective Cartan–Eilenberg resolution of `K^•` is performed by choosing arbitrarily,
for each `i`, an injective resolution `(X_B^{i,j})_{j ≥ 0}` of `B^i(K^•)` and an injective resolution
`(X_H^{i,j})_{j ≥ 0}` of `H^i(K^•)`; that done, the method of construction shows that the injective resolution
`(L^{i,j})_{j ≥ 0}` of `K^i` and the derivation operators `L^{i,j} → L^{i+1,j}` depend only on the resolutions
`(X_B^{i,•})`, `(X_H^{i,•})` and `(X_B^{i+1,•})` `(M, XVII, 1.2)`. Now, it is clear that one has
`B^i(K_{(r)}^•) = B^i(K^•)` and `H^i(K_{(r)}^•) = H^i(K^•)` for `i ≥ r + 1`. One has, on the other hand, for each `r`, a
canonical injection `φ_{r-1, r} : K_{(r)}^• → K_{(r-1)}^•`, `φ_{r-1, r}` being the identity for `i ≠ r − 1`. The
preceding remark shows that if `L^{•,•} = (L^{i,j})` is an injective Cartan–Eilenberg resolution of `K^•`, one can for
each `r` define an injective Cartan–Eilenberg resolution `L_{(r)}^{•,•} = (L_{(r)}^{i,j})` of `K_{(r)}^•` such that
`L_{(r)}^{i,j} = 0` for `i < r` and `L_{(r)}^{i,j} = L^{i,j}` for `i ≥ r + 1`. One can, on the other hand, define a
morphism of bicomplexes `Φ_{r-1, r}^{•,•} : L_{(r)}^{•,•} → L_{(r-1)}^{•,•}` corresponding to `φ_{r-1, r}`, and the
method of definition of this morphism `(loc. cit.)` shows once again that one may construct it so that
`Φ_{r-1, r}^{i,j}` is the identity for `i ≠ r` and `i ≠ r − 1`. One has thus defined an inductive system
`(L_{(r)}^{•,•})` of bicomplexes of `𝒞`, of which `L^{•,•}` is evidently the inductive limit as `r` tends to `−∞`; by
reason of the commutativity of direct sums and inductive limits, the simple complex associated to `L^{•,•}` is also the
inductive limit of the simple complex associated to `L_{(r)}^{•,•}`. Since `T` commutes by hypothesis with inductive
limits, and the same holds for cohomology (by exactness of the functor `lim_→`), one indeed has
`H^•(T(L^{•,•})) = lim_→ H^•(T(L_{(r)}^{•,•}))` up to isomorphism.

Lemma `(11.5.1)` allows one to extend to arbitrary complexes `K^•`, by passage to the inductive limit, properties valid
for complexes *bounded below*. As a first example, we shall prove:

**Proposition (11.5.2).**

<!-- label: 0_III.11.5.2 -->

Under the hypotheses of `(11.5.1)` concerning `𝒞`, `𝒞'` and `T`, `R^•T(K^•)` is a cohomological functor in the abelian
category of complexes of `𝒞`.

**Proof.** We show that we can reduce to the case of complexes bounded below: if one has an exact sequence
`0 → K'^• → K^• → K″^• → 0` of complexes, one evidently deduces from it for each `r` an exact sequence
`0 → K_{(r)}'^• → K_{(r)}^• → K_{(r)}″^• → 0`, whence by hypothesis an exact sequence

```text
  … → R^nT(K_{(r)}'^•) → R^nT(K_{(r)}^•) → R^nT(K_{(r)}″^•) →^∂ R^{n+1}T(K_{(r)}'^•) → …
```

these exact sequences forming an inductive system; lemma `(11.5.1)` and the exactness of the functor `lim_→` show that
one has an exact sequence

```text
  … → R^nT(K'^•) → R^nT(K^•) → R^nT(K″^•) →^∂ R^{n+1}T(K'^•) → …
```

To deal with the case of complexes bounded below, we may confine ourselves to those for which `K^i = 0` for `i < 0`;
these evidently form an abelian category `𝒦`.

**Lemma (11.5.2.1).**

<!-- label: 0_III.11.5.2.1 -->

In `𝒦`, let `𝒥` be the set of complexes `Q^• = (Q^i)_{i ≥ 0}` having the

<!-- original page 381 -->

following properties: 1° Every `Q^i` is an injective object of `𝒞`; 2° For every `i ≥ 0`, one has `Z^i(Q^•) = B^i(Q^•)`,
and `Z^i(Q^•)` is a direct factor of `Q^i`. Then:

(i) Every `Q^• ∈ 𝒥` is an injective object of `𝒦`.

(ii) Every object of `𝒦` is isomorphic to a subcomplex of a complex belonging to `𝒥`.

**Proof.** (i) Let `A^• = (A^i)` be an object of `𝒦`, `A'^• = (A'^i)` a subobject of `A^•`, `Q^• = (Q^i)` an object of
`𝒥`, and suppose given a morphism `f = (f^i) : A'^• → Q^•`, which we wish to extend to a morphism
`g = (g^i) : A^• → Q^•`. We shall use the language of the category of modules for simplicity (cf. `[27]`).

We identify `Q^i` with `B^i(Q^•) ⊕ B^{i+1}(Q^•)`; we proceed by induction on `i`, supposing therefore the `g^j` defined
for `j < i`, compatible with the derivation operators `d^j : A^j → A^{j+1}` and `d^{j} : Q^j → Q^{j+1}` for `j < i − 1`
and such moreover that: 1° `g^{i-1}(Z^{i-1}(A^•)) ⊂ Z^{i-1}(Q^•)`; 2° If one sets `C^j = (d^j)^{-1}(A'^{j+1})` for every
`j`, then `d^{i-1} ∘ g^{i-1}` coincides with `f^i ∘ d^{i-1}` on `C^{i-1}`. The morphism `f^i : A'^i → Q^i` gives, by
composition with the projections, two morphisms `f^{i'} : A'^i → B^i(Q^•)` and `f^{ii} : A'^i → B^{i+1}(Q^•)`. Since
`d^{i-1} ∘ g^{i-1}` carries `A^{i-1}` into `B^i(Q^•)` and vanishes on `Z^{i-1}(A^•)`, it defines a morphism
`h^i : B^i(A^•) → B^i(Q^•)`, and since `d^{i-1} ∘ g^{i-1}` coincides with `f^i ∘ d^{i-1}` on `C^{i-1}`, `h^i` coincides
with `f_1^i` on `B^i(A^•) ∩ A'^i`. Since `B^i(Q^•)`, a direct factor of `Q^i`, is injective, there is a morphism
`g^{i'} : A^i → B^i(Q^•)` which coincides with `h^i` on `B^i(A^•)` and with `f^{i'}` on `A'^i`. Consider on the other
hand the morphism `f^{ii+1} ∘ d^i : C^i → B^{i+1}(Q^•)`, which vanishes on `Z^i(A^•)`; since `B^{i+1}(Q^•)` is
injective, there is a morphism `g^{ii} : A^i → B^{i+1}(Q^•)`, which coincides with `f^{ii+1} ∘ d^i` on `C^i` and with
`0` on `Z^i(A^•)`. It suffices then to take `g^i = g^{i'} + g^{ii}` to be able to continue the induction.

(ii) To embed `A^• = (A^i)` in a complex belonging to `𝒥`, one takes for each `i ≥ 1` an injective object `Q'^i` of `𝒞`
such that there exists an injection `f'^i : A^i → Q'^i`. Then set `Q^i = 0` for `i < 0`, `Q^0 = Q'^1` and
`Q^i = Q'^i ⊕ Q'^{i+1}` for `i ≥ 1`, with the obvious derivation operator. Set `f^i = f'^{i+1} + (f'^{i+1} ∘ d^i)` for
every `i` (with `f'^i = 0` for `i ≤ 0`); it is immediate that `f^i` is injective for every `i`, and that the `f^i` are
compatible with the derivation operators.

**Corollary (11.5.2.2).**

<!-- label: 0_III.11.5.2.2 -->

Every object `K^•` of `𝒦` admits a right resolution formed of objects of `𝒥`. If `L^{•,•}` is such a resolution, then
for any resolution `L'^{•,•}` of `K^•` formed of objects of `𝒦`, there is a morphism of bicomplexes
`F : L'^{•,•} → L^{•,•}` compatible with the augmentations, and any two such morphisms `F`, `F'` are homotopic.

**Proof.** This is none other than `(M, V, 1.1 a))` applied to the abelian category `𝒦`.

**11.5.2.3.**

<!-- label: 0_III.11.5.2.3 -->

These preliminaries laid, consider an injective Cartan–Eilenberg resolution `L'^{•,•}` of `K^•` and a resolution
`L^{•,•}` of `K^•` formed of objects of `𝒥`, and let us show that one has an isomorphism
`H^•(T(L'^{•,•})) ⥲ H^•(T(L^{•,•}))`. Indeed, one deduces from `(11.5.2.2)` a morphism of bicomplexes
`T(L'^{•,•}) → T(L^{•,•})`, and consequently a morphism `'E(T(L'^{•,•})) → 'E(T(L^{•,•}))` of the first spectral
sequences of these bicomplexes. Since by virtue of `(11.3.3)` these spectral sequences are regular, it suffices
`(11.1.5)` to see that the preceding morphism is an isomorphism for the terms `E_2`, or, equivalently, that
`H_{II}^q(T(L^{i,•}))` is equal to `R^qT(K^i)`; since `L^{i,•}` is a right resolution of `K^i`, one is reduced to
proving the

<!-- original page 382 -->

**Lemma (11.5.2.4).**

<!-- label: 0_III.11.5.2.4 -->

If `L^• = (L^i)_{i ∈ ℤ}` is a right resolution of an object `A` of `𝒞` such that `R^nT(L^i) = 0` for every `i ∈ ℤ` and
every `n > 0`, then one has `H^•T(L^•) = R^•T(A)`.

**Proof.** This is a particular case of `(T, 2.5.2)`.

**11.5.2.5.**

<!-- label: 0_III.11.5.2.5 -->

The proof of `(11.5.2)` now concludes at once, for `L'^{•,•}` is an injective resolution of `K^•` in the abelian
category `𝒦`; in other words, `K^• ↦ H^•(T(L'^{•,•}))` is none other than the right-derived cohomological functor of `T`
in the category `𝒦` `(T, 2.3)`.

**Proposition (11.5.3).**

<!-- label: 0_III.11.5.3 -->

Under the hypotheses of `(11.5.1)` concerning `𝒞`, `𝒞'` and `T`, let `L^{•,•} = (L^{i,j})` be a bicomplex such that
`L^{i,j} = 0` for `j < 0` and such that, for every `i`, `L^{i,•}` is a resolution of `K^i`; suppose finally that
`R^nT(L^{i,j}) = 0` for every pair `(i, j)` and every `n > 0`. Then there exists a functorial isomorphism

```text
  R^•T(K^•) ⥲ H^•(T(L^{•,•})).                                                 (11.5.3.1)
```

**Proof.** Let `L_{(r)}^{•,•} = (L_{(r)}^{i,j})` be the bicomplex such that `L_{(r)}^{i,j} = 0` for `i < r`,
`L_{(r)}^{i,j} = L^{i,j}` for `i ≥ r`; it is immediate that `L^{•,•}` is the inductive limit of `L_{(r)}^{•,•}` as `r`
tends to `−∞`; by virtue of the hypothesis on `T` and of `(11.5.1)`, it suffices therefore to prove the proposition when
`K^•` is bounded below, for example `K^i = 0` for `i < 0`, and `L^{i,j} = 0` for `i < 0`. Let then
`L'^{•,•} = (L'^{i,j})` be a right resolution of `K^•` formed of objects of `𝒥` `(11.5.2.2)`; there is a morphism of
bicomplexes `L^{•,•} → L'^{•,•}` compatible with the augmentations, whence a morphism `'E(T(L^{•,•})) → 'E(T(L'^{•,•}))`
for the first spectral sequences; lemma `(11.5.2.4)` shows, as in `(11.5.2.3)`, that this morphism is an isomorphism,
whence the conclusion.

**Remark (11.5.4).**

<!-- label: 0_III.11.5.4 -->

The preceding arguments prove that the conclusions of `(11.5.2)` and `(11.5.3)` are valid in the category of complexes
`K^•` bounded below, without supposing that `T` commutes with filtered inductive limits. Moreover, when one considers
only the category `𝒦` of complexes `K^•` such that `K^i = 0` for `i < 0`, the characterization of `R^•T(K^•)` as the
system of right-derived functors of `T` in `𝒦` shows that this cohomological functor is *universal* `(T, 2.3)`.

Another case in which `(11.5.2)` is valid without making any additional hypothesis on `T` is the case where there exists
an integer `m > 0` such that every object of `𝒞` admits an injective resolution of length `≤ m`. Indeed, in the proof of
`(11.5.1)`, all the injective resolutions of objects of `𝒞` that intervene may be taken of length `≤ m`, whence it
follows at once that the terms of total degree `n` of the bicomplex `T(L_{(r)}^{•,•})` are equal to those of
`T(L^{•,•})` and finite in number, as soon as `r` is sufficiently large; this entails that for every `n`,
`H^n(T(L^{•,•})) = H^n(T(L_{(r)}^{•,•}))` as soon as `r` is sufficiently large. With the notation of `(11.5.2)`, one
therefore also has `R^nT(K_{(r)}^•) = R^nT(K^•)` for `r` sufficiently large (depending on `n`), and likewise for `K'^•`
and `K″^•`, whence the conclusion. In the same way, `(11.5.3)` is valid without additional condition on `T` when `𝒞`
satisfies the preceding hypothesis and one supposes that the resolutions `L^{i,•}` are of length `≤ m`.

**11.5.5.**

<!-- label: 0_III.11.5.5 -->

The result of `(11.5.2)` generalizes to covariant multifunctors. Consider for example the situation of `(11.4.6)`, where
one supposes that in `𝒞`, `𝒞'` and `𝒞″`

<!-- original page 383 -->

filtered inductive limits exist and are exact, and that `T` commutes with inductive limits. Then `R^•T(K^•, K'^•)` is a
*bifunctor* cohomological in each of the complexes `K^•`, `K'^•`; to see this, one reduces as in `(11.5.2)` to the case
where `K^•` and `K'^•` are bounded below; taking then injective resolutions of `K^•` and `K'^•` of the type described in
`(11.5.2.2)`, one is reduced to the general property proved in `(M, V, 4.1)`.

**11.5.6.**

<!-- label: 0_III.11.5.6 -->

Similarly, the results of `(11.4.7)` and `(11.5.3)` generalize as follows. Suppose (under the hypotheses of `(11.5.5)`)
that one has two bicomplexes `L^{•,•} = (L^{i,j})`, `L'^{•,•} = (L'^{i,j})` such that `L^{i,j} = 0` and `L'^{i,j} = 0`
for `j < 0`, that for every `i`, `L^{i,•}` is a resolution of `K^i` and `L'^{i,•}` is a resolution of `K'^i`, and
finally that `R^nT(L^{i,j}, L'^{h,k}) = 0` for `n > 0` and for every system of indices `(i, j, h, k)`. Then one has a
functorial isomorphism in `K^•` and `K'^•`

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, L'^{•,•})).                                  (11.5.6.1)
```

This is established as in `(11.5.3)` by reducing to the case where `K^•` and `K'^•` are bounded below.

Suppose moreover that for every pair `(i, j)` and for every pair `(h, k)`, the functors `A ↦ T(A, L'^{h,k})` and
`A' ↦ T(L^{i,j}, A')` are exact in `𝒞` and `𝒞'` respectively. Then one also has functorial isomorphisms

```text
  R^•T(K^•, K'^•) ⥲ H^•(T(L^{•,•}, K'^•)) ⥲ H^•(T(K^•, L'^{•,•})).              (11.5.6.2)
```

The proof is similar to that of `(11.4.7)`.

**11.5.7.**

<!-- label: 0_III.11.5.7 -->

One again notes that the results of `(11.5.5)` and `(11.5.6)` are valid without supposing that `T` commutes with
inductive limits, provided one restricts oneself to complexes `K^•`, `K'^•` bounded below, or one supposes that every
object of `𝒞` (resp. `𝒞'`) admits an injective resolution of bounded length, and that in `(11.5.6)` the bicomplexes
`L^{•,•}` and `L'^{•,•}` have their second degree bounded above.

### 11.6. Hyperhomology of a functor with respect to a complex `K_•`

**11.6.1.**

<!-- label: 0_III.11.6.1 -->

Let `𝒞` be an abelian category, `K_• = (K_i)_{i ∈ ℤ}` a complex of objects of `𝒞` whose derivation operator is of degree
`−1`. A *left Cartan–Eilenberg resolution* of `K_•` consists of a bicomplex `L_{•,•} = (L_{i,j})` with derivation
operators of degree `−1` with `L_{i,j} = 0` for `j < 0`, and a morphism of simple complexes `ε : L_{•,0} → K_•`, such
that the conditions obtained from those of `(11.4.2)` by "reversal of arrows" are satisfied. If every object of `𝒞` is a
quotient of a projective object, every complex `K_•` of `𝒞` admits a *projective* Cartan–Eilenberg resolution, that is,
one formed of projective objects `L_{i,j}`, with functorial properties similar to those of `(11.4.2)`. Moreover, if
`K_•` is bounded below (resp. bounded above), one may suppose that `L_{i,j} = 0` for `i < i_0` (resp. `i > i_0`) if
`K_i = 0` for `i < i_0` (resp. `i > i_0`). If every object of `𝒞` admits a projective resolution of length `≤ n`, one
may suppose that `L_{i,j} = 0` for `j > n`.

<!-- original page 384 -->

**11.6.2.**

<!-- label: 0_III.11.6.2 -->

Suppose that `T` is a *covariant additive functor* from `𝒞` to an abelian category `𝒞'`. The definition of the
*hyperhomology* `L_•T(K_•)` and of the *spectral sequences of hyperhomology* of `T` with respect to a complex `K_•` of
`𝒞` (when they exist) is performed again from `(11.4.3)` by "reversal of arrows", the terms `E^2` of the two spectral
sequences thus obtained being

```text
  'E_{p,q}^2 = H_p(L_qT(K_•))                                                  (11.6.2.1)
  ″E_{p,q}^2 = L_pT(H_q(K_•))                                                  (11.6.2.2)
```

where `L_pT` denotes the `p`th derived functor of `T` for `p ≥ 0`, and `0` for `p < 0`; `L_•T(K_•)` denotes the complex
`(L_qT(K_i))_{i ∈ ℤ}`.

The properties of hyperhomology are not all deducible by simple "reversal of arrows" from those of hypercohomology
(unless one makes additional hypotheses of type AB 5\*) of `T, 1.5` on the category `𝒞'`) because of the regularity
conditions on the two preceding spectral sequences, to which one must this time apply the criteria of `(11.3.4)`. These
last show that when one supposes that in `𝒞'` filtered inductive limits exist and are exact, then the complex defined by
the bicomplex `T(L_{•,•})` exists, and the second spectral sequence `″E(T(L_{•,•}))` is this time regular. If one
supposes either that `K_•` is bounded below, or that there exists an integer `n` such that every object of `𝒞` admits a
projective resolution of length `≤ n`, then the *two* hyperhomology spectral sequences exist (without hypothesis on
`𝒞'`) and are biregular.

**Proposition (11.6.3).**

<!-- label: 0_III.11.6.3 -->

Let `𝒞`, `𝒞'` be two abelian categories, `T` a covariant additive functor from `𝒞` to `𝒞'`. Then:

(i) Hyperhomology `L_•T(K_•)` is a homological functor in the abelian category of complexes of `𝒞` bounded below.

(ii) Let `K_•` be a complex of `𝒞` bounded below. If `L_nT(K_i) = 0` for every `n > 0` and every `i ∈ ℤ`, one has
functorial isomorphisms

```text
  L_iT(K_•) ⥲ H_i(T(K_•))                                                      (11.6.3.1)
```

for `i ∈ ℤ`.

(iii) Let `K_•` be a complex of `𝒞` bounded below. Let `L_{•,•} = (L_{i,j})` be a bicomplex such that `L_{i,j} = 0` for
`j < 0` and such that, for every `i`, `L_{i,•}` is a resolution of `K_i`; suppose finally that `L_nT(L_{i,j}) = 0` for
every pair `(i, j)` and every `n > 0`. Then there exists a functorial isomorphism

```text
  L_•T(K_•) ⥲ H_•(T(L_{•,•})).                                                 (11.6.3.2)
```

The proofs proceed as those of `(11.5.2)`, `(11.4.5)` and `(11.5.3)` in the case of complexes bounded below. We leave
the details of these arguments to the reader.

**11.6.4.**

<!-- label: 0_III.11.6.4 -->

One has entirely analogous results for covariant multifunctors additive in each of the arguments. For example, for a
bifunctor `T`, one has the two hyperhomology spectral sequences with terms `E^2` given by

<!-- original page 385 -->

```text
  'E_{p,q}^2 = H_p(L_qT(K_•, K_•'))                                            (11.6.4.1)
  ″E_{p,q}^2 = ⊕_{q'+q″=q} L_pT(H_{q'}(K_•), H_{q″}(K_•')).                    (11.6.4.2)
```

Here too, it is the *second* spectral sequence which is regular, the two sequences being biregular when one deals with
complexes `K_•`, `K_•'` bounded below, or when the objects of the abelian categories considered have projective
resolutions of fixed length.

Moreover:

**Proposition (11.6.5).**

<!-- label: 0_III.11.6.5 -->

Let `𝒞`, `𝒞'`, `𝒞″` be three abelian categories, `T` a covariant bifunctor biadditive from `𝒞 × 𝒞'` to `𝒞″`.

(i) `L_•T(K_•, K_•')` is a homological bifunctor in each of the complexes bounded below `K_•`, `K_•'` (formed
respectively of objects of `𝒞` and of objects of `𝒞'`).

(ii) Suppose `K_•` and `K_•'` bounded below. Let `L_{•,•} = (L_{i,j})`, `L_{•,•}' = (L_{i,j}')` be two bicomplexes such
that `L_{i,j} = 0` and `L_{i,j}' = 0` for `j < 0`, such that for every `i`, `L_{i,•}` is a resolution of `K_i` and
`L_{i,•}'` is a resolution of `K_i'`, and finally that `L_nT(L_{i,j}, L_{h,k}') = 0` for `n > 0` and every system
`(i, j, h, k)`. Then one has a functorial isomorphism

```text
  L_•T(K_•, K_•') ⥲ H_•(T(L_{•,•}, L_{•,•}')).                                 (11.6.5.1)
```

(iii) Suppose moreover that for every pair `(i, j)` and every pair `(h, k)`, the functors `A ↦ T(A, L_{h,k}')` and
`A' ↦ T(L_{i,j}, A')` are exact in `𝒞` and `𝒞'` respectively. Then one has functorial isomorphisms

```text
  L_•T(K_•, K_•') ⥲ H_•(T(L_{•,•}, K_•')) ⥲ H_•(T(K_•, L_{•,•}')).             (11.6.5.2)
```

The proofs are analogous to those of `(11.5.5)` and `(11.5.6)`.

### 11.7. Hyperhomology of a functor with respect to a bicomplex `K_{•,•}`

**11.7.1.**

<!-- label: 0_III.11.7.1 -->

Let `𝒞` be an abelian category in which every object is a quotient of a projective object. Consider a bicomplex
`K_{•,•} = (K_{i,j})` formed of objects of `𝒞`, and *whose two degrees are bounded below*; one may always restrict to
the case where `K_{i,j} = 0` for `i < 0` or `j < 0`, and this is what we shall do henceforth. One may consider `K_{•,•}`
as a (simple) complex formed of objects `K_{i,•} = (K_{i,j})_{j ≥ 0}` of the abelian category `𝒦` of complexes of
positive degrees of objects of `𝒞`. It follows from lemma `(11.5.2.1)` (or rather from the "dual" lemma obtained by
"reversal of arrows") and from `(M, V, 2.2)` that `K_{•,•}` admits a *projective Cartan–Eilenberg resolution* in the
category `𝒦`; such a resolution is a tricomplex `M_{•,•,•} = (M_{i,j,k})` of `𝒞`, with all degrees `≥ 0`, formed of
projective objects, such that for every `i`, `M_{i,•,•}`, `B_j^I(M_{•,•,•})`, `Z_j^I(M_{•,•,•})`, `H_j^I(M_{•,•,•})`
constitute projective resolutions of `K_{i,•}`, `B_j^I(K_{•,•})`, `Z_j^I(K_{•,•})`, `H_j^I(K_{•,•})` respectively in the
category `𝒦`; in particular, for every pair `(i, j)`, `M_{i,j,•}` is a projective resolution of `K_{i,j}` in `𝒞`.

**Proposition (11.7.2).**

<!-- label: 0_III.11.7.2 -->

Let `T` be a covariant additive functor from `𝒞` to an abelian category `𝒞'`. With the notation of `(11.7.1)`, the
homology `H_•(T(M_{•,•,•}))` of the simple complex associated to the tricomplex `T(M_{•,•,•})` is canonically isomorphic
to the hyperhomology `L_•T(K_•)` of the

<!-- original page 386 -->

simple complex associated to `K_{•,•}` `(11.6.2)`, and is the common abutment of *six biregular spectral sequences*
denoted `^{(t)}E` (with `t = a`, `b`, `a'`, `b'`, `c`, or `d`), whose terms `E^2` are given by the formulas

```text
  ^{(a)}E_{p,q}^2 = L_pT(H_q^I(K_{•,•}))
  ^{(b)}E_{p,q}^2 = H_p(L_q^{II}T(K_{•,•}))
  ^{(a')}E_{p,q}^2 = L_pT(H_q^{II}(K_{•,•}))
  ^{(b')}E_{p,q}^2 = H_p(L_q^I T(K_{•,•}))
  ^{(c)}E_{p,q}^2 = L_pT(H_q(K_{•,•}))
  ^{(d)}E_{p,q}^2 = H_p(L_q^I T(K_{•,•}))
```

(Recall that we use the notation `F(A_•)` to denote the complex of objects `F(A_i)` for every complex `A_• = (A_i)`; for
example `L_q^{II}T(K_{•,•})` denotes the complex `(L_q^{II}T(K_{i,•}))_{i ≥ 0}`, where `L_q^{II}T(K_{i,•})` is the
hyperhomology of index `q` of the functor `T` with respect to the simple complex `K_{i,•}`.)

**Proof.** Denote by `L_•` the simple complex associated to `K_{•,•}`, so that `L_i = ⊕_{r+s=i} K_{r,s}`, and set
`N_{i,•} = ⊕_{r+s=i} M_{r,s,•}`; it is clear that for each `i`, `N_{i,•}` is a projective resolution of `L_i` in `𝒞`;
therefore by `(11.6.3)` and `(11.6.4)`, one has a functorial isomorphism `L_•T(L_•) ⥲ H_•(T(N_{•,•}))`; as the simple
complex associated to the bicomplex `T(N_{•,•})` is also associated to the tricomplex `T(M_{•,•,•})`, this proves the
first assertion of the statement.

Moreover, `L_•T(L_•)` is the abutment of the two hyperhomology spectral sequences `(11.6.2)` of `T` relative to the
simple complex `L_•`, which are nothing other than the sequences `^{(b')}E` and `^{(b)}E` respectively.

Consider now `M_{•,•,•}` as a bicomplex `U_{•,•}` with `U_{i,j} = ⊕_{r+s=j} M_{i,r,s}`; `H_•(T(M_{•,•,•}))` is again the
abutment of the two spectral sequences of the bicomplex `T(U_{•,•})`. Now, for every `i`, `M_{i,•,•}` is a bicomplex
satisfying the conditions of `(11.6.3)` relative to the simple complex `K_{i,•}`; hence
`H_q^{II}(T(U_{i,•})) = L_q^{II}T(K_{i,•})`, and the first spectral sequence of `T(U_{•,•})` is nothing other than
`^{(b)}E`. On the other hand, for every `r`, `M_{•,r,•}` is a Cartan–Eilenberg resolution of the simple complex
`K_{•,r}`; the calculation done in `(M, XV, 2)` shows that `H_q^I(T(M_{•,r_•,•})) = T(H_q^I(M_{•,r_•,•}))`, hence
`H_q^I(T(U_{•,•})) = ⊕_{r+s=j} T(H_q^I(M_{•,r,s}))`; in other words, the simple complex `H_q^I(T(U_{•,•}))` is nothing
other than the simple complex associated to the bicomplex `T(H_q^I(M_{•,•,•}))`. Now, for every `q`, `H_q^I(M_{•,•,•})`
is a *projective resolution* of the simple complex `H_q^I(K_{•,•})` in the category `𝒦`; applying `(11.6.3)`, one sees
that one has

```text
  H_p^{II}(T(H_q^I(M_{•,•,•}))) = L_pT(H_q^I(K_{•,•})),
```

and one thus obtains the sequence `^{(a)}E`. Finally, the sequences `^{(a')}E` and `^{(c)}E` are obtained by
interchanging the roles of the indices `i` and `j` in the definition of the tricomplex `M_{•,•,•}` and applying to this
new tricomplex the preceding arguments.

One says that `L_•T(K_{•,•})` is the *hyperhomology of `T` relative to the bicomplex `K_{•,•}`*.

**Remarks (11.7.3).**

<!-- label: 0_III.11.7.3 -->

(i) It follows from `(11.6.3)` that `L_•T(K_{•,•})` is a homological functor in the category of bicomplexes `K_{•,•}` of
`𝒞` bounded below in each of their degrees.

<!-- original page 387 -->

(ii) Let `M_{•,•,•}` be a tricomplex of `𝒞` such that for each pair `(r, s)`, `M_{r,s,•}` is a resolution of `K_{r,s}`
and that `L_nT(M_{ijk}) = 0` for all triples `(i, j, k)` and every `n > 0`. Then one has an isomorphism
`L_•T(K_{•,•}) ⥲ H_•(T(M_{•,•,•}))`; indeed, with the notation of the proof of `(11.7.2)`, `N_{i,•}` is a resolution of
`L_i` such that `L_nT(N_{i,j}) = 0` for `n > 0` and every pair `(i, j)`, and it suffices to apply `(11.6.3, (iii))`.

(iii) One generalizes at once the results of `(11.7.2)` to covariant multifunctors; for example, let `𝒞'` be a second
abelian category in which every object is a quotient of a projective object, `K_{•,•}'` a bicomplex of `𝒞'` whose two
degrees are bounded below, and `T` a covariant additive bifunctor from `𝒞 × 𝒞'` to an abelian category `𝒞″`. If `L_•`
and `L_•'` are the simple complexes associated to `K_{•,•}` and `K_{•,•}'` respectively, one defines the hyperhomology
of `T` with respect to the two bicomplexes `K_{•,•}`, `K_{•,•}'` as the hyperhomology `L_•T(L_•, L_•')`; applying
`(11.6.4)` and `(11.6.5)`, one has, as in `(11.7.2)`, six spectral sequences abutting to this hyperhomology, which we
leave the reader to write out.

### 11.8. Complements on the cohomology of simplicial complexes

**11.8.1.**

<!-- label: 0_III.11.8.1 -->

Let `A` be a finite set, `Σ(A)` the set of finite sequences `σ = (α_0, …, α_h)` of elements of `A` ("simplices" of `A`);
one sets `|σ| = {α_0, …, α_h}`; recall that the *chain complex* `C_•(A)` is the free graded abelian group generated by
the elements of `Σ(A)`, `(α_0, …, α_h)` being of *degree `h`*, with a differential defined by

```text
  d(α_0, …, α_h) = ∑_{i=0}^h (−1)^i (α_0, …, α̂_i, …, α_h).
```

The subgroup `D_•(A)` of `C_•(A)` generated by the chains `σ = (α_0, …, α_h)` for which two of the `α_i` are equal, and
by the chains `π(σ) − ε_π · σ`, where for every permutation `π`, `π(σ) = (α_{π(0)}, …, α_{π(h)})` and `ε_π` is the
signature of `π`, is a subcomplex of `C_•(A)` whose elements are called *degenerate chains*; one sets
`L_•(A) = C_•(A)/D_•(A)`, and one has a natural homomorphism of complexes `p : C_•(A) → L_•(A)`. One defines on the
other hand a homomorphism of complexes `j : L_•(A) → C_•(A)` as follows: one totally orders `A`; to the class mod.
`D_•(A)` of a simplex `σ = (α_0, …, α_h)`, one associates `0` if two of the `α_i` are equal, and the sequence
`(β_0, …, β_h)` of the `α_i` arranged *in increasing order* otherwise. It is clear that `p ∘ j` is the identity of
`L_•(A)`.

**11.8.2.**

<!-- label: 0_III.11.8.2 -->

Let `B` be a second finite set; if `d'`, `d″` are the differentials of `C_•(A)` and `C_•(B)`, the tensor product complex
`C_•(A) ⊗ C_•(B)` can be considered as the free abelian group generated by the elements of `Σ(A) × Σ(B)`, with the
differential `d(σ, τ) = (d'σ, τ) + (−1)^{h+1}(σ, d″τ)` if `Card |σ| = h + 1`.

The natural homomorphisms `C_•(A) → L_•(A)`, `C_•(B) → L_•(B)` define a homomorphism
`p : C_•(A) ⊗ C_•(B) → L_•(A) ⊗ L_•(B)`, this last tensor product being isomorphic to
`(C_•(A) ⊗ C_•(B))/(C_•(A) ⊗ D_•(B) + D_•(A) ⊗ C_•(B))`. Likewise, by means of the homomorphisms `L_•(A) → C_•(A)` and
`L_•(B) → C_•(B)` defined in `(11.8.1)` (by means of total orders on `A` and `B`), one defines a homomorphism
`j : L_•(A) ⊗ L_•(B) → C_•(A) ⊗ C_•(B)` such that `p ∘ j` is the identity.

<!-- original page 388 -->

With this notation:

**Proposition (11.8.3).**

<!-- label: 0_III.11.8.3 -->

There exists a homotopy `h : C_•(A) ⊗ C_•(B) → C_•(A) ⊗ C_•(B)` such that `h(σ, τ)` is a linear combination of pairs of
simplices `(σ_i, τ_i)` with `|σ_i| ⊂ |σ|`, `|τ_i| ⊂ |τ|`, and such that for `f = j ∘ p` one has

```text
  f − 1 = h ∘ d + d ∘ h.                                                       (11.8.3.1)
```

**Proof.** It suffices to define `h` on each pair `(σ, τ)` of simplices, reasoning by induction on the sum of the
degrees of `σ` and `τ`, since one can take `h = 0` when this sum is `0`. Let `ω = f(σ, τ) − (σ, τ) − h(d(σ, τ))`; by the
induction hypothesis and the definition of `d`, one has `ω ∈ C_•(|σ|) ⊗ C_•(|τ|)`. One has

```text
  dω = f(d(σ, τ)) − d(σ, τ) − d(h(d(σ, τ))) = h(d(d(σ, τ))) = 0
```

by virtue of `(11.8.3.1)` and the induction hypothesis. Now, one has `H_q(C_•(A)) = 0` for `q > 0` `(G, I, 3.7.4)`,
hence also `H_q(C_•(A) ⊗ C_•(B)) = 0` for `q > 0`, by virtue of Künneth's formula `(G, I, 5.5.2)`. Applying this remark
on replacing `A` by `|σ|` and `B` by `|τ|`, one sees that there exists an element `ω'` of `C_•(|σ|) ⊗ C_•(|τ|)` such
that `ω = dω'`; taking `h(σ, τ) = ω'`, one verifies `(11.8.3.1)` for the pair `(σ, τ)` and the induction can continue.

**11.8.4.**

<!-- label: 0_III.11.8.4 -->

The notation being that of `(11.8.2)`, we shall set `(σ, τ) ≤ (σ', τ')` if `|σ| ⊂ |σ'|` and `|τ| ⊂ |τ'|`. A *system of
coefficients* `𝒮` on `Σ(A) × Σ(B)` consists of a family `(Γ_{σ,τ})` of abelian groups, where `Γ_{σ,τ}` depends only on
the sets `|σ|` and `|τ|`, and a family of homomorphisms `Γ_{σ,τ} → Γ_{σ',τ'}` for `(σ, τ) ≤ (σ', τ')`, forming an
*inductive system* for this preorder relation. One then defines a *cochain complex* `C^•(A, B; 𝒮)` as the set of
families `λ = (λ(σ, τ))` where `(σ, τ)` runs over `Σ(A) × Σ(B)`, with `λ(σ, τ) ∈ Γ_{σ,τ}` for every pair `(σ, τ)`. The
differential is given as follows: if `d(σ, τ) = ∑_i ± (σ_i, τ_i)`, one has `|σ_i| ⊂ |σ|`, `|τ_i| ⊂ |τ|` for every `i`,
and one takes

```text
  dλ(σ, τ) = ∑_i ± λ_i(σ_i, τ_i),
```

where `λ_i(σ_i, τ_i)` denotes the canonical image of `λ(σ_i, τ_i)` in `Γ_{σ,τ}`.

We shall say that a cochain `λ ∈ C^•(A, B; 𝒮)` is *bi-alternating* if `λ(σ, τ) = 0` whenever one of the two simplices
`σ`, `τ` has two equal terms, and if `λ(π(σ), τ) = ε_π λ(σ, τ)` and `λ(σ, π'(τ)) = ε_{π'} λ(σ, τ)` for arbitrary
permutations `π`, `π'` of the indices. It is clear that these cochains generate a subcomplex `L^•(A, B; 𝒮)` of
`C^•(A, B; 𝒮)`.

**Proposition (11.8.5).**

<!-- label: 0_III.11.8.5 -->

The canonical injection `L^•(A, B; 𝒮) → C^•(A, B; 𝒮)` defines an isomorphism for the cohomology of these two complexes.

**Proof.** Note that if `p` and `j` have the meaning defined in `(11.8.2)`, the maps `^t p : λ ↦ λ ∘ p` and
`^t j : λ ↦ λ ∘ j` are defined in `L^•(A, B; 𝒮)` and `C^•(A, B; 𝒮)` respectively, the first being none other than the
canonical injection. Since `^t j ∘ ^t p` is the identity, it suffices to show that `^t p ∘ ^t j` is homotopic to the
identity; now, by `(11.8.3)`, `^t h : λ ↦ λ ∘ h` is defined in `C^•(A, B; 𝒮)` and one can therefore transpose the
identity `(11.8.3.1)`, which yields the desired result.

<!-- original page 389 -->

**11.8.6.**

<!-- label: 0_III.11.8.6 -->

Proposition `(11.8.5)` reduces the computation of the cohomology of `L^•(A, B; 𝒮)` to that of the cohomology of
`C^•(A, B; 𝒮)`. Recall on the other hand that this last is, by the Eilenberg–Zilber theorem `(G, I, 3.10.2)`,
canonically isomorphic to the cohomology of the cochain complex defined as follows: one forms the chain complex
`P_•(A, B)`, consisting of the linear combinations of the `(σ, τ) ∈ Σ(A) × Σ(B)` such that `σ` and `τ` have *the same
degree*; the differential of this complex is given by `d : (σ, τ) ↦ ∑_{j, k} (−1)^{j+k} (σ_j, τ_k)` if
`dσ = ∑_j (−1)^j σ_j` and `dτ = ∑_k (−1)^k τ_k`; one then has two canonical homomorphisms of complexes

```text
  f : P_•(A, B) → C_•(A) ⊗ C_•(B),    g : C_•(A) ⊗ C_•(B) → P_•(A, B),
```

and one shows `(loc. cit.)` that there are homotopies `h`, `h'` such that

```text
  f ∘ g − 1 = d ∘ h + h ∘ d    and    g ∘ f − 1 = d ∘ h' + h' ∘ d.
```

Moreover, one has `f(σ, τ) ∈ C_•(|σ|) ⊗ C_•(|τ|)` and `g(σ, τ) ∈ P_•(|σ|, |τ|)` and the homotopies `h`, `h'` may be
taken such that `h(σ, τ) ∈ C_•(|σ|) ⊗ C_•(|τ|)` and `h'(σ, τ) ∈ P_•(|σ|, |τ|)`. This point arises from the fact that the
definition of `h(σ, τ)` and `h'(σ, τ)` can be made by induction on the sum of the degrees of `σ` and `τ`, and from the
fact that the `H^q(C_•(|σ|) ⊗ C_•(|τ|))` and `H^q(P_•(|σ|, |τ|))` are zero for `q > 0` `(loc. cit.)`; one reasons then
as in `(11.8.3)` and the conclusion follows.

One then defines `P^•(A, B; 𝒮)` as the set of families `λ = (λ(σ, τ))` where `(σ, τ)` runs over the pairs whose terms
have the same degree, with `λ(σ, τ) ∈ Γ_{σ,τ}`, and since one has `dσ = ∑_j (−1)^j σ_j ∈ C_•(|σ|)` and
`dτ = ∑_k (−1)^k τ_k ∈ C_•(|τ|)`,

```text
  dλ(σ, τ) = ∑_{j, k} (−1)^{j+k} λ_{j,k}(σ_j, τ_k)
```

is defined and gives the differential of the complex `P^•(A, B; 𝒮)`. With this, the maps `^t f : λ ↦ λ ∘ f`,
`^t g : λ ↦ λ ∘ g`, `^t h : λ ↦ λ ∘ h` and `^t h' : λ ↦ λ ∘ h'` are all defined by virtue of the preceding remarks;
`^t f ∘ ^t g` and `^t g ∘ ^t f` are therefore homotopic to the identity, whence the desired isomorphism between the
cohomology of `C^•(A, B; 𝒮)` and that of `P^•(A, B; 𝒮)`.

**Remark (11.8.7).**

<!-- label: 0_III.11.8.7 -->

The same reasoning as in `(11.8.3)`, but applied to `C_•(A)` and `L_•(A)`, shows that if `j` and `p` are defined as in
`(11.8.1)`, `f = j ∘ p` verifies once more a relation `(11.8.3.1)`, with `|h(σ)| ⊂ |σ|`, whence one deduces as in
`(11.8.5)` an isomorphism of the cohomology of `L^•(A; 𝒮)` onto that of `C^•(A; 𝒮)`, these two complexes being defined
obviously. This is the result whose proof is sketched in `(G, I, 3.8.1)`.

**11.8.8.**

<!-- label: 0_III.11.8.8 -->

Take up now the notation and hypotheses of `(11.8.2)`, and consider a *complex* `𝒮^• = (𝒮^k)` of systems of coefficients
on `Σ(A) × Σ(B)`: for each `(σ, τ)`, the `Γ_{σ,τ}^k` therefore form a complex of abelian groups `(k ∈ ℤ)`, and one has
the commutative diagrams

```text
              Γ_{σ,τ}^k       →       Γ_{σ,τ}^{k+1}
                  ↓                          ↓
              Γ_{σ',τ'}^k     →       Γ_{σ',τ'}^{k+1}
```

<!-- original page 390 -->

for `(σ, τ) ≤ (σ', τ')`. Then one verifies at once that `C^•(A, B; 𝒮^•) = (C^h(A, B; 𝒮^k))_{(h, k) ∈ ℤ × ℤ}` is a
*bicomplex* of abelian groups, and `L^•(A, B; 𝒮^•) = (L^h(A, B; 𝒮^k))` is a sub-bicomplex of it.

**Proposition (11.8.9).**

<!-- label: 0_III.11.8.9 -->

The canonical injection `L^•(A, B; 𝒮^•) → C^•(A, B; 𝒮^•)` defines an isomorphism for the cohomology of these two
bicomplexes.

**Proof.** Set `C^{•,•} = C^•(A, B; 𝒮^•)` and `L^{•,•} = L^•(A, B; 𝒮^•)` for simplicity, and note that since
`C^{hk} = L^{hk} = 0` for `h < 0`, the second spectral sequences of these bicomplexes are regular `(11.3.3)`; the
homomorphism `L^{•,•} → C^{•,•}` therefore gives a morphism of spectral sequences `″E(L^{•,•}) → ″E(C^{•,•})` which, for
the terms `E_2`, reduces to

```text
  H_{II}^p(H_I^q(L^{•,•})) → H_{II}^p(H_I^q(C^{•,•})).                          (11.8.9.1)
```

But for every `k ∈ ℤ`, it follows from `(11.8.3)` that the homomorphism `H_I^q(L^{•,k}) → H_I^q(C^{•,k})` is bijective;
the conclusion therefore follows from `(11.1.5)`.

**11.8.10.**

<!-- label: 0_III.11.8.10 -->

Likewise, with the notation of `(11.8.6)`, one has canonical homomorphisms of bicomplexes
`C^•(A, B; 𝒮^•) → P^•(A, B; 𝒮^•)` (with obvious notation), and the same reasoning as in `(11.8.9)`, based this time on
`(11.8.6)`, shows that this homomorphism again gives an isomorphism in cohomology.

### 11.9. A lemma on complexes of finite type

**Proposition (11.9.1).**

<!-- label: 0_III.11.9.1 -->

Let `𝒞` be an abelian category, `𝒦'` and `𝒦″` parts of the set of objects of `𝒞`, such that `𝒦″ ⊂ 𝒦'`, and verifying the
following conditions:

(i) For every object `A' ∈ 𝒦'` and every epimorphism `u : A → A'` in `𝒞`, there exists an object `B ∈ 𝒦″` and a morphism
`v : B → A` such that `uv` is an epimorphism.

(ii) For every pair of objects `A ∈ 𝒦″`, `B ∈ 𝒦'` and every epimorphism `u : A → B`, `Ker(u)` belongs to `𝒦'`.

(iii) The product of two objects of `𝒦″` belongs to `𝒦″`.

Let `P_• = (P_i)_{i ∈ ℤ}` be a complex in `𝒞`, such that `H_i(P_•) ∈ 𝒦'` for every `i`, and such that there exists `d`
with `H_i(P_•) = 0` for `i < d`. Then there exists a complex `Q_• = (Q_i)_{i ∈ ℤ}` in `𝒞` such that `Q_i ∈ 𝒦″` for every
`i` and `Q_i = 0` for `i < d`, and a morphism `u : Q_• → P_•` of complexes such that the corresponding morphism
`H_•(Q_•) → H_•(P_•)` is an isomorphism.

**Proof.** Let us first prove the following consequence of property (i):

(i bis) *Let `u : C → B` be an epimorphism in `𝒞`, `A` an object of `𝒦'`, `v : A → B` a morphism in `𝒞`; then there
exists an object `D ∈ 𝒦″`, an epimorphism `u' : D → A` and a morphism `v' : D → C` such that the diagram*

```text
                u'
            D    →    A
            ↓         ↓                                                        (11.9.1.1)
           v'         v
            ↓         ↓
            C    →    B
                u
```

*is commutative.*

Indeed, consider the fibre product `C ×_B A` in `𝒞` and the canonical projections `p : C ×_B A → C`, `q : C ×_B A → A`,
making the diagram

<!-- original page 391 -->

```text
                          q
            C ×_B A    →    A
                ↓             ↓                                                (11.9.1.2)
                p             v
                ↓             ↓
                C    →     B
                       u
```

commutative.

It is known `([27], p. I-12)` that the cokernel of `q` is the quotient of `A` by `v^{-1}(u(C))`; since `u` is an
epimorphism, `u(C) = B` and `v^{-1}(u(C)) = A`, hence `q` is an epimorphism; it then suffices to apply (i) to the
epimorphism `q : C ×_B A → A`: there is an object `D ∈ 𝒦″` and a morphism `w : D → C ×_B A` such that `qw` is an
epimorphism; one takes `u' = qw`, `v' = pw`.

That being said, to prove the proposition, we proceed by induction. Suppose, for some `i ≥ d − 1`, we have constructed,
for `j ≤ i`, the objects `Q_j`, the morphisms `d_j : Q_j → Q_{j-1}` and the morphisms `u_j : Q_j → P_j` so that
`Q_j = 0` for `j < d`, that `d_{j-1} ∘ d_j = 0` and `d_j ∘ u_j = u_{j-1} ∘ d_j` for `j ≤ i`; in addition, we suppose
verified the following conditions:

(I_i) One has `Q_j ∈ 𝒦″` for `j ≤ i` and `B_j(Q_•) ∈ 𝒦'` for `j < i`.

(II_i) For `j < i`, the homomorphism `H_j(Q_•) → H_j(P_•)` deduced from the family `(u_k)_{k ≤ i}` is an isomorphism.

(III_i) The composite morphism `v_i : Z_i(Q_•) → Z_i(P_•) → H_i(P_•)` (where the left arrow is the restriction of `u_i`
and the right arrow is the canonical morphism) is an epimorphism.

Note that, by (ii), `Z_i(Q_•)`, the kernel of the epimorphism `Q_i → B_{i-1}(Q_•)`, belongs to `𝒦'` by virtue of
hypothesis (I_i). One again deduces from (ii) that `N_i = Ker(v_i)` also belongs to `𝒦'`, taking into account hypothesis
(III_i). By virtue of (i bis), there exists a `Q'_{i+1} ∈ 𝒦″`, an epimorphism `d'_{i+1} : Q'_{i+1} → N_i` and a morphism
`u'_{i+1} : Q'_{i+1} → P_{i+1}`, such that the diagram

```text
                   d'_{i+1}
            Q'_{i+1}      →      N_i
                ↓                  ↓                                           (11.9.1.3)
              u'_{i+1}              v_i
                ↓                  ↓
            P_{i+1}      →      B_i(P_•)
                       d_{i+1}
```

is commutative.

Since the canonical morphism `Z_{i+1}(P_•) → H_{i+1}(P_•)` is an epimorphism and `H_{i+1}(P_•) ∈ 𝒦'` by hypothesis, it
follows from (i) that there exists an object `Q″_{i+1} ∈ 𝒦″` and a morphism `u″_{i+1} : Q″_{i+1} → Z_{i+1}(P_•)` such
that the composite `Q″_{i+1} → Z_{i+1}(P_•) → H_{i+1}(P_•)` is an epimorphism. If one takes `d″_{i+1} : Q″_{i+1} → N_i`
equal to `0`, the diagram

```text
                   d″_{i+1}
            Q″_{i+1}      →      N_i
                ↓                  ↓                                           (11.9.1.4)
              u″_{i+1}              v_i
                ↓                  ↓
            Z_{i+1}(P_•)  →      P_i
                       d_{i+1}
```

<!-- original page 392 -->

is commutative, the horizontal arrow at the bottom being `0`. Then take `Q_{i+1} = Q'_{i+1} × Q″_{i+1}`, which belongs
to `𝒦″` by virtue of (iii), and `d_{i+1} = d'_{i+1} + d″_{i+1}`, `u_{i+1} = u'_{i+1} + u″_{i+1}`. Since
`d_{i+1}(Q_{i+1}) = d'_{i+1}(Q'_{i+1}) = N_i ⊂ Z_i(Q_•)`, one has `d_i ∘ d_{i+1} = 0` and, with the usual notation,
`B_i(Q_•) = N_i`, which verifies (I\_{i+1}). The commutativity of the diagrams `(11.9.1.3)` and `(11.9.1.4)` shows that
`d_{i+1} ∘ u_{i+1} = u_i ∘ d_{i+1}`. By definition of `N_i`, the morphism `H_i(Q_•) = Z_i(Q_•)/N_i → H_i(P_•)` deduced
from the system of the `u_k` (`k ≤ i + 1`) is the morphism deduced from `v_i` by passage to quotients, hence it is an
isomorphism since `v_i` is an epimorphism, whence (II\_{i+1}). Finally, one has `Q″_{i+1} ⊂ Z_{i+1}(Q_•)` by definition;
the choice of `u″_{i+1}` shows that the morphism `v_{i+1} : Z_{i+1}(Q_•) → Z_{i+1}(P_•) → H_{i+1}(P_•)` is an
epimorphism, its restriction to `Q″_{i+1}` already being so, whence (III\_{i+1}). The induction can therefore continue,
and the proposition is proved.

**Corollary (11.9.2).**

<!-- label: 0_III.11.9.2 -->

Let `A` be a Noetherian ring (not necessarily commutative), `P_• = (P_i)_{i ∈ ℤ}` a complex of right `A`-modules.
Suppose that the `H_i(P_•)` are `A`-modules of finite type and that there exists `d` such that `H_i(P_•) = 0` for
`i < d`. Then there exists a complex `Q_• = (Q_i)_{i ∈ ℤ}` formed of right `A`-modules free of finite rank, such that
`Q_i = 0` for `i < d`, and a homomorphism `u : Q_• → P_•` of complexes, such that the homomorphism `H_•(Q_•) → H_•(P_•)`
corresponding to `u` is bijective.

**Proof.** One applies `(11.9.1)` taking for `𝒞` the category of right `A`-modules, for `𝒦'` (resp. `𝒦″`) the set of
`A`-modules of finite type (resp. the set of `A`-modules free of finite rank); verification of conditions (i), (ii) and
(iii) of `(11.9.1)` is immediate, taking into account the hypothesis that `A` is Noetherian.

**Remarks (11.9.3).**

<!-- label: 0_III.11.9.3 -->

(i) Under the conditions of `(11.9.2)`, suppose moreover that the `P_i` are *flat* right `A`-modules. Then, for every
left `A`-module `M`, the homomorphism of complexes `u ⊗ 1 : Q_• ⊗_A M → P_• ⊗_A M` still defines an isomorphism
`H_•(Q_• ⊗_A M) ⥲ H_•(P_• ⊗_A M)` of the homology, as we shall see in chap. III.

(ii) The conclusion of `(11.9.2)` is no longer necessarily exact when one does not suppose `A` Noetherian; indeed,
applying it to a complex reduced to `0` except for a single term, one would conclude that every left `A`-module of
finite type admits a resolution by free modules of finite type, which is not true in general (cf. Bourbaki, _Alg.
comm._, chap. I, § 2, exerc. 6).

However, instead of supposing `A` Noetherian, one may suppose only that the `H_i(P_•)` have an `∞`-presentation finite
(cf. chap. IV).

### 11.10. Euler–Poincaré characteristic of a complex of modules of finite length

**11.10.1.**

<!-- label: 0_III.11.10.1 -->

Let `A` be a ring (not necessarily commutative),

```text
  M^• : 0 → M^0 → M^1 → … → M^n → 0                                            (11.10.1.1)
```

a complex of left `A`-modules of finite length. One calls *Euler–Poincaré characteristic* of this complex the number

<!-- original page 393 -->

```text
  χ(M^•) = ∑_{i=0}^n (−1)^i long(M^i).                                          (11.10.1.2)
```

**Proposition (11.10.2).**

<!-- label: 0_III.11.10.2 -->

For every finite complex `M^•` of left `A`-modules of finite length, one has `χ(M^•) = χ(H^•(M^•))` (`H^•(M^•)` being
considered as a complex for the trivial derivation). In particular, if the sequence `(11.10.1.1)` is exact, one has
`χ(M^•) = 0`.

**Proof.** Set, to abbreviate, `B^i = B^i(M^•)`, `Z^i = Z^i(M^•)`, `H^i = H^i(M^•) = Z^i/B^i`; the `B^i`, `Z^i`, `H^i`
are of finite length. From the exact sequences

```text
  0 → B^i → Z^i → H^i → 0
  0 → Z^i → M^i → B^{i+1} → 0
```

one derives the relations

```text
  long(Z^i) = long(H^i) + long(B^i)
  long(M^i) = long(Z^i) + long(B^{i+1})
```

whence

```text
  long(M^i) − long(H^i) = long(B^{i+1}) + long(B^i)
```

Multiply this relation by `(−1)^i` and sum the relations obtained for `0 ≤ i ≤ n`, noting that `B^0 = B^{n+1} = 0`; the
desired equality follows.

**Corollary (11.10.3).**

<!-- label: 0_III.11.10.3 -->

Let `E = (E_r^{p,q})` be a spectral sequence in the category of modules over a ring `A`. Suppose that the `E_2^{p,q}`
are `A`-modules of finite length and that there are only finitely many pairs `(p, q)` such that `E_2^{p,q} ≠ 0`. Then
the Euler–Poincaré characteristics `χ(E_r^{(n)})` of all the complexes `E_r^{(n)} = (E_r^{p,q})_{p+q=n}` `(11.1.1)` are
all equal. If, in addition, the sequence `E` is weakly convergent and one sets `E_∞^{(n)} = ⊕_{p+q=n} E_∞^{p,q}` for
every `n ∈ ℤ`, one also has `χ(E_∞^{(•)}) = χ(E_2^{(•)})`, `E_∞^{(•)} = (E_∞^{(n)})_{n ∈ ℤ}` being considered as a
complex with trivial derivation.

**Proof.** Note first that if `E_2^{p,q} = 0`, one has `E_r^{p,q} = 0` for `2 ≤ r ≤ +∞`, so all the complexes
`E_r^{(•)}` are finite and formed of `A`-modules of finite length; the relation `χ(E_r^{(•)}) = χ(E_{r+1}^{(•)})` for
every finite `r` therefore follows from `(11.10.2)` and the isomorphism between `H^•(E_r^{(•)})` and `E_{r+1}^{(•)}` (as
complexes with trivial derivation). The hypothesis that the `E_2^{p,q}` are of finite length entails that for every pair
`(p, q)`, the sequences `(B_k(E_2^{p,q}))_{k ≥ 2}` and `(Z_k(E_2^{p,q}))_{k ≥ 2}` are stationary; the hypothesis that
`E` is weakly convergent and that `E_2^{p,q} = 0` except for finitely many pairs `(p, q)` entails therefore that there
exists an integer `r ≥ 2` such that `E_∞^{p,q} = E_r^{p,q}` for every pair `(p, q)`; whence the assertion concerning
`χ(E_∞^{(•)})`.

