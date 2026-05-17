<!-- original page 225 -->

## §20. Meromorphic functions; pseudo-morphisms

### 20.0. Introduction

Most of the notions and results of §§20 and 21 attach directly to chap. I, and depend hardly at all on chaps. II to IV,
except for the occasional use of the notion of depth and of regular local ring (in `(20.6)`, `(21.11)`, `(21.13)` and
`(21.15)`), of Zariski's "Main theorem" in `(20.4)` and `(21.12)`, and of properties of transversely regular immersions
in `(20.6)` and `(21.15)`.

<!-- original page 226 -->

In §20, we introduce several variants of the notion of rational map, already studied in `(I, 7)` from a point of view
still rather close to the classical viewpoint, and for this reason rather poorly adapted to the case of preschemes that
are not necessarily reduced. The notions and results of §20 are used in §21 (nos. 21.1 to 21.7) to develop the general
notion of divisor and its most elementary properties. This notion is especially convenient when the local rings of the
preschemes under consideration are Noetherian and integrally closed, and especially when they are moreover *factorial*
`(21.6 and 21.7)`, because of its identification in this latter case with the notion of *`1`-codimensional cycle*
(linear combination of irreducible subpreschemes of codimension `1`). In `(21.9)`, one determines the divisors on a
Noetherian prescheme of dimension `1` but not necessarily normal, which is useful for various applications. Nos.
`(21.11)` and `(21.12)` give two important theorems, due respectively to Auslander-Buchsbaum and Van der Waerden, and
related to the notion of factorial ring (nos. `(21.9)`, `(21.11)` and `(21.12)` are independent of one another). In
nos. `(21.13)` and `(21.14)`, also independent of the previous three, we study a useful variant of the notion of
factorial local ring, that of *parafactorial* local ring, which is introduced notably `[41]` in the development of
comparison theorems between the Picard group of a projective prescheme `X` over a field `k` and that of a "hyperplane
section". One will see in `(21.14.1)` (Ramanujam-Samuel theorem) that parafactorial local rings are much more numerous
than one might *a priori* have expected.

In `(20.5)`, `(20.6)` and `(21.15)`, we take up the preceding notions again but from a viewpoint "relative" to a fixed
base prescheme. For the moment these notions are used only rather rarely; in particular, the notion of relative divisor
is scarcely used except when one is dealing with positive divisors, and in this case it is explained advantageously
without recourse to the notion of relative meromorphic function, by means of the notion of transversely regular
immersion of codimension `1`. The reader will therefore find it advantageous to omit these sections on a first reading.

### 20.1. Meromorphic functions

**(20.1.1).** Let `(X, 𝒪_X)` be a ringed space, and let `𝒮` be a subsheaf *of sets* of `𝒪_X`. For every open `U` of `X`,
consider the *ring of fractions* `Γ(U, 𝒪_X)[Γ(U, 𝒮)⁻¹]` (Bourbaki, _Alg. comm._, chap. II, §2, n° 1). It is immediate
that the map `U ↦ Γ(U, 𝒪_X)[Γ(U, 𝒮)⁻¹]` is a *presheaf of rings* `(0_I, 1.5.1 and 1.5.7)`. We denote by `𝒪_X[𝒮⁻¹]` the
*sheaf of rings* associated to this presheaf and we say that this is the *sheaf of rings of fractions of `𝒪_X` with
denominators in `𝒮`*; it is a *flat* `𝒪_X`-module. It is immediate that for every `x ∈ X`, one has a canonical
isomorphism

<!-- label: IV.20.1.1 -->

```text
  (20.1.1.1)             (𝒪_X[𝒮⁻¹])_x ⥲ 𝒪_x[𝒮_x⁻¹],
```

since the reasoning of `(0_I, 1.4.5)` generalizes immediately to the case where one has an inductive system
`(A_α, φ_{βα})` of rings, and for each index `α` a subset `S_α` of `A_α` such that

<!-- original page 227 -->

`φ_{βα}(S_α) ⊂ S_β` for `α ≤ β`; one then takes for `S` the inductive limit in `A = lim A_α` of the inductive system of
subsets `(S_α)`.

**(20.1.2).** Let now `ℱ` be an `𝒪_X`-module. One then sets

```text
  (20.1.2.1)             ℱ[𝒮⁻¹] = ℱ ⊗_{𝒪_X} 𝒪_X[𝒮⁻¹]
```

and one says that this is the *sheaf of modules of fractions of `ℱ` with denominators in `𝒮`*; it is immediate that it
is associated to the presheaf of modules `U ↦ Γ(U, ℱ)[Γ(U, 𝒮)⁻¹]`, and that for every `x ∈ X` one has a canonical
isomorphism

```text
  (20.1.2.2)             (ℱ[𝒮⁻¹])_x ⥲ ℱ_x[𝒮_x⁻¹].
```

**(20.1.3).** We shall be interested here in the case where `𝒮` is the subsheaf `𝒮(𝒪_X)` of `𝒪_X` such that for every
open `U`, `Γ(U, 𝒮)` is the *set of regular elements* of the ring `Γ(U, 𝒪_X)`; it is immediate that this is a sheaf (and
not only a presheaf), the regularity of a section of `𝒪_X` over `U` being verified "fibre by fibre" (i.e. meaning that
the germ of the section at `x` is regular in `𝒪_{X,x}` for every `x ∈ U`); in other words `𝒮(𝒪_X)_x` is none other than
the set of regular elements of `𝒪_{X,x}`. The corresponding sheaf of rings

```text
                         𝓜_X = 𝒪_X[𝒮⁻¹]
```

is called the *sheaf of germs of meromorphic functions on `X`*, and the sections of `𝓜_X` over `X` are called the
*meromorphic functions on `X`*; they form a ring which one denotes `M(X)`. For every `𝒪_X`-Module `ℱ`,

```text
                         ℱ ⊗_{𝒪_X} 𝓜_X = ℱ[𝒮⁻¹]
```

is also denoted `𝓜_X(ℱ)` and called the *sheaf of germs of meromorphic sections of `ℱ`*; its sections over `X` form an
`M(X)`-module denoted `M(X, ℱ)`, whose elements are called *meromorphic sections of `ℱ` over `X`*. These definitions
imply that for every open `U` of `X`, one has a canonical isomorphism `𝓜_X(ℱ) | U ⥲ 𝓜_U(ℱ | U)`, in particular
`𝓜_X | U ⥲ 𝓜_U`.

**(20.1.3.1).** If `X` is a *reduced prescheme*, one will note that if an element `s ∈ Γ(U, 𝒪_X)` is such that
`s_ξ ≠ 0` for every maximal point `ξ` of `U`, then `s` is *regular*. Indeed, if `st = 0` for a `t ∈ Γ(U, 𝒪_X)`, one has
`s_ξ t_ξ = 0`, hence `t_ξ = 0` since `𝒪_{X,ξ}` is a field, and to say that `t_ξ = 0` for every maximal point `ξ` of `X`
means that `t = 0`: one is at once reduced to the case where `U` is affine, and an element of a reduced ring belonging
to every minimal prime ideal is zero by definition. The converse is true if the set of irreducible components of `X` is
*locally finite*. One is at once reduced to the case where `X = Spec(A)` is affine; if `𝔭_i` (`1 ≤ i ≤ n`) are the
minimal prime ideals of `A` and `s ∈ 𝔭_i` for some index `i`, then there exists `t ∈ A` such that `t ∈ 𝔭_j` for
`j ≠ i` and `t ∉ 𝔭_i` (Bourbaki, _Alg. comm._, chap. II, §1, n° 1, prop. 1); one therefore has `st ∈ 𝔭_i` for every
`i`, hence `st = 0` since `A` is reduced; so `s` is not regular.

**(20.1.4).** For every open `U` of `X`, the homomorphism `t ↦ t/1` from `Γ(U, 𝒪_X)` to `Γ(U, 𝒪_X)[Γ(U, 𝒮)⁻¹]` (which
is none other than the *total ring of fractions* of

<!-- original page 228 -->

`Γ(U, 𝒪_X)`) is injective; these homomorphisms therefore define a *canonical injective homomorphism*

```text
  (20.1.4.1)             i : 𝒪_X → 𝓜_X
```

which allows one to identify `𝒪_X` with a subsheaf of `𝓜_X`. Given a meromorphic function `φ ∈ M(X)`, one says that
`φ` is *defined* on an open `U` of `X` if `φ | U` is a section of `𝒪_X` over `U`; the sheaf axioms show that, for a
given section `φ`, there is a *largest* open on which `φ` is defined; one calls this the *domain of definition* of `φ`
and denotes it `dom(φ)`.

**(20.1.5).** For every `𝒪_X`-Module `ℱ`, one deduces from `(20.1.4.1)` a di-homomorphism formed of `i` and the
homomorphism of sheaves of additive groups

```text
  (20.1.5.1)             1_ℱ ⊗ i : ℱ → 𝓜_X(ℱ) = ℱ ⊗_{𝒪_X} 𝓜_X.
```

One will note that the latter is no longer injective in general; when it is injective, one says that `ℱ` is *strictly
torsion-free*: this means that for every open `U` of `X` and every section `s ∈ Γ(U, 𝒪_X)` which is a regular element
of that ring, the homothety `z ↦ sz` of `Γ(U, ℱ)` is injective; this condition is evidently satisfied if `ℱ` is
*locally free*.

**Proposition (20.1.6).**

<!-- label: IV.20.1.6 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module. For `ℱ` to be strictly torsion-free, it
is necessary and sufficient that `Ass(ℱ) ⊂ Ass(𝒪_X)`.*

One is at once reduced to the case where `X = Spec(A)` is affine, `ℱ = M̃`, and one knows that the elements `s` of `A`
belonging to an ideal of `Ass(M)` are exactly those for which the homothety `z ↦ sz` is not injective (Bourbaki,
_Alg. comm._, chap. IV, §1, n° 1, cor. 2 of prop. 2).

**(20.1.7).** If `u` is a section of `𝓜_X(ℱ)` over `X`, one says that `u` is *defined* at a point `x ∈ X` if there
exists an open neighbourhood `V` of `x` in `X` such that `u | V` is the image of a section of `ℱ` over `V` under the
di-homomorphism `(20.1.5.1)`. One says that `u` is *defined* on an open `U` of `X` if it is defined at every point of
`U`; there is again a largest open on which `u` is defined, called the *domain of definition* of `u` and denoted
`dom(u)`. When `ℱ` is strictly torsion-free, so that `ℱ` is identified by `(20.1.5.1)` with a subsheaf of `𝓜_X(ℱ)`,
saying that `u` is defined on `U` means that `u | U` is a section of `ℱ` over `U`.

**(20.1.8).** In accordance with the general notation `(0_I, 5.4.7)`, one denotes by `𝓜_X^×` the sheaf of multiplicative
groups such that `Γ(U, 𝓜_X^×)` is (for every open `U` of `X`) the group of *invertible elements* of `Γ(U, 𝓜_X)`. This
sheaf is none other than the sheaf `𝒮(𝓜_X)` defined in `(20.1.3)`: indeed, if `s ∈ Γ(U, 𝒮(𝓜_X))`, then for every
`x ∈ U` there exists an open neighbourhood `V ⊂ U` of `x` such that `s | V` is a regular element in the *total ring of
fractions* of `Γ(V, 𝒪_X)`, and one knows that such an element is necessarily invertible in this ring of fractions. We
shall say that the sections of `𝓜_X^×` over `X` are the *regular meromorphic functions* (one will note that we are
departing here from the terminology followed by certain authors, who call "regular" meromorphic functions those which
are sections of `𝒪_X`, identified with a subsheaf of `𝓜_X`).

Let `ℒ` be an *invertible `𝒪_X`-Module* `(0_I, 5.4.1)`; then it is clear that `𝓜_X(ℒ) = ℒ ⊗_{𝒪_X} 𝓜_X`

<!-- original page 229 -->

is an invertible `𝓜_X`-Module. Let `U` be an open such that `ℒ | U` is isomorphic to `𝒪_U`; since every automorphism
of `𝓜_U` is multiplication by an invertible element of `Γ(U, 𝓜_X)` `(0_I, 5.4.7)`, it amounts to the same thing to
say that a section `s ∈ Γ(U, 𝓜_X(ℒ))` has invertible image in `Γ(U, 𝓜_X)` under *an* isomorphism or under *every*
isomorphism onto `Γ(U, 𝓜_X)`; one will say in this case that `s` is a *regular meromorphic section of `ℒ`* over `U`; a
section `s` of `ℒ` over `X` will be called a *regular meromorphic section of `ℒ`* if, for every open `U` such that
`ℒ | U` is isomorphic to `𝒪_U`, `s | U` is a regular meromorphic section of `ℒ` over `U`. One denotes by
`(𝓜_X(ℒ))^×` the subsheaf of `𝓜_X(ℒ)` such that for every open `U`, `Γ(U, (𝓜_X(ℒ))^×)` is the set of regular
meromorphic sections of `ℒ` over `U`. Let `s` be a meromorphic section of `ℒ` over `X` (i.e. a section of `𝓜_X(ℒ)`);
it defines a homomorphism `h_s : 𝓜_X → 𝓜_X(ℒ)` which to every section `t` of `𝓜_X` over an open `U` associates
`(s | U) t`. It follows at once from the foregoing that, for `s` to be *regular*, it is necessary and sufficient that
`h_s` be *injective*, and in fact `h_s` is then a *bijective* homomorphism from `𝓜_X` to `𝓜_X(ℒ)`, and its restriction
to `𝓜_X^×` is a bijection onto `(𝓜_X(ℒ))^×`. One concludes that the homothety `t ↦ ts` is an isomorphism from
`M(X)` onto `M(X, ℒ)`.

**(20.1.9).** Let `s` be a regular meromorphic section of the invertible `𝒪_X`-Module `ℒ` over `X`; then, for every
`𝒪_X`-Module `ℱ`, `s` likewise defines a homomorphism
`h_s ⊗ 1_ℱ : 𝓜_X(ℱ) → 𝓜_X(ℱ ⊗_{𝒪_X} ℒ)`, which is again *bijective*.

**(20.1.10).** Let `s` be a meromorphic section of an invertible `𝒪_X`-Module `ℒ` over `X`; for `s` to be regular, it is
necessary and sufficient that there exist a meromorphic section `s'` of `ℒ⁻¹` over `X` such that the canonical image of
`s ⊗ s'` in `𝓜_X` `(0_I, 5.4.3)` is the unit section, and this section `s'` is then unique: indeed, the necessity of
the local existence of such a section is evident, and its local uniqueness entails its global existence (and
uniqueness); moreover, the existence of `s'` is trivially sufficient for `s` to be regular. One will set `s' = s⁻¹`.

Finally, if `ℒ'` is a second invertible `𝒪_X`-Module, `s` (resp. `s'`) a regular meromorphic section of `ℒ` (resp.
`ℒ'`) over `X`, then `s ⊗ s'` is evidently a regular meromorphic section of `ℒ ⊗ ℒ'` over `X`.

**(20.1.11).** If `f : X' → X` is a morphism of ringed spaces, there is in general no natural map sending a meromorphic
function on `X` to a meromorphic function on `X'`. For example, if `X` is the spectrum of an integral local ring `A`,
`X'` that of its residue field `k`, there is no natural homomorphism from the field of fractions `K` of `A` to `k`, and
one can send an element of `K` to an element of `k` only if it is already in `A`.

