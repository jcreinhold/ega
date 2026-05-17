<!-- original page 182 -->

## §7. Application to relations between a Noetherian local ring and its completion. Excellent rings.

The present section is devoted above all to the exposition of certain properties of Noetherian rings, generally stable
under passage to an algebra of finite type or under localization, which are true for the rings one encounters most often
(algebras of finite type over `Z`, or over a field, or over a complete Noetherian local ring), without being so for all
Noetherian rings. A first series of properties, tied to the theory of dimension and especially to the chain condition,
forms the subject of nos. 1 and 2; all the properties envisaged are true for the quotients of regular Noetherian rings,
and their proofs in this case are for the most part easy and well known [30]; for these rings the developments of §§1
and 2 are accordingly of no interest.

This is no longer so for the properties studied in nos. 3, 4 and 5 (which do not depend on nos. 1 and 2); their proofs,
even in the case of the localizations of algebras of finite type over a field or over `Z` (where they are due for the
most part to Zariski and Nagata), are most often delicate; classical examples are for instance the equivalences `A`
normal `⇔ Â` normal, and `A` reduced `⇔ Â` reduced. We develop a systematic method for formulating and proving such
properties, by means of the properties of the *fibres* of the canonical morphism `Spec(Â) → Spec(A)` and using the
notions and results expounded in §6; the success of this method rests in the last analysis on the excellent properties
of *complete local rings* and of those deduced from them by localization or passage to an algebra of finite type. In
this regard, Nagata's theorem `(6.12.7)` saying that, for such a ring, the singular locus in `Spec(A)` is closed plays a
crucial role; the same is so (concerning the permanence properties) of the regularity criterion `(0, 22.3.4)`, which is
more technical in nature.

Finally, in nos. 6 and 7, we apply the results obtained to the study of the finiteness of the integral closure of
Noetherian integral rings.

The reader will note that the most delicate results of §7 will be of only slight use in the rest of Chapter IV, and even
in the later chapters.

<!-- original page 183 -->

### 7.1. Formal equidimensionality and formally catenary rings.

**Definition (7.1.1).**

<!-- label: IV.7.1.1 -->

*We say that a Noetherian local ring `A` is **formally equidimensional** if its completion `Â` is equidimensional
`(0, 16.1.4)`.*

**Proposition (7.1.2).**

<!-- label: IV.7.1.2 -->

*Let `A` be a Noetherian local ring and `p_i` `(1 ≤ i ≤ n)` its minimal prime ideals. In order that `A` be formally
equidimensional, it is necessary and sufficient that the `A/p_i` be so and that `A` be equidimensional (in other words,
that the `A/p_i` have the same dimension).*

Indeed, this results from the fact that for every prime ideal `p'` of `Â`, `p' ∩ A` contains one of the `p_i`, hence
`p'` contains one of the `p_i Â`, and `Â/p_i Â = (A/p_i) ⊗_A Â` is the completion of the local ring `A/p_i`
`(0_I, 7.3.3)`, hence has the same dimension. Every maximal chain of prime ideals of `Â` therefore identifies
canonically with a maximal chain of prime ideals of one of the `Â/p_i Â`, and conversely, whence the conclusion at once.

**Proposition (7.1.3).**

<!-- label: IV.7.1.3 -->

*Let `A`, `A'` be two Noetherian local rings, `𝔪` the maximal ideal of `A`, `φ : A → A'` a local homomorphism; suppose
that `A'` is a flat `A`-module, and that `A'` is equidimensional and catenary. Then:*

*(i) `A` is equidimensional and catenary.*

*(ii) Suppose further that `𝔪A'` is an ideal of definition of `A'`. Then, if `𝔞` is an ideal of `A`, in order that
`A'/𝔞A'` be equidimensional, it is necessary and sufficient that `A/𝔞` be so. In particular, for every prime ideal `p`
of `A`, `A'/pA'` is equidimensional.*

Let us first prove the second assertion of (ii). Set `X = Spec(A)`, `X' = Spec(A')`, `Y = V(p) = Spec(A/p)`,
`Y' = V(pA') = Spec(A'/pA')`; if `f : X' → X` is the morphism corresponding to `φ`, `Y'` is also the closed
sub-prescheme `f⁻¹(Y)` of `X'`. Since `𝔪A'` is an ideal of definition of `A'`, one has

```text
(7.1.3.1)                                dim(X) = dim(X')
```

by virtue of `(6.1.3)`; similarly `𝔪A'/pA'` is an ideal of definition of `A'/pA'` and `Y'` is flat over `Y` `(2.1.4)`,
hence `(6.1.3)`

```text
(7.1.3.2)                                dim(Y) = dim(Y').
```

Let `y` be the generic point of `Y`, `Y'_i` `(1 ≤ i ≤ r)` the irreducible components of `Y'`, `y'_i` the generic point
of `Y'_i` `(1 ≤ i ≤ r)`; one has `f(y'_i) = y` for every `i` `(2.3.4)`. On the other hand, `y'_i` is a maximal point of
the fibre `f⁻¹(y)` `(0_I, 2.1.8)`, hence `𝒪_{X', y'_i} ⊗_{𝒪_{X, y}} 𝒌(y) = 𝒪_{X', y'_i}/𝔪_y 𝒪_{X', y'_i}` is of
dimension `0`, in other words `𝔪_y 𝒪_{X', y'_i}` is an ideal of definition of `𝒪_{X', y'_i}`; one can again apply
`(6.1.3)`, which gives

```text
(7.1.3.3)                          dim(𝒪_{X', y'_i}) = dim(𝒪_{X, y})
```

that is to say `(5.1.2)`

```text
(7.1.3.4)                       codim(Y'_i, X') = codim(Y, X)
```

for every `i`. Since `A'` is equidimensional and catenary, one has, by virtue of `(0, 14.3.5)`

```text
(7.1.3.5)                       dim(X') = dim(Y'_i) + codim(Y'_i, X')
```

<!-- original page 184 -->

for every `i`; by virtue of `(7.1.3.1)`, `(7.1.3.2)` and `(7.1.3.4)` and of the inequality `dim(Y'_i) ≤ dim(Y')`, one
deduces

```text
(7.1.3.6)                          dim(X) ≤ dim(Y) + codim(Y, X)
```

hence the two sides of this inequality are equal by `(0, 14.2.2.2)`; moreover this equality entails

```text
(7.1.3.7)                          dim(Y'_i) = dim(Y') = dim(Y)
```

for every `i`, which proves the second assertion of (ii).

Let us now prove the first assertion of (ii). Let `p_j` `(1 ≤ j ≤ n)` be the prime ideals of `A` minimal among those
that contain `𝔞`, and let `p'_{jh}` be the prime ideals of `A'` minimal among those containing `p_j A'` `(1 ≤ h ≤ m_j)`;
one then knows `(2.3.4)` that the `p'_{jh}` `(1 ≤ j ≤ n, 1 ≤ h ≤ m_j` for every `j)` are also the prime ideals of `A'`
minimal among those containing `𝔞A'`. From what was seen above, for every `j`, the dimensions of the rings `A'/p'_{jh}`
`(1 ≤ h ≤ m_j)` are all equal, and so equal to `dim(A'/p_j A')`, itself equal to `dim(A/p_j)` by `(7.1.3.2)`. To say
that `A'/𝔞A'` is equidimensional means then that the dimensions of the `A/p_j` are all equal, that is to say that `A/𝔞`
is equidimensional.

Finally let us prove (i). Let `r'` be a prime ideal of `A'` minimal among those containing `𝔪A'`, and set
`A'' = A'_{r'}`; since `A''` is a flat `A'`-module, it is also a flat `A`-module; moreover `A''` is equidimensional and
catenary `(0, 16.1.4)`, and `𝔪A''` is an ideal of definition of `A''`. We may therefore reduce to the case where `𝔪A'`
is an ideal of definition of `A'`. If now `p` and `q ⊂ p` are two prime ideals of `A`, one can apply (ii) to `A/q` and
to `A'/qA'`, which is equidimensional and flat over `A/q`; if `Z = Spec(A/q)` and `Y = Spec(A/p)`, one has therefore
`dim(Z) = dim(Y) + codim(Y, Z)`; moreover one can apply `(7.1.3.6)`, which shows that `codim(Y, X) = dim X - dim Y`;
since `X` is equicodimensional, these relations show that it is biequidimensional by virtue of `(0, 14.3.3)`.

**Corollary (7.1.4).**

<!-- label: IV.7.1.4 -->

*Let `A` be a Noetherian local ring that is formally equidimensional. Then:*

*(i) `A` is equidimensional and catenary (in other words, biequidimensional).*

*(ii) Let `𝔞` be an ideal of `A`; in order that `A/𝔞` be equidimensional, it is necessary and sufficient that `A/𝔞` be
formally equidimensional. In particular, for every prime ideal `p` of `A`, `A/p` is formally equidimensional.*

If `𝔪` is the maximal ideal of `A`, `𝔪Â` is an ideal of definition of `Â`. By hypothesis `Â` is equidimensional, and one
knows on the other hand that it is catenary `(5.6.4)`; it then suffices to apply `(7.1.3)` to `A' = Â`.

**Corollary (7.1.5).**

<!-- label: IV.7.1.5 -->

*Let `A` be a Noetherian local ring such that there exists a finitely generated `A`-module `M` which is a Cohen-Macaulay
`A`-module and for which `Supp(M) = Spec(A)` (which will be the case for instance if `A` is a Cohen-Macaulay ring). Then
`A` is formally equidimensional, hence `(7.1.4)` in order that a quotient ring `B` of `A` be formally equidimensional,
it is necessary and sufficient that it be equidimensional.*

<!-- original page 185 -->

Indeed, `M̂ = M ⊗_A Â` is a Cohen-Macaulay `Â`-module `(0, 16.5.2)` with support equal to `Spec(Â)`; consequently
`(0, 16.5.4)`, `Â` is equidimensional.

**Remark (7.1.6).**

<!-- label: IV.7.1.6 -->

*One has seen `(6.3.8)` that under the hypotheses of `(7.1.5)`, for every quotient ring `B` of `A`, the fibres of the
canonical morphism `Spec(B̂) → Spec(B)` are Cohen-Macaulay preschemes; consequently (`(6.4.3)` and `(5.7.5)`), in order
that `B` have no embedded associated prime ideals, it is necessary and sufficient that the same be so of `B̂`.*

**Lemma (7.1.7).**

<!-- label: IV.7.1.7 -->

*Let `A` be a Noetherian local ring, `p_i` `(1 ≤ i ≤ r)` its minimal prime ideals. Suppose that each of the rings
`A/p_i` is formally equidimensional. Then, for every prime ideal `q` of `A` and every `i` such that `p_i ⊂ q`, the ring
`A_q/p_i A_q` is formally equidimensional.*

Since `A_q/p_i A_q` is the local ring of `A/p_i` at the prime ideal `q/p_i`, we may reduce to the case where `A` is
integral and formally equidimensional. Set `A' = Â`, and let `q'` be one of the prime ideals of `A'` minimal among those
containing `qA'`; if one sets `B = A_q`, `B' = A'_{q'}` is a flat `B`-module `(0_I, 6.3.2)`. Set `C = B̂`, `C' = B̂'`;
since `B'` is a flat `B`-module, one knows that `C'` is a flat `C`-module (Bourbaki, *Alg. comm.*, chap. III, §5, n° 4,
prop. 4). Since `A'` is catenary `(5.6.4)` and equidimensional by hypothesis, the same is so of `B' = A'_{q'}`
`(0, 16.1.4)`; moreover, since `A'` is isomorphic to a quotient of a regular ring by virtue of Cohen's theorem
`(0, 19.8.8)`, the same is so of `B'` `(0, 17.3.9)`; one concludes therefore from `(7.1.5)` that `C'` is
equidimensional. On the other hand, `C'` is catenary `(5.6.4)`, hence `C` is equidimensional by virtue of
`(7.1.3, (i))`.

**Theorem (7.1.8).**

<!-- label: IV.7.1.8 -->

*Let `A` be a Noetherian local ring. The following conditions are equivalent:*

*a) Every integral quotient ring of `A` is formally equidimensional.*

*b) The quotient rings of `A` by its minimal prime ideals are formally equidimensional.*

*c) Every local ring `B` which is an `A`-algebra essentially of finite type `(1.3.8)` and is equidimensional, is
formally equidimensional.*

It is trivial that c) implies a) and that a) implies b). On the other hand, since every prime ideal of `A` contains a
minimal prime ideal of `A`, b) entails a) by virtue of `(7.1.4, (ii))`. It remains to see that a) implies c).

It suffices to prove that the quotients of `B` by its minimal prime ideals are formally equidimensional `(7.1.2)`; since
every quotient ring of `B` is again an `A`-algebra essentially of finite type `(1.3.9)`, one may first suppose `B`
integral. If `q` is the inverse image in `A` of the maximal ideal of `B`, one knows that `B` is also an `A_q`-algebra
essentially of finite type `(1.3.10)`, and it results from a) and `(7.1.7)` that every integral quotient ring of `A_q`
is formally equidimensional; one may therefore suppose that the homomorphism `A → B` is a local homomorphism. The kernel
`r` of this homomorphism is then a prime ideal of `A`, and by virtue of a), every integral quotient ring of `A/r` is
formally equidimensional; since `B` is an `(A/r)`-algebra essentially of finite type, one sees that one may also suppose

<!-- original page 186 -->

that `A` is integral and is a subring of `B`. One knows `(1.3.11)` that `B` is a quotient of a local ring of the form
`C_p`, where `C = A[T_1, …, T_n]` is a polynomial algebra and `p` a prime ideal of `C` lying over the maximal ideal `𝔪`
of `A`. By virtue of `(7.1.7)`, it suffices to prove that `C_p` is formally equidimensional; in other words, one may
reduce to the case where `B = C_p`.

Set `A' = Â`, and `C' = A'[T_1, …, T_n] = C ⊗_A A'`; there is a unique prime ideal `p'` of `C'` lying over the maximal
ideal `𝔪A'` of `A'`, hence lying over `p`; set `B' = C'_{p'}`; the homomorphism `B → B'` is local and makes `B'` a flat
`B`-module. One knows then that `B̂'` is a flat `B̂`-module (Bourbaki, *Alg. comm.*, chap. III, §5, n° 4, prop. 4);
since `B̂'` is catenary `(5.6.4)`, it will suffice to prove that `B̂'` is equidimensional to deduce that `B̂` is so as
well `(7.1.3, (i))`, which will finish the proof.

Now, `A'` is a quotient of a regular ring by Cohen's theorem `(0, 19.8.8)`, hence the same is so of `B'` `(0, 17.3.9)`;
by virtue of `(7.1.5)`, to show that `B'` is formally equidimensional, it suffices to prove that `B'` is
*equidimensional*; and for this, it suffices to show that `C'` is equidimensional, since `C'` is a quotient of a regular
ring, hence catenary `(5.6.4)`. Now the minimal prime ideals of `C'` are the ideals `q'C'`, where `q'` runs through the
minimal prime ideals of `A'` `(5.5.3)`, and one has `C'/q'C' = (A'/q')[T_1, …, T_n]`. Since `A'` is equidimensional by
hypothesis (since `A` is integral), the same is so of `C'` by `(5.5.4)`. Q.E.D.

**Definition (7.1.9).**

<!-- label: IV.7.1.9 -->

*When the equivalent conditions of `(7.1.8)` are satisfied, one says that `A` is a **formally catenary** ring.*

For a Noetherian local ring, it therefore amounts to the same to say that it is formally equidimensional or that it is
formally catenary and equidimensional, by virtue of `(7.1.2)`.

**Proposition (7.1.10).**

<!-- label: IV.7.1.10 -->

*Every local ring `A` which is a quotient of a Cohen-Macaulay local ring is formally catenary.*

This results at once from `(7.1.8)` and from `(7.1.5)` applied to the integral quotient rings of `A`.

**Proposition (7.1.11).**

<!-- label: IV.7.1.11 -->

*(i) A formally catenary Noetherian local ring is universally catenary.*

*(ii) If `A` is a formally catenary Noetherian local ring, every local ring `B` which is an `A`-algebra essentially of
finite type is formally catenary.*

Assertion (ii) results at once from condition c) of `(7.1.8)` and from the fact that if a local ring `C` is a
`B`-algebra essentially of finite type, `C` is also an `A`-algebra essentially of finite type `(1.3.9)`. To prove (i),
note first that by virtue of condition b) of `(7.1.8)`, a formally catenary Noetherian local ring `A` is catenary, since
the quotients of `A` by its minimal prime ideals are so `(7.1.4)`. If now `E` is an `A`-algebra of finite type, it
results from the foregoing and from (ii) that every local ring of `E` at a prime ideal is catenary, hence that `E` is
catenary. Hence `A` is universally catenary.

<!-- original page 187 -->

**Remarks (7.1.12).**

<!-- label: IV.7.1.12 -->

*(i) It is not known whether, conversely, a universally catenary Noetherian local ring is always formally catenary.*

*(ii) A Noetherian local ring `A` of dimension `1` is necessarily equidimensional, its maximal ideal not being able to
be minimal (for in this case `A` would be of dimension `0`). Since `dim(Â) = 1`, this shows that `A` is even formally
equidimensional, and a fortiori formally catenary (hence universally catenary). On the other hand, the local ring of
dimension `2` defined in `(5.6.11)`, which is catenary but not universally catenary, is a fortiori not formally
catenary.*

**Corollary (7.1.13).**

<!-- label: IV.7.1.13 -->

*Let `Y` be a locally Noetherian irreducible prescheme of dimension `1`, `X` an irreducible prescheme, `f : X → Y` a
dominant morphism of finite type, `ξ`, `η` the generic points of `X` and `Y` respectively. Then, for every `y ∈ f(X)`,
the dimensions of the irreducible components of `f⁻¹(y)` are all equal to `deg.tr_{𝒌(η)} 𝒌(ξ)`.*

By hypothesis, `f⁻¹(η)` is irreducible with generic point `ξ` and of dimension `deg.tr_{𝒌(η)} 𝒌(ξ)` `(5.2.1)`. Since `Y`
is irreducible and of dimension `1`, one has `dim(𝒪_y) = 1` for every `y ≠ η`, and `𝒪_y` is universally catenary by
virtue of `(7.1.12, (ii))`. If `y ∈ f(X)` and if `z` is a generic point of an irreducible component `Z` of `f⁻¹(y)`, one
has therefore, by `(5.6.5)`

```text
                       dim(Z) = 1 + dim(f⁻¹(η)) - dim(𝒪_{X, z}).
```

But one has `dim(𝒪_{X, z}) ≤ dim(𝒪_y)` `(0, 16.3.9)`, and on the other hand, since `z` is not the generic point of `X`,
`dim(𝒪_{X, z}) > 0`; hence `dim(𝒪_{X, z}) = 1` and `dim(Z) = dim(f⁻¹(η))`.

### 7.2. Strictly formally catenary rings.

**Notations (7.2.1).**

<!-- label: IV.7.2.1 -->

*For a Noetherian integral ring `A`, we shall denote by `A^{(1)}` the intersection of the local rings `A_p`, where `p`
runs through the set of prime ideals of `A` of height `1` `(5.10.17)`. If `A` is an integral Noetherian local ring, we
shall denote by `A^{(ω)}` the intersection of the `A_p` where this time `p` runs through the set of all prime ideals of
`A` distinct from the maximal ideal.*

*We shall say that a Noetherian local ring `A` is **strictly equidimensional** if, for every prime ideal `p ∈ Ass(A)`,
one has `dim(A/p) = dim(A)`; it amounts to the same to say that `A` is equidimensional and without embedded associated
prime ideals.*

**Example (7.2.1.1).**

<!-- label: IV.7.2.1.1 -->

*Let `A` be a Noetherian local ring of dimension `1`. Then the following conditions are equivalent:*

*a) `A` is without embedded associated prime ideals.*

*a') `Â` is without embedded associated prime ideals.*

*b) `A` is strictly equidimensional.*

*b') `Â` is strictly equidimensional.*

*c) `A` is a Cohen-Macaulay ring.*

Indeed, a) means that the maximal ideal `𝔪` of `A` is not associated to `A`, hence the prime ideals associated to `A`
are the minimal ideals of `A`, all distinct from `𝔪`, and

<!-- original page 188 -->

for such an ideal `p`, one necessarily has `dim(A/p) = 1`; hence a) implies b). Conversely, b) implies that every prime
ideal `p ∈ Ass(A)` is distinct from `𝔪`, hence minimal, and consequently b) implies a). One already knows that a) and c)
are equivalent for a local ring of dimension `1` `(5.7.8)`. Since it amounts to the same to say that `A` is a
Cohen-Macaulay ring or that `Â` is a Cohen-Macaulay ring `(0, 16.5.2)`, and since one has `dim(Â) = 1`, one finally sees
that a') and b') are equivalent to c).

