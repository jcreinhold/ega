<!-- original page 182 -->

## §22. Differential criteria for formal smoothness and regularity

The principal results of this section are:

a) The criteria `(22.2.2)` and `(22.5.8)`, which give necessary and sufficient conditions for a complete Noetherian
local ring `A` containing a field `k` to be formally smooth over `k`. The criterion `(22.5.8)` is stated without
involving any differential notion, and completes `(0_IV, 19.6.6)`; the statement `(22.2.2)`, of a somewhat more
technical nature, allows one to give a classification, for `k` fixed, of the local rings `A` considered `(22.2.5)`: they
are determined by their dimension `n` and their residue field `K`, subject only to the condition `n ≥ rg_K(Υ_{K/k})`.

b) The theorem `(22.3.3)`, and the corollary `(22.7.6)` of Nagata's Jacobian criterion `(22.7.3)`, which give conditions
allowing one to assert that a localization of a complete Noetherian local ring `A` containing a field `k` is
geometrically regular over `A`; they will play an important role in the study of the "fine" properties of local rings
carried out in Chap. IV, §7. For the moment we possess no proof of `(22.7.6)` independent of Nagata's Jacobian
criterion.

c) Zariski's Jacobian criterion `(22.6.7)` and its variants, which are easy consequences of `(0_IV, 20.7.8)`.

### 22.1. Lifting of formal smoothness

**Theorem (22.1.1).**

<!-- label: 0_IV.22.1.1 -->

*Let `s : Λ → A`, `u : A → B` be two ring homomorphisms, `𝔍` an ideal of `B`, `C` the quotient ring `B/𝔍`. Suppose that
`C` is a `Λ`-algebra formally smooth for the discrete topology.*

*(i) Suppose the following conditions are satisfied:*

*α) `𝔍/𝔍²` is a projective `C`-module.*

*β) The canonical homomorphism `S_C^•(𝔍/𝔍²) → gr_𝔍^•(B)` `(0_IV, 19.5.2)` is bijective.*

*γ) The characteristic homomorphism `χ : Υ_{C/A/Λ} → 𝔍/𝔍²` `(0_IV, 20.6.20)` is injective.*

*δ) The `C`-module `Ω^1_{B/Λ} ⊗_B C` is projective.*

*Then `B`, equipped with the `𝔍`-preadic topology, is a `Λ`-algebra formally smooth.*

*(ii) Conversely, suppose that `B` is a `Λ`-algebra formally smooth for the `𝔍`-preadic topology, and that `A` is a
`Λ`-algebra formally smooth for the discrete topology. Then the conditions α), β), γ), δ) of (i) are satisfied.*

By virtue of the exact sequence `(0_IV, 20.6.22.1)` (which is applicable, since `B/𝔍²` is a `Λ`-trivial extension of `C`
by `𝔍/𝔍²`, `C` being supposed to be a `Λ`-algebra formally smooth `(0_IV, 19.4.4)`), the condition γ) is equivalent to
`Υ^C_{B/A/Λ} = 0`, or equivalently to the following:

γ′) *The homomorphism `u_{B/A/Λ} ⊗ 1_C : Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C` is injective.*

(i) The conditions α) and β) entail that `B` is a `Λ`-algebra formally smooth for the `𝔍`-preadic topology
`(0_IV, 19.5.4)`. It therefore amounts to the same to say that `B` is (for the `𝔍`-preadic topology) a `Λ`-algebra
formally smooth, or a `Λ`-algebra formally smooth relative to `A`. To see that `B` is a `Λ`-algebra formally smooth, it
suffices, by virtue of `(0_IV, 20.7.2)`, to prove that the continuous homomorphism of topological `B`-modules
`u_{B/A/Λ} : Ω^1_{A/Λ} ⊗_A B → Ω^1_{B/Λ}` is formally left-invertible. Now, since `B` is a `Λ`-algebra formally smooth,
the topological `B`-module `Ω^1_{B/Λ}` is formally projective `(0_IV, 20.4.9)` and its topology is deduced from that of
`B` `(0_IV, 20.4.5)`. By virtue of `(0_IV, 19.1.9)`, it therefore suffices, for `u_{B/A/Λ}` to be formally
left-invertible, that `u_{B/A/Λ} ⊗ 1_C` be left-invertible. But by virtue of γ′), this last map is injective, so one has
the exact sequence `(0_IV, 20.6.14.7)`

```text
  0 → Ω^1_{A/Λ} ⊗_A C → Ω^1_{B/Λ} ⊗_B C → Ω^1_{B/A} ⊗_B C → 0.
```

Finally, by virtue of δ), the `C`-module `Ω^1_{B/Λ} ⊗_B C` is projective, so the preceding exact sequence is *split*,
which completes the proof of (i).

(ii) If `B` is a `Λ`-algebra formally smooth for the `𝔍`-preadic topology, and `A` is a `Λ`-algebra formally smooth for
the discrete topology, then `B` is a `A`-algebra formally smooth for the `𝔍`-preadic topology `(0_IV, 19.3.5, (ii))`;
the conditions α) and β) therefore result from `(0_IV, 19.5.6)`. Moreover, `(0_IV, 20.7.2)` shows that `u_{B/A/Λ}` is
formally left-invertible, hence `u_{B/A/Λ} ⊗ 1_C` is left-invertible `(0_IV, 19.1.7)`, and *a fortiori* injective.

<!-- original page 184 -->

Finally, `Ω^1_{B/Λ}` is a formally projective `B`-module `(0_IV, 20.4.9)`, and consequently `Ω^1_{B/Λ} ⊗_B C` is a
projective `C`-module `(0_IV, 19.2.4)`.

**Corollary (22.1.2).**

<!-- label: 0_IV.22.1.2 -->

*Let `s : Λ → A`, `u : A → B` be two ring homomorphisms, `𝔪` a maximal ideal of `B`, `K = B/𝔪` the quotient field.
Suppose that the `Λ`-algebras `A` and `K` are formally smooth for the discrete topology. Then the following conditions
are equivalent:*

*a) `B` is a `Λ`-algebra formally smooth for the `𝔪`-preadic topology.*

*b) The canonical homomorphism*

```text
  (22.1.2.1)   S_K^•(𝔪/𝔪²) → gr_𝔪^•(B)
```

*is bijective, and the characteristic homomorphism*

```text
  (22.1.2.2)   χ : Υ_{K/A/Λ} → 𝔪/𝔪²
```

*is injective.*

This follows immediately from `(22.1.1)`, the conditions α) and δ) being here trivially satisfied, since `K` is a field.

**Remark (22.1.3).**

<!-- label: 0_IV.22.1.3 -->

*Suppose the hypotheses of `(22.1.2)` are satisfied and moreover suppose that `𝔪/𝔪²` is a `K`-vector space of finite
rank. Then, for `B` to be a `Λ`-algebra formally smooth for the `𝔪`-preadic topology, it suffices that the following
conditions be satisfied:*

*(22.1.3.1) Given a polynomial algebra `E = K[T_1, …, T_n]`, the maximal ideal `𝔫` of `E` generated by the `T_i`
(`1 ≤ i ≤ n`), and an ideal `𝔟 ⊃ 𝔫^k` of `E`, every `Λ`-homomorphism `v : B → E/𝔟` which, by passage to the quotients,
gives the identity `K → K`, factors as `B ─w→ E/𝔫^k → E/𝔟`, where `w` is a `Λ`-homomorphism.*

*(22.1.3.2) If `F` is the trivial extension `D_K(K)` ("algebra of dual numbers over `K`"), `ρ : Λ → F` a ring
homomorphism such that the composite `Λ ─ρ→ F → K` is the canonical homomorphism, then every `Λ`-homomorphism
`v : B → K` which, by passage to the quotients, gives the identity `K → K`, factors as `B ─w→ F → K`, where `w` is a
`Λ`-homomorphism (for the `Λ`-algebra structure on `F` defined by `ρ`).*

Indeed, we have seen `(0_IV, 19.5.5)` that condition `(22.1.3.1)` entails that the canonical homomorphism `(22.1.2.1)`
is bijective. By virtue of `(22.1.2)`, it then suffices to see that the canonical homomorphism
`u_{B/A/Λ} ⊗ 1_K : Ω^1_{A/Λ} ⊗_A K → Ω^1_{B/Λ} ⊗_B K` is injective, or equivalently (since these are `K`-vector spaces)
that for every `K`-vector space `L`, the canonical homomorphism `Der_Λ(B, L) → Der_Λ(A, L)` is *surjective* (by virtue
of `(0_IV, 20.4.8)`); it is clear that for this it is necessary and sufficient that the canonical homomorphism
`Der_Λ(B, K) → Der_Λ(A, K)` be surjective, whence our assertion, by virtue of `(0_IV, 20.1.5)`.

One notes that the two conditions `(22.1.3.1)` and `(22.1.3.2)` are entailed by the following:

*(22.1.3.3) For every local Artinian `Λ`-algebra `E` with residue field equal to `K`, and every nilpotent ideal `𝔯` of
`E`, every `Λ`-homomorphism `B → E/𝔯` which, by passage to the quotients, gives the identity `K → K`, factors as
`B ─u→ E → E/𝔯`, where `u` is a `Λ`-homomorphism.*

<!-- original page 185 -->

This result generalizes as follows.

**Proposition (22.1.4).**

<!-- label: 0_IV.22.1.4 -->

*Let `φ : A → B` be a local homomorphism of Noetherian local rings, `k` (resp. `K`) the residue field of `A` (resp.
`B`). For `B` to be a `A`-algebra formally smooth (for the preadic topologies), it is necessary and sufficient that for
every local Artinian ring `C` with residue field equal to `K`, every local homomorphism `A → C` (making `C` a
topological `A`-algebra), and every nilpotent ideal `𝔍` of `C`, every local `A`-homomorphism `B → C/𝔍` such that the
homomorphism `K → K` obtained by passage to the quotients is the identity, factors as `B ─f→ C → C/𝔍`, where `f` is a
local `A`-homomorphism.*

The condition being necessary by definition `(0_IV, 19.3.1)`, we show that it is sufficient. Since the `A`-homomorphisms
of `B` into a discrete local `Â`-algebra arise by extension from local `A`-homomorphisms of `B` into this algebra, one
may reduce to the case where `A` and `B` are complete, by virtue of `(0_IV, 19.3.6)`. When `A` is a field `k`, the
proposition follows from `(22.1.3.3)`, where one takes the prime subfield of `k` for `Λ`, and from `(0_IV, 19.6.1)`. In
the general case, set `B_0 = B ⊗_A k = B/𝔪B` (`𝔪` maximal ideal of `A`), which is complete. If `C_0` is a local Artinian
`k`-algebra with residue field equal to `K`, `𝔍_0` a nilpotent ideal of `C_0`, every local `k`-homomorphism
`g_0 : B_0 → C_0/𝔍_0` giving the identity on `K` by passage to the quotients, gives by composition a local
`A`-homomorphism

```text
  g : B → B_0 → C_0/𝔍_0
```

which by hypothesis therefore factors as `B → C_0 → C_0/𝔍_0`, where `f` is a local `A`-homomorphism; but since `C_0` is
a `k`-algebra, `f` factors as `B → B_0 ─f_0→ C_0`, where `f_0` is a local `k`-homomorphism. We see therefore that the
hypotheses of the statement are still satisfied when one substitutes `B_0` and `k` for `B` and `A` respectively; hence
`B_0` is a `k`-algebra formally smooth according to what we have just seen. Applying `(0_IV, 19.7.2)` and
`(0_IV, 19.7.1)`, we see that there exists a complete Noetherian local ring `B′`, a local homomorphism `A → B′` making
`B′` a flat `A`-module and a `A`-algebra formally smooth, and an `A`-isomorphism `u_0 : B_0 ⥲ B′ ⊗_A k = B′_0`. Let
`v_0` be the inverse isomorphism of `u_0`; we propose to show that there exists a local `A`-homomorphism `v : B → B′`
such that `v_0` arises from `v` by passage to the quotients. For this, denote by `𝔫` and `𝔫′` the respective maximal
ideals of `B` and `B′`, and, for each `j`, let `w_j : B/(𝔫^{j+1} + 𝔪B) → B′/(𝔫′^{j+1} + 𝔪B′)` be the homomorphism
deduced from `v_0` by passage to the quotients; it will suffice to form for each `j` a local `A`-homomorphism
`v_j : B/𝔫^{j+1} → B′/𝔫′^{j+1}` such that the diagrams

```text
  B/𝔫^{j+1} ──v_j──▸ B′/𝔫′^{j+1}              B/𝔫^{j+1} ────v_j────▸ B′/𝔫′^{j+1}
       │                  │                          │                       │
       ▼                  ▼                          ▼                       ▼
  B/𝔫^j ──v_{j-1}──▸ B′/𝔫′^j         B/(𝔫^{j+1} + 𝔪B) ─w_j─▸ B′/(𝔫′^{j+1} + 𝔪B′)
```

be commutative; `B` and `B′` being complete, the homomorphism `v = lim v_j` will answer the question. Now, the recursive
formation of `v_j` results from the hypothesis on `B` and from the

<!-- original page 186 -->

same reasoning as in `(0_IV, 19.3.10.1)`, using the lemma `(0_IV, 19.3.10.2)` and the fact that
`𝔫′^j + (𝔫′^{j+1} + 𝔪B′) = 𝔫′^j + 𝔪B′`. It then follows from `(0_IV, 19.7.1.4)` that `v` is an `A`-isomorphism, for `B′`
is a flat `A`-module, and `B` is complete for the `𝔪`-preadic topology, the ideals `𝔪^j B` being closed in `B` for the
`𝔫`-adic topology `(0_I, 7.3.5)`. Q.E.D.

### 22.2. Differential characterization of local algebras formally smooth over a field

(22.2.1) Let `k` be a field, `P` its prime subfield, `A` a `k`-algebra which is a local ring, `𝔪` its maximal ideal,
`K = A/𝔪` its residue field. Since `K` is separable over `P`, `K` is a `P`-algebra formally smooth for the discrete
topology `(0_IV, 19.6.1)`, and consequently the `P`-extension `A/𝔪²` of `K` by `𝔪/𝔪²` is `P`-trivial, and the
characteristic homomorphism

```text
  (22.2.1.1)   χ_{A/k} : Υ_{K/k} → 𝔪/𝔪²
```

is therefore defined `(0_IV, 20.6.23)`.

**Theorem (22.2.2).**

<!-- label: 0_IV.22.2.2 -->

*Under the conditions of `(22.2.1)`, for `A` to be a `k`-algebra formally smooth for the `𝔪`-preadic topology, it is
necessary and sufficient that the following conditions be satisfied:*

*(i) The canonical homomorphism `S_K^•(𝔪/𝔪²) → gr_𝔪^•(A)` is bijective.*

*(ii) The characteristic homomorphism `χ_{A/k} : Υ_{K/k} → 𝔪/𝔪²` is injective.*

This is a particular case of `(22.1.2)`, where one replaces `Λ` by `P`, `A` by `k`, and `B` by `A`; `K` and `k`, being
separable over `P`, are indeed `P`-algebras formally smooth `(0_IV, 19.6.1)`.

**Remark (22.2.3).**

<!-- label: 0_IV.22.2.3 -->

*Condition (ii) of `(22.2.2)` may be replaced by any of the following:*

*a) The canonical homomorphism `Ω^1_k ⊗_k K → Ω^1_A ⊗_A K` is injective.*

*b) For every `n`, the canonical homomorphism `Ω^1_k ⊗_k (A/𝔪^{n+1}) → Ω^1_{A/k} ⊗_A (A/𝔪^{n+1})` is left-invertible.*