More generally, if `f = (ψ, θ)`, denote, for every open `U` of `X`, by `𝒮_f(U)` the set of *regular* sections
`s ∈ Γ(U, 𝒪_X)` such that the image of `s` under

```text
                         Γ(θ♯) : Γ(U, 𝒪_X) → Γ(f⁻¹(U), 𝒪_{X'})
```

is a regular section. It is immediate that `U ↦ 𝒮_f(U)` is a *subsheaf* of the sheaf of sets `𝒮(𝒪_X)`, which one
denotes `𝒮_f`. One sets `𝓜_f = 𝒪_X[𝒮_f⁻¹]`; this is a subsheaf

<!-- original page 230 -->

of rings of `𝓜_X`, and one canonically deduces from `θ♯ : ψ*(𝒪_X) → 𝒪_{X'}` a homomorphism of sheaves of rings
`θ'♯ : ψ*(𝓜_f) → 𝓜_{X'}` extending `θ♯` (Bourbaki, _Alg. comm._, chap. II, §2, n° 1, prop. 2); whence, recalling that
`f*(𝓜_f) = ψ*(𝓜_f) ⊗_{ψ*(𝒪_X)} 𝒪_{X'}`, a canonical homomorphism of `𝒪_{X'}`-Algebras

```text
  (20.1.11.1)            f*(𝓜_f) → 𝓜_{X'}.
```

For every meromorphic function `φ` on `X` which is a section of `𝓜_f`, `Γ(θ'♯)(φ)` is a meromorphic function on `X'`,
called the *inverse image of `φ` under `f`*, and denoted `φ ∘ f` if this entails no confusion.

Similarly, if `ℱ` is an `𝒪_X`-Module, one sets `𝓜_f(ℱ) = ℱ ⊗_{𝒪_X} 𝓜_f`, and one immediately deduces from `θ'♯` a
canonical homomorphism (also written `u ↦ u ∘ f`)

```text
                         Γ(X, 𝓜_f(ℱ)) → Γ(X', 𝓜_{X'}(f*(ℱ))).
```

Moreover, if `u ∈ Γ(X, 𝓜_f(ℱ))` is defined `(20.1.7)` at a point `x`, `u` coincides, on a neighbourhood `U` of `x`,
with a section of the form `∑_i h_i ⊗ (t_i / s_i)`, where the `h_i` belong to `Γ(U, ℱ)`, the `t_i` to `Γ(U, 𝒪_X)`, and
the `s_i` to `Γ(U, 𝒮_f)`. As by hypothesis the images of the `s_i` in `Γ(f⁻¹(U), 𝒪_{X'})` are regular, one sees that
`u ∘ f` is defined at every point of `f⁻¹(U)`; in other words, one has

```text
  (20.1.11.2)            f⁻¹(dom(u)) ⊂ dom(u ∘ f).
```

We shall see later `(20.6.5, (i))` examples (with `ℱ = 𝒪_X`) where the two sides of `(20.1.11.2)` may be distinct.

Consider in particular the case where `𝓜_f = 𝓜_X`; then, if `ℒ` is an invertible `𝒪_X`-Module, the image in
`𝓜_{X'}(f*(ℒ))`, under `Γ(θ'♯)`, of a *regular* meromorphic section of `ℒ` over `X` `(20.1.8)` is a *regular*
meromorphic section of `f*(ℒ)` over `X'`, as follows at once from the definition of these sections and from the fact
that a homomorphism of rings sends an invertible element to an invertible element.

Let `f' : X'' → X'` be a second morphism of ringed spaces, and suppose that `𝓜_f = 𝓜_X` and `𝓜_{f'} = 𝓜_{X'}`; then,
if one sets `f'' = f ∘ f'`, one also has `𝓜_{f''} = 𝓜_X`, and one sees at once that for every meromorphic section `u`
of `ℱ` over `X`, one has `u ∘ f'' = (u ∘ f) ∘ f'`.

**Proposition (20.1.12).**

<!-- label: IV.20.1.12 -->

*If the morphism `f : X' → X` is flat `(0_I, 6.7.1)`, one has `𝓜_f = 𝓜_X`, and the homomorphism `φ ↦ φ ∘ f` is defined
on all of `M(X)`. Moreover, if `f` is a (flat) morphism of ringed spaces in local rings, one has
`dom(φ ∘ f) = f⁻¹(dom(φ))`; if in addition `f` is surjective (hence faithfully flat), the homomorphism `φ ↦ φ ∘ f` is
injective.*

The first assertion follows from the fact that, if `B` is an `A`-algebra which is a flat `A`-module, every element of
`A` which is not a zero-divisor in `A` is not a zero-divisor in `B` `(0_I, 6.3.4)`. To prove the other assertions, note
that, for every `x' ∈ X'`, if `x = f(x')`, `𝒪_{X', x'}` is a flat `𝒪_{X,x}`-module, and since the homomorphism
`𝒪_{X,x} → 𝒪_{X', x'}` is local by hypothesis, it is injective `(0_I, 6.5.1 and 6.6.2)`; if one sets `A = 𝒪_{X,x}`,
`B = 𝒪_{X', x'}`, so that `A` identifies with a subring of `B`, `(f*(𝓜_X))_{x'}` is equal to `S⁻¹A ⊗_A B = S⁻¹B`,
where `S` is the set of regular elements of `A`, `(𝓜_{X'})_{x'}` is equal to `T⁻¹B`, where `T` is the set

<!-- original page 231 -->

of regular elements of `B`, and as we have seen that `S ⊂ T`, the homomorphism `S⁻¹B → T⁻¹B` is injective; in other
words, this proves that the homomorphism `(20.1.11.1)` `f*(𝓜_X) → 𝓜_{X'}` is *injective* (whence the last assertion of
the statement). The quotient `f*(𝓜_X) / 𝒪_{X'}` identifies with an `𝒪_{X'}`-submodule of `𝓜_{X'} / 𝒪_{X'}`, and
`(f*(𝓜_X) / 𝒪_{X'})_{x'}` identifies with `(𝓜_X / 𝒪_X)_x ⊗_{𝒪_{X,x}} 𝒪_{X', x'}`. Now suppose that `x ∉ dom(φ)`; the
image of `φ_x` in `(𝓜_X / 𝒪_X)_x` is therefore `≠ 0`; by faithful flatness, one deduces that the same holds for the
image of `(φ ∘ f)_{x'}` in `(𝓜_{X'} / 𝒪_{X'})_{x'}`, hence `x' ∉ dom(φ ∘ f)`, which finishes the proof.

**Remark (20.1.13).**

<!-- label: IV.20.1.13 -->

Let `X` be a *reduced* complex analytic space; then the notion of meromorphic function on `X` defined above coincides
with the usual notion. Consider on the other hand a prescheme `Y`, locally of finite type over the field `ℂ`; one then
knows that one can associate to `Y` an analytic space `Y^an` having the same underlying topological space, and that the
canonical morphism `f : Y^an → Y` is flat `[37]`; by virtue of `(20.1.12)`, the canonical homomorphism `u ↦ u ∘ f` from
`M(Y)` to `M(Y^an)` is therefore everywhere defined and injective; but it is not *surjective* in general. For example,
when `Y = 𝕍_0^r` (`Err_{III}, 14`) is the affine space of dimension `r` over `ℂ`, `M(Y)` identifies canonically with
the field `R(Y)` of rational functions on `Y` `(20.2.13, (i))`, while `M(Y^an)` is the field of usual meromorphic
functions on `ℂ^r`. By reason of this fact, it is often preferable, in algebraic geometry, to refrain from the
terminology introduced in this section, and to use the equivalent terminology of "pseudo-function" which will be defined
below.

### 20.2. Pseudo-morphisms and pseudo-functions

*The only ringed spaces considered in this section are preschemes.*

**(20.2.1).** Recall `(11.10.2)` that in a prescheme `X` one says that an open `U` is *schematically dense* if, for
every open `V` of `X`, the canonical homomorphism `Γ(V, 𝒪_X) → Γ(V ∩ U, 𝒪_X)` is injective.

Consider two preschemes `X`, `Y`, and two schematically dense opens `U`, `U'` of `X`; one says that two morphisms
`u : U → Y`, `u' : U' → Y` are *equivalent* if there exists an open `U'' ⊂ U ∩ U'`, schematically dense in `X`, such
that `u | U'' = u' | U''`. As it follows at once from the definition of schematically dense opens that the intersection
of two such opens is again one, it is immediate that the previous relation is indeed an equivalence relation. An
equivalence class under this relation is called a *pseudo-morphism of `X` into `Y`*, or a *strict rational map of `X`
into `Y`*.

If `S` is a prescheme and `X`, `Y` are two `S`-preschemes, one calls *pseudo-`S`-morphism* the equivalence class (for
the foregoing relation) of an `S`-morphism from a schematically dense open of `X` to `Y`. A pseudo-morphism is therefore
nothing other than a pseudo-`S`-morphism for `S = Spec(ℤ)`.

One denotes by `Ps.hom(X, Y)` (resp. `Ps.hom_S(X, Y)`) the set of pseudo-morphisms (resp. pseudo-`S`-morphisms) of `X`
into `Y`.

<!-- original page 232 -->

**(20.2.2).** It follows from the definition recalled above that if `U` is a schematically dense open in `X`, then for
every open `V` of `X`, `U ∩ V` is schematically dense in `V`. If two morphisms `u : U → Y`, `u' : U' → Y` of
schematically dense opens of `X` into `Y` are equivalent, it follows that their restrictions `u | (V ∩ U)` and
`u' | (V ∩ U')` are also equivalent morphisms (for the prescheme induced on `V`); their class is called the *restriction
to `V`* of the pseudo-morphism `ω`, the class of `u`, and this pseudo-morphism is denoted `ω | V`. If `W ⊂ V` is an
open of `X`, it is clear that `(ω | V) | W = ω | W`. This shows that the restriction maps define a presheaf of sets
`U ↦ Ps.hom(U, Y)`; one will note that this presheaf is not in general a sheaf (cf. `(20.2.16)`); the associated sheaf
is denoted `𝒫𝓈.hom(X, Y)`. For pseudo-`S`-morphisms, one sees likewise that `U ↦ Ps.hom_S(U, Y)` is a presheaf of sets,
whose associated sheaf is denoted `𝒫𝓈.hom_S(X, Y)`.

If `V` is schematically dense in `X`, then for every open `U` schematically dense in `X`, `U ∩ V` is also schematically
dense in `X`, so the map `ω ↦ ω | V` is a bijection from `Ps.hom(X, Y)` (resp. `Ps.hom_S(X, Y)`) onto `Ps.hom(V, Y)`
(resp. `Ps.hom_S(V, Y)`).

**(20.2.3).** Given a pseudo-`S`-morphism `ω` of `X` into `Y`, one says that it is *defined* at a point `x ∈ X` if there
exists an open neighbourhood `V` of `x` in `X`, an open `U ⊂ V` containing `x` and schematically dense in `V`, and an
`S`-morphism `u : U → Y` whose class in `Ps.hom_S(V, Y)` equals `ω | V` `(20.2.2)`; one calls *domain of definition* of
`ω`, and one denotes by `dom_S(ω)` (or simply `dom(ω)` if `S = Spec(ℤ)`), the set of `x ∈ X` where `ω` is defined; it is
evidently an open of `X`. Moreover, for every open `W` of `X`, one has

```text
  (20.2.3.1)             dom_S(ω | W) = (dom_S(ω)) ∩ W
```

by virtue of the property of schematically dense opens recalled in `(20.2.2)`.

**Proposition (20.2.4).**

<!-- label: IV.20.2.4 -->

*Suppose that `X`, `Y` are `S`-preschemes such that the structure morphism `Y → S` is separated; then, if `ω` is a
pseudo-`S`-morphism of `X` into `Y`, `dom_S(ω)` is the largest of the schematically dense opens `U` of `X` such that
there exists an `S`-morphism `u : U → Y` belonging to the class `ω`.*

It evidently suffices to prove that if `U`, `U'` are two schematically dense opens in `X` such that two `S`-morphisms
`u : U → Y` and `u' : U' → Y` are equivalent, then the restrictions of `u` and `u'` to `U ∩ U'` are equal. Now by
hypothesis there exists an open `U'' ⊂ U ∩ U'`, schematically dense in `X` and on which `u` and `u'` coincide; as `U''`
is also schematically dense in `U ∩ U'`, our assertion follows from `(11.10.1, d)`.

**Corollary (20.2.5).**

<!-- label: IV.20.2.5 -->

*Let `S` be an `S_0`-scheme, `X`, `Y` two `S`-preschemes such that the composite `Y → S → S_0` is separated (which
implies `(I, 5.5.1)` that `Y → S` is also separated). For every pseudo-`S`-morphism `ω` of `X` into `Y`, one has then
`dom_S(ω) = dom_{S_0}(ω)`. In particular, if `Y` is a scheme, one has `dom_S(ω) = dom(ω)`.*

Indeed, it is clear that `dom_S(ω) ⊂ dom_{S_0}(ω)` without any separation hypothesis; by virtue of `(20.2.4)`, it
suffices to prove that if an `S_0`-morphism `u_0 : U_0 → Y` from a schematically dense

<!-- original page 233 -->

open `U_0` of `X` into `Y` is such that the composite `v_0 : U_0 → Y → S` coincides with the restriction of the
structure morphism `w_0 : U_0 → S` on an open `U ⊂ U_0` schematically dense in `X`, then `v_0 = w_0`. But by virtue of
the hypothesis that the morphism `S → S_0` is separated, this again follows from `(11.10.1, d)`.

**Corollary (20.2.6).**

<!-- label: IV.20.2.6 -->

*Under the hypotheses of `(20.2.4)`, the presheaf `U ↦ Ps.hom_S(U, Y)` is a sheaf.*

Indeed, let `U` be an open of `X`, `(U_α)` a cover of `U` by opens of `U`; suppose given for each `α` a
pseudo-`S`-morphism `ω_α` of `U_α` into `Y`, so that for every pair of indices `α`, `β`, the restrictions `(20.2.2)` of
the pseudo-`S`-morphisms `ω_α` and `ω_β` to `U_α ∩ U_β` are equal; by virtue of `(20.2.3.1)`, this entails
`dom_S(ω_α) ∩ U_β = dom_S(ω_β) ∩ U_α`. Let `W` be the union of the opens `dom_S(ω_α)`, and, for each `α`, let `u_α` be
the unique `S`-morphism `dom_S(ω_α) → Y` belonging to the class `ω_α` `(20.2.4)`; by reason of the hypothesis and of
`(20.2.4)`, the restrictions of `u_α` and `u_β` to `dom_S(ω_α) ∩ dom_S(ω_β)` are equal, so there exists a morphism
`u : W → Y` whose restriction to each open `dom_S(ω_α)` equals `u_α`. It is clear that `W` is schematically dense in
`U`, hence defines a pseudo-`S`-morphism `ω` of `U` into `Y` whose restrictions to the `U_α` are the `ω_α`.

**Remark (20.2.7).**

<!-- label: IV.20.2.7 -->

