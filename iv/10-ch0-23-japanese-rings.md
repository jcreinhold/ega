<!-- original page 213 -->

## §23. Japanese rings

The results of this section will be completed in `(IV, 7.6)` and `(7.7)`.

### 23.1. Japanese rings

**Definition (23.1.1).**

<!-- label: 0_IV.23.1.1 -->

*We say that an integral ring `A` is a **Japanese ring** if, for every finite extension `K'` of its field of fractions
`K`, the integral closure `A'` of `A` in `K'` is an `A`-module of finite type (in other words, a finite `A`-algebra). We
say that a ring `A` is **universally Japanese** if every integral `A`-algebra of finite type is a Japanese ring.*

> _Translator's note._ "Japanese ring" is EGA's vocabulary, following Akizuki's circle and Nagata's early papers. The
> modern literature usually calls these "Nagata rings" or, with a slightly different condition, "pseudo-geometric rings"
> (Matsumura). We preserve EGA's term throughout.

<!-- original page 214 -->

It is clear that if `A` is a Japanese ring, then every ring of fractions `S⁻¹A` is also a Japanese ring, since (with the
preceding notation) `S⁻¹A'` is the integral closure of `S⁻¹A` in `K'`, and is evidently an `S⁻¹A`-module of finite type.

An integral Noetherian ring, even a discrete valuation ring, is not necessarily a Japanese ring `[30]`.

**Proposition (23.1.2).**

<!-- label: 0_IV.23.1.2 -->

*Let `A` be an integral Noetherian ring, `K` its field of fractions. If, for every finite radicial extension `K'` of
`K`, the integral closure of `A` in `K'` is an `A`-module of finite type, then `A` is a Japanese ring.*

Since `A` is Noetherian, in order to verify that `A` is a Japanese ring, it suffices to see that for every finite
quasi-Galois extension `L` of `K`, the integral closure `B` of `A` in `L` is an `A`-module of finite type. Now `L` is a
Galois extension of the greatest radicial extension `K'` of `K` contained in `L`; and if `A'` is the integral closure of
`A` in `K'`, then `B` is the integral closure of `A'` in `L`. But we know that in a separable extension of `K'`, the
integral closure of `A'` is an `A'`-module of finite type (Bourbaki, _Alg. comm._, chap. V, §1, n° 6, cor. 1 of prop.
20), whence the proposition.

It follows from `(23.1.2)` that when `K` is of characteristic `0`, to say that `A` is a Japanese ring means that its
integral closure `A'` is an `A`-module of finite type.

**Theorem (23.1.3) (Tate).**

<!-- label: 0_IV.23.1.3 -->

*Let `A` be an integral Noetherian ring, `x ≠ 0` an element of `A`. Suppose the following conditions are satisfied:*

*(i) `A` is integrally closed.*

*(ii) `𝔭 = xA` is prime and `A` is separated and complete for the `𝔭`-preadic topology.*

*(iii) `A/xA` is a Japanese ring.*

*Then `A` is a Japanese ring.*

We shall use the following lemma:

**Lemma (23.1.3.1).**

<!-- label: 0_IV.23.1.3.1 -->

*Let `A` be a ring, `x` an element of `A` not a zero-divisor in `A` and such that `xA = 𝔭` is prime; then, for every
integer `n > 0`, the inverse image of `xⁿA_𝔭` in `A` is `xⁿA`.*

Indeed, suppose that `b ∈ A` is an element such that `b/1 = xⁿa/s` in `A_𝔭`, where `a ∈ A` and `s ∉ 𝔭`; there exists
therefore `s' ∉ 𝔭` such that `s'sb = xⁿas`, whence `s'sb ∈ 𝔭`, and since `s's ∉ 𝔭`, this entails `b ∈ 𝔭`, in other words
`b = xb'` with `b' ∈ A`; since `x` is not a zero-divisor, we conclude `s'sb' = xⁿ⁻¹as` and it suffices to reason by
induction on `n`.