*c) The canonical homomorphism `Ω^1_k ⊗̂_k A → Ω̂^1_A` is left-invertible.*

*d) `A` is a `k`-algebra formally smooth (for the `𝔪`-preadic topology) relative to the prime field.*

Indeed, we have already remarked in `(22.1.1)` that the injectivity of `χ_{A/k}` is equivalent to a), and that the
conjunction of a) and condition (i) of `(22.2.2)` is equivalent to that of d) and (i). Finally, we have also seen in
`(22.1.1)` that b) and d) are equivalent, and the equivalence of b) and c) results from `(0_IV, 19.1.8)`.

(22.2.4) The principal application of `(22.2.2)` concerns local Noetherian and complete `k`-algebras (case where `𝔪/𝔪²`
is a `K`-vector space of finite rank). More precisely, let `k` be a field, `K` an extension of `k`, `V` a `K`-vector
space of

<!-- original page 187 -->

finite rank; we consider the triples `(A, α, β)`, where `A` is a complete Noetherian local `k`-algebra formally smooth
with maximal ideal `𝔪`, `α : A/𝔪 ⥲ K` an isomorphism of `k`-algebras, `β : 𝔪/𝔪² ⥲ V` a di-isomorphism of vector spaces
(for the isomorphism `α`). Given two such triples `(A, α, β)`, `(A′, α′, β′)`, an *equivalence* of the first onto the
second is a `k`-isomorphism `u : A ⥲ A′` such that (if `𝔪′` is the maximal ideal of `A′`) the diagrams

```text
       gr^0(u)                         gr^1(u)
  A/𝔪 ────────▸ A′/𝔪′             𝔪/𝔪² ────────▸ 𝔪′/𝔪′²
    │              │                  │                │
   α│              │α′               β│                │β′
    ▼              ▼                  ▼                ▼
    K ───1_K────▸ K                   V ────1_V────▸ V
```

are commutative. It is immediate that the equivalence classes of triples `(A, α, β)` form a set, which we denote
`FL(K/k, V)`. We now remark that to every triple `(A, α, β)` is associated the composite `K`-homomorphism of vector
spaces `Υ_{K/k} ─χ_{A/k}→ 𝔪/𝔪² ─β→ V` (where `χ_{A/k}` is regarded as a di-homomorphism relative to `α⁻¹`); the
preceding definition proves (by `(0_IV, 20.6.22.2)`) that this `K`-homomorphism *depends only on the equivalence class*
of `(A, α, β)` in `FL(K/k, V)`; in other words one has defined a canonical map

```text
  (22.2.4.1)   FL(K/k, V) → Hom_K(Υ_{K/k}, V).
```

**Proposition (22.2.5).**

<!-- label: 0_IV.22.2.5 -->

*Let `k` be a field, `K` an extension of `k`, `V` a `K`-vector space of finite rank. The canonical map `(22.2.4.1)` is a
bijection of `FL(K/k, V)` onto the set of injective `K`-homomorphisms of `Υ_{K/k}` into `V`.*

(i) To show that `(22.2.4.1)` is injective, one must prove the following: let `A`, `A′` be two complete Noetherian local
`k`-algebras formally smooth, `𝔪`, `𝔪′` their respective maximal ideals, `α : A/𝔪 ⥲ K`, `α′ : A′/𝔪′ ⥲ K` two
`k`-isomorphisms; suppose given two `k`-isomorphisms `v^0 : A/𝔪 ⥲ A′/𝔪′`, `v^1 : 𝔪/𝔪² ⥲ 𝔪′/𝔪′²` such that the diagrams

```text
                    v^0                                       v^1
  (22.2.5.1)   A/𝔪 ────▸ A′/𝔪′                 𝔪/𝔪² ────▸ 𝔪′/𝔪′²
                ╲       ╱                          ↖             ↗
                 α     α′                        χ_A         χ_{A′}
                  ╲   ╱                              ╲         ╱
                    K                                  Υ_{K/k}
```

are commutative. It is required to prove that there exists a `k`-isomorphism `u : A ⥲ A′` such that `gr^0(u) = v^0` and
`gr^1(u) = v^1`. Note first that since `K` is a field, the canonical homomorphism `(0_IV, 20.6.7.1)` is bijective
`(0_IV, 20.6.11)`, hence there already exists a `k`-isomorphism `v : A/𝔪² ⥲ A′/𝔪′²` such that `gr^0(v) = v^0` and
`gr^1(v) = v^1`. Note next that since `A′` is metrisable and complete, and `A` a `k`-algebra formally smooth, the
composite homomorphism `A → A/𝔪² ─v→ A′/𝔪′²` factors as `A ─u→ A′ → A′/𝔪′²`, where `u` is

<!-- original page 188 -->

a `k`-homomorphism `(0_IV, 19.3.11)`, and we therefore already have `gr^0(u) = v^0` and `gr^1(u) = v^1`. Now, one has
the commutative diagram

```text
  S_K^•(𝔪/𝔪²)  ────────▸  gr_𝔪^•(A)
       │                         │
       │ w                       │ gr^•(u)
       ▼                         ▼
  S_K^•(𝔪′/𝔪′²) ───────▸  gr_{𝔪′}^•(A′)
```

where the horizontal arrows are the canonical homomorphisms, and `w` arises from `v^0` and `v^1`; since `v^0` and `v^1`
are bijective, the same holds for `w`, and since `A` and `A′` are `k`-algebras formally smooth, one deduces from
`(22.2.2, (i))` that `gr^•(u)` is bijective. But since `A` and `A′` are separated and complete, this entails that `u`
itself is bijective (Bourbaki, *Alg. comm.*, chap. III, §2, n° 8, cor. 3 of th. 1).

(ii) It remains to show that the image of `(22.2.4.1)` is the set of *injective* homomorphisms of `Υ_{K/k}` into `V`; we
already know by `(22.2.2, (ii))` that it is contained in this set; it will then suffice to prove the

**Lemma (22.2.5.2).**

<!-- label: 0_IV.22.2.5.2 -->

*For every `K`-homomorphism `h : Υ_{K/k} → V`, there exists a `k`-algebra `A` which is a complete regular Noetherian
local ring, with maximal ideal `𝔪`, residue field `K`, and a `K`-isomorphism `β : 𝔪/𝔪² ⥲ V` such that
`h = β ∘ χ_{A/k}`.*

Indeed, if this lemma is proved, the fact that `A` is regular entails that condition (i) of `(22.2.2)` is satisfied
`(0_IV, 17.1.1)`; if moreover `h` is injective, `(22.2.2)` will show that `A` is a `k`-algebra formally smooth whose
class will have `h` for image (on the other hand, if `h` is not injective, the `k`-algebra `A` whose existence
`(22.2.5.2)` proves is not formally smooth).

To prove `(22.2.5.2)`, let `B` be the `K`-algebra `S_K^•(V)`, `𝔫` the augmentation ideal of `B`, and `A = B̂` the
completed `K`-algebra of `B` for the `𝔫`-preadic topology (so that `A` is isomorphic to the algebra of formal series
`K[[T_1, …, T_n]]` if `n = rg_K(V)`). By virtue of `(0_IV, 20.6.11)` there exists on `A/𝔪²` (where `𝔪 = 𝔫 A`) a
structure of `k`-extension of `K` by `V` (distinct in general from the `k`-trivial structure defined by the canonical
injection `k → K → A`) such that `h` is the characteristic homomorphism of this extension. If `f : k → A/𝔪²` is the
structural homomorphism, the fact that `k` is separable over the prime field permits `(0_IV, 19.6.1)` factoring `f` as
`k ─g→ A → A/𝔪²`, and the `k`-algebra `A` so defined answers the question `(0_IV, 20.6.22.2)`.

**Theorem (22.2.6).**

<!-- label: 0_IV.22.2.6 -->

*Let `k` be a field, `K` an extension of `k`. For there to exist a Noetherian local `k`-algebra `A`, with maximal ideal
`𝔪`, such that `A/𝔪 = K` and `A` is formally smooth (for its `𝔪`-preadic topology), it is necessary and sufficient that
`Υ_{K/k}` be a `K`-vector space of finite rank. The `k`-algebra `A` is then determined (up to a `k`-isomorphism giving
by passage to the quotients the identity `K → K`) by its dimension, which is subject only to the condition
`≥ rg_K(Υ_{K/k})`.*

Since `𝔪/𝔪²` is of finite rank over `K`, the necessity of the condition follows from `(22.2.2, (ii))`; conversely,
`(22.2.5)` shows that the condition is sufficient and that one may take for `𝔪/𝔪²` a `K`-vector space of arbitrary rank
`≥ rg_K(Υ_{K/k})`.

<!-- original page 189 -->

In particular, the identity homomorphism of `Υ_{K/k}` canonically associates to `K` a complete Noetherian `k`-algebra,
formally smooth, for which `Υ_{K/k}` is isomorphic to `𝔪/𝔪²`.

**Remarks (22.2.7).**

<!-- label: 0_IV.22.2.7 -->

*(i) Let `Λ` be a Noetherian local ring with residue field `k`; it follows from `(0_IV, 19.7.1)` and `(0_IV, 19.7.2)`
that the determination of the `Λ`-algebras `A` which are complete Noetherian local rings and which are formally smooth
is equivalent to the same problem where `Λ` is replaced by `k`, and is thus in principle entirely resolved by
`(22.2.5)`, which reduces the question to the structure of the residue fields of the sought-for `k`-algebras, as
extensions of `k`.*

*(ii) The fact that `Υ_{K/k}` is of finite rank over `K` does not entail that `K` is "of finite radicial multiplicity"
over `k` (cf. `(0_IV, 19.6.6)`). For example, let `k_0` be a perfect field of characteristic `p > 0`, `k = k_0(T)` the
field of rational fractions in one indeterminate over `k_0`, and `K = k^{p^{-∞}}` the smallest perfect extension of `k`.
One then has `Ω^1_k = Ω^1_{k/k_0} = 0` `(0_IV, 21.4.4)`, hence by definition `(0_IV, 20.6.1.1)` `Υ_{K/k} = Ω^1_K ⊗_k K`,
and since `k^p = k_0(T^p)`, `T` is a `p`-basis of `k` over `k^p`, hence `(0_IV, 21.4.5)`, `Ω^1_K` is of rank `1` over
`k`, and consequently `Υ_{K/k}` of rank `1` over `K`. But for every `n` the residue field of the local ring
`K ⊗_k k^{p^{-n}}` is isomorphic to `K` and is therefore not separable over `k^{p^{-n}}`.*

The theorem `(22.2.2)` generalizes as follows.

**Proposition (22.2.8).**

<!-- label: 0_IV.22.2.8 -->

*Under the conditions of `(22.2.1)`, suppose that the characteristic `p` of `k` is `> 0`; let `(k_α)` be a decreasing
filtered family of subfields of `k`, such that `⋂_α k_α(k^p) = k^p`. Then condition (ii) of `(22.2.2)` can be replaced
by any of the following:*

*a) There exists `α_0` such that the canonical homomorphism*

```text
  Ω^1_{k/k_α} ⊗_k K → Ω^1_{A/k_α} ⊗_A K
```

*is injective for every `α ≥ α_0`.*

*b) There exists `α_0` such that `A` is a `k`-algebra formally smooth (for the `𝔪`-preadic topology) relative to `k_α`,
for every `α ≥ α_0`.*

*c) For every `α` and every integer `n ≥ 0`, the canonical homomorphism*

```text
  Ω^1_{k/k_α} ⊗_k (A/𝔪^{n+1}) → Ω^1_{A/k_α} ⊗_A (A/𝔪^{n+1})
```

*is left-invertible.*

Indeed, if `A` is a `k`-algebra formally smooth, it is so *a fortiori* relative to any subfield of `k`, which entails c)
by virtue of `(0_IV, 20.7.2)` and `(0_IV, 19.1.7)`; it is clear that c) implies b), by virtue of `(0_IV, 20.7.2)`, and
that b) implies a). Finally, taking account of `(22.2.3)`, it remains to prove that a) entails that the canonical
homomorphism `u : Ω^1_k ⊗_k K → Ω^1_A ⊗_A K` is *injective*. Now, for every `α` one has a commutative diagram

```text
  Ω^1_k ⊗_k K ──────u──────▸ Ω^1_A ⊗_A K
       │                            │
       │ v_α                        │
       ▼                            ▼
  Ω^1_{k/k_α} ⊗_k K ──u_α──▸ Ω^1_{A/k_α} ⊗_A K
```

<!-- original page 190 -->

and the hypothesis that `u_α` is injective for `α ≥ α_0` implies that `Ker(u)` is contained in the intersection of the
`Ker(v_α)`. But we have seen `(0_IV, 21.8.3)` that this intersection is zero by virtue of the hypothesis
`⋂_α k_α(k^p) = k^p`, which completes the proof.

**Proposition (22.2.9).**

<!-- label: 0_IV.22.2.9 -->

*Under the hypotheses of `(22.2.1)`, the following conditions are equivalent:*

*a) `A/𝔪²` is a `k`-trivial `k`-extension of `K` by `𝔪/𝔪²`.*

*b) `χ_{A/k} = 0`.*

*c) The canonical homomorphism \`(0_IV, 20.5.11.2)*

```text
  δ_{K/A/k} : 𝔪/𝔪² → Ω^1_A ⊗_A K
```

*is injective (in other words, the sequence*

```text
  (22.2.9.1)   0 → 𝔪/𝔪² → Ω^1_A ⊗_A K → Ω^1_K → 0
```

*is exact).*

The equivalence of b) and c) results from the exact sequence `(0_IV, 20.6.22.1)`; the equivalence of c) and a) results
from `(0_IV, 20.5.12)`, the sequence `(22.2.9.1)` being split if it is exact, since these are vector spaces.

One notes that if `K` is separable over `k`, the equivalent conditions of `(22.2.9)` are satisfied, by virtue of the
definition of `χ_{A/k}` `(22.2.1)` and of `(0_IV, 20.6.3)`.

**Corollary (22.2.10).**

<!-- label: 0_IV.22.2.10 -->

*Under the hypotheses of `(22.2.1)`, consider a subfield `k_0` of `k`. The following conditions are equivalent:*

*a) `A/𝔪²` is a `k_0`-trivial `k`-extension of `K` by `𝔪/𝔪²`.*

*b) The composite homomorphism `Υ_{K/k_0} → Υ_{K/k} ─χ_{A/k}→ 𝔪/𝔪²` is zero.*

*c) The characteristic homomorphism `χ_{A/k} : Υ_{K/k} → 𝔪/𝔪²` factors as `Υ_{K/k} → Υ_{K/k/k_0} ─χ′→ 𝔪/𝔪²`.*

*Moreover, when these conditions are fulfilled, the homomorphism `χ′` is uniquely determined and coincides with the
characteristic homomorphism of the `k_0`-trivial `k`-extension `A/𝔪²` of `K` by `𝔪/𝔪²`.*

Since the composite in b) is none other than `χ_{A/k_0}`, the equivalence of a) and b) results from `(22.2.9)`; on the
other hand, b) and c) are equivalent by virtue of the exact sequence `(0_IV, 20.6.18.1)`

```text
  Υ_{K/k_0} → Υ_{K/k} → Υ_{K/k/k_0} → 0