One knows `(11.10.4)` that when `X` is reduced, it amounts to the same to say that an open of `X` is dense in `X` or
that it is schematically dense in `X`; the notion of pseudo-morphism (resp. pseudo-`S`-morphism) of `X` into `Y` then
coincides with that of *rational map* (resp. *`S`-rational map*) of `X` into `Y` `(I, 7.1.2)`. In the general case, the
notion of pseudo-morphism seems more useful than that of rational map.

**(20.2.8).** One calls *pseudo-function* on `X` a pseudo-morphism of `X` into `Spec(ℤ[T])` (`T` indeterminate), or,
what amounts to the same, an `X`-pseudo-morphism of `X` into `X ⊗_ℤ ℤ[T]`; it amounts also to the same `(I, 3.3.15)` to
say that a pseudo-function on `X` is an equivalence class of *sections of `𝒪_X` over schematically dense opens of `X`*,
two sections `g ∈ Γ(U, 𝒪_X)`, `g' ∈ Γ(U', 𝒪_X)` over such opens being equivalent if there exists an open
`U'' ⊂ U ∩ U'`, schematically dense in `X`, on which `g` and `g'` coincide. One may here apply `(20.2.4)` with `S = X`
and `Y = X ⊗_ℤ ℤ[T]`; hence, for every pseudo-function `φ` on `X`, there exists a largest schematically dense open
`dom(φ)` in `X` on which there is a section of `𝒪_X` over `dom(φ)` belonging to the class `φ`. It is clear that the
sheaf `𝒫𝓈.hom(X, X ⊗_ℤ ℤ[T])` is here a sheaf of rings, even an `𝒪_X`-Algebra, which we shall denote `𝓜'_X`; it follows
from `(20.2.6)` that, for every open `U` of `X`, `Γ(U, 𝓜'_X)` equals the set of pseudo-morphisms of `U` into
`Spec(ℤ[T])`; one sets `M'(X) = Γ(X, 𝓜'_X)`. To say that a section `φ` of `𝓜'_X` over `U` is invertible in the ring
`Γ(U, 𝓜'_X)` means that there exists an open `U'` schematically dense in `dom(φ)`, hence in `U`, such that, if `g` is
the unique section of `𝒪_X` over `dom(φ)` belonging to `φ`, `g | U'` is invertible in `Γ(U', 𝒪_X)`. It follows from
`(I, 3.3.15)` that, in the canonical correspondence between `Γ(V, 𝒪_X)` and `Hom(V, ℤ[T])` (`V` open

<!-- original page 234 -->

of `X`), the invertible elements of `Γ(V, 𝒪_X)` correspond to morphisms which factor as
`V → Spec(ℤ[T, T⁻¹]) → Spec(ℤ[T])`. One concludes that the sheaf `𝓜'_X^×` of germs of invertible sections of `𝓜'_X`
identifies canonically with the sheaf `𝒫𝓈.hom(X, X ⊗_ℤ ℤ[T, T⁻¹])`.

**Lemma (20.2.9).**

<!-- label: IV.20.2.9 -->

*Let `U` be an open of `X`, `s` a regular element of the ring `Γ(U, 𝒪_X)`; then the open set `U_s` of `x ∈ U` such that
`s(x) ≠ 0` is schematically dense in `U`.*

Indeed, let `V` be an open of `U`, `t` a section of `𝒪_X` over `V` such that `t | (V ∩ U_s) = 0`. For every affine open
`W ⊂ V`, there then exists an integer `n` such that `s^n t | W = 0` `(I, 1.4.1)`; but since `s` is a regular element of
`Γ(U, 𝒪_X)`, this entails `t | W = 0`, whence `t = 0`.

**(20.2.10).** Consider a meromorphic function `f ∈ M(X)` `(20.1.4)`; then `dom(f)` is *schematically dense* in `X`:
indeed, every point of `X` admits an open neighbourhood `U` such that there exists a section `s ∈ Γ(U, 𝒮)` which is a
regular element of this ring, and such that `s(f | U) ∈ Γ(U, 𝒪_X)`; since `s | U_s` is invertible, one concludes that
`f | U_s ∈ Γ(U_s, 𝒪_X)`, hence `U_s ⊂ dom(f)` by definition `(20.1.4)`, and our assertion follows from the lemma
`(20.2.9)`. One may therefore associate to `f` the pseudo-function equal to the class of the section of `𝒪_X` over
`dom(f)`, the restriction of `f`; operating similarly with `X` replaced by an arbitrary open of `X`, one obtains in this
way a canonical homomorphism of `𝒪_X`-Algebras

```text
  (20.2.10.1)            𝓜_X → 𝓜'_X
```

which, by restriction, evidently gives a homomorphism of sheaves of abelian groups

```text
  (20.2.10.2)            𝓜_X^× → 𝓜'_X^×
```

for the sheaves of germs of invertible sections of `𝓜_X` and `𝓜'_X`.

**Proposition (20.2.11).**

<!-- label: IV.20.2.11 -->

*(i) The canonical homomorphism `(20.2.10.1)` (and consequently also `(20.2.10.2)`) is injective.*

*(ii) Suppose either that `X` is locally Noetherian, or that `X` is reduced and the set of its irreducible components is
locally finite. Then the canonical homomorphism `(20.2.10.1)` (and consequently also `(20.2.10.2)`) is bijective.*

The questions being local on `X`, one may restrict to the case `X = Spec(A)` affine, and then show that the canonical
homomorphism `M(X) → M'(X)` is always injective, and that it is bijective in the cases considered in (ii). Taking into
account the definition of the sheaf `𝓜_X` `(20.1.3)`, one may moreover note that `(20.2.10.1)` actually comes from a
homomorphism of presheaves

```text
                         Γ(U, 𝒪_X)[Γ(U, 𝒮)⁻¹] → Γ(U, 𝓜'_X)
```

and it suffices to show that, for `U` affine, this latter is injective (resp. bijective under the hypotheses of (ii)).
Denoting by `S` the set of regular elements of `A` (so that `S⁻¹A` is the total ring of fractions of `A`), one must
therefore consider the canonical homomorphism

```text
  (20.2.11.1)            S⁻¹A → M'(X)
```

<!-- original page 235 -->

and show that it is injective (resp. bijective under the conditions of (ii)). Now, one may write
`S⁻¹A = lim A_t`, where `t` runs over the set of regular elements of `A`, ordered by the relation "`t` is a divisor of
`t'`" `(0_I, 1.4.5)`; one may also write `A_t = Γ(D(t), 𝒪_X)`. On the other hand, one has by definition
`M'(X) = lim Γ(U, 𝒪_X)`, where `U` runs over the set of schematically dense opens of `X` (ordered by `⊃`), and the map
`(20.2.11.1)` is none other than the canonical map coming from the fact that the `D(t)` constitute a part of the set of
schematically dense opens in `X` `(20.2.9)`. Note that, by definition of a schematically dense open, the homomorphism
`Γ(U, 𝒪_X) → Γ(U', 𝒪_X)` for two such opens `U' ⊂ U` is always injective, hence so are the homomorphisms
`Γ(U, 𝒪_X) → M'(X)`, and one concludes that `(20.2.11.1)` is injective. To prove that `(20.2.11.1)` is bijective, it
suffices to show that the set of `D(t)` is cofinal in the set of schematically dense opens, in other words that for
such an open `U`, there exists `t` regular in `A` such that `D(t) ⊂ U`. Now, when `X` is reduced and the irreducible
components of `X` form a locally finite set, this set is finite since `X` was supposed affine, in other words `A` has
only a finite number of minimal prime ideals `𝔭_i`; as `A` is reduced, the intersection of the `𝔭_i` reduces to `0`,
and to say that `t` is regular is therefore equivalent to saying that `t` does not belong to any of the `𝔭_i`; one
concludes by the reasoning of `(I, 7.1.9.1)`. When `A` is Noetherian, saying that `U = X − Y` (where `Y = V(𝔦)` is
closed in `X`) is schematically dense means `(5.10.2)` that `Y` does not meet `Ass(𝒪_X)`, and by virtue of Bourbaki,
_Alg. comm._, chap. IV, §1, n° 4, prop. 8, this entails the existence of a `t ∈ 𝔦` such that `t` is `A`-regular, hence
`U ⊃ D(t)`.

One has moreover proved in the course of this proof the

**Corollary (20.2.12).**

<!-- label: IV.20.2.12 -->

*If `X = Spec(A)`, where `A` is Noetherian, or reduced and having only a finite number of minimal prime ideals, the
schematically dense opens in `X` are those which contain an open of the form `D(t)`, where `t` is regular in `A`, and
`M(X) = M'(X)` is the total ring of fractions `S⁻¹A`, where `S` is the set of regular elements of `X`.*

**Remarks (20.2.13).**

<!-- label: IV.20.2.13 -->

(i) Let `φ` be an element of `M(X)`, `φ'` its image in `M'(X)`; one has evidently, by definition (`(20.1.4)` and
`(20.2.8)`), `dom(φ) ⊂ dom(φ')`; but in fact one has equality `dom(φ) = dom(φ')`, since there exists a section of `𝒪_X`
over `dom(φ')` belonging to the class `φ'`, and the corresponding meromorphic function equals `φ` `(20.2.11, (i))`, so
`dom(φ') ⊂ dom(φ)`.

(ii) One has already noted that when `X` is reduced, one has `𝓜'_X = ℛ(X)` (sheaf of rational functions on `X`
`(I, 7.3.2)`); if moreover the irreducible components of `X` form a locally finite set, one has
`𝓜_X = 𝓜'_X = ℛ(X)`. In general, since every schematically dense open set is dense, one has a canonical homomorphism
`𝓜'_X → ℛ(X)`, but even when `X` is locally Noetherian, this homomorphism is not necessarily injective. For example, if
`X = Spec(A)`, where `A` is a Noetherian ring such that `Ass(A)` contains immersed prime ideals (which entails that `A`
is not reduced), one has seen that `M(X)` and `M'(X)` identify with the total ring of fractions `S⁻¹A`,

<!-- original page 236 -->

where `S` is the set of regular elements of `A`, the complement of the union of the ideals `𝔭 ∈ Ass(A)`; on the other
hand, `R(X)` identifies with `Q⁻¹A`, where `Q` is the complement of the union of the minimal prime ideals of `A`
`(I, 7.1.9)`, and the canonical homomorphism `A → Q⁻¹A` (and *a fortiori* `S⁻¹A → Q⁻¹A`) is therefore not injective,
since there exist in `A − Q` elements `≠ 0` of `A` annihilated by elements of `Q` (Bourbaki, _Alg. comm._, chap. IV,
§1, n° 1, cor. 2 of prop. 1).

(iii) One will note that even when `X` is locally Noetherian, the `𝒪_X`-Module `𝓜_X` is not necessarily quasi-coherent.
Consider for example a Noetherian local ring `A` of dimension `≥ 2`, whose maximal ideal `𝔪` is such that
`𝔪 ∈ Ass(A)` and such that, on setting `X = Spec(A)`, the scheme induced on the open `U` of `X`, complement of `{𝔪}`,
is integral. The only regular elements of `A` are then the invertible elements, so `Γ(X, 𝓜_X) = M(X) = A`; if `𝓜_X`
were quasi-coherent, it would therefore equal `𝒪_X`, but as `U` is an integral scheme, `𝓜_X | U = R(U)` is a simple
sheaf `(I, 7.3.5)`, whereas `𝒪_X` is not a simple sheaf since `dim(A) ≥ 2`.

It remains to give an example of a ring `A` having the preceding properties. It suffices to consider an integral local
ring `B` of dimension `≥ 2` and residue field `k`, and to take `A = B ⊕ k` with the multiplication law
`(b, x)(b', x') = (bb', bx' + b'x)`.

(iv) If `X` is locally Noetherian, it follows from `(5.10.2)` that the schematically dense opens in `X` are those which
contain the set `Ass(𝒪_X)`.

**(20.2.14).** Let `X` be a prescheme, `ℱ` a quasi-coherent and *strictly torsion-free* `𝒪_X`-Module `(20.1.5)`, so
that `ℱ` identifies with an `𝒪_X`-submodule of `𝓜_X(ℱ)`. For every meromorphic section `u` of `ℱ` over `X`, one calls
*Ideal of denominators of `u`* the annihilator `𝒥` of the section `ū` image of `u` in `𝓜_X(ℱ) / ℱ`. The Ideal `𝒥` is
quasi-coherent: indeed, the question being local on `X`, one may restrict to the case where `X` is affine, and there
exists a section `s ∈ Γ(X, 𝒮(𝒪_X))` such that `v = su ∈ Γ(X, ℱ)`. To say that, for an open `U ⊂ X`, a section
`f ∈ Γ(U, 𝒪_X)` belongs to `Γ(U, 𝒥)` means that `f (u | U) ∈ Γ(U, ℱ)`, and since `s | U` is a regular element of
`Γ(U, 𝒪_X)` and `ℱ` is strictly torsion-free, the preceding relation is again equivalent to
`f ((sv) | U) ∈ Γ(U, sℱ)`; if `v̄` is the section of `ℱ / sℱ` which is the canonical image of `v`, one sees therefore
that `𝒥` is the kernel of the homomorphism `𝒪_X → ℱ / sℱ` obtained by multiplication by the section `v̄`. As `ℱ / sℱ`
is quasi-coherent, so is `𝒥`.

It follows at once from the foregoing definition that `dom(u)` is the open complement of the closed subprescheme of `X`
defined by the Ideal of denominators of `u`.

**Proposition (20.2.15).**

<!-- label: IV.20.2.15 -->

*Let `f : X' → X` be a morphism, `ℱ` a quasi-coherent `𝒪_X`-Module, `φ` a section of `𝓜_X(ℱ)` over `X` `(20.1.11)`.
Then `f⁻¹(dom(φ))` is schematically dense in `X'`.*

The question being evidently local on `X` and `X'`, one may suppose `X = Spec(A)`, `X' = Spec(A')` affine, `ℱ = M̃`,
and `φ = h ⊗ (1/s)`, where `h ∈ M` and `s` is a regular element of `A` whose image `s'` in `A'` is a regular element.
One knows then `(20.2.9)` that `D(s')` is a schematically dense open in `X'`, and it is the inverse image under `f` of
`D(s)`, which is contained in `dom(φ)`.

**Remark (20.2.16).**

<!-- label: IV.20.2.16 -->

When `Y` is not separated, the presheaf `U ↦ Ps.hom_S(U, Y)` on `X` is not necessarily a sheaf, even when `X` is
Noetherian, as the following example shows. We shall take for `X` a spectrum of a semi-local Noetherian ring `A` of
dimension `≥ 2`, having exactly two maximal ideals

<!-- original page 237 -->

