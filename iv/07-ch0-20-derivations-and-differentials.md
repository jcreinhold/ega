<!-- original page 212 -->

## §20. Derivations and differentials

The notions introduced in this section will be taken up in geometric form in chapter IV, §16, and will play an important
role in the study of preschemes. Their importance in the present chapter rests first of all on their connections with
the notion of formally smooth algebra, and notably on theorems `(20.4.9)`, `(20.5.7)`, and `(20.5.12)`, which will be
translated into geometric language in the section of chapter IV devoted to smooth morphisms, and are of constant use in
applications. On the other hand, the differential notions will serve in §22 to prove important regularity criteria which
will play an essential role in the deeper study of Noetherian local rings carried out in §7 of chapter IV.

### 20.1. Derivations and extensions of algebras

**Proposition (20.1.1).**

<!-- label: 0_IV.20.1.1 -->

*Let `A` be a ring (not necessarily commutative), `B`, `E`, `C` `A`-rings, `p : E → C` an `A`-homomorphism whose kernel
`𝔍` is of square zero, `u : B → C` an `A`-homomorphism. Suppose that there exists an `A`-homomorphism `v_0 : B → E` such
that `u` factors as `B →^{v_0} E →^{p} C`. Then the set of `A`-homomorphisms `v : B → E` such that `u = p ∘ v` is
identical to the set of maps `v_0 + D`, where `D : B → 𝔍` is a map satisfying the two following conditions:*

*(i) `D` is a homomorphism of `A`-bimodules.*

*(ii) For every pair of elements `f`, `g` in `B`, one has*

```text
(20.1.1.1)                       D(fg) = f · D(g) + D(f) · g.
```

To say that `p(v(f)) = p(v_0(f))` for `f ∈ B` means that `D(f) = v(f) − v_0(f)` belongs to `𝔍`; writing that
`v(fg) = v(f) v(g)`, one obtains the relation `(20.1.1.1)`, `𝔍` being of square zero, and condition (i) results from the
fact that `v` and `v_0` are `A`-homomorphisms.

If `ρ : A → B` is the structural homomorphism, one derives from `(20.1.1.1)` that
`D(ρ(a) f) = ρ(a) D(f) + D(ρ(a)) f` for every `a ∈ A`; but one must have `D(ρ(a) f) = ρ(a) D(f)` by (i), so, taking
`f = 1`, it follows that

```text
                                D(ρ(a)) = 0     for     a ∈ A;
```

conversely, if `D` is zero on `ρ(A)` and satisfies `(20.1.1.1)`, it also satisfies (i).

**Definition (20.1.2).**

<!-- label: 0_IV.20.1.2 -->

*Given an `A`-ring `B` and an `A`-bimodule `L`, one calls an `A`-derivation of `B` into `L` a map `D : B → L` satisfying
conditions (i) and (ii) of `(20.1.1)`.*

It follows from `(20.1.1.1)` that the kernel of an `A`-derivation `D : B → L` is a sub-`A`-ring of `B`.

One sometimes calls a *derivation of `B` into `L`* a `ℤ`-derivation, that is, an additive map from `B` into `L`
satisfying `(20.1.1.1)`; one has therefore `D(1) = 0` for such a map. If `B` is an algebra over a prime field `P`, every
`ℤ`-derivation of `B` is a `P`-derivation: this is clear from what precedes if `P` is of characteristic `> 0`, and in
the opposite case, the relation `n · n^{−1} = 1` for `n ∈ ℤ` gives

```text
                                       n D(n^{−1}) = 0
```

so `D(n^{−1}) = 0` since `P` is of characteristic `0`.

It follows at once from definition `(20.1.2)` that if `D`, `D'` are two `A`-derivations of `B` into `L`, the same holds
for `D − D'`. In other words, the set of `A`-derivations of `B` into `L` is endowed with a structure of additive group;
this group is denoted `Der_A(B, L)`. If `A` is commutative, `B` a commutative `A`-algebra, and `L` a `B`-module, then,
for every `A`-derivation `D` of `B` into `L` and every `a ∈ A`, `aD` is again an `A`-derivation of `B` into `L`; in
other words, `Der_A(B, L)` is then equipped with a structure of `A`-module.

<!-- original page 213 -->

Proposition `(20.1.1)` is interpreted as follows:

**Corollary (20.1.3).**

<!-- label: 0_IV.20.1.3 -->

*Given two `A`-homomorphisms of `A`-rings `p : E → C`, `u : B → C` the first of which has a kernel `𝔍` of square zero,
the set of `A`-homomorphisms `v : B → E` such that `u = p ∘ v` is empty or is a principal homogeneous space for the
group `Der_A(B, 𝔍)`.*

In particular:

**Corollary (20.1.4).**

<!-- label: 0_IV.20.1.4 -->

*Let `A` be a ring, `C` an `A`-ring, `L` a `C`-bimodule, `E` an `A`-extension of `C` by `L`, `p : E → C` the
augmentation. The map which, to every derivation `D ∈ Der_A(C, L)`, associates the map `x ↦ x + D(p(x))` is an
isomorphism of the group `Der_A(C, L)` onto the group of `A`-equivalences of `E` with itself.*

Apply `(20.1.1)` for `B = E`, `v_0 = 1_E`: the set of `A`-homomorphisms `v : E → E` such that `p ∘ v = p` is identical to
the set of maps `v = 1_E + D'`, where `D' ∈ Der_A(E, L)`. To say that such an `A`-homomorphism `v` is an `A`-equivalence
amounts to saying that `v` reduces to the canonical injection on `L`, or again that `D'(x) = 0` on `L`; but this also
means that `D'` factors as `E → C →^{D} L`, where `D` is an `A`-derivation. Whence the corollary.

For trivial extensions, `(20.1.3)` gives:

**Corollary (20.1.5).**

<!-- label: 0_IV.20.1.5 -->

*Let `A` be a ring, `B`, `C` two `A`-rings, `L` a `C`-bimodule, `u : B → C` an `A`-homomorphism; the map which, to every
derivation `D ∈ Der_A(B, L)`, associates the map `σ : x ↦ (u(x), D(x))` is a bijection onto the set of
`A`-homomorphisms `v : B → D_C(L)` (cf. `(18.2.3)`) such that `u` factors as `B → D_C(L) → C`.*

More particularly:

**Corollary (20.1.6).**

<!-- label: 0_IV.20.1.6 -->

*Let `A` be a ring, `B` an `A`-ring, `L` a `B`-bimodule. If, to every derivation `D ∈ Der_A(B, L)`, one associates: 1° the
`A`-equivalence `(x, y) ↦ (x, y + D(x))` of the extension `D_B(L)` with itself; 2° the `A`-homomorphism
`x ↦ (x, D(x))` of `B` into `D_B(L)`, a right inverse of the augmentation homomorphism `D_B(L) → B`, one defines canonical
bijective correspondences between:*

*(i) the set `Der_A(B, L)`;*

*(ii) the set of `A`-equivalences of `D_B(L)` with itself;*

*(iii) the set of `A`-homomorphisms right inverse to the augmentation homomorphism `D_B(L) → B`.*

It is to be noted that the bijective correspondence thus established between (i) and (ii) respects the group structures,
and that the one deduced from it between (ii) and (iii) is none other than the bijective correspondence already defined
in `(18.3.8)`.

**Corollary (20.1.7).**

<!-- label: 0_IV.20.1.7 -->

*Let `A` be a ring, `C` an `A`-ring, `L` an `A`-bimodule, `E` a trivial `A`-extension of `C` by `L`, `p : E → C` the
augmentation. The set of `A`-derivations `D` of `E` into `L` such that `D(x) = x` on `L` is identical to the set of maps
`x ↦ x − w(p(x))`, where `w` ranges over the set of `A`-homomorphisms right inverse to `p`.*

It again suffices to apply `(20.1.1)` for `B = E`, `v_0 = 1_E`; if `v = 1_E − D`, the condition `D(x) = x` for `x ∈ L` is
equivalent to `v(x) = 0` for `x ∈ L`, that is, to `v = w ∘ p`, where `w : C → E` is an `A`-homomorphism; in addition the
condition `p ∘ v = p` is equivalent to `p ∘ w = 1_C`, in other words to the fact that `w` is a right inverse of `p`.

<!-- original page 214 -->

### 20.2. Functorial properties of derivations

**(20.2.1)** Let `A` be a ring, `B` an `A`-ring, `L` a `B`-bimodule; if `L'` is a second `B`-bimodule and
`w : L → L'` a homomorphism of `B`-bimodules, it is clear that the map `D ↦ w ∘ D` is a homomorphism of additive groups

```text
(20.2.1.1)                  w_0 : Der_A(B, L) → Der_A(B, L')
```

and that if `w' : L' → L''` is a second homomorphism of `B`-bimodules, one has `(w' ∘ w)_0 = w'_0 ∘ w_0`. When `A` is
commutative, `B` a commutative `A`-algebra and `L` a `B`-module, `(20.2.1.1)` is a homomorphism of `A`-modules.

In the second place, let `B'` be an `A`-ring, `v : B' → B` an `A`-homomorphism which makes `L` into a `B'`-bimodule; then
the map `D ↦ D ∘ v` is a homomorphism of additive groups,

```text
(20.2.1.2)                  v^0 : Der_A(B, L) → Der_A(B', L)
```

as follows from `(20.1.1.1)`; if `v' : B'' → B'` is a second `A`-homomorphism, one has `(v ∘ v')^0 = v'^0 ∘ v^0`. When
`A`, `B`, and `B'` are commutative and `L` a `B`-module, `(20.2.1.2)` is a homomorphism of `A`-modules.

Finally, let `u : A' → A` be a ring homomorphism making `B` into an `A'`-ring; every `A`-derivation `D ∈ Der_A(B, L)` is
also an `A'`-derivation, whence a canonical injection of commutative groups

```text
(20.2.1.3)                  u^0 : Der_A(B, L) → Der_{A'}(B, L)
```

and if `u' : A'' → A'` is a second ring homomorphism, one has `(u ∘ u')^0 = u'^0 ∘ u^0`; when `A`, `A'`, and `B` are
commutative and `L` a `B`-module, `(20.2.1.3)` is a di-homomorphism of modules (relative to `u`).

One may further say that

```text
                              (A, B, L) ↦ Der_A(B, L)
```

is a covariant functor from the category `𝒦` defined in `(18.3.5)` to the category `Ab` of commutative groups, by making
correspond, to every triple `(u, v, w)` constituting a morphism of `𝒦`, the homomorphism `w_0 ∘ v^0 ∘ u^0`; the
verification of functoriality follows from the commutativity of the diagrams

```text
       Der_A(B, L) ─────→ Der_A(B', L)       Der_A(B, L) ─────→ Der_{A'}(B, L)
            │                  │                  │                   │
         w_0│               w_0│               w_0│                w_0│
            ↓                  ↓                  ↓                   ↓
       Der_A(B, L') ────→ Der_A(B', L')      Der_A(B, L') ────→ Der_{A'}(B, L')
                                                          u^0
```

for every homomorphism `w : L → L'` of `B`-bimodules.

<!-- original page 215 -->

**Theorem (20.2.2).**

<!-- label: 0_IV.20.2.2 -->

*Let `u : A → B`, `v : B → C` be two ring homomorphisms, `L` a `C`-bimodule. One has a canonical exact sequence of
commutative groups*

```text
(20.2.2.1)   0 → Der_B(C, L) → Der_A(C, L) →^{v^0} Der_A(B, L)
                  →^{∂} Exan_B(C, L) →^{u^1} Exan_A(C, L) →^{v^1} Exan_A(B, L)
```

*where `u^0`, `v^0` are the homomorphisms `(20.2.1.3)` and `(20.2.1.2)` respectively, `u^1`, `v^1` the homomorphisms
defined in `(18.3.4.1)` and `(18.3.3.1)` respectively, and where `∂` is defined as follows: for every `A`-derivation `D`
of `B` into `L`, `∂(D)` is the class of the `B`-extension of `C` by `L` defined on the ring `D_C(L)` by the
`A`-homomorphism `σ : x ↦ (v(x), D(x))` (cf. `(20.1.5)`). Furthermore, the exact sequence `(20.2.2.1)` is functorial in
`L` (for the homomorphisms defined in `(20.2.1.1)` and `(18.3.1.1)` respectively).*

Since `D` is an `A`-derivation (and *a fortiori* a `ℤ`-derivation) of `B` into `L`, the `A`-homomorphism
`σ : x ↦ (v(x), D(x))` does define on `D_C(L)` a structure of `B`-extension, hence `∂(D)` is well defined `(20.1.5)`.
Exactness must be verified at five places:

1) Exactness at `Der_A(C, L)` is trivial (cf. `(20.2.1)`).

2) By definition `(20.2.1)`, the kernel of `v^0` is the set of `A`-derivations of `C` into `L` which vanish on `v(B)`,
that is, those `A`-derivations which are also `B`-derivations `(20.1.1)`; whence exactness at `Der_A(C, L)`.

3) The kernel of `∂` is formed by the derivations `D ∈ Der_A(B, L)` for which the `B`-extension defined by
`σ : x ↦ (v(x), D(x))` is `B`-trivial; this means `(18.2.3)` that there exists a `B`-homomorphism `z ↦ (z, w(z))` from
`C` into `D_C(L)` (the `B`-ring structure on `D_C(L)` being defined by `σ`); but such a homomorphism, being *a fortiori*
an `A`-homomorphism, is of the form `z ↦ (z, D'(z))` where `D' ∈ Der_A(C, L)` `(20.1.6)`; and writing that it is a
`B`-homomorphism gives

```text
            D'(v(x) z) + v(x) D'(z) = D'(v(x)) z + v(x) D'(z) = (D(x) + D'(v(x))) z,
```

for `x ∈ B`, `z ∈ C`, which yields `D'(v(x)) = D(x)`; the kernel of `∂` is therefore the image of `v^0`.

4) The kernel of `u^1` is the set of classes of `B`-extensions of `C` by `L` which are `A`-trivial `(18.3.7)`, so (up to
equivalence) of the form `D_C(L)`, where the `A`-ring structure is defined by the homomorphism `t ↦ (u(t), 0)`. Now
every `B`-extension structure on `D_C(L)` is defined by a homomorphism `σ : x ↦ (v(x), D(x))`, where `D` is a
`ℤ`-derivation of `B` into `L` `(20.1.5)`; to say that the `A`-ring structure of this `B`-extension is deduced from its
`B`-ring structure by means of `u : A → B` means that `D(u(t)) = 0` for `t ∈ A`, hence that `D` is an `A`-derivation,
or again that the class of the `B`-extension considered is of the form `∂(D)`; whence exactness at `Exan_B(C, L)`.

5) The kernel of `v^1` is the set of classes of `A`-extensions `E` of `C` by `L` which become trivial on `v(B)`, that is,
those for which there exists an `A`-homomorphism `w : B → E` such that `v` factors as `B →^{w} E →^{p} C`; but such an
`A`-homomorphism defines on `E` a structure of `B`-extension whose class has as image under `u^1` the class of the given
`A`-extension; the converse being trivial, exactness at `Exan_A(C, L)` is proved.

Finally, functoriality in `L` follows trivially from the definitions.

<!-- original page 216 -->

**Corollary (20.2.3).**

<!-- label: 0_IV.20.2.3 -->

*Let `A`, `B`, `C` be three commutative rings, `u : A → B`, `v : B → C` two ring homomorphisms, `L` a `C`-module. One
has a canonical exact sequence of `A`-modules*

```text
(20.2.3.1)   0 → Der_B(C, L) → Der_A(C, L) →^{v^0} Der_A(B, L) →^{∂}
                  → Exalcom_B(C, L) →^{u^1} Exalcom_A(C, L) →^{v^1} Exalcom_A(B, L)
```

*functorial in `L`.*

The reasoning is the same as in `(20.2.2)` once one has verified that for every derivation `D ∈ Der_A(B, L)`, `∂(D)` is
indeed the class of a `B`-extension of `C` by `L` which is a commutative `B`-algebra; but this follows at once from the
commutativity of `C` and the fact that `L` is a `C`-module.

**Corollary (20.2.4).**

<!-- label: 0_IV.20.2.4 -->

*Under the hypotheses of `(20.2.2)` (resp. `(20.2.3)`), one has a canonical exact sequence, functorial in `L`,*