```

and since the canonical homomorphism `Υ_{K/k} → Υ_{K/k/k_0}` is surjective, this implies the uniqueness of `χ′`; the
fact that `χ′` is the characteristic homomorphism of the `k_0`-extension `A/𝔪²` results from `(0_IV, 20.6.22.2)`.

**Corollary (22.2.11).**

<!-- label: 0_IV.22.2.11 -->

*Under the hypotheses of `(22.2.1)`, let `p` be the characteristic exponent of `k`, and let `(k_α)` be a decreasing
filtered family of subfields of `k` such that `⋂_α k_α(k^p) = k^p`. If `Υ_{K/k}` is of finite rank over `K`, there
exists an index `α` such that `A/𝔪²` is a `k_α`-trivial `k`-extension of `K` by `𝔪/𝔪²`.*

We know `(0_IV, 21.8.3)` that there exists then an index `α` such that the canonical homomorphism
`Υ_{K/k} → Υ_{K/k/k_α}` is bijective, hence condition b) of `(22.2.10)` (where `k_α` replaces `k_0`) is satisfied.

<!-- original page 191 -->

### 22.3. Application to the relations between certain local rings and their completions

**Lemma (22.3.1).**

<!-- label: 0_IV.22.3.1 -->

*Let `A_0` be a Noetherian semi-local ring, `A` a finite `A_0`-algebra (which is thus a Noetherian semi-local ring, cf.
Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9). If `Â_0` and `Â` are the completions of `A_0` and `A`
for their respective preadic topologies, then, when one equips `A_0`, `A` and `Â` with the discrete topologies, `Â` is a
`A`-algebra formally smooth relative to `A_0` `(0_IV, 19.9.1)`.*

We know indeed that `Â = A ⊗_{A_0} Â_0` (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9 and chap. III,
§3, n° 4, th. 1), so the proposition results from `(0_IV, 19.9.3)`.

**Proposition (22.3.2).**

<!-- label: 0_IV.22.3.2 -->

*Let `A` be a regular Noetherian local ring, `K` its field of fractions, `p` the characteristic of `K`. Suppose one of
the following hypotheses is satisfied:*

*(i) `p = 0`.*

*(ii) `p > 0` and there exists a decreasing filtered family `(A_α)` of Noetherian subrings of `A`, such that `A` is a
finite `A_α`-algebra for every `α`, that `A^{p^{h(α)}} ⊂ A_α` for a suitable integer `h(α)`, and that, if `K_α` denotes
the field of fractions of `A_α`, one has `⋂_α K_α(K^p) = K^p`.*

*Let then `B` be an integral finite `A`-algebra containing `A`, `𝔫` a prime ideal of `B`, `C` the local ring `B_𝔫`, `𝔮`
a prime ideal of the completion `Ĉ` such that `𝔮 ∩ C = 0`, so that the local ring `Ĉ_𝔮` is an algebra over the field of
fractions `L` of `B`. Then `Ĉ_𝔮` is an `L`-algebra formally smooth for its `𝔮`-adic topology, and consequently a
geometrically regular ring over `L` `(0_IV, 19.6.5)`.*

Let us distinguish two cases.

I) Suppose that `𝔫` contains the maximal ideal `𝔪` of `A`, and consequently `𝔫 ∩ A = 𝔪`. Then `𝔫` is maximal (Bourbaki,
*Alg. comm.*, chap. V, §2, n° 1, prop. 1) and if `𝔯` is the radical of the semi-local ring `B`, `Ĉ` is the separated
completion of `B` for the `𝔫`-preadic topology, and one of the components of the semi-local ring `B̂`, the completion of
`B` for the `𝔯`-preadic topology (Bourbaki, *Alg. comm.*, chap. III, §3, n° 4, prop. 8); one may therefore write
`Ĉ_𝔮 = B̂_{𝔮′}`, where `𝔮′` is the prime ideal of `B̂` inverse image of `𝔮`. Note now that `B` is a subring of `B̂` and
the hypothesis `𝔮 ∩ C = 0` entails `𝔮′ ∩ B = 0`, hence `B̂_{𝔮′}` is also the localization of the ring `B̂ ⊗_B L` at one
of its prime ideals `𝔮″`, of which `𝔮′` is the inverse image in `B̂`. Moreover one has `B̂ = Â ⊗_A B` (Bourbaki, *Alg.
comm.*, chap. IV, §2, n° 5, cor. of prop. 9 and chap. III, §3, n° 4, th. 1), hence `B̂ ⊗_B L = Â ⊗_A L`; finally, if `𝔭`
is the prime ideal of `Â`, inverse image of `𝔮″`, the fact that `A → B` is injective and the commutativity of the
diagram

```text
  B ────▸ B̂
  ▲       ▲
  │       │
  A ────▸ Â
```

entail that `𝔭 ∩ A = 0`, hence `(Â ⊗_A L)_{𝔮″}` is also localized of the ring

```text
  Â ⊗_A L = (Â ⊗_A K) ⊗_K L
```

<!-- original page 192 -->

at one of its prime ideals. To show that this local ring is an `L`-algebra formally smooth, it therefore suffices to
prove that `Â_𝔭 ⊗_A K` is a `K`-algebra formally smooth `(0_IV, 19.3.5, (iii) and (iv))`; moreover `Â_𝔭 ⊗_A K = Â_𝔭`
since `𝔭 ∩ A = 0`. We are going to apply the criteria `(22.2.2)` and `(22.2.8)`. In the first place, since `A` is
regular, so is `Â` `(0_IV, 17.1.5)`, hence so is `Â_𝔭` `(0_IV, 17.3.2)`, and condition (i) of `(22.2.2)` is satisfied
`(0_IV, 17.1.1)`. It therefore suffices (when `p > 0`) to verify condition b) of `(22.2.8)`. Now, `(22.3.1)` shows that,
for every `α`, `Â` is an `A`-algebra formally smooth relative to `A_α` (for the discrete topologies); consequently
`Â ⊗_{A_α} K_α = Â ⊗_A (A ⊗_{A_α} K_α)` is a `(A ⊗_{A_α} K_α)`-algebra formally smooth relative to `K_α`, for the
discrete topologies `(0_IV, 19.9.2, (iii))`. But since `A` is a finite `A_α`-algebra, one has `A ⊗_{A_α} K_α = K`; since
`Â_𝔭` is a localization of `Â ⊗_A K`, one concludes `(0_IV, 19.9.2, (iv))` that `Â_𝔭` is a `K`-algebra formally smooth
relative to `K_α`, for the discrete topology, and *a fortiori* for its `𝔭`-adic topology (`(0_IV, 19.3.8)` and
`(0_IV, 19.9.5)`). But this is precisely condition b) of `(22.2.8)`, hence the proposition is proved in this case for
`p > 0`. When `p = 0`, the residue field of `Â_𝔭` is separable over `K`, and since `Â_𝔭` is a regular ring, it is a
`K`-algebra formally smooth by virtue of `(0_IV, 19.6.4)`.

II) General case. Let `𝔰` be the prime ideal `𝔫 ∩ A` of `A`, and set `S = A − 𝔰`, so that `S⁻¹ A = A_𝔰`, and one has
`C = (S⁻¹ B)_{S⁻¹ 𝔫}`, where this time `S⁻¹ 𝔫` contains the maximal ideal `𝔰 A_𝔰` of `A_𝔰`. Since `A_𝔰` is regular
`(0_IV, 17.3.2)` and `S⁻¹ B` is an integral finite `A_𝔰`-algebra containing `A_𝔰`, all reduces to verifying condition
(ii) for `A_𝔰` when `p > 0`: now, set `𝔰_α = 𝔰 ∩ A_α` and consider the local ring `(A_α)_{𝔰_α}`. For every `t ∉ 𝔰`, we
have by hypothesis, on setting `q = p^{h(α)}`, `t^q ∈ A_α` and `t ∉ 𝔰`, hence `t^q ∉ 𝔰_α`; if one sets
`S_α = A_α − 𝔰_α`, one sees that one has `A_𝔰 = S_α⁻¹ A`, and the hypothesis entails that `A_𝔰` is a finite
`(A_α)_{𝔰_α}`-algebra; moreover, `K_α` is also the field of fractions of `(A_α)_{𝔰_α}`, which completes the proof.

**Theorem (22.3.3).**

<!-- label: 0_IV.22.3.3 -->

*Let `A` be a complete Noetherian local ring, `𝔭` a prime ideal of `A`, `B` the localized ring `A_𝔭`, `𝔮` a prime ideal
of the completion `B̂`, `𝔯 = 𝔮 ∩ B`. Then the localized ring `B̂_𝔮` of `B̂` is a `B_𝔯`-algebra formally smooth for the
preadic topologies.*

The prime ideal `𝔯` of `B` is of the form `𝔫_𝔭`, where `𝔫 ⊂ 𝔭` is a prime ideal of `A`, and one has `B_𝔯 = A_𝔫`; let `k`
be the residue field of `B_𝔯`, which is also the field of fractions of the complete integral local ring `A′ = A/𝔫`.
Since `B̂` is a flat `B`-module `(0_I, 7.3.5)`, `B̂_𝔮` is a flat `B_𝔯`-module `(0_I, 6.3.2)`, and to prove that `B̂_𝔮`
is a `B_𝔯`-algebra formally smooth, it suffices to prove that `B̂_𝔮 ⊗_B k = B̂_𝔮/𝔯 B̂_𝔮` is a `k`-algebra formally
smooth `(0_IV, 19.7.1)`. Now `B̂_𝔮/𝔯 B̂_𝔮 = (B̂/𝔯 B̂)_{𝔮′}`, where `𝔮′` is the canonical image of `𝔮` in `B̂/𝔯 B̂`; one
has by definition `𝔮′ ∩ (B/𝔯) = 0` and `B/𝔯 = A_{𝔭′}`, where `𝔭′ = 𝔭/𝔫`; moreover `B̂/𝔯 B̂` is the completion of `B/𝔯`.

We are therefore reduced to proving the following corollary.

**Corollary (22.3.4).**

<!-- label: 0_IV.22.3.4 -->

*Let `A` be a complete integral Noetherian local ring, `K` its field of fractions, `𝔭` a prime ideal of `A`, `B` the
localized ring `A_𝔭`. Then, for every prime ideal `𝔮`*

<!-- original page 193 -->

*of the completion `B̂`, such that `𝔮 ∩ B = 0`, the local ring `B̂_𝔮` is a `K`-algebra formally smooth for its `𝔮`-adic
topology, hence a geometrically regular ring over `K`.*

Indeed, it follows from `(0_IV, 19.8.9)` that there exists a subring `A_0` of `A` which is a ring of formal series over
a field of characteristic `p > 0` or over a Cohen ring (recall that Cohen rings have a field of fractions of
characteristic `0`), and is such that `A` is a finite `A_0`-algebra. Now, one knows that the ring `A_0` is regular
`(0_IV, 17.3.8)` and verifies one of the hypotheses (i), (ii) of `(22.3.2)`, by virtue of `(0_IV, 21.8.8)`; it suffices
therefore to apply `(22.3.2)`, replacing `B` by `A` and `A` by `A_0`.

### 22.4. Preliminary results on finite extensions of local rings whose maximal ideal has square zero

**Proposition (22.4.1).**

<!-- label: 0_IV.22.4.1 -->

*Let `A` be a local ring whose maximal ideal `𝔪` has square zero, `K = A/𝔪` its residue field; denote by `V` the ideal
`𝔪` regarded as a `K`-vector space. Let `T_i` (`1 ≤ i ≤ r`) be indeterminates, and for each `i`, let `F_i` be a unitary
polynomial of `A[T_i]` of degree `d_i`; denote by `A′` the quotient of the polynomial ring `A[T_1, …, T_r]` by the ideal
`𝔟` generated by the `r` polynomials `F_i`. Suppose that `A′` is a local ring, and let `𝔪′` be its maximal ideal,
`K′ = A′/𝔪′` its residue field. Then:*

*(i) If one sets `d = ∏_{i=1}^r d_i`, `A′` is a free `A`-module of rank `d`, and one has `[K′ : K] ≤ d`.*

*(ii) For `[K′ : K] = d`, it is necessary and sufficient that `A′ ⊗_A K = A′/𝔪 A′` be a field (necessarily isomorphic to
`K′`), in other words, that `𝔪′ = 𝔪 A′`. One has in this case `𝔪′² = 0`, and if `V′` denotes the ideal `𝔪′` regarded as
a `K′`-vector space, the canonical homomorphism `V ⊗_K K′ → V′` is bijective (and consequently `rg_{K′} V′ = rg_K V`).*

Without supposing `A′` local, it is evident, by Euclidean division and induction on `r`, that if `t_i` is the class of
`T_i` mod. `𝔟`, the monomials `M_ν = t_1^{ν_1} ⋯ t_r^{ν_r}`, where `0 ≤ ν_i ≤ d_i − 1`, form a basis of the `A`-module
`A′`. If `A′` is supposed local, `K′` is a quotient of `A′/𝔪 A′ = A′ ⊗_A K`, hence `[K′ : K] ≤ [A′ ⊗_A K : K] = d`, and
there can be equality only if `𝔪′ = 𝔪 A′`, which proves (i) and the first assertion of (ii). On the other hand, it is
clear that when `𝔪′ = 𝔪 A′`, one has `𝔪′² = 0`, and `V ⊗_K K′ = 𝔪 ⊗_A A′ = 𝔪 A′ = V′` since `A′` is a free `A`-module.

**Remark (22.4.2).**

<!-- label: 0_IV.22.4.2 -->

*When `A` is Artinian (in other words `rg_K(V)` finite), the hypothesis that `A′` is local always entails that
`rg_{K′}(𝔪′/𝔪′²) ≥ rg_K(V)`, as we shall see later `(22.5.2)`. Note that these two ranks can be equal without one having
`𝔪′ = 𝔪 A′`.*

**Proposition (22.4.3).**

<!-- label: 0_IV.22.4.3 -->

*The hypotheses on `A` and the notations being those of `(22.4.1)`, suppose that the `F_i` are of the form*

```text
  (22.4.3.1)   F_i(T_i) = T_i^{d_i} + ∑_{1 ≤ k ≤ d_i} c_{ik} T_i^{d_i − k}
```

*where `d_i ≥ 2` for every `i`, and `c_{ik} ∈ 𝔪` ("Eisenstein polynomials"). Then:*

*(i) `A′` is a local ring, and its residue field `K′ = A′/𝔪′` is isomorphic to `K`.*

<!-- original page 194 -->

*(ii) The kernel of the canonical homomorphism `V → V′ = 𝔪′/𝔪′²` is the ideal `𝔫` of `A` generated by the
`ξ_i = c_{i, d_i}` ("constant terms" of the `F_i`), and the cokernel of this homomorphism has for basis over `K′` the
images of the `T_i`; in particular, one has*

```text
  (22.4.3.2)   rg_{K′}(V′) = rg_K(V) + r − r′
```

*where `r′ = rg_K(𝔫)`. When `rg_K(V)` is finite (in other words when `A` is Artinian), for `rg_{K′}(V′) = rg_K(V)`, it
is necessary and sufficient that the `ξ_i` be linearly independent over `K`.*

(i) It is clear that `A′ ⊗_A K = A′/𝔪 A′` is isomorphic to `K[T_1, …, T_r]/𝔟′`, where `𝔟′` is the ideal generated by the
`r` polynomials `T_i^{d_i}`; this is therefore a local ring of residue field `K`, whose maximal ideal is generated by
the classes of the `T_i` mod. `𝔟′`, whence (i).

(ii) Let `t_i` (`1 ≤ i ≤ r`) be the class of `T_i` mod. `𝔟`; it follows from (i) that the maximal ideal `𝔪′` of `A′` is
given by

```text
  𝔪′ = 𝔪 A′ + ∑_{i=1}^r t_i A′
```

whence, taking account of `𝔪² = 0`,

```text
  𝔪′² = ∑_{i,j} t_i t_j A′ + ∑_i t_i 𝔪 A′.
