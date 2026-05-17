# Chapter 0 — Preliminaries

## §7. Adic Rings

<!-- label: 0.7 -->

### 7.1. Admissible rings

<!-- label: 0.7.1 -->

**(7.1.1)** Recall that in a topological ring `A` (not necessarily separated), an element `x` is _topologically
nilpotent_ if `0` is a limit of the sequence `(xⁿ)_{n ≥ 0}`. A topological ring `A` is _linearly topologized_ if there
is a fundamental system of neighborhoods of `0` in `A` consisting of (necessarily _open_) _ideals_.

**Definition (7.1.2).** In a linearly topologized ring `A`, an _ideal of definition_ is an open ideal `𝔍` such that for
every neighborhood `V` of `0` there is `n > 0` with `𝔍ⁿ ⊂ V` (by abuse of language: _the sequence `(𝔍ⁿ)` tends to_ `0`).
`A` is _preadmissible_ if there is an ideal of definition in `A`; it is _admissible_ if it is preadmissible, separated,
and complete.

Plainly, if `𝔍` is an ideal of definition and `𝔏` an open ideal, then `𝔍 ∩ 𝔏` is also an ideal of definition; so the
ideals of definition of a preadmissible ring form a _fundamental system of neighborhoods of_ `0`.

**Lemma (7.1.3).** Let `A` be a linearly topologized ring.

> (i) For `x ∈ A` to be topologically nilpotent, it is necessary and sufficient that for every open ideal `𝔍 ⊂ A`, the
> canonical image of `x` in `A/𝔍` be nilpotent. The set `𝔗` of topologically nilpotent elements of `A` is an ideal. (ii)
> Suppose `A` is preadmissible and `𝔍` is an ideal of definition. Then `x` is topologically nilpotent iff its image in
> `A/𝔍` is nilpotent; `𝔗` is the inverse image of the nilradical of `A/𝔍`, and is therefore open.

**Proof.** (i) follows from the definitions. For (ii): for every neighborhood `V` of `0`, some `𝔍ⁿ ⊂ V`; if `xᵐ ∈ 𝔍`,
then `x^{mq} ∈ V` for `q ≥ n`, so `x` is topologically nilpotent.

**Proposition (7.1.4).** Let `A` be a preadmissible ring with ideal of definition `𝔍`.

> (i) For `𝔍′ ⊂ A` to be contained in an ideal of definition, it is necessary and sufficient that `𝔍′ⁿ ⊂ 𝔍` for some
> `n > 0`. (ii) For `x ∈ A` to be contained in an ideal of definition, it is necessary and sufficient that `x` be
> topologically nilpotent.

**Corollary (7.1.5).** In a preadmissible ring `A`, every open prime ideal contains every ideal of definition.

**Corollary (7.1.6).** Under the hypotheses of (7.1.4), the following are equivalent for an ideal `𝔍_0`:

> (a) `𝔍_0` is the largest ideal of definition; (b) `𝔍_0` is a maximal ideal of definition; (c) `𝔍_0` is an ideal of
> definition such that `A/𝔍_0` is reduced.

Such `𝔍_0` exists if and only if the nilradical of `A/𝔍` is nilpotent; `𝔍_0` is then the ideal `𝔗` of topologically
nilpotent elements.

When the nilradical of `A/𝔍` is nilpotent, we write `A_red` for the reduced quotient `A/𝔗`.

**Corollary (7.1.7).** A preadmissible Noetherian ring has a largest ideal of definition.

**Corollary (7.1.8).** If `A` is preadmissible and the powers `𝔍ⁿ` (`n > 0`) of some ideal of definition `𝔍` form a
fundamental system of neighborhoods of `0`, the same holds for `𝔍′ⁿ` for every ideal of definition `𝔍′`.

**Definition (7.1.9).** A preadmissible ring `A` is _preadic_ if there is an ideal of definition `𝔍` whose powers `𝔍ⁿ`
form a fundamental system of neighborhoods of `0` (equivalently, the `𝔍ⁿ` are open). An _adic_ ring is a separated and
complete preadic ring.

If `𝔍` is an ideal of definition of a preadic (resp. adic) ring `A`, we also say `A` is _𝔍-preadic_ (resp. _𝔍-adic_),
and its topology is the _𝔍-preadic_ (resp. _𝔍-adic_) topology. For an `A`-module `M`, the topology with fundamental
system of neighborhoods the submodules `𝔍ⁿM` is called the _𝔍-preadic_ (resp. _𝔍-adic_) topology. By (7.1.8), these
topologies are independent of the choice of ideal of definition `𝔍`.

**Proposition (7.1.10).** Let `A` be an admissible ring and `𝔍` an ideal of definition. Then `𝔍` is contained in the
radical of `A`.

This is equivalent to any of the following:

**Corollary (7.1.11).** For every `x ∈ 𝔍`, `1 + x` is invertible in `A`.

