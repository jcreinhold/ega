<!-- original page 116 -->

## §11. Topological properties of flat morphisms of finite presentation; local criteria of flatness

While in §2 we considered the statements concerning flatness which do not depend on any finiteness hypothesis, and while
§6 studies the notion of flatness in the framework of locally Noetherian preschemes (but without finiteness hypothesis
on the morphisms), the present section is devoted to the notion of $f$-flatness in the case where the morphism $f : X
\to Y$ is locally of finite presentation. The interest of the notion of flat morphism of finite presentation lies in the
fact that it is the one which seems to express, in the most technically adequate manner, the intuitive notion of "family
of algebraic preschemes parameterized by a scheme $Y$", whose study is one of the principal objects of Algebraic
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
base-change morphism $Y' \to Y$ (not flat in general) so as to be able to conclude that if $X \times_{Y} Y'$ is flat
over $Y'$, then $X$ is flat over $Y$. These results, more technical than those of nos. 1 to 3, are of less frequent use
in the sequel; they will however play an important role in the non-projective construction techniques in the following
chapter. The only result of nos. 4 to 8 used in the sequel of Chap. IV is the valuative criterion of flatness (n° 8),
which will be applied in `(15.2)`.

Finally, nos. 9 and 10 are devoted to the study of a notion which makes precise, in the theory of schemes, that of
density in the topological sense, namely the notion of family of sub-preschemes *schematically dense* in a given
prescheme, and notably the study of the behaviour of this notion under base change (flat or arbitrary). This notion is
used above all, for the moment, in the study of group schemes.

### 11.1. Flatness loci (Noetherian case)

**Theorem (11.1.1).**

<!-- label: IV.11.1.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module. Then the set $U$ of $x \in X$ such that $\mathcal{F}$ is $f$-flat at the point $x$ is open in
$X$.*

The question being evidently local on $X$ and $Y$, one may suppose $Y = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$, with $A$ Noetherian and $B$ an $A$-algebra of finite type. One then has $\mathcal{F} =
\tilde{M}$, where $M$ is a $B$-module of finite type. Let us apply the criterion $(0_{III}, 9.2.6)$: it therefore
suffices to prove the following assertion:

```text
  (11.1.1.1) Let A be a Noetherian ring, B an A-algebra of finite type, M a B-module of finite type, 𝔮 a prime
             ideal of B, 𝔭 its inverse image in A. Suppose that M_𝔮 is a flat A_𝔭-module. Then there exists
             g ∈ B − 𝔮 such that for every prime ideal 𝔮' ⊃ 𝔮 of B with g ∉ 𝔮', M_{𝔮'} is a flat A_{𝔭'}-module,
             where 𝔭' denotes the inverse image of 𝔮' in A (it amounts to the same thing (0_I, 6.3.1) to say
             that M_{𝔮'} is a flat A-module).
```

To this end, let us consider $B_{\mathfrak{q}'}$ as an $A$-algebra; one evidently has $\mathfrak{p} B_{\mathfrak{q}'}
\subset \mathfrak{q}' B_{\mathfrak{q}'}$. One then knows $(0_{III}, 10.2.2)$ that for $M_{\mathfrak{q}'}$ to be a flat
$A$-module, it is necessary and sufficient that $M_{\mathfrak{q}'}/\mathfrak{p} M_{\mathfrak{q}'}$ be a flat
$(A/\mathfrak{p})$-module and that one have $Tor^{A}_{1}(M_{\mathfrak{q}'}, A/\mathfrak{p}) = 0$. Now, one has
$M_{\mathfrak{q}'} = M \otimes_{B} B_{\mathfrak{q}'}$; since $B_{\mathfrak{q}'}$ is flat over $B$, one has
$M_{\mathfrak{q}'}/\mathfrak{p} M_{\mathfrak{q}'} = (M/\mathfrak{p} M)_{\mathfrak{q}'}$ and
$Tor^{A}_{1}(M_{\mathfrak{q}'}, A/\mathfrak{p}) = (Tor^{A}_{1}(M, A/\mathfrak{p}))_{\mathfrak{q}'}$ (defining `Tor` by
means of a projective resolution of $A/\mathfrak{p}$); for the same reason, since one must have $g \notin
\mathfrak{q}'$, $B_{\mathfrak{q}'}$ is flat over $B_{g}$, hence $(M/\mathfrak{p} M)_{\mathfrak{q}'} = ((M/\mathfrak{p}
M)_{g})_{\mathfrak{q}' B_{g}}$ and $(Tor^{A}_{1}(M, A/\mathfrak{p}))_{\mathfrak{q}'} = ((Tor^{A}_{1}(M,
A/\mathfrak{p}))_{g})_{\mathfrak{q}' B_{g}}$, where in these formulas $M/\mathfrak{p} M$ and $Tor^{A}_{1}(M,
A/\mathfrak{p})$ are considered as $B$-modules. Taking $(0_{I}, 6.3.2)$ into account, one sees that one is reduced to
proving the

**Lemma (11.1.1.2).**

<!-- label: IV.11.1.1.2 -->

*Under the conditions of `(11.1.1.1)`, there exists $g \in B - \mathfrak{q}$ such that:* *(i) $(M/\mathfrak{p} M)_{g}$
is a flat $(A/\mathfrak{p})$-module;* *(ii) $(Tor^{A}_{1}(M, A/\mathfrak{p}))_{g} = 0$.*

<!-- original page 118 -->

By virtue of the generic flatness theorem `(6.9.1)` applied to the integral ring $A/\mathfrak{p}$, to the
$(A/\mathfrak{p})$-algebra of finite type $B/\mathfrak{p} B$, and to the $(B/\mathfrak{p} B)$-module of finite type
$M/\mathfrak{p} M$, there exists $h \in A - \mathfrak{p}$ such that, if $\bar{h}$ is its canonical image in
$A/\mathfrak{p}$, $(M/\mathfrak{p} M)_{\bar{h}}$ is a flat $(A/\mathfrak{p})$-module. On the other hand, since
$M_{\mathfrak{q}}$ is a flat $A_{\mathfrak{p}}$-module, and consequently a flat $A$-module $(0_{I}, 6.3.1)$, one has
$Tor^{A}_{1}(M_{\mathfrak{q}}, A/\mathfrak{p}) = 0$, which one also writes $(Tor^{A}_{1}(M,
A/\mathfrak{p}))_{\mathfrak{q}} = 0$. But since $A$ and $B$ are Noetherian, $Tor^{A}_{1}(M, A/\mathfrak{p})$ is a
$B$-module of finite type, hence $(0_{I}, 5.2.2)$ there exists $g_{1} \in B - \mathfrak{q}$ such that $(Tor^{A}_{1}(M,
A/\mathfrak{p}))_{g_{1}} = 0$. Moreover, one has $(M/\mathfrak{p} M)_{\bar{h}} = (M/\mathfrak{p} M)_{h}$
($M/\mathfrak{p} M$ being considered in the second member as an $A$-module); in addition, $(M/\mathfrak{p} M)_{h}$ being
a $B$-module, $(M/\mathfrak{p} M)_{hg_{1}}$ is again a flat $(A/\mathfrak{p})$-module, for it can be written
$(M/\mathfrak{p} M)_{\bar{h} \bar{g}_{1}}$, where $\bar{h} \bar{g}_{1}$ is the canonical image of $h g_{1}$ in
$B/\mathfrak{p} B$, and it suffices to apply $(0_{I}, 6.3.2)$; finally, one has $(Tor^{A}_{1}(M, A/\mathfrak{p}))_{h
g_{1}} = 0$ and $h g_{1} \in B - \mathfrak{q}$ since $h \in A - \mathfrak{p}$. Q.E.D.

**Corollary (11.1.2).**

<!-- label: IV.11.1.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$,
$\mathcal{F}'$ two coherent $\mathcal{O}_{X}$-Modules, $u : \mathcal{F}' \to \mathcal{F}$ a homomorphism of
$\mathcal{O}_{X}$-Modules. Suppose that $\mathcal{F}$ is $f$-flat. Then the set $U$ of $x \in X$ such that, setting $y =
f(x)$, the homomorphism $u_{x} \otimes 1 : \mathcal{F}'_{x} \otimes_{\mathcal{O}_{y}} k(y) \to \mathcal{F}_{x}
\otimes_{\mathcal{O}_{y}} k(y)$ is injective, is open in $X$.*

Indeed, let $\mathcal{N}$ (resp. $\mathcal{Q}$) be the kernel (resp. the cokernel) of $u$; let us apply $(0_{III},
10.2.4)$ <sup>(\*)</sup> to the local rings $\mathcal{O}_{y}$ and $\mathcal{O}_{x}$ and to the $\mathcal{O}_{y}$-modules
$\mathcal{F}'_{x}$ and $\mathcal{F}_{x}$: to say that $u_{x} \otimes 1$ is injective amounts to saying that
$\mathcal{N}_{x} = 0$ and that $\mathcal{Q}$ is $f$-flat at the point $x$. Now since $\mathcal{N}$ and $\mathcal{Q}$ are
coherent $(0_{I}, 5.3.4)$, the set of $x$ where $\mathcal{N}_{x} = 0$ is open $(0_{I}, 5.2.2)$, and the set of $x$ where
$\mathcal{Q}$ is $f$-flat is open by `(11.1.1)`; whence the conclusion.

In particular:

**Corollary (11.1.3).**

<!-- label: IV.11.1.3 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a flat morphism locally of finite type, $g$ a section of
$\mathcal{O}_{X}$ over $X$. The set of $x \in X$ such that $g_{x} \otimes 1$ is not a zero-divisor in $\mathcal{O}_{x}
\otimes_{\mathcal{O}_{f(x)}} k(f(x))$ is open in $X$.*

It suffices to apply `(11.1.2)` to the endomorphism of $\mathcal{O}_{X}$ defined by $g$.

**Corollary (11.1.4).**

<!-- label: IV.11.1.4 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module which is $f$-flat. Let $(g_{i})_{1 \leq i \leq n}$ be a sequence of sections of
$\mathcal{O}_{X}$ over $X$. Then the set $U$ of $x \in X$ such that the sequence $((g_{i})_{x} \otimes 1)$ is
$(\mathcal{F}_{f(x)} \otimes_{\mathcal{O}_{f(x)}} k(f(x)))$-regular is open in $X$.*

Since $\mathcal{F}$ is $f$-flat, it follows from $(0_{IV}, 15.1.16)$ that $U$ is also the set of points

<sup>(\*)</sup> Here is a proof of $(0_{III}, 10.2.4)$ which was not published in N. Bourbaki's *Algèbre commutative*.
Taking $(0_{I}, 6.1.2)$ into account, it suffices to see that b) implies a). Set $P = Im(u)$, $Q = Coker(u)$, $R =
Ker(u)$. The composite $M \otimes k \to P \otimes k \to N \otimes k$ is injective, and $M \otimes k \to P \otimes k$ is
surjective, hence $P \otimes k \to N \otimes k$ is injective and $M \otimes k \to P \otimes k$ is bijective. The exact
sequence $0 \to P \to N \to Q \to 0$ gives the exact sequence $0 \to P \otimes k \to N \otimes k \to Q \otimes k \to 0$
(since $P \otimes k \to N \otimes k$ is injective), and one has $Tor^{A}_{1}(Q, k) = 0$; since $Q$ is a $B$-module of
finite type, $(0_{III}, 10.2.2)$ shows that $Q$ is a flat $A$-module; then $P$ is also a flat $A$-module by $(0_{I},
6.1.2)$. The sequence $0 \to R \to M \to P \to 0$ being exact, so is $0 \to R \otimes k \to M \otimes k \to P \otimes k
\to 0$ by $(0_{I}, 6.1.2)$; since $M \otimes k \to P \otimes k$ is bijective, one has $R \otimes k = 0$; but since $B$
is Noetherian, $R$ is a $B$-module of finite type, hence one has $R = 0$ by virtue of Nakayama's lemma.

<!-- original page 119 -->

$x \in X$ such that the sequence $(g_{i})_{x}$ is $\mathcal{F}_{x}$-regular and the $\mathcal{O}_{x}$-module
$\mathcal{F}_{x}/(\sum^{n}_{i=1} (g_{i})_{x} \mathcal{F}_{x})$ is $f$-flat. But $\mathcal{F}$ and $\mathcal{F}/(\sum
g_{i} \mathcal{F})$ are coherent, hence the corollary follows from `(11.1.1)` and $(0_{IV}, 15.2.4)$.

**Corollary (11.1.5).**

<!-- label: IV.11.1.5 -->

*Let $X$, $Y$, $Z$ be three locally Noetherian preschemes, $f : X \to Y$, $g : Y \to Z$ two morphisms of finite type,
$\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Then the set $U$ of $y \in Y$ such that, for every generization $y'$
of $y$, $\mathcal{F}$ is $(g \circ f)$-flat at all points of $f^{-1}(y')$ (i.e. such that $\mathcal{F} \otimes_{Y}
\operatorname{Spec}(\mathcal{O}_{Y, y'})$ is flat relative to the morphism $X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{Y, y'}) \to Z$) is open in $Y$.*

If $V$ is the set of $x \in X$ where $\mathcal{F}$ is $(g \circ f)$-flat, $U$ is the set of $y \in Y$ such that for
every generization $y'$ of $y$, one has $f^{-1}(y') \subset V$. Now $V$ is open `(11.1.1)`, hence locally constructible
in $X$, and the set $W$ of $y \in Y$ such that $f^{-1}(y) \subset V$ is equal to $Y - f(X - V)$, hence is also locally
constructible in $Y$ by virtue of Chevalley's theorem `(1.8.4)`. It then follows from $(0_{III}, 9.2.5)$ that the points
of $U$ are the points interior to $W$, whence the conclusion.

**Corollary (11.1.6).**

<!-- label: IV.11.1.6 -->

*Let $A$ be a Noetherian ring, $B$ an $A$-algebra of finite type, $C$ a $B$-algebra of finite type, $M$ a $C$-module of
finite type. Then the set of $\mathfrak{q} \in \operatorname{Spec}(B)$ such that $M_{\mathfrak{q}}$ is a flat $A$-module
is open in $\operatorname{Spec}(B)$.*

Taking `(2.1.2)` into account, this is a consequence of `(11.1.5)` applied to $Z = \operatorname{Spec}(A)$, $Y =
\operatorname{Spec}(B)$, $X = \operatorname{Spec}(C)$, $\mathcal{F} = \tilde{M}$.

The results of this number will be freed of the Noetherian hypotheses in `(11.3)`.

### 11.2. Flatness of a projective limit of preschemes

(11.2.1) Let $A$ be a ring, $M$, $N$ two $A$-modules, $A'$ an $A$-algebra; set $M' = M \otimes_{A} A'$, $N' = N
\otimes_{A} A'$. Recall `(III, 6.3.8)` that for every $i$ one defines a canonical homomorphism of $A$-modules

```text
  (11.2.1.1)    φ_i : Tor_i^A(M, N) → Tor_i^{A'}(M', N')
```

in the following manner: one considers a left resolution of $M$ by free $A$-modules

```text
  (11.2.1.2)    … → L_{i+1} →^{f_{i+1}} L_i → … → L_0 →^ε M → 0
```

whence one deduces by tensoring with $A'$ a complex of $A'$-modules

```text
  (11.2.1.3)    … → L'_{i+1} →^{f'_{i+1}} L'_i → … → L'_0 →^{ε'} M' → 0
```

where one has set $L'_{i} = L_{i} \otimes_{A} A'$, $f'_{i} = f_{i} \otimes 1_{A'}$, $\epsilon' = \epsilon \otimes
1_{A'}$. Let us consider on the other hand a left resolution of $M'$ by free $A'$-modules

```text
  (11.2.1.4)    … → L''_{i+1} →^{f''_{i+1}} L''_i → … → L''_0 →^{ε''} M' → 0
```

<!-- original page 120 -->

Since the $L''_{i}$ are free $A'$-modules, one knows `(M, V, 1.1)` that there are $A'$-homomorphisms $u_{i}$ forming a
commutative diagram

```text
  L'_i  ─f'_i─→  L'_{i-1}  ─→  ⋯  ─→  L'_0  ─ε'─→  M'
   │              │                    │            ‖
   u_i           u_{i-1}                u_0          1_{M'}
   ↓              ↓                    ↓            ↓
  L''_i ─f''_i─→ L''_{i-1} ─→  ⋯  ─→  L''_0 ─ε''─→  M'
```

If one composes the homomorphism $u_{\bullet} : L'_{\bullet} \to L''_{\bullet}$ of complexes thus defined with the
canonical homomorphism $L_{\bullet} \to L'_{\bullet}$, one obtains a homomorphism of complexes of $A$-modules
$L_{\bullet} \to L''_{\bullet}$; noting that one has $(L_{i} \otimes_{A} N) \otimes_{A} A' = L'_{i} \otimes_{A'} N'$,
one deduces from this a homomorphism of complexes of $A$-modules $L_{\bullet} \otimes_{A} N \to L''_{\bullet}
\otimes_{A'} N'$, whence, on passing to homology, the canonical homomorphisms `(11.2.1.1)`. Since the $u_{i}$ are well
determined up to homotopy `(M, V, 1.1)`, the homomorphisms `(11.2.1.1)` do not depend on the choice of the $u_{i}$ nor
on the choice of the free resolutions $L_{\bullet}$ and $L''_{\bullet}$.

Since the $Tor^{A'}_{i}(M', N')$ are $A'$-modules, one canonically deduces from `(11.2.1.1)` $A'$-homomorphisms

```text
  (11.2.1.5)    ψ_i : Tor_i^A(M, N) ⊗_A A' → Tor_i^{A'}(M', N').
```

Let us now consider two ring homomorphisms $\alpha : A \to A^{(1)}$, $\beta : A^{(1)} \to A^{(2)}$ and their composite
$\beta \circ \alpha : A \to A^{(2)}$; set $M^{(j)} = M \otimes_{A} A^{(j)}$, $N^{(j)} = N \otimes_{A} A^{(j)}$ for $j =
1, 2$. Then the canonical composite homomorphism

```text
  Tor_i^A(M, N) → Tor_i^{A^{(1)}}(M^{(1)}, N^{(1)}) → Tor_i^{A^{(2)}}(M^{(2)}, N^{(2)})
```

is the same as the canonical homomorphism deduced from $\beta \circ \alpha$; this results from the fact that, if
$L^{(j)}_{\bullet}$ is a free resolution of $M^{(j)}$, the diagram

```text
  L_•^{(1)}  ─→  L_•^{(2)}
     ↑              ↑
     L_•   ──────────
```

is commutative.

(11.2.2) The notation being that of `(11.2.1)`, let us now consider a filtered inductive system of $A$-algebras
$(A_{\alpha}, \xi_{\beta \alpha})$, and for every index $\alpha$, set $M_{\alpha} = M \otimes_{A} A_{\alpha}$,
$N_{\alpha} = N \otimes_{A} A_{\alpha}$; it then follows from `(11.2.1)` that for each $i$,
$(Tor^{A_{\alpha}}_{i}(M_{\alpha}, N_{\alpha}), \psi_{\beta \alpha})$, where $\psi_{\beta \alpha}$ is the canonical
homomorphism `(11.2.1.1)` corresponding to $\xi_{\beta \alpha}$, is an inductive system

<!-- original page 121 -->

of $A_{\alpha}$-modules. Set $A' = \lim A_{\alpha}$, $M' = \lim M_{\alpha} = M \otimes_{A} A'$, $N' = \lim N_{\alpha} =
N \otimes_{A} A'$; if one denotes by $\xi_{\alpha} : A_{\alpha} \to A'$ the canonical homomorphism, one deduces from
this canonical homomorphisms `(11.2.1.1)` $\psi_{\alpha} : Tor^{A_{\alpha}}_{i}(M_{\alpha}, N_{\alpha}) \to
Tor^{A'}_{i}(M', N')$ which (still by virtue of `(11.2.1)`) form an inductive system of homomorphisms; we propose to
complete the result of `(M, V, 9.4*)` by showing that the

```text
  (11.2.2.1)    ψ = lim ψ_α : lim_α Tor_i^{A_α}(M_α, N_α) → Tor_i^{A'}(M', N')
```

*are isomorphisms of $A'$-modules.* For this, we proceed as in `(M, V, 9.5*)`, associating to each $M_{\alpha}$ its
canonical free resolution. Everything boils down (taking into account the exactness of the functor `lim`) to proving the

**Lemma (11.2.2.2).**

<!-- label: IV.11.2.2.2 -->

*Let $(A_{\alpha}, \xi_{\beta \alpha})$ be a filtered inductive system of rings, $(M_{\alpha}, h_{\beta \alpha})$ an
inductive system of sets, $A' = \lim A_{\alpha}$, $M' = \lim M_{\alpha}$, $\xi_{\alpha} : A_{\alpha} \to A'$,
$h_{\alpha} : M_{\alpha} \to M'$ the canonical maps. For every $\alpha$, let $F(M_{\alpha})$ be the $A_{\alpha}$-module
of formal linear combinations of elements of $M_{\alpha}$; let similarly $F(M')$ be the $A'$-module of formal linear
combinations of elements of $M'$; if $h'_{\beta \alpha} : F(M_{\alpha}) \to F(M_{\beta})$ (for $\alpha \leq \beta$) and
$h'_{\alpha} : F(M_{\alpha}) \to F(M')$ are the $A_{\alpha}$-homomorphisms deduced from $h_{\beta \alpha}$ and
$h_{\alpha}$ respectively, $(F(M_{\alpha}), h'_{\beta \alpha})$ is an inductive system of $A_{\alpha}$-modules and
$(h'_{\alpha})$ an inductive system of homomorphisms. Then*

```text
  h' = lim h'_α : lim F(M_α) → F(M') = F(lim M_α)
```

*is an isomorphism.*

For the proof, see *Bourbaki, Alg., chap. II, 3rd ed., §6, n° 6, cor. of prop. 10*.

(11.2.3) Let us resume the notation of `(11.2.1)` and consider particularly the case $i = 1$; set $T = Tor^{A}_{1}(M,
N)$, $T' = T \otimes_{A} A'$, $T'' = Tor^{A'}_{1}(M', N')$; then $\psi_{1}$ is the homomorphism $Ker(f_{0} \otimes
1_{N})/Im(f_{1} \otimes 1_{N}) \to Ker(f''_{0} \otimes 1_{N'})/Im(f''_{1} \otimes 1_{N'})$ which is deduced by passage
to quotients from the restriction $Ker(f_{0} \otimes 1_{N}) \to Ker(f''_{0} \otimes 1_{N'})$ of

```text
  L_1 ⊗_A N → L''_1 ⊗_{A'} N'.
```

Set $R = Ker(\epsilon)$, $R'' = Ker(\epsilon'')$, so that one has the exact sequences

```text
  0 → R → L_0 →^ε M → 0    and    0 → R'' → L''_0 →^{ε''} M' → 0,
```

whence one deduces the exact sequences of homology

```text
  (11.2.3.1)    0 = Tor_1^A(L_0, N) → T →^∂ R ⊗_A N → L_0 ⊗_A N → M ⊗_A N → 0
  (11.2.3.2)    0 = Tor_1^{A'}(L''_0, N') → T'' →^{∂''} R'' ⊗_{A'} N' → L''_0 ⊗_{A'} N' → M' ⊗_{A'} N' → 0
```

One has on the other hand a homomorphism of $A'$-modules

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

is commutative. For this, one verifies at once `(M, IV, 1)` that the homomorphism $\partial : T \to R \otimes_{A} N$
comes (in the present case) by passage to the quotient from the homomorphism $w : Ker(f_{0} \otimes 1_{N}) \to R
\otimes_{A} N$, restriction of the homomorphism $g_{0} \otimes 1_{N} : L_{1} \otimes_{A} N \to R \otimes_{A} N$, where
$g_{0} : L_{1} \to R$ is such that $f_{0} = j \circ g_{0}$; similarly for $\partial''$. It therefore suffices to see
that the diagram

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

*Let $A$ be a ring, $C$ an $A$-algebra, $M$ an $A$-module, $N$ a $C$-module, $A'$ an $A$-algebra. Set $C' = C
\otimes_{A} A'$, $M' = M \otimes_{A} A'$, $N' = N \otimes_{A} A' = N \otimes_{C} C'$. Suppose that $M \otimes_{A} N$ is
a flat $C$-module. Then the canonical homomorphism*

```text
  ψ_1 : Tor_1^A(M, N) ⊗_A A' → Tor_1^{A'}(M', N')
```

*(cf. `(11.2.1.5)`) is surjective.*

Let us keep the notation of `(11.2.3)`; right exactness of the tensor product shows that the sequence $L'_{1} \to L'_{0}
\to M' \to 0$ is exact; since $L'_{0}$ and $L'_{1}$ are free $A'$-modules, one may suppose that one has taken $L''_{0} =
L'_{0}$, $L''_{1} = L'_{1}$, with $u_{0}$ and $u_{1}$ being the identity maps and $f''_{0} = f'_{0}$. Since $R =
Im(f_{1})$ and $R'' = Im(f''_{1}) = Im(f'_{1})$, the homomorphism $v$ is surjective, and so therefore is $v \otimes 1$.
The proof will be complete if one proves that the first row of `(11.2.3.3)` is exact, $\epsilon \otimes 1$ being
surjective and $u_{0} \otimes 1$ injective *(Bourbaki, Alg. comm., chap. I, §1, n° 4, cor. 2 of prop. 2)*. Let us use
for this

<!-- original page 123 -->

the hypothesis that $M \otimes_{A} N$ is a flat $C$-module. Setting $Q = Ker(\epsilon \otimes 1) = Im(j \otimes 1)$ in
the exact sequence `(11.2.3.1)`, one has the two exact sequences $0 \to Q \to L_{0} \otimes_{A} N \to M \otimes_{A} N
\to 0$ and $T \to R \otimes_{A} N \to Q \to 0$, where the homomorphisms are $C$-module homomorphisms; using the flatness
hypothesis, one deduces from this $(0_{I}, 6.1.2)$ the exact sequence

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

But by definition, for every $C$-module $P$, one has $P \otimes_{C} C' = P \otimes_{A} A'$, whence the conclusion.

**Lemma (11.2.5).**

<!-- label: IV.11.2.5 -->

*Let $A$ be a ring, $\mathfrak{J}$ an ideal of $A$, $B$ an $A$-algebra, $M$ a $B$-module, $A \to A'$ a ring
homomorphism. Set $\mathfrak{J}' = \mathfrak{J} A'$, $B' = B \otimes_{A} A'$, $M' = M \otimes_{A} A' = M \otimes_{B}
B'$. Let $\mathfrak{p}'$ be a prime ideal of $B'$ containing $\mathfrak{J} B'$. Suppose one of the following hypotheses
is verified:*

*a) $\mathfrak{J}$ is nilpotent.*

*b) $A'$ is Noetherian, $B'$ is an $A'$-algebra of finite type, $M'$ an $B'$-module of finite type.*

*Under these conditions, suppose verified the following two properties:*

*(i) $M \otimes_{A} (A/\mathfrak{J})$ is a flat $(A/\mathfrak{J})$-module.*

*(ii) The canonical composite homomorphism*

```text
  Tor_1^A(M, A/𝔍) → Tor_1^{A'}(M', A'/𝔍') → (Tor_1^{A'}(M', A'/𝔍'))_{𝔭'}
```

*(where $\psi_{1}$ is the homomorphism `(11.2.1.1)` and $\theta$ the canonical homomorphism from a $B'$-module to its
localization at $\mathfrak{p}'$) is zero.*

*Then $M'_{\mathfrak{p}'}$ is a flat $A'$-module.*

Note that in hypothesis b), $M'_{\mathfrak{p}'}$ is a $B'_{\mathfrak{p}'}$-module of finite type, $B'_{\mathfrak{p}'}$ a
Noetherian $A'$-algebra, and $\mathfrak{J}' B'_{\mathfrak{p}'}$ is contained in the radical $\mathfrak{p}'
B'_{\mathfrak{p}'}$ of $B'_{\mathfrak{p}'}$; in hypothesis a), $\mathfrak{J}'$ is nilpotent; one will therefore be able
to apply the flatness criterion $(0_{III}, 10.2.1)$ or $(0_{III}, 10.2.2)$ according as a) or b) is verified. In the
first place, one has $M'_{\mathfrak{p}'} \otimes_{A'} (A'/\mathfrak{J}') = (M' \otimes_{A'}
(A'/\mathfrak{J}'))_{\mathfrak{p}'} = ((M \otimes_{A} (A/\mathfrak{J})) \otimes_{A/\mathfrak{J}}
(A'/\mathfrak{J}'))_{\mathfrak{p}'}$; hypothesis (i) therefore entails that $M'_{\mathfrak{p}'} \otimes_{A'}
(A'/\mathfrak{J}')$ is a flat $(A'/\mathfrak{J}')$-module, taking $(0_{I}, 6.2.1 and 6.3.2)$ into account. It remains
therefore to see that $Tor^{A'}_{1}(M'_{\mathfrak{p}'}, A'/\mathfrak{J}') = 0$; but this $B'_{\mathfrak{p}'}$-module is
equal to $(Tor^{A'}_{1}(M', A'/\mathfrak{J}'))_{\mathfrak{p}'}$ by virtue of the flatness of $B'_{\mathfrak{p}'}$ over
$B'$. But by virtue of hypothesis (ii), the composite homomorphism $\theta \circ \psi_{1} : Tor^{A}_{1}(M,
A/\mathfrak{J}) \otimes_{A} A' \to (Tor^{A'}_{1}(M', A'/\mathfrak{J}'))_{\mathfrak{p}'}$ is zero; moreover, `(11.2.4)`
applied to $C = A/\mathfrak{J}$ and $N = C$ shows (taking hypothesis (i) into account) that $\psi_{1}$ is surjective
(for $A'/\mathfrak{J}' = C \otimes_{A} A'$); hence the homomorphism $\theta$ is zero, and since the image under $\theta$
of $Tor^{A'}_{1}(M', A'/\mathfrak{J}')$ generates the $B'_{\mathfrak{p}'}$-module $(Tor^{A'}_{1}(M',
A'/\mathfrak{J}'))_{\mathfrak{p}'}$, the latter is zero. Q.E.D.

**Theorem (11.2.6).**

<!-- label: IV.11.2.6 -->

*The notation being that of `(8.5.1)` and `(8.8.1)`, suppose $S_{\alpha}$ quasi-compact, $X_{\alpha}$ and $Y_{\alpha}$
of finite presentation over $S_{\alpha}$; let $f_{\alpha} : X_{\alpha} \to Y_{\alpha}$ be an $S_{\alpha}$-morphism,
$\mathcal{F}_{\alpha}$ a quasi-coherent $\mathcal{O}_{X_{\alpha}}$-Module of finite presentation.*

*(i) Let $x$ be a point of $X$, $x_{\lambda}$ its canonical projection in $X_{\lambda}$. For $\mathcal{F}$ to be
$f$-flat at the point $x$, it is necessary and sufficient that there exist $\lambda \geq \alpha$ such that
$\mathcal{F}_{\lambda}$ is $f_{\lambda}$-flat at the point $x_{\lambda}$.*

*(ii) For $\mathcal{F}$ to be $f$-flat, it is necessary and sufficient that there exist $\lambda \geq \alpha$ such that
$\mathcal{F}_{\lambda}$ is $f_{\lambda}$-flat.*

One may suppose that $S_{\alpha} = S_{0}$; since `Y_0` is of finite presentation over `S_0`, `Y_0` is quasi-compact, and
$f_{0} : X_{0} \to Y_{0}$ is a morphism of finite presentation `(1.6.2, (v))`, hence one may also confine oneself to the
case where $S_{0} = Y_{0}$. Moreover, by virtue of the quasi-compactness of `S_0` and of the fact that the index set $L$
is filtered, one may confine oneself to the case where $S_{0} = \operatorname{Spec}(A_{0})$ is affine. In addition `X_0`
is quasi-compact, hence the same reasoning shows that one may also suppose $X_{0} = \operatorname{Spec}(B_{0})$ affine;
one then has $\mathcal{F}_{0} = \tilde{M}_{0}$, where `M_0` is a `B_0`-module of finite presentation, and the statement
`(11.2.6)` is in this case equivalent to the following (taking $(0_{I}, 6.3.1)$ into account):

**Corollary (11.2.6.1).**

<!-- label: IV.11.2.6.1 -->

*Let `A_0` be a ring, $(A_{\lambda})_{\lambda \in L}$ a filtered inductive system of `A_0`-algebras, `B_0` an
`A_0`-algebra of finite presentation, `M_0` a `B_0`-module of finite presentation. Set $B_{\lambda} = B_{0}
\otimes_{A_{0}} A_{\lambda}$, $M_{\lambda} = M_{0} \otimes_{A_{0}} A_{\lambda} = M_{0} \otimes_{B_{0}} B_{\lambda}$, $A
= \lim A_{\lambda}$, $B = \lim B_{\lambda} = B_{0} \otimes_{A_{0}} A$, $M = \lim M_{\lambda} = M_{0} \otimes_{A_{0}} A =
M_{0} \otimes_{B_{0}} B$.*

*(i) Let $\mathfrak{p}$ be a prime ideal of $B$, and for every $\lambda$, let $\mathfrak{p}_{\lambda}$ be its inverse
image in $B_{\lambda}$. For $M_{\mathfrak{p}}$ to be a flat $A$-module, it is necessary and sufficient that there exist
$\lambda$ such that $(M_{\lambda})_{\mathfrak{p}_{\lambda}}$ is a flat $A_{\lambda}$-module.*

*(ii) For $M$ to be a flat $A$-module, it is necessary and sufficient that there exist $\lambda$ such that $M_{\lambda}$
is a flat $A_{\lambda}$-module.*

One has only to prove that the conditions are necessary `(2.1.4)`. We shall proceed in several steps.

*I) Reduction to the case where the $A_{\lambda}$ are Noetherian.* By virtue of `(8.9.1)`, there exists a sub-ring
$A'_{0}$ of `A_0` which is a $\mathbb{Z}$-algebra of finite type, an $A'_{0}$-algebra of finite type $B'_{0}$ and a
$B'_{0}$-module of finite type $M'_{0}$ such that one has $B_{0} = B'_{0} \otimes_{A'_{0}} A_{0}$ and $M_{0} = M'_{0}
\otimes_{A'_{0}} A_{0}$; since one has $B_{\lambda} = B'_{0} \otimes_{A'_{0}} A_{\lambda}$ and $M_{\lambda} = M'_{0}
\otimes_{A'_{0}} A_{\lambda}$, one may replace `A_0`, `B_0`, `M_0` by $A'_{0}$, $B'_{0}$, $M'_{0}$ in the statement of
`(11.2.6.1)`, considering the $A_{\lambda}$ as $A'_{0}$-algebras; one may therefore already suppose that `A_0` is
Noetherian. Let $H$ be the set of pairs $(\lambda, C_{\lambda})$, where $C_{\lambda}$ is a sub-`A_0`-algebra of finite
type of $A_{\lambda}$; order $H$ by setting $(\lambda, C_{\lambda}) \leq (\mu, D_{\mu})$ if $\lambda \leq \mu$ and the
homomorphism $\phi_{\mu \lambda} : A_{\lambda} \to A_{\mu}$ is such that $\phi_{\mu \lambda}(C_{\lambda}) \subset
D_{\mu}$; for this order $H$ is filtered increasing, for if $(\lambda, C_{\lambda})$ and $(\mu, D_{\mu})$ are two
arbitrary elements of $H$, one majorizes them by an $(\nu, E_{\nu})$ by taking $\nu \geq \lambda$, $\nu \geq \mu$ in
$L$, then $E_{\nu}$ equal to the sub-`A_0`-algebra of $A_{\nu}$ generated by $\phi_{\nu \lambda}(C_{\lambda})$ and
$\phi_{\nu \mu}(D_{\mu})$. For an element $\xi = (\lambda, C_{\lambda})$ of $H$, one will set $A_{\xi} = C_{\lambda}$,
and for $\xi \leq \eta = (\mu, D_{\mu})$ (hence $\lambda \leq \mu$ and $\phi_{\mu \lambda}(C_{\lambda}) \subset
D_{\mu}$), $\phi_{\eta \xi} : A_{\xi} \to A_{\eta}$ will be the restriction to $C_{\lambda}$ of $\phi_{\mu \lambda}$,
considered as a homomorphism into $D_{\mu}$; it is clear that one thus obtains a filtered inductive system of
`A_0`-algebras. One sets $B_{\xi} = B_{0} \otimes_{A_{0}} A_{\xi}$, $M_{\xi} = M_{0} \otimes_{A_{0}} A_{\xi}$; this time
the $A_{\xi}$ are Noetherian; moreover the double-inductive-limit formula *(Bourbaki, Alg., chap. II, 3rd ed., §6, n° 4,
prop. 7)* proves that one again has $\lim_{H} A_{\xi} = A$, $\lim_{H} B_{\xi} = B$, $\lim_{H} M_{\xi} = M$. Suppose

<!-- original page 125 -->

`(11.2.6.1)` proved for the inductive system $(A_{\xi})_{\xi \in H}$; let $\mathfrak{p}$ be a prime ideal of $B$, such
that $M_{\mathfrak{p}}$ is a flat $A$-module; there then exists $\xi \in H$ such that, if $\mathfrak{p}_{\xi}$ is the
inverse image of $\mathfrak{p}$ in $B_{\xi}$, $(M_{\xi})_{\mathfrak{p}_{\xi}}$ is a flat $A_{\xi}$-module. Let $\xi =
(\lambda, C_{\lambda})$, so that the injection $A_{\xi} = C_{\lambda} \to A_{\lambda}$ gives a homomorphism $B_{\xi} =
B_{0} \otimes_{A_{0}} C_{\lambda} \to B_{\lambda} = B_{0} \otimes_{A_{0}} A_{\lambda}$, and if $\mathfrak{p}_{\lambda}$
is the inverse image of $\mathfrak{p}$ in $B_{\lambda}$, $\mathfrak{p}_{\xi}$ is the inverse image of
$\mathfrak{p}_{\lambda}$ in $B_{\xi}$; consequently $(M_{\lambda})_{\mathfrak{p}_{\lambda}} = (M_{\xi}
\otimes_{C_{\lambda}} A_{\lambda})_{\mathfrak{p}_{\lambda}} = ((M_{\xi})_{\mathfrak{p}_{\xi}} \otimes_{C_{\lambda}}
A_{\lambda})_{\mathfrak{p}_{\lambda}}$, hence $(M_{\lambda})_{\mathfrak{p}_{\lambda}}$ is a flat $A_{\lambda}$-module
$(0_{I}, 6.2.1 and 6.3.2)$. One treats similarly case (ii) of the statement. We may therefore in the sequel suppose the
$A_{\lambda}$ Noetherian for $\lambda \in L$ (but not necessarily $A$ itself).

*II) Reduction of the global statement (ii) to the pointwise statement (i).* Suppose that $\mathcal{F}$ is $f$-flat. For
every $\lambda$, let $U_{\lambda}$ be the set of $x_{\lambda} \in X_{\lambda}$ such that $\mathcal{F}_{\lambda}$ is
$f_{\lambda}$-flat at the point $x_{\lambda}$; one knows that $U_{\lambda}$ is open in $X_{\lambda}$ since $S_{\lambda}$
is Noetherian and $f_{\lambda}$ of finite type `(11.1.1)`; let $V_{\lambda} = v^{-1}_{\lambda}(U_{\lambda})$ be its
inverse image in $X$. Since by hypothesis, for every $x \in X$, there is a $\lambda$ such that $\mathcal{F}_{\lambda}$
is $f_{\lambda}$-flat at the point $x_{\lambda}$, projection of $x$ in $X_{\lambda}$, this signifies that $x \in
V_{\lambda}$ for some $\lambda$; in other words, $X$ is the union of the $V_{\lambda}$. Moreover `(2.1.4)`, for $\lambda
\leq \mu$, one has $V_{\lambda} \subset V_{\mu}$, hence, since $X$ is quasi-compact, there exists an index $\mu$ such
that $X = V_{\mu}$. Since the $X_{\lambda}$ are quasi-compact, it follows from `(8.3.4)` that there exists an index $\nu
\geq \mu$ such that $v^{-1}_{\nu \mu}(U_{\mu}) = X_{\nu}$; but by `(2.1.4)`, this entails that $\mathcal{F}_{\nu}$ is
$f_{\nu}$-flat.

*III) End of the proof.* It remains to prove (i), supposing `S_0` affine and Noetherian; if $y_{0}$ is the projection of
$x$ in `S_0`, one may in addition, by virtue of `(2.1.4)` and `(I, 3.6.5)`, replace `S_0` by
$\operatorname{Spec}(\mathcal{O}_{S_{0}, y_{0}})$, in other words one may confine oneself to the case where `A_0` is a
Noetherian local ring, of maximal ideal $\mathfrak{m}_{0} = y_{0}$; by definition, $\mathfrak{m}_{0}$ is the inverse
image of the prime ideal $\mathfrak{p} = x$ of $B$, and $M_{\mathfrak{p}}$ is supposed to be a flat $A$-module; one
therefore has in particular $Tor^{A}_{1}(A/\mathfrak{m}_{0} A, M_{\mathfrak{p}}) = 0$, which also writes, since the
$Tor^{A}_{i}(A/\mathfrak{m}_{0} A, M)$ are $B$-modules and $B_{\mathfrak{p}}$ is flat over $B$,
$(Tor^{A}_{1}(A/\mathfrak{m}_{0} A, M))_{\mathfrak{p}} = 0$. Let us note now that
$Tor^{A_{0}}_{1}(A_{0}/\mathfrak{m}_{0}, M_{0})$ is a `B_0`-module of finite type, for one may define it by taking a
resolution of $A_{0}/\mathfrak{m}_{0}$ by free `A_0`-modules of finite type (since `A_0` is Noetherian) and tensoring
with `M_0`, which gives `B_0`-modules of finite type; since `B_0` is Noetherian, the homology of the complex thus
obtained is indeed formed of `B_0`-modules of finite type. Let $(t^{0}_{i})_{1 \leq i \leq m}$ be a system of generators
of the `B_0`-module $Tor^{A_{0}}_{1}(A_{0}/\mathfrak{m}_{0}, M_{0})$ and let $t_{i}$ be the canonical image `(11.2.1.1)`
of $t^{0}_{i}$ in $Tor^{A}_{1}(A/\mathfrak{m}_{0} A, M)$. The hypothesis entails that there exists $h \in B -
\mathfrak{p}$ such that $h t_{i} = 0$ for $1 \leq i \leq m$. Now one has `(11.2.2.1)`
`Tor_1^A(A/𝔪_0 A, M) = lim_λ Tor_1^{A_λ}(A_λ/𝔪_0 A_λ, M_λ)`; there exists therefore a $\lambda$ such that, if the
$t^{\lambda}_{i}$ are the images of the $t^{0}_{i}$ in $Tor^{A_{\lambda}}_{1}(A_{\lambda}/\mathfrak{m}_{0} A_{\lambda},
M_{\lambda})$, there exists $h_{\lambda} \in B_{\lambda}$ of image $h$, such that $h_{\lambda} t^{\lambda}_{i} = 0$ for
$1 \leq i \leq m$. Let $\mathfrak{p}_{\lambda} = v_{\lambda}(\mathfrak{p})$ be the prime ideal of $B_{\lambda}$ inverse
image of $\mathfrak{p}$; one has $h_{\lambda} \in B_{\lambda} - \mathfrak{p}_{\lambda}$, hence the canonical images of
the $t^{\lambda}_{i}$ in $(Tor^{A_{\lambda}}_{1}(A_{\lambda}/\mathfrak{m}_{0} A_{\lambda},
M_{\lambda}))_{\mathfrak{p}_{\lambda}}$ are zero, and consequently the homomorphism
$Tor^{A_{0}}_{1}(A_{0}/\mathfrak{m}_{0}, M_{0}) \to (Tor^{A_{\lambda}}_{1}(A_{\lambda}/\mathfrak{m}_{0} A_{\lambda},
M_{\lambda}))_{\mathfrak{p}_{\lambda}}$ is zero. The conditions of lemma `(11.2.5)` are therefore satisfied
($A_{0}/\mathfrak{m}_{0}$ being a field), and $(M_{\lambda})_{\mathfrak{p}_{\lambda}}$ is a flat $A_{\lambda}$-module,
which finishes the proof of the theorem.

**Corollary (11.2.7).**

<!-- label: IV.11.2.7 -->

*Let $S = \operatorname{Spec}(A)$ be an affine scheme, $f : X \to S$ a morphism, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module, $x$ a point of $X$. The following conditions are equivalent:*

*a) $f$ is a morphism of finite presentation, $\mathcal{F}$ is an $\mathcal{O}_{X}$-Module of finite presentation and
$\mathcal{F}$ is $f$-flat at the point $x$ (resp. $f$-flat).*

<!-- original page 126 -->

*b) There exist a Noetherian affine scheme $S_{0} = \operatorname{Spec}(A_{0})$, a morphism of finite type $f_{0} :
X_{0} \to S_{0}$, a coherent $\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$, a morphism $S \to S_{0}$ such that the
$S$-prescheme $X_{0} \otimes_{S_{0}} S$ is $S$-isomorphic to $X$ and that, if one identifies $X$ with $X_{0}
\otimes_{S_{0}} S$, $\mathcal{F}$ is isomorphic to $\mathcal{F}_{0} \otimes_{\mathcal{O}_{S_{0}}} \mathcal{O}_{S}$, and
$\mathcal{F}_{0}$ is $f_{0}$-flat at the point $x_{0}$ projection of $x$ in `X_0` (resp. $f_{0}$-flat).*

*c) The conditions of b) are verified and in addition `A_0` is a sub-$\mathbb{Z}$-algebra of finite type of $A$, the
morphism $S \to S_{0}$ corresponding to the canonical injection $A_{0} \to A$.*

It is clear that c) implies b) and b) implies a) by virtue of `(2.1.4)`. On the other hand, one may consider $A$ as the
inductive limit of its sub-$\mathbb{Z}$-algebras of finite type, and one knows by `(8.9.1)` that there is such a
sub-algebra `A_0` and a morphism of finite type $f_{0} : X_{0} \to S_{0}$ such that $X$ is $S$-isomorphic to $X_{0}
\times_{S_{0}} S$ and $\mathcal{F}$ isomorphic to $\mathcal{F}_{0} \otimes_{\mathcal{O}_{S_{0}}} \mathcal{O}_{S}$; one
may therefore write $X = \lim X_{\lambda}$, where $X_{\lambda} = X_{0} \otimes_{A_{0}} A_{\lambda}$, $A_{\lambda}$
running through the set of sub-$\mathbb{Z}$-algebras of finite type of $A$ containing `A_0`, and $\mathcal{F} =
v^{*}_{\lambda}(\mathcal{F}_{\lambda})$, where $v_{\lambda} : X \to X_{\lambda}$ is the canonical projection and
$\mathcal{F}_{\lambda} = \mathcal{F}_{0} \otimes_{A_{0}} A_{\lambda}$. It follows from `(11.2.6)` that there exists
$\lambda$ such that $\mathcal{F}_{\lambda}$ is $f_{\lambda}$-flat at the point $x_{\lambda} = v_{\lambda}(x)$ (resp.
$f_{\lambda}$-flat); then the sub-ring $A_{\lambda}$ of $A$ verifies the conditions of c).