```

One concludes that `A′/𝔪′²` is isomorphic to the ring `A[T_1, …, T_r]/𝔠`, where `𝔠` is the ideal generated by the
elements

```text
  F_i  (1 ≤ i ≤ r),   T_i T_j  (1 ≤ i ≤ r, 1 ≤ j ≤ r),   x T_i  (1 ≤ i ≤ r, x ∈ 𝔪).
```

Since `d_i ≥ 2` and the `T_i^{d_i}` belong to `𝔠`, the hypotheses made entail that `𝔠` is also generated by the elements

```text
  ξ_i  (1 ≤ i ≤ r),   T_i T_j  (1 ≤ i ≤ r, 1 ≤ j ≤ r),   T_i x  (1 ≤ i ≤ r, x ∈ 𝔪).
```

Let `𝔠_1 = ∑_{i,j} T_i T_j A[T_1, …, T_r]`, `𝔠_2 = 𝔠_1 + ∑_i 𝔪 T_i A[T_1, …, T_r]`, so that
`𝔠 = 𝔠_2 + ∑_i ξ_i A[T_1, …, T_r]`. It is clear that `A[T_1, …, T_r]/𝔠_1` is the direct sum of `A` and the
`A t_i^{(1)}`, where `t_i^{(1)}` is the class of `T_i` mod. `𝔠_1`. One deduces that `A[T_1, …, T_r]/𝔠_2` is the direct
sum of `A` and the `K t_i^{(2)}`, where `t_i^{(2)}` is the class of `T_i` mod. `𝔠_2`. Finally `A[T_1, …, T_r]/𝔠` is the
direct sum of `A/𝔫` and the `K t_i′`, where `t_i′` is the class of `T_i` mod. `𝔠`, and `𝔫` is the ideal of `A` generated
by the `ξ_i`; in the identification of `A′/𝔪′²` with `A[T_1, …, T_r]/𝔠`, the image of `V` identifies with `𝔪/𝔫`, and
what precedes therefore proves (ii).

**Proposition (22.4.4).**

<!-- label: 0_IV.22.4.4 -->

*The hypotheses on `A` and the notations being those of `(22.4.1)`, suppose that `K` is of characteristic `p > 0` (hence
`p · 1 ∈ 𝔪` in `A`) and that the `F_i` are of the form*

```text
  (22.4.4.1)   F_i(T_i) = T_i^p + p ∑_{k=1}^{p−1} c_{ik} T_i^{p−k} − f_i
```

*with `c_{ik} ∈ A` and `f_i ∈ A` for every `i` and every `k` such that `1 ≤ k ≤ p − 1`; moreover, if `a_i` is the class
of `f_i` mod. `𝔪`, suppose that the family `(a_i)_{1 ≤ i ≤ r}` is `p`-free over `K^p` ("absolutely `p`-free"). Then:*

*(i) `A′` is a local ring, of maximal ideal `𝔪 A′`, whose residue field `K′` is isomorphic to the extension of `K`
obtained by adjunction of the `a_i^{1/p}` (`1 ≤ i ≤ r`).*

<!-- original page 195 -->

*(ii) The elements `d_A f_i ⊗ 1_{K′}` form a basis of the kernel `N = Υ^{K′}_{A′/A}` of the canonical homomorphism
`Ω^1_A ⊗_A K′ → Ω^1_{A′} ⊗_{A′} K′`.*

(i) This time `A′ ⊗_A K = A′/𝔪 A′` is isomorphic to `K[T_1, …, T_r]/𝔟′`, where `𝔟′` is the ideal generated by the
polynomials `T_i^p − a_i`; the hypothesis on the `a_i` entails that this quotient ring is a field `(0_IV, 21.1.8)`,
whence the assertions of (i).

Before proving (ii), we establish the

**Lemma (22.4.4.2).**

<!-- label: 0_IV.22.4.4.2 -->

*Let `Λ` be a ring, `A` a `Λ`-algebra, `𝔍` an ideal of `A` such that the ring `C = A/𝔍` is of characteristic `p > 0`
(which is equivalent to saying that `p · 1 ∈ 𝔍` in `A`). Let `π` be the canonical image of `p · 1` in `𝔍/𝔍²`. If `C` is
a `(Λ/p Λ)`-algebra formally smooth for the discrete topologies, one has a canonical exact sequence*

```text
  (22.4.4.3)   0 → (𝔍/𝔍²)/C · π → Ω^1_{A/Λ} ⊗_A C → Ω^1_{C/Λ} → 0.
```

Set indeed `A′ = A/p A`, `𝔍′ = 𝔍/p A`, so that `C = A′/𝔍′`. Since `A′ = A ⊗_Λ (Λ/p Λ)`, one has
`Ω^1_{A/Λ} ⊗_A A′ = Ω^1_{A′/Λ′}` up to a canonical isomorphism, `Λ′` denoting the ring `Λ/p Λ` `(0_IV, 20.5.5)`.
Applying then the exact sequence `(0_IV, 20.5.14.1)` to the `Λ′`-algebra `C = A′/𝔍′` formally smooth, one obtains the
exact sequence

```text
  0 → 𝔍′/𝔍′² → Ω^1_{A′/Λ′} ⊗_{A′} C → Ω^1_{C/Λ′} → 0
```

and since the homomorphism `Λ → Λ′` is surjective, one has `Ω^1_{C/Λ′} = Ω^1_{C/Λ}` up to a canonical isomorphism
`(0_IV, 20.5.15)`; whence the exact sequence `(22.4.4.3)` by virtue of what precedes.

(ii) Since one has `𝔪² = 0`, we shall again denote by `V′` the ideal `𝔪′` regarded as a `K′`-vector space, and we set

```text
  (22.4.4.4)   V_0 = V/K · p = 𝔪/(𝔪² + p A),   V′_0 = V′/K′ · p = 𝔪′/(𝔪′² + p A′).
```

Applying the exact sequence `(22.4.4.3)` to the case `Λ = ℤ`, to the `ℤ`-algebra `A` (resp. `A′`) and to its ideal `𝔪`
(resp. `𝔪′`), there arises, since `K` (resp. `K′`) is separable over the prime field `ℤ/p ℤ`, hence a `(ℤ/p ℤ)`-algebra
formally smooth `(0_IV, 19.6.1)`, the exact sequences

```text
  (22.4.4.5)   0 → V_0 → Ω^1_A ⊗_A K → Ω^1_K → 0,    0 → V′_0 → Ω^1_{A′} ⊗_{A′} K′ → Ω^1_{K′} → 0.
```

Consider then the diagram `(22.4.4.6)` whose two middle columns are the second sequence `(22.4.4.5)` and the first
tensored by `K′`; since the first exact sequence `(22.4.4.5)` is formed of vector spaces over `K`, the two middle
columns of `(22.4.4.6)` are exact; moreover, the diagram formed by these columns and the horizontal arrows connecting
them is commutative, by virtue of the proof of `(22.4.4.2)` and of the commutativity of the diagram `(0_IV, 20.5.11.3)`.
The last line of `(22.4.4.6)` is the exact sequence obtained from `(0_IV, 20.6.1.1)` by replacing `A`, `B`, `C` by `ℤ`,
`K` and `K′`; the middle line is obtained by tensorisation with `K′` of the exact sequence of `K`-modules deduced from
`(0_IV, 20.6.1.1)` by replacing `A`, `B`, `C` by `ℤ`, `A`, `K` respectively. The diagram formed by these two lines and
the vertical arrows connecting them is commutative by virtue of the commutativity of `(0_IV, 20.6.4.3)`. Note on the
other hand that one is under the conditions of application of `(22.4.1, (ii))`, so the upper line of the diagram
`(22.4.4.6)` is exact; the extreme columns of the diagram

<!-- original page 196 -->

```text
                              0                       0
                              │                       │
                              ▼                       ▼
  (22.4.4.6)            V_0 ⊗_K K′ ───────────────▸ V′_0
                              │                       │
                              ▼                       ▼
  0 ──▸ N ──▸ Ω^1_A ⊗_A K′ ─────────────▸ Ω^1_{A′} ⊗_{A′} K′ ──▸ Ω^1_{A′/A} ⊗_{A′} K′ ──▸ 0
                              │                       │                        ║
                              ▼                       ▼                        ▼
  0 ──▸ Υ_{K′/K} ──▸ Ω^1_K ⊗_K K′ ────────────────▸ Ω^1_{K′} ───────────────▸ Ω^1_{K′/K} ──▸ 0
                              │                       │
                              ▼                       ▼
                              0                       0
```

are thus formed respectively of the kernels and cokernels of the middle horizontal arrows, which completes proving that
the diagram is commutative. Moreover:

**Lemma (22.4.4.7).**

<!-- label: 0_IV.22.4.4.7 -->

*The homomorphisms*

```text
  N → Υ_{K′/K}    and    Ω^1_{A′/A} ⊗_{A′} K′ → Ω^1_{K′/K}
```

*of the diagram `(22.4.4.6)` are bijective.*

Indeed, the snake-diagram (Bourbaki, *Alg. comm.*, chap. I, §1, n° 4, prop. 2) applied to the two middle columns of
`(22.4.4.6)` gives an exact sequence

```text
  0 → N → Υ_{K′/K} → 0 → Ω^1_{A′/A} ⊗_{A′} K′ → Ω^1_{K′/K} → 0.
```

Now, if `t_i` is the canonical image of `T_i` in `A′`, the relation `F_i(t_i) = 0`, together with the fact that in `A′`
one has `p · 1 ∈ 𝔪 A′ ⊂ 𝔪′`, shows at once that `d_{A′} f_i ∈ 𝔪′ Ω^1_{A′}`, hence `d_{A′} f_i ⊗ 1_{K′} = 0`; this proves
that the `d_A f_i ⊗ 1_{K′}` belong to `N`. Moreover, their images in `Υ_{K′/K}` are the `d_K a_i ⊗ 1_{K′}`, which form a
basis of `Υ_{K′/K}` over `K′` `(0_IV, 21.4.7)`; taking account of `(22.4.4.7)`, this completes the proof of `(22.4.4)`.

(22.4.5) Consider now two rings `A`, `B` of characteristic `p > 0`, and two homomorphisms

```text
  A ─i→ B ─j→ A
```

<!-- original page 197 -->

verifying the conditions of `(0_IV, 21.3.1)`. Let furthermore `𝔪` be an ideal of square zero in `A`; set

```text
  K = A/𝔪,   B_{(K)} = B ⊗_A K = B/B i(𝔪)
```

and let

```text
  φ : A → K,   ψ : B → B_{(K)}
```

be the canonical homomorphisms.

Since `φ` is surjective, `Ω^1_{B_{(K)}/A}` identifies canonically with `Ω^1_{B_{(K)}/K}` `(0_IV, 20.5.15)`. Note that,
since `p ≥ 2`, for every `x ∈ 𝔪`, one has `j(i(x)) = x^p = 0`, in other words `j(i(𝔪)) = 0`; by passage to the quotients
one therefore deduces from `j` a homomorphism

```text
  j′ : B_{(K)} → A
```

such that, if `i′ = ψ ∘ i : A → B_{(K)}`, one has

```text
  j′(i′(x)) = x^p   and   i′(j′(y)) = y^p   for x ∈ A and y ∈ B_{(K)}.
```

On setting, following the notations of `(0_IV, 21.3.2)`,

```text
  Θ_{B_{(K)}/A} = Ω^1_{B_{(K)}/A} ⊗_{B_{(K)}} A_{[j′]} = Ω^1_{B_{(K)}/K} ⊗_{B_{(K)}} A_{[j′]},
```

one has `(0_IV, 21.3.2.2)` a canonical homomorphism

```text
  (22.4.5.1)   π_{B_{(K)}/A} : Θ_{B_{(K)}/A} → Ω^1_A.
```

On the other hand, one deduces from `i` and `j`, by passage to the quotients (taking account of the fact that
`j(i(𝔪)) = 0`), homomorphisms

```text
  K ─i_0→ B_{(K)} ─j_0→ K
```

so that one has the commutative diagram

```text
  A ─i→ B ─j→ A
  │     │    │
  φ▼   ψ▼  ▼φ
  K ─i_0→ B_{(K)} ─j_0→ K
```

Clearly furthermore one has

```text
  j_0(i_0(s)) = s^p   and   i_0(j_0(t)) = t^p   for s ∈ K and t ∈ B_{(K)}.
```

One thus defines similarly

```text
  Θ_{B_{(K)}/K} = Ω^1_{B_{(K)}/K} ⊗_{B_{(K)}} K_{[j_0]} = Θ_{B_{(K)}/A} ⊗_A K
```

hence, on tensoring `(22.4.5.1)` with `K`, one obtains a canonical `K`-homomorphism

```text
  (22.4.5.2)   π′_{B_{(K)}/K} = π_{B_{(K)}/A} ⊗ 1_K : Θ_{B_{(K)}/K} → Ω^1_A ⊗_A K.
```

<!-- original page 198 -->

It results at once from the definitions that the diagram

```text
                  π_{B_{(K)}/K}
  Θ_{B_{(K)}/K} ─────────────▸ Ω^1_A ⊗_A K
            ╲                       │
   π_{B_{(K)}/K}                    │ φ_{K/A}
              ╲                     ▼
                Ω^1_K
```

is commutative, `π_{B_{(K)}/K}` being the canonical homomorphism corresponding to `i_0` and `j_0` `(0_IV, 21.3.2.2)`. By
restriction to `Ξ_{B_{(K)}/K} = Ker(π_{B_{(K)}/K})`, the homomorphism `π′_{B_{(K)}/K}` therefore defines a canonical
homomorphism

```text
  (22.4.5.3)   Ξ_{B_{(K)}/K} → Ker(Ω^1_A ⊗_A K → Ω^1_K) = Υ_{K/A}.
```

(22.4.6) The hypotheses and notations being those of `(22.4.5)`, suppose moreover that `𝔪` is a maximal ideal of square
zero, hence `K` a field, and denote by `V` the ideal `𝔪` regarded as a `K`-vector space. Since `K` is a formally smooth
algebra over its prime field `𝔽_p` `(0_IV, 21.5.2)` and `A` is an algebra over `𝔽_p` (so that `Ω^1_A = Ω^1_{A/𝔽_p}`),
one deduces from `(0_IV, 20.5.14)` that one has an exact sequence

```text
  (22.4.6.1)   0 → V → Ω^1_A ⊗_A K → Ω^1_K → 0.
```

One has therefore by `(22.4.5.3)` a homomorphism denoted

```text
  (22.4.6.2)   χ′_{B/A} : Ξ_{B_{(K)}/K} → V
```

which we shall call the *characteristic homomorphism* of the `A`-algebra `B` (relative to `i`, `j` and `𝔪`). It results
from the definitions that for `χ′_{B/A}` to be injective, it is necessary and sufficient that `π′_{B_{(K)}/K}` be
injective, the kernel of the latter being evidently contained in `Ξ_{B_{(K)}/K}`.

**Proposition (22.4.7).**

<!-- label: 0_IV.22.4.7 -->

*Let `A` be a local Artinian ring whose maximal ideal `𝔪` has square zero, `K = A/𝔪` its residue field, `V` the ideal
`𝔪` regarded as a `K`-vector space; suppose that `A` is of characteristic `p > 0`; let*

```text
  (22.4.7.1)   F_i(T_i) = T_i^p − f_i    with f_i ∈ A (1 ≤ i ≤ r)
```

*and denote by `B` the quotient ring of `A[T_1, …, T_r]` by the ideal generated by the `r` polynomials `F_i`. Then:*

*(i) `B` is a local ring.*

*(ii) If `𝔪′` is the maximal ideal of `B`, `K′ = B/𝔪′` its residue field, `V′` the `B`-module `𝔪′/𝔪′²` regarded as a
`K′`-vector space, then, for `rg_K(V) = rg_{K′}(V′)`, it is necessary and sufficient that the characteristic
homomorphism of `K`-vector spaces*

```text
  (22.4.7.2)   χ′_{B/A} : Ξ_{B_{(K)}/K} → V