To prove the theorem, we may restrict to the case where the field of fractions `K` of `A` is of characteristic `p > 0`,
since `A` is integrally closed. Let `K'` be a finite radicial extension of `K`, so that there exists a power `q = p^e`
such that `K'^q ⊂ K`; by replacing `K'` by a larger radicial extension, we may even suppose that there exists `y ∈ K'`
such that `y^q = x`. Let `A'` be the integral closure of `A` in `K'`; since `A` is integrally closed, `A'` is the set of
`x' ∈ K'` such that `x'^q ∈ A' ∩ K = A`. Set `V = A_𝔭`; the maximal ideal `𝔪 = xV` of `V` being principal, we know that
the Noetherian local ring `V` is a discrete valuation ring `(17.1.4)`; since `V` is integrally closed, the same

<!-- original page 215 -->

reasoning as above shows that the integral closure `V'` of `V` in `K'` is the set of `x' ∈ K'` such that `x'^q ∈ V`; we
know (Bourbaki, _Alg. comm._, chap. VI, §8, n° 6, prop. 6, and chap. V, §2, n° 3, lemma 4) that `V'` is a discrete
valuation ring, whose maximal ideal `𝔪'` is the set of `x' ∈ K'` such that `x'^q ∈ 𝔪`, and moreover the residue field
`V'/𝔪'` is a finite extension of `V/𝔪` (_loc. cit._, chap. VI, §8, n° 1, lemma 2). Let us show that, for every integer
`n > 0`, we have

```text
  𝔪'ⁿ ∩ A' = yⁿA'.                                                            (23.1.3.2)
```

Indeed, since `y^q = x`, we have `y^q ∈ 𝔪'`, hence `yⁿA' ⊂ 𝔪'ⁿ ∩ A'`. Conversely, let `x' ∈ 𝔪'ⁿ ∩ A'`, and set
`x' = z'yⁿ` with `z' ∈ K'`. We have `x'^q ∈ A'`; on the other hand, `x'^q` is a sum of products `t'_1 … t'_n` with
`t'_i ∈ 𝔪'`, hence `t'^q_i ∈ 𝔪`, and we conclude that `x'^q ∈ 𝔪ⁿ ∩ A`. Now lemma `(23.1.3.1)` proves that
`𝔪ⁿ ∩ A = xⁿA`, hence we have `z'^q xⁿ ∈ xⁿA`, or again `z'^q ∈ A` since `x ≠ 0`, which establishes `(23.1.3.2)`.

Let us show in the second place that on `A'` the `xA'`-preadic topology is separated; this topology is also the
`yA'`-preadic topology of `A'`, and it follows from `(23.1.3.2)` that this topology is induced by the `𝔪'`-preadic
topology of `V'`, which is separated since `V'` is a discrete valuation ring.

Let us next prove that `A'/xA'` is an `A`-module of finite type. Since `x = y^q` and `y^k A' / y^{k+1} A'` is isomorphic
to `A'/yA'`, we may restrict to showing that `A'/yA'` is an `A`-module of finite type; but formula `(23.1.3.2)` applied
for `n = 1` shows that `A'/yA'` is a subring of `V'/𝔪'`, that is to say of the residue field of `V'`, which is a finite
extension of the residue field `V/𝔪` of `V`. Now `V/𝔪` is the field of fractions of `A/𝔭`, and since `A'` is integral
over `A`, `A'/yA'` is integral over `A/𝔭`, hence contained in the integral closure of `A/𝔭` in `V'/𝔪'`; since by
hypothesis `A/𝔭` is a Noetherian Japanese ring, `A'/yA'` is an `(A/𝔭)`-module of finite type, and _a fortiori_ an
`A`-module of finite type.

This being so, the `xA'`-preadic topology of `A'` being separated, `A'` is a subring of its completion `Â'` for this
topology; but since `A'/xA'` is an `A`-module of finite type and `A` is separated and complete for the `xA`-preadic
topology, `Â'` is an `A`-module of finite type by virtue of `(0_I, 7.2.9)`, hence so is `A'`. `Q.E.D.`

**Corollary (23.1.4).**

<!-- label: 0_IV.23.1.4 -->