`𝔪'`, `𝔪''` (so that `X` has exactly two closed points `x'`, `x''`), such that `𝔪'` and `𝔪''` belong to `Ass(A)` and
such that the open `U = X − {x', x''}` is integral. Let `U' = X − {x'}`, `U'' = X − {x''}`, so that `U = U' ∩ U''`.
Note that the only schematically dense opens in `X` are those that contain `x'` and `x''` `(20.2.13, (iv))`, so they
necessarily equal `X`. To have a counter-example, it will therefore suffice to define two `S`-morphisms
`u' : U' → Y`, `u'' : U'' → Y` (with `S = X`) whose restrictions to `U` belong to the same pseudo-morphism of `U` into
`Y`, but which are such that, for every neighbourhood `V'` of `x''` in `U'` and every neighbourhood `V''` of `x'` in
`U''`, the restrictions of `u'` and `u''` to `V' ∩ V''` are distinct. For this, consider an irreducible closed subset
`Z` of `X` containing `x'` and `x''`, distinct from `X`; let `Y` be the `X`-prescheme obtained by gluing two preschemes
`Y'`, `Y''` isomorphic to `X` along the everywhere dense open `X − Z` `(I, 2.3.1)`. One will take for `u'` and `u''`
respectively the restrictions to `U'` and `U''` of the inverse isomorphisms of the structural isomorphisms
`Y' ⥲ X`, `Y'' ⥲ X`. Since `V'` and `V''` contain the generic point of `Z`, the restrictions of `u'` and `u''` to
`V' ∩ V''` are distinct, but the restrictions of `u'` and `u''` to `U − (U ∩ Z)` are equal, and `U − (U ∩ Z)` is a
dense open in `U`, hence schematically dense since `U` is reduced.

It remains then only to define `A` and `Z` so as to have the preceding properties. Let `X_0 = Spec(B)` be an integral
affine scheme (for example the affine plane over a field `k`), `Y` an irreducible closed subset of `X_0` (for example
an affine line) containing two distinct closed points `x'` and `x''`, corresponding to maximal ideals `𝔫'`, `𝔫''` of
`B`. Consider the ring `C = B ⊕ (B/𝔫' ⊕ B/𝔫'')` with the multiplication `(b, z)(b', z') = (bb', bz' + b'z)`. If
`X_1 = Spec(C)`, one has `X_0 = (X_1)_red` and `X_1` is reduced except at the points `x'`, `x''`. It then suffices to
take `A = R⁻¹C`, where `R` is the complement of the union of the maximal ideals of `C` at the points `x'`, `x''`, and
for `Z` the trace of `Y` on `X = Spec(A)`.

### 20.3. Composition of pseudo-morphisms

**(20.3.1).** Let `X`, `Y`, `Z` be three preschemes, `ω` a pseudo-morphism of `X` into `Y`, `f : Y → Z` a morphism. It
is clear that if `U'`, `U''` are two schematically dense opens in `X`, `u' : U' → Y`, `u'' : U'' → Y` two morphisms of
the class `ω`, the morphisms `f ∘ u'` and `f ∘ u''` are equivalent (for the relation defined in `(20.2.1)`); hence, for
all morphisms `u` of the class `ω`, the morphisms `f ∘ u` belong to one and the same equivalence class, which one
denotes `f ∘ ω` and which one calls the *pseudo-morphism of `X` into `Z` composed of `f` and `ω`*. One has
`dom(f ∘ ω) = dom(ω)`. If `g : Z → T` is a morphism, it is clear that `g ∘ (f ∘ ω) = (g ∘ f) ∘ ω`.

**(20.3.2).** Suppose now given a pseudo-`S`-morphism `ω` of `X` into `Y`, where `Y` is separated over `S`, so that
there exists an `S`-morphism `u : dom_S(ω) → Y` of the class `ω` `(20.2.4)`. Let `f : X' → X` be an `S`-morphism such
that the open `V = f⁻¹(dom_S(ω))` is schematically dense in `X'`; one then says that the class (for the equivalence
relation of `(20.2.1)`) of the `S`-morphism `u ∘ (f | V)` (a class defined by virtue of the foregoing hypothesis) is
the *pseudo-`S`-morphism composed of `ω` and `f`*, and one denotes it `ω ∘ f`; it is clear that one has

```text
  (20.3.2.1)             f⁻¹(dom_S(ω)) ⊂ dom_S(ω ∘ f).
```

For `f : X' → X` given, one denotes by `Ps.hom_S(X, Y)^f` the set of pseudo-`S`-morphisms `ω` of `X` into `Y`
satisfying the foregoing condition. If `ω` is such a pseudo-`S`-morphism, it is clear that for every open `V` of `X`,

```text
                         f⁻¹(dom_S(ω | V)) = f⁻¹(V ∩ dom_S(ω)) = f⁻¹(V) ∩ f⁻¹(dom_S(ω))
```

is schematically dense in `f⁻¹(V)`, so, if `f^V : f⁻¹(V) → V` is the restriction of `f`, the composite
`(ω | V) ∘ f^V` is defined and equal to `(ω ∘ f) | f⁻¹(V)`. One thus defines a

<!-- original page 238 -->

canonical restriction map `Ps.hom_S(X, Y)^f → Ps.hom_S(V, Y)^{f^V}`, which permits one to define a presheaf of sets
`V ↦ Ps.hom_S(V, Y)^{f^V}` on `X`, a sub-presheaf of `V ↦ Ps.hom_S(V, Y)`, whence an associated sheaf of sets which one
denotes `𝒫𝓈.hom_S(X, Y)^f`. Moreover, for every open `V` of `X`, one has a map `ω ↦ ω ∘ f^V` from
`Ps.hom_S(V, Y)^{f^V}` to `Ps.hom_S(f⁻¹(V), Y)`, which therefore defines an `f`-morphism of sheaves of sets

```text
                         𝒫𝓈.hom_S(X, Y)^f → 𝒫𝓈.hom_S(X', Y).
```

**(20.3.3).** Let now `f' : X'' → X'` be an `S`-morphism such that the open `f'⁻¹(f⁻¹(dom_S(ω)))` is schematically dense
in `X''`; then `ω ∘ (f ∘ f')` is defined and `u ∘ f ∘ f'` belongs to this pseudo-`S`-morphism; moreover, by virtue of
`(20.3.2.1)`, `f'⁻¹(dom_S(ω ∘ f))` is *a fortiori* schematically dense in `X''`, so `(ω ∘ f) ∘ f'` is also defined and
`u ∘ f ∘ f'` belongs to this pseudo-`S`-morphism, so one has `(ω ∘ f) ∘ f' = ω ∘ (f ∘ f')`.

On the other hand, for every `S`-morphism `g : Y → Z`, one has `dom_S(g ∘ ω) = dom_S(ω)` `(20.3.1)`, so
`(g ∘ ω) ∘ f` is defined, and `g ∘ u ∘ f` belongs to this pseudo-`S`-morphism, which shows that
`(g ∘ ω) ∘ f = g ∘ (ω ∘ f)`.

**(20.3.4).** The most important case in the definition `(20.3.2)` is the one where `𝒫𝓈.hom_S(X, Y)^f = 𝒫𝓈.hom_S(X, Y)`:
for this it suffices that for every open `U` of `X` and every open `V` schematically dense in `U`, `f⁻¹(V)` be
schematically dense in `f⁻¹(U)`; when this is the case, then, for every open `U` of `X` and every pseudo-`S`-morphism
`ω : U → Y`, one may define the composite `ω ∘ f^U`, *even if `Y` is not separated over `S`*. Indeed, if `u' : U' → Y`
and `u'' : U'' → Y` are two morphisms of the class `ω`, they coincide on an open `U_0` schematically dense in `U`,
hence the composite morphisms `f⁻¹(U') → U' → Y` and `f⁻¹(U'') → U'' → Y` coincide on `f⁻¹(U_0)`, which is by
hypothesis schematically dense in `f⁻¹(U)`; one may therefore define `ω ∘ f^U` as the class of any of the morphisms
`f⁻¹(U') → U' → Y`, where `u'` belongs to `ω`.

**Proposition (20.3.5).**

<!-- label: IV.20.3.5 -->

*Let `X`, `X'` be two preschemes, `f : X' → X` a morphism. Then, in each of the following three cases, for every open
`U` of `X` and every open `V` schematically dense in `U`, `f⁻¹(V)` is schematically dense in `f⁻¹(U)`:*

*(i) `f` is flat and locally of finite presentation.*

*(ii) `f` is flat and the underlying space of `X` is locally Noetherian.*

*(iii) `X'` is reduced, the set of irreducible components of `X` is locally finite, and every irreducible component of
`X'` dominates an irreducible component of `X`.*

Assertion (i) follows from `(11.10.5, (ii), b))`; assertion (ii) follows from `(11.10.5, (ii), a))`, since then every
open `V` in `U` is retrocompact, in other words the canonical injection `j : V → U` is a quasi-compact morphism.
Finally, to prove (iii), note that since `X'` is reduced, it suffices to show that for every open `U` of `X` and every
open `V` dense in `U`, `f⁻¹(V)` is dense in `f⁻¹(U)`. Now, for `f⁻¹(V)` to be dense in `f⁻¹(U)`, it suffices that
`f⁻¹(V)` contain all the maximal points of `X'` belonging to `f⁻¹(U)`; the conclusion therefore follows from the
hypothesis that the image under `f` of every

<!-- original page 239 -->

maximal point of `X'` belonging to `f⁻¹(U)` is a maximal point of `X` belonging to `U`, hence to `V` since the set of
irreducible components of `X` is locally finite.

**(20.3.6).** Let `X`, `Y` be two `S`-preschemes; suppose that `X` satisfies one of the two following hypotheses:

a) *`X` is locally Noetherian*;

b) *`X` is reduced and the set of its irreducible components is locally finite*.

Then, for every `x ∈ X`, the canonical `S`-morphism `j : Spec(𝒪_{X,x}) → X` is flat and satisfies condition (ii) of
`(20.3.5)` in case a), condition (iii) of `(20.3.5)` in case b). For every pseudo-`S`-morphism `ω` of `X` into `Y`, the
composite `ω ∘ j` is therefore defined and is a pseudo-`S`-morphism of `Spec(𝒪_{X,x})` into `Y`, called the
*restriction of `ω` to `Spec(𝒪_{X,x})`*. Note now that if `X` satisfies condition a) (resp. b)) of `(20.3.6)`, so does
every prescheme induced on an open `U` of `X` containing `x`. By passage to the inductive limit, one therefore deduces,
from the canonical maps `Ps.hom_S(U, Y) → Ps.hom_S(Spec(𝒪_{X,x}), Y)` thus obtained, a canonical map

```text
  (20.3.6.1)             (𝒫𝓈.hom_S(X, Y))_x → Ps.hom_S(Spec(𝒪_{X,x}), Y)
```

where the first member is the fibre at the point `x` of the sheaf `𝒫𝓈.hom_S(X, Y)`, the set of germs at `x` of
pseudo-`S`-morphisms from open neighbourhoods of `x` into `Y`.

**Proposition (20.3.7).**

<!-- label: IV.20.3.7 -->

*Under the hypotheses of `(20.3.6)`, the canonical map `(20.3.6.1)` is injective. If moreover `Y` is locally of finite
presentation over `S`, the map `(20.3.6.1)` is bijective.*

By application of the method of `(8.1.2, a))`, this proposition will be a particular case of the following:

**Proposition (20.3.8).**

<!-- label: IV.20.3.8 -->

*With the notations of `(8.8.1)`, suppose `X_α` quasi-compact (resp. quasi-compact and quasi-separated) and `Y_α`
locally of finite type (resp. locally of finite presentation) over `S_α`. Suppose moreover that one of the following
conditions is satisfied:*

*(i) The transition morphisms `S_λ → S_α` (for `λ ≥ α`) are flat, and the `X_λ` and `X` are Noetherian.*

*(ii) The `X_λ` are reduced, the set of irreducible components of `X` and of each of the `X_λ` is finite, and, for
`λ ≥ μ`, every irreducible component of `X_λ` dominates an irreducible component of `X_μ`.*

*Then the canonical map*

```text
  (20.3.8.1)             lim Ps.hom_{S_λ}(X_λ, Y_λ) → Ps.hom_S(X, Y)
```

*is injective (resp. bijective).*

Note first that, in case (i), the morphisms `X_λ → X_μ` (for `λ ≥ μ`) and `X → X_λ` are flat, so it follows from
`(20.3.4)` and `(20.3.5)` that the canonical maps

```text
                         Ps.hom_{S_μ}(X_μ, Y_μ) → Ps.hom_{S_λ}(X_λ, Y_λ)
```

<!-- original page 240 -->

for `λ ≥ μ` and `Ps.hom_{S_λ}(X_λ, Y_λ) → Ps.hom_S(X, Y)` are defined (without any separation hypothesis on the `Y_λ`
or `Y`); the same is therefore true of the map `(20.3.8.1)`. The proposition will follow from the following lemma:

**Lemma (20.3.8.2).**

<!-- label: IV.20.3.8.2 -->

*With the notations of `(8.8.1)`, suppose `X_α` quasi-compact, and let `U_α` be an open in `X_α`; let `U_λ` and `U` be
its inverse images in `X_λ` and `X` for `λ ≥ α`. Suppose that one of the conditions (i), (ii) of `(20.3.8)` is
satisfied. Then, for `U` to be schematically dense in `X`, it is necessary and sufficient that there exist `λ ≥ α` such
that `U_λ` is schematically dense in `X_λ`, and in this case `U_μ` is schematically dense in `X_μ` for `μ ≥ λ`.*

Suppose first that condition (i) is satisfied; denote by `j_λ : U_λ → X_λ` and `j : U → X` the canonical injections, by
`𝒥_λ` the kernel of the canonical homomorphism `𝒪_{X_λ} → (j_λ)_*(𝒪_{U_λ})`. The immersion `j_λ` being quasi-compact
and quasi-separated, `(j_λ)_*(𝒪_{U_λ})` is a quasi-coherent `𝒪_{X_λ}`-Module, so `𝒥_λ` is a quasi-coherent Ideal of
`𝒪_{X_λ}`, and since `X_λ` is Noetherian, `𝒥_λ` is coherent, hence of finite type. On the other hand, the transition
morphism `p_{μλ} : X_μ → X_λ` (resp. `p_λ : X → X_λ`) being flat, it follows from `(2.3.1)` that one may identify
`𝒥_μ` with `p_{μλ}*(𝒥_λ)` (resp. `𝒥` with `p_λ*(𝒥_λ)`). The assertion then follows from the definition of a
schematically dense open and from `(8.5.8, (ii))`.

To establish `(20.3.8.2)` when condition (ii) is satisfied, we shall first prove two lemmas.

**Lemma (20.3.8.3).**

<!-- label: IV.20.3.8.3 -->

*Under the hypotheses of `(8.2.2)`, let `M_λ` (resp. `M`) be the set of maximal points of `S_λ` (resp. `S`). Suppose
that for every `λ`, the set `M_λ` is finite, and that the `M_λ` form a projective system of sets. Then `M` is the
projective limit of the system of `M_λ`.*

