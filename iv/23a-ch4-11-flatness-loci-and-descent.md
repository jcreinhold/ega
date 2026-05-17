<!-- original page 116 -->

## §11. Topological properties of flat morphisms of finite presentation; local criteria of flatness

While in §2 we considered the statements concerning flatness which do not depend on any finiteness hypothesis, and while
§6 studies the notion of flatness in the framework of locally Noetherian preschemes (but without finiteness hypothesis
on the morphisms), the present section is devoted to the notion of `f`-flatness in the case where the morphism
`f : X → Y` is locally of finite presentation. The interest of the notion of flat morphism of finite presentation lies
in the fact that it is the one which seems to express, in the most technically adequate manner, the intuitive notion of
"family of algebraic preschemes parameterized by a scheme `Y`", whose study is one of the principal objects of Algebraic
Geometry. Moreover, even if one were interested at the outset only in the case of a Noetherian base scheme, it is
indispensable, for certain technical reasons (for example, for certain applications of the theory of "descent", which
leads one to introduce schemes not necessarily Noetherian), not to confine oneself to that case, as soon as one deals
with problems of essentially relative nature linked to morphisms locally of finite presentation. We shall systematically
follow this principle, already supported by the results of §§8 and 9, in the entire continuation of this Chapter, and
even in the continuation of our Treatise, even at the cost of sacrificing on occasion the simplicity of certain proofs,
which Noetherian hypotheses sometimes permit one to lighten <sup>(\*)</sup>. In the present section, this leads us to
take up again, in the context of "finite presentation" (notably in n° 3) certain flatness statements already obtained in
the Noetherian context. The essential technical tool for making the reduction to the Noetherian case is the theorem of
compatibility of flatness with projective limits of preschemes `(11.2.6)`, completing the general results of §8. We also
prove in passing `(11.3.1)` a result often used in the sequel, implying that the set of points of flatness of a morphism
locally of finite presentation is open.

<sup>(\*)</sup> This principle is also inspired by the necessity of granting droit de cité, as "parameter spaces" for
families of algebraic schemes, to arbitrary ringed spaces (and even arbitrary ringed "toposes"), for which there can no
longer be any question in general of Noetherian hypotheses. It seems rather clear that one will no longer be able to
elude for long this new extension of Algebraic Geometry, and it is fitting from the present moment to develop the
"relative"-type notions and techniques of the theory of schemes in such a way that they can adapt practically as they
stand to this more general framework.

<!-- original page 117 -->

In nos. 4 to 8, we study the question of the "descent" of flatness, consisting in finding useful conditions on a
base-change morphism `Y' → Y` (not flat in general) so as to be able to conclude that if `X ×_Y Y'` is flat over `Y'`,
then `X` is flat over `Y`. These results, more technical than those of nos. 1 to 3, are of less frequent use in the
sequel; they will however play an important role in the non-projective construction techniques in the following chapter.
The only result of nos. 4 to 8 used in the sequel of Chap. IV is the valuative criterion of flatness (n° 8), which will
be applied in `(15.2)`.

Finally, nos. 9 and 10 are devoted to the study of a notion which makes precise, in the theory of schemes, that of
density in the topological sense, namely the notion of family of sub-preschemes *schematically dense* in a given
prescheme, and notably the study of the behaviour of this notion under base change (flat or arbitrary). This notion is
used above all, for the moment, in the study of group schemes.

### 11.1. Flatness loci (Noetherian case)

**Theorem (11.1.1).**

<!-- label: IV.11.1.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module.
Then the set `U` of `x ∈ X` such that `ℱ` is `f`-flat at the point `x` is open in `X`.*

The question being evidently local on `X` and `Y`, one may suppose `Y = Spec(A)`, `X = Spec(B)`, with `A` Noetherian and
`B` an `A`-algebra of finite type. One then has `ℱ = M̃`, where `M` is a `B`-module of finite type. Let us apply the
criterion `(0_III, 9.2.6)`: it therefore suffices to prove the following assertion:

```text
  (11.1.1.1) Let A be a Noetherian ring, B an A-algebra of finite type, M a B-module of finite type, 𝔮 a prime
             ideal of B, 𝔭 its inverse image in A. Suppose that M_𝔮 is a flat A_𝔭-module. Then there exists
             g ∈ B − 𝔮 such that for every prime ideal 𝔮' ⊃ 𝔮 of B with g ∉ 𝔮', M_{𝔮'} is a flat A_{𝔭'}-module,
             where 𝔭' denotes the inverse image of 𝔮' in A (it amounts to the same thing (0_I, 6.3.1) to say
             that M_{𝔮'} is a flat A-module).
```

To this end, let us consider `B_{𝔮'}` as an `A`-algebra; one evidently has `𝔭 B_{𝔮'} ⊂ 𝔮' B_{𝔮'}`. One then knows
`(0_III, 10.2.2)` that for `M_{𝔮'}` to be a flat `A`-module, it is necessary and sufficient that `M_{𝔮'}/𝔭 M_{𝔮'}` be a
flat `(A/𝔭)`-module and that one have `Tor_1^A(M_{𝔮'}, A/𝔭) = 0`. Now, one has `M_{𝔮'} = M ⊗_B B_{𝔮'}`; since `B_{𝔮'}`
is flat over `B`, one has `M_{𝔮'}/𝔭 M_{𝔮'} = (M/𝔭 M)_{𝔮'}` and `Tor_1^A(M_{𝔮'}, A/𝔭) = (Tor_1^A(M, A/𝔭))_{𝔮'}` (defining
`Tor` by means of a projective resolution of `A/𝔭`); for the same reason, since one must have `g ∉ 𝔮'`, `B_{𝔮'}` is flat
over `B_g`, hence `(M/𝔭 M)_{𝔮'} = ((M/𝔭 M)_g)_{𝔮' B_g}` and `(Tor_1^A(M, A/𝔭))_{𝔮'} = ((Tor_1^A(M, A/𝔭))_g)_{𝔮' B_g}`,
where in these formulas `M/𝔭 M` and `Tor_1^A(M, A/𝔭)` are considered as `B`-modules. Taking `(0_I, 6.3.2)` into account,
one sees that one is reduced to proving the

**Lemma (11.1.1.2).**

<!-- label: IV.11.1.1.2 -->

*Under the conditions of `(11.1.1.1)`, there exists `g ∈ B − 𝔮` such that:* *(i) `(M/𝔭 M)_g` is a flat `(A/𝔭)`-module;*
*(ii) `(Tor_1^A(M, A/𝔭))_g = 0`.*

<!-- original page 118 -->

By virtue of the generic flatness theorem `(6.9.1)` applied to the integral ring `A/𝔭`, to the `(A/𝔭)`-algebra of finite
type `B/𝔭 B`, and to the `(B/𝔭 B)`-module of finite type `M/𝔭 M`, there exists `h ∈ A − 𝔭` such that, if `h̄` is its
canonical image in `A/𝔭`, `(M/𝔭 M)_{h̄}` is a flat `(A/𝔭)`-module. On the other hand, since `M_𝔮` is a flat
`A_𝔭`-module, and consequently a flat `A`-module `(0_I, 6.3.1)`, one has `Tor_1^A(M_𝔮, A/𝔭) = 0`, which one also writes
`(Tor_1^A(M, A/𝔭))_𝔮 = 0`. But since `A` and `B` are Noetherian, `Tor_1^A(M, A/𝔭)` is a `B`-module of finite type, hence
`(0_I, 5.2.2)` there exists `g_1 ∈ B − 𝔮` such that `(Tor_1^A(M, A/𝔭))_{g_1} = 0`. Moreover, one has
`(M/𝔭 M)_{h̄} = (M/𝔭 M)_h` (`M/𝔭 M` being considered in the second member as an `A`-module); in addition, `(M/𝔭 M)_h`
being a `B`-module, `(M/𝔭 M)_{hg_1}` is again a flat `(A/𝔭)`-module, for it can be written `(M/𝔭 M)_{h̄ ḡ_1}`, where
`h̄ ḡ_1` is the canonical image of `h g_1` in `B/𝔭 B`, and it suffices to apply `(0_I, 6.3.2)`; finally, one has
`(Tor_1^A(M, A/𝔭))_{h g_1} = 0` and `h g_1 ∈ B − 𝔮` since `h ∈ A − 𝔭`. Q.E.D.

**Corollary (11.1.2).**

<!-- label: IV.11.1.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ`, `ℱ'` two coherent
`𝒪_X`-Modules, `u : ℱ' → ℱ` a homomorphism of `𝒪_X`-Modules. Suppose that `ℱ` is `f`-flat. Then the set `U` of `x ∈ X`
such that, setting `y = f(x)`, the homomorphism `u_x ⊗ 1 : ℱ'_x ⊗_{𝒪_y} k(y) → ℱ_x ⊗_{𝒪_y} k(y)` is injective, is open
in `X`.*

Indeed, let `𝒩` (resp. `𝒬`) be the kernel (resp. the cokernel) of `u`; let us apply `(0_III, 10.2.4)` <sup>(\*)</sup> to
the local rings `𝒪_y` and `𝒪_x` and to the `𝒪_y`-modules `ℱ'_x` and `ℱ_x`: to say that `u_x ⊗ 1` is injective amounts to
saying that `𝒩_x = 0` and that `𝒬` is `f`-flat at the point `x`. Now since `𝒩` and `𝒬` are coherent `(0_I, 5.3.4)`, the
set of `x` where `𝒩_x = 0` is open `(0_I, 5.2.2)`, and the set of `x` where `𝒬` is `f`-flat is open by `(11.1.1)`;
whence the conclusion.

In particular:

**Corollary (11.1.3).**

<!-- label: IV.11.1.3 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a flat morphism locally of finite type, `g` a section of `𝒪_X`
over `X`. The set of `x ∈ X` such that `g_x ⊗ 1` is not a zero-divisor in `𝒪_x ⊗_{𝒪_{f(x)}} k(f(x))` is open in `X`.*

It suffices to apply `(11.1.2)` to the endomorphism of `𝒪_X` defined by `g`.

**Corollary (11.1.4).**

<!-- label: IV.11.1.4 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module
which is `f`-flat. Let `(g_i)_{1 ≤ i ≤ n}` be a sequence of sections of `𝒪_X` over `X`. Then the set `U` of `x ∈ X` such
that the sequence `((g_i)_x ⊗ 1)` is `(ℱ_{f(x)} ⊗_{𝒪_{f(x)}} k(f(x)))`-regular is open in `X`.*

Since `ℱ` is `f`-flat, it follows from `(0_IV, 15.1.16)` that `U` is also the set of points

<sup>(\*)</sup> Here is a proof of `(0_III, 10.2.4)` which was not published in N. Bourbaki's *Algèbre commutative*.
Taking `(0_I, 6.1.2)` into account, it suffices to see that b) implies a). Set `P = Im(u)`, `Q = Coker(u)`,
`R = Ker(u)`. The composite `M ⊗ k → P ⊗ k → N ⊗ k` is injective, and `M ⊗ k → P ⊗ k` is surjective, hence
`P ⊗ k → N ⊗ k` is injective and `M ⊗ k → P ⊗ k` is bijective. The exact sequence `0 → P → N → Q → 0` gives the exact
sequence `0 → P ⊗ k → N ⊗ k → Q ⊗ k → 0` (since `P ⊗ k → N ⊗ k` is injective), and one has `Tor_1^A(Q, k) = 0`; since
`Q` is a `B`-module of finite type, `(0_III, 10.2.2)` shows that `Q` is a flat `A`-module; then `P` is also a flat
`A`-module by `(0_I, 6.1.2)`. The sequence `0 → R → M → P → 0` being exact, so is `0 → R ⊗ k → M ⊗ k → P ⊗ k → 0` by
`(0_I, 6.1.2)`; since `M ⊗ k → P ⊗ k` is bijective, one has `R ⊗ k = 0`; but since `B` is Noetherian, `R` is a
`B`-module of finite type, hence one has `R = 0` by virtue of Nakayama's lemma.

<!-- original page 119 -->

`x ∈ X` such that the sequence `(g_i)_x` is `ℱ_x`-regular and the `𝒪_x`-module `ℱ_x/(∑_{i=1}^n (g_i)_x ℱ_x)` is
`f`-flat. But `ℱ` and `ℱ/(∑ g_i ℱ)` are coherent, hence the corollary follows from `(11.1.1)` and `(0_IV, 15.2.4)`.

**Corollary (11.1.5).**

<!-- label: IV.11.1.5 -->

*Let `X`, `Y`, `Z` be three locally Noetherian preschemes, `f : X → Y`, `g : Y → Z` two morphisms of finite type, `ℱ` a
coherent `𝒪_X`-Module. Then the set `U` of `y ∈ Y` such that, for every generization `y'` of `y`, `ℱ` is `(g ∘ f)`-flat
at all points of `f⁻¹(y')` (i.e. such that `ℱ ⊗_Y Spec(𝒪_{Y, y'})` is flat relative to the morphism
`X ×_Y Spec(𝒪_{Y, y'}) → Z`) is open in `Y`.*

If `V` is the set of `x ∈ X` where `ℱ` is `(g ∘ f)`-flat, `U` is the set of `y ∈ Y` such that for every generization
`y'` of `y`, one has `f⁻¹(y') ⊂ V`. Now `V` is open `(11.1.1)`, hence locally constructible in `X`, and the set `W` of
`y ∈ Y` such that `f⁻¹(y) ⊂ V` is equal to `Y − f(X − V)`, hence is also locally constructible in `Y` by virtue of
Chevalley's theorem `(1.8.4)`. It then follows from `(0_III, 9.2.5)` that the points of `U` are the points interior to
`W`, whence the conclusion.

**Corollary (11.1.6).**

<!-- label: IV.11.1.6 -->

*Let `A` be a Noetherian ring, `B` an `A`-algebra of finite type, `C` a `B`-algebra of finite type, `M` a `C`-module of
finite type. Then the set of `𝔮 ∈ Spec(B)` such that `M_𝔮` is a flat `A`-module is open in `Spec(B)`.*

Taking `(2.1.2)` into account, this is a consequence of `(11.1.5)` applied to `Z = Spec(A)`, `Y = Spec(B)`,
`X = Spec(C)`, `ℱ = M̃`.

The results of this number will be freed of the Noetherian hypotheses in `(11.3)`.

### 11.2. Flatness of a projective limit of preschemes

(11.2.1) Let `A` be a ring, `M`, `N` two `A`-modules, `A'` an `A`-algebra; set `M' = M ⊗_A A'`, `N' = N ⊗_A A'`. Recall
`(III, 6.3.8)` that for every `i` one defines a canonical homomorphism of `A`-modules

```text
  (11.2.1.1)    φ_i : Tor_i^A(M, N) → Tor_i^{A'}(M', N')
```

in the following manner: one considers a left resolution of `M` by free `A`-modules

```text
  (11.2.1.2)    … → L_{i+1} →^{f_{i+1}} L_i → … → L_0 →^ε M → 0
```

whence one deduces by tensoring with `A'` a complex of `A'`-modules

```text
  (11.2.1.3)    … → L'_{i+1} →^{f'_{i+1}} L'_i → … → L'_0 →^{ε'} M' → 0
```

where one has set `L'_i = L_i ⊗_A A'`, `f'_i = f_i ⊗ 1_{A'}`, `ε' = ε ⊗ 1_{A'}`. Let us consider on the other hand a
left resolution of `M'` by free `A'`-modules

```text
  (11.2.1.4)    … → L''_{i+1} →^{f''_{i+1}} L''_i → … → L''_0 →^{ε''} M' → 0
```

<!-- original page 120 -->

Since the `L''_i` are free `A'`-modules, one knows `(M, V, 1.1)` that there are `A'`-homomorphisms `u_i` forming a
commutative diagram

```text
  L'_i  ─f'_i─→  L'_{i-1}  ─→  ⋯  ─→  L'_0  ─ε'─→  M'
   │              │                    │            ‖
   u_i           u_{i-1}                u_0          1_{M'}
   ↓              ↓                    ↓            ↓
  L''_i ─f''_i─→ L''_{i-1} ─→  ⋯  ─→  L''_0 ─ε''─→  M'
```

If one composes the homomorphism `u_• : L'_• → L''_•` of complexes thus defined with the canonical homomorphism
`L_• → L'_•`, one obtains a homomorphism of complexes of `A`-modules `L_• → L''_•`; noting that one has
`(L_i ⊗_A N) ⊗_A A' = L'_i ⊗_{A'} N'`, one deduces from this a homomorphism of complexes of `A`-modules
`L_• ⊗_A N → L''_• ⊗_{A'} N'`, whence, on passing to homology, the canonical homomorphisms `(11.2.1.1)`. Since the `u_i`
are well determined up to homotopy `(M, V, 1.1)`, the homomorphisms `(11.2.1.1)` do not depend on the choice of the
`u_i` nor on the choice of the free resolutions `L_•` and `L''_•`.

Since the `Tor_i^{A'}(M', N')` are `A'`-modules, one canonically deduces from `(11.2.1.1)` `A'`-homomorphisms

```text
  (11.2.1.5)    ψ_i : Tor_i^A(M, N) ⊗_A A' → Tor_i^{A'}(M', N').
```

Let us now consider two ring homomorphisms `α : A → A^{(1)}`, `β : A^{(1)} → A^{(2)}` and their composite
`β ∘ α : A → A^{(2)}`; set `M^{(j)} = M ⊗_A A^{(j)}`, `N^{(j)} = N ⊗_A A^{(j)}` for `j = 1, 2`. Then the canonical
composite homomorphism

```text
  Tor_i^A(M, N) → Tor_i^{A^{(1)}}(M^{(1)}, N^{(1)}) → Tor_i^{A^{(2)}}(M^{(2)}, N^{(2)})
```

is the same as the canonical homomorphism deduced from `β ∘ α`; this results from the fact that, if `L_•^{(j)}` is a
free resolution of `M^{(j)}`, the diagram

```text
  L_•^{(1)}  ─→  L_•^{(2)}
     ↑              ↑
     L_•   ──────────
```

is commutative.

(11.2.2) The notation being that of `(11.2.1)`, let us now consider a filtered inductive system of `A`-algebras
`(A_α, ξ_{βα})`, and for every index `α`, set `M_α = M ⊗_A A_α`, `N_α = N ⊗_A A_α`; it then follows from `(11.2.1)` that
for each `i`, `(Tor_i^{A_α}(M_α, N_α), ψ_{βα})`, where `ψ_{βα}` is the canonical homomorphism `(11.2.1.1)` corresponding
to `ξ_{βα}`, is an inductive system

<!-- original page 121 -->

of `A_α`-modules. Set `A' = lim A_α`, `M' = lim M_α = M ⊗_A A'`, `N' = lim N_α = N ⊗_A A'`; if one denotes by
`ξ_α : A_α → A'` the canonical homomorphism, one deduces from this canonical homomorphisms `(11.2.1.1)`
`ψ_α : Tor_i^{A_α}(M_α, N_α) → Tor_i^{A'}(M', N')` which (still by virtue of `(11.2.1)`) form an inductive system of
homomorphisms; we propose to complete the result of `(M, V, 9.4*)` by showing that the

```text
  (11.2.2.1)    ψ = lim ψ_α : lim_α Tor_i^{A_α}(M_α, N_α) → Tor_i^{A'}(M', N')
```

*are isomorphisms of `A'`-modules.* For this, we proceed as in `(M, V, 9.5*)`, associating to each `M_α` its canonical
free resolution. Everything boils down (taking into account the exactness of the functor `lim`) to proving the

**Lemma (11.2.2.2).**

<!-- label: IV.11.2.2.2 -->

*Let `(A_α, ξ_{βα})` be a filtered inductive system of rings, `(M_α, h_{βα})` an inductive system of sets,
`A' = lim A_α`, `M' = lim M_α`, `ξ_α : A_α → A'`, `h_α : M_α → M'` the canonical maps. For every `α`, let `F(M_α)` be
the `A_α`-module of formal linear combinations of elements of `M_α`; let similarly `F(M')` be the `A'`-module of formal
linear combinations of elements of `M'`; if `h'_{βα} : F(M_α) → F(M_β)` (for `α ≤ β`) and `h'_α : F(M_α) → F(M')` are
the `A_α`-homomorphisms deduced from `h_{βα}` and `h_α` respectively, `(F(M_α), h'_{βα})` is an inductive system of
`A_α`-modules and `(h'_α)` an inductive system of homomorphisms. Then*

```text
  h' = lim h'_α : lim F(M_α) → F(M') = F(lim M_α)
```

*is an isomorphism.*

For the proof, see *Bourbaki, Alg., chap. II, 3rd ed., §6, n° 6, cor. of prop. 10*.

(11.2.3) Let us resume the notation of `(11.2.1)` and consider particularly the case `i = 1`; set `T = Tor_1^A(M, N)`,
`T' = T ⊗_A A'`, `T'' = Tor_1^{A'}(M', N')`; then `ψ_1` is the homomorphism
`Ker(f_0 ⊗ 1_N)/Im(f_1 ⊗ 1_N) → Ker(f''_0 ⊗ 1_{N'})/Im(f''_1 ⊗ 1_{N'})` which is deduced by passage to quotients from
the restriction `Ker(f_0 ⊗ 1_N) → Ker(f''_0 ⊗ 1_{N'})` of

```text
  L_1 ⊗_A N → L''_1 ⊗_{A'} N'.
```

Set `R = Ker(ε)`, `R'' = Ker(ε'')`, so that one has the exact sequences

```text
  0 → R → L_0 →^ε M → 0    and    0 → R'' → L''_0 →^{ε''} M' → 0,
```

whence one deduces the exact sequences of homology

```text
  (11.2.3.1)    0 = Tor_1^A(L_0, N) → T →^∂ R ⊗_A N → L_0 ⊗_A N → M ⊗_A N → 0
  (11.2.3.2)    0 = Tor_1^{A'}(L''_0, N') → T'' →^{∂''} R'' ⊗_{A'} N' → L''_0 ⊗_{A'} N' → M' ⊗_{A'} N' → 0
```

One has on the other hand a homomorphism of `A'`-modules

```text
  v : R' = Ker(ε) ⊗_A A' → Ker(ε') →^∼ Ker(ε'') = R''.
```

<!-- original page 122 -->

Let us show that the diagram

```text
  (11.2.3.3)
       T'  ─∂⊗1─→  R' ⊗_{A'} N'  ─→  L'_0 ⊗_{A'} N'  ─→  M' ⊗_{A'} N'
       │              │                  ‖                   ‖
       ψ_1            v ⊗ 1              u_0 ⊗ 1             1
       ↓              ↓                  ↓                   ↓
       T''  ─∂''─→  R'' ⊗_{A'} N'  ─→  L''_0 ⊗_{A'} N'  ─→  M' ⊗_{A'} N'
```

is commutative. For this, one verifies at once `(M, IV, 1)` that the homomorphism `∂ : T → R ⊗_A N` comes (in the
present case) by passage to the quotient from the homomorphism `w : Ker(f_0 ⊗ 1_N) → R ⊗_A N`, restriction of the
homomorphism `g_0 ⊗ 1_N : L_1 ⊗_A N → R ⊗_A N`, where `g_0 : L_1 → R` is such that `f_0 = j ∘ g_0`; similarly for `∂''`.
It therefore suffices to see that the diagram

```text
  Ker(f_0 ⊗ 1_N)  ─→  R ⊗_A N  ─→  R' ⊗_{A'} N' = (R ⊗_A N) ⊗_A A'
       │                                            │
       ↓                                            ↓
  Ker(f''_0 ⊗ 1_{N'}) ──────────────────────────→  R'' ⊗_{A'} N'
```

is commutative, which results from the commutativity of the diagram

```text
  L_1  ─→  R
   │       │
   ↓       ↓
  L''_1 ─→ R''.
```

**Lemma (11.2.4).**

<!-- label: IV.11.2.4 -->

*Let `A` be a ring, `C` an `A`-algebra, `M` an `A`-module, `N` a `C`-module, `A'` an `A`-algebra. Set `C' = C ⊗_A A'`,
`M' = M ⊗_A A'`, `N' = N ⊗_A A' = N ⊗_C C'`. Suppose that `M ⊗_A N` is a flat `C`-module. Then the canonical
homomorphism*

```text
  ψ_1 : Tor_1^A(M, N) ⊗_A A' → Tor_1^{A'}(M', N')
```

*(cf. `(11.2.1.5)`) is surjective.*

Let us keep the notation of `(11.2.3)`; right exactness of the tensor product shows that the sequence
`L'_1 → L'_0 → M' → 0` is exact; since `L'_0` and `L'_1` are free `A'`-modules, one may suppose that one has taken
`L''_0 = L'_0`, `L''_1 = L'_1`, with `u_0` and `u_1` being the identity maps and `f''_0 = f'_0`. Since `R = Im(f_1)` and
`R'' = Im(f''_1) = Im(f'_1)`, the homomorphism `v` is surjective, and so therefore is `v ⊗ 1`. The proof will be
complete if one proves that the first row of `(11.2.3.3)` is exact, `ε ⊗ 1` being surjective and `u_0 ⊗ 1` injective
*(Bourbaki, Alg. comm., chap. I, §1, n° 4, cor. 2 of prop. 2)*. Let us use for this

<!-- original page 123 -->

the hypothesis that `M ⊗_A N` is a flat `C`-module. Setting `Q = Ker(ε ⊗ 1) = Im(j ⊗ 1)` in the exact sequence
`(11.2.3.1)`, one has the two exact sequences `0 → Q → L_0 ⊗_A N → M ⊗_A N → 0` and `T → R ⊗_A N → Q → 0`, where the
homomorphisms are `C`-module homomorphisms; using the flatness hypothesis, one deduces from this `(0_I, 6.1.2)` the
exact sequence

```text
  0 → Q ⊗_C C' → (L_0 ⊗_A N) ⊗_C C' → (M ⊗_A N) ⊗_C C' → 0
```

and on the other hand, the tensor product being right exact, one has the exact sequence

```text
  T ⊗_C C' → (R ⊗_A N) ⊗_C C' → Q ⊗_C C' → 0
```

whence finally the exact sequence

```text
  T ⊗_C C' → (R ⊗_A N) ⊗_C C' → (L_0 ⊗_A N) ⊗_C C' → (M ⊗_A N) ⊗_C C' → 0.
```

But by definition, for every `C`-module `P`, one has `P ⊗_C C' = P ⊗_A A'`, whence the conclusion.

**Lemma (11.2.5).**

<!-- label: IV.11.2.5 -->

*Let `A` be a ring, `𝔍` an ideal of `A`, `B` an `A`-algebra, `M` a `B`-module, `A → A'` a ring homomorphism. Set
`𝔍' = 𝔍 A'`, `B' = B ⊗_A A'`, `M' = M ⊗_A A' = M ⊗_B B'`. Let `𝔭'` be a prime ideal of `B'` containing `𝔍 B'`. Suppose
one of the following hypotheses is verified:*

*a) `𝔍` is nilpotent.*

*b) `A'` is Noetherian, `B'` is an `A'`-algebra of finite type, `M'` an `B'`-module of finite type.*

*Under these conditions, suppose verified the following two properties:*

*(i) `M ⊗_A (A/𝔍)` is a flat `(A/𝔍)`-module.*

*(ii) The canonical composite homomorphism*

```text
  Tor_1^A(M, A/𝔍) → Tor_1^{A'}(M', A'/𝔍') → (Tor_1^{A'}(M', A'/𝔍'))_{𝔭'}
```

*(where `ψ_1` is the homomorphism `(11.2.1.1)` and `θ` the canonical homomorphism from a `B'`-module to its localization
at `𝔭'`) is zero.*

*Then `M'_{𝔭'}` is a flat `A'`-module.*

Note that in hypothesis b), `M'_{𝔭'}` is a `B'_{𝔭'}`-module of finite type, `B'_{𝔭'}` a Noetherian `A'`-algebra, and
`𝔍' B'_{𝔭'}` is contained in the radical `𝔭' B'_{𝔭'}` of `B'_{𝔭'}`; in hypothesis a), `𝔍'` is nilpotent; one will
therefore be able to apply the flatness criterion `(0_III, 10.2.1)` or `(0_III, 10.2.2)` according as a) or b) is
verified. In the first place, one has
`M'_{𝔭'} ⊗_{A'} (A'/𝔍') = (M' ⊗_{A'} (A'/𝔍'))_{𝔭'} = ((M ⊗_A (A/𝔍)) ⊗_{A/𝔍} (A'/𝔍'))_{𝔭'}`; hypothesis (i) therefore
entails that `M'_{𝔭'} ⊗_{A'} (A'/𝔍')` is a flat `(A'/𝔍')`-module, taking `(0_I, 6.2.1 and 6.3.2)` into account. It
remains therefore to see that `Tor_1^{A'}(M'_{𝔭'}, A'/𝔍') = 0`; but this `B'_{𝔭'}`-module is equal to
`(Tor_1^{A'}(M', A'/𝔍'))_{𝔭'}` by virtue of the flatness of `B'_{𝔭'}` over `B'`. But by virtue of hypothesis (ii), the
composite homomorphism `θ ∘ ψ_1 : Tor_1^A(M, A/𝔍) ⊗_A A' → (Tor_1^{A'}(M', A'/𝔍'))_{𝔭'}` is zero; moreover, `(11.2.4)`
applied to `C = A/𝔍` and `N = C` shows (taking hypothesis (i) into account) that `ψ_1` is surjective (for
`A'/𝔍' = C ⊗_A A'`); hence the homomorphism `θ` is zero, and since the image under `θ` of `Tor_1^{A'}(M', A'/𝔍')`
generates the `B'_{𝔭'}`-module `(Tor_1^{A'}(M', A'/𝔍'))_{𝔭'}`, the latter is zero. Q.E.D.

**Theorem (11.2.6).**

<!-- label: IV.11.2.6 -->

*The notation being that of `(8.5.1)` and `(8.8.1)`, suppose `S_α` quasi-compact, `X_α` and `Y_α` of finite presentation
over `S_α`; let `f_α : X_α → Y_α` be an `S_α`-morphism, `ℱ_α` a quasi-coherent `𝒪_{X_α}`-Module of finite presentation.*

*(i) Let `x` be a point of `X`, `x_λ` its canonical projection in `X_λ`. For `ℱ` to be `f`-flat at the point `x`, it is
necessary and sufficient that there exist `λ ≥ α` such that `ℱ_λ` is `f_λ`-flat at the point `x_λ`.*

*(ii) For `ℱ` to be `f`-flat, it is necessary and sufficient that there exist `λ ≥ α` such that `ℱ_λ` is `f_λ`-flat.*

One may suppose that `S_α = S_0`; since `Y_0` is of finite presentation over `S_0`, `Y_0` is quasi-compact, and
`f_0 : X_0 → Y_0` is a morphism of finite presentation `(1.6.2, (v))`, hence one may also confine oneself to the case
where `S_0 = Y_0`. Moreover, by virtue of the quasi-compactness of `S_0` and of the fact that the index set `L` is
filtered, one may confine oneself to the case where `S_0 = Spec(A_0)` is affine. In addition `X_0` is quasi-compact,
hence the same reasoning shows that one may also suppose `X_0 = Spec(B_0)` affine; one then has `ℱ_0 = M̃_0`, where
`M_0` is a `B_0`-module of finite presentation, and the statement `(11.2.6)` is in this case equivalent to the following
(taking `(0_I, 6.3.1)` into account):

**Corollary (11.2.6.1).**

<!-- label: IV.11.2.6.1 -->

*Let `A_0` be a ring, `(A_λ)_{λ ∈ L}` a filtered inductive system of `A_0`-algebras, `B_0` an `A_0`-algebra of finite
presentation, `M_0` a `B_0`-module of finite presentation. Set `B_λ = B_0 ⊗_{A_0} A_λ`,
`M_λ = M_0 ⊗_{A_0} A_λ = M_0 ⊗_{B_0} B_λ`, `A = lim A_λ`, `B = lim B_λ = B_0 ⊗_{A_0} A`,
`M = lim M_λ = M_0 ⊗_{A_0} A = M_0 ⊗_{B_0} B`.*

*(i) Let `𝔭` be a prime ideal of `B`, and for every `λ`, let `𝔭_λ` be its inverse image in `B_λ`. For `M_𝔭` to be a flat
`A`-module, it is necessary and sufficient that there exist `λ` such that `(M_λ)_{𝔭_λ}` is a flat `A_λ`-module.*

*(ii) For `M` to be a flat `A`-module, it is necessary and sufficient that there exist `λ` such that `M_λ` is a flat
`A_λ`-module.*

One has only to prove that the conditions are necessary `(2.1.4)`. We shall proceed in several steps.

