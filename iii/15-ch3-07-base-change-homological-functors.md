# §7. Study of base change in the covariant homological functors of modules

<!-- original page 175 -->

## 7.1. Functors of `A`-modules.

**7.1.1.**

<!-- label: III.7.1.1 -->

Given a ring `A` (not necessarily commutative), we shall denote by `Ab_A` the category of left `A`-modules, and shall
denote simply by `Ab` the category of `Z`-modules, identical with commutative groups. Let `T : Ab_A → Ab` be a
*covariant additive functor*, and let `M` be an `(A, A)`-bimodule; `T(M)` is then naturally equipped with a structure of
right `A`-module. Indeed, for every `a ∈ A`, let us denote by `h_{a, M}` (or simply `h_a`) the endomorphism `x ↦ xa` of
the left `A`-module `M`. By hypothesis, `T(h_a)` is an endomorphism of the `Z`-module `T(M)`; moreover, since `T` is a
covariant additive functor, we have, for `a ∈ A`, `b ∈ A`,

```text
  T(h_{ab}) = T(h_b ∘ h_a) = T(h_b) ∘ T(h_a)   and   T(h_{a+b}) = T(h_a + h_b) = T(h_a) + T(h_b);
```

this proves that the map `(a, y) ↦ T(h_a)(y)` is an external composition law of right `A`-module on `T(M)`. In
particular, `T(A_s)` is a right `A`-module.

**7.1.2.**

<!-- label: III.7.1.2 -->

When `A` is a commutative ring, it follows from `(7.1.1)` that for every `A`-module `M`, `T(M)` is naturally equipped
with a structure of `A`-module; moreover, if `u : M → N` is a homomorphism of `A`-modules, we have, for every `a ∈ A`,
`u ∘ h_{a, M} = h_{a, N} ∘ u`, whence `T(u) ∘ T(h_{a, M}) = T(h_{a, N}) ∘ T(u)`, which proves that `T(u) : T(M) → T(N)`
is a homomorphism of `A`-modules; we thus see that `T` can be considered as a covariant additive functor from the
category `Ab_A` into itself. More precisely, we have thereby defined a canonical equivalence between the category of
covariant additive functors `Ab_A → Ab` and the category of covariant `A`-*linear* functors `T : Ab_A → Ab_A`, that is,
those such that `T(h_{a, M}) = h_{a, T(M)}` for every `a ∈ A`. Since the inclusion functor `I : Ab_A → Ab`, sending each
`A`-module to its underlying `Z`-module, is exact and faithful, the exactness properties of the two functors associated
by the preceding equivalence are the same.

**7.1.3.**

<!-- label: III.7.1.3 -->

The ring `A` still being assumed commutative, let `B` be an `A`-*algebra* (not necessarily commutative), and let
`ρ : A → B` be the ring homomorphism corresponding to this algebra structure; this homomorphism defines a covariant

<!-- original page 176 -->

additive functor `ρ_* : M ↦ M_{[ρ]}` from the category `Ab_B` of left `B`-modules into the category `Ab_A` of
`A`-modules. By composition, we deduce a functor `T_{(B)} : Ab_B →^{ρ_*} Ab_A →^T Ab`, evidently covariant and additive,
which we shall also denote by `T^{(B)}` (for typographical reasons) or `T ⊗_A B`, and which we shall say is *obtained
from* `T` *by extension of scalars from* `A` *to* `B`. Of course, if `B` is commutative, one can consider `T_{(B)}` as a
functor from `Ab_B` into itself `(7.1.2)`. When `B` is commutative and `C` a `B`-algebra, one sees at once that
`T_{(C)} = (T_{(B)})_{(C)}`; it is immediate that the extension of scalars is *functorial* and *additive* in `T`;
moreover, when `T` commutes with inductive limits or with direct sums (resp. is left exact, right exact, exact), the
same is true of `T_{(B)}`: indeed, `ρ_*` is exact and commutes with inductive limits and direct sums.

**7.1.4.**

<!-- label: III.7.1.4 -->

Suppose still that `A` is commutative, and let `T` be an `A`-linear covariant additive functor `Ab_A → Ab_A`, *commuting
with inductive limits*. Then, for every multiplicative subset `S` of `A` and every `A`-module `M`, we have a canonical
functorial isomorphism of `A`-modules

```text
  T(S⁻¹ M) ⥲ S⁻¹ T(M).                                                       (7.1.4.1)
```

Suppose first that `S` is the set of powers `f^n` (`n ≥ 0`) of an element `f ∈ A`. We know then that `M_f = lim→ M_n`,
where `(M_n, φ_{nm})` is the inductive system of `A`-modules `M_n = M`, with `φ_{nm} : z ↦ f^{n−m} z` `(0_I, 1.6.1)`;
whence in this case the isomorphism `(7.1.4.1)` by virtue of the hypothesis on `T`. If next `S` is arbitrary, `S⁻¹ M` is
the inductive limit of the `M_f` for `f ∈ S` `(0_I, 1.4.5)`, and one concludes in the same way. Moreover, the
functoriality of the isomorphism `(7.1.4.1)` shows that it is an isomorphism of `S⁻¹ A`-modules, and that one can
therefore write, up to a canonical isomorphism,

```text
  T_{(S⁻¹ A)}(S⁻¹ M) = S⁻¹ T(M) = T(S⁻¹ M).                                   (7.1.4.2)
```

When `S = A − 𝔭` is the complement of a prime ideal `𝔭` of `A`, one writes `T_𝔭` instead of `T_{(A_𝔭)}`.

**Proposition (7.1.5).**

<!-- label: III.7.1.5 -->

*Under the hypotheses of `(7.1.4)`, if `T_𝔪` is left exact (resp. right exact, exact) for every maximal ideal `𝔪` of
`A`, then `T` is left exact (resp. right exact, exact).*

**Proof.** We know in fact that when two submodules `N`, `P` of an `A`-module `M` are such that `N_𝔪 = P_𝔪` for every
maximal ideal `𝔪` of `A`, then `N = P` (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 3, th. 1).

## 7.2. Characterizations of the tensor product functor.

**7.2.1.**

<!-- label: III.7.2.1 -->

Let `A` be a ring (not necessarily commutative), `M` (resp. `N`) a left (resp. right) `A`-module, `P` a `Z`-module.
Recall that giving a `Z`-homomorphism `v : N ⊗_A M → P` is equivalent to giving a `Z`-bilinear map `u : N × M → P` such
that `u(ta, x) = u(t, ax)` for `a ∈ A`, `t ∈ N`, `x ∈ M`, the two maps being related by `v(t ⊗ x) = u(t, x)`. On the
other hand, giving `u` is equivalent to giving a

<!-- original page 177 -->

`Z`-homomorphism `x ↦ f_x` of `M` into `Hom_Z(N, P)` such that `f_{ax}(t) = f_x(ta)` for `a ∈ A`, `t ∈ N`, `x ∈ M`, the
two maps being related by `u(t, x) = f_x(t)`.

**7.2.2.**

<!-- label: III.7.2.2 -->

Let `T : Ab_A → Ab` be a covariant additive functor. We are going to define, for every left `A`-module `M`, a *canonical
homomorphism functorial in* `M`, of `Z`-modules

```text
  t_M : T(A_s) ⊗_A M → T(M).                                                 (7.2.2.1)
```

It will suffice for this, by virtue of `(7.2.1)`, to define a `Z`-homomorphism `x ↦ t'_M(x)` of `M` into
`Hom_Z(T(A_s), T(M))`, such that `t'_M(ax)(y) = t'_M(x)(ya)` for `a ∈ A`, `x ∈ M` and `y ∈ T(A_s)`. Note for this that
`Hom_Z(T(A_s), T(M))` is canonically equipped with a left `A`-module structure coming from the right `A`-module
structure of `T(A_s)`, the external law being such that if `a ∈ A`, `v ∈ Hom_Z(T(A_s), T(M))`, then `(a · v)(y) = v(ya)`
for `y ∈ T(A_s)`. This being so, we define `t'_M` as the composite of the two canonical homomorphisms

```text
  M ⥲ Hom_A(A_s, M) →^T Hom_Z(T(A_s), T(M)),
```

the second arrow being the map `u ↦ T(u)`, the first the canonical isomorphism of `A`-modules `x ↦ θ_x` such that
`θ_x(ξ) = ξx` for `ξ ∈ A`, `x ∈ M`. One has `θ_{ax} = θ_x ∘ h_a`, hence `T(θ_{ax}) = T(θ_x ∘ h_a) = T(θ_x) ∘ T(h_a)`,
and consequently, for `y ∈ T(A_s)`,

```text
  T(θ_{ax})(y) = T(θ_x)(T(h_a)(y)) = T(θ_x)(ya)
```

by definition of the external law on `T(A_s)`, which proves the existence of `t_M`; it is immediate to verify that this
homomorphism is functorial in `M`, that is, that for every homomorphism `w : M → M'` of left `A`-modules, the diagram

```text
                       t_M
  T(A_s) ⊗_A M  ─────────────→  T(M)
        │                        │
   1 ⊗ w│                        │T(w)                                       (7.2.2.2)
        ↓                        ↓
  T(A_s) ⊗_A M' ─────────────→  T(M')
                      t_{M'}
```

is commutative.

The functoriality of the homomorphism `(7.2.2.1)` shows that when `A` is commutative, it is a homomorphism of
`A`-modules (cf. `(7.1.2)`).

**7.2.3.**

<!-- label: III.7.2.3 -->

When `A` is commutative, one can more generally define a canonical homomorphism of `A`-modules

```text
  T(N) ⊗_A M → T(N ⊗_A M)                                                    (7.2.3.1)
```

for every `A`-module `N`; it suffices in the construction of `(7.2.2)` to replace the homomorphism `θ_x` by the
homomorphism of `A`-modules `N → N ⊗_A M` sending each `y ∈ N` to `y ⊗ x`. It is immediate that this homomorphism is
functorial in `M` and `N`.

<!-- original page 178 -->

In particular, if `B` is an `A`-algebra (not necessarily commutative), one has a homomorphism functorial in `M`

```text
  (T(M))_{(B)} = T(M) ⊗_A B → T(M ⊗_A B) = T_{(B)}(M_{(B)})                  (7.2.3.2)
```

which, by virtue of the functoriality of `(7.2.3.1)` in `M`, is a homomorphism of `B`-modules.

One has moreover the commutative diagram

```text
                       t_M
   T(A) ⊗_A M  ───────────────→  T(M)
        │                         │
        │                         │                                          (7.2.3.3)
        ↓                         ↓
   T_{(B)}(B_s) ⊗_B M_{(B)} ───→ T_{(B)}(M_{(B)})
                       t_{M_{(B)}}
```

where the right vertical arrow is the composite homomorphism

```text
  T(M) → T(M) ⊗_A B → T(M ⊗_A B) = T_{(B)}(M_{(B)})
```

of `(7.2.3.2)` and the canonical homomorphism; as for the left vertical arrow of `(7.2.3.3)`, it is the homomorphism
`T(A) ⊗_A M → T_{(B)}(B_s) ⊗_B (B ⊗_A M) = T_{(B)}(B_s) ⊗_A M`, where `T(A) → T_{(B)}(B_s) = T(B)` is `T(ρ)`, `ρ` being
considered as a homomorphism of `A`-modules `A → B_{[ρ]}`.

**Lemma (7.2.4).**

<!-- label: III.7.2.4 -->

*If `T` is a covariant additive functor from `Ab_A` into `Ab`, commuting with direct sums, the canonical homomorphism
`t_L` `(7.2.2.1)` is an isomorphism for every free `A`-module `L`.*

**Proof.** Indeed, one has `L = ⊕_{α ∈ I} L_α` where `L_α` is isomorphic to `A_s` for every `α ∈ I`; the definition of
`t_M` given in `(7.2.2)` shows that `t_L = ⊕_{α ∈ I} t_{L_α}`, since

```text
  T : Hom_A(A_s, L) → Hom_Z(T(A_s), T(L))
```

is the direct sum of the `Z`-linear maps `T_α : Hom_A(A_s, L_α) → Hom_Z(T(A_s), T(L_α))` by virtue of the hypothesis on
`T`. We are thus reduced to proving the lemma for `L = A_s`; but `t_L` is then none other than the canonical isomorphism
`T(A_s) ⊗_A A_s ⥲ T(A_s)` valid for every right `A`-module.

**Proposition (7.2.5).**

<!-- label: III.7.2.5 -->

*Let `T` be a covariant additive functor from `Ab_A` into `Ab`, commuting with direct sums. The following conditions are
equivalent:*

- *a) `T` is right exact.*
- *b) The canonical homomorphism `t_M` `(7.2.2.1)` is an isomorphism for every left `A`-module `M`.*
- *b') `T` is semi-exact and the homomorphism `t_M` is surjective for every left `A`-module `M`.*
- *c) `T` is isomorphic to a functor in `M` of the form `N ⊗_A M`, where `N` is a right `A`-module.*

**Proof.** It is clear that b) implies c) and that c) implies a); let us show that a) implies b).

<!-- original page 179 -->

Set `T'(M) = T(A_s) ⊗_A M` for every left `A`-module `M`. There exists an exact sequence `L' → L → M → 0`, where `L` and
`L'` are two free left `A`-modules; since `T` and `T'` are right exact, we have the commutative diagram

```text
  T'(L') → T'(L) → T'(M) → 0
    │        │       │
    │t_{L'}  │t_L    │t_M
    ↓        ↓       ↓
  T(L')  →  T(L)  →  T(M)  → 0
```

where the two rows are exact; since `t_L` and `t_{L'}` are isomorphisms by virtue of `(7.2.4)`, the same is true of
`t_M` by the five lemma. Finally, it is clear that b) implies b'). To show that b') implies a), it suffices to prove

**Lemma (7.2.5.1).**

<!-- label: III.7.2.5.1 -->

*Let `𝓚`, `𝓚'` be two abelian categories, `F`, `G` two covariant additive functors from `𝓚` into `𝓚'`, `f : F → G` a
functorial morphism `(T, I, 1.2)` such that, for every object `E` of the category `𝓚`, `f_E : F(E) → G(E)` is an
epimorphism. Then, if `F` is right exact and `G` semi-exact, `G` is right exact.*

**Proof.** It all comes down to showing that for every epimorphism `v : E' → E` in `𝓚`, `G(v) : G(E') → G(E)` is an
epimorphism; one has the commutative diagram

```text
            F(v)
  F(E') ─────────→  F(E)
   │                 │
   │f_{E'}           │f_E
   ↓                 ↓
  G(E') ─────────→  G(E)
            G(v)
```

in which `F(v)`, `f_{E'}` and `f_E` are epimorphisms; hence so is `G(v)`.

**Remark (7.2.6).**

<!-- label: III.7.2.6 -->

For every right `A`-module `N`, set `T_N(M) = N ⊗_A M` for every left `A`-module `M`, so that `T_N` is a covariant
additive functor from `Ab_A` into `Ab`, right exact and commuting with direct sums. If one canonically identifies
`T_N(A_s)` with `N`, one verifies at once that the corresponding homomorphism `(7.2.2.1)` becomes the identity. One
concludes that the right `A`-module `N` in the statement of `(7.2.5, c))` is determined up to unique isomorphism and is
canonically isomorphic to `T(A_s)`. One can also say that the functorial morphisms `T ↝ T(A_s)` and `N ↝ T_N` constitute
an equivalence `(T, I, 1.2)` of the category of right `A`-modules and the category of covariant additive functors
`Ab_A → Ab` that are right exact and commute with direct sums.

**Proposition (7.2.7).**

<!-- label: III.7.2.7 -->

*Let `A` be a left artinian ring whose quotient by its radical `𝔪` is a field `k`. Let `T` be a covariant additive
functor from `Ab_A` into `Ab`, commuting with direct sums. The conditions of `(7.2.5)` are then also equivalent to*

- *d) `T` is semi-exact and the homomorphism `T(ε) : T(A_s) → T(k)` deduced from the canonical homomorphism
    `ε : A_s → k` is surjective.*

<!-- original page 180 -->

**Proof.** It is clear that condition b') of `(7.2.5)` implies d); let us prove that d) implies b'). There exists an
integer `n` such that `𝔪^n = 0`; set, for every `A`-module `M`, `M_h = 𝔪^h M`; we shall prove by descending induction on
`h` that `t_{M_h}` is surjective. The proposition is evident for `h = n`; for `h < n`, one has an exact sequence

```text
  0 → M_{h+1} → M_h → M_h / M_{h+1} → 0
```

and the induction hypothesis implies that `t_{M_{h+1}}` is surjective. On the other hand, `M_h / M_{h+1}` is annihilated
by `𝔪` and is therefore an `(A/𝔪)`-module, in other words a direct sum of `A`-modules isomorphic to `k`. To prove that
`t_{M_h / M_{h+1}}` is surjective, it suffices therefore to prove that `t_k` is, since `T` commutes with direct sums.
Now, by virtue of the commutativity of the diagram

```text
                    t_{A_s}
  T(A_s) ⊗_A A_s ───────────→  T(A_s)
        │                        │
   1 ⊗ ε│                        │T(ε)
        ↓                        ↓
  T(A_s) ⊗_A k  ───────────→  T(k)
                     t_k
```

and of `(7.2.4)`, hypothesis d) implies that `t_k` is indeed surjective. To finish the proof, it will suffice to show
that if one has an exact sequence `0 → M' →^u M →^v M'' → 0` of `A`-modules, such that `t_{M'}` and `t_{M''}` are
surjective, then `t_M` is surjective. Now, one has a commutative diagram

```text
  T'(M') ────→ T'(M)  ────→ T'(M'') ────→ 0
    │           │            │
    │t_{M'}     │t_M         │t_{M''}
    ↓           ↓            ↓
  T(M')  ────→ T(M)   ────→ T(M'')  ────→ Coker(T(v))
                      T(v)
```

