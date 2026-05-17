<!-- original page 255 -->

## §21. Divisors

On the content of the present section, see the comments of the introduction to §20. For the global properties of
divisors, the reader is referred to the section devoted to them in chap. V.

### 21.1. Divisors on a ringed space

**(21.1.1).** Let `(X, 𝒪_X)` be a ringed space, `𝓜_X` the sheaf of germs of meromorphic functions on `X` `(20.1.3)`,
`𝓜_X^×` the sheaf (of multiplicative groups) of germs of regular meromorphic functions on `X` `(20.1.8)`. It is clear
that the sheaf (of multiplicative groups) `𝒪_X^×` of germs of invertible sections of `𝒪_X` is canonically identified
with a subsheaf (of multiplicative groups) of `𝓜_X^×`.

**Definition (21.1.2).**

<!-- label: IV.21.1.2 -->

*One calls **sheaf of divisors on `X`** and denotes by `𝒟iv_X` the quotient sheaf (of commutative groups)
`𝓜_X^× / 𝒪_X^×`; the sections of this sheaf over `X` are called **divisors on `X`**; they form a commutative group
denoted `Div(X)`. For every section `f` of `𝓜_X^×` over `X` (in other words, every regular meromorphic function on `X`
`(20.1.8)`), one calls **divisor of `f`** and denotes by `div(f)` (or `div_X(f)`) the divisor on `X` image of `f` by the
canonical homomorphism `Γ(X, 𝓜_X^×) → Γ(X, 𝒟iv_X)`.*

The **support** of a divisor `D` is the closed set of `x ∈ X` such that `D_x ≠ 0`. One denotes it `Supp(D)`.

For every open `U` of `X`, one obviously has `𝓜_X^× | U = 𝓜_U^×`, `𝒪_X^× | U = 𝒪_U^×`, hence
`𝒟iv_X | U = 𝒟iv_U`, and consequently the sheaf `𝒟iv_X` is equal to the presheaf `U ↦ Div(U)`.

When `X = Spec(A)` is affine, one writes `Div(A)` instead of `Div(Spec(A))`.

**(21.1.3).** We shall always denote the group `Div(X)` of divisors on `X` *additively*. For two regular meromorphic
functions `f`, `g` on `X`, one therefore has

```text
  (21.1.3.1)             div(fg) = div(f) + div(g),

  (21.1.3.2)             div(f⁻¹) = −div(f).
```

By definition, for every regular meromorphic function `f` on `X`, one has the equivalence

```text
  (21.1.3.3)             div(f) = 0  ⟺  f ∈ Γ(X, 𝒪_X^×),
```

whence, for two regular meromorphic functions `f`, `g` on `X`,

```text
  (21.1.3.4)             div(f) = div(g)  ⟺  f = ug, u ∈ Γ(X, 𝒪_X^×).
```

**(21.1.4).** Let now `ℒ` be an invertible `𝒪_X`-Module, and let `s` be a regular meromorphic section `(20.1.8)` of `ℒ`
over `X`. Every `x ∈ X` possesses an open neighbourhood `U` such that `ℒ | U` is isomorphic to `𝒪_U`, hence
`𝓜_X(ℒ) | U` isomorphic to `𝓜_U`; by one of these isomorphisms, `s | U` corresponds to a section `f ∈ Γ(U, 𝓜_X^×)`,
and since two isomorphisms of `ℒ | U` onto `𝒪_U` differ only by multiplication by an element of `Γ(U, 𝒪_X^×)`
`(0_I, 5.4.3)`, the element `div_U(f)` of `Γ(U, 𝒟iv_X)` is independent of the chosen isomorphism; it is clear that these
elements (for variable `U`) are the restrictions of a section of `𝒟iv_X` over `X`, which one calls the **divisor of
`s`** and denotes `div(s)` (such a divisor is not necessarily of the form `div(g)` for a regular meromorphic function
`g` on `X`; see `(21.2.9)`). For `ℒ = 𝒪_X` the definition of `div(s)` coincides with that of `(21.1.2)`. If `ℒ`, `ℒ'`
are two invertible `𝒪_X`-Modules, `s` (resp. `s'`) a regular meromorphic section of `ℒ` (resp. `ℒ'`) over `X`, it is
immediate that one has

```text
  (21.1.4.1)             div(s ⊗ s') = div(s) + div(s')

  (21.1.4.2)             div(s^⊗ n) = n · div(s)        for every n ∈ ℤ
```

(`s⁻¹` being the regular meromorphic section of `ℒ⁻¹` over `X` defined in `(20.1.10)`), and, for two regular
meromorphic sections `s`, `s'` of `ℒ` over `X`, one has the relation

```text
  (21.1.4.3)             div(s) = div(s')  ⟺  s' = ts, with t ∈ Γ(X, 𝒪_X^×).
```

<!-- original page 256 -->

**(21.1.5).** The sheaf `𝒮(𝒪_X)` `(20.1.3)` whose sections over an open `U` of `X` are the regular elements of
`Γ(U, 𝒪_X)` is a subsheaf of monoids of `𝓜_X^×`; one can write

```text
  (21.1.5.1)             𝒮(𝒪_X) = 𝒪_X ∩ 𝓜_X^×.
```

If one denotes by `𝒮(𝒪_X)⁻¹` the sheaf whose sections over `U` are the inverses in `Γ(U, 𝓜_X^×)` of the elements of
`Γ(U, 𝒮(𝒪_X))`, it is clear that one has `Γ(U, 𝒮(𝒪_X)) ∩ Γ(U, 𝒮(𝒪_X)⁻¹) = Γ(U, 𝒪_X^×)`, hence

```text
  (21.1.5.2)             𝒮(𝒪_X) ∩ 𝒮(𝒪_X)⁻¹ = 𝒪_X^×.
```

**Definition (21.1.6).**

<!-- label: IV.21.1.6 -->

*The subsheaf of sets of `𝒟iv_X` that is the canonical image of the subsheaf `𝒮(𝒪_X)` of `𝓜_X^×` is denoted
`𝒟iv_X^+`; its sections over `X` are called **positive divisors on `X`**, and their set is denoted `Div^+(X)`.*

Since `𝒮(𝒪_X)` is a sheaf of (multiplicative) monoids, one has

```text
  (21.1.6.1)             Div^+(X) + Div^+(X) ⊂ Div^+(X)
```

and on the other hand, by virtue of `(21.1.5.2)` and `(21.1.3.3)`,

```text
  (21.1.6.2)             Div^+(X) ∩ (−Div^+(X)) = {0}.
```

These two relations show that `Div^+(X)` is the set of positive elements for an order structure on the group `Div(X)`,
compatible with this group structure; one denotes this order relation `D ≥ D'`; in other words, one has

```text
  (21.1.6.3)             D ≥ 0  ⟺  D ∈ Div^+(X).
```

We shall always assume in what follows that `Div(X)` is endowed with this order structure; it is clear that
`𝒟iv_X^+ | U = 𝒟iv_U^+`, hence `Γ(U, 𝒟iv_X^+) = Div^+(U)`, and one can therefore say that `𝒟iv_X^+` defines on
`𝒟iv_X` a structure of sheaf of ordered groups. The stalk `(𝒟iv_X)_x` at a point `x` of the sheaf `𝒟iv_X` is a
submonoid of the group `(𝒟iv_X)_x`, the set of elements `≥ 0` for an order structure compatible with the group
structure; for a divisor `D` on `X`, it amounts to the same to say that `D ≥ 0` or that `D_x ≥ 0` for every `x ∈ X`.

By definition, for every regular meromorphic function `f` on `X`, one has the relation

```text
  (21.1.6.4)             div(f) ≥ 0  ⟺  f ∈ Γ(X, 𝒮(𝒪_X));
```

in other words, `div(f) ≥ 0` signifies that `f` is a regular section of `𝒪_X`, or also a section of `𝒪_X` invertible in
`M(X)`.

More generally, given a divisor `D` on `X`, the relation `div(f) ≥ D` is equivalent to the following: for every open
`U` of `X` such that `D | U = div_U(g)`, where `g ∈ Γ(U, 𝓜_X^×)`, there exists a regular element `t` of
`Γ(U, 𝒪_X)` such that `f | U = tg`.

**(21.1.7).** Let `ℒ` be an invertible `𝒪_X`-Module, `s` a regular meromorphic section of `ℒ` over `X`; one has the
relation

```text
  (21.1.7.1)             div(s) ≥ 0  ⟺  s ∈ Γ(X, ℒ) ∩ Γ(X, (𝓜_X(ℒ))^×)
```

as follows at once from the definitions `(21.1.4)` and `(21.1.6)`.

**Proposition (21.1.8).**

<!-- label: IV.21.1.8 -->

*Let `X` be a locally Noetherian prescheme, `D` a divisor on `X`. Suppose that for every `x ∈ X` such that
`prof(𝒪_{X,x}) = 1` one has `D_x ≥ 0` (resp. `D_x = 0`). Then one has `D ≥ 0` (resp. `D = 0`).*

The question being local on `X`, one may assume that `D = div(f)`, `f` being a

<!-- original page 257 -->

regular meromorphic function on `X`; the relation `D_x ≥ 0` is equivalent to `x ∈ dom(f)`, hence the hypothesis means
that if `T = X − dom(f)`, one has `prof(𝒪_{X,x}) ≥ 2` for every `x ∈ T` (since `dom(f)` contains the maximal points of
`X`). Consequently `(5.10.5)` the restriction homomorphism `Γ(X, 𝒪_X) → Γ(X − T, 𝒪_X)` is bijective, which shows that
there exists a section `s` of `𝒪_X` over `X` such that `f = s | (X − T)`. But by definition of `T`, this implies
`T = ∅`, hence `f = s` and `D ≥ 0`. The assertion relative to the relation `D_x = 0` follows at once by applying what
precedes to `−D`, by virtue of `(21.1.6.2)`.

**Corollary (21.1.9).**

<!-- label: IV.21.1.9 -->

*Let `X` be a locally Noetherian prescheme, `D` a divisor on `X`. Let `S` be the support of `D`. Then, for every
maximal point `x` of `S`, one has `prof(𝒪_{X,x}) ≤ 1`.*

Indeed set `X_1 = Spec(𝒪_{X,x})`; in view of `(20.2.11)` and `(20.3.6)`, the sheaf `𝒪_X` is induced on `X_1` by `𝒪_X`,
hence one may restrict to the case where `X = X_1`, in which case, since `x ∈ S` and `x` is a maximal point of `S`, one
necessarily has `S = {x}`. If one had `prof(𝒪_{X,x}) ≠ 1`, one would conclude, by virtue of `(21.1.8)`, that `D = 0`,
which contradicts the definition of `S`.

**Proposition (21.1.10).**

<!-- label: IV.21.1.10 -->

*Let `A` be a Noetherian local ring; for `Div(A) = 0`, it is necessary and sufficient that `prof(A) = 0` (in other
words, that the maximal ideal `𝔪` of `A` be associated to `A` `(0, 16.4.6)`).*

Indeed, to say that `Div(A) = 0` means that in `A` every regular element is invertible, or also that all the elements
of `𝔪` are zero-divisors, which means that `𝔪 ∈ Ass(A)` (Bourbaki, _Alg. comm._, chap. IV, §1, n° 1, cor. 3 of prop. 2).

### 21.2. Divisors and invertible fractional Ideals

**(21.2.1).** Let `(X, 𝒪_X)` be a ringed space. One calls **fractional Ideal on `X`** a sub-`𝒪_X`-Module of the
`𝒪_X`-Module `𝓜_X` of germs of meromorphic functions on `X`. A fractional Ideal `ℐ` on `X` which is an invertible
`𝒪_X`-Module is called an **invertible fractional Ideal**.

**Proposition (21.2.2).**

<!-- label: IV.21.2.2 -->

*For a fractional Ideal `ℐ` on `X` to be invertible, it is necessary and sufficient that for every `x ∈ X`, there exist
an open neighbourhood `U` of `x` and a section `f ∈ Γ(U, 𝓜_X^×)` such that `ℐ | U = 𝒪_U · f`.*

The condition is obviously sufficient, the map `s ↦ s · (f | V)` from `Γ(V, 𝒪_X)` to `Γ(V, ℐ)` being obviously
bijective for every open `V ⊂ U`. To see that it is necessary, note that by hypothesis there exist an open
neighbourhood `U` of `x` and an isomorphism of `𝒪_X`-Modules `𝒪_U ⥲ ℐ | U`. If `f` is the image of the section
`1 ∈ Γ(U, 𝒪_X)` by this isomorphism, one may assume, restricting `U`, that `f = u⁻¹s`, where `u ∈ Γ(U, 𝒪_X)` and
`s ∈ Γ(U, 𝒮(𝒪_X))`, and the considered isomorphism then makes correspond, to every section `v ∈ Γ(V, 𝒪_X)` (where `V`
is an open contained in `U`) the section `v(u | V)⁻¹ f(s | V)⁻¹`; to say that the map thus defined is bijective means
that `u | V` is a regular element of `Γ(V, 𝒪_X)`, hence `f ∈ Γ(U, 𝓜_X^×)`.

One will note that for every open `U` of `X` such that `ℐ | U = 𝒪_U · f` with `f ∈ Γ(U, 𝓜_X^×)`, the section `f` is
determined up to multiplication by an element of `Γ(U, 𝒪_X^×)`, since the

<!-- original page 258 -->

multiplication by these elements provides all the automorphisms of the `𝒪_U`-Module `𝒪_U` `(0_I, 5.4.3)`.

**Corollary (21.2.3).**

<!-- label: IV.21.2.3 -->

*(i) Let `ℐ` be an invertible fractional Ideal; then the invertible `𝒪_X`-Module `ℐ⁻¹` is canonically identified with the
fractional Ideal `ℐ'` (transporter of `ℐ` into `𝒪_X`) defined in the following way: for every open `U` of `X` such that
`ℐ | U = 𝒪_U · f`, where `f ∈ Γ(U, 𝓜_X^×)`, one has `ℐ' | U = 𝒪_U · f⁻¹`.*

*(ii) If `ℐ_1` and `ℐ_2` are two invertible fractional Ideals, the canonical map `ℐ_1 ⊗ ℐ_2 → ℐ_1 ℐ_2` is an isomorphism
of `𝒪_X`-Modules.*

Assertion (ii) follows at once from `(21.2.2)`. On the other hand, the remark made at the end of `(21.2.2)` shows that
there exists indeed one and only one fractional Ideal `ℐ'` defined by the condition of the statement; the canonical
isomorphism of `ℐ'` onto `ℐ⁻¹ = 𝓗𝑜𝑚_{𝒪_X}(ℐ, 𝒪_X)` is obtained by making correspond to every section
`s ∈ Γ(V, ℐ⁻¹)` (where `V` is an open contained in `U` and `f ∈ Γ(V, 𝓜_X^×)`) the homomorphism
`t(f | V)⁻¹ ↦ st` from `Γ(V, ℐ)` to `Γ(V, 𝒪_X)`.

By virtue of `(21.2.3, (i))`, one will generally identify the `𝒪_X`-Modules `ℐ'` and `ℐ⁻¹`, considering therefore
`ℐ⁻¹` as a sub-`𝒪_X`-Module of `𝓜_X`.

**(21.2.4).** It follows from `(21.2.3)` that the set `Id.inv(X)` of *invertible fractional Ideals on `X`* is endowed
with a structure of commutative group for the composition law `(ℐ_1, ℐ_2) ↦ ℐ_1 ℐ_2`, the neutral element of this group
being `𝒪_X`. It is clear that for every open `U` of `X`, one has
`(ℐ_1 ℐ_2) | U = (ℐ_1 | U)(ℐ_2 | U)`, hence the restriction map `ℐ ↦ ℐ | U` is a homomorphism of groups
`Id.inv(X) → Id.inv(U)`; one thus defines a *presheaf of commutative groups* `U ↦ Id.inv(U)`; it is immediate that in
fact this presheaf is a *sheaf of commutative groups*, which one denotes `𝐼𝑑.𝑖𝑛𝑣_X`.

**(21.2.5).** For every regular meromorphic function `f ∈ Γ(X, 𝓜_X^×)`, it follows from `(21.2.2)` that
`𝒥(f) = 𝒪_X · f` is an invertible fractional Ideal, and one obviously has `𝒥(f_1 f_2) = 𝒥(f_1) 𝒥(f_2)`; in other words
the map `f ↦ 𝒥(f)` is a homomorphism from the commutative group `Γ(X, 𝓜_X^×)` into the commutative group `Id.inv(X)`.
Replacing `X` by any open `U` of `X` and noting that the homomorphisms obtained are compatible with the operations of
restriction, one obtains a canonical homomorphism of sheaves of commutative groups:

```text
  (21.2.5.1)             𝒥 : 𝓜_X^× → 𝐼𝑑.𝑖𝑛𝑣_X.
```

Note that if `f ∈ Γ(X, 𝒪_X^×)`, one has `𝒥(f) = 𝒪_X`; one deduces at once that the homomorphism `𝒥` factors as

```text
  (21.2.5.2)             𝓜_X^× → 𝓜_X^× / 𝒪_X^× = 𝒟iv_X → 𝐼𝑑.𝑖𝑛𝑣_X
```

<!-- original page 259 -->

where `𝐼` is a homomorphism from the sheaf of additive groups `𝒟iv_X` into the sheaf of multiplicative groups
`𝐼𝑑.𝑖𝑛𝑣_X`; one therefore has for every open `U` of `X` a homomorphism `𝐼_U : Div(U) → Id.inv(U)` of commutative groups,
such that, for every section `f ∈ Γ(U, 𝓜_X^×)`, one has

```text
  (21.2.5.3)             𝐼_U(div_U(f)) = 𝒪_U · f.
```

One concludes that `𝐼(D)`, for every divisor `D ∈ Div(X)`, is the invertible fractional Ideal defined in the following
way: for every open `U` of `X` such that `D | U = div_U(f)`, where `f ∈ Γ(U, 𝓜_X^×)`, `𝐼(D) | U` is the invertible
fractional Ideal `𝒪_U · f`. One therefore has, by virtue of `(21.1.6)`, for every regular meromorphic function
`f ∈ Γ(X, 𝓜_X^×)`, the relation

```text
  (21.2.5.4)             f ∈ Γ(X, 𝐼(D))  ⟺  div(f) ≥ D.
```

**Proposition (21.2.6).**

<!-- label: IV.21.2.6 -->

*The homomorphism `𝐼 : 𝒟iv_X → 𝐼𝑑.𝑖𝑛𝑣_X` is bijective.*

One defines a homomorphism `𝐼_X'` from `Id.inv(X)` into `Div(X)` by making correspond to every invertible fractional
Ideal `ℐ` on `X` the divisor `𝐼_X'(ℐ)` defined in the following way: for every open `U` of `X` such that
`ℐ | U = 𝒪_U · f`, where `f ∈ Γ(U, 𝓜_X^×)` `(21.2.2)`, one takes `𝐼_X'(ℐ) | U = div_U(f)`; by virtue of the remark
following `(21.2.2)`, this definition is independent of the generator `f` chosen in `ℐ | U`, and determines indeed a
divisor on `X`. Moreover, this definition shows at once that the homomorphisms `𝐼_X` and `𝐼_X'` are reciprocal to one
another. Replacing `X` by any open `U`, one deduces the definition of the isomorphism `𝐼' : 𝐼𝑑.𝑖𝑛𝑣_X → 𝒟iv_X`
reciprocal to `𝐼`, whence the proposition. One will set `𝐼_X'(ℐ) = div(ℐ)`, so that one has, for every regular
meromorphic function `f` on `X`,

```text
  (21.2.6.1)             div(𝒪_X · f) = div(f).
```

**(21.2.7).** One will often *identify* the sheaves `𝒟iv_X` and `𝐼𝑑.𝑖𝑛𝑣_X` (resp. the groups `Div(X)` and `Id.inv(X)`)
by means of the preceding isomorphisms `𝐼` and `𝐼'` (resp. `𝐼_X` and `𝐼_X'`). One will note that one has the relation

```text
  (21.2.7.1)             D ≥ 0  ⟺  𝐼_X(D) ⊂ 𝒪_X       for D ∈ Div(X)
```

as follows at once from the definitions `(21.1.6)` and `(21.1.5.1)`; in other words, the image
`𝐼_X(Div^+(X))` is the set of Ideals of `𝒪_X` (also sometimes called *integral Ideals*) that are invertible
`𝒪_X`-Modules: such an Ideal `ℐ` is again characterized by the fact that for every `x ∈ X`, there is an open
neighbourhood `U` of `x` in `X` such that `ℐ | U = 𝒪_U · f`, where `f` is a regular element of `Γ(U, 𝒪_X)`. The set
`𝐼_X(Div^+(X))` of these Ideals is therefore a submonoid of `Id.inv(X)`, equal to the set of positive elements for an
order relation compatible with the group structure of `Id.inv(X)`, and it is immediate that this relation is none other
than the relation opposite to inclusion; in other words, one has

```text
  (21.2.7.2)             ℐ_1 ⊂ ℐ_2  ⟺  div(ℐ_1) ≥ div(ℐ_2)
```

for `ℐ_1`, `ℐ_2` in `Id.inv(X)`.

**(21.2.8).** For every divisor `D` on `X`, one sets

```text
  (21.2.8.1)             𝒪_X(D) = (𝐼_X(D))⁻¹;
```

`𝒪_X(D)` is therefore an invertible fractional Ideal, defined in the following way: for every open `U` of `X`

<!-- original page 260 -->

such that `D | U = div_U(f)`, where `f ∈ Γ(U, 𝓜_X^×)`, `𝒪_X(D) | U` is the invertible fractional Ideal `𝒪_U · f⁻¹`; by
virtue of `(21.1.6)`, for every regular meromorphic function `f`, one has the relation

```text
  (21.2.8.2)             f ∈ Γ(X, 𝒪_X(D))  ⟺  div(f) ≥ −D.
```

Moreover, it is clear that one has canonical isomorphisms `(21.2.3)`

```text
  (21.2.8.3)             𝒪_X(0) = 𝒪_X,   𝒪_X(D + D') = 𝒪_X(D) ⊗ 𝒪_X(D'),
                         𝒪_X(nD) = (𝒪_X(D))^⊗ n,   𝒪_X(−D) = (𝒪_X(D))⁻¹
```

for every integer `n ∈ ℤ`, and for any two divisors `D`, `D'` on `X`.

**(21.2.9).** Let `ℐ` be an invertible fractional Ideal on `X`. The canonical injection `ℐ → 𝓜_X` defines by
tensorization a homomorphism of `𝒪_X`-Modules

```text
  (21.2.9.1)             𝓜_X(ℐ) = ℐ ⊗_{𝒪_X} 𝓜_X → 𝓜_X ⊗_{𝒪_X} 𝓜_X = 𝓜_X
```

which is an isomorphism: indeed, if `U` is an open of `X` such that `ℐ | U = 𝒪_U · f`, where `f ∈ Γ(U, 𝓜_X^×)`, the
homomorphism `(21.2.9.1)` restricted to `U` is none other than the isomorphism that to every section `t` of
`𝓜_X(ℐ) | U = 𝓜_U` over `V ⊂ U` makes correspond the section `t (f | V)⁻¹` of the same sheaf. In the isomorphism
`(21.2.9.1)`, to the regular meromorphic sections of `ℐ` over `X` correspond the regular meromorphic functions on `X`.

Consider in particular the case where `ℐ = 𝒪_X(D)`, where `D` is a divisor on `X`; one then has a canonical isomorphism

```text
  (21.2.9.2)             𝓜_X(𝒪_X(D)) ⥲ 𝓜_X
```

and one denotes by `s_D` the regular meromorphic section of `𝒪_X(D)` over `X` which corresponds by this isomorphism to
the section `1` of `𝓜_X`. If `U` is an open of `X` such that `𝒪_X(D) | U = 𝒪_U · f⁻¹`, where `f ∈ Γ(U, 𝓜_X^×)`, one
has `s_D | U = f` in `Γ(U, 𝓜_X)`; since one then has `D | U = div_U(f)`, one deduces `(21.1.4)` that one has

```text
  (21.2.9.3)             div(s_D) = D.
```

On the other hand, one deduces at once from the canonical isomorphisms `(21.2.8.3)` the formulas

```text
  (21.2.9.4)             s_0 = 1,   s_{D + D'} = s_D ⊗ s_{D'},   s_{nD} = s_D^{⊗ n}   (n ∈ ℤ).
```

**(21.2.10).** Let us consider, between two pairs `(ℒ, s)`, `(ℒ', s')`, where `ℒ` and `ℒ'` are two invertible
`𝒪_X`-Modules, `s` (resp. `s'`) a regular meromorphic section of `ℒ` (resp. `ℒ'`) over `X`, the relation: "there exists
an isomorphism `u : ℒ ⥲ ℒ'` such that `ū(s) = s'`", where `ū : Γ(X, 𝓜_X(ℒ)) ⥲ Γ(X, 𝓜_X(ℒ'))` is the isomorphism
deduced from `u` (one will note that the isomorphism `u` verifying this condition is then uniquely determined). It is
clear that this is an equivalence relation, and since there exists a set of invertible `𝒪_X`-Modules such that every
invertible `𝒪_X`-Module is isomorphic to an element of this set `(0_I, 5.4.7)`, one can speak of the *set `D(X)` of
equivalence classes of pairs `(ℒ, s)`* for the preceding relation. For every invertible `𝒪_X`-Module `ℒ` and every

<!-- original page 261 -->

regular meromorphic section `s` of `ℒ` over `X`, one will denote by `cl(ℒ, s)` the element of `D(X)` corresponding to
the pair `(ℒ, s)`. It follows from `(0_I, 5.4.3)` that if `s`, `s'` are two regular meromorphic sections of `ℒ` over
`X`, the relation `cl(ℒ, s) = cl(ℒ, s')` is equivalent to the existence of a section `t ∈ Γ(X, 𝒪_X^×)` such that
`s' = ts`.

It is immediate that if `(ℒ, s)` is equivalent to `(ℒ_1, s_1)` and `(ℒ', s')` to `(ℒ_1', s_1')`, the pairs
`(ℒ ⊗ ℒ', s ⊗ s')` and `(ℒ_1 ⊗ ℒ_1', s_1 ⊗ s_1')` are equivalent; one therefore defines in `D(X)` a composition law by
setting

```text
  (21.2.10.1)            cl(ℒ, s) · cl(ℒ', s') = cl(ℒ ⊗ ℒ', s ⊗ s');
```

it is immediate that this is a commutative group law, whose neutral element is `cl(𝒪_X, 1)` and where the inverse of
`cl(ℒ, s)` is `cl(ℒ⁻¹, s^{⊗(−1)})`.

**Proposition (21.2.11).**

<!-- label: IV.21.2.11 -->

*The maps*

```text
  (21.2.11.1)            D ↦ cl(𝒪_X(D), s_D),       cl(ℒ, s) ↦ div(s)
```

*are reciprocal isomorphisms of `Div(X)` onto `D(X)` and of `D(X)` onto `Div(X)` respectively.*

In view of `(21.2.8.3)`, `(21.2.9.4)` and `(21.2.10.1)`, it suffices to see that the composites of these two maps are
the identity in `Div(X)` and `D(X)` respectively. The first assertion is none other than `(21.2.9.3)`. On the other
hand, let `D = div(s)`, where `s` is a regular meromorphic section of `ℒ` over `X`, and let `U` be an open of `X` such
that there exists an isomorphism of `ℒ | U` onto `𝒪_U` transforming `s | U` into `f ∈ Γ(U, 𝓜_X^×)`, so that
`D | U = div_U(f)`, `𝒪_X(D) | U = 𝒪_U · f⁻¹`, and `s_D | U` is the unit element of `Γ(U, 𝒪_X^×)`. There is therefore an
isomorphism `v_U : ℒ | U → 𝒪_U · f⁻¹ = 𝒪_X(D) | U` such that `v̄_U` (notation of `(21.2.10)`) transforms `s | U` into
`f · f⁻¹ = 1`; one sees at once that these isomorphisms are compatible with the operations of restriction, hence define
an isomorphism `v : ℒ → 𝒪_X(D)` such that `v̄(s) = s_D`. Q.E.D.

One can transport, by the first of the isomorphisms `(21.2.11.1)`, the ordered group structure of `Div(X)` to `D(X)`;
the elements `≥ 0` of `D(X)` are therefore the classes `cl(ℒ, s)` such that `div(s) ≥ 0`, that is to say `(21.1.7.1)`
such that

```text
                         s ∈ Γ(X, ℒ) ∩ Γ(X, (𝓜_X(ℒ))^×).
```

**(21.2.12).** Let `D` be a positive divisor on a prescheme `X`; the fractional Ideal `𝒪_X(D)` is therefore an Ideal of
`𝒪_X` which is an invertible `𝒪_X`-Module; let `Y(D)` be the closed sub-prescheme of `X` it defines. For every
`x ∈ Y(D)`, there is by hypothesis an open neighbourhood `U` of `x` in `X` and a regular section `t ∈ Γ(U, 𝒪_X)` such
that `𝒪_X(D) | U = 𝒪_U · t · (𝒪_X | U)`; in other words, the canonical immersion `Y(D) → X` is *regular and of
codimension `1`* `(19.1.4)` at every point of `Y(D)`. Conversely, if `Y` is a closed sub-prescheme of `X`, regularly
immersed in `X` and of codimension `1` at every point of `Y`, there exists *one and only one positive divisor* `D` such
that `Y(D) = Y`, for every `x ∈ Y`, there is a neighbourhood `U` of `x` in `X` such that `Y ∩ U` is defined by an Ideal
of `𝒪_X` of the form `𝒪_U · t`, where `t` is regular in `Γ(U, 𝒪_X)`.

One will note that one then has `Supp(D) = Y(D)`, for to say that `D_x ≠ 0` means that `t` (with the notations above)
is not invertible, that is to say that `x ∈ Y(D)`.

<!-- original page 262 -->

### 21.3. Linear equivalence of divisors

**(21.3.1).** One says that a divisor `D` on `X` is *principal* if it is of the form `div(f)`, where `f` is a regular
meromorphic function on `X`; the regular meromorphic functions `f'` such that `div(f') = D` are then all those of the
form `tf`, where `t ∈ Γ(X, 𝒪_X^×)` `(21.1.3.4)`. The set of principal divisors is a subgroup of `Div(X)`, denoted
`Div.princ(X)`, isomorphic to `Γ(X, 𝓜_X^×) / Γ(X, 𝒪_X^×)`. Two divisors `D`, `D'` are said to be *linearly equivalent*
if `D − D'` is a principal divisor; the principal divisors are therefore the divisors *linearly equivalent to `0`*.

**(21.3.2).** Recall `(0_I, 5.4.7)` that one can speak of the set of equivalence classes of invertible `𝒪_X`-Modules
for the relation of isomorphy; one denotes this set by `Pic(X)`, and for every invertible `𝒪_X`-Module `ℒ`, one denotes
by `cl(ℒ)` the equivalence class of `𝒪_X`-Modules isomorphic to `ℒ`; moreover, `Pic(X)` is a commutative group for the
multiplication defined by `cl(ℒ) cl(ℒ') = cl(ℒ ⊗ ℒ')`. It is clear that the map

```text
  (21.3.2.1)             𝓁' : cl(ℒ, s) ↦ cl(ℒ)
```

is a homomorphism from the group `D(X)` `(21.2.10)` into the group `Pic(X)`. By composition, one therefore deduces a
homomorphism

```text
  (21.3.2.2)             𝓁 : Div(X) ⥲ D(X) → Pic(X)
```

(also denoted `𝓁_X`) such that, for every divisor `D`, one has

```text
  (21.3.2.3)             𝓁(D) = cl(𝒪_X(D)).
```

Note finally that, if `u : X' → X` is a morphism of ringed spaces, `ℒ_1`, `ℒ_2` two isomorphic invertible
`𝒪_X`-Modules, the invertible `𝒪_{X'}`-Modules `u^*(ℒ_1)` and `u^*(ℒ_2)` `(0_I, 5.4.5)` are isomorphic; since moreover,
for any two invertible `𝒪_X`-Modules `ℒ_1`, `ℒ_2`, one has `u^*(ℒ_1 ⊗ ℒ_2) = u^*(ℒ_1) ⊗ u^*(ℒ_2)` up to canonical
isomorphism `(0_I, 4.3.3)`, one sees that the morphism `u` canonically defines a homomorphism of commutative groups

```text
  (21.3.2.4)             Pic(u) : Pic(X) → Pic(X').
```

**Proposition (21.3.3).**

<!-- label: IV.21.3.3 -->

*(i) The kernel of the canonical homomorphism `𝓁 : Div(X) → Pic(X)` is the subgroup `Div.princ(X)`; in other words, for
`𝒪_X(D)` and `𝒪_X(D')` to be isomorphic, it is necessary and sufficient that `D` and `D'` be linearly equivalent. One
therefore has a canonical injective homomorphism*

```text
  (21.3.3.1)             Div(X) / Div.princ(X) → Pic(X)
```

*deduced from `𝓁`.*

*(ii) For an invertible `𝒪_X`-Module `ℒ` to be such that `cl(ℒ)` is of the form `𝓁(D)`, or also for `ℒ` to be isomorphic
to an `𝒪_X`-Module of the form `𝒪_X(D)`, it is necessary and sufficient that there exist a regular meromorphic section
of `ℒ`.*

<!-- original page 263 -->

The proposition follows at once from the definitions and from `(21.2.10)`.

**Proposition (21.3.4).**

<!-- label: IV.21.3.4 -->

*Let `X` be a prescheme satisfying one of the two following hypotheses:*

*a) `X` is locally Noetherian and `Ass(𝒪_X)` is contained in an affine open of `X`.*

*b) `X` is reduced and the set of its irreducible components is locally finite.*

*Then the canonical homomorphism `𝓁 : Div(X) → Pic(X)` is surjective, and gives, by passage to the quotient, an
isomorphism*

```text
                         Div(X) / Div.princ(X) ⥲ Pic(X).
```

It suffices to show that every invertible `𝒪_X`-Module `ℒ` admits a regular meromorphic section over `X` `(21.3.3)`. In
the two cases, it suffices, thanks to `(20.2.11, (ii))`, to define a section `s` of `(𝓜_X(ℒ))^×` over a schematically
dense open `U` of `X`, or also in case a), over an open `U` containing `Ass(𝒪_X)` `(20.2.13, (iv))`. Indeed, let `V` be
any open of `X` such that `ℒ | V` is isomorphic to `𝒪_V`, so that there exists an isomorphism of `𝓜_X(ℒ) | V` onto
`𝓜_X | V`, transforming `s | (U ∩ V)` into a section `f_V` of `𝓜_X` over `U ∩ V`. Since `U ∩ V` is schematically dense
in `V`, it follows from `(20.2.11)` that there exists one and only one regular meromorphic function `g_V` on `V` such
that `g_V | (U ∩ V) = f_V`, and this section therefore corresponds, by the isomorphism considered, to a regular
meromorphic section `u_V` of `ℒ` over `V` such that `u_V | (U ∩ V) = s | (U ∩ V)`. Moreover, if `V'` is a second open
of `X` such that `ℒ | V'` is isomorphic to `𝒪_{V'}`, the restrictions of `u_V` and `u_{V'}` to `V ∩ V'` are equal, for
they correspond by isomorphism to two meromorphic functions which coincide in a schematically dense open `U ∩ V ∩ V'`,
and one concludes again by `(20.2.11)`; the `u_V` are therefore the restrictions of a section of `(𝓜_X(ℒ))^×` over `X`.

This being so, in case b), one takes for each of the maximal points `x_λ` of `X` an open `U_λ` containing `x_λ`, not
meeting any irreducible component of `X` distinct from `{x_λ}` and such that `ℒ | U_λ` is isomorphic to `𝒪_{U_λ}`; one
will take for `s` the section such that `s | U_λ` is the section of `ℒ | U_λ` corresponding by the preceding isomorphism
to the unit section of `𝒪_{U_λ}`.

In case a), one can take by hypothesis for `U` an affine open (hence Noetherian); in other words, one may assume that
`X = Spec(A)`, where `A` is Noetherian, and `ℒ = P̃`, where `P` is a projective `A`-module of rank `1`. If `S` is the
set of regular elements of `A`, one has `Γ(X, 𝓜_X) = S⁻¹ A` `(20.2.12)` and `Γ(X, 𝓜_X(ℒ)) = S⁻¹ P`. But `S` is the
set of elements not belonging to any of the ideals associated to `A`, hence `S⁻¹ A` is a semi-local ring whose maximal
ideals come from the maximal elements of `Ass(A)`, and `S⁻¹ P` is a projective `S⁻¹ A`-module of rank `1`, hence here
free of rank `1` (Bourbaki, _Alg. comm._, chap. II, §5, n° 3, prop. 5); an element forming a basis of this `S⁻¹ A`-module
is therefore `(20.1.8)` a regular meromorphic section of `ℒ` over `X`.

**Corollary (21.3.5).**

<!-- label: IV.21.3.5 -->

*If `X` is a Noetherian prescheme such that there exists an ample invertible `𝒪_X`-Module `(II, 4.5.3)` (for example a
quasi-projective prescheme over the spectrum of a Noetherian ring `(II, 5.3.1` and `4.6.6)`), the canonical
homomorphism `𝓁 : Div(X) → Pic(X)` is surjective.*

<!-- original page 264 -->

Indeed `(II, 4.5.4)`, there then exists an affine open neighbourhood of the finite set `Ass(𝒪_X)`.

**Remark (21.3.6).**

<!-- label: IV.21.3.6 -->

*Recall `(0_I, 5.4.7)` that one has a canonical isomorphism `π : H^1(X, 𝒪_X^×) ⥲ Pic(X)` defined in the following way.
One starts from a `1`-cocycle `(c_{αβ})` with values in `𝒪_X^×` corresponding to an open cover `(U_α)` of `X`, `c_{αβ}`
being an element of `Γ(U_α ∩ U_β, 𝒪_X^×)`, and one associates with it the class of the invertible `𝒪_X`-Module obtained
by gluing the `𝒪_{U_α}` along the isomorphisms `𝒪_X | (U_α ∩ U_β) ⥲ 𝒪_X | (U_α ∩ U_β)` defined by multiplication by
`c_{αβ}`. On the other hand, one deduces from the exact sequence of sheaves of commutative groups*

```text
                         1 → 𝒪_X^× → 𝓜_X^× → 𝒟iv_X → 0
```

*the connecting homomorphism of the exact cohomology sequence*

```text
  (21.3.6.1)             ∂ : Div(X) → H^1(X, 𝒪_X^×).
```

*Let us show that the composite homomorphism*

```text
                                                ∂              π
                         Div(X) → H^1(X, 𝒪_X^×) ⥲ Pic(X)
```

*is none other than the homomorphism `𝓁` defined in `(21.3.2.2)`. Indeed, one must start from a divisor `D` and an open
cover `(U_α)` of `X` such that `D | U_α = div_{U_α}(g_α)`, where `g_α` is a regular meromorphic function over `U_α`;
`∂(D)` is the cohomology class of the cocycle `(c_{αβ})`, where `c_{αβ} = g_{α|αβ} g_{β|αβ}⁻¹`, `g_{α|αβ}` denoting the
restriction of `g_α` to `U_α ∩ U_β`. It is clear that the image by `π` of this cohomology class is the class of the
invertible fractional Ideal `ℒ` such that for every `α`, `ℒ | U_α = 𝒪_{U_α} · g_α⁻¹`, which is none other by definition
than `𝒪_X(D)` `(21.2.8)`.*

### 21.4. Inverse images of divisors