**Proposition (11.2.8).**

<!-- label: IV.11.2.8 -->

*Let $g : X \to S$, $h : Y \to S$ be two morphisms of finite presentation, $f : X \to Y$ an $S$-morphism, $\mathcal{F}$
a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation; for every $s \in S$, let $X_{s} = g^{-1}(s) = X
\times_{S} \operatorname{Spec}(k(s))$, $Y_{s} = h^{-1}(s) = Y \times_{S} \operatorname{Spec}(k(s))$, $f_{s}$ the
morphism $f \times_{S} 1 : X_{s} \to Y_{s}$, $\mathcal{F}_{s} = \mathcal{F} \otimes_{\mathcal{O}_{S}} k(s)$. Then the
set $E$ of $s \in S$ such that $\mathcal{F}_{s}$ is $f_{s}$-flat is locally constructible.*

The property that we wish to show constructible verifies condition `(9.2.1, (i))`, by virtue of `(2.2.13)` and
`(2.5.1)`. Taking `(9.2.3)` into account, one may therefore confine oneself to the case where $S$ is affine, Noetherian,
and integral, with generic point $\eta$, and to prove that $E$ or $S - E$ is a neighbourhood of $\eta$ in $S$. If $\eta
\in S - E$, this follows at once from lemma `(9.4.7.1)`. If on the contrary $\eta \in E$, it follows first of all from
`(11.2.6)`, applied according to the method of `(8.1.2, a))`, that there is an open neighbourhood $U$ of $\eta$ in $S$
such that $\mathcal{F} | g^{-1}(U)$ is $h^{-1}(U)$-flat; *a fortiori* `(2.1.4)` $\mathcal{F}_{s}$ is $f_{s}$-flat for
every $s \in U$, which finishes the proof.

The following theorem generalizes `(11.2.6.1, (ii))`:

**Theorem (11.2.9) (Raynaud).**

<!-- label: IV.11.2.9 -->

*Let `A_0` be a ring, $(A_{\lambda})_{\lambda \in L}$ a filtered inductive system of `A_0`-algebras, `B_0` an
`A_0`-algebra of finite presentation, $\mathfrak{J}_{0}$ an ideal of finite type of `B_0`, `M_0` a `B_0`-module of
finite presentation. Set $B_{\lambda} = B_{0} \otimes_{A_{0}} A_{\lambda}$, $\mathfrak{J}_{\lambda} = \mathfrak{J}_{0}
B_{\lambda}$, $M_{\lambda} = M_{0} \otimes_{A_{0}} A_{\lambda} = M_{0} \otimes_{B_{0}} B_{\lambda}$, $A = \lim
A_{\lambda}$, $B = \lim B_{\lambda} = B_{0} \otimes_{A_{0}} A$, $\mathfrak{J} = \mathfrak{J}_{0} B$, $M = \lim
M_{\lambda} = M_{0} \otimes_{A_{0}} A = M_{0} \otimes_{B_{0}} B$. For $gr^{\bullet}_{\mathfrak{J}}(M)$ to be a flat
$A$-module, it is necessary and sufficient that there exist $\lambda$ such that
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ is a flat $A_{\lambda}$-module; the canonical homomorphisms*

```text
  (11.2.9.1)    gr_{𝔍_λ}^•(M_λ) ⊗_{A_λ} A_μ → gr_{𝔍_μ}^•(M_μ)    for μ ≥ λ
```

*are then bijective and $gr^{\bullet}_{\mathfrak{J}_{\mu}}(M_{\mu})$ is a flat $A_{\mu}$-module for $\mu \geq \lambda$.*

Let us first show that the conditions are sufficient, which amounts to proving the bijectivity of `(11.2.9.1)`. This
follows from the following lemma:

<!-- original page 127 -->

**Lemma (11.2.9.2).**

<!-- label: IV.11.2.9.2 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $M$ a $B$-module, $\mathfrak{J}$ an ideal of $B$. Let $A'$ be an $A$-algebra;
set $B' = B \otimes_{A} A'$, $M' = M \otimes_{A} A' = M \otimes_{B} B'$, $\mathfrak{J}' = \mathfrak{J} B'$. If
$gr^{\bullet}_{\mathfrak{J}}(M)$ is a flat $A$-module, the canonical homomorphism*

```text
  gr_𝔍^•(M) ⊗_A A' → gr_{𝔍'}^•(M')
```

*is bijective.*

Indeed, by induction on $k$, the hypothesis that the $\mathfrak{J}^{k} M/\mathfrak{J}^{k+1} M$ are flat $A$-modules for
$k \geq 0$ first entails, by $(0_{I}, 6.1.2)$, that $M/\mathfrak{J}^{k+1} M$ is a flat $A$-module; moreover $(0_{I},
6.1.2)$, the sequence

```text
  0 → (𝔍^{k+1} M) ⊗_A A' → M ⊗_A A' → (M/𝔍^{k+1} M) ⊗_A A' → 0
```

is then exact, in other words $(\mathfrak{J}^{k+1} M) \otimes_{A} A'$ identifies with its canonical image in $M' = M
\otimes_{A} A'$. On the other hand, still by virtue of $(0_{I}, 6.1.2)$, the sequence

```text
  0 → (𝔍^{k+1} M) ⊗_A A' → (𝔍^k M) ⊗_A A' → (𝔍^k M/𝔍^{k+1} M) ⊗_A A' → 0
```

is exact, which proves the lemma.

To prove the necessity of the conditions of `(11.2.9)`, we shall proceed in several steps.

*I) Reduction to the case where the $A_{\lambda}$ are Noetherian.* — One proceeds as in reduction I) of `(11.2.6.1)`,
whose notation we keep; one must simply begin by replacing $A'_{0}$ by a sub-$A'_{0}$-algebra of finite type $A''_{0}$
of `A_0` such that, if one sets $B''_{0} = B'_{0} \otimes_{A'_{0}} A''_{0}$, there is in $B''_{0}$ an ideal of finite
type $\mathfrak{J}''_{0}$ such that $\mathfrak{J}''_{0} B_{0} = \mathfrak{J}_{0}$. For this, one considers the
sub-$A'_{0}$-algebras $A''_{\beta}$ of finite type of `A_0`, which form a filtered family, and one has $B_{0} = \lim
B''_{\beta}$, where $B''_{\beta} = B'_{0} \otimes_{A'_{0}} A''_{\beta}$; there is therefore an index $\beta$ such that a
finite system of generators of $\mathfrak{J}_{0}$ is formed of images in `B_0` of elements of $B''_{\beta}$; one will
then take $A''_{0} = A''_{\beta}$, $B''_{0} = B''_{\beta}$ and for $\mathfrak{J}''_{0}$ the ideal generated by these
elements. One may therefore suppose that `A_0` (hence also `B_0`) is Noetherian. One then defines as *loc. cit.* the
filtered set $H$ and the $A_{\xi}$, $B_{\xi}$, $M_{\xi}$ for $\xi \in H$; one will also set $\mathfrak{J}_{\xi} =
\mathfrak{J}_{0} B_{\xi}$ for every $\xi \in H$. Suppose then that one has proved that there exists a $\xi = (\lambda,
C_{\lambda})$ such that $gr^{\bullet}_{\mathfrak{J}_{\xi}}(M_{\xi})$ is a flat $C_{\lambda}$-module; since $M_{\lambda}
= M_{\xi} \otimes_{C_{\lambda}} A_{\lambda}$, it follows from `(11.2.9.2)` that
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ is a flat $A_{\lambda}$-module.

*II) Preliminary lemmas.*

**Lemma (11.2.9.3).**

<!-- label: IV.11.2.9.3 -->

*Let $A$ be a ring, $B = \bigoplus_{i \geq 0} B_{i}$ a graded $A$-algebra with positive degrees, $M = \bigoplus M_{i}$ a
graded $B$-module. Suppose that `B_0` is a local ring, and that each of the $M_{i}$ is a `B_0`-module of finite type.
For $M$ to be a $B$-module of finite type, it is necessary and sufficient that, if $\mathfrak{q}$ is the inverse image
in $A$ of the maximal ideal $\mathfrak{m}$ of `B_0`, $M \otimes_{A} k(\mathfrak{q})$ be a $(B \otimes_{A}
k(\mathfrak{q}))$-module of finite type.*

The condition being evidently necessary, let us prove that it is sufficient. Since `B_0` (and consequently $B$) is an
$A_{\mathfrak{q}}$-algebra, one may replace $A$ by $A_{\mathfrak{q}}$, in other words suppose

<!-- original page 128 -->

that $A$ is also a local ring of which $\mathfrak{q}$ is the maximal ideal. By hypothesis, there exists an integer $N$
such that the canonical homomorphism

```text
  ⨁_{i ≤ N} M_i ⊗_A k(𝔮) → M ⊗_A k(𝔮)
```

is surjective; this also signifies that, for every integer $n$, the canonical homomorphism of $k(\mathfrak{q})$-modules

```text
  ⨁_{i ≤ N} B_{n-i} ⊗_{B_0} M_i ⊗_A k(𝔮) → M_n ⊗_A k(𝔮)
```

is surjective. Now, $M_{n}$ is a `B_0`-module of finite type, `B_0` a local ring and $\mathfrak{q} B_{0} \subset
\mathfrak{m}$; hence Nakayama's lemma proves that each of the canonical homomorphisms

```text
  ⨁_{i ≤ N} B_{n-i} ⊗_{B_0} M_i → M_n
```

is surjective, whence the conclusion.

**Corollary (11.2.9.4).**

<!-- label: IV.11.2.9.4 -->

*Under the hypotheses of `(11.2.9.3)`, suppose in addition that each of the $B_{i}$ and each of the $M_{i}$ is a
`B_0`-module of finite presentation, and that $M$ is a flat $A$-module. For $M$ to be a $B$-module of finite
presentation, it is necessary and sufficient that $M \otimes_{A} k(\mathfrak{q})$ be a $(B \otimes_{A}
k(\mathfrak{q}))$-module of finite presentation.*

By virtue of `(11.2.9.3)`, if the condition of the statement is verified, $M$ is a $B$-module of finite type, hence
there exists a graded free $B$-module of finite type $L$ (having therefore a finite basis formed of homogeneous
elements) and a surjective graded homomorphism of degree `0`, $u : L \to M$. Let $R = Ker(u)$, which is a graded
$B$-module; there is then a finite number of integers $m_{j}$ ($1 \leq j \leq r$) such that for each integer $i$,
$R_{i}$ is the kernel of a surjective homomorphism $\bigoplus_{1 \leq j \leq r} B_{i + m_{j}} \to M_{i}$; one concludes
then from the hypothesis on the $M_{i}$ and the $B_{i}$ that $R_{i}$ is a `B_0`-module of finite type *(Bourbaki, Alg.
comm., chap. I, §2, n° 8, lemma 9)*. To prove that $R$ is a $B$-module of finite type, note that by virtue of the
flatness hypothesis and of $(0_{I}, 6.1.2)$, the sequence

```text
  0 → R ⊗_A k(𝔮) → L ⊗_A k(𝔮) → M ⊗_A k(𝔮) → 0
```

is exact, and the hypothesis therefore entails *(Bourbaki, loc. cit.)* that $R \otimes_{A} k(\mathfrak{q})$ is a $(B
\otimes_{A} k(\mathfrak{q}))$-module of finite type; it therefore suffices to apply lemma `(11.2.9.3)` to $R$.

*III) Reduction to the case where the transition homomorphisms $\phi_{\mu \lambda} : A_{\lambda} \to A_{\mu}$ (for
$\lambda \leq \mu$) are injective.* — Let $A'_{\lambda}$ be the image of $A_{\lambda}$ under the canonical homomorphism
$\phi_{\lambda} : A_{\lambda} \to A$; it is clear that the $A'_{\lambda}$ form an inductive system of Noetherian
sub-rings of $A$, whose inductive limit is $A$, and the transition homomorphisms $A'_{\lambda} \to A'_{\mu}$ (for
$\lambda \leq \mu$) are injective. Set $B'_{\lambda} = B_{0} \otimes_{A_{0}} A'_{\lambda}$, $\mathfrak{J}'_{\lambda} =
\mathfrak{J}_{0} B'_{\lambda}$, $M'_{\lambda} = M_{0} \otimes_{A_{0}} A'_{\lambda} = M_{\lambda} \otimes_{A_{\lambda}}
A'_{\lambda}$; one has again $B = \lim B'_{\lambda}$, $M = \lim M'_{\lambda}$. Suppose that one has proved that there
exists a $\lambda$ such that, for $\mu \geq \lambda$, $gr^{\bullet}_{\mathfrak{J}'_{\mu}}(M'_{\mu})$ is a flat
$A'_{\mu}$-module. Let $\mathfrak{a}_{\lambda}$ be the kernel of the homomorphism $\phi_{\lambda}$, which is therefore
an ideal of finite type of the Noetherian ring $A_{\lambda}$. It follows from the definition of the inductive limit that
there exists an index $\mu \geq \lambda$ such that $\phi_{\mu \lambda}(\mathfrak{a}_{\lambda}) = 0$, in other words the
homomorphism $\phi_{\mu}$ factorizes as $A_{\lambda} \to A'_{\lambda} \to A_{\mu}$, and one may write $B_{\mu} =
B'_{\lambda} \otimes_{A'_{\lambda}} A_{\mu}$, $\mathfrak{J}_{\mu} = \mathfrak{J}'_{\lambda} B_{\mu}$ and $M_{\mu} =
M'_{\lambda} \otimes_{A'_{\lambda}} A_{\mu}$; one therefore deduces from `(11.2.9.2)` that
$gr^{\bullet}_{\mathfrak{J}_{\mu}}(M_{\mu})$ is a flat $A_{\mu}$-module.

*IV) Reduction to the case where $B_{0} = A_{0}[T_{1}, \cdots, T_{n}]$ and $gr^{\bullet}_{\mathfrak{J}_{0}}(B_{0}) =
B_{0}$.* — By virtue of the hypothesis, there is a system $(t_{i})_{1 \leq i \leq n}$ of generators of the `A_0`-algebra
of finite type `B_0`, such that the $t_{i}$ for $i \leq m$ generate the ideal $\mathfrak{J}_{0}$ of `B_0`. Set $B'_{0} =
A_{0}[T_{1}, \cdots, T_{n}]$,

<!-- original page 129 -->

a polynomial algebra (hence Noetherian), and let $\mathfrak{J}'_{0}$ be the ideal of $B'_{0}$ generated by the $T_{i}$
of index $i \leq m$; one then has a surjective `A_0`-homomorphism $u_{0} : B'_{0} \to B_{0}$ transforming each $T_{i}$
into $t_{i}$ ($1 \leq i \leq n$), hence such that $u_{0}(\mathfrak{J}'_{0}) = \mathfrak{J}_{0}$; this homomorphism
permits one to consider `M_0` as a $B'_{0}$-module of finite type. One then sets $B'_{\lambda} = B'_{0} \otimes_{A_{0}}
A_{\lambda} = A_{\lambda}[T_{1}, \cdots, T_{n}]$, $\mathfrak{J}'_{\lambda} = \mathfrak{J}'_{0} B'_{\lambda}$, $B' =
B'_{0} \otimes_{A_{0}} A = A[T_{1}, \cdots, T_{n}]$, $\mathfrak{J}' = \mathfrak{J}'_{0} B'$, so that $\mathfrak{J}'$ is
the ideal of $B'$ generated by the $T_{i}$ of index $i \leq m$; moreover, it is clear that for every integer $k \geq 0$,
one has $\mathfrak{J}'^{k} M = \mathfrak{J}^{k} M$ and $\mathfrak{J}'^{k}_{\lambda} M_{\lambda} =
\mathfrak{J}^{k}_{\lambda} M_{\lambda}$ for every $\lambda$; hence $gr^{\bullet}_{\mathfrak{J}'}(M) =
gr^{\bullet}_{\mathfrak{J}}(M)$ as an $A$-module and $gr^{\bullet}_{\mathfrak{J}'_{\lambda}}(M_{\lambda}) =
gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ as an $A_{\lambda}$-module; one may therefore substitute $B'$,
$B'_{\lambda}$, $\mathfrak{J}'$, $\mathfrak{J}'_{\lambda}$ for $B$, $B_{\lambda}$, $\mathfrak{J}$,
$\mathfrak{J}_{\lambda}$ respectively in the proof; one will note in addition that by construction
$gr^{\bullet}_{\mathfrak{J}'_{0}}(B'_{0})$ identifies with $B'_{0}$ and
$gr^{\bullet}_{\mathfrak{J}'_{\lambda}}(B'_{\lambda})$ with $B'_{\lambda}$.

*V) Proof that $gr^{\bullet}_{\mathfrak{J}}(M)$ is a $gr^{\bullet}_{\mathfrak{J}}(B)$-module of finite presentation.* —
We therefore suppose from now on `A_0` and the $A_{\lambda}$ Noetherian, the transition homomorphisms $A_{\lambda} \to
A_{\mu}$ injective, $B_{0} = A_{0}[T_{1}, \cdots, T_{n}]$, $\mathfrak{J}_{0}$ being generated by the $T_{i}$ of index $i
\leq m$; the ring $C_{0} = gr^{\bullet}_{\mathfrak{J}_{0}}(B_{0})$ therefore identifies with `B_0` and $C =
gr^{\bullet}_{\mathfrak{J}}(B)$ identifies with $B$; we shall in the sequel use only first of all the fact that $C =
C_{0} \otimes_{A_{0}} A$.

We shall need the following variant of `(6.9.3)`:

**Lemma (11.2.9.5).**

<!-- label: IV.11.2.9.5 -->

*Let `A_0` be a Noetherian ring, `B_0` an `A_0`-algebra of finite type, $\mathfrak{J}_{0}$ an ideal of `B_0`, `M_0` a
`B_0`-module of finite type. There exists then a sequence $(S_{0i})_{1 \leq i \leq m}$ of sub-schemes of $S_{0} =
\operatorname{Spec}(A_{0})$ having the following properties:*

*1° The spaces underlying the $S_{0i}$ are pairwise disjoint and form a covering of `S_0`.*

*2° For each $i$, the set $S_{0i}$ is open in $\bigcup_{j \geq i} S_{0j}$.*

*3° Each scheme $S_{0i}$ is affine.*

*4° If $A_{0i}$ is the ring of $S_{0i}$ and if one sets $B_{0i} = B_{0} \otimes_{A_{0}} A_{0i}$, $\mathfrak{J}_{0i} =
\mathfrak{J}_{0} B_{0i}$, then $gr^{\bullet}_{\mathfrak{J}_{0i}}(M_{0} \otimes_{A_{0}} A_{0i})$ is a flat
$A_{0i}$-module.*

One proceeds as in `(6.9.3)` by Noetherian induction, supposing the lemma true when one replaces in it `A_0` by $A'_{0}
= A_{0}/\mathfrak{a}_{0}$, where the ideal $\mathfrak{a}_{0}$ is such that $V(\mathfrak{a}_{0}) \neq S_{0}$, `B_0` by
$B'_{0} = B_{0} \otimes_{A_{0}} A'_{0}$, $\mathfrak{J}_{0}$ by $\mathfrak{J}'_{0} = \mathfrak{J}_{0} B'_{0}$ and `M_0`
by $M_{0} \otimes_{A_{0}} A'_{0}$. One considers the nilradical $\mathfrak{N}_{0}$ of `A_0`, and it evidently suffices
to prove the lemma replacing `A_0` by $A_{0}/\mathfrak{N}_{0}$ and `B_0`, $\mathfrak{J}_{0}$, `M_0` by the corresponding
objects as above. In other words, one may suppose that `A_0` is reduced; on the other hand,
$gr^{\bullet}_{\mathfrak{J}_{0}}(B_{0})$ is an `A_0`-algebra of finite type and $gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0})$
a $gr^{\bullet}_{\mathfrak{J}_{0}}(B_{0})$-module of finite type; by virtue of the generic flatness theorem `(6.9.1)`,
there exists an open set $D(t_{0}) \subset S_{0}$ such that if one sets $A_{01} = (A_{0})_{t_{0}}$,
$gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0}) \otimes_{A_{0}} A_{01}$ is a flat $A_{01}$-module; but since $A_{01}$ is a flat
`A_0`-module, $gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0}) \otimes_{A_{0}} A_{01}$ identifies with
$gr^{\bullet}_{\mathfrak{J}_{01}}(M_{0} \otimes_{A_{0}} A_{01})$, where $B_{01} = B_{0} \otimes_{A_{0}} A_{01}$ and
$\mathfrak{J}_{01} = \mathfrak{J}_{0} B_{01}$. The complement of $D(t_{0})$ in `S_0` is then of the form
$V(\mathfrak{a}_{0})$, and one concludes by applying the Noetherian induction hypothesis.

Let us apply this lemma to the present situation, keeping the same notation; set $U_{0i} = \bigcup_{j \geq i} S_{0j}$,
which is a quasi-compact open set of `S_0`. There is therefore a finite family $(t_{ik})_{1 \leq i \leq m, 1 \leq k \leq
n_{i}}$ of elements of `A_0` such that for each $i$, $U_{0i}$ is the union of the $D(t_{ik})$ ($1 \leq k \leq n_{i}$).

<!-- original page 130 -->

The `C_0`-module $gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0})$ is generated by a finite number of homogeneous elements of
degree $i$, so that there is an epimorphism of graded `C_0`-modules $u_{0} : C^{r}_{0} \to
gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0})$. Since $C = C_{0} \otimes_{A_{0}} A$ and the canonical homomorphism
$gr^{\bullet}_{\mathfrak{J}_{0}}(M_{0}) \otimes_{A_{0}} A \to gr^{\bullet}_{\mathfrak{J}}(M)$ is surjective, one deduces
therefore from $u_{0}$ an epimorphism of graded $C$-modules

```text
  u : C^r → gr_{𝔍_0}^•(M_0) ⊗_{A_0} A → gr_𝔍^•(M),
```

and everything boils down to seeing that the graded $C$-module $Q = Ker(u)$ is of finite type.

**Lemma (11.2.9.6).**

<!-- label: IV.11.2.9.6 -->

*Under the preceding hypotheses, let $\mathfrak{A}_{0}$ be an ideal of `A_0`; set $A'_{0} = A_{0}/\mathfrak{A}_{0}$,
$B'_{0} = B_{0} \otimes_{A_{0}} A'_{0} = B_{0}/\mathfrak{A}_{0} B_{0}$, $\mathfrak{J}'_{0} = \mathfrak{J}_{0} B'_{0}$,
$\mathfrak{A} = \mathfrak{A}_{0} A$, $A' = A/\mathfrak{A}$, and suppose in addition that
$gr^{\bullet}_{\mathfrak{J}'_{0}}(M_{0} \otimes_{A_{0}} A'_{0})$ is a flat $A'_{0}$-module. Then there exists a finite
number of elements $q_{h}$ ($1 \leq h \leq s$) of $Q$ such that, for every prime ideal $\mathfrak{p} \supset
\mathfrak{A} B$ of $B$, the canonical images of the $q_{h}$ in $Q_{\mathfrak{p}}$ generate the $C_{\mathfrak{p}}$-module
$Q_{\mathfrak{p}}$.*

Suppose this lemma proved, and note that one may again apply it replacing `A_0` by $(A_{0})_{t_{0}}$, `B_0`,
$\mathfrak{J}_{0}$, `M_0`, $A_{\lambda}$ and $A$ by the corresponding objects $(B_{0})_{t_{0}}$,
$(\mathfrak{J}_{0})_{t_{0}}$, $(M_{0})_{t_{0}}$, $(A_{\lambda})_{t_{0}}$ and $A_{t_{0}}$, for any $t_{0} \in A_{0}$,
since $(A_{0})_{t_{0}}$ is a flat `A_0`-module. One will then apply this lemma replacing `A_0` successively by each of
the rings $(A_{0})_{t_{ik}}$, $\mathfrak{A}_{0}$ being replaced by the ideal $\mathfrak{A}_{ik}$ defining the closed
sub-scheme of $D(t_{ik})$ induced by $S_{0i}$ on the open set $S_{0i} \cap D(t_{ik})$ of $S_{0i}$. Since the flatness
hypothesis of `(11.2.9.6)` is verified in each of these cases by reason of `(11.2.9.5)`, one obtains in this way for
each pair $(i, k)$ a finite family $(q_{ikh})_{1 \leq h \leq l_{ik}}$ of elements of $Q_{t_{ik}}$ whose images in
$Q_{\mathfrak{p}_{ik}}$ generate this $C_{\mathfrak{p}_{ik}}$-module, for every prime ideal $\mathfrak{p}_{ik}$ of
$B_{t_{ik}}$ containing $\mathfrak{A}_{ik} B_{t_{ik}}$. One may write, for a suitable integer $d > 0$, $q_{ikh} =
b_{ikh}/t^{d}_{ik}$ for all the indices $i$, $k$, $h$, with $b_{ikh} \in Q$. Since the $S_{0i}$ cover `S_0`, every prime
ideal $\mathfrak{p}$ of $B$ is such that its image in `S_0` belongs to some set $S_{0i} \cap D(t_{ik})$, hence the image
$\mathfrak{p}_{ik}$ of $\mathfrak{p}$ in $B_{t_{ik}}$ contains $\mathfrak{A}_{ik} B_{t_{ik}}$. Since the images of the
$b_{ikh}$ ($1 \leq h \leq l_{ik}$) in $Q_{\mathfrak{p}_{ik}} = Q_{\mathfrak{p}}$ generate this
$C_{\mathfrak{p}}$-module, one concludes that the $b_{ikh}$ ($1 \leq i \leq m$, $1 \leq k \leq n_{i}$, $1 \leq h \leq
l_{ik}$) generate the $C$-module $Q$ *(Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1)*.

It remains to prove lemma `(11.2.9.6)`. Set $C' = C \otimes_{A} A' = C/\mathfrak{A} C$, $B' = B \otimes_{A} A'$,
$\mathfrak{J}' = \mathfrak{J} B'$, $M' = M \otimes_{A} A'$. By hypothesis $gr^{\bullet}_{\mathfrak{J}}(M)$ is a flat
$A$-module, hence $gr^{\bullet}_{\mathfrak{J}'}(M')$ identifies with $gr^{\bullet}_{\mathfrak{J}}(M) \otimes_{A} A'$
`(11.2.9.2)`, and one has the exact sequence $(0_{I}, 6.1.2)$

```text
  (11.2.9.7)    0 → Q ⊗_A A' → C'^r → gr_{𝔍'}^•(M') → 0.
```

Set $C'_{0} = C_{0} \otimes_{A_{0}} A'_{0} = C_{0}/\mathfrak{A}_{0} C_{0}$ and consider the epimorphism of graded
$C'_{0}$-modules

```text
  u'_0 = u_0 ⊗ 1_{A'_0} : C'^r_0 → gr_{𝔍_0}^•(M_0) ⊗_{A_0} A'_0 → gr_{𝔍'_0}^•(M_0 ⊗_{A_0} A'_0).
```

Let $Q'_{0} = Ker(u'_{0})$; using the fact that $gr^{\bullet}_{\mathfrak{J}'_{0}}(M_{0} \otimes_{A_{0}} A'_{0})$ is a
flat $A'_{0}$-module, one sees that $gr^{\bullet}_{\mathfrak{J}'_{0}}(M_{0} \otimes_{A_{0}} A'_{0}) \otimes_{A'_{0}} A'$
identifies with $gr^{\bullet}_{\mathfrak{J}'}(M')$ `(11.2.9.2)` and one has the exact sequence $(0_{I}, 6.1.2)$

```text
  (11.2.9.8)    0 → Q'_0 ⊗_{A'_0} A' → C'^r → gr_{𝔍'}^•(M') → 0,
```

<!-- original page 131 -->

whence, by comparison with `(11.2.9.7)`, an isomorphism of graded $C'$-modules

```text
  Q'_0 ⊗_{A'_0} A' ⥲ Q ⊗_A A'.
```