*I) Reduction to the case where the `A_λ` are Noetherian.* By virtue of `(8.9.1)`, there exists a sub-ring `A'_0` of
`A_0` which is a `ℤ`-algebra of finite type, an `A'_0`-algebra of finite type `B'_0` and a `B'_0`-module of finite type
`M'_0` such that one has `B_0 = B'_0 ⊗_{A'_0} A_0` and `M_0 = M'_0 ⊗_{A'_0} A_0`; since one has
`B_λ = B'_0 ⊗_{A'_0} A_λ` and `M_λ = M'_0 ⊗_{A'_0} A_λ`, one may replace `A_0`, `B_0`, `M_0` by `A'_0`, `B'_0`, `M'_0`
in the statement of `(11.2.6.1)`, considering the `A_λ` as `A'_0`-algebras; one may therefore already suppose that `A_0`
is Noetherian. Let `H` be the set of pairs `(λ, C_λ)`, where `C_λ` is a sub-`A_0`-algebra of finite type of `A_λ`; order
`H` by setting `(λ, C_λ) ≤ (μ, D_μ)` if `λ ≤ μ` and the homomorphism `φ_{μλ} : A_λ → A_μ` is such that
`φ_{μλ}(C_λ) ⊂ D_μ`; for this order `H` is filtered increasing, for if `(λ, C_λ)` and `(μ, D_μ)` are two arbitrary
elements of `H`, one majorizes them by an `(ν, E_ν)` by taking `ν ≥ λ`, `ν ≥ μ` in `L`, then `E_ν` equal to the
sub-`A_0`-algebra of `A_ν` generated by `φ_{νλ}(C_λ)` and `φ_{νμ}(D_μ)`. For an element `ξ = (λ, C_λ)` of `H`, one will
set `A_ξ = C_λ`, and for `ξ ≤ η = (μ, D_μ)` (hence `λ ≤ μ` and `φ_{μλ}(C_λ) ⊂ D_μ`), `φ_{ηξ} : A_ξ → A_η` will be the
restriction to `C_λ` of `φ_{μλ}`, considered as a homomorphism into `D_μ`; it is clear that one thus obtains a filtered
inductive system of `A_0`-algebras. One sets `B_ξ = B_0 ⊗_{A_0} A_ξ`, `M_ξ = M_0 ⊗_{A_0} A_ξ`; this time the `A_ξ` are
Noetherian; moreover the double-inductive-limit formula *(Bourbaki, Alg., chap. II, 3rd ed., §6, n° 4, prop. 7)* proves
that one again has `lim_H A_ξ = A`, `lim_H B_ξ = B`, `lim_H M_ξ = M`. Suppose

<!-- original page 125 -->

`(11.2.6.1)` proved for the inductive system `(A_ξ)_{ξ ∈ H}`; let `𝔭` be a prime ideal of `B`, such that `M_𝔭` is a flat
`A`-module; there then exists `ξ ∈ H` such that, if `𝔭_ξ` is the inverse image of `𝔭` in `B_ξ`, `(M_ξ)_{𝔭_ξ}` is a flat
`A_ξ`-module. Let `ξ = (λ, C_λ)`, so that the injection `A_ξ = C_λ → A_λ` gives a homomorphism
`B_ξ = B_0 ⊗_{A_0} C_λ → B_λ = B_0 ⊗_{A_0} A_λ`, and if `𝔭_λ` is the inverse image of `𝔭` in `B_λ`, `𝔭_ξ` is the inverse
image of `𝔭_λ` in `B_ξ`; consequently `(M_λ)_{𝔭_λ} = (M_ξ ⊗_{C_λ} A_λ)_{𝔭_λ} = ((M_ξ)_{𝔭_ξ} ⊗_{C_λ} A_λ)_{𝔭_λ}`, hence
`(M_λ)_{𝔭_λ}` is a flat `A_λ`-module `(0_I, 6.2.1 and 6.3.2)`. One treats similarly case (ii) of the statement. We may
therefore in the sequel suppose the `A_λ` Noetherian for `λ ∈ L` (but not necessarily `A` itself).

*II) Reduction of the global statement (ii) to the pointwise statement (i).* Suppose that `ℱ` is `f`-flat. For every
`λ`, let `U_λ` be the set of `x_λ ∈ X_λ` such that `ℱ_λ` is `f_λ`-flat at the point `x_λ`; one knows that `U_λ` is open
in `X_λ` since `S_λ` is Noetherian and `f_λ` of finite type `(11.1.1)`; let `V_λ = v_λ^{-1}(U_λ)` be its inverse image
in `X`. Since by hypothesis, for every `x ∈ X`, there is a `λ` such that `ℱ_λ` is `f_λ`-flat at the point `x_λ`,
projection of `x` in `X_λ`, this signifies that `x ∈ V_λ` for some `λ`; in other words, `X` is the union of the `V_λ`.
Moreover `(2.1.4)`, for `λ ≤ μ`, one has `V_λ ⊂ V_μ`, hence, since `X` is quasi-compact, there exists an index `μ` such
that `X = V_μ`. Since the `X_λ` are quasi-compact, it follows from `(8.3.4)` that there exists an index `ν ≥ μ` such
that `v_{νμ}^{-1}(U_μ) = X_ν`; but by `(2.1.4)`, this entails that `ℱ_ν` is `f_ν`-flat.

*III) End of the proof.* It remains to prove (i), supposing `S_0` affine and Noetherian; if `y_0` is the projection of
`x` in `S_0`, one may in addition, by virtue of `(2.1.4)` and `(I, 3.6.5)`, replace `S_0` by `Spec(𝒪_{S_0, y_0})`, in
other words one may confine oneself to the case where `A_0` is a Noetherian local ring, of maximal ideal `𝔪_0 = y_0`; by
definition, `𝔪_0` is the inverse image of the prime ideal `𝔭 = x` of `B`, and `M_𝔭` is supposed to be a flat `A`-module;
one therefore has in particular `Tor_1^A(A/𝔪_0 A, M_𝔭) = 0`, which also writes, since the `Tor_i^A(A/𝔪_0 A, M)` are
`B`-modules and `B_𝔭` is flat over `B`, `(Tor_1^A(A/𝔪_0 A, M))_𝔭 = 0`. Let us note now that `Tor_1^{A_0}(A_0/𝔪_0, M_0)`
is a `B_0`-module of finite type, for one may define it by taking a resolution of `A_0/𝔪_0` by free `A_0`-modules of
finite type (since `A_0` is Noetherian) and tensoring with `M_0`, which gives `B_0`-modules of finite type; since `B_0`
is Noetherian, the homology of the complex thus obtained is indeed formed of `B_0`-modules of finite type. Let
`(t_i^0)_{1 ≤ i ≤ m}` be a system of generators of the `B_0`-module `Tor_1^{A_0}(A_0/𝔪_0, M_0)` and let `t_i` be the
canonical image `(11.2.1.1)` of `t_i^0` in `Tor_1^A(A/𝔪_0 A, M)`. The hypothesis entails that there exists `h ∈ B − 𝔭`
such that `h t_i = 0` for `1 ≤ i ≤ m`. Now one has `(11.2.2.1)`
`Tor_1^A(A/𝔪_0 A, M) = lim_λ Tor_1^{A_λ}(A_λ/𝔪_0 A_λ, M_λ)`; there exists therefore a `λ` such that, if the `t_i^λ` are
the images of the `t_i^0` in `Tor_1^{A_λ}(A_λ/𝔪_0 A_λ, M_λ)`, there exists `h_λ ∈ B_λ` of image `h`, such that
`h_λ t_i^λ = 0` for `1 ≤ i ≤ m`. Let `𝔭_λ = v_λ(𝔭)` be the prime ideal of `B_λ` inverse image of `𝔭`; one has
`h_λ ∈ B_λ − 𝔭_λ`, hence the canonical images of the `t_i^λ` in `(Tor_1^{A_λ}(A_λ/𝔪_0 A_λ, M_λ))_{𝔭_λ}` are zero, and
consequently the homomorphism `Tor_1^{A_0}(A_0/𝔪_0, M_0) → (Tor_1^{A_λ}(A_λ/𝔪_0 A_λ, M_λ))_{𝔭_λ}` is zero. The
conditions of lemma `(11.2.5)` are therefore satisfied (`A_0/𝔪_0` being a field), and `(M_λ)_{𝔭_λ}` is a flat
`A_λ`-module, which finishes the proof of the theorem.

**Corollary (11.2.7).**

<!-- label: IV.11.2.7 -->

*Let `S = Spec(A)` be an affine scheme, `f : X → S` a morphism, `ℱ` a quasi-coherent `𝒪_X`-Module, `x` a point of `X`.
The following conditions are equivalent:*

*a) `f` is a morphism of finite presentation, `ℱ` is an `𝒪_X`-Module of finite presentation and `ℱ` is `f`-flat at the
point `x` (resp. `f`-flat).*

<!-- original page 126 -->

*b) There exist a Noetherian affine scheme `S_0 = Spec(A_0)`, a morphism of finite type `f_0 : X_0 → S_0`, a coherent
`𝒪_{X_0}`-Module `ℱ_0`, a morphism `S → S_0` such that the `S`-prescheme `X_0 ⊗_{S_0} S` is `S`-isomorphic to `X` and
that, if one identifies `X` with `X_0 ⊗_{S_0} S`, `ℱ` is isomorphic to `ℱ_0 ⊗_{𝒪_{S_0}} 𝒪_S`, and `ℱ_0` is `f_0`-flat at
the point `x_0` projection of `x` in `X_0` (resp. `f_0`-flat).*

*c) The conditions of b) are verified and in addition `A_0` is a sub-`ℤ`-algebra of finite type of `A`, the morphism
`S → S_0` corresponding to the canonical injection `A_0 → A`.*

It is clear that c) implies b) and b) implies a) by virtue of `(2.1.4)`. On the other hand, one may consider `A` as the
inductive limit of its sub-`ℤ`-algebras of finite type, and one knows by `(8.9.1)` that there is such a sub-algebra
`A_0` and a morphism of finite type `f_0 : X_0 → S_0` such that `X` is `S`-isomorphic to `X_0 ×_{S_0} S` and `ℱ`
isomorphic to `ℱ_0 ⊗_{𝒪_{S_0}} 𝒪_S`; one may therefore write `X = lim X_λ`, where `X_λ = X_0 ⊗_{A_0} A_λ`, `A_λ` running
through the set of sub-`ℤ`-algebras of finite type of `A` containing `A_0`, and `ℱ = v_λ^*(ℱ_λ)`, where `v_λ : X → X_λ`
is the canonical projection and `ℱ_λ = ℱ_0 ⊗_{A_0} A_λ`. It follows from `(11.2.6)` that there exists `λ` such that
`ℱ_λ` is `f_λ`-flat at the point `x_λ = v_λ(x)` (resp. `f_λ`-flat); then the sub-ring `A_λ` of `A` verifies the
conditions of c).

**Proposition (11.2.8).**

<!-- label: IV.11.2.8 -->

*Let `g : X → S`, `h : Y → S` be two morphisms of finite presentation, `f : X → Y` an `S`-morphism, `ℱ` a quasi-coherent
`𝒪_X`-Module of finite presentation; for every `s ∈ S`, let `X_s = g⁻¹(s) = X ×_S Spec(k(s))`,
`Y_s = h⁻¹(s) = Y ×_S Spec(k(s))`, `f_s` the morphism `f ×_S 1 : X_s → Y_s`, `ℱ_s = ℱ ⊗_{𝒪_S} k(s)`. Then the set `E` of
`s ∈ S` such that `ℱ_s` is `f_s`-flat is locally constructible.*

The property that we wish to show constructible verifies condition `(9.2.1, (i))`, by virtue of `(2.2.13)` and
`(2.5.1)`. Taking `(9.2.3)` into account, one may therefore confine oneself to the case where `S` is affine, Noetherian,
and integral, with generic point `η`, and to prove that `E` or `S − E` is a neighbourhood of `η` in `S`. If `η ∈ S − E`,
this follows at once from lemma `(9.4.7.1)`. If on the contrary `η ∈ E`, it follows first of all from `(11.2.6)`,
applied according to the method of `(8.1.2, a))`, that there is an open neighbourhood `U` of `η` in `S` such that
`ℱ | g⁻¹(U)` is `h⁻¹(U)`-flat; *a fortiori* `(2.1.4)` `ℱ_s` is `f_s`-flat for every `s ∈ U`, which finishes the proof.

The following theorem generalizes `(11.2.6.1, (ii))`:

**Theorem (11.2.9) (Raynaud).**

<!-- label: IV.11.2.9 -->

*Let `A_0` be a ring, `(A_λ)_{λ ∈ L}` a filtered inductive system of `A_0`-algebras, `B_0` an `A_0`-algebra of finite
presentation, `𝔍_0` an ideal of finite type of `B_0`, `M_0` a `B_0`-module of finite presentation. Set
`B_λ = B_0 ⊗_{A_0} A_λ`, `𝔍_λ = 𝔍_0 B_λ`, `M_λ = M_0 ⊗_{A_0} A_λ = M_0 ⊗_{B_0} B_λ`, `A = lim A_λ`,
`B = lim B_λ = B_0 ⊗_{A_0} A`, `𝔍 = 𝔍_0 B`, `M = lim M_λ = M_0 ⊗_{A_0} A = M_0 ⊗_{B_0} B`. For `gr_𝔍^•(M)` to be a flat
`A`-module, it is necessary and sufficient that there exist `λ` such that `gr_{𝔍_λ}^•(M_λ)` is a flat `A_λ`-module; the
canonical homomorphisms*

```text
  (11.2.9.1)    gr_{𝔍_λ}^•(M_λ) ⊗_{A_λ} A_μ → gr_{𝔍_μ}^•(M_μ)    for μ ≥ λ
```

*are then bijective and `gr_{𝔍_μ}^•(M_μ)` is a flat `A_μ`-module for `μ ≥ λ`.*

Let us first show that the conditions are sufficient, which amounts to proving the bijectivity of `(11.2.9.1)`. This
follows from the following lemma:

<!-- original page 127 -->

**Lemma (11.2.9.2).**

<!-- label: IV.11.2.9.2 -->

*Let `A` be a ring, `B` an `A`-algebra, `M` a `B`-module, `𝔍` an ideal of `B`. Let `A'` be an `A`-algebra; set
`B' = B ⊗_A A'`, `M' = M ⊗_A A' = M ⊗_B B'`, `𝔍' = 𝔍 B'`. If `gr_𝔍^•(M)` is a flat `A`-module, the canonical
homomorphism*

```text
  gr_𝔍^•(M) ⊗_A A' → gr_{𝔍'}^•(M')
```

*is bijective.*

Indeed, by induction on `k`, the hypothesis that the `𝔍^k M/𝔍^{k+1} M` are flat `A`-modules for `k ≥ 0` first entails,
by `(0_I, 6.1.2)`, that `M/𝔍^{k+1} M` is a flat `A`-module; moreover `(0_I, 6.1.2)`, the sequence

```text
  0 → (𝔍^{k+1} M) ⊗_A A' → M ⊗_A A' → (M/𝔍^{k+1} M) ⊗_A A' → 0
```

is then exact, in other words `(𝔍^{k+1} M) ⊗_A A'` identifies with its canonical image in `M' = M ⊗_A A'`. On the other
hand, still by virtue of `(0_I, 6.1.2)`, the sequence

```text
  0 → (𝔍^{k+1} M) ⊗_A A' → (𝔍^k M) ⊗_A A' → (𝔍^k M/𝔍^{k+1} M) ⊗_A A' → 0
```

is exact, which proves the lemma.

To prove the necessity of the conditions of `(11.2.9)`, we shall proceed in several steps.

*I) Reduction to the case where the `A_λ` are Noetherian.* — One proceeds as in reduction I) of `(11.2.6.1)`, whose
notation we keep; one must simply begin by replacing `A'_0` by a sub-`A'_0`-algebra of finite type `A''_0` of `A_0` such
that, if one sets `B''_0 = B'_0 ⊗_{A'_0} A''_0`, there is in `B''_0` an ideal of finite type `𝔍''_0` such that
`𝔍''_0 B_0 = 𝔍_0`. For this, one considers the sub-`A'_0`-algebras `A''_β` of finite type of `A_0`, which form a
filtered family, and one has `B_0 = lim B''_β`, where `B''_β = B'_0 ⊗_{A'_0} A''_β`; there is therefore an index `β`
such that a finite system of generators of `𝔍_0` is formed of images in `B_0` of elements of `B''_β`; one will then take
`A''_0 = A''_β`, `B''_0 = B''_β` and for `𝔍''_0` the ideal generated by these elements. One may therefore suppose that
`A_0` (hence also `B_0`) is Noetherian. One then defines as *loc. cit.* the filtered set `H` and the `A_ξ`, `B_ξ`, `M_ξ`
for `ξ ∈ H`; one will also set `𝔍_ξ = 𝔍_0 B_ξ` for every `ξ ∈ H`. Suppose then that one has proved that there exists a
`ξ = (λ, C_λ)` such that `gr_{𝔍_ξ}^•(M_ξ)` is a flat `C_λ`-module; since `M_λ = M_ξ ⊗_{C_λ} A_λ`, it follows from
`(11.2.9.2)` that `gr_{𝔍_λ}^•(M_λ)` is a flat `A_λ`-module.

*II) Preliminary lemmas.*

**Lemma (11.2.9.3).**

<!-- label: IV.11.2.9.3 -->

*Let `A` be a ring, `B = ⨁_{i ≥ 0} B_i` a graded `A`-algebra with positive degrees, `M = ⨁ M_i` a graded `B`-module.
Suppose that `B_0` is a local ring, and that each of the `M_i` is a `B_0`-module of finite type. For `M` to be a
`B`-module of finite type, it is necessary and sufficient that, if `𝔮` is the inverse image in `A` of the maximal ideal
`𝔪` of `B_0`, `M ⊗_A k(𝔮)` be a `(B ⊗_A k(𝔮))`-module of finite type.*

The condition being evidently necessary, let us prove that it is sufficient. Since `B_0` (and consequently `B`) is an
`A_𝔮`-algebra, one may replace `A` by `A_𝔮`, in other words suppose

<!-- original page 128 -->

that `A` is also a local ring of which `𝔮` is the maximal ideal. By hypothesis, there exists an integer `N` such that
the canonical homomorphism

```text
  ⨁_{i ≤ N} M_i ⊗_A k(𝔮) → M ⊗_A k(𝔮)
```

is surjective; this also signifies that, for every integer `n`, the canonical homomorphism of `k(𝔮)`-modules

```text
  ⨁_{i ≤ N} B_{n-i} ⊗_{B_0} M_i ⊗_A k(𝔮) → M_n ⊗_A k(𝔮)
```

is surjective. Now, `M_n` is a `B_0`-module of finite type, `B_0` a local ring and `𝔮 B_0 ⊂ 𝔪`; hence Nakayama's lemma
proves that each of the canonical homomorphisms

```text
  ⨁_{i ≤ N} B_{n-i} ⊗_{B_0} M_i → M_n
```

is surjective, whence the conclusion.

**Corollary (11.2.9.4).**

<!-- label: IV.11.2.9.4 -->

*Under the hypotheses of `(11.2.9.3)`, suppose in addition that each of the `B_i` and each of the `M_i` is a
`B_0`-module of finite presentation, and that `M` is a flat `A`-module. For `M` to be a `B`-module of finite
presentation, it is necessary and sufficient that `M ⊗_A k(𝔮)` be a `(B ⊗_A k(𝔮))`-module of finite presentation.*

By virtue of `(11.2.9.3)`, if the condition of the statement is verified, `M` is a `B`-module of finite type, hence
there exists a graded free `B`-module of finite type `L` (having therefore a finite basis formed of homogeneous
elements) and a surjective graded homomorphism of degree `0`, `u : L → M`. Let `R = Ker(u)`, which is a graded
`B`-module; there is then a finite number of integers `m_j` (`1 ≤ j ≤ r`) such that for each integer `i`, `R_i` is the
kernel of a surjective homomorphism `⨁_{1 ≤ j ≤ r} B_{i + m_j} → M_i`; one concludes then from the hypothesis on the
`M_i` and the `B_i` that `R_i` is a `B_0`-module of finite type *(Bourbaki, Alg. comm., chap. I, §2, n° 8, lemma 9)*. To
prove that `R` is a `B`-module of finite type, note that by virtue of the flatness hypothesis and of `(0_I, 6.1.2)`, the
sequence

```text
  0 → R ⊗_A k(𝔮) → L ⊗_A k(𝔮) → M ⊗_A k(𝔮) → 0
```

is exact, and the hypothesis therefore entails *(Bourbaki, loc. cit.)* that `R ⊗_A k(𝔮)` is a `(B ⊗_A k(𝔮))`-module of
finite type; it therefore suffices to apply lemma `(11.2.9.3)` to `R`.

*III) Reduction to the case where the transition homomorphisms `φ_{μλ} : A_λ → A_μ` (for `λ ≤ μ`) are injective.* — Let
`A'_λ` be the image of `A_λ` under the canonical homomorphism `φ_λ : A_λ → A`; it is clear that the `A'_λ` form an
inductive system of Noetherian sub-rings of `A`, whose inductive limit is `A`, and the transition homomorphisms
`A'_λ → A'_μ` (for `λ ≤ μ`) are injective. Set `B'_λ = B_0 ⊗_{A_0} A'_λ`, `𝔍'_λ = 𝔍_0 B'_λ`,
`M'_λ = M_0 ⊗_{A_0} A'_λ = M_λ ⊗_{A_λ} A'_λ`; one has again `B = lim B'_λ`, `M = lim M'_λ`. Suppose that one has proved
that there exists a `λ` such that, for `μ ≥ λ`, `gr_{𝔍'_μ}^•(M'_μ)` is a flat `A'_μ`-module. Let `𝔞_λ` be the kernel of
the homomorphism `φ_λ`, which is therefore an ideal of finite type of the Noetherian ring `A_λ`. It follows from the
definition of the inductive limit that there exists an index `μ ≥ λ` such that `φ_{μλ}(𝔞_λ) = 0`, in other words the
homomorphism `φ_μ` factorizes as `A_λ → A'_λ → A_μ`, and one may write `B_μ = B'_λ ⊗_{A'_λ} A_μ`, `𝔍_μ = 𝔍'_λ B_μ` and
`M_μ = M'_λ ⊗_{A'_λ} A_μ`; one therefore deduces from `(11.2.9.2)` that `gr_{𝔍_μ}^•(M_μ)` is a flat `A_μ`-module.

*IV) Reduction to the case where `B_0 = A_0[T_1, …, T_n]` and `gr_{𝔍_0}^•(B_0) = B_0`.* — By virtue of the hypothesis,
there is a system `(t_i)_{1 ≤ i ≤ n}` of generators of the `A_0`-algebra of finite type `B_0`, such that the `t_i` for
`i ≤ m` generate the ideal `𝔍_0` of `B_0`. Set `B'_0 = A_0[T_1, …, T_n]`,

<!-- original page 129 -->

a polynomial algebra (hence Noetherian), and let `𝔍'_0` be the ideal of `B'_0` generated by the `T_i` of index `i ≤ m`;
one then has a surjective `A_0`-homomorphism `u_0 : B'_0 → B_0` transforming each `T_i` into `t_i` (`1 ≤ i ≤ n`), hence
such that `u_0(𝔍'_0) = 𝔍_0`; this homomorphism permits one to consider `M_0` as a `B'_0`-module of finite type. One then
sets `B'_λ = B'_0 ⊗_{A_0} A_λ = A_λ[T_1, …, T_n]`, `𝔍'_λ = 𝔍'_0 B'_λ`, `B' = B'_0 ⊗_{A_0} A = A[T_1, …, T_n]`,
`𝔍' = 𝔍'_0 B'`, so that `𝔍'` is the ideal of `B'` generated by the `T_i` of index `i ≤ m`; moreover, it is clear that
for every integer `k ≥ 0`, one has `𝔍'^k M = 𝔍^k M` and `𝔍'^k_λ M_λ = 𝔍^k_λ M_λ` for every `λ`; hence
`gr_{𝔍'}^•(M) = gr_𝔍^•(M)` as an `A`-module and `gr_{𝔍'_λ}^•(M_λ) = gr_{𝔍_λ}^•(M_λ)` as an `A_λ`-module; one may
therefore substitute `B'`, `B'_λ`, `𝔍'`, `𝔍'_λ` for `B`, `B_λ`, `𝔍`, `𝔍_λ` respectively in the proof; one will note in
addition that by construction `gr_{𝔍'_0}^•(B'_0)` identifies with `B'_0` and `gr_{𝔍'_λ}^•(B'_λ)` with `B'_λ`.

*V) Proof that `gr_𝔍^•(M)` is a `gr_𝔍^•(B)`-module of finite presentation.* — We therefore suppose from now on `A_0` and
the `A_λ` Noetherian, the transition homomorphisms `A_λ → A_μ` injective, `B_0 = A_0[T_1, …, T_n]`, `𝔍_0` being
generated by the `T_i` of index `i ≤ m`; the ring `C_0 = gr_{𝔍_0}^•(B_0)` therefore identifies with `B_0` and
`C = gr_𝔍^•(B)` identifies with `B`; we shall in the sequel use only first of all the fact that `C = C_0 ⊗_{A_0} A`.

We shall need the following variant of `(6.9.3)`:

**Lemma (11.2.9.5).**

<!-- label: IV.11.2.9.5 -->

*Let `A_0` be a Noetherian ring, `B_0` an `A_0`-algebra of finite type, `𝔍_0` an ideal of `B_0`, `M_0` a `B_0`-module of
finite type. There exists then a sequence `(S_{0i})_{1 ≤ i ≤ m}` of sub-schemes of `S_0 = Spec(A_0)` having the
following properties:*

*1° The spaces underlying the `S_{0i}` are pairwise disjoint and form a covering of `S_0`.*

*2° For each `i`, the set `S_{0i}` is open in `⋃_{j ≥ i} S_{0j}`.*

*3° Each scheme `S_{0i}` is affine.*

*4° If `A_{0i}` is the ring of `S_{0i}` and if one sets `B_{0i} = B_0 ⊗_{A_0} A_{0i}`, `𝔍_{0i} = 𝔍_0 B_{0i}`, then
`gr_{𝔍_{0i}}^•(M_0 ⊗_{A_0} A_{0i})` is a flat `A_{0i}`-module.*

One proceeds as in `(6.9.3)` by Noetherian induction, supposing the lemma true when one replaces in it `A_0` by
`A'_0 = A_0/𝔞_0`, where the ideal `𝔞_0` is such that `V(𝔞_0) ≠ S_0`, `B_0` by `B'_0 = B_0 ⊗_{A_0} A'_0`, `𝔍_0` by
`𝔍'_0 = 𝔍_0 B'_0` and `M_0` by `M_0 ⊗_{A_0} A'_0`. One considers the nilradical `𝔑_0` of `A_0`, and it evidently
suffices to prove the lemma replacing `A_0` by `A_0/𝔑_0` and `B_0`, `𝔍_0`, `M_0` by the corresponding objects as above.
In other words, one may suppose that `A_0` is reduced; on the other hand, `gr_{𝔍_0}^•(B_0)` is an `A_0`-algebra of
finite type and `gr_{𝔍_0}^•(M_0)` a `gr_{𝔍_0}^•(B_0)`-module of finite type; by virtue of the generic flatness theorem
`(6.9.1)`, there exists an open set `D(t_0) ⊂ S_0` such that if one sets `A_{01} = (A_0)_{t_0}`,
`gr_{𝔍_0}^•(M_0) ⊗_{A_0} A_{01}` is a flat `A_{01}`-module; but since `A_{01}` is a flat `A_0`-module,
`gr_{𝔍_0}^•(M_0) ⊗_{A_0} A_{01}` identifies with `gr_{𝔍_{01}}^•(M_0 ⊗_{A_0} A_{01})`, where
`B_{01} = B_0 ⊗_{A_0} A_{01}` and `𝔍_{01} = 𝔍_0 B_{01}`. The complement of `D(t_0)` in `S_0` is then of the form
`V(𝔞_0)`, and one concludes by applying the Noetherian induction hypothesis.

Let us apply this lemma to the present situation, keeping the same notation; set `U_{0i} = ⋃_{j ≥ i} S_{0j}`, which is a
quasi-compact open set of `S_0`. There is therefore a finite family `(t_{ik})_{1 ≤ i ≤ m, 1 ≤ k ≤ n_i}` of elements of
`A_0` such that for each `i`, `U_{0i}` is the union of the `D(t_{ik})` (`1 ≤ k ≤ n_i`).

<!-- original page 130 -->

The `C_0`-module `gr_{𝔍_0}^•(M_0)` is generated by a finite number of homogeneous elements of degree `i`, so that there
is an epimorphism of graded `C_0`-modules `u_0 : C_0^r → gr_{𝔍_0}^•(M_0)`. Since `C = C_0 ⊗_{A_0} A` and the canonical
homomorphism `gr_{𝔍_0}^•(M_0) ⊗_{A_0} A → gr_𝔍^•(M)` is surjective, one deduces therefore from `u_0` an epimorphism of
graded `C`-modules

```text
  u : C^r → gr_{𝔍_0}^•(M_0) ⊗_{A_0} A → gr_𝔍^•(M),
```

and everything boils down to seeing that the graded `C`-module `Q = Ker(u)` is of finite type.

**Lemma (11.2.9.6).**

<!-- label: IV.11.2.9.6 -->

*Under the preceding hypotheses, let `𝔄_0` be an ideal of `A_0`; set `A'_0 = A_0/𝔄_0`,
`B'_0 = B_0 ⊗_{A_0} A'_0 = B_0/𝔄_0 B_0`, `𝔍'_0 = 𝔍_0 B'_0`, `𝔄 = 𝔄_0 A`, `A' = A/𝔄`, and suppose in addition that
`gr_{𝔍'_0}^•(M_0 ⊗_{A_0} A'_0)` is a flat `A'_0`-module. Then there exists a finite number of elements `q_h`
(`1 ≤ h ≤ s`) of `Q` such that, for every prime ideal `𝔭 ⊃ 𝔄 B` of `B`, the canonical images of the `q_h` in `Q_𝔭`
generate the `C_𝔭`-module `Q_𝔭`.*

Suppose this lemma proved, and note that one may again apply it replacing `A_0` by `(A_0)_{t_0}`, `B_0`, `𝔍_0`, `M_0`,
`A_λ` and `A` by the corresponding objects `(B_0)_{t_0}`, `(𝔍_0)_{t_0}`, `(M_0)_{t_0}`, `(A_λ)_{t_0}` and `A_{t_0}`, for
any `t_0 ∈ A_0`, since `(A_0)_{t_0}` is a flat `A_0`-module. One will then apply this lemma replacing `A_0` successively
by each of the rings `(A_0)_{t_{ik}}`, `𝔄_0` being replaced by the ideal `𝔄_{ik}` defining the closed sub-scheme of
`D(t_{ik})` induced by `S_{0i}` on the open set `S_{0i} ∩ D(t_{ik})` of `S_{0i}`. Since the flatness hypothesis of
`(11.2.9.6)` is verified in each of these cases by reason of `(11.2.9.5)`, one obtains in this way for each pair
`(i, k)` a finite family `(q_{ikh})_{1 ≤ h ≤ l_{ik}}` of elements of `Q_{t_{ik}}` whose images in `Q_{𝔭_{ik}}` generate
this `C_{𝔭_{ik}}`-module, for every prime ideal `𝔭_{ik}` of `B_{t_{ik}}` containing `𝔄_{ik} B_{t_{ik}}`. One may write,
for a suitable integer `d > 0`, `q_{ikh} = b_{ikh}/t_{ik}^d` for all the indices `i`, `k`, `h`, with `b_{ikh} ∈ Q`.
Since the `S_{0i}` cover `S_0`, every prime ideal `𝔭` of `B` is such that its image in `S_0` belongs to some set
`S_{0i} ∩ D(t_{ik})`, hence the image `𝔭_{ik}` of `𝔭` in `B_{t_{ik}}` contains `𝔄_{ik} B_{t_{ik}}`. Since the images of
the `b_{ikh}` (`1 ≤ h ≤ l_{ik}`) in `Q_{𝔭_{ik}} = Q_𝔭` generate this `C_𝔭`-module, one concludes that the `b_{ikh}`
(`1 ≤ i ≤ m`, `1 ≤ k ≤ n_i`, `1 ≤ h ≤ l_{ik}`) generate the `C`-module `Q` *(Bourbaki, Alg. comm., chap. II, §3, n° 3,
th. 1)*.

It remains to prove lemma `(11.2.9.6)`. Set `C' = C ⊗_A A' = C/𝔄 C`, `B' = B ⊗_A A'`, `𝔍' = 𝔍 B'`, `M' = M ⊗_A A'`. By
hypothesis `gr_𝔍^•(M)` is a flat `A`-module, hence `gr_{𝔍'}^•(M')` identifies with `gr_𝔍^•(M) ⊗_A A'` `(11.2.9.2)`, and
one has the exact sequence `(0_I, 6.1.2)`

```text
  (11.2.9.7)    0 → Q ⊗_A A' → C'^r → gr_{𝔍'}^•(M') → 0.
```