```text
(20.2.4.1)   0 → Der_B(C, L) → Der_A(C, L) →^{v^0} Der_A(B, L) →^{∂} Exan_{B/A}(C, L) → 0
```

*(resp.*

```text
(20.2.4.2)   0 → Der_B(C, L) → Der_A(C, L) →^{v^0} Der_A(B, L) →^{∂} Exalcom_{B/A}(C, L) → 0).
```

This follows from the definition of `Exan_{B/A}(C, L)` (resp. `Exalcom_{B/A}(C, L)`) (`(18.3.7)` and `(18.4.2)`).

**Remark (20.2.5).**

<!-- label: 0_IV.20.2.5 -->

*Suppose one has a commutative diagram of ring homomorphisms*

```text
                                A ──→ B ──→ C
                                │     │     │
                                ↓     ↓     ↓
                                A' ──→ B' ──→ C'
```

*Then one has a commutative diagram*

```text
0 → Der_B(C, L) → Der_A(C, L) → Der_A(B, L) → Exan_B(C, L) → Exan_A(C, L) → Exan_A(B, L)
        │              │              │             │              │              │
        ↓              ↓              ↓             ↓              ↓              ↓
0 → Der_{B'}(C', L) → Der_{A'}(C', L) → Der_{A'}(B', L) → Exan_{B'}(C', L) → Exan_{A'}(C', L) → Exan_{A'}(B', L)
```

*and likewise for the exact sequences `(20.2.3.1)`, `(20.2.4.1)`, and `(20.2.4.2)`.*

### 20.3. Continuous derivations in topological rings

**(20.3.1)** Given two topological rings `A`, `B` (linearly topologized as always), we denote by `Hom.cont(A, B)` the
set of continuous homomorphisms from `A` to `B`. Given a topological ring `A`, the category of topological `A`-rings is
defined as that of `A`-rings `(18.1.4)` by replacing everywhere "ring" by "topological ring" and "homomorphism" by
"continuous homomorphism"; if `B`

<!-- original page 217 -->

and `C` are two topological `A`-rings, we denote by `Hom.cont_A(B, C)` the set of continuous `A`-homomorphisms from `B`
to `C`.

Let `A` be a topological ring, `B` a topological `A`-ring, `L` a topological `B`-bimodule; we denote by
`Der.cont_A(B, L)` the set of continuous `A`-derivations from `B` into `L`; it is clear that this is a subgroup of
`Der_A(B, L)` (and a sub-`A`-module when `A` and `B` are commutative and `L` is a `B`-module).

**(20.3.2)** It is immediate that proposition `(20.1.1)` remains valid when one replaces in it "ring" by "topological
ring" and "homomorphism" by "continuous homomorphism". Likewise, `(20.1.3)` and `(20.1.4)` remain valid by replacing
`Der` by `Der.cont`, "ring" (resp. "bimodule") by "topological ring" (resp. "topological bimodule"), "homomorphism" by
"continuous homomorphism"; it is naturally necessary to assume in `(20.1.4)` that `p` is continuous, and to replace
"`A`-equivalences" by "continuous `A`-equivalences". One has the same results for `(20.1.5)` and `(20.1.6)`, provided
one takes as topology on `D_C(L)` (resp. `D_B(L)`) the product topology (on `C × L`, resp. `B × L`).

**Proposition (20.3.3).**

<!-- label: 0_IV.20.3.3 -->

*Let `A` be a topological ring, `B` a topological `A`-ring, `L` a discrete topological `B`-bimodule annihilated by an
open two-sided ideal of `B`. If in `B` the square of every open two-sided ideal is open, then one has
`Der.cont_A(B, L) = Der_A(B, L)`.*

Indeed, if `𝔎` is an open two-sided ideal of `B` annihilating `L`, and `D` an `A`-derivation of `B` into `L`, one has
`D(𝔎^2) ⊂ 𝔎 · D(𝔎) + D(𝔎) · 𝔎 = 0` `(20.1.1.1)`, hence `D` is continuous.

**(20.3.4)** All the results of `(20.2.1)` remain valid when one replaces in them "ring" by "topological ring",
"bimodule" by "topological bimodule", "homomorphism" by "continuous homomorphism", and `Der` by `Der.cont`.

**Proposition (20.3.5).**

<!-- label: 0_IV.20.3.5 -->

*Let `A` be a topological ring, `B` a topological `A`-ring, `L` a discrete topological `B`-bimodule annihilated by an
open two-sided ideal of `B`. One has then a canonical isomorphism*

```text
(20.3.5.1)              lim Der_{A/𝔍}(B/𝔎, L) ≅ Der.cont_A(B, L)
```

*where in the left-hand side the inductive limit is taken over the filtered ordered set of pairs `(𝔍, 𝔎)` of two-sided
ideals such that `𝔎 · L = L · 𝔎 = 0`, `𝔍 · B ⊂ 𝔎`, `B · 𝔍 ⊂ 𝔎`.*

Since `A/𝔍` and `B/𝔎` are discrete, one has canonical homomorphisms
`w_{𝔎,𝔍} : Der_{A/𝔍}(B/𝔎, L) → Der.cont_A(B, L)` forming an inductive system `(20.3.4)`, whence the homomorphism
`(20.3.5.1)` by passage to the inductive limit. Since the homomorphism `B/𝔎' → B/𝔎` is surjective for `𝔎 ⊃ 𝔎'`, it
follows at once from the definition that the homomorphism `Der_A(B/𝔎, L) → Der_A(B/𝔎', L)` (with `𝔎 · L = L · 𝔎 = 0`,
`𝔍 · B ⊂ 𝔎'`, `B · 𝔍 ⊂ 𝔎'`) is injective, and it is evidently the same for the homomorphism
`Der_{A/𝔍}(B/𝔎, L) → Der_{A/𝔍'}(B/𝔎, L)` for `𝔍' ⊂ 𝔍` `(20.2.1)`; one concludes that the homomorphism `(20.3.5.1)` is
injective. On the other hand, if `D` is a continuous `A`-derivation of `B` into `L`, its kernel contains an open
two-sided ideal `𝔎` of `B`, and if `𝔍_0` is an open two-sided ideal of `A` such that `𝔍_0 · B ⊂ 𝔎` and `B · 𝔍_0 ⊂ 𝔎`, it
is clear that `D` is the canonical image of an `(A/𝔍_0)`-derivation of `B/𝔎` into `L`, hence `(20.3.5.1)` is surjective.

<!-- original page 218 -->

**Proposition (20.3.6).**

<!-- label: 0_IV.20.3.6 -->

*Let `u : A → B`, `v : B → C` be two continuous homomorphisms of topological rings, `L` a discrete `C`-bimodule
annihilated by an open two-sided ideal of `C`. One has a canonical exact sequence*

```text
(20.3.6.1)   0 → Der.cont_B(C, L) → Der.cont_A(C, L) →^{v^0} Der.cont_A(B, L) →^{∂}
                  → Exantop_B(C, L) →^{u^1} Exantop_A(C, L) →^{v^1} Exantop_A(B, L)
```

*where `∂` is defined by passage to the inductive limit from the homomorphism `∂` of `(20.2.2.1)`; this exact sequence
is functorial in `L` (in the category of `C`-bimodules discrete and annihilated by open two-sided ideals).*

This follows from the exactness of the functor `lim`, starting from `(20.2.2)`.

**Corollary (20.3.7).**

<!-- label: 0_IV.20.3.7 -->

*Let `A`, `B`, `C` be three commutative topological rings, `u : A → B`, `v : B → C` two continuous homomorphisms, `L` a
discrete `C`-module annihilated by an open ideal of `C`. One has a canonical exact sequence of `A`-modules, functorial
in `L`,*

```text
(20.3.7.1)   0 → Der.cont_B(C, L) → Der.cont_A(C, L) →^{v^0} Der.cont_A(B, L) →^{∂}
                  → Exalcotop_B(C, L) →^{u^1} Exalcotop_A(C, L) →^{v^1} Exalcotop_A(B, L).
```

**Corollary (20.3.8).**

<!-- label: 0_IV.20.3.8 -->

*Under the hypotheses of `(20.3.5)` (resp. `(20.3.6)`) one has a canonical exact sequence, functorial in `L`,*

```text
(20.3.8.1)   0 → Der.cont_B(C, L) → Der.cont_A(C, L) →^{v^0} Der.cont_A(B, L) →^{∂}
                                                                  → Exantop_{B/A}(C, L) → 0
```

*(resp.*

```text
(20.3.8.2)   0 → Der.cont_B(C, L) → Der.cont_A(C, L) →^{v^0} Der.cont_A(B, L) →^{∂}
                                                              → Exalcotop_{B/A}(C, L) → 0).
```

We leave to the reader the task of writing the diagrams analogous to those of `(20.2.5)`.

### 20.4. Principal parts and differentials

In the whole sequel of this section and in the three following ones, all rings are assumed to be commutative.

**(20.4.1)** Let `A` be a topological ring, `B` a topological `A`-algebra; the `A`-algebra `B ⊗_A B` will be equipped
with the tensor-product topology, which makes it a topological `A`-algebra; we denote by `p` (or `p_{B/A}`) the
canonical surjective `A`-homomorphism

```text
(20.4.1.1)                             p : B ⊗_A B → B
```

such that `p(b ⊗ b') = bb'`; it is immediate that `p` is continuous. The kernel of `p` will be denoted `𝔍_{B/A}`
(or simply `𝔍` if there is no risk of confusion). We denote by `j_1 : B → B ⊗_A B` and `j_2 : B → B ⊗_A B` the two
canonical `A`-homomorphisms, such that

```text
                              j_1(b) = b ⊗ 1,        j_2(b) = 1 ⊗ b
```

which are continuous.

<!-- original page 219 -->

**Definition (20.4.2).**

<!-- label: 0_IV.20.4.2 -->

*One calls augmented `B`-algebra of principal parts of order `1` of `B` relative to `A` and denotes by `𝒫^1_{B/A}` the
quotient topological `A`-algebra*

```text
(20.4.2.1)                          𝒫^1_{B/A} = (B ⊗_A B) / 𝔍^2
```

*equipped with the structure of `B`-algebra defined by the homomorphism `j_1 : B → 𝒫^1_{B/A}` (deduced from `j_1` by
composition with the canonical homomorphism `B ⊗_A B → 𝒫^1_{B/A}`), and with the augmentation of `B`-algebra
`ε : 𝒫^1_{B/A} → B` (also denoted `ε_{B/A}`) deduced from `p` by passage to the quotient.*

Since `p(b ⊗ 1) = b` by definition, it is clear that `ε` is indeed an augmentation of `B`-algebra.

**Definition (20.4.3).**

<!-- label: 0_IV.20.4.3 -->

*The kernel of the augmentation `ε : 𝒫^1_{B/A} → B`,*

```text
(20.4.3.1)                          Ω^1_{B/A} = 𝔍_{B/A} / (𝔍_{B/A})^2
```

*equipped with the topology induced by that of `𝒫^1_{B/A}`, which makes it a topological `B`-module, is called the
`B`-module of `1`-differentials (or simply of differentials) of `B` relative to `A`.*

It is to be noted that the topology of `Ω_{B/A}` is also the quotient topology of the topology induced on `𝔍_{B/A}` by
that of `B ⊗_A B` (Bourbaki, _Top. gén._, chap. III, 3rd ed., §2, n° 7, prop. 20). If `B` is discrete the same holds
for `Ω_{B/A}`. We denote by `Ω̂_{B/A}` the separated completion of the topological `B`-module `Ω_{B/A}`.

Any topological ring `B` may be regarded as a topological `ℤ`-algebra (`ℤ` being equipped with the discrete topology),
so that one can define the topological `B`-module `Ω_{B/ℤ}`, which is sometimes also called the *`B`-module of absolute
differentials over `B`* and is denoted `Ω_B`. If `B` is a topological algebra over a prime field `P` (discrete), one has
`B ⊗_P B = B ⊗_ℤ B`, hence `Ω_{B/P} = Ω_B`.

**Lemma (20.4.4).**

<!-- label: 0_IV.20.4.4 -->

*Let `A` be a ring, `B` an `A`-algebra. The ideal `𝔍_{B/A}` of `B ⊗_A B` is generated by the elements `1 ⊗ s − s ⊗ 1`,
where `s` ranges over a generating set of the `A`-algebra `B`.*

It is clear that for every `x ∈ B`, one has `x ⊗ 1 − 1 ⊗ x ∈ 𝔍`; on the other hand, for any `x`, `y` in `B`, one has
`x ⊗ y = xy ⊗ 1 + (x ⊗ 1)(1 ⊗ y − y ⊗ 1)`. If `∑ (x_i ⊗ y_i) ∈ 𝔍`, one has by definition `∑ x_i y_i = 0`, so

```text
(20.4.4.1)             ∑ (x_i ⊗ y_i) = ∑ (x_i ⊗ 1)(1 ⊗ y_i − y_i ⊗ 1)
                        i              i
```

which proves that `𝔍` is the ideal generated by the elements `1 ⊗ x − x ⊗ 1`. In addition, if `x = st`, one has

```text
(20.4.4.2)       x ⊗ 1 − 1 ⊗ x = (s ⊗ 1)(t ⊗ 1 − 1 ⊗ t) + (s ⊗ 1 − 1 ⊗ s)(1 ⊗ t)
```

which immediately concludes the proof by induction.

**Proposition (20.4.5).**

<!-- label: 0_IV.20.4.5 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra. The topology of `Ω_{B/A}` is coarser than the topology
deduced from that of `B` (`(19.0.2)`); if in `B` the square of every open ideal is open, these two topologies are
identical.*

The first assertion is trivial, the tensor-product topology on `B ⊗_A B` being coarser than the topology deduced from
that of `B`; *a fortiori* the topology induced on `𝔍 = 𝔍_{B/A}`

<!-- original page 220 -->

by that of `B ⊗_A B` is coarser than the topology on `𝔍` deduced from that of `B`. To prove the second assertion, write
`M ⊗ N`, by abuse of notation, for the sub-module `Im(M ⊗_A N)` for two sub-`A`-modules `M`, `N` of `B`. Using the
relation

```text
(xy) ⊗ z − x ⊗ (yz) = (x ⊗ 1)(1 ⊗ y)(z ⊗ 1 − 1 ⊗ z) = x · (yz ⊗ 1 − 1 ⊗ yz) − x · (y ⊗ 1 − 1 ⊗ y) · z
```

in the `B`-module `B ⊗_A B` (defined by `j_1`), one sees at once, taking `(20.4.4)` into account, that, if `𝔎` is an
ideal of `B`, one has

```text
                  ((𝔎 ⊗ B) + (B ⊗ 𝔎)) ∩ 𝔍 ⊂ (𝔎 ⊗ 𝔎) ∩ 𝔍 + 𝔎 · 𝔍 + 𝔍^2
```

and on the other hand, if `x_i`, `y_i` are elements of `𝔎` such that `∑ (x_i ⊗ y_i) ∈ 𝔍`, it follows from `(20.4.4.1)`
that one has `∑ (x_i ⊗ y_i) ∈ 𝔎 · 𝔍`, so that finally

```text
(20.4.5.1)                  (𝔎 ⊗ B + B ⊗ 𝔎) ∩ 𝔍 ⊂ 𝔎 · 𝔍 + 𝔍^2.
```

Now one has a fundamental system of neighbourhoods of `0` in `𝔍` (for the topology induced by that of `B ⊗_A B`) by
taking as neighbourhoods of `0` the sets `(𝔎 ⊗ B + B ⊗ 𝔎) ∩ 𝔍`, where `𝔎` ranges over the set of open ideals. Since the
topology of `Ω_{B/A}` deduced from that of `B` is also the quotient by `𝔍^2` of the topology of `𝔍` deduced from that of
`B`, the hypothesis on the open ideals of `B` and the relation `(20.4.5.1)` complete the proof of the second assertion.

**Definition (20.4.6).**

<!-- label: 0_IV.20.4.6 -->

*Let `p_1` and `p_2` be the composite maps `B →^{j_1} B ⊗_A B → 𝒫^1_{B/A}`, `B →^{j_2} B ⊗_A B → 𝒫^1_{B/A}`, which are
continuous `A`-homomorphisms such that `ε ∘ p_1 = ε ∘ p_2 = 1_B`. The continuous `A`-homomorphism of `A`-modules*

```text
(20.4.6.1)                          d_{B/A} = p_2 − p_1 : B → Ω_{B/A}
```

*is called the exterior differential of `B` relative to `A`; for every `x ∈ B`, `d_{B/A}(x)` (also denoted `d(x)` or
`dx`) is called the differential of `x` (relative to `A`).*

When `A = ℤ`, one writes `d_B` instead of `d_{B/ℤ}`; if `B` is an algebra over a prime field `P`, one has `d_B = d_{B/P}`.

**Proposition (20.4.7).**

<!-- label: 0_IV.20.4.7 -->

*The `B`-module `Ω_{B/A}` is generated by the elements `d_{B/A}(x)`, where `x` ranges over a system of generators of the
`A`-algebra `B`.*

Since `d_{B/A}(x)` is the canonical image of `x ⊗ 1 − 1 ⊗ x` in `Ω_{B/A}`, the proposition is an immediate consequence
of `(20.4.4)`.

**Theorem (20.4.8).**

<!-- label: 0_IV.20.4.8 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra.*

*(i) There exists a unique isomorphism of augmented topological `B`-algebras*

```text
(20.4.8.1)                          φ : 𝒫^1_{B/A} ≅ D_B(Ω_{B/A})
```

*which reduces to the identity on `Ω_{B/A}`.*

*(ii) The homomorphism `d_{B/A}` is an `A`-derivation of `B` into `Ω_{B/A}`, having the following universal property:
for every topological `B`-module `L`, the map `u ↦ u ∘ d_{B/A}` is an isomorphism of `A`-modules*

```text
(20.4.8.2)              Hom.cont_B(Ω_{B/A}, L) ≅ Der.cont_A(B, L).
```

<!-- original page 221 -->

(i) It is immediate that `φ` (with the notations of `(20.4.6)`) is necessarily the map
`z ↦ (ε(z), z − p_1(ε(z)))`, and the inverse isomorphism is the map `(b, x) ↦ p_1(b) + x`, these two maps being
continuous, which proves the first assertion. It is to be noted that this implies that the topology of `B` is identified
(by `p_1`) with the quotient of the topology of `B ⊗_A B` by `𝔍_{B/A}`.

(ii) The fact that `d_{B/A}` is an `A`-derivation of `B` results from definition `(20.4.6)` and from `(20.1.1)`.

To prove the universal property, recall that `Der.cont_A(B, L)` is canonically identified with the set `𝒢` of continuous
homomorphisms of `A`-algebras `u : B → D_B(L)` such that the composite `B → D_B(L) → B` is the identity (where
`q(b, 0) = b` is the projection; cf. `(20.1.6)` and `(20.3.2)`). On the other hand, thanks to the isomorphism `φ`,
`Hom.cont_B(Ω_{B/A}, L)` is canonically identified with the set of continuous homomorphisms of `B`-algebras
`v : 𝒫^1_{B/A} → D_B(L)` such that the composite `𝒫^1_{B/A} →^{v} D_B(L) → B` is the augmentation `ε`. Since
`p_2 = p_1 − d_{B/A}` by definition, everything reduces to proving that every `u ∈ 𝒢` factors as

```text
                                     B ─────────→ D_B(L)
                                      ↘            ↗
                                    p_1│         v
                                        ↘        ↗
                                          𝒫^1_{B/A}
```

where `v` is a continuous `B`-homomorphism. Now one already has a continuous homomorphism of `A`-algebras
`j : b ↦ (b, 0)` from `B` into `D_B(L)`, which belongs to `𝒢`; by the definition of the topological tensor product of
topological algebras `(0_I, 7.7.6)`, there exists therefore a continuous `A`-homomorphism of algebras
`w : B ⊗_A B → D_B(L)` making commutative the diagram

```text
                                            j_2
                                  B ⊗_A B ──────  B
                                       │           │
                                    w  │           │ u
                                       ↓           ↓
                                  D_B(L) ──────→  B
                                              q
```

One has therefore by definition `w(b ⊗ 1 − 1 ⊗ b) = j(b) − u(b) ∈ L`, and by virtue of `(20.4.4)`, this entails
`w(𝔍) ⊂ L` so that `w(𝔍^2) = 0`; consequently `w` factors as

```text
                              B ⊗_A B → 𝒫^1_{B/A} →^{v} D_B(L)
```

where `v` is a continuous homomorphism of `A`-algebras; moreover, since `v ∘ p_1 = j` is a homomorphism of `B`-algebras,
so is `v` by the definition of the `B`-algebra structure of `𝒫^1_{B/A}`; since one has by definition `u = v ∘ p_2`, this
completes the proof.

**Theorem (20.4.9).**

<!-- label: 0_IV.20.4.9 -->

*Suppose `B` is a formally smooth topological `A`-algebra. Then the topological `B`-module `Ω_{B/A}` is formally
projective.*

Indeed, the hypothesis entails that `B ⊗_A B` (equipped with the structure of topological `B`-algebra defined by `j_1`)
is a formally smooth topological `B`-algebra `(19.3.5, (iii))`, and consequently also a formally smooth topological
`A`-algebra `(19.3.5, (ii))`; since `B` is topologically isomorphic to the quotient `A`-algebra `(B ⊗_A B) / 𝔍` and is a
formally smooth `A`-algebra, the conclusion follows from `(19.5.3)`.

<!-- original page 222 -->

**Corollary (20.4.10).**

<!-- label: 0_IV.20.4.10 -->

*Suppose in addition that in `B` the square of every open ideal is open; then, for every open ideal `𝔎` of `B`,
`Ω_{B/A} / 𝔎 · Ω_{B/A} = Ω_{B/A} / 𝔎 · Ω_{B/A}` is a projective `(B/𝔎)`-module.*

In fact, the topology of `Ω_{B/A}` is then deduced from that of `B` `(20.4.5)`, and it suffices to apply `(19.2.4)`.

**Corollary (20.4.11).**

<!-- label: 0_IV.20.4.11 -->

*Let `A`, `B` be two Noetherian local rings, `ρ : A → B` a local homomorphism making `B` into a formally smooth
topological `A`-algebra (for the preadic topologies). Then, for every ideal of definition `𝔟` of `B`, `Ω_{B/A} / 𝔟 · Ω_{B/A}`
is a free `(B/𝔟)`-module.*

In fact, it follows from `(20.4.10)` that this module is projective, and since `B/𝔟` is an Artinian ring, every
projective `(B/𝔟)`-module is free `(0_III, 10.1.3)`.

**Proposition (20.4.12).**

<!-- label: 0_IV.20.4.12 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra. If the structural homomorphism `A → B` is surjective, one
has `Ω_{B/A} = 0`.*

Indeed, one has `Der_A(B, L) = 0` for every `B`-module `L` by virtue of `(20.1.1)`, and the proposition therefore
follows at once from `(20.4.8)`.

**Examples (20.4.13).**

<!-- label: 0_IV.20.4.13 -->

*(i) Let `A` be a ring, `B = A[X_α]_{α ∈ I}` a polynomial algebra over `A`. Then `Ω_{B/A}` is a free `B`-module, of which
the `dX_α` form a basis.*

Indeed, the `dX_α` generate this `B`-module `(20.4.7)`. On the other hand, if `L` is a free `B`-module having a basis
`(e_α)_{α ∈ I}` indexed by `I`, there exists an `A`-homomorphism `u` of `B` into `D_B(L)` such that
`u(X_α) = (X_α, e_α)` for every `α ∈ I`, hence `(20.1.5)` an `A`-derivation `D` of `B` into `L` such that `D(X_α) = e_α`
for every `α`; by virtue of `(20.4.8.1)`, this proves that the `dX_α` are linearly independent.

*(ii) Let `A` be a ring, `L` an `A`-module, `B` the `A`-algebra `D_A(L)`; then the canonical homomorphism
`x ↦ d_{B/A} x` of `L` into `Ω_{B/A}` is bijective, for it is immediate that the `B`-derivations of `B = D_A(L)` into a
`B`-module `M` are the maps of the form `(b, x) ↦ u(x)`, where `u ∈ Hom_A(L, M)`; one then concludes by
`(20.4.8, (ii))`.

*(iii) Suppose that `B` is the product of two topological `A`-algebras `B_1`, `B_2` (identified with ideals of `B`).
Then the images of `B_1 ⊗_A B_2` and of `B_2 ⊗_A B_1` under the homomorphism `p` `(20.4.1.1)` are zero, whence it
follows at once that `𝒫^1_{B/A}` is identified with the product `𝒫^1_{B_1/A} × 𝒫^1_{B_2/A}`, and that the `B`-module
`Ω_{B/A}` is the (topological) direct sum of the `B`-modules `Ω_{B_1/A}` and `Ω_{B_2/A}` (annihilated respectively by
`B_2` and `B_1`).*

*(iv) Let `A`, `B` be two integral rings such that `A ⊂ B`, `A` is integrally closed, `B` is integral over `A`, and the
field of fractions of `B` is a separable extension of that of `A`. Then the `B`-module `Ω_{B/A}` is a torsion module.*

Indeed, for every `x ∈ B`, the minimal polynomial of `x` with respect to the field of fractions `K` of `A` is a
polynomial `f(T)` belonging to `A[T]`; since `x` is separable over `K`, one has `f'(x) ≠ 0`, and on the other hand one
deduces from the relation `f(x) = 0` that `f'(x) d_{B/A} x = 0`, whence our assertion by virtue of `(20.4.7)`.

**Remarks (20.4.14).**

<!-- label: 0_IV.20.4.14 -->

*(i) It is to be noted that the `B`-module `Ω_{B/A}`, deprived of its topology, is independent of the topologies of `A`
and of `B`.*

*(ii) We shall introduce later the "algebra of principal parts of order `n`" of `B` relative to `A`,
`𝒫^n_{B/A} = (B ⊗_A B) / (𝔍_{B/A})^{n+1}`, which is the basis of "differential calculus of order `n`".*

<!-- original page 223 -->

### 20.5. Fundamental functorial properties of `Ω_{B/A}`

**(20.5.1)** In the whole of this number and the following one, unless expressly stated otherwise, the rings and modules
considered are assumed to be equipped with the discrete topology.

**(20.5.2)** Let `A` be a ring, `B`, `C` two `A`-algebras, `u : B → C` an `A`-homomorphism; one has a commutative diagram

```text
                                  u ⊗ u
                          B ⊗_A B ────── C ⊗_A C
                              │              │
(20.5.2.1)                p_{B/A}         p_{C/A}
                              ↓              ↓
                              B ───────────→ C
                                     u
```

whence by passage to the quotients, an `A`-homomorphism of algebras

```text
(20.5.2.2)                          u' : 𝒫^1_{B/A} → 𝒫^1_{C/A}
```

such that the diagram

```text
                                          u'
                              𝒫^1_{B/A} ────── 𝒫^1_{C/A}
                                  ↑              ↑
                              p_1 │              │ p_1
                                  │              │
                                  B ───────────→ C
                                          u
```

is commutative; since `u ⊗ u` maps `𝔍_{B/A}` into `𝔍_{C/A}`, one obtains, by restricting `u'` to `Ω_{B/A}`, a map

```text
(20.5.2.3)                          u'' : Ω_{B/A} → Ω_{C/A}
```

such that the pair `(u'', u)` is a di-homomorphism for the `B`-module structure of `Ω_{B/A}` and the `C`-module structure
of `Ω_{C/A}`; this last fact allows one to deduce canonically a homomorphism of `C`-modules

```text
(20.5.2.4)                          u_{C/B/A} : Ω_{B/A} ⊗_B C → Ω_{C/A}.
```

In addition, since the diagram

```text
                                          u'
                              𝒫^1_{B/A} ────── 𝒫^1_{C/A}
                                  ↑              ↑
(20.5.2.5)                    p_2 │              │ p_2
                                  │              │
                                  B ───────────→ C
                                          u
```

is also commutative, one deduces that the diagram

<!-- original page 224 -->

```text
                                          u''
                              Ω_{B/A} ────── Ω_{C/A}
                                  ↑              ↑
(20.5.2.6)                  d_{B/A}            d_{C/A}
                                  │              │
                                  B ───────────→ C
                                          u
```

is commutative.

Finally, if `w : C → D` is a second homomorphism of `A`-algebras, one has the transitivity property

```text
(20.5.2.7)              (w ∘ u)_{D/B/A} = w_{D/C/A} ∘ (u_{C/B/A} ⊗ 1)
```

as follows from the definition.

**(20.5.3)** Let now `A`, `B` be two rings, `v : A → B` a ring homomorphism, `C` a `B`-algebra which becomes an
`A`-algebra by means of `v`; then the canonical map `v_0 : C ⊗_A C → C ⊗_B C` is a surjective di-homomorphism of algebras
(relative to `v : A → B`) such that the diagram

```text
                                          v_0
                                 C ⊗_A C ────── C ⊗_B C
                                     │              │
(20.5.3.1)                       p_{C/A}        p_{C/B}
                                     ↓              ↓
                                     C ───────────→ C
                                              1_C
```

is commutative; by passage to the quotients, one deduces a di-homomorphism of algebras

```text
(20.5.3.2)                          v' : 𝒫^1_{C/A} → 𝒫^1_{C/B}
```

such that the diagram

```text
                                          v'
                              𝒫^1_{C/A} ────── 𝒫^1_{C/B}
                                  ↑              ↑
                              p_1 │              │ p_1
                                  │              │
                                  C ───────────→ C
                                          1_C
```

is commutative. Since `v_0` maps `𝔍_{C/A}` into `𝔍_{C/B}` one obtains, by restricting `v'` to `Ω_{C/A}`, a map

```text
(20.5.3.3)                          v_{C/B/A} : Ω_{C/A} → Ω_{C/B}
```

which is a homomorphism of `C`-modules.

<!-- original page 225 -->

In addition, since the diagram

```text
                                          v'
                              𝒫^1_{C/A} ────── 𝒫^1_{C/B}
                                  ↑              ↑
(20.5.3.4)                    p_2 │              │ p_2
                                  │              │
                                  C ───────────→ C
                                          1_C
```

is also commutative, one deduces that the diagram

```text
                                       v_{C/B/A}
                                Ω_{C/A} ─────── Ω_{C/B}
                                  ↑                ↑
(20.5.3.5)                   d_{C/A}            d_{C/B}
                                  │                │
                                  C ─────────────→ C
                                          1_C
```

is commutative.

Finally, if `s : A' → A` is a second ring homomorphism, one has the transitivity property

```text
(20.5.3.6)                  (v ∘ s)_{C/B/A'} = v_{C/B/A} ∘ s_{C/A/A'}.
```

**(20.5.4)** If one now has a commutative diagram of ring homomorphisms

```text
                                  B ───── B'
                                  ↑         ↑
                                  │         │
                                  A ───── A'
                                       u
```

one deduces from `(20.5.2.4)` and `(20.5.3.3)`, by composition, a homomorphism of `B'`-modules

```text
(20.5.4.1)                          Ω_{B/A} ⊗_B B' → Ω_{B'/A'}
```

such that the diagram of `A'`-homomorphisms

```text
                                  Ω_{B/A} ⊗ 1
                              Ω_{B/A} ──────────→ Ω_{B'/A'}
                                  ↑                  ↑
(20.5.4.2)                  d_{B/A} ⊗ 1            d_{B'/A'}
                                  │                  │
                                  B ────────────────→ B'
                                            1_{B'}
```

is commutative.

The homomorphism `(20.5.4.1)` corresponds moreover to a di-homomorphism of `B`-modules

```text
(20.5.4.3)                          Ω_{B/A} → Ω_{B'/A'}.
```

**Proposition (20.5.5).**

<!-- label: 0_IV.20.5.5 -->

*If `A'`, `B` are two `A`-algebras and `B' = B ⊗_A A'`, the canonical homomorphism `(20.5.4.1)`*

```text
(20.5.5.1)                          Ω_{B/A} ⊗_B B' → Ω_{B'/A'}
```

*is bijective.*

<!-- original page 226 -->

The left-hand side of `(20.5.5.1)` is then nothing other than `Ω_{B/A} ⊗_A A'`. One may write
`B' ⊗_{A'} B' = (B ⊗_A B) ⊗_A A'` up to a canonical isomorphism, and `𝔍_{B'/A'}` is then identified with
`𝔍_{B/A} ⊗_A A'`; consequently (since `p` is surjective) `𝒫^1_{B'/A'} = (𝒫^1_{B/A}) ⊗_A A'` and
`Ω_{B'/A'} = Ω_{B/A} ⊗_A A'`, whence `Ω_{B'/A'} ≅ Ω_{B/A} ⊗_A A'` up to a canonical isomorphism, which carries the
augmentation ideals into themselves; since the `A`-module `𝒫^1_{B/A}` is canonically identified with the direct sum of
`B` and `Ω_{B/A}`, one has

```text
(20.5.5.2)                          Ω_{B/A} ⊗_A A' ≅ Ω_{B'/A'}
```

by the same isomorphism, and one verifies at once that the composite of this isomorphism and of the canonical
isomorphism `Ω_{B/A} ⊗_B B' ≅ Ω_{B/A} ⊗_A A'` is none other than `(20.5.5.1)`.

**(20.5.6)** The canonical homomorphisms `(20.5.2.4)` and `(20.5.3.3)` give, by functoriality, for every `C`-module `L`,
canonical homomorphisms

```text
(20.5.6.1)              Hom_C(Ω_{C/A}, L) → Hom_C(Ω_{B/A} ⊗_B C, L) = Hom_B(Ω_{B/A}, L)
(20.5.6.2)              Hom_C(Ω_{C/B}, L) → Hom_C(Ω_{C/A}, L).
```

Taking `(20.4.8.2)` and the commutative diagrams `(20.5.2.6)` and `(20.5.3.5)` into account, these homomorphisms are
none other (up to canonical identification) than the homomorphisms `(20.2.1.2)` and `(20.2.1.3)` respectively.

**Theorem (20.5.7).**

<!-- label: 0_IV.20.5.7 -->

*Let `u : A → B`, `v : B → C` be two ring homomorphisms.*

*(i) The sequence of `C`-modules*

```text
(20.5.7.1)         Ω_{B/A} ⊗_B C →^{u_{C/B/A}} Ω_{C/A} →^{v_{C/B/A}} Ω_{C/B} → 0
```

*is exact.*

*(ii) For `v_{C/B/A}` to be left-invertible, it is necessary and sufficient that `C` be a formally smooth `B`-algebra
relative to `A` (for the discrete topologies (cf. `(19.9.1)`)); in particular, it suffices for this that `C` be a
formally smooth `B`-algebra (for the discrete topologies).*

(i) The exactness of the sequence `(20.2.4.2)` shows first of all, taking `(20.5.6)` into account, that the sequence

```text
                  0 → Hom_C(Ω_{C/B}, L) → Hom_C(Ω_{C/A}, L) → Hom_B(Ω_{B/A}, L)
```

is exact for every `C`-module `L`. One knows that this implies the exactness of the sequence `(20.5.7.1)`
(Bourbaki, _Alg._, chap. II, 3rd ed., §2, n° 1, th. 1).

(ii) By virtue of the exactness of `(20.5.7.1)`, to say that `v_{C/B/A}` is left-invertible means that the sequence

```text
(20.5.7.2)              0 → Ω_{B/A} ⊗_B C → Ω_{C/A} → Ω_{C/B} → 0
```

is exact *and split*; one knows (Bourbaki, _loc. cit._, n° 1, prop. 1) that this is equivalent to saying that for every
`C`-module `L`, the sequence

```text
              0 → Hom_C(Ω_{C/B}, L) → Hom_C(Ω_{C/A}, L) → Hom_B(Ω_{B/A}, L) → 0
```

is exact; taking `(20.5.6)` and `(20.2.4.2)` into account, this condition is equivalent to
`Exalcom_{B/A}(C, L) = 0` for every `C`-module `L`, and the conclusion therefore follows from `(19.9.8.1)`.

<!-- original page 227 -->

Let us note moreover that if one has a commutative diagram of ring homomorphisms

```text
                              A' ───→ B' ───→ C'
                                ↑        ↑       ↑
                                │        │       │
                                A ────→ B ────→ C
```

one deduces a commutative diagram

```text
(20.5.7.3)
        Ω_{B/A} ⊗_B C ────────→ Ω_{C/A} ─────→ Ω_{C/B} ────→ 0
              │                      │              │
              ↓                      ↓              ↓
        Ω_{B'/A'} ⊗_{B'} C' ──→ Ω_{C'/A'} ───→ Ω_{C'/B'} ──→ 0
```

where the vertical arrows come from the di-homomorphisms `(20.5.4.3)`.

**Corollary (20.5.8).**

<!-- label: 0_IV.20.5.8 -->

*Suppose that the homomorphism `v : B → C` makes `C` a formally étale `B`-algebra (for the discrete topologies
`(19.10.2)`); then the homomorphism `(20.5.3.3)`*

```text
                                  u_{C/B/A} : Ω_{B/A} ⊗_B C → Ω_{C/A}
```

*is bijective.*

Indeed, if `C` is a formally unramified `B`-algebra for the discrete topologies, it follows from `(19.10.4)`,
`(20.4.8)`, and `(20.1.1)` that one has `Hom_C(Ω_{C/B}, L) = 0` for every `C`-module `L`, hence `Ω_{C/B} = 0`
(cf. `(20.7.4)`); on the other hand, if `C` is a formally smooth `B`-algebra for the discrete topologies, the sequence
`(20.5.7.2)` is exact; whence the corollary.

**Corollary (20.5.9).**

<!-- label: 0_IV.20.5.9 -->

*Let `A` be a ring, `B` an `A`-algebra, `S` a multiplicative subset of `B`; then the canonical homomorphism*

```text
(20.5.9.1)                          S^{−1} Ω_{B/A} → Ω_{S^{−1} B / A}
```

*is bijective.*

It suffices to apply `(20.5.8)` to `C = S^{−1} B`, which is a formally étale `B`-algebra for the discrete topologies
`(19.10.3, (ii))`.

Taking `(20.5.5)` into account, one may therefore write

```text
(20.5.9.2)                  Ω_{S^{−1} B / S^{−1} A} = S^{−1} Ω_{B/A} = Ω_{S^{−1} B / A},
```

up to canonical isomorphisms.

**Corollary (20.5.10).**

<!-- label: 0_IV.20.5.10 -->

*If `k` is a field and `K = k(X_α)_{α ∈ I}` a purely transcendental extension of `k`, the `dX_α` form a basis of the
`K`-vector space `Ω_{K/k}`.*

Since `K` is the field of fractions of the polynomial ring `k[X_α]_{α ∈ I}`, this follows from `(20.4.13, (i))` and
from `(20.5.9)`.

<!-- original page 228 -->

**(20.5.11)** Let `A` be a ring, `B` an `A`-algebra, `𝔎` an ideal of `B`, `C` the quotient `A`-algebra `B/𝔎`, and
consider the composite homomorphism of `A`-modules

```text
(20.5.11.1)                         𝔎 → B →^{d} Ω_{B/A}
```

where the first arrow is the canonical injection; since `d(xy) = x dy + y dx`, one sees that
`d(𝔎^2) ⊂ 𝔎 · Ω_{B/A}`, whence, by passage to the quotients, a homomorphism of `A`-modules

```text
(20.5.11.2)                 δ_{C/B/A} : 𝔎/𝔎^2 → Ω_{B/A} ⊗_B C = Ω_{B/A} / 𝔎 · Ω_{B/A}.
```

But in fact, `δ_{C/B/A}` is a homomorphism of `C`-modules, for `x ∈ B` and `y ∈ 𝔎`, one has
`y dx ∈ 𝔎 · Ω_{B/A}`, so `d(xy) ≡ x dy` (mod `𝔎 · Ω_{B/A}`), which first proves that `(20.5.11.2)` is a homomorphism of
`B`-modules, and since `𝔎` annihilates both sides, this establishes our assertion.

If `B'` is a second `A`-algebra, `u : B → B'` an `A`-homomorphism, `𝔎'` an ideal of `B'` such that `u(𝔎) ⊂ 𝔎'`, and
`C' = B'/𝔎'` the quotient algebra, one has a commutative diagram

```text
                                         δ
                                 𝔎/𝔎^2 ─────→ Ω_{B/A} ⊗_B C
                                    │                │
(20.5.11.3)                         ↓                ↓
                                 𝔎'/𝔎'^2 ────→ Ω_{B'/A'} ⊗_{B'} C'
                                         δ_{C'/B'/A}
```

where the vertical arrows come from `u` `(20.5.2.4)`.

**Theorem (20.5.12).**

<!-- label: 0_IV.20.5.12 -->

*Let `A` be a ring, `B` an `A`-algebra, `C` the quotient `A`-algebra `B/𝔎`, `u : B → C` the canonical homomorphism.*

*(i) One has an exact sequence of `C`-modules*

```text
(20.5.12.1)              𝔎/𝔎^2 →^{δ_{C/B/A}} Ω_{B/A} ⊗_B C →^{u_C} Ω_{C/A} → 0
```

*where `u_{C/B/A}` and `δ_{C/B/A}` are defined by `(20.5.2.4)` and `(20.5.11.2)` respectively.*

*(ii) If one sets `E = B/𝔎^2`, the canonical homomorphism `(20.5.2.4)`*

```text
                                  Ω_{B/A} ⊗_B C → Ω_{E/A} ⊗_E C
```

*is bijective.*

*(iii) The three following conditions are equivalent:*

*a) `δ_{C/B/A}` is left-invertible.*

*b) Every `A`-extension of `C` by a `C`-module `L`, whose inverse image under `u : B → C` is `A`-trivial, is itself
`A`-trivial.*