Since $C'_{0}$ is Noetherian, $Q'_{0}$ is a $C'_{0}$-module of finite type, hence $Q'_{0} \otimes_{A'_{0}} A'$ is a
graded $C'$-module of finite type, and consequently so is $Q \otimes_{A} A'$; let $q_{h}$ ($1 \leq h \leq s$) be
homogeneous elements of $Q$ whose images in $Q \otimes_{A} A'$ generate this $C'$-module.

Let us now consider an arbitrary prime ideal $\mathfrak{p} \supset \mathfrak{A} B$ of $B$; one has $C_{\mathfrak{p}} =
gr^{\bullet}_{\mathfrak{J}_{\mathfrak{p}}}(B_{\mathfrak{p}})$ by flatness, and
$gr^{0}_{\mathfrak{J}_{\mathfrak{p}}}(B_{\mathfrak{p}}) = B_{\mathfrak{p}}/\mathfrak{J}_{\mathfrak{p}}$ is reduced to
`0` or is a local ring; to prove the lemma, one may evidently confine oneself to the second case. It is then clear that
each of the $(B_{\mathfrak{p}}/\mathfrak{J}_{\mathfrak{p}})$-modules
$gr^{i}_{\mathfrak{J}_{\mathfrak{p}}}(B_{\mathfrak{p}})$ is of finite presentation. On the other hand, for every index
$i$, $M/\mathfrak{J}^{i} M$ identifies with $(M_{0}/\mathfrak{J}^{i}_{0} M_{0}) \otimes_{A_{0}} A$, and is therefore a
$B$-module of finite presentation. By induction on $i$, the hypothesis that $gr^{\bullet}_{\mathfrak{J}}(M)$ is a flat
$A$-module entails, by virtue of $(0_{I}, 6.1.2)$, that $M/\mathfrak{J}^{i} M$ is a flat $A$-module. The application of
`(11.2.6.1)` where one replaces `M_0` by $M_{0}/\mathfrak{J}^{k}_{0} M_{0}$ for $k \geq i$ shows that there exists an
index $\lambda_{i}$ such that, for $\mu \geq \lambda_{i}$, each of the $M_{\mu}/\mathfrak{J}^{i+1}_{\mu} M_{\mu}$ is a
flat $A_{\mu}$-module, and consequently also $(0_{I}, 6.1.2)$ each of the $gr^{i}_{\mathfrak{J}_{\mu}}(M_{\mu})$ is a
flat $A_{\mu}$-module for $k \leq i$. One deduces consequently from `(11.2.9.2)` that each of the
$(B/\mathfrak{J})$-modules $gr^{i}_{\mathfrak{J}}(M)$ is of finite presentation, hence
$gr^{\bullet}_{\mathfrak{J}_{\mathfrak{p}}}(M_{\mathfrak{p}})$ is a
$(B_{\mathfrak{p}}/\mathfrak{J}_{\mathfrak{p}})$-module of finite presentation. Moreover the images of the $q_{h}$ in
$Q_{\mathfrak{p}} \otimes_{B_{\mathfrak{p}}} k(\mathfrak{p}) = (Q \otimes_{A} A') \otimes_{A'} k(\mathfrak{p})$ generate
this $(C_{\mathfrak{p}} \otimes_{B_{\mathfrak{p}}} k(\mathfrak{p}))$-module (for $C_{\mathfrak{p}}
\otimes_{B_{\mathfrak{p}}} k(\mathfrak{p}) = C_{\mathfrak{p}} \otimes_{A'} k(\mathfrak{p})$); since one has the exact
sequence

```text
  0 → Q_𝔭 ⊗_{B_𝔭} k(𝔭) → C_𝔭^r ⊗_{B_𝔭} k(𝔭) → gr_{𝔍_𝔭}^•(M_𝔭) ⊗_{B_𝔭} k(𝔭) → 0,
```

one concludes that $gr^{\bullet}_{\mathfrak{J}_{\mathfrak{p}}}(M_{\mathfrak{p}}) \otimes_{B_{\mathfrak{p}}}
k(\mathfrak{p})$ is a $(C_{\mathfrak{p}} \otimes_{B_{\mathfrak{p}}} k(\mathfrak{p}))$-module of finite presentation.
Applying lemma `(11.2.9.4)` where $A$, $B$, $M$ are replaced respectively by $B_{\mathfrak{p}}$, $C_{\mathfrak{p}}$ and
$gr^{\bullet}_{\mathfrak{J}_{\mathfrak{p}}}(M_{\mathfrak{p}})$, one concludes that $Q_{\mathfrak{p}}$ is a
$C_{\mathfrak{p}}$-module of finite type. Now using Nakayama's lemma (and the fact that $C^{0} = B$), one deduces that
the images of the $q_{h}$ in $Q_{\mathfrak{p}}$ generate this $C_{\mathfrak{p}}$-module. This finishes the proof of
lemma `(11.2.9.6)` and of the fact that $gr^{\bullet}_{\mathfrak{J}}(M)$ is a $C$-module of finite presentation.

*VI) End of the proof.* — Set, to abbreviate, $C_{\lambda} = C_{0} \otimes_{A_{0}} A_{\lambda}$ (equal in fact to
$B_{\lambda}$), $N_{\lambda} = gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ and $N =
gr^{\bullet}_{\mathfrak{J}}(M)$. Note first that for each integer $k$, $\mathfrak{J}^{k} M$ identifies with $\lim
\mathfrak{J}^{k}_{\lambda} M_{\lambda}$ by exactness of the functor `lim`, the image of $\mathfrak{J}^{k}_{\lambda}
M_{\lambda}$ in $M_{\mu}$ for $\lambda \leq \mu$ (resp. in $M$) generating $\mathfrak{J}^{k}_{\mu} M_{\mu}$ (resp.
$\mathfrak{J}^{k} M$); using again the exactness of `lim`, one concludes that $N$ identifies canonically with $\lim
N_{\lambda}$. Making this identification, we shall first prove that:

*(11.2.9.9) For $\lambda$ sufficiently large, the canonical homomorphism $v_{\lambda} : N_{\lambda}
\otimes_{A_{\lambda}} A \to N$ is bijective.*

Since the $C_{\lambda}$ are Noetherian and $N_{\lambda}$ a $C_{\lambda}$-module of finite type, the $C$-modules
$N_{\lambda} \otimes_{A_{\lambda}} A$ are of finite presentation and form a filtered inductive system, whose inductive
limit identifies canonically with $N$ by virtue of the fact that `lim` commutes with tensor products. Moreover, the
transition homomorphisms $v_{\mu \lambda} : N_{\lambda} \otimes_{A_{\lambda}} A \to N_{\mu} \otimes_{A_{\mu}} A$

<!-- original page 132 -->

for $\lambda \leq \mu$ and the homomorphisms $v_{\lambda}$ are surjective. For a fixed $\lambda$, let us consider the
sub-$C$-modules $Ker(v_{\mu \lambda}) = N'_{\mu}$ of $N_{\lambda} \otimes_{A_{\lambda}} A$; by definition of the
inductive limit, they form a filtered increasing family of sub-$C$-modules of $Ker(v_{\lambda})$, whose union is
$Ker(v_{\lambda})$; but we have seen in V) that $N$ is a $C$-module of finite presentation, hence *(Bourbaki, Alg.
comm., chap. I, §2, n° 8, lemma 9)* $Ker(v_{\lambda})$ is a $C$-module of finite type; there exists consequently an
index $\mu \geq \lambda$ such that $N'_{\mu} = Ker(v_{\lambda})$, which signifies (in view of the fact that $v_{\mu
\lambda}$ is surjective) that $v_{\mu}$ is injective; since it is surjective, this proves `(11.2.9.9)`.

Up to replacing `A_0` and `M_0` by $A_{\lambda}$ and $M_{\lambda}$ for $\lambda$ sufficiently large, one may therefore
suppose that the canonical homomorphism $v_{\lambda}$ is bijective for every $\lambda$. Set then $P_{\lambda} = N_{0}
\otimes_{C_{0}} C_{\lambda} = N_{0} \otimes_{A_{0}} A_{\lambda}$, so that $N = \lim P_{\lambda}$. Since `C_0` is an
`A_0`-algebra of finite presentation and `P_0` a `C_0`-module of finite presentation, one may apply to $C$ and $N$ the
result of `(11.2.6.1)`, and one sees therefore that there exists an index $\lambda$ such that, for $\mu \geq \lambda$,
$P_{\mu}$ is a flat $A_{\mu}$-module. Now, for $\mu \geq \lambda$, one has a commutative diagram

```text
  P_μ  ──w_μ──→  N
   │            ‖
   ↓            ‖
  N_μ  ─v_μ──→  N
```

where it results from the definitions that $w_{\mu}$ is surjective. Since, by virtue of III), the homomorphisms $A_{\mu}
\to A$ are injective and $P_{\mu}$ is a flat $A_{\mu}$-module, the canonical homomorphism $P_{\mu} \to N = P_{\mu}
\otimes_{A_{\mu}} A$ is injective; one therefore concludes from the preceding commutative diagram that $w_{\mu}$ is also
injective, hence bijective, and consequently $N_{\mu}$ is a flat $A_{\mu}$-module for $\mu \geq \lambda$, which finishes
the proof of `(11.2.9)`.

**Remark (11.2.10).**

<!-- label: IV.11.2.10 -->

We do not know whether the generalization of `(11.2.6, (i))` analogous to Raynaud's theorem is valid.

### 11.3. Application to elimination of Noetherian hypotheses

**Theorem (11.3.1).**

<!-- label: IV.11.3.1 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation. Then the set $U$ of points $x \in X$ such that $\mathcal{F}$ is $f$-flat at the point $x$ is
open in $X$. Moreover, if $Supp(\mathcal{F}) = X$, $f | U$ is an open morphism.*

The second assertion has already been proved `(2.4.6)` and has been inserted only for the record.

The question being local on $X$ and $Y$, one may suppose that $X$ and $Y$ are affine, and that $f$ is a morphism of
finite presentation. Let $x \in X$ be a point such that $\mathcal{F}$ is $f$-flat at the point $x$. Applying `(11.2.7)`,
one may suppose that $X = X_{0} \times_{Y_{0}} Y$, $f = f_{0} \times_{S} 1$, $\mathcal{F} = \mathcal{F}_{0}
\otimes_{\mathcal{O}_{Y_{0}}} \mathcal{O}_{Y}$, where `Y_0` is Noetherian, $f_{0} : X_{0} \to Y_{0}$ a morphism of
finite type, $\mathcal{F}_{0}$ a coherent $\mathcal{O}_{X_{0}}$-Module; moreover, if $x_{0}$ is the canonical projection
of $x$ in `X_0`, one may suppose that $\mathcal{F}_{0}$ is $f_{0}$-flat at the point $x_{0}$. Then, by virtue of
`(11.1.1)`, the set `U_0` of points of `X_0` where $\mathcal{F}_{0}$ is $f_{0}$-flat is a neighbourhood of $x_{0}$;
hence $\mathcal{F}$ is $f$-flat at the points of the inverse image of `U_0` in $X$ `(2.1.4)`, and this proves that $U$
is a neighbourhood of $x$.

<!-- original page 133 -->

**Corollary (11.3.2).**

<!-- label: IV.11.3.2 -->

*Let $f : X \to Y$, $g : Y \to Z$ be two morphisms of finite presentation, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module of finite presentation. Then the set $U$ of $y \in Y$ such that, for every generization $y'$ of
$y$, $\mathcal{F}$ is $(g \circ f)$-flat at all points of $f^{-1}(y')$ (i.e. such that $\mathcal{F} \otimes_{Y}
\operatorname{Spec}(\mathcal{O}_{Y, y'})$ is flat relative to the morphism $X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{Y, y'}) \to Z$) is open in $Y$.*

The same reasoning as in `(11.1.5)` shows that if $V$ is the set of $x \in X$ where $\mathcal{F}$ is $(g \circ f)$-flat,
$U$ is the set of $y \in Y$ such that every generization of $y$ belongs to $E = Y - f(X - V)$. Since $g \circ f$ is of
finite presentation, $V$ is open in $X$ by virtue of `(11.3.1)`, hence ind-constructible `(1.9.6)`, and consequently
$X - V$ is pro-constructible; but since $f$ is quasi-compact, $f(X - V)$ is pro-constructible in $Y$ `(1.9.5, (vii))`,
and consequently $E$ is ind-constructible in $Y$. It then follows from `(1.10.1)` that $U$ is the interior of $E$, hence
open in $Y$.

**Corollary (11.3.3).**

<!-- label: IV.11.3.3 -->

*Let $A$ be a ring, $B$ an $A$-algebra of finite presentation, $C$ a $B$-algebra of finite presentation, $M$ a
$C$-module of finite presentation. Then the set of $\mathfrak{q} \in \operatorname{Spec}(B)$ such that
$M_{\mathfrak{q}}$ is a flat $A$-module is open in $\operatorname{Spec}(B)$.*

**Proposition (11.3.4).**

<!-- label: IV.11.3.4 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $\mathfrak{J}$ a quasi-coherent Ideal of finite type of
$\mathcal{O}_{X}$, $Y$ the closed sub-prescheme of $X$ defined by $\mathfrak{J}$, $\mathcal{F}$ an
$\mathcal{O}_{X}$-Module of finite presentation. Suppose that $gr^{\bullet}_{\mathfrak{J}}(\mathcal{F})$ is $f$-flat.
Under these conditions:*

*(i) $\mathcal{F}$ is $f$-flat at the points of $Y$.*

*(ii) If $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ is $f$-flat, $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ is
an $(\mathcal{O}_{X}/\mathfrak{J})$-Algebra of finite presentation and $gr^{\bullet}_{\mathfrak{J}}(\mathcal{F})$ is a
$(gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X}))$-Module of finite presentation.*

*(iii) Suppose $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ $f$-flat (which entails that
$\mathcal{O}_{X}/\mathfrak{J}$ is $f$-flat). Then the set $W$ of $y \in Y$ such that
$(gr^{\bullet}_{\mathfrak{J}}(\mathcal{F}))_{y}$ is a flat $\mathcal{O}_{X, y}$-module is open in $Y$.*

*(iv) Suppose $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ $f$-flat. Let $S' \to S$ be an arbitrary morphism; let $X'
= X \times_{S} S'$, $p : X' \to X$ the canonical projection, $Y' = p^{-1}(Y) = Y \times_{S} S'$ the closed sub-prescheme
of $X'$ defined by $\mathfrak{J}' = p*(\mathfrak{J}) \mathcal{O}_{X'}$, $\mathcal{F}' = p*(\mathcal{F}) = \mathcal{F}
\otimes_{\mathcal{O}_{S}} \mathcal{O}_{S'}$; then, if $W' = p^{-1}(W)$, one has
$gr^{\bullet}_{\mathfrak{J}'}(\mathcal{F}') | W' = p*(gr^{\bullet}_{\mathfrak{J}}(\mathcal{F})) | W'$, and
$gr^{\bullet}_{\mathfrak{J}'}(\mathcal{F}')$ is a flat $(\mathcal{O}_{X'}/\mathfrak{J}')$-Module at the points of $W'$.*

The questions being local on $X$ and $S$, one may suppose that $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine, $B$ being an $A$-algebra of finite presentation, and $\mathcal{F} = \tilde{M}$,
where $M$ is a $B$-module of finite presentation, $\mathfrak{J} = \tilde{\mathfrak{J}}$, where $\mathfrak{J}$ is an
ideal of finite type of $B$; by virtue of `(8.9.1)` and `(8.5.11)`, there exists a Noetherian sub-ring `A_0` of $A$, an
`A_0`-algebra of finite type `B_0` such that $B = B_{0} \otimes_{A_{0}} A$, an ideal $\mathfrak{J}_{0}$ of `B_0` such
that $\mathfrak{J} = \mathfrak{J}_{0} B$, a `B_0`-module of finite type `M_0` such that $M = M_{0} \otimes_{A_{0}} A =
M_{0} \otimes_{B_{0}} B$. Moreover, $A$ is the inductive limit of its sub-`A_0`-algebras of finite type $A_{\lambda}$;
one sets $B_{\lambda} = B_{0} \otimes_{A_{0}} A_{\lambda}$, $M_{\lambda} = M_{0} \otimes_{A_{0}} A_{\lambda} = M_{0}
\otimes_{B_{0}} B_{\lambda}$, $\mathfrak{J}_{\lambda} = \mathfrak{J}_{0} B_{\lambda}$, so that $B = \lim B_{\lambda}$,
$M = \lim M_{\lambda}$. This being so, by hypothesis $gr^{\bullet}_{\mathfrak{J}}(M)$ is a flat $A$-module; hence it
follows from `(11.2.9)` that there exists a $\lambda$ such that $gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ is
a flat $A_{\lambda}$-module. To prove that $\mathcal{F}$ is $f$-flat at the points of $Y$, one may therefore confine
oneself to the case where $S$ is Noetherian; but then $(0_{I}, 6.1.2)$, applied by induction on $n$, proves that the
$\mathcal{F}/\mathfrak{J}^{n+1} \mathcal{F}$ are $f$-flat, and one concludes by $(0_{III}, 10.2.6)$.

The proof of (ii) reduces in the same way to the case where $S$ is Noetherian,

<!-- original page 134 -->

using `(11.2.9)`; the conclusion is then evident, $gr^{\bullet}_{\mathfrak{J}}(B)$ being in this case a
$(B/\mathfrak{J})$-algebra of finite type and $gr^{\bullet}_{\mathfrak{J}}(M)$ a $gr^{\bullet}_{\mathfrak{J}}(B)$-module
of finite type.

To prove (iii), one reduces as in (i) to the case where $S$ and $X$ are affine; with the same notation, one may suppose,
by virtue of `(11.2.9)`, that $gr^{\bullet}_{\mathfrak{J}_{\lambda}}(B_{\lambda})$ and
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ are flat $A_{\lambda}$-modules and that one has
$gr^{\bullet}_{\mathfrak{J}}(B) = gr^{\bullet}_{\mathfrak{J}_{\lambda}}(B_{\lambda}) \otimes_{A_{\lambda}} A$ and
$gr^{\bullet}_{\mathfrak{J}}(M) = gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda}) \otimes_{A_{\lambda}} A$.
Consequently $gr^{\bullet}_{\mathfrak{J}}(B)$ is a $(B/\mathfrak{J})$-algebra of finite presentation and
$gr^{\bullet}_{\mathfrak{J}}(M)$ a $gr^{\bullet}_{\mathfrak{J}}(B)$-module of finite presentation. If $W_{m}$ is the set
of $\mathfrak{p} \in \operatorname{Spec}(B/\mathfrak{J})$ such that $gr^{m}_{\mathfrak{J}}(M)_{\mathfrak{p}}$ is a flat
$(B/\mathfrak{J})$-module, $W_{m}$ is open in $\operatorname{Spec}(B/\mathfrak{J})$ `(11.3.1)` and one has $W =
\bigcap_{m} W_{m}$, hence $W$ is stable under generization. Assertion (iii) then follows from `(11.3.2)` applied by
taking $X = \operatorname{Spec}(gr^{\bullet}_{\mathfrak{J}}(B))$, $Y = Z = \operatorname{Spec}(B/\mathfrak{J})$ and
$\mathcal{F} = (gr^{\bullet}_{\mathfrak{J}}(M))~$.

Finally, (iv) follows at once from `(11.2.9.2)`.

Generalizing the definition of `(6.10.1)`, one says that for a prescheme $X$, a closed sub-prescheme $Y$ of $X$ defined
by a quasi-coherent Ideal $\mathfrak{J}$ of $\mathcal{O}_{X}$, and a quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$, $\mathcal{F}$ is **normally flat along $Y$ at a point** $y$ if
$(gr^{\bullet}_{\mathfrak{J}}(\mathcal{F}))_{y}$ is a flat $\mathcal{O}_{Y, y}$-module. One says that $\mathcal{F}$ is
**normally flat along $Y$** if it is so at every point of $Y$.

**Corollary (11.3.5).**

<!-- label: IV.11.3.5 -->

*Under the general hypotheses of `(11.3.4)`, suppose that $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ and
$gr^{\bullet}_{\mathfrak{J}}(\mathcal{F})$ are $f$-flat. Then the set $W$ of $y \in Y$ such that $\mathcal{F}$ is
normally flat along $Y$ at the point $y$ is open in $Y$, and (with the notation of `(11.3.4, (iv))`) $\mathcal{F}'$ is
normally flat along $Y'$ at all points of $W' = p^{-1}(W)$.*

**Proposition (11.3.6).**

<!-- label: IV.11.3.6 -->

*The notation being that of `(8.5.1)` and `(8.8.1)`, suppose $S_{\alpha}$ quasi-compact, $X_{\alpha}$ of finite
presentation over $S_{\alpha}$, $Y_{\alpha}$ a closed sub-prescheme of $X_{\alpha}$ defined by a quasi-coherent Ideal
$\mathfrak{J}_{\alpha}$ of finite type of $\mathcal{O}_{X_{\alpha}}$ such that
$gr^{\bullet}_{\mathfrak{J}_{\alpha}}(\mathcal{O}_{X_{\alpha}})$ is flat over $S_{\alpha}$; finally suppose that
$\mathcal{F}_{\alpha}$ is an $\mathcal{O}_{X_{\alpha}}$-Module of finite presentation. For $\mathcal{F}$ to be normally
flat along $Y$, it is necessary and sufficient that there exist $\lambda$ such that $\mathcal{F}_{\lambda}$ is normally
flat along $Y_{\lambda}$.*

Note that $Y$ (resp. $Y_{\lambda}$) is the closed sub-prescheme of $X$ (resp. $X_{\lambda}$) defined by $\mathfrak{J} =
\mathfrak{J}_{\alpha} \mathcal{O}_{X}$ (resp. $\mathfrak{J}_{\lambda} = \mathfrak{J}_{\alpha}
\mathcal{O}_{X_{\lambda}}$); by virtue of the hypothesis and of `(11.2.9.2)`, one has
$gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X}) = gr^{\bullet}_{\mathfrak{J}_{\alpha}}(\mathcal{O}_{X_{\alpha}})
\otimes_{\mathcal{O}_{S_{\alpha}}} \mathcal{O}_{S}$ and
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{O}_{X_{\lambda}}) =
gr^{\bullet}_{\mathfrak{J}_{\alpha}}(\mathcal{O}_{X_{\alpha}}) \otimes_{\mathcal{O}_{S_{\alpha}}}
\mathcal{O}_{S_{\lambda}}$ for $\lambda \geq \alpha$, and $gr^{\bullet}_{\mathfrak{J}}(\mathcal{O}_{X})$ (resp.
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{O}_{X_{\lambda}})$) is flat over $S$ (resp. $S_{\lambda}$), which
entails that $Y$ is flat over $S$ (resp. $Y_{\lambda}$ flat over $S_{\lambda}$). If $\mathcal{F}_{\lambda}$ is normally
flat along $Y_{\lambda}$, $gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{F}_{\lambda}) | Y_{\lambda}$ is flat over
$Y_{\lambda}$, hence also over $S_{\lambda}$, and since
$(gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{F}_{\lambda}))_{x_{\lambda}} = 0$ for $x_{\lambda} \notin Y_{\lambda}$,
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{F}_{\lambda})$ is flat over $S_{\lambda}$. One concludes `(11.2.9.2)`
that $gr^{\bullet}_{\mathfrak{J}}(\mathcal{F}) = gr^{\bullet}_{\mathfrak{J}_{\lambda}}(\mathcal{F}_{\lambda})
\otimes_{\mathcal{O}_{S_{\lambda}}} \mathcal{O}_{S}$, hence $\mathcal{F}$ is normally flat along $Y$. To prove the
converse, one may suppose that $S_{\alpha}$ and $X_{\alpha}$ are affine and adopt the notation of `(11.2.9)`; since
$gr^{\bullet}_{\mathfrak{J}}(B)$ is a flat $A$-module, so is $gr^{\bullet}_{\mathfrak{J}}(M)$, hence, by virtue of
`(11.2.9)`, there exists $\lambda \geq \alpha$ such that $gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ is a flat
$A_{\lambda}$-module, whence $gr^{\bullet}_{\mathfrak{J}}(M) = gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})
\otimes_{A_{\lambda}} A$. Moreover `(11.3.4, (ii))`, $gr^{\bullet}_{\mathfrak{J}_{\lambda}}(M_{\lambda})$ is a
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(B_{\lambda})$-module of finite presentation and
$gr^{\bullet}_{\mathfrak{J}_{\lambda}}(B_{\lambda})$ a $(B_{\lambda}/\mathfrak{J}_{\lambda})$-algebra of finite
presentation. The conclusion then follows from `(11.2.6)`.

<!-- original page 135 -->

**Proposition (11.3.7).**

<!-- label: IV.11.3.7 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$, $\mathcal{F}'$ two quasi-coherent
$\mathcal{O}_{X}$-Modules of finite presentation, $u : \mathcal{F}' \to \mathcal{F}$ an $\mathcal{O}_{X}$-homomorphism,
$x$ a point of $X$ and $y = f(x)$; suppose that $\mathcal{F}$ is $f$-flat at the point $x$. The following conditions are
then equivalent:*

*a) One has $(Ker u)_{x} = 0$ and `Coker u` is an $\mathcal{O}_{X}$-Module $f$-flat at the point $x$.*

*b) The homomorphism $(u \otimes 1)_{x} : (\mathcal{F}' \otimes_{\mathcal{O}_{Y}} k(y))_{x} \to (\mathcal{F}
\otimes_{\mathcal{O}_{Y}} k(y))_{x}$ is injective.*

*If moreover $\mathcal{F}'$ is $f$-flat, the set of points $x$ verifying the preceding equivalent conditions is open in
$X$.*

Condition a) entails b) by virtue of $(0_{I}, 6.1.2)$, without hypothesis on $\mathcal{F}'$. To prove the converse, one
may confine oneself to the case where $X$ and $Y$ are affine, then, by virtue of `(8.9.1)` and `(11.2.7)`, suppose that
one has $X = X_{0} \times_{Y_{0}} Y$, $f = f_{0} \times 1$, $\mathcal{F} = \mathcal{F}_{0} \otimes_{\mathcal{O}_{Y_{0}}}
\mathcal{O}_{Y}$, $\mathcal{F}' = \mathcal{F}'_{0} \otimes_{\mathcal{O}_{Y_{0}}} \mathcal{O}_{Y}$, $u = u_{0} \otimes
1_{Y}$, where `Y_0` is Noetherian, $f_{0} : X_{0} \to Y_{0}$ a morphism of finite type, $\mathcal{F}_{0}$,
$\mathcal{F}'_{0}$ two coherent $\mathcal{O}_{X_{0}}$-Modules, $u_{0} : \mathcal{F}'_{0} \to \mathcal{F}_{0}$ a
homomorphism; moreover, if $x_{0}$ is the projection of $x$ in `X_0`, one may suppose that $\mathcal{F}_{0}$ is
$f_{0}$-flat at the point $x_{0}$. Set $y_{0} = f_{0}(x_{0})$; by virtue of the transitivity of fibres `(I, 3.6.4)`, the
projection morphism $f^{-1}(y) \to f^{-1}_{0}(y_{0})$ is faithfully flat `(2.2.13)`, and since $(u \otimes 1)_{x} =
((u_{0} \otimes 1)_{x_{0}}) \otimes 1_{k(y)}$, the hypothesis that $(u \otimes 1)_{x}$ is injective entails that the
same is true of $(u_{0} \otimes 1)_{x_{0}}$ `(2.2.7)`. Now this entails, by $(0_{III}, 10.2.4)$ applied to the local
Noetherian rings $\mathcal{O}_{y_{0}}$ and $\mathcal{O}_{x_{0}}$ and to the $\mathcal{O}_{y_{0}}$-modules
$(\mathcal{F}'_{0})_{x_{0}}$ and $(\mathcal{F}_{0})_{x_{0}}$ (of which the second is flat over $\mathcal{O}_{y_{0}}$),
that one has $(Ker u_{0})_{x_{0}} = 0$ and that $Coker u_{0}$ is $f_{0}$-flat at the point $x_{0}$. One deduces from
this first of all that `Coker u` is $f$-flat at the point $x$ `(2.1.4)`; by virtue of the right exactness of the tensor
product, one has moreover $Coker u = (Coker u_{0}) \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y}$; applying then $(0_{I},
6.1.2)$ to the sequence (exact by hypothesis)

```text
  0 → Ker u_0 → ℱ'_0 → ℱ_0 → Coker u_0 → 0,
```

one deduces from this that $u_{x}$ is an injective homomorphism.

Finally, it follows from `(11.1.2)` that the set `U_0` of points $x_{0} \in X_{0}$ such that the morphism $(u_{0}
\otimes 1)_{x_{0}}$ is injective is open; by flatness one deduces from this that for every $x \in X$ above $x_{0} \in
U_{0}$ the morphism $(u \otimes 1)_{x}$ is injective, hence the set of these points contains the inverse image $U$ of
`U_0` in $X$ and is consequently a neighbourhood of $x$, which finishes the proof.

**Theorem (11.3.8).**

<!-- label: IV.11.3.8 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation, $(g_{i})_{1 \leq i \leq n}$ a sequence of sections of $\mathcal{O}_{X}$ over $X$; set
$\mathcal{F}_{i} = \mathcal{F}/(\sum_{j \leq i} g_{j} \mathcal{F})$ for $0 \leq i \leq n$ (with $\mathcal{F}_{0} =
\mathcal{F}$). Let $x$ be a point of $X$, $y = f(x)$, and set $X_{y} = f^{-1}(y) = X \times_{Y}
\operatorname{Spec}(k(y))$, $\mathcal{F}_{y} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} k(y)$, which is an
$\mathcal{O}_{X_{y}}$-Module. Suppose that the $(g_{i})_{x}$ belong to the maximal ideal $\mathfrak{m}_{x}$. The
following conditions are equivalent:*

*a) The sequence $((g_{i})_{x})$ is $\mathcal{F}_{y}$-regular and the $\mathcal{F}_{i}$ ($0 \leq i \leq n$) are $f$-flat
at the point $x$.*

*b) The sequence $((g_{i})_{x})$ is $\mathcal{F}_{x}$-regular and $\mathcal{F}_{n}$ is $f$-flat at the point $x$.*

*b') There exists a neighbourhood $U$ of $x$ such that the sequence $(g_{i} | U)$ is $(\mathcal{F} | U)$-quasi-regular,
and $\mathcal{F}_{n}$ is $f$-flat at the point $x$.*

<!-- original page 136 -->

*c) $\mathcal{F}$ is $f$-flat at the point $x$, and the sequence $((g_{i} \otimes 1)_{x})$ of elements of
$\mathcal{O}_{X_{y}, x}$ images of the $(g_{i})_{x}$ is $(\mathcal{F}_{y})_{x}$-regular.*

*d) $\mathcal{F}$ is $f$-flat at the point $x$, and for every morphism $Y' \to Y$ and every point $x' \in X' = X
\times_{Y} Y'$ above $x$, if one sets $\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$, the sequence $(g_{i} \otimes 1)_{x'}$
of elements of $\mathcal{O}_{X', x'}$ is $\mathcal{F}'_{x'}$-regular.*

*Moreover the set of $x \in X$ verifying these conditions is open in the set $Z$ of $x$ such that $g_{i}(x) = 0$ for
every $i$.*

The fact that a) entails d) follows at once from `(0, 15.1.15)`, and c) is a particular case of d); moreover, a) implies
b) trivially. Let us show that b) or c) entails a). The $\mathcal{F}_{i}$ are of finite presentation; the fact that c)
implies a) then follows at once from `(11.3.7)` by induction on $n$, and this also shows that the set of $x \in X$
verifying c) is open in $Z$. To show that b) entails a), one is at once reduced, by induction on $n$, to the case $n =
1$; we shall write $g$ instead of $g_{1}$. The question being local on $X$ and $Y$, one may suppose $Y =
\operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ affine, $B$ being an $A$-algebra of finite presentation,
$\mathcal{F} = \tilde{M}$, where $M$ is a $B$-module of finite presentation. One can then `(8.9.1)` write $B = B_{0}
\otimes_{A_{0}} A$, $M = M_{0} \otimes_{A_{0}} A$, where `A_0` is a Noetherian sub-ring of $A$, `B_0` an `A_0`-algebra
of finite type and `M_0` a `B_0`-module of finite type. Moreover $A$ is the filtered inductive limit of its sub-rings
$A_{\lambda}$ which are `A_0`-algebras of finite type (hence Noetherian), and if one sets $B_{\lambda} = B_{0}
\otimes_{A_{0}} A_{\lambda}$, $M_{\lambda} = M_{0} \otimes_{A_{0}} A_{\lambda}$, $B_{\lambda}$ is an
$A_{\lambda}$-algebra of finite type, $M_{\lambda}$ a $B_{\lambda}$-module of finite type and one has $B = \lim
B_{\lambda}$, $M = \lim M_{\lambda}$. There exists therefore an index $\lambda$ and an element $g_{\lambda} \in
B_{\lambda}$ such that $g = g_{\lambda} \otimes 1$; returning to geometric notation and setting $Y_{\lambda} =
\operatorname{Spec}(A_{\lambda})$, $X_{\lambda} = \operatorname{Spec}(B_{\lambda})$ and $\mathcal{F}_{\lambda} =
\tilde{M}_{\lambda}$, it will suffice to prove that there is a $\mu \geq \lambda$ such that at the point $x_{\mu} \in
X_{\mu}$ projection of $x$, $(g_{\mu})_{x_{\mu}}$ is $(\mathcal{F}_{\mu})_{x_{\mu}}$-regular and
$\mathcal{F}_{\mu}/g_{\mu} \mathcal{F}_{\mu}$ flat over $Y_{\mu}$ at the point $x_{\mu}$. One will deduce in effect, by
`(0, 15.1.16)`, that $\mathcal{F}_{\mu}$ is flat over $Y_{\mu}$ at the point $x_{\mu}$, hence $\mathcal{F}$ flat over
$Y$ at the point $x$.

The fact that b) entails a) will thus follow from the following proposition:

**Proposition (11.3.9).**

<!-- label: IV.11.3.9 -->

*The general notation and hypotheses being those of `(8.5.1)` and `(8.8.1)`, suppose that $f_{\alpha} : X_{\alpha} \to
Y_{\alpha}$ is a morphism locally of finite presentation. Let $\mathcal{F}_{\alpha}$, $\mathcal{G}_{\alpha}$ be two
quasi-coherent $\mathcal{O}_{X_{\alpha}}$-Modules of finite presentation, $h_{\alpha} : \mathcal{F}_{\alpha} \to
\mathcal{G}_{\alpha}$ an $\mathcal{O}_{X_{\alpha}}$-homomorphism, $\mathcal{H}_{\alpha}$ its cokernel. Let finally $x$
be a point of $X$, $x_{\lambda}$ its projection in $X_{\lambda}$ for $\lambda \geq \alpha$. For $h_{x}$ to be injective
and $\mathcal{H} = Coker h$ to be $f$-flat at the point $x$, it is necessary and sufficient that there exist $\lambda
\geq \alpha$ such that $(h_{\lambda})_{x_{\lambda}}$ is injective and $\mathcal{H}_{\lambda} = Coker h_{\lambda}$ is
$f_{\lambda}$-flat at the point $x_{\lambda}$. Moreover, the set of $x \in X$ having the preceding properties is open in
$X$.*

Recall that by virtue of the right exactness of the tensor product, one has $\mathcal{H}_{\mu} = v^{*}_{\mu
\lambda}(\mathcal{H}_{\lambda})$ for $\lambda \leq \mu$ and $\mathcal{H} = v^{*}_{\lambda}(\mathcal{H}_{\lambda})$,
which justifies the notation.

The sufficiency of the condition comes from the fact that, if the sequence

$$ 0 \to \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda} \to \mathcal{H}_{\lambda} \to 0 $$

is exact and $(\mathcal{G}_{\lambda})_{x_{\lambda}}$ a flat $\mathcal{O}_{Y_{\lambda}, y_{\lambda}}$-module,
$\mathcal{H}_{x}$ is a flat $\mathcal{O}_{Y, y}$-module by base change `(2.1.4)` and the sequence $0 \to \mathcal{F}_{x}
\to \mathcal{G}_{x} \to \mathcal{H}_{x} \to 0$ is exact `(2.1.8)`. To prove

<!-- original page 137 -->

that the condition is necessary, note that $\mathcal{H}$ is of finite presentation; the question being local on $X$, one
may suppose $X$ and $Y$ affine, and, by virtue of `(11.3.1)`, suppose that $\mathcal{H}$ is $f$-flat. Let us now note
the

**Lemma (11.3.9.1).**

<!-- label: IV.11.3.9.1 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{G}$, $\mathcal{H}$ two quasi-coherent
$\mathcal{O}_{X}$-Modules of finite presentation such that $\mathcal{H}$ is $f$-flat, $p : \mathcal{G} \to \mathcal{H}$
a surjective homomorphism. Then $Ker(p)$ is an $\mathcal{O}_{X}$-Module of finite presentation.*

Indeed, one may suppose $X$, $Y$ affine, and that there exists a morphism $Y \to Y_{0}$ where `Y_0` is Noetherian, a
morphism $f_{0} : X_{0} \to Y_{0}$ of finite type such that $X = X_{0} \times_{Y_{0}} Y$, $f = (f_{0})_{(Y)}$, two
coherent $\mathcal{O}_{X_{0}}$-Modules $\mathcal{G}_{0}$, $\mathcal{H}_{0}$ and a homomorphism $p_{0} : \mathcal{G}_{0}
\to \mathcal{H}_{0}$ such that $\mathcal{G}$, $\mathcal{H}$ and $p$ are deduced from $\mathcal{G}_{0}$,
$\mathcal{H}_{0}$ and $p_{0}$ by base change `(8.9.1 and 8.5.2)`. Moreover, one may suppose $p_{0}$ surjective `(8.5.7)`
and $\mathcal{H}_{0}$ $f_{0}$-flat `(11.2.7)`. Then, if $\mathcal{K}_{0} = Ker(p_{0})$, $\mathcal{K}_{0}$ is a coherent
$\mathcal{O}_{X_{0}}$-Module $(0_{I}, 5.3.4)$ and by virtue of $(0_{I}, 6.1.2)$, $\mathcal{K} = Ker(p)$ is deduced from
$\mathcal{K}_{0}$ by base change, hence is of finite presentation.

This lemma being proved, set $\mathcal{K} = Ker(\mathcal{G} \to \mathcal{H})$, which is therefore of finite
presentation. One has a canonical homomorphism $q : \mathcal{K} \to \mathcal{F}$, and by hypothesis $q_{x} :
\mathcal{K}_{x} \to \mathcal{F}_{x}$ is an isomorphism; consequently $(0_{I}, 5.2.7)$ there exists a neighbourhood $U$
of $x$ such that $q | U$ is an isomorphism, and on restricting $X$, one may suppose that the sequence

$$ 0 \to \mathcal{K} \to \mathcal{G} \to \mathcal{H} \to 0 $$

is exact. This being so, it follows from `(11.2.6)` that for $\lambda$ large enough, $\mathcal{H}_{\lambda}$ is a flat
$\mathcal{O}_{X_{\lambda}}$-module; set $\mathcal{K}_{\lambda} = Ker(\mathcal{G}_{\lambda} \to \mathcal{H}_{\lambda})$
and $\mathcal{K}'_{\lambda} = v^{*}_{\lambda}(\mathcal{K}_{\lambda})$. For $\mu \geq \lambda$ it follows from $(0_{I},
6.1.2)$ that one has $\mathcal{K}_{\mu} = Ker(\mathcal{G}_{\mu} \to \mathcal{H}_{\mu})$ and $\mathcal{K} =
v^{*}_{\lambda}(\mathcal{K}_{\lambda}) = Ker(\mathcal{G} \to \mathcal{H}) = \mathcal{K}$. One has on the other hand for
every $\mu \geq \lambda$ a canonical homomorphism $q_{\mu} : \mathcal{K}_{\mu} \to \mathcal{F}_{\mu}$, with
$\mathcal{K}_{\mu} = v^{*}_{\mu \lambda}(\mathcal{K}_{\lambda})$ for $\lambda \leq \mu$, and $q = v^{*}_{\mu}(q_{\mu})$.
Since $q$ is an isomorphism, it follows from `(8.5.2.4)` and `(11.3.9.1)` that there exists $\mu \geq \lambda$ such that
$q_{\mu}$ is an isomorphism, and consequently $u_{\mu} : \mathcal{F}_{\mu} \to \mathcal{G}_{\mu}$ an injective
homomorphism.

Let us return to the proof of `(11.3.8)`.

Since the set of $x \in X$ verifying b) is open in $X$, it is clear that b) entails b'). Let us finally show that b')
entails c). In the first place, $\mathcal{F}_{n}$ is $f$-flat in a neighbourhood of $x$ `(11.3.1)`, and one may
therefore confine oneself to the case where $U = X$ and where $\mathcal{F}_{n}$ is $f$-flat. Since by definition
$gr^{\bullet}_{\mathfrak{F}}(\mathcal{F})$ is isomorphic to $\mathcal{F}_{n} \otimes_{\mathcal{O}_{Y}}
\mathcal{O}_{Y}[T_{1}, \cdots, T_{n}]$ `(0, 15.2.2)`, it is $f$-flat, and one concludes by `(11.3.4, (i))` that
$\mathcal{F}$ itself is $f$-flat in a neighbourhood of $x$. On the other hand, if $(\mathfrak{F}_{y})_{x}$ is the ideal
of $\mathcal{O}_{X_{y}, x}$ generated by the $(g_{i} \otimes 1)_{x}$, it follows from `(11.2.9.2)` that, in the diagram