Let us first show that a point `s ∈ lim M_λ` is maximal in `S`: indeed, if `s'` is a generization of `s`, the image
`s'_λ` of `s'` in `S_λ` is a generization of the image `s_λ` of `s`, hence equal to `s_λ` for every `λ`, which implies
`s' = s`, since the underlying set of `S` is the projective limit of the underlying sets of the `S_λ` `(8.2.9)`.
Conversely, let `s` be a maximal point of `S` and prove that it belongs to `lim M_λ`. Let `s_λ` be the image of `s` in
`S_λ`, `M'_λ` the set of maximal points of `S_λ` which are generizations of `s_λ`; the `M'_λ` are non-empty finite sets,
which form a projective system, so `M' = lim M'_λ` is non-empty and the map `M' → M'_λ` is surjective (Bourbaki, _Ens._,
chap. III, 2nd ed., §7, n° 4, Example I). On the other hand, one has `Spec(𝒪_{S,s}) = lim Spec(𝒪_{S_λ, s_λ})` by virtue
of `(8.2.12)` and `(8.2.9)`, so the points of `lim M'_λ` are also maximal points of `Spec(𝒪_{S,s})` by the first part
of the reasoning. Hence `M' = lim M'_λ` necessarily reduces to the point `s`; one concludes that `M'_λ` reduces to the
point `s_λ`, and consequently the `s_λ` are maximal in the `S_λ`, which finishes the proof of the lemma.

**Lemma (20.3.8.4).**

<!-- label: IV.20.3.8.4 -->

*With the hypotheses being those of `(20.3.8.3)`, suppose moreover `S_α` quasi-compact; let `U_α` be an open set of
`S_α`, and let `U_λ` and `U` be its inverse images in `S_λ` for `λ ≥ α` and in `S`. If `U_α` is dense in `S_α`, `U_λ`
is dense in `S_λ` for `λ ≥ α` and `U` is dense in `S`. Conversely, if `U` is dense in `S` and if moreover the set `M`
of maximal points of `S` is finite, there exists `λ ≥ α` such that `U_λ` is dense in `S_λ`.*

Indeed, since `M_α` is finite, the hypothesis that `U_α` is dense in `S_α` entails that

<!-- original page 241 -->

`M_α ⊂ U_α`, hence `M_λ ⊂ U_λ` for `λ ≥ α` and `M ⊂ U` by virtue of `(20.3.8.3)`, which proves the first assertion.
Conversely, suppose `M` finite and `U` dense in `S`, hence `M ⊂ U`; note that the `U_λ` are open, hence
ind-constructible, and the `M_λ` finite, hence pro-constructible `(1.9.6)`. The second assertion then follows from
`(8.3.2)`.

**(20.3.8.5) End of the proof of (20.3.8.2).** Suppose condition (ii) verified, and note that `X` is then reduced by
virtue of `(8.7.1)`; it amounts to the same to say that `U_λ` (resp. `U`) is schematically dense in `X_λ` (resp. `X`)
or that it is dense in `X_λ` (resp. `X`), and the conclusion follows from `(20.3.8.4)` applied to the `X_λ` and to
`X`.

**(20.3.8.6) End of the proof of (20.3.8).** To show that the map `(20.3.8.1)` is injective, consider two morphisms
`u'_α`, `u''_α` from a schematically dense open `U_α ⊂ X_α` into `Y_α`, and suppose that their images `u'`, `u''`,
morphisms of `U` into `Y`, coincide on a schematically dense open `V` of `U`. Moreover, in either of the hypotheses
(i), (ii), one may suppose `V` quasi-compact; this is evident if `X` is Noetherian; otherwise, as `X` has only a finite
number of maximal points and is reduced, it suffices to replace `V` by the union of a finite number of affine open
neighbourhoods of these maximal points (contained in `V` by hypothesis). Then there exists `λ ≥ α` such that `V` is the
inverse image of a quasi-compact open `V_λ` of `X_λ` `(8.2.11)`, and it follows from `(20.3.8.2)` that, on taking `λ`
large enough, one may suppose `V_λ` schematically dense in `X_λ`. It then follows from `(8.8.2, (i))` that, on taking
`λ` large enough, `u'_λ` and `u''_λ` coincide on `V_λ`, hence belong to the same pseudo-homomorphism.

Let us finally prove that the map `(20.3.8.1)` is surjective. Consider now a morphism `u` from a schematically dense
open `U` of `X` into `Y`; as above, one may suppose `U` quasi-compact and quasi-separated (`U` may be replaced, in case
(ii), by a union of a finite number of pairwise disjoint affine opens). One may then again suppose that there exists
`λ ≥ α` such that `U` is the inverse image of a quasi-compact open `U_λ` of `X_λ` `(8.2.11)` which is automatically
quasi-separated, and by `(20.3.8.2)` one may further suppose that `U_λ` is schematically dense in `X_λ`. Since the
`Y_λ` are supposed locally of finite presentation, it follows from `(8.8.2, (i))` that there exists `λ` such that `u`
is the image of a morphism `u_λ : U_λ → Y_λ`; whence the conclusion.

**Remarks (20.3.8.7).**

<!-- label: IV.20.3.8.7 -->

(i) To prove that the map `(20.3.8.1)` is injective, it is not necessary, under hypothesis (i) of `(20.3.8)`, to suppose
`X` Noetherian. Indeed, the lemma `(20.3.8.2)` does not use this hypothesis. With the notations of `(20.3.8.6)`, let
`Z_λ` be the sub-prescheme of coincidences of `u'_λ` and `u''_λ`, and let `Z` be the sub-prescheme of coincidences of
`u'` and `u''`; it follows from the definition `(17.4.5)` and from `(I, 3.3.10.1)` that `Z` is the projective limit of
the `Z_λ` for `μ ≥ λ`. Now, by hypothesis, `Z` majorizes a schematically dense open in `X`; it follows that `Z` is
itself induced on an open of `X` by virtue of the following lemma:

**Lemma (20.3.8.8).**

<!-- label: IV.20.3.8.8 -->

*Let `T` be a prescheme. Then every sub-prescheme `W` of `T` which majorizes a schematically dense open `V` of `T` is
induced on a (schematically dense) open of `T`.*

Indeed, the subspace of `T` underlying `W` is locally closed, hence open

<!-- original page 242 -->

in its closure, which already proves that the space underlying `W` is open in `T`; the conclusion then follows from
`(11.10.1, c))`.

This lemma being established, one concludes that for `μ ≥ λ` large enough, `Z_μ` is induced on an open of `X_μ` by
virtue of `(8.6.3)`, since `Z_λ`, as sub-prescheme of a Noetherian prescheme, is of finite presentation over `X_λ`
`(1.6.2)`, and the same therefore holds for the `Z_μ` for `μ ≥ λ` over `X_μ` and for `Z` over `X`. One may now apply
`(20.3.8.2)` which shows that for `μ ≥ λ` large enough, `Z` is schematically dense in `X`, whence the conclusion.

(ii) If, under hypothesis (i) of `(20.3.8)`, one suppresses the condition that `X` is Noetherian, one sees that the
reasoning of `(20.3.8.6)` still shows that the image of `(20.3.8.1)` is formed of the pseudo-`S`-morphisms having a
representative which is an `S`-morphism `U → Y`, where `U` is schematically dense in `X` and quasi-compact and
quasi-separated.

**Corollary (20.3.9).**

<!-- label: IV.20.3.9 -->

*Suppose one or the other hypothesis a), b) of `(20.3.6)` on `X` is satisfied, and that `Y` is locally of finite
presentation over `S`. Then, for a pseudo-`S`-morphism `ω` of `X` into `Y` to be defined at the point `x` `(20.2.3)`,
it is necessary and sufficient that its restriction to `Spec(𝒪_{X,x})` be everywhere defined (in other words, be an
`S`-morphism from `Spec(𝒪_{X,x})` into `Y`).*

The following result, which we shall use in the proof of `(20.3.11)`, uses the theory of faithfully flat descent of
chap. VI. The reader can check that the results of `(20.3)` will not be used in this theory.

**Lemma (20.3.10).**

<!-- label: IV.20.3.10 -->

*Let `f : X' → X` be a faithfully flat and quasi-compact `S`-morphism, `X'' = X' ×_X X'`, `p_1` and `p_2` the canonical
projections of `X''` onto `X'`, `Y` a prescheme separated over `S`. Let `U` be an open of `X`, `U' = f⁻¹(U)`,
`U'' = f⁻¹(U') = p_1⁻¹(U') ∩ p_2⁻¹(U')`, and suppose that `U''` is schematically dense in `X''`. Let `g : U → Y` be an
`S`-morphism; then, if `g ∘ (f | U')` extends to an `S`-morphism `X' → Y`, `g` extends to an `S`-morphism `X → Y`.*

One will note that the hypotheses entail that `U` (resp. `U'`) is schematically dense in `X` (resp. `X'`)
`(11.10.5, (i))`; one may therefore again say that if `ω` denotes the pseudo-`S`-morphism class of `g`, the statement
of `(20.3.10)` means that if `ω ∘ f` is everywhere defined, so is `ω`.

To prove `(20.3.10)`, denote by `g'` an `S`-morphism `X' → Y` which extends `g ∘ (f | U')`, and set
`g'_i = g' ∘ p_i : X'' → Y` (`i = 1, 2`). If one sets `f'' = f ∘ p_1 = f ∘ p_2 : X'' → X`, it is clear that `g'_1` and
`g'_2` coincide on `U''` with `g ∘ (f'' | U'')`. But since `Y` is separated over `S` and `U''` schematically dense in
`X''`, one has `g'_1 = g'_2` `(11.10.1, d))`. Since `f` is faithfully flat and quasi-compact, it follows from the
theory of descent (chap. VI) that there exists a unique `S`-morphism `h : X → Y` such that `h ∘ f = g'`; since the
restriction `U' → U` of `f` is a faithfully flat and quasi-compact morphism and that `U'' = U' ×_U U'`, the foregoing
uniqueness result, applied to `U` in place of `X`, shows that `h | U = g`, which proves the lemma.

**Proposition (20.3.11).**

<!-- label: IV.20.3.11 -->

*Let `Y` be an `S`-prescheme separated over `S`, `ω` a pseudo-`S`-morphism of `X` into `Y`, `f : X' → X` an
`S`-morphism. Suppose that `f` is flat, and that one of the following conditions is satisfied:*

<!-- original page 243 -->

*(i) `f` is an open morphism, or surjective and quasi-compact, and `dom_S(ω)` contains an open `U` schematically dense
in `X` and retrocompact in `X`.*

*(ii) `f` is locally of finite presentation.*

*(iii) `Y` is locally of finite presentation over `S`, and `X` satisfies one of the conditions a), b) of `(20.3.6)`.*

*Then `f⁻¹(dom_S(ω))` is schematically dense in `X'`, so that `ω ∘ f` is defined `(20.3.2)` and one has*

```text
  (20.3.11.1)            dom_S(ω ∘ f) = f⁻¹(dom_S(ω)).
```

Let us prove first that `f⁻¹(dom_S(ω))` is schematically dense in `X'`. The question being local on `X` and `X'`, one
may suppose `X` and `X'` affine, and since `f` is flat, it suffices to see, by virtue of `(11.10.5, (ii), a))`, that
`dom_S(ω)` contains an open set `U` retrocompact and schematically dense in `X`. This follows from the hypothesis in
case (i), and from `(20.2.12)` in case (iii), taking into account that in an affine scheme, every open of the form
`D(t)` is retrocompact; finally, in case (ii), one sees directly that `f⁻¹(dom_S(ω))` is schematically dense in `X'`
by applying `(20.3.5, (i))`.

Let us now prove `(20.3.11.1)`, in other words that, for every point `x' ∈ dom_S(ω ∘ f)`, one has
`x = f(x') ∈ dom_S(ω)`. Note first that one may restrict to the case where `f` is *faithfully flat* and quasi-compact.
This is indeed the hypothesis in the second case of (i); in the other cases, the question is local on `X'`, so one may
suppose `X` and `X'` already affine, hence `f` quasi-compact. In the first case of (i) and in case (ii), `f` is an open
morphism `(11.3.1)`, so one may, by replacing `X` by the open `f(X')`, suppose `f` surjective, hence faithfully flat.
In case (iii), using `(20.3.9)`, one may restrict to proving that the restriction of `ω` to `Spec(𝒪_{X,x})` is
everywhere defined, and one may therefore replace `X` by `Spec(𝒪_{X,x})`, `X'` by `X' ×_X Spec(𝒪_{X,x})`, and `f` by
its restriction to this latter prescheme, which is a surjective morphism `(2.3.4)`, hence faithfully flat.

Suppose then `f` faithfully flat and quasi-compact; with the notations of the lemma `(20.3.10)`, it suffices to see
that `U''` is schematically dense in `X''`, taking for `U` an open schematically dense in `X` and contained in
`dom_S(ω)`; this will be the case, by virtue of `(11.10.5, (ii), a))`, if `U` is taken retrocompact in `X` (since the
morphism `f'' : X'' → X` is flat). Now the existence of such an open `U` is part of the hypothesis in case (i); in case
(iii) it follows from `(20.2.12)` and from the fact that in an affine scheme `Spec(A)`, every open of the form `D(t)`
is retrocompact. Finally, in case (ii), let us take `U = dom_S(ω)` and show directly that `U''` is schematically dense
in `X''`: it suffices for this to note that `f'' : X'' → X` is flat and locally of finite presentation and to apply
`(11.10.5, (ii), b))`.

**Corollary (20.3.12).**

<!-- label: IV.20.3.12 -->

*Let `φ` be a pseudo-function on a prescheme `X`. Then, for every flat and locally of finite presentation morphism
`f : X' → X`, the pseudo-function `φ ∘ f` is defined and one has `dom(φ ∘ f) = f⁻¹(dom(φ))`.*

<!-- original page 244 -->

**Remark (20.3.13).**

<!-- label: IV.20.3.13 -->

When `X` satisfies one of the conditions a), b) of `(20.3.6)`, one has seen `(20.2.11)` that the pseudo-functions on
`X` identify with the meromorphic functions on `X`. By virtue of `(20.1.12)` and of `(20.2.13, (i))`, if one supposes
only that the morphism `f : X' → X` is flat, then, for every pseudo-function `φ` on `X`, `φ ∘ f` is defined and one
has `dom(φ ∘ f) = f⁻¹(dom(φ))`.

### 20.4. Properties of the domains of definition of rational maps

**(20.4.1).** Let `X`, `Y` be two `S`-preschemes, `ω` a pseudo-`S`-morphism of `X` into `Y`. Let `u` be an `S`-morphism
`U → Y` belonging to `ω`, where `U` is schematically dense in `X`, and consider the graph `Γ_u`, a sub-prescheme of
`U ×_S Y` `(I, 5.3.11)`, hence a sub-prescheme of `X ×_S Y`. Suppose that this sub-prescheme admits a closure
`(I, 9.5.11)` in `X ×_S Y`; if `j : Γ_u → X ×_S Y` is the canonical injection, this will be the case when the
`𝒪_{X ×_S Y}`-Module `j_*(𝒪_{Γ_u})` is quasi-coherent; it follows from the definition of the equivalence class `ω`
`(20.2.1)` that `j_*(𝒪_{Γ_u})` does not depend on the representative `u` considered, hence the closure prescheme of
`Γ_u` is then well determined by `ω`; one says that this closed sub-prescheme of `X ×_S Y` is the *graph of the
pseudo-`S`-morphism `ω`*, and one denotes it `Γ_ω`. One will note that `Γ_ω` is defined if there exists a morphism
`u : U → Y` of the class `ω` such that `U` is retrocompact in `X` and if moreover `Y` is quasi-separated over `S`,
since then the injection `j` is a quasi-compact and quasi-separated morphism `((1.2.2)` and `(1.7.4))`; the first
hypothesis will always be verified when `X` is locally Noetherian. Note also that when `X` is reduced, so is `Γ_u`,
which is isomorphic to `U` `(I, 5.3.11)`; then `Γ_ω` exists and is none other than the reduced sub-prescheme of
`X ×_S Y` whose underlying space is the closure in `X ×_S Y` of the space underlying `Γ_u` `(I, 5.2.1 and 5.2.2)`.