**Corollary (7.1.12).** For `f ∈ A` to be invertible, it is necessary and sufficient that its image in `A/𝔍` be
invertible.

**Corollary (7.1.13).** For every `A`-module `M` of finite type, `M = 𝔍M` (equivalent to `M ⊗_A (A/𝔍) = 0`) implies
`M = 0`.

**Corollary (7.1.14).** Let `u : M → N` be an `A`-module homomorphism with `N` of finite type. For `u` to be surjective,
it is necessary and sufficient that `u ⊗ 1 : M ⊗_A (A/𝔍) → N ⊗_A (A/𝔍)` be.

**Proof of (7.1.10).** The equivalences with (7.1.11), (7.1.13), and (7.1.12) follow from standard results of Bourbaki
(_Alg._, Chap. VIII). To prove (7.1.11): since `A` is separated and complete and `(𝔍ⁿ)` tends to `0`, the series
`∑_{n=0}^∞ (−1)ⁿ xⁿ` converges in `A`; its sum `y` satisfies `y(1 + x) = 1`.

### 7.2. Adic rings and projective limits

<!-- label: 0.7.2 -->

**(7.2.1)** Every projective limit of _discrete_ rings is plainly a linearly topologized, separated, and complete ring.
Conversely, let `A` be linearly topologized with `(𝔍_λ)` a fundamental system of open neighborhoods of `0` consisting of
ideals. The canonical maps `φ_λ : A → A/𝔍_λ` form a projective system, defining a continuous map `φ : A → lim⃖ A/𝔍_λ`;
if `A` is _separated_, `φ` is a topological isomorphism onto a dense subring; if also _complete_, `φ` is a topological
isomorphism onto `lim⃖ A/𝔍_λ`.

**Lemma (7.2.2).** A linearly topologized ring is admissible if and only if it is isomorphic to a projective limit
`A = lim⃖ A_λ` of discrete rings indexed by a filtered ordered set `L` with smallest element `0`, such that:

> 1. each `u_λ : A → A_λ` is surjective;
> 1. the kernel `𝔍_λ` of `u_{0λ} : A_λ → A_0` is nilpotent.

When this holds, the kernel `𝔍` of `u_0 : A → A_0` equals `lim⃖ 𝔍_λ`.

**(7.2.3)** Let `A` be admissible and `𝔍 ⊂ A` an ideal contained in an ideal of definition (equivalently, `(𝔍ⁿ)` tends
to `0`). The ring topology on `A` having the `𝔍ⁿ` (`n > 0`) as fundamental system of neighborhoods of `0` — also called
the _𝔍-preadic_ topology — is separated, since `⋂_n 𝔍ⁿ = 0`. Let `Â = lim⃖ A/𝔍ⁿ` (the `A/𝔍ⁿ` discrete) be the completion
for this topology, and let `u : A → Â` be the (possibly discontinuous) projective limit of `u_n : A → A/𝔍ⁿ`. The
`𝔍`-preadic topology is finer than the given topology `𝒯`; extending the identity of `A` (with `𝔍`-preadic topology) by
continuity to `𝒯` gives a continuous map `v : Â → A`.

**Proposition (7.2.4).** If `A` is admissible and `𝔍` is contained in an ideal of definition, then `A` is separated and
complete for the `𝔍`-preadic topology.

**Proof.** With the notation of (7.2.3), `v ∘ u = id_A` directly, and `u_n ∘ v` is the canonical `Â → A/𝔍ⁿ`, so
`u ∘ v = id_Â`.

**Corollary (7.2.5).** Under the hypotheses of (7.2.3), the following are equivalent:

> (a) `u` is continuous; (b) `v` is bicontinuous; (c) `A` is `𝔍`-adic.

**Corollary (7.2.6).** Let `A` be an admissible ring and `𝔍` an ideal of definition. `A` is Noetherian if and only if
`A/𝔍` is Noetherian and `𝔍/𝔍²` is an `A/𝔍`-module of finite type.

The conditions are clearly necessary. Conversely, by (7.2.4) `A` is complete for the `𝔍`-preadic topology, so it is
Noetherian if and only if the associated graded ring `grad(A)` (for the filtration `(𝔍ⁿ)`) is. Choosing
`a_1, …, a_n ∈ 𝔍` with classes mod `𝔍²` generating `𝔍/𝔍²`, induction shows their degree-`m` monomials generate
`𝔍ᵐ/𝔍^{m+1}` as `A/𝔍`-module. Hence `grad(A)` is a quotient of `(A/𝔍)[T_1, …, T_n]`.

**Proposition (7.2.7).** Let `(A_i, u_{ij})` (`i ∈ ℕ`) be a projective system of discrete rings, and let `𝔍_i ⊂ A_i` be
the kernel of `u_{0i} : A_i → A_0`. Suppose:

> (a) For `i ≤ j`, `u_{ij}` is surjective with kernel `𝔍_j^{i+1}` (so `A_i ≅ A_j / 𝔍_j^{i+1}`). (b) `𝔍_1 / 𝔍_1²`
> (`= 𝔍_1`) is finite-type over `A_0 = A_1 / 𝔍_1`.

Let `A = lim⃖_i A_i`, `u_n : A → A_n` the canonical map, and `𝔍^{(n+1)} ⊂ A` its kernel. Then:

> (i) `A` is adic, with `𝔍 = 𝔍^{(1)}` an ideal of definition. (ii) `𝔍^{(n)} = 𝔍ⁿ` for every `n ≥ 1`. (iii) `𝔍 / 𝔍²` is
> isomorphic to `𝔍_1`, hence finite-type over `A_0 = A / 𝔍`.

**Proof.** The surjectivity of the `u_{ij}` makes each `u_n` surjective; (a) gives `𝔍_j^{j+1} = 0`, so `A` is admissible
by (7.2.2). The `𝔍^{(n)}` form a fundamental system of neighborhoods of `0`, so (ii) ⟹ (i). Since `𝔍 = lim⃖_i 𝔍_i` with
surjective maps to `𝔍_i`, (ii) ⟹ (iii). For (ii): `𝔍^{(n)}` consists of `(x_k)` with `x_k = 0` for `k < n`, so
`𝔍^{(n)} · 𝔍^{(m)} ⊂ 𝔍^{(n+m)}` — a filtration. Also `𝔍^{(n)} / 𝔍^{(n+1)}` projects to `𝔍_n^n` (an `A_0`-module). Choose
`r` elements `a_j = (a_{jk})` of `𝔍` whose `a_{j1}` generate `𝔍_1` over `A_0`. We show by induction that monomials of
degree `n` in the `a_j` generate `𝔍^{(n)}`; the same argument (passage to graded modules) closes the induction.

**Corollary (7.2.8).** Under the hypotheses of (7.2.7), `A` is Noetherian if and only if `A_0` is.

**Proof.** By (7.2.6).

**Proposition (7.2.9).** Under the hypotheses of (7.2.7), for each `i` let `M_i` be an `A_i`-module, and for `i ≤ j` let
`v_{ij} : M_j → M_i` be a `u_{ij}`-homomorphism with `(M_i, v_{ij})` a projective system. Suppose `M_0` is
`A_0`-finite-type and each `v_{ij}` is surjective with kernel `𝔍_j^{i+1} M_j`. Then `M = lim⃖ M_i` is an `A`-module of
finite type, and the kernel of the surjective `v_n : M → M_n` is `𝔍^{n+1} M` (so
`M_n ≅ M / 𝔍^{n+1} M = M ⊗_A (A / 𝔍^{n+1})`).

**Proof.** Choose `s` elements `z_h = (z_{hk}) ∈ M` such that the `z_{h0}` generate `M_0`. Reducing to showing the
`z_{hn}` generate `M_n` over `A_n`, induction on `n` using `M_{n-1} = M_n / 𝔍_n^n M_n` plus Nakayama closes the
argument. Passage to graded modules then gives `𝔍^{(n)} M = 𝔍ⁿ M`, the kernel of `M → M_{n-1}`.

**Corollary (7.2.10).** Let `(N_i, w_{ij})` be a second such projective system, `N = lim⃖ N_i`. There is a bijective
correspondence between projective systems `(h_i)` of `A_i`-homomorphisms `M_i → N_i` and `A`-homomorphisms `M → N`
(necessarily continuous for the `𝔍`-adic topologies).

**Remark (7.2.11).** Let `A` be adic with ideal of definition `𝔍` such that `𝔍/𝔍²` is `A/𝔍`-finite-type. The
`A_i = A / 𝔍^{i+1}` satisfy (7.2.7), and `A = lim⃖ A_i`. Thus (7.2.7) describes _all_ adic rings of this type — in
particular all _adic Noetherian_ rings.

**Example (7.2.12).** Let `B` be a ring, `𝔍 ⊂ B` an ideal with `𝔍/𝔍²` finite-type over `B/𝔍`; set
`A = lim⃖_n B / 𝔍^{n+1}`. Then `A` is the separated `𝔍`-preadic completion of `B`. The `A_n = B / 𝔍^{n+1}` satisfy
(7.2.7); so `A` is adic, the closure `𝔍̄` in `A` of the image of `𝔍` is an ideal of definition, `𝔍̄ⁿ` is the closure of
the image of `𝔍ⁿ`, `A / 𝔍̄ⁿ ≅ B / 𝔍ⁿ`, and `𝔍̄ / 𝔍̄²` is isomorphic to `𝔍 / 𝔍²` as `A/𝔍̄`-module. Likewise, if `N` is a
`B`-module with `N/𝔍N` finite-type, then `M = lim⃖_i N/𝔍^{i+1} N` is `A`-finite-type, isomorphic to the separated
`𝔍`-preadic completion of `N`.

### 7.3. Preadic Noetherian rings

<!-- label: 0.7.3 -->