*c) The `A`-algebra `E = B/𝔎^2` is an `A`-trivial extension of `C` by `𝔎/𝔎^2`.*

<!-- original page 229 -->

*(iv) There is a canonical bijective correspondence between the left inverses of `δ_{C/B/A}` and the right inverses of
the canonical homomorphism `E → C`.*

(i) Since `u` is surjective, one has `Der_A(C, L) = 0` for every `C`-module `L` by virtue of `(20.1.1)`. The exact
sequence `(20.2.3.1)` therefore becomes

```text
(20.5.12.2)         0 → Der_A(B, L) →^{∂} Exalcom_B(C, L) →^{u^1} Exalcom_A(C, L) →^{v^1} Exalcom_A(B, L)
```

where `v` is the homomorphism `A → B`. Recall on the other hand `(18.3.8)` that `Exalcom_B(C, L)` is canonically
identified with `Hom_C(𝔎/𝔎^2, L)`; one therefore deduces from `(20.5.12.2)` and `(20.4.8)` the exact sequence

```text
(20.5.12.3)         0 → Hom_C(Ω_{C/A}, L) → Hom_C(Ω_{B/A} ⊗_B C, L) →^{φ} Hom_C(𝔎/𝔎^2, L) → Ker(ψ) → 0
```

with `φ = η ∘ ∂^{−1}` and `ψ = v^1 ∘ η^{−1}`. Going back to the definitions of `∂` `(20.2.2)` and of `η` `(18.3.8)`, one
sees at once that `φ` is precisely the homomorphism `Hom(δ_{C/B/A}, 1_L)`. The existence of the exact sequence formed by
the first four terms of `(20.5.12.3)` shows therefore that the sequence `(20.5.12.1)` is exact (Bourbaki, _Alg._, chap.
II, 3rd ed., §2, n° 1, th. 1).