*Let `A` be a Noetherian integrally closed Japanese ring. Then every ring of formal power series `A[[T_1, …, T_r]]` is a
Japanese ring.*

We know that for every Noetherian integrally closed ring `B`, the ring of formal power series `B[[T]]` is Noetherian and
integrally closed (Bourbaki, _Alg. comm._, chap. V, §1, n° 4, prop. 14); we may therefore, by induction on `n`, restrict
to proving that `A[[T]]` is a Japanese ring. Now the element `x = T` verifies all the conditions of `(23.1.3)`, whence
the conclusion.

**Theorem (23.1.5) (Nagata).**

<!-- label: 0_IV.23.1.5 -->

*Every complete integral Noetherian local ring `A` is a Japanese ring.*

We know `(19.8.8, (ii))` that there exists a subring `B` of `A` which is a complete regular local ring, such that `A` is
a finite `B`-algebra; it evidently suffices to prove

<!-- original page 216 -->

that `B` is a Japanese ring, in other words, we may restrict to the case where `A` is moreover regular. Let us reason by
induction on `n = dim(A)`, the theorem being evident for `n = 0`. So suppose `n > 0`, and, denoting by `𝔪` the maximal
ideal of `A`, let `x` be an element of `𝔪 - 𝔪²`; we know `(17.1.8)` that `A/xA` is a regular ring, and moreover
(`(17.1.7)` and `(16.3.4)`) that `dim(A/xA) = n - 1`; furthermore, the ideal `xA` is closed in `A` `(0_I, 7.3.5)`, hence
`A/xA` is complete. By virtue of the induction hypothesis, `A/xA` is therefore a Japanese ring, and it then follows from
`(23.1.3)` that so is `A`.

**Corollary (23.1.6).**

<!-- label: 0_IV.23.1.6 -->

*Let `A` be a complete integral Noetherian local ring, `K` its field of fractions, `K'` a finite extension of `K`; then
the integral closure `A'` of `A` in `K'` is a complete local ring.*

We already know by `(23.1.5)` that `A'` is a finite `A`-algebra, hence a complete Noetherian semi-local ring, and
consequently a direct composite of local rings; but since `A'` is integral, it is necessarily a local ring.

**Proposition (23.1.7).**

<!-- label: 0_IV.23.1.7 -->

*Let `A` be an integral Noetherian local ring, `K` its field of fractions, `K'` a finite extension of `K`, `A'` the
integral closure of `A` in `K'`. Suppose that the completion `Â` is reduced, and denote by `R` its total ring of
fractions.*

*(i) If the ring `R ⊗_K K'` is reduced (which will happen in particular when `K'` is a separable extension of `K`, `R`
being a direct composite of fields, extensions of `K` (Bourbaki, _Alg._, chap. VIII, §7, n° 3, cor. 1 of th. 1)), then
`A'` is an `A`-module of finite type.*

*(ii) If in particular `R` is a separable `K`-algebra, then `A` is a Japanese ring.*

(i) Set for simplicity `A_1 = Â`, `A'_1 = A' ⊗_A A_1`, `K'_1 = K' ⊗_A A_1`. Since `A_1` is a flat `A`-module
`(0_I, 7.3.5)`, `A'_1` identifies with a subring of `K'_1` and is evidently integral over `A_1`. On the other hand, if
we set `K_1 = K ⊗_A A_1`, we may write `K'_1 = K' ⊗_K K_1`; since `A` is integral and `A_1` is a flat `A`-module, every
element `≠ 0` of `A` is `A_1`-regular `(0_I, 6.3.4)`; since `K = S⁻¹A`, where `S = A - {0}`, we have `K_1 = S⁻¹A_1`, and
the preceding remark proves that `K_1` identifies with a subring of the total ring of fractions `R` of `A_1`. Since
every `K`-module is flat, `K'_1` identifies with a subring of `K' ⊗_K R`, which by hypothesis is reduced and is a finite
`R`-algebra. Denote by `𝔮_i (1 ≤ i ≤ n)` the minimal prime ideals of `A_1`, by `B_i` the integral ring `A_1/𝔮_i`, by
`L_i` the field of fractions of `B_i`, so that `R` is a direct composite of the `L_i`, and `K' ⊗_K R` a direct composite
of the `K' ⊗_K L_i`; these latter `K`-algebras, being reduced, are direct composites of fields, finite extensions of the
`L_i`. Since `B_i` is a complete integral local ring, Nagata's theorem `(23.1.5)` proves that the integral closure of
`B_i` in `K' ⊗_K L_i` is a `B_i`-module of finite type, and _a fortiori_ an `A_1`-module of finite type; since every
element of `K' ⊗_K R` which is integral over `A_1` is also integral over `B_i` (being annihilated by `𝔮_i`), we finally
conclude that the integral closure of `A_1` in `K' ⊗_K R` is an `A_1`-module of finite type. But since `A'_1` is
contained in this integral closure and `A_1` is Noetherian, `A'_1` is also an `A_1`-module of finite type. Finally,
since `A_1` is a faithfully flat `A`-module `(0_I, 7.3.5)`, we conclude that `A'` is an `A`-module of finite type
(Bourbaki, _Alg. comm._, chap. I, §3, n° 6, prop. 11).