```text
  (ℱ_y)_x[T_1, …, T_n] / ((𝔉_y)_x[T_1, …, T_n])  ──→  gr_{(𝔉_y)_x}^•((ℱ_y)_x)
                ‖                                              ‖
              (gr_𝔉^•(ℱ))_x ⊗_{𝒪_Y} k(y)        ──→        ((gr_𝔉^•(ℱ)) ⊗_{𝒪_Y} k(y))_x
```

<!-- original page 138 -->

the vertical arrows are isomorphisms; since the first row is an isomorphism, so is the second, hence the sequence
$((g_{i} \otimes 1)_{x})$ is $(\mathcal{F}_{y})_{x}$-quasi-regular, and consequently also
$(\mathcal{F}_{y})_{x}$-regular, since $X_{y}$ is locally of finite type over $k(y)$. Q.E.D.

**Theorem (11.3.10) (fibrewise flatness criterion).**

<!-- label: IV.11.3.10 -->

*Let $S$ be a prescheme, $g : X \to S$, $h : Y \to S$ two morphisms, $f : X \to Y$ an $S$-morphism, $\mathcal{F}$ a
quasi-coherent $\mathcal{O}_{X}$-Module, $x$ a point of $X$, $y = f(x)$, $s = h(y) = g(x)$. Suppose one of the following
two hypotheses verified:*

*1° $S$, $X$ and $Y$ are locally Noetherian and $\mathcal{F}$ is coherent.*

*2° $g$ and $h$ are locally of finite presentation and $\mathcal{F}$ is of finite presentation.*

*Then, with the notation of `(9.4.1)`, if $\mathcal{F}_{s} \neq 0$, the following conditions are equivalent:*

*a) $\mathcal{F}$ is $g$-flat at the point $x$ and $\mathcal{F}_{s}$ is $f_{s}$-flat at the point $x$.*

*b) $h$ is flat at the point $y$ and $\mathcal{F}$ is $f$-flat at the point $x$.*

*Moreover, under hypothesis 2°, the set of $x \in X$ verifying condition b) is open in $X$.*

The last assertion follows from `(11.3.1)` applied to $\mathcal{O}_{Y}$ and the morphism $h$ on the one hand, and to
$\mathcal{F}$ and the morphism $f$ (which is locally of finite presentation) on the other.

Since $g = h \circ f$, it is clear that b) implies a) without supposing 1° or 2° `(2.1.6 and 2.1.4)`. To prove that a)
entails b), one may confine oneself to the case where $S$, $X$ and $Y$ are affine; under hypothesis 2°, applying
`(11.2.7)`, one reduces to the case where in addition $S$ is Noetherian, that is, one may confine oneself to considering
the case where hypothesis 1° is satisfied. Then the assertion is equivalent to the following lemma, which improves
$(0_{III}, 10.2.5)$:

**Lemma (11.3.10.1).**

<!-- label: IV.11.3.10.1 -->

*Let $\rho : A \to B$, $\sigma : B \to C$ be local homomorphisms of Noetherian local rings, $k$ the residue field of
$A$, $M$ a $C$-module $\neq 0$ of finite type. The following conditions are equivalent:*

*a) $M$ is a flat $A$-module and $M \otimes_{A} k$ is a flat $(B \otimes_{A} k)$-module.*

*b) $B$ is a flat $A$-module and $M$ is a flat $B$-module.*

We shall first establish the following more general lemma:

**Lemma (11.3.10.2).**

<!-- label: IV.11.3.10.2 -->

*Let $A$ be a commutative ring, $B$ a commutative $A$-algebra, $\mathfrak{J}$ an ideal of $A$, $M$ a $B$-module.
Consider on the one hand the following conditions:*

*(i) $\mathfrak{J}$ is nilpotent.*

*(ii) $B$ is Noetherian and $M$ is ideally separated for the $\mathfrak{J} B$-preadic topology $(0_{III}, 10.2.1)$.*

*(iii) $\mathfrak{J} B$ is contained in the radical of $B$.*

*Consider on the other hand the four properties:*

*a) $M$ is a flat $B$-module.*

*b) $B$ is a flat $A$-module.*

*c) $M$ is a flat $A$-module and $M/\mathfrak{J} M$ a flat $(B/\mathfrak{J} B)$-module.*

*d) $B/\mathfrak{J} B$ is a flat $(A/\mathfrak{J})$-module and for every maximal ideal $\mathfrak{m} \supset
\mathfrak{J} B$ of $B$ one has $\mathfrak{m} M \neq M$.*

*Then:*

*1° If one of the conditions (i), (ii) is verified, the conjunction of a) and b) implies c), and c) implies a).*

<!-- original page 139 -->

*2° If condition (i) or the conjunction of (ii) and (iii) is verified, the conjunction of c) and d) implies the
conjunction of a) and b).*

*1°* The first assertion is immediate $(0_{I}, 6.2.1)$. Suppose then c) verified, and let us prove a). Consider the
graded rings $gr^{\bullet}_{\mathfrak{J}}(A)$, $gr^{\bullet}_{\mathfrak{J}}(B)$ and the graded module
$gr^{\bullet}_{\mathfrak{J}}(M)$ (at the same time over $gr^{\bullet}_{\mathfrak{J}}(A)$ and
$gr^{\bullet}_{\mathfrak{J}}(B)$) relative to the $\mathfrak{J}$-preadic filtrations, as well as the canonical
surjective maps $(0_{III}, 10.1.1.2)$

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

Hypothesis c) entails that $v$ is bijective $(0_{III}, 10.2.1)$; since the two other maps of the diagram are surjective,
they are also bijective. But since by virtue of hypothesis c), $M/\mathfrak{J} M$ is a flat $(B/\mathfrak{J} B)$-module,
it follows from $(0_{III}, 10.2.1)$ that $M$ is a flat $B$-module.

*2°* One or the other of conditions (i), (iii) implies that every maximal ideal of $B$ contains $\mathfrak{J} B$. It
therefore follows from 1° and from the conjunction of c) and d) that $M$ is a faithfully flat $B$-module, and
consequently $gr^{0}_{\mathfrak{J}}(M)$ a faithfully flat $gr^{0}_{\mathfrak{J}}(B)$-module $(0_{I}, 6.2.1)$. One has
seen in 1° that hypothesis c) entails that the three maps of the diagram `(11.3.10.3)` are bijective; the fact that
$gr^{0}_{\mathfrak{J}}(M)$ is a faithfully flat $gr^{0}_{\mathfrak{J}}(B)$-module therefore implies that $u$ is also
bijective $(0_{I}, 6.4.1)$. On the other hand, conditions (ii) and (iii) imply that $B$ is an $A$-module ideally
separated for the $\mathfrak{J}$-preadic filtration *(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop. 2)*; one
therefore deduces again from $(0_{III}, 10.2.1)$ that if condition (i), or the conjunction of (ii) and (iii), is
verified, $B$ is a flat $A$-module.

*(11.3.10.4)* Lemma `(11.3.10.2)` being established, one deduces from it `(11.3.10.1)` by taking for $\mathfrak{J}$ the
maximal ideal of $A$, and noting that conditions (ii) and (iii) of `(11.3.10.2)` are then satisfied *(Bourbaki, Alg.
comm., chap. III, §5, n° 4, prop. 2)*. This also finishes the proof of `(11.3.7)`.

**Corollary (11.3.11).**

<!-- label: IV.11.3.11 -->

*Let $g : X \to S$, $h : Y \to S$ be two morphisms locally of finite presentation, $f : X \to Y$ an $S$-morphism. The
following conditions are equivalent:*

*a) $g$ is flat and $f_{s} : X_{s} \to Y_{s}$ is flat for every $s \in S$.*

*b) $h$ is flat at all points of $f(X)$ and $f$ is flat.*

It suffices to apply `(11.3.10)` for $\mathcal{F} = \mathcal{O}_{X}$.

**Remark (11.3.12).**

<!-- label: IV.11.3.12 -->

It would be interesting to be able to give to `(11.3.2)` and `(11.3.10)` proofs not using passage to the inductive
limit; for this it would suffice to prove the following criterion:

\*Let $A$ be a ring, $B$ an $A$-algebra of finite presentation, $M$ a $B$-module of finite presentation, $\mathfrak{J}$
an

<!-- original page 140 -->

ideal of $A$, $\mathfrak{p}$ a prime ideal of $B$ containing $\mathfrak{J} B$. Then the following two conditions are
equivalent:\*

*a) $M_{\mathfrak{p}}$ is a flat $A$-module.*

*b) $M_{\mathfrak{p}}/\mathfrak{J} M_{\mathfrak{p}}$ is a flat $(A/\mathfrak{J})$-module and
$Tor^{A}_{1}(A/\mathfrak{J}, M_{\mathfrak{p}}) = 0$.*

When $A$ is Noetherian, this is a consequence of $(0_{III}, 10.2.2)$ applied to the Noetherian $A$-algebra $B$; can one
deduce the general statement from this by a passage to the inductive limit?

It is fitting to note in this connection that such a generalization is certainly not possible when one replaces
condition b) above by one of conditions c), d) of $(0_{III}, 10.2.1)$ where $M$ is replaced by $\tilde{M}$. Take for
example for $A$ a local ring whose maximal ideal $\mathfrak{J}$ is principal and such that the intersection
$\mathfrak{N} = \bigcap_{n \geq 0} \mathfrak{J}^{n+1}$ is not reduced to `0` (for example the ring of germs of
infinitely differentiable numerical functions in the neighbourhood of `0` in $\mathbb{R}$). Take $B = A$, $\mathfrak{p}
= \mathfrak{J}$, and $M = A/\mathfrak{N}$, where $\mathfrak{N}$ is a monogenic sub-module $\neq 0$ of $\mathfrak{N}$;
$M$ is therefore of finite presentation. It is clear that $M$ is not a flat $A$-module, for being of finite
presentation, it would be free *(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)*, which is absurd since
$\mathfrak{N} \neq 0$. However, $\mathfrak{J}^{k} M/\mathfrak{J}^{k+n} M$ is isomorphic to $A/\mathfrak{J}^{n}$ for any
positive $k$ and $n$, hence $M$ indeed verifies conditions c) and d) of $(0_{III}, 10.2.1)$ since $A/\mathfrak{J}$ is a
field.

**Proposition (11.3.13).**

<!-- label: IV.11.3.13 -->

*Let $f : X \to Y$ be a morphism of preschemes, $x$ a point of $X$ such that $f$ is flat at the point $x$; set $y =
f(x)$.*

*(i) If $X$ is reduced (resp. normal) at the point $x$, then $Y$ is reduced (resp. normal) at the point $y$.*

*(ii) Suppose in addition that $f$ is of finite presentation at the point $x$. Then, if $Y$ is reduced (resp. normal) at
the point $y$ and if the morphism $f$ is reduced (resp. normal) at the point $x$ `(6.8.1)`, $X$ is reduced (resp.
normal) at the point $x$.*

The first assertion is included only for the record, having been proved in `(2.1.13)`. To prove (ii), one may confine
oneself to the case where $X = \operatorname{Spec}(B)$, $Y = \operatorname{Spec}(A)$, with $A$ a local reduced (resp.
integral and integrally closed) ring and $B$ an $A$-algebra of finite presentation. One may then `(8.9.1)` write $B =
B_{0} \otimes_{A_{0}} A$, where `A_0` is a sub-$\mathbb{Z}$-algebra of finite type of $A$ and `B_0` an `A_0`-algebra of
finite type. Let $(C_{\alpha})$ be the filtered increasing family of sub-`A_0`-algebras of finite type of $A$, which are
therefore $\mathbb{Z}$-algebras of finite type; one has $A = \lim C_{\alpha}$. Let us now distinguish the two cases:

*1° Suppose $A$ reduced and $f$ reduced at the point $x$.* If $\mathfrak{m}$ is the maximal ideal of $A$, let
$\mathfrak{p}_{\alpha}$ be the prime ideal $\mathfrak{m} \cap C_{\alpha}$, and set $A'_{\alpha} =
(C_{\alpha})_{\mathfrak{p}_{\alpha}}$, so that one also has $A = \lim A'_{\alpha}$ `(5.13.3)`. Set $Y_{\alpha} =
\operatorname{Spec}(A'_{\alpha})$, $X_{\alpha} = \operatorname{Spec}(B_{0} \otimes_{A_{0}} A'_{\alpha})$ and let
$f_{\alpha} : X_{\alpha} \to Y_{\alpha}$, $x_{\alpha}$ (resp. $y_{\alpha}$) the projection of $x$ (resp. $y$) in
$X_{\alpha}$ (resp. $Y_{\alpha}$). Since $f$ is reduced at the point $x$, there exists $\alpha_{0}$ such that
$f_{\alpha}$ is reduced at the point $x_{\alpha}$ for $\alpha \geq \alpha_{0}$ (`(6.7.8)` and `(11.2.6)`); since
$Y_{\alpha}$ and $X_{\alpha}$ are Noetherian and $A'_{\alpha}$ is reduced (since this is the case for $C_{\alpha}$), one
deduces from `(3.3.5)` that $X_{\alpha}$ is reduced at the point $x_{\alpha}$. But since $B = \lim(B_{0} \otimes_{A_{0}}
A'_{\alpha})$, one also has $\mathcal{O}_{X, x} = \lim \mathcal{O}_{X_{\alpha}, x_{\alpha}}$ `(5.13.3)` and consequently
$\mathcal{O}_{X, x}$ is reduced `(5.13.2)`.

*2° Suppose $A$ integrally closed and $f$ normal at the point $x$.* Since $C_{\alpha}$ is universally Japanese
`(7.7.4)`, its integral closure $C'_{\alpha}$ is a finite $C_{\alpha}$-algebra, evidently contained in $A$. Let
$\mathfrak{p}'_{\alpha}$ be the prime ideal $\mathfrak{m} \cap C'_{\alpha}$ and set $A''_{\alpha} =
(C'_{\alpha})_{\mathfrak{p}'_{\alpha}}$, so that $A''_{\alpha}$ is a Noetherian integral integrally closed local ring,
and one has $A = \lim A''_{\alpha}$ `(5.13.3)`. Set $Y''_{\alpha} = \operatorname{Spec}(A''_{\alpha})$, $X''_{\alpha} =
\operatorname{Spec}(B_{0} \otimes_{A_{0}} A''_{\alpha})$ and let $f''_{\alpha} : X''_{\alpha} \to Y''_{\alpha}$,
$x''_{\alpha}$ (resp. $y''_{\alpha}$) the projection of $x$ (resp. $y$) in $X''_{\alpha}$ (resp. $Y''_{\alpha}$). Since
$f$ is normal at the point $x$, there exists $\alpha_{0}$ such that, for $\alpha \geq \alpha_{0}$, $f''_{\alpha}$ is
normal at the point $x''_{\alpha}$ (`(6.7.8)` and `(11.2.6)`);

<!-- original page 141 -->

since $X''_{\alpha}$ and $Y''_{\alpha}$ are Noetherian and $A''_{\alpha}$ is integrally closed, one deduces from
`(6.5.4)` that $X''_{\alpha}$ is normal at the point $x''_{\alpha}$. But the morphisms $\operatorname{Spec}(A''_{\beta})
\to \operatorname{Spec}(A''_{\alpha})$ for $\alpha \leq \beta$ are dominant, hence, since by virtue of `(11.3.1)` one
may suppose that the $f''_{\alpha}$ are flat for $\alpha \geq \alpha_{0}$, it follows from `(2.3.7)` that every
irreducible component of $X''_{\beta}$ dominates an irreducible component of $X''_{\alpha}$. One then concludes from
`(5.13.4)`, applied to the preschemes $\operatorname{Spec}(\mathcal{O}_{X_{0}, x_{0}} \otimes_{A_{0}} A''_{\alpha})$,
that $X$ is normal at the point $x$.

**Corollary (11.3.14).**

<!-- label: IV.11.3.14 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $x$ a point of $X$, $y = f(x)$. If $Y$ is geometrically
unibranch at the point $y$ `(6.15.1)` and if the morphism $f$ is normal at the point $x$ `(6.8.1)`, then $X$ is
geometrically unibranch at the point $x$.*

One may evidently confine oneself to the case where $Y = \operatorname{Spec}(A)$, $A$ being an integral local ring
geometrically unibranch, $y$ being the closed point of $Y$. Let $A'$ be the integral closure of $A$; set $Y' =
\operatorname{Spec}(A')$ and let $y'$ be the closed point of $Y'$, so that the morphism $g : Y' \to Y$ is radicial at
the point $y$ `(6.15.3)`, integral and birational. If one sets $X' = X \times_{Y} Y'$, and if $f' : X' \to Y'$ and $g' :
X' \to X$ are the projections, $g'$ is integral and radicial at the point $x$ `(6.15.3.1)`. Let then $x'$ be the unique
point of $g'^{-1}(x)$, which is above $y'$. The morphism $f'$ is of finite presentation and normal at the point $x'$
`(6.7.8)`, and consequently the local ring $\mathcal{O}_{X', x'}$ is integral and integrally closed `(11.3.13)`. On the
other hand, one may suppose $f$ flat `(11.3.1)`, hence $g'$ is a birational morphism `(6.15.4.1)`; consequently
$\operatorname{Spec}(\mathcal{O}_{X, x})$ is irreducible, and since $\mathcal{O}_{X, x}$ is reduced `(11.3.13)` it is
integral and geometrically unibranch by virtue of `(6.15.5)`.

**Proposition (11.3.15).**

<!-- label: IV.11.3.15 -->

*Let $A$ be a ring, $B$ an $A$-algebra of finite presentation, $M$ a $B$-module of finite presentation, which is a flat
$A$-module. Then there exists a finite sequence $(f_{i})_{1 \leq i \leq n}$ of elements of $A$ such that the ideal
generated by the $f_{i}$ is equal to $A$, and such that, for $0 \leq i < n$, $M_{f_{i+1}}/(\sum_{j \leq i} f_{j}
M_{f_{i+1}})$ is a free $(A_{f_{i+1}}/(\sum_{j \leq i} f_{j} A_{f_{i+1}}))$-module.*

One may also say that the $D(f_{i})$ form an open covering of $X = \operatorname{Spec}(A)$, and that if one sets $Z_{1}
= D(f_{1})$, then, by induction, $Z_{i+1} = D(f_{i+1}) \cap V(f_{1} A + \cdots + f_{i} A)$, the $Z_{i}$ form a partition
of $X$ into locally closed sets, $A_{f_{i+1}}/(\sum_{j \leq i} f_{j} A_{f_{i+1}})$ being the ring of an affine
sub-scheme of $X$ having $Z_{i+1}$ for underlying space.

To prove the proposition, one may first, by virtue of `(11.2.7)`, suppose that there exists a Noetherian sub-ring `A_0`
of $A$, an `A_0`-algebra of finite type `B_0` and a `B_0`-module of finite type `M_0`, flat over `A_0` and such that $B
= B_{0} \otimes_{A_{0}} A$, $M = M_{0} \otimes_{A_{0}} A$; it is clear that it will suffice to prove the proposition for
`A_0`, `B_0` and `M_0`, for if the elements $f_{i} \in A_{0}$ verify in this case the conditions of the statement, they
will also verify them for $A$, $B$, $M$, since $M_{f_{i+1}}/(\sum_{j \leq i} f_{j} M_{f_{i+1}}) =
((M_{0})_{f_{i+1}}/(\sum_{j \leq i} f_{j} (M_{0})_{f_{i+1}})) \otimes_{A_{0}} A$ *(Bourbaki, Alg. comm., chap. II, §2,
n° 7, prop. 18)*. One may therefore from now on confine oneself to the case where $A$ is Noetherian.

Let us now note that if $C$ is a Noetherian ring, $\mathfrak{N}$ its nilradical and $P$ a flat $C$-module, then it
follows from $(0_{III}, 10.1.2)$ that for $P$ to be a free $C$-module,

<!-- original page 142 -->

it is necessary and sufficient that $P \otimes_{C} (C/\mathfrak{N})$ be a free $(C/\mathfrak{N})$-module. Note on the
other hand that if $C$ is a Noetherian reduced ring, there exists $g \in C$ such that $C_{g}$ is an integral ring. Let
us now use lemma `(6.9.2)`: one can define by induction a sequence $(f_{i})_{i \geq 1}$ of elements of $A$ in the
following way:

1° $f_{1}$ is such that $A^{1} = (A_{red})_{f_{1}}$ is integral and $M \otimes_{A} A^{1}$ a free $A^{1}$-module;

2° if the ideal $\mathfrak{J}_{i}$ generated by $f_{1}, \cdots, f_{i}$ is $A$, $f_{i+1} = f_{i}$;

3° if on the contrary $\mathfrak{J}_{i} \neq A$, $f_{i+1}$ is an element not belonging to $\mathfrak{J}_{i}$ such that
$A^{i+1} = ((A/\mathfrak{J}_{i})_{red})_{f_{i+1}}$ is integral and $M \otimes_{A} A^{i+1}$ an $A^{i+1}$-module free.

Since $A$ is Noetherian, the increasing sequence $(\mathfrak{J}_{i})$ is stationary, hence there exists $n$ such that
$f_{1}, \cdots, f_{n}$ generate the ideal $A$, and the $f_{i}$ answer the question.

**Proposition (11.3.16).**

<!-- label: IV.11.3.16 -->

*Let $f : X \to Y$ be a faithfully flat morphism of finite presentation, $g : Y \to Z$ a morphism such that $g \circ f :
X \to Z$ is a morphism of finite type (resp. of finite presentation). Then $g$ is a morphism of finite type (resp. of
finite presentation).*

Since $f$ is surjective and $g \circ f$ quasi-compact, $g$ is quasi-compact `(1.1.3)`. Let us first show that if $g
\circ f$ is of finite presentation, $g$ is quasi-separated. Consider indeed an affine open set $W \subset Z$, and let
$(V_{i})$ be a finite affine cover of $g^{-1}(W)$; the matter is to see that the $V_{i} \cap V_{j}$ are quasi-compact
`(1.2.6 and 1.2.7)`. For each $i$, let $(U_{ih})$ be a finite affine open cover of $f^{-1}(V_{i})$; since $f$ is of
finite presentation, the $U_{ih} \cap U_{jk}$ are all quasi-compact; now, since $f$ is surjective, $V_{i} \cap V_{j}$ is
the union of the images $f(U_{ih} \cap U_{jk})$ for $h$, $k$ varying, hence is quasi-compact since $f$ is continuous.

The question is therefore local on $Y$ and one may suppose that $Y = \operatorname{Spec}(B)$ and $Z =
\operatorname{Spec}(A)$ are affine, $X$ being the finite union of affine open sets $X_{i} = \operatorname{Spec}(C_{i})$,
where the $C_{i}$ are $B$-algebras of finite type (resp. of finite presentation). If $X'$ is the sum prescheme of the
$X_{i}$, $p : X' \to X$ the morphism coinciding with the canonical injection on each $X_{i}$, $p$ is a faithfully flat
morphism of finite presentation `(1.6.5)`, hence $g \circ f \circ p$ is a morphism of finite type (resp. of finite
presentation) and $f \circ p$ a faithfully flat morphism of finite presentation. One may therefore also suppose that $X
= \operatorname{Spec}(C)$ is affine, and one is therefore reduced to proving the

**Corollary (11.3.17).**

<!-- label: IV.11.3.17 -->

*Let $A$ be a ring, $B$ an $A$-algebra, $C$ a $B$-algebra of finite presentation and which is a faithfully flat
$B$-module. Then, if $C$ is an $A$-algebra of finite type (resp. of finite presentation), $B$ is an $A$-algebra of
finite type (resp. of finite presentation).*

Suppose first that $g \circ f$ is of finite type. Let $(B_{\lambda})$ be the filtered increasing family of
sub-$A$-algebras of finite type of $B$; by virtue of `(8.8.2)`, there exists an index $\alpha$ such that $C = C_{\alpha}
\otimes_{B_{\alpha}} B$, where $C_{\alpha}$ is a $B_{\alpha}$-algebra of finite presentation; moreover `(8.10.5` and
`11.2.6)` one may suppose that $C_{\alpha}$ is a faithfully flat $B_{\alpha}$-module. For $\lambda \geq \alpha$, one has
therefore $C = C_{\lambda} \otimes_{B_{\lambda}} B$, where $C_{\lambda}$ is a faithfully flat $B_{\lambda}$-module;
since the map $B_{\lambda} \to B$ is injective, one deduces that the same is true of $C_{\lambda} \to C$. Moreover,
since $C = \lim C_{\lambda}$, every element of $C$ belongs to some $C_{\lambda}$, and consequently there exists
$\lambda$ such that the map $C_{\lambda} \to C$

<!-- original page 143 -->

is bijective, since $C$ is a $B$-algebra of finite type. But then the map $B_{\lambda} \to B$ is bijective by faithful
flatness, hence $B = B_{\lambda}$ is an $A$-algebra of finite type.

Suppose now that $g \circ f$ is of finite presentation, $C$ being therefore an $A$-algebra of finite presentation. From
the first part of the reasoning, one has $B = A[T_{1}, \cdots, T_{n}]/\mathfrak{J}$ for some ideal $\mathfrak{J}$; let
$(\mathfrak{J}_{\lambda})$ be the filtered family of ideals of finite type of $A[T_{1}, \cdots, T_{n}]$ contained in
$\mathfrak{J}$, so that $\mathfrak{J} = \lim \mathfrak{J}_{\lambda}$ and $B = \lim B_{\lambda}$, with $B_{\lambda} =
A[T_{1}, \cdots, T_{n}]/\mathfrak{J}_{\lambda}$. Applying as above `(8.8.2)`, `(8.10.5)` and `(11.2.6)`, one has $C =
C_{\alpha} \otimes_{B_{\alpha}} B$, where $C_{\alpha}$ is a $B_{\alpha}$-algebra of finite presentation and a faithfully
flat $B_{\alpha}$-module; one will again set $C_{\lambda} = C_{\alpha} \otimes_{B_{\alpha}} B_{\lambda}$ for $\lambda
\geq \alpha$ so that $C_{\lambda} = C_{\alpha}/(C_{\alpha} \otimes_{B_{\alpha}}
(\mathfrak{J}_{\lambda}/\mathfrak{J}_{\alpha}))$ by flatness, and similarly $C = C_{\alpha}/(C_{\alpha}
\otimes_{B_{\alpha}} (\mathfrak{J}/\mathfrak{J}_{\alpha}))$. Since by hypothesis $C$ is an $A$-algebra of finite
presentation as well as $C_{\alpha}$, $C_{\alpha} \otimes_{B_{\alpha}} (\mathfrak{J}/\mathfrak{J}_{\alpha})$ is an ideal
of finite type of $C_{\alpha}$ `(1.4.4)`, and the $C_{\alpha} \otimes_{B_{\alpha}}
(\mathfrak{J}_{\lambda}/\mathfrak{J}_{\alpha})$ identify with ideals of finite type of $C_{\alpha}$ of which $C_{\alpha}
\otimes_{B_{\alpha}} (\mathfrak{J}/\mathfrak{J}_{\alpha})$ is the union. There exists consequently $\lambda \geq \alpha$
such that $C_{\alpha} \otimes_{B_{\alpha}} (\mathfrak{J}/\mathfrak{J}_{\alpha}) = C_{\alpha} \otimes_{B_{\alpha}}
(\mathfrak{J}_{\lambda}/\mathfrak{J}_{\alpha})$, whence $\mathfrak{J} = \mathfrak{J}_{\lambda}$ by faithful flatness,
which proves that $B$ is an $A$-algebra of finite presentation.

<!-- original page 143 -->

### 11.4. Descent of flatness by arbitrary morphisms: artinian base case

**Theorem (11.4.1).**

<!-- label: IV.11.4.1 -->

*Let $A$ be a ring, $\mathfrak{J}$ a nilpotent ideal of $A$, $u_{\lambda} : A \to B_{\lambda}$ ($\lambda \in L$) a
family of ring homomorphisms such that the intersection of the kernels of the $u_{\lambda}$ is reduced to `0`. Let $M$
be an $A$-module such that for every $\lambda \in L$, $M \otimes_{A} B_{\lambda}$ is a free $B_{\lambda}$-module and $M
\otimes_{A} (A/\mathfrak{J})$ is a free $(A/\mathfrak{J})$-module. Then $M$ is a free $A$-module. If moreover the index
set $L$ is finite, one can replace "free" by "flat" throughout the preceding statement.*

In both cases it suffices to prove that $M$ is a flat $A$-module: indeed, when $M \otimes_{A} (A/\mathfrak{J})$ is a
free $(A/\mathfrak{J})$-module, it will result that $M$ is a free $A$-module by virtue of $(0_{III}, 10.1.2)$.

We shall use the following lemma, which generalizes $(0_{III}, 10.2.1)$:

**Lemma (11.4.1.1).**

<!-- label: IV.11.4.1.1 -->

*Let $A$ be a ring endowed with a finite filtration $(\mathfrak{J}_{n})_{0 \leq n \leq N+1}$ with $\mathfrak{J}_{0} =
A$, $\mathfrak{J}_{N+1} = 0$. Let $M$ be an $A$-module endowed with the filtration $(\mathfrak{J}_{n} M)_{0 \leq n \leq
N+1}$, and denote by $gr(A)$ and $gr(M)$ the corresponding graded ring and module. Suppose that $M \otimes_{A}
(A/\mathfrak{J}_{1})$ is a flat $(A/\mathfrak{J}_{1})$-module and that the canonical homomorphism*

```text
(11.4.1.2)                gr_0(M) ⊗_{gr_0(A)} gr(A) → gr(M)
```

*is injective. Then $M$ is a flat $A$-module.*

The canonical homomorphism `(11.4.1.2)` is defined in the same way as that of $(0_{III}, 10.1.1)$, being in degree $n$
the homomorphism

```text
  gr_0(M) ⊗_{gr_0(A)} gr_n(A) → gr_n(M)
```

deriving from the canonical homomorphism $M \otimes \mathfrak{J}_{n} \to \mathfrak{J}_{n} M$ by passage to quotients.
The lemma is proved by induction on $N$, since there is nothing to prove for $N = 0$.

<!-- original page 144 -->

The hypotheses on $M$ imply, by virtue of the induction hypothesis, that $M \otimes_{A} (A/\mathfrak{J}_{N})$ is a flat
$(A/\mathfrak{J}_{N})$-module. Note now that one has $\mathfrak{J}_{N} \mathfrak{J}_{N+1} = 0 \subset
\mathfrak{J}_{N+1}$, and $(M/\mathfrak{J}_{1} M) \otimes (\mathfrak{J}_{N}/\mathfrak{J}_{N+1}) = (M/\mathfrak{J}_{N} M)
\otimes (\mathfrak{J}_{N}/\mathfrak{J}_{N+1}) = (M/\mathfrak{J}_{N} M) \otimes \mathfrak{J}_{N}$; hence the canonical
homomorphism

```text
  (M/𝔍_N M) ⊗ 𝔍_N → 𝔍_N M
```

is injective. Applying $(0_{III}, 10.2.1)$ to the $\mathfrak{J}_{N}$-preadic filtration, one concludes that $M$ is
indeed a flat $A$-module.

To apply this lemma to `(11.4.1)`, we shall denote by $\mathfrak{J}_{n}$ the ideal of $A$ intersection of the inverse
images $u^{-1}_{\lambda}(\mathfrak{J}^{n} B_{\lambda})$: it is immediate that $\mathfrak{J}_{0} = A$, $\mathfrak{J}_{m}
\mathfrak{J}_{n} \subset \mathfrak{J}_{m+n}$ for $m \geq 0$, $n \geq 0$; moreover, if $\mathfrak{J}^{N+1} = 0$, one also
has $\mathfrak{J}_{N+1} = 0$ since the intersection of the kernels of the $u_{\lambda}$ is reduced to `0`.

Endow $A$ with the filtration $(\mathfrak{J}_{n})$, $M$ with the filtration $(\mathfrak{J}_{n} M)$, and, for each
$\lambda$, endow $B_{\lambda}$ and $N_{\lambda} = M \otimes_{A} B_{\lambda}$ with the $\mathfrak{J}$-preadic
filtrations; consider for each $\lambda$ the commutative diagram

```text
  gr_𝔍(M) ⊗_{gr_𝔍(A)} gr(A)  ─ f ─→  gr(M)
         │                              │
         │                              │
         ↓                              ↓
  gr_{𝔍}(N_λ) ⊗_{gr_{𝔍}(B_λ)} gr_𝔍(B_λ)  ─ φ_λ ─→  gr_𝔍(N_λ)
```

where the horizontal arrows are the canonical homomorphisms `(11.4.1.2)` and the vertical arrows are deduced from the
canonical homomorphisms $A \to B_{\lambda}$ and $M \to N_{\lambda}$. The hypothesis that $N_{\lambda}$ is a flat
$B_{\lambda}$-module implies that $\phi_{\lambda}$ is injective $(0_{III}, 10.2.1)$, hence $Ker(f) \subset
Ker(f_{\lambda})$. Setting $A_{0} = A/\mathfrak{J}_{1}$, $M_{0} = M \otimes_{A} A_{0}$, note that

```text
  gr_0(N_λ) = N_λ/𝔍 N_λ = (M/𝔍 M) ⊗_A B_λ = (M/𝔍_1 M) ⊗_A (B_λ/𝔍 B_λ)
```

since this last tensor product equals

```text
  (M ⊗_A B_λ)/(Im(M ⊗_A 𝔍 B_λ) + Im(𝔍_1 M ⊗_A B_λ))
```

and one has $Im(\mathfrak{J}_{1} M \otimes_{A} B_{\lambda}) = Im(M \otimes_{A} \mathfrak{J}_{1} B_{\lambda}) \subset
Im(M \otimes_{A} \mathfrak{J} B_{\lambda})$ since $\mathfrak{J}_{1} B_{\lambda} \subset \mathfrak{J} B_{\lambda}$ by
definition; finally, the relation $\mathfrak{J}_{1} N_{\lambda} \subset \mathfrak{J} N_{\lambda}$ shows that one has
also

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

The homomorphism $f_{\lambda}$ can thus be written

```text
  1 ⊗ gr(u_λ) : M_0 ⊗_{A_0} gr(A) → M_0 ⊗_{A_0} gr_𝔍(B_λ)
```

<!-- original page 145 -->

and as `M_0` is by hypothesis a flat `A_0`-module, the kernel of $f_{\lambda}$ equals $M_{0} \otimes_{A_{0}}
R_{\lambda}$, where $R_{\lambda}$ is the kernel of $gr(u_{\lambda}) : gr(A) \to gr_{\mathfrak{J}}(B_{\lambda})$. All
comes down therefore to proving that $\bigcap_{\lambda} (M_{0} \otimes_{A_{0}} R_{\lambda}) = 0$. Now, by definition of
the $\mathfrak{J}_{n}$, the intersection of the kernels of the homomorphisms $\mathfrak{J}_{n} A/\mathfrak{J}_{n+1} A
\to \mathfrak{J}^{n} B_{\lambda}/\mathfrak{J}^{n+1} B_{\lambda}$, as $\lambda$ runs through $L$, is reduced to `0`, in
other words $\bigcap_{\lambda \in L} R_{\lambda} = 0$. This being so, suppose first that `M_0` is a free `A_0`-module;
taking a basis of `M_0`, one sees at once that one has $M_{0} \otimes_{A_{0}} (\bigcap R_{\lambda}) = \bigcap (M_{0}
\otimes_{A_{0}} R_{\lambda})$, whence the proposition in this case. When $L$ is finite, the preceding formula is still
true under the sole hypothesis that `M_0` is a flat `A_0`-module $(0_{I}, 6.1.3)$, which completes the proof.

**Remark (11.4.2).**

<!-- label: IV.11.4.2 -->

*The conclusion of `(11.4.1)` can fail if $L$ is infinite and if one supposes only that $M \otimes_{A} (A/\mathfrak{J})$
is a flat $(A/\mathfrak{J})$-module.* For example, let $V$ be a discrete valuation ring, $K$ its field of fractions, and
let $A = V[T]/(T^{2})$ ($T$ indeterminate); take for $\mathfrak{J}$ the image of `(T)` in $A$, so that $A/\mathfrak{J} =
V$, and take $M = K$, which is a $(A/\mathfrak{J})$-module, so equal to $M \otimes_{A} (A/\mathfrak{J})$; moreover $M$
is a flat $(A/\mathfrak{J})$-module, but not a flat $A$-module, for since $\mathfrak{J}$ is nilpotent, it would result
from $(0_{III}, 10.1.2)$ that $M$ would be a free $A$-module, which is absurd since $\mathfrak{J} K = 0$. Consider on
the other hand the maximal ideal $\mathfrak{m}$ of the Noetherian local ring $A$; one has $\mathfrak{m} K = K$, hence $M
\otimes_{A} (A/\mathfrak{m}^{n}) = 0$ for every integer $n$; the $(A/\mathfrak{m}^{n})$-modules $M \otimes_{A}
(A/\mathfrak{m}^{n})$ are thus flat for every $n$, and the intersection of the $\mathfrak{m}^{n}$ is reduced to `0`.

**Corollary (11.4.3).**

<!-- label: IV.11.4.3 -->

*Let $A$ be a semi-local ring whose radical $\mathfrak{J}$ is nilpotent (for example an artinian ring), $u_{\lambda} : A
\to B_{\lambda}$ ($\lambda \in L$) a family of ring homomorphisms such that the intersection of the kernels of the
$u_{\lambda}$ is reduced to `0`. For an $A$-module $M$ to be flat, it is necessary and sufficient that for every
$\lambda \in L$, $M \otimes_{A} B_{\lambda}$ be a flat $B_{\lambda}$-module.*

Since $A/\mathfrak{J}$ is a direct product of a finite number of fields
`(Bourbaki, Alg. comm., chap. II, §3, n° 5, prop. 16)` and $\mathfrak{J}$ is nilpotent, $A$ is a direct product of a
finite number of local rings $A_{i}$ whose radical is nilpotent `(loc. cit., §4, n° 3, cor. 1 of prop. 15)`, and $M$ is
consequently a direct sum of $A$-modules $M_{i}$, each $M_{i}$ being annihilated by the $A_{j}$ of index $j \neq i$; for
$M$ to be a flat $A$-module, it is necessary and sufficient that each $M_{i}$ be a flat $A_{i}$-module; moreover, the
intersection of the kernels of the homomorphisms $A_{i} \to A \to B_{\lambda}$ is reduced to `0`, and $M_{i}
\otimes_{A_{i}} B_{\lambda}$ is a direct summand of $M \otimes_{A} B_{\lambda}$. One can therefore restrict to the case
where $A$ is moreover local. Then $A/\mathfrak{J}$ is a field, hence $M \otimes_{A} (A/\mathfrak{J})$ is a free
$(A/\mathfrak{J})$-module, and it suffices to see that for every $\lambda$, $M \otimes_{A} B_{\lambda}$ is a free
$B_{\lambda}$-module, by virtue of `(11.4.1)`. But if one sets $\mathfrak{J}_{\lambda} = \mathfrak{J} B_{\lambda}$, $(M
\otimes_{A} B_{\lambda}) \otimes_{B_{\lambda}} (B_{\lambda}/\mathfrak{J}_{\lambda}) = (M \otimes_{A} (A/\mathfrak{J}))
\otimes_{A/\mathfrak{J}} (B_{\lambda}/\mathfrak{J}_{\lambda})$ is a free $(B_{\lambda}/\mathfrak{J}_{\lambda})$-module,
and $\mathfrak{J}_{\lambda}$ is nilpotent. The conclusion thus results from the hypothesis that $M \otimes_{A}
B_{\lambda}$ is a flat $B_{\lambda}$-module and from $(0_{III}, 10.1.2)$.

**Corollary (11.4.4).**

<!-- label: IV.11.4.4 -->

*Let $A$ be a ring, $M$ an $A$-module; suppose that there exists a nilpotent ideal $\mathfrak{J}$ of $A$ such that $M
\otimes_{A} (A/\mathfrak{J})$ is a free $(A/\mathfrak{J})$-module. Then the set of ideals $\mathfrak{K}$ of $A$ such
that $M \otimes_{A} (A/\mathfrak{K})$ is a free $(A/\mathfrak{K})$-module admits a smallest element $\mathfrak{K}_{0}$
(which is also the smallest of the ideals $\mathfrak{K}$ such that $M \otimes_{A} (A/\mathfrak{K})$ is a flat
$(A/\mathfrak{K})$-module).*

<!-- original page 146 -->

*For a homomorphism $u : A \to A'$ to be such that $M \otimes_{A} A'$ is a free $A'$-module (resp. a flat $A'$-module),
it is necessary and sufficient that $u$ factor as $A \to A/\mathfrak{K}_{0} \to A'$ (or equivalently that
$\mathfrak{K}_{0} A' = 0$).*

The fact that the intersection $\mathfrak{K}_{0}$ of the ideals $\mathfrak{K}$ for which $M \otimes_{A}
(A/\mathfrak{K})$ is a free $(A/\mathfrak{K})$-module is the smallest of these ideals results from `(11.4.1)` applied to
the ring $A/\mathfrak{K}_{0}$, to its nilpotent ideal $\mathfrak{J}/\mathfrak{K}_{0}$, and to the homomorphisms
$A/\mathfrak{K}_{0} \to A/\mathfrak{K}$, whose kernels have `0` as intersection. If $A'$ is an
$(A/\mathfrak{K}_{0})$-algebra, one has $M \otimes_{A} A' = (M \otimes_{A} (A/\mathfrak{K}_{0}))
\otimes_{A/\mathfrak{K}_{0}} A'$, hence $M \otimes_{A} A'$ is a free $A'$-module. Conversely, if $A'$ is an $A$-algebra
such that $M \otimes_{A} A'$ is a free $A'$-module and if $\mathfrak{K}$ is the kernel of the homomorphism $A \to A'$,
it results from `(11.4.1)` applied to the ring $A/\mathfrak{K}$, to the $(A/\mathfrak{K})$-module $M \otimes_{A}
(A/\mathfrak{K})$, to the nilpotent ideal $\mathfrak{JK}/\mathfrak{K}$ and to the injective homomorphism $A/\mathfrak{K}
\to A'$, that $M \otimes_{A} (A/\mathfrak{K})$ is a free $(A/\mathfrak{K})$-module, hence that $\mathfrak{K} \supset
\mathfrak{K}_{0}$. The fact that one can replace "free" by "flat" in what precedes (keeping naturally the hypothesis
that $M \otimes_{A} (A/\mathfrak{J})$ is a free $(A/\mathfrak{J})$-module) results from $(0_{III}, 10.1.2)$, as was seen
at the beginning of the proof of `(11.4.1)`.

**Proposition (11.4.5).**

<!-- label: IV.11.4.5 -->

*Let $Y$ be an irreducible prescheme, $f : X \to Y$ a morphism of finite presentation, $\mathcal{F}$ an
$\mathcal{O}_{X}$-Module of finite presentation. Then there exist a non-empty open set $U$ in $Y$ and a closed subscheme
$Z$ of $U$, of finite presentation over $U$, having the following property: for every base change $U' \to U$, setting
$X' = X \times_{Y} U'$, $f' = f_{(U')}$ and $\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{U'}$, in
order that $\mathcal{F}'$ be $f'$-flat, it is necessary and sufficient that the morphism $U' \to U$ factor as $U' \to Z
\to U$. Such a scheme $Z$ has the same underlying space as $U$. Suppose moreover that $Y$ is affine, and let $(W_{i})$
be a finite cover of $X$ by affine open sets; then one may suppose $U$ chosen so that, if $U' = \operatorname{Spec}(A')$
is an affine scheme and $U' \to U$ a morphism factoring as $U' \to Z \to U$, each $\Gamma(W_{i} \times_{Y} U',
\mathcal{F}')$ is a free $A'$-module.*

One may evidently restrict to the case where $Y = \operatorname{Spec}(A)$ is affine. Using `(8.9.1)`, there exists a
Noetherian subring `A_1` of $A$, a morphism of finite type $f_{1} : X_{1} \to Y_{1} = \operatorname{Spec}(A_{1})$ and a
coherent $\mathcal{O}_{X_{1}}$-Module $\mathcal{F}_{1}$ such that $f = f_{1} \times 1$ and $\mathcal{F} =
\mathcal{F}_{1} \otimes_{\mathcal{O}_{Y_{1}}} \mathcal{O}_{Y}$; one can moreover suppose that the $W_{i}$ are inverse
images of affine open sets of `X_1`. Note moreover that `Y_1` is irreducible, the morphism $Y \to Y_{1}$ being dominant
`(I, 1.2.7)`. Suppose the proposition proved for `Y_1`, $\mathcal{F}_{1}$ and $f_{1}$, and let `U_1` be the open set of
`Y_1` and `Z_1` the closed subscheme of `U_1` having the desired properties, $U = U_{1} \times_{Y_{1}} Y$ and $Z = Z_{1}
\times_{Y_{1}} Y$ their inverse images. Then, if $U' \to U$ is a base change such that $\mathcal{F}' = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{U'} = \mathcal{F}_{1} \otimes_{\mathcal{O}_{Y_{1}}} \mathcal{O}_{U'}$ is
$f'$-flat, the morphism $U' \to U_{1}$ factors as $U' \to Z_{1} \to U_{1}$; but as $U' \to U_{1}$ also factors as $U'
\to U \to U_{1}$, the definition of fibre product of preschemes shows that $U' \to U$ factors as $U' \to Z \to U$.

One can therefore restrict to the case where $A$ is *Noetherian*; let $\mathfrak{N}$ be its nilradical, which is
nilpotent, and set $A_{0} = A_{red} = A/\mathfrak{N}$, $Y_{0} = \operatorname{Spec}(A_{0}) = Y_{red}$, $X_{0} = X
\times_{Y} Y_{0}$, $\mathcal{F}_{0} = \mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y_{0}}$, $W_{i,0} = W_{i}
\times_{Y} Y_{0}$; if $M_{i} = \Gamma(W_{i}, \mathcal{F})$, then $M_{i,0} = \Gamma(W_{i,0}, \mathcal{F}_{0})$ equals
$M_{i} \otimes_{A} A_{0}$. As `A_0` is integral, one can, by virtue of the theorem of generic flatness `(6.9.2)`,
replacing if necessary $Y$ by a non-empty open set of $Y$, suppose that the $M_{i,0}$ are free `A_0`-modules. By virtue
of `(11.4.4)`, there is therefore for each $i$ an ideal $\mathfrak{J}_{i} \subset \mathfrak{N}$ such that