**(7.3.1)** Let `A` be a ring, `𝔍 ⊂ A` an ideal, `M` an `A`-module. Write `Â = lim⃖_n A/𝔍ⁿ` (resp. `M̂ = lim⃖_n M/𝔍ⁿ M`)
for the separated `𝔍`-preadic completion of `A` (resp. `M`). For an exact sequence `M′ ──u──→ M ──v──→ M″ → 0`, the
sequence `M′/𝔍ⁿ M′ → M/𝔍ⁿ M → M″/𝔍ⁿ M″ → 0` is exact for each `n`. Since `v(𝔍ⁿ M) = 𝔍ⁿ M″`, the limit `v̂ = lim⃖ v_n` is
surjective. For `z = (z_k) ∈ Ker v̂`, lift each `z_k` to `z_k′ ∈ M′/𝔍ᵏ M′`; we find `z′ = (z_n′) ∈ M̂′` whose first `k`
components under `û` match `z`. So `Im(û)` is _dense_ in `Ker v̂`.

If `A` is _Noetherian_, so is `Â` by (7.2.12), and `𝔍/𝔍²` is `A`-finite-type. We also have:

**Theorem (7.3.2) (Krull).** Let `A` be a Noetherian ring, `𝔍 ⊂ A` an ideal, `M` an `A`-module of finite type, and
`M′ ⊂ M` a submodule. Then the topology on `M′` induced from the `𝔍`-preadic topology of `M` agrees with the `𝔍`-preadic
topology of `M′`.

This follows from:

**Lemma (7.3.2.1) (Artin–Rees).** Under the hypotheses of (7.3.2), there is `p ≥ 0` with
`M′ ∩ 𝔍ⁿ M = 𝔍^{n-p}(M′ ∩ 𝔍^p M)` for `n ≥ p`. (Bourbaki, _Alg. comm._)

**Corollary (7.3.3).** Under the hypotheses of (7.3.2), the canonical map `M ⊗_A Â → M̂` is bijective, and `M ⊗_A Â` is
exact in `M` on `A`-modules of finite type; consequently `Â` is a flat `A`-module (6.1.1).

**Proof.** First, `M̂` is exact on `A`-modules of finite type: for `0 → M′ → M → M″ → 0` exact, Krull (7.3.2) shows the
closure of the image of `M′` in `M̂` is the completion of `M′`, so `û` is injective. The canonical `M ⊗_A Â → M̂` is
bijective when `M = Aᵖ`; for general `M` of finite type, take a presentation `A^p → A^q → M → 0` and apply right
exactness of both functors.

**Corollary (7.3.4).** For `A` Noetherian, `𝔍 ⊂ A` an ideal, and `M, N` of finite type, there are canonical functorial
isomorphisms

```
(M ⊗_A N)^∧ ≅ M̂ ⊗_Â N̂,    (Hom_A(M, N))^∧ ≅ Hom_Â(M̂, N̂).
```

This follows from (7.3.3), (6.2.1), and (6.2.2).

**Corollary (7.3.5).** Let `A` be Noetherian and `𝔍 ⊂ A` an ideal. The following are equivalent:

> (a) `𝔍` is contained in the radical of `A`; (b) `Â` is a faithfully flat `A`-module (6.4.1); (c) Every `A`-module of
> finite type is separated for the `𝔍`-preadic topology; (d) Every submodule of an `A`-module of finite type is closed
> for the `𝔍`-preadic topology.

**Proof.** (b) ⟺ (c) by flatness of `Â` and (6.6.1). (c) ⟹ (d): if `N ⊂ M` with `M` of finite type, `M/N` is separated.
(d) ⟹ (a): for `𝔪 ⊂ A` maximal, `𝔪 = ⋂_p (𝔪 + 𝔍^p)`; for large `p`, `𝔪 + 𝔍^p = 𝔪`, so `𝔍^p ⊂ 𝔪`, hence `𝔍 ⊂ 𝔪`. (a) ⟹
(b): let `P` be the closure of `{0}` in an `M` of finite type for the `𝔍`-preadic topology; by Krull, the induced
topology on `P` is the `𝔍`-preadic, so `𝔍 P = P`; Nakayama gives `P = 0`.

The conditions hold when `A` is local Noetherian and `𝔍 ≠ A`.

**Corollary (7.3.6).** If `A` is `𝔍`-preadic Noetherian, every `A`-module of finite type is separated and complete for
the `𝔍`-preadic topology.

**Proof.** `Â = A`, so this follows from (7.3.3).

So (7.2.9) describes _all_ finite-type modules over an adic Noetherian ring.

**Corollary (7.3.7).** Under the hypotheses of (7.3.2), the kernel of `M → M̂ = M ⊗_A Â` is the set of `x ∈ M` killed by
an element of `1 + 𝔍`.

### 7.4. Quasi-finite modules over local rings

<!-- label: 0.7.4 -->