in which the two rows are exact, by virtue of the hypothesis that `T` is semi-exact. Since by the induction hypothesis
`t_{M'}` and `t_{M''}` are epimorphisms and the last vertical arrow is a monomorphism, the five lemma `(M, I, 1.1)`
shows that `t_M` is an epimorphism.

## 7.3. Exactness criteria for the homological functors of modules.

**Proposition (7.3.1).**

<!-- label: III.7.3.1 -->

*Let `A` be a ring (not necessarily commutative), `T_•` a covariant homological functor `(T, II, 2.1)` from the category
`Ab_A` into the category `Ab`, commuting with direct sums. Let `p` be an integer such that `T_p` and `T_{p−1}` are
defined. The following conditions are equivalent:*

- *a) `T_p` is right exact.*
- *b) `T_{p−1}` is left exact.*

<!-- original page 181 -->

- *c) For every left `A`-module `M`, the canonical functorial homomorphism `(7.2.2.1)`*
    ```text
      T_p(A_s) ⊗_A M → T_p(M)                                                (7.3.1.1)
    ```
    *is an isomorphism.*
- *d) For every left `A`-module `M`, the homomorphism `(7.3.1.1)` is an epimorphism.*
- *e) `T_p` is isomorphic to a functor `M ↦ N ⊗_A M`, where `N` is a right `A`-module.*

*If moreover the conditions of `(7.2.7)` on `A` and `𝔪` are satisfied, the preceding conditions are also equivalent to*

- *f) The canonical homomorphism `T_p(ε) : T_p(A_s) → T_p(k)` is an epimorphism.*

**Proof.** Since by definition of a homological functor, `T_i` is semi-exact for every `i` such that `T_i` is defined,
and since for every exact sequence `0 → M' →^u M →^v M'' → 0` one has `Ker(T_{i−1}(u)) = Coker(T_i(v))`, it is clear
that a) and b) are equivalent and the other assertions follow trivially from `(7.2.5)` and `(7.2.7)`.

**Corollary (7.3.2).**

<!-- label: III.7.3.2 -->

*Let `A` be a commutative ring. With the notations of `(7.3.1)`, suppose `T_p` is right exact. If `f ∈ A` does not
belong to the annihilator of any element `≠ 0` of an `A`-module `M`, then `f` does not belong to the annihilator of any
element `≠ 0` of `T_{p−1}(M)`. In particular, if `A` is an integral domain, the `A`-module `T_{p−1}(A)` is
torsion-free.*

**Proof.** Indeed, if `h_f` denotes the homothety `x ↦ fx` of `M`, the hypothesis means that `h_f` is injective; hence
so is `T_{p−1}(h_f)` by condition b) of `(7.3.1)`.

**Proposition (7.3.3).**

<!-- label: III.7.3.3 -->

*Let `A` be a ring, `T_•` a covariant homological functor from `Ab_A` into `Ab`, commuting with direct sums. Let `p` be
an integer such that `T_{p−1}`, `T_p` and `T_{p+1}` are defined. The following conditions are equivalent:*

- *a) `T_p` is exact.*
- *b) `T_{p+1}` and `T_p` are right exact.*
- *c) `T_p` and `T_{p−1}` are left exact.*
- *d) `T_{p+1}` is right exact and `T_{p−1}` is left exact.*
- *e) For every `A`-module `M`, the canonical homomorphisms*
    ```text
      T_i(A_s) ⊗_A M → T_i(M)                                                (7.3.3.1)
    ```
    *are isomorphisms for `i = p` and `i = p + 1`.*
- *e') For every `A`-module `M`, the canonical homomorphisms `(7.3.3.1)` are epimorphisms for `i = p` and `i = p + 1`.*
- *f) For every `A`-module `M`, the homomorphism `(7.3.3.1)` is an isomorphism for `i = p` and `T_p(A_s)` is a flat
    right `A`-module.*
- *f') For every `A`-module `M`, the homomorphism `(7.3.3.1)` is an epimorphism for `i = p` and `T_p(A_s)` is a flat
    right `A`-module.*

**Proof.** The equivalence of conditions a), b), c), d) results from the equivalence of conditions a) and b) of
`(7.3.1)`. The equivalence of b), e) and e') results from the equivalence of a), c) and d) in `(7.3.1)`. Finally, to say
that `T_p(A_s)` is flat means that the functor `M ↦ T_p(A_s) ⊗_A M` is left exact; the equivalence of a), f) and f')
again results from the equivalence of a), c), d) in `(7.3.1)`.

<!-- original page 182 -->

**Corollary (7.3.4).**

<!-- label: III.7.3.4 -->

*Suppose `A` commutative, `T_p` exact, and suppose moreover that `T_p(A)` is an `A`-module of finite presentation. Then
the function `x ↦ rang_{κ(x)}(T_p(κ(x)))` is locally constant on `X = Spec(A)`, hence constant if `Spec(A)` is
connected.*

**Proof.** Indeed, since `T_p(A)` is a flat `A`-module by virtue of `(7.3.3, f))`, it is projective of finite type, and
`(T_p(A))^∼` is therefore a locally free `𝒪_X`-module (Bourbaki, *Alg. comm.*, chap. II, § 5, n° 2, th. 1); one has
moreover `T_p(κ(x)) = T_p(A) ⊗_A κ(x)` `(7.3.3, e))` and we know that the rank at the point `x` of the `A`-module
`T_p(A)` is locally constant (*loc. cit.*), whence the corollary.

**Proposition (7.3.5).**

<!-- label: III.7.3.5 -->

*Suppose that `A` is a left artinian ring whose quotient by its radical `𝔪` is a field `k`. Then the conditions of
`(7.3.3)` are also equivalent to each of the following:*

- *g) The canonical homomorphism `T_i(ε) : T_i(A_s) → T_i(k)` is an epimorphism for `i = p` and `i = p + 1`.*
- *h) `T_p(ε)` is an epimorphism and `T_p(A_s)` is a flat right `A`-module (or, what amounts to the same (Bourbaki,
    *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5) a free `A`-module).*

*Suppose moreover that `A` is commutative and the `A`-module `T_p(k)` of finite length `d`. Then the preceding
conditions are also equivalent to each of the following:*

- *i) For every `A`-module `M` of finite length, one has*
    ```text
      long(T_p(M)) = d · long(M).                                            (7.3.5.1)
    ```
- *j) One has*
    ```text
      long(T_p(A)) = d · long(A).                                            (7.3.5.2)
    ```

**Proof.** The equivalence of g) and h) with the conditions of `(7.3.3)` follows immediately from `(7.2.7)`. To prove
the other assertions, we shall use the following lemma:

**Lemma (7.3.5.3).**

<!-- label: III.7.3.5.3 -->

*Let `𝓚`, `𝓚'` be two abelian categories, `F : 𝓚 → 𝓚'` a covariant additive functor; suppose that `F` is semi-exact, and
that, for every simple object `S` of `𝓚`, `F(S)` is an object of finite length in `𝓚'`. Then, for every object `E` of
finite length in `𝓚`, `F(E)` is of finite length in `𝓚'`. For every exact sequence `0 → E' →^u E →^v E'' → 0` of objects
of finite length in `𝓚`, one has*

```text
  long F(E) ≤ long F(E') + long F(E'')                                       (7.3.5.4)
```

*and for the two members of `(7.3.5.4)` to be equal, it is necessary and sufficient that the sequence*

```text
  0 → F(E') → F(E) → F(E'') → 0
```

*be exact.*

**Proof.** Indeed, the sequence `F(E') →^{F(u)} F(E) →^{F(v)} F(E'')` is exact by hypothesis; if one supposes `F(E')`
and `F(E'')` of finite length, the same is true of `Im(F(u))` and `Im(F(v))`, and since `Ker(F(v)) = Im(F(u))`, `F(E)`
is of finite length and one has

```text
  long F(E) = long Im(F(u)) + long Im(F(v)) ≤ long F(E') + long F(E'').      (7.3.5.5)
```

<!-- original page 183 -->

By induction on the length of `E`, this already proves the first assertion; moreover, the two members of `(7.3.5.5)` can
be equal only if `long Im(F(u)) = long F(E')` (which is equivalent to `long Ker(F(u)) = 0`, or `Ker(F(u)) = 0`) and
`long Im(F(v)) = long F(E'')` (which is equivalent to `long Coker(F(v)) = 0`, or `Coker(F(v)) = 0`).

We now note that if `M` is an `A`-module of finite length (`A` being commutative), the quotients of a Jordan–Hölder
sequence of `M` are necessarily isomorphic to the `A`-module `k`; therefore, by `(7.3.5.4)` and induction on the length
of `M`,

```text
  long T_p(M) ≤ d · long(M).                                                 (7.3.5.6)
```

Moreover, it follows from `(7.3.5.3)` that if `T_p` is exact, one has the equality `(7.3.5.1)`; hence condition a) of
`(7.3.3)` implies i); it is clear that i) implies j), and it remains to prove

**Lemma (7.3.5.7).**

<!-- label: III.7.3.5.7 -->

*The relation `long T_p(A) = d · long A` implies that `T_p(ε)` is an epimorphism and that `T_p(A)` is a flat
`A`-module.*

**Proof.** Indeed, starting from the exact sequence `0 → 𝔪 → A → k → 0`, it follows from `(7.3.5.4)` and `(7.3.5.6)`
that one has

```text
  long T_p(A) ≤ long T_p(𝔪) + long T_p(k) ≤ d(long 𝔪 + long k) = d · long A
```

and that equality can hold `(7.3.5.3)` only if the sequence

```text
  0 → T_p(𝔪) → T_p(A) → T_p(k) → 0                                           (7.3.5.8)
```

is exact. By virtue of `(7.2.7)` and `(7.2.5)`, `T_p` is isomorphic to a functor `M ↦ N ⊗_A M`, and the exactness of the
sequence `(7.3.5.8)` shows, by virtue of the exact sequence of Tor's, that one has `Tor_1^A(N, k) = 0`. One concludes
that `N = T_p(A)` is a flat `A`-module `(0_I, 10.1.3)`.

**Lemma (7.3.6).**

<!-- label: III.7.3.6 -->

*Let `A` be a ring, `T_•` a covariant homological functor from `Ab_A` into `Ab`, commuting with direct sums. Suppose
`T_p` and `T_{p+1}` defined, and `T_p` left exact. For `T_{p+1}` to be exact, it is necessary and sufficient that
`T_{p+1}(A_s)` be a flat right `A`-module.*

**Proof.** Indeed, one knows by `(7.3.1)` that the canonical homomorphism

```text
  T_{p+1}(A_s) ⊗_A M → T_{p+1}(M)
```

is an isomorphism of functors; it suffices to apply the definition of a flat `A`-module.

**Proposition (7.3.7).**

<!-- label: III.7.3.7 -->

*Let `A` be a ring, `T_•` a covariant homological functor from `Ab_A` into `Ab`, commuting with direct sums. Suppose
there exists `i_0` such that `T_i` is exact for `i ≤ i_0`. Then, for every integer `p > i_0`, the following conditions
are equivalent:*

- *a) `T_q` is exact for `q ≤ p`;*
- *b) `T_q(A_s)` is a flat right `A`-module for `q ≤ p`.*
- *c) For every `A`-module `M`, the canonical homomorphism `T_q(A_s) ⊗_A M → T_q(M)` is surjective for `q ≤ p + 1`.*

**Proof.** The equivalence of a) and b) results from `(7.3.6)` by induction on `q`, since `T_{i_0}` is exact by
hypothesis; the equivalence of a) and c) results from the equivalence of conditions a) and e') in `(7.3.3)`.

<!-- original page 184 -->

**7.3.8.**

<!-- label: III.7.3.8 -->

If `A` is a commutative ring, `B` an `A`-algebra (not necessarily commutative), `T_•` a covariant homological functor
from `Ab_A` into `Ab`, it follows from the definitions `(7.1.3)` that the functor from `Ab_B` into `Ab` obtained by
extension of scalars from `A` to `B`, and which we shall denote `T_•^{(B)} = (T_•)_{(B)}`, is again a *homological*
functor.

**Corollary (7.3.9).**

<!-- label: III.7.3.9 -->

*Suppose that `T_•` satisfies the general conditions of `(7.3.7)` and commutes with inductive limits, and moreover that
`A` is an integral ring and all the `T_n(A)` are `A`-modules of finite presentation. Then, for every integer `N`, there
exists `f ∈ A − {0}` such that the functor `T_•^{(A_f)} : Ab_{A_f} → Ab` is exact for `p ≤ N`.*

**Proof.** By hypothesis, `T_i` is exact for `i ≤ i_0`, hence `T_i(A)` is flat for these values of `i`. By virtue of
`(7.3.7, b))`, it suffices to take `f` such that `T_p^{(A_f)}(A_f) = T_p(A_f)` is a free `A_f`-module for `i_0 < p ≤ N`.
Now, one has `T_p(A_f) = (T_p(A))_f` since `T_p` commutes with inductive limits `(7.1.4)`. If `x` is the generic point
of `Spec(A)`, `(T_p(A))_x` is a finite-dimensional vector space over the fraction field of `A`. Since each `T_p(A)` is
of finite presentation, there does indeed exist an `f` with the desired property (Bourbaki, *Alg. comm.*, chap. II, § 5,
n° 1, cor. of prop. 2).

One will note that if there are only finitely many indices `i` such that `T_i ≠ 0`, there exists `f ∈ A − {0}` such that
*all* the `T_p^{(A_f)}` are exact.

**Corollary (7.3.10).**

<!-- label: III.7.3.10 -->

*Suppose that `T_•` satisfies the general conditions of `(7.3.7)` and commutes with inductive limits, that `A` is
commutative and noetherian, and the `T_n(A)` `A`-modules of finite type. Then, for every integer `N`, there exists a
dense open set `U` of `Spec(A)` such that, for every `p ≤ N`, the function `x ↦ rang_{κ(x)}(T_p(κ(x)))` is constant on
`U`.*

**Proof.** Let `𝔭` be a minimal prime ideal of `A`; by hypothesis, the ring `B = A/𝔭` is integral and `Spec(B)` is
identified with an irreducible component of the topological space `Spec(A)`. We shall show by induction on `p ≤ N` that
there exists `f_p ∈ B − {0}` such that, on setting `B' = B_{f_p}`, `T_i^{(B')}` is exact and the `T_i(B')` are
`B'`-modules of finite type for `i ≤ p`. The proposition is true for `p ≤ i_0` by virtue of the hypothesis, taking
`f_p = 1` (hence `B' = B = A/𝔭`): for `T_p` being then exact, `T_p(B)` is isomorphic to `T_p(A)/T_p(𝔭)`, hence is an
`A`-module (and a fortiori a `B`-module) of finite type. Let us argue by induction on `p`; `f_p` is the canonical image
in `B` of an element `g_p ∈ A`, and if one sets `A' = A_{g_p}`, one has `B' = A'/𝔭'` where `𝔭'` is a minimal prime ideal
of `A'`, equal to `𝔭_{g_p}`. Since `T_i(A_{g_p}) = (T_i(A))_{g_p}`, the `T_i(A')` are `A'`-modules of finite type, so
the functor `T_•^{(A')}` satisfies the same hypotheses as `T_•`, but replacing `i_0` by `p`. One can therefore restrict
to the case where `A' = A` and where `T_p` is exact; the exact sequence `0 → 𝔭 → A → A/𝔭 → 0` then gives the exact
sequence `T_{p+1}(A) → T_{p+1}(A/𝔭) →^∂ T_p(𝔭) → T_p(A)`, and since `T_p` is exact, the rightmost arrow is injective,
hence `T_{p+1}(A/𝔭)` is a quotient of `T_{p+1}(A)` and is consequently of finite type. We now note that the argument of
`(7.3.9)` used the fact that the `T_p(A)` are of finite type only for `p ≤ N`; one can therefore apply it to the
integral ring `B`, the functor `T_•^{(B)}` and `N = p + 1`, which completes the induction. This being so, there exists
`f_N ∈ B − {0}` such that `Spec(B_{f_N})` is an open set `V` everywhere dense in `Spec(B)` meeting no other irreducible
component of `Spec(A)`. If the proposition

<!-- original page 185 -->

is proved for `B_{f_N}`, one will have an open set `W` everywhere dense in `V` in which the functions of the statement
will be constant, since `A_x = (B_{f_N})_x` for every `x ∈ W`. Doing the same reasoning for every irreducible component
of `Spec(A)`, the corollary will be proved. One can therefore restrict to the case where `A` is integral; the reasoning
of `(7.3.9)` then proves the existence of `f ∈ A − {0}` such that the `T_p(A_f)` are free `A_f`-modules of finite type
for `p ≤ N`, which entails the conclusion of `(7.3.10)` by virtue of `(7.3.4)`.

**Proposition (7.3.11).**

<!-- label: III.7.3.11 -->

*Let `A` be a commutative local ring, `k` its residue field, `T_•` a covariant homological functor from `Ab_A` into
`Ab`, commuting with direct sums. Suppose that there exists `i_0` such that `T_i` is exact for `i ≤ i_0`, and that all
the `T_n(A)` are `A`-modules of finite presentation. Then the equivalent conditions a), b), c) of `(7.3.7)` imply the
two following ones, and are equivalent to them when the ring is moreover reduced:*

- *d) For every `x ∈ Spec(A)`, one has `rang_{κ(x)} T_q(κ(x)) = rang_k T_q(k)` for `q ≤ p`.*
- *d') For every generic point `x_j` of an irreducible component of `Spec(A)`, one has*
    ```text
      rang_{κ(x_j)} T_q(κ(x_j)) = rang_k T_q(k)   for q ≤ p.
    ```