<!-- original page 147 -->

the $A$-algebras $A'$ for which the $M_{i} \otimes_{A} A'$ are free (or flat) $A'$-modules are exactly those for which
$\mathfrak{J}_{i} A' = 0$. Let $\mathfrak{J} = \sum_{i} \mathfrak{J}_{i}$, which is an ideal contained in
$\mathfrak{N}$; to say that $\mathcal{F} \otimes_{A} A'$ is $A'$-flat is equivalent to saying that the $M_{i}
\otimes_{A} A'$ are all flat $A'$-modules, hence that $\mathfrak{J} A' = 0$. It follows that if one takes $Z =
V(\mathfrak{J})$, one answers the question, for in order that a morphism $U' \to U$ have the property of the statement,
it is evidently necessary and sufficient that for every affine open set $V' \subset U'$, the morphism $V' \to U$ have
the same property.

**Corollary (11.4.6).**

<!-- label: IV.11.4.6 -->

*Let $A$ be a ring such that $\operatorname{Spec}(A)$ is irreducible, $\mathfrak{p}$ its unique minimal prime ideal, $B$
an $A$-algebra of finite presentation, $M$ a $B$-module of finite presentation. Suppose that $M_{\mathfrak{p}}$ is a
flat $A_{\mathfrak{p}}$-module; then there exists $t \in A - \mathfrak{p}$ such that $M_{t}$ is a free $A_{t}$-module.*

Applying `(11.4.5)` to $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, $\mathcal{F} = \tilde{M}$, one can
(replacing if necessary $A$ by $A_{h}$, where $h \in A - \mathfrak{p}$) suppose that there exists an ideal of finite
type $\mathfrak{J}$ in $A$ such that the $A$-algebras $A'$ for which $M \otimes_{A} A'$ is a free $A'$-module (or flat)
are exactly those such that $\mathfrak{J} A' = 0$. In particular, the hypothesis that $M_{\mathfrak{p}}$ is a flat
$A_{\mathfrak{p}}$-module implies $\mathfrak{J} A_{\mathfrak{p}} = 0$, or equivalently $\mathfrak{J}_{\mathfrak{p}} =
0$. But as $\mathfrak{J}$ is of finite type, there exists $t \in A - \mathfrak{p}$ such that $\mathfrak{J}_{t} = 0$, or
equivalently $\mathfrak{J} A_{t} = 0$, and consequently $M_{t}$ is a free $A_{t}$-module.

**Proposition (11.4.7).**

<!-- label: IV.11.4.7 -->

*Let $A$ be a Noetherian ring, $\mathfrak{J}$ an ideal of $A$, $M$ an $A$-module ideally separated $(0_{III}, 10.2.1)$
for the $\mathfrak{J}$-preadic topology. Let $(\mathfrak{p}_{i})_{1 \leq i \leq r}$ be a finite family of prime ideals
of $A$ containing $\mathfrak{J}$; for every integer $n \geq 0$, let $\mathfrak{p}^{(n)}_{i}$ be the $n$-th symbolic
power of $\mathfrak{p}_{i}$ (kernel of the homomorphism $A \to A_{\mathfrak{p}_{i}}/\mathfrak{p}^{n}_{i}
A_{\mathfrak{p}_{i}}$); set $\mathfrak{J}_{n} = \bigcap^{r}_{i=1} \mathfrak{p}^{(n)}_{i}$, so that $\mathfrak{J}_{n}
\supset \mathfrak{J}^{n}$, and suppose that the topology defined by the filtration $(\mathfrak{J}_{n})$ is identical to
the $\mathfrak{J}$-preadic topology (in other words, that for every $n$, there exists $m$ such that $\mathfrak{J}^{n}
\supset \mathfrak{J}_{m}$). For $M$ to be a flat $A$-module, it is necessary and sufficient that $M \otimes_{A}
(A/\mathfrak{J})$ be a flat $(A/\mathfrak{J})$-module and that, for every $i$, $M \otimes_{A} A_{\mathfrak{p}_{i}} =
M_{\mathfrak{p}_{i}}$ be a flat $A_{\mathfrak{p}_{i}}$-module.*

As $M$ is ideally separated, it suffices, by virtue of $(0_{III}, 10.2.1)$, to show that, for every $n \geq 0$, $M
\otimes_{A} (A/\mathfrak{J}^{n})$ is a flat $(A/\mathfrak{J}^{n})$-module; since every $\mathfrak{J}^{n}$ contains a
$\mathfrak{J}_{m}$, it amounts to the same thing to prove that for every $n$, $M \otimes_{A} (A/\mathfrak{J}_{n})$ is a
flat $(A/\mathfrak{J}_{n})$-module. Now, as $\mathfrak{J}_{1} \supset \mathfrak{J}$, $M \otimes_{A}
(A/\mathfrak{J}_{1})$ is a flat $(A/\mathfrak{J}_{1})$-module; in the ring $A/\mathfrak{J}_{n}$, the ideal
$\mathfrak{J}_{1}/\mathfrak{J}_{n}$ is nilpotent, and finally the intersection of the kernels of the homomorphisms
$A/\mathfrak{J}_{n} \to A_{\mathfrak{p}_{i}}/\mathfrak{p}^{n}_{i} A_{\mathfrak{p}_{i}}$ is null in $A/\mathfrak{J}_{n}$,
by definition of $\mathfrak{J}_{n}$. It suffices therefore, by `(11.4.1)`, to verify that $M \otimes_{A}
(A_{\mathfrak{p}_{i}}/\mathfrak{p}^{n}_{i} A_{\mathfrak{p}_{i}})$ is a flat $(A_{\mathfrak{p}_{i}}/\mathfrak{p}^{n}_{i}
A_{\mathfrak{p}_{i}})$-module, which results from the hypothesis that $M \otimes_{A} A_{\mathfrak{p}_{i}}$ is a flat
$A_{\mathfrak{p}_{i}}$-module.

**Remark (11.4.8).**

<!-- label: IV.11.4.8 -->

*The hypothesis made in `(11.4.7)` on the topology defined by the $\mathfrak{J}_{n}$ is verified if, for every
sufficiently large $n$, $Ass(A/\mathfrak{J}^{n})$ is contained in the set of $\mathfrak{p}_{i}$.* Indeed,
$\mathfrak{J}^{n}$ is then an intersection of primary ideals for the $\mathfrak{p}_{i}$, each of which contains a
symbolic power of $\mathfrak{p}_{i}$, whence the conclusion. In particular:

**Corollary (11.4.9).**

<!-- label: IV.11.4.9 -->

*Let $A$ be a Noetherian ring, $\mathfrak{J}$ a nilpotent ideal of $A$, $M$ an $A$-module. For $M$ to be a flat
$A$-module (resp. free), it is necessary and sufficient that $M \otimes_{A} (A/\mathfrak{J})$ be a flat (resp. free)
$(A/\mathfrak{J})$-module and that for every prime ideal $\mathfrak{p} \in Ass(A)$, $M_{\mathfrak{p}}$ be a flat
$A_{\mathfrak{p}}$-module.*

<!-- original page 148 -->

The assertion concerning the case where $M \otimes_{A} (A/\mathfrak{J})$ is free still follows from the assertion
concerning the case where $M \otimes_{A} (A/\mathfrak{J})$ is flat by $(0_{III}, 10.1.2)$.

**Corollary (11.4.10).**

<!-- label: IV.11.4.10 -->

*Let $A$ be a Noetherian ring, $\mathfrak{J}$ an ideal of $A$, $M$ an $A$-module. Suppose that $M$ is ideally separated
for the $\mathfrak{J}$-preadic topology and that $gr_{\mathfrak{J}}(A)$ is a flat $(A/\mathfrak{J})$-module. For $M$ to
be a flat $A$-module, it is necessary and sufficient that $M \otimes_{A} (A/\mathfrak{J})$ be a flat
$(A/\mathfrak{J})$-module and that for every $\mathfrak{p} \in Ass(A/\mathfrak{J})$, $M_{\mathfrak{p}}$ be a flat
$A_{\mathfrak{p}}$-module.*

Taking `(11.4.8)` into account, all comes down to showing that $Ass(A/\mathfrak{J}^{n})$ is contained in
$Ass(A/\mathfrak{J})$ for every $n$. Now, if $a \in A$ belongs to none of the $\mathfrak{p} \in Ass(A/\mathfrak{J})$,
the homothety of ratio $a$ is injective in $A/\mathfrak{J}$; as each of the $\mathfrak{J}^{k}/\mathfrak{J}^{k+1}$ is a
flat $(A/\mathfrak{J})$-module, $a$ is also a $(\mathfrak{J}^{k}/\mathfrak{J}^{k+1})$-regular element, hence $a$ is
$(A/\mathfrak{J}^{n})$-regular for every $n$ `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 1 of th. 1)`, and
consequently does not belong to any prime ideal associated to $A/\mathfrak{J}^{n}$, whence the corollary
`(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`.

**Proposition (11.4.11).**

<!-- label: IV.11.4.11 -->

*Let $A$ be a local artinian ring of maximal ideal $\mathfrak{m}$, $Y = \operatorname{Spec}(A)$, $y$ the unique point of
$Y$, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Let
$(A'_{\alpha})$ be a family of local rings, and for each $\alpha$, $u_{\alpha} : A \to A'_{\alpha}$ a ring homomorphism
(necessarily local). Set $Y'_{\alpha} = \operatorname{Spec}(A'_{\alpha})$, $X'_{\alpha} = X \times_{Y} Y'_{\alpha}$,
$\mathcal{F}'_{\alpha} = \mathcal{F} \otimes_{A} A'_{\alpha}$. Let $x$ be a point of $X$, and suppose the following
conditions verified:*

*(i) The intersection of the kernels of the $u_{\alpha}$ is reduced to `0`.*

*(ii) The extension $k(x)$ of the residue field $k$ of $A$ is primary `(4.3.1)` (a condition automatically verified if
$k$ is separably closed).*

*(iii) For every $\alpha$, there exists a point $x'_{\alpha} \in X'_{\alpha}$ whose respective projections in $X$ and
$Y'_{\alpha}$ are $x$ and the closed point $y'_{\alpha}$ of $Y'_{\alpha}$, and such that $\mathcal{F}'_{\alpha}$ is
$Y'_{\alpha}$-flat at the point $x'_{\alpha}$.*

*Under these conditions, $\mathcal{F}$ is $f$-flat at the point $x$.*

The question being local on $X$, one can evidently restrict to the case where $f$ is a morphism of finite type and
suppose $\mathcal{F} \neq 0$. We shall proceed in several steps.

**I)** *Reduction to the case where $A'_{\alpha}$ is a local ring of a $Y$-prescheme of finite type and where the
residue field $k'_{\alpha}$ of $A'_{\alpha}$ is a finite extension of $k$.*