**Proposition (7.2.2).**

<!-- label: IV.7.2.2 -->

*Let `A` be an integral Noetherian local ring; set `A' = Â`, `X = Spec(A)`, `X' = Spec(A')` and denote by `f : X' → X`
the canonical morphism. Let `a` be the closed point of `X`, `j : X - {a} → X` the canonical injection. Let `ℱ` be a
coherent `𝒪_X`-Module, `ℱ' = f*(ℱ) = ℱ ⊗_{𝒪_X} 𝒪_{X'}`; then the following conditions are equivalent:*

*a) The `𝒪_X`-Module `j_*(ℱ | X - {a})` is coherent.*

*b) For every `x' ∈ Ass(ℱ')`, one has `dim(‾{x'}) ≥ 2`.*

Let `a'` be the closed point of `X'`, which is the unique point of the fibre `f⁻¹(a)`, and let `j' : X' - {a'} → X'` be
the canonical injection. Since the morphism `f` is faithfully flat and quasi-compact, it is equivalent to say that
`j_*(ℱ | X - {a})` is coherent or that `j'_*(ℱ' | X' - {a'})` is coherent `(5.9.5)`. On the other hand, since `A'` is
isomorphic to the quotient of a regular local ring by Cohen's theorem `(0, 19.8.8)`, it results from `(5.11.4)` that
condition b) of the statement is equivalent to the fact that `j'_*(ℱ' | X' - {a'})` is coherent. Whence the proposition.

Instead of applying `(5.11.4)` using Cohen's theorem, which (by `(5.11.2)`) implicitly appeals to the cohomological
results of chap. III, one may also use the fact that `A'` is universally catenary `(5.6.4)` and universally Japanese by
virtue of `(7.6.5)` (the proof of this last result not using `(7.2.2)`).

**Proposition (7.2.3).**

<!-- label: IV.7.2.3 -->

*Let `A` be an integral Noetherian local ring. With the notations of `(7.2.2)`, the following conditions are
equivalent:*

*a) `A^{(1)}` is a finite `A`-algebra.*

*b) For every closed part `T` of `X` of codimension `≥ 2`, if one denotes by `i : X - T → X` the canonical injection,
`i_*(𝒪_{X - T})` is a coherent `𝒪_X`-Module.*

*c) For every `x' ∈ Ass(𝒪_{X'})` and every closed part `T` of `X` of codimension `≥ 2`, one has
`codim(f⁻¹(T) ∩ ‾{x'}, ‾{x'}) ≥ 2`.*

Set `Z = Z^{(2)}(X)` `(5.10.13)` and `Z' = f⁻¹(Z)`, which are parts stable under specialization; conditions a) and b)
are equivalent respectively to the following properties: `a_1`) `ℋ⁰_{X/Z}(𝒪_X)` is coherent; `b_1`) `ℋ⁰_{X/T}(𝒪_X)` is
coherent for every closed part `T` of `X` of codimension `≥ 2`. Taking `(5.9.5)` into account, these two latter
properties are respectively equivalent to: `a'_1`) `ℋ⁰_{X'/Z'}(𝒪_{X'})` is coherent; `b'_1`) putting `T' = f⁻¹(T)`,
`ℋ⁰_{X'/T'}(𝒪_{X'})` is coherent for every closed part `T` of `X` of codimension `≥ 2`. Now, every point of
`Ass(𝒪_{X'})` projects in `X` to the generic point of `X` since `f` is a flat morphism `(3.3.2)`; since by definition
this point does not belong to `Z`, one sees that `Ass(𝒪_{X'})` does not meet `Z'`; the equivalence of `a'_1`) and
`b'_1`) therefore results from `(5.11.5)`, since `A'` is isomorphic to a quotient of a regular ring by virtue of Cohen's
theorem `(0, 19.8.8)` (or also

<!-- original page 189 -->

because `A'` is universally Japanese `(7.6.5)`). For this reason, conditions `b'_1`) and c) are also equivalent by
virtue of `(5.11.4)`.

**Proposition (7.2.4).**

<!-- label: IV.7.2.4 -->

*Let `A` be a Noetherian local ring and set `X = Spec(A)`. The following conditions are equivalent:*

*a) For every integral quotient ring `B` of `A`, the ring `B^{(1)}` is a finite `B`-algebra.*

*b) For every coherent `𝒪_X`-Module `ℱ` and every part `Z`, stable under specialization, such that for every
`x ∈ Ass(ℱ) ∩ (X - Z)` one has `codim(‾{x} ∩ Z, ‾{x}) ≥ 2`, the `𝒪_X`-Module `ℋ⁰_{X/Z}(ℱ)` is coherent.*

*c) For every closed part `T` of `X` and every coherent `𝒪_U`-Module `𝒢` (where `U = X - T`) such that, for every
`x ∈ Ass(𝒢)`, one has `codim(‾{x} ∩ T, ‾{x}) ≥ 2`, `i_*(𝒢)` (where `i : U → X` is the canonical injection) is a coherent
`𝒪_X`-Module.*

*d) For every integral quotient ring `B` of `A` and every ideal `𝔍` of height `≥ 2` in `B`, the ring `⋂_{p ⊉ 𝔍} B_p` is
a finite `B`-algebra.*

*e) For every integral quotient ring `B` of `A` and every local ring `C = B_q` at a prime ideal `q` of `B`, such that
`dim(C) ≥ 2`, the ring `C^{(ω)}` is a finite `C`-algebra (or, what comes to the same, if `Y = Spec(C)` and if `U` is the
complement in `Y` of the closed point of `C` and `j : U → Y` the canonical injection, `j_*(𝒪_U)` is a coherent
`𝒪_Y`-Module).*

*f) For every integral quotient ring `B` of `A`, every local ring `C = B_q` at a prime ideal `q` of `B` such that
`dim(C) ≥ 2`, and for every ideal `r ∈ Ass(Ĉ)`, one has `dim(Ĉ/r) ≥ 2`.*

One already knows `(5.11.6)` that a) and b) are equivalent, as are c) and d), and that a) entails d). The equivalence of
a) and d) in the present case results from `(7.2.3)` applied to an integral quotient ring `B` of `A`, condition d) being
an equivalent formulation of condition `(7.2.3, b))` by virtue of `(5.9.3.1)`. The equivalence of e) and f) is a
consequence of `(7.2.2)` applied to the coherent `𝒪_Y`-Module `𝒪_Y` itself. One has already remarked `(5.11.7, (ii))`
that if `A` satisfies a), the same is so of every finite `A`-algebra and of every ring of fractions of `A`. Condition a)
for `A` therefore entails (with the notations of e)) that the ring `C` satisfies a), hence also c); but since `C` is
integral and `dim(C) ≥ 2`, one may apply to `C` the condition c) taking for `T` the closed point of `Y = Spec(C)`; this
proves that a) entails e). It remains to prove that e) entails a); one may evidently reduce to the case where `A` is
integral and `B = A`, and the question is then to show that condition e) entails condition `(7.2.3, c))`. With the
notations of `(7.2.3, c))`, let us therefore consider a point `y' ∈ f⁻¹(T) ∩ ‾{x'}`, and set `y = f(y')` and
`C = 𝒪_{X, y}`; since `y ∈ T`, one has by hypothesis `dim(C) ≥ 2`, and consequently (with the notations of e)),
`j_*(𝒪_U)` is a coherent `𝒪_Y`-Module. Now, set `Y' = X' ×_X Y`; the morphism `f : X' → X` being flat, the same is so of
`g = f_{(Y)} : Y' → Y`. Moreover the space underlying `Y'` identifies with `f⁻¹(Y)` `(I, 3.6.5)`, and since `A` is
integral and `f` flat, `Ass(𝒪_{X'})` is contained in the fibre of the generic point of `X` `(3.3.2)`; the latter being
contained in `Y`, one has `x' ∈ Y'`. Let `U' = g⁻¹(U)`, and let `j'` be the canonical injection `U' → Y'`; since
`j_*(𝒪_U)` is a coherent `𝒪_Y`-Module and `g` is flat, it results from `(5.9.4)` that `j'_*(𝒪_{U'})` is a coherent
`𝒪_{Y'}`-Module. Now one has `x' ∈ Ass(𝒪_{U'})`, hence one concludes from `(5.10.10)` that one has, in `Y'`,

<!-- original page 190 -->

`codim(‾{y'} ∩ ‾{x'}, ‾{x'}) ≥ 2`. Since `y'` is arbitrary in `f⁻¹(T) ∩ ‾{x'}`, one has indeed
`codim(f⁻¹(T) ∩ ‾{x'}, ‾{x'}) ≥ 2` in `X'`. Q.E.D.

**Theorem (7.2.5).**

<!-- label: IV.7.2.5 -->

*Let `A` be a Noetherian local ring. The following conditions are equivalent:*

*a) For every integral quotient ring `B` of `A`, the completion `B̂` is strictly equidimensional `(7.2.1)`.*

*b) `A` is formally catenary `(7.1.9)` and the fibres of the canonical morphism `Spec(Â) → Spec(A)` satisfy `(S_1)` (in
other words, have no embedded associated prime cycle).*

*c) `A` is universally catenary `(5.6.2)` and for every integral quotient ring `B` of `A`, the ring `B^{(1)}` is a
finite `B`-algebra (cf. `(7.2.4)`).*

*d) `A` is universally catenary and for every integral quotient ring `B` of `A` and every local ring `C = B_q` at a
prime ideal `q` of `B`, such that `dim(C) ≥ 2`, the ring `C^{(ω)}` is a finite `C`-algebra.*

*e) `A` is universally catenary and for every integral quotient ring `B` of `A` and every local ring `C = B_q` at a
prime ideal `q` of `B`, such that `dim(C) ≥ 2`, the completed ring `Ĉ` is such that `Spec(Ĉ)` has no associated prime
cycle of dimension `1`.*

*Moreover, when these conditions are satisfied, then, for every quotient ring `B` of `A` which is strictly
equidimensional, the completion `B̂` is strictly equidimensional.*

The equivalence of c), d) and e) was proved in `(7.2.4)`. To show that a) and b) are equivalent, recall `(7.1.9)` that
to say that `A` is formally catenary means that for every integral quotient ring `B` of `A`, `B̂` is equidimensional. On
the other hand, every fibre of the morphism `Spec(Â) → Spec(A)` at a point `x ∈ Spec(A)` is the fibre of the morphism
`Spec(B̂) → Spec(B)` at the generic point `x` of `Spec(B)`, where `B = A/𝔧_x`; to say that this fibre is without
embedded associated prime cycle amounts to saying that `B̂` has no embedded associated prime ideals, by virtue of
`(3.3.3)`; this proves the equivalence of a) and b). The same reasoning shows that if a) is satisfied, then, for every
quotient ring `B` of `A` which is without embedded associated prime ideals, the completion `B̂` is also without embedded
associated prime ideals; on the other hand, the hypothesis that `A` is formally catenary entails that if `B` is
equidimensional, the same is so of `B̂` `(7.1.8)`; this establishes the last assertion of the theorem.

Let us now show that a) implies c). Condition a) implies that `A` is universally catenary `(7.1.11)`; let us show on the
other hand that for every integral quotient ring `B` of `A`, `B^{(1)}` is then a finite `B`-algebra. Taking into account
`(7.2.3)` applied to `B`, the question is to show that if `X = Spec(B)`, if `T` is a closed part of `X` of codimension
`≥ 2`, `X' = Spec(B̂)`, and `g : X' → X` the canonical morphism, then one has, for every `x' ∈ Ass(𝒪_{X'})`,
`codim(g⁻¹(T) ∩ ‾{x'}, ‾{x'}) ≥ 2`. But by hypothesis `X'` has no embedded associated prime cycle, hence
`inf(codim(g⁻¹(T) ∩ ‾{x'}, ‾{x'}))` when `x'` runs through `Ass(𝒪_{X'})` is none other than `codim(g⁻¹(T), X')`. Now,
since `g` is a faithfully flat morphism, one has `(6.1.4)`

```text
                          codim(g⁻¹(T), X') = codim(T, X) ≥ 2.
```

<!-- original page 191 -->

It remains to prove that c) entails a). We reason by induction on `n = dim(A)`, the theorem being trivial for `n = 0`;
one may moreover reduce to the case where `A = B` is integral. Let us proceed in two stages, `n` being `≥ 1`.

I) *Suppose first that `A` satisfies `(S_2)`.* — Set `X = Spec(A)`, `A' = Â`, `X' = Spec(A')` and let `u : X' → X` be
the canonical morphism; the question is to show that for every element `x' ∈ Ass(𝒪_{X'})`, one has `dim(‾{x'}) = n`. Let
`f ≠ 0` be an element of the maximal ideal of `A`, and set `C = A/fA`; one knows `(5.7.6)` that `A/fA` satisfies
`(S_1)`; moreover, since the prime ideals of `A` minimal among those containing `f` are of height `1` by virtue of the
Hauptidealsatz, and since `C` is catenary, `C = A/fA` is strictly equidimensional and `dim(C) = n - 1`. One has
`Ĉ = C ⊗_A Â = A'/fA'`, and `f` is `A'`-regular by flatness `(0_I, 6.3.4)`; if one sets `Y' = V(fA') = Spec(Ĉ)`, then,
for every maximal point `y'` of `Y' ∩ ‾{x'}`, one has `y' ∈ Ass(𝒪_{Y'})` by virtue of `(3.4.3)`; on the other hand, one
has `y' ≠ x'` since `u(x')` is the generic point of `X` `(3.3.2)` and one has `u(y') ∈ V(fA)`. One concludes from
`(5.1.8)` that

```text
(7.2.5.1)                          dim(‾{y'}) = dim(‾{x'}) - 1.
```

But the quotient ring `C = A/fA` also satisfies hypothesis c) of the statement (`(5.6.1)` and `(5.11.7, (ii))`); by
virtue of the induction hypothesis, one has `dim(‾{y'}) = dim(C) = n - 1`; the conclusion `dim(‾{x'}) = n` therefore
results in this case from `(7.2.5.1)`.

II) *General case.* — Since by hypothesis the ring `A^{(1)}` is a finite `A`-algebra, it satisfies `(S_2)` by virtue of
`(5.10.17, (i))`; the same is so of each of its local rings `(A^{(1)})_𝔫` at a maximal ideal `𝔫`, and moreover, since
`A` is universally catenary, the rings `(A^{(1)})_𝔫` (which are finite in number) are all of dimension `n` `(5.6.10)`;
moreover, these rings satisfy hypothesis c) of the statement (`(5.6.1)` and `(5.11.7, (ii))`). One knows that the
completion of `A^{(1)}`, equal to `Â ⊗_A A^{(1)}`, is the direct product of the completions of the local rings
`(A^{(1)})_𝔫`. Set `X_1 = Spec(A^{(1)})`, `X'_1 = Spec((A^{(1)})^^) = X' ×_X X_1`; for every `x'_1 ∈ Ass(𝒪_{X'_1})`, it
results from the foregoing and from case I) that one has `dim(‾{x'_1}) = n`. Let `u_1 = u_{(X_1)} : X'_1 → X_1` be the
canonical morphism; since `A` and `A^{(1)}` have the same field of fractions, the inverse image of the generic point `x`
of `X` by the projection `X_1 → X` reduces to the generic point `x_1` of `X_1`, the inverse image by the projection
`X'_1 → X'` of the fibre `u⁻¹(x)` is the fibre `u_1⁻¹(x_1)` and this projection induces an isomorphism of the prescheme
`u_1⁻¹(x_1)` onto `u⁻¹(x)`. This said, the points of `Ass(𝒪_{X'})` (resp. `Ass(𝒪_{X'_1})`) are the generic points of the
associated prime cycles of `u⁻¹(x)` (resp. `u_1⁻¹(x_1)`) `(3.3.1)`. For every `x' ∈ Ass(𝒪_{X'})`, there is therefore an
`x'_1 ∈ Ass(𝒪_{X'_1})` lying over `x'`, and if `Z'` (resp. `Z'_1`) is the reduced closed sub-prescheme of `X'` (resp.
`X'_1`) having `‾{x'}` (resp. `‾{x'_1}`) for underlying space, the projection `Z'_1 → Z'` is a finite and surjective
morphism; one concludes `(5.4.2)` that `dim(‾{x'}) = dim(‾{x'_1}) = n`. Q.E.D.

**Definition (7.2.6).**

<!-- label: IV.7.2.6 -->

*When a Noetherian local ring `A` satisfies the equivalent conditions of `(7.2.5)`, one says that it is **strictly
formally catenary**.*

<!-- original page 192 -->

**Corollary (7.2.7).**

<!-- label: IV.7.2.7 -->

*Let `A` be a Noetherian local ring such that there exists a finitely generated `A`-module `M` which is a Cohen-Macaulay
`A`-module and for which `Supp(M) = Spec(A)`; then `A` is strictly formally catenary.*

Indeed, `A` is formally catenary (`(7.1.5)` and `(7.1.9)`), and on the other hand the fibres of the canonical morphism
`Spec(Â) → Spec(A)` are Cohen-Macaulay preschemes `(6.3.8)`, hence a fortiori satisfy `(S_1)`.

**Corollary (7.2.8).**

<!-- label: IV.7.2.8 -->

*If `A` is a strictly formally catenary Noetherian local ring, every local ring `B` which is an `A`-algebra essentially
of finite type is strictly formally catenary.*

Indeed, `B` is formally catenary `(7.1.11)` and it results from `(7.4.4)` [^1] that the fibres of `Spec(B̂) → Spec(B)`
satisfy `(S_1)`, whence the conclusion.

**Corollary (7.2.9).**

<!-- label: IV.7.2.9 -->

*Every Noetherian local ring of dimension `1` is strictly formally catenary.*

Indeed, every integral quotient ring `B` of such a ring `A` is of dimension `0` or `1`, hence its completion is strictly
equidimensional `(7.2.1.1)`.

**Remarks (7.2.10).**

<!-- label: IV.7.2.10 -->

*(i) It results from `(7.2.7)` and `(7.2.8)` that every quotient ring of a Cohen-Macaulay local ring is strictly
formally catenary.*

*A Noetherian local ring of dimension `2` satisfying `(S_2)` is strictly formally catenary, since it is a Cohen-Macaulay
ring. Recall on the other hand that there are integral Noetherian local rings of dimension `2` which are not universally
catenary, nor a fortiori strictly formally catenary `(5.6.11)`.*

*(ii) It is not known whether a formally catenary ring `(7.1.9)` is strictly formally catenary; this is due to the fact
that one does not know whether, for an integral Noetherian local ring `B`, `B̂` is without embedded associated prime
ideals `(6.4.3)`. We are likewise unaware whether, in the equivalent conditions c), d), e) of `(7.2.5)`, one can replace
the hypothesis that `A` is universally catenary by the hypothesis that `A` is catenary; one can show that this is so
when `A` is Henselian `(18.9.6)`.*

### 7.3. Formal fibres of Noetherian local rings.

**(7.3.1)** We shall consider in this number and the two following ones properties `𝐏(Z, k)` of the following form:

«`Z` is a locally Noetherian prescheme over a field `k`, and for every `z ∈ Z`, one has `𝐐(𝒪_z, k)`»

where `𝐐(A, k)` is a property of a Noetherian local ring `A` which is a `k`-algebra; one supposes that if `k'` is a
field isomorphic to `k`, and if `A'` is a Noetherian local ring which is a `k'`-algebra di-isomorphic to `A`, the
properties `𝐐(A, k)` and `𝐐(A', k')` are equivalent.

<!-- original page 193 -->

If `X`, `Y` are two locally Noetherian preschemes, we shall say that a morphism `f : X → Y` is a **𝐏-morphism** if:

1° `f` is *flat*;

2° for every `y ∈ Y`, the property `𝐏(f⁻¹(y), 𝒌(y))` is true.

**Lemma (7.3.2).**

<!-- label: IV.7.3.2 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism. The following properties are equivalent:*

*a) `f` is a 𝐏-morphism.*

*b) For every `x ∈ X`, if one sets `y = f(x)`, then `𝒪_x` is a flat `𝒪_y`-module and the property
`𝐐(𝒪_x ⊗_{𝒪_y} 𝒌(y), 𝒌(y))` is true.*

*c) For every `x ∈ X`, if one sets `y = f(x)`, the morphism `Spec(𝒪_x) → Spec(𝒪_y)` corresponding to the homomorphism
`𝒪_y → 𝒪_x` is a 𝐏-morphism.*

*c') For every closed point `x ∈ X`, the morphism `Spec(𝒪_x) → Spec(𝒪_y)` is a 𝐏-morphism.*

The equivalence of a) and b) results indeed from the definitions; the same is so of the equivalence of b) and c), taking
into account `(I, 2.4.2)`; finally the equivalence of b) and c') results from the fact that for every `x ∈ X`, `‾{x}`
contains a closed point `(5.1.11)`.

**Corollary (7.3.3).**