**Proof.** Since `T_q(A)` is an `A`-module of finite presentation, condition b) of `(7.3.7)` is equivalent to saying
that `T_q(A)` is a *free* `A`-module for `q ≤ p` (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5);
condition c) implies that `T_q(κ(x)) = T_q(A) ⊗_A κ(x)` for `q ≤ p`, hence the equivalent conditions of `(7.3.7)` imply
d), and it is trivial that d) implies d'). It remains to prove that d') implies a) when `A` is *reduced*. We argue by
induction on `q ≤ p`, since `T_q` is exact for `q ≤ i_0`. Suppose then that `T_k` is exact for `k ≤ q < p` and let us
show that `T_{q+1}(A)` is a free `A`-module. By virtue of the induction hypothesis, `T_{q+1}(A) ⊗_A M` is isomorphic to
`T_{q+1}(M)` for every `A`-module `M`, by condition c) of `(7.3.7)` and `(7.3.3)`; applying this property to
`M = κ(x_j)` and `M = k`, one finds, by virtue of hypothesis d'), that

```text
  rang_{κ(x_j)} (T_{q+1}(A) ⊗_A κ(x_j)) = rang_k T_{q+1}(k)
```

for every `j`; but this implies that `T_{q+1}(A)` is free (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, prop. 7), which
completes the proof.

The preceding results will be considerably improved for the homological functors of particular type that we shall study
in `(7.4)`; we shall obtain in fact exactness criteria involving only one of the `T_p`.

## 7.4. Exactness criteria for the functors `H_•(P_• ⊗_A M)`.

**7.4.1.**

<!-- label: III.7.4.1 -->

Let `A` be a ring (not necessarily commutative), `P_•` a complex of flat right `A`-modules. Since the functor
`M ↦ P_k ⊗_A M` is then exact on `Ab_A` for every `k`, the `∂`-functor

```text
  T_•(M) = H_•(P_• ⊗_A M)                                                    (7.4.1.1)
```

<!-- original page 186 -->

is a homological functor from `Ab_A` into `Ab`, evidently `A`-linear when `A` is commutative `(7.1.2)`, and commuting
with inductive limits.

If `A` is commutative, then, for every `A`-algebra `B`, the homological functor `T_•^{(B)}` `(7.3.8)` is given by
definition by

```text
  T_•^{(B)}(N) = H_•(P_• ⊗_A N_{[ρ]})                                        (7.4.1.2)
```

where `ρ : A → B` is the homomorphism defining the algebra structure of `B`; since one can also write
`P_• ⊗_A N_{[ρ]} = P_• ⊗_A (B ⊗_B N)_{[ρ]} = (P_• ⊗_A B) ⊗_B N`, one sees that one has

```text
  T_•^{(B)}(N) = H_•(P'_• ⊗_B N)                                             (7.4.1.3)
```

for every `B`-module `N`, `P'_•` being the complex `P_• ⊗_A B` of flat `B`-modules `(0_I, 6.2.1)`.

**Proposition (7.4.2).**

<!-- label: III.7.4.2 -->

*Under the general conditions of `(7.4.1)`, and for a given integer `p ∈ Z`, the following properties are equivalent:*

- *a) `T_p` is left exact (or, what amounts to the same, `T_{p+1}` is right exact).*
- *b) `Z'_p(P_•) = Coker(P_{p+1} → P_p)` is a flat right `A`-module.*
- *c) There exists a complex `P'_•` of flat right `A`-modules such that the differential*
    ```text
      d'_{p+1} : P'_{p+1} → P'_p
    ```
    *is zero, and an isomorphism of homological functors from `H_•(P_• ⊗_A M)` onto `H_•(P'_• ⊗_A M)`.*

**Proof.** By definition, one has an exact sequence functorial in `M`

```text
  0 → T_p(M) → Z'_p(P_• ⊗ M) → P_{p−1} ⊗ M
```

where `Z'_p(P_• ⊗ M) = Coker(P_{p+1} ⊗ M → P_p ⊗ M) = Z'_p(P_•) ⊗ M` by virtue of the right exactness of the tensor
product. For every homomorphism `f : M → N`, one therefore has a commutative diagram

```text
  0 → T_p(M) ──── Z'_p(P_•) ⊗ M ──── P_{p−1} ⊗ M
        │              │                │
        │u             │v               │w                                   (7.4.2.1)
        ↓              ↓                ↓
  0 → T_p(N) ──── Z'_p(P_•) ⊗ N ──── P_{p−1} ⊗ N
```

whose rows are exact. If `f` is a monomorphism, so is `w` since `P_{p−1}` is flat; if `T_p` is left exact, `u` is also a
monomorphism; one concludes that `v` is a monomorphism, which implies that `Z'_p(P_•)` is flat. Conversely, if it is so,
`v` is a monomorphism for every monomorphism `f : M → N`, hence the diagram `(7.4.2.1)` shows that `u` is a
monomorphism, and consequently `T_p` (which is already semi-exact) is left exact. Thus a) and b) are equivalent. It is
immediate that c) implies a), for if `d'_{p+1} : P'_{p+1} → P'_p` is zero, and `0 → M' → M → M'' → 0` is an exact
sequence of `A`-modules, the boundary operator `∂` in the exact sequence

```text
  H_{p+1}(P'_• ⊗ M'') →^∂ H_p(P'_• ⊗ M') → H_p(P'_• ⊗ M)
```

<!-- original page 187 -->

is zero by definition `(M, IV, 1)`, hence `T_p` is left exact. Let us show conversely that b) implies c). If
`Z_{p+1}(P_•) = Ker(P_{p+1} → P_p)`, one has an exact sequence

```text
  0 → Z_{p+1}(P_•) → P_{p+1} → Z'_p(P_•) → 0
```

in which `P_{p+1}` and `Z'_p(P_•)` are flat, hence `Z_{p+1}(P_•)` is flat `(0_I, 6.1.2)`. We shall take

```text
  P'_i = P_i  for  i ≠ p  and  i ≠ p+1,   P'_p = Z'_p(P_•)  and  P'_{p+1} = Z_{p+1}(P_•);
```

for the differential `d'_i : P'_i → P'_{i−1}`, we shall take that of the complex `P_•` for `i ≠ p` and `i ≠ p + 1`, `0`
for `i = p + 1` and for `i = p` the homomorphism `Z'_p(P_•) → P_{p−1}` deduced from `d_p` by passage to the quotient.
Since the `P_i` are flat, one has

```text
  Z'_i(P_• ⊗ M) = Z'_i(P_•) ⊗ M,  Z_i(P_• ⊗ M) = Z_i(P_•) ⊗ M  and  B_i(P_• ⊗ M) = B_i(P_•) ⊗ M
```

(setting `B_i(P_•) = Im(P_{i+1} → P_i)`); one concludes at once for every `M` the functorial isomorphisms
`H_i(P_• ⊗ M) ⥲ H_i(P'_• ⊗ M)` for every `i`, and the verification of the fact that this is an isomorphism of
`∂`-functors follows without difficulty from the definition of `∂` `(M, IV, 1)`.

One notes that the conditions of `(7.4.2)` also imply that `B_p(P_•)` is flat, for one has an exact sequence
`0 → B_p(P_•) → P_p → Z'_p(P_•) → 0`, in which `P_p` and `Z'_p(P_•)` are flat `(0_I, 6.1.2)`.

**Corollary (7.4.3).**

<!-- label: III.7.4.3 -->

*Suppose that `A` is a noetherian regular ring of dimension 1 (in other words a product of Dedekind rings
`(0_IV, 17.1.3 and 17.3.7)`, for example a principal ring). Then, for `T_p` to be left exact, it is necessary and
sufficient that `T_p(A)` be a flat `A`-module. For `T_p` to be exact, it is necessary and sufficient that `T_p(A)` and
`T_{p−1}(A)` be flat `A`-modules.*

**Proof.** Recall that for a module `M` over a Dedekind ring, it amounts to the same to say that `M` is flat or that it
is torsion-free `(0_I, 6.3.3 and 6.3.4)`; under the hypotheses of `(7.4.3)`, every submodule of a flat `A`-module is
therefore flat.

The second assertion of `(7.4.3)` results from the first, since to say that `T_p` is exact means that `T_p` and
`T_{p−1}` are left exact. To prove the first assertion, note that one has an exact sequence

```text
  0 → H_p(P_•) → Z'_p(P_•) → B_{p−1}(P_•) → 0
```

in which `B_{p−1}(P_•)` is a flat `A`-module, as a submodule of the flat `A`-module `P_{p−1}`. It is therefore
equivalent to say that `H_p(P_•)` is flat or that `Z'_p(P_•)` is flat `(0_I, 6.1.2)`.

The most important applications of `(7.4.2)` are the following:

**Proposition (7.4.4).**

<!-- label: III.7.4.4 -->

*Let `A` be a noetherian ring, `P_•` a complex of flat `A`-modules: suppose, either that the `P_i` are of finite type,
or that the `H_i(P_•)` are `A`-modules of finite type and that there exists `i_0` such that `H_i(P_•) = 0` for
`i < i_0`. Let `T_•` be the homological functor defined by `(7.4.1.1)`. Then the set `U` of `y ∈ Spec(A)` such that
`(T_p)_y` `(7.1.4)` is right exact (resp. left exact, exact) is open in `Spec(A)`.*

**Proof.** In the second hypothesis on `P_•`, one can replace `P_•` by a complex `P'_•` of

<!-- original page 188 -->

free `A`-modules of finite type for which the functor `H_•(P'_• ⊗_A M)` is isomorphic (as a `∂`-functor) to `T_•(M)`
`(0, 11.9.3)`. One can therefore always reduce to the first hypothesis, and in this case the `Z'_p(P_•)` are of finite
type; moreover, one can restrict to proving the assertions relative to left exactness (cf. `(7.4.2, a))`). This being
so, let `x ∈ U`; since the functor `M ↦ M_x` is exact, one has `(Z'_p(P_•))_x = Z'_p((P_•)_x)`, and (taking `(7.4.1.3)`
into account) the hypothesis implies, by virtue of `(7.4.2, b))`, that `(Z'_p(P_•))_x` is a flat `A_x`-module, hence
free since it is of finite type and `A_x` is a noetherian local ring (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor.
2 of prop. 5). One concludes that there is `f ∈ A` such that `(Z'_p(P_•))_f` is free over `A_f` (Bourbaki, *Alg. comm.*,
chap. II, § 5, n° 1, cor. of prop. 2), and a fortiori `(Z'_p(P_•))_y` is free over `A_y` for every `y ∈ D(f)`, which
completes the proof by virtue of `(7.4.2, b))`.

**Corollary (7.4.5).**

<!-- label: III.7.4.5 -->

*Under the hypotheses of `(7.4.4)`, suppose moreover that `A` is integral. Then the set `U` of `x ∈ Spec(A)` such that
`(T_p)_x` is exact is open and non-empty.*

**Proof.** It suffices to prove that `(T_p)_x` is exact for the generic point `x` of `Spec(A)`, which is immediate since
`A_x` is a field, hence every additive functor on `Ab_{A_x}` is exact.

**Proposition (7.4.6).**

<!-- label: III.7.4.6 -->

*Under the general hypotheses of `(7.4.4)`, conditions a), b) and c) of `(7.4.2)` are also equivalent to:*

- *d) There exists an `A`-module `Q` and a functorial isomorphism*
    ```text
      T_p(M) ⥲ Hom_A(Q, M).                                                  (7.4.6.1)
    ```

*Moreover, the `A`-module `Q` is determined up to unique isomorphism by this property, and it is of finite type.*

**Proof.** The uniqueness of `Q` is a particular case of the uniqueness of a representative object of a representable
functor `(0, 8.1.5)`. It is clear that the second member of `(7.4.6.1)` is left exact. Conversely, to prove the
existence of `Q`, when `T_p` is left exact, one can first, as in `(7.4.4)`, reduce to the case where the `P_i` are flat
and of finite type, hence (since `A` is noetherian) *projective of finite type* (Bourbaki, *Alg. comm.*, chap. II, § 5,
n° 2, cor. of th. 1). The *dual* `P̌_i` of `P_i` is then also a projective `A`-module of finite type, `P_i` is
canonically isomorphic to the dual of `P̌_i`, and the canonical homomorphism `P_i ⊗_A M → Hom_A(P̌_i, M)` is bijective
(Bourbaki, *Alg.*, chap. II, 3rd ed., § 4, n° 2, prop. 2). One knows on the other hand `(7.4.2, c))` that one can
suppose `d_{p+1} : P_{p+1} → P_p` is zero, hence one has an exact sequence

```text
  0 → T_p(M) → P_p ⊗ M →^v P_{p−1} ⊗ M
```

where `v = d_p ⊗ 1`. Set then `Q' = Ker(d_p)`, so that one has the exact sequence `0 → Q' →^w P_p →^{d_p} P_{p−1}`,
whence by transposition the exact sequence `P̌_{p−1} →^{ᵗd_p} P̌_p →^{ᵗw} Q̌' → 0`. We shall see that
`Q = Q̌' = Coker(ᵗd_p)` answers the question. Indeed, one has the exact sequence

```text
  0 → Hom(Q, M) → Hom(P̌_p, M) →^{v'} Hom(P̌_{p−1}, M)
```

<!-- original page 189 -->

where `v' = Hom(ᵗd_p, 1)`; when one canonically identifies `P_i ⊗ M` to `Hom(P̌_i, M)`, `v'` is therefore identified
with `v = d_p ⊗ 1`, and one has consequently the functorial isomorphism `T_p(M) ⥲ Hom_A(Q, M)` sought. Moreover, `Q`,
being a quotient of `P̌_p`, is of finite type.

**Proposition (7.4.7).**

<!-- label: III.7.4.7 -->

*Suppose the general conditions of `(7.4.4)` satisfied. Then, for every `A`-module `M` of finite type:*

- *(i) The `T_i(M)` are `A`-modules of finite type.*
- *(ii) For every ideal `𝔪` of `A`, the canonical homomorphism*
    ```text
      (T_i(M))^∧ → lim←_n T_i(M ⊗_A (A/𝔪^{n+1}))                             (7.4.7.1)
    ```
    *(where the left member is the Hausdorff completion of `T_i(M)` for the `𝔪`-preadic topology) is bijective.*

**Proof.** As in `(7.4.4)`, one reduces first to the case where the `P_i` are of finite type; `A` being noetherian, the
submodules of `P_i ⊗_A M` are of finite type, whence trivially assertion (i). As for assertion (ii), it follows more
generally from the following lemma:

**Lemma (7.4.7.2).**

<!-- label: III.7.4.7.2 -->

*Let `A` be a noetherian ring, `u : E → F` a homomorphism of `A`-modules of finite type. For every `A`-module of finite
type, set `K(M) = Ker(u ⊗ 1_M)`, `C(M) = Coker(u ⊗ 1_M)`; then the canonical homomorphisms*

```text
  (K(M))^∧ → lim←_n K(M_n),    (C(M))^∧ → lim←_n C(M_n)                      (7.4.7.3)
```

*(where one has set `M_n = M ⊗_A (A/𝔪^{n+1}) = M/𝔪^{n+1} M`) are bijective for every ideal `𝔪` of `A`.*

**Proof.** Since `E ⊗ M` and `F ⊗ M` are of finite type, and the functor `M ↦ M̂` is exact in the category of
`A`-modules of finite type `(0_I, 7.3.3)`, `(K(M))^∧` and `(C(M))^∧` are respectively the kernel and the cokernel of
`(u ⊗ 1)^∧ : (E ⊗ M)^∧ → (F ⊗ M)^∧`. The left exactness of the functor `lim←` shows therefore that
`(K(M))^∧ = lim←_n K(M_n)`; on the other hand, the right exactness of the tensor product proves that
`C(M_n) = C(M) ⊗_A (A/𝔪^{n+1})`, hence `(C(M))^∧ = lim←_n C(M_n)` by definition.

**Remark (7.4.8).**

<!-- label: III.7.4.8 -->

Taking `(6.10.5)` and `(6.10.6)` into account, one sees that, given an additional flatness hypothesis, `(7.4.7)` gives
back the fact that `(4.1.7.1)` is an isomorphism, that is, the essence of the "first comparison theorem" for proper
morphisms; moreover, the statement applies not only to a coherent `𝒪_X`-module, but to a *complex* of such modules. It
would be interesting to obtain a statement comprising at the same time `(7.4.7)` and `(4.1.7.1)` as particular cases.
One will note that when the `P_i` are of finite type, the proof of `(7.4.7)` does not use the fact that they are flat
modules; it would be worthwhile examining whether the conclusion of `(7.4.7)` is still valid when the `P_i` are not
supposed flat nor of finite type, but the `H_i(P_•)` are supposed of finite type for every `i` and zero for `i < i_0`.
Is it then possible to replace `P_•` by a complex `P'_•` of `A`-modules of finite type such that the functors
`H_•(P_• ⊗ M)` and `H_•(P'_• ⊗ M)` (which are no longer homological) are still isomorphic?

<!-- original page 190 -->

## 7.5. The case of noetherian local rings.

**7.5.1.**

<!-- label: III.7.5.1 -->

Let `A` be a noetherian local ring, `𝔪` its maximal ideal, and for every `A`-module `M`, denote by `M̂` its Hausdorff
completion for the `𝔪`-preadic topology, isomorphic to `lim←(M ⊗_A (A/𝔪^{n+1})) = lim←(M/𝔪^{n+1} M)`. Let `T` be a
covariant additive functor from `Ab_A` into `Ab`; the canonical homomorphisms `(7.2.3.1)`

```text
  T(M) ⊗_A (A/𝔪^{n+1}) → T(M ⊗_A (A/𝔪^{n+1}))
```

evidently form a projective system of `A`-homomorphisms, which thus give in the limit an `Â`-homomorphism functorial in
`M`

```text
  (T(M))^∧ → lim←_n T(M_n)                                                   (7.5.1.1)
```

where one has set `M_n = M ⊗_A (A/𝔪^{n+1})`, `A_n = A/𝔪^{n+1}`.

**Proposition (7.5.2).**