(ii) Apply to `B` and to the ideal `𝔎^2` the exact sequence `(20.5.12.1)`, which gives

```text
(20.5.12.4)                         𝔎^2/𝔎^4 → Ω_{B/A} ⊗_B E → Ω_{E/A} → 0
```

whence, tensoring with `C` (considered as `E`-algebra), the exact sequence

```text
                              𝔎^2/𝔎^4 ⊗_E C → Ω_{B/A} ⊗_B C → Ω_{E/A} ⊗_E C → 0.
```

Now, if `x`, `y` are two elements of `𝔎`, and `ξ` the class of `xy` mod `𝔎^4`, the image `δ'(ξ ⊗ 1)` is by definition
`d_{B/A}(xy) ⊗ 1 = (x d_{B/A}(y) + y d_{B/A}(x)) ⊗ 1`, but since the images of `x` and of `y` in `C` are zero, one also
has `d_{B/A}(xy) ⊗ 1 = 0` in `Ω_{B/A} ⊗_B C`, which proves our assertion.

(iii) To say that `δ_{C/B/A}` is left-invertible amounts, taking the exactness of `(20.5.12.1)` into account, to saying
that the sequence

```text
(20.5.12.5)             0 → 𝔎/𝔎^2 →^{δ_{C/B/A}} Ω_{B/A} ⊗_B C →^{u_{C/B/A}} Ω_{C/A} → 0
```

is exact *and split*, and it amounts to the same (Bourbaki, _loc. cit._) to say that `Ker(ψ) = 0` in the exact sequence
`(20.5.12.3)` for every `L`, which shows the equivalence of conditions a) and b) (cf. `(18.3.6.2)`).

The fact that b) implies c) comes from the fact that the inverse image under `u : B → C` of the `A`-extension `E` of `C`
by `𝔎/𝔎^2` is `A`-trivial, `u` being composed of the canonical homomorphisms `B → E → C` `(18.1.6)`. Conversely, c)
implies b), for every `B`-extension of `C` by `L` is `B`-equivalent to `E ⊕_𝔎 L` `(18.3.8)`, in other words its class is
the image of the class of `E` (considered as `B`-extension) under the homomorphism

<!-- original page 230 -->

`w_* : Exan_B(C, 𝔎/𝔎^2) → Exan_B(C, L)` corresponding to a `B`-homomorphism `w : 𝔎/𝔎^2 → L`. The fact that c) implies b)
then follows from the commutativity of the diagram `(18.3.6.5)`

```text
                              Exan_B(C, 𝔎/𝔎^2) ─^{w_*}→ Exan_B(C, L)
                                    │                          │
                                    ↓                          ↓
                              Exan_A(C, 𝔎/𝔎^2) ─────────→ Exan_A(C, L)
```

(iv) One saw `(20.1.7)` that the right inverses of `E → C` correspond canonically and bijectively to the set of elements
`D ∈ Der_A(E, 𝔎/𝔎^2)` such that `D(x) = x` on `𝔎/𝔎^2`, hence also, by `(20.4.8)`, to the set of `E`-homomorphisms
`h : Ω_{E/A} → 𝔎/𝔎^2` such that the composite `𝔎/𝔎^2 →^{d} Ω_{E/A} →^{h} 𝔎/𝔎^2` is the identity. By tensorization with
`C`, one deduces (since `𝔎/𝔎^2` is a `C`-module) that the composite

```text
                              𝔎/𝔎^2 →^{d ⊗ 1} Ω_{E/A} ⊗_E C →^{h ⊗ 1} 𝔎/𝔎^2
```

is the identity; now, since `𝔎/𝔎^2` is a `C`-module, `h ↦ h ⊗ 1` is an isomorphism from the set
`Hom_E(Ω_{E/A}, 𝔎/𝔎^2)` onto `Hom_C(Ω_{E/A} ⊗_E C, 𝔎/𝔎^2)`; and on the other hand (ii) proves that one can canonically
identify `Ω_{E/A} ⊗_E C` and `Ω_{B/A} ⊗_B C`, `δ_{C/E/A}` being then identified with `δ_{C/B/A}`. *Q.E.D.*

**Example (20.5.13).**

<!-- label: 0_IV.20.5.13 -->

*Let `B = A[X_α]_{α ∈ I}` be a polynomial algebra over `A`, `𝔎` an ideal of `B`, `(P_λ)` a system of generators of `𝔎`
and `C = B/𝔎`; one knows that `Ω_{B/A}` is a free `B`-module of which the `dX_α` form a basis `(20.4.13, (i))`, hence
the `dX_α` also form a basis of the free `C`-module `Ω_{B/A} ⊗_B C`. On the other hand, it follows at once from the
definition that the image of `𝔎/𝔎^2` under `δ_{C/B/A}` is the sub-`C`-module generated by the*

```text
                              dP_λ = ∑ (∂P_λ / ∂X_α) dX_α.
                                     α
```

*One concludes that `Ω_{C/A}` is isomorphic to the quotient of the free `C`-module having the `dX_α` as basis, by the
sub-`C`-module generated by the `dP_λ`, which gives a description of a module of differentials of an arbitrary algebra,
every `A`-algebra `C` being obtainable in the preceding way.*

**Corollary (20.5.14).**

<!-- label: 0_IV.20.5.14 -->

*If `C` is a formally smooth `A`-algebra (for the discrete topologies), the sequence*