<!-- label: IV.7.3.3 -->

*Let `A`, `B` be two Noetherian rings, `φ : A → B` a homomorphism such that the corresponding morphism
`Spec(B) → Spec(A)` is a 𝐏-morphism. Then, for every multiplicative part `S` of `A`, the morphism
`Spec(S⁻¹B) → Spec(S⁻¹A)` is a 𝐏-morphism.*

This results at once from `(7.3.2)` and from `(I, 1.6.2)`.

**(7.3.4)** We shall always suppose in what follows that the property `𝐐` is such that the three following conditions
are satisfied:

`(P_I)` (*transitivity*). — If `f : X → Y` is a regular morphism `(6.8.1)` and `g : Y → Z` a 𝐏-morphism, then `g ∘ f` is
a 𝐏-morphism.

`(P_II)` (*descent*). — If `f : X → Y` and `g : Y → Z` are morphisms of locally Noetherian preschemes such that `f` is
faithfully flat and `g ∘ f` is a 𝐏-morphism, then `g` is a 𝐏-morphism.

`(P_III)`. — For every field `k`, the property `𝐏(Spec(k), k)` is true.

**Remarks (7.3.5).**

<!-- label: IV.7.3.5 -->

*(i) Conditions `(P_I)` and `(P_III)` entail that every regular morphism is a 𝐏-morphism.*

*(ii) Note that the hypotheses of `(P_I)` (resp. `(P_II)`) entail that `h = g ∘ f` is flat (resp. `g` is flat)
`(2.2.13)`; the hypotheses of `(P_I)` or of `(P_II)` moreover entail that for every `z ∈ Z`, `f_z : h⁻¹(z) → g⁻¹(z)` is
flat `(2.1.4)`; since, for every `y ∈ g⁻¹(z)`, `f⁻¹_z(y)` is isomorphic to `f⁻¹(y)` `(I, 3.6.4)`, this shows that it
suffices, to verify conditions `(P_I)` and `(P_II)`, to do so only when `Z` is the *spectrum of a field*.*

*(iii) In certain cases, the property `𝐐` will be such that the following condition is satisfied:*

`(P'_I)`. — *If `f : X → Y` and `g : Y → Z` are two 𝐏-morphisms, then `g ∘ f` is a 𝐏-morphism.*

<!-- original page 194 -->

**(7.3.6)** We shall say that the property `𝐏` is *geometric* if it satisfies (besides `(P_I)`, `(P_II)` and `(P_III)`)
the condition:

`(P_IV)` (*finite-type extension of the base field*). — If `𝐏(Z, k)` is true, then, for every extension `k'` of finite
type of `k`, `𝐏(Z ⊗_k k', k')` is true.

**Lemma (7.3.7).**

<!-- label: IV.7.3.7 -->

*Let `f : X → Y` be a 𝐏-morphism of locally Noetherian preschemes, `g : Y' → Y` a locally finite-type morphism. Then, if
`𝐏` satisfies condition `(P_IV)`, the morphism `f' = f_{(Y')} : X ×_Y Y' → Y'` is a 𝐏-morphism.*

Indeed, for every `y' ∈ Y'`, if one sets `y = g(y')`, `𝒌(y')` is an extension of finite type of `𝒌(y)` `(I, 6.4.11)` and
`f'⁻¹(y') = f⁻¹(y) ⊗_{𝒌(y)} 𝒌(y')` `(I, 3.6.4)`; it then suffices to apply `(P_IV)`.

**Examples (7.3.8).**

<!-- label: IV.7.3.8 -->

*The following properties `𝐏(Z, k)` satisfy conditions `(P_I)`, `(P_II)` and `(P_III)`:*

*(i) (also denoted `(i_n)`) `Z` is of codepth `≤ n`.*

*(ii) `Z` is a Cohen-Macaulay prescheme.*

*(iii) (also denoted `(iii_n)`) `Z` satisfies `(S_n)`.*

*(iv) `Z` is regular.*

*(v) (also denoted `(v_n)`) `Z` satisfies `(R_n)`.*

*(vi) `Z` is reduced.*

*(vii) `Z` is normal.*

For properties (ii) to (vii), this results from `(6.6.1)`, which in fact proves the stronger condition `(P'_I)`. For
(i), property `(P_II)` results from `(6.6.2)`; property `(P_I)` results, by the same reasoning as in `(6.6.1, (i))`,
from `(6.3.2)` and from the fact that a regular prescheme is of codepth `0`.

In addition, it results from `(6.7.8)` that properties (i), (ii) and (iii) are *geometric*; by virtue of `(6.7.8)`, the
same is so of the following:

*(iv') `Z` is geometrically regular.*

*(v') (also denoted `(v'_n)`) `Z` has the property `(R_n)` geometrically.*

*(vi') `Z` is geometrically reduced.*

*(vii') `Z` is geometrically normal.*

**Remarks (7.3.9).**

<!-- label: IV.7.3.9 -->

*(i) Each of the properties (iv'), (v'\_n), (vi'), (vii') entails respectively the corresponding property (iv), (v_n),
(vi), (vii). Property (iv) implies all the properties (i) to (vii), and property (iv') implies all the properties listed
in `(7.3.8)`. Recall also that `(i_0)` is equivalent to (ii); the conjunction of `(iii_1)` and `(v_0)` (resp. of
`(iii_1)` and `(v'_0)`) is equivalent to (vi) (resp. (vi')) `(5.8.5)`; finally the conjunction of `(iii_2)` and `(v_1)`
(resp. `(iii_2)` and `(v'_1)`) is equivalent to (vii) (resp. (vii')) `(5.8.6)`.*

*(ii) In all the examples of `(7.3.8)`, the property `𝐐(𝒪_z, k)` which serves to define `𝐏` is such that, for every
generization `z'` of `z` in `Z`, `𝐐(𝒪_z, k)` entails `𝐐(𝒪_{z'}, k)`: by virtue of `(2.3.4)`, it suffices to verify it
for the properties (i) to (vii) (and even (i) to (v) by remark `(7.3.9, (i))`): now this is included in the definition
for (iii) and (v) (`(5.7.2)` and `(5.8.2)`), it results from `(6.3.9)` for (i), and finally from `(0, 16.5.10)` and
`(17.3.2)` for (ii) and (iv).*

<!-- original page 195 -->

**(7.3.10)** We shall say that a property `𝐏(Z, k)` is *of the first type* if the property `𝐐(A, k)` which serves to
define `𝐏` is a property `𝐑(A)` not involving `k` and true when `A` is a *field*; we shall say that `𝐏(Z, k)` is *of the
second type* if the property `𝐐(A, k)` is of the form

«for every extension `k'` of finite type of `k` and every point `z'` of `Spec(A ⊗_k k')` lying over the closed point of
`Spec(A)`, one has `𝐑(𝒪_{z'})`»

where `𝐑(A)` is again assumed to be true when `A` is a *field*. It is clear that in the examples of `(7.3.8)`,
properties (i) to (vii) are of the first type, properties (iv') to (vii') of the second type.

This being so, if one resumes the reasoning of `(6.6.1)` and `(6.8.3)`, one finds that when `𝐏` is of the first or
second type for a property `𝐑(A)`, *conditions `(P_I)` and `(P_II)` are consequences of the following conditions on
`𝐑`:*

`(R_I)` Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a regular morphism; then, for every `x ∈ X`, the
property `𝐑(𝒪_{f(x)})` implies the property `𝐑(𝒪_x)`.

`(R_II)` Let `φ : A → B` be a local homomorphism of local Noetherian rings making `B` an `A`-module *flat*; then `𝐑(B)`
implies `𝐑(A)`.

Moreover, property `(P_III)` results by hypothesis from the fact that `𝐑(k)` is true for every field `k`; finally, when
`𝐏` is of the second type, condition `(P_IV)` is a consequence of the definition of `𝐏` and of the transitivity of
extensions of finite type.

**Remark (7.3.11).**

<!-- label: IV.7.3.11 -->

*We leave to the reader the task of formulating the property `𝐑` corresponding to each of the examples of `(7.3.8)`, and
of verifying conditions `(R_I)` and `(R_II)` in each case, using the results of §6. In fact, except for example (i) of
`(7.3.8)`, the property `𝐑` satisfies in the other cases the following condition:*

`(R'_I)` Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a 𝐏-morphism (for the property `𝐏` of the first
or second type defined from `𝐑`); then, for every `x ∈ X`, the property `𝐑(𝒪_{f(x)})` implies the property `𝐑(𝒪_x)`.

The reasonings of `(6.6.1)` and `(6.8.3)` prove that when `𝐑` satisfies conditions `(R'_I)` and `(R_II)`, then `𝐏`
satisfies conditions `(P'_I)` `(7.3.4, (iii))` and `(P_II)`.

**Proposition (7.3.12).**

<!-- label: IV.7.3.12 -->

*Let `𝐏` be a property of the first or second type defined from a property `𝐑` satisfying conditions `(R_I)` and
`(R_II)` (resp. `(R'_I)` and `(R_II)`). If for every locally Noetherian prescheme `X`, `U_𝐑(X)` designates the set of
`x ∈ X` such that `𝐑(𝒪_x)` is true, then, for every regular morphism (resp. every 𝐏-morphism) `f : X → Y` of locally
Noetherian preschemes, one has*

```text
(7.3.12.1)                          U_𝐑(X) = f⁻¹(U_𝐑(Y)).
```

It is an immediate consequence of the definitions.

**(7.3.13)** Given a semi-local Noetherian ring `A`, we shall call **formal fibres** of `A` the fibres of the canonical
morphism `f : Spec(Â) → Spec(A)`; for every prime ideal `p` of `A`, the formal fibre at `p` is therefore the scheme
`Spec(Â ⊗_A 𝒌(p))`; since the completion of the local ring `A/p` is `Â/pÂ = (A/p) ⊗_A Â`, one sees that the formal fibre
of `A` at `p` is also *the formal fibre of `A/p` at the generic point `(0)` of `Spec(A/p)`*.

<!-- original page 196 -->

The property `𝐏` being defined as in `(7.3.1)`, we shall say that *the formal fibres of `A` have the property `𝐏`*, or
that *`A` is a `𝐏`-ring*, if, for every `x ∈ Spec(A)`, `𝐏(f⁻¹(x), 𝒌(x))` is true. Since `f` is flat, it amounts to the
same to say that `f` is a 𝐏-morphism.

**Proposition (7.3.14).**

<!-- label: IV.7.3.14 -->

*Let `A` be a semi-local Noetherian ring, `𝔪_i` `(1 ≤ i ≤ r)` its maximal ideals, and set `A_i = A_{𝔪_i}`; in order that
`A` be a `𝐏`-ring, it is necessary and sufficient that each of the `A_i` be so.*

Indeed, `Â` is the direct product of the `Â_i`, hence the formal fibre of `A` at a point `x ∈ Spec(A)` is the sum of the
formal fibres at `x` of those of the `A_i` such that `x ∈ Spec(A_i)`.

**Proposition (7.3.15).**

<!-- label: IV.7.3.15 -->

*Let `A` be a semi-local Noetherian ring.*

*(i) If `A` is a `𝐏`-ring, every quotient ring of `A` is a `𝐏`-ring.*

*(ii) If moreover `𝐏` satisfies condition `(P_IV)` `(7.3.6)`, then every finite `A`-algebra is a `𝐏`-ring.*

For every ideal `𝔞` of `A`, `Â ⊗_A (A/𝔞)` is the completion of `A/𝔞`, and the formal fibres of `A/𝔞` are the formal
fibres of `A` at the points of `V(𝔞)`, whence (i). On the other hand, if `B` is a finite `A`-algebra, hence a semi-local
ring, one has `B̂ = B ⊗_A Â`, and (ii) follows from `(7.3.7)`.

**Proposition (7.3.16).**

<!-- label: IV.7.3.16 -->

*Suppose that the property `𝐏` is of the first (resp. second) type, defined from a property `𝐑` `(7.3.10)`. When `𝐏` is
of the second type, suppose moreover that the relation*

«for every finite extension `k'` of `k`, and every `z' ∈ Z ⊗_k k'`, `𝐑(𝒪_{z'})` is true»

*entails `𝐏(Z, k)` (which is verified for examples (iv') to (vii') of `(7.3.8)`, by virtue of `(6.7.7)` and `(4.6.1)`).*

*Let `A` be a semi-local Noetherian ring. If the property `𝐑` satisfies `(R_I)` and `(R_II)`, the following properties
are equivalent:*

*a) `A` is a `𝐏`-ring.*

*b) For every integral quotient ring `B` of `A` (resp. every integral finite `A`-algebra `B`) and every prime ideal `q`
of `B̂` whose inverse image in `B` is `0`, `𝐑(B̂_q)` is true.*

*If moreover `𝐑` satisfies condition `(R'_I)`, properties a) and b) are also equivalent to:*

*c) For every integral quotient ring `B` of `A` (resp. every integral finite `A`-algebra `B`), if one sets
`Y = Spec(B)`, `Y' = Spec(B̂)`, and if `g : Y' → Y` is the canonical morphism, one has (with the notations of
`(7.3.12)`)*

```text
(7.3.16.1)                            U_𝐑(Y') = g⁻¹(U_𝐑(Y)).
```

The equivalence of a) and b) is immediate when `𝐏` is of the first type: indeed, for every prime ideal `p` of `A`, one
has seen that the formal fibre of `B = A/p` at the generic point `(0)` of `Spec(B)` is none other than the formal fibre
of `A` at the point `p ∈ Spec(A)` `(7.3.13)`.

When `𝐏` is of the second type, the equivalence of a) and b) results from the following more general lemma:

**Lemma (7.3.16.2).**

<!-- label: IV.7.3.16.2 -->

*Let `A`, `A'` be two rings, `φ : A → A'` a homomorphism, `f : Spec(A') → Spec(A)` the corresponding morphism. In order
that for every `x ∈ Spec(A)`, every*

<!-- original page 197 -->

*finite extension `k` of `𝒌(x)` and every point `z` of `f⁻¹(x) ⊗_{𝒌(x)} k = Z`, the property `𝐑(𝒪_{Z, z})` be true, it
is necessary and sufficient that the following condition be satisfied: for every finite integral `A`-algebra `B`, if
`g : Spec(A' ⊗_A B) → Spec(B)` is the morphism deduced from `f` by extension to `B` of the base ring, and if
`T = g⁻¹(ξ)` is the fibre of the generic point `ξ` of `Spec(B)`, then, for every `t ∈ T`, `𝐑(𝒪_{T, t})` is true.*

The condition is trivially necessary since if `x` is the point of `Spec(A)` over which `ξ` lies, `𝒌(ξ)` is a finite
extension of `𝒌(x)`. Conversely, consider an arbitrary point `x ∈ Spec(A)` and let `k` be a finite extension of `𝒌(x)`.
Setting `p = j_x`, `𝒌(x)` is the field of fractions of `A/p`, and there is a base `k` of `k` over `𝒌(x)` formed of
elements integral over `A/p`; if `B` is the subring of `k` generated by these elements, `B` is an integral finite
`A`-algebra and `k` is the field `𝒌(ξ)` at the generic point `ξ` of `Spec(B)`; since `x` is the image of `ξ` in
`Spec(A)`, the fibre `g⁻¹(ξ)` is none other than `f⁻¹(x) ⊗_{𝒌(x)} k`, which finishes proving the lemma.

The fact that a) implies c) is an immediate consequence of `(7.3.15)` and `(7.3.12)`. On the other hand, let us
specialize c) to the case where `B` is integral, and if `y` denotes the generic point of `Y = Spec(B)`, one has
`𝒪_{Y, y} = 𝒌(y)`, hence `y ∈ U_𝐑(Y)`, since `𝐑(k)` is true for every field `k`; expressing that every point
`y' ∈ g⁻¹(y)` belongs to `U_𝐑(Y')`, one obtains the statement, hence c) implies b). Q.E.D.

**Proposition (7.3.17).**

<!-- label: IV.7.3.17 -->

*Suppose that the property `𝐑` satisfies conditions `(R'_I)` and `(R_II)` and that `𝐏` is the property of the first
(resp. second) type defined from `𝐑` `(7.3.10)`. Then, if `A` is a `𝐏`-ring, the properties `𝐑(A)` and `𝐑(Â)` are
equivalent.*

This results from `(7.3.12.1)` applied to `Y = Spec(A)` and `X = Spec(Â)`.

**Proposition (7.3.18).**

<!-- label: IV.7.3.18 -->

*Suppose that `𝐏` is a property of the first (resp. second) type defined from a property `𝐑` satisfying conditions
`(R'_I)` and `(R_II)` as well as the following condition:*

`(R_III)` *For every complete Noetherian local ring `C`, if one sets `Z = Spec(C)`, the set `U_𝐑(Z)` `(7.3.12)` is open
in `Z`.*

*Then, if `A` is a `𝐏`-ring and if one sets `X = Spec(A)`, the set `U_𝐑(X)` is open in `X`.*

Indeed, if `X' = Spec(Â)` and if `f : X' → X` is the canonical morphism, one has `U_𝐑(X') = f⁻¹(U_𝐑(X))` `(7.3.12)`.
Since `f` is faithfully flat and quasi-compact and by hypothesis `U_𝐑(X')` is open in `X'`, the conclusion follows from
`(2.3.12)`.

**Remarks (7.3.19).**

<!-- label: IV.7.3.19 -->

*(i) The property `𝐑` which serves to define `𝐏` satisfies condition `(R_III)` in all the examples enumerated in
`(7.3.8)`. For (i), (ii) and (iii), this results from `(6.11.2)` and from Cohen's theorem `(0, 19.8.8)`; when `𝐏` is one
of the properties (iv), (iv'), (v), (v'), this follows from `(6.12.7)` and `(6.12.9)`, and when `𝐏` is one of the
properties (vii), (vii'), from `(6.12.7)` and `(6.13.4)`; finally, for (vi) and (vi') the assertion of `(7.3.18)` is
trivial, being true for every locally Noetherian prescheme.*

<!-- original page 198 -->

*(ii) We have already pointed out `(6.4.3)` that when `𝐏` is one of the properties (ii) or `(iii_1)` of `(7.3.8)`, we
are unaware whether every Noetherian local ring is a `𝐏`-ring; recall however that when `A` is a ring quotient of a
Cohen-Macaulay ring, the formal fibres of `A` are Cohen-Macaulay schemes `(6.3.8)`.*

*(iii) The most interesting case of the notion of `𝐏`-ring is that corresponding to the strongest property (iv') of
`(7.3.8)`, that is to say the rings whose formal fibres are geometrically regular. Fields, and more generally complete
Noetherian local rings, trivially satisfy this property.*

*(iv) Let `A` be a Noetherian local ring of dimension `1`; `Spec(A)` is then formed of the closed point `a`,
corresponding to the maximal ideal `𝔪`, and of the maximal points `b_i` `(1 ≤ i ≤ r)` corresponding to the minimal prime
ideals of `A`. One has `dim(Â) = 1` and the maximal ideal of `Â` is `𝔪Â`; the formal fibre of `A` at the point `a` is
therefore `Spec(k)`, where `k = A/𝔪` is the residue field of `A`; the formal fibre at each of the `b_i` is the spectrum
of an Artinian ring whose residue fields are the residue fields `L_{ij}` of `Spec(Â)` at the maximal points `b_{ij}`
lying over `b_i`. Since an Artinian ring is a Cohen-Macaulay ring, one sees that `A` is a `𝐏`-ring when `𝐏` is property
(ii) of `(7.3.8)`. In addition, since a reduced Artinian ring is a direct sum of fields, the following properties are
equivalent `(6.7.7)`:*

*a) the formal fibres of `A` are geometrically reduced;*

*b) the formal fibres of `A` are geometrically normal;*

*c) the formal fibres of `A` are geometrically regular;*

*moreover, when `A` is reduced, they are also equivalent to:*

*d) `Â` is reduced and `L_{ij}` is a separable extension of `K_i` for every pair `(i, j)` `(4.6.1)`.*

*In particular, if `A` is a discrete valuation ring, `K` its field of fractions, and if `K̂` is the completion of `K`
for the valuation corresponding to `A` (the field of fractions of `Â`), in order that the formal fibres of `A` be
geometrically regular, it is necessary and sufficient that `K̂` be a separable extension of `K`. This will always be the
case when `K` is of characteristic `0`.*

### 7.4. Permanence of properties of formal fibres.

**(7.4.1)** In the whole of this number, we suppose that the property `𝐏` is of the form defined in `(7.3.1)`, and
satisfies conditions `(P_I)`, `(P_II)` and `(P_III)` of `(7.3.4)`. We suppose moreover that the property `𝐐` which
serves to define `𝐏` is such that, for every generization `z'` of `z` in `Z`, `𝐐(𝒪_z, k)` entails `𝐐(𝒪_{z'}, k)`.

**Lemma (7.4.2).**

<!-- label: IV.7.4.2 -->