<!-- label: III.7.5.2 -->

*Let `A` be a noetherian local ring with maximal ideal `𝔪`, `k = A/𝔪` its residue field, `T` a covariant additive
functor from `Ab_A` into `Ab`, semi-exact and commuting with inductive limits. Suppose moreover that for every
`A`-module of finite type `M`, `T(M)` is an `A`-module of finite type and that the canonical homomorphism `(7.5.1.1)` is
an isomorphism. Under these conditions, the following properties are equivalent:*

- *a) `T` is right exact.*
- *b) For every `n`, the functor `N ↦ T(N)` is right exact in the category of `A_n`-modules of finite type (which
    amounts to saying that `T` is right exact in the category of `A`-modules of finite length).*
- *c) The canonical homomorphism `T(ε) : T(A) → T(k)` is surjective.*
- *d) For every `n` sufficiently large, the canonical homomorphism `T(A_n) → T(k)` is surjective.*

**Proof.** It is clear that a) implies b). Let us show that b) implies a), that is, that if `u : M → N` is an
epimorphism of `A`-modules, `T(u)` is an epimorphism. Since `T` commutes with inductive limits and the functor `lim→` is
exact in the category of modules (for filtered index sets), one can restrict to the case where `M` and `N` are of finite
type. Since `T(M)` and `T(N)` are then of finite type, and `A` is a noetherian local ring, it suffices to show that
`(T(u))^∧ : (T(M))^∧ → (T(N))^∧` is surjective `(0_I, 7.3.5 and 0_I, 6.4.1)`. By hypothesis, `(T(M))^∧` and `(T(N))^∧`
are respectively `lim←_n T(M_n)` and `lim←_n T(N_n)`, hence `(T(u))^∧` is the limit of the projective system of
homomorphisms `T(u ⊗ 1_{A_n}) : T(M_n) → T(N_n)`. Now, b) means that these homomorphisms are surjective; moreover,
`T(M_n)` is an `A_n`-module of finite type, and `A_n` is an artinian ring by hypothesis; one concludes that `(T(u))^∧`
is surjective `(0, 13.1.2 and 13.2.2)`. It is clear that a) implies c), and since `T(ε)` factors as
`T(A) → T(A_n) → T(k)`, c) implies d); finally, it follows from `(7.2.7)` that b) and d) are equivalent since `T` is
semi-exact in `Ab_{A_n}`, which completes the proof.

**Corollary (7.5.3).**

<!-- label: III.7.5.3 -->

*Under the general hypotheses of `(7.5.2)`, if `T(k) = 0`, then `T(M) = 0` for every `A`-module `M`.*

<!-- original page 191 -->

**Proof.** Since `k` is the only simple `A`-module, one deduces from `(7.3.5.4)` that `T(E) = 0` for every `A`-module of
finite length `E`. If now `M` is of finite type, `(T(M))^∧` is isomorphic to `lim←_n T(M_n)`, and since the `M_n` are of
finite length, one has `(T(M))^∧ = 0`; since `T(M)` is of finite type by hypothesis, it is isomorphic to a submodule of
`(T(M))^∧` `(0_I, 7.3.5)`, hence one has `T(M) = 0`. Finally, for an arbitrary `A`-module `M`, `T(M)` is the inductive
limit of the `T(N_α)` for the submodules of finite type `N_α` of `M`, which completes the proof.

**Proposition (7.5.4).**

<!-- label: III.7.5.4 -->

*Let `A` be a noetherian local ring with maximal ideal `𝔪`, `k = A/𝔪` its residue field, `T_•` a homological functor
from `Ab_A` into `Ab`, commuting with inductive limits. Suppose moreover that for every `i` and every `A`-module `M` of
finite type, `T_i(M)` is of finite type and the canonical homomorphism `(T_i(M))^∧ → lim←_n T_i(M_n)` is bijective. For
a given integer `p`, the following conditions are then equivalent:*

- *a) `T_p` is exact.*
- *b) `T_p` is right exact, and `T_p(A)` is a free `A`-module.*
- *c) The canonical homomorphisms `T_{p+1}(A) → T_{p+1}(k)` and `T_p(A) → T_p(k)` are surjective.*
- *d) For every `n`, the canonical homomorphisms `T_{p+1}(A_n) → T_{p+1}(k)` and `T_p(A_n) → T_p(k)` are surjective.*
- *e) For every `n`, the functor `N ↦ T_p(N)` is exact in the category of `A_n`-modules of finite type.*

**Proof.** One knows `(7.3.3)` that a) is equivalent to saying that `T_{p+1}` and `T_p` are right exact; since `T_•` is
a homological functor in the category `Ab_{A_n}`, the same reasoning as in `(7.3.1)` shows that e) is equivalent to
saying that `T_p` and `T_{p+1}` are right exact in the category of `A_n`-modules of finite type. One therefore deduces
from `(7.5.2)` that a) and e) are equivalent; the equivalence of a), c) and d) also results from `(7.5.2)`. Finally, one
knows that every flat `A`-module of finite type is free (Bourbaki, *Alg. comm.*, chap. II, § 3, n° 2, cor. 2 of prop.
5); the equivalence of a) and b) results then from `(7.3.1)` and `(7.3.3)`.

**Corollary (7.5.5).**

<!-- label: III.7.5.5 -->

*Suppose the general conditions of `(7.5.4)` satisfied.*

- *(i) If `T_p(k) = 0`, one has `T_p = 0`, `T_{p+1}` is right exact and `T_{p−1}` is left exact.*
- *(ii) If `T_{p−1}(k) = T_{p+1}(k) = 0`, `T_p` is exact, the canonical homomorphism*
    ```text
      T_p(A) ⊗_A M → T_p(M)
    ```
    *is bijective and `T_p(A)` is a free `A`-module.*

**Proof.** (i) follows immediately from `(7.5.3)` since `T_p` is semi-exact, the last assertion resulting from the
definition of a homological functor. One concludes immediately from (i) the first two assertions of (ii), taking
`(7.3.3)` into account; the fact that `T_p(A)` is free results from `(7.5.4)`.

**Corollary (7.5.6).**

<!-- label: III.7.5.6 -->

*Suppose the general hypotheses of `(7.5.4)` satisfied, and suppose moreover that `A` is a discrete valuation ring.*

- *(i) For `T_p` to be right exact, it is necessary and sufficient that `T_{p−1}(A)` be a free `A`-module.*
- *(ii) For `T_p` to be exact, it is necessary and sufficient that `T_{p+1}(A)` and `T_p(A)` be free `A`-modules.*

<!-- original page 192 -->

**Proof.** It is clear that (i) implies (ii) (cf. `(7.3.3)`). To prove (i), note that if `f` is a generator of the
maximal ideal of `A` ("uniformizer" of `A`), for an `A`-module of finite type `M` to be free (or flat, which amounts to
the same), it is necessary and sufficient that the homothety `h_f : x ↦ fx` of `M` be injective, since this is
equivalent here to saying that `M` is torsion-free `(0_I, 6.3.4)`. Consider then the exact sequence
`0 → A →^{h_f} A → k → 0`, which provides the exact sequence of homology

```text
  T_p(A) → T_p(k) → T_{p−1}(A) →^{h_f} T_{p−1}(A).
```

One sees that `T_{p−1}(A)` is free if and only if `T_p(A) → T_p(k)` is surjective; the conclusion then results from
`(7.5.2)`.

**Remark (7.5.7).**

<!-- label: III.7.5.7 -->

One will note that, by virtue of `(7.4.7)`, the general hypotheses of `(7.4.4)` imply that the homological functor `T_•`
defined by `(7.4.1.1)` satisfies the general hypotheses of `(7.5.4)`. In this case, `(7.5.6)` is therefore contained in
`(7.4.3)`.

## 7.6. Descent of exactness properties. Semi-continuity theorem and exactness criterion of Grauert.

**Proposition (7.6.1).**

<!-- label: III.7.6.1 -->

*Under the conditions of `(7.4.1)`, let `B` be a commutative `A`-algebra. If `T_p` is right exact (resp. left exact,
exact), the same is true of `T_p^{(B)}`; the converse is true when `B` is a faithfully flat `A`-module.*

**Proof.** The first assertion is a particular case of a trivial assertion of `(7.1.3)`. Conversely, suppose first that
`B` is a flat `A`-module. One has then, for every `A`-module `M`, `H_•(P_• ⊗_A (M ⊗_A B)) = (H_•(P_• ⊗_A M)) ⊗_A B`,
which can also be written, for every `p`,

```text
  T_p(M) ⊗_A B = T_p^{(B)}(M_{(B)})                                          (7.6.1.1)
```

up to a canonical isomorphism. Suppose `T_p^{(B)}` right exact (resp. left exact, exact); since `M ↦ M_{(B)}` is an
exact functor, the first member of `(7.6.1.1)` is a functor right exact (resp. left exact, exact) in `M`; if now `B` is
faithfully flat over `A`, one deduces that `T_p` has the same exactness property `(0_I, 6.4.1)`.

**Proposition (7.6.2).**

<!-- label: III.7.6.2 -->

*Under the conditions of `(7.4.1)`, suppose moreover that `A` is a reduced noetherian ring and that the `P_i` are
`A`-modules of finite type. For `T_p` to be right exact (resp. left exact, exact), it is necessary and sufficient that,
for every `A`-algebra `B` which is a discrete valuation ring, `T_p^{(B)}` be so.*

**Proof.** By virtue of `(7.3.1)` and `(7.3.3)`, one can restrict to considering right exactness, and there is of course
only the sufficiency of the condition to prove `(7.6.1)`. By virtue of `(7.4.2)`, it suffices to show that
`Z'_{p−1}(P_•)` is a flat `A`-module; since `P_{p−1}` is of finite type, `Z'_{p−1}(P_•)` is also of finite type; the
criterion `(0, 10.2.8)` shows that it then suffices that `Z'_{p−1}(P_•) ⊗_A B` be a flat `B`-module for every
`A`-algebra `B` which is a discrete valuation ring. Now, since `P_•` is a complex of flat `A`-modules, one has

```text
  Z'_{p−1}(P_•) ⊗_A B = Z'_{p−1}(P_• ⊗_A B);
```

<!-- original page 193 -->

`P_• ⊗_A B` is a complex of flat `B`-modules `(0_I, 6.2.1)`, and for every `B`-module `N`, one has
`H_•(P_• ⊗_A N) = H_•((P_• ⊗_A B) ⊗_B N)`, hence `T_•^{(B)}(N) = H_•((P_• ⊗_A B) ⊗_B N)`; applying `(7.4.2)` to
`T_p^{(B)}`, one sees that the hypothesis that `T_p^{(B)}` is right exact is equivalent to the fact that
`Z'_{p−1}(P_• ⊗_A B)` is a flat `B`-module.

The preceding criterion leads to studying more closely the case of discrete valuation rings:

**Proposition (7.6.3).**

<!-- label: III.7.6.3 -->

*Under the conditions of `(7.4.1)`, suppose that `A` is a noetherian regular ring of dimension 1 (in other words, `A` is
noetherian and, for every `x ∈ Spec(A)`, `A_x` is a field or a discrete valuation ring). Then, for every integer `p` and
every `A`-module `M`, one has a canonical exact sequence functorial in `M`*

```text
  0 → T_p(A) ⊗_A M →^{t_M} T_p(M) → Tor_1^A(T_{p−1}(A), M) → 0.              (7.6.3.1)
```

**Proof.** In what follows, we shall suppress for simplicity the mention of the complex `P_•` in the usual homological
notations `H_p(P_•)`, `B_p(P_•)`, `Z_p(P_•)` and `Z'_p(P_•)`. One has the three exact sequences

```text
  0 → H_p → Z'_p → B_{p−1} → 0
  0 → B_{p−1} → Z_{p−1} → H_{p−1} → 0
  0 → Z_{p−1} → P_{p−1} → B_{p−2} → 0
```

Since `P_{p−1}` and `P_{p−2}` are flat, the same is true of their respective *submodules* `B_{p−1}`, `Z_{p−1}` and
`B_{p−2}`, since there is identity between flat `A_x`-modules and torsion-free `A_x`-modules (for every `x ∈ Spec(A)`);
by tensorization with `M`, one thus has the exact sequences

```text
  0 = Tor_1^A(B_{p−1}, M) → H_p ⊗ M → Z'_p ⊗ M →^u B_{p−1} ⊗ M → 0           (7.6.3.2)
  0 → Tor_1^A(Z_{p−1}, M) → Tor_1^A(H_{p−1}, M) → B_{p−1} ⊗ M →^v Z_{p−1} ⊗ M  (7.6.3.3)
  0 = Tor_1^A(B_{p−2}, M) → Z_{p−1} ⊗ M →^w P_{p−1} ⊗ M.                     (7.6.3.4)
```

By definition, `T_p(M) = Ker(d_p ⊗ 1) / Im(d_{p+1} ⊗ 1)`; it is therefore the kernel of the homomorphism
`(P_p ⊗ M) / Im(d_{p+1} ⊗ 1) → P_{p−1} ⊗ M` obtained from `d_p ⊗ 1` by passage to the quotient, a homomorphism which is
also written `Z'_p ⊗ M → P_{p−1} ⊗ M` by definition of `Z'_p = P_p / B_p`; now, this homomorphism can be considered as
the composite

```text
  Z'_p ⊗ M →^u B_{p−1} ⊗ M →^v Z_{p−1} ⊗ M →^w P_{p−1} ⊗ M.
```

Since `w` is injective by `(7.6.3.4)`, one has an exact sequence

```text
  0 → Ker u → T_p(M) → Ker v → 0,
```

which is none other than `(7.6.3.1)`, taking `(7.6.3.2)` and `(7.6.3.3)` and the fact that `H_p = T_p(A)` by definition
into account.

**Remarks (7.6.4).**

<!-- label: III.7.6.4 -->

(i) `H_•(P_• ⊗_A M)` is the homology of the bicomplex `P_• ⊗_A M`, where `M` is considered as a complex reduced to its
term of degree `0`; it is consequently `(6.3.6 and 6.3.2)` the abutment of the regular spectral sequence whose `E_2`
term is

```text
  E_2^{p,q} = Tor_p^A(H_q(P_•), M) = Tor_p^A(T_q(A), M).
```

<!-- original page 194 -->

Now, the hypothesis on the ring `A` implies that `Tor_p^A(E, F) = 0` for `p ≥ 2` and for arbitrary `A`-modules
`(0_IV, 17.2.2)`; one knows `(M, XV)` that this implies the exactness of the sequence

```text
  0 → E_{0,q}^2 → H_q(P_• ⊗_A M) → E_{1, q−1}^2 → 0
```

which is none other than `(7.6.3.1)`.

(ii) Taking `(7.3.1)` into account, the exact sequence `(7.6.3.1)` recovers as a particular case the result of
`(7.4.3)`.

**Corollary (7.6.5).**

<!-- label: III.7.6.5 -->

*Under the conditions of `(7.4.1)`, suppose that `A` is a discrete valuation ring, with fraction field `K`, residue
field `k`, and that the `T_i(A)` are `A`-modules of finite type. One has then*

```text
  rang_k T_p(k) ≥ rang_k(T_p(A) ⊗_A k) ≥ rang_A T_p(A) = rang_K T_p(K).      (7.6.5.1)
```

*Moreover, for the extreme terms of this inequality to be equal, it is necessary and sufficient that `T_p` be exact, or
equivalently that `T_p(A)` and `T_{p−1}(A)` be free `A`-modules.*

**Proof.** Indeed, setting `M = k` in the exact sequence `(7.6.3.1)`, since one is dealing with vector spaces over `k`,

```text
  rang_k T_p(k) = rang_k(T_p(A) ⊗_A k) + rang_k(Tor_1^A(T_{p−1}(A), k)).
```

On the other hand, since `T_p(A)` is a module of finite type over the integral local ring `A`, one has (Bourbaki, *Alg.
comm.*, chap. II, § 3, n° 2, cor. 1 of prop. 4)

```text
  rang_k(T_p(A) ⊗_A k) ≥ rang_A T_p(A) = rang_K(T_p(A) ⊗_A K)                (7.6.5.2)
```

and moreover the two members of `(7.6.5.2)` are equal if and only if `T_p(A)` is a free `A`-module (*loc. cit.*, prop.
7). One will note moreover that since `K` is a flat `A`-module, one has by definition
`T_p(A) ⊗_A K = H_p(P_•) ⊗_A K = H_p(P_• ⊗_A K) = T_p(K)`. One has therefore indeed the inequality `(7.6.5.1)`, and one
sees moreover that equality is possible only if: 1° `T_p(A)` is free; 2° `Tor_1^A(T_{p−1}(A), k) = 0`, a condition which
is equivalent, as one knows `(0, 10.1.3)`, to the fact that `T_{p−1}(A)` is a free `A`-module. Finally, since the
`T_i(A)` are `A`-modules of finite type, it amounts to the same to say that they are flat or free (Bourbaki, *Alg.
comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 5), and one concludes by `(7.4.3)`.

**7.6.6.**

<!-- label: III.7.6.6 -->

The hypotheses still being those of `(7.4.1)`, we shall set, for every `x ∈ Spec(A)`,

```text
  d_p(x) = d_p^T(x) = rang_{κ(x)} T_p(κ(x)).                                 (7.6.6.1)
```

**Lemma (7.6.7).**

<!-- label: III.7.6.7 -->

*Let `φ : A → A'` be a ring homomorphism, and let*

```text
  f = ᵃφ : Spec(A') → Spec(A)
```

*be the corresponding map `(I, 1.2.1)`. If one sets `T'_• = T_•^{(A')}` `(7.1.3)`, one has*

```text
  d_p^{T'} = d_p^T ∘ f.                                                      (7.6.7.1)
```

<!-- original page 195 -->

**Proof.** Indeed, for every `x' ∈ Spec(A')`, on setting `x = f(x')`, one has