```text
(20.5.14.1)         0 → 𝔎/𝔎^2 →^{δ_{C/B/A}} Ω_{B/A} ⊗_B C →^{u_{C/B/A}} Ω_{C/A} → 0
```

*is exact and split.*

In fact, every `A`-extension of `C` by a `C`-module is then trivial `(19.4.4.1)`.

<!-- original page 231 -->

**Remark (20.5.15).**

<!-- label: 0_IV.20.5.15 -->

*Let `u : A → B` be a surjective homomorphism of rings; then, for every ring homomorphism `v : B → C`, the canonical
homomorphism*

```text
(20.5.15.1)                         v_{C/B/A} : Ω_{C/A} → Ω_{C/B}
```

*is bijective; this follows in fact from the exact sequence `(20.5.7.1)`, since `Ω_{B/A} = 0` `(20.4.12)`.*

<!-- original page 136 -->

### 20.6. Imperfection modules and characteristic homomorphisms

**Definition (20.6.1).**

<!-- label: 0_IV.20.6.1 -->

*Given two ring homomorphisms `u : A → B`, `v : B → C`, the **imperfection module** of the `B`-algebra `C` relative to `A`,
denoted `Υ_{C/B/A}`, is the `C`-module kernel of the homomorphism `v_{C/B/A} : Ω^1_{B/A} ⊗_B C → Ω^1_{C/A}`.*

One thus has by definition (cf. `(20.5.7)`) the exact sequence

```text
  (20.6.1.1)   0 → Υ_{C/B/A} → Ω^1_{B/A} ⊗_B C  ──v_{C/B/A}──▸  Ω^1_{C/A}  ──u_{C/B/A}──▸  Ω^1_{C/B}  → 0.
```

When `A = ℤ` (so that the modules `Ω^1_B` and `Ω^1_C` are the "absolute" differential modules `Ω^1_B` and `Ω^1_C`), we
write `Υ_{C/B}` in place of `Υ_{C/B/ℤ}`. When `B` and `C` are algebras over a prime field `P`, one has
`Υ_{C/B/P} = Υ_{C/B}`.

Let `R`, `S` be multiplicative subsets of `B` and `C` respectively, such that the image of `R` is contained in `S`. It
then follows from the exact sequence `(20.6.1.1)` and from `(20.5.9)` that

```text
  (20.6.1.2)   Υ_{S⁻¹C / R⁻¹B / A}  =  S⁻¹ Υ_{C/B/A}.
```

**Proposition (20.6.2).**

<!-- label: 0_IV.20.6.2 -->

*If `C` is a `B`-algebra formally smooth relative to `A` (and in particular if `C` is a formally smooth `B`-algebra),
then `Υ_{C/B/A} = 0`.*

This follows from `(20.5.7, (ii))`.

**Proposition (20.6.3).**

<!-- label: 0_IV.20.6.3 -->

*Let `k` be a field, `K` an extension of `k`. For `K` to be a separable extension of `k`, it is necessary and sufficient
that `Υ_{K/k} = 0` (in other words, that the canonical homomorphism `Ω^1_k ⊗_k K → Ω^1_K` be injective, or equivalently
`(20.4.8)`, that every derivation of `k` into `K` extend to a derivation of `K` into itself).*

Indeed, it is equivalent to say that `K` is separable over `k` or a formally smooth `k`-algebra `(19.6.1)`. On the other
hand, if `P` is the prime field of `k`, then `K` is separable over `P`, hence a formally smooth `P`-algebra, so it
amounts to the same to say that `K` is a formally smooth `k`-algebra or a `k`-algebra formally smooth relative to `P`.
Finally, to say that `K` is a `k`-algebra formally smooth relative to `P` is equivalent, by `(20.5.7, (ii))`, to saying
that the homomorphism `v_{K/k/P} : Ω^1_k ⊗_k K → Ω^1_K` is left-invertible; but since `K` is a field, this last
condition is equivalent to saying that the kernel of `v_{K/k/P}`, that is to say `Υ_{K/k}`, is zero.

**(20.6.4)** Consider a commutative diagram

```text
                  u'      v'
            A' ────▸ B' ────▸ C'
            ▴        ▴        ▴
            │f       │g       │h
  (20.6.4.1)│        │        │
            A ────▸  B ────▸  C
                u       v
```

of homomorphisms of commutative rings. The commutativity of the corresponding diagram `(20.5.7.3)` entails the existence
of a unique `C`-homomorphism

```text
  (20.6.4.2)   Υ_{C/B/A} → Υ_{C'/B'/A'}
```

canonically deduced from `(20.6.4.1)` and making commutative the diagram

```text
                                   v_{C/B/A}             u_{C/B/A}
   0 → Υ_{C/B/A}   →  Ω^1_{B/A} ⊗_B C  ──────────▸  Ω^1_{C/A}  ──────────▸  Ω^1_{C/B}   → 0
       │                │                            │                       │
       ▾                ▾                            ▾                       ▾
  (20.6.4.3)
   0 → Υ_{C'/B'/A'} →  Ω^1_{B'/A'} ⊗_{B'} C'  ──▸   Ω^1_{C'/A'}  ──▸        Ω^1_{C'/B'} → 0
                                       v_{C'/B'/A'}              u_{C'/B'/A'}
```

The datum of the homomorphism `(20.6.4.2)` is moreover equivalent to that of a `C'`-homomorphism

```text
  (20.6.4.4)   Υ_{C/B/A} ⊗_C C' → Υ_{C'/B'/A'}
```

which, composed with the canonical homomorphism `Υ_{C/B/A} → Υ_{C/B/A} ⊗_C C'`, recovers `(20.6.4.2)`. It is clear that
`(20.6.4.2)` enjoys an evident transitivity property, allowing one to say that `Υ_{C/B/A}` is a *functor* in the triple
`(A, B, C)`.

**(20.6.5)** It will be convenient for the sequel, under the conditions of `(20.6.1)`, to introduce a (chain) *complex
of `C`-modules* `K_•(C/B/A)` whose terms vanish except in degrees `0` and `1`, where we take

```text
                          K_0(C/B/A) = Ω^1_{C/A}
  (20.6.5.1)
                          K_1(C/B/A) = Ω^1_{B/A} ⊗_B C
```

the differential `K_1 → K_0` being `v_{C/B/A}`. This permits one to write (up to canonical isomorphisms) `Ω^1_{C/B}` and
`Υ_{C/B/A}` as the *homology modules* of this complex:

```text
  (20.6.5.2)   H_0(K_•(C/B/A)) = Ω^1_{C/B},        H_1(K_•(C/B/A)) = Υ_{C/B/A}.
```

Likewise:

**Proposition (20.6.6).**

<!-- label: 0_IV.20.6.6 -->

*Under the hypotheses of `(20.6.1)`, for every `C`-module `L` one has canonical `C`-isomorphisms*

```text
  (20.6.6.1)   H^0(K_•(C/B/A), L) ≅ Der_B(C, L)
  (20.6.6.2)   H^1(K_•(C/B/A), L) ≅ Exalcom_{B/A}(C, L).
```

Indeed, the cochain complex `Hom_C(K_•(C/B/A), L)` is none other, by virtue of `(20.4.8)` and `(20.5.6)`, than the
complex

```text
  … → 0 → Der_A(C, L) → Der_A(B, L) → 0 → …
```

<!-- original page 138 -->

where the differential is `v⁰` (with the notations of `(20.2.1)`). The proposition then follows from the exact sequence
`(20.2.4.2)` and the definition of the cohomology modules

```text
  (20.6.6.3)   H^i(K_•, L) = H^i(Hom_C(K_•, L)).
```

If one has a commutative diagram of ring homomorphisms

```text
   A' ────▸ B' ────▸ C'
   ▴        ▴        ▴
   │        │        │
   A ────▸  B ────▸  C
```

the di-homomorphisms `(20.5.4.3)` define a di-homomorphism of complexes of modules

```text
  (20.6.6.4)   K_•(C/B/A) → K_•(C'/B'/A')
```

and the di-homomorphisms one deduces for homology or cohomology are identified, via the formulas `(20.6.5.2)`,
`(20.6.6.1)` and `(20.6.6.2)`, with the di-homomorphisms already defined in `(20.5.4.3)`, `(20.6.4.2)`, `(20.2.1)` and
`(18.3.7.2)` (taking into account, for the last, the definition of the operator `∂` in the exact sequence `(20.2.4.2)`).

**(20.6.7)** It is known that for a complex `K_•` of `C`-modules and a `C`-module `L`, one has canonical homomorphisms

```text
  α_i : H^i(K_•, L) → Hom_C(H_i(K_•), L)
```

`(M, IV, 6)`. Here, the canonical homomorphism

```text
  α_1 : H^1(K_•(C/B/A), L) → Hom_C(H_1(K_•(C/B/A)), L)
```

is defined immediately as obtained by passage to the quotient by the image of `Hom_C(K_0, L)` of the restriction
homomorphism

```text
  Hom_C(K_1(C/B/A), L) → Hom_C(H_1(K_•(C/B/A)), L),
```

since `H_1(K_•(C/B/A))` is none other than the kernel of `K_1 → K_0`; taking `(20.6.6.2)` and `(20.6.5.2)` into account,
one therefore obtains a canonical `C`-homomorphism

```text
  (20.6.7.1)   Exalcom_{B/A}(C, L) → Hom_C(Υ_{C/B/A}, L)
```

which is made explicit as follows: by virtue of `(20.2.4.2)`, every `B`-extension of `C` by `L` that is `A`-trivial comes
from the datum of an `A`-derivation `D` of `B` into `L`, hence `(20.4.8)` from a `C`-homomorphism `f` of `Ω^1_{B/A} ⊗_B C`
into `L`; one associates to the class of this extension the *restriction* of `f` to `Υ_{C/B/A}`, which depends only on
the class of the extension and not on the choice of `D`.

**Definition (20.6.8).**

<!-- label: 0_IV.20.6.8 -->

*Let `u : A → B`, `v : B → C` be two ring homomorphisms. For every `B`-extension `E` of `C` by a `C`-module `L` that is
`A`-trivial `(18.3.7)`, we call **characteristic homomorphism** of `E`, and we denote `χ_E`, the `C`-homomorphism
`Υ_{C/B/A} → L`, image of the class of `E` under the canonical homomorphism `(20.6.7.1)`.*

<!-- original page 139 -->

One can define the homomorphism `χ_E` in another way:

**Proposition (20.6.9).**

<!-- label: 0_IV.20.6.9 -->

*Let `E` be a `B`-extension of `C` by a `C`-module `L`, which is `A`-trivial `(18.3.7)`; then the diagram*

```text
                                                              v_{C/B/A}
  0 ──▸ Υ_{C/B/A} ────▸  Ω^1_{B/A} ⊗_B C    ────────────▸    Ω^1_{C/A}
        │                  │                                  │
        │ χ_E              │ q_{E/B/A} ⊗ 1_C                  │ ≅
        ▾                  ▾                                  ▾
  (20.6.9.1)
  0 ────▸    L    ────▸  Ω^1_{E/A} ⊗_E C    ────────────▸    Ω^1_{C/A}  ──▸  0
                       δ_{C/E/A}              p_{C/E/A}
```

*where `q : B → E` defines the structure of `B`-extension on `E` and `p : E → C` is the augmentation homomorphism, is
commutative and its rows are exact.*

The lower row of the diagram is the sequence `(20.5.12.5)` relative to the two homomorphisms `A → E` and
`p : E → C = E/L`; since `p` is surjective and `E` is an `A`-trivial extension, this sequence is exact and split by
virtue of `(20.5.12, (iii))`. The commutativity of the right-hand square of `(20.6.9.1)` follows from the relation
`v = p ∘ q` `(20.5.2.7)`; the image under `q_{E/B/A} ⊗ 1_C` of the kernel `Υ_{C/B/A}` of `v_{C/B/A}` is therefore
contained in the kernel `L` of `p_{C/E/A}`. On the other hand, let `h : C → E` be an `A`-homomorphism right inverse to
`p`, and let `j : L → E` be the canonical injection, so that one has `q(b) = h(v(b)) + j(D(b))` for `b ∈ B`, where `D` is
the `A`-derivation of `B` into `L` defining the `B`-extension `E`; one can write `D = f ∘ d_{B/A}`, where
`f : Ω^1_{B/A} → L` is a `B`-homomorphism. By virtue of `(20.5.2.6)`, one has

```text
  q_{E/B/A}(d_{B/A}(b)) = d_{E/A}(q(b)) = d_{E/A}(h(v(b))) + d_{E/A}(j(f(d_{B/A}(b))))   for b ∈ B.
```

Let then `z = ∑_i d_{B/A}(b_i) ⊗ c_i`, where `b_i ∈ B` and `c_i ∈ C`, be an element of `Ω^1_{B/A} ⊗_B C`; one has

```text
  (q_{E/B/A} ⊗ 1_C)(z) = ∑_i d_{E/A}(h(v(b_i))) ⊗ c_i + ∑_i d_{E/A}(j(f(d_{B/A}(b_i)))) ⊗ c_i.
```

In the first sum, one has `d_{E/A}(h(v(b_i))) = h_{E/C/A}(d_{C/A}(v(b_i)))`, hence this sum is
`(h_{E/C/A} ⊗ 1_C)(v_{C/B/A}(z))` by virtue of `(20.5.2.6)`. If one takes `z ∈ Υ_{C/B/A}`, this sum is therefore zero,
and there remains, by definition of `δ_{C/E/A}`,

```text
  (q_{E/B/A} ⊗ 1_C)(z) = ∑_i δ_{C/E/A}(c_i · f(d_{B/A}(b_i))) = δ_{C/E/A}(f(z))
```

which proves the commutativity of the left-hand square in `(20.6.9.1)`.

One will note that when one supposes only that `δ_{C/E/A}` is *injective* (and not necessarily left-invertible), this
interpretation would still permit defining `χ_E` as the restriction of `q_{E/B/A} ⊗ 1_C` to `Υ_{C/B/A}`.

**Corollary (20.6.10).**

<!-- label: 0_IV.20.6.10 -->

*If `𝔍` is an ideal of `B`, `C = B/𝔍`, `E = B/𝔍²`, and if `E` is an `A`-trivial `B`-extension `(18.3.7)` of `C` by
`𝔍/𝔍²`, then the characteristic homomorphism `χ_E : Υ_{C/B/A} → 𝔍/𝔍²` is bijective.*

<!-- original page 140 -->

Indeed, in the diagram `(20.6.9.1)`, the two right-hand vertical arrows are bijective homomorphisms `(20.5.12, (ii))`.

**Theorem (20.6.11).**

<!-- label: 0_IV.20.6.11 -->

*Let `u : A → B`, `v : B → C` be two ring homomorphisms, `L` a `C`-module. Suppose one of the following conditions holds:*

*(i) `L` is an injective `C`-module.*

*(ii) `Υ_{C/B/A}` is a direct factor of the `C`-module `Ω^1_{B/A} ⊗_B C`, and
`u_{C/B/A} : Ω^1_{C/A} → Ω^1_{C/B}` is right-invertible.*

*Then the canonical homomorphism `(20.6.7.1)`*

```text
  Exalcom_{B/A}(C, L) → Hom_C(Υ_{C/B/A}, L)
```

*is bijective.*

*In particular, if `Ω^1_{C/B}` and `Ω^1_{C/A}` are projective `C`-modules, the canonical homomorphism `(20.6.7.1)` is
bijective.*

The fact that each of conditions (i), (ii) entails that `(20.6.7.1)` is bijective follows in both cases from the
definition of `α_1`. One will note moreover that condition (ii) is *necessary and sufficient* for the homomorphism
`(20.6.7.1)` to be bijective for *every* `C`-module `L` `(Bourbaki, Alg., chap. II, 3rd ed., §2, n° 1, prop. 1)`. If one
supposes that `Ω^1_{C/B}` and `Ω^1_{C/A}` are projective `C`-modules, then, in the exact sequence `(20.6.1.1)`,
`Ker(u_{C/B/A})` is a projective `C`-module, since the exact sequence

```text
  0 → Ker(u_{C/B/A}) → Ω^1_{C/A} → Ω^1_{C/B} → 0
```

is split, `Ω^1_{C/B}` being projective; since `Ker(u_{C/B/A}) = Im(v_{C/B/A})`, the exact sequence

