# Chapter I — The Language of Schemes

## §4. Subpreschemes and Immersion Morphisms

<!-- label: I.4 -->

> **Translation status.** Translation skeleton with key definitions and theorem statements; full proofs reference
> `~/Code/ega/ega1/ega1-4.tex`.

### 4.1. Subpreschemes

<!-- label: I.4.1 -->

**Proposition (4.1.2).** Let `(X, 𝒪_X)` be a prescheme and `𝒥 ⊂ 𝒪_X` a quasi-coherent sheaf of ideals. The support of
`𝒪_X / 𝒥` is _closed_ in `X`; on this support, the pair `(Supp(𝒪_X/𝒥), (𝒪_X/𝒥)|Supp)` is a prescheme.

**Definition (4.1.3).** A _closed subprescheme_ of `(X, 𝒪_X)` is a prescheme of the form `(Y, 𝒪_X / 𝒥 | Y)` with
`𝒥 ⊂ 𝒪_X` a quasi-coherent ideal sheaf and `Y = Supp(𝒪_X/𝒥)`. An _open subprescheme_ is the prescheme `(U, 𝒪_X | U)`
induced on an open `U ⊂ X`. A _subprescheme_ is the closed subprescheme of an open subprescheme.

**Proposition (4.1.5).** A closed subprescheme is uniquely determined by its sheaf of ideals.

**Proposition (4.1.6).** For an affine scheme `X = Spec(A)`: closed subpreschemes correspond bijectively to ideals
`𝔍 ⊂ A`, the closed subprescheme being `Spec(A/𝔍)`.

**Proposition (4.1.9).** Closed subpreschemes of a Noetherian prescheme satisfy the descending chain condition.

**Corollary (4.1.10).** Every prescheme is a union of its open affine subpreschemes (a closed cover of finite type, if
Noetherian).

### 4.2. Immersion morphisms

<!-- label: I.4.2 -->

**Definition (4.2.1).** A morphism `j : Y → X` of preschemes is an _open immersion_ (resp. _closed immersion_, resp.
_immersion_) if `j` is a homeomorphism of `Y` onto an open (resp. closed, resp. locally closed) subspace of `X` and
`j^♯ : 𝒪_X → j_*(𝒪_Y)` is surjective onto the structure sheaf of the corresponding subprescheme. Equivalently, `j`
factors as `Y ⥲ Y′ ↪ X` with `Y′` an open (resp. closed, resp. locally closed) subprescheme.

**Proposition (4.2.2).** Composition of immersions is an immersion; the composite of two open (resp. closed) immersions
is open (resp. closed).

**Corollary (4.2.3).** Immersions are monomorphisms of preschemes.

**Corollary (4.2.4).** An immersion is radicial.

**Proposition (4.2.5).** Immersions are preserved under base change.

### 4.3. Products of immersions

<!-- label: I.4.3 -->

**Proposition (4.3.1).** If `j_1 : Y_1 → X_1` and `j_2 : Y_2 → X_2` are immersions of `S`-preschemes, then
`j_1 ×_S j_2 : Y_1 ×_S Y_2 → X_1 ×_S X_2` is an immersion (open or closed if both factors are).

**Corollary (4.3.2).** Open immersions and closed immersions are stable under fiber products.

### 4.4. Inverse images of subpreschemes

<!-- label: I.4.4 -->

**Proposition (4.4.1).** For a morphism `f : X → Y` and a closed subprescheme `Y′ ⊂ Y` with ideal sheaf `𝒥`, the inverse
image `f⁻¹(Y′) = X ×_Y Y′` is a closed subprescheme of `X` with ideal sheaf `f*(𝒥) · 𝒪_X = 𝒥 𝒪_X`.

**Corollary (4.4.2).** Inverse images preserve closed (resp. open) subpreschemes.

**Corollary (4.4.3).** For composable morphisms, `(g ∘ f)⁻¹(Z) = f⁻¹(g⁻¹(Z))`.

**Corollary (4.4.4).** Inverse images preserve immersions.

**Proposition (4.4.5).** For morphisms `X → Y → S` and a subprescheme `Y′ ⊂ Y`, `X ×_Y Y′ = X ×_S Y′` (when `Y′ ↪ Y` is
an immersion).

### 4.5. Local immersions and local isomorphisms

<!-- label: I.4.5 -->

**Definition (4.5.1).** A morphism `f : X → Y` is a _local immersion at_ `x ∈ X` if there is an open `U ∋ x` such that
`f | U : U → Y` is an immersion. `f` is a _local immersion_ if it is so at every point.

**Definition (4.5.2).** A morphism `f : X → Y` is a _local isomorphism at_ `x` if there is an open `U ∋ x` and an open
`V ⊃ f(U)` such that `f | U → V` is an isomorphism. `f` is a _local isomorphism_ if it is so at every point.

**Proposition (4.5.4).** A local immersion is radicial (and so injective on geometric points stalkwise).

**Proposition (4.5.5).** A local isomorphism is open. A radicial local isomorphism is a local immersion.

<!-- source: ~/Code/papers/books/ega/i/01-04-sous-preschemas-et-immersions.md and ~/Code/ega/ega1/ega1-4.tex -->