**(21.4.1).** Let `f : X' → X` be a morphism of ringed spaces; we propose to give conditions allowing us to associate
with a divisor `D` on `X` a divisor `D'` on `X'`, *inverse image* of `D` by `f`. Note first for this that for every
section `t ∈ Γ(X, 𝒪_X^×)`, the image of `t` by the canonical homomorphism `Γ(X, 𝒪_X) → Γ(X', 𝒪_{X'})` is again
invertible, in other words belongs to `Γ(X', 𝒪_{X'}^×)`. Consider then `D` as given by the equivalence class of a pair
`(ℒ, s)`, where `ℒ` is an invertible `𝒪_X`-Module and `s` a regular meromorphic section of `ℒ` over `X` `(21.2.11)`.
Form the invertible `𝒪_{X'}`-Module `f^*(ℒ) = ℒ'`; to say that the inverse image `s ∘ f` of `s` by `f` exists
`(20.1.11)` and is a regular meromorphic section of `ℒ'` over `X'` amounts to saying that the inverse images by `f` of
`s` and of `s^{⊗(−1)}` exist, in other words that `s ∈ Γ(X, 𝓜_f(ℒ))` and `s^{⊗(−1)} ∈ Γ(X, 𝓜_f(ℒ⁻¹))`; the remark made
above then shows that if `(ℒ_1, s_1)` is a pair equivalent to `(ℒ, s)` in the sense of `(21.2.10)`, the inverse image
`s_1 ∘ f` exists and is a regular meromorphic section of `ℒ_1' = f^*(ℒ_1)` over `X'`, and the pairs `(ℒ', s ∘ f)` and
`(ℒ_1', s_1 ∘ f)` are equivalent. One can therefore lay down the following definition:

**Definition (21.4.2).**

<!-- label: IV.21.4.2 -->

*Given a morphism `f : X' → X` of ringed spaces, one says that the **inverse image** by `f` of a divisor `D` on `X`
**exists** if one has `s_D ∈ Γ(X, 𝓜_f(𝒪_X(D)))` and `s_{−D} ∈ Γ(X, 𝓜_f(𝒪_X(−D)))` (cf. `(20.1.11)`). One then calls
**inverse image** of `D` by `f`, and denotes by `f^*(D)`, the divisor on `X'` which corresponds canonically `(21.2.11)`
to the class of the pair `(f^*(𝒪_X(D)), s_D ∘ f)`.*

It follows at once from this definition that if `D` and `D'` have inverse images under `f`, so do `−D` and `D + D'`
(taking account of `(21.2.9.4)`) and that one has

<!-- original page 265 -->

`f^*(D + D') = f^*(D) + f^*(D')`. In other words, the set `Div_f(X)` of divisors on `X` whose inverse image by `f`
exists is a subgroup of `Div(X)`, and the map `D ↦ f^*(D)` is an increasing homomorphism from the ordered subgroup
`Div_f(X)` into the ordered group `Div(X')`, making commutative the diagram

```text
                         Div_f(X) ─𝓁_X─→ Pic(X)
                            │              │
  (21.4.2.1)              f^*│              │ Pic(f)
                            ↓              ↓
                         Div(X') ─𝓁_{X'}→ Pic(X')
```

**(21.4.3).** Definition `(21.4.2)` shows at once that, for `f^*(D)` to exist, it is necessary and sufficient that for
every open `U` of `X`, the inverse image by `f_U : f⁻¹(U) → U` (restriction of `f`) of `D | U` exist. Now, if
`D = div(g)`, where `g` is a regular meromorphic function on `X`, to say that the inverse image of `s_D` by `f` exists
and is a regular meromorphic section of `f^*(𝒪_X(D))` signifies `(21.2.9)` that the inverse image of `g` by `f` exists
and is a regular meromorphic function on `X'`. One deduces at once a second description of `Div_f(X)` and of `f^*(D)`:
consider the subsheaf of groups of `𝓜_X^×`, denoted `𝓜_X^{f×}`, formed of the germs of regular meromorphic functions
on an open of `X` whose inverse image by `f` exists and is regular on the inverse image open `(20.1.11)`. Then if
`f = (ψ, θ)`, the canonical homomorphism `(20.1.11)` `ψ^*(𝓜_X) → 𝓜_{X'}` gives by restriction a homomorphism of sheaves
of groups `ψ^*(𝓜_X^{f×}) → 𝓜_{X'}^×`. Setting `𝒟iv_X^f = 𝓜_X^{f×} / 𝒪_X^×`, one has `Div_f(X) = Γ(X, 𝒟iv_X^f)`, and the
map `D ↦ f^*(D)` corresponds to the homomorphism of sheaves of groups
`ψ^*(𝓜_X^{f×}) / ψ^*(𝒪_X^×) → 𝓜_{X'}^× / 𝒪_{X'}^× = 𝒟iv_{X'}` deduced from the preceding one by passage to the quotients.

**(21.4.4).** It follows at once from the preceding definitions that if `f' : X'' → X'` is a second morphism of ringed
spaces, `D` a divisor on `X` such that the inverse images `f^*(D)` and `f'^*(f^*(D))` exist, then `(f ∘ f')^*(D)`
exists and is equal to `f'^*(f^*(D))`.

**Proposition (21.4.5).**

<!-- label: IV.21.4.5 -->

*Let `f : X' → X` be a morphism of ringed spaces. In each of the three following cases, the inverse image by `f` of
every divisor on `X` is defined:*

*(i) `f` is flat.*

*(ii) `X` and `X'` are locally Noetherian preschemes and one has `f(Ass(𝒪_{X'})) ⊂ Ass(𝒪_X)`.*

*(iii) `X` and `X'` are preschemes, the set of irreducible components of `X` is locally finite, `X'` is reduced, and
every irreducible component of `X'` dominates an irreducible component of `X`.*

It suffices to show that in the three cases one has `𝓜_X^{f×} = 𝓜_X^×`. In case (i), this follows from `(20.1.12)`. In
case (iii), one may restrict to the case where `X = Spec(A)` and `X' = Spec(A')` are affine; if `s ∈ A` is regular, it
does not belong to any minimal prime ideal of `A` `(20.1.3.1)`, hence the hypothesis implies that its image in `A'`
does not belong to any minimal prime ideal of `A'`, and is consequently a regular element of `A'` `(20.1.3.1)`. In case
(ii) the meromorphic functions on `X'` are identified with the pseudo-functions on `X'` `(20.2.11)`, and the hypothesis,
joined to `(20.2.13, (iv))`, ensures that the inverse image

<!-- original page 266 -->

by `f` of every schematically dense open of `X` is a schematically dense open of `X'`; one therefore concludes by
`(20.3.12)`.

**Corollary (21.4.6).**

<!-- label: IV.21.4.6 -->

*Let `X` be a prescheme having one of the following properties:*

*(i) `X` is locally Noetherian.*

*(ii) `X` is reduced and the set of its irreducible components is locally finite.*

*Then, for every `x ∈ X`, one has a canonical isomorphism*

```text
  (21.4.6.1)             (𝒟iv_X)_x ⥲ Div(𝒪_{X,x}).
```

This follows from `(20.2.11)`, `(20.3.7)` and from the fact that `𝒪_X^×` identifies with the group of invertible
elements of the ring `𝒪_{X,x}`.

**(21.4.7).** Let `X`, `X'` be two preschemes, `f : X' → X` a morphism. If `D` is a positive divisor on `X` such that
the inverse image `f^*(D)` is defined `(21.4.2)`, then the closed sub-prescheme `Y(f^*(D))` of `X'` is none other than
the inverse image `f⁻¹(Y(D))`; this follows at once from the definitions `(21.4.2)` and `(21.2.12)`.

**Proposition (21.4.8).**

<!-- label: IV.21.4.8 -->

*Let `X`, `Y` be two preschemes; `f : X → Y` a faithfully flat morphism. Then, if a divisor `D` on `Y` is such that
`f^*(D) ≥ 0` (the existence of `f^*(D)` following from `(21.4.5)`), one has `D ≥ 0`. In particular, the map
`D ↦ f^*(D)` from `Div(Y)` to `Div(X)` is injective.*

The question being local on `Y`, one may restrict to the case where `D = div(w)`, with `w = uv⁻¹`, `u` and `v` being
two regular sections of `𝒪_Y` over `Y`. By hypothesis one has `u𝒪_X ⊂ v𝒪_X`, hence, for every `x ∈ X`, if one sets
`y = f(x)`, one has `u_y 𝒪_x ⊂ v_y 𝒪_x`; one concludes that `u_y 𝒪_y ⊂ v_y 𝒪_y` by virtue of the hypothesis that `𝒪_x`
is a faithfully flat `𝒪_y`-module and of Bourbaki, _Alg. comm._, chap. I, §3, n° 5, prop. 10, (ii); whence
`u 𝒪_Y ⊂ v 𝒪_Y` since `f` is surjective, and consequently `D ≥ 0`.

### 21.5. Direct images of divisors

**(21.5.1).** Let `X`, `X'` be two preschemes, `f : X' → X` a morphism. We shall, in this n°, give sufficient
conditions to be able to associate with every divisor `D'` on `X'` a divisor `D` on `X`, *direct image* of `D'` by `f`.
We shall restrict to the case where `f` is a *finite* morphism (for more general conditions, see the chapter of this
Treatise devoted to intersection theory).

**Lemma (21.5.2).**

<!-- label: IV.21.5.2 -->

*Let `A` be a ring, `E` a free `A`-module of finite rank. For an endomorphism `u` of `E` to be injective, it is
necessary and sufficient that `det(u)` be a regular element of `A`.*

This is proved in Bourbaki, _Alg._, chap. III, 3rd ed., §8, n° 2, prop. 3.

**(21.5.3).** Suppose now that the morphism `f : X' → X` is finite, and moreover that `f` verifies one of the two
following properties:

I) `f` is a *finite locally free* morphism, in other words `(18.2.7)` the quasi-coherent `𝒪_X`-Module of finite type
`f_*(𝒪_{X'})` is locally free.

II) `X` is a reduced locally Noetherian prescheme, the `𝒪(X)`-Module `f_*(𝒪_{X'}) ⊗_𝒪 𝒦(X)` is locally free, and for
every section `s' ∈ Γ(f⁻¹(U), 𝒪_{X'})` (`U` open

<!-- original page 267 -->

in `X`), `N_{X'/X}(s')` is a section of `𝒪_X` over `U` (cf. `(II, 6.5.1)`). (One recalls that condition (II) is verified
for every finite morphism `f` when `X` is a locally Noetherian normal prescheme (_loc. cit._).)

One then knows `(II, 6.5.5)` that for every invertible `𝒪_{X'}`-Module `ℒ'` one defines the norm
`ℒ = N_{X'/X}(ℒ')` (which we shall also write `N(ℒ')`), which is an invertible `𝒪_X`-Module. Moreover, for every open
`U` of `X` and every regular section `s' ∈ Γ(f⁻¹(U), 𝒪_{X'})`, the norm
`N_{X'/X}(s') = N_{f⁻¹(U)/U}(s')` (which we shall also write `N(s')`) is a regular element of `Γ(U, 𝒪_X)`; one is
indeed at once reduced to the case where `U = X` is affine, and then the conclusion follows from `(21.5.2)` under
hypothesis (I); on the other hand, under hypothesis (II), the fact that `𝒦(X)` is a flat `𝒪_X`-Module entails that the
section `s' ⊗ 1` of `Γ(U, f_*(𝒪_{X'}) ⊗_𝒪 𝒦(X))` is also regular `(0_I, 6.1.2)`, and the conclusion follows again from
`(21.5.2)` applied to the ring `Γ(U, 𝒦(X))`, taking into account the definition of the norm of a section
`(II, 6.5.3)`. This being so, let `u'` be a meromorphic section of `ℒ'` over `X'`; the morphism `f` being affine, every
point `x ∈ X` admits an open neighbourhood `U` such that `u' | f⁻¹(U)` is of the form `t' / s'`, where
`t' ∈ Γ(f⁻¹(U), ℒ')` and `s'` is a regular section in `Γ(f⁻¹(U), 𝒪_{X'})`; the element `N(t') / N(s')` (where `N(t')`
is the section of `ℒ` defined in `(II, 6.5.3)`) is then a meromorphic section of `ℒ` over `U` by virtue of what
precedes, and it follows from the multiplicative properties of the norm `(II, 6.5.3.1)` that this section depends only
on `u' | f⁻¹(U)` and not on its expression in the form `t' / s'`; for the same reason, when `U` varies, the meromorphic
sections of `ℒ` over `U` thus defined are the restrictions of one and the same meromorphic section of `ℒ` over `X`,
which one calls the **norm** of `u'` and denotes `N_{X'/X}(u')` (or simply `N(u')`). The map thus defined

```text
  (21.5.3.1)             N_{X'/X} : Γ(X', 𝓜_{X'}(ℒ')) → Γ(X, 𝓜_X(N_{X'/X}(ℒ')))
```

extends the norm defined in `(II, 6.5.3)`; if `u'` is a regular meromorphic section of `ℒ'` over `X'`, it follows at
once from what precedes that `N(u')` is a regular meromorphic section of `ℒ` over `X`, for (with the same notations)
`N(t')` is regular if `t'` is. Finally, if `ℒ_1'`, `ℒ_2'` are two invertible `𝒪_{X'}`-Modules, `s_1'` (resp. `s_2'`) a
meromorphic section of `ℒ_1'` (resp. `ℒ_2'`) over `X'`, one has, by virtue of what precedes and of `(II, 6.5.3.1)`,

```text
  (21.5.3.2)             N(s_1' ⊗ s_2') = N(s_1') ⊗ N(s_2').
```

**(21.5.4).** Suppose still that `f` verifies one of the hypotheses I), II) of `(21.5.3)`. If `(ℒ_1', s_1')`,
`(ℒ_2', s_2')` are two pairs each formed of an invertible `𝒪_{X'}`-Module and a regular meromorphic section of that
Module over `X'`, which are moreover equivalent in the sense of `(21.2.10)`, then the pairs
`(N(ℒ_1'), N(s_1'))` and `(N(ℒ_2'), N(s_2'))` are also equivalent, for an isomorphism of invertible
`𝒪_{X'}`-Modules has for norm an isomorphism of their norms `(II, 6.5.3)`, and one has seen above that `N_{X'/X}`
transforms sections of `Γ(X', 𝒪_{X'}^×)` into those of `Γ(X, 𝒪_X^×)`. One can therefore lay down the following
definition:

<!-- original page 268 -->

**Definition (21.5.5).**

<!-- label: IV.21.5.5 -->

*Given a finite morphism `f : X' → X` of preschemes, verifying one of the conditions I), II) of `(21.5.3)`, one calls
**direct image** (or **norm**) of a divisor `D'` on `X'` by `f`, and denotes `f_*(D')` (or `N_{X'/X}(D')`), the divisor
on `X` which corresponds canonically `(21.2.11)` to the class of the pair
`(N_{X'/X}(𝒪_{X'}(D')), N_{X'/X}(s_{D'}))`.*

It follows at once from this definition, taking into account `(21.2.9.4)` and `(21.5.3.2)`, that if `D_1'`, `D_2'`,
`D'` are divisors on `X'`, one has

```text
  (21.5.5.1)             f_*(D_1' + D_2') = f_*(D_1') + f_*(D_2')
```

and `D' ≥ 0` implies `f_*(D') ≥ 0`; in other words, `D' ↦ f_*(D')` is an increasing homomorphism from the ordered group
`Div(X')` into the ordered group `Div(X)`. Definition `(21.5.5)` moreover shows at once that for every open `U` of `X`,
one has `f_{U,*}(D' | f⁻¹(U)) = f_*(D') | U` (`f_U` being the restriction `f⁻¹(U) → U` of `f`), and the
homomorphisms `f_{U,*}`, for variable `U`, therefore define a homomorphism of sheaves of ordered groups

```text
  (21.5.5.2)             N_{X'/X} : f_*(𝒟iv_{X'}) → 𝒟iv_X.
```

Moreover, for every open `U` of `X`, every invertible `𝒪_{X'}`-Module `ℒ'` and every regular meromorphic section `s'`
of `ℒ'` over `f⁻¹(U)`, one has, according to the preceding definitions and `(21.1.4)`,

```text
  (21.5.5.3)             div_X(N_{X'/X}(s')) = f_*(div_{X'}(s')).
```

**Proposition (21.5.6).**

<!-- label: IV.21.5.6 -->

*Let `f : X' → X` be a finite locally free morphism and suppose that `f_*(𝒪_{X'})` is of constant rank `n`. Then, for
every divisor `D` on `X`, `f_*(f^*(D))` is defined and one has*

```text
  (21.5.6.1)             f_*(f^*(D)) = nD.
```

The first assertion follows from the fact that `f` is flat `(21.4.5)`, and the second is an immediate consequence of
the definitions and of `(II, 6.5.3.2)`.

**Proposition (21.5.7).**

<!-- label: IV.21.5.7 -->

*Let `f : X' → X` be a finite morphism verifying one of the hypotheses I), II) of `(21.5.3)`, `f' : X'' → X'` a finite
locally free morphism of constant rank `n`. Then `f'' = f ∘ f' : X'' → X` verifies the same hypothesis as `f`, and for
every divisor `D''` on `X''`, one has*

```text
  (21.5.7.1)             f''_*(D'') = f_*(f'_*(D'')).
```

In view of definition `(21.5.5)`, it suffices to prove the following result:

**Lemma (21.5.7.2).**

<!-- label: IV.21.5.7.2 -->

*Under the hypotheses of `(21.5.7)`, one has a functorial isomorphism*

```text
  (21.5.7.3)             N_{X''/X}(ℒ'') ⥲ N_{X'/X}(N_{X''/X'}(ℒ''))
```

*in the category of invertible `𝒪_X`-Modules.*

Indeed, taking into account the definition of the norm of a section of `ℒ''` `(II, 6.5.3)` and definition `(21.5.5)`,
one will at once obtain `(21.5.7.1)`. To prove `(21.5.7.2)`, it suffices, in view of the definitions of
`(II, 6.5.2 and 6.5.3)`, to prove that for every section `s` of `f''_*(𝒪_{X''}) = f_*(f'_*(𝒪_{X''}))` over an open `U`
of `X`, one has

```text
  (21.5.7.4)             N_{X''/X}(s) = N_{X'/X}(N_{X''/X'}(s)).
```

<!-- original page 269 -->

The question is obviously local on `X`, and one may therefore restrict to the case where `X = Spec(A)` is affine; one
then has `X' = Spec(A')` and `X'' = Spec(A'')`, and one may suppose that `A''` is a projective `A'`-module of rank `n`.
When `f` is locally free, one may suppose that `A'` is a free `A`-module of rank `m`, and then `A''` is a projective
`A`-module of rank `mn`, and by restricting `X` to a suitable open, one may suppose that `A''` is a free `A`-module of
rank `mn`; formula `(21.5.7.4)` then follows from the transitivity of the norm (Bourbaki, _Alg._, chap. VIII, §12, n° 2,
prop. 7). When `f` verifies hypothesis II), `A` is Noetherian reduced, and if `R` is its total ring of fractions,
`A' ⊗_A R` is a free `R`-module of rank `m`, hence `A'' ⊗_A R = A'' ⊗_{A'} (A' ⊗_A R)` is a projective `R`-module of
rank `mn`, and since `R` is then a semi-local ring, this `R`-module is free; the proposition follows again from the
transitivity of norms.

**Proposition (21.5.8).**

<!-- label: IV.21.5.8 -->

*Let `f : X' → X` be a finite morphism, `g : Y → X` a morphism; set `Y' = X' ×_X Y`, `f' = f_{(Y)} : Y' → Y`,
`g' = g_{(X')} : Y' → X'`. Suppose verified one of the following conditions:*

*(i) `f` is locally free and `g` is flat.*

*(ii) `f` is locally free, `X` and `Y` are locally Noetherian, `g(Ass(𝒪_Y)) ⊂ Ass(𝒪_X)` and
`g'(Ass(𝒪_{Y'})) ⊂ Ass(𝒪_{X'})`.*

*(iii) `f` verifies hypothesis II) of `(21.5.3)`, `Y` is locally Noetherian, `Y` and `Y'` are reduced, and every
irreducible component of `Y` (resp. `Y'`) dominates an irreducible component of `X` (resp. `X'`).*

*Then, for every divisor `D'` on `X'`, `g'^*(D')` is defined, `g^*(f_*(D'))` is defined, and one has*

```text
  (21.5.8.1)             g^*(f_*(D')) = f'_*(g'^*(D')).
```

Indeed, in all the cases, it follows from `(II, 6.5.8)` that one has a functorial isomorphism

```text
                         g^*(N_{X'/X}(ℒ')) ⥲ N_{Y'/Y}(g'^*(ℒ'))
```

in the category of invertible `𝒪_Y`-Modules; moreover `(II, 6.5.4)`, if `s'` is a section of `𝒪_{X'}` over `f⁻¹(U)`,
`s''` the corresponding section of `𝒪_{Y'}` over `g'⁻¹(f⁻¹(U))` (`U` open of `X`), `N_{Y'/Y}(s'')` is the section of
`𝒪_Y` over `g⁻¹(U)` which corresponds to the section `N_{X'/X}(s')` of `𝒪_X` over `U`. Formula `(21.5.8.1)` will
therefore follow from the definitions if one proves that `g'^*(D')` and `g^*(D)` are defined, whatever the divisors `D'`
on `X'` and `D` on `X`. As regards `D`, this follows from the hypotheses made and from `(21.4.5)`. As regards `D'`, in
case (i) `g'` is flat, hence in all the cases `g'^*(D')` is defined by virtue of `(21.4.5)`.

### 21.6. `1`-codimensional cycle associated with a divisor

**(21.6.1).** Let `X` be a locally Noetherian prescheme, and let `𝔍(X)` denote the set of irreducible closed parts of
`X` (which is in bijective correspondence with `X` by the map `x ↦ ‾{x}`). In the product group `ℤ^X`, consider the
subgroup `𝔷(X)` of elements `(n_x)_{x ∈ X}` such that the set of `‾{x} ∈ 𝔍(X)` such that `n_x ≠ 0` (or, what amounts to the
same,

<!-- original page 270 -->

the set of `x ∈ X` such that `n_x ≠ 0`) is locally finite. It is clear that `𝔷(X)` is a subgroup of `ℤ^X` which contains
the direct sum group `ℤ^{(X)}` (free group having `𝔍(X)` for basis), and is equal to it when `X` is Noetherian. The
elements of `𝔷(X)` are called **cycles on `X`** and those of `𝔍(X)` **prime cycles** (they do not in general form a
basis of `𝔷(X)` when `X` is not Noetherian). One always considers `𝔷(X)` as *ordered* by the order induced on this
subgroup by the product order of `ℤ^X`, and one denotes `𝔷^+(X)` the set of cycles `≥ 0`.

For every cycle `Z ∈ 𝔷(X)`, equal to `(n_x)_{x ∈ X}`, one writes by abuse of language,

```text
                         Z = ∑_{x ∈ X} n_x · ‾{x};
```

one calls **multiplicity** of `Z` at the point `x` and one denotes by `mult_x(Z)` the integer `n_x` (positive or
negative). To say that `Z ≥ 0` means that `mult_x(Z) ≥ 0` for every `x ∈ X`. One calls **support** of `Z` and denotes
by `Supp(Z)` the union of the `‾{x}` such that `mult_x(Z) ≠ 0`; by definition of `𝔷(X)`, this is a closed part of `X`, as
union of a locally finite family of closed parts. One calls **dimension** (resp. **codimension**) of `Z` and denotes by
`dim(Z)` (resp. `codim(Z)`) the dimension (resp. codimension in `X`) of `Supp(Z)`.

**(21.6.2).** One says that a closed part `Y` of `X` is *purely of codimension `p` (in `X`)* if each of its irreducible
components is of codimension `p` in `X`. One says that a cycle is *purely of codimension `p`*, or (by abuse of
language) is a **`p`-codimensional cycle**, if its support is purely of codimension `p`. One denotes by `X^{(p)}` the
set of `x ∈ X` such that `codim(‾{x}, X) = p`, or, what amounts to the same `(5.1.2.1)`, `dim(𝒪_{X,x}) = p`: the cycles
purely of codimension `p` form a subgroup `𝔷^p(X)` of `𝔷(X)`, isomorphic to the subgroup of `ℤ^{X^{(p)}}` formed of the
`(n_x)_{x ∈ X^{(p)}}` such that the set of `‾{x}` (or the set of `x`) for which `n_x ≠ 0` is locally finite; this
subgroup contains the free group `ℤ^{(X^{(p)})}` and is identical to it when `X` is Noetherian. One denotes by
`𝔷^{p+}(X)` the set of elements `≥ 0` of `𝔷^p(X)`. It is clear that the ordered group `𝔷(X)` contains the direct sum of
the ordered subgroups `𝔷^p(X)`, and is identical to this direct sum when `X` is Noetherian; in this last case, one
considers `𝔷(X)` as *graded* by the `𝔷^p(X)` for `p ∈ ℕ`.

**(21.6.3).** Let `Z = ∑_{x ∈ X} n_x · ‾{x}` be a cycle on `X`, `U` an open of `X`; one calls **restriction of `Z` to
`U`** and one denotes by `Z | U` the cycle `∑_{x ∈ U} n_x · (U ∩ ‾{x})` on `U`; one has
`Supp(Z | U) = Supp(Z) ∩ U`. It is clear that `Z ↦ Z | U` is a homomorphism of ordered groups from `𝔷(X)` into `𝔷(U)`
(resp. from `𝔷^p(X)` into `𝔷^p(U)`), and that if `V` is an open contained in `U`, one has `Z | V = (Z | U) | V`; the
map `U ↦ 𝔷(U)` (resp. `U ↦ 𝔷^p(U)`) is therefore a presheaf on `X` of ordered commutative groups. In fact this
presheaf is a *sheaf*, direct sum of the sheaves `(j_x)_*(ℤ_{‾{x}})`, where `x` runs through `X` (resp. `X^{(p)}`) and for
each `x ∈ X`, `j_x` is the canonical injection `‾{x} → X` and `ℤ_{‾{x}}` is the simple sheaf associated with the constant
sheaf `ℤ` on the space `‾{x}`: this follows at once from the description of the sections of a direct sum of sheaves of
commutative groups (G, II, 2.7). One denotes this sheaf `𝔷_X` (resp. `𝔷_X^p`). One denotes by `𝔷_X^+` (resp.
`𝔷_X^{p+}`) the subsheaf

<!-- original page 271 -->

of monoids `U ↦ 𝔷^+(U)` (resp. `U ↦ 𝔷^{p+}(U)`) of `𝔷_X` (resp. `𝔷_X^p`). The sheaf `𝔷_X` is evidently the direct sum
of the sheaves `𝔷_X^p`.

Note finally that the sheaves `𝔷_X^p` (hence also `𝔷_X`) are *flasque*. Suppose indeed given a section `Z` of `𝔷_X^p`
over an open `U`, so that the set `S` of `x ∈ U` such that `mult_x(Z) ≠ 0` is locally finite in `U`; this set is also
locally finite in `X`, for, for every `ξ ∈ X` and every Noetherian open neighbourhood `V` of `ξ`, `U ∩ V` is
Noetherian, hence contains only a finite number of points of `S`. One therefore defines a section `Z'` of `𝔷_X^p` over
`X` by setting `Z' = ∑_{x ∈ U} mult_x(Z) · ‾{x}`; and since the closure of `x` in `U` is `‾{x} ∩ U`, one has indeed
`Z' | U = Z`, whence our assertion.

**(21.6.4).** We propose to define a canonical homomorphism

```text
  (21.6.4.1)             c : 𝒟iv_X → 𝔷_X^1
```

of sheaves of commutative groups. It evidently suffices to define a homomorphism from `𝓜_X^×` into `𝔷_X^1`, which
vanishes on `𝒪_X^×` `(21.1.2)`; now, by definition, `𝓜_X^×` is the symmetrization of the sheaf of monoids
`𝒮(𝒪_X) = 𝒪_X ∩ 𝓜_X^×`, and a homomorphism `𝓜_X^× → 𝔷_X^1` is uniquely determined by the data of its restriction
`𝒮(𝒪_X) → 𝔷_X^1`, which is a homomorphism of sheaf of monoids subject to the sole condition of being zero on
`𝒪_X^×`; it amounts to the same to say that to define `c`, it suffices to define a homomorphism of sheaf of monoids

```text
  (21.6.4.2)             c : 𝒟iv_X^+ → 𝔷_X^{1+}.
```

**(21.6.5).** Now, one has seen that to every positive divisor `D` on `X` corresponds the closed sub-prescheme `Y(D)`
of `X`, defined by the Ideal `𝒪_X(D) ⊂ 𝒪_X`, and which is regularly immersed and of codimension `1`. At each of the
maximal points `x` of `Y(D)`, one therefore has `((19.1.4)` and `(5.1.2))`
`codim(‾{x}, X) = dim(𝒪_{X,x}) = 1`, in other words `x ∈ X^{(1)}`; moreover the set of these maximal points is locally
finite in `X` `(3.1.6)`, and `𝒪_{Y(D),x}` is an Artinian ring. At every point `x ∈ X^{(1)}` which is not a maximal
point of `Y(D)`, one necessarily has `x ∉ Y(D)`, hence `𝒪_{Y(D),x} = 0`. Set

```text
  (21.6.5.1)             cyc(D) = ∑_{x ∈ X^{(1)}} long(𝒪_{Y(D),x}) · ‾{x}
```

which is therefore an element of `𝔷^1(X)`.

**Proposition (21.6.6).**

<!-- label: IV.21.6.6 -->

*The map `D ↦ cyc(D)` is a homomorphism from the monoid `Div^+(X)` into `𝔷^1(X)`.*

Everything reduces to seeing that for two positive divisors `D`, `D'`, one has

```text
                         cyc(D + D') = cyc(D) + cyc(D').
```

Now, one has `(21.2.5)` `𝒪_X(D + D') = 𝒪_X(D) 𝒪_X(D')`; everything reduces to seeing that if `x ∈ X^{(1)}`, if one sets
`A = 𝒪_{X,x}`, and if `t` and `t'` are two regular elements of `A`, one has
`long(A / tt'A) = long(A / tA) + long(A / t'A)`; but since `t` is regular, `tA / tt'A` is isomorphic to `A / t'A`,
whence the proposition at once.

<!-- original page 272 -->

It follows at once from the definitions that for every open `U ⊂ X`, one has

```text
                         Y(D | U) = Y(D) ∩ U,
```

hence `cyc(D | U) = cyc(D) | U`, and the homomorphisms `cyc : Div^+(U) → 𝔷^1(U)` therefore define a homomorphism of
sheaves of monoids `(21.6.4.2)`, whence the sought homomorphism `(21.6.4.1)` of sheaves of groups.

One has `Supp(cyc(D)) ⊂ Supp(D)` for every divisor `D` and

```text
  (21.6.6.2)             Supp(cyc(D)) = Supp(D)     when D ≥ 0;
```

one has indeed already seen the second relation `(21.2.12)`; when `D` is arbitrary, the relation `D_x = 0` entails the
existence of an open neighbourhood `U` of `x` such that `D | U = 0`, whence `cyc(D) | U = 0`, which proves our
assertion.

**(21.6.7).** The homomorphism `(21.6.4.1)` gives, by passage to the groups of sections over `X`, an increasing
homomorphism of ordered groups `Div(X) → 𝔷^1(X)`, which we shall again denote `D ↦ cyc(D)`; the number
`mult_x(cyc(D))` for `x ∈ X^{(1)}` is also denoted `mult_x(D)` or `mult_{‾{x}}(D)` and is called **multiplicity of the
divisor `D` at the point `x`**, or **multiplicity of the prime cycle `‾{x}` in `D`**; this is a positive or negative
integer, equal as one has seen to `long(𝒪_{Y(D),x})` when `D` is a positive divisor; one therefore has by definition

```text
  (21.6.7.1)             cyc(D) = ∑_{x ∈ X^{(1)}} mult_x(D) · ‾{x},
```

and by virtue of the fact that `D ↦ cyc(D)` is a homomorphism, one has

```text
  (21.6.7.2)             mult_x(−D) = −mult_x(D),    mult_x(D + D') = mult_x(D) + mult_x(D')
```

for any two divisors `D`, `D'`.

For every regular meromorphic function `f` on `X`, one sets in particular, for `x ∈ X^{(1)}`,

```text
  (21.6.7.3)             ω_x(f) = mult_x(div(f))
```

and one says that `ω_x(f)` (positive or negative integer) is the **order of `f` at the point `x ∈ X^{(1)}`**. If
`f ∈ 𝒪_{X,x}` (a regular element of this local ring by hypothesis), one therefore has

```text
  (21.6.7.4)             ω_x(f) = long(𝒪_{X,x} / f 𝒪_{X,x});
```

for two regular meromorphic functions `f`, `f'` on `X`, one has

```text
  (21.6.7.5)             ω_x(ff') = ω_x(f) + ω_x(f'),    ω_x(f⁻¹) = −ω_x(f)
```

for every `x ∈ X^{(1)}`. The `1`-codimensional cycles

```text
                         Z^+(f) = ∑_{x ∈ X^{(1)}, ω_x(f) > 0} ω_x(f) · ‾{x},
                         Z^−(f) = ∑_{x ∈ X^{(1)}, ω_x(f) < 0} (−ω_x(f)) · ‾{x}
```

are called respectively the **cycle of zeros** and the **cycle of poles** (or **polar cycle**) of `f`, and one has
obviously `cyc(div(f)) = Z^+(f) − Z^−(f)`. The `1`-codimensional cycles of the form `cyc(div(f))` are called
**principal** (or *linearly equivalent to `0`*) and form a subgroup `𝔷_{princ}^1(X)` of `𝔷^1(X)`. The sections over `X`
of the image `c(𝒟iv_X) ⊂ 𝔷_X^1` are

<!-- original page 273 -->

called **locally principal cycles**; such a cycle `Z` is therefore characterized by the fact that, for every `y ∈ X`,
there is an open neighbourhood `U` of `y` in `X` and a regular meromorphic function `f` on `U` such that
`Z | U = ∑_{x ∈ U ∩ X^{(1)}} ω_x(f) · (‾{x} ∩ U)`. If `Z = ∑_{x ∈ X^{(1)}} n_x · ‾{x}`, it amounts to the same to say
that, for every `y ∈ X`, if one sets `T_y = Spec(𝒪_{X,y})` and `Z_y = ∑_{x ∈ X^{(1)} ∩ T_y} n_x · (‾{x} ∩ T_y)`, `Z_y`
is principal; in other words there exists a regular meromorphic function `g` on `T_y` such that `Z_y = cyc(div(g))`.
This follows at once indeed from the preceding definition and from `(20.3.7)`, which establishes a bijective
correspondence between the regular meromorphic functions on `T_y` and the germs of regular meromorphic functions on the
open neighbourhoods of `y` in `X` when `X` is locally Noetherian. One again expresses the fact that `Z_y` is principal
by saying that *`Z` is principal at the point `y`*. The set of points where `Z` is principal is evidently open, by
virtue of what precedes.

One deduces from the canonical homomorphism `cyc : Div(X) → 𝔷^1(X)` a canonical homomorphism
`Div(X) / Div.princ(X) → 𝔷^1(X) / 𝔷_{princ}^1(X)`, by virtue of the definition of `𝔷_{princ}^1(X)`. One says that the
group `𝔷^1(X) / 𝔷_{princ}^1(X)` is the **group of classes of `1`-codimensional cycles on `X`** and one denotes it
`Cl(X)`. Two elements of `𝔷^1(X)` having the same image in `Cl(X)` are called **linearly equivalent**.

**(21.6.8).** Consider in particular the case where `X = Spec(A)`, where `A` is an integrally closed Noetherian integral
domain. Then `X^{(1)}` is the set of prime ideals of height `1` of `A`, and `𝔷^1(X)` is therefore identified with the
group of divisors (in the sense of N. Bourbaki) of the Krull ring `A` (Bourbaki, _Alg. comm._, chap. VII, §1, n° 3,
cor. of th. 2 and n° 6, th. 3).

Since on the other hand, the regular meromorphic functions on `X` are then identified with the elements `≠ 0` of the
fraction field `K` of `A`, the map `f ↦ cyc(div(f))` from `M(X)^×` into `𝔷^1(X)` is identified with the map denoted
`f ↦ div(f)` in Bourbaki (_loc. cit._, §1, n° 1); `𝔷_{princ}^1(X)` is therefore identified with the group of principal
divisors of `A` in the sense of Bourbaki, and `Cl(X)` with the group of divisor classes of `A` in the sense of Bourbaki
(_loc. cit._, §1, n° 2 and n° 10).

**Theorem (21.6.9).**

<!-- label: IV.21.6.9 -->

*Let `X` be a locally Noetherian normal prescheme.*

*(i) The canonical homomorphism `cyc : Div(X) → 𝔷^1(X)` is injective and its image is formed of the locally principal
cycles.*

*(ii) The following conditions are equivalent:*

*a) The homomorphism `cyc : Div(X) → 𝔷^1(X)` is bijective.*

*b) Every `1`-codimensional cycle is locally principal.*

*c) For every `x ∈ X`, the local ring `𝒪_{X,x}` is factorial.*

*(One then says that `X` is a **locally factorial prescheme**.)*

(i) It suffices to prove that

```text
  (21.6.9.1)             cyc⁻¹(𝔷^{1+}(X)) = Div^+(X),
```

since one has `Div^+(X) ∩ (−Div^+(X)) = 0` and `𝔷^{1+}(X) ∩ (−𝔷^{1+}(X)) = 0`. One is therefore reduced to proving that
if `D` is a divisor on `X` such that `mult_x(D) ≥ 0` for every `x ∈ X^{(1)}`, one has `D ≥ 0`. Now, for every
`x ∉ X^{(1)}`, the local ring `𝒪_{X,x}` is integral and integrally closed, and

<!-- original page 274 -->

of dimension `0` or `≥ 2`, hence one has `prof(𝒪_{X,x}) = 0` or `prof(𝒪_{X,x}) ≥ 2` `(0, 16.5.1)`. On the other hand,
at the points `x ∈ X^{(1)}`, the ring `𝒪_{X,x}` is a discrete valuation ring `(II, 7.1.6)`, hence
`prof(𝒪_{X,x}) = 1` `(0, 16.5.1)`; the only points of `X` such that `prof(𝒪_{X,x}) ≤ 1` are therefore the points of
`X^{(1)}`, and the conclusion follows from `(21.1.8)`.

(ii) The equivalence of a) and b) is clear by virtue of (i). According to the characterization of locally principal
cycles given in `(21.6.7)`, and the relation between `1`-codimensional cycles on `Spec(A)` and divisors (in the sense of
Bourbaki) of the ring `A` when `A` is an integrally closed Noetherian ring `(21.6.8)`, condition b) is equivalent to
saying that for every `x ∈ X`, every divisor of the ring `𝒪_{X,x}` is principal, in other words that the ring
`𝒪_{X,x}` is factorial (Bourbaki, _Alg. comm._, chap. VII, §3, n° 1), whence the equivalence of b) and c).

**(21.6.9.2).** When `A` is a factorial Noetherian ring, it is clear that `X = Spec(A)` is locally factorial (Bourbaki,
_Alg. comm._, chap. VII, §3, n° 4, prop. 3). If, in this case, one writes an element `f ≠ 0` of the fraction field `K`
of `A` in the form `r/s`, where `r` and `s` are two coprime elements of `A`, whose divisors are well determined
(_loc. cit._, §3, n° 3), these divisors are identified respectively with the *cycle of zeros* and the *cycle of poles*
of `f` `(21.6.7)`.

**Corollary (21.6.10).**