<!-- original page 217 -->

(ii) The hypothesis entails that the `L_i` are separable extensions of `K`, hence `K' ⊗_K R` is reduced (Bourbaki,
_Alg._, chap. VIII, §7, n° 3, th. 1), and one may apply (i) to every finite extension `K'` of `K`, which proves our
assertion.

### 23.2. Integral closure of an integral Noetherian local ring.

**(23.2.1)**

<!-- label: 0_IV.23.2.1 -->

In what follows, for every ring `A`, we shall write `A_red` for short to denote the quotient of `A` by its nilradical
(so that if `X = Spec(A)`, we have `X_red = Spec(A_red)`).

We shall say that a local ring `A` is **unibranch** if the ring `A_red` is integral and if the integral closure of
`A_red` is a local ring, which generalizes the definition given in `(III, 4.3.6)`. We shall say that `A` is
**geometrically unibranch** if it is unibranch and if the residue field of the local ring (which is the integral closure
of `A_red`) is a radicial extension of that of `A`. It is clear that an integrally closed local ring is geometrically
unibranch; it follows from `(23.1.6)` that a complete integral Noetherian local ring is unibranch.

**Lemma (23.2.2)** [\*].

<!-- label: 0_IV.23.2.2 -->

*Let `A` be an integral ring, `A'` its integral closure; for the canonical morphism `f : Spec(A') → Spec(A)` to be
radicial, it is necessary and sufficient that for every `𝔭 ∈ Spec(A)`, `A_𝔭` be geometrically unibranch; when this is
the case, `f` is a homeomorphism.*

Indeed, for every `𝔭 ∈ Spec(A)`, the integral closure of `A_𝔭` is `A'_𝔭` (Bourbaki, _Alg. comm._, chap. V, §1, n° 5,
prop. 16), and all the prime ideals of `A'_𝔭` above `𝔭A_𝔭` are maximal (_loc. cit._, §2, n° 1, prop. 1). To say that `f`
is injective therefore means that for every `𝔭 ∈ Spec(A)`, `A'_𝔭` is a local ring, that is to say that the `A_𝔭` are
unibranch. To say that every `A_𝔭` is geometrically unibranch then means that `f` is radicial by virtue of `(I, 3.5.8)`.
When this is the case, `f` is surjective and closed `(II, 6.1.10)`, hence a homeomorphism.

[\*] _In the remainder of this number, we use notions and results expounded in chap. IV, §§2 and 5; since the results of
this number are not used before chap. IV, §6, this does not entail any vicious circle._

**Lemma (23.2.3).**

<!-- label: 0_IV.23.2.3 -->

*Let `A` be an integral ring, `K` its field of fractions, `B` a Noetherian ring, `φ : A → B` a ring homomorphism making
`B` a flat `A`-module. Let `K'` be an extension of `K`; set `B_1 = B_red`, and let `R` be the total ring of fractions of
`B_1`. Then, for every sub-`A`-algebra `A'` of `K'`, the canonical homomorphism*