```text
  0 → Υ_{C/B/A} → Ω^1_{B/A} ⊗_B C → Im(v_{C/B/A}) → 0
```

is split.

**Corollary (20.6.12).**

<!-- label: 0_IV.20.6.12 -->

*Suppose that `C` is a formally smooth `A`-algebra. Then there exists a canonical homomorphism*

```text
  (20.6.12.1)   Exalcom_B(C, L) → Hom_C(Υ_{C/B/A}, L).
```

*Moreover, this homomorphism is bijective if one of conditions (i), (ii) of `(20.6.11)` is satisfied.*

Indeed, it follows from the hypothesis on `C` that `Exalcom_B(C, L) = Exalcom_{B/A}(C, L)`, and the homomorphism
`(20.6.12.1)` is none other than `(20.6.7.1)`.

**Corollary (20.6.13).**

<!-- label: 0_IV.20.6.13 -->

*If `C` is a formally smooth `A`-algebra and if `Ω^1_{C/B}` is a projective `C`-module, the homomorphism `(20.6.12.1)`
is bijective.*

Indeed, one knows then that `Ω^1_{C/A}` is a projective `C`-module `(20.4.9)`, the topologies being discrete.

**(20.6.14)** The notations remaining the same, suppose now in addition that `A`, `B`, `C` are `Λ`-algebras and `u`, `v`
are `Λ`-homomorphisms, which amounts to giving three ring homomorphisms

```text
  Λ ──s──▸ A ──u──▸ B ──v──▸ C.
```

<!-- original page 141 -->

One thus has, beyond the imperfection module `Υ_{C/B/A}`, the imperfection modules `Υ^C_{B/A/Λ}`, `Υ_{C/A/Λ}` and
`Υ_{C/B/Λ}`, and one has already defined canonical homomorphisms of `C`-modules `(20.6.4.2)`

```text
  (20.6.14.1)   u' : Υ_{C/A/Λ} → Υ_{C/B/Λ}
  (20.6.14.2)   s' : Υ_{C/B/Λ} → Υ_{C/B/A}.
```

As in the commutative diagram `(20.5.7.3)`

```text
                       Ω^1_{A/Λ} ⊗_A B  →  Ω^1_{B/Λ}  →  Ω^1_{B/A}  → 0
  (20.6.14.3)         │                   │              │
                       ▾                   ▾              ▾
                       Ω^1_{A/Λ} ⊗_A C  →  Ω^1_{C/Λ}  →  Ω^1_{C/A}  → 0
```

the lower row is formed of `C`-modules; one deduces from it by tensoring a commutative diagram

```text
                       Ω^1_{A/Λ} ⊗_A C  →  Ω^1_{B/Λ} ⊗_B C  →  Ω^1_{B/A} ⊗_B C  → 0
  (20.6.14.4)         │ =                 │                    │
                       ▾                   ▾                    ▾
                       Ω^1_{A/Λ} ⊗_A C  →  Ω^1_{C/Λ}        →  Ω^1_{C/A}        → 0
```

where the first row is again exact and the left vertical arrow is the identity. If one sets

```text
  (20.6.14.5)   Υ^C_{B/A/Λ} = Ker(u_{B/A/Λ} ⊗ 1_C) = Ker(Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C),
```

one sees, taking into account the definition of `Υ_{C/A/Λ}`, that one has a unique `C`-homomorphism

```text
  (20.6.14.6)   v' : Υ^C_{B/A/Λ} → Υ_{C/A/Λ}
```

rendering commutative the diagram

```text
   0 → Υ^C_{B/A/Λ} → Ω^1_{A/Λ} ⊗_A C →  Ω^1_{B/Λ} ⊗_B C →  Ω^1_{B/A} ⊗_B C → 0
       │ v'           │ =                │                 │
       ▾              ▾                  ▾                 ▾
  (20.6.14.7)
   0 → Υ_{C/A/Λ}   → Ω^1_{A/Λ} ⊗_A C →  Ω^1_{C/Λ}      →  Ω^1_{C/A}        → 0
```

whose rows are exact.

When `Λ = ℤ`, we shall write `Υ^C_{B/A}` in place of `Υ^C_{B/A/ℤ}`. If `Λ` is a prime field, one has
`Υ^C_{B/A/Λ} = Υ^C_{B/A}`.

**(20.6.15)** To study the relations between the preceding modules, we shall introduce on the one hand the complex of
`B`-modules `K_•(B/A/Λ)`, on the other hand the complexes of `C`-modules `K_•(C/A/Λ)` and `K_•(C/B/A)` `(20.6.5)`, and in
addition the following complexes of `C`-modules. We set first of all

<!-- original page 142 -->

```text
  (20.6.15.1)   K^C_•(B/A/Λ) = K_•(B/A/Λ) ⊗_B C.
```

On the other hand, we shall denote by `T_•(C/B/A)` the complex of `C`-modules whose terms vanish except in degrees `0`
and `1`, where

```text
  (20.6.15.2)   T_0(C/B/A) = T_1(C/B/A) = Ω^1_{B/A} ⊗_B C,
```

the differential being the identity, so that this complex is *homotopic to* `0`; we set finally

```text
  (20.6.15.3)   K'_•(C/A/Λ) = K_•(C/A/Λ) ⊕ T_•(C/B/A).
```

By virtue of the trivial character of `T_•`, it is clear that one has

```text
  (20.6.15.4)   H^i(K'_•, L) ≅ H^i(K_•, L)   and   H_i(K'_•, L) ≅ H_i(K_•, L)
```

for every `C`-module `L` and every `i`.

**(20.6.16)** Let us now define an exact sequence of complexes, split in each degree

```text
  (20.6.16.1)   0 → K^C_•(B/A/Λ) ──j──▸ K'_•(C/A/Λ) ──p──▸ K_•(C/B/A) → 0
```

as follows: let us denote for a moment by

```text
  f : Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C
  g : Ω^1_{B/Λ} ⊗_B C → Ω^1_{C/Λ}
```

the canonical homomorphisms `u_{B/A/Λ} ⊗ 1_C` and `v_{C/B/Λ}` respectively, whose composite is
`g ∘ f = (v ∘ u)_{C/A/Λ}` (cf. `(20.6.14.4)`). One takes `j_1(x) = (x, f(x))`, `p_1(y, z) = z − f(y)`,
`j_0(x) = (g(x), x)`, `p_0(y, z) = g(z) − y`, so that `Im(j_1) = Ker(p_1)` is the graph of `f`, complementary to
`{0} ⊕ T_1`, and `Im(j_0) = Ker(p_0)` is the graph of `g`, complementary to `K_1(C/A/Λ) ⊕ {0}`; the verification of the
commutativity of the diagram

```text
   0 → K^C_1(B/A/Λ) ──j_1──▸ K'_1(C/A/Λ) ──p_1──▸ K_1(C/B/A) → 0
       │                     │                   │
       ▾                     ▾                   ▾
   0 → K^C_0(B/A/Λ) ──j_0──▸ K'_0(C/A/Λ) ──p_0──▸ K_0(C/B/A) → 0
```

where the vertical arrows are the differentials, is immediate.

**Theorem (20.6.17).**

<!-- label: 0_IV.20.6.17 -->

*One has an exact sequence of `C`-modules*

```text
                                     v'             u'             ∂                v_{C/B/A}        u_{C/B/A}
  (20.6.17.1)   0 → Υ^C_{B/A/Λ}  ──────▸  Υ_{C/A/Λ}  ──────▸  Υ_{C/B/A}  ────▸  Ω^1_{B/A} ⊗_B C  ──────────▸  Ω^1_{C/A}  ──────────▸  Ω^1_{C/B}  → 0
```

<!-- original page 143 -->

*where the boundary operator `∂` is the composite*

```text
  (20.6.17.2)   Υ_{C/B/A} ──s'──▸ Υ_{C/B/Λ} ────▸ Ω^1_{B/Λ} ⊗_B C
```

*the second arrow being the canonical injection.*

By writing the exact sequence of homology for the exact sequence of complexes `(20.6.16.1)`, one obtains
`(20.6.17.1)`, the homology being zero in degrees other than `0` and `1`; the fact that the homomorphisms of this exact
sequence that come by functoriality from `j` and `p` are indeed those of the statement is immediate. It remains to
verify that `∂` is equal to `(20.6.17.2)`; now an element `z ∈ Υ_{C/B/A}` is the image under `p_1` of `(0, z)`, whence
one deduces at once that `∂(z)` is the image of `z` under the canonical homomorphism
`s_{B/A/Λ} ⊗ 1_C : Ω^1_{B/A} ⊗_B C → Ω^1_{B/Λ} ⊗_B C`. Our assertion follows from the commutativity of the diagram

```text
                Υ_{C/B/A} ──s'──▸ Υ_{C/B/Λ}
                  │                │
  (20.6.17.3)     ▾                ▾
                Ω^1_{B/A} ⊗_B C → Ω^1_{B/Λ} ⊗_B C
```

(cf. `(20.6.4.3)`).

**Corollary (20.6.18).**

<!-- label: 0_IV.20.6.18 -->

*(i) The sequence of `C`-modules*

```text
                              v'              u'             s'
  (20.6.18.1)   0 → Υ^C_{B/A/Λ}  ──▸  Υ_{C/A/Λ}  ──▸  Υ_{C/B/Λ}  ──▸  Υ_{C/B/A} → 0
```

*is exact.*

*(ii) If `B` is a `Λ`-algebra formally smooth relative to `Λ`, one has `Υ^C_{B/A/Λ} = 0`.*

(i) In `(20.6.17.1)`, the image of `Υ_{C/B/Λ}` under `∂` is the kernel of `v_{C/B/A}`, hence `Υ_{C/B/A}` by definition.

(ii) The hypothesis entails that the sequence

```text
  0 → Ω^1_{A/Λ} ⊗_A B → Ω^1_{B/Λ} → Ω^1_{B/A} → 0
```

is exact and split `(20.5.7)`; by tensoring with `C`, the sequence

```text
  0 → Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C → Ω^1_{B/A} ⊗_B C → 0
```

therefore remains exact, whence our assertion.

**Corollary (20.6.19).**

<!-- label: 0_IV.20.6.19 -->

*Let `K` be a field, `E`, `F` two extensions of `K` such that `K ⊂ E ⊂ F`.*

*(i) If `F` is a separable extension of `E`, one has `Υ_{F/E/K} = 0` (in other words, the canonical homomorphism
`Ω^1_{E/K} ⊗_E F → Ω^1_{F/K}` is injective).*

*(ii) Conversely, if `F` is a separable extension of `K` and one has `Υ_{F/E/K} = 0`, then `F` is a separable extension
of `E`.*

If `P` is the prime field of `K`, one has by `(20.6.18)` the exact sequence

```text
  Υ_{F/K/P} → Υ_{F/E/P} → Υ_{F/E/K} → 0.
```

If `Υ_{F/E/P} = Υ_{F/E} = 0`, then `Υ_{F/E/K} = 0`, whence (i) by virtue of `(20.6.3)`; conversely, if
`Υ_{F/E/K} = 0` and `Υ_{F/K/P} = Υ_{F/K} = 0`, one has `Υ_{F/E/P} = 0`, whence (ii) by virtue of `(20.6.3)`.

<!-- original page 144 -->

**Corollary (20.6.20).**

<!-- label: 0_IV.20.6.20 -->

*(i) If `K` is a separable algebraic extension of `k`, one has `Ω^1_{K/k} = 0`.*

*(ii) Let `k` be a field of characteristic `0`, `K` an extension of `k`. For `Ω^1_{K/k} = 0`, it is necessary and
sufficient that `K` be an algebraic extension of `k`. In particular, for a field `K` of characteristic `0` to be such
that `Ω^1_K = 0`, it is necessary and sufficient that `K` be an algebraic extension of `ℚ` (cf. `(21.4.4)` and
`(21.7.5)`).*

(i) For every `x ∈ K`, let `f` be the minimal polynomial of `x` over `k`; since `f'(x) ≠ 0` and
`d_{K/k}(f(x)) = f'(x) d_{K/k}(x) = 0`, one has `d_{K/k}(x) = 0`, and our assertion follows from `(20.4.7)`.

(ii) There exists a pure extension `L` of `k` such that `k ⊂ L ⊂ K` and such that `K` is an algebraic extension of `L`.
Since `K` is separable over `L`, it follows from `(20.6.19, (i))` that the sequence `(20.5.7.2)`

```text
  0 → Ω^1_{L/k} ⊗_L K → Ω^1_{K/k} → Ω^1_{K/L} → 0
```

is exact, and from (i) that `Ω^1_{K/L} = 0`. The relation `Ω^1_{K/k} = 0` is therefore equivalent to `Ω^1_{L/k} = 0`, and
since `L` is a pure extension of `k`, it follows from `(20.5.10)` that the relation `Ω^1_{L/k} = 0` is equivalent to
`L = k`.

**Remarks (20.6.21).**

<!-- label: 0_IV.20.6.21 -->

*(i) Since `Υ_{B/A/Λ}` is the kernel of `u_{B/A/Λ} : Ω^1_{A/Λ} ⊗_A B → Ω^1_{B/Λ}` and `Υ^C_{B/A/Λ}` is the kernel of
`u_{B/A/Λ} ⊗ 1_C`, one has a canonical homomorphism*

```text
  (20.6.21.1)   Υ_{B/A/Λ} ⊗_B C → Υ^C_{B/A/Λ}.
```

*This homomorphism is bijective when the sequence*

```text
  (20.6.21.2)   0 → Υ_{B/A/Λ} ⊗_B C → Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C → Ω^1_{B/A} ⊗_B C → 0
```

*is exact, which occurs in the following cases:*

*1° `C` is a flat `B`-module.*

*2° The `B`-modules `Ω^1_{B/A}` and `Ω^1_{B/Λ}` are flat; for then so is `Ker(Ω^1_{B/A} → Ω^1_{B/Λ})` `(0_I, 6.1.2)`, and
the sequence `(20.6.21.2)` is then exact by virtue of `(0_I, 6.1.2)`.*

*(ii) Consider a commutative diagram of ring homomorphisms*

```text
  Λ' ────▸ A' ────▸ B' ────▸ C'
  ▴        ▴        ▴        ▴
  │        │        │        │
  Λ  ────▸ A  ────▸ B  ────▸ C
```

*Then the definitions of `(20.6.16)` show that one has a commutative diagram of complexes (where the vertical arrows
come from `(20.6.6.4)`)*

```text
   0 → K^C_•(B/A/Λ) → K'_•(C/A/Λ) → K_•(C/B/A) → 0
       │              │              │
       ▾              ▾              ▾
   0 → K^{C'}_•(B'/A'/Λ') → K'_•(C'/A'/Λ') → K_•(C'/B'/A')
```

<!-- original page 145 -->

*whence, by passage to homology, a commutative diagram*

```text
  (20.6.21.3)
   0 → Υ^C_{B/A/Λ}      → Υ_{C/A/Λ}      → Υ_{C/B/A}      → Ω^1_{B/A} ⊗_B C    → Ω^1_{C/A}    → Ω^1_{C/B}    → 0
       │                  │                │                │                    │              │
       ▾                  ▾                ▾                ▾                    ▾              ▾
   0 → Υ^{C'}_{B'/A'/Λ'} → Υ_{C'/A'/Λ'}  → Υ_{C'/B'/A'}  → Ω^1_{B'/A'} ⊗_{B'} C' → Ω^1_{C'/A'} → Ω^1_{C'/B'} → 0
```

*One has an analogous commutative diagram for `(20.6.18.1)`.*

**Proposition (20.6.22).**

<!-- label: 0_IV.20.6.22 -->

*Let `s : Λ → A`, `u : A → B` be two ring homomorphisms, `𝔍` an ideal of `B`, `C` the quotient ring `B/𝔍`. Suppose that
`E = B/𝔍²` is an `A`-trivial `B`-extension of `C` by `𝔍/𝔍²`. Then one has the exact sequence*

```text
                                    v'           χ_E             δ_{C/B/A}                  v_{C/B/A}
  (20.6.22.1)   0 → Υ^C_{B/A/Λ}  ──▸ Υ_{C/A/Λ} ──▸ 𝔍/𝔍²  ──▸  Ω^1_{B/A} ⊗_B C  ─────────▸  Ω^1_{C/A}  → 0.
```