Set `C'_0 = C_0 ⊗_{A_0} A'_0 = C_0/𝔄_0 C_0` and consider the epimorphism of graded `C'_0`-modules

```text
  u'_0 = u_0 ⊗ 1_{A'_0} : C'^r_0 → gr_{𝔍_0}^•(M_0) ⊗_{A_0} A'_0 → gr_{𝔍'_0}^•(M_0 ⊗_{A_0} A'_0).
```

Let `Q'_0 = Ker(u'_0)`; using the fact that `gr_{𝔍'_0}^•(M_0 ⊗_{A_0} A'_0)` is a flat `A'_0`-module, one sees that
`gr_{𝔍'_0}^•(M_0 ⊗_{A_0} A'_0) ⊗_{A'_0} A'` identifies with `gr_{𝔍'}^•(M')` `(11.2.9.2)` and one has the exact sequence
`(0_I, 6.1.2)`

```text
  (11.2.9.8)    0 → Q'_0 ⊗_{A'_0} A' → C'^r → gr_{𝔍'}^•(M') → 0,
```

<!-- original page 131 -->

whence, by comparison with `(11.2.9.7)`, an isomorphism of graded `C'`-modules

```text
  Q'_0 ⊗_{A'_0} A' ⥲ Q ⊗_A A'.
```

Since `C'_0` is Noetherian, `Q'_0` is a `C'_0`-module of finite type, hence `Q'_0 ⊗_{A'_0} A'` is a graded `C'`-module
of finite type, and consequently so is `Q ⊗_A A'`; let `q_h` (`1 ≤ h ≤ s`) be homogeneous elements of `Q` whose images
in `Q ⊗_A A'` generate this `C'`-module.

Let us now consider an arbitrary prime ideal `𝔭 ⊃ 𝔄 B` of `B`; one has `C_𝔭 = gr_{𝔍_𝔭}^•(B_𝔭)` by flatness, and
`gr_{𝔍_𝔭}^0(B_𝔭) = B_𝔭/𝔍_𝔭` is reduced to `0` or is a local ring; to prove the lemma, one may evidently confine oneself
to the second case. It is then clear that each of the `(B_𝔭/𝔍_𝔭)`-modules `gr_{𝔍_𝔭}^i(B_𝔭)` is of finite presentation.
On the other hand, for every index `i`, `M/𝔍^i M` identifies with `(M_0/𝔍_0^i M_0) ⊗_{A_0} A`, and is therefore a
`B`-module of finite presentation. By induction on `i`, the hypothesis that `gr_𝔍^•(M)` is a flat `A`-module entails, by
virtue of `(0_I, 6.1.2)`, that `M/𝔍^i M` is a flat `A`-module. The application of `(11.2.6.1)` where one replaces `M_0`
by `M_0/𝔍_0^k M_0` for `k ≥ i` shows that there exists an index `λ_i` such that, for `μ ≥ λ_i`, each of the
`M_μ/𝔍_μ^{i+1} M_μ` is a flat `A_μ`-module, and consequently also `(0_I, 6.1.2)` each of the `gr_{𝔍_μ}^i(M_μ)` is a flat
`A_μ`-module for `k ≤ i`. One deduces consequently from `(11.2.9.2)` that each of the `(B/𝔍)`-modules `gr_𝔍^i(M)` is of
finite presentation, hence `gr_{𝔍_𝔭}^•(M_𝔭)` is a `(B_𝔭/𝔍_𝔭)`-module of finite presentation. Moreover the images of the
`q_h` in `Q_𝔭 ⊗_{B_𝔭} k(𝔭) = (Q ⊗_A A') ⊗_{A'} k(𝔭)` generate this `(C_𝔭 ⊗_{B_𝔭} k(𝔭))`-module (for
`C_𝔭 ⊗_{B_𝔭} k(𝔭) = C_𝔭 ⊗_{A'} k(𝔭)`); since one has the exact sequence

```text
  0 → Q_𝔭 ⊗_{B_𝔭} k(𝔭) → C_𝔭^r ⊗_{B_𝔭} k(𝔭) → gr_{𝔍_𝔭}^•(M_𝔭) ⊗_{B_𝔭} k(𝔭) → 0,
```

one concludes that `gr_{𝔍_𝔭}^•(M_𝔭) ⊗_{B_𝔭} k(𝔭)` is a `(C_𝔭 ⊗_{B_𝔭} k(𝔭))`-module of finite presentation. Applying
lemma `(11.2.9.4)` where `A`, `B`, `M` are replaced respectively by `B_𝔭`, `C_𝔭` and `gr_{𝔍_𝔭}^•(M_𝔭)`, one concludes
that `Q_𝔭` is a `C_𝔭`-module of finite type. Now using Nakayama's lemma (and the fact that `C^0 = B`), one deduces that
the images of the `q_h` in `Q_𝔭` generate this `C_𝔭`-module. This finishes the proof of lemma `(11.2.9.6)` and of the
fact that `gr_𝔍^•(M)` is a `C`-module of finite presentation.

*VI) End of the proof.* — Set, to abbreviate, `C_λ = C_0 ⊗_{A_0} A_λ` (equal in fact to `B_λ`), `N_λ = gr_{𝔍_λ}^•(M_λ)`
and `N = gr_𝔍^•(M)`. Note first that for each integer `k`, `𝔍^k M` identifies with `lim 𝔍_λ^k M_λ` by exactness of the
functor `lim`, the image of `𝔍_λ^k M_λ` in `M_μ` for `λ ≤ μ` (resp. in `M`) generating `𝔍_μ^k M_μ` (resp. `𝔍^k M`);
using again the exactness of `lim`, one concludes that `N` identifies canonically with `lim N_λ`. Making this
identification, we shall first prove that:

*(11.2.9.9) For `λ` sufficiently large, the canonical homomorphism `v_λ : N_λ ⊗_{A_λ} A → N` is bijective.*

Since the `C_λ` are Noetherian and `N_λ` a `C_λ`-module of finite type, the `C`-modules `N_λ ⊗_{A_λ} A` are of finite
presentation and form a filtered inductive system, whose inductive limit identifies canonically with `N` by virtue of
the fact that `lim` commutes with tensor products. Moreover, the transition homomorphisms
`v_{μλ} : N_λ ⊗_{A_λ} A → N_μ ⊗_{A_μ} A`

<!-- original page 132 -->

for `λ ≤ μ` and the homomorphisms `v_λ` are surjective. For a fixed `λ`, let us consider the sub-`C`-modules
`Ker(v_{μλ}) = N'_μ` of `N_λ ⊗_{A_λ} A`; by definition of the inductive limit, they form a filtered increasing family of
sub-`C`-modules of `Ker(v_λ)`, whose union is `Ker(v_λ)`; but we have seen in V) that `N` is a `C`-module of finite
presentation, hence *(Bourbaki, Alg. comm., chap. I, §2, n° 8, lemma 9)* `Ker(v_λ)` is a `C`-module of finite type;
there exists consequently an index `μ ≥ λ` such that `N'_μ = Ker(v_λ)`, which signifies (in view of the fact that
`v_{μλ}` is surjective) that `v_μ` is injective; since it is surjective, this proves `(11.2.9.9)`.

Up to replacing `A_0` and `M_0` by `A_λ` and `M_λ` for `λ` sufficiently large, one may therefore suppose that the
canonical homomorphism `v_λ` is bijective for every `λ`. Set then `P_λ = N_0 ⊗_{C_0} C_λ = N_0 ⊗_{A_0} A_λ`, so that
`N = lim P_λ`. Since `C_0` is an `A_0`-algebra of finite presentation and `P_0` a `C_0`-module of finite presentation,
one may apply to `C` and `N` the result of `(11.2.6.1)`, and one sees therefore that there exists an index `λ` such
that, for `μ ≥ λ`, `P_μ` is a flat `A_μ`-module. Now, for `μ ≥ λ`, one has a commutative diagram

```text
  P_μ  ──w_μ──→  N
   │            ‖
   ↓            ‖
  N_μ  ─v_μ──→  N
```

where it results from the definitions that `w_μ` is surjective. Since, by virtue of III), the homomorphisms `A_μ → A`
are injective and `P_μ` is a flat `A_μ`-module, the canonical homomorphism `P_μ → N = P_μ ⊗_{A_μ} A` is injective; one
therefore concludes from the preceding commutative diagram that `w_μ` is also injective, hence bijective, and
consequently `N_μ` is a flat `A_μ`-module for `μ ≥ λ`, which finishes the proof of `(11.2.9)`.

**Remark (11.2.10).**

<!-- label: IV.11.2.10 -->

We do not know whether the generalization of `(11.2.6, (i))` analogous to Raynaud's theorem is valid.

### 11.3. Application to elimination of Noetherian hypotheses

**Theorem (11.3.1).**

<!-- label: IV.11.3.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation.
Then the set `U` of points `x ∈ X` such that `ℱ` is `f`-flat at the point `x` is open in `X`. Moreover, if
`Supp(ℱ) = X`, `f | U` is an open morphism.*

The second assertion has already been proved `(2.4.6)` and has been inserted only for the record.

The question being local on `X` and `Y`, one may suppose that `X` and `Y` are affine, and that `f` is a morphism of
finite presentation. Let `x ∈ X` be a point such that `ℱ` is `f`-flat at the point `x`. Applying `(11.2.7)`, one may
suppose that `X = X_0 ×_{Y_0} Y`, `f = f_0 ×_S 1`, `ℱ = ℱ_0 ⊗_{𝒪_{Y_0}} 𝒪_Y`, where `Y_0` is Noetherian,
`f_0 : X_0 → Y_0` a morphism of finite type, `ℱ_0` a coherent `𝒪_{X_0}`-Module; moreover, if `x_0` is the canonical
projection of `x` in `X_0`, one may suppose that `ℱ_0` is `f_0`-flat at the point `x_0`. Then, by virtue of `(11.1.1)`,
the set `U_0` of points of `X_0` where `ℱ_0` is `f_0`-flat is a neighbourhood of `x_0`; hence `ℱ` is `f`-flat at the
points of the inverse image of `U_0` in `X` `(2.1.4)`, and this proves that `U` is a neighbourhood of `x`.

<!-- original page 133 -->

**Corollary (11.3.2).**

<!-- label: IV.11.3.2 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite
presentation. Then the set `U` of `y ∈ Y` such that, for every generization `y'` of `y`, `ℱ` is `(g ∘ f)`-flat at all
points of `f⁻¹(y')` (i.e. such that `ℱ ⊗_Y Spec(𝒪_{Y, y'})` is flat relative to the morphism
`X ×_Y Spec(𝒪_{Y, y'}) → Z`) is open in `Y`.*

The same reasoning as in `(11.1.5)` shows that if `V` is the set of `x ∈ X` where `ℱ` is `(g ∘ f)`-flat, `U` is the set
of `y ∈ Y` such that every generization of `y` belongs to `E = Y − f(X − V)`. Since `g ∘ f` is of finite presentation,
`V` is open in `X` by virtue of `(11.3.1)`, hence ind-constructible `(1.9.6)`, and consequently `X − V` is
pro-constructible; but since `f` is quasi-compact, `f(X − V)` is pro-constructible in `Y` `(1.9.5, (vii))`, and
consequently `E` is ind-constructible in `Y`. It then follows from `(1.10.1)` that `U` is the interior of `E`, hence
open in `Y`.

**Corollary (11.3.3).**

<!-- label: IV.11.3.3 -->

*Let `A` be a ring, `B` an `A`-algebra of finite presentation, `C` a `B`-algebra of finite presentation, `M` a
`C`-module of finite presentation. Then the set of `𝔮 ∈ Spec(B)` such that `M_𝔮` is a flat `A`-module is open in
`Spec(B)`.*

**Proposition (11.3.4).**

<!-- label: IV.11.3.4 -->

*Let `f : X → S` be a morphism locally of finite presentation, `𝔍` a quasi-coherent Ideal of finite type of `𝒪_X`, `Y`
the closed sub-prescheme of `X` defined by `𝔍`, `ℱ` an `𝒪_X`-Module of finite presentation. Suppose that `gr_𝔍^•(ℱ)` is
`f`-flat. Under these conditions:*

*(i) `ℱ` is `f`-flat at the points of `Y`.*

*(ii) If `gr_𝔍^•(𝒪_X)` is `f`-flat, `gr_𝔍^•(𝒪_X)` is an `(𝒪_X/𝔍)`-Algebra of finite presentation and `gr_𝔍^•(ℱ)` is a
`(gr_𝔍^•(𝒪_X))`-Module of finite presentation.*

*(iii) Suppose `gr_𝔍^•(𝒪_X)` `f`-flat (which entails that `𝒪_X/𝔍` is `f`-flat). Then the set `W` of `y ∈ Y` such that
`(gr_𝔍^•(ℱ))_y` is a flat `𝒪_{X, y}`-module is open in `Y`.*

*(iv) Suppose `gr_𝔍^•(𝒪_X)` `f`-flat. Let `S' → S` be an arbitrary morphism; let `X' = X ×_S S'`, `p : X' → X` the
canonical projection, `Y' = p⁻¹(Y) = Y ×_S S'` the closed sub-prescheme of `X'` defined by `𝔍' = p*(𝔍) 𝒪_{X'}`,
`ℱ' = p*(ℱ) = ℱ ⊗_{𝒪_S} 𝒪_{S'}`; then, if `W' = p⁻¹(W)`, one has `gr_{𝔍'}^•(ℱ') | W' = p*(gr_𝔍^•(ℱ)) | W'`, and
`gr_{𝔍'}^•(ℱ')` is a flat `(𝒪_{X'}/𝔍')`-Module at the points of `W'`.*

The questions being local on `X` and `S`, one may suppose that `S = Spec(A)` and `X = Spec(B)` are affine, `B` being an
`A`-algebra of finite presentation, and `ℱ = M̃`, where `M` is a `B`-module of finite presentation, `𝔍 = 𝔍̃`, where `𝔍`
is an ideal of finite type of `B`; by virtue of `(8.9.1)` and `(8.5.11)`, there exists a Noetherian sub-ring `A_0` of
`A`, an `A_0`-algebra of finite type `B_0` such that `B = B_0 ⊗_{A_0} A`, an ideal `𝔍_0` of `B_0` such that `𝔍 = 𝔍_0 B`,
a `B_0`-module of finite type `M_0` such that `M = M_0 ⊗_{A_0} A = M_0 ⊗_{B_0} B`. Moreover, `A` is the inductive limit
of its sub-`A_0`-algebras of finite type `A_λ`; one sets `B_λ = B_0 ⊗_{A_0} A_λ`,
`M_λ = M_0 ⊗_{A_0} A_λ = M_0 ⊗_{B_0} B_λ`, `𝔍_λ = 𝔍_0 B_λ`, so that `B = lim B_λ`, `M = lim M_λ`. This being so, by
hypothesis `gr_𝔍^•(M)` is a flat `A`-module; hence it follows from `(11.2.9)` that there exists a `λ` such that
`gr_{𝔍_λ}^•(M_λ)` is a flat `A_λ`-module. To prove that `ℱ` is `f`-flat at the points of `Y`, one may therefore confine
oneself to the case where `S` is Noetherian; but then `(0_I, 6.1.2)`, applied by induction on `n`, proves that the
`ℱ/𝔍^{n+1} ℱ` are `f`-flat, and one concludes by `(0_III, 10.2.6)`.

The proof of (ii) reduces in the same way to the case where `S` is Noetherian,

<!-- original page 134 -->

using `(11.2.9)`; the conclusion is then evident, `gr_𝔍^•(B)` being in this case a `(B/𝔍)`-algebra of finite type and
`gr_𝔍^•(M)` a `gr_𝔍^•(B)`-module of finite type.

To prove (iii), one reduces as in (i) to the case where `S` and `X` are affine; with the same notation, one may suppose,
by virtue of `(11.2.9)`, that `gr_{𝔍_λ}^•(B_λ)` and `gr_{𝔍_λ}^•(M_λ)` are flat `A_λ`-modules and that one has
`gr_𝔍^•(B) = gr_{𝔍_λ}^•(B_λ) ⊗_{A_λ} A` and `gr_𝔍^•(M) = gr_{𝔍_λ}^•(M_λ) ⊗_{A_λ} A`. Consequently `gr_𝔍^•(B)` is a
`(B/𝔍)`-algebra of finite presentation and `gr_𝔍^•(M)` a `gr_𝔍^•(B)`-module of finite presentation. If `W_m` is the set
of `𝔭 ∈ Spec(B/𝔍)` such that `gr_𝔍^m(M)_𝔭` is a flat `(B/𝔍)`-module, `W_m` is open in `Spec(B/𝔍)` `(11.3.1)` and one has
`W = ⋂_m W_m`, hence `W` is stable under generization. Assertion (iii) then follows from `(11.3.2)` applied by taking
`X = Spec(gr_𝔍^•(B))`, `Y = Z = Spec(B/𝔍)` and `ℱ = (gr_𝔍^•(M))~`.

Finally, (iv) follows at once from `(11.2.9.2)`.

Generalizing the definition of `(6.10.1)`, one says that for a prescheme `X`, a closed sub-prescheme `Y` of `X` defined
by a quasi-coherent Ideal `𝔍` of `𝒪_X`, and a quasi-coherent `𝒪_X`-Module `ℱ`, `ℱ` is **normally flat along `Y` at a
point** `y` if `(gr_𝔍^•(ℱ))_y` is a flat `𝒪_{Y, y}`-module. One says that `ℱ` is **normally flat along `Y`** if it is so
at every point of `Y`.

**Corollary (11.3.5).**

<!-- label: IV.11.3.5 -->

*Under the general hypotheses of `(11.3.4)`, suppose that `gr_𝔍^•(𝒪_X)` and `gr_𝔍^•(ℱ)` are `f`-flat. Then the set `W`
of `y ∈ Y` such that `ℱ` is normally flat along `Y` at the point `y` is open in `Y`, and (with the notation of
`(11.3.4, (iv))`) `ℱ'` is normally flat along `Y'` at all points of `W' = p⁻¹(W)`.*

**Proposition (11.3.6).**

<!-- label: IV.11.3.6 -->

*The notation being that of `(8.5.1)` and `(8.8.1)`, suppose `S_α` quasi-compact, `X_α` of finite presentation over
`S_α`, `Y_α` a closed sub-prescheme of `X_α` defined by a quasi-coherent Ideal `𝔍_α` of finite type of `𝒪_{X_α}` such
that `gr_{𝔍_α}^•(𝒪_{X_α})` is flat over `S_α`; finally suppose that `ℱ_α` is an `𝒪_{X_α}`-Module of finite presentation.
For `ℱ` to be normally flat along `Y`, it is necessary and sufficient that there exist `λ` such that `ℱ_λ` is normally
flat along `Y_λ`.*

Note that `Y` (resp. `Y_λ`) is the closed sub-prescheme of `X` (resp. `X_λ`) defined by `𝔍 = 𝔍_α 𝒪_X` (resp.
`𝔍_λ = 𝔍_α 𝒪_{X_λ}`); by virtue of the hypothesis and of `(11.2.9.2)`, one has
`gr_𝔍^•(𝒪_X) = gr_{𝔍_α}^•(𝒪_{X_α}) ⊗_{𝒪_{S_α}} 𝒪_S` and `gr_{𝔍_λ}^•(𝒪_{X_λ}) = gr_{𝔍_α}^•(𝒪_{X_α}) ⊗_{𝒪_{S_α}} 𝒪_{S_λ}`
for `λ ≥ α`, and `gr_𝔍^•(𝒪_X)` (resp. `gr_{𝔍_λ}^•(𝒪_{X_λ})`) is flat over `S` (resp. `S_λ`), which entails that `Y` is
flat over `S` (resp. `Y_λ` flat over `S_λ`). If `ℱ_λ` is normally flat along `Y_λ`, `gr_{𝔍_λ}^•(ℱ_λ) | Y_λ` is flat over
`Y_λ`, hence also over `S_λ`, and since `(gr_{𝔍_λ}^•(ℱ_λ))_{x_λ} = 0` for `x_λ ∉ Y_λ`, `gr_{𝔍_λ}^•(ℱ_λ)` is flat over
`S_λ`. One concludes `(11.2.9.2)` that `gr_𝔍^•(ℱ) = gr_{𝔍_λ}^•(ℱ_λ) ⊗_{𝒪_{S_λ}} 𝒪_S`, hence `ℱ` is normally flat along
`Y`. To prove the converse, one may suppose that `S_α` and `X_α` are affine and adopt the notation of `(11.2.9)`; since
`gr_𝔍^•(B)` is a flat `A`-module, so is `gr_𝔍^•(M)`, hence, by virtue of `(11.2.9)`, there exists `λ ≥ α` such that
`gr_{𝔍_λ}^•(M_λ)` is a flat `A_λ`-module, whence `gr_𝔍^•(M) = gr_{𝔍_λ}^•(M_λ) ⊗_{A_λ} A`. Moreover `(11.3.4, (ii))`,
`gr_{𝔍_λ}^•(M_λ)` is a `gr_{𝔍_λ}^•(B_λ)`-module of finite presentation and `gr_{𝔍_λ}^•(B_λ)` a `(B_λ/𝔍_λ)`-algebra of
finite presentation. The conclusion then follows from `(11.2.6)`.

<!-- original page 135 -->

**Proposition (11.3.7).**

<!-- label: IV.11.3.7 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ`, `ℱ'` two quasi-coherent `𝒪_X`-Modules of finite
presentation, `u : ℱ' → ℱ` an `𝒪_X`-homomorphism, `x` a point of `X` and `y = f(x)`; suppose that `ℱ` is `f`-flat at the
point `x`. The following conditions are then equivalent:*

*a) One has `(Ker u)_x = 0` and `Coker u` is an `𝒪_X`-Module `f`-flat at the point `x`.*

*b) The homomorphism `(u ⊗ 1)_x : (ℱ' ⊗_{𝒪_Y} k(y))_x → (ℱ ⊗_{𝒪_Y} k(y))_x` is injective.*

*If moreover `ℱ'` is `f`-flat, the set of points `x` verifying the preceding equivalent conditions is open in `X`.*

Condition a) entails b) by virtue of `(0_I, 6.1.2)`, without hypothesis on `ℱ'`. To prove the converse, one may confine
oneself to the case where `X` and `Y` are affine, then, by virtue of `(8.9.1)` and `(11.2.7)`, suppose that one has
`X = X_0 ×_{Y_0} Y`, `f = f_0 × 1`, `ℱ = ℱ_0 ⊗_{𝒪_{Y_0}} 𝒪_Y`, `ℱ' = ℱ'_0 ⊗_{𝒪_{Y_0}} 𝒪_Y`, `u = u_0 ⊗ 1_Y`, where `Y_0`
is Noetherian, `f_0 : X_0 → Y_0` a morphism of finite type, `ℱ_0`, `ℱ'_0` two coherent `𝒪_{X_0}`-Modules,
`u_0 : ℱ'_0 → ℱ_0` a homomorphism; moreover, if `x_0` is the projection of `x` in `X_0`, one may suppose that `ℱ_0` is
`f_0`-flat at the point `x_0`. Set `y_0 = f_0(x_0)`; by virtue of the transitivity of fibres `(I, 3.6.4)`, the
projection morphism `f⁻¹(y) → f_0⁻¹(y_0)` is faithfully flat `(2.2.13)`, and since
`(u ⊗ 1)_x = ((u_0 ⊗ 1)_{x_0}) ⊗ 1_{k(y)}`, the hypothesis that `(u ⊗ 1)_x` is injective entails that the same is true
of `(u_0 ⊗ 1)_{x_0}` `(2.2.7)`. Now this entails, by `(0_III, 10.2.4)` applied to the local Noetherian rings `𝒪_{y_0}`
and `𝒪_{x_0}` and to the `𝒪_{y_0}`-modules `(ℱ'_0)_{x_0}` and `(ℱ_0)_{x_0}` (of which the second is flat over
`𝒪_{y_0}`), that one has `(Ker u_0)_{x_0} = 0` and that `Coker u_0` is `f_0`-flat at the point `x_0`. One deduces from
this first of all that `Coker u` is `f`-flat at the point `x` `(2.1.4)`; by virtue of the right exactness of the tensor
product, one has moreover `Coker u = (Coker u_0) ⊗_{𝒪_Y} 𝒪_Y`; applying then `(0_I, 6.1.2)` to the sequence (exact by
hypothesis)

```text
  0 → Ker u_0 → ℱ'_0 → ℱ_0 → Coker u_0 → 0,
```

one deduces from this that `u_x` is an injective homomorphism.

Finally, it follows from `(11.1.2)` that the set `U_0` of points `x_0 ∈ X_0` such that the morphism `(u_0 ⊗ 1)_{x_0}` is
injective is open; by flatness one deduces from this that for every `x ∈ X` above `x_0 ∈ U_0` the morphism `(u ⊗ 1)_x`
is injective, hence the set of these points contains the inverse image `U` of `U_0` in `X` and is consequently a
neighbourhood of `x`, which finishes the proof.

**Theorem (11.3.8).**

<!-- label: IV.11.3.8 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation,
`(g_i)_{1 ≤ i ≤ n}` a sequence of sections of `𝒪_X` over `X`; set `ℱ_i = ℱ/(∑_{j ≤ i} g_j ℱ)` for `0 ≤ i ≤ n` (with
`ℱ_0 = ℱ`). Let `x` be a point of `X`, `y = f(x)`, and set `X_y = f⁻¹(y) = X ×_Y Spec(k(y))`, `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)`,
which is an `𝒪_{X_y}`-Module. Suppose that the `(g_i)_x` belong to the maximal ideal `𝔪_x`. The following conditions are
equivalent:*

*a) The sequence `((g_i)_x)` is `ℱ_y`-regular and the `ℱ_i` (`0 ≤ i ≤ n`) are `f`-flat at the point `x`.*

*b) The sequence `((g_i)_x)` is `ℱ_x`-regular and `ℱ_n` is `f`-flat at the point `x`.*

*b') There exists a neighbourhood `U` of `x` such that the sequence `(g_i | U)` is `(ℱ | U)`-quasi-regular, and `ℱ_n` is
`f`-flat at the point `x`.*

<!-- original page 136 -->

*c) `ℱ` is `f`-flat at the point `x`, and the sequence `((g_i ⊗ 1)_x)` of elements of `𝒪_{X_y, x}` images of the
`(g_i)_x` is `(ℱ_y)_x`-regular.*

*d) `ℱ` is `f`-flat at the point `x`, and for every morphism `Y' → Y` and every point `x' ∈ X' = X ×_Y Y'` above `x`, if
one sets `ℱ' = ℱ ⊗_Y Y'`, the sequence `(g_i ⊗ 1)_{x'}` of elements of `𝒪_{X', x'}` is `ℱ'_{x'}`-regular.*

*Moreover the set of `x ∈ X` verifying these conditions is open in the set `Z` of `x` such that `g_i(x) = 0` for every
`i`.*

The fact that a) entails d) follows at once from `(0, 15.1.15)`, and c) is a particular case of d); moreover, a) implies
b) trivially. Let us show that b) or c) entails a). The `ℱ_i` are of finite presentation; the fact that c) implies a)
then follows at once from `(11.3.7)` by induction on `n`, and this also shows that the set of `x ∈ X` verifying c) is
open in `Z`. To show that b) entails a), one is at once reduced, by induction on `n`, to the case `n = 1`; we shall
write `g` instead of `g_1`. The question being local on `X` and `Y`, one may suppose `Y = Spec(A)`, `X = Spec(B)`
affine, `B` being an `A`-algebra of finite presentation, `ℱ = M̃`, where `M` is a `B`-module of finite presentation. One
can then `(8.9.1)` write `B = B_0 ⊗_{A_0} A`, `M = M_0 ⊗_{A_0} A`, where `A_0` is a Noetherian sub-ring of `A`, `B_0` an
`A_0`-algebra of finite type and `M_0` a `B_0`-module of finite type. Moreover `A` is the filtered inductive limit of
its sub-rings `A_λ` which are `A_0`-algebras of finite type (hence Noetherian), and if one sets `B_λ = B_0 ⊗_{A_0} A_λ`,
`M_λ = M_0 ⊗_{A_0} A_λ`, `B_λ` is an `A_λ`-algebra of finite type, `M_λ` a `B_λ`-module of finite type and one has
`B = lim B_λ`, `M = lim M_λ`. There exists therefore an index `λ` and an element `g_λ ∈ B_λ` such that `g = g_λ ⊗ 1`;
returning to geometric notation and setting `Y_λ = Spec(A_λ)`, `X_λ = Spec(B_λ)` and `ℱ_λ = M̃_λ`, it will suffice to
prove that there is a `μ ≥ λ` such that at the point `x_μ ∈ X_μ` projection of `x`, `(g_μ)_{x_μ}` is
`(ℱ_μ)_{x_μ}`-regular and `ℱ_μ/g_μ ℱ_μ` flat over `Y_μ` at the point `x_μ`. One will deduce in effect, by
`(0, 15.1.16)`, that `ℱ_μ` is flat over `Y_μ` at the point `x_μ`, hence `ℱ` flat over `Y` at the point `x`.

The fact that b) entails a) will thus follow from the following proposition:

**Proposition (11.3.9).**

<!-- label: IV.11.3.9 -->

*The general notation and hypotheses being those of `(8.5.1)` and `(8.8.1)`, suppose that `f_α : X_α → Y_α` is a
morphism locally of finite presentation. Let `ℱ_α`, `𝒢_α` be two quasi-coherent `𝒪_{X_α}`-Modules of finite
presentation, `h_α : ℱ_α → 𝒢_α` an `𝒪_{X_α}`-homomorphism, `ℋ_α` its cokernel. Let finally `x` be a point of `X`, `x_λ`
its projection in `X_λ` for `λ ≥ α`. For `h_x` to be injective and `ℋ = Coker h` to be `f`-flat at the point `x`, it is
necessary and sufficient that there exist `λ ≥ α` such that `(h_λ)_{x_λ}` is injective and `ℋ_λ = Coker h_λ` is
`f_λ`-flat at the point `x_λ`. Moreover, the set of `x ∈ X` having the preceding properties is open in `X`.*

Recall that by virtue of the right exactness of the tensor product, one has `ℋ_μ = v^*_{μλ}(ℋ_λ)` for `λ ≤ μ` and
`ℋ = v_λ^*(ℋ_λ)`, which justifies the notation.

The sufficiency of the condition comes from the fact that, if the sequence

```text
  0 → ℱ_λ → 𝒢_λ → ℋ_λ → 0
```

is exact and `(𝒢_λ)_{x_λ}` a flat `𝒪_{Y_λ, y_λ}`-module, `ℋ_x` is a flat `𝒪_{Y, y}`-module by base change `(2.1.4)` and
the sequence `0 → ℱ_x → 𝒢_x → ℋ_x → 0` is exact `(2.1.8)`. To prove

<!-- original page 137 -->

that the condition is necessary, note that `ℋ` is of finite presentation; the question being local on `X`, one may
suppose `X` and `Y` affine, and, by virtue of `(11.3.1)`, suppose that `ℋ` is `f`-flat. Let us now note the

**Lemma (11.3.9.1).**

<!-- label: IV.11.3.9.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `𝒢`, `ℋ` two quasi-coherent `𝒪_X`-Modules of finite
presentation such that `ℋ` is `f`-flat, `p : 𝒢 → ℋ` a surjective homomorphism. Then `Ker(p)` is an `𝒪_X`-Module of
finite presentation.*

Indeed, one may suppose `X`, `Y` affine, and that there exists a morphism `Y → Y_0` where `Y_0` is Noetherian, a
morphism `f_0 : X_0 → Y_0` of finite type such that `X = X_0 ×_{Y_0} Y`, `f = (f_0)_{(Y)}`, two coherent
`𝒪_{X_0}`-Modules `𝒢_0`, `ℋ_0` and a homomorphism `p_0 : 𝒢_0 → ℋ_0` such that `𝒢`, `ℋ` and `p` are deduced from `𝒢_0`,
`ℋ_0` and `p_0` by base change `(8.9.1 and 8.5.2)`. Moreover, one may suppose `p_0` surjective `(8.5.7)` and `ℋ_0`
`f_0`-flat `(11.2.7)`. Then, if `𝒦_0 = Ker(p_0)`, `𝒦_0` is a coherent `𝒪_{X_0}`-Module `(0_I, 5.3.4)` and by virtue of
`(0_I, 6.1.2)`, `𝒦 = Ker(p)` is deduced from `𝒦_0` by base change, hence is of finite presentation.

This lemma being proved, set `𝒦 = Ker(𝒢 → ℋ)`, which is therefore of finite presentation. One has a canonical
homomorphism `q : 𝒦 → ℱ`, and by hypothesis `q_x : 𝒦_x → ℱ_x` is an isomorphism; consequently `(0_I, 5.2.7)` there
exists a neighbourhood `U` of `x` such that `q | U` is an isomorphism, and on restricting `X`, one may suppose that the
sequence

```text
  0 → 𝒦 → 𝒢 → ℋ → 0
```