<!-- label: IV.21.6.10 -->

*Let `X` be a locally Noetherian normal prescheme.*

*(i) There exists a canonical injective homomorphism*

```text
  (21.6.10.1)            Pic(X) → Cl(X).
```

*(ii) If `X` is locally factorial, the homomorphism `(21.6.10.1)` is bijective, and conversely.*

One has seen `(21.6.7)` that the image of `Div.princ(X)` by the homomorphism `cyc : Div(X) → 𝔷^1(X)` is
`𝔷_{princ}^1(X)`; one therefore deduces from `(21.6.9)` that the homomorphism
`Div(X) / Div.princ(X) → 𝔷^1(X) / 𝔷_{princ}^1(X) = Cl(X)` deduced from `cyc` is injective, and that it is bijective if
and only if `X` is locally factorial. The conclusion therefore follows from the fact that, when `X` is locally
Noetherian and reduced, the canonical homomorphism `Div(X) / Div.princ(X) → Pic(X)` `(21.3.3.1)` is bijective
`(21.3.4, (ii))`.

**Corollary (21.6.11).**

<!-- label: IV.21.6.11 -->

*Let `X` be a locally Noetherian and locally factorial prescheme. Then the sheaf `𝒟iv_X` is flasque, and for every open
`U` of `X`, the canonical homomorphism `Pic(X) → Pic(U)` is surjective.*

Taking into account `(21.6.9, (ii))`, the first assertion is equivalent to saying that the sheaf `𝔷_X^1` is flasque,
which has been seen above `(21.6.3)`. For every open `U` of `X`, the canonical homomorphism `𝔷^1(X) → 𝔷^1(U)` is
therefore surjective; since by virtue of `(21.6.10)`, the homomorphism `Pic(X) → Pic(U)` is canonically identified with
`𝔷^1(X) / 𝔷_{princ}^1(X) → 𝔷^1(U) / 𝔷_{princ}^1(U)`, it is also surjective.

**Proposition (21.6.12).**

<!-- label: IV.21.6.12 -->

*Let `X` be a Noetherian reduced prescheme. Let `(U_λ)_{λ ∈ L}` be a decreasing filtered family of opens of `X`
verifying the following conditions:*

*1° If `Y_λ = X − U_λ`, one has `codim(Y_λ, X) ≥ 2` for every `λ ∈ L`.*

*2° For every `x ∈ ⋂_{λ ∈ L} U_λ`, the ring `𝒪_{X,x}` is factorial.*

<!-- original page 275 -->

*Then there exist canonical isomorphisms*

```text
  (21.6.12.1)            lim Div(U_λ) ⥲ 𝔷^1(X),    lim Pic(U_λ) ⥲ Cl(X)
```

*such that, for every open `V` of `X`, the diagrams*

```text
                         lim Div(U_λ) ─⥲─ 𝔷^1(X)
                              │             │
  (21.6.12.2)
                              ↓             ↓
                         lim Div(U_λ ∩ V) ─⥲ 𝔷^1(V)

                         lim Pic(U_λ) ─⥲─ Cl(X)
                              │             │
                              ↓             ↓
                         lim Pic(U_λ ∩ V) ─⥲ Cl(V)
```

*are commutative.*

Hypothesis 1° on `U_λ` implies that for every `λ ∈ L`, one has `X^{(1)} ⊂ U_λ` `(5.1.3.1)`; hence the restriction
homomorphism `𝔷^1(X) → 𝔷^1(U_λ)` is bijective and consequently one has a canonical isomorphism
`lim 𝔷^1(U_λ) ⥲ 𝔷^1(X)`. The canonical homomorphisms `cyc : Div(U_λ) → 𝔷^1(U_λ)` define therefore, by passage to the
inductive limit, the first of the canonical homomorphisms `(21.6.12.1)`, and the second one is deduced from it by
passage to the quotients. Moreover, it follows from condition 1° that the `U_λ` are dense in `X`, hence schematically
dense since `X` is reduced `(11.10.4)`, and consequently every meromorphic function on `X` is entirely determined by
its restriction to each `U_λ`; one deduces at once from this that in the isomorphism `𝔷^1(X) ⥲ 𝔷^1(U_λ)`, the image of
`𝔷_{princ}^1(X)` is `𝔷_{princ}^1(U_λ)`, hence one also has a canonical isomorphism `lim Cl(U_λ) ⥲ Cl(X)`. The second of
the canonical homomorphisms `(21.6.12.1)` will therefore be an isomorphism if the first is, and it remains to prove
this latter point, the commutativity of the diagrams `(21.6.12.2)` being trivial.

Let us show first that the homomorphism `lim Div(U_λ) → 𝔷^1(X)` is injective. Set `T = ⋂_{λ} U_λ`, and note that the
`U_λ` form a fundamental system of neighbourhoods of `T`. Indeed, for every open `V ⊃ T`, `X − V` is a closed subspace
of `X`, hence a Noetherian space every closed irreducible part of which admits a generic point; since the sets
`(X − V) ∩ (X − U_λ)` are closed in `X − V`, form an increasing filtered family and have for union `X − V`, our
assertion follows from `(0_III, 9.2.4)`. This being so, it is a matter of seeing that if `D ∈ Div(U_λ)` is such that
`cyc(D) = 0` in `𝔷^1(U_λ)`, then there exists `μ ≥ λ` such that `D | U_μ = 0`. By virtue of what precedes, it will
suffice to see that for every `x ∈ T`, one has `D_x = 0`; indeed, there will then be a neighbourhood `W(x)` of `x` in
`X` such that `D | W(x) = 0`, and the union of the `W(x)` for `x ∈ T` contains some `U_μ`. Taking into account
`(21.4.6)`, one is therefore reduced to the case where `X = Spec(𝒪_{X,x})`; but by hypothesis `𝒪_{X,x}` is factorial,
hence integral and integrally closed, and `Spec(𝒪_{X,x})` is then normal; hence the conclusion follows from
`(21.6.9, (i))`.

To prove that the homomorphism `lim Div(U_λ) → 𝔷^1(X)` is bijective, it suffices to prove similarly that for every
`Z ∈ 𝔷^1(X)` and every `x ∈ T`, there is a neighbourhood `W(x)`

<!-- original page 276 -->

of `x` in `X` and a divisor `D_x` on `W(x)` such that `cyc(D_x) = Z | W(x)`. Indeed, one will then be able to cover
the quasi-compact set `T` by a finite number of `W(x_i)`, and by virtue of the first part of the demonstration, since
the pairs `(i, j)` are finite in number, there will exist an index `λ` such that in each of the
`W(x_i) ∩ W(x_j) ∩ U_λ`, the restrictions of `D_{x_i}` and `D_{x_j}` coincide; since one may suppose moreover that
`U_λ` is contained in the union of the `W(x_i)`, one sees that the restrictions `D_{x_i} | (W(x_i) ∩ U_λ)` are the
restrictions of one and the same divisor `D ∈ Div(U_λ)` which will be such that `cyc(D) = Z | U_λ`. One is therefore
reduced again to the case where `X = Spec(𝒪_{X,x})` with `x ∈ T`; but since `𝒪_{X,x}` is factorial, so are its
localizations (Bourbaki, _Alg. comm._, chap. VII, §3, n° 4, prop. 3), and it suffices to apply `(21.6.9, (ii))`.

**Corollary (21.6.13).**

<!-- label: IV.21.6.13 -->

*Let `A` be an integrally closed Noetherian integral local ring of dimension `≥ 2`. Set `X = Spec(A)`, and let `a` be
the closed point of `X`, `U = X − {a}`. For `A` to be factorial, it is necessary and sufficient that `U` be locally
factorial and that `Pic(U) = 0`.*

Indeed, to say that `A` is factorial is equivalent to saying that `Cl(X) = 0` (Bourbaki, _Alg. comm._, chap. VII, §1,
n° 4, cor. of th. 2 and §3, n° 2, th. 1); it therefore suffices to use the existence of the second isomorphism
`(21.6.12.1)`, taking the family `(U_λ)` restricted to the single open `U`.

**Corollary (21.6.14).**

<!-- label: IV.21.6.14 -->

*Let `A` be a Noetherian local ring of dimension `≥ 2`, `X = Spec(A)`, `a` the closed point of `X`, `U = X − {a}`. The
following conditions are equivalent:*

*a) `A` is factorial.*

*b) `Pic(U) = 0` and `prof(A) ≥ 2` (conditions which we shall later (21.13) express by saying that the ring `A` is
**parafactorial**), and `U` is locally factorial.*

It is clear that if `A` is factorial, it is normal, hence `prof(A) ≥ 2` since `dim(A) ≥ 2` `(0, 16.5.1)`, and
`(21.6.13)` shows that a) implies b). Conversely, if b) is verified, it suffices to see that `A` is integrally closed
to conclude by `(21.6.13)` that b) entails a). By virtue of Serre's criterion `(5.8.6)`, it suffices to verify for `X`
the conditions `(R_1)` and `(S_2)`. Now, `U` being locally factorial verifies these conditions, and the hypothesis
`prof(A) ≥ 2` entails that `X` verifies them also.

### 21.7. Interpretation of positive `1`-codimensional cycles in terms of subpreschemes

**(21.7.1).** Let `X` be a locally Noetherian prescheme, `C = ∑_{x ∈ X^{(1)}} n_x · ‾{x}` a positive
`1`-codimensional cycle (so that one has `n_x ≥ 0` for every `x ∈ X^{(1)}`, and `n_x = 0` except on a locally finite
set of points). Denote by `Y(C)` the closed sub-prescheme of `X`, **closed image** `(I, 9.5.3` and `9.5.1)` of the sum
prescheme `Y'(C) = ∐_{x ∈ X^{(1)}} Spec(𝒪_{X,x} / 𝔪_x^{n_x})` under the canonical morphism, and by `𝒥_X(C)` (or
`𝒥(C)`) the Ideal of `𝒪_X` defining `Y(C)`.

**Proposition (21.7.2).**

<!-- label: IV.21.7.2 -->

*Let `X` be a locally Noetherian prescheme verifying condition `(R_1)` `(5.8.2)`. For a closed sub-prescheme `Y` of
`X` to be of the form `Y(C)`, where `C` is a positive `1`-codimensional cycle, it is necessary and sufficient that it
verify the two following conditions:*

*(i) `Y` is purely of codimension `1`.*

<!-- original page 277 -->

*(ii) `Y` verifies condition `(S_1)`, in other words `(5.7.5)` has no immersed associated prime cycle.*

*One then has*

```text
  (21.7.2.1)             mult_x(C) = long(𝒪_{Y,x}).
```

*The map `C ↦ Y(C)` is a bijection of `𝔷^{1+}(X)` onto the set of closed sub-preschemes of `X` verifying conditions
(i) and (ii).*

The conditions are necessary (without assuming that `X` verifies `(R_1)`). Indeed, the question being local on `X`, one
may suppose that `X = Spec(A)`, where `A` is a Noetherian ring; one then has `Y(C) = Spec(A / 𝔍)`, where `𝔍` is by
definition `(I, 9.5.1)` the kernel of the canonical homomorphism `A → ⊕ A_{𝔭_i} / 𝔭_i^{n_i} A_{𝔭_i}`, where the
`𝔭_i` are the prime ideals corresponding to the points `x_i ∈ X^{(1)}` for which `n_{x_i} ≠ 0`, and where one has set
`n_i = n_{x_i}`. The inverse image `𝔮_i` of `𝔭_i^{n_i} A_{𝔭_i}` in `A` is a `𝔭_i`-primary ideal, and one has
`𝔍 = ⋂ 𝔮_i`. Moreover, since the `x ∈ X^{(1)}` are such that `‾{x}` is of codimension `1`, no point of `X^{(1)}` can
be adherent to another point of `X^{(1)}`. Hence the `𝔭_i` are the minimal prime ideals of `A / 𝔍` and the set of
`𝔭_i` is equal to `Ass(A / 𝔍)`, which proves conditions (i) and (ii).

The conditions are sufficient. Denoting by `𝒥` the Ideal of `𝒪_X` defining `Y`, hypothesis (ii) implies that
`Ass(𝒪_X / 𝒥)` is identical to the set `F` of maximal points of `Y`, and hypothesis (i) implies that `F` is contained
in `X^{(1)}`; hence `(3.2.6)` `𝒪_X / 𝒥` is identified with a sub-`𝒪_X`-Module of `⊕_{x ∈ F} ℰ(x)`, where for each
`x ∈ F`, `ℰ(x)` is an irredundant `𝒪_X`-Module such that `Ass(ℰ(x)) = {x}`. Now, since `X` verifies `(R_1)`, for each
`x ∈ F`, `𝒪_{X,x}` is a discrete valuation ring, and consequently the primary ideals `≠ 0` of this ring are the powers
`𝔪_x^k` of the maximal ideal; supposing still that `X = Spec(A)`, one concludes that `𝒥 = 𝔍`, where `𝔍 = ⋂ 𝔮_i`, the
`𝔮_i` being the inverse images in `A` of ideals `𝔭_i^{n_i} A_{𝔭_i}`, where the `𝔭_i` correspond to the points of `F`.
One sees therefore well that `Y` is of the form `Y(C)`.

**Corollary (21.7.3).**

<!-- label: IV.21.7.3 -->

*Let `X` be a locally Noetherian prescheme. For every positive divisor `D` on `X` such that `X` verifies `(R_1)` at the
maximal points of the closed sub-prescheme `Y(D)` `(21.2.12)`, `Y(D)` majorizes the closed sub-prescheme
`Y(cyc(D))` `(21.7.1)`, and has the same underlying space; for these two sub-preschemes to be equal, it is necessary
and sufficient that `Y(D)` verify condition `(S_1)`, or also that, for every `x ∈ Y(D)` distinct from a maximal point
of `Y(D)`, one have `prof(𝒪_{X,x}) ≥ 2` (condition always verified when `X` is normal).*

Indeed, the question being local, one may always suppose that `𝒪_X(D) = 𝒪_X · t`, `t` being a regular section of
`𝒪_X` over `X`; at every maximal point `x` of `Y(D)`, necessarily belonging to `X^{(1)}`, `𝒪_{X,x}` is by hypothesis a
discrete valuation ring, hence `𝒪_{X,x} t = 𝔪_x^{n_x}` for `n_x = mult_x(D)`. One may suppose `X = Spec(A)`, and then,
if `𝒥_X(cyc(D)) = 𝔍`, `𝒪_X(D) = 𝔍'`, it follows from what precedes and from `(21.7.1)` that `𝔍` and `𝔍'` have the same
non-immersed primary ideals; hence `𝔍' ⊂ 𝔍`, since `𝔍` is the intersection

<!-- original page 278 -->

of these primary ideals `(21.7.2)`. This proves that `Y(D)` majorizes `Y(cyc(D))` and that these two sub-preschemes
are equal if and only if `Y(D)` has no immersed associated prime cycle (in other words verifies `(S_1)`). Since for
every `x ∈ Y(D)`, there is by hypothesis an open neighbourhood `U` of `x` in `X` and a regular element
`t ∈ Γ(U, 𝒪_X)` such that `𝒪_{Y(D)} | (U ∩ Y(D))` is the restriction to `Y(D) ∩ U` of `𝒪_U / t 𝒪_U`, to say that
`Y(D)` verifies `(S_1)` also means that at every non-maximal point `x ∈ Y(D)`, one has
`prof(𝒪_{X,x} / t 𝒪_{X,x}) ≥ 1`, that is to say `(0, 16.4.6)` `prof(𝒪_{X,x}) ≥ 2`. The assertion concerning the case
where `X` is normal is then immediate since `X` verifies `(S_2)` and at the non-maximal points `x` of `Y(D)` one has
`dim(𝒪_{X,x}) ≥ 2` `(0, 16.3.4)`.

**(21.7.3.1).** One therefore sees that when `X` is normal, `Div^+(X)` is canonically identified with the set of
closed sub-preschemes `Y` of `X` verifying conditions (i) and (ii) of `(21.7.2)` and regularly immersed in `X`.

**Proposition (21.7.4).**

<!-- label: IV.21.7.4 -->

*Let `X` be a locally Noetherian prescheme, reduced at each of its isolated points. The following conditions are
equivalent:*

*a) The canonical homomorphism `c : 𝒟iv_X → 𝔷_X^1` `(21.6.4)` is an isomorphism of sheaves of ordered groups.*

*a') Every prime `1`-codimensional cycle on `X` is the image by `cyc` of a positive divisor, and the canonical
homomorphism `c : 𝒟iv_X → 𝔷_X^1` is injective.*

*a") For every integral closed sub-prescheme `Y` of `X`, of codimension `1`, the canonical immersion `Y → X` is
regular.*

*b) `X` is normal and the homomorphism `cyc : Div(X) → 𝔷^1(X)` is bijective.*

*c) `X` is locally factorial.*

The equivalence of b) and c) has been proved in `(21.6.9)`, as well as the fact that c) entails a). Moreover b) entails
a") by virtue of `(21.7.3.1)`, and a) trivially implies a'). It remains to see that a') or a") entails c).

Suppose then that condition a') is verified, and let us first show that `X` is normal. Note first that if `X` verifies
a'), so does every local scheme `Spec(𝒪_{X,x})`. Consider then `x ∈ X^{(1)}`, so that `A = 𝒪_{X,x}` is a Noetherian
local ring of dimension `1`. Applying condition a') to `Spec(A)` and to the prime `1`-codimensional cycle formed of
the closed point of `Spec(A)`, one sees that in `A` the maximal ideal is generated by a single regular element of `A`;
hence `(0, 17.1.1)` `A` is a regular ring. Since the localized rings `A_𝔭` are also regular `(0, 17.3.2)`, one sees
that `X` is regular at all its non-isolated maximal points; since it is also reduced (hence regular) at its isolated
points by hypothesis, one concludes that `X` verifies condition `(R_1)`. Let us show moreover that `X` also verifies
`(S_1)`, in other words that for every `x ∈ X` such that `dim(𝒪_{X,x}) ≥ 1`, one has `𝔪_x \notin Ass(𝒪_{X,x})`
`(0, 16.4.6)`. Indeed, hypothesis a') applied to `X_1 = Spec(𝒪_{X,x})` shows that there exists on this prescheme at
least one divisor `≠ 0`, in other words that one has `𝓜_{X_1} ≠ 𝒪_{X_1}^×`, and it suffices to apply `(21.1.10)`. One
already deduces from these results that `X` is reduced `(5.8.5)`. Let us next prove that it verifies condition `(S_2)`
(which will establish that `X` is normal, by virtue of Serre's criterion `(5.8.6)`). Argue by contradiction by
supposing that the set `E` of points `x ∈ X` where `X` does not verify `(S_2)` is non-empty, and let `x ∈ E` be a
point for which `dim(𝒪_{X,x})` is the smallest possible; since `X` verifies `(S_1)`, one has `dim(𝒪_{X,x}) ≥ 2`. In
`X_1 = Spec(𝒪_{X,x})`, the open `U = X_1 − {x}` verifies `(S_2)`; let us show that `X_1` verifies `(S_2)`, so that one
will have reached a contradiction. It suffices, by virtue of `(5.10.5)`, to show that every section `f` of `𝒪_U` over
`U` extends to a section of `𝒪_{X_1}` over `X_1`. Since `X_1` is reduced and `U` dense in `X_1`, `U` is schematically
dense in `X_1`, and consequently `f` is the restriction to `U` of a regular meromorphic section `g ∈ M(X_1)`. Moreover,
since `dim(𝒪_{X,x}) ≥ 2`, one has `cyc(div(g)) ≥ 0` since `g | U = f`; since the homomorphism `cyc` is injective, one
necessarily has `div(g) ≥ 0`, hence `(21.6.4)` `g` is a section of `𝒪_{X_1}` over `X_1`, which establishes our
assertion.

To show that a') implies c), remark then that condition a') implies that the canonical homomorphism
`cyc : Div(X) → 𝔷^1(X)` is surjective; since `X` is normal, it suffices to apply `(21.6.9)`.

Let us now prove that a") entails c). It follows from `(21.6.5)` that a") entails that every prime
`1`-codimensional cycle on `X` is the image by `cyc` of a positive divisor; the first part of the reasoning made
above therefore proves again that `X` verifies `(R_1)` and `(S_1)`. It remains to see that `X` is normal (the end of
the reasoning being then the same), that is to say that if `x ∈ X` is such that `dim(𝒪_{X,x}) ≥ 2`, one has
`prof(𝒪_{X,x}) ≥ 2`. Now, if `y` is a generization of `x` such that `‾{y}` is of codimension `1` in `X`, the reduced
sub-prescheme `Y` of `X` having `‾{y}` for underlying

<!-- original page 279 -->

space is integral, hence regularly immersed in `X` by hypothesis. This entails that there exists a regular element `t`
of `𝒪_{X,x}` such that the ideal `t 𝒪_{X,x}` is the prime ideal defining the prescheme `Y_1`, inverse image of `Y` in
`X_1 = Spec(𝒪_{X,x})`. Since `𝒪_{X,x} / t 𝒪_{X,x}` is integral, this proves that `prof(𝒪_{X,x}) ≥ 2` and finishes the
proof of `(21.7.4)`.

**Remark (21.7.5).**

<!-- label: IV.21.7.5 -->

*One cannot in `(21.7.4)` replace condition a') by the weaker condition that every prime `1`-codimensional cycle of
`X` be the image by `cyc` of a positive divisor. This is shown by the example where `X` is the affine scheme defined
in `(14.1.5)` ("union of a plane and a line meeting it"), which is not normal; with the notations introduced in
`(14.1.5)`, the prime `1`-codimensional cycles of `X` are those of the plane `X_1` and the closed points of the line
`X_2` distinct from the common point of `X_1` and `X_2`; if `t_1`, `t_2`, `t_3` are the images of `T_1`, `T_2`, `T_3`
in `A / 𝔞`, one sees therefore that the prime `1`-codimensional cycles of `X` are defined by the principal prime ideals
of generators `P(t_1, t_2)` (`P` irreducible in `K[T_1, T_2]`) or `t_3 − a`, with `a ≠ 0` in `K`; these elements being
regular in `A / 𝔞`, every `1`-codimensional cycle is indeed the canonical image of a positive divisor.*

**Corollary (21.7.6).**

<!-- label: IV.21.7.6 -->

*Let `X` be a locally Noetherian prescheme, reduced at each of its isolated points. The following conditions are
equivalent:*

*a) The canonical homomorphism `c : 𝒟iv_X → 𝔷_X^1` is an isomorphism of sheaves of ordered groups, and one has
`Div(X) = Div.princ(X)`.*

*a') The canonical homomorphism `c : 𝒟iv_X → 𝔷_X^1` is injective, and every prime `1`-codimensional cycle is the
image by `cyc` of a positive principal divisor, in other words is of the form `cyc(div(f))`, where `f` is a regular
section of `𝒪_X` over `X`.*

*a") For every integral closed sub-prescheme `Y` of `X`, of codimension `1`, there exists a regular section `f` of
`𝒪_X` over `X` such that `Y` is defined by the Ideal `f 𝒪_X`.*

*b) `X` is normal and every prime `1`-codimensional cycle on `X` is principal.*

*c) `X` is locally factorial and `Pic(X) = 0`.*

*d) `X` is normal, and for every open `U` of `X`, one has `Pic(U) = 0`.*

The equivalence of a), a'), a"), b) and c) follows at once from `(21.7.4)` and from `(21.6.11)`. Moreover, it follows
at once from a") that every non-empty open `U` of `X` again verifies the same conditions; in other words these
conditions imply d). It remains to see that d) entails b). Now, denote by `U_λ` the opens that are complements of finite
unions of sets of the form `‾{x}`, where `dim(𝒪_{X,x}) ≥ 2`; it is clear that the `U_λ` form a decreasing filtered
family, and that for every `x ∈ ⋂_λ U_λ`, one has `dim(𝒪_{X,x}) ≤ 1`, hence `𝒪_{X,x}` is a principal ring by virtue
of the hypothesis. One can therefore apply to the family `(U_λ)` proposition `(21.6.12)`, which shows that `Cl(X)` is
isomorphic to `lim Pic(U_λ)`, hence `Cl(X) = 0` by virtue of the hypothesis, which proves b) by definition.

**Remark (21.7.7).**

<!-- label: IV.21.7.7 -->

*When `X = Spec(A)`, where `A` is a Noetherian integral ring, the equivalent conditions of `(21.7.6)` are equivalent
to saying that `A` is a factorial ring.*

<!-- original page 280 -->

### 21.8. Divisors and normalization

**Lemma (21.8.1).**

<!-- label: IV.21.8.1 -->

*Let `f : X' → X` be an integral morphism of preschemes. For every `𝒪_{X'}`-Module locally free `ℰ'` of constant rank
`n` and every `x ∈ X`, there exists an open neighbourhood `U` of `x` in `X` such that, setting `U' = f⁻¹(U)`, `ℰ' | U'`
is isomorphic to `𝒪_{U'}^n`.*

Since the question is local on `X`, one may restrict to the case where `X = Spec(A)` is affine; one then has
`X' = Spec(A')`, where `A'` is an integral `A`-algebra. Then `A'` is the inductive limit of its finite sub-`A`-algebras
`A'_λ`. Setting `X'_λ = Spec(A'_λ)` and denoting by `p_λ : X' → X'_λ` the structure morphism, it follows from `(8.5.2)`
and `(8.5.5)` that there exist an index `λ` and an `𝒪_{X'_λ}`-Module `ℰ'_λ` locally free of rank `n` such that
`ℰ' = p_λ^*(ℰ'_λ)`; it will evidently suffice to prove the lemma for `X'_λ` and `ℰ'_λ`, in other words, one may restrict
to the case where the morphism `f` is finite. Set `B = 𝒪_{X,x}` and let `B'` be the ring of the affine scheme
`X'_0 = X' ×_X Spec(𝒪_{X,x})`; since `B` is a local ring and `B'` is a finite `B`-algebra, `B'` is a semi-local ring
(Bourbaki, _Alg. comm._, chap. V, §2, n° 1, prop. 3); one concludes that the locally free `𝒪_{X'_0}`-Module
`ℰ'_0 = ℰ' ⊗_{𝒪_X} 𝒪_{X,x}` is isomorphic to `𝒪_{X'_0}^n` (Bourbaki, _Alg. comm._, chap. II, §5, n° 3, prop. 5).
Considering `X'_0` as the projective limit

<!-- original page 281 -->

of the preschemes induced by `X'` on the opens `f⁻¹(U)`, where `U` ranges over the filtered set of affine open
neighbourhoods of `x` in `X`, following the method of `(8.1.2, a)`, and applying `(8.5.2.5)`, one obtains the desired
conclusion.

**Corollary (21.8.2).**

<!-- label: IV.21.8.2 -->

*Let `f : X' → X` be an integral morphism of preschemes. Then:*

*(i) `R¹ f_*(𝒪_{X'}^×) = 0` `(0_III, 12.2.1)`.*

*(ii) The group `Pic(X')` is canonically isomorphic to `H¹(X, f_*(𝒪_{X'}^×))`.*

(i) `R¹ f_*(𝒪_{X'}^×)` is the sheaf associated to the presheaf of commutative groups
`U ↦ H¹(f⁻¹(U), 𝒪_{X'}^×)` on `X` (_loc. cit._); the stalk of this sheaf at a point `x` may therefore `(0_I, 5.4.7)`
be identified with the commutative group `lim Pic(f⁻¹(U))`, where `U` ranges over the open neighbourhoods of `x`, the
transition homomorphisms `Pic(f⁻¹(U')) → Pic(f⁻¹(U))` for two opens `U ⊂ U'` being defined by `(21.3.2.4)`. Now, for
every `x ∈ X`, every open neighbourhood `U'` of `x` in `X`, and every element `ζ' ∈ Pic(f⁻¹(U'))`, it follows from
`(21.8.1)` that there is an open neighbourhood `U ⊂ U'` of `x` such that the image of `ζ'` in `Pic(f⁻¹(U))` is zero.
Hence the stalk of `R¹ f_*(𝒪_{X'}^×)` at `x` is zero.

(ii) The Leray spectral sequence for the composite functor `ℱ ↦ Γ(X, f_*(ℱ))` on sheaves of commutative groups on `X'`
`(T, 2.4)` gives the exact sequence of low-degree terms `(M, XV, 6)`

```text
                         0 → H¹(X, f_*(𝒪_{X'}^×)) → H¹(X', 𝒪_{X'}^×) → H⁰(X, R¹ f_*(𝒪_{X'}^×))
```

and the conclusion follows from (i) and from the isomorphism between `Pic(X')` and `H¹(X', 𝒪_{X'}^×)` `(0_I, 5.4.7)`.

**Proposition (21.8.3).**

<!-- label: IV.21.8.3 -->

*Let `f = (ψ, θ) : X' → X` be an integral morphism of preschemes; suppose that, for every open `U` of `X`, the
homomorphism `Γ(θ) : Γ(U, 𝒪_X) → Γ(f⁻¹(U), 𝒪_{X'})` sends regular elements to regular elements, which permits one
canonically to extend the homomorphism `θ : 𝒪_X → f_*(𝒪_{X'})` to a homomorphism of sheaves of rings
`θ' : 𝓜_X → f_*(𝓜_{X'})`, whence homomorphisms of sheaves of multiplicative groups
`θ^* : 𝒪_X^× → f_*(𝒪_{X'}^×)` and `θ'^* : 𝓜_X^× → f_*(𝓜_{X'}^×)`, yielding by passage to quotients a homomorphism
`θ''^* : 𝒟iv_X → f_*(𝒟iv_{X'})`. One then has a commutative diagram*

```text
                         1 ——→ 𝒪_X^×  ——→  𝓜_X^×  ——→  𝒟iv_X  ——→  0
                                  │           │           │
  (21.8.3.1)                    θ^*│        θ'^*│        θ''^*│
                                  ↓           ↓           ↓
                         1 ——→ f_*(𝒪_{X'}^×) → f_*(𝓜_{X'}^×) → f_*(𝒟iv_{X'}) → 0
```

*in which both rows are exact.*

The only point to verify is the exactness of the second row of the diagram, which follows from applying the exact
cohomology sequence for the functor `f_*` to the exact sequence of sheaves of commutative groups on `X'`

```text
                         1 → 𝒪_{X'}^× → 𝓜_{X'}^× → 𝒟iv_{X'} → 0
```

and from `(21.8.2)`.

<!-- original page 282 -->

**Corollary (21.8.4).**

<!-- label: IV.21.8.4 -->

*If, in addition to the hypotheses of `(21.8.3)`, the homomorphism `θ'` is an isomorphism of sheaves of rings, then
`θ^* : 𝒪_X^× → f_*(𝒪_{X'}^×)` is injective, `θ''^* : 𝒟iv_X → f_*(𝒟iv_{X'})` is surjective and `Ker(θ''^*)` is isomorphic
to `Coker(θ^*)`.*

This is an immediate consequence of the snake-diagram lemma (Bourbaki, _Alg. comm._, chap. I, §2, n° 4, prop. 2)
applied to the diagram `(21.8.3.1)`.

**Proposition (21.8.5).**

<!-- label: IV.21.8.5 -->

*Let `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` an integral morphism; assume that there exists a
schematically dense open `U` in `X` such that `f⁻¹(U)` is schematically dense in `X'` `(cf. (20.3.5))`, and that the
morphism `f⁻¹(U) → U`, the restriction of `f`, is an isomorphism. Then:*

*(i) The homomorphism `θ' : 𝓜_X → f_*(𝓜_{X'})` is defined and bijective, the homomorphism `θ^* : 𝒪_X^× → f_*(𝒪_{X'}^×)`
is injective, the homomorphism `θ''^* : 𝒟iv_X → f_*(𝒟iv_{X'})` is surjective, `Ker(θ''^*)` is isomorphic to
`𝒩 = Coker(θ^*)`, and the support of the sheaf of multiplicative groups `𝒩` is contained in `S = X − U`.*

*(ii) Assume in addition that the set `S` is discrete and, to abbreviate, set `𝒪'_X = f_*(𝒪_{X'})`. Then one has a
commutative diagram*

```text
                                  j                            i_X    i_{X'}
  1 → ∏_{s ∈ S} 𝒪'^×_{X,s}/𝒪^×_{X,s} ─→ Div(X) ──→ Div(X') ─→ 0
                                  │           │
  (21.8.5.1)                      │           │
                                  ↓           ↓
  1 → (∏_{s ∈ S} 𝒪'^×_{X,s}/𝒪^×_{X,s}) / Im Γ(X', 𝒪_{X'}^×) ─→ Pic(X) ─→ Pic(X') ─→ 0
                                  j'
```

*where the rows are exact and where the left vertical arrow is the canonical homomorphism.*

(i) The hypothesis entails that one has a canonical isomorphism `𝓜_X ⥲ f_*(𝓜_{X'})` for the sheaves of germs of
pseudo-functions `(20.2.2)`, whence the assertion concerning `θ'`, in view of the existence of the canonical
isomorphisms `𝓜_X ⥲ 𝓜'_X` and `𝓜_{X'} ⥲ 𝓜'_{X'}` `(20.2.11)`. The rest of assertion (i) follows from `(21.8.4)`, except
for what concerns the support of `𝒩`, which follows directly from the hypothesis on `U`.

(ii) Applying the exact cohomology sequence to the two exact sequences of sheaves of commutative groups

```text
                         1 → 𝒩 → 𝒟iv_X → f_*(𝒟iv_{X'}) → 0
  (21.8.5.2)
                         1 → 𝒪_X^× → f_*(𝒪_{X'}^×) → 𝒩 → 1
```

one obtains respectively the exact sequences

```text
                         1 → Γ(X, 𝒩) ─→ Div(X) → Div(X') → H¹(X, 𝒩)
                                       j
  (21.8.5.3)
                         Γ(X', 𝒪_{X'}^×) → Γ(X, 𝒩) ─→ Pic(X) → Pic(X') → H¹(X, 𝒩)
                                                    ∂
```

taking account of the canonical isomorphism `Pic(X') ⥲ H¹(X, f_*(𝒪_{X'}^×))` `(21.8.2)`. Now, since the support of `𝒩`
is contained in the discrete set `S`, closed in `X`, one has

<!-- original page 283 -->

`H¹(X, 𝒩) = H¹(S, 𝒩 | S)` `(G, II, 4.9.2)` and `H¹(S, 𝒩 | S) = ∏_{s ∈ S} H¹({s}, 𝒩_s) = 0` by definition of cohomology
`(G, II, 4.4)`. Similarly one has `Γ(X, 𝒩) = ∏_{s ∈ S} 𝒩_s` and `𝒩_s = 𝒪'^×_{X,s} / 𝒪^×_{X,s}`, by virtue of the second
exact sequence `(21.8.5.2)`. It remains to make precise the injections `j` and `j'`. One can describe a section `t` of
`𝒩` over `X` by taking a covering of `X` formed by `U` and by opens `U_i` such that `U_i ∩ S` is reduced to a single
point `s_i` and that `U_i ∩ U_j ⊂ U` for `i ≠ j`, then considering for each `i` a section `t_i` of `𝒩` over `U_i`,
necessarily such that `(t_i)_{s_i} ∈ 𝒪'^×_{X,s_i} / 𝒪^×_{X,s_i}` and `(t_i)_x = 0` at the points `x ∈ U_i − {s_i}`. The
germ `(t_i)_{s_i}` comes from a section `u_i` of `𝒪_{X'}^×` over `f⁻¹(U_i)`, which one may also consider as a section
of `𝓜_{X'}^×` over `f⁻¹(U_i)`, hence a section of `𝓜_X^×` over `U_i` (in virtue of the hypothesis); there corresponds
canonically to this section a section `d_i ∈ Γ(U_i, 𝒟iv_X)`, and since in `f⁻¹(U ∩ U_j)` the restriction of `u_i` is
identified with a section of `𝒪_{X'}^×` over `U ∩ U_j` by virtue of the hypothesis, the restrictions of the `d_i` to
`U ∩ U_j` are all zero, so the `d_i` are the restrictions of one and the same divisor `d ∈ Div(X)`, which is the image
of the section `t` under `j`. Similarly, the image of `t` under `∂ : Γ(X, 𝒩) → H¹(X, 𝒪_X^×)` comes from the cocycle
equal to the restriction of `𝒩` in `U ∩ U_j` for each `i`, to `(u_i | (U_i ∩ U_j))(u_j | (U_i ∩ U_j))⁻¹` in `U_i ∩ U_j`,
whence the expression of `j'(t)` and the commutativity of the diagram `(21.8.5.1)`.

**Remarks (21.8.6).**

<!-- label: IV.21.8.6 -->

(i) The conditions of application of `(21.8.5, (i))` are in particular satisfied when `X` is a reduced locally
Noetherian prescheme having only finitely many irreducible components, `X'` its normalization, and `X'` is also locally
Noetherian `(II, 6.3.8)`; the `𝒪_X`-Module `𝒟iv_X` is then an extension of `f_*(𝒟iv_{X'})` by the cokernel `𝒩` of
`𝒪_X^× → f_*(𝒪_{X'}^×)`, which one may regard as known. If moreover `X` is a (reduced) algebraic curve over a field
`k`, one is in the conditions of application of `(21.8.5, (ii))`.

(ii) When the conditions of application of `(21.8.5, (ii))` are satisfied and moreover the global canonical
homomorphism `Γ(X, 𝒪_X) → Γ(X', 𝒪_{X'})` is bijective, one sees that the kernels of the surjective homomorphisms
`Div(X) → Div(X')` and `Pic(X) → Pic(X')` are isomorphic.

(iii) When the conditions of application of `(21.8.5, (ii))` are satisfied, one sees that the homomorphism
`Div(X) → Div(X')` can be injective (in which case it is bijective) only if `𝒪'^×_{X,s} = 𝒪^×_{X,s}` for every `s ∈ S`.
For an `s ∈ S` such that the ring `𝒪'_{X,s}` is local (which, taking into account that `X' = Spec(𝒪'_X)` `(II, 1.3)`,
means that there exists *only one* point `s' ∈ X'` above `s`), this implies necessarily that the residue fields `k(s)`
and `k(s')` are equal and that `1 + 𝔪_s = 1 + 𝔪_{s'}`, hence finally is equivalent to the relation `𝒪'_{X,s} = 𝒪_{X,s}`,
or also (taking the hypothesis into account) to the fact that there is an open neighbourhood `V` of `s` in `X` such that
the morphism `f⁻¹(V) → V` is an isomorphism. In the general case, the ring `𝒪'_{X,s}` is semi-local (this is evident
when the morphism `f` is finite, and in the general case it follows from `(0_IV, 23.2.6)`); the canonical homomorphism
`𝒪^×_{X,s} → 𝒪'^×_{X,s}` defines, by passage to quotients, a homomorphism from the multiplicative group `(k(s))^×` to
the product of the multiplicative groups `(k(s'_j))^×`, the `s'_j` being the points (in

<!-- original page 284 -->

number `> 1`) of `X'` above `s`. It is immediate that this homomorphism can be bijective only if `k(s)` and all the
`k(s'_j)` are equal to the field `𝔽_2` with `2` elements; moreover, if this condition is verified, it is necessary in
addition that the multiplicative group `1 + 𝔪_s` have image `1 + 𝔯`, where `𝔯` is the radical of `𝒪'_{X,s}`, or also
that `𝔪_s = 𝔯`, which entails that `𝒪'_{X,s} ⊗_{𝒪_{X,s}} k(s)` is a direct sum of fields isomorphic to `k(s)` (which,
when the morphism `f` is finite, entails that it is unramified at the points `s'_j` `(17.4.1)`). If, for example, no
residue field of `X` is isomorphic to `𝔽_2`, the canonical homomorphism `Div(X) → Div(X')` can be bijective only if `f`
is an isomorphism. In the case where the canonical homomorphism `Γ(X, 𝒪_X) → Γ(X', 𝒪_{X'})` is bijective, one concludes
from the preceding and from (ii) that in the previous considerations one may replace the homomorphism
`Div(X) → Div(X')` by the homomorphism `Pic(X) → Pic(X')`.