```text
  (A' ⊗_A B)_red → (K' ⊗_A R)_red                                             (23.1.8.1)
```

*is injective.*

We may consider the canonical homomorphism `h : A' ⊗_A B → K' ⊗_A R` as the composite of the following homomorphisms

```text
  A' ⊗_A B  ⟶  K' ⊗_A B  ⟶  K' ⊗_A B_1  ⟶  K' ⊗_A R.
            u            v              w
```

Since `B` is a flat `A`-module, `u` is injective; similarly, `K'` being a flat `K`-module and `K` a flat `A`-module,
`K'` is a flat `A`-module, and `w` is therefore injective since `B_1` is reduced, hence the homomorphism `B_1 → R`
injective. Finally, for the same reason, if `𝔑` is

<!-- original page 218 -->

the nilradical of `B`, the kernel of `v` is `K' ⊗_A 𝔑`, hence it is contained in the nilradical of `K' ⊗_A B`; we
conclude immediately that if the image under `h = w ∘ v ∘ u` of an element `x ∈ A' ⊗_A B` is nilpotent, then `x` is
nilpotent, which proves the lemma.

**Proposition (23.2.4).**

<!-- label: 0_IV.23.2.4 -->

*Let `A` be an integral ring, `K` its field of fractions, `B` a Noetherian ring, `𝔮_i (1 ≤ i ≤ n)` its minimal prime
ideals, `φ : A → B` a ring homomorphism. Suppose that the `B/𝔮_i` are Japanese rings, and that `B` is a flat `A`-module.
Let `K'` be a finite extension of `K`, and let `(C_λ)` be the increasing filtering family of subrings of `K'` which are
finite `A`-algebras and admit `K'` for field of fractions; the union `A'` of the `C_λ` is therefore the integral closure
of `A` in `K'`. Then:*

*(i) There exists an index `α` such that for `λ ≥ α`, the canonical homomorphism*

```text
  (C_α ⊗_A B)_red → (C_λ ⊗_A B)_red                                           (23.2.4.1)
```

*is bijective.*

*(ii) If moreover `B` is a faithfully flat `A`-module, the morphism `Spec(A' ⊗_A B) → Spec(C_α ⊗_A B)` is radicial.*

(i) Let `B_1 = B_red`, and let `R` be the total ring of fractions of `B_1`; since `A` is integral and `B` a flat
`A`-module, every element `≠ 0` of `A` is `B`-regular `(0_I, 6.3.4)`, hence the composite homomorphism `A → B → B_1`
extends to a homomorphism `K → R`; we may then write `K' ⊗_A R = K' ⊗_K K ⊗_A R`, and since `K' ⊗_K K` identifies with
`K'`, we have `K' ⊗_A R = K' ⊗_K R`. Since `R` is a direct composite of the fields of fractions `L_i` of the `B/𝔮_i`,
`K' ⊗_K R` is a direct composite of the `K' ⊗_K L_i`, and consequently `(K' ⊗_K R)_red` is a direct composite of a
finite number of finite extensions of the `L_i`. By virtue of the hypothesis, the integral closure of `B/𝔮_i` in a
finite extension of `L_i` is a `(B/𝔮_i)`-module of finite type, hence a `B`-module of finite type; we conclude that the
integral closure `B'` of `B` in `(K' ⊗_A R)_red` is a `B`-module of finite type. By virtue of `(23.2.3)`, the
`(C_λ ⊗_A B)_red` identify canonically with subrings of `(K' ⊗_A R)_red` which are finite `B`-algebras, hence contained
in `B'`. Since `B` is Noetherian and `B'` a `B`-module of finite type, the filtering family of the `(C_λ ⊗_A B)_red`
admits a greatest element `(C_α ⊗_A B)_red`, which proves (i).