is exact. This being so, it follows from `(11.2.6)` that for `λ` large enough, `ℋ_λ` is a flat `𝒪_{X_λ}`-module; set
`𝒦_λ = Ker(𝒢_λ → ℋ_λ)` and `𝒦'_λ = v^*_λ(𝒦_λ)`. For `μ ≥ λ` it follows from `(0_I, 6.1.2)` that one has
`𝒦_μ = Ker(𝒢_μ → ℋ_μ)` and `𝒦 = v^*_λ(𝒦_λ) = Ker(𝒢 → ℋ) = 𝒦`. One has on the other hand for every `μ ≥ λ` a canonical
homomorphism `q_μ : 𝒦_μ → ℱ_μ`, with `𝒦_μ = v^*_{μλ}(𝒦_λ)` for `λ ≤ μ`, and `q = v_μ^*(q_μ)`. Since `q` is an
isomorphism, it follows from `(8.5.2.4)` and `(11.3.9.1)` that there exists `μ ≥ λ` such that `q_μ` is an isomorphism,
and consequently `u_μ : ℱ_μ → 𝒢_μ` an injective homomorphism.

Let us return to the proof of `(11.3.8)`.

Since the set of `x ∈ X` verifying b) is open in `X`, it is clear that b) entails b'). Let us finally show that b')
entails c). In the first place, `ℱ_n` is `f`-flat in a neighbourhood of `x` `(11.3.1)`, and one may therefore confine
oneself to the case where `U = X` and where `ℱ_n` is `f`-flat. Since by definition `gr_𝔉^•(ℱ)` is isomorphic to
`ℱ_n ⊗_{𝒪_Y} 𝒪_Y[T_1, …, T_n]` `(0, 15.2.2)`, it is `f`-flat, and one concludes by `(11.3.4, (i))` that `ℱ` itself is
`f`-flat in a neighbourhood of `x`. On the other hand, if `(𝔉_y)_x` is the ideal of `𝒪_{X_y, x}` generated by the
`(g_i ⊗ 1)_x`, it follows from `(11.2.9.2)` that, in the diagram

```text
  (ℱ_y)_x[T_1, …, T_n] / ((𝔉_y)_x[T_1, …, T_n])  ──→  gr_{(𝔉_y)_x}^•((ℱ_y)_x)
                ‖                                              ‖
              (gr_𝔉^•(ℱ))_x ⊗_{𝒪_Y} k(y)        ──→        ((gr_𝔉^•(ℱ)) ⊗_{𝒪_Y} k(y))_x
```

<!-- original page 138 -->

the vertical arrows are isomorphisms; since the first row is an isomorphism, so is the second, hence the sequence
`((g_i ⊗ 1)_x)` is `(ℱ_y)_x`-quasi-regular, and consequently also `(ℱ_y)_x`-regular, since `X_y` is locally of finite
type over `k(y)`. Q.E.D.

**Theorem (11.3.10) (fibrewise flatness criterion).**

<!-- label: IV.11.3.10 -->

*Let `S` be a prescheme, `g : X → S`, `h : Y → S` two morphisms, `f : X → Y` an `S`-morphism, `ℱ` a quasi-coherent
`𝒪_X`-Module, `x` a point of `X`, `y = f(x)`, `s = h(y) = g(x)`. Suppose one of the following two hypotheses verified:*

*1° `S`, `X` and `Y` are locally Noetherian and `ℱ` is coherent.*

*2° `g` and `h` are locally of finite presentation and `ℱ` is of finite presentation.*

*Then, with the notation of `(9.4.1)`, if `ℱ_s ≠ 0`, the following conditions are equivalent:*

*a) `ℱ` is `g`-flat at the point `x` and `ℱ_s` is `f_s`-flat at the point `x`.*

*b) `h` is flat at the point `y` and `ℱ` is `f`-flat at the point `x`.*

*Moreover, under hypothesis 2°, the set of `x ∈ X` verifying condition b) is open in `X`.*

The last assertion follows from `(11.3.1)` applied to `𝒪_Y` and the morphism `h` on the one hand, and to `ℱ` and the
morphism `f` (which is locally of finite presentation) on the other.

Since `g = h ∘ f`, it is clear that b) implies a) without supposing 1° or 2° `(2.1.6 and 2.1.4)`. To prove that a)
entails b), one may confine oneself to the case where `S`, `X` and `Y` are affine; under hypothesis 2°, applying
`(11.2.7)`, one reduces to the case where in addition `S` is Noetherian, that is, one may confine oneself to considering
the case where hypothesis 1° is satisfied. Then the assertion is equivalent to the following lemma, which improves
`(0_III, 10.2.5)`:

**Lemma (11.3.10.1).**

<!-- label: IV.11.3.10.1 -->

*Let `ρ : A → B`, `σ : B → C` be local homomorphisms of Noetherian local rings, `k` the residue field of `A`, `M` a
`C`-module `≠ 0` of finite type. The following conditions are equivalent:*

*a) `M` is a flat `A`-module and `M ⊗_A k` is a flat `(B ⊗_A k)`-module.*

*b) `B` is a flat `A`-module and `M` is a flat `B`-module.*

We shall first establish the following more general lemma:

**Lemma (11.3.10.2).**

<!-- label: IV.11.3.10.2 -->

*Let `A` be a commutative ring, `B` a commutative `A`-algebra, `𝔍` an ideal of `A`, `M` a `B`-module. Consider on the
one hand the following conditions:*

*(i) `𝔍` is nilpotent.*

*(ii) `B` is Noetherian and `M` is ideally separated for the `𝔍 B`-preadic topology `(0_III, 10.2.1)`.*

*(iii) `𝔍 B` is contained in the radical of `B`.*

*Consider on the other hand the four properties:*

*a) `M` is a flat `B`-module.*

*b) `B` is a flat `A`-module.*

*c) `M` is a flat `A`-module and `M/𝔍 M` a flat `(B/𝔍 B)`-module.*

*d) `B/𝔍 B` is a flat `(A/𝔍)`-module and for every maximal ideal `𝔪 ⊃ 𝔍 B` of `B` one has `𝔪 M ≠ M`.*

*Then:*

*1° If one of the conditions (i), (ii) is verified, the conjunction of a) and b) implies c), and c) implies a).*

<!-- original page 139 -->

*2° If condition (i) or the conjunction of (ii) and (iii) is verified, the conjunction of c) and d) implies the
conjunction of a) and b).*

*1°* The first assertion is immediate `(0_I, 6.2.1)`. Suppose then c) verified, and let us prove a). Consider the graded
rings `gr_𝔍^•(A)`, `gr_𝔍^•(B)` and the graded module `gr_𝔍^•(M)` (at the same time over `gr_𝔍^•(A)` and `gr_𝔍^•(B)`)
relative to the `𝔍`-preadic filtrations, as well as the canonical surjective maps `(0_III, 10.1.1.2)`

```text
  u : gr_𝔍^0(B) ⊗_{gr_𝔍^0(A)} gr_𝔍^•(A) → gr_𝔍^•(B)
  v : gr_𝔍^0(M) ⊗_{gr_𝔍^0(A)} gr_𝔍^•(A) → gr_𝔍^•(M)
  w : gr_𝔍^0(M) ⊗_{gr_𝔍^0(B)} gr_𝔍^•(B) → gr_𝔍^•(M).
```

It is clear that one has a commutative diagram

```text
  (11.3.10.3)
    gr_𝔍^0(M) ⊗_{gr_𝔍^0(A)} gr_𝔍^•(A)  ──v──→  gr_𝔍^•(M)
                          ↘                      ↗
                    gr_𝔍^0(M) ⊗_{gr_𝔍^0(B)} gr_𝔍^•(B)
```

Hypothesis c) entails that `v` is bijective `(0_III, 10.2.1)`; since the two other maps of the diagram are surjective,
they are also bijective. But since by virtue of hypothesis c), `M/𝔍 M` is a flat `(B/𝔍 B)`-module, it follows from
`(0_III, 10.2.1)` that `M` is a flat `B`-module.

*2°* One or the other of conditions (i), (iii) implies that every maximal ideal of `B` contains `𝔍 B`. It therefore
follows from 1° and from the conjunction of c) and d) that `M` is a faithfully flat `B`-module, and consequently
`gr_𝔍^0(M)` a faithfully flat `gr_𝔍^0(B)`-module `(0_I, 6.2.1)`. One has seen in 1° that hypothesis c) entails that the
three maps of the diagram `(11.3.10.3)` are bijective; the fact that `gr_𝔍^0(M)` is a faithfully flat `gr_𝔍^0(B)`-module
therefore implies that `u` is also bijective `(0_I, 6.4.1)`. On the other hand, conditions (ii) and (iii) imply that `B`
is an `A`-module ideally separated for the `𝔍`-preadic filtration *(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop.
2)*; one therefore deduces again from `(0_III, 10.2.1)` that if condition (i), or the conjunction of (ii) and (iii), is
verified, `B` is a flat `A`-module.

*(11.3.10.4)* Lemma `(11.3.10.2)` being established, one deduces from it `(11.3.10.1)` by taking for `𝔍` the maximal
ideal of `A`, and noting that conditions (ii) and (iii) of `(11.3.10.2)` are then satisfied *(Bourbaki, Alg. comm.,
chap. III, §5, n° 4, prop. 2)*. This also finishes the proof of `(11.3.7)`.

**Corollary (11.3.11).**

<!-- label: IV.11.3.11 -->

*Let `g : X → S`, `h : Y → S` be two morphisms locally of finite presentation, `f : X → Y` an `S`-morphism. The
following conditions are equivalent:*

*a) `g` is flat and `f_s : X_s → Y_s` is flat for every `s ∈ S`.*

*b) `h` is flat at all points of `f(X)` and `f` is flat.*

It suffices to apply `(11.3.10)` for `ℱ = 𝒪_X`.

**Remark (11.3.12).**

<!-- label: IV.11.3.12 -->

It would be interesting to be able to give to `(11.3.2)` and `(11.3.10)` proofs not using passage to the inductive
limit; for this it would suffice to prove the following criterion:

\*Let `A` be a ring, `B` an `A`-algebra of finite presentation, `M` a `B`-module of finite presentation, `𝔍` an

<!-- original page 140 -->

ideal of `A`, `𝔭` a prime ideal of `B` containing `𝔍 B`. Then the following two conditions are equivalent:\*

*a) `M_𝔭` is a flat `A`-module.*

*b) `M_𝔭/𝔍 M_𝔭` is a flat `(A/𝔍)`-module and `Tor_1^A(A/𝔍, M_𝔭) = 0`.*

When `A` is Noetherian, this is a consequence of `(0_III, 10.2.2)` applied to the Noetherian `A`-algebra `B`; can one
deduce the general statement from this by a passage to the inductive limit?

It is fitting to note in this connection that such a generalization is certainly not possible when one replaces
condition b) above by one of conditions c), d) of `(0_III, 10.2.1)` where `M` is replaced by `M̃`. Take for example for
`A` a local ring whose maximal ideal `𝔍` is principal and such that the intersection `𝔑 = ⋂_{n ≥ 0} 𝔍^{n+1}` is not
reduced to `0` (for example the ring of germs of infinitely differentiable numerical functions in the neighbourhood of
`0` in `ℝ`). Take `B = A`, `𝔭 = 𝔍`, and `M = A/𝔑`, where `𝔑` is a monogenic sub-module `≠ 0` of `𝔑`; `M` is therefore of
finite presentation. It is clear that `M` is not a flat `A`-module, for being of finite presentation, it would be free
*(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)*, which is absurd since `𝔑 ≠ 0`. However,
`𝔍^k M/𝔍^{k+n} M` is isomorphic to `A/𝔍^n` for any positive `k` and `n`, hence `M` indeed verifies conditions c) and d)
of `(0_III, 10.2.1)` since `A/𝔍` is a field.

**Proposition (11.3.13).**

<!-- label: IV.11.3.13 -->

*Let `f : X → Y` be a morphism of preschemes, `x` a point of `X` such that `f` is flat at the point `x`; set
`y = f(x)`.*

*(i) If `X` is reduced (resp. normal) at the point `x`, then `Y` is reduced (resp. normal) at the point `y`.*

*(ii) Suppose in addition that `f` is of finite presentation at the point `x`. Then, if `Y` is reduced (resp. normal) at
the point `y` and if the morphism `f` is reduced (resp. normal) at the point `x` `(6.8.1)`, `X` is reduced (resp.
normal) at the point `x`.*

The first assertion is included only for the record, having been proved in `(2.1.13)`. To prove (ii), one may confine
oneself to the case where `X = Spec(B)`, `Y = Spec(A)`, with `A` a local reduced (resp. integral and integrally closed)
ring and `B` an `A`-algebra of finite presentation. One may then `(8.9.1)` write `B = B_0 ⊗_{A_0} A`, where `A_0` is a
sub-`ℤ`-algebra of finite type of `A` and `B_0` an `A_0`-algebra of finite type. Let `(C_α)` be the filtered increasing
family of sub-`A_0`-algebras of finite type of `A`, which are therefore `ℤ`-algebras of finite type; one has
`A = lim C_α`. Let us now distinguish the two cases:

*1° Suppose `A` reduced and `f` reduced at the point `x`.* If `𝔪` is the maximal ideal of `A`, let `𝔭_α` be the prime
ideal `𝔪 ∩ C_α`, and set `A'_α = (C_α)_{𝔭_α}`, so that one also has `A = lim A'_α` `(5.13.3)`. Set `Y_α = Spec(A'_α)`,
`X_α = Spec(B_0 ⊗_{A_0} A'_α)` and let `f_α : X_α → Y_α`, `x_α` (resp. `y_α`) the projection of `x` (resp. `y`) in `X_α`
(resp. `Y_α`). Since `f` is reduced at the point `x`, there exists `α_0` such that `f_α` is reduced at the point `x_α`
for `α ≥ α_0` (`(6.7.8)` and `(11.2.6)`); since `Y_α` and `X_α` are Noetherian and `A'_α` is reduced (since this is the
case for `C_α`), one deduces from `(3.3.5)` that `X_α` is reduced at the point `x_α`. But since
`B = lim(B_0 ⊗_{A_0} A'_α)`, one also has `𝒪_{X, x} = lim 𝒪_{X_α, x_α}` `(5.13.3)` and consequently `𝒪_{X, x}` is
reduced `(5.13.2)`.

*2° Suppose `A` integrally closed and `f` normal at the point `x`.* Since `C_α` is universally Japanese `(7.7.4)`, its
integral closure `C'_α` is a finite `C_α`-algebra, evidently contained in `A`. Let `𝔭'_α` be the prime ideal `𝔪 ∩ C'_α`
and set `A''_α = (C'_α)_{𝔭'_α}`, so that `A''_α` is a Noetherian integral integrally closed local ring, and one has
`A = lim A''_α` `(5.13.3)`. Set `Y''_α = Spec(A''_α)`, `X''_α = Spec(B_0 ⊗_{A_0} A''_α)` and let
`f''_α : X''_α → Y''_α`, `x''_α` (resp. `y''_α`) the projection of `x` (resp. `y`) in `X''_α` (resp. `Y''_α`). Since `f`
is normal at the point `x`, there exists `α_0` such that, for `α ≥ α_0`, `f''_α` is normal at the point `x''_α`
(`(6.7.8)` and `(11.2.6)`);

<!-- original page 141 -->

since `X''_α` and `Y''_α` are Noetherian and `A''_α` is integrally closed, one deduces from `(6.5.4)` that `X''_α` is
normal at the point `x''_α`. But the morphisms `Spec(A''_β) → Spec(A''_α)` for `α ≤ β` are dominant, hence, since by
virtue of `(11.3.1)` one may suppose that the `f''_α` are flat for `α ≥ α_0`, it follows from `(2.3.7)` that every
irreducible component of `X''_β` dominates an irreducible component of `X''_α`. One then concludes from `(5.13.4)`,
applied to the preschemes `Spec(𝒪_{X_0, x_0} ⊗_{A_0} A''_α)`, that `X` is normal at the point `x`.

**Corollary (11.3.14).**