### 21.9. Divisors on preschemes of dimension 1

**(21.9.1).** Let `X` be a topological space, `x` a point of `X`, `i_x : {x} → X` the canonical injection. If `A(x)` is
a commutative group, one may regard it as a sheaf of commutative groups on the space `{x}` reduced to a single point,
and take its direct image `(i_x)_*(A(x))`, which is a sheaf of commutative groups on `X` `(0_I, 3.4.1)`; it follows at
once from the definitions that for every open `U` of `X`, `Γ(U, (i_x)_*(A(x))) = A(x)` if `x ∈ U`, and reduces to `0`
in the contrary case; hence, for `y ∈ {x}` one has `((i_x)_*(A(x)))_y = A(x)`, and for `y ∉ {x}`,
`((i_x)_*(A(x)))_y = 0`.

If now `ℱ` is a sheaf of commutative groups on `X` and `Y` a part of `X`, for every open `U` of `X` one has a canonical
homomorphism

```text
  (21.9.1.1)             Γ(U, ℱ) → ∏_{x ∈ U ∩ Y} ℱ_x = ∏_{x ∈ Y} Γ(U, (i_x)_*(ℱ_x))
```

and since these homomorphisms commute with the restriction operators, they define a canonical homomorphism of sheaves

```text
  (21.9.1.2)             j_Y : ℱ → ∏_{x ∈ Y} (i_x)_*(ℱ_x).
```

**Lemma (21.9.2).**

<!-- label: IV.21.9.2 -->

*Let `X` be a locally Noetherian topological space, `X_0` the set of its closed points, `ℱ` a sheaf of commutative
groups on `X`. The following conditions are equivalent:*

*a) The canonical homomorphism `j_{X_0} : ℱ → ∏_{x ∈ X_0} (i_x)_*(ℱ_x)` is injective and has as image
`⨁_{x ∈ X_0} (i_x)_*(ℱ_x)`.*

*a') There exists a family of commutative groups `(A(x))_{x ∈ X_0}` such that `ℱ` is isomorphic to
`⨁_{x ∈ X_0} (i_x)_*(A(x))`.*

*b) Every section of `ℱ` over an open `U` of `X` has a discrete support contained in `X_0`.*

*When this is so, for every `x ∈ X_0`, the group `A(x)` is determined up to unique isomorphism and is isomorphic to
`ℱ_x`. Moreover, the sheaf `ℱ` is then flasque.*

Since the points of `X_0` are closed in `X`, one has `((i_x)_*(A(x)))_y = 0` for every

<!-- original page 285 -->

`y ≠ x ∈ X_0`; this remark proves the uniqueness assertion relative to the groups `A(x)`, and it is clear besides that
a) implies a'). To see that a') implies b), one may restrict to the case where `U` is Noetherian; then `(G, II, 3.10)`
one has

```text
                         Γ(U, ⨁_{x ∈ X_0} (i_x)_*(A(x))) = ⨁_{x ∈ X_0} Γ(U, (i_x)_*(A(x)))
```

so every section `s` of `ℱ` over `U` is a direct sum of finitely many sections
`s_k ∈ Γ(U, (i_{x_k})_*(A(x_k)))` (`1 ≤ k ≤ n`) with `x_k ∈ X_0`. But since `x_k` is closed in `X`, the support of `s_k`
is reduced to `x_k`, so the support of `s` is contained in the finite set of the `x_k`, which is evidently discrete
since the points `x_k` are closed. Let us finally show that b) entails a); for every Noetherian open `U`, any support of
a section of `ℱ` over `U`, being discrete and quasi-compact, is finite. One thus deduces from hypothesis b) that for
every Noetherian open `U`, the image of the homomorphism `(21.9.1.1)` (for `Y = X_0`) is contained in
`⨁_{x ∈ X_0} Γ(U, (i_x)_*(ℱ_x))` and that this homomorphism is injective, which establishes a).

Finally, to show that `ℱ` is flasque, consider a section `s` of `ℱ` over an open `U` of `X`; since the support of `s` is
a discrete and closed subspace of `X`, one extends `s` to a section `s'` of `ℱ` over `X` by setting `s'_z = 0` in
`X − U`.

**Remarks (21.9.3).**

<!-- label: IV.21.9.3 -->

(i) In condition b) of `(21.9.2)`, it does not suffice to suppose that the support of every section of `ℱ` over an
arbitrary open of `X` is discrete; this is shown by the example where one takes for `X` the spectrum of a discrete
valuation ring, with a closed point `b` and a generic point `a`, and for `ℱ` the sheaf of commutative groups such that
`ℱ_b = 0` and `ℱ_a = ℤ`.

(ii) Assume that the conditions of `(21.9.2)` are verified; let `E` be a discrete part of `X_0`, and for every `x ∈ E`,
let `a(x)` be an element of `A(x)`. Then there exists one and only one section `t` of `⨁_{x ∈ X_0} (i_x)_*(A(x))` over
`X` such that `t_x = a(x)` for every `x ∈ E` and that the support of `t` is contained in `E`. Indeed, for every
Noetherian open `U`, `E ∩ U` is finite, and it suffices to take for `t` the section of
`⨁_{x ∈ X_0} (i_x)_*(A(x))` whose restriction to each Noetherian open `U` is the sum of the `a(x)` for `x ∈ E ∩ U`.

**Proposition (21.9.4).**

<!-- label: IV.21.9.4 -->

*Let `X` be a locally Noetherian prescheme of dimension `≤ 1`, `X^{(1)}` the set of points `x ∈ X` such that
`dim(𝒪_{X,x}) = 1`. One then has a canonical isomorphism*

```text
  (21.9.4.1)             𝒟iv_X ⥲ ⨁_{x ∈ X^{(1)}} (i_x)_*(Div(𝒪_{X,x}))
```

*and `𝒟iv_X` is flasque.*

Taking the isomorphism `(21.4.6.1)` into account, the homomorphism `(21.9.4.1)` is defined by `(21.9.1.2)`: let us
prove that it is a bijection. Since `dim(X) ≤ 1`, the points of `X^{(1)}` are the non-isolated closed points of `X`. One
is reduced to proving that: 1° `𝒟iv_X` verifies condition b) of `(21.9.2)`; 2° for every isolated point `x ∈ X`, one has
`(𝒟iv_X)_x = 0`. The second point follows from the fact that `𝒪_{X,x}` is then an Artinian ring and so every regular
element of `𝒪_{X,x}` is invertible. For the first, it suffices to note that for every open `U` of `X` and every divisor
`D ∈ Div(U)`, the maximal points of the support `S` of `D` are such that

<!-- original page 286 -->

`prof(𝒪_{X,x}) = 1` `(21.1.9)`, so a fortiori belong to `X^{(1)} ∩ U`; since `dim(X) ≤ 1`, the set of these points
equals `S`, and `S` is therefore discrete, the set of irreducible components of `S` being locally finite.

**Corollary (21.9.5).**

<!-- label: IV.21.9.5 -->

*Let `X` be a locally Noetherian prescheme of dimension `≤ 1`. For every discrete part `E ⊂ X^{(1)}` and every family
`(D(x))_{x ∈ E}` with `D(x) ∈ Div(𝒪_{X,x})`, there exists one and only one divisor `D` on `X` such that the support of
`D` is contained in `E` and `D_x = D(x)` for every `x ∈ E`.*

This follows from `(21.9.4)` and `(21.9.3, (ii))`.

**Corollary (21.9.6).**

<!-- label: IV.21.9.6 -->

*Let `X` be a locally Noetherian prescheme of dimension `≤ 1`; every divisor `D` on `X` is of the form `D' − D''`, where
`D'`, `D''` are two divisors `≥ 0` with supports contained in that of `D`.*

In virtue of `(21.9.5)`, one is at once reduced to the case where `X = Spec(A)`, `A` a Noetherian local ring; it then
suffices to observe that `M(X)` is the total ring of fractions of `A`, and that a section of `𝓜_X^×` over `X` is by
definition expressible as a quotient `b/a` of two regular elements of `A`.

**Corollary (21.9.7).**

<!-- label: IV.21.9.7 -->

*Let `X` be a locally Noetherian prescheme of dimension `≤ 1`, having no isolated point, and `U` a dense open in `X`.
Then there exists a divisor `D ≥ 0` on `X`, with support contained in `U` and meeting each of the irreducible components
of `X`.*

One may assume that `U` is the union of disjoint non-empty open sets `U_α`, each contained in a single irreducible
component of `X`; it then suffices to take in each `U_α` a point `x_α` closed in `X` (such a point exists since the
unique generic point of `U_α` cannot be isolated by hypothesis), and to apply `(21.9.5)` to the discrete set of the
`x_α`.

The interest of this corollary is that it will allow one to prove that a separated algebraic curve `X` over a field `k`
is quasi-projective, the divisor `D ≥ 0` defined in `(21.9.7)` being then necessarily ample in virtue of the Riemann-
Roch theorem for curves (chap. V).

**(21.9.8).** For locally Noetherian preschemes `X` of dimension `≤ 1`, proposition `(21.9.4)` reduces the determination
of `𝒟iv_X` to the case where `X = Spec(A)`, `A` a Noetherian local ring of dimension `1`.

When `A` is a regular local ring of dimension `1` (in other words, a discrete valuation ring), the group `Div(A)` is
canonically identified with `ℤ` `(21.6.8)`; consequently, in virtue of `(21.9.2)`:

**Proposition (21.9.9).**

<!-- label: IV.21.9.9 -->

*Let `X` be a regular locally Noetherian prescheme of dimension `≤ 1`. Then the sheaf `𝒟iv_X` is canonically isomorphic
to `⨁_{x ∈ X^{(1)}} (i_x)_*(ℤ(x))`, where `ℤ(x)` is the additive group `ℤ` considered as a sheaf of groups on the space
`{x}`.*

**(21.9.10).** Assume only that the Noetherian local ring `A` of dimension `1` is reduced; then, if `A'` is the
normalization of `A` (integral closure of `A` in its total ring of fractions), `A'` is Noetherian in virtue of the
Krull-Akizuki theorem (Bourbaki, _Alg. comm._, chap. VII, §2, n° 5, prop. 5), and one saw in `(21.8.6)` how

<!-- original page 287 -->

`Div(A)` may be obtained as an *extension* of `Div(A')`, the latter group being of the form `ℤ^r`.

**Proposition (21.9.11).**

<!-- label: IV.21.9.11 -->

*Let `X` be a Noetherian prescheme, `X_0` a closed subprescheme of `X` having the following properties:*

*1° `dim(X_0) ≤ 1`.*

*2° For every locally closed part `Y` of `X` such that `Y ∩ X_0` is discrete, there exists a part `Y'` of `Y`, closed
in `X` and open in `Y`, containing `Y ∩ X_0`.*

*Under these conditions:*

*(i) Let `Z_0` be the union of the sets `{x} ∩ X_0` as `x` ranges over the part of `Ass(𝒪_X)` formed by points such
that `{x} ∩ X_0` is finite. Then, for every divisor `D_0` on `X_0` whose support does not meet `Z_0`, there exists a
divisor `D` on `X` whose inverse image under the canonical injection `X_0 → X` exists `(21.4)` and equals `D_0`; if
moreover `D_0 ≥ 0`, one may suppose `D ≥ 0`.*

*(ii) Assume in addition that there exists in `X_0` an affine open `U_0` containing `Ass(𝒪_{X_0}) ∪ Z_0` (a condition
automatically satisfied when there exists an ample `𝒪_{X_0}`-Module `(II, 4.5.4)`). Then the canonical homomorphism
`(21.3.2.4)` `Pic(X) → Pic(X_0)` is surjective.*

(i) Taking `(21.9.6)` into account, one may restrict to proving the assertion concerning divisors `D_0 ≥ 0`; in virtue
of `(21.9.4)`, the support `T` of `D_0` is a finite discrete and closed set in `X_0`. One may suppose `D_0 ≠ 0`, that
is, `T ≠ ∅`, otherwise there is nothing to prove. For every `x ∈ T`, there exists an element `s_x ∈ 𝒪_{X_0,x}` which is
not a zero-divisor in this ring, belongs to its maximal ideal, and whose image in `(𝒟iv_{X_0})_x` is `(D_0)_x`. There
exists an affine open neighbourhood `U^{(x)}` of `x` in `X` and a section `g^{(x)}` of `𝒪_X` over `U^{(x)}` such that
`s_x` is the image in `𝒪_{X_0,x}` of the germ `(g^{(x)})_x ∈ 𝒪_{X,x}`; we shall see that by taking `U^{(x)}` small
enough, one can arrange for `g^{(x)}` not to be a zero-divisor in `Γ(U^{(x)}, 𝒪_X)`, in other words `(3.1.9)`, denoting
by `V^{(x)}` the closed part of `U^{(x)}` formed by `y` such that `g^{(x)}(y) = 0`, one has
`V^{(x)} ∩ Ass(𝒪_X) = ∅`. Now, if `z ∈ Ass(𝒪_X)`, the hypothesis `x ∉ Z_0` entails that one has either `x ∉ {z}`, or
`x` is not isolated in `{z} ∩ X_0`. By replacing `U^{(x)}` by a smaller open, one may suppose that the second case
occurs for a `z ∈ V^{(x)} ∩ Ass(𝒪_X)`; `V^{(x)}` would therefore contain an irreducible component of dimension `1` of
`X_0 ∩ U^{(x)}` containing `x`; but this would mean that the image `ḡ^{(x)}` of `g^{(x)}` in `Γ(U^{(x)} ∩ X_0, 𝒪_{X_0})`
would be in the nilradical of this ring, and consequently `s_x` would belong to the nilradical of `𝒪_{X_0,x}`, which is
absurd. One has therefore `x ∉ {z}` for every point `z ∈ V^{(x)} ∩ Ass(𝒪_X)`, and since this set is finite, one may,
by replacing `U^{(x)}` by a smaller open neighbourhood of `x`, suppose that `V^{(x)} ∩ Ass(𝒪_X) = ∅`.

By virtue of the choice of `U^{(x)}`, one may define a divisor `D'^{(x)}` on `U^{(x)}` by
`D'^{(x)} = div(g^{(x)})`; moreover, one saw above that `x` is necessarily isolated in `V^{(x)} ∩ X_0`, so by replacing
`U^{(x)}` again by a smaller open neighbourhood of `x`, one may suppose that `V^{(x)} ∩ X_0` is reduced to the point
`x`. But there exists then, in virtue of condition 2°, a part `W^{(x)}` of `V^{(x)}`, closed in `X` and open in
`V^{(x)}`, such that `W^{(x)} ∩ X_0 = {x}`. Replacing `U^{(x)}` again by a smaller open neighbourhood of `x`, one may
therefore suppose

<!-- original page 288 -->

that `W^{(x)} = V^{(x)}`, in other words that `V^{(x)}` is closed in `X`. One may then define a divisor `D^{(x)}` on
`X` by the condition that `D^{(x)} | U^{(x)} = D'^{(x)}` and `D^{(x)} | (X − V^{(x)}) = 0`, which makes sense because in
`U^{(x)} ∩ (X − V^{(x)})` the restriction of `g^{(x)}` is an invertible section, so the restrictions to this open of the
two divisors considered on `U^{(x)}` and `X − V^{(x)}` are equal. It then suffices, to answer the question, to take
`D = ∑_{x ∈ T} D^{(x)}`, which makes sense since `T` is finite.

(ii) Taking the commutative diagram `(21.4.2.1)` into account, the conclusion will follow from (i) if one proves that
every invertible `𝒪_{X_0}`-Module `ℒ_0` is isomorphic to an `𝒪_{X_0}`-Module of the form `𝒪_{X_0}(D_0)` `(21.2.8)`,
where `D_0` is a divisor on `X_0` whose support does not meet `Z_0`. Now, since `U_0` is schematically dense in `X_0`
`(20.2.13, (iv))`, it suffices for this to prove that there exists a section `t ∈ Γ(U_0, ℒ_0)` such that `t(z_0) ≠ 0`
at the points of `Ass(𝒪_{X_0}) ∪ Z_0` `(3.1.9)`. One may therefore restrict to the case where `X_0 = Spec(A_0)` is
affine; but then `ℒ_0` is ample `(II, 5.1.4)` and since the set `Ass(𝒪_{X_0}) ∪ Z_0` is finite, the conclusion follows
from `(II, 4.5.4)`.

**Corollary (21.9.12).**

<!-- label: IV.21.9.12 -->

*Let `A` be a Henselian local ring `(18.5.8)`, `S = Spec(A)`, `s_0` the closed point of `S`, `f : X → S` a separated
morphism of finite presentation, and suppose that the set `X_0 = f⁻¹(s_0)` is of dimension `≤ 1`. Then, for every closed
subscheme `X'_0` of `X` having `X_0` as underlying set and of finite presentation over `S`, the canonical homomorphism
`(21.3.2.4)` `Pic(X) → Pic(X'_0)` is surjective.*

Let us first show that it suffices to prove the corollary when the Henselian local ring `A` is moreover Noetherian. One
knows in fact `(18.6.15)` that one can write `A = lim A_λ`, where the `A_λ` are Noetherian Henselian local rings, the
homomorphisms `A_λ → A` being local; there exists in addition an index `α` and a separated morphism of finite
presentation `f_α : X_α → S_α = Spec(A_α)` such that `X` and `f` are deduced from `X_α` and `f_α` by the base change
`S → S_α` `(8.10.5, (v))`; with the usual notation `(8.8.1)`, the morphisms `f_λ : X_λ → S_λ` will be separated for
`λ ≥ α` and one will have `X = X_λ ×_{S_λ} S`. Moreover, one may assume that, if `s_{0λ}` is the unique closed point of
`S_λ`, there is a closed subscheme `X'_{0λ}` of `X_λ`, having the same underlying set as `f_λ⁻¹(s_{0λ})`, such that
`X'_0 = X'_{0λ} ×_{S_λ} S` `(8.6.3)`; one has, for `λ ≥ α`, `dim(X'_{0λ}) = dim(X'_0) ≤ 1` by transitivity of fibres and
`(4.1.4)`. It is a matter of seeing that if one has proved that the homomorphism `Pic(X_λ) → Pic(X'_{0λ})` is surjective
for every `λ ≥ α`, then it is the same for `Pic(X) → Pic(X'_0)`. One evidently has the commutative diagram of canonical
homomorphisms

```text
                         Pic(X_λ) ──→ Pic(X)
                              │           │
                              ↓           ↓
                         Pic(X'_{0λ}) ─→ Pic(X'_0)
```

For every invertible `𝒪_{X'_0}`-Module `ℒ'_0`, there exist a `λ ≥ α` and an invertible `𝒪_{X'_{0λ}}`-Module `ℒ'_{0λ}`
such that `ℒ'_0` is deduced from it by the base change `S → S_λ` `(8.5.2` and `8.5.5)`; it suffices to

<!-- original page 289 -->

consider an invertible `𝒪_{X_λ}`-Module `ℒ_λ` such that `cl(ℒ'_{0λ})` is the image of `cl(ℒ_λ)` in `Pic(X'_{0λ})`, then
to take the invertible `𝒪_X`-Module `ℒ` deduced from `ℒ_λ` by the base change; in virtue of the commutativity of the
preceding diagram, `cl(ℒ'_0)` will be the image of `cl(ℒ)`.

Therefore assume `A` Noetherian, hence so is `X`, and verify that `X` and `X'_0` satisfy the conditions of
`(21.9.11, (ii))`. One has by hypothesis `dim(X'_0) ≤ 1`; on the other hand, to verify condition 2° of `(21.9.11)`,
consider a subprescheme `Y` of `X` having `Y` as underlying set; the morphism `g : Y → S`, restriction of `f`, being
quasi-finite at each of the points `x_i` of `Y ∩ X_0` (`1 ≤ i ≤ n`), one may apply `(18.5.11, c)` and one sees that `Y`
is the sum of the open subpreschemes `Y_i = Spec(𝒪_{Y,x_i})` (`1 ≤ i ≤ n`) and of a prescheme `Y''` such that
`Y'' ∩ X_0 = ∅`, and moreover the canonical injections `j_i : Y_i → X` are such that `f ∘ j_i` is a finite morphism.
Since `f` is separated, `j_i` is also a finite morphism, so `Y_i` is closed in `X`; one therefore answers the question
by taking `Y' = ⋃_{1 ≤ i ≤ n} Y_i`.

It remains to verify the supplementary hypothesis of `(21.9.11, (ii))`. Now, `X'_0` being a separated curve over the
field `k(s_0)`, is a quasi-projective `k(s_0)`-scheme (chap. V) [^1], so there exists an ample `𝒪_{X'_0}`-Module
`(II, 5.3.1)`, and this completes the proof.

**Remark (21.9.13).**

<!-- label: IV.21.9.13 -->

Under the conditions of `(21.9.12)`, assuming moreover `f` proper, the morphism `f` is even projective: indeed, if
`ℒ'_0` is an ample `𝒪_{X'_0}`-Module, there exists, in virtue of `(21.9.12)`, an invertible `𝒪_X`-Module `ℒ` whose
inverse image in `X'_0` is isomorphic to `ℒ'_0`, hence is ample. Since every neighbourhood of `s_0` in `S` is
necessarily all of `S`, one then deduces from `(9.6.4)` that `ℒ` is an ample `𝒪_X`-Module, whence the conclusion
`(II, 5.3.1` and `II, 5.5.3)`.

### 21.10. Inverse images and direct images of 1-codimensional cycles

In a later chapter, devoted to intersection theory, the notions of inverse image and direct image of cycles will be
developed systematically. In the present number, we content ourselves with defining these notions in certain useful
particular cases, and for *1-codimensional* cycles, these definitions being chosen so that they are compatible with the
corresponding definitions for divisors `(21.4` and `21.5)`, taking account of the homomorphism `cyc` defined in
`(21.6)`.

**(21.10.1).** Let `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` a morphism, `T` a part of `X`; assume
that the image under `f` of every maximal point of `X'` is a maximal point of `X`, and that, for every `x' ∈ X'^{(1)}`
(i.e. such that `dim(𝒪_{X',x'}) = 1`), one has *one* of the three following conditions for the point `x = f(x')`:

(i) `x ∉ T`;

(ii) `x ∈ X^{(1)}` and `𝒪_{X',x'}` is a flat `𝒪_{X,x}`-module;

(iii) the ring `𝒪_{X,x}` is factorial and `𝔪_x ∉ Ass(𝒪_{X',x'})`.

Under these conditions, we propose, for every 1-codimensional cycle `Z` on `X` with support contained in `T`, to define
a 1-codimensional cycle `Z' = f^*(Z)`, so

[^1]: The reader will verify that `(21.9.12)` is not used to prove this property in chap. V.

<!-- original page 290 -->

that `Z ↦ f^*(Z)` is a homomorphism of ordered groups from the subgroup of `𝔍^1(X)` formed by cycles with support
contained in `T` to the ordered group `𝔍^1(X')`. For this, let

```text
  (21.10.1.1)            Z = ∑_{x ∈ T ∩ X^{(1)}} n_x · {x}
```

where the family of `x ∈ T ∩ X^{(1)}` such that `n_x ≠ 0` is locally finite. For every `x' ∈ X'^{(1)}`, let us define an
integer `n_{x'}` in the following way, setting `x = f(x')`:

1° if `x ∉ T`, take `n_{x'} = 0`;

2° if `x ∈ X^{(1)}` and `𝒪_{X',x'}` is a flat `𝒪_{X,x}`-module, one knows `(6.1.1)` that
`dim(𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}) = 0`; in other words `𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}` is an `𝒪_{X',x'}`-module of finite
length `λ_{x'}`, and one takes `n_{x'} = λ_{x'} n_x`;

3° if `𝒪_{X,x}` is factorial and `𝔪_x ∉ Ass(𝒪_{X',x'})`, one knows `(21.6.9)` that the canonical homomorphism
`cyc : Div(𝒪_{X,x}) → 𝔍^1(Spec(𝒪_{X,x}))` is bijective, and on the other hand since `dim(𝒪_{X',x'}) = 1` and
`𝔪_x ∉ Ass(𝒪_{X',x'})`, `Ass(𝒪_{X',x'})` consists solely of the maximal points of `Spec(𝒪_{X',x'})`, so the hypothesis
on `f` implies that `f(Ass(𝒪_{X',x'})) ⊂ Ass(𝒪_{X,x})`, and it follows from `(21.4.5, (ii))` that the homomorphism
`f^* : Div(𝒪_{X,x}) → Div(𝒪_{X',x'})` is defined; finally, `x'` being the unique closed point of `Spec(𝒪_{X',x'})`,
`𝔍^1(Spec(𝒪_{X',x'}))` is canonically isomorphic to `ℤ`. One has therefore a composite canonical homomorphism

```text
                                    cyc⁻¹              f^*                cyc
  (21.10.1.2)            𝔍^1(Spec(𝒪_{X,x})) ─→ Div(𝒪_{X,x}) ─→ Div(𝒪_{X',x'}) ─→ 𝔍^1(Spec(𝒪_{X',x'})) ⥲ ℤ.
```

If `Z_x` is the cycle `∑_{y ∈ Spec(𝒪_{X,x}) ∩ X^{(1)}} n_y · ({y} ∩ Spec(𝒪_{X,x}))` on `Spec(𝒪_{X,x})`, one takes for
`n_{x'}` the image of `Z_x` under the homomorphism `(21.10.1.2)`.

**(21.10.2).** We propose to show that:

A) When two of the conditions 1°, 2°, 3° of `(21.10.1)` are simultaneously satisfied, the corresponding values of
`n_{x'}` coincide.

B) The set of `x' ∈ X'^{(1)}` such that `n_{x'} ≠ 0` is locally finite in `X'`.

To prove A), assume first that `x ∉ T` and that `x` verifies one of conditions 2° or 3° of `(21.10.1)`; then `n_x = 0`
and if one is in case 2°, one has `n_{x'} = 0`; if one is in case 3°, one has `Z_x = 0` since `Supp(Z) ⊂ T`, so again
`n_{x'} = 0`. It remains to consider the case where one is at once in case 2° and in case 3°; then, since
`dim(𝒪_{X,x}) = 1`, `𝒪_{X,x}` is a discrete valuation ring; if `t` is a uniformizer of this ring, the divisor
corresponding to `Z_x` is `div(t^{n_x})` in `Div(𝒪_{X,x})`, and its image in `Div(𝒪_{X',x'})` is the divisor of
`t'^{n_x}`, where `t'` is the (regular) element of `𝒪_{X',x'}` image of `t`. One may evidently restrict to the case
where `n_x = 1`, and then the definition `(21.6.5.1)` shows that the image of `Z_x` under `(21.10.1.1)` is the number
`λ_{x'}`, which completes the proof of A).

Let us now prove B). Set `T_0 = Supp(Z) ⊂ T`, `T'_0 = f⁻¹(T_0)`; it suffices to prove that the relation `n_{x'} ≠ 0`
implies that `x'` belongs to the set of maximal points of `T'_0`, the latter being locally finite in `X'`. It is
immediate that one necessarily has `x' ∈ T'_0`; if `x'` were not maximal in the closed set `T'_0`, there would exist a
generization `y'` of `x'` in `T'_0`, distinct from `x'`, and since `x' ∈ X'^{(1)}`, `y'` would necessarily

<!-- original page 291 -->

be a maximal point of `X'`; consequently `y = f(y')` would be a maximal point of `X` by hypothesis; but this is absurd
since `y ∈ T_0` and `T_0` is purely of codimension `1` in `X`.

**(21.10.3).** One can now set

```text
                         f^*(Z) = ∑_{x' ∈ X'^{(1)}} n_{x'} · {x'},
```

the sum on the right-hand side making sense in virtue of what was proved in `(21.10.2)`; one says that the
1-codimensional cycle `f^*(Z)` is the *inverse image* of `Z` under `f`. It is immediate that the map `f^*` thus defined
is a homomorphism of ordered groups. Moreover, if `U` is an open of `X`, `V` an open of `X'` such that `f(V) ⊂ U`, and
`f' : V → U` the restriction of `f`, it follows at once from the definitions that one has

```text
  (21.10.3.1)            f'^*(Z | U) = f^*(Z) | V.
```

Denote by `Γ_T(𝔍^1_X)` the largest subsheaf of commutative groups of `𝔍^1_X` with support contained in `T`; it follows
from relation `(21.10.3.1)` that the maps `Γ(U, Γ_T(𝔍^1_X)) → Γ(V, 𝔍^1_{X'})` just defined determine a homomorphism of
sheaves of ordered commutative groups on `X'`

```text
                         ψ^*(Γ_T(𝔍^1_X)) → 𝔍^1_{X'}
```

where `ψ` is the continuous map underlying the morphism `f`.

**Proposition (21.10.4).**

<!-- label: IV.21.10.4 -->

*Assume the conditions of `(21.10.1)` are verified. Then, for every divisor `D` on `X` such that `Supp(D) ⊂ T` and that
`f^*(D)` is defined `(21.4.2)`, one has*

```text
  (21.10.4.1)            cyc(f^*(D)) = f^*(cyc(D)).
```

The question being local on `X`, one may restrict to the case where `X = Spec(A)` is affine, `D = div(t)`, `t` a regular
non-invertible element of `A`, and where the subprescheme `Y(D)` `(21.2.12)` has a single maximal point `y`, so that
`cyc(D) = n_y · {y}`, where `n_y` is the length of `𝒪_{X,y} / t 𝒪_{X,y}` `(21.6.5.1)`. One saw in the proof of
`(21.10.2, B)` that the points `x' ∈ X'` such that `mult_{x'}(f^*(cyc(D))) ≠ 0` are maximal points of `f⁻¹({y})`. If the
point `x'` is in case 3° of `(21.10.1)`, the equality of the multiplicities at `x'` of the two members of `(21.10.4.1)`
follows from the definition of `n_{x'}` by means of the homomorphism `(21.10.1.1)`. Suppose on the contrary that `x'`
is in case 2° of `(21.10.1)`, and let `x = f(x')`; since `x ∈ X^{(1)} ∩ {y}`, one necessarily has `x = y`. Let us remark
now that `f^*(D) = div(t')`, where `t'` is the image of `t` in `Γ(X', 𝒪_{X'})`, and `Y(f^*(D)) = f⁻¹(Y(D))`; the
multiplicity of `f^*(D)` at the point `x'` is therefore the length `n_{x'}` of the `𝒪_{X',x'}`-module
`𝒪_{X',x'} / t' 𝒪_{X',x'}`; since
`𝒪_{X',x'} / t' 𝒪_{X',x'} = (𝒪_{X,y} / t 𝒪_{X,y}) ⊗_{𝒪_{X,y}} 𝒪_{X',x'}`, it follows from `(4.7.1)` that one has
`n_{x'} = λ_{x'} n_y`, so the multiplicities at `x'` of the two members of `(21.10.4.1)` are again equal, which
completes the proof.

**(21.10.5).** Suppose now that `f : X' → X` is a morphism of locally Noetherian preschemes, sending every maximal
point of `X'` to a maximal point of `X`, and suppose in addition that for every rare closed part `T` of `X`, `f`
verifies the conditions

<!-- original page 292 -->

of `(21.10.1)`; this means again that for every `x' ∈ X'^{(1)}`, either `x = f(x')` is a maximal point of `X`, or `x'`
verifies one of conditions (ii), (iii) of `(21.10.1)`. If one takes into account that every 1-codimensional cycle has
rare support in `X`, one sees that `f^*(Z)` is defined for every 1-codimensional cycle `Z` on `X`; in virtue of
`(21.10.3.1)`, one has thus defined a homomorphism of sheaves of ordered commutative groups

```text
                         ψ^*(𝔍^1_X) → 𝔍^1_{X'}.
```

If, moreover, for every divisor `D` on `X`, `f^*(D)` is defined `(21.4.5)`, the fact that the support of `D` is rare in
`X` `(21.6.6)` entails that `(21.10.4)` is applicable, and one therefore has the formula `(21.10.4.1)` for every
divisor `D` on `X`. In particular:

**Proposition (21.10.6).**

<!-- label: IV.21.10.6 -->

*Let `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` a flat morphism. Then `f^*(Z)` is defined for every
1-codimensional cycle `Z` on `X`, `f^*(D)` is defined for every divisor `D` on `X`, and one has relation
`(21.10.4.1)`.*

Indeed, if `x' ∈ X'^{(1)}` is such that `x = f(x')` is not maximal, it follows from `(6.1.1)` that one necessarily has
`x ∈ X^{(1)}`, so one is in case (ii) of `(21.10.1)`. One may therefore apply `(21.10.5)`, taking account of `(21.4.5)`
and `(2.3.4)`.

**Remark (21.10.7).**

<!-- label: IV.21.10.7 -->

The existence of `f^*(Z)` for every 1-codimensional cycle `Z` on `X` already follows from the hypothesis that `f` is
flat at the points `x'` of `X'` of codimension `≤ 1` in `X'` (i.e. such that `dim(𝒪_{X',x'}) ≤ 1`); indeed, for every
maximal point `x' ∈ X'`, it follows from `(6.1.1)` that `x = f(x')` is a maximal point of `X` since
`dim(𝒪_{X,x}) ≤ dim(𝒪_{X',x'}) = 0`. Similarly, if `x' ∈ X'^{(1)}`, `x = f(x')` is maximal or belongs to `X^{(1)}` by
`(6.1.1)`; one can therefore again apply `(21.10.5)`.

**Proposition (21.10.8).**

<!-- label: IV.21.10.8 -->

*Let `X`, `X'`, `X''` be three locally Noetherian preschemes, `f : X' → X`, `g : X'' → X'` two morphisms; assume that
`f` (resp. `g`) is flat at every point of codimension `≤ 1` in `X'` (resp. `X''`). Then `f ∘ g` is flat at every point
of codimension `≤ 1` in `X''` and for every 1-codimensional cycle `Z` on `X`, one has `(f ∘ g)^*(Z) = g^*(f^*(Z))`.*

The first assertion follows from `(6.1.1)` and `(2.1.6)`. The second results from the fact that `f` (resp. `g`, resp.
`f ∘ g`) sends maximal points of `X'` (resp. `X''`, resp. `X''`) to maximal points of `X` (resp. `X'`, resp. `X`), and
that, if `x'' ∈ X''^{(1)}` is such that `x' = g(x'') ∈ X'^{(1)}` and `x = f(x') ∈ X^{(1)}`, one has

```text
                  long(𝒪_{X'',x''} / 𝔪_x 𝒪_{X'',x''}) = long(𝒪_{X'',x''} / 𝔪_{x'} 𝒪_{X'',x''}) · long(𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}).
```

Indeed, setting `A = 𝒪_{X,x}`, `A' = 𝒪_{X',x'}`, `A'' = 𝒪_{X'',x''}`, `𝔪 = 𝔪_x`, `𝔪' = 𝔪_{x'}`, one has
`A'' / 𝔪 A'' = (A' / 𝔪 A') ⊗_{A'} A''`, and the formula

```text
                         long_{A''}(A'' / 𝔪 A'') = long_{A'}(A' / 𝔪 A') · long_{A''}(A'' / 𝔪' A'')
```

follows from `(4.7.1)` and from the flatness hypothesis of `A''` over `A'`.

**(21.10.9).** Let `X` be a locally Noetherian prescheme, `Λ` a commutative group, written additively and therefore
considered as a `ℤ`-module; one will denote again by `ℤ` and `Λ` the simple sheaves on `X` associated to the constant
presheaves equal respectively to `ℤ` and `Λ` `(0_I, 3.6)`. The sheaf of commutative groups `𝔍^1_X ⊗_ℤ Λ` is called the
*sheaf of germs of 1-codimensional cycles with coefficients in `Λ`*. If `Λ = ℚ`, one says that the sections of

<!-- original page 293 -->

`𝔍^1_X ⊗_ℤ ℚ` over `X` are the *1-codimensional cycles with rational coefficients*. Since the stalks of `𝔍^1_X` are
torsion-free `ℤ`-modules `(21.6.3)`, the canonical homomorphism `𝔍^1_X → 𝔍^1_X ⊗_ℤ ℚ` is injective, so 1-codimensional
cycles are identified with 1-codimensional cycles with rational coefficients.

**(21.10.10).** We are going to see that under certain conditions, one may broaden the definition of `f^*(Z)` given in
`(21.10.3)` for a 1-codimensional cycle `Z` on `X`, but on condition of taking for `f^*(Z)` a 1-codimensional cycle
with rational coefficients on `X'`. The more general case in which we place ourselves is that where `f` sends every
maximal point of `X'` to a maximal point of `X`, and where, at every point `x' ∈ X'^{(1)}`, one has one of conditions
(i), (ii), (iii) of `(21.10.1)` or a fourth condition (setting `x = f(x')`):

(iv) `x ∈ X^{(1)}`, `𝔪_x ∉ Ass(𝒪_{X,x})`, and moreover, if one sets `A = 𝒪̂_{X,x}`, `A' = 𝒪̂_{X',x'}`, and if `K`
denotes the total ring of fractions of `A`, then `A'` is a finite `A`-algebra and `K' = A' ⊗_A K` is a free `K`-module.

Let us denote then by `r_{x'}` the rank of the free `K`-module `K'`, by `q_{x'}` the degree of `k(x') = k(A')` over
`k(x) = k(A)`, and set `μ_{x'} = r_{x'} / q_{x'}`. For a 1-codimensional cycle with support contained in `T`, given by
`(21.10.1.1)`, and every `x' ∈ X'^{(1)}`, one defines `c_{x'} ∈ ℚ` as equal to the number `n_{x'} ∈ ℤ` when one is in
one of cases 1°, 2°, 3° of `(21.10.1)`; but there remains here a fourth possibility:

4° if `x'` verifies condition (iv) above, take `c_{x'} = μ_{x'} n_x ∈ ℚ`.

**(21.10.11).** It remains to prove that when condition 4° of `(21.10.10)` is verified simultaneously with one of
conditions 1°, 2°, 3° of `(21.10.1)`, one has `n_{x'} = c_{x'}`. This is evident if `x ∉ T` since then `n_x = 0`. To
study the two other cases, note that `𝔪_x 𝒪_{X',x'}` is closed for the `𝔪_{x'}`-preadic topology, so the completion of
`𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}` for the latter topology is `A' / 𝔪_x A'`. If one is at once in case 2° and case 4°,
`𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}` is discrete for the `𝔪_{x'}`-preadic topology, so isomorphic to `A' / 𝔪_x A'`. Since `A'`
is a finite and flat `A`-algebra `(0_III, 10.2.3)`, it is a free `A`-module `(0_III, 10.1.3)`, and the rank of
`A' / 𝔪_x A'` over `A / 𝔪_x A = k(x)` is equal to the rank of `A'` over `A`, hence also to that of `K'` over `K`. On the
other hand, this rank is also equal to the product of the length `λ_{x'}` of `𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}` (as
`𝒪_{X',x'}`-module, or as `k(x')`-module) by the rank `[k(x') : k(x)] = q_{x'}`, which proves the relation
`μ_{x'} = r_{x'} / q_{x'} = λ_{x'}` in this case.