(ii) Since `B` is a faithfully flat `A`-module, it suffices `(IV, 2.6.1, (v))` to show that the morphism
`Spec(A' ⊗_A B) → Spec(C_α ⊗_A B)` is radicial, or, what amounts to the same `(I, 5.1.6)`, that the morphism
`Spec(A' ⊗_A B)_red → Spec(C_α ⊗_A B)_red` is radicial; but one has `A' ⊗_A B = lim⃗_λ (C_λ ⊗_A B)`, hence
`(IV, 5.13.2)` `(A' ⊗_A B)_red = lim⃗_λ (C_λ ⊗_A B)_red`, and the conclusion results from (i).

**Corollary (23.2.5).**

<!-- label: 0_IV.23.2.5 -->

*Let `A` be an integral Noetherian local ring, `K` its field of fractions, `K'` a finite extension of `K`. Let `(C_λ)`
be the increasing filtering family of subrings of `K'` which are finite `A`-algebras (hence Noetherian semi-local rings
(Bourbaki, _Alg. comm._, chap. IV, §2, n° 5, cor. 3 of prop. 9)) and admit `K'` for field of fractions. Then there
exists `α` such that the homomorphism `(Ĉ_α)_red → (Ĉ_λ)_red` is an isomorphism for `λ ≥ α`, and if `A'` is the integral
closure of `A` in `K'`, the morphism `Spec(Â') → Spec(Ĉ_α)` is radicial (cf. `(23.2.2)`).*

<!-- original page 219 -->

We apply `(23.2.4)` taking `B = Â`; since the `B/𝔮_i` are complete Noetherian local rings, they are Japanese rings
`(23.1.5)` and `B` is a faithfully flat `A`-module `(0_I, 7.3.5)`; moreover one has `C_λ ⊗_A B = Ĉ_λ` (Bourbaki, _Alg.
comm._, chap. III, §3, n° 4, th. 3 and chap. IV, §2, n° 5, cor. 3 of prop. 9).

**Corollary (23.2.6).**

<!-- label: 0_IV.23.2.6 -->

*Under the hypotheses of `(23.2.5)`, the integral closure `A'` of `A` in `K'` is a semi-local ring; if `𝔪` is the
maximal ideal of `A`, then, for every maximal ideal `𝔪'` of `A'`, `A'/𝔪'` is a finite extension of `A/𝔪`.*

The fact that the homomorphism `(Ĉ_α)_red → (Ĉ_λ)_red` is bijective for `λ ≥ α` entails that the number of maximal
ideals of `C_λ` is constant for `λ ≥ α` and that if `𝔪_α` is a maximal ideal of `C_α` and `𝔪_λ` the unique maximal ideal
of `C_λ` above `𝔪_α`, the fields `C_λ/𝔪_λ` and `C_α/𝔪_α` are canonically isomorphic. The conclusion results from the
fact that `𝔪' = lim⃗ 𝔪_λ` and `A'/𝔪' = lim⃗ (C_λ/𝔪_λ)` `(0_III, 10.3.1.3)`.

**Proposition (23.2.7) (Y. Mori).**

<!-- label: 0_IV.23.2.7 -->

*Let `A` be an integral Noetherian local ring, `K` its field of fractions, `A'` the integral closure of `A`. Then `A'`
is a semi-local Krull ring (Bourbaki, _Alg. comm._, chap. VII, §1); in other words, there exists a family `(V_λ)` of
discrete valuation rings having `K` for field of fractions, such that `A' = ⋂ V_λ` and that every `x ∈ K` belongs to all
the `V_λ` save for a finite number of them. Moreover, there exists a subring `C` of `K` which is a finite `A`-algebra,
and such that the `V_λ` are the integral closures of the rings `C_{𝔭_λ}`, where `(𝔭_λ)` is the family of prime ideals of
height `1` of the local ring `C`.*

Let us first prove the following lemma:

**Lemma (23.2.7.1).**

<!-- label: 0_IV.23.2.7.1 -->

*Let `A`, `B` be two rings, `φ : A → B` a homomorphism making `B` a faithfully flat `A`-module. Suppose that `A` is
integral; then, if `C = B_red`, the composite homomorphism `ψ : A → B → B_red = C` is injective and extends to an
injective homomorphism of the field of fractions `K` of `A` into the total ring of fractions `R` of `C`; moreover, if
`C'` is the integral closure of `C` in `R`, then `C' ∩ K` is the integral closure of `A`.*