<!-- label: IV.11.3.14 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`, `y = f(x)`. If `Y` is geometrically
unibranch at the point `y` `(6.15.1)` and if the morphism `f` is normal at the point `x` `(6.8.1)`, then `X` is
geometrically unibranch at the point `x`.*

One may evidently confine oneself to the case where `Y = Spec(A)`, `A` being an integral local ring geometrically
unibranch, `y` being the closed point of `Y`. Let `A'` be the integral closure of `A`; set `Y' = Spec(A')` and let `y'`
be the closed point of `Y'`, so that the morphism `g : Y' → Y` is radicial at the point `y` `(6.15.3)`, integral and
birational. If one sets `X' = X ×_Y Y'`, and if `f' : X' → Y'` and `g' : X' → X` are the projections, `g'` is integral
and radicial at the point `x` `(6.15.3.1)`. Let then `x'` be the unique point of `g'⁻¹(x)`, which is above `y'`. The
morphism `f'` is of finite presentation and normal at the point `x'` `(6.7.8)`, and consequently the local ring
`𝒪_{X', x'}` is integral and integrally closed `(11.3.13)`. On the other hand, one may suppose `f` flat `(11.3.1)`,
hence `g'` is a birational morphism `(6.15.4.1)`; consequently `Spec(𝒪_{X, x})` is irreducible, and since `𝒪_{X, x}` is
reduced `(11.3.13)` it is integral and geometrically unibranch by virtue of `(6.15.5)`.

**Proposition (11.3.15).**

<!-- label: IV.11.3.15 -->

*Let `A` be a ring, `B` an `A`-algebra of finite presentation, `M` a `B`-module of finite presentation, which is a flat
`A`-module. Then there exists a finite sequence `(f_i)_{1 ≤ i ≤ n}` of elements of `A` such that the ideal generated by
the `f_i` is equal to `A`, and such that, for `0 ≤ i < n`, `M_{f_{i+1}}/(∑_{j ≤ i} f_j M_{f_{i+1}})` is a free
`(A_{f_{i+1}}/(∑_{j ≤ i} f_j A_{f_{i+1}}))`-module.*

One may also say that the `D(f_i)` form an open covering of `X = Spec(A)`, and that if one sets `Z_1 = D(f_1)`, then, by
induction, `Z_{i+1} = D(f_{i+1}) ∩ V(f_1 A + … + f_i A)`, the `Z_i` form a partition of `X` into locally closed sets,
`A_{f_{i+1}}/(∑_{j ≤ i} f_j A_{f_{i+1}})` being the ring of an affine sub-scheme of `X` having `Z_{i+1}` for underlying
space.

To prove the proposition, one may first, by virtue of `(11.2.7)`, suppose that there exists a Noetherian sub-ring `A_0`
of `A`, an `A_0`-algebra of finite type `B_0` and a `B_0`-module of finite type `M_0`, flat over `A_0` and such that
`B = B_0 ⊗_{A_0} A`, `M = M_0 ⊗_{A_0} A`; it is clear that it will suffice to prove the proposition for `A_0`, `B_0` and
`M_0`, for if the elements `f_i ∈ A_0` verify in this case the conditions of the statement, they will also verify them
for `A`, `B`, `M`, since
`M_{f_{i+1}}/(∑_{j ≤ i} f_j M_{f_{i+1}}) = ((M_0)_{f_{i+1}}/(∑_{j ≤ i} f_j (M_0)_{f_{i+1}})) ⊗_{A_0} A` *(Bourbaki, Alg.
comm., chap. II, §2, n° 7, prop. 18)*. One may therefore from now on confine oneself to the case where `A` is
Noetherian.

Let us now note that if `C` is a Noetherian ring, `𝔑` its nilradical and `P` a flat `C`-module, then it follows from
`(0_III, 10.1.2)` that for `P` to be a free `C`-module,

<!-- original page 142 -->

it is necessary and sufficient that `P ⊗_C (C/𝔑)` be a free `(C/𝔑)`-module. Note on the other hand that if `C` is a
Noetherian reduced ring, there exists `g ∈ C` such that `C_g` is an integral ring. Let us now use lemma `(6.9.2)`: one
can define by induction a sequence `(f_i)_{i ≥ 1}` of elements of `A` in the following way:

1° `f_1` is such that `A^1 = (A_{red})_{f_1}` is integral and `M ⊗_A A^1` a free `A^1`-module;

2° if the ideal `𝔍_i` generated by `f_1, …, f_i` is `A`, `f_{i+1} = f_i`;

3° if on the contrary `𝔍_i ≠ A`, `f_{i+1}` is an element not belonging to `𝔍_i` such that
`A^{i+1} = ((A/𝔍_i)_{red})_{f_{i+1}}` is integral and `M ⊗_A A^{i+1}` an `A^{i+1}`-module free.

Since `A` is Noetherian, the increasing sequence `(𝔍_i)` is stationary, hence there exists `n` such that `f_1, …, f_n`
generate the ideal `A`, and the `f_i` answer the question.

**Proposition (11.3.16).**

<!-- label: IV.11.3.16 -->

*Let `f : X → Y` be a faithfully flat morphism of finite presentation, `g : Y → Z` a morphism such that `g ∘ f : X → Z`
is a morphism of finite type (resp. of finite presentation). Then `g` is a morphism of finite type (resp. of finite
presentation).*

Since `f` is surjective and `g ∘ f` quasi-compact, `g` is quasi-compact `(1.1.3)`. Let us first show that if `g ∘ f` is
of finite presentation, `g` is quasi-separated. Consider indeed an affine open set `W ⊂ Z`, and let `(V_i)` be a finite
affine cover of `g⁻¹(W)`; the matter is to see that the `V_i ∩ V_j` are quasi-compact `(1.2.6 and 1.2.7)`. For each `i`,
let `(U_{ih})` be a finite affine open cover of `f⁻¹(V_i)`; since `f` is of finite presentation, the `U_{ih} ∩ U_{jk}`
are all quasi-compact; now, since `f` is surjective, `V_i ∩ V_j` is the union of the images `f(U_{ih} ∩ U_{jk})` for
`h`, `k` varying, hence is quasi-compact since `f` is continuous.

The question is therefore local on `Y` and one may suppose that `Y = Spec(B)` and `Z = Spec(A)` are affine, `X` being
the finite union of affine open sets `X_i = Spec(C_i)`, where the `C_i` are `B`-algebras of finite type (resp. of finite
presentation). If `X'` is the sum prescheme of the `X_i`, `p : X' → X` the morphism coinciding with the canonical
injection on each `X_i`, `p` is a faithfully flat morphism of finite presentation `(1.6.5)`, hence `g ∘ f ∘ p` is a
morphism of finite type (resp. of finite presentation) and `f ∘ p` a faithfully flat morphism of finite presentation.
One may therefore also suppose that `X = Spec(C)` is affine, and one is therefore reduced to proving the

**Corollary (11.3.17).**

<!-- label: IV.11.3.17 -->

*Let `A` be a ring, `B` an `A`-algebra, `C` a `B`-algebra of finite presentation and which is a faithfully flat
`B`-module. Then, if `C` is an `A`-algebra of finite type (resp. of finite presentation), `B` is an `A`-algebra of
finite type (resp. of finite presentation).*

Suppose first that `g ∘ f` is of finite type. Let `(B_λ)` be the filtered increasing family of sub-`A`-algebras of
finite type of `B`; by virtue of `(8.8.2)`, there exists an index `α` such that `C = C_α ⊗_{B_α} B`, where `C_α` is a
`B_α`-algebra of finite presentation; moreover `(8.10.5` and `11.2.6)` one may suppose that `C_α` is a faithfully flat
`B_α`-module. For `λ ≥ α`, one has therefore `C = C_λ ⊗_{B_λ} B`, where `C_λ` is a faithfully flat `B_λ`-module; since
the map `B_λ → B` is injective, one deduces that the same is true of `C_λ → C`. Moreover, since `C = lim C_λ`, every
element of `C` belongs to some `C_λ`, and consequently there exists `λ` such that the map `C_λ → C`

<!-- original page 143 -->

is bijective, since `C` is a `B`-algebra of finite type. But then the map `B_λ → B` is bijective by faithful flatness,
hence `B = B_λ` is an `A`-algebra of finite type.

Suppose now that `g ∘ f` is of finite presentation, `C` being therefore an `A`-algebra of finite presentation. From the
first part of the reasoning, one has `B = A[T_1, …, T_n]/𝔍` for some ideal `𝔍`; let `(𝔍_λ)` be the filtered family of
ideals of finite type of `A[T_1, …, T_n]` contained in `𝔍`, so that `𝔍 = lim 𝔍_λ` and `B = lim B_λ`, with
`B_λ = A[T_1, …, T_n]/𝔍_λ`. Applying as above `(8.8.2)`, `(8.10.5)` and `(11.2.6)`, one has `C = C_α ⊗_{B_α} B`, where
`C_α` is a `B_α`-algebra of finite presentation and a faithfully flat `B_α`-module; one will again set
`C_λ = C_α ⊗_{B_α} B_λ` for `λ ≥ α` so that `C_λ = C_α/(C_α ⊗_{B_α} (𝔍_λ/𝔍_α))` by flatness, and similarly
`C = C_α/(C_α ⊗_{B_α} (𝔍/𝔍_α))`. Since by hypothesis `C` is an `A`-algebra of finite presentation as well as `C_α`,
`C_α ⊗_{B_α} (𝔍/𝔍_α)` is an ideal of finite type of `C_α` `(1.4.4)`, and the `C_α ⊗_{B_α} (𝔍_λ/𝔍_α)` identify with
ideals of finite type of `C_α` of which `C_α ⊗_{B_α} (𝔍/𝔍_α)` is the union. There exists consequently `λ ≥ α` such that
`C_α ⊗_{B_α} (𝔍/𝔍_α) = C_α ⊗_{B_α} (𝔍_λ/𝔍_α)`, whence `𝔍 = 𝔍_λ` by faithful flatness, which proves that `B` is an
`A`-algebra of finite presentation.

<!-- original page 143 -->

### 11.4. Descent of flatness by arbitrary morphisms: artinian base case

**Theorem (11.4.1).**

<!-- label: IV.11.4.1 -->

*Let `A` be a ring, `𝔍` a nilpotent ideal of `A`, `u_λ : A → B_λ` (`λ ∈ L`) a family of ring homomorphisms such that the
intersection of the kernels of the `u_λ` is reduced to `0`. Let `M` be an `A`-module such that for every `λ ∈ L`,
`M ⊗_A B_λ` is a free `B_λ`-module and `M ⊗_A (A/𝔍)` is a free `(A/𝔍)`-module. Then `M` is a free `A`-module. If
moreover the index set `L` is finite, one can replace "free" by "flat" throughout the preceding statement.*

In both cases it suffices to prove that `M` is a flat `A`-module: indeed, when `M ⊗_A (A/𝔍)` is a free `(A/𝔍)`-module,
it will result that `M` is a free `A`-module by virtue of `(0_III, 10.1.2)`.

We shall use the following lemma, which generalizes `(0_III, 10.2.1)`:

**Lemma (11.4.1.1).**

<!-- label: IV.11.4.1.1 -->

*Let `A` be a ring endowed with a finite filtration `(𝔍_n)_{0 ≤ n ≤ N+1}` with `𝔍_0 = A`, `𝔍_{N+1} = 0`. Let `M` be an
`A`-module endowed with the filtration `(𝔍_n M)_{0 ≤ n ≤ N+1}`, and denote by `gr(A)` and `gr(M)` the corresponding
graded ring and module. Suppose that `M ⊗_A (A/𝔍_1)` is a flat `(A/𝔍_1)`-module and that the canonical homomorphism*

```text
(11.4.1.2)                gr_0(M) ⊗_{gr_0(A)} gr(A) → gr(M)
```

*is injective. Then `M` is a flat `A`-module.*

The canonical homomorphism `(11.4.1.2)` is defined in the same way as that of `(0_III, 10.1.1)`, being in degree `n` the
homomorphism

```text
  gr_0(M) ⊗_{gr_0(A)} gr_n(A) → gr_n(M)
```

deriving from the canonical homomorphism `M ⊗ 𝔍_n → 𝔍_n M` by passage to quotients. The lemma is proved by induction on
`N`, since there is nothing to prove for `N = 0`.

<!-- original page 144 -->

The hypotheses on `M` imply, by virtue of the induction hypothesis, that `M ⊗_A (A/𝔍_N)` is a flat `(A/𝔍_N)`-module.
Note now that one has `𝔍_N 𝔍_{N+1} = 0 ⊂ 𝔍_{N+1}`, and
`(M/𝔍_1 M) ⊗ (𝔍_N/𝔍_{N+1}) = (M/𝔍_N M) ⊗ (𝔍_N/𝔍_{N+1}) = (M/𝔍_N M) ⊗ 𝔍_N`; hence the canonical homomorphism

```text
  (M/𝔍_N M) ⊗ 𝔍_N → 𝔍_N M
```

is injective. Applying `(0_III, 10.2.1)` to the `𝔍_N`-preadic filtration, one concludes that `M` is indeed a flat
`A`-module.

To apply this lemma to `(11.4.1)`, we shall denote by `𝔍_n` the ideal of `A` intersection of the inverse images
`u_λ⁻¹(𝔍^n B_λ)`: it is immediate that `𝔍_0 = A`, `𝔍_m 𝔍_n ⊂ 𝔍_{m+n}` for `m ≥ 0`, `n ≥ 0`; moreover, if `𝔍^{N+1} = 0`,
one also has `𝔍_{N+1} = 0` since the intersection of the kernels of the `u_λ` is reduced to `0`.

Endow `A` with the filtration `(𝔍_n)`, `M` with the filtration `(𝔍_n M)`, and, for each `λ`, endow `B_λ` and
`N_λ = M ⊗_A B_λ` with the `𝔍`-preadic filtrations; consider for each `λ` the commutative diagram

```text
  gr_𝔍(M) ⊗_{gr_𝔍(A)} gr(A)  ─ f ─→  gr(M)
         │                              │
         │                              │
         ↓                              ↓
  gr_{𝔍}(N_λ) ⊗_{gr_{𝔍}(B_λ)} gr_𝔍(B_λ)  ─ φ_λ ─→  gr_𝔍(N_λ)
```

where the horizontal arrows are the canonical homomorphisms `(11.4.1.2)` and the vertical arrows are deduced from the
canonical homomorphisms `A → B_λ` and `M → N_λ`. The hypothesis that `N_λ` is a flat `B_λ`-module implies that `φ_λ` is
injective `(0_III, 10.2.1)`, hence `Ker(f) ⊂ Ker(f_λ)`. Setting `A_0 = A/𝔍_1`, `M_0 = M ⊗_A A_0`, note that

```text
  gr_0(N_λ) = N_λ/𝔍 N_λ = (M/𝔍 M) ⊗_A B_λ = (M/𝔍_1 M) ⊗_A (B_λ/𝔍 B_λ)
```

since this last tensor product equals

```text
  (M ⊗_A B_λ)/(Im(M ⊗_A 𝔍 B_λ) + Im(𝔍_1 M ⊗_A B_λ))
```

and one has `Im(𝔍_1 M ⊗_A B_λ) = Im(M ⊗_A 𝔍_1 B_λ) ⊂ Im(M ⊗_A 𝔍 B_λ)` since `𝔍_1 B_λ ⊂ 𝔍 B_λ` by definition; finally,
the relation `𝔍_1 N_λ ⊂ 𝔍 N_λ` shows that one has also

```text
  gr_0(N_λ) = (M/𝔍_1 M) ⊗_{A_0} (B_λ/𝔍 B_λ),
```

so that finally one has

```text
  gr_0(N_λ) = M_0 ⊗_{A_0} gr_𝔍(B_λ)/(𝔍 · gr_𝔍(B_λ))
```

and consequently

```text
  gr_𝔍(N_λ) = M_0 ⊗_{A_0} gr_𝔍(B_λ).
```

The homomorphism `f_λ` can thus be written

```text
  1 ⊗ gr(u_λ) : M_0 ⊗_{A_0} gr(A) → M_0 ⊗_{A_0} gr_𝔍(B_λ)
```

<!-- original page 145 -->

and as `M_0` is by hypothesis a flat `A_0`-module, the kernel of `f_λ` equals `M_0 ⊗_{A_0} R_λ`, where `R_λ` is the
kernel of `gr(u_λ) : gr(A) → gr_𝔍(B_λ)`. All comes down therefore to proving that `⋂_λ (M_0 ⊗_{A_0} R_λ) = 0`. Now, by
definition of the `𝔍_n`, the intersection of the kernels of the homomorphisms `𝔍_n A/𝔍_{n+1} A → 𝔍^n B_λ/𝔍^{n+1} B_λ`,
as `λ` runs through `L`, is reduced to `0`, in other words `⋂_{λ ∈ L} R_λ = 0`. This being so, suppose first that `M_0`
is a free `A_0`-module; taking a basis of `M_0`, one sees at once that one has
`M_0 ⊗_{A_0} (⋂ R_λ) = ⋂ (M_0 ⊗_{A_0} R_λ)`, whence the proposition in this case. When `L` is finite, the preceding
formula is still true under the sole hypothesis that `M_0` is a flat `A_0`-module `(0_I, 6.1.3)`, which completes the
proof.

**Remark (11.4.2).**

<!-- label: IV.11.4.2 -->

*The conclusion of `(11.4.1)` can fail if `L` is infinite and if one supposes only that `M ⊗_A (A/𝔍)` is a flat
`(A/𝔍)`-module.* For example, let `V` be a discrete valuation ring, `K` its field of fractions, and let `A = V[T]/(T²)`
(`T` indeterminate); take for `𝔍` the image of `(T)` in `A`, so that `A/𝔍 = V`, and take `M = K`, which is a
`(A/𝔍)`-module, so equal to `M ⊗_A (A/𝔍)`; moreover `M` is a flat `(A/𝔍)`-module, but not a flat `A`-module, for since
`𝔍` is nilpotent, it would result from `(0_III, 10.1.2)` that `M` would be a free `A`-module, which is absurd since
`𝔍 K = 0`. Consider on the other hand the maximal ideal `𝔪` of the Noetherian local ring `A`; one has `𝔪 K = K`, hence
`M ⊗_A (A/𝔪^n) = 0` for every integer `n`; the `(A/𝔪^n)`-modules `M ⊗_A (A/𝔪^n)` are thus flat for every `n`, and the
intersection of the `𝔪^n` is reduced to `0`.

**Corollary (11.4.3).**

<!-- label: IV.11.4.3 -->

*Let `A` be a semi-local ring whose radical `𝔍` is nilpotent (for example an artinian ring), `u_λ : A → B_λ` (`λ ∈ L`) a
family of ring homomorphisms such that the intersection of the kernels of the `u_λ` is reduced to `0`. For an `A`-module
`M` to be flat, it is necessary and sufficient that for every `λ ∈ L`, `M ⊗_A B_λ` be a flat `B_λ`-module.*

Since `A/𝔍` is a direct product of a finite number of fields `(Bourbaki, Alg. comm., chap. II, §3, n° 5, prop. 16)` and
`𝔍` is nilpotent, `A` is a direct product of a finite number of local rings `A_i` whose radical is nilpotent
`(loc. cit., §4, n° 3, cor. 1 of prop. 15)`, and `M` is consequently a direct sum of `A`-modules `M_i`, each `M_i` being
annihilated by the `A_j` of index `j ≠ i`; for `M` to be a flat `A`-module, it is necessary and sufficient that each
`M_i` be a flat `A_i`-module; moreover, the intersection of the kernels of the homomorphisms `A_i → A → B_λ` is reduced
to `0`, and `M_i ⊗_{A_i} B_λ` is a direct summand of `M ⊗_A B_λ`. One can therefore restrict to the case where `A` is
moreover local. Then `A/𝔍` is a field, hence `M ⊗_A (A/𝔍)` is a free `(A/𝔍)`-module, and it suffices to see that for
every `λ`, `M ⊗_A B_λ` is a free `B_λ`-module, by virtue of `(11.4.1)`. But if one sets `𝔍_λ = 𝔍 B_λ`,
`(M ⊗_A B_λ) ⊗_{B_λ} (B_λ/𝔍_λ) = (M ⊗_A (A/𝔍)) ⊗_{A/𝔍} (B_λ/𝔍_λ)` is a free `(B_λ/𝔍_λ)`-module, and `𝔍_λ` is nilpotent.
The conclusion thus results from the hypothesis that `M ⊗_A B_λ` is a flat `B_λ`-module and from `(0_III, 10.1.2)`.

**Corollary (11.4.4).**

<!-- label: IV.11.4.4 -->

*Let `A` be a ring, `M` an `A`-module; suppose that there exists a nilpotent ideal `𝔍` of `A` such that `M ⊗_A (A/𝔍)` is
a free `(A/𝔍)`-module. Then the set of ideals `𝔎` of `A` such that `M ⊗_A (A/𝔎)` is a free `(A/𝔎)`-module admits a
smallest element `𝔎_0` (which is also the smallest of the ideals `𝔎` such that `M ⊗_A (A/𝔎)` is a flat `(A/𝔎)`-module).*

<!-- original page 146 -->

*For a homomorphism `u : A → A'` to be such that `M ⊗_A A'` is a free `A'`-module (resp. a flat `A'`-module), it is
necessary and sufficient that `u` factor as `A → A/𝔎_0 → A'` (or equivalently that `𝔎_0 A' = 0`).*

The fact that the intersection `𝔎_0` of the ideals `𝔎` for which `M ⊗_A (A/𝔎)` is a free `(A/𝔎)`-module is the smallest
of these ideals results from `(11.4.1)` applied to the ring `A/𝔎_0`, to its nilpotent ideal `𝔍/𝔎_0`, and to the
homomorphisms `A/𝔎_0 → A/𝔎`, whose kernels have `0` as intersection. If `A'` is an `(A/𝔎_0)`-algebra, one has
`M ⊗_A A' = (M ⊗_A (A/𝔎_0)) ⊗_{A/𝔎_0} A'`, hence `M ⊗_A A'` is a free `A'`-module. Conversely, if `A'` is an `A`-algebra
such that `M ⊗_A A'` is a free `A'`-module and if `𝔎` is the kernel of the homomorphism `A → A'`, it results from
`(11.4.1)` applied to the ring `A/𝔎`, to the `(A/𝔎)`-module `M ⊗_A (A/𝔎)`, to the nilpotent ideal `𝔍𝔎/𝔎` and to the
injective homomorphism `A/𝔎 → A'`, that `M ⊗_A (A/𝔎)` is a free `(A/𝔎)`-module, hence that `𝔎 ⊃ 𝔎_0`. The fact that one
can replace "free" by "flat" in what precedes (keeping naturally the hypothesis that `M ⊗_A (A/𝔍)` is a free
`(A/𝔍)`-module) results from `(0_III, 10.1.2)`, as was seen at the beginning of the proof of `(11.4.1)`.

**Proposition (11.4.5).**

<!-- label: IV.11.4.5 -->

*Let `Y` be an irreducible prescheme, `f : X → Y` a morphism of finite presentation, `ℱ` an `𝒪_X`-Module of finite
presentation. Then there exist a non-empty open set `U` in `Y` and a closed subscheme `Z` of `U`, of finite presentation
over `U`, having the following property: for every base change `U' → U`, setting `X' = X ×_Y U'`, `f' = f_{(U')}` and
`ℱ' = ℱ ⊗_{𝒪_Y} 𝒪_{U'}`, in order that `ℱ'` be `f'`-flat, it is necessary and sufficient that the morphism `U' → U`
factor as `U' → Z → U`. Such a scheme `Z` has the same underlying space as `U`. Suppose moreover that `Y` is affine, and
let `(W_i)` be a finite cover of `X` by affine open sets; then one may suppose `U` chosen so that, if `U' = Spec(A')` is
an affine scheme and `U' → U` a morphism factoring as `U' → Z → U`, each `Γ(W_i ×_Y U', ℱ')` is a free `A'`-module.*

One may evidently restrict to the case where `Y = Spec(A)` is affine. Using `(8.9.1)`, there exists a Noetherian subring
`A_1` of `A`, a morphism of finite type `f_1 : X_1 → Y_1 = Spec(A_1)` and a coherent `𝒪_{X_1}`-Module `ℱ_1` such that
`f = f_1 × 1` and `ℱ = ℱ_1 ⊗_{𝒪_{Y_1}} 𝒪_Y`; one can moreover suppose that the `W_i` are inverse images of affine open
sets of `X_1`. Note moreover that `Y_1` is irreducible, the morphism `Y → Y_1` being dominant `(I, 1.2.7)`. Suppose the
proposition proved for `Y_1`, `ℱ_1` and `f_1`, and let `U_1` be the open set of `Y_1` and `Z_1` the closed subscheme of
`U_1` having the desired properties, `U = U_1 ×_{Y_1} Y` and `Z = Z_1 ×_{Y_1} Y` their inverse images. Then, if `U' → U`
is a base change such that `ℱ' = ℱ ⊗_{𝒪_Y} 𝒪_{U'} = ℱ_1 ⊗_{𝒪_{Y_1}} 𝒪_{U'}` is `f'`-flat, the morphism `U' → U_1`
factors as `U' → Z_1 → U_1`; but as `U' → U_1` also factors as `U' → U → U_1`, the definition of fibre product of
preschemes shows that `U' → U` factors as `U' → Z → U`.

One can therefore restrict to the case where `A` is *Noetherian*; let `𝔑` be its nilradical, which is nilpotent, and set
`A_0 = A_red = A/𝔑`, `Y_0 = Spec(A_0) = Y_red`, `X_0 = X ×_Y Y_0`, `ℱ_0 = ℱ ⊗_{𝒪_Y} 𝒪_{Y_0}`, `W_{i,0} = W_i ×_Y Y_0`;
if `M_i = Γ(W_i, ℱ)`, then `M_{i,0} = Γ(W_{i,0}, ℱ_0)` equals `M_i ⊗_A A_0`. As `A_0` is integral, one can, by virtue of
the theorem of generic flatness `(6.9.2)`, replacing if necessary `Y` by a non-empty open set of `Y`, suppose that the
`M_{i,0}` are free `A_0`-modules. By virtue of `(11.4.4)`, there is therefore for each `i` an ideal `𝔍_i ⊂ 𝔑` such that

<!-- original page 147 -->

the `A`-algebras `A'` for which the `M_i ⊗_A A'` are free (or flat) `A'`-modules are exactly those for which
`𝔍_i A' = 0`. Let `𝔍 = ∑_i 𝔍_i`, which is an ideal contained in `𝔑`; to say that `ℱ ⊗_A A'` is `A'`-flat is equivalent
to saying that the `M_i ⊗_A A'` are all flat `A'`-modules, hence that `𝔍 A' = 0`. It follows that if one takes
`Z = V(𝔍)`, one answers the question, for in order that a morphism `U' → U` have the property of the statement, it is
evidently necessary and sufficient that for every affine open set `V' ⊂ U'`, the morphism `V' → U` have the same
property.

**Corollary (11.4.6).**

<!-- label: IV.11.4.6 -->

*Let `A` be a ring such that `Spec(A)` is irreducible, `𝔭` its unique minimal prime ideal, `B` an `A`-algebra of finite
presentation, `M` a `B`-module of finite presentation. Suppose that `M_𝔭` is a flat `A_𝔭`-module; then there exists
`t ∈ A − 𝔭` such that `M_t` is a free `A_t`-module.*

Applying `(11.4.5)` to `Y = Spec(A)`, `X = Spec(B)`, `ℱ = M̃`, one can (replacing if necessary `A` by `A_h`, where
`h ∈ A − 𝔭`) suppose that there exists an ideal of finite type `𝔍` in `A` such that the `A`-algebras `A'` for which
`M ⊗_A A'` is a free `A'`-module (or flat) are exactly those such that `𝔍 A' = 0`. In particular, the hypothesis that
`M_𝔭` is a flat `A_𝔭`-module implies `𝔍 A_𝔭 = 0`, or equivalently `𝔍_𝔭 = 0`. But as `𝔍` is of finite type, there exists
`t ∈ A − 𝔭` such that `𝔍_t = 0`, or equivalently `𝔍 A_t = 0`, and consequently `M_t` is a free `A_t`-module.

**Proposition (11.4.7).**

<!-- label: IV.11.4.7 -->

*Let `A` be a Noetherian ring, `𝔍` an ideal of `A`, `M` an `A`-module ideally separated `(0_III, 10.2.1)` for the
`𝔍`-preadic topology. Let `(𝔭_i)_{1 ≤ i ≤ r}` be a finite family of prime ideals of `A` containing `𝔍`; for every
integer `n ≥ 0`, let `𝔭_i^{(n)}` be the `n`-th symbolic power of `𝔭_i` (kernel of the homomorphism
`A → A_{𝔭_i}/𝔭_i^n A_{𝔭_i}`); set `𝔍_n = ⋂_{i=1}^r 𝔭_i^{(n)}`, so that `𝔍_n ⊃ 𝔍^n`, and suppose that the topology
defined by the filtration `(𝔍_n)` is identical to the `𝔍`-preadic topology (in other words, that for every `n`, there
exists `m` such that `𝔍^n ⊃ 𝔍_m`). For `M` to be a flat `A`-module, it is necessary and sufficient that `M ⊗_A (A/𝔍)` be
a flat `(A/𝔍)`-module and that, for every `i`, `M ⊗_A A_{𝔭_i} = M_{𝔭_i}` be a flat `A_{𝔭_i}`-module.*

As `M` is ideally separated, it suffices, by virtue of `(0_III, 10.2.1)`, to show that, for every `n ≥ 0`,
`M ⊗_A (A/𝔍^n)` is a flat `(A/𝔍^n)`-module; since every `𝔍^n` contains a `𝔍_m`, it amounts to the same thing to prove
that for every `n`, `M ⊗_A (A/𝔍_n)` is a flat `(A/𝔍_n)`-module. Now, as `𝔍_1 ⊃ 𝔍`, `M ⊗_A (A/𝔍_1)` is a flat
`(A/𝔍_1)`-module; in the ring `A/𝔍_n`, the ideal `𝔍_1/𝔍_n` is nilpotent, and finally the intersection of the kernels of
the homomorphisms `A/𝔍_n → A_{𝔭_i}/𝔭_i^n A_{𝔭_i}` is null in `A/𝔍_n`, by definition of `𝔍_n`. It suffices therefore, by
`(11.4.1)`, to verify that `M ⊗_A (A_{𝔭_i}/𝔭_i^n A_{𝔭_i})` is a flat `(A_{𝔭_i}/𝔭_i^n A_{𝔭_i})`-module, which results
from the hypothesis that `M ⊗_A A_{𝔭_i}` is a flat `A_{𝔭_i}`-module.

**Remark (11.4.8).**

<!-- label: IV.11.4.8 -->

*The hypothesis made in `(11.4.7)` on the topology defined by the `𝔍_n` is verified if, for every sufficiently large
`n`, `Ass(A/𝔍^n)` is contained in the set of `𝔭_i`.* Indeed, `𝔍^n` is then an intersection of primary ideals for the
`𝔭_i`, each of which contains a symbolic power of `𝔭_i`, whence the conclusion. In particular:

**Corollary (11.4.9).**

<!-- label: IV.11.4.9 -->

*Let `A` be a Noetherian ring, `𝔍` a nilpotent ideal of `A`, `M` an `A`-module. For `M` to be a flat `A`-module (resp.
free), it is necessary and sufficient that `M ⊗_A (A/𝔍)` be a flat (resp. free) `(A/𝔍)`-module and that for every prime
ideal `𝔭 ∈ Ass(A)`, `M_𝔭` be a flat `A_𝔭`-module.*

<!-- original page 148 -->

The assertion concerning the case where `M ⊗_A (A/𝔍)` is free still follows from the assertion concerning the case where
`M ⊗_A (A/𝔍)` is flat by `(0_III, 10.1.2)`.

**Corollary (11.4.10).**

<!-- label: IV.11.4.10 -->

*Let `A` be a Noetherian ring, `𝔍` an ideal of `A`, `M` an `A`-module. Suppose that `M` is ideally separated for the
`𝔍`-preadic topology and that `gr_𝔍(A)` is a flat `(A/𝔍)`-module. For `M` to be a flat `A`-module, it is necessary and
sufficient that `M ⊗_A (A/𝔍)` be a flat `(A/𝔍)`-module and that for every `𝔭 ∈ Ass(A/𝔍)`, `M_𝔭` be a flat `A_𝔭`-module.*

Taking `(11.4.8)` into account, all comes down to showing that `Ass(A/𝔍^n)` is contained in `Ass(A/𝔍)` for every `n`.
Now, if `a ∈ A` belongs to none of the `𝔭 ∈ Ass(A/𝔍)`, the homothety of ratio `a` is injective in `A/𝔍`; as each of the
`𝔍^k/𝔍^{k+1}` is a flat `(A/𝔍)`-module, `a` is also a `(𝔍^k/𝔍^{k+1})`-regular element, hence `a` is `(A/𝔍^n)`-regular
for every `n` `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 1 of th. 1)`, and consequently does not belong to any
prime ideal associated to `A/𝔍^n`, whence the corollary `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`.

**Proposition (11.4.11).**

<!-- label: IV.11.4.11 -->

*Let `A` be a local artinian ring of maximal ideal `𝔪`, `Y = Spec(A)`, `y` the unique point of `Y`, `f : X → Y` a
morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module. Let `(A'_α)` be a family of local rings, and for each `α`,
`u_α : A → A'_α` a ring homomorphism (necessarily local). Set `Y'_α = Spec(A'_α)`, `X'_α = X ×_Y Y'_α`,
`ℱ'_α = ℱ ⊗_A A'_α`. Let `x` be a point of `X`, and suppose the following conditions verified:*

*(i) The intersection of the kernels of the `u_α` is reduced to `0`.*

*(ii) The extension `k(x)` of the residue field `k` of `A` is primary `(4.3.1)` (a condition automatically verified if
`k` is separably closed).*

*(iii) For every `α`, there exists a point `x'_α ∈ X'_α` whose respective projections in `X` and `Y'_α` are `x` and the
closed point `y'_α` of `Y'_α`, and such that `ℱ'_α` is `Y'_α`-flat at the point `x'_α`.*

*Under these conditions, `ℱ` is `f`-flat at the point `x`.*

The question being local on `X`, one can evidently restrict to the case where `f` is a morphism of finite type and
suppose `ℱ ≠ 0`. We shall proceed in several steps.

**I)** *Reduction to the case where `A'_α` is a local ring of a `Y`-prescheme of finite type and where the residue field
`k'_α` of `A'_α` is a finite extension of `k`.*

As the reduction is done separately on each `A'_α`, one can suppress in this part the index `α`. Let `𝔪'` be the maximal
ideal of `A'`. Consider `A'` as inductive limit of its sub-`A`-algebras of finite type `B_λ`, and set `𝔫_λ = 𝔪' ∩ B_λ`;
`A'` is also inductive limit of its local subrings `B'_λ = (B_λ)_{𝔫_λ}` `(5.13.5)`, and one evidently has
`𝔪' ∩ B'_λ = 𝔫_λ`, maximal ideal of `B'_λ`. There exists therefore `(11.2.6)` an index `λ` such that, setting
`Z_λ = Spec(B'_λ)`, `ℱ ⊗_A B'_λ` is `Z_λ`-flat at the point `x'_λ`, projection of `x'`, the projection of `x'_λ` on
`Z_λ` being the closed point `ξ_λ` of `Z_λ`.

One can therefore suppose that there exists an affine scheme `Z'` of finite type over `Y` and a point `ξ'` of `Z'` such
that `A' = 𝒪_{Z', ξ'}`, and that, if one sets `T' = X ×_Y Z'`, there exists a point `t' ∈ T'` whose projections in `Z'`
and `X` are `ξ'` and `x`, and such that `ℱ ⊗_Y Z'` is `Z'`-flat at the point `t'`. Let `Z'_1` (resp. `X_1`) be a closed
subprescheme of `Z'` (resp. `X`) having as underlying space the closure of `{ξ'}` (resp. `{x}`), and set
`T'_1 = X_1 ×_Y Z'_1`. The set `U` of points of `T'_1` where `ℱ ⊗_Y Z'` is `Z'`-flat is open in `T'_1` `(11.1.1)` and
contains `t'`, hence

<!-- original page 149 -->

`V = U ∩ T'_1` is non-empty open in `T'_1`. The ring `A`, being artinian, is a Jacobson ring, hence `(10.4.6)` `Z'_1`
and `T'_1` are Jacobson preschemes; consequently there exists in `V` a point `t'_0` closed in `V`, and its image `z'_0`
in `Z'_1` is a closed point of `Z'_1` `(10.4.7)`. Let `f_1` be the restriction of `f` to `X_1`, `h : T'_1 → Z'_1` the
canonical projection; `V ∩ h⁻¹(z'_0)` is a non-empty open set in `f_1⁻¹(y) ⊗_{k(y)} k(z'_0)`, and as this latter
prescheme is flat over `f_1⁻¹(y)`, a maximal point `t'_1` of `V ∩ h⁻¹(z'_0)` is necessarily above the unique maximal
point `x` of `X_1` `(2.3.4)`. Finally, `k(t'_1)` is a *finite* extension of `k` `(I, 6.4.2)` and the homomorphism
`A = 𝒪_{Y, y} → A' = 𝒪_{Z', z'}` factors as `𝒪_{Y, y} → 𝒪_{Z', z'_0} → 𝒪_{Z', z'}`, hence its kernel is contained in
that of `𝒪_{Y, y} → 𝒪_{Z', z'_0}`. This completes the announced reduction.

**II)** *Reduction to the case where the `A'_α` are finite in number and are finite `A`-algebras.* — Let `𝔪'_α` be the
maximal ideal of `A'_α`; as `A'_α` is a Noetherian local ring, the intersection of the `𝔪'_α^n` is `0` `(0_I, 7.3.5)`;
the intersection of the `u_α⁻¹(𝔪'_α^n)` for all indices `n` and `α` is thus equal to the intersection of the kernels of
the `u_α`, hence is reduced to `0` by hypothesis (i). Since `A` is artinian, there is already a finite number of these
ideals whose intersection is `0`; denote them `u_i⁻¹(𝔪'_i^{n_i})` (`1 ≤ i ≤ r`). As the `A'_i` are Noetherian, the
`𝔪'_i^{n_i}/𝔪'_i^{n_i+1}` are `(A'_i/𝔪'_i)`-modules of finite length, and as `A'_i/𝔪'_i` is an `A`-vector space of
finite rank, one sees that `A''_i = A'_i/𝔪'_i^{n_i}` is a finite `A`-algebra and a local artinian ring. The announced
reduction thus results from `(2.1.4)`.

**III)** *End of the proof.* — Suppose from now on that the `A'_i` (`1 ≤ i ≤ r`) are finite in number and are finite
`A`-algebras. For every `i`, the residue field `k_i` of `A'_i` is a finite extension of `k`; using hypothesis (ii), one
concludes that the inverse image of `x` in `X'_i` is reduced to the single point `x'_i` `(4.3.2)`. Let `Y'` be the sum
prescheme of the `Y'_i`, `X' = X ×_Y Y'`, the sum of the `X'_i`, `ℱ' = ℱ ⊗_{𝒪_Y} 𝒪_{Y'}`. The hypothesis implies that
`ℱ'` is `Y'`-flat at the points of the inverse image of `x` by the projection `p : X' → X`. As `p` is of finite type,
there exists consequently an open set `U' ⊃ p⁻¹(x)` such that `ℱ'` is `Y'`-flat at the points of `U'` `(11.1.1)`.
Moreover, the morphism `Y' → Y` is finite since the `A'_i` are finite `A`-algebras; hence `p` is a finite morphism
`(II, 6.1.5)`, consequently closed `(II, 6.1.10)`, and there exists therefore an affine neighbourhood `U` of `x` in `X`
such that `p⁻¹(U) ⊂ U'`. Let `B` and `A'` be the rings of the schemes `U` and `Y'` (`A'` being the direct product of the
`A'_i`); replacing `X` by `U`, one has thus `ℱ = M̃`, where `M` is a `B`-module, and by hypothesis `M' = M ⊗_A A'` is a
flat `A'`-module `(2.1.2)`; as the homomorphism `A → A'` is injective by construction, one can apply `(11.4.3)`, which
proves that `M` is a flat `A`-module. Q.E.D.

**Proposition (11.4.12).**

<!-- label: IV.11.4.12 -->

*Let `A` be a local artinian ring of residue field `k`, `Y = Spec(A)`, `f : X → Y` a morphism locally of finite type,
`ℱ` a coherent `𝒪_X`-Module. Let `(A'_α)` be a family of local rings, and for each `α`, `u_α : A → A'_α` a ring
homomorphism. Set `Y'_α = Spec(A'_α)`, `X'_α = X ×_Y Y'_α`, `f'_α = f_{(Y'_α)}`, `ℱ'_α = ℱ ⊗_A A'_α`. Let `x` be a point
of `X`, and suppose the following conditions verified:*

*(i) The intersection of the kernels of the `u_α` is reduced to `0`.*

*(ii) For every `α`, `ℱ'_α` is `f'_α`-flat at all points `x'_α ∈ X'_α` whose respective projections in `X` and `Y'_α`
are `x` and the closed point `y'_α` of `Y'_α`.*

*Then `ℱ` is `f`-flat at the point `x`.*

<!-- original page 150 -->

By hypothesis, the intersection of the kernels of the `u_α` is reduced to `0`; as `A` is artinian, there already exists
a finite number of these kernels whose intersection is `0`, hence one can restrict to the case where the family `(A'_α)`
is finite. Let `k'` be an algebraic closure of `k`; one knows `(0_III, 10.3.1)` that there exists a local homomorphism
`A → B` making `B` a flat `A`-module, such that `B` is a local artinian ring, integral over `A`, and that `B ⊗_A k` is
isomorphic to `k'`. By flatness, the kernels of the homomorphisms `B → B'_α = B ⊗_A A'_α` are deduced from those of the
`u_α` by tensorisation with `B`, and as they are finite in number, their intersection is reduced to `0` `(0_I, 6.1.3)`.
Consider the rings `B'_{αβ}`, localizations of `B'_α` at its maximal ideals; one knows
`(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1)` that the intersection of the kernels of the homomorphisms
`B'_α → B'_{αβ}` (for a given `α`) is reduced to `0`; one concludes that the intersection of the kernels of the composed
homomorphisms `v_{αβ} : B → B'_α → B'_{αβ}` (`α` and `β` variable) is reduced to `0`. On the other hand, as `B` is
integral over `A`, `B'_α` is integral over `A'_α`, hence its maximal ideals are above the maximal ideal of `A'_α`. If
one sets `Z'_{αβ} = Spec(B'_{αβ})`, `T'_{αβ} = X'_α ×_{Y'_α} Z'_{αβ}`, `f'_{αβ} = f'_{α(Z'_{αβ})}`, `𝒢 = ℱ ⊗_A B` and
`𝒢_{αβ} = 𝒢 ⊗_B B'_{αβ}`, one sees thus that hypotheses (i) and (ii) are still verified when one replaces respectively
`A`, `A'_α`, `u_α`, `ℱ` and `x` by `B`, `B'_{αβ}`, `v_{αβ}`, `𝒢` and a point `t` of `T = X ⊗_A B` above `x`. As the
residue field of `B` is separably closed, one deduces from `(11.4.11)` that `𝒢` is flat over `B` at the point `t`. But
since `B` is a faithfully flat `A`-module, one concludes by `(2.1.4)` that `ℱ` is flat over `A` at the point `x`, which
proves `(11.4.12)`.

**Corollary (11.4.13).**

<!-- label: IV.11.4.13 -->

*Let `A` be a local artinian ring, `Y = Spec(A)`, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent
`𝒪_X`-Module. Let `(Y'_α)` be a family of `A`-preschemes, and for every `α`, set `X'_α = X ×_Y Y'_α`,
`f'_α = f_{(Y'_α)}`, `ℱ'_α = ℱ ⊗_Y 𝒪_{Y'_α}`. Let `x` be a point of `X` and suppose the following hypotheses verified:*

*(i) The intersection of the kernels of the homomorphisms `A → Γ(Y'_α, 𝒪_{Y'_α})` corresponding to the structure
morphisms is reduced to `0`.*

*(ii) For every `α`, `ℱ'_α` is `f'_α`-flat at all points `x'_α ∈ X'_α` whose projection in `X` is `x`.*

*Then `ℱ` is `f`-flat at the point `x`.*

Indeed, for every `y'_α ∈ Y'_α`, consider the local scheme `Y''_{α, y'_α} = Spec(𝒪_{Y'_α, y'_α})`; by virtue of
`(2.1.4)`, `ℱ ⊗_Y 𝒪_{Y''_{α, y'_α}}` is `Y''_{α, y'_α}`-flat at points whose projections on `X` and `Y''_{α, y'_α}` are
`x` and the closed point of `Y''_{α, y'_α}`. Moreover, the kernel of the homomorphism `A → Γ(Y'_α, 𝒪_{Y'_α})` is the
intersection of the kernels of the homomorphisms `A → Γ(Y''_{α, y'_α}, 𝒪_{Y''_{α, y'_α}})`, for one immediately reduces
to the case where `Y'_α` is affine, and it suffices then to apply
`Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1`. Replacing the family `(Y'_α)` by the family of
`Y''_{α, y'_α}`, one is therefore reduced to `(11.4.12)`.

### 11.5. Descent of flatness by arbitrary morphisms: general case

**Theorem (11.5.1).**

<!-- label: IV.11.5.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module,
`x` a point of `X`, `y = f(x)`. Let `(Y'_α)` be a family of local `Y`-preschemes `Y'_α = Spec(A'_α)` such that the
images of the closed points `y'_α` of `Y'_α` are all equal to `y`. For every `α`, let `𝔪'_α` be the maximal ideal of
`A'_α`, and `u_α : 𝒪_y → A'_α`*

<!-- original page 151 -->

*the canonical homomorphism `(I, 2.4.4)`; suppose that the finite intersections of the ideals `u_α⁻¹(𝔪'^{n_α}_α)` form a
fundamental system of neighbourhoods of `0` in `𝒪_y`. Set `X'_α = X ×_Y Y'_α`, `f'_α = f_{(Y'_α)}`,
`ℱ'_α = ℱ ⊗_Y 𝒪_{Y'_α}`, and suppose that one of the following hypotheses is verified:*

*(i) For every `α`, `ℱ'_α` is `f'_α`-flat at all points whose projection in `X` is equal to `x` and whose projection in
`Y'_α` is equal to `y'_α`.*

*(ii) For every `α`, there exists `x'_α ∈ X'_α` whose projection on `X` is `x` and whose projection in `Y'_α` equals
`y'_α`, such that `ℱ'_α` is `f'_α`-flat at the point `x'_α`, and `k(x)` is a primary extension of `k(y)`.*

*Under these conditions, `ℱ` is `f`-flat at the point `x`.*

Let `𝔪_y` be the maximal ideal of `𝒪_y`; as `𝒪_y` and `𝒪_x` are Noetherian and `𝒪_y → 𝒪_x` is a local homomorphism, it
suffices, by virtue of `(0_III, 10.2.2)`, to prove that for every `n > 0`, `ℱ_x/𝔪_y^n ℱ_x` is a flat
`(𝒪_y/𝔪_y^n)`-module. Denote by `(𝔍_λ)` the family of finite intersections of the `u_α⁻¹(𝔪'^{n_α}_α)`; by hypothesis,
there exists `λ` such that `𝔍_λ ⊂ 𝔪_y^n`, and as `ℱ_x/𝔪_y^n ℱ_x = (ℱ_x/𝔍_λ ℱ_x) ⊗_{𝒪_y/𝔍_λ} (𝒪_y/𝔪_y^n)`, it will
suffice to prove that `ℱ_x/𝔍_λ ℱ_x` is a flat `(𝒪_y/𝔍_λ)`-module. Now, for each `α` such that `𝔍_λ ⊂ u_α⁻¹(𝔪'^{n_α}_α)`,
one has, by passage to quotients, a homomorphism `u'_α : 𝒪_y/𝔍_λ → A'_α/𝔪'^{n_α}_α`, and the intersection of the kernels
of the `u'_α` is reduced to `0`. Taking `(I, 3.6.1)` into account, one sees that one is reduced to `(11.4.11)` in case
(ii) and to `(11.4.12)` in case (i).

**Corollary (11.5.2).**

<!-- label: IV.11.5.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module,
`x` a point of `X`, `y = f(x)`; set `A = 𝒪_y`. Let `u : A → A'` be a homomorphism of `A` into a Zariski ring `A'`, such
that the inverse image `u⁻¹(𝔯')` of the radical `𝔯'` of `A'` is the maximal ideal `𝔪` of `A`; suppose moreover that the
homomorphism `û : Â → Â'` is injective. Set `Y' = Spec(A')`, `X' = X ×_Y Y'`, `f' = f_{(Y')}`, `ℱ' = ℱ ⊗_Y 𝒪_{Y'}`. For
`ℱ` to be `f`-flat at the point `x`, it is necessary and sufficient that `ℱ'` be `f'`-flat at every point whose
projection in `X` is equal to `x` and whose projection in `Y'` is equal to a closed point of `Y'`.*

*If moreover `A'` is a finite `A`-algebra, one may in what precedes replace the hypothesis that `û` is injective by the
hypothesis that `u` is injective.*

As `A` (resp. `A'`) identifies with a subring of `Â` (resp. `Â'`)
`(Bourbaki, Alg. comm., chap. III, §3, n° 3, prop. 6)`, one sees first that `u` itself is injective and that `û` is its
prolongation by continuity to `Â`.

Let `(𝔪'_α)` be the family of maximal ideals of `A'`; as one has

```text
  𝔪'^n_α Â' = 𝔪̂'^n_α,    and    𝔪̂'^n_α ∩ A' = 𝔪'^n_α,
```