Note finally that if `Y` is separated over `S`, `Γ_u` is closed in `U ×_S Y` `(I, 5.4.3)`, hence is induced by `Γ_ω`
(when this latter exists) on the open `Γ_ω ∩ (U ×_S Y)` `(I, 9.5.10)`; on the other hand, this induced prescheme is in
general different from `Γ_u` when `Y` is not separated. In particular, if `v : X → Y` is an `S`-morphism, the graph
`Γ_ω` of the class `ω` of `v` may be distinct from the graph `Γ_v`. Accordingly, we shall in what follows, when there
is a question of the graph of a pseudo-`S`-morphism, restrict to the case where `Y` is separated over `S`.

**(20.4.2).** Suppose then `Γ_ω` defined and `Y` separated over `S`; denote by `p` and `q` the restrictions to `Γ_ω` of
the canonical projections

```text
                              X ×_S Y
                              ╱      ╲
                             p        q
                            ╱          ╲
                           X            Y
```

Then, if `U ⊂ dom_S(ω)`, the restriction `p⁻¹(U) → U` of `p` is an isomorphism `(I, 5.3.11)`; conversely, if `U` is an
open of `X` having this property, and if `u` is the inverse isomorphism of the restriction `p⁻¹(U) → U` of `p`, `q ∘ u`
is an `S`-morphism of `U` into `Y` which coincides with a morphism of the class `ω` on `U ∩ dom_S(ω)`. One concludes
that `dom_S(ω)` is the *largest open `U` of `X` such that the restriction `p⁻¹(U) → U` of `p` is an*

<!-- original page 245 -->

*isomorphism*. Let `v : dom_S(ω) → Γ_ω` be the `S`-morphism inverse of the restriction
`p⁻¹(dom_S(ω)) → dom_S(ω)` of `p`; one sometimes denotes `p⁻¹` the pseudo-`S`-morphism of `X` into `Γ_ω`, the class of
`v` (whose associated rational map `(20.2.13, (ii))` is then birational); as `p⁻¹(dom_S(ω))` is the graph of the
`S`-morphism `u = q ∘ v : dom_S(ω) → Y`, it is schematically dense in `Γ_ω` `(11.10.3, (iv))`, so `ω` may be regarded
as the composite `q ∘ p⁻¹` `(20.3.2)`. For every subset `M` of the underlying space of `X`, one sometimes sets
`ω(M) = q(p⁻¹(M))`, which then amounts to regarding `ω` as a map from `X` into `𝔓(Y)` (or, as certain authors say, a
"multivalued function"). One will note that when `x ∈ dom_S(ω)`, `ω({x})` is the set `{u(x)}`; in general, for an
arbitrary `x ∈ X`, if one denotes by `s` the image of `x` in `S`, by `Y_s` the fibre at the point `s` of the structure
morphism `Y → S`, the set `ω({x})` is a subset of the prescheme `Y_s`.

**(20.4.3).** In all the rest of this number, we restrict to the case where `X` is *reduced*, so that there is then
identity between pseudo-`S`-morphisms and `S`-rational maps `(20.2.7)`. Moreover, the graph of every `S`-rational map
of `X` into `Y` is then defined `(20.4.1)`.

**Proposition (20.4.4).**

<!-- label: IV.20.4.4 -->

*Let `X` be a locally integral `S`-prescheme, `Y` an `S`-prescheme locally of finite type and separated over `S`, `ω`
an `S`-rational map of `X` into `Y`, `p : Γ_ω → X` the canonical projection. Then, if `x ∈ X` is a normal point such
that the set `p⁻¹(x)` contains an isolated point, `ω` is defined at the point `x`.*

Indeed, the first projection `p_1 : X ×_S Y → X` is then a separated morphism, locally of finite type, so the same is
true of its restriction `p : Γ_ω → X`, which is moreover birational; and since `Γ_u` is reduced and `X` integral,
`Γ_ω` is integral; it then follows from `(Err_{IV}, 30)` that the hypothesis on `x` entails the existence of an open
neighbourhood `U` of `x` such that the restriction `p⁻¹(U) → U` of `p` is an isomorphism; whence the conclusion
`(20.4.2)`.

One will note that the statement `(20.4.4)` is the original formulation given by Zariski of his *Main theorem* (with
the restriction that he was restricting to algebraic schemes over a base field).

**Proposition (20.4.5).**

<!-- label: IV.20.4.5 -->

*The hypotheses and notations being those of `(20.4.4)`, suppose moreover `X` normal, and let `X'` be a reduced
prescheme, `f : X' → X` a morphism locally of finite type and universally open. Then `ω ∘ f` is defined, and one has
`dom_S(ω ∘ f) = f⁻¹(dom_S(ω))` (in other words, if `x' ∈ X'` and `x = f(x')`, then, for `ω` to be defined at the point
`x`, it is necessary and sufficient that `ω ∘ f` be so at the point `x'`).*

As `X'` is reduced and `f⁻¹(dom_S(ω))` everywhere dense in `X'` by virtue of `(2.4.11)`, the composite `ω ∘ f` is
defined; to prove that, when `ω ∘ f` is defined at the point `x'`, `ω` is so at the point `x`, one may evidently
replace `X'` by an open neighbourhood of `x'`, hence suppose `ω ∘ f` everywhere defined; moreover, as `f(X')` is open
in `X`, one may suppose `f` surjective. By virtue of the hypothesis on `f`, the morphism
`f_{(Y)} : X' ×_S Y → X ×_S Y` is then open, hence `f_{(Y)}(M̄) = ‾{f_{(Y)}(M)}` for every subset `M` of `X ×_S Y`;
taking for `M` the set `Γ_u`, where `u : dom_S(ω) → Y` is the restriction of `ω` to `dom_S(ω)`, it follows from the
preceding relation and from `(I, 5.3.12)` that the set underlying `Γ_{ω ∘ f}` equals `f_{(Y)}(Γ_ω)`; as one knows

<!-- original page 246 -->

that `Γ_{ω ∘ f}` is a reduced prescheme `(20.4.1)`, one sees that the `X'`-prescheme `Γ_{ω ∘ f}` equals
`(Γ_ω ×_X X')_red`. But since by hypothesis the composite morphism `Γ_{ω ∘ f} → Γ_ω ×_X X' → X'` is an isomorphism,
`p_{(X')}` is necessarily radicial; as `f` is surjective, the same is true of `p : Γ_ω → X` `(I, 3.4.8)`, so
`p⁻¹(x)` is a set reduced to a point `(I, 3.6.4)`; it then follows from `(20.4.4)` that `ω` is defined at the point
`x`.

The following proposition gives a valuative criterion for a rational map to be defined at a point:

**Proposition (20.4.6).**

<!-- label: IV.20.4.6 -->

*Let `S` be a prescheme, `X`, `Y` two `S`-preschemes; suppose `X` locally Noetherian, `Y` locally of finite type over
`S`. Let `U` be a dense open in `X`, `h : U → Y` an `S`-morphism, `x ∈ X − U` a normal point of `X`,
`h_x : Spec(k(x)) → Y` an `S`-morphism. In order that `h` can be extended to an `S`-morphism `h' : U' → Y`, where `U'`
is an open of `X` containing `U` and `x`, and such that the composite morphism `Spec(k(x)) → U' → Y` is the given
`S`-morphism `h_x`, it is necessary and sufficient that the following condition be verified:*

*(P) For every spectrum `S_1` of a discrete valuation ring, with closed point `a` and generic point `b`, and every
morphism `u : S_1 → X` such that `u(a) = x`, `u(b) ∈ U`, the composite morphism
`h'_1 = h ∘ (u | {b}) : {b} = u⁻¹(U) → Y` extends to a morphism `h'_1 : S_1 → Y` such that the diagram*

```text
                         Spec(k(a)) ────→ S_1
                              │            │
                              │            │ h'_1
                              ↓            ↓
                         Spec(k(x)) ────→ Y
                                    h_x
```

*is commutative.*

*Moreover, if this condition is verified, and if `h'' : U'' → Y` is a morphism satisfying the same conditions as `h'`,
then there exists an open set containing `U ∪ {x}` on which `h'` and `h''` coincide.*

Let us first prove the last assertion; one may suppose `h'` and `h''` defined on the same open `U_0 ⊃ U ∪ {x}`. The
sub-prescheme `Z` of coincidences of `h'` and `h''` `(17.4.5)` contains `U` and `x`, so there is an open neighbourhood
`V` of `x` in `U_0` such that the sub-prescheme induced by `Z` on the open `Z ∩ V` is a closed sub-prescheme of the
prescheme induced by `X` on `V`; as this prescheme `Z ∩ V` majorizes the sub-prescheme induced by `V` on the open
`U ∩ V`, and this latter is schematically dense in `V`, `Z ∩ V` is necessarily equal to `V` `(20.3.8.8)`, which proves
that `h'` and `h''` coincide on `U ∪ V`.

The necessity of the condition of the statement being evident, let us prove that it is sufficient. By virtue of the
biunivocal correspondence between `S`-morphisms of `X` into `Y` and `X`-sections of `X ×_S Y` `(I, 3.3.15)`, one may
restrict to the case where `S = X` and where `h` is therefore a `U`-section of `Y`; one will note that then `Y` is
locally Noetherian, and one may evidently (since `X` is locally integral and locally Noetherian) suppose `X = S`
irreducible. Moreover, taking into account `(20.3.7)`, one may suppose that `X = Spec(A)`, where `A` is a Noetherian
integral integrally closed local ring.

<!-- original page 247 -->

Note that for every `x' ∈ U`, `h(x')` is a specialization of `h_x(x) = y`. Indeed, there exists a spectrum `S_1` of a
discrete valuation ring and a morphism `u : S_1 → X` such that `u(a) = x`, `u(b) = x'` `(II, 7.1.9)`. Applying the
condition of the statement, one obtains at once our assertion, since `h(x') = h_1(b) = h'_1(b)` and `y = h'_1(a)`. If
`Y'` is an open affine neighbourhood of `y`, one therefore has `h(X ∩ U) ⊂ Y'`; one may consequently replace `Y` by
`Y'`, in other words *suppose `Y` affine*, hence separated over `X`. Let `ω` be the `X`-rational section of `Y` to
which `h` belongs, so that its graph has here as underlying set the closure of `h(U)` in `Y`. Since `Y` is separated
over `X`, one may apply `(20.4.4)` to `ω`: it will suffice to prove that, if `p : Γ_ω → X` is the canonical
projection, `p⁻¹(x)` is reduced to a single point `y` and that `h_x(x) = y`. Indeed, by `(20.4.4)`, `h` will extend to
a section `h'` over an open `U'` containing `U ∪ {x}`, such that `h'(x) = y`, and since then there exists only one
`X`-morphism `Spec(k(x)) → Y` sending `x` to `y`, this will prove the identity of `h_x` and the composite of `h'` and
`Spec(k(x)) → U'`.

Since for `x' ∈ X ∩ U`, `h(x')` is a specialization of `y`, one has `y ∈ p⁻¹(x)`. Suppose then that `η` is an
arbitrary point of `p⁻¹(x)`. Since `Γ_ω` is the closure of `h(U)` and `h(U)` is formed of points adherent to `h(ξ)`,
where `ξ` is the generic point of `X`, `Γ_ω` is the closure of `h(ξ)` in `Y`. One then takes a spectrum `S_1` of a
discrete valuation ring and a morphism `v : S_1 → Y` such that `v(a) = η`, `v(b) = h(ξ)` `(II, 7.1.9)`, and one sets
`u = p ∘ v`, so that `u(a) = x`, `u(b) = ξ`. Applying to `u` the condition of the statement, one sees that one
obtains a morphism `h'_1 : S_1 → Y` such that `h'_1(a) = y` and `h'_1(b) = h(ξ)`; but this entails `η = y` by virtue
of `(II, 7.2.3)`, since `Y` is separated over `X` and `v` and `h'_1` must therefore coincide, since they are equal at
the point `b`. Q.E.D.

**Corollary (20.4.7).**

<!-- label: IV.20.4.7 -->

*The hypotheses on `S`, `X`, `Y`, `U` and `h` being those of `(20.4.6)`, let `E` be a subset of `X − U` such that `X`
is normal at every point of `E`, and for each `x ∈ E`, let `h_x : Spec(k(x)) → Y` be an `S`-morphism such that the
condition (P) of `(20.4.6)` is verified. Suppose moreover that the union `F` of the graphs of the `h_x` (identified
with subsets of `X ×_S Y`) for `x ∈ E` is contained in the union of a finite number of opens `V_i` of `X ×_S Y` which
are separated over `X` (a condition automatically verified if `Y` is separated over `S`, or if `X` is quasi-compact
and `Y` of finite type over `S`). Then there exists an `S`-morphism `h' : U' → Y`, where `U'` is an open of `X`
containing `U ∪ E`, such that, for every `x ∈ E`, the composite*

```text
                         Spec(k(x)) → U' → Y
```

*equals `h_x`.*

Note first that, in `(20.4.6)`, if `Y` is supposed separated, there is a largest open `U_0 ⊃ U`, equal to the domain of
the `S`-rational map corresponding to `h`, on which `h` can be extended, and this extension is unique `(I, 7.2.2)`;
whence the conclusion in this case, thanks to `(20.4.6)`. In the general case, let `E_i` be the set of `x ∈ E` such
that `(x, h_x(x)) ∈ V_i`. By virtue of `(20.4.6)`, for every `x ∈ E`, there is an extension `h^{(x)}` of `h` to
`U ∪ W^{(x)}`, where `W^{(x)}` is a neighbourhood of `x` in `X` such that the graph of `h^{(x)} | W^{(x)}` is contained
in every `V_i` such that `x ∈ E_i`. Since `V_i` is separated over `X` and `X` reduced, for two points `x'`, `x''` of
`E_i`, `h^{(x')}` and `h^{(x'')}` coincide on `W^{(x')} ∩ W^{(x'')}` since they

<!-- original page 248 -->

coincide on the everywhere dense open `U ∩ W^{(x')} ∩ W^{(x'')}` of this set. There is therefore a morphism
`h_i : U ∪ U_i → Y` which extends `h` to an open `U ∪ U_i` containing `E_i`; moreover, for every pair of indices `i`,
`j`, the graphs of the restrictions `h_i | (U_i ∩ U_j)` and `h_j | (U_i ∩ U_j)` are contained in `V_i ∩ V_j`; as
`V_i ∩ V_j` is separated over `X` and the foregoing morphisms coincide on an everywhere dense open
`U ∩ U_i ∩ U_j` of `U_i ∩ U_j`, they are equal. The morphism `h'` equal to `h` on `U`, to `h_i` on each of the `U_i`,
answers the question.

**Remark (20.4.8).**

<!-- label: IV.20.4.8 -->