```

*(cf. `(22.4.6.2)`) be injective.*

Let us still denote by `a_i` (`1 ≤ i ≤ r`) the class of `f_i` mod. `𝔪`; the `a_i` are no longer necessarily
`p`-independent over `K^p`, but one may always suppose that the sub-family

<!-- original page 199 -->

`(a_i)_{s+1 ≤ i ≤ r}` is `p`-free over `K^p` and forms a `p`-basis over `K^p` of the field `K^p(a_1, …, a_r)`, so that
one has

```text
  a_i ∈ K^p(a_{s+1}, …, a_r)   for 1 ≤ i ≤ s.
```

Denote by `A″` the quotient ring of `A[T_{s+1}, …, T_r]` by the ideal generated by the `F_i` of index `i ≥ s + 1`; then,
by `(22.4.4)`, `A″` is a local ring whose maximal ideal is `𝔪″ = 𝔪 A″` (hence of square zero) and the residue field
`K″ = K(a_{s+1}^{1/p}, …, a_r^{1/p})`. One therefore has `a_i ∈ K″^p` for `1 ≤ i ≤ s` and consequently, in `A″`, the
element `f_i`, for `1 ≤ i ≤ s`, can be written

```text
  (22.4.7.3)   f_i = g_i^p + h_i
```

where `g_i ∈ A″` and `h_i ∈ 𝔪″` (since `𝔪″² = 0` and `p 𝔪″ = 0`, it is immediate that `h_i` is determined uniquely by
these conditions). Replacing `T_i` by `T_i + g_i`, one sees therefore that if one sets

```text
  G_i(T_i) = T_i^p + ∑_{k=1}^{p−1} (p choose k) g_i^{p−k} T_i^k − h_i    (1 ≤ i ≤ s)
```

`B` is the quotient ring of `A″[T_1, …, T_s]` by the ideal generated by the `G_i`; now, all the coefficients of `G_i`
except the leading coefficient belong to `𝔪″`, hence one is in the situation of `(22.4.3)`, `B` is a local ring, and its
residue field `K′` is isomorphic to `K″`, which proves (i) (which moreover follows directly from `B^p ⊂ A`, and
consequently there is only one ideal of `B` over `𝔪`).

Note now that for `(22.4.7.2)` to be injective, it is necessary and sufficient that the same hold for

```text
  π′_{B_{(K)}/K} : Ω^1_{B_{(K)}/B_{(K)}} K → Ω^1_A ⊗_A K
```

(by `(22.4.6)`). Now `B_{(K)} = B/𝔪 B` is the quotient algebra of `C = K[T_1, …, T_r]` by the ideal generated by the
polynomials `F̄_i = T_i^p − a_i`, and since `d_{C/K} F̄_i = 0` it follows from `(0_IV, 20.5.13)` that `Ω^1_{B_{(K)}/K}`
is a free `B_{(K)}`-module having for basis the `d_{B_{(K)}/K} t_i`, where `t_i` is the canonical image of `T_i`
(`1 ≤ i ≤ r`). But by definition `(22.4.5)` the canonical image by `j′ : B_{(K)} → A` of a class mod. `𝔪 B` of an
element `x ∈ B` is the element `x^p ∈ A`; one deduces at once, since `t_i^p = f_i`, that the image of
`d_{B_{(K)}/K} t_i ⊗ 1` by `π′_{B_{(K)}/K}` is `d_A f_i ⊗ 1` in `Ω^1_A ⊗_A K`; the condition that `π′_{B_{(K)}/K}` be
injective is therefore equivalent to the fact that the `d_A f_i ⊗ 1_K` are linearly independent over `K`, or
equivalently that their images `d_A f_i ⊗ 1_{K′}` are linearly independent over `K′` in `Ω^1_A ⊗_A K′`.

Now, if one applies `(22.4.4)` to the `A`-algebra `A″`, one sees that the kernel of the canonical homomorphism
`Ω^1_A ⊗_A K′ → Ω^1_{A″} ⊗_{A″} K′` has for basis the `d_A f_i ⊗ 1_{K′}` for `s + 1 ≤ i ≤ r`. The preceding condition
therefore also amounts to saying that the `d_{A″} f_i ⊗ 1_{K′}` are linearly independent in `Ω^1_{A″} ⊗_{A″} K′` for
`1 ≤ i ≤ s`. Now one has `d_{A″} f_i = d_{A″} h_i` by `(22.4.7.3)`; on the other hand, if `V″` is the `K′`-vector space
`𝔪″`, one has `rg_{K′}(V″) = rg_K(V)` `(22.4.1, (ii))`, and the condition `rg_{K′}(V′) = rg_K(V)` is therefore
equivalent to `rg_{K′}(V′) = rg_{K′}(V″)`. But it follows

<!-- original page 200 -->

from `(22.4.3)` that this last relation is equivalent to the fact that the classes `h_i` in `V″` are linearly
independent over `K′`. Now, in `Ω^1_{A″} ⊗_{A″} K′`, the `d_{A″} h_i ⊗ 1_{K′}` are the canonical images
`(0_IV, 20.5.11.2)` of the `h_i` by the *injection* `V″ → Ω^1_{A″} ⊗_{A″} K′` (cf. `(22.4.6.1)`), and this completes
proving `(22.4.7)`.

One has moreover proved:

**Corollary (22.4.7.4).**

<!-- label: 0_IV.22.4.7.4 -->

*For `rg_K(V) = rg_{K′}(V′)`, it is necessary and sufficient that the elements `d_A f_i ⊗ 1_K` (`1 ≤ i ≤ r`) be linearly
independent in the `K`-vector space `Ω^1_A ⊗_A K`.*

**Remark (22.4.8).**

<!-- label: 0_IV.22.4.8 -->

*One may define the homomorphisms `(22.4.5.2)` and `(22.4.6.2)` under slightly different conditions. Let `A` be a ring,
`𝔪` an ideal of square zero in `A`, `K = A/𝔪`, `p` a prime number such that `p · 1 ∈ 𝔪` (in other words `K` is of
characteristic `p`, but not necessarily `A`). Let on the other hand `B` be an `A`-algebra which is a faithfully flat
`A`-module (so that `A ⊂ B`), and suppose one has*

```text
  (22.4.8.1)   y^p ∈ A + p B ⊂ A + 𝔪 B
```

*for every `y ∈ B`. If `y^p = x + p z` with `x ∈ A`, `z ∈ B`, the class mod. `(A ∩ p B)` of `x` is well determined, and
since `A ∩ p B = p A` (since `B` is a faithfully flat `A`-module), one has thus defined a canonical map `j : B → A/p A`,
such that, for `x ∈ A`, `j(x)` is the class of `x^p` mod. `p A`. Moreover, if `y′ ∈ B` and `y′^p = x′ + p z′` with
`x′ ∈ A`, `z′ ∈ B`, it is immediate that the elements `(y + y′)^p − x − x′` and `(y y′)^p − x x′` belong to `p B` by
virtue of the fact that the binomial coefficients `(p choose i)` are multiples of `p` for `1 ≤ i ≤ p − 1`. The map `j`
is therefore a *ring homomorphism*. By composition, one deduces from `j` a homomorphism `j′ : B → A/p A → A/𝔪 = K` and
consequently a homomorphism `j_0 : B_{(K)} → K` such that `j′` is the composite `B → B_{(K)} = B ⊗_A K → K`; moreover,
if `i_0 : K → B_{(K)}` is the canonical map, `i_0` and `j_0` verify the conditions of `(0_IV, 21.3.1)` for the rings of
characteristic `p`, `K` and `B_{(K)}`. This being so, to define a `K`-homomorphism
`π′_{B_{(K)}/K} : Ω^1_{B_{(K)}/K} ⊗_{B_{(K)}} K_{[j_0]} → Ω^1_A ⊗_A K`, it suffices `(0_IV, 20.4.8)` to define a
`K`-derivation*

```text
  (22.4.8.2)   D_0 : B_{(K)} → Ω^1_A ⊗_A K
```

*where the second member is regarded as a `B_{(K)}`-module by means of `j_0`. For this, it suffices to define an
`A`-derivation*

```text
  (22.4.8.3)   D : B → Ω^1_A ⊗_A K
```

*which vanishes in `𝔪 B` (the second member being regarded as `B`-module by means of `j′`). Now, if one has the relation
`y^p = x + p z` with `y ∈ B`, `x ∈ A`, `z ∈ B`, the element `d_A x ⊗ 1_K` of `Ω^1_A ⊗_A K` depends only on the class
`j(y)` mod. `p A` of `x` (hence only on `y`), for every `t ∈ A` one has `d_A(p t) = p d_A(t)`, hence `d_A(p t) ⊗ 1 = 0`
in `Ω^1_A ⊗_A K = Ω^1_A / 𝔪 Ω^1_A`, since `p · 1 ∈ 𝔪`. One may therefore take*

```text
  D(y) = d_A x ⊗ 1_K.
```

*The fact that `D` is a derivation results easily from the fact that `j` is a ring homomorphism; moreover, for `t ∈ A`,
one has `d_A(t^p x) = t^p d_A(x) + p t^{p−1} x d_A(t)` and one extracts from this that `D(t y) = t D(y)`, hence `D` is
an `A`-derivation; finally, if one has moreover `t ∈ 𝔪`, one has*

<!-- original page 201 -->

*`D(t y) = t D(y) = 0` since `Ω^1_A ⊗_A K` is annihilated by `𝔪`. One has thus defined the homomorphism `(22.4.5.2)`
sought, and it is immediate to verify that the composite homomorphism*

```text
                          π_{B_{(K)}/K}
  Θ_{B_{(K)}/K} ─────────────────────────▸ Ω^1_A ⊗_A K → Ω^1_K
```

*is still the canonical homomorphism `π_{B_{(K)}/K}` (relative to `i_0` and `j_0`). One has therefore also a canonical
homomorphism analogous to `(22.4.5.3)`.*

*If now `K` is a field, `A/p A` is an `𝔽_p`-algebra, and one has the exact sequence \`(0_IV, 20.5.14)*

```text
  0 → V/p A → Ω^1_{A/p A} ⊗_{A/p A} K → Ω^1_K → 0
```

*and on the other hand one has the exact sequence \`(0_IV, 20.5.12.1)*

```text
  p A → Ω^1_A ⊗_A (A/p A) → Ω^1_{A/p A} → 0
```

*which shows, on tensoring with `K`, that the `K`-vector spaces `Ω^1_A ⊗_A K` and `Ω^1_{A/p A} ⊗_{A/p A} K` are
isomorphic. The analogue of `(22.4.6.2)` is therefore here a homomorphism*

```text
  (22.4.8.4)   Ξ_{B_{(K)}/K} → V/p A = 𝔪/(𝔪² + p A).
```

*This said, the criterion `(22.4.7)`, where one replaces `V` and `V′` by `V/p A` and `V′/p B` respectively, remains
valid supposing only that `K` is of characteristic `p > 0` (in other words, that `p · 1 ∈ 𝔪` in `A`), and that the
`F_i(T_i)` are of the more general form `(22.4.4.1)`: indeed, `B` is a free `A`-module (hence faithfully flat), and it
suffices to take up again the reasoning of `(22.4.7)`, replacing therein `(22.4.6.2)` by `(22.4.8.4)` and `V″` by
`V″/p A″`.*

### 22.5. Geometrically regular algebras and formally smooth algebras

**Proposition (22.5.1).**

<!-- label: 0_IV.22.5.1 -->

*Let `A` be a regular local ring, `A′` a local ring containing `A` and which is a finite `A`-algebra, `𝔪` (resp. `𝔪′`)
the maximal ideal of `A` (resp. `A′`), `K = A/𝔪` (resp. `K′ = A′/𝔪′`) its residue field. For `A′` to be a regular ring,
it is necessary and sufficient that one have*

```text
  (22.5.1.1)   rg_K(𝔪/𝔪²) = rg_{K′}(𝔪′/𝔪′²).
```

Indeed, the first member of `(22.5.1.1)` is `dim(A)` `(0_IV, 17.1.1)` and since `A ⊂ A′` and `A′` is a finite
`A`-algebra, `dim(A′) = dim(A)` `(0_IV, 16.1.5)`; the equality `(22.5.1.1)` is therefore necessary and sufficient for
`A′` to be regular `(0_IV, 17.1.1)`.

**Remarks (22.5.2).**

<!-- label: 0_IV.22.5.2 -->

*(i) Let `A_1 = A/𝔪²`, `A′_1 = A′ ⊗_A A_1 = A′/𝔪² A′`; since `𝔪² A′ ⊂ 𝔪′²`, `𝔪′_1 = 𝔪′/𝔪 A′` is the maximal ideal of
`A′_1` and `𝔪′_1/𝔪′_1²` is a `K′`-vector space isomorphic to `𝔪′/𝔪′²`; the regularity condition for `A′` therefore
depends only on the structure of the `A_1`-algebra `A′_1`, which will allow us below to apply the preliminary results of
`(22.4)` on the finite algebras over Artinian rings.*

*(ii) It results from the proof of `(22.5.1)` and from `(0_IV, 16.2.6.1)` that one has in any case*

```text
  (22.5.2.1)   rg_K(𝔪/𝔪²) ≤ rg_{K′}(𝔪′/𝔪′²).
```

<!-- original page 202 -->

*(iii) Suppose that `A` and `A′` satisfy the general hypotheses of `(22.4.1)`. One knows `(0_IV, 19.8.10)` that there
exists a regular local ring `B`, of maximal ideal `𝔫`, such that `A` is isomorphic to `B/𝔫²`; let `G_i ∈ B[T_i]` be a
unitary polynomial whose canonical image in `A[T_i]` is `F_i` (`1 ≤ i ≤ r`); then, if `B′` is the quotient ring of
`B[T_1, …, T_r]` by the ideal generated by the `G_i`, it is clear that `B′` is a free `B`-module of rank `d` and that
`A′ = B′ ⊗_B A = B′/𝔫² B′`; since `A′` is supposed to be a local ring, so is `B′`, and if `𝔫′` is the maximal ideal of
`B′`, `B′/𝔫′` is isomorphic to `K′` and `𝔫′/𝔫′²` isomorphic to `𝔪′/𝔪′²` as vector space over `K′`; the inequality
`(22.5.2.1)` therefore shows that under the hypotheses of `(22.4.1)`*

```text
  (22.5.2.2)   rg_K(V) ≤ rg_{K′}(𝔪′/𝔪′²).
```

**Corollary (22.5.3).**

<!-- label: 0_IV.22.5.3 -->

*Let `A` be a regular local ring, `𝔪` its maximal ideal, `T_i` (`1 ≤ i ≤ r`) indeterminates, and for each `i`, let*

```text
  (22.5.3.1)   F_i(T_i) = T_i^{d_i} + ∑_{1 ≤ k ≤ d_i} c_{ik} T_i^{d_i − k}