Assume finally that one is at once in case 3° and case 4°. Then, since `dim(𝒪_{X,x}) = 1`, `𝒪_{X,x}` is a discrete
valuation ring, hence regular. On the other hand, `𝒪_{X',x'}` is of dimension `1`, and since `𝔪_x ∉ Ass(𝒪_{X',x'})`,
`𝒪_{X',x'}` is a Cohen-Macaulay ring `(0, 16.4.6)`; finally, since `A'` is an `A`-module of finite type, `A' / 𝔪_x A'`
is a `k(x)`-vector space of finite rank; since `𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'}` is contained in `A' / 𝔪_x A'`, it is also a
`k(x)`-vector space of finite rank, hence an Artinian ring. Applying `(6.1.5)` then shows that `𝒪_{X',x'}` is a flat
`𝒪_{X,x}`-module, so one is also in case 2°, and one concludes by what was seen above.

This being so, in the case under consideration, one will set

```text
                         f^*(Z) = ∑_{x' ∈ X'^{(1)}} c_{x'} · {x'}
```

<!-- original page 294 -->

which is therefore a 1-codimensional cycle on `X'` with rational coefficients. One has again defined in this way a
homomorphism `f^*` of ordered groups, satisfying `(21.10.3.1)`, and consequently a homomorphism of sheaves of
commutative groups

```text
                         ψ^*(Γ_T(𝔍^1_X)) → 𝔍^1_{X'} ⊗_ℤ ℚ.
```

When `f` verifies the preceding conditions for every closed part `T` rare in `X`, that is, when for every
`x' ∈ X'^{(1)}`, either `x = f(x')` is a maximal point of `X`, or `x'` verifies one of conditions (ii), (iii) or (iv),
`f^*(Z)` is then defined for every 1-codimensional cycle `Z` on `X`, and one has defined a homomorphism of sheaves of
ordered commutative groups

```text
                         ψ^*(𝔍^1_X) → 𝔍^1_{X'} ⊗_ℤ ℚ
```

whence, by tensorization, a homomorphism of sheaves of ordered `ℚ`-vector spaces

```text
  (21.10.11.1)           ψ^*(𝔍^1_X ⊗_ℤ ℚ) → 𝔍^1_{X'} ⊗_ℤ ℚ.
```

**Remark (21.10.12).**

<!-- label: IV.21.10.12 -->

When one is in the situation of `(21.10.10)`, one may effectively, for 1-codimensional cycles `Z` on `X`, have for
`f^*(Z)` 1-codimensional cycles with *non-integral* coefficients; in other words, the numbers `μ_{x'}` may be non-
integers. One has an example by taking the complete integral ring `A` of `(6.15.11, (ii))` and its integral closure
`A'`: the closed point `x'` of `Spec(A')` verifies condition (iv) of `(21.10.10)` and one has `μ_{x'} = 1/2`.

**Lemma (21.10.13).**

<!-- label: IV.21.10.13 -->

*Let `A` be a Noetherian local ring of dimension `1`, `t` a regular element of `A` belonging to the maximal ideal `𝔪`
(which implies that `𝔪 ∉ Ass(A)`).*

*(i) For every `A`-module `M` of finite type, the kernel `N_t(M)` and cokernel `P_t(M)` of the homothety `t_M : M → M`
of ratio `t` are of finite length. One sets `d_t(M) = long P_t(M) − long N_t(M)`.*

*(ii) If `0 → M' → M → M'' → 0` is an exact sequence of `A`-modules of finite type, one has
`d_t(M) = d_t(M') + d_t(M'')`.*

*(iii) One has `d_t(M) ≥ 0` for every `A`-module `M` of finite type; for `d_t(M) = 0` to hold, it is necessary and
sufficient that `M` be of finite length.*

*(iv) If `K` is the total ring of fractions of `A` and if `M ⊗_A K` is a free `K`-module of rank `n`, one has
`d_t(M) = n · d_t(A) = n · long(A / tA)`.*

*(v) If `M` verifies the hypotheses of (iv) and moreover `t` is `M`-regular, one has `long(M / tM) = n · long(A / tA)`.*

(i) `Spec(A)` consists of the point `𝔪` and the minimal prime ideals `𝔭_i`; since by hypothesis `t ∉ 𝔭_i` for every `i`
(Bourbaki, _Alg. comm._, chap. IV, §1, n° 1, cor. 3 of prop. 2), the image of `t` in each of the `A_{𝔭_i}` is
invertible, and the supports of the `A`-modules of finite type `N_t(M)` and `P_t(M)` are therefore empty or reduced to
`𝔪`; one concludes `(0, 16.1.10)` that these modules are of finite length.

(ii) Since `t` is regular, one has an exact sequence

```text
                              t_A
                         0 → A ─→ A → A / tA → 0
```

<!-- original page 295 -->

and since `Tor_i^A(M, A) = 0` for `i ≥ 1`, the exact sequence of `Tor` gives on the one hand the exact sequence

```text
                                                          t_M
                         0 → Tor_1^A(M, A / tA) → M ─→ M → M / tM → 0
```

and on the other, for `i ≥ 2`,

```text
                         0 = Tor_i^A(M, A) → Tor_i^A(M, A / tA) → Tor_{i-1}^A(M, A) = 0
```

so one has `N_t(M) = Tor_1^A(M, A / tA)` and `Tor_i^A(M, A / tA) = 0` for `i ≥ 2`; the exact sequence of `Tor` gives an
exact sequence

```text
  0 → Tor_1^A(M', A / tA) → Tor_1^A(M, A / tA) → Tor_1^A(M'', A / tA) →
                              M' ⊗_A (A / tA) → M ⊗_A (A / tA) → M'' ⊗_A (A / tA) → 0
```

and this sequence is written, by the foregoing,

```text
  0 → N_t(M') → N_t(M) → N_t(M'') → P_t(M') → P_t(M) → P_t(M'') → 0
```

which proves (ii).

To prove (iii), note that there is a composition series `(M_k)` of `M` whose quotients `M_k / M_{k+1}` are isomorphic
to `A / 𝔪` or to one of the `A / 𝔭_i` (Bourbaki, _Alg. comm._, chap. IV, §1, n° 4, th. 1), and for `M` to be of finite
length, it is necessary and sufficient that all these quotients be isomorphic to `A / 𝔪`. Everything therefore reduces
(in virtue of (ii)) to proving that `d_t(A / 𝔪) = 0` and `d_t(A / 𝔭_i) > 0`. Now, the image of `t` in `A / 𝔪` being
`0`, one has `N_t(A / 𝔪) = A / 𝔪` and `P_t(A / 𝔪) = A / 𝔪`, whence the first assertion; on the other hand, the image of
`t` in `A / 𝔭_i` is regular, so `N_t(A / 𝔭_i) = 0` and `P_t(A / 𝔭_i) = A / (tA + 𝔭_i)`, which is not reduced to `0`,
whence the second assertion.

(iv) There is a basis of `M ⊗_A K` of the form `(x_j / s)_{1 ≤ j ≤ n}`, where `s` is a regular element of `A` and
`x_j ∈ M`. Consider the homomorphism `u : A^n → M` which sends the element `e_j` (`1 ≤ j ≤ n`) of the canonical basis
of `A^n` to `x_j`, and let us show that `Ker(u)` and `Coker(u)` are of finite length; indeed, for every `i`, the image
of `s` in `A_{𝔭_i}` is invertible, and since `K_{𝔭_i} = A_{𝔭_i}`, the images of the `x_j / s` in `M_{𝔭_i}` form a basis
of this `A_{𝔭_i}`-module; so `u_{𝔭_i} : A_{𝔭_i}^n → M_{𝔭_i}` is bijective. As in (i), one concludes that the supports
of `Ker(u)` and `Coker(u)` are contained in `{𝔪}`, so that these modules are of finite length. This being so, it
follows from (ii) and (iii) that one has `d_t(M) = d_t(A^n) = n · d_t(A) = n · long(A / tA)` since `t` is regular.

Finally, it is clear that (v) is at once deduced from (iv), since then `N_t(M) = 0`.

This lemma allows one to generalize `(21.10.4)`:

**Proposition (21.10.13).**

<!-- label: IV.21.10.13bis -->

*Assume that `f` verifies the conditions of `(21.10.10)`. Then, for every divisor `D` on `X` such that `Supp(D) ⊂ T`
and that `f^*(D)` is defined, one has*

```text
  (21.10.13.1)           cyc(f^*(D)) = f^*(cyc(D)).
```

Reasoning as in `(21.10.4)`, everything reduces to seeing (with the same notation) that if `x'` is in case 4° of
`(21.10.10)` and if `n_y` is the length of `𝒪_{X,y} / t 𝒪_{X,y}`, then the

<!-- original page 296 -->

length `n_{x'}` of `𝒪_{X',x'} / t' 𝒪_{X',x'}` is equal to `μ_{x'} n_y`, `μ_{x'}` being the rational number defined in
`(21.10.10)`. Since `𝒪_{X',x'} / t' 𝒪_{X',x'}` is of finite length, it has the same length as its `𝔪_{x'}`-preadic
completion `A' / t' A'`, which one may also write `A' / t_y A'`; moreover, since `t'` is regular by hypothesis in
`𝒪_{X',x'}`, `t_y` is also regular in `A'` by flatness `(0_I, 6.3.4)`, and when `A'` is considered as `A`-module, one
may also say that `t` is `A'`-regular. Since `A` is of dimension `1` and `A'` is an `A`-module of finite type such that
`A' ⊗_A K` is a free `K`-module of rank `r_{x'}`, one may apply `(21.10.13, (v))` to `M = A'` and to `t`, and the length
of `A' / t_y A'` as `K`-module is therefore `r_{x'} n_y`. Since `k(x')` is a `k(x)`-vector space of rank `q_{x'}`, the
length of `A' / t' A'` as `A'`-module is therefore `r_{x'} n_y / q_{x'} = μ_{x'} n_y`, which completes the proof.

**(21.10.14).** Let now `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` a morphism having the *two*
following properties:

a) `f` is finite;

b) the image under `f` of every maximal point of `X'` is a maximal point of `X`.

For every `x ∈ X^{(1)}`, the points `x' ∈ f⁻¹(x)` all belong to `X'^{(1)}`, as follows from hypothesis b) and the
inequality `(0, 16.3.9.1)`, the fibre `f⁻¹(x)` being discrete. Let then

```text
                         Z' = ∑_{x' ∈ X'^{(1)}} n_{x'} · {x'}
```

be a 1-codimensional cycle on `X'`. For every `x ∈ X^{(1)}`, let us define an integer `n_x` by the formula

```text
                         n_x = ∑_{x' ∈ f⁻¹(x)} n_{x'} · [k(x') : k(x)]
```

which makes sense, the points of `f⁻¹(x)` being finite in number and `k(x')` being a field of finite degree over
`k(x)` `(I, 6.4.4)`. Moreover, the set of `x ∈ X^{(1)}` such that `n_x ≠ 0` is locally finite in `X`, since it is
contained in the image under `f` of the set of `x' ∈ X'^{(1)}` such that `n_{x'} ≠ 0`, and the conclusion follows from
the fact that the morphism `f` is quasi-compact. One may thus define a 1-codimensional cycle on `X` by setting

```text
  (21.10.14.1)           f_*(Z') = ∑_{x ∈ X^{(1)}} n_x · {x}
```

and one says that `f_*(Z')` is the *direct image* of `Z'` under `f`. It is clear that the map
`f_* : 𝔍^1(X') → 𝔍^1(X)` thus defined is a homomorphism of ordered groups. Moreover, if `U` is an open of `X`,
`f_U : f⁻¹(U) → U` the restriction of `f`, it follows at once from the definitions that one has

```text
  (21.10.14.2)           (f_U)_*(Z' | f⁻¹(U)) = f_*(Z') | U
```

so, denoting by `ψ` the continuous map underlying the morphism `f`, the maps
`Γ(f⁻¹(U), 𝔍^1_{X'}) → Γ(U, 𝔍^1_X)` just defined determine a homomorphism of sheaves of ordered commutative groups on
`X`

```text
                         ψ_*(𝔍^1_{X'}) → 𝔍^1_X.
```

<!-- original page 297 -->

**Proposition (21.10.15).**

<!-- label: IV.21.10.15 -->

*Let `X`, `X'`, `X''` be three locally Noetherian preschemes, `f : X' → X`, `g : X'' → X'` two morphisms verifying
conditions a) and b) of `(21.10.14)`. Then `f ∘ g` verifies the same conditions, and for every 1-codimensional cycle
`Z''` on `X''`, one has `(f ∘ g)_*(Z'') = f_*(g_*(Z''))`.*

This follows at once from the definitions.

**Proposition (21.10.16).**

<!-- label: IV.21.10.16 -->

*Let `X`, `X'`, `X_1` be three locally Noetherian preschemes, `f : X' → X` a morphism verifying conditions a) and b)
of `(21.10.14)`, `g : X_1 → X` a flat morphism. Set `X'_1 = X' ×_X X_1` (so that `X'_1` is locally Noetherian) and note
`f_1 : X'_1 → X_1` and `g_1 : X'_1 → X'` the canonical projections. Then `f_1` verifies conditions a) and b) of
`(21.10.14)`, and for every 1-codimensional cycle `Z'` on `X'`, one has*

```text
  (21.10.16.1)           g^*(f_*(Z')) = (f_1)_*(g_1^*(Z')).
```

It is clear that `f_1` is finite, and it verifies condition b) of `(21.10.14)` by virtue of `(2.3.7)`. To prove
`(21.10.16.1)`, one is at once reduced to the case where `X`, `X'` and `X_1` are spectra of Noetherian local rings of
dimension `1`, `A`, `A'` and `A_1`, with `A'` a finite `A`-module and `A_1` a flat `A`-module. Denoting by `x`, `x'`
and `x_1` the closed points of `X`, `X'` and `X_1` respectively, it is a matter of seeing that one has

```text
  (21.10.16.2)           ∑_{x'_1} λ_{x'_1}[k(x'_1) : k(x_1)] = λ_{x'}[k(x') : k(x)]
```

where `x'_1` ranges over the set of closed points of `X'_1` (i.e. the set of points lying above both `x'` and `x_1`)
and where `λ_{x'} = long(𝒪_{X',x'} / 𝔪_x 𝒪_{X',x'})` and `λ_{x_1} = long(A_1 / 𝔪_x A_1)`. Since one has

```text
                         [k(x'_1) : k(x_1)] · [k(x_1) : k(x)] = [k(x'_1) : k(x')] · [k(x') : k(x)]
```

the left-hand side of `(21.10.16.2)` is also written

```text
                         ([k(x') : k(x)] / [k(x_1) : k(x)]) · long_{A'}(A'_1 / 𝔪_{x'} A'_1) = long_{A_1}(A'_1 / 𝔪_x A'_1)
```

where one has set `A'_1 = A' ⊗_A A_1`. One therefore has `A'_1 / 𝔪_x A'_1 = (A' / 𝔪_x A') ⊗_A A_1`, and since `A_1` is
a flat `A`-module, one has by `(4.7.1)`

```text
                         long_{A_1}(A'_1 / 𝔪_x A'_1) = long_A(A' / 𝔪_x A') · long_{A_1}(A_1 / 𝔪 A_1)
                                                    = [k(x') : k(x)] · λ_{x_1}
```

which completes the proof.

**Proposition (21.10.17).**

<!-- label: IV.21.10.17 -->

*Let `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` a finite locally free morphism. Then `f` verifies
condition b) of `(21.10.14)`, and for every divisor `D'` on `X'`, one has*

```text
  (21.10.17.1)           f_*(cyc(D')) = cyc(f_*(D')).
```

Since `f` is flat and finite, condition b) of `(21.10.14)` and the relation `f(X'^{(1)}) ⊂ X^{(1)}` follow from
`(6.1.1)`. The definition `(21.10.14.1)` shows that one may reduce to the case where `X = Spec(A) = Spec(𝒪_{X,x})` for
an `x ∈ X^{(1)}`; then `X' = Spec(A')`, where `A'` is an

<!-- original page 298 -->

`A`-algebra which is a *free* `A`-module of finite rank; moreover, one may assume that `D' = div(t')`, where `t'` is a
regular element of `A'`; one then has `f_*(D') = div(t)`, where `t = N_{A'/A}(t')` is a regular element of `A`
`(21.5.2)`. One may restrict to the case where `t'` is not invertible in `A'`, which is equivalent to `t` not being
invertible in `A`; the ring `A / tA` is then of finite length and `≠ 0`, and `A' / t' A'` is a direct sum of Artinian
local rings `A'_i` (`1 ≤ i ≤ r`), the residue field of `A'_i` being `k(x'_i)`, where `x'_i` (`1 ≤ i ≤ r`) are the
points of `X'` above `x`. If `t'_i` (`1 ≤ i ≤ r`) is the image of `t'` in `A'_i`, `A' / t' A'` is the direct sum of the
`A'_i / t'_i A'_i`; since the product `long_{A'_i}(A'_i / t'_i A'_i) · [k(x'_i) : k(x)]` equals
`long_A(A'_i / t'_i A'_i)`, one sees that the multiplicity at the point `x` of the left-hand side of `(21.10.17.1)` is
`long_A(A' / t' A')`, so that the formula to prove reduces to

```text
  (21.10.17.2)           long_A(A' / t' A') = long_A(A / tA).
```

This relation follows from the more general following lemma:

**Lemma (21.10.17.3).**

<!-- label: IV.21.10.17.3 -->

*Let `A` be a Noetherian local ring of dimension `1`, `M` a free `A`-module of finite rank, `u` an injective
endomorphism of `M`. Then one has*

```text
  (21.10.17.4)           long_A(Coker u) = long_A(A / (det u) A).
```

Let us distinguish several cases.

I) `A` is a discrete valuation ring. Indeed, let `π` be a uniformizer of `A`, and remark that `long_A(A / π^k A) = k`;
if `n` is the rank of `M` and `π^{m_i}` (`1 ≤ i ≤ n`) are the invariant factors of `u`, `Coker(u)` is the direct sum of
the `A`-modules `A / π^{m_i} A`, so has length `m = ∑_{i=1}^n m_i`, and `det(u)` is the product of an invertible
element and `π^m`, whence the conclusion in this case (Bourbaki, _Alg._, chap. VII, §4, n° 5, cor. 1 of prop. 4).

II) `A` is a complete integral ring (of dimension `1`). One knows then `(0, 19.8.8, (ii))` that there is a subring `B`
of `A` which is a discrete valuation ring, such that `B → A` is a local homomorphism making `A` a `B`-module of finite
type; since this `B`-module is evidently torsion-free, it is free (Bourbaki, _Alg. comm._, chap. VI, §3, n° 6, lemma
1). Denote by `M'` the set `M` endowed with its (free) `B`-module structure, by `u'` the endomorphism `u` regarded as a
`B`-endomorphism. It follows from I) that one has

```text
  (21.10.17.5)           long_B(Coker u') = long_B(B / (det u') B).
```

But one has (Bourbaki, _Alg._, chap. VIII, §12, n° 2, prop. 7)

```text
                         det u' = N_{A/B}(det u),
```

hence, applying `(21.10.17.4)` to the homothety `x ↦ (det u) x` of the free `B`-module `A`, it comes

```text
                         long_B(B / (det u') B) = long_B(A / (det u) A),
```

whence, substituting in `(21.10.17.5)` and dividing by `[k(A) : k(B)]`, the length of the `B`-module `k(A)`, one
obtains `(21.10.17.4)` in the case envisaged.

<!-- original page 299 -->

III) `A` is a complete ring. Note that one may suppose in addition that `𝔪 ∉ Ass(A)`; indeed, since `det(u)` is a
regular element of `A`, if one had `𝔪 ∈ Ass(A)`, one would deduce `det(u) ∉ 𝔪`, so `det(u)` would be invertible, `u`
an automorphism of `M`, and the formula `(21.10.17.4)` becomes then trivial, both members being zero.

In what follows, for an endomorphism `v` of a module `N` over a ring `R`, such that `Ker v` and `Coker v` be of finite
length, one will set

```text
                         χ(N, v) = long_R(Ker(v)) − long_R(Coker(v)).
```

One will note that the hypothesis on `v` amounts to saying that the complex

```text
                                            v
                         K^0 : 0 → N ──→ N → 0
```

has its cohomology modules of finite length and that `χ(N, v) = χ(H^0(K^0))` `(0_III, 11.10)`. One deduces that if
`N'`, `N`, `N''` are three `R`-modules, if one has a commutative diagram

```text
                                 r        s
                         0 → N' ─→ N ─→ N'' → 0
                              │     │     │
                              │v'   │v    │v''
                              ↓     ↓     ↓
                         0 → N' ─→ N ─→ N'' → 0
                                 r        s
```

whose rows are exact, and if two of the three numbers `χ(N, v)`, `χ(N', v')` and `χ(N'', v'')` are defined, then it is
the same of the third and one has

```text
  (21.10.17.6)           χ(N, v) = χ(N', v') + χ(N'', v'').
```

This follows at once from the exact cohomology sequence.

Finally, if `N` is an `R`-module of finite length, one has `χ(N, v) = 0`.

With these notations, one has the following lemma:

**Lemma (21.10.17.7).**

<!-- label: IV.21.10.17.7 -->

*Let `A` be a Noetherian local ring of dimension `1` whose maximal ideal `𝔪` is such that `𝔪 ∉ Ass(A)`; let `𝔭_i`
(`1 ≤ i ≤ n`) be the minimal prime ideals of `A`. Let `M` be a free `A`-module of finite type, `u` an endomorphism of
`M` such that `χ(M, u)` is defined; for each `i`, set `M_i = M ⊗_A (A / 𝔭_i)` and let `u_i` be the endomorphism
`u ⊗ 1_{A/𝔭_i}` of `M_i`; then, if `χ(M_i, u_i)` is defined for each `i`, one has*

```text
  (21.10.17.8)           χ(M, u) = ∑_{i=1}^n long(A_{𝔭_i}) · χ(M_i, u_i).
```

Since `𝔪 ∉ Ass(A)`, one has a unique reduced primary decomposition `(0) = ⋂_{1 ≤ i ≤ n} 𝔮_i`, where the ideal `𝔮_i`
is `𝔭_i`-primary for `1 ≤ i ≤ n`. If one sets `M'_i = M ⊗_A (A / 𝔮_i)`, one then has an exact sequence

```text
                         0 → M → ⨁_i M'_i → M'' → 0
```

of `A`-modules, where `M''` is of finite length: indeed, localizing the preceding exact sequence at each of the `𝔭_i`,
one obtains `M''_{𝔭_i} = 0`, since `(𝔮_i)_{𝔭_i} = 0` and `(𝔮_j)_{𝔭_i} = A_{𝔭_i}` for `j ≠ i` (Bourbaki, _Alg. comm._,
chap. IV, §2, n° 4, prop. 6), so `(M'_i)_{𝔭_i} = M_{𝔭_i}` and `(M'_j)_{𝔭_i} = 0`;

<!-- original page 300 -->

the support of `M''` being therefore reduced to `𝔪`, `M''` is of finite length `(0, 16.1.10)`. If one sets
`u'_i = u ⊗ 1_{A/𝔮_i}`, and if `u''` is the endomorphism of `M''` deduced from `⨁_i u'_i` by passage to quotients, one
deduces from `(21.10.17.6)` that `χ(M, u) + χ(M'', u'') = ∑_i χ(M'_i, u'_i)`, and since `M''` is of finite length,
`χ(M'', u'') = 0`. To prove `(21.10.17.8)`, one may therefore reduce to the case where `n = 1`. One will then denote
by `𝔭` the unique minimal prime ideal, which is the nilradical of `A`; if `A_0 = A / 𝔭`, `M_0 = M ⊗_A A_0`,
`u_0 = u ⊗ 1_{A_0}`, it is a matter of proving that if `χ(M_0, u_0)` is defined, one has

```text
  (21.10.17.9)           χ(M, u) = long A_𝔭 · χ(M_0, u_0).
```

Let `𝔫_j` (`0 ≤ j ≤ r`) be the "`j`-th symbolic power" of `𝔭`, inverse image in `A` of the ideal `(𝔭 A_𝔭)^j` of
`A_𝔭` (`1 ≤ j ≤ r`), with `𝔫_0 = A` and `𝔫_r = 0`; set

```text
                         M_j = 𝔫_j M / 𝔫_{j+1} M       (0 ≤ j ≤ r − 1),
```

and denote by `v_j` the endomorphism of `M_j` deduced from `u` by restriction to `𝔫_j M` and passage to quotients. We
shall first show that each of the numbers `χ(M_j, v_j)` is defined and that one has

```text
  (21.10.17.10)          χ(M, u) = ∑_j χ(M_j, v_j).
```

The first assertion will entail the second, by applying `(21.10.17.6)` to each of the exact sequences

```text
                         0 → 𝔫_j M / 𝔫_{j+1} M → M / 𝔫_{j+1} M → M / 𝔫_j M → 0.
```

To prove the first assertion, one notes that if `m` is the rank of the free `A`-module `M`, `M_j` is isomorphic to
`(𝔫_j / 𝔫_{j+1})^m`, or also (since `𝔭` annihilates each of the quotients `𝔫_j / 𝔫_{j+1}`), `M_j` is an `A_0`-module
isomorphic to `M_0 ⊗_{A_0} (𝔫_j / 𝔫_{j+1})`. Denote by `l_j` the rank of the `A_0`-module `𝔫_j / 𝔫_{j+1}`; since the
field of fractions `K_0` of `A_0` is the residue field of `A_𝔭`, `l_j` is also the length of the `A_𝔭`-module
`(𝔭 A_𝔭)^j / (𝔭 A_𝔭)^{j+1}`. There is a system of generators of the `A_0`-module `M_j` which contains a basis of
`M_j ⊗_{A_0} K_0`; so there is an `A_0`-homomorphism

```text
                         w_j : M_0^{l_j} → M_j
```

whose localization at the ideal `(0)` of `A_0` is an isomorphism, so that the supports of `Ker(w_j)` and of
`Coker(w_j)` are reduced to the maximal ideal `𝔪 / 𝔭` of `A_0`; `Ker(w_j)` and `Coker(w_j)` are therefore
`A_0`-modules of finite length `(0, 16.1.10)`. Since by hypothesis `χ(M_0, u_0)` is defined, the same holds for
`χ(M_0^{l_j}, u_0^{l_j}) = l_j χ(M_0, u_0)`, and in virtue of `(21.10.17.6)` and of the fact that `Ker(w_j)` and
`Coker(w_j)` are of finite length, one sees that `χ(M_j, v_j)` is defined and equal to `l_j χ(M_0, u_0)`; relation
`(21.10.17.10)` then gives

```text
                         χ(M, u) = (∑_j l_j) χ(M_0, u_0),
```

and in virtue of a previous remark, `∑_j l_j` is none other than the length of `A_𝔭`, which completes the proof of
the lemma `(21.10.17.7)`.

<!-- original page 301 -->

To apply this lemma when `A` is a complete ring and `𝔪 ∉ Ass(A)`, one observes that if `u` is injective, the same holds
for the `u_i` (with the notation of the lemma): indeed, `det u` is then a regular element of `A`, so does not belong to
any of the `𝔭_i`, and its image `det u_i` in `A / 𝔭_i` is consequently an element `≠ 0` of this integral ring, which
proves that `u_i` is injective. Since `Coker(u_i)` is image of `Coker(u)`, it is also of finite length and
`χ(M_i, u_i)` is therefore defined for every `i`; one has accordingly the formula `(21.10.17.8)`. On the other hand,
since `det(u)` is a regular element of `A`, it is contained in none of the `𝔭_i`; the ideal `(det u) A` is therefore
`𝔪`-primary and the quotient `A / (det u) A` of finite length. Applying the same reasoning as above to the injective
homothety `t : ξ ↦ (det u) ξ` of `A` and its images `t_i = det u_i` in the `A / 𝔭_i`, it comes

```text
                         χ(A, t) = ∑_i long(A_{𝔭_i}) · χ(A / 𝔭_i, t_i).
```

But the rings `A / 𝔭_i` are integral and complete, and applying the result of II) to each of them, one again obtains
relation `(21.10.17.4)` for `M` and `u`.

IV) General case. Set `A' = Â`, `M' = M ⊗_A A'`, `u' = u ⊗ 1_{A'}`; one has `det(u') = det(u)`, and by flatness,
`Coker(u') = (Coker(u))_{(A')}` and `A' / (det u') A' = (A / (det u) A)_{(A')}`; since the formula `(21.10.17.4)` is
true for `A'` and `u'` in virtue of III), it is also true for `A` and `u` in virtue of `(4.7.1)`.

This completes the proof of `(21.10.17)`.

**Proposition (21.10.18).**

<!-- label: IV.21.10.18 -->

*Let `X`, `X'` be two locally Noetherian preschemes, `f : X' → X` a finite morphism, sending every maximal point of
`X'` to a maximal point of `X`, and verifying for every `x' ∈ X'` one of conditions (ii), (iii), (iv) of `(21.10.10)`.
Assume in addition that there exists an integer `n` such that, for every maximal point `x` of `X`, `(f_*(𝒪_{X'}))_x` is
a free `𝒪_{X,x}`-module of rank `n`. Then, for every 1-codimensional cycle `Z` on `X`, one has*

```text
  (21.10.18.1)           f_*(f^*(Z)) = n · Z
```

*("projection formula").*

By virtue of the definitions, one is at once reduced to the case where `X` is the spectrum of a Noetherian local ring
`A` of dimension `1`, with closed point `x`, and where `Z = {x}`; set `X' = Spec(A')`, where `A'` is a finite
`A`-algebra, and, for every minimal prime ideal `𝔭_i` of `A`, `A'_{𝔭_i}` is a free `A_{𝔭_i}`-module of rank `n`. Let us
show that one may further restrict to the case where `A` is complete. Make in effect the base change `h : Y → X`, where
`Y = Spec(B)`, with `B = Â`, and set `Y' = X' ×_X Y = Spec(B ⊗_A A')` and `g = f_{(Y)} : Y' → Y`; the morphism `g` is
then finite, and since `h` is flat, the maximal points of `Y` lie above those of `X`; above each of the `𝔭_i`, there is
only a finite number of minimal ideals `𝔭_{ij}` of `B`, and `(B ⊗_A A')_{𝔭_{ij}}` is a free `B_{𝔭_{ij}}`-module of
rank `n`. Finally, if `f` verifies one of conditions (ii), (iii) or (iv) of `(21.10.10)` at each of the points `x'` of
`f⁻¹(x)`, `g` verifies the corresponding condition at the unique point `y'` of `g⁻¹(x')` above `x'` (denoting by `y` the
closed point of `Y`); this is immediate for conditions (ii) and (iv); for condition (iii), it implies that `A`

<!-- original page 302 -->

is a discrete valuation ring, so the same holds for `B`, and the condition `𝔪_{y'} ∉ Ass(𝒪_{Y',y'})` follows, by
flatness, from the condition `𝔪_{x'} ∉ Ass(𝒪_{X',x'})` `(3.3.1)`. The morphism `g` therefore verifies the same
conditions as `f`; if one proves the formula `(21.10.18.1)` for `g` and `{y}`, the same formula will be valid for `f`
and `{x}`, in virtue of `(21.10.16.1)`.

One may therefore assume that `A` is complete; then so is `A'`, which is thus the direct sum of complete local rings;
one may consequently restrict to the case where `A'` is a local ring, and it remains to verify `(21.10.18.1)` in each
of the cases (ii), (iii), (iv) for the closed point `x'` of `X'`. In case (ii), `A'` being a flat `A`-module of finite
type, is a free `A`-module `(0_III, 10.1.3)`, of rank `n` in virtue of the hypothesis. Now, one has by definition
`(21.10.1` and `21.10.3)` `f^*(Z) = λ_{x'} \cdot {x'}`, where `λ_{x'}` is the length of the `A'`-module
`A' / 𝔪_x A'`, then `f_*(f^*(Z)) = (λ_{x'} [k(x') : k(x)]) \cdot {x}`; but `λ_{x'} [k(x') : k(x)]` is the length of
`A' / 𝔪_x A' = A' ⊗_A k(x)` as `A`-module, or also its rank as `k(x)`-vector space, hence equals `n`.

In case (iii), `A` is a discrete valuation ring, hence regular, and the hypothesis `𝔪_{x'} ∉ Ass(𝒪_{X',x'})` entails
that `A'` is a Cohen-Macaulay ring `(0, 16.4.6)`; since `dim(A') = dim(A) = 1` and `A' / 𝔪_x A'` is an Artinian ring,
it follows from `(6.1.5)` that `A'` is a flat `A`-module, and one is reduced to case (ii).

In case (iv), if `K` is the total ring of fractions of `A`, `K' = A' ⊗_A K` is by hypothesis a free `K`-module of rank
`n` and by definition `(21.10.10)`, one has `f^*(Z) = (n / [k(x') : k(x)]) \cdot {x'}`, whence
`f_*(f^*(Z)) = n \cdot {x}`. Q.E.D.

One will note that the formula `(21.10.18.1)` is applicable in particular when the morphism `f` is finite and flat and
such that for every maximal point `x` of `X`, `(f_*(𝒪_{X'}))_x` is a free `𝒪_{X,x}`-module of rank `n`.

**Corollary (21.10.19).**

<!-- label: IV.21.10.19 -->

*Under the hypotheses of `(21.10.18)`, let `D` be a divisor on `X` such that `f^*(D)` is defined `(21.4.5)`; then one
has*

```text
  (21.10.19.1)           f_*(cyc(f^*(D))) = n · cyc(D).
```

This follows from `(21.10.18)` and `(21.10.13)`.

### 21.11. Factoriality of regular local rings

**Theorem (21.11.1) (Auslander-Buchsbaum).**

<!-- label: IV.21.11.1 -->

*A regular Noetherian local ring is factorial.*

The proof that follows is due to I. Kaplansky.

Let `A` be a regular Noetherian local ring of dimension `n`; we shall reason by induction on `n`. For `n = 0`, `A` is a
field, and for `n = 1`, a discrete valuation ring, hence principal (and a fortiori factorial). Suppose then `n ≥ 2` and
the theorem proved for regular rings of dimension `< n`. Set `X = Spec(A)`, denote by `a` the closed point of `X`, and
set `U = X − {a}`. At every point `y ∈ U`, one has `dim(𝒪_{X,y}) ≤ n − 1`, and since `A` is regular, the rings
`𝒪_{X,y}` are also regular `(0, 17.3.2)`, so the induction hypothesis entails that they are factorial. Moreover one has
`prof(A) = dim(A) ≥ 2` since `A` is regular, hence Cohen-Macaulay `(0, 17.1.3)`.

<!-- original page 303 -->

Using `(21.6.14)`, one is reduced to proving that `Pic(U) = 0`. Therefore consider an invertible `𝒪_U`-Module `ℒ`, and
prove that it is isomorphic to `𝒪_U`. It follows from `(I, 9.4.5)` that there exists a coherent `𝒪_X`-Module `ℱ` such
that `ℱ | U = ℒ`. Since `A` is regular, hence of finite cohomological dimension `(0, 17.3.1)`, there exists a finite
left resolution of `ℱ`:

```text
                         0 ← ℱ ← 𝒪_X^{n_1} ← 𝒪_X^{n_2} ← … ← 𝒪_X^{n_h} ← 0
```

`(0, 17.2.8` and `0, 17.2.2, (iii))`. By restriction to `U`, one therefore has a finite resolution

```text
  (21.11.1.1)            0 ← ℒ ← 𝒪_U^{n_1} ← 𝒪_U^{n_2} ← … ← 𝒪_U^{n_h} ← 0.
```

The theorem will then follow from the general considerations that follow. On a ringed space `X`, let `ℰ` be a locally
free `𝒪_X`-Module of finite rank; one will denote by `Λ^{max} ℰ` the invertible `𝒪_X`-Module which, in a neighbourhood
of each point of `X`, equals `Λ^p ℰ`, denoting by `p` the rank of `ℰ` in this neighbourhood (which may vary with the
connected component of `X`). With this notation, one has the

**Lemma (21.11.1.2).**

<!-- label: IV.21.11.1.2 -->

*Let `X` be a ringed space in local rings, and*

```text
                         0 ← ℰ_0 ← ℰ_1 ← … ← ℰ_h ← 0
```

*an exact sequence of `𝒪_X`-Modules locally free of finite rank; then the invertible `𝒪_X`-Module
`⨂_{0 ≤ i ≤ h} (Λ^{max} ℰ_i)^{⊗ (−1)^i}` is isomorphic to `𝒪_X`.*

Let us show how this lemma will allow one to conclude the proof of `(21.11.1)`. It suffices to note for this that, for
every integer `n`, `Λ^{max}(𝒪_X^n) = Λ^n 𝒪_X` is isomorphic to `𝒪_X`, as is `𝒪_X^{⊗ (−1)}`. Since on the other hand
`Λ^{max} ℒ = ℒ` for every invertible `𝒪_X`-Module `ℒ`, the lemma `(21.11.1.2)`, applied to the exact sequence
`(21.11.1.1)`, shows that `ℒ` is isomorphic to `𝒪_U`.

It remains to prove `(21.11.1.2)`; one proceeds by induction on `h`, the lemma being trivial for `h = 1`. For `h > 1`,
`𝒩 = Ker(u_0)` is an `𝒪_X`-Module locally free of finite rank `(0_I, 5.5.5)`, and one has the two exact sequences

```text
                         0 ← ℰ_0 ← ℰ_1 ← 𝒩 ← 0
                         0 ← 𝒩 ← ℰ_2 ← … ← ℰ_h ← 0
```

In virtue of the induction hypothesis, `(Λ^{max} 𝒩) ⊗ (⨂_{2 ≤ i ≤ h} (Λ^{max} ℰ_i)^{⊗ (−1)^{i−1}})` is isomorphic to
`𝒪_X`; it will therefore suffice to define a canonical isomorphism
`(Λ^{max} 𝒩) ⊗ (Λ^{max} ℰ_0) ⥲ Λ^{max} ℰ_1` to complete the proof. Now, there exists an open covering `(U_α)` of `X`
such that in every `U_α`, `ℰ_1 | U_α` is the direct sum of `𝒩 | U_α` and of an `𝒪_{U_α}`-Module locally free `ℳ_α`
`(0_I, 5.5.5)`, whence a canonical isomorphism `v_α : ℳ_α ⥲ ℰ_0 | U_α`. Since one has a canonical isomorphism

```text
                         r_α : (Λ^{max} 𝒩 | U_α) ⊗ (Λ^{max} ℳ_α) ⥲ (Λ^{max} ℰ_1) | U_α
```

one deduces from this, by means of `v_α`, an isomorphism

```text
                         u_α : (Λ^{max} 𝒩 | U_α) ⊗ (Λ^{max} ℰ_0 | U_α) ⥲ Λ^{max} ℰ_1 | U_α
```

<!-- original page 304 -->

and it is a matter of showing that `u_α` and `u_β` coincide in `U_α ∩ U_β` for any two indices `α`, `β`. Now, if `v'_α`
and `v'_β` are the restrictions to `U_α ∩ U_β` of `v_α` and `v_β` respectively, one has `v'_α = v'_β ∘ w_{βα}`, where
`w_{βα} : ℳ_α | (U_α ∩ U_β) ⥲ ℳ_β | (U_α ∩ U_β)` is the "projection parallel to `𝒩`" such that for every section
`s ∈ Γ(U_α ∩ U_β, ℳ_α)`, `w_{βα}(s) = s + t` with `t ∈ Γ(U_α ∩ U_β, 𝒩)`; the identity of `u_α` and `u_β` follows at
once from this fact and from the definition of the canonical isomorphism `r_α` (Bourbaki, _Alg._, chap. III, 3rd ed.).

<!-- original page 304 -->

### 21.12. Van der Waerden's purity theorem for the ramification locus of a birational morphism