When `E = X − U`, it is clear that if, for every affine open `T` of `X`, there exists an `S`-morphism `h_T : T → Y`
extending `h | (U ∩ T)` and such that the composite `Spec(k(x)) → T → Y` equals `h_x` for every `x ∈ T − (U ∩ T)`,
then the `h_T` are the restrictions of an `S`-morphism `h' : X → Y` (everywhere defined) by virtue of the uniqueness
assertion in `(20.4.6)`. To prove the existence of `h'`, one is therefore reduced to the case where `X` is affine, and
then it suffices that the set `F`, union of the graphs of the `h_x`, be quasi-compact in `X ×_S Y` for one to be able
to apply `(20.4.7)`. This will be the case when the `h_x` are of the form `Spec(k(x)) → Z → Y`, where `Z` is a closed
sub-prescheme of `X` having `X − U` as underlying space, and `h_x` an `S`-morphism.

**Corollary (20.4.9).**

<!-- label: IV.20.4.9 -->

*Let `S` be a locally Noetherian prescheme, `X` a locally Noetherian prescheme, `f : X → S` a flat morphism,
`g : Y → S` a morphism locally of finite type. Let `U` be a dense open in `S`, `h : f⁻¹(U) → Y` an `S`-morphism,
`T = S − U`, `Z` the reduced closed sub-prescheme of `X` having `f⁻¹(T)` as underlying space, `h_0 : Z → Y` an
`S`-morphism. Suppose `X` normal at every point of `Z`. In order that there exist an `S`-morphism (necessarily unique)
`h' : X → Y` extending `h` and `h_0`, it is necessary and sufficient that the following condition be satisfied:*

*For every spectrum `S_1` of a discrete valuation ring, with closed point `a` and generic point `b`, and every morphism
`u : S_1 → S` such that `u(a) ∈ T` and `u(b) ∈ U`, there exists an `S_1`-morphism
`h'_1 : X_{(S_1)} → Y_{(S_1)}` extending `h_1 : f⁻¹(b) → Y_b` and such that the diagram*

```text
                         Spec(k(z)) ────→ Z_{(S_1)}
                              │              │
                              │              │ h_0(S_1)
                              ↓              ↓
                          X_{(S_1)} ────→ Y_{(S_1)}
                                     h'_1
```

*is commutative for every `z ∈ Z_{(S_1)}`.*

Indeed, the hypothesis that `f` is flat entails that `f⁻¹(U)` is dense in `X` `(2.3.10)`, and it then suffices to apply
`(20.4.8)`.

**Corollary (20.4.10).**

<!-- label: IV.20.4.10 -->

*Under the hypotheses of `(20.4.6)`, suppose moreover `Y` separated and locally quasi-finite over `S`. Let `U` be a
dense open in `X`, `h : U → Y` an `S`-morphism, `ω` the corresponding `S`-rational map, `x ∈ X − U` a normal point of
`X`. In order that `ω` be defined at the point `x`, it is necessary and sufficient that the following condition be
verified: there exists a spectrum `S_1` of a discrete valuation ring, with closed point `a` and generic point `b`, and
a morphism `u : S_1 → X`*

<!-- original page 249 -->

*such that `u(a) = x`, `u(b) ∈ U` and such that the `S`-rational map `ω ∘ u` is everywhere defined.*

Indeed, by hypothesis all the fibres of the projection morphism `X ×_S Y → X` are formed of isolated points, and to
apply `(20.4.4)` it suffices to know that the fibre `p⁻¹(x)` is non-empty in `Γ_ω`. Now if `h_1` is the unique
morphism of the class `ω ∘ u`, the unique point of `X ×_S Y` above `x` and `h_1(a)` belongs to `Γ_ω`, whence the
conclusion.

**Proposition (20.4.11).**

<!-- label: IV.20.4.11 -->

*Let `X` be a locally Noetherian prescheme, `Y` an `S`-prescheme affine over `S`, `U` an open of `X`, `Z = X − U`.
Suppose that one has `prof_Z(𝒪_X) ≥ 2` `(5.10.1)`; then every `S`-morphism `f : U → Y` extends in a unique way to an
`S`-morphism of `X` into `Y`.*

One may restrict to the case where `S` and `X` are affine and (by virtue of `(I, 3.3.14)`) to the case where `S = X`;
one has therefore `X = Spec(A)`, `Y = Spec(B)`, `B` being an `A`-algebra of finite type. As `B` is a quotient of a
polynomial algebra `A[(T_λ)]_{λ ∈ L}`, `Y` is a closed sub-prescheme of `Y' = X[(T_λ)]_{λ ∈ L}`. On the other hand,
the hypothesis on `Z` entails that `U` is schematically dense in `X` by virtue of `(20.2.13, (iv))` and `(5.10.2)`. If
one proves that every `X`-morphism `u : U → Y'` extends in a unique way to an `X`-morphism `v' : X → Y'`, it will
result that `v'` factors as `X → Y → Y'`: indeed, the sub-prescheme `v'⁻¹(Y)` is closed and majorizes `U`
`(I, 4.4.1)`, so is identical to `X` `(20.3.8.8)`. Under these conditions, `v` will be the unique `S`-morphism of `X`
into `Y` extending `u`. One may therefore restrict to the case `Y = Y'`. But then there is a biunivocal correspondence
between the `X`-morphisms from an open `U ⊂ X` into `Y'` and the families `(s_λ)_{λ ∈ L}` of sections of `𝒪_X` over
`U` `(II, 1.7.9)`; the conclusion therefore follows from `(5.10.5)`.

**Corollary (20.4.12).**

<!-- label: IV.20.4.12 -->

*Let `X` be a locally Noetherian reduced `S`-prescheme satisfying condition `(S_2)` `(5.7.2)` (for example a locally
Noetherian normal `S`-prescheme `(5.8.6)`), `Y` an `S`-prescheme affine over `S`, `f` an `S`-rational map of `X` into
`Y`; then every irreducible component of `X − dom(f)` is of codimension `1` in `X`.*

It amounts to the same to say that if `Z_2` is the set of `x ∈ X` such that `dim(𝒪_{X,x}) ≥ 2`, then, for every closed
subset `Z ⊂ Z_2` of `X`, every `S`-morphism of `X − Z` into `Y` extends to an `S`-morphism of `X` into `Y`; now this
follows from the hypothesis on `X` `(5.7.2)` and from `(20.4.11)`.

### 20.5. Relative pseudo-morphisms

**(20.5.1).** Let `X`, `Y` be two `S`-preschemes. It follows from the definitions `(11.10.8)` that the intersection of
two opens `U`, `U'` of `X`, *universally schematically dense relative to `S`*, again possesses this property. One
therefore defines an equivalence relation between `S`-morphisms `u : U → Y` by replacing in `(20.2.1)` "schematically
dense" by "universally schematically dense relative to `S`". An equivalence class under this relation is called a
*pseudo-morphism of `X` into `Y` relative to `S`*, and the set of these classes is denoted `Ps.hom_{X/S}(X, Y)`.

**(20.5.2).** Since every open of `X` universally schematically dense relative to `S` is in particular schematically
dense, the elements of a pseudo-morphism

<!-- original page 250 -->

of `X` into `Y` relative to `S` are equivalent in the sense of `(20.2.1)`, whence a canonical map

```text
  (20.5.2.1)             Ps.hom_{X/S}(X, Y) → Ps.hom_S(X, Y).
```

**Proposition (20.5.3).**

<!-- label: IV.20.5.3 -->

*Suppose `Y` separated over `S`. Then:*

*(i) The map `(20.5.2.1)` is injective and identifies `Ps.hom_{X/S}(X, Y)` with the subset of `Ps.hom_S(X, Y)` formed
of pseudo-`S`-morphisms `ω` such that `dom_S(ω)` is universally schematically dense relative to `S`.*

*(ii) The presheaf `U ↦ Ps.hom_{U/S}(U, Y)` on `X` is a sheaf.*

Assertion (i) is immediate, since saying that two `S`-morphisms `u : U → Y`, `u' : U' → Y` are equivalent in the sense
of `(20.2.1)` means then that they are the restrictions of the same morphism `dom_S(ω) → Y` `(20.2.4)`, and if `U` and
`U'` are universally schematically dense relative to `S`, the same is *a fortiori* true of `dom_S(ω)`. To prove (ii),
note that `U ↦ Ps.hom_S(U, Y)` is then a sheaf `(20.2.6)`; on the other hand, given an open cover `(U_α)` of `U`, and
a pseudo-`S`-morphism `ω` of `U` into `Y`, for `dom_S(ω)` to be universally schematically dense in `U` relative to `S`,
it follows at once from the definitions (cf. `(20.2.1)`) that it is necessary and sufficient that each of the sets
`dom_S(ω) ∩ U_α = dom_S(ω | U_α)` be universally schematically dense in `U_α` relative to `S`; whence (ii).

When `Y` is separated, one will denote `𝒫𝓈.hom_{X/S}(X, Y)` the subsheaf

```text
                         U ↦ Ps.hom_{U/S}(U, Y)
```

of `𝒫𝓈.hom_S(X, Y)`.

When `X` is flat and locally of finite presentation over `S` and `Y` separated over `S`, the pseudo-morphisms of `X`
into `Y` relative to `S` again identify with the pseudo-`S`-morphisms `ω` such that, for every fibre `X_s` of the
morphism `X → S`, `dom_S(ω) ∩ X_s` is schematically dense in `X_s` `(11.10.10)`.

**(20.5.4).** A particularly important case where `Y` is separated over `S` is the case `Y = S[T] = S ⊗_ℤ Spec(ℤ[T])`
(`T` indeterminate). There is then a biunivocal correspondence between the pseudo-`S`-morphisms of `X` into `Y` and the
pseudo-functions on `X` `(20.2.8)` by virtue of the definition of a product of ℤ-preschemes. The pseudo-morphisms of
`X` into `Y` relative to `S` then identify, by virtue of `(20.5.3)`, with the *pseudo-functions `φ` on `X` such that
`dom(φ)` is universally schematically dense relative to `S`*. The sheaf `𝒫𝓈.hom_{X/S}(X, Y)` is a subsheaf of *rings*
of `𝓜'_X`, which one denotes `𝓜'_{X/S}`.

One then sets `Ps.hom_{X/S}(X, Y) = M'(X/S)` and one says that its elements are the *pseudo-functions on `X` relative
to `S`*.

**(20.5.5).** Let `X`, `Y`, `Z` be three `S`-preschemes, `f : Y → Z` an `S`-morphism. One may, in the reasoning of
`(20.3.1)`, replace everywhere "schematically dense" by "universally schematically dense relative to `S`"; for every
pseudo-morphism `ω ∈ Ps.hom_{X/S}(X, Y)`, the morphisms `f ∘ u`, where `u` runs through `ω`, therefore belong to one
and the same equivalence class (for the relation defined in `(20.5.1)`), which one

<!-- original page 251 -->

calls the *pseudo-morphism of `X` into `Z`, relative to `S`, composed of `f` and `ω`*, and which one denotes
`f ∘ ω`. If `g : Z → T` is a morphism, it is immediate that `g ∘ (f ∘ ω) = (g ∘ f) ∘ ω`.

**(20.5.6).** Suppose `Y` separated over `S`, and let `ω` be a pseudo-morphism of `X` into `Y` relative to `S`. If
`f : X' → X` is an `S`-morphism such that `f⁻¹(dom_S(ω))` is universally schematically dense in `X'` relative to `S`,
it follows from `(20.3.2)` that the pseudo-`S`-morphism `ω ∘ f` has a domain universally schematically dense relative
to `S`, hence `(20.5.3)` may be considered as a pseudo-morphism relative to `S`. When `X'` is flat and locally of
finite presentation over `S`, the condition that `f⁻¹(dom_S(ω))` be universally schematically dense relative to `S` is
again equivalent to saying that for every `s ∈ S`, `(f⁻¹(dom_S(ω)))_s` (notation of `(11.10.10)`) be schematically
dense in `X'_s`, or further, denoting `f_s : X'_s → X_s` the morphism deduced from `f` by base change, that the inverse
image under `f_s` of `(dom_S(ω))_s` be schematically dense in `X'_s`. This latter condition will in particular be
verified if, for every `s ∈ S`, `X_s`, `X'_s` and `f_s` satisfy one of the three conditions (i), (ii), (iii) of
`(20.3.5)`.

**(20.5.7).** Suppose now that `X` and `X'` are both `S`-preschemes flat and locally of finite presentation over `S`,
and that `f : X' → X` is a flat `S`-morphism (or, what amounts to the same `(11.3.10)`, that for every `s ∈ S`,
`f_s : X'_s → X_s` is a flat morphism). Then, for every open `U` of `X` and every open `V ⊂ U` universally
schematically dense in `U` relative to `S`, it follows from `(11.10.5)` and `(11.10.9)` that `f⁻¹(V)` is universally
schematically dense in `f⁻¹(U)` relative to `S`. For every pseudo-morphism `ω` of `X` into `Y` relative to `S`, it
follows from `(20.3.4)` that the pseudo-`S`-morphism `ω ∘ f` is defined and is a pseudo-morphism of `X'` into `Y`
relative to `S`, *even when `Y` is not supposed separated over `S`*. One deduces that in this case, for every
`S`-morphism `g : Y → Z`, `(g ∘ ω) ∘ f` is again defined and equal to `g ∘ (ω ∘ f)` (with the definitions of
`(20.5.1)`), and is therefore a pseudo-morphism relative to `S`.

**(20.5.8).** Let `X` be an `S`-prescheme, `S' → S` an arbitrary morphism, `X' = X_{(S')}`, `g : X' → X` the canonical
projection. Then, for every open `U` of `X` and every open `V ⊂ U` universally schematically dense in `U` relative to
`S`, `V' = g⁻¹(V)` is universally schematically dense in `U' = g⁻¹(U)` relative to `S'` by definition `(11.10.8)`. Let
then `ω` be a pseudo-morphism of `X` into an `S`-prescheme `Y` relative to `S`; if `u_1`, `u_2` are `S`-morphisms of
the class `ω`, defined respectively on opens `U_1`, `U_2` of `X` universally schematically dense in `X` relative to
`S`, it follows from the foregoing that the morphisms `u'_1 = u_1 ∘ (g | g⁻¹(U_1))` and
`u'_2 = u_2 ∘ (g | g⁻¹(U_2))` coincide on an open `U'_3` universally schematically dense relative to `S'`. Now, if
`Y' = Y_{(S')}` and if `h : Y' → Y` is the canonical projection, `u'_1` and `u'_2` factor canonically as
`u'_1 = h ∘ v_1`, `u'_2 = h ∘ v_2`, and `v_1` and `v_2` are two `S'`-morphisms into `Y'` which coincide on `U'_3`. One
therefore sees that when `u_1` runs through the class `ω`, the corresponding `S'`-morphisms `v_1` belong to one and
the same pseudo-morphism relative to `S'`, called the *inverse image of `ω` under the base-change morphism `S' → S`*
and denoted `ω_{(S')}`. It is clear that if `S'' → S'` is a second morphism, one has `(ω_{(S')})_{(S'')} = ω_{(S'')}`
(for the composite base-change morphism `S'' → S' → S`).

<!-- original page 252 -->

### 20.6. Relative meromorphic functions