```

*be a unitary polynomial of `A[T_i]`, such that `d_i ≥ 2` for every `i` and `c_{ik} ∈ 𝔪`. Let `A′` be the quotient of
the polynomial ring `A[T_1, …, T_r]` by the ideal generated by the `r` polynomials `F_i`. Then:*

*(i) `A′` is a local ring, and its residue field `K′` is isomorphic to the residue field `K` of `A`.*

*(ii) For `A′` to be a regular ring, it is necessary and sufficient that the classes `ξ_i` mod. `𝔪²` of the elements
`c_{i, d_i}` (`1 ≤ i ≤ r`) be linearly independent over `K`.*

Indeed, with the notations of `(22.5.2, (i))`, if `F̄_i` denotes the polynomial of `A_1[T_i]` obtained by applying to
the coefficients of `F_i` the homomorphism `A → A_1`, `A′_1` is defined from `A_1` and the polynomials `F̄_i` as in
`(22.4.1)`, and the conclusion therefore results from `(22.5.1)` and `(22.4.3)`.

**Theorem (22.5.4).**

<!-- label: 0_IV.22.5.4 -->

*Let `A` be a regular local ring, `K` its residue field; suppose that `K` is of characteristic `p > 0`; let*

```text
  (22.5.4.1)   F_i(T_i) = T_i^p + p ∑_{k=1}^{p−1} c_{ik} T_i^{p−k} − f_i
```

*with `c_{ik} ∈ A` and `f_i ∈ A` (`1 ≤ i ≤ r`); let `B` be the quotient ring of `A[T_1, …, T_r]` by the ideal generated
by the `r` polynomials `F_i`. Then `B` is a local ring, and the following conditions are equivalent:*

*a) `B` is regular;*

*b) the elements `d_A f_i ⊗ 1_K` (`1 ≤ i ≤ r`) are linearly independent in the `K`-vector space `Ω^1_A ⊗_A K`;*

*c) if `B′ = B/𝔪² B` and if one sets `Ξ_{B_{(K)}/K} = Ξ_{B′_{(K)}/K}` `(22.4.5)`, the characteristic homomorphism
`Ξ_{B_{(K)}/K} → 𝔪′/𝔪′²` `(22.4.6.2)` is injective.*

Indeed, `B′` is again defined from `A_1 = A/𝔪²` and the polynomials `F̄_i` obtained by applying to the `F_i` the
homomorphism `A → A_1`. Taking account of the fact that `Ω^1_{A_1} ⊗_{A_1} K` is canonically isomorphic to `Ω^1_A ⊗_A K`
`(0_IV, 20.5.12, (ii))`, the theorem results from `(22.5.1)` and `(22.4.7.4)`, using remark `(22.4.8)` when `A_1` is not
of characteristic `p`.

<!-- original page 203 -->

(22.5.5) Let `k` be a field of characteristic `p > 0`, `A` a local ring, `k′` a finite radicial extension of `k` such
that `k′^p ⊂ k`, `𝔪` the maximal ideal of `A`, `K = A/𝔪` its residue field; recall that `A′ = A ⊗_k k′` is a local ring
whose residue field is the same as that of the local ring `K ⊗_k k′` (Bourbaki, *Alg. comm.*, chap. V, §2, n° 3, lemma
4). Note that one has `A′_{(K)} = A′ ⊗_{A′} K = K ⊗_k k′`, and consequently `(0_IV, 21.3.6)`

```text
  (22.5.5.1)   Θ_{A′_{(K)}/K} = Θ_{k′/k} ⊗_k K
```

up to a canonical isomorphism. Moreover, one knows `(0_IV, 21.4.7)` that one has `Ξ_{k′/k} = 0`, in other words the
canonical homomorphism `(0_IV, 21.3.2.2)`

```text
  π_{k′/k} : Θ_{k′/k} → Ω^1_k
```

is injective, so one has a canonical injection

```text
  (22.5.5.2)   Θ_{A′_{(K)}/K} → Ω^1_k ⊗_k K
```

which is made explicit as follows (taking account of `(22.5.5.1)`): for every `x′ ∈ k′`, to the element
`d_{A′_{(K)}/K}(x′ ⊗ 1_K) ⊗ 1_K` of `Ω^1_{A′_{(K)}/A′_{(K)}} K`, one makes correspond the element `d_k(x′^p) ⊗ 1_K` of
`Ω^1_k ⊗_k K`.

**Lemma (22.5.6).**

<!-- label: 0_IV.22.5.6 -->

*With the notations of `(22.5.5)`:*

*(i) The kernel of the canonical homomorphism `π_{A′_{(K)}/K}` `(0_IV, 21.3.2.2)` identifies via `(22.5.5.2)` with
`(Θ_{k′/k} ⊗_k K) ∩ Υ_{K/k}`.*

*(ii) Let `A_1 = A/𝔪²`, `A′_1 = A_1 ⊗_k k′ = A′/𝔪² A′`; then the characteristic homomorphism `χ′_{A′_1/A_1}`
`(22.4.6.2)` identifies with the restriction of the characteristic homomorphism `χ_{A/k} : Υ_{K/k} → V = 𝔪/𝔪²`
`(0_IV, 20.6.24)` to `(Θ_{k′/k} ⊗_k K) ∩ Υ_{K/k}`.*

(i) By virtue of `(0_IV, 20.6.9)`, applied by replacing `Λ` by the prime field, `B` by `k`, `C` by `K` and `E` by
`A_1 = A/𝔪²` (extension of `K` by `V = 𝔪/𝔪²`), it suffices (cf. `(22.5.5)`) to verify that if `x′ ∈ k′` and if `y ∈ A_1`
is an element whose class mod. `𝔪/𝔪²` is `x′^p ∈ k`, then the image of `d_k(x′^p) ⊗ 1_K` by the canonical homomorphism
`Ω^1_k ⊗_k K → Ω^1_A ⊗_A K` is `d_A z ⊗ 1_K`, which results from the definitions.

(ii) Since `A′_{(K)} = K ⊗_k k′ = (A′_1)_{(K)}` (by virtue of the relation `K = A_1/(𝔪/𝔪²)`), `Θ_{A′_1/k}` identifies
with `Θ_{A′_{(K)}/K}`, and the verification results from the same calculation as in (i) and from the definition
`(22.4.5.2)` of `π′_{(A′_1)_{(K)}/K}`.

**Proposition (22.5.7).**

<!-- label: 0_IV.22.5.7 -->

*Let `k` be a field of characteristic `p > 0`, `A` a `k`-algebra which is a regular local ring, `𝔪` its maximal ideal,
`K = A/𝔪` its residue field; let `V = 𝔪/𝔪²`, regarded as a `K`-vector space. Let `k′` be a finite extension of `k` such
that `k′^p ⊂ k`, and `A′ = A ⊗_k k′`; for the local ring `A′` to be regular, it is necessary and sufficient that the
restriction of the characteristic homomorphism `χ_{A/k} : Υ_{K/k} → V` `(0_IV, 20.6.24)` to `(Θ_{k′/k} ⊗_k K) ∩ Υ_{K/k}`
be injective.*

It is required to prove that the condition of the statement is equivalent to `(22.5.1.1)`, denoting by `𝔪′` the maximal
ideal of `A′`, by `K′ = A′/𝔪′` its residue field. With the notations of remark `(22.5.2, (i))`, one has
`A′_1 = A_1 ⊗_k k′`. Now, let `(a_i)_{1 ≤ i ≤ r}` be a `p`-basis of `k′` over `k`, so that `a_i^p = b_i ∈ k`, and `k′`
is isomorphic to the quotient of the polynomial ring

<!-- original page 204 -->

`k[T_1, …, T_r]` by the ideal generated by the polynomials `F_i = T_i^p − b_i` (`1 ≤ i ≤ r`); one deduces that `A′_1` is
isomorphic to the quotient of the polynomial ring `A_1[T_1, …, T_r]` by the ideal generated by the `F_i`. One may then
apply the criterion `(22.4.7)`, and the condition of the statement therefore amounts to the fact that `χ′_{A′_1/A_1}` is
injective; one concludes with the aid of `(22.5.6)`.

We can now prove the converse of `(0_IV, 19.6.5)`:

**Theorem (22.5.8).**

<!-- label: 0_IV.22.5.8 -->

*Let `k` be a field, `p` its characteristic exponent, `A` a Noetherian local `k`-algebra. The following conditions are
equivalent:*

*a) `A` is a `k`-algebra formally smooth (for its preadic topology).*

*b) `A` is geometrically regular over `k`.*

*b′) For every finite extension `k′` of `k` such that `k′^p ⊂ k`, `A′ = A ⊗_k k′` is a regular ring.*

Taking account of `(0_IV, 19.6.6)`, one may reduce to the case `p > 1`.

The fact that a) implies b) is none other than `(0_IV, 19.6.5)`, and b) trivially entails b′). We show that b′) entails
that the conditions of `(22.2.2)` are satisfied; this is evident for the first `(0_IV, 17.1.1)` since b′) implies first
that `A` is regular. On the other hand, let `(x_α)_{α ∈ I}` be a `p`-basis of `k^{1/p}` over `k`; one knows that the
elements `d_k(x_α^p)` form a basis of the `k`-vector space `Ω^1_k` `(0_IV, 21.4.5)`, hence the elements
`d_k(x_α^p) ⊗ 1_K` form a basis of the `K`-vector space `Ω^1_k ⊗_k K`. One concludes (cf. `(22.5.5)`) that when `k′`
runs through the set of subextensions of `k^{1/p}`, finite over `k`, the family of subspaces `Θ_{k′/k} ⊗_k K` of
`Ω^1_k ⊗_k K` is filtering increasing and has for union `Ω^1_k ⊗_k K`. It follows then from `(22.5.7)` that condition
b′) entails that `χ_{A/k}` is injective, which is none other than condition (ii) of `(22.2.2)`.

**Corollary (22.5.9).**

<!-- label: 0_IV.22.5.9 -->

*Let `k` be a field, `A` a Noetherian local `k`-algebra formally smooth. Then, for every prime ideal `𝔭` of `A`, the
local ring `A_𝔭` is a `k`-algebra formally smooth (for the `𝔭`-preadic topology).*

Indeed, with the notations of `(22.5.8, b′)`, it suffices to show that the local ring `A_𝔭 ⊗_k k′` is regular; but as it
is a ring of fractions of the local ring `A ⊗_k k′` and the latter is regular by hypothesis, the same holds of
`A_𝔭 ⊗_k k′` `(0_IV, 17.3.6)`.

**Remarks (22.5.10).**

<!-- label: 0_IV.22.5.10 -->

*(i) The conclusion of `(22.5.8)` is in default when, in condition b′), one restricts to monogenic extensions
`k′ = k(x)` of `k` (with `x^p ∈ k`). It may indeed happen that for *all* these extensions `k′`, one has
`Υ_{K/k} ∩ (Θ_{k′/k} ⊗_k K) = 0`, even though `Υ_{K/k} ≠ 0`; this means that for every `x ∈ k^{1/p}` such that `x ∉ k`,
one must have `d_k(x^p) ⊗ 1 ∉ Υ_{K/k}`, or equivalently `d_K(x^p) ≠ 0`, that is to say `x^p ∉ K^p`; in other words, one
must have `K^p ∩ k = k^p`, even though `K` be an inseparable extension of `k`. Now, one easily constructs examples of
such extensions: start from a perfect field `k_0` of characteristic `p > 0`, let `X`, `Y`, `Z` be three indeterminates
and set `k = k_0(X, Y)` and `K = k(X^{1/p} + Z Y^{1/p})`; one easily verifies that `K` satisfies the preceding
conditions, hence `Υ_{K/k} ≠ 0`. Apply now the lemma `(22.2.5.2)` taking `V = K` and for `h` the zero homomorphism; `A`
is then a discrete valuation ring having `K` for residue field, with `χ_{A/k} = 0`, and is therefore not a `k`-algebra
formally smooth by `(22.2.2)`; however `A ⊗_k k′` is a regular ring for every monogenic extension `k′ ⊂ k^{1/p}` of
`k`.*

<!-- original page 205 -->

*(ii) The corollary `(22.5.9)` leads to consideration of the following question: if `A` is a Noetherian `k`-algebra,
under what conditions is the set of prime ideals `𝔭 ∈ Spec(A)` such that `A_𝔭` is a `k`-algebra formally smooth open? We
shall address certain particular cases of this later.*

### 22.6. Zariski's Jacobian criterion

**Theorem (22.6.1)** (Jacobian criterion of formal smoothness).

<!-- label: 0_IV.22.6.1 -->

*Let `A`, `B` be two topological rings, `u : A → B` a continuous homomorphism making `B` a `A`-algebra formally smooth,
`𝔍` an ideal of `B` (not necessarily closed), `C = B/𝔍` the quotient topological `A`-algebra. For `C` to be a
`A`-algebra formally smooth, it is necessary and sufficient that the canonical homomorphism (cf. `(0_IV, 20.5.11.2)`)*

```text
  (22.6.1.1)   δ_{C/B/A} : 𝔍/𝔍² → Ω^1_{B/A} ⊗_B C
```

*be formally left-invertible (cf. `(0_IV, 19.1.5)`).*

Indeed, to say that `B` (resp. `C`) is a `A`-algebra formally smooth signifies `(0_IV, 19.4.4)` that one has
`Exalcotop_A(B, L) = 0` (resp. `Exalcotop_A(C, L) = 0`) for every discrete `B`-module (resp. `C`-module) `L` annihilated
by an open ideal of `B` (resp. `C`). Since by hypothesis `Exalcotop_A(B, L) = 0` for every discrete `C`-module `L`
annihilated by an open ideal of `C`, to say that `C` is a `A`-algebra formally smooth therefore signifies that the
canonical homomorphism `Exalcotop_A(C, L) → Exalcotop_A(B, L)` is injective, and the theorem results from
`(0_IV, 20.7.8)`.

Recall `(0_IV, 19.5.3)` that when `B` and `C` are `A`-algebras formally smooth, `𝔍/𝔍²` is a formally projective
topological `C`-module; moreover, the canonical homomorphisms `φ_n : S_C^n(𝔍/𝔍²) → 𝔍^n/𝔍^{n+1}` are formal bimorphisms
when `B` is supposed to be a preadmissible ring.

**Corollary (22.6.2).**

<!-- label: 0_IV.22.6.2 -->

*The hypotheses and notations being those of `(22.6.1)`, suppose moreover that in `B` the square of every open ideal is
open, and that on `𝔍` the topology induced by that of `B` is identical to the topology deduced from that of `B`
`(0_IV, 19.0)` (note that these two conditions are satisfied when `B` is Noetherian and its topology preadic
`(0_I, 7.3.2)`, or if the topology of `B` is the `𝔍`-preadic topology). Let `(𝔟_λ)` be a fundamental system of open
ideals of `B` and set `B_λ = B/𝔟_λ` for every `λ`. Then:*

*(i) The following conditions are equivalent:*

*a) `C` is a `A`-algebra formally smooth.*

*b) For every `λ`, the homomorphism of `B_λ`-modules*

```text
  (22.6.2.1)   (𝔍/𝔍²) ⊗_B B_λ → Ω^1_{B/A} ⊗_B B_λ
```

*deduced from `δ_{C/B/A}` by tensorisation, is left-invertible (in other words an isomorphism onto a direct factor of
`Ω^1_{B/A} ⊗_B B_λ`).*

*(ii) Suppose moreover that the topological ring `C` is preadmissible `(0_I, 7.1.2)` and*

<!-- original page 206 -->

*let `𝔏` be an ideal of definition of `C`; then conditions a) and b) of (i) are equivalent also to:*

*c) The homomorphism of `(C/𝔏)`-modules*

```text
  (𝔍/𝔍²) ⊗_C (C/𝔏) → Ω^1_{B/A} ⊗_B (C/𝔏)