Since `A` is integral and `φ` injective, the intersection of `φ(A)` and the nilradical `𝔑` of `B` is reduced to `0`, and
since `C = B/𝔑`, `ψ` is injective. Every `a ≠ 0` in `A` being a non-zero-divisor in `A` is no more so in `B` by flatness
`(0_I, 6.3.4)`; we deduce that `a` is also not a zero-divisor in `C`, for if one had `ax ∈ 𝔑` for an `x ∉ 𝔑` in `B`, one
would deduce `aⁿxⁿ = 0` for an integer `n`, which contradicts the preceding since `xⁿ ≠ 0`. We may therefore extend `ψ`
to an injective homomorphism of `K` into `R`. To prove the last assertion, note that it is clear that the integral
closure `A'` of `A` is contained in `C' ∩ K`. Conversely, let `x ∈ C' ∩ K`; `x` is therefore integral over `C`, and _a
fortiori_ over `B`, in other words `B[x]` is a finite `B`-algebra; moreover, `K` identifies with a subring of `B ⊗_A K`,
and the subring `B[x]` of `B ⊗_A K` identifies with `B ⊗_A A[x]` by flatness; we conclude that `A[x]` is an `A`-module
of finite type (Bourbaki, _Alg. comm._, chap. I, §3, n° 6, prop. 11), hence that `x ∈ A'`.

This lemma being established, we shall apply it to the canonical injection of `A` into its completion `Â`, which is a
faithfully flat `A`-module; `B = (Â)_red = Â/𝔑` (where `𝔑` is the nilradical of `Â`) is a reduced complete Noetherian
local ring, whose total ring of

<!-- original page 220 -->

fractions `R` is therefore a direct composite of a finite number of fields `L_i`; the canonical image `B_i` of `B` in
`L_i` is an integral and complete Noetherian local ring, of which `L_i` is the field of fractions, and the integral
closure `B'` of `B` in `R` is the direct composite of the `B'_i`, where `B'_i` is the integral closure of `B_i`. But by
virtue of `(23.1.5)`, `B'_i` is a finite `B_i`-algebra, hence an integrally closed Noetherian local ring. We know
(Bourbaki, _Alg. comm._, chap. VII, §1, n° 3, cor. of th. 2) that `B'_i` is a Krull ring. Now, for every `i`, we have a
homomorphism `φ_i : K → L_i`, which is injective, and consequently `φ_i⁻¹(B'_i)` is a Krull ring in `K`. But since
`A' = B' ∩ K` by virtue of the lemma and `B' = ⋂_i φ_i⁻¹(B'_i)`, `A'` is the intersection of a finite number of Krull
rings and is consequently a Krull ring. To prove the last assertion of the proposition, note that there exists a finite
`A`-algebra `C ⊂ K` such that the morphism `Spec(A') → Spec(C)` is radicial and a homeomorphism `(23.2.4)`; for every
prime ideal `𝔭' ∈ Spec(A')`, `𝔭'` is therefore the only prime ideal of `A'` above `𝔭 = 𝔭' ∩ C` and `A'_{𝔭'}` the
integral closure of `C_𝔭`; on the other hand, the fact that `Spec(A') → Spec(C)` is a homeomorphism entails that the map
`𝔭' ↦ 𝔭' ∩ C` is a bijection from the set of prime ideals of height `1` of `A'` onto the set of prime ideals of height
`1` of `C`; whence the conclusion, taking account of Bourbaki, _Alg. comm._, chap. VII, §1, n° 6, th. 4.

**Remarks (23.2.8).**

<!-- label: 0_IV.23.2.8 -->

*(i) One must take care to note, in the application of `(23.2.6)` and `(23.2.7)`, that the ring `A'` is not necessarily
a Noetherian ring, as an example of Nagata with `dim(A) = 3` shows `[30]`.*