```text
  H_•(P_• ⊗_A κ(x')) = H_•((P_• ⊗_A κ(x)) ⊗_{κ(x)} κ(x')) = H_•(P_• ⊗_A κ(x)) ⊗_{κ(x)} κ(x'),
```

since `κ(x')` is flat over `κ(x)`, whence the relation `(7.6.7.1)`.

**Lemma (7.6.8).**

<!-- label: III.7.6.8 -->

*If the ring `A` is noetherian and the complex `P_•` formed of `A`-modules of finite type, the function `x ↦ d_p^T(x)`
on `Spec(A)` is constructible.*

**Proof.** It must be proved that for every irreducible closed part `Y` of `X = Spec(A)`, there exists a non-empty open
`U` of `Y` on which `d_p` is constant `(0, 9.2.2)`; since `Y = Spec(A/𝔞)`, where `𝔞` is an ideal of `A` such that `A/𝔞`
is reduced, one can, by virtue of `(7.6.7)`, restrict to the case where `Y = X` and `A` is a noetherian integral ring;
but then the assertion results from `(7.4.5)`.

**Theorem (7.6.9).**

<!-- label: III.7.6.9 -->

*Let `A` be a noetherian ring, `P_•` a complex of flat `A`-modules of finite type, `T_•(M) = H_•(P_• ⊗_A M)` the
homological functor defined by `P_•`; for every `x ∈ Spec(A)` let `d_p(x) = rang_{κ(x)} T_p(κ(x))`. Then:*

- *(i) The function `d_p` is constructible and upper semi-continuous on `Spec(A)`.*
- *(ii) If `T_p` is exact, `d_p` is continuous (hence locally constant) on `Spec(A)`; the converse is true when the ring
    `A` is reduced.*

**Proof.**

(i) The first assertion was proved in `(7.6.8)`. To prove the second, it suffices `(0, 9.2.4)` to show that if `x' ≠ x`
is a generization of `x` in `Spec(A)`, one has `d_p(x') ≤ d_p(x)`. Now, there exists then a discrete valuation ring `B`
and a morphism `f : Spec(B) → Spec(A)` such that, if `a` denotes the closed point of `Spec(B)` and `b` its generic
point, one has `f(a) = x` and `f(b) = x'` `(II, 7.1.9)`. By virtue of formula `(7.6.7.1)`, one sees that one is reduced
to proving the inequality `d_p(a) ≥ d_p(b)` in `Spec(B)`; but this is none other than the inequality `(7.6.5.1)` (¹).

(ii) The first assertion was already proved `(7.3.4)`. To prove the converse, let us use the valuative criterion
`(7.6.2)`; taking formula `(7.6.7.1)` into account, one is therefore reduced to the case where `A` is a discrete
valuation ring; but since `Spec(A)` comprises only two points, the hypothesis that `d_p` is constant indeed implies that
`T_p` is exact, by virtue of `(7.6.5)`.

> (¹) The principle of the proof of (i) by reduction to the case of a discrete valuation ring was orally communicated to
> us by Hironaka.

**Corollary (7.6.10).**

<!-- label: III.7.6.10 -->

*Let `A` be a noetherian ring, `𝔭_i` (`1 ≤ i ≤ r`) its minimal prime ideals, `k_i` the residue field of `A_{𝔭_i}`
(`1 ≤ i ≤ r`).*

- *(i) For every `x ∈ Spec(A)`, there exists an index `i` such that*
    ```text
      d_p(x) ≥ rang_{k_i} T_p(k_i).                                          (7.6.10.1)
    ```

*In particular, if `A` is integral and `K` is its fraction field, one has*

```text
  d_p(x) ≥ rang_K T_p(K)                                                     (7.6.10.2)
```

*for every `x ∈ Spec(A)`.*

<!-- original page 196 -->

- *(ii) Suppose moreover that `A` is local and reduced, and let `k` be its residue field. Then, for `T_p` to be exact,
    it is necessary and sufficient that one have*
    ```text
      rang_k T_p(k) = rang_{k_i} T_p(k_i)   for 1 ≤ i ≤ r.                   (7.6.10.3)
    ```

**Proof.** (i) is immediate since every neighbourhood of `x` contains one of the `𝔭_i`, and it suffices to apply the
definition of semi-continuity. On the other hand, if `A` is local, the only neighbourhood in `Spec(A)` of the maximal
ideal `𝔪` is `Spec(A)` in its entirety, hence one has `d_p(x) ≤ rang_k T_p(k)` for every `x ∈ Spec(A)`; this relation,
joined to (i), shows that condition `(7.6.10.3)` implies that `d_p(x)` is constant on `Spec(A)`, and consequently that
`T_p` is exact by virtue of `(7.6.9, (ii))`; the converse is obvious by virtue of `(7.6.9, (ii))`.

**Remark (7.6.11).**

<!-- label: III.7.6.11 -->

One can ask whether the assertion of `(7.6.9, (i))` cannot be strengthened by the inequality

```text
  rang_{κ(x)} T_p(κ(x)) ≥ rang_{κ(x)} (T_p(A) ⊗_A κ(x))                      (7.6.11.1)
```

for every `x ∈ Spec(A)`, which effectively holds when `A` is a discrete valuation ring and `x` its maximal ideal
`(7.6.5)`. Let us restrict to the case where `A` is a noetherian local ring with maximal ideal `𝔪` and residue field
`k`. Then, the following conditions are equivalent:

- a) For every complex `P_•` of flat `A`-modules of finite type, one has
    ```text
      rang_k(T_p(k)) ≥ rang_k(T_p(A) ⊗_A k)   for every integer p.           (7.6.11.2)
    ```
- b) For every `A`-module `M` of finite type, one has
    ```text
      rang_k(M ⊗_A k) ≥ rang_k(M̌ ⊗_A k).                                     (7.6.11.3)
    ```
- c) For every `A`-module `N` of finite type, one has
    ```text
      rang_k(Tor_1^A(N, k)) ≥ rang_k(Tor_2^A(N, k)).                         (7.6.11.4)
    ```

One will note that it amounts to the same, by shifting `(M, V, 7.2)`, to say that one has, for every `i ≥ 1`,

```text
  rang_k(Tor_i^A(N, k)) ≥ rang_k(Tor_{i+1}^A(N, k)).                         (7.6.11.5)
```

Let us give quickly some indications on the proof. To see that a) implies b), one considers an exact sequence
`L_1 →^d L_0 → M → 0` where `L_0` and `L_1` are free of finite type, and one applies a) to the complex `P_1 →^{ᵗd} P_0`
with `P_0 = Ľ_1`, `P_1 = Ľ_0`, the other terms being zero; one has then `T_1(A) = M̌` and
`T_1(k) = Hom_k(M, k) = Hom_k(M/𝔪 M, k)`, that is, `T_1(k)` is the dual of the vector space `M ⊗_A k`, and therefore has
the same rank as the latter. To prove that b) implies c), we shall first establish the following lemma:

**Lemma (7.6.11.6).**

<!-- label: III.7.6.11.6 -->

*Given a complex `… → 0 → P_1 →^d P_0 → 0 → …` of flat `A`-modules, one has an exact sequence*

```text
  0 → Tor_2^A(Z'_0, k) → T_1(A) ⊗_A k → T_1(k) → Tor_1^A(Z'_0, k) → 0.        (7.6.11.7)
```

<!-- original page 197 -->

**Proof.** Indeed, starting from the exact sequence `0 → Z_1 → P_1 → B_0 → 0`, one deduces the exact sequence
`0 → Tor_1^A(B_0, k) → Z_1 ⊗ k → P_1 ⊗ k →^u B_0 ⊗ k → 0`. From the exact sequence `0 → B_0 → Z_0 → Z'_0 → 0`, one
deduces, since `Z_0 = P_0` is flat, `Tor_1^A(B_0, k) = Tor_2^A(Z'_0, k)`; by definition, one has `Z_1 = T_1(A)`;
finally, one has `T_1(k) = Ker(d ⊗ 1)`, and `d ⊗ 1` factors as `P_1 ⊗ k →^u B_0 ⊗ k →^v Z_0 ⊗ k = P_0 ⊗ k`; one has
`T_1(k) = u^{−1}(R)`, where `R = Ker v`, and since `u` is surjective, `R = u(T_1(k))`; finally, `R = Tor_1^A(Z'_0, k)`
by definition of `v`, which finishes establishing the exact sequence `(7.6.11.7)`.

To deduce c) from b), one considers an exact sequence `L_1 →^d L_0 → N → 0`, where `L_0` and `L_1` are free modules of
finite type; consider the functor `T` associated to the complex formed of `L_1` and `L_0`; since `L_0` and `L_1` are
free, they are identified with their biduals; hence if `M = Coker(ᵗd)`, `T_1(A) = Ker(d) = M̌`; on the other hand,
`M ⊗_A k = Coker(ᵗd ⊗ 1_k)` has the same rank over `k` as `Ker(d ⊗ 1_k)`. The hypothesis b) implies consequently that

```text
  rang_k(T_1(A) ⊗_A k) ≤ rang_k(T_1(k));
```

since `Z'_0 = N`, inequality `(7.6.11.4)` results from the exact sequence `(7.6.11.7)`. Finally, to prove that c)
implies a), let us apply `(7.6.11.6)` replacing `P_0` and `P_1` by `P_p` and `P_{p−1}`; hypothesis c) applied to the
module `Z'_p` gives `rang_k R ≥ rang_k S`, where `R = Ker(P_p ⊗ k → P_{p−1} ⊗ k)` and `S = Z'_p ⊗ k`. Now, if one
factors `d_{p+1} : P_{p+1} → P_p` as `P_{p+1} →^v Z_p →^j P_p`, one has `Im(d_{p+1} ⊗ 1) = (j ⊗ 1)(Im(v ⊗ 1))`. Since

```text
  T_p(A) ⊗_A k = (Z_p / B_p) ⊗_A k = (Z_p ⊗ k) / Im(v ⊗ 1),
```

and `T_p(k) = R / Im(d_{p+1} ⊗ 1)`, one indeed concludes the inequality `(7.6.11.2)`.

This being so, suppose that the local ring `A` is regular of dimension `n`; one knows then [17] that the `A`-module
`Tor_i^A(k, k)` is isomorphic to the `i`th exterior power `∧^i(𝔪/𝔪^2)`; one sees therefore that condition `(7.6.11.4)`
is not satisfied for `N = k`, as soon as `n ≥ 4`. On the other hand, if the integral local ring `A` is such that every
reflexive `A`-module of finite type is free (which is the case when `A` is a regular ring of dimension 2), condition
`(7.6.11.3)` is satisfied: indeed, one knows that the dual `M̌` of an `A`-module of finite type `M` is reflexive, hence
free, and consequently `rang_k(M̌ ⊗_A k) = rang_K(M̌) = rang_K(M)` (`K` fraction field of `A`); on the other hand, one
knows that every basis over `k` of `M ⊗_A k` is formed of images of a system of generators of `M` (Bourbaki, *Alg.
comm.*, chap. II, § 3, n° 2, cor. 2 of prop. 4), hence `rang_K(M) ≤ rang_k(M ⊗_A k)`, which proves our assertion.

## 7.7. Application to proper morphisms: I. The exchange property.

The three subsections that follow are, essentially, translations into the language of morphisms of preschemes of the
results of the preceding subsections.

**7.7.1.**

<!-- label: III.7.7.1 -->

Let `f : X → Y` be a quasi-compact and separated morphism of preschemes, and let `𝒫_•` be a complex of quasi-coherent
`𝒪_X`-modules whose derivation operator is of degree `−1`; suppose moreover that the `𝒪_X`-modules `𝒫_i` are `Y`-flat
`(0_I, 6.7.1)`.

<!-- original page 198 -->

We are going to consider the `∂`-functor `ℳ ↦ 𝒯_•(ℳ)` (also denoted `𝒯_•(𝒫_•, ℳ)`) in the category of quasi-coherent
`𝒪_Y`-modules, with values in the category of quasi-coherent `𝒪_Y`-modules (by virtue of `(6.2.3)`), defined by

```text
  𝒯_n(𝒫_•, ℳ) = 𝒯_n(ℳ) = ℋ^{−n}(f, 𝒫^• ⊗_{𝒪_X} ℳ)   for n ∈ Z,                 (7.7.1.1)
```

where `𝒫^•` is the complex whose term of degree `j` is `P_{−j}`, the derivation operator being then of degree `+1`. The
functor `𝒯_•` thus defined is a *homological functor* in `ℳ` `(6.2.6)`.

**7.7.2.**

<!-- label: III.7.7.2 -->

Let `g : Y' → Y` be a morphism, and set `X' = X_{(Y')} = X ×_Y Y'` and `f' = f_{(Y')} : X' → Y'`, which is a
quasi-compact and separated morphism; let on the other hand `𝒫'_• = 𝒫_• ⊗_{𝒪_Y} 𝒪_{Y'}`; this is a complex of
quasi-coherent `𝒪_{X'}`-modules which are `Y'`-flat by virtue of `(I, 9.1.12)` and `(0_I, 6.2.1)`. We shall set (with
the same conventions on degrees)

```text
  𝒯'_•^{Y'}(ℳ') = ℋ^•(f', 𝒫'^• ⊗_{𝒪_{X'}} ℳ') = ℋ^•(f', 𝒫^• ⊗_{𝒪_X} ℳ')        (7.7.2.1)
```

which is a homological functor in the quasi-coherent `𝒪_{Y'}`-module `ℳ'`. When `Y'` is an affine scheme with ring `A'`,
one will write `𝒯_•^{A'}` instead of `𝒯_•^{Y'}`; for every `A'`-module `M'`, one has then
`𝒯_•^{A'}(M̃') = (Γ(Y', 𝒯_•^{Y'}(M̃')))^∼`; one will set `T_•^{A'}(M') = Γ(Y', 𝒯_•^{Y'}(M̃'))`, which is a homological
functor of `A'`-modules, with values in the category of `A'`-modules. One will observe that if `Y = Spec(A)` is also
affine, the functor of `A'`-modules `T_•^{A'}` coincides with the functor obtained by extension of scalars from `A` to
`A'` from the homological functor of `A`-modules `T_•^A` `(7.1.3)`: indeed, let `g : Y' → Y` be the morphism
corresponding to the ring homomorphism `A → A'`, and let `g' : X' → X` be the corresponding morphism, which is affine
`(II, 1.6.2)`; if `𝔘` is an affine open cover of `X`, `𝔘' = g'^{−1}(𝔘)` is an affine open cover of `X'`; by virtue of
`(6.2.2)`, it all comes down to seeing that `C^•(𝔘', 𝒫^• ⊗_{𝒪_X} g'_*(ℳ')) = C^•(𝔘', 𝒫^• ⊗_{𝒪_X} ℳ')`, and finally, that
for every affine open `U` of `X`, on setting `U' = g'^{−1}(U)`, one has
`Γ(U, 𝒫_• ⊗_{𝒪_X} g'_*(ℳ')) = Γ(U', 𝒫_• ⊗_{𝒪_X} ℳ')`, which is trivial `(I, 1.3 and 3.2)`.

In particular, if `U` is an open of `Y`, one has, for every quasi-coherent `𝒪_Y`-module `ℳ`,

```text
  𝒯_•^U(ℳ | U) = (𝒯_•(ℳ)) | U.                                                (7.7.2.2)
```

**7.7.3.**

<!-- label: III.7.7.3 -->

For every quasi-coherent `𝒪_Y`-module `ℳ`, one has a canonical homomorphism, functorial in `ℳ`:

```text
  𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ → 𝒯_p(ℳ).                                                (7.7.3.1)
```

Indeed, if `Y` is affine, this homomorphism has been defined in `(7.2.2)`; this definition extends without difficulty to
the general case, by noting that if `U`, `V` are two affine opens of `Y` such that `V ⊂ U`, the diagram

<!-- original page 199 -->

```text
  (𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ) | U = 𝒯_p^U(𝒪_Y | U) ⊗_{𝒪_Y | U} (ℳ | U) → 𝒯_p^U(ℳ | U) = (𝒯_p(ℳ)) | U
                │                                                          │
                ↓                                                          ↓
  (𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ) | V = 𝒯_p^V(𝒪_Y | V) ⊗_{𝒪_Y | V} (ℳ | V) → 𝒯_p^V(ℳ | V) = (𝒯_p(ℳ)) | V
```

is commutative by `(7.2.3.3)`.

For every morphism `g : Y' → Y` one has a canonical homomorphism

```text
  𝒯_p(𝒪_Y) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒯_p^{Y'}(𝒪_{Y'})                                  (7.7.3.2)
```

which is none other than the particular case of `(6.7.11.2)` (for the abutments) in the case where `S = Y`, `v_1 = f`,
`v_2 = 1_Y`, `𝒫'^{(2)}_•` reduced to the single term `ℳ` of degree `0`.

When `Y = Spec(A)`, `Y' = Spec(A')` are affine, `(7.7.3.2)` is none other than the homomorphism of sheaves corresponding
to the canonical homomorphism of `A'`-modules defined in `(7.2.2)`

```text
  T_p^A(A) ⊗_A A' → T_p^{A'}(A') = T_p^A(A')
```

as easily results from `(6.7.11)` (since in the case envisaged, one can take `𝔘'^{(i)} = u_i^{−1}(𝔘^{(i)})` in
`(6.7.11)`).

**7.7.4.**

<!-- label: III.7.7.4 -->

When `f` is a *proper* morphism, `Y = Spec(A)` a noetherian affine scheme and `𝒫_•` a complex of coherent and `Y`-flat
`𝒪_X`-modules bounded below, we saw `(6.10.5)` that one can write up to an isomorphism, `𝒯_•(ℳ) = ℋ_•(ℒ_• ⊗_{𝒪_Y} ℳ)`,
with `ℒ_• = L̃_•`, where `L_•` is a complex of free `A`-modules of finite type bounded below; the functor `𝒯_•` is
therefore of the type that has been studied in detail in `(7.4)` and `(7.6)`. We are going to translate the results of
this study:

**Theorem (7.7.5).**

<!-- label: III.7.7.5 -->

*Let `Y` be a locally noetherian prescheme, `(U_α)` an open affine cover of `Y`, `f : X → Y` a proper morphism, `𝒫_•` a
complex of coherent and `Y`-flat `𝒪_X`-modules bounded below. The homological functor `𝒯_•(ℳ)` defined by `(7.7.1.1)`
then has the following properties:*

- *I) (The semi-continuity property) (¹). The function*
    ```text
      y ↦ d_p(y) = rang_{κ(y)} T_p^{κ(y)}(κ(y))                              (7.7.5.1)
    ```
    *is upper semi-continuous.*

<!-- original page 200 -->

- *II) (The exchange property). For a given integer `p`, the following conditions are equivalent:*
    - *a) `𝒯_p` is right exact.*
    - *a') `𝒯_p(ℳ)` is isomorphic to a functor of the form `𝒩 ⊗_{𝒪_Y} ℳ` (`𝒩` being necessarily isomorphic to
        `𝒯_p(𝒪_Y) = ℋ^{−p}(f, 𝒫^•)`).*
    - *a'') The canonical functorial homomorphism `(7.7.3.1)` is an isomorphism.*
    - *b) `𝒯_{p−1}` is left exact.*
    - *b') There exists an `𝒪_Y`-module `𝒬` (necessarily coherent, and determined up to unique isomorphism) and an
        isomorphism of functors*
        ```text
          𝒯_{p−1}(ℳ) ⥲ ℋom_{𝒪_Y}(𝒬, ℳ).                                       (7.7.5.2)
        ```
    - *c) Denoting by `A_α` the ring of the affine open `U_α`, for every index `α` the functor of `A_α`-modules
        `T_p^{A_α}` is right exact.*
    - *d) For every morphism `g : Y' → Y`, the canonical homomorphism*
        ```text
          𝒯_p(𝒪_Y) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒯_p^{Y'}(𝒪_{Y'})                          (7.7.5.3)
        ```
        *is an isomorphism.*

> (¹) A particular case of this theorem is already found in note [3] of Chow–Igusa. The semi-continuity property has
> been discovered, in the context of analytic spaces (and under fairly particular hypotheses), by Kodaira–Spencer (*On
> the variations of almost-complex structures*, *Algebraic Geometry and Topology, A Symposium in honor of S. Lefschetz*,
> Princeton Series n° 12, p. 139–150, Princeton, 1957) and the general version proved by Grauert [5].

**Proof.** The semi-continuity property is local on `Y` and therefore results from remark `(7.7.4)` and from `(7.6.9)`.
It is clear that a'') implies a') and that a') implies a). The equivalence of a), a''), b) and b') has been proved in
`(7.3.1)` and `(7.4.6)`, taking remark `(7.7.4)` into account, when `Y` is affine. To pass to the general case, let us
first prove that a) is equivalent to c), which will prove the *local* character on `Y` of property a); the proof will
likewise serve to prove the local character of a'') and b). Since it is clear that c) implies a), it all comes down to
proving the converse. It evidently suffices to show that for every affine open `U` of `Y` and every exact sequence
`0 → 𝒢' → 𝒢 → 𝒢'' → 0` of quasi-coherent `(𝒪_Y | U)`-modules, there exists an exact sequence `0 → ℱ' → ℱ → ℱ'' → 0` of
quasi-coherent `𝒪_Y`-modules such that `𝒢' = ℱ' | U`, `𝒢 = ℱ | U`, `𝒢'' = ℱ'' | U`; now, this results at once from the
hypothesis that `Y` is locally noetherian, and from `(I, 9.4.2)`: one extends in fact `𝒢` to a quasi-coherent
`𝒪_Y`-module `ℱ`, `𝒢'` to a sub-`𝒪_X`-module `ℱ'` of `ℱ`, and it suffices to take `ℱ'' = ℱ / ℱ'`.

To prove the equivalence of b) and b') in the general case, note that when `Y` is affine, one knows that `𝒬` is
determined up to unique isomorphism; if then `U` is an affine open of the affine scheme `Y`, one concludes that there
exists a functorial isomorphism `𝒯_{p−1}(ℳ | U) ⥲ ℋom_{𝒪_Y | U}(𝒬 | U, ℳ | U)`. In the general case, for every affine
open `U` of `Y`, there is a coherent `(𝒪_Y | U)`-module `𝒬_U` and a functorial isomorphism
`𝒯_{p−1}^U(ℳ | U) → ℋom_{𝒪_Y | U}(𝒬_U, ℳ | U)`; the preceding remark shows that if `V` is an affine open contained in
`U`, one has `𝒬_U | V = 𝒬_V`; whence the existence and uniqueness of the `𝒪_Y`-module `𝒬` satisfying `(7.7.5.2)`.

It remains to show the equivalence of a) and d); it is clear that d) is of local character on `Y`, and one has seen
above that the same is true of a); moreover, d) is also local on `Y'`. Now, when `Y = Spec(A)`, `Y' = Spec(A')`, one has
seen that `T_p^{A'}` is the functor obtained

<!-- original page 201 -->

from `T_p^A` by extension of scalars to `A'`, and it is then clear that a') implies that `(7.7.5.3)` is an isomorphism.
Conversely, suppose still `Y = Spec(A)` affine and let `A'` be the `A`-algebra `A ⊕ M`, where `M` is an arbitrary
`A`-module, the multiplication in `A'` being given by `(a_1, m_1)(a_2, m_2) = (a_1 a_2, a_1 m_2 + a_2 m_1)`; then

```text
  T_p^{A'}(A') = T_p(A ⊕ M) = T_p(A) ⊕ T_p(M),
```

and the hypothesis that `(7.7.5.3)` is bijective implies that the canonical map `T_p(A) ⊗_A M → T_p(M)` is bijective, in
other words d) implies a''), which completes the proof.

**Theorem (7.7.6).**

<!-- label: III.7.7.6 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `ℱ` a coherent and `Y`-flat `𝒪_X`-module.
There exists then a coherent `𝒪_Y`-module `𝒬` (determined up to unique isomorphism) and an isomorphism of functors in
the quasi-coherent `𝒪_Y`-module `ℳ`:*

```text
  f_*(ℱ ⊗_{𝒪_Y} ℳ) ⥲ ℋom_{𝒪_Y}(𝒬, ℳ)                                        (7.7.6.1)
```

*(whence an isomorphism of functors*

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬, ℳ).)                                     (7.7.6.2)
```

**Proof.** Indeed, since `ℳ ↦ ℱ ⊗_{𝒪_Y} ℳ` is exact `(0_I, 6.7.4)` and `f_*` is left exact, the functor
`ℳ ↦ f_*(ℱ ⊗_{𝒪_Y} ℳ)` is left exact. It then suffices to apply the equivalence of `(7.7.5, b))` and `(7.7.5, b'))` for
`p = 1`.

**Corollary (7.7.7).**

<!-- label: III.7.7.7 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `ℱ`, `ℱ'` two coherent and `Y`-flat
`𝒪_X`-modules, `u : ℱ → ℱ'` a homomorphism. Consider the two functors in the quasi-coherent `𝒪_Y`-module `ℳ`:*

```text
  𝒯(ℳ) = Ker(f_*(ℱ ⊗_{𝒪_Y} ℳ) → f_*(ℱ' ⊗_{𝒪_Y} ℳ))
  T(ℳ) = Γ(Y, 𝒯(ℳ)) = Ker(Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ)).
```

*Then there exists a coherent `𝒪_Y`-module `ℛ` (determined up to unique isomorphism) and isomorphisms of functors*

```text
  𝒯(ℳ) ⥲ ℋom_{𝒪_Y}(ℛ, ℳ)                                                    (7.7.7.1)
  T(ℳ) ⥲ Hom_{𝒪_Y}(ℛ, ℳ).                                                   (7.7.7.2)
```

**Proof.** One can restrict to proving `(7.7.7.2)`; this will prove `(7.7.7.1)` in the case where `Y` is affine, and one
will pass from there to the general case by reasoning as in the proof of the equivalence of `(7.7.5, b)` and `b')`,
thanks to the uniqueness up to unique isomorphism of a representative of a representable functor `(0, 8.1.8)`. It
follows from `(7.7.6)` that there exist two coherent `𝒪_Y`-modules `𝒬`, `𝒬'` defining functorial isomorphisms

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬, ℳ),   Γ(X, ℱ' ⊗_{𝒪_Y} ℳ) ⥲ Hom_{𝒪_Y}(𝒬', ℳ).
```

Now, `u : ℱ → ℱ'` defines canonically a morphism of functors

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ);
```

<!-- original page 202 -->

to this corresponds a unique homomorphism `v : 𝒬' → 𝒬` of `𝒪_Y`-modules such that the diagram

```text
  Γ(X, ℱ ⊗_{𝒪_Y} ℳ) → Γ(X, ℱ' ⊗_{𝒪_Y} ℳ)
        │                    │
        ↓                    ↓
  Hom_{𝒪_Y}(𝒬, ℳ)   → Hom_{𝒪_Y}(𝒬', ℳ)
```

be commutative `(0, 8.1.4)`. Since the contravariant functor `𝒩 ↝ Hom_{𝒪_Y}(𝒩, ℳ)` is left exact in the category of
`𝒪_Y`-modules, it suffices to take `ℛ = Coker(v)` to obtain the isomorphism `(7.7.7.2)` sought.

**Corollary (7.7.8).**

<!-- label: III.7.7.8 -->

*Under the hypotheses of `(7.7.6)` relative to `X`, `Y` and `f`, let `ℱ`, `𝒢` be two coherent `𝒪_X`-modules satisfying
the following conditions: (i) `ℱ` is `Y`-flat; (ii) `𝒢` is isomorphic to the cokernel of a homomorphism of locally free
`𝒪_X`-modules of finite type `ℰ_1 → ℰ_0`. Consider the two functors in the quasi-coherent `𝒪_Y`-module `ℳ`:*

```text
  𝒯(ℳ) = f_*(ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ))
  T(ℳ) = Γ(Y, 𝒯(ℳ)) = Hom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ).
```

*Then there exists a coherent `𝒪_Y`-module `𝒩` (determined up to unique isomorphism) and isomorphisms of functors*

```text
  𝒯(ℳ) ⥲ ℋom_{𝒪_Y}(𝒩, ℳ)                                                    (7.7.8.1)
  T(ℳ) ⥲ Hom_{𝒪_Y}(𝒩, ℳ).                                                   (7.7.8.2)
```

**Proof.** By virtue of the functorial isomorphism `(0_I, 5.4.2.1)`, one has functorial isomorphisms in `ℰ`

```text
  ℋom_{𝒪_X}(ℰ_i, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Ě_i ⊗_{𝒪_X} (ℱ ⊗_{𝒪_Y} ℳ) ⥲ (Ě_i ⊗_{𝒪_X} ℱ) ⊗_{𝒪_Y} ℳ ⥲ ℋom_{𝒪_X}(ℰ_i, ℱ) ⊗_{𝒪_Y} ℳ
```

for `i = 0, 1`. Set `ℱ_i = ℋom_{𝒪_X}(ℰ_i, ℱ)` for `i = 0, 1`; these are coherent `𝒪_X`-modules `(0_I, 5.3.5)` and
`Y`-flat `(0_I, 5.4.2)`; let `u = ℋom(v, 1_ℱ) : ℱ_0 → ℱ_1`. By virtue of the left exactness of the functor
`ℋ ↝ ℋom_{𝒪_X}(ℋ, ℱ ⊗_{𝒪_Y} ℳ)`, one has functorial isomorphisms in `ℳ`

```text
  ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ) ⥲ Ker(ℋom_{𝒪_X}(ℰ_0, ℱ ⊗_{𝒪_Y} ℳ) → ℋom_{𝒪_X}(ℰ_1, ℱ ⊗_{𝒪_Y} ℳ)) ⥲
                                                                          Ker(ℱ_0 ⊗_{𝒪_Y} ℳ → ℱ_1 ⊗_{𝒪_Y} ℳ).
```

Since `f_*` is left exact, one deduces a functorial isomorphism

```text
  f_*(ℋom_{𝒪_X}(𝒢, ℱ ⊗_{𝒪_Y} ℳ)) ⥲ Ker(f_*(ℱ_0 ⊗_{𝒪_Y} ℳ) → f_*(ℱ_1 ⊗_{𝒪_Y} ℳ))
```

and it then suffices to apply `(7.7.7)`.

<!-- original page 203 -->

**Remarks (7.7.9).**

<!-- label: III.7.7.9 -->

(i) In `(7.7.6)`, `(7.7.7)`, `(7.7.8)`, *the formation of the `𝒪_Y`-modules `𝒬`, `ℛ`, `𝒩` commutes with base change*.
For example (keeping the notations of `(7.7.2)`), in the case `(7.7.6)`, one has, for every quasi-coherent
`𝒪_{Y'}`-module `ℳ'`, the isomorphism

```text
  f'_*(ℱ' ⊗_{𝒪_{Y'}} ℳ') ⥲ ℋom_{𝒪_{Y'}}(g^*(𝒬), ℳ')
```

for, by virtue of the remark made in `(7.7.2)`, everything comes down to seeing that one has

```text
  Hom_{𝒪_Y}(𝒬, g_*(ℳ')) = Hom_{𝒪_{Y'}}(g^*(𝒬), ℳ')
```

which is none other than `(0_I, 4.4.3.1)`. Similarly, when in `(7.7.7)` one replaces `Y, f, ℳ, ℱ, ℱ'` by
`Y', f', ℳ', ℱ ⊗_{𝒪_X} 𝒪_{X'}, ℱ' ⊗_{𝒪_X} 𝒪_{X'}`, one must replace `ℛ` by `g^*(ℛ)`. Finally, in `(7.7.8)`, when one
replaces `X, Y, f, ℳ, ℱ` by `X', Y', f', ℳ', ℱ ⊗_{𝒪_X} 𝒪_{X'}`, and `𝒢` by `𝒢' = 𝒢 ⊗_{𝒪_X} 𝒪_{X'}`, one must replace `𝒩`
by `g^*(𝒩)`: this follows from the fact that one has again an exact sequence `ℰ'_1 → ℰ'_0 → 𝒢' → 0` with
`ℰ'_i = ℰ_i ⊗_{𝒪_X} 𝒪_{X'}`, and from the fact that `Ě'_i ⊗_{𝒪_{X'}} (ℱ ⊗_{𝒪_Y} ℳ') = Ě_i ⊗_{𝒪_X} (ℱ ⊗_{𝒪_Y} ℳ')`
(`i = 0, 1`).

(ii) Condition (ii) of the statement of `(7.7.8)` relative to `𝒢` is always satisfied for an arbitrary coherent
`𝒪_X`-module `𝒢` when there exists an invertible `Y`-ample `𝒪_X`-module, for example when `Y` is affine and `f : X → Y`
is a projective morphism. It then suffices to note (taking `(II, 5.5.1)` into account) that there exists a locally free
`𝒪_X`-module of finite type `ℰ_0` such that `𝒢` is isomorphic to a quotient of `ℰ_0` `(II, 2.7.10)`; since `ℰ_0` and `𝒢`
are coherent, the same is true of the kernel `ℰ_1` of `ℰ_0 → 𝒢`, and applying the same result to `ℰ_1`, one indeed
obtains an exact sequence `ℰ_1 → ℰ_0 → 𝒢 → 0` where `ℰ_0` and `ℰ_1` are locally free of finite type.

(iii) We shall prove in chap. V that, in `(7.7.8)`, the restrictive hypothesis (ii) is superfluous.

**Proposition (7.7.10) (local criteria for the exchange property).**

<!-- label: III.7.7.10 -->

*Under the general conditions of `(7.7.5)`, let `y` be a point of `Y`, `p` an integer. The following properties are
equivalent:*

- *a) The functor `T_p^{𝒪_y}` is right exact.*
- *b) The canonical homomorphism `T_p^{𝒪_y}(𝒪_y) → T_p^{𝒪_y}(κ(y))` is surjective.*
- *c) For every integer `n`, the canonical homomorphism `T_p^{𝒪_y}(𝒪_y / 𝔪_y^{n+1}) → T_p^{𝒪_y}(κ(y))` is surjective.*

*Moreover, the set of `y ∈ Y` satisfying these conditions is the largest open `U` of `Y` such that `𝒯_p^U` is right
exact.*

**Proof.** Taking `(7.7.4)` into account, the equivalence of a), b) and c) results from `(7.4.7)` and `(7.5.2)`. The
fact that the set `U` where `T_p^{𝒪_y}` is right exact is open is also a consequence of `(7.4.4)`, and conversely if
`𝒯_p^U` is right exact, the same is true of `T_p^{𝒪_y}` for every `y ∈ V`, by condition c) of `(7.7.5)` and `(7.6.1)`.

**Corollary (7.7.11).**

<!-- label: III.7.7.11 -->

*If `𝒯_p` is right exact (resp. left exact), then, for every morphism `g : Y' → Y`, `𝒯_p^{Y'}` is right exact (resp.
left exact). The converse is true when the morphism `g` is faithfully flat.*

<!-- original page 204 -->

**Proof.** The first assertion is an immediate consequence of `(7.6.1)` and the fact that the question is local on `Y`
and `Y'`, by `(7.7.5, c) and b))`. To prove the second assertion, it suffices to see that for every `y ∈ Y`, `T_p^{𝒪_y}`
is right exact (resp. left exact), by virtue of `(7.7.10)`. But by hypothesis, there exists `y' ∈ Y'` such that
`g(y') = y`, and `𝒪_{y'}` is a faithfully flat `𝒪_y`-module; the conclusion then results from the hypothesis and from
`(7.6.1)`.