and the `𝔪̂'^n_α` are open in `Â'`, one has `u⁻¹(𝔪'^n_α) = A ∩ û⁻¹(𝔪̂'^n_α)`, and it will suffice to show that in `A`,
the finite intersections of the `û⁻¹(𝔪̂'^n_α)` form a fundamental system of neighbourhoods of `0`, which will allow
application of `(11.5.1)` to the composed homomorphisms `v_α ∘ u : A → Â'_{𝔪'_α}`, where `p_α : Â' → Â'_{𝔪'_α}` is the
canonical homomorphism. As `Â`

<!-- original page 152 -->

is complete, it will suffice to show that the intersection of the `û⁻¹(𝔪̂'^n_α)` is reduced to `0`
`(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8, where one may in the proof replace the decreasing sequence by any filtered set)`.
Now, for every fixed `α`, the intersection of the `𝔪̂'^n_α Â'_{𝔪'_α}` for `n > 0` is reduced to `0` in the Noetherian
local ring `Â'_{𝔪'_α}`. On the other hand the `𝔪̂'_α` are the maximal ideals of `Â'`, hence the canonical homomorphism
`Â' → ∏_α Â'_{𝔪'_α}` is injective `(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1)`, and as by hypothesis
`û : Â → Â'` is also injective, this completes the proof in the general case. The last assertion results from the fact
that `Â` is a faithfully flat `A`-module `(0_I, 7.3.5)` and `Â' = A' ⊗_A Â` since `A'` is by hypothesis an `A`-module of
finite type `(Bourbaki, Alg. comm., chap. III, §3, n° 4, th. 3 and chap. IV, §2, n° 5, cor. 3 of prop. 9)`.

**Proposition (11.5.3).**

<!-- label: IV.11.5.3 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation,
`x` a point of `X`, `y = f(x)`, `g = (ψ, θ) : Y' → Y` a proper morphism of finite presentation. Suppose that:*

*(i) The homomorphism `θ_y : 𝒪_y → (g_*(𝒪_{Y'}))_y` is injective.*

*(ii) For every `x' ∈ X' = X ×_Y Y'` whose projection in `X` is `x`, `ℱ' = ℱ ⊗_Y 𝒪_{Y'}` is `Y'`-flat at the point
`x'`.*

*Then `ℱ` is `f`-flat at the point `x`.*

The question being local on `X`, one can suppose `f` of finite presentation. Let `p : X' → X` be the canonical
projection. As `f' = f_{(Y')} : X' → Y'` is of finite presentation `(1.6.2)` and `ℱ'` is an `𝒪_{X'}`-Module of finite
presentation `(0_I, 5.2.5)`, it results from `(11.3.1)` that the set `U'` of points of `X'` where `ℱ'` is `f'`-flat is
open. As `U'` contains `p⁻¹(x)` by hypothesis, and `p` is proper, hence closed, `U'` contains a set of the form
`p⁻¹(U)`, where `U` is a neighbourhood of `x`. Replacing `X` by `U`, one can therefore suppose already that `ℱ'` is
`f'`-flat. On the other hand, taking `(I, 3.6.5)`, `(II, 5.4.2)` and `(2.1.4)` into account, one can replace `Y` by
`Spec(𝒪_y)`, i.e. suppose that `Y = Spec(A)`, where `A` is a local ring. Under these conditions, we shall prove that `ℱ`
is `f`-flat. By virtue of `(5.13.5)`, `A` is the inductive limit of Noetherian local subrings `A_λ` such that the
canonical injection `A_λ → A` is a local homomorphism. By virtue of `(8.9.1)`, one can suppose that `X = X_λ ⊗_{A_λ} A`,
`f = f_λ ⊗ 1_A`, `ℱ = ℱ_λ ⊗_{A_λ} A`, for a suitable `λ`, `f_λ : X_λ → Y_λ = Spec(A_λ)` being a morphism of finite type,
`ℱ_λ` a coherent `𝒪_{X_λ}`-Module. Similarly, one can suppose that `Y' = Y'_λ ⊗_{A_λ} A`, `g = g_λ ⊗ 1_A`, where
`g_λ : Y'_λ → Y_λ` is a morphism of finite presentation; moreover `(8.10.5, (xii))`, one can suppose that `g_λ` is
proper. As by hypothesis the homomorphism `A → Γ(Y', 𝒪_{Y'})` is injective and `A_λ` is a subring of `A`, the
homomorphism `A_λ → Γ(Y', 𝒪_{Y'})` is also injective. Finally, by virtue of `(11.2.6)`, one can suppose `λ` taken such
that `ℱ'_λ = ℱ_λ ⊗_{Y_λ} Y'_λ` is `f'_λ`-flat, since `ℱ' = ℱ'_λ ⊗_{Y'_λ} Y'`. These remarks prove that one may from now
on suppose the ring `A` Noetherian, the other hypotheses of `(11.5.3)` being verified. Set then `B = Â`, `Z = Spec(B)`;
as `B` is a faithfully flat `A`-module `(0_I, 7.3.5)`, it amounts to the same thing to say that `ℱ` is `f`-flat or that
`ℱ ⊗_Y Z` is `Z`-flat `(2.1.4)`; similarly, if one sets `Z' = Y' ×_Y Z`, the morphism `Z' → Y'` is faithfully flat
`(2.2.13)`, hence it amounts to the same thing to say that `ℱ'` is `f'`-flat or that `ℱ' ⊗_{Y'} Z'` is `Z'`-flat;
finally `h = g_{(Z)} : Z' → Z` is proper `(II, 5.4.2)` and of finite type `(1.5.2)`, `Â` is Noetherian, and if `z` is
its

<!-- original page 153 -->

closed point, the homomorphism `Â → (h_*(𝒪_{Z'}))_z` is injective, for it results from `(2.3.1)` that
`h_*(𝒪_{Z'}) = g_*(𝒪_{Y'}) ⊗_Y Z`, and our assertion results from hypothesis (i) and from the definition of flat modules
`(0_I, 6.1.1)`.

One can therefore from now on suppose the Noetherian local ring `A` *complete*; the proof will be completed if one
proves that the intersection of the kernels of the homomorphisms `A = 𝒪_y → 𝒪_{y'}` (where `y'` runs through `g⁻¹(y)`)
is reduced to `0`. Indeed, the `𝒪_{y'}` are Noetherian local rings, hence for each `y'` the intersection of the
`𝔪_{y'}^n` (`n > 0`) is reduced to `0`; if `𝔞_{n, y'}` is the inverse image in `A` of `𝔪_{y'}^n`, the finite
intersections of the `𝔞_{n, y'}` are neighbourhoods of `0` in `A` and the intersection of all the `𝔞_{n, y'}` is reduced
to `0`; the finite intersections of the `𝔞_{n, y'}` will thus form a fundamental system of neighbourhoods of `0` in `A`
`(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8, where in the proof one may replace the decreasing sequence by any filtered set)`;
one will be able to apply `(11.5.1)`. Now, let `s ∈ A` be an element belonging to the kernel of each of the
homomorphisms `A → 𝒪_{y'}`; the image `s'` of `s` in `Γ(Y', 𝒪_{Y'})` is thus a section of `𝒪_{Y'}` over `Y'` such that
`s'_{y'} = 0` for every `y' ∈ g⁻¹(y)`; there exists consequently a neighbourhood `V` of `g⁻¹(y)` in `Y'` such that
`s' | V = 0`. But as `g` is closed, `V` contains a set of the form `g⁻¹(V')`, where `V'` is an open neighbourhood of `y`
in `Y`; now, `Y` is a local scheme, hence the only neighbourhood of the closed point `y` of `Y` is `Y` entire, in other
words `V' = Y`, `V = Y'`, `s' = 0`, and as `A → Γ(Y', 𝒪_{Y'})` is injective by hypothesis, `s = 0`. Q.E.D.

The following particular case of `(11.5.3)` will be useful to us in Chap. V:

**Corollary (11.5.4).**

<!-- label: IV.11.5.4 -->

*Let `f = (ψ, θ) : X → Y` be a proper morphism of finite presentation, and let `p : X ×_Y X → X` be the first
projection. Suppose that `θ : 𝒪_Y → f_*(𝒪_X)` is injective. Then for `f` to be flat, it is necessary and sufficient that
`p` be so.*

**Proposition (11.5.5).**

<!-- label: IV.11.5.5 -->

*Let `A` be a ring, `Y = Spec(A)`, `f : X → Y` a morphism locally of finite presentation, `ℱ` a quasi-coherent
`𝒪_X`-Module of finite presentation, `x` a point of `X`. Let `A → A'` be an injective homomorphism making `A'` an
integral algebra over `A`. Set `Y' = Spec(A')`, `X' = X ×_Y Y'`, `f' = f × 1`, `ℱ' = ℱ ⊗_Y 𝒪_{Y'}`. Then, if `ℱ'` is
`f'`-flat at every point of `X'` whose projection in `X` is equal to `x`, `ℱ` is `f`-flat at the point `x`.*

Suppose first that `A'` is a *finite* `A`-algebra of finite presentation; then the morphism `Y' → Y` is proper
`(II, 6.1.11)` and of finite presentation, hence the hypotheses of `(11.5.3)` are verified, whence the conclusion. In
the general case, the proposition will result from this particular case, from the fact that `A'` is the inductive limit
of its finite sub-`A`-algebras `A'_λ`, and from the two following lemmas:

**Lemma (11.5.5.1).**

<!-- label: IV.11.5.5.1 -->

*Every finite `A`-algebra `A'` is an inductive limit of `A`-algebras `A'_λ` which are finite and of finite
presentation.*

One argues as in `(1.9.3.1)`. Indeed one has `A' = B/𝔍`, where `B` is a finite `A`-algebra that is a free `A`-module,
and `𝔍` an ideal of `B` `(1.4.7.1)`. Now, `𝔍` is the inductive limit of the ideals `𝔍_λ ⊂ 𝔍` of `B` which are of finite
type (and *a fortiori* `A`-modules of finite type), hence, by the exactness of the functor `lim`, `A'` is the inductive
limit of the `A`-algebras `B/𝔍_λ`; now, `B/𝔍_λ` is by definition an `A`-module of finite presentation, hence also
`(1.4.7)` an `A`-algebra of finite presentation.

<!-- original page 154 -->

To apply this lemma to the situation of `(11.5.5)`, one will note moreover that if the homomorphism `A → A'` is
injective, so *a fortiori* is `A → A'_λ` for every `λ`.

**Lemma (11.5.5.2).**

<!-- label: IV.11.5.5.2 -->

*Let `A` be a ring, `A'` an `A`-algebra, `(A'_λ)` an inductive system of `A`-algebras such that `A' = lim A'_λ`; set
`Y = Spec(A)`, `Y' = Spec(A')`, `Y'_λ = Spec(A'_λ)`. Let `f : X → Y` be a morphism of finite presentation, `ℱ` a
quasi-coherent `𝒪_X`-Module of finite presentation; set `X' = X ×_Y Y'`, `f' = f_{(Y')}`, `ℱ' = ℱ ⊗_Y Y'`,
`X'_λ = X ×_Y Y'_λ`, `f'_λ = f_{(Y'_λ)}`, `ℱ'_λ = ℱ ⊗_Y Y'_λ`. Let `x` be a point of `X` such that `ℱ'` is `f'`-flat at
all points `x' ∈ X'` above `x`; then there exists `λ` such that `ℱ'_λ` is `f'_λ`-flat at every point of `X'_λ` above
`x`.*

Let `U'` be the set of `x' ∈ X'` such that `ℱ'` is `f'`-flat at the point `x'`; one knows `(11.3.1)` that `U'` is open
in `X'` since `f'` is of finite presentation `(1.6.2)`; similarly the set `U'_λ` of points of `X'_λ` where `ℱ'_λ` is
`f'_λ`-flat is open in `X'_λ`, and one knows moreover `(11.2.6)` that `U'` is the union of the `v_λ⁻¹(U'_λ)`, where
`v_λ : X' → X'_λ` is the canonical projection. Consider the scheme `T = Spec(k(x))`; set `T' = T ×_Y Y'`,
`T'_λ = T ×_Y Y'_λ`, and let `w_λ : T' → T'_λ`, `g' : T' → X'`, `g'_λ : T'_λ → X'_λ` be the canonical projections. Set
`V'_λ = g'_λ⁻¹(U'_λ)`, `V' = g'⁻¹(U') = ⋃_λ w_λ⁻¹(V'_λ)`. By hypothesis one has (taking `(I, 3.6.1)` into account)
`V' = T'`; as `T'` is quasi-compact, there exists `λ` such that `w_λ⁻¹(V'_λ) = T'`. One then deduces from `(8.3.3)`
applied to the closed quasi-compact parts `T'_λ − V'_λ` of `T'_λ`, that there exists `μ ≥ λ` such that `T'_μ = V'_μ`;
this means that `ℱ'_μ` is `f'_μ`-flat at all points of `X'_μ` whose projection in `X` is `x`. Q.E.D.

### 11.6. Descent of flatness by arbitrary morphisms: case of a unibranch base prescheme

**Theorem (11.6.1).**

<!-- label: IV.11.6.1 -->

*Let `A` be a local integral domain that is geometrically unibranch `(0, 23.2.1)`, `Y = Spec(A)`, `f : X → Y` a morphism
locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation. Let `A'` be a local ring,
`u : A → A'` an injective local homomorphism; set `Y' = Spec(A')`, `X' = X ×_Y Y'`, `f' = f_{(Y')}`, `ℱ' = ℱ ⊗_Y Y'`.
Let `x` be a point of `X` whose projection `f(x) = y` is the closed point of `Y`, `x'` a point of `X'` whose projections
in `X` and `Y'` are respectively `x` and the closed point `y'` of `Y'`. Then, if `ℱ'` is `f'`-flat at the point `x'`,
`ℱ` is `f`-flat at the point `x`.*

One can restrict to the case where `f` is of finite presentation, the question being local on `X`. We shall proceed in
several steps.

**I)** *Reduction to the case where `A` and `A'` are integrally closed local rings.*

As `u` is injective and `A` is integral, there exists a prime ideal `𝔭'` of `A'` such that `u⁻¹(𝔭') = 0` `(0_I, 1.5.8)`;
the composed homomorphism `A → A' → A'' = A'/𝔭'` is therefore injective and local, and if `Y'' = Spec(A'')`,
`X'' = X' ⊗_{A'} A'' = X ×_Y Y''`, `ℱ'' = ℱ' ⊗_{A'} A''`, `ℱ''` is `Y''`-flat at the points of `X''` above `x'`
`(2.1.4)`; replacing if necessary `A'` by `A''` and taking `(I, 3.4.7)` into account, one can therefore suppose first
that `A'` is integral. If `K'` is the field of fractions of `A'`, there exists then a valuation ring `B'` in `K'` which
dominates `A'`; the composed homomorphism `A → A' → B'` being injective and local, the same reasoning as

<!-- original page 155 -->

before allows replacement of `A'` by `B'`; one can thus suppose the local ring `A'` integrally closed, with `A` a local
subring of `A'` dominated by `A'`. Let `A_1` be the integral closure of `A`; it is clear that `A ⊂ A_1 ⊂ A'`, and by
hypothesis `A_1` is a local ring; if `𝔪`, `𝔪_1`, `𝔪'` are the maximal ideals of `A`, `A_1`, `A'`, one has
`𝔪 ⊂ 𝔪_1 ⊂ 𝔪'`; indeed, `𝔪_1` is the only prime ideal of `A_1` above `𝔪`, since `A_1` is a local ring
`(Bourbaki, Alg. comm., chap. V, §2, n° 1, prop. 1)`; as `𝔪' ∩ A = 𝔪`, one has `𝔪' ∩ A_1 ∩ A = 𝔪`, hence
`𝔪' ∩ A_1 = 𝔪_1`. Set `Y_1 = Spec(A_1)`, `X_1 = X ×_Y Y_1`, `f_1 = f_{(Y_1)}`, `ℱ_1 = ℱ ⊗_Y Y_1`, and let `x_1` be the
projection of `x'` in `X_1`; denote on the other hand by `y_1` the unique closed point of `Y_1`, so that
`y_1 = f_1(x_1)`. By hypothesis, the morphism `Spec(k(y_1)) → Spec(k(y))` is radicial, whence one concludes, by the
transitivity of fibres `(I, 3.6.4)` and `(I, 3.5.7)`, that the morphism `f_1⁻¹(y_1) → f⁻¹(y)` is radicial, and in
particular that `x_1` is the only point of `X_1` whose projections in `X` and `Y_1` are respectively `x` and `y_1`;
moreover, one has seen that `y_1` is the only point of `Y_1` whose projection in `Y` is `y`, hence `x_1` is the only
point of `X_1` whose projection in `X` is `x`. If one proves that `ℱ_1` is `f_1`-flat at the point `x_1`, one can apply
`(11.5.5)`, from which will result the conclusion. One is therefore reduced to the case where `A` itself is integrally
closed.

**II)** *Reduction to the case where `A` and `A'` are local rings of `ℤ`-algebras of finite type which are integrally
closed.*

One can consider `A'` as a filtered inductive limit of its sub-`ℤ`-algebras (integral) of finite type `B_λ`; moreover,
as `A'` is integrally closed and the integral closure of a `ℤ`-algebra of finite type is also a `ℤ`-algebra of finite
type `(7.8.3)`, one sees that `A'` is the inductive limit of its sub-`ℤ`-algebras of finite type `B_λ` *integrally
closed*; if `𝔫_λ = 𝔪' ∩ B_λ`, `A'` is also the inductive limit of the local subrings `(B_λ)_{𝔫_λ} = A'_λ` dominated by
`A'` `(5.13.3)`. For every `λ`, `B_λ ∩ A` is also the inductive limit of its sub-`ℤ`-algebras of finite type `B_{αλ}`,
hence `A = lim_{α, λ} B_{αλ}`, and as before one can replace `B_{αλ}` in this formula by its integral closure (contained
by hypothesis in `B_λ ∩ A`), then by the local ring `A_{αλ} = (B_{αλ})_{𝔪_{αλ}}`, where
`𝔪_{αλ} = 𝔪 ∩ B_{αλ} = 𝔪'_λ ∩ B_{αλ}`, so that `A_{αλ}` is dominated by `A'_λ` and by `A`. Set `Y_{αλ} = Spec(A_{αλ})`;
it results from `(8.9.1)` that there exists a sufficiently large couple `(α, λ)`, a morphism `f_{αλ} : X_{αλ} → Y_{αλ}`
of finite type and a coherent `𝒪_{X_{αλ}}`-Module `ℱ_{αλ}` such that `X = X_{αλ} ×_{Y_{αλ}} Y`, `f = f_{αλ} × 1_Y`,
`ℱ = ℱ_{αλ} ⊗_{Y_{αλ}} Y`; if `x_{αλ}` is the projection of `x` in `X_{αλ}`, it will suffice to show that `ℱ_{αλ}` is
`f_{αλ}`-flat at the point `x_{αλ}`. As `A'` is the inductive limit of the `A'_μ` for `μ ≥ λ`, `X'` is the projective
limit of `X_{αλ} ×_{Y_{αλ}} Y'_μ = X'_μ`, and one has also `ℱ' = lim ℱ'_μ`, where `ℱ'_μ = ℱ_{αλ} ⊗_{Y_{αλ}} Y'_μ`.
Applying `(11.2.6)`, one sees that one can take `μ` large enough that `ℱ'_μ` is `Y'_μ`-flat at the point `x'_μ`,
projection of `x'` in `X'_μ`, and moreover, by construction of the `A'_μ`, the projection of `x'_μ` in `Y'_μ` is the
closed point of `Y'_μ`.

**III)** *Reduction to the case where the residue field `k'` of `A'` is a finite radicial extension of the residue field
`k` of `A`.*

One can in the first place repeat the reasoning of part I) of the proof of `(11.4.11)`, taking into account the fact
that `ℤ` is a

<!-- original page 156 -->

Jacobson ring; one reduces thus to the case where `k'` is a finite extension of `k`, which one will suppose in what
follows. Let `k''` be the largest separable extension of `k` contained in `k'`, `k_1` a finite Galois extension of `k`
containing `k''`, so that `k'' ⊗_k k_1` is a direct product of fields isomorphic to `k_1`; as `k'` is a radicial
extension of `k''`, `k' ⊗_k k_1` is thus a direct product of radicial extensions of `k_1`. There exists a local ring
`A_1` that is an `A`-algebra and a free `A`-module of finite type, such that `A_1/𝔪 A_1` is `k`-isomorphic to `k_1`
`(0_III, 10.3.1.2)`; more precisely, one can suppose that `A_1 = A[T]/(r)`, where `r` is a unitary irreducible separable
polynomial of `k[T]` of degree `n`; if `R` is a unitary polynomial of `A[T]` whose canonical image is `r` (and which is
therefore of degree `n`), one can take `A_1 = A[T]/(R)`. Now, if `K` is the field of fractions of `A`, it is clear that
`R` is an irreducible separable polynomial of `K[T]`; one deduces from this first that `A_1` is an integral ring whose
field of fractions `K_1 = K[T]/(R)` is a separable extension of `K`. Moreover, if `t` is the canonical image of `T` in
`A_1`, the `t^j` (`0 ≤ j < n`) form a basis of the `A`-module `A_1`, and their images in `k_1` a basis over `k`; one
deduces from this that `d = det(Tr_{A_1/A}(t^{i+j}))` is an element of `A` whose class in `k` is `≠ 0`, and which is
consequently invertible. The same reasoning as in `(6.12.4.1, I))` then proves that the morphism `Spec(A_1) → Spec(A)`
is flat and has its fibres regular; one concludes consequently from `(6.5.4, (ii))` that `A_1` is integrally closed.
Consider then the ring `A'_1 = A' ⊗_A A_1`; it is a free `A'`-module of finite type, hence a semi-local ring
`(Bourbaki, Alg. comm., chap. IV, §2, n° 5, cor. 3 of prop. 9)`; moreover, the maximal ideals of this finite
`A'`-algebra are all above the maximal ideal `𝔪'` of `A'`, and *a fortiori* contain `𝔪 A'_1`. But
`A'_1/𝔪 A'_1 = (A'/𝔪 A') ⊗_k k_1`, and as `k_1` is a separable finite extension of `k`, the radical of `A'_1/𝔪 A'_1`
equals `(𝔪'/𝔪 A') ⊗_k k_1` `(Bourbaki, Alg., chap. VIII, §7, n° 2, cor. 2 of prop. 3)`; if `𝔫_i` (`1 ≤ i ≤ r`) are the
maximal ideals of `A'_1`, the fields `A'_1/𝔫_i` are thus the fields composing the algebra `k' ⊗_k k_1`, in other words
they are *finite radicial extensions of `k_1`*. Moreover, as `A → A'` is an injective homomorphism, so is `A_1 → A'_1`,
`A_1` being a flat `A`-module; the canonical homomorphism `A'_1 → ∏_{i=1}^r (A'_1)_{𝔫_i}` being also injective
`(Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1)`, so is the composite `A_1 → ∏_{i=1}^r (A'_1)_{𝔫_i}`. But `A_1` is
integral, and the kernels of the homomorphisms `A_1 → (A'_1)_{𝔫_i}` are finite in number; as their intersection is null,
one of them is already null. In other words, there is a `B_1 = (A'_1)_{𝔫_i}` such that the homomorphism `A_1 → B_1` is
injective and local. Set `Y'_1 = Spec(B_1)`, `X'_1 = X' ×_{Y'} Y'_1`; `ℱ'_1 = ℱ' ⊗_{Y'} Y'_1` is `Y'_1`-flat at all
points of `X'_1` above `x'`; moreover the maximal ideal of `B_1` is the only one above `𝔪'`, hence all these points have
as projection in `Y'_1` the closed point `y'_1`. Let `x'_1` be one of these points. Set on the other hand
`Y_1 = Spec(A_1)`, `X_1 = X ×_Y Y_1`, `ℱ_1 = ℱ ⊗_Y Y_1`; if `x_1` is the projection of `x'_1` in `X_1`, the projection
of `x_1` in `X` is `x` and its projection in `Y_1` is the closed point `y_1`. If one proves that `(ℱ_1)_{x_1}` is a flat
`𝒪_{y_1}`-module, it will result that `ℱ_x` is a flat `𝒪_y`-module; indeed `𝒪_{y_1}` is a flat `𝒪_y`-module, hence
`(ℱ_1)_{x_1}` is a flat `𝒪_y`-module `(0_I, 6.2.1)`.

<!-- original page 157 -->

But `(ℱ_1)_{x_1} = ℱ_x ⊗_{𝒪_x} 𝒪_{x_1}` and `𝒪_{x_1}` is a faithfully flat `𝒪_x`-module; hence `(2.2.11, (iii))` `ℱ_x`
is a flat `𝒪_x`-module. As `X'_1 = X_1 ×_{Y_1} Y'_1`, `ℱ'_1 = ℱ_1 ⊗_{Y_1} Y'_1`, one is indeed reduced to the situation
of the statement `(11.6.1)`, with `A` and `A'` replaced respectively by `A_1` and `B_1`.

**IV)** *End of the proof.* — One is finally reduced to proving `(11.6.1)` under the following supplementary hypotheses:

(i) `A` and `A'` are local rings of `ℤ`-algebras of finite type (hence excellent rings `(7.8.3)`);

(ii) `A` is integrally closed;

(iii) the residue field `k'` of `A'` is a finite radicial extension of the residue field `k` of `A`.

One knows then (`(7.8.3)` and `(2.3.8)`) that under conditions (i) and (ii), if `𝔪` and `𝔪'` are the maximal ideals of
`A` and `A'` respectively, the `𝔪`-adic topology on `A` is induced by the `𝔪'`-adic topology of `A'`. The completion
`û : Â → Â'` is therefore an injective homomorphism. On the other hand, as the morphism `Spec(k') → Spec(k)` is
radicial, so is the morphism `f'⁻¹(y') → f⁻¹(y)` `(I, 3.5.7)`, and there is therefore only one point `x'` of `X'` whose
projections in `X` and `Y'` are `x` and `y'` respectively. One can therefore apply the result of `(11.5.2)`. Q.E.D.

**Corollary (11.6.2).**

<!-- label: IV.11.6.2 -->

*Let `A` be a unibranch local integral ring, `Y = Spec(A)`, `f : X → Y` a morphism locally of finite presentation, `ℱ` a
quasi-coherent `𝒪_X`-Module of finite presentation. Let `A'` be a local ring, `A → A'` an injective local homomorphism;
set `Y' = Spec(A')`, `X' = X ×_Y Y'`, `f' = f_{(Y')}`, `ℱ' = ℱ ⊗_Y Y'`. Let `x` be a point of `X` whose projection
`f(x) = y` is the closed point of `Y`; suppose that `ℱ'` is `f'`-flat at all points `x'` of `X'` whose projections in
`X` and `Y'` are respectively `x` and the closed point `y'` of `Y'`. Then `ℱ` is `f`-flat at the point `x`.*

One can indeed retake part I) of the proof of `(11.6.1)`, which proves (with the same notations) that if `ℱ_1` is
`f_1`-flat at all points `x_1` of `X_1` whose respective projections in `X` and `Y_1` are `x` and `y_1`, then `ℱ` is
`f`-flat at the point `x`; one is thus reduced to the case where `A` is integrally closed, hence geometrically
unibranch, and the conclusion then results from `(11.6.1)`.

### 11.7. Counter-examples

**(11.7.1)** Let us consider first the case where `A` is a local artinian ring, and where the hypotheses of `(11.4.11)`
are satisfied except condition (ii) concerning the residue field `k` of `A`. We shall see that the conclusion of
`(11.4.11)` may then fail. Let `k` be a field admitting a Galois extension `k'` of degree `[k' : k] > 1`, and denote by
`Γ` the Galois group of `k'`. Let `A` be a `k`-algebra having a basis of 3 elements `1`, `a`, `b` with the
multiplication table `a² = ab = ba = b² = 0`, so that `A` is a local artinian ring whose maximal ideal `𝔪 = ka + kb` is
of square zero. Let `A' = A ⊗_k k'`, which is a `k'`-algebra of basis `1`, `a`, `b`, a local artinian ring of maximal
ideal `𝔪' = k'a + k'b = 𝔪 A'`, of square zero; `A` identifies canonically with a subring of `A'`. Let `𝔍` be the
sub-`A'`-vector space of `𝔪'` generated by `a + γb`, where `γ ∈ k'` does not belong to `k`; it is clear that `𝔍` is an
ideal of `A'`. Set `B = A'/𝔍`; this is an artinian ring which is a non-flat `A`-module; otherwise
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, `B` would be a free `A`-module; as `A'` is also a free
`A`-module, and the canonical homomorphism `A/𝔪 A' → B/𝔪 B` is bijective, the canonical homomorphism `A' → B = A'/𝔍`
would also

<!-- original page 158 -->

be bijective `(loc. cit., n° 2, cor. of prop. 6)`, which is absurd. In other words, if one sets `Y = Spec(A)`,
`X = Spec(B)`, `𝒪_X` is not `Y`-flat at the unique point `x` of `X`. But let `A_1 = B`, `Y_1 = Spec(A_1)`, and consider
the canonical homomorphism `A → A_1`, which is local and injective since `𝔍 ∩ A = 0`; if `B_1 = B ⊗_A A_1 = B ⊗_A B`, we
shall see that there exists a point of `X_1 = X ×_Y Y_1 = Spec(B_1)` where `𝒪_{X_1}` is `Y_1`-flat. For this, remark
that one has `B ⊗_A B = (A' ⊗_A A')/(Im(𝔍 ⊗_A A') + Im(A' ⊗_A 𝔍))`. Now the structure of `C' = A' ⊗_A A'` is obtained
easily; one considers the `A`-algebra product `C = ∏_{σ ∈ Γ} A'_σ`, where all the `A'_σ` are equal to `A'`, and the
canonical map `φ : A' ⊗_A A' → C` such that `φ(x ⊗ y) = (σ(x) y)_{σ ∈ Γ}` (the group `Γ` operating canonically on `A'`);
by passage to quotients, one deduces a homomorphism `C'/𝔪 C' → C/𝔪 C` which is none other than the canonical
homomorphism `k' ⊗_k k' → ∏_σ k'_σ` (with `k'_σ = k'` for all `σ ∈ Γ`); one knows that this last is bijective
`(Bourbaki, Alg., chap. VIII, §8, prop. 4)`, hence so is `φ`, since `C'` and `C` are free `A`-modules
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. of prop. 6)`. From the preceding, it follows that `B ⊗_A B` is a
semi-local `A`-algebra, direct product of the local `A`-algebras `A'/(σ(𝔍) + 𝔍)`. The one of these algebras
corresponding to the identity of `Γ` is isomorphic to `A'/𝔍`, hence is a flat `A_1`-module; but as `γ ∉ k`, there exists
at least one `σ ∈ Γ` such that `σ(𝔍) ≠ 𝔍`; then `σ(𝔍) + 𝔍 = 𝔪'`, and `A'/𝔪'` is not a flat `(A'/𝔍)`-module, since it is
the quotient of `A'/𝔍` by a non-null ideal.

**(11.7.2)** We shall now show that the result of `(11.5.4)` loses its validity when one no longer supposes `f` to be a
proper morphism (and *a fortiori* `(11.5.3)` ceases to be exact when one no longer supposes `g` proper). Let `k` be a
field, `A_0` the polynomial ring `k[S, T]`, `A` the quotient ring `A_0/A_0 ST`; `Y = Spec(A)` is therefore the reducible
curve formed by the two "coordinate axes" in the affine plane `Y_0 = Spec(A_0)`. The ring `A` admits two minimal prime
ideals `𝔭_1 = A_0 S/A_0 ST`, `𝔭_2 = A_0 T/A_0 ST`, and as `A` is reduced, it embeds canonically into `B = B_1 ⊕ B_2`,
where `B_1 = A/𝔭_1`, `B_2 = A/𝔭_2`; moreover, `B_1` identifies with `k[T]` and `B_2` with `k[S]`, hence they are
integrally closed integral rings and consequently `Z = Spec(B)` is none other than the normalization of the prescheme
`Y` relative to `R(Y)` `(II, 6.3.8)`, the sum of the two schemes `Z_1 = Spec(B_1)`, `Z_2 = Spec(B_2)`. Denote by `y` the
"double point" of `Y`, corresponding to the maximal ideal `𝔭_1 + 𝔭_2 = 𝔪` of `A`, by `z_1` and `z_2` the points of `Z`
which project to `y`, corresponding respectively to the maximal ideals `𝔫_1 = (T)` and `𝔫_2 = (S)` of `B_1` and `B_2`.
We shall denote by `X` the subprescheme of `Z` induced on the complement of `z_2` in `Z`; one has thus
`X = Spec(B_1 ⊕ (B_2)_S)`; it is immediate that the homomorphism `A → A' = B_1 ⊕ (B_2)_S` is injective, but the
corresponding morphism `f : X → Y` is *not closed* (for `f(Z_2 − {z_2})` is not closed in `Y`, although `Z_2 − {z_2}` is
closed in `X`); *a fortiori* it is not proper. We shall now see that `f` is not flat at the point `z_1`; it will suffice
to show `(0_I, 6.6.2)` that `𝒪_{z_1}` is not a faithfully flat `𝒪_y`-module, and for this it suffices to see that the
canonical homomorphism `𝒪_y → 𝒪_{z_1}` is not injective; but this is immediate since `𝒪_{z_1}` is an integral ring,
while `𝒪_y` has zero-divisors. However, the first projection `p : X ×_Y X → X` *is an isomorphism*: indeed, one has
`B_1 ⊗_A B_1 = (A/𝔭_1) ⊗_A (A/𝔭_1) = A/𝔭_1`; `(B_2)_S ⊗_A (B_2)_S = (B_2 ⊗_A B_2)_S = (B_2)_S` for the same reason, and
finally `B_1 ⊗_A (B_2)_S = 0`, since the canonical image of `S` in `B_1` is null.