*(ii) The conclusions of `(23.2.7)` are still valid if `A'` is the integral closure of `A` in a finite extension `K'` of
`K`; it suffices in fact to consider a finite `A`-algebra `B` of which `K'` is the field of fractions; `B` is a
Noetherian semi-local ring, hence an intersection of a finite number of Noetherian local rings `B_{𝔪_i}` (`𝔪_i` maximal
ideals of `B`), and its integral closure (which is equal to `A'`) is the intersection of the `A'_{𝔪_i}` (Bourbaki, _Alg.
comm._, chap. II, §3, n° 3, cor. 4 of th. 1) which are the integral closures of the `B_{𝔪_i}`, hence Krull rings by
`(23.2.7)`; consequently `A'` is a Krull ring.*

*(iii) One can show (`[30]`, 3.3.10) that for every integral Noetherian ring `A` (not necessarily local), the integral
closure of `A` is a Krull ring.*

**Corollary (23.2.9).**

<!-- label: 0_IV.23.2.9 -->

*Let `A` be an integral Noetherian ring, `A'` its integral closure. Suppose that for every ring `C` such that
`A ⊂ C ⊂ A'` and such that `C` is a finite `A`-algebra, and for every prime ideal `𝔮` of height `1` in `C`, `𝔮 ∩ A` is a
prime ideal of height `1` in `A`. Let `P` be the set of prime ideals of height `1` in `A'`; then one has*

```text
  A' = ⋂_{𝔭 ∈ P} A'_𝔭.
```

Since `A'` is a torsion-free `A`-module, one has `A' = ⋂_𝔪 A'_𝔪`, where `𝔪` runs through the set of maximal ideals of
`A` (Bourbaki, _Alg. comm._, chap. II, §3, n° 3, cor. 4 of th. 1); it will therefore suffice to prove that `A'_𝔪` is the
intersection of the `A'_𝔭` for the prime ideals `𝔭 ⊂ 𝔪` of height `1`. Since `A'_𝔪` is the integral closure of `A_𝔪`, we
see that we may restrict to demonstrating the corollary for `A_𝔪`. Now there is then, by virtue of `(23.2.7)`, an
`A_𝔪`-algebra

<!-- original page 221 -->

`B` of finite type contained in `A'_𝔪` such that `A'_𝔪` is the intersection of the integral closures of the rings `B_𝔮`,
where `𝔮` runs through the set of prime ideals of height `1` of `B`. But `B` is of the form `C_𝔪`, where `C` is a finite
`A`-algebra; hence, for every prime ideal `𝔮` of height `1` in `B`, `𝔮 ∩ A` is by hypothesis a prime ideal of height `1`
in `A`; since the integral closure of `B_𝔮` contains that of `A_{𝔮 ∩ A}` and the latter contains `A'_𝔪`, it indeed
follows that `A'_𝔪` is the intersection of the `A'_𝔭` for `𝔭 ∈ P` and `𝔭 ⊂ 𝔪`, which completes the proof.

**Remarks (23.2.10).**

<!-- label: 0_IV.23.2.10 -->

*(i) We shall see (`(IV, 5.6.3)` and `(5.6.10)`) that the hypothesis of `(23.2.9)` is satisfied when `A` is universally
catenary, in particular (`(IV, 5.10.17)` and `(5.11.2)`) when `A` is a quotient of a regular ring; finally, it is
evidently satisfied if `Spec(A') → Spec(A)` is a homeomorphism, in particular if this morphism is radicial `(23.2.2)`.*

*(ii) The conclusion of `(23.2.9)` is no longer necessarily exact when one omits the hypothesis on the finite
sub-`A`-algebras of `A'`. Indeed, one can define an integral Noetherian local ring `A`, of dimension `2`, whose integral
closure `A'` is a finite `A`-algebra, but such that there is a prime ideal `𝔭'` of `A'` of height `1` above the maximal
ideal `𝔪` (of height `2`) of `A`, and such moreover that for every prime ideal `𝔭` of height `1` in `A`, `A_𝔭` is
integrally closed `(IV, 5.6.11)`; the intersection of these rings `A_𝔭` cannot then be equal to `A'` since `A'` is a
Krull ring (Bourbaki, _Alg. comm._, chap. VII, §1, n° 5, prop. 9).*

(_To be continued._)