**Remarks (7.7.12).**

<!-- label: III.7.7.12 -->

(i) Under the hypotheses of `(7.7.4)`, suppose moreover that `𝒫_•` is a *finite* complex; then it results from `(7.7.1)`
(since one can take for `𝔘` a finite affine open cover of `X`) that the bicomplex `C^•(𝔘, 𝒫^• ⊗_{𝒪_X} ℳ)` is also
finite, and more precisely that there exists a finite set `E` of pairs, independent of `ℳ`, such that
`C^h(𝔘, 𝒫^k ⊗_{𝒪_X} ℳ) = 0` for all pairs `(h, k) ∉ E`. One concludes that there exists `i_1` such that, for `i ≥ i_1`,
one has `𝒯_i(ℳ) = 0` for every quasi-coherent `𝒪_Y`-module `ℳ`. In particular, `𝒯_i` is trivially an exact functor in
`ℳ` for these values of `i`, and consequently `(7.4.1)`, `Z'_{i_1}(L_•)` is a flat `A`-module of finite type (hence
projective of finite type, since `A` is noetherian) for these values of `i`. Consider then the complex `(L'_i)` of
`A`-modules such that `L'_i = L_i` for `i < i_1`, `L'_{i_1} = Z'_{i_1}(L_•)` and `L'_i = 0` for `i > i_1` and let
`ℒ'_• = L̃'_•`. It is clear that `ℋ_i(ℒ'_• ⊗_{𝒪_Y} ℳ) = ℋ_i(ℒ_• ⊗_{𝒪_Y} ℳ)` for `i < i_1 − 1` and also for `i ≥ i_1`
(the two members being then zero); finally, since `Im(Z'_{i_1} ⊗_A M) = Im(L_{i_1} ⊗_A M)` by definition, one also has
`ℋ_i(ℒ'_• ⊗_{𝒪_Y} ℳ) = ℋ_i(ℒ_• ⊗_{𝒪_Y} ℳ)` for `i = i_1 − 1`. One thus sees that one can suppose in `(7.7.4)` that `ℒ_•`
is also a *finite* complex, on condition of requiring only that the `ℒ_i` be locally free `𝒪_Y`-modules (associated with
projective `A`-modules of finite type).

This reasoning applies in particular to the case where `𝒫_•` is reduced to a single term `ℱ ≠ 0`, of degree `0` (in
which case `𝒯_n(ℰ) = R^{−n} f_*(ℱ ⊗_{𝒪_Y} ℰ)`); one can then suppose that the `ℒ_i` are zero for `i > 0`; one will use
preferentially in this case the cohomological notations, thus writing `𝒯^{−p}` instead of `𝒯_p`.

(ii) When in the statement of `(7.7.5)` one no longer supposes that the `𝒫_i` are `Y`-flat, the conclusions remain valid
on condition that one sets this time

```text
  𝒯_p(ℰ) = 𝒯or_n^Y(f, 1_Y; 𝒫_•, ℰ).                                          (7.7.12.1)
```

Indeed, `𝒯or_n^Y(f, 1_Y; 𝒫_•, 𝒪_Y)` is then a coherent `𝒪_Y`-module by virtue of `(6.7.9)`. The proof of `(6.10.5)`
applies without change, taking `(6.10.1)` into account, and shows again that when `Y = Spec(A)` is affine, one has
`𝒯_p(ℰ) = ℋ_p(ℒ_• ⊗_{𝒪_Y} ℰ)`, with `ℒ_• = L̃_•`, where `L_•` is a complex of free `A`-modules of finite type; this
proves our assertion.

## 7.8. Application to proper morphisms: II. Cohomological flatness criteria.

**Definition (7.8.1).**

<!-- label: III.7.8.1 -->

*Let `X`, `Y` be two preschemes, `f : X → Y` a quasi-compact and separated morphism, `𝒫_•` a complex of quasi-coherent
and `Y`-flat `𝒪_X`-modules, `𝒯_•` the homological functor of quasi-coherent*

<!-- original page 205 -->

*`𝒪_Y`-modules defined by `(7.7.1.1)`, `y` a point of `Y`. One says that `𝒫_•` is* homologically flat over `Y` at the
point `y`, in dimension `p` *(or* cohomologically flat over `Y` at the point `y`, in dimension `−p`*) if there exists an
open neighbourhood `U` of `y` in `Y` such that `𝒯_p^U = 𝒯^{−p}_U` is exact. One says that `𝒫_•` is* homologically flat
in dimension `p` over `Y` *(or* cohomologically flat in dimension `−p` over `Y`*) if it is homologically flat over `Y`
at every point `y ∈ Y`, in dimension `p`.*

*When `𝒫_•` is homologically flat over `Y` (resp. over `Y` at the point `y`) for every dimension `p`, one says simply
that `𝒫_•` is* homologically flat over `Y` *(resp. over `Y` at the point `y`) or* cohomologically flat over `Y` *(resp.
over `Y` at the point `y`).*

**7.8.2.**

<!-- label: III.7.8.2 -->

By definition, the notion of homological flatness over `Y` is *local* on `Y`. If `Y` is locally noetherian, or a scheme,
for `𝒫_•` to be homologically flat over `Y` in dimension `p`, it is necessary and sufficient that the functor `𝒯_p` be
exact: the proof has been done in the case where `Y` is locally noetherian in the course of the proof of `(7.7.5)`; the
reasoning is the same (based on `(I, 9.4.2)` applied to an affine open in a quasi-compact scheme) when `Y` is a scheme.

**Proposition (7.8.3).**

<!-- label: III.7.8.3 -->

*The notations and hypotheses being those of `(7.8.1)`, the following conditions are equivalent:*

- *a) `𝒫_•` is homologically flat over `Y` at the point `y` in dimension `p`.*
- *b) There exists an open neighbourhood `U` of `y` in `Y` such that `𝒯_p^U` and `𝒯_{p+1}^U` are right exact.*
- *c) There exists an open neighbourhood `U` of `y` in `Y` such that `𝒯_p^U` and `𝒯_{p−1}^U` are left exact.*
- *d) There exists an open neighbourhood `U` of `y` in `Y` such that `𝒯_{p+1}^U` is right exact and `𝒯_{p−1}^U` is left
    exact.*

**Proof.** Taking the interpretation of `𝒯_p` when `Y` is affine into account, this is but a translation of part of
`(7.3.3)`.

**Proposition (7.8.4).**

<!-- label: III.7.8.4 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `𝒫_•` a complex of coherent and `Y`-flat
`𝒪_X`-modules bounded below, `𝒯_•` the functor defined by `(7.7.1.1)`. For every `y ∈ Y`, the following conditions are
equivalent:*

- *a) `𝒫_•` is homologically flat over `Y` at `y` in dimension `p`.*
- *b) The functor `T_p^{𝒪_y}` is exact.*
- *c) There exists an integer `n_0` such that for `n ≥ n_0`, one has*
    ```text
      long T_p^{𝒪_y}(𝒪_y / 𝔪_y^{n+1}) = long T_p^{𝒪_y}(κ(y)) · long 𝒪_y / 𝔪_y^{n+1}     (7.8.4.1)
    ```
    *(where one is dealing with lengths of `𝒪_y`-modules).*
- *d) There is an open neighbourhood `U` of `y` such that `(ℋ^{−p}(f, 𝒫^•)) | U` is isomorphic to a `(𝒪_Y | U)`-module
    of the form `(𝒪_Y | U)^m` and such that, for every quasi-coherent `(𝒪_Y | U)`-module `ℳ`, the canonical
    homomorphism*
    ```text
      ((ℋ^{−p}(f, 𝒫^•)) | U) ⊗_{𝒪_Y | U} ℳ → ℋ^{−p}(f, (𝒫^• | U) ⊗_{𝒪_Y | U} ℳ)         (7.8.4.2)
    ```
    *is bijective.*

*When these conditions are satisfied, one has moreover the following property:*

- *e) There exists a neighbourhood of `y` in which the function `z ↦ d_p(z)` (defined in `(7.7.5.1)`) is constant.*

*Moreover, if `Y` is reduced at the point `y` `(0_I, 4.1.4)`, e) is equivalent to the other conditions.*

<!-- original page 206 -->

**Proof.** Indeed, condition b) is equivalent to saying that `T_p^{𝒪_y}` and `T_{p+1}^{𝒪_y}` are right exact `(7.3.3)`.
The equivalence of a) and b) results then from `(7.7.10)` and `(7.8.3)`. Since `𝒪_y / 𝔪_y^{n+1}` is artinian, and
`T_p^{𝒪_y}(𝒪_y / 𝔪_y^{n+1})` and `T_p^{𝒪_y}(κ(y))` are `(𝒪_y / 𝔪_y^{n+1})`-modules of finite type `(7.7.4)`, hence of
finite length, the equivalence of b) and c) again results from `(7.7.10)` and from `(7.3.5.7)`. The fact that a) implies
e), and is equivalent to it when `𝒪_y` is reduced, is a consequence of `(7.6.9)`. Finally, a) implies that `(7.8.4.2)`
is bijective by virtue of definition `(7.8.1)` and of `(7.7.5)`; on the other hand, a) implies that `(ℋ^{−p}(f, 𝒫^•))_y`
is a flat `𝒪_y`-module `(7.3.3, f)`, hence free `(0, 10.1.3)`, since it is an `𝒪_y`-module of finite type by virtue of
`(7.7.4)`; since `ℋ^{−p}(f, 𝒫^•)` is a coherent `𝒪_Y`-module `(7.7.4)`, it is locally free in a neighbourhood of `y`
`(0_I, 5.2.7)`. Conversely, it is clear that d) implies a) by definition of the functor `𝒯_p^U` `(7.7.2.2)`.

**Proposition (7.8.5).**

<!-- label: III.7.8.5 -->

*Under the hypotheses of `(7.8.4)`, the following conditions are equivalent:*

- *a) `𝒫_•` is homologically flat over `Y` in every dimension `i ≤ p`.*
- *b) For `i ≤ p + 1` the functors `𝒯_i` are right exact.*
- *c) For `i ≥ −p`, the `𝒪_Y`-modules `ℋ^i(f, 𝒫^•)` are locally free.*

**Proof.** The equivalence of a) and b) is trivial `(7.8.3)` and a) implies c) by virtue of `(7.8.4)`. Conversely,
suppose c) verified, note on the other hand that one has `ℒ_i = 0` for `i ≤ i_0` `(7.7.4)`, hence also `𝒯_i = 0` for
`i ≤ i_0`. Every point `y ∈ Y` has therefore an affine neighbourhood `U = Spec(A)` such that `T_i^A(A)` is a free
`A`-module for `i ≤ p`; by virtue of `(7.3.7)`, one concludes that `𝒯_i^U = T_i^A` is exact for `i ≤ p`.

We shall mainly apply the cohomological flatness criteria to the case where the complex `𝒫_•` is reduced to a single
coherent `𝒪_X`-module `ℱ` flat over `Y`, taken equal to `𝒫_0`; recall that one has then
`𝒯_n(ℳ) = R^{−n} f_*(ℱ ⊗_{𝒪_Y} ℳ)`.

**Proposition (7.8.6).**

<!-- label: III.7.8.6 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper and flat morphism, `y` a point of `Y`; denote by `X_y`
the fibre `f^{−1}(y) = X ⊗_Y κ(y)`. Suppose that `Γ(X_y, 𝒪_{X_y}) = R` is a separable `κ(y)`-algebra (Bourbaki, *Alg.*,
chap. VIII, § 7, n° 5), that is, composed of a finite number of separable extensions of finite degree of `κ(y)`. Then
`𝒪_X` is cohomologically flat over `Y` at the point `y` in dimension `0`.*

**Proof.** By virtue of `(7.8.4)`, one can restrict to the case where `Y` is the spectrum of the local ring `A = 𝒪_y`;
the hypothesis that `f` is flat implies `𝒯_{−1} = 0`, hence one already sees that `T_0^A` is left exact and it all comes
down to seeing that it is right exact; by virtue of `(7.7.10, c))`, one is even reduced to the case where `A = 𝒪_y` is
artinian. Let `k'` be a finite extension of `κ(y)` which is a splitting field of `R`, so that `R ⊗_{κ(y)} k'` is the
direct sum of a finite number of fields isomorphic to `k'`. We know that there exists a local homomorphism of `A` into a
local ring `A'`, making `A'` a finite free `A`-algebra, and such that the residue field of `A'` is isomorphic to `k'`
`(0, 10.3.2)`. By virtue of `(7.6.1)`, one is reduced to proving that `T_0^{A'}` is right exact, in other words one can
suppose that `R` is the direct sum of `m` fields isomorphic to `κ(y)`. Let us now note the following elementary lemma:

**Lemma (7.8.6.1).**

<!-- label: III.7.8.6.1 -->

*Let `Z` be a space ringed in local rings; for `Z` to be connected, it is necessary*

<!-- original page 207 -->

*and sufficient that the ring `Γ(Z, 𝒪_Z)` not be a product of two rings not reduced to `0`.*

**Proof.** It is clear in fact that if `Z` is the union of two non-empty disjoint opens, `Γ(Z, 𝒪_Z)` is isomorphic to
the product of the two rings `Γ(Z_1, 𝒪_Z)` and `Γ(Z_2, 𝒪_Z)` not reduced to `0`. Conversely, to say that `Γ(Z, 𝒪_Z)` is
such a product amounts to saying that there is in `Γ(Z, 𝒪_Z)` an idempotent `s` distinct from `0` and `1`; for every
`z ∈ Z`, `s_z` is then an idempotent in `𝒪_z`, hence equal to `0` or `1`. But it is clear that the set of `z` such that
`s_z = 0` is open; on the other hand, if `s_z = 1`, one has by definition `s(z) ≠ 0`, hence the set of `z` where
`s_z = 1` is also open `(0_I, 5.5.2)`; whence the conclusion.

It results from this lemma that `X_y` has exactly `m` connected components `X'_i` and that `Γ(X'_i, 𝒪_{X'_i}) = κ(y)`
for every `i`. Since `A` was supposed local and artinian, its spectrum is reduced to a point, hence `X` and `X_y` have
the same underlying space; `X` therefore has `m` connected components `X_i` such that `X'_i = X_i ⊗_Y κ(y)`. One is thus
finally reduced to the case where `R = κ(y)`; by virtue of `(7.7.10, b))`, one is reduced to proving that the canonical
homomorphism `Γ(X, 𝒪_X) → Γ(X_y, 𝒪_{X_y})` is surjective; but this is trivial, since the composite

```text
  Γ(Y, 𝒪_Y) = A → Γ(X, 𝒪_X) → Γ(X_y, 𝒪_{X_y}) = κ(y)
```

is already surjective.

**Corollary (7.8.7).**

<!-- label: III.7.8.7 -->

*Under the hypotheses of `(7.8.6)`, there exists an open neighbourhood `U` of `y` such that:*

- *(i) `f_*(𝒪_X) | U` is isomorphic to a `(𝒪_Y | U)`-module of the form `(𝒪_Y | U)^m`.*
- *(ii) For every `z ∈ U`, the canonical homomorphism*
    ```text
      (f_*(𝒪_X))_z ⊗_{𝒪_z} κ(z) → Γ(X_z, 𝒪_{X_z})
    ```
    *is bijective.*

**Proof.**

(i) follows from `(7.8.6)` and `(7.8.4)`.

(ii) follows from the fact that `𝒯_0^U` is exact (for `U` suitably chosen), and from `(7.7.5.3)`.

**Corollary (7.8.8).**

<!-- label: III.7.8.8 -->

*Suppose the conditions of `(7.8.6)` satisfied and moreover that `Γ(X_y, 𝒪_{X_y}) = κ(y)`. Then there exists an open
neighbourhood `U` of `y` such that the canonical homomorphism `𝒪_Y | U → f_*(𝒪_X) | U` is bijective.*

**Proof.** Indeed, it follows from `(7.8.7, (ii))` that the integer `m` appearing in `(7.8.7, (i))` is necessarily equal
to `1`.

**Corollary (7.8.9).**

<!-- label: III.7.8.9 -->

*Under the hypotheses of `(7.8.6)`, there exists an open neighbourhood `U` of `y`, a coherent `𝒪_U`-module `𝒬`
(determined up to unique isomorphism) and an isomorphism of functors in the quasi-coherent `𝒪_U`-module `ℳ`:*

```text
  R^1 f_*(f^*(ℳ)) ⥲ ℋom_{𝒪_U}(𝒬, ℳ).                                         (7.8.9.1)
```

**Proof.** Indeed, the hypothesis implies that `𝒯_0^U` is exact for a suitable `U`; it therefore suffices to apply the
equivalence of `(7.7.5, a))` and `(7.7.5, b'))` in the case `p = 0` and taking for `𝒫_•` the complex reduced to its term
of degree `0` equal to `𝒪_X`.

**Remarks (7.8.10).**

<!-- label: III.7.8.10 -->

(i) Under the conditions of `(7.8.6)`, consider the Stein factorization of `f` `(4.3.3)`

```text
  X →^{f'} Y' →^g Y
```

<!-- original page 208 -->

with `Y' = Spec(f_*(𝒪_X))`; the finite morphism `g` is then such that `g_*(𝒪_{Y'}) = f_*(𝒪_X)` is locally free in a
neighbourhood of `y`, and its fibre at `y` is the spectrum of a separable algebra over `κ(y)` `(II, 1.5.1)`. We shall
deduce in chap. IV that there is an open neighbourhood `U` of `y` in `Y` such that for the restriction `g^{−1}(U) → U`
of `g`, every fibre `g^{−1}(z)` (where `z ∈ U`) is the spectrum of a separable algebra over `κ(z)` (this is what we
shall call an *étale cover* of `U`); it will then result from `(7.8.7, (ii))` that the hypothesis made on the point `y`
in `(7.8.6)` is satisfied also at every point of a neighbourhood of `y`.