**Definition (7.4.1).** Let `A` be a local ring with maximal ideal `𝔪`. An `A`-module `M` is _quasi-finite_ (over `A`)
if `M/𝔪M` is of finite rank over the residue field `k = A/𝔪`.

When `A` is Noetherian, the `𝔪`-preadic completion `M̂` is then an `Â`-module of finite type; this follows from (7.2.12)
and the hypothesis on `M/𝔪M`.

In particular, if `A` is also complete and `M` is separated for the `𝔪`-preadic topology (i.e. `⋂_n 𝔪ⁿ M = 0`), then `M`
is `A`-finite-type: `M̂` is `A`-finite-type, `M ↪ M̂`, and so `M` is also finite-type (and equal to its completion, by
(7.3.6)).

**Proposition (7.4.2).** Let `A`, `B` be local rings with maximal ideals `𝔪`, `𝔫`, and suppose `B` is Noetherian. Let
`φ : A → B` be a local homomorphism, `M` a `B`-module of finite type. If `M` is `A`-quasi-finite, then the `𝔪`-preadic
and `𝔫`-preadic topologies on `M` agree (so both are separated).

**Proof.** `M/𝔪M` has finite length as `A`-module, hence as `B`-module. Therefore `𝔫` is the unique prime ideal of `B`
containing `Ann(M/𝔪M)`: reducing to `M/𝔪M` simple, we have `M/𝔪M ≅ B/𝔫`. By (0.1.7.5), the primes containing `Ann(M/𝔪M)`
are those containing `𝔪B + 𝔟`, where `𝔟 = Ann_B M`. Since `B` is Noetherian, `𝔪B + 𝔟` is an ideal of definition for `B`;
so for some `k > 0`, `𝔫^k ⊂ 𝔪B + 𝔟 ⊂ 𝔫`, giving for every `h > 0`

```
𝔫^{hk} ⊂ (𝔪B + 𝔟)^h M = 𝔪^h M ⊂ 𝔫^h M.
```

Hence the two topologies agree; separation follows from (7.3.5).

**Corollary (7.4.3).** Under the hypotheses of (7.4.2), if `A` is also Noetherian and complete for the `𝔪`-preadic
topology, then `M` is `A`-finite-type.

**(7.4.4)** The most important case of (7.4.2) is when `B` is `A`-quasi-finite — i.e., `B/𝔪B` is a finite-rank
`k = A/𝔪`-algebra. This breaks into:

> (i) `𝔪B` is an ideal of definition for `B`; (ii) `B/𝔫` is a finite-rank extension of `A/𝔪`.

Then every `B`-module of finite type is `A`-quasi-finite.

**Corollary (7.4.5).** Under the hypotheses of (7.4.2), if `𝔟 = Ann_B(M)`, then `B/𝔟` is `A`-quasi-finite.

### 7.5. Rings of restricted formal series

<!-- label: 0.7.5 -->

**(7.5.1)** Let `A` be a linearly topologized ring, separated and complete; let `(𝔍_λ)` be a fundamental system of open
ideals with `A ≅ lim⃖ A/𝔍_λ` (7.2.1). For each `λ`, set `B_λ = (A/𝔍_λ)[T_1, …, T_r]`; the `B_λ` form a projective system
of discrete rings. Set

```
A{T_1, …, T_r} = lim⃖ B_λ.
```

This ring is independent of `(𝔍_λ)`. Concretely, let `A′` be the subring of `A[[T_1, …, T_r]]` consisting of formal
series `∑_α c_α T^α` (`α = (α_1, …, α_r) ∈ ℕᵣ`) with `lim c_α = 0` (along the filter of cofinite subsets of `ℕᵣ`); call
these _restricted formal series_ in the `T_i` with coefficients in `A`. With the topology whose fundamental system of
neighborhoods of `0` consists of `{∑ c_α T^α : c_α ∈ V}` for `V` a neighborhood of `0` in `A`, `A′` is a separated
topological ring. There is a canonical topological isomorphism `A{T_1, …, T_r} ⥲ A′`, given by sending
`y ∈ A{T_1, …, T_r}` to `∑_α φ_α(y) T^α`, where `φ_α` extracts the coefficient of `T^α` (the result is restricted
because almost all components vanish in each `A/𝔍_λ`).

**(7.5.2)** Identify `A{T_1, …, T_r}` with the ring of restricted formal series via (7.5.1). The canonical isomorphisms
`(A/𝔍_λ)[T_1, …, T_r][T_{r+1}, …, T_s] ≅ (A/𝔍_λ)[T_1, …, T_s]` give a canonical isomorphism

```
(A{T_1, …, T_r}){T_{r+1}, …, T_s} ≅ A{T_1, …, T_s}.
```

**(7.5.3) Universal property.** For every continuous homomorphism `u : A → B` to a linearly topologized, separated,
complete ring `B`, and every system `(b_1, …, b_r)` in `B`, there is a _unique_ continuous homomorphism
`ū : A{T_1, …, T_r} → B` with `ū|A = u` and `ū(T_j) = b_j`, namely