**(11.7.3)** The preceding example can be generalized: one considers over a field `k` a reduced algebraic curve `Y`
admitting a single "ordinary double point" `y` (a notion to be defined later in general), and its normalization `Z`, so
that the morphism `g : Z → Y` is finite, that the restriction of `g` to `Z − g⁻¹(y)` is an isomorphism on `Y − {y}`, and
that `g⁻¹(y)` reduces to two "simple" points `z_1`, `z_2`; moreover the prescheme `g⁻¹(y)` is the sum of two preschemes
`Spec(k(z_1))`, `Spec(k(z_2))`, canonically isomorphic to `Spec(k(y))`. Let `X` be the subprescheme of `Z` induced on
the open set `Z − {z_2}`; the morphism `f : X → Y`, restriction of `g` to `X`, is not proper, otherwise `(II, 5.4.3)` so
would the canonical injection `j : X → Z`, which is not closed. The morphism `f` is radicial, for every `y' ∈ Y`, the
fibre `f⁻¹(y')` comprises only one point `x'`, `k(y') → k(x')` being an isomorphism; one concludes first that the
diagonal morphism `Δ_f : X → X ×_Y X` is bijective `(1.7.7.1)` and on the other hand, as `f` is unramified
`(17.4.2, d')`, `Δ_f` is an open immersion `(17.4.2, b')`; consequently `Δ_f` is an isomorphism, and the first
projection `p : X ×_Y X → X` the inverse isomorphism. However `f` is not flat at the point `z_1`; otherwise `𝒪_{z_1}`
would be a faithfully flat `𝒪_y`-module `(0_I, 6.6.2)`, and as `𝒪_y` contains two distinct minimal prime ideals `𝔭_1`,
`𝔭_2` (corresponding to the two "branches" of `Y` at the point `y`) there would exist in `𝒪_{z_1}` two distinct prime
ideals whose inverse images by `u : 𝒪_y → 𝒪_{z_1}` would be `𝔭_1` and `𝔭_2` `(0_I, 6.5.1)`; but this is absurd, for
`𝒪_{z_1}` has only two distinct prime ideals, `0` and the maximal ideal `𝔪_1`, and `u⁻¹(𝔪_1)` is the maximal ideal `𝔪`
of `𝒪_y`.

**(11.7.4)** One will note that in the preceding example the homomorphism `u` is injective when `Y` is irreducible (one
may for example take `Y = Spec(k[S, T]/(S(S² + T²) − (S² − T²)))`, "cubic with a double point"); one can in this case
(replacing `Y` by an affine neighbourhood of `y`) suppose that `Y = Spec(A)`, where `A` is integral, whence
`Z = Spec(B)`, where `B` is the integral closure of `A`; as `B`, `𝒪_y` and `𝒪_{z_1}` then identify with subrings of

<!-- original page 159 -->

the field of fractions of `A`, `u` is obviously injective. One will note on the contrary that the homomorphism
`û : 𝒪̂_y → 𝒪̂_{z_1}` is not injective, for `𝒪̂_{z_1}` is an integral local ring (`z_1` being a simple point), while
`𝒪̂_y` has two distinct minimal prime ideals (corresponding to the two "branches" of `Y`) and thus has zero-divisors.
This gives an example showing that in the statement `(11.5.2)`, one cannot replace the hypothesis that `û` is injective
by the hypothesis that `u` itself is injective, even when `A'` is a local ring. It suffices indeed to take (with the
preceding notations) `A = 𝒪_y`, `A' = 𝒪_{z_1}`, `Y = Spec(A)`, `X = Spec(A')`; the reasoning of `(11.7.3)` still proves
that the first projection `p : X ×_Y X → X` is an isomorphism, although `f` is not flat at the point `z_1`.

**(11.7.5)** The examples of `(11.7.2)` and `(11.7.3)` explain the restriction to unibranch local rings in `(11.6.1)`
and `(11.6.2)`. We shall now see that in `(11.6.1)` one cannot weaken the hypothesis on `A` by supposing only `A`
unibranch. Consider indeed the complete local integral ring `A = ℝ[[U, V]]/(U² + V²)` which is unibranch but not
geometrically unibranch `(6.5.11)`. One knows `(loc. cit.)` that if `u`, `v` are the images of `U` and `V` in `A`, the
integral closure of `A` is `Ā = A[t]` with `t = v/u`, such that `t² = −1`, so that `Ā` is isomorphic to `ℂ[[U]]`. Set
`Y = Spec(A)`, `X = Spec(Ā)` (normalization of `Y` `(II, 6.3.8)`) and let `y` and `x` be the closed points of `Y` and
`X` respectively; we shall show that for a suitable local `A`-algebra `A'`, if one sets `Y' = Spec(A')`,
`X' = X ×_Y Y'`, and if `y'` denotes the closed point of `Y'`, `𝒪_{X'}` is `Y'`-flat at a point of `X'` whose
projections in `X` and `Y'` are respectively `x` and `y'`, but is not `Y'`-flat at all points having these projections;
it will follow `(2.1.4)` that `𝒪_X` is not `Y`-flat at the point `x` (which is otherwise trivial *a priori*, `Ā` not
being a free `A`-module).

Let `B = A ⊗_ℝ ℂ`, isomorphic to `ℂ[[U, V]]/(U + iV)(U − iV)`; `B` has two minimal prime ideals `𝔭'`, `𝔭''` generated
respectively by `u + iv` and `u − iv`, and `𝔫 = 𝔭' + 𝔭''` is the maximal ideal of the complete local ring `B`. Let
`B̄ = Ā ⊗_ℝ ℂ`; `B̄` is a direct product of two algebras isomorphic to `ℂ[[U]]`, generated by the idempotents
`e' = (1 ⊗ 1 + t ⊗ i)/2` and `e'' = (1 ⊗ 1 − t ⊗ i)/2`; as the homomorphism `A → Ā` is injective, so is `B → B̄`, and
the images of `u + iv` and of `u − iv` by this injection are respectively `u e'` and `u e''`; one concludes at once that
`B̄` identifies canonically with `(B/𝔭') ⊕ (B/𝔭'')`. This being so, take for `A'` the local ring `B/𝔭'`; then `Ā ⊗_A A'`
identifies with `B̄ ⊗_B A'`. But one has `(B/𝔭') ⊗_B (B/𝔭') = B/𝔭'` and `(B/𝔭') ⊗_B (B/𝔭'') = B/𝔫`, hence `Ā ⊗_A A'` is
isomorphic to `A' ⊕ (B/𝔫)`. This establishes our assertion, for `B/𝔫 = A'/(𝔫/𝔭')` is not a flat `A'`-module (otherwise
it would be a free `A'`-module `(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, which is absurd).

### 11.8. A valuative criterion of flatness

**Theorem (11.8.1).**

<!-- label: IV.11.8.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation,
`x` a point of `X`, `y = f(x)`. Suppose the local ring `𝒪_y` integral (resp. reduced and Noetherian). For `ℱ` to be
`f`-flat at the point `x`, it is necessary and sufficient that, for every valuation ring (resp. every discrete valuation
ring) `A'` and every local homomorphism `𝒪_y → A'`, the following condition be satisfied: setting `Y' = Spec(A')`,
`X' = X ×_Y Y'`, `f' = f_{(Y')}`, the `𝒪_{X'}`-Module `ℱ' = ℱ ⊗_Y Y'` is `f'`-flat at all points `x'` of `X'` whose
respective projections in `X` and `Y'` are `x` and the closed point `y'` of `Y'`.*

The condition being obviously necessary `(2.1.4)`, it remains to prove that it is sufficient. One can evidently
(`(I, 3.6.5)` and `(I, 2.4.4)`) restrict to the case where `Y = Spec(A)` is the spectrum of a local ring `A` and `y` the
closed point of `Y`.

**(i)** *Case where `A` is integral.* — Let `K` be the field of fractions of `A`, `A_1` the integral closure of `A`;
setting `Y_1 = Spec(A_1)`, `X_1 = X ×_Y Y_1`, `f_1 = f_{(Y_1)}`, it suffices, by virtue of `(11.5.5)`, to show that
`ℱ_1 = ℱ ⊗_Y Y_1` is `f_1`-flat at all points `x_1` of `X_1` of which `x` is the projection in `X`. Now, if
`f_1(x_1) = y_1`, one has `y_1 = 𝔪_1`, where `𝔪_1` is a prime ideal

<!-- original page 160 -->

of `A_1` whose trace `𝔪 = 𝔪_1 ∩ A` on `A` is the maximal ideal of `A` (`𝔪_1` is moreover necessarily a maximal ideal).
Let `A'` be a valuation ring for `K` which dominates `𝒪_{y_1} = (A_1)_{𝔪_1}`; the homomorphism `A → 𝒪_{y_1}` being
local, so is `A → A'`. There exists then at least one point `x' ∈ X'` whose projections in `X_1` and `Y'` are
respectively `x_1` and `y'` `(I, 3.4.7)`; as by hypothesis `ℱ'` is `f'`-flat at the point `x'`, and `𝒪_{y_1}` is
integrally closed, one can apply `(11.6.1)`, and one deduces that `ℱ_1` is `f_1`-flat at the point `x_1`, whence the
theorem in this case.

**(ii)** *Case where `A` is reduced and Noetherian.* — Let `𝔭_i` (`1 ≤ i ≤ m`) be the minimal ideals of `A`; as `A` is
reduced, it identifies canonically with a subring of the product of the `A_i = A/𝔭_i`, which are Noetherian local rings;
setting `Y_i = Spec(A_i)`, `X_i = X ×_Y Y_i`, `f_i = f_{(Y_i)}`, it results from `(11.5.2)` that it suffices to show
that for each `i`, `ℱ_i = ℱ ⊗_Y 𝒪_{Y_i}` is `f_i`-flat at every point `x_i` of `X_i` whose projections in `X` and `Y_i`
are `x` and the closed point `y_i` of `Y_i` respectively. Now, as `A_i` is a Noetherian integral local ring, there
exists in its field of fractions `K_i` a subring `A''_i` containing `A_i`, that is a finite `A`-algebra (hence a
Noetherian semi-local ring) and whose local rings are geometrically unibranch (`(6.15.5)` and `(0, 23.2.5)`). As the
maximal ideals of `A''_i` are then necessarily above the maximal ideal of `A_i`, one deduces still from `(I, 3.4.7)` and
from `(11.5.2)` that it suffices, setting `Y''_i = Spec(A''_i)`, `X''_i = X ×_Y Y''_i`, `f''_i = f_{(Y''_i)}`, to prove
that `ℱ''_i = ℱ ⊗_Y Y''_i` is `f''_i`-flat at every point `x''_i` of `X''_i` whose projections in `X` and `Y''_i` are
`x` and the closed point `y''_i` of `Y''_i` respectively. Now, let `A'` be a discrete valuation ring for `K_i`
dominating `𝒪_{y''_i}`, and let `x'` be a point of `X'` whose projections in `X''_i` and in `Y'` are `x''_i` and `y'`
respectively `(I, 3.4.7)`; as `𝒪_{y''_i}` is geometrically unibranch, one can still apply `(11.6.1)` and one deduces
that `ℱ''_i` is `f''_i`-flat at the point `x''_i`.

**Remarks (11.8.2).**

<!-- label: IV.11.8.2 -->

*(i) In the statement of `(11.8.1)`, one can restrict to supposing that the condition on `ℱ'` is verified for complete
valuation rings `A'` whose residue field is algebraically closed.* One knows indeed that every valuation ring `A'` is
dominated by such a ring `A''` `(II, 7.1.2)`, and that if `A'` is a discrete valuation ring, one can suppose that so is
`A''` `(0_III, 10.3.1)`.

*(ii) The proof of `(11.8.1)` simplifies when one supposes not only that `A` is integral and Noetherian, but that its
completion `Â` is also integral.* Replacing `X` by `X ⊗_A Â` and reasoning as in the proof of `(11.5.3)`, one can in
this case reduce to proving `(11.8.1)` when `A = 𝒪_y` is integral, Noetherian and complete. Now, one knows `(II, 7.1.7)`
that such a ring `A` is dominated by a complete discrete valuation ring; the conclusion therefore results directly from
`(11.5.2)`.

### 11.9. Separating and universally separating families of homomorphisms of sheaves of modules

**(11.9.1)** Let `X` be a prescheme, `(f_λ)_{λ ∈ L}` a family of morphisms `f_λ : Z_λ → X`, `ℱ` a quasi-coherent
`𝒪_X`-Module; for every `λ ∈ L`, suppose given a quasi-coherent `𝒪_{Z_λ}`-Module `𝒢_λ` and a homomorphism

```text
(11.9.1.1)                u_λ : ℱ → (f_λ)_*(𝒢_λ).
```

<!-- original page 161 -->

One says that the family `(u_λ)` (or the corresponding family of `u'_λ : f_λ^*(ℱ) → 𝒢_λ`) is **separating** if the
intersection of the kernels of the `u_λ` is null. In other words, this means that for every open set `U` of `X`, and
every section `t` of `ℱ` over `U`, such that, for every `λ`, the section `u_λ(t)` (which, by definition, is a section of
`𝒢_λ` over `f_λ⁻¹(U)`) is null, then `t` is itself null.

**(11.9.2)** With the notations of `(11.9.1)`, let `M` be a second index set; for every `λ ∈ L`, let `(g_{λμ})_{μ ∈ M}`
be a family of morphisms `g_{λμ} : Z_{λμ} → Z_λ`; for every couple `(λ, μ)`, suppose given a quasi-coherent
`𝒪_{Z_{λμ}}`-Module `𝒢_{λμ}` and a homomorphism `v_{λμ} : 𝒢_λ → (g_{λμ})_*(𝒢_{λμ})`; set
`h_{λμ} = f_λ ∘ g_{λμ} : Z_{λμ} → X` and consider the composed homomorphism

```text
  ℱ ─u_λ─→ (f_λ)_*(𝒢_λ) ─(f_λ)_*(v_{λμ})─→ (h_{λμ})_*(𝒢_{λμ}).
```

Suppose that, for every `λ ∈ L`, the family `(v_{λμ})_{μ ∈ M}` is separating: then so is the family of `(f_λ)_*(v_{λμ})`
(`μ ∈ M`), as one sees at once. One concludes that, for the family `(u_λ)` to be separating, it is necessary and
sufficient that the family `((f_λ)_*(v_{λμ}) ∘ u_λ)_{(λ, μ) ∈ L × M}` be so.

**(11.9.3)** To verify that the family `(u_λ)` is separating (with the notations of `(11.9.1)`), one can evidently
reduce first to the case where `X` is affine, the property being local on `X`. One can moreover suppose that `Z_λ = X`
for every `λ ∈ L`. Indeed, let `M` be an index set, sum of a family `(M_λ)_{λ ∈ L}`, and for every `λ ∈ L`, let
`(Y_{λμ})_{μ ∈ M_λ}` be an affine open cover of `Z_λ`; let `j_{λμ} : Y_{λμ} → Z_λ` be the canonical injection and set
`𝒢_{λμ} = j_{λμ}^*(𝒢_λ) = 𝒢_λ | Y_{λμ}`. If one considers the canonical homomorphism
`v_{λμ} = ρ_{𝒢_λ} : 𝒢_λ → (j_{λμ})_*(j_{λμ}^*(𝒢_λ)) = (j_{λμ})_*(𝒢_{λμ})` relative to `j_{λμ}` `(0_I, 4.4.3.2)`, it is
immediate that for each `λ ∈ L`, the family `(v_{λμ})_{μ ∈ M_λ}` is separating. By virtue of `(11.9.2)`, one is
therefore reduced to proving that the family of composed homomorphisms `((f_λ)_*(v_{λμ})) ∘ u_λ` is separating, in other
words one is reduced to the case where the `Z_λ` are affine. But then the `(f_λ)_*(𝒢_λ)` are quasi-coherent
`𝒪_X`-Modules `(I, 1.6.2)` and by virtue of the definition, one can replace the `Z_λ` by `X` and the `𝒢_λ` by the
`(f_λ)_*(𝒢_λ)`, whence our assertion.

One will note in addition that if `L` is *finite* and the `f_λ` quasi-compact, one can, in the preceding reduction,
suppose that the `M_λ` are also finite, hence one is in this case reduced to verifying that a finite family of
homomorphisms of `ℱ` into quasi-coherent `𝒪_X`-Modules is separating.

**(11.9.4)** Let us therefore consider the case where `Z_λ = X` for every `λ`, and where `X = Spec(A)` is affine; then
one has `ℱ = M̃` and `𝒢_λ = Ñ_λ`, where `M` and `N_λ` are `A`-modules, and `u_λ = φ̃_λ`, where the `φ_λ : M → N_λ` are
`A`-homomorphisms. To say that the family `(u_λ)` is separating means then that, for every `s ∈ A`, the intersection of
the kernels of the `(φ_λ)_s : M_s → (N_λ)_s` is reduced to `0`. One says then also that the family `(φ_λ)` is
*separating*. One will note that if `L` is finite, it amounts to the same to say that the intersection of the kernels of
the `φ_λ` is `0`, for one has then `⋂_{λ ∈ L} Ker((φ_λ)_s) = (⋂_{λ ∈ L} Ker(φ_λ))_s` `(0_I, 1.3.2)`. But this relation
is no longer exact in general when `L` is infinite, and the fact that the intersection of the kernels of the `φ_λ` is
`0` *does not entail*, in general,

<!-- original page 162 -->

that the family `(φ_λ)` is separating. For example, suppose that `A` is a discrete valuation ring of maximal ideal `𝔪`,
and consider the family of homomorphisms `φ_k : A → A/𝔪^k`, whose intersection of kernels `𝔪^k` is reduced to `0`; this
family is however not separating, for the fibres of all the `𝔪^k` at the generic point `x` of `X = Spec(A)` (which is
open in `X`) are equal to `𝒪_x = k(x)`, the field of fractions of `A`, and their intersection is therefore not reduced
to `0`.

**(11.9.5)** We shall be principally concerned in what follows with the problem of base change for separating families.
The notations being those of `(11.9.1)`, consider a morphism `g : X' → X` and set `ℱ' = ℱ ⊗_{𝒪_X} 𝒪_{X'} = g^*(ℱ)`, and,
for every `λ`, `Z'_λ = Z_λ ×_X X'`, `f'_λ = f_λ × 1`, `𝒢'_λ = 𝒢_λ ⊗_{𝒪_{Z_λ}} 𝒪_{Z'_λ} = g'_λ^*(𝒢_λ)`, where
`g'_λ : Z'_λ → Z_λ` is the canonical projection. For every `λ`, denote then by `u'_λ : ℱ' → (f'_λ)_*(𝒢'_λ)` the
homomorphism obtained as follows: let

```text
  σ_λ : g^*((f_λ)_*(𝒢_λ)) → (f'_λ)_*(g'_λ^*(𝒢_λ)) = (f'_λ)_*(𝒢'_λ)
```

be the homomorphism `(f_λ)_*(ρ_{𝒢_λ})`, where `ρ` is the canonical homomorphism `(0_I, 4.4.3.2)` corresponding to
`g'_λ`. Then `u'_λ` is defined as the composite

```text
  g^*(ℱ) ─g^*(u_λ)─→ g^*((f_λ)_*(𝒢_λ)) ─σ_λ─→ (f'_λ)_*(g'_λ^*(𝒢_λ)) → (f'_λ)_*(𝒢'_λ)
```

where `σ = σ(f')*(g')` is the canonical homomorphism `(0_I, 4.4.3.3)` corresponding to `g`. One will say for short that
`u'_λ` is *deduced from `u_λ` by the base change `g`*. When `f_λ : Z_λ → X` is an affine morphism, one has
`(f'_λ)_*(𝒢'_λ) = g^*((f_λ)_*(𝒢_λ))`, and in this case one has therefore simply `u'_λ = g^*(u_λ)`.

One can also interpret `u'_λ` in the following way: it suffices to know the value of `u'_λ(t')`, when `t'` is a section
of `ℱ'` over an open set `U'` of `X`, of the particular following type: `t'` is the restriction to `U'` of the canonical
image by `Γ(U, ℱ) → Γ(g⁻¹(U), ℱ')` of a section `t` of `ℱ` over an open set `U` of `X` containing `g(U')` (these
sections in effect generating the `𝒪_{X'}`-Module `ℱ'` `(0_I, 3.7.1)`). Consider the section `u_λ(t)` of `𝒢_λ` over
`f_λ⁻¹(U)`, and its canonical image `t''` by `Γ(f_λ⁻¹(U), 𝒢_λ) → Γ(f'_λ⁻¹(f_λ⁻¹(U)), 𝒢'_λ)`; then `u'_λ(t')` is the
restriction of `t''` to `f'_λ⁻¹(U')`.

Consider in particular the case where `Z_λ` is a subprescheme induced on an open set of `X`, `𝒢_λ = j_λ^*(ℱ)`, where
`j_λ : Z_λ → X` is the canonical injection, and where `u_λ` is the canonical homomorphism
`ρ_ℱ : ℱ → (j_λ)_*(j_λ^*(ℱ)) = (j_λ)_*(𝒢_λ)` `(0_I, 4.4.3.2)` corresponding to `j_λ`. Then `Z'_λ` is induced on an open
set of `X'`, and the preceding interpretation shows that `u'_λ` is none other than the canonical homomorphism
`ρ_{ℱ'} : ℱ' → (j'_λ)_*(j'_λ^*(ℱ')) = (j'_λ)_*(𝒢'_λ)` corresponding to the canonical injection `j'_λ : Z'_λ → X'`.

**(11.9.6)** Under the conditions of `(11.9.5)`, suppose that `X` and `X'` are affine, and that one wants to prove that
for every section `t'` of `ℱ'` over `X'`, whose images by all the `u'_λ` are null, then `t'` is itself null. Then one
can again restrict to the case where `Z_λ = X` for every `λ ∈ L`. Indeed, with the notations of `(11.9.3)` and
`(11.9.5)`, if one sets `Y'_{λμ} = Y_{λμ} ×_X X'`, the homomorphism `v'_{λμ}` deduced from `v_{λμ}` by the base change
`g` is none other than the canonical homomorphism

<!-- original page 163 -->

`ρ_{𝒢'_λ} : 𝒢'_λ → (j'_{λμ})_*(j'_{λμ}^*(𝒢'_λ))` corresponding to the canonical injection `j'_{λμ} : Y'_{λμ} → Z'_λ`, as
one has seen in `(11.9.5)`. The assertion then results from the reasonings of `(11.9.2)` and `(11.9.3)`, `Y_{λμ}` and
`v_{λμ}` being replaced by `Y'_{λμ}` and `v'_{λμ}`.

One has a similar reduction when one wants to prove that the family `(u'_λ)` is separating (`X` and `X'` being affine):
this still results from `(11.9.2)` and `(11.9.3)`.

**Proposition (11.9.7).**

<!-- label: IV.11.9.7 -->

*With the notations of `(11.9.1)` and `(11.9.5)`, suppose `X = Spec(A)` and `X' = Spec(A')` affine, and suppose moreover
that `A'` is a projective `A`-module. Then, if the family `(u_λ)` is separating, every section `t'` of `ℱ'` over `X'`
whose images by all the `u'_λ` are null, is itself null.*

One has seen `(11.9.6)` that one can restrict to the case where all the `Z_λ` are equal to `X`. The proposition is then
a consequence of the following lemma:

**Lemma (11.9.7.1).**

<!-- label: IV.11.9.7.1 -->

*Let `A` be a ring, `(M_λ)_{λ ∈ L}` a family of `A`-modules, `M` an `A`-module and for each `λ`, `u_λ : M → M_λ` a
homomorphism. Suppose that the intersection of the kernels of the `u_λ` is reduced to `0`. Then, for every projective
`A`-module `N`, the intersection of the kernels of the homomorphisms `u_λ ⊗ 1 : M ⊗_A N → M_λ ⊗_A N` is reduced to `0`.*

Indeed, `N` is a direct summand of a free `A`-module `L`, and it evidently suffices to prove that the intersection of
the kernels of the homomorphisms `v_λ : M ⊗_A L → M_λ ⊗_A L` is reduced to `0`, since `u_λ ⊗ 1 : M ⊗_A N → M_λ ⊗_A N` is
the restriction of `v_λ`. But the assertion then results trivially from the hypothesis.

**Remark (11.9.8).**

<!-- label: IV.11.9.8 -->

*We do not know whether, under the hypotheses of proposition `(11.9.7)`, the family `(u'_λ)` is separating: one would
need indeed `(11.9.4)` to prove that a section `t'` of `ℱ'` over an open set `D(h') ⊂ X'` (where `h' ∈ A'`) such that
the `u'_λ(t')` are all null, is itself null. Now, one cannot apply proposition `(11.9.4)` to `D(h') = Spec(A'_{h'})`,
for from the fact that `A'` is a projective `A`-module (even free), it does not follow that `A'_{h'}` is a projective
`A`-module. For example, one may take for `A` a discrete valuation ring, for `A'` a discrete valuation ring which is a
free `A`-module of rank 2, and for `A'_{h'}` the field of fractions of `A'`.*

One has however the following result:

**Corollary (11.9.9).**

<!-- label: IV.11.9.9 -->

*Let `X` be an artinian prescheme, `g : X' → X` a flat morphism (one will note that these two conditions are satisfied
if `X` is the spectrum of a field and `g` an arbitrary morphism). Then, with the notations of `(11.9.1)` and `(11.9.5)`,
if the family `(u_λ)` is separating, so is the family `(u'_λ)`.*

One can evidently restrict to the case where `X = Spec(A)` is the spectrum of a local artinian ring `A` `(I, 6.2.2)`;
one notes then that for every affine open set `U' = Spec(A')` of `X'`, `A'` is a flat `A`-module, hence projective
`(0_III, 10.1.3)`. It suffices therefore to apply `(11.9.7)` to every affine open set of `X'` to obtain the corollary.

**Theorem (11.9.10).**

<!-- label: IV.11.9.10 -->

*Let `X` be a prescheme, `(u_λ)` a family of homomorphisms `(11.9.1.1)`, `g : X' → X` a morphism, `(u'_λ)` the family of
homomorphisms deduced from `(u_λ)` by the base change `g` `(11.9.5)`.*

*(i) If `g` is a faithfully flat morphism and if the family `(u'_λ)` is separating, then the family `(u_λ)` is
separating.*

<!-- original page 164 -->

*(ii) Suppose that `g` is a flat morphism, and moreover that one of the two following conditions is verified:*

*a) `L` is finite and the `f_λ` are quasi-compact.*

*b) The morphism `g` is locally of finite presentation.*

*Then, if the family `(u_λ)` is separating, so is the family `(u'_λ)`.*

(i) By virtue of `(2.2.8)`, it suffices to show that if a section `t` of `ℱ` over an open set `U` of `X` belongs to the
kernel of each of the `u_λ`, its image `t'` by the canonical homomorphism
`Γ(ρ) : Γ(U, ℱ) → Γ(g⁻¹(U), g^*(ℱ)) = Γ(U, g_*(g^*(ℱ)))` is null. Now the images of `t'` by the `g^*(u_λ)` are the
images of the `u_λ(t)` by the homomorphism `Γ(U, (f_λ)_*(𝒢_λ)) → Γ(g⁻¹(U), g^*((f_λ)_*(𝒢_λ)))`, hence are null, and *a
fortiori* one has `u'_λ(t') = 0` for every `λ`, hence `t' = 0` by hypothesis, which proves (i).

(ii) The question being local on `X` and `X'`, one can restrict to the case where `X = Spec(A)` and `X' = Spec(A')` are
affine, `A'` being a flat `A`-module, and to proving that, for every section `z'` of `ℱ'` over `X'` whose images by all
the `u'_λ` are null, then `z'` is itself null. One has moreover seen `(11.9.6)` that one can then suppose `Z_λ = X` for
every `λ`.

Let us distinguish now the two cases.

**a)** If `L` is finite and the `f_λ` quasi-compact, one has seen `(11.9.3)` that one can again reduce to the case where
`Z_λ = X` for every `λ ∈ L`, and where moreover `L` is finite. It then amounts to the same to say that the intersection
of the kernels of the `u_λ : ℱ → 𝒢_λ` is null, or that the homomorphism `u = (u_λ) : ℱ → 𝒢 = ⊕ 𝒢_λ` is injective. As
`u' = g^*(u)` is injective since `g` is flat, the proposition is proved in this case.

**b)** Let `ℱ = M̃`, `𝒢_λ = Ñ_λ`, and set `M' = M ⊗_A A'`, `N'_λ = N_λ ⊗_A A'`, so that `ℱ' = M̃'`, `𝒢'_λ = Ñ'_λ`; by
abuse of language, we shall still denote by `u_λ` the homomorphism `M → N_λ`, and `u'_λ` the homomorphism
`u_λ ⊗ 1 : M' → N'_λ`. Let us give ourselves an element `z' ∈ M'` such that `u'_λ(z') = 0` for every `λ`; the question
is to prove that one has `z' = 0`. Now, the hypothesis that `g` is flat and of finite presentation implies, by
`(11.3.15)`, that there exists a finite sequence `(s_i)_{1 ≤ i ≤ n}` of elements of `A`, such that, setting
`𝔍_i = s_1 A + ⋯ + s_i A`, and `A_i = A_{s_i}/𝔍_{i-1} A_{s_i}`, the ring `A'_i = A' ⊗_A A_i` is a free `A_i`-module for
`1 ≤ i ≤ n`, and `𝔍_n = A`. The proposition will be established if we prove for `1 ≤ i ≤ n` the following assertion:

*(\*\_i) There exists an integer `m_i > 0` such that `s_j^{m_i} z' = 0` for `j ≤ i`.*

Indeed, setting then `k = m_n` and noting that the `s_i^k` (`1 ≤ i ≤ n`) also generate the unit ideal of `A`, the
assertion `(*_n)` will show that `z'`, a linear combination of the `s_i^k z'`, is null.

Let us prove `(*_i)` by induction on `i`, the assertion being empty for `i = 0`. Suppose therefore `i > 0` and let `m`
be a common multiple of the `m_j` for `j ≤ i − 1`. Remark that (for `1 ≤ h ≤ n`) if `𝔍'_h` is the ideal generated by the
`s_j^m` (`1 ≤ j ≤ h`), `𝔍'_h/𝔍_h` is nilpotent; to replace the `s_j` by `s_j^m` for `1 ≤ j ≤ n` amounts therefore to
replacing, for `1 ≤ h ≤ n`, `A_h` by `A_{s_h}/𝔍'_{h-1} A_{s_h} = B_h`, so that `A_h = B_h/(𝔍_{h-1}/𝔍'_{h-1})B_h`; as
`A'` is a flat `A`-module, it results from `(0_III, 10.1.2)` that `B'_h = A' ⊗_A B_h` is still a free `B_h`-module. One
can therefore

<!-- original page 165 -->