*Let `A`, `A'` be Noetherian local rings, `φ : A → A'` a local homomorphism such that `f = ᵃφ : Spec(A') → Spec(A)` is a
𝐏-morphism. Then, if the formal fibres of `A'` are geometrically regular, `A` is a `𝐏`-ring.*

<!-- original page 199 -->

Consider the completed homomorphism `φ̂ : Â → Â'` and the corresponding morphism `f̂ = ᵃφ̂`; one has the commutative
diagram

```text
       Spec(Â)  ←^{f̂}  Spec(Â')
         ↓ g                ↓ g'
       Spec(A)  ←^{f}   Spec(A')
```

where `g` and `g'` are the canonical morphisms. Since by hypothesis `f` is a 𝐏-morphism and `g'` a regular morphism, it
results from `(P_I)` that `f ∘ g' = g ∘ f̂` is a 𝐏-morphism. On the other hand, the hypothesis that `f` is a 𝐏-morphism
implies that `f` is flat, hence the same is so of `f̂` (Bourbaki, *Alg. comm.*, chap. III, §5, n° 4, cor. of prop. 3),
which is moreover a local homomorphism, hence faithfully flat `(0_I, 6.6.2)`; it then results from `(P_II)` that `g` is
a 𝐏-morphism.

**Corollary (7.4.3).**

<!-- label: IV.7.4.3 -->

*(i) Let `A` be a Noetherian local `𝐏`-ring, `A' = Â` its completion. Suppose that for every prime ideal `p'` of `A'`,
the formal fibres of `A'_{p'}` are geometrically regular; then, for every prime ideal `p` of `A`, `A_p` is a `𝐏`-ring.*

*(ii) Suppose that `𝐏` verifies condition `(P_IV)` `(7.3.6)`. Let `A` be a Noetherian local `𝐏`-ring, `B` an `A`-algebra
essentially of finite type that is local, and such that the homomorphism `A → B` is local. Set `A' = Â`, and let `𝔫'` be
the unique prime ideal of `B' = B ⊗_A A'` lying over the maximal ideal of `B` and over the maximal ideal of `A'`. If the
formal fibres of `B'_{𝔫'}` are geometrically regular, then `B` is a `𝐏`-ring.*

(i) Since by hypothesis `Spec(A') → Spec(A)` is a 𝐏-morphism, the same is so of `Spec(A'_p) → Spec(A_p)` by virtue of
`(7.3.2, b))`, for every prime ideal `p` of `A` and every prime ideal `p'` of `A'` lying over `p`. It then suffices to
apply lemma `(7.4.2)` to this morphism, noting that the morphism `Spec(A') → Spec(A)` is surjective.

(ii) By virtue of `(7.4.2)`, it suffices to prove that the morphism `Spec(B'_{𝔫'}) → Spec(B)` is a 𝐏-morphism. Now one
has `B = C_𝔫`, where `C` is an `A`-algebra of finite type and `𝔫` a prime ideal of `C` lying over the maximal ideal of
`A`. If one sets `C' = C ⊗_A A'`, it results from the hypotheses and from `(7.3.7)` that `Spec(C') → Spec(C)` is a
𝐏-morphism; since `B'_{𝔫'}` is a local ring of `C'` at a prime ideal of `C'` lying over `𝔫`, the conclusion results from
`(7.3.2, b))`.

**Theorem (7.4.4).**

<!-- label: IV.7.4.4 -->

*The hypotheses on `𝐏` being those of `(7.4.1)`, let `A` be a Noetherian local `𝐏`-ring.*

*(i) For every prime ideal `p` of `A`, `A_p` is a `𝐏`-ring.*

*(ii) Suppose moreover that `𝐏` verifies condition `(P_IV)`. Then every local ring which is an `A`-algebra essentially
of finite type is a `𝐏`-ring.*

(i) Applying `(7.4.3, (i))`, the whole question is to see that for every prime ideal `p'` of `A' = Â`, `A'_{p'}` has
geometrically regular formal fibres. Now, this has been proved in `(0, 22.3.3` and `22.5.8)`.

<!-- original page 200 -->

(ii) Let `B` be an `A`-algebra essentially of finite type that is a local ring; if `p` is the prime ideal of `A` over
which the maximal ideal of `B` lies, `B` is also an `A_p`-algebra essentially of finite type `(1.3.8)`; by virtue of
(i), one may therefore suppose that `p` is the maximal ideal `𝔪` of `A`. One has then `B = C_q`, where `C` is an
`A`-algebra of finite type, `q` a prime ideal of `C` lying over `𝔪`; let `𝔫 ⊃ q` be a maximal ideal of `C` (necessarily
lying over `𝔪`); if one sets `k = A/𝔪`, `C/𝔪C` is a `k`-algebra of finite type, hence the residue field `k'` of `C` at
the maximal ideal `𝔫` is finite over `k` `(I, 6.4.2)`; by virtue of (i), it will suffice to prove that `C_𝔫` is a
`𝐏`-ring, since `C_q` is a local ring of `C_𝔫` at a prime ideal of `C_𝔫`. One is thus reduced to proving the

**Lemma (7.4.4.1).**

<!-- label: IV.7.4.4.1 -->

*Let `A` be a Noetherian local `𝐏`-ring, `k` its residue field, `C` an `A`-algebra of finite type, `B` a local ring at a
prime ideal `𝔫` of `C`, such that: 1° the homomorphism `A → B` is local; 2° the residue field `k'` of `B` is a finite
extension of `k`. If `𝐏` satisfies `(P_IV)`, `B` is a `𝐏`-ring.*

Let `(x_i)_{1 ≤ i ≤ m}` be a system of generators of the `A`-algebra `C`; let us show first that one may reason by
induction on `m`. Let `C'` be the subalgebra of `C` generated by `x_1, …, x_{m-1}`, and let `𝔫' = 𝔫 ∩ C'`. The
homomorphism `A → C_𝔫` factors into `A → C'_{𝔫'} → C_𝔫`, and it is clear that `A → C'_{𝔫'}` and `C'_{𝔫'} → C_𝔫` are
local homomorphisms; if `k''` is the residue field of `C'_{𝔫'}`, `k → k''` factors likewise into `k → k'' → k'`, hence
`k''` is a finite extension of `k` and `k'` an extension of `k''`. The induction hypothesis entails that `C'_{𝔫'}` is a
`𝐏`-ring; moreover, if `S' = C' - 𝔫'`, `C_𝔫` is a local ring of `S'⁻¹ C`; as `C = C'[x_m]`, one has
`S'⁻¹ C = C'_{𝔫'}[x_m / 1]` and the induction hypothesis again shows that `C_𝔫` is a `𝐏`-ring. One is thus reduced to
the case where `C` is an `A`-algebra generated by a *single* element `t`.

Let us apply `(7.4.3, (ii))`; setting `A' = Â`, `B' = B ⊗_A A'` is a local ring of `C ⊗_A A'` at a prime ideal lying
over `𝔫`; since `A` and `A'` have the same residue field `k`, the residue field of `C ⊗_A A'` at this prime ideal is
equal to `k'`. Moreover `C ⊗_A A'` is an `A'`-algebra generated by a single element. It results then from
`(7.4.3, (ii))` that one may reduce to proving `(7.4.4.1)` when `𝐏` is property (iv') of `(7.3.8)`, that `A` is
*complete* and `C` generated by a single element `t`.

To show that the formal fibres of `B = C_𝔫` are then geometrically regular, let us apply criterion `(7.3.16, b))`. Let
`B_1` be an integral finite `B`-algebra, hence generated by a finite number of elements integral over `B`. By
multiplying these elements by an element of `S = C - 𝔫`, one may suppose they are integral over `C`, and one may then
write `B_1 = S⁻¹ C_1`, where `C_1` is a sub-`C`-algebra of `B_1` generated by a finite number of elements integral over
`C`, hence a *finite and integral* `C`-algebra. On the other hand, `B_1` is a semi-local ring, and every local ring
`B_2` of `B_1` at a maximal ideal is a local ring of `C_1` at a prime ideal, such that `A → B_2` is a local
homomorphism; moreover, the residue field of `B_2` is a finite extension of `k'`, hence of `k`. One sees therefore
(taking into account `(7.3.14)` and (i)) that one is reduced to the following question: let `C` be an integral
Noetherian ring, containing a subring `C_0` which is an `A`-algebra generated by a single element `t` and such that `C`
is a *finite* `C_0`-algebra; if `𝔫` is a maximal ideal of `C`

<!-- original page 201 -->

lying over the maximal ideal of `A`, and `B = C_𝔫`, the question is to show that for every prime ideal `q` of `B̂` whose
inverse image in `B` is `0`, the ring `B̂_q` is *regular*. One may moreover replace `A` by its image in `C`, which is a
complete local ring (as a quotient of `A`) and integral. The conclusion to prove is then a consequence of the following
more general lemma:

**Lemma (7.4.4.2).**

<!-- label: IV.7.4.4.2 -->

*Let `A` be a Noetherian local integral and complete ring, `k` its residue field, `C` an integral ring containing `A`,
such that there exists `t ∈ C` for which `C` is a finite `A[t]`-algebra. Let `𝔫` be a maximal ideal of `C` lying over
the maximal ideal `𝔪` of `A`; set `B = C_𝔫`, `X = Spec(B)`, `B' = B̂`, `X' = Spec(B̂)`; if `U = Reg(X)`, `U' = Reg(X')`,
and if `f : X' → X` is the canonical morphism, one then has `f⁻¹(U) ⊂ U'`.*

The assertion to prove to obtain `(7.4.4.1)` will follow from this lemma observing that, since `B` is integral, the
generic point of `X` belongs to `U`.

One will note that since `C` is an `A`-algebra of finite type, and `𝔫` a maximal ideal of `C`, the residue field `k'` of
`C_𝔫 = B` (hence also of `B'`) is a *finite* extension of `k` (`(I, 6.4.11)` and `(6.4.2)`).

If one sets `Y = Spec(C)`, it results from `(6.12.8)` that `Reg(Y)` is open in `Y`; since the local rings of `X` are
local rings of `Y` `(I, 2.4.2)`, one has `U = X ∩ Reg(Y)`, hence `U` is open in `X`; on the other hand `(6.12.7)` `U'`
is open in `X'`, hence `S' = X' - U'` is closed; consequently `S' ∩ f⁻¹(U)` is locally closed in `X'`, and the whole
question is to prove that this set is empty. One knows `(5.1.10)` that in the contrary case, there would exist a prime
ideal `p'` of `S' ∩ f⁻¹(U)` such that `dim(B'/p') ≤ 1`. Let us remark first that `p'` cannot be the maximal ideal `𝔪B'`
of `B'`, where `𝔪` is the maximal ideal of `B`. Indeed, this would signify that `B = B_𝔪` is regular, hence also
`B' = B̂` `(0, 17.1.5)`, and one would have by hypothesis `𝔪B' ∈ U'` contrary to the hypothesis. One must therefore have
`dim(B'/p') = 1`. Set `p = B ∩ p'`; by hypothesis `B_p` is regular, but `B'_{p'}` is not so; since `B'_{p'}` is a flat
`B_p`-module, it results from `(6.5.2)` that the fibre `Z` of `f` at the point `p` is not regular at the point `p'`. Let
us show that one may reduce to the case where `p = 0`. Indeed, in the general case, if one sets `q = p ∩ C`,
`r = p ∩ A`, `C/q` is an `(A/r)[t̄]`-algebra finite (where `t̄` is the class of `t` mod. `q`); since `p = qB`, `B/p`
equals `(C/q)_{𝔫/q}`, and `𝔫/q` is a maximal ideal of `C/q` lying over the maximal ideal `𝔪/r` of `A/r`; one sees thus
that the hypotheses of `(7.4.4.2)` are still satisfied by `A/r`, `C/q` and `B/p`, and since the completion of `B/p` is
`B'/pB'`, this proves our assertion. Suppose therefore that `p = 0`, so that `Z` is the generic fibre of `f` and the
homomorphism `B → B'/p'` is *injective*. Set `V = B'/p'`, and distinguish two cases:

I) *`V` is a finite `A`-algebra.* — Since `B ⊂ V`, `B` is a fortiori a finite `A`-algebra, and since `A` is complete,
the same is so of `B` (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9), whence `B' = B`, `p' = 0`, hence
`B'_{p'}` is a field, and consequently a regular local ring, contrary to the hypothesis.

II) *`V` is not a finite `A`-algebra.* — Since the local ring `A` is *complete*, this implies that `V` is not a
quasi-finite `A`-algebra (`(0_I, 7.4.1)` and `(7.4.2)`); but by hypothesis the residue field `k'` of `V` is a *finite*
extension of the residue field `k` of `A`,

<!-- original page 202 -->

hence `(0_I, 7.4.4)` the ideal `𝔪V` is *not an ideal of definition of `V`*. Since `V` is an integral Noetherian local
ring of dimension `1`, `0` is the only ideal of `V` that is not an ideal of definition, hence `𝔪V = 0`. But one has
`A ⊂ V` and `V` is integral, whence `𝔪 = 0` and `A = k` is a field. One deduces from this first of all `dim(C) ≤ 1`
`(0_I, 16.1.5)`; but since `dim(V) = 1`, the relations `dim(V) ≤ dim(B') = dim(B) ≤ dim(C)` show that this entails
`dim(C) = dim(B) = dim(B') = dim(B'/p') = 1`, and consequently `p'` is necessarily a *minimal ideal* of `B'`. We shall
thus arrive at a contradiction if we prove that `B'_{p'}` is a field, or again that the ring `B'` is reduced. Now, since
`C` is a `k`-algebra of finite type, the integral closure `C_1` of `C` is a *finite* `C`-algebra (Bourbaki, *Alg.
comm.*, chap. V, §3, n° 2, th. 2); if one sets `S = C - 𝔫`, `B_1 = S⁻¹ C_1` is the integral closure of `B`, hence a
finite `B`-algebra, and consequently a semi-local Noetherian, integral and integrally closed ring of dimension `1`
`(0, 16.1.5)`; if `𝔪_j` `(1 ≤ j ≤ h)` are its maximal ideals, the `(B_1)_{𝔪_j}` are therefore discrete valuation rings
`(II, 7.1.6)`, and the completion `B'_1` of `B_1` is the direct composite of the completed discrete valuation rings of
the `(B_1)_{𝔪_j}` (Bourbaki, *Alg. comm.*, chap. III, §2, n° 13, prop. 18); `B'_1` is therefore reduced, and since the
completion `B'` of `B` is a subring of `B'_1` (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9), it is
also a reduced ring. Q.E.D.

**Corollary (7.4.5).**

<!-- label: IV.7.4.5 -->

*Suppose that the property `𝐏` satisfies conditions `(P_I)`, `(P_II)`, `(P_III)`. Let `A` be a Noetherian ring. The
following conditions are equivalent:*

*a) For every prime ideal `p` of `A`, `A_p` is a `𝐏`-ring.*

*b) For every maximal ideal `𝔪` of `A`, `A_𝔪` is a `𝐏`-ring.*

*If moreover `𝐏` satisfies `(P_IV)`, properties a) and b) are also equivalent to:*

*c) For every `A`-algebra of finite type `B` and every prime ideal `q` of `B`, `B_q` is a `𝐏`-ring.*

The equivalence of a) and b) results from `(7.4.4, (i))`, and that of a) and c) from `(7.4.4, (ii))`.

When condition a) of `(7.4.5)` is satisfied, one says that `A` is a **𝐏-ring**; for semi-local Noetherian rings, this
definition coincides with that of `(7.3.13)`, when conditions `(P_I)`, `(P_II)` and `(P_III)` are satisfied. The ring
`Z` is a 𝐏-ring `(7.3.19, (iv))`; every complete local ring is a 𝐏-ring.

**Proposition (7.4.6).**

<!-- label: IV.7.4.6 -->

*Suppose that the property `𝐏` satisfies conditions `(P_I)`, `(P_II)` and `(P_III)`. Let `A` be a Noetherian ring, `𝔍`
an ideal of `A`, `Â` the separated completion of `A` for the `𝔍`-preadic topology. Then, if `A` is a `𝐏`-ring `(7.4.5)`,
the canonical morphism `Spec(Â) → Spec(A)` is a 𝐏-morphism.*

Using `(7.3.2, c'))`, it suffices to prove that for every maximal ideal `𝔫` of `Â`, of inverse image `𝔪` in `A`, the
morphism `Spec((Â)_𝔫) → Spec(A_𝔪)` is a 𝐏-morphism. One knows (Bourbaki, *Alg. comm.*, chap. III, §3, n° 4, prop. 8)
that the canonical homomorphism `A_𝔪 → (Â)_𝔫` is injective, that the `𝔪A_𝔪`-preadic topology on `A_𝔪` is induced by the
`𝔫(Â)_𝔫`-preadic topology and that `A_𝔪` is dense in `(Â)_𝔫`, so that the completion of `A_𝔪` for the `𝔪A_𝔪`-preadic
topology identifies with that of `(Â)_𝔫` for the `𝔫(Â)_𝔫`-preadic topology. One therefore has two morphisms

```text
       Spec((A_𝔪)^)  →^{f}  Spec((Â)_𝔫)  →^{g}  Spec(A_𝔪)
```

<!-- original page 203 -->

such that `f` is faithfully flat; since by hypothesis `g ∘ f` is a 𝐏-morphism, the same is so of `g` by virtue of
`(P_II)`.

**Corollary (7.4.7).**

<!-- label: IV.7.4.7 -->

*Suppose that `𝐏` verifies conditions `(P_I)`, `(P'_I)`, `(P_II)`, `(P_III)` and `(P_IV)`. Then, if `A` is a `𝐏`-ring
`(7.4.5)`, the canonical morphism `Spec(A[[T_1, …, T_r]]) → Spec(A)` is a 𝐏-morphism. In particular, if moreover `A` is
integral, `K` its field of fractions, and if `p` is a prime ideal of `B = A[[T_1, …, T_r]]` such that `p ∩ A = 0`, then
the property `𝐏(B_p, K)` is true.*

Indeed, the canonical morphism `Spec(B) → Spec(A)` factors into

```text
   Spec(A[[T_1, …, T_r]])  →^{f}  Spec(A[T_1, …, T_r])  →^{g}  Spec(A).
```

It is clear that the morphism `g` is regular `(0, 17.3.7)`; by virtue of `(7.4.5)`, `A[T_1, …, T_r]` is a `𝐏`-ring,
hence it results from `(7.4.6)` that `f` is a 𝐏-morphism; since `g` is regular, hence also a 𝐏-morphism `(7.3.5, (i))`,
the same is so of `g ∘ f` by virtue of `(P'_I)`.

One will note that the conclusion is still valid if instead of supposing that `𝐏` verifies `(P'_I)` and that every
regular morphism is a 𝐏-morphism, one supposes only that a composite morphism `g ∘ f` is a 𝐏-morphism when `g` is
regular and `f` a 𝐏-morphism (a sort of symmetric condition of `(P'_I)`).

**Remark (7.4.8).**

<!-- label: IV.7.4.8 -->

*The preceding results pose the following problems:*

*A) Let `A` be a Zariski ring **complete**, and let `𝔍` be an ideal of definition of `A`; if the ring `A/𝔍` is a
`𝐏`-ring, is the same so of `A`? It would result from this that for every Noetherian `𝐏`-ring `A` and every ideal `𝔍` of
`A`, the separated completion `Â` for the `𝔍`-preadic topology would also be a `𝐏`-ring.*

*B) Let `k` be a complete non-discrete valued field; one again calls **ring of restricted formal series**
`k{T_1, …, T_n}` the subring of the ring of formal series `k[[T_1, …, T_n]]` formed of the series whose coefficients
**tend to 0**. Is such a ring a `𝐏`-ring?*

*C) If `A` is a linearly topologized `𝐏`-ring, `S` a multiplicative part of `A`, are the rings `A{S⁻¹}` `(0_I, 7.6.1)`
and `A_{(S)}` `(0_I, 7.6.15)` `𝐏`-rings?*

<!-- original page 203 -->

### 7.5. A criterion for `𝐏`-morphisms.

**(7.5.0)** This number will not be used in the sequel of Chapter IV, and may therefore be omitted at a first reading.
We shall see moreover further on `(7.9.8)` that the results of the present number can be considerably improved when one
has at one's disposal "resolution of singularities".

In the sequel of this number, we shall consider a property `𝐑(A)`, and we shall denote by `𝐏(Z, k)` the following
property:

> "`Z` is a locally Noetherian prescheme over a field `k`, and, for every finite extension `k'` of `k`, if one sets
> `Z' = Z ⊗_k k'`, the property `𝐑(𝒪_{Z', z'})` is true for every `z' ∈ Z'`."

**Theorem (7.5.1).**

<!-- label: IV.7.5.1 -->