```

*is left-invertible.*

The hypotheses entail that on `Ω^1_{B/A}` the topology is deduced from that of `B` `(0_IV, 20.4.5)`, hence (i) results
from `(22.6.1)` and `(0_IV, 19.1.7)`. On the other hand, recall `(0_IV, 20.4.9)` that since `B` is a `A`-algebra
formally smooth, `Ω^1_{B/A}` is a formally projective `B`-module, hence `Ω^1_{B/A} ⊗_B B_λ` is a projective `B_λ`-module
for every `λ` `(0_IV, 19.2.4)`; the equivalence of c) with a) and b) when `C` is preadmissible then results from
`(0_IV, 19.1.9)`.

In particular:

**Corollary (22.6.3).**

<!-- label: 0_IV.22.6.3 -->

*Let `A` be a ring, `B` a `A`-algebra, `𝔍` an ideal of `B`, `C = B/𝔍`; suppose `A`, `B`, `C` equipped with the discrete
topologies and that `B` is a `A`-algebra formally smooth. For `C` to be a `A`-algebra formally smooth, it is necessary
and sufficient that the canonical homomorphism `(22.6.1.1)` be left-invertible.*

Note that since every `A`-algebra `C` is a quotient of a polynomial algebra `A[T_α]_{α ∈ I}`, and the latter is formally
smooth `(0_IV, 19.3.3)`, the criterion `(22.6.3)` permits in principle to recognize whether `C` is a `A`-algebra
formally smooth.

**Proposition (22.6.4).**

<!-- label: 0_IV.22.6.4 -->

*Let `A` be a ring, `B` a `A`-algebra formally smooth (for the discrete topologies), `𝔍` an ideal of `B`, `C = B/𝔍`;
suppose that `𝔍/𝔍²` is a `C`-module of finite type. Let `𝔭` be a prime ideal of `C`, `k(𝔭)` the residue field of `C_𝔭`,
`𝔭′` the inverse image of `𝔭` in `B`, `𝔮` the prime ideal of `A` inverse image of `𝔭′`. The following conditions are
equivalent:*

*a) `C_𝔭` is a `A_𝔮`-algebra formally smooth (for the discrete topologies).*

*a′) `C_𝔭` is a `A`-algebra formally smooth (for the discrete topologies).*

*b) The canonical homomorphism*

```text
  (22.6.4.1)   (𝔍/𝔍²) ⊗_C k(𝔭) → Ω^1_{B/A} ⊗_B k(𝔭)
```

*is injective.*

*c) There exists `f ∈ C − 𝔭` such that `C_f` is a `A`-algebra formally smooth.*

*If moreover `B` is Noetherian, the preceding conditions are also equivalent to*

*d) `C_𝔭` is a `A_𝔮`-algebra formally smooth for the `𝔭`-preadic topology on `C_𝔭` and the discrete topology (or the
`𝔮`-preadic topology) on `A_𝔮`.*

Since `A_𝔮` is a `A`-algebra formally smooth `(0_IV, 19.3.5, (iv) and (ii))`, one already knows that a) and a′) are
equivalent `(0_IV, 19.3.5, (ii))`. One has `C_𝔭 = B_{𝔭′}/𝔍 B_{𝔭′}` and `B_{𝔭′}` is a `A`-algebra formally smooth for the
discrete topology `(0_IV, 19.3.5, (iv))`; moreover `Ω^1_{B_{𝔭′}/A} = (Ω^1_{B/A})_{𝔭′}` `(0_IV, 20.5.9)`. The equivalence
of a′) and b) then results from the application of `(22.6.3)` to `B_{𝔭′}` and `C_𝔭`, taking account of the fact that
`Ω^1_{B/A}` is a projective `B`-module (`(0_IV, 20.4.9)` and `(0_IV, 19.2.1)`) and `𝔍/𝔍²` a `B`-module of finite type,
and using `(0_IV, 19.1.12)`. The application of `(0_IV, 19.1.12)` also proves the equivalence of b) and c). Finally,
note that since `B_{𝔭′}` is a `A_𝔮`-algebra formally smooth for the discrete topologies

<!-- original page 207 -->

`(0_IV, 19.3.5, (iv))`, `B_{𝔭′}`, equipped with the `𝔭′`-preadic topology, is still a `A_𝔮`-algebra formally smooth when
one takes on `A_𝔮` the discrete topology or the `𝔮`-preadic topology `(0_IV, 19.3.8)`. To show the equivalence of b) and
d) when `B` is Noetherian, apply `(22.6.2)` to the ring `A_𝔮` discrete (or `𝔮`-preadic) and to the ring `B_{𝔭′}`,
equipped with the `𝔭′`-preadic topology; since `C_𝔭` is preadmissible and `𝔭 C_𝔭` is an ideal of definition for its
topology, one may invoke the equivalence of c) and a) in `(22.6.2)`.

**Corollary (22.6.5).**

<!-- label: 0_IV.22.6.5 -->

*Under the general hypotheses of `(22.6.4)`, the set of `𝔭 ∈ Spec(C)` such that `C_𝔭` is a `A`-algebra formally smooth
(or a `A_𝔮`-algebra formally smooth, denoting by `𝔮` the inverse image of `𝔭` in `A`) for the discrete topologies, is
open in `Spec(C)`.*

This results from form c) of `(22.6.4)`. Note that when `B` is Noetherian, one may replace the discrete topologies by
the preadic topologies.

**Corollary (22.6.6).**

<!-- label: 0_IV.22.6.6 -->

*Under the general hypotheses of `(22.6.4)`, the following conditions are equivalent:*

*a) `C` is a `A`-algebra formally smooth (for the discrete topologies).*

*b) For every `𝔭 ∈ Spec(C)` (or only for every maximal ideal `𝔭` of `C`), `C_𝔭` is a `A`-algebra formally smooth (or a
`A_𝔮`-algebra formally smooth, denoting by `𝔮` the inverse image of `𝔭` in `A`) for the discrete topologies.*

*Moreover, when `B` is Noetherian, one may in b) replace the discrete topologies by the preadic topologies on `A_𝔮` and
`C_𝔭`.*

The last assertion results from `(22.6.4)`. By virtue of `(22.6.3)`, condition a) amounts to the fact that the
homomorphism `(22.6.1.1)` is left-invertible; the equivalence of a) and b) therefore results from `(0_IV, 19.1.14)`,
taking account of the fact that `Ω^1_{B/A}` is a projective `B`-module and `𝔍/𝔍²` a `C`-module of finite type.

**Proposition (22.6.7).**

<!-- label: 0_IV.22.6.7 -->

*Let `k_0` be a field, `k` a separable extension of `k_0`, `C` a `k`-algebra of finite type.*

*(i) Let `𝔭` be a prime ideal of `C`. The following conditions are equivalent:*

*a) `C_𝔭` is a `k_0`-algebra formally smooth for the discrete topology.*

*b) `C_𝔭` is a `k_0`-algebra formally smooth for the `𝔭`-preadic topology.*

*c) There exists `f ∈ C − 𝔭` such that `C_f` is a `k_0`-algebra formally smooth for the discrete topology.*

*d) `C_𝔭` is a geometrically regular ring `(0_IV, 19.6.5)` over `k_0`.*

*Moreover the set of `𝔭 ∈ Spec(C)` having any one of these properties is open in `Spec(C)`.*

*(ii) The following conditions are equivalent:*

*a) `C` is a `k_0`-algebra formally smooth for the discrete topology.*

*b) Every `𝔭 ∈ Spec(C)` satisfies the equivalent conditions of (i).*

*c) Every maximal ideal `𝔪` of `C` satisfies the equivalent conditions of (i).*

*d) For every extension `k′` of `k_0`, `C ⊗_{k_0} k′` is a regular ring `(0_IV, 17.3.6)`; one says again that `C` is a
geometrically regular ring over `k_0`.*

<!-- original page 208 -->

*(iii) Let `B = k[T_1, …, T_r]` be a polynomial algebra, `𝔍` an ideal of `B` such that `C` is isomorphic to `B/𝔍`. Let
`𝔮` be a prime ideal of `B` containing `𝔍` and set `𝔭 = 𝔮/𝔍`. The conditions of (i) are then still equivalent to the
following ("Zariski's Jacobian criterion"):*

*e) There exists a system of elements `(f_i)_{1 ≤ i ≤ m}` of `𝔍`, generating the ideal `𝔍_𝔮` in `B_𝔮`, and
`k_0`-derivations `D_j` of `B` into itself (`1 ≤ j ≤ m`) such that `det(D_j(f_i)) ∉ 𝔮`.*

One knows that `C` is always isomorphic to a `k`-algebra of the form `B/𝔍`. Since `B` is a `k`-algebra formally smooth
`(0_IV, 19.3.3)` and `k`, being separable over `k_0`, is a `k_0`-algebra formally smooth `(0_IV, 19.6.1)`, `B` is a
`k_0`-algebra formally smooth `(0_IV, 19.3.5, (ii))`. The equivalence of conditions a), b), c) of (i) therefore results
from `(22.6.4)`, and that of a), b), c) in (ii) results from `(22.6.6)`; the equivalence of a) and d) in (i) results
from `(22.5.8)`; since every localization of `C ⊗_{k_0} k′` is also a localization of `C_𝔭 ⊗_{k_0} k′` for a suitable
prime ideal `𝔭 ∈ Spec(C)`, the equivalence of d) and b) in (ii) results from the equivalence of d) and a) in (i).
Finally, since `Ω^1_{B/k_0}` is a projective `B`-module, the equivalence of Zariski's criterion e) and the other
conditions of (i) follows from `(0_IV, 19.1.12)` and `(22.6.3)`, taking account of `(0_IV, 20.4.8)`.

Zariski was in fact interested in a differential criterion of *regularity* for the local rings `C_𝔭`. Since it amounts
to the same to say that a Noetherian local ring containing a field is regular or is formally smooth as algebra over its
prime subfield `(0_IV, 19.6.4)`, one obtains at once such a criterion by replacing `k_0` by the prime subfield of `k` in
`(22.6.7)`; in particular, one obtains the following result, which we shall later find again `(IV, 6.12.5)` as a
particular case of more general results of Nagata:

**Corollary (22.6.8)** (Zariski).

<!-- label: 0_IV.22.6.8 -->

*Let `C` be a finite-type algebra over a field. Then the set of `𝔭 ∈ Spec(C)` such that `C_𝔭` is a regular local ring is
open in `Spec(C)`.*

**Remarks (22.6.9).**

<!-- label: 0_IV.22.6.9 -->

*(i) The statements of `(22.6.7)` are still valid if instead of supposing `k` separable over `k_0`, one supposes only
that it is of finite radicial multiplicity, in other words `(0_IV, 19.6.6)` that there exists a finite radicial
extension `k′_0` of `k_0` such that the residue field of the local Artinian ring `k ⊗_{k_0} k′_0` is a separable
extension `k′` of `k′_0`. There then exists a `k_0`-monomorphism `k′ → k ⊗_{k_0} k′_0` which, composed with the
canonical homomorphism `k ⊗_{k_0} k′_0 → k′`, gives the identity, since `k′` is a `k′_0`-algebra formally smooth
`(0_IV, 19.6.1)`; one concludes that `C ⊗_{k_0} k′_0` is equipped with a structure of `k′`-algebra of finite type, and
since `k′` is separable over `k′_0`, one may apply `(22.6.7)` to this `k′`-algebra; one concludes our assertion by
applying `(0_IV, 19.4.7)`. Since we shall not have to make use of this generalization, we leave the detail to the
reader. We do not know on the other hand whether the results of `(22.6.7)` are valid without any hypothesis on the
extension `k` of `k_0`.*

*(ii) Under the general hypotheses of `(22.6.7)`, let `(k_α)` be a decreasing filtered family of subfields of `k`
containing `k_0` and such that `⋂_α k_α(k^p) = k_0(k^p)` (where `p` is the characteristic exponent of `k_0`). Using a
dimension-counting method due to Nagata, one can show that, in the Jacobian criterion `(22.6.7, (iii))`, one may
restrict to derivations `D_j` of `B` which are `k_α`-derivations for a suitable `α`.*

<!-- original page 209 -->

*The interest of this result is that there are always such families `(k_α)` for which `[k : k_α]` is finite
`(0_IV, 21.8.6)`. We shall not prove this refinement of Zariski's criterion, of which we shall not have to make use. In
`(22.7)`, we shall give, for complete local rings, a variant (also due to Nagata) of Zariski's criterion, which is
proved essentially by the same method (with somewhat greater technical difficulties).*

### 22.7. Nagata's Jacobian criterion

(22.7.1) Nagata's Jacobian criterion is the analogue of Zariski's Jacobian criterion, but for quotient rings of rings of
formal series over a field. We shall give, like Nagata `[31]`, two versions, presented here as criteria of formal
smoothness.

**Proposition (22.7.2).**

<!-- label: 0_IV.22.7.2 -->

*Let `k` be a field, `A = k[[T_1, …, T_r]]` a ring of formal series over `k`, equipped with its usual structure of
`k`-algebra, `𝔮` an ideal of `A`, `B = A/𝔮`. Let `𝔭` be a prime ideal of `A` containing `𝔮`. Suppose there exists a
sub-`k`-algebra `C′` of `C = A/𝔭`, isomorphic to an algebra of formal series `k[[X_1, …, X_s]]`, such that `C` is finite
over `C′` and that the field of fractions `L` of `C` is a separable extension of `L′ = k((X_1, …, X_s))` (hypothesis
always satisfied if `k` is of characteristic `0`). Then the following conditions are equivalent:*

*a) `B_𝔭 = A_𝔭/𝔮 A_𝔭` is a `k`-algebra formally smooth for the `𝔭`-preadic topology.*

*b) There exist `k`-derivations `D_i` (`1 ≤ i ≤ m`) of `A` into itself, and elements `f_i` (`1 ≤ i ≤ m`) of `𝔮`, such
that the images of the `f_i` in `𝔮 A_𝔭` generate this ideal of `A_𝔭`, and that one has `det(D_i f_j) ∉ 𝔭`.*

*c) `B_𝔭` is a regular ring.*

The residue field of `B_𝔭` is `k(𝔭)`; since `k((X_1, …, X_s))` is separable over `k` `(0_IV, 21.9.6.4)`, `k(𝔭)` is
separable over `k` by hypothesis, and one already knows that under these conditions properties a) and c) are equivalent
`(0_IV, 19.6.4)`. Moreover `A_𝔭` is a regular ring (`(0_IV, 17.1.4)` and `(0_IV, 17.3.2)`), and since its residue field
`k(𝔭)` is separable over `k`, `A_𝔭` is formally smooth over `k` for the `𝔭`-preadic topology `(0_IV, 19.6.4)`. It
therefore results from `(22.6.2, (ii))` that condition a) amounts to the fact that the homomorphism of `L`-vector spaces

```text
  (22.7.2.1)   j_0 : (𝔮/𝔮²) ⊗_A L → Ω^1_{A_𝔭} ⊗_{A_𝔭} L = Ω̂^1_{A/k} ⊗_A L
```

is injective.

Consider on the other hand the composite homomorphism

```text
  (22.7.2.2)   j : (𝔮/𝔮²) ⊗_A L ─j_∗→ Ω^1_{A/k} ⊗_A L → Ω̂^1_{A/k} ⊗_A L