As the reduction is done separately on each $A'_{\alpha}$, one can suppress in this part the index $\alpha$. Let
$\mathfrak{m}'$ be the maximal ideal of $A'$. Consider $A'$ as inductive limit of its sub-$A$-algebras of finite type
$B_{\lambda}$, and set $\mathfrak{n}_{\lambda} = \mathfrak{m}' \cap B_{\lambda}$; $A'$ is also inductive limit of its
local subrings $B'_{\lambda} = (B_{\lambda})_{\mathfrak{n}_{\lambda}}$ `(5.13.5)`, and one evidently has $\mathfrak{m}'
\cap B'_{\lambda} = \mathfrak{n}_{\lambda}$, maximal ideal of $B'_{\lambda}$. There exists therefore `(11.2.6)` an index
$\lambda$ such that, setting $Z_{\lambda} = \operatorname{Spec}(B'_{\lambda})$, $\mathcal{F} \otimes_{A} B'_{\lambda}$
is $Z_{\lambda}$-flat at the point $x'_{\lambda}$, projection of $x'$, the projection of $x'_{\lambda}$ on $Z_{\lambda}$
being the closed point $\xi_{\lambda}$ of $Z_{\lambda}$.

One can therefore suppose that there exists an affine scheme $Z'$ of finite type over $Y$ and a point $\xi'$ of $Z'$
such that $A' = \mathcal{O}_{Z', \xi'}$, and that, if one sets $T' = X \times_{Y} Z'$, there exists a point $t' \in T'$
whose projections in $Z'$ and $X$ are $\xi'$ and $x$, and such that $\mathcal{F} \otimes_{Y} Z'$ is $Z'$-flat at the
point $t'$. Let $Z'_{1}$ (resp. `X_1`) be a closed subprescheme of $Z'$ (resp. $X$) having as underlying space the
closure of ${\xi'}$ (resp. ${x}$), and set $T'_{1} = X_{1} \times_{Y} Z'_{1}$. The set $U$ of points of $T'_{1}$ where
$\mathcal{F} \otimes_{Y} Z'$ is $Z'$-flat is open in $T'_{1}$ `(11.1.1)` and contains $t'$, hence

<!-- original page 149 -->

$V = U \cap T'_{1}$ is non-empty open in $T'_{1}$. The ring $A$, being artinian, is a Jacobson ring, hence `(10.4.6)`
$Z'_{1}$ and $T'_{1}$ are Jacobson preschemes; consequently there exists in $V$ a point $t'_{0}$ closed in $V$, and its
image $z'_{0}$ in $Z'_{1}$ is a closed point of $Z'_{1}$ `(10.4.7)`. Let $f_{1}$ be the restriction of $f$ to `X_1`,
$h : T'_{1} \to Z'_{1}$ the canonical projection; $V \cap h^{-1}(z'_{0})$ is a non-empty open set in
$f^{-1}_{1}(y) \otimes_{k(y)} k(z'_{0})$, and as this latter prescheme is flat over $f^{-1}_{1}(y)$, a maximal point
$t'_{1}$ of $V \cap h^{-1}(z'_{0})$ is necessarily above the unique maximal point $x$ of `X_1` `(2.3.4)`. Finally,
$k(t'_{1})$ is a *finite* extension of $k$ `(I, 6.4.2)` and the homomorphism
$A = \mathcal{O}_{Y, y} \to A' = \mathcal{O}_{Z', z'}$ factors as
$\mathcal{O}_{Y, y} \to \mathcal{O}_{Z', z'_{0}} \to \mathcal{O}_{Z', z'}$, hence its kernel is contained in that of
$\mathcal{O}_{Y, y} \to \mathcal{O}_{Z', z'_{0}}$. This completes the announced reduction.

**II)** *Reduction to the case where the $A'_{\alpha}$ are finite in number and are finite $A$-algebras.* — Let
$\mathfrak{m}'_{\alpha}$ be the maximal ideal of $A'_{\alpha}$; as $A'_{\alpha}$ is a Noetherian local ring, the
intersection of the $\mathfrak{m}'^{n}_{\alpha}$ is `0` $(0_{I}, 7.3.5)$; the intersection of the
$u^{-1}_{\alpha}(\mathfrak{m}'^{n}_{\alpha})$ for all indices $n$ and $\alpha$ is thus equal to the intersection of the
kernels of the $u_{\alpha}$, hence is reduced to `0` by hypothesis (i). Since $A$ is artinian, there is already a finite
number of these ideals whose intersection is `0`; denote them $u^{-1}_{i}(\mathfrak{m}'^{n_{i}}_{i})$ ($1 \leq i \leq
r$). As the $A'_{i}$ are Noetherian, the $\mathfrak{m}'^{n_{i}}_{i}/\mathfrak{m}'^{n_{i}+1}_{i}$ are
$(A'_{i}/\mathfrak{m}'_{i})$-modules of finite length, and as $A'_{i}/\mathfrak{m}'_{i}$ is an $A$-vector space of
finite rank, one sees that $A''_{i} = A'_{i}/\mathfrak{m}'^{n_{i}}_{i}$ is a finite $A$-algebra and a local artinian
ring. The announced reduction thus results from `(2.1.4)`.

**III)** *End of the proof.* — Suppose from now on that the $A'_{i}$ ($1 \leq i \leq r$) are finite in number and are
finite $A$-algebras. For every $i$, the residue field $k_{i}$ of $A'_{i}$ is a finite extension of $k$; using hypothesis
(ii), one concludes that the inverse image of $x$ in $X'_{i}$ is reduced to the single point $x'_{i}$ `(4.3.2)`. Let
$Y'$ be the sum prescheme of the $Y'_{i}$, $X' = X \times_{Y} Y'$, the sum of the $X'_{i}$, $\mathcal{F}' = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$. The hypothesis implies that $\mathcal{F}'$ is $Y'$-flat at the points of
the inverse image of $x$ by the projection $p : X' \to X$. As $p$ is of finite type, there exists consequently an open
set $U' \supset p^{-1}(x)$ such that $\mathcal{F}'$ is $Y'$-flat at the points of $U'$ `(11.1.1)`. Moreover, the
morphism $Y' \to Y$ is finite since the $A'_{i}$ are finite $A$-algebras; hence $p$ is a finite morphism `(II, 6.1.5)`,
consequently closed `(II, 6.1.10)`, and there exists therefore an affine neighbourhood $U$ of $x$ in $X$ such that
$p^{-1}(U) \subset U'$. Let $B$ and $A'$ be the rings of the schemes $U$ and $Y'$ ($A'$ being the direct product of the
$A'_{i}$); replacing $X$ by $U$, one has thus $\mathcal{F} = \tilde{M}$, where $M$ is a $B$-module, and by hypothesis
$M' = M \otimes_{A} A'$ is a flat $A'$-module `(2.1.2)`; as the homomorphism $A \to A'$ is injective by construction,
one can apply `(11.4.3)`, which proves that $M$ is a flat $A$-module. Q.E.D.

**Proposition (11.4.12).**

<!-- label: IV.11.4.12 -->

*Let $A$ be a local artinian ring of residue field $k$, $Y = \operatorname{Spec}(A)$, $f : X \to Y$ a morphism locally
of finite type, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Let $(A'_{\alpha})$ be a family of local rings, and
for each $\alpha$, $u_{\alpha} : A \to A'_{\alpha}$ a ring homomorphism. Set $Y'_{\alpha} =
\operatorname{Spec}(A'_{\alpha})$, $X'_{\alpha} = X \times_{Y} Y'_{\alpha}$, $f'_{\alpha} = f_{(Y'_{\alpha})}$,
$\mathcal{F}'_{\alpha} = \mathcal{F} \otimes_{A} A'_{\alpha}$. Let $x$ be a point of $X$, and suppose the following
conditions verified:*

*(i) The intersection of the kernels of the $u_{\alpha}$ is reduced to `0`.*

*(ii) For every $\alpha$, $\mathcal{F}'_{\alpha}$ is $f'_{\alpha}$-flat at all points $x'_{\alpha} \in X'_{\alpha}$
whose respective projections in $X$ and $Y'_{\alpha}$ are $x$ and the closed point $y'_{\alpha}$ of $Y'_{\alpha}$.*

*Then $\mathcal{F}$ is $f$-flat at the point $x$.*

<!-- original page 150 -->

By hypothesis, the intersection of the kernels of the $u_{\alpha}$ is reduced to `0`; as $A$ is artinian, there already
exists a finite number of these kernels whose intersection is `0`, hence one can restrict to the case where the family
$(A'_{\alpha})$ is finite. Let $k'$ be an algebraic closure of $k$; one knows $(0_{III}, 10.3.1)$ that there exists a
local homomorphism $A \to B$ making $B$ a flat $A$-module, such that $B$ is a local artinian ring, integral over $A$,
and that $B \otimes_{A} k$ is isomorphic to $k'$. By flatness, the kernels of the homomorphisms $B \to B'_{\alpha} = B
\otimes_{A} A'_{\alpha}$ are deduced from those of the $u_{\alpha}$ by tensorisation with $B$, and as they are finite in
number, their intersection is reduced to `0` $(0_{I}, 6.1.3)$. Consider the rings $B'_{\alpha \beta}$, localizations of
$B'_{\alpha}$ at its maximal ideals; one knows `(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1)` that the
intersection of the kernels of the homomorphisms $B'_{\alpha} \to B'_{\alpha \beta}$ (for a given $\alpha$) is reduced
to `0`; one concludes that the intersection of the kernels of the composed homomorphisms $v_{\alpha \beta} : B \to
B'_{\alpha} \to B'_{\alpha \beta}$ ($\alpha$ and $\beta$ variable) is reduced to `0`. On the other hand, as $B$ is
integral over $A$, $B'_{\alpha}$ is integral over $A'_{\alpha}$, hence its maximal ideals are above the maximal ideal of
$A'_{\alpha}$. If one sets $Z'_{\alpha \beta} = \operatorname{Spec}(B'_{\alpha \beta})$, $T'_{\alpha \beta} =
X'_{\alpha} \times_{Y'_{\alpha}} Z'_{\alpha \beta}$, $f'_{\alpha \beta} = f'_{\alpha(Z'_{\alpha \beta})}$, $\mathcal{G}
= \mathcal{F} \otimes_{A} B$ and $\mathcal{G}_{\alpha \beta} = \mathcal{G} \otimes_{B} B'_{\alpha \beta}$, one sees thus
that hypotheses (i) and (ii) are still verified when one replaces respectively $A$, $A'_{\alpha}$, $u_{\alpha}$,
$\mathcal{F}$ and $x$ by $B$, $B'_{\alpha \beta}$, $v_{\alpha \beta}$, $\mathcal{G}$ and a point $t$ of $T = X
\otimes_{A} B$ above $x$. As the residue field of $B$ is separably closed, one deduces from `(11.4.11)` that
$\mathcal{G}$ is flat over $B$ at the point $t$. But since $B$ is a faithfully flat $A$-module, one concludes by
`(2.1.4)` that $\mathcal{F}$ is flat over $A$ at the point $x$, which proves `(11.4.12)`.

**Corollary (11.4.13).**

<!-- label: IV.11.4.13 -->

*Let $A$ be a local artinian ring, $Y = \operatorname{Spec}(A)$, $f : X \to Y$ a morphism locally of finite type,
$\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Let $(Y'_{\alpha})$ be a family of $A$-preschemes, and for every
$\alpha$, set $X'_{\alpha} = X \times_{Y} Y'_{\alpha}$, $f'_{\alpha} = f_{(Y'_{\alpha})}$, $\mathcal{F}'_{\alpha} =
\mathcal{F} \otimes_{Y} \mathcal{O}_{Y'_{\alpha}}$. Let $x$ be a point of $X$ and suppose the following hypotheses
verified:*

*(i) The intersection of the kernels of the homomorphisms $A \to \Gamma(Y'_{\alpha}, \mathcal{O}_{Y'_{\alpha}})$
corresponding to the structure morphisms is reduced to `0`.*

*(ii) For every $\alpha$, $\mathcal{F}'_{\alpha}$ is $f'_{\alpha}$-flat at all points $x'_{\alpha} \in X'_{\alpha}$
whose projection in $X$ is $x$.*

*Then $\mathcal{F}$ is $f$-flat at the point $x$.*

Indeed, for every $y'_{\alpha} \in Y'_{\alpha}$, consider the local scheme $Y''_{\alpha, y'_{\alpha}} =
\operatorname{Spec}(\mathcal{O}_{Y'_{\alpha}, y'_{\alpha}})$; by virtue of `(2.1.4)`, $\mathcal{F} \otimes_{Y}
\mathcal{O}_{Y''_{\alpha, y'_{\alpha}}}$ is $Y''_{\alpha, y'_{\alpha}}$-flat at points whose projections on $X$ and
$Y''_{\alpha, y'_{\alpha}}$ are $x$ and the closed point of $Y''_{\alpha, y'_{\alpha}}$. Moreover, the kernel of the
homomorphism $A \to \Gamma(Y'_{\alpha}, \mathcal{O}_{Y'_{\alpha}})$ is the intersection of the kernels of the
homomorphisms $A \to \Gamma(Y''_{\alpha, y'_{\alpha}}, \mathcal{O}_{Y''_{\alpha, y'_{\alpha}}})$, for one immediately
reduces to the case where $Y'_{\alpha}$ is affine, and it suffices then to apply
`Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1`. Replacing the family $(Y'_{\alpha})$ by the family of
$Y''_{\alpha, y'_{\alpha}}$, one is therefore reduced to `(11.4.12)`.

### 11.5. Descent of flatness by arbitrary morphisms: general case

**Theorem (11.5.1).**

<!-- label: IV.11.5.1 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module, $x$ a point of $X$, $y = f(x)$. Let $(Y'_{\alpha})$ be a family of local $Y$-preschemes
$Y'_{\alpha} = \operatorname{Spec}(A'_{\alpha})$ such that the images of the closed points $y'_{\alpha}$ of
$Y'_{\alpha}$ are all equal to $y$. For every $\alpha$, let $\mathfrak{m}'_{\alpha}$ be the maximal ideal of
$A'_{\alpha}$, and $u_{\alpha} : \mathcal{O}_{y} \to A'_{\alpha}$*

<!-- original page 151 -->

*the canonical homomorphism `(I, 2.4.4)`; suppose that the finite intersections of the ideals
$u^{-1}_{\alpha}(\mathfrak{m}'^{n_{\alpha}}_{\alpha})$ form a fundamental system of neighbourhoods of `0` in
$\mathcal{O}_{y}$. Set $X'_{\alpha} = X \times_{Y} Y'_{\alpha}$, $f'_{\alpha} = f_{(Y'_{\alpha})}$,
$\mathcal{F}'_{\alpha} = \mathcal{F} \otimes_{Y} \mathcal{O}_{Y'_{\alpha}}$, and suppose that one of the following
hypotheses is verified:*

*(i) For every $\alpha$, $\mathcal{F}'_{\alpha}$ is $f'_{\alpha}$-flat at all points whose projection in $X$ is equal to
$x$ and whose projection in $Y'_{\alpha}$ is equal to $y'_{\alpha}$.*

*(ii) For every $\alpha$, there exists $x'_{\alpha} \in X'_{\alpha}$ whose projection on $X$ is $x$ and whose projection
in $Y'_{\alpha}$ equals $y'_{\alpha}$, such that $\mathcal{F}'_{\alpha}$ is $f'_{\alpha}$-flat at the point
$x'_{\alpha}$, and $k(x)$ is a primary extension of $k(y)$.*

*Under these conditions, $\mathcal{F}$ is $f$-flat at the point $x$.*

Let $\mathfrak{m}_{y}$ be the maximal ideal of $\mathcal{O}_{y}$; as $\mathcal{O}_{y}$ and $\mathcal{O}_{x}$ are
Noetherian and $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is a local homomorphism, it suffices, by virtue of $(0_{III},
10.2.2)$, to prove that for every $n > 0$, $\mathcal{F}_{x}/\mathfrak{m}^{n}_{y} \mathcal{F}_{x}$ is a flat
$(\mathcal{O}_{y}/\mathfrak{m}^{n}_{y})$-module. Denote by $(\mathfrak{J}_{\lambda})$ the family of finite intersections
of the $u^{-1}_{\alpha}(\mathfrak{m}'^{n_{\alpha}}_{\alpha})$; by hypothesis, there exists $\lambda$ such that
$\mathfrak{J}_{\lambda} \subset \mathfrak{m}^{n}_{y}$, and as $\mathcal{F}_{x}/\mathfrak{m}^{n}_{y} \mathcal{F}_{x} =
(\mathcal{F}_{x}/\mathfrak{J}_{\lambda} \mathcal{F}_{x}) \otimes_{\mathcal{O}_{y}/\mathfrak{J}_{\lambda}}
(\mathcal{O}_{y}/\mathfrak{m}^{n}_{y})$, it will suffice to prove that $\mathcal{F}_{x}/\mathfrak{J}_{\lambda}
\mathcal{F}_{x}$ is a flat $(\mathcal{O}_{y}/\mathfrak{J}_{\lambda})$-module. Now, for each $\alpha$ such that
$\mathfrak{J}_{\lambda} \subset u^{-1}_{\alpha}(\mathfrak{m}'^{n_{\alpha}}_{\alpha})$, one has, by passage to quotients,
a homomorphism $u'_{\alpha} : \mathcal{O}_{y}/\mathfrak{J}_{\lambda} \to
A'_{\alpha}/\mathfrak{m}'^{n_{\alpha}}_{\alpha}$, and the intersection of the kernels of the $u'_{\alpha}$ is reduced to
`0`. Taking `(I, 3.6.1)` into account, one sees that one is reduced to `(11.4.11)` in case (ii) and to `(11.4.12)` in
case (i).

**Corollary (11.5.2).**

<!-- label: IV.11.5.2 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module, $x$ a point of $X$, $y = f(x)$; set $A = \mathcal{O}_{y}$. Let $u : A \to A'$ be a
homomorphism of $A$ into a Zariski ring $A'$, such that the inverse image $u^{-1}(\mathfrak{r}')$ of the radical
$\mathfrak{r}'$ of $A'$ is the maximal ideal $\mathfrak{m}$ of $A$; suppose moreover that the homomorphism $\hat{u} :
\hat{A} \to \hat{A}'$ is injective. Set $Y' = \operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$,
$\mathcal{F}' = \mathcal{F} \otimes_{Y} \mathcal{O}_{Y'}$. For $\mathcal{F}$ to be $f$-flat at the point $x$, it is
necessary and sufficient that $\mathcal{F}'$ be $f'$-flat at every point whose projection in $X$ is equal to $x$ and
whose projection in $Y'$ is equal to a closed point of $Y'$.*

*If moreover $A'$ is a finite $A$-algebra, one may in what precedes replace the hypothesis that `û` is injective by the
hypothesis that $u$ is injective.*

As $A$ (resp. $A'$) identifies with a subring of `Â` (resp. `Â'`)
`(Bourbaki, Alg. comm., chap. III, §3, n° 3, prop. 6)`, one sees first that $u$ itself is injective and that `û` is its
prolongation by continuity to `Â`.

Let $(\mathfrak{m}'_{\alpha})$ be the family of maximal ideals of $A'$; as one has

```text
  𝔪'^n_α Â' = 𝔪̂'^n_α,    and    𝔪̂'^n_α ∩ A' = 𝔪'^n_α,
```

and the $\hat{\mathfrak{m}}'^{n}_{\alpha}$ are open in `Â'`, one has $u^{-1}(\mathfrak{m}'^{n}_{\alpha}) = A \cap
\hat{u}^{-1}(\hat{\mathfrak{m}}'^{n}_{\alpha})$, and it will suffice to show that in $A$, the finite intersections of
the $\hat{u}^{-1}(\hat{\mathfrak{m}}'^{n}_{\alpha})$ form a fundamental system of neighbourhoods of `0`, which will
allow application of `(11.5.1)` to the composed homomorphisms $v_{\alpha} \circ u : A \to
\hat{A}'_{\mathfrak{m}'_{\alpha}}$, where $p_{\alpha} : \hat{A}' \to \hat{A}'_{\mathfrak{m}'_{\alpha}}$ is the canonical
homomorphism. As `Â`

<!-- original page 152 -->

is complete, it will suffice to show that the intersection of the $\hat{u}^{-1}(\hat{\mathfrak{m}}'^{n}_{\alpha})$ is
reduced to `0`
`(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8, where one may in the proof replace the decreasing sequence by any filtered set)`.
Now, for every fixed $\alpha$, the intersection of the $\hat{\mathfrak{m}}'^{n}_{\alpha}
\hat{A}'_{\mathfrak{m}'_{\alpha}}$ for $n > 0$ is reduced to `0` in the Noetherian local ring
$\hat{A}'_{\mathfrak{m}'_{\alpha}}$. On the other hand the $\hat{\mathfrak{m}}'_{\alpha}$ are the maximal ideals of
`Â'`, hence the canonical homomorphism $\hat{A}' \to \prod_{\alpha} \hat{A}'_{\mathfrak{m}'_{\alpha}}$ is injective
`(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 2 of th. 1)`, and as by hypothesis $\hat{u} : \hat{A} \to \hat{A}'$ is
also injective, this completes the proof in the general case. The last assertion results from the fact that `Â` is a
faithfully flat $A$-module $(0_{I}, 7.3.5)$ and $\hat{A}' = A' \otimes_{A} \hat{A}$ since $A'$ is by hypothesis an
$A$-module of finite type
`(Bourbaki, Alg. comm., chap. III, §3, n° 4, th. 3 and chap. IV, §2, n° 5, cor. 3 of prop. 9)`.

**Proposition (11.5.3).**

<!-- label: IV.11.5.3 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation, $x$ a point of $X$, $y = f(x)$, $g = (\psi, \theta) : Y' \to Y$ a proper morphism of finite
presentation. Suppose that:*

*(i) The homomorphism $\theta_{y} : \mathcal{O}_{y} \to (g_{*}(\mathcal{O}_{Y'}))_{y}$ is injective.*

*(ii) For every $x' \in X' = X \times_{Y} Y'$ whose projection in $X$ is $x$, $\mathcal{F}' = \mathcal{F} \otimes_{Y}
\mathcal{O}_{Y'}$ is $Y'$-flat at the point $x'$.*

*Then $\mathcal{F}$ is $f$-flat at the point $x$.*

The question being local on $X$, one can suppose $f$ of finite presentation. Let $p : X' \to X$ be the canonical
projection. As $f' = f_{(Y')} : X' \to Y'$ is of finite presentation `(1.6.2)` and $\mathcal{F}'$ is an
$\mathcal{O}_{X'}$-Module of finite presentation $(0_{I}, 5.2.5)$, it results from `(11.3.1)` that the set $U'$ of
points of $X'$ where $\mathcal{F}'$ is $f'$-flat is open. As $U'$ contains $p^{-1}(x)$ by hypothesis, and $p$ is proper,
hence closed, $U'$ contains a set of the form $p^{-1}(U)$, where $U$ is a neighbourhood of $x$. Replacing $X$ by $U$,
one can therefore suppose already that $\mathcal{F}'$ is $f'$-flat. On the other hand, taking `(I, 3.6.5)`,
`(II, 5.4.2)` and `(2.1.4)` into account, one can replace $Y$ by $\operatorname{Spec}(\mathcal{O}_{y})$, i.e. suppose
that $Y = \operatorname{Spec}(A)$, where $A$ is a local ring. Under these conditions, we shall prove that $\mathcal{F}$
is $f$-flat. By virtue of `(5.13.5)`, $A$ is the inductive limit of Noetherian local subrings $A_{\lambda}$ such that
the canonical injection $A_{\lambda} \to A$ is a local homomorphism. By virtue of `(8.9.1)`, one can suppose that $X =
X_{\lambda} \otimes_{A_{\lambda}} A$, $f = f_{\lambda} \otimes 1_{A}$, $\mathcal{F} = \mathcal{F}_{\lambda}
\otimes_{A_{\lambda}} A$, for a suitable $\lambda$, $f_{\lambda} : X_{\lambda} \to Y_{\lambda} =
\operatorname{Spec}(A_{\lambda})$ being a morphism of finite type, $\mathcal{F}_{\lambda}$ a coherent
$\mathcal{O}_{X_{\lambda}}$-Module. Similarly, one can suppose that $Y' = Y'_{\lambda} \otimes_{A_{\lambda}} A$, $g =
g_{\lambda} \otimes 1_{A}$, where $g_{\lambda} : Y'_{\lambda} \to Y_{\lambda}$ is a morphism of finite presentation;
moreover `(8.10.5, (xii))`, one can suppose that $g_{\lambda}$ is proper. As by hypothesis the homomorphism $A \to
\Gamma(Y', \mathcal{O}_{Y'})$ is injective and $A_{\lambda}$ is a subring of $A$, the homomorphism $A_{\lambda} \to
\Gamma(Y', \mathcal{O}_{Y'})$ is also injective. Finally, by virtue of `(11.2.6)`, one can suppose $\lambda$ taken such
that $\mathcal{F}'_{\lambda} = \mathcal{F}_{\lambda} \otimes_{Y_{\lambda}} Y'_{\lambda}$ is $f'_{\lambda}$-flat, since
$\mathcal{F}' = \mathcal{F}'_{\lambda} \otimes_{Y'_{\lambda}} Y'$. These remarks prove that one may from now on suppose
the ring $A$ Noetherian, the other hypotheses of `(11.5.3)` being verified. Set then $B = \hat{A}$, $Z =
\operatorname{Spec}(B)$; as $B$ is a faithfully flat $A$-module $(0_{I}, 7.3.5)$, it amounts to the same thing to say
that $\mathcal{F}$ is $f$-flat or that $\mathcal{F} \otimes_{Y} Z$ is $Z$-flat `(2.1.4)`; similarly, if one sets $Z' =
Y' \times_{Y} Z$, the morphism $Z' \to Y'$ is faithfully flat `(2.2.13)`, hence it amounts to the same thing to say that
$\mathcal{F}'$ is $f'$-flat or that $\mathcal{F}' \otimes_{Y'} Z'$ is $Z'$-flat; finally $h = g_{(Z)} : Z' \to Z$ is
proper `(II, 5.4.2)` and of finite type `(1.5.2)`, `Â` is Noetherian, and if $z$ is its

<!-- original page 153 -->

closed point, the homomorphism $\hat{A} \to (h_{*}(\mathcal{O}_{Z'}))_{z}$ is injective, for it results from `(2.3.1)`
that $h_{*}(\mathcal{O}_{Z'}) = g_{*}(\mathcal{O}_{Y'}) \otimes_{Y} Z$, and our assertion results from hypothesis (i)
and from the definition of flat modules $(0_{I}, 6.1.1)$.

One can therefore from now on suppose the Noetherian local ring $A$ *complete*; the proof will be completed if one
proves that the intersection of the kernels of the homomorphisms $A = \mathcal{O}_{y} \to \mathcal{O}_{y'}$ (where $y'$
runs through $g^{-1}(y)$) is reduced to `0`. Indeed, the $\mathcal{O}_{y'}$ are Noetherian local rings, hence for each
$y'$ the intersection of the $\mathfrak{m}^{n}_{y'}$ ($n > 0$) is reduced to `0`; if $\mathfrak{a}_{n, y'}$ is the
inverse image in $A$ of $\mathfrak{m}^{n}_{y'}$, the finite intersections of the $\mathfrak{a}_{n, y'}$ are
neighbourhoods of `0` in $A$ and the intersection of all the $\mathfrak{a}_{n, y'}$ is reduced to `0`; the finite
intersections of the $\mathfrak{a}_{n, y'}$ will thus form a fundamental system of neighbourhoods of `0` in $A$
`(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8, where in the proof one may replace the decreasing sequence by any filtered set)`;
one will be able to apply `(11.5.1)`. Now, let $s \in A$ be an element belonging to the kernel of each of the
homomorphisms $A \to \mathcal{O}_{y'}$; the image $s'$ of $s$ in $\Gamma(Y', \mathcal{O}_{Y'})$ is thus a section of
$\mathcal{O}_{Y'}$ over $Y'$ such that $s'_{y'} = 0$ for every $y' \in g^{-1}(y)$; there exists consequently a
neighbourhood $V$ of $g^{-1}(y)$ in $Y'$ such that $s' | V = 0$. But as $g$ is closed, $V$ contains a set of the form
$g^{-1}(V')$, where $V'$ is an open neighbourhood of $y$ in $Y$; now, $Y$ is a local scheme, hence the only
neighbourhood of the closed point $y$ of $Y$ is $Y$ entire, in other words $V' = Y$, $V = Y'$, $s' = 0$, and as $A \to
\Gamma(Y', \mathcal{O}_{Y'})$ is injective by hypothesis, $s = 0$. Q.E.D.

The following particular case of `(11.5.3)` will be useful to us in Chap. V:

**Corollary (11.5.4).**

<!-- label: IV.11.5.4 -->

*Let $f = (\psi, \theta) : X \to Y$ be a proper morphism of finite presentation, and let $p : X \times_{Y} X \to X$ be
the first projection. Suppose that $\theta : \mathcal{O}_{Y} \to f_{*}(\mathcal{O}_{X})$ is injective. Then for $f$ to
be flat, it is necessary and sufficient that $p$ be so.*

**Proposition (11.5.5).**

<!-- label: IV.11.5.5 -->

*Let $A$ be a ring, $Y = \operatorname{Spec}(A)$, $f : X \to Y$ a morphism locally of finite presentation, $\mathcal{F}$
a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation, $x$ a point of $X$. Let $A \to A'$ be an injective
homomorphism making $A'$ an integral algebra over $A$. Set $Y' = \operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' =
f \times 1$, $\mathcal{F}' = \mathcal{F} \otimes_{Y} \mathcal{O}_{Y'}$. Then, if $\mathcal{F}'$ is $f'$-flat at every
point of $X'$ whose projection in $X$ is equal to $x$, $\mathcal{F}$ is $f$-flat at the point $x$.*

Suppose first that $A'$ is a *finite* $A$-algebra of finite presentation; then the morphism $Y' \to Y$ is proper
`(II, 6.1.11)` and of finite presentation, hence the hypotheses of `(11.5.3)` are verified, whence the conclusion. In
the general case, the proposition will result from this particular case, from the fact that $A'$ is the inductive limit
of its finite sub-$A$-algebras $A'_{\lambda}$, and from the two following lemmas:

**Lemma (11.5.5.1).**

<!-- label: IV.11.5.5.1 -->

*Every finite $A$-algebra $A'$ is an inductive limit of $A$-algebras $A'_{\lambda}$ which are finite and of finite
presentation.*

One argues as in `(1.9.3.1)`. Indeed one has $A' = B/\mathfrak{J}$, where $B$ is a finite $A$-algebra that is a free
$A$-module, and $\mathfrak{J}$ an ideal of $B$ `(1.4.7.1)`. Now, $\mathfrak{J}$ is the inductive limit of the ideals
$\mathfrak{J}_{\lambda} \subset \mathfrak{J}$ of $B$ which are of finite type (and *a fortiori* $A$-modules of finite
type), hence, by the exactness of the functor `lim`, $A'$ is the inductive limit of the $A$-algebras
$B/\mathfrak{J}_{\lambda}$; now, $B/\mathfrak{J}_{\lambda}$ is by definition an $A$-module of finite presentation, hence
also `(1.4.7)` an $A$-algebra of finite presentation.

<!-- original page 154 -->

To apply this lemma to the situation of `(11.5.5)`, one will note moreover that if the homomorphism $A \to A'$ is
injective, so *a fortiori* is $A \to A'_{\lambda}$ for every $\lambda$.

**Lemma (11.5.5.2).**

<!-- label: IV.11.5.5.2 -->

*Let $A$ be a ring, $A'$ an $A$-algebra, $(A'_{\lambda})$ an inductive system of $A$-algebras such that $A' = \lim
A'_{\lambda}$; set $Y = \operatorname{Spec}(A)$, $Y' = \operatorname{Spec}(A')$, $Y'_{\lambda} =
\operatorname{Spec}(A'_{\lambda})$. Let $f : X \to Y$ be a morphism of finite presentation, $\mathcal{F}$ a
quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation; set $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$,
$\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$, $X'_{\lambda} = X \times_{Y} Y'_{\lambda}$, $f'_{\lambda} =
f_{(Y'_{\lambda})}$, $\mathcal{F}'_{\lambda} = \mathcal{F} \otimes_{Y} Y'_{\lambda}$. Let $x$ be a point of $X$ such
that $\mathcal{F}'$ is $f'$-flat at all points $x' \in X'$ above $x$; then there exists $\lambda$ such that
$\mathcal{F}'_{\lambda}$ is $f'_{\lambda}$-flat at every point of $X'_{\lambda}$ above $x$.*

Let $U'$ be the set of $x' \in X'$ such that $\mathcal{F}'$ is $f'$-flat at the point $x'$; one knows `(11.3.1)` that
$U'$ is open in $X'$ since $f'$ is of finite presentation `(1.6.2)`; similarly the set $U'_{\lambda}$ of points of
$X'_{\lambda}$ where $\mathcal{F}'_{\lambda}$ is $f'_{\lambda}$-flat is open in $X'_{\lambda}$, and one knows moreover
`(11.2.6)` that $U'$ is the union of the $v^{-1}_{\lambda}(U'_{\lambda})$, where $v_{\lambda} : X' \to X'_{\lambda}$ is
the canonical projection. Consider the scheme $T = \operatorname{Spec}(k(x))$; set $T' = T \times_{Y} Y'$, $T'_{\lambda}
= T \times_{Y} Y'_{\lambda}$, and let $w_{\lambda} : T' \to T'_{\lambda}$, $g' : T' \to X'$, $g'_{\lambda} :
T'_{\lambda} \to X'_{\lambda}$ be the canonical projections. Set $V'_{\lambda} = g'^{-1}_{\lambda}(U'_{\lambda})$, $V' =
g'^{-1}(U') = \bigcup_{\lambda} w^{-1}_{\lambda}(V'_{\lambda})$. By hypothesis one has (taking `(I, 3.6.1)` into
account) $V' = T'$; as $T'$ is quasi-compact, there exists $\lambda$ such that $w^{-1}_{\lambda}(V'_{\lambda}) = T'$.
One then deduces from `(8.3.3)` applied to the closed quasi-compact parts $T'_{\lambda} - V'_{\lambda}$ of
$T'_{\lambda}$, that there exists $\mu \geq \lambda$ such that $T'_{\mu} = V'_{\mu}$; this means that
$\mathcal{F}'_{\mu}$ is $f'_{\mu}$-flat at all points of $X'_{\mu}$ whose projection in $X$ is $x$. Q.E.D.

### 11.6. Descent of flatness by arbitrary morphisms: case of a unibranch base prescheme

**Theorem (11.6.1).**

<!-- label: IV.11.6.1 -->

*Let $A$ be a local integral domain that is geometrically unibranch `(0, 23.2.1)`, $Y = \operatorname{Spec}(A)$, $f : X
\to Y$ a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite
presentation. Let $A'$ be a local ring, $u : A \to A'$ an injective local homomorphism; set $Y' =
\operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$, $\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$. Let $x$
be a point of $X$ whose projection $f(x) = y$ is the closed point of $Y$, $x'$ a point of $X'$ whose projections in $X$
and $Y'$ are respectively $x$ and the closed point $y'$ of $Y'$. Then, if $\mathcal{F}'$ is $f'$-flat at the point $x'$,
$\mathcal{F}$ is $f$-flat at the point $x$.*

One can restrict to the case where $f$ is of finite presentation, the question being local on $X$. We shall proceed in
several steps.

**I)** *Reduction to the case where $A$ and $A'$ are integrally closed local rings.*

As $u$ is injective and $A$ is integral, there exists a prime ideal $\mathfrak{p}'$ of $A'$ such that
$u^{-1}(\mathfrak{p}') = 0$ $(0_{I}, 1.5.8)$; the composed homomorphism $A \to A' \to A'' = A'/\mathfrak{p}'$ is
therefore injective and local, and if $Y'' = \operatorname{Spec}(A'')$, $X'' = X' \otimes_{A'} A'' = X \times_{Y} Y''$,
$\mathcal{F}'' = \mathcal{F}' \otimes_{A'} A''$, $\mathcal{F}''$ is `Y''`-flat at the points of `X''` above $x'$
`(2.1.4)`; replacing if necessary $A'$ by `A''` and taking `(I, 3.4.7)` into account, one can therefore suppose first
that $A'$ is integral. If $K'$ is the field of fractions of $A'$, there exists then a valuation ring $B'$ in $K'$ which
dominates $A'$; the composed homomorphism $A \to A' \to B'$ being injective and local, the same reasoning as

<!-- original page 155 -->

before allows replacement of $A'$ by $B'$; one can thus suppose the local ring $A'$ integrally closed, with $A$ a local
subring of $A'$ dominated by $A'$. Let `A_1` be the integral closure of $A$; it is clear that $A \subset A_{1} \subset
A'$, and by hypothesis `A_1` is a local ring; if $\mathfrak{m}$, $\mathfrak{m}_{1}$, $\mathfrak{m}'$ are the maximal
ideals of $A$, `A_1`, $A'$, one has $\mathfrak{m} \subset \mathfrak{m}_{1} \subset \mathfrak{m}'$; indeed,
$\mathfrak{m}_{1}$ is the only prime ideal of `A_1` above $\mathfrak{m}$, since `A_1` is a local ring
`(Bourbaki, Alg. comm., chap. V, §2, n° 1, prop. 1)`; as $\mathfrak{m}' \cap A = \mathfrak{m}$, one has $\mathfrak{m}'
\cap A_{1} \cap A = \mathfrak{m}$, hence $\mathfrak{m}' \cap A_{1} = \mathfrak{m}_{1}$. Set $Y_{1} =
\operatorname{Spec}(A_{1})$, $X_{1} = X \times_{Y} Y_{1}$, $f_{1} = f_{(Y_{1})}$, $\mathcal{F}_{1} = \mathcal{F}
\otimes_{Y} Y_{1}$, and let $x_{1}$ be the projection of $x'$ in `X_1`; denote on the other hand by $y_{1}$ the unique
closed point of `Y_1`, so that $y_{1} = f_{1}(x_{1})$. By hypothesis, the morphism $\operatorname{Spec}(k(y_{1})) \to
\operatorname{Spec}(k(y))$ is radicial, whence one concludes, by the transitivity of fibres `(I, 3.6.4)` and
`(I, 3.5.7)`, that the morphism $f^{-1}_{1}(y_{1}) \to f^{-1}(y)$ is radicial, and in particular that $x_{1}$ is the
only point of `X_1` whose projections in $X$ and `Y_1` are respectively $x$ and $y_{1}$; moreover, one has seen that
$y_{1}$ is the only point of `Y_1` whose projection in $Y$ is $y$, hence $x_{1}$ is the only point of `X_1` whose
projection in $X$ is $x$. If one proves that $\mathcal{F}_{1}$ is $f_{1}$-flat at the point $x_{1}$, one can apply
`(11.5.5)`, from which will result the conclusion. One is therefore reduced to the case where $A$ itself is integrally
closed.

**II)** *Reduction to the case where $A$ and $A'$ are local rings of $\mathbb{Z}$-algebras of finite type which are
integrally closed.*

One can consider $A'$ as a filtered inductive limit of its sub-$\mathbb{Z}$-algebras (integral) of finite type
$B_{\lambda}$; moreover, as $A'$ is integrally closed and the integral closure of a $\mathbb{Z}$-algebra of finite type
is also a $\mathbb{Z}$-algebra of finite type `(7.8.3)`, one sees that $A'$ is the inductive limit of its
sub-$\mathbb{Z}$-algebras of finite type $B_{\lambda}$ *integrally closed*; if $\mathfrak{n}_{\lambda} = \mathfrak{m}'
\cap B_{\lambda}$, $A'$ is also the inductive limit of the local subrings $(B_{\lambda})_{\mathfrak{n}_{\lambda}} =
A'_{\lambda}$ dominated by $A'$ `(5.13.3)`. For every $\lambda$, $B_{\lambda} \cap A$ is also the inductive limit of its
sub-$\mathbb{Z}$-algebras of finite type $B_{\alpha \lambda}$, hence $A = \lim_{\alpha, \lambda} B_{\alpha \lambda}$,
and as before one can replace $B_{\alpha \lambda}$ in this formula by its integral closure (contained by hypothesis in
$B_{\lambda} \cap A$), then by the local ring $A_{\alpha \lambda} = (B_{\alpha \lambda})_{\mathfrak{m}_{\alpha
\lambda}}$, where $\mathfrak{m}_{\alpha \lambda} = \mathfrak{m} \cap B_{\alpha \lambda} = \mathfrak{m}'_{\lambda} \cap
B_{\alpha \lambda}$, so that $A_{\alpha \lambda}$ is dominated by $A'_{\lambda}$ and by $A$. Set $Y_{\alpha \lambda} =
\operatorname{Spec}(A_{\alpha \lambda})$; it results from `(8.9.1)` that there exists a sufficiently large couple
$(\alpha, \lambda)$, a morphism $f_{\alpha \lambda} : X_{\alpha \lambda} \to Y_{\alpha \lambda}$ of finite type and a
coherent $\mathcal{O}_{X_{\alpha \lambda}}$-Module $\mathcal{F}_{\alpha \lambda}$ such that $X = X_{\alpha \lambda}
\times_{Y_{\alpha \lambda}} Y$, $f = f_{\alpha \lambda} \times 1_{Y}$, $\mathcal{F} = \mathcal{F}_{\alpha \lambda}
\otimes_{Y_{\alpha \lambda}} Y$; if $x_{\alpha \lambda}$ is the projection of $x$ in $X_{\alpha \lambda}$, it will
suffice to show that $\mathcal{F}_{\alpha \lambda}$ is $f_{\alpha \lambda}$-flat at the point $x_{\alpha \lambda}$. As
$A'$ is the inductive limit of the $A'_{\mu}$ for $\mu \geq \lambda$, $X'$ is the projective limit of $X_{\alpha
\lambda} \times_{Y_{\alpha \lambda}} Y'_{\mu} = X'_{\mu}$, and one has also $\mathcal{F}' = \lim \mathcal{F}'_{\mu}$,
where $\mathcal{F}'_{\mu} = \mathcal{F}_{\alpha \lambda} \otimes_{Y_{\alpha \lambda}} Y'_{\mu}$. Applying `(11.2.6)`,
one sees that one can take $\mu$ large enough that $\mathcal{F}'_{\mu}$ is $Y'_{\mu}$-flat at the point $x'_{\mu}$,
projection of $x'$ in $X'_{\mu}$, and moreover, by construction of the $A'_{\mu}$, the projection of $x'_{\mu}$ in
$Y'_{\mu}$ is the closed point of $Y'_{\mu}$.

**III)** *Reduction to the case where the residue field $k'$ of $A'$ is a finite radicial extension of the residue field
$k$ of $A$.*

One can in the first place repeat the reasoning of part I) of the proof of `(11.4.11)`, taking into account the fact
that $\mathbb{Z}$ is a

<!-- original page 156 -->

Jacobson ring; one reduces thus to the case where $k'$ is a finite extension of $k$, which one will suppose in what
follows. Let `k''` be the largest separable extension of $k$ contained in $k'$, $k_{1}$ a finite Galois extension of $k$
containing `k''`, so that $k'' \otimes_{k} k_{1}$ is a direct product of fields isomorphic to $k_{1}$; as $k'$ is a
radicial extension of `k''`, $k' \otimes_{k} k_{1}$ is thus a direct product of radicial extensions of $k_{1}$. There
exists a local ring `A_1` that is an $A$-algebra and a free $A$-module of finite type, such that $A_{1}/\mathfrak{m}
A_{1}$ is $k$-isomorphic to $k_{1}$ $(0_{III}, 10.3.1.2)$; more precisely, one can suppose that $A_{1} = A[T]/(r)$,
where $r$ is a unitary irreducible separable polynomial of `k[T]` of degree $n$; if $R$ is a unitary polynomial of
`A[T]` whose canonical image is $r$ (and which is therefore of degree $n$), one can take $A_{1} = A[T]/(R)$. Now, if $K$
is the field of fractions of $A$, it is clear that $R$ is an irreducible separable polynomial of `K[T]`; one deduces
from this first that `A_1` is an integral ring whose field of fractions $K_{1} = K[T]/(R)$ is a separable extension of
$K$. Moreover, if $t$ is the canonical image of $T$ in `A_1`, the $t^{j}$ ($0 \leq j < n$) form a basis of the
$A$-module `A_1`, and their images in $k_{1}$ a basis over $k$; one deduces from this that $d =
det(Tr_{A_{1}/A}(t^{i+j}))$ is an element of $A$ whose class in $k$ is $\neq 0$, and which is consequently invertible.
The same reasoning as in `(6.12.4.1, I))` then proves that the morphism $\operatorname{Spec}(A_{1}) \to
\operatorname{Spec}(A)$ is flat and has its fibres regular; one concludes consequently from `(6.5.4, (ii))` that `A_1`
is integrally closed. Consider then the ring $A'_{1} = A' \otimes_{A} A_{1}$; it is a free $A'$-module of finite type,
hence a semi-local ring `(Bourbaki, Alg. comm., chap. IV, §2, n° 5, cor. 3 of prop. 9)`; moreover, the maximal ideals of
this finite $A'$-algebra are all above the maximal ideal $\mathfrak{m}'$ of $A'$, and *a fortiori* contain $\mathfrak{m}
A'_{1}$. But $A'_{1}/\mathfrak{m} A'_{1} = (A'/\mathfrak{m} A') \otimes_{k} k_{1}$, and as $k_{1}$ is a separable finite
extension of $k$, the radical of $A'_{1}/\mathfrak{m} A'_{1}$ equals $(\mathfrak{m}'/\mathfrak{m} A') \otimes_{k} k_{1}$
`(Bourbaki, Alg., chap. VIII, §7, n° 2, cor. 2 of prop. 3)`; if $\mathfrak{n}_{i}$ ($1 \leq i \leq r$) are the maximal
ideals of $A'_{1}$, the fields $A'_{1}/\mathfrak{n}_{i}$ are thus the fields composing the algebra $k' \otimes_{k}
k_{1}$, in other words they are *finite radicial extensions of $k_{1}$*. Moreover, as $A \to A'$ is an injective
homomorphism, so is $A_{1} \to A'_{1}$, `A_1` being a flat $A$-module; the canonical homomorphism $A'_{1} \to
\prod^{r}_{i=1} (A'_{1})_{\mathfrak{n}_{i}}$ being also injective `(Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1)`,
so is the composite $A_{1} \to \prod^{r}_{i=1} (A'_{1})_{\mathfrak{n}_{i}}$. But `A_1` is integral, and the kernels of
the homomorphisms $A_{1} \to (A'_{1})_{\mathfrak{n}_{i}}$ are finite in number; as their intersection is null, one of
them is already null. In other words, there is a $B_{1} = (A'_{1})_{\mathfrak{n}_{i}}$ such that the homomorphism $A_{1}
\to B_{1}$ is injective and local. Set $Y'_{1} = \operatorname{Spec}(B_{1})$, $X'_{1} = X' \times_{Y'} Y'_{1}$;
$\mathcal{F}'_{1} = \mathcal{F}' \otimes_{Y'} Y'_{1}$ is $Y'_{1}$-flat at all points of $X'_{1}$ above $x'$; moreover
the maximal ideal of `B_1` is the only one above $\mathfrak{m}'$, hence all these points have as projection in $Y'_{1}$
the closed point $y'_{1}$. Let $x'_{1}$ be one of these points. Set on the other hand $Y_{1} =
\operatorname{Spec}(A_{1})$, $X_{1} = X \times_{Y} Y_{1}$, $\mathcal{F}_{1} = \mathcal{F} \otimes_{Y} Y_{1}$; if $x_{1}$
is the projection of $x'_{1}$ in `X_1`, the projection of $x_{1}$ in $X$ is $x$ and its projection in `Y_1` is the
closed point $y_{1}$. If one proves that $(\mathcal{F}_{1})_{x_{1}}$ is a flat $\mathcal{O}_{y_{1}}$-module, it will
result that $\mathcal{F}_{x}$ is a flat $\mathcal{O}_{y}$-module; indeed $\mathcal{O}_{y_{1}}$ is a flat
$\mathcal{O}_{y}$-module, hence $(\mathcal{F}_{1})_{x_{1}}$ is a flat $\mathcal{O}_{y}$-module $(0_{I}, 6.2.1)$.

<!-- original page 157 -->

But $(\mathcal{F}_{1})_{x_{1}} = \mathcal{F}_{x} \otimes_{\mathcal{O}_{x}} \mathcal{O}_{x_{1}}$ and
$\mathcal{O}_{x_{1}}$ is a faithfully flat $\mathcal{O}_{x}$-module; hence `(2.2.11, (iii))` $\mathcal{F}_{x}$ is a flat
$\mathcal{O}_{x}$-module. As $X'_{1} = X_{1} \times_{Y_{1}} Y'_{1}$, $\mathcal{F}'_{1} = \mathcal{F}_{1} \otimes_{Y_{1}}
Y'_{1}$, one is indeed reduced to the situation of the statement `(11.6.1)`, with $A$ and $A'$ replaced respectively by
`A_1` and `B_1`.

**IV)** *End of the proof.* — One is finally reduced to proving `(11.6.1)` under the following supplementary hypotheses:

(i) $A$ and $A'$ are local rings of $\mathbb{Z}$-algebras of finite type (hence excellent rings `(7.8.3)`);

(ii) $A$ is integrally closed;

(iii) the residue field $k'$ of $A'$ is a finite radicial extension of the residue field $k$ of $A$.

One knows then (`(7.8.3)` and `(2.3.8)`) that under conditions (i) and (ii), if $\mathfrak{m}$ and $\mathfrak{m}'$ are
the maximal ideals of $A$ and $A'$ respectively, the $\mathfrak{m}$-adic topology on $A$ is induced by the
$\mathfrak{m}'$-adic topology of $A'$. The completion $\hat{u} : \hat{A} \to \hat{A}'$ is therefore an injective
homomorphism. On the other hand, as the morphism $\operatorname{Spec}(k') \to \operatorname{Spec}(k)$ is radicial, so is
the morphism $f'^{-1}(y') \to f^{-1}(y)$ `(I, 3.5.7)`, and there is therefore only one point $x'$ of $X'$ whose
projections in $X$ and $Y'$ are $x$ and $y'$ respectively. One can therefore apply the result of `(11.5.2)`. Q.E.D.

**Corollary (11.6.2).**

<!-- label: IV.11.6.2 -->

*Let $A$ be a unibranch local integral ring, $Y = \operatorname{Spec}(A)$, $f : X \to Y$ a morphism locally of finite
presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite presentation. Let $A'$ be a local ring,
$A \to A'$ an injective local homomorphism; set $Y' = \operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$,
$\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$. Let $x$ be a point of $X$ whose projection $f(x) = y$ is the closed point
of $Y$; suppose that $\mathcal{F}'$ is $f'$-flat at all points $x'$ of $X'$ whose projections in $X$ and $Y'$ are
respectively $x$ and the closed point $y'$ of $Y'$. Then $\mathcal{F}$ is $f$-flat at the point $x$.*

One can indeed retake part I) of the proof of `(11.6.1)`, which proves (with the same notations) that if
$\mathcal{F}_{1}$ is $f_{1}$-flat at all points $x_{1}$ of `X_1` whose respective projections in $X$ and `Y_1` are $x$
and $y_{1}$, then $\mathcal{F}$ is $f$-flat at the point $x$; one is thus reduced to the case where $A$ is integrally
closed, hence geometrically unibranch, and the conclusion then results from `(11.6.1)`.

### 11.7. Counter-examples

**(11.7.1)** Let us consider first the case where $A$ is a local artinian ring, and where the hypotheses of `(11.4.11)`
are satisfied except condition (ii) concerning the residue field $k$ of $A$. We shall see that the conclusion of
`(11.4.11)` may then fail. Let $k$ be a field admitting a Galois extension $k'$ of degree $[k' : k] > 1$, and denote by
$\Gamma$ the Galois group of $k'$. Let $A$ be a $k$-algebra having a basis of 3 elements `1`, $a$, $b$ with the
multiplication table $a^{2} = ab = ba = b^{2} = 0$, so that $A$ is a local artinian ring whose maximal ideal
$\mathfrak{m} = ka + kb$ is of square zero. Let $A' = A \otimes_{k} k'$, which is a $k'$-algebra of basis `1`, $a$, $b$,
a local artinian ring of maximal ideal $\mathfrak{m}' = k'a + k'b = \mathfrak{m} A'$, of square zero; $A$ identifies
canonically with a subring of $A'$. Let $\mathfrak{J}$ be the sub-$A'$-vector space of $\mathfrak{m}'$ generated by $a +
\gamma b$, where $\gamma \in k'$ does not belong to $k$; it is clear that $\mathfrak{J}$ is an ideal of $A'$. Set $B =
A'/\mathfrak{J}$; this is an artinian ring which is a non-flat $A$-module; otherwise
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, $B$ would be a free $A$-module; as $A'$ is also a free
$A$-module, and the canonical homomorphism $A/\mathfrak{m} A' \to B/\mathfrak{m} B$ is bijective, the canonical
homomorphism $A' \to B = A'/\mathfrak{J}$ would also

<!-- original page 158 -->

be bijective `(loc. cit., n° 2, cor. of prop. 6)`, which is absurd. In other words, if one sets $Y =
\operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, $\mathcal{O}_{X}$ is not $Y$-flat at the unique point $x$ of $X$.
But let $A_{1} = B$, $Y_{1} = \operatorname{Spec}(A_{1})$, and consider the canonical homomorphism $A \to A_{1}$, which
is local and injective since $\mathfrak{J} \cap A = 0$; if $B_{1} = B \otimes_{A} A_{1} = B \otimes_{A} B$, we shall see
that there exists a point of $X_{1} = X \times_{Y} Y_{1} = \operatorname{Spec}(B_{1})$ where $\mathcal{O}_{X_{1}}$ is
`Y_1`-flat. For this, remark that one has $B \otimes_{A} B = (A' \otimes_{A} A')/(Im(\mathfrak{J} \otimes_{A} A') +
Im(A' \otimes_{A} \mathfrak{J}))$. Now the structure of $C' = A' \otimes_{A} A'$ is obtained easily; one considers the
$A$-algebra product $C = \prod_{\sigma \in \Gamma} A'_{\sigma}$, where all the $A'_{\sigma}$ are equal to $A'$, and the
canonical map $\phi : A' \otimes_{A} A' \to C$ such that $\phi(x \otimes y) = (\sigma(x) y)_{\sigma \in \Gamma}$ (the
group $\Gamma$ operating canonically on $A'$); by passage to quotients, one deduces a homomorphism $C'/\mathfrak{m} C'
\to C/\mathfrak{m} C$ which is none other than the canonical homomorphism $k' \otimes_{k} k' \to \prod_{\sigma}
k'_{\sigma}$ (with $k'_{\sigma} = k'$ for all $\sigma \in \Gamma$); one knows that this last is bijective
`(Bourbaki, Alg., chap. VIII, §8, prop. 4)`, hence so is $\phi$, since $C'$ and $C$ are free $A$-modules
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. of prop. 6)`. From the preceding, it follows that $B \otimes_{A} B$ is
a semi-local $A$-algebra, direct product of the local $A$-algebras $A'/(\sigma(\mathfrak{J}) + \mathfrak{J})$. The one
of these algebras corresponding to the identity of $\Gamma$ is isomorphic to $A'/\mathfrak{J}$, hence is a flat
`A_1`-module; but as $\gamma \notin k$, there exists at least one $\sigma \in \Gamma$ such that $\sigma(\mathfrak{J})
\neq \mathfrak{J}$; then $\sigma(\mathfrak{J}) + \mathfrak{J} = \mathfrak{m}'$, and $A'/\mathfrak{m}'$ is not a flat
$(A'/\mathfrak{J})$-module, since it is the quotient of $A'/\mathfrak{J}$ by a non-null ideal.

**(11.7.2)** We shall now show that the result of `(11.5.4)` loses its validity when one no longer supposes $f$ to be a
proper morphism (and *a fortiori* `(11.5.3)` ceases to be exact when one no longer supposes $g$ proper). Let $k$ be a
field, `A_0` the polynomial ring `k[S, T]`, $A$ the quotient ring $A_{0}/A_{0} ST$; $Y = \operatorname{Spec}(A)$ is
therefore the reducible curve formed by the two "coordinate axes" in the affine plane $Y_{0} =
\operatorname{Spec}(A_{0})$. The ring $A$ admits two minimal prime ideals $\mathfrak{p}_{1} = A_{0} S/A_{0} ST$,
$\mathfrak{p}_{2} = A_{0} T/A_{0} ST$, and as $A$ is reduced, it embeds canonically into $B = B_{1} \oplus B_{2}$, where
$B_{1} = A/\mathfrak{p}_{1}$, $B_{2} = A/\mathfrak{p}_{2}$; moreover, `B_1` identifies with `k[T]` and `B_2` with
`k[S]`, hence they are integrally closed integral rings and consequently $Z = \operatorname{Spec}(B)$ is none other than
the normalization of the prescheme $Y$ relative to $R(Y)$ `(II, 6.3.8)`, the sum of the two schemes $Z_{1} =
\operatorname{Spec}(B_{1})$, $Z_{2} = \operatorname{Spec}(B_{2})$. Denote by $y$ the "double point" of $Y$,
corresponding to the maximal ideal $\mathfrak{p}_{1} + \mathfrak{p}_{2} = \mathfrak{m}$ of $A$, by $z_{1}$ and $z_{2}$
the points of $Z$ which project to $y$, corresponding respectively to the maximal ideals $\mathfrak{n}_{1} = (T)$ and
$\mathfrak{n}_{2} = (S)$ of `B_1` and `B_2`. We shall denote by $X$ the subprescheme of $Z$ induced on the complement of
$z_{2}$ in $Z$; one has thus $X = \operatorname{Spec}(B_{1} \oplus (B_{2})_{S})$; it is immediate that the homomorphism
$A \to A' = B_{1} \oplus (B_{2})_{S}$ is injective, but the corresponding morphism $f : X \to Y$ is *not closed* (for
$f(Z_{2} - {z_{2}})$ is not closed in $Y$, although $Z_{2} - {z_{2}}$ is closed in $X$); *a fortiori* it is not proper.
We shall now see that $f$ is not flat at the point $z_{1}$; it will suffice to show $(0_{I}, 6.6.2)$ that
$\mathcal{O}_{z_{1}}$ is not a faithfully flat $\mathcal{O}_{y}$-module, and for this it suffices to see that the
canonical homomorphism $\mathcal{O}_{y} \to \mathcal{O}_{z_{1}}$ is not injective; but this is immediate since
$\mathcal{O}_{z_{1}}$ is an integral ring, while $\mathcal{O}_{y}$ has zero-divisors. However, the first projection $p :
X \times_{Y} X \to X$ *is an isomorphism*: indeed, one has $B_{1} \otimes_{A} B_{1} = (A/\mathfrak{p}_{1}) \otimes_{A}
(A/\mathfrak{p}_{1}) = A/\mathfrak{p}_{1}$; $(B_{2})_{S} \otimes_{A} (B_{2})_{S} = (B_{2} \otimes_{A} B_{2})_{S} =
(B_{2})_{S}$ for the same reason, and finally $B_{1} \otimes_{A} (B_{2})_{S} = 0$, since the canonical image of $S$ in
`B_1` is null.

**(11.7.3)** The preceding example can be generalized: one considers over a field $k$ a reduced algebraic curve $Y$
admitting a single "ordinary double point" $y$ (a notion to be defined later in general), and its normalization $Z$, so
that the morphism $g : Z \to Y$ is finite, that the restriction of $g$ to $Z - g^{-1}(y)$ is an isomorphism on $Y -
{y}$, and that $g^{-1}(y)$ reduces to two "simple" points $z_{1}$, $z_{2}$; moreover the prescheme $g^{-1}(y)$ is the
sum of two preschemes $\operatorname{Spec}(k(z_{1}))$, $\operatorname{Spec}(k(z_{2}))$, canonically isomorphic to
$\operatorname{Spec}(k(y))$. Let $X$ be the subprescheme of $Z$ induced on the open set $Z - {z_{2}}$; the morphism $f :
X \to Y$, restriction of $g$ to $X$, is not proper, otherwise `(II, 5.4.3)` so would the canonical injection $j : X \to
Z$, which is not closed. The morphism $f$ is radicial, for every $y' \in Y$, the fibre $f^{-1}(y')$ comprises only one
point $x'$, $k(y') \to k(x')$ being an isomorphism; one concludes first that the diagonal morphism $\Delta_{f} : X \to X
\times_{Y} X$ is bijective `(1.7.7.1)` and on the other hand, as $f$ is unramified `(17.4.2, d')`, $\Delta_{f}$ is an
open immersion `(17.4.2, b')`; consequently $\Delta_{f}$ is an isomorphism, and the first projection $p : X \times_{Y} X
\to X$ the inverse isomorphism. However $f$ is not flat at the point $z_{1}$; otherwise $\mathcal{O}_{z_{1}}$ would be a
faithfully flat $\mathcal{O}_{y}$-module $(0_{I}, 6.6.2)$, and as $\mathcal{O}_{y}$ contains two distinct minimal prime
ideals $\mathfrak{p}_{1}$, $\mathfrak{p}_{2}$ (corresponding to the two "branches" of $Y$ at the point $y$) there would
exist in $\mathcal{O}_{z_{1}}$ two distinct prime ideals whose inverse images by $u : \mathcal{O}_{y} \to
\mathcal{O}_{z_{1}}$ would be $\mathfrak{p}_{1}$ and $\mathfrak{p}_{2}$ $(0_{I}, 6.5.1)$; but this is absurd, for
$\mathcal{O}_{z_{1}}$ has only two distinct prime ideals, `0` and the maximal ideal $\mathfrak{m}_{1}$, and
$u^{-1}(\mathfrak{m}_{1})$ is the maximal ideal $\mathfrak{m}$ of $\mathcal{O}_{y}$.

**(11.7.4)** One will note that in the preceding example the homomorphism $u$ is injective when $Y$ is irreducible (one
may for example take $Y = \operatorname{Spec}(k[S, T]/(S(S^{2} + T^{2}) - (S^{2} - T^{2})))$, "cubic with a double
point"); one can in this case (replacing $Y$ by an affine neighbourhood of $y$) suppose that $Y =
\operatorname{Spec}(A)$, where $A$ is integral, whence $Z = \operatorname{Spec}(B)$, where $B$ is the integral closure
of $A$; as $B$, $\mathcal{O}_{y}$ and $\mathcal{O}_{z_{1}}$ then identify with subrings of

<!-- original page 159 -->

the field of fractions of $A$, $u$ is obviously injective. One will note on the contrary that the homomorphism
$\hat{u} : \hat{\mathcal{O}}_{y} \to \hat{\mathcal{O}}_{z_{1}}$ is not injective, for $\hat{\mathcal{O}}_{z_{1}}$ is an
integral local ring ($z_{1}$ being a simple point), while $\hat{\mathcal{O}}_{y}$ has two distinct minimal prime ideals
(corresponding to the two "branches" of $Y$) and thus has zero-divisors. This gives an example showing that in the
statement `(11.5.2)`, one cannot replace the hypothesis that `û` is injective by the hypothesis that $u$ itself is
injective, even when $A'$ is a local ring. It suffices indeed to take (with the preceding notations)
$A = \mathcal{O}_{y}$, $A' = \mathcal{O}_{z_{1}}$, $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(A')$; the
reasoning of `(11.7.3)` still proves that the first projection $p : X \times_{Y} X \to X$ is an isomorphism, although
$f$ is not flat at the point $z_{1}$.

**(11.7.5)** The examples of `(11.7.2)` and `(11.7.3)` explain the restriction to unibranch local rings in `(11.6.1)`
and `(11.6.2)`. We shall now see that in `(11.6.1)` one cannot weaken the hypothesis on $A$ by supposing only $A$
unibranch. Consider indeed the complete local integral ring $A = \mathbb{R}[[U, V]]/(U^{2} + V^{2})$ which is unibranch
but not geometrically unibranch `(6.5.11)`. One knows `(loc. cit.)` that if $u$, $v$ are the images of $U$ and $V$ in
$A$, the integral closure of $A$ is $\bar{A} = A[t]$ with $t = v/u$, such that $t^{2} = -1$, so that `Ā` is isomorphic
to $\mathbb{C}[[U]]$. Set $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(\bar{A})$ (normalization of $Y$
`(II, 6.3.8)`) and let $y$ and $x$ be the closed points of $Y$ and $X$ respectively; we shall show that for a suitable
local $A$-algebra $A'$, if one sets $Y' = \operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, and if $y'$ denotes the
closed point of $Y'$, $\mathcal{O}_{X'}$ is $Y'$-flat at a point of $X'$ whose projections in $X$ and $Y'$ are
respectively $x$ and $y'$, but is not $Y'$-flat at all points having these projections; it will follow `(2.1.4)` that
$\mathcal{O}_{X}$ is not $Y$-flat at the point $x$ (which is otherwise trivial *a priori*, `Ā` not being a free
$A$-module).

Let $B = A \otimes_{\mathbb{R}} \mathbb{C}$, isomorphic to $\mathbb{C}[[U, V]]/(U + iV)(U - iV)$; $B$ has two minimal
prime ideals $\mathfrak{p}'$, $\mathfrak{p}''$ generated respectively by $u + iv$ and $u - iv$, and $\mathfrak{n} =
\mathfrak{p}' + \mathfrak{p}''$ is the maximal ideal of the complete local ring $B$. Let $\bar{B} = \bar{A}
\otimes_{\mathbb{R}} \mathbb{C}$; $\bar{B}$ is a direct product of two algebras isomorphic to $\mathbb{C}[[U]]$,
generated by the idempotents $e' = (1 \otimes 1 + t \otimes i)/2$ and $e'' = (1 \otimes 1 - t \otimes i)/2$; as the
homomorphism $A \to \bar{A}$ is injective, so is $B \to \bar{B}$, and the images of $u + iv$ and of $u - iv$ by this
injection are respectively `u e'` and `u e''`; one concludes at once that $\bar{B}$ identifies canonically with
$(B/\mathfrak{p}') \oplus (B/\mathfrak{p}'')$. This being so, take for $A'$ the local ring $B/\mathfrak{p}'$; then
$\bar{A} \otimes_{A} A'$ identifies with $\bar{B} \otimes_{B} A'$. But one has $(B/\mathfrak{p}') \otimes_{B}
(B/\mathfrak{p}') = B/\mathfrak{p}'$ and $(B/\mathfrak{p}') \otimes_{B} (B/\mathfrak{p}'') = B/\mathfrak{n}$, hence
$\bar{A} \otimes_{A} A'$ is isomorphic to $A' \oplus (B/\mathfrak{n})$. This establishes our assertion, for
$B/\mathfrak{n} = A'/(\mathfrak{n}/\mathfrak{p}')$ is not a flat $A'$-module (otherwise it would be a free $A'$-module
`(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 5)`, which is absurd).

### 11.8. A valuative criterion of flatness

**Theorem (11.8.1).**

<!-- label: IV.11.8.1 -->

*Let $f : X \to Y$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation, $x$ a point of $X$, $y = f(x)$. Suppose the local ring $\mathcal{O}_{y}$ integral (resp. reduced
and Noetherian). For $\mathcal{F}$ to be $f$-flat at the point $x$, it is necessary and sufficient that, for every
valuation ring (resp. every discrete valuation ring) $A'$ and every local homomorphism $\mathcal{O}_{y} \to A'$, the
following condition be satisfied: setting $Y' = \operatorname{Spec}(A')$, $X' = X \times_{Y} Y'$, $f' = f_{(Y')}$, the
$\mathcal{O}_{X'}$-Module $\mathcal{F}' = \mathcal{F} \otimes_{Y} Y'$ is $f'$-flat at all points $x'$ of $X'$ whose
respective projections in $X$ and $Y'$ are $x$ and the closed point $y'$ of $Y'$.*

The condition being obviously necessary `(2.1.4)`, it remains to prove that it is sufficient. One can evidently
(`(I, 3.6.5)` and `(I, 2.4.4)`) restrict to the case where $Y = \operatorname{Spec}(A)$ is the spectrum of a local ring
$A$ and $y$ the closed point of $Y$.

**(i)** *Case where $A$ is integral.* — Let $K$ be the field of fractions of $A$, `A_1` the integral closure of $A$;
setting $Y_{1} = \operatorname{Spec}(A_{1})$, $X_{1} = X \times_{Y} Y_{1}$, $f_{1} = f_{(Y_{1})}$, it suffices, by
virtue of `(11.5.5)`, to show that $\mathcal{F}_{1} = \mathcal{F} \otimes_{Y} Y_{1}$ is $f_{1}$-flat at all points
$x_{1}$ of `X_1` of which $x$ is the projection in $X$. Now, if $f_{1}(x_{1}) = y_{1}$, one has $y_{1} =
\mathfrak{m}_{1}$, where $\mathfrak{m}_{1}$ is a prime ideal

<!-- original page 160 -->

of `A_1` whose trace $\mathfrak{m} = \mathfrak{m}_{1} \cap A$ on $A$ is the maximal ideal of $A$ ($\mathfrak{m}_{1}$ is
moreover necessarily a maximal ideal). Let $A'$ be a valuation ring for $K$ which dominates $\mathcal{O}_{y_{1}} =
(A_{1})_{\mathfrak{m}_{1}}$; the homomorphism $A \to \mathcal{O}_{y_{1}}$ being local, so is $A \to A'$. There exists
then at least one point $x' \in X'$ whose projections in `X_1` and $Y'$ are respectively $x_{1}$ and $y'$ `(I, 3.4.7)`;
as by hypothesis $\mathcal{F}'$ is $f'$-flat at the point $x'$, and $\mathcal{O}_{y_{1}}$ is integrally closed, one can
apply `(11.6.1)`, and one deduces that $\mathcal{F}_{1}$ is $f_{1}$-flat at the point $x_{1}$, whence the theorem in
this case.

**(ii)** *Case where $A$ is reduced and Noetherian.* — Let $\mathfrak{p}_{i}$ ($1 \leq i \leq m$) be the minimal ideals
of $A$; as $A$ is reduced, it identifies canonically with a subring of the product of the $A_{i} = A/\mathfrak{p}_{i}$,
which are Noetherian local rings; setting $Y_{i} = \operatorname{Spec}(A_{i})$, $X_{i} = X \times_{Y} Y_{i}$, $f_{i} =
f_{(Y_{i})}$, it results from `(11.5.2)` that it suffices to show that for each $i$, $\mathcal{F}_{i} = \mathcal{F}
\otimes_{Y} \mathcal{O}_{Y_{i}}$ is $f_{i}$-flat at every point $x_{i}$ of $X_{i}$ whose projections in $X$ and $Y_{i}$
are $x$ and the closed point $y_{i}$ of $Y_{i}$ respectively. Now, as $A_{i}$ is a Noetherian integral local ring, there
exists in its field of fractions $K_{i}$ a subring $A''_{i}$ containing $A_{i}$, that is a finite $A$-algebra (hence a
Noetherian semi-local ring) and whose local rings are geometrically unibranch (`(6.15.5)` and `(0, 23.2.5)`). As the
maximal ideals of $A''_{i}$ are then necessarily above the maximal ideal of $A_{i}$, one deduces still from `(I, 3.4.7)`
and from `(11.5.2)` that it suffices, setting $Y''_{i} = \operatorname{Spec}(A''_{i})$, $X''_{i} = X \times_{Y}
Y''_{i}$, $f''_{i} = f_{(Y''_{i})}$, to prove that $\mathcal{F}''_{i} = \mathcal{F} \otimes_{Y} Y''_{i}$ is
$f''_{i}$-flat at every point $x''_{i}$ of $X''_{i}$ whose projections in $X$ and $Y''_{i}$ are $x$ and the closed point
$y''_{i}$ of $Y''_{i}$ respectively. Now, let $A'$ be a discrete valuation ring for $K_{i}$ dominating
$\mathcal{O}_{y''_{i}}$, and let $x'$ be a point of $X'$ whose projections in $X''_{i}$ and in $Y'$ are $x''_{i}$ and
$y'$ respectively `(I, 3.4.7)`; as $\mathcal{O}_{y''_{i}}$ is geometrically unibranch, one can still apply `(11.6.1)`
and one deduces that $\mathcal{F}''_{i}$ is $f''_{i}$-flat at the point $x''_{i}$.

**Remarks (11.8.2).**

<!-- label: IV.11.8.2 -->

*(i) In the statement of `(11.8.1)`, one can restrict to supposing that the condition on $\mathcal{F}'$ is verified for
complete valuation rings $A'$ whose residue field is algebraically closed.* One knows indeed that every valuation ring
$A'$ is dominated by such a ring `A''` `(II, 7.1.2)`, and that if $A'$ is a discrete valuation ring, one can suppose
that so is `A''` $(0_{III}, 10.3.1)$.

*(ii) The proof of `(11.8.1)` simplifies when one supposes not only that $A$ is integral and Noetherian, but that its
completion `Â` is also integral.* Replacing $X$ by $X \otimes_{A} \hat{A}$ and reasoning as in the proof of `(11.5.3)`,
one can in this case reduce to proving `(11.8.1)` when $A = \mathcal{O}_{y}$ is integral, Noetherian and complete. Now,
one knows `(II, 7.1.7)` that such a ring $A$ is dominated by a complete discrete valuation ring; the conclusion
therefore results directly from `(11.5.2)`.

### 11.9. Separating and universally separating families of homomorphisms of sheaves of modules

**(11.9.1)** Let $X$ be a prescheme, $(f_{\lambda})_{\lambda \in L}$ a family of morphisms $f_{\lambda} : Z_{\lambda}
\to X$, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module; for every $\lambda \in L$, suppose given a
quasi-coherent $\mathcal{O}_{Z_{\lambda}}$-Module $\mathcal{G}_{\lambda}$ and a homomorphism

$$ (11.9.1.1) u_{\lambda} : \mathcal{F} \to (f_{\lambda})_{*}(\mathcal{G}_{\lambda}). $$

<!-- original page 161 -->

One says that the family $(u_{\lambda})$ (or the corresponding family of $u'_{\lambda} : f^{*}_{\lambda}(\mathcal{F})
\to \mathcal{G}_{\lambda}$) is **separating** if the intersection of the kernels of the $u_{\lambda}$ is null. In other
words, this means that for every open set $U$ of $X$, and every section $t$ of $\mathcal{F}$ over $U$, such that, for
every $\lambda$, the section $u_{\lambda}(t)$ (which, by definition, is a section of $\mathcal{G}_{\lambda}$ over
$f^{-1}_{\lambda}(U)$) is null, then $t$ is itself null.

**(11.9.2)** With the notations of `(11.9.1)`, let $M$ be a second index set; for every $\lambda \in L$, let
$(g_{\lambda \mu})_{\mu \in M}$ be a family of morphisms $g_{\lambda \mu} : Z_{\lambda \mu} \to Z_{\lambda}$; for every
couple $(\lambda, \mu)$, suppose given a quasi-coherent $\mathcal{O}_{Z_{\lambda \mu}}$-Module $\mathcal{G}_{\lambda
\mu}$ and a homomorphism $v_{\lambda \mu} : \mathcal{G}_{\lambda} \to (g_{\lambda \mu})_{*}(\mathcal{G}_{\lambda \mu})$;
set $h_{\lambda \mu} = f_{\lambda} \circ g_{\lambda \mu} : Z_{\lambda \mu} \to X$ and consider the composed homomorphism

```text
  ℱ ─u_λ─→ (f_λ)_*(𝒢_λ) ─(f_λ)_*(v_{λμ})─→ (h_{λμ})_*(𝒢_{λμ}).
```

Suppose that, for every $\lambda \in L$, the family $(v_{\lambda \mu})_{\mu \in M}$ is separating: then so is the family
of $(f_{\lambda})_{*}(v_{\lambda \mu})$ ($\mu \in M$), as one sees at once. One concludes that, for the family
$(u_{\lambda})$ to be separating, it is necessary and sufficient that the family $((f_{\lambda})_{*}(v_{\lambda \mu})
\circ u_{\lambda})_{(\lambda, \mu) \in L \times M}$ be so.

**(11.9.3)** To verify that the family $(u_{\lambda})$ is separating (with the notations of `(11.9.1)`), one can
evidently reduce first to the case where $X$ is affine, the property being local on $X$. One can moreover suppose that
$Z_{\lambda} = X$ for every $\lambda \in L$. Indeed, let $M$ be an index set, sum of a family $(M_{\lambda})_{\lambda
\in L}$, and for every $\lambda \in L$, let $(Y_{\lambda \mu})_{\mu \in M_{\lambda}}$ be an affine open cover of
$Z_{\lambda}$; let $j_{\lambda \mu} : Y_{\lambda \mu} \to Z_{\lambda}$ be the canonical injection and set
$\mathcal{G}_{\lambda \mu} = j^{*}_{\lambda \mu}(\mathcal{G}_{\lambda}) = \mathcal{G}_{\lambda} | Y_{\lambda \mu}$. If
one considers the canonical homomorphism $v_{\lambda \mu} = \rho_{\mathcal{G}_{\lambda}} : \mathcal{G}_{\lambda} \to
(j_{\lambda \mu})_{*}(j^{*}_{\lambda \mu}(\mathcal{G}_{\lambda})) = (j_{\lambda \mu})_{*}(\mathcal{G}_{\lambda \mu})$
relative to $j_{\lambda \mu}$ $(0_{I}, 4.4.3.2)$, it is immediate that for each $\lambda \in L$, the family $(v_{\lambda
\mu})_{\mu \in M_{\lambda}}$ is separating. By virtue of `(11.9.2)`, one is therefore reduced to proving that the family
of composed homomorphisms $((f_{\lambda})_{*}(v_{\lambda \mu})) \circ u_{\lambda}$ is separating, in other words one is
reduced to the case where the $Z_{\lambda}$ are affine. But then the $(f_{\lambda})_{*}(\mathcal{G}_{\lambda})$ are
quasi-coherent $\mathcal{O}_{X}$-Modules `(I, 1.6.2)` and by virtue of the definition, one can replace the $Z_{\lambda}$
by $X$ and the $\mathcal{G}_{\lambda}$ by the $(f_{\lambda})_{*}(\mathcal{G}_{\lambda})$, whence our assertion.

One will note in addition that if $L$ is *finite* and the $f_{\lambda}$ quasi-compact, one can, in the preceding
reduction, suppose that the $M_{\lambda}$ are also finite, hence one is in this case reduced to verifying that a finite
family of homomorphisms of $\mathcal{F}$ into quasi-coherent $\mathcal{O}_{X}$-Modules is separating.

**(11.9.4)** Let us therefore consider the case where $Z_{\lambda} = X$ for every $\lambda$, and where $X =
\operatorname{Spec}(A)$ is affine; then one has $\mathcal{F} = \tilde{M}$ and $\mathcal{G}_{\lambda} =
\tilde{N}_{\lambda}$, where $M$ and $N_{\lambda}$ are $A$-modules, and $u_{\lambda} = \tilde{\phi}_{\lambda}$, where the
$\phi_{\lambda} : M \to N_{\lambda}$ are $A$-homomorphisms. To say that the family $(u_{\lambda})$ is separating means
then that, for every $s \in A$, the intersection of the kernels of the $(\phi_{\lambda})_{s} : M_{s} \to
(N_{\lambda})_{s}$ is reduced to `0`. One says then also that the family $(\phi_{\lambda})$ is *separating*. One will
note that if $L$ is finite, it amounts to the same to say that the intersection of the kernels of the $\phi_{\lambda}$
is `0`, for one has then $\bigcap_{\lambda \in L} Ker((\phi_{\lambda})_{s}) = (\bigcap_{\lambda \in L}
Ker(\phi_{\lambda}))_{s}$ $(0_{I}, 1.3.2)$. But this relation is no longer exact in general when $L$ is infinite, and
the fact that the intersection of the kernels of the $\phi_{\lambda}$ is `0` *does not entail*, in general,

<!-- original page 162 -->

that the family $(\phi_{\lambda})$ is separating. For example, suppose that $A$ is a discrete valuation ring of maximal
ideal $\mathfrak{m}$, and consider the family of homomorphisms $\phi_{k} : A \to A/\mathfrak{m}^{k}$, whose intersection
of kernels $\mathfrak{m}^{k}$ is reduced to `0`; this family is however not separating, for the fibres of all the
$\mathfrak{m}^{k}$ at the generic point $x$ of $X = \operatorname{Spec}(A)$ (which is open in $X$) are equal to
$\mathcal{O}_{x} = k(x)$, the field of fractions of $A$, and their intersection is therefore not reduced to `0`.

**(11.9.5)** We shall be principally concerned in what follows with the problem of base change for separating families.
The notations being those of `(11.9.1)`, consider a morphism $g : X' \to X$ and set $\mathcal{F}' = \mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'} = g^{*}(\mathcal{F})$, and, for every $\lambda$, $Z'_{\lambda} = Z_{\lambda}
\times_{X} X'$, $f'_{\lambda} = f_{\lambda} \times 1$, $\mathcal{G}'_{\lambda} = \mathcal{G}_{\lambda}
\otimes_{\mathcal{O}_{Z_{\lambda}}} \mathcal{O}_{Z'_{\lambda}} = g'^{*}_{\lambda}(\mathcal{G}_{\lambda})$, where
$g'_{\lambda} : Z'_{\lambda} \to Z_{\lambda}$ is the canonical projection. For every $\lambda$, denote then by
$u'_{\lambda} : \mathcal{F}' \to (f'_{\lambda})_{*}(\mathcal{G}'_{\lambda})$ the homomorphism obtained as follows: let

```text
  σ_λ : g^*((f_λ)_*(𝒢_λ)) → (f'_λ)_*(g'_λ^*(𝒢_λ)) = (f'_λ)_*(𝒢'_λ)
```

be the homomorphism $(f_{\lambda})_{*}(\rho_{\mathcal{G}_{\lambda}})$, where $\rho$ is the canonical homomorphism
$(0_{I}, 4.4.3.2)$ corresponding to $g'_{\lambda}$. Then $u'_{\lambda}$ is defined as the composite

```text
  g^*(ℱ) ─g^*(u_λ)─→ g^*((f_λ)_*(𝒢_λ)) ─σ_λ─→ (f'_λ)_*(g'_λ^*(𝒢_λ)) → (f'_λ)_*(𝒢'_λ)
```

where $\sigma = \sigma(f')*(g')$ is the canonical homomorphism $(0_{I}, 4.4.3.3)$ corresponding to $g$. One will say for
short that $u'_{\lambda}$ is *deduced from $u_{\lambda}$ by the base change $g$*. When $f_{\lambda} : Z_{\lambda} \to X$
is an affine morphism, one has $(f'_{\lambda})_{*}(\mathcal{G}'_{\lambda}) =
g^{*}((f_{\lambda})_{*}(\mathcal{G}_{\lambda}))$, and in this case one has therefore simply $u'_{\lambda} =
g^{*}(u_{\lambda})$.

One can also interpret $u'_{\lambda}$ in the following way: it suffices to know the value of $u'_{\lambda}(t')$, when
$t'$ is a section of $\mathcal{F}'$ over an open set $U'$ of $X$, of the particular following type: $t'$ is the
restriction to $U'$ of the canonical image by $\Gamma(U, \mathcal{F}) \to \Gamma(g^{-1}(U), \mathcal{F}')$ of a section
$t$ of $\mathcal{F}$ over an open set $U$ of $X$ containing $g(U')$ (these sections in effect generating the
$\mathcal{O}_{X'}$-Module $\mathcal{F}'$ $(0_{I}, 3.7.1)$). Consider the section $u_{\lambda}(t)$ of
$\mathcal{G}_{\lambda}$ over $f^{-1}_{\lambda}(U)$, and its canonical image `t''` by $\Gamma(f^{-1}_{\lambda}(U),
\mathcal{G}_{\lambda}) \to \Gamma(f'^{-1}_{\lambda}(f^{-1}_{\lambda}(U)), \mathcal{G}'_{\lambda})$; then
$u'_{\lambda}(t')$ is the restriction of `t''` to $f'^{-1}_{\lambda}(U')$.

Consider in particular the case where $Z_{\lambda}$ is a subprescheme induced on an open set of $X$,
$\mathcal{G}_{\lambda} = j^{*}_{\lambda}(\mathcal{F})$, where $j_{\lambda} : Z_{\lambda} \to X$ is the canonical
injection, and where $u_{\lambda}$ is the canonical homomorphism $\rho_{\mathcal{F}} : \mathcal{F} \to
(j_{\lambda})_{*}(j^{*}_{\lambda}(\mathcal{F})) = (j_{\lambda})_{*}(\mathcal{G}_{\lambda})$ $(0_{I}, 4.4.3.2)$
corresponding to $j_{\lambda}$. Then $Z'_{\lambda}$ is induced on an open set of $X'$, and the preceding interpretation
shows that $u'_{\lambda}$ is none other than the canonical homomorphism $\rho_{\mathcal{F}'} : \mathcal{F}' \to
(j'_{\lambda})_{*}(j'^{*}_{\lambda}(\mathcal{F}')) = (j'_{\lambda})_{*}(\mathcal{G}'_{\lambda})$ corresponding to the
canonical injection $j'_{\lambda} : Z'_{\lambda} \to X'$.

**(11.9.6)** Under the conditions of `(11.9.5)`, suppose that $X$ and $X'$ are affine, and that one wants to prove that
for every section $t'$ of $\mathcal{F}'$ over $X'$, whose images by all the $u'_{\lambda}$ are null, then $t'$ is itself
null. Then one can again restrict to the case where $Z_{\lambda} = X$ for every $\lambda \in L$. Indeed, with the
notations of `(11.9.3)` and `(11.9.5)`, if one sets $Y'_{\lambda \mu} = Y_{\lambda \mu} \times_{X} X'$, the homomorphism
$v'_{\lambda \mu}$ deduced from $v_{\lambda \mu}$ by the base change $g$ is none other than the canonical homomorphism

<!-- original page 163 -->

$\rho_{\mathcal{G}'_{\lambda}} : \mathcal{G}'_{\lambda} \to (j'_{\lambda \mu})_{*}(j'^{*}_{\lambda
\mu}(\mathcal{G}'_{\lambda}))$ corresponding to the canonical injection $j'_{\lambda \mu} : Y'_{\lambda \mu} \to
Z'_{\lambda}$, as one has seen in `(11.9.5)`. The assertion then results from the reasonings of `(11.9.2)` and
`(11.9.3)`, $Y_{\lambda \mu}$ and $v_{\lambda \mu}$ being replaced by $Y'_{\lambda \mu}$ and $v'_{\lambda \mu}$.

One has a similar reduction when one wants to prove that the family $(u'_{\lambda})$ is separating ($X$ and $X'$ being
affine): this still results from `(11.9.2)` and `(11.9.3)`.

**Proposition (11.9.7).**

<!-- label: IV.11.9.7 -->

*With the notations of `(11.9.1)` and `(11.9.5)`, suppose $X = \operatorname{Spec}(A)$ and $X' =
\operatorname{Spec}(A')$ affine, and suppose moreover that $A'$ is a projective $A$-module. Then, if the family
$(u_{\lambda})$ is separating, every section $t'$ of $\mathcal{F}'$ over $X'$ whose images by all the $u'_{\lambda}$ are
null, is itself null.*

One has seen `(11.9.6)` that one can restrict to the case where all the $Z_{\lambda}$ are equal to $X$. The proposition
is then a consequence of the following lemma:

**Lemma (11.9.7.1).**

<!-- label: IV.11.9.7.1 -->

*Let $A$ be a ring, $(M_{\lambda})_{\lambda \in L}$ a family of $A$-modules, $M$ an $A$-module and for each $\lambda$,
$u_{\lambda} : M \to M_{\lambda}$ a homomorphism. Suppose that the intersection of the kernels of the $u_{\lambda}$ is
reduced to `0`. Then, for every projective $A$-module $N$, the intersection of the kernels of the homomorphisms
$u_{\lambda} \otimes 1 : M \otimes_{A} N \to M_{\lambda} \otimes_{A} N$ is reduced to `0`.*

Indeed, $N$ is a direct summand of a free $A$-module $L$, and it evidently suffices to prove that the intersection of
the kernels of the homomorphisms $v_{\lambda} : M \otimes_{A} L \to M_{\lambda} \otimes_{A} L$ is reduced to `0`, since
$u_{\lambda} \otimes 1 : M \otimes_{A} N \to M_{\lambda} \otimes_{A} N$ is the restriction of $v_{\lambda}$. But the
assertion then results trivially from the hypothesis.

**Remark (11.9.8).**

<!-- label: IV.11.9.8 -->

*We do not know whether, under the hypotheses of proposition `(11.9.7)`, the family $(u'_{\lambda})$ is separating: one
would need indeed `(11.9.4)` to prove that a section $t'$ of $\mathcal{F}'$ over an open set $D(h') \subset X'$ (where
$h' \in A'$) such that the $u'_{\lambda}(t')$ are all null, is itself null. Now, one cannot apply proposition `(11.9.4)`
to $D(h') = \operatorname{Spec}(A'_{h'})$, for from the fact that $A'$ is a projective $A$-module (even free), it does
not follow that $A'_{h'}$ is a projective $A$-module. For example, one may take for $A$ a discrete valuation ring, for
$A'$ a discrete valuation ring which is a free $A$-module of rank 2, and for $A'_{h'}$ the field of fractions of $A'$.*

One has however the following result:

**Corollary (11.9.9).**

<!-- label: IV.11.9.9 -->

*Let $X$ be an artinian prescheme, $g : X' \to X$ a flat morphism (one will note that these two conditions are satisfied
if $X$ is the spectrum of a field and $g$ an arbitrary morphism). Then, with the notations of `(11.9.1)` and `(11.9.5)`,
if the family $(u_{\lambda})$ is separating, so is the family $(u'_{\lambda})$.*

One can evidently restrict to the case where $X = \operatorname{Spec}(A)$ is the spectrum of a local artinian ring $A$
`(I, 6.2.2)`; one notes then that for every affine open set $U' = \operatorname{Spec}(A')$ of $X'$, $A'$ is a flat
$A$-module, hence projective $(0_{III}, 10.1.3)$. It suffices therefore to apply `(11.9.7)` to every affine open set of
$X'$ to obtain the corollary.

**Theorem (11.9.10).**

<!-- label: IV.11.9.10 -->

*Let $X$ be a prescheme, $(u_{\lambda})$ a family of homomorphisms `(11.9.1.1)`, $g : X' \to X$ a morphism,
$(u'_{\lambda})$ the family of homomorphisms deduced from $(u_{\lambda})$ by the base change $g$ `(11.9.5)`.*

*(i) If $g$ is a faithfully flat morphism and if the family $(u'_{\lambda})$ is separating, then the family
$(u_{\lambda})$ is separating.*

<!-- original page 164 -->

*(ii) Suppose that $g$ is a flat morphism, and moreover that one of the two following conditions is verified:*

*a) $L$ is finite and the $f_{\lambda}$ are quasi-compact.*

*b) The morphism $g$ is locally of finite presentation.*

*Then, if the family $(u_{\lambda})$ is separating, so is the family $(u'_{\lambda})$.*

(i) By virtue of `(2.2.8)`, it suffices to show that if a section $t$ of $\mathcal{F}$ over an open set $U$ of $X$
belongs to the kernel of each of the $u_{\lambda}$, its image $t'$ by the canonical homomorphism $\Gamma(\rho) :
\Gamma(U, \mathcal{F}) \to \Gamma(g^{-1}(U), g^{*}(\mathcal{F})) = \Gamma(U, g_{*}(g^{*}(\mathcal{F})))$ is null. Now
the images of $t'$ by the $g^{*}(u_{\lambda})$ are the images of the $u_{\lambda}(t)$ by the homomorphism $\Gamma(U,
(f_{\lambda})_{*}(\mathcal{G}_{\lambda})) \to \Gamma(g^{-1}(U), g^{*}((f_{\lambda})_{*}(\mathcal{G}_{\lambda})))$, hence
are null, and *a fortiori* one has $u'_{\lambda}(t') = 0$ for every $\lambda$, hence $t' = 0$ by hypothesis, which
proves (i).

(ii) The question being local on $X$ and $X'$, one can restrict to the case where $X = \operatorname{Spec}(A)$ and $X' =
\operatorname{Spec}(A')$ are affine, $A'$ being a flat $A$-module, and to proving that, for every section $z'$ of
$\mathcal{F}'$ over $X'$ whose images by all the $u'_{\lambda}$ are null, then $z'$ is itself null. One has moreover
seen `(11.9.6)` that one can then suppose $Z_{\lambda} = X$ for every $\lambda$.

Let us distinguish now the two cases.

**a)** If $L$ is finite and the $f_{\lambda}$ quasi-compact, one has seen `(11.9.3)` that one can again reduce to the
case where $Z_{\lambda} = X$ for every $\lambda \in L$, and where moreover $L$ is finite. It then amounts to the same to
say that the intersection of the kernels of the $u_{\lambda} : \mathcal{F} \to \mathcal{G}_{\lambda}$ is null, or that
the homomorphism $u = (u_{\lambda}) : \mathcal{F} \to \mathcal{G} = \oplus \mathcal{G}_{\lambda}$ is injective. As $u' =
g^{*}(u)$ is injective since $g$ is flat, the proposition is proved in this case.

**b)** Let $\mathcal{F} = \tilde{M}$, $\mathcal{G}_{\lambda} = \tilde{N}_{\lambda}$, and set $M' = M \otimes_{A} A'$,
$N'_{\lambda} = N_{\lambda} \otimes_{A} A'$, so that $\mathcal{F}' = \tilde{M}'$, $\mathcal{G}'_{\lambda} =
\tilde{N}'_{\lambda}$; by abuse of language, we shall still denote by $u_{\lambda}$ the homomorphism $M \to
N_{\lambda}$, and $u'_{\lambda}$ the homomorphism $u_{\lambda} \otimes 1 : M' \to N'_{\lambda}$. Let us give ourselves
an element $z' \in M'$ such that $u'_{\lambda}(z') = 0$ for every $\lambda$; the question is to prove that one has $z' =
0$. Now, the hypothesis that $g$ is flat and of finite presentation implies, by `(11.3.15)`, that there exists a finite
sequence $(s_{i})_{1 \leq i \leq n}$ of elements of $A$, such that, setting $\mathfrak{J}_{i} = s_{1} A + \cdots + s_{i}
A$, and $A_{i} = A_{s_{i}}/\mathfrak{J}_{i-1} A_{s_{i}}$, the ring $A'_{i} = A' \otimes_{A} A_{i}$ is a free
$A_{i}$-module for $1 \leq i \leq n$, and $\mathfrak{J}_{n} = A$. The proposition will be established if we prove for $1
\leq i \leq n$ the following assertion:

*(\*\_i) There exists an integer $m_{i} > 0$ such that $s^{m_{i}}_{j} z' = 0$ for $j \leq i$.*

Indeed, setting then $k = m_{n}$ and noting that the $s^{k}_{i}$ ($1 \leq i \leq n$) also generate the unit ideal of
$A$, the assertion $(*_{n})$ will show that $z'$, a linear combination of the $s^{k}_{i} z'$, is null.

Let us prove $(*_{i})$ by induction on $i$, the assertion being empty for $i = 0$. Suppose therefore $i > 0$ and let $m$
be a common multiple of the $m_{j}$ for $j \leq i - 1$. Remark that (for $1 \leq h \leq n$) if $\mathfrak{J}'_{h}$ is
the ideal generated by the $s^{m}_{j}$ ($1 \leq j \leq h$), $\mathfrak{J}'_{h}/\mathfrak{J}_{h}$ is nilpotent; to
replace the $s_{j}$ by $s^{m}_{j}$ for $1 \leq j \leq n$ amounts therefore to replacing, for $1 \leq h \leq n$, $A_{h}$
by $A_{s_{h}}/\mathfrak{J}'_{h-1} A_{s_{h}} = B_{h}$, so that $A_{h} =
B_{h}/(\mathfrak{J}_{h-1}/\mathfrak{J}'_{h-1})B_{h}$; as $A'$ is a flat $A$-module, it results from $(0_{III}, 10.1.2)$
that $B'_{h} = A' \otimes_{A} B_{h}$ is still a free $B_{h}$-module. One can therefore

<!-- original page 165 -->

replace all the $s_{j}$ ($1 \leq j \leq n$) by $s^{m}_{j}$ without changing the properties of the $\mathfrak{J}_{h}$ and
of the $A_{h}$, and suppose henceforth that $m = 1$. Then $z'$, being annihilated by $\mathfrak{J}_{i-1}$, identifies
with an element of $\operatorname{Hom}_{A'}(A'/\mathfrak{J}_{i-1} A', M')$, and as $\mathfrak{J}_{i-1} A'$ is an ideal
of finite type of $A'$, this module of homomorphisms identifies itself with
$\operatorname{Hom}_{A}(A/\mathfrak{J}_{i-1}, M) \otimes_{A} A'$ $(0_{I}, 6.2.2)$. Let
`v_λ = Hom(1, u_λ) : Hom_A(A/𝔍_{i-1}, M) → Hom_A(A/𝔍_{i-1}, N_λ)` be the homomorphism deduced from $u_{\lambda}$; the
family $(v_{\lambda})$ is also separating. Indeed, for every $t \in A$, one has
$(\operatorname{Hom}_{A}(A/\mathfrak{J}_{i-1}, M))_{t} = \operatorname{Hom}_{A_{t}}(A_{t}/(\mathfrak{J}_{i-1})_{t},
M_{t})$ and likewise replacing $M$ by $N_{\lambda}$, since the ideal $\mathfrak{J}_{i-1}$ is of finite type $(0_{I},
1.3.5)$; as by hypothesis the intersection of the kernels of the $(u_{\lambda})_{t}$ is null, so is the intersection of
the kernels of the $(v_{\lambda})_{t} = \operatorname{Hom}(1, (u_{\lambda})_{t})$, whence our assertion `(11.9.4)`.
Replacing $A$ by $A/\mathfrak{J}_{i-1}$, $M$ by $\operatorname{Hom}_{A}(A/\mathfrak{J}_{i-1}, M)$, $N_{\lambda}$ by
$\operatorname{Hom}_{A}(A/\mathfrak{J}_{i-1}, N_{\lambda})$ (which are $(A/\mathfrak{J}_{i-1})$-modules), $u_{\lambda}$
by $v_{\lambda}$ and finally $A'$ by $A'/\mathfrak{J}_{i-1} A'$, one sees that one can reduce to the case where, in the
initial situation, the element $s = s_{i} \in A$ is such that $A'_{s}$ is a free $A_{s}$-module. Now, the family of
$(u_{\lambda})_{s} : M_{s} \to (N_{\lambda})_{s}$ is separating by hypothesis; as one has $(u'_{\lambda})_{s}(z'/1) =
0$, it results from `(11.9.7)` that one has $z'/1 = 0$ in $M'_{s}$; but this means that there exists an integer $r$ such
that $s^{r} z' = 0$ in $M'$, which completes the proof of $(*_{i})$ by induction.

**Remark (11.9.11).**

<!-- label: IV.11.9.11 -->

*Let us restrict ourselves for simplicity to the case where $Z_{\lambda} = X$ for every $\lambda$. It must be noted that
if the family of homomorphisms $u_{\lambda} : \mathcal{F} \to \mathcal{G}_{\lambda}$ is separating, it does not
necessarily follow that, for every $x \in X$, the intersection of the kernels of the homomorphisms $(u_{\lambda})_{x} :
\mathcal{F}_{x} \to (\mathcal{G}_{\lambda})_{x}$ is reduced to `0`.* For example, let $X$ be a Jacobson locally
Noetherian prescheme, of dimension $\geq 1$, and $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module; for every closed
point $x$ of $X$, and every integer $n \geq 0$, $\mathfrak{m}^{n}_{x} \mathcal{F}$ is a coherent
$\mathcal{O}_{X}$-Module of support contained in $\overline{x}$. The family of canonical homomorphisms $\mathcal{F} \to
\mathcal{F}/\mathfrak{m}^{n}_{x} \mathcal{F}$ (where $x$ runs through the set `X_0` of closed points of $X$ and $n$ the
set of integers $\geq 0$) is separating: indeed, if $t$ is a section of $\mathcal{F}$ over an open set $U$ of $X$ whose
images in the $\Gamma(U, \mathcal{F}/\mathfrak{m}^{n}_{x} \mathcal{F})$ are all null, it follows at once that for every
closed point $x \in U$, one has $t_{x} = 0$; as the set of closed points contained in $U$ is very dense in $U$, this
implies $t = 0$ `(10.2.1)`. However, if one takes $\mathcal{F} = \mathcal{O}_{X}$, and if $y \in X$ is a non-closed
point of $X$, one has $(\mathcal{O}_{X}/\mathfrak{m}^{n}_{x} \mathcal{O}_{X})_{y} = 0$ for every closed point $x$ of
$X$, but $\mathcal{O}_{X, y} \neq 0$, and the intersection of the kernels of the homomorphisms $\mathcal{O}_{X, y} \to
(\mathcal{O}_{X}/\mathfrak{m}^{n}_{x} \mathcal{O}_{X})_{y}$ is equal to $\mathcal{O}_{X, y}$.

**Lemma (11.9.12).**

<!-- label: IV.11.9.12 -->

*The notations being those of `(11.9.1)` and `(11.9.5)`, suppose the family $(u_{\lambda})$ separating; suppose moreover
that $X$ is an $S$-prescheme, where $S = \operatorname{Spec}(A)$ is an affine scheme, and that $X' = X \times_{S} S'$,
where $S' = \operatorname{Spec}(A')$, $A'$ being an $A$-algebra; suppose finally that the $\mathcal{G}_{\lambda}$ are
$S$-flat. Let $(A'_{\alpha})_{\alpha \in I}$ be the filtered family of sub-$A$-algebras of finite type of $A'$; for
every $\alpha \in I$, set $S'_{\alpha} = \operatorname{Spec}(A'_{\alpha})$, $X'_{\alpha} = X \times_{S} S'_{\alpha}$,
$Z'_{\alpha \lambda} = Z_{\lambda} \times_{X} X'_{\alpha}$, and let $f'_{\alpha \lambda} : Z'_{\alpha \lambda} \to
X'_{\alpha}$, $\mathcal{F}'_{\alpha}$, $\mathcal{G}'_{\alpha \lambda}$ and $u'_{\alpha \lambda}$ be the morphisms,
Modules and homomorphisms of Modules deduced from $f_{\lambda}$, $\mathcal{F}$, $\mathcal{G}_{\lambda}$ and
$u_{\lambda}$ by the base change $X'_{\alpha} \to X$. Then, if, for every $\alpha \in I$, the family $(u'_{\alpha
\lambda})_{\lambda \in L}$ is separating, so is $(u'_{\lambda})_{\lambda \in L}$.*

It is a matter of proving that if a section $t'$ of $\mathcal{F}'$ over an affine open set $U'$

<!-- original page 166 -->

of $X'$ is such that $u'_{\lambda}(t') = 0$ for every $\lambda \in L$, one has $t' = 0$. If $h_{\alpha} : X' \to
X'_{\alpha}$ is the canonical projection, it results from `(8.2.11)` that there exists an index $\alpha$ and a
quasi-compact open set $U'_{\alpha} \subset X'_{\alpha}$ such that $U' = h^{-1}_{\alpha}(U'_{\alpha})$; moreover, by
virtue of `(8.5.2, (i))`, one can suppose that there is a section $t'_{\alpha}$ of $\mathcal{F}'_{\alpha}$ over
$U'_{\alpha}$ such that $t'$ is the canonical image of $t'_{\alpha}$. Up to replacing $S$, $X$, $Z_{\lambda}$,
$f_{\lambda}$, $\mathcal{F}$, $\mathcal{G}_{\lambda}$ and $u_{\lambda}$ by $S'_{\alpha}$, $U'_{\alpha}$,
$f^{-1}_{\alpha}(U'_{\alpha})$ and the corresponding restrictions of $\mathcal{F}'_{\alpha}$, $\mathcal{G}'_{\alpha
\lambda}$ and $u'_{\alpha \lambda}$, one can therefore suppose that $U' = X'$, that $t'$ is the canonical image of a
section $t$ of $\mathcal{F}$ over $X$ and that the homomorphism $A \to A'$ is injective, or equivalently, if $p : S' \to
S$ is the corresponding morphism, that the homomorphism $\mathcal{O}_{S} \to p_{*}(\mathcal{O}_{S'})$ involved in the
definition of $p$ is injective. It follows at once by virtue of the flatness of $\mathcal{G}_{\lambda}$ over $S$ (and
reducing for example to the case where $Z_{\lambda}$ is affine over $S$ `(I, 1.6.3 and 1.6.5)`) that the canonical
homomorphism $\rho : \mathcal{G}_{\lambda} \to (g'_{\lambda})_{*}(\mathcal{G}'_{\lambda})$ is also injective. But the
composed homomorphism

```text
  Γ(X, ℱ) → Γ(Z_λ, 𝒢_λ) → Γ(Z_λ, (g'_λ)_*(𝒢'_λ))
```

is equal by definition to the composed homomorphism

```text
  Γ(X, ℱ) ─Γ(ρ)─→ Γ(X', ℱ') → Γ(Z'_λ, 𝒢'_λ);
```

hence the image of $t$ by these composed homomorphisms is $u'_{\lambda}(t') = 0$; by virtue of the injectivity of the
homomorphism $\Gamma(Z_{\lambda}, \mathcal{G}_{\lambda}) \to \Gamma(Z'_{\lambda}, \mathcal{G}'_{\lambda})$ one concludes
that $u_{\lambda}(t) = 0$ for every $\lambda \in L$, whence $t = 0$ by hypothesis, and finally $t' = 0$.

**Proposition (11.9.13).**

<!-- label: IV.11.9.13 -->

*The notations being those of `(11.9.1)` and `(11.9.5)`, suppose that $X$ is a prescheme over a field $k$, and that,
setting $S = \operatorname{Spec}(k)$, one has $X' = X \times_{S} S'$, where $S'$ is an arbitrary $k$-prescheme. Then, if
the family $(u_{\lambda})_{\lambda \in L}$ is separating, so is $(u'_{\lambda})$.*

One can restrict to the case where $S' = \operatorname{Spec}(A')$ is affine. If $A'$ is a $k$-algebra of finite type,
the morphism $g : X' \to X$ is flat and of finite presentation, and one is then in the conditions of application of
`(11.9.10, (ii), b))`. In the general case, one considers $A'$ as the inductive limit of its sub-$k$-algebras
$A'_{\alpha}$ of finite type, and one applies to each $A'_{\alpha}$ the result of `(11.9.10, (ii), b))`; one then
concludes by means of lemma `(11.9.12)`, since the $\mathcal{G}_{\lambda}$ are $S$-flat.

**(11.9.14)** Let us keep always the notations of `(11.9.1)` and `(11.9.5)` and suppose that $X$ is an $S$-prescheme. If
for every base change $g : X \times_{S} S' \to X$, where $S' \to S$ is an arbitrary morphism, the corresponding family
$(u'_{\lambda})$ is separating, we shall say that the family $(u_{\lambda})$ is **universally separating relative to
$S$**. When the family $(u_{\lambda})$ is reduced to a single element $u$, we shall also say that $u$ is **universally
injective**, relative to $S$. It is clear then that for every morphism $h : S' \to S$, the corresponding family
$(u'_{\lambda})$ is universally separating relative to $S'$; conversely, if $h$ is faithfully flat and if
$(u'_{\lambda})$ is universally separating relative to $S'$, then $(u_{\lambda})$ is universally separating relative to
$S$, as results at once from `(11.9.10, (i))` and the fact that for every morphism $S'' \to S$, the corresponding
morphism $S'' \times_{S} S' \to S''$ is faithfully flat.

<!-- original page 167 -->

**Proposition (11.9.15).**

<!-- label: IV.11.9.15 -->

*The notations being those of `(11.9.1)`, suppose that $X$ is an $S$-prescheme, the $\mathcal{G}_{\lambda}$ being
$S$-flat. Let `S_0` be a closed subprescheme of $S$ defined by a quasi-coherent nilpotent Ideal $\mathcal{J}$ of
$\mathcal{O}_{S}$, such that the $(\mathcal{O}_{S}/\mathcal{J})$-Modules $\mathcal{J}^{k}/\mathcal{J}^{k+1}$ are all
locally free. Let $(u_{\lambda, 0})$ be the family of homomorphisms obtained from the base change $X_{0} = X \times_{S}
S_{0} \to X$. Then, if the family $(u_{\lambda, 0})$ is separating (resp. universally separating relative to `S_0`), the
family $(u_{\lambda})$ is separating (resp. universally separating relative to $S$).*

Note that if $S' \to S$ is an arbitrary base change and $S'_{0} = S' \times_{S} S_{0}$, $S'_{0}$ is a closed
subprescheme of $S'$ defined by a quasi-coherent nilpotent ideal $\mathcal{J}'$ of $\mathcal{O}_{S'}$ such that
$\mathcal{J}'^{k}/\mathcal{J}'^{k+1}$ is a locally free $(\mathcal{O}_{S'}/\mathcal{J}')$-Module for every $k$
`(2.1.8, (i))`; as moreover the $\mathcal{G}'_{\lambda} = \mathcal{G}_{\lambda} \otimes_{S} S'$ are $S'$-flat, one sees
that the assertion concerning universally separating families is a consequence of the assertion concerning separating
families. To prove this last, one can `(11.9.3)` reduce to the case where $S = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$ are affine, $Z_{\lambda} = X$ for every $\lambda$, $\mathcal{F} = \tilde{M}$,
$\mathcal{G}_{\lambda} = \tilde{N}_{\lambda}$, where $M$ and the $N_{\lambda}$ are $B$-modules, the $N_{\lambda}$ being
flat $A$-modules. Moreover, the question being local on $X$ and $S$, it suffices to see that if $t \in M$ is such that
$u_{\lambda}(t) = 0$ for every $\lambda$, then $t = 0$. One has $\mathcal{J} = \tilde{\mathfrak{J}}$, where
$\mathfrak{J}$ is a nilpotent ideal of $A$, such that the $\mathfrak{J}^{k}/\mathfrak{J}^{k+1}$ are free
$(A/\mathfrak{J})$-modules, and by hypothesis the $u_{\lambda, 0} : M/\mathfrak{J} M \to N_{\lambda}/\mathfrak{J}
N_{\lambda}$ form a separating family. Suppose that $\mathfrak{J}^{n+1} = 0$ ($n$ integer $\geq 0$) and let us argue by
induction on $n$, the assertion being trivial for $n = 0$. If $\bar{t}$ is the class of $t$ in $M/\mathfrak{J}^{n} M$,
the class of $u_{\lambda}(t)$ in $N_{\lambda}/\mathfrak{J}^{n} N_{\lambda}$ is null for every $\lambda$, hence, by the
induction hypothesis, $\bar{t} = 0$, in other words one has $t \in \mathfrak{J}^{n} M$. Now $\mathfrak{J}^{n} =
\mathfrak{J}^{n}/\mathfrak{J}^{n+1}$ is a free $(A/\mathfrak{J})$-module; if $(e_{\alpha})$ is a basis of this module,
one can therefore write $t = \sum_{\alpha} e_{\alpha} t_{\alpha}$, with $t_{\alpha} \in A/\mathfrak{J}$, null except for
a finite number of indices. On the other hand, since $N_{\lambda}$ is a flat $A$-module, $\mathfrak{J}^{n} N_{\lambda}$
identifies with $\mathfrak{J}^{n} \otimes_{A/\mathfrak{J}} (N_{\lambda}/\mathfrak{J} N_{\lambda})$ and one can
consequently write $u_{\lambda}(t) = \sum_{\alpha} e_{\alpha} u_{\lambda}(t_{\alpha}) = \sum_{\alpha} e_{\alpha} \otimes
u_{\lambda, 0}(\bar{t}_{\alpha})$. As by hypothesis $u_{\lambda}(t) = 0$, one deduces that $u_{\lambda,
0}(\bar{t}_{\alpha}) = 0$ for every $\alpha$ and every $\lambda$; whence $\bar{t}_{\alpha} = 0$ for every $\alpha$ since
the family $(u_{\lambda, 0})$ is separating, and consequently $t = 0$. Q.E.D.

**Theorem (11.9.16).**

<!-- label: IV.11.9.16 -->

*The notations being those of `(11.9.1)`, suppose that $X$ is a locally Noetherian $S$-prescheme, $\mathcal{F}$ a
coherent $\mathcal{O}_{X}$-Module and that the $\mathcal{G}_{\lambda}$ are $S$-flat. For every $s \in S$, let
$((u_{\lambda})_{s})_{\lambda \in L}$ be the family obtained from $(u_{\lambda})$ by the base change $X_{s} = X
\times_{S} \operatorname{Spec}(k(s)) \to X$. Then, for the family $(u_{\lambda})$ to be universally separating relative
to $S$, it is necessary and sufficient that for every $s \in S$, the family $((u_{\lambda})_{s})$ be separating.*

The necessity of the condition follows trivially from the definitions. Conversely, suppose the condition of the
statement verified, and let us first prove that the family $(u_{\lambda})$ is separating. One can `(11.9.3)` reduce to
the case where $S = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ are affine, $Z_{\lambda} = X$ for every
$\lambda$, $\mathcal{F} = \tilde{M}$, $\mathcal{G}_{\lambda} = \tilde{N}_{\lambda}$, where $B$ is Noetherian, $M$ is a
$B$-module of finite type and the $N_{\lambda}$ $A$-flat modules, and restrict to proving that, if $t \in M$ is such
that $u_{\lambda}(t) = 0$ for every $\lambda$, then $t = 0$. To show that $t = 0$, it suffices to prove that for every
maximal ideal $\mathfrak{p}$ of $B$, the image $t_{\mathfrak{p}}$ of $t$ in $M_{\mathfrak{p}}$ is null
`(Bourbaki, Alg. comm., chap. II, §3, n° 3, cor. 1 of th. 1)`. One can therefore restrict to showing that the
intersection of the kernels

<!-- original page 168 -->

of the $(u_{\lambda})_{\mathfrak{p}} : M_{\mathfrak{p}} \to (N_{\lambda})_{\mathfrak{p}}$ deduced from $(u_{\lambda})$
by the base change $\operatorname{Spec}(B_{\mathfrak{p}}) \to \operatorname{Spec}(B)$ is reduced to `0`. In other words,
one is reduced to the case where $B$ is a Noetherian local ring, and by considering the prime ideal of $A$ inverse image
of the maximal ideal of $B$, one can also suppose that $A$ is a local ring of maximal ideal $\mathfrak{m}$. Then, as
$\mathfrak{m} B$ is contained in the maximal ideal of $B$, and $M$ is a $B$-module of finite type, the intersection of
the $\mathfrak{m}^{n} M$ is reduced to `0` $(0_{I}, 7.3.5)$, hence it suffices to prove that for every $n$, the image of
$t$ in $M/\mathfrak{m}^{n+1} M$ is null. It suffices therefore to prove that the family deduced from $(u_{\lambda})$ by
the base change $\operatorname{Spec}(B/\mathfrak{m}^{n+1} B) \to \operatorname{Spec}(B)$ is separating, which still
means that one can restrict to the case where $A$ is a local ring whose maximal ideal $\mathfrak{m}$ is nilpotent. But
then the $\mathfrak{m}^{k}/\mathfrak{m}^{k+1}$ are free $(A/\mathfrak{m})$-modules, and by virtue of the hypothesis on
the $(u_{\lambda})_{s}$, one is precisely in the conditions of application of `(11.9.15)`, whence the announced
conclusion.

Let now $h : S' \to S$ be a base change morphism, and $(u'_{\lambda})$ the family obtained from $(u_{\lambda})$ by the
base change $h' : X \times_{S} S' \to X$; let us prove that $(u'_{\lambda})$ is also separating. Suppose first that $h$
is *locally of finite type*; so is then $h'$, hence $X' = X \times_{S} S'$ is locally Noetherian; moreover, if $s' \in
S'$ is above the point $s \in S$, it results from `(11.9.13)` applied to $X_{s}$ and to $X_{s'} = X_{s} \otimes_{k(s)}
k(s')$ that, for every $s' \in S'$, the family $((u'_{\lambda})_{s'})$ is separating; one can consequently conclude from
the first part of the proof that in this case $(u'_{\lambda})$ is separating.

Finally, if $h$ is arbitrary, one can evidently limit oneself to the case where $S = \operatorname{Spec}(A)$ and $S' =
\operatorname{Spec}(A')$ are affine, and consider $A'$ as the inductive limit of its sub-$A$-algebras of finite type. As
the $\mathcal{G}_{\lambda}$ are $S$-flat, it suffices to apply what precedes and lemma `(11.9.12)` to complete the
proof.

**Proposition (11.9.17).**

<!-- label: IV.11.9.17 -->

*Let $f : X \to S$ be a morphism locally of finite presentation, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module
of finite presentation and $f$-flat, $U$ an open set of $X$, $j : U \to X$ the canonical injection, $u : \mathcal{F} \to
j_{*}(j^{*}(\mathcal{F}))$ the canonical homomorphism $(0_{I}, 4.4.3.2)$. For every $s \in S$, let $X_{s}$ be the fibre
$X \times_{S} \operatorname{Spec}(k(s))$, $U_{s}$ the open set $U \cap X_{s}$ of $X_{s}$, $\mathcal{F}_{s} = \mathcal{F}
\otimes_{\mathcal{O}_{S}} k(s)$, $j_{s} : U_{s} \to X_{s}$ the canonical injection, $u_{s} : \mathcal{F}_{s} \to
(j_{s})_{*}((j_{s})^{*}(\mathcal{F}_{s}))$ the canonical homomorphism. For $u$ to be universally injective relative to
$S$, it is necessary and sufficient that $u_{s}$ be injective for every $s \in S$.*

There remains only to prove the sufficiency of the condition. When $X$ is locally Noetherian, the proposition is an
immediate corollary of `(11.9.16)`. We shall reduce to this case in two steps, restricting ourselves, as one can
evidently do, to the case where $S = \operatorname{Spec}(A)$ and $X$ are affine.

**A)** *Case where $U$ is quasi-compact.* — We shall use the following lemma:

**Lemma (11.9.17.1).**

<!-- label: IV.11.9.17.1 -->

*Under the general hypotheses of `(11.9.17)`, and supposing in addition $S$ and $X$ affine and $U$ quasi-compact, the
set $E$ of $s \in S$ such that $u_{s}$ is injective is constructible.*

Indeed, the fibres $X_{s}$ are locally Noetherian preschemes, hence $E$ can also, by virtue of `(5.10.2)`, be defined as
the set of $s \in S$ such that $Ass(\mathcal{F}_{s}) \subset U_{s}$. Note moreover that $U$, being quasi-compact in an
affine scheme, is constructible. Then, the verification of condition `(9.2.1, (i))` follows at once from `(4.2.7)`; on
the other

<!-- original page 169 -->

hand, the verification of `(9.2.1, (ii))` is made easily by using the study of associated prime cycles in the
neighbourhood of the generic fibre `(9.8.3)`, as well as `(9.5.2)` and `(9.5.3)`.

This lemma being established, one can, by virtue of `(8.9.1)` and `(8.2.11)`, suppose that there exists a Noetherian
subring `A_0` of $A$, a prescheme of finite type `X_0` over $S_{0} = \operatorname{Spec}(A_{0})$, an open set `U_0` of
`X_0` and a coherent $\mathcal{O}_{X_{0}}$-Module $\mathcal{F}_{0}$ such that $X = X_{0} \times_{S_{0}} S$ and that, if
$p_{0} : X \to X_{0}$ is the canonical projection, one has $U = p^{-1}_{0}(U_{0})$ and $\mathcal{F} =
p^{*}_{0}(\mathcal{F}_{0})$. Let $(A_{\alpha})$ be the filtered family of subrings of $A$ which are `A_0`-algebras of
finite type, and set $X_{\alpha} = X_{0} \times_{S_{0}} S_{\alpha}$, $U_{\alpha} = U_{0} \times_{S_{0}} S_{\alpha}$,
$\mathcal{F}_{\alpha} = \mathcal{F}_{0} \otimes_{S_{0}} S_{\alpha}$; let $u_{\alpha}$ be the canonical homomorphism
relative to $\mathcal{F}_{\alpha}$ and $U_{\alpha}$, defined as in `(11.9.17)`. For every $s \in S$, the hypothesis that
$u_{s}$ is injective implies that $(u_{\alpha})_{s_{\alpha}}$ is also so `(11.9.10, (i))`, where $s_{\alpha} =
q_{\alpha}(s)$ is the image of $s$ by the morphism $q_{\alpha} : S \to S_{\alpha}$. If $E_{\alpha}$ is the set of
$s_{\alpha} \in S_{\alpha}$ such that $(u_{\alpha})_{s_{\alpha}}$ is injective, one has therefore $S =
q^{-1}_{\alpha}(E_{\alpha})$, and the $E_{\alpha}$ form a projective system of sets. But lemma `(11.9.17.1)` applied to
$u_{\alpha}$, shows that $E_{\alpha}$ is constructible in $S_{\alpha}$; one deduces therefore from `(8.3.4)` that there
exists an index $\alpha$ such that $E_{\alpha} = S_{\alpha}$. But then, as $X_{\alpha}$ is Noetherian, $u_{\alpha}$ is
universally injective by virtue of `(11.9.16)`, hence so is $u$.

**B)** *General case.* — The open set $U$ is a filtered increasing union of quasi-compact open sets $U_{\lambda}$; if
$j_{\lambda} : U_{\lambda} \to X$ is the canonical injection and $u_{\lambda} : \mathcal{F} \to
(j_{\lambda})_{*}((j_{\lambda})^{*}(\mathcal{F}))$ the corresponding homomorphism, it results from lemma `(11.9.17.1)`
that the set $E_{\lambda}$ of $s \in S$ such that $(u_{\lambda})_{s}$ is injective is constructible. On the other hand,
for $s \in S$, to say that $u_{s}$ (resp. $(u_{\lambda})_{s}$) is injective means that $Ass(\mathcal{F}_{s}) \subset U
\cap X_{s}$ (resp. $Ass(\mathcal{F}_{s}) \subset U_{\lambda} \cap X_{s}$) `(5.10.2)`. As $Ass(\mathcal{F}_{s})$ is
finite `(3.1.6)`, to say that $u_{s}$ is injective therefore means that there exists $\lambda$ such that $s \in
E_{\lambda}$; the hypothesis means consequently that $S = \bigcup_{\lambda} E_{\lambda}$. By virtue of `(1.9.9)`, there
exists an index $\lambda$ such that $S = E_{\lambda}$, whence one concludes by the first part of the reasoning that
$u_{\lambda}$ is universally injective. It then follows from the factorization of $u_{\lambda}$:

```text
  ℱ ─u─→ j_*(j^*(ℱ)) → (j_λ)_*((j_λ)^*(ℱ))
```

that $u$ is also universally injective.

**Remark (11.9.18).**

<!-- label: IV.11.9.18 -->

*Let $X$ be a prescheme, $\mathcal{F}$, $\mathcal{G}$ two quasi-coherent $\mathcal{O}_{X}$-Modules of finite
presentation, $\mathcal{G}$ being moreover assumed locally free, $u : \mathcal{F} \to \mathcal{G}$ a homomorphism. The
following conditions are equivalent:*

*a) for every morphism $g : X' \to X$, the homomorphism $g^{*}(u) : g^{*}(\mathcal{F}) \to g^{*}(\mathcal{G})$ is
injective;*

*b) for every $x \in X$, the homomorphism $u \otimes 1_{k(x)} : \mathcal{F} \otimes_{\mathcal{O}_{x}} k(x) \to
\mathcal{G} \otimes_{\mathcal{O}_{x}} k(x)$ is injective;*

*c) for every $x \in X$, there exists an open neighbourhood $U$ of $x$ such that $u | U : \mathcal{F} | U \to
\mathcal{G} | U$ is an isomorphism of $\mathcal{F} | U$ onto a direct summand of $\mathcal{G} | U$.*

Indeed, it is clear that c) implies a) and that a) implies b). The fact that b) implies c) results from `(0, 19.1.12)`,
$(0_{I}, 5.2.5)$ and $(0_{I}, 5.5.5)$.

When the preceding equivalent conditions are verified, one says that $u$ is **universally injective**.

<!-- original page 170 -->

### 11.10. Schematically dominant families of morphisms and schematically dense families of subpreschemes

**Proposition (11.10.1).**

<!-- label: IV.11.10.1 -->

*Let $X$ be a prescheme, $(Z_{\lambda})_{\lambda \in L}$ a family of preschemes, and for every $\lambda \in L$, let
$f_{\lambda} = (\psi_{\lambda}, \theta_{\lambda}) : Z_{\lambda} \to X$ be a morphism. The following conditions are
equivalent:*

*a) The family of homomorphisms $\theta_{\lambda} : \mathcal{O}_{X} \to (f_{\lambda})_{*}(\mathcal{O}_{Z_{\lambda}})$ is
separating (in other words `(11.9.1)`, the intersection of the kernels of the $\theta_{\lambda}$ is null).*

*b) For every open set $U$ of $X$, every section $t$ of $\mathcal{O}_{X}$ over $U$ whose images by all the canonical
homomorphisms*

```text
(11.10.1.1)         (θ_λ)_U : Γ(U, 𝒪_X) → Γ(f_λ⁻¹(U), 𝒪_{Z_λ})
```

*are null, is itself null.*

*c) For every open set $U$ of $X$, and every closed subprescheme $Y$ of $U$ such that for every $\lambda \in L$, there
exists a factorization*

```text
(11.10.1.2)         f_λ⁻¹(U) → Y ─j─→ U
```

*of the restriction $f^{-1}_{\lambda}(U) \to U$ of $f_{\lambda}$ (where $j$ is the canonical injection), one has $Y =
U$.*

*If moreover $X$ is an $S$-prescheme, these conditions are also equivalent to the following:*

*d) For every separated morphism $g : X' \to S$ and every couple of $S$-morphisms $u$, $v$ of an open set $U$ of $X$
into $X'$, such that for every $\lambda$, the composites of $u$ and $v$ with the morphism $f^{-1}_{\lambda}(U) \to U$,
restriction of $f_{\lambda}$, are equal, one has $u = v$.*

The equivalence of a) and b) results from the definitions. To see that b) implies c), it suffices to consider the
quasi-coherent Ideal $\mathcal{I}$ of $\mathcal{O}_{U}$ defining $Y$, and to note that, for every open set $V \subset
U$, the hypothesis implies that the morphism $(\theta_{\lambda})_{V}$ factors as

```text
  Γ(V, 𝒪_U) → Γ(V, 𝒪_Y) → Γ(f_λ⁻¹(V), 𝒪_{Z_λ}).
```

One concludes that every section $t$ of $\mathcal{I}$ over $V$ has image `0` in all the $\Gamma(f^{-1}_{\lambda}(V),
\mathcal{O}_{Z_{\lambda}})$, hence, by virtue of b), $\mathcal{I} = 0$ and $Y = U$. Conversely, if c) is verified, it
suffices, to prove b), to apply c) to the closed subprescheme $Y$ of $U$ defined by the Ideal $t\mathcal{O}_{U}$: the
hypothesis that the images of $t$ by the $(\theta_{\lambda})_{U}$ are all null implies that one has factorizations
`(11.10.1.2)` for every $\lambda$ `(I, 4.1.9)`. To prove that c) implies d), it suffices to apply c) to the closed
subprescheme $Y$ of $U$, inverse image of the diagonal of $X' \times_{S} X'$ by $(u, v)$, and to use `(I, 4.4.1)`.
Conversely, one deduces b) from d) by considering the $S$-scheme $X' = S[T] = S \otimes_{\mathbb{Z}} \mathbb{Z}[T]$ ($T$
indeterminate) and recalling that the sections of $\mathcal{O}_{U}$ over $U$ correspond bijectively to $S$-morphisms $U
\to S[T]$ `(I, 3.3.15)`; to say that two sections of $\mathcal{O}_{U}$ over $U$ have the same images by all the
$(\theta_{\lambda})_{U}$ amounts to saying that the composites of the two corresponding morphisms with all the morphisms
$f^{-1}_{\lambda}(U) \to U$ are equal.