```
ū(∑_α c_α T^α) = ∑_α u(c_α) b_1^{α_1} ⋯ b_r^{α_r}.
```

This characterizes `A{T_1, …, T_r}` up to unique isomorphism.

**Proposition (7.5.4).**

> (i) If `A` is admissible, so is `A′ = A{T_1, …, T_r}`. (ii) If `A` is `𝔍`-adic with `𝔍/𝔍²` finite-type over `A/𝔍`,
> then setting `𝔍′ = 𝔍 A′`, `A′` is `𝔍′`-adic with `𝔍′/𝔍′²` finite-type over `A′/𝔍′`. If `A` is Noetherian, so is `A′`.

**Proof.** (i) For an ideal of definition `𝔍 ⊂ A`, let `𝔍′ ⊂ A′` consist of `∑ c_α T^α` with all `c_α ∈ 𝔍`. Then
`𝔍′ⁿ ⊂ (𝔍ⁿ)′`, so `𝔍′` is an ideal of definition. (ii) Apply (7.2.7) to the projective system `A_i′ = A_i[T_1, …, T_r]`
with `A_i = A/𝔍^{i+1}`. (One checks the kernels match `𝔍_j′^{i+1}` using induction; details omitted.) Noetherianness
follows from (7.2.8).

**Proposition (7.5.5).** Let `A` be a Noetherian `𝔍`-adic ring and `B` an admissible topological ring; let `φ : A → B`
be a continuous homomorphism making `B` an `A`-algebra. The following are equivalent:

> (a) `B` is Noetherian and `𝔍B`-adic, and `B/𝔍B` is a finite-type algebra over `A/𝔍`. (b) `B` is topologically
> `A`-isomorphic to `lim⃖ B_n`, where `B_n = B_m / 𝔍^{n+1} B_m` for `m ≥ n`, and `B_1` is a finite-type
> `A_1 = A/𝔍²`-algebra. (c) `B` is topologically `A`-isomorphic to a quotient of some `A{T_1, …, T_r}` by a (necessarily
> closed) ideal.

**Proof sketch.** (c) ⟹ (a): `A′ = A{T_1, …, T_r}` is Noetherian (7.5.4); `𝔍 A′` is an ideal of definition of `A′`, and
`B/𝔍B` is a quotient of `(A/𝔍)[T_1, …, T_r]`. (a) ⟹ (b): by (7.2.11), `B ≅ lim⃖ B/𝔍^{n+1} B`. (b) ⟹ (c): choose
generators `(c_i)` of the `A/𝔍`-algebra `B/𝔍B` and apply (7.5.3) to get a continuous `A`-homomorphism `u : A′ → B`;
surjectivity is checked passing to associated graded modules.

### 7.6. Completed rings of fractions

<!-- label: 0.7.6 -->

**(7.6.1)** Let `A` be linearly topologized, `(𝔍_λ)` a fundamental system of open neighborhoods of `0` consisting of
ideals, and `S ⊂ A` a multiplicative subset. With `A_λ = A/𝔍_λ`, set `S_λ = u_λ(S)`; the `u_{λμ}` give surjective
`S_μ⁻¹ A_μ → S_λ⁻¹ A_λ`, a projective system. Write

```
A{S⁻¹} = lim⃖ S_λ⁻¹ A_λ.
```

This is independent of `(𝔍_λ)`:

**Proposition (7.6.2).** `A{S⁻¹}` is topologically isomorphic to the separated completion of `S⁻¹A` for the topology
with fundamental system of neighborhoods of `0` the `S⁻¹ 𝔍_λ`.

**Corollary (7.6.3).** If `S′` is the canonical image of `S` in `Â`, then `A{S⁻¹} ≅ Â{S′⁻¹}`.

If `A` is separated and complete, `S⁻¹A` need not be: take `S = {fⁿ}` with `f` topologically nilpotent but not
nilpotent; then `S⁻¹A ≠ 0` but `S⁻¹ 𝔍_λ = S⁻¹A` for each `λ`.

**Corollary (7.6.4).** If `0 ∉ S` in `A`, then `A{S⁻¹} ≠ 0`.

**(7.6.5)** Call `A{S⁻¹}` the _completed ring of fractions_ of `A` with denominators in `S`. There is a canonical
continuous `A → A{S⁻¹}`.

**(7.6.6) Universal property.** For every continuous `u : A → B` to a separated, complete linearly topologized ring `B`
with `u(S)` consisting of invertible elements, `u` factors uniquely as `A → A{S⁻¹} ──u′──→ B` with `u′` continuous.

**(7.6.7) Functoriality.** For `φ : A → B` continuous with `φ(S) ⊂ T`, there is a unique continuous
`φ′ : A{S⁻¹} → B{T⁻¹}` extending `φ`. For `B = A`, `φ = id`, and `S ⊂ T`, this gives `ρ^{T,S} : A{S⁻¹} → A{T⁻¹}` with
`ρ^{U,S} = ρ^{U,T} ∘ ρ^{T,S}` for `S ⊂ T ⊂ U`.