Indeed, since `v : B → C` is surjective, one has `Ω^1_{C/B} = 0` `(20.4.12)`. Furthermore, it follows from `(20.6.10)`
that `Υ_{C/B/A}` is canonically identified with `𝔍/𝔍²`. It then suffices to apply the exact sequences `(20.6.17.1)` and
`(20.6.18.1)`, noting that one has a commutative diagram

```text
                Υ_{C/A/Λ}                ──▸ Ω^1_{A/Λ} ⊗_A C
                  │                            │
                  ▾ χ_E                        ▾
   Υ_{C/B/Λ} = Υ_{C/B/A} = 𝔍/𝔍²  ──δ_{C/B/A}──▸  Ω^1_{B/A} ⊗_B C = Ω^1_{E/A} ⊗_E C
                  │                            │
                  ▾                            ▾
                𝔍/𝔍²              ──δ_{C/B/A}──▸  Ω^1_{B/A} ⊗_B C
```

and using the commutativity of the diagram `(20.6.17.3)`.

One has thus specified the kernel of `δ_{C/B/A}` in the case where there exists a ring `Λ` such that `A` is a
`Λ`-algebra and `B/𝔍²` is `Λ`-trivial; one observes that this is the case in particular when `C` is a formally smooth
`Λ`-algebra (for the discrete topology).

Suppose in addition that one has a commutative diagram of ring homomorphisms

```text
  Λ' ────▸ A' ────▸ B'
  ▴        ▴        ▴
  │        │        │ f
  Λ  ────▸ A  ────▸ B
```

<!-- original page 146 -->

such that `𝔍'` is an ideal of `B'` with `f(𝔍) ⊂ 𝔍'`, and `E' = B'/𝔍'²` is an `A'`-trivial `B'`-extension of
`C' = B'/𝔍'` by `𝔍'/𝔍'²`. One then has a commutative diagram

```text
  (20.6.22.2)
   0 → Υ^{C'}_{B'/A'/Λ'} → Υ_{C'/A'/Λ'} → 𝔍'/𝔍'² → Ω^1_{B'/A'} ⊗_{B'} C' → Ω^1_{C'/A'} → 0
       ▴                   ▴               ▴       ▴                       ▴
       │                   │               │       │                       │
   0 → Υ^C_{B/A/Λ}        → Υ_{C/A/Λ}    → 𝔍/𝔍²   → Ω^1_{B/A} ⊗_B C      → Ω^1_{C/A}    → 0
```

as follows from `(20.6.21.3)` and `(20.5.11.3)`.

**Corollary (20.6.23).**

<!-- label: 0_IV.20.6.23 -->

*Under the hypotheses of `(20.6.22)`, suppose in addition that `B` is a formally smooth `Λ`-algebra. Then one has an
exact sequence*

```text
                              χ_E           δ_{C/B/A}                  v_{C/B/A}
  (20.6.23.1)   0 → Υ_{C/A/Λ}  ──▸  𝔍/𝔍²  ──▸  Ω^1_{B/A} ⊗_B C  ──▸  Ω^1_{C/A} → 0.
```

This indeed follows from `(20.6.18, (ii))`.

**(20.6.24)** When the hypotheses of `(20.6.22)` are satisfied, one says again that the characteristic homomorphism
`χ_E` is the **characteristic homomorphism** of the `A`-algebra `B`, relative to `Λ` and to the ideal `𝔍` (suppressing
these last specifications when there is no risk of confusion); it will sometimes be denoted `χ_B` or `χ_{B/Λ}`.

**Proposition (20.6.25).**

<!-- label: 0_IV.20.6.25 -->

*Let `s : Λ → A`, `u : A → B`, `v : B → C` be three ring homomorphisms, `L` a `C`-module. One then has an exact sequence*

```text
                                  u⁰              v⁰              ∂
  (20.6.25.1)   0 → Der_B(C, L)  ──▸  Der_A(C, L)  ──▸  Der_Λ(B, L)  ──▸
                          ──▸  Exalcom_{B/A}(C, L)  ──u¹──▸  Exalcom_{A/Λ}(C, L)  ──v¹──▸  Exalcom_{A/Λ}(B, L)  → 0
```

*where `u¹`, `v¹` are the homomorphisms defined in `(18.3.6.4)` and `(18.3.6.2)`, and `∂` is defined as in `(20.2.2)`.*

Indeed, since the exact sequence `(20.6.16.1)` is split, one deduces an exact sequence

```text
  0 → Hom_C(K_•(C/B/A), L) → Hom_C(K'_•(C/A/Λ), L) → Hom_C(K^C_•(B/A/Λ), L) → 0.
```

If one applies to this complex the exact sequence of cohomology, taking into account `(20.6.15.4)` and `(20.6.6)`, one
obtains `(20.6.25.1)`, since one has

```text
  Hom_C(K^C_•(B/A/Λ), L) = Hom_B(K_•(B/A/Λ), L)
```

by definition; the identification of `u¹` and `v¹` with the homomorphisms of `(18.3.4.2)` follows from `(20.6.6.4)`.

**Remark (20.6.26).**

<!-- label: 0_IV.20.6.26 -->

*In this number, the complexes `K_•(C/B/A)` have appeared as a technical artifice destined to simplify the exposition of
certain functorial behaviours. In reality, these complexes, considered as objects of the category of complexes of
<!-- original page 147 -->
`C`-modules "up to homotopy" (that is, where the morphisms are the classes of homotopic homomorphisms), are remarkable
invariants, finer than the pair formed of `Ω^1_{C/B}` and `Υ_{C/B/A}`. When `k` is a prime field, and `C` is a formally
smooth `k`-algebra (for example a regular ring of finite type over an extension of `k` (cf. `(IV, 6.8.6)`)), one can
show that the complex `K_•(C/A/k)` can be described uniquely in terms of `C` and `A` (to the exclusion of `k`): one
expresses `C` as the quotient of a polynomial algebra `B` over `A` by an ideal `𝔏`, and one considers the complex
`F_•(C/A)` with two non-zero terms*

```text
  … → 0 → 𝔏/𝔏² → Ω^1_{B/A} ⊗_B C → 0 → …
```

*(whose homology coincides indeed with that of `K_•(C/A/k)` by virtue of `(20.6.23.1)`). These complexes `F_•(C/A)`,
which from the point of view of homological algebra play the role of a conormal bundle for `Spec(C)` over `Spec(A)`,
will occupy an important place in the chapters of this work devoted to the duality of coherent sheaves and to the
Riemann-Roch theorem.*

### 20.7. Generalizations to topological rings

**(20.7.1)** It follows at once from the definitions that if, in `(20.5.2)` and `(20.5.3)`, the rings `A`, `B`, `C` are
supposed to be topological rings and the ring homomorphisms `u`, `v` continuous, then the homomorphisms `u_{C/B/A}` and
`v_{C/B/A}` are *continuous* (one must naturally take on `Ω^1_{B/A} ⊗_B C` the tensor product topology).

Moreover, `u_{C/B/A} : Ω^1_{C/A} → Ω^1_{C/B}` is a *strict surjective morphism* of topological `C`-modules; for it is
thus for the canonical homomorphism `C ⊗_A C → C ⊗_B C`, taking into account the definition of the tensor product
topology; by passage to the quotients one deduces that the corresponding homomorphism `P^1_{C/A} → P^1_{C/B}` is a
strict surjective morphism, and `u_{C/B/A}` is the restriction of this last to `Ω^1_{C/A}`.

In `(20.5.5)`, if `A'` and `B` are topological `A`-algebras, and if `B'` and `Ω^1_{B/A} ⊗_A B'` are equipped with the
tensor product topologies, the canonical homomorphism `(20.5.5.1)` is a *topological isomorphism*, taking into account
the fact that `P^1_{B/A}` is the topological direct sum of `B` and `Ω^1_{B/A}` `(20.4.8)`.

**Proposition (20.7.2).**

<!-- label: 0_IV.20.7.2 -->

*Let `u : A → B`, `v : B → C` be two continuous homomorphisms of topological rings. For the continuous homomorphism
`v_{C/B/A} : Ω^1_{B/A} ⊗_B C → Ω^1_{C/A}` to be formally left-invertible (cf. `(19.1.5)`), it is necessary and sufficient
that `C` be a `B`-algebra formally smooth relative to `A` `(19.9.1)` (and a fortiori it suffices that `C` be a formally
smooth `B`-algebra).*

To say that `v_{C/B/A}` is formally left-invertible signifies indeed, since the topologies of `Ω^1_{C/A}` and
`Ω^1_{B/A} ⊗_B C` are coarser than those deduced from the topology of `C` `(20.4.5)`, that for every discrete `C`-module
`L`, annihilated by an open ideal of `C`, the canonical homomorphism

```text
  Hom.cont_C(Ω^1_{C/A}, L) → Hom.cont_C(Ω^1_{B/A} ⊗_B C, L)
```

<!-- original page 148 -->

is surjective `(19.1.5)`; since `Hom.cont_C(Ω^1_{B/A} ⊗_B C, L) = Hom.cont_C(Ω^1_{B/A}, L)` by definition of the tensor
product topology, it amounts to the same, by virtue of `(20.4.8)`, to say that the canonical homomorphism

```text
  Der.cont_A(C, L) → Der.cont_A(B, L)
```

is surjective. But the exact sequence `(20.3.8.2)` shows that this condition is equivalent to
`Exalcotop_{B/A}(C, L) = 0`, that is to say precisely to the fact that `C` is formally smooth relative to `A` `(19.9.8)`.

**Corollary (20.7.3).**

<!-- label: 0_IV.20.7.3 -->

*Suppose that in `B` and in `C`, the square of an open ideal is open. For `C` to be a `B`-algebra formally smooth
relative to `A`, it is necessary and sufficient that, if one denotes by `(𝔎_λ)` a fundamental system of neighbourhoods
of `0` formed of ideals of `C`, then, for every `λ`, the homomorphism*

```text
  (20.7.3.1)   v_{C/B/A} ⊗ 1_{C/𝔎_λ} : Ω^1_{B/A} ⊗_B (C/𝔎_λ) → Ω^1_{C/A} ⊗_C (C/𝔎_λ)
```

*be left-invertible.*

One knows indeed in that case that the topology of `Ω^1_{B/A}` (resp. `Ω^1_{C/A}`) is deduced from that of `B`
(resp. of `C`) `(20.4.5)`; one concludes at once that the topology of `Ω^1_{B/A} ⊗_B C` is also deduced from that of
`C`; the corollary then follows from `(20.7.2)` and `(19.1.7)`.

**Proposition (20.7.4).**

<!-- label: 0_IV.20.7.4 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra. For `B` to be formally unramified `(19.10.2)`, it is
necessary and sufficient that the separated completion `Ω̂^1_{B/A}` be zero.*

Indeed, it follows at once from `(19.10.4)` and `(20.1.1)` that, for `B` to be formally unramified, it is necessary and
sufficient that for every open ideal `𝔎` of `B`, every open ideal `𝔍` of `A` such that `𝔍·B ⊂ 𝔎`, and every
`(B/𝔎)`-module `L`, one have `Der_A(B/𝔎, L) = 0`, that is to say `Der.cont_A(B, L) = 0` for every discrete `B`-module `L`
annihilated by an open ideal of `B`; by virtue of `(20.4.8)`, this is equivalent to
`Hom.cont_B(Ω^1_{B/A}, L) = 0` for such a `B`-module, whence at once the proposition.

When `B` is discrete, the condition in the statement of `(20.7.4)` is therefore equivalent to `Ω^1_{B/A} = 0`.

**Corollary (20.7.5).**

<!-- label: 0_IV.20.7.5 -->

*Let `A` be a ring, `𝔪` an ideal of `A`, `B` an `A`-algebra; equip `A` with the `𝔪`-preadic topology, `B` with the
topology deduced from that of `A`, and set `A_0 = A/𝔪`, `B_0 = B/𝔪B = B ⊗_A A_0`. Then, for `B` to be a formally
unramified `A`-algebra, it is necessary and sufficient that `Ω^1_{B_0/A_0} = 0` (or, equivalently, that `B_0` be a
formally unramified `A_0`-algebra).*

Indeed, one has `Ω^1_{B/A} ⊗_B B_0 = Ω^1_{B/A} / 𝔪·Ω^1_{B/A} = Ω^1_{B_0/A_0}` by virtue of `(20.5.5)`; to write that
every open submodule of `Ω^1_{B/A}` is equal to `Ω^1_{B/A}` is equivalent, by `(20.4.5)`, to writing
`𝔪·Ω^1_{B/A} = Ω^1_{B/A}`, whence the conclusion.

**Proposition (20.7.6).**

<!-- label: 0_IV.20.7.6 -->

*Let `u : A → B`, `v : B → C` be two continuous homomorphisms of topological rings, and suppose that `v` makes `C` into
a formally étale `B`-algebra; then `v_{C/B/A} : Ω^1_{B/A} ⊗_B C → Ω^1_{C/A}` is a formal bimorphism `(19.1.2)`.*

Indeed, for every discrete `C`-module `L` annihilated by an open ideal of `C`, one then has `(20.7.4)`
`Der.cont_B(C, L) = 0` and consequently `(20.3.6.1)` the canonical homomorphism

<!-- original page 149 -->

`Der.cont_A(C, L) → Der.cont_A(B, L)` is injective; it is moreover surjective by virtue of `(20.7.2)`, hence bijective.
It follows that the image of `v_{C/B/A}` is necessarily dense in `Ω^1_{C/A}`, otherwise the quotient of `Ω^1_{C/A}` by
the closure of `Im(v_{C/B/A})` would be separated and `≠ 0` and would therefore have a discrete quotient `L ≠ 0`,
contrary to what we have just seen (taking `(20.4.8)` into account). Consequently `v_{C/B/A}`, which is a formal
monomorphism by virtue of `(20.7.2)`, is also a formal epimorphism `(19.1.2)`, hence a formal bimorphism.

**Corollary (20.7.7).**

<!-- label: 0_IV.20.7.7 -->

*Suppose that in `B` and in `C` the square of every open ideal is open. If `C` is a formally étale `B`-algebra, then,
for every open ideal `𝔎_λ` of `C`, the homomorphism `(20.7.3.1)` is bijective.*

Indeed, by virtue of `(19.1.1)`, this homomorphism is surjective, and it is injective by `(20.7.3)`.

**Proposition (20.7.8).**

<!-- label: 0_IV.20.7.8 -->

*Let `u : A → B` be a continuous homomorphism of topological rings, `𝔍` an ideal of `B`, `C` the quotient topological
ring `B/𝔍`, `v : B → C` the canonical homomorphism. Then:*

*(i) In the exact sequence `(20.5.12.1)`*

```text
                    δ_{C/B/A}                v_{C/B/A}
  𝔍/𝔍²  ────────────▸  Ω^1_{B/A} ⊗_B C  ────────────▸  Ω^1_{C/A} → 0
```

*the homomorphism `δ_{C/B/A}` is continuous and the homomorphism `v_{C/B/A}` is a strict morphism of topological
`C`-modules.*

*(ii) For `δ_{C/B/A}` to be formally left-invertible `(19.1.5)`, it is necessary and sufficient that for every discrete
`C`-module `L` annihilated by an open ideal of `C`, the canonical homomorphism*

```text
  (20.7.8.1)   Exalcotop_A(C, L) → Exalcotop_A(B, L)
```

*be injective.*

(i) The first assertion is evident. On the other hand, the canonical homomorphism
`v ⊗ v : B ⊗_A B → C ⊗_A C` is a strict morphism by definition of the tensor product topology, and one deduces at once
(cf. `(20.5.2)`) that the same holds of `v_{C/B/A}`.

(ii) To say that `δ_{C/B/A}` is formally left-invertible signifies that for every discrete `C`-module `L` annihilated by
an open ideal of `C`, the canonical homomorphism

```text
  Hom.cont_C(Ω^1_{B/A} ⊗_B C, L) → Hom.cont_C(𝔍/𝔍², L)
```

is surjective. Now, taking into account `(18.4.3)` and `(20.4.8)`, this amounts to saying that the canonical
homomorphism

```text
  Der.cont_A(B, L) → Exalcotop_B(C, L)
```

is surjective, and the conclusion therefore follows from the exact sequence `(20.3.6.1)`.