*Let `A`, `B` be two complete Noetherian local rings, `𝔪` the maximal ideal of `A`, `k = A/𝔪` its residue field,
`φ : A → B` a local homomorphism such that:*

*(i) The residue field of `B` is a finite extension of `k`.*

*(ii) `B` is a flat `A`-module.*

*Let on the other hand `𝐑(C)` be a property verifying condition `(R_III)` `(7.3.18)` and the following condition:*

*`(R_IV)` For every local ring `C` at a prime ideal of a complete Noetherian local ring and every `C`-regular element
`t` in the maximal ideal of `C`, the property `𝐑(C/tC)` implies `𝐑(C)`.*

*This being so, let `f = ᵃφ : Spec(B) → Spec(A)`, and suppose that the property `𝐏(Spec(B ⊗_A k), k)` is true. Then, for
every `x ∈ Spec(A)`, the property `𝐏(f⁻¹(x), 𝒌(x))` is true.*

In other words, the property `𝐏` for the fibre of the closed point of `Spec(A)` entails this same property for all
fibres of the morphism `f` (in other words, `f` is a `𝐏`-morphism `(7.3.1)`).

We shall proceed in several steps:

I) *Reduction to the study of the local rings of the generic fibre.* — Let us apply lemma `(7.3.16.2)`: it suffices to
see that for every finite integral `A`-algebra `A'`, of field of fractions `K'`, if one sets `B' = B ⊗_A A'`, all the
local rings of `Spec(B' ⊗_{A'} K')` verify the property `𝐑`. The ring `A'` (resp. `B'`) is complete semi-local (`B'`
being a finite `B`-algebra), hence a direct composite of complete local rings; since `A'` is assumed integral, it is
local; every maximal ideal `𝔫'` of `B'` lies above the maximal ideal `𝔫` of `B`, hence above `𝔪`, and consequently its
inverse image in `A'` is the maximal ideal `𝔪'` of `A'`. Since every local ring of `Spec(B' ⊗_{A'} K')` is a local ring
of `Spec(B')`, hence of one of the `Spec(B'_{𝔫'})` (above the generic point of `A'`), one sees that it will suffice to
prove that the local rings of `Spec(B'_{𝔫'} ⊗_{A'} K')` possess the property `𝐑`. Now `A'` and `B'_{𝔫'}` are complete
Noetherian local rings; the residue field of `B'_{𝔫'}` is a finite extension of that of `B`, hence also of `k`, and a
fortiori of the residue field `k'` of `A'`; this remark and `(2.1.4)` show that `A'` and `B'_{𝔫'}` verify conditions (i)
and (ii) of the statement. On the other hand, if `k''` is a finite extension of `k'`, `k''` is also a finite extension
of `k`, and the local rings of `Spec(B'_{𝔫'} ⊗_{A'} k'')` are also local rings of `Spec(B ⊗_A k'')`; hence the
hypothesis that `𝐏(Spec(B ⊗_A k), k)` is true entails that `𝐏(Spec(B'_{𝔫'} ⊗_{A'} k''), k')` is true.

One is thus reduced to the case where `A` is moreover assumed integral, of field of fractions `K`, and to proving that
the local rings of `Spec(B ⊗_A K)` possess the property `𝐑`.

II) *Case where `dim(A) = 1`.* — Let `A'` be the integral closure of `A`; one knows `(0, 23.1.6)` that `A'` is a finite
`A`-algebra and a complete local ring; if one sets `B' = B ⊗_A A'`, one has `B ⊗_A K = B' ⊗_{A'} K`. The same reasoning
as in I) shows that it suffices, for every maximal ideal `𝔫'` of `B'`, to prove that the local rings of
`B'_{𝔫'} ⊗_{A'} K` verify `𝐑`; moreover, this reasoning also shows that `A'` and `B'_{𝔫'}` verify the hypotheses (i) and
(ii) of the statement and that `𝐏(Spec(B'_{𝔫'} ⊗_{A'} k'), k')` is true (`k'` being the residue field of `A'`).
Moreover, since `dim(A') = 1` `(0, 16.1.5)` and `A'` is integral and integrally closed, it is a complete discrete
valuation ring. One may therefore restrict to the case where `A` is already a complete discrete valuation ring; if then
`u` is a uniformizing parameter of `A`, the fact that `u` is `A`-regular and that `B` is a flat `A`-module entails that
`t = φ(u)` is a `B`-regular element, lying in the maximal ideal of `B`. The hypothesis that `𝐏(Spec(B ⊗_A k), k)` is
true entails in particular that `𝐑(B/tB)` is true; by virtue of `(R_IV)`, `𝐑(B)` is therefore true. In other words,
`U_𝐑(Spec(B))` contains the closed point of `Spec(B)`. But since `U_𝐑(Spec(B))` is open by virtue of `(R_III)` and
`Spec(B)` is the only open set of `Spec(B)` containing the closed point, all the local rings of `Spec(B)` possess the
property `𝐑`, and in particular those of `Spec(B ⊗_A K)`.

III) *General case.* — The case `dim(A) = 0` is trivial, since then `A = k`; one may therefore restrict to the case
where `dim(A) ≥ 1`. One knows `(6.12.7)` that `Spec(A)` contains a non-empty open set `V` all of whose points are
regular; since `dim(A) ≥ 1`, the intersection `V'` of `V` and the complement of the closed point of `Spec(A)` is a
non-empty open set, hence containing the generic point of `Spec(A)`. If we prove that `f⁻¹(V') ⊂ U_𝐑(Spec(B))`, the
proposition will be proved a fortiori. In other words, it suffices to see that the set `Z`, intersection of `f⁻¹(V')`
and the complement of `U_𝐑(Spec(B))`, is empty. Let us reason by contradiction: since, by virtue of `(R_III)`,
`U_𝐑(Spec(B))` is open in `Spec(B)`, `Z` is locally closed in `Spec(B)`; if it were not empty, it would contain a point
`x` such that `dim(‾{x}) ≥ 1` `(5.1.10)`; since `f(x) ∈ V'` is distinct from the closed point of `Spec(A)`, `x` is
distinct from the closed point of `Spec(B)`, in other words `dim(‾{x}) = 1`. We shall prove that this is impossible, in
other words that, if `dim(‾{x}) = 1` and `f(x) ∈ V'`, then one has `𝐑(𝒪_x)`. In other terms, the matter is to see that,
if `𝔮` is a prime ideal of `B` such that `dim(B/𝔮) = 1` and if `𝔭 = ᵃφ⁻¹(𝔮)` is distinct from `𝔪` and such that `A_𝔭` is
regular, then one has `𝐑(B_𝔮)`. Since `𝔭 ≠ 𝔪`, `𝔪(B/𝔮)` is not reduced to `0`, hence is an ideal of definition of the
integral Noetherian local ring `B/𝔮` of dimension `1`; on the other hand, by virtue of (i), the residue field of `B/𝔮`
is a finite extension of the residue field `k` of `A/𝔭`, hence `B/𝔮` is a quasi-finite `(A/𝔭)`-algebra `(0_I, 7.4.4)`.
But `A/𝔭` is complete and `B/𝔮` is separated for the `𝔪`-preadic topology (which is identical to its local-ring
topology); hence `(0_I, 7.4.1)`, `B/𝔮` is a finite `(A/𝔭)`-algebra. Moreover, by definition, the homomorphism
`A/𝔭 → B/𝔮` is injective, hence `(0, 16.1.5)` one has `dim(A/𝔭) = dim(B/𝔮) = 1`. One can then apply to the rings `A/𝔭`
and `B/𝔭B` the result of II), for the residue fields of these local rings are respectively those of `A` and of `B`, and
`B/𝔭B` is a flat `(A/𝔭)`-module; moreover, one has `(B/𝔭B) ⊗_{A/𝔭} k = B ⊗_A k = B/𝔪B`. Consequently, the local rings of
`Spec((B/𝔭B) ⊗_{A/𝔭} 𝒌(𝔭))` verify `𝐑`. Now, `B_𝔮/𝔭B_𝔮` is one of the local rings of `Spec((B/𝔭B) ⊗_{A/𝔭} 𝒌(𝔭))`.
Moreover, `B_𝔮` is a flat `A_𝔭`-module, and `A_𝔭` is regular. Now one has the following lemma:

<!-- original page 205 -->

**Lemma (7.5.1.1).**

<!-- label: IV.7.5.1.1 -->

*Let `𝓒` be a full subcategory of the category of Noetherian local rings, such that every quotient ring of a ring of `𝓒`
still belongs to `𝓒`. Let `𝐑(C)` be a property such that if `C ∈ 𝓒` and if `t` is a regular element of the maximal ideal
of `C` such that `𝐑(C/tC)` is true, then `𝐑(C)` is true.*

*This being so, let `C` be a regular local ring, `k` its residue field, `D` a local ring belonging to `𝓒`, `φ : C → D` a
local homomorphism making `D` a flat `C`-module. Then, if `𝐑(D ⊗_C k)` is true, the same is so of `𝐑(D)`.*

Let us reason by induction on `n = dim(C)`, the lemma being true by hypothesis if `n = 0`, since then `C = k`. Let `t`
be an element of the maximal ideal `𝔪` of `C` not belonging to `𝔪²`; one knows then that `C/tC` is regular and that
`dim(C/tC) = n - 1` (`(0, 17.1.8)` and `(0, 16.3.4)`). Since `(D/tD) ⊗_{C/tC} k = D ⊗_C k`, and `D/tD ∈ 𝓒`, the
induction hypothesis shows that `𝐑(D/tD)` is true; moreover, `t` is `C`-regular, hence also `D`-regular by flatness
`(0_I, 6.3.4)`; the hypothesis made on `𝐑` therefore shows that `𝐑(D)` is true.

To finish the proof of `(7.5.1)`, it suffices here to apply lemma `(7.5.1.1)` taking for `𝓒` the category of the local
rings of the spectra of complete local rings, taking into account the hypothesis `(R_IV)`, and taking for `C` the ring
`A_𝔭`, for `D` the ring `B_𝔮`.

**Corollary (7.5.2).**

<!-- label: IV.7.5.2 -->

*Let `A` be a Noetherian local ring, `𝔪` the maximal ideal of `A`, `k = A/𝔪` its residue field, `B` a Noetherian local
ring, `φ : A → B` a local homomorphism such that:*

*(i) The residue field of `B` is a finite extension of `k`.*

*(ii) `B` is a flat `A`-module.*

*Let on the other hand `𝐑(C)` be a property verifying conditions `(R_II)` `(7.3.10)`, `(R_III)` `(7.3.18)` and `(R_IV)`
`(7.5.1)`.*

*Finally, let `𝐑'(C)` be a property verifying the following condition:*

*`(R_V)` If `C`, `D` are two Noetherian local rings, `ψ : C → D` a local homomorphism such that*
*`g = ᵃψ : Spec(D) → Spec(C)` is a `𝐏`-morphism, then the property `𝐑'(C)` implies `𝐑(D)`.*

*Suppose that the canonical morphism `Spec(Â) → Spec(A)` is a `𝐏'`-morphism, where `𝐏'` is defined from `𝐑'` as `𝐏` from
`𝐑` in `(7.5.0)`.*

*This being so, let `f = ᵃφ : Spec(B) → Spec(A)`, and suppose that the property `𝐏(Spec(B ⊗_A k), k)` is true. Then, for
every `x ∈ Spec(A)`, the property `𝐏(f⁻¹(x), 𝒌(x))` is true (in other words, `f` is a `𝐏`-morphism).*

Let us proceed once again in two steps:

I) *Reduction to the study of the local rings of the generic fibre.* — Let us apply once again lemma `(7.3.16.2)`; the
only difference with the reasoning of I) in `(7.5.1)` is that here the ring `A'` is only a semi-local integral ring, but
not necessarily local; every maximal ideal `𝔫'` of `B'` is then above a maximal ideal `𝔪'` of `A'`; since every local
ring of `Spec(B' ⊗_{A'} K')` is a local ring of `Spec(B')`, hence of one of the `Spec(B'_{𝔫'})` (above the generic point
of `Spec(A'_{𝔪'})`), one is reduced to proving that the local rings of `Spec(B'_{𝔫'} ⊗_{A'_{𝔪'}} K')` possess the
property `𝐑`. Now, the definition of `𝐏'` implies that if `𝐏'(Z, k)` is true, the same is so of `𝐏'(Z ⊗_k k', k')` for
every finite extension `k'` of `k`; the same reasoning as in `(7.3.7)` proves that the formal fibres of `A'_{𝔪'}`
possess the property `𝐏'`. One sees as in part I) of the proof of `(7.5.1)` that `A'_{𝔪'}` and `B'_{𝔫'}` verify
conditions (i) and (ii) of `(7.5.2)`; on the other hand, if `k'` is the residue field of `A'_{𝔪'}`, the property
`𝐏(Spec(B'_{𝔫'} ⊗_{A'_{𝔪'}} k'), k')` is true: in effect, the completion of `A'_{𝔪'}` is one of the component local
rings of `Â' = Â ⊗_A A'`, and the completion of `B'_{𝔫'}` one of the component local rings of
`B̂' = B̂ ⊗_B B' = B̂ ⊗_A A' = B ⊗_A Â'`; the reasoning of I), in `(7.5.1)`, proves therefore our assertion.

One may therefore restrict to the case where `A` is moreover assumed integral, and to proving that, if `K` is the field
of fractions of `A`, the local rings of `Spec(B ⊗_A K)` possess the property `𝐑`.

II) *Reduction to the case where `A` and `B` are complete.* — Let `ξ` be the generic point of `Spec(A)`, `y` an
arbitrary point of `f⁻¹(ξ)`; the matter is to prove that `𝐑(𝒪_y)` is true; taking account of condition `(R_II)`, it will
suffice to see that there exists in `Spec(B̂)` a point `z` above `y` and such that `𝐑(𝒪_z)` is true. Now, it results
from the hypothesis made on `Spec(B ⊗_A k)` and from `(7.5.1)` that the morphism `f̂ : Spec(B̂) → Spec(Â)` is a
`𝐏`-morphism. On the other hand, for every point `z ∈ Spec(B̂)` above `y` (there exists such a point, since `B̂` is a
faithfully flat `B`-module), the image `x` of `z` in `Spec(Â)` belongs to the fibre `h⁻¹(ξ)` for the canonical morphism
`h : Spec(Â) → Spec(A)`; by virtue of the hypothesis made on `A`, the property `𝐑'(𝒪_x)` is true; hence by virtue of
`(R_V)`, `𝐑(𝒪_z)` is true. Q.E.D.

**Examples (7.5.3).**

<!-- label: IV.7.5.3 -->

*Let us consider the following properties `𝐑(C)` (`C` being a Noetherian local ring):*

*(i) (also denoted `(i_n)`) `coprof(C) ≤ n`.*

<!-- original page 206 -->

*(ii) (also denoted `(ii_k)`) `C` verifies `(S_k)`.*

*(iii) `C` is a Cohen-Macaulay ring.*

*(iv) `C` is a regular ring.*

*(v) (also denoted `(v_k)`) `C` is integral, integrally closed and verifies `(R_k)`.*

*(vi) `C` is integral and integrally closed.*

*(vii) `C` is integral.*

*(viii) `C` is reduced.*

All these properties verify `(R_III)`, as one has seen in `(7.3.19, (i))`. They also verify `(R_IV)`: for (i), this
results from `(0, 16.4.10, (ii))`, and for (ii) and (iii), this results from `(5.12.4)` and from the fact that a
complete Noetherian local ring is catenary `(5.6.4)`; for (iv), this is a particular case of `(0, 17.1.8)`; for (vii),
this follows from `(3.4.5)` and for (viii) from `(3.4.6)`; for (vi) this results from `(5.12.7)` and from the fact that
a complete Noetherian local ring is catenary `(5.6.4)`; finally, for (v), this results from what precedes and from
`(5.12.5)`.

One can therefore apply the theorem `(7.5.1)` when `𝐑` is any of the properties above. On the other hand, one has
already remarked `(7.3.11)` that the properties (i) to (viii) verify `(R_II)` (except for (vii), where the verification
of `(R_II)` is a consequence of `(2.1.14)`). As regards `(R_V)`, one will note that if one takes there `𝐑' = 𝐑`, the
condition `(R_V)` reduces to the condition `(R_I)` of `(7.3.11)`, and one has noted that the properties (ii) to (vi), as
well as (viii), verify `(R_I)` `(7.3.11)`; for the property (i), one can take for `𝐑'` the property of being a
Cohen-Macaulay ring, by virtue of `(6.3.2)`. Finally, for the property (vii), the condition `(R_I)` is no longer
verified (nor moreover `(R_I)`), as the example of `(6.15.11, (ii))` or of `(6.5.5, (ii))` shows. By contrast, `(R_V)`
is then true when one takes for `𝐑'` the property of being regular: it suffices in effect to apply lemma `(7.5.1.1)`
taking for `𝓒` the category of all Noetherian local rings, and for `𝐑(C)` the property of being integral; this is
possible by virtue of `(3.4.5)`.

One sees thus in particular that when `𝐑` is any of the properties (i) to (viii), the conclusion of corollary `(7.5.2)`
is applicable when one supposes that the formal fibres of `A` are geometrically regular (cf. `(7.8.2)`).

**Remarks (7.5.4).**

<!-- label: IV.7.5.4 -->

*(i) It would be interesting to know whether the theorem `(7.5.1)` subsists without the finiteness hypothesis (i) on the
residue field of `B`. The answer is affirmative when the residue field `k` of `A` is of characteristic `0`, as one sees
using Hironaka's results on resolution of singularities (cf. `(7.9.8)`). Let us signal the following particular case of
the question raised here: Let `A` and `B` be two complete Noetherian rings, `k` the residue field of `A`, `φ : A → B` a
local homomorphism making `B` a formally smooth `A`-algebra `(0, 19.3.1)` (which is equivalent to saying that `B` is a
flat `A`-module and that `B ⊗_A k` is geometrically regular over `k` `(0, 19.7.1)`). Are then the fibres of the morphism
`ᵃφ : Spec(B) → Spec(A)` geometrically regular? Such is the case when the residue field `k'` of `B` is a finite
extension of `k`, by `(7.5.1)`; one can prove that the answer is still affirmative when `k'` is a finitely generated
extension of `k`. We do not know the answer when `B ⊗_A k` is a field equal to the separable closure of `k`.*

*(ii) One could state a result analogous to `(7.5.1)` relative to an `A`-module `M`, a `B`-module `N`, both of finite
type, concerning the properties of `(M ⊗_A N)_y ⊗_{𝒪_y} 𝒌(y)`, where `y` runs over `Spec(B)` and `x = f(y)`, following
from properties of the same type of `M_x` and `N_y`.*

*(iii) When the property `𝐑` verifies the conditions `(R_I)`, `(R_II)`, `(R_III)` and `(R_IV)` and the hypotheses (i)
and (ii) of `(7.5.2)` are fulfilled, then, from the properties `𝐑(A)` and `𝐏(Spec(B ⊗ k), k)` one deduces `𝐑(B)`. This
is the case, as one has seen `(7.5.3)`, for the properties given as examples in `(7.5.3)`, except for (i) and (vii). As
regards (vii), it is however plausible that the answer to the following question is affirmative: let `φ : A → B` be a
local homomorphism of Noetherian local rings, making `B` a flat `A`-module. Suppose that `A` is complete, integral and
geometrically unibranch, and that the fibre `Spec(B ⊗_A k)` (where `k` is the residue field of `A`) is geometrically
locally integral; then is it true that `B` is integral? One can prove it when `k` is of characteristic `0`, using
Hironaka's resolution of singularities `(7.9.8)`; one can also show that the answer is affirmative when `B` is an
`A`-algebra essentially of finite type `(1.3.8)` (cf. `(11.3.10)` and `(11.3.11)`) or when `Spec(B ⊗_A k)` is
geometrically normal (for it results then from `(7.5.3)` that the morphism `Spec(B) → Spec(A)` is normal, hence one
concludes by `(6.15.10)`). But even supposing that the residue field of `B` is equal to that of `A` and that `B` is also
complete, we do not know if the answer is affirmative in the general case.*

*(iv) Let us consider the property `𝐑(C)`: "`C` is reduced, equidimensional and verifies `(R_1)`"; it verifies `(R_IV)`,
by virtue of `(5.12.5)`, but it is not known on the other hand whether it verifies `(R_I)`, `(R_II)` or `(R_III)`, the
difficulties coming from the verification of equidimensionality.*

<!-- original page 207 -->

In the sequel of this number, we shall apply `(7.5.1)` to the study of the completed tensor products `A ⊗̂_k B` of
Noetherian local rings that are algebras over a field `k`.

**Lemma (7.5.5).**

<!-- label: IV.7.5.5 -->

*Let `k` be a field, `A`, `B` two complete Noetherian local rings containing `k`, the residue field of `A` being a
finite extension of `k`. Let `C` be the completed tensor product `A ⊗̂_k B` `(0_I, 7.7.5)`. Then:*