**(7.6.8)** For multiplicative subsets `S_1, S_2 ⊂ A` with `S_2′` the image of `S_2` in `A{S_1⁻¹}`,

```
A{(S_1 S_2)⁻¹} ≅ A{S_1⁻¹}{S_2′⁻¹}.
```

**(7.6.9)** Let `𝔞 ⊂ A` be an _open_ ideal. Then `S⁻¹ 𝔞` is open in `S⁻¹A`; its separated completion
`𝔞{S⁻¹} = lim⃖ (S⁻¹ 𝔞 / S⁻¹ 𝔍_λ)` is an open ideal of `A{S⁻¹}`, and `A{S⁻¹} / 𝔞{S⁻¹} ≅ S⁻¹ A / S⁻¹ 𝔞 = S⁻¹ (A/𝔞)`.
Conversely, every open ideal of `A{S⁻¹}` is of the form `𝔞{S⁻¹}` for a unique open `𝔞 ⊃ 𝔍_λ ⊂ A`.

**Proposition (7.6.10).** The map `𝔭 ↦ 𝔭{S⁻¹}` is an increasing bijection between open prime ideals of `A` not meeting
`S` and open prime ideals of `A{S⁻¹}`; the residue field of `A{S⁻¹}/𝔭{S⁻¹}` is canonically the field of fractions of
`A/𝔭`.

**Proposition (7.6.11).**

> (i) If `A` is admissible, so is `A′ = A{S⁻¹}`, and `𝔍′ = 𝔍{S⁻¹}` is an ideal of definition for `A′` whenever `𝔍` is
> for `A`. (ii) If `A` is `𝔍`-adic with `𝔍/𝔍²` finite-type over `A/𝔍`, then `A′` is `𝔍′`-adic with `𝔍′/𝔍′²` finite-type
> over `A′/𝔍′`. If `A` is Noetherian, so is `A′`.

**Corollary (7.6.12).** Under (7.6.11)(ii), `(𝔍{S⁻¹})ⁿ = 𝔍ⁿ{S⁻¹}`.

**Proposition (7.6.13).** Let `A` be an adic Noetherian ring and `S ⊂ A` multiplicative. Then `A{S⁻¹}` is a flat
`A`-module.

**Proof.** `A{S⁻¹}` is the completion of the Noetherian `S⁻¹A` for its `S⁻¹𝔍`-preadic topology, hence flat over `S⁻¹A`
(7.3.3); transitivity (6.2.1) plus flatness of `S⁻¹A` over `A` (6.3.1) finishes the proof.

**Corollary (7.6.14).** Under (7.6.13), if `S′ ⊂ S`, then `A{S⁻¹}` is flat over `A{S′⁻¹}`.

**(7.6.15)** For `f ∈ A`, write `A_{f} = A{S_f⁻¹}` with `S_f = {fⁿ : n ≥ 0}`, and `𝔞_{f} = 𝔞{S_f⁻¹}` for an open ideal
`𝔞`. For `g ∈ A`, there is a canonical `A_{f} → A_{fg}` (7.6.7). For `S` multiplicative, set
`A_{S} = lim⃗_{f ∈ S} A_{f}`; there is a canonical `A_{S} → A{S⁻¹}`.

**Proposition (7.6.16).** If `A` is Noetherian, `A{S⁻¹}` is flat over `A_{S}`.

**Proof.** By (7.6.14), `A{S⁻¹}` is flat over each `A_{f}` (`f ∈ S`); conclude by (6.2.3).

**Proposition (7.6.17).** Let `𝔭` be an open prime ideal in an admissible ring `A`, and `S = A − 𝔭`. Then `A{S⁻¹}` and
`A_{S}` are local rings, the canonical `A_{S} → A{S⁻¹}` is local, and both residue fields are canonically the field of
fractions of `A/𝔭`.

**Corollary (7.6.18).** If moreover `A` is adic Noetherian, then `A{S⁻¹}` and `A_{S}` are Noetherian local rings, and
`A{S⁻¹}` is a faithfully flat `A_{S}`-module.

### 7.7. Completed tensor products

<!-- label: 0.7.7 -->

**(7.7.1)** Let `A` be linearly topologized and `M, N` two linearly topologized `A`-modules. Let `𝔍 ⊂ A`, `V ⊂ M`,
`W ⊂ N` be open submodules with `𝔍 M ⊂ V`, `𝔍 N ⊂ W`. The `(M/V) ⊗_{A/𝔍} (N/W)` form a projective system; their limit is
an `Â`-module, the _completed tensor product_, written `(M ⊗_A N)^∧`. In terms of completions,
`(M ⊗_A N)^∧ ≅ M̂ ⊗̂_Â N̂`.