The fact that `(20.7.8.1)` be injective is also expressed in the following manner, taking into account the definition of
the two members `(18.4.1)`: for every open ideal `𝔐` of `A`, every open ideal `𝔑` of `B` such that `𝔐B ⊂ 𝔑`, and every
`(A/𝔐)`-extension `E` of `B/(𝔍 + 𝔑)` by a `(B/(𝔍 + 𝔑))`-module `L`, such that the inverse image of `E` under the
canonical homomorphism `B/𝔑 → B/(𝔍 + 𝔑)` be `(A/𝔐)`-trivial, there exists an open ideal `𝔐' ⊂ 𝔐` of `A`,
<!-- original page 150 -->
an open ideal `𝔑' ⊂ 𝔑` of `B` such that `𝔐'B ⊂ 𝔑'` and such that the inverse image of `E` under the canonical
homomorphism `B/(𝔍 + 𝔑') → B/(𝔍 + 𝔑)` be `(A/𝔐')`-trivial. In particular:

**Corollary (20.7.9).**

<!-- label: 0_IV.20.7.9 -->

*If the topological `A`-algebra `C = B/𝔍` is formally smooth, the canonical homomorphism `δ_{C/B/A}` is formally
left-invertible.*

**(20.7.10)** In `(20.6.1)`, when `A`, `B`, `C` are topological rings and `u`, `v` continuous homomorphisms, one
equips `Υ_{C/B/A}` with the topology induced by that of `Ω^1_{B/A} ⊗_B C`; the homomorphisms `(20.6.4.2)` and
`(20.6.4.4)` are then continuous, provided the same holds for those of the diagram `(20.6.4.1)`. Moreover, if, in
`(20.6.7)`, one assumes that `L` is a discrete `C`-module annihilated by an open ideal of `C`, one deduces, by passage
to the inductive limit, a canonical `C`-homomorphism

```text
  (20.7.10.1)   Exalcotop_{B/A}(C, L) → Hom.cont_C(Υ_{C/B/A}, L)
```

taking into account `(18.5.3.1)`: for every open ideal `𝔐` of `A`, every open ideal `𝔑` of `B` such that `𝔐B ⊂ 𝔑`,
every open ideal `𝔓` of `C` such that `𝔑C ⊂ 𝔓` and `𝔓·L = 0`, every `(B/𝔑)`-extension `E` of `C/𝔓` by `L` that is
`(A/𝔐)`-trivial comes from the datum of a continuous `C`-homomorphism `f` of `Ω^1_{B/A} ⊗_B C` into `L`, and the
homomorphism `(20.7.10.1)` associates to the image in `Exalcotop_{B/A}(C, L)` of the class of `E`, the restriction of
`f` to `Υ_{C/B/A}`, the **characteristic homomorphism** of `E`, again denoted `χ_E`.

**Proposition (20.7.11).**

<!-- label: 0_IV.20.7.11 -->

*Suppose that the topology of `C` is such that the square of an open ideal is open. If `C` is a topological `A`-algebra
that is formally smooth and if `Ω^1_{C/B}` is a formally projective `C`-module, one has a canonical isomorphism*

```text
  (20.7.11.1)   Exalcotop_B(C, L) ≅ Hom.cont_C(Υ_{C/B/A}, L)
```

*for every discrete `C`-module `L` annihilated by an open ideal of `C`.*

Indeed, in the exact sequence `(20.3.7.1)`, one has `Exalcotop_A(C, L) = 0` `(19.4.4)`, hence
`Exalcotop_B(C, L) = Exalcotop_{B/A}(C, L)` and the homomorphism `(20.7.8.1)` is none other than `(20.7.10.1)`; the
fact that it is bijective is deduced from `(20.6.13)` by passage to the inductive limit, taking into account that the
topology of `Ω^1_{C/B}` is then deduced from that of `C` `(20.4.5)` and `(19.2.4)`.

**(20.7.12)** In `(20.6.14)` one again equips `Υ^C_{B/A/Λ}` with the topology induced by that of `Ω^1_{A/Λ} ⊗_A C`,
and then the homomorphism `(20.6.14.6)` is continuous, when the rings considered are topological and the ring
homomorphisms continuous.

**(20.7.13)** If, in `(20.6.23)`, one supposes that the rings `Λ`, `A`, `B`, `C` are topological, the homomorphisms
`s`, `u`, `v` continuous and `L` a discrete `C`-module annihilated by an open ideal of `C`, then one may pass to the
inductive limit as in `(20.3.6)`, and one has an exact sequence

```text
  (20.7.13.1)   0 → Der.cont_B(C, L) → Der.cont_A(C, L) → Der.cont_Λ(B, L) →
                  → Exalcotop_{B/A}(C, L) → Exalcotop_{A/Λ}(C, L) → Exalcotop_{A/Λ}(B, L) → 0.
```

**(20.7.14)** Let `A` be a topological ring, `B` a topological `A`-algebra, `𝔐'` an open ideal of `A`, `𝔑'` an open
ideal of `B` such that `𝔐'B ⊂ 𝔑'`; set `A' = A/𝔐'`,
<!-- original page 151 -->
`B' = B/𝔑'`; the kernel of the homomorphism `B ⊗_A B → B' ⊗_{A'} B'` is `𝔘' = Im(𝔑' ⊗ B + B ⊗ 𝔑')`, from which it
follows at once that the kernel of the homomorphism

```text
  (20.7.14.1)   φ_{(𝔐', 𝔑')} : Ω^1_{B/A} → Ω^1_{B'/A'}
```

is `((𝔍 ∩ 𝔘') + 𝔍²)/𝔍²`; on the other hand, the homomorphism `(20.7.14.1)` is *surjective*, as follows from `(20.4.7)`.
If `𝔐''` (resp. `𝔑''`) is a second open ideal of `A` (resp. `B`) such that `𝔐'' ⊂ 𝔐'`, `𝔑'' ⊂ 𝔑'` and `𝔐''B ⊂ 𝔑''`,
and if one sets `A'' = A/𝔐''`, `B'' = B/𝔑''`, one has likewise a surjective homomorphism

```text
  φ_{(𝔐', 𝔑'), (𝔐'', 𝔑'')} : Ω^1_{B''/A''} → Ω^1_{B'/A'}
```

and these homomorphisms obviously form a *projective system*. If one remarks that the `((𝔍 ∩ 𝔘') + 𝔍²)/𝔍²` form a
fundamental system of neighbourhoods of `0` in `Ω^1_{B/A}`, one sees therefore that the separated completion
`Ω̂^1_{B/A}` of the topological `B`-module `Ω^1_{B/A}` is given, up to a canonical isomorphism, by

```text
  (20.7.14.2)   Ω̂^1_{B/A} = lim←(Ω^1_{B'/A'}).
```

Moreover, the canonical homomorphism `j : Ω^1_{B/A} → Ω̂^1_{B/A}` is the projective limit of the projective system of
the `φ_{(𝔐', 𝔑')}`, hence `φ_{(𝔐', 𝔑')}` factors as `Ω^1_{B/A} ──j──▸ Ω̂^1_{B/A} → Ω^1_{B'/A'}`, and since it is
surjective one concludes that the canonical homomorphism

```text
  (20.7.14.3)   Ω̂^1_{B/A} → Ω^1_{B'/A'}
```

is *surjective* for every pair `(𝔐', 𝔑')`.

One may moreover in the foregoing replace `A'` everywhere by `A`.

Finally, if `L` is a separated and complete topological `B`-module, every continuous `B`-homomorphism of `Ω^1_{B/A}`
into `L` extends in a unique way to a continuous `B̂`-homomorphism of `Ω̂^1_{B/A}` into `L`, and conversely such a
homomorphism gives back by composition with `Ω^1_{B/A} → Ω̂^1_{B/A}` a continuous `B`-homomorphism, so that one has a
canonical isomorphism

```text
  Hom.cont_{B̂}(Ω̂^1_{B/A}, L) ≅ Hom.cont_B(Ω^1_{B/A}, L).
```

More particularly, if `L` is a discrete `B`-module annihilated by an open ideal of `B`, one sees that the canonical
isomorphism `(20.4.8.2)` may also be written

```text
  (20.7.14.4)   Hom.cont_B(Ω̂^1_{B/A}, L) ≅ Der.cont_A(B, L).
```

**Proposition (20.7.15).**

<!-- label: 0_IV.20.7.15 -->

*Let `A` be a discrete ring, `B` a topological adic `A`-algebra `(0_I, 7.1.9)`, `𝔫` an ideal of definition of `B`,
`B_0 = B/𝔫`. Suppose that `Ω^1_{B_0/A}` and `𝔫/𝔫²` are `B_0`-modules of finite type. Then `Ω̂^1_{B/A}` is a `B̂`-module
of finite type.*

Since the square of every open ideal of `B` is open, the topology of `Ω^1_{B/A}` is the `𝔫`-preadic topology
`(20.4.5)`. Taking into account the hypothesis that `B` is an adic ring, it therefore suffices, by virtue of
`(0_I, 7.2.7 and 7.2.9)`, to prove

<!-- original page 152 -->

that `Ω^1_{B/A} / 𝔫·Ω^1_{B/A} = Ω^1_{B/A} ⊗_B B_0` is a `B_0`-module of finite type. But this follows from the
hypothesis and from the exact sequence `(20.5.12.1)`

```text
  𝔫/𝔫² → Ω^1_{B/A} ⊗_B B_0 → Ω^1_{B_0/A} → 0.
```

**(20.7.16)** The proposition `(20.7.15)` applies for example when `A` is a field `k`, `B = k'[[T_1, …, T_n]]` a
formal power series algebra equipped with its usual topology, `k'` a finite extension of `k` (cf. `(21.9.2)`). One will
note that the field of fractions `K` of `B` has infinite transcendence degree over `k`; when `k` is of characteristic
`0`, one deduces at once (with the help of `(20.4.13, (i))` and of `(20.5.9)` in particular, also using the fact that
every derivation of a field of characteristic `0` extends to every extension) that `Ω^1_{K/k}` is *not* a `K`-module of
finite type.

**(20.7.17)** Let `A`, `B`, `C` be three topological rings, `u : A → B`, `v : B → C` two continuous homomorphisms;
replacing `A`, `B`, `C` by quotients by open ideals `A' = A/𝔐'`, `B' = B/𝔑'`, `C' = C/𝔓'` with `u(𝔐') ⊂ 𝔑'`,
`v(𝔑') ⊂ 𝔓'`, so that one has homomorphisms `u' : A' → B'`, `v' : B' → C'`, one deduces canonical homomorphisms
`u_{C'/B'/A'}`, `v_{C'/B'/A'}` which, by virtue of `(20.5.4)`, form projective systems, and give in consequence, by
passage to the limit, canonical homomorphisms, extensions to the separated completions of the homomorphisms of the
exact sequence `(20.5.7.1)`

```text
                              v_{C/B/A}             u_{C/B/A}
                Ω^1_{B/A} ⊗_B C  ────────▸  Ω^1_{C/A}  ────────▸  Ω^1_{C/B}  → 0

  (20.7.17.1)   v̂_{C/B/A} : Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ → Ω̂^1_{C/A}

  (20.7.17.2)   û_{C/B/A} : Ω̂^1_{C/A} → Ω̂^1_{C/B}
```

and in the sequence

```text
                              v̂_{C/B/A}             û_{C/B/A}
  (20.7.17.3)   Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ  ────────▸  Ω̂^1_{C/A}  ────────▸  Ω̂^1_{C/B}  → 0
```

the composite of two consecutive homomorphisms is `0`, but the sequence *is not necessarily exact*. However, if `B` and
`C` are metrizable, the homomorphism `û_{C/B/A}` is *surjective*, and `Im(v̂_{C/B/A})` is *dense* in `Ker(û_{C/B/A})`:
this follows at once (cf. `(0_I, 7.3.1)`) from the fact that, if `(𝔐_k)` (resp. `(𝔑_k)`) is a decreasing sequence of
ideals of `B` (resp. `C`) forming a fundamental system of neighbourhoods of `0`, and if one sets `B_k = B/𝔐_k`,
`C_k = C/𝔑_k`, the transition homomorphisms `Ω^1_{C_{k+1}/B_{k+1}} → Ω^1_{C_k/B_k}`,
`Ω^1_{C_{k+1}/A} → Ω^1_{C_k/A}` and `Ω^1_{B_{k+1}/A} → Ω^1_{B_k/A}` are surjective `(20.7.14)`.

**Proposition (20.7.18).**

<!-- label: 0_IV.20.7.18 -->

*Let `A`, `B`, `C` be three topological rings, `u : A → B`, `v : B → C` two continuous homomorphisms. Suppose `B` and
`C` admissible `(0_I, 7.1.2)` and metrizable. For the canonical homomorphism
`v̂_{C/B/A} : Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ → Ω̂^1_{C/A}` to admit a left inverse that is a continuous `C`-homomorphism, it is
necessary and sufficient that `C` be a `B`-algebra formally smooth relative to `A`.*

The condition is necessary by virtue of `(20.7.2)` and `(19.1.6)`. To see that it is sufficient, note that the
topological `C`-module `L = Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ` is metrizable and complete by virtue of the hypothesis, hence
`E = D_C(L)`, equipped with the product topology, is

<!-- original page 153 -->

metrizable and complete; it is moreover admissible, for if `𝔎` is an ideal of definition in `C`, the sequence of
`(𝔎 ⊕ L)^n = 𝔎^n ⊕ 𝔎^{n-1}L` tends to `0`. Since the composite application

```text
  D : B  ──d_{B/A}──▸  Ω^1_{B/A}  ──▸  Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ = L
```

is a continuous `A`-derivation of `B` into `L`, the continuous `A`-homomorphism

```text
  f : x ↦ (v(x), D(x))
```

of `B` into `E` defines on `E` a structure of `B`-extension. Since `L` is a closed ideal in `E`, it follows from
`(19.9.5)` and from the hypothesis that the identity application `C → E/L` (which is a `B`-homomorphism) factors as
`C ──g──▸ E ──▸ E/L`, where `g` is a continuous homomorphism such that `g ∘ v = f`; consequently `(20.1.3)`, `g` is of
the form `y ↦ (y, D'(y))`, where `D'` is a continuous `B`-derivation of `C` into `L`, in other words `D' ∘ v = D`.
Taking into account `(20.7.14.4)`, one has `D' = h ∘ d̂_{C/A}`, where `h : Ω̂^1_{C/A} → L` is a continuous
`C`-homomorphism; but one has `d̂_{C/A} ∘ v = v̂_{C/B/A} ∘ d̂_{B/A}` by definition, and since the image of `B` under `D`
generates (topologically) the `C`-module `L` `(20.4.7)`, the relation `D' ∘ v = D` gives indeed `h ∘ v̂_{C/B/A} = 1_L`.
Q.E.D.

**Corollary (20.7.19).**

<!-- label: 0_IV.20.7.19 -->

*Under the hypotheses of `(20.7.18)`, if one supposes in addition that in `B` and `C` the square of an open ideal is
open, then, for `C` to be a `B`-algebra formally smooth relative to `A`, it is necessary and sufficient that
`v̂_{C/B/A}` be left-invertible.*

Indeed, the topologies of `Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ` and of `Ω̂^1_{C/A}` are then deduced from that of `C` `(20.4.5)`, and
every `C`-homomorphism of one into the other is necessarily continuous.

**(20.7.20)** Let `A` be a topological ring, `B` a topological `A`-algebra, metrizable and complete, `𝔍` a closed ideal
of `B`, `C = B/𝔍` the quotient topological ring, which is metrizable and complete. Let `(𝔐_k)` be a decreasing
fundamental system of neighbourhoods of `0` in `B` formed of ideals, and set `B_k = B/𝔐_k`, `𝔍_k = (𝔍 + 𝔐_k)/𝔐_k`,
`C_k = B_k/𝔍_k`. One has a projective system of homomorphisms
`δ_{C_k/B_k/A} : 𝔍_k/𝔍_k² → Ω^1_{B_k/A} ⊗_{B_k} C_k` `(20.5.11.3)`, from which one deduces by passing to the limit a
canonical homomorphism

```text
  δ̂_{C/B/A} : 𝔍/𝔍² → Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ
```

and reasoning as in `(20.7.17)`, one sees that the canonical homomorphism
`û_{C/B/A} : Ω̂^1_{B/A} ⊗̂_{B̂} Ĉ → Ω̂^1_{C/A}` is *surjective* and that `Im(δ̂_{C/B/A})` is *dense* in
`Ker(û_{C/B/A})`.