*(i) `C` is a complete semi-local Noetherian ring.*

*(ii) `C` is a flat `A`-module and a flat `B`-module.*

*(iii) If `𝔪` is the maximal ideal of `A`, `𝔪C` is contained in the radical of `C`, and `C/𝔪C` is isomorphic to
`(A/𝔪) ⊗_k B`.*

*(iv) The residue fields of the local components of `C` are finite extensions of the residue field of `B`.*

Properties (i), (iii) and the first assertion of (ii) are particular cases of `(0, 19.7.1.2)`. To prove that `C` is a
flat `B`-module, let us note that for every `h > 0`, `C/𝔪^h C = (A/𝔪^h) ⊗_k B` is a flat `B`-module, since `k` is a
field; it therefore suffices to apply `(0_III, 10.2.6)` to each of the local components of `C` (of which `C` is the
direct composite). Finally, if `𝔫` is the maximal ideal of `B`, the residue fields of the local components of `C` are
also those of the local components of the Artinian ring `(A/𝔪) ⊗_k (B/𝔫)`, which, by hypothesis, are finite extensions
of `B/𝔫`.

**Proposition (7.5.6).**

<!-- label: IV.7.5.6 -->

*Let `k` be a field, `A`, `B` two complete Noetherian local rings containing `k`, and whose residue fields are finite
extensions of `k`. Let on the other hand `𝐑` be a property verifying conditions `(R_I)`, `(R_III)` and `(R_IV)` (the
property `𝐏` being defined from `𝐑` by `(7.5.0)`). Suppose that `𝐑(A)` is true, as well as `𝐏(Spec(B), k)` (which
signifies that for every finite extension `k'` of `k` and for each of the complete local rings `B_h` of which `B ⊗_k k'`
is the direct composite, `𝐑(B_h)` is true). Then, for each of the complete local rings `C_j` of which `A ⊗̂_k B` is the
direct composite, `𝐑(C_j)` is true.*

It results from `(7.5.5, (iii))` that each of the homomorphisms `A → C_j` is local and from `(7.5.5, (ii))` that each of
the `C_j` is a flat `A`-module; finally, by `(7.5.5, (iv))`, the residue fields of the `C_j` are finite extensions of
`A/𝔪`. On the other hand, the property `𝐏(Spec(C_j ⊗_A (A/𝔪)), A/𝔪)` is true, since `C/𝔪C = (A/𝔪) ⊗_k B`, and the
assertion results from the definition of `𝐏` and from the hypothesis that `A/𝔪` is a finite extension of `k`. All the
conditions of `(7.5.1)` are therefore verified for the local homomorphisms `A → C_j`, and the corresponding morphisms
`Spec(C_j) → Spec(A)` are therefore `𝐏`-morphisms; the conclusion results then from `(R_I)` and from the hypothesis that
`𝐑(A)` is true.

**Corollary (7.5.7) (Chevalley).**

<!-- label: IV.7.5.7 -->

*Let `k` be a perfect (resp. algebraically closed) field, `A`, `B` two complete Noetherian local rings containing `k`
and whose residue fields are finite extensions of `k`. Then, if `A` and `B` are reduced (resp. integral), the completed
tensor product `A ⊗̂_k B` is reduced (resp. integral).*

I) Suppose `k` perfect, `A` and `B` reduced; let `A_i` (resp. `B_j`) be the quotients of `A` (resp. `B`) by its minimal
prime ideals (`1 ≤ i ≤ r`, `1 ≤ j ≤ s`), which are complete; the hypothesis entails that `A` (resp. `B`) identifies with
a subring of the direct composite of the `A_i` (resp. `B_j`); the tensor products being taken over a field, `A ⊗_k B`
identifies with a subring of the direct composite of the `A_i ⊗_k B_j`, and one verifies at once that the tensor-product
topology of `A ⊗_k B` is induced by the product of the topologies of the `A_i ⊗_k B_j`. It results from this that
`A ⊗̂_k B` identifies with a subring of the direct composite of the `A_i ⊗̂_k B_j`, and one is therefore reduced to the
case where `A` and `B` are integral. Let then `A'` and `B'` be the integral closures of `A` and `B` respectively; one
knows, by Nagata's finiteness theorem `(0, 23.1.6)`, that `A'` (resp. `B'`) is a finite `A`-module (resp. `B`-module)
and a complete local ring. Moreover, `A ⊗̂_k B` identifies with a subring of `A' ⊗̂_k B'`: indeed, it will suffice to
prove that `A ⊗̂_k B` identifies with a subring of `A' ⊗̂_k B`, and the latter with a subring of `A' ⊗̂_k B'`. This
results from the following lemma:

**Lemma (7.5.7.1).**

<!-- label: IV.7.5.7.1 -->

*Let `A`, `B` be two complete Noetherian local rings containing a field `k` and whose residue fields are finite
extensions of `k`. Let `𝔪` be the maximal ideal of `A`. For every `A`-module `M` of finite type (endowed with the
`𝔪`-adic topology), the completed tensor product `M ⊗̂_k B` `(0_I, 7.7.1)` identifies canonically with
`M ⊗_A (A ⊗̂_k B)`.*

Indeed, one has a canonical isomorphism `M ⊗_k B ⥲ M ⊗_A (A ⊗_k B)`, hence a canonical composite homomorphism

```text
   φ : M ⊗_k B  →  M ⊗_A (A ⊗_k B)  →  M ⊗_A (A ⊗̂_k B)
```

and it is immediate that this homomorphism is continuous for the tensor-product topologies; moreover, `M ⊗_A (A ⊗̂_k B)`
is separated and complete (`(7.5.5)` and `(0_I, 7.7.8)`), hence one also has by completion a continuous homomorphism

```text
   φ̂ : M ⊗̂_k B  →  M ⊗_A (A ⊗̂_k B).
```

<!-- original page 208 -->

It is immediate that this homomorphism is bijective when `M` is free of finite type; since one has an exact sequence
`L' → L → M → 0`, where `L` and `L'` are finite free `A`-modules, one deduces from it a commutative diagram

```text
   L' ⊗̂_k B  ──────→  L ⊗̂_k B  ──────→  M ⊗̂_k B  ────→  0

   L' ⊗_A (A ⊗̂_k B) → L ⊗_A (A ⊗̂_k B) → M ⊗_A (A ⊗̂_k B) → 0
```

where the rows are exact (the first by virtue of the definition of the completed tensor product and of `(0_I, 13.2.2)`);
the first two vertical arrows being bijections, the same is so of the third.

The fact that `A ⊗̂_k B` identifies with a subring of `A' ⊗̂_k (A ⊗̂_k B)` results then from the fact that `A` is a
subring of `A'` and that `A ⊗̂_k B` is a flat `A`-module `(7.5.5)`. One may thus suppose moreover that `A` and `B` are
integrally closed; since moreover `k` is assumed perfect, `Spec(A)` and `Spec(B)` are geometrically normal over `k` by
virtue of `(6.7.7, b))`; one can then apply `(7.5.6)` taking for `𝐑` the property (vi) of `(7.5.3)`.

II) Suppose `k` algebraically closed, `A` and `B` integral. The reasoning of I) reduces once again to the case where `A`
and `B` are integrally closed; it then results from `(7.5.6)` that `Spec(A ⊗̂_k B)` is normal, hence `A ⊗̂_k B` is a
direct composite of integrally closed complete local rings, and everything comes down to seeing that `A ⊗̂_k B` is a
local ring. It suffices for this to verify that if `𝔪` and `𝔫` are the maximal ideals of `A` and `B`, `(A/𝔪) ⊗_k (B/𝔫)`
is a local ring (see proof of `(0, 19.7.1.2)`); but since `A/𝔪` and `B/𝔫` are finite extensions of `k`, they are
identical to `k`, whence the conclusion.

**Remark (7.5.8).**

<!-- label: IV.7.5.8 -->

*It would be interesting to determine whether, in `(7.5.7)`, one can replace the hypothesis that `k` is perfect or
algebraically closed by the hypothesis that `Spec(A)` or `Spec(B)` is geometrically integral over `k`, or at least by
the hypothesis that `A` (for example) is integral and contains a subring `A_0` isomorphic to a ring of formal series
`k[[T_1, …, T_n]]`, such that the field of fractions `K` of `A` is separable over the field of fractions `K_0` of `A_0`
(one can show that this condition entails that `A` is geometrically integral over `k`, and that the two properties are
equivalent when `[k : k^p]` is finite (`p` being the characteristic exponent of `k`)). Likewise, it would be desirable
to develop variants of `(7.5.6)` and `(7.5.7)` in which one would weaken the hypothesis of finiteness of the residue
fields of `A` and `B`, by supposing for example that only one of them is a finite extension of `k`, the other being
arbitrary.*

### 7.6. Applications: I. Local Japanese rings.

**Proposition (7.6.1).**

<!-- label: IV.7.6.1 -->

*Let `A` be a reduced Noetherian local ring whose formal fibres are geometrically normal. Then the completion `Â` is
reduced, the integral closure `A'` of `A` in its total ring of fractions is a finite `A`-algebra (hence a semi-local
Noetherian ring) and its completion `Â'` is isomorphic to the integral closure of `Â` in its total ring of fractions.*

The formal fibres of `A` are a fortiori geometrically reduced, hence the hypothesis that `A` is reduced entails that the
same is so of `Â`, by virtue of `(7.3.17)`. Let `p_i` `(1 ≤ i ≤ n)` be the minimal prime ideals of `A`, and set
`B_i = A/p_i`; the formal fibres of the local rings `B_i` are then also geometrically normal `(7.3.15)`, hence the
`B̂_i` are also reduced and it results from `(0, 23.1.7, (i))` that the integral closure `B'_i` of `B_i` in its field of
fractions is a `B_i`-module of finite type, hence an `A`-module of finite type; since `A'` is the direct composite of
the `B'_i` `(II, 6.3.8)`, one sees that `A'` is an `A`-module of finite type. Let `𝔪_j` `(1 ≤ j ≤ r)` be the maximal
ideals of the semi-local ring `A'`; one knows that the completion `Â'` of `A'` identifies with the direct composite of
the completions `Â'_{𝔪_j}` of the `A'_{𝔪_j}` (Bourbaki, *Alg. comm.*, chap. III, §2, n° 13, cor. of prop. 19).

<!-- original page 209 -->

Now, it results from the hypothesis and from `(7.3.15)` that the formal fibres of the `A'_{𝔪_j}` are geometrically
normal; since `Spec(A')` is normal by definition, the same is so of the `Spec(A'_{𝔪_j})`, and one deduces therefore from
`(7.3.17)` that `Spec(Â'_{𝔪_j})` is normal for every `j`, hence also `Spec(Â')`. On the other hand (Bourbaki, *Alg.
comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9 and chap. III, §3, n° 4, th. 3), `Â'` identifies with `A' ⊗_A Â` since
`A'` is an `A`-module of finite type; since `A'` contains `A` and is contained in the total ring of fractions `R` of
`A`, and since `Â` is a flat `A`-module, `Â'` contains `Â` and is contained in `R' = R ⊗_A Â`; finally, since `Â` is a
flat `A`-module, every regular element of `A` is also `Â`-regular `(0_I, 6.3.4)`; hence `R'` identifies canonically with
a subring of the total ring of fractions `R''` of `Â` (Bourbaki, *Alg. comm.*, chap. II, §2, n° 1, Remark 7). Since
`Spec(Â')` is normal and `Â'` is an `Â`-module of finite type, `Â'` is indeed the integral closure of `Â` in `R''`.

**Corollary (7.6.2).**

<!-- label: IV.7.6.2 -->

*Under the hypotheses of `(7.6.1)`, there is a canonical bijective correspondence between the set of maximal ideals
`𝔪_j` of `A'` (in other words, the set of points of `Spec(A')` above the closed point of `A`) and the set of minimal
prime ideals `𝔮_j` of `Â` (in other words, the set of maximal points of `Spec(Â)`); in this correspondence, the
completion `Â'_{𝔪_j}` of `A'_{𝔪_j}` is isomorphic to the integral closure of `Â/𝔮_j`.*

One knows indeed that the integral closure of `Â` in its total ring of fractions is the direct composite of the integral
closures of the `Â/𝔮_j`, which are complete local rings `(0, 23.1.6)`.

**Corollary (7.6.3).**

<!-- label: IV.7.6.3 -->

*Under the hypotheses of `(7.6.1)`, in order that `A` be integral, it is necessary and sufficient that `Â` be unibranch;
in order that `A` be geometrically unibranch, it is necessary and sufficient that `Â` be so.*

This is a particular case of `(7.6.2)`.

**Theorem (7.6.4) (Zariski-Nagata).**

<!-- label: IV.7.6.4 -->

*Let `A` be a semi-local Noetherian ring. The following conditions are equivalent:*

*a) For every reduced finite `A`-algebra `C`, the completion `Ĉ` is a reduced ring.*

*a') For every integral quotient ring `B` of `A`, of field of fractions `K`, the completion `B̂` is reduced, and the
component fields `L_j` of the total ring of fractions of `B̂` are separable extensions of `K`.*

*a'') The formal fibres of `A` are geometrically reduced (in other words, for every integral quotient ring `B` of `A`,
of field of fractions `K`, the `K`-algebra `B̂ ⊗_B K` is separable `(4.6.2)`).*

*b) Every integral quotient ring `B` of `A` is a Japanese ring.*

To show that a) entails a'), it suffices to verify that the `L_j` are separable extensions of `K`, or again `(4.6.1)`
that for every finite extension `K'` of `K`, the ring `B̂ ⊗_B K'` is reduced; now `K'` is generated by a finite number
of elements integral over `B`, and these last generate a finite sub-`B`-algebra `B'` of `K'`, of which `K'` is the field
of fractions. One has `B̂' = B̂ ⊗_B B'` (`(0_I, 7.3.3)` and Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop.
9),

<!-- original page 210 -->

hence `B̂ ⊗_B K' = B̂' ⊗_{B'} K'` by associativity of the tensor product; but `B'` is a finite integral `A`-algebra,
hence `B̂'` is a reduced ring by virtue of a), and since `B̂'` is a flat `B'`-module, the elements `≠ 0` of `B'` are
`B̂'`-regular, which entails that `B̂' ⊗_{B'} K'` identifies with a subring of the total ring of fractions of `B̂'`, and
a fortiori is reduced.

To see that a') entails a''), let us consider an arbitrary point `x` of `X = Spec(A)`, and let `Y` be the integral
closed sub-scheme of `X` having `{x}` for underlying space; one has `Y = Spec(B)`, where `B` is an integral quotient
ring of `A`, and `Spec(B̂) = Y ×_X Spec(Â)`, so that the formal fibre of `A` at the point `x` is the same as that of
`B`, or again is equal to `Spec(B̂ ⊗_B K)`. Since the local rings of `Spec(B̂ ⊗_B K)` are those of `Spec(B̂)` at the
points of the fibre of `x`, the hypothesis entails that `B̂ ⊗_B K` is reduced, and the conditions of a') entail
therefore that `B̂ ⊗_B K` is a separable `K`-algebra `(4.6.1)`.

The condition a'') entails a), for it results from `(7.3.15)` that the formal fibres of `C` are then geometrically
reduced, and if `C` is reduced, the same is then so of `Ĉ` (particular case of `(7.3.17)`).

The fact that a') implies b) is a particular case of `(0, 23.1.7)`. It therefore remains to prove that b) entails a).
Let us note that if `C` is a finite `A`-algebra, for every prime ideal `𝔮` of `C`, the inverse image `𝔭` of `𝔮` in `A`
is a prime ideal and `C/𝔮` is a finite `(A/𝔭)`-algebra, hence hypothesis b) entails that every integral quotient ring of
`C` is a Japanese ring. One is thus reduced to proving that under hypothesis b), the completion of every integral
quotient of `A` is reduced. Let us reason by induction on `n = dim(A)`, the assertion being trivial for `n = 0`; by
replacing `A` by the quotients of `A` by its minimal prime ideals `p_i`, one can restrict to the case where `A` is
integral (every integral quotient of `A` being a quotient of one of the `A/p_i`). For every prime ideal `p ≠ 0`, the
induction hypothesis shows already that the completion of `A/p` is reduced, and it therefore suffices to prove that `Â`
is reduced. Moreover, the integral closure `A'` of `A` is by hypothesis an `A`-module of finite type, hence a semi-local
Noetherian ring, and `Â` identifies with a subring of `Â'` (`(0_I, 7.3.3)` and Bourbaki, *Alg. comm.*, chap. IV, §2, n°
5, cor. 3 of prop. 9); it will therefore suffice to prove that `Â'` is reduced; one has seen above that hypothesis b) is
also verified by `A'`, which is moreover of dimension `n` `(0, 16.1.5)`; one may therefore restrict to the case where
`A` is integrally closed. Let `t ≠ 0` be an element of the radical of `A`, and let `𝔮_j` `(1 ≤ j ≤ n)` be the prime
ideals minimal among those containing `tA`; one has the following properties:

*(i) `t` is regular.*

*(ii) `A/tA` has no embedded associated prime ideals.*

*(iii) The `A_{𝔮_j}` are discrete valuation rings.*

*(iv) The completions of the `A/𝔮_j` are reduced.*

Indeed, (i) is trivial since `A` is integral and `t ≠ 0`. Since `A` is integrally closed, `A/tA` verifies `(S_1)`, that
is `(5.7.7)` has no embedded associated prime ideals (Bourbaki, *Alg. comm.*, chap. VII, §1, n° 4, prop. 8). Still
because `A` is integrally closed, the `A_{𝔮_j}` are so and one knows (*loc. cit.*) that these rings are of dimension
`1`,

<!-- original page 211 -->

hence are discrete valuation rings, whence (iii). Finally, (iv) comes from the induction hypothesis. The proof will be
finished if we prove the

**Lemma (7.6.4.1) (Zariski).**

<!-- label: IV.7.6.4.1 -->

*Let `A` be a semi-local Noetherian ring, `t` an element of its radical verifying conditions (i) to (iv) above; then `Â`
is reduced.*

Let us set for simplicity `A' = Â`, and consider `t` as an element of `A'`; one has `A'/tA' = (A/tA) ⊗_A A'`, and since
`A'` is a flat `A`-module, it results from `(3.3.1)` that the prime ideals of `A'` associated with the `A'`-module
`A'/tA'` are the prime ideals `𝔮'_h` such that `𝔮'_h` lies above `𝔮_j` and associated with the `𝒌_j`-module
`(A'/tA') ⊗_A 𝒌_j`, where `𝒌_j` is the field of fractions of `A/𝔮_j`. Now, `Spec((A'/tA') ⊗_A 𝒌_j)` is the formal fibre
of `A` at the point `𝔮_j`, or also that of `A/𝔮_j` at the point `𝔮_j` (generic point of `Spec(A/𝔮_j)`). Since by virtue
of (iv) the completion `A'/𝔮_j A'` of `A/𝔮_j` is reduced, the same is so of the formal fibre of `A/𝔮_j` at the generic
point of `Spec(A/𝔮_j)`; this formal fibre has therefore no embedded associated prime cycle and its local rings at the
generic points `𝔮'_h` of its irreducible components are fields `(3.2.1)`. One sees therefore by `(3.3.3)` and hypothesis
(ii) that `A'/tA'` has no embedded associated prime ideals, and on the other hand that `𝔮_j A'_{𝔮'_h}` is the maximal
ideal of `A'_{𝔮'_h}` for every `h`; since `A_{𝔮_j}` is a discrete valuation ring, its maximal ideal `𝔮_j A_{𝔮_j}` is
principal, hence the maximal ideal of the Noetherian local ring `A'_{𝔮'_h}` is principal, which entails that this ring
is a discrete valuation ring (Bourbaki, *Alg. comm.*, chap. VI, §3, n° 6, prop. 9). We have thus verified hypotheses (i)
to (iv) for the complete local ring `A'`. It therefore suffices to show that if `A` is complete and verifies hypotheses
(i) to (iii) ((iv) being automatic in this case), then `A` is reduced. Now, hypotheses (i) and (ii) imply that, if
`φ : A → ∏_{j=1}^n A_{𝔮_j}` is the canonical homomorphism, one has `tA = φ⁻¹(φ(tA))` `(3.4.9)`; since the canonical
image of `tA` in the discrete valuation ring `A_{𝔮_j}` is a power `𝔮_j^{n_j} A_{𝔮_j}` of the maximal ideal, one sees
that on `A` the `(tA)`-preadic topology is the inverse image by `φ` of the product topology on `∏_{j=1}^n A_{𝔮_j}`. Now,
since `t` belongs to the radical of `A`, the `(tA)`-preadic topology is separated, hence `φ` is injective. But by virtue
of hypothesis (iii), the `A_{𝔮_j}` are integral, hence `∏_{j=1}^n A_{𝔮_j}` is reduced, and a fortiori the same is so of
`A`. Q.E.D.