**(21.12.1).** Let `X` and `U` be two preschemes, `f : U → X` a quasi-compact and quasi-separated morphism, so that
`f_*(𝒪_U)` is a quasi-coherent `𝒪_X`-Algebra `(1.7.4)`. We call **affine envelope** of the `X`-prescheme `U` the
`X`-prescheme affine over `X`

```text
                       U^∘ = Aff(U/X) = Spec(f_*(𝒪_U)) = Spec(𝒜(U))                  (II, 1.1.1).
```

If `f^∘ : U^∘ → X` is the structural morphism, one has therefore by definition

```text
                       𝒜(U^∘) = f^∘_*(𝒪_{U^∘}) = f_*(𝒪_U) = 𝒜(U),
```

and to the identity isomorphism of `f_*(𝒪_U)` there corresponds by `(II, 1.2.7)` a canonical `X`-morphism

<!-- label: IV.21.12.1 -->

```text
  (21.12.1.1)                          i_U : U → U^∘.
```

For `i_U` to be an isomorphism, it is evidently necessary and sufficient that the morphism `f : U → X` be affine.

For every `X`-prescheme `V` affine over `X`, the map `u ↦ u ∘ i_U` is a bijection

```text
                       Hom_X(U^∘, V) ⥲ Hom_X(U, V)
```

functorial in `V`: this results from the existence of the canonical bijections `Hom_X(U, V) ⥲ Hom_{𝒪_X}(𝒜(V), 𝒜(U))`
and `Hom_X(U^∘, V) ⥲ Hom_{𝒪_X}(𝒜(V), 𝒜(U^∘))` `(II, 1.2.7)`.

One can therefore say that `U^∘` represents the covariant functor `V ↦ Hom_X(U, V)` in the category of `X`-preschemes
affine over `X` `(0_III, 8.1.11)`. One deduces `(0_III, 8.1.7)` that, for `X` fixed, `U ↦ Aff(U/X)` is a covariant
functor from the category of quasi-compact and quasi-separated `X`-preschemes into the category of `X`-preschemes
affine over `X`; more precisely, if `U_1`, `U_2` are two quasi-compact and quasi-separated `X`-preschemes, to every
`X`-morphism `g : U_1 → U_2` there corresponds the unique `X`-morphism `g^∘ : U_1^∘ → U_2^∘` rendering the diagram

```text
                       U_1 ────────→ U_2
                        │             │
                  i_{U_1}│             │i_{U_2}
                        ↓             ↓
                       U_1^∘ ──g^∘──→ U_2^∘
```

commutative.

<!-- original page 305 -->

More generally, consider a commutative diagram

```text
                       U ──u──→ U'
                       │        │
                      f│        │f'
                       ↓        ↓
                       X ──v──→ X'
```

where the morphisms `f`, `f'` are quasi-compact and quasi-separated and the morphism `u` affine. Setting `h = u ∘ f`,
one has `h_*(𝒪_U) = u_*(f_*(𝒪_U)) = u_*(f^∘_*(𝒪_{U^∘}))` and `u ∘ f^∘` is an affine morphism; one has consequently
`U^∘ = Aff(U/X')` (relative to the morphism `h`), whence a unique `X'`-morphism `v^∘ : U^∘ → U'^∘` rendering the
diagram

```text
                       U ──u──→ U'
                       │        │
                  i_U  │        │i_{U'}
                       ↓        ↓
                       U^∘ ─v^∘→ U'^∘
```

commutative.

**Proposition (21.12.2).**

<!-- label: IV.21.12.2 -->

*Let `f : U → X` be a quasi-compact and quasi-separated morphism, `h : X' → X` a flat morphism; set
`U' = U ×_X X'`, `f' = f_{(X')} : U' → X'`. Then one has a canonical `X'`-isomorphism*

```text
  (21.12.2.1)                          Aff(U'/X') ⥲ Aff(U/X) ×_X X'.
```

Indeed, one has `Aff(U'/X') = Spec(f'_*(𝒪_{U'}))`, and `Aff(U/X) ×_X X' = Spec(h^*(f_*(𝒪_U)))` `(II, 1.5.1)`; the
isomorphism of the statement comes from the canonical isomorphism `h^*(f_*(𝒪_U)) ⥲ f'_*(𝒪_{U'})` `(2.3.1)`.

**Corollary (21.12.3).**

<!-- label: IV.21.12.3 -->

*For every quasi-compact and quasi-separated morphism `f : U → X` and every `x ∈ X`, one has, up to a canonical
isomorphism*

```text
  (21.12.3.1)                          U^∘ ×_X Spec(𝒪_{X,x}) = (U ×_X Spec(𝒪_{X,x}))^∘.
```

It also follows from `(21.12.2)` that one has, up to a canonical isomorphism, for every open `V` of `X`

<!-- label: IV.21.12.4 -->

```text
  (21.12.4)                            (f^{-1}(V))^∘ ≃ (f^∘)^{-1}(V).
```

**(21.12.5).** We shall consider in particular the case where `f : U → X` is an *open immersion*, so that `U` is
identified with a prescheme induced on an open of `X`. Since the morphism `f_*(𝒪_U) → 𝒪_U` is the identity, it follows
from `(21.12.4)` that the morphism `(f^∘)^{-1}(U) → U` restriction of `f^∘` is an isomorphism, `i_U : U → U^∘` being
therefore an *open immersion* permitting `U` to be identified with a prescheme induced on an open of `U^∘`.

More generally, for an open `V` of `X`, the restriction `(f^∘)^{-1}(V) → V` of `f^∘` is an isomorphism of
`(f^∘)^{-1}(V)` onto the prescheme induced on the open `V ∩ U` if and only if the open immersion `U ∩ V → V` is an
affine morphism. It is clear `(II, 1.2.1)`

<!-- original page 306 -->

that the union of these opens `V` is the largest of them, `U_1`, which contains `U`; by virtue of the foregoing, `U_1`
is also the largest open not meeting the set

```text
                       Daf(U/X) = f^∘(U^∘) − U
```

("affineness defect" of the open `U` relative to `X`, which is empty if and only if `U` is affine over `X`); in other
words, the closed set `Z = X − U_1` is the *closure* of the set `Daf(U/X)`.

Note that for every flat morphism `h : X' → X`, if one sets `U' = h^{-1}(U)`, one has

<!-- label: IV.21.12.5.1 -->

```text
  (21.12.5.1)                          Daf(U'/X') = h^{-1}(Daf(U/X))
```

as follows at once from `(21.12.2.1)` and `(I, 3.4.8)`. In particular, for every open `V` of `X`, one has

<!-- label: IV.21.12.5.2 -->

```text
  (21.12.5.2)                          Daf((U ∩ V)/V) = Daf(U/X) ∩ V
```

and for every `x ∈ X`,

<!-- label: IV.21.12.5.3 -->

```text
  (21.12.5.3)                          Daf((U ∩ Spec(𝒪_{X,x}))/Spec(𝒪_{X,x})) = Daf(U/X) ∩ Spec(𝒪_{X,x}).
```

We shall, when `X` is locally Noetherian, give precise information on the nature of the set `Daf(U/X)`, showing for
example that when `U` is everywhere dense in `X`, `Daf(U/X)` is not an arbitrary rare closed set:

**Theorem (21.12.6).**

<!-- label: IV.21.12.6 -->

*Let `X` be a locally Noetherian prescheme, `U` a non-empty open of `X`, `f : U → X` the canonical injection. Then:*

*(i) The closure `Z = X − U_1` of `Daf(U/X)` is of codimension `⩾ 2` in `X`.*

*(ii) If `T = X − U ⊃ Z` is of codimension `⩾ 2`, the morphism `f^∘ : U^∘ → X` is surjective.*

(i) Let us first show that for every point `x ∈ Daf(U/X)` one necessarily has `dim(𝒪_{X,x}) ⩾ 1`. Indeed, `x` cannot
evidently be a maximal point of `X`, being contained in `Ū − U`; we have therefore to see that one cannot have
`dim(𝒪_{X,x}) = 1`. But this relation would entail, by `(21.12.5.3)`, that `x ∈ Daf(U_x/Spec(𝒪_{X,x}))`, where
`U_x = U ∩ Spec(𝒪_{X,x})`. But the only opens of `Spec(𝒪_{X,x})` are `Spec(𝒪_{X,x})` itself and the subsets of the
(finite) set of maximal points of `Spec(𝒪_{X,x})`. Now the open set reduced to a maximal point of `Spec(𝒪_{X,x})` is
affine, by definition of preschemes; one concludes that all open sets in `Spec(𝒪_{X,x})` are affine, hence
`Daf(U_x/Spec(𝒪_{X,x})) = ∅`, contrary to the hypothesis made.

To prove (i) one must show more, namely that if `x ∈ X` is such that `dim(𝒪_{X,x}) = 1`, there exists an open
neighbourhood `W` of `x` in `X` such that `W` does not meet `Daf(U/X)`, that is to say such that the canonical
injection `f_W : U ∩ W → W` is affine. But, with the same notations as above, one has just seen that the canonical
injection `f^{(x)} : U^{(x)} → Spec(𝒪_{X,x})` is affine. One can evidently restrict to the case where `X` is
Noetherian; since the morphism `f` is of finite presentation, the conclusion results from `(8.10.5, (viii))` applied
following the method of `(8.1.2, a))`.

<!-- original page 307 -->

(ii) We must prove that for every point `x ∈ T`, one has `x ∈ f^∘(U^∘)`; we shall first show that one may reduce to the
case where `X = Spec(A)`, where `A` is a complete Noetherian local ring, and `x` the closed point of `X`. For this, it
suffices to make the base change `h : X' = Spec(Â) → X`, where `Â = 𝒪̂_{X,x}`; if one sets `U' = h^{-1}(U)`,
`f' = f_{(X')}` is the canonical injection `U' → X'`, and since the morphism `h` is flat, it follows from `(21.12.2)`
that if one proves that `x` belongs to `f'^∘(U'^∘)`, one deduces that `x ∈ f^∘(U^∘)`. By virtue of `(6.1.1)`, the
reduction sought has indeed been effected.

Let then `X_1` be a closed reduced sub-prescheme of `X` whose underlying space is an irreducible component of `X`, of
maximal dimension among those which contain an irreducible component of `T`, and set `U_1 = U ∩ X_1`,
`T_1 = T ∩ X_1 = X_1 − U_1`; one has therefore `codim(T_1, X_1) ⩾ 2` `(0, 14.2.1)`, and the pair `(U_1, X_1)` therefore
verifies the same hypotheses as the pair `(U, X)` (`X_1` being the spectrum of a quotient ring of `A`, hence local
Noetherian and complete). One has moreover a commutative diagram

```text
                       U_1 ──→ U
                        │      │
                       f_1│     │f
                        ↓      ↓
                       X_1 ──j→ X
```

where `i` and `j` are the canonical injections, `i` being therefore an affine morphism; one deduces `(21.12.1)` the
existence of a morphism `j^∘ : U_1^∘ → U^∘` rendering the diagram

```text
                       U_1^∘ ──→ U^∘
                        │        │
                       f_1^∘│     │f^∘
                        ↓        ↓
                       X_1 ────→ X
```

commutative, and consequently, to prove that `x ∈ f^∘(U^∘)`, it suffices to prove that `x ∈ f_1^∘(U_1^∘)`. One can
therefore replace `X` by `X_1`, and one can consequently suppose that the ring `A` is moreover *integral*. But `A` is
the quotient of a regular Noetherian ring by virtue of Cohen's theorem `(0, 19.8.8, (i))`, and since it is integral,
one can apply `(5.11.1)` with the family `(x_α)` reduced to the unique maximal point of `X`; since `codim(T, X) ⩾ 2`
by hypothesis, one sees that `f_*(𝒪_U)` is a coherent `𝒪_X`-Module, hence the morphism `f^∘ : U^∘ → X` is *finite*;
since this morphism is dominant (`U` being everywhere dense), it is surjective `(II, 6.1.10)`, and consequently
`x ∈ f^∘(U^∘)`. **Q.E.D.**

**Corollary (21.12.7).**

<!-- label: IV.21.12.7 -->

*Let `X` be a locally Noetherian prescheme, `U` a sub-prescheme induced on an open of `X`, `j : U → X` the canonical
immersion; suppose that `j` is an affine morphism. Then every irreducible component of `T = X − U` is of
codimension `⩽ 1` (and consequently of codimension `1` if `U` is everywhere dense).*

Suppose indeed that one of the irreducible components `T_1` of `T` is of codimension `⩾ 2` in `X`. Replacing if needed
`X` by an open neighbourhood of the generic point of `T_1`, one can suppose `T` irreducible and of codimension `⩾ 2`.
But then the hypothesis

<!-- original page 308 -->

that `j : U → X` is affine implies that `U^∘` is identified with `U` and `j^∘` with `j`, in other words that
`j^∘(U^∘) = U`; but this contradicts the conclusion of `(21.12.6)` which, under the dimension hypothesis made, implies
that `j^∘` must be surjective.

**(21.12.8).** Let `A` be a Noetherian local ring, `Y = Spec(A)`, `y` the unique closed point of `Y`, `Y' = Y − {y}`.
Consider the following condition:

**(W)** *For every open `U` of `Y` contained in `Y'`, containing no irreducible component of `Y'` and such that the
canonical immersion `U → Y'` is affine, `U` is itself an affine open.*

This condition is entailed by the following:

**(W̃)** *For every closed part `T` of `Y` every irreducible component of which is of codimension `1` in `Y`, and such
that for every irreducible component `Y_i` of `Y`, one has `Y_i ∩ T ≠ {y}`, the open `U = Y − T` is affine.*

Indeed, if **(W̃)** is verified and if the open `U` of `Y` verifies the hypothesis of **(W)**, it follows from
`(21.12.7)` that no irreducible component of `T = Y − U` can be of codimension `⩾ 2`; since moreover `U` contains
none of the irreducible components `Y_i − {y}` of `Y'`, condition **(W̃)** shows that `U` is affine.

Note that condition **(W̃)** simplifies when `Y` is irreducible and is then equivalent to the following:

**(W̃')** *For every irreducible closed part `T` of `Y`, of codimension `1` in `Y`, `Y − T` is an affine open.*

Indeed, it is clear that **(W̃)** entails **(W̃')** when `Y` is irreducible, and the converse is true by considering the
irreducible components of `T` and noting that the intersection of a finite number of affine opens is an affine open
`(I, 5.5.6)`.

**Examples (21.12.9).** If `A` is a factorial Noetherian local ring, it verifies **(W̃)** (and a fortiori **(W)**),
since every prime ideal of height `1` is principal `(I, 1.3.6)`. But there are non-factorial Noetherian local rings
verifying **(W)**, for example those of dimension `⩽ 1`: indeed, one noted in the proof of `(21.12.6, (i))` that all
opens of `Y` are then affine. One can moreover prove by using local duality theory (chap. III, 3rd part) that every
Noetherian local ring of dimension `2` verifies **(W)**.

The interest of condition **(W)** lies in the following result:

**Proposition (21.12.10).**

<!-- label: IV.21.12.10 -->

*Let `X`, `Y` be two locally Noetherian preschemes; `g : X → Y` a morphism, `y` a closed point of `Y`, `Y' = Y − {y}`,
`X' = g^{-1}(Y')`; suppose that the morphism `g' : X' → Y'` restriction of `g` is an open immersion, and that the local
ring `𝒪_{Y,y}` verifies condition **(W)** `(21.12.8)`. Then, for every irreducible component `Z` of
`X_y = g^{-1}(y)`, either `Z` is of codimension `⩽ 1` in `X`, or its generic point is isolated in `Z`. If `Z` is
locally of finite type over `k(y)`, the second alternative implies that `Z` is reduced to a single point.*

The last assertion of the statement results from the fact that `Z` is then a Jacobson prescheme `(10.4.7)`, and since
the set of closed points of `Z` is then dense in `Z`, the generic point of `Z` can be isolated in `Z` only if `Z` is
reduced to a single point.

Suppose that there exists in `X_y` an irreducible component `Z` whose generic point `ξ` is not isolated in `Z`, and
such that `codim(Z, X) ⩾ 2`. The question being local

<!-- original page 309 -->

on `X` and `Y` since `ξ` is non-isolated in `Z`, one can, by replacing `X` by an open neighbourhood of `ξ` in `X`,
suppose `X` and `Y` affine, `X_y = Z` irreducible, not reduced to a point and such that `codim(X_y, X) ⩾ 2`. The image
`g(X − X_y) = U` is an open of `Y'` isomorphic to `X − X_y` by hypothesis; let us show that on replacing if needed `X`
by an open neighbourhood of `ξ` in `X`, one can suppose that `U` contains none of the irreducible components of `Y'`
whose closure contains `y`. Indeed, one can first suppose that all maximal points of `X` are generizations of `ξ`, the
set of these points being finite; hence the set of maximal points of `U` is the set of images `y_i`, by `g` of the
maximal points `x_i` of `X` (no maximal point of `X` being able by hypothesis to be contained in `X_y`, since
`dim(𝒪_{X,ξ}) ⩾ 2`). Set `X_i = {x̄_i}`. By hypothesis, one has `ξ ∈ X_i` and since `ξ` is not isolated in `X_y`, there
exists in `X_y` a point `x_i ≠ ξ`. Since `X_i ≠ Z`, there exists in `X_i` a point `t_i` such that, if one sets
`T_i = {t̄_i}`, one has `dim(𝒪_{T_i, ξ}) = 1` `(10.5.9)`; this entails by hypothesis `t_i ∉ Z`, hence `t_i` is not a
generization of `ξ`. Replacing `X` by `X' = X − ⋃T_i`, one sees that the image by `g` of `X' − X_y` does not contain
the images `g(t_i)`, hence contains none of the irreducible components of `Y'` whose closure contains `y`. That being
the case, since `X` and `Y` are affine, the morphism `g : X → Y` is affine, hence so is the restriction
`g' : X' → Y'`; since `g'` is an open immersion, the canonical immersion `U → Y'` is affine. Set `Y_1 = Spec(𝒪_{Y,y})`,
`Y_1' = Y_1 − {y} = Y' ∩ Y_1`, `U_1 = U ∩ Y_1`. The foregoing proves that the canonical immersion `U_1 → Y_1'` is
affine, hence `U_1` is an affine open in `Y_1` by virtue of **(W)**, in other words the canonical immersion
`U_1 → Y_1` is affine. But since this immersion is of finite presentation `(1.6.2)`, it follows from `(8.10.5, (viii))`
applied following the method of `(8.1.2, a))` that on restricting if needed `Y` to an affine open neighbourhood of
`y`, one can suppose that the immersion `U → Y` is affine. One would conclude that the open `X − X_y` of `X`,
isomorphic to `U`, would be affine, which would contradict `(21.12.7)`; the proposition is thus proved.

**Corollary (21.12.11).**

<!-- label: IV.21.12.11 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `X` being supposed irreducible; let `g : X → Y` be a morphism
locally of finite type, and let `V` be the largest open of `X` such that the restriction `g | V : V → Y` is a local
isomorphism. Suppose that for every point `y ∈ Y`, the local ring `𝒪_{Y,y}` verifies condition **(W)**
`(21.12.8)`. Then every irreducible component of `T = X − V` is either of codimension `⩽ 1`, or such that its generic
point `ξ` is isolated in `g^{-1}(g(ξ))`.*

Set `g(ξ) = y`. The question depending only on the fibre `g^{-1}(y)` and the local ring `𝒪_{Y,y}`, one can by base
change restrict to the case where `Y = Spec(𝒪_{Y,y})` and where `X` is affine (`(I, 3.6.5)` and `(I, 4.5.5)`);
replacing if needed `X` by an open neighbourhood of `ξ` in `X`, one can suppose that `T` is irreducible; moreover one
can restrict to the case where `V` is non-empty. The morphism `g` can therefore be supposed separated and `y` closed
in `Y`; since the restriction `g | V : V → Y` is a local isomorphism and the non-empty open `V` of `X`

<!-- original page 310 -->

is irreducible, it follows from `(I, 8.2.8)` that `g | V : V → Y` is an open immersion. The restriction
`g | (V ∩ X_y) : V ∩ X_y → {y} = Spec(k(y))` is therefore also an open immersion, which shows that `V ∩ X_y` is either
empty or reduced to a point `x` rational over `k(y)`, hence closed in `X_y` `(I, 6.4.2)`. Replacing once again if
needed `X` by a smaller open neighbourhood of `ξ` in `X`, one can therefore restrict to the case where
`V ∩ X_y = ∅`, in other words `T ⊃ X_y`; since moreover `ξ ∈ X_y` is the generic point of `T`, one has
`g(T) ⊂ {y} = {y}`, in other words `T = X_y`. One is then exactly in the conditions of application of `(21.12.10)`,
whence the conclusion.

**Theorem (21.12.12)** (van der Waerden).

<!-- label: IV.21.12.12 -->

*Let `X`, `Y` be two locally Noetherian integral preschemes, `g : X → Y` a birational morphism locally of finite type.
Suppose moreover that `Y` is normal and that for every `y ∈ Y`, the ring `𝒪_{Y,y}` verifies condition **(W)** of
`(21.12.8)` (conditions fulfilled in particular when `Y` is locally factorial `(21.12.9)`). If `V` is the largest open
of `X` such that the restriction `g | V : V → Y` is a local isomorphism, all irreducible components of `T = X − V` are
of codimension `1` in `X`.*

Note that since `g` is birational, the open set `V` is non-empty; it therefore suffices to prove that a maximal point
`ξ` of `T` cannot be isolated in `X_y`, where `y = g(ξ)`. But, by restricting to an open neighbourhood of `ξ`, one can
restrict to the case where `T = X_y`; then all the fibres `g^{-1}(y')` (`y' ∈ Y`) would be empty or reduced to a
point, and it would follow from the *Main theorem* `(8.12.10)` that `g` would be a local isomorphism, contrary to the
hypothesis `ξ ∈ T`.

**Corollary (21.12.13).**

<!-- label: IV.21.12.13 -->

*Suppose the hypotheses of `(21.12.12)` are verified and in addition suppose that `g` is quasi-finite at each of the
points of `X_y` (recall that these are the points where `dim(𝒪_{X,x}) = 1`); then `g` is a local isomorphism, and if
moreover `g` is separated, `g` is an open immersion.*

It suffices to prove the first assertion, the second being a consequence of the first and of `(I, 8.2.8)`. Everything
reduces to proving, with the notation of `(21.12.12)`, that `T = ∅`; in the contrary case, a generic point `ξ` of an
irreducible component of `T` would belong to `X_y` by virtue of `(21.12.12)`, and by hypothesis it would be isolated
in `X_y` with `y = g(ξ)`; but we saw in the proof of `(21.12.12)` that this is not possible.

**Remarks (21.12.14).**

<!-- label: IV.21.12.14 -->

(i) The conclusion of `(21.12.12)` applies when `Y` is regular and integral and `X` integral, since by virtue of the
Auslander-Buchsbaum theorem `(21.11.1)`, `Y` is then locally factorial. On the other hand, examples are known where
`X` and `Y` are normal algebraic schemes of dimension `3`, over an algebraically closed field of arbitrary
characteristic, and where the conclusion of `(21.12.12)` is no longer valid.

(ii) The set `T` of `(21.12.12)` is also the set of points where `g` is ramified. Indeed, if `g` is unramified at a
point `x ∈ X`, it is also unramified in an affine open neighbourhood `U` of `x` `(17.3.7)`, hence `g | U` is a
separated, quasi-finite and birational morphism `(17.4.3)`. Since `Y` is normal, one concludes from the *Main theorem*
`(III, 4.4.9)` that `g` is a local isomorphism at the point `x`, hence `x ∈ X − T`. Conversely, `g` is evidently
unramified at every point where it is a local isomorphism. This justifies the title given to this section.

(iii) Without supposing that `Y` is locally factorial, but supposing on the other hand that `X` is a complete
intersection relative to `Y` (chap. V), we shall see in chap. V

<!-- original page 311 -->

that one has a more precise result than `(21.12.12)`, by expressing `T` as a `1`-codimensional cycle of a section of
an invertible `𝒪_X`-Module, canonically associated to `g`. This will apply notably when `X` and `Y` are both regular,
or when `g` is an `S`-morphism, `X` and `Y` being smooth preschemes over `S`.

(iv) One may ask whether `(21.12.10)` admits a converse; in other words, for a given Noetherian local ring `A`, if one
sets `Y = Spec(A)`, `y` denoting the closed point of `Y`, and if, for every locally Noetherian prescheme `X` and every
morphism `g : X → Y` such that `g' : X' → Y'` is an open immersion, every irreducible component of `X_y` is of
codimension `⩽ 1` in `X` or is reduced to a point, is it then true that `A` verifies condition **(W)** of
`(21.12.8)`?

(v) Let `Y` be an integral regular prescheme, `X` a locally Noetherian normal prescheme, `g : X → Y` a morphism locally
of finite type; suppose moreover that, if `η` is the generic point of `Y`, the fibre `X_η` is étale over `k(η)`, and
let `T'` be the complement of the largest open `V` of `X` such that `g | V : V → Y` is étale; is it then true that all
irreducible components of `T'` are of codimension `1`? This is indeed so when one supposes in addition that `g` is
locally quasi-finite (Zariski-Nagata "purity theorem"). One can show that the foregoing conjecture would be a
consequence of the following one (and would even be equivalent to it if the conjecture of (iv) were verified): for a
regular local ring `A` contained in an integral and integrally closed local ring `B`, such that `B` is a finite
`A`-module, the open `U` of points of `Spec(B)` at which `Spec(B)` is unramified over `Spec(A)` (or, what amounts to
the same by `(18.10.1)`, étale over `Spec(A)`) is affine.

**Proposition (21.12.15).**

<!-- label: IV.21.12.15 -->

*Let `S` be a prescheme, `g : X → S` a flat morphism locally of finite presentation, whose fibres
`X_s = g^{-1}(s)` are geometrically irreducible `(4.5.2)`; `h : Y → S` a smooth morphism; one denotes
`Y_s = h^{-1}(s)` the fibres of this morphism. Let `f : X → Y` be a proper `S`-morphism such that, for every maximal
point `η` of `S`, the morphism `f_η : X_η → Y_η` is an isomorphism. Then `f` is an isomorphism.*

Since `h` is flat, every maximal point of `Y` is above a maximal point of `S` `(2.3.4)`, hence the union of the `Y_η`,
when `η` runs through the set of maximal points of `S`, is dense in `Y`; since the `f_η` are isomorphisms, `f` is
dominant and hence surjective since it is proper. It therefore suffices to show that `f` is an open immersion. Taking
`(17.9.5)` into account, it suffices to prove that for every `s ∈ S`, `f_s : X_s → Y_s` is an open immersion. Since
every `s ∈ S` is a generization of a maximal point `η`, one can already, by making the base change
`Spec(𝒪_{S',s}) → S`, where `S'` is the reduced sub-prescheme of `S` having `{η̄}` as underlying space, reduce to the
case where `S` is a local and integral scheme of closed point `s`: the fibres at the points `η` and `s` are indeed
not changed and the properties of the morphisms `g`, `h` and `f` are preserved by base change. Moreover, the question
is local on `Y`; replacing `Y` by an affine open neighbourhood `U` in `Y` of a point of `Y_s`, and `X` by `f^{-1}(U)`,
which is quasi-compact since `f` is proper, one sees that one can suppose in addition that `X` and `Y` are of finite
presentation over `S`. There then exists a Noetherian local sub-ring `A_0` of `A = 𝒪_{S,s}` such that `A_0 → A` is a
local homomorphism, two morphisms of finite type `g_0 : X_0 → S_0 = Spec(A_0)`, `h_0 : Y_0 → S_0` and an
`S_0`-morphism

<!-- original page 312 -->

`f_0 : X_0 → Y_0` such that `g`, `h` and `f` are deduced from `g_0`, `h_0`, `f_0` by the base change `S → S_0`
(`(8.9.1)` and `(5.13.3)`); one can in addition suppose `g_0` flat `(11.2.7)`, `h_0` smooth `(17.7.9)` and `f_0` proper
`(8.10.5, (xii))`. On the other hand, the projection on `S_0` of the generic point `η` of `S` is the generic point
`η_0` of `S_0` and it follows from `(2.7.1, (viii))` that the morphism `(f_0)_{η_0} : (X_0)_{η_0} → (Y_0)_{η_0}` is an
isomorphism; finally the closed point `s` of `S` is above the closed point `s_0` of `S_0`, hence the fibre `(X_0)_{s_0}`
of `g_0` is geometrically irreducible `(4.5.6)`. One sees therefore that one can restrict to the case where `S` is the
spectrum of an integral Noetherian local ring, of closed point `s`, weaken the hypothesis on the fibres by supposing
only that `X_s` and `X_η` are geometrically irreducible, and prove that under these hypotheses `f_s` is an open
immersion. There is then a discrete valuation ring `A'` and a morphism `S' = Spec(A') → S` which transforms the closed
point `a` of `S'` into `s` and the generic point `b` of `S'` into `η` `(II, 7.1.9)`; let `g' : X' → S'`,
`h' : Y' → S'`, `f' : X' → Y'` be the morphisms deduced from `g`, `h`, `f` by the base change `S' → S`, which again
verify the hypotheses verified by `g`, `h`, and `f` in the statement of `(21.12.15)`; if one proves that
`f'_a : X'_a → Y'_a` is an open immersion, it will follow from `(2.7.1, (x))` that the same will be true for
`f_s : X_s → Y_s`. One can therefore finally restrict to the case where `S` is the spectrum of a *discrete valuation
ring*. Then, since `h : Y → S` is smooth, `Y` is regular `(17.5.8)`, and since the question is local on `Y`, one can
restrict to the case where `Y` is integral. Since `g : X → S` is flat, the maximal points of `X` are contained in
`X_η` `(2.3.4)` and since `f_η` is an isomorphism, `X` is irreducible and the local ring at its generic point is a
field; moreover, by flatness `(3.3.2)`, one sees that `X` has no immersed prime cycles, hence `X` is reduced `(3.2.1)`
and consequently integral and `f` is a birational and separated morphism. To prove that `f` is an open immersion, one
can therefore apply the criterion `(21.12.13)`; to see that `f` is quasi-finite at the points of `X_s`, one remarks
that the assertion is evident at those of these points which belong to `X_η`; the only point of `X_s` belonging to
`X_η` is the generic point `x` of `X_s`, by virtue of `(6.1.1)`. Now, it follows from `(2.4.6)` and `(14.2.2)` that the
morphisms `g` and `h` are equidimensional; since `X_η` and `Y_η` are isomorphic, the irreducible components of `X_s`
and of `Y_s` have all the same dimension. But by hypothesis `X_s` is irreducible and one has seen that `f` is
surjective, hence so is `f_s : X_s → Y_s`, which entails that `Y_s` is also irreducible; if `y` is the generic point
of `Y_s`, one has therefore `f(x) = y`, and the relation `dim(X_s) = dim(Y_s)` then entails, by virtue of `(5.6.6)`,
that `dim(f_s^{-1}(y)) = 0`, in other words `f_s` (and consequently also `f`) is indeed quasi-finite at the point `x`,
which completes the proof.

**Corollary (21.12.16).**

<!-- label: IV.21.12.16 -->

*Let `g : X → S` be a proper, flat morphism of finite presentation, `h : Y → S` a smooth, proper morphism of finite
presentation, `f : X → Y` an `S`-morphism. Suppose that the fibres `X_s = g^{-1}(s)` of `g` are geometrically
irreducible. Let `U` be the set of `s ∈ S` such that `f_s : X_s → Y_s` is an isomorphism. Then `U` is open and closed
in `S`, and the morphism `g^{-1}(U) → h^{-1}(U)`, restriction of `f`, is an isomorphism.*

The last assertion will result from the first and from `(17.9.5)`. One already knows `(9.6.1, (xi))` that `U` is
locally constructible in `S`. By virtue of `(1.10.1)`, it suffices to prove that `U` is stable by specialization and
by generization. To demonstrate these assertions one

<!-- original page 313 -->

can, by a base change `Spec(𝒪_{S,s}) → S`, reduce to the case where `S` is a local scheme of closed point `s` and
generic point `η`, and one must show that, in order for `f_s` to be an isomorphism, it is necessary and sufficient
that `f_η` be one. Now, the sufficiency of this condition results from `(21.12.15)`. To show that it is necessary, one
argues as in the proof of `(21.12.15)` (remarking, with the same notations, that the projection of the closed point of
`S` is the closed point of `S_0`) to reduce to the case where in addition `S` is Noetherian; but then the conclusion
results from `(III, 4.6.7, (ii))`.

**Remarks (21.12.17).**

<!-- label: IV.21.12.17 -->

(i) The conclusion of proposition `(21.12.15)` is no longer valid if one eliminates the hypothesis that the fibres
`X_s` are irreducible. Take indeed `S = Spec(A)`, where `A` is a discrete valuation ring, `Y = ℙ_S^1`, which is proper
and smooth over `S` `(17.3.9)`. Denote again `s` and `η` the closed point and the generic point of `S`; let `z` be a
closed point of `Y_s`, for example a point rational over `k = k(s)`, and let `X` be the `Y`-prescheme obtained by
blowing up the point `z`. Since the polynomial ring `A[T]` is regular `(0, 17.3.7)` and of dimension `2`, one sees as
in the proof of `(15.1.1.6)` that, if `f : X → Y` is the structure morphism, `f^{-1}(z)` is isomorphic to `ℙ^1`, and
on the other hand, the complement of `f^{-1}(z)` in `X_s` is isomorphic to `Y_s − {z}`, hence `Z_1 = f^{-1}(z)` and
`Z_2`, the closure in `X_s` of the complement of `Z_1`, are the two irreducible components of `X_s`. Moreover, `f` is
evidently proper and `g = h ∘ f` is flat, since `X` is integral `(II, 8.1.4)` and for every affine open `U` of `X`,
the homomorphism `A → Γ(U, 𝒪_X)` is injective `(I, 1.2.7)`, hence `Γ(U, 𝒪_X)` is a torsion-free `A`-module, and
consequently flat since `A` is a discrete valuation ring `(0_I, 6.3.4)`. It is clear that `f_η : X_η → Y_η` is an
isomorphism, although `f_s : X_s → Y_s` is not.

(ii) The conclusion of `(21.12.15)` also fails if, in the hypotheses, one suppresses the hypothesis that `f` is proper.
It suffices, to see this, to define `S` and `Y` as in (i), but to replace `X` by the complement `X'` of `Z_2` in the
prescheme `X` defined in (i), and `f` by the restriction `f' : X' → Y` of `f`; the morphism `g' : X' → S`, restriction
of `g`, is still flat, and this time `X'_s` is geometrically irreducible; `X'_s` is moreover isomorphic to the
complement of a closed point in `ℙ_k^1`, hence is an affine scheme isomorphic to `𝕍_k^1`; since its image in `Y_s` is
reduced to the closed point `z`, `f'` is not proper `(III, 4.4.2)` and `f'_s` is not an isomorphism, although `f'_η`
is one.

(iii) It is possible that the statement of proposition `(21.12.15)` remains valid when one replaces the word
"isomorphism" by "étale morphism" (cf. `(21.12.14, (v))`). The same will then still hold for `(21.12.16)`.

### 21.13. Parafactorial couples. Parafactorial local rings.

**Definition (21.13.1).**

<!-- label: IV.21.13.1 -->

*Let `X` be a ringed space, `Y` a closed part of `X`, `U = X − Y`. One says that the couple `(X, Y)` is **parafactorial**
if, for every open `V` of `X`, the restriction functor `ℒ ↦ ℒ | (U ∩ V)`, from the category of `𝒪_V`-Modules
invertible to that of `𝒪_{U ∩ V}`-Modules invertible, is an equivalence of categories.*

To say that the couple `(X, Y)` is parafactorial means therefore that, for every open `V` of `X`, the following
conditions are verified:

1° the functor `ℒ ↦ ℒ | (U ∩ V)` is fully faithful, in other words, for two invertible `𝒪_V`-Modules `ℒ`, `ℒ'`, the
restriction map

```text
                       Hom_{𝒪_V}(ℒ, ℒ') → Hom_{𝒪_{U ∩ V}}(ℒ | (U ∩ V), ℒ' | (U ∩ V))
```

is bijective;

2° the functor `ℒ ↦ ℒ | (U ∩ V)` is essentially surjective, in other words, for every

<!-- original page 314 -->

invertible `𝒪_{U ∩ V}`-Module `ℒ_0`, there exists an invertible `𝒪_V`-Module `ℒ` such that `ℒ_0` is isomorphic to
`ℒ | (U ∩ V)`; this is also expressed by saying that the canonical homomorphism `(21.3.2.4)`

```text
                       Pic(V) → Pic(U ∩ V)
```

is surjective.

**Lemma (21.13.2).**

<!-- label: IV.21.13.2 -->

*Let `f : X' → X` be a morphism of ringed spaces; for every open `V` of `X`, one denotes `f_V : f^{-1}(V) → V` the
restriction of `f`. The following conditions are equivalent:*

*a) For every open `V` of `X`, the functor `ℰ ↦ f_V^*(ℰ)` from the category of `𝒪_V`-Modules locally free of finite
rank into the category of `𝒪_{f^{-1}(V)}`-Modules locally free of finite rank is faithful (resp. fully faithful).*

*a') For every open `V` of `X`, the functor `ℒ ↦ f_V^*(ℒ)` from the category of `𝒪_V`-Modules locally free of rank `1`
into the category of `𝒪_{f^{-1}(V)}`-Modules locally free of rank `1` is faithful (resp. fully faithful).*

*b) For every open `V` of `X`, the canonical homomorphism `(0_I, 4.4.3.2)` `ℰ → (f_V)_*(f_V^*(ℰ))` is a monomorphism
(resp. an isomorphism) for every `𝒪_V`-Module `ℰ` locally free of finite rank.*

*b') The canonical homomorphism `𝒪_X → f_*(𝒪_{X'})` is a monomorphism (resp. an isomorphism).*

*Suppose that the canonical homomorphism `𝒪_X → f_*(𝒪_{X'})` is bijective; then, for an `𝒪_{X'}`-Module `ℰ'` locally
free of finite rank to be isomorphic to an `𝒪_{X'}`-Module of the form `f^*(ℰ)`, where `ℰ` is an `𝒪_X`-Module locally
free of finite rank, it is necessary and sufficient that the two following conditions be fulfilled:*

*(i) `f_*(ℰ')` is an `𝒪_X`-Module locally free;*

*(ii) The canonical homomorphism `(0_I, 4.4.3.3)` `f^*(f_*(ℰ')) → ℰ'` is an isomorphism.*

*When these two conditions are fulfilled, `ℰ` is isomorphic to `f_*(ℰ')`.*

To say that the functor `ℰ ↦ f_V^*(ℰ)` is faithful (resp. fully faithful) means that for two `𝒪_V`-Modules `ℰ_1`,
`ℰ_2` locally free of finite rank, the map
`Hom_{𝒪_V}(ℰ_1, ℰ_2) → Hom_{𝒪_{f^{-1}(V)}}(f_V^*(ℰ_1), f_V^*(ℰ_2))` is injective (resp. bijective); since this must
hold on replacing `V` by an open `W ⊂ V` and `ℰ_1`, `ℰ_2` by `ℰ_1 | W`, `ℰ_2 | W`, and since
`Hom_{𝒪_W}(ℰ_1 | W, ℰ_2 | W) = Γ(W, ℋom_{𝒪_V}(ℰ_1, ℰ_2))`, the condition means again that the canonical
homomorphism of sheaves

<!-- label: IV.21.13.2.1 -->

```text
  (21.13.2.1)             ℋom_{𝒪_V}(ℰ_1, ℰ_2) → (f_V)_*(f_V^*(ℋom_{𝒪_V}(ℰ_1, ℰ_2)))
```

is injective (resp. bijective). But since `ℰ_1` and `ℰ_2` are locally free of finite rank, `ℋom_{𝒪_V}(ℰ_1, ℰ_2)`,
isomorphic to `ℰ_1^∨ ⊗_{𝒪_V} ℰ_2` `(0_I, 5.4.2)`, is also locally free of finite rank; this already shows that b)
entails a), and conversely b) is a particular case of a), taking into account the isomorphism `ℰ ≃ ℋom_{𝒪_V}(𝒪_V, ℰ)`.
It is clear that a') is a particular case of a) and b') a particular case of b). Conversely, since b) is a local
property, one can, to verify it, restrict to the case where `ℰ = 𝒪_V`, and this shows that b') entails b).