**(20.6.1).** Let `S` be a prescheme, `X` an `S`-prescheme which is flat and locally of finite presentation over `S`;
for every `s ∈ S`, we shall denote by `X_s` the fibre at the point `s` of the structure morphism `X → S`. In general,
if `φ` is a meromorphic function on `X`, it is not possible to associate to it, in a "natural" way, for each `s ∈ S`,
an "induced" meromorphic function on `X_s` `(20.1.11)`. For every open `U` of `X`, denote by `𝒮_{X/S}(U)` the set of
sections `t ∈ Γ(U, 𝒪_X)` such that, for every `s ∈ S`, the image `t_s` of `t` under the canonical homomorphism
`Γ(U, 𝒪_X) → Γ(U ∩ X_s, 𝒪_{X_s})` is a *regular* section; this implies moreover, by the equivalence of a) and b) in
`(11.3.7)`, that `t` is itself a regular section. It is clear that `U ↦ 𝒮_{X/S}(U)` is a subsheaf of the sheaf of sets
`𝒮 = 𝒮(𝒪_X)` (notation of `(20.1.3)`), which one denotes `𝒮_{X/S}`; one sets

```text
  (20.6.1.1)             𝓜_{X/S} = 𝒪_X[𝒮_{X/S}⁻¹]
```

(notation of `(20.1.1)`) and one says that this sheaf of rings is the *sheaf of germs of meromorphic functions on `X`
relative to `S`*; its sections over `X` are called *meromorphic functions on `X` relative to `S`* and their set is
denoted `M(X/S)`. It is clear that `𝓜_{X/S}` is a subsheaf of `𝓜_X = 𝒪_X[𝒮⁻¹]`; for every meromorphic function
`φ ∈ M(X/S)` and every `s ∈ S`, the inverse image of `φ` under the canonical injection morphism `j_s : X_s → X` is then
defined `(20.1.11)`, and denoted `φ_s`.

**(20.6.2).** Now let `ℱ` be a quasi-coherent `𝒪_X`-Module; one sets

```text
  (20.6.2.1)             𝓜_{X/S}(ℱ) = ℱ ⊗_{𝒪_X} 𝓜_{X/S};
```

the sections of `𝓜_{X/S}(ℱ)` are called *meromorphic sections of `ℱ` over `X`, relative to `S`* and their set is
denoted `M(X/S, ℱ)`. The canonical homomorphism `ℱ → 𝓜_{X/S}(ℱ)` is not necessarily injective; when it is, one says
that `ℱ` is *torsion-free relative to `S`*: this means that for every open `U` of `X` and every section
`t ∈ 𝒮_{X/S}(U)`, `t` is `(ℱ | U)`-regular; this condition is *a fortiori* verified when `ℱ` is strictly torsion-free
`(20.1.5)`. In this latter case, it follows at once from the definitions `(20.1.2)` that the canonical homomorphism of
`𝒪_X`-Modules

```text
  (20.6.2.2)             𝓜_{X/S}(ℱ) → 𝓜_X(ℱ)
```

is injective, so that the meromorphic sections of `ℱ` relative to `S` are meromorphic sections of `ℱ` in the sense of
`(20.1.3)`.

**Proposition (20.6.3).**

<!-- label: IV.20.6.3 -->

*The image, under the injective homomorphism `(20.2.10.1)`, of the subsheaf `𝓜_{X/S}` of `𝓜_X` is the subsheaf
`𝓜'_{X/S}` of pseudo-functions on `X` relative to `S` (i.e. of pseudo-functions whose domain of definition is
universally schematically dense relative to `S` `(20.5.4)`).*

One may evidently restrict to proving that the image of `M(X/S)` under the canonical homomorphism `M(X) → M'(X)` equals
`M'(X/S)`; the proposition is then a consequence of the following more general proposition:

<!-- original page 253 -->

**Proposition (20.6.4).**

<!-- label: IV.20.6.4 -->

*Let `ℱ` be a quasi-coherent `𝒪_X`-Module of finite presentation and strictly torsion-free. Then, for a meromorphic
section `φ` of `ℱ` over `X` to be a meromorphic section relative to `S`, it is necessary and sufficient that `dom(φ)`
be universally schematically dense relative to `S`.*

The necessity of the condition follows from `(20.2.15)` applied to each canonical injection `X_s → X` (`s ∈ S`),
taking `(11.10.9)` into account. To see that the condition is sufficient, one must prove that for every `x ∈ X`,
there exists an open neighbourhood `U` of `x` in `X` and a section of `𝓜_{X/S}(ℱ)` over `U` whose restriction to
`U ∩ dom(φ)` coincides with `φ` on a schematically dense open of `U ∩ dom(φ)`. Consider the *Ideal of denominators*
`𝒥` of `φ` `(20.2.14)`, which is quasi-coherent, and which defines a closed sub-prescheme of `X` whose underlying
space is `X − dom(φ)`. By hypothesis, if `s` is the image of `x` in `S`, `dom(φ) ∩ X_s` is schematically dense in
the locally Noetherian prescheme `X_s`, hence `(20.2.13, (iv))` contains `Ass(𝒪_{X_s})`; this implies that the ideal
`𝒥_x` of `𝒪_{X,x}` has an image in `𝒪_{X_s, x} = 𝒪_{X,x} / 𝔪_s 𝒪_{X,x}` which is not contained in any of the prime
ideals `𝔭_i ∈ Ass(𝒪_{X_s, x})` (finite in number); hence (Bourbaki, _Alg. comm._, chap. II, §1, n° 1, prop. 2) there
exists an element `t_x ∈ 𝒥_x` whose image in `𝒪_{X_s, x}` does not belong to any of the `𝔭_i`, and is consequently
regular in this Noetherian ring. Let `t` be a section of `𝒥` over an affine open neighbourhood `U` of `x` whose germ
at the point `x` is `t_x`; since `X` is flat and locally of finite presentation over `S`, one may suppose `(11.3.8)`
that `t` is a regular section of `𝒪_X` over `U` and that, for every `s' ∈ S`, the image of `t` in `Γ(U ∩ X_{s'},
𝒪_{X_{s'}})` is also regular; in other words, one has `t ∈ 𝒮_{X/S}(U)`. But then, by definition of `𝒥`, since `ℱ` is
strictly torsion-free, `t(φ | (U ∩ dom(φ)))` is a section `u` of `ℱ` over `U ∩ dom(φ)`; on the other hand,
`U ∩ dom(φ)` contains the open set `U_t` of points `x' ∈ U` where `t(x') ≠ 0`, and this latter contains `x` and is
schematically dense in `U` `(20.2.9)`. One therefore sees that on `U_t`, `φ` coincides with the restriction to `U_t`
of the section `u/t` of `𝓜_{X/S}(ℱ)` over `U`. Q.E.D.

**Remarks (20.6.5).**

<!-- label: IV.20.6.5 -->

(i) Let `φ` be a meromorphic function on `X` relative to `S`, so that for every `s ∈ S`, `φ_s` is a meromorphic
function on `X_s` `(20.6.1)`; by virtue of `(20.1.11.1)`, one has

```text
  (20.6.5.1)             dom(φ) ∩ X_s ⊂ dom(φ_s).
```

But it is worth noting that even when `S` is the spectrum of a discrete valuation ring `A` and `X = S[T]` (`T`
indeterminate), the two sides of `(20.6.5.1)` are not necessarily equal: for example, if `π` is a uniformizer of `A`,
it is immediate that `φ = π/T` is a meromorphic function on `S` relative to `S`, since if `a` and `b` are the closed
point and the generic point of `S`, `T` is regular in `Γ(X_a, 𝒪_{X_a}) = k[T]` and in
`Γ(X_b, 𝒪_{X_b}) = K[T]`, `k` and `K` being the residue field and the field of fractions of `A`. One has
`dom(φ) = D(T)` in `X`, but `dom(φ_a) = X_a` since `φ_a = 0`.

(ii) For a meromorphic function `φ` relative to `S` to be invertible in the ring `M(X/S)`, it is necessary and
sufficient that for every `s ∈ S`, `φ_s` be invertible in `M(X_s)` (in other words, that `φ_s` be a regular
meromorphic function on `X_s` `(20.1.8)`). The condition is

<!-- original page 254 -->

indeed trivially necessary. Conversely, if it is verified, and if `x` is any point of `X`, `s` its image in `S`,
there exists by hypothesis an open neighbourhood `U` of `x` in `X` and two sections `u`, `t` of `𝒪_X` over `U` such
that `t ∈ 𝒮_{X/S}(U)` and `φ | U = u/t`; the hypothesis entails that if `u_s` is the image of `u` in
`Γ(U ∩ X_s, 𝒪_{X_s})`, `u_s` is regular at the point `x`. By restricting `U`, one may therefore suppose, by virtue of
`(11.3.8)`, that `u ∈ 𝒮_{X/S}(U)`, whence the conclusion.

When `φ` is invertible in `M(X/S)`, one again says that `φ` is a *regular meromorphic function relative to `S`*. One
will note that `φ ∈ M(X/S)` may be invertible in `M(X)` (in other words, regular in the sense of `(20.1.8)`) without
being so in `M(X/S)`, as the example in (i) at once shows.

(iii) Let `ℒ` be an invertible `𝒪_X`-Module, and let `φ` be a regular meromorphic section of `ℒ` over `X` `(20.1.8)`;
one says that `φ` is *regular relative to `S`* if, for every open `U` of `X` such that `ℒ | U` is isomorphic to
`𝒪_U`, `φ | U` corresponds to an element of `Γ(U, 𝓜_X)` which is regular relative to `S`; by virtue of (ii), it is
immediate that it is necessary and sufficient for this that, for every `s ∈ S`, `φ_s` be a regular meromorphic section
`(20.1.8)` of the invertible `𝒪_{X_s}`-Module `ℒ_s = ℒ ⊗_{𝒪_X} k(s)`. If `φ'` is the inverse of `φ` in `ℒ⁻¹`
`(20.1.10)`, `φ'` is then also regular relative to `S`. If `ℒ_1` is a second invertible `𝒪_X`-Module, `φ_1` a
meromorphic section of `ℒ_1` over `X`, regular relative to `S`, then `φ ⊗ φ_1` is a meromorphic section of
`ℒ ⊗ ℒ_1` over `X`, regular relative to `S`.

**Proposition (20.6.6).**

<!-- label: IV.20.6.6 -->

*Let `X` be an `S`-prescheme flat and locally of finite presentation over `S`, `ℱ` an `𝒪_X`-Module locally free of
finite type; for every `s ∈ S`, denote by `X_s` the fibre at the point `s` of the structure morphism `f : X → S`. Let
`φ` be a meromorphic section of `ℱ` over `X`, relative to `S`, and suppose that `φ` is defined at every point `x ∈ X`
such that `prof(𝒪_{X_{f(x)}, x}) ≤ 1`. Then `φ` is everywhere defined.*

By hypothesis, `dom(φ) ∩ X_s` is schematically dense in `X_s` for every `s ∈ S`, hence contains the points `x` of
`X_s` such that `prof(𝒪_{X_s, x}) = 0` `(5.10.2)`; the hypothesis means therefore that if one sets `Z = X − dom(φ)`,
one has `prof(𝒪_{X_{f(x)}, x}) ≥ 2` at every point of `Z`. It therefore suffices to apply `(19.9.8)`.

**(20.6.7).** Let `X`, `X'` be two `S`-preschemes flat and locally of finite presentation over `S`,
`f = (ψ, θ) : X' → X` an `S`-morphism. For every open `U` of `X`, denote by `𝒮_{f, /S}(U)` the set of sections
`t ∈ 𝒮_{X/S}(U)` whose image in `Γ(f⁻¹(U), 𝒪_{X'})` belongs to `𝒮_{X'/S}(f⁻¹(U))`; it is immediate that
`U ↦ 𝒮_{f, /S}(U)` is a subsheaf of the sheaf of sets `𝒮_{X/S}`, which one denotes `𝒮_{f, /S}`. One sets
`𝓜_{X/S, f} = 𝒪_X[𝒮_{f, /S}⁻¹]`; this is a subsheaf of rings of `𝓜_{X/S}`, and one canonically deduces from
`θ♯ : ψ*(𝒪_X) → 𝒪_{X'}` a homomorphism of sheaves of rings `θ'♯ : ψ*(𝓜_{X/S, f}) → 𝓜_{X'/S}` extending `θ♯`. If a
meromorphic function `φ` on `X`, relative to `S`, is a section of `𝓜_{X/S, f}`, `Γ(θ'♯)(φ)` is a meromorphic function
on `X'`, called the *inverse image of `φ` under `f`*, and denoted `φ ∘ f` if this entails no confusion. One extends in
the same way the definitions of `(20.1.11)` relative to `𝒪_X`-Modules.

**Proposition (20.6.8).**

<!-- label: IV.20.6.8 -->

*With the notations of `(20.6.7)`, if the `S`-morphism `f : X' → X` is flat, one has `𝓜_{X/S, f} = 𝓜_{X/S}`, and the
homomorphism `φ ↦ φ ∘ f` is defined on all of `M(X/S)`.*

<!-- original page 255 -->

Indeed, the hypothesis entails, by virtue of `(11.3.10)`, that for every `s ∈ S`, `f_s : X'_s → X_s` is flat; so, for
every section `t ∈ 𝒮_{X/S}(U)`, if `t'` is its inverse image in `Γ(f⁻¹(U), 𝒪_{X'})`, `t'_s`, which is the inverse
image of `t_s`, is a regular section of `𝒪_{X'_s}` over `f⁻¹(U) ∩ X'_s`, by virtue of `(20.1.12)`; one concludes
that by definition `t' ∈ 𝒮_{X'/S}(f⁻¹(U))`, whence the proposition.

One deduces from this, as in `(20.1.12)`, a canonical homomorphism of `𝒪_{X'}`-Algebras

```text
  (20.6.8.1)             f*(𝓜_{X/S}) → 𝓜_{X'/S}.
```

**(20.6.9).** Consider finally an arbitrary morphism `S' → S`, and set `X' = X ×_S S'`, which is flat and locally of
finite presentation over `S'`; let `p : X' → X` be the canonical projection. Let `U` be an open of `X`, `t` a section
belonging to `𝒮_{X/S}(U)`, `t'` its image in `Γ(p⁻¹(U), 𝒪_{X'})`; for every `s' ∈ S'`, if `s ∈ S` is the image of
`s'`, one has `X'_{s'} = X_s ⊗_{k(s)} k(s')`, hence the morphism `X'_{s'} → X_s` is flat, and consequently
`(20.1.12)` the inverse image `t'_{s'}` of `t_s` in `Γ(p⁻¹(U) ∩ X'_{s'}, 𝒪_{X'_{s'}})` is regular; this proves that
one has `t' ∈ 𝒮_{X'/S'}(p⁻¹(U))`. This permits one to define canonically, as in `(20.6.8)`, a canonical homomorphism
of `𝒪_{X'}`-Algebras

```text
  (20.6.9.1)             p*(𝓜_{X/S}) → 𝓜_{X'/S'}.
```

By means of the identification permitted by `(20.6.3)`, this notion of base change for relative meromorphic functions
is a particular case of the analogous notion for relative pseudo-morphisms `(20.5.8)`.