**Corollary (7.6.5).**

<!-- label: IV.7.6.5 -->

*Let `A` be a semi-local Noetherian ring verifying the equivalent conditions of `(7.6.4)`; every semi-local `A`-algebra
essentially of finite type also verifies the conditions of `(7.6.4)`.*

Condition a'') of `(7.6.4)` signifies indeed that `A` is a `𝐏`-ring, where `𝐏(Z, k)` is the property "`Z` is
geometrically reduced over `k`"; the corollary is therefore a consequence of the general theorem `(7.4.4)`.

**Corollary (7.6.6).**

<!-- label: IV.7.6.6 -->

*Let `A` be a semi-local Noetherian integral ring of dimension `1`, `K` its field of fractions. In order that `A` be a
Japanese ring, it is necessary and sufficient that the completion `Â`*

<!-- original page 212 -->

*of `A` be reduced and that, if `𝔮_j` `(1 ≤ j ≤ n)` are the minimal prime ideals of `Â`, the fields of fractions of the
integral rings `Â/𝔮_j` be separable extensions of `K`.*

The integral quotients of `A` are indeed `A` itself and fields, hence condition b) of `(7.6.4)` is equivalent to the
hypothesis that `A` is a Japanese ring, and hypothesis a') to the conditions of the statement on `Â`, whence the
conclusion.

**Remarks (7.6.7).**

<!-- label: IV.7.6.7 -->

*(i) The equivalent conditions of `(7.6.6)` signify again that the formal fibres of `A` are geometrically regular
`(7.3.19, (iv))`. One has already observed (*loc. cit.*) that this condition is verified when `A` is a discrete
valuation ring whose field of fractions is of characteristic `0`.*

*(ii) The same reasoning as in the first part of the proof of `(7.6.4)` shows that for a semi-local Noetherian ring `A`,
the two following conditions are equivalent:*

*a) For every integral quotient ring `B` of `A`, the completion `B̂` is reduced.*

*a') The formal fibres of `A` are reduced.*

*Taking account of `(0, 23.1.7, (i))`, these two conditions imply the following:*

*b) For every integral quotient ring `B` of `A`, the integral closure of `B` is a finite `B`-algebra.*

*When `A` is a universally catenary ring, one can prove that condition b) entails conversely a'); we shall have no need
to use this result.*

### 7.7. Applications: II. Universally Japanese rings.

**(7.7.1)** Recall `(0, 23.1.1)` that one calls **universally Japanese ring** a ring `A` such that every integral
`A`-algebra of finite type is a Japanese ring. It comes to the same to say that for every integral `A`-algebra of finite
type `B`, the integral closure of `B` is a finite `B`-algebra.

**Theorem (7.7.2) (Nagata).**

<!-- label: IV.7.7.2 -->

*Let `A` be a Noetherian ring. The following conditions are equivalent:*

*a) `A` is a universally Japanese ring.*

*b) Every integral quotient ring of `A` is a Japanese ring.*

*c) For every maximal ideal `𝔪` of `A`, every integral quotient ring of `A_𝔪` is a Japanese ring, and for every integral
quotient ring `B` of `A`, of field of fractions `K`, every finite radicial extension `K'` of `K` and every finite
sub-`B`-algebra `B'` of `K'`, of field of fractions `K'`, there exists `f ≠ 0` in `B'` such that `B'_f` be integrally
closed (cf. `(6.13.7)`).*

*Moreover, if `A` verifies these conditions, the same is so of every ring of fractions `S⁻¹A` of `A` and of every
`A`-algebra of finite type.*

Let us first show that b) entails c); every integral quotient ring of `A_𝔪` is a ring of fractions of an integral
quotient ring of `A`, hence a Japanese ring `(0, 23.1.1)`. On the other hand, every quotient `B` of `A` by one of its
prime ideals is a Japanese ring, hence the same is so of `B'` `(0, 23.1.1)`. One deduces from this that the set
`Nor(Spec(B'))` is open `(6.13.3)`, hence contains a non-empty open set `D(f') = Spec(B'_{f'})`.

<!-- original page 213 -->

Let us show in the second place that if `A` verifies c), the same is so of every `A`-algebra of finite type `B`. In the
first place, for every prime ideal `𝔮` of `B`, `B_𝔮` is the local ring at a prime ideal of `S⁻¹B`, where `S = A - 𝔭`,
`𝔭` being the inverse image of `𝔮` in `A`; since by hypothesis every integral quotient ring of `A_𝔭` is a Japanese ring,
the same is so of every integral quotient ring of `B_𝔮`, since `S⁻¹B` is an `A_𝔭`-algebra of finite type `(7.6.5)`. On
the other hand, if `C` is an integral quotient of `B`, of field of fractions `K`, `K'` a finite radicial extension of
`K` and `C'` a finite sub-`C`-algebra of `K'`, of field of fractions `K'`, `C'` is an integral `A`-algebra of finite
type, and by virtue of `(6.13.7)`, hypothesis c) on `A` entails that the spectrum of `C'` contains a non-empty open part
all of whose points are normal; in other words, there is a `g' ≠ 0` in `C'` such that `C'_{g'}` be integrally closed,
which proves our assertion.

This result shows that, to prove the equivalence of a), b) and c), it suffices to show that c) entails b), and even to
prove that for every integral quotient ring `B` of `A`, of field of fractions `K`, the integral closure `B'` is a
`B`-module of finite type. Now, condition c) entails that there exists `f ≠ 0` in `B` such that `B_f` be integrally
closed, and one has thus verified for `B` condition (i) of `(6.13.6)`. On the other hand, condition (ii) of `(6.13.6)`
is also verified by `B`; indeed, for every maximal ideal `𝔮` of `B`, `B_𝔮` is a quotient of a local ring `A_𝔭`, where
`𝔭` is maximal in `A`; since `A_𝔭` is by hypothesis a Japanese ring, the same is so of `B_𝔮`; moreover, for every prime
ideal `𝔯` of `B`, `B_𝔯` is a ring of fractions of a `B_𝔮`, where `𝔮` is a maximal ideal of `B`, hence is again a
Japanese ring, which proves our assertion.

One has moreover seen above that if `A` verifies the equivalent conditions a), b), c), the same is so of every
`A`-algebra of finite type. On the other hand, if `A` verifies b), the same is so of every ring of fractions `S⁻¹A`, for
every integral quotient of `S⁻¹A` is of the form `S⁻¹A / S⁻¹𝔭`, where `𝔭` is a prime ideal of `A`, and since `A/𝔭` is by
hypothesis a Japanese ring, the same is so of `S⁻¹(A/𝔭)` `(0, 23.1.1)`. This completes the proof of the last assertion
of the statement.

**Corollary (7.7.3).**

<!-- label: IV.7.7.3 -->

*Let `A` be a Noetherian ring verifying the following conditions:*

*(i) For every maximal ideal `𝔪` of `A`, the formal fibres of `A_𝔪` are geometrically reduced.*

*(ii) The equivalent conditions of `(6.12.4)` are verified.*

*Then `A` is universally Japanese.*

Indeed, it results then from `(7.6.4)` that every integral quotient ring of `A_𝔪` is a Japanese ring; whence the
conclusion, by virtue of `(7.7.2)`.

**Corollary (7.7.4).**

<!-- label: IV.7.7.4 -->

*A Dedekind ring whose field of fractions is of characteristic `0` (in particular `ℤ`) is a universally Japanese ring. A
Noetherian local ring whose formal fibres are geometrically reduced (in particular a complete Noetherian local ring) is
universally Japanese.*

The first assertion results from `(7.7.3)`, `(7.6.7, (i))` and `(6.12.6)`. The second results from `(7.6.4)` and
`(7.7.2)`.

<!-- original page 214 -->

### 7.8. Excellent rings.

**(7.8.1)** The preceding numbers of this section (as well as `(6.11)`, `(6.12)` and `(6.13)`) have been devoted to the
study of problems one frequently encounters in the use of Noetherian rings and preschemes, and which can be grouped in
the following types:

A) For a Noetherian local ring `A`, are the properties of `A` "transmitted" to its completion `Â`? For example, if `A`
is reduced (resp. integral, resp. integral and integrally closed), is the same so of `Â`? Most of these questions are
linked to the local properties of the formal fibres of `A` (let us recall that these are the fibres of the canonical
morphism `Spec(Â) → Spec(A)`). An exception is formed by the properties linked to the notion of dimension, for example
the property of being equidimensional; it is then the chain condition and its various refinements that play the
essential role.

B) For a locally Noetherian prescheme `X` (in particular for an affine scheme `Spec(A)`), is the set of `x ∈ X` where
the local ring `𝒪_x` possesses a certain property (for instance being integrally closed, or Cohen-Macaulay, or regular)
open?

C) For an integral ring `A`, is the integral closure of `A` in a finite extension of its field of fractions an
`A`-module of finite type? Of course, this question can be translated for Noetherian preschemes `(II, 6.3)`.

The problems of type B) or C) can also be posed for local rings, but it does not in general suffice that they be
resolved affirmatively for every local ring `A_𝔭` of a ring `A` for them to be so for `A` (cf. `(6.13.6)`).

Let us emphasize moreover that in the study of these problems, we have systematically been concerned with whether the
affirmative answer to one of them is stable under the two most important operations of commutative algebra: localization
and passage to an algebra of finite type.

The results obtained in the study of these problems lead one to single out the definition of a class of Noetherian rings
whose behaviour in this regard is the best possible:

**Definition (7.8.2).**

<!-- label: IV.7.8.2 -->

*One says that a ring `A` is **excellent** if it is Noetherian and verifies the following conditions:*

*(i) `A` is universally catenary (or, what comes to the same `(5.6.3, (i))`, for every prime ideal `𝔭` of `A`, `A_𝔭` is
universally catenary).*

*(ii) For every prime ideal `𝔭` of `A`, the formal fibres of `A_𝔭` are geometrically regular.*

*(iii) For every integral quotient ring `B` of `A` and every finite radicial extension `K'` of the field of fractions
`K` of `B`, there exists a finite sub-`B`-algebra `B'` of `K'`, containing `B`, having `K'` for field of fractions, and
such that the set of regular points of `Spec(B')` contains a non-empty open set.*

With this terminology, the essential part of the results of §7 and of a part of §6 is then summarized as follows:

**Scholium (7.8.3).**

<!-- label: IV.7.8.3 -->

*(i) In conditions (i) and (ii) of definition `(7.8.2)` one may restrict to the ideals `𝔭` maximal in `A`. In order that
a Noetherian local ring be excellent, it is necessary and*

<!-- original page 215 -->

*sufficient that it be universally catenary and that its formal fibres be geometrically regular.*

*(ii) If `A` is an excellent ring, the same is so of every ring of fractions `S⁻¹A` and of every `A`-algebra of finite
type.*

*(iii) A complete local ring (in particular a field) is excellent. A Dedekind ring whose field of fractions is of
characteristic `0` (in particular `ℤ`) is excellent.*

*(iv) Let `A` be an excellent ring, `X = Spec(A)`; the set `Reg(X)` (resp. `Nor(X)`, `U_{𝐑_k}(X)`) of points where `X`
is regular (resp. normal, resp. verifies `(R_k)`) is open in `X`. For every coherent `𝒪_X`-Module `ℱ`, the set
`U_{C_n}(ℱ)` (resp. `U_{S_k}(ℱ)`, `CM(ℱ)`) of `x ∈ X` where `coprof(ℱ) ≤ n` (resp. of points where `ℱ` verifies `(S_k)`,
resp. of points where `ℱ` is a Cohen-Macaulay `𝒪_X`-Module) is open in `X`.*

*(v) Let `A` be an excellent ring, `𝔍` an ideal of `A`, `Â` the separated completion of `A` for the `𝔍`-preadic
topology. Then the canonical morphism `f : Spec(Â) → Spec(A)` is regular (in other words, flat and with geometrically
regular fibres). If one sets `X = Spec(A)`, `X' = Spec(Â)`, one has (with the notations of (iv) and setting
`ℱ' = ℱ ⊗_{𝒪_X} 𝒪_{X'}`),*

```text
(7.8.3.1)
   Reg(X') = f⁻¹(Reg(X)),     Nor(X') = f⁻¹(Nor(X)),         U_{𝐑_k}(X') = f⁻¹(U_{𝐑_k}(X))
   U_{C_n}(ℱ') = f⁻¹(U_{C_n}(ℱ)),  U_{S_k}(ℱ') = f⁻¹(U_{S_k}(ℱ)),  CM(ℱ') = f⁻¹(CM(ℱ))
```

*In particular, if `𝔍` is contained in the radical of `A` (for example if `A` is local and `𝔍` its maximal ideal), in
order that `A` be regular (resp. normal, resp. reduced, resp. verifies `(R_k)`, resp. be of codepth `≤ n`, resp.
verifies `(S_k)`, resp. be a Cohen-Macaulay ring), it is necessary and sufficient that the same be so of `Â`; in
particular, in order that `A` have no embedded associated prime ideals, it is necessary and sufficient that the same be
so of `Â`.*

*(vi) An excellent ring `A` is universally Japanese; in particular, if `A` is integral, its integral closure in every
finite extension of its field of fractions is a finite `A`-algebra.*

*(vii) Let `A` be a reduced excellent local ring. Then the completion `Â` is reduced, the integral closure `A'` of `A`
in its total ring of fractions is a finite `A`-algebra (hence a semi-local ring), and the integral closure of `Â` in its
total ring of fractions is isomorphic to the completion `Â'` of `A'`. Moreover, there is a canonical bijective
correspondence between the set of maximal points of `Spec(Â)` (in other words, the set of minimal prime ideals of `Â`)
and the set of closed points of `Spec(A')` (in other words, the set of maximal ideals of `A'`). In order that the local
ring `A` be unibranch, it is necessary and sufficient that `Â` be integral; in order that `A` be geometrically
unibranch, it is necessary and sufficient that `Â` be so.*

*(viii) If `A` is an excellent integral ring, the integral closure of `A` is the intersection of the integral closures
of the rings `A_𝔭`, where `𝔭` runs over the set of prime ideals of `A` of height `1`.*

*(ix) Let `A` be an excellent ring, `X = Spec(A)`, `Z` a closed part of `X`, `U = X − Z`, `i : U → X` the canonical
injection, `ℱ` a coherent `𝒪_X`-Module. In order that the `𝒪_X`-Module `i_*(ℱ|U)` be coherent, it is necessary and
sufficient that, for every `x ∈ Ass(ℱ)`, one have `codim(‾{x} ∩ Z, ‾{x}) ≥ 2`. In particular, if `A` is integral and `ℱ`
torsion-free, in order that `i_*(ℱ|U)` be coherent, it is necessary and sufficient that `codim(Z, X) ≥ 2`.*

<!-- original page 216 -->

*(x) Let `A` be an excellent local ring. For every integral quotient ring `B` of `A`, `B̂` is equidimensional. In order
that `A` be equidimensional, it is necessary and sufficient that `Â` be so.*

Most of these results have already been proved.

(i) The first assertion results from `(5.6.3, (i))` and `(7.4.4, (i))`; the second, from `(7.4.4)`, `(7.3.18)`,
`(6.12.7)` and `(6.12.4)`.

Assertion (ii) results from `(5.6.1)`, `(5.6.3, (i))`, `(7.4.4)` and `(6.12.4)`.

(iii) The first assertion was seen in `(5.6.4)` and `(7.4.4)`, taking account of (i). The second was seen in `(5.6.4)`
and `(7.3.19, (iv))`, taking account of (i).

Assertion (iv) results from `(6.12.4)`, `(6.13.5)`, `(6.12.9)` and `(6.11.8)` (taking account of (ii)).

The first assertion of (v) is a consequence of `(7.4.6)`; the relations `(7.8.3.1)` follow from it, taking account
respectively of `(6.5.1)`, `(6.5.4)`, `(6.5.3)`, `(6.3.5)` and `(6.4.2)`. The last assertion of (v) is the particular
case corresponding to property `(S_k)` for `n = 1` `(5.7.5)`.

Assertion (vi) results from `(7.7.3)`, and assertion (vii) from `(7.6.1)`, `(7.6.2)` and `(7.6.3)`. To prove (viii), let
us note that the ring `A^{(1)}`, intersection of the `A_𝔭` for all the prime ideals `𝔭` of height `1` of `A`, is a
finite `A`-algebra, as results from (vi), from `(7.8.2, (i))` and from `(5.11.2)`. Since the integral closure `A'` of
`A` is a finite `A`-algebra, the prime ideals of height `1` of `A'` are exactly those that lie above the prime ideals of
height `1` of `A` `(5.10.17, (iv))`; the conclusion results therefore from `(0, 23.2.9)`.

The first assertion of (ix) is a consequence of (vi) and of `(5.11.4)`; the second is a particular case of it, if one
observes that when `ℱ` is torsion-free, `Ass(ℱ)` is reduced to the generic point of `Spec(A)`. Finally, to prove (x), it
suffices to observe that `B` is an excellent local ring by (ii); since `B` is universally catenary and universally
Japanese by virtue of (vi), the ring `B^{(1)}` is a finite `B`-algebra `(5.11.2)`, which shows that `A` is strictly
formally catenary by `(7.2.5, c))` and finishes the proof of (x).

**Remarks (7.8.4).**

<!-- label: IV.7.8.4 -->

*(i) If one considers the Noetherian rings `A` that verify only conditions (ii) and (iii) of definition `(7.8.2)`, one
verifies by inspection of the preceding proofs that the assertions (ii), (iii), (iv), (v), (vi) and (vii) of `(7.8.3)`
are still valid, replacing "excellent" by "verifying" `(7.8.2, (ii) and (iii))`.*

*(ii) The catenary local ring `A` constructed in `(5.6.11)` verifies conditions (ii) and (iii) (but not condition (i))
of definition `(7.8.2)`. Indeed, the formal fibre at the maximal ideal `𝔫𝒪_A` of `A` is trivially geometrically regular,
and that at the other prime ideals `𝔭` of `A` coincides with that of the ring `E` at these prime ideals; now `E` is a
`V`-algebra of finite type and `V` is a discrete valuation ring, which is consequently an excellent ring if one takes
the field `k_0` of characteristic `0` `(7.8.3, (iii))`; consequently `E` is an excellent ring `(7.8.3, (ii))` and this
therefore proves that `A` verifies condition `(7.8.2, (ii))`. On the other hand, the complement of the closed point in
`Spec(A)` is isomorphic to an open part of `Spec(E)`, of which an affine open part is the spectrum of an excellent*

<!-- original page 217 -->

*ring, hence verifies condition `(6.12.4, a))` by virtue of `(7.8.3, (v))`; this proves that `A` itself verifies the
condition of `(6.12.4, a))`, hence also `(6.12.4, c))`, which is none other than condition `(7.8.2, (iii))`. Yet `A`
does not satisfy condition `(7.8.2, (i))`, since we have seen `(5.6.11)` that it is not universally catenary.*

*(iii) One may replace condition (i) of definition `(7.8.2)` by the following (apparently weaker, taking account of
`(5.6.10)`):*

*`(i')` For every minimal prime ideal `𝔭_i` of `A` `(1 ≤ i ≤ r)`, let `A'_i` be the integral closure of the integral
ring `A_i = A/𝔭_i`; then, for every maximal ideal `𝔪'` of `A'_i`, one has, designating by `𝔪` the inverse image of `𝔪'`
in `A`,*

```text
(7.8.4.1)                            dim(A_𝔪) = dim((A'_i)_{𝔪'}).
```

Indeed, one has seen (Remark (i)) that under the sole hypotheses (ii) and (iii) of `(7.8.2)`, the analogues of
properties (ii), (v), (vi) and (vii) of `(7.8.3)` are valid. One deduces therefore first from (vi) and (ii) that the
`A'_i` verify `(7.8.2, (ii) and (iii))`; it follows then from (v) that the completions `((A'_i)_{𝔪'})^` are integral
(and integrally closed). Let now `𝔪` be an arbitrary maximal ideal of `A`; for every `i` such that `𝔭_i ⊂ 𝔪`, the
integral closure of `A_𝔪/𝔭_i A_𝔪` is a `(A_𝔪/𝔭_i A_𝔪)`-algebra finite by (vi), hence semi-local, and its local
components are of the form `(A'_i)_{𝔪'}`, where `𝔪'` is a prime ideal (necessarily maximal) of `A'_i` above `𝔪/𝔭_i`; it
results then from (vii), from what precedes and from `(7.8.4.1)` that the quotients of the completion `(A_𝔪/𝔭_i A_𝔪)^`
by its minimal prime ideals all have the same dimension equal to `dim(A_𝔪)`. Consequently (`7.1.9` and `7.1.8, b)`),
`A_𝔪` is formally catenary, and a fortiori `(7.1.11)` universally catenary; the same is therefore so of `A_𝔭` for every
prime ideal `𝔭` of `A` `(5.6.3, (i))`, hence also of `A`.