(ii) We shall see in chap. V that, even if `X` is projective over `Y` (and even if it is moreover "smooth" over `Y`, a
property which will be defined in chap. IV), the `𝒪_Y`-module `𝒬` of `(7.8.9)` is not necessarily locally free; in other
words, `𝒪_X` (under these conditions) is not necessarily cohomologically flat in dimension 1 over `Y` at the point `y`.
In chap. V, we shall interpret `𝒬` as the sheaf of 1-differentials of the Picard scheme of `X` with respect to `Y` along
the unit section.

## 7.9. Application to proper morphisms: III. Invariance of the Euler–Poincaré characteristic and the Hilbert polynomial.

**7.9.1.**

<!-- label: III.7.9.1 -->

Let `A` be a ring, `M` a projective `A`-module of finite type; recall (Bourbaki, *Alg. comm.*, chap. II, § 5, n° 2) that
it amounts to the same to say that the `𝒪_X`-module `M̃` associated on `X = Spec(A)` is locally free of finite type. For
every `𝔭 ∈ Spec(A)` one calls *rank of `M` at* `𝔭` and one denotes by `rang_𝔭(M)` the rank of the free `A_𝔭`-module
`M_𝔭` (or equivalently the rank at `𝔭` of the locally free `𝒪_X`-module `M̃`). One has therefore

```text
  rang_𝔭 M = rang_{A_𝔭}(M_𝔭) = rang_{κ(𝔭)}(M ⊗_A κ(𝔭)).                       (7.9.1.1)
```

**Proposition (7.9.2).**

<!-- label: III.7.9.2 -->

*Let `P_•` be a finite complex of projective `A`-modules of finite type, and for every `A`-module `M`, let
`T_•(M) = H_•(P_• ⊗_A M)`. Then, for every `𝔭 ∈ Spec(A)`, one has*

```text
  Σ_i (−1)^i rang_{κ(𝔭)} T_i(κ(𝔭)) = Σ_i (−1)^i rang_𝔭(P_i).                 (7.9.2.1)
```

**Proof.** Indeed, one has by definition `T_i(κ(𝔭)) = H_i(P_• ⊗_A κ(𝔭))` and, taking `(7.9.1.1)` into account, formula
`(7.9.2.1)` is none other than the invariance of the Euler–Poincaré characteristic of a finite complex of
finite-dimensional vector spaces under passage to homology `(0, 11.10.2)`.

**Corollary (7.9.3).**

<!-- label: III.7.9.3 -->

*The function*

```text
  𝔭 ↦ Σ_i (−1)^i rang_{κ(𝔭)} T_i(κ(𝔭))
```

*is locally constant on `Spec(A)`.*

**Theorem (7.9.4).**

<!-- label: III.7.9.4 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `𝒫_•` a finite complex of coherent and
`Y`-flat `𝒪_X`-modules. If one sets `𝒯_•(ℳ) = ℋ^•(f, 𝒫^• ⊗_{𝒪_X} ℳ)` (cf. `(7.7.1.1)`), the function*

<!-- original page 209 -->

```text
  y ↦ Σ_i (−1)^i rang_{κ(y)} T_i(κ(y))                                       (7.9.4.1)
```

*is locally constant on `Y`.*

**Proof.** One can restrict to the case where `Y = Spec(A)` is affine with noetherian ring `A`. Since the complex `𝒫_•`
is finite, one knows `(7.7.12, (i))` that one has `𝒯_p(ℳ) = ℋ_p(ℒ_• ⊗_{𝒪_Y} ℳ)`, where `ℒ_• = L̃_•`, `L_•` being a
finite complex of projective `A`-modules of finite type. The theorem then results from `(7.9.3)`.

**7.9.5.**

<!-- label: III.7.9.5 -->

Under the conditions of `(7.9.4)`, the function `(7.9.4.1)` is constant when `Y` is connected. When `Y` is connected and
non-empty, one denotes the unique (integer) value of `(7.9.4.1)` by `EP(f, 𝒫_•)` or `EP(Y, 𝒫_•)`, or simply `EP(𝒫_•)` if
there can be no confusion, and one says that this integer is the *Euler–Poincaré characteristic of `𝒫_•` relative to
`f`* (or to `Y`). In the general case, one will also denote `EP(f, 𝒫_•; y)` or `EP(Y, 𝒫_•; y)` or `EP(𝒫_•; y)` the
second member of `(7.9.4.1)`.

**7.9.6.**

<!-- label: III.7.9.6 -->

Under the hypotheses of `(7.9.4)` relative to `X`, `Y` and `f`, let

```text
  0 → 𝒫'_• →^u 𝒫_• →^v 𝒫''_• → 0
```

be an exact sequence of finite complexes of coherent and `Y`-flat `𝒪_X`-modules, the homomorphisms `u` and `v` being of
*even* degrees `2d`, `2d'` respectively. Since `𝒯_•` is a homological functor `(7.7.1)`, one has an exact sequence of
homology

```text
  → 𝒯_i(𝒫'_•, κ(y)) → 𝒯_{i+2d}(𝒫_•, κ(y)) → 𝒯_{i+2d'}(𝒫''_•, κ(y)) → 𝒯_{i−1}(𝒫'_•, κ(y)) → …
```

having moreover only a finite number of terms. By writing that the Euler–Poincaré characteristic of this complex is zero
`(0, 11.10.1)`, it follows at once

```text
  EP(𝒫_•; y) = EP(𝒫'_•; y) + EP(𝒫''_•; y)                                    (7.9.6.1)
```

for every `y ∈ Y`. Now, if for example `𝒫_• = (𝒫_i)` with `𝒫_i = 0` for `i < 0`, one has the exact sequence of complexes

```text
  … → 0 → 0 → 0 → 0 → …
            ↓ ↓ ↓
  … → 0 → 0 → 𝒫_1 → 𝒫_2 → …
            ↓ ↓ ↓ ↓
  … → 0 → 𝒫_0 → 𝒫_1 → 𝒫_2 → …
            ↓ ↓ ↓ ↓
  … → 0 → 𝒫_0 → 0 → 0 → …
            ↓ ↓ ↓
  … → 0 → 0 → 0 → 0 → …
```

the non-zero vertical arrows being the identity automorphisms; one can apply `(7.9.6.1)` to this exact sequence, whence,
by induction on the length of `𝒫_•`, the formula

```text
  EP(𝒫_•; y) = Σ_i (−1)^i EP(𝒫_i; y)                                         (7.9.6.2)
```

<!-- original page 210 -->

where, for every coherent `𝒪_X`-module `ℱ`, flat on `Y`, one denotes by `EP(ℱ; y)` (or `EP(f, ℱ; y)` or `EP(Y, ℱ; y)`)
the function `EP(𝒫_•; y)` corresponding to the complex `𝒫_•` whose only term `≠ 0` is of degree `0` and equal to `ℱ`.
One thus sees that one can reduce to studying the Euler–Poincaré characteristics of complexes reduced to a single term.

**Proposition (7.9.7).**

<!-- label: III.7.9.7 -->

*Under the hypotheses of `(7.9.4)`, let `Y'` be a locally noetherian prescheme, `g : Y' → Y` a morphism,
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`, `𝒫'_•` the finite complex `𝒫_• ⊗_{𝒪_Y} 𝒪_{Y'}` of `𝒪_{X'}`-modules; `𝒫'_•`
is formed of coherent and `Y'`-flat `𝒪_{X'}`-modules, and for every `y' ∈ Y'`, one has*

```text
  EP(𝒫'_•; y') = EP(𝒫_•; g(y')).                                             (7.9.7.1)
```

**Proof.** The `𝒪_{X'}`-modules `𝒫'_i`, being inverse images of the `𝒫_i` by the projection `X' → X`, are coherent, they
are `Y'`-flat by virtue of `(0_I, 6.2.1)` and `(1.4.14.5)`, the question being local on `X`, `Y` and `Y'`; finally, one
knows that `f'` is proper `(II, 5.4.2)`, hence the first member of `(7.9.7.1)` is defined. Formula `(7.9.7.1)` then
results from `(6.10.4.2)`, `(7.7.2)` and from lemma `(7.6.7)`, by reducing, as one can always do, to the case where `Y`
and `Y'` are affine.

**Proposition (7.9.8).**

<!-- label: III.7.9.8 -->

*Suppose the hypotheses of `(7.9.4)` satisfied and moreover that there exists an integer `i_0` such that `T_i(κ(y)) = 0`
for `i ≠ i_0` and every `y ∈ Y`. Then `𝒯_{i_0}(𝒪_Y) = ℋ^{−i_0}(f, 𝒫^•)` is a locally free `𝒪_Y`-module, whose rank at
`y ∈ Y` is equal to `(−1)^{i_0} EP(f, 𝒫_•; y)`.*

**Proof.** Note first that the hypotheses of `(7.4.4)` are satisfied by the `T_•^{𝒪_y}`, hence `(7.4.7)` is applicable
to them, and the hypothesis implies that `T_i^{𝒪_y}` is zero for `i ≠ i_0` by virtue of `(7.5.3)`; in view of `(7.3.3)`,
`𝒯_{i_0}` is therefore also exact, and consequently `(7.8.4)`, `ℋ^{−i_0}(f, 𝒫^•)` is locally free and its rank at a
point `y ∈ Y` is

```text
  rang_{κ(y)} T_{i_0}(κ(y)) = EP(f, 𝒫_•; y)
```

by definition, since `T_i(κ(y)) = 0` for `i ≠ i_0`.

**Corollary (7.9.9).**

<!-- label: III.7.9.9 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `ℱ` a coherent and `Y`-flat `𝒪_X`-module;
suppose that there exists an integer `i_0` such that `H^i(f^{−1}(y), ℱ ⊗_{𝒪_X} κ(y)) = 0` for every `i ≠ i_0` and every
`y ∈ Y`. Then `R^{i_0} f_*(ℱ)` is a locally free `𝒪_Y`-module, whose rank at `y` is equal to `(−1)^{i_0} EP(f, ℱ; y)`.*

In particular:

**Corollary (7.9.10).**

<!-- label: III.7.9.10 -->

*Under the preliminary conditions of `(7.9.9)` for `X`, `Y` and `ℱ`, suppose that one has `R^i f_*(ℱ) = 0` for every
`i > 0`. Then `f_*(ℱ)` is a locally free `𝒪_Y`-module, whose rank at `y` is equal to `EP(f, ℱ; y)`.*

**Proof.** It will suffice, by virtue of `(7.9.9)`, to prove the following lemma:

**Lemma (7.9.10.1).**

<!-- label: III.7.9.10.1 -->

*Under the hypotheses of `(7.9.10)`, one has `H^i(f^{−1}(y), ℱ ⊗_{𝒪_X} κ(y)) = 0` for every `i > 0` and every `y ∈ Y`.*

**Proof.** Indeed, one can restrict to the case where `Y = Spec(A)` is affine. With the notations of `(7.9.4)`, and
`𝒫_•` being reduced to its term of degree `0` equal to `ℱ`, one has indeed `𝒯_p(𝒪_Y) = 0` for `p < 0` by hypothesis; one
concludes from `(7.3.7)` that `𝒯_p` is exact for `p < 0`, and the lemma results then from the equivalence of
`(7.7.5, a))` and `(7.7.5, d))`.

<!-- original page 211 -->

**Proposition (7.9.11).**

<!-- label: III.7.9.11 -->

*The hypotheses being those of `(7.9.4)`, let `ℒ` be a very ample invertible `𝒪_X`-module for `Y`, and set
`𝒫_•(n) = 𝒫_• ⊗_{𝒪_X} ℒ^{⊗ n}` for every `n ∈ Z`. Then, for every `y ∈ Y`, the function*

```text
  n ↦ EP(f, 𝒫_•(n); y)                                                       (7.9.11.1)
```

*is a polynomial with coefficients in `Q`, which is the same for all points of one and the same connected component of
`Y`.*

**Proof.** It is clear that `𝒫_•(n)` is a complex of `Y`-flat `𝒪_X`-modules. By virtue of `(7.9.6.2)`, one can restrict
to the case where `𝒫_•` is reduced to a single term `ℱ ≠ 0` of degree `0`; moreover, since these are local questions on
`Y`, one can suppose `Y` affine and `f` projective `(II, 5.5.3)`; set `X_y = f^{−1}(y)`, and let `ℒ_y = ℒ ⊗_{𝒪_X} κ(y)`,
which is a very ample `𝒪_{X_y}`-module `(II, 4.4.10)`; by virtue of `(7.7.2)`, one has, for the functor `𝒯_•` relative
to the complex `𝒫_•(n)`, `T_i(κ(y)) = H^{−i}(X_y, ℱ_y ⊗ ℒ_y^{⊗ n})` (where `ℱ_y = ℱ ⊗_{𝒪_X} κ(y)`); whence it follows
that `EP(f, ℱ(n); y)` is none other than the Euler–Poincaré characteristic `χ_{κ(y)}(ℱ_y(n))` defined in `(2.5.1)`; the
fact that `(7.9.11.1)` is a polynomial then results from `(2.5.3)`; moreover, for each `n`, its value is constant on a
connected component of `Y` `(7.9.4)`, which completes the proof.

We shall denote by `PH(f, 𝒫_•; y)` or `PH(𝒫_•; y)` the polynomial `(7.9.11.1)`, with rational coefficients, and we shall
say that it is the *Hilbert polynomial at `y` relative to `𝒫_•`, `f` and `ℒ`* (or simply the *Hilbert polynomial at `y`
of `𝒫_•`*, or *of `f`*, if no confusion results); when `Y` is connected non-empty, one suppresses the mention of `y` in
the notation and the terminology. The invariant thus obtained will play an essential role in chap. V, in the theory of
"modules" of coherent quotient sheaves of a given coherent sheaf.

**7.9.12.**

<!-- label: III.7.9.12 -->

With the notations of `(7.9.6)` and `(7.9.11)`, one has

```text
  PH(𝒫_•; y) = PH(𝒫'_•; y) + PH(𝒫''_•; y)                                    (7.9.12.1)
```

and in particular

```text
  PH(𝒫_•; y) = Σ_i (−1)^i PH(𝒫_i; y);                                        (7.9.12.2)
```

this results trivially from `(7.9.6.1)` and `(7.9.6.2)`. Similarly, with the notations and hypotheses of `(7.9.7)`, one
has

```text
  PH(𝒫'_•; y') = PH(𝒫_•; g(y')).                                             (7.9.12.3)
```

Formula `(7.9.12.2)` reduces the study of Hilbert polynomials of a complex to that of Hilbert polynomials of a single
`Y`-flat `𝒪_X`-module. The latter admit a remarkable interpretation independent of homological considerations:

**Corollary (7.9.13).**

<!-- label: III.7.9.13 -->

*Let `Y` be a noetherian prescheme, `f : X → Y` a proper morphism, `ℒ` a very ample invertible `𝒪_X`-module for `Y`, `ℱ`
a coherent and `Y`-flat `𝒪_X`-module. There exists an integer `n_0` such that for `n ≥ n_0`, `f_*(ℱ(n))` is a locally
free `𝒪_Y`-module, of rank at `y ∈ Y` equal to `PH(f, ℱ; y)(n)`.*

**Proof.** Since the morphism `f` is projective `(II, 5.5.3)`, there exists `n_0` such that for `n ≥ n_0`

<!-- original page 212 -->

one has `R^i f_*(ℱ(n)) = 0` for every `i > 0` `(2.2.1)`; the conclusion therefore results from `(7.9.10)`.

The following flatness criterion will be important in the theory of "modules" of coherent sheaves in chap. V:

**Proposition (7.9.14).**

<!-- label: III.7.9.14 -->

*Let `Y` be a noetherian prescheme, `f : X → Y` a projective morphism, `ℒ` an invertible `𝒪_X`-module ample for `f`, and
set `ℱ(n) = ℱ ⊗ ℒ^{⊗ n}` for every `𝒪_X`-module `ℱ` and every `n ∈ Z`. For a coherent `𝒪_X`-module `ℱ` to be `Y`-flat,
it is necessary and sufficient that there exist an integer `n_0` such that, for every `n ≥ n_0`, `f_*(ℱ(n))` be a
locally free `𝒪_Y`-module.*

**Proof.** The necessity of the condition is proved as in `(7.9.13)` (the result of `(2.2.1)` applying to an ample sheaf
`ℒ`, since `f` is projective). To prove the converse, one can restrict to the case where `Y` is affine with ring `A`; by
virtue of the hypothesis and of `(2.2.2, (i))`, the `A`-modules `Γ(X, ℱ(n))` are of finite type and projective
(Bourbaki, *Alg. comm.*, chap. II, § 5, n° 2, th. 1). Let `S` be the graded ring `⊕_{n ≥ 0} Γ(X, ℒ^{⊗ n})`; one knows
that `X` is canonically identified with `Proj(S)` `(II, 4.5.2, (b) and 5.4.4)`. Let `M = ⊕_{n ≥ n_0} Γ(X, ℱ(n))`;
replacing if necessary `ℒ` by a power `ℒ^{⊗ d}`, one can suppose that `S` is generated by a finite number of elements of
degree 1 `(2.3.5.1)`, and it then results from `(II, 2.7.5 and 2.7.2)` that `ℱ` is identified with `𝒫𝒓𝒪𝒿_0(M)`. For
every homogeneous element `g ∈ S` of degree `> 0`, one has therefore `Γ(X_g, ℱ) = M_{(g)}`; now, `M`, the direct sum of
projective `A`-modules, is a flat `A`-module, hence so is `M_g` `(0_I, 6.3.2)`, and consequently so is `M_{(g)}`, which
is a direct factor of `M_g` `(0_I, 6.1.2)`. One concludes `(1.4.14.5)` that `ℱ` is `Y`-flat at every point of `X_g`, and
since the `X_g` cover `X`, the proposition is proved.

(*To be continued.*)