```

and let us show that condition b) is equivalent to saying that `j` is injective. Note indeed that
`(𝔮/𝔮²) ⊗_A L = (𝔮 A_𝔭/𝔮² A_𝔭) ⊗_{A_𝔭} L`; condition b) signifies that if `F_i = j(f′_i ⊗ 1)`, where `f′_i` is the image
of `f_i` in `𝔮 A_𝔭/𝔮² A_𝔭`, the matrix `(⟨F_i, D_j ⊗ 1⟩)` is invertible; hence this entails that the `F_i` are linearly
independent, and *a fortiori* the same holds of the `f′_i ⊗ 1`; but since these last generate
`(𝔮 A_𝔭/𝔮² A_𝔭) ⊗_{A_𝔭} L`, one concludes that `j` is injective. Conversely, suppose `j` injective, and take the `f_i`
such that the `f′_i ⊗ 1` form

<!-- original page 210 -->

a basis of `(𝔮 A_𝔭/𝔮² A_𝔭) ⊗_{A_𝔭} L`; then the `F_i` form a basis of the image of `j`; but one knows `(0_IV, 21.9.3)`
that `Ω̂^1_{A/k}` is a free `A`-module of rank `r` and the `k`-derivations of `A` into itself generate its dual; the
fact that the `F_i` are linearly independent therefore entails the existence of `k`-derivations `D_j` of `A` into itself
such that the matrix `(⟨F_i, D_j ⊗ 1⟩)` be invertible, in other words condition b).

These remarks already show that b) entails a). To prove conversely that condition a) entails that `j` is injective,
consider the commutative diagram

```text
                              j
  (22.7.2.3)   (𝔮/𝔮²) ⊗_A L ─────▸ Ω̂^1_{A/k} ⊗_A L
                       │                  ║
                       α                  ║
                       ▼                  ║
              (𝔭/𝔭²) ⊗_A L ─────▸ Ω̂^1_{A/k} ⊗_A L
                              i
```

and note the following lemma:

**Lemma (22.7.2.4).**

<!-- label: 0_IV.22.7.2.4 -->

*Let `R` be a regular local ring, `𝔪` its maximal ideal, `K = R/𝔪` its residue field. If `𝔫` is an ideal of `R` such
that `R/𝔫` is regular, then the canonical homomorphism*

```text
  (22.7.2.5)   α : (𝔫/𝔫²) ⊗_R K → (𝔪/𝔪²) ⊗_R K
```

*is injective.*

Indeed, one knows `(0_IV, 17.1.6)` that `𝔫` is generated by a sequence `(x_i)_{1 ≤ i ≤ t}` forming part of a regular
system of parameters `(x_i)_{1 ≤ i ≤ n}` of `R`; the images of the `x_i` (`1 ≤ i ≤ t`) form a basis of `(𝔫/𝔫²) ⊗_R K`,
and their images by `α` form part of the basis of `(𝔪/𝔪²) ⊗_R K` formed of the images of the `x_i` for `1 ≤ i ≤ n`,
whence the lemma.

This lemma and the diagram `(22.7.2.3)` therefore reduce (by virtue of hypothesis a)) to proving that `i` is injective.
Now, in the sequence

```text
  (22.7.2.6)   𝔭/𝔭² ─h→ Ω̂^1_{A/k} ⊗̂_A (A/𝔭) ─g→ Ω̂^1_{(A/𝔭)/k} → 0
```

one knows `(0_IV, 20.7.20)` that `g` is surjective and that the image of `h` is *dense* in the kernel of `g` for the
`𝔪`-adic topology (`𝔪` being the maximal ideal of `A`); since `Ω̂^1_{A/k}` is an `A`-module of finite type, all the
submodules of the `(A/𝔭)`-module `Ω̂^1_{A/k} ⊗_A (A/𝔭) = Ω̂^1_{A/k} ⊗̂_A (A/𝔭)` are closed for the `𝔪`-adic topology
`(0_I, 7.3.5)`, hence the sequence `(22.7.2.6)` is exact. Tensoring by `L`, there arises the exact sequence

```text
  (𝔭/𝔭²) ⊗_A L ─i→ Ω̂^1_{A/k} ⊗_A L → Ω̂^1_{(A/𝔭)/k} ⊗_A L → 0.
```

Now, the hypothesis of separability made on `L` entails, by virtue of `(0_IV, 21.9.5)`, that `Ω̂^1_{(A/𝔭)/k} ⊗_{A/𝔭} L`
is of rank `s` over `L`; since `Ω̂^1_{A/k} ⊗_A L` is of rank `r` over `L` `(0_IV, 21.9.3)`, one has
`rg_L(Im(i)) = r − s`. But since `A/𝔭` is finite over a subalgebra isomorphic to `k[[T_1, …, T_s]]`, one has
`dim(A/𝔭) = s` (`(0_IV, 17.1.4)` and `(0_IV, 16.1.5)`); hence

```text
  r − s = dim(A) − dim(A/𝔭) = dim(A_𝔭)
```

<!-- original page 211 -->

by `(0_IV, 16.5.11)`. Now, since `A_𝔭` is regular `(0_IV, 17.3.2)`, `dim(A_𝔭)` is equal to the rank over `L` of
`𝔭 A_𝔭/𝔭² A_𝔭` `(0_IV, 17.1.1)`, hence to the rank over `L` of `(𝔭/𝔭²) ⊗_A L`, which completes proving that `i` is
injective.

**Theorem (22.7.3).**

<!-- label: 0_IV.22.7.3 -->

*Let `k` be a field, `A` a complete Noetherian local ring with residue field `K`. Suppose that:*

*1° `[k : k^p] < +∞` (where `p` is the characteristic exponent of `k`);*

*2° `K` is a finite extension of a separable extension `K_0` of `k`;*

*3° `A` is equipped with a structure of `K_0`-algebra formally smooth (for the preadic topology).*

*Let `𝔮` be an ideal of `A`, `B = A/𝔮`, `𝔭` a prime ideal of `A` containing `𝔮`. The following conditions are
equivalent:*

*a) `B_𝔭` is a `k`-algebra formally smooth (for the `𝔭`-preadic topology).*

*b) There exist `k`-derivations `D_i` of `A` into itself (`1 ≤ i ≤ m`) and elements `f_i` (`1 ≤ i ≤ m`) of `𝔮`, such
that the images of the `f_i` in `𝔮 A_𝔭` generate this ideal of `A_𝔭`, and that one has `det(D_i f_j) ∉ 𝔭`.*

*b′) There exists a subextension `k′` of `K_0`, containing `K_0^p`, such that `[K_0 : k′] < +∞`, `k′`-derivations `D_i`
of `A` into itself (`1 ≤ i ≤ m`) and elements `f_i` of `𝔮` (`1 ≤ i ≤ m`), such that the images of the `f_i` in `𝔮 A_𝔭`
generate this ideal of `A_𝔭` and that one has `det(D_i f_j) ∉ 𝔭`.*

Let us distinguish two cases, according as `p = 1` or `p > 1`.

A) `k` is of characteristic `0`. Since `K` is then a separable extension of `K_0`, it follows from `(0_IV, 19.6.4)` that
`A` is `K_0`-isomorphic to a ring of formal series `K[[T_1, …, T_r]]` equipped with its usual structure of `K`-algebra.
But then, taking account of `(0_IV, 19.8.8, (ii))` applied to `A/𝔭`, one sees that the general conditions of `(22.7.2)`
are satisfied by replacing therein `k` by `K`. Moreover, by virtue of `(0_IV, 19.6.4)`, it amounts to the same to say
that `B_𝔭` is a `k`-algebra formally smooth or a `K`-algebra formally smooth, the two conditions being equivalent to the
fact that `B_𝔭` is a regular ring. One may therefore apply the conclusions of `(22.7.2)`, and it is immediate that this
proves the equivalence of a), b) and b′) (with `k′ = K_0` in b′)).

B) `k` is of characteristic `p > 0`. Since `A` is a `K_0`-algebra formally smooth and `K_0` is separable over `k`, it
follows from `(0_IV, 19.3.5, (ii))` and `(0_IV, 19.6.1)` that `A` is a `k`-algebra formally smooth; by virtue of
`(22.5.9)`, `A_𝔭` is also a `k`-algebra formally smooth for the `𝔭`-preadic topology. It results then again from
`(22.6.2, (ii))` that condition a) amounts to the fact that the homomorphism `j_0` defined in `(22.7.2.1)` (where
`L = k(𝔭)`) is injective. Hence `(0_IV, 19.1.12, c))` already shows that b) implies a); since on the other hand b′)
trivially implies b), all reduces to showing that the hypothesis that `j_0` is injective entails b′).

Denote first by `k′` any subextension of `K_0` such that `[K_0 : k′] < +∞`. Note that `Ω̂^1_{A/k′}` is a free `A`-module
of finite type. By the reasoning of `(22.7.2)`, it suffices to show that (for a suitable choice of `k′`), the composite
homomorphism

```text
  (22.7.3.1)   j′ : (𝔮/𝔮²) ⊗_A L ─j_∗→ Ω^1_{A/k′} ⊗_A L → Ω̂^1_{A/k′} ⊗_A L
```

<!-- original page 212 -->

is injective. Consider once more the commutative diagram

```text
                                       i_∗
  (22.7.3.2)   (𝔮/𝔮²) ⊗_A L ─────▸ Ω̂^1_{A/k′} ⊗_A L ─────▸ Ω̂^1_{A/k} ⊗_A L
                       │                    ║                       ║
                       α                    ║                       ║
                       ▼                    ║                       ║
              (𝔭/𝔭²) ⊗_A L ─────▸ Ω̂^1_{A/k′} ⊗_A L ─────▸ Ω̂^1_{A/k} ⊗_A L
                                       i_∗
```

Since `j_0` is injective, one has `Ker(i_0 ∘ α) = 0`. But since `A_𝔭` is a regular ring and hypothesis a) implies that
`B_𝔭 = A_𝔭/𝔮 A_𝔭` is also a regular ring `(0_IV, 19.6.5)`, the lemma `(22.7.2.4)` shows that `α` is injective, whence
`α⁻¹(Ker(i_0)) = 0`. If `i′` is the composite of the homomorphisms of the second line of `(22.7.3.2)`, one has similarly
`Ker(j′) = α⁻¹(Ker(i′))`, and all reduces therefore to showing that, for a suitable choice of `k′`, one has

```text
  (22.7.3.3)   Ker(i′) = Ker(i).
```

But the same reasoning as in `(22.7.2)` shows that one has an exact sequence

```text
  (𝔭/𝔭²) ⊗_A L ─i′→ Ω̂^1_{A/k′} ⊗_A L → Ω̂^1_{(A/𝔭)/k′} ⊗_{A/𝔭} L → 0.
```

Now, the hypotheses made permit applying `(0_IV, 21.9.8)`, hence there exists a subextension `k′` of `K_0` containing
`K_0^p`, such that `[K_0 : k′] < +∞`, and for which one has

```text
  rg_L(Ω̂^1_{(A/𝔭)/k′} ⊗_{A/𝔭} L) = dim(A/𝔭) + rg_L Υ_{L/k} + rg_K Ω^1_{K_0/k′}.
```

But one has

```text
  dim(A/𝔭) = dim(A) − dim(A_𝔭)
```

by `(0_IV, 16.5.11)`,

```text
  dim(A_𝔭) = rg_L((𝔭/𝔭²) ⊗_A L)
```

since `A_𝔭` is regular `(0_IV, 17.1.1)`, and finally

```text
  dim(A) + rg_K Ω^1_{K_0/k′} = rg_L(Ω̂^1_{A/k′} ⊗_A L)
```

by virtue of `(0_IV, 21.9.2)`; one therefore obtains

```text
  (22.7.3.4)   rg_L(Ker(i′)) = rg_L Υ_{L/k}.
```

On the other hand, the residue field of `A_𝔭` being formally smooth over the prime field of `k`, one has an exact
sequence `(0_IV, 20.6.22.1)`

```text
  Υ_{L/k} ─χ_{A_𝔭/k}→ (𝔭 A_𝔭)/(𝔭 A_𝔭)² ─i→ Ω^1_{A_𝔭/k} ⊗_{A_𝔭} L
```

and since `A_𝔭` is a `k`-algebra formally smooth for the `𝔭`-preadic topology, it follows from `(22.2.2)` that
`χ_{A_𝔭/k}` is an injective homomorphism, hence `Ker(i)` is isomorphic to `Υ_{L/k}`, and taking account of `(22.7.3.4)`
and the fact that `Ker(i) ⊂ Ker(i′)`, this completes proving `(22.7.3.3)` and consequently the theorem.

<!-- original page 213 -->

**Remark (22.7.4).**

<!-- label: 0_IV.22.7.4 -->

*One has in fact shown (using `(0_IV, 21.9.6)`) that condition b′) is still equivalent to the other conditions of
`(22.7.3)` when one subjects `k′` to being one of the fields of a decreasing filtered family `(k_α)` of subfields of
`K_0` containing `K_0^p`, such that `[K_0 : k_α] < +∞` for every `α` and `⋂_α k_α = K_0^p`.*

**Corollary (22.7.5).**

<!-- label: 0_IV.22.7.5 -->

*Under the general hypotheses of `(22.7.3)`, the set of prime ideals `𝔫 ∈ Spec(B)` such that `B_𝔫` is a `k`-algebra
formally smooth (for the `𝔫`-preadic topology) is open in `Spec(B)`.*

With the notations of `(22.7.3)`, it suffices to see that if `B_𝔭` is formally smooth over `k`, the same holds for
`B_{𝔭′}` for every `𝔭′ ∈ V(𝔮)` sufficiently close to `𝔭` in `Spec(A)`. Now, if the `k`-derivations `D_i` and the
elements `f_i` of `𝔮` verify the criterion b) of `(22.7.3)`, one has also `f = det(D_i f_j) ∉ 𝔭′` for `𝔭′ ∈ D(f)`; on
the other hand, there exists a `g ∉ 𝔭` such that the images of the `f_i` in `𝔮 A_{𝔭′}` generate `𝔮 A_{𝔭′}` for
`𝔭′ ∈ D(g)` (Bourbaki, *Alg. comm.*, chap. II, §5, n° 1, prop. 2), which completes proving the corollary.

**Corollary (22.7.6)** (Nagata).

<!-- label: 0_IV.22.7.6 -->

*Let `B` be a complete Noetherian local ring containing a field. Then the set of `𝔫 ∈ Spec(B)` such that `B_𝔫` is
regular is open in `Spec(B)`.*

Indeed, `B` is an algebra over a prime field `k`, hence `(0_IV, 19.8.8, (i))` of the form `A/𝔮`, where
`A = K_0[[T_1, …, T_r]]` is a ring of formal series and `K_0` an extension of `k`; on the other hand, to say that `B_𝔫`
is regular amounts to saying that it is a `k`-algebra formally smooth for the `𝔫`-preadic topology `(0_IV, 19.6.4)`. All
the conditions of application of `(22.7.5)` are therefore fulfilled.

**Remarks (22.7.7).**

<!-- label: 0_IV.22.7.7 -->

*(i) We shall later see, with Nagata, using `(22.7.6)`, that one can extend the conclusion of `(22.7.6)` to the case of
an arbitrary complete Noetherian local ring `(IV, 6.12.7)`.*

*(ii) The conclusion of theorem `(22.7.3)` is not necessarily exact when one no longer supposes that `[k : k^p]` be
finite. Take for example `k = 𝔽_p(X_n)_{n ≥ 0}`, `A = k[[T, U]]`, `𝔮` equal to the principal ideal `A f`, where
`f = U^p − ∑_{n=0}^∞ X_n T^{np}`; `A` is a factorial ring in which `f` is an extremal element, for it is extremal in the
polynomial ring `k((T))[U]`, hence also in the ring of formal series `k((T))[[U]]` (Bourbaki, *Alg. comm.*, chap. VII,
§3), and *a fortiori* in `A`. Take `𝔭 = 𝔮`, so that `B_𝔭` is the field denoted `E` in `(0_IV, 21.9.7)`, which is
separable over `k` (*loc. cit.*), hence a `k`-algebra formally smooth. But one has here, with the notations of
`(22.7.3)`, `k = K_0 = K`, and the `k`-derivations of `A` into itself are the linear combinations of `∂/∂T` and `∂/∂U`;
since one has `∂f/∂T = ∂f/∂U = 0`, the criteria b) and b′) of `(22.7.3)` are not satisfied.*