<!-- original page 171 -->

**Definition (11.10.2).**

<!-- label: IV.11.10.2 -->

*When the equivalent conditions of `(11.10.1)` are verified, one says that the family $(f_{\lambda})$ is **schematically
dominant**. When the $f_{\lambda}$ are the canonical immersions in $X$ of a family $(Z_{\lambda})$ of subpreschemes of
$X$, one says also that the family $(Z_{\lambda})$ is **schematically dense**.*

**Remarks (11.10.3).**

<!-- label: IV.11.10.3 -->

*(i) The notion of schematically dominant family is local on $X$, as results for example from form b) in `(11.10.1)`: if
$(W_{\alpha})$ is an open cover of $X$, the family $(f_{\lambda})$ is schematically dominant if and only if so is each
of the families formed of the morphisms $f^{-1}_{\lambda}(W_{\alpha}) \to W_{\alpha}$ restrictions of the
$f_{\lambda}$.*

*(ii) If $Z$ is the sum prescheme of the $Z_{\lambda}$, $f : Z \to X$ the morphism coinciding with $f_{\lambda}$ on each
of the $Z_{\lambda}$, it amounts to the same to say that the family $(f_{\lambda})$ is schematically dominant, or that
the family reduced to the single element $f$ is so.*

*(iii) Let $M$ be a second index set and, for every $\lambda \in L$, let $(g_{\lambda \mu})_{\mu \in M}$ be a family of
morphisms $g_{\lambda \mu} : Z_{\lambda \mu} \to Z_{\lambda}$; if, for each $\lambda \in L$, the family $(g_{\lambda
\mu})_{\mu \in M}$ is schematically dominant, then it amounts to the same to say that the family $(f_{\lambda})_{\lambda
\in L}$ is schematically dominant, or that the family $(f_{\lambda} \circ g_{\lambda \mu})_{(\lambda, \mu) \in L \times
M}$ is so `(11.9.2)`.*