**(7.7.2)** `(M ⊗_A N)^∧` is the separated completion of `M ⊗_A N` for the topology whose fundamental system of
neighborhoods of `0` consists of `Im(V ⊗_A N) + Im(M ⊗_A W)` (`V, W` open in `M, N`); this is the _tensor product
topology_.

**(7.7.3)** For continuous `u : M → M′` and `v : N → N′`, there is a continuous `u ⊗̂ v : (M ⊗_A N)^∧ → (M′ ⊗_A N′)^∧`.
Thus `(M ⊗_A N)^∧` is bifunctorial in `M, N`.

**(7.7.4)** Similarly for any finite number of factors, with associativity and commutativity.

**(7.7.5)** For `A`-algebras `B, C` linearly topologized, `B ⊗_A C` carries a tensor-product ring topology whose
fundamental system of neighborhoods of `0` consists of ideals `Im(𝔎 ⊗_A C) + Im(B ⊗_A 𝔏)` (`𝔎, 𝔏` open ideals of
`B, C`). `(B ⊗_A C)^∧` is a topological `Â`-algebra.

**(7.7.6) Universal property.** For every separated, complete `A`-algebra `D` and every pair `(u, v)` of continuous
`A`-homomorphisms `u : B → D`, `v : C → D`, there is a unique continuous `A`-homomorphism `w : (B ⊗_A C)^∧ → D` with
`u = w ∘ ρ`, `v = w ∘ σ` (where `ρ, σ` are the canonical maps from `B, C`).

**Proposition (7.7.7).** If `B, C` are preadmissible `A`-algebras, then `(B ⊗_A C)^∧` is admissible; if `𝔎, 𝔏` are
ideals of definition of `B, C`, the closure in `(B ⊗_A C)^∧` of the canonical image of `Im(𝔎 ⊗_A C) + Im(B ⊗_A 𝔏)` is an
ideal of definition.

**Proof.** Use `𝔥^{2n} ⊂ Im(𝔎ⁿ ⊗_A C) + Im(B ⊗_A 𝔏ⁿ)`.

**Proposition (7.7.8).** Let `A` be preadic with ideal of definition `𝔍`, `M` an `A`-module of finite type with the
`𝔍`-preadic topology. For every adic Noetherian `A`-algebra `B`, `B ⊗_A M` is identified with `(B ⊗_A M)^∧`.

### 7.8. Topologies on modules of homomorphisms

<!-- label: 0.7.8 -->

**(7.8.1)** Let `A` be a Noetherian `𝔍`-adic ring, `M, N` two `A`-modules of finite type with `𝔍`-preadic topology. By
(7.3.6), they are separated and complete; every `A`-homomorphism `M → N` is continuous, and `Hom_A(M, N)` is
`A`-finite-type. With `A_i = A/𝔍^{i+1}`, `M_i = M/𝔍^{i+1} M`, `N_i = N/𝔍^{i+1} N`, the `Hom_{A_i}(M_i, N_i)` form a
projective system, and by (7.2.10) there is a canonical `φ : Hom_A(M, N) ⥲ lim⃖_i Hom_{A_i}(M_i, N_i)`.

**Proposition (7.8.2).** Under the hypotheses of (7.8.1), the submodules `Hom_A(M, 𝔍^{i+1} N)` form a fundamental system
of neighborhoods of `0` in `Hom_A(M, N)` for the `𝔍`-adic topology, and `φ` is a topological isomorphism.

**Proof.** Reduce to `M = L = Aᵐ`; then `Hom_A(L, N) = Nᵐ` and `Hom_A(L, 𝔍^{i+1} N) = 𝔍^{i+1} Nᵐ`.

**Proposition (7.8.3).** Under the hypotheses of (7.8.2), the set of injective (resp. surjective, bijective)
homomorphisms `M → N` is open in `Hom_A(M, N)`.

**Proof.** For surjectivity: by (7.3.5) and (7.1.14), `u` is surjective iff `u_0 : M/𝔍M → N/𝔍N` is, so the set is the
preimage of a discrete subset under the continuous `Hom_A(M, N) → Hom_{A_0}(M_0, N_0)`. For injectivity: let `v : M → N`
be injective and set `M′ = v(M)`. By Artin–Rees (7.3.2.1), there is `k ≥ 0` with `M′ ∩ 𝔍^{m+k} N ⊂ 𝔍ᵐ M′` for `m > 0`.
For `w ∈ 𝔍^{k+1} Hom_A(M, N)`, `u = v + w` is injective: if `u(x) = 0` and `x ∈ 𝔍ⁱ M`, then `w(x) ∈ 𝔍^{i+k+1} N`, so
`v(x) = −w(x) ∈ M′ ∩ 𝔍^{i+k+1} N ⊂ 𝔍^{i+1} M′`, hence `x ∈ 𝔍^{i+1} M`. By induction, `x ∈ ⋂ 𝔍ⁱ M = 0`.