replace all the `s_j` (`1 ≤ j ≤ n`) by `s_j^m` without changing the properties of the `𝔍_h` and of the `A_h`, and
suppose henceforth that `m = 1`. Then `z'`, being annihilated by `𝔍_{i-1}`, identifies with an element of
`Hom_{A'}(A'/𝔍_{i-1} A', M')`, and as `𝔍_{i-1} A'` is an ideal of finite type of `A'`, this module of homomorphisms
identifies itself with `Hom_A(A/𝔍_{i-1}, M) ⊗_A A'` `(0_I, 6.2.2)`. Let
`v_λ = Hom(1, u_λ) : Hom_A(A/𝔍_{i-1}, M) → Hom_A(A/𝔍_{i-1}, N_λ)` be the homomorphism deduced from `u_λ`; the family
`(v_λ)` is also separating. Indeed, for every `t ∈ A`, one has
`(Hom_A(A/𝔍_{i-1}, M))_t = Hom_{A_t}(A_t/(𝔍_{i-1})_t, M_t)` and likewise replacing `M` by `N_λ`, since the ideal
`𝔍_{i-1}` is of finite type `(0_I, 1.3.5)`; as by hypothesis the intersection of the kernels of the `(u_λ)_t` is null,
so is the intersection of the kernels of the `(v_λ)_t = Hom(1, (u_λ)_t)`, whence our assertion `(11.9.4)`. Replacing `A`
by `A/𝔍_{i-1}`, `M` by `Hom_A(A/𝔍_{i-1}, M)`, `N_λ` by `Hom_A(A/𝔍_{i-1}, N_λ)` (which are `(A/𝔍_{i-1})`-modules), `u_λ`
by `v_λ` and finally `A'` by `A'/𝔍_{i-1} A'`, one sees that one can reduce to the case where, in the initial situation,
the element `s = s_i ∈ A` is such that `A'_s` is a free `A_s`-module. Now, the family of `(u_λ)_s : M_s → (N_λ)_s` is
separating by hypothesis; as one has `(u'_λ)_s(z'/1) = 0`, it results from `(11.9.7)` that one has `z'/1 = 0` in `M'_s`;
but this means that there exists an integer `r` such that `s^r z' = 0` in `M'`, which completes the proof of `(*_i)` by
induction.

**Remark (11.9.11).**

<!-- label: IV.11.9.11 -->

*Let us restrict ourselves for simplicity to the case where `Z_λ = X` for every `λ`. It must be noted that if the family
of homomorphisms `u_λ : ℱ → 𝒢_λ` is separating, it does not necessarily follow that, for every `x ∈ X`, the intersection
of the kernels of the homomorphisms `(u_λ)_x : ℱ_x → (𝒢_λ)_x` is reduced to `0`.* For example, let `X` be a Jacobson
locally Noetherian prescheme, of dimension `≥ 1`, and `ℱ` a coherent `𝒪_X`-Module; for every closed point `x` of `X`,
and every integer `n ≥ 0`, `𝔪_x^n ℱ` is a coherent `𝒪_X`-Module of support contained in `‾{x}`. The family of canonical
homomorphisms `ℱ → ℱ/𝔪_x^n ℱ` (where `x` runs through the set `X_0` of closed points of `X` and `n` the set of integers
`≥ 0`) is separating: indeed, if `t` is a section of `ℱ` over an open set `U` of `X` whose images in the
`Γ(U, ℱ/𝔪_x^n ℱ)` are all null, it follows at once that for every closed point `x ∈ U`, one has `t_x = 0`; as the set of
closed points contained in `U` is very dense in `U`, this implies `t = 0` `(10.2.1)`. However, if one takes `ℱ = 𝒪_X`,
and if `y ∈ X` is a non-closed point of `X`, one has `(𝒪_X/𝔪_x^n 𝒪_X)_y = 0` for every closed point `x` of `X`, but
`𝒪_{X, y} ≠ 0`, and the intersection of the kernels of the homomorphisms `𝒪_{X, y} → (𝒪_X/𝔪_x^n 𝒪_X)_y` is equal to
`𝒪_{X, y}`.

**Lemma (11.9.12).**

<!-- label: IV.11.9.12 -->

*The notations being those of `(11.9.1)` and `(11.9.5)`, suppose the family `(u_λ)` separating; suppose moreover that
`X` is an `S`-prescheme, where `S = Spec(A)` is an affine scheme, and that `X' = X ×_S S'`, where `S' = Spec(A')`, `A'`
being an `A`-algebra; suppose finally that the `𝒢_λ` are `S`-flat. Let `(A'_α)_{α ∈ I}` be the filtered family of
sub-`A`-algebras of finite type of `A'`; for every `α ∈ I`, set `S'_α = Spec(A'_α)`, `X'_α = X ×_S S'_α`,
`Z'_{αλ} = Z_λ ×_X X'_α`, and let `f'_{αλ} : Z'_{αλ} → X'_α`, `ℱ'_α`, `𝒢'_{αλ}` and `u'_{αλ}` be the morphisms, Modules
and homomorphisms of Modules deduced from `f_λ`, `ℱ`, `𝒢_λ` and `u_λ` by the base change `X'_α → X`. Then, if, for every
`α ∈ I`, the family `(u'_{αλ})_{λ ∈ L}` is separating, so is `(u'_λ)_{λ ∈ L}`.*

It is a matter of proving that if a section `t'` of `ℱ'` over an affine open set `U'`

<!-- original page 166 -->

of `X'` is such that `u'_λ(t') = 0` for every `λ ∈ L`, one has `t' = 0`. If `h_α : X' → X'_α` is the canonical
projection, it results from `(8.2.11)` that there exists an index `α` and a quasi-compact open set `U'_α ⊂ X'_α` such
that `U' = h_α⁻¹(U'_α)`; moreover, by virtue of `(8.5.2, (i))`, one can suppose that there is a section `t'_α` of `ℱ'_α`
over `U'_α` such that `t'` is the canonical image of `t'_α`. Up to replacing `S`, `X`, `Z_λ`, `f_λ`, `ℱ`, `𝒢_λ` and
`u_λ` by `S'_α`, `U'_α`, `f_α^{-1}(U'_α)` and the corresponding restrictions of `ℱ'_α`, `𝒢'_{αλ}` and `u'_{αλ}`, one can
therefore suppose that `U' = X'`, that `t'` is the canonical image of a section `t` of `ℱ` over `X` and that the
homomorphism `A → A'` is injective, or equivalently, if `p : S' → S` is the corresponding morphism, that the
homomorphism `𝒪_S → p_*(𝒪_{S'})` involved in the definition of `p` is injective. It follows at once by virtue of the
flatness of `𝒢_λ` over `S` (and reducing for example to the case where `Z_λ` is affine over `S` `(I, 1.6.3 and 1.6.5)`)
that the canonical homomorphism `ρ : 𝒢_λ → (g'_λ)_*(𝒢'_λ)` is also injective. But the composed homomorphism

```text
  Γ(X, ℱ) → Γ(Z_λ, 𝒢_λ) → Γ(Z_λ, (g'_λ)_*(𝒢'_λ))
```

is equal by definition to the composed homomorphism

```text
  Γ(X, ℱ) ─Γ(ρ)─→ Γ(X', ℱ') → Γ(Z'_λ, 𝒢'_λ);
```

hence the image of `t` by these composed homomorphisms is `u'_λ(t') = 0`; by virtue of the injectivity of the
homomorphism `Γ(Z_λ, 𝒢_λ) → Γ(Z'_λ, 𝒢'_λ)` one concludes that `u_λ(t) = 0` for every `λ ∈ L`, whence `t = 0` by
hypothesis, and finally `t' = 0`.

**Proposition (11.9.13).**

<!-- label: IV.11.9.13 -->

*The notations being those of `(11.9.1)` and `(11.9.5)`, suppose that `X` is a prescheme over a field `k`, and that,
setting `S = Spec(k)`, one has `X' = X ×_S S'`, where `S'` is an arbitrary `k`-prescheme. Then, if the family
`(u_λ)_{λ ∈ L}` is separating, so is `(u'_λ)`.*

One can restrict to the case where `S' = Spec(A')` is affine. If `A'` is a `k`-algebra of finite type, the morphism
`g : X' → X` is flat and of finite presentation, and one is then in the conditions of application of
`(11.9.10, (ii), b))`. In the general case, one considers `A'` as the inductive limit of its sub-`k`-algebras `A'_α` of
finite type, and one applies to each `A'_α` the result of `(11.9.10, (ii), b))`; one then concludes by means of lemma
`(11.9.12)`, since the `𝒢_λ` are `S`-flat.

**(11.9.14)** Let us keep always the notations of `(11.9.1)` and `(11.9.5)` and suppose that `X` is an `S`-prescheme. If
for every base change `g : X ×_S S' → X`, where `S' → S` is an arbitrary morphism, the corresponding family `(u'_λ)` is
separating, we shall say that the family `(u_λ)` is **universally separating relative to `S`**. When the family `(u_λ)`
is reduced to a single element `u`, we shall also say that `u` is **universally injective**, relative to `S`. It is
clear then that for every morphism `h : S' → S`, the corresponding family `(u'_λ)` is universally separating relative to
`S'`; conversely, if `h` is faithfully flat and if `(u'_λ)` is universally separating relative to `S'`, then `(u_λ)` is
universally separating relative to `S`, as results at once from `(11.9.10, (i))` and the fact that for every morphism
`S'' → S`, the corresponding morphism `S'' ×_S S' → S''` is faithfully flat.

<!-- original page 167 -->

**Proposition (11.9.15).**

<!-- label: IV.11.9.15 -->

*The notations being those of `(11.9.1)`, suppose that `X` is an `S`-prescheme, the `𝒢_λ` being `S`-flat. Let `S_0` be a
closed subprescheme of `S` defined by a quasi-coherent nilpotent Ideal `𝓙` of `𝒪_S`, such that the `(𝒪_S/𝓙)`-Modules
`𝓙^k/𝓙^{k+1}` are all locally free. Let `(u_{λ, 0})` be the family of homomorphisms obtained from the base change
`X_0 = X ×_S S_0 → X`. Then, if the family `(u_{λ, 0})` is separating (resp. universally separating relative to `S_0`),
the family `(u_λ)` is separating (resp. universally separating relative to `S`).*

Note that if `S' → S` is an arbitrary base change and `S'_0 = S' ×_S S_0`, `S'_0` is a closed subprescheme of `S'`
defined by a quasi-coherent nilpotent ideal `𝓙'` of `𝒪_{S'}` such that `𝓙'^k/𝓙'^{k+1}` is a locally free
`(𝒪_{S'}/𝓙')`-Module for every `k` `(2.1.8, (i))`; as moreover the `𝒢'_λ = 𝒢_λ ⊗_S S'` are `S'`-flat, one sees that the
assertion concerning universally separating families is a consequence of the assertion concerning separating families.
To prove this last, one can `(11.9.3)` reduce to the case where `S = Spec(A)`, `X = Spec(B)` are affine, `Z_λ = X` for
every `λ`, `ℱ = M̃`, `𝒢_λ = Ñ_λ`, where `M` and the `N_λ` are `B`-modules, the `N_λ` being flat `A`-modules. Moreover,
the question being local on `X` and `S`, it suffices to see that if `t ∈ M` is such that `u_λ(t) = 0` for every `λ`,
then `t = 0`. One has `𝓙 = 𝔍̃`, where `𝔍` is a nilpotent ideal of `A`, such that the `𝔍^k/𝔍^{k+1}` are free
`(A/𝔍)`-modules, and by hypothesis the `u_{λ, 0} : M/𝔍 M → N_λ/𝔍 N_λ` form a separating family. Suppose that
`𝔍^{n+1} = 0` (`n` integer `≥ 0`) and let us argue by induction on `n`, the assertion being trivial for `n = 0`. If `t̄`
is the class of `t` in `M/𝔍^n M`, the class of `u_λ(t)` in `N_λ/𝔍^n N_λ` is null for every `λ`, hence, by the induction
hypothesis, `t̄ = 0`, in other words one has `t ∈ 𝔍^n M`. Now `𝔍^n = 𝔍^n/𝔍^{n+1}` is a free `(A/𝔍)`-module; if `(e_α)`
is a basis of this module, one can therefore write `t = ∑_α e_α t_α`, with `t_α ∈ A/𝔍`, null except for a finite number
of indices. On the other hand, since `N_λ` is a flat `A`-module, `𝔍^n N_λ` identifies with `𝔍^n ⊗_{A/𝔍} (N_λ/𝔍 N_λ)` and
one can consequently write `u_λ(t) = ∑_α e_α u_λ(t_α) = ∑_α e_α ⊗ u_{λ, 0}(t̄_α)`. As by hypothesis `u_λ(t) = 0`, one
deduces that `u_{λ, 0}(t̄_α) = 0` for every `α` and every `λ`; whence `t̄_α = 0` for every `α` since the family
`(u_{λ, 0})` is separating, and consequently `t = 0`. Q.E.D.

**Theorem (11.9.16).**

<!-- label: IV.11.9.16 -->

*The notations being those of `(11.9.1)`, suppose that `X` is a locally Noetherian `S`-prescheme, `ℱ` a coherent
`𝒪_X`-Module and that the `𝒢_λ` are `S`-flat. For every `s ∈ S`, let `((u_λ)_s)_{λ ∈ L}` be the family obtained from
`(u_λ)` by the base change `X_s = X ×_S Spec(k(s)) → X`. Then, for the family `(u_λ)` to be universally separating
relative to `S`, it is necessary and sufficient that for every `s ∈ S`, the family `((u_λ)_s)` be separating.*

The necessity of the condition follows trivially from the definitions. Conversely, suppose the condition of the
statement verified, and let us first prove that the family `(u_λ)` is separating. One can `(11.9.3)` reduce to the case
where `S = Spec(A)`, `X = Spec(B)` are affine, `Z_λ = X` for every `λ`, `ℱ = M̃`, `𝒢_λ = Ñ_λ`, where `B` is Noetherian,
`M` is a `B`-module of finite type and the `N_λ` `A`-flat modules, and restrict to proving that, if `t ∈ M` is such that
`u_λ(t) = 0` for every `λ`, then `t = 0`. To show that `t = 0`, it suffices to prove that for every maximal ideal `𝔭` of
`B`, the image `t_𝔭` of `t` in `M_𝔭` is null `(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 1 of th. 1)`. One can
therefore restrict to showing that the intersection of the kernels

<!-- original page 168 -->

of the `(u_λ)_𝔭 : M_𝔭 → (N_λ)_𝔭` deduced from `(u_λ)` by the base change `Spec(B_𝔭) → Spec(B)` is reduced to `0`. In
other words, one is reduced to the case where `B` is a Noetherian local ring, and by considering the prime ideal of `A`
inverse image of the maximal ideal of `B`, one can also suppose that `A` is a local ring of maximal ideal `𝔪`. Then, as
`𝔪 B` is contained in the maximal ideal of `B`, and `M` is a `B`-module of finite type, the intersection of the `𝔪^n M`
is reduced to `0` `(0_I, 7.3.5)`, hence it suffices to prove that for every `n`, the image of `t` in `M/𝔪^{n+1} M` is
null. It suffices therefore to prove that the family deduced from `(u_λ)` by the base change
`Spec(B/𝔪^{n+1} B) → Spec(B)` is separating, which still means that one can restrict to the case where `A` is a local
ring whose maximal ideal `𝔪` is nilpotent. But then the `𝔪^k/𝔪^{k+1}` are free `(A/𝔪)`-modules, and by virtue of the
hypothesis on the `(u_λ)_s`, one is precisely in the conditions of application of `(11.9.15)`, whence the announced
conclusion.

Let now `h : S' → S` be a base change morphism, and `(u'_λ)` the family obtained from `(u_λ)` by the base change
`h' : X ×_S S' → X`; let us prove that `(u'_λ)` is also separating. Suppose first that `h` is *locally of finite type*;
so is then `h'`, hence `X' = X ×_S S'` is locally Noetherian; moreover, if `s' ∈ S'` is above the point `s ∈ S`, it
results from `(11.9.13)` applied to `X_s` and to `X_{s'} = X_s ⊗_{k(s)} k(s')` that, for every `s' ∈ S'`, the family
`((u'_λ)_{s'})` is separating; one can consequently conclude from the first part of the proof that in this case `(u'_λ)`
is separating.

Finally, if `h` is arbitrary, one can evidently limit oneself to the case where `S = Spec(A)` and `S' = Spec(A')` are
affine, and consider `A'` as the inductive limit of its sub-`A`-algebras of finite type. As the `𝒢_λ` are `S`-flat, it
suffices to apply what precedes and lemma `(11.9.12)` to complete the proof.

**Proposition (11.9.17).**

<!-- label: IV.11.9.17 -->

*Let `f : X → S` be a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation
and `f`-flat, `U` an open set of `X`, `j : U → X` the canonical injection, `u : ℱ → j_*(j^*(ℱ))` the canonical
homomorphism `(0_I, 4.4.3.2)`. For every `s ∈ S`, let `X_s` be the fibre `X ×_S Spec(k(s))`, `U_s` the open set
`U ∩ X_s` of `X_s`, `ℱ_s = ℱ ⊗_{𝒪_S} k(s)`, `j_s : U_s → X_s` the canonical injection,
`u_s : ℱ_s → (j_s)_*((j_s)^*(ℱ_s))` the canonical homomorphism. For `u` to be universally injective relative to `S`, it
is necessary and sufficient that `u_s` be injective for every `s ∈ S`.*

There remains only to prove the sufficiency of the condition. When `X` is locally Noetherian, the proposition is an
immediate corollary of `(11.9.16)`. We shall reduce to this case in two steps, restricting ourselves, as one can
evidently do, to the case where `S = Spec(A)` and `X` are affine.

**A)** *Case where `U` is quasi-compact.* — We shall use the following lemma:

**Lemma (11.9.17.1).**

<!-- label: IV.11.9.17.1 -->

*Under the general hypotheses of `(11.9.17)`, and supposing in addition `S` and `X` affine and `U` quasi-compact, the
set `E` of `s ∈ S` such that `u_s` is injective is constructible.*

Indeed, the fibres `X_s` are locally Noetherian preschemes, hence `E` can also, by virtue of `(5.10.2)`, be defined as
the set of `s ∈ S` such that `Ass(ℱ_s) ⊂ U_s`. Note moreover that `U`, being quasi-compact in an affine scheme, is
constructible. Then, the verification of condition `(9.2.1, (i))` follows at once from `(4.2.7)`; on the other

<!-- original page 169 -->

hand, the verification of `(9.2.1, (ii))` is made easily by using the study of associated prime cycles in the
neighbourhood of the generic fibre `(9.8.3)`, as well as `(9.5.2)` and `(9.5.3)`.

This lemma being established, one can, by virtue of `(8.9.1)` and `(8.2.11)`, suppose that there exists a Noetherian
subring `A_0` of `A`, a prescheme of finite type `X_0` over `S_0 = Spec(A_0)`, an open set `U_0` of `X_0` and a coherent
`𝒪_{X_0}`-Module `ℱ_0` such that `X = X_0 ×_{S_0} S` and that, if `p_0 : X → X_0` is the canonical projection, one has
`U = p_0⁻¹(U_0)` and `ℱ = p_0^*(ℱ_0)`. Let `(A_α)` be the filtered family of subrings of `A` which are `A_0`-algebras of
finite type, and set `X_α = X_0 ×_{S_0} S_α`, `U_α = U_0 ×_{S_0} S_α`, `ℱ_α = ℱ_0 ⊗_{S_0} S_α`; let `u_α` be the
canonical homomorphism relative to `ℱ_α` and `U_α`, defined as in `(11.9.17)`. For every `s ∈ S`, the hypothesis that
`u_s` is injective implies that `(u_α)_{s_α}` is also so `(11.9.10, (i))`, where `s_α = q_α(s)` is the image of `s` by
the morphism `q_α : S → S_α`. If `E_α` is the set of `s_α ∈ S_α` such that `(u_α)_{s_α}` is injective, one has therefore
`S = q_α⁻¹(E_α)`, and the `E_α` form a projective system of sets. But lemma `(11.9.17.1)` applied to `u_α`, shows that
`E_α` is constructible in `S_α`; one deduces therefore from `(8.3.4)` that there exists an index `α` such that
`E_α = S_α`. But then, as `X_α` is Noetherian, `u_α` is universally injective by virtue of `(11.9.16)`, hence so is `u`.

**B)** *General case.* — The open set `U` is a filtered increasing union of quasi-compact open sets `U_λ`; if
`j_λ : U_λ → X` is the canonical injection and `u_λ : ℱ → (j_λ)_*((j_λ)^*(ℱ))` the corresponding homomorphism, it
results from lemma `(11.9.17.1)` that the set `E_λ` of `s ∈ S` such that `(u_λ)_s` is injective is constructible. On the
other hand, for `s ∈ S`, to say that `u_s` (resp. `(u_λ)_s`) is injective means that `Ass(ℱ_s) ⊂ U ∩ X_s` (resp.
`Ass(ℱ_s) ⊂ U_λ ∩ X_s`) `(5.10.2)`. As `Ass(ℱ_s)` is finite `(3.1.6)`, to say that `u_s` is injective therefore means
that there exists `λ` such that `s ∈ E_λ`; the hypothesis means consequently that `S = ⋃_λ E_λ`. By virtue of `(1.9.9)`,
there exists an index `λ` such that `S = E_λ`, whence one concludes by the first part of the reasoning that `u_λ` is
universally injective. It then follows from the factorization of `u_λ`:

```text
  ℱ ─u─→ j_*(j^*(ℱ)) → (j_λ)_*((j_λ)^*(ℱ))
```

that `u` is also universally injective.

**Remark (11.9.18).**

<!-- label: IV.11.9.18 -->

*Let `X` be a prescheme, `ℱ`, `𝒢` two quasi-coherent `𝒪_X`-Modules of finite presentation, `𝒢` being moreover assumed
locally free, `u : ℱ → 𝒢` a homomorphism. The following conditions are equivalent:*

*a) for every morphism `g : X' → X`, the homomorphism `g^*(u) : g^*(ℱ) → g^*(𝒢)` is injective;*

*b) for every `x ∈ X`, the homomorphism `u ⊗ 1_{k(x)} : ℱ ⊗_{𝒪_x} k(x) → 𝒢 ⊗_{𝒪_x} k(x)` is injective;*

*c) for every `x ∈ X`, there exists an open neighbourhood `U` of `x` such that `u | U : ℱ | U → 𝒢 | U` is an isomorphism
of `ℱ | U` onto a direct summand of `𝒢 | U`.*

Indeed, it is clear that c) implies a) and that a) implies b). The fact that b) implies c) results from `(0, 19.1.12)`,
`(0_I, 5.2.5)` and `(0_I, 5.5.5)`.

When the preceding equivalent conditions are verified, one says that `u` is **universally injective**.

<!-- original page 170 -->

### 11.10. Schematically dominant families of morphisms and schematically dense families of subpreschemes

**Proposition (11.10.1).**

<!-- label: IV.11.10.1 -->

*Let `X` be a prescheme, `(Z_λ)_{λ ∈ L}` a family of preschemes, and for every `λ ∈ L`, let `f_λ = (ψ_λ, θ_λ) : Z_λ → X`
be a morphism. The following conditions are equivalent:*

*a) The family of homomorphisms `θ_λ : 𝒪_X → (f_λ)_*(𝒪_{Z_λ})` is separating (in other words `(11.9.1)`, the
intersection of the kernels of the `θ_λ` is null).*

*b) For every open set `U` of `X`, every section `t` of `𝒪_X` over `U` whose images by all the canonical homomorphisms*

```text
(11.10.1.1)         (θ_λ)_U : Γ(U, 𝒪_X) → Γ(f_λ⁻¹(U), 𝒪_{Z_λ})
```

*are null, is itself null.*

*c) For every open set `U` of `X`, and every closed subprescheme `Y` of `U` such that for every `λ ∈ L`, there exists a
factorization*

```text
(11.10.1.2)         f_λ⁻¹(U) → Y ─j─→ U
```

*of the restriction `f_λ⁻¹(U) → U` of `f_λ` (where `j` is the canonical injection), one has `Y = U`.*

*If moreover `X` is an `S`-prescheme, these conditions are also equivalent to the following:*

*d) For every separated morphism `g : X' → S` and every couple of `S`-morphisms `u`, `v` of an open set `U` of `X` into
`X'`, such that for every `λ`, the composites of `u` and `v` with the morphism `f_λ⁻¹(U) → U`, restriction of `f_λ`, are
equal, one has `u = v`.*

The equivalence of a) and b) results from the definitions. To see that b) implies c), it suffices to consider the
quasi-coherent Ideal `𝓘` of `𝒪_U` defining `Y`, and to note that, for every open set `V ⊂ U`, the hypothesis implies
that the morphism `(θ_λ)_V` factors as

```text
  Γ(V, 𝒪_U) → Γ(V, 𝒪_Y) → Γ(f_λ⁻¹(V), 𝒪_{Z_λ}).
```

One concludes that every section `t` of `𝓘` over `V` has image `0` in all the `Γ(f_λ⁻¹(V), 𝒪_{Z_λ})`, hence, by virtue
of b), `𝓘 = 0` and `Y = U`. Conversely, if c) is verified, it suffices, to prove b), to apply c) to the closed
subprescheme `Y` of `U` defined by the Ideal `t𝒪_U`: the hypothesis that the images of `t` by the `(θ_λ)_U` are all null
implies that one has factorizations `(11.10.1.2)` for every `λ` `(I, 4.1.9)`. To prove that c) implies d), it suffices
to apply c) to the closed subprescheme `Y` of `U`, inverse image of the diagonal of `X' ×_S X'` by `(u, v)`, and to use
`(I, 4.4.1)`. Conversely, one deduces b) from d) by considering the `S`-scheme `X' = S[T] = S ⊗_ℤ ℤ[T]` (`T`
indeterminate) and recalling that the sections of `𝒪_U` over `U` correspond bijectively to `S`-morphisms `U → S[T]`
`(I, 3.3.15)`; to say that two sections of `𝒪_U` over `U` have the same images by all the `(θ_λ)_U` amounts to saying
that the composites of the two corresponding morphisms with all the morphisms `f_λ⁻¹(U) → U` are equal.

<!-- original page 171 -->

**Definition (11.10.2).**

<!-- label: IV.11.10.2 -->

*When the equivalent conditions of `(11.10.1)` are verified, one says that the family `(f_λ)` is **schematically
dominant**. When the `f_λ` are the canonical immersions in `X` of a family `(Z_λ)` of subpreschemes of `X`, one says
also that the family `(Z_λ)` is **schematically dense**.*

**Remarks (11.10.3).**

<!-- label: IV.11.10.3 -->

*(i) The notion of schematically dominant family is local on `X`, as results for example from form b) in `(11.10.1)`: if
`(W_α)` is an open cover of `X`, the family `(f_λ)` is schematically dominant if and only if so is each of the families
formed of the morphisms `f_λ⁻¹(W_α) → W_α` restrictions of the `f_λ`.*

*(ii) If `Z` is the sum prescheme of the `Z_λ`, `f : Z → X` the morphism coinciding with `f_λ` on each of the `Z_λ`, it
amounts to the same to say that the family `(f_λ)` is schematically dominant, or that the family reduced to the single
element `f` is so.*

*(iii) Let `M` be a second index set and, for every `λ ∈ L`, let `(g_{λμ})_{μ ∈ M}` be a family of morphisms
`g_{λμ} : Z_{λμ} → Z_λ`; if, for each `λ ∈ L`, the family `(g_{λμ})_{μ ∈ M}` is schematically dominant, then it amounts
to the same to say that the family `(f_λ)_{λ ∈ L}` is schematically dominant, or that the family
`(f_λ ∘ g_{λμ})_{(λ, μ) ∈ L × M}` is so `(11.9.2)`.*

*(iv) Let `f : Z → X` be a morphism such that `f_*(𝒪_Z)` is a quasi-coherent `𝒪_X`-Module (for example a quasi-compact
and quasi-separated morphism `(1.7.4)`). Then, to say that `f` is schematically dominant means that the closed image of
`Z` by `f` `(I, 9.5.3)` is identical to `X`.*

**Proposition (11.10.4).**

<!-- label: IV.11.10.4 -->

*If the family of morphisms `f_λ : Z_λ → X` is schematically dominant, the union of the `f_λ(Z_λ)` is dense in `X`.
Conversely, if this union is dense in `X` and if moreover `X` is reduced, the family `(f_λ)` is schematically dominant.*

The first assertion results at once from `(11.10.1, b))`. On the other hand, if `X` is reduced, and if the union of the
`f_λ(Z_λ)` is dense in `X`, then, if one has factorizations `(11.10.1.2)` for every `λ ∈ L`, one has also factorizations
`(f_λ⁻¹(U))_red → Y_red → U`, and the hypothesis implies that the underlying space of `Y` is identical to `U`, hence
`Y = Y_red = U` since `U` is reduced.

The results of `n° 11.9` on separating families translate into results on schematically dominant families:

**Theorem (11.10.5).**

<!-- label: IV.11.10.5 -->

*Let `(f_λ)` be a family of morphisms `f_λ : Z_λ → X`, `g : X' → X` a morphism, and set `Z'_λ = Z_λ ×_X X'`,
`f'_λ = (f_λ)_{(X')} : Z'_λ → X'`.*

*(i) If `g` is faithfully flat and if the family `(f'_λ)` is schematically dominant, then the family `(f_λ)` is
schematically dominant.*

*(ii) Suppose that `g` is a flat morphism, and moreover that one of the following conditions is verified:*

*a) `L` is finite and the `f_λ` are quasi-compact.*

*b) The morphism `g` is locally of finite presentation.*

*Then, if the family `(f_λ)` is schematically dominant, so is the family `(f'_λ)`.*

<!-- original page 172 -->

**Proposition (11.10.6).**

<!-- label: IV.11.10.6 -->

*The notations being those of `(11.10.5)`, suppose that `X` is a prescheme over a field `k`, and that, setting
`S = Spec(k)`, one has `X' = X ×_S S'`, where `S'` is an arbitrary `k`-prescheme. Then, if the family `(f_λ)` is
schematically dominant, so is `(f'_λ)`.*

**Corollary (11.10.7).**

<!-- label: IV.11.10.7 -->

*Let `X` be a prescheme over a field `k`, `(Z_λ)_{λ ∈ L}` a family of `k`-preschemes geometrically reduced over `k`, and
for each `λ ∈ L`, let `f_λ : Z_λ → X` be a `k`-morphism. Denote by `Y` the reduced subprescheme of `X` having as
underlying space the closure of `⋃_{λ ∈ L} f_λ(Z_λ)`. Let `k'` be an extension of `k`, `X'`, `Z'_λ`, `f'_λ : Z'_λ → X'`
the preschemes and morphisms deduced from `X`, `Z_λ` and `f_λ` by extension of the base to `k'`. Then, if `Y'` is the
reduced subprescheme of `X'` having as underlying space the closure of `⋃_{λ ∈ L} f'_λ(Z'_λ)`, one has `Y' = Y ⊗_k k'`.
In particular, `Y` is geometrically reduced over `k`.*

As the `Z_λ` are reduced, the morphisms `f_λ` factor as `f_λ : Z_λ ─g_λ─→ Y ─j─→ X`, where `j` is the canonical
injection `(I, 5.2.12)`. It results then from `(11.10.4)` that `(g_λ)` is a schematically dominant family. Set
`Y'_1 = Y ⊗_k k'`, closed subprescheme of `X'`, and let `g'_λ` be the morphism deduced from `g_λ` by extension of the
base to `k'`, so that `f'_λ` factors as `Z'_λ ─g'_λ─→ Y'_1 ─j'─→ X'`, where `j'` is the canonical injection. It results
from `(11.10.6)` that the family `(g'_λ)` is schematically dominant. But by hypothesis the `Z'_λ` are reduced, hence
`(I, 5.2.2)` the `g'_λ` factor as `Z'_λ → Y' → Y'_1`; one concludes therefore from `(11.10.2)` that `Y' = Y'_1` and
`f'_λ = g'_λ`, which establishes the corollary.

**Definition (11.10.8).**

<!-- label: IV.11.10.8 -->

*The notations being those of `(11.10.5)`, suppose that `X` is an `S`-prescheme. One says that `(f_λ)` is **universally
schematically dominant (relative to `S`)** if, for every base change `S' → S`, the family `(f'_λ)` corresponding to the
base change `X' = X ×_S S' → X` is schematically dominant.*

When `S` is the spectrum of a field, prop. `(11.10.6)` thus means that a schematically dominant family is universally
schematically dominant (relative to `S`).

When the `f_λ` are canonical immersions `Z_λ → X`, one will also say that the family of subpreschemes `Z_λ` is
**universally schematically dense in `X` (relative to `S`)** instead of saying that the family `(f_λ)` is universally
schematically dominant (relative to `S`).

**Theorem (11.10.9).**

<!-- label: IV.11.10.9 -->

*The notations being those of `(11.10.5)`, suppose that `X` is a locally Noetherian `S`-prescheme and that the `Z_λ` are
all `S`-flat. For every `s ∈ S`, let `X_s = X ×_S Spec(k(s))`, `(Z_λ)_s = Z_λ ×_S Spec(k(s))`,
`(f_λ)_s = f_λ × 1 : (Z_λ)_s → X_s`. For the family `(f_λ)` to be universally schematically dominant relative to `S`, it
is necessary and sufficient that, for every `s ∈ S`, the family `((f_λ)_s)` be schematically dominant.*

**Proposition (11.10.10).**

<!-- label: IV.11.10.10 -->

*Let `f : X → S` be a flat morphism locally of finite presentation, `U` an open set of `X`. For `U` to be universally
schematically dense in `X` relative to `S`, it is necessary and sufficient that, for every `s ∈ S`, `U_s = U ∩ X_s` be
schematically dense in `X_s` (or, equivalently, that one have `Ass(𝒪_{X_s}) ⊂ U_s`).*