*(iv) Let $f : Z \to X$ be a morphism such that $f_{*}(\mathcal{O}_{Z})$ is a quasi-coherent $\mathcal{O}_{X}$-Module
(for example a quasi-compact and quasi-separated morphism `(1.7.4)`). Then, to say that $f$ is schematically dominant
means that the closed image of $Z$ by $f$ `(I, 9.5.3)` is identical to $X$.*

**Proposition (11.10.4).**

<!-- label: IV.11.10.4 -->

*If the family of morphisms $f_{\lambda} : Z_{\lambda} \to X$ is schematically dominant, the union of the
$f_{\lambda}(Z_{\lambda})$ is dense in $X$. Conversely, if this union is dense in $X$ and if moreover $X$ is reduced,
the family $(f_{\lambda})$ is schematically dominant.*

The first assertion results at once from `(11.10.1, b))`. On the other hand, if $X$ is reduced, and if the union of the
$f_{\lambda}(Z_{\lambda})$ is dense in $X$, then, if one has factorizations `(11.10.1.2)` for every $\lambda \in L$, one
has also factorizations $(f^{-1}_{\lambda}(U))_{red} \to Y_{red} \to U$, and the hypothesis implies that the underlying
space of $Y$ is identical to $U$, hence $Y = Y_{red} = U$ since $U$ is reduced.

The results of $n^{\circ} 11.9$ on separating families translate into results on schematically dominant families:

**Theorem (11.10.5).**

<!-- label: IV.11.10.5 -->

*Let $(f_{\lambda})$ be a family of morphisms $f_{\lambda} : Z_{\lambda} \to X$, $g : X' \to X$ a morphism, and set
$Z'_{\lambda} = Z_{\lambda} \times_{X} X'$, $f'_{\lambda} = (f_{\lambda})_{(X')} : Z'_{\lambda} \to X'$.*

*(i) If $g$ is faithfully flat and if the family $(f'_{\lambda})$ is schematically dominant, then the family
$(f_{\lambda})$ is schematically dominant.*

*(ii) Suppose that $g$ is a flat morphism, and moreover that one of the following conditions is verified:*

*a) $L$ is finite and the $f_{\lambda}$ are quasi-compact.*

*b) The morphism $g$ is locally of finite presentation.*

*Then, if the family $(f_{\lambda})$ is schematically dominant, so is the family $(f'_{\lambda})$.*

<!-- original page 172 -->

**Proposition (11.10.6).**

<!-- label: IV.11.10.6 -->

*The notations being those of `(11.10.5)`, suppose that $X$ is a prescheme over a field $k$, and that, setting $S =
\operatorname{Spec}(k)$, one has $X' = X \times_{S} S'$, where $S'$ is an arbitrary $k$-prescheme. Then, if the family
$(f_{\lambda})$ is schematically dominant, so is $(f'_{\lambda})$.*

**Corollary (11.10.7).**

<!-- label: IV.11.10.7 -->

*Let $X$ be a prescheme over a field $k$, $(Z_{\lambda})_{\lambda \in L}$ a family of $k$-preschemes geometrically
reduced over $k$, and for each $\lambda \in L$, let $f_{\lambda} : Z_{\lambda} \to X$ be a $k$-morphism. Denote by $Y$
the reduced subprescheme of $X$ having as underlying space the closure of $\bigcup_{\lambda \in L}
f_{\lambda}(Z_{\lambda})$. Let $k'$ be an extension of $k$, $X'$, $Z'_{\lambda}$, $f'_{\lambda} : Z'_{\lambda} \to X'$
the preschemes and morphisms deduced from $X$, $Z_{\lambda}$ and $f_{\lambda}$ by extension of the base to $k'$. Then,
if $Y'$ is the reduced subprescheme of $X'$ having as underlying space the closure of $\bigcup_{\lambda \in L}
f'_{\lambda}(Z'_{\lambda})$, one has $Y' = Y \otimes_{k} k'$. In particular, $Y$ is geometrically reduced over $k$.*

As the $Z_{\lambda}$ are reduced, the morphisms $f_{\lambda}$ factor as $f_{\lambda} : Z_{\lambda}
\xrightarrow{g_{\lambda}} Y \xrightarrow{j} X$, where $j$ is the canonical injection `(I, 5.2.12)`. It results then from
`(11.10.4)` that $(g_{\lambda})$ is a schematically dominant family. Set $Y'_{1} = Y \otimes_{k} k'$, closed
subprescheme of $X'$, and let $g'_{\lambda}$ be the morphism deduced from $g_{\lambda}$ by extension of the base to
$k'$, so that $f'_{\lambda}$ factors as $Z'_{\lambda} \xrightarrow{g'_{\lambda}} Y'_{1} \xrightarrow{j'} X'$, where $j'$
is the canonical injection. It results from `(11.10.6)` that the family $(g'_{\lambda})$ is schematically dominant. But
by hypothesis the $Z'_{\lambda}$ are reduced, hence `(I, 5.2.2)` the $g'_{\lambda}$ factor as $Z'_{\lambda} \to Y' \to
Y'_{1}$; one concludes therefore from `(11.10.2)` that $Y' = Y'_{1}$ and $f'_{\lambda} = g'_{\lambda}$, which
establishes the corollary.

**Definition (11.10.8).**

<!-- label: IV.11.10.8 -->

*The notations being those of `(11.10.5)`, suppose that $X$ is an $S$-prescheme. One says that $(f_{\lambda})$ is
**universally schematically dominant (relative to $S$)** if, for every base change $S' \to S$, the family
$(f'_{\lambda})$ corresponding to the base change $X' = X \times_{S} S' \to X$ is schematically dominant.*

When $S$ is the spectrum of a field, prop. `(11.10.6)` thus means that a schematically dominant family is universally
schematically dominant (relative to $S$).

When the $f_{\lambda}$ are canonical immersions $Z_{\lambda} \to X$, one will also say that the family of subpreschemes
$Z_{\lambda}$ is **universally schematically dense in $X$ (relative to $S$)** instead of saying that the family
$(f_{\lambda})$ is universally schematically dominant (relative to $S$).

**Theorem (11.10.9).**

<!-- label: IV.11.10.9 -->

*The notations being those of `(11.10.5)`, suppose that $X$ is a locally Noetherian $S$-prescheme and that the
$Z_{\lambda}$ are all $S$-flat. For every $s \in S$, let $X_{s} = X \times_{S} \operatorname{Spec}(k(s))$,
$(Z_{\lambda})_{s} = Z_{\lambda} \times_{S} \operatorname{Spec}(k(s))$, $(f_{\lambda})_{s} = f_{\lambda} \times 1 :
(Z_{\lambda})_{s} \to X_{s}$. For the family $(f_{\lambda})$ to be universally schematically dominant relative to $S$,
it is necessary and sufficient that, for every $s \in S$, the family $((f_{\lambda})_{s})$ be schematically dominant.*

**Proposition (11.10.10).**

<!-- label: IV.11.10.10 -->

*Let $f : X \to S$ be a flat morphism locally of finite presentation, $U$ an open set of $X$. For $U$ to be universally
schematically dense in $X$ relative to $S$, it is necessary and sufficient that, for every $s \in S$, $U_{s} = U \cap
X_{s}$ be schematically dense in $X_{s}$ (or, equivalently, that one have $Ass(\mathcal{O}_{X_{s}}) \subset U_{s}$).*