In particular, if `A` is normal, or more generally if `A_𝔪` is unibranch for every maximal ideal `𝔪` of `A`, condition
`(i')` is always fulfilled, since `𝔪` can contain only a single prime ideal `𝔭_i` `(0, 16.1.5)`; one may in this case
omit (i) in definition `(7.8.2)`. More particularly, *if `A` is a unibranch Noetherian local ring, it is excellent if
and only if its formal fibres are geometrically regular*.

*(iv) Let us recall that a quotient ring of a local Cohen-Macaulay ring (and a fortiori a quotient ring of a local
regular ring) also verifies the properties `(7.8.3, (ix) and (x))` by virtue of `(7.2.7)`; but the interest of the
quotients of regular rings resides above all in their cohomological properties (chap. III, 3rd Part).*

*(v) We shall see further on (§18) that if `k` is a non-discrete complete valued field, the ring `k{{T_1, …, T_n}}` of
convergent power series (in a neighbourhood of `0` in `k^n`) is an excellent ring.*

**(7.8.5)** One says that a locally Noetherian prescheme `X` is **excellent** if for one cover `(U_α)` of `X` formed of
affine open sets, each of the rings `A_α` of the `U_α` is excellent; this property is then true for every cover `(U_α)`
of `X` formed of affine open sets.

**Proposition (7.8.6).**

<!-- label: IV.7.8.6 -->

*Let `X` be an excellent prescheme.*

*(i) If `f : X' → X` is a locally finite-type morphism, `X'` is excellent.*

<!-- original page 218 -->

*(ii) If `X` is reduced, its normalization `X'` `(II, 6.3.8)` is finite over `X`.*

*(iii) The sets `Reg(X)`, `Nor(X)`, `U_{𝐑_k}(X)` are open in `X`, as well as `U_{C_n}(ℱ)`, `U_{S_k}(ℱ)` and `CM(ℱ)` for
every coherent `𝒪_X`-Module `ℱ`.*

This results at once from `(7.8.3, (ii), (vi) and (iv))`. Let us note also that `(7.8.3, (ix))` is valid without
modification of statement when `X` is an excellent prescheme.

### 7.9. Excellent rings and resolution of singularities.

**(7.9.1)** Given a locally Noetherian reduced prescheme `X`, one calls **resolving morphism** for `X` a morphism
`f : X' → X` such that `X'` is regular and `f` is proper and birational. When such a morphism exists, one says that one
can **resolve the singularities** of `X` (or more simply that one can **resolve `X`**). For instance, if `A` is a
Japanese ring of dimension `1`, one can resolve `X = Spec(A)` since the morphism `X' → X` (where `X'` is the
normalization of `X`) is finite (hence proper) and birational, and the local rings of `X'` are integrally closed rings
of dimension `1`, hence discrete valuation rings, and are consequently regular.

**(7.9.2)** It is clear that if one can resolve `X`, one can also resolve every prescheme induced on an open set of `X`
and every local prescheme `Spec(𝒪_x)` of `X` `(II, 5.4.2)`. On the other hand, if one can resolve `X`, it is clear that
there exists in `X` an open set everywhere dense contained in `Reg(X)`. These remarks show at once that if, for every
integral closed sub-prescheme `Y` of `X` and every `Y`-prescheme `Y'` integral, finite and radicial over `Y`, one can
resolve `Y'`, then the affine open sets of `X` verify condition (iii) of `(7.8.2)`.

On the other hand, for local schemes, one has the following proposition:

**Proposition (7.9.3).**

<!-- label: IV.7.9.3 -->

*Let `A` be a reduced Noetherian local ring, and suppose that one can resolve `Spec(A)`. Then the fibres of the
canonical morphism `Spec(Â) → Spec(A)` at the maximal points of `Spec(A)` are regular.*

Set `X = Spec(A)`, `X' = Spec(Â)`, and let `g : X' → X` be the canonical morphism. Let `f : Y → X` be a resolving
morphism; set `Y' = X' ×_X Y`, and let `f' : Y' → X'` and `g' : Y' → Y` be the canonical projections, so that one has a
commutative diagram

```text
                X' ←──f'── Y'
                │          │
                g          g'
                │          │
                ▼          ▼
                X  ←──f─── Y
```

It will suffice to prove that the prescheme `Y'` is regular: indeed, since `f` is birational and of finite type, there
is an open set `U` everywhere dense in `X` such that the restriction `f⁻¹(U) → U` of `f` is an isomorphism and that
`f⁻¹(U)` be everywhere dense in `Y` `(I, 6.5.5)`; the preschemes induced respectively on the open set `g⁻¹(U)` of `X'`
and the open set `g'⁻¹(f⁻¹(U))` of `Y'` are therefore isomorphic; this proves that `g⁻¹(U)` is regular, and a fortiori
the same is so of the fibres of `g` at the maximal points of `X`, which are contained in `U`.

<!-- original page 219 -->

Let us note that the morphism `f'` is proper `(II, 5.4.2)`, and in particular of finite type, hence `Y'` is Noetherian,
since it is so of `X'`. Let `a'` be the closed point of `X'`; to see that `Y'` is regular, it will suffice to prove that
for every `y' ∈ f'⁻¹(a')`, the local ring `𝒪_{Y', y'}` is regular. Indeed, one will then have `f'⁻¹(a') ⊂ Reg(Y')`. But
since `X'` is the spectrum of a complete local ring and `f'` is of finite type, `Reg(Y')` is open in `Y'` `(6.12.8)`,
and since the morphism `f'` is closed and `f'⁻¹(a') ⊂ Reg(Y')`, there exists a neighbourhood `V` of `a'` in `X'` such
that `f'⁻¹(V) ⊂ Reg(Y')`. Since `Â` is a local ring, one necessarily has `V = X'`, hence `Reg(Y') = Y'` and the
proposition will be proved.

Now, if `a` is the closed point of `X`, one has `g⁻¹(a) = {a'}` and the residue fields `𝒌(a)` and `𝒌(a')` are
isomorphic; hence `g'⁻¹(f⁻¹(a)) = f'⁻¹(a')` and the restriction `f'⁻¹(a') → f⁻¹(a)` of `g'` is an isomorphism of these
two fibres. Let `y = g'(y')` and set `B = 𝒪_y`; if `𝔫 = 𝔪` is the maximal ideal of `B`, what precedes shows that there
exists in the (Noetherian) ring `B' = B ⊗_A Â` a single maximal ideal `𝔫'` above `𝔫` and that one has
`𝒪_{Y', y'} = B'_{𝔫'}`. To show that the local ring `B'_{𝔫'}` is regular, it suffices to establish that its completion
`(0, 17.1.5)` is so; now, by hypothesis `B` is regular, hence the same is so of its completion `B̂`. The conclusion will
follow consequently from the following lemma:

**Lemma (7.9.3.1).**

<!-- label: IV.7.9.3.1 -->

*Let `A`, `B` be two Noetherian local rings, `φ : A → B` a local homomorphism such that the ring `B' = B ⊗_A Â` be
Noetherian. Then, for every maximal ideal `𝔫'` of `B'` above the maximal ideal `𝔫` of `B` and the maximal ideal of `Â`,
the completions of `B` and of `B'_{𝔫'}` are isomorphic.*

Let `𝔪` be the maximal ideal of `A` and set `B'' = B'_{𝔫'}`. For every integer `h > 0`, one has
`B'/𝔪^h B' = B ⊗_A (Â/𝔪^h Â)`; but `Â/𝔪^h Â` is isomorphic to `A/𝔪^h`, hence `B'/𝔪^h B'` is isomorphic to `B/𝔪^h B`, and
in particular is a local ring whose maximal ideal is `𝔫'/𝔪^h B'`; consequently `B''/𝔪^h B''`, isomorphic to
`(B'/𝔪^h B')_{𝔫'}`, is `B`-isomorphic to `B'/𝔪^h B'`, and finally to `B/𝔪^h B`; in particular, the maximal ideal of
`B''` is equal to `𝔫 B''`, and `B''/𝔫^h B''` is isomorphic to `B/𝔫^h` according to what precedes. Since
`B̂'' = lim B''/𝔫^h B''`, the lemma is proved, as well as `(7.9.3)`.

**Corollary (7.9.4).**

<!-- label: IV.7.9.4 -->

*Let `A` be a Noetherian local ring.*

*(i) If, for every integral quotient ring `B` of `A`, one can resolve `Spec(B)`, then the formal fibres of `A` are
regular.*

*(ii) Suppose that, for every integral quotient ring `B` of `A`, and every integral ring `B'` containing `B`, which is a
`B`-algebra finite and whose field of fractions is radicial over that of `B`, one can resolve `Spec(B')`; then the
formal fibres of `A` are geometrically regular.*

Every formal fibre of `A` being a formal fibre of an integral quotient ring of `A` at the generic point of its spectrum,
it is clear that (i) is an immediate consequence of `(7.9.3)`, and (ii) results from (i) and from `(6.7.7)`.

**Proposition (7.9.5).**

<!-- label: IV.7.9.5 -->

*Let `X` be a locally Noetherian prescheme, such that, for every prescheme `Y` integral and finite over `X`, one can
resolve `Y`. Then the rings of the affine open sets of `X` verify conditions (ii) and (iii) of `(7.8.2)`; if moreover
`X` is universally catenary `(5.6.3)` (and*

<!-- original page 220 -->

*in particular if `X` is locally immersible in a regular prescheme `(5.6.4)`), `X` is an excellent prescheme `(7.8.5)`.*

This results at once from `(7.9.4)` and `(7.9.2)`.

**Remark (7.9.6).**

<!-- label: IV.7.9.6 -->

*It is possible that the converse of `(7.9.5)` is true, that is, that the hypothesis that `X` is reduced and that the
rings of the affine open sets of `X` verify conditions (ii) and (iii) of `(7.8.2)` implies the possibility of resolving
`X` (and consequently also the possibility of resolving every reduced prescheme locally of finite type over `X`, by
virtue of `(7.4.4)` and `(6.12.4)`). This is true in any case when one restricts to reduced Noetherian preschemes whose
residue fields are of characteristic `0`, as Hironaka's recent results `[35]` show (the latter states his results under
hypotheses that are too restrictive, his reasonings being in fact valid under the sole hypotheses (ii) and (iii) of
`(7.8.2)` for the rings of the affine open sets of `X`, together with the fact that the residue fields are of
characteristic `0`). By contrast, for the general case, one has up to now resolved only the algebraic schemes of
dimension `2` over a perfect field `[36]`. In view of the importance that the resolution of singularities is taking on
in the topological study of schemes (notably as regards their homological and homotopic properties), this gives a
particular interest to the category of excellent rings or excellent preschemes.*

*One can also note in this connection that the least delicate part of Hironaka's reasonings (*loc. cit.*) shows that
independently of any hypothesis on the characteristics of the residue fields, and using only properties (ii) and (iii)
of `(7.8.2)` for the local rings of a prescheme `X`, the problem of resolution of singularities of `X` is reduced to the
case where `X = Spec(A)`, `A` being a complete integral Noetherian local ring. Consequently, if later results should put
in default the conjecture advanced above, and should therefore lead to formulating more restrictive conditions on the
local rings of `X`, this could hardly be otherwise than by means of restrictive conditions imposed on complete local
rings (probably conditions concerning their residue fields, perhaps the condition* *`[k : k^p] ≠ +∞` (`p` exponent
characteristic of `k`)).*

**(7.9.7)** Let us consider on the one hand a full subcategory `𝓒` of the category of locally Noetherian preschemes, on
the other hand a property `𝐑(A)`, subjected to the following conditions:

1° For every `X ∈ 𝓒`, every prescheme locally of finite type over `X` belongs to `𝓒`. For every Noetherian ring `A` such
that `Spec(A) ∈ 𝓒` and every multiplicative part `S` of `A`, one has `Spec(S⁻¹A) ∈ 𝓒`.

2° For every `X ∈ 𝓒`, the set `U_𝐑(X)` of `x ∈ X` such that `𝐑(𝒪_x)` be true is open in `X`.

3° For every Noetherian local ring `A` such that `Spec(A) ∈ 𝓒` and every regular element `t` of the maximal ideal of
`A`, `𝐑(A/tA)` entails `𝐑(A)`.

Let us then denote as in `(7.5.0)` by `𝐏(Z, k)`, for a field `k` and a `k`-prescheme `Z ∈ 𝓒`, the following property:

<!-- original page 221 -->

> "For every finite extension `k'` of `k`, all the local rings of `Z ⊗_k k'` verify the property `𝐑`."

We shall further suppose that `𝐑` verifies the following condition:

4° If `𝐏(Z, k)` is true, then, for every finitely generated extension `k''` of `k`, all the local rings of `Z ⊗_k k''`
verify the property `𝐑`.

One will note that these conditions are verified when one takes for `𝓒` the category of excellent preschemes and for `𝐑`
one of the properties (i) to (viii) of `(7.5.3)`; for condition 1°, this results from `(7.8.3, (ii))`, and for
conditions 2° and 3°, from the reasonings of `(7.5.3)`, taking account of the fact that every excellent ring is
catenary. Finally, for condition 4°, it results, for (i), (ii) and (iii) from `(6.7.1)`; for (iv), (v), (vi) from
`(6.7.7)`, and for (viii) from `(4.6.1)`; as regards property (vii) of `(7.5.3)`, the corresponding property `𝐏(Z, k)`
entails that `Z` is locally integral (being locally Noetherian) and that each of the integral sub-preschemes of which
`Z` is the sum is geometrically integral, by virtue of `(4.5.9)` and `(4.6.1)`; one again concludes property 4° above in
this case.

With these notations and hypotheses:

**Proposition (7.9.8).**

<!-- label: IV.7.9.8 -->

*Let `A` be a Noetherian local ring, `k` its residue field, `B` a Noetherian local ring such that `Spec(B) ∈ 𝓒`,
`φ : A → B` a local homomorphism making `B` a flat `A`-module; set `Y = Spec(A)`, `X = Spec(B)` and let `f : X → Y` be
the morphism corresponding to `φ`. Suppose that:*

*1° The property `𝐏(B ⊗_A k, k)` is true;*

*2° For every finite morphism `Y_1 → Y`, one can resolve `(Y_1)_red`.*

*Then, for every `y ∈ Y`, the property `𝐏(f⁻¹(y), 𝒌(y))` is true.*

Let us note that condition 2° of `(7.9.8)` is still verified when one replaces `Y` by the spectrum of a local ring at a
maximal ideal of a finite `A`-algebra `A'` `(7.9.2)`; on the other hand, by virtue of condition 1° of `(7.9.7)`, the
spectrum of a ring of fractions of `B ⊗_A A'` also belongs to `𝓒`. Lemma `(7.3.16.2)` then shows (as in part I) of the
reasoning of `(7.5.2)`) that it suffices to prove that, if `Y` is integral and if `y` is the generic point of `Y`, the
local rings of the fibre `f⁻¹(y)` verify `𝐑`.

This being so, there exists by hypothesis a regular prescheme `Y'` and a proper and birational morphism `g : Y' → Y`;
since `Y'` is Noetherian and locally integral, the hypothesis that `g` is birational entails that `Y'` is integral; let
`X' = X ×_Y Y'`, so that one has a commutative diagram

```text
                X ←──f'── X'
                │         │
                f         f'
                │         │
                ▼         ▼
                Y ←──g─── Y'
```

*(7.9.8.1)*

where `f'` and `g'` are the canonical projections. Taking account of condition 2° of `(7.9.7)`, the same reasoning as at
the beginning of `(7.9.3)`

<!-- original page 222 -->

shows that it suffices to prove that one has `U_𝐑(X') = X'`, then, denoting by `a` the closed point of `X`, that
`g'⁻¹(a) ⊂ U_𝐑(X')`. Now, let `x' ∈ g'⁻¹(a)`, and set `y' = f'(x')`, so that `b = g(y')` is the closed point of `Y`. One
has therefore `f'⁻¹(y') = f⁻¹(b) ⊗_{𝒌(b)} 𝒌(y')`, and since `𝒌(y')` is a finitely generated extension of `k` (since `g`
is proper, hence of finite type), the hypothesis that `𝐏(f⁻¹(b), k)` is true entails by virtue of condition 4° of
`(7.9.7)` that the same is so of `𝐏(f'⁻¹(y'), 𝒌(y'))`. But since `𝒪_{Y', y'}` is a regular ring and
`Spec(𝒪_{Y', y'}) ∈ 𝓒` by virtue of condition 1° of `(7.9.7)`, lemma `(7.5.1.1)` proves that `𝐑(𝒪_{X', x'})` is true,
which finishes the proof.

**Corollary (7.9.9).**

<!-- label: IV.7.9.9 -->

*Let `A`, `B` be two Noetherian local rings, `φ : A → B` a local homomorphism making `B` a flat `A`-module. Suppose that
`A` is integral and geometrically unibranch, and that for every finite integral `A`-algebra `A'` one can resolve
`Spec(A')` (which will be the case for example if the formal fibres of `A` are geometrically regular and the residue
field of `A` is of characteristic `0`, on account of Hironaka's results `[35]`). Let `k` be the residue field of `A` and
suppose that `Spec(B ⊗_A k)` is geometrically pointwise integral `(4.6.9)`. Then `B` is integral.*

We are going to apply `(7.9.8)` taking for `𝓒` the category of all locally Noetherian preschemes, for `𝐑` the property
of being integral; the reasonings of `(7.5.3)` and `(7.9.7)` show that conditions 1°, 2°, 3° and 4° of `(7.9.7)` are
satisfied in this case. The hypothesis on `B ⊗_A k` and proposition `(7.9.8)` show therefore (with the notations of
`(7.9.8)`) that the fibres `f⁻¹(y)` are geometrically pointwise integral for `y ∈ Y`; a fortiori the `f⁻¹(y)` for
`y ∈ Y` are reduced preschemes, and since `A` is integral (and a fortiori reduced), one sees already that `B` is reduced
`(3.3.5)`. It remains to prove that `X = Spec(B)` is irreducible. Now, the proof of `(7.9.8)` proves that `X'` is
locally integral (being locally Noetherian). Since the morphism `g' : X' → X` is surjective, it therefore suffices to
see that `X'` is irreducible, or (since `X'` is locally integral) that `X'` is connected. But it suffices for this to
prove that the fibre `g'⁻¹(a)` is connected. Indeed, if this point is established, `X'` cannot be the sum of two
non-empty open preschemes `X_1`, `X_2`, for one would then have for example `g'⁻¹(a) ∩ X_1 = ∅`; but the restriction
`X_2 → X` of `g'` being proper (since `X_2` is a closed sub-prescheme of `X'`), `g'(X_2)` would be a non-empty closed
part of `X` not containing the closed point `a`, which is absurd. Now, one has `g'⁻¹(a) = g⁻¹(b) ⊗_{𝒌(b)} 𝒌(a')`; but
`g : Y' → Y` is proper and birational, hence, in the Stein factorization `Y' → Y'' → Y` of the morphism `g`
`(III, 4.3.3)`, the finite morphism `u` is also birational and consequently `Y''` is integral. Since `A` is assumed
geometrically unibranch, it results then from `(III, 4.3.4)` that `g⁻¹(b)` is geometrically connected, which finishes
the proof.

**Remarks (7.9.10).**

<!-- label: IV.7.9.10 -->

*(i) We shall show further on `(18.8.11)` that in order that a reduced local ring `B` be geometrically unibranch, it is
necessary and sufficient that for every étale morphism `h : X' → X = Spec(B)` and every point `x' ∈ X'` above the closed
point of `X`, `𝒪_{X', x'}` be integral. One deduces from this that if, in `(7.9.9)`, one supposes, not only that
`Spec(B ⊗_A k)` is geometrically pointwise integral, but geometrically unibranch, then one can conclude that `B` is
geometrically unibranch.*

<!-- original page 223 -->

*(ii) Let `X`, `Y` be two excellent preschemes, `f : X → Y` a flat morphism, and suppose that for every finite morphism
`Y_1 → Y`, one can resolve `(Y_1)_red`. It results from `(7.9.8)`, taking for `𝐑` the property of being regular, that
the set `U` of points `x ∈ X` such that the fibre at the point `f(x)` of the morphism*

```text
   Spec(𝒪_x ⊗_{𝒪_{f(x)}} 𝒌(f(x))) → Spec(𝒌(f(x)))
```

*be geometrically regular, is stable under generization. We do not know whether this set is open (or, what comes to the
same `(0_III, 9.2.5)`, whether it is constructible), even in the particular case where `Y` is the spectrum of `ℤ` or of
a ring of polynomials in one indeterminate `k[T]` over a field `k`, and where consequently the condition of
"resolvability" imposed on `Y` is trivially satisfied.*

*(To be continued.)*

[^1]: Cor. `(7.2.8)` is not used to prove `(7.4.4)`.