If the canonical homomorphism `𝒪_X → f_*(𝒪_{X'})` is bijective, and if conditions (i) and (ii) are fulfilled, it is
clear that `ℰ' = f^*(ℰ)` with `ℰ = f_*(ℰ')`, up to isomorphism.

<!-- original page 315 -->

Conversely, suppose that `ℰ' = f^*(ℰ)`, with `ℰ` locally free; the question being local on `X`, one can suppose that
`ℰ = 𝒪_X`, whence `ℰ' = 𝒪_{X'}`, and conditions (i) and (ii) result from the hypothesis that `𝒪_X → f_*(𝒪_{X'})` is
an isomorphism.

In this number, we shall apply the preceding lemma to a canonical injection `j : U → X`, where `U` is the ringed space
induced by `X` on an open of `X`. With these notations, `(21.13.2)` translates into:

**Corollary (21.13.3).**

<!-- label: IV.21.13.3 -->

*Let `X` be a ringed space, `Y` a closed part of `X`, `U = X − Y`, `j : U → X` the canonical injection. The following
conditions are equivalent:*

*a) For every open `V` of `X`, the restriction functor `ℰ ↦ ℰ | (U ∩ V)` from the category of `𝒪_V`-Modules locally
free of finite rank into the category of `𝒪_{U ∩ V}`-Modules locally free of finite rank is faithful (resp. fully
faithful).*

*a') For every open `V` of `X`, the restriction functor `ℒ ↦ ℒ | (U ∩ V)` from the category of `𝒪_V`-Modules locally
free of rank `1` into the category of `𝒪_{U ∩ V}`-Modules locally free of rank `1` is faithful (resp. fully
faithful).*

*b) For every open `V` of `X`, the canonical homomorphism `ℰ → (j_*)(ℰ | (U ∩ V))` is injective (resp. bijective) for
every `𝒪_V`-Module `ℰ` locally free of finite rank.*

*b') The canonical homomorphism `𝒪_X → j_*(𝒪_U)` is injective (resp. bijective).*

*Suppose that the canonical homomorphism `𝒪_X → j_*(𝒪_U)` is bijective. Then, for an `𝒪_U`-Module `ℰ'` locally free of
finite rank to be of the form `ℰ | U`, where `ℰ` is an `𝒪_X`-Module locally free of finite rank, it is necessary and
sufficient that `j_*(ℰ')` be an `𝒪_X`-Module locally free, and in this case, one may take `ℰ = j_*(ℰ')`.*

**Lemma (21.13.4).**

<!-- label: IV.21.13.4 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed part of `X`, `U = X − Y`, `j : U → X` the canonical injection.
For the canonical homomorphism `𝒪_X → j_*(𝒪_U)` to be injective (resp. bijective), it is necessary and sufficient
that `prof_Y(𝒪_X) ⩾ 1` (resp. `prof_Y(𝒪_X) ⩾ 2`) (in other words, that `prof(𝒪_{X,x}) ⩾ 1` (resp.
`prof(𝒪_{X,x}) ⩾ 2`) for every `x ∈ Y`).*

These assertions are particular cases of `(5.10.2)` and `(5.10.5)`.

**Proposition (21.13.5).**

<!-- label: IV.21.13.5 -->

*Let `X` be a ringed space, `Y` a closed part of `X`, `U = X − Y`, `j : U → X` the canonical injection. For the couple
`(X, Y)` to be parafactorial, it is necessary and sufficient that the canonical homomorphism `𝒪_X → j_*(𝒪_U)` be
bijective, and that for every open `V` of `X` and every invertible `𝒪_{U ∩ V}`-Module `ℒ`, `(j_V)_*(ℒ)` be an
invertible `𝒪_V`-Module (notation of `(21.13.3)`).*

This is an immediate consequence of definition `(21.13.1)` and of `(21.13.3)`.

**Corollary (21.13.6).**

<!-- label: IV.21.13.6 -->

*Let `X` be a ringed space, `Y` a closed part of `X`.*

*(i) If the couple `(X, Y)` is parafactorial, the same is true of `(W, Y ∩ W)` for every open `W` of `X`. Conversely,
if `(W_α)` is an open covering of `X` such that each of the couples `(W_α, Y ∩ W_α)` is parafactorial, then the
couple `(X, Y)` is parafactorial.*

*(ii) If the couple `(X, Y)` is parafactorial, the same is true of `(X, Y')` for every closed part `Y'` of `Y`.*

*(iii) Suppose that `X` is a prescheme, and let `X'` be a prescheme, `f : X' → X` a faithfully flat and quasi-compact
morphism; set `Y' = f^{-1}(Y)`. Suppose that the couple `(X', Y')` is parafactorial and that the open `U = X − Y` is
retrocompact in `X` `(0_III, 9.1.1)`. Then the couple `(X, Y)` is parafactorial.*

<!-- original page 316 -->

(i) Since the fact that the canonical homomorphism `𝒪_X → j_*(𝒪_U)` is bijective is a local property on `X`,
everything reduces (by virtue of `(21.13.5)`) to seeing, denoting by `j_α` the canonical injection
`U ∩ W_α → W_α`, that one has the following property: if, for every `α` and for every invertible `𝒪_{U ∩ W_α}`-Module
`ℒ`, `(j_α)_*(ℒ | (U ∩ W_α))` is an invertible `𝒪_{W_α}`-Module, then `j_*(ℒ)` is an invertible `𝒪_X`-Module. But the
property of being an invertible `𝒪_X`-Module is local on `X`, and `(W_α)` is an open covering of `X`; since one has
`j_*(ℒ) | W_α = (j_α)_*(ℒ | (U ∩ W_α))`, this proves our assertion.

(ii) Set `U' = X − Y'` and let `j' : U' → X` be the canonical injection. To say that the homomorphism
`𝒪_X → j'_*(𝒪_{U'})` is bijective amounts to saying that for every open `V` of `X`, the homomorphism
`Γ(V, 𝒪_X) → Γ(V ∩ U', 𝒪_X)` is bijective; but the composite homomorphism

```text
                       Γ(V, 𝒪_X) → Γ(V ∩ U', 𝒪_X) → Γ(V ∩ U, 𝒪_X)
```

is bijective by hypothesis `(21.13.5)`, and on replacing `V` by `V ∩ U'`, one sees that
`Γ(V ∩ U', 𝒪_X) → Γ(V ∩ U, 𝒪_X)` is bijective, hence `Γ(V, 𝒪_X) → Γ(V ∩ U', 𝒪_X)` is bijective. Note next that if
`j'' : U → U'` is the canonical injection and if `ℒ'` is an invertible `𝒪_{U'}`-Module, `ℒ' | U` is an invertible
`𝒪_U`-Module, hence `j_*(ℒ' | U) = j'_*(j''_*(ℒ' | U))` is by hypothesis an invertible `𝒪_X`-Module. Since the couple
`(U', U' ∩ Y)` is parafactorial by virtue of (i), one has `j''_*(ℒ' | U) ≃ ℒ'`, hence `j'_*(ℒ')` is an invertible
`𝒪_X`-Module. It then suffices, to conclude, to replace in the preceding argument `X`, `U` and `U'` by `V`, `V ∩ U` and
`V ∩ U'`, where `V` is an open of `X`.

(iii) Set `U' = X' − Y' = f^{-1}(U)` and note that since one is dealing with preschemes, one can write
`U' = U ×_X X'`; let `f_U : f^{-1}(U) → U` be the restriction of `f` and let `j' : U' → X'` be the canonical injection,
which one also writes `j_{(X')}`. Let us first show that the canonical homomorphism `ρ : 𝒪_X → j_*(𝒪_U)` is bijective;
for this, note that by hypothesis the canonical homomorphism `𝒪_{X'} → j'_*(𝒪_{U'})` is bijective; but since the
morphism `j` is quasi-compact and separated by hypothesis, and the morphism `f` flat, `j'_*(𝒪_{U'}) = j'_*(f_U^*(𝒪_U))`
is canonically identified with `f^*(j_*(𝒪_U))` by virtue of `(2.3.1)`; since `𝒪_{X'} = f^*(𝒪_X)`, one sees that the
homomorphism `f^*(ρ) : f^*(𝒪_X) → f^*(j_*(𝒪_U))` is bijective; one concludes that `ρ` is bijective since `f` is
faithfully flat `(2.2.7)`. Consider next an invertible `𝒪_U`-Module `ℒ`, and let `ℒ' = f_U^*(ℒ)`, which is an
invertible `𝒪_{U'}`-Module. By hypothesis `j'_*(f_U^*(ℒ))` is an invertible `𝒪_{X'}`-Module, which is isomorphic to
`f^*(j_*(ℒ))` by `(2.3.1)` as above. But since `f` is faithfully flat and quasi-compact, this entails that `j_*(ℒ)`
is an `𝒪_X`-Module locally free `(2.5.2)`. To complete the proof, it suffices to replace `X` by an open `V` and `X'`
by `f^{-1}(V)` in the foregoing.

**Definition (21.13.7).**

<!-- label: IV.21.13.7 -->

*One says that a local ring `A` is **parafactorial** if, setting `X = Spec(A)` and denoting by `a` the closed point of
`X`, the couple `(X, {a})` is parafactorial.*

**Proposition (21.13.8).**

<!-- label: IV.21.13.8 -->

*The notations being those of `(21.13.7)`, set `U = X − {a}`. For `A` to be parafactorial, it is necessary and
sufficient that it verify the following conditions:*

*(i) The canonical homomorphism `A = Γ(X, 𝒪_X) → Γ(U, 𝒪_X)` is bijective,*

*(ii) `Pic(U) = 0`.*

<!-- original page 317 -->

*If moreover `A` is Noetherian, condition (i) is equivalent to*

*(i bis) `prof(A) ⩾ 2`.*

Indeed, the only open of `X` containing `a` is `X` itself, and consequently every invertible `𝒪_X`-Module is isomorphic
to `𝒪_X`, in other words `Pic(X) = 0`; the first assertion therefore results from definition `(21.13.1)` and from
`(21.13.3)`. The second assertion is a particular case of `(21.13.4)`.

**Examples (21.13.9).**

<!-- label: IV.21.13.9 -->

(i) A parafactorial Noetherian local ring is necessarily of dimension `⩾ 2` by virtue of `(21.13.8)`; in other words a
Noetherian local ring of dimension `⩽ 1` is not parafactorial.

(ii) A factorial Noetherian local ring `A` of dimension `⩾ 2` is parafactorial, as follows from `(21.13.8)` and
`(21.6.14)`.

(iii) If `A` is a Noetherian local ring of dimension `⩾ 3` and parafactorial, it is not necessarily normal nor even
reduced. Consider a regular local ring `B` of dimension `⩾ 3`, and let `A = D_B(B)` `(0, 18.2.3)`, isomorphic to
`B[T]/(T^2)`; one sees at once that one has `prof(A) = prof(B) = dim(B) ⩾ 3`. To show that `A` is parafactorial, it
suffices, with the notations of `(21.13.8)`, to prove that `Pic(U) = 0`. Let `𝒥` be the kernel of the augmentation
`A → B`, which is such that `𝒥^2 = 0` and which, as a `B`-module, is isomorphic to `B`. Since `B = A/𝒥`, `X = Spec(A)`
and `X_0 = Spec(B)` have the same underlying space; if `ℐ = 𝒥̃`, `X_0` is the sub-scheme defined by `ℐ`, we shall
denote `U_0` the sub-prescheme induced by `X_0` on the open `U`. For every `z ∈ 𝒥`, set `φ(z) = 1 + z`; since
`(1 + z)(1 − z) = 1`, `1 + z` is invertible in `A` and `φ(𝒥)` is the kernel of the canonical surjective homomorphism of
multiplicative groups `A^× → B^×`; in other words, one has an exact sequence of commutative groups

```text
                       0 → 𝒥 →^φ A^× → B^× → 1
```

(the last three groups being multiplicative, the first two additive). For the same reason, for every `t ∈ A`, one has
the exact sequence

```text
                       0 → 𝒥_t → (A_t)^× → (B_{t_0})^× → 1
```

denoting by `t_0` the image of `t` in `B`, since `B_{t_0} = A_t / 𝒥_t`; in other words, one has an exact sequence of
sheaves of commutative groups on the topological space `X`

```text
                       0 → ℐ → 𝒪_X^× → 𝒪_{X_0}^× → 1
```

whence by restriction to the open `U`, an exact sequence

```text
                       0 → ℐ | U → 𝒪_U^× → 𝒪_{U_0}^× → 1.
```

By the cohomology exact sequence, one deduces an exact sequence

<!-- label: IV.21.13.9.1 -->

```text
  (21.13.9.1)             H^1(U, ℐ) → H^1(U, 𝒪_U^×) → H^1(U, 𝒪_{U_0}^×).
```

But since `𝒥` is a `B`-module isomorphic to `B`, one has `H^1(U, ℐ) ≃ H^1(U_0, 𝒪_{U_0})`, and it follows from chap.
III, 3rd part (see also `[41, III, Example III-1]`) that one has

<!-- original page 318 -->

`H^1(U_0, 𝒪_{U_0}) = 0` by reason of the relation `prof(B) ⩾ 3`. Moreover, since `B` is factorial, one has
`H^1(U, 𝒪_{U_0}^×) = Pic(U_0) = 0`; one therefore draws indeed from the preceding exact sequence that
`Pic(U) = H^1(U, 𝒪_U^×) = 0`.

(iv) There also exist Noetherian local rings of dimension `3` which are integral, integrally closed and parafactorial,
but not factorial. Let indeed `B` be a Noetherian local ring, complete, integral and integrally closed, of dimension
`⩾ 2` and non-factorial (for example the completion of the localized ring of the integral algebra
`k[U, V, W]/(W^2 − UV)` at the maximal ideal image of `(U) + (V) + (W)`). Then it will follow from what we shall see
below `(21.14.2)` that the local ring `A = B[[T]]` of formal series in `T` over `B` is parafactorial, but it is not
factorial, otherwise `B` would be by virtue of `(21.13.12)` below.

(v) One can show that an absolute complete intersection local ring `(19.3.1)` of dimension `⩾ 4` is parafactorial
(cf. `[41, XI, 3.13 (i))]`).

(vi) One has seen (Remark (ii)) that every factorial Noetherian local ring `A` of dimension `2` is parafactorial. But
there are Noetherian local rings of dimension `2` which are parafactorial and non-factorial. One can show that, for a
Noetherian local ring `A` of dimension `2` to be parafactorial and non-factorial, it is necessary and sufficient that
it satisfy the three following conditions:

1° `A` is a Cohen-Macaulay ring (in other words `prof(A) = 2`).

2° `A` is integral and if `A'` is its integral closure, `A'` is factorial and is a finite `A`-algebra.

3° Let `𝒥` be the conductor of `A` in `A'` (annihilator of the `A`-module `A'/A`, or also the largest ideal of `A'`
contained in `A`); set `B = A/𝒥`, `B' = A'/𝒥`; then `dim(B) = 1` (which implies `A' ≠ A`, in other words `A` is not
integrally closed), and the canonical map `D(B) → D(B')` `(21.4.5)` is surjective.

One can show moreover that these conditions entail the following property:

4° The ring `B'` (and a fortiori `B ⊂ B'`) is reduced, and the morphism `Spec(B') → Spec(B)` is bijective.

If one sets `X = Spec(A)`, `X' = Spec(A')`, `Y = Spec(B)`, `Y' = Spec(B')`, so that `Y` (resp. `Y'`) is defined by the
ideal `𝒥` of `A` (resp. `A'`), the structural morphism `f : X' → X` is an isomorphism of `X' − Y'` onto `X − Y`
(Bourbaki, _Alg. comm._, chap. V, §1, n° 5, cor. 5 of prop. 16). One sees therefore by virtue of 4° that `f` is a
bijective morphism; in other words, `X` is a unibranch prescheme `(6.15.1)` (and in particular `A'` is a Noetherian
local ring); in general `X` is not geometrically unibranch. The space `Y`, of dimension `1`, is constituted by the
closed point `x` of `X` and the maximal points `y_i` (`1 ⩽ i ⩽ r`) of `Y`, and the unique point `y'_i` of `Y'` above
`y_i` is also a maximal point of `Y'`; since `B` and `B'` are reduced, one deduces that one has `𝔪_{X', z'} = 𝔪_{X, z}`
for `z = y_i` and `z' = y'_i`; this relation is also evidently verified for `z ∈ Y` and `z'` the unique point of
`f^{-1}(z)`, hence for every `z ∈ U = X − {x}` and `z'` the unique point of `f^{-1}(z)`. In particular, if the ring `A`
is of characteristic `0` `(0, 21.1.1)` one sees that `U'` is unramified over `U` (but not étale in general).

We shall restrict ourselves here to demonstrating that conditions 1°, 2°, 3° above are sufficient for `A` to be

<!-- original page 319 -->

parafactorial. Now, by virtue of condition 1° and of `(21.13.8)`, it suffices to show that `Pic(U) = 0`.

Since `A'` is factorial by virtue of 2°, one has `Pic(U') = 0`, and one deduces from `(21.8.5, (ii))` an exact sequence

```text
                       1 → (⨁_{s ∈ S} (A'_{p'_s})^× / (A_{p_s})^×) / Im(Γ(U', 𝒪_{U'}^×)) → Pic(U) → Pic(U') → 0
```

and one must therefore show that the second term of this sequence is reduced to the neutral element, taking for `S` the
set of the `y_i` (`1 ⩽ i ⩽ r`) and noting that here `f_*(𝒪_{X'}) = A'` is the `𝒪_X`-Algebra `Ã'`. Let `p_i`, `p'_i` be
the prime ideals of `A` and `A'` corresponding to the points `y_i`, `y'_i`, and remark that `p'_i ∩ A = p_i`; let us
give for each `i` an invertible element `a'_i/s_i` of `A'_{p'_i}` with `a'_i ∈ A'`, `s_i ∉ p'_i`; since we have only
to examine the quotient groups `A'_{p'_i}^× / A_{p_i}^×`, one can suppose `s_i = 1` for all `i`; let `b'_i ∈ B' = A'/𝒥`
be the canonical image of `a'_i`, so that `b'_i` is a non-zero element of `k(y'_i) = B'_{p'_i}`. The set `U ∩ Y` formed
by the `y_i` is an affine open of the form `D(t)` in `Y`, with `t ∉ 𝔪`, the maximal ideal of `A`; there exists
therefore an invertible element `b ∈ B'_t` whose `b'_i` are the canonical images, and since `t` is regular in the
integral ring `A'`, one can suppose `b` of the form `b''/t^n`, where `b'' ∈ B'` is invertible. Let `a''` be an element
of `A'` in the class `b''`, which is therefore necessarily invertible; `a' = a''/t^n` is invertible in `A'_t` and for
every `i`, one has `u_i = a' − a'_i ∈ 𝒥`, whence `t^n a'_i = a'' − t^n u_i = a''(1 − a''^{-1} t^n u_i)`; but
`a''^{-1} t^n u_i ∈ 𝒥 ⊂ 𝔪`, hence `1 − a''^{-1} t^n u_i` is an invertible element of `A`, and the classes of `a'` and
`a'_i` in `A'_{p'_i}^× / A_{p_i}^×` are the same, which completes the proof.

To have an explicit example of a parafactorial ring of dimension `2` obtained in this manner and *non-factorial*,
consider the ring `E = ℝ[[U, V]]/(U^2 + V^2)`, whose integral closure `E'` identifies with `ℂ[[U]]` `(6.15.11)`. If one
sets `A = E[[T]]`, the integral closure of `A` is the ring `A' = E'[[T]]` (Bourbaki, _Alg. comm._, chap. V, §1, n° 4,
prop. 14); one verifies at once that the conductor of `E` in `E'` is the maximal ideal `𝔫` of `E`, hence the conductor
`𝒥` of `A` in `A'` is `𝔫[[T]]`, and one has `B = A/𝒥 ≃ ℝ[[T]]`, `B' = A'/𝒥 ≃ ℂ[[T]]`. It is then immediate that
conditions 1°, 2° and 3° stated above are indeed verified, but `A` is not even integrally closed.

One can vary this example, and the reader will see without difficulty that if `k` is an algebraically closed field, the
ring `A`, localization of the ring `k[U, V, W]/(U^2 − WV^2)` at the maximal ideal generated by the images of `U`, `V`
and `W`, verifies also conditions 1°, 2° and 3° above.

It could be that these three conditions imply even that each of the rings `B'/p'_i` is a discrete valuation ring,
which would entail that `A'` is even a regular ring.

**Proposition (21.13.10).**

<!-- label: IV.21.13.10 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed part of `X`. For the couple `(X, Y)` to be parafactorial it is
necessary and sufficient that, for every `y ∈ Y`, the local ring `𝒪_{X,y}` be parafactorial.*

Set `U = X − Y` and let `j : U → X` be the canonical injection.

By virtue of `(21.13.4)`, to say that the canonical homomorphism `𝒪_X → j_*(𝒪_U)` is injective is equivalent to saying
that each of the local rings `𝒪_{X,y}` for `y ∈ Y` satisfies condition (i bis) of `(21.13.8)`.

Let us first show that if the couple `(X, Y)` is parafactorial, each of the rings `𝒪_{X,y}` (`y ∈ Y`) is parafactorial.
Taking the preceding remark into account, everything reduces to seeing that, if one sets `T_y = Spec(𝒪_{X,y})` and
`U_y = T_y − {y}`, every invertible `𝒪_{U_y}`-Module `ℒ_0` is isomorphic to `𝒪_{U_y}`. Now, when `V` runs through the
set of affine open neighbourhoods of `y` in `X`, it follows from `(8.2.13)` and `(I, 2.4.2)` that the prescheme `U_y` is
projective limit of the preschemes induced by `X` on the opens `V − (V ∩ {y})` which are quasi-compact since `X` is
locally Noetherian. Since the `U_V = V − (V ∩ {y})` are separated, it follows from `(8.5.2, (ii))` and `(8.5.5)` that
there is an affine open neighbourhood `V` of `y` in `X` and an invertible `𝒪_{U_V}`-Module `ℒ_V` such that `ℒ_0` is the
sheaf induced by `ℒ_V` on `U_y`. But the hypothesis entails, by virtue of `(21.13.6, (i) and (ii))`, that the couple
`(V, V ∩ {y})` is parafactorial; one concludes by definition `(21.13.1)` that there exists a `𝒪_V`-Module invertible
`ℒ_V'` inducing `ℒ_V` on `U_V`. Replacing if needed `V` by a smaller open neighbourhood of `y`, one can suppose that
`ℒ_V'` is isomorphic to `𝒪_V`, whence one concludes that `ℒ_0` is isomorphic to `𝒪_{U_y}`.

Conversely, let us prove that if all the `𝒪_{X,y}` (`y ∈ Y`) are parafactorial the couple `(X, Y)` is parafactorial.
One is evidently reduced, taking the remark at the beginning into account, to showing that for every invertible
`𝒪_U`-Module `ℒ`, `j_*(ℒ)` is an invertible `𝒪_X`-Module `(21.13.5)`. The question being local on `X`, one can suppose
`X` Noetherian. The set of `x ∈ X` such that the restriction of `j_*(ℒ)` to an open neighbourhood of `x` in `X` is
invertible is evidently open in `X`; one must show that `V = X`. For this, suppose the contrary and set
`Z = X − V ≠ ∅`. Let `y` be a maximal point of `Z`; since `Z ⊂ Y` by definition, `𝒪_{X,y}` is by hypothesis a
parafactorial ring. Replacing if needed `X` by an open neighbourhood of `y` in `X`, one can suppose that the
restriction of `j_*(ℒ)`

<!-- original page 320 -->

to `V − (V ∩ {y})` is invertible; hence, with the notations introduced above, the `𝒪_{U_y}`-Module `ℒ_0` induced by
`j_*(ℒ)` on `U_y` is invertible. Since `𝒪_{X,y}` is parafactorial, `ℒ_0` is induced by an invertible `𝒪_{T_y}`-Module
`ℒ'`; but since `T_y` is the projective limit of the open neighbourhoods `W` of `y` in `X`, one can again apply
`(8.5.2, (ii))` and `(8.5.5)`, proving the existence of such a neighbourhood `W` and of an invertible
`𝒪_W`-Module `ℒ''` inducing `ℒ'` on `T_y`, hence inducing `ℒ_0` on `U_y`; applying this time `(8.5.2.5)` and
`(8.5.2, (i))`, one deduces that on replacing if needed `W` by a smaller open neighbourhood of `y`, one can suppose
that the restrictions of `j_*(ℒ)` and of `ℒ''` to `W − (W ∩ {y})` are equal. If one then sets `V_1 = V ∪ W` and if one
denotes by `ℒ_1` the invertible `𝒪_{V_1}`-Module equal to `ℒ''` in `W`, to `j_*(ℒ) | V` in `V`, one has `U ⊂ V_1` and
`ℒ_1 | U = ℒ`. One then concludes from the fact that the homomorphism `𝒪_X → j_*(𝒪_U)` is bijective and from
`(21.13.2, b))` that `j_*(ℒ) | V_1` is isomorphic to `ℒ_1`, hence invertible. But this contradicts the definition of
`V`, and therefore concludes the proof of `(21.13.10)`.

**Corollary (21.13.11).**

<!-- label: IV.21.13.11 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed part of `X`, `U = X − Y`. Suppose that the couple `(X, Y)` is
parafactorial and that `U` is locally factorial; in other words `(21.13.10)`, for every `x ∈ X`, the ring `𝒪_{X,x}`
is: 1° parafactorial if `x ∈ Y`; 2° factorial if `x ∉ Y`. Then `X` is locally factorial (in other words, `𝒪_{X,x}` is
in fact factorial for every `x ∈ X`).*

Suppose indeed the contrary, and let `y` be a point of `Y` such that `𝒪_{X,y}` is not factorial and has minimal
dimension among all points of `Y` having this property. Then, if one sets `T_y = Spec(𝒪_{X,y})`, `U_y = T_y − {y}`,
the hypothesis that `𝒪_{X,y}` is parafactorial entails `Pic(U_y) = 0` and `prof(𝒪_{X,y}) ⩾ 2` `(21.13.8)`; moreover the
choice of `y` entails that `U_y` is locally factorial. But then `(21.6.14)` proves that `𝒪_{X,y}` is factorial,
contrary to hypothesis.

**Proposition (21.13.12).**

<!-- label: IV.21.13.12 -->

*Let `A`, `B` be two Noetherian local rings, `ρ : A → B` a local homomorphism making `B` a flat `A`-module. Then, if
`B` is factorial, so is `A`.*

One already knows that `A` is integral and integrally closed `(6.5.4)`, hence one can restrict to the case where
`dim(A) ⩾ 2`, and reason by recurrence on `n = dim(A)`. Let `X = Spec(A)`, `a` the closed point of `X`,
`X' = Spec(B)`, `f : X' → X` the structural morphism, `U = X − {a}`, `U' = f^{-1}(U)`.

The local rings `𝒪_{X', x'}` at points `x' ∈ f^{-1}(a)` are factorial and of dimension `⩾ 2` `(6.1.2)`, hence
parafactorial `(21.13.9, (ii))`; one concludes `(21.13.10)` that the couple `(X', f^{-1}(a))` is parafactorial. By
virtue of `(21.13.6, (iii))`, this shows that the ring `A` is parafactorial, hence `prof(A) ⩾ 2` and `Pic(U) = 0`
`(21.13.8)`. Finally, the local rings of `U` being of dimension `< n`, the recurrence hypothesis proves that `U` is
locally factorial; the conclusion then results from `(21.6.14)`.

**(21.13.12.1).** Note that the statement `(21.13.12)` where one replaces "factorial" by "parafactorial" is no longer
exact, as shows the example where `A = k` is a field and `B` the factorial local ring `k[[T_1, T_2]]`. However, it
follows from `(21.13.6, (iii))` that, under the conditions of `(21.13.12)`, if `𝔪` denotes the maximal ideal of `A`
and if `𝔪B` is an ideal

<!-- original page 321 -->

of definition of `B` (in other words, if `dim(B/𝔪B) = 0`), then, when `B` is parafactorial, so is `A`. In particular,
if the completion `Â` of a Noetherian local ring is parafactorial, so is `A`.

**Remark (21.13.13).**

<!-- label: IV.21.13.13 -->

A part of the foregoing definitions and results is attached to more general considerations on the cohomology of
sheaves of commutative groups on a topological space, developed in chap. III, 3rd part, and we have given here an
independent exposition only for the convenience of the reader. Indeed, if `X` is a ringed space, one has a canonical
equivalence between the category of invertible `𝒪_X`-Modules and that of principal homogeneous sheaves under the
sheaf of groups `𝒪_X^×` `(16.5.15)`. This equivalence is defined by associating to every invertible `𝒪_X`-Module `ℒ`
the sheaf `ℒ^* = ℐ𝓈om_{𝒪_X}(𝒪_X, ℒ)` of germs of isomorphisms of `𝒪_X` onto `ℒ`; it is immediate that `ℒ^*` is
canonically equipped with a structure of principal homogeneous sheaf under
`𝒪_X^× = ℐ𝓈om_{𝒪_X}(𝒪_X, 𝒪_X)`. The verification of the fact that the functor `ℒ ↦ ℒ^*` is an equivalence of
categories is immediate. That being the case, consider in a general way a topological space `X` and a sheaf of groups
`𝒢` on `X`; let `Y` be a closed part of `X`, set `U = X − Y`, and let `i` be an integer such that `0 ⩽ i ⩽ 2`; one
will say that the couple `(X, Y)` is **`i`-pure for `𝒢`** if, for every open `V` of `X`, the restriction functor
`𝒮 ↦ 𝒮 | (U ∩ V)`, from the category of principal homogeneous sheaves under the sheaf of groups `𝒢 | V`, into the
analogous category under the sheaf of groups `𝒢 | (U ∩ V)`, is faithful (`i = 0`), resp. fully faithful (`i = 1`),
resp. an equivalence of categories (`i = 2`). In the case where `X` is a ringed space and `𝒢 = 𝒪_X^×`, to say that
`(X, Y)` is `i`-pure means therefore for `i = 0`, that the homomorphism `𝒪_X^× → j_*(𝒪_U^×)` is *injective*; for
`i = 1`, that this homomorphism is *bijective*; and finally, for `i = 2`, that the couple `(X, Y)` is *parafactorial*
`(21.13.3)`.

Returning to the general case, recall that the morphisms in the category of principal sheaves under `𝒢` are by
definition the *isomorphisms*. To say that the couple `(X, Y)` is `0`-pure means therefore that for every open `V` of
`X`, the canonical homomorphism `H^0(V, 𝒢) → H^0(U ∩ V, 𝒢)` is injective; to say that the couple `(X, Y)` is `1`-pure
means that the canonical homomorphism `H^0(V, 𝒢) → H^0(U ∩ V, 𝒢)` is bijective (and then the canonical homomorphism
`H^1(V, 𝒢) → H^1(U ∩ V, 𝒢)` is injective); finally, one can show that for the couple `(X, Y)` to be `2`-pure, it is
necessary and sufficient that the homomorphisms `H^i(V, 𝒢) → H^i(U ∩ V, 𝒢)` be bijective for `i = 0` and `i = 1`. When
`𝒢` is a sheaf of commutative groups, introducing the cohomology sheaves `ℋ_Y^p(𝒢)` defined in chap. III, 3rd part,
to say that `(X, Y)` is `i`-pure for `i ⩽ 2` means that `ℋ_Y^p(𝒢) = 0` for `p ⩽ i`; in this form, the notion
generalizes immediately for every integer `i`.

**Proposition (21.13.14).**

<!-- label: IV.21.13.14 -->

*Let `X` be a locally Noetherian normal prescheme, `(U_λ)_{λ ∈ L}` a filtering decreasing family of opens of `X`. The
following conditions are equivalent:*

*a) Every `1`-codimensional cycle `Z` on `X` such that there exists an index `λ` for which `Z | U_λ` is locally
principal `(21.6.7)`, is locally principal.*

*b) For every `x ∈ X` such that `dim(𝒪_{X,x}) ⩾ 2` and such that `x` does not belong to `⋂ U_λ`, the ring `𝒪_{X,x}` is
parafactorial.*

<!-- original page 322 -->

*b') For every closed part `Y` of `X` such that `codim(Y, X) ⩾ 2` and such that there exists `λ` for which
`Y ⊂ X − U_λ`, the couple `(X, Y)` is parafactorial.*

Property a) can again be expressed in the following manner: if the closed set `N` of points `x ∈ X` where `Z` is not
principal is contained in one of the `X − U_λ`, then `Z` is locally principal. Since `X` is normal, the condition
`dim(𝒪_{X,x}) ⩽ 1` entails that `𝒪_{X,x}` is a field or a discrete valuation ring, hence `Z_x` is principal; in other
words, one has necessarily `codim(N, X) ⩾ 2` `(5.1.3)`. Property a) is therefore equivalent to the following:

a') *If there exists a closed set `Y` contained in one of the `X − U_λ`, such that `codim(Y, X) ⩾ 2` and such that
`Z | X − Y` is locally principal, then `Z` is locally principal.*

Note on the other hand that b) implies b') by virtue of `(21.13.10)`; conversely, if b') is verified and if `x ∉ U_λ`,
then `Y = {x̄}` is contained in `X − U_λ` and one has `codim(Y, X) ⩾ 2`, hence it follows again from `(21.13.10)` that
`𝒪_{X,x}` is parafactorial, which proves the equivalence of b) and b'). One is thus reduced to proving the equivalence
of a') and b'). Note that since `X` is normal, one has, for every closed part `Y` of `X` such that
`codim(Y, X) ⩾ 2`, `prof_Y(𝒪_X) ⩾ 2` `(5.8.6)`; if one sets `U = X − Y`, the homomorphism `𝒪_X → j_*(𝒪_U)` is therefore
bijective `(21.13.4)`; since the conditions a') and b') are local, one sees that it suffices to show the equivalence of
the following conditions, when `X` is Noetherian and normal and `Y` is closed in `X` and such that
`codim(Y, X) ⩾ 2`:

a'') *For every `1`-codimensional cycle `Z` on `X`, the hypothesis that `Z | U` (where `U = X − Y`) is locally
principal entails that `Z` itself is locally principal.*

b'') *The canonical homomorphism `Pic(X) → Pic(U)` is surjective.*

Let us first prove that a'') entails b''); an element `ζ_0 ∈ Pic(U)` has for image in `Cl(U)` `(21.6.11)` the class of
a `1`-codimensional cycle `Z_0` on `U`, which is locally principal. The hypothesis `codim(Y, X) ⩾ 2` entails that the
restriction homomorphism `𝒵^1(X) → 𝒵^1(U)` is bijective, hence `Z_0 = Z | U`, where `Z` is a `1`-codimensional cycle
on `X`; since `Z_0` is locally principal, so is `Z` by virtue of a''); it follows from `(21.6.11)` that the image of `Z`
in `Cl(X)` is the image of a unique element `ζ ∈ Pic(X)`, and it is clear then that `ζ_0` is the image of `ζ`.

Conversely, let us prove that b'') entails a''). Let then `Z` be a `1`-codimensional cycle on `X` such that `Z | U` is
locally principal; the image of `Z | U` in `Cl(U)` is therefore the image of a unique element `ζ_0 ∈ Pic(U)`
`(21.6.11)`. By hypothesis there exists `ζ ∈ Pic(X)` whose image in `Pic(U)` is `ζ_0`; the image of `ζ` in `Cl(X)` is
therefore the class of a `1`-codimensional cycle `Z'` on `X` such that `Z | U` and `Z' | U` are linearly equivalent.
But since `U` is schematically dense in `X`, the image of `𝒵_{princ}^1(X)` by the isomorphism `𝒵^1(X) → 𝒵^1(U)` is
`𝒵_{princ}^1(U)`, hence `Z` and `Z'` are linearly equivalent, and since `Z'` is locally principal, so is `Z`.

**Corollary (21.13.15).**

<!-- label: IV.21.13.15 -->

*Let `X` be a locally Noetherian and normal prescheme, `S` a part of `X`. The following conditions are equivalent:*

*a) Every `1`-codimensional cycle on `X` which is principal at the points of `S` is locally principal.*

<!-- original page 323 -->

*b) For every `x ∈ X` which is not a generization of a point of `S` (in other words, such that `{x̄} ∩ S = ∅`) and
which is such that `dim(𝒪_{X,x}) ⩾ 2`, the ring `𝒪_{X,x}` is parafactorial.*

It is clear that the set `S'` of points of `X` generizations of points of `S` is the intersection of the open
neighbourhoods of `S`. One can restrict to the case where `X` is Noetherian (properties a) and b) being local on `X`);
since every `1`-codimensional cycle on `X` which is principal at the points of `S` is also so at the points of an open
neighbourhood of `S`, one sees that condition a) of `(21.13.15)` is equivalent to condition a) of `(21.13.14)` applied
to the family `(U_λ)` of open neighbourhoods of `S`. The corollary then results from the equivalence of a) and b) in
`(21.13.14)`.

**Remark (21.13.16).**

<!-- label: IV.21.13.16 -->

Under the general conditions of `(21.13.14)`, suppose moreover that one has `lim Pic(U_λ) = 0`. Then condition a) of
`(21.13.14)` is also equivalent to the following:

c) *Every `1`-codimensional cycle on `X` whose support is contained in one of the sets `X − U_λ` is locally
principal.*

One can restrict to the case where `X` is irreducible and all `U_λ` are non-empty. It is clear that a) entails c), for
if the `1`-codimensional cycle `Z` on `X` has its support in `X − U_λ`, `Z | U_λ = 0`, hence `Z | U_λ` is locally
principal. Conversely c) entails a): let indeed `Z` be a `1`-codimensional cycle on `X` such that `Z | U_λ` is locally
principal; since `X` is normal, `Z | U_λ = cyc(D_λ)`, where `D_λ` is a divisor on `U_λ` `(21.6.10, (i))`, and the
hypothesis implies (by virtue of `(21.3.4)`) that there is a set `U_μ ⊂ U_λ` such that `D_μ = D_λ | U_μ` is equivalent
to `0`. If `D_μ = div(f_μ)`, where `f_μ` is a regular rational function on `U_μ`, `f_μ` can be considered as a regular
rational function on `X`. If `Z' = cyc(div(f_μ))`, one sees therefore that `Z'' = Z − Z'` has its support in
`X − U_μ`; by virtue of the hypothesis, `Z''` is locally principal, whence the conclusion.

The condition `lim Pic(U_λ) = 0` will in particular be fulfilled if `(U_λ)` is the family of open neighbourhoods of a
point `z ∈ X`, for every invertible `𝒪_{U_λ}`-Module `ℒ_λ`, there exists by definition a `U_μ ⊂ U_λ` such that
`ℒ_λ | U_μ` is isomorphic to `𝒪_{U_μ}`. One sees therefore that, in the statement of `(21.13.15)`, if `S = {z}`,
conditions a) and b) are also equivalent to the following:

c) *Every `1`-codimensional cycle on `X` whose support does not contain `z` is locally principal.*

If moreover `Pic(X) = 0`, one will conclude that this condition entails that every `1`-codimensional cycle whose
support does not contain `z` is *principal*.

### 21.14. The Ramanujam-Samuel theorem

**Theorem (21.14.1)** (Ramanujam-Samuel).

<!-- label: IV.21.14.1 -->

*Let `A` be a Noetherian local ring of maximal ideal `𝔪`, such that its completion `Â` is integral and integrally
closed. Let `B` be a Noetherian local ring such that `dim(B) > dim(A)`, `ρ : A → B` a local homomorphism making `B` a
formally smooth `A`-algebra (for the preadic topologies `(0, 19.3.1)`) and such that the residue field of `B` is
finite over that of `A`. Then every `1`-codimensional cycle on `Spec(B)` which is principal at the point `p = 𝔪B` is a
principal `1`-codimensional cycle.*

If `k = A/𝔪` is the residue field of `A`, `B/𝔪B` is a formally smooth `k`-algebra (for

<!-- original page 324 -->

its preadic topology) `(0, 19.3.5)`, hence regular, and in particular integral; in other words `p = 𝔪B` is indeed a
prime ideal of `B`, which justifies the statement. Everything evidently reduces to proving that every prime ideal `q`
of `B` not contained in `p` is principal.

Let `Â`, `B̂` be the completions of `A` and `B` respectively, so that the maximal ideal of `Â` is `𝔪Â`; one knows
`(0, 19.3.6)` that `B̂` is a formally smooth `Â`-algebra for the adic topologies. Let `k'` be the residue field of `B`,
a finite extension of `k`; there exists a local homomorphism `Â → C`, where `C` is a Noetherian local ring which is a
finite and flat (hence free) `Â`-module and is such that `C/𝔪C` is isomorphic to `k'` `(0_III, 10.3.1)`; one deduces
that `C` is complete, and it then follows from `(7.5.1)`, `(7.5.3)` and `(6.5.4, (ii))` that `C` is integral and
integrally closed. Moreover, `D = B̂ ⊗_Â C` is a complete semi-local ring, direct composite of complete local rings
one of which, `D_0`, has residue field `k'` (since `k' ⊗_k k'` is direct composite of local rings one of which is
isomorphic to `k'`). Since `D` is formally smooth over `C`, the same is true of `D_0`; consequently `D_0/𝔪D_0` is a
formally smooth `k'`-algebra, of residue field `k'`, which entails that it is `k'`-isomorphic to a formal series
algebra `k'[[T_1, …, T_n]]` `(0, 19.6.4)`; one concludes, by `(0, 19.7.1.5)`, that `D_0` is `C`-isomorphic to
`C[[T_1, …, T_n]]`, and consequently integral and integrally closed (Bourbaki, _Alg. comm._, chap. V, §1, n° 4,
prop. 14). Since the morphisms `Spec(D_0) → Spec(B̂)` and `Spec(D_0) → Spec(B)` are faithfully flat, one deduces that
`B̂` and `B` are also integral and integrally closed `(2.1.13)`. This proves that the ideal `qD_0` is divisorial
(Bourbaki, _Alg. comm._, chap. VII, §1, n° 10, prop. 15) and not contained in `𝔪D_0`, otherwise one would have
`q = (qD_0) ∩ B ⊂ (𝔪D_0) ∩ B = 𝔪B = p` by faithful flatness `(0_I, 6.5.1)`. One concludes that none of the prime ideals
`r_i` of height `1` in `D_0` which contain `qD_0` can be contained in `𝔪D_0`; if one proves that these ideals are
principal, it will follow that `qD_0` is principal, the divisors (in Bourbaki's sense) of `qD_0` and of a product of
powers of the `r_i` being equal (Bourbaki, _Alg. comm._, chap. VII, §1, n° 4, prop. 5). Since `qD_0 ∩ B = q`, one
deduces by faithful flatness that `q` is principal `(2.5.2)`, using the fact that `B` is a local ring.

One is thus reduced to proving the theorem in the particular case where `A` is complete and `B = A[[T_1, …, T_n]]`.
Let us first show that one can reduce to the case where `n = 1`. Indeed, proceed by recurrence on `n`, and let `f ∈ q`
be an element not belonging to `p = 𝔪B`; it will suffice to show that there exists an `A`-automorphism `σ` of `B` such
that `σ(f)` does not belong to the ideal `p' = p + BT_1 + ⋯ + BT_{n−1}`: indeed, if `B' = A[[T_1, …, T_{n−1}]]`, `B'`
is complete and has maximal ideal `𝔪B' + B'T_1 + ⋯ + B'T_{n−1} = 𝔪'`. Since one has `B = B'[[T_n]]` and `p' = 𝔪'B`,
it will follow from the recurrence hypothesis (taking into account that `B'` is integral and integrally closed) that
the ideal `σ(q)` is principal in `B`, hence so is `q`. Now, if `f̄ ∈ k[[T_1, …, T_n]]` is the image of `f` ("reduced
series" of `f`), one knows (Bourbaki, _Alg. comm._, chap. VII, §3, n° 7, lemma 3) that there is an `A`-automorphism
`σ` of `B` such that `(σ(f̄))(0, …, 0, T_n) ≠ 0`, which evidently implies `σ(f) ∉ p'`.

Suppose then `n = 1` and write `T` in place of `T_1`, so that `B = A[[T]]`. It suffices to show that in the polynomial
ring `A[T]`, the ideal `q ∩ A[T]` is principal;

<!-- original page 325 -->

in fact, let `f` be an element of `q` not belonging to `𝔪B`; it is a formal series whose reduced series `f̄_0` is not
zero; hence, by virtue of the preparation theorem (Bourbaki, _Alg. comm._, chap. VII, §3, n° 8, prop. 5), for every
`f ∈ q`, there exist `g ∈ B` and a polynomial `r ∈ A[T]` such that `f = gf + r`, and one has therefore `r ∈ q ∩ A[T]`;
on the other hand (loc. cit., prop. 6) there exist a non-constant distinguished polynomial `F_0 ∈ A[T]` and an
invertible element `u ∈ B` such that `f_0 = uF_0`, hence one also has `F_0 ∈ q ∩ A[T]`, which proves that `q` is
generated by `q ∩ A[T] = q_1`. Since `B` is flat over `A[T]` `(0_I, 7.3.3)`, it follows from Bourbaki, _Alg. comm._,
chap. VII, §1, n° 10, prop. 15, that `q_1` is a prime ideal of height `1` in `A[T]`. Moreover, one has necessarily
`q_1 ∩ A = 0`; otherwise, `q_1 ∩ A` would necessarily be of height `> 1`, and it would follow from `(5.5.3)` that one
would have `q_1 = (q_1 ∩ A)A[T]`. But then, since `q_1 ∩ A ⊂ 𝔪`, one would have `q_1 ⊂ 𝔪A[T]` contrary to the
hypothesis on `q`. If `K` is the field of fractions of `A`, `q_1K[T]` is therefore a prime ideal distinct from `0`
and from `K[T]` in `K[T]`, hence of the form `h·K[T]`, where `h(T) = T^m + a_1 T^{m−1} + ⋯ + a_m` with `m ⩾ 1` and the
`a_i ∈ K`, `h` being irreducible in `K[T]`. But one has seen above that there exists in `q_1` a non-constant
distinguished polynomial `F_0 ∈ A[T]`. If `t` is the class of `T` in `K[T]/q_1K[T]`, `t` is therefore a root of the
polynomial `F_0` in an extension of `K` and consequently `h` divides `F_0` in `K[T]`; but since `h` and `F_0` are
monic, this entails that the coefficients `a_i` of `h` are integral over `A` (Bourbaki, _Alg. comm._, chap. V, §1,
n° 3, prop. 11), hence belong to `A` since `A` is integrally closed. In other words, one has
`h ∈ A[T] ∩ q_1 K[T] = q_1` (Bourbaki, _Alg. comm._, chap. II, §1, n° 5, prop. 11); since every polynomial `g ∈ q_1`
is divisible by `h` in `K[T]` and `h` is monic, the coefficients of `g/h` belong to `A`, hence `q_1 = h·A[T]`. **Q.E.D.**

The statement `(21.14.1)` is equivalent to the following:

**Corollary (21.14.2).**

<!-- label: IV.21.14.2 -->

*Under the hypotheses of `(21.14.1)` on `A`, `B` and `p`, for every prime ideal `q` of `B` not contained in `p = 𝔪B`
and such that `dim(B_q) ⩾ 2`, the ring `B_q` is parafactorial. In particular, if `dim(B ⊗_A k) > 0` (i.e.
`dim B > dim A` (`(0, 19.7.1)` and `(6.1.1)`)), the ring `B` is parafactorial.*

Indeed, one has seen in the proof of `(21.14.1)` that the conditions of the statement entail that `B` is integral and
integrally closed; the equivalence of the statements `(21.14.1)` and `(21.14.2)` then results from `(21.13.15)`
applied to `X = Spec(B)` and `S = {p}`.

**Proposition (21.14.3).**

<!-- label: IV.21.14.3 -->

*Let `S` be a normal prescheme, `f : X → S` a smooth morphism.*

*(i) If `S` is locally Noetherian (hence also `X`), then, for every `x ∈ X` such that `dim(𝒪_{X,x}) ⩾ 2` and such that
`x` is not a maximal point of its fibre `f^{-1}(f(x))`, the ring `𝒪_{X,x}` is parafactorial. Every `1`-codimensional
cycle `Z` on `X` such that `Supp(Z)` contains no irreducible component of a fibre `f^{-1}(s) = X_s`, is locally
principal.*

*(ii) Let `Y` be a closed part of `X` containing no irreducible component of a fibre `X_s`, and such that for every
maximal point `η` of `S`, `Y_η = Y ∩ X_η` is of codimension `⩾ 2` in `X_η`. Then the couple `(X, Y)` is parafactorial.*

Note that the conditions of (ii) are fulfilled if `Y` is a closed part of `X` such that, for every `s ∈ S`,
`Y_s = Y ∩ X_s` is of codimension `⩾ 2` in `X_s`.

To prove `(21.14.3)`, note first that under the hypotheses of (i), if one

<!-- original page 326 -->

sets `Y = {x̄}`, there exists an open neighbourhood `V` of `x` in `X` such that `Y ∩ V` and `V` verify the conditions
of (ii): indeed, it follows from the hypothesis and from `(9.5.3)` that one can take `V` such that `V ∩ Y` contains no
irreducible component of an `X_s`; on the other hand, for every maximal point `η` of `S` such that `Y ∩ X_η ≠ ∅`, the
points of `Y ∩ X_η` are specializations of `x`, hence at such a point `z` one has `dim(𝒪_{X,z}) ⩾ 2` and since
`𝒪_{X_η, z} = 𝒪_{X, z}` (`S` being reduced to the point `η` by virtue of `(2.1.13)`), `Y ∩ X_η` is indeed of
codimension `⩾ 2` in `X_η`. Since the couple `(V, Y ∩ V)` is then parafactorial by virtue of (ii), one concludes from
`(21.13.10)` that the ring `𝒪_{X,x}` is parafactorial, that is to say the first assertion of (i). To prove the
second, one can restrict to the case where `Z = {ξ̄}`, where `ξ ∈ X_η`; since `𝒪_{X,ξ}` is an integrally closed local
ring of dimension `1`, it is a discrete valuation ring and `Z` is therefore principal at the point `ξ`; for every other
point `x` of `Supp(Z)`, one therefore has `dim(𝒪_{X,x}) ⩾ 2` and `x` is not a maximal point of its fibre by
hypothesis, hence `𝒪_{X,x}` is parafactorial. Apply then `(21.13.15)` taking for `S` the set formed by `ξ` and the
maximal points of the fibres of `f`; it is clear that `Z` is principal at the points of `S` since `ξ` is the only point
of `S` belonging to `Supp(Z)`; since on the other hand condition b) of `(21.13.15)` is evidently fulfilled, one
concludes that `Z` is locally principal.

One is therefore reduced to proving (ii). Set `U = X − Y` and let `j : U → X` be the canonical injection.

Since the hypotheses and the conclusion are local on `S` and on `X` by virtue of `(21.13.6, (i))`, one can restrict to
the case where `S` and `X` are affine, `f` being therefore of finite presentation. Since the fibres of `f` are
regular, the hypothesis on `Y` entails that, for every

<!-- original page 327 -->

point `x ∈ Y`, one has `prof(𝒪_{X_{f(x)}, x}) = dim(𝒪_{X_{f(x)}, x}) ⩾ 1`; it follows from `(19.9.8)` that the
canonical homomorphism `𝒪_X → j_*(𝒪_U)` is *injective*. Moreover, replacing `Y` by a larger closed part following the
method of the proof of `(19.9.8)`, and using `(21.13.6, (ii))`, one can suppose that `Y` is defined by an ideal of
finite type of the ring of `X`, hence the open `U = X − Y` is quasi-compact and quasi-separated and the closed set
`Y` is constructible.

To prove (ii), it suffices, for every invertible `𝒪_U`-Module `ℒ` and every point `x ∈ Y` given, to establish the
existence of an open neighbourhood `V` of `x` in `X` such that: 1° the canonical homomorphism
`𝒪_V → (j_V)_*(ℒ | (U ∩ V))` is surjective; 2° there exists an invertible `𝒪_V`-Module `ℒ_V` such that
`ℒ_V | (U ∩ V) = ℒ | (U ∩ V)` (`(21.13.5)` and `(21.13.3)`).

Set `s = f(x)`; we shall see that one can restrict to the case where `S = S_0 = Spec(𝒪_{S,s})`. Let `(S_ν)` be a
fundamental system of affine open neighbourhoods of `s` in `S`, and set `X_ν = f^{-1}(S_ν)`, `Y_ν = Y ∩ X_ν`,
`U_ν = X_ν − Y_ν`, `j_ν : U_ν → X_ν` being the canonical injection; `X_0 = X ×_S S_0` is then projective limit of the
`X_ν`, `(8.1.2, a))`; suppose the proposition true for the morphism `f_0 : X_0 → S_0` and for `Y_0 = Y ∩ X_0`, and set
`U_0 = X_0 − Y_0`, `j_0 : U_0 → X_0` being the canonical injection. The projection `p_ν : X_0 → X_ν` being an affine
morphism, one has `(j_0)_*(ℒ | U_0) = p_ν^*((j_ν)_*(ℒ | U_ν))` `(II, 1.5.2)` and the canonical homomorphism
`ρ_0 : 𝒪_{X_0} → (j_0)_*(ℒ | U_0)` is none other than `p_ν^*(ρ_ν)`, where `ρ_ν : 𝒪_{X_ν} → (j_ν)_*(ℒ | U_ν)` is the
canonical homomorphism; since by hypothesis `ρ_0` is surjective, the same is true of `ρ_ν` for `ν` large enough
`(8.5.7)`. Let on the other hand `ℒ_0` be the invertible `𝒪_{U_0}`-Module restriction of `ℒ`, and note that the
`X_ν` are affine, hence quasi-compact and quasi-separated; since by hypothesis there exists an invertible
`𝒪_{X_0}`-Module `ℒ'_0` such that `ℒ_0 | U_0 = ℒ'_0`, there exists a `ν` large enough and a quasi-coherent
`𝒪_{X_ν}`-Module `ℒ'_ν` of finite presentation such that `ℒ'_0` is isomorphic to `p_ν^*(ℒ'_ν)` `(8.5.2, (ii))`;
moreover `(8.5.5)` one can suppose that `ℒ'_ν` is invertible. Finally, since the `U_ν` are quasi-compact and
quasi-separated and `ℒ_0 | U_0 = ℒ'_0`, there exists `ν` large enough such that `ℒ | U_ν` and `ℒ''_ν = ℒ'_ν | U_ν` are
isomorphic `(8.5.2.5)`.

One is thus reduced to the case where `S = Spec(A)`, `X = Spec(B)`, where `A` is a *local* ring; since `X` is normal
and `f` smooth, `S` is normal `(17.5.7)`, hence `A` is integral and integrally closed. Consider then `A` as inductive
limit of its sub-`ℤ`-algebras of finite type; since the integral closure of such a sub-`ℤ`-algebra is a subring of
`A` and is also a `ℤ`-algebra of finite type `(7.8.3, (ii), (iii) and (vi))`, `A` is filtered inductive limit of the
sub-`ℤ`-algebras of finite type `A_λ` of `A` which are integrally closed rings. By virtue of `(1.8.4.2)`, there exists
an index `λ` and an `A_λ`-algebra of finite type `B_λ` such that `B = B_λ ⊗_{A_λ} A` up to an `A`-isomorphism. Set
`S_λ = Spec(A_λ)`, `X_λ = Spec(B_λ)`; if `p_λ : X → X_λ` is the canonical projection, one can moreover suppose (since
`Y` is constructible) that `Y = p_λ^{-1}(Y_λ)`, where `Y_λ` is a closed part of `X_λ` `(8.3.11)`. Let `f_λ` be the
morphism `X_λ → S_λ`; by virtue of the transitivity of fibres and of `(4.2.6)`, `Y_λ` contains no irreducible
component of the fibres `f_λ^{-1}(s_λ)` for any `s_λ ∈ S_λ`. Since `f` is smooth, one can also suppose that `f_λ` is
smooth `(17.7.8)`; finally, the image of the generic point `η` of `S` in `S_λ` is the generic point `η_λ` of `S_λ`,
and one has `codim((Y_λ)_{η_λ}, (X_λ)_{η_λ}) = codim(Y_η, X_η) ⩾ 2` by virtue of `(6.1.4)`. One sees therefore that
`S_λ`, `X_λ` and `Y_λ` verify all the hypotheses of (ii), and on setting `X_μ = X_λ ×_{S_λ} S_μ` for `λ ⩽ μ`, the
same is true for `S_μ`, `X_μ` and `Y_μ`. Let us show that if one proves that the couple `(X_μ, Y_μ)` is parafactorial
for every `μ ⩾ λ`, the same is true for `(X, Y)`. Indeed, let `U = X − Y`, `U_μ = X_μ − Y_μ`, `j : U → X`,
`j_μ : U_μ → X_μ` the canonical injections; the projection `p_μ : X → X_μ` being an affine morphism, one has
`j_*(𝒪_U) = p_μ^*((j_μ)_*(𝒪_{U_μ}))` `(II, 1.5.2)`, and consequently the canonical homomorphism
`ρ : 𝒪_X → j_*(𝒪_U)` is none other than `p_μ^*(ρ_μ)`, where `ρ_μ : 𝒪_{X_μ} → (j_μ)_*(𝒪_{U_μ})` is the canonical
homomorphism; the latter being bijective by hypothesis, the same is true of `ρ`. On the other hand, for every
invertible `𝒪_U`-Module `ℒ`, there exists `μ ⩾ λ` and an invertible `𝒪_{U_μ}`-Module `ℒ̃` such that
`ℒ ≃ p_μ^*(ℒ̃)` (denoting by `p_μ : U → U_μ` the restriction of `p_μ`) `(8.5.2 and 8.5.5)`, `U_μ` being quasi-compact
since `X_μ` is Noetherian. By hypothesis, there exists an invertible `𝒪_{X_μ}`-Module `ℒ'_μ` such that
`ℒ'_μ | U_μ` is isomorphic to `ℒ̃`; `ℒ' = p_μ^*(ℒ'_μ)` is then an invertible `𝒪_X`-Module such that `ℒ' | U` is
isomorphic to `ℒ`, which proves our assertion.

One is thus reduced to proving (ii) when the ring `A` is a `ℤ`-algebra of finite type integrally closed; since the
local rings `𝒪_{S, y}` of `S` are then excellent integrally closed rings, their completions are also integrally
closed `(7.8.3, (ii), (iii) and (vii))`. To prove that the couple `(X, Y)` is parafactorial, it suffices to show that
for every `x ∈ Y`, the ring `𝒪_{X,x}` is parafactorial `(21.13.10)`. Let `y` be a closed point of `Y_{f(x)}`, which is
a specialization of `x` `(5.1.11)`; if one sets `s = f(x) = f(y)`, `𝒪_{S,s}` has a

<!-- original page 328 -->

integrally closed completion, and `𝒪_{X,y}` is a formally smooth `𝒪_{S,s}`-algebra for the preadic topologies
`(17.5.3)`; since `Y_s` contains no irreducible component of `X_s`, one has `dim(𝒪_{X,y}) > dim(𝒪_{S,s})`
`(17.5.8)`. If `x ≠ η`, one has `dim(𝒪_{X,x}) ⩾ 1`; if on the contrary `y = η`, one has by hypothesis
`dim(𝒪_{X,η}) ⩾ 2`; hence in all cases `dim(𝒪_{X,x}) ⩾ 2`. Moreover, the prime ideal of `𝒪_{X,y}` corresponding to
the point `x` is not contained in `𝔪_y 𝒪_{X,y}` since `Y` contains no irreducible component of `X_s`. Finally, since
`y` is closed in `X_s`, `k(y)` is a finite extension of `k(s)` `(I, 6.4.2)`. In all cases, one can apply to
`A = 𝒪_{S,s}`, `B = 𝒪_{X,y}` and `q = 𝔪_x 𝒪_{X,y}` the result of `(21.14.2)`, which completes the proof.

**Remarks (21.14.4).**

<!-- label: IV.21.14.4 -->

(i) It may be that the statements `(21.14.1)` and `(21.14.2)` remain valid without hypothesis on the residue field of
`B`. Stated with this generality, the result would be equivalent, by virtue of `(21.13.15)` and `(21.13.12.1)`, to the
following: *Let `A` be a Noetherian local ring complete, integral and integrally closed, `B` a Noetherian local ring
which is a formally smooth `A`-algebra, such that `dim(B) > dim(A)`; then `B` is parafactorial.*

(ii) We shall see in chap. VI, by using a "finite descent" technique applied to the morphism
`Y' → Y = Spec(A)`, where `Y'` is the normalization of `Y`, that the conclusion of `(21.14.1)` (or of `(21.14.2)`)
remains valid on replacing the hypothesis that `Â` is integrally closed by the hypothesis that `Â` is reduced provided
that `dim B ⩾ dim A + 2`. If one replaces this last condition by `dim B ⩾ dim A + 3`, one can even suppress the
hypothesis that `Â` is reduced. Similarly, the conclusion of `(21.14.3)` remains valid on replacing the hypothesis
that `X` is normal by the hypothesis that `X` is reduced, provided that `dim(𝒪_{X,x}) ⩾ dim(𝒪_{S,s}) + 2`.

(iii) In chap. III, 3rd part, one proves that if `f : X → S` is a smooth morphism, `Y` a locally constructible closed
part of `X` such that, for every `s ∈ S`, one has (with the notations of `(21.14.3)`) `codim(Y_s, X_s) ⩾ 3`, then the
couple `(X, Y)` is parafactorial (`[41]`, XII, 4.8). This conclusion is no longer valid when one supposes only that
`codim(Y_s, X_s) ⩾ 2` for every `s ∈ S` and when one no longer supposes `X` reduced. For example, let `k` be a field,
`A = k[T]/(T^2)`, algebra of dual numbers over `k`, `S = Spec(A)`, `X = Spec(A[T_1, T_2])` (`T_1, T_2`
indeterminates), so that `X = 𝕍_S^2`, `Y` being the "zero section" of this bundle; if `s` is the unique closed point
of `S`, one has `X_s = 𝕍_k^2` and `Y_s` is the "zero section" of `X_s`. To see that the couple `(X, Y)` is not
parafactorial, it suffices to show that the ring `B = A[T_1, T_2]_𝔪`, where `𝔪` is the ideal `(T_1) + (T_2)` which
defines `Y`, is not parafactorial `(21.13.10)`. Let `B_0 = B_{red}`, and denote `U` and `U_0` the complements of the
closed point in `Spec(B)` and `Spec(B_0)`; arguing as in `(21.13.9)`, one has the exact sequence, extension of
`(21.13.9.1)`

```text
                       Γ(U, 𝒪_U^×) → Γ(U_0, 𝒪_{U_0}^×) → H^1(U_0, 𝒪_{U_0}) → Pic(U) → Pic(U_0).
```

Now, one has `Γ(U, 𝒪_U) = B`, `Γ(U_0, 𝒪_{U_0}) = B_0` since `prof(B) = prof(B_0) = 2` `(5.10.5)`. Moreover
`Pic(U_0) = 0` since `B_0` is factorial, and `H^1(U_0, 𝒪_{U_0}) ≠ 0` `[41, 3, Example III-1]`; since the homomorphism
`B^× → B_0^×` is surjective, one concludes that `Pic(U) ≠ 0`, hence that `B` is not parafactorial.

<!-- original page 329 -->

(iv) The result `(21.14.3)` was first proved by C. Seshadri `[44]` in the particular case where `S` is a normal
algebraic scheme over an algebraically closed field `k` and `X = S ×_k T`, where `T` is a `k`-prescheme algebraic and
smooth over `k`. Seshadri's proof `[44, p. 188-189]` is global in nature and uses the theory of Picard schemes. It
gives moreover (loc. cit.) results such as the following (for which one does not at present possess a proof by local
means). Let `S`, `T` be two preschemes locally of finite type over a field `k`, `X = S ×_k T`, `Z` a `1`-codimensional
cycle on `X` (considered as `S`-prescheme); suppose the following conditions are verified:

1° `S` and `T` are geometrically normal over `k` `(6.7.6)`;

2° For every maximal point `η` of `S`, the `1`-codimensional cycle `Z_η` on the fibre `X_η`, having the same
multiplicity as `Z` at every point of `X_η ∩ X_{(s_η)}`, is locally principal (in other words, is the image of a
divisor of `X_η`, since `X_η` is normal);

3° For every `s ∈ S`, `Z` is principal at the maximal points of the fibre `X_s`.

Then `Z` is locally principal. In other words, `X` being normal `(6.14.1)`, for every `x ∈ X` which is not maximal in
its fibre `X_s` and which belongs to none of the "generic fibres" `X_η` (which implies `dim(𝒪_{X,x}) ⩾ 2` by virtue of
`(6.1.1)`), the local ring `𝒪_{X,x}` is parafactorial, by virtue of `(21.12.15)`.[^21.14.4-seshadri]

[^21.14.4-seshadri]: In fact, in the article cited above, Seshadri supposes that `k` is algebraically closed, `T`
separated and "semi-complete" (i.e. such that `Γ(T, 𝒪_T)` is `k`-isomorphic to `k`) and replaces hypothesis 3° by the
stronger hypothesis that `Supp(Z)` contains none of the fibres `X_s` for `s ∈ S`. But since the statement is local on
`S`, one concludes at once that it suffices to make hypothesis 3°, and this proves that the conclusion (interpreted
as above in terms of the parafactoriality property of the rings `𝒪_{X,x}`) is local on `S` and on `T`, which allows
one to eliminate completely the hypothesis that `T` is "semi-complete" and that `k` is algebraically closed, since
(by passing first to the algebraic closure of `k`) one can suppose first `T` affine, which allows one to embed it as
an open of a projective normal scheme over `k`, to which Seshadri's result applies. Note also that, thanks to this
reduction, it suffices to do Seshadri's proof in the case where `T` is projective (and not only "semi-complete"), a
case in which the Picard scheme theory used by Seshadri is contained in the theory which will be developed in chap. VI
of our Treatise.

### 21.15. Relative divisors

**(21.15.1).** Let `S` be a prescheme, `f : X → S` a flat morphism locally of finite presentation. One has defined in
`(20.6.1)` the sheaf of rings `𝓜_{X/S}` of germs of meromorphic functions on `X` relative to `S`, a subsheaf of
`𝓜_X`; it is clear that the canonical injection `𝒪_X → 𝓜_X` `(20.1.4.1)` sends `𝒪_X` onto a subsheaf of `𝓜_{X/S}`,
with which one identifies it. Let `𝓜_{X/S}^×` be the sheaf (in multiplicative groups) of germs of invertible sections
of `𝓜_{X/S}`; it is therefore a subsheaf of `𝓜_X^×` and contains `𝒪_X^×` as a subsheaf.

**Definition (21.15.2).**

<!-- label: IV.21.15.2 -->

*One calls **sheaf of divisors on `X` relative to `S`**, or **sheaf of divisors on `X` transversal to `f`**, and one
denotes `𝒟iv_{X/S}` the quotient sheaf (of commutative groups) `𝓜_{X/S}^× / 𝒪_X^×`; the sections of this sheaf over
`X` are called **divisors on `X` relative to `S`**, or **divisors on `X` transversal to `f`**; they form a commutative
group denoted `Div(X/S)`.*

It is clear that `𝒟iv_{X/S}` identifies canonically with a subsheaf of `𝒟iv_X`, and consequently `Div(X/S)` with a
subgroup of `Div(X)`, which one again denotes additively.

<!-- original page 330 -->

For every open `U` of `X`, one has `𝓜_{X/S} | U = 𝓜_{U/S}`, hence `𝒟iv_{X/S} | U = 𝒟iv_{U/S}`, and the sheaf
`𝒟iv_{X/S}` is therefore equal to the presheaf `U ↦ Div(U/S)`.

Since `𝓜_{X/S}^×` is a subsheaf of `𝓜_X^×`, the definitions, notations and formulas relating to the divisors of
sections of `𝓜_X` over `X` `(21.1.3)` apply without change to the sections of `𝓜_{X/S}` over `X`.

**(21.15.3).** The structure of sheaf of ordered groups on `𝒟iv_X` `(21.1.6)` induces on the subsheaf `𝒟iv_{X/S}` a
structure of sheaf of ordered groups, for which the sheaf of monoids of germs of positive sections is
`𝒟iv_X^+ ∩ 𝒟iv_{X/S}`, which one denotes `𝒟iv_{X/S}^+`. One has `Γ(X, 𝒟iv_{X/S}^+) = Div^+(X) ∩ Div(X/S)`; one denotes
this submonoid of `Div(X/S)` by `Div^+(X/S)`, and it is formed of elements `⩾ 0` for a structure of ordered group on
`Div(X/S)`. It follows from `(21.1.5.1)` that `𝒟iv_{X/S}^+` is the image in `𝓜_{X/S}^×` of the subsheaf of monoids

<!-- label: IV.21.15.3.1 -->

```text
  (21.15.3.1)             𝒪_X^{+,⋆} = 𝒪_X^⋆ ∩ 𝓜_{X/S}^×.
```

For every open `U` of `X`, `Γ(U, 𝒪_X^{+,⋆})` is the set of sections `t` of `𝒪_X` over `U` such that `t` be regular and
that `1/t` belong to `Γ(U, 𝓜_{X/S})`, which means, with the notations of `(20.6.1)`, that `t ∈ 𝒮_{X/S}(U)`, so that
the sheaf `𝒪_X^{+,⋆}` is none other than the sheaf denoted `𝒮_{X/S}` in `(20.6.1)`. One can therefore write

<!-- label: IV.21.15.3.2 -->

```text
  (21.15.3.2)             𝒟iv_{X/S}^+ = 𝒮_{X/S} \ 𝒪_X^×
```

up to a canonical isomorphism.

**(21.15.3.3).** Let `D ∈ Div^+(X/S)` and consider the closed sub-prescheme `Y(D)` of `X` defined by the Ideal
`𝒥_X(D)` of `𝒪_X` `(21.2.12)`; by virtue of what precedes, for every `x ∈ Y(D)`, there is an open neighbourhood `U`
of `x` in `X` and a section `t ∈ Γ(𝒮_{X/S}(U))` such that `𝒥_X(D) | U = (𝒪_X | U) · t`; since `x ∈ Y(D)`, the image
`t_x` of `t` in `Γ(U ∩ X_{f(x)}, 𝒪_{X_{f(x)}})` belongs to the maximal ideal of `𝒪_{X_{f(x)}, x}`, and moreover, by
definition, for every `s ∈ S`, the image `t_s` of `t` in `Γ(U ∩ X_s, 𝒪_{X_s})` is a regular section. One deduces
therefore from `(11.3.8)` and `(19.2.4)` that the canonical immersion `Y(D) → X` is *transversally regular* relative
to `S` and of codimension `1` at the point `x`. The converse being immediate, one sees that one can identify
canonically the positive divisors on `X` relative to `S` with the closed sub-preschemes `Y` of `X` such that the
canonical injection `Y → X` be a transversally regular immersion relative to `S` and of codimension `1`. We shall
ordinarily make this identification.

**Proposition (21.15.4).**

<!-- label: IV.21.15.4 -->

*Let `D` be a divisor on `X`, `𝒪_X(D)` the corresponding invertible fractional Ideal `(21.2.5)`. For
`D ∈ Div(X/S)`, it is necessary and sufficient that, for every `x ∈ X`, one have
`(𝒪_X(D) ⊗_{𝒪_X} 𝓜_{X/S})_x = 𝓜_{X/S, x}` (or what amounts to the same, that one have
`𝒪_X(D) ⊗_{𝒪_X} 𝓜_{X/S} = 𝓜_{X/S}(𝒪_X(D))`).*

Indeed, to say that `D ∈ Div(X/S)` means that for every `x ∈ X`, there exists an open neighbourhood `U` of `x` and a
section `f ∈ Γ(U, 𝓜_{X/S})` such that `D | U = div_U(f)`; since `𝒪_X(D) | U` is the invertible fractional Ideal
`𝒪_U f`, the proposition follows at once.

<!-- original page 331 -->

**Proposition (21.15.5).**

<!-- label: IV.21.15.5 -->

*Let `D` be a divisor on `X`, `𝒪_X(D)` the invertible fractional Ideal and `s_D` the regular meromorphic section of
`𝒪_X(D)` defined canonically by `D` `(21.2.8 and 21.2.9)`. For `D ∈ Div(X/S)`, it is necessary and sufficient that
`s_D ∈ Γ(X, 𝓜_{X/S}(𝒪_X(D)))`.*

Indeed, if `U` is an open of `X` such that `D | U = div_U(f)`, where `f ∈ Γ(U, 𝓜_X)`, to say that
`s_D ∈ Γ(U, 𝓜_{X/S}(𝒪_X(D)))` means, by virtue of definitions `(20.6.2)`, that `f^{-1} ∈ Γ(U, 𝓜_{X/S})`, whence the
proposition.

The interpretation of divisors on `X` by means of the classes `cl(ℒ, s)` `(21.2.11)` therefore permits the
interpretation of the elements of `Div(X/S)` as the couples (up to isomorphism) `(ℒ, s)` such that `ℒ` be an
invertible `𝒪_X`-Module and that `s` be a meromorphic section of `ℒ` over `X`, regular relative to `S` `(20.6.5, (iii))`.

**Proposition (21.15.6).**

<!-- label: IV.21.15.6 -->

*Let `D` be a divisor on `X` relative to `S`, and suppose that for every `x ∈ X` such that
`prof(𝒪_{X_{f(x)}, x}) = 1`, one has `D_x ⩾ 0` (resp. `D_x = 0`). Then one has `D ⩾ 0` (resp. `D = 0`).*

As in `(21.1.8)`, one can restrict to the case where `D = div(φ)`, where `φ` is a regular meromorphic function
relative to `S`, and everything reduces to seeing that if `D_x ⩾ 0` at every point `x ∈ X` such that
`prof(𝒪_{X_{f(x)}, x}) = 1`, `φ` is everywhere defined in `X`. But this hypothesis means that, if `T = X − dom(φ)`,
one has `prof(𝒪_{X_{f(x)}, x}) ⩾ 2` for every `x ∈ T`, and it suffices, to conclude, to apply `(20.6.6)`.

**(21.15.7).** Let `X'` be a second `S`-prescheme flat and locally of finite presentation over `S`, and let
`g : X' → X` be an `S`-morphism. If the `S`-morphism `g` is flat, one knows `(21.4.5)` that the inverse image by `g`
of every divisor on `X` is defined; if moreover `D ∈ Div(X/S)`, it follows from definition `(21.15.2)` and from
`(20.6.8)` that one has then `g^*(D) ∈ Div(X'/S)`.

**(21.15.8).** Let `X'` be a second `S`-prescheme flat and locally of finite presentation over `S`, and let
`g : X' → X` be a finite and flat `S`-morphism. Note that `g` is then necessarily of finite presentation
`(1.4.3, 1.4.6 and 1.6.3)`, hence `g_*(𝒪_{X'})` is a flat and finite-presentation `𝒪_X`-Module, and consequently
locally free `(2.1.12)`; in other words `g` is a *locally free morphism* `(18.2.7)`; for every `s ∈ S`, the
corresponding morphism `g_s : X'_s → X_s` is therefore also finite and locally free. One deduces then from
`(21.5.2)` and `(20.6.1)` that for every open `U` of `X` and every section `f ∈ Γ(g^{-1}(U), 𝓜_{X'/S})`, the norm
`N_{X'/X}(f)` belongs to `Γ(U, 𝓜_{X/S})`; the reasoning of `(21.5.3)` then proves that for every invertible
`𝒪_{X'}`-Module `ℒ'` and every meromorphic section `u'` of `ℒ'` over `X'`, regular relative to `S`, the norm
`N_{X'/X}(u')` is a meromorphic section of `𝒪_X^{N_{X'/X}(ℒ')}` over `X`, regular relative to `S`. The interpretation
of divisors relative to `S` given in `(21.15.5)` and the definition of the direct image of a divisor `(21.5.5)` then
prove that for every divisor `D' ∈ Div(X'/S)`, one has `g_*(D') ∈ Div(X/S)`.

**(21.15.9).** Consider finally any morphism `S' → S`, and (under the hypotheses of `(21.15.1)`) set
`X' = X ×_S S'`, which is flat and locally of finite presentation over `S'`; if `p : X' → X` is the canonical
projection, one has seen `(20.6.9)` that one has a canonical homomorphism `p^*(𝓜_{X/S}) → 𝓜_{X'/S'}`, which evidently
transforms every section of `𝓜_{X/S}` over an open `U`, regular relative to `S`, into a section of `𝓜_{X'/S'}` over
`p^{-1}(U)`, regular relative to `S'` `(20.6.5, (iii))`; one then concludes from the definition

<!-- original page 332 -->

`(21.15.2)` and from the right-exactness of the functor `p^*`, that the foregoing homomorphism defines by passage to
quotients a canonical homomorphism

<!-- label: IV.21.15.9.1 -->

```text
  (21.15.9.1)             Div(X/S) → Div(X'/S')
```

which evidently transforms the elements of `Div^+(X/S)` into elements of `Div^+(X'/S')`. One sets again
`Div(X'/S') = Div_{X/S}(S')` (resp. `Div^+(X'/S') = Div_{X/S}^+(S')`), and one sees at once that one has thus defined
two contravariant functors

```text
                       𝒟iv_{X/S} : Sch_{/S}^∘ → Ab,        𝒟iv_{X/S}^+ : Sch_{/S}^∘ → Set
```

from the category of `S`-preschemes into that of commutative groups (resp. of sets). One will see later (chap. VI)
important cases where the functor `𝒟iv_{X/S}` is representable `(0_III, 8.1.8)`.

For every divisor `D ∈ Div(X/S)`, the image of `D` by the homomorphism `(21.15.9.1)` is none other than the inverse
image `p^*(D)` (in the sense of `(21.4.2)`): the existence of this inverse image and the preceding assertion are
indeed immediate consequences of `(20.6.5, (iii))` and `(20.6.9)`.

The elements of `Div(X'/S')` are often called, by abuse of language, *"families of divisors on `X` relative to `S`,
parametrized by the `S`-prescheme `S'`"*; this terminology is used especially when one is dealing with positive
divisors.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/34-c4-s21-diviseurs.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-4.pdf, pp. 304-332 -->
